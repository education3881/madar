# Ruling #89 — An invariant needs one place that holds both its sides; across deploys, that place is the artefact

**Filed:** 2026-10-06, at the point of filing, by the daily run's QA lane.
**Family:** assertion discipline — **twenty-seventh member**, and the first whose
subject is not what a check *reads* but **when both of its operands exist at once.**
**Lane:** standing-queue item 2, raised 2026-09-06, named twelve times across five
weeks, done zero times. Reached the head today by the one-queue rule's displacement
clause and its 10-05 tiebreak (*among items past the three-displacement threshold, the
oldest goes first*), at 29 days — the oldest item the board has ever carried.

---

## The rule

> **A claim that relates two quantities can only be checked where one place holds
> both.** If the two live in different kinds of evidence, the claim is not merely
> unchecked — it is **unfalsifiable**, and it will read as settled for as long as
> nobody notices which side is missing.
>
> **Corollary, and it is the operative half.** When one of the quantities is *the
> previous state of the thing itself*, no single run can hold both, because a run only
> ever sees now. Something must be carried across. **The only state an operation has
> across deploys is what it published** — so the artefact must carry its own
> fingerprint forward, or the invariant stays unfalsifiable no matter how many checks
> are added.

## What was unfalsifiable, and for how long

`<lastmod>` is a claim relating two quantities: **a date** and **a change in the served
bytes of a page**. `sitemapLastmod.mjs` derives the date from **git history** over
`CONTENT_DIRS` and `CHROME_GLOBS`. The served bytes live in `dist`, and the *previous*
served bytes live only at the origin — until the next deploy overwrites them.

So the two sides of the claim have never once been in the same place:

| | where it lives | who can see it |
|---|---|---|
| the date | git history | every build |
| this deploy's bytes | `dist` | every build |
| **the previous deploy's bytes** | **the origin, until overwritten** | **nobody** |

Every instrument the operation owns reads one of the first two rows. `qa_lastmod`
(2026-09-08) bounds the date from **above** — no `<lastmod>` newer than its own per-URL
ceiling — which is the *leak* direction, and it is a good check: it closed two real
production defects (`9886987` on 08-30, `642fef2` on 09-02, both held drafts dating live
pages). But a ceiling is a one-sided bound by construction. **Nothing has ever bounded
the other side**, and the other side is the one a crawler acts on: *a page whose
rendered content changed and whose date says it did not.*

The `verify` job cannot see it either, and the reason is worth stating precisely because
the obvious reading is wrong. Verify downloads the exact artifact `deploy-pages`
published and byte-compares it against the origin. By the time it runs, **origin ==
artifact by construction.** It is a strong check of *did my deploy land* and it is
structurally incapable of answering *what changed since the last one*. A check wired
there would have passed forever — which is standing-queue item 1's entire subject,
arrived at from the opposite direction.

## The hole is not hypothetical. Measured, not argued.

