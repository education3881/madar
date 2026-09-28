#!/usr/bin/env python3
"""
qa_feed_direction.py — standing assertion 26: a feed field CARRIES ITS OWN
DIRECTION, measured from the rendering and not from our markup.

THE QUESTION, AND THE 40 DAYS IT WAITED
---------------------------------------
Named as the next surface on 2026-08-18, restated in the RUNBOOK on 08-23, and
carried unanswered into six weekly reviews:

    Both feeds are well-formed and serve 38 items each, and nothing has ever
    verified that an item renders legibly in an actual reader, that Arabic items
    carry their direction, or that the links resolve from outside our origin.

`qa_feed_enclosures` closed the third limb and `qa_feed_validators` the
well-formedness. This closes the direction limb.

WHY OUR MARKUP IS THE WRONG WITNESS (#55's LAYER QUESTION)
----------------------------------------------------------
`web/src/lib/feed.ts` already contains direction work, added 2026-08-23, and its
own comment states the mechanism as a fact:

    `<title>` is PLAIN TEXT by spec. ... The only available lever is to prefix
    the value with U+200F, which sets the paragraph base direction to RTL.

It does not. U+200F RLM is a strong *directional character*. It satisfies the
**first-strong heuristic** — which is what `dir="auto"` and an otherwise
undetermined paragraph consult — and it has no effect whatsoever on a paragraph
whose base direction is already determined, which is precisely the reader case
that comment describes. Measured in headless Chrome on 2026-09-28, inside a host
document explicitly `dir="ltr"`, the same Arabic string with and without the RLM
prefix laid out **identically, to the pixel**. The lever that changes the
embedding level is an *isolate* — U+2067 RLI … U+2069 PDI — and it was never
tried.

So an assertion that read the RLM out of our own XML would have reported the
feed correct. The claim was in our source for 36 days and read like a verified
one. **A metadata lever is verified at the layer that consumes it.**

THE ORACLE: INVARIANCE UNDER THE HOST'S BASE DIRECTION
------------------------------------------------------
A reader drops our field into *its* document, whose base direction is the
subscriber's UI language and is never ours. So the property we actually want is
not "is this field RTL" — it is:

    **does this field render the same way regardless of the base direction of
    the document it lands in?**

That is measurable without reading a single attribute. Render each field twice,
once inside `dir="ltr"` and once inside `dir="rtl"`, both with no site CSS at
all — the reader's chrome, not ours — and compare the *visual order* of the
field's own characters. A field that carries its own direction renders the same
character order in both. A field that does not, inherits, and the two orders
differ.

Visual order is taken from `Range.getBoundingClientRect()` per character and
reduced to a **signature**: one symbol per adjacent pair, `-` if the next
character sits to the left of its predecessor, `+` if to the right, `0` within
half a pixel. Comparing signatures rather than absolute positions makes the
oracle immune to where the browser happened to place the line, and ties resolve
identically on both sides instead of flipping.

This is the same shape as assertion 18 (`qa_arabic_joining`), one surface over:
compare the artefact against **itself** under a known transformation, so the
control is a construction rather than a defect we must arrange to exist.

WHAT IT CORRECTLY DOES NOT FLAG
-------------------------------
A field that is one unbroken Arabic run with no punctuation, digits or Latin at
its edges lays out right-to-left in an LTR host too — the bidi algorithm handles
the run itself, and only the *paragraph-level* placement of neutrals and of
opposite-direction runs depends on the base direction. Its signature is
invariant, and this check passes it. That is the right answer, not a miss: such
a field needs no direction metadata. The defect appears exactly where the base
direction is load-bearing, which is why the check measures rather than audits.

BOTH LANGUAGES, BECAUSE A CHECK SCOPED TO ARABIC CANNOT SEE THE ENGLISH HALF
----------------------------------------------------------------------------
The bet that paid for this named the *Arabic* direction. Written that way it
would have enumerated one feed and passed the other in silence — the 08-16
lesson exactly. An English dek ending in a full stop, read in an Arabic-language
reader, puts that full stop on the wrong side by the identical mechanism. Both
feeds are measured; each is asserted against invariance, never against a
direction, so neither feed's expected answer is hard-coded here.

USAGE
    qa_feed_direction.py <dist-dir>

EXIT 0 clean · 1 defects found · 2 cannot run (no feed, no browser, no fields)
A check that could not run has FAILED, not passed (RUNBOOK 2026-09-13).
"""

from __future__ import annotations

import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata

# Bidi controls and formatting characters are the instruments under test, so they
# are never themselves measured — only their effect on the characters around them.
CONTROLS = set("‎‏؜") | {chr(c) for c in range(0x202A, 0x202F)} | {
    chr(c) for c in range(0x2066, 0x206A)
}

# Fewer fields than this and the check has found nothing to measure, which is a
# failure and not a pass (the silent-pass trap, 2026-08-16).
MIN_FIELDS = 20

