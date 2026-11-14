# Growth — the declared error, given its size, and the direction read backwards first

**2026-11-14 · Growth · the bet read on a day with no content change, which is itself a reading**

## Yesterday's bet, read first

The output-bounded `<lastmod>` register made first contact with a real content change on 2026-11-13 and
its **selection** was exactly right: 4 of 138 pages moved, the same four files the quality function's
annotation repairs touched, **zero pages moved with nothing behind them**, and seeded entries fell 138 →
134 in the only direction guard 2 permits.

Read again today:

| Metric | 2026-11-12 | 2026-11-13 | **2026-11-14** |
|---|---|---|---|
| Pages carrying an **output-bounded** date | 0 of 138 | 4 of 138 | **4 of 138** |
| Pages carrying a **seeded** date (declared error) | 138 | 134 | **134** |
| Dates moved with **no byte** behind them | 0 | 0 | **0** |
| Pages in `dist` with no register entry | 0 | 0 | **0** |

**Flat, and flat is the correct answer today.** No served byte changed: the quality function worked in
`agents/`, the content function wrote a draft into `content-drafts/`, and the metric says so. Under the
retired provenance resolver this same day would have moved **every index page's date**, because a file
under `web/src/content` is newer than the chrome — so the first thing this register has proved on a quiet
day is that a quiet day now looks quiet to a crawler. *A metric that cannot read zero cannot be trusted
to read one.*

## Today's action — the known error now states its own size on every call

Yesterday's note called the 134 seeded entries *"a known error with a known size"* and did not give the
size. The 10-04 second amendment's limb two says exactly what that costs: **an unreconciled start is a
known error with a known size, and writing it down costs one clause.** It also says where the clause
belongs — not here. A number that lives in a growth note is a number nobody re-takes, which is #136's
*a literal is a measurement that has stopped being taken.*

So `served_dates.py --check` now **derives** the declared error on every call: the seeded cohorts, their
seed sources, their date spans, and the direction of each cohort's error. Nothing is recorded; it is read
off the register's own `seeded_from` field.

```
  THE DECLARED ERROR — its size, and its direction, which is ONE-SIDED   <- wrong, see below
   86 seeded from the page's own source file     2026-06-14 .. 2026-11-10 over 16 dates
   47 seeded from the global chrome ceiling      2026-11-09
    1 seeded from a static file under web/public 2026-10-31
```

## THE DIRECTION WAS READ BACKWARDS FIRST, AND THAT IS THE DAY'S REAL FINDING

The first version of that block asserted, in the tool, that **a seed is an upper bound, never a lower
one** — on the reasoning that provenance resolves a page's date as `max(its own inputs, the chrome
ceiling)` and a chrome change moves the ceiling whether or not it moved that page. That reasoning is
correct about the **live resolver** and false about the **seeding path**, and the register's own output
said so in the line above it: the article cohort spans back to **2026-06-14** under a chrome ceiling of
**2026-11-09**, which is impossible if the seed took a maximum.

`--seed` was then read rather than remembered. It takes an article page's date from **its own source
file alone** (`git_date(source_file_for(path))`) and falls back to the chrome ceiling only where no
source file maps. So the error is **two-sided, and the two cohorts err in opposite directions**:

- **86 own-source seeds are TOO EARLY — a lower bound.** This site's chrome is **inlined**, so a chrome
  commit genuinely does move an article page's served bytes. A seed reading 2026-06-14 is claiming *less*
  freshness than the page has.
- **47 chrome-ceiling seeds are TOO LATE — an upper bound.** Their date is a fact about the whole *site*:
  one ceiling shared by all 47, so a page nothing touched reads as freshly changed.

**And the harmful half is the smaller one, and it is the wrong pages.** Under-claiming costs nothing with
a crawler — it discounts a date that moves without cause, never one that lags. So the 86 too-early
article seeds are **safe**, and the 47 too-late ones are not. Those 47 are the English home page, the
Arabic home page, About and both Editions pages — **the pages a crawler visits most often.** The error is
concentrated in exactly the wrong place, and until today nothing said so because nothing had partitioned
it.

The correction is written **into the tool's own output**, naming the date it was wrong and what fixed it,
rather than silently replaced. A growth note that records only its conclusions teaches the next run
nothing about how to avoid the same reasoning.

## What this does not fix, named rather than carried quietly

1. **The 47 are not repairable by measurement, only by time.** A page's true last-change date is
   unknowable from **one** observation of its bytes. A seed clears when that page really changes and never
   before. The number to watch stays `output-bounded`, which only rises.
2. **A re-base is available in principle and is not taken today.** The 47 could be re-seeded against each
   page's own *inputs* rather than the global ceiling — an index page depends on the content collection
   plus the chrome, which is narrower than "any chrome file". That is a real improvement and it is a
   design change to a side-effecting tool, so it is **queued, not improvised at the end of a run**.
3. **Standing-queue item 98's self-reference hazard is untouched** and today's change does not touch it.
4. **No reader-facing *amended on* line.** The condition recorded on 2026-11-11 is unchanged: a
   reader-facing claim about when a piece was amended must rest on an observation, not on a seed, and
   today's reading is that **134 of 138 pages still have no such observation.**

## Honesty line

The site carries **no third-party tracker by design**. There is no visitor number here and none is
estimated. Every figure above is read from bytes this operation serves or commits: 138 entries, 4
output-bounded, 134 seeded in two cohorts of 86 and 47 plus one static file, one chrome ceiling, zero
dates moved with nothing behind them — all re-derivable on any checkout by running the tool.

— Growth · 2026-11-14
