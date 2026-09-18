#!/usr/bin/env python3
"""
qa_arabic_joining.py — standing assertion 18: the Arabic letters JOINED.

THE QUESTION, AND WHERE IT CAME FROM

Assertion 17 (`qa_arabic_shaping`, 2026-09-17) proves no Arabic run on the site
computes a `letter-spacing` other than `normal`. Its own forward question, written
into the 09-17 QA log the hour it landed, was the honest residue:

    Assertion 17 proves no Arabic run is TRACKED. It does not prove the glyphs
    SHAPED. A missing font, a broken `font-feature-settings`, or tofu would pass
    it in silence, because computed style reports what was ASKED FOR, never what
    the font DELIVERED.

That is #55's LAYER question one layer further out: 17 reads the cascade's output,
which is still an instruction. This reads the shaping engine's output, which is a
measurement.

THE CANDIDATE ORACLE THE 09-17 LOG NAMED — AND WHY IT IS UNSOUND

Quoted from that log: "measure its advance width against the same string rendered
with `letter-spacing` forced ... if the two widths are identical the font is not
shaping." Tested on 2026-09-18 before anything was built on it, and it fails on a
healthy page, in two independent ways:

  1. It cannot run on this site at all. Ruling #55's fix is
     `:lang(ar){letter-spacing:normal!important}` — so `letter-spacing` CANNOT be
     forced onto an Arabic element here any more. Measured: the forced-tracking
     width equals the natural width to the pixel, on all four probe strings. The
     proposed check would read "identical" — its own failure condition — on a page
     that is completely correct. **A rule and the instrument proposed to succeed it
     were written hours apart in the same artefact, and they are incompatible.**
  2. Even where it could run, the inference is wrong. Forcing tracking widens both
     a shaped and an unshaped run, so the comparison measures tracking, not joining.

THE ORACLE THAT WORKS: U+200C

Compare the run against ITSELF with U+200C ZERO WIDTH NON-JOINER between every
pair of letters. ZWNJ is the Unicode-defined suppression of joining, so the second
string is the known-unshaped case — same font, same size, same page, same line —
a control by construction rather than a font we must arrange to be missing (the
control the 09-17 log said the operation did not have; it turns out not to need
one). A cursive run that shaped is NARROWER than its own de-joined letters,
because medial and final forms are narrower than isolated ones and lam-alef is a
ligature. Measured on the real Arabic home page, natural / de-joined:

    بببب      0.433        العربية   0.518        لا  0.783 (ligature)
    مدار      0.972   <-- and this is why the brand is not the probe

`مدار` has exactly one join in it: dal and alef do not connect leftward, so a
correctly shaped `مدار` is 3% narrower than a broken one and no threshold can tell
them apart. **The probe string is chosen for joining density, never for being ours.**

TWO HALVES, BECAUSE THERE ARE TWO DEFECTS

  FONT     — a fixed, joining-dense probe rendered in the page's own inherited
             Arabic font. Fires when the resolved face does not shape.
  SERVED   — the page's own longest real Arabic run. Fires when the CONTENT or the
             CSS breaks joining (a stray ZWNJ or RLM in a field, a
             `font-feature-settings` that disables `init/medi/fina`) while the font
             is perfectly capable.

They are independent and both are needed: the 09-17 defect was in the CSS and the
font was fine, and a font outage would leave the served text unchanged.

WHAT THIS CANNOT SEE, SAID PLAINLY (the same honesty assertion 17 owed)

The Arabic face is **Amiri, fetched from fonts.googleapis.com at read time** — a
third party we do not own, on the reader's network, not ours. This check measures
the font THIS RUNNER resolved. A reader behind a proxy that blocks Google Fonts, or
on a system with no Arabic face at all, gets a fallback we have never measured and
this assertion will never see. Ruling #16 says judge in the environment that
judges, and the environment that judges an Arabic webfont is the reader's browser,
which is exactly the one environment CI is not. What this DOES gate is every
shaping defect that is a property of our own bytes — which is the whole of what we
have ever shipped.

Proved per ruling #35, four ways, every injection verified to have changed the
artefact before the check read it (the 2026-09-14 discipline):
  control — silent on the real build;
  bite A  — `font-feature-settings` disabling init/medi/fina injected into the
            built CSS: both halves fire, ratios go to 1.000;
  bite B  — ZWNJ injected into one page's served Arabic text: the SERVED half
            fires and the FONT half stays clean, proving the halves independent;
  bite C  — non-vacuity: a page stripped of its Arabic fails the floor rather
            than passing with nothing to measure.

Usage: qa_arabic_joining.py <dist-dir>
Exit 0 = PASS, 1 = defects found, 2 = could not check (counts as a failure).
"""
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

