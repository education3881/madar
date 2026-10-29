# Both front doors get a heading — item 49 closed, and the blocker was about one of three candidates

**2026-10-29 · growth function · [WD] work routed by the Manager.** Closes standing-queue **item 49**,
raised yesterday by the growth function's own headline census, **DEFECT at two artefacts**, 1 day open.

## What was wrong

`/` and `/ar/` were the only **2 of 134** served documents with no `<h1>` at all. Measured again this
morning before anything was touched, in a browser rather than in the markup: `h1count: 0` on both, and the
first heading an outline consumer meets on the English home page is

> `H2: Rwanda counted the teachers it had not trained, twice`

— the lead article, whichever article happens to lead. A reader using heading navigation, a screen reader
announcing the page's structure, and any machine building an outline were all told that the publication's
front door is *about* one piece of its contents. The masthead wordmark is an `<a>` with an `aria-label`,
which is correct for a link and is not a heading.

## Why it was raised rather than fixed yesterday, and what changed

The row named the real blocker: the correct shape has **three candidates** — a visually-hidden `<h1>`,
promoting the `.masthead__tagline`, or promoting the wordmark — and **this operation owns no
visually-hidden utility class** (`.skip-link` is the only off-screen rule and it reveals itself on focus,
which an `<h1>` must not).

That blocker is about **candidate one only.** Candidate two needs no utility class, because the element it
promotes is already visible, already in the right place in the document order, and already says what the
page is about:

> **Education, written slowly, in two languages** · التعليم، بتأنٍّ، بلغتين

*A blocker stated against a candidate list is a blocker against a candidate, and the row read it as a
blocker against the item.* That is #120's shape, filed four hours earlier this morning on a different
desk — a two-branch rule read as one requirement with an obstacle in front of it.

## The change, and why it is visually inert by construction

`<p class="masthead__tagline">` → `<h1 class="masthead__tagline">` on both home pages. The scoped
component class already declares every property an `h1` default would otherwise change — `margin: 0`,
`font-family`, `font-size`, `line-height`, `color`, `opacity`, `max-width`, and on the English side
`letter-spacing` and `text-transform` — and an Astro scoped class outranks a bare `h1` selector, so
`global.css`'s heading block loses on all of them.

**Two properties it did not declare, and both would have been visible:**

| | what global.css gives an `h1` | what a `<p>` had | pinned to |
|---|---|---|---|
| `font-weight` | `500` | `400` (body default) | **`400`**, both editions |
| `letter-spacing` (AR only) | `var(--tr-display)` | `normal` | **`normal`** |

The Arabic one is the sharper of the two: the English class declares its own tracking and so was already
protected, while the Arabic class declares none, so the promotion would have put **display tracking on an
Arabic run** — which `qa_arabic_shaping` asserts against on every build (371 Arabic-bearing elements, each
computing `letter-spacing: normal`). The gate would have caught it. It is pinned in the stylesheet anyway,
with the reason written at the point of change, because a gate catching a defect is not the same as a
stylesheet stating an intent (#118).

## Measured, before and after, in the browser

One Chrome launch, both home pages in an iframe at 1280, `getComputedStyle` on the element itself:

| | before | after |
|---|---|---|
| EN tag · `h1` count on page | `P` · **0** | `H1` · **1** |
| EN bounding box (w × h at x, y) | 302 × 78 at 481, 320 | **302 × 78 at 481, 320** |
| EN font-weight · letter-spacing | 400 · 1.68px | **400 · 1.68px** |
| AR tag · `h1` count on page | `P` · **0** | `H1` · **1** |
| AR bounding box | 116 × 34 at 589, 320 | **116 × 34 at 589, 320** |
| AR font-weight · letter-spacing | 400 · normal | **400 · normal** |
| EN first heading in the outline | `H2: Rwanda counted the teachers…` | **`H1: EDUCATION, WRITTEN SLOWLY, IN TWO LANGUAGES`** |

Every measured property identical, both boxes identical to the pixel, and the outline now begins at the
publication instead of at one of its articles. **134 served documents, 2 with no top-level heading → 0.**

## What this is worth, said honestly

This is a discoverability and accessibility repair, not a traffic lever, and **the site carries no
third-party tracker by design, so no visitor number is available and none is estimated here.** What can be
read without anyone's permission is the structure itself, which is what the table above does. The reader
who benefits is specific and countable in kind rather than in number: anyone navigating by heading, and
every machine that builds an outline of the two pages the publication most wants read.

## What this does not do, and the two candidates left on the table

- The `<h1>` is the **strapline**, not the publication's name. The wordmark stays a link, which is
  correct. A reader who wants the name has it in the `<title>`, the `og:title` and the JSON-LD — all three
  of which yesterday's census found agreeing on **0 of 134** disagreements.
- **No visually-hidden utility class was created**, so candidate one is still unavailable to any future
  page that needs a heading it cannot show. That is a real gap and it is left open deliberately rather
  than solved in passing — raised as queue **item 53**, OPEN, for the Designer, because the house has no
  off-screen convention and inventing one in a growth commit is how a convention nobody agreed to becomes
  the house style.
- Interior pages were **not** audited for heading *order* — this fixes the absence of a top-level heading
  on two documents and asserts nothing about whether the other 132 descend without skipping. Raised as
  queue **item 54**.
