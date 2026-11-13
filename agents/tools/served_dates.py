#!/usr/bin/env python3
"""served_dates — a page's <lastmod> moves when ITS OWN served bytes move.

WHY (standing-queue item 96, raised 2026-11-10 from the growth function, taken
as the board's only DEFECT on 2026-11-11; the question itself is the 2026-09-06
weekly review's forward question, 66 days old)
-----------------------------------------------------------------------------
`sitemapLastmod.mjs` resolves every page's date as `max(chrome, its own content
file)`. That is **provenance-derived** and the module says so honestly in its
own header. The consequence was measured on 2026-11-10 by
`qa_served_manifest --check`, against the bytes the origin was actually
serving:

    138 pages compared
     18 changed their rendered content AND moved their date   (correct)
     47 moved their date with byte-identical content          (noise)
      0 changed silently

So of the 65 dates that moved, **18 had anything behind them — precision 28%.**
Every chrome commit moves all 138. The cost is not paid on the noise; it is
paid on the **real** changes, because a crawler that finds a `lastmod`
unreliable stops believing it, and then today's 18 genuine amendments are
indistinguishable from outside from the 47 that are not.

WHAT THIS DOES, AND THE ONE REASON IT IS POSSIBLE AT ALL
--------------------------------------------------------
It keeps a committed per-URL register of **the date each page's own normalised
served bytes last changed**, and `sitemapLastmod.mjs` reads it in preference to
git provenance. The operand is `content_sha` — `qa_served_manifest`'s existing
normalised page hash, imported from that module rather than reimplemented here,
because two normalisers deciding independently what "the page says" means is
the drift defect this repository has already paid for twice.

**Why the sitemap half is tractable and the JSON-LD half is not, stated here so
the split does not read as an oversight.** A page's `<lastmod>` lives in
`sitemap-0.xml` and NOT in the page's own bytes, so making it output-bounded is
not self-referential: the date can be derived from the hash because the hash
cannot see the date. `dateModified` in the page's JSON-LD **is** in the page's
own bytes, so deriving it from `content_sha` would be a fixed point — the date
moves, the bytes move, the hash moves, the date must move again, forever, on
every page, on every deploy. Closing that half requires `content_sha` to
exclude the self-referential date fields, which changes the manifest's
normaliser and therefore makes every baseline on the origin incomparable until
a deploy has re-seeded it. That is a migration, not an afternoon, and it is
raised as its own row rather than half-done here.

THE SEED IS A KNOWN ERROR WITH A KNOWN SIZE, AND THAT IS DECLARED
-----------------------------------------------------------------
Nothing in this repository ever recorded when a page's served bytes last
changed — that is the whole defect — so the register cannot be derived
backward. Per the 2026-10-04 second amendment's limb two (*a point-of-filing
rule fixes a count's future and leaves a step discontinuity where it was
written*), the seed states its own date and its own error:

  * Article pages are seeded from the last commit touching **their own source
    file** (`web/src/content/articles{,-ar}/<slug>.md`) — not `max()` with
    chrome. That is the honest best available estimate and it is wrong exactly
    where a chrome change genuinely altered what a page says.
  * Index pages have no own file, so they are seeded at the register's opening
    date.
  * Every seeded entry carries `"seeded": true`. From the first `--update`
    after a real content change, that page's date is output-bounded and the
    flag clears. The flag is what makes the discontinuity visible in the
    register instead of in a memory.

At the seed on 2026-11-11 the register was NOT reconciled against the
population, because the population it would be reconciled against does not
exist. 47 of 138 entries were wrong on 2026-11-10 by the measurement above,
and that is the size of the error being carried in.

WHAT IS GATED, AND WHAT IS ONLY PRINTED (#93)
---------------------------------------------
`--check` is **offline and deterministic** and asserts only what cannot be
wrong on a healthy tree: the register parses, its schema matches, no date is in
the future, and every entry's shape is well-formed. It reports register
staleness against a built `dist` — pages whose `content_sha` has moved since
the register was last updated — and **does not fail on it**, because a build
that reds until a side-effecting tool is re-run would red the deploy job, where
nobody can re-run it. Wiring staleness as a gate is the next step and it is
deliberately not taken before these dates have survived one real deploy: a gate
whose determinism across two machines is assumed rather than proved is the
2026-10-20 shape, where four green local builds sat beside a red deploy.

EXIT CODES
----------
  0  register is well-formed (and, with a dist, its staleness is reported)
  1  register is malformed, missing, or carries a future date
  2  FAILURE TO CHECK — no dist, no sitemap, or the manifest could not be built

USAGE
-----
  python3 agents/tools/served_dates.py --seed   [repo] [--dist web/dist]
  python3 agents/tools/served_dates.py --update [repo] [--dist web/dist]
  python3 agents/tools/served_dates.py --check  [repo] [--dist web/dist]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import qa_served_manifest as manifest  # noqa: E402  (sibling tool, one normaliser)

SCHEMA = "madar-served-dates/1"
REGISTER = Path("agents/stats/served-dates.json")


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def head_date(repo: Path) -> str:
    """The HEAD commit's own timestamp — NEVER the wall clock.

    THIS COST A BUILD, AND THE FAILURE WAS THE RIGHT ONE. The first version of
    this tool stamped `changed_at` with `now`, and `qa_lastmod` turned the build
    red on 48 of 138 URLs within a minute: its limb 2 asserts that no `<lastmod>`
    is NEWER than its own URL's provenance ceiling, because anything above that
    ceiling "can only have come from a held draft, from build time, or from thin
    air". A clock reading IS build time. The register describes bytes that were
    built from HEAD's tree, so HEAD's commit timestamp is both the truthful date
    and the one that stays inside the ceiling — and the existing gate, written
    for a different fabrication two months earlier, caught this one unmodified.

    One input is deliberately left unmodelled: a commit that changes a page's
    served bytes while touching neither `CHROME_GLOBS` nor an approved content
    file (a `web/public` asset inlined into a page, say) would stamp above the
    ceiling and red `qa_lastmod`. That is a true finding about an input nothing
    models, so it is left to fail loudly rather than clamped into silence.
    """
    out = subprocess.run(["git", "log", "-1", "--pretty=format:%cI"],
                         cwd=repo, capture_output=True, text=True, timeout=60)
    v = out.stdout.strip()
    if not v:
        raise SystemExit("FAIL(2): cannot read HEAD's commit date; refusing to "
                         "stamp a served-date register from the wall clock.")
    return v


def url_path(url: str) -> str:
    """Full URL -> the site-relative path the resolver is handed, slash-normalised.

    The register is keyed on the PATH and never on the origin, so a custom
    domain (a founder decision, issue #2) cannot invalidate 138 dates.
    """
    cut = url.find("/", url.find("://") + 3) if "://" in url else -1
    p = url[cut:] if cut != -1 else url
    return p if p.endswith("/") else p + "/"


def source_file_for(path: str) -> str | None:
    """The page's OWN source file, for seeding only. None for index pages."""
    body = path
    for prefix in ("/madar/", "/"):
        if body.startswith(prefix):
            body = body[len(prefix) - 1:]
            break
    body = body.strip("/")
    if body.startswith("ar/articles/"):
        return f"web/src/content/articles-ar/{body[len('ar/articles/'):]}.md"
    if body.startswith("articles/"):
        return f"web/src/content/articles/{body[len('articles/'):]}.md"
    # /valence/ is a hand-written static file under public/ and has its own life
    # — the resolver says so too. It is built from that one file and NOT from
    # the chrome, so the chrome ceiling is not its ceiling: seeding it there put
    # its date 9 days above `qa_lastmod`'s own per-URL bound and red the build a
    # third time. A page with no own file in `src/content` is not the same thing
    # as a page with no own file.
    if body == "valence":
        return "web/public/valence/index.html"
    return None


def git_date(repo: Path, rel: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--pretty=format:%cI", "--", f":/{rel}"],
            cwd=repo, capture_output=True, text=True, timeout=60,
        )
    except Exception:
        return None
    v = out.stdout.strip()
    return v or None


def pages_from_dist(dist: Path) -> tuple[dict[str, str] | None, int]:
    """path -> content_sha, built by qa_served_manifest's own code."""
    man, rc = manifest.build_manifest(dist)
    if man is None:
        return None, rc
    return {url_path(u): e["content_sha"] for u, e in man["pages"].items()}, 0


CHROME_GLOBS = (":/web/src/layouts", ":/web/src/components",
                ":/web/src/lib", ":/web/src/pages")


def chrome_ceiling(repo: Path) -> str | None:
    """Newest commit touching the chrome — the seed for a page with no own file.

    AND THE REASON IT IS COMPUTED FROM GIT RATHER THAN READ FROM `dist`. The
    first version seeded these 48 pages from the `<lastmod>` the built sitemap
    already carried, on the stated ground that it *is* the provenance ceiling.
    It was not: that sitemap had been produced by the previous build, which had
    already read the broken wall-clock register this seed was replacing. So the
    seed read its answer off its own prior output and reproduced the exact
    defect it was correcting, and `qa_lastmod` red a second time with the
    identical 48 URLs and the identical timestamp. 2026-09-14's trap 2 — *an
    assertion must not read its answer off the field it supplements* — on a
    seeding path rather than on a check, and 2026-10-06's warning about a
    manifest generated by the build it describes, met head-on.

    The chrome ceiling is by construction <= `qa_lastmod`'s per-URL ceiling,
    which is `max(chrome, that URL's own approved content)`.
    """
    out = subprocess.run(["git", "log", "-1", "--pretty=format:%cI", "--", *CHROME_GLOBS],
                         cwd=repo, capture_output=True, text=True, timeout=60)
    return out.stdout.strip() or None


def load(repo: Path) -> dict | None:
    p = repo / REGISTER
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except Exception:
        return None


def save(repo: Path, reg: dict) -> None:
    p = repo / REGISTER
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(reg, indent=1, sort_keys=True) + "\n")


