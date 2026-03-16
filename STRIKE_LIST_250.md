# Strike List: 250 Items Toward the Platonic Ideal

Generated 2026-03-15. Each item is specific enough to execute in a single action.
Items are grouped by category. Priority: CRITICAL > HIGH > MEDIUM > FRONTIER.

**How to use this file**: Pick any item. Read the referenced file at the given line.
Execute the fix. Build (`make fast`). Commit. Mark done below with `[x]`.

**Vol I** = ~/chiral-bar-cobar
**Vol II** = ~/chiral-bar-cobar-vol2

---

## A. BUILD HEALTH (10 items) — CRITICAL

- [ ] **A1.** Vol I: remove duplicate label `conj:agt-w-algebra` from `chapters/connections/holomorphic_topological.tex:19` (primary is in `w_algebras_framework.tex:1934`)
- [ ] **A2.** Vol I: remove duplicate label `conj:holographic-bar-cobar` from `chapters/connections/bv_brst.tex:1016` (primary is in `genus_complete.tex:558`)
- [ ] **A3.** Vol I: fix undefined ref `def:cyclic-l-infinity-deformation` in `chapters/theory/deformation_theory.tex:4063` — likely should be `def:cyclic-deformation-elementary` (line 728) or `def:cyclic-deformation-bar` (line 1061)
- [ ] **A4.** Vol II: deduplicate 10 multiply-defined labels in `chapters/connections/ym_synthesis.tex` — content at lines 280/543 is duplicated. Keep one, delete or rename the other.
- [ ] **A5.** Vol II: rename `\label{sec:foundations}` in `chapters/connections/log_ht_monodromy.tex:103` to `\label{sec:log-ht-foundations}` (conflicts with `chapters/theory/foundations.tex:2`)
- [ ] **A6.** Vol II: add `\providecommand` to main.tex preamble for: `\Defmod`, `\Coder`, `\Bmod`, `\orline`, `\StGraph` (used in `modular_pva_quantization.tex`)
- [ ] **A7.** Vol II: fix `\text{\rm -mod}` → `\mathrm{-mod}` in `chapters/connections/anomaly_completed_topological_holography.tex:1099,1101`
- [ ] **A8.** Vol II: map 38 undefined citation keys to their correct Vol II equivalents. Pattern: short keys (`AF`, `BD`, `CDG`) → full keys (`AF15`, `BD04`, `CDG20`). Files affected: `log_ht_monodromy.tex`, `holomorphic_topological.tex`, `ht_bulk_boundary_line.tex`, `w-algebras.tex`, `bv_ht_physics.tex`, `celestial_boundary_transfer.tex`, `hochschild.tex`, `axioms.tex`, `foundations.tex`, `bar-cobar-review.tex`, `line-operators.tex`, `brace.tex`
- [ ] **A9.** Vol I: fix 3 critical overfull boxes in `chapters/frame/heisenberg_frame.tex` — line 710 (77pt), line 754 (299pt!), line 1216 (189pt). Reformat long inline math to display or add `\allowbreak`.
- [ ] **A10.** Vol II: fix 2 critical overfull boxes — line 63 (175pt), line 99 (90pt). Locate source and reformat.

## B. MISSING CLAIM STATUS (10 items) — HIGH

