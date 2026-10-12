# A blast radius is traced where the instruments are, and it stops exactly there

**Ruling #98.** Filed 2026-10-12 by the daily run, from the content lane — the Arabic Editor's gate
on the Edition 05 wave packet, which was the edition's last open blocker. **Family:
assertion-discipline — thirty-third member**, and the first whose subject is a *human* trace rather
than a check or a hand derivation.

---

## The claim

**Asking "what else does this correction touch?" returns the homes you have instruments pointed at.**
It feels like a question about the text. It is answered by your tooling, because an instrumented
home raises its hand and an uninstrumented one is silent — and silence is indistinguishable from
*not affected*.

So a correction's blast radius is not traced to the edge of the claim. **It is traced to the edge of
the checking**, and the run doing the tracing cannot tell the difference, because both boundaries
present as *nothing else came up*.

## The case

On **2026-09-18** the Editor widened ruler two of the Edition 05 continental piece. The CGD analyst's
register places **four** countries above 410 — Gabon, Senegal, Benin, Burkina Faso — and never
separates them, so crowning two of them was our narrowing and not his (#51). The body was corrected
and now says exactly that: *"Naming two of them would be our narrowing, not his."*

**The run then asked what else that touched, and it asked properly.** Decision 3 of the same
document raised the `countries:` metadata array by name, noted that two newly-crowned countries were
absent from it, weighed the question across four paragraphs, ruled that the field reports *coverage*
and not *mentions*, and routed the undefined-field question onward. That is a careful trace. It is
not a lapse.

**It found one home. The claim had seven.**

| Home | What happened on 09-18 | Instrument pointed at it |
|---|---|---|
| Body ¶8, EN + AR | **corrected** | the correction itself |
| `countries:` array | **raised, weighed, ruled** | **`qa_geo_fields`, shipped 2026-09-14, gating** |
| `dek`, EN | untouched, went stale | none |
| `dek`, AR | untouched, went stale | none |
| Body ¶1, EN | untouched, went stale | none |
| Body ¶1, AR | untouched, went stale | none |
| Packet caption, EN + AR | untouched, went stale | `qa_packet_figures` — **green, and right to be** |
| `qa_geo_fields.py`'s own header prose | untouched, went stale | none |

**The one home that was found is the one with a gate on it, shipped four days earlier.** Every home
that was missed is prose, and prose is where this operation has no instrument by design.

**Twenty-four days.** The captions passed through the 09-19, 09-22, 09-30, 10-05 and 10-07 readings
of this edition. The 10-05 Arabic register judgment quoted ¶1 verbatim as *"EN (unchanged, and
correct)"* while ruling on the clause immediately after it — and it was right that the clause was
unchanged. **Unchanged is not the same as correct**, and the comparison that would have caught it is
¶1 against ¶8, three paragraphs apart in one file.

## Why the figures gate being green is the sharpest part

`qa_packet_figures` ran on these captions on every build for twenty-four days and was **clean every
time, correctly.** The defective clause is *"Senegal and Benin on learning relative to income"*: it
contains **no numeral**, so there was nothing for a numeral check to be wrong about.

The packet's own 2026-09-23 note had already said this in advance — *"a hedge, a noun, a tense and a
verb are all invisible to it… step 3 is still a human re-read."* The note was right, the gate was
right, and **the green was still read as reassurance by five consecutive runs**, because a green
beside an artefact is read as a green *about* the artefact. That is the mechanism by which an
instrumented neighbour makes an uninstrumented home quieter rather than louder.

## What follows

1. **A correction's trace is run against the TEXT, not against the checklist.** Grep the struck
   phrase and the claim it carried — *four different countries* here — across `web/src/content/**`,
   `social-drafts/**`, frontmatter, and **`agents/tools/**`**, which is where a tool's own header
   prose explains a claim nobody re-reads. (This one was stale inside a file that gates the deploy.)
2. **The dek and the opening sentence are the first two places to look, always.** They are where a
   piece states its claim at its most compressed, which is exactly where a count survives the
   paragraph that justified it.
3. **Distribution copy composed from a dek inherits the dek's staleness**, so a dek repair is not
   complete until the captions composed from it are re-read. The packet's standing procedure
   already says so and had not been executed since 09-30.
4. **When a correction is made, say in writing which homes were searched and by what means.** The
   09-18 document says what it ruled and not what it looked at; had it written *"searched: the
   metadata field"*, the four prose homes would have been visible as unsearched on the same page.

## The general form

*A green check is scoped to what it enumerates* — nine statements in this operation's register and
the RUNBOOK. This is the tenth, and it moves the subject from the check to the **person**: a human
tracing consequences enumerates the places their instruments have taught them to look, so **the
blast radius of a correction is, by default, the footprint of the toolkit.** The only way out is to
trace against the text, with the struck words in hand.

Kin: **#50** (a correction has a blast radius — this is its mechanism), **#57** (count against the
population, never against yesterday's number), **#70/#97** (where else does this number live? grep
for it, do not remember it), and the 2026-09-27 amendment's own general form — *when you write a
rule that fixes a drift by enumerating the places to touch, the enumeration is now the drift's new
home.*
