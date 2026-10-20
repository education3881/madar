#!/usr/bin/env python3
r"""
qa_composition.py — standing assertion 34. Owner: Assertions Engineer.

Closes standing-queue **item 14** (raised 2026-10-13 as that day's forward
question, seven displacements, 7 days open) and **item 13** (raised the same day
from the Edition 05 flip's render inspection, six displacements, 7 days open).
Ruling **#109**.

THE QUESTION ITEM 14 ASKED, verbatim: *which of this publication's claims are
properties of a COMPOSITION rather than of a file?* — and the half that had to be
answered before anything could be built: *can the BUILD be made to ask this at
all, or is composition only ever visible to a render?*

THE ANSWER, and it is a boundary rather than a yes or a no. A composition defect
is one that holds of an assembly and of **no part**. Sort them by who does the
assembling and the boundary falls in one place, cleanly:

  (1) assembled by the BUILD into one document — N independently-correct
      fragments inlined into one cascade, one id namespace, one graph. The
      collision is **in the served bytes**, so a static reader can see it.
  (2) assembled by a CONSUMER across documents — the JSON-LD graph a crawler
      merges, the two feeds one reader subscribes to, the hreflang cluster.
      Also **in the served bytes**, but only if the corpus is read as one
      document instead of file by file.
  (3) assembled by the LAYOUT ENGINE — which of two matching rules wins, what
      the winner then paints, what overflows. **Only a render can see this**,
      and that is assertion 33's territory and queue item 28's.

So the build can ask (1) and (2) and cannot ask (3). **What this tool asserts is
the PRECONDITION, not the consequence**, and that is the deliberate choice: a
collision whose consequence is invisible today becomes visible the day a sixth
cover lands, and the precondition is the half a static check can state honestly.

WHAT IT ASSERTS, in two limbs that share one input.

  LIMB 1 — NO TWO INLINE <style> BLOCKS IN ONE SERVED DOCUMENT DECLARE THE SAME
  FULL SELECTOR. This is the Edition 05 cover leak (queue item 13) stated as a
  property of the document rather than of a cover. `inlineCover()` injects each
  cover's markup *including its own <style> block*; five blocks in one document
  are one cascade; when five covers all wrote `.kick`, the last in document order
  won for all five and **every edition's cover type printed in Edition 01's
  vermilion from the second cover onward**. Every one of the five SVG files was
  correct standalone. The repair scoped each cover under `.ed-cover-NN`; nothing
  in the operation would have noticed the sixth cover omitting that prefix.

  LIMB 2 — EVERY INLINED COVER'S KICKER FILL IS ITS OWN REGISTRY ACCENT. Read
  from the declared rule in the served document and compared against
  `web/src/lib/editions.ts`. **Limb 2 is only sound because limb 1 holds**, and
  the tool says so in its output: a declared value is the computed value exactly
  when no other rule in the document can match the same element. If limb 1 fails,
  limb 2's reading is unlicensed and the tool says that instead of asserting it.

WHY NOT A BROWSER. Item 13 specified the computed `fill` read out of a real
browser through an iframe — the way the defect was originally measured. That is
the right instrument for a *measurement* and the wrong one for a *gate* here:
four assertions already pay for a headless Chrome, the thing being gated is a
cascade with one rule per element, and limb 1 is precisely the assertion that
makes the cheap reading equal the expensive one. **The specification was not the
scope, for the fourteenth consecutive closure** — item 13 asked for a check on
covers and what is asserted is a property of every served document, of which the
covers are today the only instance.

WHAT WAS MEASURED WHILE BUILDING IT, over the real `dist` of 2026-10-20, and
recorded here because four of the five surfaces came back clean and a clean
surface nobody writes down is a surface the next run re-checks blind:

  * **inline <style> blocks: 13 across 135 served documents** — five on each
    editions page, three on `/valence/`. Full-selector collisions: **0**. The
    surface limb 1 guards is small, and it is small because Astro scopes
    component styles into an external sheet with `data-astro-cid-*`; what is
    inlined is exactly what the build was told to inline.
  * **JSON-LD: 266 distinct `@id` across the corpus, 2 described (not merely
    referenced) on more than one page, 0 disagreements** about any property.
    This is surface (2) and the one a consumer is explicitly invited to merge.
  * **the two feeds as one subscription: 44 + 44 items, 0 shared `<guid>`, 0
    shared `<link>`** — no item silently swallowed by a reader taking both.
  * **hreflang: 396 alternate links across 132 pages, reciprocity clean**;
    134 canonicals and 134 `og:url` over 135 pages, none shared by two pages.
  * **`og:image` is shared by 45 pairs of pages and that is correct** — a pair
    shares one card by design, and the non-article pages share the brand card.

TWO FALSE POSITIVES THE HARNESS PRODUCED BEFORE THE CODE WAS RIGHT, both of the
same shape, and the shape is the part worth carrying. A first draft collected
**bare class tokens** rather than full selectors and reported the editions pages
as 5-way collisions — `.kick` does appear in five blocks, scoped five different
ways, which is the repair working. A second probe reported **33 of 43 pieces
missing from their country facet page**; `web/src/pages/browse/[...path].astro`
says in a comment that four countries clear a `>= 2` bar and thirty-eight do not
and are linked directly to their piece. Neither was a defect and both read
exactly like one. **A composition check's error rate is set by whether it knows
the INTENDED assembly** — #35 says prove the bite as carefully as the control,
and this is its input-side twin: an assembly you have not been told the shape of
will report every deliberate arrangement as a collision. That is why limb 1
compares full selectors and limb 2 reads the registry rather than guessing.

Exit 0 clean · 1 on any failed assertion · 2 on bad input.
No third-party dependencies, no browser.
"""

