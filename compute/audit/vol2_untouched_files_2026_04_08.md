# Vol II Untouched Files Report

## Summary

Of the **64 files** \input'd in Vol II main.tex, **22 have uncommitted
modifications** (appear in `git diff --name-only`) and **42 are untouched**
(no pending changes in the working tree).

Two additional files have uncommitted modifications but are NOT \input'd
in main.tex:
- `chapters/connections/concordance.tex` (the constitution; not compiled into Vol II)
- `chapters/theory/foundations_recast_draft.tex` (draft file; not compiled)

## Counts

| Category | Count |
|----------|-------|
| Total \input'd files | 64 |
| Touched (have uncommitted changes) | 22 |
| Untouched (no pending changes) | 42 |
| Modified but not \input'd | 2 |

## Touched Files (22 of 64 input'd)

### Theory (7)
1. chapters/theory/factorization_swiss_cheese.tex
2. chapters/theory/foundations.tex
3. chapters/theory/introduction.tex
4. chapters/theory/modular_swiss_cheese_operad.tex
5. chapters/theory/pva-descent-repaired.tex

### Connections (13)
6. chapters/connections/3d_gravity.tex
7. chapters/connections/anomaly_completed_frontier.tex
8. chapters/connections/bar-cobar-review.tex
9. chapters/connections/celestial_holography_core.tex
10. chapters/connections/dnp_identification_master.tex
11. chapters/connections/line-operators.tex
12. chapters/connections/modular_pva_quantization_core.tex
13. chapters/connections/ordered_associative_chiral_kd_core.tex
14. chapters/connections/ordered_associative_chiral_kd_frontier.tex
15. chapters/connections/relative_feynman_transform.tex
16. chapters/connections/spectral-braiding-core.tex
17. chapters/connections/thqg_3d_gravity_movements_vi_x.tex
18. chapters/connections/thqg_critical_string_dichotomy.tex
19. chapters/connections/thqg_perturbative_finiteness.tex

### Examples (3)
20. chapters/examples/examples-worked.tex
21. chapters/examples/rosetta_stone.tex
22. chapters/examples/w-algebras-w3.tex

### Modified but not input'd (2, not counted above)
- chapters/connections/concordance.tex
- chapters/theory/foundations_recast_draft.tex

## Untouched Files (42 of 64 input'd)

### Appendices (1)
1. appendices/brace-signs.tex

### Theory (10)
2. chapters/theory/axioms.tex
3. chapters/theory/bv-construction.tex
4. chapters/theory/equivalence.tex
5. chapters/theory/fm-calculus.tex
6. chapters/theory/fm-proofs.tex
7. chapters/theory/locality.tex
8. chapters/theory/orientations.tex
9. chapters/theory/pva-expanded-repaired.tex
10. chapters/theory/raviolo.tex
11. chapters/theory/raviolo-restriction.tex

### Frame (1)
12. chapters/frame/preface.tex

### Connections (24)
13. chapters/connections/affine_half_space_bv.tex
14. chapters/connections/anomaly_completed_core.tex
15. chapters/connections/brace.tex
16. chapters/connections/celestial_boundary_transfer_core.tex
17. chapters/connections/celestial_boundary_transfer_frontier.tex
18. chapters/connections/celestial_holography_frontier.tex
19. chapters/connections/conclusion.tex
20. chapters/connections/dg_shifted_factorization_bridge.tex
21. chapters/connections/fm3_planted_forest_synthesis.tex
22. chapters/connections/hochschild.tex
23. chapters/connections/ht_bulk_boundary_line_core.tex
24. chapters/connections/ht_bulk_boundary_line_frontier.tex
25. chapters/connections/ht_physical_origins.tex
26. chapters/connections/log_ht_monodromy_core.tex
27. chapters/connections/log_ht_monodromy_frontier.tex
28. chapters/connections/modular_pva_quantization_frontier.tex
29. chapters/connections/spectral-braiding-frontier.tex
30. chapters/connections/thqg_gravitational_complexity.tex
31. chapters/connections/thqg_gravitational_yangian.tex
32. chapters/connections/thqg_holographic_reconstruction.tex
33. chapters/connections/thqg_modular_bootstrap.tex
34. chapters/connections/thqg_soft_graviton_theorems.tex
35. chapters/connections/thqg_symplectic_polarization.tex
36. chapters/connections/ym_synthesis_core.tex
37. chapters/connections/ym_synthesis_frontier.tex

### Examples (6)
38. chapters/examples/examples-complete-conditional.tex
39. chapters/examples/examples-complete-proved.tex
40. chapters/examples/examples-computing.tex
41. chapters/examples/w-algebras-frontier.tex
42. chapters/examples/w-algebras-virasoro.tex

## Breakdown by Part

| Part | Total input'd | Touched | Untouched |
|------|---------------|---------|-----------|
| Frame (preface) | 1 | 0 | 1 |
| Theory | 15 | 5 | 10 |
| Connections | 37 | 13 | 24 |
| Examples | 8 | 3 | 5 (including w-algebras-virasoro) |
| Appendices | 1 | 0 | 1 |
| **Not input'd** | **2** | **2** | **0** |

## Notes

- The untouched count (42/64 = 66%) represents files with no pending
  modifications in the current working tree.  They may have been modified
  in earlier committed work.
- The heaviest concentration of untouched files is in the Connections
  part (24/37 = 65% untouched), particularly the THQG gravity chapters,
  the HT/bulk-boundary chapters, and the YM synthesis chapters.
- All theory foundations files (axioms, bv-construction, equivalence,
  fm-calculus, fm-proofs, locality, orientations, raviolo,
  raviolo-restriction) are untouched.
- The preface is untouched.
