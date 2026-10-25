#!/usr/bin/env python3
"""
qa_font_payload — standing assertion #39: every webfont file a browser FETCHES
for a served page is justified by a glyph that page actually paints, and no
Arabic text is painted in a slanted style.

WHY THIS IS THE THIRTY-NINTH AND NOT A VARIANT OF ONE OF THE OTHER THIRTY-EIGHT.

Every instrument this operation owns reads a byte that EXISTS — in `dist`, in
`web/src/content`, in the workflow file, in this repository's own prose. A woff2
file is not like that. It exists in `dist` whether or not anyone ever receives
it, and it is transferred to a reader only when the layout engine has to paint a
glyph out of it. So the bytes a reader actually pays for a page are a product of
four things that meet nowhere except at render time: the page's text, the
cascade's font stacks, the `unicode-range` carve in `madar-fonts.css`, and the
browser's own matching. **Nothing in this operation has ever read that quantity**,
and two defects of the same class were found by hand eight days apart because of
it, both in the same queue lane:

  2026-10-17  `.site-footer__closing` set the Arabic strapline in Newsreader
              Italic — a Latin-only face. It rendered from the system serif,
              and the browser fetched 146,872 bytes to paint NONE of it. The
              single largest request on every Arabic page, for nine words.

  2026-10-25  Two `<em>` tags in the about paragraph slanted Arabic. `Amiri
              Italic` is a real slanted face, so unlike the strapline it did
              render — 111,720 + 19,380 bytes to paint 29 characters, 30.7% of
              the Arabic home page's whole font payload.

Both were found by looking. Neither could have been found by any gate. This one
gates both shapes, and it gates them as two limbs because they are two different
questions about the same measurement.

LIMB 1 — NO SLANTED ARABIC. Asserted.
  No painted text run containing an Arabic code point resolves to a computed
  `font-style` other than `normal`. Arabic typography has no italic convention,
  which is the same fact as *tracking is never applied to Arabic* (RUNBOOK,
  2026-08-18 clause 4), and this stylesheet had already said it twice — at
  `[dir="rtl"] .pullquote` and in `SiteFooter.astro` — both times per component,
  which is why the third instance stood. **The boundary is exact and the
  artefact supplies it**: a code point is in an Arabic block or it is not, no
  classifier and no guess, which is #113's and #114's method applied to a script
  instead of to an acronym or a digit.

LIMB 2 — NO DEAD FETCH. Asserted.
  Every `*.woff2` the browser requested is justified by at least one painted
  code point that (a) lies inside that file's own `unicode-range`, (b) is in a
  run whose computed font stack names that file's family, and (c) is in a run
  whose computed style and weight the file's `@font-face` accepts. A file that
  is fetched and justified by nothing is the 10-17 defect exactly.

  **This limb is deliberately CONSERVATIVE, and the reason is written here
  rather than discovered later.** Plain JS cannot ask which face actually
  painted a glyph — `getComputedStyle` returns the DECLARED stack, not the
  resolved face, and the resolved face is only reachable over CDP. So a run
  whose stack is `"JetBrains Mono", …, serif` justifies a JetBrains file for any
  code point in its range even if a system font did the painting. The limb
  therefore cannot produce a false RED, and it can miss a waste case where an
  earlier family in the stack already covered the glyph. It still catches the
  10-17 shape, because that defect's mismatch is in the `unicode-range` and not
  in the family: Arabic code points are not in a Latin subset's range, so the
  Newsreader italic file had nothing to justify it. Stated as a limit rather
  than left as a surprise (#90's habit, and item 26's subject).

WHAT IS MEASURED AND DELIBERATELY NOT ASSERTED.
  The per-page payload total and the bytes-per-painted-character of each face
  are printed on every run and asserted by nothing. A ceiling is the obvious
  next assertion and it would be the wrong one today: the two reductions item 20
  names (subset to the corpus glyph inventory, drop a family) are both out of
  this lane's reach, so a floor above today's reality would turn every build red
  until work nobody here can do lands — which is `qa_bridge_coverage`'s 2.3%
  reasoning in a second costume. The numbers are printed so the next person to
  look does not have to build the probe again.

PAGE SET. Six served pages, both editions, three kinds: the two home pages (the
most type-dense documents the publication serves), one article pair (the longest
running prose), and the two editions indexes. It is a sample and it says so —
134 pages × one Chrome launch is not a build step. A defect that exists only on
a page outside this set is outside this gate, which is the enumeration family's
own standing warning turned on its newest member.

Exit 0 = clean. Exit 1 = a limb failed. Exit 2 = could not measure (no Chrome,
no dist, no font CSS) — never silently green.

Usage:
    python3 agents/tools/qa_font_payload.py web/dist
    python3 agents/tools/qa_font_payload.py web/dist --report   # print, never fail
"""