FEEDS = [("en", "rss.xml"), ("ar", "ar/rss.xml")]


def measurable(ch: str) -> bool:
    """A character whose rendered position means something.

    Combining marks (Arabic tashkeel is category Mn) carry no advance of their
    own and sit on their base, so their rects tie with it; format characters
    have no rect at all. Both would put ties into the signature that resolve on
    the browser's whim rather than on the bidi algorithm's.
    """
    if ch.isspace() or ch in CONTROLS:
        return False
    return unicodedata.category(ch) not in ("Mn", "Cf", "Me", "Cc")


def fields_of(feed_text: str, lang: str) -> list[dict]:
    """Every field a reader renders, in the form the reader receives it.

    `title` and `category` are plain text by RSS 2.0 and are handed to the
    renderer as text. `description` is HTML by universal convention — which is
    why it is the one field that can carry a `dir` attribute at all — and is
    handed over as markup. The split is the spec's, and `lib/feed.ts` is written
    to it; this reads the served document rather than trusting that.
    """
    out: list[dict] = []
    channel = feed_text.split("<item>", 1)[0]

    def grab(block: str, tag: str) -> str | None:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", block, re.S)
        return html.unescape(m.group(1)) if m else None

    for tag, kind in (("title", "text"), ("description", "html")):
        v = grab(channel, tag)
        if v:
            out.append({"feed": lang, "where": f"channel/{tag}", "kind": kind, "value": v})

    for n, item in enumerate(re.findall(r"<item>(.*?)</item>", feed_text, re.S), 1):
        link = grab(item, "link") or f"item {n}"
        slug = link.rstrip("/").rsplit("/", 1)[-1]
        for tag, kind in (("title", "text"), ("description", "html"), ("category", "text")):
            v = grab(item, tag)
            if v:
                out.append({"feed": lang, "where": f"{slug}/{tag}", "kind": kind, "value": v})
    return out


PROBE = """<!DOCTYPE html>
<html lang="en" dir="ltr"><head><meta charset="utf-8"><style>
/* Deliberately NO site CSS. A subscriber's reader does not have ours, and the
   whole point of this probe is the chrome we do not own. `pre` and a very wide
   box keep every field on one line, so a visual-order comparison is unambiguous
   rather than a question about where the browser chose to wrap. */
.host { width: 60000px; white-space: pre; font-family: serif; font-size: 20px; }
</style></head><body>
<div id="ltr" dir="ltr"></div><div id="rtl" dir="rtl"></div>
<script>
var FIELDS = %(fields)s;
var CONTROLS = %(controls)s;

function signature(el) {
  // One symbol per adjacent measurable pair: where did the NEXT character land
  // relative to this one? That is the bidi algorithm's output, read off the
  // layout rather than inferred from an attribute.
  var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
  var lefts = [], chars = [], node;
  while ((node = walker.nextNode())) {
    var v = node.nodeValue;
    for (var i = 0; i < v.length; i++) {
      var ch = v[i];
      if (CONTROLS.indexOf(ch) !== -1) continue;
      var r = document.createRange();
      r.setStart(node, i); r.setEnd(node, i + 1);
      var b = r.getBoundingClientRect();
      if (b.width <= 0) continue;          // no advance of its own
      lefts.push(b.left); chars.push(ch);
    }
  }
  var sig = '';
  for (var k = 0; k + 1 < lefts.length; k++) {
    var d = lefts[k + 1] - lefts[k];
    sig += (d > 0.5) ? '+' : (d < -0.5) ? '-' : '0';
  }
  return { sig: sig, chars: chars.join(''), n: lefts.length };
}

var out = [];
for (var f = 0; f < FIELDS.length; f++) {
  var spec = FIELDS[f], m = {};
  for (var h = 0; h < 2; h++) {
    var hostId = h ? 'rtl' : 'ltr';
    var d = document.createElement('div');
    d.className = 'host';
    if (spec.kind === 'html') { d.innerHTML = spec.value; } else { d.textContent = spec.value; }
    document.getElementById(hostId).appendChild(d);
    m[hostId] = signature(d);
  }
  out.push({ i: f, ltr: m.ltr, rtl: m.rtl });
}
document.title = 'QADIR:' + JSON.stringify(out);
</script></body></html>
"""


