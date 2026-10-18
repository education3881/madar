# Ruling #107 — a trigger nobody is named to evaluate is a note, not a rule

**Filed** 2026-10-18, at the weekly review.
**Family** operating cost — the **fourth** member, and the first about the run's position in time rather
than its consumption of it.
**Measured over** all 38 scheduled runs of `madar-daily.yml` and `madar-weekly.yml` since the 2026-09-15
cron offset change, read from the Actions API.

---

## The rule, in one line

**A rule written as a condition — *if X is still true, do Y* — is evaluated by nobody unless somebody is
named and the measurement is cheap.** The 09-20 rule says *a count in a heading is maintained by nobody
unless somebody is named*; a **condition** is worse than a count, because a stale count at least looks
wrong when you read it, while an unevaluated condition looks exactly like diligence — the thinking is on
the page, the trigger is stated, and the inference was never made. **And a condition written in a file the
run cannot edit is addressed to a reader who never comes.**

## The instance

`madar-daily.yml`'s header, written 2026-09-15 when the cron was moved from `04:00` to `04:23`:

> It was 04:00 until 2026-09-15, when the first scheduled run landed roughly five and a half hours late.
> GitHub queues every repository's cron on the same minute together, and :00 of the hour is the most
> contended minute there is; an odd offset is the documented mitigation. **If a run is still hours late on
> this offset, the delay is not contention and the next step is to stop planning the day around the cron at
> all** (the 08-30 rule about a cadence the constraint does not support).

That paragraph is correct, complete and self-aware. It names the hypothesis, the mitigation, the
falsification condition and the consequence. **The condition has been true on every run since, and nobody
has ever evaluated it**, because:

- the text lives in `.github/workflows/**`, the one directory this identity is refused write access to, so
  no run has a reason to open the file;
- nothing anywhere else records a scheduled start time, so the delay was not in any artefact a run reads;
- and the mitigation *appeared* to have worked, because every run did eventually fire and every brief got
  written. **A symptom that does not get worse stops being read.**

### What the measurement says

| Workflow | Scheduled runs since 2026-09-15 | Earliest start after cron | Latest | Median |
|---|---|---|---|---|
| `madar-daily.yml` (cron `23 4 * * *`) | 33 | **4 h 14 m** | **7 h 42 m** | **5 h 37 m** |
| `madar-weekly.yml` (cron `23 5 * * 0`) | 5 | **4 h 19 m** | **6 h 04 m** | **5 h 13 m** |

**38 of 38. Not one scheduled run in 33 days has started within four hours of its cron.** The offset change
did not help: the pre-change figure the header quotes is *roughly five and a half hours*, and the median
after it is 5 h 37 m. The hypothesis the odd offset was chosen on is falsified by its own data, and the
instruction attached to that falsification was never read.

### What it cost, concretely

- **The CHARTER's cadence table has said `~08:00 Asia/Dubai` for the daily and `Sun 09:00` for the weekly
  since 2026-06-03** — the first document every session reads. The cron is 08:23 and 09:23 Dubai, and the
  measured median start is **≈ 14:00 and ≈ 14:36 Dubai**. The operation's day has begun in the afternoon
  for five weeks, in a table that says morning. This is the CHARTER's `(7)` headcount defect exactly, one
  table down.
- **This morning the daily run spent judgment on it and put it in the founder's brief.** The 10-18 brief
  records that *"the weekly review had not fired four hours past its cron and is named rather than
  absorbed"* — correct discipline, applied to **the single most normal event in the operation's history.**
  Naming a non-event costs a line in the brief and a paragraph of attention; worse, it spends the operation's
  alarm on the thing that never varies, which is how a real miss would come to look ordinary.
- It is also the reason the daily and the weekly can **never** be mistaken for each other's slot and nothing
  about the ordering is at risk: both drift together, and the one-hour cron gap has held in all five weeks.

## What was done

1. **The measurement moved onto the fast clock.** `run_envelope.py` now parses the `cron:` out of the same
   workflow file it already reads the two budget numbers from, computes the delay against the run's own
   `run_started_at`, and **prints it on every call**, with the measured band beside it so a 4-to-8-hour
   delay reads as *ordinary* rather than as a near-miss. A cron expression the parser cannot read prints
   **UNREAD**, never zero — this instrument refuses rather than remembering (#105).
2. **The CHARTER's cadence table now states the measured start window**, with its date, its method and its
   owner — the weekly review re-measures it, because a number with no named maintainer is the defect above.
3. **Nothing was planned on the cron.** The 08-30 rule's instruction — *stop planning the day around a
   cadence the constraint does not support* — is executed here rather than quoted: the cadence is *one run
   per day*, not *a run at 08:23*, and no artefact may assert a time of day it has not measured.

## Why it is in the operating-cost family

The family's subject is **the run itself, as a process with a boundary**. #94 measured the fixed price at
the front of a day, #96 the cliff at the back, #105 found half the envelope observable all along. **#107 is
the run's position in time rather than its consumption of it** — the same class of fact about the container,
discovered the same way: by one API call nobody had made. And it answers the family's standing question
(*which other rule of ours has a cost nobody has measured?*) for the second time in one day, which is itself
worth noticing: #105's answer was *the ruler*, and this one's is *the clock the ruler hangs on*.

## Proof — both ways (#35)

| # | Case | Expected | Got |
|---|---|---|---|
| 1 | this run, weekly cron, live `run_started_at` | 4.3 h, matching the API figure 259 min | **4.3 h** |
| 2 | daily cron, `--started-at 2026-10-18T08:53:10Z` | 4.5 h, computed independently | **4.5 h** |
| 3 | cron replaced with `*/5 * * * *` in a copied workflow | **UNREAD**, never a number | UNREAD |
| 4 | weekly cron, a **Tuesday** start instant | 51.6 h — the previous *Sunday*, not the previous day | **51.6 h** |

Case 4 is a bug this harness found rather than confirmed: the first draft rolled back one **day** and
ignored the cron's weekday field, so a late weekly would have been measured against a Monday 05:23 that is
not a cron instant at all. A wrong number is worse than an unread one from an instrument whose whole claim
is that it refuses.

## Kin

* **#105** — *a constant is not a measurement*. Same morning, same file, adjacent defect: there a number was
  recorded and the question retired; here an inference was written and never drawn.
* **The 09-20 rule** — *a count in a heading is maintained by nobody unless somebody is named.* This is that
  rule with a condition in place of a count.
* **The 08-30 rule** — *plan as if the guaranteed window is weekly.* Its own instruction, finally executed.
* **Standing-queue item 24** (*which of our rules has never been tested against the world it claims about?*)
  — this is that question's answer taken at the head, by the review, with the measurement attached.