- [ ] **B1.** Vol I `chapters/connections/bv_brst.tex`: add ClaimStatus to 30+ theorem-class environments. Key lines: 148, 183, 220, 267, 312, 377, 502, 535, 569, 615, 631, 728, 740, 823. Use ProvedHere for algebraic theorems, ProvedElsewhere for cited results, Heuristic for physics dictionary.
- [ ] **B2.** Vol II `chapters/connections/anomaly_completed_topological_holography.tex`: add ClaimStatus to 35 environments. Lines: 152, 190, 228, 241, 265, 428, 476, 533, 583, 638, 661, 796, 844, 866, 899, 997, 1032, 1086, 1124, 1136, 1158, 1267, 1279, 1344, 1387, 1410, 1437, 1470, 1503, 1550, 1560, 1573+
- [ ] **B3.** Vol II `chapters/theory/bv-construction.tex`: add ClaimStatus to 10 environments
- [ ] **B4.** Vol II `chapters/examples/examples-computing.tex`: add ClaimStatus to 9 environments
- [ ] **B5.** Vol II `chapters/theory/pva-descent.tex`: add ClaimStatus to 11 environments
- [ ] **B6.** Vol II `chapters/theory/axioms.tex`: add ClaimStatus to 6 environments
- [ ] **B7.** Vol II `chapters/connections/bar-cobar-review.tex`: add ClaimStatus to 5 environments (lines 52, 110, 170, 209, 315)
- [ ] **B8.** Vol II `chapters/connections/spectral-braiding.tex`: add ClaimStatus to 5 environments
- [ ] **B9.** Vol II `chapters/connections/brace.tex`: add ClaimStatus to 4 environments (lines 51, 69, 90, 153)
- [ ] **B10.** Vol II `chapters/connections/celestial_holography.tex`: add ClaimStatus to 3 environments (lines 143, 191, 256)

## C. STRUCTURAL INTEGRITY (10 items) — HIGH

- [ ] **C1.** Vol I: add `\chapter{Ordered Associative Chiral Koszul Duality}` before `\label{chap:ordered-associative-kd}` in `appendices/ordered_associative_chiral_kd.tex:1`
- [ ] **C2.** Vol I: add `\chapter{Chiral Koszul Duality and Casimir Transgression}` before `\label{chap:chiral-koszul-casimir-transgression}` in `appendices/chiral_koszul_casimir_transgression.tex:1`
- [ ] **C3.** Vol I: add chapter header to `appendices/modular_dg_shifted_yangian.tex` (starts with `\providecommand` block)
- [ ] **C4.** Vol II: verify `affine_half_space_bv.tex` compiles correctly as `\chapter` under memoir with `\input` (not `\include`)
- [ ] **C5.** Vol I: verify stub chapters (`holomorphic_topological.tex`, `physical_origins.tex`) don't produce blank pages in the PDF
- [ ] **C6.** Vol II Part II: consider moving `ht_bulk_boundary_line.tex` and `celestial_boundary_transfer.tex` to Part V (Holographic) — they're about the bulk/boundary/line triangle, not PVA descent
- [ ] **C7.** Vol I concordance §three-rings: verify `\ref{app:nonlinear-modular-shadows}`, `\ref{app:branch-line-reductions}`, `\ref{app:subregular-hook-frontier}` all resolve
- [ ] **C8.** Vol I: verify `semistrict_modular_higher_spin_w3.tex` in `chapters/connections/` appears in the right Part
- [ ] **C9.** Vol II: verify `celestial_boundary_transfer.tex` uses `\providecommand` (not `\newcommand`)
- [ ] **C10.** Vol I: verify `fm3_planted_forest_residue.tex` `\chapter` header renders in appendix environment

## D. FOUR-OBJECT DISTINCTION SWEEP (10 items) — HIGH

- [ ] **D1.** Vol I `chapters/examples/free_fields.tex:2325`: verify "three dualities" passage uses "Koszul duality" not "bar-cobar Koszul duality"
- [ ] **D2.** Vol I `appendices/existence_criteria.tex`: verify "Koszul dual?" / "Bar-cobar inversion?" labels intact
- [ ] **D3.** Vol I `chapters/examples/genus_expansions.tex`: verify sl_2 Theorem A uses "bar construction and Verdier duality" not "bar-cobar adjunction"
- [ ] **D4.** Vol I `chapters/examples/kac_moody_framework.tex:153`: verify "For Koszul duality" not "For bar-cobar duality"
- [ ] **D5.** Vol I `chapters/theory/bar_cobar_construction.tex:2858`: verify "bar-cobar inversion" not "bar-cobar duality"
- [ ] **D6.** Vol I `chapters/connections/bv_brst.tex:94`: verify title "QME as Maurer-Cartan equation"
- [ ] **D7.** Vol I `chapters/theory/chiral_modules.tex:2368`: verify remark title "...and the bar complex"
- [ ] **D8.** Vol I `chapters/examples/yangians.tex:6087`: verify "module Koszul duality functor"
- [ ] **D9.** Vol II `chapters/connections/bar-cobar-review.tex`: verify genus tower section distinguishes curved R-factorization correctly
- [ ] **D10.** Vol I Convention 112 (`chapters/theory/bar_cobar_construction.tex:112`): verify four-object table and convolution Lie algebra intact

