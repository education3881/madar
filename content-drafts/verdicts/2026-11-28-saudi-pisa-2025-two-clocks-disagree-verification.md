# Verifier's verdict: `2026-11-27-saudi-pisa-2025-two-clocks-disagree`

**VERDICT: VERIFIED WITH CORRECTIONS REQUIRED — two corrections, both applied in-run.**

Verifier, 2026-11-28. I did not write this piece. I read the brief, both editions, the Editor's five-test
verdict and the Arabic Editor's gate. Both OECD registers were re-fetched into a clean directory and
**each was read in two independently captured snapshots** — the drafter's declared capture and a second one
taken 55 and 65 days earlier by a crawler that did not know this piece existed. Every figure and every span
below is confirmed in both.

## 1. Provenance, and the hash this piece puts its weight on

The piece declares two OECD registers and says of the first that it was *"fetched and hashed TWICE in this
run… which is the third independent reproduction of this hash."* **It is now the fourth.** Re-fetched at
this gate:

| Register | Declared | Re-fetched | sha256 |
|---|---|---|---|
| Volume I, Chapter 2 | 2,426,000 | **2,426,000** | `e5a429b0…f068a71` **match** |
| Volume I full-report page | 1,614,913 | **1,614,913** | `1c3018b4…87264a1b` **match** |

The piece also claims the full-report hash *"is the same hash the Qatar piece's source row was corrected to
on 2026-11-27, so that correction is confirmed rather than asserted."* **Independently confirmed here**: the
same triple reproduced for the UAE piece an hour ago and again for this one, so ruling #161's repair to the
Qatar row now stands on three separate re-fetches rather than on the run that made it.

`www.oecd.org` answers this runner **403**, re-tested at this gate. The second channel is therefore a second
capture rather than a second origin, and that is stated rather than glossed: Chapter 2 at `20260910092914`
(2,422,806 bytes) and the full-report page at `20260910151315` (1,611,271). **No load-bearing figure or span
differs between the two captures of either register.**

## 2. Twenty-six quoted spans, each in two captures of its own register

Extracted by pattern, not by eye; normalisation declared (NFC, quotes folded, the three dashes and the
minus sign folded, `Türkiye`/`Turkiye` folded, whitespace collapsed) and **terminal punctuation NOT
normalised**, which is #159's second cause.

