# Publish gate — 2026-06-05

**Run by:** Manager, in writing, before staging the push (per charter §3).
**Scope of this push:** folds in the un-pushed 2026-06-04 work (sitemap.xml, robots.txt, Saudi Arabic-original park, ECE source-index guidebook, brief 07) **plus** today's 2026-06-05 work (nine IG tiles, Issue 02 Sierra Leone recon, render-method guidebook, brief 08). **No new article ships** — content advance is recon + assets, so the article-level gate is N/A this run; the build/QA and brand-chrome gates still apply in full.

---

## Gate 1 — Editorial / content
- **No fresh article in this push.** Saudi remains parked (verdict on record, 2026-06-04). Issue 02 Sierra Leone NDLS logged as a recon candidate only — explicitly *not* commissioned. → **No article gate to clear; pass by N/A.**
- Quality-over-slot honoured: nothing thin manufactured to fill a slot.

## Gate 2 — Designer assets
- Nine opening-grid tiles present at `/design-assets/instagram/opening-grid/tile-01…09.png`, 1080×1080. Verified on a 3×3 contact sheet — coherent, on-brand, wordmark + divider read correctly. → **Pass.**
- These are social assets, not site assets; they do not affect the deploy surface.

## Gate 3 — Web Developer build + QA
Build run via the /tmp route-around (the recurring `node_modules/.vite` EPERM FUSE boundary blocks in-place build — routed around, not fought):
- `astro build`: **23 pages, complete, no errors.**
- `sitemap.xml` + `robots.txt` confirmed at dist root; sitemap **validates as XML**; 23 `<url>` entries; **66 hreflang alternates** (each EN page wired to its AR twin and back).
- Brand chrome: **0** `<img>`-based wordmarks; inline SVG wordmark present on home. → intact.
- Base path `/madar/` correct on home links.
- EN/AR parity: **10 / 10.**
- Orphan/placeholder scan: **0** hits (`lorem`/`TODO`/`FIXME`/`placeholder`).
→ **Pass.**

## Gate 4 — Arabic Editor
- No new or changed Arabic article in this push (10/10 parity unchanged; last AR full-pass 2026-05-29, Bo + UAE Madrasa name corrections on record). → **No AR change to verify; pass by N/A.**

---

**Verdict: cleared to stage.** The push changes the live site only by adding `/sitemap.xml` and `/robots.txt` at the root (additive, dependency-free) — already validated above. All other 2026-06-05 outputs are repo artefacts (tiles, memos, guidebook, brief) that do not alter the deploy surface.

— Manager · 2026-06-05