def run_probe(browser: str, fields: list[dict]) -> list | dict:
    page = PROBE % {
        "fields": json.dumps([{"kind": f["kind"], "value": f["value"]} for f in fields]),
        "controls": json.dumps("".join(sorted(CONTROLS))),
    }
    tmp = tempfile.mkdtemp(prefix="qa_feeddir_")
    probe_path = os.path.join(tmp, "probe.html")
    with open(probe_path, "w", encoding="utf-8") as fh:
        fh.write(page)
    profile = tempfile.mkdtemp(prefix="qa_feeddir_profile_")
    try:
        res = subprocess.run(
            [browser, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
             "--window-size=1200,1400", f"--user-data-dir={profile}",
             "--virtual-time-budget=20000", "--dump-dom", f"file://{probe_path}"],
            capture_output=True, text=True, timeout=300,
        )
        m = re.search(r"QADIR:(\[.*?\])</title>", res.stdout, re.S)
        if not m:
            return {"error": "the browser returned no measurement"}
        return json.loads(m.group(1))
    except subprocess.TimeoutExpired:
        return {"error": "the browser did not return within 300s"}
    finally:
        shutil.rmtree(profile, ignore_errors=True)
        shutil.rmtree(tmp, ignore_errors=True)


def describe(field: dict, ltr: dict, rtl: dict) -> str:
    """Name the defect in reader terms, at the first character that moves."""
    a, b = ltr["sig"], rtl["sig"]
    chars = ltr["chars"]
    at = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
    ch = chars[at + 1] if at + 1 < len(chars) else chars[-1] if chars else "?"
    name = unicodedata.name(ch, "U+%04X" % ord(ch)) if ch else "?"
    side_ltr = "left" if a[at:at + 1] == "-" else "right"
    side_rtl = "left" if b[at:at + 1] == "-" else "right"
    return (f"{field['feed']} · {field['where']} ({field['kind']}) — inherits the reader's base "
            f"direction. First character to move: {ch!r} ({name}), which falls to the "
            f"{side_ltr} of its predecessor in an LTR reader and to the {side_rtl} in an RTL one.")


def main() -> int:
    dist = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "")
    if not dist.is_dir():
        print("usage: qa_feed_direction.py <dist-dir>")
        return 2
    browser = next((b for b in ("google-chrome", "chromium", "chromium-browser",
                                "google-chrome-stable") if shutil.which(b)), None)
    if not browser:
        print("qa_feed_direction: no headless chrome on PATH — cannot check, which is a failure")
        return 2

    print(f"qa_feed_direction: {dist.resolve()}")

    fields: list[dict] = []
    counts: dict[str, dict[str, int]] = {}
    for lang, rel in FEEDS:
        path = dist / rel
        if not path.exists():
            print(f"qa_feed_direction: {rel} is not in dist — cannot check, which is a failure")
            return 2
        text = path.read_text(encoding="utf-8")
        got = fields_of(text, lang)
        fields += got
        counts[lang] = {
            "items": len(re.findall(r"<item>", text)),
            "fields": len(got),
        }

    print("qa_feed_direction: " + " · ".join(
        f"{lang} {counts[lang]['items']} item(s) · {counts[lang]['fields']} field(s)"
        for lang, _ in FEEDS))

    if len(fields) < MIN_FIELDS:
        print(f"qa_feed_direction: only {len(fields)} field(s) to measure, floor is {MIN_FIELDS} "
              "— a check with nothing to measure has failed, not passed")
        return 2

    rep = run_probe(browser, fields)
    if isinstance(rep, dict):
        print(f"qa_feed_direction: {rep['error']} — cannot check, which is a failure")
        return 2
    if len(rep) != len(fields):
        print(f"qa_feed_direction: measured {len(rep)} of {len(fields)} field(s) "
              "— cannot check, which is a failure")
        return 2

    defects, measured, chars = [], 0, 0
    for r in rep:
        f = fields[r["i"]]
        ltr, rtl = r["ltr"], r["rtl"]
        if ltr["n"] == 0 or rtl["n"] == 0:
            defects.append(f"{f['feed']} · {f['where']} — no measurable character rendered")
            continue
        if ltr["n"] != rtl["n"]:
            defects.append(f"{f['feed']} · {f['where']} — {ltr['n']} character(s) rendered in an "
                           f"LTR reader against {rtl['n']} in an RTL one")
            continue
        measured += 1
        chars += ltr["n"]
        if ltr["sig"] != rtl["sig"]:
            defects.append(describe(f, ltr, rtl))

    print(f"  {measured} field(s) rendered twice, {chars} character positions measured, "
          "in a host document carrying no CSS of ours")

    if defects:
        print(f"\nFAIL qa_feed_direction — {len(defects)} field(s) do not carry their own "
              "direction:\n")
        for d in defects:
            print(f"  - {d}")
        print("\nA field whose visual order depends on the reader's base direction is a promise "
              "\nmade to a machine we do not own and not kept. Plain-text fields take an isolate "
              "\n(U+2066/U+2067 … U+2069); description fields take a dir attribute on their own "
              "\nwrapper. An RLM is not an isolate: it answers the first-strong heuristic and "
              "\nnothing else (ruling filed 2026-09-28).")
        return 1

    print("CLEAN qa_feed_direction — every field renders in the same visual order in an LTR reader "
          "and an RTL one, so each carries its own direction rather than inheriting one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
