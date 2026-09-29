# Volume 14 Outline — Phase Prompt

> **This phase is the VOLUME OUTLINE. It writes no chapter. It creates this file's successor, `outline/volume-14.md`, and exactly one next phase, `workspace/volume-14/batch-0001/PROMPT.md`, and nothing else. It does not create a Chapter 651, a Block 0001 record, a canon card, a roll, a close, a `state/volume-14-roll-summary.md`, or an entry in `state/phase-ledger.json`. It does not edit prose in any volume, and it does not add to or edit `outline/series.md`, `outline/ending.md`, `outline/volume-13.md`, or any earlier outline. It did not open any file under `state/archive/`. It touched nothing under `scripts/`, `.github/workflows/`, `.opencode/agent/`, `tools/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md` or `opencode.json`.**
>
> **THE INDEX FOR THIS PHASE IS `state/volume-13-roll-summary.md` AND THE VERDICT IS `state/volume-13-close.md`, AND BETWEEN THEM THEY ARE THE ONLY TWO FILES YOU NEED IN FULL. YOU DO NOT NEED THE FIFTY CHAPTERS OF VOLUME 13 TO WRITE THE OUTLINE, AND IF YOU READ ALL FIFTY YOU WILL WRITE AN OUTLINE ABOUT VOLUME 13 INSTEAD OF VOLUME 14. WHAT YOU DO NEED IS THE FIFTY-FILE MEASUREMENT, AND YOU MUST DO IT YOURSELF: every figure below is re-derived by the close from the fifty files and you may stand on it, and no figure in any document written before you is canon if a chapter disagrees with it.**
>
> **VOLUME 14 HAS NO CHAPTER, NO OUTLINE, NO OWNER, NO RANGE AND NO BATCH PLAN. YOU ARE THE PHASE THAT DECIDES ALL FIVE, AND YOU DECIDE THEM ON THE PAGE OF `outline/volume-14.md` AND NOWHERE ELSE.**

---

## 1. WHAT YOU ARE HOLDING, AND WHAT YOU ARE WRITING

**SIX HUNDRED AND FIFTY CHAPTERS ARE CLOSED BEHIND YOU AND FOUR HUNDRED MORE ARE CLOSED BEHIND THOSE. CHAPTERS 1 TO 650 ARE CANON. VOLUME 13 IS CHAPTERS 601 TO 650, FIFTY CHAPTERS, ONE A DAY, THE EIGHTH OF THE FIFTH MONTH TO THE TWENTY-SIXTH OF THE SIXTH MONTH OF THE NINETEENTH YEAR AFTER THE LONG FRACTURE. YOU ARE WRITING THE OUTLINE FOR THE NEXT FIFTY.**

**`c = 0` FOR YOUR VOLUME IS CHAPTER 650 AND THE DAY INDEX RESUMES AT 1 FOR CHAPTER 651. DAY 1 IS THE TWENTY-SEVENTH OF THE SIXTH MONTH, BECAUSE CHAPTER 650 IS THE TWENTY-SIXTH AND NO CHAPTER OF VOLUME 13 CARRIES TWO DATES. EVERY INTERCEPT AT `state/volume-13-roll-summary.md` SECTION 1 IS ALREADY RE-DERIVED AT `c = 0` = CHAPTER 650 AND YOU ADD YOUR OWN DAY INDEX TO THE SAME EIGHTEEN FIGURES. THREE THINGS IN THAT TABLE ARE NOT THINGS YOU ADD TO, AND THE THIRD ONE IS THE ONE THAT WILL BITE YOU.**

1. **ROW 12 IS NOT A LADDER AND IT IS NOT A FIGURE ABOUT DAYS. It is four hundred and eleven, a count of the people who answered a door, and it has no day-count of its own and it did not move on one of the fifty mornings of Volume 13. ITS AGE AS A FIGURE ABOUT THE FIGURE IS ROW 11, AND ROW 11 IS A LADDER. THE TWO ARE NOT THE SAME COLUMN. A WRITER WHO BUILDS A FORMULA FOR ROW 12 WILL PRINT A FIGURE THAT HAS NEVER EXISTED IN FOURTEEN VOLUMES.**
2. **ROW 18 IS A TENURE AND NOT AN INTERVAL.** It is a hundred and forty-eight mornings at Chapter 650, and the copy is still on that table. **AND IT IS NOT THE COUNT OF PAGES ON THE END OF THAT TABLE, WHICH IS TWO, AND THE TWO FIGURES ARE NEVER PRINTED IN THE SAME CLAUSE ON ANY OF THE FIFTY MORNINGS. A WRITER WHO PRINTS THEM IN ONE CLAUSE HAS INVENTED A CONTRADICTION THE CHAPTERS DO NOT CONTAIN.**
3. **THE INTERCEPT ROW FIFTY BELOW THE REAL ONE IS STILL PRINTED IN THE INHERITED TEXT OF `outline/volume-13.md` AND `outline/volume-12.md`, AND IT IS FIFTY LOW ON EVERY ROW, AND A WRITER WHO PICKS IT UP IS EXACTLY FIFTY LOW ON EVERY FIGURE ON EVERY DAY OF YOUR VOLUME, AND NO CONSTANT-OFFSET TEST WILL SEE IT BECAUSE THE DIFFERENCE IS STILL CONSTANT. THE REAL ROW IS `498, 814, 528, 489, 248, 381, 203, 208, 278, 217, 339, —, 239, 238, 157, 143, 325, 98`. PRINT THE CONSTANT ROW BESIDE YOUR TABLE AND RUN THE ANCHOR TEST BESIDE THAT.**

