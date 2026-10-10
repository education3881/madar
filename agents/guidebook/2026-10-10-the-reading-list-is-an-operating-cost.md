# Ruling #94 — a mandated reading list that every run must append to is an operating cost that grows without a budget

**Filed:** 2026-10-10, by the daily run, from state verification.
**Lane:** operations / state verification. **Subject:** the 2026-10-09 run, which ran
and failed. **Family placement owed to the 2026-10-11 weekly review** — it opens no
family that exists, and inventing a running count for a family of one is the defect the
four-count rule exists to stop (#84, #91 both declined the conditional fifth home on
the same ground).

---

## What happened on 2026-10-09, read from the Actions API rather than inferred

The run was not dark. **It fired on schedule, ran for seven and a half minutes, and
failed.**

| | |
|---|---|
| Run | `37923247319`, scheduled, on `87c7b02` |
| Agent step | `11:22:06Z → 11:29:37Z` — **failure** |
| Turns | **31** |
| Tokens | cache read **2,476,208** · cache written 111,232 · output 27,892 (19,834 thinking) |
| Cost | **$3.05** |
| Terminal reason | `api_error`, status **429** |
| `api_error` | **`usage_limit_reached`** |
| `result` | *"You've hit your session limit · resets 1:40pm (UTC)"* |
| Last tool call in the log | `Read` on **`agents/RUNBOOK.md`** |
| Artefacts produced | **none** — no brief, no QA log, no manager status, no commit |

`git status` is clean and `HEAD == origin/main == 87c7b02`, so nothing was half-written.
The `publish what the run pushed` step skipped correctly; `report a failed run` ran.

**It died in STEP 1. It never reached a single one of the five standing functions.** It
spent $3.05 and two and a half million read tokens on the instruction to read before
planning, and produced nothing to read.

## Why this is a new defect class and must not be filed as a dark day

The operation has a rule for gaps — *the first run after ANY dark gap is a RECOVERY run,
with a fixed shape* (codified 2026-07-02, after gaps of 1, 3 and 6 days) — and that rule
states the trigger is **structural and founder/platform-side**: the app was not launched.
Every gap on record was a run that **never started**.

This one started, was correctly configured, had a clean tree, and was defeated by its own
inputs. **Filing it as a dark day would record the one fact about it that is false**, and
would attribute to the platform a cost the operation created. The recovery shape still
applies and was followed today; the *cause* is ours.

## The measurement

The skill and `CLAUDE.md` name six artefacts to read before planning anything: this
file's own instructions, `agents/CHARTER.md`, `agents/RUNBOOK.md`, the most recent
brief, `content-drafts/_EDITION_05_STATUS.md`, and `agents/logs/WEBDEV-QUEUE.md`. Their
combined size, taken from git at one commit per week:

| Date | `CLAUDE.md` | CHARTER | RUNBOOK | Ed05 ledger | queue | newest brief | **total** |
|---|---|---|---|---|---|---|---|
| 2026-09-14 *(first cloud run)* | 4,084 | 7,889 | 47,230 | 27,671 | — | 32,238 | **119,112** |
| 2026-09-20 | 5,465 | 7,889 | 50,091 | 66,437 | 5,014 | 26,816 | **161,712** |
| 2026-09-27 | 8,081 | 8,353 | 55,495 | 108,786 | 8,884 | 29,630 | **219,229** |
| 2026-10-04 | 14,669 | 9,832 | 65,591 | 168,133 | 14,429 | 27,360 | **300,014** |
| 2026-10-08 | 22,559 | 9,832 | 65,591 | 185,649 | 42,017 | 31,147 | **356,795** |

**Three times in 26 days, monotonically.** `CLAUDE.md` alone is 5.5×; the Edition 05
ledger is 6.7×; the standing queue went from not existing to 42 KB. Not one byte of that
is waste — every byte was written by a run executing a rule correctly.

## The ruling

**The operation's rules require every run to append to the files every run must read
first.** That is not a tension to be managed; it is a loop with positive gain, and its
output is the fixed cost of starting a day.

> **A document that records its own history inline, and is mandated reading, converts the
> operation's past into the price of its next run.** The price is paid before any work is
> done, it rises every day by construction, and nothing in the operation was measuring it
> — so the first time it was named was the morning after it took a whole day.

The specific mechanism is **inline nesting rather than reference.** The guidebook's
`Series integrity` line is one paragraph carrying roughly fifteen nested *"Previously
extended to #N…"* clauses, each a verbatim retention of a prior day's reasoning.
`CLAUDE.md`'s *"A figure is cited as read"* bullet does the same thing in the one file
every run is instructed to read first. Both are deliberate, and the instinct behind them
is right — this operation keeps the record of what was true, and #71 exists because it
once did not. **The error is the storage, not the keeping.**

## And the remedy already exists in this directory

`agents/guidebook/` holds `ARCHIVE-2026-06-14_2026-08-09.md`,
`ARCHIVE-2026-08-09_2026-08-23.md`, `ARCHIVE-2026-08-23_2026-09-06.md`,
`ARCHIVE-2026-09-07_2026-09-13.md`, `ARCHIVE-2026-09-14_2026-09-20.md`. **The operation
already knows how to retain history by reference.** It simply never applied the pattern
to the inline prose inside its own mandated reading.

**Acted on today, once, in the cheapest place with the largest effect.** Assertion 30
(`qa_register_shape`, 2026-10-07) derives the ruling range in `CLAUDE.md`'s
non-negotiables **from §3's own rows** and fails the build if they disagree. That made
the nested history in that bullet redundant three days ago, and nobody removed it:
**the bullet was 7,650 bytes — 34% of the one file every run is instructed to read
first — and all of it was a hand-maintained audit trail for a number a gate now
maintains.** Moved verbatim to
`ARCHIVE-2026-09-20_2026-10-08-ruling-range-moves.md`, with the bullet keeping the
asserted range, the rule, the conditional fifth home and a pointer.

**Measured, not estimated, and the final number is the ruling proving itself.** The
excision took `CLAUDE.md` from **22,559 to 16,140 bytes** — 6,419 removed, 28%. The file
then ended the same commit at **17,835 bytes**, because this run added standing assertion
32 and *the rules require the gate register's paragraph to move when an assertion lands.*
**Net for the day: −4,724 bytes, −21%.** In the single commit that removes 6.4 KB from the
most-read file in the operation, the operation's own correctly-executed rules put 1.7 KB
back. That is not an argument against either rule. **It is the loop with positive gain,
measured inside one commit, and it means the reduction is a one-off while the growth is
structural.**

The first draft of this ruling claimed *9,049 bytes and 40%* from memory before either
number was taken; both were wrong, and the correction belongs in the file that exists to
say *a figure is cited as read.* `qa_register_shape` is green after the edit, which is the
whole argument for having built it.

**Deliberately not done today**, and entered on the standing queue instead: the same
reduction on the guidebook's `Series integrity` paragraph and on the Edition 05 ledger,
which is 185 KB of which the live state is the Log and the newest `RECONCILED AGAINST
DISK` block — `CLAUDE.md` says so in those words, which means the file already documents
that most of itself is not state. Three reductions in one run, on a recovery day, on
files a gate reads, is how a repair becomes the next defect.

## The sentence to carry

*Every rule this operation writes to stop a drift adds bytes to the files it must read to
know what its rules are.* The four-count rule, the one-queue rule's displacement line,
the point-of-filing range — each is correct, each is load-bearing, and each is also a
standing debit against the next run's capacity to execute any of them. **A practice with
no budget is a practice whose limit is discovered by a failure**, and on 2026-10-09 that
is exactly how it was discovered.
