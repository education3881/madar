# Public-copy patches — 2026-05-25 (Editor → Web Developer)

Vini has made a hard rule today: the publication's country list and exclusions are **internal editorial discipline** and never appear in public-facing copy. No enumeration, no list-by-negation, no "places others don't look", no "underrepresented geographies". The full rule lives in `/docs/40_voice_and_style.md` under *The geography rule — internal only*.

The following live pages and copy strings violate the rule. Please apply the patches below as a single batch, then rebuild. The About page is also being rewritten in parallel — patch [5] points to the new source. After applying these, please grep the codebase one more time for any of: *underrepresented*, *places others*, *don't look*, *twelve countries*, *not in scope*, *underprivileged*, *sub-Saharan Africa, the Levant*, and ping me if anything remains.

---

## [1] Home tagline — English

**File:** `/web/src/pages/index.astro`
**Line ~89 (inside `.masthead__tagline`)**

**Old:**
```
Education, from the places others don't look
```

**New:**
```
Education, written slowly, in two languages
```

**Reason:** "From the places others don't look" is a list-by-negation — it tells the reader, in fewer words, exactly the kind of manifesto statement Vini wants out of public copy. The replacement says what the publication *does* (writes slowly, in two languages, about education), not what others fail to do. It also pairs cleanly with the Arabic line we're replacing it with in patch [2].

---

## [2] Home tagline — Arabic

**File:** `/web/src/pages/index.astro`
**Line ~90 (`.masthead__tagline-ar`)**

**Old:**
```
التعليم من الأماكن التي لا يُنظر إليها
```

**New:**
```
التعليم، بتأنٍّ، بلغتين
```

**Reason:** Direct parallel to patch [1]. *بتأنٍّ* — "with deliberateness / unhurriedly" — carries the slowness without straining; *بلغتين* — "in two languages" — names the bilingual register. The Arabic register stays close to the English, neither more decorative nor more apologetic, and the manifesto move ("the places not looked at") is removed.

---

## [3] Arabic home page — masthead tagline + page `<title>`

**File:** `/web/src/pages/ar/index.astro`

**(a) Line ~54 — Base `title=`**

**Old:**
```
مدار — التعليم من الأماكن التي لا يُنظر إليها
```

**New:**
```
مدار — التعليم، بتأنٍّ، بلغتين
```

**(b) Line ~86 — inside `.masthead__tagline`**

**Old:**
```
التعليم من الأماكن التي لا يُنظر إليها
```

**New:**
```
التعليم، بتأنٍّ، بلغتين
```

**Reason:** Same violation as [1] and [2], in the Arabic entry point and the `<title>` element. The `<title>` is doubly important because it appears in search-engine snippets and browser tabs — i.e. public-facing surface area.

---

## [4] Site meta description (Base layout default)

**File:** `/web/src/layouts/Base.astro`
**Line 20 (default value of `description`)**

**Old:**
```
description = 'An editorial publication on education, from underrepresented geographies.',
```

**New:**
```
description = 'An editorial publication on early childhood and K-12 education, written and made in English and Arabic.',
```

**Reason:** *Underrepresented* is the worst single offender — it is NGO-frame language *and* implies a list-by-negation. The replacement names the subject (early childhood and K-12 education) and the publication's bilingual register, without smuggling a scope enumeration in. This default propagates across every page that doesn't pass its own `description`.

---

## [5] About page body — full rewrite

**File:** `/web/src/pages/about.astro`
**Lines ~20–155 (the entire `.about-page__body` content)**

**Action:** Replace the embedded About body with the new draft now living at `/content-drafts/about-page.md`.

The new About:
- Drops the *Where we look* section in full.
- Drops the twelve-country enumeration.
- Drops the explicit Iran / Israel / Yemen exclusions paragraph.
- Replaces *Where we look* with *How we choose what to cover*, framed in terms of editorial posture (texture, slowness, dignity, bilingual logic) rather than geography.
- Keeps the *How we write* conventions section essentially intact.
- Keeps the *What we refuse* register-list (lightly tightened — *underrepresented* is now refused alongside *voices* and *beneficiaries*).
- Keeps the Arabic closing line *نكتب من مدار واحد بلغتين، ولكلٍ منهما وزنها الخاص*.

Also, on line ~127, the existing About body contains `<em>underrepresented</em>` as part of the refusals list. That instance is deliberate (we are *refusing* the word). In the new draft it is restated as part of a tightened sentence — please match the new draft exactly, do not preserve the old paragraph.

**Headline tags to update with this rewrite:**

- Page `<h2>Where we look <span class="ar-pair" lang="ar" dir="rtl">· أين ننظر</span></h2>` is **removed** in full.
- New `<h2>How we choose what to cover</h2>` replaces it.

**Reason:** This is the biggest single violation in the codebase. The current About page does exactly what Vini has now forbidden — it enumerates the twelve MENA countries, names Iran / Israel / Yemen exclusions head-on, and reads as a manifesto of inclusion-and-exclusion. The new draft holds the publication's posture without naming a single country in its scope discussion.

---

## [6] Home About mini-block — English

**File:** `/web/src/pages/index.astro`
**Lines ~172–179 (inside `.about__col.en`)**