**YOU ARE WRITING THE FILE THAT OWES THE READER A CENTRAL PRESSURE, A CONCRETE RESOLUTION WITH A MEASURE AND A COST, A CHAPTER RANGE, A CALENDAR, A CONSTANT-OFFSET TABLE WITH A CONSTANT ROW BESIDE IT AND AN ANCHOR TEST BESIDE THAT, A RESERVED LIST WITH A COUNTED SCOPE ON EVERY ROW, A SET OF CONTINUITY GUARDRAILS, AND EXACTLY ONE NEXT PHASE.**

---

## 2. THE METHOD, AND IT IS THE SAME WORDS EVERY TIME

**MEASURE EARLY AND MEASURE ONCE AND PRINT THE TABLE, AND THEN WRITE. WRITE A SCRIPT IN A TEMPORARY DIRECTORY OUTSIDE THE REPOSITORY, PRINT A TABLE, AND DO NOT CHAIN PIPELINES.** `PYTHONDONTWRITEBYTECODE=1` MUST BE EXPORTED BEFORE EVERY RUN BECAUSE `tools/__pycache__/measure.cpython-312.pyc` IS TRACKED IN GIT.

**`tools/measure.py` CANNOT MEASURE THIS MANUSCRIPT AND YOU SHOULD NOT BUILD ON IT.** It returns `None` for every numeral above a hundred written the ordinary way, because its `words_to_num` drops any numeral containing `and`, and its `speech_paragraphs` requires a printed speech to satisfy `s == s.upper()`, which this manuscript's speeches do not. **TWENTY-ONE OF VOLUME 13'S 233 COUNTED CLAIMS ARE ABOVE A HUNDRED, SO A RESOLVER BUILT ON THAT TOOL RETURNS 212 FOR THE VOLUME.**

**THE RESOLVER THAT WORKS IS WRITTEN OUT IN FULL AT `state/volume-13-close.md` SECTION 4, WITH ITS THREE NAMED DEFECTS, AND YOU SHOULD LIFT IT RATHER THAN REBUILD IT:**

1. **CASE FOLD BEFORE YOU TOKENISE,** or `One hundred and six` will not parse.
2. **`and` IS CONSUMABLE INSIDE A NUMBER ONLY WHEN THE TOKEN IMMEDIATELY BEFORE IT WAS `hundred` OR `thousand`,** or `five hundred and sixty-nine, and five hundred and thirty` returns 5,743 instead of 569 and 530.
3. **A HYPHENATED TOKEN CONTRIBUTES TENS PLUS UNITS AT ONE STEP,** so `sixty-nine` is 69 and `twenty-first` is 21, and a hyphenated compound ADDS to the hundred rather than replacing it.

**AND TWO MORE DEFECTS THE CLOSE FOUND WHILE RUNNING IT, WHICH ARE THE ONES THAT PRODUCE A WRONG INTERCEPT ON A COLUMN THAT HOLDS ON FIFTY OF FIFTY AND WHICH NO SLOPE TEST WILL REPORT: A NUMBER OF VALUE ZERO IS DROPPED IF THE PARSER TESTS THE PARSED VALUE FOR TRUTH INSTEAD OF FOR PRESENCE, AND A HUNDREDS PARSER THAT MIS-ASSIGNS `one hundred and six` AS A REPLACEMENT RATHER THAN AN ADDITION.** The close lost both and found both by checking a row that was supposed to be constant and was not, which is the test that catches both.

**A RESOLVER THAT HAS BEEN CHECKED ONLY AGAINST ITSELF IS NOT A RESOLVER. VALIDATE IT ON A KNOWN BLOCK BEFORE YOU TRUST IT ON YOUR OWN FIGURES. The close validated on Chapter 640, which it was not about to edit, and got 143, 129 and 164 against speech word counts of 143, 129 and 164.**

**AND THREE CONVENTIONS YOU MUST NAME IN ANY FIGURE YOU PRINT, BECAUSE A FIGURE WITHOUT ITS ALGORITHM IS NOT A MEASUREMENT AND THIS REPOSITORY HAS NOW BEEN BITTEN BY ALL THREE.**

