# Verification verdict — `2026-11-28-uruguay-pisa-2025-own-account`

**Verifier · 2026-11-28 · cell 6 of 8 · RESULT: PASS WITH TWO CORRECTIONS, both applied in-run.**
Taken the run after the pair verdict, as the rule requires.

---

## Provenance: four registers re-fetched DIRECTLY, and all four reproduced

This is the first Edition 06 piece whose primary registers answer this runner without an archive, so the
re-fetch is a read of the owner's own bytes rather than of a snapshot of them.

| Register | http | Bytes | sha256 | Verdict |
|---|---|---|---|---|
| `pisa.anep.edu.uy/sites/default/files/Uruguay en PISA 2025_Reporte ejecutivo.pdf` | **200** | **6,397,306** | `88bdb9752f0a663bb587b6488ca1b82032ffeec6dc9a47d53a7393e54d087de1` | **reproduced to the byte** |
| `pisa.anep.edu.uy/` | **200** | **87,980** | — | **reproduced** |
| `pisa.anep.edu.uy/equipo` | **200** | **46,994** | — | **reproduced** |
| `pisa.anep.edu.uy/Informes_nacionales` | **200** | **70,402** | — | **reproduced** |

The two OECD registers were re-fetched in the same run for the Uzbekistan verdict and both hashes
reproduced; `oecd.org` still answers **403** direct.

**Quotation channel: EN 6 of 6 register spans verbatim, AR 7 of 8** against the independently fetched
bytes, with five further Arabic `«…»` spans correctly identified as **this publication's own piece
titles** rather than register quotations — which is exactly the ambiguity the Arabic gate raised this
morning as queue item 166, met here for the first time by an instrument that had to be told the
difference by hand.

**And the eighth AR span is correction 1 below.**

## CORRECTION 1 — a stale claim about one of OUR OWN artefacts, created by a repair made in this same run

The Arabic body cited the Uzbekistan piece as **«أكبرُ هبوطٍ في الإصدار»** and the English as
***The largest fall in the release***. **Both were true when written this morning and both were false by
the afternoon**, because the Verifier's FAIL on that piece changed its title in both editions three hours
later. Repaired in all four files (both collection editions and both drafts) to *The largest movement in
the chapter* / **«أكبرُ حركةٍ في الفصل»**.

**Nothing served was wrong — both pieces are held — and that is the only reason this is a correction and
not an incident.** What it exposes is a class with no instrument: **this corpus cites its own pieces by
TITLE in running prose, and nothing checks a title against the piece it names.** `qa_body_links` resolves
`related:` slugs and source URLs; `qa_pair_frontmatter` compares a pair against itself; `qa_citation_identity`
compares a quotation against a third party's bytes. **A title quoted in a body is a claim about an
artefact of ours, and it is the one claim in the corpus with no checker at all** — which is the Uruguay
Arabic gate's own finding of this morning (*a title is a claim about another artefact of ours and it is the
claim we are least likely to check*) earned a second time, in the same piece, by a different route, on the
same day. Raised as queue item **169**.

## CORRECTION 2 — a claim about another organisation's publication scheme, falsified by the piece's own register

The body read:

> The volumes are numbered **2, 4 and 5**, not 1 to 3: Uruguay has numbered its national volumes to the
> OECD's own volume scheme, so the two report sets are built to be read against each other.

The first clause is confirmed. **The second has no register behind it and the piece's own cited index
contradicts it one section lower.** `pisa.anep.edu.uy/Informes_nacionales` was parsed in full:

- **2025:** *Reporte ejecutivo* · **Volumen 2** *Equidad y desigualdad educativa* · **Volumen 4** *Logros
  en ciencias* · **Volumen 5** *Logros en matemática* · *Reporte técnico*.
- **2022:** *Reporte ejecutivo* · **Volumen 1, 2, 3, 4, 6, 7, 8** · *Reporte técnico*.

**Uruguay numbered its 2022 volumes up to 8, and the OECD's PISA 2022 Results had five volumes.** A
numbering that runs to 8 cannot be a mapping onto a five-volume scheme, so *numbered to the OECD's own
volume scheme* is an inference, not a reading — and no register in this piece names the OECD's 2025 volume
list at all. The two registers in hand name **only Volume I, *Future-Ready Students***.

Repaired to say what the index prints and stop: the gaps are the programme's own practice across both
cycles, and this piece does not claim to know what they mean. **The repaired sentence is shorter and
carries a second fact the original did not** — that the gaps are a habit rather than a one-off — which is
the test a correction should pass.

