#!/usr/bin/env python3
"""
qa_selector_coverage — standing assertion #41: every selector this build SHIPS
matches at least one element on at least one page that LOADS it, or it is in
this file's register with a class and a reason.

WHY THIS IS THE FORTY-FIRST AND NOT A VARIANT OF ONE OF THE OTHER FORTY.

Every instrument this operation owns reads an OUTPUT and asks whether the output
is right. This one reads the STYLESHEET and asks whether the stylesheet's own
statement ever reaches an output. The difference is not a refinement; it is a
direction. A rule that matches nothing leaves nothing in the output to read
(#103), so no comparison of two served bytes can ever see it — the same shape as
#117's tense, where the falsifying agent is the calendar rather than a byte, and
#115's font payload, where the subject does not exist until render time.

The direction matters because of what it catches going the other way. A
previously-matched selector that stops matching is a MARKUP REGRESSION: the rule
still states the design and the markup walked away from it. Delete the
`<h2 class="subhead">Sources</h2>` and nothing in this operation notices, because
`qa_render` renders what is there and `qa_composition` compares what is there
against itself. This gate notices, because `.subhead` would leave the matched set
and enter an unmatched set the register does not license. **A stylesheet is a
specification of the markup, and it is the only one this repository keeps in
machine-readable form.**

ITEM 21'S RE-SPECIFICATION (#118) IS THE DESIGN, AND IT HAS FOUR BUCKETS, NOT TWO.
  Item 21 asked for a byte count and #118 replaced it with a partition:
  *superseded* (the design moved on, the rule is residue) or **orphaned** (the
  design stands and the markup walked away), because deleting an orphaned rule
  destroys the only surviving statement of what the document was supposed to look
  like. Measured over the real population, two buckets cannot hold it: 27 of the
  43 unmatched selectors are neither — they are the untaken branch of a template
  that is working exactly as designed, including the CHARTER-mandated CSS-only
  wordmark fallback, which is REQUIRED to match nothing while the SVG is present.
  Calling those residue would have deleted a non-negotiable. So the register
  carries four classes, and that is #57/#70 pointed at a specification instead of
  at a count: *a bucket set is an enumeration too, and it cannot report a
  distinction it cannot hold.*

    CONDITIONAL  the markup is emitted by a template branch the current content
                 does not take. Correct by design. Matching nothing is the
                 feature. (27)
    LATENT       a bare element-type or element-in-context rule for an element
                 the corpus happens not to contain. Defensive typography; this
                 is how standing-queue item 57's class is absorbed rather than
                 re-introduced. (10)
    ORPHANED     the design stands, stated somewhere outside the stylesheet, and
                 the markup walked away. It is an unfiled defect report about the
                 markup, and the report is the output. (1)
    SUPERSEDED   the design moved on; the rule is residue. (5)

  THE CLASS BOUNDARY IS MEASURED, NEVER READ OFF THE RULE — AND THAT COST TWO
  FABRICATED DEFECTS IN ONE HOUR, BOTH IN THE SAME DIRECTION.
  `hr.rule` was classified ORPHANED first, on the reasoning that markdown cannot
  attach a class so the design must have walked away, and a global `re.sub` was
  used to restore "the defect" for the proof. That substitution rewrote THREE
  rules, not one, because both article templates re-state the thematic break
  scoped to their own `.body-main`. With all three broken the probe reported the
  user agent's inset groove and read exactly like a confirmed 160-day published
  defect. It was not one: the five served breaks have computed to 1px solid
  rgba(14,27,44,0.18) with 54px block margins since 2026-05-25. `.pullquote` was
  classified ORPHANED on the same reasoning and was wrong the same way — the
  article templates restate all twelve of its declarations as
  `.body-main :global(blockquote)`, and six blockquotes are served.
  *A bite wider than the rule it targets manufactures the defect it was aimed at,
  and a manufactured defect reads exactly like a found one* — #114's "a bite
  aimed at the specification tests the specification", one turn further in.
  So: every SUPERSEDED entry below names what superseded it, and the naming was
  found by grepping the built CSS for the element the rule targets, never by
  reading the rule's shape. **All five superseded entries have ONE cause** —
  markdown cannot attach a class — which makes item 21's answer the opposite of
  its question: 43 of the 44 unmatched selectors are not dead weight at all.

WHAT IS ASSERTED, AND WHAT IS ONLY PRINTED (#93).
  LIMB 1 — every unmatched selector in a sheet this gate can measure is in the
  register. A new rule that matches nothing fails the build, and so does markup
  that walks away from an old one.
  LIMB 2 — every register entry is still present in the shipped CSS and still
  unmatched. A register cannot rot: an entry whose selector started matching, or
  whose rule was deleted, fails the build and must be struck. This is the half
  that #114's seeded register did not have, and it is cheap here because the
  register is hand-written and this tool writes nothing.
  PRINTED, NOT ASSERTED — `valence/index.html`'s inline block. It is a
  scroll-and-JS-driven instrument whose markup and whose classes are written at
  runtime by template literals; item 58's closure measured that directly (10 of
  its 13 defective headings were absent from the served bytes a static parse
  reads). A static answer about it is an answer about the probe, not about the
  document — the 09-14 trap — so its 87 unmatched selectors are reported with
  that sentence attached and gate nothing.

WHAT THE ORACLE IS, AND WHAT IT CANNOT SEE.
  `document.querySelectorAll` in a headless Chrome, over the served bytes of
  every page, parsed with `DOMParser`. One browser launch, the full population of
  135 documents rather than a sample (standing-queue item 41's question, answered
  by construction rather than by promise).
  It cannot see a class a script adds after load. One selector is registered as
  such and named. It also cannot see which rule WINS — that is #109's boundary
  and this gate does not cross it: a matched selector is a selector whose subject
  exists, never a selector whose declaration paints.
  State pseudo-classes and pseudo-elements are stripped before asking, because a
  rule targeting `:hover` is about an element that EXISTS and is not currently
  hovered. The stripping is longest-first with a `(?![\\w-])` boundary: with a
  plain `\\b`, `:focus` matches inside `:focus-visible` and leaves `a-visible`, a
  selector that matches nothing and reads exactly like a dead rule. That false
  positive was in this harness's first run, which is #109's own lesson — *a
  composition check's error rate is set by whether it knows the intended
  assembly* — met again one instrument later.
  Astro's `data-astro-cid-<hash>` is normalised to `[data-astro-cid-*]` in the
  register. The hash is a per-component content hash, so without this a wholly
  unrelated edit to a component rehashes every one of its selectors, the register
  goes stale, the build goes red for no defect, and the gate gets switched off
  inside a week (09-13).

Exit 0 clean · 1 a limb failed · 2 cannot measure · 4 refused.
Python 3, no deps, needs a headless Chrome.
"""

