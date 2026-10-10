#!/usr/bin/env python3
r"""
qa_bridge_coverage.py — standing assertion 32. Owner: Assertions Engineer.

Closes standing-queue **item 1**, raised 2026-10-04 as the daily's forward question,
displaced from the head four times, 6 days open. Ruling **#93**.

THE ITEM ASKED THE WRONG QUESTION AND THE MEASUREMENT SAYS SO. Item 1 read: *of the
assertions that gate the deploy, which are wired somewhere that cannot observe the
thing they assert?* Answered by enumeration on 2026-10-10: **none of them.** All 28
gating assertions read `web/dist` or the repository root, both of which exist in the
`build` job where all 28 run. Not one is in a home blind to its own subject.

**The wrong home is not an assertion's. It is the BRIDGE's.** Every one of those 28
assertions concludes something about `dist`. A reader is not served `dist`; a reader
is served the origin. The only thing in this operation that carries a conclusion from
`dist` to the origin is the `verify` job's byte-compare — and it compares
**sitemap-0.xml plus a five-file sample**, which its own comment says plainly. Six
files. The origin serves 120 pages and 135 assets. **So 28 assertions, every one of
them correct, are promoted to statements about the publication across a bridge
covering 2.4% of it — and 0% of the assets.** Nothing has ever measured that ratio,
which is why it was never anybody's defect.

WHY THE FONTS MADE IT URGENT RATHER THAN MERELY TRUE. On 2026-10-08 the publication
self-hosted its five typefaces: **40 new files**, the largest single addition to the
served surface in its history, and **not one of them is inside the bridge**. The
2026-10-08 log named the exposure in writing — *"if it goes wrong the failure is
silent, because the new assertion asserts where we do not point and never what
arrives"* — and the 10-10 run confirmed one `woff2` by hand at `font/woff2`. **By
hand.** That is the 2026-09-13 defect exactly: a green that costs a human's attention
is paid for out of the runs that have least of it.

WHAT IT ASSERTS, in two limbs, over a bridge it DERIVES rather than lists.

  LIMB 1 — THE BRIDGE'S MEMBERS EXIST IN THE ARTEFACT. Every path the `verify` job
  byte-compares must be present in `dist`. A sample naming a file the build has
  stopped producing cannot compare it. Today that would fail loudly at the origin
  `curl`, *after* the deploy; this limb moves the finding to the `build` job, before
  anything is published, which is this queue item's entire subject applied to the
  bridge itself.

  LIMB 2 — THE BRIDGE'S SHAPE SPANS THE PUBLICATION'S DIVISIONS. A six-file sample
  licenses conclusions about 255 files only if it is representative in some checkable
  way, and exactly one division is cheap to check and expensive to lose: **both
  editions and both feeds.** A bridge that silently dropped its Arabic half would
  byte-compare the English half and pass forever, while the Arabic edition — half of
  this publication, composed and not translated — crossed to the reader unverified.
  The four required classes are derived from `dist`: an English page, an Arabic page
  (any path under `ar/`), the English feed, the Arabic feed. Every `.html` member of
  the bridge must also appear in the sitemap's own `<loc>` set, because the bridge's
  width is scarce and spending it on a page the publication does not claim to serve
  is spending it on nothing.

WHAT IT MEASURES AND DELIBERATELY DOES NOT ASSERT. The coverage ratio itself, and the
blind set broken out by class. The reason is stated in the output rather than left to
be inferred: **widening the bridge is an edit to `.github/workflows/**`, which this
identity is refused write access to.** An assertion with a floor above today's
measured reality would red every build until a patch nobody can apply lands — which
is `qa_feed_validators`' position (2026-09-24) turned into a self-inflicted outage.
So the ratio is printed on every build, the remedy is staged as a patch, and the
number moves into the QA log where a human reads it. Same disposition as
`qa_third_party_origins`' 3,350 citations: counted, printed, not asserted, with the
reason beside the count.

THE REMEDY IS ALREADY ON DISK AND ALREADY PUBLISHED, WHICH IS THE PART WORTH KNOWING.
`qa_served_manifest --emit` writes a per-URL fingerprint of **every** served page and
asset into `dist`, and that file is served at the origin (200, 67,737 bytes, confirmed
2026-10-10). A 255-file bridge therefore costs one `curl` and one comparison, not 255
of them — the wide instrument exists, is gated, and is being published daily, while
the bridge it could replace still samples six files. Staged at
`agents/patches/2026-10-10-verify-bridge-via-served-manifest.md`. Open item 7 (*the
published oracle has no auditor*) and open item 8 (*`--check` has no honest home
before the commit*) are the same triangle from two other corners; this tool names the
third and asserts the part of it that is reachable from here.

WHY IT IS NOT IN qa_census. The census cross-checks a tool's printed number against a
population it derives independently. This tool's population is a set of shell paths
parsed out of a YAML file; the census has no independent derivation for that, and a
census row whose expected value is read from the same file the tool reads is the
self-agreement defect (#57). Stated here rather than left unexplained, per 2026-09-13.

SCOPE AND THE ONE THING THAT COULD GO WRONG. The verify job is parsed, not executed,
and the parse is deliberately narrow: the `cmp -s live-probe dist/<path>` probe and
the `for f in <list>; do ... cmp ... "dist/$f"` sample, both inside the `verify:` job
block only. **A bridge widened by a mechanism this parser does not recognise would be
reported as narrower than it is** — a false alarm, never a false pass, which is the
correct direction for a parser to be wrong in. If the parse finds nothing at all it
exits 3 rather than reporting a clean zero-width bridge (#16's silent-pass trap).

THE DEFECT THIS TOOL'S OWN HARNESS FOUND, recorded because it is the reason the parse
is per-loop rather than per-job. The first draft credited **every** `for f in` list
inside the verify job. That job has two: the byte-compare loop, and the feed-cache
step, which `curl -I`s both feeds for an ETag and compares nothing. So two files were
credited as byte-confirmed on the strength of a step that does not confirm bytes —
**overcounting the bridge, which is the false-pass direction.** It survived the
control because on the real tree both parsers print **6**: the two lists overlap
exactly on the two feeds. The right number for the wrong reason, which is 2026-09-14's
input-side question — *where does the string I am looking for also legitimately
appear?* — and it was caught only because bite 2 was written to drop `ar/rss.xml`
from one loop while the other still named it. A bite aimed at a file named once would
have passed and left the bug in.

EXIT CODES
  0  clean
  1  a bridge member missing from dist, a bridge class unspanned, or an .html
     member absent from the sitemap
  2  usage
  3  failure to check — the verify job, its comparisons, or the sitemap could not
     be located at all. A bridge that cannot be found is not a bridge of width zero.

USAGE
  python3 agents/tools/qa_bridge_coverage.py .                 # assert + measure
  python3 agents/tools/qa_bridge_coverage.py . --workflow PATH # override, for proofs
  python3 agents/tools/qa_bridge_coverage.py . --quiet         # exit code only
"""

