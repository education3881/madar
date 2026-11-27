# Verifier's verdict: `2026-11-27-thailand-pisa-2025-fourth-list`

**VERDICT: VERIFIED WITH CORRECTIONS REQUIRED — three corrections, all applied in-run.**

Verifier, 2026-11-27. I did not write this piece. I read the brief, both editions, the Editor's five-test
verdict and the Arabic Editor's gate. **I re-fetched every register myself into a clean directory rather
than reading the run's copies**, and I re-derived the nine-round table from the spreadsheet's own XML
instead of from either edition's table.

## 1. Staleness control on a register nobody has snapshotted

The Thai notice is live and un-archived, so the only control available is a second read. I re-fetched
`pisathailand.ipst.ac.th/news-23/` nineteen minutes after the compose-time read and compared two ways:
`cmp` reports **byte-identical**, and sha256 agrees —
`8edbc1b1783c3e3bd37df65b9f9c93fdeb08d9c6f2995cdb8ad4e9657ba6ff90` on both reads, **185,102 bytes**. The
spreadsheet re-downloaded to the same hash, `2c46edde2ac56f37…`, 73,730 bytes. The three OECD snapshots
re-fetched to the three hashes the recon banked on 2026-11-26, at 1,468,371, 1,614,913 and 1,464,823 bytes.

## 2. The nine rows, re-derived rather than re-read

I parsed `xl/worksheets/sheet1.xml` from the re-downloaded workbook and resolved the merged header blocks
independently: the nine cycle blocks run 2025, 2022, 2018, 2015, 2012, 2009, 2006, 2003, 2000, and within
each block the order is reading, mathematics, science. **The row is self-identifying** — its label cell
reads «คะแนนเฉลี่ยของประเทศไทย», Thailand's average scores — so the national row is named by the register
and not inferred by position, which is the one thing I wanted to establish before trusting any pre-2022
figure.

Twenty-seven values, and all twenty-seven match both editions' tables digit for digit. Two independent
checks on the mapping held: the 2022 triple (379, 394, 409) reproduces Thailand's published PISA 2022
averages, and the 2025 triple (392, 407, 432) reproduces the three figures the notice states in prose.

**The two rank claims re-counted from scratch.** Science 432 is **third** of the nine, behind 2012's 444
and 2000's 436. Mathematics 407 is **second-lowest**, above only 2022's 394. Reading 392 is
**second-lowest**, above only 2022's 379 — and 2018's 393 sits one point above it, which the piece does
not need to say but which is why this count had to be run rather than eyeballed. The Editor's note 2
reports catching *second-highest* in the draft; independently re-counted, the published word **third** is
right.

## 3. Twenty-nine figure claims, checked against the re-fetched register

I built one needle per claim out of the register's own Thai, including its own spacing, and required each
to be present in the re-fetched served text: the sample and its month, the global totals, the four OECD
averages, the eight-name list and its significance condition, Thailand's four averages, the three science
sub-competency averages, the three rises, the trend sentence, the percentile gap, the socio-economic gap
and its OECD counterpart, the resilient-student shares, all five proficiency-share claims, the
computational-problem-solving shares, the school-group findings and the 2027 promise. **Twenty-nine of
twenty-nine present. Zero figures wrong in either edition.**

