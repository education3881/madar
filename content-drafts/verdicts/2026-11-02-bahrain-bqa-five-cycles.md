# Editor's five-test verdict — `2026-10-23-bahrain-bqa-five-cycles`

**Verdict: APPROVE on the frame and on all five tests.**
**Two binding annotation corrections before the flag moves, and the flag itself is blocked on issue #13.**

**Editor** · 2026-11-02 · draft of 2026-10-23, commissioned 2026-10-21, recon 2026-10-18 as corrected
2026-10-22. **Ten days between hand-off and verdict, and that is this verdict's own finding** — see the
closing note.

---

## Test 1 — sourcing reality. **PASS, and re-probed at verdict rather than read off the draft.**

The commission says *all five registers re-opened at verdict, dates recorded.* The draft's Test 1 table is
dated **2026-10-23**. A verdict that accepted it would be accepting a ten-day-old observation as a present
state, which is #76 exactly (*a serving state is an observation with a date*). All five were re-opened
**today, 2026-11-02**:

| # | Register | At verdict, 2026-11-02 | Against the draft's 10-23 reading |
|---|---|---|---|
| 1 | `data.gov.bh` dataset page | 200 · 160,891 bytes | reachable |
| 1a | **the CSV export the figures rest on** | **200 · 183,191 bytes** · sha256 `aca3d7de144187c5…` | **the draft recorded 183,242 — the file moved 51 bytes** |
| 2 | `bqa.gov.bh/open-data/` | 200 · 87,300 bytes | reachable; nothing cited from it |
| 3 | Annual Report 2025 PDF | 200 · **13,440,188 bytes** | **byte-identical**, fourth consecutive reading |
| 4 | Performance Report 2024–25 PDF | 200 · **4,243,331 bytes** | **byte-identical**, fourth consecutive reading |
| 5 | the predecessor, as served | 200 · 38,847 bytes | the quoted question is on a page a reader can open |

**The register moved and no claim moved with it.** Because row 1a's bytes changed, the whole spine was
**recounted from today's bytes** rather than accepted — and every figure in the draft is confirmed:

* 1,022 data rows · **882 `Review`** · 140 monitoring in **three** row types (45 / 61 / 34) ✓
* grades over the 882: `(3) Satisfactory` **350**, `(4) Inadequate` **245**, `(2) Good` **202**,
  `(1) Outstanding` **85** ✓
* monitoring on its own three-band scale only: `(B)` 97, `(C)` 23, `(A)` 20 ✓
* **245** in the register · **242** ever reviewed · **76** in all five counting monitoring · **52**
  reviewed in all five ✓
