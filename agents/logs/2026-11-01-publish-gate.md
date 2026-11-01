# Publish gate — 2026-11-01

**Written out a row per piece although no `approved` flag moved**, because a correction or addition to a
published body is editorial work and goes through the gate exactly like a flip (standing practice since
2026-10-31).

## What changed in the served corpus

| Piece | Edition | Change | Gate |
|---|---|---|---|
| `2026-07-07-turkiye-earthquake-school-recovery` | EN | annotation extended with the figures MEB's own 25 January 2024 register actually prints (119,200 pre-quake, 22,039 new classrooms targeted, 129,120 total, 8.3%) plus that register's publication date, which it had never carried; body gains the finding that the finish line itself moved, 129,120 → a projected 137,505, up 8,385 | PASS |
| `2026-07-07-turkiye-earthquake-school-recovery` | AR | same, **composed** not translated, written with the register open per 09-13 | PASS |
| `ar/editions/index.html` | AR | a standing-pieces section, giving the Arabic edition its first path to `/madar/valence/` | PASS |
| `editions/index.html` | EN | unchanged | PASS |

**No piece's `approved` flag moved. Zero held pieces on disk** (`madar:withhold-held-assets` — *no held
pieces; nothing withheld*), so the held-slug leak check is in its all-approved mode per the 2026-08-09
inversion rule: `approved: false` count in the build path = 0, and `qa_held_assets` confirms every approved
asset is served.

## The gate, row by row

- **Editor / Arabic verdicts on file:** unchanged — no new piece, no flag change. The Türkiye pair's
  verdicts stand; today's work is an addition to a published body under the same frame, and the standing
  prohibitions carried from Edition 05's commissions apply unchanged (announced ≠ measured, labelled at the
  figure).
- **A figure is cited as read:** every figure added today was read in served text on 2026-11-01 from
  `meb.gov.tr/.../haber/32430/tr`, which the piece has cited since it shipped. **Nothing was carried from a
  search summary** — a search result did assert a *minimum fifteen percent* target and it is **not** in the
  piece, because no register this run could open states it; what the result lists carried was reported
  speech from a podium, and #43 settles that (*the podium is not the document*).
- **Units labelled at the figure:** the body now names all three units in one clause — two regional
  aggregates (129,120 and 137,505), one per-province floor (ten percent), one ministerial average
  (sixteen percent) — so the unit confusion that produced item 61 cannot be repeated by the next reader.
- **No unattributed editorial future (#117):** every projection added carries the dated register that
  announced it.
- **Caps counted at compose (07-27):** deks and titles untouched — EN dek **181/200**, AR dek **158/200**,
  titles **39/100** and **31/100**, code points, tashkeel +1 each.
- **Acronyms (#101):** none added. `MEB` remains expanded in `sources[]` in both editions.
- **Named humans (#86):** none added, so no gender determination was made.
- **Hero still and share card:** on disk and unchanged; `qa_consumer_surface` green (og:image raster + alt).
- **`astro build` clean:** exit 0. **All 41 assertions green**, 38 gating, derived 41 / 12 / 26 / 38 of 41.
- **Held-slug leak:** zero, and in the correct mode for an all-approved corpus.
- **Arabic composition gates:** `qa_arabic_shaping` 378 Arabic-bearing elements all at `letter-spacing:
  normal`; `qa_arabic_joining` 12 runs all shaped; `qa_ar_language` clean; `qa_a11y_lang` clean, which is
  the gate that licenses the one Latin-script string placed on an Arabic page today — it is marked
  `lang="en" dir="ltr"` and the Arabic reader is told in Arabic what they are clicking into.
- **Pair parity:** `qa_pair_frontmatter` clean. Parity is a floor, never a verdict (#86).
- **Re-verifiability:** `qa_claim_registers` — all 353 cited registers hold a dated observation.
  `qa_citation_identity` — all 231 quotation-bearing registers hold a dated reading. No new register
  entered the corpus today, so neither needed a new row.

## Rendered and looked at before the push

The Arabic editions index was rendered in a browser and **measured**, not merely built — and the inspection
found two real typographic defects no gate could catch (Arabic set in a Latin serif, Latin set in an Arabic
face, in one block). Both repaired, then re-rendered and re-measured. The daily brief was likewise rendered
and inspected per the 08-23 rule, container wrapper intact.

**Verdict: PASS.** Nothing editorial is staged unpushed; each function committed and pushed at its own
close per #96.
