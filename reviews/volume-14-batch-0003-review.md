# Volume 14 Block 0003 — Review and Review Fix, Chapters 681 to 690, Days 31 to 40

**A REVIEW FIX, WRITTEN AFTER THE TEN CHAPTERS WERE WRITTEN AND MEASURED AND AFTER THE PROSE WAS REPAIRED. EVERY FIGURE IN `state/volume-14-batch-0003-summary.md` AND IN THIS FILE WAS RE-DERIVED FROM THE TEN FILES AFTER THE LAST PROSE EDIT, NOT BEFORE IT. THE HARNESS LIVES IN `/tmp`, IS NOT IN THE REPOSITORY, AND ITS RESOLVER VALIDATES ON CHAPTER 640, WHICH IS NOT A CHAPTER OF THIS BLOCK AND WAS NOT EDITED.**

**WHAT THE PASS FOUND: SEVEN FINDINGS, ALL SEVEN REPAIRED. THREE WERE BLOCKING AND THREE WERE ACCURACY DEFECTS IN THE BLOCK'S OWN RECORD AND ONE WAS A PROSE DEFECT. THE REVIEWER VERIFIED A LARGE FIGURE SET AS ACCURATE AND THAT VERIFICATION IS KEPT IN SECTION 5 RATHER THAN DISCARDED.**

---

## 0. THE STATE OF THE REVIEW ITSELF, WHICH IS A PIPELINE FINDING AND NOT A WRITER'S

`novel-reviewer` DID NOT DISPATCH AGAIN. THE FALLBACK PASS PRODUCED A COMPLETE LOG AT `logs/batch-0003.review.log` AND A VERDICT AT ITS END, WHICH IS BETTER THAN BLOCK 0001'S AND WORSE THAN IT SHOULD BE. **THE SINGLE STRUCTURAL DEFECT OF THE QUALITY GATE IS THAT EVERY REVIEW IN THIS REPOSITORY IS A WRITER'S ACCOUNT OF THE WRITER'S OWN WORK**, INCLUDING THIS ONE, AND `AGENTS.md`'s line "a reviewer has checked the result" remains unsatisfied for every batch to date. The fix is a registration and a dispatcher under `.opencode/`, and neither is a phase's file.

**AND ONE PROCESS DEFECT THIS PASS FOUND, WHICH IS WORTH MORE THAN ANY PROSE FINDING BECAUSE IT IS THE SIXTH OCCURRENCE OF THE SAME FAILURE. THE REVIEWER'S OWN LOG RECORDS THAT THE WRITER PHASE BEFORE IT HAD ALREADY RE-ENTERED BLOCK 0003 WITH A CHECKPOINT, AND THAT CHAPTERS 691 TO 700 WERE ALREADY ON DISK. **A BLOCK THAT IS ALREADY WRITTEN GETS DISPATCHED AGAIN, AND A POINTER THAT GOES STALE SENDS A WRITER BACK INTO FINISHED WORK, AND NEITHER SURFACES UNTIL A REVIEWER HAPPENS TO LOOK AT THE TREE RATHER THAN AT THE DIFF.****

---

## 1. THE THREE BLOCKING FINDINGS

### 1.1 THE NEXT DISPATCH WOULD HAVE REWRITTEN TEN CHAPTERS THAT ALREADY EXIST. **REPAIRED.**

`workspace/volume-14/batch-0004/PROMPT.md` was a fresh "write chapters 691 to 700" instruction and contained **zero** occurrences of any warning — `ALREADY ON DISK`, `already written`, `DO NOT REWRITE` all returned nothing. Yet `chapters/volume-14/chapter-0691.md` through `chapter-0700.md` and a 406-line `state/volume-14-batch-0004-summary.md` were on disk. **The warning existed only as prose buried inside `state/current.md`, and `scripts/novel_runner.sh` selects a phase with `find workspace -name PROMPT.md`, so the next writer run would have received the PROMPT and not the warning.**

