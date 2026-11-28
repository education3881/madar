# Editor's five-test verdict: `2026-11-28-uruguay-pisa-2025-own-account`

**VERDICT: PASS — with four repairs required, all four closed in-run. Title TAKEN, amended.**

Editor, 2026-11-28. Edition 06, piece 7 — the piece the Uzbekistan verdict made conditional, and the
condition was met before the commission rather than after it.

## Test 1 — Sourcing reality. **PASS**, and it was re-run rather than accepted.

All four registers re-fetched at this desk, independently of the drafter's compose-time read:

| Register | Declared | At the Editor's desk |
|---|---|---|
| `pisa.anep.edu.uy` | 200, 87,980 | **200, 87,980** |
| `/equipo` | 200, 46,994 | **200, 46,994** |
| `/Informes_nacionales` | 200, 70,402 | **200, 70,402** |
| `Uruguay en PISA 2025_Reporte ejecutivo.pdf` | 200, 6,397,306, sha256 `88bdb975…d087de1` | **200, 6,397,306, hash reproduces** |

Every URL resolves today to the document the piece claims. The OECD figures were re-derived from the
parsed tables in both captures. **6 of 6 quoted spans verbatim** on an independent re-run.

**And the one figure error in the piece is here, found by reading the register rather than the draft** —
see repair 1.

**Repair 1 (required, closed). "four volumes and a technical report" is wrong.** The 2025 block of
`/Informes_nacionales` lists, in order: `Reporte ejecutivo`, `Volumen 2 Equidad y desigualdad educativa`,
`Volumen 4 Logros en ciencias`, `Volumen 5 Logros en matemática`, `Reporte técnico`. That is **an
executive report, THREE numbered volumes, and a technical report** — and the executive report is not a
volume. The draft both miscounted and promoted a document into a class it is not in.

*The error is instructive about where this edition's counts go wrong.* Five documents are listed; the
drafter counted five and then described four of them with a noun that fits three. **Nothing in the piece
depends on the number** — which is exactly why it survived composition, and why it would have survived to
print: a count nobody's argument rests on is a count nobody re-reads.

**And the repair carries a fact worth more than the one it replaces.** The volumes are numbered **2, 4
and 5**, not 1, 2 and 3. Uruguay has numbered its national volumes **to the OECD's own volume scheme** —
R1 says so in as many words, `Los volúmenes 2, 4 y 5 abordan la equidad educativa y los logros en ciencias
y matemática` — so the national report set is deliberately legible against the international one, which
is the piece's whole subject showing up in the shelf-marks.

## Test 2 — Specificity. **PASS on the repair, and it was the close call the brief predicted.**

Place: Uruguay, named throughout, with the tested population described as the register describes it.
Time: 2025, 2022-to-2025, 2015-to-2025, and the report's own September 2026.

**The named human is the issue, and the brief put the Editor on notice about exactly this:** *the named
human must appear with a function the register states, not as decoration; if the piece has nothing for
Laura Noboa to be named for, the Test 2 debt is not discharged by putting the name in a sentence.*

As drafted, **Laura Noboa appears once, in a credit line**, in a late section called *Who publishes this*,
in a sentence whose grammatical subject is the programme. That is not a fabrication and it is not padding
— but it is a name in an acknowledgements position, and had the piece been returned for it I would have
been returning it for the thing the brief said to watch.

**Repair 2 (required, closed).** The attribution moves to where it does work. The piece's pivot sentence
is *"Uruguay's own report does"* — does what the OECD's chapter will not, print a reading mean. **A report
is not an agent; a programme with a named coordinator is.** The repair names the programme and its
coordinator at the pivot, so the reader learns who is answerable for the figure at the moment the figure
is produced, and the late section becomes a detail rather than a credit.

I am **not** requiring more than that, and the restraint is deliberate: no register read for this piece
says that Laura Noboa decided to publish a reading mean, and a piece that implied it would be composing
an intention from a masthead. **The name carries attribution, not motive.**

## Test 3 — Why now. **PASS.**

Paragraph two: the volumes are dated September 2026, the month the OECD launched PISA 2025. The reader
knows by the third sentence that this is a national account published alongside an international one and
reachable today. Nothing here reads as an encyclopedia entry.

## Test 4 — The dignity check. **PASS.**

