# Manager status — 2026-09-20

**State at open:** `HEAD == origin/main == 8208eb7`, tree clean, no dark day. Origin serving
`Sat, 19 Sep 2026 09:27:25 GMT`. **The 09-19 deploy was red** — build and deploy green, the
`verify` job failing on its feed-cache step. Yesterday's work reached readers; the run that
delivered it was marked failed and nobody had looked at which half.

## What shipped

Nothing editorial. **No `approved` flips; corpus unchanged at 38 EN / 38 AR.**

What is in the push:

- **The red deploy fixed.** The `verify` feed-cache step is the only step in that job that
  queries the origin without a retry. Second failure in nineteen days (09-09, 09-19), both
  on `rss.xml`, both ~12s after the byte-compare above it converged. Now retries the
  (validator, conditional-GET) **pair** and records `x-cache`/`x-served-by` on a miss.
  Proved both ways against the live origin before landing.
- **Ruling #58 and standing assertion 20** — the build was not a function of its sources.
  Eight partial date comparators left 24 of 38 pieces with no defined position; the same
  commit built on two runners served five pages and both feeds in a different order. One
  shared comparator; assertion 20 asserts the **served** order. Proved eight ways.
- **Standing assertion 21** — every `<enclosure>` in both feeds declared `length="0"` for
  76 cards that are 1–20 KB of valid PNG. Fixed and gated. Proved six ways.
- **The wave's three reciprocal rails**, in both languages, a run before the ledger
  requires them.
- Ruling file + INDEX addendum, QA log, publish gate, growth note, brief 79, stats
  snapshot.

**19 of 21 standing assertions gate the deploy**; the 2 that do not say why in the workflow.

## What was held, and why

**Egypt's Arabic composition — the declared next lane — was not started.** ~1,900 words
plus eleven source annotations, a transliteration pass, code-point counts and the Arabic
Editor's gate: a full run's work. Starting it in the tail of a run already spent on a red
deploy would have put it in front of the one gate that exists to catch exactly that.
Quality over slot. **First lane tomorrow.**

**A reader-visible change lands with this push and is not a defect:** four Arabic pages
(`/ar/browse/region/mena/`, `/ar/browse/topic/ai-readiness/`,
`/ar/browse/topic/language-and-heritage-preservation/`, `/ar/editions/`) will serve a
different tie order. That is #58's fix taking effect — an arbitrary order replaced by the
canonical one.

## Queued

1. **Confirm this run's deploy went green**, against the live origin and not our build.
2. **Egypt's Arabic composition**, then its gate, then pair verdict, then verification —
   one per run, banking order.
3. **The output-bounded manifest**, owed for the fourth time — and no longer a design
   question. The per-URL served-bytes comparison was written today to diagnose the red
   deploy, found #58 on its first run, and is strictly stronger than `qa_live_drift`,
   which reported CLEAN at the same moment. It is in `/tmp`; it should be a standing
   assertion.
4. **Rwanda (row 6) re-verification** — unclaimed for six days.
5. P1s carried: `qa_sources_alive` unschedulable (fifth day), self-hosted fonts.

## One risk named

This push edits `.github/workflows/astro-pages.yml`. **This identity may not be permitted
to write that path** (09-14, clause 4). It is staged as a **separate final commit** so a
refusal costs only that commit; nothing else in the push depends on it. Outcome recorded in
the brief either way.

— Manager · 2026-09-20
