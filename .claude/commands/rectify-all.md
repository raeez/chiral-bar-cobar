---
description: "Launch Chriss-Ginzburg rectification across all chapters of all three volumes in parallel tiers"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Full Three-Volume Rectification

The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

Launch `/chriss-ginzburg-rectify` on every chapter of all three volumes, in tiered parallel waves. One agent per file. Worktree isolation for each.

**Model assignment principle**: opus for anything with proofs, formulas, or cross-reference networks requiring independent verification. Sonnet for tables, census files, editorial/frame chapters, mechanical frontier extensions, and simple example families.

**Rate-limit discipline**: launch in waves of 5-8 agents. Wait for completions or confirmations before the next wave. Never 25 agents simultaneously.

---

## Tier 0: Load-bearing theory (launch first, ALL opus)

These files have the most downstream citations in the dependency DAG. Errors here propagate furthest.

```
Agent(description="Rectify introduction", isolation="worktree", model="opus",
  prompt="/chriss-ginzburg-rectify chapters/theory/introduction.tex")

Agent(description="Rectify bar-cobar-curved", isolation="worktree", model="opus",
  prompt="/chriss-ginzburg-rectify chapters/theory/bar_cobar_adjunction_curved.tex")

Agent(description="Rectify bar-cobar-inversion", isolation="worktree", model="opus",
  prompt="/chriss-ginzburg-rectify chapters/theory/bar_cobar_adjunction_inversion.tex")

Agent(description="Rectify higher-genus-modular", isolation="worktree", model="opus",
  prompt="/chriss-ginzburg-rectify chapters/theory/higher_genus_modular_koszul.tex")

Agent(description="Rectify chiral-koszul-pairs", isolation="worktree", model="opus",
  prompt="/chriss-ginzburg-rectify chapters/theory/chiral_koszul_pairs.tex")
```

## Tier 1: Structural theory (launch second, ALL opus)

```
Agent (opus): chapters/theory/chiral_hochschild_koszul.tex
Agent (opus): chapters/theory/higher_genus_foundations.tex
Agent (opus): chapters/theory/higher_genus_complementarity.tex
Agent (opus): chapters/theory/chiral_center_theorem.tex
Agent (opus): chapters/theory/e1_modular_koszul.tex
Agent (opus): chapters/theory/en_koszul_duality.tex
Agent (opus): chapters/theory/ordered_associative_chiral_kd.tex
Agent (opus): chapters/theory/configuration_spaces.tex
Agent (opus): chapters/theory/chiral_modules.tex
Agent (opus): chapters/theory/derived_langlands.tex
Agent (opus): chapters/theory/poincare_duality_quantum.tex
Agent (opus): chapters/theory/poincare_duality.tex
Agent (opus): chapters/theory/koszul_pair_structure.tex
Agent (opus): chapters/theory/filtered_curved.tex
Agent (opus): chapters/theory/fourier_seed.tex
Agent (opus): chapters/theory/hochschild_cohomology.tex
Agent (opus): chapters/theory/quantum_corrections.tex
Agent (opus): chapters/theory/computational_methods.tex
Agent (opus): chapters/theory/algebraic_foundations.tex
Agent (opus): chapters/theory/bar_construction.tex
Agent (opus): chapters/theory/cobar_construction.tex
```

Also the remaining dispatchers (opus — these contain load-bearing cross-references):
```
Agent (opus): chapters/theory/bar_cobar_adjunction.tex
Agent (opus): chapters/theory/higher_genus.tex
```

## Tier 2: Standard landscape (launch third, opus for dense families, sonnet for simple)

```
Agent (opus): chapters/examples/w_algebras.tex
Agent (opus): chapters/examples/w_algebras_deep.tex
Agent (opus): chapters/examples/w3_composite_fields.tex
Agent (opus): chapters/examples/yangians_drinfeld_kohno.tex
Agent (opus): chapters/examples/yangians_computations.tex
Agent (opus): chapters/examples/yangians_foundations.tex
Agent (opus): chapters/examples/yangians.tex
Agent (opus): chapters/examples/kac_moody.tex
Agent (opus): chapters/examples/minimal_model_examples.tex
Agent (opus): chapters/examples/minimal_model_fusion.tex
Agent (opus): chapters/examples/deformation_quantization.tex
Agent (opus): chapters/examples/deformation_quantization_examples.tex
Agent (opus): chapters/examples/genus_expansions.tex
Agent (sonnet): chapters/examples/free_fields.tex
Agent (sonnet): chapters/examples/lattice_foundations.tex
Agent (sonnet): chapters/examples/beta_gamma.tex
Agent (sonnet): chapters/examples/heisenberg_eisenstein.tex
Agent (sonnet): chapters/examples/toroidal_elliptic.tex
Agent (sonnet): chapters/examples/bar_complex_tables.tex
Agent (sonnet): chapters/examples/landscape_census.tex
```

