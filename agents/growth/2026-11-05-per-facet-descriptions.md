# Growth — 2026-11-05 · the 32 facet pages now describe themselves, and the Arabic half needed four constructions where the English needed two

**Action:** per-facet `<meta name="description">` on every browse page, both editions, **derived from
the collection at build time and hand-written nowhere.**
**Queue row:** item **76**, narrowed rather than closed.

---

## 1 · The state this acted on

Item 76 measured, on 2026-11-03, that **44 of 134 served pages carried one identical
`<meta name="description">`** — both homes, both browse hubs, all 16 region pages, all 16 topic pages,
8 Arabic country pages and both editions indexes — because none of those templates passed a
`description` and `Base.astro` held a single per-language default. The **wrong-language** half was
repaired that day (22 Arabic pages were serving English in three fields each). **The uniqueness half
was not**, and the row said so in writing: *a region page and a topic page still describe themselves
identically, and a description is the one piece of copy we control in a search result.*

That matters for the reason the 11-02 growth function established about the `related:` rail: **the
likeliest landing page for a reader who has never heard of this publication is not the home.** A facet
page is a page about a question — *AI-readiness*, *ECE access*, *MENA* — and it was telling every
search engine the same sentence as 43 other pages.

## 2 · What shipped

| | Before | After |
|---|---|---|
| Served pages carrying a description | 134 of 134 | **135 of 135** |
| **Distinct** descriptions | **91** | **133** |
| Pages sharing their description with another page | 44 | **4** |
| Facet pages (16 region + 16 topic + 8 country + 2 hubs, both editions) | one string | **32 distinct, 2 hubs distinct** |

**Derived, never hand-written**, per the 2026-06-07 rule — anything that must equal the current article
set is build-generated. The counts move with the corpus, which is precisely why this is **two template
edits rather than forty-four pieces of copy to maintain**:

* region — `Madār's 15 pieces from MENA, across 13 countries: early-childhood and K-12 education, read
  from named primary sources in English and Arabic.`
* topic — `Madār's 6 pieces on AI-readiness, across 6 countries: …`
* country — `Madār's N pieces on education in Bahrain: early-childhood and K-12, …`
* hub — `Every Madār piece by region, topic and country: 44 pieces across 42 countries, …`

## 3 · The finding, and it is the Arabic half

**A derived count in Arabic is not one construction. It is four.** The English template needs
`n === 1`; the Arabic template needs all of:

| n | Arabic | Why |
|---|---|---|
| 1 | `مادة واحدة` | singular |
| 2 | `مادتان` | the **dual**, which English does not have |
| 3–10 | `٦ مواد` | the plural, genitive |
| ≥ 11 | `٤٤ مادة` | **singular again**, accusative |

The same four shapes govern `بلد` (`بلد واحد` · `بلدان` · `٦ بلدان` · `١٣ بلدًا`). A template that
interpolated a numeral in front of one noun form — the obvious translation of the English — **would be
ungrammatical on most of this corpus**, and it would have been ungrammatical silently: a `<meta>`
content attribute is served without ever being painted, so no render check and no reader would ever
have seen it. That is #121's shape (*the half of an artefact nobody looks at*) meeting #86's
(*composition, not translation*), and it is the second time in three days that the Arabic edition's
grammar turned out to carry a distinction the English edition does not have to make.

Numerals are Arabic-Indic via `Intl.NumberFormat('ar-EG')` — the tag this edition already uses for every
date, chosen on 2026-09-14 because plain `'ar'` resolves to `latn` and serves `7 يوليو 2026`.

**It is composed and it still owes the Arabic Editor's gate on the frame**, which is noted on item 76:
the sentence is formulaic by design, the four branches are grammar rather than style, and the Arabic
Editor's call is on the frame's wording — `مقروءة من مصادر أولية مُسمّاة` — not on the arithmetic.

## 4 · What remains, and it is exactly four pages

**Four of 135 still share a description, in two pairs, and both pairs are `home ≡ editions index`.**
The home keeps the publication's own sentence — which is correct, it being the publication's front door
— and the editions index inherits it as a fallback. An editions index knows something the home does not
(*five editions, 44 pieces, October 2026 the latest*) and could derive its own in the same way. **Item
76 is narrowed to that, and the measurement is written into the row** rather than left for whoever next
reads the file.

## 5 · No traffic figure

The site carries no third-party tracker by design, so this action's effect on arrivals cannot be read
here and is not estimated. **What the operation can read without anyone's permission** is the thing
asserted above: 133 distinct descriptions over 135 served pages, counted out of `dist` by the same
method that measured the 91, and re-countable by any later run. *A description is a promise to a
machine we do not own (#18's consumer-format reasoning); the part we own is whether the promise is
distinct, true, and in the reader's language.*

---

**Signed** · Manager, growth function · 2026-11-05 · build exit 0, 39 of 42 gating assertions green,
`qa_a11y_lang` and `qa_ar_language` both clean on the new Arabic strings.
