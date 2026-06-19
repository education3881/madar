# Memo — retire the hand-patched sitemap: `@astrojs/sitemap` integration recipe

**From:** Manager · **To:** Web Developer · **Date:** 2026-06-18
**Status:** Scheduled for the **06-25/26 buffer day** (or any clean Web-Dev checkout). **Not** to be attempted on a daily-ship day — see "Why not today."
**Trigger:** 5th consecutive hand-patch of `web/public/sitemap.xml` (06-08, 06-10, 06-16, 06-17, 06-18). Codified rule (RUNBOOK "Prevention rules", 2026-06-07): *generated artefacts that must mirror the article set are build-generated, never hand-maintained.* This memo turns the standing flag into a concrete, verifiable task.

## Why not today (the honest reason it keeps slipping)

The hand-maintained sitemap is not a thin file — it carries **per-URL hreflang alternates** (`<xhtml:link rel="alternate" hreflang="en|ar|x-default">`) for every page. A naïve `@astrojs/sitemap` drop-in emits a *flat* URL list and **loses those alternates**, which is a real bilingual-SEO regression — a worse sitemap than the one we have. Getting the alternates back requires the integration's `i18n` option, and our layout has one wrinkle: **EN lives at the site root (`/madar/…`) and AR under `/madar/ar/…`** — the default locale has no path segment. That has to be verified on the *actual* production build output, which a ship day cannot safely host. Hence: buffer day, against a clean checkout, in production mode.

## The recipe

1. **Install** (clean checkout, real `node_modules`):
   ```bash
   cd web && npm install @astrojs/sitemap
   ```
2. **Configure** `web/astro.config.mjs` — add the integration with i18n so alternates survive:
   ```js
   import sitemap from '@astrojs/sitemap';
   // …
   integrations: [
     sitemap({
       i18n: {
         defaultLocale: 'en',
         locales: { en: 'en', ar: 'ar' }, // ar pages are under /ar/; en at root
       },
       // optional: filter out any non-canonical routes if they ever appear
       // filter: (page) => !page.includes('/draft/'),
     }),
   ],
   ```
   `site` (`https://education3881.github.io`) + `base` (`/madar`) are already set, so emitted `<loc>`s will be correctly prefixed.
3. **Delete the static file** `web/public/sitemap.xml` (otherwise both ship and the static one shadows the generated `sitemap-index.xml`).
4. **Point robots at the index** — in `web/public/robots.txt`, set `Sitemap: https://education3881.github.io/madar/sitemap-index.xml` (the integration emits `sitemap-index.xml` + `sitemap-0.xml`, not `sitemap.xml`).

## Verification checklist (must all pass before commit)

- Build emits `dist/sitemap-index.xml` and `dist/sitemap-0.xml`; exit 0.
- **35 `<loc>` entries** (today's count) — EN + AR for every article, plus home/about/editions.
- **Each article URL carries en + ar + x-default `<xhtml:link>` alternates** with the right cross-language hrefs. This is the make-or-break check; if alternates are missing, the i18n config is wrong — do not ship, fall back to the hand file for that day.
- `<loc>`s all carry the `/madar/` base; no `localhost`, no `/ar/ar/` doubling, no 404 routes.
- `robots.txt` resolves to the new index URL.
- Diff the generated URL set against the last hand sitemap — they should match 1:1 (35 = 35).

## Fallback

If the i18n alternates can't be made to emit correctly in the time-box, **keep the static hand file** and close the loop a different way: a tiny build script that *generates* `public/sitemap.xml` from the content collection (same hreflang shape we maintain by hand) run as a `prebuild` step. That also satisfies the "build-generated, not hand-kept" rule without depending on the integration's i18n behaviour. Either path ends the hand-patch; pick whichever verifies clean first.

— Manager · 2026-06-18
