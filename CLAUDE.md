# Madār (مدار) — repository guide for Claude

This repository **is** the publication and **is** the operation. There is no state
outside it: the editorial charter, the operating rules, the accumulated rulings, the
content in both languages, the QA tools and the daily briefs all live here. A run that
reads this repository has everything it needs.

Read on every run, in this order:

1. `agents/CHARTER.md` — the operating mandate. The five standing functions.
2. `agents/RUNBOOK.md` — the accumulated procedural rules. Long, and load-bearing.
3. The most recent `agents/briefs/*.html` — yesterday's artefact, **not** today's state.
4. `content-drafts/_EDITION_05_STATUS.md` — the live edition's ledger. **A dated section inside it is
   history, not state** — read the Log and the newest `RECONCILED AGAINST DISK` block before planning
   from any section above them. A run on 2026-10-04 reported three closed items as open because it
   read the 09-27 section, which is eleven screens above the entry closing them.
5. `agents/logs/WEBDEV-QUEUE.md` — **the operation's one standing queue, and from 2026-10-04 its head is
   binding** (RUNBOOK, *one queue, one head*). The previous run's forward question enters at the head;
   an item displaced three times goes first regardless; the run writes one line naming which head it
   took and what it displaced. **This file is in this list because a binding queue nobody is told to
   read is the same defect as a count nobody is named to maintain.**

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
  `agents/guidebook/INDEX.md` — currently **#1–#94**, and binding. **This range is
  ASSERTED, not remembered:** standing assertion 30, `qa_register_shape`, derives it from
  §3's own rows and fails the build when this sentence disagrees with them. Do not hand-edit
  it to match a memory; file the ruling and let the gate tell you the number.
  *(A filing run moves four counts always — §3's range, §3's heading, §1's count line and
  this one — plus a conditional fifth when the ruling joins a register family that keeps a
  running member count. The rule, both its amendments and the reasoning that earned them are
  in the RUNBOOK; the day-by-day record of every move this line made between 2026-09-20 and
  2026-10-08 is archived at `agents/guidebook/ARCHIVE-2026-09-20_2026-10-08-ruling-range-moves.md`.
  It was moved out of this file on 2026-10-10 under **ruling #94**, because 7,650 bytes of
  audit trail for a number a gate now maintains is a cost every run pays before it can do
  any work — and on 2026-10-09 that cost took the whole run.)*

- **Prove an assertion both ways.** A new check must be shown to stay silent on a
  known-good control *and* to fail on the defect it exists to catch. Prove the bite as
  carefully as the control: an injection that fails to change the artefact reads
  exactly like a passing control.
- **Never invent a traffic number.** The site carries no third-party tracker by
  design. Say so rather than estimating.
- **Count against the population, never against yesterday's number.** Ruling #57, earned four weeks
  running. A count that agrees with itself every day can disagree with the thing it counts for a
  month: the assertion-discipline family's member count was arithmetically perfect for five
  consecutive filings and wrong by three the whole time, because the rule that moves it was written
  after three members had already joined. **A point-of-filing rule fixes a count's future and leaves a
  step discontinuity where it was written; it never reconciles backward.** And count the *shape* too —
  five rows of the canonical ruling register carried three columns in a four-column table while every
  row count and range check ever run on it passed (2026-10-04).

## Layout

| Path | What it holds |
|---|---|
| `web/` | The Astro site. `src/content/articles` (EN) and `articles-ar` (AR). |
| `agents/` | CHARTER, RUNBOOK, guidebook (rulings), briefs, logs, growth notes, tools. |
| `agents/tools/` | **Thirty-two** standing QA assertions plus `madar_stats.py` and `build_font_bundle.py` (a generator, not an assertion — the count globs `qa_*.py`). Python 3, no deps — except `qa_render.py`, `qa_arabic_shaping.py`, `qa_arabic_joining.py` and `qa_feed_direction.py`, which need a headless Chrome. |
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

