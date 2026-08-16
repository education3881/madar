# Growth — Edition 05 head-terms surface audit: the aggregator gap
**Filed:** 2026-08-16 · Growth (briefed by the Manager) · in-control step, no founder action needed
**Trigger:** today's recon 6 discovered that the single highest-intent query for the Africa edition is owned end-to-end by low-quality composite-ranking sites. That is not just an editorial problem — it is the clearest discoverability opening the corpus has found.

## The finding
The query **"best education system in Africa"** and its family return, on the first screen, a tier of composite-ranking aggregators (`worldpopulationreview.com`, `pulse.com.gh`, `matsh.co`, `capmad.com`, `allafrica.com` listicles). Every one of them:

- publishes an ordinal with **no formula, no weights, no vintages, no comparison set** (the defect ruling #29 was filed for today);
- **recycles the same underlying ordinal**, each citing the last;
- contains **no primary source, no named ministry register, and no traceable figure**;
- and is **checkably wrong in at least one place** — crowning South Africa in the same window South Africa's own DBE published its grade-5 pupils last of 58 in TIMSS 2023.

Nobody serious is answering this question on the open web. The institutional registers that *could* answer it (World Bank HCI briefs, CONFEMEN/PASEC, DBE/HSRC national reports) do not compete for the query — they publish PDFs and index pages, not answers to the question a parent or a regulator actually typed.

**That gap is the opportunity.** A primary-sourced, ruler-first piece is not competing with the World Bank; it is competing with `matsh.co`. That is a fight the corpus wins on quality.

## The surface, classified
Head terms split cleanly into three tiers, and only one is worth pursuing.

| Tier | Example queries | Who owns it now | Winnable? |
|---|---|---|---|
| **A — aggregator-owned** | best education system in Africa · top 10 education systems in Africa · most educated country in Africa · which African country has the best schools | Composite-ranking listicles, no primaries | **Yes.** The incumbent tier has no defensible quality floor. This is the target. |
| **B — institution-owned** | human capital index · PASEC 2019 results · TIMSS 2023 results | World Bank, CONFEMEN, IEA | **No, and we should not try.** We cite these; we do not outrank their own data. |
| **C — long-tail, unowned** | learning-adjusted years of school Africa · why do education rankings disagree · which African country improved most in TIMSS · PASEC between-school inequality | Nobody — thin or no results | **Yes, cheaply.** These are the piece's own section-level claims. Low volume, high intent, zero competition. |

Tier C matters more than it looks: those are the queries a ministry adviser or a researcher types, which is Madār's actual reader. Tier A brings the volume; Tier C brings the reader who returns — and **return rate, not reach, is the metric that governs** (Charter §Growth).

## On-page requirements for the best-system piece
Handed to the Editor and the Web Developer now, so they land with the piece rather than being retrofitted:

1. **The title must answer the question, not evade it.** The piece's honest answer is "it depends on the ruler" — but a title that *only* says that loses to a listicle. Recommended shape: a named crown plus the correction, e.g. a title that carries **Mauritius** and the ruler in the same line. Editor's call; the requirement is that a reader scanning results sees an answer, not a riddle.
2. **Dek carries a number.** The existing dek cap is 200 characters (schema-enforced). One concrete figure inside it — 9.4 learned years out of 12.4 expected — separates the piece from every listicle on the page at a glance.
3. **The four rulers become four semantic subheads**, each phrased as the query a reader would type. This is what makes Tier C free rather than a separate content investment.
4. **Every figure keeps its source link inline**, per house style. The differentiator against the aggregator tier is literally visible traceability — it should be visible above the fold.
5. **A comparison table in HTML, not an image.** The Mauritius/Kenya table in the recon is the single most extractable asset in the piece. As markup it is machine-readable; as a PNG it is invisible.
6. **`region: Africa` + `country:` set correctly** — the piece names several countries; the frontmatter `country:` should carry the crowned one (Mauritius) so the corpus's country count stays honest and the Africa cluster wires cleanly.

## Internal-link wiring (extends the 2026-08-13 pre-wire audit)
The best-system piece is the **hub node** the Africa cluster has been missing. The 08-13 audit found 9 live Africa pieces with 2 orphans (`2026-05-28-ghana-cbe-curriculum`, `2026-05-27-egypt-ekb-decade`) and 2 one-way edges.

This piece resolves both orphans at once, because it has a natural reason to reference Ghana and Egypt — they are the two countries the discredited aggregator ordinal crowns, and the piece can point at each with a real editorial reason rather than a manufactured "related" link. Recommended edges at integration:

- **best-system → Ghana (`ghana-cbe-curriculum`)** and **best-system → Egypt (`egypt-ekb-decade`)** — the two orphan nodes, entered on merit.
- **best-system ↔ Sierra Leone (recon 4 piece)** — reciprocal; both are about instruments that measure honestly.
- **best-system ↔ Sudan (recon 5 piece)** — reciprocal; the delivery counterpart.
- **best-system → the Ed04 measurement cluster** — the arc bridge (Ed04 measured the child; this measures the system). First edge in the corpus to link three editions.

Projected at landing: **Africa cluster 9 nodes / 2 orphans → 14 nodes / 0 orphans, all reciprocal.**

## Measurement, stated honestly up front
The site carries **no third-party tracker, by design** — so this audit predicts nothing and promises nothing about traffic. What it does is make the piece *eligible* to be found. The privacy-clean signals that will actually read the result — Substack opens, return rate, country distribution, attributable inbound shares — switch on when Issue 01 sends, and are read in the weekly review, never invented in a daily.

**The one thing to watch when signal exists:** whether Tier-C queries bring readers who return. A listicle-driven visitor bounces; an adviser who searched "learning-adjusted years of school Africa" is the reader the publication is for.

## Status
Staged, no corpus change today. Requirements ride Ed05 integration through the publish gate. Two open founder calls unchanged and unblocking: **custom domain**, **Substack account**.
