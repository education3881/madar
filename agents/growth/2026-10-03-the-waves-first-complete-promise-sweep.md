# Growth — the wave's first complete source-promise sweep, eight days before the gate

**Date:** 2026-10-03 · **Lane:** Growth (return-rate instrument, not a traffic one)
**Instrument:** `qa_sources_alive.py --held-only --sample 0`, run after today's ruling **#85** fixed its
parser · full output and JSON kept at run time
**Why today:** the Edition 05 ledger instructs this sweep *"immediately before the flip commit."* The
gate target is **2026-10-11 — eight days.** Running it now rather than on flip day is the whole point:
a finding on flip day is a delay, and a finding today is a week of slack.

---

## Why this is a growth action and not a QA chore

The publication's single differentiating claim is that every figure stands on a named primary source the
reader can open. **A rotted source link does not degrade a piece slightly — it converts the piece's
central promise into a dead end in front of the one reader who cared enough to click**, and that reader
is definitionally the returning reader. This is the instrument's own charter and it is the reason it
leads with no traffic number: the site carries no third-party tracker by design, so what can be measured
is whether the promises hold, not how many people tested them.

## The result

**59 distinct URLs cited by the six held pairs. 53 answer 200. Zero 404s. Zero dead names.**

| Bucket | Count | Disposition |
|---|---|---|
| `ok` | **53** | nothing owed |
| `timeout` | **4** | all one host — `parliament.gov.zm`, Zambia (row 1) |
| `walled` (403) | **2** | `tandfonline.com` (row 3, Sudan) · `cgdev.org` (row 4, slot 3) |

**Both walls are already disposed or assigned.** Sudan's was closed in today's confirmation read with a
verbatim second channel (RePEc/IDEAS). CGDev's belongs to slot 3's confirmation read, which is the next
one owed, and it is a wall rather than a death — *a 403 is a source we cannot see, which is a different
fact from a dead source and gets a different bucket*.

## The finding: ruling #80 was tested by the world within 48 hours and held

The four timeouts are the whole of `parliament.gov.zm`, and they matter because **this operation has now
recorded that one host six different ways in four weeks**:

| Read | What we received |
|---|---|
| 09-10 | unreachable |
| 09-16 | connection refused at :443 |
| 09-30 | invalid certificate |
| **10-01** | **HTTP 200, valid to 10 Dec 2026, chain incomplete but closable — a reader meets nothing** |
| 10-03 (sweep, 20s) | no response |
| 10-03 (re-probe, **75s**) | **no response — so it is not merely slow** |

On 10-01 the Zambia confirmation read filed **ruling #80** on the strength of the fourth reading, and
rewrote **twelve annotations across the pair as dated observations** — *"re-probed 2026-10-01, HTTP 200,
304,258 bytes"* — rather than as statements about what the host *is*.

**Two days later the host does not answer at all, and not one published sentence has gone false.** Every
annotation says what we received and when we received it. Had 10-01 written *"the document is served"* as
a property of the register, today twelve annotations in two languages would be wrong, eight days before
the wave carries them to readers.

> **This is the first time this operation has been able to watch that discipline pay rather than argue
> for it.** A serving state is observed by a client, at a time (#80) — and the cost of obeying that is
> four words per annotation, while the cost of ignoring it is a false sentence in a published piece,
> discovered by a reader.

**Nothing is edited on row 1 today.** The annotations are already correct *as written*, which is the
point. Per #20 a sixth reading does not become a seventh disposition: the host's behaviour is now
demonstrably variable, which is itself the dated fact the annotations carry.

## What the fixed instrument changes, stated precisely rather than dramatically

Today's ruling **#85** found this tool collecting **678 of the corpus's 684** source promises. Measured
honestly, **that bug did not corrupt this sweep**: held-cited distinct URLs are **59 under both the old
parser and the new one**, because the six lost citations belong to the Netherlands pair, which is
published rather than held. What the bug corrupted was the **corpus-wide** count, and its held-set half
was **latent** — a held piece whose frontmatter contained `---` would have had *every* source dropped
from this exact sweep.

So the honest claim is the narrow one: **this is the wave's first complete promise sweep because it is
the first run on an instrument proved to read the whole frontmatter — not because the number changed.**
A number that would have been right by luck is still a number nobody could have checked.

## The bet this reads against, and what it costs

No bet is opened. This closes a standing ledger item a week early and converts the flip's riskiest
remaining mechanical step — an unbounded, previously un-observable sweep at the worst possible moment
(the 09-16 P1) — into a dated, bounded, re-runnable one. **Owed at the flip commit regardless:** one
re-run, because a sweep is an observation with a date and the flip is eight days away.

**Traffic:** the site carries no third-party tracker by design. No visitor figure is estimated here or
anywhere.
