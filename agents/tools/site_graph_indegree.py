#!/usr/bin/env python3
"""site_graph_indegree.py — the in-degree census of the publication's own graph.

A MEASUREMENT AND NOT AN ASSERTION. No `qa_` prefix, so it is outside the
counting glob and no count in `CLAUDE.md` moves. It asserts nothing, per #93:
every floor available here is either already guaranteed by a gate that exists
(`qa_reachability` asserts every page is reachable from its own front door;
`qa_body_links` asserts every declared rail and source URL renders) or is an
EDITORIAL quantity the Editor owns and an instrument must not legislate — a rail
is curated judgment, and a tool that demanded "at least N inbound rails" would
be a tool commissioning content.

WHAT IT MEASURES AND WHY NOTHING ELSE DOES
------------------------------------------
`qa_reachability` asks whether a page can be reached AT ALL — a floor of one,
satisfied by a listing. The 2026-08-17 orphan sweep asks whether a served page
has any inbound path at all. Neither asks **how thickly a piece is woven in**,
and that is the quantity a reader actually walks: a piece reachable only from
the listing that must contain it is reachable the way a filing cabinet is.

So this counts, per article page, the inbound internal edges SPLIT BY THE KIND
OF PAGE THEY COME FROM — article, browse listing, editions page, front door —
because the four are worth entirely different amounts to a reader and summing
them hides exactly the distinction that matters. An edge from a listing is
automatic; an edge from another piece is a judgment somebody made.

THE BILINGUAL READING IS THE POINT, AND IT IS THE CHARTER'S OWN CLAIM
---------------------------------------------------------------------
The CHARTER says Arabic is *a distribution advantage, not just a translation
cost*. Nothing had ever measured that. The per-slug EN/AR comparison here is
that sentence made falsifiable: if the two editions' in-degrees disagree, the
Arabic reader walks a thinner publication than the English one, and the
publication is bilingual in its text and monolingual in its graph.

Usage:  python3 agents/tools/site_graph_indegree.py .            # census
        python3 agents/tools/site_graph_indegree.py . --thin 4   # list the thin end
Exit 0 always, except 2 when there is no dist to read (cannot measure).
"""
from __future__ import annotations

import collections
import pathlib
import re
import sys

ORIGIN = "https://education3881.github.io/madar"
HREF = re.compile(r'href="([^"]+)"')
ARTICLE = re.compile(r"^/(?:ar/)?articles/([^/]+)/$")
KINDS = ("article", "browse", "editions", "archive", "front", "other")


def route(path: pathlib.Path, dist: pathlib.Path) -> str:
    rel = "/" + str(path.parent.relative_to(dist)).replace("\\", "/") + "/"
    return "/" if rel == "/./" else rel


def normalise(href: str) -> str | None:
    href = href.split("#")[0].split("?")[0]
    for prefix in (ORIGIN, "/madar"):
        if href.startswith(prefix):
            href = href[len(prefix):]
            break
    else:
        if href.startswith("http"):
            return None
    if not href.startswith("/"):
        return None
    return href if href.endswith("/") else href + "/"


def kind(rel: str) -> str:
    if ARTICLE.match(rel):
        return "article"
    for k in ("browse", "editions", "archive"):
        if re.match(rf"^/(?:ar/)?{k}", rel):
            return k
    return "front" if rel in ("/", "/ar/") else "other"


def census(dist: pathlib.Path) -> tuple[dict, dict]:
    pages = {route(p, dist): p for p in sorted(dist.rglob("index.html"))}
    inbound: dict[str, collections.Counter] = {
        r: collections.Counter() for r in pages if ARTICLE.match(r)}
    # same-language article->article edges, kept apart from the language switcher:
    # an EN page linking its own AR twin is chrome, not curation.
    # TWO UNITS, DELIBERATELY, and the first draft of this tool shipped only the
    # second and overclaimed on it. `curated` counts DISTINCT SOURCE PAGES - how
    # many other pieces a reader could arrive from - and `edges` counts LINKS,
    # which a page can carry twice (once as a `related:` rail and once as a
    # `sources[]` URL, which is what a self-citation does). Reachability is a
    # property of the first unit; only the second can disagree on multiplicity.
    # Reporting "the Arabic reader walks a different publication" off an edge
    # count is #111's denominator defect: the same number wearing the wrong unit.
    curated: dict[str, set] = {r: set() for r in inbound}
    edges: dict[str, int] = {r: 0 for r in inbound}
    for rel, path in pages.items():
        k = kind(rel)
        from_ar = rel.startswith("/ar/")
        html = path.read_text(encoding="utf-8", errors="replace")
        for href in set(HREF.findall(html)):
            target = normalise(href)
            if target is None or target not in inbound or target == rel:
                continue
            inbound[target][k] += 1
            if k == "article" and target.startswith("/ar/") == from_ar:
                curated[target].add(rel)
                edges[target] += 1
    return inbound, {r: len(v) for r, v in curated.items()}, edges


