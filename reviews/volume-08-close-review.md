# Volume 08 Close Review Repair

**This is the repair response to the review of commit `6352d44`, "novel: save writer work close".** The review found six things: two blockers, two majors, a moderate and a minor. **All six are repaired or disposed of below, and nothing was left as a claim without the change.** Three of the review's own verifications were re-run here before any of its numbers were believed, and two of the three did not need changing and one did.

**Nothing was restarted. No chapter was touched. No prose in any volume was edited. No date, age, trade, character, scene, beat or planned plot moved. The ending of Volume 08 stands: the eighteenth of the tenth month, the second chair at the end of the trestle table, and a man of fifty-six sitting in it.** Every repair below is a figure, a pointer, a header, or a sentence of instruction in a document.

---

## What was fixed

### 1. BLOCKER — the next-phase prompt told the Volume 09 outline to settle the protagonist's name, which standing canon forbids — FIXED

`workspace/volume-09/outline/PROMPT.md` offered the writer the choice to settle the name amendment "in `outline/volume-09.md`, in the reserved list, in one sentence," and repeated it as an outline-level power in its thirteenth carried-forward item, in its list of things that may not be spent, and in its required section 1.

`outline/volume-08.md:26` states the only door, and the review was right that the prompt inverted it:

> the amendment may be settled by a later volume's outline **on the day a person in this district says the name out loud in a room or a yard, in a scene, and the later outline records that the prose now carries it.**

**The order in that sentence is the whole rule: the prose first, the outline second.** The prompt dropped the precondition entirely and handed the writer a power that no file grants an outline written before a single word of its volume's prose exists.

**Four places in the prompt now say the same thing, and each says it for its own context:** the prohibition, with both of the reasons it is not the writer's to settle; item (13) of the thirteen things to carry; the things that may not be spent; and the required section 1. The section-1 instruction is no longer "settled or not" — it is **not settled, with the reason, and with the day the volume has to make possible.**

**What replaced the power is work rather than a refusal, because a prompt that only takes a decision away leaves the writer with nothing to do about it:** the outline must say the position on the page, must plan a room or a yard in which a person in this district *could* say the name out loud with a reason on the page why they would and somebody there who tells them not to, must name who settles it afterwards and when, and must carry the default in its reserved list unchanged. It must also disclose, if its own chapters never give the name a day, that the amendment is still open at the end of it.

**The review's second reason holds and is now in the prompt in full:** a name an outline settles is a name a block may use, and a name a block uses lights up `tools/measure.py`'s reserved scan, which is run at every close. Settling the amendment in Volume 09's outline would have guaranteed a reserved-scan hit in Volume 09's own close — inside the very phase the prompt spends its length policing.

### 2. BLOCKER — the volume's headline figure did not reproduce: 92 printed, 87 actual — FIXED

Measured here, independently, before the repair, and again after it:

```
per-chapter occurrences of "four hundred and eleven", Chapters 341-390:
341-350: 3 1 1 1 3 2 2 2 3 2   (block 1 = 20)
351-360: 2 2 2 2 2 2 2 2 2 2   (block 2 = 20)
361-370: 2 1 2 2 2 2 2 1 2 2   (block 3 = 18)
371-380: 1 2 3 1 1 2 1 2 2 1   (block 4 = 16)
381-390: 1 1 1 1 1 1 1 1 3 2   (block 5 = 13)
total = 87; chapters with at least one occurrence: 50 of 50
```

`\b411\b` is 0, `four-hundred-and-eleven` is 0, and `four hundred eleven` is 0, so no digit or hyphenated form is being missed. The one bare `four hundred` in the fifty chapters is Chapter 344's "written over four hundred times" and is not this figure.

**What was wrong, and it was worse than the total.** The published per-chapter column at `state/volume-08-roll-summary.md` section 9 had **fifty-one cells for fifty chapters** and summed to **ninety-four**, which is not the ninety-two printed in bold three cells earlier in the same row. Nineteen of its fifty cells disagreed with a count. The block figures `24 / 21 / 18 / 16 / 13` should be `20 / 20 / 18 / 16 / 13`: the first and second blocks were wrong and the last three were right. **The error is consistent with *four hundred yards* swept in — there are 27 of those and 16 of *four hundred miles* across the fifty — and with real hits dropped in other chapters.** Chapter 389 carries the string three times, in one of them twice in a single sentence, which is the shape of occurrence that a line count misses.

**Repaired in three places, with both sets of numbers printed wherever a repair moved a disclosure, per the house rule:**

| file | was | now |
|---|---|---|
| `state/volume-08-roll-summary.md` section 9 column | 51 cells, sum 94 | 50 cells, sum 87, cell-for-cell against the files |
| `state/volume-08-roll-summary.md` block row | 24 / 21 / 18 / 16 / 13, **92** | 20 / 20 / 18 / 16 / 13, **87**, both sets printed |
| `state/volume-08-roll-summary.md` §1, §4 and the standing-figure paragraph | 92 | 87 |
| `state/volume-08-close.md` frame-table row | **92**, 1/1275, 24 / 21 / 18 / 16 / 13 | **87**, 1/1348, 20 / 20 / 18 / 16 / 13 |
| `state/volume-08-close.md` §1 table and the read of the table | NINETY-TWO | EIGHTY-SEVEN, with item 10 added |

