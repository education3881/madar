# Arabic Editor's gate: `2026-11-26-qatar-pisa-2025-two-of-three`

**Composition** `content-drafts/drafts/2026-11-26-qatar-pisa-2025-two-of-three-ar.md` · **Edition** 06,
piece 4 · **Read** 2026-11-27 (daily run) · **Cell 5 of eight**

## VERDICT: **APPROVED**, with one substitution caught in both editions and one standing gap recorded rather than invented around.

## Composed, not translated — and what that means on this piece specifically

Every register behind this piece is **English**. The composition reads them directly and renders the
argument in Arabic, keeping each quoted span **in the register's own script**, which is the house practice on
every Edition 06 pair so far.

**That inverts ruling #160, and the inversion is worth writing down.** #160 was earned yesterday on
`2026-11-26-jordan-pisa-2025-counts-from-2022`, whose primary register is Arabic: there the Arabic edition
was the only one in which every quotation was a byte beside a byte, and the English edition carried 19
translations no instrument we own could compare against anything. **Here the registers are English and the
Arabic composition quotes them in English, so BOTH editions' quotations are byte-comparable** — 15
Latin-bearing quoted spans in the Arabic body, every one checked against served text in this run, and 15 in
the English. Neither edition carries a translated quotation at all.

So the asymmetry #86, #101 and #160 describe is a property of **the register's language**, not of the Arabic
edition. **Where the register is in a third language the Arabic edition is the forced, better channel; where
the register is English the two editions are equally checkable; where the register is Arabic the English
edition is the weak one.** Three configurations, and this operation has now shipped one of each inside nine
days.

## Checks run

| Check | Result |
|---|---|
| 15 Latin-bearing quoted spans against served register text | **15 of 15 verbatim**, re-run independently of the Editor's Test 1 |
| Named-human transliteration | **ماتياس كورمان** — Mathias Cormann, the rendering already published in `2026-11-27-thailand-pisa-2025-fourth-list`, so the two pieces cannot drift on one name |
| Gender (#86 clause 1 as amended by #134) | **0 of 1 read from a register.** No register read here carries a pronoun or a gendered title for Cormann, so **no gendered construction is attached to the name in either edition** — the Arabic uses `في كلمةٍ عنوانُها…`, a nominal construction, so no verb agrees with the person. Declared in the annotation as this edition's own abstention, with its date (#86 clause 2) |
| Institution and place names | منظمة التعاون الاقتصادي والتنمية · الجبل الأسود · الجمهورية السلوفاكية / سلوفاكيا (both, because the two registers print both) · تركيا · الإمارات العربية المتحدة · موريشيوس · أوزبكستان · ألبانيا · اليونان · صربيا · لوكسمبورغ · ماكاو (الصين). The press release prints *the Slovak Republic* and the launch speech prints *Slovakia*; both quoted spans keep their own register's form and the Arabic prose does not unify them |
| Emphasis (standing prohibition, settled 2026-11-15) | **Held.** No italic, no tracking, no weight shift on any Arabic run. Emphasis is syntactic and by « ». The Latin runs keep the Latin script's own conventions, which is the prohibition's converse clause |
| Digits | Western digits throughout, matching the registers and the rest of the corpus |
| `dek` / `title` caps | **dek 168/200 · title 26/100** code points, tashkeel counted +1 each |
| Buddhist/other calendars | not applicable; all dates Gregorian in both editions |

## The substitution, caught here and fixed in BOTH editions

The composition quoted the front page's note as *«OECD average science scores fell from 489 to 482 points
between 2015 and 2025.»* — **with a terminal full stop the register does not put there.** The register's
sentence continues past a comma: *"…between 2015 and 2025, while remaining broadly stable among non-OECD
participants at 436 and 437 points, respectively."* Substituting a stop for a comma turns a clause into a
sentence and silently drops what the register went on to say.

**The English edition had the identical substitution**, inherited from the same read, and it had passed the
Editor's Test 1 an hour earlier because Test 1's span check normalises whitespace and quotation marks and was
never asked about terminal punctuation. That is **#159's second cause exactly** — *terminal punctuation
substituted on 6* was one of the four undeclared normalisations that ruling was filed for — appearing on the
next piece but one. Both editions now end the quotation at *2025* and say in prose what the rest of the
sentence is about.

*A normalisation that makes two strings comparable also makes one class of difference invisible, and the
class it hides is chosen when the normaliser is written, not when it is run.*

## The standing gap, recorded rather than invented around

The standing prohibition settled on 2026-11-15 ends: *"The composer marks such a run with its `lang`, which
the accessibility family has wanted since 2026-09-13."* **No Arabic body in this corpus carries a single
`lang="en"` attribute** — counted today across the published pairs, including the two shipped yesterday
under the rule.

This gate does **not** introduce the markup on this piece. Wrapping 15 Latin runs in raw HTML inside an
Arabic markdown body is a change to the served bytes and therefore the Web Developer's, it has never been
run past `qa_arabic_shaping`, `qa_arabic_joining` or `qa_composition`, and a pattern first attempted inside
a piece's own gate is a pattern nobody proved. It is recorded as a **standing-queue row** with its real size
— every Arabic body in the corpus, not just this one — because this is limb two of the 2026-10-04 second
amendment on an obligation rather than a count: *a point-of-filing rule never reconciles backward*, and the
honest move is to state the step discontinuity instead of quietly starting the count at this piece.

## Hand-off lines

`dek: 168/200 · title: 26/100` · `annotation == sentence` re-run on all five sources ·
`named humans — gender read from register: 0 of 1, abstention declared` · `acronyms expanded in the body: 0`
· `cross-language pairs: 0 — every acronym (OECD, PISA) appears in the Arabic as the registers print it, and
no English name is promoted to an Arabic expansion (#141)` · `editorial futures: 1, the same one as the
English edition, about this publication's own conduct and carrying no register's claim`

## Owed next

**Cell 6, the Verifier**, whose instruction from the Editor stands and is reinforced here: re-read Table
I.2.6 and Table I.2.8 **independently of both this gate and the five-test verdict** — two of the Editor's
eight repairs were position errors, and now a third defect on this piece has turned out to be a punctuation
one, so the remaining risk is concentrated in exactly what a normaliser folds away. Then cell 7, the hero
still and share card; then cell 8, the flip with the two forward rails.
