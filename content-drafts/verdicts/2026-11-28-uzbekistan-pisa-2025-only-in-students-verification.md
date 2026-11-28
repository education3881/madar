# Verification verdict — `2026-11-27-uzbekistan-pisa-2025-only-in-students`

**Verifier · 2026-11-28 · cell 6 of 8 · RESULT: FAIL WITH ITEMS.**
**The piece's central claim is falsified by the register it is built on, in both editions.**

---

## Provenance: both triples reproduced on an independent re-fetch

Fetched from this runner, in this run, with no reference to the banked read beyond the timestamp:

| Register | Asked | Bytes | sha256 | Verdict |
|---|---|---|---|---|
| Chapter 2 of *PISA 2025 Results (Volume I)* | `web.archive.org/web/20261104162528id_/…student-performance-in-pisa-2025_23e075c2.html` | 2,426,000 | `e5a429b011ff90e5676417dda3cf5358b2f72b940ee068fae3faa96a6f068a71` | **reproduced** |
| The full-report front page | `web.archive.org/web/20261114165129id_/…full-report.html` | 1,614,913 | `1c3018b4d17e205b7e6331bdc91217546ac8ebdce5d68439ea38f5fd87264a1b` | **reproduced** |

`oecd.org` was re-tested and still answers **403** to this runner, so the refusal recorded in the
annotations is current and was not routed around. The archive served the raw snapshot gzip-encoded; the
hash is of the decompressed bytes, which is what the annotation says it is of.

**Quotation channel: 15 of 15 curly-quoted spans in the English body are verbatim** in the independently
fetched captures, 12 of them the bold-quoted register spans. The eleven register quotations repeated in
`sources[]` are the same strings. **The Arabic body's Latin-bearing spans were checked against the same two
captures and are verbatim**, 16 of 16, the extra being `OECD average-35` as the Arabic gate recorded.

---

## ITEM 1 — FAIL, and it is the spine. The chapter DOES print a score-point change for Uzbekistan.

The piece says, in a section of its own:

> Everything above is counted in students. The release's other unit is the score point, and it has two
> tables for it. **Uzbekistan is in neither.**

and then:

> the chapter behind that page prints no score-point change for Uzbekistan in either of the two tables that
> would carry one. … **a reader who wants the figure behind it will not find one in this report**

**Both sentences are false, and the second is the piece's title, dek, finding and hero still.** All fourteen
tables of Chapter 2 were parsed in full from the re-fetched capture and every cell reading `Uzbekistan` was
enumerated. Uzbekistan appears in **eight** of the fourteen — I.2.1, I.2.3, I.2.4, I.2.8,
I.2.10, I.2.11, I.2.12 and I.2.13 — and **two of the eight print a change in score points**:

| Table | Title, as the chapter prints it | Uzbekistan's row | Unit |
|---|---|---|---|
| I.2.10 | Change between 2022 and 2025 in the socio-economic gap in science performance | disadvantaged **+85**, advantaged **+87**, gap **+2** | **score points** |
| I.2.12 | Change between 2022 and 2025 in mean performance in science, by gender | girls **+85**, boys **+80**, gender gap (boys − girls) **−5** | **score points** |

Both notes read *"Positive change in mean performance"* / *"Only countries and economies that can compare
PISA 2022 and PISA 2025 results are shown."* These are changes in **mean science performance**, 2022 to
2025, in score points, for Uzbekistan, in the chapter the piece says prints none.

**And they are the largest in their own tables.** I.2.12 holds 76 entries: Uzbekistan +85 for girls, then
Georgia +38, Cambodia +37, Montenegro +34 — Uzbekistan is more than double the next, against an **OECD
average-35 of −2 for girls and −3 for boys**. I.2.10 holds 74 entries: Uzbekistan +85 for disadvantaged
students, then Georgia +55, the UAE +40.

So the reader the piece sends away empty-handed is handed **+85 and +80 score points** by the same chapter,
on the same screen, two tables down from the one the piece quotes.

**What is true, and it is the better finding.** The two tables the piece names are genuinely empty for
Uzbekistan, and this re-fetch confirms it: no `Uzbekistan` cell exists in **I.2.6** or **I.2.9**. What the
piece missed is **why**, and the reason is printed in the notes it already quotes. I.2.6 shows only systems
that can compare 2022 and 2025 *"in all three subjects"*; I.2.9 needs *"at least two previous
assessments"*. I.2.10 and I.2.12 are gated on neither — their note asks only that 2022 and 2025 be
comparable at all. **Uzbekistan clears that and fails the other two.** The consequence is exact and is a
sharper piece than the one drafted: **the chapter prints Uzbekistan's science score-point change only when
it is SPLIT — by gender, and by socio-economic status — and never once as a single number for all
students**, because the only table that would carry the single number is gated on a subject requirement
that has nothing to do with science. The front page's *"scores also went up"* is therefore supported in the
report, and the one figure a reader would quote for it is the one figure the chapter never prints.

