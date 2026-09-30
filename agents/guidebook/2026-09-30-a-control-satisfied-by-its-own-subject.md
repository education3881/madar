# Ruling #78 — a control satisfied by the component the claim is about is not a control

**Filed:** 2026-09-30, by the Verifier's verdict on Edition 05 row 6 (Rwanda), item 3.
**Family:** the enumeration family, on its **input** side — the 2026-09-14 masking trap restated for a
citation instead of an assertion.
**Cousins:** #47 (a description's date is not the document's date), #74 (a hash proves the injection
landed, not where), #76 (a serving state is an observation with a date), and the 09-14 finding that
*the field the assertion exists to supplement was masking the assertion.*

---

## The ruling

**When a claim about a page is proved by finding a string on that page, the proof must name *where on
the page*.** A template serves the same furniture to every page it renders; a string found in the
furniture is evidence about the template, not about the article. And the trap has a specific, repeatable
geometry: **on exactly one page, the furniture and the subject coincide** — the latest-news rail's
newest entry is the newest article, so on that article's own page the rail appears to be a byline.
That page is the one a careful reader will pick as the control, precisely because the string is there.

**Second limb, and the one that cost the error here: a finding about a template applies to every page
that template serves, including the page you are about to use as your control.** If you have just
established that a host's news pages carry no date of their own, you have established it about *all* of
them. Re-deriving it per page is the work; not re-deriving it, and then leaning on one of those pages
as independent evidence, is the defect.

---

## What happened, measured

Edition 05 row 6's `sources[]` entry **4** says, correctly and carefully, of MINEDUC's QBE progress
note: *"the article page itself carries no publication date, byline date or timestamp of any kind —
every date string on the page belonged to the sidebar's latest-news rail and none to the article."* It
then rests the note's date on the ministry's news index and proves the index's pairing on a control:

> *"the index dates the 10 August 2026 reforms release to Monday, 10 August, 2026, **which is the date
> that release prints on its own page.**"*

Entry **5**, the very next annotation, says of that release: *"dated on its own page Monday, 10 August,
2026."*

Measured on 2026-09-30, on three MINEDUC `news-detail` pages:

| page | `<time itemprop="datePublished">` elements | which ones |
|---|---|---|
| QBE progress note | **9** | the latest-news rail, 10 Aug 2026 → 21 Feb 2026 |
| reforms release | **9** | **byte-identical set, same order** |
| salary communiqué | **9** | **byte-identical set, same order** |

**No MINEDUC news page dates its own article.** The reforms release's "own page" date is its own entry
in the rail — because the rail's newest item *is* the reforms release. One page in the corpus has that
property, and it is the page that was chosen as the control.

So the control does not exist. What actually agreed was the index's rendering of a date and the rail's
rendering of the same CMS field: two templates over one record, a consistency check and not an
independent confirmation. **The body was right throughout** — it says the date is the index's — and the
*proof* behind the body was the thing that was wrong, which is the more dangerous of the two, because a
wrong proof reads as a green.

---

## The control that does exist, and how it was found

Two replacements, both measured, and together they make *"the date is the index's"* a complete statement
rather than a hedge:

1. **The index's own ordering.** Strictly reverse-chronological; the note sits on **page 3 of 35 between
   a 17 November 2025 item and a 30 October 2025 item**, dated Wednesday, 05 November, 2025.
2. **A positive enumeration of where the date is *not* served on that host:** no
   `article:published_time`, no date in the page's JSON-LD (breadcrumbs only), `sitemap.xml` **404**,
   both TYPO3 news-feed routes **500**.

**Method note that belongs in the ruling, because it nearly ate the re-verification:** page 3 is only
reachable through the index's own pagination `href`, which carries a required `cHash`. A guessed
`currentPage` parameter returns **page 1 silently, with HTTP 200**. A verification that had guessed the
URL would have re-read page 1 and reported agreement — with itself. *The same defect as the control:
a request that answers 200 has not necessarily answered the question.*

---

## The general form

*Ask not only "is the string there?" but "what would put it there if my claim were false?"* — the 09-14
question (*where does the string I am looking for also legitimately appear?*) asked of a citation rather
than of a regex. On a templated site the answer is almost always **the furniture**, and the furniture is
identical on every page, which is exactly what makes one page's copy of it look like evidence.
