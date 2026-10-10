# Ruling #93 — a conclusion travels no further than what carries it

**Filed:** 2026-10-10, by the daily run, as its first work, before the content lane.
**Lane:** QA / Assertions Engineer. **Closes:** standing-queue **item 1**, raised
2026-10-04 as the daily's forward question, displaced from the head four times, 6 days.
**Instrument:** `qa_bridge_coverage.py`, standing assertion **32**, 29 of 32 gating.
**Family:** assertion-discipline (TWENTY-NINE → THIRTY).

---

## The item asked the wrong question, and the measurement is what says so

Item 1, in its own words: *of the 28 that gate the deploy, which are wired somewhere
that cannot observe the thing they assert?* It named two suspects — `qa_feed_enclosures`
and `qa_feed_direction`, *"suspect by their own names"* — and it carried the sharpest
sentence on the board: **a check in the wrong home passes forever.**

Enumerated today, tool by tool, home by home: **none of them.** All 29 gating assertions
read `web/dist` or the repository root. Both exist in the `build` job, which is where all
29 run — twelve wired in `astro-pages.yml`, seventeen from `postbuild`. Not one is blind
to its own subject. The two suspects are innocent: both read built files, and built files
are what they are about.

**The wrong home is real. It does not belong to an assertion.** It belongs to the step
that promotes an assertion's conclusion from the artefact to the publication.

## What that step actually is, measured

Every one of the 29 concludes something about `dist`. No reader is served `dist`. The
only thing in this operation that carries a conclusion from `dist` to the origin is the
`verify` job's byte-compare, and it compares **six files**: the `sitemap-0.xml` probe,
then `index.html`, `ar/index.html`, `rss.xml`, `ar/rss.xml`, `sitemap-index.xml`. The
workflow's own comment says so plainly — *"byte-compares a five-file sample"* — and has
said so since the job was written. Nobody had put it beside the other number.

The other number: the origin serves **120 pages and 137 assets**.

> **6 of 257 = 2.3%.** Of the 137 assets, the four confirmed are both feeds and both
> sitemaps, so everything a **page loads** is confirmed **zero** times: 46 stills, 40
> share cards, **34 woff2 fonts**, two stylesheets, one script.

Twenty-nine assertions, every one of them correct, are promoted to statements about the
publication across a bridge covering one fortieth of it. That is not a defect in any
assertion. It is a defect in the **inference**, and the inference is the thing no
instrument in this operation had ever been pointed at.

## The ruling

**An assertion's scope is not where it runs. It is how far its conclusion is allowed to
travel, and something has to carry it that distance.** When a check reads the artefact
and the claim is about the publication, the carrier is part of the assertion — and if
nobody measures the carrier, the strength of 29 checks is whatever the carrier happens
to be, discovered later.

Seventh statement of the enumeration family, and the first aimed past the check itself.
The previous six all asked *what can this check not see?* — the flag-sweep inversion
(08-09), the chrome 404 (08-16), the orphan sweep (08-17), the consumer-format rule
(08-18), the human-artefact rule (08-23), the held-date rule (09-06). This one asks:
**the check saw correctly — what carried its answer to the reader, and how wide is
that?** A green check scoped to what it enumerates is still only a green check *there*.

## Why the ratio is measured and not asserted, which is the honest half

Widening the bridge is an edit to `.github/workflows/**`, and this identity is refused
write access to it (09-14, clause 4). An assertion with a floor above today's measured
reality would red every build until a patch nobody can apply lands — which is
`qa_feed_validators`' position turned into a self-inflicted outage. So assertion 32
**prints** the ratio on every build and **asserts** only what is reachable from here:

1. every bridge member exists in `dist` — a sample naming a file the build stopped
   producing cannot compare it, and the finding belongs in the `build` job rather than
   at the origin `curl` after the deploy;