def cmd_seed(repo: Path, dist: Path) -> int:
    if load(repo) is not None:
        print("REFUSED: the register already exists. Seeding again would discard "
              "every output-bounded date earned since it was opened and replace "
              "them with provenance estimates. Use --update.")
        return 1
    cur, rc = pages_from_dist(dist)
    if cur is None:
        return rc
    opened = head_date(repo)
    ceiling = chrome_ceiling(repo)
    pages: dict[str, dict] = {}
    from_own_file = 0
    from_ceiling = 0
    for path, sha in sorted(cur.items()):
        rel = source_file_for(path)
        d = git_date(repo, rel) if rel else None
        if d:
            from_own_file += 1
            src = rel
        else:
            d = ceiling
            if d:
                from_ceiling += 1
                src = "chrome-ceiling-at-seeding"
            else:
                d, src = opened, "head-at-register-opening"
        pages[path] = {
            "content_sha": sha,
            "changed_at": d,
            "seeded": True,
            "seeded_from": src,
        }
    reg = {
        "schema": SCHEMA,
        "opened": opened,
        "note": ("Per-URL date of the last change to the page's own normalised "
                 "served bytes. Seeded estimates carry seeded:true and are a "
                 "declared known error — see agents/tools/served_dates.py."),
        "pages": pages,
    }
    save(repo, reg)
    print(f"OK served_dates --seed — register OPENED at {opened}")
    print(f"  entries ..................... {len(pages)}")
    print(f"  seeded from their own file .. {from_own_file}")
    print(f"  seeded at the chrome ceiling  {from_ceiling}  (no own source file)")
    print(f"  seeded at HEAD .............. {len(pages) - from_own_file - from_ceiling}")
    print("  every entry carries seeded:true and clears on its first real change")
    return 0


