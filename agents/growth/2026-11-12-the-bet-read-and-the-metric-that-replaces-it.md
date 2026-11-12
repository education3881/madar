# Growth — yesterday's bet read on the origin, and the metric that has to replace it

**2026-11-12 · Growth · read without anyone else's permission, which is the only kind this operation sets**

## 1. The bet, read

Yesterday the growth function made two claims about what the 11-11 deploy would do to the one
discoverability signal this publication controls, and set one of them up as a **falsification test**.
Both are now readable on the live origin.

| Claim, made 2026-11-11 | Read 2026-11-12 on `education3881.github.io/madar/sitemap-0.xml` |
|---|---|
| *"The origin is serving THREE distinct `lastmod` dates across 138 URLs… The next deploy serves seventeen."* | **17 distinct dates across 138 URLs.** Forecast by differencing two sitemaps; confirmed by reading the served one. |
| *"The number to watch from now on is dates moved later with no byte behind them, which must be zero on every future deploy and is a build-visible falsification if it is not."* | **ZERO.** `qa_served_manifest --check` against the origin: 138 pages compared, 0 changed and dated, 0 presentation-only, **0 unbacked dates**, 0 new, 0 gone. |

**The falsification test passed its first contact with the world, which is the only contact that counts.**
A locally green build told us nothing about this yesterday: the question was whether a register committed
on one machine produces, through a deploy, the dates it predicted — and 2026-10-20 is the standing reason
that is not the same question.

## 2. Where the signal actually stands, by page kind rather than in aggregate

Aggregate distinctness flatters it. Grouped:

| `lastmod` | URLs | what they are |
|---|---|---|
| 2026-11-09 | **49** | **41 `/browse/` facet pages** + home + about + the Arabic home + 2 article pages |
| 2026-11-10 | 18 | article pages |
| 2026-10-16 | 10 | article pages |
| 2026-11-07 / 11-08 / 09-08 | 8 each | article pages |
| 2026-10-13 / 10-14 / 07-07 / 08-08 | 6 each | article pages |
| nine further dates | 1–2 each | article pages, and `/valence/` alone on 2026-10-31 |

So the 90 article pages are spread across **15 dates** and the 48 non-article pages are concentrated on
**one**, because a page with no source file of its own was seeded at the chrome ceiling and nothing has
changed its bytes since. **That is the declared seed and not a regression** — every one of the 138 entries
still carries `seeded: true` — but it is worth saying plainly that **one date covers 35.5% of the
sitemap**, which is the unreliable pattern this repair exists to end, surviving at a third of its old
scale.

## 3. THE METRIC THAT REPLACES DISTINCT-DATE COUNT, named now because the old one saturates

Distinct-date count went 3 → 17 in one deploy and **cannot go much further**: it is bounded by how many
dates the seed happens to hold, and it will drift up slowly whether or not the register is doing its job.
It is a proxy. The real quantity is in the register itself and it reads, today:

```
served_dates --check
  entries ..................... 138
  output-bounded ...............   0
  still seeded (declared error) 138
```

**Output-bounded of 138 — starting value ZERO, today.** A page becomes output-bounded the first time its
own served bytes really change, at which point its date stops being an estimate and becomes an
observation. The number can only rise, it rises exactly as fast as the publication actually changes
things, and **nobody outside this repository has to grant us anything to read it.** It is also the honest
denominator for any future claim about precision: the 28% figure measured on 2026-11-10 cannot be
recomputed until there are output-bounded dates to recompute it from.

Two things to watch beside it, both build-visible:

- **Dates moved later with no byte behind them: must stay 0 on every deploy** (carried from yesterday,
  and now with one clean reading behind it).
- **`seeded: true` entries: must only fall.** A rise means something re-seeded, which would discard
  observations and replace them with estimates — the exact thing `--seed`'s own refusal guard exists to
  prevent.

## 4. The facet surface, audited because the cluster pointed at it — a NEGATIVE RESULT

41 of the 49 pages sharing one date are `/browse/` facet pages, so the cluster raised a fair question:
are those pages any good as landing pages, or are they filler that a crawler collapses? Audited across
all **42** browse pages in `dist` (the 41 in the cluster plus the browse index):

| | |
|---|---|
| distinct `<title>` | **42 of 42** — none shared |
| distinct `<meta name="description">` | **42 of 42** — none shared, none missing |
| `<link rel="canonical">` | **42 of 42** present |
| hreflang alternates | **5 on every page**, EN↔AR reciprocal |
| `<h1>` present | **42 of 42** |
| served size | 19,242 – 32,465 bytes |

**Nothing to fix.** The descriptions are composed per facet and carry their own counts in their own
language (*«٣ مواد في مدار عن التعليم في مصر»*), which is the opposite of the templated near-duplicate
that gets a facet page dropped from an index. Reported rather than discarded, because a clean audit of a
surface nothing had ever audited is the only way the next run knows not to spend a day on it — and
because the measurement that sent us here was a date, not a defect: **a concentration in one signal is
not evidence of a weakness in the pages that share it.**

The facet surface does carry one deliberate gap, and it is not a defect: country pages exist only for
countries with **two or more** pieces, so five exist. A one-piece country page would restate its single
article. The bar is documented in the build and it is the same bar whose documentation a probe misread as
33 missing pages on 2026-10-20.

## 5. The action: the rail step, written into the gate that still exists

Item 72's measurement is three weeks old and its open half was never the sweep — it was *the step that
stops the defect regenerating*: a rail is curated when a piece is written, so every follow-up points back
and nothing ever points forward. **Added today to `_STANDING_LEDGER.md`'s eight-cell gate**, which is the
only commission template left now that editions have closed:

- **cell 1** — the Editor's brief names, by slug, the pieces this one follows up, and states the forward
  edge owed to each;
- **cell 8** — the flip commit adds those forward edges to the older pieces, both editions, within the
  proven 6-rail cap.

A flip that adds a backward rail and no forward one is now incomplete in the same way a piece without its
hero still is incomplete. **The first instance is on disk the same day**: today's Ofsted commission names
both Bahrain pieces and the two forward edges owed to them. This closes item 72's *regeneration* half;
the 22 declined backward edges stay open on their own terms.

**Traffic honesty, unchanged:** this site carries no third-party tracker by design. There are no visitor
numbers here and none are estimated. Every figure above is read from bytes this operation either serves
or commits.
