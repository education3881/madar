# Edition 04 — "The measurement question" · status & completion plan
**As of:** 2026-07-22 · **Manager** · Ed03 is shipped/live/gated; Ed04 is the next wave, mid-build and correctly held.
**07-22 update:** **bench draft 1 shipped — netherlands-doorstroomtoets** ("The test that grades the advice"; the reform that changed the *job* of the test — a legal duty to revise the teacher's track advice upward when the test outscores it; three cycles in, the lever moves but its grip is uneven by region and class). Editor five-test **APPROVE for the wave** on file (`content-drafts/verdicts/2026-07-22-netherlands-doorstroomtoets.md`); held `approved: false`; **all load-bearing figures live-re-verified** before compose (Inspectorate speech read as text — IJsselstein 8/10 vs Stadskanaal 4/10 verbatim, Oppers confirmed as Inspector-General 15 Apr 2026; PO-Raad rapportage read in full — schoolweging paradox + both Dries quotes + 2029/2030 convergence). **Resolves us-naep's forward `related:` ref** (no more orphan). Ruling **#25** filed (*a conditional rate carries its condition* — eligibility rate ≠ event-given-eligibility rate; +INDEX). **Slate = 7 drafted / 6 verified** — Netherlands enters the Verifier queue as the one unverified draft (pacing 1, well under ≤3). QA: build 65pp exit 0, parity 30=30, held-leak zero; one P1 (250-char dek → schema cap 200) found+fixed same-run. Bench remaining: **3** to reach 10 (england-report-cards / japan-assessment-cbt lead).
**07-17 baseline below.**
**07-16 update:** bench drafting has begun — **australia-naplan-reset drafted** (Editor five-test APPROVE for the wave on file; Verifier trace list attached; held `approved: false`). Slate = **6 drafted / 4 verified**; pacing 2 unverified (NZ date-bound 20 Jul + Australia), under the ≤3 ceiling. Bench remaining: ~4 to reach 10.
**07-21 update:** **nz-ncea-corequisite CLEARED on scoped re-check** — NZQA's 20 Jul Writing/Numeracy release landed; the canonical tables now carry Event 1 2026 (reading 60.5%, writing 56.8%, numeracy 51.7% — the series' first backward steps). Closing line re-cut on the actual numbers per the 07-13 verdict, both surfaces; ledger reconciled (verdict: `2026-07-21-ed04-nz-ncea-scoped-recheck.md`). **Slate = 6 drafted / 6 verified — drafted-slate verification is COMPLETE.** The binding constraint is now wholly bench drafting (~4 to reach 10), AR (5 of 6 lack it), stills (10), editions.ts, gate. Bench lane clear: england-report-cards or netherlands-doorstroomtoets lead.
**07-17 update:** **australia-naplan-reset verified** — the Verifier's third verdict: FAIL one item (2024 volumes carried "more than 1.3 million students"; the register says "almost" — 2025 is the "over" year) → fixed same-run on both surfaces → **CLEARED** (ruling #23, *an approximation has a direction*). Slate = **6 drafted / 5 verified**; the only open verdict is NZ's date-bound scoped re-check (NZQA, **20 Jul** — three days out). Pacing: 1 unverified, well under the ≤3 ceiling — **the bench lane is clear for draft 2** (england-report-cards or netherlands-doorstroomtoets lead the recon bench). Note for the gate: NAPLAN 2026 platform outage (11 Mar) surfaced in coverage — the piece's fenced claims survive it; re-check the ACARA newsroom at gate per recon §6.

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
| nz-ncea-corequisite | New Zealand | the standalone literacy/numeracy co-requisite gate that outlived NCEA | **✓ 2026-07-21 (scoped re-check CLEARED; 07-13 FAIL items 1+2 both closed; Event 1 2026 figures in print)** |
| chile-simce-return | Chile | census assessment returns from suspension carrying "more than scores" | **✓ 2026-07-15 (verdict on file; FAIL 1 item → fixed same-run → CLEARED; live re-fetch)** |
| australia-naplan-reset | Australia | the 2023 proficiency reset — a raised bar, a self-declared series break, three cycles of stillness | **✓ 2026-07-17 (verdict on file; FAIL 1 item — approximation direction — → fixed same-run both surfaces → CLEARED; live re-fetch)** |

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
