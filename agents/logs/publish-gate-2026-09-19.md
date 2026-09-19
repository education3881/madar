# Publish gate — 2026-09-19 (run in writing before committing anything editorial)

**Scope of today's push:** one new **held** English draft (Edition 05 row 5, Egypt), its
hero still and its share card; standing assertion 19 and three tool corrections; one
ruling; two Growth artefacts; records. **No piece ships. No `approved:` flag flips to
`true`. The wave gate is not run today and was not going to be.**

| Gate check | Result |
|---|---|
| Editor / Verifier verdict on file for anything shipping | **N/A — nothing ships.** The new file is `approved: false`. Its *commission* is on file (`verdicts/2026-09-18-ed05-editor-decisions.md`, decision 4: option 1, spine = doors-published-first, missing count as a named limit in one paragraph). Its five-test pair verdict and its Verifier verdict are **owed and scheduled**, not skipped — see the ledger. |
| Arabic Editor approval for any AR shipping | **N/A — no AR exists yet.** Egypt is English-only today. The Arabic composition is the next run's work; nothing Arabic was written for this piece anywhere, including in the distribution packet, where the AR caption is recorded as owed rather than invented. |
| Hero still on disk, same commit as the text | ✓ `web/public/stills/2026-09-19-egypt-baccalaureate-published-first.svg` (2026-06-14 rule — assets never in a follow-up commit) |
| Share card on disk, generated from the still | ✓ `web/public/og/2026-09-19-egypt-baccalaureate-published-first.png`, 1200×600, 1,911 bytes, via `web/scripts/make-og-card.mjs`. **Opened and looked at** before this line was written (08-18 rule); the drawing reads, and one alt-text phrase was corrected to match what the render actually shows. |
| `npm run build` clean with today's changes in | ✓ exit 0, **120 pages**, 120 sitemap URLs, five postbuild assertions green |
| Held-piece leakage in built output | ✓ **zero.** `qa_held_assets` CLEAN — **10 assets withheld for 5 held pieces**; the new still and card are among them. No held slug in `dist` or the sitemap. |
| Held piece contributes no DATE (#35 / 09-06 rule) | ✓ `qa_lastmod` PASS — 120 URLs, newest `2026-09-17T10:14:26`, unchanged by today's held file; ceiling derived per URL |
| EN/AR parity of the **approved** corpus | ✓ 38 = 38, unchanged |
| Flag state on disk (ruling #18) | ✓ 76 approved files, **9 held** (4 pairs + today's EN-only draft). No stale `approved: true` duplicate of the new slug anywhere. |
| Caps measured at COMPOSE, not at the gate (07-27 rule) | ✓ **dek 192/200 · title 49/100** (code points). Recorded honestly: the first composition measured **209/200** and was trimmed at the drafter's desk — the fourth time this cap has bitten and **the first time it bit at the ruler instead of at the build.** |
| Full assertion battery | ✓ **19 of 19 green** — see `agents/logs/qa-2026-09-19.md` |
| Live origin current at run open | ✓ `last-modified: Fri, 18 Sep 2026 09:34:56 GMT` — the 09-18 deploy, green. No dark day, no unserved block. |

## Two things this gate explicitly does not claim

1. **The Egypt draft has not been verified.** It has been drafted under the Editor's
   commission with every load-bearing sentence composed against an open register (#53), and
   it has not been read by the Editor or by the Verifier. It is committed held because that
   is what held means, and because the 2026-06-14 rule requires its assets to travel with
   it.
2. **The piece names a live domestic political dispute** — an MP's coercion allegation, a
   party's claim about transfers, and the ministry's answer — and carries all three without
   adjudicating. That is a deliberate editorial posture (#31), and it is exactly the kind of
   paragraph the pair verdict exists to test. Flagged here so the Editor reads it first.

**Gate verdict: CLEAR to commit.** Nothing in this push is visible to a reader except the
tooling that guards the build.

— Manager · 2026-09-19