Use `npm run build`, not `npx astro build`: **seventeen** of the thirty-two assertions
(`qa_css_tokens`, `qa_render`, `qa_arabic_shaping`, `qa_arabic_joining`, `qa_stable_order`,
`qa_date_identity`, `qa_feed_enclosures`, `qa_feed_direction`, `qa_chrome_links`, `qa_census`,
`qa_packet_figures`, `qa_pair_frontmatter`, `qa_patch_queue`, `qa_served_manifest`, `qa_register_shape`,
`qa_third_party_origins`, `qa_bridge_coverage`) are gated from `postbuild` in `web/package.json`,
because an autonomous run is refused write access to `.github/workflows/**`. **`qa_packet_figures`
is the first gate that is not handed `dist`** — it takes the repository root, because a
distribution caption is never built; it is in `postbuild` because that is where a gate this
identity can wire lives, not because it has anything to do with the build. **`package.json`
is a second, equal home for gates** — a reader asking "what gates the deploy?" must read both
files (issue #6, default C applied 2026-09-20).

**The build must run in a full git checkout** (`fetch-depth: 0`). The sitemap's
`lastmod` resolver reads file dates out of git history and fails loudly — correctly —
in a shallow clone. This bit us once already; do not "fix" it by weakening the guard.

`.github/workflows/astro-pages.yml` runs twelve assertions as build steps, seventeen more
arrive through `postbuild`, and then a `verify` job byte-compares the published
artifact against the live origin. **29 of the 32 gate the deploy**; of the three that do
not, two (`qa_live_drift` — the `verify` byte-compare is strictly stronger;
`qa_sources_alive` — someone else's 404 is not our build's failure) say why in the
workflow file. **The third, `qa_feed_validators` (added 2026-09-24), is the first whose
reason cannot be written where the others are** — it belongs in the `verify` job and this
identity cannot write `.github/workflows/**`, so its reason lives in the tool's own header
and the one-line patch is staged at `agents/patches/` — **one home for the patch queue, moved
there 2026-09-27** when the weekly review found the queue split across two directories with
this file naming one and issue #7 naming the other. Applying that patch makes it
**27 of 29**. A green run means the bytes are actually served, not merely built.

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
**They moved again on 2026-10-10 with assertion 32, `qa_bridge_coverage` (ruling #93, standing-queue item 1)** — **seventeen** `postbuild` entries, **thirty-two** tools, **29 of 32 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is not the publication and not this repository's prose, but the STEP THAT CARRIES the other assertions' conclusions to the reader.** Item 1 asked which gating assertion is wired where it cannot observe its subject; the answer, enumerated, is **none of them** — all read `dist` or the repository root, both of which exist in the `build` job where all 29 run. The wrong home belongs to the **bridge**: only the `verify` job's byte-compare promotes a claim about `dist` into a claim about the origin, and it compares **six files of 257 — 2.3%**, with **zero of the 133 assets a page loads**, including the 34 fonts added two days earlier. It takes the repository root, not `dist` — the **fifth** such gate — because it parses the workflow file. The ratio is **measured and deliberately not asserted** (widening the bridge needs a workflow write this identity does not have, and a floor above today's reality would red every build until a patch nobody can apply lands); what it asserts is that bridge members exist, that every `.html` member is a page the sitemap claims, and that **the bridge spans both editions and both feeds.** Proved 13 ways, bite first, on /tmp copies — **and the harness caught the tool overcounting the bridge while its control printed the correct total**, because the verify job names both feeds twice and the two lists overlap exactly. Previously moved on 2026-10-08 with assertion 31, `qa_third_party_origins` (the self-hosted fonts, standing-queue item 4)** — **sixteen** `postbuild` entries, **thirty-one** tools, **28 of 31 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is the publication's *privacy posture*, which until 2026-09-18 was a sentence in the CHARTER with no number behind it and until today was a measurement with no gate behind it.** It asserts one thing: no page fetches anything automatically from an origin we do not own. The whole design is a classification the 09-18 audit wrote before any code existed — **by who initiates the fetch, never by origin** — because this publication points at ~180 external origins on purpose and a check that counted those would report our own method as our largest defect and be switched off inside a week. `<a href>` and `og:image` are counted and printed and **not** asserted, with the reason in the output. Proved **19 ways**, bite first, on a copy of `dist`, and the first bite is the markup removed from `Base.astro` this morning rather than an invented one. *(Also corrected today: `qa_patch_queue` printed its first home's label as `agents/tools/*.py` while the glob has always been `qa_*.py` — harmless for nine days, misleading from the moment this day added the first non-assertion tool to that directory.)* Previously moved on 2026-10-07 with assertion 30, `qa_register_shape` (ruling #90) — **fifteen** `postbuild` entries, **thirty** tools, **27 of 30 gating**, all three derived by `qa_patch_queue` rather than counted by hand. **It is the first assertion whose subject is this repository's own prose rather than the publication**, and the first to make one of this file's own counts a build failure: the ruling range in the non-negotiables above is now derived from §3's rows, which is the 09-27 amendment's fourth home closed by an instrument instead of by a habit. It takes the repository root, not `dist` — the **fourth** such gate — because a markdown table is never built. Previously moved on 2026-10-06 with assertion 29, `qa_served_manifest` (ruling #89) — fourteen
`postbuild` entries, twenty-nine tools, **26 of 29 gating**, all three derived by `qa_patch_queue`
rather than counted by hand. **It is the first assertion whose gated half and asserting half are
different modes of the same tool, and the distinction is load-bearing rather than tidy.** `--emit`
writes a per-URL fingerprint of the served bytes into `dist` and is gated from `postbuild`, because if
it ever fails to run the chain of memory breaks and the *next* build has no baseline; `qa_census` reads
it as a sixteenth instrument and asserts its routed-page count against the sitemap's own `<loc>` set, so
a manifest that quietly stops describing some pages fails the build instead of narrowing in silence.
`--check` fetches the manifest the **origin** is currently serving and is **not** gated — its home is the
`build` job after `npm run build`, which this identity cannot write, so the reason lives in the tool's
header and the step is staged at `agents/patches/2026-10-06-build-served-manifest-check.md`. **The
`verify` job is the wrong home and that is worth knowing rather than guessing:** verify compares the
artifact it just published against the origin, so origin == artifact by construction and the manifest
would be compared against itself — a check in the wrong home, passing forever, which is standing-queue
item 1's subject reached from the other side.

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