The rate is re-derived against the close's own stated denominator of 117,329 on its own floor convention: 117,329 ÷ 87 = 1,348.6, and 87 × 1348 = 117,276 while 87 × 1349 = 117,363, so the cell is 1/1348 and the old 1/1275 was 117,329 ÷ 92 truncated.

**The finding itself was never in doubt and is unaffected.** The number did not move on any of the fifty days, its coverage is fifty of fifty chapter files, and its own age runs from ninety days at Chapter 341 to one hundred and thirty-nine at Chapter 390. Only the count of its appearances was wrong. **No chapter was edited, because a close may not edit prose and a review may not either.**

A new item 10 in the close's read of the table records the error, the method, and the cell-count failure, and the roll's section 9 preamble now says the check caught this row after it was written — which is the argument for printing the sum beside the total.

### 3. MAJOR — the next-phase prompt's reading list could not fit in a context — FIXED

The prompt told the writer to read `state/current.md` **in full** plus `state/continuity.md`, `state/open-threads.md` and `state/character-state.md`, on top of opening with a 124 KB close and a 136 KB roll. Measured:

```
continuity.md 400 KB + character-state.md 412 KB + open-threads.md 330 KB + current.md 234 KB = 1,376 KB
```

That is roughly 340,000 tokens of state before 260 KB of close and roll, before `outline/volume-08.md`, five block records, five canon cards, `series.md` and `ending.md`. It contradicts `PHASE_SYSTEM.md`, which says never to load the whole manuscript into every phase prompt and to create a volume-level index when the continuity files grow too large.

**The reading instruction is replaced with a six-step priority order**, and the sizes are printed in it so the writer can see the problem instead of discovering it at the cost of the phase:

1. `state/volume-08-close.md` whole, `state/volume-08-roll-summary.md` **in slices** (section 1 for the fifty-day table, 7 for the frame table, 8 for the method, 9 for the per-chapter columns, plus the reserved and guardrail sections), with `grep -n '^## '` given as the way to find them.
2. `outline/ending.md` and `outline/volume-08.md`, both whole.
3. `outline/series.md`, whole.
4. The four state files **in slices only**: `state/current.md` above the `## HISTORICAL` line and nothing below it, then the newest section of each of the other three and nothing older, located by `grep`.
5. The five Volume 08 block records and canon contracts **in slices**, with the standing warning carried over that three of the five block records no longer reproduce against the chapter files, so where a block record and the roll disagree the roll is measured and the block record is a record.
6. Chapters 381 to 390 in full, only if the verified context budget safely allows it after all of the above.

`state/volume-08-roll-summary.md` is named as the volume-level index that `PHASE_SYSTEM.md` asks for, because that is what it is. **The four archive files and `logs/` are excluded, and the prompt now says `logs/` is gitignored so nothing in it resolves and nothing in it is a source.**

### 4. MAJOR — the live state headers contradicted the phase that had just closed — FIXED

**`state/continuity.md`, `state/open-threads.md` and `state/character-state.md` all still carried the header "LIVE, Volume 05 (*The Nine Locks*, Chapters 201–250)" — three volumes stale** — and a scope line reading "Volume 05 only," while each file's last section described Chapter 390. A writer trusting the header got an explicit wrong scope statement from the file it was told to read for the current position.

Each of the three headers now names Volume 08 closed, states the real scope as Volume 05 onward, records that the header was stale until this review found it, and carries the file's own size with the instruction not to load it whole. **Nothing below the headers was rewritten**, because the sections above are the record of their own blocks and the sections at the end are the live ones.

**`state/current.md`'s live header — the part of the file that declares itself the current position — said the close was the only next phase, and that `state/volume-08-roll-summary.md` did not exist and was the close's to write.** Both were false, and the second named the very file the commit had created. The `Current phase:`, `Rolling volume summary:`, `Last batch summary:` and `Next phase:` fields are corrected to the closed position and point at the Volume 09 outline phase. **The appended section 17 was already correct; it now agrees with the header above it instead of contradicting it.**

### 5. MODERATE — a dangling log citation and a missing outline — DISPOSED OF, DIFFERENTLY

**The log citation is repaired at the point of citation, and no file was invented.** `state/current.md`, `state/open-threads.md`, `state/volume-08-batch-0005-summary.md` and `outline/batches/volume-08-batch-0005.md` each named `logs/batch-0005.review.log` as if it resolved. It does not: `logs/` is gitignored, and the file is not in the repository and never was. Each of the four now says so where it gives the path, which is the disclosure `state/volume-04-close.md` records the Volume 04 fix pass having already adopted — *"a reviewer's words are not a writer's to write, and a file invented to satisfy a citation is worse than a citation that admits it is broken."* This file is the committed record of the close review instead.