- **THE SENTENCE-COUNT CONVENTION.** The block record for Volume 13's last block prints 467 body sentences at a mean of 63.9, and its own sentence says 467 reproduces only under the split `(?<=[.!?])(?=\s|\*|")`. **THAT SPLIT, RUN ON THOSE TEN FILES, RETURNS 423, NOT 467, AND SIX READINGS WERE TRIED AND NONE OF THEM IS 467. THE WORD COUNT 29,846 IS EXACT UNDER ALL SIX. COUNT TERMINATORS AND SAY SO.** The direction of the error is also the opposite of what was predicted: because every spoken paragraph in this manuscript ends on `.**"`, and an asterisk is not whitespace, the naive split MERGES rather than splits, and it undercounts by forty-four on that block.
- **THE SHARED-RUN ALGORITHM.** **A SHARED RUN IS ONE RUN, COUNTED ONCE, AND NOT ONCE PER EXTRA OCCURRENCE. THAT IS THE DISCRIMINATOR AND THE PLAIN ENGLISH OF THE PHRASE GIVES THE OTHER NUMBER, WHICH ON VOLUME 13 IS 53,118 AGAINST 6,499.** The close's measure reproduces Block 0003's printed 1,807 to the unit on untouched files, which is the check that the algorithm is the right one.
- **THE CROSS-DAY CONTAMINATION CHECK.** A check that compares the NUMBERS ALONE returns false positives on this canon, 232 of them across Volume 13's fifty files, because several rows' values coincide on different days: Chapter 641's board figure is also Chapter 650's figure for the days from the second of January. **CHECK EVERY FIGURE IN ITS OWN CARRIER PHRASE. THE FIGURE IS NOT THE POINT AND THE RULE IS.**

---

## 3. THE SENTENCES YOU DO NOT OWE AND MAY NOT PAY

**VOLUME 13 OWED ONE SENTENCE, ON WHAT AN INSTRUCTION IS, AND IT WAS PAID, IN A DOING, ON CHAPTER 626. YOU DO NOT OWE IT AND YOU MAY NOT RE-PRINT IT AS YOUR OWN. IT STANDS ALONE AT `state/volume-13-close.md` SECTION 1 AND THAT IS THE ONLY PLACE IT IS PRINTED.**

**VOLUME 12 OWED ONE SENTENCE, ON WHAT AN ADMISSION IS FOR, AT `outline/volume-12.md` SECTION 11, AND IT IS UNPAID ACROSS SIX HUNDRED AND FIFTY CHAPTERS AND ACROSS TWO VOLUMES. IT IS NOT YOURS EITHER AND IT MAY NOT BE RE-PRINTED AS YOUR OWN, BECAUSE A VOLUME THAT RE-PRINTS IT OWNS IT AND OWNING IT IS NOT PAYING IT. IT IS OWED TO A VOLUME 12 CLOSE THAT HAS NOT BEEN WRITTEN AND THAT YOU MAY NOT WRITE.**

**THE DIFFERENCE BETWEEN A DEBT AND A LIABILITY IS THE ONE THING TO CARRY OUT OF THAT PARAGRAPH. A DEBT HAS AN OWNER. A LIABILITY HAS A CREDITOR WHO CANNOT FIND THE OWNER. `state/volume-12-close.md` and `state/volume-12-roll-summary.md` DO NOT EXIST — MEASURED BY LISTING `state/` — AND A CLOSE HAS NOW PRINTED THAT UNPAID SENTENCE FIVE TIMES ALONGSIDE ITS OWN AND PAID IT NONE OF THOSE TIMES. NAME IT AS AN INHERITED LIABILITY IN YOUR OUTLINE. DO NOT PAY IT AND DO NOT HAND IT ON AS IF IT WERE YOURS.**

**WHAT YOU OWE IS A VOLUME THAT BUILDS ON A REMEDY PAID BY A PERSON.** The last thing this district did was move a reading from the fourth of the five to the fifth of the five by having a man say no out loud in a yard, in front of about nineteen people, to a stranger who came down a lane on the words of a page this district wrote. **THE ONLY THING IN THIRTEEN VOLUMES THAT HAS EVER PROTECTED A PAGE FROM BEING USED FOR THE WRONG THING IS A PERSON SAYING NO. AND A PERSON SAYING NO IS NOT A THING THAT SCALES, AND THE COUNT OF PEOPLE WHO HAVE COME DOWN THAT LANE WITH A PAGE IN THEIR HAND WENT FROM NOTHING TO NINE ACROSS THE SAME FIFTY DAYS AND DID NOT STOP.** A volume that builds on that owes the reader a sentence about what a district has when its one protection is a person, and **it must not be a sentence about trust, and it must not be about scale either, because scale is already said and it is a dead end.**

---

