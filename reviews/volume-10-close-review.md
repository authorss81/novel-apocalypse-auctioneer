# Volume 10 Close Review

**This is the Volume 10 close's self-review. It is a list of defects and not a list of things that came out well. It was written by the same agent that wrote the close, and that fact is the first defect on the list and not a footnote to it.**

**Nothing was restarted. No chapter was written and no chapter was edited. Chapter 500, Chapter 490 and Chapter 455 are canon, and the three arithmetic deviations in them are reported at full size in `state/volume-10-close.md` sections 6, 6.1 and 6.2 and left standing. Every figure below was measured by re-running the measurement over the sixty chapter files, not by reading the close record's own claims, and every measurement in the close record that could be checked was checked again from the chapters.**

**THE REVIEWER'S OWN STANDING IS THE FIRST ITEM BECAUSE IT GOVERNS THE READING OF EVERY OTHER ITEM. `reviews/volume-08-close-review.md`, `reviews/volume-09-batch-0005-review.md` and `reviews/volume-10-batch-0001-review.md` through `0004` were all written by the default agent because the `novel-reviewer` subagent fell back. The three previous closes each found real defects in the record they were given, which is the argument and not a reason to trust this one. Read this file as the writer's account of the writer's own work.**

---

## 1. BLOCKER — the day map the day-lists were measured on was wrong for the last twelve chapters, and it changed nothing, and that is worse

**How it was found.** After the close record was written, the whole day-lists table was recomputed from a day map built forward from the two-chapter list rather than by the method the first pass used. The two maps agree exactly through Chapter 488 and disagree from Chapter 489.

The first pass built its day index by advancing a counter once per chapter and then applying a correction pass for the doubled days. That spends the doubled day 43 on Chapters 490 and 491 instead of 491 and 492, and every chapter from 489 onward is then a day out. **Because every cell in section 14 of the close record is "on N of 50 days", the whole table was riding on that index.**

**What survived, and it survived in a way that is itself the finding.** Recomputing the entire day-lists table on the clean map changed **no total and no day count.** The off-by-one touched nothing, because each of those strings is either on all fifty days or silent on a run the error never reached. **A map that is wrong and changes nothing is a map nobody will ever notice is wrong**, and it is a worse state to be in than a map that is visibly wrong, because the day count is the load-bearing part of every "on N of 50 days" cell in the table and there is no signal anywhere that says the thing under it is soft.

**And the two cells that did turn out to be wrong were not cells the map touched.** They were two cells written into the record by hand that the chapters did not support. **So the day map was not the cause of anything and the map being wrong is the reason this file has an item at all: the close could not tell the difference between a table measured on a broken instrument and a table measured on a sound one, because the broken instrument agreed with the sound one.**

**What is available as a check, and was not used here: the ladder.** Every one of the fifteen columns at close section 5.1 was built on the clean map and holds on fifty of fifty days with a single cell failing in two of them. That is the only verification in this phase that could have caught the map, because a ladder is sensitive to a day and a string count is not.

**Not repaired: the method. A close should rebuild its own index before measuring, and should measure every day-dependent figure twice by two routes, and should use a figure that is sensitive to a day as the check on a table that is not.**

## 2. MAJOR — the close record printed the form *was not run* at 60 and the chapters give 61

Chapter 454 carries it twice: once inside the clerk's entry in the first line of the chapter and once on a line of its own, `It was not run on this day.` Every other chapter carries it once. The total is 61 on 50 of 50 days.

**This is the second time in this repository that a doubled chapter has produced a doubled count and the document has printed the undoubled figure** — the first was `four hundred and eleven` on Chapter 479, which the close record caught and this one it did not. The shape is identical and the volume contains both instances. A close that found one and missed the other, in the same table, on the same volume, did not have a check for the shape and found the first by looking.