**`outline/volume-04.md` is disclosed, not created.** It does not exist, `git log --all -- outline/volume-04.md` returns nothing, so it was never committed and was not deleted. It is already disclosed in four documents — `state/open-threads.md` items 6, `state/volume-07-batch-0001-summary.md` item 17, `reviews/batch-0005-review.md` item 3 and `state/volume-04-close.md` — every one of which declined to create it, and the standing reason is unchanged: *writing a volume outline for a closed volume during a repair pass would put an unverified document into the outline set, which is worse than an acknowledged gap.* **It was not created here for the same reason.** What is new is that a writer is now told about it before they go looking: the Volume 09 outline prompt carries a paragraph naming the gap, forbidding its creation, and pointing at `state/volume-04-close.md`, `state/volume-04-roll-summary.md` and the five Volume 04 block records as the record instead. **The real cost, which the review named, is that a series-level audit across every volume outline cannot run, and that is stated in the prompt as a known cost and not as a fix.**

### 6. MINOR — two claims in the new prompt needed a method or different wording — FIXED

- **"Identical paragraphs of twelve words or more: one over the fifty."** A plain paragraph-equality scan returns **0**. The pair reproduces only with markdown emphasis markers stripped, because Chapter 371 sets the first line of the lot book as a plain standalone paragraph and Chapter 383 sets the same line inside `**`. The prompt now says one, names the strip as part of the method, states the plain scan's figure, and instructs the writer to say which method produced any figure of their own.
- **"*volumes* four times, at Chapters 376, 377, 382 and 383."** That is four **chapters** and **five occurrences**; Chapter 383 carries it twice. The close's own table lists chapters, and the prompt restated them as occurrences. It now prints both figures and says they are two figures.

### 7. A CRAFT RISK THE REVIEW DECIDED RATHER THAN FIXED — THE TITLE

The prompt was headed *what holds without a name, and who is going to hold it*, which is built on Volume 08's own title, *What Holds Without a Name* (`outline/volume-08.md:1`), while `outline/series.md:225` gives Volume 09 **The Empty Lot**. The deviation was disclosed rather than hidden, so it was not a defect — but two consecutive volumes of a manuscript that runs on an auctioneer's vocabulary should not share a title construction, and the choice is a writer's to make deliberately.

**The prompt is now headed with the series file's title**, and says in one place that the title is the outline writer's decision, may not echo Volume 08, defaults to the series file's unless a reason is stated, and goes in the deviations table whatever is chosen. **This is not a directive to use that title; it is the removal of an inherited one that should never have been seeded.** `outline/series.md` may still not be amended to match.

---

## Claims of the review that were re-run here and needed no change

The review verified these and so did this pass, on the same method, so the next phase does not inherit them on trust:

- `python3 tools/measure.py calib` reproduces **53 class-one claims, 0 mismatches, denominator 25,569, `wc -w` 25,689, 675 shared twelve-word runs**. All four.
- **Panel count holds.** Exactly two `^>` lines exist in the fifty chapters: Chapter 354, the panel, and Chapter 385, a document line. "A close that counts two has counted a document" is right.
- **The inherited Chapter 373 mismatch reproduces:** the speech under the claim `a hundred and ninety` is 188 words. Still unrepaired, because the repair is the claim figure and no phase may edit prose in another block's chapters.
- **Opening shape: 50 of 50** chapters match `The [ordinal] of the [ordinal] month came in …`.
- `the reader` = **3** case-insensitively at 342, 349, 355, all in-world. Reserved hits reproduce: `noon` ×2 at 346, `registrar` ×2 at 375 and 376, `a bell` ×3 at 342, 345, 348. The one bare `four hundred` is at 344 and is not a hit on the figure.
- **The figure's own age reproduces:** first of the sixth to the thirtieth of the eighth is 90 days, and to the eighteenth of the tenth is 139.
- `scripts/novel_runner.sh:189-201` — `ensure_next_phase` really does write only a generic continuation stub, with no concept of a volume outline or a close. The standing claim that a writer creates the next phase is verified.

## What belongs to the pipeline owner and was not touched

- **`state/phase-ledger.json` still reads `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0`, `range: null`,** with three hundred and ninety chapters committed. Controller-owned. Reported, not edited, as every phase since has done.
- **The review agent never ran.** `logs/close.review.log:1` reads `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`, so the close was reviewed by the writer reviewing itself. This is the same finding already on the open-threads list from Volume 07, it is why several of the six findings above needed checking rather than believing, and the fix belongs in `.opencode/agent/` or the dispatch in `.github/workflows/`, not in a chapter.
- **`logs/` is gitignored**, so no review transcript is ever committed. That is why the citation repair above is a disclosure and not a restored file, and why this response lives in `reviews/`.

## Where the repair is recorded

`state/current.md` section 18 and `state/open-threads.md` section 22 carry the same account in the state files, so a writer reading state and not `reviews/` still gets it. **The full figure table is at `state/volume-08-close.md` section 8, item 10 of the read of the table and the per-chapter column is at `state/volume-08-roll-summary.md` section 9.**
