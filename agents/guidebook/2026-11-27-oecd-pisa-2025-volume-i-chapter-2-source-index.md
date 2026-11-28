# Source index (row 156) — OECD, *PISA 2025 Results (Volume I)*, Chapter 2, "Student performance in PISA 2025"

**Opened 2026-11-27 by the daily run.** Three Edition 06 pieces now lean on this chapter and it had no
source index. Test 1 is pre-cleared at the index level for the tables listed below; every figure is still
re-read at compose (#101).

## Reachability, measured and re-measured

- **`www.oecd.org` answers this runner 403** and has all month. Re-tested 2026-11-26 and twice on 2026-11-27.
  The refusal is **not routed around**.
- The chapter is read from the Internet Archive. **Cite the capture's own fourteen-digit timestamp, not the
  date you asked for, and name the object you measured — ruling #161.**
- Capture used: **`20261104162528`**. Raw snapshot decompressed: **2,426,000 bytes**, sha256
  `e5a429b011ff90e5676417dda3cf5358b2f72b940ee068fae3faa96a6f068a71`. Reproduced to the byte on 2026-11-26
  and 2026-11-27.
- The other two objects of the same capture, recorded so a future reading does not mistake one for another:
  playback page **2,544,478**, raw gzip **279,017**. `curl --compressed` on the raw path gives 2,420,884 and
  is not the house method.
- **How the chapter was found:** it is one of twenty chapter pages linked from the `href` set of the Volume I
  full-report page, which this operation had read, hashed and re-hashed three times without opening a room.
  *A register is a document, not a page.*

```
http://web.archive.org/web/20261104162528id_/https://www.oecd.org/en/publications/
  pisa-2025-results-volume-i_73451bc5-en/full-report/student-performance-in-pisa-2025_23e075c2.html
```

## The tables, read in full and what each is for

| Table | Caption as printed | What it answers | Watch |
|---|---|---|---|
| **I.2.1** | *Comparing countries' and economies' performance in science* | each system's 2025 science mean, and the systems whose mean is **not statistically different** from it | **carries NO numeric OECD average** — only the bands *significantly above / not statistically different from / significantly below*. A piece that attributes 482 to this table is wrong (the Qatar verdict's repair 5) |
| **I.2.3** | *Comparing countries and economies on the science competency subscales* | the same overall science mean in column 1, then three subscale means | **this is where the chapter prints the OECD average as a number**: OECD average 482 482 481 480; Qatar 434 435 433 438 |
| **I.2.6** | *Change between 2022 and 2025 in mean performance in science, reading and mathematics* | the three-year change, **ranked descending by the science change**, for systems comparable in all three subjects | **printed as THREE PANELS side by side**, so the served text runs across them and a row distance is a fact about the page, not the table. Significance is carried by **cell colour**, which served text does not preserve |
| **I.2.8** | *Change between 2022 and 2025 in low- and top performers in science* | two columns, *"Change in percentage of low performers"* and *"…top performers"* | the unit is **percentage points**, and it is not comparable with I.2.6's score points |
| **I.2.9** | *Trends in mean performance … since 2015*, subtitled *"Based on average decennial trend"* | a trend **fitted across cycles**, not the difference between two of them | never set against I.2.6 as if one ruler |

| **I.2.10** | *Change between 2022 and 2025 in the socio-economic gap in science performance* | the three-year change in **score points** for *Disadvantaged students*, *Advantaged students* and the *Socio-economic gap* between them | **a score-point change table that most readers never reach.** 74 entries. Its note asks only *"Only countries and economies that can compare PISA 2022 and PISA 2025 results are shown."* — **no subject condition**, so its population is WIDER than I.2.6's |
| **I.2.11** | *Change between 2022 and 2025 in low and top performers in science, by national quarter of socio-economic status* | the same two shares as I.2.8, split by bottom and top national quarter | **percentage points**, 74 entries, and not comparable with I.2.10 one row above it despite the near-identical caption |
| **I.2.12** | *Change between 2022 and 2025 in mean performance in science, by gender* | the three-year change in **score points** for *Girls*, *Boys* and the *Gender gap (Boys - Girls)* | **the second score-point change table with the wide population.** 76 entries, same note as I.2.10, OECD average-35 at -2 / -3. **This is the table that answers *did the score go up* for a system I.2.6 excludes** |
| **I.2.13** | *Change between 2022 and 2025 in low- and top performers in science, by gender* | I.2.8 split four ways: low performers girls then boys, top performers girls then boys | **percentage points**, column order read off the header row and never assumed |

