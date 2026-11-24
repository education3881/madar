#!/usr/bin/env python3
"""Proof harness for item 50's limb in qa_citation_identity — WHICH FORM did it match.

Run: python3 agents/tools/proofs/qa_citation_identity_forms_proof.py

Proves the limb both ways per #35, bite first, with THREE guards the operation has
paid for and which this harness executes rather than cites:

  * 2026-09-14 trap 1 — assert the injection CHANGED the artefact before running
    the check on it. A bite that fails to change the bytes reads exactly like a
    passing control.
  * RULING #157 / standing-queue item 156, filed 2026-11-23 — assert the
    population did not FALL. A bite ADDS a defect, so it may move a measurement
    up or leave it flat; a bite that moves it DOWN has broken the input rather
    than planted a defect, and that also reads like a passing control. One line,
    and nobody had it until yesterday.
  * 2026-09-14 trap 2 — where else does the string I am looking for legitimately
    appear? The <title> and the <h1> here are DIFFERENT strings on purpose, so a
    classifier that read the wrong one cannot accidentally be right.

Offline and deterministic: the documents are synthetic bytes, so nothing here
depends on anybody else's CMS at 09:00.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
if not (ROOT / "web").is_dir():  # a proofs/ file is two levels down; assert it
    raise SystemExit(f"not the repository root: {ROOT}")
sys.path.insert(0, str(ROOT / "agents" / "tools"))

import qa_citation_identity as Q  # noqa: E402

H1 = "AI-powered textbooks fail to make the grade in South Korea"
TITLE = "South Korea's AI textbooks fail after rushed rollout"
OG = "South Korea AI textbook rollout, one year on | Rest of World"
BODY_SENTENCE = "Everything was rushed, the teacher said, and nobody asked us first."
URL = "https://example.org/2025/south-korea-ai-textbook-rollout-failure/"

DOC = """<!doctype html><html><head>
<title>{title}</title>
<meta property="og:title" content="{og}">
<script type="application/ld+json">{{"@type":"NewsArticle","headline":"{title}"}}</script>
</head><body><h1>{h1}</h1>
<p>{body}</p>
<p>The page also prints its own tab string somewhere in the furniture: {title}</p>
</body></html>"""

failures: list[str] = []


def say(ok: bool, label: str, detail: str = "") -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {label}" + (f"   {detail}" if detail else ""))
    if not ok:
        failures.append(label)


def forms_of(raw: bytes, url: str = URL) -> dict:
    return Q.headline_forms(raw, "text/html", url)


def classify(token: str, raw: bytes, url: str = URL) -> tuple[str, list[str]]:
    return Q.classify_form(token, False, forms_of(raw, url))


# --------------------------------------------------------------- the control
print("\nCONTROL — the document leads with the string we quoted")
full = DOC.format(title=TITLE, og=OG, h1=H1, body=BODY_SENTENCE).encode()
forms = forms_of(full)
say(sorted(forms) == ["h1", "headline", "og:title", "slug", "title"],
    "all five forms are read out of the bytes", str(sorted(forms)))
form, hits = classify(H1, full)
say(form == "h1" and Q.FORM_STANDING[form] == "evidence",
    "a token in the <h1> is classified h1 / evidence", f"{form} {hits}")
form_body, _ = classify(BODY_SENTENCE, full)
say(form_body == "body",
    "a token in running text and in no form is classified body", form_body)

# ------------------------------------------------------------------ bite one
print("\nBITE 1 — the quotation is the tab's string, and the page leads with another")
form, hits = classify(TITLE, full)
say(form in ("title", "headline"), "a <title>-only token is NOT reported as h1", f"{form} {hits}")
say(Q.FORM_STANDING[form] == "warning", "and its standing is a warning", Q.FORM_STANDING[form])
say(form != "h1" and classify(H1, full)[0] == "h1",
    "the two forms are told APART on one document — which is the whole finding")

# ------------------------------------------------------------------ bite two
print("\nBITE 2 — the quotation exists only in the ADDRESS of the document")
# PADDED ON PURPOSE, and the padding is the second finding of this harness.
# The first version of this bite served a 366-byte document and compare() returned
# `script-mismatch`, not `found` — correctly: SCRIPT_FLOOR is 200 characters of a
# script before a token in that script may be asked of a document, so a document
# too short to HAVE a dominant script declines the comparison. The bite was
# testing the instrument's licence instead of the limb it was aimed at. A bite
# must clear the floors the instrument declares before it can reach the code it
# targets — 2026-09-14's trap read one layer in.
FILLER = ("This page has been archived and the article it carried is no longer "
          "available at this address. Our readers may wish to browse the current "
          "edition instead, where the newsroom publishes daily reporting from "
          "across the region and beyond. ") * 2
stripped = DOC.format(title="Rest of World", og="Rest of World", h1="Rest of World",
                      body=FILLER).encode()
say(stripped != full, "the injection changed the artefact (2026-09-14 trap 1)",
    f"{len(full)} -> {len(stripped)} bytes")
slug_token = "south korea ai textbook rollout failure"
form, hits = classify(slug_token, stripped)
say(form == "slug" and Q.FORM_STANDING[form] == "COUNTERFEIT",
    "a slug-only token is classified slug / COUNTERFEIT", f"{form} {hits}")
row = Q.compare(URL, [{"token": slug_token, "script": "latin", "convention": "straight-single"}],
                {"status": 200, "ctype": "text/html", "raw": stripped})
verdicts = row.get("tokens", [])
say(bool(verdicts) and verdicts[0]["verdict"] == "found"
    and verdicts[0].get("form") == "slug",
    "compare() reports it found-in-the-slug rather than absent",
    json.dumps(verdicts[0], ensure_ascii=False)[:120])

# ---------------------------------------------------------------- bite three
print("\nBITE 3 — the gated limb: an emit that stops recording the form")
with tempfile.TemporaryDirectory() as tmp:
    sandbox = pathlib.Path(tmp)
    (sandbox / "web" / "src" / "content").mkdir(parents=True)
    live = ROOT / Q.REGISTER
    data = json.loads(live.read_text(encoding="utf-8"))
    target = sandbox / Q.REGISTER
    target.parent.mkdir(parents=True, exist_ok=True)

    def population(path: pathlib.Path) -> int:
        """How many confirmed tokens the register asserts a form for. #157's guard
        needs a number that a broken input would move DOWN."""
        rows = json.loads(path.read_text(encoding="utf-8"))["registers"]
        return sum(1 for r in rows for v in r.get("tokens", [])
                   if v.get("verdict") == "found" and "form" in v)

    target.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    before = population(target)

    hollowed = json.loads(json.dumps(data))
    touched = 0
    for r in hollowed["registers"]:
        if str(r.get("observed", "")) < Q.FORM_EPOCH:
            continue
        for v in r.get("tokens", []):
            if v.get("verdict") == "found" and "form" in v:
                del v["form"]
                touched += 1
    target.write_text(json.dumps(hollowed, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    after = population(target)
    say(touched > 0 and after < before,
        "the injection changed the artefact and removed N forms", f"{before} -> {after}")

    # #157's guard, stated in the direction it was earned: here the measurement
    # falling IS the planted defect, so the harness asserts the fall is EXACTLY
    # the forms it deleted and that no ROW disappeared. A bite that shrank the
    # population by breaking the file would also shrink this number.
    rows_before = len(data["registers"])
    rows_after = len(hollowed["registers"])
    say(rows_before == rows_after and before - after == touched,
        "and it broke nothing else — row count flat, the fall equals the deletion (#157)",
        f"rows {rows_before}, forms -{touched}")

    def run_check(where: pathlib.Path) -> tuple[int, str]:
        out = subprocess.run([sys.executable, str(ROOT / "agents/tools/qa_citation_identity.py"),
                              str(where)], capture_output=True, text=True)
        return out.returncode, out.stdout + out.stderr

    # The sandbox has no corpus, so --check refuses before it reaches the limb.
    # The limb is therefore exercised against the REAL repository root, with the
    # real register hollowed in place and restored immediately. Nothing else in
    # the tree is touched and the restore is asserted byte-for-byte.
    original = live.read_bytes()
    try:
        live.write_text(json.dumps(hollowed, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        code_bite, out_bite = run_check(ROOT)
        say(code_bite == 1 and "no recorded form" in out_bite,
            "--check RED on a register whose confirmed tokens lost their form",
            f"exit {code_bite}")
    finally:
        live.write_bytes(original)
    say(live.read_bytes() == original, "the live register is restored byte-for-byte")
    code_ctl, out_ctl = run_check(ROOT)
    say(code_ctl == 0 and "CLEAN qa_citation_identity" in out_ctl,
        "--check GREEN on the real register as it stands", f"exit {code_ctl}")
    say("WHICH FORM DID IT MATCH" in out_ctl,
        "and the census is printed, not asserted (#93)")

print("\n" + ("PROOF CLEAN — all limbs" if not failures
             else f"PROOF FAILED — {len(failures)}: {failures}"))
sys.exit(1 if failures else 0)
