# Execution Plan — Chiral Bar-Cobar Monograph
## Updated March 1, 2026 (Session 42)

---

## Current State

### Manuscript
- **951 pages**, zero LaTeX errors, zero undefined refs, zero warnings
- 55 active .tex files

### Claim Census (verified via `grep -rF` on .tex files)
| Status | Count |
|--------|-------|
| ProvedHere | 472 |
| ProvedElsewhere | 264 |
| Conjectured | 70 instances (~38 distinct claims) |
| Open | 0 |

### Session 42 Accomplishments
1. **Fixed 16 hyperref warnings** — All `\texorpdfstring` fixes in chiral_koszul_pairs.tex (4), detailed_computations.tex (1), beta_gamma.tex (1)
2. **Proved thm:elliptic-vs-rational** (toroidal_elliptic.tex) — Conjectured → ProvedHere. Complete proof via correction-order spectral sequence + Zhu modular invariance + Heisenberg verification.
3. **Corrected affine periodicity theorem** (koszul_pair_structure.tex) — The statement "period 2h for all g" was found to be incorrect for rank > 1. Explicit computation shows sl₃ fails 6-periodicity at degree 1 vs 7. Theorem refined to: rank-1 periodicity (proved in principle) + higher-rank polynomial growth (correct structural statement). Kept as Conjectured with greatly enhanced analysis.
4. **Proved thm:qme-bar-cobar** (bv_brst.tex) — Conjectured → ProvedHere. The gap (functor-level natural transformation) was already closed by thm:bv-functor (line 694, ProvedHere). Proof rewritten as 2-stage: algebraic QME↔MC equivalence + functor-level naturality via Verdier duality.

### Conjectured Breakdown (updated)
| Category | Count |
|----------|-------|
| Definitely provable | 1 (affine rank-1 periodicity) |
| Borderline provable | 3 |
| Computational | 2 |
| Non-trivially computational | 1 |
| Genuinely open | 5 |
| Physics | ~28 |

---

## Remaining Work

### A. Provable Conjectures

**1. Affine periodicity at critical level, rank 1** (koszul_pair_structure.tex:588)
- For ŝl₂ at k = -2: CH^{n+4} ≅ CH^n
- Strategy: Same as Virasoro periodicity proof (spectral sequence + Gel'fand-Fuchs)
- Status: Proof strategy is clear; main technical step is BD comparison at critical level

### B. Borderline Provable Conjectures

2. **thm:chiral-kontsevich** (deformation_quantization.tex:162) — all-orders Stokes boundary cancellation
3. **thm:EO-recursion** (genus_complete.tex:260) — topological recursion axiom verification
4. **thm:mk-general-structure** (feynman_diagrams.tex) — all-genus propagator identification (tree-level now split out as thm:mk-tree-level, ProvedHere)

### C. Items NOT to Touch

- **~28 physics conjectures**: Correctly scoped, appropriate for the monograph
- **5 genuinely open problems**: Actual open math — keep as conjectures
- **2+1 computational items**: Well-defined but laborious calculations
- **All ProvedHere items**: Do not re-verify or rewrite

---

## Completed Items

- [x] Fix 16 hyperref warnings (Session 42)
- [x] Prove thm:elliptic-vs-rational (Session 42)
- [x] Correct affine periodicity theorem formulation (Session 42)
- [x] Prove thm:qme-bar-cobar (Session 42)
- [x] Split thm:mk-general-structure: tree-level → thm:mk-tree-level (ProvedHere), all-genus remains Conjectured (Session 42)
- [x] Systematic audit of all 70 remaining Conjectured items — all correctly classified (Session 42)
- [x] Documentation rewrite — CLAUDE.md, EXECUTION_PLAN.md, CONJECTURE_REGISTRY.md (Session 40)
- [x] Prove Main Theorem C / Kodaira-Spencer map (Session 20)
- [x] All 40 Open → ProvedHere (Sessions 16-18)
- [x] Phases 0-6 complete (Sessions 1-15)
