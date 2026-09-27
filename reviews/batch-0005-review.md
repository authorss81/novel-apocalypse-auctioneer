# Batch 0005 Review Repair — Volume 05, *The Nine Locks*, Chapters 241–250

**This is the repair response to `logs/batch-0005.review.log`.** The review pass reported nine findings. **Two were real and are fixed. Four were checked against the chapters and are not defects; the evidence is below, because acting on them would have damaged the volume. Three belong to the pipeline owner and are flagged, not edited.**

**The batch was not restarted. No chapter was rewritten. No beat was dropped, no date moved, no count changed, and the planned plot is untouched.** Two sentences were amended in two chapters and the rest of the work is state-file hygiene and this record.

---

## What was fixed

### 1. The two System panels were not identifiable as panels — FIXED

This was the review's finding 5 and it is a real defect, and it is a defect **against the batch's own canon contract** rather than against a house style. `outline/batches/volume-05-batch-0005.md` line 30 sets the test: *a document is introduced as a thing somebody reads out and is read back afterwards because it is the rule of the counter; a panel arrives unasked and is then argued with or not argued with.*

The three printed documents pass. The first charter is read out and read back at `chapters/volume-05/chapter-0244.md:15`, the covenant at `chapter-0246.md:19`, and the letter at `chapter-0249.md:17`.

**The two panels failed, because the word *panel* appeared zero times in Chapter 247 and zero times in Chapter 249.** They arrived as "something that arrived in that barn" and "something arrived in that yard", which on the page is indistinguishable from a document somebody brought. The review was right that a reader cannot tell them apart. The volume already had the word and the definition — *a panel is a rule and a rule is not a document and is not a fourth and is not one of the six instruments this district built and not named*, at `chapter-0216.md:45`, and `A PANEL CAME INTO A YARD THAT NOBODY HAD ASKED FOR` at `chapter-0218.md:73` — and the panels were never named with it.

Each arrival sentence now names the arrival and restates the definition at the moment it is needed. **The panels' three lines each are byte-identical, the characters still disagree with the third of the three, and the counts are unchanged at a hundred and seventeen and a hundred and twenty-six.**

The Chapter 249 clause additionally states on the page that the three documents this district does not own are three and **a panel is not a fourth of them**, so the repair cannot be read as moving a count this volume has held still since Batch 0001.

### 2. The state files could not be loaded by the next phase — FIXED

This was the review's finding 7 and it is the finding that would actually have broken the Volume 05 close. The close was instructed to read four state files "in full" and they totalled roughly 2.2 MB before a single chapter was opened. The largest single line was 18,476 characters.

**The four files were rotated, not trimmed. Nothing was deleted, edited, summarised or reworded.** Everything before Chapter 201 was moved verbatim into `state/archive/`, and each live file now carries a scope header and Volume 05 only.

| file | before | after | archive |
|---|---|---|---|
| `state/continuity.md` | 610,758 | 115,653 | 496,351 |
| `state/chapter-summaries.md` | 880,736 | 249,678 | 632,335 |
| `state/character-state.md` | 515,665 | 108,409 | 408,515 |
| `state/open-threads.md` | 204,592 | 66,371 | 139,465 |

**Verified line by line against `HEAD`: every non-blank line of all four original files is present in either the live file or its archive. Zero missing, in all four files.**

`state/current.md` (82 KB in 110 lines) keeps its existing `## HISTORICAL` divider and gained a reading-scope header. `workspace/volume-05/close/PROMPT.md` step 6, which carried the unfollowable instruction, is corrected in place: read all four live files in full, which is now possible, and do not open the archives.

---

## What was not fixed, and why

### 3. "The counted-it device is noise" — NOT A DEFECT. The evidence is unambiguous.

The review reported 22 instances of "counted it and got NNN" as a device with no rule, citing Chapter 242 (97 and 140) and Chapter 241 (84, 116, 123 and 108) as evidence of arbitrariness.

**The device has a rule, the rule is stated in the book, and the arithmetic is exact.** The man of about nineteen counts the **words in the speech**. The rule is on the page at `chapters/volume-04/chapter-0151.md:17` — *counted the words in that sentence once and got twenty-five* — and corroborated at `chapter-0152.md:85` and `chapter-0155.md:45`, and at `chapter-0206.md:69` where a man says twenty-one words and the counter gets twenty-one.

**Re-measured for this repair: of fifty-five counted speeches in Chapters 241 to 250, fifty-three match their stated count exactly. One is a parsing artifact of the checking script. The fifty-fifth is `chapter-0250.md:51`, an eight-word line which the prose explicitly declines to count — "it was not counted, because there was nobody there to count it".** The review's own cited examples are consistent with the rule: 97 and 140 are different-length speeches, and 84, 116, 123 and 108 are four different-length speeches.

This matters more than a formatting quibble. **The volume's theme is who counts what and whether a count is a fact, and a counter who is right every time is the load-bearing evidence for it.** "Fixing" this would have broken the thing the book is about. `state/volume-05-batch-0005-summary.md` already claims the counts were measured and written afterwards; that claim now holds under independent check, and section 11 of that record tells the volume close not to "fix" a count.

### 4. "Bold is doing the work of emphasis, and Chapter 1 has neither" — NOT A DEFECT

The review counted 30 `**` markers in `chapter-0241.md` and compared them to Chapter 1.

**Bold-wrapped dialogue is a series convention that begins at `chapters/volume-01/chapter-0021.md`, not something this batch introduced**, and it is *less* dense in this batch than in the forty chapters before it:

