# Publish gate — 2026-10-28

**What is being published:** no new piece and **no flag change.** Five served pieces were edited — four as
the repair of standing-queue item 33 (citation identity) and one as the dated follow-up of item 42c — plus
one static page under `web/public/`. Every one of the five is already `approved: true` and has been since
its original ship date; the corpus has been all-approved since the 2026-10-13 flip.

**Why the gate still runs in writing.** The skill requires it *before committing anything editorial*, and a
correction to a published body is editorial. The 2026-08-09 inversion applies: the held-leak assertion is
`approved: false` count in the build path **= 0**, and the positive checks run in its place.

## Row per piece

| Slug | Editions touched | What changed | Editor | Arabic gate | Verifier | Still + og card | Register re-read |
|---|---|---|---|---|---|---|---|
| `2026-05-28-iraq-mosul-library` | EN + AR | annotation and body: UNESCO project title restored to *Restoring and modernizing the Mosul University Library* | on file (original ship) — correction approved under #101 cl. 4 | AR annotation and body recomposed as «استعادة وتحديث مكتبة جامعة الموصل»; no named human touched, so no #86 determination arises | on file; the change is a correction to a quoted title, inside the Verifier's quotation axis (#46) | unchanged | `core.unesco.org` 2026-03-27 snapshot read, then `confirmed` by the instrument's own client 2026-10-28 |
| `2026-07-07-us-naep-honesty-gap` | EN only | annotation headline restored to the register's own, inner single quotation marks included; outer delimiter switched to the escaped-double convention because the register's headline itself contains single quotes | on file | **no AR change and that is correct** — the Arabic annotation never quoted the headline, only the inner phrase «الصدق والشفافية», which the register does print | on file | unchanged | `oklahomavoice.com` 2026-09-09 snapshot read; `confirmed` 2026-10-28 |
| `2026-06-17-korea-aidt-reversal` | EN + AR | four annotation headlines corrected, one URL corrected to the article, and the money paragraph rewritten to give each figure its own register, hedge and scope | on file; the figure re-attribution is a correction of record, written in each register's own words | all four AR annotation renderings recomposed from the corrected headlines; AR body paragraph recomposed, not translated | on file; the re-attribution is traced against three registers in served text today | unchanged | Korea Herald (live + 2025-08-04 + 2025-08-26 snapshots), Korea Times, Rest of World, World Bank article — all read in served text 2026-10-28 |
| `2026-06-25-brazil-crianca-alfabetizada` | **neither** | **no byte changed.** The register serves its whole page today and the quotation is `found`; the 10-22 soft-200 was a transient | n/a | n/a | n/a | unchanged | `agenciabrasil.ebc.com.br` `confirmed` 2026-10-28 |
| `2026-07-16-australia-naplan-reset` | EN + AR | one annotation added (ACARA's 5 August 2026 release) and the closing paragraph extended with the dated follow-up | on file; a dated follow-up, never a rewrite (#41) | AR annotation and two AR paragraphs composed, not translated | on file; all nine figures traced to the release read this morning, and the two not printed in a body are registered with their clause | unchanged | ACARA release read by extracting text from the served PDF; the limit of that read is stated in the annotation itself |
| `web/public/valence/index.html` | n/a (static) | whitespace between three `display: block` spans inside the `<h1>`, so the served text reads `The Elements of good Education` | n/a — not an article | n/a | n/a | n/a | n/a |

## The checks

| Gate | Result |
|---|---|
| `npm run build` | **exit 0** (eighth build of the run; the first seven were red or intermediate by design and are named in the QA log) |
| Twenty-four postbuild assertions | **all green** |
| `npm run gates` → twelve build-job assertions | **CLEAN** — the local gate set is the deploy's gate set |
| `qa_pair_frontmatter` | green — reads source files, held pieces included |
| `qa_register_shape` | CLEAN — all four homes of the ruling range agree with §3's own rows at #1–#119 |
| `qa_annotation_figures` | green after registering three quantities on the new ACARA annotation; it bit on this run's own work and was right |
| `qa_claim_registers` / `qa_citation_identity` | green after `--emit` asked the new register; both bit on this run's own work and were right |
| `qa_patch_queue` | green — 39 tools, 24 postbuild entries, 36 of 39 gating, all derived |
| Held-slug leak | **zero** — and the assertion in force is the post-flip inverse |
| EN/AR parity | 44 pairs, 88 files, 100% |
| `qa_artefact_render` | 137 founder-facing artefacts render at 1280px with nothing overflowing |

## Dek and title caps

**No `dek` or `title` was touched on any of the five pieces**, so the 200/100 code-point caps are not in
play and no count line is owed (07-27). The annotation `title:` fields that changed are `sources[]` entries,
which carry no cap.

## Quoted headlines — the new hand-off line, applied to this run

Ruling #119 clause 5 adds `quoted headlines: N, each read from the page's own heading: ☐` to the Editor
hand-off. Applied here, retroactively to the pieces this run touched:

**quoted headlines: 6, each read from the page's own heading: ☑ (5 of 6) · ☒ (1 of 6).** The exception is
the Korea Herald entry, whose page carries a `<title>` and no `<h1>` at all in the markup this runner
receives; its heading was taken from the `<title>`, which is the only form that document serves, and the
annotation does not claim otherwise. **Rest of World's entry names its own disagreement in the annotation
text**, because that page serves two headlines and a reader is owed the fact rather than our choice.

## Verdict

**CLEARED.** Five pieces corrected, one static page corrected, nothing flipped, nothing held, no flag
moved, and every correction written in its register's own words as #101 clause 4 and #119 limb 3 require.