## Tier 3: Connections + frontier (launch fourth, SPLIT opus/sonnet)

### Opus — constitution, load-bearing bridges, dense proof chapters:
```
Agent (opus): chapters/connections/concordance.tex
Agent (opus): chapters/connections/arithmetic_shadows.tex
Agent (opus): chapters/connections/frontier_modular_holography_platonic.tex
Agent (opus): chapters/connections/thqg_open_closed_realization.tex
Agent (opus): chapters/connections/thqg_holographic_reconstruction.tex
Agent (opus): chapters/connections/entanglement_modular_koszul.tex
Agent (opus): chapters/connections/holographic_codes_koszul.tex
Agent (opus): chapters/connections/feynman_connection.tex
Agent (opus): chapters/connections/bv_brst.tex
Agent (opus): chapters/connections/ym_boundary_theory.tex
Agent (opus): chapters/connections/holomorphic_topological.tex
Agent (opus): chapters/connections/twisted_holography_quantum_gravity.tex
Agent (opus): chapters/connections/kontsevich_integral.tex
Agent (opus): chapters/connections/physical_origins.tex
```

### Sonnet — mechanical compilations, extensions, editorial:
```
Agent (sonnet): chapters/connections/genus_complete.tex
Agent (sonnet): chapters/connections/thqg_gravitational_complexity.tex
Agent (sonnet): chapters/connections/thqg_3d_gravity_movements_vi_x.tex [Vol II only]
Agent (sonnet): chapters/connections/thqg_soft_graviton_theorems.tex
Agent (sonnet): chapters/connections/thqg_symplectic_polarization.tex
Agent (sonnet): chapters/connections/thqg_perturbative_finiteness.tex
Agent (sonnet): chapters/connections/thqg_fredholm_partition_functions.tex
Agent (sonnet): chapters/connections/thqg_gravitational_s_duality.tex
Agent (sonnet): chapters/connections/thqg_gravitational_yangian.tex
Agent (sonnet): chapters/connections/thqg_modular_bootstrap.tex
Agent (sonnet): chapters/connections/thqg_critical_string_dichotomy.tex
Agent (sonnet): chapters/connections/thqg_entanglement_programme.tex
Agent (sonnet): chapters/connections/thqg_concordance_supplement.tex
Agent (sonnet): chapters/connections/thqg_introduction_supplement.tex
Agent (sonnet): chapters/connections/thqg_introduction_supplement_body.tex
Agent (sonnet): chapters/connections/thqg_preface_supplement.tex
Agent (sonnet): chapters/connections/semistrict_modular_higher_spin_w3.tex
Agent (sonnet): chapters/connections/feynman_diagrams.tex
Agent (sonnet): chapters/connections/poincare_computations.tex
Agent (sonnet): chapters/connections/outlook.tex
Agent (sonnet): chapters/connections/editorial_constitution.tex
Agent (sonnet): chapters/connections/ym_higher_body_couplings.tex
Agent (sonnet): chapters/connections/ym_instanton_screening.tex
```

### Frame (sonnet — editorial, low conceptual density):
```
Agent (sonnet): chapters/frame/preface.tex
Agent (sonnet): chapters/frame/heisenberg_frame.tex
Agent (sonnet): chapters/frame/guide_to_main_results.tex
```

## Tier 4: Appendices (launch fifth, ALL sonnet except signs)

### Opus — authoritative reference, must be perfect:
```
Agent (opus): appendices/signs_and_shifts.tex
Agent (opus): appendices/nonlinear_modular_shadows.tex
```

