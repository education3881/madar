# Publish gate — 2026-09-14, run 2

Run in writing before staging the commit, per the standing rule. This run commits **editorial
content** (the Arabic side of slot 3), so the gate is not optional. The morning run's gate is at
`2026-09-14-publish-gate.md`; this supersedes nothing in it and adds the Arabic row.

**Nothing ships to readers today. No flag was flipped. The published corpus is byte-identical.**

## Gate 1 — editorial verdict and approval

| Piece | State | Verdicts on file | Flag |
|---|---|---|---|
| `2026-08-25-zambia-free-education-act` (EN+AR) | banked | Editor 08-27 PASS · Verifier 09-08 FAIL-1 fixed in-run | `approved: false` |
| `2026-08-28-sierra-leone-sleic-outcomes` (EN+AR) | banked | Editor 08-30 PASS · Verifier 09-09 FAIL-2 fixed in-run | `approved: false` |
| `2026-09-01-sudan-cant-wait-to-learn` (EN+AR) | banked | Editor 09-04 PASS · Verifier 09-10 FAIL-3 fixed in-run | `approved: false` |
| `2026-09-14-africa-best-system-ruler` (EN) | drafted 09-14 run 1 | — | `approved: false` |
| **`2026-09-14-africa-best-system-ruler` (AR)** | **composed today** | **Arabic Editor gate 09-14 PASS** | `approved: false` |

The Arabic gate is on file at `content-drafts/verdicts/2026-09-14-africa-best-system-ruler-ar-gate.md`.
**Still owed before this pair is banked:** the Editor's five-test **pair verdict**, then the
Verifier's verdict. Neither is claimed and neither is implied by today's PASS — the Arabic Editor
gates the Arabic composition, nothing more.

**Two EN-side corrections were made this run** and are recorded because they touch a piece that has
not yet had its pair verdict: the attribution verb on the TIMSS launch caution (`said` → the
register's `cautions`, with the applause it sits inside restored), and the Principal Investigator
named and titled in the `sources[]` annotation as served. Both are register restorations, not new
claims; no figure was added or removed. The numeral multiset was re-checked after the edits.

**Gate dependency, re-checked before composing the commit.** Unchanged from run 1 and still binding
four pieces: row 4's `related:` rail names rows 1, 2 and 3, all held; rows 2 and 3 rail into row 1
and each other. **The four flip atomically or `qa_body_links` (#10) fails the build on a dead end.**
The reciprocal edges *into* row 4 are still owed and must land in the same commit as the flip, not
after it. The Arabic file added today carries the identical `related:` rail, so the Arabic side
inherits exactly the same constraint.

## Gate 2 — assets on disk

- Hero still and share card for slot 3 were drawn in run 1 and are unchanged; the Arabic file
  points at the **same** still with Arabic alt text, which is house practice.
- `qa_held_assets` **CLEAN**: 8 assets withheld for 4 held pieces; every approved asset still served.

## Gate 3 — build and assertions

Full checkout, `CI=true`. `astro build` exit **0**, **120 pages**. Parity **38/38** approved.
Sitemap **120 URLs / 120 lastmod**, newest `2026-09-14T06:13:32Z` — held files contributed no date.
Both feeds 38 items. **Held-slug leak zero.**

**12 of 13 standing assertions gate the deploy and all 12 are green**, including `qa_css_tokens`,
which lands and is gated this run — from `web/package.json`, not from the workflow file. The thirteenth (`qa_live_drift`) is out by stated reason. Full
table and the four-way proof of the new assertion are in `agents/logs/qa-2026-09-14.md`.

## Gate 4 — Arabic full pass

- **Dek 145/200** code points (tashkeel +1 each), **title 58/100** — measured at compose and
  recorded in the hand-off, per the 2026-07-27 enforcement addendum, not discovered at the gate.
- **Numeral multiset EN↔AR: zero Arabic-only figures.** EN-only tokens are grade labels
  (*Grade 9/8/5* → ordinal words) and the caption's Curated number in Arabic-Indic digits — both
  established properties of the two languages.
- Five named humans: four confirmed, one restored and stated as a restoration. The nine-author
  TIMSS list is deliberately untransliterated, with the served Latin list retained beside the
  Arabic lead name.
- `qa_geo_fields` confirms the EN/AR twins declare the same `countries` set.
- `approved: false` on both sides; zero build leak verified above.

## Push note

The first attempt at this commit **did** touch `.github/workflows/astro-pages.yml`, to add the new
assertion beside the other eleven. **The push was rejected:**

    refusing to allow a GitHub App to create or update workflow
    `.github/workflows/astro-pages.yml` without `workflows` permission

This is a hard property of the Actions token and not something `permissions:` in the workflow can
grant itself. The workflow edit is reverted out of this commit and **the assertion is gated from
`web/package.json` instead** — `npm run build` is exactly what the deploy job runs, and npm runs
`postbuild` after `build`, so a failure there fails the build job and nothing deploys. Proved
through that entry point rather than by argument: `npm run build` **exit 0** on the real tree,
**exit 1** with today's defect reinjected at source, restored and green again.

This is not a weakened guard. It is gated in one respect *more* strongly than a workflow step,
because it also fails every local build. What it costs is legibility: `astro-pages.yml` is no
longer the complete list of gates, and that is worth fixing properly. Filed as a founder decision
(the fix needs a credential only he can add), with a stated default and date.

**Verdict: CLEAR TO COMMIT.** Nothing ships editorially; the corpus is unchanged; the build is clean
in the judging environment; the one behavioural change to the live site is the browse pages' accent
colour, which is a defect fix, is asserted, and was proved both ways before landing.

— Manager · 2026-09-14 (run 2)