## E. CROSS-VOLUME COHERENCE (10 items) — MEDIUM

- [ ] **E1.** Vol I: verify `thm:bar-swiss-cheese` in `chapters/theory/en_koszul_duality.tex` compiles and cross-refs resolve
- [ ] **E2.** Vol II abstract: verify it references Vol I's bar complex and Swiss-cheese identification
- [ ] **E3.** Vol I concordance "Bridges to Volume II": update 5 bridge conjectures to reference Vol II's Parts IV/V
- [ ] **E4.** Vol II Part I intro: verify "bar complex presents Swiss-cheese" and Convention 112 ref
- [ ] **E5.** Vol II Part IV intro: verify `\ref*{rem:fake-complementarity}` from Vol I
- [ ] **E6.** Vol II Part V intro: verify transgression algebra B_Theta and secondary anomaly u=eta^2
- [ ] **E7.** Vol I `deformation_theory.tex`: verify `thm:ambient-complementarity` has 5 parts and genus shadow (v) cross-refs Theorem C
- [ ] **E8.** Vol II `bar-cobar-review.tex` genus tower: verify `prop:curved-R-factorization` cross-refs Vol I theorems
- [ ] **E9.** Vol I `heisenberg_frame.tex` Theorem A summary: verify convolution Lie algebra and Convention 112 cross-ref
- [ ] **E10.** Vol II bibliography: verify 27 entries from Vol I are present without duplicates

## F. MATHEMATICAL CONTENT VERIFICATION (15 items) — HIGH

- [ ] **F1.** Vol I: verify `prop:formal-legendre` tagged `\ClaimStatusConjectured`
- [ ] **F2.** Vol I: verify ambient complementarity theorem conditional on "cyclic deformation complexes exist as filtered cyclic L∞-algebras"
- [ ] **F3.** Vol I `nonlinear_modular_shadows.tex`: verify quartic shadow computed for all 5 frame families
- [ ] **F4.** Vol I `branch_line_reductions.tex`: verify genus-3 constant 7 is theorem with proof
- [ ] **F5.** Vol I `typeA_baxter_rees_theta.tex`: verify weightwise MC4 distinguished from unweighted
- [ ] **F6.** Vol I `ordered_associative_chiral_kd.tex`: verify "new results" appendix tagged ProvedHere
- [ ] **F7.** Vol I `subregular_hook_frontier.tex`: verify Bershadsky-Polyakov is first non-principal example
- [ ] **F8.** Vol I `shifted_rtt_duality_orthogonal_coideals.tex`: verify three-layer separation is theorem
- [ ] **F9.** Vol I `celestial_bf_frontier_synthesis.tex`: verify first Jacobi equation stated precisely
- [ ] **F10.** Vol I `categorical_logarithm_frontier.tex`: verify four theorems connected to four logarithm properties
- [ ] **F11.** Vol II `modular_pva_quantization.tex`: verify W_3 H^1-sector has exact dimensions
- [ ] **F12.** Vol II `affine_half_space_bv.tex`: verify one-loop exactness qualified under H1-H4
- [ ] **F13.** Vol II `log_ht_monodromy.tex`: verify HT associator conditional on quasi-linear class
- [ ] **F14.** Vol II `anomaly_completed_topological_holography.tex`: verify genus-Clifford dichotomy stated precisely
- [ ] **F15.** Vol II `ht_bulk_boundary_line.tex`: verify corrected triangle A_bulk ≃ Z_der ≃ HH(A^!) is theorem with hypotheses

