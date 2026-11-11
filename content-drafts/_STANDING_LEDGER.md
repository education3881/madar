# The standing ledger — one row per piece, no edition framing

**Opened 2026-11-08 at the weekly review, by applying GitHub issue #13's stated default (option B) on the
date it fell due.** This is the live ledger. `_EDITION_05_STATUS.md` is a **closed-edition record** and
nothing is planned from it.

> **A decision made by silence is visible as one.** Issue #13 — *what the next piece is an edition of,
> twelve days after Edition 05 closed* — was opened 2026-10-25 with three options and a stated default:
> *if there is no reply by 2026-11-08, the operation applies option B.* It was open **fourteen days**, no
> reply arrived, and the default is applied here. **B was chosen as the default not because it is the best
> option but because it is the only one the operation can execute without a word from the founder** —
> options A and C both need a frame, and only he can set one. *A default the operation cannot execute is
> not a default* (the rule issue #8 settled).
>
> **What B costs, recorded rather than glossed:** no shared throughline, no registry row six, no cover, and
> the Editions page stops growing at five. The founder's recommendation in the issue was *A if you have a
> frame in mind this week; otherwise C* — so the operation is now running the option its own
> recommendation ranked **third**, and it will keep saying so. **Issue #13 stays open**, because applying a
> default settles what happens next week and not what the publication is. A frame arriving on any later day
> supersedes this file for pieces after it; pieces already shipped as singles stay shipped (#41 —
> supersede, don't resurrect).

## How a piece ships here

Each piece ships **the day its own gate closes** — no wave, no all-or-nothing flip, and the 71-day
invisibility of Edition 05 cannot recur. The gate is unchanged; what changes is that it is read per piece
rather than per wave. Eight cells, and a piece ships when all eight are filled:

1. Editor's brief · 2. EN draft · 3. Editor five-test verdict · 4. AR composition ·
5. Arabic Editor's gate · 6. Verifier verdict · 7. Hero still + og card · 8. `approved: true` in both
editions, in one commit with its assets (the 2026-06-14 rule)

**The Verifier's verdict is scheduled the run after the pair verdict** (2026-09-06) and **drafter ≠
verifier is structural** — neither is relaxed by the absence of a wave. The ceiling stays **one fresh piece
per day at most**, and the standing rule holds: **quality over slot, hold rather than ship thin.**

## In flight

| Piece | Brief | EN draft | Editor verdict | AR | AR gate | Verifier | Still + og | Flag | Open cells |
|---|---|---|---|---|---|---|---|---|---|
| **Ofsted — the cohort frozen by rule** (working title; no slug yet) | — | — | — | — | — | — | — | — | **all eight — recon done 2026-11-11, cell 1 is next** |

**Reconciled against disk 2026-11-11. The table is no longer empty, and what fills it is a candidate with
recon on file rather than a piece in production** — the distinction is kept in the *Open cells* column on
purpose, because a row here with eight open cells is a commission decision waiting for the Editor, not a
draft. Recon at `content-drafts/recon/2026-11-11-instrument-vs-schools-candidate-recon.md`: **candidate 1 (KHDA Dubai) parked and then UN-PARKED the same run, the park being wrong — ruling #139**, measured — `web.khda.gov.ae` serves its leaf certificate with no
intermediate, so the chain cannot be built by any client that verifies one — **and that is a `tls-chain` condition, which #80 ruled on 2026-10-01 is NOT an access failure**: the leaf's own AIA address yields an intermediate against which it verifies `OK`, valid to 18 December 2026, so every browser reads the register and only our client cannot; **candidate 2 (Ofsted, England) PROCEED**, because the regulator exempted outstanding
schools from routine inspection from May 2012, lifted the exemption in November 2020, re-graded the frozen
cohort and printed the yield beside the stock in one release — *"Only 17% of previously exempt schools that
had a graded inspection this year remained outstanding"* against *"Eighty-eight per cent of all schools are
good or outstanding."* **That is the Bahrain single's closing question answered by a regulator's own
arithmetic**, and the recon's contribution is that the piece's claim *the register that would settle it is
one nobody publishes anywhere* is false.

**Three reads are owed before the Editor's brief, and they are named in the recon rather than left to the
drafter:** the newest `state-funded-schools-inspections-and-outcomes` release for a current stock figure
(the one read is *as at 31 August 2022* and the piece is read in the reader's present, #117), Ofsted's
first-party account of the September 2024 removal of single-word overall judgements (a second instrument
change on the same register), and the Editor's call on whether an England candidate needs a Gulf register
to carry it or whether `bahrain-bqa-five-cycles` is a sufficient anchor **inside our own corpus** — which
would be the first time a single leans on a published predecessor that way.

**The 2026-11-10 note below is superseded by the paragraph above and kept for the record.** `bahrain-bqa-five-cycles` filled its eighth cell on 2026-11-09 and moved to *Shipped as
singles* below. **This is a state, not a gap, and the daily run must not read an empty table as a quiet
day:** with no wave to fall back on, an empty in-flight row means the next piece needs the first cell —
the Editor's brief, which needs the Researcher's recon first — and nothing downstream can advance until
it exists. **Standing rule for this file, from today: the run that empties this table names the next
commission's candidate in the same commit, or states plainly in the brief that it did not.** An empty
pipeline that nobody names reads exactly like a pipeline between pieces, which is the 71-day shape option
B was adopted to prevent, one scale down.

**Named today, not commissioned:** the obvious successor is the question the Bahrain single closed on, and
the operation does **not** yet have recon on it. Recon is the Researcher's and it precedes the Editor's
brief; it is queued as the next content function's first action rather than improvised at the end of a run
whose content function was spent on the board's head.

## Shipped as singles

| Piece | Shipped | Note |
|---|---|---|
| `2026-10-23-bahrain-bqa-five-cycles` — five cycles of public school grading | **2026-11-09** | The first single, and the first piece shipped since **2026-09-27** — a gap of **43 days**, named rather than smoothed. Also the first piece in this publication's history to ship with **no `edition:` field at all**, which needed no code change: the schema has always declared it optional and `/editions/` skips a null. Five gates bit on it before it could ship and every one was right. Corpus 45 EN and 45 AR. |

**Assets of record:** still at `web/public/stills/2026-10-23-bahrain-bqa-five-cycles.svg`, card at
`web/public/og/2026-10-23-bahrain-bqa-five-cycles.png` (1200×600, rendered by
`web/scripts/make-og-card.mjs` and **looked at**, per 2026-08-18). `heldAssets.mjs` no longer strips
either, the piece being approved.

## Standing prohibitions — these bind every piece here

Carried from Edition 05's commissions, where they were written, and they **outlive the edition**: they are
the terms four of those six pieces were commissioned under and they bind any successor piece on the same
ground.

- No **"best"** without its ruler in the same sentence; no composite of rulers (#29, #30).
- **Improvement never without its floor.**
- **Announced ≠ measured**, labelled at the figure — and from #117, an editorial future is written with its
  register's date attached or it is not written.
- The positive posture **never denies context** (the Sudan commission's term).
- A pair carries only what **both languages share** (#42) — and a figure printed only in an annotation is
  still published (#114).
- A named human's gender is read off the register's **pronoun, gendered title, or a morpheme the register
  prints** (#86 clause 1 as amended by **#134**), never off how a name sounds; where no register carries
  it, the determination is declared in the annotation as this edition's own, with its date (#86 clause 2).
- An **acronym** is expanded in the body only if `sources[]` expands it (#101).

## The hand-off lines a draft cannot reach the Editor without

A hand-off missing any of these is **returned unread** — the same teeth in every case:

- `dek: NNN/200 · title: NN/100` (code points, tashkeel +1 each) — 2026-07-27
- `annotation == sentence` per leaned-on source — 2026-09-13
- `named humans — gender read from register: N of M` — #86
- `acronyms expanded in the body: N, each expanded in sources[]: ☐` — #101
- `editorial futures: N, each attributed to a dated register: ☐` — #117

**Re-measured 2026-11-10 (`agents/tools/arabic_side_reach.py`): 1 of 45 published pairs carries the #86
line and 1 carries the #101 line** — and it is the same pair, `2026-10-23-bahrain-bqa-five-cycles`, the
first piece drafted under all five hand-off lines and now shipped. The figure was **0 of 44** when
measured on 2026-11-07, because every published hand-off predates its rule — the 10-04 second amendment's
limb two, *a point-of-filing rule never reconciles backward*, on an obligation rather than a count. **The
step discontinuity is now visible in the register as one row**, which is what that limb asks for: the
rule's start date is the first row that satisfies it, and the 44 rows before it are a known error with a
known size.
