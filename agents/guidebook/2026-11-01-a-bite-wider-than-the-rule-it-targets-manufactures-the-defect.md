# Ruling #123 — A stylesheet is a specification of the markup; and a bite wider than the rule it targets manufactures the defect it was aimed at

**Filed** 2026-11-01, by the daily run, from the standing queue's own head — **item 21 at 15 days**, the
oldest head this board has handed out since 2026-10-25, reached because #116's DEFECT bucket stood empty
for the first time since it was created.
**Family** assertion discipline (the forty-fourth member).
**Earned by** standing assertion **41**, `qa_selector_coverage`, and by two defects this run fabricated and
nearly published as findings.

---

## 1. The instrument, and why its direction is the whole point

Item 21 asked: **how many of the selectors this build ships match nothing on any page we serve?** Ruling
#118 re-specified it before any code existed — *partition first, answer the markup question each orphan
raises, and only then count bytes* — because deleting an orphaned rule destroys the only surviving
statement of what the document was supposed to look like.

The answer, over the full population of 135 served documents: **1 of 399 asserted selectors is dead
weight.** The byte count item 21 asked for is almost nothing, and the instrument is still worth having,
for a reason that only became visible once it ran.

**Every one of the other forty assertions reads an OUTPUT and asks whether the output is right. This one
reads the STYLESHEET and asks whether the stylesheet's own statement ever reaches an output.** That is a
direction, not a refinement, and it is the direction that buys something no other instrument here owns:

> A selector that **stops** matching is a **markup regression.** The rule still states the design; the
> markup walked away from it.

Delete `<h2 class="subhead">Sources</h2>` from all 88 article pages and nothing in this operation notices.
`qa_render` renders what is there. `qa_composition` compares what is there against itself. `qa_census`
counts what is there. Every one of them is green, because the defect is an **absence**, and an absence
leaves nothing in the output to read (#103). This gate reds, because `.subhead` leaves the matched set and
enters an unmatched set the register does not license. Proved: stripping that one class from 88 pages reds
five selectors.

**A stylesheet is a specification of the markup, and it is the only one this repository keeps in
machine-readable form.** The design system's prose (`SYSTEM.md`), the three hand-built article mockups and
the component comments all state intent too, and none of them can be compared against anything by a
machine. The cascade can.

## 2. #118's partition has four buckets, not two, and the two-bucket version would have deleted a non-negotiable

#118 named *superseded* and *orphaned*. Measured against the real population, **27 of the 44 unmatched
selectors are neither.** They are the untaken branch of a template working exactly as designed — and the
set includes `.mark-latin`, `.mark-divider`, `.mark-arabic` and the three `.masthead__mark-*` rules, which
are **the CHARTER's mandated CSS-only typographic fallback for the wordmark.** That fallback is *required*
to match nothing while the wordmark SVG is present. A two-bucket partition must call it residue, and the
action residue invites is deletion. **The specification, honestly applied, would have deleted a
non-negotiable.**

The four classes, as the gate now prints them:

| Class | N | What it means |
|---|---|---|
| CONDITIONAL | 27 | the markup is emitted by a template branch the current content does not take. Matching nothing is the feature. |
| LATENT | 11 | a bare element-type rule for an element the corpus happens not to contain. |
| SUPERSEDED | 5 | the design moved on; the rule is residue. |
| ORPHANED | 1 | the design stands, stated outside the stylesheet, and the markup walked away. |

This is **#57 and #70 pointed at a specification instead of at a count:** *a bucket set is an enumeration
too, and it cannot report a distinction it cannot hold.* #70's amendment asked *where else does this number
live?* — the same question asked of a classification is **which distinctions does my bucket set destroy?**

The LATENT bucket is also how **standing-queue item 57's class is absorbed rather than re-introduced.**
`h4`, `h5` and `h6` match nothing now that items 54 and 58 are closed — 89 of 135 documents were repaired
off `h4` on 10-30 and valence's thirteen on 10-31. Those three rules are defensive, and deleting them is
precisely how the heading-order class returns the day somebody adds a heading.

## 3. The expensive half: two fabricated defects in one hour, both in the same direction

**`hr.rule` was classified ORPHANED first.** The reasoning was clean and wrong: markdown cannot attach a
class, so a `---` in an article body produces a bare `<hr>`, so this rule can never be reached, so the
design must have walked away. To prove it, the run restored "the defect" with

```python
re.sub(r'\bhr\{border:none', 'hr.rule{border:none', css)
```

That substitution rewrote **three rules, not one** — both article templates re-state the thematic break
scoped to their own `.body-main`, with `--space-xl` and `width: 50%`. With all three broken the probe
reported the user agent's inset groove: 2px, `rgb(128,128,128)`, 9px margins. **It read exactly like a
confirmed 160-day published defect on five served pages, four of them Arabic** — including the
one-edition asymmetry item 21's own wording predicts, which is what made it persuasive.

It was not a defect. Measured against the unmodified tree, the five served breaks compute to **1px solid
`rgba(14,27,44,0.18)` with 54px block margins, and have since 2026-05-25.** A one-line CSS change had
already been written and would have shipped.

**`.pullquote` was wrong the same way, on the same reasoning, twenty minutes later.** It was filed as the
day's headline finding: `global.css:243` states the design rule in its own comment — *"Pullquote (one per
piece; the only orange typographic event in the body)"* — the markup exists in all three mockups, two
dedicated tokens exist, and **zero of 88 article pages has one.** Every clause of that is true. The
conclusion was false: both article templates restate **all twelve** of the rule's declarations as
`.body-main :global(blockquote)`, differing only in `max-width` (34ch against 32ch), and **six blockquotes
are served**. The only orange typographic event in the body does reach the reader — through the *element*,
not the *class*.

