# Verifier verdict — `2026-10-23-bahrain-bqa-five-cycles`

**Verifier** · 2026-11-03 · the run after the Editor's pair verdict, per the 2026-09-06 rule.
**Editor's five-test verdict:** APPROVE on all five, 2026-11-02
(`content-drafts/verdicts/2026-11-02-bahrain-bqa-five-cycles.md`).
**Draft:** `content-drafts/drafts/2026-10-23-bahrain-bqa-five-cycles.md`

## Verdict

**VERIFIED on the numbers. ONE BINDING CORRECTION on the tense, found here and applied in this
commit.** `approved: false` stands and the flag is four things away, not three: Arabic composition
and its gate, the still and the og card, and founder issue **#13** on the edition field.

---

## 1 · Figure trace — the fifth independent count, and the first against a DIFFERENT serialisation

Every prior count read the same export: `data.gov.bh`'s CSV with the portal's default parameters,
183,242 bytes on 2026-10-18/20/22 and 183,191 at the Editor's verdict on 11-02. **Four agreeing reads
of one serialisation cannot distinguish a stable register from a stable parse of it.** So this trace
fetched the register's **English-labelled, semicolon-delimited export** — 72,925 bytes, HTTP 200,
2026-11-03 — and counted it with an independently written counter.

| Claim in the draft | Independently counted today | |
|---|---|---|
| 1,022 rows | 1,022 | ☑ |
| 882 `Review` + 140 monitoring | 882 + 140 | ☑ |
| monitoring in three row types: 45 / 61 / 34 | `Monitoring Visit` 45, `Monitoring Visit 1` 61, `Monitoring Visit 2` 34 | ☑ |
| 245 schools in the register · 242 ever graded | 245 · 242 | ☑ |
| grade totals: (3) 350 · (4) 245 · (2) 202 · (1) 85 | 350 · 245 · 202 · 85 | ☑ |
| monitoring scale only on monitoring rows: (B) 97 (C) 23 (A) 20 | 97 · 23 · 20, and **zero numbered grades on any monitoring row** | ☑ |
| cycle coverage over the 242: 52 / 124 / 22 / 15 / 29 | 52 / 124 / 22 / 15 / 29 | ☑ |
| 76 schools in all five cycles counting monitoring | 76 | ☑ |
| C1 202 · 7 / 60 / 94 / 41 | identical, pct 3.5 / 29.7 / 46.5 / 20.3 | ☑ |
| C2 206 · 14 / 48 / 89 / 55 | identical, pct 6.8 / 23.3 / 43.2 / 26.7 | ☑ |
| C3 207 · 31 / 39 / 70 / 67 | identical, pct 15.0 / 18.8 / 33.8 / 32.4 | ☑ |
| C4 128 · 10 / 25 / 41 / **52** | identical, pct 7.8 / 19.5 / 32.0 / **40.6** | ☑ |
| C5 139 · 23 / 30 / 56 / 30 | identical, pct 16.5 / 21.6 / 40.3 / 21.6 | ☑ |
| cycle date spans, all five | 2009-06→2011-05 · 2012-02→2015-03 · 2015-09→2019-04 · 2019-06→2023-12 · 2024-07→2026-04 | ☑ |
| register spans 2009-06 → 2026-04 | 2009-06 → 2026-04 | ☑ |

**Twenty-three claims, twenty-three agreements, zero discrepancies**, in a serialisation 110,266 bytes
smaller than the one every prior count read. The two derived claims check out too: `(4) Inadequate` is
the modal verdict in C4 alone (52 > 41; in every other cycle `(3)` is modal), and the modal school has
been reviewed in **four** cycles (124), not five.

## 2 · THE FINDING — a scope attributed to the Authority that its register does not state

**The draft said, in three places, that the fifth cycle is "running to April 2026."** The register has
**five columns** — `Cycle`, `Publication Date`, `Review Type`, `School Name`, `Grade` — and **no
cycle-end field anywhere.** `2026-04` is the maximum of the `Publication Date` column over C5's 139
rows. It is the date of the most recent review the Authority has *published*; it is not a date the
Authority has stated for the cycle's *close*, and nothing in the register distinguishes "the cycle ends
then" from "that is the last one out so far."