**THE GATING RULE THIS CHAPTER RUNS ON, AND IT IS THE INDEX'S MOST LOAD-BEARING LINE — added 2026-11-28
under ruling #162.** The chapter has **four** tables that report a change in score points, and they fall
into two populations with different gates:

- **I.2.6 and I.2.9 print the change WHOLE** — one figure for all students — and are gated on something
  other than the subject: I.2.6 on comparability *"in all three subjects"*, I.2.9 on *"at least two
  previous assessments among PISA 2015, PISA 2018 and PISA 2022"*.
- **I.2.10 and I.2.12 print the same change SPLIT** — by socio-economic status and by gender — and are
  gated only on 2022 and 2025 being comparable at all.

**So a system can be comparable in science, absent from both whole-change tables, and present in both
split ones.** Uzbekistan is exactly that: no row in I.2.6 or I.2.9, and **+85 / +80 score points in
I.2.12** and **+85 / +87 in I.2.10**, the largest row in each. Any piece about a system missing from I.2.6
**must check I.2.10 and I.2.12 before saying the chapter prints no score-point change for it.** The
Uzbekistan draft did not, shipped the claim into its title and dek, and was caught at cell 6.

**The enumeration, for any future piece that needs it.** Every cell reading a country name was listed
across all fourteen numbered tables. For Uzbekistan the answer is **eight of fourteen** — I.2.1, I.2.3,
I.2.4, I.2.8, I.2.10, I.2.11, I.2.12, I.2.13 — and the route is thirty seconds of parsing. **For a piece
whose spine is an absence, that sweep is the verification** (#162 clause 3).

Also present: I.2.2 (proficiency levels described), I.2.4 (computational problem solving), I.2.5
(within-country correlation across domains), I.2.7 (yearly learning gain, ten systems), Figure I.2.5
(average change in science for low and high achievers 2022-2025), and 112 distinct table and figure captions
in all. Source line for I.2.6: *OECD, PISA 2025 Database, Tables I.B1.2a.36, I.B1.2a.37 and I.B1.2a.38*.

## Rows read and confirmed in served text, 2026-11-27

**Table I.2.6** — Georgia 38/10/26 · Cambodia 35/18/29 · Jordan 32/20/26 · Montenegro 32/13/5 · United Arab
Emirates 26/15/21 · Saudi Arabia 23/5/1 · Thailand 23/13/13 · Türkiye 18/16/8 · Philippines 17/20/16 ·
**Qatar 2/−1/2** · **OECD average-35 −3/−14/−9**.

**Table I.2.8** — Qatar −0.8 / −0.1 (percentage points) · OECD average-35 1.2 / −0.3.

**Table I.2.9** — Qatar 19/18/12 · **United Arab Emirates 18/−6/20** · Saudi Arabia 37/−18/25 · Thailand
4/−20/−16 · Türkiye 62/34/35 · Cambodia 72/36/57 · **OECD average-35 −7/−27/−24**.

**Table I.2.1** — Qatar **434**, not statistically different from *Mauritius, Uzbekistan, Montenegro,
Albania\*, Greece, Thailand, Serbia*. **Table I.2.3** — Qatar 434, OECD average 482.

**The asterisk on Albania is the register's own.** The chapter does not define it and points to *Annex A2,
"Population coverage, and school and student participation rate standards"*, which has not been read. The
marker is reproduced and **not** interpreted.

## The quoted spans this index pre-clears, verbatim in the capture above

- *"as shown in Table I.2.6 , it is equally relevant to note that eight countries and economies improved
  their performance in all three subjects."* (the served text renders the anchor with a space before the
  comma)
- *"Only five countries/economies, Montenegro, Qatar, the Slovak Republic, Türkiye and the United Arab
  Emirates, , were able to simultaneously reduce their shares of low-performing students and increase their
  shares of top-performing students over the past decade"* — **the doubled comma is the register's own**
- *"in Luxembourg, Macao (China), Qatar and the United Arab Emirates, more than half of students have an
  immigrant background"* and *"Each should therefore be examined in its own context"*
- *"Only countries and economies that can compare PISA 2022 and PISA 2025 results in all three subjects are
  shown."* · *"Countries and economies are ranked, in descending order of the change in science performance
  between 2022 and 2025."*

## Standing cautions for any piece built on this chapter

1. **No significance claim rests on this chapter alone.** Table I.2.6 marks it by colour; colour is not text.
2. **Never mix I.2.6 with I.2.9.** One is a three-year difference, the other a fitted decennial trend. Most
   list memberships in the PISA 2025 release are decade memberships.
3. **Never mix I.2.6 with I.2.8.** Score points and percentage points.
4. **Name the table a figure came from.** Two of the chapter's tables carry the same science mean and only
   one carries the OECD average.
