#!/usr/bin/env python3
"""site_graph_depth — how many clicks from the front door to each published piece.

A MEASUREMENT AND NOT AN ASSERTION. No `qa_` prefix, outside the counting glob,
so no count in `CLAUDE.md` moves. It asserts nothing, per #93: the honest ceiling
for a reader's walk is an editorial judgment nobody here has made, and a floor
above today's reality would red every build.

WHY, AND WHAT IT IS NOT A DUPLICATE OF
--------------------------------------
`qa_reachability` gates the deploy and asserts that **every page is reachable
from its own language's front door** — a floor of ONE path. It passes whether the
path is one click or five. The 2026-08-17 orphan sweep asks the same question in
the other direction and is also satisfied by a single inbound edge.
`site_graph_indegree.py` (2026-11-23) counts how many pages point AT a piece, and
found `2026-07-06-morocco-ecoles-pionnieres` sitting on the floor at one inbound
rail with every gate green (standing-queue item 158).

None of those three is a DISTANCE. In-degree is a property of a node; depth is a
property of the walk a reader actually takes, and the two come apart: a piece
with one inbound rail from the home page is one click away, and a piece with
three inbound rails all from other articles can be three. **Nothing in this
operation has ever measured the distance**, which means the publication's own
answer to *is this worth walking?* has never been read.

METHOD
------
Breadth-first search over the built `dist`, per language, from that language's
own front door, following only same-origin links the pages actually render. The
graph is read out of the served bytes rather than out of the content collection,
because a rail that exists in frontmatter and is not rendered is not a path a
reader can take (the 2026-08-16 chrome rule's direction).

Exit 0 always unless the tree is unreadable: this prints, it does not judge.
"""
from __future__ import annotations

import collections
import html
import json
import pathlib
import re
import sys

LINK = re.compile(r"""(?is)<a\b[^>]*\bhref\s*=\s*("|')(.*?)\1""")
TAGS = re.compile(r"(?is)<(script|style)\b.*?</\1>")
BASE = "/madar/"
DOORS = (("en", "index.html"), ("ar", "ar/index.html"))


def page_key(rel: pathlib.Path) -> str:
    s = str(rel).replace("\\", "/")
    return s[: -len("index.html")].rstrip("/") or ""


def read_graph(dist: pathlib.Path) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for path in sorted(dist.rglob("index.html")):
        key = page_key(path.relative_to(dist))
        body = TAGS.sub(" ", path.read_text(encoding="utf-8", errors="replace"))
        out: set[str] = set()
        for _, href in LINK.findall(body):
            href = html.unescape(href.strip())
            if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
                continue
            if "://" in href:
                continue  # off-origin, and an absolute self-link is not a walk we own
            if not href.startswith(BASE):
                continue
            target = href[len(BASE):].split("#")[0].split("?")[0].strip("/")
            out.add(target)
        graph[key] = out
    return graph


def walk(graph: dict[str, set[str]], door: str) -> dict[str, int]:
    seen = {door: 0}
    queue = collections.deque([door])
    while queue:
        node = queue.popleft()
        for nxt in sorted(graph.get(node, ())):
            if nxt in graph and nxt not in seen:
                seen[nxt] = seen[node] + 1
                queue.append(nxt)
    return seen


def main(argv: list[str]) -> int:
    root = pathlib.Path(argv[1]).resolve() if len(argv) > 1 else pathlib.Path.cwd()
    dist = root / "web" / "dist"
    if not dist.is_dir():
        print(f"CANNOT MEASURE site_graph_depth — no dist at {dist}; run npm run build")
        return 2
    graph = read_graph(dist)
    print(f"site_graph_depth — {len(graph)} routed page(s) read out of dist, "
          f"{sum(len(v) for v in graph.values())} rendered same-origin link(s)")

    report: dict[str, dict] = {}
    for lang, door_file in DOORS:
        door = page_key(pathlib.Path(door_file))
        if door not in graph:
            print(f"  {lang}: no front door at {door_file}")
            continue
        depths = walk(graph, door)
        arts = {k: d for k, d in depths.items()
                if re.match(r"^(ar/)?articles(-ar)?/", k)}
        hist = collections.Counter(arts.values())
        unreached = [k for k in graph
                     if re.match(r"^(ar/)?articles(-ar)?/", k) and k not in depths
                     and (k.startswith("ar/") == (lang == "ar"))]
        print(f"\n  {lang.upper()} front door → {len(arts)} article page(s) reached, "
              f"{len(unreached)} not reached from this door")
        # SPLIT BY THE TARGET'S OWN EDITION, because the first reading pooled them
        # and the pooled number is not a reader's experience: the English front
        # door reaches all 92 article pages of BOTH editions, and every one of the
        # deepest was an Arabic page reached through its English pair's language
        # switch. A depth histogram over two editions from one door measures the
        # bilingual rails, not the walk. (#111's denominator lesson, on a graph.)
        own = {k: d for k, d in arts.items() if k.startswith("ar/") == (lang == "ar")}
        other = {k: d for k, d in arts.items() if k.startswith("ar/") != (lang == "ar")}
        print(f"    own edition {len(own)} · other edition {len(other)}")
        for label, group in (("own", own), ("other", other)):
            h = collections.Counter(group.values())
            print(f"    {label:<6} " + " · ".join(f"{d} click(s): {n}" for d, n in sorted(h.items())))
        for d in sorted(hist):
            print(f"    {d} click(s) {'':<2} {hist[d]:>4}")
        deepest = sorted(arts.items(), key=lambda kv: (-kv[1], kv[0]))[:6]
        print("    deepest:")
        for k, d in deepest:
            print(f"      {d}  {k}")
        report[lang] = {"reached": len(arts), "histogram": dict(sorted(hist.items())),
                        "deepest": deepest, "unreached": sorted(unreached)}

    out = root / "agents" / "stats" / "site-graph-depth.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\n  written to {out.relative_to(root)}")
    print("  PRINTED AND NOT ASSERTED (#93): the honest ceiling for a reader's walk is an "
          "editorial judgment nobody here has made.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
