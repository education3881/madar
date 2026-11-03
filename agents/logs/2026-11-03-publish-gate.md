# Publish gate — 2026-11-03

**Written before the editorial commit, per the CHARTER and the RUNBOOK.** Nothing is published today
and no flag moves. **The gate still runs in writing**, because the day changed **served bytes on 44
already-approved pages**, and a change to the publication is gated whether or not it is a new piece.

## What is being published

**No new piece. No flag change. One change to the site chrome, touching 44 pages in both editions.**

`web/src/layouts/Base.astro` — the default `<meta name="description">` becomes a **per-language pair**
instead of a single English string. It reaches `description`, `og:description` and
`twitter:description` on every page whose template passes no description: both homes, both browse
indexes, 16 region pages, 16 topic pages, 8 Arabic country pages, both editions indexes.

**No body text, no frontmatter, no `approved:` flag and no article file is touched.** The 88 article
pages are unchanged — every one already carries its own description from its `dek`.

## The gate, row by row

| Gate | State |
|---|---|
| Editor verdict on file for anything newly published | **n/a — nothing is newly published.** No piece moved to `approved: true`. |
| Arabic verdict / Arabic Editor gate | **Satisfied without a new gate, and this is the load-bearing row.** The Arabic sentence now served on 22 pages is **not new prose**: it is this publication's own self-description, already composed (not translated) and already gated by the Arabic Editor when the Arabic feed shipped, and it is served today byte-identical to the string in `src/pages/ar/rss.xml.ts`. **No Arabic was written by the Manager today.** Had a new Arabic sentence been needed, this gate would have blocked and the change would have waited. |
| Hero still + share card on disk | **n/a** — no new piece. `og:image` is unchanged on all 134 pages. |
| `astro build` clean | **exit 0.** |
| Standing assertions green | **38 of 41 gating, all green**, including the twelve build-job gates via `build_job_gates` and the **widened** `qa_render` (assertion 14, its ruler changed this morning under ruling #126). |
| Held-slug leak zero | **Zero.** `approved: false` pieces contribute no page, no sitemap entry, no feed item, no `lastmod`, no bytes. The Bahrain piece is held and leaked nothing. |
| Change verified in the SERVED bytes, not in the template | **Yes.** Re-counted over all 134 built pages after the change: **92 distinct descriptions** (from 91), two values on more than one page (22 Arabic + 22 English, one per edition), and **0 Arabic pages serving a non-Arabic description**, down from 22. |

## Why this change is a correction and not a preference

**22 Arabic pages were serving an English sentence in three fields each — 66 declarations, including the
Arabic edition's own front door.** That is a served artefact that was wrong, in the 2026-09-13
wrong-language class, in a field neither `qa_a11y_lang` nor `qa_ar_language` enumerates because both
read text a reader can see and a `<meta>` content attribute is never painted. It was **fixed in the run
that found it** rather than raised as a DEFECT row, which is why the board carries no DEFECT tonight.

Secondarily, the English default was the feed's own sentence with its last clause — *A research
instrument, not a magazine* — **cut off**, so 22 English pages have had the strongest line of the
publication's self-description restored.

## The Bahrain piece — verified today, and still explicitly NOT gated

`2026-10-23-bahrain-bqa-five-cycles` received the **Verifier's verdict today**
(`content-drafts/verdicts/2026-11-03-bahrain-bqa-five-cycles-verification.md`): **twenty-three figures
re-counted from an independently fetched serialisation of the register with zero discrepancies, and one
binding correction found, applied and re-verified.** It did not approach this gate and must not. **The
flag is four things away, one of them not ours:**

1. **`approved: false` stands.** No page, no sitemap entry, no feed item, no `lastmod`, no bytes.
2. **Arabic composition has not started**, so there is no pair and the Arabic Editor's gate has not
   run. It carries a live **park condition**: the four populations must be holdable apart in Arabic.
3. **No hero still and no og card.**
4. **The `edition:` field is HELD, not guessed** — there is no Edition 06, the registry exports
   `hasOpenEdition: false`, and the question is founder **issue #13**, default **2026-11-08**.

Item 3 of yesterday's five — *no Verifier verdict* — is closed. **The count went five → four and the
remaining four are unchanged.** A verdict is not a clearance.

## Signed

Manager · 2026-11-03 · build exit 0, 38 of 41 gating assertions green, **nothing published and no flag
moved**, one chrome correction to 44 pages verified in the served bytes, one verification verdict
recorded, one approved piece correctly unshipped.
