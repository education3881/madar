# Ruling #118 — The evidence that diagnoses a layout defect is the part you were going to discard

**Filed** 2026-10-27, from the standing queue's own head — item 27 at 8 days, the second served DEFECT
ever to take a head under ruling #116, and the first whose whole subject is the founder-facing corpus.
**Family:** assertion discipline — the **thirty-sixth** member.
**Cites:** #103 (a rule that cannot match is indistinguishable from a rule that matches and does
nothing) · #35 (prove an assertion both ways) · the 2026-09-14 bite trap · #101 clause 4 (a correction
is written in the register's own words) · #93 (a floor above today's reality reds every build).

---

## The rule, in one line

**A layout defect has two authorities — what the document was supposed to look like, and what it
actually did — and in this repository both of them live in artefacts the operation is inclined to treat
as disposable: the CSS rule that matches nothing, and the pre-repair file in git.**

## What happened

Standing-queue item 27 named **25 founder-facing artefacts that render broken at 1280px** and **two**
mechanisms. Repairing them found **three**, and each of the three was diagnosed by reading something
that an efficiency pass would have deleted.

### Limb 1 — the unmatched selector is the specification

**The push-block seven (2026-08-10 → 08-18).** These seven briefs write the founder's one copy-paste
action as `<pre class="push">`. **`.push` is not styled in any of the seven stylesheets.** The element
therefore fell back to the user-agent `pre` default — wraps nothing, scrolls nothing — and the
unbreakable `cd "/Users/vini/Documents/Claude/Projects/Educational Website"` line made those documents
**7,277 to 34,254 px wider than the 1280px viewport** for 62 days.

And sitting three inches above it in every one of those same seven stylesheets:

```css
.push-block { background: var(--color-ink); color: var(--color-paper); … }
.push-block code { display: block; font-family: var(--font-mono); font-size: 12.5px;
                   overflow-x: auto; white-space: pre;
                   border-inline-start: 2px solid var(--color-orange); }
```

**106 of the 116 briefs use `.push-block`, including every brief written before 08-10 and every brief
written after 08-18.** The seven are a contiguous template regression: the markup walked away from its
own stylesheet for seven days and walked back, and nobody noticed the departure or the return.

**The same shape, a second time, in the same window.** Looking at the repaired 08-17 render — the
RUNBOOK's 2026-08-23 rule, *open it and look at it* — showed the document still rendering edge to edge.
`.container { max-width: var(--container-max); margin-inline: auto; padding-inline: … }` is in the
stylesheet of **both** 08-16 and 08-17, and `<main class="container">` is in the markup of neither:
08-16 kept the orphaned closing tag, 08-17 lost both. **That is the exact defect the 2026-08-23
founder-facing perimeter rule was written about** — *the two briefs that followed rendered edge to
edge* — and the rule was written, the perimeter was asserted, and **the two artefacts that earned the
rule were never repaired.** Both are fixed here.

**Why this inverts a live queue item.** Standing-queue item 21 asks *how many of the selectors this
build ships match nothing on any page we serve?*, and it asks it as a **payload** question — dead
weight, bytes to reclaim. #103 sharpened it to an **observability** question: a rule that never matched
leaves nothing in the output, so no instrument of ours can see it. Today adds the third and opposite
reading, and it is the useful one: **an unmatched selector is a statement of design intent that the
markup has stopped honouring.** It is not dead. It is the only surviving record of what the document
was supposed to look like, and it is therefore the thing that tells a repair what to do.

Concretely: I did not have to invent a treatment for `pre.push`. The stylesheet already said what a
push block looks like in this publication — ink ground, paper type, 12.5px mono, a 2px orange rule on
the inline start, and the overflow **held in a scrolling box rather than wrapped**, because a shell
line is copied and a soft wrap invites a reader to retype it. The repair is that rule collapsed onto
the single element the markup kept. **This is #101 clause 4 — *a correction is written in the
register's own words* — with the stylesheet as the register.**

**So the disposition changes.** Before deleting an unmatched rule, ask which of the two kinds it is:
*superseded* (the design moved on and the rule is residue) or *orphaned* (the design stands and the
markup moved away). The second kind is a **defect report nobody filed**, and an efficiency pass that
sweeps it away deletes the diagnosis along with the bytes. Item 21 is therefore re-specified in the
queue: its first output is not a byte count, it is a partition.

### Limb 2 — a bite rebuilt by hand tests the diagnosis, not the defect

