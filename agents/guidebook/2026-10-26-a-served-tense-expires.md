# Ruling #117 — A served tense expires, and the date is not the defect

**Filed** 2026-10-26, by the daily run, from standing-queue **item 25** taken at the head — the first
served DEFECT ever to take a head under ruling #116, eight days after item 25 was raised and one day
after the bucket that reaches it was created.
**Family** Non-numeric (the fourteenth member) — and the first whose unit is **TENSE**.
**Status** Binding.

---

## The rule, in one line

**A FORWARD-LOOKING DATE IS NOT A DEFECT; A FUTURE TENSE BOUND TO IT IS, THE DAY THE DATE ARRIVES.** A
served sentence written in this publication's own voice that says a thing *will* happen at a date was
true when it was composed and is unverified from the moment that date passes — and it re-asserts itself
every day the page is served. The date needs no correction and gets none. The **verb** does.

## What was asked, and why the count it asked for was the wrong count

Item 25 was raised at the 2026-10-18 weekly review in these words: *22 of 44 published EN pieces and 19
of 44 AR carry a date that has not yet arrived — 78 mentions in EN alone.* The instruction attached to it
was right — *classify each claim arrived-and-now-false · arrived-and-still-true · not-yet-arrived, correct
the false ones in both editions, and leave the rest dated.*

**The unit was wrong, and it was wrong in the direction of being uncloseable.** A date that has not yet
arrived is not a defect: the bytes are right, the reader is not misled, and **the population shrinks by
itself as the calendar moves, with no correction and no run.** Counting it measures the weather. Worse, it
can never reach zero, because every piece this publication will ever ship cites a dated plan.

The population that *is* wrong now is narrower, and it is the complement of the one item 25 named: a date
that **has** arrived, carrying a verb that still points past it. Re-measured today over
`web/src/content/**`, both editions, reference day 2026-10-26:

| | EN | AR |
|---|---|---|
| dated mentions 2026–2040 | 774 | 771 |
| of those, forward-marked | 167 | — (see *the Arabic wall* below) |
| **strong-future, period FULLY arrived** | **18 on 11 pieces** | 20 candidates on 16 pieces |
| **of those, unshielded — our own voice** | **5 on 4 pieces** | **4 on 3 pieces** |

**Nine served sentences. Four pieces.** `2026-06-10-rak-iqra-arabic-diglossia`,
`2026-07-07-turkiye-earthquake-school-recovery` (two), `2026-07-16-australia-naplan-reset`,
`2026-07-28-england-report-cards-first-term`. All four repaired in this run's first commit, both editions.

## The boundary that makes it decidable: the attribution shield

Thirteen of the eighteen EN candidates are **not** defects, and they are not defects for one reason
stated three ways:

1. **A quotation does not expire.** `2026-08-25-zambia-free-education-act` carries *'The polls shall take
   place on Thursday, 13th August 2026'* inside quotation marks. The poll has happened; the register still
   says that; the quotation is still exact. Correcting it would **break** #112.
2. **Reported speech does not expire.** *The New Times of Kigali reported on 24 August 2026 that the two
   extra years will let college graduates qualify at A1* is a claim about what a dated newspaper reported,
   not about what will happen. The subject of the sentence is the report.
3. **A resolved target does not expire.** *clearing the year's target of 64%* is past tense already.

What expires is **our own editorial future with no attributive frame around it** — *from September 2026,
Iqra will run*; *September 2026 … by then the classroom stock … will all be countable*; *the national
results are due in August 2026*; *From September 2026 Ofsted will apply*. Each of those four is this
publication predicting, in its own voice, with the register's authority borrowed and its date left behind.

**So the repair is not a tense change. It is the Edition 05 standing prohibition applied to tense:
`announced ≠ measured, labelled at the figure`.** Each sentence is restated as the register's dated
announcement — *the emirate's May 2026 announcement put Iqra into … from September 2026*; *ACARA's own
key-dates page put the national results in August 2026*; *Ofsted's own 12 June 2026 update put the change
from September 2026* — which is true today, stays true, and **asserts nothing about an outcome nobody here
has re-read.** The two Türkiye sentences keep their date and say plainly that it has passed.

This is why the repair could be done without a network read, and it is also why a second item is owed
rather than closed: **restoring the attribution fixes the false tense; it does not tell the reader what
actually happened in September 2026.** That half is a register read on four pieces and is raised as a
separate row, because *an announcement correctly labelled as an announcement is not a measurement* and
pretending otherwise would be the same defect with better grammar.

## The Arabic wall, and it is the third time this month