import functools
import html as H
import http.server
import json
import pathlib
import re
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading

BROWSERS = ("google-chrome-stable", "google-chrome", "chromium-browser", "chromium")

# Sheets whose unmatched set is PRINTED and not asserted, with the reason.
NOT_ASSERTED = {
    "inline:valence/index.html":
        "a scroll-and-JS-driven instrument whose markup and classes are written "
        "at runtime by template literals (item 58's closure measured 10 of 13 "
        "defective headings absent from the served bytes); a static answer here "
        "is an answer about the probe, not the document",
}

# State / dynamic pseudo-classes. A rule targeting one of these is about an
# element that exists and is not currently in that state.
DYN = ("hover", "focus", "focus-visible", "focus-within", "active", "visited",
       "link", "any-link", "target", "target-within", "checked", "indeterminate",
       "disabled", "enabled", "read-only", "read-write", "placeholder-shown",
       "default", "valid", "invalid", "in-range", "out-of-range", "required",
       "optional", "user-valid", "user-invalid", "autofill", "defined", "modal",
       "popover-open", "fullscreen", "picture-in-picture")

PSEUDO_EL = ("before", "after", "placeholder", "selection", "marker",
             "first-line", "first-letter", "backdrop", "file-selector-button",
             "cue", "part", "slotted", "details-content", "spelling-error",
             "grammar-error", "target-text", "view-transition", "highlight",
             "scroll-marker", "scroll-button")

