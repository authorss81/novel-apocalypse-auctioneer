# Phase Review — volume-06 batch-0003 (Chapters 271–280)

**Scope reviewed:** commit `8183e6a` "novel: save writer work batch-0003" — ten chapters, one canon card, six state files and the Batch 0004 handoff prompt. The review phase read the phase out of git and edited nothing; this file was written by the repair pass that answered it. `state/phase-ledger.json` is controller-owned by Actions and was not touched.

**Reviewer note, and it is a real limitation of this gate.** `logs/batch-0003.review.log` line 1 records `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent.` The review therefore ran on the same model that wrote the batch. That is a property of the runner in `scripts/`, and this phase may not edit it. It is disclosed here rather than left for someone to find. **The useful thing about it is that the review re-ran the writer's own checks and agreed with every one of them, and then found seventeen things the checks cannot see. A second reader looking for contradictions rather than for numbers was worth more than a second reader looking for numbers.**

This file is the audit history for the batch. It is not story state. The handoff a writer needs is `state/volume-06-batch-0003-summary.md`; the repair itself is itemised at section 5A of that record.

---

## 1. What verified clean, run rather than read

- **All 32 class-one spoken-span counts reproduce exactly**, before and after the repair, using `tools/measure.py` through a wrapper that imports the module and calls its own functions. Zero drift both times.
- **All 5 class-two `in N words` spans reproduce exactly** — 10, 15, 61, 16, 74.
- **The reserved-term scan returns zero** for all 31 terms, and zero for the seven weekday names, and zero for metric and colon-times. The reviewer's first scan for *First House* and *Alder Reach* was too naive and it says so in the log; the claim holds.
- **Every day-ladder figure is internally consistent across all ten chapters** — board 179→188, train 495→504, unentered 209→218, second of January 170→179, removal 41→32, chair 59→68, six households 61→70, no-board-lines 82→91, ninth night 62→71, record-in-force 20→29. **Every ladder was correct and every one of the seventeen defects was somewhere else**, which is the finding this file exists to record.
- **Both printed documents reproduce the canon card character for character**, and the two reprinted walls at 273 diff clean against Chapter 259.
- **The block ends on a sheet in a lane, not on a declaration**, as the card requires.

Lengths, emphasis counts and the zero-panel result were all in band.

## 2. What was wrong, and the shape of it

Thirteen defects inside the new prose, four in the canon card, two craft findings, two process findings.

**The prose defects share one grammar, and it is worth stating because it is the whole lesson of this pass:** a sentence that names a **person, a place, a time, a measure, or an event** has to be checked against every *other* sentence that names it. It does not have to be checked against a ladder, a day-count, or a figure, because in this batch every one of those was right and every one of these was wrong.

| # | Finding | Shape |
|---|---|---|
| 1 | `chapter-0280.md:5` said the sixth month had two days left in it, on the thirtieth of a thirty-day month; lines 11 and 49 said the opposite twice. | **A chapter refuting itself inside itself.** |
| 2 | `chapter-0273.md:48` said the rope went into the hands of the woman of about thirty-one *and* that she was not in that yard; line 50 said the man who mends fencing. | **A failed splice of a sentence the card puts in a clerk's entry.** |
| 3 | `chapter-0274.md:51` put the scale keeper in her doorway for the whole nine-minute ringing; line 61 had her say she had been there two minutes and had never heard it. | **A person placed in a scene and then given a line that the scene forbids.** |
| 4 | `chapter-0276` ran 10 a.m. → 3:30 p.m. → 4:30 p.m. → **11 a.m.** → 6:30 p.m. `chapter-0278` ran 1:30 p.m. → **6 p.m.** → **4:30 p.m.** → 6:30 p.m. | **Scenes filed in the order they were written.** |
| 5 | `chapter-0276.md:21` gave a clerk's entry from the eighth of this month to *a man of about twenty-four years ago*. | **A quotation attributed to the wrong century and the wrong person.** `chapter-0258` and `chapter-0278` both had it right. |
| 6 | `chapter-0277.md:41` called nine inches tied to two feet of new rope *about a foot and a half*. | **A measure that contradicts a scene three chapters earlier.** |
| 7 | `chapter-0275.md:43` and `chapter-0276.md:15` both said *about nine hundred yards of lane*; the lane is two hundred. | **One wrong fact duplicated into two counted speeches, so both counts were correct and the fact was not.** |
| 8 | `chapter-0278.md:31` had the man of fifty-six claim the third-column argument he had heard another man make in a room the day before. | **A man taking credit in public for a private argument.** |
| 9 | `chapter-0280.md:15` said a board and a stool were proposed in the same two days; Chapter 272 has both in the same morning. | **A count paragraph misplacing an event.** |
| 10 | `chapter-0279.md:63` said both sheets were in one book; `chapter-0278` had the registrar refusing to put it in *that night*, and no page moved it in. | **A state of the world asserted with no decision on the page.** |
| 11 | `chapter-0276.md:61` promised *you will put your own hand underneath mine*; `chapter-0279.md:17` has her write it herself; `chapter-0280.md:41` says *I put my own hand under yours*. | **A promise made, undone by a body, and then reported as if kept.** |
| 12 | `chapter-0279.md:11` and `chapter-0280.md:17` said nine people gave a refusal with a reason; the card's own list of the eight is eight, and the prose carries all eight. | **An in-prose figure colliding with a standing count of the same name.** |
| 13 | `chapter-0280.md:33` invented that he had been wrong about four hundred and eleven for six weeks, that a woman of fifty-eight sat down on a step, and that he said so in a yard. | **A load-bearing beat relocated into an event no state file had ever recorded.** Chapter 269 has the step, the six weeks and the lane. |

