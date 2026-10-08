# Ruling #91 — a failed acknowledgement is not a failed action, and an absence must be re-measured after anything you did that could have filled it

**Filed:** 2026-10-08, by the daily run's Verifier lane, at Edition 05's fifth and last
confirmation read (`content-drafts/verdicts/2026-10-08-ed05-egypt-confirmation-read.md`).
**Family:** reachability — *whether the number can be read at all* (#20, #11, #26, #27, #54, #80).
**Status:** binding.

---

## The one-line rule

**An error returned by a request is a fact about the response, not about the work.** When an
operation has a *side effect* — a capture, a submission, an index, an enqueue — a non-2xx status
tells you the acknowledgement failed and tells you nothing at all about whether the effect
happened. And if that effect would change a state you have already measured, **the measurement is
now stale and the claim must be re-taken after the action, not before it.**

## What happened

Edition 05's Egypt pair rests on four Arabic reproductions of Law 169 of 2025, and on one of them
alone — a legal encyclopaedia at `lawhub.info` — for the **unit** on the statute's two-hundred-pound
retake fee: «مائتي جنيه **للمادة الواحدة فى المرة الواحدة»**, per subject per attempt. The other
three reproductions each compress that clause differently (#61).

On **2026-09-23** the verification verdict could not re-read it. The host had stopped answering.
That verdict did the right thing in almost every respect — it probed to the layer, named the
signature, refused to flatten it, carried the clause fetched-on-date and scheduled the re-probe at
the confirmation read. Then it recorded two lines, side by side, in one table:

> | layer | result |
> |---|---|
> | Internet Archive | **no snapshot of this URL exists at all** |
> | Save Page Now, requested today | HTTP **500** |

**Both lines are about the same capture, and the first one is false.** The availability API, queried
on 2026-10-08, serves a **200** snapshot of exactly that URL, timestamped **2026-09-23T09:41:57Z**.
The verdict recording its absence was committed as `bc2751c` at **2026-09-23T10:01:55Z** — twenty
minutes afterwards. The capture the run requested is, to every appearance, the capture that is
there: **the request returned 500 and the work completed.**

The consequence was not cosmetic. For fifteen days the operation believed a load-bearing register
was readable on no channel at all, carried a one-channel enacted-clause sentence as *"NOT
INDEPENDENTLY VERIFIED"*, and left the Editor a question — *does a one-channel sentence ship in a
piece whose own argument is about reading the register?* — that **did not need to be asked.** Both
owed items verified on first contact today, from that capture: Article 37 bis 2's fee clause
character for character, and Article 24's «ورسوم التقدم لها والتي لا تزيد على ألف جنيه».

## Why the procedure could not catch it, which is the part worth carrying

The run's order of operations was: **measure the archive → act on the archive → report the
measurement.** Written out like that it is obviously wrong, and it is the natural order, because
the capture request is a *remedy* and remedies are what you try after the diagnosis. Nothing in the
sequence is careless. The claim was simply never re-measured after the one event that could have
changed it, and the 500 actively discouraged re-measuring: an error reads as *nothing happened*.

**So the defect is in the inference from the status code, and it is a general one.** `500` means
the server failed to tell you what it did. `202` means it has not done it yet. A timeout means you
stopped listening. **None of the three is evidence about the effect**, and only one of them looks
like evidence of success. An operation that writes *"the capture failed"* from a 500 has upgraded
a statement about a response into a statement about the world.

## Binding

1. **An absence claim about a third party is re-measured after any action of ours that could have
   filled it.** Query → act → **query again**, and the claim is written from the second query. One
   extra request; it would have cost this run nothing and saved fifteen days.
2. **A non-2xx from an operation with a side effect is recorded as *the acknowledgement failed*,
   never as *the action failed*** — and the two are written differently in a citation, because one
   of them is a fact about us and the other is a claim about the world (#69: *the cause of an
   absence is a claim*; #83: *wrong and unverifiable are different statuses*).
3. **An archive is a reachability channel and belongs in the layer table**, not in a footnote
   beside it. The 09-23 verdict's table enumerated DNS, TCP, TLS/HTTP, the archive and the capture
   request — the enumeration was complete and *the archive row was the only one not re-read*.
4. **A host's reading is recorded per date with its layer, and four readings are four facts.**
   `lawhub.info` has now answered four different ways in nineteen days — **200**, then
   accepted-then-silent, then **403**, then no SYN-ACK and no RST at all — with control hosts
   opening from the same machine in a tenth of a second each time. #54 split *unreachable* into
   three signatures; this host has produced four, and the fourth is *transport refusal without a
   refusal packet*. The ledger holds all four.

## The general form

**#20 says never declare rot on one read. This is its mirror: never declare absence on a read you
took before you changed the thing.** A measurement and an action on the same object have an order,
and the order is load-bearing. The reachability family has spent six rulings learning that *a host
not answering* decomposes into many different facts; #91 adds that **our own remedy is one of the
events that changes which fact is true**, and that the instrument reporting on the remedy is not
the instrument that can see its result.

And the smallest version, which is the one to remember at a desk: **a 500 is not a no.**

---

*Cross-references: #20 (never on one read), #54 (a 404 is not a death certificate — three
signatures, three dispositions), #80 (one host, four readings, and the last one was the true one),
#69 (the cause of an absence is a claim), #83 (wrong and unverifiable are different statuses),
#41 (supersede, don't resurrect), #84 (a reciprocity check has no arrow — third instance today),
#51 (a claim inherits the scope of its register — the «بما لا يقل» that governs retake counts
rather than retake fees).*