def stamp_for(repo: Path, path: str, head: str, chrome: str | None) -> str:
    """The date a moved page's bytes CHANGED — not the date they were observed.

    THIS COST A BUILD TOO, AND IT IS THE SECOND HALF OF `head_date`'s LESSON.
    `head_date` was right to refuse the wall clock and wrong about WHICH commit:
    it stamped every moved page with HEAD's timestamp, and under ruling #96 a run
    commits at the close of every standing function, so HEAD is routinely a
    commit that touched no served byte at all. On 2026-11-13 — the register's
    FIRST contact with a real content change — four pages moved at the `1of5`
    commit (12:30:20Z, which touched approved content) and were stamped with the
    `2of5` commit (12:34:02Z, which touched only `agents/` and
    `content-drafts/`). `qa_lastmod` red on all four: its ceiling is the newest
    commit touching an approved or chrome file, and HEAD was 3m42s above it.

    The ceiling was not the thing that was wrong. Attributing a change to a
    commit that did not make it was. So a moved page is stamped with the newest
    commit touching ITS OWN source file, falling back to the chrome when it has
    none, and bounded above by HEAD:

        min(head, max(own source file's last commit, chrome))

    Both limbs of the max are, by construction, at or below `qa_lastmod`'s own
    ceiling — `max(newest approved content, newest chrome)` — because an article's
    own file IS one of the approved files. The register therefore cannot put a
    date above the ceiling that governs it, and it stays output-bounded in the
    half that was ever the point: WHICH pages moved. *The register's contribution
    is the selection, never the clock; provenance was always right about when and
    only ever wrong about who.*
    """
    cands = []
    src = source_file_for(path)
    if src:
        d = git_date(repo, src)
        if d:
            cands.append(d)
    if chrome:
        cands.append(chrome)
    if not cands:
        return head
    return min(head, max(cands))