**THE REPAIR USED THE MECHANISM THE RUNNER ALREADY READS AND TOUCHED NO DISPATCH LOGIC.** An empty `workspace/volume-14/batch-0004/.retired` marker was created, which is the condition `scripts/novel_runner.sh` line 38 and `.github/workflows/novels.yml` line 138 already test, and the same one `workspace/volume-12/outline/.retired` and `workspace/volume-14/outline/.retired` already carry. The prompt now also opens with a warning block naming the ten files and pointing a writer at the block record and at Chapter 700. **No workflow file, no runner script, no dispatch rule, no timeout, no retry policy and no checkpoint logic was edited, and no entry was created in `state/phase-ledger.json`.** A marker is an input to the existing rule; the rule is untouched.

### 1.2 THE VOLUME'S ACTUAL NEXT PHASE WAS THE CLOSE AND IT DID NOT EXIST. **REPAIRED.**

`outline/volume-14.md` scopes the volume at Chapters 651 to 700 and all fifty files were on disk. `workspace/volume-14/` had no `close/` directory. **The stale pointer in 1.1 was therefore not merely a warning that was missing: it was the only pointer there was, and while it stood, the volume close could never be created.** Every prior volume from 03 to 13 has a `close/`. Volume 14 did not, and would not have, because the pipeline was aiming at a fifth block instead.

**THE REPAIR CREATED `workspace/volume-14/close/PROMPT.md` AND CORRECTED THE LIVE POINTER IN `state/current.md` IN PLACE.** The close prompt writes no chapter. It owes `state/volume-14-close.md` and `state/volume-14-roll-summary.md`, five appends, the in-place header correction, and exactly one next phase. **It opens by naming the one sentence this volume owes, because the reviewer's standing-risk finding (section 4) is the reason it has to exist.**

### 1.3 THERE WAS NO REVIEW ARTIFACT FOR THE BLOCK. **REPAIRED.**

`reviews/volume-14-batch-0003-review.md` did not exist; only `volume-14-batch-0001-review.md` did. **A phase that updated every state file and left a `.checkpoint` with no review record is indistinguishable, from the outside, from a phase that was reviewed and found clean.** This file is that record.

---

## 2. THE TWO ACCURACY DEFECTS IN THE BLOCK'S OWN RECORD

### 2.1 THE UNIT CHECK WAS UNFALSIFIABLE AND REPORTED A FALSE ZERO. **REPAIRED.**

`state/volume-14-batch-0003-summary.md` section 5 claimed: *"ANY UNIT OF DISTANCE, WEIGHT OR MONEY AFTER A FIGURE, **0**, MEASURED WITH A LIST OF THIRTY UNIT WORDS."* **The reviewer counted seventy-one such constructions in the ten chapters after spelled figures: `nine feet` ×16, `nine inches` ×11, `four feet` ×11, `one inch` ×10, `hundred miles` ×10, `eleven miles` ×10, `hundred feet` ×2, `two feet` ×1.**

**THE CAUSE IS WORTH NAMING BECAUSE IT IS A CLASS OF BUG THAT WILL RECUR. THE CHECK ONLY FIRED ON AN ARABIC FIGURE, AND THE ONLY WORD THAT FOLLOWS A DIGIT ANYWHERE IN THIS BLOCK IS `seconds` — twenty-one times, which is the mechanism and not a distance. A CHECK THAT CANNOT FIRE IS NOT A PASS; IT IS A CHECK THAT WAS NEVER RUN AGAINST THE PROSE IT WAS MEANT TO GUARD.**

**THE REPAIR REPLACED IT WITH ONE THAT MATCHES SPELLED FIGURES AS WELL, WHICH RETURNS SEVENTY-ONE, AND NAMED ALL SEVENTY-ONE.** They are this manuscript's own units: the hollow in the stone is one inch deep, the cart wheel is lifted nine inches, men stand four feet and nine feet and two feet apart, the road keeper's unasked stretch is eleven miles, a body sits four hundred miles off and a wall reading two hundred feet away. **The prohibition at `outline/volume-14.md` section 5.3 item 21 is on a metric unit, a weekday name, a colon-form time and a twenty-four-hour clock, and all four are zero on all ten mornings.** The false zero is gone and the true figure is printed with its convention.

