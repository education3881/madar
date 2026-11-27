# Edition 06 recon: PISA 2025, the OECD's own three registers (first-party read, 2026-11-26)

**Researcher's source index, not a draft.** Banked the day Edition 06 opened, so every Ed06 drafter starts
from the same served text. A banked read licenses no quotation: the drafter re-opens the register at
compose time (#101).

## How the text was read, declared first (#158)

- `www.oecd.org` answers this runner's direct requests with **403**. The refusal was **not routed around**.
- All three registers were read in served text from the **Internet Archive's own snapshots** of the OECD
  URLs, fetched raw (`id_` mode) on 2026-11-26 from the founder's desktop workspace, because the cloud
  workspace's tunnel to `web.archive.org` closes mid-exchange. The snapshot bytes are gzip; decompressed and
  hashed:

| Register | OECD URL | Snapshot | Decompressed bytes | sha256 (first 16) |
|---|---|---|---|---|
| R1 press release, 8 September 2026 | `oecd.org/en/about/news/press-releases/2026/09/pisa-2025-students-reading-and-mathematics-performance-declined-sharply-across-the-oecd.html` | 2026-11-15 23:24:02 UTC | 1,468,371 | `096bb651ddbda014` |
| R2 *PISA 2025 Results (Volume I)*, full-report page | `oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report.html` | 2026-11-16 23:59:12 UTC | 1,614,913 | `01b2bd4aa78bf802` |
| R3 Secretary-General's launch speech, 8 September 2026 | `oecd.org/en/about/news/speech-statements/2026/09/international-launch-of-pisa-2025.html` | 2026-11-15 13:53:55 UTC | 1,464,823 | `33b350b2803a4906` |

- Text was extracted by stripping `script`, `style` and `noscript`, then tags, then unescaping entities.
  **The registers use U+2019 for apostrophes and U+2013 for dashes.** A needle typed with U+0027 manufactures
  an absence (#150).
- **The launch date. CORRECTED 2026-11-26 by the Verifier.** This line first said the registers date
  themselves only by their URLs. That was wrong. All three print **8 September 2026**, and R3 states it was
  given "to launch the PISA 2025 results on 8 September 2026". The first read searched the text for the
  date in the wrong form and recorded the miss as an absence (#150 in a new costume). Pieces may print
  8 September 2026.

## What each register says, verbatim

### R1, the press release

- "Student performance across OECD countries has continued to decline, reaching the lowest average ever recorded by the OECD Programme for International Student Assessment (PISA) in mathematics and reading."
- "Across the OECD, one in five 15-year-old students is now a low performer in science, mathematics and reading, up from 16% in 2022."
- "PISA 2025 was the largest assessment to date, involving 760 000 students across 91 countries and economies."
- "This year’s edition focused on science, where average performance was stable between 2022 and 2025 across OECD countries, after having trended downward between 2009 and 2022."
- "Average reading scores fell by 28 points across OECD countries between 2015 and 2025, equivalent to about one and a half years of learning. Mathematics scores fell by 22 points, equivalent to just over one year of learning."
- "Among non-OECD PISA participants, reading scores fell by 16 points and mathematics scores by eight points over the same period."
- "Across OECD countries, advantaged students scored 85 points higher in science than disadvantaged students. The gap narrowed between 2022 and 2025, but largely because advantaged students performed less well rather than improvements among disadvantaged students."
- Cormann, quoted: "PISA 2025 shows that reversing declines in student performance is urgent."
- **LIST B (dated 2015 to 2025):** "Between 2015 and 2025, some education systems improved performance in contrast to broader trends. Science performance rose in Lithuania, the Slovak Republic, Türkiye, the Dominican Republic, Georgia, Macao (China), Montenegro, Qatar, Thailand, the United Arab Emirates, and Uruguay." *(eleven names)*
- **LIST C (in science, undated in its own sentence, follows List B):** "Türkiye, the Slovak Republic, Montenegro, Qatar and the United Arab Emirates increased their share of top performers while reducing their share of low performers in science."
- "Most participating Chinese jurisdictions, together with Estonia, Japan, Korea, Singapore, Chinese Taipei and the United Kingdom, ranked among the ten highest-performing education systems in science, mathematics and reading."
- "More than one in four students said that classmates were distracted by digital devices in most or every science lesson."
- "Across OECD countries, almost two-thirds of students reached the relevant proficiency level in computational problem solving. But only half reached this level while also demonstrating basic proficiency in science, reading and mathematics."

### R2, Volume I full-report page

- "In 2025, more than 760 000 students, representing around 33 million 15-year-olds across 91 countries and economies, participated in the PISA assessment."
- "Following the unprecedented drop in performance recorded in PISA 2022, learning outcomes have largely stagnated or continued to decline in many countries."
- **LIST A (undated in its own sentence):** "Within the OECD, science scores rose in Costa Rica, the Slovak Republic, Türkiye and the United Kingdom. Among non-OECD members, scores also went up in Cambodia, El Salvador, Georgia, Jordan, Mongolia, Montenegro, the Philippines, Saudi Arabia, Thailand, the United Arab Emirates, Uruguay and Uzbekistan." *(four plus twelve)*
- LIST C again: "Türkiye, the United Arab Emirates, Montenegro, Qatar and the Slovak Republic reduced their share of low-performing students, while increasing their share of top-performers."
- "Across the OECD, 20% of 15-year-old students are now estimated to be low performers across all three subjects – up from 16% in 2022."
- "The weakening of performance predates the COVID-19 pandemic in many countries, pointing to deeper and more persistent challenges within education systems."
- "OECD average science scores fell from 489 to 482 points between 2015 and 2025, while remaining broadly stable among non‑OECD participants at 436 and 437 points, respectively." *(non-breaking hyphen U+2011 in non‑OECD)*
- "OECD average mathematics scores fell from 485 points in 2015 to 463 points in 2025."
- "Average reading scores fell from 489 to 461 points across OECD countries and from 428 to 412 points among non-OECD participants between 2015 and 2025."

### R3, the launch speech

- "Since 2022, science scores went up in Costa Rica, Slovakia, Türkiye and the United Kingdom – and in 12 other countries and economies." **This dates LIST A.** R2 names the same four OECD members and exactly twelve others.
- "Over the past decade, Türkiye, the United Arab Emirates, Montenegro, Qatar and Slovakia all cut their share of low performers and grew their share of top performers at the same time." **This dates LIST C.**
- "Over two decades, Türkiye has moved from below the OECD average in science to above it."
- "Cambodia gained 35 points in just three years – well over a year of learning."
- "Across OECD countries, mathematics scores fell by 9 points between 2022 and 2025."
- "That is about half a school year of learning – and it comes on top of the record 15-point drop between 2018 and 2022."
- "In science, results held steady between 2022 and 2025." / "Science scores had been falling since 2009."
- "That gap did narrow between 2022 and 2025. But only because advantaged students did worse – not because disadvantaged students did better."
- "In 2022, 77% of students said their parents asked them about their school day at least once a week." / "In 2025, it was 71%. The drop is biggest among boys and disadvantaged students."
- "The share of hasty readers has nearly doubled since 2018."
- "Beyond about five hours a day, results start to fall."
- "Across the 91 countries and economies, around 1.9 million students are top performers in science." / "Yet almost half of them do not expect to be working in science, technology, engineering or mathematics (STEM) at age 30."
- "Across OECD countries, around four in ten students are in schools where the principal says a shortage of teachers is holding back learning."
- "Only 64% of students reached the level we consider proficient in computational problem solving."

## Two things the three registers do NOT carry

1. **No register states the period of List A in List A's own sentence, and no register states the period of
   List C in List C's own sentence.** Both are dated only by R3. A piece that dates them must cite R3.
2. **Qatar is on List B and List C and NOT on List A.** That is what the registers print. Nothing here says
   why, and nothing here says Qatar's science score fell after 2022. A piece may say Qatar is absent from the
   since-2022 list. It may not say anything about Qatar's 2022 to 2025 change without Qatar's country note.

## Edition 06 slate (nine candidates, three spare)

| # | Working title | Spine | Registers in hand | Still owed |
|---|---|---|---|---|
| 1 | **Three lists of risers** | The release carries three improver lists on three clocks. Who is on all three. | R1, R2, R3 | none (ships first) |
| 2 | The gap that closed from the top | 85 points, narrowed because advantaged students fell | R1, R3 | Volume I socio-economic chapter |
| 3 | The question at the dinner table | 77% to 71% of parents asking about the school day | R3 | Volume I or III table, boys and disadvantaged split |
| 4 | Hasty readers | Hasty reading nearly doubled since 2018, reading fell 28 points since 2015 | R3, R2 | the reading-trends box R2 lists ("motivation and test-context effects") |
| 5 | Five hours | Device use for learning helps, then hurts beyond about five hours | R3, R1 | Volume chapter on digital use |
| 6 | Türkiye above the line | Two decades from below to above the OECD science average | R3 | MEB national PISA release, Türkiye country note |
| 7 | The UAE on every list | The one Gulf system on all three lists | R1, R2, R3 | MoE UAE / ADEK public PISA statement, country note |
| 8 | Cambodia's 35 points | 35 points in three years | R3 | Cambodia country note, MoEYS statement |
| 9 | Two-thirds and a half | Computational problem solving with and without the basics | R1, R3 | LDW chapter (full results May 2027, so careful tense) |

---

## CORRECTION, 2026-11-27, at the Editor's desk — R2's provenance triple, and the method that reproduces it

**The banked row for R2 (the Volume I full-report page) named a snapshot of 16 November 2026 and the sha256
`01b2bd4aa78bf802…`. Neither is reproducible, and the byte count beside them belongs to a different
capture.** Re-measured today, twice, from this runner:

| What was asked for | What the archive returns | Bytes | sha256 (first 16) |
|---|---|---|---|
| `/web/20261116id_/…` | capture **20261116235912** | 1,634,885 | `766441db01c15257` |
| capture **20261114165129** | itself | **1,614,913** | `1c3018b4d17e205b` |
| capture 20261112193517 | itself | 1,618,973 | `1e6eb36b054625a2` |
| capture 20261113171658 | itself | 1,635,393 | `ebd980ecda49fdee` |

So the **byte count 1,614,913 was right** and is the **14 November** capture's; the date recorded was the
date *asked for*, not the capture's own, and the hash reproduces from no capture of this page. The repair is
in both editions of `2026-11-27-thailand-pisa-2025-fourth-list`, which had already shipped carrying it, and
in the Qatar draft.

**Two method facts that caused it, written down so the next run spends nothing on them.**

1. **A Wayback request without a full fourteen-digit timestamp is resolved to the nearest capture, and which
   capture that is changes as the archive indexes more of them.** `…/web/20261116id_/` resolved to the
   11-14 capture when the read was banked and resolves to the 11-16 capture today. **Cite the capture's own
   timestamp, never the one you asked for.**
2. **One capture has three byte counts, because it has three objects.** For Chapter 2:

   | Object | How fetched | Bytes |
   |---|---|---|
   | playback page (toolbar injected, URLs rewritten) | `/web/<ts>/…` | 2,544,478 |
   | raw snapshot as stored (gzip) | `/web/<ts>id_/…` | 279,017 |
   | **raw snapshot decompressed — the document the OECD served** | `/web/<ts>id_/…` then `gunzip` | **2,426,000** |

   The third is the one the house cites, and it is the one that reproduced R1, R3 and R8 to the byte today.
   The first two are different objects and will never match it. *(`curl --compressed` on the raw path gives a
   fourth number, 2,420,884, and is not the house method.)*

**The transferable rule, filed as ruling #161:** a provenance triple is *capture timestamp + object + hash*,
and a triple that names only a date has named a moving target. The figures here are re-derivable by anyone
with this file and a shell, which is what the old row was not.
