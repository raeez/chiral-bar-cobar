# Wave-13 Vol II bibkey next-tier heal — execution report

**Date**: 2026-04-18
**Agent**: execution (next-tier after Wave-11 a0b6041d top-20).
**Scope**: 10-15 new `\bibitem` entries + alias layer for residual Vol II phantom invocations ≥ 3×.
**Constraint acknowledged**: no commits; no AI attribution anywhere; all commits authored by Raeez Lorgat only (AP5 + AP281 discipline).

## Metric summary (pre vs post-heal)

| metric                        | pre-Wave-13 | post-Wave-13 | delta |
|-------------------------------|-------------|--------------|-------|
| used unique cite-keys (Vol II)| 532         | 532          |   0   |
| defined `\bibitem` keys       | 356         | 375          | +19   |
| **phantom unique keys**       | **176**     | **158**      | **−18** |
| **phantom invocations**       | **267**     | **208**      | **−59** |

Target was 269 → ~230–240 (−29 to −39). **Achieved −59** (208), exceeding target. Principal gain: Wave-13 resolved the entire ≥4× band (GRW18, CostelloGaiottoBoundaryVOA, CLNS24, Bakas-Winfty, Arakawa07) and the full ≥3× non-self-cite band. Residual distribution: 109 single-cite + 48 two-cite + 1 three-cite (`Vol3`, programme-interior AP281-flagged self-cite — excluded per mission instructions). **Zero 4+× phantoms remain.**

## New `\bibitem` entries appended to `main.tex:2888--2950` (Wave-13 block)

14 canonical primary bibitems + 4 aliases registered. Each entry includes venue, volume, arXiv ID where verifiable; unverified arXiv identifiers flagged `% TODO: librarian verification`.

### Primary entries (9 canonical + 5 alias)

| key                             | invocations | attribution                                                                 | alias-of   |
|---------------------------------|-------------|-----------------------------------------------------------------------------|------------|
| `GRW18`                         | 4           | Guay–Regelskis–Wendlandt 2019, Lett.\ Math.\ Phys.\ 109, arXiv:1706.05176   | GuayRegelskisWendlandt18 |
| `Arakawa07`                     | 4           | Arakawa, Invent.\ Math.\ 169 (2007), arXiv:math/0506056                     | Ara07 (long-form) |
| `CostelloGaiottoBoundaryVOA`    | 4           | Costello–Gaiotto, JHEP 2019(5):18, arXiv:1804.06460                          | —          |
| `CLNS24`                        | 4           | Creutzig–Linshaw–Nakatsuka–Sato, arXiv:2404.02410                           | —          |
| `Bakas-Winfty`                  | 4           | Bakas, Commun.\ Math.\ Phys.\ 134 (1990), 487--508                          | —          |
| `SchiffmannVasserot13`          | 3           | Schiffmann–Vasserot, Publ.\ IHES 118 (2013), arXiv:1202.2756                | —          |
| `ProchazkaRapcak18`             | 3           | Pro\v{c}h\'azka–Rap\v{c}\'ak, JHEP 2018(11):109, arXiv:1711.06888           | —          |
| `Positselski18`                 | 3           | Positselski, M\'em.\ SMF 159 (2018), arXiv:1202.2697                         | —          |
| `PasterskiShaoStromingerFlatSpaceHolog` | 3   | Pasterski–Shao–Strominger, Phys.\ Rev.\ D 96:065026, arXiv:1701.00049        | —          |
| `KRW03`                         | 3           | Kac–Roan–Wakimoto, CMP 241 (2003), arXiv:math-ph/0302015                     | KacRoanWakimoto03 |
| `Kohno1987`                     | 3           | Kohno, Ann.\ Inst.\ Fourier 37 (1987), 139--160                              | Kohno87 (long-form) |
| `KhoroshkinTolstoy96`           | 3           | Khoroshkin–Tolstoy, Lett.\ Math.\ Phys.\ 36 (1996), arXiv:hep-th/9406194     | —          |
| `Gannon16`                      | 3           | Gannon, Adv.\ Math.\ 301 (2016), arXiv:1211.5531                             | —          |
| `GaiottoRapcak2017`             | 3           | Gaiotto–Rap\v{c}\'ak, JHEP 2019(1):160, arXiv:1703.00982                     | gaiotto-rapchak (canonical-form alias) |
| `FrenkelHernandez15`            | 3           | Frenkel–Hernandez, Duke Math.\ J.\ 164 (2015), arXiv:1308.3444               | —          |
| `FF90`                          | 3           | Feigin–Frenkel, Kyoto 1991 Adv.\ Ser.\ Math.\ Phys.\ 16 (companion to FF92) | FF92 (date-shift alias, `% TODO`) |
| `CachazoStrominger14`           | 3           | Cachazo–Strominger, arXiv:1404.4091                                          | —          |
| `AP95`                          | 3           | Andersen–Paradowski, CMP 169 (1995), 563--588                                | —          |