### 2.2 A REPEATED SCENE WAS MISCLASSIFIED AS A LEDGER LINE. **REPAIRED.**

Section 9 closed: *"EVERY ONE OF THESE IS THE HOUSE LEDGER LINE OR THE HOUSE SIGHTING LINE AND NONE OF THEM IS A SCENE."* **That was false. The top item, identical on nine of ten files, is a 62-to-70-word action paragraph** — a cart arrives at three, a near wheel is dragging, a man lifts it nine inches with one arm, he goes up the bank, he sets the shafts down, he does not turn round. Similarity between the Chapter 681 and Chapter 686 versions is 0.77, and the "reword" the record credited itself with touches only the tail sentence, which is why 686 is not in the nine.

**THE REPAIR RECLASSIFIED THE FIFTEEN ROWS BY WHAT THE PARAGRAPH IS. TWO ARE LEDGER LINES — THE CLERK'S ENTRY AFTER A SPEECH, ON THREE FILES, AND THE LEDGER'S OWN `ABOUT TWO THINGS WERE SAID OUT LOUD` CLAUSE, ON TWO — AND THIRTEEN ARE SCENE OR SIGHTING PARAGRAPHS.** The record's own principle, printed a section earlier, is that a paragraph recording a count is a ledger line and a paragraph recording a body moving through a yard is a scene. The classification now follows it. **A record that reclassifies its own repeated prose to make the repetition look like house furniture is the failure, and the correction is in the file rather than in the prose because the repetition itself is this volume's subject.**

---

## 3. THE PROSE DEFECT, AND IT WAS THE WORST OF THE SEVEN

### 3.1 A TICK HAD BECOME A TEMPLATE. **REPAIRED.**

`about four of you have worked out that` appeared **six to nine times on every chapter** and **up to four times inside a single speech** on Chapter 686. `and that is all I have got` and its sibling `and that is the whole of what I have got` between them closed **all twenty-one** relay speeches. Every one of those speeches had the same skeleton: a claim, then three identical frames, then a signature.

**This is the mechanical-filler repetition `AGENTS.md` prohibits by name.** The block record had already noticed the count — it printed the figure, 65, and called the repeated clause inside a bolded speech "not a defect and was not touched." **That was the record negotiating with the finding instead of reporting it.**

**THE REPAIR WAS MADE IN TWENTY-ONE PLACES AND IT CHANGED NO EVENT.** Each speech kept its claim, its speaker, its audience, its order, its stamp and its position in the morning. The second and third frames became plain predicates — the same claim, said without an attribution wrapper around it — and the twenty-one signatures became twenty-one different sentences.

| | before | after |
|---|---|---|
| `about four of you have worked out that`, all ten chapters | **65** | **21**, one per relay speech |
| in a single speech, worst case | **4** (Ch 686) | **1** |
| distinct closing phrasings across 21 relay speeches | 2 | **21** |
| `about four of them have said that` (the bystander register) | 76 | **76, untouched** |

**THE ATTRIBUTION REGISTER ITSELF WAS NOT TOUCHED.** `about four of them have said that` and `have said since that` live in the bystander paragraphs, where they are this manuscript's actual instrument, and both are unchanged. The repair removed a frame from inside an utterance, not a device from the book.

### 3.2 PROSE WAS FITTED TO THE CEILING. **REPAIRED, BY CUTTING IN THE OTHER DIRECTION.**

Chapter 686 stood at **exactly 3,200** and Chapter 684 at 3,198. Two of ten chapters landing on the cap is what prose cut to fit a constraint looks like. The repair cut 404 words out of the block by shortening the twenty-one speeches, which moved the figures to **30,691 total, mean 3,069.1, minimum 2,936 at Chapter 683, maximum 3,162 at Chapter 684, and no chapter on either edge.** The band was not widened and the floor was never at risk.

### 3.3 EVERY COUNTED FIGURE AND EVERY DURATION STAMP WAS RE-DERIVED, BECAUSE EVERY SPEECH MOVED. **REPAIRED, AND THE CONSEQUENCE FOR ANYONE WHO QUOTES THE OLD RECORD.**

