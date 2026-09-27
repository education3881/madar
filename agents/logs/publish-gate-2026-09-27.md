# Publish gate — 2026-09-27 (run in writing before committing anything editorial)

**Scope of today's push:** one new **held** English draft (Edition 05 row 6, Rwanda), its hero
still and its share card; one instrument change (`qa_sources_alive`); two rulings; one recon
addendum; one hand-off; one Growth artefact; a superseded RUNBOOK clause; records.
**No piece ships. No `approved:` flag flips to `true`. The wave gate is not run today and was not
going to be.**

| Gate check | Result |
|---|---|
| Editor / Verifier verdict on file for anything shipping | **N/A — nothing ships.** The new file is `approved: false`. Its **commission** is on file (`briefs/2026-09-25-…`) as amended (`verdicts/2026-09-26-…`), and the draft answers the amendment clause by clause in `content-drafts/2026-09-27-ed05-rwanda-draft-handoff.md`. Its five-test pair verdict is **owed the next run** and its Verifier verdict the run after — scheduled in the ledger, not skipped. |
| Arabic Editor approval for any AR shipping | **N/A — no AR exists yet.** Rwanda is English-only today; the Arabic is *composed*, not translated, and is a later lane. Nothing Arabic was written for this piece anywhere, including the distribution packet, where the fifth entry remains **owed rather than invented**. The eight named-human transliterations the commission flags are the Arabic Editor's to verify at compose; none is pre-empted here. |
| Hero still on disk, same commit as the text | ✓ `web/public/stills/2026-09-27-rwanda-teacher-certification.svg` (06-14 rule — assets never in a follow-up commit) |
| Share card on disk, generated from the still | ✓ `web/public/og/2026-09-27-rwanda-teacher-certification.png`, 1200×600, 1,644 bytes, via `web/scripts/make-og-card.mjs`. **Opened and looked at** before this line was written (08-18 rule) — and the first render was **rejected and redrawn**: the composition sat in the lower half with 130px of dead space below the ground line, against the corpus's own ground line at y=524. The alt text was regenerated from the same string that produces the SVG's `aria-label`, so the two cannot drift. |
| Still contains no figure and no numeral | ✓ Deliberate. The drawing is two ledger columns standing level with a dashed level line between their tops, and a row of 34 tally strokes along the foot — the flow/stock finding drawn, with nothing a reader could mistake for a published quantity. |
| `npm run build` clean with today's changes in | ✓ exit 0, **121 pages**, 120 sitemap URLs, **ten** postbuild assertions green |
| Held-piece leakage in built output | ✓ **zero.** `qa_held_assets` CLEAN — held slugs **5 → 6**, and the new still and card are among the withheld. No held slug in `dist` or the sitemap. **Served pages unchanged at 121.** |
| Held piece contributes no DATE (#35 / 09-06 rule) | ✓ `qa_lastmod` PASS across 120 URLs, unchanged by today's held file; and independently, `qa_live_drift` reports **0 lastmod drift** against the origin. |
| EN/AR parity of the **approved** corpus | ✓ 38 = 38, unchanged |
| Flag state on disk (ruling #18) | ✓ 76 approved files, **11 held** (5 pairs + today's EN-only draft). No stale `approved: true` duplicate of the new slug anywhere. |
| Caps measured at COMPOSE, not at the gate (07-27 rule) | ✓ **dek 199/200 · title 53/100 · body 2,300/2,300** (code points; body by the same `\S+` count the ledger has used since slot 3). Recorded honestly: the first composition measured **dek 263** and **body 2,437**, both cut at the drafter's desk. **Second consecutive piece to catch the dek at the ruler rather than the build, and the first ever to measure the WORD cap at compose** — slot 3 discovered its overrun at the verdict and still carries a waiver. |
| `related:` rail resolves | ✓ Three approved EN slugs — Sierra Leone TSC, Yemen teacher pay, Brazil. **Deliberately not** the 08-18 recon's instruction to cross-link "the CBC/exam story", which is a **recon and has never been an article**; `RelatedReading.astro` filters unknown slugs silently, `qa_body_links` reads approved pages only, and a held piece's dangling rail would therefore have surfaced at the six-piece atomic flip. Raised to the Editor in the hand-off. |
| Source URLs verified before the text carried them | ✓ All eight probed in served text today. **Six are on `mineduc.gov.rw`, whose certificate expired 23 September 2026** — documents still served, every annotation states it, ruling #70. One (World Bank) serves a valid certificate. One (allAfrica) 200, re-read for byline, date, quote and the two things it does *not* contain. |
| Full assertion battery | ✓ **23 of 23 runnable green** — see `agents/logs/qa-2026-09-27.md`. Two not run, each with its reason. |
| Founder-owned decisions touched | **None.** Edition scope is closed at six (09-13, by the stated default). The custom domain, Substack and public identity are untouched. |
| Credentials, tokens or keys in the diff | **None.** Checked: the only network material committed is public URLs in `sources[]` and a certificate's expiry date, which is public by construction. |

## The one thing this gate does NOT clear, stated rather than buried

**The slug's date moved without the Editor.** The amendment of 09-26 says *"Slug unchanged"*; the file
is `2026-09-27-rwanda-teacher-certification`, dated `2026-09-27`. The reasoning, the precedent and the
revert instruction are in the hand-off's open items; the short version is that the amendment fixed the
slug on the assumption of a 09-26 draft that its own draft-blocker displaced, a dateline is a claim
while a slug is an identifier, and the corpus's slug-prefix-equals-date invariant holds at **0
mismatches across 87 files** and is asserted by nothing. **This is a Manager call on an identifier, made
because the alternative was knowingly printing a false dateline, and it is routed for the Editor's
confirmation at the pair verdict.** Nothing has shipped; reverting costs one rename and two frontmatter
lines, and the still and card are named to match either way.

— Manager · 2026-09-27