## 4. WHAT YOU INHERIT, AND EVERY FIGURE BELOW IS COUNTED AND NONE IS CARRIED FORWARD AS IF IT WERE SETTLED

| what | figure at Chapter 650 | the counted scope, and where it is checked |
|---|---|---|
| things this district has made | **13** | 13 on all fifty mornings, no fourteenth proposed, and `a remedy being paid is not a fifteenth, because a remedy is a thing a person does and not a thing a district has` is refused in a mouth on the page |
| things this district does not have | **5** | the fifth named on all fifty mornings as a way to pay a person who is not in a household, **paid on none of them** |
| documents this district does not own | **4** | no fifth proposed, and a page a person carried is not a fifth, and a page a person put down and took up is not a fifth |
| protected things | **5** | no sixth proposed, and a remedy is refused as a sixth in a mouth |
| conditions with no end on it | **4** | **printed on 22 of the fifty mornings and not on the other twenty-eight.** The fifth line IS one of them and the count did not move |
| columns of not-askings | **4** | no fifth ruled, and no column is ruled on any day |
| refusals to read | **9**, standing | **no figure for it is printed on any page of Volume 13 and the string is on no line of the fifty files.** A refusal entered on a page is a tenth thing of that kind and the count stays at nine |
| a month length counted | **five, standing** | the twelfth at thirty, the first at thirty-one, the third at thirty-one, **the fourth at thirty on Chapter 605 and the fifth at thirty-one on Chapter 633.** Both were counted off a board in the open in daylight and neither corrected a date |
| a new person added to this district | **none** | none on any of the fifty days, and strangers came down that lane on nine of them |
| a rate turning a year into coppers | **none** | a year is not a toll and a day is not a wage and a figure is not a price |
| a panel | **zero** | the cap is one a chapter, and every chapter carries a four-figure line set as a bolded pull-quote inside quotation marks so a grep for `>` returns nothing |
| places where those three lines can be read | **four** | **a shop counter is a place and is not on the list and may not be added to it** |
| pages on the end of that second table | **two** on all fifty mornings, three for about four minutes on Chapter 648, two again | not a ladder, and not the tenure |
| **people who have come down that lane with a page in their hand** | **nine** | not a ladder; it moved on nine mornings and every move had a person and a reason in the room before the hand |
| **the reading of that lot** | **the fifth of the five**, and not the sixth | it was the fourth of the five on 49 of the 50 mornings and moved in a clerk's hand in the afternoon of the twenty-fifth |
| the bid | **248** days at `c = 0`, **298** at the fiftieth morning, and not run on any of the fifty days | no chapter proposed closing it in a mouth or in a page |
| the figure on the sheet at that gatepost | **411**, and its own age **339** | row 12 is not a ladder and row 11 is |
| the man of about sixty-four | night **239**, slept on **238**, at `c = 0`; **289** and **288** at Chapter 650 | given nothing on all fifty days, not asked one thing, and the volume did not soften it |

**AND THE TWO FIGURES ON THAT WALL THAT ARE OUT, WHICH ARE A PERMANENT CONDITION OF THE CURRENT ORDERING AND NOT A MYSTERY. Row 3, the days nobody has entered anything, is out by a day and the size of it was never computed on a page. Row 4, the days from the second of January, is out by a whole year, and THE SIZE OF THAT ERROR IS ON A PAGE TWICE, BOTH TIMES IN A MOUTH, ON CHAPTER 608 AND ON CHAPTER 609, AND IN A LEDGER NEVER. IT MAY NOT BE PAID A THIRD TIME IN A MOUTH, IT MAY NOT BE ENTERED IN A LEDGER, AND IT MAY NOT BE COMPUTED IN YOUR OUTLINE AND PRINTED AS A FIGURE FOR A WRITER TO CARRY. A VOLUME THAT INHERITS A CALENDAR THAT CAN NOW COUNT MONTHS HAS NO EXCUSE AND HAS NO PERMISSION.**

**AND THE PARTING, WHICH IS A FINDING AND NOT A CAUSE. THE NINTH OF THE NINE PRINTED NIGHTS IS FOUR HUNDRED AND THIRTY-ONE DAYS BACK AND THE SHEET CARRIES FOUR HUNDRED AND ELEVEN, AND THE PARTING IS TWENTY FIGURES. A FIGURE IS NOT A FIGURE BECAUSE IT AGREES WITH ANOTHER FIGURE, A COINCIDENCE IS NOT A PATTERN, AND NEITHER MAY BE READ AS A THREAD.**

---

## 5. THE FOUR MEASUREMENTS YOU MUST NOT INHERIT WITHOUT RE-DERIVING, AND WHY

**These four are exact and they are the ones a batch will quote at you. Re-measure them and print your own, and name the convention with each.**

