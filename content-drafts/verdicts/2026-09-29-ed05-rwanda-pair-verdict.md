# Editor's five-test PAIR verdict — Edition 05, row 6

**Pair:** `2026-09-27-rwanda-teacher-certification` (EN + AR)
**Title:** *Rwanda counted the teachers it had not trained, twice* / «عدَّت رواندا المعلِّمين الذين لم تُدرِّبهم، مرَّتَين»
**Read:** 2026-09-29, both languages, against the piece's own `sources[]` and against the calendar.
**Verdict: RETURNED-3-NOTES → all three closed in-run, in both languages → PASS. BANKED.**

The edition's sixth and last pair. Read as a pair, in one sitting, EN then AR, per #42 — a pair
carries only what both languages share, and every note below was found in one language and applied
to both.

---

## The five tests

**Test 1 — Sourcing reality. PASS, and it is the test that produced two of today's three notes.**

All eight URLs re-probed live at the verdict, 2026-09-29, not taken from the draft's own record.
All eight return HTTP 200. The two yearbook PDFs return the byte counts the annotations claim —
4,023,048 and 5,224,340 — identical on a third day, which is a stronger confirmation than a status
code: the documents carried at this verdict are the documents the drafter read.

Every named institution is real and identifiable: MINEDUC, the Rwanda Basic Education Board, the
National Examination and School Inspection Authority, the World Bank, Umwalimu SACCO, The New Times
of Kigali via allAfrica. Two named humans, both attached to a named date and a named occasion:
State Minister for Education **Claudette Irere** (speaking 20 August 2026 at the 2025/26 results
release) and **Pelagie Abayikunda** (a primary French teacher in Kigali, quoted inside the funder's
own feature and labelled as such in the body).

**And the serving state had changed under the piece — see note 1.** This is the Test 1 discipline
working exactly as written: *does every cited URL resolve, today, to the document the piece claims
it does?* The answer was yes, and the reason it took a re-probe to find the note is that the piece
made a claim about *how* it resolves.

