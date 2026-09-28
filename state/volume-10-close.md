# Volume 10 Close — *The Unfinished Sale*, Chapters 441 to 500, days 1 to 50

> This phase is the volume close. It wrote no chapter. It created this file, `state/volume-10-roll-summary.md` and `reviews/volume-10-close-review.md`, and it appended to the five live state files. It did not create a next phase, a next batch directory, a next prompt, or a roll for a later volume. It did not edit a chapter, `outline/series.md`, `outline/ending.md`, `outline/volume-09.md` or `outline/volume-10.md`, anything under `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md` or `opencode.json`, and it did not open anything under `state/archive/` or `tools/`. It made no entry in `state/phase-ledger.json`.
>
> The volume is sixty chapters on fifty days. The ten days that carry two chapters are 3, 16, 19, 22, 25, 30, 33, 36, 43 and 48, and each of those two is a morning and its afternoon. `c` is the day index and it runs 1 to 50; `c = 0` is Chapter 440, the last day of Volume 09. Forty days carry one chapter and ten carry two, and `50 + 10 = 60`.
>
> Every figure under a heading that says measured was measured from the sixty chapter files after the last prose edit. Where a chapter and this record disagree, the chapter is canon and this record is wrong. Where a document and the chapters disagree, both are printed and neither is repaired.
>
> The method for every figure that came out of `tools/measure.py` is the same every time and it is this: `python3 tools/measure.py calib` returns 53 class-one claims, 0 mismatches, a denominator of 25,569, a `wc -w` total of 25,689, 675 shared twelve-word runs, one identical paragraph and zero class-two claims. All five reproduce, and the calibration was run before anything was measured and again after everything was written. The tool is hard-coded to Chapters 241 to 250 for every mode but `calib`, so it was run for this volume through a wrapper in a temporary directory that imports the module and calls its own functions. `PYTHONDONTWRITEBYTECODE=1` was exported before every run because `tools/__pycache__/measure.cpython-312.pyc` is tracked in git. `git diff tools/` and `git status tools/` are both empty.

---

## 1. The four sentences this close owes, in a body, and nowhere else

**These are the four sentences the last three closes owed and did not pay. Each stands alone. None is defended, unqualified or pardoned, and none is followed by a paragraph about why the route was reasonable. They are in the narrator's register, which is the register the chapters are in: a sentence about a thing, with a figure in it, and no adjective doing work a figure could do.**

**One, on the figure nobody had to put down, and on what this district did with one.**

> This district spent five volumes learning to write down when, and then it put a stone under a book and let a book keep its own count, and nobody turned that stone over for two volumes, and when it was turned over the count could not be a day out and it could not be checked either, and that is the whole of what this district did with a figure it was never obliged to have.

**Two, on the column that was named more and never filled.**

> A column for the name of whoever read a thing out loud was ruled in this yard before this volume began and it is ruled and it is empty at the end of the fiftieth morning, and across sixty chapters on fifty days it was named seventy-six times, and a clerk read an entry out loud in front of about nineteen people on more days than that, and nobody was asked for a name on any of them, and there is no job in this district for that column to hold a name for, because the reading is done by whoever is standing in the yard and standing in a yard is not a post.

**Three, on the fifth of the five things this district does not have, and on why saying it out loud did not pay it.**

> The fifth of the five things this district does not have is a way to pay a person who is not in a household, and on the thirty-sixth day a man who has refused to read anything out loud in that yard for a volume put his own hand on a book and said the fifth of the five out loud in front of about nineteen people with the man it is about four feet away, and a clerk entered that saying it in front of those people was not paying it and was not going to be, and the clerk was right, and it is not paid, and six things stand in that yard that are not a payment and none of the six is one, and the count of the five is still five.

**Four, on the body four hundred miles off and the figure on the sheet.**

> The figure on the sheet at that gatepost is a count of the people who answered a door, and it has said four hundred and eleven on fifty days of this volume and has not moved on one of them, and the body that printed it is a hundred and seventeen days past a printing it did not make and it has no face, and a habit is not a person and a count of answerers is not a count of the people, and the sheet has no day-count of its own and never has had one, and no arrival of anything is written down anywhere in these sixty chapters.

**And the disclosure that goes with the fourth, because a later volume should not have to find it. `outline/volume-10.md` section 15.1 owes this volume two sentences and pays both of them itself, in the outline: the first about the third line of that lot book, the second about the figure on the sheet. Neither sentence is on any of the sixty pages. `a count of the people who answered a door` is at zero across the sixty files, `carries its own expiry` is at zero, `stop being true` is at zero, and `a habit` is at seventeen occurrences without ever being attached to the figure on the sheet. The second half of the finding — that a public record that carries its own expiry is a record of the person who watched it stop being true, and that a district wanting a public record of a thing and not of a person cannot have one that carries its own expiry — was said out loud in a yard four times in thirteen days in a different wording and was never entered as that sentence, and it is not paid here either except in the sentence above. The fourth line of the offer is a separate matter: it is on this volume's own list of things the climax may not spend, it was not read out, and it remains unread. A close may not pay it and has not tried to.**

---

## 2. What was measured, and in what order, and why the order is the finding

**The order this close worked in was: measure the prose, then weigh the prose against itself, then answer, then record. A close that answers first and measures afterwards writes a document that agrees with itself. The three figures below are the reason the order is not academic.**

1. **`outline/volume-10.md` section 10.4, the volume's own resolution paragraph and the check that follows it, is wrong on six of the eight figures it names, right on two, and one of the eight is two high rather than one.** The paragraph says 282 for the ninth of the nine printed nights, 190 and 189 for the man of about sixty-four, 149 for the bid, and 399, 715, 430 and 390 for the four figures a man of fifty-six reads. The sixty chapter files give 281, 190, 189, 148, 398, 714, 428 and 389. The two figures about the man of about sixty-four are not a document error at all: they are what Chapter 500 prints, and Chapter 500 is the one chapter in the volume where two of its figures are a day high. That is section 6 below and it is the most consequential thing this close found.
2. **The handoff prompt's own ladder table is two low on its `Pool` column on all fifteen rows of its last block**, `Pool` is at zero on the pages of all sixty chapters, and the outline's own table at section 6.1 prints the column correctly. Reported, not repaired; the prompt is not a file and the outline is not this phase's.
3. **The inherited block records carry two formulas the prose contradicts.** The marks in chalk along the edge of the second table are `c` less seven and not *fifteen plus `c`*, and the formula is seven out at every cell under every pattern, while the scope attached to it in the inherited record is right for the pattern that record used and is one of four scopes printed for the same measurement. The full reconciliation is at section 5.1 and the one cell that does not hold the ladder is at section 6.2. The count of things in that yard that are not a payment is six on fourteen chapters of this volume, and `seven things` is at zero across all sixty files, and the inherited record and the inherited contract both say seven. The chapters are canon.

**And the one figure a close may take from a document because it is inherited standing and is not on a page of this volume: the four hundred and eleven is the figure on a sheet at a gatepost four hundred miles from any water, it is a count of the people who answered a door, it is four hundred and eleven on fifty of fifty days of Volume 09 and on fifty of fifty days of this one, and there is no day-count for the sheet and its own tenure on that post is not a figure this canon has.**

**And a fourth, which this close found in itself and which is the reason the other three are believable.**

4. **Two cells of this record were wrong when they were first written, and re-measuring them from a clean day map found both — and found that the broken map was not why.**

The script that built the day index advanced a counter per chapter and then corrected for the doubled days, and that map is wrong from Chapter 489: it spends the doubled day 43 on Chapters 490 and 491 instead of 491 and 492, so the last twelve chapters are a day out. **A day count is not a nuisance and every "on N of 50 days" cell in section 14 is one, so the whole table was rebuilt from the two-chapter list forward and every cell recomputed.**

**Every total and every day count came back identical, and that is a worse finding than a broken map.** It means the off-by-one changed nothing in this table, because each of these strings is either on all fifty days or silent on a run the error never reached. **A map that is wrong and changes nothing is a map nobody will ever notice is wrong**, and the two cells that did turn out to be wrong were not cells the map touched: they were two cells written into this record by hand that the chapters did not support. **The form *was not run* is 61 and not 60 because Chapter 454 carries it twice, once inside the clerk's entry in its first line and once on a line of its own. `a habit` is 17 lowercase and 18 case-insensitive because the eighteenth is the Chapter 441 title, and this table's own stated convention is case-insensitive.** Both are corrected in section 14 and both are logged in the self-review. Nothing else in this record moved: 176 claims, 0 mismatches, the denominator, the `wc -w` band, 7,626 shared runs, 3 identical paragraphs, the six relays and the cap breach at Chapter 479 all re-derived exactly. **And the ladder at section 5.1 was built on the clean map and every one of its fifteen columns holds on fifty of fifty days, which is the check that the clean map is the right one and is not available to the day-lists at all.**

5. **A later pass over this record found three more figures in it that were wrong, and all three were the same mistake, and one of the three had a chapter in it.**

