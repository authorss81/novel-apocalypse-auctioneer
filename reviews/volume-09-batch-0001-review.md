# Volume 09 Batch 0001 Review Record — *The Empty Lot*, Chapters 391–400

Audit history for the first prose block of Volume 09. This file records what the review found, what was repaired in the prose, what was repaired in the state, and what belongs to the pipeline owner rather than to a writer. It is not story state. The handoff a writer needs is `state/volume-09-batch-0001-summary.md`, whose section 13 carries the same repair record where the next writer will actually see it; the full prose measurements are at `state/current.md` section 19.3 and the standing defect rows at `state/open-threads.md` section 23.4.

## How this batch was reviewed

One pass, and it was not an independent one. `scripts/novel_runner.sh` runs the audit with `--agent novel-reviewer`, but `.opencode/agent/novel-reviewer.md` declares `mode: subagent` and opencode refuses it and falls back to the default writer agent. The fallback is the first line of the run log:

```
logs/batch-0001.review.log:1  ! agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent
logs/batch-0001.review.log:3  > novel-writer · space-bunny-free
```

So the prose was reviewed by the agent that wrote it minutes earlier, which is the same condition that was recorded for the first prose batch of Volume 01 and the same condition under which the inherited counted-claim mismatch at Chapter 373 survived fifty chapters. **The finding below that took three phases and four hundred chapters to surface is the argument for fixing the dispatch, and no amount of care inside a self-review substitutes for it.**

## The headline

**The numeric engine worked and the sentences did not.** Every constraint the phase prompt set was met. The chapter failed `AGENTS.md`'s prose standard badly enough that it was not publishable, and the block's own record said so in advance: `state/current.md` printed *a figure that reproduces is not a chapter that is sound* in the same section that printed twenty-one reproducing figures. The block did not act on it. This review did.

| Measured on Chapters 391 to 400 | As the writer phase left it | As the chapters stand now |
|---|---|---|
| Narration sentences | 324 | 780 |
| Mean words per sentence | 71.9 | 25.9 |
| Median words per sentence | 60 | 24 |
| Longest sentence | 209 words | 72 words |
| Sentences of 100 words or more | 96 | **0** |
| Sentences under ten words | 13 | 152 |
| Sentences carrying four or more *and* | 171 | 67 |
| *that yard* | 194 | 22 |
| *about four people in that yard said* | 37 | 0 |
| Lines carrying spoken dialogue | none | 156 |
| Openings of the inherited shape | 2 of 10 | 0 of 10 |
| Shared twelve-word runs | 857 (and 811) | 628 |
| Class-one claims, and mismatches | 20, and 0 | 20, and 0 |

**What was added is exchange, interiority and physical ground. What was cut is the chaining of clauses. No beat moved, no date moved, no figure moved, and the twenty counted claims and the thirty-seven bolded set pieces were not touched at all**, because a counted speech is a document and a document is not prose. That is why the claim column did not move while the denominator, the word count and the run count all did.

The three places the machinery was not driving were the good ones and they were kept and are still good: the boy who goes down the bank into the ditch and brings back no figure (392), the hand that does not close on the edge of a table (393, 400), and the forearm that takes six seconds where it took a second and a half (399).

## The prose repair, chapter by chapter

Every chapter was rewritten in its narration. The spine of each — the figures, the count, the cost, the standing column, the figure on the sheet at that gatepost, the last image of 400 — is the spine the canon card sets out.

- **391** now opens on frost coming off the boards and a man who lifts his hand off them at nine and puts it back, and the man of fifty-six's disclosure is met by four lines of yard talk about the difference between not knowing and refusing to guess, which is the argument the chapter was making in one clause. The protagonist's nine feet gets its reason: six feet is being asked something. The hour of counting back the marks is now a scene with two men in it, one of whom says a board counts days and has never once counted a month on it.
- **392** is the chapter with the boy in the water, and it is the chapter the review's date defect was in. The two evenings ago, the chair, the loam man who walks nine feet to look at the water and comes back and speaks, and the boy who goes down on his own are all still here; the difference is that the man of fifty-six now answers the report about the chair by saying nothing at all, which the ledger then records, and the reader can see it.
- **393** has the sixty-one days, the three things that can be done with a book in the open, and the hand that will not close. The mender's three things are asked for twice and given twice in the same words, and the yard's objection to the third one arrives before he can get there. The protagonist's fear is met by an accusation he does not deny and by a hand that goes further into a coat.
- **394** has the rule and its price and the counting dispute. The mender's rule is asked for again, is not the same words, and the clerk shuts her page at half past four and gives a reason, and the reason is now a scene with four people asking her why.
- **395** has the two buckets. The woman of fifty-eight comes down the bank, fills them, carries them up the first go, turns round and comes back down to the table, and reads the two lines with her hand on the boards. That beat was always the best thing in the block and it is now the centre of the chapter rather than a paragraph in it, and the mender's nine feet down a lane with a sheet in his hand, and the four people who say to each other, not to him, that they would have asked her.
- **396** has the man with the cart and the four days in a week. Two men now argue the eighty against the two hundred out loud for nine minutes and the mender stops them in four seconds with a reason.
- **397** is the thing on the end of that table seen from four feet back, and the stone moved an inch. The stranger's eye is now rendered as a man standing four feet back and looking, and the boy reading nine headings and refusing to guess which line is current.
- **398** is the six things nobody is asking for, and a man's left hand that does not go the way he sends it in front of about nine people who say nothing.
- **399** is the man at the foot of the wall, the good evenings said to each other instead, the child's hand through the gap, and the six seconds.
- **400** is four things in one yard and a clerk refusing to tell a month its own length, and it still ends on the ditch over the low wall, out of sight of everybody standing at that table.

