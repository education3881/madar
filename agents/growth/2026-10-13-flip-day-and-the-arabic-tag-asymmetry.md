# Flip day — what the packet can and cannot do today, and the Arabic tag asymmetry decided

**2026-10-13 · Growth · the day Edition 05 reached `origin`**

## 1 · The flip-day checklist, run as far as it can be run

The packet's own checklist (`social-drafts/2026-08-31-ed05-wave-packet.md`, step 1) requires **wave
gate flipped, deploy green, `verify` byte-compared** before anything else is even looked at.

- **Step 1 — half.** The gate is flipped and the twelve flags are on `origin` (commit `2ae8250`,
  pushed this morning). **No deploy has fired yet, and that is ruling #71 rather than a defect:**
  `madar-daily.yml` dispatches `astro-pages.yml` from a step that runs *after* the agent step, so the
  publication is still serving yesterday's bytes while this is written. Checked against the Actions
  API, not inferred.
- **Steps 2–4 — blocked, correctly.** Both URLs per piece returning 200 *from the origin* cannot be
  asserted before the deploy, and the packet's own rule is that nothing posts before origin-confirmed
  state. **Nothing posts today.** That is the 08-30 scheduling rule working, not a delay.

**Step 3's age is moved, which is the point of carrying the date:** the captions were last re-read
against the shipped text on **2026-10-12** — the Arabic gate that returned row 4 — and the repair
landed the same day, so the re-read's age is one day, the lowest it has been since 09-30.

## 2 · The Arabic tag asymmetry — DECIDED, and the decision is the growth-positive one

**The finding, carried from yesterday rather than settled in a run's tail:** of the packet's six
Arabic captions, **Egypt's carried three composed Arabic hashtags** (`#مصر #سياسات_التعليم #أفريقيا`)
and **the other five carried none**, while all six English captions carried three each.

Three options were on the table and only one survives contact with what this publication is:

1. **Strike Egypt's three and carry none in Arabic.** Symmetrical and cheap — and it throws away the
   only discovery instrument the Arabic edition has on the channels we will post to. Arabic
   discoverability is the reason the Arabic edition is a distribution advantage and not a translation
   cost (CHARTER). Rejected.
2. **Transliterate the English sets.** Rejected on the same ground the editorial side rejects
   translation: a tag is read by Arabic-speaking readers searching in Arabic, and `#Zambia` on an
   Arabic caption is addressed to nobody.
3. **Compose Arabic tags for all six, following the pattern Egypt's own caption already set** —
   country · subject · `#أفريقيا`. **Taken.**

Composed today for the five that lacked them:

| Piece | Arabic tags |
|---|---|
| Zambia | `#زامبيا #سياسات_التعليم #أفريقيا` |
| Sierra Leone | `#سيراليون #تمويل_التعليم #أفريقيا` |
| Sudan | `#السودان #التعليم_في_الطوارئ #أفريقيا` |
| The ruler piece | `#أفريقيا #بيانات_التعليم #التقييم` |
| Rwanda | `#رواندا #المعلمون #أفريقيا` |

`qa_packet_figures` re-run and CLEAN — tags carry no numerals, so the gate that reads captions is
unaffected, and it says so rather than being assumed to.

**What is owed and is named rather than skipped: the Arabic Editor's sign-off on the five tag sets.**
These are channel metadata rather than prose, and no reader can see them before the first post, which
is itself blocked on a green `verify` — so the sequence is sound. But a tag is Arabic that this
operation will publish, and *the Arabic Editor gates Arabic*. It is on the next run's list, ahead of
any posting.

## 3 · The reader-visible item this flip does not fix

**Standing-queue item 5 — five dead citations on four already-published pieces**, eight live pages,
displaced a third time today. Edition 05 adds twelve pages to the publication and none of them carries
a dead link; the eight that do are older. Naming it here because a flip day is exactly when a growth
note is tempted to report only what shipped.

## 4 · No traffic figure appears here and none can

The site carries no third-party tracker by design. There is no visitor number, no impression count and
no estimate standing in for one. What this operation can read without anyone's permission is its own
served bytes — and as of today it can read **all** of them: `qa_served_manifest --audit-origin` checked
256 of 256 published claims against the origin this morning. That is the only kind of number this note
is allowed to lead with, and it is a number about the publication rather than about its readers.

— Growth · 2026-10-13
