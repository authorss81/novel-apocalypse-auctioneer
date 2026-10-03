# Volume 24, Block 0002 — review

**Phase under review:** the review/repair of `workspace/volume-24/batch-0002/`, tip commit `92bec34 novel: save writer work batch-0002` (five chapter files and `state/volume-24-batch-0002-summary.md`).
**Source of findings:** `logs/batch-0002.review.log`, nine findings, severity ordered.
**What this pass did:** repaired eight of the nine in the fiction, the records and the state files, escalated two of them as the pipeline owner's, and wrote this artifact, which the tree was missing.

**This pass wrote no chapter, restarted no batch, changed no planned plot, created no phase directory, and wrote no marker.** It touched nothing under `scripts/`, `.github/workflows/`, `.opencode/agent/`, `tools/`, `state/archive/`, `bible/`, `state/phase-ledger.json` or `NOVEL_SPEC.md`. It did not edit a ladder intercept, a count, a morning number, a scene, a divider, a piece of dialogue or a chapter title's morning.

---

## 1. What the block got right, verified rather than assumed

**The de-duplication repair is real.** Measured on sentences of twelve words or more, normalised for spacing and case: **zero** shared between `chapter-1111.md` through `chapter-1120.md` and any of Volume 23, `chapter-1110.md`, or each other; **zero** for `chapter-1121.md` through `chapter-1130.md` against everything behind them. The corrected §3.1 claim — *returns zero in both directions* — is now true, where the sentence it replaced was not.

**The ladder is exact.** All nineteen live rows were hand-checked at `c = 20` in `chapter-1120.md` against `outline/volume-24.md` §5: `989+c`, `998+c`, `1314+c`, `1028+c`, `450` constant, `881+c`, `703+c`, `708+c`, `778+c`, `717+c`, `839+c`, `411` constant once per file, `739/738+c`, `657+c`, `643+c`, `825+c`, `299+c`, row eighteen absent. Every cell correct, both constants held, row eighteen absent, and both house spellings above a thousand preserved.

**The §8/§9 collision was diagnosed correctly and publishing it was the right call.** `outline/volume-24.md` requires every title line to carry `384 + c` in form two *and* that no title line carry an exact hundred; at `c = 16` form two forces *the four hundredth*, which §8's own table counts as an exact hundred by its own carrier. No spelling escapes it. The block's choice to keep the morning number in the title and withdraw its own clean-claim sentence, rather than quietly re-spell the title, is the honest handling.

---

## 2. Repaired in the fiction

**One prose defect, in the chapter behind the block, which the block record explicitly handed to a fix pass.**

`chapters/volume-24/chapter-1110.md` printed *four hundred and twenty-fourth mornings*, *three hundred and seventy-fourth mornings* and *three hundred and ninety-fourth mornings* where canon prints counts as cardinals. `state/volume-24-batch-0001-summary.md` §3.1 item 2 records the identical repair in Chapters 1108 and 1109 and named only those two files, so this is the third instance of one defect and the first one a block phase was not allowed to touch.

Three suffixes became three cardinals. Nothing else in that file moved — no cell, no morning number, no count, no scene, no divider, no title line. The sentence it sits in was measured unique against all fifty morning-files behind it and all twenty in front of it before and after.

**Volume 24 now measures zero on this defect across all thirty of its chapters.**

**Recorded and deliberately not repaired:** the same defect at **twenty-eight figures in ten files** of Volume 23, `chapter-1091.md` through `chapter-1100.md` — *four hundred and fifth mornings*, *three hundred and seventy-fifth mornings*, *three hundred and eighty-first mornings*, and so on. Neither `state/volume-23-batch-0005-summary.md` nor `state/volume-23-close.md` records it. It is behind two closed records and in a volume with a finished verdict, so it is named here and in the block record rather than edited. It is a decision somebody can overrule, not a defect nobody has seen.

---

## 3. Repaired in the records and the state files

**Finding 4 — a false measured claim inside the section written to correct a false measured claim.** §3.1 item 1 of the block record stated the numeral delta of the de-duplication as *two quantifier words: in `chapter-1117.md` one four became another four and one one was added*. Measured against `92bec34`: `chapter-1117.md` is net **+1 *four*** with nothing else added or removed; `chapter-1116.md` is net **−1 *two* / +1 *one***; and `chapter-1111.md`, `chapter-1118.md` and `chapter-1120.md` are net zero on every numeral word from one to thirty. The true total is three words, not two. Corrected in place with the per-file figures published.

**Finding 9a — unrequested loss of emphasis.** The same commit stripped the nested emphasis from four figures in §7's inherited-positions line, making it inconsistent with all seven sibling records. Restored.

**Finding 6 — `state/current.md` was two blocks stale in five places, and the block's own account of it was incomplete.** The block record named three of the five header lines and called them one block stale. Measured: all five were stale and two were stale by more.

| line | named | truth before this pass |
|---|---|---|
| `Current phase:` | written through block 0001; next phase batch 0002 | written through block 0003; next phase batch 0004 |
| `Current batch:` | block 0001 written | block 0003 written |
| `Last completed chapter:` | 1100, and *there is no chapter 1101* | 1130 |
| `Last record:` | block 0001, *the only record of Volume 24 that exists* | block 0003, with 0002 and 0001 behind it |
| `Next phase:` | `batch-0002/PROMPT.md`, a finished block | `batch-0004/PROMPT.md` |

