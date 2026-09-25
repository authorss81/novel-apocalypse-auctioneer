#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
mkdir -p logs

PRIMARY="${NOVEL_MODEL:-opencode/space-bunny-free}"
FALLBACKS="${NOVEL_FALLBACK_MODELS:-opencode/muse-spark-1.3-contributor-free,opencode/muse-spark-1.2-contributor-free,opencode/nemotron-3-ultra-free,opencode/nemotron-3.5-lightning-free,opencode/mimo-v2.6-flash-free,opencode/ling-3.0-flash-fin-free}"

if [ -z "${OPENCODE_API_KEY:-}" ]; then
  echo "OPENCODE_API_KEY is missing" >&2
  exit 2
fi

phase_dir=""
while IFS= read -r prompt_file; do
  candidate="$(dirname "$prompt_file")"
  if [ ! -f "$candidate/.done" ] && [ ! -f "$candidate/.blocked" ]; then
    phase_dir="$candidate"
    break
  fi
done < <(find workspace -name PROMPT.md -type f | sort)

if [ -z "$phase_dir" ]; then
  echo "No incomplete phase found"
  exit 0
fi

phase_id="$(basename "$phase_dir")"
prompt_file="$phase_dir/PROMPT.md"
log_file="logs/${phase_id}.log"
review_log="logs/${phase_id}.review.log"

printf '%s\n' "Running $phase_id" | tee "$log_file"

run_model() {
  local model="$1"
  shift
  set +e
  opencode run --model "$model" --agent novel-writer "$@" >>"$log_file" 2>&1
  local code=$?
  set -e
  return "$code"
}

model_list=("$PRIMARY")
IFS=',' read -r -a fallback_list <<< "$FALLBACKS"
for model in "${fallback_list[@]}"; do
  [ -n "$model" ] && model_list+=("$model")
done

writer_ok=false
for model in "${model_list[@]}"; do
  if run_model "$model" "$(cat "$prompt_file")"; then
    printf 'Writer model used: %s\n' "$model" | tee -a "$log_file"
    writer_ok=true
    break
  fi
  if grep -qiE '429|rate limit|too many requests|quota|timeout|timed out|502|503|504|model not found|unavailable' "$log_file"; then
    printf 'Model unavailable or rate limited: %s\n' "$model" | tee -a "$log_file"
    continue
  fi
  printf 'Writer failed with a work error; not switching models.\n' | tee -a "$log_file"
  break
done

if [ "$writer_ok" != true ]; then
  touch "$phase_dir/.deferred"
  printf 'Phase deferred: %s\n' "$phase_id"
  exit 0
fi

set +e
opencode run --model "$PRIMARY" --agent novel-reviewer "Review the current batch and write concrete findings to your response. Read the current phase files and do not edit anything." >"$review_log" 2>&1
review_code=$?
set -e

if [ "$review_code" -eq 0 ] && grep -qiE 'finding|problem|issue|contradiction|repetition|outline-like|meta' "$review_log"; then
  set +e
  opencode run --model "$PRIMARY" --agent novel-writer "Read the reviewer findings in $review_log. Apply necessary fixes to the current batch and state files. Preserve good prose, do not restart the batch, and do not change the planned plot." >>"$log_file" 2>&1
  fix_code=$?
  set -e
  if [ "$fix_code" -ne 0 ]; then
    printf 'Review fix failed; leaving phase for retry.\n'
    touch "$phase_dir/.blocked"
    exit 1
  fi
fi

touch "$phase_dir/.done"
rm -f "$phase_dir/.deferred" "$phase_dir/.blocked"

git config user.name "novel-fleet-bot"
git config user.email "novel-fleet-bot@users.noreply.github.com"
git add -A
if git diff --cached --quiet; then
  echo "No changes produced"
else
  git commit -m "novel: complete $phase_id"
  git push origin HEAD
fi

if [ -n "${GH_TOKEN:-}" ]; then
  gh api -X POST \
    -H "Accept: application/vnd.github+json" \
    "repos/${GITHUB_REPOSITORY}/dispatches" \
    -f event_type=novel_tick \
    -f "client_payload[phase]=${phase_id}" \
    -f "client_payload[run_id]=${GITHUB_RUN_ID:-local}" || true
fi

echo "Completed $phase_id"
