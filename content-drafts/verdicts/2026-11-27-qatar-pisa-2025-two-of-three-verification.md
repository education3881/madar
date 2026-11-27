# Verifier's verdict: `2026-11-26-qatar-pisa-2025-two-of-three`

**Edition** 06, piece 4 · **Cell 6 of eight** · **Run** 2026-11-27 (daily) · **Verifier** acting
independently of the Editor's five-test verdict and of the Arabic Editor's gate, both of which filed earlier
in this run

## VERDICT: **VERIFIED.** No correction required. Two residual observations, neither of them a defect.

Both desks ahead of this one instructed the same thing in writing: *re-read Tables I.2.6 and I.2.8
independently*, because two of the Editor's eight repairs were **position** errors and the Arabic gate's one
finding was a **punctuation** error, which is the pair of classes a second human reading tends to reproduce
rather than catch.

**So this verdict did not re-read them. It re-derived them.** A parser was written against the chapter's
served text that takes a table caption and a system name and returns the three integers on that row, with no
input from the body, the verdict, the recon or the gate. Then the body's claims were asserted against its
output.

## The re-derivation, printed in full so the next reader need not take it on trust

**Table I.2.6, *Change between 2022 and 2025 in mean performance in science, reading and mathematics***

| System | Science | Reading | Mathematics |
|---|---|---|---|
| Georgia | 38 | 10 | 26 |
| Cambodia | 35 | 18 | 29 |
| Jordan | 32 | 20 | 26 |
| Montenegro | 32 | 13 | 5 |
| United Arab Emirates | 26 | 15 | 21 |
| Saudi Arabia | 23 | 5 | 1 |
| Thailand | 23 | 13 | 13 |
| Türkiye | 18 | 16 | 8 |
| Philippines | 17 | 20 | 16 |
| **Qatar** | **2** | **−1** | **2** |
| **OECD average-35** | **−3** | **−14** | **−9** |

**Table I.2.9, *Trends in mean performance … since 2015*, "Based on average decennial trend"** — Qatar 19 /
18 / 12 · OECD average-35 −7 / −27 / −24 · United Arab Emirates 18 / **−6** / 20.

**Table I.2.8** — Qatar −0.8 / −0.1 · OECD average-35 1.2 / −0.3, both in percentage points.

**Table I.2.1** — Qatar 434, not statistically different from *Mauritius, Uzbekistan, Montenegro, Albania\*,
Greece, Thailand, Serbia* (the parser returns the asterisk, so the register prints it and the body is right
to keep it). **Table I.2.3** — Qatar 434, OECD average 482.

## The trace

| # | Claim in the body | Source | Result |
|---|---|---|---|
| 1 | Qatar science +2 | I.2.6 | **PASS** |
| 2 | Qatar reading −1 | I.2.6 | **PASS** |
| 3 | Qatar mathematics +2 | I.2.6 | **PASS** |
| 4 | OECD average-35 −3 / −14 / −9 | I.2.6 | **PASS** |
| 5 | Jordan +32 / +20 / +26 | I.2.6 | **PASS** |
| 6 | UAE +26 / +15 / +21 | I.2.6 | **PASS** |
| 7 | Saudi Arabia +23 / +5 / +1 | I.2.6 | **PASS** |
| 8 | "thirty score points" top row to bottom in science | arithmetic on I.2.6 (32 − 2) | **PASS** |
| 9 | Qatar 19 / 18 / 12 on the decennial trend | I.2.9 | **PASS** |
| 10 | OECD average-35 −7 / −27 / −24 on the same measure | I.2.9 | **PASS** |
| 11 | Qatar −0.8 and −0.1 percentage points | I.2.8, column headers read | **PASS** |
| 12 | Qatar science mean 434 | I.2.1 and I.2.3 | **PASS** |
| 13 | OECD average 482, attributed to I.2.3 and the front page's note 1 | I.2.3 row + R2 note | **PASS**, and I.2.1 confirmed to carry no numeric average |
| 14 | seven-system comparison group, Albania asterisked | I.2.1 | **PASS** |
| 15 | 489 → 482 over 2015–2025 | R2 note 1 | **PASS**, quotation now ends where the register's clause does |

**Residue: none.** Every numeral in the English body is accounted for by a traced row, an arithmetic
operation on two traced rows, a date, or the edition number. The usual tail of untraceable numbers is empty
on this piece, which is a first for an Edition 06 piece and is a consequence of the Editor's repair 5 — once
every figure had to name its own table, there was nowhere for an untraced one to sit.

## Cross-edition parity (#42)

**The Arabic body prints nothing the English body does not** — the numeral multiset difference is empty in
that direction. The reverse direction shows twelve English-only tokens and **all twelve are artefacts or
legitimate composition**: the Arabic spells *الطبعةُ السادسة* where the English writes *Edition 06*, spells
the two share figures in words in one sentence while printing them as digits in another, and uses U+2212 for
the minus sign, which a naive multiset comparison reads as a different token.

So the multiset instrument reports twelve differences and zero of them are real, which is the **10-01
negative result holding** (annotation numeral parity measured 117 false positives out of 338). Parity was
therefore checked the way that works: **each of 25 load-bearing figures was looked for in the Arabic body by
name and sentence position, and all 25 are present** — the three I.2.6 Qatari changes, the three OECD
average-35 changes, the two share figures, the three decennial figures, the three OECD decennial figures,
434, 482, 489, the four systems' nine table figures, and the thirty-point spread (written *ثلاثون نقطةً*).

## The two residual observations, neither a defect

**1. The UAE's decennial reading trend is −6, and this piece does not mention it.** It is in Table I.2.9, one
row from Qatar's, and it belongs to `2026-11-26-uae-pisa-2025-all-three-lists`, the row in flight at cell 1 —
a system on all three of the 2022-to-2025 lists whose fitted ten-year reading trend is **negative**. Printing
it here would be the comparison across two questions that this piece's own brief prohibits. **It is handed
to the UAE row's brief instead**, which is where it is the finding rather than a decoration.

**2. The Editor's repair 2 is confirmed by the parser rather than by a second reading.** The claim deleted
was *"nine rows below Qatar's"*. The parser locates Qatar's row and the OECD average-35 row in the same
served text and neither reading — down Qatar's own panel (4th against 20th) nor across the flattened text
(forty-eight entries) — produces nine. **The deletion was right and the number was not recoverable**, which
is the correct outcome for a claim about a page's layout: there is no true value to substitute, so there is
nothing to correct to.

## Flag state (#18) and schema

`approved: false` in both editions at the time of this verdict. Dek EN 196/200, AR 168/200; title EN 34/100,
AR 26/100. `related:` resolves to three slugs, all three live in both editions. `arabicVersion` /
`englishVersion` reciprocal. No composite figure; `contains_composites: false` is correct.

## Cleared for cells 7 and 8

The hero still and share card, then the flip — which owes the **two forward rails** named at cell 1, into
`2026-11-26-pisa-2025-three-lists-of-risers` and `2026-05-31-qatar-humanity-spark-strategy`, in the same
commit as the flag (the 2026-06-14 rule applied to the graph).
