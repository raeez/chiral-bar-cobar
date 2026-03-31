# Beilinson Rectification Swarm — Master Findings Register
## Date: 2026-03-31
## Scope: Full manuscript (both volumes), 21 parallel audit agents

## Summary
- **21 agents deployed** across all chapters in both volumes
- **22 SERIOUS findings** (8 fixed, 14 remaining)
- **~55 MODERATE findings** (4 fixed, ~51 remaining)
- **Build: 2,098pp clean after fixes**

## SERIOUS Findings

### FIXED (8)
| # | File | Fix | AP |
|---|------|-----|-----|
| S1 | higher_genus_foundations:3047 | Riemann bilinear sign +2i→-2i | AP5 |
| S4 | poincare_duality_quantum:54 | D(A)=Omega(B(A))→D_Ran B(A) | AP9 |
| S6 | hochschild_cohomology:362 | ChirHoch^1(Heis) 0→C | AP5 |
| S8 | higher_genus_complementarity:2307 | Vir_0→Vir_13 self-dual | AP8 |
| S9 | higher_genus_complementarity:374 | Theta_A+Theta_{A!}=0 qualified | AP7 |
| S10 | bar_cobar_adjunction_inversion:2061 | Label collision removed | — |
| S11 | chiral_koszul_pairs:4293 | "Koszulity fails"→classical vs chiral | AP14 |
| S12 | chiral_koszul_pairs:4275 | W-alg table split universal/simple | AP14 |

### REMAINING (14)
| # | File | Diagnosis | AP |
|---|------|-----------|-----|
| S2 | poincare_duality:668 | thm:completion-koszul hidden finite-dim hypothesis | AP4/AP7 |
| S3 | derived_langlands:893 | sl2 periodicity generic vs critical level confusion | AP4/AP13 |
| S5 | chiral_koszul_pairs:1802 | Meta-thm (viii) "ChirHoch vanishes outside {0,1,2}" literally false for Vir (means generators in {0,1,2}) | AP7 |
| S7 | Cross-file | ChirHoch* = two different objects (global/curve vs fiber/disc) — AP9 | AP9 |
| S13 | yangians_drinfeld_kohno:21-25 | DK-4/5 "completion follows from MC3" overclaim | AP7 |
| S14 | yangians_drinfeld_kohno:1204 | "DK-4 closed via MC4" contradicts conj:dk4-inverse-limit | AP7 |
| S15 | yangians_computations:1437 | "DK-4 resolved" same error as S14 | AP7 |
| S16 | yangians_drinfeld_kohno:5599 | "DK-4 now resolved" third instance | AP7 |
| S17 | Vol II twisted_holography:1925-1994 | F_g formula: general gives F_1=kappa/24 but explicit says -kappa/12 (factor -2) | AP1/AP10 |
| S18 | Vol II bar-cobar-review:1300 | "Com^!=Lie≃Com" is FALSE (Lie≠Com) | AP9 |
| S19 | Vol II thqg_spectral_braiding_ext:798 | Definition tagged ProvedHere | AP4 |
| S20 | bar_cobar_adjunction_curved (signs appendix line 539) | Cobar differential sign error in AUTHORITATIVE signs appendix | AP5 |
| S21 | Vol II modular_swiss_cheese_operad:101 | Heisenberg OPE inconsistency (simple vs double pole) across Vol II | AP9 |
| S22 | Vol II modular_swiss_cheese_operad:1881 | genus-g formality claim may be overclaim for g>=1 (non-formal config spaces) | AP7 |

## KEY MODERATE Findings (selected, ~55 total)
- M31: Theorem B MC3 stale "type A only" (FIXED)
- M24: w_algebras alpha=32/(5c+22) should be 16/(5c+22) typo
- M27: Theorem C remark (-1)-shifted→-(3g-3)-shifted (FIXED)
- Shadow tower R_5 Virasoro: -12/(5c^2) should be -6/(5c^2)
- Shadow tower F_2 caption: 7/240 should be 7/5760
- Theorem D uses type-A H_N for general g (should be rho(g))
- PBW propagation scope includes beta-gamma without weight-0 qualification
- 8 Yangian AP12 stale tags ("type A" → "all simple types")
- 3 Yangian conjectures proved but still tagged Conjectured
- Vol II spectral-braiding: 6 theorems use stale (H1)-(H4) framework
- Vol II connections: orientation line convention discrepancy
- Vol II connections: (k+h^v)^g instead of kappa^g in scalar MC class
- Vol I connections: G9 "self-conjugate" at c=26 (should be c=13)
- Vol I connections: G10 Fredholm scope inflation (Heisenberg only, not full landscape)
- Concordance: EO recursion part (b) ProvedHere depends on Heuristic input
- Preface: "twelve Koszulness equivalences" (only 10 are equivalences)
- Introduction: kappa(A)=c(A)/2 stated as general (Virasoro only)

## CONVERGED Chapters (zero actionable findings)
- Lattice + census + tables (all kappa formulas independently verified)
- Vol I appendices (signs_and_shifts.tex internally consistent, shadow formulas verified)

## Coverage
- Vol I theory: 100% (all 20 theory chapters audited)
- Vol I examples: 100% (all 6 example clusters audited)
- Vol I connections: 100% (concordance + arithmetic + THQG + physics bridges)
- Vol I appendices: 100%
- Vol I frame: 100% (preface + intro + heisenberg frame)
- Vol II theory: 100% (all 7 theory files)
- Vol II connections: 100% (core + BBL + THQG)
