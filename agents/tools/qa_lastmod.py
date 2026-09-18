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
  2. No <lastmod> is NEWER than ITS OWN URL'S ceiling (see below).
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

THE CEILING IS PER-URL, BECAUSE THE RESOLVER IS PER-URL (2026-09-18, ruling #56)
-------------------------------------------------------------------------------
The first version of this file computed ONE ceiling —
    max(newest approved content commit, newest chrome commit)
— and applied it to every URL in the sitemap. That is the correct bound for two
of the resolver's three branches (article pages, index pages) and the correct
bound for NEITHER of the things the third branch does.

`/valence/` is a hand-written static file under `web/public/`, and the resolver
dates it from that file alone. `web/public` is in neither CONTENT_DIRS nor
CHROME_GLOBS, so the global ceiling says nothing whatever about it:

  * FALSE POSITIVE — the failure that found this. Commit bd3c48e (09-17) edited
    `web/public/valence/index.html`, the page's served bytes genuinely changed,
    the resolver emitted the truthful date, and this check failed the deploy.
    The whole of the 09-17 work sat unserved for a day for a defect in the
    instrument rather than in the site.
  * FALSE NEGATIVE — the half nobody had noticed, and the reason this is a
    strengthening and not a loosening. Under one global ceiling, /valence/'s
    date was only ever tested for being too LARGE. Any value below the ceiling
    passed — including a date with no relationship at all to the file the page
    is built from. The URL this check has failed on today is the one URL it had
    never actually checked.

Why not simply add `web/public` to the global ceiling: a held piece's hero still
and share card live under `web/public/stills` and `web/public/og`. A ceiling
that rose with them would rise every time a held draft was touched — which is
the precise leak (9886987, 642fef2) this file was written to close. Widening the
ceiling to admit one served page would re-open the hole for four unserved ones.

So the ceiling is derived per URL, from the same rule the resolver uses:

    a URL served by a hand-written `web/public/<p>/index.html`
        -> ceiling = that file's own last commit
    every other URL
        -> ceiling = max(approved content, chrome), as before

and the static set is DISCOVERED from the filesystem (`web/public/**/index.html`)
rather than named here, so a second static page inherits the rule without anyone
remembering to add it (ruling #36 — derive, never assert).

WHAT THIS STILL CANNOT SEE, SAID PLAINLY
---------------------------------------
A ceiling bounds from ABOVE only. A <lastmod> that is too OLD — a page that
changed and reports that it did not — passes every branch of this check, and
that is the direction a crawler actually punishes, because it is the direction
in which we stop being crawled. The per-URL ceiling narrows the gap (a static
page's bound is now its own file rather than the whole corpus's newest commit)
without closing it. Naming it here so it is not mistaken for covered.

Proved per ruling #35 on landing: bites on a sitemap with an injected
above-ceiling date, bites on a sitemap with a lastmod stripped, silent on the
real build. Re-proved 2026-09-18 with the per-URL ceiling, four ways, every
injection verified to have changed the artefact before the check read it:
control silent on the real 120-URL build; bite on an article dated above the
content+chrome ceiling (the original assertion, intact); bite on a stripped
lastmod; bite on the static page's URL removed from the sitemap, so a ceiling
that matched nothing is a failure and not a pass; and the isolating bite —
/valence/ dated above its own file's commit and BELOW the content+chrome
ceiling, which the old single-ceiling version printed as PASS in the same
breath as the new one prints as a defect.

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
# Hand-written pages Astro copies through verbatim. The resolver dates each of
# these from its own file (`sitemapLastmod.mjs`, the /valence branch), so each
# gets its own ceiling. Enumerated from disk, not listed — see the module head.
STATIC_PAGE_ROOT = "web/public"


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

    # ---- the per-URL ceilings for hand-written static pages ------------------
    # Discovered from the filesystem, never named here: any `web/public/<p>/
    # index.html` is a page the resolver dates from that file alone, so its
    # ceiling is that file's own commit and NOT the content-and-chrome ceiling,
    # which has no bearing on it in either direction. Matched against the
    # sitemap by URL suffix so this needs no knowledge of the deploy base.
    static_ceilings: dict[str, datetime] = {}
    for f in sorted((repo / STATIC_PAGE_ROOT).glob("*/index.html")):
        rel = f"{STATIC_PAGE_ROOT}/{f.parent.name}/index.html"
        out = git(repo, ["log", "-1", "--pretty=%cI", "--", f":/{rel}"])
        if not out:
            # The file is served and git cannot date it: the resolver emits no
            # lastmod for it at all. Absent is a failure here, not a default.
            print(f"qa_lastmod: {rel} is served but has no commit date — cannot bound its URL")
            return 2
        static_ceilings[f"/{f.parent.name}/"] = parse_iso(out)

    # ---- the assertion -------------------------------------------------------
    defects: list[str] = []
    locs = 0
    lastmods: list[datetime] = []
    static_matched: set[str] = set()
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

            url_ceiling, basis = ceiling, "no approved or chrome file is that new"
            for suffix, static_date in static_ceilings.items():
                if url.endswith(suffix):
                    static_matched.add(suffix)
                    url_ceiling = static_date
                    basis = (
                        f"this page is built from {STATIC_PAGE_ROOT}{suffix}index.html "
                        "and nothing else, and that file is not that new"
                    )
                    break

            if d > url_ceiling:
                defects.append(
                    f"{url} lastmod {d.isoformat()} is ABOVE the ceiling "
                    f"{url_ceiling.isoformat()} — {basis}"
                )
            if d > now:
                defects.append(f"{url} lastmod {d.isoformat()} is in the future")

    if locs == 0:
        print("qa_lastmod: sitemap has zero <url> entries — nothing to check, a failure")
        return 2

    # A per-URL ceiling that matched no URL is machinery wired to nothing — the
    # 08-16 silent-pass trap, in the half of this check added to close it.
    for suffix in static_ceilings:
        if suffix not in static_matched:
            print(
                f"qa_lastmod: {STATIC_PAGE_ROOT}{suffix}index.html is served but no sitemap "
                f"URL ends in {suffix} — its ceiling checked nothing"
            )
            return 2

    if defects:
        for d in defects[:40]:
            print("DEFECT:", d)
        if len(defects) > 40:
            print(f"... and {len(defects) - 40} more")
        print(f"qa_lastmod: {len(defects)} defect(s) across {locs} URL(s)")
        return 1

    statics = ", ".join(f"{s} <= {d.date()}" for s, d in sorted(static_ceilings.items()))
    print(
        f"qa_lastmod: PASS — {locs} URLs, {len(lastmods)} lastmod, newest "
        f"{max(lastmods).isoformat()} against the ceiling that governs it "
        f"(content+chrome {ceiling.isoformat()}; chrome {chrome_date.date()}, "
        f"{approved_count} approved / {held_count} held; held files contribute no date). "
        f"{len(static_ceilings)} static page(s) bounded by their own file: {statics}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
