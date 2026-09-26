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
| Quoted blocks | twenty-one in twenty-one blocks | **nineteen in nineteen paragraphs**, holding twenty-three `>` lines |
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