## G. TYPOGRAPHIC AND FORMATTING (10 items) — MEDIUM

- [ ] **G1.** Vol I: verify garamondthm/garamonddef use `4pt plus 1pt minus 1pt` (not `\topsep`)
- [ ] **G2.** Vol II: update theorem spacing to match Vol I's tightened `4pt plus 1pt minus 1pt`
- [ ] **G3.** Vol I: verify proposition title "Universal twisting morphisms" is short enough (was overfull)
- [ ] **G4.** Vol I: verify Virasoro example title "Virasoro Koszul dual" is intact
- [ ] **G5.** Vol I: run 2-pass build, report definitive overfull count
- [ ] **G6.** Vol II: run 2-pass build, report definitive overfull count
- [ ] **G7.** Vol I: verify `\setlength{\abovedisplayskip}{8pt plus 2pt minus 4pt}` in main.tex
- [ ] **G8.** Vol II: add matching display math spacing to main.tex
- [ ] **G9.** Vol I: `grep -rn '^\\newcommand' chapters/ appendices/ --include='*.tex'` — fix any hits to `\providecommand`
- [ ] **G10.** Vol II: same `\newcommand` check in chapter files

## H. BIBLIOGRAPHY AND CITATIONS (10 items) — MEDIUM

- [ ] **H1.** Vol I: verify FeiginSemikhatov, FehilyHook, GenraStages, ButsonNair in `references.tex`
- [ ] **H2.** Vol I: verify HZ24, ZhangTheta24 in `references.tex`
- [ ] **H3.** Vol I: verify GZ26 in `references.tex`
- [ ] **H4.** Vol I: `grep 'Citation.*undefined' main.log` on fresh build — fix any remaining
- [ ] **H5.** Vol II: fix all 38 undefined citation keys
- [ ] **H6.** Vol II: verify `\bibitem{CF00}` present
- [ ] **H7.** Vol I: `grep '\\bibitem{' bibliography/references.tex | sort | uniq -d` — fix duplicates
- [ ] **H8.** Vol II: same duplicate check on inline bibliography
- [ ] **H9.** Vol I: verify `\cite{Voronov99}` in Swiss-cheese section (not `\cite{Vor99}`)
- [ ] **H10.** Vol II: verify all moved chapters use Vol II's citation keys

## I. COMPUTE/TEST INTEGRITY (5 items) — HIGH

- [ ] **I1.** Run `make test` — verify 0 failures
- [ ] **I2.** Run `python3 scripts/generate_metadata.py` — verify census
- [ ] **I3.** Verify `metadata/census.json` has `Open: 0`
- [ ] **I4.** Verify sl_2 bar H^2=5 test in fast suite
- [ ] **I5.** Verify d_bracket^2 != 0 test in fast suite

## J. FRONTIER RESEARCH (10 items) — FRONTIER

- [ ] **J1.** Compute cubic term of S_A for Heisenberg (first genuine-vs-fake discriminant)
- [ ] **J2.** Compute cubic term of S_A for sl_2-hat (first non-abelian cubic shadow)
- [ ] **J3.** Verify quartic resonance class R^mod_{4,g,n} for W_3 against semistrict W_3 chapter
- [ ] **J4.** Prove/disprove: Bershadsky-Polyakov W_3^(2) strictly Koszul at any admissible level
- [ ] **J5.** Extend weightwise MC4 to non-principal case
- [ ] **J6.** Compute complementarity potential S_A for free fermion (should match Heisenberg by Lie-Com duality)
- [ ] **J7.** Prove filtered trace-detecting uniqueness unconditionally
- [ ] **J8.** Verify shifted RTT boundary quotient for sl_2 produces quantized Kleinian surface
- [ ] **J9.** Extend FM_3 planted-forest L∞ model to FM_4
- [ ] **J10.** Write test verifying universal genus-3 constant 7

## K. PROOF FORTIFICATION (15 items) — MEDIUM

