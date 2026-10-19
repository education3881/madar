#!/usr/bin/env bash
# qa_artefact_render_proof.sh — prove standing assertion 33 both ways (#35).
#
# Run from the repository root:  bash agents/tools/proofs/qa_artefact_render_proof.sh
#
# Every bite runs on a /tmp copy, never on the repository, and **every bite first
# asserts that the injection changed the file** — the 2026-09-14 trap: an
# injection that fails to change the artefact reads exactly like a passing
# control, and is the more dangerous of the two failures.
set -u
REPO="$(pwd)"
TOOL="$REPO/agents/tools/qa_artefact_render.py"
LAB="$(mktemp -d)"
PASS=0; FAIL=0
BRIEF="2026-10-18-daily-brief.html"          # clean, current template
BASELINED="2026-05-31-daily-brief.html"      # in OVERFLOW_BASELINE (blockified inline)

note() { printf '\n== %s\n' "$*"; }
ok()   { PASS=$((PASS+1)); printf '   PASS  %s\n' "$*"; }
bad()  { FAIL=$((FAIL+1)); printf '   FAIL  %s\n' "$*"; }

# a fresh lab root holding only the two artefact families the tool collects
fresh() {
  rm -rf "$LAB/root"; mkdir -p "$LAB/root/agents/briefs" "$LAB/root/agents/reviews"
  cp "$REPO/agents/briefs/$BRIEF"    "$LAB/root/agents/briefs/"
  cp "$REPO/agents/briefs/$BASELINED" "$LAB/root/agents/briefs/"
  cp "$REPO/agents/reviews/2026-10-18-weekly-review.html" "$LAB/root/agents/reviews/"
}

changed() {  # changed <file> <before-sum> ; the 09-14 guard
  local now; now="$(md5sum "$1" | cut -d' ' -f1)"
  if [ "$now" = "$2" ]; then bad "INJECTION DID NOT CHANGE $1 — bite is void"; return 1; fi
  ok "injection changed $(basename "$1") ($2 -> $now)"
}

# ---------------------------------------------------------------- 1. CONTROL
note "1. CONTROL — the lab corpus, untouched, must pass"
fresh
OUT="$(python3 "$TOOL" "$LAB/root" 2>&1)"; RC=$?
echo "$OUT" | sed 's/^/      /'
[ $RC -eq 0 ] && ok "control exit 0" || bad "control exit $RC (expected 0)"
echo "$OUT" | grep -q "tail renders .......... 3 of 3" \
  && ok "all three tails render" || bad "tail count wrong"

# ------------------------------------------------- 2. BITE A — the 10-12 defect
note "2. BITE A — an HTML comment opened and never closed (the real 2026-10-12 defect)"
fresh
F="$LAB/root/agents/briefs/$BRIEF"
B="$(md5sum "$F" | cut -d' ' -f1)"
# the exact shape: the generator's CSS comment-block opener, pasted and unterminated
python3 - "$F" <<'PY'
import sys, re
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
i = s.find("</main>")
assert i > 0, "no </main> to inject before"
open(p, "w", encoding="utf-8").write(
    s[:i] + "<!-- Panel CSS (add once to the brief's\n" + s[i:])
PY
changed "$F" "$B" || true
OUT="$(python3 "$TOOL" "$LAB/root" 2>&1)"; RC=$?
echo "$OUT" | sed 's/^/      /'
[ $RC -eq 1 ] && ok "bite A exit 1" || bad "bite A exit $RC (expected 1)"
echo "$OUT" | grep -q "TAIL NOT RENDERED" \
  && ok "named the defect: TAIL NOT RENDERED" || bad "wrong diagnosis"
echo "$OUT" | grep -q "carry a closing tag" \
  && ok "reported the swallowing comment node" || bad "comment node not reported"