Card defects, all of the class the card's own header promises to repair: four relative months that read as the fifth month where the prose says the sixth (finding 14), a refusal cited to a chapter that does not contain it (finding 16), and a row that announced two proposals and then listed five and called them six (finding 17).

## 3. What the repair did, and what it did not

Prose corrections in thirteen places across eight chapters. **Four class-one figures moved as a consequence and every one was re-measured on the printed sentence, not re-aimed:** 262→263 (misattributed quotation cut out), 172→169 (rope measure corrected), 176→193 (another man's argument credited to him), 175→185 (invented scene cut out). **No sentence was shortened to make a figure true and no figure was changed to fit a sentence.**

One scene was **moved and not re-timed** — the road keeper at 276, whose counted speech says *this morning* and whose card entry says the morning of the twenty-sixth. One document's entry was **put on the page** rather than asserted. The card was corrected in **nine** places, thirteen in total with the writer's own pass, and **no chapter was touched to meet the card, because the chapters were right.**

Not done: no chapter restarted, no scene cut, no date moved, no count that did not move changed, no clause added to raise a measurement, no thread closed, no panel added, the romance left unresolved, the rival record unanswered, the ninth charter's line and the third column of the covenant still empty, the nine names still unprinted, the bell not rung twice, the child not used again, and the ending untouched — a wrong sheet in a lane and a man who is not going to take it back out of a book.

## 4. The two craft findings

**The stock figures sentence had been verbatim identical in all twenty chapters from 261 to 270 and in all ten of this block, and the ledger's own instrument phrase stood a hundred times in the new ten.** The ten lead-in sentences of this block were rewritten as ten different sentences carrying the same two facts. **The identical-paragraph measure for this block went from one to zero, the first time in Volume 06, and a sweep for duplicated sentences of nine words or more went from one to zero. The two blocks before it were not touched**, and a reader crossing 270 into 271 will find a seam. That is disclosed in the record rather than papered over, because rewriting two finished blocks to hide a seam would be the worse lie.

**`chapter-0278.md:13` fused two injuries** — a voice that went on the twenty-fifth and a hand that has been bad since the thirteenth — into *had not been able to hold a pen above a whisper*. Split back into the two things they are.

## 5. The two process findings, which belong to the pipeline owner

1. **The review phase runs the same model that wrote the batch**, because `novel-reviewer` is a subagent and the runner falls back to the default agent. **This is a property of `scripts/novel_runner.sh` and of `.opencode/agent/`, both of which this phase is forbidden to edit, so it is recorded and not fixed.**
2. **`reviews/batch-0003-review.md` is a review of Volume 01 Chapters 21–30** and collides with the volume-scoped naming; Volume 06 had no review file at all, so the AGENTS.md gate "a reviewer has checked the result" was unmet for this phase. **This file is the volume-scoped record. The colliding file was left where it is**, because it is a true record of a different phase and deleting it would be the worse of the two errors. The pipeline owner may want to rename it.

## 6. The standing note for the next reviewer

**Read every sentence that names a person, a place, a time, a measure or an event against every other sentence that names it, separately from checking any ladder.** In this block the ladders were all right, the counts were all right, and seventeen things were wrong. **And read the canon card back against the chapters at the end of the block, not only at the start of it** — four of the seventeen were in the contract, and the contract is the document the next writer trusts most.
