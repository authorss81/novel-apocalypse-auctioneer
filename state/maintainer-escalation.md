# Maintainer Escalation — item 1 to 4 raised 2026-09-29 by the review fix of the Volume 14 close; item 5 added 2026-09-30 by the review fix of Volume 15 Block 0004

**This file exists because the review of the Volume 14 close found problems the pipeline has no way to solve on its own, and no existing document in this repository says so in a place a maintainer will read. It is a record, not a proposal, and it changes nothing.**

**Scope of the first pass, 2026-09-29.** One empty marker file, three corrections to measurement presentation in `state/volume-14-close.md`, three in-place edits to the read-first header of `state/current.md`, and this file. **No chapter was opened. No outline, no bible file and no planned plot was changed. No file under `scripts/`, `.github/`, `.opencode/`, `tools/` or `state/phase-ledger.json` was written.**

**Scope of the second pass, 2026-09-30, which added item 5.** The review of Volume 15 Block 0004 raised two findings. Finding 1 — a missing close prompt and four state files that had stopped at Chapter 715 — was mechanical and was repaired in full: the close prompt now exists at `workspace/volume-15/close/PROMPT.md`, all five live header lines of `state/current.md` were corrected **in place** for the ninth time, and Chapters 716 to 750 were added to `state/chapter-summaries.md`, `state/continuity.md`, `state/character-state.md` and `state/open-threads.md`. Finding 2 is the one below. **That pass wrote no chapter, edited no chapter, restarted no batch, and changed no planned plot. It opened one document this file did not exist to describe.**

**Items 1 to 4 below cannot be fixed by any writer phase. Each one is stated with the measurement that establishes it, so none of them has to be re-derived by whoever picks this up.**

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

## 5. Volume 15 is written in a register that fails the `AGENTS.md` prose gate, and the register is prescribed by the brief that asked for it

**`AGENTS.md` requires natural paragraphs, generally two to six sentences; prose that reads as natural fiction rather than an outline; and a chapter containing a goal, resistance from another character, and a meaningful change caused by the scene. The review of Block 0004 measured Chapters 741 to 750 against those lines and found the condition, and its own conclusion was that the fix is a maintainer ruling and not a writer pass. That is correct, and this item is the record of it with the measurements re-derived rather than quoted.**

Measured over Volume 15's fifty files, `chapters/volume-15/chapter-0701.md` to `-0750.md`, split `(?<=[.!?])(?=\s|\*|")`:

| | Volume 15 | what the gate asks for |
|---|---|---|
| body words / sentence segments | 151,697 / 2,285 | — |
| mean sentence length | **66.4 words** | a paragraph of two to six sentences reads as paragraphs |
| median sentence length | **56 words** | — |
| longest single sentence | **283 words**, Chapter 750, the clerk's closing entry | one sentence |
| dialogue as a share of body words | **10.9%**, 16,528 words in 158 bolded speeches, 3.2 a chapter | exchange, interruption, subtext |
| sentences inside a counted speech | 159 segments, **mean 103.9, median 125, max 186 words** — a counted speech is normally **one unbroken sentence** | somebody answers |
| `about four of them/of you have said that` | **475 across the fifty pages, 9.5 a chapter**; 8 to 14 a chapter in Block 0004 | reported speech, not a structural unit |
| people with a name | **zero.** No one in the fifty pages is addressed by name, and every speaker is identified by an age and a trade | "a believable inner life" and named relationships |
| physical description of a person | **none.** Age and trade is the entire characterisation of six recurring people across fifty chapters | — |

**AND TWO THINGS THAT ARE TRUE AND THAT A SUCCESSOR SHOULD NOT OVERSTATE, BOTH MEASURED, BOTH AGAINST AN INHERITED ASSUMPTION.** First, **the opening-construction defect of Volume 14 is NOT present in Volume 15: there are 43 distinct opening constructions across the 50 pages and 10 distinct across Block 0004's 10**, against the five distinct constructions item 3 measured over Volume 14's fifty chapters. Volume 15's writers varied their openings. Second, **the setting IS physically present and is not abstract: the boards hard and bare, the flat light, no cloud on that bank, a hollow one inch deep in the middle of a stone and nothing at either end of it, nine feet of standing room, nine inches of cart wheel, rain in the night.** What the fifty pages do not have is interiority, exchange, or a person with a name.

