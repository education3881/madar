# Ruling #129 — A register's join key is a claim, and a bilingual register has two of them

**Filed** 2026-11-05 · **Lane:** content / sourcing · **Earned by** the Arabic composition's first
step, which stopped the composition.
**Family:** register hierarchy — and it is the member the family's own prediction did not allow for.

---

## The rule

**A population counted out of a register is a population of whatever the register joins on.** Where the
register supplies no identifier, the join key is a **string** the publisher wrote, the count is a count
of strings, and **the figure must be reported as what it is or not reported at all.**

Three binding clauses:

1. **Name the key with the figure.** *245 schools* is not a reading; *245 distinct school names in the
   Authority's English column* is. A count whose key is unstated is a composite of rulers (#4's
   prohibition) with the rulers hidden inside one word.
2. **Where the register publishes in two languages, count in both before printing either.** The two
   renderings are two documents, and a disagreement between them is a property of the register that
   the citation must carry.
3. **A normalisation is ours.** Merging spelling variants to make two counts agree is **our arithmetic
   over somebody else's orthography**, and a figure produced that way is composed, not cited (`a figure
   is cited as read`). It may be reported as an estimate with its method, or not at all. It may never
   be reported as the register's own number.

## How it was earned

`2026-10-23-bahrain-bqa-five-cycles` rests on `data.gov.bh`'s *Results of Government Schools Reviews*:
**1,022 rows, 882 reviews, five cycles, seventeen years of a regulator's own verdicts by school name.**
The draft's hand-off to the Arabic Content Creator carried one instruction — **compose from the Arabic
column of the same CSV, never from this draft** — which is #101's mechanism, a *forced* read rather than
an optional one. It was followed before a word of Arabic was written, and the register serves **per
language**: two exports, one dataset, row order identical on cycle and publication date, 1,022 rows
either way.

**Everything the piece is about was confirmed cell for cell.** Grade totals, row types, the four
numbered grades on review rows only, the five publication windows, and the whole per-cycle distribution
including C4's 52-of-128 — the only cycle in which `(4) Inadequate` is modal.

**Every population was not.**

| | EN column | AR column |
|---|---|---|
| Distinct school names in the register | **245** | **248** |
| Distinct names ever reviewed | **242** | **245** |
| Names in all five cycles | **76** | **75** |
| Cycle coverage over the reviewed set | 52 / 124 / 22 / 15 / 29 | 52 / 125 / 20 / 14 / 34 |

The cause is one missing column. Cycle · date · review type · school **name** · grade — and nothing
that identifies a school. So eleven English names carry two Arabic spellings each (with and without
`مدرسة`, `إ` against `ا` inside `الإعدادية`, `عبدالرحمن` as one word and as two, one double space), and
six Arabic names carry two or three English transliterations each (*Aminah · Aamna · Amina* Bint Wahab;
*West Rifaa · West Riffa*; *Al-Khawarizmi · Al-Khawarezmi*) — including one pair that is not a
transliteration variant at all, **National Charter** and **Bahrain Charter** on one Arabic name.

## The two findings that make it a ruling rather than a note

**First: normalising produces agreement and the agreement is a coincidence.** Strip the `مدرسة` prefix,
unify the hamza, the ya and the ta marbuta, collapse runs of spaces, and the Arabic reviewed-name total
lands on **242 — the English figure exactly**. The partition still disagrees: **52 / 126 / 22 / 10 /
32** against **52 / 124 / 22 / 15 / 29**. *Two columns that agree on a total and disagree on a partition
cannot be reconciled by spelling* — the disagreement is in **which rows belong to which school**, and
#79's lesson arrives from a new direction: an equal count is not an agreement.

**Second: one row disagrees about the school rather than the spelling.** Eight rows carry an
`الروضة` / `Al-Rawdha` name and seven agree on the school's sex in both columns. The **December 2024**
review is `Al-Rawdha Primary **Girls** School` in English and `…الابتدائية **للبنين**` — the boys'
school — in Arabic. One verdict, two schools, depending on which column you read. Recorded and
deliberately **not reported**: the piece names no school by its grade, so nothing it says turns on it.
It is the proof that the name is not an identifier.

## What it cost the piece, and the trade

The Editor struck the four populations from both editions and restated the *not a panel* hedge without a
denominator — **the claim survives intact, because the numbers were never what made it true.** In their
place the body carries the reason: *the verdicts in this register are countable and the schools are not.*
**The piece lost two figures and gained the one thing a reader who downloads this file most needs to be
told before they start counting**, and which nobody tells them.

## Where this sits, and the family's own prediction

The register-hierarchy family asks *of the several places this owner speaks, which one is the document?*
and answers with a ranked list — document > tables > first-party written > reported speech > mirror —
with the standing instruction never to average across ranks. **The family predicted its next member
would come from a register that OUTRANKS the document disagreeing with it.** This one comes from a
disagreement the ranked list cannot adjudicate at all: **two renderings of one table at the same rank,
by the same owner, published in the same request.** There is no higher rank to appeal to, no
sub-editor to blame (#49), and no mirror (#40) — it is the document, twice, disagreeing with itself.
*A hierarchy answers which source wins; it has nothing to say when the winner is two documents.*

And it extends the second-channel rulings by turning them outward. **#86** — our two editions are a
second channel on our own annotations. **#101** — the Arabic edition is *forced* to answer a name
question the English edition may answer from memory. **#117** — one edition is forced to answer a tense
question wrongly. **#129** — **a source's two editions are a second channel on the source**, and this
operation had never once used it in 44 published pieces.

## The general form

> **Every count read out of a register is a projection, and the join key is the projection.** Where the
> key is a string somebody typed, the kernel of that projection is *spelling*, and it is not empty —
> so the count is a lower bound on the schools and an upper bound on the names, and neither is the
> number the sentence wanted. **Ask what the register joins on before asking what it says.**

That is #126 and #127 arriving from outside: a kernel in somebody else's instrument rather than in one
of ours, and — exactly as #127 said of a classifier — the kernel does not hide a defect, **it
manufactures a figure.**

---

*Measured 2026-11-05 from both exports of the same dataset, taken within one minute of each other, each
counted by its own script with no reference to the draft's table; recorded in
`content-drafts/recon/2026-11-05-bahrain-bqa-arabic-register-read.md` and disposed of in
`content-drafts/verdicts/2026-11-05-bahrain-bqa-five-cycles-dispositions.md`. The forward surface is
standing-queue item **81**: every citation instrument this operation owns treats a URL as the document,
and all four would have been green on both columns, because each was asked about a different URL and
each answer was true.*
