# Ruling #64 — a digit set belongs to the register, not to the language

**Filed:** 2026-09-25 · **Daily run, Arabic Editor's gate** · **Section 1 row 59**
**Family:** composition discipline / the annotation and the sentence — with a limb in *citing a ruling inside its scope*
**Origin case:** a corrected Arabic caption written in Arabic-Indic digits against a piece that writes Western ones.

---

## The statement

**Which digits a number is written in is a property of the register it sits in, not of the
language the sentence is in.** One Arabic page can carry three registers, each with its own
digit set, and all three can be right at once:

- **Prose** — body, dek, caption copy — takes the digits **the piece itself uses**, because a
  caption's function is to be checkable against the piece, and a reader who carries a figure
  from the caption to the article must find it *as typed*.
- **Design furniture** — a still's `caption:`, a hero's `alt:` series mark — takes the set the
  designer has applied across the corpus, because a series mark is an ornament, not a quantity.
- **Machine-rendered values** — datelines, listing dates — take whatever the formatter is told
  to emit, and that instruction is named explicitly (#59) and asserted every build (#60).

**The operational form:** *do not ask what language this sentence is in; ask what this number is
part of, and match that.* "Arabic takes Arabic-Indic digits" is the wrong shape of rule — it is
true of one register out of three and it crosses the other two.

**And the limb, which is the reason the defect got written at all:** a ruling cited outside its
scope licenses nothing. The correction was recorded as *"Arabic-Indic digits, per #59"*. #59 is
about naming the **locale, collation and numbering system inside an assertion** so a comparison
stops being a property of the runner; it has nothing to say about which digits Arabic prose
carries. It was the nearest ruling with the word *numbering* in it. **A register only means
something while its numbers are load-bearing** — a ruling reached for by keyword is a ruling
spent.

---

## The origin case

Standing assertion 23 (`qa_packet_figures`, filed 09-23) checks that every numeral in a
distribution caption appears in the shipped text of the piece it advertises. On 09-24 the Growth
sweep found the Instagram grid's tile 1 advertising *"Sierra Leone marked **ten years** of its
Free Quality School Education policy in 2026"* against a piece that says *"From 2018"* and marks
no anniversary. Corrected the same run, in both languages. The Arabic correction read:

> «تغطّي سيراليون الرسومَ الدراسية والكتبَ المدرسية ورسومَ الامتحانات منذ **٢٠١٨**.»

The Arabic piece it advertises — `articles-ar/2026-05-25-bo-teacher-chalk.md` — reads:

> «**منذ 2018**، تعهَّدت حكومة سيراليون بتغطية الرسوم الدراسية…»

Same claim, same year, two scripts. **The build passes this and is right to**: assertion 23
normalises Arabic-Indic to Western before comparing, so the numeral multiset agrees. It is not a
wrong figure. It is a figure the reader cannot match by eye — a different defect, and one only a
human gate looks for.

## Why the corpus settled it and taste did not

The convention was not declared today. It was **read off every Arabic surface in the repository**,
and the corpus was already consistent:

| Register | Set | What was read |
|---|---|---|
| Arabic prose | **Western** | Brazil AR: `66٪ · 56٪ · 49.3٪ · 5,570 · 2023`. Bo AR: `منذ 2018`. The three held Ed05 Arabic pieces carry **697, 304 and 536** Western digit characters between them and not one Arabic-Indic digit in prose. The Ed05 wave packet's five AR captions already do it: `325`, `2014`, `2025`. |
| Design furniture | **Arabic-Indic** | «سكون · ذا ستِل · كيوريتد **٤٤** · زامبيا», **٤٥** · سيراليون, **٤٦** · السودان, «لِفِلد نوت **١**» — a series numbering, applied consistently since the first publish. |
| Rendered datelines | **Arabic-Indic** | Emitted by the formatter, asserted every build by `qa_date_identity`. |

Two captions out of eight crossed register; both corrected in-run. The other six were already
right, which is the evidence that this is a convention the operation has rather than one it is
now inventing.

## The corollaries

**Corollary 1 — a normalising check is silent on presentation by design, and that silence is not
a gap in the check.** Assertion 23 compares *quantities*; it must normalise, or an Arabic caption
could never be checked against an Arabic body at all. The presentation question belongs to a gate,
not to a build. **Do not widen a check to cover what a human is supposed to look at** — that is
how a check acquires opinions it cannot defend (#63, the same instinct in a different costume).

**Corollary 2 — copy that lives outside `web/src/content/` has never had a register.** This is
the first Arabic gate this operation has run on distribution copy, and it found something on its
first pass, which is the 08-16 pattern exactly: *a green check is scoped to what it enumerates*,
and nothing had ever enumerated the Arabic in `social-drafts/`.

**Corollary 3 — the ornament register has never been gated by anyone.** «كيوريتد ٤٤ · زامبيا»
has been served on every Arabic page since 2026-05-25. It is the Designer's, the Arabic Editor
has never read it, and nobody has established that it reads as a series mark to an Arabic reader
rather than as a quantity. Named, routed, and deliberately not answered here.

---

**How to apply it.** When composing or gating any Arabic copy: locate the number's register
first, then match it. For prose, open the piece and copy its digits. Never reach for a ruling by
keyword — read the ruling before citing it, and if it does not govern, say so and file the one
that does.

*Related:* [[2026-09-21-a-comparator-with-no-locale-asks-the-machine]] (#59, the one this was
mis-cited from), [[2026-09-22-a-date-is-not-a-moment]] (#60), [[2026-09-23-a-date-that-matches-is-not-a-date-that-agrees]] (#62 — the annotation and the sentence printing the same digits and meaning different things; here they print different digits and mean the same thing, which is the mirror).
