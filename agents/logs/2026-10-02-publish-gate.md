# Publish gate in writing — 2026-10-02

**Scope of the editorial change in this run:** `sources[]` annotations on Edition 05 row 2
(`2026-08-28-sierra-leone-sleic-outcomes`), **both languages**. **No flag flipped. No piece ships. The
wave stays held.** This gate is run because the run touched editorial content, per the standing rule that
the gate precedes any editorial commit — not because anything is being published.

---

## The gate

| Item | Status |
|---|---|
| **Editor verdict on file** | Pair verdict `verdicts/2026-08-30-ed05-sierra-leone-pair-verdict.md` — **PASS**, unchanged. Today's edits do not touch the frame, the argument or any body sentence, so the pair verdict is not reopened. |
| **Arabic verdict on file** | `verdicts/2026-08-29-sierra-leone-sleic-outcomes-ar-gate.md` — **PASS**, unchanged. The Arabic edit is a `sources[]` annotation composed in Arabic, mirroring the English in substance, with no body prose and no numeral touched. |
| **Verifier verdict on file** | `verdicts/2026-09-09-sierra-leone-sleic-outcomes-verification.md` — FAIL-2, both fixed in-run 09-09, **and the confirmation read filed today** (`verdicts/2026-10-02-ed05-sierra-leone-confirmation-read.md`) re-confirms both against living registers and disposes the third owed item. |
| **Hero still on disk** | `web/public/stills/2026-08-28-sierra-leone-sleic-outcomes.svg` — present, committed, unchanged. |
| **Share card on disk** | `web/public/og/2026-08-28-sierra-leone-sleic-outcomes.png` — present, raster, unchanged. |
| **`astro build` clean** | `npm run build` → **exit 0**, 121 pages. |
| **Assertions green** | **25 of 28 gating, all CLEAN.** `qa_pair_frontmatter` CLEAN at **684 source URLs** across 44 pairs — the number that proves today's URL correction landed in **both** languages; had it landed in one, this gate would have failed. |
| **Held-slug leak zero** | `qa_held_assets` — **held slugs in dist and sitemap = 0**; held set 6 slugs / 12 files; approved 38. |

## Word and numeral discipline

| | EN | AR |
|---|---|---|
| Body words before | 1,592 | 1,343 |
| Body words after | **1,592** | **1,343** |
| Body numerals moved | **none** | **none** |

**No body prose was edited in either language.** Every change is inside `sources[]`. No waiver sought
and none needed.

## What changed, precisely

1. **Entry 8 (the analysis repository), both languages** — the attribution corrected from *Save the
   Children UK* as publisher to the named author on his own account, quoting the README's own
   self-description; the rename and the permanent redirect recorded; the URL moved to the living address
   (#41). **Ruling #84.**
2. **Entry 2 (the EOF programme register), both languages** — a second read date added (2 October 2026)
   with the served spelling confirmed unchanged, and the reason that second date exists stated: a
   separate typo on the same page has since been corrected, so the register is maintained and the
   quotation is a dated reading rather than a property of the page (#80).

## Verdict

**PASS for commit.** Nothing is published by this commit; the wave remains held and every held-piece
invariant holds. The two annotations are more accurate than they were this morning and the pair agrees
with itself in both languages, proved by the gate rather than asserted.

— Manager · 2026-10-02