### Sonnet — tables, reference material, standard proofs:
```
Agent (sonnet): appendices/arnold_relations.tex
Agent (sonnet): appendices/branch_line_reductions.tex
Agent (sonnet): appendices/casimir_divisor_core_transport.tex
Agent (sonnet): appendices/coderived_models.tex
Agent (sonnet): appendices/combinatorial_frontier.tex
Agent (sonnet): appendices/computational_tables.tex
Agent (sonnet): appendices/dg_shifted_factorization_bridge.tex
Agent (sonnet): appendices/dual_methodology.tex
Agent (sonnet): appendices/existence_criteria.tex
Agent (sonnet): appendices/general_relations.tex
Agent (sonnet): appendices/homotopy_transfer.tex
Agent (sonnet): appendices/koszul_reference.tex
Agent (sonnet): appendices/nilpotent_completion.tex
Agent (sonnet): appendices/notation_index.tex
Agent (sonnet): appendices/ordered_associative_chiral_kd.tex
Agent (sonnet): appendices/shifted_rtt_duality_orthogonal_coideals.tex
Agent (sonnet): appendices/spectral_higher_genus.tex
Agent (sonnet): appendices/spectral_sequences.tex
Agent (sonnet): appendices/subregular_hook_frontier.tex
Agent (sonnet): appendices/theta_functions.tex
Agent (sonnet): appendices/typeA_baxter_rees_theta.tex
Agent (sonnet): appendices/_sl2_yangian_insert.tex
```

## Tier 5: Volume II (launch sixth, SPLIT opus/sonnet)

### Opus — core proof chapters with dense mathematics:
```
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/foundations.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/factorization_swiss_cheese.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/axioms.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/locality.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/equivalence.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/pva-descent-repaired.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/bv-construction.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/concordance.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer_core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/brace.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/affine_half_space_bv.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/bv_ht_physics.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/physical_origins.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex
```

### Sonnet — frontier/extension scaffolding, mechanical compilations:
```
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/theory/pva-preview.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/theory/foundations_overclaims_resolved.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/fm3_planted_forest_synthesis.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/dg_shifted_factorization_bridge.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/conclusion.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/connections/thqg_*.tex (all thqg extension files)
```

### Vol II Examples (opus for proof-dense, sonnet for tables):
```
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex
Agent (opus): ~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/examples-computing.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/examples-complete-core.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex
```

### Vol II Frame + Appendices (sonnet):
```
Agent (sonnet): ~/chiral-bar-cobar-vol2/chapters/frame/preface.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/appendices/pva-expanded.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/appendices/pva-expanded-repaired.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/appendices/fm-proofs.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/appendices/orientations.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/appendices/brace-signs.tex
```

## Tier 6: Volume III — Calabi-Yau Quantum Groups (NEW)

### Opus — theory chapters with proofs and constructions:
```
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/introduction.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/cy_categories.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/hochschild_calculus.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex
```

### Opus — connection chapters (cross-volume bridges need full verification):
```
Agent (opus): ~/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex
Agent (opus): ~/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex
```

### Sonnet — examples and conventions:
```
Agent (sonnet): ~/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/chapters/examples/fukaya_categories.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/appendices/conventions.tex
```

---

## Tier 7: Working Notes, Standalone Papers, Archive Files

### Opus — standalone papers (self-contained mathematical arguments):
```
Agent (opus): ~/chiral-bar-cobar/standalone/shadow_towers.tex
Agent (opus): ~/chiral-bar-cobar/standalone/shadow_towers_v2.tex
Agent (opus): ~/chiral-bar-cobar/standalone/riccati.tex
Agent (opus): ~/chiral-bar-cobar/standalone/classification.tex
Agent (opus): ~/chiral-bar-cobar/standalone/computations.tex
```

### Sonnet — working notes (research logs, less formal):
```
Agent (sonnet): ~/calabi-yau-quantum-groups/working_notes.tex
Agent (sonnet): ~/chiral-bar-cobar-vol2/archive/platonic_introduction_volume_II.tex
```

### Vol III notes — opus for theory, sonnet for physics heuristics:
```
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_generalized_root_datum.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_cy2_cy3_fibration.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_coha_e1_sector.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_higgs_cy2_qvcg.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_e2_chiral_formalism.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_automorphic_shadow.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex
Agent (opus): ~/calabi-yau-quantum-groups/notes/theory_cy_to_chiral_construction.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_bps_root_multiplicities.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_topological_strings.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_3d_mirror.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_bv_brst_cy.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_sduality_langlands.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_wall_crossing_mc.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_4d_n2_hitchin.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_celestial_cy.tex
Agent (sonnet): ~/calabi-yau-quantum-groups/notes/physics_hitchin_langlands.tex
```

---

## File Count Summary

