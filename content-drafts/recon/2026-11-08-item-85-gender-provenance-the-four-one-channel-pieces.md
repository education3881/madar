# Item 85, first taking — the four one-channel pieces, read against their own registers

**Date** 2026-11-08 · **Queue head** item 85, the board's one DEFECT, raised 2026-11-07 at 1 day ·
**Owner on the row** Arabic Editor + Editor · **Scope taken** the four pieces the row sends first,
because a determination the other edition could contradict has a cheap second opinion and these four
were measured as having none.

**Population taken: 10 honorific tokens over 6 named humans on 4 served Arabic pieces** — the row's own
`arabic_side_reach.py` counts (Oman masc 3 fem 1, Iraq fem 3, Singapore masc 1 fem 1, UAE masc 1).
**22 tokens over the other 10 both-channel pieces are NOT taken** and remain the row's open remainder.

## The ten, one row each

| # | Piece | AR token | Named human | What the cited register PRINTS | Verdict |
|---|---|---|---|---|---|
| 1–3 | `2026-06-20-oman-school-performance-ratings` | السيد ×3 (2 in `sources[]`, 1 in body) | HH Sayyid Theyazin bin Haitham Al Said, Minister of Culture, Sports and Youth | Times of Oman: *"HH Sayyid Theyazin bin Haitham Al Said, Minister of Culture, Sports and Youth, today presided over the launch"* | **EVIDENCED** — `Sayyid` (masc; fem is `Sayyida`) **and** `bin` (masc patronymic; fem is `bint`) |
| 4 | same | الدكتورة ×1 | Dr Jokha bint Abdullah Al Shukaili, CEO of the Authority | gov.om management listing: *"H.E Dr Jokha bint Abdullah Al Shukaili, Chief Executive Officer"* | **EVIDENCED** — `bint`, printed in Latin script by the piece's own cited register |
| 5–6 | `2026-05-28-iraq-mosul-library` | السيدة ×2 | Zena Ali Ahmad, UNDP Resident Representative in Iraq | UNDP release: *"added Ms. Ahmad"* | **EVIDENCED** — `Ms.` |
| 7 | same | الدكتورة ×1 | Dr. Anna-Christine Janke, Country Director, KfW Office Iraq | UNDP release: *"added Dr. Anna-Christine Janke, Country Director of the KfW Office Iraq"* — **no pronoun, no gendered title** | **UNDETERMINED by the register.** #86 clause 2 applied: written into both annotations as this edition's own, dated 2026-11-08. Settling fetch named: KfW's own Iraq-office page |
| 8 | `2026-07-07-singapore-psle-sbb` | السيدة ×1 | Grace Chua, principal, Pasir Ris Secondary | *"Mrs Grace Chua, principal of Pasir Ris Secondary School"* … *"But she noted that students are no longer grouping themselves by academic ability"* | **EVIDENCED twice** — a title **and** a pronoun, the only pronoun in all ten |
| 9 | same | السيد ×1 | Mohamed Ashiq, year head, upper secondary | *"Mr Mohamed Ashiq, the school's year head of upper secondary level"* | **EVIDENCED** — `Mr` |
| 10 | `2026-05-27-uae-madrasa-tiktok` | الدكتور ×1 | Dr. Waleed Al Ali, General Coordinator, Madrasa.org | GDN/WAM: *"Dr. Waleed Al Ali, General Coordinator of the Madrasa.org online platform"*, then *"Dr. Al Ali said"*, *"Dr. Al Ali noted"* — **no pronoun, no gendered title** | **UNDETERMINED by the register.** #86 clause 2 applied, dated 2026-11-08. The MBRGI programme page, also cited, returns 403 to every client here |

**Result: 8 of 10 evidenced, 2 of 10 undetermined, 0 of 10 WRONG.** #86's own sample of ten found two
wrong, so a zero here is a result and not a formality; it is also a sample of ten on four pieces and not
a statement about the remaining 22.

## How the registers were reached

Four fetches answered directly (`timesofoman.com` 200, `stomp.sg` 200, `gdnonline.com` 200, `gov.om` 200).
**`undp.org` returns 403 to every client available here**, direct and on its `/iraq/` path, and was read
through a text-extraction proxy (`r.jina.ai`) — recorded because *how* a register was reached is part of
the read (#70, walled by rendering, not dead). `oaaaqa.gov.om/public/external-activities/cseqa` serves 1,322
bytes that extract to **61 characters** of text: still walled, as the Edition 05 memo already says of the
SLEIC document. `almaktouminitiatives.org` 403.

## Three findings the taking produced, none of which the row predicted

**1 · The gender evidence in a register is almost never a pronoun.** One of the eight evidenced
determinations rests on a pronoun (`she`, Chua). The other seven rest on a **title** (`Ms.`, `Mrs`, `Mr`)
or on a **morpheme inside the name as the register prints it** (`Sayyid`, `bin`, `bint`). Every instrument
and every hand-check this operation has aimed at this class looked for a pronoun first.

**2 · #86 clause 1 is too wide as written, and the correction is a distinction rather than a loosening.**
The clause says *never off the name*, and it was earned by two real errors — Alex Maclean and the Benin
minister — both read off **how the name sounds**. But `bin`/`bint` and `Sayyid`/`Sayyida` are not how a
name sounds: they are morphemes the register prints, obligatory in Arabic naming, and reading one is
exactly as much a read as reading `she`. Four of the eight evidenced determinations stand on one.
**The name's SOUND is not evidence; the name's MORPHOLOGY, as the register prints it, is** — filed today
as a ruling.

**3 · Two of the four "one-channel" pieces have a second channel, and the English edition threw one away.**
Oman's **English** annotation already printed `HH Sayyid Theyazin bin Haitham`, so that piece was never
one-channel; the row's detector reads a closed class of English honorifics (`Dr|Professor|Minister|Sheikh|
Mr|Mrs|Ms|…`) and `Sayyid` and `bin` are not in it — #113's own lesson, a closed class cannot see a title
outside it. Singapore is the sharper case: the register prints **`Mrs Grace Chua`** and **`Mr Mohamed
Ashiq`**, and the English annotation had reduced both to **`Principal Grace Chua and Year Head Mohamed
Ashiq`** — so the evidence was in the register, the Arabic edition kept it, and **the English edition
deleted its own second channel at compose time.** That inverts #101, where Arabic was forced back to the
register and English took the cheap token: here Arabic carried the register's word and English smoothed it.
Both titles are restored to the English annotation today.

## What was written to served bytes

Eight annotation edits across four pairs (EN + AR for Oman ×2, Iraq ×1, Singapore ×1, UAE ×1 — the Oman
and Singapore AR edits carry two and two names respectively). **No body sentence changed**: every one of
the ten honorifics in the prose is consistent with its register or is now declared as this edition's own.
Pair parity preserved — each note is written into both editions (#42).

## What this leaves on the row

**22 tokens over 10 both-channel pieces**, listed in `arabic_side_reach.py` §2. They are cheaper per
token than these four were, because each has an English gendered form that can already disagree — which
is why the row sent them second. Item 85 is **narrowed, not closed**.
