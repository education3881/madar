# Recon — Uruguay's own PISA register, read in served text 2026-11-28

**Researcher, 2026-11-28, during the content run.** Banked on the day the door was found open, per the
standing rule that an access window has a shelf life. **This is a source index, not a draft**, and it
licenses no quotation: the drafter re-opens every register at compose time (#101).

## Why this was looked for at all

The Editor's cell-3 verdict on the Uzbekistan piece recorded an **edition-level debt** and made it a
condition: *three Ed06 pieces carry Cormann and two carry none, and the seventh piece may not be
commissioned without a named human from a reachable non-OECD register*, or the edition stops at six. That
is a search specification, so it was run as one.

**Doors tested today, all of them measured rather than assumed:**

| Door | Result |
|---|---|
| `moeys.gov.kh` (Cambodia) | **200 with 266 bytes that are a refusal** — `Request Rejected`, a WAF block page. A 200 that is a no. Every path tried returns the same 266 bytes, including `sitemap.xml`. |
| `deped.gov.ph` (Philippines) | **403** direct. Archive holds captures, but **the 2026 captures are themselves 403** — the crawler banked the block page, so the archive route is closed too, not merely slow. |
| `moet.gov.vn`, `meds.gov.mn`, `mineduc.gov.gt` | no answer at all (connection fails) |
| `moe.gov.jo`, `edu.gov.qa` | no answer — **re-tested today** rather than carried from the 11-26 reading (#159's family). Unchanged. |
| `mined.gob.sv` (El Salvador) | 403 |
| `ceibal.edu.uy` | 403 |
| **`anep.edu.uy` (Uruguay)** | **200, 152,208 bytes — and the string `pisa` occurs in its served bytes.** |

**And the open door was found by the link-set method, not the front door.** `anep.edu.uy` carries exactly
one `pisa` link: `https://pisa.anep.edu.uy/`. That is the method that unblocked the Qatar piece — *a
register is a document, not a page* — applied to a ministry instead of to a report, and it worked on the
first host whose front door answered.

## What is behind the door

**R1 · `https://pisa.anep.edu.uy/` — PISA Uruguay, the national centre.** 200, **87,980 bytes**, HTML,
Spanish, extracts cleanly. Carries `PISA 2025` and this sentence, which gives the national sample:
*"PISA-Uruguay de la ANEP presentó los resultados de la evaluación internacional aplicada en 2025, en la
que participaron aproximadamente 6.500 estudiantes uruguayos de 15 años de educación media."* Note the
hedge **`aproximadamente`** — it travels with the figure into any sentence that uses it.

**R2 · `https://pisa.anep.edu.uy/equipo` — the team page. THIS IS WHAT THE EDITOR'S CONDITION ASKED FOR.**
200, **46,994 bytes**. Eight named people with their functions, read in served text:

> **Laura Noboa — Coordinadora nacional.** Paola Cazulo and Amalia Astiazaran — Análisis de datos.
> Bruno Fonseca — Estadística. Juan Francisco Duarte — Informática. Marcela Armúa — Área Ciencias.
> Magdalena Romano — Área Matemática. Martín García — Logística.

**The register prints its own gendered titles, which is #134's admissible evidence and not an inference
from the names:** `Coordinadora` is feminine where `Coordinador` exists. So a gender determination here is
**licensed by the register's morphology**, and both editions carry the token verbatim in their annotations
(#134's binding). **That is the clean contrast with the two corrections the Verifier made this morning**,
where `OECD Secretary-General` is ungendered in English, no register carried a pronoun, and the Arabic was
forced to determine with nothing behind it. *The same ruling that forbids reading gender off a name is the
one that admits reading it off a title the register prints — and this register prints seven of them.*

**R3 · `https://pisa.anep.edu.uy/Informes_nacionales` — the national reports index.** 200, **70,402
bytes**. **Uruguay has published its own PISA 2025 volumes**: `Reporte ejecutivo`, `Volumen 2 — Equidad y
desigualdad educativa`, `Volumen 4 — Logros en ciencias`, `Volumen 5 — Logros en matemática`, and a
`Reporte técnico`. The same index carries the 2022 cycle's eight volumes and national reports back to 2003.

**R4 · `Uruguay en PISA 2025_Reporte ejecutivo.pdf`.** 200, **6,397,306 bytes**, `application/pdf`,
**76 pages**, sha256 `88bdb9752f0a663bb587b6488ca1b82032ffeec6dc9a47d53a7393e54d087de1`. Carries a text
layer. **Imprint read from it: ISBN `978-9915-716-20-6`, ISBN obra completa `978-9915-716-19-0`, and the
date `Setiembre de 2026`** — so the national report is contemporaneous with the OECD's 8 September launch
and is not a later commentary.

### THE EXTRACTION CAUTION, DECLARED FIRST (#158)

**R4's text layer is kerned and partially custom-encoded, and a naive extraction produces text no one
should quote.** Measured: 177,993 characters come out, and they come out like
`R eport e ejecutiv o`, `Adminis tr aci\363n`, `Dir ec ci\363n E duc a tiv a` — inter-letter spacing
promoted to real spaces, accented characters as octal escapes, and the subset fonts carrying their own
encodings. **1,530 runs of 45+ characters are recoverable as prose and the rest is noise.**

Binding on the drafter: **quote from R1, R2 and R3, which are HTML and extract clean. Treat R4 as a
document to read and cite by page, not as a surface to lift spans from**, unless a span is re-verified
character by character against a re-extraction that declares its own method. This is `#158`'s rule applied
before the defect rather than after it.

**And one artefact already visible, flagged so nobody resolves it from the extraction:** the authorities
page yields `Mtra. Daysi Iglesias` beside `CONSEJERO` — a feminine courtesy title against a masculine
role label. That is almost certainly a **column-order artefact of the extraction**, the label belonging to
the next person in a two-column layout, and **not a claim the register makes**. It must be settled against
the rendered page before any name from R4 is used. *An extraction that breaks words also breaks the
association between a name and the label beside it, and the second break is invisible where the first one
is obvious.*

## What the OECD's chapter says about Uruguay, re-derived from the parsed tables in two independent captures

Both captures of Chapter 2 (`20261104162528`, 2,426,000 bytes; `20260910092914`, 2,422,806 bytes):

| Table | Uruguay | OECD average-35 |
|---|---|---|
| **I.2.6**, change 2022→2025 | **9** science, **−7** reading, **−4** mathematics | −3, −14, −9 |
| **I.2.9**, fitted decennial trend | **11** science, **−10** reading, **−14** mathematics | −7, −27, −24 |
| **I.2.8**, low / top performers 2022→2025 | **−4.7** and **0.0** percentage points | 1.2 and −0.3 |

**The editorial fact, and it is the inverse of the Saudi piece:** for Uruguay **the two clocks agree.**
Science is positive on both (+9 and +11); reading is negative on both (−7 and −10); mathematics is
negative on both (−4 and −14). Nothing changes sign with the table. Saudi Arabia was the case where one
subject's sign flips between clocks; Uruguay is the case where none does — **and Uruguay is nonetheless on
both of the release's decade science lists**, the press release's eleven and the front page's
*bucking the trend*, because both of those lists are about **science alone**. A reader who takes either
list as a statement about a school system rather than about one subject gets Uruguay exactly backwards:
its science rose on both clocks and its reading and mathematics fell on both.

Uruguay's `0.0` in the top-performer column of I.2.8 is worth a sentence of its own care: it is a change of
zero to one decimal place, not an absence, and the table prints it where Uzbekistan's row prints `0.5`.

## What this recon does NOT establish

- **No figure from R1–R4 has been traced to a page or a table yet.** The sample sentence and the imprint
  are the only things quoted here, both from clean HTML or from an imprint block.
- **Whether Uruguay's own volumes disagree with the OECD's chapter anywhere** is the question that would
  make the piece, and it is unanswered. It is also the first time in this edition that the question can be
  asked at all, because every previous piece had to write *no first-party register has been read*.
- **Ceibal is a separate matter.** `ceibal.edu.uy` answers 403 and is not needed; Uruguay's one-laptop
  programme is an Edition 08 subject, not a PISA 2025 one, and reaching for it here would be the
  institution-not-geography error in a new coat.
