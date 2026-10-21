# Ruling #111 — the unit of re-verifiability is the claim, and a per-URL rate hides it

**Filed** 2026-10-21, daily run, from the standing queue's own head — **item 15 at 7 days and six
displacements**, the oldest item past the three-displacement threshold.
**Family** — reachability (*whether the number can be read at all*), joining #20, #26, #11, #27, #54
and #100. **That family keeps no running member count on purpose, so FOUR homes move and not five**
(10-04 second amendment, limb one), and the member is appended to the family's enumeration in §3
rather than counted.
**Instrument** — standing assertion 35, `agents/tools/qa_claim_registers.py`.

---

## The rule, in one line

**A URL's health is not a claim's health, and the arithmetic does not carry in either direction: one
dead register strands every figure whose only support it was and strands nothing at all where a
second register carries the same figure — so a per-URL defect rate is not a small version of the
claim-level answer, it is a different quantity with a different shape.** Measure re-verifiability in
claims, and ask the question in the form *can **anybody** open this, not just us.*

## What was asked, and by whom

Item 15 was raised on 2026-10-14 by the run that swept 342 distinct outbound URLs and bucketed 60 of
them — 5 dead, 6 bot-walled 403s, 1 bad certificate, 53 fine. Its own text named the gap it had just
demonstrated: *today's sweep classifies URLs and has no row anywhere for a claim.* One instance had
been produced by accident on that morning — **Morocco's one-in-six refusal ratio**, whose denominator
left the public record when the ministry withdrew two list PDFs that no archive had kept — and it was
found only because a *different* citation on the same piece happened to 404 (#100).

It then sat for seven days and six displacements. It came off the board this morning by rule, not by
memory: clause (2) of the one-queue rule, and the 10-05 tiebreak at 7 days against 6.

## The axis nothing we own had ever queried

Every instrument this operation has that touches an outbound promise asks **what we receive**.
`qa_body_links` proves the link is rendered; `qa_sources_alive` asks whether the far side answers and
buckets the reply; `qa_reachability` asks the same of our own pages. All three are about the two
parties to our own request. Item 15's question has a third party in it:

| | openable by **us** | openable by **anybody** |
|---|---|---|
| live | yes | yes |
| walled to us (#70) | no | yes — a human with a browser |
| dead, archived | no | yes — the public record kept a copy |
| dead, no snapshot | no | **no, and never again** |

Only the last row is a claim-level defect, and the axis that separates it from the row above is
**whether a snapshot exists** — one API call per register, against a host whose entire purpose is to
answer it, and we had never made it once in five months of publishing.

## What the measurement found, and it is a SHAPE and not a rate

Measured 2026-10-21 over all 88 approved pieces, EN and AR, 342 distinct registers — of which
**205 have an answer and 137 are still owed one**, the measurement being paced for the reason in the
next section:

* **40 of the 205 answered registers hold no snapshot anywhere — 19.5%.** Of those, **28 are live and
  we can read them today** — one copy in the world, on somebody else's server — and **12 refuse us as
  well** (403), so they are readable right now by a human with a browser and by nobody at all the day
  the publisher changes them. Among the twelve is **medias24.com**, which item 15's own text had named
  as *Morocco's surviving public carrier of the very list that went missing.* It is unreadable to us
  and unarchived. Also in it: four `nation.africa` citations, two `doi.org` resolvers, Egypt's own
  `moe.gov.eg`, `sudantribune.com`, and an opening statement to an Australian Senate estimates
  committee hosted at `aph.gov.au`.
* **1,490 body figures are anchored in a named register.** Joining those against the register's state,
  the figures whose **every** carrier is unreadable-and-unarchived number **24 — and 20 of them are on
  one piece**, `2026-07-04-kenya-cbe-grade10-pathways` (12 EN, 8 AR), whose four `nation.africa`
  citations are all in that bucket. The remaining four are two figures in each edition of
  `2026-07-07-sudan-exam-continuity`.

**That is the ruling.** A per-URL report of the same facts reads *40 of 205 answered, 19.5%, spread
across the corpus* — a tolerable-sounding rate inviting a tolerable-sounding response. The claim-level unit reads
*one piece whose spine cannot be re-opened.* The remedy the second framing asks for is addressed to a
piece and is editorial: re-read that piece's figures against whatever register survives, or re-source
them, or mark them. The remedy the first framing asks for is a percentage target, which nobody can
act on. **A population rate is not a weaker version of a concentration; it is the concentration with
the only actionable thing about it averaged away.**

Worth naming beside it: the Kenya piece has now produced **three separate rulings** — #100 (the dead
citation), #101 (the institution named wrongly for 103 days, surfaced because that citation died) and
this one. It is the thinnest evidentiary base in the corpus and it has been telling us so three times
in seven days, each time through a different instrument, and no instrument ever said *this piece*.

## What the instrument asserts, and why only half of it can

`qa_claim_registers` is `qa_served_manifest`'s design (#89) with the two modes the other way round.

* **`--emit` — network, gates nothing.** Asks the archive about every cited register, probes the
  origin ourselves for the ones with no snapshot, and writes a dated row per register to
  `agents/stats/claim-registers.json`. It must never gate: the far side belongs to archive.org,
  ministries and journals, and their outage is not our build's failure — which is exactly the reason
  written in `astro-pages.yml` beside `qa_sources_alive`.
* **`--check` — offline, deterministic, GATED from `postbuild`.** Asserts that the register **covers
  the corpus**: every distinct `sources[].url` an approved piece carries has a row with its required
  fields. It makes no network call and knows nothing about the world.

So the gate asserts our own bookkeeping and the measurement asserts nothing, and that division is not
a compromise — it is the only one available, for a reason worth stating flatly: **a claim's
re-verifiability is a property of the world, not of this repository and not of the served bytes.**
Thirty-four assertions read bytes we produce. This one cannot. What a gate *can* buy is the thing #89
bought: the chain of memory. If the emit silently stops describing some registers, or a piece ships a
citation nobody has ever asked an archive about, the build goes red instead of the measurement
narrowing in silence.

Proved four ways on a copy, bite first, controls green on either side of each, every injection
asserted to have changed the artefact before the check was run on it (#35, #65): a cited register
with no row; a row that drops a required field; the register file gone entirely; and the silent-pass
trap, a corpus with no approved content at all.

## The measurement hygiene half, which cost the most and generalises furthest

The first emit asked all 342 registers with six workers. It got **100 answers and then 242
consecutive HTTP 429s**, and wrote a register in which **242 of 342 rows read `archive-unknown`.**

That file was not a measurement of the public record. **It was a measurement of our own request
rate, wearing the schema of a finding.** Nothing in the output said so; `archive-unknown` is exactly
what a genuinely unarchived-and-unknowable register would have produced, and a run reading that file
tomorrow would have concluded that 71% of this publication's evidentiary base is in an unknown state.

So the emit now carries a **request budget and a spacing**, re-asks only the rows that have no answer
or a stale one, never overwrites a known answer with a throttled one, and tops the register up across
runs. **General form, and it is the part to carry:** when you measure somebody else's server, your
own rate limit enters the data in the same column as the answer — so a measurement of a third party
records *what we asked and when*, and a bucket meaning *we did not find out* is never allowed to
share a name with a bucket meaning *there is nothing there.* Same family as #76 (*a serving state is
an observation with a date*) seen from the measurer's side rather than the host's.

**And this ruling's own first draft committed the error it describes, inside the same run.** The first
reading, taken when only 100 registers had answered, was written up as *22 of 342 — 6.4%* and quoted
in that commit's subject line. The denominator was wrong: 242 of those 342 had not been asked, so the
rate divided the findings by a population that included the registers we had declined to measure.
Against the answered population the same morning's figure is **19.5%** — three times larger. *A rate
whose denominator contains unmeasured units is not conservative; it is just wrong, in the flattering
direction.* **#57 restated on a sweep instead of on a register: count against the population you
actually measured, and name which one that is.** The commit subject stands as filed and is corrected
here rather than rewritten, because an intermediate reading of a paced measurement is a real event in
the record.

## What this does NOT assert, said in the tool's own output

The claim→register map was measured on the way: **406 of 1,896 distinct body numerals (21.4%) appear
in no annotation of their own piece.** That is printed as a **candidate list and not a defect list**,
and it will stay that way. A body writes *thirty-six facilitators* where its register prints `36`; it
recomputes a share the annotation states as a count; it carries years the annotation never repeats.
A figure's boundary is not a textual property (#85), and an assertion on that number would fail on
correct articles and be switched off inside a week (#35). It is reported so the distribution is
visible and so the top of it can be read by a human.

Also honest about one limitation: four of the no-snapshot registers are `doi.org` resolver URLs, and
a DOI's permanence is the resolver's promise rather than the snapshot's. *No snapshot of this URL* is
a true statement about that URL and a weak statement about that document, and the register says so.

## Binding

1. **Re-verifiability is reported in claims, with its concentration named.** A sweep that reports a
   per-URL rate is incomplete until it says *which pieces* and *how many figures*. The rate goes in
   the log; the piece goes to the Editor.
2. **A register with no snapshot is a P2 the day it is found, not the day it dies.** The window in
   which anything can be done about it is exactly the window in which the document is still there.
3. **`--emit` runs with a budget and the register is topped up across runs**, oldest answer first;
   137 registers are still owed an answer as of today and that number is printed, not estimated.
4. **A bucket meaning *we could not find out* never shares a name with a bucket meaning *there is
   nothing there*** — in this instrument or any other.

## Forward

The join above is only as good as the claim→register edge, and that edge is a numeral appearing in
both a body and an annotation of the same piece. It cannot see a figure the body states in words, a
share the body recomputes, or a sentence that is load-bearing and carries no number at all — which is
the whole non-numeric family (#45 — #47, #101, #104). **So the 24 is a floor on a population whose
size is unknown**, and the honest next question is whether a claim's support can be identified at all
without the drafter writing it down at compose time.