**Repaired** at `state/volume-10-close.md` section 14 and carried into the roll. It is worth stating plainly that this is the second instance of the shape in sixty chapters and a Volume 11 writer should expect the shape again.

## 3. MODERATE — `a habit` was printed at 17 with no case stated, and the table's own stated convention is case-insensitive

The string is 17 lowercase and 18 case-insensitive. The eighteenth is the chapter title at Chapter 441, *A habit is a finding*. Section 3.6 of the close record states the convention for its tables as case-insensitive, and section 14 did not restate it, so a reader applying the document's own convention to that cell gets 18.

**The finding this cell supports is unaffected** — `a habit` occurs seventeen times in a body and is never once attached to the figure on the sheet, which is the point section 1 of the close record makes about it. The defect is that the number and the convention disagreed and nothing said which one the number was using.

**Repaired:** both figures are now printed and the case is named.

## 4. BLOCKER — six ladder intercepts are printed as day-one values in three documents, and a writer who reads them as intercepts is wrong on forty-nine of the fifty days

**This is the most useful thing the review found and it was not in the close record when the close record was written.**

The handoff prompt's ladder, `outline/volume-10.md` section 6.1 and `state/volume-10-batch-0004-summary.md` section 6 all give the value of these six figures **at Chapter 441** in a column a writer will read as the constant in a `constant + c` rule:

| the figure | printed as | true intercept at `c = 0` | holds as printed | holds as an intercept |
|---|---|---|---|---|
| how long the bid has been open | 99 | **98** | 1 day of 50 | 50 of 50 |
| how far back the ninth of the nine printed nights is | 232 | **231** | 1 day of 50 | 50 of 50 |
| how far behind the figure on the second line is | 54 | **53** | 1 day of 50 | 50 of 50 |
| how long since the first day of the eighth month | 129 | **128** | 1 day of 50 | 50 of 50 |
| how far past a printing a body four hundred miles off is | 68 | **67** | 1 day of 50 | 50 of 50 |
| the age of the figure on that sheet | 190 | **189** | 1 day of 50 | 50 of 50 |

Each of the six was verified cell by cell across all sixty files. Each holds on one day of fifty as printed and on fifty of fifty as `intercept + c`. **The bid is the worst of the six, because 98 is the less round of the two numbers and a writer reaching for the rounder one will be a day out from Chapter 443 to Chapter 500 without once finding out.**

The other four columns in the same ladder — the board, the train, nobody having entered anything, and the days from the second of January — are printed as true intercepts (348, 664, 378, 339) and are correct. **So one ladder in three documents mixes two conventions in fourteen rows and gives no sign that it has.** That is the defect. It is not a wrong figure in any of them; it is a table that cannot be used without knowing which of its rows are which.

**Repaired in the documents this phase owns:** the full verified table is at `state/volume-10-close.md` section 5.1 and `state/volume-10-roll-summary.md` section 1, with the six rows in bold and the convention stated in the header. **Not repaired in `outline/volume-10.md` section 6.1, `state/volume-10-batch-0004-summary.md` section 6, or the handoff prompt, because none of those is this phase's to edit.** They are reported instead, which is the same disposition the close gave the other three document defects.

## 5. MAJOR — there is a second arithmetic deviation in the volume and the close record named only one

The close record's section 6 is headed "the two figures in Chapter 500 that are a day high". Re-deriving every ladder found a second one, in the other direction, on a different object, and not in the inherited warning that pointed at the first:

- The rule said out loud in that yard was said on the tenth of the tenth month. The figure is `58 + c`. It holds on 49 of 50 days: 97 at Chapter 487, 98 at 488, 99 at 489, **99 at Chapter 490**, 101 at Chapter 491, 102 at Chapter 493.
- **Chapter 490 is day 42. The ladder gives one hundred. The chapter prints ninety-nine.**

