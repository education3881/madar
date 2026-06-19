# Publish gate — 2026-06-18 — Egypt NPDA / Arabic literacy (EN + AR)

Run IN WRITING before staging. Slug: `2026-06-18-egypt-npda-arabic-literacy`. Sprint piece 5 of 10.

## Gate items (RUNBOOK §3)

- [x] **Editor verdict = APPROVE**, on record: `/content-drafts/verdicts/2026-06-18-egypt-npda-arabic-literacy.md`. Five-test rubric passed line by line; channel-attribution caveat held in print (not laundered).
- [x] **Arabic-Editor sign-off**, on record: `/content-drafts/verdicts/ar/2026-06-18-egypt-npda-arabic-literacy.md`. Named-human transliterations verified (نجلاء راغب, فيروز); the unverified minister quote correctly **cut**, not restored. First piece on the compose/verify split (Arabic Content Creator composed; Arabic Editor verified).
- [x] **Article md present, `approved: true`** — EN `web/src/content/articles/2026-06-18-egypt-npda-arabic-literacy.md`; AR `web/src/content/articles-ar/2026-06-18-egypt-npda-arabic-literacy.md`.
- [x] **Hero still on disk, in the same commit as the text** — `web/public/stills/2026-06-18-egypt-npda-arabic-literacy.svg` (6.2 KB; the spoken-marks → written-word bridge, one ink subject + the single kiln-orange "bridge" gesture — Korea's exclusionary orange inverted into a connective one). Asset-with-text invariant honoured: still + AR written to disk immediately after the EN text, before this gate.
- [x] **Clean build** — real `astro build` via the tmpfs/`VITE_CACHE_DIR` route: **exit 0, 35 pages**, both Egypt pages generated. No schema rejection (deks under cap).
- [x] **QA spot-check on built `dist/`** — see `agents/logs/qa-2026-06-18.md`. Parity **15 = 15**; hero still in `dist/stills/`; related rail resolves to Iqra/Kuwait/Sierra Leone; wordmark inlined; caption "Curated 13", zero drift.
- [x] **Sitemap mirrors the article set** — hand-patched to **35 urls** (Egypt EN+AR; homepage `lastmod` → 06-18). Parity re-validated. Integration recipe written for the buffer day (memo on record).

## State note (honest)

- Opened on `555f586` (Korea, deployed clean); local HEAD == origin/main at start of run; working tree clean. **No missed day** — 06-17 ran and pushed. Re-checked `git fetch origin` before composing the push block (push-race protocol): origin unmoved.
- The piece is Egypt's **second** appearance (after the 06-05 Knowledge Bank piece). Distinct subject + slug; country count holds at 12, stated honestly in the brief's statistics panel rather than inflated.

**Verdict: GREEN — cleared to stage.** No push from the sandbox; Vini holds the push.

— Manager · 2026-06-18
