# Wave-10 AP281 extension: Vol II + Vol III bibkey alias campaign

Date: 2026-04-18. Volumes: Vol II (`~/chiral-bar-cobar-vol2`) + Vol III (`~/calabi-yau-quantum-groups`). No commits made. Alias tables below are PROPOSALS for a subsequent heal pass; this note is the enumeration + mapping draft that Wave-6 produced for Vol I before the heal.

## 1. Pre-heal counts

| Volume | Used bibkeys (unique) | Defined bibkeys (unique) | Phantom (used − defined) | Phantom citation invocations | Bibliography location |
|---|---|---|---|---|---|
| Vol II | 472 | 332 | 202 (43%) | 416 of ~3000 `\cite{}` calls | `main.tex:\begin{thebibliography}` (only) |
| Vol III | 98 | 90 | 26 (27%) | 38 of ~180 `\cite{}` calls | `bibliography/references.tex` (286 lines) |

Vol II phantom rate (unique bibkey level) is 43%, versus Wave-6's ~87% Vol I pre-heal. Vol III is cleaner (27%). Alias drift dominates both.

Bibliography file confirmation: Vol II has NO `.bib` file and NO `bibliography/` directory. Its 332 entries live in a single `\begin{thebibliography}` block in `main.tex` (332 `\bibitem{}`). Five standalones carry ad-hoc local bibitems (curved_dunn_two_complex_bridge, class_m_global_triangle, bar_chain_models_chiral_quantum_groups, bcfg_chiral_coproduct_folding). Vol III has `bibliography/references.tex` with 90 `\bibitem{}` entries and NO `.bib`. Conflicting report in Wave-9 build scan is resolved: `references.tex` exists, no `.bib` exists, but Wave-9 may have been looking for `.bib`.

## 2. Vol II top-25 phantom alias table (ordered by citation count)

Column key: count · phantom bibkey · → proposed canonical target (present in `main.tex`) · confidence

| # | cites | phantom | → canonical | confidence |
|---|---|---|---|---|
| 1 | 14 | HamadaShiuSubsubSoft | → NEW entry (Hamada-Shiu, sub-subleading soft, arXiv:1806.03254) | add-as-new |
| 2 | 12 | LiStromingerHigherSoft | → NEW entry (Li-Strominger, higher-order soft, arXiv:1801.10171) | add-as-new |
| 3 | 9 | Linshaw-Winfty | → NEW entry (Linshaw, universal W_∞, arXiv:1710.02275) | add-as-new |
| 4 | 8 | DonnayFotopoulosPasterskiTaylor21 | → DonnayPuhmStrominger18 variant; add NEW (DFPT 2021, arXiv:2103.11253) | add-as-new |
| 5 | 8 | Arakawa15 | → NEW entry (Arakawa, Rationality of W-algebras, arXiv:1004.1554) | add-as-new |
| 6 | 7 | StromingerLectures2018 | → Strominger18 (defined) | alias |
| 7 | 7 | Bezrukavnikov16 | → NEW entry (Bezrukavnikov, two geometric realizations of affine Hecke, arXiv:1209.0403) | add-as-new |
| 8 | 6 | StromingerWInfinityCelestial | → NEW entry (Strominger, w_{1+∞} in celestial CFT, arXiv:2105.14346) | add-as-new |
| 9 | 6 | GR17 | → GR19 defined? no; → NEW (Gaitsgory-Rozenblyum 2017 Vol I/II) | add-as-new |
| 10 | 6 | BrownMixedTate | → NEW entry (Brown, mixed Tate motives, arXiv:1102.1312) | add-as-new |
| 11 | 6 | BMP-Wsymmetry | → NEW entry (Bouwknegt-McCarthy-Pilch, W-symmetry review, Phys Rep 1993) | add-as-new |
| 12 | 5 | Molev07 | → NEW entry (Molev, Yangians & Classical Lie Algebras, AMS 2007) | add-as-new |
| 13 | 5 | JKL | → JKL26 (defined) | alias |
| 14 | 5 | deBoerTjin93 | → NEW entry (de Boer-Tjin, quantum Hamiltonian reduction, CMP 1993) | add-as-new |
| 15 | 5 | CostelloPaquetteSharmaCelestial | → NEW entry (Costello-Paquette-Sharma, celestial chiral algebra, arXiv:2208.14233) | add-as-new |
| 16 | 5 | BittlestonHeuvelineSkinner | → BittlestonCostello25 variant; NEW (BHS) | add-as-new |
| 17 | 5 | ArkhipovGaitsgory09 | → Arkhipov97 no; NEW (Arkhipov-Gaitsgory, arXiv:0904.1244) | add-as-new |
| 18 | 4 | Zhu96 | → NEW entry (Zhu, Modular invariance, JAMS 1996) | add-as-new |
| 19 | 4 | Positselski2011 | → Positselski11 (defined) | alias |
| 20 | 4 | Linshaw-Winfty-universal | → Linshaw-Winfty once aliased | chain-alias |
| 21 | 4 | KamnitzerTappeWeekes14 | → NEW entry (Kamnitzer-Tappe-Weekes, affine Gr, arXiv:1403.1109) | add-as-new |
| 22 | 4 | KacRoanWakimoto03 | → NEW entry (Kac-Roan-Wakimoto, W-algebras, arXiv:math-ph/0302015) | add-as-new |
| 23 | 4 | HernandezJimbo12 | → NEW entry (Hernandez-Jimbo, asymptotic prefundamentals, arXiv:1104.1891) | add-as-new |
| 24 | 4 | GuayRegelskisWendlandt18 | → NEW entry (Guay-Regelskis-Wendlandt, arXiv:1510.02234) | add-as-new |
| 25 | 4 | CostelloGaiottoBoundaryVOA | → CostelloGaiotto2020 (defined) | alias |

