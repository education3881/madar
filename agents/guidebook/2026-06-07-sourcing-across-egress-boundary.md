# Guidebook · Sourcing method — verifying figures when the primary source is outside the sandbox allowlist

**Logged:** 2026-06-07 · **For:** Content Creator, Editor, Manager
**Companion to:** `2026-06-06-sierra-leone-tsc-source-index.md` (the index this method was forced to confront)
**Trigger:** the Sierra Leone TSC dossier (2026-06-07) — the commission's seven hard figures live in a technical-report PDF on `edtechhub.org` / `docs.edtechhub.org` / `documents1.worldbank.org`, all **outside the network allowlist**. `WebSearch` reached the summaries; it could not open the report.

## The increment (the reusable rule)

**When the primary source host is egress-blocked, `WebSearch` corroborates the *spine* but cannot *trace* the figures. Treat the two as different tiers and never let the second leak into a draft.**

Concretely, sort every claim into:
- **Tier 1 — corroborated:** returned by *multiple independent* search results (not one press release). Safe to write, cite the corroborating source.
- **Tier 2 — quarantined:** appears in the brief / index but only in a primary you cannot open. Write it as a `[[TRACE]]` placeholder the Editor will not pass to `approved: true`. **A figure without a traceable primary does not go in the draft** — the standing rule, restated for the egress case.
- **Tier 3 — discrepancy:** an independent source reports the *same metric differently*. Resolve against the primary before writing **either** number.
- **Tier 4 — attribution risk:** a named human / quote that the open sources do not confirm. Hold the voice; do not invent the chairmanship or the quote to keep the colour.

## Two concrete cautions this surfaced

1. **Secondary aggregators round and blend.** The brief's "57% to disadvantaged districts" came back from an independent source as "56% of new posts + 53% of early-years posts to the 10-of-16 disadvantaged districts." Same story, different denominator. A single rounded percentage lifted from a summary is a Test-1 risk; the defensible move is the sourced *construction* ("the majority of new posts… just over half of early-years posts…") until the primary's exact figure is in hand.
2. **"Recruited" ≠ "passed the exam."** The 2,341 figure was reported both ways in secondary summaries. When a cohort number is described two ways, the technical report is the only arbiter — write the conservative claim until then.

## The procedural fix (so this stops being a per-run tax)

The blocker is **infrastructural, not editorial**, and it converts to a single founder action: **allowlist the source hosts** (`edtechhub.org`, `docs.edtechhub.org`, `documents1.worldbank.org`, and `doi.org` for DOI resolution) in Settings → Capabilities. Once allowlisted, a run can open the technical report (DOI .1115), trace the seven figures and the Keifala/Elacqua attributions directly, and the piece drafts to full source in one step. **Carry this to the Sunday weekly review as a standing infrastructure item** — the same way `@astrojs/sitemap` is carried: a one-time route, not a recurring edit.

## The test (did the team get smarter?)

Before today, the egress boundary would have surfaced mid-draft as "why won't this URL open?" Now it is a pre-draft sort: the Content Creator quarantines untraceable figures *up front*, the Editor sees exactly which claims are load-bearing-but-unverified, and the Manager has a named, one-action unblock instead of a vague "sources are hard." That is the increment.

— logged by the Manager · 2026-06-07