- [ ] **K1.** Vol I `higher_genus.tex:~9137`: decompose 242-line proof into 3-4 named lemmas
- [ ] **K2.** Vol I `bar_cobar_construction.tex:~2338`: extract "coderivation Leibniz" as standalone lemma
- [ ] **K3.** Vol I `chiral_koszul_pairs.tex`: verify Theorem A proof A₀/A₁/A₂ steps have forward refs
- [ ] **K4.** Vol I `deformation_theory.tex`: convert "cyclic minimal-model transfer" into lemma
- [ ] **K5.** Vol I `higher_genus.tex`: verify Theorem B coderived part (b) clearly marked conditional
- [ ] **K6.** Vol I `poincare_duality.tex`: verify intrinsic A^! definition (Construction 248) complete
- [ ] **K7.** Vol I `en_koszul_duality.tex`: Swiss-cheese proof — strengthen "collision residues commute with interval splitting" with sign computation
- [ ] **K8.** Vol I `bar_cobar_construction.tex`: BV functor — verify Berger-Fresse citation correct theorem number
- [ ] **K9.** Vol I `nonlinear_modular_shadows.tex`: verify every clutching identity has explicit proof
- [ ] **K10.** Vol I `branch_line_reductions.tex`: verify genus-2 transparency proof is self-contained (no Ring 3 dependency)
- [ ] **K11.** Vol I `typeA_baxter_rees_theta.tex`: verify Schur-envelope formula proof complete
- [ ] **K12.** Vol I `ordered_associative_chiral_kd.tex`: verify Calabi-Yau transport is proved consequence
- [ ] **K13.** Vol I `casimir_divisor_core_transport.tex`: verify "single Casimir separates spectrum" for all simple types
- [ ] **K14.** Vol II `affine_half_space_bv.tex`: verify one-loop exactness cites Gwilliam-Williams
- [ ] **K15.** Vol II `anomaly_completed_topological_holography.tex`: verify Morita-triviality has complete proof

## L. CROSS-REFERENCE DENSITY (10 items) — MEDIUM

- [ ] **L1.** Vol I `categorical_logarithm_frontier.tex`: add \ref to the four theorems it characterizes
- [ ] **L2.** Vol I `nonlinear_modular_shadows.tex`: add backward ref to ambient complementarity in deformation_theory.tex
- [ ] **L3.** Vol I `lifted_spectral_defect_calculus.tex`: add ref to `branch_line_reductions.tex`
- [ ] **L4.** Vol I `celestial_bf_frontier_synthesis.tex`: add ref to Vol II's anomaly_completed chapter
- [ ] **L5.** Vol I concordance §three-rings: systematize all appendix refs as \ref (not text)
- [ ] **L6.** Vol I `subregular_hook_frontier.tex`: add ref to `w_algebras_framework.tex` and `w_algebras_deep.tex`
- [ ] **L7.** Vol I `shifted_rtt_duality_orthogonal_coideals.tex`: add ref to yangians DK ladder and typeA weightwise MC4
- [ ] **L8.** Vol II Part IV intro: add \ref* to `rem:fake-complementarity` and `def:complementarity-potential`
- [ ] **L9.** Vol II Part V intro: add \ref* to `thm:ambient-complementarity` and `conv:bar-coalgebra-identity`
- [ ] **L10.** Vol I `dg_shifted_factorization_bridge.tex`: add ref to `modular_dg_shifted_yangian.tex`

## M. INDEX COMPLETION (10 items) — MEDIUM