1. **LENGTH.** 150,857 words over fifty files, `wc -w`, mean 3,017.1, minimum 2,685 at Chapter 601, maximum 3,200 at Chapter 613, none outside 2,200 to 3,200. Per block 43,521, 46,715, 30,478, 30,143. **Re-derive it, because a block record in this repository has been wrong about a day-list more times than the number of blocks in it.**
2. **COUNTED CLAIMS.** 233 on a fifty-cell column, all resolving, zero mismatches, zero unparsed, 21,745 speech words, 8,254 stamped seconds, 2.63 words a second, and the relay `read the number back to himself in a low voice` is 233 and EQUALS the claim count, which is the relay's own rule and is checked three times. **THE CLAIM COLUMN, THE LEDGER'S `about N things were said out loud` FIGURE AND THE RELAY ARE ONE FIGURE AND NOT THREE THAT AGREE. Run all three and compare.**
3. **THE HEDGE.** 4,265 at 28.7 per 1,000 body words, case-sensitive whole word with titles out; 4,403 at 29.6 per 1,000 case-insensitively. **No cap was set on the hedge in advance because a cap set in advance on a hedge is a rule, and none is set now.**
4. **SHARED TWELVE-WORD RUNS.** 6,499 distinct shared, 43.1 per 1,000, counted once per distinct run in two or more files, and 53,118 if you count once per extra occurrence. **And the duplication sweep, which is the one the four block records got wrong: there are TWELVE DISTINCT SENTENCES OF TWELVE WORDS OR MORE ACROSS TWENTY-FIVE OF VOLUME 13'S FIFTY CHAPTERS AND ONE IDENTICAL PARAGRAPH, AND TEN OF THE TWELVE PAIRS STRADDLE A BLOCK BOUNDARY, WHICH IS WHY EVERY BLOCK RECORD PRINTS ZERO, AND TWO ARE INSIDE BATCH 0001'S OWN TEN FILES AND ARE A REAL DEFECT. A DUPLICATED-SENTENCE COUNT OF ZERO IS NOT EVIDENCE OF VARIETY IN A VOLUME BUILT ON A PROTECTED FRAME. YOUR BLOCK PROMPTS MUST INSTRUCT A PER-FILE SWEEP AND A VOLUME-WIDE SWEEP, AND THE PER-FILE ONE WILL NOT SEE A PAIR THAT CROSSES A BOUNDARY.**

**AND THE TITLE CAP, WHICH IS THE OTHER THING A BATCH WILL QUOTE AT YOU. Volume 13's titles run from 21 to 55 words with a median of 42, and FORTY OF THE FIFTY ARE OVER THE THIRTY-WORD CAP AND ALL FORTY ARE IN CHAPTERS 601 TO 640; THE LAST TEN ARE ALL UNDER IT. A BATCH THAT REWROTE FORTY CHAPTERS OF ANOTHER BATCH'S TITLES TO SATISFY A CAP IN ITS OWN BRIEF WOULD HAVE DONE SOMETHING NO BATCH IS ASKED TO DO. OWN YOUR OWN TITLES AND SAY SO IN THE OUTLINE.**

---

## 6. THE THINGS A VOLUME 14 MAY NOT CARRY FORWARD AS IF THEY WERE SETTLED

1. **THAT A MAN SAYING NO IS A REMEDY THAT SCALES.** It is not. It stopped one question on one morning, and the count of strangers went from nothing to nine across the same fifty days. **The finding is the pair.**
2. **THAT THE FIFTH LINE MIGHT NOT WORK.** It works. It has never been ambiguous and nobody in that yard ever had to decide. **Do not build a volume on whether an instruction works. It works, and that is worse, and a volume that has to ask is a volume that has run out of things to do with the page.**
3. **THAT THE FIFTH OF THE FIVE HAS BEEN PAID AND THE VOLUME IS OVER.** It was paid, once, by a person, on Chapter 649, and it did not advance past the fifth, and the page is still on the table. **THE FIFTH OF THE FIVE THINGS THIS DISTRICT DOES NOT HAVE IS A DIFFERENT FIFTH AND IS UNPAID, AND THE TWO ARE ON FACING CLAUSES IN THE CLOSING LEDGER OF CHAPTER 650 SO THAT A WRITER WHO CONFLATES THEM CONFLATES THEM VISIBLY.**
4. **THAT THE CALENDAR IS AN ASSUMPTION.** It is not. Two month lengths are on a page, one of them counted on the thirty-third morning of the last volume, and the outline that Volume 14 inherits says in four places that the fifth month is uncounted and is a debt, and it is counted. **CONFIRMED OFF CHAPTER 633 ITSELF. DO NOT CARRY THE DEBT ON.**
5. **THAT A FIGURE CAN BE CORRECTED.** It cannot, not even by this district's own clerk, and not on the day it is found to be out. Two of the four on that wall are out and both stand.
6. **THAT THE COLUMN FOR THE NAME OF WHOEVER READ A THING OUT LOULD MAKE A GOOD PLACE TO PUT SOMEBODY.** It is ruled and empty at about six on fifty of fifty mornings and a refusal was entered on it on the forty-ninth. **A WRITER WHO SEES THE SHAPE OF THE LAST VOLUME AND FILLS THE COLUMN HAS BROKEN THE ONLY ORDERING RULE THE NAME HAS.** The shape is this: the last volume was about a man who became the answer to a question nobody asked, and the protagonist is the man who put him there, and the yard noticed the shape of that on the morning of the no, and the column is emptier than it was on the first morning of the volume.
7. **THAT VOLUME 13 HAD NO REPEATED PROSE.** It had twelve duplicated sentences in twenty-five chapters and one identical paragraph, two pairs of them inside a block that reported zero.
8. **THAT A REMEDY BEING PAID MAKES A FIFTEENTH THING.** It does not. A remedy is a thing a person does and a protected thing is a thing a district has, and a clerk entered that reason out loud with the count on the last page.

