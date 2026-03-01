# Conjecture Registry — Chiral Bar-Cobar Monograph
## Updated March 1, 2026 (Session 44)

**Census**: 78 uses of `\ClaimStatusConjectured` in .tex files; 35 theorem-level + 6 per-item = ~35 distinct mathematical claims.

---

## Classification Summary

| Category | Distinct Claims | Action |
|----------|----------------|--------|
| **PROVED (Sessions 42-44)** | 10 | See below |
| **BORDERLINE PROVABLE** | 1 | Arnold g≥2 (computational) |
| **GENUINELY OPEN** | 5 | Actual open mathematical problems |
| **PHYSICS** | ~28 | Correctly scoped outside pure math |

---

## PROVED IN SESSIONS 42-44

### Session 42
1. **thm:elliptic-vs-rational** (toroidal_elliptic.tex) → ProvedHere. Correction-order spectral sequence + Zhu modular invariance.
2. **thm:qme-bar-cobar** (bv_brst.tex) → ProvedHere. 2-stage: algebraic QME↔MC + functor-level via thm:bv-functor.
3. **prop:modular-weight-formula** (heisenberg_eisenstein.tex) → ProvedElsewhere. Standard Siegel modular form theory.
4. **thm:mk-tree-level** split from thm:mk-general-structure → ProvedHere.

### Session 43
5. **thm:affine-periodicity-critical** (koszul_pair_structure.tex) → ProvedHere. BD comparison + Gel'fand-Fuchs/Feigin-Tsygan.
6. **thm:bv-structure-bar** (koszul_pair_structure.tex) → ProvedHere. BV algebra on bar complex + QME.
7. **thm:mk-general-structure** (feynman_diagrams.tex) → ProvedHere. All-genus Feynman expansion via Feynman transform + Arakelov-Green.
8. **thm:chiral-kontsevich** (deformation_quantization.tex) → ProvedHere. Stokes on FM compactification.
9. **thm:deformation-acyclicity** (chiral_modules.tex) → ProvedHere. Grothendieck + Katz-Oda + Deligne nearby/vanishing cycles.

### Session 44
10. **thm:EO-recursion** (genus_complete.tex) — **Partially proved**: Koszul case → ProvedHere (Feynman transform + abstract topological recursion). Heisenberg → ProvedElsewhere. General case → Conjectured.
11. **thm:w-algebra-bar-cobar** items 2,3 (holomorphic_topological.tex) — **Partially proved**: Generic level → ProvedHere (weight spectral sequence + thm:w-algebra-hochschild). Admissible levels → Conjectured.

---

## REMAINING BORDERLINE (1)

### Genus ≥ 2 Arnold Relations
- **File**: higher_genus.tex, line 1772
- **Label**: Part (c) of `thm:quantum-arnold-relations`
- **What's needed**: Explicit computation with prime form and Arakelov-Green function on Σ_g; expected from Fay trisecant identity
- **Note**: The propagator definition at genus g≥2 requires using the full exterior derivative d (not just ∂) of the Arakelov-Green function to produce a mixed (1,0)+(0,1) form; the resulting Arnold 3-form then has a (1,1)-component via cross-terms

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
