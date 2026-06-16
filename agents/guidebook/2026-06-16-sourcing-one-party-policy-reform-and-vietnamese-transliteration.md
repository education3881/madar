# Method — sourcing a one-party / parliamentary policy reform, and a Vietnamese→Arabic transliteration table

**Banked:** 2026-06-16 (Vietnam tuition-free ship) · **Owners:** Researcher (sourcing rule) + Arabic Editor (transliteration table)
**Why it exists:** Vietnam was our first piece on a one-party state and our first with Vietnamese named humans. Two reusable assets came out of it — keep them so the next Vietnam/China/Laos candidate starts ahead.

---

## 1. The dual-instrument rule (sourcing discipline)

In a one-party-plus-legislature system, a major reform usually arrives as **two distinct instruments**, and the headline ("school is free now") collapses them. The accurate account keeps them apart:

- **A Party / executive DECISION** sets direction. *(Vietnam: the Politburo decision of **28 Feb 2025**.)*
- **A legislature's RESOLUTION / LAW** binds the budget. *(Vietnam: National Assembly **Resolution 217/2025/QH15**, adopted **26 Jun 2025**, 440/441.)*

**The rule:** name **both** instruments with their **own dates**; never write the Party decision and the legislative act as one event. A Party decision is not yet a budget line; the resolution is.

**Sub-rule — adoption ≠ signing/certification.** Outlets cite different dates for the *same* act: the **adoption/vote** date vs. the **signing/certification** date (Vietnam: adopted 26 Jun; certified by NA Chairman Trần Thanh Mẫn shortly after). Flag both if the piece needs a date; **conflate neither**; attribute the certification to the named official.

This is the policy-instrument twin of the guidebook's *"a program name is not a citation"* rule (Section 3 #4): a reform's **headline is not its legal instrument** — pin every claim to the specific instrument + date that carries it. Generalises to any system where a Party/executive act and a legislative act are separate (China, Laos, Vietnam, and — in a different key — any decree-vs-statute system).

**Companion fence used on this piece (carry it):** *tuition-free ≠ fee-free.* When a reform "removes a cost," establish what that cost **legally is** (here: *học phí*, a small capped monthly fee) and what it is **not** (insurance, service fees, the "voluntary" fund, meals, extra classes). The story is usually the gap, and it must be sourced to the country's **own** press (Tuoi Tre's fee breakdown; the word *lạm thu*), never to outside commentary alone — that is what keeps the dignity check clean.

---

## 2. Vietnamese → Arabic transliteration table (Arabic-Editor rulings, 2026-06-16)

Northern (Hanoi) pronunciation; **tones are dropped** in Arabic (Arabic carries no tone — keep the Latin original in the source index and gloss once in-body). Choices optimise **reader recognition** over strict phonetics where the two conflict.

| Vietnamese | Arabic | Note |
|---|---|---|
| Nguyễn | نغوين | the established Arabic form; use it for every Nguyễn |
| Thị | ثي | `Th` → `ث` |
| Vân | فان | |
| Hồng | هونغ | `-ông` → `-ونغ` |
| Kim Sơn | كيم سون | (Minister Nguyễn Kim Sơn) |
| Trần | تران | |
| Thanh | ثانه | final `-nh` → `-نه` |
| Mẫn | مان | (NA Chairman Trần Thanh Mẫn) |
| Chương | تشونغ | `Ch` → `تش`; `-ương` → `-ونغ` |
| Dương | دونغ | Northern `D` = /z/, but rendered `د` for recognition (matches common Arabic use of *dong/đồng*); fix the choice and repeat it |
| Hoàn Kiếm | هوان كيم | Hanoi district |
| Hà Nội | هانوي | |
| Hải Phòng | هاي فونغ | (banked for the backup-voice city) |
| Đinh Văn Tân | دينه فان تان | (banked; the parked backup voice) |
| *Tiền Phong* (paper) | تيين فونغ | |
| *Tuổi Trẻ* (paper) | توي تري | |
| Mỹ Dung (reporter) | مي دونغ | |

**Transferable sub-rules:** `Ph→ف`, `Th→ث`, `Ch→تش`, final `-nh→-نه`, `-ương/-ông → -ونغ`; pick one rendering per name and keep it identical on every mention; keep Vietnamese concept-words (*học phí, học thêm, lạm thu*) in Latin with an adjacent Arabic gloss, because the reader gains from seeing the original.

---

## 3. Also banked this run — a QA ruling (frontmatter-key parity)

The EN draft shipped its first build **missing its entire `hero:` block**; it built clean and rendered a slug-fallback still but silently lost its `og:image`, `alt`, and caption — a parity gap the body-text diff would never show. **Ruling:** at the publish gate, diff the EN and AR frontmatter for **key parity** (`hero/src/alt/caption`, `related`, `arabicVersion`/`englishVersion`), not just body and figures. A missing key builds clean and ships broken; only a key-level diff catches it.

## Cross-refs
- Section 1 source index: `2026-06-14-vietnam-tuition-free-source-index.md` (now shipped).
- [[edu_website_publish_gate]] — add the frontmatter-key-parity line to the gate checklist.
- Builds on Section 3 #4 (*a program name is not a citation*) — same discipline, policy-instrument dimension.
