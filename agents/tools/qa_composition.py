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

LIMBS 3, 4 AND 5 — ADDED 2026-11-04, closing standing-queue **item 29** (raised
2026-10-20 as that day's forward question, 15 days, the oldest row in OPEN).
**Second instance of ruling #125** — see the WITHDRAWN note below, which is that
ruling read from the other side: #125 is about a decline that delegates to a
sibling, and this is a ruling that declared a surface *ungated* while the sibling
had gated it for sixty days. A claim about what is **not** checked is read off
the wiring, never off the ruling that wrote it.
THE RULER AND ITS KERNEL, in one sentence per #126 clause 1:
*this tool's ruler is textual identity across served documents — it can tell that
two documents disagree and it cannot tell which of them a consumer will believe,
so its kernel is the CONSUMER'S PRECEDENCE RULE, and that is why every limb here
asserts a precondition and none asserts a consequence.*

Item 29's ask: #109 named four statically-computable composition surfaces and
assertion 34 gated **one**, leaving the other three as `/tmp` probes that would
not survive the runner. Promote them. **Three were promoted and the fourth was
WITHDRAWN, because the enumeration in #109 was wrong by one** — and finding that
out cost one grep of a sibling, which is the whole of #125:

  LIMB 3 — EVERY JSON-LD `@id` DESCRIBED ON MORE THAN ONE PAGE AGREES ON EVERY
  PROPERTY THE PAGES SHARE. The intended assembly is stated in `ld_nodes()`: a
  consumer merges nodes **by `@id`** across every page it crawls, so `{"@id": X}`
  alone is a *reference* that claims nothing while `{"@id": X, "name": …}` is a
  *description* that does. Two pages describing one node differently is a
  contradiction that exists in **neither page** — the merged graph holds both.
  Measured on the 2026-11-04 build: **1,206 nodes carrying an `@id`, 386
  distinct, 2 described on more than one page, 0 disagreements.** The 386 is item
  29's own hand-verified figure now derived by a gate: that row recorded 266 →
  386 after the growth function added 120 nodes mid-run, *"and the only reason it
  was re-measured is that I happened to remember."*

  LIMB 4 — THE TWO FEEDS ARE ONE SUBSCRIPTION. No `<guid>` and no `<link>` is
  shared between `rss.xml` and `ar/rss.xml`, none repeats inside either, and none
  is absent. The intended assembly: a reader subscribing to both editions holds
  one item list keyed by `guid`, so a shared identity means one item **silently
  swallows** the other and the publication cannot tell. 44 + 44 items, 0 shared.
  Genuinely ungated before today — `qa_feed_validators` is one of the three
  assertions that do not gate, and it reads a validator rather than the identity.

  LIMB 5 — THE CANONICAL NAMESPACE. Every served page claims **exactly one**
  canonical, no two pages claim the **same** one, and the single exemption is
  **positional rather than textual** (#113's shape): `404.html` must claim
  **none**, because a canonical on an error page invites a crawler to index the
  error as the preferred version of something. 134 canonicals over 135 documents,
  the one gap being the error page. That property was already written down — in
  `qa_reachability`'s prose, *"carries noindex for the same reason it carries no
  canonical"* — and asserted nowhere, which is #125 one more time.

  **WITHDRAWN — hreflang reciprocity.** #109 named it as ungated and item 29
  inherited that. It is not: **`qa_hreflang_clusters` clauses 1 and 2 have
  asserted cluster membership, dereferencing and reciprocity since 2026-09-01,
  as a BUILD STEP in `astro-pages.yml`.** The count is printed here (264
  alternates across 132 pages, x-default excluded, which is #109's 396 minus one
  per page) and the decline names the sibling **having read it and proved it**,
  not on the assumption that somebody must be. Shipping the duplicate would have
  put one number in a second place to drift from.

PROVED 14 WAYS on copies of the real `dist`, bite first, every injection asserted
to have changed the file before the check ran on it (#35 and its 09-14 addendum):
five bites red — one `@id` described twice with different names, one `guid` in
both feeds, two pages claiming one canonical, a canonical on `404.html`, and a
real page with its canonical removed — and **bite 5 was caught twice**, by the
error-page clause and by the uniqueness clause, because the root it named was
already claimed by `/`; so a sixth bite gives `404.html` a canonical **nothing
else claims**, which isolates the clause. *A defect two limbs catch proves
neither of them necessary* — #126's kernel lesson applied to a harness. Three
controls green either side, including the control that matters most for limb 3: a
bare `@id` **reference** injected into the same page must stay silent, and does.
And the withdrawal is proved in both directions: the two hreflang bites are
**silent here and red in `qa_hreflang_clusters`**. Harness of record:
`agents/tools/proofs/qa_composition_limbs_proof.py`.

**THE GATE COUNT DOES NOT MOVE: 41 tools, 38 gating.** Three limbs were added to
an assertion already wired into `postbuild`; no tool was added, so
`qa_patch_queue` derives the same three numbers. *A run that adds a limb and
reports a tool is how a count drifts.*

Exit 0 clean · 1 on any failed assertion · 2 on bad input.
No third-party dependencies, no browser.
"""

import json
import re
import sys
from pathlib import Path

SITE = "https://education3881.github.io/madar/"

STYLE = re.compile(r"<style[^>]*>(.*?)</style>", re.S | re.I)
JSONLD = re.compile(
    r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', re.S | re.I)
LINK_TAG = re.compile(r"<link\b[^>]*>", re.I)
ATTR = re.compile(r'([A-Za-z][\w:-]*)="([^"]*)"')
ITEM = re.compile(r"<item\b.*?</item>", re.S | re.I)
GUID = re.compile(r"<guid[^>]*>(.*?)</guid>", re.S | re.I)
RLINK = re.compile(r"<link\b[^>]*>(.*?)</link>", re.S | re.I)
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


def served_url(rel: str) -> str:
    """dist-relative path -> the URL that path is served at.

    THE INTENDED ASSEMBLY, stated rather than inferred (item 29): this site is
    built with `build.format: 'directory'`, so every route is a directory with an
    `index.html` and is served WITHOUT that filename. The root `index.html` is
    the site root. Nothing else in dist is HTML.
    """
    rel = rel.replace("\\", "/")
    if rel == "index.html":
        return SITE
    if rel.endswith("/index.html"):
        return SITE + rel[: -len("index.html")]
    return SITE + rel


def ld_nodes(text: str):
    """Every JSON-LD node carrying an @id, with the keys that DESCRIBE it.

    THE INTENDED ASSEMBLY: a consumer merges JSON-LD nodes BY `@id` across every
    page it crawls — that is what an `@id` is for. So `{"@id": X}` alone is a
    *reference* and carries no claim, while `{"@id": X, "name": ...}` is a
    *description* and does. Two pages describing one node differently is a
    contradiction that exists in neither page: the merged graph says both.
    """
    out = []
    for raw in JSONLD.findall(text):
        try:
            payload = json.loads(raw)
        except Exception:
            out.append(("(unparseable)", {}))
            continue
        stack = [payload]
        while stack:
            cur = stack.pop()
            if isinstance(cur, list):
                stack.extend(cur)
            elif isinstance(cur, dict):
                stack.extend(v for v in cur.values()
                             if isinstance(v, (dict, list)))
                node_id = cur.get("@id")
                if isinstance(node_id, str):
                    described = {k: v for k, v in cur.items() if k != "@id"}
                    out.append((node_id, described))
    return out


def link_rels(text: str):
    """Every <link> tag as a dict of its attributes."""
    for tag in LINK_TAG.findall(text):
        yield dict(ATTR.findall(tag))


def feed_items(path: Path):
    """(guid, link) per <item> in an RSS file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    rows = []
    for chunk in ITEM.findall(text):
        g = GUID.search(chunk)
        l = RLINK.search(chunk)
        rows.append((g.group(1).strip() if g else None,
                     l.group(1).strip() if l else None))
    return rows


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

    # ------- limb 3: one @id, one description, however many pages -------
    print("  LIMB 3  every JSON-LD @id DESCRIBED on >1 page agrees on every")
    print("          property the pages share")
    described = {}        # @id -> {page: {key: json}}
    ld_total = 0
    unparseable = []
    for page in pages:
        rel = str(page.relative_to(dist))
        text = page.read_text(encoding="utf-8", errors="replace")
        for node_id, desc in ld_nodes(text):
            if node_id == "(unparseable)":
                unparseable.append(rel)
                continue
            ld_total += 1
            if not desc:
                continue          # a bare reference makes no claim
            frozen = {k: json.dumps(v, sort_keys=True, ensure_ascii=False)
                      for k, v in desc.items()}
            described.setdefault(node_id, {}).setdefault(rel, {}).update(frozen)

    multi = {i: d for i, d in described.items() if len(d) > 1}
    ld_disagree = []
    for node_id, by_page in multi.items():
        keys = set()
        for d in by_page.values():
            keys |= set(d)
        for key in sorted(keys):
            values = {rel: d[key] for rel, d in by_page.items() if key in d}
            if len(set(values.values())) > 1:
                ld_disagree.append((node_id, key, values))

    print("          nodes with an @id .................. %d, of which %d distinct"
          % (ld_total, len(described)))
    print("          described on more than one page .... %d" % len(multi))
    if unparseable:
        print("          FAIL — JSON-LD that does not parse on %d page(s): %s"
              % (len(unparseable), ", ".join(sorted(set(unparseable))[:5])))
    if ld_disagree:
        print("          FAIL — the merged graph holds two values for one property:")
        for node_id, key, values in ld_disagree[:12]:
            print("            %s  '%s'" % (node_id, key))
            for rel, val in sorted(values.items()):
                print("              %-46s %s" % (rel, val[:90]))
    elif multi:
        print("          ok — no property disagrees, so a crawler merging these")
        print("          pages reads one consistent node per @id")

    # ------- limb 4: the two feeds are ONE subscription -------
    print("  LIMB 4  the two feeds are one subscription: no item identity is")
    print("          shared between them, and none repeats inside one")
    feed_paths = [dist / "rss.xml", dist / "ar" / "rss.xml"]
    feed_fail = []
    feeds = {}
    for fp in feed_paths:
        if not fp.exists():
            feed_fail.append(("(missing)", str(fp.relative_to(dist)), ""))
            continue
        feeds[str(fp.relative_to(dist))] = feed_items(fp)
    if len(feeds) != 2:
        print("          REFUSED — %d of 2 feeds found under dist. Both feeds are"
              % len(feeds))
        print("          shipped by this publication; a missing one is a change")
        print("          this assertion must not pass over in silence.")
    else:
        for name, rows in feeds.items():
            for field, idx in (("guid", 0), ("link", 1)):
                vals = [r[idx] for r in rows]
                if any(v is None for v in vals):
                    feed_fail.append((name, field,
                                      "%d item(s) carry no <%s>"
                                      % (sum(v is None for v in vals), field)))
                seen = {}
                for v in vals:
                    if v is not None:
                        seen[v] = seen.get(v, 0) + 1
                dupes = [v for v, n in seen.items() if n > 1]
                if dupes:
                    feed_fail.append((name, field,
                                      "%d value(s) repeat inside this feed: %s"
                                      % (len(dupes), dupes[:3])))
        (a_name, a_rows), (b_name, b_rows) = list(feeds.items())
        for field, idx in (("guid", 0), ("link", 1)):
            shared = ({r[idx] for r in a_rows if r[idx]}
                      & {r[idx] for r in b_rows if r[idx]})
            if shared:
                feed_fail.append(("%s + %s" % (a_name, b_name), field,
                                  "%d value(s) in BOTH feeds: %s"
                                  % (len(shared), sorted(shared)[:3])))
        print("          items ............................. %s"
              % " · ".join("%s %d" % (n, len(r)) for n, r in feeds.items()))
        if feed_fail:
            print("          FAIL — a reader subscribed to both is served one item")
            print("          where two were published, or one twice:")
            for name, field, why in feed_fail:
                print("            %s  <%s>  %s" % (name, field, why))
        else:
            print("          ok — every item in either feed is its own identity, so")
            print("          a reader taking both loses nothing and sees nothing twice")

    # ------- limb 5: the canonical namespace -------
    print("  LIMB 5  the canonical namespace: every served page claims exactly")
    print("          one canonical and no two pages claim the same one")
    alt_map = {}          # page url -> set of alternate urls (x-default excluded)
    canon = {}            # canonical url -> [page urls]
    url_of = {}
    for page in pages:
        rel = str(page.relative_to(dist))
        url_of[served_url(rel)] = rel
    for page in pages:
        rel = str(page.relative_to(dist))
        text = page.read_text(encoding="utf-8", errors="replace")
        me = served_url(rel)
        alts = set()
        for attrs in link_rels(text):
            relv = (attrs.get("rel") or "").lower()
            href = attrs.get("href")
            if not href:
                continue
            if relv == "alternate" and attrs.get("hreflang"):
                if attrs["hreflang"].lower() != "x-default":
                    alts.add(href)
            elif relv == "canonical":
                canon.setdefault(href, []).append(me)
        alt_map[me] = alts

    alt_total = sum(len(v) for v in alt_map.values())
    dangling = [(p, t) for p, ts in alt_map.items() for t in ts
                if t not in url_of]
    one_way = []
    for p, ts in alt_map.items():
        for t in ts:
            if t in url_of and p not in alt_map.get(t, set()):
                one_way.append((p, t))
    shared_canon = {c: ps for c, ps in canon.items() if len(ps) > 1}

    # Canonical COVERAGE, and the one exemption is positional and by design
    # (item 29's requirement: state the intended assembly in code). Every served
    # page declares exactly one canonical EXCEPT `404.html`, which must declare
    # none: a canonical on an error page tells a crawler the error page is the
    # preferred version of something. The exemption is one literal filename, not
    # a list that grows — anything else missing a canonical is a defect.
    claimed = set()
    for c, ps in canon.items():
        claimed.update(ps)
    no_canon = sorted(set(alt_map) - claimed)
    error_url = served_url("404.html")
    missing_canon = [u for u in no_canon if u != error_url]
    error_has_canon = error_url in claimed
    print("          coverage .......................... %d of %d page(s); the "
          "exemption is 404.html by design" % (len(claimed), len(pages)))
    if missing_canon:
        print("          FAIL — %d page(s) other than 404.html declare no canonical:"
              % len(missing_canon))
        for u in missing_canon[:8]:
            print("            %s" % u)
    if error_has_canon:
        print("          FAIL — 404.html declares a canonical. An error page that")
        print("          names a preferred URL invites a crawler to index the error.")

    print("          canonicals declared ............... %d over %d served page(s)"
          % (sum(len(p) for p in canon.values()), len(pages)))
    # The hreflang half of #109's surface (2) is MEASURED HERE AND NOT ASSERTED,
    # and the decline names its sibling the way #125 requires — by having gone
    # and looked rather than by saying somebody must be doing it. Reciprocity,
    # dereferencing and cluster membership are asserted by
    # `qa_hreflang_clusters` clauses 1 and 2, wired as a BUILD STEP in
    # astro-pages.yml since 2026-09-01, and both are proved live against this
    # tool's own bites 3 and 7 in agents/tools/proofs/qa_composition_limbs_proof.
    # So #109's enumeration of three ungated surfaces was wrong by one, and
    # standing-queue item 29 inherited the error: duplicating a gating sibling
    # buys nothing and costs a second place for the same number to drift.
    print("          hreflang alternates .............. %d across %d page(s) — "
          "MEASURED, NOT ASSERTED" % (alt_total,
                                      sum(1 for v in alt_map.values() if v)))
    print("            one-way %d · naming a URL this build does not serve %d. "
          "Asserted by" % (len(one_way), len(dangling)))
    print("            qa_hreflang_clusters clauses 1-2, a build step since "
          "2026-09-01, read")
    print("            and proved rather than assumed (#125).")
    if shared_canon:
        print("          FAIL — %d canonical URL(s) claimed by more than one page:"
              % len(shared_canon))
        for c, ps in list(shared_canon.items())[:8]:
            print("            %s  <-  %s" % (c, ", ".join(ps)))
    if not (shared_canon or missing_canon or error_has_canon):
        print("          ok — every served page but the error page claims exactly")
        print("          one canonical, and no two pages claim the same one")

    limb3_fail = bool(ld_disagree or unparseable)
    limb4_fail = bool(feed_fail) or len(feeds) != 2
    limb5_fail = bool(shared_canon or missing_canon or error_has_canon)

    if collisions or failed_covers or limb3_fail or limb4_fail or limb5_fail:
        print("\nqa_composition: FAIL — see above. Each of these defects lives in "
              "no file; it is created by putting correct files together, which is "
              "why thirty-three assertions reading one artefact at a time could "
              "not see it.")
        sys.exit(1)

    print("\nCLEAN qa_composition — %d served documents. %d inlined style blocks, "
          "no two writing one selector into one cascade; %d cover kicker(s) each "
          "printing its own registry accent; %d distinct @id with %d described on "
          "more than one page and no property disagreeing; two feeds of %s items "
          "sharing no guid and no link; and %d canonicals, one per served page "
          "but 404.html, no two of them the same. %d hreflang alternates "
          "measured here and asserted by qa_hreflang_clusters." %
          (len(pages), blocks_total, covers_checked, len(described), len(multi),
           " + ".join(str(len(r)) for r in feeds.values()), len(canon),
           alt_total))
    sys.exit(0)


if __name__ == "__main__":
    main()