- [ ] **M1.** Vol I `en_koszul_duality.tex`: add `\index{Swiss-cheese operad}` beyond the definition
- [ ] **M2.** Vol I `deformation_theory.tex`: add `\index{complementarity potential}`
- [ ] **M3.** Vol I concordance: verify `\index{three concentric rings}` renders
- [ ] **M4.** Vol I `categorical_logarithm_frontier.tex`: add `\index{categorical logarithm|textbf}`
- [ ] **M5.** Vol I `fm3_planted_forest_residue.tex`: add `\index{planted-forest $L_\infty$-algebra}`
- [ ] **M6.** Vol I `casimir_divisor_core_transport.tex`: add `\index{Casimir recurrence module}`
- [ ] **M7.** Vol I `typeA_baxter_rees_theta.tex`: add `\index{weightwise stabilization}`
- [ ] **M8.** Vol I `shifted_rtt_duality_orthogonal_coideals.tex`: add `\index{orthogonal coideal}`
- [ ] **M9.** Vol I `nonlinear_modular_shadows.tex`: add `\index{quartic resonance class}`
- [ ] **M10.** Vol I `branch_line_reductions.tex`: add `\index{branch-line reduction}`

## N. NOTATION CONSISTENCY (10 items) — MEDIUM

- [ ] **N1.** Vol I: standardize `\mathfrak{g}` vs `\fg` globally
- [ ] **N2.** Vol I: standardize `\bar{B}` vs `\barB` globally
- [ ] **N3.** Vol I: use `\Conf` macro everywhere (not inline `C_n(X)`)
- [ ] **N4.** Vol I: use `\ChirHoch` everywhere (not inline `CH^*`)
- [ ] **N5.** Vol II: use `\Ainf` everywhere (not inline `A_\infty`)
- [ ] **N6.** Vol I: verify `\kappa` for modular characteristic throughout
- [ ] **N7.** Vol I: verify `\omega_g` for Arakelov form throughout
- [ ] **N8.** Vol I: verify `\dzero`, `\dfib`, `\Dg{g}` used consistently in frontier appendices
- [ ] **N9.** Vol II: use `\SCchtop` everywhere (not inline `\mathsf{SC}^{\mathrm{ch,top}}`)
- [ ] **N10.** Vol I: verify only `\ClaimStatusProvedHere` (no variants) for proved-here claims

## O. COMPUTATIONAL VERIFICATION (10 items) — FRONTIER

- [ ] **O1.** Write test: quartic shadow vanishes for Heisenberg
- [ ] **O2.** Write test: cubic shadow proportional to Casimir for sl_2-hat
- [ ] **O3.** Write test: genus-2 transparency quotient trivial for rank-two
- [ ] **O4.** Write test: Feigin-Semikhatov Bell-recursive OPE for W_3^(2)
- [ ] **O5.** Write test: spectral discriminant Δ_A for Virasoro
- [ ] **O6.** Write test: common two-sheet sl_2-hat / Virasoro
- [ ] **O7.** Write test: weightwise bar tower stabilization Y(sl_2) weights 0-4
- [ ] **O8.** Write test: planted-forest cubic bracket on FM_3 non-zero for sl_2
- [ ] **O9.** Write test: seed propagation formula matches additive spectral kernel
- [ ] **O10.** Write test: orthogonal coideal at Kleinian point for sl_2

## P. EXPOSITION UPGRADES (15 items) — MEDIUM

- [ ] **P1.** Vol I introduction: add paragraph on Swiss-cheese and R-direction factorization
- [ ] **P2.** Vol I introduction: add three-ring summary subsection
- [ ] **P3.** Vol I `heisenberg_frame.tex`: add remark connecting to Swiss-cheese
- [ ] **P4.** Vol I concordance: update census numbers (~1,700 claims, ~1,960 pages)
- [ ] **P5.** Vol I concordance: update DK ladder for shifted RTT boundary quotient
- [ ] **P6.** Vol I concordance: update MC4 for weightwise stabilization
- [ ] **P7.** Vol I concordance: add entry for modular dg-shifted Yangian
- [ ] **P8.** Vol II abstract: update page/chapter counts
- [ ] **P9.** Vol II conclusion: expand to reference Parts IV/V
- [ ] **P10.** Vol II concordance: expand from 147 lines to proper constitution
- [ ] **P11.** Vol I `examples_summary.tex`: add Bershadsky-Polyakov row
- [ ] **P12.** Vol I `w_algebras_framework.tex`: forward ref to subregular hook appendix
- [ ] **P13.** Vol I `yangians.tex`: forward ref to typeA_baxter_rees_theta
- [ ] **P14.** Vol I `yangians.tex`: forward ref to shifted_rtt_duality
- [ ] **P15.** Vol I `yangians.tex`: forward ref to dg_shifted_factorization_bridge