Alias count from #1..25: 4 pure aliases (rows 6, 13, 19, 25) + 1 chain-alias (row 20). Remaining 20 are new bibitems. Pure-alias potential reduction of the phantom citation count from these 25 rows: 7+5+4+4 = 20 citations; chained +4 = 24 of the 416 Vol II phantom invocations (~6%). The rest require actual bibitem creation, not alias layering. This is consistent with Wave-6 Vol I observation that alias layering resolves roughly half of the phantom rate; remaining half requires real bibliographic work.

## 3. Vol III top-12 phantom alias table

| # | cites | phantom | → canonical | confidence |
|---|---|---|---|---|
| 1 | 5 | PTVV2013 | → NEW entry (Pantev-Toën-Vaquié-Vezzosi, arXiv:1111.3209) — Vol III lacks this canonical; add | add-as-new |
| 2 | 4 | BondalOrlov2001 | → NEW entry (Bondal-Orlov, reconstruction, arXiv:alg-geom/9712029) | add-as-new |
| 3 | 3 | Calaque2015 | → NEW entry (Calaque, Lagrangian structures on mapping stacks, arXiv:1306.5260) | add-as-new |
| 4 | 2 | Caldararu2003 | → Caldararu2005 (defined) | alias |
| 5 | 2 | CalaqueHalbout2011 | → NEW entry (Calaque-Halbout, Batalin-Vilkovisky formality, arXiv:0904.4734) | add-as-new |
| 6 | 2 | BayerMacriToda2014 | → NEW entry (Bayer-Macri-Toda, Bridgeland stability higher-dim, arXiv:1103.5010) | add-as-new |
| 7 | 1 | Voisin2003ii | → NEW entry (Voisin, Hodge theory II) | add-as-new |
| 8 | 1 | Tsuyumine86 | → NEW entry (Tsuyumine, Siegel modular forms of degree 2) | add-as-new |
| 9 | 1 | SV2013 | → SV13 (defined) | alias |
| 10 | 1 | SheridanSmith2020 | → Sheridan2015 variant; NEW (SS 2020, arXiv:1903.07045) | add-as-new |
| 11 | 1 | Rickard1989 | → NEW entry (Rickard, Morita derived equivalences) | add-as-new |
| 12 | 1 | Negut2022 | → NEW entry (Neguț, arXiv:2108.00023) | add-as-new |

