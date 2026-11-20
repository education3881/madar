#!/usr/bin/env python3
"""Standing assertion 43 — every date a TEMPLATE emits is derived from the tree,
and none from the clock.

WHY THIS EXISTS (standing-queue items 44 and 46, closed together 2026-11-20)
---------------------------------------------------------------------------
Two rows sat on the board for 25 and 24 days asking the same question about two
fields, and item 44 said in writing that *"the two should be closed by one
instrument rather than two."* They are the same claim:

  item 44 (raised 2026-10-26) — `dateModified` was missing from all 88 article
      pages until the growth function wired it to the sitemap's own resolver.
      **88 of 88 is a measurement, not an assertion**: a later template edit can
      drop the field and no build goes red.
  item 46 (raised 2026-10-27) — `copyrightYear` replaced `new Date().getFullYear()`
      in `SiteFooter.astro` on all 134 pages the same week, for the reason written
      into `lib/copyrightYear.mjs`: a build-clock year **agrees with itself across
      any two builds run in the same period**, so no comparison this operation
      owns can ever catch it. On 1 January it is wrong on every page and nothing
      changes.

Item 46's sentence is the design brief for this file. Every instrument here puts
one byte beside another byte, and a clock-derived date is the one served claim
that is invisible to that method — not because the comparison is weak but because
both operands move together. So this file has two kinds of limb, and the second
kind is not a refinement of the first:

  LIMBS 1-4 read the OUTPUT and compare two channels that must agree.
  LIMB 5 reads the SOURCE and asks whether a clock is consulted at all.

Limb 5 is the direction `qa_selector_coverage` opened on 2026-11-01 — *read the
specification, not only the artefact* — pointed at time instead of at markup. It
is the only limb that can see the defect item 46 names, and it costs one grep.

WHAT IT ASSERTS
---------------
1. **Presence, by name and not by number.** Every article page in `dist` carries
   a `dateModified` in its JSON-LD, well-formed `YYYY-MM-DD`, and the set of
   pages carrying one equals the set of article pages the build serves. A count
   would have been maintained by nobody (#57); the comparison is between two
   sets of page paths.
2. **Monotonicity.** `dateModified >= datePublished` on every article page. A
   page modified before it was published is a resolver reading the wrong file.
3. **Two channels, one answer.** For every article page, its own `dateModified`
   equals the date half of the sitemap `<lastmod>` for that page's own URL. Both
   are emitted by `createLastmodResolver()`, from two call sites — `astro.config.mjs`
   for the sitemap and `pages/[...slug].astro` for the page — and nothing but
   this limb has ever compared them.
4. **The copyright year is the site's own date, not the machine's.** Every served
   HTML document carries the `©` notice, all of them carry ONE year, and that
   year equals the year of the sitemap's `<lastmod>` for the site root, which is
   what `copyrightYear()` claims to derive. `valence/index.html` is a DECLARED
   exemption, named here rather than skipped: it is a standalone instrument served
   out of `public/` and never rendered through `Base.astro`, so it has no footer
   to carry one (the 08-17 orphan audit's page, same exemption shape as
   `qa_date_identity`'s standing listing row).
5. **No clock reaches a served date.** No file under `web/src/` calls the clock —
   zero-argument `new Date()`, `new Date` with no call, `Date.now()` — outside a
   declared exemption list, and the list is empty today. `new Date(x)` with an
   argument is a PARSE and is allowed; `sitemapLastmod.mjs` has two and they are
   how it compares git dates to each other.

WHY THE TREE GUARD IS NOT CALLED, EVALUATED RATHER THAN QUOTED
--------------------------------------------------------------
Item 44's own wording prescribes a precondition for limb 3: *"`lastmod_tree_guard.py`
exists precisely because a git-derived date must not be compared against a
working-tree build, so the third limb needs the guard."* **It does not, and the
reason is worth the paragraph.** That guard protects a comparison with ONE
provenance-derived operand and one operand made of bytes on disk; a dirty tree
moves those two apart and manufactures a finding. Every comparison in this file
has **two date operands emitted by one build**. A dirty tree, or a `dist` behind
`HEAD`, moves both of them together — the sitemap and the article page call the
same resolver on the same HEAD, and a stale `served_dates` register is read by
both — so no state of the working tree can make limb 3 or limb 4 disagree when
the templates are right. This file reads git **not at all**, which is checkable
by inspection: there is no `subprocess` import below.

A precondition with no axis to protect is not a safe extra; it is a refusal this
instrument would hand out on drafting days for no reason, which is how a guard
gets switched off. The queue row was read and then measured against what the
limbs actually compare.

No third-party dependencies. Exit 0 clean, exit 1 with a sentence.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# Derived from the sitemap's own <loc> values rather than written here, so a
# base-URL change cannot leave this file pointing at the old origin.
ARTICLE_PAGE_RE = re.compile(r"^(?:ar/)?articles/[^/]+/index\.html$")
LOC_LASTMOD_RE = re.compile(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>")
ISO_DAY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
COPYRIGHT_RE = re.compile(r"©\s*(\d{4})")

# A served document with no footer, declared with its reason. See limb 4.
DECLARED_FOOTERLESS = {"valence/index.html"}

# A clock read is a zero-argument Date construction or Date.now(). `new Date(x)`
# is a parse and is allowed — the resolver uses two to compare git dates.
CLOCK_RES = (
    re.compile(r"\bnew\s+Date\s*\(\s*\)"),
    re.compile(r"\bnew\s+Date\b(?!\s*\()"),
    re.compile(r"\bDate\.now\s*\("),
)
# Declared exemptions, as `relative/path.ext:line`. EMPTY TODAY, and that is the
# assertion: a clock read in a served template is the defect, not a style.
DECLARED_CLOCK_READS: set[str] = set()

SRC_SUFFIXES = (".astro", ".mjs", ".js", ".ts", ".tsx", ".jsx")


def strip_comments(text: str) -> str:
    """Blank every comment, preserving line count so a hit keeps its line number.

    THIS FUNCTION IS THE LIMB'S FIRST FALSE POSITIVE, FIXED IN PLACE. Limb 5's
    first run reported `web/src/lib/copyrightYear.mjs:8` as a clock read: that
    line is inside the block comment that EXPLAINS why the clock read was
    removed, so the one file in the repository written to document the fix was
    the only file reported as carrying the defect. The first draft stripped
    `//` and nothing else, which is the same shape as item 97's `<style>`
    counted inside an HTML comment and 2026-09-14's trap on the input side:
    *where does the string I am looking for also legitimately appear?* In a
    codebase whose convention is to write the reason for every repair beside
    it, the answer is always "in the prose about the defect".
    """
    out = []
    i, n = 0, len(text)
    while i < n:
        two = text[i:i + 2]
        if two == "/*":
            j = text.find("*/", i + 2)
            j = n if j == -1 else j + 2
            out.append(re.sub(r"[^\n]", " ", text[i:j]))
            i = j
        elif two == "//":
            j = text.find("\n", i)
            j = n if j == -1 else j
            out.append(" " * (j - i))
            i = j
        elif text[i:i + 4] == "<!--":
            j = text.find("-->", i + 4)
            j = n if j == -1 else j + 3
            out.append(re.sub(r"[^\n]", " ", text[i:j]))
            i = j
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def json_ld_blocks(html: str) -> list[dict]:
    out = []
    for m in re.finditer(
        r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S
    ):
        try:
            parsed = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        out.extend(parsed if isinstance(parsed, list) else [parsed])
    return out


def walk_nodes(node, acc):
    if isinstance(node, dict):
        acc.append(node)
        for v in node.values():
            walk_nodes(v, acc)
    elif isinstance(node, list):
        for v in node:
            walk_nodes(v, acc)
    return acc


def main() -> int:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "web" / "dist"
    if not dist.is_dir():
        print(f"qa_emitted_dates: FAIL — no dist at {dist}")
        return 1

    failures: list[str] = []

    sitemaps = sorted(dist.glob("sitemap-*.xml"))
    if not sitemaps:
        print("qa_emitted_dates: FAIL — no sitemap-*.xml in dist; limbs 3 and 4 "
              "have nothing to compare against, which is a refusal to pass and "
              "not a pass (08-16 silent-pass trap).")
        return 1
    lastmod: dict[str, str] = {}
    for s in sitemaps:
        for loc, lm in LOC_LASTMOD_RE.findall(s.read_text(encoding="utf-8")):
            lastmod[loc] = lm
    if not lastmod:
        print("qa_emitted_dates: FAIL — the sitemap carries no <lastmod> at all.")
        return 1

    # The site root's own URL, derived from the shortest <loc> rather than
    # written down. Every other URL is a suffix of it.
    root_url = min(lastmod, key=len)

    # ---- limbs 1, 2, 3 -------------------------------------------------
    article_pages: list[str] = []
    carrying: list[str] = []
    for page in sorted(dist.rglob("index.html")):
        rel = page.relative_to(dist).as_posix()
        if not ARTICLE_PAGE_RE.match(rel):
            continue
        article_pages.append(rel)
        html = page.read_text(encoding="utf-8", errors="replace")
        nodes = walk_nodes(json_ld_blocks(html), [])
        mods = {n["dateModified"] for n in nodes if isinstance(n.get("dateModified"), str)}
        pubs = {n["datePublished"] for n in nodes if isinstance(n.get("datePublished"), str)}
        if not mods:
            failures.append(f"{rel}: no dateModified in any JSON-LD block — the field left silently")
            continue
        if len(mods) > 1:
            failures.append(f"{rel}: {sorted(mods)} — one page, one modification date")
            continue
        carrying.append(rel)
        mod = next(iter(mods))
        if not ISO_DAY_RE.match(mod):
            failures.append(f"{rel}: dateModified {mod!r} is not a bare YYYY-MM-DD")
            continue
        for pub in sorted(pubs):
            if ISO_DAY_RE.match(pub) and mod < pub:
                failures.append(
                    f"{rel}: dateModified {mod} is BEFORE datePublished {pub} — "
                    f"a page cannot be modified before it exists"
                )
        url = root_url + rel[: -len("index.html")]
        if url not in lastmod:
            failures.append(f"{rel}: serves an article page the sitemap does not list as {url}")
            continue
        sm_day = lastmod[url][:10]
        if sm_day != mod:
            failures.append(
                f"{rel}: dateModified {mod} against sitemap <lastmod> {sm_day} — "
                f"two call sites of one resolver have stopped agreeing"
            )

    if not article_pages:
        print("qa_emitted_dates: FAIL — zero article pages found in dist; this check read nothing.")
        return 1
    # The population is compared against the SOURCE, not against itself. The
    # first draft compared `article_pages` with `carrying` — two sets derived
    # from the same loop, so every member of the difference had already failed a
    # per-page branch one screen above. #128 declined a row for exactly that:
    # *a defect two limbs catch proves neither of them necessary.* The set that
    # cannot be derived from `dist` is the set of APPROVED pieces on disk, and a
    # page that was never built is invisible to a loop over built pages.
    expected: set[str] = set()
    for coll, prefix in (("articles", "articles/"), ("articles-ar", "ar/articles/")):
        for f in sorted((REPO / "web" / "src" / "content" / coll).glob("*.md")):
            head = f.read_text(encoding="utf-8").split("\n---", 1)[0]
            if re.search(r"^approved:\s*true\s*$", head, re.M):
                expected.add(f"{prefix}{f.stem}/index.html")
    if not expected:
        failures.append("presence: no approved piece on disk; this limb has no population to name")
    unbuilt = sorted(expected - set(carrying))
    unexpected = sorted(set(carrying) - expected)
    if unbuilt:
        failures.append(
            f"presence: {len(unbuilt)} approved piece(s) serve no readable dateModified — "
            f"{unbuilt[:4]}; the sets are compared by NAME, never by count (#57), and against "
            f"the source rather than against this loop's own output"
        )
    if unexpected:
        failures.append(
            f"presence: {len(unexpected)} page(s) carry a dateModified for a slug no approved "
            f"piece declares — {unexpected[:4]}"
        )

    # ---- limb 4 --------------------------------------------------------
    years: dict[str, list[str]] = {}
    footerless: list[str] = []
    declared: list[str] = []
    for page in sorted(dist.rglob("*.html")):
        rel = page.relative_to(dist).as_posix()
        html = page.read_text(encoding="utf-8", errors="replace")
        found = COPYRIGHT_RE.findall(html)
        if not found:
            (declared if rel in DECLARED_FOOTERLESS else footerless).append(rel)
            continue
        for y in set(found):
            years.setdefault(y, []).append(rel)
    if footerless:
        failures.append(
            f"limb 4: {len(footerless)} served document(s) carry no copyright notice "
            f"and are not declared — {footerless[:4]}"
        )
    for rel in sorted(DECLARED_FOOTERLESS):
        if rel not in declared and (dist / rel).exists():
            failures.append(
                f"limb 4: {rel} is declared footerless and now carries a notice — "
                f"a declared exemption that has stopped applying is a stale exemption"
            )
    if len(years) > 1:
        failures.append(
            "limb 4: the copyright notice carries " + ", ".join(
                f"{y} on {len(p)} page(s)" for y, p in sorted(years.items())
            ) + " — one publication, one year"
        )
    elif years:
        served_year = next(iter(years))
        root_year = lastmod[root_url][:4]
        if served_year != root_year:
            failures.append(
                f"limb 4: the footer says {served_year} and the sitemap's own date for "
                f"{root_url} is {root_year} — the year is no longer a fact about the tree"
            )

    # ---- limb 5 --------------------------------------------------------
    src = REPO / "web" / "src"
    clock_hits: list[str] = []
    scanned = 0
    if not src.is_dir():
        failures.append(f"limb 5: no {src} to read; a limb that enumerates nothing asserts nothing")
    else:
        for f in sorted(src.rglob("*")):
            if not f.is_file() or f.suffix not in SRC_SUFFIXES:
                continue
            scanned += 1
            rel = f.relative_to(REPO).as_posix()
            text = strip_comments(f.read_text(encoding="utf-8", errors="replace"))
            for i, line in enumerate(text.splitlines(), 1):
                if any(rx.search(line) for rx in CLOCK_RES):
                    tag = f"{rel}:{i}"
                    if tag not in DECLARED_CLOCK_READS:
                        clock_hits.append(f"{tag}: {line.strip()[:110]}")
        if scanned == 0:
            failures.append("limb 5: zero source files scanned; this limb read nothing")
    for hit in clock_hits:
        failures.append(
            f"limb 5: {hit} — a served date read off the build machine's clock. "
            f"It agrees with itself across any two builds in the same period, so no "
            f"comparison of bytes can ever catch it (item 46)."
        )
    for tag in sorted(DECLARED_CLOCK_READS):
        path, _, line_no = tag.rpartition(":")
        p = REPO / path
        if not p.exists():
            failures.append(f"limb 5: declared exemption {tag} names a file that no longer exists")

    if failures:
        print(f"qa_emitted_dates: FAIL — {len(failures)} finding(s).")
        for f in failures[:40]:
            print(f"  ✗ {f}")
        if len(failures) > 40:
            print(f"  … and {len(failures) - 40} more")
        print("  A date a template emits is a claim about the repository. If it is a "
              "claim about the machine instead, it is true on the day it is built and "
              "silently wrong afterwards.")
        return 1

    print(
        f"qa_emitted_dates: PASS — {len(carrying)} of {len(article_pages)} article pages carry a "
        f"dateModified, the set equal by NAME to the {len(expected)} pages the approved corpus owes, "
        f"every one at or after its own datePublished and equal to the sitemap "
        f"<lastmod> for its own URL; one copyright year ({next(iter(years), '—')}) across "
        f"{sum(len(p) for p in years.values())} served documents, matching the sitemap's date for "
        f"{root_url}, with {len(declared)} declared footerless; and {scanned} source files under "
        f"web/src read the clock {len(clock_hits)} times. "
        f"Limbs 1-4 compare two emitted channels; limb 5 is the only one that can see a clock, "
        f"because a clock-derived date agrees with itself."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
