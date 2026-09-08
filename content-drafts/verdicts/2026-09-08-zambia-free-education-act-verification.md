# Verification verdict — Zambia, *The law that moved the finish line* (EN + AR)

**Slug:** `2026-08-25-zambia-free-education-act`
**Edition:** 05 (Africa) · wave row 1 · **banking order position 1 of 3**
**Verifier:** persona #11 · **Date:** 2026-09-08
**Drafted:** 2026-08-25 (EN) / 2026-08-26 (AR) · **Editor's pair verdict:** 2026-08-27 PASS
**Flag state at verdict:** `approved: false` on **both** files — the hold holds (#18).

> **Standing note.** This is Edition 05's **first** verification verdict, owed since the
> 09-03 P1 and scheduled by the 09-06 weekly review for 09-07 — a dark day. It is
> delivered on 09-08, one day late, named rather than absorbed. Three pairs are banked
> against zero verdicts; the ≤3 ceiling is reached and this verdict is the instrument
> that unblocks slot-3 drafting.

---

## RESULT: **FAIL WITH ONE ITEM** (plus two carried notes)

Every load-bearing figure in this piece traces, and the great majority were confirmed
through a **second, independently-routed channel** (#27) — my own re-fetch on 09-08,
fourteen days after the drafter's compose-time read. The piece is, on the evidence,
unusually well built: it declines the figures it cannot stand behind, it fences the audit
before it uses it, and it carries every guardrail the recon flagged.

**One figure fails the trace on its semantic type**, in both languages, and it is a
figure the piece itself introduces with the word *unambiguously*. That combination —
a claim of unambiguity resting on a source sentence that is ambiguous — is precisely
what a verification pass exists to catch, so it is an item rather than a note.

---

## Item 1 — FAIL · the ECZ K15 million is a **saving** in the source, a **price** in the piece

**Where.** EN §"What the teachers cost, and what the results say", final paragraph;
AR line 90; and the ZANIS `sources[]` title in **both** files' frontmatter.

**The piece says (EN):**
> The Examinations Council built its own in-house results-processing system for
> **K4.7 million**, against an estimated K15 million to procure it externally…

**The source says, re-fetched as served text 2026-09-08** (ZANIS `?p=1779`, ¶408):
> He further revealed that ECZ has developed a new in-house results processing system at
> a cost of 4.7 Million Kwacha, **a move that has saved Government about 15 Million
> Kwacha** that would have been spent on procuring an external system.

**The defect.** The source states a **saving of about K15 million**. The piece renders
that K15 million as the **external procurement price**. The two are the same number only
under one of the sentence's two available readings:

| Reading | External system costs | Net saving | Piece is |
|---|---|---|---|
| A — "the 15m that *would have been spent* [on procurement]" was avoided | K15m | K10.3m | correct |
| B — the *saving itself* was 15m | K19.7m | K15m | wrong by K4.7m |

Reading A is the more natural parse of the relative clause and is probably what ZANIS
means. But *probably* is not the standard. The source does not settle it, the piece does
not flag it, and the piece stakes the word **"unambiguously"** on it. Under **#23** (an
approximation has a direction — the source's own hedge is *about*) and **#22** (a
qualifier keeps its scope — *saved* is a scope, not a decoration), the fence must be in
the sentence.

**Aggravating, and the reason this is an item and not a note:** the AR carries the same
reading independently — *«مقابل تقديرٍ بخمسةَ عشرَ مليونًا لشرائه من الخارج»* ("against an
estimate of fifteen million to buy it from abroad"). Both languages assert the price
reading. A pair that is wrong in parallel is still wrong twice.

**Required fix (routes Editor → Content Creator → Arabic Editor):** render the figure in
the source's own grammar — a saving, attributed, hedged — in EN, in AR, and in both
`sources[]` titles. Do **not** compute K19.7m: that is reading B asserted, and we do not
adjudicate a source against itself (#38).

**Status: fix applied in-run 2026-09-08** (see the run's manager log). The piece
**re-enters the Verifier's queue behind the wave** for a confirmation read at the gate;
it does not flip on this verdict.

---

## Carried note A — learning poverty 99% is attributed to the mirror, not the owner

**Re-fetched 09-08** (UNESCO IICBA Zambia brief, served):
> Learning poverty… is estimated by **the World Bank, UNESCO, and other organizations**
> at [99 percent] — hyperlinked to a World Bank document.

The piece says *"UNESCO's institute for capacity building in Africa **puts** Zambian
learning poverty at 99 per cent."* IICBA **carries** the estimate; it does not make it.
Under **#40** (a mirror can misname the instrument) and **#44** (a converted figure has
two owners) the honest form names the estimating bodies and the register we read them in.

**Not escalated to an item**, on two grounds: the figure itself is confirmed exactly, and
IICBA is a UNESCO institute publishing a UNESCO brief, so "puts" is defensible as the
register's own voice rather than a misattribution to an uninvolved party. **Recorded for
the wave-gate read**, and recorded because the brief's very next sentence carries a
composition fact the piece omits:

> This is in part because out-of-school children are unlikely to achieve reading
> proficiency. But it mostly results from the fact that **98 percent of children enrolled
> in primary school could be learning poor.**

The 99% folds in out-of-school children, and the enrolled-child figure is itself hedged
(*could be*). The piece presents 99% as "a measurement that has not moved" with neither
its composition nor its vintage in the sentence. The vintage **is** in the `sources[]`
title (January 2024) and **is not** in the prose — the weakest vintage link in the piece
(#21, and #44's third corollary: the owner's own hedge anchors the vintage clause).

## Carried note B — the IICBA brief drifts against itself on its own vintage (#38)

Read from the served page's own markup on 09-08: `<meta name="description" content="January 2024">`
while the page's JSON-LD carries `"datePublished": "2024-10-21"` and
`"dateModified": "2024-10-21"`. The brief calls itself January 2024 and its own
structured data says October 2024. **Sixth instance of the #38 family.** Our
`sources[]` title says "vintage January 2024", which cites the brief's own description —
correct per #38 (a figure carries its page; cite the register). No change required;
banked so the next piece touching an IICBA brief does not rediscover it.

---

## Figure trace — every load-bearing figure, with its axes

Legend: **2ch** = confirmed through a second, independently-routed channel on 09-08.

### The statute (spine — traced to the Bill text via the recon's full read)
| Figure / claim | Axes checked | Verdict |
|---|---|---|
| s.15 "A child who is a citizen shall have the right to free education" | scope, position | quoted verbatim, 14 words as claimed |
| s.15(3) proof of citizenship at enrolment | scope | carried with its consequence (refugee settlements named) |
| s.15(4) 300,000 penalty units / 3 years / or both | scope, condition | penalty *ceiling* ("up to") carried correctly |
| s.119(1) admission + tuition + **accommodation** | scope | the expansion beyond 2022 is the claim, and it is the text |
| s.2 accommodation = bed space, bed and mattress | scope | verbatim |
| s.119(2) ministerial fee power, category undefined | scope | carried as an undefined category, not glossed |
| primary redefined grades 1–6; secondary forms 1–6 | position | the piece's central finding; in the text |
| Schedule conversion 30 May 2026 → 30 May 2031 | vintage | dates as served |
| eight key stages incl. day care 0–3, nursery 3–4, reception 4–5 | scope | as served |
| **Act number** | provenance | **correctly absent from both bodies** — recon bound it out (no gazette traced); the Bill number appears only in a `sources[]` title, which is the Bill, not the Act. Verified by grep: 0 hits in either body. |
| Assent 4 June 2026 | vintage | recon's non-date anchor (the President's 64th birthday) is a genuinely independent corroborant; 5 June readings are downstream drift |

### The audit (Auditor General / Committee report)
| Figure | Axes | Verdict |
|---|---|---|
| 2022–23 ESB published November 2024 (~2-year lag) | vintage, provenance | the government's own admission; this is what licenses the declension below |
| §2.6 CBD sampling; 61 districts, **27 responded (44%)** | coverage | arithmetic re-checked: 27/61 = 44.3% → "44 per cent" correct and **placed before** the audit's figures, not after |
| ECE 2,000 planned / **548** recruited | scope | 548/2,000 = **27.4%** exact |
| Primary 3,000 / 1,057 · Secondary 3,000 / 2,595 | scope | as printed |
| components **4,200** vs printed total **7,841** | **arithmetic** | re-summed independently: 548+1,057+2,595 = **4,200** ✔. Printed planned total 8,000 = 2,000+3,000+3,000 ✔ — so the planned column *does* add, which is what makes the recruited column an internal failure rather than a scope ambiguity we invented. 7,841/8,000 = **98.0%** ✔; 4,200/8,000 = **52.5%** ✔. The piece refuses to adjudicate and refuses to round — correct (#34). |
| 115 govt secondary = 69 + 36 + 10 | arithmetic | **115** ✔ |
| ZEEP 202 = 82 + 120 | arithmetic | **202** ✔ |
| **151** = 69 + 82 | arithmetic | **151** ✔ — and the piece's claim that this traces a speech figure to its two component programme lines is exactly what the sum shows |
| ZEEL 222 = 110 hub + 112 satellite | arithmetic, condition | **222** ✔; the qualifier *"all at different stages of construction"* **travels with the figure** (#19) |
| 1 ESO : up to 69 schools · 480 computers + 24 printers to 24 schools / 10 provinces (2021–24) · textbook ratio worse than 1:1 | scope, vintage | as served; "up to" preserved |

### The 2022 baseline (ministerial statement)
| Figure | Axes | Verdict |
|---|---|---|
| K1,994,817,600 budget line | vintage | 2022, stated |
| 100,877 applications vs **30,000 posts** | **funnel stage** | **the critical axis, and the piece nails it**: *"it reports 30,000 posts allocated. It is not a record of 30,000 teachers in classrooms, and the two are not interchangeable."* Announced ≠ measured, labelled at the figure (#14, #19) |
| Central 17,513/4,150 · Western 7,153/3,600 · Lusaka 5,318/740 | scope | as served |
| ratios 1:58 primary, 1:38 secondary vs standards 1:45, 1:35 | vintage, provenance | carried as *"announced figures, vintage 2022, with the underlying source unstated"* — provenance hedge **in the sentence** |

### The 2025 Grade 12 results — **2ch, re-fetched 09-08**
| Figure | Verdict |
|---|---|
| 136,434 full School Certificates | **2ch ✔** verbatim |
| 54,771 statements of results | **2ch ✔** verbatim, and correctly characterised as *"not a certificate"* |
| 194,148 sat | **2ch ✔** (source serves it as "194, 148" with a stray space — a typographic drift, not a figure drift) |
| 70.26%, up from 68.19%, first time above 70 | **2ch ✔** verbatim |
| denominator = entrants, not cohort | **the scope fence is in the claiming sentence** — independently re-derived: 136,434/194,148 = **70.27%**, which reproduces the announced 70.26% from the components and confirms the denominator the piece names |
| Minister's attribution to free education etc. | carried as *"an attribution, offered by an interested party, not a finding"* — correct |
| 8 days → 48 hours; Michael Chilala named | **2ch ✔** verbatim |
| K4.7m / K15m | **2ch — FAILS on type. See Item 1.** |

### The floor — **2ch, re-fetched 09-08**
| Figure | Verdict |
|---|---|
| learning poverty 99% | **2ch ✔** figure exact; **attribution + composition + vintage → Carried note A** |
| expected years of schooling 8.8 | **2ch ✔** verbatim |
| harmonised learning outcome 358 (scale 625 advanced / 300 lowest) | **2ch ✔** verbatim |
| learning-adjusted years = **5** | **2ch ✔**, and independently re-derived: 8.8 × 358/625 = **5.04** → the source's own "5 years". Two routes agree. |
| 40% of potential | **2ch ✔** verbatim |
| Grade 7 completion 97% (2019) → 86.4% (2020) | **2ch ✔** verbatim, **with the COVID cause the source gives**, and the source's own attribution to the 2020 ESB matches our `sources[]` title |
| Grade 9 pass 53%, Grade 12 64% | as served in the same brief |
| 2002 FBE Policy *"for grades 1 to 7"* | the hinge of the closing section; quoted, and the discontinuity claim is stated as *discontinuous, not false* — correctly bounded |
| general election August 2026 | named, with the recon's required posture ("positive about the statute, sceptical about the aggregates") visibly executed rather than asserted |

---

## Guardrail carriage (#19) — every recon §"MAY NOT USE" and every wall

| Recon guardrail | Carried in prose? |
|---|---|
| ❌ 2.3 / 2.5 / 2.6 million children returned | **YES, and better than avoidance** — the piece names all three ledgers, states that none discloses a base year or counting rule, and **declines the aggregate with the government's own audit as the citation**. Silent avoidance would have been a fail; this is the opposite of silent. |
| ❌ teacher totals (30,496 / 46,236 / "over 40,000" / "over 41,000" / "4,500 more") | **absent from both bodies** — verified by grep, 0 hits each |
| ⚠️ ESB series (5,538,681 / 5,936,505 / 6,527,980; 154,304 / 158,504) | **absent from both bodies in any form** — verified by grep, 0 hits each. The recon's own bite (the same teacher pair attached to two different year-pairs in two search summaries) stayed caught. |
| GIR 112.8% / NIR 55.2% | absent — search-stage only, correctly not laundered in |
| **§2.6 binding condition** on any use of the audit | **YES, and positioned before the audit's figures** rather than after — the reader meets the fence before the field |
| Political timing must be named | **YES**, with its own passage, and without letting it deflate the statute |
| Act number stays out | **YES** — 0 hits in either body |

**Guardrail verdict: 7 of 7 carried. No silent avoidance.**

---

## Mechanical checks

| Check | EN | AR |
|---|---|---|
| `approved:` | **false** ✔ | **false** ✔ |
| title code points (cap 100) | 34 ✔ | 31 ✔ |
| dek code points (cap 200, incl. tashkeel) | 177 ✔ | 191 ✔ |
| `related:` — 3 slugs | all 3 resolve in **both** collections, all 3 `approved: true` ✔ | identical set ✔ |
| hero still on disk | `/stills/2026-08-25-…svg`, 7,094 B ✔ | same asset ✔ |
| og raster card on disk | `/og/2026-08-25-…png`, 6,526 B ✔ (raster, not SVG) | shared ✔ |
| stale `approved: true` duplicate anywhere in repo (07-11 trap) | **none** — swept all 7 files bearing the slug ✔ |

### Numeral multiset, EN body vs AR body (the Sudan test, applied)
AR-only numerals: **none**. EN-only numerals: **7** — `2,000`, `30,000`, `15`, `12`, `9`, `7`, `70`.
Each traced into the Arabic body as a **spelled-out** form, which is correct Arabic
register, not an absence: `ألفين` · `ثلاثين ألف` · `خمسةَ عشرَ مليونًا` · `الثاني عشر` ·
`التاسع` · `السابع` · `سبعين`.
**Zero one-sided figures. Parity of substance holds (#42).**

---

## What would have had to happen for an error to survive

Per #27, a clean figure needs two independent routes. On this piece the drafter's
compose-time read (08-25) and my re-fetch (09-08) are fourteen days and separate
retrievals apart, and for the arithmetic figures a **third** route exists — the sums
themselves, re-computed here from the components without reference to either read
(4,200; 115; 202; 151; 222; 27.4%; 52.5%; 44%; 70.27%; 5.04). Item 1 survived the
drafter's read precisely because it is **not** an arithmetic or a transcription error:
the digits are right and the noun is wrong. That is the class of error two channels of
*figure* checking cannot catch, and only a read of the source **sentence** can.

**Method increment for the persona, filed to the guidebook this run:** trace the figure's
**type**, not only its value — a number's noun (price / saving / target / reached) is part
of the figure, and a piece that calls a figure *unambiguous* has taken on a burden the
source may not carry.

---

## Verdict

**FAIL WITH ONE ITEM.** Item 1 fixed in-run; the pair returns to the queue for a
confirmation read at the wave gate and **does not flip on this verdict**. Carried notes A
and B are recorded for that gate and for the guidebook, not for redraft.

The ceiling moves: with this verdict on file, **slot-3 drafting is unblocked** (3 banked,
1 verified). Sierra Leone is next in banking order.

— Verifier · 2026-09-08