* cycle coverage over the 242: **52 / 124 / 22 / 15 / 29** ✓
* all five cycle rows, every count and every percentage, to the decimal: C1 202 (3.5/29.7/46.5/20.3),
  C2 206 (6.8/23.3/43.2/26.7), C3 207 (15.0/18.8/33.8/32.4), C4 128 (7.8/19.5/32.0/**40.6**),
  C5 139 (16.5/21.6/40.3/21.6) ✓
* span 2009-06 → 2026-04 ✓

So the drafter's third count was right in every cell, and a **fourth** count ten days later against moved
bytes agrees with it. That is as strong as Test 1 gets on this publication's method.

### Correction 1, binding — the annotation currently says something that is now false

Source 1 reads *"unchanged across three prior readings"*. **The file's bytes are not unchanged.** Rewrite
to the claim that is true and that the reader can use:

> *1,022 rows and every count below unchanged across four readings, 2026-10-18 → 2026-11-02; the export's
> own byte length moved from 183,242 to 183,191 in that window, outside every field this piece reads.*

This is #112's rule applied to our own annotation rather than to somebody else's document: we asserted a
property of a register's bytes, and the bytes are the one thing that did change. **An annotation may not
claim a stability it has stopped having, even when every figure resting on it held.**

### What the 51 bytes buy the operation, recorded because it is not this piece's to carry

Standing-queue **item 55** asks for a *moved since we read it* flag over all 348 registers, and names its
own honest limb: *a moved byte is not a new claim.* **This is the first measured instance of that limb in
this operation's history** — a first-party state register whose bytes moved while **every one of
twenty-three counted claims held exactly.** A body-hash flag would have raised this register today and
been right about the bytes and wrong about the piece.

So the cheap first cut for item 55 is better specified than it was this morning: hash a **claim-bearing
projection**, not the file. For this register the projection is `(cycle, review_type, grade, school_name,
year)` over all 1,022 rows, sorted — recorded here as today's baseline so the next read can tell *moved*
from *moved where we look*:

* full file sha256 `aca3d7de144187c583941a92ef4007c5`
* **claim-bearing projection** sha256 `04115c5b1fcf16f3f2637fb5a5925895`
* distribution-only projection sha256 `ba6af6e079d092fdfa36533f579491e0`

Handed to item 55 as a specification, not fixed here, because an instrument over 348 registers is the
Assertions Engineer's and a per-register projection is the drafter's.

## Test 2 — specificity. **PASS, strongly.**

Not relocatable by find-and-replace, and not by much else. Seventeen years of one authority's own scale,
printed by that authority in both languages in the same row (`(3) Satisfactory` / `(3) مرضٍ`), a named
instrument (**Gold Seal**), a named framework (**Schools Reviews Framework 2024**), a named open-data
portal with a stated licence state, and a per-cycle distribution **nobody had computed before** — the
commission asked for the cross-tabulation the predecessor could not get, and the piece is that
cross-tabulation. The sentence that carries the whole piece is specific to this register and could not be
written about any other: *the distribution widens for three cycles, inverts in the fourth, and narrows in
the fifth.*

## Test 3 — why now. **PASS, and the draft led with it as instructed.**

The commission said this test is the strongest part and the draft *should lead with it, not bury it.* It
opens on the predecessor's own closing question, quoted verbatim from the served page with its date, and
names the interval — *150 days later*. The second paragraph answers it. That is the test executed rather
than satisfied.

Two further *why now* supports are present and correctly hedged: C5 runs to **April 2026** and is
**open**, labelled open at every single use, and the 2024 framework's first batch has reported.

## Test 4 — dignity. **PASS, and this is the test the draft worked hardest.**

A register with 245 `Inadequate` rows is the easiest scandal in this publication's history to write, and
the draft refuses it in the body rather than in a note: *"That is not a scandal and this piece will not
write it as one. It is what a four-point scale looks like when a regulator actually uses all four points
of it, in public, with the school's name attached."* The frame credits the openness — *"has done the rare
and difficult thing"* — without using the credit to soften the figures, which is the Sudan prohibition
(*the positive posture never denies context*) run the other way round.

**No school is named by its grade.** Verified: the register names 245 schools and the body names none.

**And the hardest line in the piece is the one that protects the schools from the ruler**: cycle four's
40.6% is left unexplained because *"the register records what the Authority found; it does not say why,
and neither will we."* A causal sentence there would have been free to write and impossible to defend.

## Test 5 — long arc. **PASS.**

Slow, GCC-anchored, one register read properly, and it closes on what the distribution **cannot** say
rather than on a moral — arriving at a sharper version of the predecessor's question instead of at its
answer: *how much of the movement in a published distribution belongs to the schools, and how much to the
instrument.* That is the right ending and it is also the next commission, which is how this publication
is supposed to compound.

---

## Standing prohibitions — checked one by one

| Prohibition | Carried? |
|---|---|
| No "best" without its ruler in the same sentence | n/a — no superlative claimed |
| No composite of rulers | **☑ and it is the piece's fourth hedge** — *verdicts issued*, not schools measured; the 2024 framework named as a possible ruler change the register does not speak to |
| Improvement never without its floor | **☑** — `(1) Outstanding` 3.5% → 16.5% is **never** written as improvement; the draft says so explicitly in its own not-claimed list |
| announced ≠ measured, labelled at the figure | **☑** — 22 Gold Seals (calendar 2025, recognitions), 26% (academic 2024-25, a batch of 76), 16.5% (an open cycle's 139 reviews): three clocks, named at each figure, *"and treats none of them as the others"* |
| A pair carries only what both languages share (#42) | ☑ at the AR gate; the grade names are forced renderings printed by the Authority in the same row |
| The positive posture never denies context | **☑** — see Test 4 |

## Hand-off lines — the four that return a draft unread

1. **Caps** — `dek 197/200 · title 47/100`, counted at compose; the first dek came out at 225 and was cut
   before hand-off. **Fourth strike of the 07-27 shape caught at the ruler instead of the backstop.** ☑
2. **`annotation == sentence`** per leaned-on register — present, five rows. ☑ *(and it is now one
   correction short — see Correction 1, which this line's own discipline is what caught.)*
3. **Named humans, gender read from register: 0 of 0** — the draft names no individual and correctly does
   not re-report the predecessor's named official. ☑
4. **Acronyms expanded in the body: 1, each expanded in `sources[]`** — `BQA` → *Education & Training
   Quality Authority*, carried in annotation 2 in the Authority's own form. ☑ **By hand, because
   `qa_acronym_evidence` structurally cannot see this one** — `BQA` shares not one word-initial with the
   expansion, which is standing-queue item 37 and was found by running the gate on this very draft.
5. **Editorial futures, each attributed to a dated register (#117)** — checked at verdict. The piece's
   only forward reference is *"a cycle that runs to April 2026"*, which is the register's own stated cycle
   end and is a fact about the cycle's definition rather than a claim about an outcome. **C5 is labelled
   OPEN at every use.** ☑

## Correction 2, binding — `edition: 6` may not ship

The frontmatter claims `edition: 6`. **There is no Edition 06.** The registry carries five editions, all
`status: 'closed'`, with `hasOpenEdition` exported and `false` since 2026-10-31, and *what the next piece
is an edition of* is **founder issue #13**, open 8 days with a stated default of **2026-11-08**. Shipping
`edition: 6` would put a claim in the frontmatter that the registry contradicts — which is **item 62's
defect class exactly**, one week after that row was raised to gate it.

So: the field is held, not guessed. **The verdict is the frame; the flag waits on #13.** If #13 is
unanswered on 2026-11-08 the default applies and is recorded as a decision made by silence.

## Park conditions, each read against the draft rather than assumed

* **Licence resolving against reporting counts** — **did not fire.** The portal prints *Licence unknown*
  and carries no licence statement; the draft's annotation says so in terms. The shipped body **reports
  counts and derived percentages in prose and reproduces nothing**: no table, no excerpt-as-table, no
  chart, no embed. The per-cycle table lives in the drafter's working section and **does not cross into
  the article.** **Binding on the Web Developer and the Designer: it stays out.** A chart of this
  distribution would be the most shareable thing this publication has ever made and is the one thing the
  licence state will not support.
* **Annual Report 2025 Gold Seal sentence not re-openable at verdict** — **did not fire.** 200,
  byte-identical, fourth reading.
* **Three populations not holdable apart in Arabic** — **not yet testable.** This fires or clears at the
  Arabic gate, and it is a stated park condition, so the Arabic Content Creator composes against it
  knowing that *writing around it is not an option.*

---

## What is now owed, in order

1. **Corrections 1 and 2 applied to the draft** — one annotation sentence, one held field.
2. **Arabic composition** from the CSV's own Arabic column, never from this draft (forced renderings, #101).
3. **Arabic Editor's gate**, carrying the park condition above as a live test.
4. **Verifier's verdict** — scheduled the run after this one, per the 2026-09-06 rule, in banking order.
   Its first job is `qa_claim_registers --emit` over these five registers: hand-off line 5 reads
   *UNKNOWN of 5*, and **two are state PDFs and one is a CSV behind an API query string**, which are the
   three classes item 34 names as the ones our instruments systematically cannot read. Any figure resting
   on an unarchived single register is double-sourced or dropped.
5. **Designer hero still + og card.** Not started.
6. **Publish gate in writing**, then the flag — **and not before #13.**

## The verdict's own finding, which is not about the piece

**This draft waited ten days for a verdict it passes on every test.** The Editor is the filter, and a
filter that takes ten days on a clean draft is a constraint on the pipeline rather than on the piece. The
cause is visible in the board: the DEFECT bucket was non-empty on four of those ten days and the standing
queue's head took the content function's attention on the rest. **Nothing on this draft needed ten days** —
Test 1's re-probe and the full recount that justified it cost twelve minutes this morning.

Recorded here rather than in the brief because it is the Editor's own answer to a question nobody asked:
*the pipeline's binding constraint is not drafting, and it has not been for a while.*

— Editor · 2026-11-02