2. every `.html` member is a page the sitemap claims — the bridge's width is scarce;
3. **the bridge spans both editions and both feeds.** This is the limb that bites. A
   bridge that silently lost its Arabic half would byte-compare the English half and
   pass forever while half the publication — composed, not translated — crossed
   unverified. Proved by dropping `ar/index.html` from the sample: exit 1.

**The remedy is already on disk, already gated, and already published**, which is the
part worth carrying. `qa_served_manifest --emit` writes a fingerprint of every served
page and asset into `dist`, and `served-manifest.json` is live at the origin (200,
67,737 bytes, **256 entries**, confirmed today). A 257-file bridge therefore costs **one
`curl` and one comparison**, not 257. Staged at
`agents/patches/2026-10-10-verify-bridge-via-served-manifest.md`.

## The fonts are why this was urgent rather than merely true

On 2026-10-08 the publication self-hosted its five typefaces: **40 new files**, the
largest single addition to the served surface in its history. **Not one is inside the
bridge.** That run named the exposure itself — *"if it goes wrong the failure is silent,
because the new assertion asserts where we do not point and never what arrives"* — and
this morning one `woff2` was confirmed at the origin as `font/woff2` **by hand**. By
hand is the 2026-09-13 defect: *a green that costs a human's attention is paid for out
of the runs that have least of it.* The queue's own item 1 saved
`qa_served_manifest --check` from the `verify` job by asking its question without
building it; today it was built, and the first thing it measured was yesterday's work.

## Second limb — the tool's own first draft, and why its control could not see the bug

Recorded because it changed the code and because the shape is general.

The first parser credited **every** `for f in` list inside the verify job. That job has
two. The second is the feed-cache step, which `curl -I`s both feeds for an `ETag` and
**byte-compares nothing** — so two files were counted as byte-confirmed on the strength
of a step that confirms no bytes. **That overcounts the bridge, which is the false-pass
direction.**

It survived the control, and the reason is the finding: **on the real tree both parsers
print 6**, because the two lists overlap exactly on the two feeds. The right number for
the wrong reason. It was caught only because bite 2 was written to drop `ar/rss.xml`
from the comparing loop *while the other loop still named it* — a bite aimed at any file
named once would have passed and left the bug in.

> **A control that returns the expected number cannot distinguish a correct derivation
> from an incorrect one. Only a bite aimed inside the overlap can.**

That is #57 — *equal cardinalities are not an agreement* — moved from two instruments
onto one instrument's own parse, and it is 2026-09-14's input-side question (*where does
the string I am looking for also legitimately appear?*) with the answer being *in the
same file, under a step that means something else*.

## Proved both ways, bite first (#74), on copies in /tmp

**13 of 13.** Five bites: the lopsided bridge (Arabic page dropped), the Arabic feed
dropped from the comparing loop only, a sample member the build does not produce, an
`.html` member absent from the sitemap (`404.html`, a real candidate — it is served and
deliberately unlisted), and the probe itself drifting to `sitemap-7.xml`. Two control
negatives: a `cmp` injected into the **build** job must not widen the bridge, and the
untouched workflow must read CLEAN. Five failure-to-check guards: no workflow, no
`dist`, a verify job whose comparisons are all disabled, the verify job deleted
outright, and a `dist` with no sitemap — all exit 3, because **a bridge that cannot be
found is not a bridge of width zero** (#16's silent-pass trap). Every injection is
checked for having changed the file before the assertion is judged on it (09-14), and
every expected value is derived from the tree rather than hardcoded, because the 10-07
harness went stale inside an hour on its own constant.

## What this leaves open, stated rather than closed

Open items **7** and **8** are this same triangle from the other two corners: item 7 is
*the published oracle has no auditor* (the origin's manifest against the origin's own
pages), item 8 is *`--check` has no honest home before the commit*. Item 1 was the third
corner — **the carrier** — and it is now measured and partly asserted. The three want one
answer, and the 2026-10-11 review is the place to say whether they are one item.
