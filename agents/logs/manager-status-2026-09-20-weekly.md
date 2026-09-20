# Manager status — 2026-09-20 (weekly review)

**State at open:** `HEAD == origin/main == 78ea08c`, tree clean, 0 commits ahead or behind.
The live origin serves `Sun, 20 Sep 2026 09:51:25 GMT` — **today's bytes**, from a deploy
that went green on all three jobs (`build`, `deploy`, `verify`) at 09:50, forty seconds
after the daily's last commit. Nothing is unserved and nothing is unpushed. **This is the
first weekly review in this operation's history to open with no gap of any kind to name.**

The daily run fired at 09:19 and completed before this review started; its four commits are
on the origin. This review runs as the second run of the day and reads the edition ledger's
lane rule before planning, as that rule requires.

## The week, counted

| | |
|---|---|
| Window | 2026-09-14 → 2026-09-20 |
| Days with a run | **7 of 7 — no dark day, a first** |
| Runs | **9** (two on 09-14, two on 09-15, one on each of the other five) |
| Commits landed | 19 |
| Days unpushed, at any point | **0** |
| Deploys | 10 · **8 green, 2 red** (09-17 `qa_lastmod`; 09-19 the `verify` feed-cache step) |
| Rulings filed | **#49 → #58 — ten, against a previous single-week record of four** |
| Standing assertions | 14 → **21**; gating 13 → **19** |
| Pieces published | **0** · 54th consecutive day |
| Editorial progress | 1 drafted (Egypt, row 5) · 1 pair banked (slot 3, 09-15) · 1 verification verdict (slot 3, 09-17) |

## What this review did

- **Consolidated the guidebook**, which had drifted further than at any point on record:
  ten rulings on disk against a header, a table and a series line all reading `#1–#48`, and
  **Section 1 stopped at row 39** with rows 40–53 as loose files. All reconciled; fourteen
  §1 rows merged, seven row numbers assigned; §3's families heading corrected from "three"
  to eight — it had said "three" since 2026-08-23 while four more families were named
  under it; the 08-23 → 09-06
  addenda archived per the two-cycle rule. **#1–#58, no gaps, no duplicates, verified file
  by file.**
- **Corrected `CLAUDE.md`**, which told every run the operation owns *fourteen* assertions
  of which *13 gate the deploy*. True numbers: **21 and 19**. Stale by seven assertions in
  the one file every session is told to read first.
- **Reconciled the edition ledger against disk** — every cell backed by a file — and
  **re-read every forward-looking date in the held set against the calendar**, which found
  two items that block the flip (below).
- **Retired the lane split.** Declared 09-16, never once tested, the last desktop run was
  09-16. Rwanda's re-verification is released to any run after seven days reserved for a
  cadence that did not fire.
- **Read last week's bet** (it paid, four numbers, verified on the live origin a week on)
  and **set this week's**.
- **Applied issue #6's stated default (option C)** — its date was today and it passed
  unanswered.
- **Opened `agents/logs/WEBDEV-QUEUE.md`** and held team expansion for the eighth week,
  with a trigger that is now checkable by looking rather than by arguing.
- **Closed one 33-day-old debt**: every feed link and enclosure fetched from this runner's
  egress against the live origin — 78/78, 76/76, and every declared `length` exact.

## Two findings routed, neither fixed here

Both are in the held set, both are **#46's clock**, both block the wave gate, and neither is
edited by this review — the prose is the Editor's and the trace is the Verifier's.

1. **Zambia (row 1), both languages:** *"Zambia goes to a general election in August 2026"*,
   in a piece datelined 25 August, read on 20 September, gating on 11 October. **This review
   states nothing about when the election was held or what it returned** — no register for it
   has been read by this operation, and supplying one from memory is a figure composed from a
   pattern. The Verifier opens a register; the Editor re-tenses.
2. **Slot 3 (row 4), both languages:** the closing sentence narrows its own register's *last
   quarter of 2026* to **December**. The annotation is right, both bodies are wrong, and the
   wrong thing is *narrower* rather than false — ruling **#51** committed a third time inside
   the piece that earned it, this time by a date.

