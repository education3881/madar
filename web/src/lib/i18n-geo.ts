/**
 * Arabic display names for the schema's controlled English vocabularies.
 *
 * WHY THIS MODULE EXISTS (2026-08-23)
 * -----------------------------------
 * `content.config.ts` is ONE schema shared by both collections, so an Arabic
 * article's `country`, `region`, `level` and `themes` are stored in English —
 * `country: Sierra Leone`, `region: Africa`, `level: K-12`,
 * `themes: [value of teachers]`. That is correct as *data*: one controlled
 * vocabulary, one enum, one set of tags, comparable across both corpora, and
 * it must stay that way.
 *
 * It was NOT correct as *display*. From the first publish on 2026-05-25 until
 * today, every Arabic page printed those raw English values to an Arabic
 * reader — in the byline block, in the marginalia field «المرجع الميداني»,
 * in the related-reading meta, on the AR home page and the AR editions index,
 * and as the `<category>` of every item in the Arabic RSS feed.
 *
 * The sharpest instance, and the reason a sweep never caught it:
 *
 *     <span class="piece__country" lang="ar" dir="rtl">{piece.data.country}</span>
 *
 * The markup ASSERTS the content is Arabic and then puts Latin text inside it.
 * Every check we own passed: parity counted 38 AR files against 38 EN files,
 * the pages built, the links resolved, `lang`/`dir` were present and correct.
 * None of them read the words. Parity counted files, not language.
 *
 * So the fix is a display layer, not a data change: the schema is untouched,
 * no article file is edited, the English side renders exactly as before, and
 * there is one place to correct a rendering.
 *
 * FAIL-LOUD, NOT FAIL-QUIET. An unmapped key returns the English string —
 * a new country must still render *something* rather than break a build — but
 * `missingArabicGeoKeys()` reports every key that fell through, and the QA
 * sweep fails on a non-empty result. A silent English fallback is exactly the
 * defect this module was written to end, so it is never allowed to be silent.
 * (Cf. the 2026-08-16 rule: an assertion that finds nothing to check has
 * failed, not passed — so the sweep asserts the maps are COMPLETE, not merely
 * that they did not throw.)
 */

/** Country → Arabic. Keys are the exact `country:` values used in frontmatter. */
export const COUNTRY_AR: Record<string, string> = {
  Australia: 'أستراليا',
  Bahrain: 'البحرين',
  Bangladesh: 'بنغلاديش',
  Brazil: 'البرازيل',
  Chad: 'تشاد',
  Chile: 'تشيلي',
  Egypt: 'مصر',
  Ghana: 'غانا',
  India: 'الهند',
  Indonesia: 'إندونيسيا',
  Iraq: 'العراق',
  Kenya: 'كينيا',
  Kuwait: 'الكويت',
  Lebanon: 'لبنان',
  Morocco: 'المغرب',
  Netherlands: 'هولندا',
  'New Zealand': 'نيوزيلندا',
  Oman: 'عُمان',
  Palestine: 'فلسطين',
  Philippines: 'الفلبّين',
  Poland: 'بولندا',
  Qatar: 'قطر',
  'Sierra Leone': 'سيراليون',
  Singapore: 'سنغافورة',
  'South Korea': 'كوريا الجنوبية',
  Sudan: 'السودان',
  Syria: 'سوريا',
  // Endonym, per the state's own 2022 request to the UN; the Arabic register
  // has always used تركيا, which is unaffected by the Latin-script change.
  'Türkiye': 'تركيا',
  Ukraine: 'أوكرانيا',
  'United Arab Emirates': 'الإمارات العربية المتحدة',
  'United Kingdom': 'المملكة المتحدة',
  'United States': 'الولايات المتحدة',
  Uruguay: 'الأوروغواي',
  Vietnam: 'فيتنام',
  Yemen: 'اليمن',

  // Reconned for Edition 05 and not yet shipped — mapped ahead of the piece so
  // the first Arabic composition never lands on an English fallback.
  Zambia: 'زامبيا',
  Namibia: 'ناميبيا',
  Botswana: 'بوتسوانا',
  'South Africa': 'جنوب أفريقيا',
  Rwanda: 'رواندا',
  Nigeria: 'نيجيريا',
  Ethiopia: 'إثيوبيا',
  Tanzania: 'تنزانيا',
  Senegal: 'السنغال',
  Benin: 'بنين',
  Niger: 'النيجر',
  'Burkina Faso': 'بوركينا فاسو',
  Mauritius: 'موريشيوس',
  Seychelles: 'سيشل',
  Tunisia: 'تونس',
  Jordan: 'الأردن',
  'Saudi Arabia': 'السعودية',
};

