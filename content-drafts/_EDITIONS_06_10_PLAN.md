# Editions 06 to 10. Founder directive, 2026-11-26

**Set by Vini on 2026-11-26. This file is binding and it supersedes the standing ledger's "no edition"
state (GitHub issue #13 is answered by it).** The operation does not ask him anything further about
these five editions. Every call inside this plan is the Manager's and the Editor's to make.

His words: *"Each edition minimum 6 pieces. Each day at least 1 piece. Each week one edition. Deploy
whatever team needed, but just do it and don't depend on me for anything else. I want content."*

## The calendar (Asia/Dubai dates)

| Ed | Theme | Window | Minimum |
|---|---|---|---|
| 06 | **PISA, globally.** PISA 2025 results (OECD, launched 8 Sep 2026): what moved, where, and why. | Thu 26 Nov to Sun 6 Dec (a lead-in week plus one) | 6 pieces |
| 07 | **China.** | Mon 7 Dec to Sun 13 Dec | 6 pieces |
| 08 | **Latin America, with the focus on public education.** | Mon 14 Dec to Sun 20 Dec | 6 pieces |
| 09 | **Special and sponsored education programmes**, with Entreculturas as the highlight piece. Every other piece follows the same frame: programmes run or funded by foundations, NGOs, faith networks, companies or donors; special events; special and inclusive education. | Mon 21 Dec to Sun 27 Dec | 6 pieces |
| 10 | **The UAE, with the focus on Abu Dhabi.** | Mon 28 Dec to Sun 3 Jan 2027 | 6 pieces |

## The three numbers, and how they are counted

1. **At least one piece ships every day.** A piece "ships" when it is `approved: true` in BOTH
   editions and on `origin`. Shipped means served: the run checks the deploy went green.
2. **Each edition reaches at least six pieces.** Seven is the target (one per day). Six is the floor.
3. **One edition per week.** The next edition opens on its Monday whether or not the last one reached
   six. If an edition is short at its Sunday, it stays open and keeps receiving pieces until it reaches
   six, while the new edition also runs. The calendar never slips. A short edition is named in the brief.

## How a piece ships (unchanged gate, faster path)

The eight-cell gate in `_STANDING_LEDGER.md` stays exactly as it is: Editor brief, EN draft, Editor
five-test verdict, AR composition, Arabic Editor gate, Verifier verdict, hero still + og card, the flag.
**Quality is not traded for speed.** What changes is the throughput around the gate:

- **Each piece ships the day its own gate closes**, tagged `edition: N` in frontmatter. No wave flip.
  Edition 05's 71 held days must never recur.
- **Recon one edition ahead.** By each Thursday, the next edition has a slate of at least 9 candidates,
  each with 2 or more primary registers already opened and read in served text. The slate lives in
  `content-drafts/recon/` as `<date>-ed0N-slate.md`. Three spares exist because some candidates fail Test 1.
- **Three or more pieces in flight at all times**, at different cells, so a piece that parks does not
  leave a day empty.
- **Pick the candidate whose sources are already open.** A piece whose primary register cannot be
  reached today is swapped for one whose register can. A blocked source is a reason to swap, not to wait.
- **Edition registry.** On the day an edition's first piece ships, its row goes into
  `web/src/lib/editions.ts` with `status: 'current'`, a ground, an accent, a motif and a line-art cover in
  the house style. The previous edition moves to `'closed'` when it has six pieces. The Designer makes the
  cover in the lead-in, not on ship day.
- **Hero stills in batches.** The Designer draws each edition's stills as one batch while the slate is
  drafted, to the existing standard (pure line, one orange accent), with a contact sheet reviewed.

## Where the time goes (this overrides the five-function balance)

The operation spent October and November building 16 assertions and 83 rulings while shipping 2
pieces. That ratio ends today.

- **Content gets at least 70% of every run.** The content function runs FIRST, not after quality.
- **Quality:** build and run the existing gates. Fix only what blocks a ship or breaks a served page.
  **No new assertion is built** unless a defect on a served page needs one. The standing-queue head
  rule is suspended except for DEFECT rows.
- **Research:** the daily knowledge increment IS the recon for the next edition's slate (a source index
  entry counts). A new numbered ruling is filed only when a piece's verdict earns one.
