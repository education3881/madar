#!/usr/bin/env python3
"""
qa_held_assets — standing assertion #12: a held piece contributes no BYTES.

WHY (Quality, 2026-09-09 — the 09-08 forward question, answered)
----------------------------------------------------------------
`approved: false` is the hold (#18). Since 2026-09-06 the rule has read: *a held
file is not part of the publication — nothing derived from the content set may
read it.* By 09-08 a held piece contributed no page, no sitemap entry, no feed
item and no <lastmod>. It still contributed FILES: its hero still and its raster
share card live under `web/public/`, and `public/` is copied into `dist` whole.

Measured on the 09-09 build before the fix: six assets, ~48 KB, for three
unpublished Edition 05 pieces, referenced by nothing in any served HTML or XML.
"Nothing links to it" is the wrong test — it is the same wrong test that let the
SVG share cards resolve perfectly and render nowhere for 83 days (08-18). The
right test is what a stranger can GET, and every one of those paths is derivable
from the slug pattern the published articles advertise:

    /madar/og/<held-slug>.png            -> 200
    /madar/articles/<held-slug>/         -> 404

A share card is a derivable promise (#36) for an article that does not exist.
And the still is an SVG carrying its own <title> in readable text, so the
withheld piece's SUBJECT was being served at a guessable URL — an edition that
ships as one gated wave, pre-announcing its own contents.

The fix is the `madar:withhold-held-assets` integration (src/lib/heldAssets.mjs),
which deletes held slugs' assets from `dist` at build:done. This is its
output-side twin: the integration is the mechanism, this is the assertion, and
the assertion does not trust the mechanism.

WHAT IT ASSERTS
---------------
1. No file anywhere in `dist` has a held slug as its filename stem.
2. Every held slug's assets are still present in `public/` — the withholding
   must be an omission from the SERVED output, never a deletion from the repo,
   because the publish gate checks stills and cards on disk before the wave
   flips.
3. Every APPROVED slug's still and card ARE present in `dist` — the control.
   Without it, a sweep that deleted the whole `og/` directory would pass.

Proved both ways per #35 before being trusted:
  BITE    — run against a dist built with the integration disabled: 6 findings.
  CONTROL — run against the real build: silent, and all 38 approved cards found.

Usage:  python3 agents/tools/qa_held_assets.py [--dist web/dist] [--root .]
Exit 0 clean, 1 on any finding.
"""

from __future__ import annotations

import argparse
import os
import re
import sys

CONTENT_DIRS = ("web/src/content/articles", "web/src/content/articles-ar")
SLUG_ASSET_DIRS = ("stills", "og")


def frontmatter_approved(path: str) -> bool:
    """Parse the frontmatter BLOCK — never a fixed line window (09-08 lesson)."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    if not lines or lines[0].strip() != "---":
        raise SystemExit(f"qa_held_assets: {path} does not open with a frontmatter block.")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise SystemExit(f"qa_held_assets: {path} has an unterminated frontmatter block.")
    for line in lines[1:end]:
        m = re.match(r"^approved:\s*(\S+)", line)
        if m:
            value = m.group(1).strip()
            if value not in ("true", "false"):
                raise SystemExit(
                    f"qa_held_assets: {path} has `approved: {value}`, neither true nor false."
                )
            return value == "true"
    raise SystemExit(
        f"qa_held_assets: {path} has no readable `approved:` field. A draft whose hold "
        "state cannot be read must not be assumed published."
    )


def collect(root: str) -> tuple[set[str], set[str]]:
    held: set[str] = set()
    approved: set[str] = set()
    for d in CONTENT_DIRS:
        full = os.path.join(root, d)
        names = [n for n in os.listdir(full) if n.endswith(".md")]
        if not names:
            raise SystemExit(
                f"qa_held_assets: content directory {d} is EMPTY. An approval sweep that "
                "finds nothing to check has failed, not passed."
            )
        for name in names:
            slug = name[:-3]
            (approved if frontmatter_approved(os.path.join(full, name)) else held).add(slug)
    # A slug held in either language is held. The pair flips together or not at all.
    approved -= held
    return held, approved


def stems(directory: str) -> dict[str, str]:
    """filename stem -> full path, for one asset directory."""
    out: dict[str, str] = {}
    if not os.path.isdir(directory):
        return out
    for name in os.listdir(directory):
        out[os.path.splitext(name)[0]] = os.path.join(directory, name)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--dist", default="web/dist")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    dist = os.path.join(root, args.dist) if not os.path.isabs(args.dist) else args.dist
    public = os.path.join(root, "web/public")

    held, approved = collect(root)
    findings: list[str] = []

    # 1. no held slug anywhere in dist
    for sub in SLUG_ASSET_DIRS:
        for stem, path in stems(os.path.join(dist, sub)).items():
            if stem in held:
                findings.append(f"LEAK  dist/{sub}/{os.path.basename(path)} — slug is held")

    # 1b. and nowhere else in dist either, under any extension
    for dirpath, _dirnames, filenames in os.walk(dist):
        for fn in filenames:
            stem = os.path.splitext(fn)[0]
            if stem in held:
                rel = os.path.relpath(os.path.join(dirpath, fn), dist)
                if not any(rel.startswith(f"{s}{os.sep}") for s in SLUG_ASSET_DIRS):
                    findings.append(f"LEAK  dist/{rel} — slug is held")

    # 2. held assets must still exist in the repo
    for slug in sorted(held):
        present = [
            sub for sub in SLUG_ASSET_DIRS if slug in stems(os.path.join(public, sub))
        ]
        if not present:
            findings.append(
                f"MISSING  public/: held slug {slug} has no still and no card. "
                "Withholding is an omission from the served output, not a deletion."
            )

    # 3. CONTROL — approved slugs must be served
    control_checked = 0
    for slug in sorted(approved):
        for sub in SLUG_ASSET_DIRS:
            if slug in stems(os.path.join(public, sub)):
                control_checked += 1
                if slug not in stems(os.path.join(dist, sub)):
                    findings.append(
                        f"OVER-REACH  dist/{sub}/ is missing approved slug {slug}"
                    )
    if control_checked == 0:
        findings.append(
            "CONTROL FOUND NOTHING TO CHECK — an assertion with no control has failed, "
            "not passed (08-16 silent-pass trap)."
        )

    print(f"qa_held_assets: {len(held)} held slug(s), {len(approved)} approved slug(s), "
          f"{control_checked} control asset(s) checked")
    for f in findings:
        print("  " + f)
    if findings:
        print(f"FAIL — {len(findings)} finding(s)")
        return 1
    print("CLEAN — no held piece contributes bytes; every approved asset is served")
    return 0


if __name__ == "__main__":
    sys.exit(main())
