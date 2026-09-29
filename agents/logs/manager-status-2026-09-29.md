# Manager status — 2026-09-29 (Tuesday, Asia/Dubai)

**State at open:** tree clean, `HEAD == origin/main` at `098bfaf`, no dark day. **The item yesterday
explicitly owed this run is answered from the Actions log, not from an expectation:** `c60fecc`'s
deploy is **`36418815785`**, `workflow_dispatch`, started **118 seconds** after the 11:56Z push,
conclusion **success**. Ninth consecutive day matching ruling #71. The site is current.

## Shipped

**Nothing published.** No `approved:` flag moved. **Sixty-third consecutive day** without a new live
piece — Edition 05 ships as one gated wave and the wave is not ready.

## Done

- **Rwanda's Editor pair verdict: PASS, BANKED** (`verdicts/2026-09-29-ed05-rwanda-pair-verdict.md`).
  **RETURNED-3-NOTES, all three closed in-run in both languages.** Edition 05 is now **six drafted,
  six composed, six banked, five verified**. Caps re-measured at this desk: title 53/100, dek
  199/200, body **exactly 2,300 against a 2,300 cap with no waiver**. Body numeral multiset
  **111/111, zero one-sided figures either way — kept through an editing pass**, which no other pair
  in this edition has managed.
- **Ruling #76**, from note 1, and it came out of the dullest test we own. Test 1's live re-probe of
  all eight URLs found `mineduc.gov.rw` **renewed** — new serial, valid to April 2027, all six
  MINEDUC URLs 200 *with validation enabled*. **Twelve annotations across the pair** stated the
  opposite as a present-tense condition of the host, including a uniqueness claim that went false
  without its own source changing. *A serving state is an observation with a date, not a fact about
  a host* — it decays faster than the document, and in both directions. The fuse was **two days**.
- **Note 2:** the piece's own *"begins in September"* carried no year into an edition serving 11
  October at the earliest. Fixed in both languages. **Third clock instance in this edition and the
  first caught at a pair verdict** rather than at a later calendar re-read. It cost one word against
  the cap and the same sentence gave one back rather than taking a waiver.
- **Item C ruled, open two days** (`verdicts/2026-09-29-ed05-dateline-convention-ruling.md`):
  **keep the compose datelines, all six.** Not on blast radius — that is a tiebreaker, not a reason.
  The dateline is the date we did the reading, and moving it to flip day would make every source
  look freshly checked on flip day. *A stale dateline understates our freshness; a moved one
  overstates our evidence.* #50 is not triggered; no slug, date field or derived artefact moves.
- **Ruling #75 and standing assertion 27, `qa_patch_queue`** — yesterday's forward question, tested
  before anything new was added, and it bit. A staged patch was wrong about **four** counts **43
  hours after the weekly review refreshed it**; `git apply --check` returned 0 on every day it was
  wrong. The queue is now gated. **And the durable fix is the change of mind:** the patch was
  re-staged to state **no count at all** and point at the derivation — 0 numeric claims, so it
  cannot go stale again. **27 assertions, 24 gating**, counted in both homes.
- **Growth: the edition became one connected graph.** Six rails, three pairings, both languages.
  Rows 5 and 6 went from **zero** held siblings to 1 and 2; every row now has an inbound and an
  outbound edge inside the wave. Twelve days early rather than in the flip commit. Write-up at
  `agents/growth/2026-09-29-the-edition-becomes-one-graph.md`.
- **Four counts moved at the point of filing** — §3's range, §3's heading, §1's count line and
  `CLAUDE.md`'s non-negotiable range — plus §1 rows 71–72 and §3 rows 75–76. Second run to execute
  the 09-27 four-count rule. Reconciled by counting rows: **76 §3 rows, 72 §1 rows.**

## Held, and why

- **The Verifier's verdict on Rwanda.** Next run, one per run in banking order, into a backlog of
  zero. It is the edition's **last owed production cell**.
