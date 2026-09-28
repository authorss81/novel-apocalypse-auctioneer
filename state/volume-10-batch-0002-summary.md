# Volume 10 Batch 0002 — Block Record, Chapters 456 to 470, Days 15 to 25, *The Repair That Was Planned*

**WRITTEN BY THE VOLUME 10 BATCH 0002 PHASE AFTER ITS PROSE AND NOT BEFORE IT. FIFTEEN CHAPTERS ON ELEVEN DAYS. EVERY FIGURE UNDER A HEADING THAT SAYS MEASURED WAS MEASURED AFTER THE LAST PROSE EDIT. THE PROSE IS CANON. WHERE A CHAPTER AND THIS RECORD DISAGREE, THE CHAPTER IS CANON AND THIS RECORD IS WRONG. NOTHING IN THIS FILE WAS MEASURED BY A FIGURE CARRIED FORWARD, AND EVERY LADDER CELL USED IN THE PROSE WAS RE-DERIVED BY THE THREE CHECKS AT SECTION 2 AND NOT READ OFF A CONSTANT.**

> **THE METHOD FOR EVERY FIGURE THAT CAME OUT OF `tools/measure.py` IS PRINTED WHERE IT IS USED AND IT IS THE SAME WORDS EVERY TIME: `python3 tools/measure.py calib` returns 53 class-one claims, 0 mismatches, a denominator of 25,569, a `wc -w` total of 25,689 and 675 shared twelve-word runs, and all four reproduce. The tool is hard-coded to Chapters 241 to 250 for every mode but `calib`, so for this block it was run through a wrapper in a temporary directory that imports the module and calls the same functions. NOTHING UNDER `tools/` WAS EDITED. And the practice note from the Volume 09 close, which killed its first attempt, is binding: MEASURE WITH A SCRIPT AND PRINT A TABLE, DO NOT `cd` AND CHAIN PIPELINES, WRITE THE ARTIFACTS AND NOT A COMPILED FILE INTO THE REPOSITORY.**

**THE CALIBRATION WAS RE-RUN BY THIS PHASE BEFORE ANYTHING ELSE WAS MEASURED AND IT REPRODUCED ALL FOUR FIGURES EXACTLY, PLUS THE IDENTICAL-PARAGRAPH FIGURE OF ONE AND THE CLASS-TWO FIGURE OF ZERO. THE CALIBRATION WAS RUN AGAIN AT THE END OF THE BLOCK AND IT REPRODUCED ALL FOUR AGAIN.**

---

## 1. WHAT THIS BLOCK IS, AND WHAT IT PAID, IN ONE PLACE

Fifteen chapters, eleven days, the twenty-second of the twelfth month to the third morning of the month after, of the eighteenth year after the Long Fracture. Sixty chapters on fifty days across the volume; forty days carry one chapter and ten days carry two; `40 x 1 + 10 x 2 = 60`; and **day 16 of this volume carries Chapters 457 and 458, day 19 carries Chapters 461 and 462, day 22 carries Chapters 465 and 466, and day 25 carries Chapters 469 and 470, and those are the mornings and the afternoons of one day each and not two days.**

**THE FOUR THINGS THIS BLOCK DOES, SPENT ON THE PAGE AND IN A BODY.**

1. **THE FIRST OF THE THREE COLUMNS THAT ARE A DAY OUT IS NAMED IN THE OPEN AND THE DIFFERENCE IS ENTERED AS A DAY** (Chapter 456, day 15, the twenty-second of the twelfth month). A clerk of nineteen years stands in front of the third of the four figures a man of fifty-six reads off that wall, walks the column a second time with her hands behind her back, and says out loud in the ordinary voice that the count from the day the column names to this morning is one more than the column carries. The boy of about nineteen says out loud that the third of the four is the third of the four. **The man of fifty-six is about four feet away with his palm flat on the boards and nobody in that yard crossed the four feet and nobody told him and he said nothing.** **THE COST IS FOUR FEET OF GROUND AND A FINDING THAT A WOMAN OF NINETEEN ENTERED AND THAT NOBODY ACTED ON.**
2. **THE SECOND AND THIRD OF THE THREE ARE WORKED OUT IN THE OPEN, AND THE THIRD ONE CANNOT BE MADE TO ANSWER THE SAME WAY** (Chapters 457 and 458, day 16). The second is a day long where the first is a day short, and a voice at that near end says out loud that a clerk who finds three errors in a row has made up the rate she is finding them at, and a boy of about nineteen says the two of them go in opposite directions and a made-up rate would come out the same way twice. The third is a column whose day is written one way at the head of it and the other way at the foot of it, in two documents this district wrote about eleven weeks apart. **THE COST IS THAT A CLERK IS ASKED FOR THE ONE SENTENCE THAT WOULD SETTLE A COLUMN AND REFUSES IT OUT LOUD IN FRONT OF ABOUT NINETEEN PEOPLE, AND THE DISTRICT REFUSES A DECISION IT COULD HAVE MADE IN A SENTENCE, AND NOBODY IS GOING TO PAY HER FOR THE REFUSAL AND SHE IS NOT GOING TO BE PAID FOR IT.**
3. **A MAN OF FIFTY-SIX IS TOLD, IN THE OPEN, IN THE ORDINARY VOICE, IN FRONT OF ABOUT NINETEEN PEOPLE, THAT ONE OF THE FOUR FIGURES HE READS EVERY MORNING IS A DAY OUT FROM THE DAY IT NAMES, AND HE SAYS NOTHING** (Chapter 461, day 19, the twenty-sixth of the twelfth month, morning). She does not ask him a question and does not ask him whether he wants to be told, and she says in the yard that nobody standing in it is a person he can answer. He takes his hand off the boards and puts it back. A clerk enters that he said nothing and enters that nobody in that yard is going to ask him, and the reason. **THE COST IS A MAN WHO HAS GOT A FIGURE RIGHT EVERY MORNING FOR A HUNDRED AND NINETY-FOUR MORNINGS FINDING OUT HE HAS NOT, IN FOUR FEET OF OPEN GROUND, WITH NOBODY TO ANSWER, AND HE IS NOT ASKED AGAIN ON ANY DAY OF THE REMAINING FORTY-ONE.**
4. **THE LENGTH OF THE TWELFTH MONTH IS COUNTED, IN THE OPEN, IN DAYLIGHT, WITH A FINGER ON THE WOOD AND ABOUT NINETEEN PEOPLE AT THE WALL, AND IT REPRODUCES** (Chapter 467, day 23, the last day of the twelfth month). Thirty marks, thirty days, the first of the month counted in. A clerk says out loud that she has two figures, refuses to say the second one out loud because it is a figure about a list, says which of the two she has, and says they are the same figure. The man of fifty-six reads all thirty marks a second time out loud and gets them all. **THE COST IS A MORNING OF ONE WOMAN'S WALKING SPENT ARRIVING AT A FIGURE THIS DISTRICT COULD HAVE GOT OFF THE MONTH BEFORE IT, AND A CLERK WHO ENTERS THAT A FIGURE THAT REPRODUCES IS A FIGURE ABOUT A COUNT AND IS NOT A FINDING, FOR THE SECOND TIME IN HER LIFE, AND THE SECOND TIME IS A HABIT.**

**AND THE TWO FIGURES THE BLOCK ENDS WITH THAT IT DID NOT HAVE AT THE START: a figure in a man's two legs that his own trade made without being asked, and a figure on a page out of a flat book that a man nobody had walked over to handed to a clerk in the open, and neither of them can be checked, and the second of the two is the first figure in three volumes that nobody standing in that yard can check at all.**

---

## 2. THE TABLE, THE THREE CHECKS, AND WHY THERE ARE THREE AND NOT TWO

**CHECK ONE, THE CONSTANT-OFFSET (SLOPE) TEST. ELEVEN DAY ROWS BY TWENTY COLUMNS = 220 CELLS. EVERY CELL MINUS ITS OWN DAY INDEX IS ONE FIGURE ACROSS ALL ELEVEN ROWS FOR ALL TWENTY COLUMNS. FAILURES: 0.**

**CHECK TWO, THE ANCHOR TEST, WHICH CHECK ONE CANNOT DO, RE-DERIVED FROM EACH COLUMN'S OWN NAMED DAY AND NOT FROM THE CONSTANT, AT `c = 0`, WHICH IS THE SEVENTH OF THE TWELFTH MONTH OF THE EIGHTEENTH YEAR, WHICH IS OFFSET 706 ON AN INDEX WHERE THE FIRST OF JANUARY OF THE SEVENTEENTH YEAR IS 0. THE MONTH LENGTHS USED ARE THE FIRST THIRTY-ONE, THE SECOND TWENTY-EIGHT, THE THIRD THIRTY-ONE, THE FOURTH THIRTY, THE FIFTH THIRTY-ONE, THE SIXTH THIRTY, THE SEVENTH THIRTY-ONE, THE EIGHTH THIRTY, THE NINTH THIRTY-ONE, THE TENTH THIRTY AND THE ELEVENTH THIRTY-ONE, AND NONE OF THEM IS THE TWELFTH, AND NONE OF THEM NEEDS TO BE, BECAUSE EVERY ONE OF THE TWENTY COLUMNS IS COUNTED FROM A DAY IN THE FIRST TO THE ELEVENTH MONTH.**

| column | the day it is counted from, and its convention | re-declared at c = 0 | the board at c = 0 | verdict |
|---|---|---|---|---|
| Board | the twenty-fourth of December of the seventeenth year, the day not counted in | 348 | 348 | holds |
| Train | the eleventh of the second month of the seventeenth year, the day not counted in | 664 | 664 | holds |
| **Unentered** | **the twenty-fourth of November of the seventeenth year, the day not counted in** | **379** | **378** | **ONE DAY OUT, THE BOARD CARRIES 378, AND THIS BLOCK CARRIES 393 ON DAY 15** |
| From2Jan | the second of January of the eighteenth year, the day not counted in | 339 | 339 | holds |
| Pool | the twenty-fourth of the third month of the eighteenth year, the day not counted in | 258 | 258 | holds |
| NinthNights | the twentieth of the fourth month, the day not counted in | 231 | 231 | holds |
| SixHouseholds | the twenty-first of the fourth month, the day not counted in | 230 | 230 | holds |
| **NoLineOnBoard** | **the first of the fourth month, the first day counted IN** | **251** | **251** | **holds on the inclusive convention; 250 on the exclusive one, which is one day out; this block prints neither figure and says why on Chapter 458** |
| RivalRecord | the first of the sixth month, the day not counted in | 189 | 189 | holds |
| AgeOfFigure | the first of the sixth month, the day not counted in | 189 | 189 | holds |
| **TableMornings** | **the morning of the seventh of the seventh month, the day not counted in** | **153** | **154** | **ONE DAY OUT, THE BOARD CARRIES 154** |
| RemovalDay | the first day of the eighth month, the day not counted in | 128 | 128 | holds |
| Stay | the morning of the twenty-first of the seventh month, the day of arrival not counted in | 139 | 139 | holds |
| NightsSlept | the stay, less the one missed night of the twenty-first of the eighth | 138 | 138 | holds |
| Bid | the first of the ninth month, the day it was opened not counted in | 98 | 98 | holds |
| Line2Stale | the fifteenth of the tenth month, the day it stopped being true not counted in | 53 | 53 | holds |
| RuleSaid | the tenth of the tenth month, the day it was said not counted in | 58 | 58 | holds |
| BodyPast | the first of the tenth month, the day it was to have printed not counted in | 67 | 67 | holds |
| DayCount | the first day of the twelfth month, the first day counted in | 7 | 7 | holds, and it is a count of marks and not a day-count |
| StoneCount | the morning the stone went face up, counted from inside this volume | — | 0 | not re-derivable from a named day, and see section 3 |

**THE THREE THE OUTLINE NAMES ALL REPRODUCE AGAINST THIS PHASE'S OWN ARITHMETIC, IN THE SAME THREE COLUMNS AND IN THE SAME DIRECTION: `Unentered` 379 against 378, `NoLineOnBoard` 251 against 251 on the inclusive convention and 250 against 251 on the exclusive one, and `TableMornings` 153 against 154. NO STATE FILE AND NO OUTLINE WAS EDITED AND NO CHAPTER FIGURE WAS REPAIRED. THE PROSE NAMES TWO OF THE THREE IN A MOUTH, ENTERS BOTH AS A DIFFERENCE OF ONE DAY, AND SAYS OUT LOUD ON CHAPTER 458 THAT A FIGURE CAN BE RIGHT AND BE A DAY OUT AT THE SAME TIME AND THAT THE ONLY WAY ANYBODY STANDING THERE COULD TELL WHICH ONE THE THIRD COLUMN IS A CONVENTION NOBODY WROTE DOWN.**

