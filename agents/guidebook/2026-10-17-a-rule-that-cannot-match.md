# Ruling #103 — a rule that cannot match is indistinguishable from a rule that matches and does nothing

**Filed** 2026-10-17, by the daily run, from the standing queue's own head (item 10, 7 days,
five displacements). **Family:** assertion discipline — *how a check earns trust* — of which
it is the thirty-fourth member. **Cited from, not counted in:** the enumeration family
(*a green check is scoped to what it enumerates*).

---

## What was true

From the first publish on **2026-05-25 until today — 145 days** — every Arabic page in this
publication computed its body font as **`Newsreader`**, a Latin face that contains no Arabic
glyph, so any Arabic text in an element with no `font-family` rule of its own fell through the
Latin stack and was drawn by whatever serif the reader's system happened to supply. Not Amiri.
Amiri is the face this publication chose for Arabic, self-hosts, ships 34 subset files for,
and guards with a standing assertion.

Measured in a browser rather than reasoned from the stylesheet:

```
EN article   html: Times New Roman   body: Newsreader
AR article   html: Amiri             body: Newsreader     <-- 145 days
AR home      html: Amiri             body: Newsreader
```

`global.css` has carried `[dir="rtl"] { font-family: var(--font-arabic); }` since the
beginning, and `dir="rtl"` is on `<html>`. It was meant to hand Amiri down the whole
document. It never reached `<body>`, because:

> **A declaration that matches an element always beats a value that element inherits,**
> whatever the two selectors' specificities are.

`body { font-family: var(--font-body) }` matches `<body>` directly. `[dir="rtl"]` matches
`<html>` and only offers `<body>` an inheritance. Specificity never entered it — the two
rules were never in competition, which is why reading them side by side does not show the
defect and computing the style does.

## And three more rules written for the Arabic edition never matched at all

Found while fixing the first. `SiteFooter.astro` carries `[dir="rtl"] .site-footer__links`
twice, in its base rules and in its mobile media query. Astro scopes component styles by
attaching the component's own `data-astro-cid` attribute, and it attached it **to the bare
`[dir="rtl"]`** — which is `<html>`, an element this component does not render and therefore
never carries that attribute. Compiled:

```css
[data-astro-cid-gcn2mc3v][dir=rtl] .site-footer__links[data-astro-cid-gcn2mc3v] { … }
```

A selector that cannot match any document this build will ever produce. `ShareRail.astro`
writes `:global([dir="rtl"])` and has since it was written; `RelatedReading.astro` puts the
attribute on its own `<nav>` and is fine. `SiteFooter.astro` did neither, so the Arabic
footer's link alignment has never once applied.

**Both halves are the same defect in two costumes: a rule that is in the stylesheet and not
in the cascade.**

## What it cost the reader, measured

Because `<body>` declared a Latin face, the browser fetched it — on every Arabic page, to
draw nothing. Observed network fetches in headless Chrome, confirmed twice by two independent
methods (see limb two), before and after:

| | before | after | delta |
|---|---|---|---|
| AR article, median of all 44 | 574,500 | **295,628** | **−278,872 (−48.5%)** |
| AR article, heaviest of 44 | 825,868 | 546,996 | −278,872 |
| AR home | 705,600 | 426,728 | −278,872 |
| AR editions | 613,760 | 334,888 | −278,872 |
| AR browse | 521,136 | 261,808 | −259,328 |
| **EN article, all 44 — min / median / max** | **487,672 / 521,408 / 703,556** | **487,672 / 521,408 / 703,556** | **0, in every statistic** |

The Arabic edition was **heavier than the English** (574,500 against 521,408 at the median)
and is now **43% lighter**. The control is the whole English population, not a sampled member.

## Why nothing we own could see it

Three of this operation's standing assertions drive a real browser over Arabic pages.

* **`qa_arabic_shaping`** reads **computed style** — and it exists *because of this exact
  defect class.* Its own note in `global.css`, written 2026-09-17, says the worst instances
  *"arrived by inheritance from a `body` rule that names no component at all."* It reads
  computed **`letter-spacing`**. It has stood **one CSS property away** from this for 30 days.
* **`qa_ar_language`** asks which **language** a string is in. Every string here was correctly
  Arabic. It has nothing to say about which face drew it.
* **`qa_render`** counts accent pixels in a band. A different serif in the same colour is
  invisible to it.

And the general form, which is the part worth carrying:

> **Every instrument this operation owns reads an OUTPUT. A rule that never matched leaves
> nothing in the output to read — it fails by looking exactly like a rule whose effect was
> already satisfied.** A green check cannot distinguish *the page is as the stylesheet
> intends* from *the stylesheet's intent never reached the page*. The only instruments that
> can are computed style read against the declaration's **intent**, and the compiled selector
> read against the document it claims to select.

Tenth-plus statement of *a green check is scoped to what it enumerates*, one turn further out
than #93: #93 asked which gating assertion is wired where it cannot observe its subject. This
asks **which of our own written intentions has never been observed at all.**

## Limb two — the probe was inside the thing it measured, and that was tested rather than assumed

The method for all of the above is the one the 2026-10-10 growth note used: copy a built page,
append a script that reads `performance.getEntriesByType('resource')`, serve over loopback to
headless Chrome. **For a font measurement that probe is a hazard**, because the injected
`<script>` is Latin text in an element inheriting the body's Latin font stack — the instrument
can pull the very face it is counting.

So it was measured both ways: the injected probe, and **the loopback server's own access log
with nothing injected into the page at all.** Identical on all four pages — 778,376 / 705,600 /
521,408 / 805,568, file for file. The suspicion was wrong and the 10-10 method is cleared.

**And one reading was not reproducible.** A single run reported the English home at 646,408
over 9 files instead of 778,376 over 12 — it had dropped exactly the three `latin-ext` subsets,
which are the last files discovered during layout. On a page that could not have changed, under
a fix whose whole claim was *bytes went down*, **it had the precise shape of a success.** Three
consecutive repeats returned 778,376/12, matching four earlier readings.

> **A measurement that moves on a control is a measurement, not a finding** — and the cheapest
> defence against a flaky instrument is to carry a control that cannot legitimately move, and to
> re-read it rather than the result you were hoping for.

This is #35's *prove it both ways* pointed at the **instrument** rather than at the assertion,
and it is why the before/after table above reports the English population at all.

## Binding

1. **An assertion that reads computed style names the properties it reads, and a property it
   does not read is not covered by it** — `qa_arabic_shaping`'s coverage is `letter-spacing`,
   and saying so is the precondition for anyone noticing `font-family` was never in it.
2. **A component's scoped style that keys on an ancestor the component does not render uses
   `:global()`** — the idiom is already in this repository, in `ShareRail.astro`. A bare
   attribute selector on `<html>` inside a scoped block compiles to a selector that cannot match.
3. **Where a stylesheet states an intent for an edition, that intent is verified on the
   rendered page of that edition, in computed style** — not read back out of the CSS, which is
   where the intent already demonstrably is.
4. **A reader-byte claim carries the population it was taken over and a control that cannot
   legitimately move** — one sampled page reported as a property of 118 is the defect this
   ruling's own queue item was specified by (see #104's sibling note on item 10).

Links: [[2026-09-13-a-hand-run-assertion-is-a-habit]] · [[2026-10-10-the-bridge-that-carries-the-verdict]] ·
[[2026-10-17-the-house-spelling-is-not-ours-to-apply]]
