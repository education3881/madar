# Growth — the front door had no route to the archive, and it was the only page that didn't

**2026-11-22 · Growth, for the Manager · one action, measured on our own served bytes**

## What was wrong

`/browse/` is the archive. In its own words: *"Every published piece, grouped. Editions are chronological;
this is the same corpus read by region, by topic and by country."* It carries the whole corpus —
**46 pieces, 7 regions, 8 topics, 42 countries** — and the Arabic side says the same thing in its own
words, *"الأرشيف كاملًا، مُجمَّعًا."*

**Both home pages — the publication's two front doors — were the only served pages with no link to it.**

Measured, not assumed: `href="…/browse/"` appeared in **140 of the 143** served documents. The three
without it were `valence/index.html` (a standalone instrument, out of scope) and **`index.html` and
`ar/index.html`**. The cause is structural rather than an oversight anyone could have spotted by reading
the nav: `SiteHeader.astro` carries the browse link and **both homes use their own `masthead` instead of
`SiteHeader`**, so the one page-level component that holds that edge is the one component the homes do not
use. `SiteHeader`'s own comment says the link *"is the ONLY inbound edge"* into the hub — correct, and
therefore absent from both front doors for the 69 days since the hub shipped on 2026-09-14.

## Why it matters more now than it did on 2026-09-14

The home's only route into the corpus beyond the six pieces it features was **`Browse all editions →`**,
seven times over, pointing at `/editions/`. On 2026-09-14 "all editions" and "all pieces" were the same
set. **They are not any more.** Since 2026-11-08 pieces ship as singles against a standing ledger and
belong to no edition (issue #13's applied default), so *all editions* is now a **smaller set than all
pieces, and shrinking as a share**: the two newest pieces — `2026-10-23-bahrain-bqa-five-cycles` and
`2026-11-12-england-ofsted-exempt-cohort` — are in no edition at all, and they reach a reader through the
`/editions/` page only via its standing block, which is standing-queue item 92's two-populations-under-one-
heading problem.

**And yesterday made the lost reader real rather than hypothetical.** Every share of the England piece
followed between 13:14Z on 2026-11-21 and this run's deploy landed on our 404 page, because the run that
shipped the piece died before the deploy was dispatched (item 77). The 404 is well built and offers both
front doors — and both front doors offered a chronology of five closed editions as the way to find
everything we publish.

## The action

Two links where there was one, in the previous-editions strip on both homes, with the second pointing at
the archive:

- English — **`Every published piece →`** → `/browse/`
- Arabic — **«الأرشيف كاملًا ←»** → `/ar/browse/`, in the archive page's own vocabulary rather than a
  fresh phrase.

Both are inside a wrapping flex row, and the labels are kept short **on purpose**: this strip is a flex
container and the served corpus measures zero real overflowing boxes, which is a property worth not
breaking in the same run that spent its quality function repairing seventeen artefacts for exactly that.

## Measured before and after, from `web/dist`

| | before | after |
|---|---|---|
| served documents carrying a route to a browse hub | **140 of 143** | **142 of 143** |
| of those, the two homes | **0 of 2** | **2 of 2** |
| routes into the corpus from the English home | 1 (`/editions/`) | 2 (`/editions/`, `/browse/`) |
| routes into the corpus from the Arabic home | 1 (`/ar/editions/`) | 2 (`/ar/editions/`, `/ar/browse/`) |
| served pages overflowing at 1280px | 2 of 143 | **2 of 143** (both the oracle, item 143) |
| served pages overflowing at 390px | 1 of 143 | **1 of 143** (valence's zero-width div, #93) |
| build | — | exit 0, 28 `postbuild` assertions and 12 build-job gates green |

The only remaining page without the route is `valence/index.html`, which is a standalone instrument with
its own three links back into Madār and is deliberately not a publication page.

## The rail graph, measured while here and NOT a defect

A route into the corpus is worth nothing if the corpus is a set of dead ends, so the `related:` graph was
counted over all 46 approved pieces: **180 edges, zero dangling, out-degree 2 to 6 (median 3), in-degree 1
to 8, and no piece with an out-degree or an in-degree of zero.** Every published piece can be left and
every published piece can be reached. **Printed and not asserted**, because it is clean and a floor at
today's reality on a graph that the rail step (standing ledger, 2026-11-12) rewrites on every ship would
red a build for an editorial judgment.

**One pressure worth naming before it bites:** **10 of the 46 pieces are at the proven maximum of six
rails.** The rail step now requires a forward edge into every piece a new single follows up, and the cap
already displaced an edge on 2026-11-21. The out-degree ceiling is fixed and the corpus is not, so each
new single increasingly *displaces* an older edge rather than adding one — the graph's edge count will
flatten while the piece count grows. That is a growth question with a date on it rather than a defect
today, and it goes to the queue rather than into this note's conclusions.

## Return, not reach

No traffic figure appears above and none is estimated. **The site carries no third-party tracker, no
analytics and no third-party request by design**, so this operation cannot say how many readers met the
old front door. What it can say is what the front door offered them, counted from the bytes we serve: one
route, into a set that no longer contains our newest work.

— Growth, 2026-11-22