This house counts what the boy said and stamps how long it took. A speech that changes length has its stamped figure and its duration changed with it, or the page is lying. All twenty-one were re-derived by script from the prose and re-checked:

| | before | after |
|---|---|---|
| counted claims | 21 | **21**, all three checks agreeing on 10 of 10 |
| speech figures | 134, 146, 136, 126, 115, 125, 135, 141, 131, 156, 123, 129, 129, 170, 122, 146, 162, 134, 180, 149, 185 | **116, 127, 117, 106, 97, 111, 117, 123, 108, 138, 108, 111, 115, 151, 103, 126, 140, 118, 148, 133, 160** |
| duration stamps | 52, 56, 52, 48, 44, 48, 52, 54, 55, 60, 47, 50, 50, 65, 47, 56, 62, 52, 69, 57, 71 | **45, 49, 45, 41, 37, 43, 45, 47, 42, 53, 42, 43, 44, 58, 40, 48, 54, 45, 57, 51, 62** |
| mismatches after re-derivation | — | **0** |
| block length | 31,095 | **30,691** |
| body segments / mean | 467 / 65.93 | **498 / 61.01** |
| attribution layers | 213 | **169** |

---

## 4. THE STANDING RISK, AND IT IS WHY THE CLOSE EXISTS

**The volume's owed sentence — what a district has when the only thing protecting it is a person — is unpaid through Chapter 690 and is explicitly not the carrying. With Chapter 700 already on disk, written by a phase this block did not write and no phase reviewed, it will be paid or lapse in a chapter outside every gate.**

The repair did **not** pay it and could not: `outline/volume-14.md` section 15.1 gives it to the close, payable only in a doing and never as a thesis, and never as a sentence about trust, scale, rules or the no. **`workspace/volume-14/close/PROMPT.md` now opens by naming it, and `state/current.md`, `state/continuity.md` and `state/open-threads.md` all record it as live, unpaid, and owed to the close. If `state/volume-14-close.md` does not print it standing alone and undefended, it lapses across seven hundred chapters and no phase in this pipeline may print it afterwards.**

---

## 5. WHAT THE REVIEWER VERIFIED AS ACCURATE, AND WAS NOT RE-DERIVED FOR NOTHING

- **All twenty-one counted claims matched their speech word counts exactly**, re-derived independently by the reviewer.
- `read the number back to himself in a low voice` = 21, equal to the claim count; `seconds` = 21; **no other word follows a digit anywhere in the ten files.**
- Titles 26, 29, 28, 25, 29, 16, 26, 25, 23, 29 — minimum 16, maximum 29, median 26, as the record stated.
- In-file duplicate prose paragraphs = 0; five identical paragraphs across the ten, as the record stated. **The count was right and the classification of them was not, which is finding 2.2.**
- The calendar: 681 = 26th of the 7th … 686 = 31st, 687 = 1st of the 8th … 690 = 4th of the 8th, consistent with day 1 = 27th of a thirty-one-day sixth month.
- The reserved scan returns an empty dictionary; zero lines begin `>`; zero panels.

**AND THE ANCHOR WAS RE-RUN AFTER THE REPAIR BY THE SAME EXTRACTOR AND RETURNS 175 CORRECT CELLS PLUS FIVE DELIBERATELY STOPPED, WHICH IS 180, AT ZERO FAILURES — UNCHANGED, BECAUSE NO CARRIER PHRASE LIVES INSIDE A SPEECH.** The resolver re-validated on Chapter 640 at 143, 129, 164 against speech word counts of 143, 129, 164.

---

## 6. WHAT THE REPAIR DID NOT DO

It did not restart the block. It did not rewrite a chapter or cut a chapter or lose a scene. **The carrying on Chapter 686 is where it was, with the same two men at the same two ends of the same table, the clerk's hands on the same book, the same four costs allocated to the same bodies, and the same four figures left uncorrected on the same wall.** It did not change the planned plot, the branch, the calendar, the intercept, or a single ladder figure. It did not edit a controller file. It did not pay the owed sentence, and it did not create a fourteenth phase: it created one, `workspace/volume-14/close/PROMPT.md`, because the volume is complete and a complete volume owes a close.
