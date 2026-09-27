# Review Record — Volume 06, Batch 0004 (Chapters 281–290)

> Audit history, not story state. The handoff a writer needs is `state/volume-06-batch-0004-summary.md`; the canon contract is `outline/batches/volume-06-batch-0004.md`. This file records what the review pass found, what it fixed in the prose, and what it corrected in the documents that describe the prose.

## What the pass was

A review of the writer's save commit for Batch 0004 (`f035fb9`, Chapters 281–290, the canon card, the four state files, the block record and the Batch 0005 prompt). Every mechanical figure in card section 10 was re-run with the repository's own `tools/measure.py` functions through a read-only wrapper in `/tmp`; nothing under `tools/` was edited.

**Scope discipline for the repair pass: prose inside Chapters 281–290 only, plus the documents that describe it. No chapter outside this block was edited, no controller, workflow, agent or dispatcher file was touched, `state/phase-ledger.json` was not read for write, and no next phase was created or removed. The batch was not restarted.**

## What reproduced exactly

The mechanical layer of this phase is sound. Everything the reviewer could independently re-derive, it re-derived:

- **25 class-one counting claims, class counts 3/2/4/2/4/2/2/2/2/2, 0 mismatches**, and the 25 figures in order of appearance matched the card digit for digit. 0 class-two claims.
- **Calibration on Chapters 241–250 reproduced** — 53 claims, counts 8/7/4/5/7/4/4/5/5/4, 0 mismatches, 25,569 / 25,689 / 675 runs.
- **All 48 rows of the frame table**, including the three earlier blocks re-measured on the current tree.
- **Every interval**, walked out of the seven month lengths: board, train, unentered days, second-of-January, chair, six households, board-days, rival record, pool of refusals, ninth of the nine nights, the ditch's twenty-three days, the removal ladder.
- **The relative months**, which the card named as its own top flagged risk. Every *last month* resolves to the sixth month; *the month after next* is retired in 281 and used nowhere else; *three months back* is correct in all three uses.
- **The Batch 0005 prompt's calendar**, all of it.

**The audit of the block was not the problem. The failures were concentrated in the layer the audits do not reach: three footers that disagree with their own chapters, one scene that opens mid-sentence, one refusal that exists only in a clerk's entry, one figure that moves without an entry, and one set of disclosures that describes something other than what is on disk.**

## The eighteen findings, and what was done about each

| # | Finding | Repair |
|---|---|---|
| 1 | `chapter-0289.md:22` — the second scene opened mid-sentence on a stranded *and*, with the woman of about thirty-one named only later in the same sentence. | Paragraph now opens with her as its subject. No scene cut, no count on that paragraph. |
| 2 | The "second hand-cart" refusal existed only in a clerk's entry at `285:47` and `290:23`. No character proposes one; the only *cart* in 285 is a table in a hand-cart in the convenor's speech. | Both entries rewritten to the one thing actually refused on the page, **a join** — the five lines and the four lines of print on one page, refused in about four seconds with a reason. The phantom withdrawn from **seven** files: two chapters, the card, the block record, `state/continuity.md`, `state/open-threads.md`, `state/current.md`, `state/chapter-summaries.md`, the Batch 0005 prompt. |
| 3 | Card section 5's instruments row contradicted itself and contradicted 290. | Row rewritten to 290's ledger: seven things, one refused, six entered. |
| 4 | Card section 11's baseline for *A clerk of nineteen years entered* was *a hundred and one*; measurement gives **a hundred**, and the stated rise of four only works from a hundred. | Corrected in the card and in `PROMPT.md`, which had inherited it. |
| 5 | Card section 10 printed **781** shared twelve-word runs for 251–260; it measures **780**. | Corrected in the card and the block record. |
| 6 | Card section 10's duplicate-sentence disclosure described a repair that was not the duplicate on the disk. The sweep returns a 27-word sentence in five consecutive chapters. | Disclosure corrected to the disk, and the five ledger lead-ins at 283/284/285/286/287 made into five different sentences. |
| 7 | A 31-word sentence was duplicated across the block boundary, 290 against 280, where a block-local sweep is blind by construction. | 290 rewritten. A re-run against 271–290 returned a **second** cross-boundary duplicate the original sweep could never have seen, a 28-word sentence shared by 282 and 275; also broken. Card section 10 re-specifies the sweep to cross the boundary. |
| 8 | Three footers disagreed with their own chapters, and the footer-support pass passed all three because it only checks that a number appears somewhere in the body. | `284:59` four days → **ten days**; `285:55` garble → **a join of five lines and four lines put on one page**; `289:42` **a reason for the first time in eleven years** → **a reason she had never given anybody, and eleven years of walking her lines**. The same eleven-years overclaim corrected out of four state files. |
| 9 | `289:26` attributed to the 288 room a line he never says there; *do not come and ask me again this month* is **her** instruction. | Rewritten to what he did say in that room. The chapter's title still stands. |
| 10 | A figure moved eight → nine across two consecutive chapters with no entry, and *by three women* was unsupported and collided with the standing nine of eleven-coppers refusals. | The move is real and continuous and is now entered at the point it moves, naming both women; the two nines are named as two different nines; *by three women* struck from both chapters and from `state/current.md`. |
| 11 | `state/open-threads.md` carried a corruption, *the MANNISH proof of it*. | **the PLAINEST proof of it.** |
| 12 | `PROMPT.md` said nine costs were paid and then listed five, one and one. | Seven, and the arithmetic is now shown: five and one and one is seven. |
| 13 | `state/current.md` and `PROMPT.md` named different fifth examples in the same list of twenty-two defects. | `state/current.md` corrected to the derivation, which is item 2 of the list; both documents now also carry the class of the review's own eighteen. |
| 14 | Card section 5 claimed an entry was made once in each of ten days; it is in six of the ten, because the block holds about three refusals with a reason and not eight. | Card corrected and the reason given. `PROMPT.md`'s *defended eight times against eight separate attempts* corrected, because an attempt is not a figure. |
| 15 | Card sections 5 and 6 merged two attempts on two different documents. | All three copies now given with the document each is of: the five lines carried two miles, the five lines stopped at two, and the four lines of print stopped at two. |
| 16 | `PROMPT.md`: *has lost the use of both hands in his own hands*. | *carrying a hand-cart eleven miles twice*. |
| 17 | Card section 11's read of the fall of *a bell* was stronger than the prose supports; one of the three occurrences is a live back-reference at 286. | Point rewritten to say the fall has one thread still attached to it. The bell is still not rung. |
| 18 | One night described two ways: `285:19` had an undecided *a man* in a doorway questioned by nine people, `282:53` had the digger counting nine people through one door, and 274 and 278 both put the digger in that doorway because the yard asked him to be. | 285's sentence brought into line with the other three. **The counted figure on that speech moved from a hundred and ninety-six to two hundred and twenty-three, re-measured on the printed sentence.** |