- **Growth:** one small action, or the line "growth: none today, content took the time". Both are fine.
- **Brief:** one screen. Lead with: pieces shipped today (titles, both languages), edition count
  (`Ed06: 3 of 6`), pieces in flight by cell, and tomorrow's ship. No essays.

## The team for this plan

The Manager may add any persona the plan needs without asking. Added on 2026-11-26:
`agents/13_content_creator_3.md` (third English drafting hand) and
`agents/14_arabic_content_creator_2.md` (second Arabic composer). Leans: CC1 GCC/MENA, CC2 comparative
and Latin America, CC3 the edition's lead theme (PISA, China, Entreculturas). The Arabic side splits by
piece, not by language register.

**A second run each day.** `.github/workflows/madar-content.yml` runs the content pipeline only
(`.claude/skills/madar-content/SKILL.md`), twice a day, in the same concurrency group as the daily run so
the two never touch the tree at once. The daily and weekly runs' envelope went from 180 to 400 turns, and
the publish step now runs even when the agent step overran, so a capped run's pushed work is served.

## Edition notes (starting points, every one to be verified in served text)

**06 PISA.** Primary set: OECD *PISA 2025 Results* Volumes, country notes, the launch press release and
the Secretary-General's 8 Sep 2026 speech. Candidate angles: the record low in OECD reading and maths;
the equity gap that narrowed because advantaged students fell; the systems that cut low performers AND
grew top performers (the OECD names Türkiye, the UAE, Montenegro, Qatar and the Slovak Republic); the
new Learning in the Digital World assessment; devices and screen time against results; science and
environmental agency; a MENA reading (Qatar, UAE, Saudi Arabia, Jordan); a Latin America reading; Asia's
top systems. Every figure carries its scale, year and comparison group in the sentence.

**07 China.** Primary sources in Chinese and English: Ministry of Education (moe.gov.cn), State Council
notices, provincial bureaus, Xinhua for dates only. Candidate angles to verify: the move to free
preschool, the "double reduction" policy years on, rural boarding schools and left-behind children, AI
education guidance for schools, teacher pay and rural teachers, vocational routes, whether and how China
took part in PISA 2025. Respect the scope rule: report what the state and its registers say, with
named voices, no editorial posture on the political system.

**08 Latin America, public education.** Public systems first: Brazil (Ceará and Sobral literacy, the
national literacy commitment), Chile, Colombia, Mexico, Peru, Uruguay (Ceibal), Argentina, the
Caribbean. Ministry registers and national assessments (SAEB, SIMCE, Saber, PLANEA or its successor).
CC2 leads. Spanish and Portuguese primaries are read in the original.

**09 Special and sponsored programmes, Entreculturas highlight.** The highlight piece is a profile of
Entreculturas and the programmes it supports (for example through the Fe y Alegría network), told
through named people and the programmes' own reports. **Madār is not sponsored by anyone**: "sponsored"
describes the programmes covered, never this publication, and no piece implies a partnership. The
other pieces follow the same frame: foundation or NGO funded programmes, faith-network schools, special
and inclusive education for children with disabilities, refugee education, and special events (for
example the International Day of Persons with Disabilities on 3 December, read for what it produced).
Respect for religion applies.

**10 UAE, Abu Dhabi focus.** Public sources only: ADEK public pages, published policies and inspection
frameworks, the Ministry of Education, the federal inspection framework, Bayanat and SCAD data, WAM for
dates. **No internal, unpublished or non-public material of any kind, ever.** Fair and plain, like every
other system Madār covers. The in-flight row `2026-11-22-abu-dhabi-irtiqaa-biennial-yield` (Editor
returned it on 2026-11-25 with four repairs) moves into Edition 10: finish its repairs in the Ed10 lead-in
week and ship it as Ed10's first piece. Until then it is parked and costs no run time.

## What is NOT changed

Every non-negotiable in `CLAUDE.md`: figures cited as read, held pieces invisible, the Editor is the
filter, Arabic is composed, no invented traffic. A piece that fails its gate is held, and the day's ship
comes from the next piece in flight. That is why three must always be in flight.