What makes this one worth more than a transcription slip is that **the same sentence tells the reader what the figure is.** The chapter has a clerk enter that figure as a figure about a rule and not about how many days the rule has been kept. So the one cell in sixty chapters that is a day out from its own ladder is the one cell whose chapter declares on the page that it is not a day-count.

**The review does not claim to know whether the writer of Chapter 490 meant the ninety-nine, and does not resolve it.** What can be said is that the deviation and the sentence about the deviation are in one line, and that both readings are available to a reader. It is also the sharpest instance in the volume of the volume's own argument, arrived at by arithmetic error rather than by design, which is the kind of thing a reader will notice and a close should not tidy.

**Repaired in the documents this phase owns:** section 6.1 of the close record, and the liability is in both the close and the roll.

## 6. MODERATE — the scope for the marks in chalk has been printed four times under four patterns, and this item installed a third of them and called it a repair

**This item is the reason the two items after it exist, and it is left in the wrong tense on purpose. As first written it said `Repaired`, and it was not, and the thing it repaired was not broken.**

The inherited block record and the inherited contract both give the formula for the marks in chalk as *fifteen plus `c`*. **That is seven out at every cell under every pattern and the close record caught it.** What is in dispute is the scope, and **the inherited scope of twenty-four chapters on twenty-one days is not short. It is exactly what the pattern `there are N marks in chalk` returns, and this item called it short by two chapters and one day, which was wrong.** The defect this item reports is real but it is a different defect, and it is the defect that matters: this close, its own review, and a later pass have now printed four scopes for one measurement and no two of them were produced by the same pattern.

| the pattern | chapters | days | cells failing `c` less seven | published by |
|---|---|---|---|---|
| `there are N marks in chalk` | **24** | **21** | 0 | the inherited block record, and the close's first pass. **Right for its pattern** |
| the same, plus `there are N of them in a row`, matched case-sensitively | **26** | **22** | 0 | the close's first correction, republished in four documents |
| the same pair, matched case-insensitively | **27** | **23** | 0 | the later pass that reviewed this item |
| every numbered form, case-insensitive | **32** | **27** | **1** | the repair, and the pattern the tables are now measured on |

**The second row is the one that is wrong in a way no reader could have caught from the number.** A case-sensitive match requires a lower-case `there are`, and that drops exactly one chapter, and the chapter is Chapter 453, whose first line of the book reads `There are five marks in chalk along the edge of that second table` with a capital on the front of the sentence — the first printed value of the whole ladder and the cell the arithmetic hangs from. **A case convention deleted the anchor, and the number it produced, twenty-six on twenty-two, is lower and tidier than the number it replaced, which is why it survived four documents.** This close has now been bitten by case sensitivity twice in two tables, and the second bite is the same shape as the first, which is item 3: a count that a reader has to apply a stated convention to by hand, where the convention applied mechanically gives a different number.

**And the fourth row found a chapter, which is the reason this item is MODERATE and not MINOR.** The three narrower patterns miss five chapters — 455, 464, 469, 470 and 476 — and four of the five hold the ladder and one does not. Chapter 455, day 14, prints five where `c` less seven gives seven, and five is the figure Chapter 453 prints on day 12. That is a third arithmetic deviation in the volume and it is now at section 6.2 of the close record. **The volume had two deviations for as long as a case-sensitive pattern was in use, and the pattern was in use because it reported zero cells failing.**

**Repaired now, in the four documents this phase owns, with all four patterns printed beside the scope the tables use, the case convention named, and the failing cell named.** The same repair is in the close record at sections 2 item 5, 5.1 and 6.2, in the roll at section 0.3 and section 1, and in the state appends at `state/current.md` sections 3, 4 and 7.1 and at `state/continuity.md` sections 2, 3 and 4.

## 7. MODERATE — the close record's own paragraph runs contain two literal `\n` sequences

