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

---

# Publish gate, 2026-11-26: `2026-11-26-jordan-pisa-2025-counts-from-2022` (Edition 06, piece 2)

| Cell | Evidence | State |
|---|---|---|
| 1 Editor brief | content-drafts/briefs/2026-11-26-jordan-pisa-2025-counts-from-2022-brief.md — names the rails and the forward edges owed | FILLED |
| 2 EN draft | content-drafts/drafts/2026-11-26-jordan-pisa-2025-counts-from-2022.md — 27 quoted spans, 8 of 8 comparable verbatim, 0 words changed; 19 are translations of an Arabic register and no instrument can compare them | FILLED |
| 3 Editor verdict | content-drafts/verdicts/2026-11-26-jordan-pisa-2025-counts-from-2022.md — PASS, two notes closed in-run, one of them a fabricated comparison | FILLED |
| 4 AR composition | content-drafts/drafts/2026-11-26-jordan-pisa-2025-counts-from-2022-ar.md | FILLED |
| 5 Arabic Editor gate | content-drafts/verdicts/2026-11-26-jordan-pisa-2025-counts-from-2022-arabic-gate.md — APPROVED, both editions, three named humans confirmed, and the translation check the Editor routed here | FILLED |
| 6 Verifier | content-drafts/verdicts/2026-11-26-jordan-pisa-2025-counts-from-2022-verification.md — independent re-fetch of all four registers, VERIFIED WITH CORRECTIONS REQUIRED, all five applied in both editions before this gate | FILLED |
| 7 Still + og | web/public/stills/2026-11-26-jordan-pisa-2025-counts-from-2022.svg, web/public/og/2026-11-26-jordan-pisa-2025-counts-from-2022.png (1200x600, rasterised from the still, looked at and rebalanced once because the first composition sat in the right third) | FILLED |
| 8 Flag | approved: true in both editions in this commit, with assets, and the forward rails into all three railed pieces (both editions: three-lists-of-risers 2 to 3, us-naep-honesty-gap 5 to 6, bahrain-bqa-five-cycles 4 to 5, all at or under the cap of 6) | THIS COMMIT |

**Registers.** All four re-fetched at compose time (#101) and the three OECD snapshots re-hashed against the
read banked this morning: byte-identical, 1,468,371 / 1,614,913 / 1,464,823 bytes, sha256 prefixes
`096bb651ddbda014` / `01b2bd4aa78bf802` / `33b350b2803a4906`. **The recon's note that this workspace cannot
hold a connection to `web.archive.org` was false today** — all three fetched direct from the runner with no
route-around. The Jordanian register answers this runner directly and was fetched twice, at the start and
the end of the audit, with identical text.

**Build.** `npm run build` exit **0**, all 28 postbuild gates green and `build_job_gates` green on all 12
build-job gates, so the local gate set is the deploy's gate set. Four red builds preceded it and each red
was a real register obligation this piece created rather than a flake:

1. `qa_claim_registers --check` — the two new cited registers had no observation row. Closed by `--emit`,
   which asked 40 registers this run, 0 throttled, 375 rows now on file. **The Jordanian register's row
   reads `archive-unknown / not yet asked`**, and under issue #12's applied default (option B) the
   operation may not send a new URL to an archive, so it stays that way and is named here rather than
   quietly fixed.
2. `qa_citation_identity --check` — same two registers, same cause, closed by its own `--emit`.
3. `qa_annotation_figures` — **six annotation quantities printed in no body**: `403`, `85`, `760`, `000`
   in the English annotations and `403`, `16` in the Arabic. Five were annotation furniture (an HTTP status
   code and two OECD figures the body never uses) and were removed. **The sixth is a latent class**: the
   gate's date licence recognises English month names only, so `16 نوفمبر 2026` leaves a bare `16` while
   `16 November 2026` does not. Edition 06's first piece passed this gate this morning only because `16%` is
   in its body. Fixed here by writing the Arabic snapshot dates in the ISO form the same sentence already
   uses. **Recorded as the QA forward question.**
4. `qa_selector_coverage` LIMB 2 — the **twenty** current-edition secondary and also-in-this-edition
   selectors now MATCH, because the open edition holds more than one piece. Their own register entries said
   *strike these the day LIMB 2 says they match*, and this is that day. Struck, with the reason written at
   the point of the strike. **The gate predicted its own next state and was right**, which is the first time
   a CONDITIONAL entry in this register has expired on schedule.

**Held-slug leak: zero** — no `approved: false` file remains in either collection, so the sweep is in
all-approved mode (2026-08-09 inversion) and the positive checks are what ran: both new slugs resolve in
`dist` and in the sitemap, both hero stills resolve in the built article HTML, and both pages render.

**Prior publication, observed before this build (#128 limb 5):** last `astro-pages.yml` run 45822027663,
conclusion **success**, deployed `5b7232f` — Edition 06's first piece is served. Strand at observation time:
1 commit (`d020a35`, this run's own content bank).