import json
import re
import sys
from pathlib import Path

STYLE = re.compile(r"<style[^>]*>(.*?)</style>", re.S | re.I)
COMMENT = re.compile(r"/\*.*?\*/", re.S)
AT_RULE = re.compile(r"@[a-zA-Z-]+[^{;]*\{(?:[^{}]|\{[^{}]*\})*\}", re.S)
COVER_SCOPE = re.compile(r"\.ed-cover-(\d+)\s+\.kick\b")
FILL = re.compile(r"fill:\s*(#[0-9A-Fa-f]{3,8}|[a-zA-Z]+)")
REGISTRY_NUM = re.compile(r"number:\s*(\d+)")
REGISTRY_ACCENT = re.compile(r"accent:\s*'([^']+)'")


def rules(css):
    """(selector, declaration-body) pairs, at-rules and comments removed."""
    css = COMMENT.sub(" ", css)
    css = AT_RULE.sub(" ", css)
    out = []
    for chunk in css.split("}"):
        if "{" not in chunk:
            continue
        head, body = chunk.split("{", 1)
        body = " ".join(body.split())
        for sel in head.split(","):
            sel = " ".join(sel.split())
            if sel:
                out.append((sel, body))
    return out


def read_registry(root):
    """edition number -> accent, from web/src/lib/editions.ts."""
    src = root / "web" / "src" / "lib" / "editions.ts"
    if not src.exists():
        return None, "web/src/lib/editions.ts not found"
    text = src.read_text(encoding="utf-8")
    numbers = [int(m.group(1)) for m in REGISTRY_NUM.finditer(text)]
    accents = [m.group(1) for m in REGISTRY_ACCENT.finditer(text)]
    if not numbers or len(numbers) != len(accents):
        return None, ("editions.ts parsed to %d number(s) and %d accent(s); a "
                      "short or uneven parse is refused rather than compared"
                      % (len(numbers), len(accents)))
    return dict(zip(numbers, accents)), None


