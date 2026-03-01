# Execution Plan — Chiral Bar-Cobar Monograph
## Updated March 1, 2026 (Session 44)

---

## Current State

### Manuscript
- **951 pages**, zero LaTeX errors, zero undefined refs, zero warnings
- 55 active .tex files

### Claim Census (verified via `grep -rF` on .tex files)
| Status | Count |
|--------|-------|
| ProvedHere (theorem-level) | 444 |
| ProvedElsewhere (theorem-level) | 227 |
| Conjectured (theorem-level) | 35 |
| Per-item ProvedHere | 12 |
| Per-item Conjectured | 6 |
| Open | 0 |

### Session 44 Accomplishments
1. **Proved thm:EO-recursion for Koszul algebras** (genus_complete.tex) — Restructured as 3-part theorem: (a) Heisenberg ProvedElsewhere, (b) Koszul ProvedHere, (c) General Conjectured. Proof via Feynman transform (thm:mk-general-structure) + abstract topological recursion axiom verification.
2. **Proved W-algebra Koszul property at generic k** (holomorphic_topological.tex) — Items 2,3 of thm:w-algebra-bar-cobar: ProvedHere at generic k via weight spectral sequence degeneration + thm:w-algebra-hochschild. Admissible levels remain Conjectured.
3. Updated documentation: CONJECTURE_REGISTRY.md, EXECUTION_PLAN.md

### Conjectured Breakdown (updated)
| Category | Count |
|----------|-------|
| Remaining borderline | 1 (Arnold g≥2) |
| Genuinely open | 5 |
| Physics | ~28 |

---

## Remaining Work

### A. Remaining Borderline Item

**1. Genus ≥ 2 Arnold Relations** (higher_genus.tex:1772)
- Part (c) of `thm:quantum-arnold-relations`
- Requires explicit computation with Arakelov-Green function + Fay trisecant identity
- Propagator definition needs to use full d (not just ∂) for mixed form types
- Expected result: A_3^(g) = 2πi · μ_Ar where μ_Ar is the Arakelov (1,1)-form

### B. Items NOT to Touch

- **~28 physics conjectures**: Correctly scoped, appropriate for the monograph
- **5 genuinely open problems**: Actual open math — keep as conjectures
- **All ProvedHere items**: Do not re-verify or rewrite

---

## Completed Items

- [x] Prove thm:EO-recursion for Koszul algebras (Session 44)
- [x] Prove W-algebra Koszul at generic k (Session 44)
- [x] Prove thm:affine-periodicity-critical (Session 43)
- [x] Prove thm:bv-structure-bar (Session 43)
- [x] Prove thm:mk-general-structure all-genus (Session 43)
- [x] Prove thm:chiral-kontsevich (Session 43)
- [x] Prove thm:deformation-acyclicity (Session 43)
- [x] Fix 16 hyperref warnings (Session 42)
- [x] Prove thm:elliptic-vs-rational (Session 42)
- [x] Correct affine periodicity theorem formulation (Session 42)
- [x] Prove thm:qme-bar-cobar (Session 42)
- [x] Split thm:mk-general-structure tree-level (Session 42)
- [x] Upgrade prop:modular-weight-formula to ProvedElsewhere (Session 42)
- [x] Systematic audit of all Conjectured items (Session 42)
- [x] Documentation rewrite (Session 40)
- [x] Prove Main Theorem C / Kodaira-Spencer map (Session 20)
- [x] All 40 Open → ProvedHere (Sessions 16-18)
- [x] Phases 0-6 complete (Sessions 1-15)