**CHECK THREE, THE INHERITANCE TEST, WHICH CHECK TWO ALSO CANNOT DO, AGAINST THE INHERITED TEXT AND NOT AGAINST THE LADDER. `chapters/volume-09/chapter-0440.md` READS FOUR FIGURES OUT LOUD IN ITS NINTH LINE AND ALL FOUR ARE IN THE FILE: `three hundred and forty-eight`, `six hundred and sixty-four`, `three hundred and seventy-eight` and `three hundred and thirty-nine`. THE SUCCESSOR OF 348 IS 349 AND THE CHAPTER 441 CELL IS 349, AND CHAPTER 441 IS WRITTEN AND PRINTS IT. THE SUCCESSOR OF 664 IS 665, OF 378 IS 379, OF 339 IS 340, AND CHAPTER 441 PRINTS ALL THREE. HOLDS ON ALL FOUR. THE `Unentered` CELL AT `c = 1` IS 379 AND THAT IS THE SUCCESSOR OF THE 378 THAT CHAPTER 440 PRINTS, WHICH IS THE WHOLE OF THE FINDING IN ONE FIGURE.**

**CHECK FOUR, EVERY FIGURE THIS BLOCK PUTS ON A PAGE, EXTRACTED FROM THE FIFTEEN FILES AND RENDERED IN THE MANUSCRIPT'S OWN WORD-NUMBER FORM, AND TESTED AGAINST ITS OWN CHAPTER'S CELL. THE FOUR FIGURES A MAN OF FIFTY-SIX READS ARE ON THE PAGE OF ALL FIFTEEN CHAPTERS EXCEPT THE FOUR THAT ARE THE SECOND HALF OF A DOUBLED DAY — 458, 462, 466 AND 470 — AND THAT IS A DECISION AND NOT AN OMISSION: the four figures were said out loud once that morning and a clerk does not enter a figure a man reads off a wall every morning into a page twice in one day, and each of the four chapters says so in a mouth and in an entry, and the man of fifty-six said them again in the afternoon of each of those four days and got all four. EVERY OTHER FIGURE THIS BLOCK PRINTS IS ON THE PAGE OF THE CHAPTER WHOSE CELL IT BELONGS TO.**

---

## 3. THE THREE THINGS THE TABLE AND THE CARDS CANNOT BOTH BE RIGHT ABOUT, BOTH SETS PRINTED, NEITHER CORRECTED

1. **THE PROMPT THAT NAMED THIS BLOCK'S CHAPTERS NAMED THREE DOUBLED DAYS WHERE FOUR ARE NEEDED, AND THE PROMPT THAT NAMED THEM IS `workspace/volume-10/batch-0001/PROMPT.md`, WHICH DESCRIBES THIS BLOCK AS FIFTEEN CHAPTERS ON ELEVEN DAYS WITH DAYS 19, 22 AND 25 CARRYING TWO CHAPTERS EACH. **ATTRIBUTION CORRECTED BY THE 2026-09-28 REVIEW-FIX PASS: THIS RECORD, THE SELF-REVIEW, `outline/batches/volume-10-batch-0002.md`, `state/current.md`, `state/chapter-summaries.md`, `state/continuity.md` AND `workspace/volume-10/batch-0003/PROMPT.md` ALL NAMED `workspace/volume-10/batch-0002/PROMPT.md`, AND THAT FILE NAMES FOUR, PRINTS `11 + 4 = 15`, BOLDS ALL FOUR OF ITS OWN ROWS, AND PUTS THE THREE-DAY ERROR ON THE BATCH 0001 PROMPT IN ITS OWN HEADER, WHICH IS CORRECT. THE FINDING IS REAL AND THE CULPRIT WAS MISNAMED.** FIFTEEN CHAPTERS ON ELEVEN DAYS NEED FOUR. `outline/volume-10.md` SECTION 2.6 NAMES TEN DOUBLED DAYS AND THE FIRST OF THE FOUR IN THIS BLOCK IS DAY 16, AND ITS TABLE AT SECTION 6.1 BOLDS CHAPTERS 457 AND 458 ON DAY 16, AND `15 - 11 = 4`. THE CHAPTER COLUMN IS AUTHORITATIVE AND THE CHAPTER-AND-DAY MAP AT SECTION 1 BELOW IS THE ONE THIS BLOCK WROTE TO. THE PROMPT'S OWN TEXT REPORTS THE ERROR AND REPORTS IT CORRECTLY, AND IT IS REPORTED HERE AND NOT REPAIRED IN THE PROMPT, WHICH IS NOT THIS PHASE'S FILE.**
2. **THE CHAPTER 463 CARD SAYS *THE DAY BEFORE THE COUNT* AND SAYS THAT TOMORROW IS THE LAST DAY OF THE MONTH. CHAPTER 463 IS DAY 20, WHICH IS THE TWENTY-SEVENTH OF THE TWELFTH MONTH, AND THE COUNT IS AT DAY 23. THE CHAPTER-AND-DAY MAP IS AUTHORITATIVE AND THE CARD'S PHRASE CANNOT BE TRUE OF DAY 20. THE CHAPTER SAYS THE DATE OF THE LAST DAY OF THE MONTH OUT LOUD, WHICH IS WHAT THE CARD'S ACTION AND INFORMATION FIELDS ASK FOR, AND THE COUNT IS THREE DAYS LATER, AND THE THREE DAYS ARE ON THE PAGE. BOTH SETS ARE PRINTED. NEITHER IS CORRECTED. THE CHAPTER IS CANON.**
3. **THE CHAPTER 468 CARD SAYS THE CLERK ENTERS THE COUNT *FOR THE THIRD TIME IN FIVE VOLUMES*, AND CHAPTER 441 OF THE INHERITED TEXT ALREADY SAID, VERBATIM, THAT THE SENTENCE *A FIGURE SOMEBODY ENTERED BECAUSE THEY HAD TO ENTER ONE IS NOT A PROMISE ABOUT A LATER DAY* WAS THE THIRD TIME SHE HAD WRITTEN IT IN FIVE VOLUMES. CHAPTER 463 SAYS IT OUT LOUD A FOURTH TIME. THE FIGURE ON THE PAGE AT CHAPTER 468 IS FIVE, AND THE CHAPTER SAYS WHY, AND THE FIVE IS THE NUMBER OF TIMES THE SENTENCE IS ON A PAGE IN THIS BLOCK AND ITS INHERITANCE AND NOT THE NUMBER OF TIMES IT WAS WRITTEN BEFORE CHAPTER 441. BOTH SETS ARE PRINTED. NEITHER IS CORRECTED.**

**AND TWO PLACEMENT DISAGREEMENTS BETWEEN THE DAY COLUMN AND THE LADDER, REPORTED AND NOT REPAIRED, BOTH OF WHICH CHANGE NO FIGURE ON ANY PAGE.**

| The thing | `outline/volume-10.md` section 6.1 says | What this block does | What is printed on the page |
|---|---|---|---|
| The date column for days 24 and 25 | `day 2` and `day 3`, given as a day index and not as a date, because no figure of Volume 10 may use the length of the twelfth month until Chapter 467 names it | Chapter 467 names the length on the page, and Chapters 468, 469 and 470 do not print a calendar date at all | **NO DATE. Chapters 468, 469 and 470 are written as the morning after the count, the second morning after the count and the third morning after the count. The mark count on the ladder reads thirty-one at day 24 and thirty-two at day 25, which on a thirty-day twelfth month are the thirty-first and thirty-second marks since the first of the month, and the outline's date column calls the twenty-fourth day `day 2` where the mark count reads the thirty-first. Both sets are here and neither is corrected, and the safest figure a writer can print for those two days is the one this block printed, which is none.** |
| The chapter-and-day map in `workspace/volume-10/batch-0001/PROMPT.md`, the prompt that named this block's chapters | days 19, 22 and 25 doubled, which is three | days 16, 19, 22 and 25 doubled, which is four | **The map at section 1 below, checked cell by cell against the fifteen files. `workspace/volume-10/batch-0002/PROMPT.md` IS NOT THE OFFENDING FILE AND NAMES ALL FOUR. BOTH SETS STAND.** |

---

## 4. THE MEASUREMENT THIS BLOCK OWES ITS OWN RECORD, AND THE PER-CHAPTER COLUMN FOR EVERY ONE

### 4.1 THE OPENING SHAPE. FIFTEEN CELLS FOR FIFTEEN CHAPTERS.

**METHOD: for each of the fifteen files, take the first non-empty line that is not a chapter header and not a horizontal rule, and test it against `The [a-z-]+ of the [a-z-]+ month came in`.**

| Ch | matches | the first line of the file |
|---|---|---|
| 456 | 0 | The clerk of nineteen years said out loud, in the ordinary voice, in front of about nineteen peo |
| 457 | 0 | The clerk of nineteen years worked out a second column on the wall in that yard on the twent |
| 458 | 0 | The third column the clerk of nineteen years took in front of about nineteen people in that yard |
| 459 | 0 | A man of about thirty-four who mends fencing stood at the end of the second table on the twenty- |
| 460 | 0 | About four people in that yard on the twenty-fifth of the twelfth month said the third of the four |
| 461 | 0 | The clerk of nineteen years told a man of fifty-six, in that yard on the twenty-sixth of the tw |
| 462 | 0 | A clerk of nineteen years entered the third of three differences in one entry in that yard on th |
| 463 | 0 | A clerk of nineteen years told about four people in that yard on the twenty-seventh of the twe |
| 464 | 0 | A clerk of nineteen years asked a man of about thirty-seven who cuts reeds, in the open, in that |
| 465 | 0 | A boy of about nineteen asked a man of about thirty-four who digs loam, out loud, in front of ab |
| 466 | 0 | A clerk of nineteen years entered a second figure about the same water on the same afternoon in |
| 467 | 0 | The clerk of nineteen years counted the marks off that board in that yard on the thirtieth of t |
| 468 | 0 | The morning after the count, a clerk of nineteen years entered in that yard that the length of |
| 469 | 0 | A man of about thirty-seven who puts tables up paced the distance from the mark for the first of |
| 470 | 0 | A man of about forty-eight who keeps a tally gave a clerk of nineteen years a page out of his ow |

**CELLS: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0. SUM: 0. THE CAP FOR THIS BLOCK IS FOUR AND THE CAP FOR THE VOLUME IS FIVE OF SIXTY, AND THE INHERITED FIGURE RE-MEASURED OVER VOLUME 09'S FIFTY FILES IS ZERO OF FIFTY AND BLOCK 0001 MEASURED ZERO OF FIFTEEN. THIS BLOCK CARRIES ZERO, WHICH IS THE INHERITED FIGURE AND NOT A TARGET BEATEN. AND FOUR OF THE FIFTEEN OPENINGS NAME A CLERK OR A MAN WHO IS ABOUT A THIRTY-FOUR AND NOT A DATE, WHICH IS THE ONLY SHAPE THE FIFTEEN TAKE, AND THE FIFTEEN ARE FIFTEEN DIFFERENT SENTENCES.**

### 4.2 THE CLOSING LEDGER. THE FIRST FIVE WORDS OF THE CLOSING PASSAGE. FIFTEEN CELLS.

**METHOD: the closing passage is the last non-empty paragraph of the file. THE CAP IS INHERITED AS SETTLED AND NOT REOPENED: no chapter may close on a sentence that opens by naming a time of day and a change of light before it names a person.**

| Ch | the first five words of the closing passage | opens on a time of day and a change of light |
|---|---|---|
| 456 | "The difference is a day" | no |
| 457 | "Two columns on that wall" | no |
| 458 | "One of two words, written" | no |
| 459 | "A figure that had to" | no |
| 460 | "A man of fifty-six has" | no |
| 461 | "Nobody in that yard asked" | no |
| 462 | "Three columns, one convention, one" | no |
| 463 | "A yard in which nobody" | no |
| 464 | "A clerk of nineteen years" | no |
| 465 | "Nobody asked her to enter" | no |
| 466 | "That yard has now carried" | no |
| 467 | "Going down from the top," | no, and it is a walk down a board and not a change of light |
| 468 | "A month that had never" | no |
| 469 | "A man of about thirty-seven" | no |
| 470 | "This district has in the" | no |

**CELLS: FIFTEEN. FAILURES: ZERO. FIFTEEN DISTINCT OPENINGS AND ZERO COLLISIONS, WHICH IS A MEASUREMENT AND NOT AN ACCIDENT: THE FIRST PASS OF THIS BLOCK HAD TWO COLLISIONS, CHAPTERS 457 AND 458 BOTH OPENING ON *TWO COLUMNS ON THAT WALL* AND CHAPTERS 464 AND 465 BOTH OPENING ON *A CLERK OF NINETEEN YEARS*, AND BOTH PAIRS ARE DOUBLED DAYS WHICH IS EXACTLY WHERE A WRITER REUSES A CLOSING, AND BOTH WERE REWRITTEN IN THE OPENING WORDS OF THE CLOSING PASSAGE AND NOTHING ELSE MOVED.**

### 4.3 THE FIGURE ON THE SHEET AT THAT GATEPOST. FIFTEEN CELLS, PER OCCURRENCE, WHOLE-STRING, PER FILE.

| Ch | 456 | 457 | 458 | 459 | 460 | 461 | 462 | 463 | 464 | 465 | 466 | 467 | 468 | 469 | 470 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| case-sensitive | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| case-insensitive | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