- **Clock items A and B**, now **nine days** open, and both still need a judgment rather than a
  task. Item A needs a served register for the August 2026 Zambian election, which this operation
  has never read. Item B's disposition is now **coupled to today's dateline ruling** — the same
  sentence's two halves — so it is one edit, not two, and should not be closed as two.
- **The fifth wave-packet entry.** Still composes from a dek the Editor had not read until today; it
  is now readable, and it is tomorrow's or the next run's.
- **The font self-hosting work.** Routed 09-26, deliberately not started for a **fourth** day. Two
  of five families are Arabic and a font swap is exactly what the three Arabic assertions exist to
  catch. It needs a run of its own, and saying so a fourth time is more honest than half-doing it.

## Named rather than absorbed

- **Three defects in my own new assertion, all found before it shipped**, and all three the same
  family as the three the 09-28 run reported. It flagged the README's deliberate record of a *past*
  wrong number as a live claim — the 09-14 masking trap inside the instrument built to catch it. Its
  silent-pass guard, copied from `qa_census`, **failed the tree for being correct**, because ruling
  #75 makes an empty queue the goal. And a lookbehind added to stop one misreading invited the next
  one in the same edit. Limbs recorded: *a check whose population can legitimately be empty cannot
  use "found nothing" as its failure signal; it needs a fixture*, and *a negative lookbehind
  constrains one starting position, not the match.*
- **Yesterday's reported tokenizer defect reproduced itself on me within the hour.** Establishing
  ground truth I wrote `qa_[a-z_]+`, got 11 build steps instead of 12, in the same direction, for
  the same reason — that class cannot match `qa_a11y_lang`. It is now an assertion inside the tool
  rather than a lesson in a log.
- **The founder-facing artefact had drifted, and only the render found it.** The 09-27 and 09-28
  briefs both carry the **09-26 brief's `<title>` and `<meta description>`** — his browser tab said
  *26 September* while he read the 27th and the 28th. Both corrected. Scope bounded by checking: the
  footers were right in all six briefs 09-23 → 09-28. **And I introduced a third instance today** —
  copying yesterday's tail carried its footer, *visible to the reader*, into this brief. Parsing
  found nothing; looking at the picture found it. Fixed. Also remapped ten item labels from
  `status-ok/warn/hold`, which the stylesheet does not define, to the vocabulary it does — the
  colour signal has been silently absent.
- **The brief-integrity check is named and deliberately NOT built.** One assertion per run is
  already delivered; a second on the same day gets a skimped proof. Four of its five values are
  derivable from the filename.
- **`qa_sources_alive` was not run as a sweep**, second day, and **bet item 2 is still not done.**
  It matters for flip day because the ledger makes that sweep the last step before the flip commit.
  Partial mitigation, stated as partial: all eight of row 6's URLs were probed individually *with
  TLS verification* at the pair verdict, which is how ruling #76 happened.

## Queued — next run

1. **The Verifier's verdict on Rwanda.** Closes the edition's last owed production cell.
2. **Clock items A and B**, as the two remaining judgments. B is one edit with today's dateline
   ruling; A needs a register opened for the Zambian election before anything is re-tensed — and
   composing one from what a model remembers of Zambian electoral law is a figure composed from a
   pattern (#41).
3. **Tomorrow's named QA question:** assertion 27 is the only one of twenty-seven that proves it can
   still read correctly *before* it judges anything. The other twenty-six were each proved once, by
   a bite then thrown away. **A bite run once is a claim about the day it ran; a fixture is a claim
   about every day since.** Which of the twenty-six can have its original proof frozen into a
   permanent self-test, and which is cheapest first?

## Owed, carried

The output-bounded `lastmod` manifest (twelfth time). The absence register. The coverage map, owed
four times. Bet item 2. The brief-integrity assertion named above. The serving-state-date row on the
Verifier's trace (#76's forward surface).

**Twelve days to the 10-11 gate target. Six drafted, six composed, six banked, five verified,
verification backlog zero, and the rail graph closed.**
