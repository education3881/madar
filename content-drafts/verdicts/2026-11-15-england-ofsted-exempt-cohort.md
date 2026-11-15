# Editor's five-test verdict — `2026-11-12-england-ofsted-exempt-cohort`

**Editor · 2026-11-15 · cell 3 of eight.**
Draft judged: `content-drafts/drafts/2026-11-14-england-ofsted-exempt-cohort.md` (CC1, 2026-11-14).
Commission: `content-drafts/briefs/2026-11-12-england-ofsted-exempt-cohort-brief.md`.

## VERDICT — **RETURN WITH NOTES, on Test 3.** Not a park. One revision pass, no re-reporting.

**Tests 1 and 2 PASS.** **Test 3 FAILS** and the protocol is explicit — *you do not progress to the
next test until the prior one is passed* — so **Tests 4 and 5 were not judged, and this verdict does
not pretend otherwise.** They are owed on the revision.

The draft is strong. Nothing in this verdict asks for a figure to be re-traced or a register to be
re-read; the sourcing is the best this publication has had at a first pass. What fails is where the
piece puts its own reason for existing.

---

## TEST 1 — Sourcing reality. **PASS**, and it was re-verified rather than accepted.

Every URL was fetched today and every quoted token compared against the bytes the register is
currently serving — #112's method applied before publication instead of after it.

| register | HTTP | quoted tokens checked | verbatim |
|---|---|---|---|
| 1 · Ofsted, *Main findings … as at 31 August 2022* | **200** | 13 | **13** |
| 2 · Ofsted, *Hundreds of formerly outstanding schools reinspected*, 22 Nov 2022 | **200** | 9 | **9** |
| 3 · DfE + Bridget Phillipson MP, *Single headline Ofsted grades scrapped*, 2 Sep 2024 | **200** | 4 | **4** |
| 4 · Ofsted, *Understanding Ofsted report cards and grades* | **200** | 3 | **3** |
| 5 · Ofsted, *Main findings … as at 31 August 2026*, 10 Nov 2026 | **200** | 6 | **6** |
| 6 · Ofsted, *Amanda Spielman's speech to the Festival of Education, 2023* | **200** | 1 | **1** |
| 7, 8 · Madār, the two Bahrain pieces | **200**, **200** | — | — |

**Thirty-five of thirty-five quoted tokens are present verbatim in the served bytes.** The figures the
body states without quoting were checked in the registers' own tables and all hold: Figure 3's
**263 primary · 104 secondary · 367 all previously exempt**, Figure 1's **21,725 / 18 / 70 / 9 / 3** for
31 Aug 2022, register 5's six evaluation-area percentages and its five grade names, and register 4's
**Published: 1 December 2025 · Last updated: 2 November 2026** (the body's dates are right; the page
prints them with colons).

**§A4's strike is confirmed in the strongest available form: the word *retrospective* does not occur
anywhere in register 1 or register 3.** The claim that arrived from a search summary is not merely
unsupported, it is absent from both registers that could have carried it. That is ruling #41 working
at the margin #49 says is the right one, and the drafter is right to have struck it.

**And Figure 3 says something sharper than §A2 claims, which the revision should use.** §A2 places the
two seventeens *fourteen weeks apart in two registers*. They are closer than that: the statistical
release's own Figure 3 row for **all previously exempt schools** reads

```
    367   17 outstanding   62 good   17 requires improvement   4 inadequate
```

— **the two seventeens are in one table, in one row, four columns apart.** The draft's decision to
print no bare *17%* anywhere is therefore not caution, it is necessity, and saying so with the row
quoted is stronger than the fourteen-weeks framing.

### Two Test 1 DEFECTS OF ARTEFACT — both omissions of a thing, neither an error of fact.

**(i) Source 6 carries no URL.** Every other entry in the `sources[]` block ends with its address;
this one ends with a parenthesis. It is the only register in the piece cited **for a property of the
page rather than for a claim in the body** — it supplies the gender determination, not a sentence —
and the drafter's habit of writing the address beside the claim had no claim to attach it to. The
address is **not reconstructible**: the page is titled *Amanda Spielman's speech to the Festival of
Education, 2023* and its slug is `amanda-spielmans-last-speech-at-the-wellington-festival-of-education`.
Supplied by the Editor, fetched today, **200**, standfirst verbatim:

```
https://www.gov.uk/government/speeches/amanda-spielmans-last-speech-at-the-wellington-festival-of-education
   "Ofsted's Chief Inspector reflects on her first speech at the Festival of Education, …"
```

The schema (`web/src/content.config.ts`, `url: z.string().url()`) would have caught it at the build —
which is the 2026-07-27 lesson exactly: *a ruler that first fires at the backstop has already eaten a
cycle.* It is caught here instead, which is where it belongs.

**(ii) The dek is not in the draft.** The hand-off line reports `dek: 188/200` and the string it counts
appears nowhere in the document. The Editor cannot verify a cap on a text that is absent, and the
Arabic composer cannot compose a parallel dek from a number. The title is present (34 code points,
confirmed by counting it); the dek is a measurement with no artefact under it. **Required on the
revision**, written out in full beside its count. The Editor does not supply it: the Editor is the
filter, never the drafter.

