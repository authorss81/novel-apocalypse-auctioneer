# Model Verification

Command run locally:

```text
opencode models
```

Free-tag models observed during verification:

```text
opencode/space-bunny-free
opencode/ling-3.0-flash-fin-free
opencode/mimo-v2.6-flash-free
opencode/muse-spark-1.2-contributor-free
opencode/muse-spark-1.3-contributor-free
opencode/nemotron-3-ultra-free
opencode/nemotron-3.5-lightning-free
```

Primary requested model:

```text
opencode/space-bunny-free
```

Approved fallback order for the first workflow prototype:

```text
opencode/muse-spark-1.3-contributor-free
opencode/muse-spark-1.2-contributor-free
opencode/nemotron-3-ultra-free
opencode/nemotron-3.5-lightning-free
opencode/mimo-v2.6-flash-free
opencode/ling-3.0-flash-fin-free
```

The production workflow must run `opencode models` before generation and record the actual model used for every batch. Model availability can change.

Fallback is permitted only for classified provider errors, rate limits, timeouts, or unavailable models. It is not permitted to hide writing, continuity, or review failures.
