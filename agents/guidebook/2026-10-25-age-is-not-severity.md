# Ruling #116 — Age is not severity, and the queue's two keys were one key

**Filed:** 2026-10-25, weekly review.
**Family:** operating-cost family (named 2026-10-11), its **FIFTH** member — and the first whose
subject is not a *run's* boundary but a *rule's* throughput.
**Kin, deliberately not reassigned:** **#70** (*a check's bucket set is an enumeration too, and
cannot report a distinction it cannot hold*). Limb 1 below is #70 said about a **sort key** instead
of a bucket set, and it belongs there by shape. It is counted here because what it measures is the
price of a rule this operation wrote for itself, which is this family's whole subject.

---

## What was found

The standing queue (`agents/logs/WEBDEV-QUEUE.md`) has been ordered since 2026-10-04 by the
*one queue, one head* rule: the previous run's forward question enters at the head; **an item
displaced from the head three times goes first regardless**; the run writes one line naming which
head it took and what it displaced. Nineteen of the last twenty daily selections were made by that
rule rather than by judgment, and the queue says so with justified pride.

Three things are true about it this morning, and all three were measured rather than argued.

### Limb 1 — the tiebreak has four rungs and two of them are the same rung

The ladder, as built: **(1)** displacement count, **(2)** age in days (10-05), **(3)** the 10-11
ANSWER 1 narrowing, which separates on displacements again, **(4)** raise order within a shared
raising commit (10-16, whose author called it *the last the artefacts can support*).

**Over all eighteen open rows, the displacement count equals the age in days. Exactly. Every row.**

| item | raised | age (days) | displacements the prose maintains |
|---|---|---|---|
| 21 | 2026-10-17 | 8 | 8 |
| 22 · 25 · 26 | 2026-10-18 | 7 | 7 each |
| 27 · 28 | 2026-10-19 | 6 | 6 each |
| 29 | 2026-10-20 | 5 | 5 |
| 31 · 32 | 2026-10-21 | 4 | 4 each |
| 33 · 34 | 2026-10-22 | 3 | 3 each |
| 35 · 36 · 37 | 2026-10-23 | 2 | 2 each |
| 38 | 2026-10-24 | 1 | 1 |
| 39 · 40 · 41 | 2026-10-25 | 0 | 0 each |

This is not a coincidence and it is not a theorem. **It is an identity that holds whenever there is
exactly one head selection per day and the item was never taken** — which describes every day since
the rule was written, because the operation has had no dark day since 2026-10-04. The two numbers
can only diverge on a dark day, on a day with two selections, or on an item closed and reopened.
None has occurred.

So the ladder's first three rungs are one rung wearing three labels, and **this morning's selection
reached rung four for the first time** — items 20 and 21 tied at 8 days, the ANSWER 1 narrowing was
applied and *also* returned a tie at seven displacements each, and the decision fell to raise order.
It had to. A second key that is a copy of the first cannot break a tie the first did not break.

### Limb 2 — the one real key cannot see a reader, and cannot see a wall

Age orders eighteen rows into one line. It is blind to the two distinctions that decide whether
taking the head is worth a day:

**(a) A served defect and a question are the same height.** Four of the eighteen open items name a
non-zero count of artefacts that are **wrong right now**, in bytes a reader or the founder is being
served:

- **item 25** — 78 future-dated claims served across 22 of 44 EN pieces and 19 of 44 AR, none ever
  re-read against the calendar (raised 10-18, age 7);
- **item 27** — 25 founder-facing artefacts render broken, **7 of them 7,277 to 34,254 px wider than
  the viewport**, unseen for 62 days in the one artefact the CHARTER names as the proof-of-work
  contract (raised 10-19, age 6);
- **item 33** — three published citations misquote their own registers and a fourth is unreadable
  (raised 10-22, age 3);
- **item 35** — **4 of 15 acronym expansions in the served corpus have no evidence in their own
  annotations** — re-measured by `qa_acronym_evidence` during this review, and one of the four is on
  the piece that earned #101 (raised 10-23, age 2).

The other twelve are questions, coverage gaps and face judgments — all worth doing, none of them a
byte that is currently false. **In nineteen consecutive rule-made selections, not one head has been
a served defect**, because a defect our instruments found yesterday is by construction newer than
every question they asked last week. Item 35 is eleventh in line.