import json
import os
import re
import sys

WORKFLOW = ".github/workflows/astro-pages.yml"
DIST = os.path.join("web", "dist")
SITEMAP = "sitemap-0.xml"
MANIFEST = "served-manifest.json"

# The verify job's two comparison mechanisms, parsed rather than executed.
#   probe:  cmp -s live-probe dist/sitemap-0.xml
#   sample: for f in index.html ar/index.html rss.xml ...; do ... cmp ... "dist/$f"
PROBE = re.compile(r"""cmp\s+-s\s+\S+\s+["']?dist/([^\s"';$]+)""")
# Each `for f in <list>; do ... done` block, captured WITH its body. The list is
# credited to the bridge only if THAT block's own body byte-compares against dist.
# Scoping this to the whole verify job was the tool's first defect and its own
# proof harness found it: the job's second loop is the feed-cache-validator step,
# which `curl -I`s for ETag and compares nothing — crediting its two files as
# bridge coverage overcounts the bridge, which is the false-pass direction. On the
# real tree it even produced the right total, because the two lists overlap
# exactly on the feeds: the right number for the wrong reason (2026-09-14).
FOR_BLOCK = re.compile(
    r"""^[ \t]*for\s+f\s+in\s+(?P<list>.+?);\s*do\s*$(?P<body>.*?)^[ \t]*done\b""",
    re.M | re.S,
)
CMP_IN_LOOP = re.compile(r"""cmp\s+-s\s+\S+\s+["']?dist/\$f["']?""")
JOB = re.compile(r"^  (\w[\w-]*):\s*$", re.M)

