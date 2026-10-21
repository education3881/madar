#!/usr/bin/env bash
# Proof harness for standing assertion 35, qa_claim_registers (2026-10-21).
#
# #35 both ways, and the bite proved as carefully as the control: every
# injection below is asserted to have CHANGED the artefact before the check is
# run on it, because a bite that fails to change the file reads exactly like a
# passing control (ruling #65 / the 09-14 trap).
#
# Only the OFFLINE half (`--check`) is proved here. The `--emit` half asks
# archive.org about every register this publication cites; it gates nothing, it
# is rate-limited by design on the far side, and a harness that depended on it
# would be a harness about somebody else's uptime.
set -u
REPO="${1:-/home/runner/work/madar/madar}"
TOOL="$REPO/agents/tools/qa_claim_registers.py"
R=/tmp/claim-bite
rm -rf "$R"; mkdir -p "$R/web/src/content" "$R/agents/stats" "$R/empty/web/src/content/articles" "$R/empty/agents/stats"
cp -r "$REPO/web/src/content/articles" "$R/web/src/content/"
cp -r "$REPO/web/src/content/articles-ar" "$R/web/src/content/"
cp "$REPO/agents/stats/claim-registers.json" "$R/agents/stats/"
cp "$REPO/agents/stats/claim-registers.json" "$R/empty/agents/stats/"
J="$R/agents/stats/claim-registers.json"
P="$R/web/src/content/articles/2026-07-16-australia-naplan-reset.md"

say() { printf '\n== %s\n' "$*"; }
run() { python3 -I "$TOOL" "$1" >/dev/null 2>&1; echo "$?"; }
changed() { # changed <file> <md5-before>
  local now; now=$(md5sum "$1" | cut -d' ' -f1)
  [ "$now" != "$2" ] && echo "   injection CHANGED the artefact ($2 -> $now)" \
                     || { echo "   INJECTION DID NOT BITE — experiment failed"; exit 9; }
}

say "CONTROL — the real corpus, copied"
echo "   exit $(run "$R")   (expect 0)"

say "BITE 1 — a cited register nobody has ever asked an archive about"
B=$(md5sum "$P" | cut -d' ' -f1)
python3 - "$P" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1]); t = p.read_text()
p.write_text(t.replace('hero:\n',
    '  - title: "An injected register, bite 1"\n'
    '    url: "https://example.invalid/never-asked-about"\n'
    'hero:\n', 1))
PY
changed "$P" "$B"
echo "   exit $(run "$R")   (expect 1)"
git -C "$REPO" show HEAD:web/src/content/articles/2026-07-16-australia-naplan-reset.md > "$P"
echo "   restored; control exit $(run "$R")   (expect 0)"

say "BITE 2 — a register row that stops describing its subject"
B=$(md5sum "$J" | cut -d' ' -f1)
python3 - "$J" <<'PY'
import sys, json, pathlib
p = pathlib.Path(sys.argv[1]); d = json.loads(p.read_text())
d['registers'][5].pop('state')
p.write_text(json.dumps(d, indent=1, ensure_ascii=False))
PY
changed "$J" "$B"
echo "   exit $(run "$R")   (expect 1)"
cp "$REPO/agents/stats/claim-registers.json" "$J"
echo "   restored; control exit $(run "$R")   (expect 0)"

say "BITE 3 — the chain of memory broken: no register on disk at all"
mv "$J" "$J.bak"
echo "   exit $(run "$R")   (expect 1)"
mv "$J.bak" "$J"
echo "   restored; control exit $(run "$R")   (expect 0)"

say "BITE 4 — the silent-pass trap: a corpus with no approved content"
echo "   exit $(run "$R/empty")   (expect 1)"

say "done"
