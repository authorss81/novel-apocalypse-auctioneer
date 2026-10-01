# Volume 18 Block 0001 — Review of Chapters 841 to 850, and of the state handoff around them

> **THIS IS AN EXTERNAL REVIEW PASS AND IT IS THE FIRST ONE IN THIS TREE TO ACTUALLY RUN. `novel-reviewer` DOES NOT DISPATCH AS A PRIMARY IN THIS REPOSITORY — THE RUN LOG `logs/batch-0001.review.log` BEGINS WITH THE FALLBACK NOTICE — SO EVERY PASS EITHER BLOCK RECORDED IN `state/volume-18-batch-0001-summary.md` AND `state/volume-18-batch-0002-summary.md` WAS A WRITER AGAINST ITS OWN WORK. THIS PASS WAS DISPATCHED BY THE PHASE THAT READ THAT LOG, AND IT IS STILL A REVIEW AGAINST THE TREE AND NOT A REVIEWER OF INDEPENDENT AUTHORSHIP. THE `AGENTS.md` GATE ASKS FOR A REVIEWER; WHAT IS RECORDED HERE IS WHAT WAS AVAILABLE.**
>
> **IT REVIEWED THE CHAPTERS 841 TO 850, THE STATE HANDOFF, AND CHAPTERS 851 TO 860 AS THE SUCCESSOR'S INHERITANCE. IT CHANGED ONE CHARACTER IN ONE CHAPTER, FIVE PLACES IN ONE STATE FILE, AND THREE CLAIMS IN ONE BLOCK RECORD. IT DID NOT RESTART THE BLOCK, MOVE A BEAT, RENAME A CHARACTER, ALTER A LADDER CELL, OR TOUCH THE PLANNED PLOT. THE PLOTTED SHAPE OF VOLUME 18 IS UNCHANGED AND THE OUTLINE IS UNTOUCHED.**

---

## 1. WHAT WAS INDEPENDENTLY CONFIRMED AS CORRECT

**THE LADDER HOLDS. THIS IS THE STRONGEST RESULT IN THE PASS.** An instrument was written from nothing outside the repository, importing nothing from `tools/`, with `PYTHONDONTWRITEBYTECODE=1` exported before every run. It was validated **first** against three ten-chapter ranges of Volume 17 where every figure is already known — Chapters 811 to 820, 821 to 830 and 831 to 840 — and it returned **zero findings on all thirty**. Only then was it run against Volume 18.

**IT THEN RETURNED ZERO FAILURES ACROSS CHAPTERS 841 TO 860 — ALL FIFTY CHAPTERS, ALL SEVENTEEN CARRYING ROWS PLUS ROW 19** — against the intercept taken from the Chapter 840 column. Every cell on every morning reproduces `INTERCEPT + c` exactly.

| the thing | the result |
|---|---|
| Rows 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17 | every cell correct on all twenty mornings of Volume 18 to date |
| Row 12, the constant | four hundred and eleven on twenty of twenty, its carrier printed once per file, never in one sentence with row 11 |
| Row 5, the struck row | its past-tense carrier exactly once per file, its present tense at zero on all twenty — the bid was not reopened |
| Row 18, the gone row | absent on twenty of twenty and not invented |
| Row 19, the origin | `39 + c`, forty on Chapter 841 rising one a morning to fifty-nine on Chapter 860, and **the Volume 17 `c - 1` trap was avoided** |
| the lane count | twenty-seven and unmoved through block 0001; moved once, to twenty-eight, on `c = 11` only |
| the back page | thirty-three on twenty of twenty |
| the counted months | six on twenty of twenty |
| things this district has made | fourteen; the five things it does not have are five and unpaid |
| the register | 30,250 words and 151 dividers for block 0001; 30,228 and 188 for block 0002 — both re-measured off the files after the repair |

**THE MORNING NUMBER, THE `c` ORIGIN, THE ANCHOR, AND THE DECLARED DIRECTION SPLIT** — ten rows before the carrier and seven after — all hold. A figure-only checker fires on every row that prints before its carrier and every one of those fires is correct; that is the house's design and it is named in the record.