So one of our own arithmetic facts was printed as the register's announcement — and then it expired.
**April 2026 was already six months past when the draft was written on 2026-10-23, and is seven months
past today**, which makes *"a cycle that runs to April 2026"* a present-tense claim about a bound that
has gone. This is ruling **#117**'s class, and the draft carried no `editorial futures: N, each
attributed to a dated register: ☐` hand-off line, because #117 was codified on 2026-10-26 and the
hand-off was written on 10-23. The Editor's APPROVE on 11-02 did not add it. *A hand-off requirement
added after a draft is written is nobody's unless the next gate adds it* — the same shape as the
09-27 fourth-home defect, one desk over.

**Applied in this commit, by the drafter on this finding, in all three places:**

* body: *"the fifth running from July 2024 to the register's most recent publication, April 2026"*
* body: *"The fifth cycle is **not finished**. Its 139 reviews are the ones the register carries,
  published between July 2024 and April 2026, and the register does not say when the cycle closes — so
  each share below it is a share so far, not a result."*
* hedge 1, which is the binding instruction the Arabic composer works from: the label *not finished* is
  now stated as **our inference with its ground** — 139 against 202, 206 and 207 — rather than as a
  date the Authority gave.

**Re-verified against the register rather than self-graded**, which is the only part of a repair a
verifier may check on its own work: each replacement sentence asserts nothing that is not a cell or an
aggregate of cells in the 72,925 bytes counted above. The two remaining uses of the word *open* (at
*"the open fifth cycle, so far — 16.5%"* and *"16.5% of an open cycle"*) assert **no date** and carry
the hedge at the figure, so they stand.

**What this repair is worth beyond the piece, and it is an addendum to #117:** the fix converts a
**tense** into a **dated figure**. *April 2026* attached to *the register's most recent publication* is
a claim that goes stale by the register changing, which `qa_citation_identity` and
`qa_claim_registers` can both reach; *running to April 2026* goes stale by the calendar turning, which
#117 says no comparison of two bytes can ever see. **The repair does not just correct the sentence; it
moves the claim into the class our instruments can watch.** That is the general form and it is worth
more than the instance.

## 3 · Non-numeric axes (#45 noun, #46 quotation and clock, #47 description-date)

* **Noun (#45).** *reviews* never *schools*, *rows* where rows, *verdicts issued* never *schools
  measured*, *batch* never *cycle*. The four populations are held apart at every use. ☑
* **Quotation (#46).** One verbatim quotation from the Annual Report 2025 — *"22 government schools and
  7 private schools received Gold Seals for outstanding performance"* — carried with *for outstanding
  performance* inside the quotation marks and the 22/7 split printed rather than summed. ☑
* **Clock (#46).** Three clocks, named at every figure: the register's `Publication Date`, the Annual
  Report's **calendar 2025**, the Performance Report's **academic year 2024-25**. No percentage from
  one clock is set beside a percentage from another without both labels. ☑
* **Description-date (#47).** The cycle spans are the register's own; the one date that was *ours*
  dressed as the register's is the finding in §2.
* **Acronyms (#101).** One, `BQA`, expanded as *Education & Training Quality Authority* and carried in
  annotation 2 in the Authority's own form. Verified by hand, because `qa_acronym_evidence` shares no
  word-initial with that expansion and returns no anchor — standing-queue item 37, unchanged.
* **Named humans (#86).** None. The predecessor carries Dr. Maryam Hasan Mustafa and her determination;
  this piece does not re-report her, so no gendered construction is made here and none is owed.

## 4 · Structural rows

* **Flag state (#18).** `approved: false`. No page, no sitemap entry, no feed item, no `lastmod`, no
  bytes. Verified green by `qa_pair_frontmatter` and the held-leak assertions on this build.
* **Schema caps (07-27).** `dek: 197/200 · title: 47/100`, counted at compose and recorded in the
  hand-off. Re-counted here: within cap.
* **`related:` resolution.** All three slugs resolve, EN and AR, all three `approved: true`.
  **And all three point BACKWARD** — 2026-05-26, 2026-06-20, 2026-07-28 — with **zero of the three
  pointing forward at this piece.** That is standing-queue item **72** reproducing itself on the very
  next piece through the pipeline, exactly as that row predicted it would; the forward edges are owed
  **in the flip commit**, not later, and this verdict is where that is written down.
* **Guardrails (#19).** All four hedges on the distribution table are carried in the body, not in a
  note: C5 unfinished, C4 smallest-and-longest with the span stated and no explanation offered, not a
  panel (52 of 242), and the ruler may not be constant. The Edition 05 standing prohibitions hold: no
  *best* without its ruler, no composite of rulers, improvement never without its floor, announced ≠
  measured.
* **Licence.** The portal prints `Licence unknown`. Counts are reported; the table is not reproduced,
  excerpted as a table, charted or embedded. Verified against the shipped body: no table markup.
* **Archival coverage (#111).** Still **UNKNOWN of 5** and still blocking the flag rather than the
  verdict. Two state-host PDFs and one API-query CSV are the three classes item 34 names as the ones our
  instruments systematically cannot read. `qa_claim_registers --emit` runs over these five before the
  flag moves.

## 5 · What is owed before the flag, in order

1. **Arabic composition**, carrying the live park condition — the four populations must be holdable
   apart in Arabic — and now also carrying hedge 1 in its corrected form.
2. **Arabic Editor's gate**, with the `named humans — gender read from register: 0 of 0` line.
3. **Hero still and og card.**
4. **The `edition:` field**, which is founder **issue #13**, default **2026-11-08**.

Plus, in the flip commit and not after it: **three forward rails** into the three pieces this one
follows up (item 72).

---

**Signed** · Verifier · 2026-11-03 · twenty-three figures re-counted from an independently fetched
serialisation with zero discrepancies; one binding correction found, applied and re-verified against
the register; `approved: false` stands.
