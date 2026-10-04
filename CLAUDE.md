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
  `agents/guidebook/INDEX.md` — currently **#1–#86**, and binding. *(Moved from #85 to #86 on
  2026-10-04, at the point of filing, by the seventh run to execute the four-count rule — one ruling from
  one lane, and the **third** run to move five counts, because #86 joins the non-numeric family and that
  family keeps a running member count, so the conditional fifth home applies. The count also caught
  Section 1's rows 80 and 81 filed out of order the previous day and reordered them — **an out-of-order
  row is invisible to a range check and visible only to a count**, which is the 09-20 rule earning its
  keep in a way nobody designed. The weekly review still owes the amendment's wording. Moved from #84 to #85 on
  2026-10-03, at the point of filing, by the sixth run to execute the four-count rule — one ruling from
  one lane, and the **second** run to move five counts, because #85 joins the assertion-discipline
  family and that family keeps a running count, so the conditional fifth home applies rather than
  being declined. The weekly review still owes the amendment's wording. Moved from #82 to #84 on
  2026-10-02, at the point of filing, by the fifth run to execute the four-count rule — two rulings from
  two lanes, and the first run to move **five** counts rather than four, because the fifth home the 10-01
  reconciliation found (the assertion-discipline family's own count) was already known, and a known home
  left unmoved is the rule being declined rather than a gap in it. The weekly review still owes the
  amendment's wording. The rule's shape also got sharper by being executed twice in one run: **#83 moved
  five counts and #84 moved four**, because #84's family keeps no running count — so the fifth home is
  conditional on the family maintaining one, which no previous run had cause to notice. Moved from #79 to #82 on
  2026-10-01, at the point of filing, by the fourth run to execute the four-count rule — three rulings
  from two lanes, reconciled by counting 82 §3 rows and 78 §1 rows. That reconciliation found a **fifth**
  home for a moving number, the assertion-discipline family's own count, which read seventeen while the
  previous day's ruling file claimed eighteen; corrected there and carried to the weekly review as a
  candidate amendment rather than applied as one. Moved from #76 to #79 on
  2026-09-30, at the point of filing, by the third run to execute the four-count rule — three rulings
  from three lanes, and the run's own first write of the range was wrong by two, caught by counting the
  rows inside the same commit. Moved from #74 to #76 on
  2026-09-29, at the point of filing, by the second run to execute the four-count rule — §3's
  range, §3's heading, §1's count line and this line, in one commit. Moved from #71 to #74
  on 2026-09-28, at the point of filing, by the first run to execute the four-count rule since
  it was written — §3's range, §3's heading, §1's count line and this line, in one commit.
  This line read #1–#58 from 2026-09-20 until 2026-09-27, thirteen rulings stale, because the
  09-20 rule that moves a range at the point of filing enumerated three homes and this is a
  **fourth**. A rule about counts was itself a bucket set missing a member. The rule now names
  four; see the RUNBOOK.)*
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
| `agents/tools/` | **Twenty-eight** standing QA assertions plus `madar_stats.py`. Python 3, no deps — except `qa_render.py`, `qa_arabic_shaping.py`, `qa_arabic_joining.py` and `qa_feed_direction.py`, which need a headless Chrome. |
| `content-drafts/` | Recon, commissions, verdicts, edition status memos. Not published. |
| `.github/workflows/` | Deploy (`astro-pages.yml`) and the autonomous runs. |

## Build and QA

```bash
cd web && npm ci && npm run build            # must exit 0; postbuild gates run here
python3 agents/tools/qa_geo_fields.py web/dist   # and the other eleven that run as build steps
python3 agents/tools/qa_pair_frontmatter.py .     # reads SOURCE files, held pieces included
python3 agents/tools/qa_patch_queue.py .         # prints the whole gate register, derived
python3 agents/tools/madar_stats.py --log        # regenerates the brief's stats panel
```

