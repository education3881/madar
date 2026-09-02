#!/usr/bin/env python3
"""qa_robots — the inbound half of discoverability.

Asserts, against a built dist/:
  1. robots.txt EXISTS in dist (a site with no robots.txt leaves crawler
     behaviour to defaults and its sitemap unadvertised).
  2. It contains exactly one Sitemap: line, and that line's URL is DERIVED
     from the build's own contract — site + base from astro.config.* — not
     hand-asserted (ruling #36: a promise must be derived from the asset it
     promises). The advertised file must also EXIST in dist (ruling #37:
     asserted by existence).
  3. No Disallow: line blocks anything we serve. The only acceptable
     Disallow value is the empty string (which by spec allows everything).
  4. The legacy /sitemap.xml stub, if present, must point at a sitemap file
     that exists in dist (a bookmarked URL that redirects to a 404 is worse
     than none).

Proved per ruling #35 on first landing: bites on a dist with robots.txt
removed, bites on a Disallow: /ar/ injection, silent on the real build.

Usage: qa_robots.py <dist-dir> [--config <astro-config-path>]
Exit 0 = PASS, 1 = defects found, 2 = could not check (counts as failure:
an assertion that finds nothing to check has failed, not passed).
"""
import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: qa_robots.py <dist-dir> [--config <astro-config>]")
        return 2
    dist = Path(sys.argv[1])
    config_path = None
    if "--config" in sys.argv:
        config_path = Path(sys.argv[sys.argv.index("--config") + 1])
    else:
        # derive: dist/../astro.config.mjs (the build's own contract)
        for cand in ("astro.config.mjs", "astro.config.ts", "astro.config.js"):
            p = dist.parent / cand
            if p.exists():
                config_path = p
                break
    if not dist.is_dir():
        print(f"FAIL(2): dist not found at {dist}")
        return 2
    if config_path is None or not config_path.exists():
        print("FAIL(2): astro config not found — expected sitemap URL cannot be DERIVED")
        return 2

    defects = []

    # -- derive the expected sitemap URL from the build's own contract
    cfg = config_path.read_text(encoding="utf-8")
    m_site = re.search(r"site:\s*['\"]([^'\"]+)['\"]", cfg)
    m_base = re.search(r"base:\s*['\"]([^'\"]+)['\"]", cfg)
    if not m_site:
        print("FAIL(2): no site: in astro config — cannot derive")
        return 2
    site = m_site.group(1).rstrip("/")
    base = (m_base.group(1) if m_base else "").strip("/")
    expected_sitemap = f"{site}/{base}/sitemap-index.xml" if base else f"{site}/sitemap-index.xml"

    # -- 1. robots.txt exists
    robots = dist / "robots.txt"
    if not robots.exists():
        print(f"DEFECT: robots.txt missing from dist ({robots})")
        print("qa_robots: 1 defect")
        return 1
    text = robots.read_text(encoding="utf-8")

    # -- 2. exactly one Sitemap line, derived URL, advertised file exists
    sitemap_lines = [l.split(":", 1)[1].strip() for l in text.splitlines()
                     if l.lower().startswith("sitemap:")]
    if len(sitemap_lines) != 1:
        defects.append(f"expected exactly 1 Sitemap: line, found {len(sitemap_lines)}")
    else:
        advertised = sitemap_lines[0]
        if advertised != expected_sitemap:
            defects.append(
                f"Sitemap URL drift: robots advertises {advertised}, "
                f"build contract derives {expected_sitemap}")
        if not (dist / "sitemap-index.xml").exists():
            defects.append("advertised sitemap-index.xml does not exist in dist")

    # -- 3. no effective Disallow
    for l in text.splitlines():
        if l.lower().startswith("disallow:"):
            val = l.split(":", 1)[1].strip()
            if val:
                defects.append(f"robots.txt disallows a path we serve: '{val}'")

    # -- 4. legacy stub, if present, must point at files that exist
    legacy = dist / "sitemap.xml"
    if legacy.exists():
        for loc in re.findall(r"<loc>([^<]+)</loc>", legacy.read_text(encoding="utf-8")):
            fname = loc.rsplit("/", 1)[-1]
            if not (dist / fname).exists():
                defects.append(f"legacy sitemap.xml points at {fname}, absent from dist")

    if defects:
        for d in defects:
            print("DEFECT:", d)
        print(f"qa_robots: {len(defects)} defect(s)")
        return 1
    print(f"qa_robots: PASS — robots.txt present, 1 Sitemap line == derived "
          f"{expected_sitemap}, target exists, 0 disallows, legacy stub resolves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