## The concrete defects, and what was done with each

1. **The chair date was off by one, and the prose was self-contradicting.** `chapter-0392.md` fell on the twentieth and said *yesterday evening the man of fifty-six had sat down in a chair at the end of that table and had got up out of it and had gone up that lane*, which put the sitting on the nineteenth, contradicted the canon card, contradicted `chapter-0396.md`, and contradicted `chapter-0391.md`, where the man of fifty-six is at the table with his hand flat on the boards from half past eight to dark and never sits. The true day is the eighteenth, the last day of Volume 08, where at about half past six he looks at the second chair for about a second and a half and sits down in it and nobody counts how long he is in it. **Repaired in the prose: it now reads *two evenings ago*, and the false clause about his going up the lane afterwards is gone, and nobody has said a word about the chair since the eighteenth.**
2. **Three sentences told the reader how the page was made.** `chapter-0397.md`, `chapter-0398.md` and `chapter-0399.md` each ended a sentence with *and the count is eighty-six / seventy-three / seventy-six because that is what is printed there.* That is a statement about the artifact and not about the yard, and `AGENTS.md`'s gate on meta language is not a matter of degree. **Repaired: the three clauses are gone, the counts stay in the prose in the ordinary form, and all three claims still reproduce.** A fourth instance of the same sentence was sitting in `state/chapter-summaries.md` and was repaired there too, because a handoff file that teaches the habit teaches it twice.
3. **The canon card contradicted itself on one figure.** Section 2 of `outline/batches/volume-09-batch-0001.md`, the prose, `state/current.md` and `state/continuity.md` all give the man of about sixty-four ninety days in this district at Chapter 391, and the card's own table of people gave ninety-first. The card's rule is that where a chapter and the card disagree the chapter is canon and the card is corrected. **The card is corrected, with the error named in the cell, and the prose was not touched.**
4. **Four self-measurements in the state files described a draft.** The denominator, the `wc -w` total, the per-chapter word column, the shared-run count and the clerk-entry share in `state/current.md` and `state/open-threads.md` were all measured before the block's own clerk-share repair, and the block record had a second, later set. **All five are now the figures the chapters actually produce, and the figures they were before are printed beside them, in all three files.** A stale self-measurement is the specific defect that makes a later phase trust a record it should have measured.
5. **Two character-state day-counts were wrong against the chapter files.** The road keeper was recorded as coming up that lane on seven of the ten days and he is in ten of ten. The reed cutter was recorded as being in that ditch on all ten days and he is absent from Chapter 395 entirely. **Both entries are corrected with the measurement beside them, and nobody was put into a chapter to satisfy an entry.**
6. **The next phase inherited an all-prohibition prompt and four stale measurements.** `workspace/volume-09/batch-0002/PROMPT.md` is roughly 50 KB and almost entirely a list of things not to do, with no guidance on constructing a scene, on sentence rhythm, or on dialogue, and it inherited the repetition figure, the clerk-share figure and the opening-shape figure as its baseline. **A scene section was added at the front of its craft brief — nine binding items on the sentence, the exchange, the room, the openings, the short forms, the *about* hedge, and the ban on describing the page — and the three stale figures were replaced with the current measurements and the earlier ones printed beside them.**
7. **The next phase also inherited the defect as an inherited instruction.** Its opening-shape item listed the last block's ten openings and said two of the ten are of the inherited shape, which was true when written and is not true now, and its repetition item printed 857 as the figure to beat. Both now carry the current figures and the history.

## Adjudicated and not actioned

