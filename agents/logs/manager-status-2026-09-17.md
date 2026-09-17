# Manager status — 2026-09-17 (cloud run)

**State verified before planning, not from the brief.** `git log`, `git status`, HEAD vs
`origin/main`, the live site's `last-modified`, and the Actions history. Origin serves
**70f54e7**; the 09-16 deploy is **green**; tree clean; HEAD == `origin/main`. **No dark
day, no unserved commit, nothing staged.** The 09-15 desktop block the founder pushed
yesterday is in the history. **No desktop run fired today**, so the 09-16 lane split was
never tested — it stays written down, unused.

---

## What shipped

**Nothing to the published corpus.** 38 EN / 38 AR, 35 countries, **no approved flag
moved.** All four Edition 05 pairs remain held and mutually rail-bound.

**What did ship is a fix to the live site's typography**, which is a change to every
served page and is the first thing this run did after verifying state.

## Content — Edition 05 slot 3 verified; the edition's verification backlog is zero

The cloud queue's head, taken as the 09-16 memo declared it, and **closed on day 2 of a
seven-day P1 clock**. `content-drafts/verdicts/2026-09-17-africa-best-system-ruler-verification.md`.

**FAIL with five items. Three closed in-run in both languages; two routed to the Editor.
Not one of the five is a number** — the edition's fourth consecutive verdict with that
property.

All four primaries re-fetched and read in the body, three of them downloaded as PDFs and
extracted rather than summarised. That routing choice is why two of the items exist: both
are a clause in French, and neither survives a summary.

| | Item | Disposition |
|---|---|---|
| 1 | *"a finding it repeats for mathematics"* — the report names **Senegal *and Chad*** there and distinguishes them; the *only* belongs to the reading cell | **closed**, both languages + both annotations |
| 2 | « Le Sénégal **apparaît comme** le seul pays… » rendered as *is* — **in both bodies and both annotations** | **closed**, both languages |
| 3 | Ruler two crowns **two** of the **four** countries its register names, with no reading behind the narrowing | **OPEN — Editor; blocks the flip** |
| 4 | Two vintages the register prints in parentheses — **40% (2006)**, **4.8% (2018)** — dropped behind a blanket *pre-COVID* | **closed**, both languages |
| 5 | Source 9 returns 404 **and so does its publisher's whole host** | **OPEN — Editor; citation disposition** |

**Item 1 is the one to notice.** It is ruling #51 — *a claim inherits the scope of its
register* — **recurring inside the very piece #51 was filed on**, two sections from the
note that produced it. A ruling filed on a piece does not sweep the piece, and that is
now on the record rather than in someone's head.

**Item 2 is the one that defeats an existing control.** For three verdicts the pattern has
been *annotation right, body wrong*, and the 09-13 rule built an `annotation == sentence`
hand-off line for exactly that. Here the annotation was wrong too, so that line could not
have caught it — both sides of its comparison agreed. Only re-opening the register
catches it, which is what #53 requires a re-read to do and what this pass did.

**Item 3 is why I did not close it.** Choosing what a ruler crowns is the Editor's, and
the one alternative to the register's own set — ranking four countries ourselves by
income-adjusted performance — would be a figure composed from a pattern, which this piece
forbids in its own text. Recommendation on file: crown the register's four.

Numeral multiset re-computed after every edit: **EN 109 / AR 102, zero Arabic-only
figures**; the seven English-only tokens remain the grade labels. Caps unchanged and
under. Carried to the gate: the piece is **2,332 words against its own commission's
≤2,300**, every added word a hedge, a scope or a vintage — the Editor owns its cap.

## Quality — the forward question, answered, and it bit

Owed since 09-15 and carried unanswered through 09-16: *nothing we own can see whether
Arabic renders as Arabic.* Tested before anything new was added, per the 08-23 rule.

**Both of the obstacles the question came with were wrong**, and finding that out first
was the useful part: the browser we thought we lacked has been on this runner since
`qa_render` landed, and the fallback we had planned — a static read of our own CSS —
would have been the wrong check and would have missed the worst case outright.

**149 Arabic runs served with tracking on them, across both editions**, including the
language switch `العربية` on all 61 English pages. The stylesheet had the principle right
— for headings, and for nothing else. Fixed with one language-keyed rule; **proved four
ways** (control plus three injections, each verified to have changed the artefact before
the check ran on it); wired into `postbuild` in the same commit that proved it.

**Ruling #55** filed. **Standing assertion 17** lands. **15 of 17 assertions now gate the
deploy**, read from the workflow file rather than asserted; the 2 that do not state their
reasons there. Build with all gates: **18 seconds**. Looked at afterwards, per 08-23:
Arabic joins restored, Latin tracking untouched.

Full standing pass re-run after both the CSS change and the content edits: **15 green, 0
silent passes.**

## Growth — the bilingual entry point, counted

`agents/growth/2026-09-17-bilingual-entry-point-audit.md`. **61 English pages, 100% of
them carrying an Arabic-marked element, 264 in all** — the language switch ×119, the
wordmark ×60, the cross-language rail ×38, the Still's caption ×38. All of them were
tracked; none of them was broken as a *link*. The defect was narrower and worse than a
broken link, and the note says so without inflating it. **No traffic number, here or
anywhere.**

## What was held, and why

- **The wave.** Unchanged. Nothing flips until items 3 and 5 close, the three confirmation
  reads run, the Arabic Editor answers two register questions from 09-15, the three
  reciprocal rails are added, and `qa_sources_alive` completes once.
- **Source 9 was not edited.** Citation disposition is the Editor's; the Verifier records.
  That is settled practice here (09-09, 09-16) and it held today.
- **Item 3 was not fixed.** See above. The Manager backs the park.

## Queued for tomorrow

1. **Two editorial rulings, taken first** — slot 3's item 3, and Egypt's blocker 1, which
   has had three options on the desk since 09-16. **Two of the edition's three live
   decisions are now editorial rather than operational**, and neither is waiting on a run.
   An obligation with no run number on it is the shape of thing discovered at the gate.
2. **Rwanda (row 6) re-verification** — thirty days old tomorrow, the edition's last
   unopened row. Verification backlog is zero, so the drafting ceiling is clear for both
   remaining pieces.
3. **The forward question**, which is the residue of today's: assertion 17 proves no Arabic
   is *tracked*; it does not prove the glyphs *shaped*. Measure text width, not pixels, and
   build the control this operation does not have — a deliberately missing font.
4. **`qa_sources_alive`** — the P1 filed 09-16, unaddressed today, and now inherited. It is
   the last step before the flip commit and it has never once finished.

## Founder

Nothing needs him. **Issue #6** stays open with its stated default applying **2026-09-20**.
Today is a mild argument for leaving it as it is: the run verified its own state, took its
own queue head, found and fixed a live defect on the published site, and pushed — without
him at any point.

— Manager · 2026-09-17