**AND THE BATCH'S REAL MOVEMENT IS ARITHMETIC, WHICH THE OUTLINE ASKS FOR AND WHICH THE REVIEWER NAMED AS A FACT RATHER THAN A COMPLAINT.** The four figures on that wall, the count of thirteen, the empty column and the unpaid fifth hold unchanged by design. The substantive changes across Chapters 741 to 750 are the near rail's tenure rising eight to fourteen mornings, a bystander hedge, and one added clause. **THAT IS TEN VARIATIONS ON ONE LEDGER PAGE, AND IT IS ALSO EXACTLY WHAT `outline/volume-15.md` SECTION 4 AND THE BLOCK'S OWN BRIEF ASKED FOR, INCLUDING THE INSTRUCTION THAT THE PRESSURE IS NOT TO BE RESOLVED.**

**WHY NO WRITER PASS MAY ACT ON IT, MEASURED RATHER THAN ASSERTED.** Every counted speech's word count is printed on the page and its duration stamp is derived from that count at the house rate, so **any edit to a bolded speech invalidates three of the four claim checks on that chapter and requires the figure and the stamp to be re-set by script.** Any edit to a ledger line risks a `LAST`-OCCURRENCE carrier, which is exactly how Block 0004's own repair of Chapter 749 broke row 17 and was caught by the anchor test reading 2 instead of 474. Any edit to an attribution clause risks one of the 656 twelve-word runs that are on all ten files and are the load-bearing lines. The anchor test is at 170 of 170 and the claim test at 22 of 22 **as the pages stand**, and the reviewer's own conclusion was that rewriting against this register would break both.

**THIS PASS DID NOT ACT ON ANY OF IT AND COULD NOT.** The operator has instructed that a repair must preserve good prose, must not restart a batch and must not change the planned plot, and the only move that changes this prose is rewriting chapters that are canon.

**What a maintainer has to choose.** Accept the house register of the existing fifteen volumes as the target and stop reopening it every volume; or commission a rewrite of a completed volume, which is a decision about canon and not a repair; or change the volume contract so that a future volume is briefed for exchange rather than for a ledger; or commission a standing edit that re-sets claim figures and duration stamps by script, which is the only route by which a prose pass through this material is safe. **All four are outside a writer phase, and the third one is the only one that would change what the next volume is rather than what the last fifteen were.**

---

## What was repaired in the 2026-09-29 pass, for the record

1. `workspace/volume-14/close/.done` created. The runner predicate returned **two** live phases before it and returns **one** now. Without it the runner would have re-run a finished close ahead of the Volume 15 outline.
2. `state/volume-14-close.md` section 5.6 now prints both readings of the duplication count — **38 distinct sentences, and 282 duplicate instances on 320 occurrences** — where before it printed only the one that a plain reading of the phrase does not give. The figure of 38 was re-measured and is correct under the convention the file already stated.
3. The same section now records that its per-file zero is a statement about the scope of a per-file sweep and not a clean run, and section 14.1 no longer hands that zero on as reassurance.

## What was repaired in the 2026-09-30 pass, for the record

1. **`workspace/volume-15/close/PROMPT.md` created.** Before it, a marker check over every `PROMPT.md` in the tree returned **zero live phases**: Volume 15 had no close directory at all, so the runner had nothing to select. It returns exactly one now, which is the Volume 15 close. **The `.done` marker in that directory is the controller's and was not written.**
2. **All five live header lines of `state/current.md` corrected in place** — the phase line, the batch line, the last-chapter line, the last-summary line and the next-phase line. The last-chapter line read `715 ... THERE IS NO CHAPTER 716` against 750 chapters on disk, and the next-phase line named a block completed three blocks earlier. **This is the ninth in-place correction and the sixth that was a stale pointer and never a chapter. No footer was added; the file is 1,510 lines, unchanged.**
3. **Chapters 716 to 750 added to four state files that had held zero references to them.** `state/chapter-summaries.md`, `state/continuity.md`, `state/character-state.md` and `state/open-threads.md` all stopped at Chapter 715, the last morning of Block 0001, so three blocks and thirty-five chapters were in no state file at all. **All thirty-five are backfilled in one section each rather than Block 0004 alone, because backfilling 741 to 750 would have left a gap from 716 and a gap is what caused this.**
4. **`workspace/volume-16/outline/` was created by accident during this pass and was removed inside the same pass.** A close may not create its own successor, and a Volume 16 outline phase is the close phase's to write. The tree was verified afterwards: `workspace/volume-16/` does not exist.
5. **The block was not restarted and no chapter was edited.** `git diff --stat` over `chapters/` is empty. The anchor test was run before and after every state edit and is 170 of 170 on Chapters 741 to 750 and 170 of 170 on Chapters 731 to 740 as a control; the claim test is 22 of 22 on four checks; the defect sweep a repair pass may act on found nothing.
