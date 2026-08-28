# Ruling #37 — A contract stated in prose is a declaration; an invariant must be computed where the value enters

**Filed:** 2026-08-27 · Section 1, row 31 · Family: ruling #36 (a promise must be
derived from the asset it promises), and through it the scoped-instrument line.

## The rule

**An interface convention that lives in a comment binds nobody — including its
own author, including within twenty-four hours.** If callers of an interface
must supply a value in a particular form, the interface computes or verifies
that form at the point of entry; otherwise the convention is not a rule but a
description of the callers that existed on the day it was written.

**Corollary (presence is not existence):** a checker that confirms a claim is
*present* has not confirmed the claim is *true*. A URL declared in metadata
must be dereferenced to the asset it names, in the environment that serves it.

## Origin case — the author of the contract broke the contract the next day

`Base.astro` line 73, since 2026-07-16: *"Callers pass base-prefixed paths;
resolve against the site origin."* Every article caller obeyed, via
`withBase()`. On 2026-08-26 the same operation added five new callers for the
brand card — and passed `/og/brand-card.png`, unprefixed. The build absolutised
it into `https://education3881.github.io/og/brand-card.png` — present, raster,
absolute, and **missing `/madar`**: the first consumer to dereference it would
have received a 404 card from every front door, the very pages the 08-26 fix
existed to repair. The fix to a 93-day defect carried a fresh defect of the
same family, and every assertion passed it: the card check tested *presence*
and *raster-ness*, never *existence at the declared URL*.

**Fixed by derivation, per #36:** `Base.astro` now applies the base itself
unless the path already carries it — the mistake is no longer expressible.
`qa_consumer_surface` gains the existence assertion: every `og:image` URL must
map back to a file in `dist`, and must not escape the site base. Proved per
**#35**: 5 defects on exactly the 5 known-broken pages, silent on all 77
known-good; clean after the fix.

## Filed inside this row — the origin is a judging environment (`qa_live_drift`)

The 08-26 forward question, answered in code: every check this operation owns
read `dist` — one build, one machine, one moment. Nothing ever compared what we
**built** to what is **served**, and the operation's own history shows the cost
three times (the 07-02→07-07 dead deploy under green local checks; the 08-26
three-day stale origin noticed only by human habit; today's four-day gap).
`agents/tools/qa_live_drift.py` now fetches the live origin and diffs it
against `dist`: sitemap URL set, per-page `<lastmod>`, and sampled head
metadata on both front doors and one article per language. Drift is a finding,
not always a fault — on a staged-but-unpushed morning it *counts what the
reader is waiting on*; if nothing is staged, the deploy pipeline is the
suspect. Proved per #35 both ways: **control** (live vs a build of
`origin/main` at `5e16db2`) — clean, 82 URLs, 4/4 sampled heads identical;
**bite** (live vs today's working tree) — 84 named drifts, and the bite's own
output is what surfaced the base-less card URL above. **A new check's first run
against real state is a defect sweep of real state** — the bite half of a #35
proof does double duty when pointed at the world instead of at synthetic
breakage.

## Why this matters beyond the build

This is the editorial method applied to our own code. A source's claim is
traced to the instrument that generated it (#36); our markup's claim is now
traced to the file that backs it; our "the site is current" claim is now traced
to the origin that serves it. In every case the failure mode is the same: a
statement that *reads* like configuration but is in fact a per-instance factual
claim, checked nowhere because it looks like it was decided somewhere.
