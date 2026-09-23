# Publish gate — 2026-09-23 (run in writing before staging the push)

**Scope of today's push:** the Verifier's verdict on Edition 05 row 5 and the six held-file
edits that close it; one new standing assertion, gated; the first sweep of every distribution
artefact in `social-drafts/**` and the one live-piece caption defect it found; ruling #62 with
its register rows; and records. **No piece ships. No `approved:` flag flips to `true`.**

| Gate check | Result |
|---|---|
| Editor / Verifier verdict on file for anything shipping | N/A — nothing ships. Today **produces** a verdict rather than consuming one: `content-drafts/verdicts/2026-09-23-egypt-baccalaureate-published-first-verification.md`, FAIL-3-ITEMS, all three closed in-run, one further item OPEN and named |
| Arabic Editor approval for any AR shipping | N/A — no AR ships. **Three AR artefacts were composed today and are owed a gate**, named rather than assumed: the two Arabic body edits and two Arabic annotations on the held Egypt piece, and the corrected Arabic caption in the Brazil packet. With the wave packet's five, the Arabic Editor now gates **six captions** and one held pair's edits |
| Hero stills / og cards on disk for anything shipping | N/A — nothing ships. `qa_held_assets` CLEAN: 5 held slugs, zero bytes |
| `npm run build` clean with today's changes in | ✓ exit 0, run four times across the day — 121 served pages, 120 sitemap URLs, all nine `postbuild` gates green |
| Standing assertions | ✓ **23 of 23 green; 21 gate the deploy.** One new this run (`qa_packet_figures`), **proved seven ways** before wiring, with the bite taken from a real historical defect (the 09-21 packet's *120-year-old*) rather than an invention, and every injection asserted to have changed its file first (09-14 rule) |
| Held-piece leakage in built output | ✓ zero slugs, zero bytes, zero dates. The six content edits are all inside `approved: false` files |
| EN/AR parity | ✓ 38 = 38, unchanged. Held pair's numeral multiset after every edit: **EN 40 / AR 40, zero one-sided figures in either direction** |
| Flag state on disk (ruling #18) | ✓ 76 `approved: true` (38 EN + 38 AR), 10 held files / 5 held slugs, **no flips** |
| Live origin at run open | ✓ serving `Tue, 22 Sep 2026 09:54:55 GMT` — the 09-22 deploy. `qa_live_drift` CLEAN, 0 drift |
| Workflow change in this push | None. `.github/workflows/**` is untouched; the new gate goes into `web/package.json`, which this identity may write |
| Anything reader-visible changing on the next deploy | **No.** Every content edit is inside a held file, and `package.json` is not served. The expected served diff is zero bytes |

**One thing that is NOT clean, and is named rather than absorbed.** Edition 05 row 5's source
1 — the statute reproduction the fee clause and the Article 24 sentence both stand on alone —
**stopped answering this reader today**, between the Editor's verdict and its verification. It
is carried fetched-on-date with the failure layer stated in both languages, and the re-probe is
the first item of the wave's confirmation read. **That is a flip-day risk on a held piece, not
a defect in this push**, and it is recorded in the ledger so nobody arrives at the gate
surprised by it.

**A second, smaller one.** A caption in a **live** piece's distribution packet was wrong for 90
days and was corrected today. Nothing in this repository records whether it was ever posted, and
nothing in this push changes what a reader can see. Said plainly rather than filed as a win.

**Gate verdict: CLEAR to push.** Nothing editorial ships; every editorial edit is held-side and
closes a verification verdict rather than opening a question.

— Manager · 2026-09-23