# Feeds are not pages and are not in the sitemap; they are the other half of what
# this publication actually serves to a machine. Derived by name from dist below.
EN_FEED = "rss.xml"
AR_FEED = os.path.join("ar", "rss.xml")


def die(code, msg):
    print(msg)
    sys.exit(code)


def verify_job_block(wf_text):
    """The text of the `verify:` job only. A comparison in `build` or `deploy` is
    not a bridge to the origin — it is a check on the artefact we already hold."""
    names = [(m.start(), m.group(1)) for m in JOB.finditer(wf_text)]
    for i, (pos, name) in enumerate(names):
        if name == "verify":
            end = names[i + 1][0] if i + 1 < len(names) else len(wf_text)
            return wf_text[pos:end]
    return None


def bridge_members(block):
    """Every dist-relative path the verify job byte-compares against the origin."""
    members = []
    for m in PROBE.finditer(block):
        p = m.group(1)
        if p != "$f":
            members.append(p)
    for m in FOR_BLOCK.finditer(block):
        if not CMP_IN_LOOP.search(m.group("body")):
            continue  # a loop that does not byte-compare is not part of the bridge
        for tok in m.group("list").split():
            if tok and not tok.startswith("$") and "*" not in tok:
                members.append(tok)
    # order-preserving dedupe: the printed list should read as the file does
    seen, out = set(), []
    for p in members:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def sitemap_locs(dist):
    path = os.path.join(dist, SITEMAP)
    if not os.path.isfile(path):
        return None
    text = open(path, encoding="utf-8").read()
    return set(re.findall(r"<loc>([^<]+)</loc>", text))


def loc_to_distfile(loc):
    """A sitemap <loc> as the dist-relative file that serves it."""
    tail = re.sub(r"^https?://[^/]+/madar/?", "", loc)
    tail = tail.strip("/")
    return "index.html" if not tail else os.path.join(tail, "index.html")