Quoted spans. English: six, of which four are verbatim in the OECD snapshots (List A in Volume I; *Check
against delivery* and the since-2022 sentence in the speech; the 85-point equity sentence in the press
release) and two are renderings — the Thai sentence, whose 182-character original is present in R5, and
one span re-read out of yesterday's Jordan article so the two pieces cannot drift on one translation.
Arabic: four Latin spans, **all four verbatim**, which is the same four. Normalisation ledger (#159):
whitespace only on all eight comparable spans; the en dash in the speech's sentence is U+2013 in both the
register and both editions; **words changed: 0.**

## 4. The three corrections

**Correction 1 — a byte count taken from the fetch next door.** The Editor's verdict table gave R5 as
184,426 bytes. That is the byte count of the institute's **home page**, fetched one call earlier into the
same directory; R5 is **185,102**. The hash in the same row was correct, the register was correct, and
every other column was correct, which is exactly why nobody read the number again. Applied, and the
Editor's verdict now carries the correction above its own table rather than a silent edit. **No served
page carried this figure** — neither edition's annotation states R5's byte count — so this is a correction
to the operation's own record, not to the publication.

**Correction 2 — an attribution the register does not make, in both editions.** Both editions said level 2
is the floor *the OECD treats* as the threshold for using a skill in real life. The register states the
threshold and attributes it to nobody: «ระดับ 2 ถือเป็นระดับพื้นฐานที่นักเรียนสามารถใช้ทักษะและความรู้ในชีวิตจริงได้».
The OECD's own three registers read for this edition do not define level 2 at all. Both editions now
attribute the description to the institute. **This is the brief's own prohibition — the OECD averages and
statements in this piece are IPST's reporting unless an OECD register carries them — caught applying to a
definition rather than to a number.**

**Correction 3 — two Arabic institutional renderings tightened.** «مدارسُ اللجنة الثانوية» read as the
committee's own secondary schools rather than the secondary schools under the same office, and the Bangkok
group lost the register's own دائرة التعليم. Both corrected against the register's wording. Figures
unaffected.

## 5. Checked and left standing

- **"The test those rises passed."** The register does not attach the significance word to Thailand's three
  rises in the sentence that states them; it attaches it to the eight-name list, of which Thailand is a
  member. Membership of a list carries the list's stated condition, so the sentence is licensed — and it is
  the only inference in the piece that needed this ruling made explicitly.
- **"University demonstration schools."** The notice's category is «กลุ่มโรงเรียนสาธิต», demonstration
  schools. The qualifier *university* comes from the spreadsheet's own longer name for the same group,
  «โรงเรียนสาธิตของมหาวิทยาลัยในสังกัดกระทรวงการอุดมศึกษา...». Both registers are the institute's and the
  group is the same; the qualifier is supported, by R6 rather than by R5, and this is where that is written
  down.
- **The venue.** The register gives Prince Ballroom 3, Prince Palace Hotel, Bangkok. "A conference room at
  a Bangkok hotel" is accurate and deliberately unnamed; naming a hotel would be the piece's least useful
  specific.
- **The subset arithmetic.** Re-computed from the two quoted lists as sets: eight names, sixteen names,
  **eight in the intersection, zero outside it.** The eight on List A that are not on the institute's list
  are the eight the piece names.
- **No all-three-subject riser list in any OECD register read here.** Re-checked by searching all three
  snapshots for *all three*, *three subjects* and *in all three*: the phrase occurs for **low performers**
  and for **top-ten ranking**, never for a riser list. The dek's claim holds.
- **No Buddhist-era year reaches either edition.** Searched both bodies for 2569, 2568 and 2570: absent.

## 6. What I could not verify, stated as such

- **The Thai-to-English and Thai-to-Arabic renderings as translation.** No Thai reader sits at this desk
  either. What is verified is that the Thai original is present in the served bytes, that both editions
  carry the same figures out of it, and that the register's own hedge travels with the list in both.
- **The institute's own arithmetic.** Whether IPST's columns, significance tests and OECD averages are
  right is IPST's to answer. This piece says what the register says and names the register.
- **Whether the other seven of the eight would confirm their own entries.** One does — Jordan, in Arabic,
  on the same day, which is why that paragraph is in the piece. The other six are named and not
  characterised.

---

## ADDENDUM, same run, two hours after the flip: CORRECTION 4, and it is the piece's frame

**The piece shipped saying the OECD's registers do not carry the eight-country finding. They do.** It is
in Chapter 2 of *PISA 2025 Results (Volume I)* — **"as shown in Table I.2.6, it is equally relevant to
note that eight countries and economies improved their performance in all three subjects"** — and
Table I.2.6 prints the 2022-to-2025 change in science, reading and mathematics for every system that can
be compared in all three.

**How it was found, because the how is the lesson.** After the flip this run went looking for a register
to unblock the two rows in flight, and read the link list inside the Volume I full-report page we have
been citing since 2026-11-26. It links twenty chapter pages of the same report. The Internet Archive holds
snapshots of them. Nobody had opened one. **The register that answered the question was one link inside a
register we had already read, banked and hashed three times.** A register is not a page; it is a document,
and we had been reading its front door.

**What was wrong and what was right.** The published claim was that the sentence appears in none of *the
three OECD registers read for this edition* — literally true, and it was carrying an implication the piece
then made explicit in its own words: *a count the international release does not carry*. That implication
is false. What survives, re-checked against the chapter's served text: the OECD **counts** eight and
**does not name them** in that chapter; the names and the significance condition are IPST's; the eight
derivable from the table's ranking are the eight IPST names, in the same order; and the three registers
this edition opened with carry neither the count nor the names, which is why piece 1 found three lists.

**Applied in both editions in one commit**: a new section that quotes the chapter, prints Table I.2.6's
nine relevant rows, and sets Saudi Arabia's +23, +5, +1 immediately above Thailand's +23, +13, +13 as the
near-miss that shows what the list tests; a rewritten paragraph where the false implication stood; new
deks in both languages; the chapter added as a fifth register in both annotations with its hash, its byte
count and its own source line.

**And the correction brought a corroboration the piece did not have an hour ago.** Thailand's three
changes in the OECD's table are **+23 science, +13 reading, +13 mathematics** — the three figures IPST
states in prose, now printed by a second register in another country. Correction 2 of this verdict was
about an attribution the register does not make; this one hands the piece something stronger than the
claim it replaced.

**Normalisation ledger (#159) for the new span.** The chapter's served text renders the link as
*"Table I.2.6 ,"* with a space before the comma, a markup artefact of the anchor; the body prints
*"Table I.2.6,"*. Whitespace only, **words changed: 0**, and the clause from *it is equally relevant* to
*all three subjects* is verbatim.

**Length.** The EN body goes from 1,558 to 1,953 words, over the brief's 1,800 ceiling by 153. Allowed on
the Editor's own authority and recorded rather than trimmed: the words bought are a register, a table and
a near-miss row, and a length ceiling is guidance where the non-negotiables are not.

**What this does NOT change.** Every figure verified in sections 2 and 3 above stands; the nine-round
table, the subset arithmetic and the two equity sentences are untouched. **And the eight-name list is
still the institute's**: the chapter's cell colours are not in the served text, so which rises are
statistically significant cannot be read out of the OECD register we hold, and the piece says so in the
annotation.
