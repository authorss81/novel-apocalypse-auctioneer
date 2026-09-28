# Volume 10 Close Review

**This is the Volume 10 close's self-review. It is a list of defects and not a list of things that came out well. It was written by the same agent that wrote the close, and that fact is the first defect on the list and not a footnote to it.**

**Nothing was restarted. No chapter was written and no chapter was edited. Chapter 500 and Chapter 490 are canon and the two arithmetic deviations in them are reported at full size in `state/volume-10-close.md` section 6 and left standing. Every figure below was measured by re-running the measurement over the sixty chapter files, not by reading the close record's own claims, and every measurement in the close record that could be checked was checked again from the chapters.**

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

## 6. MODERATE — the inherited scope for the marks in chalk was understated, though its formula was correctly reported

The inherited block record and the inherited contract both give the formula for the marks in chalk as *fifteen plus `c`*. **That is seven out at every cell and the close record caught it.** What the close record then reported as the scope — twenty-four chapters on twenty-one days — is itself short.

Re-measured with a wider pattern that takes both surface forms, `there are N marks in chalk` and `there are N of them in a row`: **26 chapters across 22 days, from day 12 (Chapter 453, five marks) to day 50 (Chapter 500, forty-three), with zero cells failing `c` less seven.**

So the close record got the right formula, named the right two-day gap in its count of chapters and days, and was still two chapters and one day short. **This is the seventh time this repository has had to say that a figure taken from an inherited document is a figure about that document's own fifteen chapters and not about the volume**, and the close record says so itself about `a foot and a half` at section 14 while carrying a wrong scope for the chalk in the same table.

**Repaired** in both documents.

## 7. MODERATE — the close record's own paragraph runs contain two literal `\n` sequences

`state/volume-10-close.md` section 15, at the paragraphs beginning "All three duplicated paragraphs straddle a block boundary" and "And the volume figure of 7,626", each end with a backslash-n as two characters rather than a newline. **A close that publishes a measurement of markdown integrity at section 15 and then ships a markdown defect in the same section is not measuring the same document it is publishing.** This is the same class of error as item 1 and item 4: the instrument and the thing measured came apart.

**Repaired.**

## 8. MODERATE — three of the twenty-five things a close may not do were broken in prose, and the close could only report them

`outline/batches/volume-10-batch-0004.md` section 5 forbids using a wall, a lane, a gatepost, a rubbed heading, or a looking in front of one as a device. Measured over the volume:

- `a gatepost` — 2 occurrences, both on day 33 at Chapter 479, both the sheet nailed to a gatepost nine hundred yards off. A gatepost used as a device and a looking in front of one used as a device, both, in one chapter.
- `a lane` — 1 occurrence, day 9, Chapter 450, a man walking down a lane recalled inside a comparison.
- `a wall` — 29 over 15 days, of which **four are the wall the three columns that are a day out stand on, at Chapters 486, 491, 498 and 499.** Twenty-two are the low wall at the foot of which the man of about sixty-four sits and four are the yard's own wall. **The four are the wall the central pressure of the volume stands on, used in four chapters of the last block, and the block record and the canon card both printed the count as eighteen and both printed every one of them as the low wall. Both were wrong and the count of wall-as-device occurrences is four, not zero.**

**None of these is a close's to repair, because Chapters 479, 450, 486, 491, 498 and 499 are canon.** They are weighed and printed. The honest summary is that a prohibition inherited into a close's own list of things it may not do was broken six times in prose, and the phase whose job is to weigh had nothing to weigh it with except a count.

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

## 17. What this review did not find, and what that does not mean

**Seventeen items and every one of them is a defect.** There is no item here reporting that a measurement came out well, and that is deliberate and it is also the review's own bias: a self-review that lists successes is a document nobody can act on, and a self-review written by the writer is a document whose omissions cannot be counted. **The absence of an eighteenth item is not evidence that the volume is sound.**

Specifically, this review did not independently re-derive, from the chapters and without the close record's assistance: the anchor test's eighteen columns, the figure table at section 7, the thirty-one weighed items at section 10, the four sentences at section 1, or the twenty-five prohibitions inherited from `outline/batches/volume-10-batch-0004.md`. **Those were carried from the close record on the strength of the checks that were run, which were: the calibration in five figures, the counting motif in 176 claims and 0 mismatches, the denominator, the `wc -w` band and its two extremes, the shared twelve-word-run volume figure and its four block figures, the three identical paragraphs and their three boundaries, the reserved scan, the footer scan, the six relay totals and their silence lists, thirty-nine of the forty-one day-list cells, and the fifteen ladder columns at section 5.1. Everything else in the close record rests on the writer having been right the first time.**

---

## 18. Disposition

**Repaired in the documents this phase owns: items 2, 3, 4 (in the two documents), 5, 6, 7, 16, and item 1's table.**

**Reported and not repaired, because the file is not this phase's: items 4's three source documents, 8's six chapters, 11's tool, 12's ledger, 13's `.gitignore`, 14's premise.**

**No repair available at all: items 9, 10, and the two arithmetic deviations in Chapters 490 and 500, all of which are in a closed volume.**

**No chapter was edited. No outline was edited. No earlier volume's record was edited. No entry was created in `state/phase-ledger.json`. Nothing under `scripts/`, `.github/workflows/`, `.opencode/agent/`, `tools/`, `state/archive/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md` or `opencode.json` was edited. And no next phase, no next batch directory and no next prompt was created, because the phase after a close is the controller's.**
