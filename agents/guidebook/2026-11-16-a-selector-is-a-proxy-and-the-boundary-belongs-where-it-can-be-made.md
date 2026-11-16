# Ruling #146 — a selector is a PROXY for an authorial category, and the boundary belongs in the layer that can make it

**Filed:** 2026-11-16, by the quality function, raising and closing standing-queue item 118.
**Family:** Assertion discipline (member **fifty-nine**).

## The rule

**When a rule's selector is a proxy for an authorial category, the rule is wrong on exactly the
difference between them — and if the distinguishing boundary is a comparison the enforcing layer cannot
make, the boundary must MOVE to a layer that can. Sharpening the proxy is not available.**

## The defect

Both article templates carried
`.body-main p > em:only-child { display:block; font-size:…; color:muted; margin-block-start:… }`. Its
intent is the dagger note a drafter writes as `*† Names marked with a dagger are…*` — **a paragraph that
IS one emphasised run.**

**`:only-child` counts ELEMENT children and ignores TEXT nodes.** So these are the same selector:

```html
<p><em>† Names marked with a dagger are…</em></p>              ← intended
<p>Tuition in Vietnam — <em>học phí</em> — is a monthly…</p>    ← an accident
```

Measured over every served article body: **166 matches — 79 intended footnotes and 87 inline phrases in
running prose**, 50 English and 37 Arabic, across **41 pages**. **Verified in a browser rather than
inferred:** each of the 87 is served `display: block` at **10.5px against a 19px body** (15px on
Arabic), in `rgba(14,27,44,0.62)` instead of ink, with a **25.5px margin opening mid-sentence**. An
inline foreign-language phrase rendered as a block-level muted footnote in the middle of a paragraph,
since the templates were written.

**It catches Arabic phrases as readily as Latin ones, so it is not a script question and never was** —
which is what separates it from #145, found in the same hour. #145's selector was wider than its
**fact**; this one is wider than its **intent**. Opposite directions, one shape.

## The repair, and why it is not a sharper selector

The boundary is exact and the artefact supplies it: **does the run's own text account for the whole
paragraph?** That compares an element's text with its parent's — **CSS has no text-node selector and no
content comparison, so it cannot make that comparison at all.** The build can make it trivially. So the
guess moved out of the stylesheet and into the pipeline: `web/src/lib/footnoteParagraphs.mjs`, a rehype
plugin with no dependency, marks `p.footnote-para`, and both templates re-key to
`p.footnote-para > em`.

Same shape as #113's acronym boundary and #114's digit boundary: *when a rule or a check needs a
distinction it cannot hold, look for the boundary the artefact already states rather than sharpening the
guess.* This adds the layer clause — **the artefact may state the boundary in a vocabulary the enforcing
layer does not speak, and then the work is a translation and not a refinement.**

## Two findings from the proof, both worth more than they cost

**1 · A boundary drawn one character too tight reads exactly like a boundary drawn right.** The first
draft demanded the `<em>` account for *every character* of the paragraph. The corpus's sign-off is
written `— *The Editors*`, and **an em dash is furniture, not prose** — so the sign-off lost its footnote
styling on all 45 English pieces and `qa_render` failed the build on a 130-row blank band. Widened to
*no letter and no digit outside the run* (`/[\p{L}\p{N}]/u`). Only a gate that looks at the **raster**
could tell the two boundaries apart. *(And that gate was itself wrong in a way this run then had to fix
— see #147.)*

**2 · A build cache can report on a pipeline change it never ran.** The rebuild after widening reported
**the same 33 marked pages** as the build before it: the predicate was right and **Astro's content cache
had served the previous build's markdown output, because a rehype-plugin change does not invalidate
it.** The correct fix read as a failed one. `rm -rf node_modules/.astro .astro dist` → 33 → **49**. The
hazard is general: every gate in `postbuild` reads `dist`, and `dist` can be a faithful report on a tree
the build did not process. **CI is safe only because it checks out clean — so the condition is invisible
exactly where runs are developed.** Queue item 120; same family as item 112, *an instrument reading a
tree the repository does not yet describe.*

## Proved

Two independent boundaries agree exactly: 166 → **79 marked / 87 not**, the same split a classifier
written before the plugin returned. **Bite cleared** — `Lan fɔ lan.` → `display:inline`, 19px, *italic*,
ink, zero margin. **Control held** — the genuine footnotes and both sign-offs still render block, 10.5px,
muted, 25.5px margin. **And it closed #145's remainder:** freed from this rule, item 107's last four runs
compute italic, 30 of 30.

**Evidence:** `agents/logs/qa-2026-11-16.md`; `web/src/lib/footnoteParagraphs.mjs`; `web/astro.config.mjs`;
both `[...slug].astro` templates; queue items 118 (closed), 120, 121.
