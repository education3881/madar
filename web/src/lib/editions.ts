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
  /** Motif key — 'horizon' (macron-style rule) or 'thread' (two joined nodes). */
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
    status: 'current',
  },
];

/** The edition currently marked 'current' (falls back to the highest number). */
export const currentEdition: Edition =
  editions.find((e) => e.status === 'current') ??
  editions.reduce((a, b) => (b.number > a.number ? b : a));

/** Look up an edition by its number. */
export function getEdition(n: number): Edition | undefined {
  return editions.find((e) => e.number === n);
}
