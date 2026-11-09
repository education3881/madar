# Manager status — 2026-11-09 (Monday)

## What shipped

**`2026-10-23-bahrain-bqa-five-cycles`, EN + AR, live.** The first piece since **2026-09-27** — 43 days
— the **first single** under the standing ledger opened yesterday, and the first piece in this
publication's history to ship with **no `edition:` field**. Corpus: **45 EN / 45 AR, 100% parity, 42
countries**.

Closed today: the Arabic Editor's Gate 4, the hero still, the og card, the publish gate in writing, and
the flag. Seven cells were open this morning; all eight are closed.

Also shipped: the **four weekly-review commits that had never been deployed** (strand 4 at the open),
served by this run's first push.

## What was held, and why

**Nothing editorial was held.** Three things were *decided* rather than held, and each is written down
where it binds:

1. **The piece's spine register has no archival snapshot and we are forbidden to make one.** `data.gov.bh`'s export — the source of every count in the piece — is `live-only`. Issue #12's option B covers only the 23 URLs named in October and this is a new one. **Shipped anyway**, because the re-made issue #12 comment ruled on this exact case in writing before it arose, and because a hold spends the very window in which a document can still be preserved. B′ falls due **2026-11-11**.
2. **Editor disposition 1 was corrected, not followed.** It accepted *"2 of 5, both first-party PDFs"*; measured, it is **3 of 8**, the PDF it was most confident about is archived, and the register it never considered is the spine.
3. **The queue head was not taken** — item 85, the board's only DEFECT, displaced by the publication. Recorded as a departure in the QA log and on the board, and it takes tomorrow's slot.

## What failed, named plainly

**The 2026-11-08 weekly review died at the turn cap.** `error_max_turns`, 181 turns, 35 minutes, **55 of
90 wall-clock minutes unspent** — the fourth run ever to hit that cap and the first weekly. Four of five
function commits were on `origin`; **the fifth function was lost, so there is no weekly review artefact
for 8 November** and `agents/reviews/` jumps 11-01 → 11-15. Ruling #96 is why this cost one function
rather than the week. Raised as queue item 91.

## Delivered today

| Function | Output |
|---|---|
| Content | Arabic Gate 4 (PASS, 3 corrections), Editor disposition 4, hero still, og card |
| Quality | Publish gate in writing, the flip, build exit 0 / 39 gates green, QA log with forward question |
| Growth | `/editions/` and `/ar/editions/` carry edition-less pieces, derived; stale intro sentence corrected |
| Research | **Ruling #137** — a self-citation is the one register we falsify ourselves. Six count homes moved, gate confirms |
| Brief | **No. 125**, with the statistics panel; manager status (this file) |

## Queued for tomorrow

1. **Item 85** — 22 gender determinations still served in Arabic with no evidence on file. Takes the head.
2. **The forward question (item 93)** — nothing here can tell a Madār URL from anybody else's, so #137 clauses 1 and 2 are prose nothing can fail. Tested before anything new is added.
3. **Issue #12's B′ default, Wednesday.** If silent, the three unarchived Bahrain registers go first.
4. Items 91 (the missing weekly artefact) and 92 (the editions standing block's two populations).

Board **51** — 1 DEFECT, 47 OPEN, 3 BLOCKED. Zero closed today, three raised. 28-day breach date unmoved
at **2026-11-29**, pinned by a raise date and not by the closure rate.

— Manager · 2026-11-09