#101 made the Arabic edition the **control** for a disputed name, because Arabic cannot carry a Latin
acronym and the composer is forced back to the register. #112 and #113 then measured what that costs in
the other direction — 128 of 134 declined quotation tokens Arabic, 0 acronym anchors across 44 Arabic
bodies. **Tense is the same wall, and it is worse, because here the obstacle is orthographic rather than
lexical.**

English marks the future with a **free word** — `will`, `shall`, `is due` — which a regular expression
finds in one pass. Arabic marks it with a **bound prefix**, `سـ` on the imperfect, and that prefix is a
single letter homographic with the first letter of ordinary words. The detector written for this audit
found 40 AR candidates and **most were nouns**: `سنوات` (years), `ستة` (six), `ستريتس` (Streets), `سيارا`
(Ceará), `سيمسه` (SIMCE), `سيراليون` (Sierra Leone). The first AR pass, written against a closed list of
future *verbs*, missed three real instances — `سيجعلها`, `سيكون`, `سيطبِّق` — and returned instead ten hits
on `بحلول`, which is a **past-completion** preposition in every one of them. **Two passes, two populations,
neither one the subject.**

*A closed list of words cannot detect a bound morpheme.* That is #113's lesson inverted: #113 found a
boundary the artefact supplies (an acronym states its own word count); here the artefact supplies no
boundary at all, because the morpheme is not separable from the word it rides on. So the EN half of this
class is assertable and the AR half is not — by the same means — and any gate built on this ruling must
say so in its header rather than report an AR count of zero as cleanliness.

**And the pair disagreed, once, in the direction that matters.** `rak-iqra` EN said *Iqra **will run***;
the Arabic said *فمن سبتمبر 2026 **يعمل** «اقرأ»* — the bare imperfect, unmarked for tense, which reads
as *runs* and **has not expired.** One of the four pieces carried this defect in English only, because
English made the composer choose a tense and Arabic did not. #86 asked which questions only one edition
can answer; #101 asked which questions one edition is **forced** to answer; this adds the third:
**which questions one edition is forced to answer *wrongly*.** English futurity is obligatory where
Arabic's is optional, so the English composer had to commit to an outcome and the Arabic composer did not
have to — and the edition that was not forced is the one that is still true.

## Binding

1. **An editorial future is written with its register's date attached, or it is not written.** Where a
   piece states that something will happen, the sentence names **who announced it and when** — *the
   ministry's 12 June 2026 update puts the change from September* — never the bare prediction. An
   attributed announcement cannot expire; a bare forecast expires on a known date.
2. **The hand-off to the Editor carries `editorial futures: N, each attributed to a dated register: ☐`** —
   and a hand-off missing the line is returned unread. Same teeth as the dek/title cap (07-27), the
   `annotation == sentence` line (09-13), the named-humans gender line (#86) and the acronym line (#101).
3. **The weekly review's forward-date mandate is re-scoped.** Its present wording — *re-read every
   forward-looking date in every held piece* — has been **vacuous since 2026-10-13**, when Edition 05
   flipped and the operation stopped holding anything. It now reads: *re-read every editorial future in
   the **served** corpus whose date has arrived since the last review.* A held plan is invisible (#18); a
   served plan re-asserts itself every day the page is served (#102).
4. **A gate for this class asserts the EN half and prints the AR half.** Arabic futurity is a bound
   prefix and is not findable by string match; a check that reports 0 for Arabic is reporting its own
   blindness, and must say so where #93's reasoning says so — in the output, not in a floor.

## General form

**A served artefact is read in the reader's present, not in the author's.** Every instrument this
operation owns compares a byte against a fact — a figure against a register, a quotation against a
document, an annotation against a body — and all of those comparisons are **time-invariant**: if they
held on the day of composition they hold today. A tense is not. It is the one property of a sentence that
**the passage of time alone can falsify**, with no byte changing on either side. So the class has no
natural trigger: nothing fails, nothing 404s, no gate reds, and the page goes on saying *will* for as
long as it is served.

*A check that compares two things cannot see a claim that only the calendar can refute.* Which is why
this one needed a date in the rule and a row on the queue, and not a smarter comparison.

---

*Related: [`#18`](INDEX.md) held is invisible · [`#86`](2026-10-04-a-forced-determination-is-still-a-claim.md)
which edition can answer · [`#101`](2026-10-15-an-expansion-the-annotation-never-carries.md) which edition
is forced to answer · [`#102`](2026-10-16-a-name-is-a-claim-about-now.md) a name is a claim about now ·
[`#112`](2026-10-22-a-quotation-mark-is-a-claim-about-somebody-elses-bytes.md) ·
[`#113`](2026-10-23-an-acronym-is-a-boundary-its-name-does-not-have.md) ·
[`#116`](2026-10-25-age-is-not-severity.md) the DEFECT bucket that made this item reachable.*
