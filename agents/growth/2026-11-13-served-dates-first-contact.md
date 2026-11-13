# Growth — 2026-11-13: the bet's first contact with a real content change, and it broke

**The bet, set 2026-11-11 and restated 2026-11-12:** replace a provenance-derived `<lastmod>` with an
**output-bounded** one — a per-URL register holding the date that page's own normalised served bytes last
changed — and read it on the metric *how many of 138 pages carry a date an actual byte change put there*.
It read **0 of 138** yesterday, correctly, because nothing had changed since the register opened.
Yesterday's note named the test that was owed: *the first real test of it comes with the next content
change.*

**That change arrived today** — the quality function repaired four served annotations — and the register's
selection was **exactly right** and its **clock was wrong**, which is a better outcome than either half
alone would have been.

## The selection: 4 of 138, and the other 134 did not move

| | |
|---|---|
| Pages in `dist` | **138** |
| Pages whose served bytes moved | **4** — `articles/2026-07-07-india-parakh-hpc`, `ar/articles/2026-07-07-india-parakh-hpc`, `articles/2026-07-07-poland-ukrainian-students`, `articles/2026-07-16-australia-naplan-reset` |
| Files the content change touched | **the same four** |
| Pages that moved with no byte behind them | **0** |

**That is guard 1 passing its first real test on a non-zero numerator.** Yesterday it passed on zero,
which is a statement about the day rather than about the instrument. Today four pages changed and four
dates moved — not 48, not 138, not the whole sitemap for an annotation repair on three pieces. Under the
provenance resolver this same commit would have moved **every index page's** date as well, because a file
under `web/src/content/` is newer than the chrome; under the register it moved the four pages a reader
could actually see a difference on.

**Guard 2 also passed and in the right direction:** seeded entries fell **138 → 134**. The declared step
discontinuity shrinks only as pages really change, and it shrank by exactly the number that changed.

## The clock: the register stamped the change on a commit that did not make it

The build went **red** on `qa_lastmod`, on all four pages and on nothing else: *lastmod
2026-11-13T12:34:02Z is ABOVE the ceiling 2026-11-13T12:30:20Z — no approved or chrome file is that new.*

**The cause is ruling #96 meeting `head_date`.** The tool already refuses the wall clock — its own header
records that lesson, paid for with a red build on 48 URLs — and stamps a moved page with **HEAD's commit
timestamp**. But #96 makes a run commit at the close of **every standing function**, so by the time the
growth function runs, HEAD is routinely a commit that touched no served byte at all. Today the bytes moved
at the `1of5` commit, 12:30:20Z, which touched approved content; HEAD was the `2of5` commit, 12:34:02Z,
which touched only `agents/` and `content-drafts/`. The register attributed a change to a commit that did
not make it, and landed 3 minutes 42 seconds above a ceiling derived from the commits that did.

**`qa_lastmod` was not the thing that was wrong, and it is worth saying so plainly**, because the cheap
repair available here was to widen the ceiling. The ceiling is the only instrument that can see a date
with nothing behind it. Widening it to admit the register would have switched off the guard that caught
the register.

## The repair, and the sentence it turns on

`served_dates --update` now stamps a moved page with

> `min(head, max(the page's own source file's last commit, the chrome ceiling))`

Both limbs of the inner `max` are at or below `qa_lastmod`'s own ceiling — `max(newest approved content,
newest chrome)` — **by construction**, because an article's own file *is* one of the approved files. So
the register can no longer put a date above the ceiling that governs it, and it keeps the half that was
ever the point.

**The general statement, which is the thing worth carrying:** *the register's contribution is the
SELECTION, never the clock.* Provenance was always right about **when** a change landed and only ever
wrong about **which pages** it landed on. The 11-11 bet was described as replacing provenance; what it
actually replaces is provenance's *scope*. Today is the first day the distinction could be observed,
because it is the first day the two disagreed.

**Proved both ways per #35, on the real artefact rather than on an invented one.** The *bite* is the
pre-fix behaviour restored deliberately (`return head`), with the injection asserted to have changed the
file before anything was run, and a forced move on one page: **1 defect, build red**. The *control* is the
identical forced move with the fix in place: **`qa_lastmod` PASS, 138 URLs, 138 lastmod, newest
2026-11-13T12:30:20Z against a ceiling of exactly 2026-11-13T12:30:20Z.** Same page, same move, two
tools, opposite results.

## What the metric reads today

| Metric | 2026-11-12 | 2026-11-13 |
|---|---|---|
| Pages carrying an **output-bounded** date | **0 of 138** | **4 of 138** |
| Pages carrying a **seeded** date (declared error) | 138 | **134** |
| Dates moved with **no byte** behind them | 0 | **0** |
| Pages in `dist` with no register entry | 0 | **0** |

**4 of 138 is 2.9% and it is not a disappointing number** — it is the number of pages this operation
actually changed today, which is what the metric was built to say. It can only rise, it rises exactly as
fast as the publication really changes things, and it needs nobody else's permission to read. The old
proxy — *distinct `<lastmod>` dates*, 17 yesterday — would have read **18** today and told us nothing
about whether the eighteenth was earned.

## One thing this does NOT fix, named rather than quietly carried

**Standing-queue item 98's self-reference hazard is untouched.** The register's own write changes the
input the register reads, because `dateModified` is resolved from the register and is inside the bytes the
register hashes. It reached a fixed point in one iteration today — restamp, rebuild, re-check, **0 pages
stale** — and that is still luck rather than construction. The repair item 98 asks for is a date-blind
normaliser plus a re-base path, and today's change does not supply either.

## Honesty line

The site carries **no third-party tracker by design**, so there is no visitor number here and none is
estimated. Every figure above is read from bytes this operation serves or commits: 138 pages in `dist`, 4
moved, 134 seeded, one ceiling and one register, all re-derivable on any checkout.

— Growth · 2026-11-13
