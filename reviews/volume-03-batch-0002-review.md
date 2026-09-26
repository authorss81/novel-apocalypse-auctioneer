# Phase Review — volume-03 batch-0002 (Chapters 111–120)

**Scope reviewed:** a checkpoint audit over the ten chapters, the canon card, the state files and the Batch 0003 handoff prompt, run after the batch had been written and saved. `state/phase-ledger.json` was untouched: it is controller-owned by Actions.

This file is the audit history for the batch. It is not story state. The handoff a writer needs is `state/volume-03-batch-0002-summary.md`.

## The finding that matters

**The prose shipped with a hard check that passed and a set of claims about the prose that had drifted away from the files.** The phase prompt's own script — bold markers, doubled separators, quotation parity — returned clean, and it returned clean again here. The five figures that no longer reproduced were all measurements, and measurements are not what that script checks.

The worst of them was hiding a defect. The flags said *the longest single-sentence narration paragraph in the batch is 122 words, in Chapter 116, and nothing in that measure passes a hundred and thirty.* **Chapter 120 held one at 132.** The prompt sets a hundred and thirty as a ceiling for that measure and gives the remedy: break at the last clean conjunction and leave a paragraph break rather than a rewrite. It has been broken once, at the conjunction before *and a man of thirty-four who mends fencing has said in public*, into two paragraphs of sixty-eight and sixty-four words. **No sentence was changed, no word was added or cut, and no beat moved.** Chapter 120's word count is unchanged at 4,349 and its emphasis figure is unchanged at thirty-five point six, because a paragraph break is not a word.

## Prose defect: one, and it is fixed

Chapter 120 only. **No other chapter was edited, and no plot beat was moved, cut or re-staged.**

## Measurements that did not reproduce, and what replaced them

Every one is now a figure that reproduces under a stated method, and every superseded value is named and withdrawn in the line that supersedes it, in all four files that carried it: the batch summary, `state/continuity.md`, the canon card and the Batch 0003 prompt.

| Claim | Was | Is |
|---|---|---|
| Per-chapter length | 3,778 / 3,866 / 4,072 / 4,151 / 4,427 / 3,898 / 4,051 / 3,889 / 3,946 / 4,315 | 3,695 / 3,865 / 4,087 / 4,013 / 4,415 / 3,901 / 4,146 / 3,911 / 3,993 / 4,349 |
| Batch total | 40,393 | 40,375 |
| Chapter 111 against the band | twenty-two words under | **a hundred and five words under** |
| Chapter 115 against the band | a hundred and seventy-three over | **inside the band at 4,415** |
| Emphasis, Chapters 114 / 117 / 118 | 36.4 / 45.7 / 46.6 | 38.0 / 46.9 / 46.4 |
| Literal-shape nesting detector | fourteen | **three**, all named |
| Quoted blocks | twenty-one in twenty-one blocks | **nineteen in nineteen paragraphs**, holding twenty-seven `>` lines |
| Paragraph shape | 318 of 353, ninety point one | **317 of 351, ninety point three** |
| Other two denominators | 586 of 711; 540 of 665 | **574 of 698; 528 of 652** |
| Longest single-sentence narration | 122 in Chapter 116 | **122, a tie in Chapters 116 and 118** |
| Paragraphs over a hundred words | forty-three | **fifty-five**, broken down four / one / nineteen / thirty-one |
| *About* plus a number word | 169 | **89** |
| *About* plus any word | 240 | **241** |
| Case-insensitive *about* | 271 | **278** |

**The length line is the one that would have misled a writer.** It said all ten chapters sat inside the band. Nine do. It also invented a chapter that was never out of the band, and understated the one that is.

## Two things that were not defects and are recorded rather than fixed

- **Two inside-paragraph repetitions survive, and both are the point.** A scan for any run of ten or more consecutive words appearing twice inside one paragraph returns exactly two, both deliberate and both self-explaining in the prose: Chapter 117, where a man of thirty-four asks that *the price is a figure I did in eleven seconds* be entered **twice** so that it cannot be paraphrased down, and Chapter 119, where a man of fifty-six says that in four years a stranger will read *nineteen lines about a thing that does not exist yet* and think it does. The Chapter 111 duplicated clause that the writing pass cut no longer appears in the scan.
- **A garbled arithmetic claim, now separated into the two facts it had merged.** The flags read *Ninety pans is sixty-one under water and thirty-four over the loams is thirty miles plus a rise of about ninety feet.* That made thirty-four a count of pans where it is a distance in miles, and ran the pans as a sum of ninety-one where they are nested counts that are never added. The pans and the distances are now stated separately, each in the words the prose uses.

## A distinction the batch earns and must not be flattened

**The Salt Verge is thirty miles east and about thirty-four, and Chapter 115 reconciles them in a mouth:** thirty miles is thirty miles on a road, and over the loams it is about thirty-four, the four extra being a rise of ninety feet that a cart does not enjoy. The prose uses thirty for the district's own figure, the flat road, and everything said before the party set out, and thirty-four for the party at the loams measured from a counter, a printer, a fourth place or its own market. `state/character-state.md` already carried the distinction; `state/current.md` did not and now does. **It is recorded in the Batch 0003 prompt so a later writer does not collapse it into one number.**

