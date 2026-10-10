# Growth — what a reader actually downloads for our typefaces

**Taken:** 2026-10-10, by the daily run. **Lane:** Growth (reader experience).
**Why now:** the 2026-10-08 run self-hosted five typefaces and made a *design* claim it
did not measure. This measures it.

---

## The claim that was made and not measured

The 10-08 closure of standing-queue item 4 rests on one argument, quoted from its own
record: Google's `css2` response is **73 `@font-face` blocks over 34 files** carved into
`unicode-range` subsets, so the five hand-written `@font-face` rules every tutorial shows
*"would have shipped the entire Arabic face to every English reader and been a
performance regression dressed as a privacy fix."* The bundle was therefore generated as
a **mirror** of that response rather than hand-written.

The argument is sound. **Nothing measured what a reader now fetches**, and the run's own
forward note said as much: the new assertion *"asserts where we do not point and never
what arrives."* The 10-08 measurement was a **face count** (`document.fonts`), which is
not a byte count and, per that run's own ruling #92, is not even an arrival count.

## Method, and its one weakness stated first

Each built page was copied, a probe script appended that reads
`performance.getEntriesByType('resource')` after load, and the copy served over loopback
to headless Chrome — the same probe shape the four Chrome-driven assertions already use.
**These are observed network fetches, not a model of them.**

One thing this does *not* measure: the live origin's `Content-Encoding`. `woff2` is
already compressed and GitHub Pages does not usefully re-compress it, and the
`encodedBodySize` figures below match the on-disk file sizes, so the gap is small — but
it is a loopback measurement and it is labelled as one.

## The numbers

| Page | woff2 files fetched | bytes | families fetched |
|---|---|---|---|
| EN home | 12 | **778,376** | Amiri, Cormorant Garamond, JetBrains Mono, Newsreader |
| AR home | 11 | **705,600** | + Cairo |
| **EN article** | **7** | **501,864** | Amiri, Cormorant Garamond, JetBrains Mono, Newsreader |
| *whole bundle on disk* | *34* | *2,792,392* | *all five* |

**The article page is the one that matters.** It is where a search visitor lands and it is
118 of our 120 served pages.

## What this establishes

**1. The mirror decision was worth roughly 2.29 MB per first-time English reader.** The
naive five-rule implementation serves every family whole: 2,792,392 bytes. The mirror
serves **501,864** on an English article. The `unicode-range` slicing is doing exactly
what the 10-08 run said it would, and the figure it was worth is now on file instead of
asserted.

**2. An English page does fetch an Arabic subset, and that is correct.**
`amiri-normal-400-arabic.woff2` is fetched on the English home *and* on the English
article. Not a leak and not a regression: the English pages genuinely render Arabic — the
wordmark, and every Arabic title in the pair rails. The browser fetched the subset
because the glyphs are on the page. **What the 10-08 argument prevented was shipping the
*whole* Arabic face to readers who need four characters of it**; the EN pages pull Amiri's
Arabic subset and never Cairo's, while the AR home pulls both. The mechanism discriminates
at exactly the granularity claimed.

**3. My own derived estimate was wrong by 47%, which is why this was measured.** Before
running Chrome I computed the answer the way the browser does — intersecting each face's
`unicode-range` against the page's codepoint set — and got **1,141,776 bytes** for the EN
home against an observed **778,376**. The derivation over-counts because it credits every
family whose range intersects the page, while the browser fetches a subset only for text
actually *rendered in that family*. **A model of a consumer is not the consumer** — #16's
rule, and the 08-18 share-card defect is the same shape: verify against *that machine*,
never against our own reasoning about it.

**4. `document.fonts.size` is 73 on every page, including pages that fetch 7 files.** All
73 declarations register; 7 arrive. This is **ruling #92 from the other side** — that
ruling found `document.fonts.check()` returns `true` with zero faces loaded; here `.size`
is constant across pages with a 277 KB spread in actual transfer. Independent instance,
same lesson: **the Font Loading API describes what the stylesheet declared, never what the
network delivered.** Anyone reaching for it as a *did our typeface arrive* instrument will
get a number that cannot move.

## The action this does NOT take, and why

**502 KB of webfont on an article page is heavy**, and four families on one page is a
design choice no one has re-read since 2026-05-25. The obvious reductions — subsetting to
our own corpus's glyph inventory rather than mirroring Google's generic slices, or
dropping a family — are **served bytes**, which the role split assigns to the Web
Developer even when another lane found it, and a typeface change is a **Designer**
judgment about the publication's face. Three days after a font migration and one day
before the Edition 05 gate is the wrong moment, for the same reason the 09-18 audit gave
for deferring the migration itself: *not while something bigger is in the commit.*

**Entered on the standing queue instead**, with this measurement as its specification, so
it is queued rather than merely mentioned (the queue's own rule).

## Growth reading, per the CHARTER

Return rate, not raw counts — and there is no return-rate number, because **the site
carries no third-party tracker by design and none was added here.** Every figure above
was taken from our own files and our own browser. This is the kind of bet the CHARTER
prefers: *an outcome the operation can read without anyone else's permission.* Page weight
is the one reader-experience number we can measure honestly, it affects discoverability
through Core Web Vitals, and as of today it has a baseline: **501,864 bytes of webfont on
an English article, 2026-10-10.**
