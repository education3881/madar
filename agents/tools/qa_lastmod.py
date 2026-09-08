#!/usr/bin/env python3
"""qa_lastmod — a held draft may not date a page a reader can reach.

WHY (2026-09-08, from the 2026-09-06 weekly review)

`sitemapLastmod.mjs` resolved the five index pages as max(chrome, newest file
under src/content/) with no regard to `approved:`. A held draft is a file in the
content directory and not a byte of served output, so a commit touching only a
held draft moved five live <lastmod> values and told every crawler the site had
changed when nothing reachable had. It reached production twice — 9886987
(08-30, held Sierra Leone AR only) and 642fef2 (09-02, held Sudan EN only).

The existing held-leak sweep was green through both, because it asserted zero
held SLUGS in the sitemap and a held slug never has a URL to leak. It never
enumerated DATES. Sixth member of the enumeration family: an assertion that
checks one shape of a leak does not check the leak.

WHAT THIS ASSERTS, against a built dist/ and the repo's own git history:

  1. Every <loc> in the sitemap carries a <lastmod>. (A sitemap that quietly
     loses its lastmod is the 08-24 regression; absence is the failure the
     resolver's own guards exist to prevent, re-checked here from the output.)
  2. No <lastmod> is NEWER than the ceiling, where the ceiling is
        max(newest commit touching an approved content file,
            newest commit touching a chrome file)
     Anything above that ceiling can only have come from a held draft, from
     build time, or from thin air — the three fabrications the resolver's
     module head rejects by name.
  3. No <lastmod> is in the future relative to now (a clock or timezone fault).
  4. The ceiling itself resolves — an empty approved set or an empty chrome set
     means the check has nothing to check, which is a failure, not a pass
     (the 08-16 silent-pass trap).

This is the OUTPUT-side twin of the resolver's input-side guards. The resolver
can be correct and the emitted sitemap still wrong (a stale dist, a serialize
hook that drops the field, an integration upgrade); ruling #16 says judge in the
environment that judges, and the environment that judges lastmod is the file a
crawler fetches.

Proved per ruling #35 on landing: bites on a sitemap with an injected
above-ceiling date, bites on a sitemap with a lastmod stripped, silent on the
real build.

Usage: qa_lastmod.py <dist-dir> [--repo <repo-root>]
Exit 0 = PASS, 1 = defects found, 2 = could not check (counts as failure).
"""
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CONTENT_DIRS = ("web/src/content/articles", "web/src/content/articles-ar")
CHROME_GLOBS = (
    "web/src/layouts",
    "web/src/components",
    "web/src/lib",
    "web/src/pages",
)


def git(repo: Path, args: list[str]) -> str:
    return subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True, check=True
    ).stdout.strip()


def parse_iso(s: str) -> datetime:
    d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def is_approved(path: Path) -> bool | None:
    """True/False from frontmatter; None when the field cannot be read."""
    lines = path.read_text(encoding="utf-8").split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None
    for line in lines[1:end]:
        m = re.match(r"^approved:\s*(\S+)", line)
        if m:
            val = m.group(1).strip()
            if val in ("true", "false"):
                return val == "true"
            return None
    return None


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: qa_lastmod.py <dist-dir> [--repo <repo-root>]")
        return 2
    dist = Path(sys.argv[1])
    if not dist.is_dir():
        print(f"qa_lastmod: dist not found: {dist}")
        return 2

    if "--repo" in sys.argv:
        repo = Path(sys.argv[sys.argv.index("--repo") + 1]).resolve()
    else:
        try:
            repo = Path(git(dist, ["rev-parse", "--show-toplevel"]))
        except Exception as e:  # noqa: BLE001
            print(f"qa_lastmod: cannot locate a git work tree ({e})")
            return 2

    sitemaps = sorted(dist.glob("sitemap-*.xml"))
    if not sitemaps:
        print("qa_lastmod: no sitemap-*.xml in dist — nothing to check, which is a failure")
        return 2

    # ---- the ceiling, derived from git rather than asserted ------------------
    approved_dates: list[datetime] = []
    unreadable: list[str] = []
    approved_count = held_count = 0
    for d in CONTENT_DIRS:
        for f in sorted((repo / d).glob("*.md")):
            state = is_approved(f)
            rel = f"{d}/{f.name}"
            if state is None:
                unreadable.append(rel)
                continue
            if not state:
                held_count += 1
                continue
            approved_count += 1
            out = git(repo, ["log", "-1", "--pretty=%cI", "--", f":/{rel}"])
            if out:
                approved_dates.append(parse_iso(out))

    if unreadable:
        for u in unreadable:
            print(f"DEFECT: {u} has no readable `approved:` field")
        print(f"qa_lastmod: {len(unreadable)} unreadable content file(s)")
        return 1
    if approved_count == 0:
        print("qa_lastmod: zero approved content files found — nothing to check, a failure")
        return 2

    chrome_out = git(repo, ["log", "-1", "--pretty=%cI", "--", *[f":/{g}" for g in CHROME_GLOBS]])
    if not chrome_out:
        print("qa_lastmod: no chrome commit resolved — the ceiling is unbounded, a failure")
        return 2
    chrome_date = parse_iso(chrome_out)
    ceiling = max([chrome_date, *approved_dates])
    now = datetime.now(timezone.utc)

    # ---- the assertion -------------------------------------------------------
    defects: list[str] = []
    locs = 0
    lastmods: list[datetime] = []
    for sm in sitemaps:
        xml = sm.read_text(encoding="utf-8")
        for entry in re.findall(r"<url>(.*?)</url>", xml, re.S):
            locs += 1
            loc = re.search(r"<loc>([^<]+)</loc>", entry)
            lm = re.search(r"<lastmod>([^<]+)</lastmod>", entry)
            url = loc.group(1) if loc else "(no loc)"
            if not lm:
                defects.append(f"{url} carries no <lastmod>")
                continue
            try:
                d = parse_iso(lm.group(1))
            except ValueError:
                defects.append(f"{url} has an unparseable <lastmod>: {lm.group(1)}")
                continue
            lastmods.append(d)
            if d > ceiling:
                defects.append(
                    f"{url} lastmod {d.isoformat()} is ABOVE the ceiling "
                    f"{ceiling.isoformat()} — no approved or chrome file is that new"
                )
            if d > now:
                defects.append(f"{url} lastmod {d.isoformat()} is in the future")

    if locs == 0:
        print("qa_lastmod: sitemap has zero <url> entries — nothing to check, a failure")
        return 2

    if defects:
        for d in defects[:40]:
            print("DEFECT:", d)
        if len(defects) > 40:
            print(f"... and {len(defects) - 40} more")
        print(f"qa_lastmod: {len(defects)} defect(s) across {locs} URL(s)")
        return 1

    print(
        f"qa_lastmod: PASS — {locs} URLs, {len(lastmods)} lastmod, newest "
        f"{max(lastmods).isoformat()} <= ceiling {ceiling.isoformat()} "
        f"(chrome {chrome_date.date()}, {approved_count} approved / {held_count} held; "
        f"held files contribute no date)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