`state/volume-10-close.md` section 15, at the paragraphs beginning "All three duplicated paragraphs straddle a block boundary" and "And the volume figure of 7,626", each end with a backslash-n as two characters rather than a newline. **A close that publishes a measurement of markdown integrity at section 15 and then ships a markdown defect in the same section is not measuring the same document it is publishing.** This is the same class of error as item 1 and item 4: the instrument and the thing measured came apart.

**Repaired.**

## 8. MODERATE — three of the twenty-five things a close may not do were broken in prose, and the close could only report them

`outline/batches/volume-10-batch-0004.md` section 5 forbids using a wall, a lane, a gatepost, a rubbed heading, or a looking in front of one as a device. Measured over the volume:

- `a wall` — 29 occurrences on 15 days. **Classified by one rule: take the forty-five characters either side of each occurrence and ask whether a figure or a column is named. Twenty-four name a figure. Three name a column, and two of those three are the string `three columns of a wall` at Chapters 486 and 498. Two are a man standing at that wall with nothing on it, at Chapters 482 and 491. The yard's own wall is zero: the phrase does not occur in the volume.** `that low wall`, the existing object the man of about sixty-four sits at the foot of, is 61 on 50 of 50 days and 60 of 60 chapters, and it is a different string, and it is not inside this count. **So the count of wall-as-device occurrences is two, not zero and not eighteen and not four.**
- `a lane` — 1 occurrence, day 9, Chapter 450, a man walking down a lane recalled inside a comparison.
- `a gatepost` — 2 occurrences, both on day 33 at Chapter 479, both the sheet nailed to a gatepost nine hundred yards off. A gatepost used as a device and a looking in front of one used as a device, both, in one chapter.

**This item as first written split the twenty-nine as twenty-two, four and three and named four of them as the wall three columns stand on, at Chapters 486, 491, 498 and 499. Both halves were wrong.** The string `three columns of a wall` is at two, at Chapters 486 and 498, and Chapters 491 and 499 are two of the reads. The yard's own wall is not in the volume. **The four-chapter claim was not invented here: it came in from `state/volume-10-batch-0004-summary.md` section 4.9 and its finding 3, and from `outline/batches/volume-10-batch-0004.md` item 13, and from the Batch 0004 review-fix blocks in `state/current.md` and `state/continuity.md`, and the close carried it forward and re-split the same twenty-nine into a different wrong shape.** That is a documented loss carried into a following block for the third time in this repository's history, and it is the same shape as items 1, 6 and 11: a figure believed because the sentence around it read like a measurement.

**None of these is a close's to repair, because Chapters 450, 479, 482, 486, 491, 498 and 499 are canon. They are weighed and printed, and the prohibition's own count is now honest.** The honest summary is that a prohibition inherited into a close's own list of things it may not do was broken three times in prose, in three chapters, and that the phase whose job is to weigh had nothing to weigh it with except a count and inherited that count from the block it was weighing.

## 9. MINOR — the protected relay that carries the man nobody gives anything to has fallen and the standing is unchanged

`at the foot of that low wall with his coat folded on the stones` is on 42 of 50 days, down from 30 of 30 in the first two blocks. **This is the first time a protected relay in this manuscript has fallen, it fell by two thirds inside one block, and the cause is traceable to a review repair in Batch 0003 that removed a time of day from a protected string and, in removing it, removed the sentence that put the man on the stones.**

The close did not raise it and did not lower it, which is correct: none of the six may be smoothed by deletion and a phase that lowers one has destroyed a measurement. **The defect is not the figure. The defect is that a repair to a protected string was made, the block record named the loss, and the next block did not put it back — and that is the second time in this repository's history that a documented loss has simply been carried forward into the following block.** The man the relay carries was given nothing on all fifty days and is off the page for eight of them, and the loss and the giving are the same fact.

**No repair is available.** The volume is closed and restoring eight days of a relay would be writing prose into it.

## 10. MINOR — the cap on the figure on the sheet was passed by exactly the coincidence it exists to prevent, and no rule could catch it

