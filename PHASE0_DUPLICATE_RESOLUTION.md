# Phase 0 Duplicate Resolution (Rescaffolded)

Date: 2026-02-28

## Duplicate-Label Status
- Initial active-graph duplicate labels observed this run: 148 (stale mixed overlap graph)
- Post-canonicalization active-graph duplicate labels: 20
- Current active-graph duplicate labels: 0 (`main.log`: no `multiply defined` warnings)
- Current repository-wide duplicate labels (`*.tex` scope, including off-graph/archives/debris): 0

## Canonical Stack Decisions (Merge-or-Reference)

| Overlap Source | Canonical Active Owner | Resolution in `main.tex` | Preservation |
|---|---|---|---|
| `chapters/theory/bar_cobar_quasi_isomorphism.tex` | `chapters/theory/bar_cobar_construction.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/bar_cobar_quasi_isomorphism_legacy_20260228_phase0.tex` |
| `chapters/theory/higher_genus_full.tex` | `chapters/theory/higher_genus.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/higher_genus_full_legacy_20260228_phase0.tex` |
| `chapters/theory/higher_genus_quasi_isomorphism.tex` | `chapters/theory/higher_genus.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/higher_genus_quasi_isomorphism_legacy_20260228_phase0.tex` |
| `chapters/examples/heisenberg_higher_genus.tex` | `chapters/examples/heisenberg_eisenstein.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/heisenberg_higher_genus_legacy_20260228_phase0.tex` |
| `chapters/examples/obstruction_classes.tex` | `chapters/theory/higher_genus.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/obstruction_classes_legacy_20260228_phase0.tex` |
| `chapters/examples/kac_moody_computations.tex` | `chapters/examples/kac_moody_framework.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/kac_moody_computations_legacy_20260228_phase0.tex` |
| `chapters/examples/w_algebras_computations.tex` | `chapters/examples/w_algebras_framework.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/w_algebras_computations_legacy_20260228_phase0.tex` |
| `chapters/examples/deformation_quantization_complete.tex` | `chapters/examples/deformation_quantization.tex` | removed from active include graph | source replaced by canonical-pointer stub; full body snapshot in `archive/legacy/deformation_quantization_complete_legacy_20260228_phase0.tex` |

## Label De-dup Passes Applied

| Duplicate Label | Old Location(s) | Canonical Label Kept | Change |
|---|---|---|---|
| `prop:filtered-to-curved`, `ex:*bar-completion`, `thm:bar-convergence`, `rem:practitioner-takeaway` | `bar_cobar_construction.tex` + `filtered_curved.tex` | `bar_cobar_construction.tex` keys | renamed `filtered_curved.tex` labels with `-fc` suffix |
| `lem:orientation` | `free_fields.tex` + `bar_cobar_construction.tex` | `bar_cobar_construction.tex` key | renamed in `free_fields.tex` to `lem:orientation-freefields` |
| `sec:fusion-examples` | `free_fields.tex` + `minimal_model_examples.tex` | `minimal_model_examples.tex` key | renamed in `free_fields.tex` to `sec:free-fields-fusion-overview` |
| `thm:fact-homology` | `configuration_spaces.tex` + `poincare_duality_quantum.tex` | `configuration_spaces.tex` key | renamed in `poincare_duality_quantum.tex` to `thm:fact-homology-quantum` |
| `thm:normal-crossings` | two locations in `configuration_spaces.tex` | first theorem key | second renamed to `thm:normal-crossings-preservation` |
| `thm:completion-convergence` | `existence_criteria.tex` + `nilpotent_completion.tex` | `nilpotent_completion.tex` key | renamed in `existence_criteria.tex` to `thm:completion-convergence-criteria` |
| `const:quadratic-dual` | `existence_criteria.tex` + `algebraic_foundations.tex` | `algebraic_foundations.tex` key | renamed in `existence_criteria.tex` to `const:quadratic-dual-criteria` |
| `def:curved-ainfty` | `w_algebras_framework.tex` + `bar_cobar_construction.tex` | `bar_cobar_construction.tex` key | renamed in `w_algebras_framework.tex` to `def:curved-ainfty-w` |
| `ex:virasoro-completion` | `nilpotent_completion.tex` + `chiral_koszul_pairs.tex` | `nilpotent_completion.tex` key | renamed in `chiral_koszul_pairs.tex` to `ex:virasoro-completion-chiral` |
| `thm:curvature-central` | `koszul_reference.tex` + `bar_cobar_construction.tex` | `bar_cobar_construction.tex` key | renamed in appendix to `thm:curvature-central-appendix` |
| `app:koszul_higher_genus` | `koszul_reference.tex` + `koszul_across_genera.tex` | `koszul_across_genera.tex` key | renamed in appendix to `app:koszul-reference-higher-genus` |

## Cross-Reference Integrity
- Added canonical alias labels for drifted legacy keys (chapter/theorem/definition aliases) so old references resolve without reintroducing duplicate labels.
- Fixed malformed broken keys split across lines:
  - `thm:arnold- +three` -> `thm:arnold-three`
  - `thm:mumford- formula` -> `thm:mumford-formula`

## Current Risk
- Duplicate-label risk in active graph: closed.
- `hyperref` PDF-string risk in active graph: closed (`main.log`: 0 token warnings).
- Repository-wide duplicate labels in full `*.tex` scope: closed (`0` duplicate label keys after off-graph archival namespacing).
- Off-graph semantic-drift risk from duplicated theorem bodies: materially closed (all eight overlap streams now stubs).
- Remaining structural risk is warning-polish only.
- Current active-graph warning-polish status: `Overfull=0`, `Underfull=0`, `Float-too-large=0`.
