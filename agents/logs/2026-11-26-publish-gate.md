# Publish gate, 2026-11-26: `2026-11-26-pisa-2025-three-lists-of-risers` (Edition 06, piece 1)

| Cell | Evidence | State |
|---|---|---|
| 1 Editor brief | content-drafts/briefs/2026-11-26-pisa-2025-three-lists-of-risers-brief.md | FILLED |
| 2 EN draft | content-drafts/drafts/2026-11-26-pisa-2025-three-lists-of-risers.md, 23 bold spans byte-checked, 0 words changed | FILLED |
| 3 Editor verdict | content-drafts/verdicts/2026-11-26-pisa-2025-three-lists-of-risers.md, PASS, notes closed in-run | FILLED |
| 4 AR composition | content-drafts/drafts/2026-11-26-pisa-2025-three-lists-of-risers-ar.md | FILLED |
| 5 Arabic Editor gate | content-drafts/verdicts/2026-11-26-pisa-2025-three-lists-of-risers-arabic-gate.md, APPROVED | FILLED |
| 6 Verifier | content-drafts/verdicts/2026-11-26-pisa-2025-three-lists-of-risers-verification.md, independent agent, VERIFIED WITH CORRECTIONS REQUIRED, all seven applied in both editions before this gate | FILLED |
| 7 Still + og | web/public/stills/2026-11-26-pisa-2025-three-lists-of-risers.svg, web/public/og/2026-11-26-pisa-2025-three-lists-of-risers.png (1200x600, rasterised from the still, looked at) | FILLED |
| 8 Flag | approved: true in both editions in this commit, with assets, the Edition 06 registry row and cover, and the forward rail into 2026-09-14-africa-best-system-ruler (both editions, 6 of 6) | THIS COMMIT |

Build: `astro build` exit 0 and all 29 postbuild gates green, including the 12 build-job gates. Browser gates
retried on timeout only (this workspace's Chrome stalls intermittently; each passed on re-run).
qa_selector_coverage: 20 home-page selectors registered CONDITIONAL (secondary and also rows, untaken until
Edition 06's second piece ships), and .edition__tag struck because it now matches.
Held-slug leak: zero (no held pieces after this flip).