---

## 7. THE NAME, AND IT IS NOT YOURS ALONE

**`Adrian` IS ON 43 OF 50 FILES IN VOLUME 01, 30 IN VOLUME 02, 15 IN VOLUME 03, ONE IN VOLUME 04, AND ON NO PAGE IN VOLUMES 05 TO 13, WHICH IS FIVE HUNDRED CHAPTERS. `auction` IS ON NO PAGE SINCE CHAPTER 200. `Common Measure` AND `Great Closing` ARE ON NO PAGE OF THE ENTIRE MANUSCRIPT, MEASURED AND NOT ASSUMED. `outline/ending.md` REQUIRES THAT MAN'S THREE CHOICES, A FOUNDING TOLL AND A BRASS BELL IN A PUBLIC MARKET. `outline/series.md` STILL PLANS VOLUMES 14 TO 17 OUT PAST CHAPTER 840. THERE IS NO ON-PAGE MECHANISM BY WHICH HE RETURNS, BECAUSE HE IS NOT ON ANY PAGE.**

**THE THREE AVAILABLE MOVES ARE TO RECONVERGE, TO RETCON A RETURN, OR TO RE-SCOPE THE ENDING, AND ALL THREE ARE A MAINTAINER'S. NO OUTLINE, BLOCK RECORD, BATCH, CLOSE OR REVIEW IN THIS REPOSITORY HAS EVER MADE THAT DECISION AND NEITHER MAY YOU. THE RULE IS AT `outline/volume-11.md` SECTION 6 AND IT IS NOT AN OUTLINE'S TO CHANGE: THE NAME MAY BE SETTLED ONLY ON A DAY A PERSON IN THIS DISTRICT SAYS IT OUT LOUD IN A ROOM OR A YARD, IN A SCENE, WITH THE PROSE FIRST AND THE DOCUMENT SECOND, AND NOT BEFORE DAY 41.**

**YOUR OUTLINE MAY NOT SETTLE THE NAME. IT MAY NOT NAME THE DAY. IT MAY NOT NAME A PERSON WHO WOULD SAY IT. IT MAY NOT PROMISE IT FOR A BLOCK. IT MAY NOT ALLOW A BLOCK TO PLAN FOR IT, AND A BLOCK PROMPT THAT PLANS FOR IT IS WRITTEN AGAINST THIS SECTION. A BATCH THAT REACHES A MORNING WHERE A PERSON COULD SAY IT AND DOES NOT HAS DONE ITS JOB.**

**AND THE MATERIAL IS BETTER NOW THAN IT HAS EVER BEEN AND NONE OF IT IS A SETTLING. A man in that yard said out loud what he did and did not know about himself, on a morning when a stranger asked him in front of about nineteen people what he thinks, and it was the first time in thirteen volumes that a person in that yard had heard it. HE DID NOT SAY HIS NAME AND NEITHER DID ANYBODY ELSE. The volume's own method — a person says a thing out loud in a yard and a clerk writes it down — was demonstrated two hundred and thirty-three times in the last volume and applied zero times to the protagonist, and a close has now weighed the whole of that and resolved none of it, and the weighing is at `state/volume-13-close.md` section 9 and the cost is named there at full size.**

---

## 8. THE SIX FINDINGS YOU MAY NAME ONCE EACH, AND THE THREE DEBTS YOU MAY NOT PAY

**These six have been named by a writer before you and every one of them has been right and none of them has been fixed, and that is the correct disposition for a controller-owned file. Name them if you must. Fix none of them. They are not a volume's to fix and they are not yours.**

