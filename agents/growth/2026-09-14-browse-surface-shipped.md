# Growth — the browse surface shipped, and the four numbers the bet is read on

**Date:** 2026-09-14 · **Desk:** Growth (build by the Web Developer, in-run) · Bet of the week set at the 2026-09-13 weekly review
**Audit of record:** `agents/growth/2026-09-13-taxonomy-index-audit.md`

---

## The four numbers the audit said Sunday would read

| Reading | Target | Shipped | |
|---|---|---|---|
| Index pages per language | 18 | **19** (18 facets + the hub) | the hub was not in the audit's count and is not optional: it is the only page the header can link to |
| Sitemap URLs | 82 → 118 | **82 → 120** | +38, two more than forecast, for the same reason |
| New internal edges | ~140 | **500** | **140 into articles** — the audit's forecast, exactly — plus **360 between index pages**, which the audit did not count |
| `qa_reachability` on the larger graph | zero orphans | **zero orphans on 120 pages** | the bet's own pass condition |

**The bet paid on its own terms, and all four numbers were readable without anyone's permission** — which was the criterion the bet was chosen on, after last week's IndexNow bet turned out to depend on a word we do not control.

## What shipped

- `/browse/` and `/ar/browse/` — the hub, grouping the corpus three ways.
- 7 region pages, 8 topic pages, 3 country pages, per language.
- `src/lib/taxonomy.ts` — the facet set, **derived from the approved collection at build time**, never hand-listed (#36, and the 2026-06-07 rule). The selection thresholds are computed against the live corpus, so the page set grows with the corpus: at the Edition 05 flip Africa moves 5 → 11 and becomes the second-largest region page in the publication, and Zambia, Sudan and Rwanda arrive on a page that already exists. Nobody edits anything.
- A `Browse` / «تصفّح» item in the site header, in **both** the home nav and the **article** nav.

## Three decisions worth recording

**1. The article nav, not just the home nav.** The reader who wants more of a subject is the one who has just finished a piece about it. Putting the link only on the home page would have made the surface reachable and unused.

**2. The hub is the whole reachability story.** Thirty-eight new URLs, and exactly one inbound path into them from the rest of the site. That is the VALENCE shape of 2026-08-25 — a page in the sitemap that nothing linked to, reachable for seventeen days only by someone who already knew the URL — and the reason the header change is not cosmetic. A sitemap entry is a declaration; a link is an edge.

**3. Each language derives its own facet set.** The alternative — deriving from English and reusing the slugs — would have been simpler and would have hidden a divergence if one ever appeared. As built, if the two collections ever disagree about which facets exist, the hreflang cluster for the odd page names a URL that is not in dist and `qa_hreflang_clusters` (#9) fails the build. The divergence *is* the defect and it should be loud.

## The editorial call is still the Editor's, and it got sharper today

The audit recommended pages only for tags that discriminate, and the build honours that: `government-led programs` (38/38), `access` (34/38) and `value of teachers` (26/38) get no page, because a page listing the whole corpus is the editions index with extra steps.

Today added an argument the audit could not have made. **The piece drafted this run is about measurement — four rulers, four crowns, an argument that a number without its instrument is an opinion with decimal places — and the vocabulary has no tag for assessment.** It was filed under `government-led programs, access, value of teachers`: three true tags, none of which is what the piece is about, and the first of which is true of every piece we have ever published.

That is no longer a browse problem. It is a statement about what this publication can say about itself. **Recommendation to the Editor, restated and now with an instance:** the controlled vocabulary needs a term for *measurement and assessment*, and it needs to lose or demote a term that has been true 38 times out of 38 since 2026-05-25.

## Not claimed

No traffic figure, no indexing claim. The site carries no third-party tracker by design, and a `site:` query is an observation about a search product, not a measurement of this one (#41). The fifth dated `site:` observation still returns zero URLs from the domain; every discoverability lever the operation can pull alone has now been pulled, and the remaining ones are founder-gated (domain, Search Console, Substack, IndexNow's one word).

— Growth · 2026-09-14