**THE TWO STRUCTURAL CLAIMS THE PASS TREATED AS MOST LIKELY TO BE WRONG BOTH CHECKED OUT.** The claim that a second occurrence of `night of that run` / `having slept on` carries the same figure as the first is **true on every morning where it occurs**, and Volume 17 prints the same pair twice on Chapters 830 to 835, 839 and 840, so a successor treating a second occurrence as a defect would flag seven chapters that are right.

---

## 2. THE SIX FINDINGS AND WHAT WAS DONE ABOUT EACH

### FINDING 1 — THE VOLUME RANGE IN THE LIVE HEADER WAS WRONG ON THREE COUNTS AT ONCE. **FIXED.**

`state/current.md` printed `VOLUME 18 (*The Auction of the World*, CHAPTERS 841 TO 880)`. The contract is **Chapters 841 to 890, mornings 125 to 174**. The header was ten chapters short, cut the volume off at the end of block 0004 so it excluded block 0005 entirely, and was internally inconsistent with its own sentence saying the resolution begins at Chapter 886 — outside the range it printed.

**REPAIRED IN PLACE** on the `Current phase:` line, which now prints 841 to 890 and names the correction and its three errors. This is the header-correction practice the file itself prescribes: correct in place, name the correction, never append a footer.

### FINDING 2 — A REPAIR THE BLOCK REPORTED AS DONE WAS NOT DONE. **FIXED IN THE CHAPTER AND CORRECTED IN THE RECORD.**

Block 0001's summary §2.4 closed with a sentence asserting **EVERY QUOTATION MARK** across the ten mornings was clean, reporting that a fifth pass had added an asymmetry test for unbalanced marks and that it was **at zero on all ten files now**.

**That zero was false.** `chapter-0841.md:127` read:

```
"Ask her," said Mavis Dorr. "You do not have to say why.""
```

— a doubled closing mark, 75 quotation marks in the file, an odd total. **Chapter 841 was the only parity-broken file in the block and the only `""` site in the ten.** The block had repaired the same *class* of defect in Chapter 843 in §5.1 item 2 and reported that repair accurately; the miss was in Chapter 841, and because the doubled mark sat on the page **before** the block's measurement passes ran, no later pass could be expected to catch it.

**REPAIRED TO ONE MARK. ONE CHARACTER CHANGED. NO WORD AROUND IT TOUCHED, NO BEAT MOVED, NO FIGURE AFFECTED** — the word count of the chapter is unchanged at 3,357 and the register of the block is unchanged at 30,250 words and 151 dividers.

**AND THE RECORD'S CLAIM WAS CORRECTED RATHER THAN LEFT STANDING**, in §5.1 item 2 and in §2.4, with the lesson named: **a test added after a repair is not evidence about the past, only about the present.** The zero is now stated as true of the ten files as they stand and explicitly false of them as they stood.

### FINDING 3 — THE HANDOFF NAMED A PHASE THAT WAS ALREADY WRITTEN. **FIXED, AND IT WAS WORSE THAN REPORTED.**

The reviewer's report was that `workspace/volume-18/batch-0003/PROMPT.md` was on disk and unaccounted for in the read-first box. **On inspection the defect was larger and in the opposite direction from what was reported:** the `Next phase:` line pointed at `workspace/volume-18/batch-0002/PROMPT.md`, chapters 851 to 860 — **and that block is complete.** Its ten chapters are on the page, `state/volume-18-batch-0002-summary.md` is on the page, and its own closing sentence reads *BLOCK 0002 IS COMPLETE*. Block 0002's brief was created by block 0002, which is why the reviewer took the authorship claim at face value; the real problem is that **the header had fallen one whole block behind the page and was pointing a successor at work already done.**

**THE LIVE POINTER IS NOW `workspace/volume-18/batch-0003/PROMPT.md`, CHAPTERS 861 TO 870, `c = 21` TO `c = 30`.** The corrected `Next phase:` line, the read-first box, the `Last completed chapter:` line (now 860, not 850), the `Last batch summary:` line (now naming **both** current records and no longer calling block 0001's record "the only file that carries the measurement"), and the `Current batch:` line (now covering both blocks' measured registers) were all corrected together, because a header that is right on one line and stale on the next is a header nobody can use.

