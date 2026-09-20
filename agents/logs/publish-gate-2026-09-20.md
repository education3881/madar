# Publish gate — 2026-09-20 (run in writing before staging the push)

**Scope of today's push:** a build-correctness fix touching every list surface the site
serves, two new standing assertions, one workflow repair, six held-file frontmatter edits,
and records. **No piece ships. No `approved:` flag flips to `true`.**

| Gate check | Result |
|---|---|
| Editor / Verifier verdict on file for anything shipping | N/A — nothing ships. The six content edits are **inside held drafts** (`approved: false`): the wave's reciprocal `related:` edges into row 4, a decision already recorded in `_EDITION_05_STATUS.md` since 2026-09-14 and there instructed to land no later than the flip commit |
| Arabic Editor approval for any AR shipping | N/A — no AR ships. The three AR edits are the same rail edge as their EN twins, so the pair carries the same rail (#42). No Arabic prose was composed or altered |
| Hero stills / og cards on disk for anything shipping | N/A — nothing ships. Held assets remain withheld; `qa_held_assets` CLEAN |
| `npm run build` clean with today's changes in | ✓ exit 0 — 121 served pages, 120 sitemap URLs, all four `postbuild` gates green |
| Standing assertions | ✓ **21 of 21 green.** Two new this run (`qa_stable_order`, `qa_feed_enclosures`), each proved both ways per #35 before landing, each with its build gate proved by a real `npm run build` exit 1 |
| Held-piece leakage in built output | ✓ **zero slugs, zero bytes, zero dates.** Proved rather than asserted: six held files were edited and `dist` is **byte-identical before and after** |
| EN/AR parity | ✓ 38 = 38, unchanged |
| Flag state on disk (ruling #18) | ✓ 76 `approved: true` (38 EN + 38 AR), 9 held files / 5 held slugs, **no flips** |
| Live origin at run open | ✓ serving `Sat, 19 Sep 2026 09:27:25 GMT` — the 09-19 deploy. `qa_live_drift` CLEAN |
| Workflow change in this push | ⚠ `.github/workflows/astro-pages.yml` is edited (the `verify` feed-cache retry). **This identity may not be permitted to push that path** (09-14, clause 4). Staged as a **separate, final commit** so a refusal costs nothing but that one commit — see the brief |

**One thing that is NOT clean, and is named rather than absorbed:** four Arabic pages will
change their served bytes on the next deploy — `/ar/browse/region/mena/`,
`/ar/browse/topic/ai-readiness/`, `/ar/browse/topic/language-and-heritage-preservation/`
and `/ar/editions/`. That is the ruling #58 fix taking effect: those pages were serving an
arbitrary tie order and will now serve the canonical one. It is a correction, it is
intended, and it is the only reader-visible change in this push.

**Gate verdict: CLEAR to push.** Nothing editorial ships; the editorial edits are held-side
and execute a recorded decision earlier than required rather than later.

— Manager · 2026-09-20
