# Manager status — 2026-11-02 (Monday)

**Run:** `madar-daily-operation`, scheduled, started 12:31Z — **8.1 h after its cron**, which is *outside*
the measured band (4 h 14 m – 7 h 43 m over 54 runs, re-measured yesterday) by 24 minutes. Noted, not
escalated: #107's point is that the cron is not a start time, and one run 24 minutes past a band of
fifty-four is a wider band, not an incident. **State verified before planning, not from a brief:** `HEAD`
and `origin/main` both at `79a4d1f`, tree clean, yesterday's deploy green. No dark day — 11-01 ran both
the daily and the weekly review and both landed.

**Delivered in five commits, one at the close of each function (#96), with `run_envelope.py --log --label`
called at every one (#122 clause 1).** Wall clock at the close: well inside 90; turn axis UNMEASURABLE at
every reading, which is why delivery was staged rather than saved.

---

## What shipped

**Nothing was published and no flag moved** — correct state, not a stall: Edition 05 closed 2026-10-13,
there is no open edition, and what the next piece is an edition of is issue **#13**. Six already-approved
pieces changed served bytes (frontmatter rails); gated in writing at
`agents/logs/2026-11-02-publish-gate.md`.

## Queue — head taken as written, board 34 → 35

**Item 26 CLOSED at 15 days**, the oldest row in OPEN, second consecutive head from the backlog with the
DEFECT bucket empty. **Twenty-seventh selection in twenty-eight daily runs made by the rule rather than by
judgment, eighth under #116.** Displaced 30 OPEN rows including items 67 and 70 — the daily's and the
weekly review's own forward questions — on their first and second mornings.

The row expected a list of checks and the answer is a **partition**: 76 declining statements across 21 of
41 instruments, **20 genuine declines in five reason-kinds** — A delegated to a sibling (1), B blocked on a
permission (3), C a #93 floor above today's reality (7), D an oracle limit (6), E a missing artefact (3).
**Two of the five kinds have now produced a falsified reason and this row found both**: kind E on 10-18
(#106), kind A today.

**Kind A was false.** `qa_third_party_origins` — the one gate whose subject is the privacy posture — had
declined **1,203 served declarations** for 25 days because *their format and origin are
`qa_consumer_surface`'s subject*. The format half is true; **the sibling has no origin comparison in it at
all**, three literal-origin hits in the file and all three in prose. Limb 2 now asserts it, measured at
**0 of 1,203 foreign** before anything was asserted so the floor sits at today's reality (#93), with
`author`/`license`/`me` exempt **by rel** and printed. Three bites red, three controls green — **and bite 3
did not bite**, a `sed` delimiter colliding with a comma so the file never changed and the check printed
CLEAN. Caught by the 09-14 guard rather than by me noticing afterwards, which is the first time that has
happened.

**Gate count deliberately unchanged: 41 tools, 38 gating.** A limb is not a tool, and a run that adds a
limb and reports a tool is how a count drifts.

**Two rows raised, neither a DEFECT:** item **71** (seven kind-C declines expire by arithmetic and nothing
watches the counts) and item **72** (the `related:` rail's direction). Board **34 → 35**: 0 DEFECT, 32
OPEN, 3 BLOCKED, counted by reading the rows per #57 for the eighth week. Breach date unmoved at
**2026-11-11**.

## Content — the Bahrain draft approved after ten days, against a register that had moved

**APPROVE on all five tests**, `content-drafts/verdicts/2026-11-02-bahrain-bqa-five-cycles.md`. Test 1 was
re-probed **at verdict** rather than read off the draft (#76) — and **the CSV the whole piece rests on had
changed**, 183,191 bytes against the 183,242 the draft recorded as byte-identical ten days earlier.

So the spine was recounted from today's bytes rather than accepted, and **every figure held**: 1,022 rows,
882 reviews, 350 / 245 / 202 / 85 across the four grades, 245 / 242 / 76 / 52 across the four populations,
coverage 52 / 124 / 22 / 15 / 29, all five cycle rows to the decimal including C4's 40.6%. *A fourth count
against moved bytes agreeing with the third in every cell is as strong as Test 1 gets here.*

**Two corrections applied to the draft in the same commit rather than left as notes:** the annotation
claimed *unchanged across three prior readings*, which is now false of the bytes, so it states stability of
the **counts** and names the 51-byte move (#112 turned on our own annotation); and **`edition: 6` is
HELD**, because there is no Edition 06, the registry exports `hasOpenEdition: false`, and shipping it would
be **item 62's defect class one week after that row was raised to gate it**.

The 51 bytes are also **the first measured instance of item 55's honest limb** — a first-party register
whose bytes moved while all twenty-three counted claims held, so a body-hash flag would have been right
about the bytes and wrong about the piece. A claim-bearing projection hash is recorded as the baseline and
handed to item 55 as a specification.

**The verdict's own finding, which is not about the piece:** a clean draft waited ten days for a verdict
that cost twelve minutes. The pipeline's binding constraint is not drafting, and has not been for a while.

## Growth — the related rail only points backwards in time

138 directed edges between pieces, **98 reciprocated, 40 one-way — and 34 of the 40 point newer → older.**
Connectivity is clean (0 pieces with no inbound rail, 0 with no outbound, 0 dangling, EN and AR identical),
so this is a **clock**, not an orphan: a rail is curated when a piece is published and at that moment only
the older pieces exist. **Sixteen published pieces are pointed at by a newer piece and offer no forward
path**, worst Oman with five followers and none — and the older piece is the likelier landing page.

Three forward rails turned round in both editions, each a same-instrument pair. **The other 31 deliberately
untouched, and not for time:** reciprocating mechanically would convert an editorial claim into a graph
operation. Raised as item **72** for the Editor, and the ask is a step in the commission template, because
the defect regenerates with every piece published — the Bahrain draft has three rails and all three are
backward.

**No traffic figure anywhere.** The site carries no third-party tracker by design.

## Research — ruling #125

*A decline may not name a sibling instrument without naming the sibling's limb, and the run that writes it
reads that limb first.* Owner, limb, date; a bare tool name is not a delegation, it is a hope. An
overturned reason is written out beside the new limb, never deleted. **Five homes moved at the point of
filing**, the conditional fifth firing because #125 joins assertion discipline as its **forty-sixth**
member, and the membership list moved with the number (#95 limb 3).

**`qa_register_shape` refused my own work four times before it passed** — a 5-cell row against a 4-cell
header (the 10-04 defect), a stale series-integrity line, a second declared-count home I had not found by
reading, and **a parenthetical of mine that silently narrowed the declared-list read from three to two**.
That last is #124's own class, committed inside the commit filing against it.

## Held, and why

Nothing editorial held for quality. The Bahrain piece is **approved and correctly unshipped** — five things
away, one of which is not ours.

## Queued for 2026-11-03

* **Item 28 at 14 days** takes the head unless a DEFECT is raised: *which of our four render assertions rest
  on an oracle nobody has interrogated?*
* **Item 71**, today's forward question, enters at OPEN's head and will be displaced.
* Bahrain: Arabic composition from the CSV's own Arabic column, carrying the park condition live.
* **Issue #13's default falls 2026-11-08** — Sunday, at the weekly review. Not applied today; the date has
  not arrived. It cost something concrete for the first time today.

## Founder questions, carried by name

**#13** 8 days, default **2026-11-08** · **#12** 9 days · **#11** 18 days, default applied 10-22 · **#8**
29 days · **#7** **43 days — the oldest, and still the one that costs most.**

---

Brief 119 delivered, rendered and **looked at** at 1280 and at 390 per 08-23. Build exit 0, 38 of 41
gating assertions green, five commits pushed, origin confirmed.
