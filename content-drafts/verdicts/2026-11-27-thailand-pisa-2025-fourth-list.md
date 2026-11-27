# Editor's five-test verdict: `2026-11-27-thailand-pisa-2025-fourth-list`

**Draft** `content-drafts/drafts/2026-11-27-thailand-pisa-2025-fourth-list.md` · **Brief**
`content-drafts/briefs/2026-11-27-thailand-pisa-2025-fourth-list-brief.md` · **Edition** 06, piece 3 ·
**Read** 2026-11-27 · **Editor** acting on the content run

## VERDICT: **PASS, with two notes closed in-run.** Title taken: *Thailand's fourth list*.

## Test 1, sourcing reality. PASS

Every URL in the frontmatter was opened in this run, before this verdict was written, and every register was
read in served text rather than through a summary. The two IPST registers answer this runner **directly**;
the three OECD registers do not, and were read from the Internet Archive's own snapshots of the OECD URLs,
which is recorded in each annotation. `www.oecd.org` answered 403 again this morning and the refusal was not
routed around.

| register | read how | bytes | sha256 (first 16) |
|---|---|---|---|
| R5 IPST PISA 2025 notice | **direct**, `pisathailand.ipst.ac.th` | 184,426 | `8edbc1b1783c3e3b` |
| R6 IPST nine-cycle score series | **direct** download, xlsx | 73,730 | `2c46edde2ac56f37` |
| R1 OECD press release | Archive snapshot 2026-11-15, re-fetched today | 1,468,371 | `096bb651ddbda014` |
| R2 OECD Volume I full-report page | Archive snapshot 2026-11-16, re-fetched today | 1,614,913 | `01b2bd4aa78bf802` |
| R3 OECD launch speech | Archive snapshot 2026-11-15, re-fetched today | 1,464,823 | `33b350b2803a4906` |

All three OECD figures are **byte-identical to the read banked on 2026-11-26**, which is #101's requirement
satisfied by re-fetching rather than by trusting the bank.

**The body's six quoted spans were checked one at a time against the served text, not against the draft.**
Four are verbatim in the OECD registers (List A in R2; *Check against delivery* and the since-2022 sentence
in R3; the 85-point equity sentence in R1). Two are translations and are checked differently: the
eight-name sentence is this publication's own English for one Thai sentence whose full 182-character
original is present in R5's served bytes, and *"statistically significant in the three fields"* is the
translation this publication published yesterday from Jordan's Arabic register, re-read from our own
article file so the two pieces cannot drift apart on one register's wording.

