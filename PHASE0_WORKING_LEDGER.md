# Phase 0 Working Ledger (Rescaffolded)

Date: 2026-02-28
Workspace: `/Users/raeez/chiral-bar-cobar`

## Compile Snapshot
- Command: `make integrity` (forced rebuild + 3-pass `pdflatex` + stabilization pass + strict metric checks)
- Result: success (`main.pdf` produced)
- Output: `main.pdf` (919 pages, 3.75M)
- `LaTeX Error`: 0
- `Undefined control sequence`: 0
- Multiply-defined labels: 0
- Undefined references: 0
- Undefined citations: 0
- `pdfTeX` missing-destination warnings: 0

## Non-fatal Warning Snapshot
- `hyperref` PDF-string warnings: 0
- `Overfull \\hbox`/`\\vbox`: 5 (`integrity` limit: `<= 5`)
- `Underfull \\hbox`/`\\vbox`: 17 (`integrity` limit: `<= 17`)
- `Float too large for page`: 0
- `memoir` headheight warnings: 0

## Inventory Summary (All `.tex` Files Accounted)
- Total `.tex` files discovered: 86
- Active in `main.tex` include/input graph: 55
- Non-active `.tex` files: 30

## Canonical Content Ledger

### Integrated (Active Main Graph, 55 Files)
- `chapters/theory/introduction.tex`
- `chapters/theory/algebraic_foundations.tex`
- `chapters/theory/configuration_spaces.tex`
- `chapters/theory/bar_cobar_construction.tex`
- `chapters/theory/poincare_duality.tex`
- `chapters/theory/higher_genus.tex`
- `chapters/theory/koszul_across_genera.tex`
- `chapters/theory/chiral_koszul_pairs.tex`
- `chapters/theory/koszul_pair_structure.tex`
- `chapters/theory/deformation_theory.tex`
- `chapters/theory/classical_to_chiral.tex`
- `chapters/theory/chiral_modules.tex`
- `chapters/theory/poincare_duality_quantum.tex`
- `chapters/theory/quantum_corrections.tex`
- `chapters/theory/filtered_curved.tex`
- `chapters/theory/hochschild_cohomology.tex`
- `chapters/examples/free_fields.tex`
- `chapters/examples/beta_gamma.tex`
- `chapters/examples/heisenberg_eisenstein.tex`
- `chapters/examples/kac_moody_framework.tex`
- `chapters/examples/w_algebras_framework.tex`
- `chapters/examples/w3_composite_fields.tex`
- `chapters/examples/minimal_model_fusion.tex`
- `chapters/examples/minimal_model_examples.tex`
- `chapters/examples/w_algebras_deep.tex`
- `chapters/examples/deformation_quantization.tex`
- `chapters/examples/deformation_examples.tex`
- `chapters/examples/yangians.tex`
- `chapters/examples/toroidal_elliptic.tex`
- `chapters/examples/genus_expansions.tex`
- `chapters/examples/detailed_computations.tex`
- `chapters/examples/examples_summary.tex`
- `chapters/connections/poincare_computations.tex`
- `chapters/connections/feynman_diagrams.tex`
- `chapters/connections/feynman_connection.tex`
- `chapters/connections/bv_brst.tex`
- `chapters/connections/holomorphic_topological.tex`
- `chapters/connections/physical_origins.tex`
- `chapters/connections/genus_complete.tex`
- `chapters/connections/concordance.tex`
- `appendices/general_relations.tex`
- `appendices/arnold_relations.tex`
- `appendices/signs_and_shifts.tex`
- `appendices/sign_conventions.tex`
- `appendices/theta_functions.tex`
- `appendices/spectral_sequences.tex`
- `appendices/spectral_higher_genus.tex`
- `appendices/koszul_reference.tex`
- `appendices/homotopy_transfer.tex`
- `appendices/dual_methodology.tex`
- `appendices/computational_tables.tex`
- `appendices/existence_criteria.tex`
- `appendices/nilpotent_completion.tex`
- `appendices/notation_index.tex`
- `bibliography/references.tex`

### Overlap Streams Preserved but Not Included (8 Files; canonical-pointer stubs)
- `chapters/theory/bar_cobar_quasi_isomorphism.tex`
- `chapters/theory/higher_genus_full.tex`
- `chapters/theory/higher_genus_quasi_isomorphism.tex`
- `chapters/examples/heisenberg_higher_genus.tex`
- `chapters/examples/obstruction_classes.tex`
- `chapters/examples/kac_moody_computations.tex`
- `chapters/examples/w_algebras_computations.tex`
- `chapters/examples/deformation_quantization_complete.tex`
All eight overlap streams are now explicit stubs with canonical-owner pointers and no theorem body.

### Archive-Preserved Legacy (14 Files)
- `archive/legacy/bar_cobar_quasi_isomorphism_legacy.tex`
- `archive/legacy/higher_genus_full_legacy.tex`
- `archive/legacy/higher_genus_quasi_isomorphism_legacy.tex`
- `archive/legacy/kac_moody_computations_legacy.tex`
- `archive/legacy/w_algebras_computations_legacy.tex`
- `archive/legacy/deformation_quantization_legacy.tex`
- `archive/legacy/bar_cobar_quasi_isomorphism_legacy_20260228_phase0.tex`
- `archive/legacy/higher_genus_full_legacy_20260228_phase0.tex`
- `archive/legacy/higher_genus_quasi_isomorphism_legacy_20260228_phase0.tex`
- `archive/legacy/heisenberg_higher_genus_legacy_20260228_phase0.tex`
- `archive/legacy/obstruction_classes_legacy_20260228_phase0.tex`
- `archive/legacy/kac_moody_computations_legacy_20260228_phase0.tex`
- `archive/legacy/w_algebras_computations_legacy_20260228_phase0.tex`
- `archive/legacy/deformation_quantization_complete_legacy_20260228_phase0.tex`

### Debris / Off-Graph (8 Files)
- `debris/CONCEPTUAL_INVENTORY.tex`
- `debris/INTEGRATION_GUIDE_Higher_Genus_Expansion.tex`
- `debris/chiralduality.tex`
- `debris/coins_per_share_dual_engine_framework.tex`
- `debris/debris.tex`
- `debris/mainreduced.tex`
- `debris/part5c_walgebras.tex`
- `debris/part7.tex`

### Root Driver
- `main.tex` (driver; not included by itself)

## Immediate Residual Blockers
- No hard compile blockers remain in active graph.
- Submission-polish warning debt is bounded and regression-gated (`Overfull=5`, `Underfull=17`, `Float-too-large=0`; limits `5/17/0`).
- External font-stack residual is closed in this run: `ntxebgmia.vf`
  checksum/width mismatch messages are now absent (`NTXEBGMIA_MISMATCH=0`).
- Claim provenance tags are mechanically attached to all active claim-bearing theorem-like heads (`707/707` for kinds `theorem`, `lemma`, `proposition`, `corollary` in included graph).
- Machine-checkable dependency extraction for active theory theorem labels is now materialized in `PHASE0_THEOREM_DEPENDENCY_INDEX.md`, regenerated by `scripts/generate_theorem_dependency_index.py`.
- Aux-corruption recovery protocol was exercised and stabilized this run (`make clean` + full rebuild after invalid-character `.aux` failure).
- CI-style integrity gate is now active via `make integrity` / `scripts/integrity_gate.sh`.
- Proof-depth residual is now scoped to explicit conjectural items (`thm:backreaction`, `thm:curved-mc-cobar`, `thm:partition-cyclic`, `thm:yangian-self-dual`, and three conjectural corollaries listed in `PHASE0_PROOF_STATUS.md`).