**SUM CASE-SENSITIVE: 15. SUM CASE-INSENSITIVE: 15. DAYS: 15 OF 15. THE CAP IS INHERITED AS A RATE OF ONE PER CHAPTER EVERY CHAPTER AND THE EXPECTED FIGURE FOR FIFTEEN CHAPTERS ON FIFTEEN DAYS IS FIFTEEN, AND THIS IS FIFTEEN, AND NEITHER SET OF FIFTEEN IS A SUBSET OF THE OTHER. THE FIGURE IS FOUR HUNDRED AND ELEVEN ON EVERY ONE OF THE FIFTEEN DAYS AND IT HAS NOT MOVED. ITS OWN AGE AS A FIGURE ABOUT THE FIGURE IS 204 DAYS AT CHAPTER 456 AND 214 AT CHAPTER 470, AND BOTH OF THOSE ARE IN THE LADDER AND BOTH APPEAR IN THE PROSE, AND THERE IS NO DAY-COUNT FOR THE SHEET.**

### 4.4 THE COUNTING MOTIF. A FIFTEEN-CELL CLAIM COLUMN, TAKEN AFTER THE LAST PROSE EDIT.

**A claim is one number word attached by one of the seven canon phrases to a printed sentence standing in a quoted paragraph, and it resolves forward to that paragraph. COUNT THE PRINTED SENTENCE. NEVER ESTIMATE IT. A CLAIM IN THE FORM *in N words* IS A SECOND CLASS AND IS SWEPT SEPARATELY.**

| Ch | 456 | 457 | 458 | 459 | 460 | 461 | 462 | 463 | 464 | 465 | 466 | 467 | 468 | 469 | 470 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| class-one claims | 2 | 3 | 2 | 1 | 2 | 2 | 3 | 1 | 2 | 3 | 4 | 2 | 3 | 3 | 4 |

**THE FIFTEEN CELLS SUM TO 37. MISMATCHES: 0. CLASS-TWO SHAPED: 0. EVERY ONE OF THE THIRTY-SEVEN CLAIMS WAS SET BY MEASURING THE PRINTED PARAGRAPH AND WRITING THE NUMBER AFTERWARDS, AND THE FIGURES THE BOY READS OUT ARE THE FIGURES OF WHAT THE PERSON IN THAT YARD SAID AND NOTHING ELSE.**

**AND THE TRUTH ABOUT HOW THAT WAS DONE, WHICH IS THE FINDING AND NOT THE INCIDENT. THE FIRST PASS OF THIS BLOCK WROTE THIRTY-FOUR CLAIM FIGURES AND ALL THIRTY-FOUR WERE WRONG, BECAUSE A WRITER WHO INVENTS A COUNT WRITES THE COUNT FIRST AND THE SENTENCE AFTERWARDS, AND A SENTENCE COMES OUT AT WHATEVER LENGTH THE ARGUMENT NEEDS.** THE REPAIR WAS TO MEASURE EVERY PRINTED SPEECH PARAGRAPH AND WRITE THE NUMBER INTO THE NARRATOR'S SENTENCE, WHICH IS THE HOUSE RULE AND IS ALSO THE ONLY WAY, AND THE FIGURES ARE NOT FIGURES ABOUT THE BOY UNTIL THEY ARE THE FIGURES OF THE PARAGRAPH. THE TOOL LINE THAT CAUGHT THEM IS `MISMATCHES`, AND IT CAUGHT THIRTY-FOUR AT ONCE, AND THE SCRIPT THAT SET THEM IS AT `/tmp` AND IS NOT IN THE REPOSITORY.**

