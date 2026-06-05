# Publish gate — 2026-06-04

Run in writing before staging the push, per the standing 3+1-gate checklist.

## What is being staged

No new article and no change to any article body (EN or AR). The live-site change is **discoverability infrastructure only**: a new `sitemap.xml` and `robots.txt` in `web/public/`. The rest of the commit is internal documentation (Arabic-original recon verdict, guidebook increment, this log, the daily brief, the stats snapshot).

Because nothing editorial ships to readers today, the editorial gates (Editor verdict, Arabic Editor verdict, hero stills on disk) are **not triggered** — there is no piece to clear. The build and integrity gates still apply to the site change and were run.

## Gate results

1. **Editorial verdict (Editor / Arabic Editor).** N/A — no piece shipped. The one editorial action today (the Saudi Arabic-original recon) ended in a **park**, documented at `content-drafts/verdicts/ar/2026-06-04-saudi-arabic-original-recon.md`. A park requires no live change. ✅ (correctly inert)
2. **Hero stills on disk.** N/A — no new piece. ✅
3. **Astro build clean.** Built via the /tmp route-around (the recurring vite-cache/FUSE EPERM on `node_modules/.vite` blocks an in-place build). Result: **23 pages, build complete, no errors.** `sitemap.xml` and `robots.txt` confirmed copied to `dist/` root. ✅
4. **AR full-pass where relevant.** N/A — no AR article changed. Parity unchanged at **10 EN / 10 AR, 100%.** ✅

## Integrity checks on the site change

- `sitemap.xml` parses as valid XML (`xml.dom.minidom`). ✅
- 23 `<url>` blocks = exactly the 23 built routes (2 homepages + about + 10 EN + 10 AR). ✅
- Bilingual `hreflang` alternates wired EN↔AR on the homepage pair and all 10 article pairs; `x-default` → EN. ✅
- `robots.txt` allows all and points to the absolute sitemap URL (`https://education3881.github.io/madar/sitemap.xml`). ✅
- Brand chrome unchanged this commit; spot-check confirms wordmark still inline SVG (no `<img src>`), `/madar/` base path correct on all links. ✅

## Verdict

**Cleared to stage.** Low-risk, additive, dependency-free. The sitemap is a static artefact and will go stale as articles are added — a weekly-review signal is logged to wire `@astrojs/sitemap` for auto-maintenance so this becomes a one-time route rather than a recurring hand-edit.

— Manager · 2026-06-04
