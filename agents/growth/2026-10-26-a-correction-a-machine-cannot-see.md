# Growth — a correction a machine cannot see did not travel

**Date** 2026-10-26 · **Function** Growth, daily run · **Owner** Web Developer (served bytes), measured by
the Assertions Engineer's instruments · **Outcome readable without anybody's permission:** yes, by counting
pages in `dist`.

---

## What was done, and why today

This morning's content function repaired **nine served sentences across four pieces** under ruling #117 —
claims written in this publication's own future tense whose dates had arrived. The sitemap's `<lastmod>`
moved for all eight affected URLs, correctly, because the resolver reads git.

Then the obvious growth question: **did anything else tell a consumer those pages changed?**

**No. Zero of 88 article pages carried a `dateModified` in their structured data.** Every article's JSON-LD
declared `datePublished` and nothing else — which asserts, to every consumer that reads JSON-LD rather than
the sitemap, that the page has not changed since the day it published. For `australia-naplan-reset` that
claim was *July*. The sitemap said one thing and the page's own machine-readable description said another,
and the page is the louder channel: `schema.org/Article`'s `dateModified` is the field a search engine reads
for freshness, and an article structured-data block that omits it is an article that has never been revised.

**This is ruling #117 on the machine-facing surface.** The reader was being told something false in a verb;
the crawler was being told something false in a missing field. Both were repaired today.

## The change

`articleJsonLd` now takes an optional `dateModified` and the two article route templates pass it from
**`createLastmodResolver()` — the same git-derived resolver the sitemap already uses.** Not a build
timestamp, not the frontmatter date. Those two were rejected for `<lastmod>` on 2026-08-24 and the reasons
are unchanged: a build timestamp says every page changed on every deploy, which is the canonical unreliable
pattern a crawler discards; the publication date asserts the page has never changed, which is false for
every page on this site. **One resolver, two channels** — the 2026-06-07 rule, that anything which must
equal the current state of the corpus is generated and never hand-kept, applied to a second consumer.

The field is **omitted rather than guessed** when the resolver cannot answer. A fabricated freshness signal
is worse than none.

## Measured, after

| | Before | After |
|---|---|---|
| article pages carrying `dateModified` | **0 of 88** | **88 of 88** |
| disagreements with the sitemap's `<lastmod>` on the same URL | n/a | **0 of 88** |
| distinct values | — | 2026-10-25 × 81 · **2026-10-26 × 7** |

**The differential control is this run's own asymmetry, and it is the proof that matters.** The English
`rak-iqra` page reads **2026-10-26** and the Arabic one reads **2026-10-25** — because the English sentence
expired and was corrected today, and the Arabic sentence was deliberately left alone, its bare imperfect
never having expired at all (#117). **A page that did not change does not claim to have changed.** That is
exactly the property build-time stamping cannot have, demonstrated on a pair this operation repaired
asymmetrically four hours earlier rather than on an invented example.

## What this is NOT, stated so nobody reads it as more

* **It is not a traffic number.** The site carries no third-party tracker by design, Search Console never
  registered, and nothing here estimates a visitor, an impression or a rank. What is measured above is
  bytes in `dist`, counted.
* **The signal is coarse, and the coarseness is the resolver's documented design.** 81 of 88 pages read
  2026-10-25 because that is `max(content file, newest chrome file)` and the chrome moved that day — so
  `dateModified` means *the last time anything that renders this page changed*, not *the last time this
  page's text changed*. That is already true of the sitemap and is the honest reading of a page built from
  shared components; the 2026-09-06 forward question about an **output-bounded** date (a per-URL content
  hash across deploys) is the sharper instrument and is still owed, now with a second consumer behind it.
* **Nothing asserts it yet.** No gate fails if a future template change drops the field. That is a real gap
  and it is the one this note hands on — see below.

## Handed on

* **To the standing queue (OPEN):** nothing gates `dateModified`'s presence. 88 of 88 today is a
  measurement, and the 2026-09-13 rule is explicit that a check nobody wires is a habit. The cheap
  assertion is *every article page in `dist` carries a `dateModified` ≥ its `datePublished`, and it equals
  the sitemap `<lastmod>` for the same URL* — a one-line extension to `qa_date_identity`, which already owns
  the date-identity question and is already gated. Raised as **item 44**.
* **To the founder, nothing.** This needed no decision and no credential, which is the kind of growth bet
  the CHARTER asks for: *prefer bets whose outcome the operation can read without anyone else's permission.*