## Q. VOL II CHAPTER QUALITY (15 items) — HIGH

- [ ] **Q1.** Vol II `ym_synthesis.tex`: deduplicate content at lines 280/543
- [ ] **Q2.** Vol II `modular_pva_quantization.tex`: add `\providecommand` for 5 undefined macros
- [ ] **Q3.** Vol II `log_ht_monodromy.tex`: rename `\label{sec:foundations}` to avoid conflict
- [ ] **Q4.** Vol II `anomaly_completed_topological_holography.tex`: fix `\rm` → `\mathrm`
- [ ] **Q5.** Vol II `ht_bulk_boundary_line.tex`: verify no `\newcommand` remains
- [ ] **Q6.** Vol II `celestial_holography.tex`: add ClaimStatus to 3 untagged environments
- [ ] **Q7.** Vol II `fm3_planted_forest_synthesis.tex`: move `\providecommand` to main.tex
- [ ] **Q8.** Vol II `affine_half_space_bv.tex`: verify `\chapter` works with `\input`
- [ ] **Q9.** Vol II Part II: evaluate moving `ht_bulk_boundary_line` and `celestial_boundary_transfer` to Part V
- [ ] **Q10.** Vol II: verify `equivalence.tex` is included or absorbed
- [ ] **Q11.** Vol II: verify `pva-preview.tex` included or absorbed
- [ ] **Q12.** Vol II `w-algebras.tex`: add cross-volume DS reduction remarks
- [ ] **Q13.** Vol II `examples-worked.tex` (80 lines): expand or absorb into `examples-complete.tex`
- [ ] **Q14.** Vol II `conclusion.tex` (80 lines): expand to summarize five-part architecture
- [ ] **Q15.** Vol II `concordance.tex` (147 lines): expand to proper constitution

## R. METADATA AND INFRASTRUCTURE (10 items) — MEDIUM

- [ ] **R1.** Vol I: run `python3 scripts/generate_metadata.py` and commit
- [ ] **R2.** Vol I: verify census reflects new appendices (~200+ new claims)
- [ ] **R3.** Vol I: update `notes/autonomous_state.md`
- [ ] **R4.** Vol I: verify `.gitignore` includes `archive/`
- [ ] **R5.** Vol II: create `scripts/` with build script matching Vol I
- [ ] **R6.** Vol II: create `metadata/` with census script
- [ ] **R7.** Vol I: verify `make test` passes after appendix additions
- [ ] **R8.** Vol I: run 3-pass build, verify convergence
- [ ] **R9.** Vol II: run 2-pass build, record page/error/overfull counts
- [ ] **R10.** Both: verify simultaneous builds don't interfere

## S. DEEP MATHEMATICAL FRONTIER (15 items) — FRONTIER

- [ ] **S1.** Prove S_A non-quadratic for sl_2-hat (genuine complementarity ≠ fake)
- [ ] **S2.** Prove planted-forest cubic on FM_3 vanishes for Heisenberg (abelian = quadratic)
- [ ] **S3.** Compute spectral discriminant Δ_A for Bershadsky-Polyakov W_3^(2)
- [ ] **S4.** Compute branch-line reduction quotient at genus 3 for Virasoro — verify constant 7
- [ ] **S5.** Prove diagonal GKO transgression unconditionally
- [ ] **S6.** Compute first positive KK shell in celestial BF for sl_3
- [ ] **S7.** Prove filtered trace-detecting uniqueness at two-channel level
- [ ] **S8.** Construct boundary Kodaira-Spencer class for Baxter-Rees family
- [ ] **S9.** Verify dg-shifted factorization bridge strictification for sl_2
- [ ] **S10.** Compute modular Yang-Baxter class at genus 1 for sl_2
- [ ] **S11.** Prove W-normal form vanishing extends from W_3 to W_4
- [ ] **S12.** Compute Miura-Appell symbols for W_7^(2)
- [ ] **S13.** Prove orthogonal coideal at rank 2
- [ ] **S14.** Verify metaplectic anomaly matches Weil representation theory
- [ ] **S15.** Construct genus-Clifford completion test for Heisenberg at genus 1

