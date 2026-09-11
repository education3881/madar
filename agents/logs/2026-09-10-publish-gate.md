# Publish gate — 2026-09-10, run in writing before staging

**Manager** · run before composing the push block, per the standing rule.

## Gate 1 — editorial verdict and approval
**Nothing ships editorially today.** No article added, no `approved` flag flipped.
- Corpus unchanged: **38 EN / 38 AR approved, 35 countries.**
- On disk: 41 EN / 41 AR — the three Edition 05 pairs remain `approved: false`.
- Sudan pair edited today (five fixes, both languages) under the Verifier's verdict; flag untouched, verified on disk in both files, no stale `approved: true` duplicate anywhere in or outside the build path (#18).

## Gate 2 — assets on disk
- Stills: present for all three held pairs, both languages.
- og cards: present, raster, for all three held pairs.
- Withheld from `dist` by the build hook — **6 assets for 3 held pieces**, logged by the hook, and independently re-asserted by `qa_held_assets` (assertion #12) with the control confirming all approved assets still serve.

## Gate 3 — build clean, in the judging environment
Built **twice** today, because the first build failed and the route-around cannot produce `lastmod`.

| Build | Environment | Result |
|---|---|---|
| 1 | route-around, pre-fix | **FAILED** — `heldAssets` died on `git rev-parse` outside a work tree |
| 2 | route-around, post-fix | exit 0 · 83 pages · hook withheld 6 assets |
| 3 | **real non-shallow clone, `CI=true`** | exit 0 · 83 pages · sitemap **82 URLs / 82 lastmod** |

Standing assertions against build 3's `dist` — **all ten clean**:

`qa_a11y_lang` PASS · `qa_ar_language` CLEAN · `qa_body_links` PASS · `qa_consumer_surface` CLEAN · `qa_hreflang_clusters` PASS · `qa_jsonld` CLEAN · `qa_lastmod` PASS (82/82, newest 2026-09-09, 76 approved / 6 held, held files contribute no date) · `qa_reachability` PASS · `qa_robots` PASS · `qa_held_assets` CLEAN.

Also: parity 38/38 · both feeds 38 items · **held-slug leak zero** across pages, sitemap, feeds and assets · **`qa_live_drift` CLEAN** against the origin (82 URLs, 0 lastmod drift, 4 sampled heads identical) — third consecutive clean read.

New assertion proved both ways (#35) before it was trusted:
- `heldAssets.resolveRepoRoot` — **control silent** on the real build; **bite loud** when the content probe is pointed at a directory that moved (`heldAssets: could not locate the content set…`).

## Gate 4 — Arabic full pass where relevant
Five edits made on the Arabic side today, **composed not translated**. Numeral multiset re-checked after every edit: **EN and AR identical, zero one-sided figures**; `2018` added to both sides so the symmetry survives. Deks: EN 192 / AR 178 code points, both under the 200 cap. The Arabic Editor's 09-03 transliteration sign-off is unaffected — no named human's rendering changed.

## Push-scope note
**No files under `.github/workflows/` were touched today.** This push needs an ordinary repo-scope token; the workflow scope is not required.

## Not shipping, recorded
- `qa_sources_alive.py` is a tool, **not wired into CI and deliberately not a deploy gate**. It runs weekly and before every wave gate.
- Its first finding — a hard 404 on a Sierra Leone source — is an **editorial** decision routed to the Editor for the confirmation read, not a build defect.

— Manager · 2026-09-10
