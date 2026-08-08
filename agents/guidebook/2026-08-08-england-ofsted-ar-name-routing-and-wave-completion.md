# England / Ofsted AR name-routing + the Ed04 AR wave closes (Section 1 addendum to row 12)

**Filed:** 2026-08-08 · **For:** the Arabic composition of any England/UK-schools piece, and any future British byline; also records the wave-completion milestone. Hangs off the England/Ofsted source index (row 12, filed 2026-07-28) and the composition family **#28b**. No new numbered ruling.

## 1. The England AR is composed — the Ed04 Arabic wave is complete (8 of 8)

`england-report-cards-first-term` composed in Arabic today (`content-drafts/staged-ed0304/articles-ar/2026-07-28-england-report-cards-first-term.md`, `approved: false`). This is the **eighth and last** owed AR of the Ed04 wave; the AR-composition path — the binding parallel constraint since the drafted slate went verification-complete (2026-07-29) — is now **closed**. All eight Ed04 pieces exist EN+AR.

**Placement note (important, mirrors England's held posture):** England EN is the one Ed04 piece held **entirely out of the build path** — it lives in `content-drafts/staged-ed0304/articles/`, not `web/src/content/articles/` (staged double-safe since 07-28). So England AR was placed the same way — **staging only, NOT `web/src/content/articles-ar/`**. The other seven Ed04 pieces have both surfaces in the build path held `approved:false`; England has neither in the build path. Placing England AR in the build path would have created an orphan (an AR file whose `englishVersion:` target is absent from the build) and broken parity. The build stays 37 EN / 37 AR / 30 published each; England joins the build only at the wave gate, when both surfaces move in together.

## 2. Name-routing — the British Anglo byline, and the one non-Anglo surname

Nine named humans in the England piece; all route CONFIRMED-by-convention (per #28b — standard Arabic-media Anglo forms, none "unheard," none PROVISIONAL). The convention worth banking: **a British public-life byline is an Anglo byline routed phonetically, with two watch-points.**

| Name | AR | Note |
|---|---|---|
| Ruth Perry | روث بيري | the orienting one-sentence reference only (frame-sibling fence with Oman, per row 12) |
| Frank Coffield | فرانك كوفيلد | `-ield` → ‑يلد |
| Peter Tymms | بيتر تِمز | **watch-point A:** `y` as short /ɪ/ (not a diphthong) → تِمز, never تايمز |
| Christine Pascal | كريستين باسكال | |
| Frank Norris | فرانك نوريس | |
| Colin Richards | كولن ريتشاردز | |
| **Saini J** (Mr Justice) | القاضي سايني | **watch-point B:** a Sikh/Punjabi-origin surname on a British bench — route by its **own** origin (Saini = /ˈsaɪni/), same principle as Chile's Gino (route each part by its origin, not the jurisdiction's). "Mr Justice" → «القاضي», the judicial courtesy title, not transliterated |
| Paul Whiteman | بول وايتمان | `White‑` → وايت (the diphthong England's own /aɪ/ **is** here — contrast Tymms) |
| Lee Owston | لي أوستون | sources only (the "national director" in the body is unnamed, as in EN) |

**The two watch-points are the whole lesson:** English `y`/`i`/`ei`/`igh` do not map one-to-one to Arabic — *Tymms* is تِمز (short) while *Whiteman* is وايت (diphthong) in the same article. Route by **heard vowel**, not by letter. And a non-Anglo surname on a British institution (Saini) routes by its origin language, extending the Chile/Singapore multi-origin principle to the UK.

## 3. Institutions — Latin tag + Arabic gloss, per #28a
Ofsted → أوفستد (Latin-tagged first mention); NAHT, DfE, IFF Research, EIF each keep the Latin acronym + a one-time Arabic gloss (الرابطة الوطنية لمديري المدارس / وزارة التعليم / …). The five grade bands are glossed as Arabic phrases (تحسينٌ عاجل / يحتاج انتباهًا / المستوى المتوقَّع / مستوًى قوي / استثنائي) and the old four-word scale glossed with its Latin original in italics on first use — never map "exceptional = outstanding" (row 12: the bands are not the old scale renamed). "secure fit" → «المطابقة المُحكَمة» (Latin-tagged), because the rule's name is load-bearing.

## 4. What remains before Ed04 can ship (AR is no longer on the list)
With AR closed, the binding constraint is now three items, all downstream of composition: **(1)** the 10 hero stills (Designer batch — none on disk yet; the standing gap); **(2)** the `web/src/lib/editions.ts` Ed04 registry entry (second gate); **(3)** the wave publish-gate in writing → flip all 16 files (8 EN + 8 AR) `approved: true` in one wave → push. Distribution (Substack announce) still waits on the two founder-gated items (custom domain, Substack account), neither of which blocks the site.

— Researcher → team · Section 1 row 12 addendum (+INDEX). Ruling series unchanged at #1–#28.
