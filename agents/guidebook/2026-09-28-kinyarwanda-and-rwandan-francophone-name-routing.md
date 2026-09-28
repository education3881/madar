# Transliteration routing — Kinyarwanda and Rwandan francophone names into Arabic

**Filed:** 2026-09-28, Arabic Editor's gate on Edition 05 row 6 (Rwanda), the publication's first
Rwandan piece. **Section 1 row 67.**
**Peer:** the West African labial-velar routing filed 2026-08-29 (row 33, `kp` /k͡p/ → **كب**). Same
purpose: settle the phoneme-to-grapheme decisions **once**, so the next Rwandan or Great Lakes piece
inherits them instead of re-deciding them at a gate under time pressure.

## The two-name problem a Rwandan piece presents

Rwandan public names come in two layers and they route differently:

1. **Kinyarwanda names** — *Abayikunda, Mugenzi, Irere, Umwalimu, Nyagatare*. Transparent phonology,
   consistent Latin orthography, and no Arabic tradition to inherit.
2. **French given names**, carried widely from the francophone period — *Pélagie, Claudette, Jean-Baptiste*.
   These route by **French** phonology, not by Kinyarwanda, and getting this wrong is the likeliest
   error: *Pélagie* read as Kinyarwanda would produce *بيلاغي*.

**A Rwandan's full name may therefore need two different routings, one per element.** Pelagie
Abayikunda is the worked case: **بيلاجي أبايِكوندا** — French /ʒ/ → **ج** in the given name, Kinyarwanda
throughout the family name.

## The routing table

| Sound | Latin | Arabic | Note |
|---|---|---|---|
| /a/ | a | **ا** | |
| /e/ | e | **ي** (or fatḥa + ي) | Kinyarwanda /e/ is close [e]; *Irere* → إيريري |
| /i/ | i | **ي** | |
| /o/ | o | **و** | |
| /u/ | u | **و** | |
| /b/ | b | **ب** | |
| /d/ | d | **د** | |
| /g/ | g | **غ** | **Settled by the established كاغامي**; never ج, never ك. *Kigali* → كيغالي |
| /k/ | k | **ك** | |
| /m/ | m | **م** | |
| /n/ | n | **ن** | |
| /ɲ/ | ny | **ني** | *Nyagatare* → نياغاتاري |
| /ɾ/ | r | **ر** | Kinyarwanda r is a flap; never ل, despite the r/l allophony in some words |
| /s/ | s | **س** | |
| /ʃ/ | sh | **ش** | *Shallon* → شالون |
| /t/ | t | **ت** | |
| /w/ | w | **و** | |
| /j/ | y | **ي** | See the `-yi-` rule below |
| /z/ | z | **ز** | *Mugenzi* → موغينزي |
| /p/ | p | **ب** | Not native to Kinyarwanda; appears in loans and French names. **ب, never پ** — the house prohibits Persian-augmented letters |
| /ʒ/ | g/j in French names | **ج** | *Pélagie* → بيلاجي |

### The `-yi-` rule, which is the one decision worth writing down

A Latin `yi` is consonant /j/ followed by vowel /i/. Written as a bare **ي** it collapses:
*Abayikunda* → أبايكوندا reads /abaykunda/, losing a syllable. Two repairs are available and the house
picks the first:

- **أبايِكوندا** — one ي carrying the consonant, with an explicit **kasra** marking the vowel. Preferred:
  the house already counts tashkeel as +1 in the dek cap and writes voweled prose, so a diacritic is in
  register, and the string stays short.
- ~~أباييكوندا~~ — doubled ي. Common in Arabic newspapers, and rejected here: it reads as a long /iː/
  as readily as /ji/, so it trades one ambiguity for another at greater length.

Same rule applies to `-yu-`, `-ya-` in word-medial position.

## Institutions and acronyms, per #28a and the 08-02 conventions

- **Latin, unchanged**: REB, NESA, TTC/TTCs, MINEDUC (as a parenthetical tag), **Umwalimu SACCO**. That
  last is the instructive one: it is a Rwandan cooperative whose own name is Kinyarwanda in Latin script,
  and it is **never transliterated** — an institution keeps its own tag, and *أومواليمو ساكو* would be a
  tag this operation invented.
- **Arabic with the Latin acronym on first mention**: «مجلسُ التعليم الأساسيِّ الرواندي (REB)»،
  «هيئةُ الامتحانات والتفتيش المدرسيِّ الوطنية (NESA)»، «وزارةُ التعليم الرواندية (MINEDUC)».
- **Arabic by established name, not by routing**: **البنك الدولي**.

## Confirmation status of the forms used, and where the gap is

| Form | Status |
|---|---|
| **رواندا** | **CONFIRMED in served Arabic text** — Al-Sharq (Doha), 08 March 2025: «جمهورية رواندا» |
| **كلوديت إيريري** | **CONFIRMED in served Arabic text** — same register: «سعادة السيدة كلوديت إيريري وزيرة الدولة للتعليم في جمهورية رواندا». Read on the page, not taken from either search summary that offered the same form (#41) |
| **بيلاجي أبايِكوندا** | **By convention, on this routing.** Searched and not found on any Arabic register, as expected for a primary schoolteacher |
| **كيغالي** | **By convention.** غ per the table, consistent with كاغامي. **No first-party Arabic register for the city could be read from this runner**: `mofa.gov.ae`'s Arabic embassy pages — a UAE state register that carries «كيغالي» in its own page titles — served a client-rendered shell to two different clients, and `teachertaskforce.org`'s Arabic page on Rwanda's teacher CPD framework, the single best candidate Arabic register on Rwandan teacher policy, returned **HTTP 403 with a 5,785-byte challenge body** to both `WebFetch` and a browser-identified `curl`. **Walled, not dead** (#70 — the record names the layer that failed). Both carried to the wave's confirmation read, because either would upgrade this row from convention to a served register |

## The standing instruction this row leaves

**A francophone African name is routed element by element, not name by name.** Ask of each element
*which language is this word from?* before routing a single letter — and where the answer is French,
route the French. The failure this prevents is not exotic: it is a single element of a two-element name
routed by the wrong phonology, which produces a plausible Arabic string that is nobody's name.
