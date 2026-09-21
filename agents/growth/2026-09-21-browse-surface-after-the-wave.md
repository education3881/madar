# Growth — what the Edition 05 flip does to the browse surface, read before the flip

**Date:** 2026-09-21 · **Author:** Growth · **Read by:** the Manager at the wave gate
**Why now:** the browse surface is derived from the *approved* corpus at build time. Five held
pieces flip in one commit, and until today nobody had asked what the reader-facing navigation
looks like on the other side of that commit. An index page that appears, disappears or changes
its URL is a discoverability event; discovering one *after* the flip is discovering it from the
outside.

Computed from the content collection with the same derivation the build uses (`expected_facets`
in `qa_stable_order.py`, which is the Python half of `facetsFor`), by flipping every held piece's
flag in memory. Nothing was written to a content file.

## The answer, and it is the good one

```
                 now          after the flip
EN pieces        38           43
AR pieces        38           43
EN facet pages   18           19
AR facet pages   18           19
```

- **One new page, in each language: `/browse/country/sudan/` and `/ar/browse/country/sudan/`.**
  Sudan reaches two pieces — the Edition 03 exam-continuity piece and the new *Cant Wait to
  Learn* piece — and crosses the country threshold.
- **No page is lost. No existing URL changes. No facet row changes its position** except by the
  count moves below, and every move is downward-in-the-list-free: the order after the flip is the
  order before it, with `country/sudan` inserted between `sierra-leone` and
  `united-arab-emirates`.
- **EN and AR are identical, page for page and position for position** — which is what keeps the
  hreflang clusters reciprocal without either side naming the other's slugs, and it is asserted
  every build by `qa_hreflang_clusters`.
- Counts that move: **Africa 5 → 10**, student wellbeing 2 → 3, Egypt 2 → 3, Sierra Leone 2 → 3.

## Two things worth saying out loud

**1. `taxonomy.ts` predicts Africa 5 → 11 and the true figure is 5 → 10.** The comment was written
on 2026-09-14, when the edition's scope had been set at six; five of the six are drafted and the
sixth (Rwanda) is not. The comment is not wrong, it is *early* — it describes the edition, and the
flip describes the drafts. It will read true the day Rwanda lands. Left in place deliberately, with
this note as its date stamp: a prediction in a comment is a promise about a future commit, and the
honest thing is to record which commit it is waiting for.

**2. The continental piece contributes no country page, and that is correct.** Slot 3 carries
`countries: [Mauritius, Senegal, Niger, Benin, South Africa]` and each of those five reaches
exactly one piece — below the two-piece threshold that exists so a facet page never lists a single
article. So the piece that measures five countries adds none to the browse surface, while adding
five to the stats panel's country count. **Those two numbers are answering different questions**
and the tension is the one the 09-18 run routed to the weekly review as a definition question
(*does `countries:` report coverage or mentions?*). Recorded here as the second place it shows up,
which is an argument for answering it rather than carrying it.

## Growth's read

This is the least eventful answer available and it is the one worth having in writing. The wave's
risk was never the new page — it was an existing index URL changing under a reader or a crawler
mid-flip, which is the kind of thing that is invisible until a link rots. **Nothing rots.** The
flip adds one country index in each language and moves four counts.

**Return-rate note, per the standing rule:** the site carries no third-party tracker by design, so
there is no traffic figure to lead with and none is estimated here. What is readable without
anyone's permission is the *structure* — page count, URL stability, EN/AR symmetry — and all three
are now read for the flip in advance rather than after it.

**Owed at the gate, one line for the flip commit:** confirm the post-flip build emits 19 facet
pages per language and that `/browse/country/sudan/` resolves in both. Assertion 20 now asserts
their order, so a permutation fails the build rather than the reader.
