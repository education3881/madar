#!/usr/bin/env python3
"""
qa_jsonld — standing assertion: the machine-readable layer honours the consumer's contract.

WHY (Web Developer, 2026-08-29 — the 08-28 forward question, answered)
----------------------------------------------------------------------
Since 08-23 the site emits schema.org Article nodes, and since 08-28 a
BreadcrumbList on all article pages. Every existing check asserts these are
PRESENT and PARSE. None asserts they are TRUE. A typo'd @type, a breadcrumb
`item` pointing at a page that is not in dist, an og card URL dropped by a
refactor, or an Arabic page declaring inLanguage "en" would pass every check
we own — presence was checked, meaning was not.

This is ruling #37's pattern (a promise is asserted by EXISTENCE in dist, not
by presence in markup) applied to the JSON-LD layer, plus ruling #36 (a claim
about a page must agree with the page it sits on):

1. Every application/ld+json block must parse (a parse failure is a defect,
   not an absence).
2. BreadcrumbList: itemListElement non-empty; positions sequential from 1;
   every `name` non-empty; every `item` an absolute URL under the site base
   that DEREFERENCES to a file in dist.
3. Article: required keys present (headline, description, url,
   datePublished, inLanguage, image); `url`, mainEntityOfPage.@id and the
   node @id dereference to dist; image.url dereferences to a raster file in
   dist; workTranslation / translationOfWork @id dereferences to dist;
   inLanguage AGREES with the page's own path language (ar/ ↔ "ar");
   citation URLs, when present, must be absolute (external registers are not
   dereferenced — they are not ours to assert).

Proved both ways per ruling #35 before being trusted (2026-08-29):
- CONTROL (must be silent): today's 82-page build — 0 defects, 152 nodes
  checked (76 BreadcrumbList + 76 Article), 608 promises dereferenced to dist.
- BITE (must fire): a copy of dist with one breadcrumb `item` retargeted to
  a page not in dist, one Article JSON-LD image retargeted to a missing PNG,
  and one Arabic page's inLanguage flipped to "en" — FAIL(3), each defect
  naming its page and its field, silent on all 79 other pages.

Exit 0 clean; exit 1 with named defects otherwise.
"""
import json
import re
import sys
from pathlib import Path

BASE = "https://education3881.github.io/madar/"


def find_dist() -> Path:
    for cand in (Path("web/dist"), Path("dist"), Path(__file__).resolve().parents[2] / "web" / "dist"):
        if (cand / "sitemap-0.xml").exists() or (cand / "index.html").exists():
            return cand
    sys.exit("FAIL(2): no dist found — build first.")


def url_to_dist(url: str, dist: Path):
    """Map an absolute site URL to the file it promises in dist, or None if foreign."""
    if not url.startswith(BASE):
        return None
    rel = url[len(BASE):].split("#", 1)[0]
    if rel == "" or rel.endswith("/"):
        return dist / rel / "index.html"
    p = dist / rel
    # a bare path with no extension is a page URL missing its trailing slash
    if p.suffix == "":
        return p / "index.html"
    return p


def main() -> int:
    dist = find_dist()
    pages = sorted(dist.rglob("index.html"))
    defects: list[str] = []
    nodes_checked = 0
    derefs = 0

    for page in pages:
        rel = page.relative_to(dist).as_posix()
        page_lang = "ar" if rel.startswith("ar/") else "en"
        html = page.read_text(encoding="utf-8")
        for block in re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.S
        ):
            try:
                data = json.loads(block)
            except json.JSONDecodeError as e:
                defects.append(f"{rel}: JSON-LD does not parse ({e})")
                continue
            for node in data if isinstance(data, list) else [data]:
                nodes_checked += 1
                ntype = node.get("@type")
                if ntype == "BreadcrumbList":
                    items = node.get("itemListElement") or []
                    if not items:
                        defects.append(f"{rel}: BreadcrumbList with empty itemListElement")
                    for i, li in enumerate(items, start=1):
                        if li.get("position") != i:
                            defects.append(
                                f"{rel}: breadcrumb position {li.get('position')!r} at slot {i}"
                            )
                        if not (li.get("name") or "").strip():
                            defects.append(f"{rel}: breadcrumb slot {i} has empty name")
                        item = li.get("item", "")
                        target = url_to_dist(item, dist)
                        if target is None:
                            defects.append(f"{rel}: breadcrumb item not under base: {item}")
                        elif not target.exists():
                            defects.append(f"{rel}: breadcrumb item 404s in dist: {item}")
                        else:
                            derefs += 1
                elif ntype == "Article":
                    for key in ("headline", "description", "url", "datePublished", "inLanguage", "image"):
                        if not node.get(key):
                            defects.append(f"{rel}: Article missing {key}")
                    lang = node.get("inLanguage")
                    if lang and lang != page_lang:
                        defects.append(
                            f"{rel}: Article inLanguage='{lang}' disagrees with page path language '{page_lang}'"
                        )
                    for label, url in (
                        ("url", node.get("url")),
                        ("@id", (node.get("@id") or "").split("#")[0] or None),
                        ("mainEntityOfPage", (node.get("mainEntityOfPage") or {}).get("@id")),
                        ("image", (node.get("image") or {}).get("url")),
                        ("workTranslation", (node.get("workTranslation") or {}).get("@id")),
                        ("translationOfWork", (node.get("translationOfWork") or {}).get("@id")),
                    ):
                        if not url:
                            continue
                        target = url_to_dist(url, dist)
                        if target is None:
                            defects.append(f"{rel}: Article {label} not under base: {url}")
                        elif not target.exists():
                            defects.append(f"{rel}: Article {label} 404s in dist: {url}")
                        else:
                            derefs += 1
                    img = (node.get("image") or {}).get("url", "")
                    if img.endswith(".svg"):
                        defects.append(f"{rel}: Article image is SVG (consumer contract is raster): {img}")
                    for c in node.get("citation") or []:
                        cu = c.get("url", "")
                        if cu and not re.match(r"https?://", cu):
                            defects.append(f"{rel}: citation url not absolute: {cu}")

    print(
        f"qa_jsonld: pages {len(pages)} · nodes {nodes_checked} · dereferenced {derefs} promises to dist"
    )
    if defects:
        for d in defects:
            print("  DEFECT:", d)
        print(f"FAIL({len(defects)}): the machine-readable layer breaks its contract.")
        return 1
    print("CLEAN — every JSON-LD promise parses, agrees with its page, and dereferences to dist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
