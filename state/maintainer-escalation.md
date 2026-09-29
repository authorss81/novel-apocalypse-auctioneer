# Maintainer Escalation — raised 2026-09-29 by the review fix of the Volume 14 close

**This file exists because the review of the Volume 14 close found a problem the pipeline has no way to solve on its own, and no existing document in this repository says so in a place a maintainer will read. It is a record, not a proposal, and it changes nothing.**

**Scope of the pass that wrote it.** One empty marker file, three corrections to measurement presentation in `state/volume-14-close.md`, three in-place edits to the read-first header of `state/current.md`, and this file. **No chapter was opened. No outline, no bible file and no planned plot was changed. No file under `scripts/`, `.github/`, `.opencode/`, `tools/` or `state/phase-ledger.json` was written.**

**Four items below cannot be fixed by any writer phase. Each one is stated with the measurement that establishes it, so none of them has to be re-derived by whoever picks this up.**

---

## 1. The planned ending is unreachable, and no phase in the current design is permitted to say so

**`outline/ending.md` requires Adrian to accept Iven's mark, to auction the right to administer the Tally with no single buyer, to sign as first bearer of a one-time founding toll that burns out his mark, and to end beside Mara in Alder Reach beside a brass bell in a public market. `AGENTS.md` requires preserving the planned ending.**

`Adrian` appears in **89 chapter files, all in Volumes 01 to 04, the last at Chapter 162.** He has been off the page for **538 chapters.** He is not in Volume 14, not in `state/volume-14-roll-summary.md`, and not in the Volume 15 prompt except as a liability to be deferred again.

`outline/series.md` still plans Volumes 15, 16 and 17 out to Chapter 840. On the current trajectory the manuscript passes the point where the ending can be reached and keeps going, with no phase holding the contradiction open.

**The close handles this correctly under its own constraints.** `state/volume-14-close.md` section 9 weighs the name once, refuses to invent a mechanism for it, and lists it as a liability. `workspace/volume-15/outline/PROMPT.md` correctly states that all three available moves are a maintainer's decision and forbids the outline phase from settling it. **Both documents are behaving as designed. The design itself is the problem, and the correct disposition of a close and an outline phase is to refuse, which is why this has now been refused five times without anyone being told.**

**What a maintainer has to choose.** One of: bring the protagonist back onto the page in a Volume 15 outline, with a stated mechanism and a stated chapter; re-scope `outline/ending.md` to the book actually being written; or stop planning to Chapter 840. **All three change the planned plot. No writer phase may choose among them and none of them is a repair.**

## 2. The five live state files cannot be loaded, and rotation has been deferred five times

`AGENTS.md` asks for summaries that are "compact and useful for the next batch" and says not to load the entire manuscript into every prompt.

| file | words |
|---|---|
| `state/chapter-summaries.md` | 74,012 |
| `state/character-state.md` | 71,358 |
| `state/current.md` | 59,860 |
| `state/open-threads.md` | 58,709 |
| `state/continuity.md` | 54,485 |
| **the five together** | **318,424** |

All of `state/` is **1,494,548 words against 2,136,462 words of chapters — roughly 41% of all prose in this repository is commentary about the prose.** `state/current.md` alone is 59,860 words and its own header tells the reader not to read it to the end. **22,246 of its words are set in capitals, 39.8% of the file, and that density is file-wide rather than confined to the header.**

Rotation to `state/archive/` is precedented twice — `state/archive/current-through-volume-09.md` and `state/archive/open-threads-through-volume-09.md` both exist — and the boundary rule is already written down in `state/open-threads.md`. **It has been declined on the grounds that deleting canon is riskier than a large file, five times now. This pass compressed the read-first header, removed one duplicated account of the file's own maintenance history from it, and pointed the header here. It did not rotate, because rotation deletes hundreds of kilobytes of state text and that is a maintainer's call, not a repair pass's.**

**What a maintainer has to choose.** Rotate the five files at the volume-13 boundary using the existing precedent and filenames, or accept the size and stop reopening the question every pass.

## 3. Volume 14 is not prose by the standards in `AGENTS.md`, and the only fix is a rewrite that is forbidden

`AGENTS.md` requires six structural beats per chapter, of which "resistance from another character" and "a meaningful change caused by the scene" are **absent by design** across Volume 14.

- **Five distinct opening constructions across fifty chapters**: 28 open "There was no rime on the boards of that second table on", 14 open with the same construction on the first table, 6 open "There was a hard white rime", 2 are singletons.
- **Live speech has fallen by 58% over the same nominal scene structure**: 233 stamped speech durations in Volume 13, 99 in Volume 14.
- **The volume's own repetition is structural, not incidental**: 38 distinct sentences of twelve words or more appear whole and identical in two or more of the fifty chapters, on 50 of 50 — 4 of them on 35 files each, one on 32. The cart with the dragging wheel is on all 50 files and byte-identical on 35 of them.
- No reserved string from the series premise appears on any of the fifty pages.

**This pass did not act on any of it, and could not.** The only move that changes the prose is rewriting chapters that are canon, which a close and a repair pass are both forbidden to do and which the operator has instructed must not be done. The batch was not restarted. The finding is recorded here instead, with the measurements attached, so that the decision is available to whoever is entitled to make it.

**What a maintainer has to choose.** Accept the house style of the existing volumes as the target, or commission a rewrite of a completed volume, or change the volume contract. **All three are outside a writer phase.**

## 4. Two smaller items that are not a writer's to touch

- **`state/phase-ledger.json` still reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0` after 700 chapters and roughly fifty phases.** It is controller-owned and was not opened. Note that `AGENTS.md` instructs writers to update the phase ledger while the phase prompts and the operating instructions forbid it. **That contradiction should be resolved in one of the two documents rather than left for the next agent to find at runtime.**
- **`tools/measure.py` returns `None` for every numeral above a hundred written the ordinary way, because `words_to_num` drops any numeral containing `and`.** Four volumes have now hand-rolled a replacement inside a workspace directory. This is a tooling defect being paid for in writer phases on every volume.

---

## What was repaired in this pass, for the record

1. `workspace/volume-14/close/.done` created. The runner predicate returned **two** live phases before it and returns **one** now. Without it the runner would have re-run a finished close ahead of the Volume 15 outline.
2. `state/volume-14-close.md` section 5.6 now prints both readings of the duplication count — **38 distinct sentences, and 282 duplicate instances on 320 occurrences** — where before it printed only the one that a plain reading of the phrase does not give. The figure of 38 was re-measured and is correct under the convention the file already stated.
3. The same section now records that its per-file zero is a statement about the scope of a per-file sweep and not a clean run, and section 14.1 no longer hands that zero on as reassurance.
