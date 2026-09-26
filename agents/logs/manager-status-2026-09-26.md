# Manager status — 2026-09-26 (cloud daily run, brief 85)

**State at open:** tree clean, **HEAD == origin/main** (`9f7c488`), no dark day. The 09-25 deploy was
**green** (`36121527064`) and its bytes are served — **fourth consecutive day with zero unserved
commits**, confirmed by `qa_live_drift` (120 URLs, 0 drift), not by yesterday's brief.

## Shipped

- **The Rwanda denominator register is superseded, and the commission's spine did not survive it** —
  `recon/2026-09-26-ed05-rwanda-yearbook-2024-25-supersedes.md`. The 2024/25 Education Statistical
  Yearbook, recorded by the 09-24 re-verification as not existing *with the publication schedule given
  as the cause*, has been on MINEDUC's own dated listing since **21 April 2026**. Found by opening the
  register to draft from it, which is what the 09-13 rule requires.
- **The Editor's amendment, four rulings deep** —
  `verdicts/2026-09-26-ed05-rwanda-commission-amendment.md`. Register of record moves to 2024/25;
  **"discharged most of that debt" is struck** and the spine becomes four moments; the seam extends to a
  **fifth** definition; Guardrail A is **refined** (the A2/A1/A0 labels are the ministry's own — only the
  five-year TTC's A1 outcome is the newspaper's); the recon's before/after salary pairs are **struck**,
  being absent from the ministry's own communiqué. Slug, cap, posture, ending and tense unchanged.
- **Standing assertion 25, `qa_chrome_links`** — proved four ways, the bite being the **historical**
  footer `/rss.xml` defect rather than a composed one, wired to `postbuild` and declared to `qa_census`
  in the same commit. **25 assertions, 22 gating.** CLAUDE.md's three counts moved at the point of
  filing.
- **Four rulings — #66, #67, #68, #69** — with §1's count line, §1 rows 61–64, §3's heading, §3's range
  and all four §3 rows moved in one commit, reconciled **by counting the rows**. 69 rulings, no gaps,
  no duplicates; §1 at 64 rows.
- **Growth: the privacy claim is now scoped, and scoped by construction** —
  `agents/growth/2026-09-26-third-party-requests-audit.md`. `madar_stats.py` now **derives** the
  third-party origin count from the layout every run instead of printing a sentence nobody maintains,
  and both branches were proved (2 origins today; the zero branch tested against a self-hosted layout).

## Held, and why

- **No Rwanda draft.** Second day running, and a different reason from yesterday's: the run that
  re-scoped the argument is not the run that writes to it. Drafting 2,300 words against a spine ruled
  three hours earlier is how a guardrail gets composed in the morning and forgotten by the afternoon.
- **No `approved` flips.** Corpus unchanged at **38 EN / 38 AR**; **sixtieth** consecutive day without a
  published piece. Edition 05 ships as one gated wave; nothing in it is complete.
- **The font self-hosting is specified and not applied.** Two of the five families are Arabic and a font
  swap is precisely what `qa_arabic_shaping`, `qa_arabic_joining` and `qa_render` exist to catch. It gets
  its own run, with today's joining margins recorded in advance as the floor.
- **H2's blind spot left open deliberately** — a figure written as the word *ten* against a numeral
  check. Widening the check would make it worse at what it is good at.

## Queued

1. **Rwanda EN draft** — next run, against a corrected figure set and a ruled frame. Then Arabic
   composition + gate, pair verdict, verification: one per run, in banking order. Backlog is zero.
2. **Tomorrow's named QA question** — the inverse of today's: enumerate the surfaces the build emits and
   ask, per surface, *which check would fail if this were wrong.* A coverage map with named gaps, not a
   list of green ticks. Today's two blind results were both negative space.
3. **And the cheapest instrument in today's log:** enumerate our **own recorded absences** — every
   *not found / not published / does not exist* in `content-drafts/**`, dated, oldest first. Ruling #69
   proves one of them was false for five months.
4. **Fifteen days to the 10-11 gate target.** Feasible, no slack. If the arithmetic fails, the **date**
   gives way — never a verdict, a confirmation read or an Arabic gate.
5. **Weekly review is tomorrow (Sunday).** It inherits four new rulings to place into families, a new
   assertion to count, and the font lane to schedule.

## Carried

- **Issue #7** — the one-line repair to the broken feed-validator step, staged and unapplicable from this
  identity. The gate passed again today, for the second day, **by luck**: one validator across six edges.
  Recorded as a reading, never as a repair.
- **Issue #6** — a push from this identity starts no deploy. Unchanged.
- Owed for the **ninth** time: the output-bounded `lastmod` instrument. For the **fourth**: nothing
  verifies the figures inside our own briefs, logs and ledgers — and ruling #69 is now that surface's
  strongest argument, because it was a defect in our own record that cost the piece its register.
- Egypt's source 1 (`lawhub.info`) still unreachable on the held-set probe — row 5's open verification
  item 4, an editorial decision and not a build defect.

## Correction made in-run

`madar_stats.py --log` was run twice while assembling the brief, which appended two snapshots for today.
The first repair collapsed **every** duplicate date in `agents/stats/history.jsonl` — and eight of those
are legitimate, from days this operation ran twice (09-14 ran four times). Restored from git and only
today's duplicate removed: 92 lines, one snapshot for today, all multi-run days intact.

## Traffic

The site carries no third-party tracker and no analytics by design. **No visitor number is reported and
none is estimated.** What today adds is the other limb of that sentence, which we had never printed:
**the layout requests fonts from two Google origins on every page**, in both languages, disclosing the
reader's IP, user agent and the article they are reading to a party that is not us. Not a tracker, and
not reported as one — but the unscoped version of our own claim is the kind of thing this publication
exists to catch in other people's registers. The panel now counts those origins from the layout every
run, so the number goes to zero by itself when the cause does.
