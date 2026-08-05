# Monthly persona review — lessons of the last ~30 days, folded into the team

**Date:** 2026-08-05 · **Author:** Manager · **Prompted by:** founder request — review the month's learned lessons and update each team member's instructions/profile, with special focus on **content quality** and **research**.

**What changed:** a dated *"Lessons carried forward — 2026-08-05"* block was added to all eleven persona files, and one stale fact was corrected (Web Developer's deploy path). Nothing already-correct was removed; every addition ties to a guidebook ruling (#16–#28) or a Verifier verdict from the month, so the changes are traceable, not editorial whim.

---

## The month's spine (where the lessons came from)
The dominant work was the **Ed04 held wave** — eight verified drafts on "the measurement question," now five-of-eight in Arabic — plus the **07-02→07-07 CI outage** and its recovery. Two bodies of learning came out of it:

- **The figure-discipline family (#21–#25):** every load-bearing figure travels with *seven axes* — administration/coverage (#12/#12b), funnel stage (#14), **vintage** (#21, a recount ≠ a revision), **scope** (#22, a qualifier keeps its scope), **direction** (#23, an approximation has a direction), **position** (#24, a series point carries its column + base note), **condition** (#25, a conditional rate carries its condition). All four of the Verifier's FAIL-and-fix catches were *real figures with the wrong companion fact* — catchable only by reading the primary beside the draft.
- **The method + composition families (#19, #20, #26, #27, #28):** guardrail-in-the-sentence (#19); a 404 is an observation with N-of-M re-fetch (#20); an un-quotable dashboard value is not a citation (#26); two independent channels satisfy drafter ≠ verifier (#27); and the Arabic composition/transliteration doctrine (#28a Latin-tagged acronyms, #28b PROVISIONAL for unheard names, plus the name-origin routing extended through Singapore's three origins and Chile's Spanish-vs-Italian split).

---

## Changes by team member

### Content & research cluster (deep — the founder's focus)

**Editor (02).** Test 1 now explicitly checks the *seven figure-axes* and the *in-sentence guardrail* (#19). Codified that the Editor's verdict is "APPROVE for the wave," not the ship gate — the `approved: true` flip is earned by the Verifier's second-channel re-trace (#27) and held by the flag (#18). Dek/schema caps checked at verdict.

**Content Creator (06).** Five amendments to "Your standards": (1) live-re-verify every figure *before compose* — a resolving URL is not a tracing figure; (2) carry the right companion fact on all seven axes; (3) put the guardrail in the sentence (#19); (4) a source you can't quote isn't a citation (#20/#26) + the banked mirror routes; (5) trim the dek at compose.

**Content Creator II (09).** Inherits the 06 addendum; lean-specific note that the non-MENA/comparative slate is assessment-series-heavy (NAPLAN/NCEA/SIMCE/PARAKH/PSLE), exactly where vintage/scope/direction/position bite — draft for a second-channel re-trace.

**Arabic Editor (07).** The Ed04 AR wave's transliteration doctrine bound at Gate 4: #28a (Latin-tagged acronyms), #28b (PROVISIONAL for unheard names), and the name-origin routing including the Latin-American two-origins subtlety (route each name-part by its own origin — Gino Cortez → جينو كورتيس). Composition is now the Arabic Content Creator's; the gate is fresh-eyes verification.

**Arabic Content Creator (10).** Same transliteration routing bound at *compose* time; the "lakh"/magnitude-word carry (glossed once, never silently converted); figures carry their seven axes and in-sentence guardrails in Arabic too.

**Researcher (08).** The index must **pre-flag each figure's fragile axis**, not just its trace tier; §6 guardrails phrased so they can be lifted into a sentence (#19); mirror-verification routes banked as a named pattern (#20/#26) with dashboard-only figures quarantined `[[TRACE]]`; the seven-axes checklist is now Section-1 discipline.

**Verifier (11).** The seven-axis trace is the core method; a clean verdict means *every figure confirmed twice by different routes* (#27), not "found no error"; the un-quotable-dashboard rule (#26); guardrail-in-sentence (#19) + flag-state check including staging duplicates (#18).

### Ops cluster (targeted)

**Manager (01).** Verify-in-the-judging-environment + two-gate deploy (#16/#17); the flag is the hold (#18); verification paces the wave (drafting ≤3 ahead); route around the sandbox lock, never hand-edit the lockfile; run-the-day-autonomously with the brief as proof-of-work; protect the compounding loop.

**Web Developer (03).** A green build ≠ a live site (#16/#17); never hand-edit the lockfile (the EUSAGE outage); the /tmp build route-around is sanctioned; hreflang-in-head + absolute share images are now render contract; zero held-leak is a build invariant. **Corrected the stale stack note** — deploy is GitHub Actions on `main` as of 07-07, not the legacy gh-pages branch.

**Growth (04).** The bilingual internal-link cluster is the best owned discoverability asset (measurement cluster now 5-wide); audit the live surface every run and lead with structure over counts; the two distribution blockers are founder calls that don't block content; kill experiments that return zero (the retired IG grid tile).

**Designer (05).** Hero stills are the current binding gap on Ed04 (ten owed) and stills-on-disk is a hard publish gate (Gate 2) — batch them now, in parallel with the AR path; hold the established still idiom (single-line ink drawing, one kiln-orange mark, fixed caption format, themeable `currentColor`).

---

## The one line to keep
The team is measurably smarter than a month ago in a specific, testable way: **a piece drafted under these rules clears the Verifier in fewer passes, and no deploy is called "live" until the environment that judges it says so.** That is the compounding test the CHARTER sets, and this review is it being paid forward.

— Manager · 2026-08-05
