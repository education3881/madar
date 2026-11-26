# Arabic Editor's gate: `2026-11-26-jordan-pisa-2025-counts-from-2022`

**Arabic Editor · 2026-11-26 · cell 5 of eight.** Composition judged:
`content-drafts/drafts/2026-11-26-jordan-pisa-2025-counts-from-2022-ar.md` (Arabic Content Creator).
**Also judged, because cell 3 routed it here: the ENGLISH edition's nineteen translated quotations.**

## VERDICT: **APPROVED**, both editions, and with one finding recorded that the Editor could not have made.

## 1. The finding, first, because it changes what this gate is

**This is the first piece in the corpus whose primary register is Arabic.** Every piece before it read
English registers and composed Arabic from them, so Arabic was always the edition that had to translate.
Here it is the other way round, and the consequence is measurable rather than rhetorical:

| edition | quoted spans | verbatim against their register | unverifiable by any instrument |
|---|---|---|---|
| **Arabic** | 30 | **29** | **0** |
| English | 27 | 8 | **19** |

The Arabic edition carries the Jordanian register in its own Arabic and the three OECD registers in their
own English, inside «», which is exactly how the house already carries an English-only register (#72: one
treatment for every voice in the piece). So **every quotation in the Arabic edition is a byte beside a byte.** The thirtieth «...» span is not a
quotation at all but the Arabic title of the OECD volume, and it is declared here rather than counted,
because the house uses «...» for titles as well as for quotations and a span check cannot tell them apart.
The English edition cannot do this: it must render the Arabic register into English, and nineteen of its
twenty-seven quoted spans are therefore translations that `qa_citation_identity` would decline.

#86 said the Arabic edition answers MORE questions than the English one. #101 said it is FORCED to answer
some. #117 said it can be forced to answer one wrongly. **This adds a fourth: on a piece with a non-English
primary register, the Arabic edition is the only one in which the citation identity is checkable at all** —
and the operation's instruments read it as the weaker edition, because they measure Latin spans.

## 2. The nineteen, checked by reading, which is the only test available

Each English rendering was read against the Arabic it renders, sentence by sentence. All nineteen are
faithful. Four were tightened and one carried a substantive error, now fixed in both editions:

- `القرائية` is literacy, and PISA's third domain is reading. The English renders it *reading* throughout
  and the annotation records the register's own word. The Arabic keeps القرائية, because changing a
  register's word inside its own language is the one thing a composition may not do.
- `مدارس الريف والبادية` is **rural schools and badia schools**, two named school categories, not a
  rural-versus-urban contrast. The English says so.
- `السلطات التعليمية` is *educational authorities* — the register's administrative term for the Ministry,
  UNRWA, private and military-culture providers. Rendered as that and not as "sectors".
- The register names the ministry in two forms. The English reproduces each where the register prints it
  rather than normalising to one, and says so in the annotation.
- **The error:** an earlier English line attributed the press conference to the centre and placed it in
  Amman. The register names no convener and no venue. Struck in both editions at cell 3.

## 3. Named humans. All three CONFIRMED from the register's own spelling

| register | English | basis |
|---|---|---|
| الدكتور عبدالله عبابنة، رئيس المركز | Dr Abdullah Ababneh, president, NCHRD | standard transliteration of عبدالله / عبابنة |
| الدكتور عماد عبابنة، المنسّق الوطني | Dr Imad Ababneh, national PISA coordinator | عماد as Imad, not Emad, matching the corpus |
| الدكتور عزمي محافظة، الوزير | Dr Azmi Mahafzah, Minister of Education and Human Resources Development | محافظة as Mahafzah; it is a family name here, not the noun |

**Two of the three share a surname and are different people.** The register distinguishes them by given
name and by post, and both editions do the same every time either is named — no bare "Ababneh" appears in
either edition. **Gender:** the register uses masculine agreement for all three, so both editions follow the
register rather than assuming.

## 4. Register and composition

Neutral fusha. The piece was composed, not mirrored: the Arabic opens on the launch and the notice rather
than on the English edition's first clause, the three open questions are set as Arabic questions, and the
closing sentence is an Arabic sentence rather than a translated one. Acronyms keep the Latin tag with the
Arabic name on first mention (#28a). `بيزا` is used as the register itself uses it.

## 5. Figures travel with their axes

Every figure carries its two years, its subject and whose average it is, in the same sentence, in both
editions. **No figure is computed in either edition** — no difference, no percentage, no ratio. The
fifteen quantities were re-checked against R4's served text from the Arabic side: all fifteen present as
printed.

## 6. What this gate deliberately does NOT clear

The three OECD spans the Arabic carries in English are verbatim, but the Arabic edition's *annotations*
render their sense in Arabic. A reader of the Arabic annotation is reading this publication's Arabic for an
English register's claim. That is the same class as the English edition's nineteen, one layer out, and no
instrument reaches it either.

Measured: title 21 characters, dek 198 of 200 code points (tashkeel counted +1 each), body 1,424 words.
`country: Jordan` resolves in `web/src/lib/i18n-geo.ts` (الأردن) — no new key needed.
