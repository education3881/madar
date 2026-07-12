# Growth · post-outage discoverability audit + one Web-Developer action
**Date:** 2026-07-11 · **Manager (Growth function)** · **Trigger:** the site recovered from a week-long outage on 07-07; 12 URLs are new to the live crawl. Before pushing for re-crawl, confirm the discoverability surface the crawler will meet is clean — and bank one cheap improvement.

## Why this, today
Growth leads with **quality of the discoverability surface**, not raw counts (Charter). The single highest-leverage *founder* action remains the **Search Console sitemap resubmission** (still standing from Brief 29 — surfaces the twelve outage-stranded URLs at once). This note does the part the operation owns: audit what the recrawler will actually read on a live page, and file the one improvement worth making before the crawl lands.

## Audited live (Morocco, 2026-07-06 — a representative recovered page)
Fetched the live HTML and read the `<head>` + body discoverability surface. **Clean on every count that matters for indexing:**
- **`<title>`** distinct and descriptive ("The label that can be refused — Madār"). ✓
- **`<meta name="description">`** present, unique, matches the dek (no boilerplate duplication). ✓
- **`<link rel="canonical">`** self-referential and correct (the outage's stale-cache risk would have shown here). ✓
- **Open Graph + Twitter card** complete: `og:type=article`, `og:title/description/url/image`, `twitter:card=summary_large_image`. Shares will unfurl with the hero still. ✓
- **`<meta name="robots" content="index, follow">`** — explicitly indexable. ✓
- **Brand chrome intact:** the wordmark is **inlined SVG** in the header (not `<img src>`), so it survives even if an asset path 404s — the exact rule from the 06-10 Iqra incident, holding on live pages. ✓
- **Sources** render as a real `<ol>` of primary-source outbound links (ministry PDFs, World Bank, CSEFRS, J-PAL/MEL) — the citation density search engines and serious readers both reward. ✓
- **Bilingual signal present** via the sitemap's `xhtml:link rel="alternate" hreflang` pairs (verified in `sitemap-0.xml`, EN↔AR reciprocal for all 30 pairs) **and** an in-body `<a hreflang="ar">النسخة العربية ↗` cross-link. ✓

## The one action to file for the Web Developer (P2 — enhancement, not defect)
**Add `<link rel="alternate" hreflang>` pairs to the page `<head>`.** Google reads hreflang from three places — HTTP headers, `<head>` `<link rel="alternate">`, or the XML sitemap. Madār currently supplies it via **the sitemap + in-body anchors only**; the `<head>` carries none. The sitemap method is valid and sufficient, so this is **not** a defect and nothing is mis-indexed. But head-level alternates are the most widely-honoured signal and are near-free to emit from the same collection data the sitemap already uses:
```
<link rel="alternate" hreflang="en"        href="…/articles/<slug>/" />
<link rel="alternate" hreflang="ar"        href="…/ar/articles/<slug>/" />
<link rel="alternate" hreflang="x-default" href="…/articles/<slug>/" />
```
Emit on every article page (EN and AR) and on home/editions. Bilingual reach is Madār's structural discoverability advantage (Charter §traffic-loop 4) — belt-and-suspenders hreflang makes the AR corpus maximally findable to Arabic-language search with one small layout change. **Definition of done:** each EN page's head names its AR alternate and x-default, and vice-versa; build stays clean; parity holds. Brief it into the next Web-Developer integration window; no rush — it can ride the Ed04 ship commit.

## One cosmetic observation (P3 — low)
The article kicker renders as `Curated · Curated` (type and section both surfacing "Curated"). Reads slightly redundant; candidate to show `Curated · Edition NN` or a single label. Non-urgent, purely cosmetic; parked for a Web-Developer polish pass, not worth its own commit.

## Standing founder lever (carried, not new)
**Search Console → resubmit `sitemap-index.xml`.** Thirty seconds; converts two weeks of outage-stranded work into crawlable, discoverable pages. Unchanged from Brief 29; still the highest-return single action this week. No metrics invented — return rate, not raw counts, is the number that matters, and it switches on when Substack opens.
