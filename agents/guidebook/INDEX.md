# Guidebook — index of durable working knowledge

**Maintained by:** the Manager, consolidated in the weekly review.
**Last consolidation:** 2026-06-07 (Issue 02 week).
**Purpose:** one entry point to everything the team has learned the hard way. The durable manual (`slow-cadence-publication-guidebook.html`) is the *replicable* model for any subject; the files indexed below are *Madār-specific* verified reference and method. A writer should be able to start any piece, or render any asset, without re-running reconnaissance that has already been done and banked.

---

## 1. Verified primary-source indices (Test 1 pre-cleared at the index level)

| File | Subject | What it gives | Status |
|---|---|---|---|
| `2026-06-06-sierra-leone-tsc-source-index.md` | Sierra Leone TSC / GIS teacher-deployment matching | Institutions (exact names), four named voices (2024–25) with proposed AR transliterations, the 2024 hard figures with the "source from the technical report not the blog" rule, mandatory counter-texture, live source URLs | Externally re-verified 2026-06-06; Issue 02 secondary commissioned off it |
| `2026-06-04-saudi-ece-source-index.md` | Saudi early-childhood (ECE) sourcing landscape | Tiered source map (strategic / institutional / data / operational), the GASTAT 2025 data-led inversion route, binding transliteration rulings for the minister + KG director | Reference; Saudi remains **parked** — operational-tier voice not reachable in open primaries |

Per-draft caveat: Test 1 is re-run per draft. The index pre-clears the *landscape*; the writer re-checks each URL at draft time.

## 2. Production method notes

| File | Method | One-line rule |
|---|---|---|
| `2026-06-05-rendering-stills-to-png.md` | SVG still/tile → PNG via `cairosvg`, no headless browser | Our stills are pure line-art (`grep -c '<text'` == 0) and the wordmark is path-based, so `cairosvg` renders both exactly — pad with paper to 1:1, never crop; always eyeball a 3×3 contact sheet before sign-off |
| `2026-06-07-sourcing-across-egress-boundary.md` | Verifying figures when the primary source host is outside the network allowlist | `WebSearch` corroborates the *spine* but cannot *trace* figures behind egress-blocked hosts — sort every claim into corroborated / quarantined `[[TRACE]]` / discrepancy / attribution-risk; a figure without a traceable primary never enters a draft. Procedural fix: allowlist the source hosts (one founder action) |

## 3. Durable rulings lifted from this week's increments (the generalizable lessons)

These are the transferable rules the source-specific notes paid for. Apply them to *every* future candidate, not just the country they came from:

1. **The operational-not-ceremonial-voice rule (from Sierra Leone).** When a strategy PDF is the candidate, the unpark hinges on finding the person who *runs the mechanism*, datelined 2024+ — not the person who *announced* it. Sierra Leone cleared (Marian Abu, TSC Director of Teacher Management, on classroom impact, Dec 2024); Saudi parked (only the launch/target tier was reachable). Run this test on every "document worth reading slowly" before commissioning.

2. **The tiered-sourcing-asymmetry rule (from Saudi).** For a government-led program with a flagship national target, expect the minister and the target to be over-documented and the classroom to be under-documented — in *both* languages. Plan the sourcing around that asymmetry from the start; do not discover it on day three. When the operational tier is unreachable, consider the **data-led inversion** (let an official statistics report carry the why-now, require only one named operational voice for dignity) before abandoning the candidate.

3. **The render-is-a-method-not-a-gap rule (from the IG tiles).** Before treating an asset class as a capability gap (and a reason to expand the team), confirm it is not simply an un-banked one-time method. Image rendering read as a Designer bottleneck across two runs; it was a `cairosvg` recipe, now banked. Bank the method before escalating the gap.

4. **The egress-boundary sourcing rule (from the Sierra Leone dossier).** When the primary-source host is outside the network allowlist, separate corroboration from tracing: search results can confirm a claim's spine across multiple independent sources but cannot trace an exact figure to its primary. Quarantine untraceable figures as `[[TRACE]]` *up front*, never mid-draft; the Editor must see exactly which claims are load-bearing-but-unverified before any `approved: true`. The clean fix is infrastructural — allowlist the source hosts — not a per-run editorial tax.

## Consolidation note — 2026-06-07

Four loose research increments existed at week's end (Saudi index, rendering method, Sierra Leone index, egress-boundary sourcing method). **No duplicates to prune** — each is distinct and durable. The consolidation this week is (a) this index, giving the team a single entry point, and (b) lifting the four transferable rulings above out of their country-specific notes so they bind generally. The source-index `.md` files are retained as durable reference (they are reference, not transient increments). The durable HTML manual is unchanged this week; its content is the replicable model, and nothing this week revised that model — only Madār's working knowledge grew.

— Manager · 2026-06-07