# ---------------------------------------------------------------------------
# THE REGISTER. Hand-written. This tool has no --emit and writes nothing, for
# #114's reason: a tool that seeds its own licence is a check reading its answer
# off the field it supplements. Every entry is a selector that matches nothing
# today, with the class it falls in and the evidence for that class.
# ---------------------------------------------------------------------------
REGISTER = {
    # ---- CONDITIONAL — an untaken template branch. Matching nothing is correct.
    ".mark-latin[data-astro-cid-*]": ("CONDITIONAL",
        "SiteHeader.astro's else-branch: the CHARTER-mandated CSS-only typographic "
        "fallback, rendered only when the wordmark SVG is absent. REQUIRED to match "
        "nothing while the SVG is present"),
    ".mark-divider[data-astro-cid-*]": ("CONDITIONAL",
        "SiteHeader.astro wordmark fallback, same branch as .mark-latin"),
    ".mark-arabic[data-astro-cid-*]": ("CONDITIONAL",
        "SiteHeader.astro wordmark fallback, same branch as .mark-latin"),
    ".masthead__mark-latin[data-astro-cid-*]": ("CONDITIONAL",
        "pages/index.astro masthead wordmark fallback, same shape"),
    ".masthead__mark-divider[data-astro-cid-*]": ("CONDITIONAL",
        "pages/index.astro masthead wordmark fallback, same shape"),
    ".masthead__mark-arabic[data-astro-cid-*]": ("CONDITIONAL",
        "pages/index.astro masthead wordmark fallback, same shape"),
    ".masthead__fallback[data-astro-cid-*]": ("CONDITIONAL",
        "pages/ar/index.astro masthead wordmark fallback, same shape"),
    ".edition__tag[data-astro-cid-*]": ("CONDITIONAL",
        "the 'Current' tag on the editions index, emitted only when an edition is "
        "open. No edition is open since Edition 05 closed 2026-10-13, and the "
        "status flag was corrected to match on 2026-10-31 (item 62)"),
    ".edition__empty[data-astro-cid-*]": ("CONDITIONAL",
        "the empty-state line for an edition registry row with no pieces; every "
        "row has pieces"),
    ".placeholder[data-astro-cid-*]": ("CONDITIONAL",
        "empty-state block on the home pages and the article template, emitted "
        "only when a listing has nothing to list"),
    ".placeholder[data-astro-cid-*] h2[data-astro-cid-*]": ("CONDITIONAL",
        "inside the empty-state block above"),
    ".placeholder[data-astro-cid-*] p[data-astro-cid-*]": ("CONDITIONAL",
        "inside the empty-state block above"),
    ".placeholder__lead[data-astro-cid-*]": ("CONDITIONAL",
        "pages/ar/index.astro empty-state lead"),
    ".placeholder__lead[data-astro-cid-*] a[data-astro-cid-*]": ("CONDITIONAL",
        "inside the empty-state lead above"),
    ".excerpts[data-astro-cid-*]": ("CONDITIONAL",
        "pages/ar/index.astro excerpts block, emitted only when the Arabic front "
        "door has English-only pieces to excerpt; AR parity is 100 per cent"),
    ".excerpts__head[data-astro-cid-*]": ("CONDITIONAL", "inside the excerpts block"),
    ".excerpts__lead[data-astro-cid-*]": ("CONDITIONAL", "inside the excerpts block"),
    ".excerpts__lead[data-astro-cid-*] a[data-astro-cid-*]": ("CONDITIONAL",
        "inside the excerpts block"),
    ".excerpts__list[data-astro-cid-*]": ("CONDITIONAL", "inside the excerpts block"),
    ".excerpt[data-astro-cid-*]": ("CONDITIONAL", "inside the excerpts block"),
    ".excerpt__en[data-astro-cid-*]": ("CONDITIONAL", "inside the excerpts block"),
    ".excerpt__ar[data-astro-cid-*]": ("CONDITIONAL", "inside the excerpts block"),
    ".sources__title[data-astro-cid-*]": ("CONDITIONAL",
        "a source whose URL is an example.com placeholder is rendered as a span "
        "instead of a link; no published piece carries a placeholder URL"),
    ".sources__note[data-astro-cid-*]": ("CONDITIONAL",
        "the provisional-sources note, emitted only when a piece has placeholder "
        "URLs; see .sources__title"),
    ".title-block__draft[data-astro-cid-*]": ("CONDITIONAL",
        "the draft badge on an article page; no served piece is a draft"),
    ".pill": ("CONDITIONAL",
        "'Draft - pending source verification' badge in pages/index.astro and the "
        "article template; no served piece is a draft"),
    ".share-rail__toast[data-astro-cid-*].is-visible": ("CONDITIONAL",
        "the copy-link toast's visible state, added by ShareRail.astro's script "
        "after a click. The element exists; the class is runtime state this "
        "oracle cannot and should not simulate"),

    # ---- LATENT — defensive rules for elements the corpus does not contain.
    "h4": ("LATENT",
        "no served document carries an h4 since items 54 and 58 repaired 89 of "
        "135 documents to h2 and valence's thirteen to h3. The rule stays: "
        "deleting it is how item 57's class returns the day somebody adds one"),
    "h5": ("LATENT", "no served document carries an h5; same reasoning as h4"),
    "h6": ("LATENT", "no served document carries an h6; same reasoning as h4"),
    # STRUCK 2026-11-01, hours after it was written, by limb 2 and by real work
    # rather than by an injection: `[dir=rtl] h3` was registered LATENT because
    # h3 was served on two EN pages and no Arabic page used one. The growth
    # function then gave the Arabic editions index its own standing section with
    # an h3 item, the selector started matching, and the build went red until
    # this entry came out. That is the register-cannot-rot half proved on the
    # day it shipped, and it is the whole reason limb 2 exists: #114's seeded
    # register had no way to notice its own entries going stale.
    "[dir=rtl] h4": ("LATENT", "no h4 anywhere; the RTL half of the h4 rule"),
    "[dir=rtl] i": ("LATENT",
        "no <i> element is served on any Arabic page. One of the stylesheet's "
        "three statements that Arabic is not slanted (#115 limb 1 asserts the "
        "property itself, so this rule is belt and braces)"),
    "[dir=rtl] cite": ("LATENT",
        "no <cite> element is served anywhere; the only markup that would produce "
        "one is the pullquote attribution, which is ORPHANED below"),
    ".lead__title[data-astro-cid-*] em[data-astro-cid-*]": ("LATENT",
        "an <em> inside a lead title. Markdown can produce one; no current title "
        "does"),
    ".secondary__title[data-astro-cid-*] em[data-astro-cid-*]": ("LATENT",
        "an <em> inside a secondary title; same as .lead__title em"),
    ".title[data-astro-cid-*] em[data-astro-cid-*]": ("LATENT",
        "an <em> inside an article title; same as .lead__title em"),
    ".orange": ("LATENT",
        "a one-declaration colour utility in global.css. No markup uses it, and "
        "SYSTEM.md states what it is for - 'orange is what changed, what crossed "
        "a threshold' - so it is a utility awaiting a consumer rather than "
        "residue. Related: standing-queue item 53 on the utility layer"),

    # ---- ORPHANED — the design stands elsewhere and the markup walked away.
    #      Exactly ONE, and it is filed as standing-queue item 66.
    ".body-grid--resumed": ("ORPHANED",
        "a body grid that resumes after a full-bleed interruption takes zero top "
        "margin. The markup exists in all three design-assets article mockups "
        "(<div class='body-grid body-grid--resumed'>) and in no Astro template. "
        "Standing-queue item 66"),

    # ---- SUPERSEDED — the design moved on, and every one of these five moved
    #      for ONE reason: markdown cannot attach a class. The design system was
    #      authored as hand-built HTML with classes (the three article mockups),
    #      the publication's bodies are markdown, so each classed body rule had
    #      to be restated as an ELEMENT selector scoped to `.body-main`, and the
    #      classed original is the residue. Standing-queue item 67.
    ".pullquote": ("SUPERSEDED",
        "superseded by `.body-main :global(blockquote)` in BOTH article "
        "templates, which restates all twelve of this rule's declarations "
        "(--fs-pullquote, --tr-pullquote, the 2px --color-orange inline-start "
        "border) and differs only in max-width, 34ch against 32ch. Markdown "
        "produces `> quote` as a bare <blockquote> and cannot attach a class. "
        "Measured, not assumed: SIX blockquotes are served across six documents, "
        "so 'the only orange typographic event in the body' that global.css:243 "
        "promises DOES reach the reader - through the element, not the class"),
    ".pullquote cite": ("SUPERSEDED",
        "the pullquote's attribution line. Markdown has no syntax for a <cite> "
        "inside a blockquote, so the attribution is written as body text; see "
        ".pullquote"),
    "[dir=rtl] .pullquote": ("SUPERSEDED",
        "the RTL half, superseded by the Arabic article template's own "
        "`.body-main :global(blockquote)`. It is cited by name in "
        "SiteFooter.astro's comment and in qa_font_payload's header as one of the "
        "two places this stylesheet had already said Arabic is not slanted - and "
        "the Arabic template says it a third time, at "
        "`.body-main :global(em) { font-style: normal }`, which is why #115 limb 1 "
        "is green"),
    "hr.rule": ("SUPERSEDED",
        "markdown cannot attach a class, so a `---` in an article body produces a "
        "bare <hr> and this selector can never be reached. It is SUPERSEDED and "
        "not ORPHANED, and the difference was MEASURED rather than assumed: both "
        "article templates re-state the same rule scoped to their own .body-main "
        "with --space-xl and width:50%, and all five served breaks compute to "
        "1px solid rgba(14,27,44,0.18) with 54px block margins. Nothing is "
        "broken. The thematic break is stated three times, twice per-component "
        "and once here unreachably - 2026-10-25's slanted-Arabic shape one "
        "instrument later. Consolidation is standing-queue item 67"),
    ".still__field svg": ("SUPERSEDED",
        "the hero still is served as <img src='...svg'> with authored alt text, "
        "not as an inlined <svg>. Inlining is the rule for brand-critical chrome "
        "only (CHARTER); a hero still is content and carries an alt string, so "
        "the <img> is the design rather than a regression"),
}

