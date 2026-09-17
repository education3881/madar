# Growth — the bilingual entry point, counted

**Growth · 2026-09-17** · read off the build, no tracker, no estimate
**Occasioned by:** today's QA finding (ruling #55) — 149 Arabic runs served with their
letter-joins pulled apart, across both editions

---

## Why this is a growth note and not only a quality one

The CHARTER's traffic loop, point 4: *"bilingual reach (Arabic is a distribution
advantage, not just a translation cost)"*. That advantage is not delivered by the Arabic
articles existing. It is delivered by the **path** from one edition to the other — the
handful of Arabic strings that sit inside the English layout and say *this exists in your
language*. Today's defect landed on exactly that path, and it landed on all of it.

## The count

Measured from `web/dist` as built 2026-09-17. Nothing here is estimated; every number is
a count of served elements.

| | |
|---|---|
| English pages in the build | **61** |
| Arabic pages in the build | **59** |
| English pages carrying an Arabic-marked element | **61 — 100%** |
| Arabic-marked elements on the English side | **264** |

The strings themselves, by frequency:

| Count | String | What it is |
|---|---|---|
| **119** | العربية | the language switch in the header and footer of every English page |
| **60** | مدار | the wordmark's Arabic half, and its CSS-only fallback |
| **38** | النسخة العربية ↗ | the cross-language rail — one per English article, the link to its twin |
| **38** | سكون · | the Still's caption, on every article |
| 1 each | عن مدار · حول مدار · التعليم، بتأنٍّ، بلغتين · … | the About page's Arabic block and the home's tagline |

**Every one of the 264 was tracked** — `letter-spacing` inherited from rules written for
Latin mono labels — and therefore rendered as disconnected letterforms rather than joined
script. For the life of the bilingual site.

## What that means in audience terms, stated without inflation

It does **not** mean the links were broken. They resolved, they were crawlable, the
hreflang cluster was reciprocal, and `qa_reachability` was right to pass on every one of
them. A reader who clicked arrived.

It means that the moment at which an Arabic-reading visitor to the English edition is
asked to trust that this publication can set their language, **the publication was
visibly failing to set their language.** `العربية` rendered with pulled joins is the
typographic equivalent of a misspelling in the one word that has to be right. It is a
first impression, and it was made 119 times per crawl of the site.

There is no way to measure what that cost, and this note will not pretend otherwise —
**the site carries no third-party tracker by design, and no visitor number is estimated
here or anywhere.** What can be said is what changed: as of today the count of tracked
Arabic runs on the served build is **zero**, asserted on every build by standing
assertion 17, and proved to fail if it ever returns.

## The share card — checked, and correct, which is the finding

Every Arabic page declares a raster share card, and the brand card is what 44 pages hand
to a social consumer. It was rendered and looked at today: **the Arabic wordmark مدار
carries its joins correctly.** That is not reassurance. It is the shape of the defect:
the 2026-08-18 fix removed tracking from the Arabic wordmark on the **card** and never
reached the **page**, and for thirty days the card that advertised the Arabic edition was
better typeset than the edition. A correction has a blast radius (#50), and that one's
radius was one file.

## What this changes in the growth plan — nothing, deliberately

No new bet is opened on the back of this. The standing Edition 05 wave packet is unchanged
and still held with the wave; nothing posts before the wave gate and a green `verify` job.
What this note does is close a question the growth loop had never asked: *is the
distribution advantage actually being delivered at the surface where it is claimed?* It
was not. Now it is, and the instrument that says so runs on every build rather than when
somebody remembers.

**Owed, and named rather than dropped:** the same question applied to the feeds — the
surface carried unanswered since 2026-08-18. Both feeds serve 38 items and nothing has
ever verified that an Arabic item renders legibly in a reader, carries its direction, or
resolves from outside our origin. Today's finding raises the prior on that considerably:
the defect class we just found is *chrome composed in one script and styled by rules
written for another*, and a feed reader applies **its own** stylesheet to our Arabic. We
control less there, not more.

— Growth · 2026-09-17