The chalk scope has been printed three times already, as twenty-four chapters on twenty-one days, then twenty-six on twenty-two, then twenty-seven on twenty-three, and **all three are defensible measurements of three different patterns, and none of them is the pattern the thing being counted needs.** A fourth pattern has now been run and the fourth scope is thirty-two chapters on twenty-seven days. All four patterns and all four scopes are printed together at section 5.1, and the second of the three turned out to be wrong by exactly one chapter for a reason worth a writer's time: a case-sensitive match misses a `There are` that opens a sentence. The closing-ledger repeat was named as 480 with 498, and that pair is the third identical-paragraph pair from a different sweep. The `a wall` split was printed as twenty-two, four and three, and the yard's own wall is not in the volume. **All three defects are corrected in place at sections 5.1, 3.2 and 14, in the roll, and in the five state appends. One of them found a chapter, which is Chapter 455 and section 6.2, and that is the reason a repair of a table cell is not always a repair of a number.** The pattern this record kept making is worth naming once: a figure was believed because the number it produced was plausible and because the sentence around it read like a measurement, and in all three cases the sentence was the part that was wrong. **A close that prints a pattern beside a scope should be read as printing the pattern first and the scope second, and when the two disagree, the pattern is the finding.**

---

## 3. The ten columns this volume owes its close, each with sixty cells and a checked total

`outline/volume-10.md` section 14.4 names the ten. Each is measured here over all sixty files. Every column has sixty cells, and every column is added and checked against the total printed beside it, because a column with fifty-nine cells for a volume of sixty is a defect, and a column that does not add up is a defect whatever the figure is.

### 3.1 The opening shape. Zero of sixty, against a cap of five of sixty.

Method, named in advance by the outline: for each of the sixty files, take the first non-empty line that is not a chapter header and not a horizontal rule, and test it against `The [a-z-]+ of the [a-z-]+ month came in`.

**Cells: sixty zeros. Sum: 0. Matches: 0 of 60. The sixty first lines are sixty different sentences.**

The inherited figure, re-measured over Volume 09's fifty files, is zero of fifty, and this volume carries zero of sixty. A cap of five of sixty was set before a word of prose existed, and zero is the argument and not a target beaten. The inherited shape died by writing in Volume 09 and stayed dead.

### 3.2 The closing ledger. Zero of sixty open on a time of day, and fifty-six distinct openings in sixty closings.

Method: the closing passage is the last non-empty paragraph of the file, and the first five words of it are taken. A chapter fails if those five words name a time of day or a change of light before they name a person.

**Cells: sixty zeros. Sum: 0. Failures: 0 of 60. Distinct five-word openings: 56 in 60. The four repeats are 445 and 449 against 443, 446 against 444, and 496 against 464 — which is three groups and four repeats, and the three groups are `The man of about thirty four` at Chapters 443, 445 and 449, `The boy of about nineteen` at Chapters 444 and 446, and `A clerk of nineteen years` at Chapters 464 and 496.**

The three blocks before the last one each measured zero of fifteen. The model is Chapters 438 and 439. The inherited shape opened *By the time the light* on eleven of Volume 09's fifty closings and is on none of these sixty. The cap was not re-argued and no chapter found a way around it.

**The repeats are named rather than left, and the naming matters more than it looks, because the first pass of this record named the wrong pair and got it from the wrong measurement. The three groups are the closings of Chapters 443, 445 and 449, of Chapters 444 and 446, and of Chapters 464 and 496. The first pass printed the fourth as 480 with 498, and Chapters 480 and 498 close on `Three certainties went onto one page` and `Four certainties went onto one page`, which are two different sentences; 480 and 498 are the third identical-paragraph pair at section 15, and a pair from one sweep was carried into another.**

**What the doubled days actually do here is the opposite of what this record first printed. Day 3 is the first doubled day in the volume and it carries two chapters, and each of the two heads one of the two front groups: 443 is the first half of day 3 and opens its closing like 445 and 449, and 444 is the second half of day 3 and opens its closing like 446. So one of the four repeats is a first half of a doubled day and one is a second half, and the third, 464 with 496, is a repeat between two ordinary days, and it is the only one of the three groups that is not in the first block at all.** The earlier claim that two of the four were the first half of a doubled day was wrong, and a doubled-day pair sitting where something repeats itself is still the shape this repository keeps meeting; what is not supported is the count.

### 3.3 The figure on the sheet. Sixty-two, on fifty of fifty days, against a cap of sixty.

**Per-chapter column, sixty cells: one on every chapter and three on Chapter 479. Sum: 62. Days: 50 of 50. The cap is one a chapter, every chapter, which is 60.**

**`outline/volume-10.md` section 14.4 item 2 predicted, before any prose existed, that the volume would carry sixty-one: the figure will be on sixty of them and the total will be sixty-one, and that is the cap kept and not beaten. Measured, it is sixty-two. The cap is one a chapter and the volume is two over it, and the close is required to say so rather than to say the figure less often. It is not said less often. It is on all fifty days, once a chapter, and twice more on one day.**

**The two extras are on one day, and the reason is on the page. Chapter 479 is day 33, and on day 33 the third of the four figures a man of fifty-six reads — nobody having entered anything — is four hundred and eleven, which is 378 + 33, and that is the same figure to the last digit as the one on the sheet nine hundred yards off that wall. A boy of about nineteen is the only person in that yard who has noticed, and the chapter says so, and the clerk enters that she does not know whether a number she did not make is a figure and rules no column for it. So the cap was exceeded by exactly the number of times the district's own figure and the figure it borrowed came out equal, and on that one morning the yard held a coincidence and nobody treated it as one. The figure on the sheet did not move, and neither did the third of the four.**

### 3.4 The length band. All sixty inside, and the longest mean of the four blocks.

**Per-chapter column of `wc -w`, sixty cells, given in the roll. Total 143,944. Mean 2,399.1. Minimum 2,236 at Chapter 481. Maximum 3,186 at Chapter 467. Chapters outside the band of 2,200 to 3,200: none.**

Inherited, Volume 09: mean 2,419.5, minimum 2,182 at Chapter 399, maximum 2,839 at Chapter 411, forty-nine of fifty inside. The four blocks of this volume, each measured over its own fifteen after its own last edit: Batch 0001 2,388.1, Batch 0002 2,435.3, Batch 0003 2,360.9, Batch 0004 2,399.1. **No chapter was padded to fill a band and no chapter was cut to fit one. Chapter 467 at 3,186 is fourteen words under the ceiling, and it is the chapter that counts the length of a month nobody counted, so the one long chapter in the volume is long because it is doing arithmetic out loud.**

### 3.5 The *about* hedge. Three thousand nine hundred and seventy-nine, the highest rate in the repository.

**Per-chapter column of sixty cells, given in the roll. Sum 3,979. Mean 66.3 a chapter. Denominator 143,220. Rate 277.8 per 10,000 words.**

The line, in order: 253 per 10,000 in Volume 09 over a denominator of 120,329; 294 at Batch 0001; 284 at Batch 0002; 257 at Batch 0003; 274 at Batch 0004; **277.8 over the whole volume.** No document in this repository sets a cap on a hedge and none is set here, because a cap set in advance on a hedge is a rule. The figure rose across the volume from the block that was lowest, and the rise is printed. The one measurement that would explain any part of it is a count of hedges inside a figure's own sentence against a count inside a person's, and nobody has run it, and this close did not invent it at the end of a volume.

### 3.6 The six protected relays. Four at fifty of fifty days, one at forty-seven, one at forty-two, and the one at forty-two is a fall that was made inside a block and reported.

Convention: whole string, per occurrence, case-insensitive, per file. All six strings are named verbatim as the inherited contract names them. None was lowered by deletion and none was raised to fill a page.

| the string | total | days of 50 | the days it is silent on |
|---|---|---|---|
| `the record about the not asking says not asked` | **374** | 50 | none |
| `read the number back to himself in a low voice` | **194** | 50 | none |
| `at the foot of that low wall with his coat folded on the stones` | **50** | **42** | **26, 28, 29, 31, 32, 34, 36, 37** |
| `was not asked about the eleven miles` | **56** | **47** | 29, 34, 37 |
| `got it up about nine inches` | **59** | 50 | none |
| `by ten there were about nineteen people` | **60** | **50** | none |

**The finding is the third row, and it is the first time a protected relay in this manuscript has fallen, and it fell by two thirds inside one block.** The relay that carries the man of about sixty-four is on thirty of the thirty chapters of the first two blocks, on four of the fifteen of the third, and on sixteen across the fifteen of the last, one chapter of the last block carrying two. `state/volume-10-batch-0003-summary.md` printed it at fifteen of fifteen at `head` and four after its own review repair, and both figures are in that record, and the repair was made to take a time of day out of a protected string. What the repair took out was the sentence that put the man on the stones. The block record named the loss, the next block did not put it back, and the volume closed with the man of about sixty-four off the page for eight days in the middle of it.**

**The standing is unchanged and it is printed here rather than acted on: none of the six may be smoothed by deletion, and a block that lowers one has destroyed a measurement. This close did not lower it, did not raise it, and did not repair the eight missing days, because repairing them would be writing prose into a closed volume. The figure is 50 on 42 of 50 days and it is the lowest any of the six has ever stood. The man it carries is the one person in this volume who was given nothing on every one of fifty days, so the loss of the relay and the giving of nothing are the same fact, and neither of them is a decision anybody made on the page.**

**The sixth row is worth one line for a different reason. `by ten there were about nineteen people` is on sixty of sixty chapters, one a chapter, and it is the one relay the volume held exactly. It is also the one the block before the last lost from five chapters and put back. The cap on it is a rate of one a chapter, the volume carries that cap exactly on every chapter, and the two days that carry two chapters each carry it once.**

### 3.7 The shared twelve-word-run figure. Seven thousand six hundred and twenty-six, and it is lower than the sum of its own four blocks.