**Test 2 — Specificity. PASS, strongly.** Rwanda; Kigali; all thirty districts; sixteen model
schools; the school years ending July 2024 and July 2025 named separately at every figure; April
2024 (programme opening), March 2026 (the funder's count), February 2026 and 21 April 2026 (the
register's two dates), 1 August 2022 (the salary communiqué), 10 August 2026 (the reform release),
20 and 24 August 2026 (the speech and the newspaper), 5 November 2025 (the progress note, dated off
the ministry's index). This piece could not be find-and-replaced into another country: its argument
is a property of one ministry's bookkeeping.

**Test 3 — Why now. PASS.** Established by paragraph two and rebuilt at the second count: the
2024/25 yearbook has been on the ministry's own listing since 21 April 2026 and it carries the
column that undercuts the March 2026 headline. Two further 2026 events carry the close — the 10
August reform release and the 20 August upgrade-window remarks. The reader knows by the second
paragraph that the news is the *second count*, not the programme.

**Test 4 — The dignity check. PASS, and it is the strongest thing about the pair.** A senior
Rwandan educator would recognise this account. The piece credits the discharge as "a large and
genuine piece of work a stock count cannot see" and refuses to read the flat stock as a failure —
the arithmetic is explicitly barred in both directions. The one teacher's voice is carried at
length, in her own words, about her own working life, and the piece says plainly where it reaches
us from rather than presenting it as independent testimony. Ruling #72's translation policy is
applied to her exactly as to the ministry; I re-read the Arabic specifically to confirm the
typography does not rank the voices, and it does not.

The structural absence — no independent evaluator, no union, no critical academic, no pass rate —
is stated in print rather than balanced away with a manufactured counterweight. That is the right
call and the right register.

**Test 5 — Fit with the long arc. PASS.** This is a Madār piece and could not be anything else.
Its subject is a *register*, not a programme, and its finding is bookkeeping. It closes the Africa
edition on the same virtue the Brazil piece was built on — a state printing the unkind number
beside the kind one — and the body names that precedent rather than leaving it for the rail.

**Caps, measured at this desk per the 2026-07-27 enforcement addendum:**

| | title | dek | body |
|---|---|---|---|
| EN | 53/100 | 199/200 | **2,300 / ≤2,300** |
| AR | 51/100 | 194/200 | 2,013 |

**No waiver.** The cap was measured before and after every edit below; note 2 added a word and it
was recovered in the same sentence rather than waived (see note 2). Row 6 remains the only piece in
this publication to have measured its word cap at the writer's desk and held it at the verdict.

**Guardrails, checked one by one and all intact:**
- The **five-definition seam** is whole. The 24,000 is written as a **flow** and the 27,322 / 27,409
  as **stocks**, in the same paragraph, in bold, with the prohibition on any subtraction, share or
  residual stated in both directions. Ruling #68 is carried, not cited.
- **Announced ≠ measured** at every mention of the five-year TTC. The word *announced* is used and
  the piece says in its own voice why.
- The A2→A1 window is carried as **remarks by a named minister on a named date in one newspaper**,
  in the body and not in the close, with the four-channel enumeration behind the stated absence.
  Guardrail A intact: A2/A1/A0 are the ministry's own, the 68,207 carries all three qualifiers in
  one sentence, and the before/after salary pairs do not appear.
- The overlap between the A2 window and the untrained counts is explicitly **not** asserted:
  *"Those are different sets, and nothing read establishes their overlap."*
- **No "best" without a ruler; no composite.** Neither appears; `contains_composites: false` is
  correct.
- The 22,000 national classroom total is separated from the project's 11,000, with the funder's
  conflation named and refused.

---

## The three notes, all found today, all closed in-run in both languages

### NOTE 1 — the serving state the piece reports as a condition of the host had changed in two days. Six annotations in each language. CLOSED.

The pair's annotations state, six times each, that `mineduc.gov.rw` serves its documents behind a
certificate that **expired on 23 September 2026**, that "a reader following this link in any
mainstream browser meets a full-page security interstitial", and that certificate validation
disabled "is the only way to obtain it today". Source 3 leans on the same fact for a uniqueness
claim: the World Bank is "the only source for this piece whose host serves a valid certificate".

**Re-probed at this verdict. None of that is true today.** Measured directly:

```
subject = CN = mineduc.gov.rw
issuer  = C = US, O = DigiCert Inc, CN = RapidSSL TLS RSA CA G1
notBefore = Sep 23 00:00:00 2026 GMT
notAfter  = Apr  9 23:59:59 2027 GMT
serial    = 08C5F3EEE50C8CF981221D5B9C21AB76
```

Same common name, same issuer, **new serial**, valid to 9 April 2027. All six MINEDUC URLs return
HTTP 200 **with validation enabled**, at the same byte counts. The host was renewed between the
09-27 draft and this verdict; the piece would have shipped telling readers that six of its eight
links meet a security wall they do not meet.

**What was wrong is not the observation — the 09-26/09-27 reads were correct and are ruling #70's
origin. What was wrong is the tense.** The annotations state a host's momentary failure as a
standing property, in the present tense, with "today" doing the dating. That is the same defect
class as the two clock items open on this edition since 09-20, arriving on a two-day fuse instead
of a two-month one, and in an annotation instead of a body. **Filed as ruling #76.**

**Closed as follows, in both languages:** source 1's serving-state block is rewritten as **two
dated observations** — what was served on 26 and 27 September, and what is served on 29 September,
each with its date, the second carrying the new certificate's own validity window — and it closes
on the reason for the shape: *a serving state is an observation with a date, not a fact about a
host.* The five repeated "same host, same expired certificate as source 1" notes become "the same
certificate history: served behind an expired certificate on 26 and 27 September 2026, re-probed 29
September 2026 at HTTP 200 with validation enabled". Source 3's uniqueness claim is **bounded to
its dates** and its expiry stated in the same clause — it was true on 24 and 27 September and is no
longer a distinguishing property. The Arabic mirrors all eight edits.

Nothing in either body changed: the certificate never appeared in the prose, only in `sources[]`.
No figure moved. The re-probe is still owed at the wave's confirmation read, and the annotation now
says so in a way that will still be honest whenever it is read.

### NOTE 2 — "the programme begins in September", carried without its year into an edition that ships in October at the earliest. Both languages, one sentence each. CLOSED.

EN: *"what is published is an announcement, dated 10 August 2026, that the programme begins in
September"*. AR: «بأنَّ البرنامجَ يبدأ في سبتمبر». The quotation from the register is verbatim and
correct and is not touched — *"Beginning in September 2026"* is the ministry's own sentence.

The piece's **own** prose then drops the year. Composed on 27 September that reads as a month about
to arrive. This wave's gate target is **11 October** and its outer bound **15 November**: on either
day a reader meets a bare "September" in a piece datelined September, and the sentence stops being
about a named month and becomes about an ambiguous one.

**The claim itself survives the calendar and that is worth stating**, because it is the reason this
is a note and not a return: the piece says *nothing read establishes that the first five-year
cohort enrolled*, and on 11 October that is a **stronger** sentence than on 27 September, not a
weaker one. September will have passed and the record will still be silent. Only the date needed
fixing, not the argument.

**Closed:** "begins in September **2026**" / «يبدأ في سبتمبر **2026**». This is the edition's
**third** instance of the clock class and **the first caught at a pair verdict rather than at a
later calendar re-read** — which is where it is cheapest, and is the answer to the forward question
the 09-20 ledger named (*does a hedge survive its own paragraph?*) asked of a date instead of a
hedge.

**And it cost a word, which is recorded rather than waived.** The EN body measured exactly 2,300
against a ≤2,300 cap; "September 2026" made it 2,301. Rather than take a one-word waiver, the same
sentence gave one back: *"in this sentence and in every other one about it"* → *"in this sentence
and every other one about it"*. Identical meaning, better rhythm, cap held at 2,300 with no waiver.

### NOTE 3 — the two register questions the Arabic composer raised and deliberately did not settle. ANSWERED, no edit.

Routed from the 09-28 gate, and they are the Arabic Editor's to answer, not mine; recorded here
because the ledger requires them answered before the flip.

1. **«المخزون» carrying more weight in Arabic than *stock* does in English.** Answered: keep it.
   The English is doing the same work — the piece sets *flow* and *stock* in bold as technical
   terms precisely because they are not ordinary words in either language, and the paragraph defines
   both in its own sentences before using them. A lighter Arabic word would make the Arabic *easier*
   at the point where the piece wants the reader to slow down. The weight is the instrument.
2. **The gloss opener «أي إنَّ» nine times over.** Answered: keep, and the reason is #72. Every one
   of the eight registers is English, so every gloss in the Arabic is a gloss of an English phrase
   carried in its own language; a *varied* opener would make some glosses read as the piece's own
   voice and others as translation, which is the voice hierarchy #72 exists to refuse. Nine
   identical openers are a convention the reader learns once. Repetition here is a promise that the
   treatment does not change between voices.

---

## Observations for the Verifier, not failures

- **The body numeral multiset is 111 / 111 with zero one-sided figures in either direction**,
  re-measured after all of today's edits. The pair keeps the clean-both-ways property it earned at
  the 09-28 gate — it is the edition's second such pair and the only one to keep it through an
  editorial pass.
- **The `sources[]` multiset is a wider population than the gate measured, and it differs by two.**
  EN 300 / AR 299. Both divergences are benign and pre-existing: the hero caption's `51` against
  «٥١» (the site's Arabic-Indic caption convention, not this piece's choice), and source 3's "all
  30 districts" in EN against «المقاطعات الثلاثين» in AR — where both *bodies* write *thirty* as a
  word. Neither is a defect; both are recorded because an annotation multiset has never been
  measured on this edition and the next pair should not rediscover them.
- **The confirmation read inherits three items** from this pair: the MINEDUC certificate (re-probe
  again, and it has now moved twice), the two candidate first-party Arabic registers recorded as
  **walled, not dead** (#70), and «كيغالي» carried by convention.

---

## Disposition

**PASS. BANKED.** Row 6 enters verification.

Per the 2026-09-06 rule the Verifier's verdict is scheduled **the next run**, one per run in
banking order, and the backlog it enters is **zero**. That closes the edition's last owed cell.

The wave still does not flip. Outstanding and unchanged: clock items **A** (Zambia ¶103) and **B**
(slot 3 ¶94), item **C**'s dateline ruling (ruled today — see
`2026-09-29-ed05-dateline-convention-ruling.md`), the rails owed between rows 5/6 and the wave, and
the confirmation reads.

— The Editor · 2026-09-29
