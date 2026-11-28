# Edition 07 (China) — the door test, run 2026-11-28 by the daily run

**Why today.** The plan requires Edition 07's slate — nine candidates, each with two or more primary
registers already opened and read in served text — **by Thursday 3 December**, and Edition 07 opens Monday
7 December. Every Edition 06 piece but one has been written off a register that this runner could reach only
through an archive snapshot, because `www.oecd.org` answers **403**. The first question about a new
edition's subject is therefore not *what are the angles* but **which doors answer this runner**, and it is
cheap to ask. Measured, not assumed.

## What answers, measured from the cloud runner at 2026-11-28 13:4x UTC

| Door | Result | Bytes | Note |
|---|---|---|---|
| `http://www.moe.gov.cn/` | **200** | 101,977 | Ministry of Education portal, `charset=utf-8`, Chinese |
| `https://www.moe.gov.cn/` | **302 to nothing** | 0 | **the https host redirects and serves no body to this runner; the http host does.** A door called closed on the scheme we tried first |
| `http://en.moe.gov.cn/` | **200** | 21,280 | the ministry's own English edition, with *Documents · Laws and Policies · Reports* in its own navigation |
| `http://ar.moe.gov.cn/` | **200** | 21,636 | **the ministry's own ARABIC edition** |
| `https://www.gov.cn/` | **200** | 67,401 | State Council portal |
| `https://www.stats.gov.cn/` | **200** | 141,425 | National Bureau of Statistics |
| `http://www.moe.gov.cn/jyb_xwfb/` | **200** | 48,878 | the news index — a link set, which is where the Qatar and Uzbekistan method starts |
| `http://www.moe.gov.cn/srcsite/A06/` | **200** | 11,014 | a departmental document directory |
| `http://www.moe.gov.cn/sitemap.xml` | 404 | 12 | no sitemap; the link set has to be walked |
| `http://www.moe.gov.cn/robots.txt` | 404 | 12 | no robots file |
| `www.oecd.org` (re-tested in the same run) | **403** | — | unchanged, so the Edition 06 archive route still stands |

Eight language subdomains are linked from the Chinese front page: `en`, `ru` (as `Pусский`), `jp`, `de`,
`fr`, `es` and `ar`, plus internal subdomains `dxs`, `hudong`, `jsj` and `qspfw`.

## The finding that changes how this edition is written

**`ar.moe.gov.cn` is a first-party ministry register in Arabic, and it belongs to a state whose language is
neither of ours.** Ruling **#160** says the asymmetry between our two editions belongs to *the register's
language, not to the Arabic edition*: an Arabic register makes the **Arabic edition the only one in which
every quotation is a byte beside a byte** and leaves the English edition carrying translations no instrument
we own can compare. #160 has been tested on four configurations — Arabic (Jordan), Thai (Thailand), English
(Qatar), Spanish (Uruguay) — and its 2026-11-28 simplification was that *a register in any third language
makes both editions equal.* China offers something none of the four did: **the same owner publishing in
Chinese, in English and in Arabic.** One ministry, three first-party editions, so for a single claim this
publication can choose which of its own editions is the checkable one — and that is a configuration the
ruling has no entry for.

**It is a candidate, not a finding, and the next step is written down so it is not skipped.** The Arabic
front page is **3,784 characters of extracted text and almost all of it is navigation**; nothing has been
read yet that shows it carries dated policy documents rather than a standing brochure. **Before any piece
leans on it, the Arabic edition's own link set is walked and one dated document is read in served text in
both Chinese and Arabic and compared.** If the Arabic edition turns out to be a brochure, the configuration
collapses to the ordinary one and the English edition is the register.

## What this does NOT establish

- **Nothing about PISA 2025 and China.** The ministry front page carries **no occurrence of `PISA`** in
  either case, and none of 学前, 免费, 义务教育 or 双减 either — it is a portal shell, and *a register is a
  document, not a page* (the method that opened the Qatar and Uruguay pieces). The link set is the next read.
- **No candidate has a second register yet.** The plan's bar is two or more primary registers opened and
  read per candidate, over nine candidates. This file is the reachability layer under that work, not the
  slate.
- **No judgement on scope.** The plan's own instruction for Edition 07 stands unchanged: report what the
  state and its registers say, with named voices, and take no editorial posture on the political system.

## Owed next, in order

1. Walk `jyb_xwfb/` and `srcsite/` link sets for dated 2026 documents on the plan's named angles — free
   preschool, double reduction years on, rural boarding and left-behind children, AI guidance for schools,
   teacher pay, vocational routes, and whether China took part in PISA 2025.
2. Read one dated document in Chinese **and** in its Arabic and English first-party editions, and compare.
   That single read settles the #160 configuration question for the whole edition.
3. Only then write the slate at `content-drafts/recon/<date>-ed07-slate.md`, nine candidates, two registers
   each, three of them spares.
