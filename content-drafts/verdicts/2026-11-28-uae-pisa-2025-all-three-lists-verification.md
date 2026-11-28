# Verifier's verdict: `2026-11-26-uae-pisa-2025-all-three-lists`

**VERDICT: VERIFIED WITH CORRECTIONS REQUIRED — five corrections, all applied in-run. Four of the five
are in both editions; the fifth is in the Arabic annotation alone and was found only because the Arabic
annotation was read as a register in its own right rather than as a translation of the English one.**

Verifier, 2026-11-28. I did not write this piece. I read the brief, both editions, the Editor's five-test
verdict and the Arabic Editor's gate. **Every register was re-fetched into a clean directory rather than
read from the run's copies, and for each of the four registers I fetched a SECOND, independently captured
snapshot** — a different Wayback timestamp — so that each figure and each span is confirmed twice over
bytes that were captured on different days by a crawler that did not know this piece existed. That is
#27's two channels built out of the only axis available when the origin refuses us.

## 0. The doors, re-tested rather than quoted (#159's family)

`www.oecd.org` answers this runner **403** today, re-tested at the top of this verdict. The refusal was not
routed around. The archive answers, and its availability API returns the same closest capture the drafter
used, `20261104162528`.

## 1. All four provenance triples reproduce exactly — which is #161 passing where it failed twice

The piece declares four registers by byte count and sha256 of the decompressed raw snapshot. I re-fetched
each at its declared fourteen-digit timestamp and hashed it:

| Register | Declared bytes | Re-fetched | sha256 |
|---|---|---|---|
| Volume I, Chapter 2 | 2,426,000 | **2,426,000** | `e5a429b0…f068a71` **match** |
| Volume I full-report page | 1,614,913 | **1,614,913** | `1c3018b4…87264a1b` **match** |
| Press release, 8 Sep 2026 | 1,468,371 | **1,468,371** | `096bb651…bb671166a5` **match** |
| Cormann launch speech | 1,464,823 | **1,464,823** | `33b350b2…2e323a9` **match** |

Four for four, byte count and hash. **This is the ruling that cost the Qatar piece its most expensive
repair** — R2's triple did not reproduce there, and the same bad triple had already shipped in Thailand.
Here the triples were written correctly the first time. I note also that the gzip member's own header
declares an uncompressed length of 2,426,000, so the declared figure is checkable from the transfer itself
without trusting the decompressor.

**The second channel.** Independent captures fetched and used throughout: Chapter 2 at `20260910092914`
(2,422,806 bytes), the full-report page at `20260910151315` (1,611,271), the press release at
`20260908134936` (1,472,216), the speech at `20260913174024` (1,460,924). All four differ from the
drafter's captures in total bytes — they are genuinely different documents of the same register, 55 to 68
days apart — and **not one load-bearing figure or span differs between the two captures of any register.**

## 2. Twenty-three quoted spans, each confirmed in TWO captures of its own register

I extracted every quoted span from the English body by pattern rather than by eye and required each to be
present in the normalised served text of both captures of the register it is attributed to. Normalisation
is declared: NFC, curly quotes folded to straight, the three dashes and the minus sign folded to hyphen,
`Türkiye`/`Turkiye` folded, whitespace collapsed. **Terminal punctuation is NOT normalised**, which is
#159's second cause and the defect the Arabic gate caught on the Qatar piece an hour after Test 1 missed it.

**23 of 23 verbatim in both captures of their register. 0 in one capture only. 0 not found.** By register:
13 to Chapter 2, 2 to the press release, 1 to the full-report page, 2 to the speech, and the five table and
column titles to Chapter 2.

The attribution of each span to a register was checked rather than assumed: run against all eight extracts
at once, each span is present in exactly the register the piece names and absent from the other three. The
`Slovakia` / `the Slovak Republic` split survives this test in the right direction — `Slovakia` is in the
speech and in neither the chapter nor the press release, which is the observation the piece is built to
preserve, and it is preserved in both editions.

## 3. Every figure re-derived from the tables, not read from prose

I parsed the HTML tables themselves — cell by cell, resolving the three-panel layout — rather than matching
digits in running text.

- **Table I.2.6.** UAE **26 | 15 | 21**, in the table's own column order science, reading, mathematics
  (column order read off the parsed header, not assumed). OECD average-35 **−3 | −14 | −9**. Both captures.
- **The twelve.** The piece's own count of rows positive in all three columns reproduces exactly: **12**,
  from 75 parsed entries, in **both** captures — Georgia, Cambodia, Jordan, Montenegro, the United Arab
  Emirates, Saudi Arabia, Thailand, Türkiye, the Philippines, Costa Rica, the Slovak Republic, El Salvador.
  The UAE is among them. The piece attributes twelve to itself and eight to the chapter and leaves the gap
  open with the colour reason; that is correct and it is the right handling of an unattributable count.
