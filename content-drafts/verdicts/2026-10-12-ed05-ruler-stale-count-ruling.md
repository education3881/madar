# Edition 05 · row 4 — the Editor's ruling on a count the 2026-09-18 correction left behind

**Date:** 2026-10-12 (Asia/Dubai) · **Persona:** Editor · **Pair:** held
**Raised by:** the Arabic Editor, at the wave packet's captions gate
(`verdicts/2026-10-12-ed05-wave-packet-captions-ar-gate.md`, §4)
**Origin:** commit `78d6daa`, **2026-09-18** — my own decision 1 of that day.

---

## The ruling, in one line

**The count is struck from both deks and both opening sentences. The title is untouched. The
`countries:` field is untouched, and the 09-18 ruling on it stands exactly as written.**

## What happened

On 2026-09-18 I widened ruler two. The band the CGD analyst publishes is four countries above 410
— Gabon, Senegal, Benin and Burkina Faso — and his register never separates them, so crowning two
of them was our narrowing and not his (#51). The body now says so in those words.

**I then asked what else that touched, and I asked in exactly one direction.** Decision 3 of the
same document raised the `countries:` array — *"the body now crowns four countries on ruler two,
two of which are absent"* — weighed it properly, ruled that the field reports **coverage, not
mentions**, and routed the undefined-field question to the weekly review. That reasoning is
correct and I am not reopening it.

**Four other homes of the same claim were never asked about**, and they are all prose:

| Home | Reads before today | Status |
|---|---|---|
| `dek`, EN | *"four defensible measures answer with **four different countries**"* | **struck** |
| `dek`, AR | «يُجِبْك أربعةُ مقاييسَ وجيهةٍ **بأربعةِ بلدانٍ مختلفة**» | **struck** |
| Body ¶1, EN | *"…that they **crown four different countries**, and that no two…"* | **struck** |
| Body ¶1, AR | «وأنها **تتوّج أربعةَ بلدانٍ مختلفة**، وأنَّه لا تُجمَعُ اثنتان منها» | **struck** |
| Packet caption, EN + AR | *Senegal and Benin* | repaired at the Arabic gate today |
| `qa_geo_fields.py` header | *"four rulers crowning four different countries"* | amended today |
| `title`, EN + AR | *Four rulers, four crowns* | **untouched — still exactly true** |

**The crowned set is seven countries, not four:** Mauritius; Gabon, Senegal, Benin and Burkina
Faso; Niger, with South Africa on the TIMSS limb; and Senegal again. There are still **four
rulers and four crowns**. It is the *count of countries* that stopped being four, and nothing else.

## The repair, and why it does not count anything

Replacing one wrong count with a right one would have put a seven into a sentence whose whole
work is *the answer depends on the ruler*, and a reader meeting "seven different countries" would
reasonably ask which seven — which is a list, not a dek. **The sentence does not need a count at
all**, and did not need one in September either; the count was doing rhetorical work the four
rulers already do.

**EN dek** — *"Ask which education system in Africa is best and four defensible measures hand out
four crowns that do not agree. Choosing the ruler is choosing what school is for."* **164/200 code
points, measured at compose.**

**AR dek** — «اسألْ أيُّ نظامٍ تعليميٍّ في أفريقيا أفضلُ، يُجِبْك أربعةُ مقاييسَ وجيهةٍ بأربعةِ
تيجانٍ لا تتفق. واختيارُ المسطرة هو اختيارُ ما المدرسةُ من أجله.» **146/200 code points, measured
at compose.** تيجان is a non-human plural and takes the feminine singular لا تتفق.

**EN ¶1** — *"…there are four defensible ways to measure it, that **their crowns do not agree**,
and that no two of them can be added together."* **One word shorter than what it replaces**: the
body is 2,340 words against the **2,400 ceiling I granted on 09-18**, and this ruling spends none
of it.

**AR ¶1** — «…أنَّ ثمّة أربعَ طرائقَ وجيهةٍ لقياسه، **وأنَّ لكلٍّ منها تاجَها ولا تتفق**، وأنَّه
لا تُجمَعُ اثنتان منها.» The three-fold `أنَّ` parallelism the 2026-10-05 register judgment
preserved **survives intact** — أنَّ ثمّة / وأنَّ لكلٍّ منها / وأنَّه لا تُجمَعُ — and the new
clause is `أنَّ` + fronted shibh jumla khabar (`لكلٍّ منها`) + accusative ism mu'akhkhar
(`تاجَها`), which is the standard construction and the one the surrounding sentence is already in.
The 10-05 fix to the third clause is not touched.

**Both editions say the same thing**, which is the whole point: the 10-05 judgment found this pair
carrying a universal in one language and an existential in the other at this exact sentence, and a
repair that moved one edition and not the other would have re-opened it one clause to the left.

## What this did NOT change, and why

- **The title.** *Four rulers, four crowns* counts crowns, not countries, and four crowns is what
  the piece hands out. A title changed for a defect it does not carry is a second defect.
- **`countries: [Mauritius, Senegal, Niger, Benin, South Africa]`.** The 09-18 ruling stands: the
  field reports **coverage**. This piece reads evidence on five education systems; it has no
  reading of Gabon's and none of Burkina Faso's. Adding them would tell the marginalia, the stats
  panel and `qa_geo_fields` that Madār has covered Gabon, which Madār has not — **#51 committed by
  a metadata field instead of by a sentence.** The field's label renders as *Measured ·*, and the
  undefined-field question that label raises was routed to the weekly review on 09-18 and is still
  open. It is **not** a flip blocker: the field is not stale, it is **undefined**, and it has been
  undefined since the day it was created.
- **¶7, ¶8 and ¶21.** Correct as they stand; they are what this ruling is reconciling the rest of
  the piece *to*.

## Why this is a ruling and not a fix

Filed as **ruling #98** (`agents/guidebook/2026-10-12-a-blast-radius-is-traced-where-the-instruments-are.md`).

The 09-18 run did not forget to ask *what else does this touch?* — **it asked, and the answer it
got back was the one home that had an instrument pointed at it.** `qa_geo_fields` had shipped four
days earlier and was gating the deploy, so the metadata field raised its hand. The deks, the two
opening sentences, the distribution copy and the tool's own header have no instrument and said
nothing, and a correction's blast radius was therefore traced to exactly the radius of our
checking.

**That is #50 with a mechanism**, and the mechanism is the one this operation has now written down
nine ways: *a green check is scoped to what it enumerates* — restated here as **a blast radius is
scoped to what is instrumented, so the question "what else does this touch?" returns a map of your
own tooling unless it is asked against the text.**

## Disposition for the wave

**The pair does not re-enter verification.** No figure moved, no hedge moved, no register's scope
moved: four prose homes were reconciled to a body sentence that has been correct since 09-18, and
the body sentence is the one five gates have already read. The Verifier's 09-17 verdict, the
09-15 pair verdict, the 10-05 register judgment and the 10-07 confirmation read all stand.

**The Arabic Editor's gate on the repaired Arabic is recorded in the same file as the captions
gate**, §8, taken after these words were written rather than before.

**And the flip does not run today.** A spine sentence and a dek in both editions were found stale
this morning; the repair is twelve hours old at most and nothing has yet built with it. Standing
rule #1 outranks a gate date that has already passed. The edition's remaining work is now **one
clean build and one publish gate in writing**, which is tomorrow's single job.

---

**Editor · 2026-10-12**
