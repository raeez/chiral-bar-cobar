# Modular Homotopy Theory Treatise Audit

This report summarizes a structural audit of the uploaded Volume I and Volume II source archives.

## Critical findings

- Volume I is already organized as a large treatise: Overture, Algebraic Engine, Standard Landscape, Bridges and Programmes, Frontier.
- Volume II is still chapter/section mis-scaled: chapter-size files are currently embedded as sections, and several large files insert local `\tableofcontents`, producing repeated Contents entries in the compiled TOC.
- Several Volume I files currently living under `appendices/` are promoted into the main theorem flow by `main.tex` and should be physically relocated into `chapters/` if the public architecture is to be stable.
- Monster files should be split. A practical threshold from the audit is: split any file with >1500 lines, >120 references, or >=10 conjectural/conditional markers.
- Cross-volume references need a shared label system. Volume II currently carries many unresolved references which should be imported from Volume I rather than left unresolved.
- Some topics appear as short bridge stubs in Volume I and as full chapters in Volume II; these need canonical homes.

## Especially overloaded files

### Volume I
- `chapters/examples/w_algebras.tex`
- `chapters/theory/chiral_hochschild_koszul.tex`
- `chapters/theory/chiral_modules.tex`
- `chapters/examples/lattice_foundations.tex`
- `chapters/examples/bar_complex_tables.tex`
- `chapters/connections/concordance.tex`
- `appendices/nonlinear_modular_shadows.tex`

### Volume II
- `chapters/connections/ht_bulk_boundary_line.tex`
- `chapters/connections/anomaly_completed_topological_holography.tex`
- `chapters/connections/ordered_associative_chiral_kd.tex`
- `chapters/connections/modular_pva_quantization.tex`
- `chapters/connections/celestial_holography.tex`
- `chapters/connections/ym_synthesis.tex`
- `chapters/examples/w-algebras.tex`

## Files that need canonical-home decisions

- `holomorphic_topological.tex` — short bridge form in V1, full chapter in V2.
- `physical_origins.tex` — short bridge form in V1, full chapter in V2.
- `twisted_holography_quantum_gravity.tex` — short bridge form in V1, full frontier form in V2.
- `ordered_associative_chiral_kd.tex` — appendix-scale in V1, major chapter in V2.
- `dg_shifted_factorization_bridge.tex` — appendix-scale in V1, major chapter in V2.
- `concordance.tex` — very large atlas chapter in V1, short ledger in V2.

See `v1_audit.csv` and `v2_audit.csv` for the per-file metrics.