Two probes on the real tree today, each confirmed to have changed the artefact before
the measurement was believed (#74), each reverted in the same run.

**Probe 1 — `web/src/styles/global.css`, one character (`max-width: 100%` → `99%`).**

```
served bytes changed on   120 of 121 HTML pages
<lastmod> values moved:     0
```

Astro serves the stylesheet as a **content-hashed filename**
(`/madar/_astro/style.DBd_Pbzi.css`), so the hash is printed into the head of every page
that links it. `web/src/styles` is excluded from `CHROME_GLOBS` **on purpose**, with a
written reason — *presentation is excluded, rendered content is included* — and that
reason is defensible for lastmod semantics. Its consequence had never been looked at.

**Probe 2 — `design-assets/wordmark/madar-wordmark.svg`, one `<title>` element.**

```
pages whose RENDERED CONTENT changed:  117 of 120 routed
<lastmod> values moved:                  0
```

This one is not a declared exception. It is an **omission**, and it is worse than the
stylesheet in three ways at once:

1. Three separate build-time readers inline that file into the page —
   `SiteHeader.astro`, `pages/index.astro` and `pages/ar/index.astro`, each via
   `readFileSync`. The SVG markup lands in the served HTML as content, not as a
   reference.
2. `design-assets/` is in **neither** `CHROME_GLOBS` **nor** `CONTENT_DIRS`.
3. It is not even in the resolver's git query, which asks only for `:/web/src` and
   `:/web/public`. The directory is invisible to the resolver *in principle*, not merely
   unmatched by a glob.

So the Designer's own working file — a file whose entire purpose is to change what every
page looks like — changes what 117 served pages **say** while telling every crawler that
nothing anywhere has changed. That is the defect the queue item described on 2026-09-06,
sitting in the tree the whole time, reachable by one edit, and invisible to twenty-eight
standing assertions.

## What makes it checkable: two hashes, not one

`qa_served_manifest.py` (standing assertion 29) emits a per-URL fingerprint into `dist`,
which the next build fetches back **from the origin**. The published artefact becomes the
memory. There is nowhere else to keep it that is not provenance again.

The design turns on recording **two** hashes per page rather than one:

- `bytes_sha` — the served bytes exactly as a reader receives them.
- `content_sha` — the same bytes with the build's own content-hashed asset filenames
  collapsed (`/_astro/style.CTkyS1Kw.css` → `/_astro/style.__.css`).

Measured on probe 1: **raw 120 differ, normalised 0 differ.** A presentation-only change
is therefore *mechanically* separable from a rendered-content change — which is what
makes the whole thing an assertion instead of an alarm. Three states that were
indistinguishable yesterday because all three were invisible:

| | what happened | disposition |
|---|---|---|
| 1 | `content_sha` moved, date did not | **FAIL.** The page changed what it says and kept its date. No declared exception exists. |
| 2 | `bytes_sha` moved, `content_sha` did not, date did not | **Reported, counted.** The resolver's own declared exclusion. The tool asserts the resolver's stated intent; it does not overrule it. |
| 3 | date moved, `content_sha` did not | **Reported, counted.** The 09-04 shape, ruled a design question and not a defect. |

Case 3 is the one worth dwelling on, because it is the reason the queue item was *named*
twelve times and *done* zero. The 09-04 deploy moved all 119 dates for a change that
altered the served output of one page. Every run since has been able to describe that
shape in prose and not one has been able to put a number on it. **A design question with
no measurement attached does not get decided; it gets restated.** It is now printed, with
a count, on every run.

## Why the normalisation is narrow, and why that needed a guard

The collapse matches only `/_astro/<name>.<hash>.(css|js)`. A wider normaliser would be
easier to write and would hide real changes — the 09-14 trap on the input side, where an
assertion scoped wider than the thing it checks finds the right string for the wrong
reason.

And a normaliser that silently matches **nothing** is strictly worse than no normaliser,
because `content_sha` would equal `bytes_sha` everywhere, case 2 would collapse into case
1, and the tool would fail on every stylesheet edit while *looking* like it was working.
So the emit half refuses to produce a manifest (exit 2) if `dist/_astro` carries hashed
stylesheets and zero substitutions were applied. Proved by stripping the hashes out of a
copy of `dist` and watching it refuse.

## The seed cannot come from a build

The first baseline is taken with `--seed-from-origin`: every sitemap URL fetched from the
origin and hashed from the **bytes the origin actually serves**, under a total wall-clock
ceiling per #88. Seeding from a local build would be the 09-14 masking trap raised to the
level of the whole instrument — an oracle calibrated against the thing it exists to
judge. The seed also produced a measurement worth keeping on its own: **the origin serves
byte-for-byte what we build across all 120 pages**, where `qa_live_drift` samples four
heads.

## What this still cannot do, written down so it does not read as covered

The manifest is generated by the same build whose output it describes. If a build is
wrong, the manifest is wrong consistently and the comparison passes. **It compares across
deploys and can never validate a single build in isolation.** That is not a gap to be
closed later; it is the shape of the instrument, and the reason the seed is
origin-derived.

## A known future bite, with a date

`SiteFooter.astro` computes `new Date().getFullYear()` at build time. On **2027-01-01**
the first deploy will change the served bytes of every page with no commit touching any
source file and no date moving anywhere — case 1, on the whole corpus, from the calendar
rather than from anyone's edit. It is recorded in the tool's header so that when it fires
it is recognised as predicted rather than diagnosed from scratch. *(Named as item (e) in
the 09-27 QA log, where it appeared once and was never mentioned again — which is the
one-queue rule's measurement, not a coincidence.)*

## Where it is wired, and the half that is not

`--emit` is gated from `web/package.json`'s `postbuild`, because a gap in the chain
leaves the next build with no baseline, and `qa_census` asserts its routed-page count
against the sitemap's own `<loc>` set — so a manifest that quietly stops describing some
pages fails the build instead of narrowing in silence.

`--check` has **no gated home this identity can write.** Its correct home is the `build`
job after `npm run build`, while the origin still serves the previous deploy; the reason
is in the tool's header and the one-line step is staged at
`agents/patches/2026-10-06-build-served-manifest-check.md`. Until that lands the check is
hand-run every day and its three counts recorded in the QA log — **which is the 09-13
defect by name**, carried deliberately, with a staged patch instead of a promise.

## Proved both ways, bite first (#35, #74)

| # | What | Result |
|---|---|---|
| 1 | CONTROL — clean build vs origin-derived baseline | CLEAN, exit 0 · 120/120 byte-identical to the origin |
| 2 | BITE — wordmark `<title>`, a real source file | **117 silent content changes, exit 1** |
| 3 | CONTROL restored by reverting the wordmark | CLEAN, exit 0 — proves the bite was the cause, not drift |
| 4 | REPORT — stylesheet value, a real source file | 119 presentation-only, **0 silent**, exit 0 |
| 5 | REPORT — baseline dates moved back, content untouched | 120 unbacked dates, **0 silent**, exit 0 |
| 6 | GUARD — origin serves no manifest (today's real state) | exit **3**, its own code, never a pass |
| 7 | GUARD — a sitemap URL with no built file | exit 2, the join is asserted and not assumed |
| 8 | GUARD — asset hashes stripped so the normaliser matches nothing | exit 2, refuses to emit |

## The general form, which outlives sitemaps

Ask of any invariant: **where does each side of it live, and is there a single place that
sees both?** If the answer is no, the check that appears to cover it covers one side and
infers the other — and an inference is exactly what a ceiling is.

The variant that cost this operation five weeks is the temporal one. When one side of an
invariant is *the previous state of the thing itself*, no amount of checking inside one
run will ever reach it, because **a run cannot observe its own past.** The fix is never a
better check; it is **state deliberately carried forward**, in the only vessel that
survives the gap. Here that vessel is the published artefact — which also means the
instrument's memory is, correctly, a served byte, and therefore the Web Developer's even
though an assertion found it.

Kin: **#85** (a tool exempted for the cost of its action is not exempted for the cost of
its input — an exemption inherited by the wrong half), **#58** (the publication is not a
function of its sources), **#57** (count against the population, never against yesterday's
number — the same refusal to let a derived value stand in for a measured one), and the
RUNBOOK's enumeration family, whose standing question *what can this check not
structurally see?* this answers with **a second point in time**.