**Volume figure, under the tool's own method: 7,626 shared twelve-word runs, which is 127.1 a chapter. The four blocks measured over their own fifteen under the same method are 1,597, 2,065, 2,202 and 2,347, which sum to 8,211. The volume figure is 585 lower than the sum of the four block figures.**

Volume 09 found the same thing in the other direction: its volume figure of 4,837 exceeded the sum of its five block figures, 4,324, by 513. **The direction has reversed, and the reason is structural and not a matter of prose getting better or worse. A run that appears in all sixty chapters is one run in the volume figure and four in the sum of the block figures, because it is shared inside each block. The six protected relays and the two standing ledger clauses are on fifty, fifty-nine and sixty of the sixty chapters, so the frame carries the volume figure down and lifts the sum. Any close that prints the volume figure beside the sum of its block figures and calls the difference a trend is reading the shape of the frame and not the shape of the writing.**

**The per-chapter column of shared runs, sixty cells, is in the roll. It is not additive and must not be added: the additive sum of the column is 46,113, which is a figure about nothing, because a run shared by six chapters is counted once in each of those six cells.**

**And the largest commercial risk in this manuscript is this figure, in `outline/volume-10.md` section 14.5, in the outline's own words: the pages are dominated by ledger enumeration, `out loud` is on all fifty days and rose, `a figure` is on all fifty days and rose, and the column for the name of whoever read a thing out loud is named on more days than any of them and is still empty. Measured over this volume: `out loud` 889 on 50 of 50 days, `a figure` 773 on 50 of 50, `clerk` 901 on 50 of 50, `clerk of nineteen years` 557 on 50 of 50, `a clerk of nineteen years entered` 404 on 50 of 50, `about four` 521 on 50 of 50, and the column named 76 times on 49 of 50 days and empty on all of them. The frame is intact, the frame is the risk, and this volume added a table, a stone, a chalk mark and a twenty-column ladder to a yard that already had four figures on a wall, which is what section 14.5 said would happen, and the warning was in the file before the first chapter was written.**

### 3.8 The counting motif. One hundred and seventy-six claims, sixty cells, zero mismatches.

**Per-chapter column of sixty cells, printed in full in the roll, summing to 176. Mismatches: 0. Claims of the second class, in the form *in N words*: 0.**

In order across the volume: 1.4 a chapter in Volume 09 over 120,329 words; 1.4 at Batch 0001 on 35,831; 2.5 at Batch 0002 on 36,355; 3.9 at Batch 0003 on 35,259; 3.9 at Batch 0004 on 35,775; **2.9 over the whole volume on 143,220.** The rate climbed across the first three blocks and held across the fourth, and over the volume it sits at 2.9, which is higher than anything before this volume and lower than the last two blocks of it. The first two blocks of this volume are the two thinnest the manuscript has carried, at 1.4 a chapter, and they are the two blocks in which the counting figure was not the thing the chapters were about. A figure that reproduces is not a chapter that is sound. The two chapters in Volume 09 with no counted claim at all are still the two a reader would rather read, and **this volume produced no chapter with no counted claim at all: the column's minimum is one, not zero.**

**Every one of the 176 claims was set by measuring the printed sentence and writing the claim afterwards, and all 176 resolve. That is the strongest single fact this close can print about the volume's arithmetic, and it is not a fact about the volume.**

### 3.9 The panel count. Zero panels, and two quoted-block lines that are not panels.

**Quoted-block lines across the sixty files: 2, at Chapter 443 and Chapter 445, one each. Both are a line of that lot book: the first line at Chapter 443, the second line at Chapter 445. `outline/volume-10.md` section 13.3 says a document line that exists to be reproduced character for character is not a panel and is not a second system. The exemption applies to both, and the panel count for the volume is zero against a cap of one in a chapter and two in a block.**

A close that counted lines beginning with `>` and printed two would have published a false figure against its own contract, and the two lines are the first and second lines of the object the whole volume is about. None is a virtue and none is a reward, and zero is not the panel running out.

### 3.10 The counts that may not be made larger, each checked against its own page.

Every one of these held its figure across the volume, and every move is on a page where a person and a reason were in the room.

| the count | figure | scope, measured |
|---|---|---|
| things this district has made | **12** | entered as twelve on every chapter from 450 to 500, moved once at Chapter 448 with the reason in a mouth |
| things this district does not have | **5** | the fifth named on 50 of 50 days, 64 occurrences, the count of five is five, and no sixth was proposed on any of the fifty days |
| instruments built and not named | **6** | a worn stone and a second stone were each entered as not a seventh, with a person in the room, on the day each went on |
| documents this district does not own | **3** | a stone, a table and a chalk mark were each refused as a fourth, in a mouth, on the page |
| protected things | **5** | a second reader was asked for in a yard and refused out loud with a reason, and a stone and a table were each refused as a sixth |
| conditions with no end on it | **4** | a wear is not a condition, and the end of a wear is the part nobody wrote down, and that is on the page at Chapter 500 |
| readings of the rival record | **7** | the third line of that book, a stone and a mark in chalk were each refused as an eighth, in a mouth |
| different ninths in this district | **5** | a stone is not a sixth ninth and a wear is not a ninth of anything, said out loud in a yard |
| refusals to read | **9** | a clerk refused twice in front of about nine people, said she could read it and was not going to, read it on the third morning, and the reading did not advance |
| refusals with no reason a clerk of a house has given | **8** | did not move on any of the fifty days |
| refusals of eleven coppers a week | **9** | did not move, and `eleven coppers` is at zero across the volume |
| refusals about the ninth holding | **7** | did not move, and the three figures are three figures and are not added together |
| boards and lines full | **5 / 6** | nobody put a line on a board on any of the fifty days, and a chalk mark a morning is a count of marks and not a line on a board |
| columns of not-askings | **4** | no fifth ruled, and a column on a stone is not a column |
| a rate turning a year into coppers | **none** | a wear is not a rate, a stone is not a price, and a chalk mark a morning is not a wage, all three said out loud in a yard |
| a new person added to this district | **none** | nobody arrived on any of the fifty days |
| the System panels | **0** | against a cap of one in a chapter and two in a block |

---

## 4. The two figures in the open at once

`outline/volume-10.md` section 10.2 fixes the reversal in one sentence: the only figure in this district that cannot be a day out is a figure nobody has to enter, and the only figure nobody has to enter is a figure nobody can check. The volume built the instrument and the volume paid for it. What is on the page at the last morning, measured:

- **The wear.** One inch deep in the middle of the underside of a stone lying face up on the end of the second table, and nothing at either end. It is a figure about a book standing still on a table. It cannot be a day out from a day it does not name, and it cannot be checked by anybody, including the man who put his thumb in it for about two minutes and a half on the fiftieth morning.
- **The three columns.** Carried on a board a stranger can walk up to and read. Three of the eighteen figures on that board are a day out from the days they name. They can be put right by writing a newer figure beside them and have not been, and a clerk has been asked out loud whether a person is allowed to write a newer figure beside an older one and has said that a person is allowed.
- **A clerk of nineteen years has entered two figures in one entry and has refused, out loud, to enter which of the two she means**, and has entered that she does not know which of the two is the better one, and has said she would rather the page sat there being useless than have her pick one in a yard because about nine people made a face.
- **Four mouths said out loud in thirteen days that the two cannot be compared.** None of the four was about a hand, or about the man who reads the figures, or about anybody. None of it is a rule. The two halves of the reason a bid cannot be run on were read out loud three times in five volumes and were not joined, and joining them would put on a page the thing that the bid is finished.

**The volume ends with both figures in the open and neither of them chosen, and section 10.2 forbids that being resolved, and a close may not resolve it and has not. What a close owes instead is the sentence, and it is the first of the four at section 1, and it is paid there.**

**And the finding this volume arrived at twelve chapters before it was due: a column can be named more often, on a page, by more people, and go emptier. Measured, the column is named seventy-six times on forty-nine of fifty days and is empty at the end of the fiftieth morning, and a clerk read an entry out loud in that yard in front of about nineteen people on more days than that, and nobody was asked for a name on any of them. The occurrence count went from sixteen on Batch 0003's fifteen to twenty-eight on Batch 0004's fifteen to seventy-six over the volume, and the column did not fill. That is the finding. It is on the page in four mouths and in a clerk's entry, and nothing in this volume settles it.**

---

## 5. The three columns that are a day out, the anchor test, and the figure the protagonist is afraid of

**The anchor test runs, and its failing column is the one the volume is about. Re-derived at `c = 0` from each column's own named day and not from the constant: seventeen of the eighteen re-derivable columns hold somewhere, three of them only on the inclusive convention their own anchors name, and `Unentered` does not hold. From the twenty-fourth of November of the seventeenth year to the seventh of the twelfth month is 379 days, and the board carries 378. Year 17 is 365 days, which `Board` at 348 and `Train` at 664 both require and which no document in this repository states; it is derived and not assumed.**

**The volume printed the board's figure on all fifty days and never printed the re-derived one. Measured cell by cell across the sixty files, with a parser this close wrote for the purpose and not the repository's, because the repository's tool cannot read any figure above a hundred written the ordinary way — see section 9 — the third of the four figures a man of fifty-six reads is `378 + c` on fifty of fifty days and is `379 + c` on none of them. The other three hold on all fifty days: `Board` at 348 + c, `Train` at 664 + c, `From2Jan` at 339 + c, and every cell of all four is its own day's cell.**

**Nothing is corrected, nothing is re-anchored, and the figure on the board wins on every one of the twenty columns. One of the three columns that are a day out is one of the four figures a man of fifty-six reads every morning, a clerk entered the difference as a day, a man was told in a yard in front of about nineteen people that one of his four was a day out, and he said nothing, and nobody asked him twice.**

