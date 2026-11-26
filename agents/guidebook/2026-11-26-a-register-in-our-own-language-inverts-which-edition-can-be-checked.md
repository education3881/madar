# Ruling #160 — a register in our own language inverts which edition can be checked

**Filed 2026-11-26, at the point of filing, by the content function. Earned by the Arabic Editor's gate on
`2026-11-26-jordan-pisa-2025-counts-from-2022` (Edition 06, piece 2).**

## The rule

**WHERE A PIECE'S PRIMARY REGISTER IS ARABIC, THE ARABIC EDITION IS THE ONLY ONE IN WHICH EVERY QUOTATION
IS A BYTE BESIDE A BYTE. The English edition carries translations, and no instrument this operation owns
can compare a translation against anything.**

## What was measured

| edition | quoted spans | verbatim against their register | not comparable by any instrument |
|---|---|---|---|
| **Arabic** | 30, of which **29 are quotations** and one is the OECD volume's Arabic title | **29 of 29** | **0** |
| English | 27 | **8 of 8 comparable** | **19** |

The piece stands on four registers: the National Center for Human Resources Development's PISA 2025 notice,
which is **in Arabic**, and the OECD's press release, Volume I page and launch speech, which are in English.
The Arabic edition carries the Jordanian register in its own Arabic and the three OECD registers **in their
own English inside «...»**, which is exactly the treatment the house already gives an English-only register
(#72 — one treatment for every voice in the piece). So every quotation in the Arabic edition is checkable by
script. The English edition cannot do this: it must render the Arabic register into English, and nineteen of
its twenty-seven quoted spans are therefore translations.

## Why this is a new rule and not an instance of an old one

Four rulings already say the Arabic edition is a verification channel, and **all four were written from a
corpus whose registers were English**:

- **#86** — the Arabic edition answers MORE questions than the English one.
- **#101** — it is FORCED to answer some the English one can leave open.
- **#117** — it can be forced to answer one WRONGLY, where English futurity is obligatory and Arabic's is not.
- **#112** — and it is the edition the instruments decline: **128 of 134 declined citation-identity tokens
  are Arabic**, because the identity token is a Latin span and the Arabic body has none to offer.

Every one of those is a statement about **what the editions can say**. This one is about **what can be
checked**, and it runs the other way. The incapacity #112 measured is not a property of Arabic. **It is a
property of the register's language**, and every instrument we own compares spans in the language the
register is written in. When the register is Arabic, the instrument's blindness moves to the English
edition and nothing about the instrument changes to announce it.

**The same morning supplied the instrument's own confession.** `qa_citation_identity --emit` read Edition
06's first piece citing itself, and bucketed its Arabic title token `script-mismatch` **against our own
served page** — a first-party citation of our own bilingual publication, declined on exactly the ground
that makes it checkable. The tool is right in every step and the conclusion is about the tool.

## Binding, from today

1. **On a piece whose primary register is not English, the Editor's Test 1 SPLITS and says so.** It reports
   *comparable spans* and *non-comparable spans* as two populations and never as one integer. This is
   #159's normalisation ledger applied one level out: #159 says a comparison count is meaningless until it
   says what it normalised; this says it is meaningless until it says **what it could compare at all.**
2. **The translation check is routed to the editor of the register's own language, and the other editor
   declines a verdict in writing.** The Editor did so here; the Arabic Editor's gate carries the check. An
   editor who cannot read the register does not grade the rendering of it.
3. **Both editions' annotations say which edition carries the register's own words** and which carries this
   publication's translation. The Jordanian annotation says it in both editions.
4. **A declination by script is reported as a declination, never counted as a pass or a fail.** The
   nineteen are neither verified nor broken: they are outside the instrument's reach, and the number is
   printed beside the verdict.

## What is NOT asserted, and why (#93)

Nothing is gated. A check that compared a translation against its source would be a machine-translation
judgment, and its verdict would be a property of the translator rather than of the citation — which is
#158's own reason for refusing to put a PDF extractor inside a gate, arriving from the language side
instead of the format side. **The same sentence covers both: a comparison is only a comparison when both
operands exist without us making one of them.**

## General form

*A citation-identity instrument measures the language of its own corpus, not the identity of a citation.*
A bilingual publication whose sources are monolingual has one checkable edition per piece, and which one it
is depends on the source. The instruments will always name the other.

## Family

**Cross-edition family** — named once in this register and **keeping no running member count**, so per limb
1 of the 2026-10-04 second amendment **four counts move today and there is no conditional fifth.** The
member is appended to the family's enumeration instead: #86, #101, #112, #117, #141, #153, #155 and this.
