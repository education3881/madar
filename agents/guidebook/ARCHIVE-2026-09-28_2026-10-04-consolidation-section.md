# ARCHIVE — the 2026-10-04 consolidation section, rolled out of `INDEX.md`

**Rolled 2026-10-18** at the weekly consolidation, under the two-cycle rule in
`.claude/skills/madar-weekly/SKILL.md` (*roll anything older than two consolidation cycles into a dated
`ARCHIVE-*.md`*) and as the item the 2026-10-11 section named as **owed to this consolidation**. The two
cycles that remain in `INDEX.md` are **2026-10-11** and **2026-10-18**.

This is the record of the largest week the ruling register has ever taken — fifteen rulings, #72 through
#86 — and of the five malformed §3 rows it found. **Read it to answer a question about what happened in
that week; never plan a consolidation from it.** The register's current state is derived by
`python3 agents/tools/qa_register_shape.py .`, never read from a section like this one.

---

## Consolidation — 2026-10-04 (weekly review; covers 2026-09-28 → 2026-10-04)

**The largest week this register has ever taken, and the register was already true when it arrived —
for the second consecutive week. What was false was the two instruction sheets that tell people how
to use it.** Seven runs across seven days, no dark day, and **fifteen rulings, #72 through #86**,
against a previous single-week record of thirteen. The range read `#1–#86`, the §3 heading read
`#1–#86`, the series-integrity line read `#1–#86` and §1's count line read eighty-two — **all four
confirmed by counting rows, not by trusting numbers: 86 §3 rows contiguous 1 → 86 with no gaps and no
duplicates, 82 §1 rows, and every long-form pointer in §1, §2 and §3 resolving to a file on disk.**
The 09-20 point-of-filing rule has now survived three consecutive weeks and 38 rulings.

- **Ruling register #1–#71 → #1–#86.** Fifteen canonical one-liners were already in place, filed by
  the runs that earned them. What this consolidation added is placement and prose, and two repairs.

- **FIVE OF THE LAST EIGHT §3 ROWS WERE MALFORMED MARKDOWN, and the register's own reconciliation
  could not see it.** Rows **#80, #81, #82, #83 and #84** carried **three columns in a four-column
  table** — no `Long-form` cell at all — so each rendered with an empty last column and the file
  behind each ruling was unreachable from the canonical register. All five files exist and always
  did. The reconciliation the 09-20 rule prescribes counts *rows* and checks *ranges*; a row with the
  wrong number of **cells** is a perfect row by both tests. Fixed, and the check is now
  `len(row.split("|")) == 6` across all 86 — which found exactly these five and nothing else.
  **This is the 09-28 §1 finding repeated in §3 three days later:** *a reader following this
  section's own form found nothing, which is the only cost and it is a real one.* And it is #57
  again, one level down — equal row counts are not an agreement about rows.

- **§0 WAS REPAIRED AFTER BEING CARRIED A THIRD TIME, and it was stale in two homes.** The 09-06
  consolidation named it owed; the 09-20 consolidation named it owed again and wrote *"it is the first
  item of next week's consolidation and is not to be carried a third time"*; the 09-27 consolidation
  does not mention it once. §0 said **seven axes** and was last touched 2026-07-27 — **ten weeks** —
  while five consecutive Edition 05 verdicts worked **eight** and said so in writing. **And the grep
  the 09-27 amendment demands found a second live home nobody had ever reconciled:
  `agents/11_verifier.md` line 9, the one file the Verifier is told to read, also said seven and named
  only the original seven.** Both corrected in this commit; both now carry a count line; §0 declared
  canonical and the persona file told to defer to it. §0 now holds **eight numeric axes** (type/noun,
  #45, as the eighth) and **eight non-numeric rows** (register #43 · quotation #46 · clock #46 ·
  description-date #47 · seam #48 · re-read scope #53 · date referent #62 · forced determination #86).
  *The numeric axes took four months to reach eight; the non-numeric rows took four weeks. That is not
  a change in diligence, it is where the errors are now.*

- **Why a written obligation was carried three times in the same week the daily forward question ran
  seven-for-seven.** Both queues were honoured by every run. The difference is structural and it is
  **the slot**: the RUNBOOK binds the next run to test the previous run's forward question before
  adding anything new, and a forward question **generates its own successor**, so the slot is never
  vacated. Everything else — §0, the bet's part B, the five (a)–(e) items the 09-27 QA log carried,
  the queue's three oldest instruments — queues behind a relay that is always already full.
  **Measured, not asserted:** the strings *coverage map*, *absence register*, *output-bounded*,
  *font origin* and *new Date()* appear **zero times across all seven** of this week's QA logs, and
  the word *bet* appears on 09-28 and 09-29 and then not again. The RUNBOOK gains the rule this
  earned: **one queue, one head.**

- **The non-numeric family is enumerated in full for the first time — NINE members: #45, #46, #47,
  #49, #51, #53, #62, #64, #86.** The bullet carried correct *ordinals* (#62 seventh, #64 eighth, #86
  ninth) over an incomplete *list*, so #49 and #51 were counted and not named; #51's own file claims
  *"fifth member"* in so many words. **And #86's own file, filed this morning, enumerated six members
  and then claimed the ninth place** — two numbers in one sentence that could have disagreed and were
  never compared, inside a ruling about one edition making a claim with nothing able to contradict it.
  Corrected in the file, with the joke recorded. **#51 is cited from two families and counted in one**
  (the seven axes, where scope is an axis); the rule is stated at the point of the citation so the next
  count does not have to re-derive it.