| Tier | Vol | Opus | Sonnet | Total |
|------|-----|------|--------|-------|
| 0 | I | 5 | 0 | 5 |
| 1 | I | 23 | 0 | 23 |
| 2 | I | 13 | 7 | 20 |
| 3 | I | 14 | 26 | 40 |
| 4 | I | 2 | 22 | 24 |
| 5 | II | 32 | 32 | 64 |
| 6 | III | 16 | 7 | 23 |
| 7 | All | 16 | 13 | 29 |
| **Total** | | **121** | **107** | **228** |

Opus handles 53% of files (all proof-dense, formula-heavy, or cross-reference-critical).
Sonnet handles 47% (tables, census, editorial, extensions, scaffolding, simple families).

---

## Rate-Limit Resilience

**Wave size**: 5-8 agents per wave. Wait for at least 3 completions before launching the next wave.

Track each agent's file and phase. If rate-limited:
1. Record `{file, phase_reached, last_line_swept}`
2. On reset, relaunch: `/chriss-ginzburg-rectify <file>` with note to start from interrupted phase
3. Never two agents on the same file

**Adaptive throttling**: If >50% of a wave hits 429, halve the next wave size. If 0% hit 429, increase by 2.

## Post-Swarm Verification (mechanical)

After all agents converge, merge worktrees and run:
```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 3
make fast                                              # Vol I
cd ~/chiral-bar-cobar-vol2 && make                     # Vol II
cd ~/calabi-yau-quantum-groups && pdflatex main.tex    # Vol III
cd ~/chiral-bar-cobar && make test                     # Tests
python3 scripts/generate_metadata.py                   # Census
```

Cross-volume AP5 check: for every formula changed by any agent, grep all three volumes.

---

## Post-Swarm Cross-Chapter Consistency Pass

Each `/chriss-ginzburg-rectify` agent runs the LINEAR BEILINSON RECTIFICATION LOOP internally: stepping through its chapter chunk-by-chunk (~100 lines), running a full audit-fortify-fix-reaudit convergence loop on each chunk before advancing. By the time an agent reports CONVERGED, every chunk of its chapter has been individually audited and rectified.

What chapter-level isolation CANNOT catch: inter-chapter inconsistencies introduced by independent worktree edits. Two agents may independently "fix" the same formula in different directions (AP5 across worktrees), or a scope tightening in `higher_genus_modular_koszul.tex` may contradict what the introduction agent wrote.

### Cross-Chapter Pass Protocol

After all chapter agents converge and worktrees are merged, launch ONE opus agent per volume:

```
Agent(description="Cross-chapter consistency Vol I", model="opus",
  prompt="CROSS-CHAPTER CONSISTENCY PASS on assembled Vol I.

  All chapter-level rectification has converged. Your job: catch INTER-CHAPTER
  inconsistencies from independent worktree edits. This is NOT a chapter-level
  rectification — that's done. This is a SEAM INSPECTION.

  Read the source files sequentially (preface → introduction → theory → examples
  → connections → appendices). At each chapter boundary and cross-reference site:

  1. FORMULA CONSISTENCY (AP5): Same formula in different files must be identical.
     Grep every formula that was likely edited. Flag divergences.
  2. CROSS-REFERENCE INTEGRITY: Every \\ref resolves. Every cited theorem's
     hypotheses match how it's used at the citation site.
  3. SCOPE CONSISTENCY (AP7, AP32): Introduction claims ≤ body chapter claims.
     Concordance status matches actual theorem status after rectification.
  4. CONVENTION CONSISTENCY: Signs, gradings, shifts uniform across files.
     Check against signs_and_shifts.tex.
  5. NARRATIVE SEAMS: Do chapter transitions read smoothly after independent
     rewrites? Chapter N's closing and chapter N+1's opening should connect.

  Fix issues. Grep all three volumes for variants. Build after every 3 fixes.

  If >5 findings cluster in one file: flag it for a second /chriss-ginzburg-rectify round.

  Build all three volumes. Run make test.")
```

Launch one per volume (3 total, parallel, opus).

### Full Convergence Criterion

The rectification programme is COMPLETE when:
1. All ~199 chapter agents have converged (each chunk's Beilinson loop converged)
2. All 3 cross-chapter passes have converged (zero inter-chapter inconsistencies)
3. All 3 volumes build clean (0 undefined refs, 0 undefined citations)
4. All tests pass (`make test`)
5. Census is consistent (`python3 scripts/generate_metadata.py`)
6. No chapter was flagged for a second round

If any chapter IS flagged, relaunch `/chriss-ginzburg-rectify` on it, then re-run the cross-chapter pass on that volume. Iterate until convergence.
