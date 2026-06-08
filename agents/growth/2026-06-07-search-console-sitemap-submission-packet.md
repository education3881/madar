# Growth — Search Console + Bing sitemap submission packet (send-ready)

**Date:** 2026-06-07 · **From:** Growth → Vini (one action) · **Posture:** privacy-clean, no third-party tracker, discoverability only

## Why this, today

Today's QA pass independently re-verified the discoverability surface: **sitemap.xml is valid — 23 `<url>` entries, 66 hreflang annotations — and robots.txt sits at the dist root.** That is the precondition for the single highest-return, zero-tracker growth lever we have: getting search engines to crawl the bilingual surface correctly so the Arabic pages are indexed as Arabic and surfaced to Arabic searchers. Arabic is a distribution advantage, not a translation cost (charter, traffic loop §4). This packet turns that verified surface into one Vini action.

## The action (one-time, ~5 minutes, then it runs itself)

**Google Search Console**
1. Add property `https://education3881.github.io/madar` (URL-prefix property; GitHub Pages can't do domain-level DNS verification, so use the HTML-file or meta-tag method — the meta tag drops into `Base.astro` `<head>` once and is privacy-inert).
2. Sitemaps → submit: `https://education3881.github.io/madar/sitemap.xml`
3. Use URL Inspection on the Bo anchor piece (`/articles/2026-05-25-bo-teacher-chalk/`) and its Arabic twin to confirm both index under the right `hreflang`.

**Bing Webmaster Tools**
1. Add the same site; import from Search Console if you'd rather not re-verify.
2. Submit the same sitemap URL.

## What we read afterwards (return, not reach)

In the **weekly review**, not the daily — and only real, privacy-clean signals:
- Indexed-page count EN vs AR (target: 10/10 each indexed, no `hreflang` errors).
- Which **queries** surface us (the honest read on whether the primary-source, named-voice editorial line is what search rewards).
- Country distribution of impressions (does the Arabic surface reach Arabic searchers?).

No click-tracking, no analytics pixel, no visitor counter. Search Console reports are aggregate and engine-side — they do not put a tracker on a reader.

## Standing (unchanged, still one Vini-action each, non-blocking)

- **Issue 01 send-ready packet** — still staged, still a Vini action.
- **IG opening grid (nine tiles)** — still send-ready; cadence Mon/Wed/Fri.
- **Sierra Leone TSC piece** — distribution angle banked at commission (bidirectional internal cross-link with Uruguay/Ceibal; "teacher-deployment/matching" engagement-list segment, quiet posture). Activates when the piece clears the gate — which today's dossier shows is one allowlist-or-fetch step away, not a content step.

— Growth · 2026-06-07
