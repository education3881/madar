#!/usr/bin/env python3
"""
qa_reachability — standing assertion: every published page can be REACHED by
following links from the home page.

WHY (Growth + Quality, 2026-08-25)
----------------------------------
Our sweeps have always asked "does this link resolve?" and "is this page in the
sitemap?". Neither question asks the one a crawler actually answers: starting at
the front door and following links, where can I get to?

VALENCE was published on 2026-08-08. It sat in the sitemap, it returned 200, and
every link on it resolved — so the 08-18 sweep recorded the orphan as CLEARED.
Nothing on the site linked to it. For 17 days it was reachable only by someone
who already knew the URL, which is the definition of unreachable for both a
crawler and a reader. A sitemap entry is a DECLARATION that a page exists; a
link is the EDGE that lets anything arrive. We had been auditing declarations.

This matters more than usual right now: as of 2026-08-24, 0 of 82 URLs are
indexed and the pages have never been crawled. The first crawler to arrive will
arrive at a link, and will then walk the graph. Anything off the graph stays
invisible even after the rest starts working.

PER-LANGUAGE ROOTS (added 2026-08-26)
------------------------------------
The first version of this check walked from ONE root, `/index.html`, which is
the ENGLISH front door. It therefore proved something narrower than it printed:
that every page is reachable *by a reader who is willing to pass through English
pages*. An Arabic reader does not arrive at `/`; they arrive at `/ar/`, and a
crawler fetching the Arabic sitemap entries walks the Arabic subgraph. If an
Arabic article were linked only from an English hub, this check would have
reported PASS while the Arabic edition had a hole in it — the same shape as the
08-17 orphan (a page in the sitemap that nothing points at), one language over.

So the walk now runs once per language root, CONFINED to that language's pages:
`/index.html` over the non-`/ar/` pages, `/ar/index.html` over the `/ar/` pages.
A language edition must be navigable on its own terms. The whole-site walk is
kept as the third pass, because a page can be language-neutral (VALENCE).

Proved both ways before being trusted, per ruling #35: on the real build the
Arabic subgraph is complete (40/40, max depth 2); on a build with the article
links severed from the two Arabic hubs it reports 12 orphans.

Exit codes: 0 clean · 1 orphans found · 2 nothing to check (a FAILURE, per the
08-16 silent-pass trap).
"""

from __future__ import annotations

import collections
import os
import re
import sys
from pathlib import Path

BASE = "/madar"
ROOT = "/index.html"
AR_ROOT = "/ar/index.html"

# Pages nothing is expected to link to from the site graph. Empty on purpose:
# if a page belongs on the site, something should point at it, and if nothing
# should point at it, it probably should not be published. Add entries here only
# with a reason, so the exemption is an argument rather than a silencer.
EXPECTED_ORPHANS: dict[str, str] = {
    "/404.html": (
        "The branded 404 (2026-09-09). It is reached by FAILURE, never by a link: "
        "GitHub Pages serves it for every unmatched URL under /madar/, including "
        "/ar/ paths. Linking to it from the site graph would be nonsense, and it "
        "carries noindex for the same reason it carries no canonical — it has no "
        "address of its own. This is the one page on the site whose orphanhood is "
        "the design; the allowlist is asserted to contain exactly this entry below."
    ),
}

# The allowlist itself is checked, because an exemption list is a place defects
# go to hide (08-09 flag-sweep inversion). Two ways: every exempted page must
# actually EXIST in dist — an exemption for a page we no longer build is a stale
# silencer — and the list must not grow without this line changing with it.
EXPECTED_ORPHAN_COUNT = 1


def normalise(href: str) -> str | None:
    """Map an href to the dist-relative HTML file it resolves to, or None."""
    href = href.split("#")[0].split("?")[0]
    if not href.startswith(BASE):
        return None  # external, mailto:, or a bare anchor
    path = href[len(BASE):] or "/"
    if not path.startswith("/"):
        path = "/" + path
    if path.endswith("/"):
        path += "index.html"
    elif not os.path.splitext(path)[1]:
        path += "/index.html"
    return path


def outbound(dist: Path, page: str) -> list[str]:
    f = dist / page.lstrip("/")
    if not f.exists():
        return []
    html = f.read_text(encoding="utf-8", errors="replace")
    out = []
    for m in re.finditer(r"<a\b[^>]*href=\"([^\"]+)\"", html):
        n = normalise(m.group(1))
        if n and n.endswith(".html") and (dist / n.lstrip("/")).exists():
            out.append(n)
    return out


def walk(dist: Path, root: str, universe: set[str]) -> dict[str, int]:
    """BFS from `root`, following only edges that land inside `universe`."""
    depth = {root: 0}
    queue = collections.deque([root])
    while queue:
        cur = queue.popleft()
        for nxt in outbound(dist, cur):
            if nxt in universe and nxt not in depth:
                depth[nxt] = depth[cur] + 1
                queue.append(nxt)
    return depth


def main() -> int:
    dist = Path(sys.argv[1] if len(sys.argv) > 1 else "web/dist")
    pages = {
        "/" + str(p.relative_to(dist))
        for p in dist.rglob("*.html")
    }
    if not pages:
        print(f"FAIL(2): no HTML under {dist} — nothing to check is not a pass.")
        return 2
    if ROOT not in pages:
        print(f"FAIL(2): no {ROOT} to start from.")
        return 2

    ar_pages = {p for p in pages if p.startswith("/ar/")}
    en_pages = pages - ar_pages

    # Each pass: (label, root, universe). A language edition must be navigable
    # WITHOUT leaving its own language; the whole-site pass catches the rest.
    passes = [
        ("English side, from /index.html", ROOT, en_pages),
        ("Arabic side, from /ar/index.html", AR_ROOT, ar_pages),
        ("whole site, from /index.html", ROOT, pages),
    ]

    failed = False
    for label, root, universe in passes:
        if not universe:
            print(f"FAIL(2): {label} — no pages in scope; nothing to check is not a pass.")
            return 2
        if root not in universe:
            print(f"FAIL(2): {label} — no {root} to start from.")
            return 2
        depth = walk(dist, root, universe)
        orphans = sorted(universe - set(depth) - set(EXPECTED_ORPHANS))
        hist = dict(sorted(collections.Counter(depth.values()).items()))
        print(
            f"{label}: pages {len(universe)} · reachable {len(depth)} · "
            f"orphans {len(orphans)} · depth {hist}"
        )
        for o in orphans:
            print(f"  ORPHAN {o} — reachable only from outside this language, or not at all.")
        failed = failed or bool(orphans)

    # Check the exemption list itself, both ways.
    if len(EXPECTED_ORPHANS) != EXPECTED_ORPHAN_COUNT:
        print(
            f"  ALLOWLIST DRIFT — {len(EXPECTED_ORPHANS)} exempted page(s), expected "
            f"{EXPECTED_ORPHAN_COUNT}. An orphan exemption is an argument; adding one "
            "means writing the reason AND moving this number."
        )
        failed = True
    for page, reason in sorted(EXPECTED_ORPHANS.items()):
        if not (dist / page.lstrip("/")).exists():
            print(f"  STALE EXEMPTION {page} — allowlisted but not built.")
            failed = True
        else:
            print(f"  exempt {page} — {reason.split('.')[0]}.")

    if failed:
        print("FAIL(1): a page nothing links to cannot be crawled or found.")
        return 1
    print("PASS: every page is reachable from its own language's front door.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
