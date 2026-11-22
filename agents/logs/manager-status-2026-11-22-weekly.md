# Manager status — 2026-11-22 (weekly review)

**Run:** `madar-weekly.yml`, autonomous, no founder in the loop. Started 13:26Z, 8.1 h after its cron —
inside the derived band (77 scheduled runs, 4.23–9.16 h, median 6.27 h, zero inside four hours), so not a
missed run and not anybody's fault (#107).
**State verified before planning, not from a brief:** on arrival `HEAD = 9a2f10c = origin/main`, tree
clean, nothing ahead or behind; today's deploy green on that SHA at 13:22Z with build, deploy and verify
all green; live origin re-read directly, home and sitemap both 200.

## What this review found and did, in order

1. **The week counted.** 7 of 7 runs, 7 briefs, 46 commits, 1 piece shipped, 0 held, 6 green deploys in
   seven days. **One run died at the turn cap (11-21, 181 turns in 43 of 90 minutes) — the fifth ever —
   and it cost a day of PUBLICATION rather than a day of work.** All five function commits were banked;
   step 9 `publish what the run pushed` carries `if: success()` and was skipped, so both editions of the
   piece that shipped returned 404 all day while brief 137 said it had shipped. **#96's guarantee ends at
   `origin`; the reader is one step further out.**
2. **`CLAUDE.md` corrected for the third time in fourteen days** — FOUR cap deaths over 55 rows against a
   true FIVE over 58. The derived figures beside it did not move, for the first time.
3. **Queue reconciled against its rows.** Board 81 on arrival (0 / 77 / 4) against a section heading
   reading EIGHTY. **The raise and closure rates this file printed at its last two reviews were derived by
   a method that balances by construction**, and items 135–138 never existed, so the published rates were
   overstated by 14% and 29%. True figures: **28 raised, 14 closed, net +14.**
4. **The fourth bucket scheduled for today is DECLINED**, on the measurement: 82 OPEN rows, zero past 28
   days, median 12 — the board has no tail, and a bucket keyed on *intention* has no observable key and
   would be filled by the run the age measures. Trigger for reversal written down: a tail.
5. **Guidebook consolidated.** Register true on arrival for the tenth and eleventh weeks; ten rulings
   #145–#154, ten for ten; 174 file references and 33 links, zero unresolved; 11-08 section rolled to
   archive. **Two rulings filed: #155** (the owed one — a composed name reads exactly like a quoted one)
   and **#156** (a coverage count is not a coverage list — `qa_register_shape` limb 3 reads two of nine
   families and reports the other seven as a smaller number).
6. **Ledger reconciled true on arrival.** 46 EN / 46 AR, parity 100%, zero held, cell 1 of eight on the
   in-flight single. **The forward-date mandate found nothing in its own window** — all 17 in-window dates
   are our own provenance timestamps — **and the corpus-wide sweep found one unshielded editorial future
   whose target carries no date at all**, which is why a date-keyed window never reached it. Repaired in
   both editions; world-read and rescope queued.
7. **The bet read on its due date** over 143 documents instead of six: 3,989,640 bytes in 54 fetches on 48
   of 143 pages paint fewer than five characters, 7.3% of the corpus payload; worst page
   `/browse/region/europe/` at 195,168 bytes. **Zero dead fetches on the whole population — limb 2 of
   assertion 39 confirmed beyond its sample for the first time.** The bet's denominator was stale and its
   technique (`DOMParser`) could not have worked.
8. **Gate ratio: 40 of 43**, derived. One assertion added this week (43, `qa_emitted_dates`). All 12
   build-job gates green locally in 1.9 s. Patch queue re-read: **eight** patches, zero numeric claims,
   both `.patch` files apply — and the *nine staged patches* two previous reviews wrote was the tool's
   file count including its own README.
9. **Team expansion: HELD at twelve.** No ladder rung fires. The Assertions Engineer's restraint test was
   re-read rather than left at its dated pass, **is failing on its own terms (8 → 25 days)**, and fold-back
   is declined because the number is a property of the board's arithmetic and not of the role. Test
   replaced with the **OPEN-head closure rate**, 0.86/day this week; fold-back below 0.5/day for two
   consecutive weeks with an empty DEFECT bucket. Next evaluation 2026-11-29.
10. **Review document** at `agents/reviews/2026-11-22-weekly-review.html`, stylesheet inherited from the
    11-15 file so item 144's mobile repair carries forward. `qa_artefact_render` **164 of 164 at 1280px
    and 328 of 328 renders at both widths**, this document included. `qa_brief_head` CLEAN across 140
    briefs and 23 reviews.

## Held, and why

Nothing editorial was held. **One ruling is deliberately not filed** — #117's selector cannot reach an
undated editorial future — and is recorded as owed to the 2026-11-29 consolidation with its queue row
(155) beside it, because a ruling written in the last twenty minutes of an envelope is a ruling nobody
re-reads.

## Queued for the week

- **Tomorrow's head: item 48** at 26 days, tied with item 50 on the same `Raised` cell. **Both reach 28
  days on 2026-11-25**, so the next three days need one OPEN-head closure each.
- Board closes at **86**: 0 DEFECT, 82 OPEN, 4 BLOCKED. This review closed one row and raised six, and
  says so rather than netting it off.
- **Next week's bet (item 151):** cut the chrome's font cost, re-read the committed register on 2026-11-29,
  target zero for the 22-page `/browse/country/` class.
- Five founder questions open and carried by name: **#7 (63 days), #8 (49), #11 (38), #12 (29), #13 (28)**.
  No sixth raised — nothing this week needed a decision only he can make that is not already on that list.