def cmd_update(repo: Path, dist: Path) -> int:
    reg = load(repo)
    if reg is None:
        print(f"FAIL(1): no register at {REGISTER}. Run --seed once.")
        return 1
    cur, rc = pages_from_dist(dist)
    if cur is None:
        return rc
    stamp = head_date(repo)
    chrome = chrome_ceiling(repo)
    pages = reg["pages"]
    moved, added, removed = [], [], sorted(set(pages) - set(cur))
    for path, sha in sorted(cur.items()):
        e = pages.get(path)
        at = stamp_for(repo, path, stamp, chrome)
        if e is None:
            pages[path] = {"content_sha": sha, "changed_at": at,
                           "seeded": False, "seeded_from": "first-served"}
            added.append(path)
        elif e["content_sha"] != sha:
            e["content_sha"] = sha
            e["changed_at"] = at
            e["seeded"] = False
            e.pop("seeded_from", None)
            moved.append(path)
    for path in removed:
        pages.pop(path)
    reg["updated_at"] = stamp
    save(repo, reg)
    print(f"OK served_dates --update — {stamp}")
    print(f"  pages in dist ............... {len(cur)}")
    print(f"  dates MOVED (bytes changed) . {len(moved)}")
    for p in moved[:12]:
        print(f"      ~ {p}")
    if len(moved) > 12:
        print(f"      … and {len(moved) - 12} more")
    print(f"  new pages ................... {len(added)}")
    for p in added[:6]:
        print(f"      + {p}")
    print(f"  entries dropped ............. {len(removed)}")
    still = sum(1 for e in pages.values() if e.get("seeded"))
    print(f"  still carrying a SEEDED date  {still} of {len(pages)} — "
          "the declared step discontinuity, shrinking only as pages really change")
    return 0


def cmd_check(repo: Path, dist: Path | None) -> int:
    reg = load(repo)
    if reg is None:
        print(f"FAIL(1): no register at {REGISTER}, or it does not parse. The "
              "resolver falls back to git provenance without it, which is the "
              "defect item 96 names — so its absence is a failure, not a default.")
        return 1
    if reg.get("schema") != SCHEMA:
        print(f"FAIL(1): register schema {reg.get('schema')!r} != {SCHEMA!r}.")
        return 1
    pages = reg.get("pages") or {}
    if not pages:
        print("FAIL(1): the register is EMPTY. A date register that describes no "
              "page has failed, not passed (the 08-16 silent-pass trap).")
        return 1
    now = now_iso()
    bad = []
    for path, e in sorted(pages.items()):
        if not isinstance(e, dict) or not e.get("content_sha") or not e.get("changed_at"):
            bad.append((path, "malformed entry"))
        elif e["changed_at"] > now:
            bad.append((path, f"date in the FUTURE: {e['changed_at']}"))
    if bad:
        print(f"FAIL(1): {len(bad)} malformed or future-dated entr(ies):")
        for path, why in bad[:10]:
            print(f"  ! {path} — {why}")
        return 1
    seeded = sum(1 for e in pages.values() if e.get("seeded"))
    print("OK served_dates --check — register well-formed")
    print(f"  entries ..................... {len(pages)}")
    print(f"  output-bounded ............... {len(pages) - seeded}")
    print(f"  still seeded (declared error)  {seeded}")
    print(f"  opened ...................... {reg.get('opened')}")
    print(f"  last updated ................ {reg.get('updated_at', '— never')}")

    if dist is None:
        return 0
    cur, rc = pages_from_dist(dist)
    if cur is None:
        return rc
    stale = sorted(p for p, sha in cur.items()
                   if p in pages and pages[p]["content_sha"] != sha)
    absent = sorted(set(cur) - set(pages))
    print("\n  REPORTED AND NOT ASSERTED (#93) — register staleness against this dist")
    print(f"  pages whose bytes moved since the last --update  {len(stale)}")
    for p in stale[:10]:
        print(f"      ~ {p}")
    print(f"  pages in dist with no register entry ........... {len(absent)}")
    for p in absent[:6]:
        print(f"      ? {p}")
    if stale or absent:
        print("  -> run --update, then rebuild, so the sitemap carries these dates.")
    print("  Not gated: a build that reds until a side-effecting tool is re-run")
    print("  would red the DEPLOY job, where nobody can re-run it.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("repo", nargs="?", default=".")
    ap.add_argument("--dist", default=None)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--seed", action="store_true")
    g.add_argument("--update", action="store_true")
    g.add_argument("--check", action="store_true")
    a = ap.parse_args()

    repo = Path(a.repo).resolve()
    dist = Path(a.dist).resolve() if a.dist else (repo / "web" / "dist")
    if (a.seed or a.update) and not dist.exists():
        print(f"FAIL(2): no dist at {dist}. This tool reads SERVED BYTES; there is "
              "no provenance route to the answer, which is the point.")
        return 2
    if a.seed:
        return cmd_seed(repo, dist)
    if a.update:
        return cmd_update(repo, dist)
    return cmd_check(repo, dist if dist.exists() else None)


if __name__ == "__main__":
    raise SystemExit(main())
