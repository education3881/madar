#!/usr/bin/env python3
"""qa_hreflang_clusters — the cluster a crawler reassembles must equal the
sitemap's own URL set.

The 09-01 forward question: qa_robots asserts one sitemap for both languages,
qa_consumer_surface counts hreflang links, qa_jsonld dereferences translation
links — but nothing has ever asserted that the hreflang CLUSTERS a crawler
reassembles from our pages match the sitemap's URL set. A cluster is the unit
a search engine indexes a bilingual pair by; a URL in a cluster the sitemap
omits, or a sitemap URL in two clusters, or a one-way alternate, each silently
splits a pair into two unrelated pages.

Asserts, against a built dist/:
  1. Every page-level cluster (the set of hreflang en/ar hrefs a page emits)
     is INTERNALLY CONSISTENT: it names its own canonical URL, every member
     DEREFERENCES to a file in dist (ruling #37), and x-default, if present,
     is a member.
  2. Every cluster is RECIPROCAL: each member page emits the identical
     cluster (a one-way alternate is a broken promise the other page never
     made).
  3. Every sitemap URL appears in EXACTLY ONE cluster, or in none — and the
     "none" set is ASSERTED, not merely printed: NO_ALTERNATE_ALLOWED below
     names the pages that legitimately have no Arabic twin (About: the Arabic
     About is a section of the Arabic home, /ar/#about, since the 08-18 nav
     fix; VALENCE: a standalone English instrument). A no-alternate page
     outside that list is a DEFECT (an EN page shipped without its AR twin,
     or a held slug leaking one-sided); an allowlisted page that now HAS
     alternates is also a DEFECT (a stale allowlist is a green light wired
     to nothing — the 09-03 forward question, 08-16 silent-pass family).
     Either give the page its twin or edit the list in the same commit.
  4. No cluster names a URL the sitemap omits (a held or parked page leaking
     through hreflang would be caught here even if the sitemap was clean).
  5. The sitemap's own xhtml:link alternates agree with the page-level
     cluster for that URL (two declarations of one promise must not drift —
     ruling #36 applied across two files).

Proved per ruling #35 on first landing (2026-09-03): silent on the real build
(82 URLs, 40 clusters, 2 no-alternate pages); bites on a synthetic dist where
one Arabic page's `hreflang="en"` href is retargeted (reciprocity + sitemap
disagreement), and on a synthetic dist where a held slug's cluster is injected
into a page (URL absent from sitemap). Allowlist assertion added 2026-09-04
and proved both ways: control silent; bite 3 = a third no-alternate page
(About duplicated as a sitemap URL) → FAIL naming it; bite 4 = About removed
from the allowlist while still no-alternate → FAIL naming it.

Usage: qa_hreflang_clusters.py <dist-dir>
Exit 0 = PASS, 1 = defects found, 2 = could not check (counts as failure:
an assertion that finds nothing to check has failed, not passed).
"""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r'<link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"\s*/?>')
CANON_RE = re.compile(r'<link\s+rel="canonical"\s+href="([^"]+)"\s*/?>')
URL_BLOCK_RE = re.compile(r"<url>(.*?)</url>", re.S)
LOC_RE = re.compile(r"<loc>(.*?)</loc>")
XHTML_RE = re.compile(r'<xhtml:link\s+rel="alternate"\s+hreflang="([^"]+)"\s+href="([^"]+)"\s*/?>')

# Pages allowed to have no hreflang alternates, as site-root-relative paths.
# Edit this list in the SAME commit as the page it describes (see docstring 3).
NO_ALTERNATE_ALLOWED: frozenset[str] = frozenset({
    "about/",    # Arabic About lives at /ar/#about (section of the AR home), not a page
    "valence/",  # standalone English instrument under public/, no AR edition
})