Promoting the overflow limb of standing assertion 33 from *measured* to *asserted* needs the bite
proved (#35). I had the mechanism correctly diagnosed and written down, so I reconstructed it: on a
repaired brief I put `display: grid; grid-template-columns: 1.5rem 1fr` back onto `.twin li`.

**The injection changed the file — 10 bytes, asserted before the run, per the 2026-09-14 trap — and the
check exited 0.** A clean control, a changed artefact, and no bite. That reads exactly like a check
that does not work.

The check was fine. **The reconstruction restored one half of a two-part mechanism.** The defect is
grid blockification *plus* a `::before` bullet that is itself an in-flow grid item: the generated box
takes cell (1,1), which pushes the first inline run into cell (1,2) and the next one into (2,1) — the
24px column — where it overflows. My repair had taken the bullet **out of flow**, and my injection put
back only the `display: grid`. With the bullet absolutely positioned, the first text run lands in the
narrow column instead, and text wraps, so nothing overflows. One correct half of a correct diagnosis
produced a *different, harmless* layout.

Replaced with `git show HEAD:<path>` — the literal published artefact — the bite was immediate and
exact: `<strong> overflows its 27px box by 65px: 'RUNBOOK Researcher-wiring'`. Bite 2, the 62-day
push-block defect restored the same way, reported `document 34254px wider than the 1280px viewport`.
**Two bites red, four controls green, each injection asserted to have changed the artefact first.**

**The rule: when the defect is in version control, the bite is `git show`, never a reconstruction.** A
hand-built injection is a model of the defect, and a model is exactly as complete as the understanding
that built it — so it tests the diagnosis and reports the result as though it had tested the check. It
is the 2026-09-14 trap's third form. That trap has now appeared three ways: an injection that **did not
change the artefact** (09-14), an injection that **changed the wrong thing** (2026-10-24, outside the
brackets the check read), and now an injection that **changed the right thing by half**. All three exit
0. All three read as a passing control.

## What was asserted, and what deliberately was not

The baseline is emptied and limb B of standing assertion 33 **gates** from `postbuild` from today. Its
two stated reasons for not gating have moved in opposite directions and only one survives:

* *There is an excused population of 25.* **Gone** — all 25 are repaired, 136 of 136 render clean, and
  the floor now sits **at** today's reality rather than above it, which is the condition #93 names for
  a measurement to become a gate.
* *The probe cannot be shown to bite on the class it was commissioned for.* **Still true**, and still
  standing-queue item 28: `scrollWidth` is silent on inline text overflowing an `overflow: visible`
  block. But **a blind spot is a gap in sensitivity, never a source of false positives**, and the class
  the probe *can* see produced every defect it has ever found. So the limb gates on strictly less than
  its own name, and the tool now says so in its output: *no artefact overflows in a way `scrollWidth`
  reports.* The rest is item 28's.

**An assertion that catches one of two mechanisms is worth more than a measurement that catches
neither.**

## The third mechanism, recorded because the item named only two

Item 27 and the tool's own comment both describe the eighteenth non-push member as a `li { display:
grid }` artefact. **`agents/reviews/2026-09-20-weekly-review.html` contains no such rule.** Its overflow
is a `<table>` whose min-content width is 19px wider than its section, driven by **a full prose sentence
inside a `<td class="n">`**, where `.n` is the review's own *numeric cell* class and carries
`white-space: nowrap`. The repair is markup, not CSS: the cell is prose, so it loses the numeric-cell
class and the number inside it takes `<span class="num">`, which is what the same table's other rows
already do. *A population described by its dominant mechanism will have members that are not that
mechanism, and they are found by repairing it rather than by counting it.*

## Measured

| | |
|---|---|
| Artefacts rendered at 1280px | **136** (116 briefs, 20 reviews) |
| Overflowing on arrival | **25** (baseline set 2026-10-19) |
| Overflowing after repair | **0** — 136 of 136 |
| Mechanism 1, unstyled `pre.push` | **7** briefs, 2026-08-10 → 08-18, 7,277–34,254 px past the viewport, 62 days |
| Mechanism 2, grid-blockified inline | **17** briefs, 2026-05-28 → 06-17, 11–190 px past a 24px column, up to 152 days |
| Mechanism 3, prose in a `nowrap` numeric cell | **1** review, 19 px |
| Also repaired, found by looking rather than by the probe | **2** briefs with no `<main class="container">` at all (08-16, 08-17) |
| Briefs using `.push-block` | **106 of 116** — the seven are a contiguous regression, not a transition |
| Bites | 2 red, both the literal published defect from `git show` |
| Controls | 4 green |
| Reconstructed bites that did not bite | **1** |

## Where this binds

1. **Before deleting a selector that matches nothing, partition it** — *superseded* or *orphaned*. An
   orphaned rule is an unfiled defect report about the markup, and it is deleted only after the markup
   question it raises has been answered.
2. **A repair to a styled artefact is written in the stylesheet's own words** where the stylesheet
   still states the intent, exactly as a correction to a name is written in the register's own words
   (#101 clause 4). Inventing a third treatment is how a corpus acquires a fourth.
3. **Where the defect exists in version control, the bite is the artefact restored from it.** A
   reconstruction is permitted only where no instance was ever committed, and then the run says so.
4. **A rule written about an artefact does not repair that artefact.** The 2026-08-23 perimeter rule
   named two broken briefs, built a standing perimeter around the whole family, and left both of them
   broken for 65 days. *A correction reaches the instance it was sent to; only an instrument reaches
   the class* (#113) — **and an instrument reaches the class only if somebody then repairs it.**
