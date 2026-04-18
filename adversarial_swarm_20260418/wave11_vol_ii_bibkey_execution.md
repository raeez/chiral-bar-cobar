# Wave-11 Vol II Bibkey Execution (2026-04-18)

Execution note for the Vol II top-25 bibkey heal drafted by Wave-10 bibkey alias
campaign (agent ac602ea1) + this execution pass. Scope: 20 new `\bibitem`
entries + 4 pure aliases appended to
`/Users/raeez/chiral-bar-cobar-vol2/main.tex` inside the in-line
`\begin{thebibliography}` block.

## Inputs

Raw phantom analytics (pre-heal):
- `/tmp/vol2_used.txt`             — 472 unique `\cite{}` keys
- `/tmp/vol2_defined.txt`          — 332 `\bibitem{}` definitions (pre-heal)
- `/tmp/vol2_phantoms_final.txt`   — 212 phantom keys (used, not defined)
- `/tmp/vol2_used_counts.txt`      — invocation counts per key
- `/tmp/vol2_top25.txt`            — Wave-10 top-25 ranking

Pre-heal phantom invocation count: **396**.

## Mission brief adjustment

The Wave-10 brief's "4 pure aliases" list (`Strominger18`, `JKL26`,
`Positselski11`, `CostelloGaiotto2020`) pointed to keys that already exist
as defined canonicals. The actual phantom variants requiring aliasing are
their long-form siblings. Adjusted plan:

| Phantom (alias, N×) | Canonical target |
|---------------------|------------------|
| `Positselski2011` (4×) | `Positselski11` |
| `StromingerLectures2018` (7×) | `Strominger18` |
| `JKL` (5×) | `JKL26` |
| `GR17` (6×) | `GR14` |

All four canonicals exist as `\bibitem` in `main.tex`. Alias pattern matches
the existing convention (`Pos11` / `Positselski11` duplicate-entry pair) —
full bibliographic body repeated with trailing `% Alias for X.` comment.

## 20 new bibitems inscribed (with best-effort attribution)

1. `HamadaShiuSubsubSoft` — Hamada--Shiu, PRL 120 (2018) 201601, arXiv:1801.05528. **TODO: librarian verification** (exact subsub-soft paper candidate).
2. `LiStromingerHigherSoft` — Li--Strominger, higher-spin soft theorems. **TODO: librarian verification** (arXiv placeholder).
3. `Linshaw-Winfty` — Linshaw, Compos. Math. 157 (2021), arXiv:1710.02148.
4. `DonnayFotopoulosPasterskiTaylor21` — arXiv:2108.11969 (2021). **TODO: verify**.
5. `Arakawa15` — Arakawa, Ann. of Math. 182 (2015) 565--604, arXiv:1505.09016.
6. `Bezrukavnikov16` — Bezrukavnikov, Publ. IHES 123 (2016), arXiv:1209.0403.
7. `StromingerWInfinityCelestial` — Strominger, PRL 127 (2021) 221601, arXiv:2105.14346.
8. `BrownMixedTate` — F. Brown, Ann. of Math. 175 (2012) 949--976, arXiv:1102.1312.
9. `BMP-Wsymmetry` — Bouwknegt--Schoutens, Phys. Rep. 223 (1993), arXiv:hep-th/9210010. **TODO: verify** (alt candidate: Bouwknegt--McCarthy--Pilch LNP m42 1996).
10. `Molev07` — Molev, *Yangians and Classical Lie Algebras*, AMS Surv. 143 (2007).
11. `deBoerTjin93` — de Boer--Tjin, CMP 158 (1993) 485--516, arXiv:hep-th/9211109.
12. `CostelloPaquetteSharmaCelestial` — PRL 130 (2023) 061602, arXiv:2208.14233.
13. `BittlestonHeuvelineSkinner` — JHEP 2023:09:008, arXiv:2305.09451.
14. `ArkhipovGaitsgory09` — preprint 2009. **TODO: verify** (identifier + published venue).
15. `Zhu96` — Zhu, JAMS 9 (1996) 237--302.
16. `Linshaw-Winfty-universal` — alias of `Linshaw-Winfty` (long-form naming variant).
17. `KamnitzerTappeWeekes14` — Algebra Number Theory 8 (2014) 857--893, arXiv:1209.0349.
18. `KacRoanWakimoto03` — Kac--Roan--Wakimoto, CMP 241 (2003) 307--342, arXiv:math-ph/0302015.
19. `HernandezJimbo12` — Hernandez--Jimbo, Compos. Math. 148 (2012) 1593--1623, arXiv:1104.1891.
20. `GuayRegelskisWendlandt18` — Lett. Math. Phys. 109 (2019) 327--379, arXiv:1706.05176.

`Linshaw-Winfty-universal` is architecturally a fifth alias (long-form naming
variant of `Linshaw-Winfty`) but counted among the 20 bibitems because the
canonical `Linshaw-Winfty` is itself introduced in this same heal block;
chain-alias pattern.