def url_to_dist(url: str, site_root: str, dist: Path) -> Path | None:
    if not url.startswith(site_root):
        return None
    rel = url[len(site_root):].lstrip("/")
    p = dist / rel
    if p.is_dir():
        p = p / "index.html"
    return p


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: qa_hreflang_clusters.py <dist-dir>")
        return 2
    dist = Path(sys.argv[1])
    sitemaps = [p for p in dist.glob("sitemap-*.xml") if p.name != "sitemap-index.xml"]
    if not dist.is_dir() or not sitemaps:
        print(f"FATAL: dist or sitemap not found under {dist}")
        return 2

    # --- sitemap: URL set + its own declared clusters
    sitemap_urls: set[str] = set()
    sitemap_clusters: dict[str, frozenset[str]] = {}
    for sm in sitemaps:
        text = sm.read_text(encoding="utf-8")
        for block in URL_BLOCK_RE.findall(text):
            loc = LOC_RE.search(block)
            if not loc:
                continue
            u = loc.group(1).strip()
            sitemap_urls.add(u)
            alts = {href for lang, href in XHTML_RE.findall(block) if lang in ("en", "ar")}
            if alts:
                sitemap_clusters[u] = frozenset(alts)
    if not sitemap_urls:
        print("FATAL: sitemap enumerated zero URLs — nothing to check is a failure")
        return 2
    # site root = longest common prefix of all sitemap URLs up to the base path
    sample = sorted(sitemap_urls)[0]
    m = re.match(r"(https?://[^/]+/[^/]+/)", sample)
    site_root = m.group(1) if m else sample
    if not all(u.startswith(site_root) for u in sitemap_urls):
        # fall back to scheme+host only
        site_root = re.match(r"(https?://[^/]+/)", sample).group(1)

    # --- pages: page-level clusters
    defects: list[str] = []
    page_clusters: dict[str, frozenset[str]] = {}   # canonical -> cluster
    no_alt_pages: list[str] = []
    pages = sorted(p for p in dist.rglob("*.html"))
    for page in pages:
        html = page.read_text(encoding="utf-8", errors="replace")
        canon_m = CANON_RE.search(html)
        canon = canon_m.group(1) if canon_m else None
        alts = {href for lang, href in LINK_RE.findall(html) if lang in ("en", "ar")}
        xdef = [href for lang, href in LINK_RE.findall(html) if lang == "x-default"]
        rel = str(page.relative_to(dist))
        if not alts:
            if canon and canon in sitemap_urls:
                no_alt_pages.append(canon)
            continue
        if not canon:
            defects.append(f"{rel}: emits hreflang but no canonical")
            continue
        cluster = frozenset(alts)
        # 1. internal consistency
        if canon not in cluster:
            defects.append(f"{rel}: cluster {sorted(cluster)} does not name its own canonical {canon}")
        for member in cluster:
            target = url_to_dist(member, site_root, dist)
            if target is None or not target.is_file():
                defects.append(f"{rel}: alternate {member} does not dereference to dist")
        for xd in xdef:
            if xd not in cluster:
                defects.append(f"{rel}: x-default {xd} is not a cluster member")
        page_clusters[canon] = cluster

    # 2. reciprocity
    for canon, cluster in page_clusters.items():
        for member in cluster:
            other = page_clusters.get(member)
            if other is None:
                if member != canon:
                    defects.append(f"{canon}: names {member}, which emits no cluster (one-way alternate)")
            elif other != cluster:
                defects.append(f"{canon}: cluster {sorted(cluster)} != {member}'s cluster {sorted(other)} (not reciprocal)")

    # 3. every sitemap URL in exactly one cluster, or none (named)
    distinct_clusters = set(page_clusters.values())
    membership: dict[str, int] = {u: 0 for u in sitemap_urls}
    for cl in distinct_clusters:
        for member in cl:
            if member in membership:
                membership[member] += 1
            else:
                # 4. cluster names a URL the sitemap omits
                defects.append(f"cluster {sorted(cl)} names {member}, absent from the sitemap")
    multi = [u for u, n in membership.items() if n > 1]
    for u in multi:
        defects.append(f"{u}: appears in {membership[u]} distinct clusters")
    zero = sorted(u for u, n in membership.items() if n == 0)
    unexpected_zero = [u for u in zero if u not in no_alt_pages]
    for u in unexpected_zero:
        defects.append(f"{u}: in sitemap, in no cluster, and its page emits no hreflang — unnamed no-alternate page")

    # 3b. the no-alternate set is asserted against the allowlist, both ways
    def _rel(u: str) -> str:
        return u[len(site_root):] if u.startswith(site_root) else u
    for u in sorted(no_alt_pages):
        if _rel(u) not in NO_ALTERNATE_ALLOWED:
            defects.append(
                f"{u}: no-alternate page NOT in NO_ALTERNATE_ALLOWED — an EN page without its AR twin "
                f"(or a one-sided leak); give it a twin or list it in the same commit")
    present_rel = {_rel(u) for u in no_alt_pages}
    for allowed in sorted(NO_ALTERNATE_ALLOWED):
        if allowed not in present_rel:
            state = ("now emits alternates" if (site_root + allowed) in page_clusters
                     else "is not a sitemap URL / not built")
            defects.append(
                f"{site_root + allowed}: listed in NO_ALTERNATE_ALLOWED but {state} — stale allowlist entry; "
                f"edit the list in the same commit")

    # 5. sitemap-declared clusters agree with page-level clusters
    for u, sm_cluster in sitemap_clusters.items():
        pc = page_clusters.get(u)
        if pc is None:
            defects.append(f"{u}: sitemap declares alternates {sorted(sm_cluster)} but the page emits none")
        elif pc != sm_cluster:
            defects.append(f"{u}: sitemap cluster {sorted(sm_cluster)} != page cluster {sorted(pc)}")
    for u, pc in page_clusters.items():
        if u in sitemap_urls and u not in sitemap_clusters:
            defects.append(f"{u}: page emits cluster {sorted(pc)} but the sitemap entry declares no alternates")

    print(
        f"qa_hreflang_clusters: sitemap URLs {len(sitemap_urls)} · pages {len(pages)} · "
        f"clusters {len(distinct_clusters)} · no-alternate pages {len(no_alt_pages)} "
        f"({', '.join(sorted(no_alt_pages)) or '—'})"
    )
    if defects:
        for d in defects:
            print(f"  DEFECT {d}")
        print(f"FAIL({len(defects)})")
        return 1
    print("PASS — every cluster is reciprocal, dereferences to dist, and is the sitemap's own set; no cluster names a URL the sitemap omits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