**The forward risk in the month arithmetic is a misreading and the plan is right.** The review held that the switch of the third month from seven months back to eight months back on the first of the eleventh is eight days wrong, on the strength of the twenty-fourth of March to the first of November measured against an average month of 30.44 days. The volume counts months as months. From the fifth of the tenth the third month is seven months back, and from the first of the eleventh it is eight, and both are true, and `outline/volume-09.md` states both correctly. The day of the month on which the refusals last moved, the twenty-fourth of the third, is not part of either statement, and no chapter, no clerk's entry and no man in any yard says a day-count about how many months back anything is. **Nothing was changed for this finding, and the reasoning is now printed in `state/volume-09-batch-0001-summary.md` section 13 item 6 and in the review log, so that a fourth phase does not raise it again and change the plan to satisfy a miscount.**

## What is sound and was left alone

- **The figure arithmetic.** All eighteen columns re-derived for `b` = 50 to 59 against their own anchors. Every printed value matches, the cross-year trap on the siding was derived correctly and avoided, the stay figure agrees with the prose at ninety and ninety-nine, and the two figures that land on one interval are still distinguished from each other.
- **The guardrails.** *The eleventh month*, *unchecked*, *eight months back*, *a third line*, *a third reader*, *the office*, *two walls*, *fourth line*, *the departure*, *eleven words* and *a foot and a half* are all at zero across the ten chapters, measured. Zero panels, zero reserved-list hits, zero duplicated paragraphs of twelve words or more, no all-caps footer line anywhere, zero markdown, unit or weekday integrity issues, and the bare words *volume*, *block* and *batch* at zero.
- **The counted motif.** Twenty class-one claims, zero mismatches, the per-chapter column 2, 2, 2, 3, 2, 2, 2, 1, 1, 3, and every claim printed beside the printed sentence it counts.
- **The not-asking bookkeeping.** The broader reading of the ceiling, which counts *cannot be counted either way* together with *the record about the not asking says not asked*, gives 2, 1, 2, 0, 3, 0, 0, 4, 2, 0 across the ten days. Chapters 395 and 398 are over that broader ceiling. **They were over it when the writer phase ended, the column is identical before and after this repair, and they have not been drawn down**, because the not-asking is what this block spends and a repair that removed it to satisfy a wider reading of the block's own ceiling would be the opposite of a repair. The column and the decision are both printed.

## Open for the owner, not fixable by a writer

These are pipeline defects, not manuscript defects, and they are recorded here for the same reason they were recorded for the first batch: the writer is forbidden from editing `scripts/`, `.github/workflows/`, `.opencode/agent/`, `opencode.json` and `state/phase-ledger.json`, and a maintainer reading only the manuscript would never know they exist.

- **The review phase is not an independent review.** Same defect as the first batch, and the reason this block's prose went three phases and four hundred chapters without anyone noticing that it was a transcript with figures in it. Promote the reviewer to a primary agent or invoke it through a supported path.
- **`state/phase-ledger.json` is dead state.** It still reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0` after four phases of Volume 09, while the self-dispatch workflow selects work from `.done` markers. Reported by every phase since the third and not repairable here.
- **`scripts/novel_runner.sh`'s `ensure_next_phase` has no concept of a batch or a volume close.** It writes a generic continuation stub. Every `batch/PROMPT.md` and every `close/PROMPT.md` in this repository was created by a writer's commit, and the runner's "one next phase" rule is satisfied by accident rather than by design.
- **A tracked bytecode file.** `tools/__pycache__/measure.cpython-312.pyc` is tracked in git, was modified by the writer phase's commit, and `.gitignore` has no `__pycache__` or `*.pyc` rule. Untracking it is a git operation and adding the rule is outside the fiction and state files a writer may touch, so it is reported rather than done. It is a symptom: the measurement tool is imported by writers through a wrapper, and the wrapper leaves bytecode in a tracked path.

## Deliberately not changed

- **The plot.** No beat, no date, no figure, no column, no cost and no ending moved. Chapter 400 still ends on a ditch with standing water in it seen over a low wall, and the volume's final image remains fixed at `outline/volume-09.md` section 10.5.
- **The bolded set pieces.** All thirty-seven are byte-identical to what the writer phase produced, because a counted speech is a document. The repair is the prose around them.
- **The three places the machinery is not driving.** The boy in the water, the hand that will not close, the forearm that takes six seconds. They were the best writing in the block and they are untouched.
- **The ending, the amendment, and the antagonist.** The protagonist's name is still on no page and is still unsettled; the volume's answer to it is Chapter 429 and nothing here pre-empts it; the antagonists of this volume are still a count, a habit and two dates, and none of them has acquired a face.