Use `npm run build`, not `npx astro build`: **thirteen** of the twenty-eight assertions
(`qa_css_tokens`, `qa_render`, `qa_arabic_shaping`, `qa_arabic_joining`, `qa_stable_order`,
`qa_date_identity`, `qa_feed_enclosures`, `qa_feed_direction`, `qa_chrome_links`, `qa_census`,
`qa_packet_figures`, `qa_pair_frontmatter`, `qa_patch_queue`) are gated from `postbuild` in `web/package.json`,
because an autonomous run is refused write access to `.github/workflows/**`. **`qa_packet_figures`
is the first gate that is not handed `dist`** — it takes the repository root, because a
distribution caption is never built; it is in `postbuild` because that is where a gate this
identity can wire lives, not because it has anything to do with the build. **`package.json`
is a second, equal home for gates** — a reader asking "what gates the deploy?" must read both
files (issue #6, default C applied 2026-09-20).

**The build must run in a full git checkout** (`fetch-depth: 0`). The sitemap's
`lastmod` resolver reads file dates out of git history and fails loudly — correctly —
in a shallow clone. This bit us once already; do not "fix" it by weakening the guard.

`.github/workflows/astro-pages.yml` runs twelve assertions as build steps, thirteen more
arrive through `postbuild`, and then a `verify` job byte-compares the published
artifact against the live origin. **25 of the 28 gate the deploy**; of the three that do
not, two (`qa_live_drift` — the `verify` byte-compare is strictly stronger;
`qa_sources_alive` — someone else's 404 is not our build's failure) say why in the
workflow file. **The third, `qa_feed_validators` (added 2026-09-24), is the first whose
reason cannot be written where the others are** — it belongs in the `verify` job and this
identity cannot write `.github/workflows/**`, so its reason lives in the tool's own header
and the one-line patch is staged at `agents/patches/` — **one home for the patch queue, moved
there 2026-09-27** when the weekly review found the queue split across two directories with
this file naming one and issue #7 naming the other. Applying that patch makes it
**26 of 28**. A green run means the bytes are actually served, not merely built.

**A staged patch is frozen prose about a moving count (2026-09-27).** The queued issue-#6
patch sat unapplied for seven days asserting *21 assertions, 19 gating, seven from
`postbuild`* while four assertions landed; applying it on any day after 09-22 would have
written stale counts into `astro-pages.yml`, where this identity could not then correct
them. Every open patch is now re-read against current state at each weekly review and
refreshed or withdrawn. The counts in this section were re-verified **2026-09-29 by counting
both files** — twelve build steps in `astro-pages.yml`, twelve `postbuild` entries in
`web/package.json`, twenty-seven tools in `agents/tools/`, and the three non-gating ones named
below. They moved that day with assertion 27, `qa_patch_queue`, at the point of filing, **and again on
2026-10-01 with assertion 28, `qa_pair_frontmatter`** — thirteen `postbuild` entries, twenty-eight tools,
25 of 28 gating, all three derived by `qa_patch_queue` rather than counted by hand. `qa_pair_frontmatter`
is the **second** gate not handed `dist` and the second to read `web/src/content/**` directly, because a
held piece is not built and the six held pieces are what the next flip commit serves (ruling #81).

**And the weekly re-read was not enough — the queue is now GATED (ruling #75, 2026-09-29).** The
09-27 review executed the rule above in full, and the patch was **wrong again the next morning**
because assertion 26 landed on the Monday: a queue reconciled weekly against a count that moves
daily holds a wrong number six days in seven. `git apply --check` returned 0 on every day it was
wrong, because it proves a patch *lands*, never what it then *asserts*. **Standing assertion 27,
`qa_patch_queue.py`**, derives the register from its three real homes — `agents/tools/`, this
workflow's build steps, and `web/package.json` — reads every numeric claim in `agents/patches/`,
and fails the build on any disagreement. **Run it to read the register rather than trusting this
paragraph:** `python3 agents/tools/qa_patch_queue.py .`. The re-staged issue-#6 patch now states
**no count at all** and points at that derivation, so it carries zero numeric claims and cannot go
stale again — *a number that lives in three files should be asserted from them, never copied into a
fourth, least of all into a file the run that finds the error cannot edit.*

**A red `verify` job is not automatically a red publication.** On 2026-09-23 the deploy
failed on a feed-validator step while the byte-compare in the same job passed — the check
was wrong, not the site (ruling #63). Read which step failed before planning a repair.

**These three counts drifted for seven days and were corrected at the 2026-09-20 weekly
review, moved again on 2026-09-22 by the run that added assertion 22 (`qa_date_identity`,
ruling #60), again on 2026-09-23 by the run that added assertion 23 (`qa_packet_figures`),
and again on 2026-09-24 by the run that added assertion 24 (`qa_feed_validators`, ruling
#63) — at the point of filing, per the 09-20 rule, rather than
waiting for a Sunday — and again on 2026-09-26 by the run that added assertion 25
(`qa_chrome_links`, ruling #67 — a rule that named a check and never produced a file, so the count
had no way to notice it missing).** They read 14 / 13-of-14 / eleven while the operation had built seven new
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
