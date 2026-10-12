# Arabic gate — the Edition 05 wave packet's six captions

**Date:** 2026-10-12 (Asia/Dubai) · **Persona:** Arabic Editor, as verifier (the compose-vs-judge
split, 2026-06-16 / ratified 06-24) · **Artefact:** `social-drafts/2026-08-31-ed05-wave-packet.md`
**Routed:** 2026-09-22 (Egypt, five captions) and widened to six on 2026-09-30 (Rwanda)
**Age at judgment:** **20 days**, and the edition's last open blocker.

**This gate was taken once before, on 2026-10-11, by a run that reached its turn cap and banked
nothing** (ruling #96). The judgment was not recovered from that run's transcript — *a gate verdict
is the Arabic Editor's judgment, not a string the Manager possesses* — so it is made again here,
from the artefacts, and committed in the turn it is finished.

---

## Verdict

**FIVE OF SIX PASS. ROW 4 — the continental ruler — RETURNS, in BOTH languages.**

The defect is not in the Arabic. It is in **both** captions equally, it has stood for **24 days**,
and it is a claim the piece's own body **explicitly forbids in the sentence beside it**.

| # | Piece | AR caption | EN caption (flip-day checklist step 3) |
|---|---|---|---|
| 1 | Zambia | **PASS** | **PASS** |
| 2 | Sierra Leone | **PASS** | **PASS** |
| 3 | Sudan | **PASS** | **PASS** |
| 4 | **Africa — the ruler piece** | **RETURN** | **RETURN** |
| 5 | Egypt | **PASS** | **PASS** |
| 6 | Rwanda | **PASS** | **PASS** |

---

## 1. Named-human transliteration — the gate's core, and it is EMPTY

**No caption names a human.** Enumerated rather than assumed: the six AR captions carry
**zero** personal names. What they do carry is **seven country names and no institutions**
— موريشيوس · السنغال · بنين · النيجر · جنوب أفريقيا · زامبيا · سيراليون · السودان · مصر ·
رواندا — every one of which is in the shipped pieces' own Arabic text and in `COUNTRY_AR`.

This is worth one line rather than none, because the gate's core test is the one test this
artefact cannot fail, and **a test with nothing to check has failed rather than passed** (the
2026-08-16 silent-pass trap). The gate's weight therefore falls entirely on §3 below, which is
where it found something.

**Ruling #86 is likewise vacuous here and is recorded as vacuous:** no caption gives a role noun
to a named human, so the Arabic edition makes **no gender determination the English one does not**.
Zero of zero, against 24 of 43 in the article bodies.

## 2. Figures — gated, and the gate is green but narrow

`qa_packet_figures` (standing assertion 23): **4 packets · 9 entries · 21 captions · 45 figures ·
CLEAN**, 21 of them discriminating at three digits or more. Every numeral in every caption is in
the shipped text of the piece it advertises, in that caption's own language.

**And it is green on the row this gate returns.** The defect below carries **no numeral at all**,
which is exactly what the packet's own 2026-09-23 note says the instrument cannot reach: *"a
hedge, a noun, a tense and a verb are all invisible to it."* Step 3 is still a human re-read. It
found something on its first execution as a gate.

## 3. THE FINDING — row 4's caption names two countries where the piece crowns four, and the piece says so

**The caption, both languages, as staged:**

> …**Senegal and Benin** on learning relative to income…
> …**والسنغال وبنين** على التعلُّم منسوبًا إلى الدخل…

**The piece, ¶8, as shipped today:**

> So ruler two crowns **all four that cleared 410 — Gabon, Senegal, Benin and Burkina Faso** —
> and it does so on an analyst's axis rather than a measurement. The band is where his register
> stops: he places the four above the global median… and never separates the four from one
> another. ***Naming two of them would be our narrowing, not his.***

The distribution copy commits, word for word, **the narrowing the piece's own body names and
refuses** — and it refuses it on #51 grounds, because the analyst's register stops at the band.

**Dated, not estimated.** The widening landed in commit `78d6daa` on **2026-09-18**, four days
after the caption was composed on 09-14. The captions have been wrong for **24 days** and have
passed through the 09-19, 09-22, 09-30, 10-05 and 10-07 readings of this edition.

**Fourth instance of #50 in this one file** — Sudan's captions (09-14), Egypt's EN caption
(09-22), Egypt's AR caption composed late (09-22), and now this. The packet's standing procedure
— *before flip-day, every caption is re-read against the current text of the piece it advertises*
— is correct, was written after the second instance, and had **not been executed since 09-30.**

## 4. THE FINDING UNDER THE FINDING — it is not only the caption, and the rest is the EDITOR'S

The caption was composed from the piece's **dek**, exactly as the packet's procedure requires. So
the obvious question is whether the dek says it too. It does, and so do three other places.

**Grep for it; do not remember it.** The claim *four rulers crown four different countries* has
**seven homes**, and the 09-18 widening moved **one**:

| Home | Reads today | Status |
|---|---|---|
| Body ¶8, EN + AR | *"all four that cleared 410 — Gabon, Senegal, Benin and Burkina Faso"* | **moved 09-18 — the only one that was** |
| Body ¶1, EN | *"four defensible ways to measure it, that they crown **four different countries**"* | **left behind** |
| Body ¶1, AR | «أربعَ طرائقَ وجيهةٍ لقياسه، وأنها تتوّج **أربعةَ بلدانٍ مختلفة**» | **left behind** |
| `dek`, EN | *"four defensible measures answer with **four different countries**"* | **left behind** |
| `dek`, AR | «يُجِبْك أربعةُ مقاييسَ وجيهةٍ **بأربعةِ بلدانٍ مختلفة**» | **left behind** |
| Packet caption, EN + AR | *Senegal and Benin* | **left behind — returned above** |
| `qa_geo_fields.py` header | *"a continental piece whose honest deliverable is four rulers crowning four different countries"* | **left behind**, in a tool that gates the deploy |

**The crowned set is seven countries, not four:** Mauritius (ruler 1); Gabon, Senegal, Benin and
Burkina Faso (ruler 2); Niger, with South Africa on the TIMSS limb (ruler 3); Senegal again
(ruler 4). The piece's **title** — *Four rulers, four crowns* — is **untouched and still exactly
true**: there are four crowns, and the second one is shared. It is the *count of countries* that
stopped being four, and only that.

**And the 2026-10-05 Arabic register judgment quoted ¶1 as `EN (unchanged, and correct)` while
ruling on the clause immediately after it.** It was right that the clause was unchanged. *Unchanged
is not the same as correct*, and the comparison that would have caught it — ¶1 against ¶8, three
paragraphs apart in the same piece — is the internal-consistency family's question (#34) asked of
prose rather than of a table.

**This is routed to the Editor and is NOT taken here.** A caption is the Arabic Editor's and
Growth's; a dek and an opening sentence are the frame of the piece, and *the Editor is the filter,
never the Manager* (CHARTER). The Editor's ruling is filed separately today, because it blocks the
flip and nobody else will answer it.

**The `countries:` array is named and deliberately NOT called a defect.** It reads
`[Mauritius, Senegal, Niger, Benin, South Africa]` in both editions — five names, omitting Gabon
and Burkina Faso, which the piece now crowns. `qa_geo_fields` passes, correctly: it asserts
structure (every name resolves, `country` ∈ `countries`, no duplicates, EN/AR twins identical) and
has never claimed to assert *editorial membership*. Whether a crowned country belongs in a geo
field is a question for the Editor and the Web Developer together, and inventing an answer at an
Arabic captions gate would be exactly the over-reach this gate exists not to commit.

## 5. The five that pass, and what each was checked against

Each caption was re-read against the **current** text of its piece, not against the draft it was
composed from (#50), and each piece **had changed** since its caption was written — all six did.

- **Zambia.** Claims: statutory right, *not* a policy renewed; widened to the boarder's bed; the
  end of primary moved grade 7 → 6; the twenty-year measurement line. All four are in the piece's
  own dek sentence and in §*Accommodation is now inside the fee ban* and §*Which returns to the
  redefinition*. The three body edits since 09-14 are the K4.7m attribution, the learning-poverty
  attribution (*puts* → *reports… an estimate its brief attributes to*) and the election moving to
  past tense with its date — **none is in the caption**, and the hedge that was added to the
  learning-poverty sentence is not a hedge the caption carries, because the caption does not make
  the claim. **PASS.**
- **Sierra Leone.** $18m / 325 schools / Year-3 under target / *paid what the measurement said* /
  one provider chose the ruler that shrank its own number — all present, and the last is a section
  heading with Save the Children named under it as the provider that computed both ways and
  published the smaller. The 10-02 and 10-04 edits moved a **source URL and an attribution** (the
  SCUK repository is a personal account, #84) — the caption attributes nothing to a repository.
  **PASS.**
- **Sudan.** 2014, nine years before its own war, tablet + solar panel + educational games +
  trained adult from the village, scaled into other countries' emergencies, came home under other
  names. The 10-03 read added annotations and corrected one institution's name — *National Council
  for Literacy* → *…and Adult Education* — **which the caption does not name**. The 09-10
  verification's struck claim (*games that teach Arabic and maths*) is still absent from both
  captions, where the 09-14 repair put it. **PASS.**
- **Egypt.** Legislated 2025, optional, free, standing beside Thanaweya Amma; a year before anyone
  sat an exam two ministries published which faculties each track opens; the price is in the
  statute; the admissions arithmetic published with a worked example; the student count not
  published. **One was weighed rather than waved through:** the body bounds itself —
  *"What is not established from this register is any particular faculty's entry for any
  particular track"* — while the caption says the map was published. These are compatible and the
  reasoning is written down so the next reader does not have to re-derive it: the body's bound is
  about **which faculty for which track**, which the caption never names, and *published* is the
  piece's **own headline word** (*The doors were published before the exams existed*), approved at
  the Editor's verdict. The 10-08 read's edits are date-provenance repairs (EIPR 21 July → 7 July;
  *on 3 August* → *in an account published on 3 August*) and the caption carries neither date.
  **PASS.**
- **Rwanda.** The flow-and-stock seam is carried in the caption at the cost of a clause, exactly
  as the 09-30 entry claims: *شهاداتِ البرنامج تدفُّقٌ والإحصاءَ يَعُدُّ مخزونًا*, with 24,000
  never written as a subset of either census figure — the commission's standing prohibition held in
  distribution copy. The only edit since is the news-index enumeration gaining a second date, which
  the caption does not touch. **PASS.**

## 6. Arabic register, orthography and digits

- **Digit set (#64).** All six AR captions use **Western digits** — 325, 2014, 24,000, 27,409,
  27,322, 2025 — matching the prose digits of the Arabic pieces they advertise. A caption exists
  to be checked against its piece by eye, so prose follows the piece. **Correct, and it is a
  property of the register the string sits in, not of the language.**
- **Tashkeel** is partial and functional throughout — on the ambiguous forms only (صفًّا، حقًّا،
  شهَّدت، أُغلقت) — the house practice, not full vocalisation.
- **No Latin hashtags on the Arabic side except where the piece's own Arabic uses them**: rows 1–4
  and 6 carry **no** hashtags in Arabic, row 5 carries `#مصر #سياسات_التعليم #أفريقيا` in Arabic.
  **That inconsistency is noted and not corrected here** — it is Growth's call about a channel, not
  a register question, and five captions carrying none while one carries three is a decision
  somebody should make deliberately before flip-day. Carried to the Growth note, not to the piece.
- **Direction and joining** are not assertable on a markdown file and are not asserted; they are
  gated on the rendered editions by `qa_arabic_shaping`, `qa_arabic_joining` and `qa_feed_direction`.

## 7. What this verdict does NOT clear

- **The EN caption repair is made under this verdict** because the flip-day checklist's step 3 is
  a single re-read of both languages and splitting it would leave one edition carrying a claim the
  other had dropped — which is the one-edition state the packet's own 09-19 note forbids.
- **The flip is NOT cleared by this gate**, and the reason is in §4: an opening sentence and a dek
  in both editions are now known to be stale, the Editor's ruling on them is filed today, and
  **a repair to the spine of a piece is not a tail-end job on the day it is found.** Standing rule
  #1 outranks the gate date, which has already passed.

---

**Arabic Editor · 2026-10-12**