**The figure the protagonist is afraid of, per section 5.3 of the outline, is a day. It was said once in this volume, on day 14, and he did not say it again and was not asked to. He said things out loud in a yard in this volume more times than in any volume before it and was asked for nothing and given nothing on any of the fifty days, none of the things he said put his own hand into the reason for anything, and his name is not on any page of the sixty or of the four hundred and forty before them.**

### 5.1 Every ladder in this volume, re-derived, and the intercept six documents print as a day-one figure

**This is the table a writer arriving for Volume 11 needs and it is not the table in the handoff prompt. `c` is the day and runs 1 to 50, and `c = 0` is Chapter 440. Six of the fourteen columns below are printed in the handoff prompt, in `outline/volume-10.md` section 6.1 and in `state/volume-10-batch-0004-summary.md` section 6 as the value at Chapter 441, and a writer who takes one of those six as an intercept is wrong on forty-nine of the fifty days. Measured over the sixty files, every cell, no figure taken from a document.**

| the figure | intercept at `c = 0` | formula | at `c = 1`, Chapter 441 | at `c = 50`, Chapter 500 | days of 50 it holds |
|---|---|---|---|---|---|
| the days on that board | 348 | `348 + c` | **349** | **398** | **50 of 50** |
| the days the train on that siding has stood | 664 | `664 + c` | **665** | **714** | **50 of 50** |
| the days nobody has entered anything | 378 | `378 + c` | **379** | **428** | **50 of 50** |
| the days from the second of January | 339 | `339 + c` | **340** | **389** | **50 of 50** |
| **how long the bid has been open** | **98** | `98 + c` | **99** | **148** | **50 of 50** |
| **how far back the ninth of the nine printed nights is** | **231** | `231 + c` | **232** | **281** | **50 of 50** |
| **how far behind the figure on the second line is** | **53** | `53 + c` | **54** | **103** | **50 of 50** |
| how long the rule said out loud has stood | 58 | `58 + c` | **59** | **108** | **49 of 50 — Chapter 490 prints 99** |
| how long it is since the first day of the eighth month | 128 | `128 + c` | **129** | **178** | **50 of 50** |
| **how far past a printing a body four hundred miles off is** | **67** | `67 + c` | **68** | **117** | **50 of 50** |
| **the age of the figure on that sheet, as a figure about the figure** | **189** | `189 + c` | **190** | **239** | **50 of 50** |
| **the night the man of about sixty-four is on** | 139 | `139 + c` | **140** | **189 — Chapter 500 prints 190** | **49 of 50** |
| **the nights of that run he has slept on** | 138 | `138 + c` | **139** | **188 — Chapter 500 prints 189** | **48 of 50** |
| the marks cut off that board since the mark for the first of the twelfth month | 7 | `7 + c` | **8** | **57** | **50 of 50** |
| the marks in chalk along the edge of that second table | — | `c` less seven | not in the yard on day 1 | **43** | **27 days, 32 chapters, days 12 to 50, 26 of 27 cells holding — Chapter 455 is the one that does not, see section 6.2** |

**The six in bold are the six a document prints as a day-one value and a writer may read as an intercept. The bid is the worst of the six, because 99 is a rounder figure than 98 and a writer who reaches for the round one will be a day out from Chapter 443 to Chapter 500 without once knowing it.**

**The first three of the four a man of fifty-six reads are `348 + c`, `664 + c` and `378 + c`, and the fourth is `339 + c`, and every cell of all four is its own day's cell. That is not a claim about the four; it is what the anchor test needs, and it is why the anchor test can be run at all.**

**And the marks in chalk: `c` less seven. This measurement has now been run four times in this repository, with four different patterns, and the four patterns and the four scopes are printed together here because the patterns are the finding and the scopes are only consequences of them.**

| the pattern | chapters | days | cells failing `c` less seven | who published it |
|---|---|---|---|---|
| `there are N marks in chalk` | **24** | **21** | 0 | the inherited block record, and the close's first pass. **Its scope is right for its pattern and only its formula is wrong** |
| the same, plus `there are N of them in a row`, matched case-sensitively | **26** | **22** | 0 | the close's first correction, carried into four documents |
| the same pair, matched case-insensitively | **27** | **23** | 0 | this close's second correction |
| every numbered form, case-insensitive | **32** | **27** | **1** | this close, and the pattern the table above is measured on |

**The second row is the one to look at, because it is wrong in a way no scope can warn a reader about.** Matching case-sensitively requires a lower-case `there are`, and that drops exactly one chapter, and the chapter is Chapter 453, whose first line of the book reads `There are five marks in chalk along the edge of that second table` with a capital on the front of the sentence. **A case convention quietly deleted the anchor, and the number it produced, twenty-six on twenty-two, is lower and tidier than the number it replaced, which is why it survived four documents.** This close has now been bitten by case sensitivity twice, in two different tables, and the second bite is the same shape as the first, which is the `a habit` cell: a count that a reader has to apply a stated convention to by hand, where a machine applying it mechanically gets a different number. See section 14 and `reviews/volume-10-close-review.md` item 3.

**The last row is the one the table above is measured on, and the reason is not that it is the biggest.** The volume prints the count in five forms: `there are N marks in chalk` in the opening ledger line of a chapter, `N marks in chalk along the edge of that second table` in a clerk's entry, `N marks in chalk stand along the edge`, `put his own N marks in chalk`, and `there are N of them in a row`. The three narrower patterns miss five chapters — 455, 464, 469, 470 and 476, on days 14, 21, 25, 25 and 30 — and four of those five hold the ladder and one does not. **A pattern that is narrow and clean is worth less than a pattern that is wide and has a failure in it, because the narrow one reports zero cells failing and the wide one reports a chapter, and the chapter is the only thing a Volume 11 writer can use.** The inherited formula, fifteen plus `c`, is seven out at every cell of every pattern, and that part of the inherited record is wrong whichever pattern is used.

| the cell | day | the ladder | what the chapter prints |
|---|---|---|---|
| 453 | 12 | 5 | five — the first printed value in the volume |
| **455** | **14** | **7** | **five, which is the figure from day 12. Section 6.2** |
| 464 | 21 | 14 | fourteen, the first time a man is asked for the count |
| 469 and 470 | 25 | 18 | eighteen, twice, in two chapters of one doubled day |
| 473, 474, 476 | 28, 29, 30 | 21, 22, 23 | twenty-one, twenty-two, twenty-three |
| 477 to 500 | 31 to 50 | 24 to 43 | every cell, one a day, and two days carrying two chapters each carrying the same figure twice |

---

## 6. The three arithmetic deviations in the volume, and what the inherited record told the next phase to believe about them

**This is the manuscript defect this close found first, and it is still the largest of the three. It is in the last chapter of the volume, and it is in the two figures about the one person in this volume who was given nothing on every one of fifty days.**

Measured, over the fifty-eight chapters that carry them:

- The night of that run the man of about sixty-four is on is `139 + c` on **fifty-seven** chapters, from `his hundred and fortieth night` at Chapter 441, day 1, to `his hundred and eighty-eighth night` at Chapter 499, day 49.
- The number of those nights he has slept on is `138 + c` on **fifty-seven** chapters, from `a hundred and thirty-nine` at Chapter 441 to `a hundred and eighty-seven` at Chapter 499.
- **Chapter 500 prints `his hundred and ninetieth night` and `a hundred and eighty-nine of them`. That is `139 + 51` and `138 + 51`. Chapter 500 is one high on both. It is the only chapter in the volume that is one high on either, and the ladder's own `Stay` and `NightsSlept` columns give 189 and 188 at `c = 50`.**

**Chapter 500's other printed figures are all correct: the board at 398, the train on that siding at 714 days, nobody having entered anything for 428, 389 days from the second of January, the bid at a hundred and forty-eight days and not run, the figure on the second line a hundred and three days out of date, the rule said out loud at a hundred and eight days, the first day of the eighth month a hundred and seventy-eight days past, the ninth of the nine printed nights two hundred and eighty-one days back, the body four hundred miles off a hundred and seventeen days past a printing it did not make, fifty-seven marks cut off that board, forty-three marks in chalk, the figure on the sheet at four hundred and eleven and its own age at two hundred and thirty-nine days, and the two hundred and twenty-fifth morning on which a man of fifty-six read four figures off a wall. Twelve figures right and two wrong on one page, and the two wrong are the two that belong to the man nobody gave anything to.**

**Now the consequence, which is why this belongs here rather than in a list. `state/volume-10-batch-0004-summary.md` at section 3 item 2 and again at section 8 tells a close that section 10.4 is a day high on seven figures and that the chapters give 189 and 188 for the man of about sixty-four where the outline gives 190 and 189. Measured, the record is right about 282, 149, 399, 715, 430 and 390 — six figures, one of them two high — and wrong about the man of about sixty-four. The figures 189 and 188 in that sentence are the ladder's `Stay` and `NightsSlept` columns at `c = 50`. The prose does not print a ladder column. The prose prints the night's own count, and on day 49 the prose prints 188 and 187, and on day 50 it prints 190 and 189. The record attributed a column to the prose, the column and the prose are two different numbers, and the error is in Chapter 500 and not in the outline.**