Binding, and it belongs beside #35, #114 and #115:

1. **An injection is scoped to the rule it targets, and the scope is asserted.** #114 established *assert
   that the injection changed the artefact before running the check on it*. That is necessary and it is not
   sufficient: both of today's bites **did** change the artefact, visibly, and both changed more than they
   named. The assertion to add is **how many** sites the injection touched, against how many it intended.
2. **A bite wider than the rule it targets manufactures the defect it was aimed at, and a manufactured
   defect reads exactly like a found one.** #114 gave *a bite aimed at the specification tests the
   specification*; this is one turn further in — a bite aimed at a defect you have already decided is there
   will find it.
3. **A selector's class is read off what supersedes it, never off the rule's own shape.** Both errors came
   from reasoning about the rule in isolation. The correct procedure costs one grep: search the **built**
   CSS for every rule targeting the *element* the classed rule describes. Both times that grep was decisive
   and both times it was run only after the conclusion was written.
4. **Every SUPERSEDED entry in the register names what superseded it, and every ORPHANED entry names where
   the surviving statement lives.** A class with no named counterpart is an unverified class.

## 4. What all five SUPERSEDED entries turned out to share

One cause: **markdown cannot attach a class.**

The design system was authored as hand-built HTML — `<div class="pullquote">`, `<hr class="rule">`,
`<div class="body-grid body-grid--resumed">` in three mockups. The publication's bodies are markdown
rendered through `<Content />`. So every classed body rule had to be **restated as an element selector
scoped to `.body-main`** (`:global(blockquote)`, `:global(hr)`, `:global(em)`, `:global(h2)`), and the
classed original became residue the cascade can never reach. The thematic break is now stated **three**
times, the pullquote **twice**, in both editions.

That is **2026-10-25's slanted-Arabic shape inverted.** There, the stylesheet said *Arabic is not slanted*
twice, both times per component, and neither statement reached a third instance. Here the per-component
statements are the **only** ones that reach anything and the global statement reaches nothing. Same cause —
a rule restated per component instead of once — opposite symptom. Consolidating the three is a
Designer/Web Developer call and is **standing-queue item 65**, not a change this instrument's author makes
(RUNBOOK: *a fix that changes served bytes is the Web Developer's even when an assertion found it*).

The one true ORPHAN is **`.body-grid--resumed`**: no `:global` restatement, no scoped variant, markup in
all three mockups and in no Astro template. Per #118 it stays, and the markup question it raises is filed
as **item 64**.

## 5. Two further things the build measured

**The harness was wrong before the code was right, for the third instrument running.** The first sweep
reported four `:focus-visible` selectors as dead. `:focus` was stripped with a `\b` boundary, which matches
*inside* `:focus-visible` and leaves `a-visible` — a selector that matches nothing and reads exactly like a
dead rule. Longest-first with a `(?![\w-])` boundary fixes it. #109's *a composition check's error rate is
set by whether it knows the intended assembly* now has a sibling: **a selector check's error rate is set by
whether it knows which parts of a selector are state.**

**Population, not sample, and it cost nothing.** The first design launched Chrome once per page: 135
launches, minutes. The shipped design launches **once**, fetches all 135 documents inside that one context
and parses each with `DOMParser` — **1.9 s for the whole corpus.** Standing-queue item 41 asks *which of
our gating assertions read a SAMPLE rather than a population* — this one answers by construction rather
than by promise, and the answer was also the fast one.

**And what is deliberately NOT asserted (#93):** valence's inline block, 129 of 266 selectors unmatched.
Its markup and its classes are written at runtime by template literals — item 58's closure measured that
directly, 10 of 13 defective headings absent from the served bytes a static parse reads. A static answer
about valence is an answer about the probe, not about the document (09-14). It is printed, with that
sentence attached, and gates nothing.

---

## The rule, in one line

**A stylesheet is a specification of the markup — so a selector that stops matching is a markup regression,
and a classification of unmatched rules must be read off what supersedes each one, never off the rule's own
shape; an injection is scoped to the rule it targets and the scope is asserted, because a bite wider than
its target manufactures the defect it was aimed at and a manufactured defect reads exactly like a found
one.**