**26 of 26 verbatim in both captures of their register. 0 in one capture only. 0 not found.**
*(Re-run after the corrections: **27 of 27** English and **30 of 30** Arabic Latin-bearing, the extra span in
each being the Table I.2.4 title correction 2 introduced, both verbatim in both captures. The count moved
because the piece gained a quotation, not because one changed — which is the distinction a bare `N of N`
cannot make and #159 asks for.)* This
reproduces the hand-off's own count of 26 of 26 exactly — the first time in this edition that a declared
span count has survived an independent re-run without moving (#159 was earned by a count that did not).
Twenty-two resolve to Chapter 2 and four to the full-report page, each present in the register the piece
names and absent from the others.

## 3. The figures, re-derived from the parsed tables in both captures

- **Table I.2.6.** Saudi Arabia **23 | 5 | 1**, science then reading then mathematics in the table's own
  column order. OECD average-35 **−3 | −14 | −9**.
- **Table I.2.9.** Saudi Arabia **37 | −18 | 25**. OECD average-35 **−7 | −27 | −24**.
- **So the piece's spine holds: reading is +5 on one table and −18 on the other**, both the OECD's, both in
  Chapter 2, both about Saudi Arabia. And the claim that the other two subjects agree in sign holds too —
  science +23 and +37, mathematics +1 and +25.
- **Table I.2.8.** Saudi Arabia **−13.0** and **0.4**; OECD average-35 **1.2** and **−0.3**. Percentage
  points, labelled as such and fenced off from score points in the paragraph that prints both.
- **Table I.2.3.** Saudi Arabia's overall science mean **413**, OECD average **482**.
- **The twelve.** Re-counted from the parsed rows of Table I.2.6 in both captures: **12** systems positive in
  all three columns out of 75 parsed entries, Saudi Arabia among them. Attributed to this publication and set
  beside the chapter's own "eight", with the colour reason given. Correct, and correctly attributed.
- **Table I.2.7.** The piece says a yearly learning gain for **ten named systems**, Saudi Arabia not among
  them. Re-counted: exactly **ten** system rows — Austria, Brunei Darussalam, Cambodia, Ireland, the
  Netherlands, Serbia, England, Northern Ireland, Scotland, the United States — and **Saudi Arabia is not
  one**. Reading is one of its three columns, as the piece says.
- **Table I.2.5.** A within-country correlation across domains, with Reading as a row and a column. A
  coefficient, not a level, as the piece says.
- **"between 2015 and 2025" occurs five times on the front page** — counted, **5** in both captures.
- **The front-page signature** is `Mathias Cormann, OECD Secretary-General`, present in both captures.
- **The cited own-site URL resolves.** Source 3 is this publication's Qatar piece; it answers **200** live,
  so the rail the argument leans on is served and not merely written.

## 4. The table census, which is the piece's own load-bearing count — and it is RIGHT

The piece asserts twice that Chapter 2 carries **fourteen numbered tables** and that not one prints a
reading mean. **I set out to fail this and could not.** A text sweep for `Table I.2.N` returns thirteen,
I.2.1 to I.2.13, in both captures — so the first reading contradicted the piece. Parsing the chapter's own
`figcaption` headings instead returns **fourteen**: the fourteenth is **Table I.2.14, "PISA 2025 figures and
tables in Chapter 2"**, an index, which is cross-referenced nowhere in the body text the sweep could see.
*A count read off cross-references is a count of mentions; a count read off captions is a count of tables,
and the piece counted tables.* Fourteen stands.

And the reading claim survives the full census: **no table in this chapter prints a reading mean for any
system.** Levels appear in I.2.1 (science), I.2.3 (science overall and subscales) and I.2.4 — see correction
2. Reading appears in I.2.5, I.2.6, I.2.7 and I.2.9, and in none of them as a level.

## 5. The eight axes and the eight rows

**Administration / coverage (1):** one instrument, one administrator, named; the piece carries Table I.2.6's
own comparability note and Table I.2.9's "at least three PISA assessments" condition in the sentences that
use them. **Funnel stage (2):** not engaged. **Vintage (3):** every figure the OECD's own as adopted; the
one derived count attributed to this publication where it is printed. **Scope (4):** correction 2 is this
axis. **Direction (5):** the hedges travel — "broadly stable", "masks a sustained, long-term decline",
"more than 10 percentage points" are all quoted with their own grammar rather than firmed up.
**Position (6):** both change measures carry their table, their span and their definition at the point of
use; the piece gives **no row distances and no row positions**, which it declares, because I.2.6 is three
panels side by side — the repair the Qatar piece earned, applied here before it could bite.
**Condition (7):** "48 out of 74" and "(61), 7, 7" are quoted with their denominators; percentage points are
never chained to score points. **Type / noun (8):** the whole piece is this axis done well — a change is
never set against a differently-fitted change, +5 is never subtracted from −18, and the refusal is stated
before the pair appears.

**Register (A):** two OECD voices plus this publication's own piece, kept distinct. **Quotation (B):** §2.
**Clock (C):** no forward-looking date; "that will be a different piece" is not a dated promise.
**Description-date (D):** the undated-list problem is the piece's own subject and it handles it by stating
that the defence is subject-specific — *"Had the same undated sentence been written about reading it would
have been unreadable"* — which is the strongest sentence in the piece. **Seam (E):** two instruments, two
tables, declared. **Re-read scope (F):** I re-settled everything both registers give this piece, not only
the items in dispute, which is how correction 2 surfaced. **Date referent (G):** capture timestamps
distinguished from event dates to the second. **Forced determination (H):** correction 1.

## 6. Structure

Dek **195**/200 EN, **167**/200 AR. Titles 49 and 53. Bodies 1,784 and 1,475 words. All four `related:`
slugs resolve in both collections and all four are `approved: true`. Hero still 3,405 bytes, OG card 1,598
bytes, both on disk. Flags `approved: false` in both editions at the time of this verdict; no stale
`approved: true` anywhere in a staging copy (#18).

## 7. The two corrections

### Correction 1 — the same forced determination as the UAE piece, stated more strongly here. (Row H, #86 clause 1 as amended by #134.)

The second source note ends: *"No register read for this piece carries a pronoun or a gendered title for
Cormann, so no gendered construction attaches to the name in either edition."* The Arabic form goes further
and says it in so many words: **«فلا تُسنَد إليه في هذه المادة صيغةٌ دالّةٌ على جنسٍ، في العربية ولا في
الإنجليزية»** — *no gender-bearing form is attached to him in this piece, neither in Arabic nor in English.*

**The premise is true and I verified it on this piece's own registers.** Across both captures of Chapter 2
and both of the front page: `he` 0, `his` 0, `him` 0, `Mr` 0, `Mr.` 0, `Mrs` 0; the apparent `Ms` hits are
substrings of *systems* and *forms*. The title both registers print is `OECD Secretary-General`, ungendered
in English, and `Mathias Cormann` carries no name morpheme of the kind #134 made admissible. There is no
licence.

**The conclusion is false for the Arabic edition, and the Arabic clause refutes itself twice while making
it** — `جنسه` is *his* gender and `إليه` is *to him*, both masculine. Two paragraphs away the Arabic body
writes **«ماتياس كورمان، الأمين العامّ للمنظمة»**: `الأمين العامّ` is masculine, the feminine
`الأمينة العامة` exists and is used, and Arabic has no neutral form, so the Arabic edition **has** made the
determination.

**This is the second instance of one class inside one morning**, found on the UAE piece an hour ago and
present here in a sharper form. Both pieces were composed from the same register set by the same reasoning,
which is exactly why a correction sent to one instance does not reach the other: *the English sentence is
self-consistent and the Arabic one is not expressible, so the defect is invisible in the edition where the
note is drafted and inescapable in the edition where it is composed.* #86 prescribes the remedy and both
pieces now carry it.

**Repair, applied:** the second source note in **both** editions records that the Arabic edition is forced
into `الأمين العامّ`, that no register read for this piece licenses it, and that the determination is this
publication's own. The English edition continues to decline and the note says its silence is not
confirmation. Carried in both annotations, per #134's binding.

**And it is handed on rather than only fixed.** Two pieces in one morning is a class, not a coincidence: any
Ed06 piece that names Cormann is a candidate, and the two already shipped with this annotation shape —
`2026-11-26-qatar-pisa-2025-two-of-three` and `2026-11-26-pisa-2025-three-lists-of-risers` — must be read
for it. Raised for the standing queue rather than swept inside this verdict, because a pattern first
attempted inside one piece's gate is a pattern nobody proved (the item-166 precedent).

### Correction 2 — "Every table that reports a level reports science" is false, and the table that falsifies it makes the piece's point better. (Axis 4.)

The sentence introducing the register's asymmetry reads: *"Every table that reports a level reports
science: Table I.2.1 ranks systems by their science mean, [Table I.2.3] gives Saudi Arabia's overall science
mean as 413 against an OECD average of 482, and the rest count low and top performers in science, science by
socio-economic quarter, science by gender."*

**Table I.2.4 is "Comparing countries' and economies' performance in computational problem solving", its
first column is a mean score, and Saudi Arabia's is 426** — confirmed in both captures. That is a table
reporting a level, and the level is not science. The universal is wrong.

Nothing else in the piece depends on it: the reading claim is about *reading*, and no table prints a reading
mean. But the corrected form is a better fact than the wrong one. The chapter prints a level for **science
and for computational problem solving — the two domains PISA 2025 assessed as its focus and its innovative
domain — and for neither reading nor mathematics.** So the absence the piece is built on is not a quirk
aimed at reading; it is a property of the cycle, and **reading is the one of the two level-less subjects
whose two change figures disagree in sign**, mathematics being +1 and +25. That is the piece's own argument
with its real boundary drawn.

**Repair, applied:** the sentence now states that the chapter reports levels for science and for
computational problem solving and for neither of the other two core subjects, names Saudi Arabia's
computational problem solving mean of 426 with its table, and says that reading is the level-less subject
where the sign changes. Both editions. **And because the body now names a table the annotation did not, a
Table I.2.4 clause was added to both annotations in the same edit** — 426 re-read in both captures — since a
figure is cited as read and the register clause behind it has to be nameable. The annotation's parallel
clause — *"This chapter carries fourteen
numbered tables and not one prints a reading mean for any system"* — is **correct as written** and is not
touched.

## 8. What I did not change

**"Reading is in four of the fourteen."** Strictly, Table I.2.14 is an index of the chapter's figures and
tables and its rows carry the titles of I.2.6 and I.2.9, so the string *reading* occurs in it seven times.
The sentence's own enumeration names the four and says *never as a level*, and an index reports no quantity
about any system, so the claim is about where reading is reported and is true. Changing it would trade a
true sentence for a longer one.

**The eight-or-twelve section stays open**, and I could not close it either: the significance assignment is
carried by cell colour and the served markup carries the three legend labels as text with no significance
token on any row. The piece's refusal to place Saudi Arabia inside or outside the eight is the only honest
position available.

**The closing section stays as written.** The two Saudi doors are measured in the piece itself on
2026-11-27, one day before this verdict, and the measurements are dated and scoped to that read. I did not
re-test them: the piece claims a dated observation, not a current state, and a 2026-11-28 re-test would
produce a figure the piece does not claim.

## 9. Result

**VERIFIED.** Two corrections required, both applied in-run and re-checked after application. Every
load-bearing figure confirmed in two independent captures of its own register; 27 of 27 quoted spans
verbatim in both after the repairs, 26 of 26 before them; both provenance triples reproducing to the byte and the hash, one of them for the fourth
time. The piece may take cell 6 and proceed to the flag.