62 occurrences against a cap of 60. **The two extras are on Chapter 479, the one morning in fifty on which the district's own third column (`378 + 33` = 411) and the figure it borrowed from nine hundred yards off (411) came out equal to the last digit.** A boy of about nineteen noticed and the clerk entered that she does not know whether a number she did not make is a figure.

**The defect is that a cap on how often a borrowed figure may appear cannot detect the day the borrowed figure and the district's own figure coincide**, because on that day a writer obeying the cap and a writer breaking it are indistinguishable from the page alone. The close printed the morning and declined to raise the cap for one morning, which is the right decision and is not a repair of anything. It is recorded here as an unfalsifiable rule that met the one case it was written for.

## 11. MINOR — the measurement tool cannot read any figure this volume is about, and its calibration cannot see that

`tools/measure.py`'s `words_to_num` rejects any token not in its units table and `and` is not in the units table, so `two hundred and thirty-nine` returns `None` while `forty-three` returns 43. The counted-claim path escapes the failure because `parse_number_after` strips `and` first.

**Every figure this volume is about — 349, 665, 379, 340, 411, 281, 239, 148, 190, 189, 398, 714, 428, 389, 117, 103 — is written with an `and` or an article and returns `None`.** The calibration at Chapters 241 to 250 holds fifty-three claims and every one of them is under two hundred, so it cannot see the defect either. All five calibration figures reproduce and are reported as reproducing.

**The consequence for this phase is concrete and it is the reason item 4 exists: the ladders had to be re-derived by a parser written for the purpose in a temporary directory outside the repository, and that parser had three separate bugs of its own** — it chained numerals across a comma, it checked the gap on the wrong side of the conjunction, and it built its day index wrongly. **All three produced plausible numbers and none produced an error.** A close whose measuring instrument is a fresh script it wrote itself, with no test fixture, is measuring with something that has never been shown to fail. **That is the most serious process finding in this file and it is the reason items 1, 4 and 5 all existed at all.**

**Not repairable here.** Nothing under `tools/` was edited and `git diff tools/` and `git status tools/` are both empty. A one-line fix in a controller-owned file.

## 12. MINOR — the phase ledger still reads the bootstrap phase after five hundred chapters

