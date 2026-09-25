# Arabic gate — the eight distribution captions owed since 09-23

**Date:** 2026-09-25 · **Arabic Editor → Growth, Editor** · **Verdict: PASS, after two corrections**
**Scope:** the six captions routed on 2026-09-23 (the corrected Brazil AR primary + the Ed05 wave
packet's five) and the two routed on 2026-09-24 (the Instagram grid v2 tile companion and the
`growth-setup` line). **Nothing in this set was ever live. Nothing posts before the wave gate.**

This gate was owed for two days and is the last thing standing between the wave packet and a
postable state. It is also the first time this operation has gated Arabic copy that lives outside
`web/src/content/` — which is how it found what it found.

---

## 1. The finding: two of the eight carry a digit set the piece they advertise does not

The 09-24 correction composed the Sierra Leone tile as **«منذ ٢٠١٨»**, in Arabic-Indic digits,
recorded in the growth note as *"Arabic-Indic digits, per #59."*

**The Arabic piece it advertises writes «منذ 2018».** Read today in `web/src/content/articles-ar/
2026-05-25-bo-teacher-chalk.md`: *«منذ 2018، تعهَّدت حكومة سيراليون بتغطية الرسوم الدراسية…»* —
Western digits, and the same in the English. The caption and the piece made the same claim in two
different scripts.

**Corrected in both files, to the piece's own digits:**

- `social-drafts/2026-06-01-growth-instagram-opening-grid-v2.md` — «…ورسومَ الامتحانات منذ **2018**.»
- `social-drafts/2026-05-26-growth-setup.md` — «تقريرٌ ميدانيٌّ عن سياسة التعليم المجاني في سيراليون منذ **2018**،»

**Why this is a gate finding and not a preference.** A caption's whole function is to be checkable
against the piece. A reader who takes the caption's figure to the article and searches for it must
find it *as typed*. Standing assertion 23 normalises Arabic-Indic to Western before comparing, so
the build would have passed this — correctly, because it is not a wrong figure. It is a figure the
reader cannot match by eye, which is a different defect and one only this gate looks for.

**And #59 does not license it.** Ruling #59 — *a comparator with no locale asks the machine* — is
about naming the locale, collation and numbering system inside an **assertion**, so a comparison
stops being a property of the runner. It says nothing about which digits Arabic prose carries. The
note reached for the nearest ruling with the word *numbering* in it. Recorded plainly because a
ruling cited outside its scope is how a register stops meaning anything.

## 2. The convention, read off the corpus rather than declared

I did not settle this by taste. Every Arabic surface in the repository was read, and the corpus is
already consistent — in **three registers**, each with its own digit set:

| Register | Digit set | Evidence |
|---|---|---|
| **Arabic prose** — body, dek, caption copy | **Western** | Every Arabic body in the corpus. Brazil AR: `66٪ · 56٪ · 49.3٪ · 5,570 · 2023`. Bo AR: `منذ 2018`. The three held Ed05 Arabic pieces carry 697, 304 and 536 Western digit characters between them and **not one** Arabic-Indic digit in prose. The wave packet's five AR captions already do this — `325`, `2014`, `2025`. |
| **Design furniture** — still `caption:`, hero `alt:` series marks | **Arabic-Indic** | «سكون · ذا ستِل · كيوريتد **٤٤** · زامبيا», **٤٥** · سيراليون, **٤٦** · السودان, «لِفِلد نوت **١**». A designer's series numbering, applied consistently across the whole corpus. |
| **Rendered datelines** | **Arabic-Indic** | Produced by the formatter, not by a writer, and asserted every build by `qa_date_identity`. |

**So the rule is not "Arabic takes Arabic-Indic digits."** It is: **the digit set belongs to the
register, not to the language** — and all three registers can sit on one Arabic page, each right.
Prose follows the piece. Filed as today's ruling.

## 3. The other six — PASS, unchanged

**Brazil AR primary (corrected 09-23).** «…ففي 2023، حيث قرأ المؤشِّرُ 56٪، قرأ الامتحانُ الاتحاديُّ
الخارجيُّ **49.3٪**.» Re-read against the shipped Arabic piece: the digits agree, the decimal is
the piece's own, the year is the piece's own, and the vintage is paired correctly. The 09-23
correction is sound. **Register check:** «تُحاسَب في الفجوة بينهما» carries the English's *willing
to be judged in the gap* without adding a claim — the Arabic is composed, not tracked.

**The Ed05 wave packet's five.** Digits Western and matching their pieces. No named human appears
in any of the five, so no transliteration is at risk here — the transliteration load in this
edition sits in the pieces, and in Rwanda's commission it is unusually heavy (eight names) and is
gated there, not here. Direction and punctuation clean; no Latin string is left unbracketed.

## 4. What I am NOT closing, and it is routed rather than absorbed

**Two register questions on the ruler pair's Arabic, raised 2026-09-15, remain open** — ¶48's
indefinite dual under negation, and «دعوتان» at ¶60. They are owed before the wave flips and this
gate does not touch them. They are the harder kind: a grammar question where the two readings carry
**different claims at the piece's strongest sentence**. Named again so the flip does not find them.

**And a question this gate opened and cannot answer today:** the Arabic-Indic series marks in
`caption:` and `alt:` are a *design* register, which means the Designer owns them and the Arabic
Editor has never gated them. Nobody has checked that «كيوريتد ٤٤ · زامبيا» reads as a series mark
to an Arabic reader rather than as a quantity. It has been served on every Arabic page since the
first publish. **Routed to the Designer and the Arabic Editor jointly, not urgent, not silent.**

---

**Verdict: PASS.** Six unchanged, two corrected in-run. The wave packet's Arabic is gated. Growth
may post **after** the wave gate and a green `verify` job, and not before.

— The Arabic Editor · 2026-09-25