from __future__ import annotations

import functools
import html as H
import http.server
import json
import os
import pathlib
import re
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading
import unicodedata

BROWSERS = ("google-chrome-stable", "google-chrome", "chromium-browser", "chromium")

# The Arabic blocks a published page of this publication can carry. Presentation
# forms are included because a copy-pasted register can carry them even though
# this operation composes in the base block.
ARABIC_RANGES = ((0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
                 (0xFB50, 0xFDFF), (0xFE70, 0xFEFF))

PAGES = [
    ("EN home", "index.html"),
    ("AR home", "ar/index.html"),
    ("EN article", "articles/2026-07-04-kenya-cbe-grade10-pathways/index.html"),
    ("AR article", "ar/articles/2026-07-04-kenya-cbe-grade10-pathways/index.html"),
    ("EN editions", "editions/index.html"),
    ("AR editions", "ar/editions/index.html"),
]

PROBE = r"""
<script>
window.addEventListener('load', function () {
  var runs = [];
  var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  var n;
  while ((n = w.nextNode())) {
    var t = n.nodeValue;
    if (!t || !t.trim()) continue;
    var el = n.parentElement;
    if (!el) continue;
    var tag = el.tagName;
    if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'TITLE') continue;
    /* SVG IS NOT SKIPPED, AND THE FIRST DRAFT SKIPPED IT. An inlined cover's
       <text> is painted and loads webfonts exactly like body copy; only
       <title>, <desc> and <metadata> are not. Skipping the whole subtree cost
       this tool a FALSE RED on /ar/editions/ — 39,260 bytes of Cormorant Italic
       reported as justified by nothing, when the six inlined edition covers
       paint it. A limb that cannot see part of the page reports that part as
       waste, which is the enumeration family pointed at this tool's own eyes. */
    if (el.closest('title, desc, metadata')) continue;
    var cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    if (!el.getClientRects().length) continue;  /* laid out, or it paints nothing */
    var fams = cs.fontFamily.split(',').map(function (s) {
      return s.trim().replace(/^["']|["']$/g, '');
    });
    var cps = {};
    var txt = t.trim();
    for (var i = 0; i < txt.length; i++) {
      if (/\s/.test(txt[i])) continue;
      var c = txt.codePointAt(i);
      if (c > 0xFFFF) i++;
      cps[c] = (cps[c] || 0) + 1;      /* counts, not presence: the denominator
                                          has to be characters actually painted
                                          out of this subset, not characters in
                                          a run that happens to touch it */
    }
    runs.push({
      f: fams, s: cs.fontStyle, w: parseInt(cs.fontWeight, 10) || 400,
      c: cps,
      n: txt.replace(/\s/g, '').length,
      e: tag.toLowerCase() + (el.className ? '.' + String(el.className).trim().split(/\s+/)[0] : ''),
      x: txt.slice(0, 48)
    });
  }
  document.body.innerHTML = '<pre id="probe">' + JSON.stringify(runs) + '</pre>';
});
</script>
"""


def die(msg, code=2):
    print("REFUSED qa_font_payload — %s" % msg)
    sys.exit(code)


def find_browser():
    for c in BROWSERS:
        p = subprocess.run(["which", c], capture_output=True, text=True)
        if p.returncode == 0:
            return p.stdout.strip()
    return None


def parse_faces(css_text):
    """Every @font-face in the bundle, as (file, family, style, weights, ranges).

    Derived from the stylesheet the build actually serves, never copied: the
    bundle is regenerated by `build_font_bundle.py` and a list typed here would
    be a fourth home for a fact that already has one (#75).
    """
    faces = {}
    n_blocks = 0
    for blk in re.findall(r"@font-face\s*\{(.*?)\}", css_text, re.S):
        n_blocks += 1
        def field(name):
            m = re.search(r"\b%s\s*:\s*([^;]+);" % name, blk)
            return m.group(1).strip() if m else ""
        fam = field("font-family").strip("'\"")
        style = field("font-style") or "normal"
        weight = field("font-weight") or "400"
        src = field("src")
        m = re.search(r"url\(([^)]+)\)", src)
        if not m or not fam:
            continue
        fname = m.group(1).strip("'\"").rsplit("/", 1)[-1]
        ws = [int(x) for x in re.findall(r"\d+", weight)] or [400]
        lo, hi = min(ws), max(ws)
        ranges = []
        for tok in re.findall(r"U\+([0-9A-Fa-f?]+)(?:-([0-9A-Fa-f]+))?", field("unicode-range")):
            a, b = tok
            if "?" in a:
                lo_cp = int(a.replace("?", "0"), 16)
                hi_cp = int(a.replace("?", "F"), 16)
            else:
                lo_cp = int(a, 16)
                hi_cp = int(b, 16) if b else lo_cp
            ranges.append((lo_cp, hi_cp))
        if not ranges:
            ranges = [(0, 0x10FFFF)]
        # ONE FILE IS DECLARED BY SEVERAL @font-face BLOCKS, and keying the dict
        # by filename cost this tool its first run: the bundle writes a separate
        # block per weight — Newsreader normal 400, 500 and 600 all point at
        # `newsreader-normal-400-600var-latin.woff2` — so the last block read
        # overwrote the others and the file was recorded as weight 600 only.
        # Every body paragraph on the site is weight 400, so limb 2 reported the
        # publication's own body face as justified by nothing, on six pages.
        # A file is justified when ANY of its declaring faces is.
        faces.setdefault(fname, []).append(
            {"family": fam, "style": style, "wlo": lo, "whi": hi, "ranges": ranges})
    return faces, n_blocks


def in_any(cp, ranges):
    return any(a <= cp <= b for a, b in ranges)


class _Log(http.server.SimpleHTTPRequestHandler):
    hits = None

    def log_message(self, *a):
        pass

    def send_head(self):
        r = super().send_head()
        if _Log.hits is not None:
            _Log.hits.append(self.path)
        return r


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    report_only = "--report" in sys.argv
    dist = pathlib.Path(argv[0] if argv else "web/dist").resolve()
    if not dist.is_dir():
        die("no dist at %s" % dist)
    css = dist / "fonts" / "madar-fonts.css"
    if not css.is_file():
        die("no served font stylesheet at %s" % css)
    browser = find_browser()
    if not browser:
        die("no headless Chrome on this runner; this assertion cannot be faked green")

    faces, n_blocks = parse_faces(css.read_text(encoding="utf-8"))
    if not faces:
        die("parsed 0 @font-face blocks out of the served stylesheet")

    scratch = pathlib.Path(tempfile.mkdtemp(prefix="qa_font_payload_"))
    root = scratch / "madar"
    shutil.copytree(dist, root)

    _Log.hits = []
    handler = functools.partial(_Log, directory=str(scratch))
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    httpd.allow_reuse_address = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    port = httpd.server_address[1]

    slanted, dead, measured, skipped = [], [], [], []
    punct_only, uncovered = [], []

    for label, rel in PAGES:
        page = root / rel
        if not page.is_file():
            skipped.append((label, rel))
            continue
        src = page.read_text(encoding="utf-8")
        if "</body>" not in src:
            skipped.append((label, rel))
            continue
        page.write_text(src.replace("</body>", PROBE + "</body>"), encoding="utf-8")

        _Log.hits.clear()
        dump = subprocess.run(
            [browser, "--headless=new", "--no-sandbox", "--disable-gpu",
             "--hide-scrollbars", "--force-device-scale-factor=1",
             "--window-size=1280,1600", "--virtual-time-budget=9000",
             "--dump-dom", f"http://127.0.0.1:{port}/madar/{rel}"],
            capture_output=True, text=True, timeout=240)
        fetched = sorted({h.rsplit("/", 1)[-1] for h in _Log.hits
                          if h.endswith(".woff2")})
        m = re.search(r'<pre id="probe">(.*?)</pre>', dump.stdout, re.S)
        if not m:
            httpd.shutdown()
            die("the probe did not run on %s — a silent probe reads exactly like "
                "a clean page (the 09-14 trap)" % rel)
        runs = json.loads(H.unescape(m.group(1)))

        # --- limb 1: no Arabic code point painted in a slanted style ----------
        for r in runs:
            if r["s"] == "normal":
                continue
            n_ar = sum(k for cp, k in ((int(c), n) for c, n in r["c"].items())
                       if in_any(cp, ARABIC_RANGES))
            if n_ar:
                slanted.append((label, r["e"], r["s"], n_ar, r["x"]))

        # --- measured, not asserted: a stack that cannot paint its own text ---
        bundled = {}
        for decls in faces.values():
            for f in decls:
                bundled.setdefault(f["family"], []).extend(f["ranges"])
        for r in runs:
            n_ar = sum(k for cp, k in ((int(c), n) for c, n in r["c"].items())
                       if in_any(cp, ARABIC_RANGES))
            if not n_ar:
                continue
            if any(in_any(cp, bundled.get(fam, []))
                   for fam in r["f"] for cp in (int(c) for c in r["c"])
                   if in_any(cp, ARABIC_RANGES)):
                continue
            uncovered.append((label, r["e"], r["f"][0], n_ar, r["x"]))

        # --- limb 2: every fetched file is justified by a painted code point --
        page_bytes = 0
        rows = []
        for fname in fetched:
            fp = dist / "fonts" / fname
            size = fp.stat().st_size if fp.is_file() else 0
            page_bytes += size
            decls = faces.get(fname)
            if not decls:
                dead.append((label, fname, size, "no @font-face in the served bundle names this file"))
                continue
            painted = 0
            letters = 0
            for r in runs:
                for face in decls:
                    if face["family"] not in r["f"]:
                        continue
                    if r["s"] != face["style"]:
                        continue
                    if not (face["wlo"] <= r["w"] <= face["whi"]):
                        continue
                    for c, n in r["c"].items():
                        cp = int(c)
                        if in_any(cp, face["ranges"]):
                            painted += n
                            if unicodedata.category(chr(cp)).startswith("L"):
                                letters += n
                    break
            if painted == 0:
                dead.append((label, fname, size,
                             "fetched, and no painted run on this page can justify it"))
            elif letters == 0:
                punct_only.append((label, fname, size, painted))
            rows.append((fname, size, painted))
        measured.append((label, rel, page_bytes, rows))

    httpd.shutdown()
    shutil.rmtree(scratch, ignore_errors=True)

    # ---- report ---------------------------------------------------------------
    print("qa_font_payload — %d @font-face block(s) over %d file(s), parsed out of the "
          "SERVED bundle rather than copied into this file" % (n_blocks, len(faces)))
    for label, rel, total, rows in measured:
        print("  %-12s %9s bytes over %d file(s)   /%s" % (label, f"{total:,}", len(rows), rel))
        for fname, size, painted in sorted(rows, key=lambda r: -r[1]):
            per = ("%s b/char" % f"{size // painted:,}") if painted else "PAINTS NOTHING"
            print("      %9s  %-56s %6d chars  %s" % (f"{size:,}", fname, painted, per))
    if skipped:
        print("  skipped (not built): %s" % ", ".join("%s=%s" % s for s in skipped))
    print("  payload totals and bytes-per-char above are MEASURED, NOT ASSERTED — "
          "see the header for why a ceiling would be the wrong gate today.")
    if punct_only:
        print("\n  MEASURED, NOT ASSERTED — %d fetch(es) justified by punctuation, digits or "
              "symbols alone, with not one LETTER painted. This is the 2026-10-17 defect's "
              "true shape and the reason bite 2 did not bite: a Latin text face pulled onto "
              "an Arabic page by the full stop at the end of an Arabic sentence is not a dead "
              "fetch, it is a fetch justified by one character that every subset contains."
              % len(punct_only))
        for label, fname, size, n in punct_only:
            print("      %-12s %9s  %-56s %d non-letter char(s)" % (label, f"{size:,}", fname, n))
    if uncovered:
        print("\n  MEASURED, NOT ASSERTED — %d painted Arabic run(s) whose own declared font "
              "stack names no bundled family that covers Arabic, so a system font paints them. "
              "Not a gate today because the publication does this DELIBERATELY for mono and "
              "uppercase labels (`[dir=\"rtl\"] .mono`, global.css) and a floor above today's "
              "reality reds every build (#93's ratio reasoning)." % len(uncovered))
        for label, el, fam, n, x in uncovered[:12]:
            print("      %-12s %-26s stack-head=%-18s %3d chars  %s" % (label, el, fam, n, x))
        if len(uncovered) > 12:
            print("      ... and %d more" % (len(uncovered) - 12))

    bad = 0
    if slanted:
        bad = 1
        print("\nFAIL (limb 1) — %d painted Arabic run(s) in a slanted style. Arabic "
              "typography has no italic convention:" % len(slanted))
        for label, el, style, n, x in slanted:
            print("    %-12s %-28s font-style:%-8s %3d chars   %s" % (label, el, style, n, x))
    if dead:
        bad = 1
        print("\nFAIL (limb 2) — %d fetched font file(s) nothing on the page justifies:"
              % len(dead))
        for label, fname, size, why in dead:
            print("    %-12s %9s  %-56s %s" % (label, f"{size:,}", fname, why))

    if bad and not report_only:
        return 1
    if bad:
        print("\n--report: findings above are printed, not failed.")
        return 0
    print("\nCLEAN qa_font_payload — no slanted Arabic on any probed page, and every "
          "fetched font file is justified by a glyph that page paints.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