# The joining-dense probe. Four beh (connects both sides, four forms) plus the
# cross-language link's own word, which is the string an English reader actually
# clicks to reach the Arabic edition.
PROBE_STRINGS = ["بببب", "العربية"]

# label, path, minimum Arabic-bearing elements expected (the non-vacuity floor)
TARGETS = [
    ("AR home", "/madar/ar/", 20),
    ("AR article", "/madar/ar/articles/2026-05-25-bo-teacher-chalk/", 20),
    ("EN home", "/madar/", 2),
    ("VALENCE", "/madar/valence/", 1),
]

# A shaped, joining-dense run is far narrower than its de-joined self; the measured
# spread on a healthy build is 0.43-0.52. A run that did not shape measures 1.000
# exactly, because the de-joined string IS the unshaped string. The thresholds sit
# in the wide empty middle, not near either edge.
FONT_MAX = 0.75
SERVED_MAX = 0.90
SERVED_MIN_LEN = 12  # shorter runs carry too few joins to measure; see مدار above

PROBE = """<!doctype html>
<html><head><meta charset="utf-8"><title>probe</title></head><body><script>
(function () {
  var AR = /[\\u0620-\\u064A\\u066E-\\u06D3]/;
  var f = document.createElement('iframe');
  f.style.width='1200px'; f.style.height='1400px'; f.style.border='0';
  f.addEventListener('load', function () {
    try {
      var d = f.contentDocument, w = f.contentWindow;
      // Not every element carrying Arabic is TEXT a reader receives, and not every
      // string carrying Arabic is an Arabic string. The first draft of this check
      // selected "the longest text containing any Arabic" and chose the JSON-LD
      // block — 4,000 characters of Latin schema.org with the publication's Arabic
      // name inside it — then reported a ratio of 0.998 against a perfect build.
      // A selection rule scoped wider than the thing it selects finds the right
      // string for the wrong reason (2026-09-14, the masking trap).
      var SKIP = {SCRIPT:1, STYLE:1, NOSCRIPT:1, TEMPLATE:1, TITLE:1, META:1};
      var FMT = /[\\u00AD\\u200B-\\u200F\\u202A-\\u202E\\u2060-\\u2064\\u2066-\\u2069\\uFEFF]/g;
      function arabicCount(t){ var m = t.match(/[\\u0620-\\u064A\\u066E-\\u06D3]/g); return m ? m.length : 0; }
      var all = d.querySelectorAll('*'), seen = 0, host = null, longest = '', best = 0;
      for (var i=0;i<all.length;i++){
        var el = all[i], own = '', n = el.childNodes;
        if (SKIP[el.tagName]) continue;
        for (var j=0;j<n.length;j++) if (n[j].nodeType===3) own += n[j].nodeValue;
        if (!AR.test(own)) continue;
        seen++;
        if (!host) host = el;
        var t = own.replace(/\\s+/g,' ').trim();
        // Zero-width format characters are struck from the DENSITY denominator and
        // left in the MEASURED string. They must be: a de-joined run is by
        // definition a run stuffed with invisible non-Arabic characters, so counting
        // them would drop the density below any threshold and make this check
        // structurally unable to select the one text it exists to catch. The first
        // version did count them, and the ZWNJ bite fired as "no Arabic run long
        // enough to measure" instead of "this run did not join" — a check that could
        // not run, wearing the costume of a check that found something.
        var dense = t.replace(/\\s/g,'').replace(FMT,'').length;
        var ar = arabicCount(t);
        // Predominantly Arabic, or it cannot testify about Arabic joining.
        if (dense === 0 || ar / dense < 0.8) continue;
        if (ar > best) { best = ar; longest = t; host = el; }
      }
      if (!host) { document.title='QAJOIN:'+JSON.stringify({seen:0}); return; }

      var cs = w.getComputedStyle(host);
      // The `font:` SHORTHAND resets font-feature-settings, font-variant-ligatures
      // and font-kerning to their initial values — which are exactly the properties
      // a shaping defect lives in. A probe built from the shorthand carries the
      // page's typeface and discards the page's shaping instructions, and would have
      // been structurally blind to the defect class this assertion exists for.
      // Copy the longhands, individually, after the layout properties.
      var FONT_PROPS = ['fontFamily','fontSize','fontWeight','fontStyle','fontStretch',
                        'fontFeatureSettings','fontVariantLigatures','fontKerning',
                        'fontVariationSettings','fontSynthesis','textRendering'];
      function measure(text) {
        var s = d.createElement('span');
        // letter-spacing:normal is asserted separately by assertion 17; pinning it
        // here keeps THIS measurement about joining and nothing else.
        s.style.cssText = 'position:absolute;visibility:hidden;white-space:pre;'
          + 'left:-9999px;top:0;letter-spacing:normal;';
        for (var q=0;q<FONT_PROPS.length;q++) {
          var v = cs[FONT_PROPS[q]];
          if (v) s.style[FONT_PROPS[q]] = v;
        }
        s.textContent = text;
        d.body.appendChild(s);
        var wd = s.getBoundingClientRect().width;
        s.parentNode.removeChild(s);
        return wd;
      }
      function dejoin(t){ return t.split('').join('\\u200C'); }
      function ratio(t){
        var a = measure(t), b = measure(dejoin(t));
        return { natural: a, dejoined: b, ratio: (b > 0 ? a / b : null) };
      }

      var probes = {};
      var P = %(probes)s;
      for (var k=0;k<P.length;k++) probes[P[k]] = ratio(P[k]);

      document.title = 'QAJOIN:' + JSON.stringify({
        seen: seen,
        fontFamily: cs.fontFamily,
        probes: probes,
        served: { text: longest.slice(0, 60), length: longest.length,
                  metrics: best >= %(minlen)d ? ratio(longest) : null, arabic: best }
      });
    } catch (e) { document.title='QAJOIN:'+JSON.stringify({error:String(e)}); }
  });
  f.src = '%(target)s';
  document.body.appendChild(f);
})();
</script></body></html>
"""


