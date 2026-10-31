/**
 * Edition registry — the canonical metadata for each monthly issue of Madār.
 *
 * Articles carry an `edition` number in their frontmatter; this file holds the
 * editorial framing (period, theme) and the visual identity (ground wash,
 * accent, motif) that the /editions/ pages render. Keep article body pages
 * untouched — this is presentation metadata only.
 */

export interface Edition {
  number: number;
  periodEn: string;
  periodAr: string;
  themeEn: string;
  themeAr: string;
  /** Subtle background wash for the edition block. */
  ground: string;
  /** Accent colour for the numeral, kickers and rule. */
  accent: string;
  /** Motif key — 'horizon' (macron-style rule), 'thread' (two joined nodes), or
   *  'throughline' (a continuous rule absorbing a shock). */
  motif: string;
  /** Cover SVG filename under /public/covers/ — inlined onto pages. */
  cover: string;
  status: 'current' | 'closed';
}

// AR: signed off by the Arabic Editor 2026-06-14. Rulings: "placement" → «التوزيع»
// (deployment/matching), not «الإسناد» (which reads as attribution); «البيداغوجيا»
// retained for consistency with the shipped Husseiny caption; the page uses «إصدار»
// throughout (never «عدد»), per the founder's Editions/الإصدارات naming choice.
export const editions: Edition[] = [
  {
    number: 1,
    periodEn: 'May 2026',
    periodAr: 'مايو ٢٠٢٦',
    themeEn: 'The founding survey — systems across the map, two languages, one question.',
    themeAr: 'المسح التأسيسي — أنظمةٌ من مختلف البلدان، بلغتين، وسؤالٌ واحد.',
    ground: '#E8E2D0',
    accent: '#D94F2A',
    motif: 'horizon',
    cover: 'edition-01.svg',
    status: 'closed',
  },
  {
    number: 2,
    periodEn: 'June 2026',
    periodAr: 'يونيو ٢٠٢٦',
    themeEn: 'The instrument in use — pedagogy and deployment, measured.',
    themeAr: 'الأداة في الاستخدام — البيداغوجيا والتوزيع، بالقياس.',
    ground: '#FAFAF7',
    accent: '#2F6F6A',
    motif: 'thread',
    cover: 'edition-02.svg',
    status: 'closed',
  },
  {
    number: 3,
    periodEn: 'July 2026',
    periodAr: 'يوليو ٢٠٢٦',
    themeEn: 'Continuity under disruption — how school systems keep their promises through war, disaster and collapse.',
    themeAr: 'الاستمرارية رغم الاضطراب — كيف تُبقي الأنظمةُ التعليميةُ مدارسَها عاملةً في الحرب والكارثة والانهيار.',
    ground: '#EAEEF1',
    accent: '#2E4C63',
    motif: 'throughline',
    cover: 'edition-03.svg',
    status: 'closed',
  },
  {
    number: 4,
    periodEn: 'August 2026',
    periodAr: 'أغسطس ٢٠٢٦',
    themeEn: 'The measurement question — what a score actually measures, and who defines, moves and defends the thresholds that turn a child’s work into a label.',
    themeAr: 'سؤال القياس — ماذا تقيس الدرجةُ فعلًا، ومَن يحدِّد العتباتِ التي تحوِّل عملَ الطفل إلى تصنيف، ومَن يحرِّكها ومَن يدافع عنها.',
    ground: '#E9E5DB',
    accent: '#9C5B3A',
    motif: 'horizon',
    cover: 'edition-04.svg',
    status: 'closed',
  },
  // Ed05: the period label names the month the issue reaches readers, not the
  // span of its datelines — the convention every row above already follows
  // (Ed04 is 'August 2026' over pieces dated 07-07 to 07-28). This wave's six
  // pieces are dated 2026-08-25 to 2026-09-27 and ship in October; there was no
  // September edition, and the gap is honest rather than hidden.
  {
    number: 5,
    periodEn: 'October 2026',
    periodAr: 'أكتوبر ٢٠٢٦',
    themeEn: 'Africa entire — six systems, each read on the instrument it chose for itself.',
    themeAr: 'أفريقيا بأكملها — ستةُ أنظمة، كلٌّ منها يُقرأ بالأداةِ التي اختارها لنفسه.',
    ground: '#E4E8DF',
    accent: '#2D6A4F',
    motif: 'thread',
    cover: 'edition-05.svg',
    // CLOSED 2026-10-31. It was closed on 2026-10-13 - twelve flags in one
    // commit - and `content-drafts/_EDITION_05_STATUS.md` has said so in its
    // first line ever since, while this field went on saying 'current' for
    // eighteen days and the home pages printed the kicker "Current edition"
    // over it in both languages. Two files in this repository disagreed about
    // one fact and the served bytes carried the wrong one. Standing-queue item
    // 45 named the PERIOD LABEL going stale on 2026-11-01 as the defect; the
    // label is the issue's name and names do not expire (Ed04 is 'August 2026'
    // over pieces dated July). The defect was this flag, and it was already
    // served. What is NOT decided here, and is not ours, is what the next
    // edition is: GitHub issue #13, stated default 2026-11-08.
    status: 'closed',
  },
];

/**
 * Whether any edition is actually open. False from 2026-10-31: Edition 05
 * closed on 2026-10-13 and nothing has been commissioned to follow it (issue
 * #13). Consumers must not print the word "current" over the fallback.
 */
export const hasOpenEdition: boolean = editions.some((e) => e.status === 'current');

/**
 * The edition to feature. The one marked 'current' if there is one, otherwise
 * the highest-numbered - which is the LATEST edition and not the current one.
 * Read `hasOpenEdition` before labelling it.
 */
export const currentEdition: Edition =
  editions.find((e) => e.status === 'current') ??
  editions.reduce((a, b) => (b.number > a.number ? b : a));

/** Look up an edition by its number. */
export function getEdition(n: number): Edition | undefined {
  return editions.find((e) => e.number === n);
}
