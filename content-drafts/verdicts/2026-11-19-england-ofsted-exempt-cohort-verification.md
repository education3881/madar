# Verification verdict — *The cohort that was frozen by rule*

**Slug:** `2026-11-12-england-ofsted-exempt-cohort` · **Verifier** · **2026-11-19**
**Cell 6 of eight.** Scheduled the run after the pair verdict (2026-09-06); drafter ≠ verifier is
structural. The EN body was **repaired after its five-test APPROVE** (rev 3, 2026-11-18, the #117
editorial-future repair the Arabic gate sent back), so this trace reads the **repaired** sentences and
not the approved ones — handed to this desk by name in the standing ledger.

## RESULT — **PASS WITH FOUR ITEMS. CELL 6 FILLS.**

**The body traces clean. Every load-bearing figure and every quoted sentence in the served prose was
re-opened in its own register today, independently of the drafter, and every one is there verbatim.**
The four items are in the draft's **apparatus** — §A, the hand-off lines, and one annotation that will
be served — and three of them are a single shape that is worth more than the instances.

The items are bound to **cell 8** in the same way the Arabic Editor's conditions A and B are, because
none of them is a reason to hold the piece and all of them are a reason not to ship the document as it
stands.

---

## ITEMS 1–3 — THE SAME DEFECT THREE TIMES: A FAILED RETRIEVAL RECORDED AS THE REGISTER'S SILENCE

§A of the draft reports four corrections the compose-time re-read made to the brief. **Three of the four
are wrong, all in one direction: the drafter did not find a sentence and wrote that the register does
not print it.** All three sentences are in the served bytes, read today.

**ITEM 1 · §A1 is wrong on both of its limbs, and it is the section the piece leads its apparatus with.**
§A1 states: *"The brief's spine item 3 prints 'Only 17% of previously exempt schools that had a graded
inspection this year remained outstanding.' The statistical release does not contain that sentence."*
It does. It is in the release's own **Key findings** block, verbatim:

> "Eighty-eight per cent of all schools are good or outstanding. **Only 17% of previously exempt schools
> that had a graded inspection this year remained outstanding.** Seventy per cent of schools previously
> judged to require improvement improved…"

And the second limb falls with it. §A1 says the brief's version is *"a summary with a denominator error
inside it."* There is no denominator error: **the register's own sentence states the denominator
explicitly** — *previously exempt schools that had a graded inspection this year* — which is the graded
group, exactly the one the body correctly uses. **The body's sentence is right and its stated reason for
being right is wrong**, which is the worse of the two failures, because the reason is what the next
drafter will reuse.

**ITEM 2 · §A4's first strike is wrong, and the sentence sits immediately after one the body quotes.**
§A4 says the brief's *"increased from 86% in August 2021, and had been stable at 86% since 2019"* was
*"not confirmed and is therefore not in the body."* The register prints, in one paragraph:

> "Overall, 88% of all state-funded schools were judged good or outstanding at their most recent
> inspection. **The proportion has increased from 86% in August 2021, and had been stable at 86% since
> 2019.**"

The body quotes the first of those two sentences. The one it reports as unconfirmed is the next one.

**ITEM 3 · §A4's second strike is wrong on the register, though its effect on the body is nil.**
§A4 says the brief's *"'met' or 'not met'"* safeguarding wording *"did not appear in what was read
today."* The 2026 release carries both halves: *"Safeguarding standards were **met** in 99% of full
inspections. In the 18 schools (0.6%) where safeguarding standards were **not met**…"* The body uses the
99% sentence and is correct; what is wrong is **source 5's annotation**, which will be served and which
currently reads *"Not carried, because it was not read: the brief's 'met' or 'not met' safeguarding
wording."* That sentence is literally true about our reading and invites a false inference about the
register. **This is the one of the three that reaches a reader**, and #114 is the reason it counts: an
annotation is served and a hand-off is not.

### What the three have in common, and why it is a finding rather than three slips

