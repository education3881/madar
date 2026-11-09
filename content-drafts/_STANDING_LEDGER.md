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
| `bahrain-bqa-five-cycles` — five cycles of public school grading | 2026-10-21 | 2026-10-23 | **2026-11-02** (+ dispositions 1–2 on 11-05, 3 on 11-07, **4 on 11-09**) | **2026-11-07** | **2026-11-09** | **2026-11-03** (+ retrace 11-07) | **2026-11-09** | — | **one: the flag** |

**Read against disk on 2026-11-09, not against this table's own account of itself.** Verdict files are in
`content-drafts/verdicts/`; the drafts are in `content-drafts/drafts/`; the still is at
`web/public/stills/2026-10-23-bahrain-bqa-five-cycles.svg` and the card at `web/public/og/…png`
(1200×600, 1,849 bytes, rendered from the still by `web/scripts/make-og-card.mjs` and **looked at**, per
2026-08-18). Both assets are safe on disk while the piece is held: `heldAssets.mjs` strips them from
`dist` at the end of every build, so a held piece's subject is not served at a guessable URL.

**The piece is NOT in `web/src/content/` and must not be until all eight cells are filled.**

**Next action, and it is the Manager's:** seven of eight cells are closed. The flag is the eighth and it
moves only after the **publish gate in writing** — Editor and Arabic verdicts on file ✓, Verifier verdict
on file ✓, hero still and share card on disk ✓, `astro build` clean, assertions green, held-slug leak
zero. The flip commit carries the article text **and its assets together** (the 2026-06-14 rule), and
this is the first piece in this publication's history that will ship with **no `edition:` field at all**
— which needed no code change, because the schema has always declared it optional and `/editions/` skips
a null (Arabic Editor's Gate 4 §3).

## Shipped as singles

| Piece | Shipped | Note |
|---|---|---|
| — | — | Nothing yet. The first single will be the first piece this publication has shipped since **2026-09-27**, and the gap is named in every brief rather than smoothed. |

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

**Measured 2026-11-07 (`agents/tools/arabic_side_reach.py`, ruling #132): 0 of 44 published pairs carry
the #86 line and 0 carry the #101 line**, because every published hand-off predates its rule — the 10-04
second amendment's limb two, *a point-of-filing rule never reconciles backward*, on an obligation rather
than a count. The first piece drafted under all five is the one in flight above.
