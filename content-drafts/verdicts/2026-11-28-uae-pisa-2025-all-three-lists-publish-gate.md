# Publish gate: `2026-11-26-uae-pisa-2025-all-three-lists`

**Run in writing by the content run of 2026-11-28, Asia/Dubai. RESULT: PASS — the piece ships.**
Edition 06's **fifth** piece. The eighth cell closes here.

## RUNBOOK rule 3, clause by clause

**(a) Editorial verdicts on file, and the article is `approved: true` in both editions.**
Editor's five-test verdict `content-drafts/verdicts/2026-11-27-uae-pisa-2025-all-three-lists.md` — PASS.
Arabic Editor's gate `content-drafts/verdicts/ar/2026-11-26-uae-pisa-2025-all-three-lists-arabic-gate.md`
— APPROVED, five corrections applied at the gate. Verifier's verdict
`content-drafts/verdicts/2026-11-28-uae-pisa-2025-all-three-lists-verification.md` — **VERIFIED**, five
corrections required and all five applied in-run, re-checked after application. Flags flipped to
`approved: true` in `web/src/content/articles/` and `web/src/content/articles-ar/` in this commit.

**(b) Designer hero still exists and is committed.** `web/public/stills/2026-11-26-uae-pisa-2025-all-three-lists.svg`,
2,653 bytes, on origin since cell 7 on 2026-11-27. Raster share card
`web/public/og/2026-11-26-uae-pisa-2025-all-three-lists.png`, a valid PNG at 1200×600, 854 bytes —
checked as a raster and not merely as a path, which is the 2026-08-18 rule.

**(c) Clean build and QA spot-check.** `npm run build` exit **0** with the piece approved. All **40**
gating assertions green — the twenty-eight from `postbuild` and the twelve build-job steps, the latter run
through `build_job_gates` so the local gate set is the deploy's gate set rather than two-thirds of it.

## The two gates the flip itself turned red, and why that is the system working

Neither was a defect in the piece. Both are gates that **cannot see a held piece at all**, so a flip is the
first moment they are asked anything — which is the 2026-08-09 inversion rule arriving from the other
direction: an assertion scoped to a corpus state has to be re-derived when the state changes, and here two
assertions acquired a subject they had never had.

1. **`qa_claim_registers --check` failed** on one cited register with no row: `https://moe.gov.ae/en/pages/home.aspx`.
   This is the gate behaving exactly as its header promises — *a citation nobody has ever asked an archive
   about fails the build instead of narrowing the measurement in silence.* Cleared by running the network
   `--emit` half, which asked 40 registers within its budget and returned this one **archived, snapshot
   2026-11-10, status 200**. So the one door this piece reports as answering-but-silent is itself
   re-verifiable, which is worth having on the record for a piece whose closing section is about that door.
2. **`qa_annotation_figures` failed** on 40 annotation quantities across the two editions, 17 distinct
   tokens. Every one is provenance rather than education: four decompressed byte counts, seven
   capture-timestamp fields, one HTTP status, two ruling numbers, and three comma-joined table rows that
   **are** printed in both bodies but in the true-minus form where the annotation uses an ASCII hyphen.
   Cleared the way #114 requires — by hand, because `--emit` deliberately writes nothing — with 17 rows
   written into `agents/stats/annotation-figures.json`, each naming where the figure was read from. The
   four byte counts carry their re-measured sha256 from this morning's independent re-fetch, so these rows
   record a confirmed measurement rather than a reported one.

## The post-flip assertions, which the held-mode sweep could not run (2026-08-09)

| Assertion | Result |
|---|---|
| `approved: false` for this slug anywhere in the build path | **0** |
| Both editions' pages built | `dist/articles/…` and `dist/ar/articles/…` both present |
| Both URLs in the sitemap, with reciprocal hreflang | **present**, `en` ↔ `ar` both ways |
| Hero still referenced in built article HTML | **1 each**, both editions |
| OG raster referenced in built article HTML | **1 each**, both editions |
| Assets now **served** rather than withheld | both in `dist/`; the build's withhold step named only Saudi |
| Both feeds carry the item | `rss.xml` and `ar/rss.xml` |
| Rails | 4 declared, all resolving in both collections, all to `approved: true` pieces |

## The rail step at cell 8, derived and not read (the 2026-11-27 amendment)

The amendment is binding from yesterday: **at cell 8 the forward edges are derived from the piece's OWN
FINAL `related:`, not from cell 1's list**, because under the founder directive something ships every day
and a piece commissioned on 11-26 is flipping against a board that moved twice underneath it. Derived here
rather than read, and the derivation is why Qatar gets its edge: Qatar was commissioned before this piece
existed and cell 1 could not have named it.

Four slugs in the final `related:`, so four reciprocal edges, written into **both** collections in this
same commit — eight file edits — each checked against the proven cap of 6 rails per piece:

| Older piece | Rails before | After | Cap |
|---|---|---|---|
| `2026-11-26-pisa-2025-three-lists-of-risers` | 5 | **6** | at cap |
| `2026-11-26-qatar-pisa-2025-two-of-three` | 4 | **5** | under |
| `2026-05-27-uae-madrasa-tiktok` | 2 | **3** | under |
| `2026-06-10-rak-iqra-arabic-diglossia` | 5 | **6** | at cap |

All four fit. Two land exactly on the cap, which is worth noting rather than passing over: the next Ed06
piece that wants to point at the edition's opener or at the Iqra piece **cannot be given a reciprocal edge
without displacing one**, and the amendment gives no displacement rule. Handed forward as a question rather
than answered here, because answering it inside a flip commit would be a rail policy invented at the one
moment nobody can review it.

## What ships

**"The UAE is on every list but one line"** · `2026-11-26-uae-pisa-2025-all-three-lists` · EN 1,806 words,
dek 193/200 · AR **«الإمارات على كلّ قائمة إلّا خطًّا واحدًا»** 1,422 words, dek 171/200 · `edition: 6` ·
four OECD registers, each read in two independent captures. Both titles carry the exception in the
headline itself and both deks scope the claim to improver lists, which is why correction 4 moved a body
sentence and left the title and dek alone · 23 of 23 English quoted spans and 29 of 29
Arabic Latin-bearing spans verbatim against served bytes.

Ed06 goes to **5 of 6** against a floor of six and a target of seven, on day 3 of the window, with the
directive's one-a-day floor met on every day the edition has existed.
