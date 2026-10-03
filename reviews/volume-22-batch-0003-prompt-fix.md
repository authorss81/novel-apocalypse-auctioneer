# Review fix — the brief and state files for Volume 22 Block 0003

**Run 2026-10-02, against `logs/batch-0001.review.log`. This is the record of the pass that took that review's findings 1 to 5 and escalated its findings 6 and 7. It wrote no chapter, restarted no batch, and changed no planned plot.**

## What was wrong, in one paragraph

The review found a pipeline that cannot close its own phases, a block record three times larger than the change it documented, a fiction that had degenerated into repeated readouts, a logline the last two volumes had silently abandoned, and a state layer at parity with the manuscript and talking mostly about itself. **Only two of those five are things a review-fix phase may fix, and both of them live in the phase brief and the state files rather than in the prose.** The brief was 10,644 words at 78.3% capitals and asked for register families, tokeniser variants and published instrument self-findings; the block record was 11,892 words at 75.2% capitals and published word and divider tables for ten mornings; the four live state files had just been handed 164 lines and 5,630 words of capital letters restating three figures. **The next ten chapters would have been written against that brief, so the brief was the finding with a deadline on it.**

## What was done

| file | before | after | what changed |
|---|---:|---:|---|
| `workspace/volume-22/batch-0003/PROMPT.md` | 10,644 words, 55,596 bytes, 78.3% capitals | 7,786 words, 40,912 bytes, 1.5% capitals | Plain sentence case; prose requirements first; measurement apparatus removed; every canon figure kept |
| `state/volume-22-batch-0001-summary.md` | 11,892 words, 64,009 bytes, 75.2% | 2,716 words, 14,339 bytes, 2.7% | Day map, three document corrections, two prose repairs, promise position and unpaid debts kept; word and divider tables, register families, tokeniser counts, hedge family and instrument audit removed |
| `state/chapter-summaries.md` | +2,116 bytes appended by `99e4950` | +1,306 | Compact entry carrying the two repairs and nothing else |
| `state/character-state.md` | +1,748 | +1,202 | Compact entry: no person changed, and what did |
| `state/continuity.md` | +4,085 | +2,647 | Compact entry: position, the two repairs, the hand-off line, the four absent files |
| `state/open-threads.md` | +5,382 | +7,844 | Threads 81 and 82 kept and shortened, 83 and 84 withdrawn by name, threads 85 to 87 opened |
| `state/current.md` | five live header lines stale by one volume | corrected in place | Named Volume 22 open at block 0003, the reversal record, Chapter 1030 and the block 0003 brief; read-first item (2) repointed; the five lines went from 9,032 bytes to 5,122 |
| `state/maintainer-escalation.md` | item 11 the last item | items 12 and 13 added, item 7 updated, pass record appended | The three findings no phase may fix |
| `reviews/volume-22-batch-0003-prompt-fix.md` | absent | this file | The record |

## How it was checked

**The brief was checked by comparing every numeral in it against the one it replaced.** Fifty-seven figures disappeared and every one of them is a word count, a divider count, a register-family count, a tokeniser variant, a hedge-family cell, a self-test threshold or a section number. **No ladder intercept, no ladder cell, no count value, no morning number, no page cell, no prohibition number, no day-map entry and no promise morning disappeared.** Nothing plot-bearing was cut to make room for craft.

**The record was checked the same way.** Of the figures removed, none belongs to a morning, a page, a lane, a person or an answer; the two figures that could not be reproduced are withdrawn by name in its own §6 rather than deleted silently, because a record that loses its own errors cannot be checked against them.

**The prose was checked and left alone.** Over `chapters/volume-22/chapter-1011.md` through `chapter-1030.md`: quotation parity is even in all twenty files, every file carries at least two scene dividers, no sentence exceeds 130 words, and the only occurrences of meta-language are the twenty title lines' own chapter numbers. **No new prose defect exists in those twenty files beyond the two the review already repaired,** and the degeneration is systemic rather than local.

## The measurements behind the escalation, with their conventions

- Duplicate-sentence rate: **346 of 1,894 sentences (18.3%)** over the twenty files, counting each file split on sentence-ending punctuation and comparing whitespace-normalised sentences, case preserved. Volume 01 gives 0.3% on the same convention. The review measured 19.2% on a different one; both are published beside each other rather than reconciled, because the number that matters is the order of magnitude and the shape.
- Readout share of a chapter's words: **30.5%** in block 0001 and **33.0%** in block 0002, where the readout is everything before the first line that is exactly `---`. Volume 01 gives 9.3%.
- Quoted words: **1,678 of 50,475 words, 3.3%**, as whitespace-separated words between straight double quotes. Volume 01 gives 39.8% and Volume 16 gives 49.2%.
- Title lines: mean **61.5** words in block 0002 and **72.7** in block 0001, maximum 96. Volume 01's mean is **7.1** words, maximum 12.
- Premise strings, counted case-insensitively: `auction` **17 / 0 / 0** and `System` **7 / 0 / 0** across Volumes 01, 21 and 22, with no System panel in either of the last two.
- The five live state files are **3,028,329 bytes** against a manuscript of **3,100,306 words** (`cat chapters/*/chapter-*.md | wc -w` over 1,030 files), down 3,331 bytes on this pass, which is the first time one of these passes has made the layer smaller.

## What was deliberately not done, and why

**The twenty finished chapters were not re-voiced.** The repair is bounded and knowable — fresh wording for the eight readout sentences that repeat on sixteen to twenty of the twenty files, about a hundred and sixty sentences, every figure unchanged — and it is not this pass's work, because it edits chapter files a writer phase may not touch and because a re-voice of two volumes is a decision a maintainer should authorise. It is escalated as item 13 with its size, so that the next pass does not have to re-derive it.

**`outline/volume-22.md` was not edited.** It is the contract, and the cause of the degeneration, and it is canon against every document in the tree. Item 13 says so and leaves the decision.

**`NOVEL_SPEC.md` was not edited.** Finding 7's accretion in it is real and its status line still advertises the Volume 05 outline as the next phase, but it is a specification rather than a state file and no phase asked for it to be touched. It is escalated in item 12's second paragraph.

**No marker was written, and `state/phase-ledger.json` was not touched.** `workspace/volume-22/batch-0001/` carries `.attempts`, `.deferred`, `.retry-after` (expired) and `.wip-conflict` and no `.done`, so the next dispatch goes there again instead of to the block that has work to do. **That is finding 1, it is the runner's, and item 7 of the escalation file now carries its measurement for Volume 22.** The one thing available without a marker was to state the fact where the next writer will look, and the `Next phase:` line of `state/current.md` now says it.

## What a successor should check first

Read `chapters/volume-22/chapter-1021.md` through `chapter-1030.md` as prose before reading anything else, then `workspace/volume-22/batch-0003/PROMPT.md` §1 and §2, then the contract's §4 day map and §11 prohibitions. **Do not inherit any of the ten readout sentences named in §2 of the brief**, and do not measure the block against a word band or a divider band: there is no longer one, and the previous brief's was 138 dividers for ten files, which is what ten readouts look like when they are the chapter.