1. **`state/phase-ledger.json` still reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0`, `range: null`, `actualModel: null`, after six hundred and fifty chapters.**
2. **`tools/__pycache__/measure.cpython-312.pyc` is tracked in git.** `PYTHONDONTWRITEBYTECODE=1` must be exported before every run of yours.
3. **`novel-reviewer` does not dispatch as a primary, so every review in this repository is a writer's account of the writer's own work, INCLUDING THE VOLUME 13 CLOSE.** `AGENTS.md`'s line "a reviewer has checked the result" remains unsatisfied for every batch to date. The fix is a registration and a dispatcher under `.opencode/` and neither is a writer's file.
4. **`outline/volume-04.md` has never existed** and is not yours to invent. Chapters 201 to 250 are canon and five of them are in no outline at all.
5. **`tools/measure.py` returns `None` for every numeral above a hundred written the ordinary way.** The resolver that works is at `state/volume-13-close.md` section 4 with its five named defects.
6. **`bible/premise.md` describes a system-apocalypse market novel and the manuscript is a yard on a bank.** The reserved scan over the fifty chapters of Volume 13 returns an empty dictionary for forty-five strings and no metric unit appears after a figure anywhere. **Nothing was restored and nothing was touched, and this is a re-scope and not a typo and it is a maintainer's.**

**AND THE THREE THINGS YOU MAY NOT PAY, PRINT AS YOUR OWN, OR HAND ON AS IF THEY WERE YOURS. The sentence Volume 13 owed was paid on Chapter 626 and stands alone in one place. The sentence Volume 12 owed is unpaid and is owed to a close that does not exist. The protagonist's name is a liability with a maintainer behind it and no on-page mechanism in front of it.**

---

## 9. WHAT YOU ARE OWING THE FILE, AND THE SHAPE OF IT

**A VOLUME OUTLINE IN THIS REPOSITORY OWES THE FOLLOWING AND NO MORE. YOU MAY NOT EXCEED IT AND YOU MAY NOT OMIT ANY OF IT.**

- **A RANGE, CHAPTERS 651 TO 700, FIFTY CHAPTERS, FIFTY DAYS, ONE A DAY, FROM THE TWENTY-SEVENTH OF THE SIXTH MONTH, WITH NO DAY CARRYING TWO DATES AND NO CHAPTER PRINTING A WEEKDAY NAME, A METRIC, A COLON-TIME OR A TWENTY-FOUR-HOUR CLOCK.**
- **A DAY MAP WITH ITS TWO STATED ASSUMPTIONS NAMED AS ASSUMPTIONS, WHICH IS THE METHOD OF THIS DISTRICT AND NOT A CAVEAT — EXCEPT THAT YOU HAVE FEWER ASSUMPTIONS THAN THE LAST OUTLINE HAD, BECAUSE TWO MONTH LENGTHS ARE NOW ON A PAGE. A MONTH THAT HAS ENDED CAN BE COUNTED OFF A BOARD AND A MONTH A PERSON IS IN CANNOT. YOUR DAY MAP MAY DEPEND ON AN UNCOUNTED MONTH ONLY IF THE MONTH IS ONE NOBODY IS IN, AND YOU MUST SAY WHICH IT IS AND WHY.**
- **A CENTRAL PRESSURE THAT CANNOT BE FIXED IN PLACE, WITH THE REASONS ALL ON A PAGE AND NOT ASSERTED.** The last four volumes each had one, and the reason they could not be fixed in place was always a guardrail the volume itself had spent six volumes building. Find the guardrail your pressure runs into before you write the resolution.
- **A RESOLUTION THAT IS A THING AND NOT A RULE, ALLOCATED TO BODIES, WITH FOUR COSTS NONE OF THEM SOFTENED, AND WITH THE THING THE VOLUME IS NOT PAYING PRINTED BESIDE THE THING IT IS PAYING BECAUSE A WRITER WILL CONFLATE THE FIFTHS.** The last volume had two fifths and put them on facing clauses of one ledger sentence so the conflation would be visible. Do the same or do something better.
- **A MIDPOINT REVERSAL FIXED IN THE OUTLINE AND NOT CHOSEN BY A WRITER BATCH, ON A NAMED DAY, IN A PLACE, IN A SCENE, WITH THE QUESTION IN THE ORDINARY VOICE AND NOBODY ANSWERING IT FOR A COUNTED NUMBER OF SECONDS.**
- **A FIXED FINAL CHAPTER IMAGE, FIXED IN THE OUTLINE, WITH ITS PROHIBITIONS ENUMERATED, AND THE PROHIBITIONS MUST INCLUDE AT MINIMUM: it may not run the bid; it may not fill the column for the name of whoever read a thing out loud; it may not pay the fifth of the five things this district does not have; it may not pay a second time in a mouth the size of the error in the fourth of the four; it may not name a night; it may not close the ninth of the nine printed nights; it may not arrive anybody; it may not give the man of about sixty-four anything; it may not reach day fifty-one; it may not put a thumb in the hollow; it may not put a hand on the fourth line or the fifth line or the third line; it may not strike, correct, supersede, replace or take out the nine words; it may not correct any figure on that wall; it may not correct a date; and it may not settle the protagonist's name.**
- **A LADDER TABLE, EIGHTEEN ROWS, INTERCEPT PLUS `c` AND NOTHING ELSE, AT `c = 0` = CHAPTER 650, WITH THE CONSTANT ROW PRINTED BESIDE IT AND THE ANCHOR TEST PRINTED BESIDE THAT, AND WITH ROW 12 PRINTING WHAT IT IS INSTEAD OF A FORMULA AND ROW 18 NAMED A TENURE.**
- **A RESERVED LIST WITH A COUNTED SCOPE ON EVERY ROW, INCLUDING A FIGURE NOBODY IS ALLOWED TO QUOTE, OR AN EXPLICIT STATEMENT THAT NO SUCH FIGURE EXISTS.**
- **A SET OF CONTINUITY GUARDRAILS, EACH NAMED AND EACH ATTRIBUTED TO A VOLUME IT CAME FROM, AND EACH OF THEM A THING A CHAPTER CAN BE ASKED NOT TO DO.**
- **A SECTION NAMING THE SENTENCES OWED, AND THIS VOLUME OWES ONE, AND IT MAY NOT BE PAID IN THE OUTLINE BECAUSE A VOLUME THAT OWES A SENTENCE MAY NOT PAY IT IN ITS OWN OUTLINE. THE CLOSE IS THE PHASE THAT MAY PRINT IT, AND IT IS PAYABLE ONLY IN A DOING AND NOT AS A THESIS, AND NOT BY A LEDGER, NOT BY A FIGURE, NOT BY A CHARACTER EXPLAINING THE VOLUME, AND NOT BY A CLERK ENTERING THAT A THING IS TRUE.**
- **AND EXACTLY ONE NEXT PHASE, WHICH IS `workspace/volume-14/batch-0001/PROMPT.md`.**

---

## 10. WHAT YOU MAY NOT DO

**You may not write a chapter. You may not create a Chapter 651. You may not create a block record, a roll, a close, a canon card, or an entry in `state/phase-ledger.json`. You may not edit `outline/series.md` or `outline/ending.md` or any earlier outline or any chapter of any volume. You may not fill the column for the name of whoever read a thing out loud and may not name a person for it. You may not settle the protagonist's name, name the day, name a person who would say it, or promise it for a block. You may not print either owed sentence as your own. You may not add a figure for the size of the error in the fourth of the four, or compute it, or hand it on as a debt. You may not hand `the length of the fifth month` on as a debt of your volume, because Chapter 633 settled it. You may not add a sixth protected thing, a fifth thing this district does not have, a fifth document it does not own, a fifth condition with no end, a fifth column, a fifth place where those three lines can be read, a rate, or a panel. You may not run the bid or propose closing it. You may not name a night or close the ninth of the nine printed nights. You may not give the man of about sixty-four anything. You may not correct a figure. You may not reach day fifty-one. You may not propose a final enemy. You may not restore any piece of `bible/premise.md`. You may not touch `scripts/`, `.github/`, `.opencode/agent/`, `tools/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md` or `opencode.json`, and you may not change workflow dispatch, phase selection, timeout, retry or checkpoint logic.**

---

## 11. WHAT YOU HAND ON

**Your successor is a batch phase and it will read your outline and nothing else unless you tell it otherwise. Hand it:**

- **The eighteen intercepts at `c = 0` = Chapter 650, printed as a table, with the constant row beside it and the anchor test beside that, and with row 12 printing what it is and row 18 named a tenure.**
- **The day map for Chapters 651 to 700, with every assumption it makes named as an assumption, and with the two month lengths that are now counted named as counted.**
- **The counts that may not be made larger, each with a counted scope and a place it is checked.**
- **The relays that are protected, each with its rule and its floor, INCLUDING THE ONE THAT IS SILENT ON EXACTLY ONE MORNING: `was not asked about the eleven miles` is on 49 of Volume 13's 50 mornings and is silent on Chapter 627, where the road keeper is asked how far the eleven miles is and answers it. A block that inherits that relay inherits a relay with one known silence and must not print a figure for the fiftieth morning of it.**
- **The sentence this volume owes, marked as owed, payable only in a doing, and not payable by you.**
- **The name, marked as unsettled, with the three moves named as a maintainer's and the rule at `outline/volume-11.md` section 6 quoted.**
- **The four measurements re-measured by you, with your conventions named and your figures printed, and not the last volume's.**
- **A central pressure that cannot be fixed in place, a resolution with four costs allocated to bodies, a midpoint reversal on a named day in a scene, and a fixed final image with its prohibitions enumerated — the same shape every outline in this repository has had for five volumes, and the only reason it has survived thirteen is that the district refused, in a mouth, to make a rule out of any of it.**
