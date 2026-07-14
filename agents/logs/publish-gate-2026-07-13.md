# Publish gate — 2026-07-13 (run in writing before staging the push)
**Scope of today's push:** records + two surgical changes inside held/staging material. **No piece ships. No `approved:` flag flips to `true`.**

| Gate check | Result |
|---|---|
| Editor / Verifier verdict on file for anything shipping | N/A — nothing ships. The one content edit (NZ ¶4 recount clause) is *inside a held draft* (`approved: false`), applied under the Verifier's FAIL-item routing (Editor → CC), verdict on file: `verdicts/2026-07-13-ed04-nz-ncea-verification.md` |
| Arabic Editor approval for any AR shipping | N/A — no AR ships. The only AR-side change *lowers* exposure: staged us-naep AR flag defused `true → false` |
| Hero stills on disk for anything shipping | N/A — nothing ships (NZ still remains a gate-side Designer deliverable, logged in the verdict) |
| `astro build` clean with today's changes in | ✓ exit 0, **65 pages**, sitemap 65 URLs, tmpfs route-around (qa-2026-07-13) |
| Held-piece leakage in built output | ✓ zero — no Ed04 slug in `dist/` |
| EN/AR parity | ✓ 30 = 30 |
| Flag state on disk (ruling #18) | ✓ web/src: 30 true EN + 30 true AR + 5/1 false held; staging: zero `approved: true` on any Ed04 copy (AR trap defused this run) |
| Live-site marker at run open | ✓ homepage current, hreflang triples serving (e5eecba deployed) |

**Gate verdict: CLEAR to stage.** The push block in Brief 32 carries: NZ verdict + one-clause fix (web/src + staging), staged AR flag defusal, qa-2026-07-13, ruling #21 + INDEX addendum, growth preflight memo, Ed04 status update, stats history snapshot, Brief 32.

— Manager · 2026-07-13