*This is #162's own lesson in the positive direction, filed four hours earlier on the piece one row up: a
claim of absence has no second operand, and so does a claim about a third party's internal scheme. Both
read as facts because of the sentence they sit in.*

---

## The figure trace: everything else CONFIRMED, each re-derived from a parsed register

| Claim | Route | Result |
|---|---|---|
| OECD gives Uruguay's science mean **445** | Table I.2.3 row 44 and Table I.2.1 row 42, both parsed | **445** in both |
| Uruguay's own report gives **444,5** science, **423,2** reading, **404,9** mathematics | the executive PDF, three independent occurrences of each | confirmed, with the register's comma separator |
| The two accounts of science agree | 445 against 444,5 — one number, one rounding convention | confirmed, and the brief's parking condition 3 correctly forbade reporting it as a disagreement |
| **The chapter prints a reading mean for no system** | all fourteen numbered tables parsed; the four that mention *Reading* are I.2.5 (correlations), I.2.6 (changes), I.2.7 (yearly learning gain) and I.2.9 (decennial trends) | **upheld — not one prints a reading mean.** I.2.3's four columns are the overall science scale and three science subscales |
| **The two clocks: I.2.6 gives 9, −7, −4 and I.2.9 gives 11, −10, −14** | both rows parsed | **confirmed exactly**, and nothing changes sign |
| The corroboration check: the report retells the international top ten and the range **509 to 597** | Uruguay's own text against Table I.2.1 parsed in full | **confirmed** — B-S-J-Z (China) 597, Singapore 560, Macao (China) 541, Chinese Taipei 540, Japan 538, Estonia 527, Korea 526, United Kingdom 511, Canada\* 510, New Zealand\* 509: **the same ten systems in the same order with those exact endpoints** |
| The sample, **"aproximadamente 6.500 estudiantes uruguayos de 15 años de educación media"** | the national centre's front page | **verbatim**, and the hedge is the register's as the piece says |
| **Laura Noboa, `Coordinadora nacional`** | `/equipo` | confirmed; #134 licensed on the register's own token and not on the name |
| For the 2025 cycle: an executive report, **three** numbered volumes and a technical report | the index parsed | confirmed |
| The 2025 volumes are **2, 4 and 5** | the index parsed | confirmed |
| dek / title caps | counted | EN title 45/100 dek **186**/200; AR title 41/100 dek **170**/200 |
| `region` | frontmatter | **`LatAm-Caribbean`** in both, the controlled enum, repaired at cell 7 |
| Flag state (#18) | both editions | `approved: false`, no stale duplicate |
| Assets | read as bytes | still 2,968 bytes; og card a **valid 1200×600 PNG**, header parsed |
| Guardrails (#19) | read in the prose | all carried: the rounding convention stated where the two means meet, the extraction method declared where a span is not quoted, the refusal to read motive into a named coordinator stated in the body, and the page-citation decision declared |
| Acronyms (#101) | `qa_acronym_evidence` | clean |
| Served tense (#117) | read | no editorial future on an arrived date |

## Two things PRINTED and not failed on

1. **Uruguay's two first-party registers hedge the same figure differently.** The front page says
   *aproximadamente 6.500*; the executive report says *poco más de 6.500* — *approximately* against *a
   little more than*, and the second has a direction the first does not. The piece quotes the front page
   and attributes the hedge to it, so it is right; but **#38's *a source drifts against itself* now has an
   instance inside one owner's own 2026 publications**, and any future Uruguay piece should quote the
   report's hedge if it is quoting the report.
2. **The top-ten boundary falls on a tie.** Table I.2.1 puts **Australia at 509 as well**, level with New
   Zealand, so eleven systems stand at or above the range's lower endpoint while Uruguay's report names
   ten. That is the register's own cut and the piece reproduces the register, which is correct. Recorded
   because a reader who re-counts will get eleven.

## Disposition

**PASS. Cell 6 CLOSED. Cell 8 is the only cell left, and this piece flips THIRD.** Its `related:` rail
names **two** held slugs — `2026-11-27-saudi-pisa-2025-two-clocks-disagree` and
`2026-11-27-uzbekistan-pisa-2025-only-in-students` — so the corpus fixes the order of all three: **Saudi,
then Uzbekistan, then Uruguay.** Three pieces one cell from the flag, in a derived order, which is the
strongest board this publication has carried and covers the directive's floor for three consecutive days
without a new commission.