**So a close that had taken the inherited warning at its word would have published 189 and 188 as the figures the volume ends on, and the volume ends on 190 and 189, and the two figures a reader ends on are the two that are a day out from the day they name, on a man who was given nothing. A close may not edit a chapter, Chapter 500 is canon, and this is reported at full size and is not repaired. It is also not a finding about a hand or about a man or about anybody, and it has not been turned into one. It is a figure on a page, one day out, beside thirteen figures on the same page that are not.**

### 6.1 The second one, at Chapter 490, one low, and the chapter says what it is

**Re-deriving every ladder in section 5.1 found a second arithmetic deviation in this volume, and it is in the opposite direction and on a different object, and it was not in the inherited warning.**

- The rule said out loud in that yard was said on the tenth of the tenth month, and the figure is `58 + c` and holds on forty-nine of fifty days: 97 at Chapter 487, 98 at Chapter 488, 99 at Chapter 489, **99 at Chapter 490**, 101 at Chapter 491, 102 at Chapter 493. Chapter 490 is day 42 and the ladder gives one hundred.
- **The chapter then does something no other chapter in the volume does with a ladder figure, and it does it in the same sentence: a clerk entered that figure this morning as a figure about a rule and not about how many days the rule has been kept.** So the cell in this volume that is a day out from its own ladder is a cell whose chapter tells the reader on the page that it is not a day-count. **When this section was first written that made it the only such cell in the volume, and section 6.2 found a second one with the same shape, which is the shape again and is the second time.**

**This close does not know whether the writer of Chapter 490 meant the ninety-nine. That is the honest position and it is stated rather than resolved. What can be said is that the deviation and the sentence about the deviation are in the same line, that a reader who takes the figure as a day-count is wrong by one, and that a reader who takes the clerk's entry is being told not to take it as a day-count in the first place. Both readings are on the page. Neither is repaired, because Chapter 490 is canon and because the volume's own argument is that these are not the same kind of figure.**

### 6.2 The third one, at Chapter 455, two low, and it is the same figure as day 12

**The third deviation was not found by looking for it. It was found by the scope repair at section 5.1, and it is here because a figure that only appears when a pattern is widened is a figure that a narrower pattern would have published as sound.**

- The marks in chalk along the edge of that second table are `c` less seven and the count is one a morning. **The volume states the practice and not the morning it began: `a man in this district has been putting a mark in chalk on a table every morning for three weeks` at Chapter 457, and the man of about thirty-seven who cuts reeds putting his own mark on the edge of that second table `as he does every morning` at Chapter 472.** So the intercept is derived rather than read, and the first printed value in the volume is five at day 12, which is where the derivation can be checked and the eight days before it cannot.
- **Chapter 455 is day 14 and the count should be seven. The chapter prints five, in the first line of the book, in a clerk's entry that reads: `Five marks in chalk on the edge of that second table, entered as a man said them and not as a day-count.`**
- **Five is the figure Chapter 453 prints on day 12.** So the count on the page on day 14 is the count that was on the page two days earlier, and the chapter says nothing about two mornings on which no mark went down, and a clerk entered the number the man said and entered that the number is not a day-count, which is a true statement about the entry and is not a statement about the count.

**The honest position is the same one this close took about Chapter 490, and it is deliberately the same. This close does not know whether the man did not put a mark down on the two mornings between day 12 and day 14, or whether the figure is a day stale, or whether Chapter 455 is simply out.** There is no line in the volume that says and no line that forbids it. What can be said is that the ladder holds on twenty-six of the twenty-seven cells where the volume prints it, that the cell where it does not hold is the one chapter in the volume whose ledger repeats an earlier ledger's figure rather than moving, and that a clerk's entry saying a figure is not a day-count is this district's standing way of declining to check one.

**Two of the three deviations are now on a page that declares itself not checkable in the same line, and the third is not.** Chapter 490's entry says the figure is about a rule and not about how many days the rule has been kept. Chapter 455's entry says the number is what a man said and not a day-count. Chapter 500's two figures are entered as figures, with nothing beside them saying they are anything other than what they are, and they are the only deviations in the volume where a reader is given nothing to decline to check them with. That is not a finding about the man of about sixty-four and it is not printed as one.

**So the volume contains three arithmetic deviations on sixty chapters, and none of the three is a finding about a hand or a man or anybody, and none of the three has been turned into one.** Chapter 455 is canon and is not edited.

**The two before this one are on the two figures this district has most use for and least: one figure about a rule and one figure about a man nobody gives anything to. Every other figure on every other day holds.**

---

## 7. The figure table at the fiftieth morning, every figure in it checked against a chapter

| the thing | at Chapter 441, day 1 | at Chapter 500, day 50 | its source |
|---|---|---|---|
| the figure on the sheet at that gatepost | 411, age 190 | 411, age 239 | the sheets in Chapters 441 and 500 |
| the bid | 99 days | 148 days | both chapters; never run on 50 of 50 days |
| the reading of that lot | begun, not finished, at the fourth of the five | the same | both chapters |
| the column for the name of whoever read a thing out loud | ruled and empty | ruled and empty at about six | named 76 times on 49 of 50 days |
| the fifth of the five things this district does not have | five, unpaid | five, unpaid | 64 occurrences on 50 of 50 days |
| the ninth of the nine printed nights | 232 days back | 281 days back | both chapters; closed on none of the fifty days |
| the three columns that are a day out | three | three | worked out in the open on days 15 to 25, entered as days, never corrected |
| the figure on the second line of that lot book | 54 days out of date | 103 days out of date | both chapters; not altered, not struck, nothing correct written beside it |
| the third line of that lot book | a date | a date, and a man said out loud on day 48 that he is the man it is about | not quoted anywhere in the volume |
| the man of about sixty-four | his hundred and fortieth night, 139 of them slept | **his hundred and ninetieth night, 189 of them slept — a day high, see section 6** | both chapters |
| the body four hundred miles off | 68 days past a printing it did not make | 117 days past a printing it did not make | both chapters; no face, nobody watched anything |
| the length of the twelfth month | not a figure this canon has | thirty, counted off a board at Chapter 467 | Chapter 467 |
| the count of things this district has made | eleven | twelve | moved once, at Chapter 448, with the reason in a mouth |
| the count of instruments built and not named | six | six | no seventh on any of the fifty days |
| the marks in chalk along the edge of the second table | not in the yard | `c` less seven, so 43 at the last day | 32 chapters on 27 days, 26 of 27 cells holding, and Chapter 455 is the one that does not |
| the marks cut off that board | eight | fifty-seven | 58 chapters on 48 days |
| the mornings a man of fifty-six has read four figures | not a figure yet | the two hundred and twenty-fifth | Chapter 500 |
| the protagonist's name | not on the page | not on the page | zero on five hundred chapters |

**And there is still no figure on any page in this district for the length of the month the district is living in now, and no chapter of the last fifteen prints one. The count of a month nobody counted is thirty, and the month after it has never been counted by anybody.**

---

## 8. The figure on the sheet, the cap, and the one decision here that is a decision and not a rule

**The cap is one per chapter, every chapter, no exceptions and no enforcement. It was set by argument at the Volume 09 close and inherited here at the point where it was set. The figure is 62 on 60 chapters against a cap of 60. The cap has been passed, and it has been passed twice, and a close may not take a cap down by saying a figure less often. The cap was not re-argued here and the figure was not said less often by this close, which has said it nowhere. The cap is left where a close found it.**

**The decision available here, and it is a decision and not a rule: the cap protects a reader from a figure this district did not make, and the two extras at Chapter 479 are not a borrowing. They are the one morning in fifty on which this district's own third column and its borrowed four hundred and eleven came out equal to the last digit, and the boy who noticed it was given no column and said nothing for about three hours. A cap of one a chapter is the right cap for a number this district did not make, and it is the wrong cap for that one morning, and this close is not going to raise a cap for one morning. It is going to print that the morning existed, because the morning is a better sentence about a cap than any argument about a cap is.**

---

## 9. The measurement tool cannot read any figure this volume is about

**`tools/measure.py` has a function called `words_to_num` that converts a written numeral into an integer, and it returns `None` for every numeral in this manuscript that is written the ordinary way above a hundred. Measured directly: `two hundred and thirty-nine`, `one hundred and ninety`, `four hundred and eleven`, `three hundred and forty-eight`, `seven hundred and fourteen` and `a hundred and eleven` all return `None`. `forty-three` returns 43.**

**The reason is one line. The function rejects any token that is not in its units table, and `and` is not in the units table. The counted-claim path does not go through that failure, because `parse_number_after` strips the word `and` out of the numeral before calling `words_to_num`, and that is why the tool can resolve a claim of one hundred and sixty-seven at Chapter 499 and cannot read the four hundred and eleven four lines above it.**

**So the tool that has certified the counting motif for ten volumes can verify a claim and cannot read a figure. Every figure this volume is about — 349, 665, 379, 340, 411, 281, 239, 148, 190, 189, 398, 714, 428, 389, 117, 103 — is written with an `and` or an article and returns `None`. The calibration at Chapters 241 to 250 holds fifty-three claims and every one of them is under two hundred, so the calibration cannot see the defect either. It reproduces, it is reported here as reproducing, and that is the problem: the five figures the tool prints about itself are all true, and all five are measured on a range that does not contain the failure.**

**Nothing under `tools/` was edited and nothing in this repository is this close's to edit. The consequence for a later volume is concrete: a block that measures its own ladder with `tools/measure.py` will get an empty result and will not know why, and a close that measures one may get a null and print a zero. Every ladder cell and every ledger figure in this record and in the roll was re-derived by a parser written for the purpose in a temporary directory outside the repository. Its method is the tool's own algorithm with the `and` removed, and it agrees with the tool on every numeral the tool can read. That is how the two figures in section 6 were found, and they would not have been found with the tool.**