## What was deliberately not done

- **No chapter was restarted.** No scene was removed. No chapter's date moved. No count that did not move was changed. No thread was closed. **The ending of the block is untouched: a gate, in a lane behind a bank, that a man of about thirty-four who mends fencing does not know what it is yet.**
- **No figure was re-aimed.** The one counted figure that moved, moved because a sentence it sits on was corrected to name the man in the doorway, and it was re-measured on the printed words afterwards.
- **No measurement was added to or removed from any chapter to move a number.** Where a figure rose, it is disclosed: *clerk* went from 187 to 188 and its rate rose anyway on a denominator that fell, and the raw counts are printed beside the rates.
- **No chapter outside Chapters 281–290 was edited.** A sweep found the same ledger sentence still standing at 260, 270 and 280; that is disclosed in the card and the block record for a later phase and left alone here.
- **No new phase was created, and no existing phase was removed.** The Batch 0005 prompt at `workspace/volume-06/batch-0005/PROMPT.md` remains the single next phase and is not a Batch 0006 and not the volume close.

## Re-measurement after the last prose edit

Every length, denominator, run count and frame rate in the card and the block record was re-derived after the final edit, because a prose repair moves the word counts and a stale list is a defect and not a rounding.

| | Before the review repairs | After |
|---|---|---|
| `wc -w` block total | 25,196 | **25,391** |
| `wc -w` range | 2,332 – 2,870 | **2,365 – 2,870** |
| Batch 0005 denominator | 25,091 | **25,286** |
| Shared twelve-word runs | 1,135 | **1,138** |
| Class-one claims / mismatches | 25 / 0 | **25 / 0** |
| Identical paragraphs ≥ 12 words | 0 | **0** |
| Duplicated sentences ≥ 9 words, swept 271–290 | 1 seen | **0** |
| Bold clauses per chapter | 9/12/9/10/7/9/7/7/5/5 | **9/12/9/10/7/9/7/7/6/5** |
| Reserved terms / integrity / footer-support failures | 0 / 0 / 0 | **0 / 0 / 0** |

The only frame count that changed is **the bare word *clerk*, 187 to 188**, and it changed because one of the repairs put the word *clerk* into a sentence that previously had no person in it. Every rate in the table moved because the denominator moved, and both are printed.

## A nineteenth defect, found by the repair pass itself

**The all-caps restatement at the foot of Chapter 289 had never been closed.** Its two bold markers paired with nothing, so the chapter read one clause short of bold and nothing said so. **Neither the block's own markdown-integrity pass nor the review looked at it**, because the integrity pass counts doubled stops, doubled spaces, trailing whitespace, commas without a space and periods without a space, and an unclosed marker is none of those. It is closed, the bold-clause count for that chapter is re-derived from 5 to 6, and the figure is corrected in the card and the block record. **It is the same class as finding 8: a footer's own markup can be wrong in a way no number reports, and a footer has to be read.**

## The class, and what the next writer should take from it

**Fourteen of the eighteen were found by reading and none by a count. The three a count could have caught were caught by a count, and only after a sentence had been read.**

The rule the twenty-two defects of the writing pass taught was that a sentence naming a person, a place, a time, a measure or an event must be checked against every other sentence that names it, and not against a ladder. **The review adds the second half, and it is the same rule: a document that describes the prose is itself prose, and it goes wrong the same way.** Three of these eighteen are a footer, a clerk's entry and a frame baseline that were each internally consistent and each wrong against the thing they describe; six are a disclosure that names a thing the disk does not contain.

Three operational consequences, carried into `workspace/volume-06/batch-0005/PROMPT.md`:

1. **Sweep across the block boundary, not inside it.** A block-local duplicate sweep is blind by construction to a sentence that arrived from the chapter before. Two of the eighteen were invisible for that reason alone, and the second was found only by widening the window after the first was fixed.
2. **Footer-support is necessary and not sufficient.** It passed all three broken footers, because it checks that a number in the footer appears somewhere in the body, not that the footer's *sentence* agrees with the body. Read the footers.
3. **A correction is not a measurement.** Five of the seven corrections the writing pass made to its own card were incomplete or wrong, and one of them — the second hand-cart — put a thing into canon that no chapter contains and then propagated it into a standing state file and into the prompt for the climax block. **Re-measure a correction before you rely on it.**
