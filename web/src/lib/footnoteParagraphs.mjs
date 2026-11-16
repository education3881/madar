/**
 * footnoteParagraphs — mark a paragraph that IS an emphasised run, so the
 * stylesheet stops guessing at it with `:only-child`.
 *
 * WHY THIS EXISTS (2026-11-16, standing-queue item 118, ruling #146).
 *
 * Both article templates carry a footnote rule written as
 *
 *     .body-main p > em:only-child { display:block; font-size:…; color:muted; … }
 *
 * whose intent is the dagger note at the foot of a piece: a paragraph the
 * drafter wrote as `*† Names marked with a dagger are…*`, i.e. a paragraph that
 * is ENTIRELY one emphasised run. The rule has been in both templates since the
 * templates were written.
 *
 * `:only-child` CANNOT EXPRESS THAT, because it counts ELEMENT children and
 * ignores text nodes. So
 *
 *     <p><em>† Names marked…</em></p>                        ← intended
 *     <p>Tuition in Vietnam — <em>học phí</em> — is a…</p>    ← an accident
 *
 * are the same selector. Measured over the served corpus on 2026-11-16: 166
 * matches, of which **79 are intended footnotes and 87 are inline phrases in
 * running prose**, across 41 article pages, 50 English and 37 Arabic. Verified
 * in a browser rather than inferred: each of the 87 is served `display: block`
 * at 10.5px (English) or 15px (Arabic) against body size, in muted grey, with a
 * 25.5px margin opening mid-sentence. An inline foreign-language phrase was
 * being rendered as a block-level footnote in the middle of a paragraph.
 *
 * It catches Arabic phrases as readily as Latin ones, so it is not a script
 * question and never was — which is what separates it from ruling #115, whose
 * enforcement was over-broad in the other direction (a page standing in for a
 * script, standing-queue item 107).
 *
 * THE BOUNDARY IS EXACT AND THE ARTEFACT SUPPLIES IT: does the `<em>`'s own
 * text account for the whole paragraph? That is a comparison between an
 * element's text and its parent's, which **CSS cannot make** — it has no
 * text-node selector and no content comparison — and which the BUILD can make
 * trivially. So the guess moves out of the stylesheet and into the pipeline,
 * and the stylesheet is handed a class that means what the rule meant all
 * along. Same shape as #113's acronym boundary and #114's digit boundary: when
 * a check or a rule needs a distinction it cannot hold, look for the boundary
 * the artefact already states rather than sharpening the guess.
 *
 * No dependency: the hast tree is walked by hand rather than through
 * `unist-util-visit`, because this repository's tools take no third-party
 * imports and a plugin is not a reason to start.
 */

/* The text beside the run may be FURNITURE but never PROSE, and the boundary
   is exact: furniture carries no letter and no digit. The corpus's sign-off is
   written `— *The Editors*`, and an em dash is not prose — the first draft of
   this plugin demanded the <em> account for every character of the paragraph,
   missed that line on all 45 English pieces, and `qa_render` failed the build
   on a 130-row blank band where the sign-off had been. The gate found it before
   it could be believed: a boundary drawn one character too tight reads exactly
   like a boundary drawn right. */
const PROSE = /[\p{L}\p{N}]/u;

/** A paragraph qualifies when its only prose content is one <em>. */
function isWhollyEmphasised(node) {
  let em = null;
  for (const child of node.children || []) {
    if (child.type === 'text') {
      if (PROSE.test(child.value)) return null; // prose beside the run
      continue;
    }
    if (child.type === 'comment') continue;
    if (child.type !== 'element') return null;
    if (child.tagName !== 'em') return null; // a link, a <strong>, an <img>
    if (em) return null; // two emphasised runs is prose, not a footnote
    em = child;
  }
  return em;
}

function walk(node, onParagraph) {
  if (!node || !node.children) return;
  for (const child of node.children) {
    if (child.type === 'element' && child.tagName === 'p') {
      onParagraph(child);
    }
    walk(child, onParagraph);
  }
}

export function footnoteParagraphs() {
  return function transformer(tree) {
    walk(tree, (p) => {
      if (!isWhollyEmphasised(p)) return;
      p.properties = p.properties || {};
      const existing = p.properties.className;
      const classes = Array.isArray(existing)
        ? existing
        : typeof existing === 'string' && existing
          ? existing.split(/\s+/)
          : [];
      if (!classes.includes('footnote-para')) classes.push('footnote-para');
      p.properties.className = classes;
    });
  };
}

export default footnoteParagraphs;