## Verified intentional — do not "fix" this later

- **The two distances.** Earned, explained in the prose, and correct.
- **The 132-word paragraph's two halves** reading as a list joined by *and that*. That is the documentary register, not a drafting artefact.
- **A chapter that refuses to be decided on a date.** The twenty-ninth of August ended with nothing decided, and the finding reverses a rule Batch 0001 had made. It is disclosed as a canon change in the batch summary.
- **The guild certificates.** Nothing is forged. Four people were asked, four answered, and one of the four was not in the room. The defect is that a guild form with twenty-nine columns has no column for whether a person was in the room, and `outline/series.md` and `outline/volume-03.md` both say *forged*; the prose is the narrower and more accurate statement and the outlines are corrected by a later outline pass, not by a writer phase.

## Carried defects, not this phase's

**The count of odd paragraphs in the whole of Volume 02 is exactly seven and is still exactly seven**, all of them carried and canon in Chapters 51 to 69. **Volume 03 is zero across all twenty chapters. Volume 01 holds ten**, in Chapters 16, 40, 42, 43 and 45, so an unscoped run over the whole manuscript returns seventeen and not seven; that ten is carried, canon and closed, and **a writer phase is not to repair it.** Chapters 51 to 100 were not opened.

## Belongs to the pipeline owner, not the writer

`state/phase-ledger.json` is controller-owned by Actions and is not a writer file, so it still reads `phase-000-bootstrap` / `planned` / `attempts 0` after 120 chapters. Treat that as a pipeline gap rather than as story state.

## Fix pass — a third audit, and what it found

Run after the second audit above, as a writer phase, over the ten files and the four state files that carried the flags. **No chapter was edited and no plot beat was moved. Every measurement that bears on the prose reproduces, and the longest single-sentence narration paragraph in the batch is still 122 words, a tie in Chapters 116 and 118.** The prose needed nothing.

**What this pass found is that four claims in the flags were still not checkable as written, which is the same failure the second audit found and it had survived the correction because the correction was applied to the numbers and not to the sentences around them.**

- **The `>` line count was four short, and the cause is the kind of mistake worth naming once.** The line said the nineteen blocks hold twenty-three `>` lines, seventeen of them single-line blocks and two runs, and then described the runs as *a two-line block in Chapter 112 and the four-line panel in Chapter 116*. **Chapter 112's run is three lines and Chapter 116's is seven, of which four are the panel, so a panel was counted as a block and a third line went missing in the same sentence.** The nineteen blocks hold **twenty-seven** `>` lines. Corrected in the summary, in `state/continuity.md`, in the canon card and in the Batch 0003 prompt.
- **The two false positives of the day-of-month search were named wrongly.** A search for a one- or two-digit number not followed by *of* returns zero hits, and what it flags is **Lot 17** in Chapter 117, once in the terms and once in the security. The line named *the third channel* in Chapters 117 and 119 and *the seventh of the seven* in Chapter 119 and then called them "two flags" while naming three. Those three belong to a **different** search — an ordinal word not followed by *of* and a month — and both searches are now stated with what each raises, and the total is five names, none of which is a day of a month.
- **The list of days inside a quoted block was not the list.** The line said *every* day inside a quoted block carries its month and then named five of them, in Chapters 117 and 119. Days also sit inside quoted blocks in Chapters 111, 112, 113, 114 and 120, and Chapter 119's own fifteenth of September was missing from the chapter it named. **The headline claim held; the evidence under it did not.** The whole list is now in the batch summary, in `state/continuity.md` and in the canon card.
- ***This month* was carried as eleven and is twelve.** *Last month* at eleven is right. The count is 1 + 1 + 8 + 1 + 0 + 0 + 0 + 0 + 1 + 0 by chapter, and all twelve are in prose and none is in a quoted block, which is the register the line describes.
- **The case-insensitive *about* figure of 278 was doing a job the sentence did not describe.** 278 is the case-insensitive count of the word *about* standing alone; 241 is *about* followed by a word, and the case-insensitive form of **that** measure is 272. Two different measures were sharing one sentence, which is how the earlier figure came to be out by eighty in the first place. **All four are now named as 241, 272, 247 and 278, in all four files, so a check runs the one it means.** The yard counts are also now marked as counted without regard to case, since *In the yard* with a capital returns nothing and the eight is a case-insensitive figure.

**The one outstanding request in this review is now done.** `outline/volume-03.md` had the midpoint reversal at Chapters 121 to 126, and the batch spent it in Chapters 117 and 118. The heading now says where the beat is, a paragraph records that the prose is canon and the correction moves nothing, and the unspent part of the 121-to-130 block is listed: the first channel to fail, the food convoy's choice, the aggregate unpaid toll as one number against Adrian's name, the worker council out of four unsigned things, and Nera Voss's first agent.

**Left alone on purpose.** `state/phase-ledger.json` is controller-owned. The ten odd paragraphs in Volume 01 are carried and canon. The *forged* consent in `outline/series.md` and `outline/volume-03.md` is corrected by a later outline pass and not here, as this review says it should be — **though it is worth naming that the two lines are now the only places in the repository that describe a forging, and the twenty chapters of prose say four people were asked, four answered, and one of the four was in another town.**
