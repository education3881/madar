# Publish gate — 2026-10-31

**Why this gate runs although no flag moved.** A correction to a **published body** is editorial, and today
both editions of `2026-07-07-turkiye-earthquake-school-recovery` changed — including both deks — plus the
served labels on both home pages and the editions index. Served bytes changed on **135** documents. The
gate is written out a row per affected piece, per the standing rule.

## Rows

| Check | `turkiye-earthquake-school-recovery` EN | `turkiye-earthquake-school-recovery` AR |
|---|---|---|
| Editor verdict on file | yes — `content-drafts/verdicts/`, unchanged; this is a **dated follow-up under #41**, not a rewrite, so the original verdict governs | yes, unchanged |
| Arabic gate | n/a | **yes** — composed, not translated; the follow-up was composed against the same registers read today |
| Verifier verdict on file | yes, unchanged; the new figures are traced in this file below | yes, unchanged |
| Hero still on disk | yes — `/stills/2026-07-07-turkiye-earthquake-school-recovery.svg` | same asset, shared |
| Share card (raster) on disk | yes — `/og/2026-07-07-turkiye-earthquake-school-recovery.png` | same asset, shared |
| `dek` within 200 code points (tashkeel +1) | **181 / 200**, counted at compose per 07-27 | **158 / 200** |
| `title` within 100 | 39 / 100 | 31 / 100 |
| `approved:` | `true`, unchanged | `true`, unchanged |
| `npm run build` | exit **0** | exit **0** |
| 25 postbuild assertions | green | green |
| 12 build-job assertions (`build_job_gates`) | green | green |
| Held-slug leak | **zero** — 44 pairs, 44 approved, 0 held | zero |

## Figure trace for everything added today

Every quantity below was read in **served text** today from MoNE's own register,
`https://www.meb.gov.tr/asrin-gayreti-maarifin-iyilestirici-gucu-raporu-yayimladi/haber/39744/tr`
(published **6 February 2026**, 161 pages, thirteen chapters), and appears in **both** bodies and in the
`sources[]` annotation of both editions.

| Figure | What it is | Status |
|---|---|---|
| 11,567 / 119,200 | schools / classrooms in the eleven provinces before 6 Feb 2023 | as read |
| 10,272 / 109,401 | schools / classrooms undamaged or lightly damaged after | as read; 119,200 − 9,799 = 109,401, internally consistent |
| 1,295 / 9,799 | schools / classrooms rendered unusable | as read — **revises the piece's earlier "about 9,500"**, which was the ministry's own Feb 2025 figure |
| 14,202 | classrooms completed | as read — **supersedes the podium's 14,304** (#43) |
| 655 / 8,648 | schools / classrooms under construction | as read |
| 70 / 2,352 | schools / classrooms being strengthened | as read |
| 915 / ~72 bn lira | completed projects / value at today's prices | as read |
| ~85,000 | lightly damaged classrooms repaired | as read |
| 233 / 2,965 | schools / classrooms strengthened rather than replaced | as read |

**Not reconciled, and said so in the body rather than smoothed:** the agency's *9,763 under construction*
against the report's *8,648 + 2,352*. Both are printed, each attributed to its own register, and the
ranking is stated (#43). **No composite was formed and nothing was averaged.**

**Carried as a hedge, per the open-register rule (09-13):** the report is dated **seven months before** the
September 2026 deadline it cannot speak to, and the body says so.

**Deliberately not written:** the possible restatement of the surplus target from 10% to 15%. It exists
only in a search summary. *A figure is cited as read.* Queued as item 61.

## Identity tokens (#112)

| Token | Verdict against served bytes |
|---|---|
| `Asrın Gayreti: Maarifin İyileştirici Gücü` | **found** |
| `9 bin 799 derslik ise kullanılamaz hâle geldi` | **found** |
| `14 bin 202 dersliğin yapımı tamamlandı` | **found** |
| the Arabic rendering of the report's title | `script-mismatch` — declined per #112, as the asymmetry predicts |

Coverage: `qa_claim_registers --check` CLEAN at **353** registers with a dated observation;
`qa_citation_identity --check` CLEAN at **231** quotation-bearing registers with a dated reading.

## Non-editorial served changes in the same push

| Surface | Change | Verified |
|---|---|---|
| `/madar/valence/` | 13 heading elements `h4` → `h3` with their ID-scoped selectors | rendered probe: only `tagName` differs across 13 computed properties |
| EN + AR home pages | kicker *Current edition* / *الإصدار الحالي* → *Latest edition* / *أحدث إصدار* | both strings now appear in **zero** files in `dist`; masthead and piece count untouched |
| `/madar/editions/` | Edition 05's *Current* tag removed | 0 `edition__tag` in `dist`, driven by the flag (proved both ways) |

## Verdict

**PASS.** Nothing held. No flag moved. Both editions of the Türkiye pair carry the same corrected figures
from the same register read the same day, in both languages.
