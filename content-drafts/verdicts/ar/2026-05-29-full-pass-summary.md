# Arabic Editor — Full-pass review, 2026-05-29

## Scope

All seven Arabic-language articles on the live site, plus the AR-side site chrome (homepage, about, masthead, footer). This is the Arabic Editor's first comprehensive pass since the persona was added today.

## Coverage and outcomes

| # | Piece | First-pass status | Today's full-pass outcome |
|---|---|---|---|
| 1 | Bo (Sierra Leone) | not previously reviewed | **approved after correction** — name transliteration fixed (6 instances) |
| 2 | Bahrain BQA | not previously reviewed | **approved, no edits** — cleanest of the four newly-reviewed |
| 3 | Egypt EKB | not previously reviewed | **approved with source-verification flag** — Shawki 2015 quote may be back-translation; flag carried forward |
| 4 | UAE Madrasa × TikTok | not previously reviewed | **approved after correction** — "Kinda Ibrahim" transliterated (3 instances) |
| 5 | Kuwait CCET | approved this morning | re-read; verdict stands; one style note ("البنية الإقليمية") carried forward unchanged |
| 6 | Iraq Mosul Library | approved this morning | re-read; verdict stands; one style note ("يَقوم بِالعمل الأثقل") carried forward unchanged |
| 7 | Ghana CBE | approved this morning | re-read; verdict stands; no additional notes |

## Corrections applied to disk (queued for next push)

**Bo — `2026-05-25-bo-teacher-chalk.md`** — 6 in-body replacements:
- `هَوَى` → `حَوَا` (the anonymised teacher's name, restored from the abstract noun "passion" to the Krio/Arabic-origin personal name Hawa, contemporary short form of حَوَّاء)

**UAE Madrasa — `2026-05-27-uae-madrasa-tiktok.md`** — 3 replacements (body and source block):
- `Kinda Ibrahim` → `كندة إبراهيم` (transliteration of the TikTok regional executive's name, for consistency with how the other named humans in the same paragraphs are rendered)

## Pieces approved without edit

Bahrain, Egypt, Kuwait, Iraq, Ghana — verdicts on file in this directory. Source apparatus, named-quote handling, register fit, and dignity check all hold.

## Carried-forward style notes (not edited, for future drafts)

- **Bo** — none beyond the name correction
- **Bahrain** — none
- **Egypt** — verify originating language of all historical quotes before next Egypt piece
- **UAE Madrasa** — colloquial idiom "إيقاع" → "تَصَيُّد" preferred in fusha-analytic register
- **Kuwait** — "البنية الإقليمية لِأداء هذا العمل" → "البنية الإقليمية القادرة على القيام بِهذا العمل"
- **Iraq** — "يَقوم بِالعمل الأثقل" → "يَحمل ثِقَل المعنى"
- **Ghana** — none

These are not corrections. They are notes for the Content Creator's future Arabic drafting — the kinds of sentences a careful Arabic editor would re-touch on the next pass through similar material.

## Site-chrome review

**AR homepage (`web/src/pages/ar/index.astro`)**

- Masthead tagline "التعليم، بتأنٍّ، بلغتين" — approved, clean fusha.
- Section kicker "الأحدث" — approved.
- About-mini body "نكتبُ من مدارٍ واحدٍ بلغتَين، ولكلٍّ منهما وزنُها الخاصّ" — approved. Holds the brand.
- **Defunct placeholder text** (lines 95–103, only renders when the AR collection is empty) — the AR collection is now populated with 7 pieces, so the conditional never triggers. The placeholder text ("لم يصدر بعد عددٌ عربيٌّ مكتمل...") is dead code now and could be removed in the next Web Developer cleanup. Not urgent; the live site is not affected because the conditional is correctly gated.

**About page (`web/src/pages/about.astro`)**

- The two Arabic strings on the page ("حول مدار" and "نكتب من مدار واحد بلغتين، ولكلٍ منهما وزنها الخاص") — approved.
- **Structural gap noted, not for today.** The body of the About page is in English only. For a bilingual publication, the About is the canonical statement of what the publication is, and an Arabic-reading subscriber arriving via the AR homepage does not see a full Arabic articulation of the publication's identity. This is a real but non-urgent structural gap. The fix is a full AR About body, written by the Content Creator under an Arabic Editor brief, ideally as an Arabic-original (not a translation of the EN). Flagged as a quiet idea for the editorial calendar in June.

**Site footer and masthead chrome (`SiteHeader.astro`, `SiteFooter.astro`)** — reviewed for Arabic strings; nothing requiring an Arabic Editor verdict at this pass.

## Aggregate read on the AR side of the publication

Seven pieces live, all now reviewed against the five-test rubric. Two real corrections applied (the Bo name; the UAE name). Five pieces stand without edit. One source-verification flag carried forward (Egypt). One structural gap noted (full AR About body).

The Arabic side of Madār reads, on this slow pass, as a publication — not as a courtesy translation. The fusha holds the publication's voice in a register that matches the head Editor's English-language work. The corrections applied today are not defects in the writing; they are the kind of detail-level work that the Arabic Editor's existence is designed to absorb, so the head Editor and the Content Creator are not single-handedly carrying both languages.

The publish-gate posture changes. From the next push forward, no piece ships in Arabic without an Arabic Editor verdict on file. Today's full-pass closes the inherited gap on the seven pieces shipped before the persona existed.

— *الْمُحَرِّر العربي · 2026-05-29*
