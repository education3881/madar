# Ruling #109 — a composition defect lives in no file, and the build can see the collision but never the consequence

**Filed** 2026-10-20 (daily — the head of the standing queue, item 14 at 7 days and seven
displacements, taken by the three-displacement threshold plus age, with item 13 closed beside it).
**Family** Assertion discipline / build determinism — the family's **thirty-seventh** member.
**Instrument** standing assertion 34, `agents/tools/qa_composition.py`, gated from `postbuild`.
**Closes** standing-queue items **14** and **13**.

---

## The ruling

**A composition defect holds of an assembly and of no part, so every instrument that reads one
artefact at a time is structurally incapable of seeing it — and the fix is not a better reader but a
different unit of judgment.** Sort composition defects by *who does the assembling* and the
boundary between what a build can see and what only a render can see falls in exactly one place:

| assembled by | example | visible to |
|---|---|---|
| **the build**, into one document | N inlined fragments → one cascade, one id namespace | the **served bytes** |
| **a consumer**, across documents | the JSON-LD graph a crawler merges; two feeds, one reader; an hreflang cluster | the **served bytes**, read as one document |
| **the layout engine** | which of two matching rules wins; what the winner paints; what overflows | **only a render** |

So the answer to item 14's question — *can the build be made to ask this at all?* — is **yes for two
of the three kinds, and the third is assertion 33's territory.** What a static check can state
honestly is the **collision**; what it cannot state is the **consequence**. That is not a weakness
to apologise for, it is the correct thing to gate: a collision whose consequence is invisible today
becomes visible the day a sixth cover lands, and **the precondition is the half that is still true
before anybody has looked.**

## Where it comes from

The Edition 05 flip's render inspection (2026-10-13, ruling #99) found every edition cover printing
in Edition 01's vermilion. `inlineCover()` injects each cover's markup *including its own `<style>`
block*; five blocks in one document are one cascade; five covers all wrote `.kick`; the last in
document order won for all five. **Every one of the five SVG files was correct standalone.** The
line work was right throughout, because strokes are presentation attributes on the elements
themselves — only the type leaked, which is why four editions of looking at that page never caught
it. The repair scoped each cover under `.ed-cover-NN`. Nothing in the operation would have noticed
the sixth cover omitting that prefix, and that gap is what item 13 asked for and what limb 1 now
closes — **as a property of every served document, of which the covers are today the only instance.**

## The licensing clause, which is the part that is actually new

Item 13 specified *the computed `fill` of each cover's kicker, read out of a real browser through an
iframe* — the instrument the defect was originally measured with. The tool does not use it, and the
reason generalises: **a declared value is the computed value exactly when no other rule in the
document can match the element, which is precisely what limb 1 asserts.** So limb 2 reads the
declared rule and compares it against `web/src/lib/editions.ts`, and **when limb 1 fails, limb 2
prints `NOT ASSERTED` and withholds its reading** rather than reporting a pass it is not entitled
to. A cheap check licensed by a cheaper one is worth more than an expensive check standing alone,
and the licence has to be machine-checked or it is a comment.

This is the fourteenth consecutive closure in which **the specification was not the scope.**

## What was measured, including the four surfaces that came back clean

Written down because a clean surface nobody records is a surface the next run re-checks blind. Over
the real `dist` of 2026-10-20, 135 served documents:

* **inline `<style>` blocks: 13 across 3 documents** — five on each editions page, three on
  `/valence/`. Full-selector collisions: **0**. The surface limb 1 guards is small, and it is small
  for a reason worth knowing: Astro scopes component styles into an external sheet with
  `data-astro-cid-*`, so what is inlined is exactly what the build was told to inline.
* **JSON-LD: 266 distinct `@id`, 2 described (not merely referenced) on more than one page, 0
  disagreements** about any property. This is the one artefact on this site a consumer is
  *explicitly invited* to merge across documents, and nothing had ever compared two pages' claims
  about one node.
* **the two feeds as one subscription: 44 + 44 items, 0 shared `<guid>`, 0 shared `<link>`** — no
  item silently swallowed by a reader who takes both editions.
* **hreflang: 396 alternate links across 132 pages, reciprocity clean**; 134 canonicals and 134
  `og:url` across 135 pages, none shared by two pages. `og:image` *is* shared by 45 pairs and that is
  correct — a pair shares one card by design.

## The second half of the ruling, and it is the expensive half

**A composition check's error rate is set by whether it knows the INTENDED assembly.** The harness
produced two false positives before the code was right, and both read exactly like defects:

1. A first draft collected **bare class tokens** rather than full selectors and reported the
   editions pages as 5-way collisions on `.wm`, `.ar`, `.kick`, `.th`, `.thm`. Those five names *do*
   appear in five blocks — scoped five different ways. **The repair working looked identical to the
   defect.**
2. A facet probe reported **33 of 43 published pieces missing from their country facet page.**
   `web/src/pages/browse/[...path].astro` says in a comment that four countries clear a `>= 2` bar
   and thirty-eight do not and are linked directly to their piece. **A deliberate arrangement read as
   an absence.**

Ruling #35 says *prove the bite as carefully as the control*. This is its input-side twin: **an
assembly whose intended shape you have not been told will report every deliberate arrangement as a
collision**, and a check with that error rate is switched off inside a week. It is why limb 1
compares full selectors rather than names and why limb 2 reads the registry rather than inferring a
palette. It is also #85's shape — *a name's boundary is not a textual property* — moved from names
onto layouts: **an assembly's intent is not a property of its output.**

## Proof

Control green on the real `dist` (135 documents, 13 blocks, 10 cover kicker rules, 5 registry rows).
Three bites, each on a `/tmp` copy, each injection asserted to have changed the artefact **before**
the check ran, per 2026-09-14:

* **bite 1 — the pre-repair state.** `.ed-cover-NN ` scope stripped from every block on the editions
  page: limb 1 red with 5 colliding selectors across blocks 0–4, limb 2 correctly withheld.
* **bite 2 — the historical symptom alone.** Edition 03's kicker set to Edition 01's `#D94F2A` with
  the scoping intact: limb 1 green, limb 2 red and naming the edition.
* **bite 3 — the vacuous-pass trap.** All inline `<style>` blocks removed from both editions pages:
  the tool **refuses** rather than passing on an empty population, because a check that finds nothing
  to check has failed rather than passed (2026-08-16).

## What it does not reach, named so it is not mistaken for covered

The consequence. Whether a collision changes a painted pixel depends on specificity, document order
and whether the element exists on the page at all — all three are the layout engine's answers, and
asking them is standing-queue item 28's business, not this tool's.
