/**
 * scriptRuns — split a mixed-script string into runs so each can be marked
 * with the language it is actually written in.
 *
 * ---------------------------------------------------------------------------
 * WHY THIS EXISTS (Quality, 2026-08-25 — the assistive-technology surface)
 *
 * The consumer question, aimed for the first time at a reader using a screen
 * reader. A screen reader picks its voice and its pronunciation rules from the
 * nearest `lang` in the accessibility tree, and it does not look at the script
 * of the characters. Arabic text sitting inside a page that declares
 * `lang="en"` is therefore read out with an English voice — which does not
 * produce accented Arabic, it produces noise.
 *
 * The site was already careful about this in the one place someone thought
 * about it: the wordmark carries `lang="ar" dir="rtl"` in both the header and
 * the footer. The still's colophon did not. Every English article page prints
 *
 *     سكون · The Still · Curated NN · Country
 *
 * in a single span with no `lang` at all — 38 pages, live since the first
 * publish on 25 May. `سكون` (sukūn — stillness) is the name of the form, and
 * it is the one word in the caption a reader would most want to hear said.
 *
 * WHY A SPLITTER AND NOT A `lang` ON THE SPAN
 *
 * The caption is genuinely bilingual: one Arabic word, then Latin. Marking the
 * whole span `ar` would fix the Arabic and break the English. `lang` describes
 * a run of text, not a box, so the honest markup is one element per run.
 *
 * SCOPE — deliberately narrow. This is for CHROME strings we compose (the
 * colophon), not for article prose. Under ruling #33's corollary the Latin
 * script inside Arabic body text and source titles is correct as written — an
 * institution keeps its own name — and re-marking prose runs would be a
 * cosmetic rewrite of copy the Arabic Editor approved.
 * ---------------------------------------------------------------------------
 */

export type ScriptRun = { text: string; script: 'arabic' | 'other' };

/** Arabic, Arabic Supplement, Extended-A, and the Arabic presentation forms. */
const ARABIC = /[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]/;

/**
 * Split on script boundaries, keeping neutral characters (spaces, the middot
 * separator, digits, punctuation) attached to the run they follow — so
 * "سكون · The Still" yields "سكون " and "· The Still" rather than three runs
 * with a homeless separator between them.
 */
export function splitScriptRuns(input: string): ScriptRun[] {
  const runs: ScriptRun[] = [];
  if (!input) return runs;

  for (const ch of input) {
    const script: ScriptRun['script'] = ARABIC.test(ch) ? 'arabic' : 'other';
    const neutral = !/\p{L}/u.test(ch);
    const last = runs[runs.length - 1];

    if (last && (neutral || last.script === script)) {
      last.text += ch;
      continue;
    }
    runs.push({ text: ch, script });
  }

  // A neutral-only tail (" · 2026") belongs with what preceded it, which the
  // loop already does. Drop any run that ended up empty.
  return runs.filter((r) => r.text.length > 0);
}
