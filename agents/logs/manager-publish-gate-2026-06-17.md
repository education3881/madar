# Publish gate — 2026-06-17 — Korea AIDT reversal (EN + AR)

Run IN WRITING before staging. Slug: `2026-06-17-korea-aidt-reversal`.

## Gate items (RUNBOOK §3)

- [x] **Editor verdict = APPROVE**, on record: `/content-drafts/verdicts/2026-06-17-korea-aidt-reversal.md`. Unparks the 06-12 park; five-test rubric passed line by line.
- [x] **Arabic-Editor sign-off**, on record: `/content-drafts/verdicts/ar/2026-06-17-korea-aidt-reversal.md`. Six named-human transliterations verified; the three-way "Lee" collision (President Lee Jae-myung / Minister Lee Ju-ho / teacher Lee Hyun-joon) role-qualified on every mention.
- [x] **Article md present, `approved: true`** — EN `web/src/content/articles/2026-06-17-korea-aidt-reversal.md`; AR `web/src/content/articles-ar/2026-06-17-korea-aidt-reversal.md`.
- [x] **Hero still on disk, in the same commit as the text** — `web/public/stills/2026-06-17-korea-aidt-reversal.svg` (6.1 KB; book-and-tablet, one ink subject + the single kiln-orange "redrawn definition" gesture). Asset-with-text invariant honoured.
- [x] **Clean build** — real `astro build` via the tmpfs/`VITE_CACHE_DIR` route: **exit 0, 33 pages**, both Korea pages generated. (Gate caught one real defect first: AR + EN deks over the 200-char schema cap → both trimmed, rebuilt clean.)
- [x] **QA spot-check on built `dist/`** — see `agents/logs/qa-2026-06-17.md`. EN/AR article parity **14 = 14**; hero still in `dist/stills/`; related rail resolves to Uruguay/Indonesia/Qatar; caption register-style **"Curated 12"**, zero `Issue 0x` drift; homepage rebuild (founder's cover-removal) builds clean, wordmark still inlined.
- [x] **Sitemap mirrors the article set** — hand-patched to **33 urls** (Korea EN+AR added, lastmod 2026-06-17). Third consecutive hand-patch; `@astrojs/sitemap` re-flagged for the weekly.

## State note (honest)

Working tree opened with two **uncommitted founder edits** (homepage EN+AR, 06-16 09:05, *after* that day's commit): the edition cover SVG removed from the current-edition block. Read as the founder's hands-on edit (consistent with the 06-15 editions live-editing pattern; Manager stays out of `web/`). Verified it builds clean and is coherent (covers retained in the previous-editions strip). **Preserved, not reverted**; swept into today's commit. The off-ops-vs-hands-on working agreement remains a weekly item.

**Verdict: GREEN — cleared to stage.** No push from the sandbox; Vini holds the push.

— Manager · 2026-06-17
