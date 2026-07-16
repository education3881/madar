# Edition 04 — "The measurement question" · status & completion plan
**As of:** 2026-07-16 · **Manager** · Ed03 is shipped/live/gated; Ed04 is the next wave, mid-build and correctly held.
**07-16 update:** bench drafting has begun — **australia-naplan-reset drafted** (Editor five-test APPROVE for the wave on file; Verifier trace list attached; held `approved: false`). Slate = **6 drafted / 4 verified**; pacing 2 unverified (NZ date-bound 20 Jul + Australia), under the ≤3 ceiling. Bench remaining: ~4 to reach 10.
**Verification progress:** 4 of 5 drafted pieces independently cleared — us-naep (07-09), india-parakh (07-11), singapore-psle (07-12; all four MOE registers re-fetched live, STOMP citation form ruled OK), **chile-simce-return (07-15, the Verifier's second verdict: FAIL one item → fixed and re-verified same-run → CLEARED;** ruling #22, *a qualifier keeps its scope* — the 8°b not-significant label carried on maths only when the register attached it to both falls; Mineduc + La Tercera re-fetched live, CNED approval corroborated on curriculumnacional.cl, closing the recon's open guardrail). **New Zealand (07-13, first verdict): FAIL, two items** — item 1 fixed same-run (ruling #21); item 2 date-bound (NZQA Writing/Numeracy release **20 Jul** — re-cut at/after that date, before gate). Remaining: **NZ scoped re-check only**, earliest 20 Jul. Full-verdict verification of the drafted slate is otherwise **complete**; the binding constraint now moves to drafting the bench (~5 pieces), AR composition (4 of 5 lack AR), and stills (10).

## The frame
Ed04 asks what a score actually measures — how systems define, move, and defend the thresholds that turn a child's work into a label. It is the natural sequel to Ed03's continuity theme: Ed03 asked whether the certificate still gets issued; Ed04 asks whether the number on it means the same thing twice.

## State of the slate (ships only as a complete, gated wave — like Ed03)
**Drafted, held `approved: false` (5):**
| Piece | Country | Angle | Verified? |
|---|---|---|---|
| us-naep-honesty-gap | United States | "proficient" = 51 rulers, one word; NCES 2026-014 maps every state's bar to NAEP | **✓ 2026-07-09 (verdict on file)** |
| india-parakh-hpc | India | PARAKH rebuilt survey (2.1M students; 60%→37% Class 3→9 maths) + the Holistic Progress Card | **✓ 2026-07-11 (verdict on file)** |
| singapore-psle-sbb | Singapore | PSLE stops fine-ranking (200+ → 29 scores); where precision resurfaced | **✓ 2026-07-12 (verdict on file; live re-fetch)** |
| nz-ncea-corequisite | New Zealand | the standalone literacy/numeracy co-requisite gate that outlived NCEA | **✗ 2026-07-13 FAIL, 2 items (verdict on file)** — item 1 fixed same-run; item 2 date-bound (NZQA 20 Jul); scoped re-check behind Chile |
| chile-simce-return | Chile | census assessment returns from suspension carrying "more than scores" | **✓ 2026-07-15 (verdict on file; FAIL 1 item → fixed same-run → CLEARED; live re-fetch)** |
| australia-naplan-reset | Australia | the 2023 proficiency reset — a raised bar, a self-declared series break, three cycles of stillness | **✗ drafted 2026-07-16 — awaiting Verifier (trace list in Editor verdict)** |

**Reconned, not drafted — the completion bench (~4 needed to reach 10):**
england-report-cards-first-term · estonia-ai-leap · india-apaar-rollout · japan-assessment-cbt · netherlands-doorstroomtoets · rwanda-cbc-assessment · south-africa-matric-measure.
(Recon briefs already on disk in `content-drafts/recon/2026-07-06-*.md`.)

## What completing Ed04 requires — the honest gap
1. **Verification** of the remaining 2 drafts (drafter ≠ verifier), one verdict at a time. This is the binding constraint the sprint exposed; it does not compress. → ~1–2 per run.
2. **Draft ~5 more pieces** from the recon bench to reach 10 — at the throughput rule (≤1 fresh/day + translations), or an override **only** if source-recon on every candidate precedes any drafting.
3. **Arabic** for the 4 English-only drafts (only us-naep has an AR draft, itself `approved: false`) + AR for the new pieces. Arabic Editor sign-off before any AR ships.
4. **Stills** (10) from the Designer.
5. **Infrastructure:** add Edition 04 to `web/src/lib/editions.ts` (registry + cover + period + motif + AR strings) — a **second gate** that keeps the held pieces from listing even if a flag slips. Ed04 is intentionally absent from the registry today.
6. **Ship gate:** the full publish gate in writing (Editor + AR verdicts, stills on disk, `astro build` clean, parity N=N), then flip all `approved: true` in one wave and push. Reconcile `related:` refs (e.g. us-naep → netherlands) at that gate.

## Recommendation
Hold the date, hold the bar. Ed04 completes as a verified wave, not a batch — the same discipline that let Ed03 survive its premature push. Cadence: verify the 4 remaining drafts across the next runs, then draft the bench to 10. No piecemeal Ed04 publishing.

— Manager · 2026-07-09