# the comment oracle fires first here; the text-loss oracle is isolated in 2b
# ------------------------------- 2b. BITE A2 — swallowed with NO comment node
note "2b. BITE A2 — an unclosed <script>: the SAME deletion with no comment node at all"
fresh
F="$LAB/root/agents/briefs/$BRIEF"
B="$(md5sum "$F" | cut -d' ' -f1)"
python3 - "$F" <<'PY4'
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
# injected MID-document, not at the tail: the 2026-10-12 defect swallowed the
# Tomorrow section, and an injection after the last section loses no text at all
i = s.find("<main")
i = s.index(">", i) + 1
mid = s.find("<div", (i + len(s)) // 2)
assert mid > i, "no mid-document section to inject before"
open(p, "w", encoding="utf-8").write(s[:mid] + "<script>var x = 1;\n" + s[mid:])
PY4
changed "$F" "$B" || true
OUT="$(python3 "$TOOL" "$LAB/root" 2>&1)"; RC=$?
echo "$OUT" | sed 's/^/      /'
[ $RC -eq 1 ] && ok "bite A2 exit 1" || bad "bite A2 exit $RC (expected 1)"
echo "$OUT" | grep -q "visible characters" \
  && ok "the text-loss oracle fired alone, with no comment node to help it" \
  || bad "text-loss oracle did not fire"

# --------------------------------------------- 3. BITE B — the KNOWN BLIND SPOT
note "3. BITE B — the overflow probe's blind spot, proved rather than assumed"
echo "   This is the bite that FAILED to bite, and it is why measurement B does not"
echo "   gate the build. A white-space:pre push block is injected into a clean brief;"
echo "   Chrome reports scrollWidth == clientWidth == 1028 for text far wider, so the"
echo "   probe sees nothing. Recorded here so the next run does not re-derive it."
fresh
F="$LAB/root/agents/briefs/$BRIEF"
B="$(md5sum "$F" | cut -d' ' -f1)"
python3 - "$F" <<'PY2'
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
i = s.find("</main>")
assert i > 0
open(p, "w", encoding="utf-8").write(
    s[:i] + '<p style="white-space:pre">cd "/Users/vini/Documents/Claude/Projects/'
    'Educational Website" && git add -A && git commit -m "x" && git push origin HEAD:main</p>'
    + s[i:])
PY2
changed "$F" "$B" || true
OUT="$(python3 "$TOOL" "$LAB/root" 2>&1)"; RC=$?
echo "$OUT" | sed 's/^/      /'
[ $RC -eq 0 ] && ok "exit 0 — the probe is blind to this shape, as the header states" \
             || bad "exit $RC: the blind spot has closed, so measurement B can now be ASSERTED and the header is stale"
echo "$OUT" | grep -q "MEASURED, NOT ASSERTED" \
  && ok "printed its own blind spot beside its findings" || bad "blind spot not printed"

# -------------------------------- 4. BITE C — the membership list cannot go stale
note "4. BITE C — a baselined artefact that stops overflowing must be NAMED for deletion"
fresh
F="$LAB/root/agents/briefs/$BASELINED"
B="$(md5sum "$F" | cut -d' ' -f1)"
# repair the real mechanism: stop grid from blockifying inline children of <li>
python3 - "$F" <<'PY3'
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
i = s.find("</head>")
open(p, "w", encoding="utf-8").write(
    s[:i] + "<style>li{display:block !important}</style>\n" + s[i:])
PY3
changed "$F" "$B" || true
OUT="$(python3 "$TOOL" "$LAB/root" 2>&1)"; RC=$?
echo "$OUT" | sed 's/^/      /'
echo "$OUT" | grep -q "delete from OVERFLOW_BASELINE" \
  && ok "named the stale member for deletion" || bad "stale member not named"
echo "$OUT" | grep -q "$BASELINED" \
  && ok "named which one" || bad "did not say which"

# ------------------------------------------------- 5. BITE D — a check that lies
note "5. BITE D — no browser must REFUSE (exit 2), never pass"
fresh
mkdir -p "$LAB/bin"; ln -sf "$(command -v python3)" "$LAB/bin/python3"
ln -sf "$(command -v md5sum)" "$LAB/bin/md5sum" 2>/dev/null
OUT="$(PATH="$LAB/bin" "$LAB/bin/python3" "$TOOL" "$LAB/root" 2>&1)"; RC=$?
echo "$OUT" | sed 's/^/      /'
[ $RC -eq 2 ] && ok "refused with exit 2" || bad "exit $RC (expected 2)"
echo "$OUT" | grep -q "REFUSED" && ok "said REFUSED out loud" || bad "silent skip"

# -------------------------------------------- 6. BITE E — an empty corpus lies too
note "6. BITE E — an empty corpus must REFUSE, not report 0 of 0 clean"
rm -rf "$LAB/empty"; mkdir -p "$LAB/empty/agents/briefs"
OUT="$(python3 "$TOOL" "$LAB/empty" 2>&1)"; RC=$?
echo "$OUT" | sed 's/^/      /'
[ $RC -eq 2 ] && ok "refused with exit 2" || bad "exit $RC (expected 2)"

note "RESULT  $PASS passed, $FAIL failed"
rm -rf "$LAB"
[ "$FAIL" -eq 0 ] || exit 1
