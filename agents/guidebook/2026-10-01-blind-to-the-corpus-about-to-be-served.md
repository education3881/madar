# Ruling #81 — an assertion scoped to the served corpus is blind to the corpus that is about to be served

**Filed:** 2026-10-01, by the QA lane, answering the 2026-09-30 forward question and finding the
defect on the way.
**Artefact:** `agents/tools/qa_pair_frontmatter.py` — standing assertion 28, the second of the
twenty-eight to read source files rather than `dist`, wired into `postbuild` in the same commit that
proved it.
**Family:** enumeration — *a green check is scoped to what it enumerates* — as its seventh numbered
member, and the first to point at the **direction of time** rather than at a surface.
**Cousins:** the 2026-08-09 flag-sweep inversion (whose exact mirror this is), the 08-16 chrome 404,
the 08-17 orphan sweep, the 08-18 consumer-format rule, the 08-23 artefact-perimeter rule, the
09-06 held-file rule, #50 (*a correction has a blast radius*), #42 (*a pair carries only what both
languages share*).

---

## The ruling

The 2026-08-09 rule says an assertion is scoped to a **corpus state**, and that when the state
changes the assertion must be re-derived rather than re-run — because a held-mode sweep passes
vacuously the moment there is nothing held left to leak. **This is the same sentence read in the
other direction, and it is the half nobody had written down:**

> An assertion that reads `dist` cannot see a defect in a file that `dist` does not contain. A held
> piece is exactly such a file. So **every assertion scoped to the served corpus is structurally
> blind to the corpus that is about to be served** — and a wave that flips as one commit changes the
> served corpus by six pairs in a single step, with twenty-five gates downstream of it and, until
> today, **none upstream.**

The arithmetic, counted rather than asserted: **22 of the 25 gating assertions are handed `web/dist`**
— twelve build steps plus ten of the thirteen `postbuild` entries — and `dist` contains no held piece.
Five of them do reach back into `web/src/content/**` (`qa_geo_fields`, `qa_held_assets`,
`qa_stable_order`, `qa_packet_figures`, and now `qa_pair_frontmatter`), **but every one of those reads
a held piece for a frontmatter fact.** Not one assertion has ever examined the HTML a held piece will
serve, for the plain reason that the HTML does not exist until the flip. So the surfaces this
morning's defect lives on — the hreflang cluster, the JSON-LD translation node, the cross-language
link — meet the wave **for the first time on flip day**, the one day of the edition on which a failure
is most expensive and least expected, after four gates per piece have already passed.

*(That sentence is narrower than the one first written here, which said twenty-three of twenty-four
assertions read `dist`. It was corrected before the commit by counting both homes instead of
remembering them — the same correction this register has now made four days running.)*

---

## The case

`qa_pair_frontmatter` was written to answer a different question (see #82's sibling note and the
2026-09-30 QA log: *which claims in `sources[]` are machine-checkable against the document?*). On its
first run over the content collection it found, in a field nobody was looking at:

**`2026-09-19-egypt-baccalaureate-published-first` carried no `arabicVersion:`** — alone among 44
English articles. Its Arabic twin pointed at it. It pointed at nothing. Banked 09-22, verified 09-23,
held, and ten days from a gate.

`arabicVersion` is `.optional()` in the schema, and `web/src/pages/articles/[...slug].astro` derives
three things from it. **Measured, not inferred** — by flipping the pair to `approved: true` in a
scratch build and reading the served bytes both ways:

| served on the EN page | with the field | without it |
|---|---|---|
| `<link rel="alternate" hreflang=…>` | **3** (en, ar, x-default) | **0** |
| `workTranslation` node in the article JSON-LD | **1** | **0** |
| in-page cross-language link to the Arabic twin | **1** | **0** |

So the pair would have shipped one-way: the Arabic page linking to the English, the English page
declaring no Arabic edition at all — on the publication whose own growth doctrine calls Arabic *a
distribution advantage, not just a translation cost*.

**Why nothing caught it, which is the ruling rather than the anecdote.** `qa_hreflang_clusters`
enumerates built pages and has been green every day. It is green *because* Egypt is not built. The
check is correct, its population is correct, and its answer is about 38 approved pairs — a set that
does not include the six pairs about to join it.

### The two traps inside the investigation, both recorded because they nearly inverted the finding

1. **The first served-side bite did not bite, and the reason was my own pattern.** Grepping for
   `ar/articles/2026-09-19` reported two matches on the bitten page — because `m`**`ad`**`ar/articles/…`
   contains it. That is the 2026-09-14 masking rule (*where does the string I am looking for also
   legitimately appear?*) committed again, on the input side, by the run that was quoting it. The
   finding only resolved when the actual `<link>` elements were printed instead of counted.
2. **The warm-cache warning has two homes.** The 09-30 log diagnosed `[glob-loader] Duplicate id` as
   Astro's content-layer cache and recorded that clearing `web/.astro` removes it. Today it did not;
   the stale entry was in **`web/node_modules/.astro`**, and clearing both gave a build with zero
   warnings. A correct diagnosis that names one of two homes is the #70/#57 shape again, one day
   old.

---

## What changed

* **Standing assertion 28, `qa_pair_frontmatter.py`**, reads `web/src/content/**` — held pieces
  included — and asserts, per pair: reciprocity in **both** directions; byte-identity on every
  frontmatter field that is a fact about the piece (`date`, `edition`, `country`, `countries`,
  `region`, `level`, `type`, `contains_composites`, `approved`, `themes`); the `related:` rail as a
  **sequence**; `hero.src`; and the `sources[]` URL multiset. `title`, `dek` and the hero's `alt` and
  `caption` are deliberately not compared — those are composed, and a pair whose deks matched token
  for token would be the defect.
* **Three legitimate source asymmetries are declared in the tool with their exact URL sets and their
  reasons** (Indonesia, Morocco, Sudan). A declaration is not a blanket exemption: if a declared
  pair's asymmetry changes shape, the check fails and the declaration has to be re-earned. A declared
  pair that no longer exists also fails — a stale exemption is an exemption nobody can fail.
* **Proved both ways before wiring**: eleven fixtures per #79, pinning the population as well as the
  verdict; control silent on 44 pairs / 432 identity fields / 684 source URLs; **seven bites against
  the real tree, each producing exactly one finding, each the finding it named** — including the
  genuine Egypt defect and a rail that is merely **reordered**, which a set comparison reads green.
  Two further bites were aimed at the recogniser itself: dropping `approved` from the identity list
  fails three fixtures, and switching the rail comparison to `sorted()` fails exactly the reorder
  fixture.
* **The gate ratio moves at the point of filing**: 28 standing assertions, **25 gating**, thirteen
  from `postbuild`, derived by `qa_patch_queue` from its three homes.

## The general form

*An assertion is scoped to a corpus state — and "the corpus" always means the one that is already
served.* Before any event that changes that corpus in a single step — a wave flip, a bulk import, a
schema migration — ask which of your gates has ever met the incoming set. If the honest answer is
*none*, the event is not gated; it is merely scheduled.