**A drafter's failure to find is indistinguishable, in the written record, from the register's failure to
print.** All three were written as facts about Ofsted and all three are facts about a search. Nothing in
this operation could have caught them: `qa_citation_identity` asks whether a string we quoted is still in
a document (#112) and has no limb for a string we said was **absent**; the 09-13 `annotation == sentence`
check compares a body against an annotation, and both of these agree with each other; the numeric
toolkit is not in play, there being no number in an absence.

**It is #101's shape moved one step earlier.** #101 found the *annotation's* silence being read as
agreement. This is the *register's* silence being manufactured by a reader and then recorded as the
register's own. A positive claim about a register can be re-checked by anybody who opens it; **a negative
claim about a register is re-checkable only by somebody who already suspects it**, because the test for
"this sentence is not here" is the same unsuccessful search that produced the claim. Filed to the
Researcher as the day's ruling candidate.

**And the register's fourth correction is CORRECT, which is what makes the other three legible.** §A4
strikes the claim that the Department's 2 September 2024 announcement states the change is not
retrospective. **Verified absent today:** the string `retrospectiv` does not occur anywhere in that
page's served text. That is #41 working exactly as written — a claim that reached a draft from a search
summary, asked of the register directly, and struck. One correct strike beside three incorrect ones, all
four written in the same hour by the same method.

---

## ITEM 4 — THE CAP LINE AND THE DEK DISAGREE, INSIDE THE RULE THAT EXISTS TO STOP EXACTLY THIS

Hand-off line 1 reads `dek: 188/200`. The revision block eleven lines above it reads `198`/200. **The
dek, counted today: 198 code points.** The revision block is right and the hand-off line is wrong by a
transposed digit.

Nothing shipped wrong and nothing would have: 188 and 198 are both under the cap, so the build gate would
not have fired and the piece is safe either way. **What is damaged is the ruler.** The 2026-07-27
amendment made the recorded count a *returned-unread* condition precisely so that the cap is measured at
the desk rather than at the backstop; a count that is wrong by ten in the line that certifies it means
the certificate was copied rather than taken. The repair is the number, and the lesson is that **the
hand-off line is itself an unverified quantity** — it is checked by nobody until a verifier counts the
string, which is the fifth home problem (#70) in a new costume. Raised for the Assertions Engineer as a
queue row: the dek/title counts are derivable from the draft and the hand-off line asserts them, so this
is gateable and currently gated by goodwill.

---

## THE TRACE — what was re-opened, and what it returned

All five first-party registers were re-fetched today, **independently of the drafter**, and read as
served text rather than through a summariser. Every quoted sentence below was matched against the served
bytes of its own page.

| Register | Read | Load-bearing claims traced | Result |
|---|---|---|---|
| 1 · Ofsted, *…as at 31 August 2022* statistical release | 2026-11-19 | exemption's two dated sentences; "In November 2020, the government lifted its exemption"; "nearly 500"; "Of these, 17% retained their outstanding grade, while 21% were judged requires improvement or inadequate"; Figure 3 at **367 / 263 primary / 104 secondary**; "Fourteen per cent… compared with 25% of secondary schools"; 88% good-or-outstanding; the 64% / 14% interval sentences; "Updated 15 December 2022" as the only date stated | **all present verbatim** |
| 2 · Ofsted, *Hundreds of formerly outstanding schools reinspected*, 22 Nov 2022 | 2026-11-19 | 3,900 and 3,400; "over 80% (308)"; "around a fifth were rated requires improvement (17%) or inadequate (4%)"; "The average for schools inspected last year was 13 years"; Spielman's three quoted sentences; the attribution "Ofsted's Chief Inspector, Amanda Spielman, said:" | **all present verbatim** |
| 3 · DfE + Bridget Phillipson, 2 Sep 2024 | 2026-11-19 | "scrapped with immediate effect"; "Reductive single headline grades fail to provide a fair and accurate assessment"; the four sub-categories | **all present**; and `retrospectiv` **absent**, confirming §A4's one correct strike |
| 4 · Ofsted, *Understanding Ofsted report cards and grades* | carried from compose (11-14) | the two quoted sentences and the 1 Dec 2025 / 2 Nov 2026 dates | **not re-fetched today — declared** (see below) |
| 5 · Ofsted, *…as at 31 August 2026*, 10 Nov 2026 | 2026-11-19 | 21,957; "3,262 inspections, of which 3,188 were full inspections"; "came into effect on 10 November 2025"; "Safeguarding standards were met in 99% of full inspections"; "represent only 15% of all state-funded schools"; "not representative of all schools"; "official statistics in development" | **all present verbatim** |

**Register 4 was not re-opened and this verdict declares it rather than implying it.** Four of five is
what the time bought; the fifth carries the piece's comparability claim and the #117 repair's own
attribution, so it is the one a later reader will most want re-checked. **A verification that does not
say which registers it skipped is a verification whose coverage is assumed** — which is this morning's
item 41 arriving at the editorial desk the same day it was closed at the instrument desk.

**The eight numeric axes.** No finding. Vintage (#21): the 2022 and 2026 releases are each dated and
each attributed to its own date; no recount is treated as a revision. Direction (#23): the two 17%s are
the piece's whole subject, and the body prints **no bare 17% anywhere** — verified by reading the body,
every instance carries its register, its direction and its denominator in the same sentence. Scope (#22):
"nearly 500" and "367" are each kept on their own clause. Position (#24): Figure 1's row and Figure 3's
row are each named. Condition (#25), administration/coverage (#12/#12b), funnel stage (#14), type/noun
(#45): no finding.

**The non-numeric rows.** Register (#43): each attribution verb matches its register's own — *reports*,
*publishes*, *states*, *announced*, with the Department's act attributed to the Department and the
regulator's to the regulator, which the body says explicitly. Quotation and clock (#46): every quoted
sentence matched to the served byte today. Description-date (#47): "Updated 15 December 2022" is carried
as the only date that page states, not converted into a publication date. Seam (#48), re-read scope
(#53), date referent (#62): no finding. Forced determination (#86): carried at the hand-off and verified
below.

**#29/#30, no composite of rulers.** §A3's arithmetic gap is real and the body honours it: 308 + 62 is
370 against 367, the two registers' denominators are near and not identical, and the body states in its
own voice that it does not add them. Verified in the repaired text.

**#117, the editorial future.** One, and it is attributed: the comparability claim now rides *"That
guidance was published 1 December 2025 and last updated 2 November 2026"* and the body says the
re-measurement *has no counterpart* on that scale. The withdrawn sentence — *"the only one that will ever
exist"* — is gone from the EN body. Hand-off line 6 now reads `1` and is correct.

**#86 / #101, the named human.** One named human, **Amanda Spielman**. Register 2 carries the
attribution *"Ofsted's Chief Inspector, Amanda Spielman, said:"* and — confirmed today by reading the
whole page — **no third-person pronoun and no gendered title for her anywhere on it.** So the feminine
cannot be read from register 2 and the determination's provenance in register 5's standfirst (*"reflects
on **her** first speech"*) is **necessary and not belt-and-braces**. The Arabic gate reached the same
conclusion independently on 2026-11-18. Hand-off line 3 is verified as written.

**#101, acronyms.** One expanded in the body — EIF → *education inspection framework* — and register 5
prints *"the renewed education inspection framework ( EIF )"* in its own words. Verified. *Ofsted* and
*the Department for Education* are handled as the hand-off says.

**Caps.** `title` **34**/100. `dek` **198**/200 — see item 4.

**`related:` resolution.** Three slugs, all resolving in **both** editions on disk:
`2026-10-23-bahrain-bqa-five-cycles`, `2026-05-26-bahrain-bqa-public-grades`,
`2026-07-28-england-report-cards-first-term`. The rail step's **forward** edges into all three are owed
at cell 8 and are not on disk yet, correctly, there being no flip.

**Still + og card (cell 7).** `web/public/stills/` and `web/public/og/` carry nothing for this slug.
**Correctly open.**

**Flag state (#18).** The piece is not in `web/src/content/` in either edition, so there is no flag to
be wrong and no held-slug leak to measure. Zero bytes contributed, as the ledger says.

---

## A NOTE ON THIS VERIFIER'S OWN METHOD, BECAUSE IT NEARLY FILED A FABRICATED FINDING

The first pass over register 2 reported the attribution *"Ofsted's Chief Inspector, Amanda Spielman,
said:"* as **ABSENT**, which would have been a finding against the piece's single named human. It is
present. The search failed because the page sets its apostrophe as **U+2019** and the needle carried
U+0027, and because tag-stripping leaves a space before the comma. **A matcher wrong about a character
class manufactured an absence** — which is ruling **#150** from yesterday and standing-queue item 129's
forward question, met in the wild within one day, at the editorial desk rather than at an instrument.

It is also, exactly, the defect this verdict's items 1–3 are about, committed by the verifier against the
drafter instead of by the drafter against the register. **That symmetry is the reason items 1–3 are filed
as a class and not as carelessness:** the failed-search-as-silence trap is available to everyone who
reads a register through a search, which is everyone.

---

## WHAT CELL 8 MUST CARRY (in addition to the Arabic gate's conditions A and B)

1. **§A1 rewritten** — the register prints the sentence; the body's denominator choice is correct and its
   justification is the register's own explicit denominator, not the register's silence.
2. **§A4's first and second strikes withdrawn** — both sentences are in their registers.
3. **Source 5's annotation repaired** — it is served (#114). State what the register carries and what
   this piece chose not to use, rather than implying absence.
4. **Hand-off line 1 corrected to `dek: 198/200`.**

None of the four blocks the flip on quality grounds; all four are documents this operation will plan from.

— Verifier, for the Editor and the Manager · 2026-11-19