def served_surface(dist):
    """Every file the build will publish, split into pages and assets."""
    pages, assets = set(), set()
    for root, _dirs, files in os.walk(dist):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), dist)
            (pages if fn == "index.html" else assets).add(rel)
    return pages, assets


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    quiet = "--quiet" in flags
    wf_override = None
    for f in flags:
        if f.startswith("--workflow"):
            i = sys.argv.index(f)
            if i + 1 < len(sys.argv):
                wf_override = sys.argv[i + 1]
    if len(args) < 1:
        die(2, "usage: qa_bridge_coverage.py <repo-root> [--workflow PATH] [--quiet]")
    root = args[0]
    wf_path = wf_override or os.path.join(root, WORKFLOW)
    dist = os.path.join(root, DIST)

    if not os.path.isfile(wf_path):
        die(3, f"qa_bridge_coverage: FAILURE TO CHECK — no workflow at {wf_path}")
    if not os.path.isdir(dist):
        die(3, f"qa_bridge_coverage: FAILURE TO CHECK — no built artefact at {dist}")

    block = verify_job_block(open(wf_path, encoding="utf-8").read())
    if block is None:
        die(3, "qa_bridge_coverage: FAILURE TO CHECK — no `verify:` job in the workflow. "
               "The bridge from dist to the origin could not be located at all.")

    members = bridge_members(block)
    if not members:
        die(3, "qa_bridge_coverage: FAILURE TO CHECK — the verify job compares nothing "
               "this parser recognises. A bridge that cannot be found is not a bridge "
               "of width zero (#16's silent-pass trap).")

    locs = sitemap_locs(dist)
    if not locs:
        die(3, f"qa_bridge_coverage: FAILURE TO CHECK — no {SITEMAP} in {dist}")

    pages, assets = served_surface(dist)
    sitemap_files = {loc_to_distfile(l) for l in locs}

    failures = []

    # LIMB 1 — every bridge member exists in the artefact.
    missing = [p for p in members if not os.path.isfile(os.path.join(dist, p))]
    for p in missing:
        failures.append(f"bridge member not in dist: {p} — the verify job compares a "
                        f"file this build does not produce, so that comparison cannot bite")

    # LIMB 2 — the bridge spans both editions and both feeds.
    present = [p for p in members if p not in missing]
    html = [p for p in present if p.endswith(".html")]
    spans = {
        "an English page": [p for p in html if not p.startswith("ar" + os.sep)
                            and p in sitemap_files],
        "an Arabic page": [p for p in html if p.startswith("ar" + os.sep)
                           and p in sitemap_files],
        "the English feed": [p for p in present if p == EN_FEED],
        "the Arabic feed": [p for p in present if p == AR_FEED],
    }
    for label, hits in spans.items():
        if not hits:
            failures.append(f"the bridge does not span {label} — a byte-compare blind to "
                            f"it would pass forever while that half of the publication "
                            f"crossed to the reader unverified")

    # LIMB 2b — an .html member the publication does not claim to serve.
    for p in html:
        if p not in sitemap_files:
            failures.append(f"bridge member {p} is not in the sitemap's <loc> set — the "
                            f"bridge's width is scarce and this spends it on a page the "
                            f"publication does not claim to serve")

    if quiet:
        sys.exit(1 if failures else 0)

    # ---- the measurement: printed, never asserted. Reason beside the number.
    total = len(pages) + len(assets)
    confirmed = len([p for p in members if p not in missing])
    conf_pages = len([p for p in members if p in pages])
    conf_assets = len([p for p in members if p in assets])
    mpath = os.path.join(dist, MANIFEST)
    mcount = None
    if os.path.isfile(mpath):
        try:
            m = json.load(open(mpath, encoding="utf-8"))
            mcount = sum(len(v) for v in m.values() if isinstance(v, dict))
        except (ValueError, OSError):
            mcount = None

    print(f"qa_bridge_coverage — the dist-to-origin bridge, parsed from {os.path.basename(wf_path)}")
    print(f"  byte-compared against the origin (ASSERTED) ... {confirmed:>4}  {', '.join(members)}")
    print(f"  served pages ................................. {len(pages):>4}")
    print(f"  served assets ................................ {len(assets):>4}")
    print(f"  coverage of the served surface (NOT asserted) . {confirmed}/{total}"
          f"  = {100.0 * confirmed / total:.1f}%")
    print(f"    of which pages ............................. {conf_pages}/{len(pages)}")
    print(f"    of which assets ............................ {conf_assets}/{len(assets)}")
    # Break the uncovered assets out by class. The four covered assets are the two
    # feeds and the two sitemaps — the machine-readable surface. Everything a PAGE
    # loads is a separate population and it is covered zero times; saying "the
    # assets are unverified" without this split would overclaim by four.
    uncovered = sorted(a for a in assets if a not in set(members))
    classes = {}
    for a in uncovered:
        ext = os.path.splitext(a)[1].lower() or "(none)"
        classes[ext] = classes.get(ext, 0) + 1
    print(f"  uncovered assets by class .................... {len(uncovered)} total")
    for ext, n in sorted(classes.items(), key=lambda kv: -kv[1]):
        print(f"      {ext:<10} {n:>4}")
    print("  the four covered assets are both feeds and both sitemaps — the")
    print("  machine-readable surface. Everything a PAGE loads (styles, scripts, fonts,")
    print("  stills, share cards) is covered ZERO times.")
    if mcount is not None:
        print(f"  served-manifest.json already fingerprints ... {mcount:>4} entries, "
              f"emitted into dist and published")
        print(f"  so a {total}-file bridge costs one curl and one comparison, not {total}.")
    print("  the ratio is MEASURED AND NOT ASSERTED on purpose: widening the bridge is an")
    print("  edit to .github/workflows/**, which this identity is refused write access to,")
    print("  so a floor above today's reality would red every build until a patch nobody")
    print("  can apply lands. Remedy staged at agents/patches/.")
    print()

    if failures:
        print(f"FAIL qa_bridge_coverage — {len(failures)} finding(s)")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)

    print(f"CLEAN qa_bridge_coverage — all {confirmed} bridge member(s) exist in the")
    print("artefact, every .html among them is a page the sitemap claims, and the bridge")
    print("spans both editions and both feeds. What crosses it is narrow; what crosses it")
    print("is at least not lopsided.")
    sys.exit(0)


if __name__ == "__main__":
    main()
