# Publish gate — 2026-10-03

**What is being committed editorially:** `sources[]` corrections and one three-word body correction on
**Edition 05 row 3** (`2026-09-01-sudan-cant-wait-to-learn`, EN + AR), arising from the pair's
**confirmation read** (`content-drafts/verdicts/2026-10-03-ed05-sudan-confirmation-read.md`).

**No flag is flipped. Nothing is published.** The wave stays held; the publication's served bytes are
unchanged by this commit except for the brief and logs, which are not in `dist`.

---

## The gate, item by item

| Gate item | State |
|---|---|
| Editor pair verdict on file | **YES** — `verdicts/2026-09-04-ed05-sudan-pair-verdict.md`, PASS |
| Arabic Editor gate on file | **YES** — `verdicts/2026-09-03-sudan-cant-wait-to-learn-ar-gate.md`, PASS |
| Verifier verdict on file | **YES** — `verdicts/2026-09-10-sudan-cant-wait-to-learn-verification.md`, FAIL-3 → all closed in-run |
| **Confirmation read on file** | **YES — closed today**, third of the five owed at the gate |
| Hero still on disk | **YES** — `web/public/stills/2026-09-01-sudan-cant-wait-to-learn.svg` |
| Share card (og) on disk | **YES** — `web/public/og/2026-09-01-sudan-cant-wait-to-learn.png` |
| `npm run build` clean | **YES — exit 0**, 121 pages, 120 sitemap URLs |
| All gating assertions green | **YES — 25 of 28**, counted in both homes by `qa_patch_queue`, not read off prose |
| The twelve CI build-step assertions, run by hand | **YES — every one exit 0** |
| **Held-slug leak** | **ZERO** — `qa_held_assets`: 6 held slugs, 38 approved, 76 control assets, *"no held piece contributes bytes"* |
| Caps at compose | EN **1,866** / ≤2,300 · AR **1,607** / ≤2,300 — **no waiver**; title and dek untouched |
| Numeral multiset, both bodies | **37/37 symmetric**, zero one-sided figures in either direction, re-measured after every edit |
| Cross-language source URL set | **symmetric** — `qa_pair_frontmatter` CLEAN at 684 source URLs; the moved War Child address changed in **both** languages, which is what this gate proves |

## What changed, exactly

- **English body, three words:** *"the National Council for Literacy"* → *"the National Council for
  Literacy **and Adult Education**"* — the owner's own name for it. **Arabic was already correct and is
  not touched.** No numeral involved, so the multiset is unmoved.
- **`sources[]`, both languages:** the War Child handover URL moved to its living address
  (`/news/` → `/latest/article/`, a one-hop redirect) and its annotation gained the register's own date
  (18 May 2026), today's read date and an independent second channel (Bond, 9 Sep 2026, quoted).
- **`sources[]`, both languages:** Brown et al. gains its second channel (RePEc/IDEAS, verbatim) and the
  publisher's 403 recorded as *walled, not dead*.
- **`sources[]`, both languages:** the War Child Annual Report annotation now states plainly that its
  figures stand on **one channel attested on two dates**, with the second channel attempted and named as
  not carrying them.
- **`sources[]`, English:** the facilitator register's annotation gains the owner's verbatim sentence and
  the read date. **Arabic:** gains the cross-edition attestation.

## Assertion-side changes in the same commit, and why they are not editorial

`agents/tools/qa_sources_alive.py` (parser fixed, `--collect-only` added) and
`agents/tools/qa_census.py` (fifteenth instrument) — **ruling #85**. Neither changes a served byte.
Proved both ways with the injection asserted to have landed and the tree restored byte-identical;
`qa_census` is a gating assertion and the full build was re-run after the change, **exit 0**.

## Not done, deliberately

- **The flip rehearsal is NOT re-run in this commit.** It is owed *in the run that composes the flip
  commit*, and this is not that run. **It is now stale by three content files** (10-02 touched two, today
  touched two more), and that is recorded rather than quietly carried.
- **No twenty-ninth assertion.** Eight days from the gate, the day already changes a gating tool.

**Gate verdict: PASS for what is being committed — which is a correction to a held pair, not a
publication.**

— Manager, on the Editor's and Verifier's verdicts · 2026-10-03
