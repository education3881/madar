#!/usr/bin/env bash
# Proof harness for standing assertion 36, qa_citation_identity (2026-10-22).
#
# #35 both ways, and the bite proved as carefully as the control: every
# injection below is asserted to have CHANGED the artefact before the check is
# run on it, because a bite that fails to change the file reads exactly like a
# passing control (ruling #65 / the 09-14 trap).
#
# TWO HALVES ARE PROVED HERE, AND THE SECOND IS THE NEW PART.
#   A. The GATED half (`--check`), offline, exactly as #111's harness proves its
#      own: coverage, row shape, the chain of memory, the silent-pass trap.
#   B. The COMPARISON itself (`compare()`), which is where this tool's actual
#      judgment lives and which the network half merely feeds. It is proved
#      against SYNTHETIC served bytes rather than against somebody else's
#      server, because a harness that depended on a ministry's uptime would be
#      a harness about their uptime. Four readings, each a different verdict.
set -u
REPO="${1:-/home/runner/work/madar/madar}"
TOOL="$REPO/agents/tools/qa_citation_identity.py"
R=/tmp/ident-bite
rm -rf "$R"; mkdir -p "$R/web/src/content" "$R/agents/stats" \
                      "$R/empty/web/src/content/articles" "$R/empty/agents/stats"
cp -r "$REPO/web/src/content/articles" "$R/web/src/content/"
cp -r "$REPO/web/src/content/articles-ar" "$R/web/src/content/"
cp "$REPO/agents/stats/citation-identity.json" "$R/agents/stats/"
cp "$REPO/agents/stats/citation-identity.json" "$R/empty/agents/stats/"
J="$R/agents/stats/citation-identity.json"
REL=web/src/content/articles/2026-07-16-australia-naplan-reset.md
P="$R/$REL"

say() { printf '\n== %s\n' "$*"; }
run() { python3 -I "$TOOL" "$1" >/dev/null 2>&1; echo "$?"; }
changed() { local now; now=$(md5sum "$1" | cut -d' ' -f1)
  [ "$now" != "$2" ] && echo "   injection CHANGED the artefact ($2 -> $now)" \
                     || { echo "   INJECTION DID NOT BITE — experiment failed"; exit 9; } }

say "CONTROL — the real corpus and the real register, copied"
echo "   exit $(run "$R")   (expect 0)"

say "BITE 1 — a piece quotes a register nobody has ever read the quotation against"
B=$(md5sum "$P" | cut -d' ' -f1)
python3 - "$P" <<'PY'
import sys, pathlib
q = chr(39)  # the corpus's own identity-token convention, kept out of quote hell
tok = q + 'a sentence this operation put inside quotation marks' + q
p = pathlib.Path(sys.argv[1]); t = p.read_text()
p.write_text(t.replace('hero:\n',
    '  - title: "An injected register, bite 1, which prints ' + tok + '"\n'
    '    url: "https://example.invalid/quoted-but-never-compared"\n'
    'hero:\n', 1))
PY
changed "$P" "$B"
echo "   exit $(run "$R")   (expect 1)"
git -C "$REPO" show "HEAD:$REL" > "$P"
echo "   restored; control exit $(run "$R")   (expect 0)"

say "BITE 2 — a row that stops describing its subject (shape)"
B=$(md5sum "$J" | cut -d' ' -f1)
python3 - "$J" <<'PY'
import sys, json, pathlib
p = pathlib.Path(sys.argv[1]); d = json.loads(p.read_text())
d['registers'][3].pop('state')
p.write_text(json.dumps(d, indent=1, ensure_ascii=False))
PY
changed "$J" "$B"
echo "   exit $(run "$R")   (expect 1)"
cp "$REPO/agents/stats/citation-identity.json" "$J"
echo "   restored; control exit $(run "$R")   (expect 0)"

say "BITE 3 — the chain of memory broken: no register on disk at all"
mv "$J" "$J.bak"
echo "   exit $(run "$R")   (expect 1)"
mv "$J.bak" "$J"
echo "   restored; control exit $(run "$R")   (expect 0)"

say "BITE 4 — the silent-pass trap: an approved corpus with no quotation in it"
echo "   exit $(run "$R/empty")   (expect 1)"

