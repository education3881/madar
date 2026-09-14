# Growth audit — the corpus cannot be browsed by anything except date

**Date:** 2026-09-13 (weekly review) · **Desk:** Growth, with an editorial call owed to the Editor
**Status:** audit complete; this is the week's growth bet, briefed for the Web Developer + Editor from Monday 2026-09-14.

---

## The finding

`web/src/pages/` serves exactly seven route files. There is **no route in this publication that groups articles by anything** — not by country, not by region, not by theme. A reader who finishes the Sierra Leone piece and wants the rest of what we have written about Africa, or about teachers, has **no page to go to**. The editions index lists editions, chronologically. The related rail carries two or three hand-curated siblings. That is the entire navigation surface of a 38-piece bilingual publication covering 35 countries.

This is not a defect in anything — nothing is broken, every check is green. It is an **absence**, and absences are what the enumeration family of rulings keeps finding: a green check is scoped to what it enumerates, and no check enumerates *pages that ought to exist*.

## Why it is the right bet this week

Three dated `site:` observations (08-24, 09-04, 09-06) return zero URLs from the domain. Every discoverability *fix* the operation can make alone has now been made — robots, sitemap with lastmod, reciprocal hreflang clusters, JSON-LD on every page with a resolving publisher entity, both feeds with enclosures and cache validators, raster share cards, a branded 404, zero orphans. The remaining inbound levers are **all founder-gated** (domain, Search Console, Substack) or **founder-gated by one word** (IndexNow, built and staged off since 09-06, unanswered).

So the honest reading of last week's bet: **it could not be read, because its result depended on a word we do not control.** A bet whose outcome requires someone else's decision is not a bet; it is a request. This week's bet is chosen on the opposite criterion — *what can we build, ship and read entirely by ourselves?*

Taxonomy pages qualify, and they happen to be the single highest-value structure a text publication can add for discovery: they create new indexable URLs whose content is *entirely our own already-verified prose*, and they multiply internal edges, which is what a crawler walks.

## The arithmetic

| | Count | Note |
|---|---|---|
| Regions | **7** | every one holds ≥1 piece; MENA 15, Asia 7, Africa 5, Europe 5, LatAm–Caribbean 3, Oceania 2, N-America 1 |
| Themes worth a page | **8** | of 14 tags (see the vocabulary finding below) |
| Countries worth a page | **3** | Egypt, Sierra Leone, UAE — the only countries with ≥2 pieces |
| **Index pages per language** | **18** | |
| **New URLs (both languages)** | **36** | sitemap **82 → 118** |
| **New internal edges (both languages)** | **~140** | each edge is a link from an index page to an article |

At the Edition 05 flip the same structure compounds without new work: Africa moves 5 → 11 and becomes the second-largest region page in the publication, and Zambia, Sudan and Rwanda arrive on region pages that already exist.

## The vocabulary finding (the editorial call)

Running the taxonomy exposed something about the theme tags themselves. Of 14 tags across 38 approved pieces:

- **`government-led programs` is on 38 of 38 — 100% of the corpus.** A tag that is true of everything carries **zero information**. It is not a theme; it is a description of the publication's beat.
- `access` is on 34 (89%), `value of teachers` on 26 (68%). Both are closer to beats than to themes.
- At the other end, **three tags hold exactly one piece each** (`curriculum`, `inspiring stories`, `parent-led projects`). A page listing one article is a dead end in the exact sense `qa_body_links` was written to catch.

**Recommendation to the Editor — this is an editorial call, not a Growth one.** Build pages only for tags that *discriminate* (< 50% of the corpus) and are *non-trivial* (≥ 2 pieces): the eight in the table. Leave the three beat-tags in the frontmatter — they are honest, they are just not navigation — and let the one-piece tags accumulate until they are worth a page. The separate and larger question the Editor may want to take up: **a controlled vocabulary in which one term is always true needs revising, not just excluding** — a 100% tag has been carried on every piece since 2026-05-25 and has never once told a reader anything.

## Standing constraints these pages must honour (non-negotiable, from the register)

1. **Bilingual by construction.** Every index page exists in both languages, with reciprocal hreflang, or it does not ship — `qa_hreflang_clusters` (#9) will fail the build, correctly.
2. **Arabic labels come from the display layer**, `lib/i18n-geo` (the 08-23 fix — 52 countries, the region enum, all 14 theme tags already mapped). A new page must not reintroduce English controlled vocabulary into Arabic chrome; `qa_ar_language` now gates the deploy and will say so.
3. **Held pieces are invisible.** Every derivation over the content collection reads `approved: true` only (RUNBOOK, 2026-09-06). An index page that counts held drafts leaks both a slug and a date.
4. **Derived, never hand-listed** (#36, and the 2026-06-07 rule): these pages are generated from the collection at build time. A hand-kept list of slugs is correct the day it is written.
5. **Reachable and reciprocal.** Each index page needs an inbound path from the chrome or the editions index (`qa_reachability`), and the article pages should point back, or the edges run one way only.
6. **`lastmod` honesty.** These pages change when the corpus changes; the resolver must date them from the approved set, not from the chrome commit.

## How next Sunday reads this bet

Four numbers, all readable without anyone's permission: **index pages shipped** (target 18 per language), **sitemap URL count** (82 → 118), **internal edges added**, and **whether `qa_reachability` still reports zero orphans on the larger graph**. Indexing itself is *not* the reading — no instrument we own can attribute a crawl, and a `site:` query is an observation about a search product (#41). If the pages ship and the graph stays clean, the bet paid.

---

*Filed by Growth at the 2026-09-13 weekly review. Briefed to the Web Developer (build) and the Editor (which tags get pages, and whether a 100% tag survives the vocabulary).*
