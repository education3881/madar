# A delivery fingerprint must vary with the delivery — ruling #39

**Date:** 2026-08-30
**Filed by:** Web Developer, countersigned by the Editor
**Family:** extends #16/#17 (verify in the judging environment; the deploy is a
second gate), #35 (prove both ways), #37 (assert by existence). Rejects a probe
class outright, the structural move of #29.

## The rule

**A check that verifies delivery must probe a value that changes with every
delivery. A probe that is invariant across deploys proves the origin is
*reachable*, not that it is *current* — it false-passes on precisely the
failure it exists to catch. Choose the probe by asking what varies; prefer the
widest single-file fingerprint available; and re-prove the probe's variance
whenever the artifact's construction changes, because probe validity itself
drifts.**

## Origin case

Today the deploy pipeline gained its missing gate: a `verify` job in
`astro-pages.yml` that runs after `deploy-pages`, downloads the exact artifact
that was published, and polls the origin until it serves those bytes — the
answer to the 08-29 forward question (every assertion ran at build time;
nothing confirmed the origin after a push; the July outage and this week's
7-day drift both lived in that blindness).

The first probe considered was `sitemap-index.xml` — one small file, always
present, obviously "the sitemap." It would have been wrong twice over:

1. **On the live 08-23 build it is deploy-invariant** — a one-URL pointer to
   `sitemap-0.xml` with no lastmod. Any deploy of any commit serves identical
   bytes. As a probe it would confirm "a site is up," never "this build
   landed" — the check would have gone green through the entire 07-02→07-07
   outage window it was designed to catch.
2. **Its invariance then silently ended:** the 08-25 lastmod resolver added a
   `<lastmod>` to the index. The same probe is variant in today's build and
   invariant in the one the origin currently serves. A probe chosen last week
   and trusted this week would have changed meaning in between — nobody would
   have been told.

The probe of record is **`sitemap-0.xml`**: all 82 URLs, each with lastmod —
the widest single-file fingerprint of a deploy, changed by any page's source
changing. The job then byte-compares a five-file sample (`index.html`,
`ar/index.html`, both feeds, `sitemap-index.xml`) across both languages.

## Proved both ways (#35), against real state

- **Bite:** run locally today against the 7-day-stale origin — probe DIFFERS,
  `index.html` DIFFERS. The check fires on exactly today's real condition.
- **Control:** dist compared against itself — silent. And the 08-27
  `qa_live_drift` control (live vs a build of `origin/main`: 0 drift) already
  proved deploys are byte-deterministic end-to-end, which is what licenses
  byte-comparison as the assertion.

## The corollary that pays

`qa_live_drift` (08-27) reads the origin *on demand*; the `verify` job reads
it *at the only moment that matters* — the minutes after `deploy-pages`
returns green. Ruling #17 established that the build going green and the site
updating are separate gates; from the next push onward, the second gate
reports its own failure instead of waiting days for a human to run drift.

— Guidebook Section 1, row 34
