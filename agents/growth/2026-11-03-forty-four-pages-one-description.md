# Growth — 44 of 134 served pages described themselves identically, and 22 of them in the wrong language

**2026-11-03 · the day's one concrete audience action · a discoverability fix and a correctness fix in
the same two lines.**

## What was measured

Over all **134 served pages** of the built corpus, three fields read out of each `<head>`:

| field | missing | distinct values | values on more than one page |
|---|---|---|---|
| `<title>` | 0 | **134 of 134** | **0** |
| `<meta name="description">` | 0 | 91 | **1 value, on 44 pages** |
| `<meta property="og:description">` | 0 | 91 | **1 value, on 44 pages** |

Every title is unique. **The descriptions are not: one string appears on 44 pages — 32.8% of the
publication.**

The 44 are exactly the pages whose template passes no `description`, so `Base.astro`'s single default
answered for all of them: both home pages, both browse indexes, all **16 region** pages (8 EN + 8 AR),
all **16 topic** pages (8 EN + 8 AR), **8 Arabic country** pages and both editions indexes. The
articles are all individually described — the defect is entirely in the **navigational** surface, which
is the half a reader arrives at from a search result for a *subject* rather than for a *piece*.

## The sharper half, which is not about discoverability at all

**22 of the 44 are Arabic pages, and they were serving an English sentence** — in three fields each
(`description`, `og:description`, `twitter:description`), **66 declarations**, including the Arabic
edition's own front door at `/ar/`.

That is the 2026-09-13 wrong-language class — `qa_a11y_lang` bit on **471** chrome strings served under
a language they were not written in, `qa_ar_language` on **235** Arabic-page fields printing English —
living in a field **neither of those gates enumerates**. Both read text a reader can *see*. A `<meta>`
content attribute is served and never painted, so it is outside both by construction. Same shape as
**#121** (the half of a founder-facing artefact no human looks at) and **#115** (a quantity that is not
in `dist` at all), and it is today's own ruling **#126** one surface over: the gates' ruler is *rendered
text*, and a served-but-unpainted attribute is in its kernel.

## What was fixed, and the reason it cost no new prose

**Both feeds already carry this publication's self-description as a composed, per-language pair** —
`src/pages/rss.xml.ts` and `src/pages/ar/rss.xml.ts` — the Arabic *composed rather than translated* and
gated by the Arabic Editor when the feeds shipped. The pages are now given the same pair:

* **en** — *An editorial publication on early childhood and K-12 education, written and made in English
  and Arabic. A research instrument, not a magazine.*
* **ar** — *مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تتناول التعليم في مرحلتَي الطفولة المبكّرة والتعليم العام، تصدر
  بالعربيّة والإنجليزيّة. أداةُ بحثٍ، لا مجلّةً.*

**No Arabic was written today**, which is the point: the Arabic edition is composed, not translated, and
the right source for a fallback sentence is a sentence this publication has already composed and gated,
not a new one produced in a hurry by the Manager.

**And the English default turned out to be the feed's sentence with its last clause cut off.** *A
research instrument, not a magazine* — the clause that says what Madār actually is — was missing from
every page that fell back to the default. It is the strongest sentence in the pair and it was absent
from the description of 22 English pages, the English home among them.

## What was NOT fixed, and why it is a queue row rather than a rush

The 44 pages now serve **two** distinct strings rather than one. **That fixes the language and not the
uniqueness** — a region page and a topic page still describe themselves identically, and a description
is the one piece of copy this operation controls in a search result.

Per-facet descriptions are the right answer and they must be **derived, not hand-written** (2026-06-07:
anything that must equal the current article set is build-generated, never hand-maintained) — but the
*frame* around the derivation is forty-four pieces of copy in two languages, and the Arabic half needs
the Arabic Editor's gate. Composing that between one build and the next is how a publication ships
Arabic as a translation cost. **Standing-queue item 76**, for the Editor, the Arabic Editor and the Web
Developer together.

## Lead with return rate, not raw counts — and the honest line

**There is no traffic figure in this note and there will not be one.** The site carries **no
third-party tracker by design**, Search Console was never registered, and this operation does not
estimate a visitor number. What makes this a growth action rather than a guess is that its outcome is
readable **without anyone else's permission**: 134 pages, 91 distinct descriptions before and 92 after,
and 66 Arabic-page declarations moved out of the wrong language — every one of those numbers is counted
off our own built bytes, which is the only kind of bet this operation is willing to place.

## Verified

Build exit **0**, all **38 of 41** gating assertions green. The duplicate population was enumerated
before the change and re-counted after it; the Arabic pages' three fields were read out of the built
HTML, not inferred from the template.
