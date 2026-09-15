# Publish gate — 2026-09-15 (run in writing before the commit)

**Scope of today's push:** the Editor's pair verdict on Edition 05 slot 3 with its
four in-run fixes (inside **held** files), one new standing assertion, one extended
assertion, one growth change to the site chrome, ruling #51, and the day's records.
**No piece ships. No `approved:` flag flips to `true`.**

| Gate check | Result |
|---|---|
| Editor verdict on file for anything shipping | N/A — nothing ships. Today's editorial work is **inside held drafts** (`approved: false`): `content-drafts/verdicts/2026-09-15-ed05-best-system-pair-verdict.md`, four notes returned and closed in-run |
| Verifier verdict on file for anything shipping | N/A — nothing ships. Slot 3's verification verdict is **next run**, per the 09-06 RUNBOOK rule; ceiling clear (4 banked, 3 verified, drafting ≤3 ahead) |
| Arabic Editor approval for any AR shipping | N/A — no AR ships. Gate 4 PASS on file from 09-14, with **today's addendum** disposing of a sixth name (إيلير هونكبودوتيه) moved from annotation into the body |
| Hero still + og card on disk for anything shipping | N/A — nothing ships. Slot 3's still and card are on disk and **withheld from the build** (8 assets for 4 held pieces) |
| `astro build` clean with today's changes in | ✓ exit 0, **120 pages**, `CI=true`, full checkout; `postbuild` gates both green |
| The twelve deploy-gating assertions | ✓ all green (§2 of `agents/logs/qa-2026-09-15.md`) |
| The new assertion, proved both ways before landing | ✓ `qa_render` — control silent, three bites each verified to have changed the artefact first |
| The extended assertion, proved both ways | ✓ `qa_consumer_surface` alt check — control silent, two bites |
| Held-piece leakage in built output | ✓ **zero** — `grep -rl` over `web/dist` returns 0 files for each of the four held slugs |
| Held-piece leakage into dates (09-06 rule) | ✓ newest sitemap `<lastmod>` is still **2026-09-14T07:46:10Z**; today's edits to held files moved no live date |
| EN/AR parity | ✓ 38 = 38 published; 4 EN / 4 AR held on disk |
| Flag state on disk (ruling #18) | ✓ 38 `approved: true` EN + 38 AR; 4 + 4 `false`, all four Ed05 pairs |
| Gate dependency re-checked | ✓ all four pairs are mutually `related:`-bound and flip atomically; the three reciprocal edges into slot 3 are still owed **at the flip commit** |
| Live origin at run open | ✓ serves the 09-14 build, 09-14 deploy green, `HEAD == origin/main` |
| Credentials, tokens, keys in the diff | ✓ none |

**Gate verdict: CLEAR to commit.** Nothing editorial ships; the corpus is unchanged
at 38 EN / 38 AR and 35 countries.

— Manager · 2026-09-15
