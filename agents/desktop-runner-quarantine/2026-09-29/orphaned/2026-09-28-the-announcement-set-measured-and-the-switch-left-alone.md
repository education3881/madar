# Growth — the set we would announce, measured exactly; and the switch deliberately left alone

**Filed:** 2026-09-28 · desktop session, workflow-write lane · **Function (c), one concrete action**
**Traffic honesty:** the site carries **no third-party tracker by design.** Nothing below is a
visitor number and none is estimated. Every figure is a measurement of a *surface*, taken today
from outside the origin.

---

## 1. The action: the reader's poll path is now gated, for real this time

The two RSS feeds are the only reader-facing distribution path Madār has that needs no platform,
no account and no permission. Whether a subscriber's poll is cheap or expensive is decided entirely
by cache validators, and the step that protects that path has been a coin flip since the feeds
shipped (#63).

Measured today against the live origin, before touching anything:

| Feed | Connections | Distinct validators | Edges seen | Revalidated 304 |
|---|---|---|---|---|
| `/madar/rss.xml` | 8 | 1 | 5 | **8 / 8** |
| `/madar/ar/rss.xml` | 8 | 1 | 7 | **8 / 8** |

**16 of 16 honoured.** And the honest reading, which cuts the other way: the origin served **one**
validator per feed today, so **the broken step being removed would have passed today too** — by
luck, a third time. The fix landed on a green day on purpose. A check that is right three times in
four is not a check, and waiting for it to go red again to justify repairing it is the same bill the
09-23 deploy already paid.

**What actually changed today is not the measurement — it is that the measurement is now enforced.**
`qa_feed_validators` gates from `verify`. **22 → 23 of 25.** A regression in a subscriber's poll path
now fails the deploy instead of failing quietly at the reader.

**And the correction this note owes its predecessor.** The 2026-09-25 growth note said this fix "was
applied in this session" and that "from the next dispatch, a regression in the reader's poll path
fails the deploy." **That was not true and could not have been.** The edit was applied to a working
tree on a clone nine days behind `origin/main` and never committed, so for three days the gate was
not gating. Ruling #72 carries it. The measurement in that note was sound; the claim about the world
was one level too wide.

## 2. The announcement set, measured exactly — the IndexNow precondition nobody had checked

The IndexNow step reads its URL set from the **served** `sitemap-0.xml`, never from the tree
(#36). So the quality of any future announcement is exactly the quality of that served set, and
until today nobody had counted it against the build it claims to describe.

| | |
|---|---|
| Served `sitemap-0.xml` locs | **120** |
| Built `dist/sitemap-0.xml` locs | **120** |
| Held slugs appearing in the served sitemap | **0 of 6**, checked one by one |
| `robots.txt` | 200, one `Sitemap:` line, resolving to `sitemap-index.xml` |
| Key file `/madar/66ec26c5232c206b2c4714fd916a29a8.txt` | **200** |
| `qa_live_drift` | **CLEAN** — 120 URLs, 0 lastmod drift, 4 sampled heads identical |

The six held pieces — Zambia, Sierra Leone, Sudan, the ruler piece, Egypt and Rwanda — leak into
nothing: not the sitemap, not the feeds, and their twelve stills and cards are withheld at build
(`withheld 12 asset(s) for 6 held piece(s)`).

**So the set we would announce is exactly the set we serve, and the set we serve is exactly the set
we built.** That is the precondition for IndexNow being useful rather than noisy, and it is now a
measured fact rather than an assumption, on the eve of the largest batch of URLs this publication
will ever publish at once.

## 3. The switch stays off — and this note does not reopen it

`INDEXNOW: "off"`. The 09-25 note put the decision to the founder with the trade stated rather than
a recommendation, and recorded the Manager's view: **turn it on after the wave is live and a `verify`
job is green, not before.** Edition 05's wave gate targets **2026-10-11**, thirteen days out.

**That view is unchanged and this run did not act on it**, even though this lane is the only one that
*can* flip it — `INDEXNOW` lives in `astro-pages.yml`, and today this session wrote that file twice.
Being the only identity able to do a thing is not authority to do it. Submitting our URL set to an
external index is an action in the publication's name (#7) and it is the founder's word.

**The honest line on measurement, repeated because it is the one that cuts against acting:** turning
IndexNow on will produce **no number we can read**, now or later. It changes when an index learns a
URL exists; our instruments cannot see an index. Anyone arguing for it argues from mechanism, not
from evidence, and should say so.

## 4. Return rate, not raw counts

Still zero readable return signal, and the reason is the design, not a gap: no tracker, and Substack
has not sent. The first privacy-clean return number this operation will ever have arrives with
Issue 01, and it is read in the weekly review, not invented in a daily.

**Two third-party origins** are requested by the layout (`fonts.googleapis.com`, `fonts.gstatic.com`),
derived from the layout every run since 09-26 so the count cannot drift. That is the whole of our
third-party surface and it is the scope our privacy claim is entitled to.
