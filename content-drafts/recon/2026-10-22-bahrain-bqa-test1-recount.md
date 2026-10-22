# Test 1, executed — Bahrain BQA, all five registers re-opened and the dataset recounted from the bytes

**Date of reading: 2026-10-22.** Run by the Researcher at the Editor's instruction, before a sentence
of `2026-10-21-bahrain-bqa-five-cycles` is composed. The commission is explicit about why this comes
first: *"The CSV counted again from the bytes, not carried from the recon's table."*

**It found two corrections, and both are population-boundary errors — the exact class the
commission's own prohibition table was written to stop.** Better here than in a verdict.

---

## A. The five registers, re-probed. All five open.

| # | Register | 2026-10-22 | Against the recon's reading |
|---|---|---|---|
| 1 | `data.gov.bh` CSV export | **200 · 183,242 bytes** · sha256 `d6b62bda651083dc…` | **byte-identical** to 10-18 |
| 1b | `data.gov.bh` dataset page | 200 · 159,357 bytes | reachable |
| 2 | `bqa.gov.bh/open-data/` | 200 · 87,303 bytes | reachable (page is dynamic; 10-18 read 96,867 on the Publications page, see below) |
| 2b | `bqa.gov.bh/publications/` | 200 · 92,737 bytes | reachable; **10-20 read 96,867** — a 4,130-byte difference on a WordPress index whose news rail moves. Not a change to anything cited. |
| 3 | Annual Report 2025 PDF | **200 · 13,440,188 bytes** | **byte-identical** to 10-20 |
| 4 | Performance Report 2024–25 PDF | **200 · 4,243,331 bytes** | **byte-identical** to 10-20 |
| 5 | `2026-05-26-bahrain-bqa-public-grades` as served | verified live earlier today (`qa_live_drift` CLEAN, 134 URLs) | the predecessor's closing question is quoted from a page a reader can open |

A serving state is an observation with a date (#76). Three byte-identical reads across four days is the
strongest statement available about a document's stability, and it is the statement, not an inference
about the host.

**Archival snapshot state, owed by the commission's hand-off requirement 5 (#111):** carried into the
hand-off, not answered here — `agents/stats/claim-registers.json` is the register and the Bahrain URLs
are not yet in it, because the piece is not yet in the corpus. The drafter asks for them before the
verdict.

---

## B. The recount. Four figures confirmed, two corrected.

Counted from `reviews.csv` (`;`-delimited, eight columns, the Authority printing every grade name and
review type in **Arabic and English in the same row** — which is what makes every one of them a forced
rendering under #101).

**Confirmed, exactly as the recon and the commission have it:**

| Figure | Recount | Status |
|---|---|---|
| Rows in the export | **1,022** | confirmed |
| `Review` rows | **882** | confirmed |
| Monitoring visits | **140** | confirmed — and it is *three* row types, not one: `Monitoring Visit 1` 61, `Monitoring Visit` 45, `Monitoring Visit 2` 34 |
| Grade distribution over the 882 reviews | `(3) Satisfactory` **350** · `(4) Inadequate` **245** · `(2) Good` **202** · `(1) Outstanding` **85** | confirmed, and it sums to 882 exactly |
| C5 `Review` rows | **139** | confirmed |
| C5 shares | 17 / 22 / 40 / 22 % — `(1)` 23 · `(2)` 30 · `(3)` 56 · `(4)` 30 | confirmed |
| Cycle spans | C1 2009-06→2011-05 · C2 2012-02→2015-03 · C3 2015-09→2019-04 · C4 2019-06→2024-03 · **C5 2024-07→2026-04, OPEN** | confirmed |

**The four numbered grades appear on `Review` rows and nowhere else**, and the three lettered
progress grades (`(A) Sufficient Progress` 20, `(B) In Progress` 97, `(C) Insufficient Progress` 23)
appear on monitoring-visit rows and nowhere else. That is a clean partition of the 1,022 and it means
no sentence about the four-grade scale can be contaminated by a monitoring visit. Worth stating
because it was assumed rather than checked until today.

### Correction 1 — there are **245** schools in this dataset, not 242, and the difference is a population

The recon's table reads *242 schools*. Recounted: **245 distinct school names across all 1,022 rows**,
and **242 across the 882 `Review` rows.** Both numbers are right about different sets. **Three schools
in this register have been visited and never reviewed** — they hold monitoring-visit rows only and no
grade on the four-band scale has ever been issued to them.

The recon's 242 is therefore correct *for the review population* and must be labelled with it. Binding
on the draft: **"242 schools have been graded" and "245 schools appear in the Authority's review
register" are different sentences and neither may be written without its population.** This is the
same defect shape as the 26/24/30/20-against-76 trap the commission already carries — one register,
two denominators, and the smaller one reads like the whole.

### Correction 2 — **52** schools have been reviewed in all five cycles, not 53

The recon's table reads *53 in all five cycles*. Recounted twice, two ways:

* schools with a **`Review` row** in each of C1–C5: **52**
* schools with **any row at all** (review or monitoring visit) in each of C1–C5: **76**

So the recon's 53 matches neither population, and is off the review-based count by one. The full
distribution of cycle-coverage over the 242 reviewed schools, which nothing had computed before today:
**52** schools in all five cycles, **124** in four, **22** in three, **15** in two, **29** in one.

The 124 is the more interesting number and the draft should consider it: *the modal school in this
register has been reviewed in four of the five cycles, not five.* A seventeen-year series is not a
seventeen-year panel, and a sentence that says "the same schools, five times" would be wrong for 190
of the 242.

---

## C. What this changes in the commission, and what it does not

**Does not change:** the spine. `(3) Satisfactory` 350, `(4) Inadequate` 245 ahead of `(2) Good` 202,
`(1) Outstanding` 85, all over the 882 reviews, all confirmed from the bytes today. The Gold Seal
sentence is in a byte-identical PDF. The *why now* — the predecessor's own closing question — is
quoted from a live page.

**Changes, and they are now draft-blocking in the same way the commission's three populations are:**

1. A fourth row joins the prohibition table: **242 reviewed schools / 245 schools in the register / 76
   schools present in all five cycles / 52 schools reviewed in all five cycles.** No sentence may use
   one of those four as another.
2. The draft may not write the five cycles as a panel. **52 of 242** is the panel.
3. The monitoring visits are a second instrument with its own three-band scale, and the piece either
   says so once or does not mention them. It may not fold 1,022 into a statement about grading.

**Park conditions unchanged**, and none of them has fired: the licence question is unchanged (counts
reportable, table not ours to serve), the Annual Report 2025 Gold Seal sentence re-opened
byte-identically today, and the Arabic grade names are printed by the Authority in the same row.

**Next step, named so the next run does not have to decide it:** the EN draft, from this recount's
numbers rather than the recon's table, with the four-population line in the drafter's envelope. The
Arabic Content Creator composes from the Arabic column of this same CSV, never from the EN draft.

— Researcher · 2026-10-22 · *the recount was required by the commission, and the commission was right
to require it*