def serve(dist: pathlib.Path):
    root = tempfile.mkdtemp(prefix="qa_join_root_")
    shutil.copytree(dist, os.path.join(root, "madar"))

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=root, **kw)

        def log_message(self, *a):
            pass

    httpd = socketserver.TCPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, httpd.server_address[1], root


def probe(browser: str, root: str, port: int, path: str):
    page = PROBE % {
        "probes": json.dumps(PROBE_STRINGS),
        "minlen": SERVED_MIN_LEN,
        "target": f"http://127.0.0.1:{port}{path}",
    }
    fd, probe_path = tempfile.mkstemp(suffix=".html", dir=os.path.join(root, "madar"))
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(page)
    url = f"http://127.0.0.1:{port}/madar/{os.path.basename(probe_path)}"
    profile = tempfile.mkdtemp(prefix="qa_join_profile_")
    try:
        res = subprocess.run(
            [browser, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             "--window-size=1200,1400", f"--user-data-dir={profile}",
             "--virtual-time-budget=8000", "--dump-dom", url],
            capture_output=True, text=True, timeout=120,
        )
        m = re.search(r"QAJOIN:(\{.*?\})</title>", res.stdout, re.S)
        return json.loads(m.group(1)) if m else None
    except subprocess.TimeoutExpired:
        # A hung browser fails legibly, not as a traceback. It still FAILS: a check
        # that cannot run has not passed (RUNBOOK 2026-09-13, and the 09-17 addendum
        # that hardened assertion 17 for exactly this).
        return {"error": "the browser did not return within 120s on this target"}
    finally:
        shutil.rmtree(profile, ignore_errors=True)
        try:
            os.unlink(probe_path)
        except OSError:
            pass


