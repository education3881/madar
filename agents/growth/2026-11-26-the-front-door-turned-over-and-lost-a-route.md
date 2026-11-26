# Growth, 2026-11-26 — the front door turned over, and lost a route on the way

**One action, and it was a repair rather than a bet.** The founder directive puts growth at one line if that
is what the day affords. This is three paragraphs because the measurement found something served and wrong.

## What the front door now shows, measured rather than assumed

The depth census was re-run over the built corpus, BFS from both home pages, normalising trailing slashes:

| reading | 2026-11-24 | 2026-11-26 |
|---|---|---|
| article pages | 92 | **96** |
| unreachable | 0 | **0** |
| deeper than two clicks | 0 | **0** |
| **one click from a home page** | 6, **all from a wave that closed eight weeks earlier** | **4 — both of today's pieces, in both languages** |

**That is the one-click slot turning over for the first time in eight weeks**, and it is a direct consequence
of the registry carrying an open edition again: the home page's current-edition block draws from
`status: 'current'`, which was empty from 2026-10-13 until this morning. The slots are fewer and newer. Four
is the right number while the open edition holds two pieces, and it will grow with the edition rather than
with the calendar.

## The defect the measurement found, fixed in this commit

`/map/` and `/ar/map/` shipped this morning as yesterday's growth action. **The two home pages were the only
two pages in the publication that did not link it** — 77 other pages do, and it is in the sitemap, so it was
never an orphan; it was simply absent from the one page a new reader lands on. The cause is on record in the
template's own comment: the home pages draw their own masthead instead of `SiteHeader.astro`, **which is the
same reason they were the only two pages without `/browse/`**, fixed in the same strip earlier this month.
*A chrome route added to a shared header reaches every page that uses the shared header, and the front door
is not one of them.* Added to both, reusing `.prev-editions__browse` so the selector register does not move.
Build exit 0 and both links verified in `dist`.

**This is the third member of a family worth naming before it recurs a fourth time**: the footer RSS 404
(2026-08-16, 83 days), `/browse/` missing from the home pages (this month), and now `/map/` on the day it
shipped. The gap closes when the home pages stop having a second navigation, and that is a Web Developer
question rather than a growth one.

## Traffic

**The site carries no third-party tracker by design, so there is no visitor number to report and none is
estimated.** What this function can read without anyone's permission is the site graph, which is what is
measured above. Return rate switches on when a distribution channel does (issue #11, still open).

— Growth · 2026-11-26
