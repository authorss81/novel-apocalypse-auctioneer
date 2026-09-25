# Phase Review — batch-0003 (Chapters 21–30)

**Scope reviewed:** commit `97812b3` "novel: save writer work batch-0003" — 10 chapters (45,237 words), 6 state files, bible and `NOVEL_SPEC` edits, and `workspace/volume-01/batch-0004/PROMPT.md`. Working tree clean, so the commit was the phase. No files were edited during the review.

**Reviewer note:** the `novel-reviewer` subagent could not be dispatched and the review fell back to the default agent reading the phase out of git. It is a continuity-and-reference audit rather than a line edit pass, and it is recorded here so that the gate for this phase has a file. Nothing below is a comment on the plot, the plan, or the ending.

---

## High severity — continuity contradictions that would propagate

**1. Off-by-one-day drift on the batch's central timeline.** The writer's own deviation note (`state/batch-0003-summary.md`) correctly fixed Chapters 21–22 to the *crossing day* (19th), consistent with Ch 20 (8:30 a.m.–1:05 p.m. on the 19th) and Ch 23's arithmetic (bus out 7:25 a.m. + "eleven hours and forty minutes" = the evening of the **19th**; notice board rewritten 4:10 a.m.; child at the depot by 10:15 p.m.). But "the twentieth" was left in the downstream text:

- `ch24` — the child "was found … in the evening of the **twentieth**"
- `ch24` — "died between eleven o'clock and half past twelve" — Ch 23 has her alive and attended at 2 a.m.
- `ch24` — "you said in this yard on the **twentieth** that it was real" (that statement is Ch 20, the 19th)
- `ch24` — the steward "was on a cart on the **twentieth**"
- `ch25` — the suspension and the board's refusal both "on the **twentieth**"
- `ch30` — "on the night of the **twentieth**, when nine people were on a bus"
- Propagated into `state/continuity.md`, `state/character-state.md` (Tarin, Lina) and `workspace/volume-01/batch-0004/PROMPT.md` ("all nine were found … on the twentieth"). **Consequence: the 20th had no events at all in the volume.** Fix the prose first, then the four state/prompt files.

**2. `ch22:63` contradicts the span's own status.** "The crossing had been shut since the previous evening … Selik had shut it on the seventeenth" — but Ch 21 has Adrian putting three boxes on the supervised cargo exception and Ch 22 has them cross at 5:10 p.m. This is the justification for the "Load trace: flat" reading, so the fix is load-bearing.

**3. `ch29:35` contradicts `ch29:33`.** Selik says he closed the span on the 17th, then three paragraphs later that he has "carried a hundred and sixty people on the strength of that instrument **since the twenty-ninth**" — the 29th is after the 17th, and the housing was certified in March.

**4. The carter's accident has three dates.** `ch28:80` stages it "on the fourth night" of a table that ran the 31st/1st/2nd; `ch28:117` dates the same night "the night of the thirty-first … morning of the first"; `ch29:75` says "on the second of this month". As staged, the man who has lost three days is also the man who brings the claim to the table on the fourth night.

**5. `ch28:5` regresses canon.** "Three brokers. **Two** of them were the people he had already proved were carrying a single printing plate" — the plate is carried by all three (Prent, Slade, Vell).

**6. The Chapter 26 refusal timestamps are wrong and the arithmetic built on them fails.** Ch 18 stages the office scene: Mara 3:20 p.m., Tarin at four, Selik at twenty past four, Fen Ambrose at half past five — afternoon of the 18th. `ch26` says "ten past six on the evening of the eighteenth" and "twenty past four **the same morning**", and concludes "**fourteen hours** before twenty-eight people boarded." Against a 7:25 a.m. departure the true intervals are 13h25m (Tarin) and 15h05m (Selik). The Tarin quotation is verbatim from Ch 18; only the stamps are wrong. The same error is locked into `state/continuity.md`.

**7. The pilot line is timed two ways, in a file that forbids it.** The tape deviates "at 7:37" but Selik's own covering note says "at **twenty to eight**", and Ch 29 repeats "twenty to eight" three times — 7:40, a different minute. The decision to leave the pilot attached is "at about eleven" on the 19th in Ch 22 and "half past one in the morning of the twentieth" in Ch 29 and in `state/continuity.md`, under a heading that reads *must not be told two ways*.

---

## Medium