**NO CHAPTER IS MISSING AND NO PHASE WAS SKIPPED.** The chapters run 841 to 860 without a gap. The next chapter to write is 861.

### FINDING 4 — THE FIGURE BLOCK IS ABOUT 29 PERCENT OF EACH CHAPTER. **RECORDED AS A RISK. NOT REWRITTEN.**

Measured, per chapter, as the words in the figure block against the whole file: **843, 841, 860, 846, 837, 867, 831, 853, 859, 833 — mean 847 words, mean 28.6 per cent of the chapter.** Across the ten mornings the block reproduces itself with only its digits moving.

This is in tension with two `AGENTS.md` gates: *Do not spam the reader with statistics* and *Vary sentence length and paragraph rhythm*.

**It was not rewritten, and the reason is recorded rather than assumed.** The figure block is **load-bearing**: it is where seventeen ladder rows, six static counts, the row-19 origin, and the struck and gone rows live. Reducing its density would mean either dropping rows the contract requires or moving them into prose, and moving a figure into a prose mouth is precisely the failure mode this manuscript's own record calls *a figure in a mouth* — the defect class that produced three of block 0001's twelve. **The honest position is that the architecture and the prose gate are in conflict and this pass did not resolve the conflict.** It is disclosed here and in the live header so a successor inherits it as a known cost rather than as a neutral house move.

**THE NUMBER IS NOT UNIQUE TO BLOCK 0001.** Block 0002's figure block averages 880 words and 29.4 per cent, so this is the volume's architecture and not one block's lapse.

### FINDING 5 — THE REGISTER CADENCE RUNS ABOVE THE HOUSE RATE, AND WAS BEING MEASURED INSTEAD OF RESOLVED. **PARTLY RESOLVED IN THE MEASUREMENT; THE PROSE IS DELIBERATELY LEFT ALONE.**

Per thousand words, counted whole-file:

| the family | Volume 17, 40 chapters | block 0001 | block 0002 |
|---|---:|---:|---:|
| `have said since` | 0.17 | **2.02** | 1.32 |
| `about nine people at the top of eleven feet` | 1.41 | **3.01** | 2.55 |
| `about four people at the top of eleven feet` | 0.39 | **2.41** | 1.29 |
| `about four of them` | 0.54 | **2.91** | 2.78 |
| `about four feet off` | 1.14 | 1.59 | 1.82 |

Block 0001's record measured `have said since` at 61 against 19 across forty chapters, labelled it the house's own move, and declined to act. **That is honest, and it is also the disposition this pass did not simply repeat.** The finding is real: 2.02 per thousand is **roughly twelve times** the Volume 17 rate, and `AGENTS.md` names exactly this pattern as prohibited mechanical filler.

**Two things are now true that were not before.** First, block 0002 came in at 1.32 — **about a third lower** — so the block's own successor had already begun thinning the cadence without being told to, and the elevated rate is **specific to block 0001 rather than a property of the volume's plan.** Second, the comparison the record made was **per block against per block, which is the fair comparison, and it holds**: 61 in one block against a best of 7 in any Volume 17 block is an order of magnitude, not a rounding difference.

**The prose was not rewritten.** Every one of these families is doing narrative work — `have said since` is how the block reports what people said afterwards about something that was not decided, which is the volume's central fact; the crowd families are how a yard of about nineteen people is made audible without inventing interiority for any of them. Stripping them would not remove repetition, it would remove the **mechanism** by which this particular book renders a crowd, and would leave the beats thinner than they already are.

**What changed is the framing.** Block 0001's record called this "the house's own move" and measured it so a close would inherit the rate. That is **understated**: it is a measurable conflict with a stated prose gate, it is above the rate the volume's own next block achieved, and it is now disclosed as a risk in the live header with numbers, so that a writer revising block 0001 for any other reason can thin it toward block 0002's 1.32 **without being told the current density is intentional.**