PROBE = r"""<script>
window.__done = 0;
(async function(){
  var PLAN = __PLAN__;            // [{page, sels:[...]}]
  var out = {};
  for (var i=0;i<PLAN.length;i++){
    var job = PLAN[i], doc = null;
    try {
      var r = await fetch(job.page);
      var txt = await r.text();
      doc = new DOMParser().parseFromString(txt, 'text/html');
    } catch (e) { out['!'+job.page] = 'fetch-failed'; continue; }
    var hits = [];
    for (var j=0;j<job.sels.length;j++){
      var n = -1;
      try { n = doc.querySelectorAll(job.sels[j]).length; } catch (e) { n = -2; }
      if (n !== 0) hits.push([j, n]);
    }
    out[job.page] = hits;
  }
  var pre = document.createElement('pre'); pre.id = 'probe';
  pre.textContent = JSON.stringify(out);
  document.body.appendChild(pre);
  window.__done = 1;
})();
</script>"""


def die(msg, code=2):
    print("REFUSED qa_selector_coverage — %s" % msg if code == 4
          else "ERROR qa_selector_coverage — %s" % msg)
    sys.exit(code)


def find_browser():
    for c in BROWSERS:
        p = subprocess.run(["which", c], capture_output=True, text=True)
        if p.returncode == 0:
            return p.stdout.strip()
    return None