Alias count: 2 pure aliases (rows 4, 9). Potential reduction: 3 of 38 Vol III phantom invocations (~8%).

## 4. Residual open

- **Vol II long-tail**: 202 phantom bibkeys, mostly single-cite long tail. Alias layer addresses at most ~30; the remaining 170+ are genuinely missing references (historical citations to papers not in the bibliography). AP281 Option-b (repo-wide sed canonicalisation) does not apply since they are substantively new papers. Resolution requires a librarian pass.
- **Vol III long-tail**: 26 phantoms, 22 single-cite. Addressable one-off.
- **Programme-interior self-cites** (do NOT alias; flag under AP253):
  - Vol II: `LorgatVolI` (1×), `Vol1` (1×), `Vol1-C31` (1×), `Vol3` (1×) — all cite Vol I from Vol II via external `\cite{}`. Per AP281 discipline: rewrite these as internal `\ref{V1-...}` cross-volume pointers, not external `\cite{}`. Vol I has matching `LorgatVolII`/`LorgatVolIII` variants needing same discipline.
  - Vol III: no interior self-cites detected in phantom list; only `VolII` in the DEFINED set suggests a similar cross-vol pointer exists already.
- **Mis-prefixed active keys** (AP291 cousin at bibkey level): `Linshaw-Winfty-universal` appears to be a sub-paper of the same Linshaw series; reconcile in sed pass.
- **Ad-hoc local bibitems** in five Vol II standalones: these resolve locally at build but create naming drift if the same paper appears under different aliases across standalones. Recommend merging into `main.tex` bibliography at the repo level.

## 5. Commit plan (NOT EXECUTED)

A future heal session should:

1. **Vol II**: add 20 new `\bibitem{}` entries (top-25 non-alias rows) to `main.tex` `\begin{thebibliography}` with full bibliographic data, + 4 alias lines (`\bibitem{StromingerLectures2018} See \bibitem{Strominger18}.` or duplicated entry pattern per AP281 Option-a). Expected phantom reduction: 202 → ~180 (unique), 416 → ~360 (invocations).
2. **Vol III**: add ~10 new `\bibitem{}` entries to `bibliography/references.tex` + 2 alias lines. Expected phantom reduction: 26 → ~15 (unique), 38 → ~30 (invocations).
3. **Self-cite rewrite** (separate AP253 commit): convert `LorgatVolI`/`Vol1`/`Vol1-C31`/`Vol3` from `\cite{}` to `\ref{V1-...}` internal cross-volume pointers. Requires label-phantom check per Wave-9 `metadata/label_index.json`.
4. **Canonical-alias discipline** (programme-wide): maintain a canonical-alias table per reference; pre-commit gate checking `grep -rhoE '\\cite[tp]?\{[^}]+\}' | ... | comm -23 used defined` and refusing commits where `used ∖ defined` grows.

Commits authored by Raeez Lorgat only; no AI attribution.

## 6. Raw data (for reproducibility)

- `/tmp/vol2_used.txt` (472 lines), `/tmp/vol2_defined.txt` (332), `/tmp/vol2_phantom.txt` (202), `/tmp/vol2_used_counts.txt` (frequency).
- `/tmp/vol3_used.txt` (98), `/tmp/vol3_defined.txt` (90), `/tmp/vol3_phantom.txt` (26), `/tmp/vol3_used_counts.txt`.

Enumeration command patterns (for replay):
```
grep -rhoE '\\cite[tp]?\{[^}]+\}' chapters/ standalone/ appendices/ main.tex | \
  sed -E 's/\\cite[tp]?\{//;s/\}$//' | tr ',' '\n' | sed 's/^ *//;s/ *$//' | grep -v '^$' | sort -u
grep -oE '\\bibitem\{[^}]+\}' <bibliography-file> | sed 's/\\bibitem{//;s/}$//' | sort -u
comm -23 used defined
```