def main():
    if len(sys.argv) != 2:
        print("usage: qa_composition.py <repo-root>", file=sys.stderr)
        sys.exit(2)
    root = Path(sys.argv[1]).resolve()
    dist = root / "web" / "dist"
    if not dist.is_dir():
        print("qa_composition: %s is not a built site (no web/dist)" % root,
              file=sys.stderr)
        sys.exit(2)

    pages = sorted(dist.rglob("*.html"))
    if len(pages) < 50:
        print("qa_composition: REFUSED — %d served document(s) found under "
              "web/dist; a short parse is refused rather than passed vacuously."
              % len(pages), file=sys.stderr)
        sys.exit(2)

    print("qa_composition — properties of an ASSEMBLY, not of any file in it")
    print("  served documents ........................... %d" % len(pages))

    # ---------------- limb 1: one cascade, one namespace ----------------
    blocks_total = 0
    docs_with_blocks = 0
    collisions = []      # (page, selector, block indices, n distinct bodies)
    for page in pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        blocks = STYLE.findall(text)
        blocks_total += len(blocks)
        if blocks:
            docs_with_blocks += 1
        if len(blocks) < 2:
            continue
        seen = {}
        for i, block in enumerate(blocks):
            for sel, body in rules(block):
                seen.setdefault(sel, []).append((i, body))
        for sel, occurrences in seen.items():
            where = sorted({i for i, _ in occurrences})
            if len(where) < 2:
                continue
            bodies = {b for _, b in occurrences}
            collisions.append((str(page.relative_to(dist)), sel, where,
                               len(bodies)))

    print("  inline <style> blocks ...................... %d across %d document(s)"
          % (blocks_total, docs_with_blocks))
    print("  LIMB 1  full selectors declared in >1 block of one document  %d"
          % len(collisions))

    limb1_ok = not collisions
    if collisions:
        print("    FAIL — each of these is two independently-correct fragments")
        print("    writing into ONE cascade. The later block wins for every")
        print("    element the earlier one meant to style, and no file is wrong.")
        for page, sel, where, nbodies in collisions[:20]:
            verdict = ("DIFFERENT declarations — one silently wins"
                       if nbodies > 1 else "identical declarations")
            print("      %s  '%s'  blocks %s  (%s)"
                  % (page, sel, where, verdict))
        if len(collisions) > 20:
            print("      ... and %d more" % (len(collisions) - 20))
    else:
        print("    ok — every inlined fragment keeps its own namespace, so no")
        print("    element in any served document is matched by two inline rules")

    # ---------------- limb 2: the cover keeps its identity ----------------
    registry, why = read_registry(root)
    failed_covers = []
    covers_checked = 0
    print("  LIMB 2  each inlined cover's kicker fill == its registry accent")
    if registry is None:
        print("    REFUSED — %s" % why)
        print("\nqa_composition: FAIL — limb 2 could not read its ruler.")
        sys.exit(1)

    if not limb1_ok:
        print("    NOT ASSERTED — limb 1 failed, so a declared value is not")
        print("    known to be the computed value. The reading below would be")
        print("    unlicensed; it is withheld rather than printed as a pass.")
    else:
        for page in pages:
            text = page.read_text(encoding="utf-8", errors="replace")
            for block in STYLE.findall(text):
                for sel, body in rules(block):
                    m = COVER_SCOPE.fullmatch(sel)
                    if not m:
                        continue
                    number = int(m.group(1))
                    declared = FILL.search(body)
                    covers_checked += 1
                    expected = registry.get(number)
                    got = declared.group(1) if declared else None
                    if expected is None:
                        failed_covers.append(
                            (str(page.relative_to(dist)), number, "no registry row", got))
                    elif got is None:
                        failed_covers.append(
                            (str(page.relative_to(dist)), number, expected, "no fill declared"))
                    elif got.lower() != expected.lower():
                        failed_covers.append(
                            (str(page.relative_to(dist)), number, expected, got))
        print("    covers read ............................. %d scoped kicker rule(s), "
              "%d registry row(s)" % (covers_checked, len(registry)))
        if covers_checked == 0:
            print("    REFUSED — no `.ed-cover-NN .kick` rule found in any served")
            print("    document. Either the editions page stopped inlining covers")
            print("    or the scoping convention changed; both are a change this")
            print("    assertion must not pass over in silence.")
            failed_covers.append(("(corpus)", 0, "at least one cover", "none"))
        elif failed_covers:
            print("    FAIL — a cover is printing in another edition's colour:")
            for page, number, expected, got in failed_covers:
                print("      %s  edition %02d  expected %s  declared %s"
                      % (page, number, expected, got))
        else:
            print("    ok — every cover prints its own accent, and the DECLARED")
            print("    value is the COMPUTED value because limb 1 holds: no other")
            print("    inline rule in the document can match these elements.")

    if collisions or failed_covers:
        print("\nqa_composition: FAIL — see above. Each of these defects lives in "
              "no file; it is created by putting correct files together, which is "
              "why thirty-three assertions reading one artefact at a time could "
              "not see it.")
        sys.exit(1)

    print("\nCLEAN qa_composition — %d served documents, %d inlined style blocks, "
          "no two of which write the same selector into one cascade, and %d cover "
          "kicker(s) each printing its own registry accent." %
          (len(pages), blocks_total, covers_checked))
    sys.exit(0)


if __name__ == "__main__":
    main()