### FINDING 6 — THE QUALITY GATE'S REVIEWER REQUIREMENT WAS UNMET, AND THE MISSED DEFECT PROVES IT. **RECORDED; NOT RESOLVABLE IN THIS REPOSITORY.**

`reviews/` held no Volume 18 file, and both block records state that `novel-reviewer` does not dispatch as a primary, so every pass either block ran was the writer against its own work.

**Finding 2 is the proof that the gap was real and not a formality.** A defect that the block's own record reported as repaired — the quotation-mark parity zero — was false, it was on the page before the measurement, and **no self-pass could have found it, because a test added after a repair cannot fail on a defect that predates the test.** The reviewer that did run on this pass found it in seconds with a parity check the block did not think to run at all.

This is not fixable here: `novel-reviewer` dispatch is controller-owned, and no controller file was edited. What is fixable is that the gap is now **on the record with a named instance**, so it is a tracked condition rather than a footnote in a summary nobody reads.

---

## 3. WHAT WAS NOT CHANGED, AND WHY

| not changed | why |
|---|---|
| the figure block's content or density | load-bearing; see finding 4; rewriting it would move figures into mouths |
| the register families in the prose | they are the crowd mechanism; see finding 5 |
| any ladder cell, carrier, count, or direction split | twenty of twenty verified correct; no reason to touch a correct figure |
| the planned plot of Volume 18 | out of scope for a review, and nothing found required it |
| `outline/volume-18.md` | the contract is correct; finding 1 was a header error **against** it |
| chapters 851 to 860 | outside the block under review; read and measured as inheritance, found correct, edited nothing |
| `state/volume-18-batch-0002-summary.md` | its claims were checked against the files and hold; one clause about the live header is stale and is corrected by the header correction itself |
| `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, `state/phase-ledger.json`, anything under `tools/` | controller-owned; no byte written |

**NO FOOTER WAS APPENDED TO ANY LIVE STATE FILE AND NO NEW PHASE DIRECTORY WAS CREATED.** `workspace/volume-18/batch-0003/PROMPT.md` already existed and is the next phase's brief; this pass corrected a pointer to it and created nothing.

---

## 4. THE FINDING THAT MATTERS MOST

**This block's arithmetic was excellent and its two most confident claims about itself were both wrong.** The ladder is clean on twenty of twenty mornings and the register reproduces to the word — but the record reported its quotation-mark coverage as complete when it was not, and the live header reported the volume as ten chapters shorter than it is and pointed at a phase that was already written.

**Both errors point the same way: they are claims of completeness, made by the process that produced the work, and never checked by anything outside it.** The volume 17 record already predicted this, in its own words — *not one of the twelve was a ladder cell* — and block 0001 repeated the finding thirteen times. The numbers were never the problem. **A figure-only checker will keep returning zero on prose that has a doubled quote mark in it, and a writer will keep writing excellent figures and then mis-describing what it checked.**

The useful thing a review pass can do here is not to improve the arithmetic. It is to make the record stop claiming more than it measured.

---

## 5. THE VERDICT

**BLOCK 0001 PASSES ON ITS FIGURES AND ITS PLOT, AND ITS RECORD AND THE HEADER AROUND IT DID NOT PASS.** The ten chapters are sound: the ladder is clean, the counts are right, the escalation is built as the contract requires, the asking does spread and stop being one man's, and the reversal at Chapter 865 and the resolution at Chapter 886 are neither pre-empted nor disturbed.

**REPAIRED:** one doubled quotation mark in Chapter 841; one false zero-claim in two places in the block record; one wrong volume range; one handoff pointer aimed at a completed block; one read-first box naming the wrong inherited record.

**RECORDED AND NOT RESOLVED:** the figure block at 28.6 per cent of each chapter, and a register cadence at roughly twelve times the Volume 17 rate on `have said since` — both disclosed with figures, both real conflicts with the stated prose gate, neither rewritten, because rewriting either would cost more than it buys and would move figures out of the only place this book can safely hold them.

**THE ONE THING A SUCCESSOR MUST NOT INHERIT UNCHANGED** is the belief that a passing measurement is the same thing as a correct record of what was measured.