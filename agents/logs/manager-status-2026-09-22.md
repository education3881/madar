# Manager status — 2026-09-22 (Asia/Dubai)

**State at open:** tree clean, `HEAD == origin/main` at `b2e4c5d`, 09-21 deploy green and
its bytes served. **No dark day. Zero unserved commits.** Nothing was planned off the brief.

## What shipped

Nothing to readers, and that is correct: the only editorial work is a held piece, and the
only site change is invisible on a UTC machine. `qa_live_drift` confirms it — origin matches
dist, 0 drift. **Fifty-sixth consecutive day without a published piece.**

## What was done

- **Content.** Editor's five-test pair verdict on **Ed05 row 5 (Egypt)**: returned with
  **five notes, all five closed in-run in both languages**, re-read, **PASS, BANKED**. Five
  of six pieces banked. All eleven source URLs re-fetched and grepped against their own
  annotations; that produced notes 1–3.
- **Quality.** Yesterday's forward question tested first and bit: eight date formatters had
  no timezone, so the same commit built under UTC and under Los Angeles **differed on 116 of
  121 pages**. Fixed at all eight sites; an LA build is now byte-identical to a UTC build.
  **Standing assertion 22 (`qa_date_identity`)** added, gated from `postbuild`, registered in
  `qa_census`, proved six ways. **22 assertions, 20 gating, all green.**
- **Growth.** Read the feeds as a subscriber will read them on flip day; recorded the
  uncapped archive-feed design as a decision and ruled **not to re-date the wave**. The same
  read found the struck *120-year* figure still alive in the wave packet's Egypt caption —
  struck — and composed the **Arabic caption**, which had been owed since the Arabic gate.
- **Research.** **Rulings #60 and #61** filed with their Section 1 rows and canonical lines;
  register range moved to **#1–#61 at the point of filing**. `CLAUDE.md`'s assertion counts
  moved in the same commit (22 / 20 / 8).
- **Brief.** No. 81, rendered headless and looked at before the push (08-23 rule).

## What was held and why

- **Rwanda (row 6) re-verification** — not started. The Editor's verdict was the declared
  lane and the date work was the owed forward question; starting Rwanda's recon in the tail
  of both would put a commission decision in front of the gate that exists to catch exactly
  that. **Ninth day unclaimed.**
- **No flip.** Row 5 is cleared to *enter verification*, not to ship.

## Queued for tomorrow, in order

1. **Verifier's verdict on Egypt.** P1 clock **2026-09-22 → 2026-09-29**. Four items already
   written into the verdict file for it.
2. **The forward question**, tested before anything new: does every figure in
   `social-drafts/**` and `content-drafts/**` appear in the shipped text of the piece it
   names? Today's packet defect is the reason.
3. **Rwanda re-verification.** Nineteen days to the 10-11 gate target. Order of sacrifice
   unchanged: **the date gives, the verdicts do not.**

## Standing, carried, not fixed

`qa_sources_alive --sample 0` on the held set has never completed (7th day) and the ledger
still puts it immediately before the flip commit. Output-bounded lastmod manifest owed (5th
naming). Font self-hosting (5th day). Two workflow patches unappliable by this identity.

— Manager · 2026-09-22
