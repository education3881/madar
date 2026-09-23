# Madār (مدار) — repository guide for Claude

This repository **is** the publication and **is** the operation. There is no state
outside it: the editorial charter, the operating rules, the accumulated rulings, the
content in both languages, the QA tools and the daily briefs all live here. A run that
reads this repository has everything it needs.

Read on every run, in this order:

1. `agents/CHARTER.md` — the operating mandate. The five standing functions.
2. `agents/RUNBOOK.md` — the accumulated procedural rules. Long, and load-bearing.
3. The most recent `agents/briefs/*.html` — yesterday's artefact, **not** today's state.
4. `content-drafts/_EDITION_05_STATUS.md` — the live edition's ledger.

## What this publication is

Madār is a bilingual (English + Arabic) publication about early-childhood and K–12
education, written for educators, parents and education regulators. Every piece stands
on **named primary sources read in served text**. The Arabic edition is *composed*, not
translated. Nothing ships without clearing the Editor's five-test rubric in writing.

## Non-negotiables

- **Verify state before planning.** Never plan a day off a brief. Check `git log`,
  compare local against `origin/main`, check `git status`, and confirm the live site.
  Name any missed day plainly. (`agents/guidebook` — state verification.)
- **Quality over slot.** Hold a piece rather than ship it thin. The Editor is the
  filter and the Manager never overrides a park.
- **Held pieces are invisible.** `approved: false` means the piece contributes no
  page, no sitemap entry, no feed item, no `lastmod` date and no bytes. Four standing
  assertions enforce this; do not weaken them.
- **A figure is cited as read.** Never composed from a pattern, never averaged across
  registers, never carried from a search summary. See the ruling register in
  `agents/guidebook/INDEX.md` — currently #1–#58, and binding.
- **Prove an assertion both ways.** A new check must be shown to stay silent on a
  known-good control *and* to fail on the defect it exists to catch. Prove the bite as
  carefully as the control: an injection that fails to change the artefact reads
  exactly like a passing control.
- **Never invent a traffic number.** The site carries no third-party tracker by
  design. Say so rather than estimating.

## Layout

| Path | What it holds |
|---|---|
| `web/` | The Astro site. `src/content/articles` (EN) and `articles-ar` (AR). |
| `agents/` | CHARTER, RUNBOOK, guidebook (rulings), briefs, logs, growth notes, tools. |
| `agents/tools/` | **Twenty-three** standing QA assertions plus `madar_stats.py`. Python 3, no deps — except `qa_render.py`, `qa_arabic_shaping.py` and `qa_arabic_joining.py`, which need a headless Chrome. |
| `content-drafts/` | Recon, commissions, verdicts, edition status memos. Not published. |
| `.github/workflows/` | Deploy (`astro-pages.yml`) and the autonomous runs. |

## Build and QA

```bash
cd web && npm ci && npm run build            # must exit 0; postbuild gates run here
python3 agents/tools/qa_geo_fields.py web/dist   # and the other eleven that run as build steps
python3 agents/tools/madar_stats.py --log        # regenerates the brief's stats panel
```

Use `npm run build`, not `npx astro build`: **nine** of the twenty-three assertions
(`qa_css_tokens`, `qa_render`, `qa_arabic_shaping`, `qa_arabic_joining`, `qa_stable_order`,
`qa_date_identity`, `qa_feed_enclosures`, `qa_census`, `qa_packet_figures`) are gated from `postbuild` in `web/package.json`,
because an autonomous run is refused write access to `.github/workflows/**`. **`qa_packet_figures`
is the first gate that is not handed `dist`** — it takes the repository root, because a
distribution caption is never built; it is in `postbuild` because that is where a gate this
identity can wire lives, not because it has anything to do with the build. **`package.json`
is a second, equal home for gates** — a reader asking "what gates the deploy?" must read both
files (issue #6, default C applied 2026-09-20).

**The build must run in a full git checkout** (`fetch-depth: 0`). The sitemap's
`lastmod` resolver reads file dates out of git history and fails loudly — correctly —
in a shallow clone. This bit us once already; do not "fix" it by weakening the guard.

`.github/workflows/astro-pages.yml` runs twelve assertions as build steps, nine more
arrive through `postbuild`, and then a `verify` job byte-compares the published
artifact against the live origin. **21 of the 23 gate the deploy**; the two that do not
(`qa_live_drift` — the `verify` byte-compare is strictly stronger; `qa_sources_alive` —
someone else's 404 is not our build's failure) say why in the workflow file. A green run
means the bytes are actually served, not merely built.

**These three counts drifted for seven days and were corrected at the 2026-09-20 weekly
review, moved again on 2026-09-22 by the run that added assertion 22 (`qa_date_identity`,
ruling #60), and again on 2026-09-23 by the run that added assertion 23 (`qa_packet_figures`)
— at the point of filing, per the 09-20 rule, rather than
waiting for a Sunday.** They read 14 / 13-of-14 / eleven while the operation had built seven new
assertions and wired five of them — in the one file every run is told to read first. The
weekly review now prints the ratio (`N of M gate the deploy`) and reconciles it against
both homes; if this paragraph and that ratio ever disagree, the workflow files are the
state and this paragraph is the stale one.

## Writing

House voice: plain, specific, unhurried. Short declarative sentences. No marketing
register, no exclamation marks, no hype. A hedge that appears in a source's citation
must appear in the sentence that uses it — the annotation and the sentence are written
from the same open register. Prefer the source's own grammar over a firmer paraphrase.

## Commit messages

Single line, ASCII, no `!` and no `$` (they break in zsh history expansion, twice
already). Keep the detail in the brief, not the subject line.
