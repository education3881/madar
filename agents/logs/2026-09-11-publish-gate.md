# Publish gate — 2026-09-11 (run in writing before staging the push)

**Manager · run at the close of the daily operation. Nothing ships editorially today.**

## Gate 1 — Editor verdict + `approved: true`

**N/A — no piece flips today.** The corpus is unchanged at **38 EN / 38 AR approved**, 35 countries. The three Edition 05 pairs (Zambia, Sierra Leone, Sudan) remain `approved: false`, held for the wave gate. No `approved:` field was touched in this run.

Slot 3 (`africa-best-system-ruler`) advanced by **research only** — draft-blocker 2 closed. No draft exists; nothing to gate.

## Gate 2 — hero stills and share cards on disk

**N/A for new pieces — none.** The three held pairs have their stills and og cards on disk and **correctly withheld from `dist`** by the build hook (6 assets, 3 pieces, logged by name at build time). `qa_held_assets` CLEAN: no held piece contributes bytes; every one of the 76 approved assets still serves.

## Gate 3 — clean build + QA

Run in a **real git clone** at `/tmp/mclone-20260911`, working tree copied over it byte-for-byte, `CI=true` — the judging environment (#16), and the environment the 09-10 run could not reach.

| Check | Result |
|---|---|
| `astro build` (pre-fix) | **exit 0**, 82 pages |
| `astro build` (post-fix) | **exit 0**, 82 pages |
| EN / AR parity | **38 / 38 approved**, 41 / 41 files |
| Sitemap | 82 URLs, **82 `lastmod`** |
| Feeds | EN 38 items / 38 enclosures · AR 38 / 38 |
| Held-slug leak (pages, sitemap, feeds, assets) | **0** across all three slugs |
| `qa_a11y_lang` | PASS |
| `qa_ar_language` | CLEAN (235 chrome fields) |
| `qa_body_links` | PASS |
| `qa_consumer_surface` | CLEAN |
| `qa_held_assets` | CLEAN |
| `qa_hreflang_clusters` | PASS — 82 sitemap URLs, 40 clusters, 2 named no-alternate |
| `qa_jsonld` (**extended today**) | **BITE FAIL(228) on pre-fix · CLEAN on fixed** — 308 nodes, 608 promises, 306 references resolved |
| `qa_lastmod` | PASS — 82/82, **held files contribute no date** |
| `qa_reachability` | PASS — 0 orphans |
| `qa_robots` | PASS |
| `qa_live_drift` | **CLEAN** — origin matches dist, 0 lastmod drift, 4 sampled heads identical |

**Ten standing assertions green after the change**, re-run as a regression set.

## Gate 4 — Arabic full-pass

**N/A** — no Arabic article was composed, edited or flipped. The AR front door gained two JSON-LD nodes; both are language-neutral identity nodes (`Organization`, `WebSite`) carrying the publication's own attested names — `name: "Madār"`, `alternateName: "مدار"` on the Organization; `name: "Madār · مدار"` on the WebSite. No Arabic prose, no transliteration, no named human. `qa_ar_language` re-run and CLEAN, which is the assertion that would catch Latin-script vocabulary leaking into Arabic chrome.

---

## Drift statement — what the reader sees change

**Nothing editorial.** The push carries:

- **Served bytes that change:** the `<head>` JSON-LD of 76 article pages (two nodes added, one field corrected) and of the two front doors (two nodes added, where there were none).
- **Served bytes that do not change:** every word of every article, every image, the sitemap, both feeds, all chrome.

The 09-10 day's work carried in this same push (Sudan verdict fixes, `heldAssets.mjs` root resolution, `qa_sources_alive.py`, ruling #47) changes **no served bytes at all** — the Sudan article edits are on held files, which is why `qa_live_drift` read CLEAN against the origin *before* today's structured-data change. One day unpushed cost the reader nothing; it cost the operation only the delay.

## Push-scope warning

**This commit touches `.github/workflows/astro-pages.yml`** (one new QA step: `qa_jsonld` becomes a deploy gate). The push therefore needs the **`workflow`-scope PAT**, not a plain repo-scope token. Flagged in the brief's push block per the standing note.

---

**Verdict: CLEAR TO STAGE.** Nothing ships editorially; the corpus is unchanged; the build is clean in the judging environment; the one behavioural change to the live site is additive, asserted, and proved both ways.

— Manager, 2026-09-11