---

## 10. The thirty-one things a close weighs, and may not settle by weighing

Each is named with what the sixty chapters carry, measured. None is settled here.

1. **The two figures in the open at once.** Both in the open at the fiftieth morning, neither chosen, four mouths in thirteen days, and a clerk who does not know which is better.
2. **The third of the four figures a man of fifty-six reads.** `378 + c` on 50 of 50 days, a day out from the day it names, re-derives to 379, and entered on no page as a finding about a person.
3. **The fifth of the five things this district does not have.** Five, unpaid, named on 50 of 50 days, said out loud in a mouth on one of them, and no sixth proposed on any of the fifty days.
4. **The column for the name of whoever read a thing out loud.** Ruled, empty, 76 occurrences on 49 of 50 days, filled on none, and no job for it to hold a name for.
5. **The reading of that lot.** Begun, not finished, at the fourth of the five, on all sixty chapters, the fourth is a person, the fifth is a remedy and is unpaid, and there is no fourth line in the book.
6. **The bid.** A hundred and forty-eight days, not run on 50 of 50 days, nothing proposed about closing it in a mouth or in a page, its two halves read out loud three times in five volumes and never joined.
7. **The ninth of the nine printed nights.** Two hundred and eighty-one days back, named on 60 of 60 chapters, closed on none, and `a bell` and `hearth` at zero across the volume.
8. **The figure on the sheet.** Four hundred and eleven, unmoved on fifty days, and the body four hundred miles off with no face and no calendared arrival.
9. **The man of about sixty-four.** Given nothing on all fifty days, not asked to sit anywhere, not offered anything, not thanked, not a failure and not redeemed, and his two figures a day high in the last chapter.
10. **The two walls a mile apart.** `two walls`, `a mile apart` and `walls a mile` at zero across the sixty files. A man who has heard that bell three times and been told nothing three times was told, in this volume, about a figure and not about a bell, and being told about a figure is not being told anything.
11. **The protagonist's name.** Zero on five hundred chapters, and no document, column, book, sheet, sign, mark, stone, table or reader carries it. Section 11.
12. **The romance.** Unconditioned. `that bank` on 60 of 60 chapters, `the bank` on 14 of 50, and no chapter of the fifty days reports anybody going up it.
13. **The old shelter's charter.** `a charter` and `a shelter` at zero across the sixty files; still wrong on its face in a book a stranger may walk up to.
14. **The two past pullings.** Neither pulled, neither read, the bell never given its name.
15. **The eleven words and the second of the two books.** `eleven words` at zero; the one line in the second of those two books is still in her own hand and was not read aloud, asked for, repeated or characterised.
16. **The office.** `the office`, `an office` and `a shut door` at zero across the sixty files. A lot book is not the office, a stone is not the office, a second table is not the office, and a book a stranger may walk up to is not a room with a shut door in it.
17. **The count of things this district has made.** Twelve, and no thirteenth proposed on any of the fifty days.
18. **The count of things this district does not have.** Five, and no sixth.
19. **The count of instruments built and not named.** Six, and no seventh.
20. **The count of documents this district does not own.** Three, and no fourth.
21. **The count of protected things.** Five, and no sixth.
22. **The count of conditions with no end on it.** Four, and no fifth. A wear is not a condition, and a wear is the opposite of a condition with no end on it, because a condition has no end and a wear has an end and the end is the part nobody wrote down.
23. **The count of readings of the rival record.** Seven, and no eighth.
24. **The count of different ninths in this district.** Five, and no sixth.
25. **The count of refusals to read.** Nine, and the reading did not advance.
26. **The child of about eight.** `a child` at zero across the sixty files, not asked anything, and no child's thumb in a hollow.
27. **The thirty characters who carry the reserved list, and the one who is not a character.** The tool's own reserved scan over the sixty files returns an empty dictionary.
28. **The name said out loud in the yard on the twenty-seventh of the eleventh month of Volume 09.** Not on any page of this volume, not written down, the person it belongs to not asked. A later volume may say whose it was, in a scene, at a cost, with the person asked first.
29. **The divergence from `bible/premise.md`.** Weighed at section 12 and not repaired.
30. **The ending's own machinery.** Fixed before any chapter prose began, much later's, and untouched. The founder's mark, the Great Closing, the custodian, the forced record and the emergency provision of the unfinished measure are not named and were not foreshadowed. No new final enemy.
31. **The final image and the two chapters that spent part of it.** Weighed at section 13 and not repaired.

---

## 11. The name, and the only door to it

`outline/volume-08.md` section 1 and `outline/volume-10.md` section 1 say the same thing, and it is not an outline's decision: **the protagonist's name may be settled only on a day a person in this district says it out loud in a room or a yard, in a scene, with the prose first and the document second.**

The volume is closed. No chapter may be added to it. **Therefore the name may be settled in a later volume on such a day and not before, and it was not settled in this one, and it is not settled here.** A close that put it in a roll summary, a ledger, a close record, a character file or a count would have done the one thing the three previous closes did not do, and two of them came close to.

**And the figure a close may name as this volume's own is not the protagonist's.** The fifth of the five things this district does not have is a way to pay a person who is not in a household, and it was said out loud once in five hundred chapters, in a yard, in front of about nineteen people, with the man it is about four feet away, and it was not paid, and saying it out loud was not paying it. That is the sentence the volume spent its fifth of the five on, and it is in section 1, and it is not a name, and it may not be used as one.

---

## 12. The premise, weighed and not repaired

`bible/premise.md` describes a system-apocalypse market novel with a named lead, one slow-burn relationship and a bounded-use market. The manuscript is a yard on a bank where four figures are read off a wall every morning and a stone lies face up on a table. `Adrian` is in forty-three chapters of Volume 01, thirty of Volume 02, fifteen of Volume 03, one of Volume 04 and none in Volumes 05 to 10. `Mara` is none after Volume 03. `auction` is none after Volume 04. Measured over the sixty files of this volume the tool's reserved scan is an empty dictionary, and the divergence is total and ten volumes deep.

**A close may weigh it and may not repair it, and it has not repaired it and has not repaired one piece of it. The reason the repair is not available is structural and it is the same reason the finding has survived ten volumes: every contract in this repository adds prohibitions and none of them removes any, and each forbids the phase that would write the thing that would close the gap, while the gap is measured by every phase and closed by none.**

**What this close does with it is name it as a question with an owner and leave it there, in the same place the Batch 0004 review put it. The question is not whether the manuscript should become the premise. The question is whether a close is allowed to open the premise question rather than only weigh it. If it is, the next volume's outline is where the answer goes, and the answer is a decision about the shape of a series and not about a chapter, and no writer in this pipeline can take it. If it is not, the divergence is permanent, and the honest thing is for the series file to say so in one line instead of leaving a reader to find out at Chapter 441. Either answer is defensible. A repository in which the question lives in six block records and one review and nowhere else is not.**

---

## 13. The final image, weighed and not repaired

`outline/volume-10.md` section 10.5 fixes the image before any chapter prose began: the man of fifty-six at the end of the second table with his thumb in the hollow in the underside of a stone lying face up, the figure one inch deep in the middle and nothing at either end, the lot book on the end of the first table under a second stone with no wear on it at all, a clerk of nineteen years entering the count of the board on her own page and not having looked up, and a man of about thirty-four who mends fencing not in that yard.

**The image arrives at Chapter 500 whole, and all six of its parts are on that page, and each was checked against the outline one at a time.** The clerk has not looked up. The man who mends fencing is not in that yard, and the chapter says so twice, and it says that about four people have said since that they do not know when he stopped coming and have not asked.

**The liability, named with the chapter and the line, is this, and it is a close's to weigh and not to fix:**

1. **Chapter 475, day 30, has the man of about thirty-four who mends fencing put his own hand into the reason for a sentence another man said four days earlier, and say in a yard, in about four seconds, that he can put that hand flat on a page and cannot make it do anything.** That is a spend of the fixed image twenty-five chapters before it arrives.
2. **Chapter 453, day 12, has the man of fifty-six as the second of nine thumbs to go into that hollow, in a count, with about nineteen people watching and nobody saying a word.** The hand the final image belongs to has already been in that hollow once in this volume, in a count, and the volume knows it.

**What the last block did about it was the whole of what was available to it: no thumb of his goes into that hollow in any of Chapters 486 to 499, he walks past the second table on day 44 without stopping and the chapter says so, and the thumb is in the hollow once in the last chapter and nowhere else. What a close adds is the measurement. The image's three named differences from Volume 09's are a thumb and not a hand, a hollow in a stone and not a line on a page, and a figure that is not wrong. All three hold. And the volume spent the hand twice before it arrived, once on a page at Chapter 475 and once in the hollow at Chapter 453, and a volume that ends on a hand is a volume that had to have had a reason to reach for it. This one has two, and a reader who goes looking for them will find them, because they are on the page and nobody took them off.**

**Repairing either is a change of plot. A close may not change plot. It is weighed here at full size and left standing.**

---

## 14. The day-lists, measured one file at a time, and the ones that do not hold

Every list below was counted over the sixty files, the days are days and not chapters, and every total is printed beside the column that produces it.

