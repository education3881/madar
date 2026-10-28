# Our own headline forms — a census of six, across 134 served pages

**Growth function, 2026-10-28.** Ruling **#119**, filed this morning from the queue head, says that a
document serves several forms of its own headline — `<h1>`, `<title>`, `og:title`, `twitter:title`, a
JSON-LD `headline`, a URL slug — that these drift apart, and that a quotation mark promises the one the
document *prints*. Six published misquotations were repaired on that finding, every one of them a form
some other publisher served about their document rather than the form they printed.

**The obvious next question is the one about us, and nobody had asked it.** If a drifting headline is a
trap for whoever cites someone else, it is a trap for whoever cites Madār — and the same forms are what
search engines, feed readers and social cards actually read. So: do our own 134 served pages agree with
themselves?

Measured in `dist` over every served document, no new tool, one script.

## The result, leading with what a consumer reads

| Pair | Documents where the two disagree |
|---|---|
| `<title>` vs `og:title` | **0 of 134** |
| `<title>` vs `twitter:title` | **0 of 134** |
| `og:title` vs `twitter:title` | **0 of 134** |
| `<h1>` vs JSON-LD `headline` | **0 of 132** (46 documents carry no `headline`, all of them non-article pages, by design) |
| `<h1>` vs `og:title` | 132 of 132 — **and this is a convention, not a drift** |

**Madār serves exactly two headline strings per page, and the relation between them is a pure suffix.**
`og:title` is the `<h1>` plus ` — Madār` on an article, ` · Browse · Madār` on a browse facet, ` · Madār`
on a section index. A citer who copies either one gets a string that reduces to the other by removing a
known, constant site suffix. That is the opposite of the six registers repaired this morning, where the
forms differed in **words, word order and punctuation** — `raises rigor` against `raises testing rigor`,
`under new government` against `under South Korea's new administration`, an inner quotation present in
one form and absent in the other.

So the honest headline of this census is: **on the property #119 is about, this publication is clean,
and it is clean because two of its forms are generated from one source and the third is generated from
the first.** The defect class #119 names arrives when a human copies; ours are composed by a template.

## Three things the census found anyway

**1. Both home pages serve no `<h1>` at all.** `/` and `/ar/` are the only two of the 134 with no
top-level heading in the document. The masthead wordmark is an `<a>` carrying an `aria-label`, which is
correct for a link and is not a heading, so **each front door's heading outline begins at an `<h2>` that
is one specific article's title** — the lead piece. A consumer building an outline of the English home
page is told the page is about *Rwanda counted the teachers it had not trained, twice*. This is the two
highest-value pages in the publication, and it is the only finding of the three that a reader using a
screen reader or a heading-navigation shortcut meets directly. **Raised as standing-queue item 49,
DEFECT, 2 artefacts** — not fixed here, because a heading on a front door is a served-bytes and
design-system decision that belongs to the Web Developer and the Designer (the 09-27 split), and because
the correct fix has at least three candidate shapes (a visually-hidden `<h1>`, promoting the tagline,
promoting the wordmark) and this operation has no utility class for the first of them.

**2. `/valence/`'s `<h1>` served `The Elementsof goodEducation` to every machine that read it — FIXED
TODAY.** The heading is three `<span class="ln">` line boxes with no whitespace between them. `.mega .ln`
is `display: block`, so the page *looks* exactly right and has since 2026-08-08; the string any crawler,
screen reader or quoting reader extracts has two missing spaces in it. **This is #119 pointed at us and
landing**: the form the document prints *visually* and the form it serves *as text* were different
strings, and every instrument we own reads text. Repaired by inserting a newline between the spans —
whitespace between block-level elements contributes nothing to the rendering, so the fix is **visually
inert by construction** and the extracted string is now `The Elements of good Education`.

**3. `/valence/` and `/about/` are the only two pages where our two forms differ by more than the
suffix**, and both are deliberate rather than broken. `/valence/` prints `The Elements of good
Education` and declares `VALENCE — The Elements of Good Education`: a prefix the page's own wordmark
supplies visually, and a capital *G* where the design keeps the rotating word lowercase. `/about/`
prints `About Madār` and declares `About — Madār`, the suffix rule correctly declining to append a
second *Madār*. Recorded rather than changed — a design that says the same thing two ways on purpose is
not the defect #119 describes, but **it is the thing that makes a census necessary to tell them apart.**

## Why this is a growth action and not a QA one

The three forms a social or search consumer reads — `<title>`, `og:title`, `twitter:title` — agree on all
134 pages, which is the discoverability claim this operation can actually make without anyone's
permission. The two that a *human* or a *crawler* extracts from the page body — the `<h1>` and the
JSON-LD `headline` — agree with each other on all 132 that have both, and were **wrong on one page and
absent on two**. The site carries no third-party tracker by design, so there is no traffic number here
and none is estimated. What is readable without permission is this: of the six headline forms this
publication serves, five were already consistent, one page's body heading was unreadable as text for 81
days, and the two front doors have no heading of their own.

**Return-rate framing, honestly:** nothing in this census moves a return rate on its own. What it does is
remove the two ways a reader or a machine could carry away a wrong string about a Madār page — which is
the same promise the og:image fix made on 2026-08-18 and the chrome-link sweep made on 2026-08-16, and
both of those were found the same way: by asking what a consumer at the other end actually receives.

## Forward

The census covers the pages. It does not cover **the two feeds**, which serve a `<title>` per item and
a channel `<title>`, nor the **og cards**, which carry a rendered title as pixels. A feed item's title
is a seventh form, a card's is an eighth, and this census read neither.
