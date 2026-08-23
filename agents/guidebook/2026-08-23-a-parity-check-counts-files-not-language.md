# A parity check counts files, not language

**Filed:** 2026-08-23 · **Ruling #33** · Section 1, row 26
**Opened by:** the daily QA pass, not by a recon — the second consecutive defect found by asking what the *consumer* receives rather than what the *repository* contains.
**Kin:** #16 (verify in the judging environment) · the 2026-08-18 og:image finding (a link that resolves is not an asset that renders) · the 2026-08-16 silent-pass trap (an assertion finding nothing to check has failed, not passed).

---

## The rule

**A bilingual publication's parity check must read the words on the page, not count the artefacts behind it.** "38 Arabic files exist for 38 English files" is a statement about the repository. It is not a statement about what an Arabic reader sees. The two are different claims and need different assertions.

**Corollary, and the sharper half:** **markup that declares a language is a claim, and a claim is checked.** `lang="ar"` is an assertion about the content inside the element. An automated check that looks for the *presence* of `lang` and `dir` verifies that we made the claim, not that the claim is true — and the presence of correct language metadata around incorrect content is the most durable form of this defect, because it survives every audit designed to catch its absence.

---

## The origin case

From the first publish on **2026-05-25** until **2026-08-23** — 90 days, the entire life of the publication — every Arabic page printed the English controlled vocabulary to an Arabic reader.

An Arabic article page carried, in three separate places:

- byline block: `سيراليون` … no. **`Sierra Leone · Africa`**
- marginalia «المرجع الميداني»: **`Sierra Leone · Africa`** / `المرحلة · K-12` / `المحاور · value of teachers، ECE access، government-led programs`
- related-reading rail, under an Arabic headline: **`Sierra Leone · Africa`**

The Arabic home page and the Arabic editions index carried the English country on every card. The Arabic RSS feed — built 2026-08-16 to make good on a footer link — gave every item an Arabic title, an Arabic dek, and an **English `<category>`**.

**The worst line in the codebase, and the reason nothing caught it:**

```astro
<span class="piece__country" lang="ar" dir="rtl">{piece.data.country}</span>
```

The markup asserts the content is Arabic, sets the direction for Arabic, and then interpolates `Sierra Leone`. Every check we owned passed. Parity counted 38 against 38. The build was clean. The links resolved. `hreflang` was reciprocal, 476 pairs. `lang` and `dir` were present *and correct*. **Not one of them read the words.**

---

## Why the defect class is structural, not careless

`content.config.ts` is **one schema shared by both collections** — deliberately. An Arabic article stores `country: Sierra Leone`, `region: Africa`, `level: K-12`, `themes: [value of teachers]`, and it **must**, because that is what makes the two corpora comparable: one controlled vocabulary, one enum, one tag set, one set of counts in `madar_stats.py`.

So the data was right and the display was wrong, and **nothing in the pipeline distinguished the two.** The frontmatter is correct English data; the page is an Arabic surface; the schema had no place to say "this field is data, never display." That is the general shape:

> **A controlled vocabulary is data. Data crossing a language boundary needs a display layer, and the display layer needs its own assertion.**

Every field a *writer* composes (title, dek, body, source titles) was Arabic from day one, because a human wrote it in Arabic. Every field the *site* generated from the schema was English, because no human ever wrote it at all. **The defect lives exactly where authorship ends and templating begins** — which is precisely where editorial review does not look and automated checks do not read.

---

## The fix, and why it took the shape it did

`web/src/lib/i18n-geo.ts` — a display layer, not a data change:

- `COUNTRY_AR` (35 shipped + 17 pre-mapped for Ed05), `REGION_AR` (the enum, exactly), `LEVEL_AR`, `THEME_AR`.
- **The schema is untouched. No article file was edited. The English side renders identically.** One place to correct a rendering.
- **Fail-loud, never fail-quiet.** An unmapped key returns the English string — a new country must render *something* rather than break a build — but every fall-through is recorded and `missingArabicGeoKeys()` reports it. A silent English fallback is the exact defect the module exists to end, so it is never permitted to be silent.
- **Ed05 countries were mapped before the pieces exist**, so the first Arabic composition of the Zambia piece cannot land on a fallback.

