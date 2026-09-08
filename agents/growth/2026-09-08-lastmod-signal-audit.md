# Growth — the lastmod signal audit: leak-free is not the same as informative

**Date:** 2026-09-08 · **Owner:** Growth, with the Web Developer
**Follows:** today's held-date leak fix (assertion #11, `qa_lastmod`) and the 2026-09-06
review's carried item (d), which asked for an output-bounded lastmod design.

---

## The finding, measured

Today's fix stopped held drafts from dating live pages. With it in, I read what a crawler
actually receives from the built sitemap:

| | |
|---|---|
| URLs carrying a `<lastmod>` | **82 of 82** |
| **Distinct dates across all 82** | **2** |
| `2026-09-04` | **81 URLs — 99%** |
| `2026-08-18` | 1 URL (VALENCE, a `public/` file with its own life) |

**Eighty-one of eighty-two pages tell a crawler they changed on the same day.**

If each article instead carried the date it was itself last touched, the same corpus would
show **9 distinct dates across 76 articles** — a real publication history, clustered where
the work actually happened (22 articles on 07-07, 16 on 08-08, 6 on 07-06).

## Why this matters, in the resolver's own words

`sitemapLastmod.mjs` rejected build-time stamping on 2026-08-24 with this reasoning:

> every page would claim to change on every deploy… "all 82 pages changed simultaneously,
> again" is the canonical unreliable pattern. We would be spending the signal to say nothing.

We are producing that pattern anyway — not from build time, but from the chrome rule. Any
edit under `src/layouts`, `src/components`, `src/lib` or `src/pages` becomes the floor for
every page, and this operation edits chrome most days. The module head named the failure
and the implementation walked into it by another door.

**And today is the sharpest possible illustration.** This run edited the Zambia pair in
both languages — a real content change. `qa_live_drift` reads **CLEAN** against the origin,
because the pair is held and produces no served bytes. Under the *old* resolver, that same
edit would have moved five live `<lastmod>` values on pages nobody had changed. Under the
new one it moves none. Correct — and it also means the next chrome edit will move all 82
regardless, which is the half we have not fixed.

Note the irony and accept it once, as the review said: today's fix touches `src/lib`, so it
bumps all 82 dates one more time on landing.

## Why this is a Growth item and not only a Quality one

With **0 of 82 URLs indexed** (the standing `site:` observation, most recently 09-04), the
first crawler to arrive is the whole audience. It gets two signals from us: the link graph
(fixed 08-25 for orphans, 09-06 for dead ends) and the change signal. The change signal is
currently one bit — *everything, always* — which is the signal a crawler is documented to
discount. We are not being penalised for lying; we are being ignored for being uninformative.

**No traffic figure is claimed here. None exists: the site carries no third-party tracker
by design.** This is a read of what we emit, not of what anyone received.

## Proposal for the 09-13 review — output-bounded lastmod, using a job we already run

The honest instrument is per-URL **output** change, which only the deploy pipeline can know.
We already have the pipeline: the `verify` job (landed 08-30) downloads the exact artifact
`deploy-pages` published and byte-compares it against the origin. The addition is small:

1. **At build, emit a manifest** — `dist/.hashes.json`, one SHA-256 per routed URL's HTML,
   with the volatile head fields (the lastmod itself) excluded so the hash cannot chase
   its own tail.
2. **At verify, fetch the previous deploy's manifest** from the live origin and diff it.
3. **Carry forward** — a URL whose hash is unchanged keeps its previous lastmod; a URL whose
   hash changed takes this deploy's date. The manifest ships with the site, so the next
   deploy reads it back; no external state.
4. **Fail loud on the cold start** — no previous manifest means "no data", not "everything
   changed"; first run emits the git-derived date exactly as today and says so.

This keeps everything today's fix earned (held files still contribute nothing — a held file
produces no routed URL, so it has no hash) and replaces a *proxy for change* with *change*.
A stylesheet edit stops bumping 82 dates; a genuine chrome edit bumps exactly the pages it
altered; and the assertion landing today needs one line changed, because its ceiling
(max of approved-content and chrome commits) still bounds any honest value from above.

**Cost:** one build step, one verify step, one fetch. **Risk:** a manifest that drifts from
the artifact — which is the failure `verify` already exists to catch, pointed at itself.

## Recommendation

Ship the leak fix now (done). Take the output-bounded design to the **2026-09-13 review** as
a decision, not a discussion — with the measurement above as the argument. Sequence it
**before** the IndexNow switch is turned on: announcing 82 URLs whose dates all say the same
thing spends a fresh channel on the uninformative signal.

— Growth · 2026-09-08
