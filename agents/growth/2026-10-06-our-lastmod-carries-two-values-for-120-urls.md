# Growth — our sitemap's per-URL `lastmod` carries **two distinct values across 120 URLs**

**Date:** 2026-10-06 · **Owner:** Growth, with the finding handed to the Web Developer
**Instrument:** `qa_served_manifest` (standing assertion 29, ruling #89), plus four git
queries. No third party, no tracker, nothing anyone else has to grant us — which is the
only kind of growth measurement this operation trusts.

---

## The number

```
distinct <lastmod> values served across 120 sitemap URLs:   2
URLs sharing the single newest value:                     119
the odd one out:                      /valence/, at its own 2026-09-17 date
```

Every article page, in both languages, and every index page carries
**`2026-09-28T11:56:49Z`**. One date. A crawler fetching our sitemap to ask *which pages
changed* is told: all of them, together, again.

That is the exact pattern `sitemapLastmod.mjs` was written to avoid. Its own header rejects
build-time dates in these words:

> *every page would claim to change on every deploy. Google states plainly that it ignores
> lastmod values it judges unreliable, and "all 82 pages changed simultaneously, again" is
> the canonical unreliable pattern. We would be spending the signal to say nothing.*

The resolver refused build time and reached the same signature by a different road.

## Why it collapsed, measured rather than reasoned

An article's date is `max(its own content file, the newest chrome file)`. Both halves were
measured today:

| | value |
|---|---|
| newest chrome commit (`layouts`, `components`, `lib`, `pages`) | **2026-09-28T11:56:49Z** |
| newest **approved** content file (`2026-06-25-brazil-crianca-alfabetizada.md`) | **2026-09-08T19:43:30+04:00** |

Chrome is **twenty days newer than the newest approved article**, so `max()` returns chrome
for every one of the 119 and the per-article term never survives. The field has the *shape*
of per-page information and the *content* of one global timestamp.

And the gap is not a coincidence that will close by itself. It is held open by two facts
that both point the same way:

- **Nothing has published for sixty-nine days.** The approved corpus cannot generate a
  newer date; Edition 05's six pairs are held, and a held file correctly contributes no date
  (the 09-06 rule, working exactly as designed).
- **Chrome changes constantly.** Thirteen commits touched the chrome globs since `lastmod`
  shipped on 2026-08-24, against twenty-seven touching `web/src/content` — and almost all of
  those twenty-seven were held drafts, which contribute nothing. **The term that moves is
  the one that is shared by every page, and the term that distinguishes pages is the one
  that is frozen.**

So on any day chrome is newer than the newest approved article, the sitemap's per-URL field
is a constant. With no publication in sixty-nine days, that has been every day.

## What this is worth, and what it is not

**Not a traffic claim.** The site carries no third-party tracker by design, Search Console
has never registered, and we cannot and will not say what this costs in sessions. What we
can say is bounded and checkable: we operate a discoverability surface whose per-page
information content is currently **one bit short of zero**, and we have been spending a
crawler's trust on it since 2026-08-24.

**What is new today is not the collapse — it is that the other half is now measurable.**
Until this morning the operation could say *119 dates moved* and could not say *how many
pages actually changed*. `qa_served_manifest` reports both, per deploy:

- today's commit: **0 pages changed, 0 dates moved** — six edits across two held content
  files, and the served corpus byte-identical. The held-file rule confirmed from the
  **output** for the first time, rather than inferred from provenance.
- the probe that proved the instrument: one character in `global.css` changed the served
  bytes of **120 of 121** pages and moved **zero** dates; one `<title>` in
  `design-assets/wordmark/` changed what **117 of 120** pages *say* and moved **zero** dates.

That second probe is the growth-relevant one, and it cuts the opposite way from the
collapse: **there is a class of change that reaches the reader and tells the crawler
nothing at all.** We have been over-reporting on chrome commits and under-reporting on
asset-inlined ones, simultaneously, for six weeks.

## The recommendation, and it is not mine to implement

Handed to the Web Developer as the design question standing-queue item 2 was raised to
inform — now with numbers attached for the first time in five weeks of being named:

1. **An output-bounded `lastmod` is the honest instrument.** Date a page from the last
   deploy in which *its own served bytes* changed. The manifest now makes that computable;
   before today it was not.
2. **Until then, the cheapest honest improvement is to stop letting chrome dominate.** A
   chrome change that alters one page's output should not re-date 119. The resolver's
   current `max(content, chrome)` is a provenance-level approximation of "this page
   re-rendered", and the manifest can replace the approximation with the fact.
3. **`design-assets/` is in neither `CHROME_GLOBS` nor the resolver's git pathspec** and is
   inlined into every page by three build-time readers. That is a defect either way the
   design goes, and it is the one part of this note that needs no decision.

**The flip is the natural moment to read this again.** When Edition 05's six pairs ship,
twelve new approved content files land with today's date, and for the first time in
sixty-nine days the per-article term will beat chrome. The sitemap should go from two
distinct values to several. **That is a prediction, it is written down before the fact, and
it costs one `sort -u` to check** — exactly the shape of bet this operation keeps saying it
wants: readable without anyone else's permission.

If the distinct-value count does **not** rise on flip day, the per-article term is not
reaching the resolver at all, and that is a bigger finding than this note.