Neither defect touches a sentence, so neither reopens Test 1's substance. Both are required before
cell 4 opens.

## TEST 2 — Specificity. **PASS.**

Place: England, and the instrument is England's. Time: **May 2012 – November 2020** exact, 2021/22 for
the yield, **2 September 2024**, **10 November 2025**, **10 November 2026** — every one of them dated
to a register. Named human: **Amanda Spielman**, then Chief Inspector, with three quoted sentences, and
she is **operational** rather than representative — she ran the instrument the piece is about, and her
sentences carry the policy's rationale (*"founded on the hope that high standards, once achieved, would
never drop"*) and its verdict (*"removing a school from scrutiny does not make it better"*). Not
decorative, and not substitutable. The piece cannot be find-and-replaced to another country: the
exemption is England's, the frozen cohort is England's, and the whole argument is that **this**
regulator published the re-measurement.

## TEST 3 — The "why now" test. **FAIL. RETURN.**

> *Does the reader know by paragraph two why you are showing this to them now?*

No. Paragraph one frames an unintended experiment; paragraph two is **May 2012 to November 2020**. The
reader learns the subject by paragraph two and does not learn why it is in front of them in November
2026. The piece's own answer to that question is excellent and it is already written — **it is just a
long way down.** Two sentences carry it:

- the instrument has been withdrawn and replaced, so the 2022 re-measurement **is the only one that
  will ever exist** on that scale; and
- Ofsted published the first annual release under the replacement on **10 November 2026** — *five days
  before this verdict* — and that release says in its own words that **the new grades cannot be
  compared to the old ones.**

The draft's nearest thing to a why-now is *"The result is the one number this publication has been
looking for and had said, in print, did not exist"*, which arrives around paragraph five and is a
why-now **about us**. It is a good sentence and it should stay where it is. It is not a substitute: a
reader who has not read the Bahrain piece has no reason to care that we were wrong, and a reader who
has still does not know why *this week*.

**The remedy is a move, not a rewrite.** Bring the November 2026 fact and the *can't be compared*
sentence up into the opening, before or immediately after the 2012–2020 frame, so that the exemption is
introduced as *the thing that was measured once, on a ruler that has since been taken away*. Nothing
has to be re-reported and no register has to be re-read; every sentence the revision needs is already
in the draft under *"And then the ruler was taken away, twice"* and *"The first year of the new
instrument"*.

**Why this is a return and not a note-on-approval.** The test exists because a piece that reads as a
permanent entry is not journalism, and the order of the tests exists so that a structural failure is
not absorbed into a list of improvements. This one is structural: it is the difference between an
article about an eight-year-old English policy and an article about a measurement that has just become
unrepeatable.

## TESTS 4 and 5 — **NOT JUDGED.**

The protocol is *you do not progress to the next test until the prior one is passed*, and it is
honoured literally. Dignity (Test 4) and long-arc fit (Test 5) are owed on the revision and this
verdict makes no claim about either. **Stated rather than quietly skipped**, because a verdict that
looks complete and is not is worse than a short one — a list of five ticks with two unexamined reads
exactly like a full read.

---

## THE THREE CALLS THE DRAFTER LEFT OPEN — decided here so the revision is ONE pass

**1 · The title — KEEP *The cohort that was frozen by rule*.** It is house-shaped (*The exam that was
switched off*, *The law that moved the finish line*) and it is accurate. The obvious alternative was
tried and **rejected for a reason rather than a preference**: any title built on *thirteen years* —
*The grades that were frozen for thirteen years* — drops the word **average**, and thirteen is the mean
gap for the schools inspected in 2021/22, not a property of the cohort. A title cannot carry a
qualifier, so a title must not take a figure that needs one (#19's family, #29's rule on rulers). The
drafter's abstraction is the price of not overclaiming, and it is the right price.

**2 · The struck retrospectivity claim — NO, it stays out of the body, and the drafter's reason is
upgraded.** The drafter wrote *the body should not list what it declined to say*; the body does in fact
name one declination, where it refuses to reconcile the two registers' arithmetic. The distinction that
actually holds: **that declination is about figures the piece prints, and this one is about a figure the
piece does not.** A reader cannot miss what was never there. And the record is not lost by keeping it
out — source 3's annotation carries *"Recorded as NOT carried"*, and an annotation is **served** (#114),
so the strike is published where claims about registers live.

**3 · The Bahrain correction — KEEP IT LAST.** Opening with our own error would make the piece about
us before the reader knows the subject, and it spends the payoff in the first line. It also collides
with the Test 3 remedy: the opening is about to be given a different job. **One amendment:** the
correction's closing sentence should name the date of the clause it corrects, so that the piece is
correcting a dated claim of ours and not a vague past position.

---

## What is owed before cell 4 (Arabic composition) opens

1. The Test 3 revision — the why-now moved into the opening.
2. The **dek**, written out in full beside its count.
3. Source 6's **URL** — supplied above; the drafter pastes it rather than re-finding it.
4. Tests 4 and 5, judged on the revised draft.
5. The Figure 3 row, used to sharpen §A2 (optional, and recommended).

**Cell 3 remains OPEN.** Quality over slot: the Editor's verdict is on file, which is what advances the
pipeline today, and the flag does not move on a draft whose third test failed.

— Editor, 2026-11-15