Would a senior Uruguayan educator find this accurate and fair? I think yes, and the test is not trivial
here, because the piece reports a system below the OECD average in all three subjects and second to Chile
in one. It does so in the national report's own framing and with the national report's own comparisons,
which is the right way round: the figures that place Uruguay are Uruguay's choice of figures.

**The sentence I weighed hardest and am keeping:** *"A national report that prints its own second place in
the subject where it chose to publish a number nobody else published is doing something worth noticing. It
would have been easier not to print the reading mean at all."* This comes close to imputing a motive. It
survives because what it actually asserts is a counterfactual about ease, not a claim about intent, and
because the observation is **to the register's credit and made in the register's favour**. A piece may
notice that someone did the harder thing.

## Test 5 — Fit with the long arc. **PASS, and this is the strongest piece of the edition on this test.**

A bilingual publication reading a Spanish-language national register in the original, against an
international register in English, and reporting that where the two overlap **they agree** — that is
Madār's method with nothing borrowed. It is also the first Edition 06 piece whose closing section is not
an apology for an unreachable door.

## The three questions handed up

**Q1 — page citation for the 76-page PDF. THE DRAFTER IS UPHELD, with one condition.** The drafter asked
to be overruled rather than print page numbers it cannot stand behind. It should not be overruled. A page
number recovered from an extraction that does not reliably recover page boundaries is **false precision
with a citation's authority**, which is worse than document-level citation by exactly the margin a reader
trusts it. The condition: **the annotation must state the extraction method** so the quotation is
reproducible by a reader who has the same file — a hash plus a method is re-findable; a hash plus a page
number nobody can verify is not. The drafter's hand-off already states the method; it moves into
`sources[]` at this cell.

**Q2 — is the closing too much about us? Partly. Repair 3 (required, closed).** The plain statement stays:
a piece whose argument is *this country published what the report did not* owes the reader an account of
how well we could read what it published, and the two dropped sentences are a real editorial fact.
**What does not stay in the body is the kern threshold of 120 thousandths of an em.** That is a parameter
of our tooling, it belongs in `sources[]` where a checker needs it, and in the body it asks a reader of an
education publication to hold a typesetting unit for no return.

**Q3 — region `Latin America`.** Correct and in scope on the open list. Noted for the stats panel; no
action.

## The title

**TAKEN, with one word changed. Repair 4 (required, closed): *Uruguay printed the number the report would
not* → *Uruguay printed the number the report did not*.**

*Would not* imputes refusal. **The body explicitly declines that framing two paragraphs earlier** — *"This
is not a correction of the OECD and it is not a scoop. The international report is a comparative
instrument and it has reasons for publishing a change where it does not publish a level."* A title that
contradicts the fence its own body builds is the worst place to carry an insinuation, because the title is
what travels: into a tab, a link preview, a feed item and a search result, where the fence does not go.

*Did not* costs the headline nothing and is true.

**The rejected alternative is correctly rejected.** *Uruguay and the OECD agree* is accurate and buries
the piece: the agreement is the setup that makes the rest usable, and the finding is the reading mean.

## Owed at the next cells

- **Cell 4, the AR composition.** By #160 a Spanish register makes **Arabic the forced and better
  channel**: each Spanish span is quoted in Spanish in both editions and neither translates a quotation.
- **#134 is licensed here and must be carried in BOTH annotations:** `/equipo` prints `Coordinadora
  nacional`, feminine where `Coordinador` exists. The determination is read off the register's own token.
  **This is the edition's first licensed determination**, and it arrives on the same day the Verifier
  corrected two pieces for an Arabic determination that no register licensed — the contrast belongs in the
  Arabic gate's reading, not only in this file.
- **Cell 6, the Verifier's,** is the run after the pair verdict. It is owed a re-run of the corroboration
  check: Uruguay's retelling of the international top ten against Table I.2.1. The drafter flagged in
  writing that it was verified by comparing a hand-typed list against a script-parsed one — **two
  different kinds of reading** — and asked for it to be re-run rather than accepted. That request is
  granted and recorded here so it is not lost.
- **Cell 8** must derive its forward rails from the piece's own final `related:`, and
  `2026-11-26-pisa-2025-three-lists-of-risers` is **already at the cap of 6**: displace or decline, and say
  which.