`state/phase-ledger.json` reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0`, `range: null`, `actualModel: null`. Because `attempts` never increments there is no durable record that any phase failed and had to be re-run, and any retry or fallback logic keyed on attempts has nothing to read.

**Reported, not repaired. A writer that writes its own phase status cannot be counted as having reached a phase.** Controller-owned.

## 13. MINOR — the compiled bytecode file is tracked in git and it degrades the only review surface a close has

`tools/__pycache__/measure.cpython-312.pyc` is tracked. `.gitignore` covers `logs/`, `*.log`, `.env*` and `.DS_Store` and nothing else. **Phase-level diffing is the surface this file is written against, and it is unreliable while that file moves in commits it has nothing to do with.** Named by many phases. One line, and not this phase's file.

## 14. STRUCTURAL — the close could not repair the premise, and the reason is not a writer's

`bible/premise.md` describes a system-apocalypse market novel. The manuscript is a yard on a bank. `Adrian` is in 43 chapters of Volume 01, 30 of Volume 02, 15 of Volume 03, 1 of Volume 04, and none in Volumes 05 to 10. `Mara` is none after Volume 03. `auction` is none after Volume 04.

**Every contract in this repository adds prohibitions and none of them removes any, and each forbids the phase that would write the thing that would close the gap, while the gap is measured by every phase and closed by none.** This close was told to weigh it and not to repair it, and it did not repair it and did not repair one piece of it.

**The defect is that the question has now been named in six block records, one review, one close and one roll and has an owner in none of them.** The specific question — whether a close is allowed to open the premise question rather than only weigh it — has to be answered by a person before Volume 11 is outlined, because every contract after Volume 11 will be written against the answer.

## 15. STRUCTURAL — the state layer's own convention is the reason its figures should be distrusted

`NOVEL_SPEC.md` records that this repository's capitals style produced seven verifiably false figures in Volume 04 Batch 0002. **This close wrote its three documents and its five appends in ordinary sentence case on purpose, and the reason is that a document that shouts is a document nobody checks.**

The defect is that the convention is not enforced anywhere and is carried by each phase's own discipline. **It survived into this phase's own work before this phase corrected it: the close record as first written carried two wrong cells and a wrong day map (items 1 and 2) and was written in the same register as the documents it was criticising.** Being measured in the same instrument as everything else turns out to be the part that matters, and the register is the part that made anyone look.

---

## 16. BLOCKER — the close record asserted the number of its own in-place edits and got it wrong

**The close record section 16 and the head of the block appended to `state/current.md` both said that four live header lines had been changed in place, and that `Last completed chapter:` had not been touched. Five lines were changed and it was touched.** `git diff -U0 state/current.md` against the checkpoint shows hunks at lines 7, 9, 11, 13 and 15 — `Current phase:`, `Current batch:`, `Last completed chapter:`, `Last batch summary:` and `Next phase:`.

Two things went wrong and they are the same mistake. The first is that the edit was applied by searching for a key string from the top of the file, and the key `Current phase:` occurs twice — once inside the instructional blockquote at line 4, which is a historical note about a staleness that was already repaired, and once on the live line. The script found the blockquote first and rewrote that, leaving the live line stale; the blockquote was restored from the checkpoint and the live line then changed, and the restore was verified against `git show HEAD:state/current.md`. **The second is that the documents asserted a count of their own edits without taking the count from the diff.** If it had read `git diff --stat` or `git diff -U0` before writing the sentence, it would have found five.

**This is item 1, item 4 and item 11 again, in the close's own instruments: a figure produced by a method the writer did not write down, believed because it was plausible, and printed. A document that states how much of itself it changed is describing its own measurement and gets the same discount as any other.** Both documents now say five lines and name what each one changed for.

## 17. MAJOR — the fourth closing-ledger repeat was named from a different measurement, and the doubled-day claim built on it was wrong

**Found by re-deriving the closing-ledger column group by group and printing the opening of every colliding chapter, which the close had not done.**

Measured, over all sixty files: **56 distinct five-word openings in 60 closings, which is four repeats, in three groups.**

| the closing opens on | chapters | days |
|---|---|---|
| `The man of about thirty four` | 443, 445, 449 | 3, 4, 8 |
| `The boy of about nineteen` | 444, 446 | 3, 5 |
| `A clerk of nineteen years` | 464, 496 | 21, 47 |

**The close printed the fourth as 480 with 498. Chapters 480 and 498 close on `Three certainties went onto one page of a clerk's book` and `Four certainties went onto one page of a clerk's book`, which are two different sentences, and the pair is the third identical-paragraph pair at section 15 of the close record.** A pair from the duplication sweep was carried into the closing-ledger sweep and printed as a finding of it, which is the same failure as item 1: two measurements agreed with each other because one of them was copied, and the copy read like a citation.

**The dependent claim was wrong too, and it is the more useful half of this item.** The close printed that two of the four repeats are the first half of a doubled day, and that this is the sixth time a doubled-day pair sits where something repeats itself. Day 3 is the first doubled day in the volume and it carries Chapters 443 and 444, and **each of the two heads one of the two front groups: 443 is the first half of day 3 and opens its closing like 445 and 449, and 444 is the second half of day 3 and opens its closing like 446.** So one of the four repeats involves a first half and one involves a second half, and the third group, 464 with 496, is the only one of the three that is not in the first block at all. A doubled-day pair sitting where something repeats itself is still the shape this repository keeps meeting and the count of how many times is not something this file can verify and is not printed as a finding any more.

**Repaired** at `state/volume-10-close.md` section 3.2 and section 19, at `state/volume-10-roll-summary.md` section 5.5, and in the state appends. The close record's own section 18 and section 19 claims about the pair were the only other places it was printed, and both are corrected.

## 18. MINOR — the volume has three arithmetic deviations and every document in this phase said two

**Found by the item 6 scope repair and not by looking. It is listed separately because it changes a number that a Volume 11 writer would have taken as final, and because the review as first written asserted the opposite in its own preamble.**

Chapter 455, day 14, prints five marks in chalk where `c` less seven gives seven, and five is the figure Chapter 453 prints on day 12. It is the third location in the volume that is off its own ladder, after Chapter 490 and Chapter 500, and the first of the three in reading order. The close record's section 19 also printed the Chapter 500 pair as *the one arithmetic error in the volume*, which contradicted the close record's own section 6 and section 6.1, and both of those had already been right about two.

**Reported, not repaired: Chapter 455 is canon.** Carried as a liability in the roll at section 0.3, in the close record at section 6.2, in `state/current.md` at section 4, in `state/continuity.md` at section 3 and in `state/open-threads.md` at section 2, where it is opened as a thread, and the honest position is the one taken for Chapter 490: the volume nowhere says the man missed two mornings and nowhere says he did not, and this file does not decide it.

## 19. What this review did not find, and what that does not mean

**Eighteen items and every one of them is a defect.** There is no item here reporting that a measurement came out well, and that is deliberate and it is also the review's own bias: a self-review that lists successes is a document nobody can act on, and a self-review written by the writer is a document whose omissions cannot be counted. **The absence of a nineteenth item is not evidence that the volume is sound.**

Specifically, this review did not independently re-derive, from the chapters and without the close record's assistance: the anchor test's eighteen columns, the figure table at section 7, the thirty-one weighed items at section 10, the four sentences at section 1, or the twenty-five prohibitions inherited from `outline/batches/volume-10-batch-0004.md`. **Those were carried from the close record on the strength of the checks that were run, which were: the calibration in five figures, the counting motif in 176 claims and 0 mismatches, the denominator, the `wc -w` band and its two extremes, the shared twelve-word-run volume figure and its four block figures, the three identical paragraphs and their three boundaries, the reserved scan, the footer scan, the six relay totals and their silence lists, thirty-nine of the forty-one day-list cells, and the fifteen ladder columns at section 5.1. Everything else in the close record rests on the writer having been right the first time.**

**And the sentence above is now the wrong sentence, because three of the figures it says were not re-derived have now been re-derived and three of them were wrong.** The closing-ledger repeats, the `a wall` split and the chalk scope have each been measured again from the sixty files, without the close record in hand, and each moved. **A list of what a document did not check is not a list of what is right, and this one was the closest thing in the file to an assurance and it was the assurance that let three figures stand.**

---

## 20. Disposition

**Repaired in the documents this phase owns: items 2, 3, 4 (in the two documents), 5, 6, 7, 8, 16, 17, 18, and item 1's table.**

**Reported and not repaired, because the file is not this phase's: items 4's three source documents, 6's and 8's three inherited documents, 11's tool, 12's ledger, 13's `.gitignore`, 14's premise.**

**No repair available at all: items 9, 10, and the three arithmetic deviations in Chapters 455, 490 and 500, all of which are in a closed volume.**

**Nothing was restarted, no chapter was written, no chapter was edited, and no plot, no count, no character state and no owed sentence moved. The batch was not reopened.**

**No chapter was edited. No outline was edited. No earlier volume's record was edited. No block record was edited. No entry was created in `state/phase-ledger.json`. Nothing under `scripts/`, `.github/workflows/`, `.opencode/agent/`, `tools/`, `state/archive/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md` or `opencode.json` was edited. And no next phase, no next batch directory and no next prompt was created, because the phase after a close is the controller's.**
