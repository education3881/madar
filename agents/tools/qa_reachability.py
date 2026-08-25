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

# Pages nothing is expected to link to from the site graph. Empty on purpose:
# if a page belongs on the site, something should point at it, and if nothing
# should point at it, it probably should not be published. Add entries here only
# with a reason, so the exemption is an argument rather than a silencer.
EXPECTED_ORPHANS: dict[str, str] = {}


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

    depth = {ROOT: 0}
    queue = collections.deque([ROOT])
    while queue:
        cur = queue.popleft()
        for nxt in outbound(dist, cur):
            if nxt not in depth:
                depth[nxt] = depth[cur] + 1
                queue.append(nxt)

    orphans = sorted(pages - set(depth) - set(EXPECTED_ORPHANS))
    hist = dict(sorted(collections.Counter(depth.values()).items()))

    print(f"pages: {len(pages)} · reachable from {ROOT}: {len(depth)} · orphans: {len(orphans)}")
    print(f"click-depth histogram: {hist}")
    if orphans:
        for o in orphans:
            print(f"  ORPHAN {o} — in the sitemap, and nothing links to it.")
        print("FAIL(1): a page nothing links to cannot be crawled or found.")
        return 1
    print("PASS: every page is reachable by following links from the home page.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