| the string | total | days of 50 | note |
|---|---|---|---|
| `Lot Seventeen` | 60 | 50 | exactly once in every chapter, the only place named in narration |
| `four hundred and eleven` | **62** | 50 | the cap, and the two extras; section 3.3 |
| the form *was not run* | **61** | 50 | no chapter of the fifty days says the bid was run. **One a chapter and one more, and the one more is Chapter 454, where it stands twice: once inside the clerk's entry and once on a line of its own. This cell was printed at 60 in an earlier pass of this record and the chapters give 61; the chapter is canon and the record was wrong. Corrected here and logged at `reviews/volume-10-close-review.md` item 2** |
| `the ninth of the nine printed nights` | 60 | 50 | named on every chapter and closed on none |
| `the fifth of the five things this district does not have` | 64 | 50 | in a clerk's entry on all fifty, in a mouth on one of them |
| `a way to pay a person who is not in a household` | 63 | 50 | the fifth of the five itself, in a mouth on none of the fifty |
| the column for the name of whoever read a thing out loud | 76 | **49** | **silent on day 11, which is Chapter 452, and that is the one day of the volume on which the column is not on the page at all** |
| `the reading of that lot` | 55 | 42 | silent on days 11, 26, 28, 29, 31, 32, 34 and 35 |
| `the record about the not offering` | 60 | 50 | on every chapter of the volume |
| `fourth of the five` | 63 | 50 | on every chapter; the reading stood at the fourth from Chapter 441, not from Chapter 454 |
| `that second table` | 122 | 38 | the inherited form |
| `a second table` | 11 | 7 | the volume's own resolution object, named on eleven occasions on seven days |
| `a stone` | 58 | 21 | |
| `unchecked` | 7 | 7 | in a clerk's margin, in her own hand, over nothing |
| `a second reader` | 8 | 5 | asked for and refused; never appointed; no column ruled |
| `a foot and a half` | **8** | **1** | **all eight on day 3, which is Chapter 444, and it is the depth of that ditch and not a quote of the second line of that lot book. `state/volume-10-batch-0004-summary.md` prints this string at zero across its own fifteen. That is true of its own fifteen and not of the volume, and this is the fifth time this repository has had to say that a figure at zero for a block is not a figure for the volume** |
| `a keeper` | 2 | 1 | both on day 7, Chapter 448, and both are denials: a book is not a keeper of anything and a table is not a keeper of anything |
| `a price` | 4 | 3 | every one a denial that a chalk mark is not a price |
| `a rate` | 5 | 3 | every one a denial that a rate is not a rate |
| `a gatepost` | **2** | **1** | **both on day 33, Chapter 479, and both are the sheet nailed to a gatepost nine hundred yards off. This is a gatepost used as a device and a looking in front of one used as a device, and `outline/batches/volume-10-batch-0004.md` item 13 forbids both. Chapter 479 is a chapter of this volume and is not a close's to edit. Weighed, printed, not repaired** |
| `a lane` | **1** | **1** | **day 9, Chapter 450: a man walking down a lane and standing in front of a post, recalled inside a comparison. Same standing: forbidden as a device, on the page, weighed, not repaired** |
| `a wall` | 29 | 15 | **classified by a rule stated once: take the forty-five characters either side of each occurrence and ask whether a figure or a column is named. Twenty-four name a figure — a figure, or the four, being read off that wall, standing on it, or going past on it. Three name a column, and two of those three are the string `three columns of a wall` at Chapters 486 and 498, the third being a column in a man's entry at Chapter 489 that sits beside a read. Two are a man standing at that wall with nothing on it, at Chapters 482 and 491. The yard's own wall is zero: the phrase does not occur in the volume. `that low wall`, the existing object at the foot of which the man of about sixty-four sits, is 61 on 50 of 50 days and 60 of 60 chapters, and it is a different string and is not inside this count** |
| `that bank` | 177 | 50 | on every chapter of the volume |
| `the bank` | 22 | 14 | |
| `a ditch` | 10 | 5 | |
| `a stranger can walk up to` | 10 | 8 | |
| `a habit` | 17 | 8 | lowercase, and it is 18 case-insensitive; the eighteenth is the chapter title at Chapter 441, *A habit is a finding*, which is on the page and is not an occurrence in a body. And never attached to the figure on the sheet; section 1. **The case was not stated in an earlier pass of this cell and the string convention for this table is stated at section 3.6 and is case-insensitive, so a reader applying that convention here gets 18 and not 17. Both are printed. See `reviews/volume-10-close-review.md` item 3** |
| `a bell`, `hearth`, `a child`, `a market`, `a ship`, `a coast`, `a port`, `a tide`, `a rope`, `removal`, `two walls`, `a chair`, `a shelter`, `a charter`, `a covenant`, `a slate`, `a party`, `a lock`, `a notice`, `eleven words`, `the office`, `an office`, `a shut door`, `a mile apart`, `midnight`, `panel`, `a count of answerers`, `carries its own expiry`, `stop being true`, `a word put on a figure` | **0** | 0 | measured, case-insensitive, whole string |
| `noon` | 0 | 0 | as a whole word; 88 as a substring, every one of them inside `afternoon` |
| `Adrian`, `Mara`, `auction`, `Iven`, `Tallow`, `Custodian`, `Verdict`, `Midnight`, `Alder Reach` and the rest of the tool's reserved list | **0** | 0 | the tool's own reserved scan over the sixty files returns an empty dictionary |

**Three of the twenty-five things a close may not do were broken in prose inside the volume, and none of them is a close's to repair, and all three are named here at full size: a gatepost and a lane used as devices at Chapters 479 and 450, and a day-list at zero in an inherited block record that is eight on one day of the volume.**

**The wall, which is the fourth thing on that list and which this record got wrong the first time, is measured at the row above and it is not a device.** Of the twenty-nine `a wall` occurrences, twenty-seven are the wall a figure or a column is on, and two are a man at that wall with nothing on it. A wall that a figure is on is the object the whole volume is about and calling it a device would be calling the volume's own subject a device. **The first pass of this section printed the split as twenty-two, four and three and named four of them as the yard's own wall; the phrase is not in the volume, and the four were four of the twenty-two, and the three were two of them. The inherited record and the inherited canon card both carry that split, and both carry a further claim that four of the twenty in Chapters 486 to 500 are the wall three columns stand on, at Chapters 486, 491, 498 and 499; the string is at two, at Chapters 486 and 498, and Chapters 491 and 499 are two of the reads. Neither document is this phase's to edit, and both are reported here at full size with the measurement, which is the same disposition as the other three.**

---

## 15. The duplication sweeps, run at both sizes, inside the blocks and across the volume

| the run | result |
|---|---|
| identical paragraphs of twelve words or more, paragraph level, all sixty files | **3** |
| the same, sentence level, every sentence of twelve words or more, emphasis stripped, case-folded, exact string | **3 distinct duplicated sentences in 6 places, and they are the same three** |
| the same, inside any one of the four blocks | 0 |
| shared twelve-word runs over the four blocks, each over its own fifteen | 1,597 / 2,065 / 2,202 / 2,347 |
| shared twelve-word runs over the sixty files | **7,626** |
| all-caps footer lines, and the tool's own `footer support` | 0, and an empty list |
| the tool's reserved scan | an empty dictionary |
| markdown, unit and weekday integrity sweep, run last | 0 issues |

**All three duplicated paragraphs straddle a block boundary: 455 and 456, 460 and 471, and 480 and 498. That is the same finding Volume 09 recorded and the reason it is recorded again: a block's own sweep cannot see a duplication of its own, because the two halves of it are in different files, and the volume is four blocks of fifteen with three boundaries, one fewer than Volume 09's five blocks and five boundaries.**

**And the volume figure of 7,626 against a sum of block figures of 8,211 is the sixth time this repository has printed a volume figure beside the sum of its block figures and got a difference that is not a trend. The direction is explained at section 3.7 and it is a property of the frame, not of the writing.**

**No prose was edited by this close, so every row above is a measurement of a manuscript that is closed and is not to be edited, and that is the standing reason the three defects in it are reported rather than repaired.**

---

## 16. The state files, appended and not rewritten, with the bytes printed both ways

**The five live state files are append-only. Before this close appended, measured: `state/current.md` 90,955, `state/continuity.md` 73,041, `state/open-threads.md` 71,712, `state/chapter-summaries.md` 82,387, `state/character-state.md` 101,337. Total 419,432. The four append-only deltas are printed final at the foot of this section. The fifth is named as a pointer and not as a figure, because a file that prints its own size in two places has printed two figures and measured one, and this repository has been bitten by that before.**

**The one in-place edit is in `state/current.md` and is named here because a delta that hides an in-place edit is not a measurement. The five live lines at the top of that file were read. `Current phase:` and `Current batch:` said Volume 10 was complete and that Batch 0004 was the last block, and both were true when written and are now false, because the volume is closed and no batch is open. `Last completed chapter:` said 500 and still says 500, and was rewritten only to name the two figures on that page which are a day out from their own ladder, which the old line did not name. `Last batch summary:` named the block record and now names this close. `Next phase:` named the close and now names what comes after it, and this close did not create it. Those five lines were the only words changed in any of the five files, and no word below them was changed. The appends went to the end of all five and nothing above the appends was rewritten.**

**No earlier volume's record, no block record, no roll and no close was edited. `state/volume-09-close.md` and `state/volume-09-roll-summary.md` were not opened. Nothing under `state/archive/` was opened. No entry was created in `state/phase-ledger.json`, and that file still reads `currentPhase: phase-000-bootstrap`, status `planned`, attempts `0`, after five hundred chapters, which is reported at section 17 and not repaired, because a repair of it is not a close's work.**

