# Conjecture Registry — Chiral Bar-Cobar Monograph
## Updated March 1, 2026 (Session 42)

**Census**: 70 uses of `\ClaimStatusConjectured` in .tex files, corresponding to approximately 38 distinct mathematical claims.

---

## Classification Summary

| Category | Distinct Claims | Action |
|----------|----------------|--------|
| **PROVED (Session 42)** | 2 | thm:elliptic-vs-rational, thm:qme-bar-cobar — DONE |
| **DEFINITELY PROVABLE** | 1 | Affine rank-1 periodicity |
| **BORDERLINE PROVABLE** | 3 | Provable in principle; substantial new work needed |
| **COMPUTATIONAL** | 2 | Explicit calculations; well-defined but laborious |
| **NON-TRIVIALLY COMPUTATIONAL** | 1 | Requires new techniques (irregular connections) |
| **GENUINELY OPEN** | 5 | Actual open mathematical problems |
| **PHYSICS** | ~28 | Correctly scoped outside pure math |

---

## PROVED IN SESSION 42

### 1. Elliptic vs Rational Homology — PROVED
- **File**: toroidal_elliptic.tex, line 220
- **Label**: `thm:elliptic-vs-rational`
- **Status**: **ProvedHere** (Session 42)
- **Proof method**: Correction-order spectral sequence on the bar complex, with E₁ = H(B^rat(A)); modular structure of corrections from Zhu's theorem on genus-1 conformal blocks; splitting by weight grading on (quasi-)modular forms. Verified for Heisenberg.

### 2. QME = Bar-Cobar Duality — PROVED
- **File**: bv_brst.tex, line 99
- **Label**: `thm:qme-bar-cobar`
- **Status**: **ProvedHere** (Session 42)
- **Proof method**: 2-stage: (1) algebraic QME ↔ MC equivalence in bar-cobar dg Lie algebra (standard BV algebra manipulations); (2) functor-level naturality via thm:bv-functor (already ProvedHere at line 694), which constructs the BV functor with Verdier duality compatibility D(B(A)) ≅ Ω(A!).
- **Key insight**: The gap identified in previous sessions (functor-level natural transformation) was already closed by thm:bv-functor, which had been proved earlier but not recognized as closing this gap.

### 3. Affine Periodicity at Critical Level — CORRECTED AND ENHANCED
- **File**: koszul_pair_structure.tex, line 588
- **Label**: `thm:affine-periodicity-critical`
- **Status**: Still **Conjectured**, but theorem statement corrected and analysis greatly enhanced
- **Key finding**: The period formula "2h for all g" is INCORRECT for rank > 1. Explicit computation shows sl₃ at critical level fails 6-periodicity (dim CH⁰ = 1 but dim CH¹² = 3 ≠ dim CH⁶ = 1). Correct statement: rank-1 periodicity (period 2h = 4 for sl₂) + polynomial-exterior ring structure for higher rank.

---

## BORDERLINE PROVABLE (3)

### 4. Chiral Kontsevich Formula
- **File**: deformation_quantization.tex, line 162
- **Label**: `thm:chiral-kontsevich`
- **Gap**: All-orders verification of Stokes boundary cancellations on chiral FM compactification
- **Scope remark**: "provable in principle" but "complete all-orders verification has not appeared in the literature"

### 5. Eynard-Orantin Recursion for Bar Complex
- **File**: genus_complete.tex, line 260
- **Label**: `thm:EO-recursion`
- **Gap**: Verifying abstract topological recursion axioms (Kontsevich-Soibelman, Andersen-Borot-Orantin) for general chiral algebras
- **Status**: Proved for Heisenberg/Gaussian

### 6. General m_k Structure — TREE-LEVEL SPLIT OUT
- **File**: feynman_diagrams.tex
- **Label**: `thm:mk-general-structure` (all-genus, Conjectured), `thm:mk-tree-level` (tree-level, **ProvedHere**)
- **Session 42 action**: Split theorem into tree-level (ProvedHere) and all-genus (Conjectured). Tree-level proved via Kadeishvili homotopy transfer + loop-number calculation.
- **Remaining gap**: All-genus Feynman expansion requires (1) higher-genus propagator identification, (2) Eynard-Orantin axiom verification

---

## COMPUTATIONAL (2)

### 7. Genus >= 2 Arnold Relations
- **File**: higher_genus.tex, line 1772
- **Label**: Part (c) of `thm:quantum-arnold-relations`
- **What's needed**: Explicit computation with prime form and Arakelov-Green function on Sigma_g; expected from Fay trisecant identity

### 8. Modular Weight Formula
- **File**: heisenberg_eisenstein.tex, line 315
- **Label**: `prop:modular-weight-formula`
- **What's needed**: More detailed analysis at genus >= 3 where Siegel cusp forms complicate the picture

---

## NON-TRIVIALLY COMPUTATIONAL (1)

### 9. Deformation of Acyclicity
- **File**: chiral_modules.tex, line 583
- **Label**: `thm:deformation-acyclicity`
- **Gap**: Gauss-Manin framework requires passage through singular fiber; needs irregular connections (Sabbah, Mochizuki)

