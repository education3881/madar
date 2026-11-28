# Publish gate in writing — 2026-11-28 (daily run)

**Result: ONE FLIP — `2026-11-27-saudi-pisa-2025-two-clocks-disagree`, Edition 06's sixth and its floor.**
*(This file's first section read **NO FLAG FLIPS TODAY** when it was written at 14:1xZ, and that was true
then. The Saudi hold was lifted later in the same run once both other rows reached 7 of 8 — see
`content-drafts/verdicts/2026-11-28-saudi-pisa-2025-two-clocks-disagree-publish-gate.md`, which is the
flip's own gate and the authoritative record for it. This file is the gate on the state the run's editorial
edits leave behind, and the table below is corrected to the final state rather than rewritten, so the
sequence stays legible.)*

**The flip's own three red gates are in that file's §D** — `qa_claim_registers`, `qa_citation_identity` and
`qa_annotation_figures`, all three blind to a held piece and all three meeting the piece for the first time
at the flag, cleared by two `--emit` runs and **thirteen hand-written provenance rows**.

## A. The flip gate, piece by piece

| Piece | Editor | Arabic gate | Verifier | Still | og card | Flag | Verdict |
|---|---|---|---|---|---|---|---|
| `2026-11-27-saudi-pisa-2025-two-clocks-disagree` | PASS 2026-11-27 | APPROVED 2026-11-27 | **VERIFIED 2026-11-28**, two corrections applied | served | served | **`true`** | **SHIPPED 2026-11-28.** Served and verified in `dist` before the commit: EN 66,314 bytes, AR 77,887 bytes, both URLs in the sitemap with reciprocal hreflang, three entries in each feed |
| `2026-11-27-uzbekistan-pisa-2025-only-in-students` | PASS 2026-11-27 | **APPROVED 2026-11-28**, re-run on the changed passages, three corrections | **FAIL 2026-11-28 → repaired → re-verified PASS** | on disk, **not redrawn** | valid 1200×600 | `false` | **GATE-READY, RAIL NOW UNBLOCKED by the Saudi flip. Ships 2026-11-29**, first in the order |
| `2026-11-28-uruguay-pisa-2025-own-account` | PASS 2026-11-28 | APPROVED 2026-11-28 | **PASS 2026-11-28**, two corrections applied | on disk | valid 1200×600 | `false` | **GATE-READY AND BLOCKED BY THE CORPUS.** Its `related:` rail names the still-held Uzbekistan slug. **Ships 2026-11-30**, second in the order |

## B. The five standing checks

1. **Editor and Arabic verdicts on file** — yes, for all three; file paths in the ledger rows.
2. **Hero still and share card on disk** — yes for all three. **The invariant inverted at the flip, as the
   2026-08-09 rule requires, and was asserted in both directions afterwards:** `qa_held_assets` CLEAN at
   **2 held slugs and 52 approved**, so the flipped piece contributes bytes and the two still held
   contribute none — no page, no sitemap entry, no still, no og card. The Uzbekistan and Uruguay og cards
   were re-read as bytes rather than assumed — PNG signature valid, header parsed, **1200×600** each.
3. **`astro build` clean** — `cd web && npm run build` **exit 0**, and `build_job_gates` ran the twelve
   build-job gates out of the workflow file: all twelve ok. **40 of 43 green.**
4. **Assertions green** — see `agents/logs/qa-2026-11-28.md` §2.
5. **Held-slug leak zero** — yes, on the two that remain held. Asserted, not trusted, and asserted
   *after* the flip rather than before it.

## C. What this gate is NOT asserting, said plainly

**It is not asserting that this run's own work is served.** No run has ever observed its own publication
(#128): the deploy runs after the agent step ends. `madar-daily.yml`'s step 9 `publish what the run
pushed` carries `if: always()` since 2026-11-26 and will dispatch `astro-pages.yml` on the commits this
run pushed. **The next run reads the conclusion and the strand out of
`agents/stats/publication-observations.jsonl` and prints them in its brief.** Today's reading, taken before
the repair: deploy **46103196013 failure**, strand **14**.

**The one thing this gate can promise about the repair** is that the build it gates is green on the same
tree that is now on `origin`, which is the condition the 2026-11-28 failure violated and the only
condition this identity can check from inside the run.
