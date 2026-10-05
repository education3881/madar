# Publish gate — 2026-10-05

**Run in writing before the commit, per the CHARTER and the skill. This run publishes NOTHING: no
`approved` flag moved in either direction. The gate is run anyway, because the run edited editorial
content** (the held Arabic body of Edition 05 row 4) **and the rule is that the gate is the backstop,
not the first ruler.**

## What this commit does to the published corpus

**Nothing.** Stated by name rather than assumed:

| Check | Result |
|---|---|
| `approved: true` files added or changed | **none** |
| `approved: false` → `true` flips | **none** |
| Files changed under `web/src/content/articles/` (EN) | **none** |
| Files changed under `web/src/content/articles-ar/` (AR) | **one — `2026-09-14-africa-best-system-ruler.md`, which is HELD** |
| Files changed under `web/public/`, `design-assets/` | **none** |
| Held slugs in `dist` / sitemap | **zero** (asserted by `qa_held_assets`, green) |
| Live `lastmod` values moved by this tree | **zero** — 119 of 120 still `2026-09-28T11:56:49Z` in the built sitemap, verified post-build |

**The one content edit is to a held piece**, so it contributes no page, no sitemap entry, no feed item,
no `lastmod` and no bytes until the flip commit. The 09-06 held-file rule was re-tested against this
very edit and holds.

## The five gate items, for the record

1. **Editor verdict on file** — n/a, nothing ships. The Editor's pair verdict for row 4 remains on file
   from the banking run; **today's change is an Arabic Editor register judgment**, filed at
   `content-drafts/verdicts/2026-10-05-ed05-ruler-arabic-register-judgment.md`.
2. **Arabic verdict on file** — **yes, and it is the artefact of record for this change.** Both
   questions adjudicated with the grammar reasoning written out, the ruled fix stated, and the two
   declined alternatives recorded so the next composer does not re-litigate them.
3. **Hero still and share card on disk** — unchanged; all **twelve** held assets (6 stills, 6 og cards)
   present, none in a path the build can serve while held.
4. **`npm run build` clean** — **exit 0, three times** (baseline, after the tool change, after the
   content change). The third run is the one that counts: it is the exact tree being pushed.
5. **Assertions green** — **all 28**. Thirteen from `postbuild` inside the build; the twelve CI
   build-step assertions additionally run by hand, every one exit 0; the three non-gating ones run
   deliberately. Gate register **25 of 28**, derived by `qa_patch_queue` from its three homes.

## Content-change discipline on the one edited file

- **No numeral moved**, either direction, either language. Both edits are grammar and lexis.
- **No EN prose touched** — the English was correct at both sentences. A one-sided correction for the
  one reason that justifies one (the 10-03 precedent).
- **No `sources[]` annotation touched** — neither defect was in an annotation.
- **Arabic rendering re-checked after the edit:** `qa_arabic_shaping` CLEAN (310 Arabic-bearing
  elements, every one `letter-spacing: normal`), `qa_arabic_joining` CLEAN, `qa_ar_language` exit 0.
- **`qa_pair_frontmatter` green** — correctly, since the change is body prose. **Noted rather than
  celebrated:** this is the fourth consecutive day that gate has been rightly blind to a real defect,
  which is the substance of ruling #87 and not a reassurance.

## Tool change in the same commit

`agents/tools/qa_sources_alive.py` — the total ceiling (#88) and the IRI→URI fix (#80, second
instance). **It is one of the three assertions that do NOT gate the deploy**, so this change cannot red
the build; `--collect-only`, which *is* read by `qa_census`, was re-run and is unchanged at 684
citations / 343 URLs / 59 held / 88 files. Both changes proved both ways, with the bite proved before
the control in each case.

## Verdict

**GATE PASSED for a commit that publishes nothing.** Nothing with `approved: true` is added or altered;
no held asset is exposed; the build is clean; every assertion is green on the exact tree being pushed.

— Manager · 2026-10-05