- **The assertion-discipline family's quotable sentence read five members stale while its own count
  line, three sentences earlier in the same bullet, was right.** *"Seventeen of seventy-one rulings, a
  quarter of everything the operation has written down"* against a true twenty-two of eighty-six.
  Re-counted off the member list: **twenty-two**. The reason nobody caught it is worth keeping —
  **the ratio held.** A quarter was true at 17/71 and is true at 22/86, so the sentence stayed
  plausible while both of its terms went stale. *A ratio that survives its own numerator going wrong
  is a count that cannot be checked by reading it.* (The identical figure inside the `Last
  consolidation: 2026-09-27` paragraph is **left alone** — that paragraph is a dated record of what
  that review found, and a dated record is not drift.)

- **No new family, three weeks running, 38 rulings — and the placements were read off each ruling's own
  declared `Family:` line rather than assigned here.** All fifteen joined existing families:
  **assertion discipline** takes #73, #74, #75, #79, #80, #82, #83 and #85 — eight, which is why the
  family is now **twenty-five** and not twenty-two; **enumeration** takes #77, #78 and #81 (#81 as its
  seventh numbered member) with #75 dual-declared; **register hierarchy** takes #84, with #73 dual;
  **the clock / sourcing** takes #76; **composition discipline** takes #72; **the non-numeric family**
  takes #86. **Thirty-eight consecutive rulings without a new family is now a claim about the taxonomy
  rather than about the weeks** — though *composition discipline*, declared by #72 and by the 09-13
  RUNBOOK rule it extends, is the closest thing to a ninth family on the board and is named here as the
  candidate so the next review has something to count rather than to notice.

- **Archive roll, and the procedure changed.** `ARCHIVE-2026-09-14_2026-09-20.md` created, holding the
  09-20 consolidation section (due now, two cycles on) **and the 2026-09-11 daily addendum, which was
  due at the 09-20 roll and stood two cycles past it** — because each roll moved the block the previous
  review had named and nothing enumerated the remainder. The roll is now performed by listing every
  dated block below the tables and checking each one's age. Nothing deleted, nothing summarised. The
  **missing 09-27 section is recorded as an absence**, with the debt it dropped.

- **Section 1's three unresolved path references — the Researcher's call, made.** Found 09-28 and
  carried here: Brazil's and Kenya's source indices and the earlier Rwanda CBC recon resolve only in
  `content-drafts/recon/`, while 95 of 98 §1 references resolve in `agents/guidebook/`. **Decision:
  they stay where they are and the full path stays written out in the row.** A recon brief that also
  serves as a source index is both things, and moving the file would break the recon lineage every
  verdict and amendment on those pieces cites by path, to repair a convention that costs a reader one
  extra directory. **What is fixed instead is the convention's statement:** §1's rows name a bare
  filename *when the file is in `agents/guidebook/`* and a full repo-relative path otherwise, which is
  what the three rows now do and what every future row does. *A convention with three exceptions
  written into it is a convention; a convention with three exceptions nobody wrote down is a defect.*

- **Owed, carried deliberately and with the form that carries it.** From today these items live in the
  **standing queue** (`agents/logs/WEBDEV-QUEUE.md`) rather than in this paragraph, because this
  paragraph is exactly where the §0 debt went to die. Named here for the record only: the derived-register
  assertion (which would have caught the five malformed rows, and is queue item 3), and §0's own
  reconciliation at the next consolidation — now cheap, because it has a count line and a named owner.
