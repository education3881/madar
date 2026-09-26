#!/usr/bin/env python3
"""
qa_chrome_links — standing assertion #25: every internal pointer the build
emits resolves to a file the build also emits, and no pointer escapes the
base path.

WHY THIS FILE EXISTS (2026-09-26)
---------------------------------
It exists because a rule was not enough, and the run that found that out found
it by re-injecting its own history.

On **2026-08-16** the weekly review found that the footer's RSS link had
pointed at `/rss.xml` — off the `/madar` base path, a hard 404 — in the footer
of every page, in both languages, since the first publish on 2026-05-25. **83
days and 35 QA passes.** The rule codified that day is explicit:

    "the QA pass enumerates every href/src emitted by Base.astro,
     SiteHeader.astro, SiteFooter.astro and any layout-level component, and
     asserts each resolves in dist"

That rule was executed, by hand, as a one-line sweep — 98 targets, zero
unresolved — and recorded as the action of record. **It never became a file.**
Forty-one days later, the 2026-09-25 forward question asked whether the checks
this operation owns catch the defects it has actually shipped, rather than the
bites it composed for them. The footer link was re-injected into `dist` exactly
as it shipped (`"/madar/rss.xml"` -> `"/rss.xml"`, 2 occurrences on the English
home), the injection was proved to have changed the file, and the three
assertions that plausibly cover it were run:

    qa_reachability      control=0  bite=0   BLIND
    qa_body_links        control=0  bite=0   BLIND
    qa_consumer_surface  control=0  bite=0   BLIND

Nothing we own catches it. The reasons are each correct in isolation and that
is the point:

  * `qa_reachability` asserts that every **page is arrived at**. Its exit codes
    are clean / orphans / nothing-to-check. A pointer at nothing produces no
    orphan — it simply is not an edge. It is structurally blind here, and this
    check is its exact mirror: reachability asks *is every page pointed at?*,
    this asks *does every pointer resolve?* (the 08-17 orphan sweep and the
    08-16 chrome sweep are the two halves of one enumeration, and only the
    first was ever built).
  * `qa_body_links` enumerates what an **article** promises — the related rail,
    `sources[].url`, in-body markdown. Chrome is not an article's promise.
  * `qa_consumer_surface` reads the metadata surfaces (og, canonical, print).
    A footer anchor is not one.

Filed as ruling #67 — *a rule that names an assertion and does not produce a
file has produced nothing.* The 2026-09-13 rule counted the assertions the
operation owns and asked which of them were wired; it could not ask about an
assertion that was never a file, because a file that does not exist is not in
the count and can never drift out of it.

WHAT THIS CHECK ENUMERATES
--------------------------
For every `*.html` the build emits:

  1. Every `href`, `src`, `poster` and `srcset` target in the **served markup**
     — with `<script>` bodies and HTML comments removed first. VALENCE's inline
     script composes `<a href="${s.u}">` inside a JS template literal; that is
     source, not a pointer, and an assertion that reads it would report a
     defect that no consumer can see (the 2026-09-14 rule: scope the assertion
     to the thing it checks).

  2. **The base-path assertion.** Any root-relative target beginning with `/`
     and not with `/madar` is a defect by construction — it leaves the base
     path and lands on the host's root, where this site does not exist. This is
     the 08-16 defect's exact shape, and it is asserted separately from
     resolution because it has a separate cause: not a missing file, a missing
     prefix.

  3. **Resolution.** Every internal target — root-relative under the base, or
     absolute under this site's own origin — is dereferenced to a file in
     `dist`. Directory URLs resolve to `index.html`. Query strings and
     fragments are stripped before resolution; a fragment-only target (`#main`)
     is counted and not resolved, because its referent is the page itself.

  4. **The chrome set, printed by name.** A target that appears on at least 95%
     of served pages is layout-level by construction. The report prints that
     set explicitly rather than folding it into a total, because the defect
     this file exists for was a chrome link, and a report that says "0
     unresolved of 3,412" does not tell its reader that the footer was
     enumerated at all. Assertion 23's carried note of 2026-09-24 is the same
     complaint: print what you read.

External targets (other origins, `mailto:`, `tel:`, `data:`) are counted and
not fetched. Someone else's 404 is not our build's failure — the same reason
`qa_sources_alive` is deliberately out of the deploy gate.

PROVED BOTH WAYS (#35), against the defect as it shipped and not a composed one
------------------------------------------------------------------------------
  * control — the real 121-page build: exit 0.
  * bite — the historical footer link restored (`/madar/rss.xml` -> `/rss.xml`
    on the English home): exit 1, both occurrences named, reported as an
    off-base pointer rather than as a missing file.
  * bite 2 — a chrome stylesheet target repointed at a hashed filename the
    build does not emit: exit 1, named, and reported against the chrome set so
    the count moves as well as the verdict.
  * silent-pass trap (2026-08-16) — run against a directory with no HTML: exit
    2. An assertion with nothing to enumerate has failed, not passed.

Exit codes: 0 clean · 1 defects found · 2 nothing to check (a FAILURE).
"""

