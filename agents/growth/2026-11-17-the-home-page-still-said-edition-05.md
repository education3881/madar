# Growth — the publication told every search engine it was Edition 05 for nine days after editions ended

**2026-11-17 · Growth · the day's one audience action.**
**Outcome readable without anyone's permission:** it is our own served bytes.

## What was wrong

Issue #13's default (option B) was applied on **2026-11-08**: editions closed at five, and pieces now
ship as singles against the standing ledger. `bahrain-bqa-five-cycles` shipped on **2026-11-09** and
belongs to **no edition**. The England piece in flight belongs to no edition.

And for the nine days since, the publication's chrome said otherwise, at page level:

| Surface | What it served | Pages |
|---|---|---|
| EN home `<title>` | `Madār · مدار — Edition 05` | 1, and it is the most-linked page we have |
| EN home `og:title` | the same string | 1 |
| EN + AR home top bar | `Edition 05 · 2026` / `الإصدار ٠٥ · 2026` | 2 |
| **the footer `issue` line, every page in the corpus** | `Edition 05 · 2026` / `الإصدار ٠٥ · 2026` | **139 of 139** |

A `<title>` is the string that reaches a tab, a link preview, a share and a search result. A reader or a
crawler arriving at the front door of a publication that had stopped publishing editions was told the
page *was* an edition — and then handed a list whose newest item is not in it.

## The two things that make this a defect rather than a stale label

**1 · The library already knew, and says so in its own comment.** `web/src/lib/editions.ts` derives
`hasOpenEdition` and carries the instruction *"Read `hasOpenEdition` before labelling it."* **Three call
sites on the two home pages read it** and correctly print *Latest edition* / *أحدث إصدار* above the
edition block. The `<title>` did not read it, and neither did the footer. So this was not an unknown
condition; it was a known condition with one named reader and four unnamed ones — **2026-09-20's *a count
in a heading is maintained by nobody unless somebody is named*, pointed at a label instead of a count.**

**2 · The two editions disagreed, and the Arabic was right.** The AR home's `<title>` is
`مدار — التعليم، بتأنٍّ، بلغتين` and **has never claimed an edition at all.** The EN title did. That is
#86's structure in the chrome rather than in an annotation: two editions, one claim, only one of them
capable of being wrong — and nothing we own compares the two titles, because `qa_pair_frontmatter` reads
articles and the home page is not an article.

## What was changed, derived rather than hardcoded

- `homeTitle` and `edPageLabel` (EN), `edPageLabelAr` (AR), and the footer's `issue` line all now read
  `hasOpenEdition`, exactly as the library's comment instructs and the three sibling call sites already did.
- **Page-level framing and edition-block framing are now different strings**, which is the actual fix.
  Inside the edition section `edLabel` is untouched and still reads `Edition 05 — Africa entire…`,
  because that block **is** Edition 05. The claim that was wrong was never *Edition 05 exists*; it was
  *this page is it*.
- The EN title, when no edition is open, is `Madār · مدار — Education, unhurried, in two languages` —
  composed to sit beside the Arabic strapline rather than translated from it, and built out of this
  publication's own published words about itself (*slow-cadence*, *in English and Arabic*, the About
  column). **No new identity was invented and no scope decision was taken:** issue #13 stays open, and if
  the founder sets a frame, one boolean flips and every one of these strings follows it.

## Measured, after

| | before | after |
|---|---|---|
| Served pages making a page-level `Edition 05` claim | **139 of 139** | **0** |
| Pages carrying the corrected label | 0 | **139** — 70 EN, 69 AR |
| Pages asserting `Edition 05` anywhere | 139 | **1** — the EN home's own edition block, which is correct |
| EN home `<title>` / `og:title` | `— Edition 05` | the strapline, and the pair no longer disagrees |

## Why this is the growth action and not a QA fix

It changes what a crawler, a share and a tab are told the publication is, on every page it serves, and
the lead string on the most-linked page. It needs no tracker to evaluate — **the site carries no
third-party tracker by design, and no visitor number is estimated here or anywhere.** What can be read
without permission is the bytes, and they are counted above.

## Carried forward

**The thing this action could not see, and it is the honest limit:** nothing compares the EN and AR home
pages' `<title>` to each other. The defect above was found by reading the served head by hand while
measuring something else entirely (a font payload), which is luck wearing the clothes of method. The two
front doors are a pair exactly as an article pair is, and `qa_pair_frontmatter` does not reach them.
Raised as standing-queue item **127**.
