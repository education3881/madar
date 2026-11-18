# Growth — 2026-11-18 · the archive described itself as the front door

**Action:** the last four pages of standing-queue item **76** repaired. Every served page now has a
`<meta name="description">` that no other page has.

| | Before | After |
|---|---|---|
| Served documents | 139 | 139 |
| Distinct `<meta name="description">` | **137** | **139** |
| Pages sharing a description with another page | **4**, in two pairs | **0** |
| Distinct `<title>` | 139 of 139 | 139 of 139 (unchanged) |

---

## What was wrong, and it is not a count

`/editions/` served the **English home page's description, verbatim**, and `/ar/editions/` served the
**Arabic home page's**. Neither editions template passed a `description`, and `Base.astro` holds a single
default, so both archives inherited the front door's sentence.

**A home and an archive are not the same promise.** A description is the one piece of copy this
publication controls inside a search result, and the sentence these two pages were spending it on —
*"An editorial publication on early childhood and K-12 education, written and made in English and
Arabic. A research instrument, not a magazine."* — is true of **every page we serve**, which is another
way of saying it distinguishes none of them. A reader who reaches a result for this page is being
offered the corpus arranged by edition, and was told instead what the publication is.

This is the residue of a row that started at **44 of 134 pages describing themselves identically.** The
wrong-language half closed 2026-11-03 (22 Arabic pages serving English in three fields each, 66
declarations). The facet half closed 2026-11-05 (32 region and topic pages, 32 derived strings). What
was left was exactly four pages in two pairs, and it sat for thirteen days because **four is a small
number and the four were the two most important browse surfaces we have.**

## The repair, derived rather than written

Both strings are built from the collection at build time (2026-06-07: anything that must equal the
current article set is build-generated). Nothing to maintain, and the numbers move with the corpus:

> **EN** — *Madār's archive: 44 pieces in 5 closed monthly editions, and 1 piece outside them.
> Early-childhood and K-12 education, read from named primary sources in English and Arabic.*
>
> **AR** — *أرشيف مدار: ٤٤ مادة في ٥ إصدارات مُغلقة، ومادة واحدة خارجها. التعليم المبكر والتعليم العام،
> مقروءة من مصادر أولية مُسمّاة، بالعربية والإنجليزية.*

**The two populations are counted separately on purpose.** 44 pieces sit in editions; 1 does not, because
issue #13's default made pieces singles from 2026-11-08 and `bahrain-bqa-five-cycles` shipped on 11-09
belonging to no edition. The page's own standing block holds that distinction and its description now
carries it too. *(This is not a closure of item 92, which asks the harder version — two populations under
one heading inside the page body. It is the same distinction made in the one field a search engine reads.)*

Also derived rather than asserted: whether the editions are **closed**. The phrase reads *5 closed
monthly editions* only while every registry row has `status: 'closed'`; if one is ever `current` the
template says *monthly editions* instead. A hardcoded *closed* would be yesterday's defect — the
publication told every search engine it **was** Edition 05 for nine days — in the field one page over.

## The Arabic half is the finding, and it is the gate item 76 was still owed

Item 76 recorded, correctly, that the uniqueness half was done on 11-05 but that **the Arabic Editor's
gate on the frame's wording** was still owed. It is given today, by the same desk that gated the England
composition this morning, and it passes — **because a derived count in Arabic is four constructions and
not one interpolation**:

| n | Construction | This page serves |
|---|---|---|
| 1 | singular | `مادة واحدة` ✓ (the 1 piece outside the editions) |
| 2 | the **dual**, which English does not have | `مادتان` |
| 3–10 | plural of paucity, genitive | `٥ إصدارات` ✓ |
| 11+ | accusative singular | `٤٤ مادة` ✓ |

**And the adjective agrees with the counted noun in every one of the four**, which the 11-05 template
did not have to handle because no facet description carried one. `إصداران مُغلقان` is not
`إصداران مُغلقة`, and `٥ إصدارات مُغلقة` takes the feminine singular because a non-human plural does.
So the edition noun and its adjective move together through all four branches. An English template needs
`n === 1`; this one needs eight forms.

Three of the four branches are exercised by the corpus today and all three are grammatical in the served
bytes. **The dual is the branch nothing exercises**, and it is written and unexercised on purpose: it
fires the day a second piece ships outside the editions, which on the current ledger is the next flip.

Arabic-Indic numerals via `ar-EG`, the tag this edition uses on every other page, so the description
matches the dates beside it.

## Why this was invisible

A `<meta>` content attribute is **served and never painted.** `qa_a11y_lang` and `qa_ar_language` both
read text a reader can see, so neither enumerates it — which is how 22 Arabic pages served English
descriptions for 162 days before 11-03. The uniqueness half has the same property one step further out:
**nothing in this operation asserts that two pages describe themselves differently**, so this repair can
regress on the next template that forgets to pass a description, and the only instrument that would
notice is a hand count. Raised as queue item **130**.

## Traffic, stated plainly

**The site carries no third-party tracker, no analytics and no third-party request by design**, so there
is no visitor number here and none is estimated. What this action buys is not measurable by us as
traffic, and the honest claim is narrower and checkable: **139 of 139 served pages now offer a distinct
description, counted from the served bytes by this run.** That is a property of the artefact, which we
own, rather than a forecast about a search engine, which we do not. The outcome we can read without
anyone's permission is the count itself, and it is the one stated.
