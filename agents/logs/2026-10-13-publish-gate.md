# PUBLISH GATE — Edition 05 (AFRICA), the wave flip

**Date:** 2026-10-13 (Asia/Dubai) · **Run:** autonomous daily · **Gate taken by:** the Manager, after
every departmental verdict below was already on file.

This is the gate the RUNBOOK requires in writing before any editorial commit. It is written **in the
flip commit itself**, which is what the 2026-10-10 rehearsal entry said it was owed in.

**What flips:** twelve content files, six slugs, both editions, `approved: false → approved: true`.
Nothing else about any piece changes in this commit.

---

## 1 · The wave gate, row by row — every artefact named and located

The operational gate is **Editor pair verdict + Verifier verdict + Arabic gate + still + og card +
publish gate in writing → the Manager flips.** The founder owns the edition's scope, never its
approvals; scope was set at six on 2026-09-13 by a stated default that expired in silence.

| # | Slug | Editor pair verdict | Arabic gate | Verifier verdict | Confirmation read | Still | og card |
|---|---|---|---|---|---|---|---|
| 1 | `2026-08-25-zambia-free-education-act` | `verdicts/2026-08-27-ed05-zambia-pair-verdict.md` | **§5 of that same file** (composed before the standalone-gate convention; located here so nobody hunts a file that was never written) | `verdicts/2026-09-08-zambia-free-education-act-verification.md` | `verdicts/2026-10-01-ed05-zambia-confirmation-read.md` | ✓ | ✓ |
| 2 | `2026-08-28-sierra-leone-sleic-outcomes` | `verdicts/2026-08-30-ed05-sierra-leone-pair-verdict.md` | `verdicts/2026-08-29-sierra-leone-sleic-outcomes-ar-gate.md` | `verdicts/2026-09-09-sierra-leone-sleic-outcomes-verification.md` | `verdicts/2026-10-02-ed05-sierra-leone-confirmation-read.md` | ✓ | ✓ |
| 3 | `2026-09-01-sudan-cant-wait-to-learn` | `verdicts/2026-09-04-ed05-sudan-pair-verdict.md` | `verdicts/2026-09-03-sudan-cant-wait-to-learn-ar-gate.md` | `verdicts/2026-09-10-sudan-cant-wait-to-learn-verification.md` | `verdicts/2026-10-03-ed05-sudan-confirmation-read.md` | ✓ | ✓ |
| 4 | `2026-09-14-africa-best-system-ruler` | `verdicts/2026-09-15-ed05-best-system-pair-verdict.md` | `verdicts/2026-09-14-africa-best-system-ruler-ar-gate.md` (+ addendum, §2 of the same file) | `verdicts/2026-09-17-africa-best-system-ruler-verification.md` | `verdicts/2026-10-07-ed05-ruler-confirmation-read.md` | ✓ | ✓ |
| 5 | `2026-09-19-egypt-baccalaureate-published-first` | `verdicts/2026-09-22-ed05-egypt-pair-verdict.md` | `verdicts/2026-09-21-egypt-baccalaureate-published-first-ar-gate.md` | `verdicts/2026-09-23-egypt-baccalaureate-published-first-verification.md` | `verdicts/2026-10-08-ed05-egypt-confirmation-read.md` | ✓ | ✓ |
| 6 | `2026-09-27-rwanda-teacher-certification` | `verdicts/2026-09-29-ed05-rwanda-pair-verdict.md` | `verdicts/2026-09-28-rwanda-teacher-certification-ar-gate.md` | `verdicts/2026-09-30-rwanda-teacher-certification-verification.md` | none owed — all six verification items closed in-run | ✓ | ✓ |

**Five confirmation reads ran and five of five found something** after every prior gate had cleared
the pair (Zambia 2, Sierra Leone 1, Sudan 2, ruler 1, Egypt 1 — seven defects on five pairs). That
count is the reason the read exists as a step and not as a line.