say "BITE 5 — the corpus keeps its 682 citations and loses every quotation mark"
# The trap this tool is most exposed to: a style change that stops annotations
# quoting their registers would leave coverage perfect and the instrument blind.
rm -rf "$R/noquote"; mkdir -p "$R/noquote/agents/stats"
cp -r "$R/web" "$R/noquote/web"
cp "$J" "$R/noquote/agents/stats/"
B=$(cat "$R/noquote/web/src/content/articles"/*.md "$R/noquote/web/src/content/articles-ar"/*.md | md5sum | cut -d' ' -f1)
python3 - "$R/noquote" <<'PY'
import pathlib, sys, re
root = pathlib.Path(sys.argv[1])
for folder in ("articles", "articles-ar"):
    for p in (root / "web/src/content" / folder).glob("*.md"):
        t = p.read_text(encoding="utf-8")
        # all FIVE conventions, not four: the first run of this bite stripped the
        # guillemets and the single quotes, left `\"` alone, and exited 0 — a bite
        # that fails to remove every token reads exactly like a passing control.
        t = t.replace('\\"', " ")
        p.write_text(re.sub(r"[«»‘’“”']", " ", t), encoding="utf-8")
PY
NOW=$(cat "$R/noquote/web/src/content/articles"/*.md "$R/noquote/web/src/content/articles-ar"/*.md | md5sum | cut -d' ' -f1)
[ "$NOW" != "$B" ] && echo "   injection CHANGED the corpus ($B -> $NOW)" \
                   || { echo "   INJECTION DID NOT BITE — experiment failed"; exit 9; }
echo "   exit $(run "$R/noquote")   (expect 1)"

say "B. THE COMPARISON — compare() against synthetic served bytes, eleven readings"
python3 -I - "$REPO" <<'PY'
import sys, pathlib, importlib.util
spec = importlib.util.spec_from_file_location(
    "qci", pathlib.Path(sys.argv[1]) / "agents/tools/qa_citation_identity.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

EN = {"token": "declined only marginally", "script": "latin"}
AR = {"token": "التعليم الأساسي "
               "مجاني وإلزامي",
      "script": "arabic"}
# the UN interview's real clause, with the tashkeel our annotation carries
AR2 = {"token": "يُطلَق عليها اسم "
                "مكانيا باللغة "
                "العربية",
       "script": "arabic"}
PAD = "نص " * 150   # 300 Arabic characters: a document, not a UI label
LPAD = "ordinary prose " * 40   # 560 Latin characters, same purpose

def served(body, ctype="text/html; charset=utf-8", status=200):
    return {"status": status, "ctype": ctype, "raw": body.encode("utf-8")}

cases = [
  ("CONTROL — the quotation is still there, typographically mangled",
   "https://x.invalid/a", [EN],
   served("<html><body><p>" + LPAD + "The count   &ldquo;declined\n only   marginally&rdquo; "
          "in the latest annual.</p></body></html>"), "confirmed"),
  ("BITE — a 200 serving a listing page with none of the article's text",
   "https://x.invalid/?p=508411", [EN],
   served("<html><body><h1>Latest news</h1><p>" + LPAD + "</p><ul><li>Something else entirely</li>"
          "</ul></body></html>"), "absent"),
  ("LICENCE — an Arabic quotation against a document not written in that script",
   "https://x.invalid/c", [AR],
   served("<html><body><p>An English ministry page.</p></body></html>"), "script-mismatch"),
  ("LICENCE — the same Arabic quotation against a document that carries it",
   "https://x.invalid/d", [AR],
   served("<html><body><p>" + PAD + "التعليمُ "
          "الأساسيُ "
          "مجانيٌ وإلزاميٌ"
          "</p></body></html>"), "confirmed"),
  ("BOUNDARY — a PDF is not readable text and must not be called absent",
   "https://x.invalid/e.pdf", [EN],
   served("%PDF-1.4 binary-ish", "application/pdf"), "unreadable-format"),
  ("BOUNDARY — a 403 is walled, not absent (#70)",
   "https://x.invalid/f", [EN], served("", "text/html", 403), "walled"),
  ("FALSE POSITIVE 1, fixed — a language-switcher label is not an Arabic document",
   "https://x.invalid/decree", [AR],
   served("<html><body><a>العربية</a>"
          "<p>An English decree summary, " + "word " * 400 + "</p></body></html>"),
   "script-mismatch"),
  ("FALSE POSITIVE 2, fixed — a quotation mark INSIDE a quotation is punctuation",
   "https://x.invalid/un", [AR2],
   served("<html><body><p>" + PAD +
          "يطلق عليها اسم "
          "&quot;مكانيا&quot; "
          "باللغة العربية"
          "</p></body></html>"),
   "confirmed"),
  ("FALSE POSITIVE 3, fixed — U+2011 non-breaking hyphen is typography, not identity",
   "https://x.invalid/gna", [{"token": "curriculum for out-of-school children", "script": "latin"}],
   served("<html><body><p>" + LPAD + "CEA launches revised curriculum for "
          "out‑of‑school children</p></body></html>"), "confirmed"),
  ("FALSE POSITIVE 4, fixed — an English rendering of a Cyrillic programme name",
   "https://x.invalid/osvita", [{"token": "School Offline programme", "script": "latin"}],
   served("<html><body><nav>Home About Login Legislation Secondary</nav><p>"
          + "про організацію " * 40
          + "</p></body></html>"), "script-mismatch"),
  ("BOUNDARY — one token found, one gone: partial, not confirmed",
   "https://x.invalid/g", [EN, {"token": "a sentence that was removed", "script": "latin"}],
   served("<p>" + LPAD + " declined only marginally</p>"), "partial"),
]
bad = 0
for label, url, toks, got, expect in cases:
    row = m.compare(url, toks, got)
    ok = row["state"] == expect
    bad += 0 if ok else 1
    print(f"   {'ok ' if ok else 'FAIL'} {row['state']:<18} expect {expect:<18} {label}")
print("   all comparison verdicts as specified" if not bad else f"   {bad} WRONG")
sys.exit(1 if bad else 0)
PY
echo "   comparison harness exit $?   (expect 0)"

say "done"