## T. AESTHETIC AND STRUCTURAL (15 items) — MEDIUM

- [ ] **T1.** Vol I introduction: rewrite opening to lead with categorical logarithm
- [ ] **T2.** Vol I `heisenberg_frame.tex`: add road map diagram
- [ ] **T3.** Vol I concordance: DK ladder as tikz dependency diagram
- [ ] **T4.** Vol I concordance: three-ring diagram as tikz figure
- [ ] **T5.** Vol II abstract: Swiss-cheese as FIRST sentence
- [ ] **T6.** Vol II Part IV: add "proved/remains" summary table
- [ ] **T7.** Vol II Part V: same summary table
- [ ] **T8.** Vol I: every frontier appendix has "Status and scope" remark first
- [ ] **T9.** Vol I: every frontier appendix has "What is proved here" summary
- [ ] **T10.** Vol I: master table of frontier appendices with theorem counts and Ring assignment
- [ ] **T11.** Vol I `en_koszul_duality.tex`: update §en-summary to include Swiss-cheese as item 6
- [ ] **T12.** Vol II: promote `conclusion.tex` to genuine synthesis chapter
- [ ] **T13.** Both: create shared notation page includable in both volumes
- [ ] **T14.** Vol I: verify TOC renders all frontier appendix titles
- [ ] **T15.** Vol II: verify TOC shows all five Parts

## U. FINAL INTEGRITY (25 items) — HIGH

- [ ] **U1.** Vol I: grep for unmatched `\begin{proof}` / `\end{proof}`
- [ ] **U2.** Vol I: grep for unmatched `\begin{theorem}` / `\end{theorem}`
- [ ] **U3.** Vol II: same unmatched environment check
- [ ] **U4.** Vol I: verify no `\include` (vs `\input`) for frontier appendices
- [ ] **U5.** Vol I: check for circular references
- [ ] **U6.** Vol I: find orphan labels (defined but never referenced)
- [ ] **U7.** Vol II: verify no theorem counter resets mid-chapter
- [ ] **U8.** Vol I: verify `\makeindex` and `\printindex` present
- [ ] **U9.** Both: verify `\setlength{\emergencystretch}{3em}`
- [ ] **U10.** Vol I: verify `\hfuzz=1pt` in main.tex
- [ ] **U11.** Vol I: verify no `\providecommand` conflicts with main.tex definitions
- [ ] **U12.** Vol II: verify `\providecommand{\Ainf}` doesn't conflict with `\newcommand{\Ainf}`
- [ ] **U13.** Vol I: verify bibliography alphabetically sorted
- [ ] **U14.** Vol II: verify no duplicate bib keys
- [ ] **U15.** Vol I: check for `??` in compiled PDF
- [ ] **U16.** Vol II: same
- [ ] **U17.** Vol I: verify `scripts/build.sh` has `buf_size=1000000`
- [ ] **U18.** Vol I: verify `make test-full` works
- [ ] **U19.** Both: verify clean `git status`
- [ ] **U20.** Both: verify commit history coherent (`git log --oneline | head -20`)
- [ ] **U21.** Vol I: verify `SOURCES` wildcard includes `appendices/*.tex`
- [ ] **U22.** Vol I: `git tag v43-session-complete`
- [ ] **U23.** Vol II: `git tag v2-session-complete`
- [ ] **U24.** Vol I: verify `make clean` doesn't delete frontier appendices
- [ ] **U25.** Both: verify PDF file sizes are reasonable (Vol I ~8MB, Vol II ~2MB)