**Classification.** This is not a transcription error and no instrument this operation owns could have
caught it. Every figure in the piece is correct. Every quotation is verbatim. The defect is a **claim of
absence scoped to the tables the drafter enumerated and then generalised to a unit** — two tables checked,
four tables in that unit, and the quantifier in the sentence is *"the release's other unit … has two tables
for it."* #57's defect on a negative claim: *an enumeration cannot report what it did not enumerate, and a
claim of absence inherits the enumeration's edge as if it were the world's.* Filed as **ruling #162**.

## ITEM 2 — FAIL. A count the chapter's own tables falsify.

> The same chapter does this to **two other systems** on the same both-ends list of seven — Jordan and
> Uzbekistan are both missing from the decade's table — and a reader who takes an absence from a list as a
> finding about a country will get **all three** of them wrong.

Measured over the seven systems the both-ends sentence names (Jordan, Uzbekistan, Montenegro, Saudi Arabia,
Türkiye, the United Arab Emirates, the United Kingdom):

- **I.2.9, the decade's table:** Jordan **absent**, Uzbekistan **absent**, the other five **present**.
- **I.2.6:** Uzbekistan **absent**, Jordan **present**, the other five **present**.

So **one** other system is affected, not two, and the set is two systems, not three. The sentence's own
appositive contradicts its count: it says *two other* and then names *Jordan and Uzbekistan*, which is one
other plus the piece's own subject. Neither *two* nor *all three* has a referent in the register.

## ITEM 3 — PRINTED, not failed. Three tables of Uzbek figures the piece does not use.

Recorded so the repair is not re-researched at the next cell. Beyond the cells the piece uses, Uzbekistan also
has rows in **I.2.4** (computational problem solving, mean **402**, company Jordan, Brazil, Argentina, El
Salvador) and **I.2.11** (low and top performers by national quarter of socio-economic status, **−47.5** and
**−49.2** percentage points, **+0.4** and **+0.5**). Neither is needed for the repaired spine and both are
available to it. I.2.11 in particular says the fall is present in both the bottom and the top
socio-economic quarters, which the piece's gender section already does for girls and boys.

---

## Everything else the trace covers: CLEAR