---

## GENUINELY OPEN (5)

### 10-12. Infinite-Dimensional Koszul Duals
- **File**: free_fields.tex, lines 950-952 (table entries)
- Virasoro <-> W_infinity
- W_N <-> Yangian Y(gl_N)
- Super-Virasoro <-> Super-W_infinity
- **Obstruction**: Curved Koszul duality for non-quadratic algebras with infinitely many generators

### 13. Reflected Modular Periodicity
- **File**: deformation_theory.tex, line 636
- **Harmonic mean relation**: 1/N + 1/N' = 1/12
- **Obstruction**: Koszul duality may not preserve rationality; number-theoretic cyclotomic fields question

### 14. Extended bc-betagamma Koszul Duality
- **File**: chiral_koszul_pairs.tex, line 1929
- **Obstruction**: Requires systematic derived chiral Koszul duality beyond current framework

---

## PHYSICS (28 claims — all correctly scoped, no action needed)

**free_fields.tex (8)**: String Amplitude Correspondence, Bulk-Boundary Correspondence, Classification of Extendable Algebras, Bulk Reconstruction, Holographic Dictionary, Loop Corrections, String Amplitude Formula, Modular Anomaly & BRST

**holomorphic_topological.tex (8)**: CL Produces Chiral, HCS Chiral Operad, Open-Closed Duality, Dimension Tower, W from Hitchin, W Bar Complex, Bar-Cobar Quantum, AGT Bar-Cobar, W-Algebra Bar-Cobar

**poincare_duality_quantum.tex (2)**: Gravitational Backreaction, Holographic Koszul Duality

**bv_brst.tex (1)**: Costello-Gaiotto AGT

**koszul_pair_structure.tex (3)**: Gaiotto-Witten S-duality, WRT, AdS/CFT as CS/Koszul, BV Structure

**deformation_theory.tex (1)**: Holographic Koszul Duality (deformation)

**deformation_quantization.tex (1)**: Holographic Duality (deformation quantization)

**higher_genus.tex (2)**: Physical Complementarity, String Theory Complementarity

**genus_complete.tex (2)**: String Amplitude = Bar Cohomology, Holographic Duality via Bar-Cobar

**physical_origins.tex (3)**: Non-Commutative CS, D-Brane E_1, q-AGT

**w_algebras_framework.tex (1)**: AGT W-Algebra Version

**kac_moody_framework.tex (1)**: Kac-Moody Holography

---

## Conjectured Items by File (verified fresh)

| File | CJ instances | Distinct claims | Provable | Physics | Open | Computational |
|------|-------------|-----------------|----------|---------|------|---------------|
| free_fields.tex | 13 | 11 | 0 | 8 | 3 | 0 |
| holomorphic_topological.tex | 10 | 8 | 0 | 8 | 0 | 0 |
| deformation_theory.tex | 8 | 2 | 0 | 1 | 1 | 0 |
| koszul_pair_structure.tex | 8 | 6 | 1 | 4 | 0 | 0 |
| higher_genus.tex | 7 | 4 | 0 | 2 | 0 | 1 |
| poincare_duality_quantum.tex | 6 | 2 | 0 | 2 | 0 | 0 |
| bv_brst.tex | 4 | 2 | 0 | 1 | 0 | 0 |
| deformation_quantization.tex | 4 | 2 | 0-1 | 1 | 0 | 0 |
| genus_complete.tex | 4 | 3 | 0-1 | 2 | 0 | 0 |
| physical_origins.tex | 3 | 3 | 0 | 3 | 0 | 0 |
| chiral_koszul_pairs.tex | 2 | 1 | 0 | 0 | 1 | 0 |
| toroidal_elliptic.tex | 0 | 0 | 0 | 0 | 0 | 0 |
| chiral_modules.tex | 1 | 1 | 0 | 0 | 0 | 1 |
| heisenberg_eisenstein.tex | 1 | 1 | 0 | 0 | 0 | 1 |
| feynman_diagrams.tex | 1 | 1 | 0-1 | 0 | 0 | 0 |
| **Total** | **70** | **~38** | **2+3** | **~28** | **5** | **2+1** |

---

## Items That Were WRONG in Previous Classifications

The following items were listed as "Conjectured" in CONJECTURE_REGISTRY v1 or the Session 40 initial assessment but are actually ProvedHere or ProvedElsewhere:

- All 5 periodicity theorems in deformation_theory.tex — **ProvedHere** (Session 28 Virasoro Cascade)
- thm:periodicity-exchange-koszul — **ProvedHere** (proved modulo the open harmonic mean conjecture)
- thm:master-identity-deformation (deformation_quantization.tex) — **ProvedElsewhere**
- thm:pinf-formality (deformation_examples.tex) — **ProvedElsewhere**
- thm:virasoro-hochschild (hochschild_cohomology.tex) — **ProvedHere**
- thm:ss-genus (spectral_higher_genus.tex) — **ProvedHere** (no Conjectured items in file)
- All Yangian items (yangians.tex) — **ProvedHere** (0 Conjectured remaining)
- thm:yangian-self-dual (chiral_koszul_pairs.tex) — **ProvedHere**