from __future__ import annotations

import collections
import os
import re
import sys

BASE = "/madar"
ORIGIN = "https://education3881.github.io"
SITE = ORIGIN + BASE

SCRIPT_RE = re.compile(r"<script\b.*?</script>", re.DOTALL | re.IGNORECASE)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
ATTR_RE = re.compile(
    r"""\b(href|src|poster)\s*=\s*["']([^"']*)["']""", re.IGNORECASE)
SRCSET_RE = re.compile(r"""\bsrcset\s*=\s*["']([^"']*)["']""", re.IGNORECASE)

# Chrome threshold: a target on this share of served pages is layout-level.
CHROME_SHARE = 0.95


def served_markup(raw: str) -> str:
    """The markup a consumer parses: script bodies and comments removed."""
    return COMMENT_RE.sub(" ", SCRIPT_RE.sub(" ", raw))


def targets(markup: str):
    for _attr, value in ATTR_RE.findall(markup):
        value = value.strip()
        if value:
            yield value
    for value in SRCSET_RE.findall(markup):
        for candidate in value.split(","):
            candidate = candidate.strip().split()[0] if candidate.strip() else ""
            if candidate:
                yield candidate


def classify(target: str):
    """(kind, path_or_none). kind in: fragment external off-base internal."""
    if target.startswith("#"):
        return "fragment", None
    low = target.lower()
    for scheme in ("mailto:", "tel:", "data:", "javascript:"):
        if low.startswith(scheme):
            return "external", None
    if target.startswith(SITE):
        rest = target[len(SITE):]
        return "internal", rest if rest.startswith("/") else "/" + rest
    if target.startswith("http://") or target.startswith("https://") \
            or target.startswith("//"):
        return "external", None
    if target.startswith("/"):
        if target == BASE or target.startswith(BASE + "/"):
            return "internal", target[len(BASE):] or "/"
        return "off-base", target
    # Document-relative. The build emits none today; resolved by the caller
    # against the page's own directory, and counted so a zero is a count.
    return "relative", target


def resolve(dist: str, path: str):
    """Dereference an internal path to a file in dist. Returns the path that
    was tried and whether it exists."""
    path = path.split("#", 1)[0].split("?", 1)[0]
    if not path:
        path = "/"
    rel = path.lstrip("/")
    tried = []
    if path.endswith("/") or rel == "":
        tried.append(os.path.join(dist, rel, "index.html"))
    else:
        tried.append(os.path.join(dist, rel))
        if not os.path.splitext(rel)[1]:
            tried.append(os.path.join(dist, rel, "index.html"))
    for candidate in tried:
        if os.path.exists(candidate):
            return candidate, True
    return tried[0], False