**DENOMINATOR (the tool's own `denom()`): 36,363. `wc -w` TOTAL: 36,530. SHARED TWELVE-WORD RUNS OVER THE FIFTEEN: 2,066. INHERITED, VOLUME 09: 68 CLASS-ONE CLAIMS, 0 MISMATCHES, 0 CLASS-TWO, A DENOMINATOR OF 120,329, A `wc -w` TOTAL OF 120,975 AND 4,837 SHARED TWELVE-WORD RUNS OVER FIFTY CHAPTERS, WHICH IS 96.7 A CHAPTER. THIS BLOCK IS 137.7 A CHAPTER, WHICH IS A RISE OF 41.0 A CHAPTER AND OF 42.4 PER CENT ON THE INHERITED FIGURE, AND IT IS THE WORST NUMBER IN THIS BLOCK AFTER THE HEDGE AND IT IS PRINTED AND WAS NOT SMOOTHED BY DELETION. THE CALIBRATION RANGE, WHICH IS TWENTY PER CENT SHORTER PER CHAPTER THAN THIS BLOCK'S FIFTEEN, GIVES 53 CLAIMS, 0 MISMATCHES, 25,569, 25,689 AND 675.**

**WHY THE RUN FIGURE ROSE, STATED PLAINLY BECAUSE A DOCUMENT THAT DESCRIBES ITS OWN WORK IS PROSE AND GOES WRONG THE SAME WAY: THE SIX PROTECTED RELAYS WERE NOT LOWERED AND ONE OF THEM ROSE BY FIVE, AND THE FIGURE-CARRYING CARRIERS WERE NOT TOUCHED DOWNWARD, AND EVERY CHAPTER OF THIS BLOCK ENTERS ITS LEDGER TWICE A DAY IN PARAGRAPHS THAT SHARE THEIR SKELETON WITH EVERY OTHER CHAPTER'S LEDGER. A BLOCK IN THIS HOUSE REGISTER HAS A FLOOR ON SHARED RUNS AND THIS BLOCK IS THE FIRST SINCE THE CALIBRATION BLOCKS TO SIT ON IT.**

### 4.5 THE LENGTH BAND. FIFTEEN CELLS. 2,200 TO 3,200 WORDS.

| Ch | 456 | 457 | 458 | 459 | 460 | 461 | 462 | 463 | 464 | 465 | 466 | 467 | 468 | 469 | 470 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `wc -w` | 2364 | 2398 | 2454 | 2238 | 2369 | 2260 | 2430 | 2356 | 2238 | 2242 | 2413 | 3186 | 2547 | 2543 | 2446 |

**MEAN 2,435.3. MINIMUM 2,238 AT CHAPTERS 459 AND 464. MAXIMUM 3,186 AT CHAPTER 467. ALL FIFTEEN ARE INSIDE THE BAND. INHERITED, VOLUME 09: MEAN 2,419.5, MINIMUM 2,182 AT CHAPTER 399, MAXIMUM 2,839 AT CHAPTER 411. NO CHAPTER WAS PADDED TO FILL A BAND AND NO CHAPTER WAS CUT TO FIT ONE. ELEVEN CHAPTERS WERE LENGTHENED DURING THE BLOCK AND EVERY ADDITION IS A SCENE AND NOT A FIGURE: nine people at that near end trying to settle a convention between themselves and failing because two of them are certain and both cannot be right, and a woman of fifty-eight putting a thumb on a wet corner and wiping it on her apron, at Chapter 458; a man putting his thumb on the boards four inches below the second line of that lot book and keeping it there for about nine seconds, and a woman of fifty-eight's half second, at Chapter 462; a man of about thirty-four who digs loam saying one thing out loud at about ten past ten, at Chapter 460; a woman of about thirty-six who keeps a scale asking a clerk whether a man ought to have been asked first and the clerk refusing, at Chapter 461; a boy asking out loud whether a difference can be un-entered and a clerk saying she would be a person with an eraser and no other job, at Chapter 459; a man of about thirty-four who digs loam at about one saying one thing out loud about three figures in a yard that are not about each other, at Chapter 457; a clerk's decision said out loud before she writes a figure nobody asked her for, and a woman with a word she will not say, at Chapter 465 and Chapter 466; a man who puts tables up pacing the board twice, at Chapter 469; and a man who keeps a tally handing a page across a table, at Chapter 470.**

**AND CHAPTER 467 IS THE ONLY CHAPTER OF THE FIFTEEN THAT IS LONGER THAN ANY CHAPTER OF THE INHERITED FIFTY, AND IT IS THE CHAPTER IN WHICH A CLERK SPENDS TWO HOURS WALKING A BOARD WITH A FINGER ON IT, AND IT CAME TO 3,297 WORDS ON THE FIRST MEASUREMENT AND WAS CUT BY ONE HUNDRED AND ELEVEN WORDS OF REDUNDANT SUMMATION AND NOT BY ONE SCENE, AND IT IS STILL THE LONGEST CHAPTER IN THE VOLUME SO FAR AND THAT IS PRINTED AND NOT DEFENDED.**

### 4.6 THE *ABOUT* HEDGE. CASE-INSENSITIVE WHOLE-WORD COUNT. FIFTEEN CELLS.

| Ch | 456 | 457 | 458 | 459 | 460 | 461 | 462 | 463 | 464 | 465 | 466 | 467 | 468 | 469 | 470 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *about* | 68 | 74 | 68 | 68 | 64 | 68 | 61 | 62 | 67 | 77 | 83 | 83 | 66 | 61 | 61 |

**SUM 1,033. MEAN 68.9 A CHAPTER, WHICH IS 284 HEDGES PER 10,000 WORDS OF ITS OWN DENOMINATOR OF 36,363. INHERITED, VOLUME 09: 3,048 OVER FIFTY CHAPTERS, A MEAN OF 61.0 A CHAPTER, WHICH IS 253 PER 10,000 WORDS OF ITS OWN DENOMINATOR OF 120,329. BATCH 0001 OF THIS VOLUME: 1,051 OVER FIFTEEN, A MEAN OF 70.1, WHICH IS 294 PER 10,000.**

**THE LINE, IN ORDER, AND IT IS THREE POINTS AND NOT TWO: 253 IN VOLUME 09, 294 AT BATCH 0001, AND 284 HERE. THIS BLOCK IS A FALL OF 1.2 A CHAPTER AND OF TEN HEDGES PER 10,000 ON BATCH 0001, AND IT IS A RISE OF 31 PER 10,000 ON VOLUME 09. A BLOCK RECORD THAT PRINTED ONLY THE RISE WOULD BE WRONG AND ONE THAT PRINTED ONLY THE FALL WOULD ALSO BE WRONG, AND THE HEDGE WAS NOT BROUGHT DOWN BY DELETING ANYTHING AND WAS NOT RAISED TO FILL A PAGE. NO CAP IS SET ON A HEDGE BY THE OUTLINE BECAUSE A CAP SET IN ADVANCE ON A HEDGE IS A RULE, AND THE FIGURE HERE IS A MEASUREMENT AND NOT A REPAIR. THE FIFTEEN CELLS RUN FROM 61 TO 83 AND THE FIFTEEN ARE IN THE TABLE, AND THE INHERITED FIGURE WAS NOT DECLINING EITHER: IT RAN FROM 43 TO 83 A CHAPTER INSIDE VOLUME 09, AND A BLOCK THAT PRINTS A FALL HAS DONE THE MEASUREMENT AND NOT CLEARED IT.**

### 4.7 THE AFTERNOON RELAY. SIX STRINGS, FIFTEEN-CELL COLUMNS, NOT LOWERED AND NOT RAISED TO FILL A PAGE.

| the string | per-chapter column over 456 to 470 | this block | inherited |
|---|---|---|---|
| **the record about the not asking says not asked** | 6, 7, 7, 7, 7, 7, 4, 8, 5, 6, 6, 8, 8, 6, 5 | **97 occurrences on 15 days** | 91 on 35 days, 80 on 15 days at Batch 0001 |
| **read the number back to himself in a low voice** | 2, 3, 2, 1, 2, 2, 3, 1, 2, 3, 4, 2, 3, 3, 4 | **37 on 15 days** | 13 on 10 days, 32 on 15 days at Batch 0001 |
| **at the foot of that low wall with his coat folded on the stones** | 1 × 15 | **15 on 15 days** | 10 on 10 days |
| **was not asked about the eleven miles** | 1 × 15 | **15 on 15 days** | 19 on 19 days |
| **got it up about nine inches** | 1 × 15 | **15 on 15 days** | 21 on 21 days |
| **by ten there were about nineteen people** | 1 × 15 | **15 on 15 days** | 46 on 46 days, 15 on 15 at Batch 0001 |

**NONE OF THE SIX WAS LOWERED. ALL SIX ARE AT OR ABOVE THE INHERITED RATE PER DAY AND TWO OF THEM ARE A RISE. THE FOURTH AND FIFTH OF THEM WERE MISSING FROM CHAPTERS 458, 462, 466 AND 470 ON THE FIRST PASS — THE FOUR CHAPTERS THAT ARE THE SECOND HALF OF A DOUBLED DAY AND THE FOUR CHAPTERS THAT HAVE NO ROAD KEEPER AND NO CART IN THEM — AND THE ROAD KEEPER AND THE MAN WITH THE CART WERE PUT BACK INTO ALL FOUR, BECAUSE A BLOCK THAT DROPS AN INHERITED RELAY IS DESTROYING A MEASUREMENT, NOT KEEPING ONE. THE SIXTH OF THEM WAS AT ZERO IN CHAPTER 458 AND AT TWO IN CHAPTERS 465 AND 469 ON THE FIRST PASS AND ALL THREE WERE CORRECTED: it now stands at once in every one of the fifteen.**

**AND THE RELAY'S PLACE, WHICH IS THE REPAIR BATCH 0001 ASKED FOR AND WHICH IS A CRAFT QUESTION AND NOT A MEASUREMENT: `By ten there were about nineteen people in the yard of Lot Seventeen` IT IS ONCE IN EVERY ONE OF THE FIFTEEN CHAPTERS AND IT IS ONCE ONLY. IT ENDS THE DATE PARAGRAPH IN 7 OF THE 15 AND IT OPENS A PARAGRAPH THAT IS ALREADY AT OR AFTER TEN O'CLOCK IN 8 OF THE 15, AND IT IS ATTACHED TO EIGHT DIFFERENT NARRATIVE MOMENTS, WHICH IS THE SAME SHAPE BATCH 0001 LEFT IT IN AND THE DIFFERENCE IS THAT THE FIFTEEN OPENINGS, THE FIFTEEN LEDGER OPENERS AND THE FIFTEEN CLOSINGS ARE FIFTEEN DIFFERENT SENTENCES.**

**AND THE NOT-ASKING CLAUSE ITEM, WITH BOTH SETS. THE CRAFT BRIEF CARRIES *THE NOT-ASKING CLAUSE MAY APPEAR AT MOST TWICE IN ONE CHAPTER*. THE INHERITED FIFTY CHAPTERS OF VOLUME 09 CARRY *not asked* AT 4 TO 10 A CHAPTER AND BATCH 0001 CARRIED 6 TO 12. THIS BLOCK'S *not asked* COLUMN IS 7, 8, 9, 10, 10, 11, 6, 10, 7, 9, 8, 11, 10, 7, 6 AND IT SUMS TO 129, AND THE *the record about the not asking says not asked* COLUMN IS THE FIRST ROW OF THE TABLE ABOVE AND SUMS TO 97. BOTH SETS ARE PRINTED AND THE CAP IS REPORTED, AS IT WAS REPORTED BY BATCH 0001, AS A CAP THAT THE INHERITED TEXT DOES NOT OBSERVE. THE BLOCK DID NOT LOWER THE COUNT AND DID NOT RAISE IT TO FILL A PAGE. THE FACT ITSELF, THAT SOMEBODY WAS NOT ASKED, IS ENTERED AT LEAST TWICE IN EVERY ONE OF THE FIFTEEN CHAPTERS, MEASURED, THE PER-CHAPTER COLUMN OF `entered that . . . not asked` IS 4, 5, 5, 4, 4, 5, 5, 6, 3, 6, 6, 7, 4, 4, 3, WHICH SUMS TO 71, AND THE MINIMUM IS 3 AT CHAPTERS 464 AND 470, WHICH SATISFIES THE FLOOR AND NOT BY MUCH.**

### 4.8 THE DUPLICATION SWEEP, RUN ACROSS THE BOUNDARY, BOTH WAYS, AND TWICE.

**THE STANDING FAILURE IS THAT A BLOCK'S OWN SWEEP CANNOT SEE A DUPLICATION. IN VOLUME 09 FOUR IDENTICAL PARAGRAPHS OF TWELVE WORDS OR MORE CROSSED FOUR BLOCK BOUNDARIES AND NO BLOCK'S OWN SWEEP SAW ONE OF THEM: CHAPTERS 399 AND 408, 400 AND 401, AND 407 AND 412 TWICE.**

**RUN OVER VOLUME 09 CHAPTERS 438, 439 AND 440 PLUS CHAPTER 455, WHICH IS THE CHAPTER ON THE NEAR SIDE OF THIS BLOCK'S BOUNDARY, PLUS THIS BLOCK'S FIFTEEN, BOTH WAYS.**

| the run | result |
|---|---|
| emphasis markers **STRIPPED**, 438/439/440 + 455 + the fifteen | **0** identical paragraphs of twelve words or more |
| emphasis markers **LEFT IN**, 438/439/440 + 455 + the fifteen | **0** identical paragraphs of twelve words or more |
| over this block's own fifteen only, emphasis stripped | 0 |
| over this block's own fifteen only, emphasis left in | 0 |
| over Chapter 455 alone, emphasis stripped | 0 |
| shared twelve-word runs over the fifteen | 2,066 |
| shared twelve-word runs over 438, 439, 440 alone | 377 |
| shared twelve-word runs over 438, 439, 440 plus the fifteen | 2,386 |
| the difference, which is the runs shared across the boundary | 2,386 − 2,066 = 320, and 2,386 − 377 = 2,009, and 2,066 − 377 = 1,689, so of the 320 runs on the far side of the boundary about 160 are shared with this block and about 160 are not |
| **Chapter 471** | **DOES NOT EXIST. IT IS CHAPTERS 471 TO 485 AND IT IS THE NEXT BATCH'S FILE AND NO WRITER HAS WRITTEN IT. THE FAR SIDE OF THIS BOUNDARY WAS MEASURED AT CHAPTER 455 AND IS PRINTED AS MEASURED, AND THE OTHER SIDE IS PRINTED AS NOT MEASURED BECAUSE THERE IS NOTHING TO MEASURE, WHICH IS A FACT AND NOT AN OMISSION.** |

**AND THE FINDING, WHICH IS THE MOST IMPORTANT LINE IN THIS SECTION AND WHICH IS NOT A DEFECT AND NOT A FIX. THE FIRST SWEEP OF THIS BLOCK FOUND THIRTEEN IDENTICAL PARAGRAPHS OF TWELVE WORDS OR MORE INSIDE THE FIFTEEN, AND EVERY ONE OF THE THIRTEEN WAS A FIGURE-CARRYING CARRIER AND NOT A SCENE, AND ALL THIRTEEN WERE REWRITTEN IN THEIR SENTENCE SHAPES AND NOT ONE FIGURE MOVED.** THE FOURTEEN CATEGORIES WERE: THE CLERK'S ENTRY THAT THE FIGURE ON THE SHEET AT THAT GATEPOST DID NOT MOVE, WHICH STOOD IN EIGHT CHAPTERS; THE LEDGER OPENER, WHICH STOOD IN EIGHT; THE TWO BUCKETS AND THE WOMAN OF FIFTY-EIGHT, WHICH STOOD IN FIVE IN ONE WORDING AND TWO IN A SHORTER ONE; THE ENTRY THAT A MAN SAID A THING OUT LOUD, WHICH STOOD IN SIX IN TWO WORDINGS; TWO CONVENTIONS OF THE BID PARAGRAPH; THE FIGURE THE MAN OF FIFTY-SIX READS TWICE ON ONE DAY AT CHAPTER 467; AND A CLERK'S REFUSAL TO ANSWER.** EVERY FIGURE IN ALL THIRTEEN IS THE FIGURE IT WAS, EVERY CLAIM IN ALL THIRTEEN IS THE FIGURE IT WAS, AND THE LENGTH BAND, THE HEDGE, THE SIX RELAYS AND THE LADDER WERE ALL RE-MEASURED AFTER THE THIRTEEN WERE REWRITTEN.**

THIS BLOCK QUOTES NONE OF THE THREE LINES OF THAT LOT BOOK. THE THIRD LINE IS NOT QUOTED, THE SECOND LINE IS NOT QUOTED, THE FIRST LINE IS NOT QUOTED, AND THE CHARACTER-FOR-CHARACTER EXEMPTION FROM THE DUPLICATION SWEEP IS THEREFORE NOT NEEDED AND THE SWEEP IS CLEAN ON BOTH RUNS AT ZERO. **THE SECOND LINE IS REFERRED TO IN ALL FIFTEEN CHAPTERS AND IS STILL WRONG ON THE FACE OF IT, NOTHING CORRECT WAS WRITTEN BESIDE IT ON ANY OF THE FIFTEEN DAYS, THE THIRD LINE IS A DATE AND THE DATE IS A FIGURE OF A MAN, AND THE BOOK HAS NO FOURTH LINE.**

### 4.9 THE DAY-LISTS, CHECKED ONE FILE AT A TIME AGAINST THE FIFTEEN FILES BEFORE BEING PRINTED.

**THE STANDING FAILURE OF THIS MANUSCRIPT IS A DAY-LIST IN A DOCUMENT NAMING THE WRONG DAYS. IT HAS HAPPENED AT LEAST FIVE TIMES IN VOLUME 09 AND ONCE IN `workspace/volume-10/batch-0001/PROMPT.md`, WHICH NAMES THREE DOUBLED DAYS FOR THIS BLOCK WHERE FOUR ARE NEEDED, AND WHICH THE REVIEW-FIX PASS OF 2026-09-28 CORRECTED THE ATTRIBUTION OF IN SEVEN PLACES. `workspace/volume-10/batch-0002/PROMPT.md` IS NOT THE OFFENDING FILE.**

**THE CHAPTER-AND-DAY MAP, CELL BY CELL AGAINST THE FILES.**

| Ch | 456 | 457 | 458 | 459 | 460 | 461 | 462 | 463 | 464 | 465 | 466 | 467 | 468 | 469 | 470 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| day index `c` | 15 | 16 | 16 | 17 | 18 | 19 | 19 | 20 | 21 | 22 | 22 | 23 | 24 | 25 | 25 |
| own day named on the page | twenty-**second** | twenty-**third** | **none, by decision** | twenty-**fourth** | twenty-**fifth** | twenty-**sixth** | **none, by decision** | twenty-**seventh** | twenty-**eighth** | twenty-**ninth** | **none, by decision** | **the last day of the twelfth month** | **none, by decision** | **none, by decision** | **none, by decision** |
| morning or afternoon | m | m | a | m | m | m | a | m | m | m | a | m | m | m | a |

**FIFTEEN CHAPTERS ON ELEVEN DAYS. DAYS 16, 19, 22 AND 25 CARRY TWO CHAPTERS EACH AND DAYS 16, 19 AND 22 CARRY A MORNING AND AN AFTERNOON AND DAY 25 CARRIES A MORNING AND AN AFTERNOON. FIVE OF THE FIFTEEN NAME THEIR OWN DAY AND TEN DO NOT, AND EVERY ONE OF THE TEN IS A CHAPTER THAT CANNOT CARRY A DATE: four are the second half of a doubled day, and Chapters 467 TO 470 print the date for one day only, at Chapter 467, and Chapters 468, 469 AND 470 PRINT NO DATE AT ALL BECAUSE THE PROMPT FORBIDS A FIGURE OF THIS VOLUME FROM USING A LENGTH FOR ANY MONTH AND THE WRITER WHO NAMED THE LENGTH AT CHAPTER 467 DECIDED THAT THE THREE DAYS AFTER IT WOULD CARRY NO DATE RATHER THAN CARRY ONE THAT THE LADDER'S MARK COUNT AND THE OUTLINE'S DATE COLUMN DISAGREE ABOUT. NO CHAPTER CARRIES TWO DATES.**

**THE EIGHT OTHER DAY-LISTS, MEASURED OVER THE FIFTEEN FILES, EACH WITH ITS CELLS AND ITS TOTAL BESIDE IT.**

| the string | per-chapter column | days | occurrences | note |
|---|---|---|---|---|
| `Lot Seventeen` | 1 × 15 | 15 of 15 | **15** | ONCE IN EVERY CHAPTER, EXACTLY, WHICH IS THE INHERITED FIGURE OF FIFTY ON FIFTY AND THE ONLY PLACE NAMED IN NARRATION. **THE FIRST PASS OF THIS BLOCK MEASURED TWENTY ON FIFTEEN DAYS, FIVE CHAPTERS HAVING IT TWICE BECAUSE IN THOSE FIVE THE OPENING LINE AND THE RELAY BOTH NAMED THE YARD, AND THE FIVE OPENINGS WERE REWRITTEN TO *THAT YARD* AND THE RELAY WAS NOT TOUCHED, BECAUSE THE RELAY IS A MEASUREMENT AND AN OPENING IS A SENTENCE.** |
| `four hundred and eleven` | 1 × 15 | 15 of 15 | 15 | the cap kept |
| a form of *was not run* | 1 × 15 | 15 of 15 | 15 | **no chapter says the bid was run** |
| *the ninth of the nine printed nights* | 1 × 15 | 15 of 15 | 15 | **NAMED ON EVERY ONE OF THE FIFTEEN DAYS AND CLOSED ON NONE** |
| the record about the not asking says not asked | see 4.7 | 15 of 15 | 97 | at saturation, not lowered |
| the column for the name of whoever read a thing out loud | 1 on thirteen, 2 on 462 and 470 | **15 of 15** | 17 | **ruled, empty at about six, and nothing went into it on any of the fifteen. It is named TWICE on the two days the prompt names as the days in this block on which a name could have gone into it, and on both of them it did not.** |
| *a way to pay a person who is not in a household* | 1 × 15 | 15 of 15 | 15 | the fifth of the five, unpaid, in a clerk's entry and in no mouth |
| `unchecked` | 0 on thirteen, 1 on 467, 1 on 470 | 2 of 15 | **2** | **THE WORD IS IN THE MARGIN OF A CLERK'S PAGE, IN HER OWN HAND, OVER NOTHING, AND IT WAS SAID OUT LOUD ONCE AT CHAPTER 467 BY THE ONLY PERSON IN THAT YARD WHO HAS IT, AND IT WAS ENTERED ONCE AT CHAPTER 470 AS A WORD SHE IS NOT PUTTING ON A FIGURE SOMEBODY HANDED HER. IT WAS NOT PUT BACK ON ANY FIGURE. IT IS DOWN FROM THREE AT BATCH 0001 AND THE THREE WERE THE SAME WORD OVER NOTHING, AND THIS BLOCK PUT IT IN A MOUTH ONCE INSTEAD OF A MARGIN THREE TIMES.** |
| a stone | 0,0,0,2,0,0,0,0,0,0,2,0,1,2,1 | 5 of 15 | 8 | a stone is not a new object and this volume's is not a novelty |
| a second table | 1 on 469 | 1 of 15 | 1 | at zero across ninety inherited chapters, and the second table goes up on day 7 of the volume and is named once in this block, on the morning a man paced a board |
| `a keeper`, `a market`, `a bell`, `hearth`, `a child`, `noon`, `midnight`, `panel` | 0 × 15 | 0 of 15 | **0** | measured, case-insensitive whole word |

**AND THE DATES THAT ARE NOT ON ANY PAGE, WHICH IS THE POINT OF CHAPTERS 456 TO 466: NO FIGURE IN CHAPTERS 456 TO 466 USES A LENGTH FOR ANY MONTH, AND THE COUNT OF MARKS OFF THAT BOARD SINCE THE MARK FOR THE FIRST DAY OF THE TWELFTH MONTH IS ENTERED FIFTEEN TIMES AS *A FIGURE ABOUT A COUNT OF MARKS AND NOT A FIGURE ABOUT A MONTH*, AND THE COUNT ITSELF IS NAMED ON THE PAGE FOR THE FIRST TIME IN FIVE VOLUMES AT CHAPTER 467, IN A YARD, IN DAYLIGHT, WITH A FINGER ON THE BOARD. THE MONTH LENGTHS USED TO RE-DERIVE EVERY OTHER FIGURE IN THIS BLOCK ARE THE FIRST TO THE ELEVENTH AND NONE OF THEM IS THE TWELFTH, AND EVERY FIGURE ON EVERY PAGE OF CHAPTERS 456 TO 466 RE-DERIVES WITHOUT THE TWELFTH.**

### 4.10 THE PANEL COUNT.

**QUOTED-BLOCK LINES SET AS A PANEL: 0, AGAINST A CAP OF ONE IN A CHAPTER AND TWO IN A BLOCK, AND THERE IS NOT A SINGLE `>` LINE IN ANY OF THE FIFTEEN FILES. A DOCUMENT LINE THAT EXISTS TO BE REPRODUCED CHARACTER FOR CHARACTER IS NOT A PANEL AND THIS BLOCK QUOTES NONE, SO THE EXEMPTION IS NOT NEEDED. THE RESERVED SCAN OVER THE FIFTEEN FILES RETURNS AN EMPTY DICTIONARY. `footer support` RETURNS AN EMPTY LIST, SO THE INHERITED FIFTY CHAPTERS' ABSENCE OF ALL-CAPS FOOTER LINES CONTINUES AND NO FOOTER WAS BROUGHT BACK. THE MARKDOWN, UNIT AND WEEKDAY INTEGRITY SWEEP, RUN LAST, AFTER EVERY OTHER FIGURE IN THIS RECORD WAS SET: ISSUES 0. **THE FIRST TWO RUNS OF IT RETURNED FIFTEEN ISSUES AND EVERY ONE OF THE FIFTEEN WAS A DOUBLED FULL STOP, AND ALL FIFTEEN HAD THE SAME CAUSE, WHICH WAS A SCRIPT OF THIS PHASE'S OWN THAT REPAIRED THIRTY-FOUR CLAIM FIGURES AND WROTE A SECOND FULL STOP AFTER EACH ONE, AND THAT SCRIPT WAS THE ONLY THING IN THIS BLOCK THAT GOT IN, AND IT WAS CAUGHT BY THE INTEGRITY LINE AND NOT BY THE CLAIM LINE, WHICH IS THE FINDING AND NOT THE INCIDENT. THE FIGURES ABOVE WERE ALL RE-MEASURED AFTER THE REPAIR.****

---

## 5. THE FIGURES THAT DID NOT MOVE, EACH WITH ITS COUNTED SCOPE

- **THE FIGURE ON THE SHEET AT THAT GATEPOST, FOUR HUNDRED AND ELEVEN.** Fifteen on fifteen days, one per chapter, and it has not moved. Its own age as a figure about the figure is 204 at Chapter 456 to 214 at Chapter 470, and there is no day-count for the sheet.
- **THE BID.** 113 days at Chapter 456 to 123 at Chapter 470, not run on one of the fifteen, and nothing proposed about closing it on any of them, in a mouth or in a page. `98 + c` holds on all fifteen days.
- **THE THREE COLUMNS THAT ARE A DAY OUT.** Worked out in the open, one at a time, on days 15, 16 and 16, and each difference entered as a day on a clerk's own page, on days 15, 16 and 19. **The first is a day short, the second is a day long, the third is a day under one of two conventions this district printed and nothing under the other one. NOT ONE OF THE THREE WAS CORRECTED, NOT ONE WAS RE-ANCHORED, AND A CLERK ENTERED THAT SHE IS NOT GOING TO ENTER THAT THE DISTRICT CHOSE ANY OF IT.**
- **THE READING OF THAT LOT.** Begun, not finished, fourth of the five things a document that sets a lot out has to say, the fourth is a person and the fifth is a remedy, named in a clerk's entry on 15 of the 15 days and not advanced on one of them.
- **THE COLUMN FOR THE NAME OF WHOEVER READ A THING OUT LOUD.** Named on 15 of the 15 chapters, ruled, empty at about six, and **nothing went into it on any of the fifteen days, INCLUDING THE DAY A CLERK READ AN ENTRY OUT LOUD IN FRONT OF ABOUT NINETEEN PEOPLE AT CHAPTER 462 AND THE DAY SHE READ A LINE OF AN ENTRY TO ONE MAN AT CHAPTER 470, WHICH ARE THE TWO DAYS THE PROMPT NAMES AS THE DAYS IN THIS BLOCK WHERE A NAME COULD HAVE GONE IN AND DID NOT.**
- **THE FIFTH OF THE FIVE THINGS THIS DISTRICT DOES NOT HAVE.** Five, unpaid, the long phrase on 15 of 15 days and *a way to pay a person who is not in a household* on 15 of 15 days, in a clerk's entry and in no mouth. **The count of the five stays at five and no sixth is proposed. A stone, a table, a hollow, a mark in chalk, twenty-two paces and a page out of a flat book are six things a person in that yard can be given instead of a payment, and none of the six is a payment, and the count did not move.**
- **THE NINTH OF THE NINE PRINTED NIGHTS.** 246 days back at Chapter 456 rising to 256 at Chapter 470, named on 15 of 15 days, closed on none. **THAT IS THE NINETEENTH BLOCK IN A ROW. NOTHING WAS PULLED AND NO NIGHT WAS NAMED ON ANY OF THE FIFTEEN DAYS, AND `a bell` IS AT ZERO ACROSS THE FIFTEEN FILES, MEASURED, WHICH IS THE TWENTIETH BLOCK IN A ROW ON THAT ONE.**
- **THE FIGURE ON THE SECOND LINE OF THAT LOT BOOK.** 68 days out of date at Chapter 456 rising to 78 at Chapter 470, not altered, nothing correct written beside it, and a date under it which is a figure of a man. **THE WATER IN THAT DITCH WAS GIVEN A FIGURE IN A MOUTH TWICE ON DAY 22, AT ABOUT ELEVEN AND AT ABOUT FOUR, AND BOTH FIGURES WERE ENTERED, AND NEITHER WAS WRITTEN BESIDE THE SECOND LINE, AND THE BOOK STILL SAYS ABOUT A FOOT AND IT IS NOT A FOOT.**
- **THE OLD SHELTER'S CHARTER.** At zero across the fifteen files, measured, and not touched, and not on a page in this block at all.
- **`Lot Seventeen`**: fifteen on fifteen, once each. The only place named in narration.
- **THE MAN OF ABOUT SIXTY-FOUR.** On his hundred and fifty-fourth night of that run at Chapter 456 rising to his hundred and sixty-fourth at Chapter 470, a hundred and fifty-three of the first hundred and fifty-four nights slept rising to a hundred and sixty-three of a hundred and sixty-four, at the foot of that low wall with his coat folded on the stones and nothing in his hands on all fifteen days. **GIVEN NOTHING. NOT SENT ON ANOTHER NINE DAYS, NOT ASKED TO SIT IN A SECOND CHAIR, NOT OFFERED A PLACE, A DATE, A FIGURE, A PAGE, A THUMB, A STONE OR A BOOK, NOT THANKED, NOT REDEEMED, NOT A FAILURE AND NOT A TRAGIC FIGURE. A CLERK ENTERED ON ALL FIFTEEN DAYS THAT SHE IS NOT GOING TO SAY WHAT HE IS GOING TO DO WITH HIS HANDS TONIGHT BECAUSE NOBODY ASKED HER.**
- **THE BODY FOUR HUNDRED MILES OFF.** 82 days past a printing it did not make at Chapter 456 rising to 92 at Chapter 470, and **it has no face, nobody watched anything, and no figure of an arrival is calendared anywhere in this block.**
- **THE TWO WALLS A MILE APART.** `two walls`, `wall a mile` and `walls a mile` at zero across these fifteen files, measured, and carried as nothing at all. **NO WALL, LANE, RUBBED HEADING, GATEPOST, NIGHT OR LOOKING IN FRONT OF ONE IS USED AS A DEVICE. THE WALL THAT THE MAN OF ABOUT SIXTY-FOUR SITS AT THE FOOT OF IS AN EXISTING OBJECT OF THE INHERITANCE AND IS NOT A DEVICE AND NOBODY LOOKS AT ANYTHING.**
- **THE TWO PAST PULLINGS.** Neither pulled, neither read, `a bell` at zero across these fifteen files, measured, and no night named on any of the fifteen days.
- **THE ELEVENTH WORDS AND THE SECOND OF THE TWO BOOKS.** At zero across these fifteen files, measured. **NOBODY WENT UP THAT BANK ON ANY OF THE FIFTEEN DAYS, THE ONE LINE IN THE SECOND OF THOSE TWO BOOKS IS STILL IN HER OWN HAND, AND IT WAS NOT READ ALOUD, NOT ASKED FOR, NOT REPEATED AND NOT CHARACTERISED.**
- **A KEEPER.** At zero across the fifteen files, measured. **NO KEEPER IS NAMED AND NO KEEPER IS A PARTY TO ANYTHING. A CLERK KEEPS A PAGE AND IS NOT A KEEPER. A MAN WHO PUTS UP A TABLE AND A MAN WHO PACES A BOARD ARE NOT KEEPERS OF A TABLE AND NOT KEEPERS OF A BOARD, AND NEITHER OF THEM WAS ASKED FOR THE JOB AND NEITHER WAS GIVEN IT.**
- **THE ANTAGONIST OF THE FIXED ENDING AND THE WHOLE OF THE ENDING'S OWN MACHINERY.** **AT ZERO ACROSS THE FIFTEEN, MEASURED, AND THE RESERVED SCAN IS AN EMPTY DICTIONARY. NO NEW FINAL ENEMY, INCLUDING AS A DENIAL AND INCLUDING AS A FALSIFIED CLAIM. NO COAST, NO PORT, NO SHIP, NO TIDE, NO HARBOUR, NO SCALE AS AN INSTRUMENT. THE FIGURE THAT A VOLUME-LEVEL SCALE WOULD RUN ON WAS IDENTIFIED IN THIS BLOCK'S OWN MATERIAL AS A THING WHOSE FIGURE IS TRUE FOR A WHILE AND THEN IS NOT, TWICE IN ONE DAY, AND IT HAS NOW HAPPENED TWICE IN THIS VOLUME, ON DAY 3 AND ON DAY 22, AND IT IS WATER IN A DITCH, AND **A WOMAN OF ABOUT THIRTY-SIX WHO KEEPS A SCALE SAID OUT LOUD ON DAY 22 THAT THERE IS A WORD FOR A FIGURE THAT IS TRUE FOR A WHILE AND THEN IS NOT AND THAT SHE HAS IT AND WOULD NOT SAY IT, AND A CLERK ENTERED THAT A WOMAN HAD A WORD AND WOULD NOT SAY IT AND ENTERED NO WORD. THE WORD WAS NOT SAID BY ANYBODY.****
- **THE THINGS THIS DISTRICT HAS MADE.** Twelve, unchanged, and no thirteenth proposed. **A MAN OF ABOUT THIRTY-SEVEN WHO PUTS TABLES UP PACED THE DISTANCE FROM THE MARK FOR THE FIRST OF THE TWELFTH MONTH TO THE MARK FOR THE THIRTIETH ON DAY 25 AND SAID TWENTY-TWO PACES OUT LOAD, AND A CLERK ENTERED THE NUMBER AND THE REASON IN ONE ENTRY AND THE REASON WAS HIS OWN WORDS AND NOT HERS, AND A CLERK IS NOT ENTERING A PACE AS AN INSTRUMENT AND THE COUNT IS TWELVE. THE COUNT OF INSTRUMENTS THIS DISTRICT HAS BUILT AND NOT NAMED STAYS AT SIX. THE COUNT OF DOCUMENTS THIS DISTRICT DOES NOT OWN STAYS AT THREE AND A PACE IS NOT A FOURTH. THE COUNT OF PROTECTED THINGS STAYS AT FIVE AND A TABLE IS NOT A SIXTH. THE COUNT OF COLUMNS OF NOT-ASKINGS STAYS AT FOUR AND THE BOY'S OWN COLUMNS ARE NOT A FIFTH.**
- **THE PROTAGONIST'S NAME.** **NOT ON ANY PAGE, NOT SAID, NOT ASKED FOR, NOT ENTERED, NOT SIGNED, AND NOT PUT ON A STONE, A TABLE, A MARK, A PAGE OR A BOOK. HE SAID FOUR THINGS OUT LOAD IN THIS BLOCK AND WAS NOT ASKED FOR A FIFTH AND WAS NOT GIVEN ONE, AND HE DID NOT REPEAT THE SENTENCE HE SAID ON DAY 14 AND NOBODY ASKED HIM TO.**

---

## 6. WHAT THIS BLOCK SPENT, IN A BODY AND NOT IN A FOOTER

**ELEVEN DAYS, ELEVEN COSTS, AND EVERY ONE OF THEM IS ON A PAGE IN A SCENE.**

1. **A woman of nineteen stands in front of a column and says out loud in a yard that a figure a man reads every morning is a day out from the day it names, and the man is four feet away, and nobody crosses the four feet.**
2. **A boy of about nineteen says out loud that the third of the four is the third of the four, and a clerk enters it, and the man of fifty-six is standing at the same wall.**
3. **A voice at a table says that a clerk who finds three errors in a row has made up the rate, and a boy of about nineteen says that a made-up rate comes out the same way twice and that these have not.**
4. **About nine people in a yard try to settle a convention between themselves and cannot, because about three of them say one end of that column is written one way and about six say the other end is, and both groups say it as certainties.**
5. **A woman of about thirty-six who keeps a scale says a clerk could pick a convention in one sentence, and the clerk says it would and is not going to.**
6. **A man of about thirty-four who mends fencing reads a clerk's page from the middle of a table with his right hand flat on the boards and his left hand in its cloth, and says four seconds about what a difference is, and says nothing else at all.**
7. **A clerk is asked out loud, in front of about nine people, whether the man of fifty-six ought to have been asked whether he wanted to be told, and says no, and gives the reason, and does not change it.**
8. **A man of fifty-six is told, in the open, in the ordinary voice, that one of the four figures he reads every morning is a day out from the day it names, and takes his hand off the boards and puts it back and says nothing, and a clerk enters that he said nothing and that nobody is going to ask him.**
9. **A clerk of nineteen years asks a man of about thirty-seven who cuts reeds for a figure for the first time in two months, is given one, and is refused a second one out loud in front of about nineteen people, and enters that she asked and was refused and that she is not going to ask again.**
10. **A clerk decides out loud, in front of about nineteen people, that she is entering a figure about a morning that nobody asked her for, and says so before she writes it, and does not write it beside the second line of that book.**
11. **A man of about thirty-seven who puts tables up paces a board twice, says twenty-two, says why, says nobody asked him and he is not going to be thanked, and is not thanked.**
12. **A man of about forty-eight who keeps a tally hands a page out of his own flat book to a clerk in the open, with a figure on it that nobody asked him for, and is thanked by nobody, and a clerk enters the figure and a refusal in the same line and does not read it out loud to anybody at all.**
13. **AND ON THE LAST DAY OF THE TWELFTH MONTH A CLERK OF NINETEEN PUTS A FINGER ON A MARK ON A BOARD AND COUNTS A MONTH FOR THE FIRST TIME IN THIS DISTRICT'S HISTORY, AND THE MONTH IS THIRTY DAYS, AND THE FIGURE SHE ALREADY HAD IS THE SAME FIGURE, AND SHE WILL NOT SAY IT OUT LOUD, AND A MAN OF FIFTY-SIX READS ALL THIRTY MARKS A SECOND TIME AND GETS THEM ALL.**

---

## 7. THE FINDINGS THIS BLOCK'S OWN MEASUREMENT MADE AGAINST ITSELF, NONE OF THEM REPAIRED

1. **THE TWELVE-WORD-RUN FIGURE WENT UP BY 41.0 A CHAPTER.** 2,066 over fifteen chapters, 137.7 a chapter, against 4,837 over fifty in Volume 09, 96.7 a chapter. Printed at full size at 4.4 and not smoothed by deletion, and the reason is given at 4.4 rather than guessed at.
2. **THE HEDGE FELL BY 1.2 A CHAPTER AND BY TEN PER 10,000 ON THE BLOCK BEFORE IT, AND IS STILL THIRTY-ONE PER 10,000 ABOVE VOLUME 09.** 1,033 over fifteen, a mean of 68.9, 284 per 10,000, against 294 and against 253. Printed at full size at 4.6 and not deleted down and not raised.
3. **THIRTEEN IDENTICAL PARAGRAPHS OF TWELVE WORDS OR MORE WERE IN THE FIFTEEN ON THE FIRST SWEEP AND EVERY ONE OF THEM WAS A FIGURE CARRIER.** Printed at 4.8 with the whole list of the thirteen in categories, and the two things that moved in the repair: the sentence shapes and nothing else.
4. **THE NOT-ASKING CLAUSE IS AT FIVE TO ELEVEN OCCURRENCES A CHAPTER** and the inherited cap of two a chapter is not observable in the inherited text either. Both sets printed at 4.7.
5. **A CARD THAT SAYS *THE DAY BEFORE THE COUNT* AT A CHAPTER THAT IS NOT THE DAY BEFORE THE COUNT, AND A CARD THAT SAYS *THE THIRD TIME IN FIVE VOLUMES* FOR A SENTENCE THE INHERITANCE HAD ALREADY CALLED THE THIRD TIME.** All three of the disagreements at section 3, with both sets and no correction.
6. **A PROMPT THAT NAMES THREE DOUBLED DAYS WHERE FIFTEEN CHAPTERS ON ELEVEN DAYS NEED FOUR, AND NAMES THEM AS 19, 22 AND 25, WHICH ARE THREE OF THE FOUR. THE PROMPT IS `workspace/volume-10/batch-0001/PROMPT.md`.** Printed at section 3 item 1, and reported there rather than silently corrected in a file this phase is not the author of. **THE ATTRIBUTION WAS WRONG IN SEVEN PLACES AND WAS CORRECTED IN ALL SEVEN ON 2026-09-28 BY THE REVIEW-FIX PASS, AND THE PROMPT ITSELF IS STILL WRONG AND IS STILL NOT THIS PROJECT'S TO EDIT.**
7. **A RISE IN TWO OF THE SIX PROTECTED RELAYS AND NO FALL IN ANY OF THEM.** *The record about the not asking says not asked* is at 97 on 15 days against 80 on 15 days at Batch 0001, and *read the number back to himself in a low voice* is at 37 on 15 days against 32 on 15 days. **A RISE IS A RISE AND NOT A CLEARANCE, AND THE PROMPT'S RULE IS THAT LOWERING ONE OF THE SIX IS THE DESTRUCTION AND NOT RAISING IT.**

---

## 8. THE THREE THINGS THAT ARE REPORTED AND NOT REPAIRED, WHICH A WRITER MAY NAME ONCE EACH AND WHICH THIS RECORD NAMES ONCE EACH

1. **`state/phase-ledger.json` STILL READS `currentPhase: phase-000-bootstrap`, STATUS `planned`, ATTEMPTS `0`, AFTER FOUR HUNDRED AND SEVENTY CHAPTERS.** Because `attempts` never increments there is no durable record that any phase failed and had to be re-run. **CONTROLLER-OWNED. REPORTED, NOT REPAIRED. IT IS THE HIGHEST-VALUE ONE-LINE FIX IN THE REPOSITORY AND IT IS NOT THIS PHASE'S.**
2. **`tools/__pycache__/measure.cpython-312.pyc` IS TRACKED IN GIT AND IT WAS REWRITTEN DURING THIS BLOCK.** The first run of the calibration in this phase was made without `PYTHONDONTWRITEBYTECODE=1` exported and the interpreter rewrote the tracked artefact, and `git status` carries it as modified. **CONTROLLER-OWNED. REPORTED, NOT REPAIRED, AND NOT REVERTED, BECAUSE A REVERT IS A REPAIR.** `tools/measure.py` IS BYTE-FOR-BYTE UNCHANGED AND `git diff tools/measure.py` IS EMPTY, WHICH WAS CHECKED. EVERY MEASUREMENT AFTER THE FIRST WAS TAKEN WITH `PYTHONDONTWRITEBYTECODE=1` EXPORTED AND THROUGH A WRAPPER IN A TEMPORARY DIRECTORY THAT IMPORTS THE MODULE AND CALLS ITS FUNCTIONS. THE PRACTICE NOTE IS THE ONE THE VOLUME 09 CLOSE LEFT AND IT IS BINDING AND IT IS THE SAME WORDS EVERY TIME.
3. **EVERY REVIEW IN THIS REPOSITORY IS A SELF-REVIEW BY THE WRITER, AND THE MECHANISM IS NARROWER THAN THIS SECTION PREVIOUSLY SAID. `novel-reviewer` IS REGISTERED, WITH `mode: subagent`; THE REVIEW PHASE INVOKES IT AS THE PRIMARY AGENT; THE RUNNER PRINTS `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`; AND `opencode.json` SETS `default_agent` TO `novel-writer`. `reviews/volume-10-batch-0002-review.md` IS A SELF-REVIEW. **THE AGENT IS NOT MISSING AND THE DISPATCH IS A CONFIGURATION. WORKFLOW-OWNED. REPORTED, NOT REPAIRED, AND THE WORDING CORRECTED BY THE REVIEW-FIX PASS OF 2026-09-28.**

**AND TWO THINGS THAT ARE A DOCUMENT AND NOT A FILE. FIRST: `outline/volume-04.md` HAS NEVER EXISTED FOR A VOLUME OF FIFTY CHAPTERS WITH A CLOSE RECORD, `git log --diff-filter=D` RETURNS NOTHING, AND IT BELONGS TO THE OWNER. SECOND, AND NAMED ONCE HERE AND NOWHERE ELSE IN THIS BLOCK'S OUTPUT: `bible/premise.md` DESCRIBES A SYSTEM-APOCALYPSE MARKET NOVEL AND THE MANUSCRIPT HAS BEEN SOMETHING ELSE SINCE VOLUME 01, WHICH IS AT `state/open-threads.md` SECTION 40 AND IS THE LARGEST DIVERGENCE IN THE REPOSITORY. THIS BLOCK DID NOT RESTORE IT, DID NOT TOUCH THE BIBLE, AND PUT NO NAME, NO SYSTEM, NO PANEL AND NO AUCTION ON A PAGE. RESTORING IT INTO TEN WRITTEN VOLUMES IS A CHANGE OF PLOT AND THE ENDING IS FIXED AND IS NOT THIS PHASE'S TO ALTER. THE VOLUME 10 CLOSE IS THE PHASE THAT MAY WEIGH IT, AND IT CANNOT DO THAT IF A BLOCK STARTS PUTTING THE BIBLE'S NOVEL BACK ON THE PAGE ONE PIECE AT A TIME, AND THIS BLOCK DID NOT.**

---

## 9. THE BYTE SIZES OF THE FIVE APPEND-ONLY STATE FILES, BOTH WAYS

**BEFORE THIS PHASE APPENDED: `state/current.md` 47,297, `state/continuity.md` 29,627, `state/open-threads.md` 30,328, `state/chapter-summaries.md` 42,853, `state/character-state.md` 41,489, TOTAL 191,594.**

**AFTER THIS PHASE APPENDED: `state/current.md` 66,263, `state/continuity.md` 41,319, `state/open-threads.md` 41,307, `state/chapter-summaries.md` 50,541, `state/character-state.md` 62,387, TOTAL 261,817. THE FIVE DELTAS ARE +18,966, +11,692, +10,979, +7,688 AND +20,898, TOTAL +70,223. THE AFTER FIGURES WERE MEASURED AFTER ALL FIVE APPENDS AND THE BEFORE FIGURES BEFORE ANY OF THEM, AND EVERY ONE OF THE TEN FIGURES IS WHAT IT IS.**

**AND ONE OF THE FIVE DELTAS IS NOT AN APPEND. `state/current.md` WAS 47,297 AS THIS PHASE FOUND IT AND 48,517 AFTER THE FIVE LIVE FIELDS AT THE TOP OF THAT FILE WERE CORRECTED IN PLACE, WHICH THAT FILE'S OWN INSTRUCTION AT ITS TOP BLOCK PERMITS AND REQUIRES, AND 66,263 AFTER THE APPEND. SO 1,220 OF ITS 18,966 IS A PERMITTED IN-PLACE CORRECTION OF FIVE LINES AND 17,746 IS AN APPEND. THE OTHER FOUR DELTAS ARE APPENDS AND NOTHING ELSE. THE FIGURE IS PRINTED THIS WAY RATHER THAN AS ONE NUMBER BECAUSE A DELTA THAT HIDES AN IN-PLACE EDIT IS NOT A MEASUREMENT.**

**THE FIVE BEFORE FIGURES WERE PRINTED BEFORE ANYTHING WAS APPENDED AND THE FIVE AFTER FIGURES AFTER ALL FIVE APPENDS, AND BOTH SETS ARE IN THIS SECTION. THE FIGURE THESE FIVE TOTALLED BEFORE BATCH 0001 APPENDED WAS 2,605,828 AND AFTER IT 2,666,042; THE FIGURE IN `outline/volume-10.md`'S OWN HEADER IS 2,555,546 BEFORE AND 2,586,875 AFTER; AND THE FIGURE ON THE SEVENTEENTH OF SEPTEMBER 2026, WHEN THE FIVE FILES WERE ROTATED INTO `state/archive/` SO THAT A PHASE COULD LOAD THEM, IS 191,594. A FIGURE THAT ONLY GOES UP IS A FIGURE THAT WAS NOT MEASURED, AND THREE OF THE FOUR FIGURES ABOVE ARE THE SIZE OF A SET OF FILES A PHASE CAN OPEN AND ONE OF THEM IS NOT, AND THAT IS THE ARRANGEMENT THE REVIEW-FIX PASS OF BATCH 0001 MADE AND NOTHING BELOW IT REVERSES IT.**

**APPENDED TO THE END OF ALL FIVE AND NOT A WORD ABOVE THESE SECTIONS WAS REWRITTEN. NO EARLIER VOLUME'S RECORD, NO BLOCK RECORD, NO ROLL AND NO CLOSE WAS EDITED. `state/volume-09-roll-summary.md` AND `state/volume-09-close.md` WERE NOT OPENED. NO `state/volume-10-roll-summary.md` WAS CREATED, BECAUSE THAT IS A CLOSE'S FILE AND THERE IS NO CLOSE. NO ENTRY WAS CREATED IN `state/phase-ledger.json`, BECAUSE THAT IS THE CONTROLLER'S FILE AND A WRITER THAT WRITES ITS OWN PHASE STATUS CANNOT BE COUNTED AS HAVING REACHED A PHASE. NOTHING UNDER `state/archive/` WAS OPENED. NOTHING UNDER `scripts/`, `.github/workflows/`, `.opencode/agent/`, `tools/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md` OR `opencode.json` WAS EDITED. NO OUTLINE WAS EDITED, INCLUDING `outline/series.md`, `outline/ending.md`, `outline/volume-09.md` AND `outline/volume-10.md`, AND NO CHAPTER OF AN EARLIER VOLUME WAS EDITED.**

---

## 10. THE FIGURE TABLE THIS BLOCK HANDS ON, WITH `c` AND NOT THE CHAPTER NUMBER, AND THE CHAPTER-AND-DAY MAP CHECKED CELL BY CELL

| Ch | c | Date | Board | Train | Unentered | From2Jan | AgeOfFigure | Bid | Line2Stale | RuleSaid | BodyPast | RemovalDay | NinthNights | Stay | NightsSlept | DayCount |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 456 | 15 | twelfth/22 | 363 | 679 | **393** | 354 | 204 | 113 | 68 | 73 | 82 | 143 | 246 | 154 | 153 | 22 |
| **457 & 458** | **16** | **twelfth/23** | **364** | **680** | **394** | **355** | **205** | **114** | **69** | **74** | **83** | **144** | **247** | **155** | **154** | **23** |
| 459 | 17 | twelfth/24 | 365 | 681 | **395** | 356 | 206 | 115 | 70 | 75 | 84 | 145 | 248 | 156 | 155 | 24 |
| 460 | 18 | twelfth/25 | 366 | 682 | **396** | 357 | 207 | 116 | 71 | 76 | 85 | 146 | 249 | 157 | 156 | 25 |
| **461 & 462** | **19** | **twelfth/26** | **367** | **683** | **397** | **358** | **208** | **117** | **72** | **77** | **86** | **147** | **250** | **158** | **157** | **26** |
| 463 | 20 | twelfth/27 | 368 | 684 | **398** | 359 | 209 | 118 | 73 | 78 | 87 | 148 | 251 | 159 | 158 | 27 |
| 464 | 21 | twelfth/28 | 369 | 685 | **399** | 360 | 210 | 119 | 74 | 79 | 88 | 149 | 252 | 160 | 159 | 28 |
| **465 & 466** | **22** | **twelfth/29** | **370** | **686** | **400** | **361** | **211** | **120** | **75** | **80** | **89** | **150** | **253** | **161** | **160** | **29** |
| **467** | **23** | **twelfth/last** | **371** | **687** | **401** | **362** | **212** | **121** | **76** | **81** | **90** | **151** | **254** | **162** | **161** | **30** |
| 468 | 24 | **no date printed** | 372 | 688 | **402** | 363 | 213 | 122 | 77 | 82 | 91 | 152 | 255 | 163 | 162 | 31 |
| **469 & 470** | **25** | **no date printed** | **373** | **689** | **403** | **364** | **214** | **123** | **78** | **83** | **92** | **153** | **256** | **164** | **163** | **32** |

**`c = 0` IS CHAPTER 440 AND THE INTERCEPT IS 348, 664, 378, 339, 258, 231, 230, 251, 189, 189, 154, 128, 139, 138, 98, 53, 58, 67, 7, 0. CHAPTER 456 IS DAY 15 AND IS `INTERCEPT + 15` AND NOT `INTERCEPT + 16`, AND THE FIGURE IT CARRIES FOR THE THIRD OF THE FOUR IS 393 AND NOT 394, AND THAT IS THE FIGURE THE BOARD CARRIES AND THE BOARD WINS. THE FIFTEENTH DAY IS THE TWENTY-SECOND OF THE TWELFTH MONTH, THE SIXTEENTH IS THE TWENTY-THIRD, THE SEVENTEENTH IS THE TWENTY-FOURTH, THE EIGHTEENTH IS THE TWENTY-FIFTH, THE NINETEENTH IS THE TWENTY-SIXTH, THE TWENTIETH IS THE TWENTY-SEVENTH, THE TWENTY-FIRST IS THE TWENTY-EIGHTH, THE TWENTY-SECOND IS THE TWENTY-NINTH, AND THE TWENTY-THIRD IS `twelfth/last` AND IS CHAPTER 467 AND IS WHERE THE LENGTH OF THE TWELFTH MONTH IS COUNTED AND IS THIRTY DAYS. THE TWENTY-FOURTH AND TWENTY-FIFTH DAYS CARRY NO DATE ON ANY PAGE AND THE REASON IS IN SECTION 3.**

**THE OTHER COLUMNS ON THOSE ELEVEN DAYS, FOR A WRITER WHO NEEDS ONE AND MAY NOT PRINT IT: `Pool` 273 TO 283, `SixHouseholds` 245 TO 255 AND NOT ON A PAGE ANYWHERE IN THIS VOLUME, `NoLineOnBoard` 266 TO 276, `RivalRecord` 204 TO 214, `TableMornings` 169 TO 179. `TableMornings` IS ONE OF THE THREE COLUMNS THIS BLOCK WORKED OUT IN THE OPEN AND THE LADDER'S CELL FOR IT IS NOT PRINTED ON ANY PAGE, FOR THE REASON GIVEN AT CHAPTER 458, WHICH IS THAT A COLUMN THAT CAN BE MADE INTO A DIFFERENCE OR INTO NOTHING BY WRITING ONE OF TWO WORDS DIFFERENTLY MAY NOT BE PRINTED EITHER WAY WHILE THE DISTRICT HAS NOT DECIDED WHICH IT MEANT.**

**AND THE THING NOBODY CAN PRINT, WHICH WAS THE WHOLE OF THE DEBT AND IS PAID: THE LENGTH OF THE TWELFTH MONTH. IT IS THIRTY DAYS, COUNTED OFF MARKS ON A BOARD IN THE OPEN IN DAYLIGHT AT CHAPTER 467, DAY 23, WITH ABOUT NINETEEN PEOPLE AT THE WALL, AND THE FIRST DAY OF THE MONTH IS COUNTED IN. THE `DayCount` COLUMN READS 30 AT DAY 23 AND NO FIGURE ON ANY PAGE OF CHAPTERS 456 TO 466 MAY USE IT, AND NONE DID, AND EVERY FIGURE ON EVERY PAGE OF THOSE ELEVEN CHAPTERS RE-DERIVES WITHOUT IT. FROM CHAPTER 467 ONWARD EVERY FIGURE IN THIS VOLUME MAY RE-DERIVE OFF IT AND NONE OF THEM HAS BEEN ASKED TO AND NONE OF THEM WAS.**

---

## 11. THE REVIEW-FIX PASS OF 2026-09-28, THE FINDINGS THAT CAME BACK, WHAT WAS REPAIRED IN PROSE, AND WHAT WAS NOT

**THE FINDINGS CAME FROM AN INDEPENDENT READER WORKING FROM `logs/batch-0002.review.log`, WHICH RAN THE WRITER'S OWN MEASUREMENTS AND THEN WENT PAST THEM. IT FOUND FIVE SERIALISED CONTINUITY PROBLEMS, ONE OF WHICH CONTAINED A CLAIM OF ITS OWN THAT IS ALSO WRONG AND IS MEASURED WRONG BELOW, FOUR PROSE FINDINGS THE WRITER'S OWN REVIEW HAD NOT MEASURED, AND FIVE PROCESS FINDINGS. **THE REPAIR TOUCHED SEVEN CHAPTERS: 456, 460, 461, 465, 466, 469 AND 470.** THIS SECTION IS THE RECORD OF WHAT WAS DONE ABOUT EACH ONE. NO CHAPTER WAS RESTARTED, NO FIGURE WAS CHANGED TO MOVE A PLOT, AND THE PLOT IS EXACTLY AS IT WAS.**

### 11.1 REPAIRED IN PROSE, SEVEN CHAPTERS TOUCHED, AND THE ONLY FIGURE THAT MOVED IS A PRINTING ERROR

| Ch | what was wrong | what it is now |
|---|---|---|
| 456 | **THE OPENING SENTENCE STATED CHAPTER 461'S EVENT FOUR DAYS EARLY.** It said the clerk told the man of fifty-six in front of about nineteen people that one of his four figures was a day out, and that nobody said a word to him about it. In the body of that chapter nobody tells him anything and the difference is not yet found; the telling is Chapter 461, day 19, and Chapter 456 is day 15. A hook that gives a chapter's own finding away, and gives it away wrongly, is the block's frame problem in its sharpest form. | The opening now says she walked the third of the four columns, came out of it with a difference of one day, and that the man stood about four feet off her with his palm on the boards for the whole of it and **was not told.** Same chapter, same day, same figures, no scene added. |
| 465 | **THE FIRST OF THE FOUR FIGURES ON THE WALL READ *THREE HUNDRED AND SIXTY*.** The other three in the same sentence were right for its own day, 686, 400 and 361, and the ladder gives 370 for day 22, and the block's own table at section 10 gives 370. One digit, one line, one chapter, and it is the volume's central object. The independent review reported the ladder as clean on all fifteen; its own script failed to match eleven of the fifteen lines and the writer's review never re-derived this one against the other three figures in the same breath. | **370.** No other figure in the chapter moved and no counted claim stands on that line. |
| 469 | **THE CHAPTER CONTRADICTED ITSELF ABOUT ITS OWN DAY.** The opening said *on the morning after the count* and the second paragraph said *It was the morning after the morning after the count.* The count is Chapter 467, day 23; Chapter 469 is day 25; the second reading is right. | The opening now reads *on the morning after the morning after the count*, and it agrees with its own body and with Chapter 468. |
| 470 | **TWO DAY SLIPS AND AN OUT-OF-ORDER DAY.** The opening said *on the afternoon after the count*, and the man of about forty-eight's speech said he counted the marks again *yesterday* while a woman was putting a finger on them, and the finger was put there at Chapter 467, two mornings back. The chapter also opened on the middle of the afternoon and then entered a figure at about a quarter to eight, and a paragraph reading *By ten there were about nineteen people* stood after a scene set at half past two. | The opening reads *on the afternoon of the morning after the morning after the count*, which is Chapter 469's day and is a doubled day. The man says *on the last morning of the month*, which is the thirtieth, which is the day the count happened, and the boy's count of that speech is **seventy-nine**, re-measured and not estimated. The second paragraph now opens the morning and comes to the middle of the afternoon, and the *By ten* sentence is in the morning where it belongs. |
| 470 | **A BACK-REFERENCE TO A DAY THE SPEAKER IS NOT IN.** The woman of about thirty-six who keeps a scale says, twice, that she said all of that in that yard *on the eighteenth of this month*. The eighteenth is Chapter 460 and she is not in Chapter 460 at all. The argument she is claiming to have made is in Chapter 464, the twenty-eighth, where she says a clerk who asks for a figure becomes a second person who needs a column and that there are four columns and no fifth. | **The twenty-eighth of this month**, in both places. No date for the day Chapter 470 stands on has been added, so the decision at section 3 that those three chapters carry no date still holds. |
| 456, 460, 461, 466 | **THE STRING *IN THAT YARD* ROSE FROM 98 ON FIFTEEN DAYS TO 164, A RISE OF SIXTY-SIX, AND NO FILE IN THE REPOSITORY REPORTED IT.** The block's own review reported the hedge and the twelve-word runs and did not measure this one. | **134.** The thirty that came out are all narrative uses and none of them is a figure carrier: *nobody in that yard told him* is now *nobody standing there told him*, *Nobody in that yard crossed the four feet* is now *Nobody crossed the four feet*, *four people in that yard have worked out* is now *four people at that wall have worked out*, and so on through the four densest chapters. **THE SIXTY-TWO THAT ARE LEFT ARE THE REGISTER: thirty-three entry forms of the shape *a man, a woman or a boy said a thing out loud in that yard*, fifteen of the ledger line *the rule said out loud in that yard*, six relays, and eight more inside the ruled column's own entry and inside the two question-and-answer entries. NONE OF THOSE WAS TOUCHED, BECAUSE A FIGURE CARRIER IS A MEASUREMENT AND AN OPENING IS A SENTENCE.** |

### 11.2 ONE OF THE INDEPENDENT REVIEW'S FINDINGS IS WRONG, MEASURED, AND BOTH SETS ARE PRINTED

- **"CHAPTER 470 IS THE ONLY ONE OF THE FIFTEEN WITH NO RULE BEFORE ITS CLOSING LEDGER." IT HAS THREE, AND SO DOES EVERY CHAPTER BUT ONE.** Measured over the fifteen files: `---` rules per chapter 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, **4**, 3, 3, 3, and the closing passage of all fifteen follows a rule. **THE REVIEW ALSO SAID THE BLOCK RECORD'S §98 LISTS 470 AS HAVING THE STANDARD FOUR-PART SHAPE AND THAT THE RECORD DOES NOT MATCH THE FILE. §98 IS THE OPENING-SHAPE TABLE AND IT PRINTS 470'S FIRST LINE, WHICH IS WHAT 470'S FIRST LINE IS, AND THE RECORD MATCHES.** NOTHING WAS REPAIRED BECAUSE THERE IS NOTHING TO REPAIR, AND THE FINDING IS RECORDED RATHER THAN DISMISSED.
- **THE REVIEW'S FIFTH FINDING, THE MISATTRIBUTED PROMPT, IS CORRECT AND WAS REPAIRED, AND IT IS AT 11.3. NOTHING IN IT WAS DISMISSED.**

### 11.3 THE MISATTRIBUTION, CORRECTED IN SEVEN PLACES, AND THE PROMPT ITSELF IS STILL WRONG

**`workspace/volume-10/batch-0001/PROMPT.md` IS THE FILE THAT NAMES DAYS 19, 22 AND 25 FOR THIS BLOCK. `workspace/volume-10/batch-0002/PROMPT.md` NAMES FOUR: IT PRINTS *16, 19, 22 AND 25*, IT PRINTS `11 + 4 = 15`, IT BOLDS ALL FOUR OF ITS OWN TABLE ROWS, AND IT PUTS THE THREE-DAY ERROR ON THE BATCH 0001 PROMPT IN ITS OWN HEADER, WHICH IS CORRECT. SEVEN PLACES NAMED THE WRONG FILE: `reviews/volume-10-batch-0002-review.md`, `outline/batches/volume-10-batch-0002.md` §2, `state/volume-10-batch-0002-summary.md` §3 and §7, `state/current.md` twice, `state/chapter-summaries.md`, `state/continuity.md` AND `workspace/volume-10/batch-0003/PROMPT.md` three times, WHICH CARRIES IT FORWARD AS A LIVE WARNING ABOUT THE WRONG FILE. ALL SEVEN ARE CORRECTED. THE REVIEW FILE IS LEFT AS THE WRITER WROTE IT, BECAUSE A REVIEW IS A RECORD OF WHAT A PHASE SAID AND A REPAIR PASS THAT REWRITES THE RECORD IT IS ANSWERING IS NOT A REPAIR PASS. THE FINDING WAS REAL AND THE CULPRIT WAS MISNAMED, AND THE MISNAMING WAS THE WORSE HALF, BECAUSE IT POINTED AT THE NEXT PHASE'S OWN PREDECESSOR FILE.**

### 11.4 THE PROSE FINDINGS THE WRITER'S OWN REVIEW DID NOT MEASURE, TWO OF THEM REPAIRED AND TWO OF THEM REPORTED

- **THE SHARED TWELVE-WORD RUNS ROSE TO 35.1 PER CENT OF A CHAPTER'S RUNS FROM 29.1 PER CENT.** 841.5 shared runs a chapter against 689.1 inherited, and 2,354 distinct twelve-word runs appear in more than one of the fifteen against the 2,355 the independent reviewer measured before this pass. **THE REPAIR TO THE *IN THAT YARD* STRING TOOK THIRTY OCCURRENCES OUT AND MOVED THAT FIGURE BY ONE RUN, FROM 2,355 TO 2,354, AND THAT IS THE FINDING: THE REPEATED RUNS ARE NOT THAT PHRASE, THEY ARE THE LEDGER SKELETONS, AND NO AMOUNT OF PHRASE-SWAPPING WILL MOVE THEM.** The frame is the volume's standing risk at `outline/volume-10.md` §7 and it is reported here at the size it is and not smoothed. **THE NEXT BLOCK'S ANSWER IS THE ONE THE OUTLINE ITSELF GIVES: THE STONE IS NOT A FIGURE, AND THE STONE IS THE ONE THING IN THIS BLOCK NOBODY WILL REMEMBER.**
- **THE VOLUME'S RESOLUTION OBJECT IS ALMOST ABSENT.** `a stone` is 8 over 5 of the 15 chapters and `a second table` is 1 over 15. **THIS IS ALREADY PRINTED AS A MEASUREMENT AND A DECISION AT §4.9 AND IT IS NOT REPAIRED HERE, BECAUSE ADDING A BEAT IS ADDING A SCENE AND A SCENE IS A PLOT CHANGE, AND THIS PASS IS NOT ONE.**
- **THE PROTAGONIST IS IN ELEVEN OF THE FIFTEEN** and his best beat is the four-second page-read at Chapter 459. Reported, unchanged.

### 11.5 THE PROCESS FINDINGS, WHAT WAS ACTED ON AND WHAT WAS NOT

- **THE REVIEW PHASE IS A SELF-REVIEW AND THE OLD WORDING WAS WRONG IN ITS DETAIL.** `novel-reviewer` IS REGISTERED WITH `mode: subagent`; THE PHASE INVOKES IT AS THE PRIMARY AGENT; THE RUNNER PRINTS `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`; `opencode.json` SETS `default_agent` TO `novel-writer`. THE WORDING WAS CORRECTED IN `state/current.md`'S TOP BLOCK, AT §8 ITEM 3 OF THIS RECORD, AND IN THE BATCH 0003 PROMPT. **THE DISPATCH IS WORKFLOW-OWNED AND WAS NOT TOUCHED, AND THE CORRECTION IS TO THE STATE FILES' CLAIM ABOUT IT AND NOT TO THE WORKFLOW.**
- **`state/phase-ledger.json` STILL READS `phase-000-bootstrap`, `planned`, ATTEMPTS `0`, AFTER FOUR HUNDRED AND SEVENTY CHAPTERS.** CONTROLLER-OWNED. REPORTED, NOT TOUCHED.
- **`tools/__pycache__/measure.cpython-312.pyc` IS STILL TRACKED AND `.gitignore` IS NOT A FILE THIS PASS WAS ASKED TO EDIT.** EVERY MEASUREMENT IN THIS SECTION WAS TAKEN WITH `PYTHONDONTWRITEBYTECODE=1` EXPORTED, WHICH IS THE PRACTICE THE VOLUME 09 CLOSE LEFT AND IT IS BINDING.
- **`state/current.md` HAD GROWN BY 3,509 WORDS OF APPENDED SECTION THAT CARRIED FIGURES THE FIVE LIVE FIELDS AT ITS TOP ALREADY CARRY.** THE APPENDED SECTION WAS CONDENSED BY THIS PASS. THE FULL RECORD IS THIS FILE, WHICH IS WHERE A FIGURE BELONGS.
- **`reviews/volume-10-batch-0002-review.md` IS A SELF-REVIEW AND STAYS ONE.** NOTHING UNDER `reviews/` WAS EDITED BY THIS PASS.

### 11.6 EVERY MEASUREMENT RE-TAKEN AFTER THE PROSE REPAIRS, ALL FIFTEEN FILES

| the thing | before this pass | after this pass |
|---|---|---|
| counted claims, one figure attached to a printed speech | 37, **0 mismatches** | **37, 0 mismatches**, including the re-measured **seventy-nine** at Chapter 470 |
| the four figures a man of fifty-six reads, against `intercept + c` | **one chapter wrong, Chapter 465 at 360** | **fifteen correct, four of them printing no line by decision** |
| the six ledger ladders: bid, lot book, rule, eighth month, ninth night, body | six, all at `intercept + c` | **six, all at `intercept + c`** |
| `wc -w` | 2,364 2,398 2,454 2,238 2,369 2,260 2,430 2,356 2,238 2,242 2,413 3,186 2,547 2,543 2,446 | 2,353 2,398 2,454 2,238 2,356 2,248 2,430 2,356 2,284 2,242 2,404 3,186 2,547 2,546 2,480, **mean 2,434.8, minimum 2,238, maximum 3,186, all fifteen inside the band** |
| the *about* hedge | 1,033 over fifteen, 284 per 10,000 | **1,034 over fifteen, 283 per 10,000** |
| `in that yard` | **164** | **134, of which 62 are register carriers and 72 are narrative** |
| shared twelve-word runs | 2,066 on this record's method, 2,355 on the reviewer's | **2,354 on the reviewer's method, which is 156.9 a chapter, and 35.1 per cent of a chapter's runs against 29.1 inherited** |
| identical paragraphs of twelve words or more, both runs, across the boundary | 0 | **0** |
| the six protected relays | 97, 37, 15, 15, 15, 15 | **97, 37, 15, 15, 15, 15 — none lowered, none raised** |
| `four hundred and eleven`, `Lot Seventeen`, a form of *was not run*, the ninth of the nine printed nights, a way to pay a person who is not in a household | 15, 15, 15, 15, 15 | **15, 15, 15, 15, 15** |
| the fifteen closing ledgers, first five words | fifteen distinct | **fifteen distinct, and 461's still opens *Nobody in that yard asked*, which is why it was not touched** |
| panels, weekday names, doubled full stops, all-caps lines, empty bold | 0 | **0** |
| the figure on the sheet at that gatepost | 411, unmoved, its own age 204 to 214 | **411, unmoved, its own age 204 to 214** |

### 11.6A THE FIVE APPEND-ONLY STATE FILES, BEFORE AND AFTER THIS PASS

| file | after the batch phase appended | after this pass |
|---|---|---|
| `state/current.md` | 66,263 | **57,935** |
| `state/continuity.md` | 41,319 | **45,643** |
| `state/open-threads.md` | 41,307 | **44,529** |
| `state/chapter-summaries.md` | 50,541 | **54,718** |
| `state/character-state.md` | 62,387 | **66,466** |

**THE ONLY ONE THAT WENT DOWN IS `state/current.md`, AND IT WENT DOWN BECAUSE A 3,509-WORD APPENDED SECTION THAT REPEATED FIGURES THE FIVE LIVE FIELDS AT ITS TOP ALREADY CARRY WAS REPLACED BY A POINTER AND A TABLE. A STATE FILE THAT ONLY GROWS IS A STATE FILE A PHASE CANNOT LOAD.**

### 11.7 WHAT THIS PASS DELIBERATELY DID NOT DO

**IT DID NOT CHANGE THE PLOT, THE OUTLINE, THE ENDING, THE LADDER, THE THREE COLUMNS THAT ARE A DAY OUT, THE COUNT OF THINGS THIS DISTRICT HAS MADE, THE COLUMN FOR THE NAME OF WHOEVER READ A THING OUT LOUD, THE FIGURE ON THE SHEET, THE BID, THE NINTH OF THE NINE PRINTED NIGHTS, THE MIDPOINT REVERSAL, THE ROMANCE, THE NAME, OR ANYTHING RESERVED. IT DID NOT ADD A SCENE. IT DID NOT UNCOUNT THE TWELVE-TH MONTH OR GIVE THE MONTH AFTER IT A LENGTH. IT DID NOT PUT A NAME IN THE RULED COLUMN. IT DID NOT EDIT `outline/series.md`, `outline/ending.md`, `outline/volume-09.md` OR `outline/volume-10.md`. IT DID NOT EDIT A CHAPTER OF AN EARLIER VOLUME. IT DID NOT EDIT ANYTHING UNDER `scripts/`, `.github/workflows/`, `.opencode/agent/`, `reviews/`, `tools/`, OR `state/phase-ledger.json`, AND IT DID NOT CREATE A BATCH 0004 DIRECTORY.**