| | lines opening `"**` | bold markers per 1,000 words |
|---|---|---|
| Volume 01 | 163 | — |
| Volume 02 | 573 | — |
| Volume 03 | 602 | — |
| Volume 04 | 356 | — |
| Volume 05, Ch 201–240 | — | 14.5 |
| Volume 05, Ch 241–250 | — | 9.1 |

**Stripping wrapper-bold from ten chapters would make Volume 05's last block inconsistent with the other two hundred and forty.** The underlying observation — that this register is heavily marked-up — is fair, and it is already disclosed as a property of the writing in the block record's frame disclosure. It is a series-level typography question, not a Batch 0005 repair, and it is flagged below for the owner.

### 5. "The cast has no names and the protagonist is unidentifiable" — NOT FIXED HERE, and it is not a Batch 0005 defect

**The review's own framing concedes this is not a one-batch problem** — "~88 chapters of drift". It is longer than that. The lead's descriptor "mends fencing" first appears at `chapter-0086.md`, and the lead is still named outright as recently as `chapter-0162.md`, so the two systems overlap for about seventy chapters rather than replacing each other cleanly.

Three reasons this was not actioned in a repair pass:

1. **The descriptor system is load-bearing and it is consistent.** Six men of about thirty-four appear in this batch, and each is qualified by a trade — *mends fencing*, *digs loam*, *keeps a tally for six households*, *keeps a scale*, *keeps a road*, *keeps a goat* — used 252, 202 and 46 times for the top three. **The trade is the identifier and it never collides.**
2. **`outline/volume-05.md` itself relies on the same distinction.** Line 53 names the registrar as thirty-four and line 54 pairs "Adrian" with "the man of about thirty-four who digs loam" as two different men. The volume outline is written in the descriptor register too.
3. **`bible/characters.md` has a standing section headed *Unnamed and unnamed on purpose*,** which is how this project handles the question.

**Renaming the cast is a series-wide retcon that would touch roughly two hundred chapters, every state file, the bible and the ending's dependency on a findable protagonist. It is not a repair and it must not be done inside one.** It is flagged for the owner as the single largest open craft question in the manuscript.

The review's narrower, fair point is retained: in `chapter-0241.md` the lead and the loam man do trade speeches within a page of each other. Both carry their trade on every mention, so this is density rather than ambiguity, and it was judged not worth destabilising a canon chapter over.

### 6. "One sentence frame carries the whole batch" — NOT SMOOTHED, ON PURPOSE

The review's counts are accurate and the block record **already discloses the same thing independently**, naming the rise of the block's own instrument phrase as *the block's finding and not a virtue*. Re-measured here for the record:

| frame | Batch 0004 | Batch 0005 |
|---|---|---|
| `not asked` | 61 | 73 |
| `in his own words` | 39 | 29 |
| `a clerk of nineteen years entered` | 7 | 26 |
| `mends fencing` | 59 | 47 |
| `digs loam` | 25 | 20 |

**Two frames rose and two character descriptors fell in rate, and the phrase that rose fastest is the block's own instrument.** That is already on the record in `outline/batches/volume-05-batch-0005.md` line 180 and in section 8 of the block record.

**Reducing it now would be the wrong repair.** The volume close is explicitly instructed to *carry the frame disclosure forward as a fact about how this volume is written and not smooth it*, and `workspace/volume-05/close/PROMPT.md` step 0 says this pass should not smooth it either. A repair pass that quietly lowered the repetition would have destroyed the disclosure the block made about itself. **The measurement is recorded here so the close inherits it as a fact.**

---

## Belongs to the pipeline owner — flagged, not edited

These are controller-owned or series-level. Per `AGENTS.md` this repair does not touch `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`.

1. **The review agent never ran.** `logs/batch-0005.review.log:1` reads `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`. The review phase fell back to the **writer** agent reviewing itself, which is why three of its five blocking findings are checkable assertions that do not survive checking. `reviews/` holds 5 files for more than twenty batches. **Fix belongs in `.opencode/agent/` or the dispatch in `.github/workflows/novels.yml`.** This is the highest-value fix in the list: it is the reason the other findings needed this much checking.

2. **`state/phase-ledger.json` is stale** — still `phase-000-bootstrap`, status `planned`, 0 attempts, while five Volume 05 batches are canon. Controller-owned.

3. **`outline/volume-04.md` is missing** (01, 02, 03 and 05 all exist). Volume 04 is closed at Chapter 200 and its roll and close record are in `state/`, so nothing is broken now, but Volume 06 planning will want it. **Not reconstructed here**: writing a volume outline for a closed volume during a repair pass would put an unverified document into the outline set, which is worse than an acknowledged gap.

4. **Series-level craft questions, in the order I would put them to the owner:** the descriptor-only cast (item 5 above), and the typographic density of the blockquote register (item 4 above). Both are real, both are series-wide, and neither should be settled inside a single batch.

---

## What the volume close should take from this

- **The two panels are now panels on the page, named in the volume's own word.** Do not "correct" the Chapter 247 or Chapter 249 arrival sentences back to "something".
- **All four state files are loadable and Volume 05 only.** Read them in full; do not open `state/archive/`.
- **The word counts are right. Do not fix them.**
- **The frame repetition is a disclosed property of the volume, not a defect to be smoothed.** See `state/volume-05-batch-0005-summary.md` section 11.