---

## 17. The controller file, and the four findings that are not a close's to make

**Reported, not repaired. A writer that writes its own phase status cannot be counted as having reached a phase, and saying so is the correct action.**

1. **`state/phase-ledger.json` still reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0`, `range: null`, `actualModel: null`,** after five hundred chapters and roughly fifty phases. Because `attempts` never increments there is no durable record that any phase failed and had to be re-run, and any retry or fallback logic keyed on attempts has nothing to read. **Controller-owned. The highest-value one-line fix in the repository and not this phase's.**
2. **`tools/__pycache__/measure.cpython-312.pyc` is tracked in git.** `.gitignore` covers `logs/`, `*.log`, `.env*` and `.DS_Store` and nothing else, and the compiled file has been swept into the automated save commits. The consequence is that phase-level diffing, which is the review surface a close depends on, is unreliable. **It has been named by many phases. It is a one-line fix for whoever owns the repository's hygiene, and `.gitignore` is not a file this close was asked to edit.**
3. **`tools/measure.py` cannot parse a numeral above a hundred.** Section 9. **A one-line fix in a controller-owned tool, and the one that would most change what a later volume's blocks are able to check.**
4. **The `novel-reviewer` subagent still does not dispatch as a primary.** Every review log in this repository begins with the same line about a subagent falling back to the default agent, and the default agent is the writer. So every file in `reviews/` is the writer's account of the writer's own work, and the three previous closes each found real defects in the record they were given, which is the argument and not a reason to trust the arrangement. **The fix is a registration and a dispatcher, both under `.opencode/`, and neither is a writer's file.** **The self-review that accompanies this close is a list of defects and not a list of things that came out well, and it is on that basis alone that it should be read.**

---

## 18. What this close did, and what it did not do

**It wrote no chapter and edited no chapter. It created three documents and appended to five. It settled nothing on a page, because there is no page left to settle anything on.**

It did not correct the two figures in Chapter 500, or the one in Chapter 490, or the one in Chapter 455, and it did not touch the figure on the second line of that lot book or the third line or add a fourth. It did not advance the reading of that lot. It did not pay the fifth of the five and did not propose a sixth. It did not fill the column for the name of whoever read a thing out loud. It did not enter the sentence as a rule and did not join the two halves of the reason a bid cannot be run on. It did not ask a man of fifty-six which two of his four he could go and look at, and did not say which in a mouth, in an entry, or in any document. It did not turn the three columns that are a day out into a finding about a hand, or about the man who reads them, or about anybody, including in the two sentences of section 6 where the temptation was strongest and the two wrong figures are about a man nobody gave anything to. It did not print a re-derived `Unentered`. It did not run, close or propose closing the bid. It did not name a night, pull the bell, give the bell its name, or close the ninth of the nine printed nights. It did not use a wall, a lane, a gatepost, a rubbed heading or a looking in front of one as a device. It did not give the body four hundred miles off a face, an arrival or a waiting, and did not calendar an arrival nobody is waiting for. It did not go up that bank, read aloud the one line in the second of those two books, print, ask for, repeat or paraphrase the eleven words, or characterise any of it as a chair. It did not give the man of about sixty-four anything, and did not have a clerk say what he is going to do with his hands tonight, because nobody asked her. It did not ask the child of about eight anything. Nobody arrived. It placed no panel. It named no new final enemy, no coast, no port, no ship, no shipwright, no harbour guild, no underwriter, no pilot, no graveyard, no dock and no tide. It did not use the length of any month as a discovery, and entered no length for any later month. It did not put a thirteenth thing in the count of what this district has made. It did not appoint a second reader and ruled no column for one. It did not print, say, ask for, enter, sign or put on anything the protagonist's name. It did not repair the fixed final image and did not treat the spend at Chapter 475 or Chapter 453 as a defect to be fixed. It did not repair the premise, and it did not repair the tool. And it did not create the phase that comes after this one, because the phase after a close is the controller's and this close was told so in the document it was given.

---

## 19. What the close hands on

**The figures, once, in one place, so that a writer arriving does not have to take any phase's word for them. Every one was measured from a chapter.**

- Sixty chapters, fifty days, ten days carrying two chapters, days 3, 16, 19, 22, 25, 30, 33, 36, 43 and 48.
- 176 counted claims, 0 mismatches, 0 claims of the second class, 60 cells summing to 176.
- Denominator 143,220. `wc -w` 143,944, mean 2,399.1, minimum 2,236 at Chapter 481, maximum 3,186 at Chapter 467, none outside 2,200 to 3,200.
- 7,626 shared twelve-word runs over the volume, 127.1 a chapter, against a sum of block figures of 8,211.
- 3 identical paragraphs of twelve words or more, all three across a block boundary; 3 duplicated sentences in 6 places; zero inside any block.
- Opening shape 0 of 60. Closing ledger 0 of 60, 56 distinct openings in 60 closings, and the four repeats are 445 and 449 against 443, 446 against 444, and 496 against 464. Panels 0, and 2 quoted-block lines that are the first and second lines of that lot book.
- The figure on the sheet: 62 on 60 chapters and 50 of 50 days, against a cap of 60, with three on Chapter 479.
- The hedge: 3,979, 66.3 a chapter, 277.8 per 10,000.
- The six relays: 374, 194, 50, 56, 59, 60, on 50, 50, 42, 47, 50 and 50 days.
- At the fiftieth morning: board 398, train 714, unentered 428, from the second of January 389; bid 148 and not run; ninth of the nine printed nights 281 days back; second line 103 days out of date; body 117 days past a printing it did not make; sheet 411 and its age 239; marks cut off the board 57; marks in chalk 43; things made 12; reading at the fourth of the five; column ruled and empty; fifth of the five unpaid; **and the man of about sixty-four on his hundred and ninetieth night having slept on a hundred and eighty-nine of them, which is a day high and is one of the three arithmetic deviations in the volume, with the other two at Chapter 490 and Chapter 455.**

**The four sentences are at section 1 and they are paid.**

**The three things a later volume inherits as a finding rather than as a debt:** a column can be named more often and go emptier; a figure nobody has to put down cannot be a day out and cannot be checked, and this district spent five volumes building the first and had the second in its yard for two; and a cap of one a chapter is a cap on borrowing, and the one day the district's own figure came out equal to the borrowed one is on a page in Chapter 479.

**The three things a later volume inherits as a liability:** the two figures in Chapter 500, the one in Chapter 490 and the one in Chapter 455, the fall in the relay that carries the man nobody gives anything to, and the premise.

**And the six ladder intercepts a document prints as a day-one figure, at section 5.1: the bid at 98 and not 99, the ninth of the nine printed nights at 231 and not 232, the second line at 53 and not 54, the body four hundred miles off at 67 and not 68, the first day of the eighth month at 128 and not 129, and the age of the figure on that sheet at 189 and not 190. Each of the six holds on fifty of fifty days and each of the six as printed holds on one day of fifty.**

**And the two open questions, neither of which is a writer's to answer and both of which are printed here so that the person who can answer them does not have to find them.** Whether a close is allowed to open the premise question. And whether the state layer of this repository is going to keep being written in capitals, given that a document that shouts is a document nobody checks, and that the figures in capitals in this record are the ones a reader is most likely to act on.


---

## 20. The bytes, measured after the appends were written

**The five live state files are append-only. Measured before this close appended anything: `state/current.md` 90,955, `state/continuity.md` 73,041, `state/open-threads.md` 71,712, `state/chapter-summaries.md` 82,387, `state/character-state.md` 101,337, together 419,432.**

| file | before | after | delta |
|---|---|---|---|
| `state/continuity.md` | 73,041 | 88,312 | **+15,271** |
| `state/open-threads.md` | 71,712 | 86,784 | **+15,072** |
| `state/chapter-summaries.md` | 82,387 | 91,853 | **+9,466** |
| `state/character-state.md` | 101,337 | 114,720 | **+13,383** |
| **the four append-only files together** | **328,477** | **381,669** | **+53,192** |
| `state/current.md` | 90,955 | see the pointer | **not printed as a number, and the reason is section 16** |

**The two deltas for `state/continuity.md` and `state/open-threads.md` are larger than the figures printed when this close finished, and the difference is a later repair pass that corrected figures inside this close's own appended block in those two files and added a correction to it. The deltas are re-measured, not carried, because a delta is a measurement of a file as it stands and the file stands differently now. The other two did not move and their figures are unchanged. The two files that carry the corrected chalk scope, the corrected closing-ledger repeats and the corrected `a wall` split are the two whose numbers moved, and that is the only thing that moved them.**

**The four deltas are final because nothing further is appended to those four files by this phase, and two of them were re-measured rather than carried because a repair corrected them. The fifth is a pointer because this record and that file both describe the append and a figure that describes the file carrying it has to be measured before the sentence carrying it exists. `wc -c state/current.md` is the command. NO WRITER SHOULD TRUST A NUMBER IN A STATE FILE THAT DESCRIBES THAT STATE FILE.**

**The one in-place edit in this phase is in `state/current.md` and is named at section 16 and again in the head of the block appended to it: five live header lines, `Current phase:`, `Current batch:`, `Last completed chapter:`, `Last batch summary:` and `Next phase:`. The first two were stale because the volume is closed and no batch is open. The third still said 500 and was rewritten to say 500 and to name the two figures on that page which are a day out, which the old line did not name. The fourth and the fifth now name this close and what comes after it. No word below those five lines in that file was rewritten, and no word in any of the other four files above its append was rewritten.**