**Old:**
```
Madār is a slow-cadence editorial publication on education in geographies
the international press tends to look past — sub-Saharan Africa, the
Levant, North Africa, Latin America, the small island states. We publish
two kinds of pieces: <em>field notes</em> we report ourselves, and
<em>curated readings</em> of one carefully-chosen source from somewhere
worth listening to. Two to three pieces an issue. One issue a month.
A research instrument, not a magazine.
```

**New:**
```
Madār is a slow-cadence editorial publication on early childhood and
K-12 education, written in English and Arabic. We publish two kinds of
pieces: <em>field notes</em> we report ourselves, and <em>curated
readings</em> of one carefully-chosen source worth listening to. Two
to three pieces an issue. One issue a month. A research instrument,
not a magazine.
```

**Reason:** The original enumerates a regional list — *sub-Saharan Africa, the Levant, North Africa, Latin America, the small island states* — and frames it as "geographies the international press tends to look past", which is list-by-negation. Both moves violate the rule. The replacement names the subject (early childhood and K-12 education) and the bilingual register, drops the enumeration, and preserves the rest of the paragraph (field notes / curated readings / cadence / research instrument) intact.

---

## [7] Home About mini-block — Arabic

**File:** `/web/src/pages/index.astro`
**Lines ~187–192 (inside `.about__col.ar`)**

**Old:**
```
«مدار» مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تَتناولُ التعليمَ في جغرافياتٍ
لا تَلتفتُ إليها الصحافةُ الدوليّةُ كثيراً — أفريقيا جنوبَ الصحراء،
المشرقُ العربيّ، شمالُ أفريقيا، أمريكا اللاتينيّة، والدولُ الجَزَريّةُ
الصغرى. نَنشرُ نوعَين من المواد: <em>تقاريرَ ميدانيّة</em> نَكتبُها
بأنفسنا، و<em>قراءاتٍ مختاَرة</em> لمصدرٍ واحدٍ يَستحقّ الإصغاء.
قطعتان أو ثلاث في كلّ عدد. عددٌ واحدٌ كلّ شهر. أداةُ بحثٍ، لا مجلّةً.
```

**New:**
```
«مدار» مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تَتناولُ التعليمَ في مرحلتَيِ
الطفولةِ المبكّرةِ والتعليمِ العامّ، تَصدرُ بالعربيّةِ والإنجليزيّة.
نَنشرُ نوعَين من المواد: <em>تقاريرَ ميدانيّة</em> نَكتبُها بأنفسنا،
و<em>قراءاتٍ مختاَرة</em> لمصدرٍ واحدٍ يَستحقّ الإصغاء. قطعتان أو ثلاث
في كلّ عدد. عددٌ واحدٌ كلّ شهر. أداةُ بحثٍ، لا مجلّةً.
```

**Reason:** Direct Arabic parallel to patch [6]. Drops the enumeration of sub-regions, replaces it with the subject (early childhood + K-12) and the bilingual register, keeps everything else intact.

---

## [8] Arabic home About mini-block

**File:** `/web/src/pages/ar/index.astro`
**Lines ~156–162 (inside `.about__body`)**

**Old:**
```
«مدار» مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تَتناولُ التعليمَ في جغرافياتٍ لا تَلتفتُ
إليها الصحافةُ الدوليّةُ كثيراً — أفريقيا جنوبَ الصحراء، المشرقُ العربيّ، شمالُ
أفريقيا، أمريكا اللاتينيّة، والدولُ الجَزَريّةُ الصغرى. ننشرُ نوعَين من المواد:
<em>تقاريرَ ميدانيّة</em> نَكتبُها بأنفسنا، و<em>قراءاتٍ مختاَرة</em> لمصدرٍ
واحدٍ يَستحقّ الإصغاء. أداةُ بحثٍ، لا مجلّةً.
```

**New:**
```
«مدار» مجلّةٌ تحريريّةٌ بطيئةُ الإيقاع تَتناولُ التعليمَ في مرحلتَيِ الطفولةِ
المبكّرةِ والتعليمِ العامّ، تَصدرُ بالعربيّةِ والإنجليزيّة. ننشرُ نوعَين من
المواد: <em>تقاريرَ ميدانيّة</em> نَكتبُها بأنفسنا، و<em>قراءاتٍ مختاَرة</em>
لمصدرٍ واحدٍ يَستحقّ الإصغاء. أداةُ بحثٍ، لا مجلّةً.
```

**Reason:** Same as [7]. The Arabic entry point's About block carries the same violation as the English home's.

---

## [9] package.json description

**File:** `/web/package.json`
**Line 6**

**Old:**
```
"description": "Editorial publication on education from underrepresented geographies.",
```

**New:**
```
"description": "Editorial publication on early childhood and K-12 education, in English and Arabic.",
```

**Reason:** Mostly invisible to readers, but it leaks into npm metadata and into any scaffolding that reads package.json. Same offending word (*underrepresented*) as patch [4]; same fix.

---

## After applying

Please rebuild and ping me when the build is clean. I'd like to do a final pass on the rendered About page to make sure the new draft reads as well in the page's typography as it does in the markdown. Also please rerun the codebase grep listed at the top of this file — I'd rather find any remaining violation now than discover it later in a press email.

— Editor
