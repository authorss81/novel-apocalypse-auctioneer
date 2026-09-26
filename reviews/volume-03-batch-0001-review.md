# Phase Review — volume-03 batch-0001 (Chapters 101–110)

**Scope reviewed:** commit `f19d13d` "novel: save writer work batch-0001" — a review/repair pass over the ten chapters, one canon card, six state files and the Batch 0002 handoff prompt. Working tree was clean, so the commit was the phase. `state/phase-ledger.json` was untouched: it is controller-owned by Actions.

This file is the audit history for the batch. It is not story state. The handoff a writer needs is `state/volume-03-batch-0001-summary.md`.

## Pass 1 — audit after the prose

One prose defect was found and repaired in place, with no beat moved: **the registrar's speech in Chapter 102 opened and never closed**, so the chapter carried sixty-one quotation marks. The phase prompt's own script counts bold markers, which cannot see an unclosed speech, so the defect shipped in a batch whose hard check had passed. It was found only after a quotation-mark parity check was added. All ten chapters now carry an even number.

A set of checkable figures in the batch's own review-pass flags was also found not to reproduce on a word-boundary count, and was corrected. The batch summary's Review-pass flags now name every superseded value where it is superseded, because the convention in this repo is that a claim about prose must be checkable and an uncheckable claim is worse than no claim.

One claim in the canon card contradicted its own chapter and was corrected in the card, not the prose.

## Pass 2 — independent audit of pass 1, and the repairs it forced

The pass-1 corrections were re-measured from the files. Length, emphasis, headers, blockquote counts, the Chapter 102 repair, the bold-marker counts and every tic figure reproduced exactly. **Three classes of finding did not survive re-measurement**, and all three were the same defect in different clothes: a figure in a state file that a stated method did not return.

- **A stale paragraph directly beneath the one that had been corrected.** The repair updated the measurement record in `state/continuity.md` but left the tic paragraph below it carrying all six withdrawn figures. Three files then disagreed in adjacent lines.
- **A series that matched none of the possible methods.** The paragraph-shape percentages and the 508-of-697 total were quoted identically in three files under a method that did not say whether bold headers and quoted-speech paragraphs sat in the denominator. Three defensible readings of "non-quote paragraph" existed and each was being asserted as the only one. **The denominator is now defined once and the other two readings are recorded** so that a check reproduces whichever it runs. The Batch 0005 comparison, which had been withdrawn because the stated baseline did not reproduce, is restored: measured on the fixed definition the two batches are like for like, and this batch is about nineteen points higher.
- **A count that was corrected in two files and not the third,** and a neighbouring baseline off by one.
- **A carried-defect list that said seven and named nine,** two of the nine pointing at a chapter with no odd-marker line and no odd-marker paragraph. The two void references were deleted rather than renumbered.
- **A stale characterisation in `state/current.md`,** which still described the review flags as recording four measurement disagreements after the repair pass had superseded that description.
- **An overstated justification in `NOVEL_SPEC.md`.** It said the canon card claimed four lines where Chapter 108 says three. Chapter 108 says both numbers at different moments: three written on the fourth of August, a fourth added on the eighth. The card now records that the instrument stood at three when begun and **stands at four at the end of the batch**, which is the fact a later batch needs.

## Prose defects: one, and it is fixed

Chapter 102 only. **No other chapter was edited in either pass, and no plot beat was moved, cut or re-staged.** The audit found no structural failure: every chapter changes the situation, one System panel appears in the batch and it is in Chapter 103, the romance does not resolve and is not spoken about, and the ending creates forward pull without manufacturing a cutaway.

## Verified intentional — do not "fix" this later

**The blockquote `I DO NOT LIKE IT, AND I SAY YES.` stands at `chapter-0105.md:61` and again at `chapter-0106.md:27`.** It is one woman's standing answer, given in the same order every month since the twenty-ninth of March, and the second chapter says so in the paragraph that follows. The repetition is deliberate and load-bearing: a person who answers identically every month and is asked from a different room each time is the volume's argument about whether an answer is a decision. A duplicated-paragraph detector will flag it. It is now recorded in the batch summary's review-pass flags and in the Batch 0002 prompt so no later audit cuts it.

## Standing invariants, and the guard that protects them

Odd-marker paragraph counts are scoped, and a maintainer running the check across the whole repository will get a different number from the one the state files quote. **Volume 03 is zero. Volume 02 is exactly seven. Volume 01 is ten**, in Chapters 16, 40, 42, 43 and 45. All of them are carried and canon. **An unscoped run returns seventeen, not seven.** The Batch 0002 prompt now ships a guard loop that prints the per-volume counts by both paragraph and line, and fails loudly if Volume 02 is ever anything but seven.

## Left alone on purpose

- **`chapter-0070.md:15` and `:23` remain named in the prompts for three completed phases** — volume-02 batch-0004, volume-02 batch-0005 and volume-03 batch-0001. The references are void, and they are left in place because each file is the record of what that phase was actually told, and a completed phase's instructions are not to be rewritten. The live handoff is correct.
- **The odd-marker paragraphs in Volumes 01 and 02 are not repaired.** Both volumes are closed and canon. Fixing them would be a new phase, not a review.
- **The twelve-foot geography, the dates and the canon figures were not re-derived in this pass.** The date map and the closed numbers live in `state/current.md` and were not in scope.

## Open for the pipeline owner

- **The reviewer subagent never runs.** `.opencode/agent/novel-reviewer.md` declares `mode: subagent` while `opencode.json` sets `default_agent: novel-writer`, so opencode refuses it and falls back to the writer model. **Every review of this manuscript is the prose reviewing itself minutes after writing**, which is visible in the log's first line. This is the single largest weakness in the quality process and it is a pipeline change, not a writer change. It is also why pass 2 found things pass 1 did not.
- **`state/phase-ledger.json` still reads `phase-000-bootstrap` / `planned` / `attempts 0` / `range null` after 110 chapters.** Controller-owned by Actions; not a writer fix.
- **A figure that reproduces under one method and not another will keep appearing.** The cause is a method that is described in prose rather than carried in a script. The Batch 0002 prompt now states its methods explicitly and ships the check; a later phase should consider quoting the script's output rather than re-deriving the number by hand.
