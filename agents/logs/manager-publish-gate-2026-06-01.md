# Manager — publish gate, 2026-06-01

## Scope of this gate

Three AR translations only. No new EN content today. The publish gate checklist runs in writing per the binding rule codified 2026-05-26 and re-enforced after the 2026-05-27 Egypt miss.

| # | Slug | Type | EN ref |
|---|---|---|---|
| 1 | `2026-05-31-indonesia-permen-13-coding-ai` | AR | EN already live since 2026-05-31 |
| 2 | `2026-05-31-qatar-humanity-spark-strategy` | AR | EN already live since 2026-05-31 |
| 3 | `2026-05-31-uruguay-eduia-lab-ceibal` | AR | EN already live since 2026-05-31 |

## Gate 1 — Editor verdict + `approved: true`

- [x] **Indonesia AR** — verdict in `/content-drafts/verdicts/ar/2026-06-01-indonesia-qatar-uruguay-ar.md`. `approved: true` in `web/src/content/articles-ar/2026-05-31-indonesia-permen-13-coding-ai.md`.
- [x] **Qatar AR** — same verdict file. `approved: true` in `web/src/content/articles-ar/2026-05-31-qatar-humanity-spark-strategy.md`.
- [x] **Uruguay AR** — same verdict file. `approved: true` in `web/src/content/articles-ar/2026-05-31-uruguay-eduia-lab-ceibal.md`.

Verdict file also documents the named-human transliterations applied and the cross-language frontmatter integrity (every EN article in this batch now carries `arabicVersion:` pointing back at the AR slug; every AR article carries `englishVersion:` pointing at the EN slug).

## Gate 2 — Hero stills on disk

AR layouts reuse the EN stills; no new SVGs required.

- [x] `/web/public/stills/2026-05-31-indonesia-permen-13-coding-ai.svg` — present, 6.6 KB.
- [x] `/web/public/stills/2026-05-31-qatar-humanity-spark-strategy.svg` — present, 4.9 KB.
- [x] `/web/public/stills/2026-05-31-uruguay-eduia-lab-ceibal.svg` — present, 6.2 KB.

## Gate 3 — Astro build clean

`VITE_CACHE_DIR=/tmp/madar-vite-cache-0601 npx astro build` from `/web` — completed.

All 22 article routes generated:
- 10 EN pages (incl. the three 5/31 pieces)
- 10 AR pages (incl. the three new AR pieces from today)
- about page
- ar/index, index, rss.xml

Build emitted a trailing `EPERM: unlink dist/noop-entrypoint.mjs` — this is the known sandbox-FUSE boundary on Vite cleanup (see [[edu-website-sandbox-lock]]). It is **not** a build failure; all routes generated before it; production deploy via GitHub Actions does not encounter this boundary because the workflow runs in a non-sandboxed environment.

## Gate 4 — Arabic Editor full pass

Codified 2026-05-29 as the fourth gate for AR releases. Today's pass is documented in `/content-drafts/verdicts/ar/2026-06-01-indonesia-qatar-uruguay-ar.md` and covers:

- Five-test rubric per piece
- Named-human transliteration list (cross-checked for internal consistency)
- Source-block bilingual integrity
- Cross-language frontmatter integrity
- Style notes carried forward for next AR drafts

All three pieces approved by the Arabic Editor.

## All four gates pass.

## Push — deferred to Vini's terminal

Sandbox FUSE boundary on `.git/index.lock` is active (observed today, consistent with the 2026-05-28 / 29 / 30 / 31 pattern). The push cannot run from the sandbox. The one-line fix and the commit/push sequence is documented in today's EOD brief at `/agents/logs/brief-2026-06-01.html`.

Until the push lands, the three AR pieces sit on disk in working-tree-modified state alongside the three EN frontmatter modifications (the `arabicVersion:` field additions). The live site continues to show the 2026-05-31 state until the next push.

— Manager
