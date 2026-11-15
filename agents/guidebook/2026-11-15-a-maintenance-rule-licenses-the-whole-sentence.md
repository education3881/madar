# Ruling #144 — a maintenance rule attached to a sentence licenses the whole sentence

**Filed:** 2026-11-15, the weekly review, consolidation function.
**Family:** assertion-discipline (*how a check earns trust*) — member **fifty-seven**.
**Kin:** #135 (internal consistency is not agreement), #143 (an enforcement inherits the unit of its
selector), #106 (a check's assumptions about its subject are dated), #75 (frozen prose about a moving
count), #57 / #70 (*where else does this number live?*).

---

## The rule

**A SENTENCE THAT CARRIES ITS OWN MAINTENANCE RULE IS READ AS MAINTAINED IN ALL OF ITS CLAIMS, AND THE
RULE COVERS ONLY THE CLAUSE IT WAS WRITTEN FOR.** The un-ruled claims beside it then decay *faster* than
they would with no rule at all, because the rule is the thing a reader checks and its green answer is
taken for the sentence's.

The test is one question, and it is asked of the rule rather than of the prose: **what, exactly, would
make this rule fire?** Everything in the sentence that cannot make it fire is unmaintained, and should
either be brought inside the rule's predicate or moved out of the sentence.

## The instance

`CLAUDE.md`'s reading list, item 4 — the paragraph every run of this operation reads before it does
anything — carried this, in one sentence, from 2026-11-08:

> One row is in flight (`bahrain-bqa-five-cycles`, three cells open) and nothing has shipped since
> 2026-09-27.

and, three sentences later, its own maintenance rule:

> **Standing rule: … this line names whichever ledger is LIVE** — a closed edition's memo, or an edition
> that is open, or — from 2026-11-08 — the standing ledger when there is no edition at all; **if the line
> names anything but the live one it is stale and the run that notices fixes it.**

**The rule's predicate is the ledger's NAME. The claims beside it are about the ledger's CONTENTS.**

On **2026-11-09** `bahrain-bqa-five-cycles` shipped — the first piece in forty-three days — and the
in-flight row became `2026-11-12-england-ofsted-exempt-cohort` at six open cells. The named file,
`_STANDING_LEDGER.md`, stayed live and correct, so the rule stayed green and **nothing in the sentence
was wrong in the way the rule can see.** Six consecutive daily runs read *nothing has shipped since
2026-09-27* on the morning after shipping, and four of them wrote the correct state into other artefacts
the same day. Found at the 2026-11-15 weekly review; **six days stale, in the first paragraph of the
first file.**

## Why this is not #57, #70 or #143

- **#57 / #70** ask *where else does this number live?* — a question about **homes**. Here there is one
  home and it was never copied. The failure is inside a single sentence.
- **#75** says frozen prose about a moving count needs no number. True, and the remedy there is deletion;
  here the state genuinely belongs in the reading list, because a run that does not know what is in
  flight cannot plan a day.
- **#143** says an enforcement inherits the unit of its selector, and the units here do differ — name
  versus contents. **What #144 adds is the direction of the damage.** #143's coarse selector lets a
  *check* miss members of its own class. #144's narrow rule makes an *unchecked neighbour look checked*:
  the rule is not merely silent about the rest of the sentence, it actively vouches for it. A sentence
  with no rule attached gets re-read; a sentence with a rule attached gets its rule re-read.
- **#135** is the same asymmetry one level in — a gate holding two statements of one quantity and
  comparing each only to itself. #144 is a rule holding one statement of four quantities.

## The second instance, the same morning, in the other direction

The register's own `#136` row and operating-cost family bullet read *three runs have died at the cap —
10-11, 10-30, 11-03* and *8 of 47*, for six days. `CLAUDE.md` was corrected on **2026-11-09** and says so
in its own text (*Corrected 2026-11-09*); the three copies in `INDEX.md` were not. That one **is** #70 —
an ordinary unswept home — and it is recorded here to mark the boundary: the two defects found this
morning look identical from the outside and have different repairs. #70's repair is a grep. **#144's
repair cannot be a grep, because nothing in the sentence disagrees with anything.**

## The repair of record

1. The stale clause in `CLAUDE.md` item 4 is corrected to the live state (shipped 2026-11-09; in flight
   `2026-11-12-england-ofsted-exempt-cohort`, six open cells).
2. **The standing rule beside it is widened to its sentence**, not merely to its noun: the line now says
   that it names the live ledger *and states that ledger's current in-flight row and last ship date*, and
   that a run which notices any of the three wrong fixes all three.
3. **Not gated, and the reason is #93's.** Both sides are on disk — `_STANDING_LEDGER.md`'s in-flight
   table and the newest `date:` among `approved: true` articles — so the *last ship date* half is
   derivable and the *in-flight row* half is a prose summary that no schema pins. Raised as a standing-queue
   row rather than built by the run that found it, because the derivable half alone would be a check that
   reports a green on the clause that was already right. The forward question is in the queue.

## General form

*When you attach a maintenance rule to a sentence, read the sentence back and ask which of its claims the
rule can falsify. The claims it cannot falsify are now worse off than before you wrote it.*