- **Units break the world.** `ch22` introduces "eighty kilo", "nineteen kilos", "nineteen degrees" — **zero** metric instances exist in Chapters 1–20, which use feet/inches/yards over two hundred times. Pick one system.
- **`ch26:71`** — "the nine had been on it for fifty-three minutes" is transplanted from Ch 20's 53-minute interval. At the find it was eleven hours and forty minutes.
- **`ch24:73,81`** — the sealed-page register does not reconcile: three real sheets described across rows dated 9th / 9th-and-16th / 19th, and the 19th row's role never stated. A reader cannot tell which single cell changed. The registrar says she cannot certify her own instrument; her own instrument should still be followable.
- **`ch27:93`** — "He had four figures available to him"; three are then described.
- **A state file misattributes a chapter.** `state/chapter-summaries.md` and `state/character-state.md` place the "twenty-two letters / five of them" beat in Chapter 22. It is in **Chapter 29** and appears nowhere in Ch 22.
- **The reading ledger does not match the book.** `ch27:61` has Nessa enter "the fourth entered this month," but `state/current.md` and `state/character-state.md` list three and "three hours." Chapter 20's reading of the brass is the missing fourth.
- **Crowd counts drift inside one scene.** Ch 25: the same yard is six hundred, four hundred and three hundred in a single morning; Ch 21 runs 200/240. Since exact headcounts are a rhetorical device here, this reads as error rather than growth.
- **`ch28:3`** — "by twenty-eight o'clock that evening": a 24-hour register in a feet-and-yards world.
- **Stage-direction tic.** "in the yard" 36×, "the yard" 119×, "on the rail" 13×, "own words" 12× across 45k words. Not a correctness problem.

---

## What was working, and must not be flattened

- **Panel discipline is a real improvement.** Exactly three panels in ten chapters — one each in 24, 27, 30 — none of which solves its scene. Ch 30's is read off an open page of the public book rather than the brass, and that extension is declared and bounded in `bible/power-system.md`.
- **Motive integrity holds under pressure.** Selik wins on the merits and is argued with, not defeated, and does not gloat. Halloway is more credible than before and says so in public. Adrian's second exception is a decision with a genuinely good stated argument, refused on professional rather than villainous grounds; the accusation in Ch 25 targets the shape of the thinking, and nobody in the room is satisfied — including Adrian, who has no answer.
- **Both mandated beats land and are paid for.** The far-side clause saves eight and costs eleven hours, four streets, six children in the cold and a child, with Tarin putting the liability on himself in his own words. The nine-line term is entered unattached and the yard stops asking Adrian anything — the loss lands as absence, not as a beating.
- **Board mechanics are dramatised, not announced.** All four seats named aloud before the board acts in Ch 24 and 25; the new limits (cannot strike a line, cannot grant a use, does not audit a claim) each break a scene.
- `state/batch-0003-summary.md`'s Plan deviations section is honest and specific, including the panel-frequency and length flags.

---

## Gate status

- Chapters exist as finished prose, in order, each changing the situation. ✔
- Midpoint reversal and batch climax both present (25/26 accusation, 28 second backwash, 29 closure). ✔
- Exactly one next-phase directory exists (`batch-0004`); no over-dispatch. ✔
- **State files were not consistent with the prose** (findings 1, 6, 7, and the two ledger errors), and the next prompt inherited the wrong date, so the repair had to land in the prose and the state files rather than in a new prompt. **Fixed in this pass.**
- **No `reviews/batch-0003-review.md` existed** when the review ran, so the reviewer gate for this phase was unmet. **This file closes it.**

**Recommended repair order:** (1) the day-drift in Ch 24/25/30 and its four downstream files; (2) Ch 22:63 and Ch 29:35 span status; (3) the pilot-line time and decision-time single version; (4) Ch 28 accident date and broker count; (5) Ch 26 refusal stamps; (6) the state-file misattribution and reading ledger. Items 1–3 are single-line edits in most cases; none require rewriting prose.

---

## Repair record

All of the above were actioned in a single follow-up pass. Prose was edited in place and no chapter was restarted; the batch's beats, motives, panel budget and planned ending are untouched. Notable judgement calls:

- **The child's hour is now refused, not replaced.** Ch 24 no longer names one. Ch 23 never stated it, and a registrar who declines to invent a time is more in character than a repaired clock time.
- **The sealed-page register was rebuilt as one changed cell** — the children's row renumbered forty-three to forty-four, with a forty-third appearing dated the nineteenth and no page behind it — plus the fact that Mara was reading a fair copy. This is a small change of mechanism, made because the reviewer's point was that the reader could not follow her own instrument, and it leaves the chapter's actual beat (a fourth sheet that has never existed, and a registrar who cannot certify her own page) intact and sharper.
- **The Chapter 28 accident moved to after the table session**, which is where the prose's own logic required it: Tove's warning is conditional and the "nobody had blamed anybody" line is retrospective. He now brings the claim to the four o'clock table on the second, is told out loud that the return point is under nine feet of water, and goes over about an hour later. This is a better scene than the version it replaces and it removes a date.
- **The span was never "shut on the seventeenth."** The seventeenth is the manifest cut; the span is shut when the certificate is suspended on the twenty-first. Both Ch 22 and Ch 29 and Ansel Roak's question were rewritten to that, which also fixed the "five days before the bus" arithmetic at no extra cost.
- **Mara now refuses to enter an interval** for the two refusals and enters both figures instead, which is the registrar's argument made in her own voice and removes the fourteen-hour error without a new number to defend.
- **One error was introduced and caught during the repair:** the first pass wrote the pilot time as "twenty-five minutes to eight", which is 7:35. The correct rendering of 7:37 is "twenty-three minutes to eight" and it is now that, everywhere.
- **Six instances of the "in the yard" tic** were varied. Dessa Rill's yard — a service cut four streets away — was left alone, because it is not the same yard.