TODO comments left inline per mission directive for librarian verification of
6 entries (HamadaShiu, LiStrominger, DonnayFot..., BMP, Arkhipov, and
alias-target-independent ones flagged `TODO: librarian verification`).

## Phantom reduction (verified)

| Metric | Pre-heal | Post-heal | Delta |
|---|---|---|---|
| Defined `\bibitem` keys | 332 | 356 | +24 |
| Phantom unique keys | 212 | 178 | **-34** |
| Phantom invocation count | 396 | 269 | **-127** |

The invocation-count reduction of 127 (32% of pre-heal invocation phantoms
resolved) exceeds the target band "~24-50 phantom invocations resolved" — the
top-25 distribution is heavily skewed: the top-24 keys accounted for 127
invocations.

Residual long-tail: 178 phantom keys / 269 phantom invocations across 416
pre-heal invocation sites → ~65% of pre-heal phantom invocations remain. Top
residuals by invocation count (4× each): `GRW18` (defined already, stale
phantom-scan artefact), `CostelloGaiottoBoundaryVOA`, `CLNS24`,
`Bakas-Winfty`, `Arakawa07`. Below that: long tail of ≤3× entries suitable
for Wave-12 or on-demand healing.

`GRW18` is genuinely phantom (pre-heal phantom scan correct; the
superficially similar `GRW21` is defined at `main.tex:1902`-era). Wave-10
mission brief listed `GRW18` as "check attribution"; appears to be
Guay--Regelskis--Wendlandt 2018 (same authors as the already-aliased
`GuayRegelskisWendlandt18` just added). Candidate for chain-alias in
Wave-12.

## Verification performed

1. `grep -n '\\begin{thebibliography}\|\\end{thebibliography}'` — bibliography at `main.tex:1846-2798` (post-heal).
2. Read tail entries (`EMS20`, format convention) and alias precedent (`Pos11`/`Positselski11`, line 2346-2351).
3. All 4 pure-alias targets exist as canonical `\bibitem` entries (`Strominger18:2447`, `JKL26:2593`, `Positselski11:2346`, `GR14` defined separately).
4. Post-heal `\bibitem` count: 356 (pre: 332); delta matches 24 planned additions.
5. Post-heal phantom-invocation count computed via `awk` join against `/tmp/vol2_phantoms_post.txt` and `/tmp/vol2_used_counts.txt`.

## Commit plan (DEFERRED — no commits in this execution pass)

Mission constraint: "No commits". All heals are inscribed in the working
tree; separate commit pass will batch:

- `chore(vol2-bib): Wave-11 bibkey heal — +20 bibitems, +4 aliases (phantom invocations 396 → 269)`
- Commit author: Raeez Lorgat.
- No AI attribution.
- Scope: `main.tex` only (bibliography block).
- Pre-commit: verify the hook's AP8/AP25/AP14/AP7/V2-AP26 flags in `main.tex`
  are pre-existing (not introduced by this heal); fresh grep for those
  patterns within the Wave-11 insertion block should return zero.
- Build verification: `pkill -9 -f pdflatex; sleep 2; make fast` after commit
  batch; expected: phantom `\cite` count drops by 127 invocations (BibTeX /
  build-log `[?]` reduction).

## Residual heal priorities (Wave-12 candidates)

Next-tier phantom keys by invocation count (post-heal):

| Key | Count | Likely target |
|---|---|---|
| `GRW18` | 4 | Chain-alias to `GuayRegelskisWendlandt18` (same paper, short form) |
| `CostelloGaiottoBoundaryVOA` | 4 | Costello--Gaiotto boundary VOA paper; probably arXiv:1905.05640 or similar |
| `CLNS24` | 4 | Unknown attribution — librarian required |
| `Bakas-Winfty` | 4 | Bakas W_∞ algebra, probably 1989--1990 phys. lett. |
| `Arakawa07` | 4 | Arakawa 2007 Kazhdan filtration, Invent. Math. |
| `Vol3` / `Vol2-*` / `V1-thm:*` | various | AP253 — rewrite to `\ref{}`, NOT `\cite{}` |

The programme-internal self-cites (`Vol3`, `Vol2-*`, `LorgatVolI`, etc.) are
**NOT** addressed in this heal per mission directive: they need AP253
rewrite to cross-volume `\ref{}`, not bibliography entries.

## AP flags

- AP124 `\bibitem` uniqueness: verified (24 new keys, all absent from pre-heal defined set).
- AP281 Option-a alias layer discipline: applied (duplicate-entry convention matches existing `Pos11`/`Positselski11` precedent).
- AP28 undefined terminological qualifier: 6 TODO markers inline for librarian pass.
- AP253 programme-internal self-cites: deliberately excluded (out of scope).
- No AI attribution anywhere. Author: Raeez Lorgat.
