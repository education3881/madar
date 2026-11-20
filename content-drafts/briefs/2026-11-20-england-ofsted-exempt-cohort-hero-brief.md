# Hero brief and delivery — `2026-11-12-england-ofsted-exempt-cohort`

**Cell 7 of eight. Brief written and executed in the same run, 2026-11-20** (Manager → Designer), against
`content-drafts/briefs/2026-11-12-england-ofsted-exempt-cohort-brief.md` and the three verdicts on file.
The piece carries six conditions on cell 8 and none of them touches the still; cell 7 was the next
content action named in `_STANDING_LEDGER.md`.

## The brief

**Theme.** A regulator stopped measuring one cohort for eight years, went back and measured it with the
instrument of the day, then withdrew that instrument and replaced it with one that does not join to it.

**Dominant emotion.** Not loss. *Discontinuity* — the particular unease of a series that stops.

**What this piece is NOT.** It is not about schools getting worse. Guardrail 1 of the commission is that
there is no composite of the two rulers and the piece may not build one; guardrail 2 is the 17% collision.
**So the still may not be a chart, may not set the two instruments on one axis, and may not encode any
published proportion in any length, pitch or position.** A still whose proportions encoded either
distribution would be a chart of it, which is the Bahrain still's disposition arriving here for a
different reason — there it was a licence, here it is the Editor's refusal of the composite.

**Two refs.** `2026-07-28-england-report-cards-first-term` (the same country, the same regulator, and the
*instrument that reads the instrument* gesture) and `2026-10-23-bahrain-bqa-five-cycles` (the slab-and-tick
vocabulary, and the convention that one warm mark is a pointer carrying no magnitude).

## What was drawn

`design-assets/stills/2026-11-12-england-ofsted-exempt-cohort.svg` — 1200×600, paper-cream ground
(`#FAFAF7`), pure line, no fills, no gradients, no filters, no text, two palette tokens (ink `#1A2B3C`,
kiln orange `#C75B39`). v0.4-compliant, checked by parsing the file rather than by reading the source.

**The object is the regulator's own measuring edge, drawn once, in three spans.** The left span is
graduated and in use. **The middle span is drawn as a continuous line carrying no graduations at all** —
the eight years in which the best-graded schools were not routinely inspected, which is a span of time
that went on being reported about while nothing in it was being measured. A dashed bracket beneath marks
it as a span and not as a gap in the drawing. The right span resumes **at twice the pitch**, because the
regulator went back in and inspected a great many of them in one year, and then the edge **stops, capped**.

**The second edge is a different instrument and the composition refuses to join them.** It is turned a few
degrees out of true, its **six** graduations hang *below* its line rather than standing above it, and
**two** further strokes sit apart from the six. Nothing connects it to the first edge and the gap between
them is empty — the regulator has said in writing that the new grades cannot be compared to the old ones.
Six because the renewed framework grades six core evaluation areas; two apart because safeguarding is
reported separately as met or not met.

**The one warm mark** is a single graduation that has come away from the first edge at the point where
measurement resumed, lying below the line and slightly adrift. One mark, no magnitude.

**The sparseness is the subject and is not an unfinished drawing.** Both Bahrain and the 07-28 England
still are dense; this one is not, because the thing it is about is a span in which nothing was read.

**Looked at, not merely rendered** (2026-08-18 clause 4). The first render was inspected and rejected: the
composition sat in the lower-left quadrant, the second edge was pushed almost off the right margin and read
as a detached scribble rather than as an instrument, and the orange mark had landed on the bracket's own
terminal upright, where it read as part of the bracket. Baseline raised, second edge brought in and lifted,
the mark moved clear. The second render was inspected and accepted.

## og card

`design-assets/og/2026-11-12-england-ofsted-exempt-cohort.png` — 1200×600 PNG, 7,800 bytes, rasterised
from the still at 144 dpi with `sharp`, never drawn twice (2026-08-18 clause 3). Raster, not SVG, because
no major social consumer renders SVG.

## WHERE THE TWO ASSETS LIVE, AND WHY NOT IN `web/public/`

**They are staged at `design-assets/`, and cell 8 copies them into `web/public/stills/` and
`web/public/og/` in the same commit as the flip** (the 2026-06-14 rule — an article's assets ship in the
same commit as its text).

This is not tidiness. **`heldAssets.mjs` withholds a held piece's assets from `dist` by reading the held
slugs out of the content collection**, and this piece has no file in `web/src/content/` at all yet — it is
at cell 7 of eight, not held, *absent*. An asset dropped into `web/public/og/` today would therefore be
copied into `dist` whole and served at `/madar/og/2026-11-12-england-ofsted-exempt-cohort.png` while
`/madar/articles/2026-11-12-england-ofsted-exempt-cohort/` returns 404 — **the exact 2026-09-09 defect
`heldAssets` was built to close**, and the still carries its own `<title>` in readable text, so the
unshipped piece's subject would be served at a guessable URL.

**Measured rather than assumed, this morning:** a card for this slug was copied into a scratch `dist` and
`qa_held_assets` was run against it. It **exited 0 and printed CLEAN** — *0 held slugs, 45 approved slugs,
90 control assets checked.* Both of its limbs enumerate a set that cannot contain this file: limb 1 reads
**held** slugs and limb 2 reads **approved** ones, and a piece mid-gate is neither. Raised as standing-queue
item **140**.
