# Ruling #162 — A claim of absence inherits the edge of the enumeration behind it

**Filed 2026-11-28 by the daily run, out of the Verifier's cell-6 FAIL on
`2026-11-27-uzbekistan-pisa-2025-only-in-students`.**
**Family: non-numeric (whether the words around the number are true), member TWENTY-FIVE.**
**Nearest kin: #151 (*a failed search is not a silence*) and #57/#70 (*an enumeration cannot report a
distinction it cannot hold*).**

## The statement

**A PUBLISHED CLAIM THAT A REGISTER DOES NOT CONTAIN SOMETHING IS A CLAIM ABOUT EVERYTHING THE DRAFTER
DID NOT LOOK AT.** A positive claim is bounded by the thing quoted: the span either is in the served bytes
or is not, and one comparison settles it. A negative claim is bounded by **the drafter's enumeration**, and
the sentence never says what that enumeration was — so the claim ships at the width of the register and
is true only at the width of the search. Binding: **a claim of absence is published with its own scope
written into `sources[]` — the set that was enumerated, named — or it is not published.**

## What it cost

The piece's spine was: *the PISA 2025 release measures Uzbekistan's movement in only one of its two units;
the chapter prints no score-point change for it, and a reader who wants the figure behind the front page's
"scores also went up" will not find one in this report.*

Chapter 2 prints Uzbekistan's change in mean science performance **twice**, in score points:

- **Table I.2.12**, *Change between 2022 and 2025 in mean performance in science, by gender* — girls
  **+85**, boys **+80**, gender gap **−5**.
- **Table I.2.10**, *Change between 2022 and 2025 in the socio-economic gap in science performance* —
  disadvantaged **+85**, advantaged **+87**, gap **+2**.

Both are the **largest in their own tables** — I.2.12's 76 entries put Georgia next at +38, and the OECD
average-35 row at −2 and −3 — so the omitted figures were not a footnote. They were the biggest numbers in
the chapter about the country the piece was about.

**Nothing in the piece was wrong except the quantifier.** Every figure was correct; every quotation was
verbatim in two independent captures; the two tables the piece named really are empty for Uzbekistan, and
their notes really do say why. The drafter enumerated **two** tables — I.2.6 and I.2.9, the two that print
a single all-system change — generalised to *the unit*, and wrote the generalisation into the title, the
dek, the hero still's reading and both editions' body. **Four tables in that chapter report a change in
score points, and the two the drafter did not open are the two Uzbekistan is in.**

## Why no instrument could reach it

Every comparison this operation owns puts one byte beside another. A positive claim has a second operand
by construction — the register. **A negative claim has no second operand**: there is no byte to compare a
*nothing* against, and the only thing that would falsify it is a read of a surface the sentence does not
name. `qa_citation_identity` confirmed every span. `qa_annotation_figures` found every annotation quantity
in a body. `qa_claim_registers` found the register archived. The Editor's Test 1 re-fetched the register
and compared what was quoted. **All of them were right, and the piece was wrong**, because none of them
was looking at the tables the sentence had silently excluded. This is #151 one step further out: #151 said
*a failed search is not a silence* about a search that returned nothing; this says **a search that was
never run reads exactly like a search that returned nothing**, and a published absence does not record
which it was.

## Why the mechanism is the chapter's and not the drafter's

Worth keeping, because the repaired piece turns on it. The two empty tables are gated on conditions that
have nothing to do with the subject being reported: **I.2.6** shows only systems comparable *"in all three
subjects"*, **I.2.9** needs *"at least two previous assessments"*. **I.2.10 and I.2.12** ask only that
2022 and 2025 be comparable at all. Uzbekistan clears the second pair and fails the first, so it appears
in every table that splits the change by a student characteristic and in none that prints it whole. **A
system can be comparable in the subject a table reports and still be absent from that table** — which is
the fact that made the drafter's two-table enumeration look complete. The absence had a plausible reason,
and a plausible reason is what stops a reader asking where else to look.

## The binding practice

1. **A claim of absence names its population in `sources[]`.** Not *the report does not print X* but *X is
   not printed in any of the following, enumerated in served text:* — and then the list. The Uzbekistan
   repair now carries every one of the fourteen numbered tables in Chapter 2 and the eight that hold an
   `Uzbekistan` cell, by name.
2. **The hand-off to the Editor carries `claims of absence: N, each with its enumerated population in
   sources[]: ☐`**, and a hand-off missing it is returned unread — the same teeth as the dek/title cap
   (07-27), `annotation == sentence` (09-13), the named-humans gender line (#86), the acronym line (#101)
   and the editorial-futures line (#117).
3. **The Verifier enumerates the population, not the claim.** The route to this finding was mechanical and
   cheap: parse all fourteen tables, print every cell equal to the subject's name. Thirty seconds. For a
   piece whose spine is an absence, **that sweep is the verification** — comparing the figures that are
   present can only ever confirm what the drafter already looked at.
4. **A negative spine is a park-or-enumerate decision at cell 1.** The Editor's brief for a piece built on
   an absence states the population the absence will be claimed over, before drafting, so the drafter's
   enumeration is the Editor's and is on file.

## The general form

*A positive claim is checked against the world; a negative claim is checked against a search.* So the
search is the artefact that has to be published — and an operation whose instruments all compare two
bytes will be structurally blind to every sentence whose subject is the absence of one.