def strip_comments(t):
    return re.sub(r"/\*.*?\*/", " ", t, flags=re.S)


def style_rules(css):
    """Every style rule's selector list, with its at-rule context."""
    css = strip_comments(css)
    out, stack, i, n, buf = [], [], 0, len(css), ""
    while i < n:
        c = css[i]
        if c == "{":
            head, buf = buf.strip(), ""
            if head.startswith("@"):
                stack.append(head)
                i += 1
                continue
            depth, j = 1, i + 1
            while j < n and depth:
                if css[j] == "{":
                    depth += 1
                elif css[j] == "}":
                    depth -= 1
                j += 1
            out.append((head, tuple(stack)))
            i = j
            continue
        if c == "}":
            if stack:
                stack.pop()
            buf = ""
            i += 1
            continue
        buf += c
        i += 1
    return out


def split_list(s):
    parts, depth, cur = [], 0, ""
    for ch in s:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return [p.strip() for p in parts if p.strip()]


def normalise(sel):
    """Strip pseudo-elements and state pseudo-classes. LONGEST FIRST, and the
    boundary is (?![\\w-]) rather than \\b -- see the header."""
    s = sel
    for p in sorted(PSEUDO_EL, key=len, reverse=True):
        s = re.sub(r"::?" + re.escape(p) + r"(?![\w-])(\([^)]*\))?", "", s, flags=re.I)
    s = re.sub(r"::-[a-z-]+(\([^)]*\))?", "", s, flags=re.I)
    for p in sorted(DYN, key=len, reverse=True):
        s = re.sub(r":" + re.escape(p) + r"(?![\w-])(\([^)]*\))?", "", s, flags=re.I)
    s = re.sub(r"\s+", " ", s).strip()
    if s in ("", ">", "+", "~"):
        return None
    return s