- **Table I.2.8.** UAE **−10.0** and **1.7**; OECD average-35 **1.2** and **−0.3**. Unit percentage points,
  which the piece states and fences against score points.
- **Table I.2.9.** UAE **18 | −6 | 20**; OECD average-35 **−7 | −27 | −24**. The decade's five on the
  reading column: Montenegro **−13**, Qatar **18**, the Slovak Republic **−8**, Türkiye **34**, the UAE
  **−6**. All five re-read from the parsed table.
- **The classification of those five, re-derived.** Türkiye 62/34/35 and Qatar 19/18/12 are positive in all
  three; Montenegro 16/−13/−14 and the Slovak Republic 12/−8/−13 are negative in two of three; the UAE
  18/−6/20 is positive in two and negative in exactly one. **So "two", "two" and "the only one" are all
  three correct**, and the uniqueness claim the piece makes here is the one uniqueness claim in it that
  holds (see correction 2). −6 is also the smallest of the three negatives, as the piece says.
- **Table I.2.1.** UAE science mean **458**, and its not-statistically-different column holds exactly one
  system, **Viet Nam**, whose own mean is **457**. The band of one is real.
- **Table I.2.3.** First column is the overall science mean: UAE **458**, OECD average **482**.
- **Jordan and Uzbekistan are absent from Table I.2.9** — 0 occurrences, both captures — and present in
  I.2.8, which is exactly the asymmetry the piece uses. The register's own note gives the reason and the
  piece quotes it. This is the piece's best paragraph and it checks out completely.
- **The three riser lists, intersected from scratch.** Press release decade-science list: 11 names. Decade
  both-ends list: 5. Front-page "bucking the trend": 16 (4 OECD + 12 non-OECD, both halves read in served
  text). The intersection of all three is **exactly four — Montenegro, the Slovak Republic, Türkiye and the
  UAE** — as the piece names them. Qatar drops out because it is not on the front page's list, which I
  confirmed rather than inferred.

## 4. The eight axes and the eight rows

**Administration / coverage (1):** one instrument, one administrator, named. **Funnel stage (2):** not
engaged; no pipeline. **Vintage (3):** every figure is the OECD's own as adopted in its own report; the one
derived count is attributed to this publication in the sentence that prints it. **Scope (4):** the
`OECD average-35` label carries its own country count and the piece reproduces the label rather than
writing "the OECD average" — but see corrections 2, 3 and 4, which are all this axis. **Direction (5):**
"at least three assessments" is a correct derivation from the register's "at least two previous
assessments", and the hedge travels with it. **Position (6):** the decennial trend carries its definition
and its subtitle in the sentence that uses it. **Condition (7):** percentage points are labelled as such
and fenced off from score points in the paragraph that prints both; no rate is chained. **Type / noun (8):**
the strongest thing in the piece — change and level are kept apart by a section break and an explicit
sentence, and the refusal to set 18 against 26 is stated before the pair appears.

**Register (A):** four voices, kept distinct, with the one disagreement between them preserved rather than
normalised. **Quotation (B):** §2. **Clock (C):** no forward-looking date; 8 September 2026 is past, and the
title "OECD Secretary-General Mathias Cormann" is printed by captures of 14 and 15 November 2026, thirteen
days before today. **Description-date (D):** the speech is cited as prepared text carrying "Check against
delivery", not as a transcript. **Seam (E):** the piece's whole architecture is a refusal to cross two
seams, both declared. **Re-read scope (F):** I re-opened all four registers and re-settled everything the
piece takes from each, not only the items in dispute. **Date referent (G):** capture timestamps are
distinguished from event dates throughout, to the second. **Forced determination (H):** correction 1.

## 5. Structure

