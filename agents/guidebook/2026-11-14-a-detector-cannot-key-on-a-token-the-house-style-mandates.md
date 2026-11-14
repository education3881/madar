# Ruling #142 — a detector cannot key on a token the house style mandates

**Filed:** 2026-11-14, at the point of filing, by the quality function, from the standing queue's own head
(item 38, the oldest row in OPEN at **21 days**, DEFECT bucket empty for a third day).
**Family:** assertion discipline — *how a check earns trust*. The family keeps a running member count and
goes **FIFTY-FOUR → FIFTY-FIVE** (10-04 limb 1's conditional fifth home).
**Working artefacts:** `agents/logs/qa-2026-11-14.md`, `agents/tools/annotation_claims.py`.

---

## THE RULING

**A class's reachability is a property of the CORPUS'S OWN CONVENTIONS, not of the class. Before building
a detector, ask which of its keys this publication's own disciplines have already spent — and if the
answer is the load-bearing one, the class is a Verifier row and not a gate, however clean the idea is.**

Five binding clauses.

**1 · A candidate check is judged on its PRECISION against the whole population, never on its recall
against the founding instance.** Item 38 named one defect and asked for an instrument. The instrument was
built, aimed at the obvious rule, and flagged **13 rows out of 714 served annotations with 0 true
positives.** A detector with that precision is not an unfinished gate; it is a different artefact wearing
a gate's clothes, and shipping it would have turned 13 correct annotations red on every build until
somebody deleted the rule or the prose.

**2 · WHERE THE HOUSE STYLE MANDATES A TOKEN, NO NARROWING WILL EVER REACH INSIDE IT, because both uses
are correct and one of them is compulsory.** The candidate rule was #101 clause 1 moved from an expansion
onto an utterance: *either the annotation quotes the register, or it does not claim the register's
speech*. Its key is the attribution verb. But this operation's standing prohibition is **announced ≠
measured, labelled at the figure** (#117 extends it to tense), so a *correct* annotation is **required**
to print `announced` or `stated` beside a figure — *the announced scale: a target of about 23 lakh
students*; *the 2025 tally as announced at the minister's press conference*. **Nine of the thirteen
flagged rows are the mandated idiom, used exactly as the rule demands.** This is not noise to be tuned
out. It is the publication's own quality rule occupying the detector's only key, and it is the first time
this register has recorded a check defeated by a rule the same register wrote.

**3 · AN ABSENCE CLAIM IS UNQUOTABLE BY CONSTRUCTION, so a rule demanding evidence-by-quotation INVERTS
on it.** The Arabic edition of `2026-05-27-egypt-ekb-decade` had already written the argument down, in its
own annotation, before any instrument was aimed at it:

> وقد ذُكرت الصيغةُ هنا بِلا علامات اقتباس عن قصد، لأنَّ الاقتباسَ ادِّعاءُ أنَّ البايتات تَحملها، وهذا
> ادِّعاءُ أنَّها لا تَحملها.
> *(the form is given here without quotation marks deliberately, because a quotation is a claim that the
> bytes carry it, and this is a claim that they do not.)*

Its claim is that the register titles a named human **by his deanship and not by a doctorate** — a claim
about what is **absent**. A quotation asserts presence. The rule would therefore have demanded presence as
the evidence for absence, and would have reddened the most carefully reasoned annotation in the corpus.
**Generalised: a check that requires positive evidence cannot be pointed at a claim of absence**, and
absence claims are exactly what a careful citation discipline produces more of over time, so this failure
mode gets worse as the corpus gets better.

**4 · The two cheaper grounds are stated because they are the ones a run will hit first.** *(a)* **The
document-type noun occupies the verb**: a wide attribution vocabulary flags 184 annotations and forms with
no English noun reading flag 76, the 108 difference being `Annual Report 2024`, `Situation Report #203`,
`Country Note`, `review reports` — and a citation's whole job is to **name documents**, so the noun sense
dominates by construction. This is 2026-09-14's trap on the input side, now with a measured size. *(b)*
**The verb's subject is not always the register**: *roughly one in three Year 9 students **writes** at a
level expected in primary school*, *the address **printed** inside that certificate*. A string match
cannot read a subject, and these two subjects are a schoolchild and a field in a TLS certificate.

**5 · WHAT IS REACHABLE IS FOUND BY ASKING WHICH CLAIMS SPECIFY THEIR OWN TEST, and the answer was a
class item 38 never named.** 39 of the 714 annotations print a **method together with its value** —
`sha256 d6b62bda…`, `HTTP 200`, `Last-Modified 2026-08-16`, a byte length, a dated fetch — which is
**#113's criterion met by a different artefact**: an acronym states how many words and which letter each
begins with; a sha256 states which function over which bytes. Its offline tier (a read date that has not
arrived, a `Last-Modified` later than the read that observed it, a sha256 that is not hex) is gateable and
measured at **zero violations over all 39**; its network tier cannot gate for #111's reason. **It is not
wired**, because the tier has zero bite and all 39 instances postdate 2026-10-23, so a gate would guard a
convention rather than enforce one. Handed over as queue row **103**.

---

## THE SECOND LESSON, AND IT IS ABOUT ROWS RATHER THAN ABOUT CHECKS

**A row re-states its predecessor's instance, and the instance is the one thing a row never re-measures.**

Item 38 quotes, as the defect it exists to reach, a `gov.om` parenthetical reading *"the issuing body and
its mandate; renamed in 2026"* against a page carrying no rename, no date and no instrument — and states
that it **would still pass today.** It would. There is nothing there to pass. The string left
`2026-06-20-oman-school-performance-ratings` on **2026-10-16** in commit `1552367`, **eight days before
item 38 was raised on 2026-10-24.** The annotation now reads *"…and **says nothing about a rename**"*, and
the rename is carried by its own instrument — *Royal Decree 12/2026, issued 22 Rajab 1447 / 12 January
2026, Official Gazette 1630a of 13 January 2026 — Article I renames…*.

Item 38 inherited the example from item 19's own wording. Nothing was careless: the row's author was
quoting the row it was the complement of, which is the right thing to do, and **the quotation was true
when item 19 wrote it.** What nobody did was re-open the file. This is **#57 pointed at an instance
instead of at a count** — a row's count gets re-measured because a count looks like a number, and a row's
instance does not, because it looks like history.

**Binding, and it costs one command:** a run taking a head **re-reads that row's own named instance in the
current tree before planning the work**, and says in the QA log what it found. Three consecutive days have
now had the head's premise move under re-measurement — 11-12 the printed head was re-measured and the rule
pointed elsewhere, 11-13 the count held and was an undercount, 11-14 the instance was gone — so this is a
rate, not an anecdote.

## THE THIRD LESSON — the proof's failure was worth more than its success

Proved both ways on a `/tmp` copy, injection asserted to have changed the file first (2026-09-14):
control 0 violations, bite **2 of 3**. **Bite 3 did not bite.** Turning one `HTTP 200` into `HTTP 404`
beside a surviving `HTTP 200` in the same annotation exits like a passing control, because the limb can
only ask *all statuses ≥ 400* — and it **must**, since an annotation legitimately records a dead register
beside a live one (yesterday's Ofsted read recorded a `gov.uk` person page that now 404s, in exactly that
shape). **The annotation is not the claim's boundary**: one annotation carries many fetches, so a
per-claim limb has nothing to attach to. That is item 38's own problem one level down, **inside the half
that was supposed to be the reachable one** — and it was found only because the bite was run and watched
rather than assumed.

## WHY THIS IS NOT #93, AND NOT A RESTATEMENT OF #140

- **#93** says a floor above today's reality reds every build. That is a statement about a **threshold**.
  Here there is no threshold: the check's answers would be **wrong**, not merely strict.
- **#140** says an outside boundary locates a population and cannot classify it, so it is a measurement
  and never a gate. That is a statement about a **boundary the artefact supplies**. #142 is the
  complement: the boundary here is not weak, it is **already occupied**, and occupied by us.
- **#141** says an instrument returning *no answer* on a class it reaches is behaving correctly. #142 adds
  the harder case: an instrument that returns a **confident wrong answer** on a class it reaches, because
  the signal it reads was put there on purpose by a different rule.

**The one-sentence form for a drafter:** *before you build the check, grep your own style guide for its
key.*

---

**Counts moved in this commit, six homes:** §3's range (#1–#142), §3's heading, §3's new row 142, §1's
count line (138 rows) and §1's new row 138, `CLAUDE.md`'s non-negotiables (#1–#142), plus the conditional
fifth — the **assertion-discipline family's own member count, FIFTY-FOUR → FIFTY-FIVE**, with the
membership list appended in the same commit per limb 3 of the 10-04 amendment — and the families ratio,
*fifty-five of one hundred forty-two*. Verified by `qa_register_shape`, which derives §3's range from §3's
own rows and fails the build when the prose disagrees.

— Assertions Engineer, with the Verifier · 2026-11-14