**The axes (#21–#25).** Every load-bearing figure in the body carries its scale, its two years and whose
average it is. The three that needed watching:

- **Vintage.** R5 is dated 8 September 2026 and marked revised 9 September 2026. The piece uses the revised
  served text and says so in the annotation.
- **Scope.** The eight-name list's qualifier — statistical significance, in all three domains, against 2022
  — governs the whole list and is carried in the sentence that prints it. The OECD averages R5 reports are
  attributed to R5 wherever R1 and R2 do not carry the same figure, and the annotation enumerates which do.
- **Position.** Every pre-2022 Thai figure is a row of R6 and no other register. The two rank statements
  are counted from those rows in front of the Editor, not characterised.

## Test 2, specificity. PASS after note 1

Place, span and institution are named throughout: Thailand, nine rounds dated 2000 to 2025, the national
centre by name, four named school-group authorities.

**Note 1, closed in-run.** The draft named **no human at all**, and neither IPST register names one — not
the notice, not the invitation page, not the institute's own news item on the same results. The Editor did
not wave the test through on the ground that the register is institutional. It went looking for where a
human was already load-bearing, and found one in the piece's own logic: **List A's sentence carries no
period of its own**, so the whole eight-of-sixteen comparison depends on the OECD Secretary-General's
launch speech to put the sixteen on a three-year clock. That dependency was implicit in the draft and is
now a paragraph, naming **Mathias Cormann** and marking the page's own **"Check against delivery"**. A
named human who is load-bearing was available all along because the piece could not be written without
that sentence.

**Gender:** no register read here states it, so the body carries no pronoun for Cormann, and the Arabic
composer is instructed to avoid gendered verbs and gendered relative pronouns in the same sentence
(#86 clause 1). The same instruction applies to the institute, which is an institution and takes no person.

## Test 3, why now. PASS

Paragraph one dates the register to the day of the global launch and states the finding: the national
centre printed a list the international release does not carry. By paragraph two the reader has the list.
PISA 2025 is eleven weeks old, this edition opened yesterday, and nothing in the piece would read the same
at any other time.

## Test 4, dignity. PASS after note 2

A senior Thai educator reading this would recognise the register and the arithmetic. Three paragraphs were
read specifically for condescension and one was changed.

**Note 2, closed in-run.** The draft of the nine-round section carried the claim that Thailand's 2025
science average was its **second-highest ever**. Counted against R6's own nine rows it is the **third**,
behind 2012's 444 and 2000's 436. The brief carried the same error, filed from the feeling of a 23-point
rise rather than from the rows; the brief now carries the correction above its own paragraph rather than a
silent edit, and the body says third. **This is #57 inside one run** — a count checked against an
impression of a series instead of against the series — and it is exactly the shape the non-negotiable
warns about, which is why it is recorded here instead of fixed quietly.

Checked and left standing: the piece does not call any school group better or worse than another, names
them as the administrative authorities R5 names, and reports the institute's recommendations as
recommendations rather than converting them into causes. The word *recovery* appears once, in a sentence
saying it should be read **after** the nine rows, which is the opposite of a flourish.

## Test 5, the long arc. PASS

This is the third piece of Edition 06 and the second to reach a national register in a language that is
neither English nor Arabic. It extends the edition's opening method — a list is only as good as its clock —
to a register the OECD does not publish, and it does the one thing a comparative education publication can
do that an aggregator cannot: it counts two quoted lists against each other and shows the overlap. It also
answers the slate's own blocker in a way the next three pieces can reuse: **a candidate recorded as
"OECD-wide, needs a geography" is not blocked; it is unanchored, and an in-scope geography with a reachable
national centre anchors it.**

## Measured at compose

- Title 22 characters. Dek **199** code points, against the schema's 200 limit.
- Body **1,471 words** as drafted and **1,558** after note 1, inside the brief's 1,300 to 1,800.
- Nine table rows, 27 figures, every one traceable to R6's national row.
- Six quoted spans, four verbatim-checked against served OECD bytes, two translation-checked as above.

## Prohibitions, checked one by one against the body

| Brief's prohibition | Held? |
|---|---|
| No computed distance between Thai and OECD averages except where R5 computes it | **Held.** The only two computed distances in the body — the 55-against-85 science gap and the proficiency shares — are R5's own comparisons. Elsewhere the figures sit side by side and the reader does the subtraction or does not. |
| OECD averages attributed to IPST where R1/R2 do not carry them | **Held.** The body says "the OECD averages the institute reports". The 14, 9 and 3-point OECD falls against 2022, which only R5 carries, are in the annotation and were kept out of the body. |
| "Statistically significant" travels with the eight-name list | **Held**, in the quoted sentence itself. |
| Nothing about why any of the eight rose | **Held.** No cause appears. |
| No rank for Thailand | **Held.** No rank, and R5 prints none. |
| The subset shown, not asserted; no "omitted" or "suppressed" | **Held.** Both lists are quoted in full and the paragraph after them says in as many words that a question nobody asked is not a question avoided. |
| The other seven names appear once, uncharacterised | **Held**, except Jordan, which the brief licensed as corroboration and which gets one paragraph with a rail instead of a figure. |
| School groups keep IPST's names, no ranking | **Held.** |
| No unconverted Buddhist-era year | **Held.** 2569, 2568 and 2570 appear nowhere; 8 September 2026, August 2025 and 2027 appear. |
| Every figure carries scale, years, whose average | **Held**, re-read sentence by sentence. |
| No editorial future without a dated register (#117) | **Held.** The one forward statement is the 2027 publication of the self-regulated-learning results, which is R5's own. |

## Owed next

Cell 4, the Arabic composition, with the instruction above on gendered verbs; cell 5, the Arabic Editor's
gate, which also owes the Arabic rendering of the institute's name and of Thailand; cell 6, the Verifier,
whose first job is to re-count R6's nine rows **independently of this verdict's reading of them**, because
note 2 is precisely the error a second reader catches; cell 7, the hero still and the share card; cell 8,
the flip with the three forward rails.