def key_of(sel):
    """Register key: Astro's per-component content hash normalised away."""
    return re.sub(r"data-astro-cid-[a-z0-9]+", "data-astro-cid-*", sel)


class _Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    report_only = "--report" in sys.argv
    dist = pathlib.Path(argv[0] if argv else "web/dist").resolve()
    if not dist.is_dir():
        die("no dist at %s" % dist)
    browser = find_browser()
    if not browser:
        die("no headless Chrome on this runner; this assertion cannot be faked green")

    pages = sorted(p for p in dist.rglob("*.html"))
    if not pages:
        die("found 0 html pages under %s" % dist)

    # --- which sheets does each page load, and what inline blocks does it carry
    loads = {}          # page relpath -> set of sheet labels
    sheet_css = {}      # sheet label -> css text
    for p in pages:
        rel = str(p.relative_to(dist))
        t = p.read_text(encoding="utf-8", errors="replace")
        labels = set()
        for tag in re.findall(r"<link\b[^>]*>", t):
            if "stylesheet" not in tag:
                continue
            m = re.search(r'href="([^"]+)"', tag)
            if not m:
                continue
            key = m.group(1).split("/madar/", 1)[-1].lstrip("/")
            f = dist / key
            if f.is_file():
                labels.add(key)
                sheet_css.setdefault(key, f.read_text(encoding="utf-8", errors="replace"))
        blocks = re.findall(r"<style[^>]*>(.*?)</style>", t, re.S)
        if blocks:
            lbl = "inline:" + rel
            labels.add(lbl)
            sheet_css[lbl] = "\n".join(blocks)
        loads[rel] = labels
    if not sheet_css:
        die("parsed 0 stylesheets out of %d served pages" % len(pages))

    # --- the selector universe, per sheet
    universe = {}       # sheet label -> {register key -> (raw sel, probe sel)}
    for lbl, css in sheet_css.items():
        rules = style_rules(css)
        got = {}
        for head, ctx in rules:
            if any(a.startswith(("@keyframes", "@font-face", "@property",
                                 "@counter-style")) for a in ctx):
                continue
            for sel in split_list(head):
                probe = normalise(sel)
                if probe is None:
                    continue
                got.setdefault(key_of(sel), (sel, probe))
        universe[lbl] = got

    pages_of = {}       # sheet label -> [page relpaths]
    for rel, labels in loads.items():
        for lbl in labels:
            pages_of.setdefault(lbl, []).append(rel)

    # --- one browser launch; DOMParser over the served bytes of every page
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="qa_selcov_"))
    root = scratch / "madar"
    shutil.copytree(dist, root)
    handler = functools.partial(_Q, directory=str(scratch))
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    httpd.allow_reuse_address = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    port = httpd.server_address[1]

    plan, index = [], []
    for rel in sorted(loads):
        sels, keys = [], []
        for lbl in sorted(loads[rel]):
            for k, (raw, probe) in sorted(universe[lbl].items()):
                sels.append(probe)
                keys.append((lbl, k))
        if sels:
            plan.append({"page": f"/madar/{rel}", "sels": sels})
            index.append(keys)

    host = root / "_selcov_probe.html"
    host.write_text("<!doctype html><html><head><meta charset=utf-8></head><body>"
                    + PROBE.replace("__PLAN__", json.dumps(plan))
                    + "</body></html>", encoding="utf-8")
    try:
        dump = subprocess.run(
            [browser, "--headless=new", "--no-sandbox", "--disable-gpu",
             "--hide-scrollbars", "--window-size=1280,900",
             "--virtual-time-budget=120000", "--dump-dom",
             f"http://127.0.0.1:{port}/madar/_selcov_probe.html"],
            capture_output=True, text=True, timeout=900)
    finally:
        httpd.shutdown()
        host.unlink(missing_ok=True)

    m = re.search(r'<pre id="probe">(.*?)</pre>', dump.stdout, re.S)
    if not m:
        die("the probe did not run — a silent probe reads exactly like a clean "
            "sweep (the 09-14 trap)")
    res = json.loads(H.unescape(m.group(1)))
    bad = [k for k in res if k.startswith("!")]
    if bad:
        die("the probe could not fetch %d page(s): %s" % (len(bad), bad[:3]))

    matched, errored = {}, {}
    probed = 0
    for job, keys in zip(plan, index):
        hits = res.get(job["page"])
        if hits is None:
            die("the probe returned nothing for %s" % job["page"])
        probed += 1
        for j, n in hits:
            k = keys[j]
            if n == -2:
                errored.setdefault(k, 0)
            else:
                matched[k] = matched.get(k, 0) + n

    if probed != len(plan):
        die("probed %d of %d planned pages" % (probed, len(plan)))
    if errored:
        die("%d selector(s) the browser could not evaluate: %s"
            % (len(errored), [k[1] for k in list(errored)[:3]]))

    unmatched = {}
    for lbl, got in universe.items():
        for k in got:
            if (lbl, k) not in matched:
                unmatched.setdefault(lbl, []).append(k)

    # ---------------------------------------------------------------- report
    print("qa_selector_coverage — does the stylesheet's own statement reach a page?")
    print("  pages read ................. %d" % len(loads))
    print("  stylesheets ................ %d" % len(sheet_css))
    gated_sheets = [l for l in sorted(sheet_css) if l not in NOT_ASSERTED]
    tot_g = sum(len(universe[l]) for l in gated_sheets)
    un_g = sum(len(unmatched.get(l, [])) for l in gated_sheets)
    for lbl in sorted(sheet_css):
        n, u = len(universe[lbl]), len(unmatched.get(lbl, []))
        tag = "  PRINTED, NOT ASSERTED" if lbl in NOT_ASSERTED else ""
        print("    %-34s %4d selectors, %3d unmatched  (%4.1f%%)%s"
              % (lbl[:34], n, u, 100.0 * u / n if n else 0.0, tag))
    print("  asserted population ........ %d selectors over %d sheet(s)"
          % (tot_g, len(gated_sheets)))
    print("  unmatched, asserted ........ %d  (%.1f%%)"
          % (un_g, 100.0 * un_g / tot_g if tot_g else 0.0))

    for lbl, why in sorted(NOT_ASSERTED.items()):
        if lbl in unmatched:
            print("\n  NOT ASSERTED — %s: %d unmatched selectors." % (lbl, len(unmatched[lbl])))
            print("    %s." % why)

    byclass = {}
    for lbl in gated_sheets:
        for k in unmatched.get(lbl, []):
            cls = REGISTER.get(k, ("UNREGISTERED",))[0]
            byclass.setdefault(cls, []).append(k)
    if byclass:
        print("\n  THE PARTITION (#118), over the asserted population:")
        for cls in ("CONDITIONAL", "LATENT", "ORPHANED", "SUPERSEDED", "UNREGISTERED"):
            if cls in byclass:
                print("    %-12s %3d" % (cls, len(byclass[cls])))
        for k in sorted(byclass.get("ORPHANED", [])):
            print("    ORPHANED  %s" % k)
            print("              %s" % REGISTER[k][1])

    # ---------------------------------------------------------------- limbs
    fail = []

    # LIMB 1 — nothing unmatched is unlicensed.
    rogue = sorted(k for lbl in gated_sheets for k in unmatched.get(lbl, [])
                   if k not in REGISTER)
    if rogue:
        fail.append("LIMB 1 — %d selector(s) match nothing on any page that loads "
                    "them and are not in this file's register. Either the markup "
                    "walked away from the rule (a defect: file it and fix the "
                    "markup) or the rule is new and dead (classify it in REGISTER "
                    "with its evidence). Do NOT delete an orphan without reading "
                    "#118." % len(rogue))
        for k in rogue:
            fail.append("           %s" % k)

    # LIMB 2 — the register cannot rot.
    live = set()
    for lbl in gated_sheets:
        live |= set(universe[lbl])
    stale, woke = [], []
    for k in sorted(REGISTER):
        if k not in live:
            stale.append(k)
        elif not any(k in unmatched.get(lbl, []) for lbl in gated_sheets):
            woke.append(k)
    if stale:
        fail.append("LIMB 2 — %d register entr(ies) name a selector this build no "
                    "longer ships. Strike them." % len(stale))
        for k in stale:
            fail.append("           %s" % k)
    if woke:
        fail.append("LIMB 2 — %d register entr(ies) now MATCH. The markup arrived; "
                    "strike the entry so the register keeps meaning what it says."
                    % len(woke))
        for k in woke:
            fail.append("           %s  (was %s)" % (k, REGISTER[k][0]))

    print()
    if fail:
        for line in fail:
            print("FAIL qa_selector_coverage — " + line if line.startswith("LIMB")
                  else line)
        if report_only:
            print("(--report: not failing the build)")
            return 0
        return 1

    print("CLEAN qa_selector_coverage — %d of %d asserted selectors reach a page; "
          "the %d that do not are registered, classified and evidenced."
          % (tot_g - un_g, tot_g, un_g))
    return 0


if __name__ == "__main__":
    sys.exit(main())