Dek **193** code points of 200, EN; **171**, AR. Titles 37 and 40. Bodies 1,806 and 1,422 words. All four
`related:` slugs resolve in **both** collections and all four are `approved: true`. Hero still on disk,
2,653 bytes. OG card on disk, a valid PNG at 1200×600, consistent with its three siblings. Flag state
checked on disk in both editions: `approved: false` in both at the time of this verdict, no stale
`approved: true` in any staging copy (#18) — the content-drafts hits are prose in ledgers, not frontmatter,
and nothing in `content-drafts/` is in the build path.

## 6. The five corrections

### Correction 1 — the Arabic edition makes a forced determination that no register licenses, and the annotation says it makes none. (Row H, #86 clause 1 as amended by #134.)

The fourth source note — the Cormann speech — ends: *"No register read for this piece carries a pronoun or a gendered title for
Cormann, so no gendered construction attaches to the name in either edition."*

**The premise is true and I verified it.** Across both captures of the speech and both of the press release:
`he` 0, `his` 0, `him` 0, `Mr` 0, `Mr.` 0. The title the registers print is `OECD Secretary-General`, which
is ungendered in English. #134's widening does not reach it either — `Mathias Cormann` carries no name
morpheme of the kind #134 made admissible, no `بن`, no `بنت`, no honorific, no feminine nisba. There is no
licence anywhere in the four registers.

**The conclusion is false for the Arabic edition.** The Arabic body writes
**«ماتياس كورمان، الأمين العامّ للمنظمة»**. `الأمين العامّ` is the masculine form; the feminine
`الأمينة العامة` exists and is used. Arabic cannot print this role noun without choosing, so the Arabic
edition **has** made the determination — and the annotation in both editions states that neither edition
did.

**And the Arabic form of the note refutes itself twice inside the sentence that makes the claim.** It read:
«ولا يحمل أيٌّ من السجلّات المقروءة هنا ضميرًا ولا لقبًا دالًّا على **جنسه**، فلا تُسنَد **إليه** صيغةٌ دالّةٌ
على جنسٍ في أيٍّ من الطبعتين» — `جنسه` is *his* gender and `إليه` is *to him*, both masculine, in the very
clause denying that either edition attaches a gendered construction. Arabic could not write the denial
without performing the thing denied. That is the sharpest available demonstration that the claim was a claim
about English wearing the clothes of a claim about the piece, and it is why the English note's wording could
survive its own author: in English the sentence is self-consistent, and in Arabic it is not expressible.

This is #86's own named failure mode, the "5 standing on nothing" of its measurement, reached through a new
door: not a composer asserting a gender they guessed, but a composer correctly finding no licence, correctly
reporting that there is none, and then writing the sentence as though the Arabic had the option of silence.
**English's freedom to decline was read as a property of the piece rather than of English.** #86 anticipates
exactly this and prescribes the remedy in its own words: *where no register carries it, the construction
cannot be declined, so the determination is recorded in the annotation as this edition's own.*

**Repair, applied:** the fifth source note in **both** editions now records that the Arabic edition is
forced into `الأمين العامّ`, that no register read for this piece licenses it, and that the determination is
therefore this publication's own and not the OECD's. The English edition continues to decline, and the note
now says that its silence is not confirmation. Carried in both annotations, per #134's binding.

### Correction 2 — the central finding reads as unique to the UAE, and three systems hold it.

*"Seven systems over three years, five over the decade, and the UAE is in both. That is the finding this
piece exists for… Being on two lists is ordinary; being on the same list on two different clocks is not."*

Intersecting the two lists: **Montenegro, Türkiye and the UAE are all three on both.** The piece names
Qatar as on the decade's five and off the three years' seven, and Saudi Arabia the other way, so a reader
is shown two systems that fail the test and one that passes it, and takes away that passing is rare in a
way the register does not support. Nothing in the piece is false here — it never writes "only" — but the
rhetorical weight of "that is the finding this piece exists for" does the work "only" would have done.

**Repair, applied:** the paragraph now names Montenegro and Türkiye as also on both, in both editions. This
costs the piece nothing and buys it something: three of seven surviving the clock change, against five of
five on the decade list, is a sharper reading of the clocks' disagreement than the UAE alone was.

### Correction 3 — "the only number in this chapter" outruns its own qualifiers.

*"It is also the only number in this chapter, on either clock, at either end of the distribution, that does
not go the UAE's way."*

The qualifiers name the two clocks and the two ends, and within those four measures the claim is exactly
right. But the head is "the only number in this chapter", and the chapter also prints the UAE's science
mean of **458** against an OECD average of **482** — a number in the chapter that does not go the UAE's way.
The piece knows this; it prints both figures two sections later under a heading calling it a different
question. The head of the sentence is simply wider than the sentence.

**Repair, applied:** "the only number" becomes "the only **change**" in both editions, which makes the head
agree with the qualifiers and with the piece's own later section break.

### Correction 4 — "every list a system can be on" is contradicted inside the same chapter.

*"Read in the release's own performance chapter, the UAE is on every list a system can be on."*

Chapter 2's own "What the data tell us" opens: **"B-S-J-Z (China) and Singapore were the two
highest-performing systems across science, mathematics and reading in PISA 2025."** That is a list in this
chapter, and the UAE is not on it — necessarily, at 458 against 482.

**The piece's own dek already has the right scope** — *"named on every improver list the PISA 2025 release
prints"* — so this is a body sentence that lost a word its own dek kept.

**Repair, applied:** "every list a system can be on" becomes "every improver list a system can be on", both
editions.

### Correction 5 — the Arabic annotation prints one entry of a five-entry list in the wrong unit, and under the wrong register's name for the country. (Axis 8, and the Arabic gate's own correction class.)

This one is in the Arabic edition only, and it is the reason an annotation has to be read rather than
diffed. The Arabic Chapter 2 note gave the decennial **reading** trends of the decade's both-ends five as:

> «ومن صفوفه خطوطُ القراءة العَقديّة للخمسة: الجبل الأسود −13، وقطر 18، **وسلوفاكيا 12 و−8 و−13**، وتركيا 34، والإمارات −6.»

**Two defects in one clause, and neither figure in it is false.** The Slovak Republic's row in Table I.2.9
is 12 | −8 | −13 and I confirmed all three; what is wrong is that this is a list of five *reading* figures
in which four entries carry one number and the fifth carries a whole row. A reader counting the list finds
seven numbers where there should be five, and the only entry that states a science and a mathematics trend
is the one the sentence is not about. That is axis 8 inside an annotation: the same digits under a different
noun. The English note is correct — *"the Slovak Republic -8"* — so this never existed as a composition
decision, only as an Arabic-side slip no body check could reach.

**And it is named `سلوفاكيا` — *Slovakia*.** This clause's register is the **chapter**, and the chapter
prints *the Slovak Republic*; `Slovakia` is the **speech's** word, and keeping the two apart is the single
observation this piece is built to preserve. The Arabic Editor's gate on 2026-11-27 caught exactly this
class in the **body** — two instances, recorded as two of its five corrections, and praised in the ledger as
the first time a cell-3 warning caught something at cell 5 — and the ledger's own note explains why it
stopped there: *a finding that two registers name one country differently is destroyed by a composition that
is internally consistent.* The gate swept the prose and the quoted spans. **The annotation is prose too, and
it is served, and it was not swept.** `qa_annotation_figures` exists because an annotation figure is outside
every body instrument this operation owns; this is the same gap with a proper noun in it instead of a number.

**Repair, applied:** the clause now reads «والجمهوريةُ السلوفاكية −8» — the chapter's own name for the
system, and the reading figure alone, matching the other four entries and the English note.

## 7. What I did not change

**The twelve-against-eight gap stays open.** I could not close it either: the assignment of a cell to
"Positive change", "Non-significant change" or "Negative change" is carried by cell colour, and I confirmed
by parsing that the served markup carries the three legend labels as text while the row cells carry no
significance token of any kind. The piece's refusal to claim significance on this register's authority is
correct and is the only honest position available.

**The "band of one" sentence stays.** I checked the asymmetry: the UAE's row lists only Viet Nam, while Viet
Nam's row lists the United Arab Emirates **and Malta**. The piece's claim is about the UAE's own column and
is true as written; the asymmetry is a property of the OECD's pairwise test, not an error, and saying so
would cost a paragraph to explain a point the piece does not rest on.

**The closing section stays as written.** The five doors are re-tested in the piece itself on 2026-11-27,
one day before this verdict, and the piece states plainly that no first-party UAE register has been read.
I did not re-test them a third time; the piece's claim is dated and scoped to its own read, which is the
correct form, and a 2026-11-28 re-test would have produced a figure the piece does not claim.

## 8. Result

**VERIFIED.** Five corrections required, all five applied in-run and re-checked after application. Every
load-bearing figure confirmed through two independently captured channels of its own register; 23 of 23
quoted spans verbatim in both captures; four of four provenance triples reproducing to the byte and the
hash. The piece may take cell 6 and proceed to the flag.

**Two findings are worth carrying past this piece, and they are the same shape pointed at different
objects.** Correction 5 is the smaller one and it is a method note: the Arabic annotation was checked here by
reading it, and the figure-level comparison I ran against the English annotation afterwards found exactly the
two tokens the reading had found — a spurious `12` and a second `−13` — which means the cheap instrument
would have worked and nobody had ever pointed one at an annotation pair. Four instruments compare a body
against an annotation; none compares an annotation against its twin.

The larger one is correction 1, and it is a ruling rather than a repair: an
annotation that reports *no register licenses this* is reporting on the registers, and an annotation that
reports *so neither edition makes the claim* is reporting on the editions — and the second does not follow
from the first in any pair where one language is forced. The sentence that joins them is the defect, and it
will read as scrupulous every time, because the half of it that is about the registers is always the half
that was actually checked.