**The shape they share is the week's sharpest finding:** each sits in a sentence whose first
half is correct and fails in the second, where the writer moved from the register to the
rhythm. A hedge dropped outright is what the 09-13 rule catches. A hedge that survives the
citation, survives the first clause and dies in the last one is a different failure, and
nothing we own looks for it. Named as the forward surface for the week.

## Queued for tomorrow

1. **Egypt's Arabic composition and gate** — the declared lane for two runs running, and it
   has now slipped twice. It is the first lane, before anything else.
2. The two clock items above, Verifier then Editor.
3. The Web Developer queue, in its own file for the first time — item 2 (`qa_sources_alive`
   unschedulable) is the only one that blocks the flip.
4. Rwanda (row 6) re-verification, now unreserved.

## Nothing to escalate

No P0. The two open founder decisions (#6, #7) are carried in the review by name with their
ages and their stated defaults; #6's default fired today and was applied.

— Manager · 2026-09-20 (weekly review)

## Artefact check — the 2026-08-23 rule, closed properly for the first time

The rule requires that every HTML artefact the operation renders for a human is **opened and
looked at** before the push. Last week's review could not do it — no headless browser was
installable in that sandbox — and said so rather than glossing it. **This runner has one**,
the same Chrome three standing assertions already drive, so the rule is met as written
rather than substituted for.

`agents/reviews/2026-09-20-weekly-review.html`:

- **Tag-balance parse:** 0 mismatches, 0 unclosed, 6 sections opened and closed.
- **CSS variables:** 16 used, 16 defined, 0 unresolved. Every class used has a rule (15/15).
- **Rendered in headless Chrome** at 1200px: DOM 46,826 bytes, **5,415 visible words**, `<main>`
  and the `.container` wrapper both present in the *rendered* DOM — which is the assertion the
  08-16 defect earned, when two briefs shipped edge to edge because the template lost its
  wrapper and nobody looked.
- **Looked at, in three places, not just measured:** the masthead and founder summary; §4's two
  flag boxes; and the footer. The Arabic in §4 — «فزامبيا ذاهبةٌ إلى انتخاباتٍ عامةٍ في أغسطس
  2026» and «تُقرأ من جديد في ديسمبر» — renders **shaped, joined and right-to-left**, inline
  inside English sentences, with no broken joins. That is assertion 17/18's property checked by
  eye on an artefact those assertions do not cover, because they enumerate `dist` and this file
  is not in `dist`.

**Not claimed:** nothing here says the file looks *good*, only that it is not broken in the four
ways we have previously broken one.

— Manager · 2026-09-20

## Addendum — the deploy this review cannot watch, and why the 403 happens

Block pushed as `1bbd384`. The review then attempted `gh workflow run astro-pages.yml` so it
could confirm the deploy itself, and was refused **HTTP 403 — Resource not accessible by
integration**. Third refusal of that exact call (09-14, 09-15, today), and the first time the
cause has been pinned rather than described.

**Inside the agent step, `GITHUB_TOKEN` and `GH_TOKEN` hold the same value, and it is the
Claude App's installation token** — `gh auth status` reports `claude[bot]`. It is *not* the
workflow job's Actions token. The `actions: write` permission `madar-weekly.yml` grants at
line 38 belongs to a credential this process never sees, which is why declaring it on 09-15
changed nothing, and why the workflow's own `publish what the review pushed` step works: that
step passes `${{ github.token }}` explicitly, at step level, where the expression is resolved
by the runner rather than read from the environment.

**Two identities, one deliberately weaker, and the weaker one is the one the agent runs as.**
That is a correct design and this review is not asking for it to change — it is the same
property that makes the workflows-directory refusal worth keeping. It does mean the 09-14
rule's clause 3 applies to the weekly exactly as it applies to the daily: **the run verifies
the live origin rather than its own build, and it cannot verify a deploy that starts after it
ends.**

Routed into issue #6 as the missing half of its diagnosis.

**Monday's first act, before Egypt's Arabic and before anything else:** confirm the deploy for
`1bbd384` or later went green on all three jobs, **against the live origin**. If it went red on
the `verify` feed-cache step, that is issue #7's known flake — twice in nineteen days, both
times while the site published perfectly — and it says nothing about the publication. Anything
else is real and is the day's first priority.

— Manager · 2026-09-20