/** Region enum → Arabic. Mirrors the `region` enum in content.config.ts exactly. */
export const REGION_AR: Record<string, string> = {
  MENA: 'الشرق الأوسط وشمال أفريقيا',
  Africa: 'أفريقيا',
  Asia: 'آسيا',
  'LatAm-Caribbean': 'أمريكا اللاتينية والكاريبي',
  Europe: 'أوروبا',
  'N-America': 'أمريكا الشمالية',
  Oceania: 'أوقيانوسيا',
  Other: 'أخرى',
};

/**
 * Level enum → Arabic.
 * «التعليم العام» is the register's standing rendering for K-12 and is used
 * across the published Arabic corpus; it is not a coinage introduced here.
 */
export const LEVEL_AR: Record<string, string> = {
  ECE: 'الطفولة المبكّرة',
  'K-12': 'التعليم العام',
  Both: 'المرحلتان معًا',
};

/** Theme tag → Arabic. Keys are the exact free-form tags used in frontmatter. */
export const THEME_AR: Record<string, string> = {
  'AI-readiness': 'الجاهزية للذكاء الاصطناعي',
  'ECE access': 'إتاحة الطفولة المبكّرة',
  access: 'الإتاحة',
  curriculum: 'المناهج',
  'education for displaced children': 'تعليم الأطفال النازحين',
  'female education': 'تعليم الفتيات',
  'government-led programs': 'برامج تقودها الحكومات',
  'inspiring stories': 'قصص مُلهِمة',
  'language and heritage preservation': 'صون اللغة والتراث',
  'national identity': 'الهوية الوطنية',
  'parent-led projects': 'مبادرات يقودها الأهل',
  'student wellbeing': 'عافية الطلبة',
  sustainability: 'الاستدامة',
  'value of teachers': 'قيمة المعلِّم',
};

/** Keys that fell through to the English fallback during this render pass. */
const missing = new Set<string>();

function lookup(map: Record<string, string>, key: string, kind: string): string {
  const hit = map[key];
  if (hit === undefined) {
    missing.add(`${kind}:${key}`);
    return key;
  }
  return hit;
}

export const countryAr = (v: string) => lookup(COUNTRY_AR, v, 'country');
export const regionAr = (v: string) => lookup(REGION_AR, v, 'region');
export const levelAr = (v: string) => lookup(LEVEL_AR, v, 'level');
export const themeAr = (v: string) => lookup(THEME_AR, v, 'theme');

/** Every unmapped key seen so far. The QA sweep fails on a non-empty array. */
export const missingArabicGeoKeys = (): string[] => [...missing].sort();

/**
 * Right-to-left mark (U+200F).
 *
 * Needed where Arabic text is handed to a consumer that supplies its own base
 * direction and accepts no markup — specifically RSS `<title>`, which is plain
 * text by spec. In an LTR base paragraph a trailing «.» or a run of digits
 * ("12,348", "2026") resolves to the wrong side of an Arabic string. An RLM
 * prefix sets the paragraph's base direction to RTL for the whole value, which
 * is the only lever a markup-free field gives us.
 */
export const RLM = '‏';

/** Prefix an Arabic plain-text value with RLM unless it already carries one. */
export const rtlText = (v: string) => (v.startsWith(RLM) ? v : RLM + v);