def main() -> int:
    dist = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "web/dist")
    print("qa_chrome_links: %s" % dist)

    pages = []
    for dirpath, _dirnames, filenames in os.walk(dist):
        for name in sorted(filenames):
            if name.endswith(".html"):
                pages.append(os.path.join(dirpath, name))
    pages.sort()

    if not pages:
        print("qa_chrome_links: FAIL — no HTML found under %s. An assertion "
              "with nothing to enumerate has failed, not passed." % dist)
        return 2

    seen = collections.Counter()          # target -> pages carrying it
    kinds = collections.Counter()
    off_base = []                         # (page, target)
    unresolved = []                       # (page, target, tried)
    n_refs = 0

    for page in pages:
        rel_page = os.path.relpath(page, dist)
        raw = open(page, encoding="utf-8", errors="replace").read()
        markup = served_markup(raw)
        page_targets = set()
        for target in targets(markup):
            n_refs += 1
            page_targets.add(target)
            kind, path = classify(target)
            kinds[kind] += 1
            if kind == "off-base":
                off_base.append((rel_page, target))
            elif kind == "internal":
                tried, ok = resolve(dist, path)
                if not ok:
                    unresolved.append(
                        (rel_page, target, os.path.relpath(tried, dist)))
            elif kind == "relative":
                base_dir = os.path.dirname(page)
                probe = os.path.join(base_dir, path.split("#")[0].split("?")[0])
                if not os.path.exists(probe) and not os.path.exists(
                        os.path.join(probe, "index.html")):
                    unresolved.append(
                        (rel_page, target, os.path.relpath(probe, dist)))
        for target in page_targets:
            seen[target] += 1

    n_pages = len(pages)
    chrome = sorted(t for t, n in seen.items() if n >= CHROME_SHARE * n_pages)

    print("qa_chrome_links: %d page(s) · %d pointer(s) · %d distinct target(s)"
          % (n_pages, n_refs, len(seen)))
    print("  by kind: " + " · ".join(
        "%s %d" % (k, kinds[k]) for k in
        ("internal", "external", "fragment", "off-base", "relative")
        if kinds[k] or k in ("internal", "off-base")))

    print("  chrome set — on >=%d%% of served pages, printed by name because "
          "the defect this file exists for was a chrome link:"
          % int(CHROME_SHARE * 100))
    if not chrome:
        print("    NONE — no target appears on nearly every page. On this site "
              "that is itself a defect: the layout emits a stylesheet, a "
              "favicon and a nav.")
        unresolved.append(("(site)", "(chrome set)", "empty"))
    for target in chrome:
        kind, path = classify(target)
        if kind == "internal":
            _tried, ok = resolve(dist, path)
            state = "resolves" if ok else "UNRESOLVED"
        else:
            state = kind
        print("    %-44s %4d/%d  %s" % (target[:44], seen[target], n_pages, state))

    if off_base:
        print("\nDEFECT — %d pointer(s) leave the base path %s and land on the "
              "host root, where this site does not exist:" % (len(off_base), BASE))
        for rel_page, target in off_base[:40]:
            print("  %s -> %s" % (rel_page, target))
        if len(off_base) > 40:
            print("  ... and %d more" % (len(off_base) - 40))

    if unresolved:
        print("\nDEFECT — %d internal pointer(s) do not resolve in dist:"
              % len(unresolved))
        for rel_page, target, tried in unresolved[:40]:
            print("  %s -> %s (tried %s)" % (rel_page, target, tried))
        if len(unresolved) > 40:
            print("  ... and %d more" % (len(unresolved) - 40))

    if off_base or unresolved:
        print("\nFAIL qa_chrome_links — %d off-base, %d unresolved."
              % (len(off_base), len(unresolved)))
        return 1

    print("\nCLEAN qa_chrome_links — every internal pointer the build emits "
          "resolves to a file the build emits, and none leaves %s." % BASE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
