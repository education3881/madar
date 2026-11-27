# Publish gate, in writing — `2026-11-26-qatar-pisa-2025-two-of-three`

**Run** 2026-11-27 (daily) · **Edition 06, piece 4** · **Cell 8 of eight** · Written **before** the flip was
committed, which is the whole point of writing it.

| Gate item | State |
|---|---|
| Editor's five-test verdict on file | **PASS**, eight repairs required and closed in-run — `content-drafts/verdicts/2026-11-27-qatar-pisa-2025-two-of-three.md` |
| Arabic Editor's gate on file | **APPROVED**, one substitution caught in both editions — `content-drafts/verdicts/ar/2026-11-27-qatar-pisa-2025-two-of-three-arabic-gate.md` |
| Verifier's verdict on file (#27, drafter ≠ verifier) | **VERIFIED**, no correction required, 15 of 15 traced and **zero residue** — `content-drafts/verdicts/2026-11-27-qatar-pisa-2025-two-of-three-verification.md` |
| Hero still on disk | `web/public/stills/2026-11-26-qatar-pisa-2025-two-of-three.svg` — pure line, one orange accent, two trios on one ruler |
| Share card on disk, and **looked at** (2026-08-18 clause 4) | `web/public/og/2026-11-26-qatar-pisa-2025-two-of-three.png`, 1200×600, **1,556 bytes**. Rendered and inspected in this run; the first draft was redrawn because the composition sat in the middle third of the frame and read small at raster size |
| `npm run build` | **exit 0**. The 28 `postbuild` assertions green, and `build_job_gates` parsed the **12** build-job gates out of `astro-pages.yml` and ran them green against this tree's `dist` — so the local gate set is the deploy's gate set, **40 of 43**, rather than two-thirds of it. Red three times first, each failure named below |
| EN + AR both `approved: true` | yes, in **one commit with their assets** (the 2026-06-14 rule) |
| Held-slug leak | **zero** — and the corpus now holds **no held piece at all**, so this assertion is in its vacuous mode and the 2026-08-09 inversion applies: the positive checks were run instead |
| Positive checks (the inverted sweep) | both routes built (`dist/articles/…` and `dist/ar/articles/…`), the slug is in the sitemap, the hero still resolves in the built HTML |
| Forward rails (the rail step, 2026-11-12) | **added in this same commit**, both editions, into `2026-11-26-pisa-2025-three-lists-of-risers` (now 5 rails) and `2026-05-31-qatar-humanity-spark-strategy` (now 4), both under the cap of 6 |
| Dek / title caps | EN 196/200 and 34/100 · AR 168/200 and 26/100, code points, tashkeel +1 |
| Credentials, tokens, keys | none, in any file touched |

## The three red builds, named rather than summarised

A green build that was green on the first try would be worth one line. This one was red three times, each
time on a different gate, and each gate caught something a human reading would not have.

1. **`qa_annotation_figures`, on the Thailand repair.** Correcting a served annotation introduced two new
   annotation-only quantities per edition — `1,634,885` and `51`. The gate refused the build until each had
   a hand-written provenance. **The repair for a published figure was itself a published figure.**
2. **`qa_register_shape`, twice.** First on the two guidebook rows filed for ruling #161, which carried
   three cells against a four-column header; then on the ledger update, whose multi-paragraph prose wrapped
   a table row and would have terminated the table. Neither would have moved a number, which is exactly why
   it is a gate and not a habit.
3. **`qa_pair_frontmatter`, on the flip itself.** The pair's self-citation points at the EN page from the
   EN edition and the AR page from the AR edition, which the gate reads as two different registers and
   refuses until a human declares why. **It is also the gate that made this run settle a house rule**: its
   own Thailand entry says in writing that the corpus holds two rival conventions for self-citation and
   *"only one can be the house rule."* Settled here — **a self-citation is cited per language** — with the
   one older pair that does it the other way left as it shipped and the step recorded, because a convention
   settled today fixes the future and does not reconcile backward.

Plus **`qa_prior_publication`** limb 5, which refused to let the daily run build before observing the
previous publication. It observed: deploy **45934798669**, conclusion **success**, head `4aeae58a`, **strand
0 — the origin is serving the tip.**

## Disposition

**CLEARED TO SHIP.** Edition 06 goes to **4 of 6** with ten days of its window left, and the directive's
floor of one piece a day was already met this morning by `2026-11-27-thailand-pisa-2025-fourth-list`, so
this is the second piece served today and the first time this publication has shipped two on a day that was
not its edition's opening day.