**(b) A blocked item ages like any other and will take a head it cannot vacate.** Two open items
cannot be closed by anyone in this operation: **item 22** (the turn axis; its remedy has been staged
at `agents/patches/2026-10-11-run-envelope-and-checkpoints.md` since 10-11 and needs the
`workflows` permission of **issue #7**, open 35 days) and **item 32** (archive submissions, awaiting
**issue #12**). On the age rule, **item 22 reaches the head on 2026-10-27** — where the run must
either spend the day on work it cannot finish or break the streak by judgment. The CHARTER already
rules on this exact shape one desk over: *a bet whose outcome the operation does not own is a
request, not a bet.* **An item whose closure the operation does not own is a request too, and a
request must not be able to occupy a head somebody is obliged to take.**

### Limb 3 — the ceiling the threshold was chosen to enforce is breached on 2026-11-25

The 10-04 rule chose three displacements because it is *"short enough that nothing reaches 28 days."*
Today the oldest item is 8 days and the Assertions Engineer's restraint test passed on that number
(8 against 28, down 20). **That is a snapshot on a rising curve.**

Measured over 2026-10-19 → 2026-10-25: **15 items raised, 10 closed, board 13 → 18.** Raise rate
2.14/day, closure rate 1.43/day, net +0.71/day. Under oldest-first, a new item waits for everything
ahead of it, so the oldest age converges on `board ÷ closure rate`:

```
board(t)      = 18 + 0.71 t
oldest age(t) = board(t) / 1.43
28 days  ⇒  18 + 0.71 t = 40  ⇒  t ≈ 31 days  ⇒  2026-11-25
```

The threshold does not hold the ceiling. **The closure rate holds the ceiling, and the threshold
only decides who waits.** Nothing in the 10-04 rule is wrong about starvation at the tail; what it
got wrong is believing a displacement counter bounds an age when the board is growing.

---

## Why nobody caught it, and it is the same reason as last time

The row-level **Age** and **Displaced** columns stopped being maintained after 2026-10-22. **Fifteen
of eighteen rows arrived at this review understating their own age by one to three days**, under a
section header reading *"ages to 2026-10-25"* — rewritten that morning, correctly, by the run whose
prose computed item 21 at 8 days and then left the cell below it reading 5.

That is **limb 3 of the 10-04 second amendment** — *a count incremented beside a list that was not
appended to* — for the fourth and fifth time in eight days, and this time **in the file whose head
is binding and whose sort key is the number that went stale.** The 10-18 review found the same shape
three times in one week in three files. Escalating diligence has now failed on it four weeks running.

**And the fix is not diligence, because the number is derivable.** Age = today − Raised, and Raised
is already in the row. Displacements = the same number, by limb 1. The queue was hand-keeping two
copies of one computable quantity in eighteen rows — thirty-six hand-written numbers, all of them
derived from a date sitting three cells to the left. #75's rule applies verbatim: *a number that
lives in several files should be derived from them, never copied into a fourth.*

---

## The rule

**(1) Drop both derived columns.** The queue's rows carry **Raised** and nothing else about time.
Age is `today − Raised`, computed by the run that needs it — which is what every selection has
actually done in prose. The displacement count is deleted outright: it is age, and the tiebreak rungs
that read it are deleted with it. **The ladder is now two rungs: age, then raise order.**

**(2) Three buckets, and only one of them is ordered by age.**

- **BLOCKED** — closure needs a credential, a purchase or a word nobody in this operation holds.
  Carried in its own block with the blocker named by issue number and its age printed. **It never
  enters the head ordering** and is re-read at the weekly review, not by the daily.
- **DEFECT** — the row names **N > 0 artefacts, currently served or currently founder-facing, that
  are wrong, broken or unevidenced.** The boundary is supplied by the artefact and not by judgment:
  a defect carries a count of defective things that exist; a question carries no such count, because
  the count is what it would measure. Coverage gaps and efficiency findings are not defects — the
  bytes are right, and the row says so.
- **OPEN** — everything else: questions, gaps, face judgments. Ordered by age exactly as now.

**(3) The head is the oldest DEFECT if any DEFECT is open; otherwise the oldest OPEN.** The forward
question still enters at the head of OPEN, and the three-displacement threshold is retired, having
been a second name for age throughout its life.

**(4) The bucket is written in the row by the run that raises it**, and the weekly review reconciles
the three bucket counts against the rows — never against last week's numbers (#57).

**(5) The review prints the closure and raise rates and the implied date at which the oldest item
reaches 28 days.** One line. It is the only number that says whether the ordering is a schedule or a
queue, and the threshold clause was carrying that claim without any arithmetic behind it.

---

## The general form

**An ordering rule can express only the distinctions its keys can hold — so count the keys, and
check that they are not one key.** A tiebreak ladder reads as four independent discriminators and
cost nothing to add, which is exactly why nobody asked whether rung two was a function of rung one.
And a single key, however fair, converts every property it cannot see into a property nobody is
ranked on: this queue could not see *a reader is being served a false sentence*, so for nineteen
selections nobody was.

The further half, which is the one to carry: **a throughput rule's guarantee is a claim about a
rate, and it must be stated as one.** *Nothing reaches 28 days* is checkable arithmetic about two
measurable rates, and it was written as a property of a counter. The counter was honest; the claim
was never tested against the two numbers that decide it.

---

## Measured, and recorded because the measurements are the ruling

- Displacement ≡ age on **18 of 18** open rows.
- Stale Age cells on arrival: **15 of 18**, every one understated, by 1 to 3 days, under a header
  claiming *ages to 2026-10-25*.
- Served/founder-facing defect items: **4 of 18** (25, 27, 33, 35). Heads they have taken in the
  rule's 19 selections: **0**.
- Blocked items: **2 of 18** (22 → issue #7 at 35 days, 32 → issue #12 at 1 day). Head arrival of
  item 22 on the retired rule: **2026-10-27**.
- Week 10-19 → 10-25: **15 raised, 10 closed**, board **13 → 18**. Implied 28-day breach
  **2026-11-25**.
- `qa_acronym_evidence` re-run during this review: **15 anchored expansions, 11 evidenced, 4 not** —
  unchanged since 10-23, which is what makes item 35 a defect rather than a measurement.

## What this does not claim

It does not claim the board should be smaller. Fifteen raises in a week is five standing assertions
finding things, and a queue that grows because the instruments work is not a defect — **#115 alone
opened three rows.** It does not claim anybody was slow: 10 closures in 7 days is this operation's
best week on that number. And it does not claim a thirteenth persona would help. The raise rate is
generated by the instruments, so a desk that builds instruments raises it; that is the 09-27 split's
own finding, and the fix here is the same shape as the fix there — **a rule, not a role.**