`agents/tools/qa_ar_language.py` — the standing assertion, added to the daily sweep:

- Extracts the **chrome** — byline meta, marginalia, related meta, listing country — and fails on Latin-script controlled vocabulary inside it.
- **Deliberately does not check body text or the sources list**, because Latin script there is *correct and required*: ruling **#28a** keeps an institution's own Latin tag (*Universidad de Santiago de Chile*, *India TV News (PTI)*, *Uruguay XXI*) and never re-initialises it from an Arabic gloss. 8 such hits exist today and all are legitimate. **A check that flagged them would train the team to ignore it** — which is worse than no check.
- **Allowlists with reasons, never silently.** `English version ↗` on an Arabic page is *correct*: a language switch is labelled in its target language, mirroring «النسخة العربية ↗» on the English page. It is exempted by name, with the reason in the source, and the exemption is scoped to elements that *declare* `lang="en"` — so correct markup earns the exemption and bare Latin text does not. (`lang="en" dir="ltr"` was added to that link in the same run; the English page had carried `lang="ar" dir="rtl"` on its counterpart since launch, and the asymmetry meant a screen reader on an Arabic page never switched voice.)
- **Refuses to pass on an empty run.** Zero chrome fields located = exit 2, not exit 0 (the 08-16 trap).

**The check was proved against the defect, not merely run.** Pre-fix build: **235 defects across 235 chrome fields**. Post-fix build: **CLEAN, 235 fields checked.** A new assertion that has never been shown to fail on the bug it was written for is not evidence of anything (#16, in its general form: verify in the judging environment, and verify that the verifier bites).

---

## The feed, same lens, second finding

Yesterday's forward question asked whether the feeds are readable by anything but us. Well-formedness is to a feed what "resolves" was to the og:image.

- **`<title>` is plain text by RSS 2.0 spec** — no markup, so no `dir`. The reader drops the string into a paragraph whose base direction is the reader's UI language, LTR for most subscribers. Under an LTR base, trailing punctuation and digit runs (**"12,348"**, **"2026"**) resolve to the **wrong side** of an Arabic string. **27 of our 38 Arabic deks mix Arabic with Latin or digits**, and not one character of direction metadata appeared anywhere in either feed. The only lever a markup-free field offers is a **U+200F RLM prefix**, which sets the paragraph base direction. Applied to every AR title and category.
- **`<description>` is HTML by universal convention**, so it takes real markup: wrapped in `<div dir="rtl" lang="ar">`. Stronger and more explicit than a control character; use markup where markup is available.
- **`<enclosure>` added to both feeds**, pointing at the raster share cards generated on 08-18 — so an item now carries its art into a reader. **Raster only**: the 08-18 rule (no consumer renders SVG) binds the feed exactly as it binds `og:image`, and the assertion checks both the extension and that the file exists on disk.

---

## Binding, and what it does not touch

- **Not retroactive to prose.** No shipped Arabic body text is reopened; this is a chrome and feed ruling.
- **The Verifier's checklist gains one question:** *does every field on this page that the site generated — not the writer — appear in the page's own language?* Two acceptable answers: it does, or it is a foreign-language string that declares its own `lang` and is exempted by name. **"The parity check passed" is not an acceptable answer**, and per the 08-16 trap, an Arabic surface that raises no language question has not been checked.
- **Generalises past Arabic.** If the publication ever adds a third language, the schema stays English and a second display map is added. The ruling is about the boundary, not about Arabic.

**Ruling series now #1–#33, no gaps, no dupes.**

---

*The 08-18 finding was that a link resolving is not an asset rendering. Today's is that a file existing is not a language being spoken. Both are the same question asked of a different layer: what does the consumer actually receive? That question has now found a 83-day defect and a 90-day defect on consecutive runs. It should be asked of every remaining surface — and the surfaces left are the sitemap, the `<head>` metadata, and the print stylesheet.*