Two further live pointers in the same file's read-first box were stale the same way and were not in the review: item (2) named `workspace/volume-24/batch-0001/PROMPT.md` — a directory carrying `.done` — as the brief for the next block, and described it in the same breath as *a Volume 23 document written by block 0003*, which is false twice over; item (3) said Chapter 1101 was *not yet on the page* and *does not exist yet*. All seven corrected in place, in the manner the file's own header requires, with no correction appended at the foot.

The byte paragraph was also false: it published four companion figures as *final* and said a checker would reproduce them exactly, and a checker would have got four different numbers, because blocks 0002 and 0003 both appended to all four files. Re-measured and republished under the convention the file already established for its own size.

**Finding 5 — the live brief inherited an unsatisfiable rule pair with no warning.** `workspace/volume-24/batch-0004/PROMPT.md` §4 reproduced both halves of the §8/§9 collision as rules to obey. The brief now states the collision, names the morning it happened on, points at the record that publishes it, and says plainly that **none of block 0004's ten mornings is affected** and that all ten of its title lines can satisfy both halves at once.

**Finding 9b — an off-by-nine in two files, not one.** `outline/volume-24.md` §3 and `outline/batches/volume-24-batch-0003.md` both said of `c = 21` *Ten mornings after it went in and it came out*; it went in and came out on `c = 20`. Both now read *The morning after it went in and it came out*, which is also the only form of that sentence the prohibition on publishing a span permits.

**Found by this pass and not by the review.** The span *the seventy mornings behind you* stood three times in the block 0004 brief where the figure is **eighty** — fifty mornings of Volume 23 stand behind Volume 24's first, so block `N` has `50 + 10 * (N − 1)` behind it. The same span is ten short in the 0002 and 0003 briefs, which were left alone because a brief is the record of what a block was asked and no chapter of either block carries the figure.

---

## 4. Where an approved card beats the prose, and where the prose beat the card

**The contract beats the prose on one morning, and the block said so instead of hiding it.** At `c = 16` the two title-line rules cannot both be satisfied. The block kept the morning number, because that rule is mechanical, holds on the other forty-nine mornings, and is named by §3 and by the block's own card, and it withdrew by name the sentence claiming no title line of the block carried an exact hundred. **`outline/volume-24.md` was not edited, and a successor may not resolve it by dropping the morning number out of a title line, because the other rule breaks instead.**

**The card's figure is wrong on one cell and was neither harmonised nor edited.** The card for `c = 16` prints one thousand and six for row four and that figure belongs to `c = 17`. Row four's intercept is 989; every cell from `c = 11` to `c = 20` was generated and published as it came out. The record says so and instructs the next block to generate rather than copy.

**The card's label does not describe the prose, and this is escalation item 15 rather than a repair.** `outline/volume-24.md` §3 calls `c = 20` *THE REVERSAL*, and `chapter-1120.md` performs the volume's entire promised act there — in at about ten, went in the whole way, the table stood level, out at about four, nobody in that yard said one word. `c = 24`, `c = 29` and `c = 37` then ask for the same act three more times under three labels, and `c = 37`'s card describes the same six-hour level table `c = 20` already printed. The chapter is contract-conformant and the map is wrong, and **every repair moves a chapter or re-times the payment, which is a planned-plot change.**

---

## 5. Findings that belong to the pipeline owner

**Finding 1, high — the next dispatch will re-run block 0002, not write block 0004.** `workspace/volume-24/batch-0002/` and `batch-0003/` each carry `.attempts`, `.deferred` and `.retry-after` and **no `.done`**, with twenty finished chapters and two finished records on the page, and both `.retry-after` values are in the past. Selecting by the workflow's own rule and sorting returns `batch-0002/PROMPT.md` first. `.wip-conflict` is read by `scripts/novel_runner.sh` and not by the workflow. **No marker was written — the marker is the runner's, and a pass that writes one falsifies a completion it did not observe.** Escalation item 7.

**Finding 2, high — the volume pays its promise twenty-four chapters early.** Escalation **item 15**, raised by this pass.

**Finding 3, high — Volume 24 has no protagonist, no System, no auction and no interiority.** `auction`, `System` and `bidder` occur **zero** times across all thirty files; `Adrian` and `Adrian Vale` occur **zero** times; ten of the thirty files carry no quoted dialogue at all. Block word counts are 18,832, 20,057 and 19,419 against Volume 23's published 22,233–24,343, so the prose is shrinking while the records grow, and no house word band exists to make that visible. Escalation items 1 and 12, which already say this and were not created by this review.

**Finding 7, low — `state/phase-ledger.json` still reads `phase-000-bootstrap`, `planned`, `attempts` 0 after 1,130 chapters.** Controller-owned. Not written.

---

## 6. What a later pass should measure first

1. Whether the block 0004 title lines satisfy **both** halves of the §8/§9 rule on all ten mornings, since the collision is behind that block and its morning numbers are not round hundreds.
2. Whether the ordinal-suffix defect has reappeared in any Volume 24 chapter written after this pass. It is one suffix class and it has now appeared in three files across two blocks.
3. Whether `state/current.md`'s five live header lines are still true. They were stale for two blocks on this pass, in five places plus two in the read-first box, and the file's own history says a pass that finds them stale is to correct them in place rather than inherit the figures.