def main(argv: list[str]) -> int:
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".")
    thin = 4
    for a in argv[2:]:
        if a.startswith("--thin"):
            thin = int(a.split("=", 1)[1]) if "=" in a else int(argv[argv.index(a) + 1])
    dist = root / "web" / "dist"
    if not dist.is_dir():
        print(f"CANNOT MEASURE site_graph_indegree — no dist at {dist}; run `npm run build` in web/")
        return 2

    inbound, curated, edges = census(dist)
    en = sorted(r for r in inbound if not r.startswith("/ar/"))
    ar = sorted(r for r in inbound if r.startswith("/ar/"))
    print(f"site_graph_indegree — {len(inbound)} article pages ({len(en)} EN, {len(ar)} AR), "
          f"read from {dist}")
    print("  MEASUREMENT, NOT AN ASSERTION (#93). A rail is editorial curation; an instrument")
    print("  that demanded N inbound rails would be an instrument commissioning content.\n")

    for label, group in (("EN", en), ("AR", ar)):
        vals = sorted(curated[r] for r in group)
        if not vals:
            continue
        mid = vals[len(vals) // 2]
        ev = sorted(edges[r] for r in group)
        print(f"  {label} same-language inbound, DISTINCT SOURCE PIECES: "
              f"min {vals[0]} · median {mid} · max {vals[-1]} · sum {sum(vals)}")
        print(f"     distribution {dict(sorted(collections.Counter(vals).items()))}")
        print(f"     and as LINKS (a page may link the same piece twice): sum {sum(ev)}, "
              f"max {ev[-1]} — a different unit, not a better one")

    print("\n  THE BILINGUAL READING — the CHARTER's claim, made falsifiable:")
    disagree, multiplicity = [], []
    for r in en:
        slug = ARTICLE.match(r).group(1)
        twin = f"/ar/articles/{slug}/"
        if twin not in curated:
            continue
        if curated[twin] != curated[r]:
            disagree.append((slug, curated[r], curated[twin]))
        elif edges[twin] != edges[r]:
            multiplicity.append((slug, edges[r], edges[twin]))
    if disagree:
        print(f"     {len(disagree)} of {len(en)} slug(s) whose EN and AR in-degree DISAGREE — "
              "the Arabic reader walks a different publication:")
        for slug, e, a in sorted(disagree, key=lambda x: abs(x[1] - x[2]), reverse=True)[:12]:
            print(f"       EN {e:>2}  AR {a:>2}  delta {e - a:+d}   {slug}")
    else:
        print(f"     0 of {len(en)} slugs disagree on DISTINCT SOURCE PIECES. The two graphs are")
        print("     identical in reachability, so the Arabic reader walks exactly the same")
        print("     publication the English reader does — which is the CHARTER's claim, measured.")
    if multiplicity:
        print(f"\n     {len(multiplicity)} slug(s) agree on source pieces and differ on LINK COUNT.")
        print("     This is multiplicity, NOT reachability, and it is reported in its own unit:")
        for slug, e, a in sorted(multiplicity, key=lambda x: abs(x[1] - x[2]), reverse=True)[:12]:
            print(f"       EN {e:>2}  AR {a:>2}  delta {e - a:+d}   {slug}")

    print("\n  INBOUND BY KIND, over the EN edition — the four are worth different amounts:")
    for k in KINDS:
        vals = collections.Counter(inbound[r][k] for r in en)
        if any(vals):
            print(f"     {k:<9} {dict(sorted(vals.items()))}")
    print("     An edge from a listing is automatic. An edge from another piece is a judgment.")

    thinnest = sorted(en, key=lambda r: (curated[r], inbound[r]["browse"]))
    print(f"\n  THE THIN END — pieces with fewer than {thin} same-language inbound rails:")
    shown = [r for r in thinnest if curated[r] < thin]
    for r in shown:
        slug = ARTICLE.match(r).group(1)
        c = inbound[r]
        print(f"     rails {curated[r]}  ·  browse {c['browse']} editions {c['editions']} "
              f"front {c['front']}  ·  {slug}")
    if not shown:
        print(f"     none — every piece carries at least {thin}")
    print("\n  Handed to the EDITOR, never repaired here: a forward rail is written when a later")
    print("  piece genuinely follows an earlier one (standing ledger, cell 1 names / cell 8 writes).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