**The last blocker, judged 2026-10-12 and repaired the same day:** the Arabic Editor's gate on the six
wave-packet distribution captions (`verdicts/2026-10-12-ed05-wave-packet-captions-ar-gate.md`) —
**five pass, row 4 returned in both languages**, repaired across its seven homes
(`verdicts/2026-10-12-ed05-ruler-stale-count-ruling.md`, **ruling #98**). The repair is a day old and
has been built, gated and read since. **Nothing in today's commit changes a word of any piece.**

---

## 2 · Build and assertions — on the artefact this commit actually produces

```
cd web && npm run build          → EXIT 0
qa_census: served 135 · sitemap 134 · EN 69 · AR 66 · article pages 88 · content pieces 88 (approved 88 / held 0)
```

The 135/134 difference is the branded 404, declared by name inside `qa_census` itself.

**All 29 gating assertions green on the flipped artefact, run in both of their homes:**

- **17 from `postbuild` in `web/package.json`** — inside the build above, exit 0.
- **12 CI build-step assertions re-run by hand against the built `dist`** — `qa_dist_input`,
  `qa_robots`, `qa_hreflang_clusters`, `qa_body_links`, `qa_lastmod`, `qa_reachability`, `qa_jsonld`,
  `qa_a11y_lang`, `qa_ar_language`, `qa_consumer_surface`, `qa_geo_fields`, `qa_held_assets` — every
  one exit 0.

Gate register **29 of 32**, derived by `qa_patch_queue` from its three homes rather than counted here.

## 3 · The held-leak assertion, INVERTED — the 2026-08-09 rule, executed by the tool

A sweep that asserts *zero held slugs in dist* passes **vacuously forever** the moment the wave flips.
The corpus state changed, so the assertion is re-derived rather than re-run:

```
qa_held_assets: 0 held slug(s), 44 approved slug(s), 88 control asset(s) checked
```

`qa_held_assets` inverts itself: with nothing held, it checks the positive side — **every approved
slug's still and og card is served**, 88 control assets, clean. Beside it, the positive checks the
held-mode sweep never ran, taken by hand on the six new slugs:

- **Every new slug resolves EN + AR in the built sitemap** — 6 × 2 `<loc>` entries, confirmed one by one.
- **Every new hero still resolves in both built article pages**, and **every og card resolves in the EN page** — 6 × 3 confirmed.
- **Held count on disk: 0.** `grep -rl '^approved: false$' web/src/content/` returns nothing; approved files **88**.

## 4 · What else is in this commit, and why it belongs in the flip rather than after it

**(a) The Edition 05 registry row** (`web/src/lib/editions.ts`). The editions index renders
`editions.map(...)` — **the registry, never the corpus** — so six pieces carrying `edition: 5` with no
row would have shipped **invisible on the archive surface**, and both home pages would have gone on
calling Edition 04 "current" while serving a newer wave. Row 5 is `status: 'current'`; Edition 04 moves
to `'closed'`. Period label **October 2026**: the label names the month an issue reaches readers, not
the span of its datelines — the convention every row already follows (Edition 04 is "August 2026" over
pieces dated 07-07 → 07-28). There was no September edition and the gap is left visible.

**(b) The cover** (`web/public/covers/edition-05.svg`), in the house line-art convention: six upright
strokes at six heights on one baseline, one thread through all six notches, the fourth notch ringed.
Ground `#E4E8DF`, accent `#2D6A4F` — contrast computed from the two values rather than judged by eye,
**5.15:1**, which clears AA (4.5:1) for the 12px mono kicker it carries. *Recorded while measuring it,
not acted on: Edition 04's `#9C5B3A` on its own `#E9E5DB` reads **4.20:1**, under AA for normal text.
That is an existing cover, a Designer's call, and it is not a thing to change inside a flip commit —
it is written down here so it is a known number rather than a thing nobody looked at.*

**(c) A served-bytes defect found by looking at the render, and fixed in the same commit.** See §5.

## 5 · The render was looked at, and it was wrong — the cover accent leak

Per ruling #16 and the 2026-08-23 rule, the editions page was **rendered and inspected**, not merely
counted. The Edition 05 cover printed its kicker in **Edition 01's vermilion**.

Measured rather than eyeballed — computed `fill` read out of a real browser, through an iframe, on the
built page:

| Cover | Registry accent | Computed `fill` BEFORE | Computed `fill` AFTER |
|---|---|---|---|
| Edition 05 | `#2D6A4F` | `rgb(217, 79, 42)` | `rgb(45, 106, 79)` |
| Edition 04 | `#9C5B3A` | `rgb(217, 79, 42)` | `rgb(156, 91, 58)` |
| Edition 03 | `#2E4C63` | `rgb(217, 79, 42)` | `rgb(46, 76, 99)` |
| Edition 02 | `#2F6F6A` | `rgb(217, 79, 42)` | `rgb(47, 111, 106)` |
| Edition 01 | `#D94F2A` | `rgb(217, 79, 42)` | `rgb(217, 79, 42)` |

**Cause:** `inlineCover()` injects each cover's markup — including its own `<style>` block — into the
page, and every cover uses the same five class names (`.wm`, `.ar`, `.kick`, `.th`, `.thm`). Inlined
SVGs do not carry a private scope: five `<style>` blocks in one document are **one cascade**, and the
last one in document order wins for all five figures. Render order is current-first then descending,
so the last block has always been **Edition 01's**, and every other edition's cover type has rendered
in Edition 01's accent since the second cover was inlined. The *line work* was always right, because
strokes are presentation attributes on the elements themselves — only the type leaked, which is why it
survived four editions of looking at the page.

**Fix (served bytes, Web Developer's lane):** each cover's root carries `class="ed-cover ed-cover-NN"`
and each of its five rules is scoped under that class. The file stays self-contained — it renders
identically when fetched standalone at `/covers/edition-05.svg` — and no cover can reach another's
type again. Five files, five rules each, verified by the table above.

**This is the day's ruling, filed as #99.**

## 6 · What must never be committed — checked, not assumed

- **No piece carries `approved: true` without clearing this gate in writing.** All six cleared it above.
- **No held piece's assets are left where the build can serve them.** There are no held pieces; the
  inverse check (every approved asset served) is green.
- **No credential, token or key.** The diff is twelve one-word frontmatter changes, one TypeScript
  registry row, one new SVG and five scoped `<style>` blocks.

---

## Verdict

**GATE PASSED — the wave flips.** Six pairs, twelve files, Edition 05 (AFRICA) ships. Seventy-one
consecutive days without a published piece end with this commit; the reason each of those days held is
on file, and none of them was a thin piece shipped to fill a slot.

— Manager · 2026-10-13
