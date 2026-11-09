# Ruling #137 — a self-citation is the one register this operation falsifies by itself

**Filed:** 2026-11-09, at the point of filing, by the content and quality functions jointly.
**Family:** non-numeric (*whether the words around the number are true*) — nineteenth member.
**Found by:** `qa_citation_identity --emit`, on the first self-citation in this corpus, at the publish
gate of the first piece shipped in 43 days.

---

## The ruling

**WHEN THE CITED REGISTER IS OUR OWN PAGE, EVERY CITATION DISCIPLINE THIS OPERATION OWNS INVERTS: WE ARE
THE PARTY THAT CHANGES THE BYTES, AND BOTH LANGUAGE EDITIONS ARE OURS, SO THE ONE REGISTER A COMPOSER IS
CERTAIN THEY ALREADY KNOW IS THE ONE THEY MAY NOT RECALL.**

Binding:

1. **A citation of a Madār page carries no byte length and no digest.** It carries the read date, the HTTP code and — where a quotation is taken — the verified text. We edit that page; a number describing its size is a claim we falsify by our own ordinary work, with no register changing on either side.
2. **A Madār page's TITLE is read off that page, in that page's own language, exactly like any other register's.** The sibling edition's title is not evidence for it. The two editions are *composed*, not translated, which is precisely why neither is a rendering of the other.
3. **This repository is the archive of record for a self-citation**, and `qa_claim_registers` already says so (`ours-git-archived`). No external snapshot is owed and none is implied.

## How it was found

`2026-10-23-bahrain-bqa-five-cycles` is a follow-up that answers its predecessor's own closing question,
so it cites `2026-05-26-bahrain-bqa-public-grades` in both editions. **Measured before ruling on it:
`grep` for `education3881` across all 88 published bodies returns zero.** In 44 pairs and 168 days this
publication had never once cited itself. The class acquired its first two members this morning, and
acquired two defects with them.

### Finding 1 — the Arabic title was composed from the English

`qa_citation_identity` reported the Arabic annotation's quoted title as **absent** from the page it
names, while the English token on the English page came back **confirmed**. Checked by hand against the
served bytes:

| | |
|---|---|
| what our annotation said | «البحرين تُصدِر درجاتِ مدارسِها، بالاسم، في العَلَن» |
| what the page is titled | «البحرين تُقَيِّم مدارسها، بالاسم، على الملأ» |
| the English title | *Bahrain grades its schools, by name, in public* |

Read the three together and the mechanism is visible without asking anyone. *تُصدِر* is **issues**;
*تُقَيِّم* is **grades**. *في العَلَن* is **in public**; *على الملأ* is the published page's own idiom.
**Our Arabic annotation is a careful, idiomatic Arabic rendering of the ENGLISH title** — composed at
the desk, from the sibling edition, by a composer who knew exactly what the piece was called and
therefore had no reason to open it.

This is **#101 turned on ourselves.** #101 found that Arabic cannot carry a Latin acronym, so the
Arabic composer was *forced* back to the register while the English composer had the token and took it
— and ruled that **the forced rendering is the control.** A self-citation has **no forced side**: both
titles exist, both are ours, and both are *recallable*. The forcing mechanism that has protected this
publication for 44 pairs is absent exactly where confidence is highest. **#86 asked which questions only
one edition can answer; #101, which questions one edition is FORCED to answer; #117, which questions one
edition is forced to answer wrongly. This adds: which questions NEITHER edition is forced to answer —
and those are the ones about ourselves.**

And note what did not catch it. The composition's own hand-off line says every register was read and the
English draft never was, and that line is **true of all five registers except this one**, because this
one did not feel like a register. `qa_pair_frontmatter` passed (parity is a floor, #86). The quotation
from the same page was **exact** — 296 code points, verbatim, verified twice. *The composer opened that
page to take the quotation and did not read the title at the top of it.*

### Finding 2 — the byte length was already false when it was written

The same annotation recorded the page at **45,656 bytes, read 2026-11-07**. Re-read this morning:
**46,033 bytes.** Nothing happened to the register. Commit `ffa3e0d` — this operation's own content
function, 2026-11-07 — rewrote part of that page the same day.

The piece already carries this lesson from the other side. Its English annotation 1 says the CSV's own
byte length moved *"outside every field this piece reads — so the stability claimed here is of the
COUNTS and not of the bytes"* (#112, turned on our own annotation). **Applied to a Madār page the result
is stronger, because the moving party is us**: a byte length in a self-citation is not a fact that might
age, it is a fact we have undertaken to break.

**Population:** 26 byte-length figures are published in annotations across the corpus, and **every one
of them is about somebody else's document.** This was the first about ours, and it was false inside 48
hours.

## Why it is one ruling and not two

Both findings are the same structural fact wearing two units. A citation is a promise that **someone
else's** document says what we say it says, and every instrument this operation owns is built on that
asymmetry: `qa_sources_alive` asks whether their host answers, `qa_claim_registers` asks whether an
archive kept their page, `qa_citation_identity` asks whether their bytes still carry our quotation,
#112 names the failure mode *a citation that dies softly at 200*. **Turn the citation inward and the
asymmetry disappears.** Their host becomes our build; their archive becomes our git history; their
drift becomes our editing; and their unfamiliar prose, which forces a read, becomes our own sentence,
which invites a recall. One cause, two symptoms, one rule.

## Disposition, executed 2026-11-09 before the flag moved

- Arabic annotation 5 now carries the **served** title.
- The byte length is **struck** from both editions' self-citations; what replaces it is the claim the number was there to support — *re-read 2026-11-09 at HTTP 200, the quotation identical in both readings.*
- Both editions now state in their own text **why** no byte length is given, so the restraint is legible to a reader rather than being an absence they cannot interpret.

## What this does NOT say

It does not say a self-citation is weak. `qa_claim_registers` classes both our pages
`ours-git-archived`, and that is the strongest archival state any register in this corpus holds: the
document's full history is in this repository and is re-derivable by a stranger with `git`. **The
register is the best we cite. The citation of it was the worst.**

## Forward

The corpus now has two self-citations and will acquire more — a follow-up is a shape this publication
likes, and the standing ledger's singles make follow-ups cheaper, not dearer. **No instrument asserts
clause 1 or clause 2.** `qa_citation_identity` caught today's title defect only because the title
happened to be a quoted identity token, and it cannot see a byte length at all; nothing distinguishes a
`education3881.github.io` URL in a `sources[]` entry from any other host. Raised to the standing queue
rather than built by the run that earned the ruling.

---

*A register you can recall is the only register you will not read.*
