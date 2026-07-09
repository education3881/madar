# Ed04 verification — United States · "Two rulers, one word" (NAEP honesty gap)
**Date:** 2026-07-09 · **Method:** drafter ≠ verifier · **Verifier:** Manager (independent audit against the research record)
**Source of truth checked against:** `content-drafts/recon/2026-07-06-us-naep-honesty-gap.md` + the draft's own `sources:` ledger
**Draft state:** `web/src/content/articles/2026-07-07-us-naep-honesty-gap.md` — `edition: 4`, `approved: false` (correctly held)

## Why this piece, this run
Edition 03 shipped and cleared its retroactive gate (10/10). The sprint's own finding was that **verification, not drafting, is the binding constraint** — so the disciplined pipeline advance is to audit what is already drafted, not to draft more. This is the first Edition 04 piece taken through independent verification. It is the edition's thematic flagship ("the measurement question"): what the word *proficient* means when fifty-one systems each define it.

## Checks (each figure traced to the record; no re-drafting)
1. **Central instrument** — "Mapping State Proficiency Standards Onto the NAEP Scales" (NCES 2026-014, Feb 2026), maps each state's *proficient* cut onto the NAEP scale using same-year (2022) data. Draft ¶1–2 match recon §1. ✓
2. **Grade-4 reading map** — 6 systems at NAEP Proficient (AK, DC, IL, MA, OK, RI); 2 below NAEP Basic (IA, VA); strict-to-lenient spread **49 NAEP points**, wider than the **30-point** Basic→Proficient distance. Draft ¶3 = recon §2 exactly. **Internal arithmetic reconciles:** 49 > 30, so "scattered across more distance than the ruler's own distance between two words" holds. ✓
3. **NAEP 2024 read** — 31% of G4 at/above Proficient (reading); −2 pts both grades vs 2022; ~40% of G4 below Basic (largest since 2002); ~⅓ of G8 below Basic (largest ever); math +2 at G4 (~40% Proficient), flat at G8; no state gained in reading; only Louisiana (G4 reading) and Alabama (G4 math) above 2019. Draft ¶3 = recon §2. ✓
4. **Oklahoma** — after a 2024 cut-score lowering, the Commission for Educational Quality and Accountability voted unanimously (May 2025) to restore the 2017–2023 NAEP-aligned cuts ("truth and transparency"). Draft ¶4 = recon §2. ✓
5. **Route-2 discipline (counter-direction)** — the draft says "several states recalibrating benchmarks downward" and **declines to name a specific second state**, exactly as recon §6 required (Wisconsin/any named mover must be verified on its own DOE page; not load-bearing here). Correctly generalised. ✓
6. **Three self-protecting cautions present** (¶5): NAEP Proficient ≠ grade level; the study is explicitly "not an evaluation" of state assessments; NAEP achievement levels are statutorily "trial basis." All three required by recon §6; all three carried. The piece protects itself against the very error it describes. ✓
7. **"Honesty gap"** attributed to the Collaborative for Student Success as an advocacy coinage, and explicitly declined ("follows the study rather than the slogan"). ✓
8. **Zero-partisan guardrail (founder rule)** — the 2025 turbulence (LTT age-17 cancelled, field ops ended 19 Feb 2025; the commissioner placed on paid leave; April 2025 scope cuts; the schedule trimmed through 2033) is reported as dated institutional events. **No party named; no motive ascribed.** ¶6 holds the guardrail. ✓
9. **Operator voice** — Patrick Kelly (NAGB member + serving AP U.S. Government teacher, S.C.), quote verbatim from the 29 Jan 2025 NAGB release, correctly tiered (holds the ruler *and* a classroom). ✓
10. **Dek vs body** — dek claims only what the body proves (cross-state flip; Feb 2026 study; most bars at Basic). Not stronger than body; ≤200 incl. spacing (passed the dek scan). ✓

## One housekeeping item (NOT a defect — graceful-filtered)
- The draft's `related:` list points to `2026-07-07-netherlands-doorstroomtoets`, a **reconned-but-not-drafted** Ed04 sibling. The RelatedReading component filters any slug that is not approved-and-existing, so it degrades silently today. **Reconcile at the Ed04 ship gate:** either Netherlands ships in the same wave, or prune this ref before flipping `approved: true`.

## Verdict
**CLEARS the rubric — verified, HOLD for the Edition 04 wave.** Every figure traces; arithmetic reconciles; guardrails and cautions all present; operator voice verbatim and correctly tiered. It does not ship solo — Editions publish as complete waves — so it stays `approved: false` until Ed04 is complete (10/10) and gated. **1 of 5 drafted Ed04 pieces now independently verified.**

— Manager / verification wave · 2026-07-09