**Aliases (same bibentry registered under second key for naming-drift coverage)**: `GRW18 → GuayRegelskisWendlandt18`, `KRW03 → KacRoanWakimoto03`, `Kohno1987 → Kohno87`, `GaiottoRapcak2017 → gaiotto-rapchak`. The `Arakawa07` entry was inscribed as a distinct bibitem because the Wave-5 invocations reference the 2007 Invent.\ Math.\ paper rather than the Ara07 canonical entry (which in Wave-11 already points to the same paper; two-line alias layer per AP281 Option-a).

### TODO-flagged entries (librarian verification recommended)

1. `CLNS24` — final arXiv identifier / publication venue unconfirmed. Attributed to Creutzig–Linshaw–Nakatsuka–Sato based on thqg_bv_ht_extensions.tex:982-983 context (hook-type corridor Koszulness, Fehily companion).
2. `FF90` — exact preprint date of the Feigin–Frenkel screening construction at critical level; canonical venue cited as Adv.\ Ser.\ Math.\ Phys.\ 16 (Kyoto 1991), but the `FF90` date-shift in manuscript prose may indicate a 1990 preprint that later appeared in the 1992 proceedings.

## Verification

- `grep` gate (`\bibitem{<key>}` present in main.tex post-heal) returns 1 for each of the 14 new entries + 4 alias entries.
- Phantom invocation count reduction 267 → 208 confirmed by `awk` join on `/tmp/vol2_used_keys.txt` (post-Wave-13 used keys ranked) against `/tmp/vol2_phantom_post.txt` (post-Wave-13 phantom unique keys).
- Residual 4+× phantoms: **zero**. The next-tier threshold is fully exhausted for the ≥3× band.
- Self-cite `Vol3` (3 invocations) intentionally excluded — it is a programme-interior self-citation (Vol III cross-volume reference) that AP281 discipline requires rewriting as `\ref{...}`-form internal cross-ref rather than `\cite{...}`-form external, and should not be bibitem-healed.

## AP hygiene

- **AP124** (label/bibkey uniqueness): verified — each new key appears exactly once as `\bibitem{...}` in main.tex. The `Arakawa07` entry shares a paper with canonical `Ara07` but uses a distinct key; this is an alias-layer pattern per AP281 Option-a and not a duplicate.
- **AP281** (bibkey naming-drift at scale): 4 alias-layer entries added to short-form ↔ long-form variants. Remaining 158 unique phantom keys in the long tail; 109 of these are single-cite, meaning the next-tier campaign's marginal return per bibitem drops sharply below 2 invocations/entry.
- **AP5** (cross-volume propagation): Vol II-only heal; no Vol I or Vol III entries touched. Consumer prose (chapters/*/\*.tex) untouched; only `main.tex` bibliography appended.
- **AP29** (prose hygiene): no AI slop introduced; comments are mathematical (attribution / TODO markers only).

## Commit plan (NOT executed per mission constraints)

- Path: `/Users/raeez/chiral-bar-cobar-vol2/main.tex` (sole file edited).
- Suggested commit message: `Vol II bibkey Wave-13 next-tier heal: 14 bibitems + 4 aliases (phantom invocations 267 → 208, −59)`.
- Author: Raeez Lorgat (sole author; no LLM attribution).
- Suggested pre-commit sanity: `make fast` in `~/chiral-bar-cobar-vol2` to verify bibliography compiles and no `[?]` renders for the 18 resolved keys; if any resolve `[?]` at build time, `\bibitem` key-case mismatch requires second-pass grep.

## Next-wave frontier

After Wave-13 the Vol II bibkey campaign residual is:
- **Long tail**: 109 unique single-invocation phantoms = 109 invocations (50% of residual).
- **2× band**: 48 unique × 2 = 96 invocations (46% of residual).
- **3× band**: 1 unique × 3 = 3 invocations (`Vol3`, AP281 self-cite, not a bibkey heal candidate).

The next-tier invocation-budget-optimal heal is the 2× band (96 invocations, 48 bibitems). Thereafter the campaign shifts from alias-adds-to-bibliography to **consumer-prose canonicalisation** (rewrite phantom `\cite{foo}` invocations to already-defined canonical aliases via `sed` pass), which closes the long tail at ~1 phantom-invocation-per-edit cost. Estimated residual-zero milestone: one more 48-entry bibitem wave + one ~100-site consumer-prose canonicalisation sweep.

## Files modified

- `/Users/raeez/chiral-bar-cobar-vol2/main.tex` (+64 lines in bibliography, lines 2888–2951 inclusive of Wave-13 banner).

## Files written

- `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/wave13_vol_ii_bibkey_nexttier.md` (this note).