| Row | Result |
|---|---|
| **I.2.8** Uzbekistan −46.1 / +0.5 | confirmed in the re-fetched capture |
| **I.2.8** OECD average-35 1.2 / −0.3 | confirmed |
| **−46.1 is the largest movement in the table** | confirmed — 76 entries parsed independently, Uzbekistan first |
| **Cambodia −22.1 is the next largest reduction** | confirmed, and *less than half of it* checks (22.1 × 2 = 44.2 < 46.1) |
| **Latvia +11.4 the largest the other way** | confirmed |
| **76 entries** | confirmed by independent parse |
| **I.2.13** −49.7 / −42.5 / +0.6 / +0.4, columns girls-then-boys | confirmed, column order read off the header row again |
| **I.2.1** science mean 438; the ten not-different systems in table order | confirmed — Chile, Israel, Iceland, Brunei Darussalam, Mauritius, Montenegro, Albania\*, Qatar, Greece, Thailand |
| **I.2.3** 438 beside an OECD average of 482 | confirmed — I.2.3 prints 482 in its own first column, which is where the Qatar repair (#161's run) put it |
| **The three population sentences and the coverage passage** | verbatim |
| **The front page's non-OECD sentence and *bucking the trend*** | verbatim on the front-report page, and **absent from Chapter 2**, exactly as the piece says |
| **Uzbekistan not named in the coverage passage** | confirmed — the six named are Cambodia, Ecuador, El Salvador, Lebanon, Morocco, Paraguay |
| **Fourteen numbered tables in Chapter 2** | confirmed independently, which is the Saudi verdict's count holding on a second parse |
| Guardrail carriage (#19) | the coverage fence, the colour-is-not-text limit and the significance limit are all carried **in the prose**, not avoided |
| Acronym evidence (#101) | PISA and OECD both expanded in `sources[]`; `qa_acronym_evidence` clean |
| Forced determination (#86 / #134) | **0 named humans**, and the gap is stated in the body. Nothing to determine |
| Served tense (#117) | no editorial future on an arrived date |
| dek / title caps | EN title 66/100, dek 191/200; AR title 53/100, dek 163/200 |
| `related:` resolution | three slugs, all resolve. **Note for the flip:** `2026-11-27-saudi-pisa-2025-two-clocks-disagree` is still **held**, so this piece cannot flip before it |
| Flag state (#18) | `approved: false` in both editions, no stale duplicate outside the build path |
| Assets | still 3,393 bytes on disk; og card a valid 1200×600 PNG, header parsed rather than assumed |

---

## Disposition

**FAIL WITH ITEMS. The flag does not flip on this verdict.** Items 1 and 2 go back through the Editor. Item
1 is a spine repair and not a correction: it moves the title, the dek, two sections and both editions'
`sources[]`, and it has to be made in Arabic as well as English. Every figure the repair needs is in this
verdict, measured from the re-fetched capture, so no cell needs to re-open a register to make it.

**The hero still survives the repair and should not be redrawn.** Its two dotted empty rectangles are
Tables I.2.6 and I.2.9, which are empty for Uzbekistan — the one thing in the piece that item 1 does not
touch. What changes is what the piece says they mean.

---

# RE-VERIFICATION OF THE REPAIRED SPINE — 2026-11-28, same run. RESULT: PASS. Cell 6 CLOSED.

The Editor returned the piece with the spine inverted rather than parked
(`2026-11-28-uzbekistan-pisa-2025-only-in-students-editor-disposition.md`). Re-verified against the same
two independently re-fetched captures, whose hashes are in the table at the top of this file and were
reproduced in this run.

| Row | Result |
|---|---|
| Item 1's claim removed | **yes** — no sentence in either edition now says the chapter prints no score-point change for Uzbekistan |
| The replacing figures | **I.2.12** girls +85, boys +80, gap −5; **I.2.10** disadvantaged +85, advantaged +87, gap +2 — each re-read from the parsed table in the re-fetched capture, both editions agreeing with it |
| The two population counts | **I.2.12 holds 76 entries** (next after Uzbekistan: Georgia +38, Cambodia +37); **I.2.10 holds 74** (next: Georgia +55) — both re-derived by independent parse, both marked in `sources[]` as this publication's own count and not attributed to the OECD |
| **OECD average-35** in I.2.12 | −2 girls, −3 boys — confirmed |
| The mechanism claim | confirmed from the notes themselves: I.2.6 *"in all three subjects"*, I.2.9 *"at least two previous assessments"*, I.2.10 and I.2.12 *"can compare PISA 2022 and PISA 2025 results"* with no subject condition |
| The negative claim's scope, now written down | `sources[]` in both editions names every table carrying an `Uzbekistan` cell — I.2.1, I.2.3, I.2.4, I.2.8, I.2.10, I.2.11, I.2.12, I.2.13, **eight of fourteen** — so the claim *no single all-student figure is printed* now ships with the enumeration that makes it checkable. This is the repair item 1 actually needed |
| Item 2's count | corrected in both editions: one other system (Jordan), absent from I.2.9 only; the other five present; Uzbekistan alone absent from both |
| Quotation channel after the repair | **EN 18 of 18** quoted spans verbatim (was 15), **AR 19 of 19** (was 16) — the three new strings in each are the two table titles and the shared note |
| dek / title caps | EN title 59/100, dek **198**/200; AR title 43/100, dek **183**/200 — counted at compose, not at the gate |
| Arabic gate on the changed passages | APPROVED with three corrections, recorded in the disposition |
| Guardrails (#19) | unchanged and still carried; the repair **adds** one — that an absence from a table is not an absence from the unit |
| Flag state (#18) | `approved: false` in both editions. **Unchanged, deliberately** |
| Assets | still and og card untouched and still true; see the disposition for why the still is not redrawn |

**Cell 6 is closed and cell 8 is the only cell left. The piece does not flip today**, and the reason is
not the repair: its `related:` rail names `2026-11-27-saudi-pisa-2025-two-clocks-disagree`, which is still
held, and a flip would put an approved page's rail on a slug the build does not serve. **Saudi flips first,
on 2026-11-29 by the decision recorded in the ledger, and this piece flips behind it.** That ordering is
now a fact about the corpus rather than a preference, and it is written into the ledger row.

**What this verdict cost and what it bought.** It is the first verification in this edition to fail on its
piece's central claim, and the first to fail on something no instrument this operation owns could reach: a
negative claim, every figure in it correct, every quotation verbatim, falsified only by reading the tables
the sentence did not enumerate. Filed as **ruling #162**.