def main() -> int:
    dist = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "")
    if not dist.is_dir():
        print("usage: qa_arabic_joining.py <dist-dir>")
        return 2
    browser = next((b for b in ("google-chrome", "chromium", "chromium-browser",
                                "google-chrome-stable") if shutil.which(b)), None)
    if not browser:
        print("qa_arabic_joining: no headless chrome on PATH — cannot check, which is a failure")
        return 2

    print(f"qa_arabic_joining: {dist.resolve()}")
    httpd, port, root = serve(dist)
    defects: list[str] = []
    measured = 0
    worst_font = 0.0
    worst_served = 0.0
    try:
        for label, path, floor in TARGETS:
            rep = probe(browser, root, port, path)
            if rep is None:
                defects.append(f"{label} ({path}) — the probe returned nothing")
                continue
            if "error" in rep:
                defects.append(f"{label} ({path}) — {rep['error']}")
                continue
            seen = rep.get("seen", 0)
            if seen < floor:
                defects.append(
                    f"{label} ({path}) — only {seen} Arabic-bearing element(s), floor is {floor}; "
                    "a check with nothing to measure has failed, not passed"
                )
                continue

            for text, m in rep.get("probes", {}).items():
                r = m.get("ratio")
                if r is None:
                    defects.append(f"{label} — probe {text!r} measured zero width")
                    continue
                measured += 1
                worst_font = max(worst_font, r)
                if r > FONT_MAX:
                    defects.append(
                        f"{label} — the resolved Arabic face did not JOIN: probe {text!r} is "
                        f"{m['natural']:.1f}px against {m['dejoined']:.1f}px de-joined "
                        f"(ratio {r:.3f} > {FONT_MAX}); font-family {rep.get('fontFamily')!r}"
                    )

            served = rep.get("served") or {}
            sm = served.get("metrics")
            if sm is None:
                defects.append(
                    f"{label} — no Arabic run of {SERVED_MIN_LEN}+ characters to measure "
                    f"(longest predominantly-Arabic run held {served.get('arabic', 0)} Arabic characters); too few joins to judge"
                )
            elif sm.get("ratio") is None:
                defects.append(f"{label} — the served Arabic run measured zero width")
            else:
                measured += 1
                worst_served = max(worst_served, sm["ratio"])
                if sm["ratio"] > SERVED_MAX:
                    defects.append(
                        f"{label} — the SERVED Arabic did not join: {served['text']!r} is "
                        f"{sm['natural']:.1f}px against {sm['dejoined']:.1f}px de-joined "
                        f"(ratio {sm['ratio']:.3f} > {SERVED_MAX}) — the font joins, so this is "
                        "our own bytes: a de-joining character in the text, or CSS disabling the "
                        "shaping features"
                    )
    finally:
        httpd.shutdown()
        shutil.rmtree(root, ignore_errors=True)

    if measured == 0:
        print("qa_arabic_joining: nothing was measured at all — a failure, not a pass")
        return 2
    if defects:
        for d in defects:
            print("DEFECT:", d)
        print(f"qa_arabic_joining: {len(defects)} defect(s) across {len(TARGETS)} target(s)")
        return 1
    print(
        f"CLEAN qa_arabic_joining — {len(TARGETS)} targets, {measured} runs measured against "
        f"their own de-joined selves; every one shaped. Worst font probe {worst_font:.3f} "
        f"(threshold {FONT_MAX}), worst served run {worst_served:.3f} (threshold {SERVED_MAX}) "
        f"— printed so the margin is visible rather than merely sufficient"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
