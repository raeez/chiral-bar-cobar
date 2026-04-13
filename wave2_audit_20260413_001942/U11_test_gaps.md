# U11_test_gaps (624s)

- [HIGH] compute/lib/__init__.py:1 — PROBLEM: The package initializer contains kernel logic but has no matching `compute/tests/test___init__.py`, and no current test imports it directly. FIX: add `compute/tests/test___init__.py` with direct imports and initializer-level assertions.
- [HIGH] compute/lib/euler_koszul_moments.py:1 — PROBLEM: This module has no matching `compute/tests/test_euler_koszul_moments.py`, and no current test imports it directly. FIX: add `compute/tests/test_euler_koszul_moments.py` with direct imports and module-scoped assertions.
- [HIGH] compute/lib/feynman_integral_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_feynman_integral_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_feynman_integral_engine.py` with direct imports and module-scoped assertions.
- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
- [HIGH] compute/lib/graph_complex_cohomology_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_graph_complex_cohomology_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_graph_complex_cohomology_engine.py` with direct imports and graph-complex cohomology assertions.
- [HIGH] compute/lib/lattice_genus2_theta.py:1 — PROBLEM: This module has no matching `compute/tests/test_lattice_genus2_theta.py`; the only current hit is a narrative mention in `test_theorem_genus2_sl3_partition_engine.py`, not an import. FIX: add `compute/tests/test_lattice_genus2_theta.py` with direct imports and theta-series assertions.
- [HIGH] compute/lib/mc4_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_mc4_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_mc4_diagnostic.py` with direct imports and diagnostic-state assertions.
- [HIGH] compute/lib/mc5_genus_geq2_strategies.py:1 — PROBLEM: This strategy module has no matching `compute/tests/test_mc5_genus_geq2_strategies.py`; `test_mc5_higher_genus.py` only names it in the docstring and does not import it. FIX: add `compute/tests/test_mc5_genus_geq2_strategies.py` with direct imports and strategy-level checks.
- [HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
- [HIGH] compute/lib/ope_corrected_sewing.py:1 — PROBLEM: This module has no matching `compute/tests/test_ope_corrected_sewing.py`, and no current test imports it directly. FIX: add `compute/tests/test_ope_corrected_sewing.py` with direct imports and sewing-correction assertions.
- [HIGH] compute/lib/poincare_duality_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_poincare_duality_engine.py`; `test_poincare_duality_bar_engine.py` targets a different module and only mentions this file in its header. FIX: add `compute/tests/test_poincare_duality_engine.py` with direct imports and engine-level Poincare-duality assertions.
- [HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
- [HIGH] compute/lib/w3_h2_sl3_decomposition_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_w3_h2_sl3_decomposition_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_h2_sl3_decomposition_engine.py` with direct imports and decomposition assertions.
- [HIGH] compute/lib/w3_miura_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_w3_miura_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_miura_diagnostic.py` with direct imports and Miura-diagnostic assertions.
- [HIGH] compute/lib/w4_primary_projection.py:1 — PROBLEM: This module has no matching `compute/tests/test_w4_primary_projection.py`, and no current test imports it directly. FIX: add `compute/tests/test_w4_primary_projection.py` with direct imports and primary-projection assertions.
- [MEDIUM] compute/lib/abjm_holographic_datum.py:1 — PROBLEM: No exact matching test file exists; ABJM-specific checks are buried in broader twisted-holography suites instead of `compute/tests/test_abjm_holographic_datum.py`. FIX: add `compute/tests/test_abjm_holographic_datum.py` and move the ABJM-only assertions out of `test_twisted_holography_comparison_engine.py`.
- [MEDIUM] compute/lib/alpha_g_simple_lie_verification_engine.py:1 — PROBLEM: The engine is tested only through the misnamed file `compute/tests/test_alpha_g_simple_lie_verification.py`, so the exact `test_<module>.py` contract is missing. FIX: rename `compute/tests/test_alpha_g_simple_lie_verification.py` to `compute/tests/test_alpha_g_simple_lie_verification_engine.py`.
- [MEDIUM] compute/lib/arithmetic_comparison_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_arithmetic_comparison.py`, but the exact matching file `compute/tests/test_arithmetic_comparison_test.py` is missing. FIX: rename `compute/tests/test_arithmetic_comparison.py` to `compute/tests/test_arithmetic_comparison_test.py`.
- [MEDIUM] compute/lib/bar_graph_complex_bridge_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bar_graph_complex_bridge.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bar_graph_complex_bridge.py` to `compute/tests/test_bar_graph_complex_bridge_engine.py`.
- [MEDIUM] compute/lib/bethe_tq_relation_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bethe_tq_relation.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bethe_tq_relation.py` to `compute/tests/test_bethe_tq_relation_engine.py`.
- [MEDIUM] compute/lib/bv_brst_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bv_brst_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bv_brst_purity.py` to `compute/tests/test_bv_brst_purity_engine.py`.
- [MEDIUM] compute/lib/cohft_dr_hierarchy_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_dr_hierarchy.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_dr_hierarchy.py` to `compute/tests/test_cohft_dr_hierarchy_engine.py`.
- [MEDIUM] compute/lib/cohft_givental_rmatrix_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_givental_rmatrix.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_givental_rmatrix.py` to `compute/tests/test_cohft_givental_rmatrix_engine.py`.
- [MEDIUM] compute/lib/cohft_string_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_string_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_string_genus2.py` to `compute/tests/test_cohft_string_genus2_engine.py`.
- [MEDIUM] compute/lib/cohft_toprec_string_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_toprec_string.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_toprec_string.py` to `compute/tests/test_cohft_toprec_string_engine.py`.
- [MEDIUM] compute/lib/cohft_virasoro_constraints_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_virasoro_constraints.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_virasoro_constraints.py` to `compute/tests/test_cohft_virasoro_constraints_engine.py`.
- [MEDIUM] compute/lib/coxeter_anomaly_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_coxeter_anomaly.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_coxeter_anomaly.py` to `compute/tests/test_coxeter_anomaly_test.py`.
- [MEDIUM] compute/lib/delta_fg_degree_pattern_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_delta_fg_degree_pattern.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_delta_fg_degree_pattern.py` to `compute/tests/test_delta_fg_degree_pattern_engine.py`.
- [MEDIUM] compute/lib/dmod_counterexample_search_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_counterexample_search.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_counterexample_search.py` to `compute/tests/test_dmod_counterexample_search_engine.py`.
- [MEDIUM] compute/lib/dmod_filtration_ss_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_filtration_ss.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_filtration_ss.py` to `compute/tests/test_dmod_filtration_ss_engine.py`.
- [MEDIUM] compute/lib/dmod_kl_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_kl_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_kl_purity.py` to `compute/tests/test_dmod_kl_purity_engine.py`.
- [MEDIUM] compute/lib/dmod_mixed_hodge_bar_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_mixed_hodge_bar.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_mixed_hodge_bar.py` to `compute/tests/test_dmod_mixed_hodge_bar_engine.py`.
- [MEDIUM] compute/lib/dmod_purity_char_variety_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_purity_char_variety.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_purity_char_variety.py` to `compute/tests/test_dmod_purity_char_variety_engine.py`.
- [MEDIUM] compute/lib/e8_lattice_bar.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_e8_lattice.py`. FIX: rename `compute/tests/test_e8_lattice.py` to `compute/tests/test_e8_lattice_bar.py`.
- [MEDIUM] compute/lib/formality_obstruction_loop4_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_formality_obstruction_loop4.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_formality_obstruction_loop4.py` to `compute/tests/test_formality_obstruction_loop4_engine.py`.
- [MEDIUM] compute/lib/graph_complex_orientation_database.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_graph_complex_orientation.py`. FIX: rename `compute/tests/test_graph_complex_orientation.py` to `compute/tests/test_graph_complex_orientation_database.py`.
- [MEDIUM] compute/lib/holographic_dmod_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_holographic_dmod_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_holographic_dmod_purity.py` to `compute/tests/test_holographic_dmod_purity_engine.py`.
- [MEDIUM] compute/lib/integrable_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_integrable_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_integrable_genus2.py` to `compute/tests/test_integrable_genus2_engine.py`.
- [MEDIUM] compute/lib/kac_chevalley_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_kac_chevalley.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_kac_chevalley.py` to `compute/tests/test_kac_chevalley_test.py`.
- [MEDIUM] compute/lib/lattice_genus2_universality_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_lattice_genus2_universality.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_lattice_genus2_universality.py` to `compute/tests/test_lattice_genus2_universality_engine.py`.
- [MEDIUM] compute/lib/mc4_stage4_resolution.py:1 — PROBLEM: No exact matching test file exists; the direct unit coverage lives in `compute/tests/test_mc4_defect_vanishing.py`. FIX: rename `compute/tests/test_mc4_defect_vanishing.py` to `compute/tests/test_mc4_stage4_resolution.py`.
- [MEDIUM] compute/lib/mc_crossing_theorem_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mc_crossing_theorem.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mc_crossing_theorem.py` to `compute/tests/test_mc_crossing_theorem_engine.py`.
- [MEDIUM] compute/lib/mg_genus2_clutching_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_genus2_clutching.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_genus2_clutching.py` to `compute/tests/test_mg_genus2_clutching_engine.py`.
- [MEDIUM] compute/lib/mg_harer_stability_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_harer_stability.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_harer_stability.py` to `compute/tests/test_mg_harer_stability_engine.py`.
- [MEDIUM] compute/lib/mg_kuranishi_parity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_kuranishi_parity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_kuranishi_parity.py` to `compute/tests/test_mg_kuranishi_parity_engine.py`.
- [MEDIUM] compute/lib/mg_tautological_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_tautological_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_tautological_purity.py` to `compute/tests/test_mg_tautological_purity_engine.py`.
- [MEDIUM] compute/lib/mg_w3_genus2_graph_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_w3_genus2_graph.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_w3_genus2_graph.py` to `compute/tests/test_mg_w3_genus2_graph_engine.py`.
- [MEDIUM] compute/lib/modular_periodicity_test.py:1 — PROBLEM: The dedicated coverage sits in `compute/tests/test_modular_periodicity_conjecture.py`, while `compute/tests/test_modular_periodicity.py` targets a different module. FIX: rename `compute/tests/test_modular_periodicity_conjecture.py` to `compute/tests/test_modular_periodicity_test.py`.
- [MEDIUM] compute/lib/multigen_universality_attack.py:1 — PROBLEM: The module is covered through the misnamed dedicated suite `compute/tests/test_multigen_universality_proof.py`, so the exact `test_<module>.py` file is still missing. FIX: rename `compute/tests/test_multigen_universality_proof.py` to `compute/tests/test_multigen_universality_attack.py`.
- [MEDIUM] compute/lib/n2_sca_chiral_bar_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_n2_sca_chiral_bar.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_n2_sca_chiral_bar.py` to `compute/tests/test_n2_sca_chiral_bar_engine.py`.
- [MEDIUM] compute/lib/n2_sca_chiral_bar_weight_graded_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_n2_sca_chiral_bar_weight_graded.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_n2_sca_chiral_bar_weight_graded.py` to `compute/tests/test_n2_sca_chiral_bar_weight_graded_engine.py`.
- [MEDIUM] compute/lib/niemeier_multichannel.py:1 — PROBLEM: No exact matching test file exists; `compute/tests/test_multichannel_shadow.py` mixes `niemeier_multichannel.py` assertions with a different module. FIX: add `compute/tests/test_niemeier_multichannel.py` and move the Niemeier-specific assertions out of `test_multichannel_shadow.py`.
- [MEDIUM] compute/lib/offdiag_newton_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_offdiag_newton.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_offdiag_newton.py` to `compute/tests/test_offdiag_newton_test.py`.
- [MEDIUM] compute/lib/operadic_koszul_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_operadic_koszul_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_operadic_koszul_genus2.py` to `compute/tests/test_operadic_koszul_genus2_engine.py`.
- [MEDIUM] compute/lib/ordered_trace_invariant_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_ordered_trace_invariant.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_ordered_trace_invariant.py` to `compute/tests/test_ordered_trace_invariant_engine.py`.
- [MEDIUM] compute/lib/rectangular_w_algebra_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_rectangular_w_algebra.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_rectangular_w_algebra.py` to `compute/tests/test_rectangular_w_algebra_engine.py`.
- [MEDIUM] compute/lib/sft_graph_complex_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_sft_graph_complex.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_sft_graph_complex.py` to `compute/tests/test_sft_graph_complex_engine.py`.
- [MEDIUM] compute/lib/siegel_eisenstein.py:1 — PROBLEM: No exact matching test file exists; coefficient and product checks are scattered across several Siegel and E8 suites instead of `compute/tests/test_siegel_eisenstein.py`. FIX: add `compute/tests/test_siegel_eisenstein.py` and move the direct module checks there.
- [MEDIUM] compute/lib/tautological_genus2_numerical_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_tautological_genus2_numerical.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_tautological_genus2_numerical.py` to `compute/tests/test_tautological_genus2_numerical_engine.py`.
- [MEDIUM] compute/lib/toroidal_bar.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_toroidal.py`. FIX: rename `compute/tests/test_toroidal.py` to `compute/tests/test_toroidal_bar.py`.
- [MEDIUM] compute/lib/vertex_algebra_extensions_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_vertex_algebra_extensions.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_vertex_algebra_extensions.py` to `compute/tests/test_vertex_algebra_extensions_engine.py`.
- [MEDIUM] compute/lib/w3_bar_extended.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_w3_extended.py`. FIX: rename `compute/tests/test_w3_extended.py` to `compute/tests/test_w3_bar_extended.py`.
- [MEDIUM] compute/lib/w4_ds_ope.py:1 — PROBLEM: No exact matching test file exists; direct `w4_ds_ope.py` assertions are scattered across multiple W4 suites and mixed with `w4_ds_ope_extraction.py`. FIX: add `compute/tests/test_w4_ds_ope.py` and move the direct Miura/Wick assertions there.
- [MEDIUM] compute/lib/w_algebra_transport_propagation.py:1 — PROBLEM: No exact matching test file exists; direct checks of this module are mixed into broader transpose and DS suites. FIX: add `compute/tests/test_w_algebra_transport_propagation.py` and move the direct module assertions there.
- [MEDIUM] compute/lib/wp_koszulness_definitive_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_wp_koszulness_definitive.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_wp_koszulness_definitive.py` to `compute/tests/test_wp_koszulness_definitive_engine.py`.

## Summary
Checked: 1325 | Findings: 65 | Verdict: FAIL


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d840a-fa35-7d40-a5eb-91fa51b7874d
--------
user
<task>
You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
Tear apart every weakness. Accept NOTHING at face value.
For EVERY finding, you MUST provide the EXACT FIX — not just the diagnosis.
Format: [SEVERITY] file:line — PROBLEM: ... FIX: ...
</task>

<grounding_rules>
Ground every claim in file contents you actually read. No guesses. No inferences presented as facts.
</grounding_rules>

<completeness_contract>
Exhaust the audit surface. After the first finding, dig deeper for second-order failures.
After the obvious issues, hunt for the SUBTLE ones that survive surface-level review.
</completeness_contract>

<verification_loop>
Re-verify each finding against actual file contents. Remove false positives.
</verification_loop>

<structured_output_contract>
Return findings as:
- [CRITICAL] file:line — PROBLEM: ... FIX: ...
- [HIGH] file:line — PROBLEM: ... FIX: ...
- [MEDIUM] file:line — PROBLEM: ... FIX: ...
- [LOW] file:line — PROBLEM: ... FIX: ...

End with:
## Summary
Checked: N | Findings: N | Verdict: PASS/FAIL
</structured_output_contract>


MISSION: UNFINISHED WORK AUDIT.

Find compute engines (compute/lib/*.py) without matching test files (compute/tests/test_*.py). Each missing test is a finding.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers



thinking
**Planning an audit task**

I need to address the user's request to audit unfinished work. Specifically, I need to locate compute engines in `compute/lib/*.py` without matching any test files from `compute/tests/test_*.py`. I’ll likely need to use tools for this, maybe the `deep-beilinson-audit` skill since it suits the task. I should also check if I need any additional reading or skills, like the `build-surface` or `claim-surface-sync`, though those might not be necessary. I should follow the guidelines carefully.
thinking
**Determining audit approach**

First, I should definitely use explorers to tackle this, as they're preferred for codebase questions. I could spawn an explorer agent to find the files in `compute/lib` and the matching tests. Alternatively, I might consider using shell commands, but explorers are typically the way to go. I need to inspect the repository structure carefully to ensure an exhaustive audit of `compute/lib/*.py` while excluding any `compute/tests/test_*.py`. I should clarify what "matching" means to get precise results. Frequent updates will help keep everything clear!
thinking
**Analyzing test file requirements**

The user wants me to identify the compute engines in `compute/lib/*.py` while excluding any matching test files in `compute/tests/test_*.py`. My first step is to establish what it means to be a "matching" file — it could be based on the module base name or similar functionality. I need to read through both lists carefully to determine which library files do not have a corresponding test file, like `foo.py` versus `test_foo.py`. I need to handle this thoughtfully!
codex
I’m auditing the compute surface specifically for `compute/lib/*.py` modules that lack a corresponding `compute/tests/test_*.py` file. I’ll read the audit skill, inventory both directories, and then verify each candidate against actual filenames before reporting only grounded findings.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

codex
I’ve fixed the audit surface to compute modules versus test coverage. Next I’m loading the required repo constitutive files, then I’ll inventory `compute/lib` and `compute/tests`, cross-check naming module by module, and re-read any edge cases before finalizing findings.
Plan update
Audit only the unfinished compute-work surface: `compute/lib/*.py` modules lacking corresponding `compute/tests/test_*.py` coverage files. Findings will be grounded in files actually read and verified against the live tree before reporting.
  → Read required audit context files and confirm repo conventions relevant to compute audits
  • Inventory compute engine modules and existing tests from the live tree
  • Match modules to tests, re-check edge cases, and isolate missing-test findings only
  • Return exhaustive findings in the requested severity format with exact fixes and summary
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2809 |
| Total tagged claims | 3615 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2809 |
 succeeded in 52ms:
# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
- high: **807**

thinking
**Examining compute engines**

The user mentioned computing engines without matching test files, and I'm thinking about including every Python file, even `__init__.py`. But typically, that’s not an engine, so I need to be grounded in the details. I should examine the list of files closely. I’m considering using a command like `rg --files compute/lib compute/tests` and maybe I could run some checks in parallel to make it more efficient.
codex
The constitutive files are loaded. I’m moving to the live audit surface now: exact module inventory, exact test inventory, then a module-by-module name match so the final list contains only verified missing-test cases.
exec
/bin/zsh -lc 'rg --files compute/tests' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg --files compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 1332

compute/lib/theorem_hca_pillar_a_engine.py
compute/lib/bc_euler_product_shadow_engine.py
compute/lib/beilinson_auditor.py
compute/lib/mv_positivity_sl3.py
compute/lib/genus_expansion.py
compute/lib/w3_wline_shadow_tower.py
compute/lib/w3_h5_verification.py
compute/lib/linf_bracket_engine.py
compute/lib/cy_mathieu_moonshine_engine.py
compute/lib/pixton_genus3_shadow_engine.py
compute/lib/moonshine_shadow_depth.py
compute/lib/bc_nc_distance_shadow_engine.py
compute/lib/pade_resolution.py
compute/lib/roelcke_selberg_decomposition.py
compute/lib/theorem_open_closed_rectification_engine.py
compute/lib/modular_forms_shadow_engine.py
compute/lib/bc_isomonodromic_shadow_engine.py
compute/lib/theorem_transport_transpose_sl4_engine.py
 succeeded in 53ms:
Total output lines: 1391

compute/tests/test_shadow_period_integral_engine.py
compute/tests/test_bc_topological_recursion_shadow_engine.py
compute/tests/test_pixton_planted_forest.py
compute/tests/test_bv_bar_class_c_engine.py
compute/tests/test_csft_from_bar.py
compute/tests/test_e8_genus2_hecke.py
compute/tests/test_discriminant_atlas_complete.py
compute/tests/test_bc_deformation_quantization_shadow_engine.py
compute/tests/test_matrix_rankin_selberg.py
compute/tests/test_rigid_oper_motives_engine.py
compute/tests/test_lagrangian_perfectness.py
compute/tests/test_genus4_stable_graphs.py
compute/tests/test_scattering_resonance.py
compute/tests/test_bar_tqft_state_sum_engine.py
compute/tests/test_w4_stage4_coefficients.py
compute/tests/test_conformal_bootstrap_shadow.py
compute/tests/test_gerstenhaber_sl2_bracket_engine.py
compute/tests/test_virasoro_ainfty_higher.py






thinking
**Evaluating test modules**

I need to find every module that doesn't have matching tests, and it's likely there are quite a few. I should aim for exhaustive findings, which could lead to hundreds of items. Yet, I need to keep the final answer between 50 to 70 lines according to the general instructions, while the user wants comprehensive results. I’ll need to figure out how to reconcile these requirements, maybe by compressing or summarizing essential information.
thinking
**Considering findings format**

I'm trying to figure out how to format my findings. If there are hundreds, the final output might be lengthy, but the instructions say to keep it under 50-70 lines to avoid overwhelming. The user has requested a list, but maybe I could also consider generating a report file and summarizing? However, they didn't specifically ask for a saved file. I need to decide on the best approach, especially after computing the exact count of missing tests.
thinking
**Determining line references**

I'm considering how to get exact line references for each finding by using the format file:line. Line one could suffice, especially since the user wants grounded evidence from the actual file contents, so I’m thinking about using `nl -ba file | sed -n '1,5p'` to access the first few lines of each missing candidate. Even though there are many files, it should be manageable. But since the final output shouldn't include content, just the file and line references, I need to ensure I've read them correctly.
thinking
**Deciding on test claims**

I'm considering whether simply listing the absence of matching tests would be sufficient or if I should check the compute/tests filenames for accuracy. It feels safer to verify their existence through the shell. I might need to read the first line of each matching test, but that’s unnecessary for missing tests. I also need to determine if modules named with `_test.py` or `_verification.py` should be counted as engines, even without tests, since the user specifically requested them from compute/lib.
thinking
**Analyzing module tests**

I could check line 1 of the module to see if it has a `main` or classes, but that might be overwhelming. Maybe there aren’t too many missing tests since many already exist. I think I should run a shell script to count them. Since the user asked for matching test files, I need to focus on exact matches like `test_<module_base>.py` and ignore non-matching ones. I need to establish a rule for exact basename matches. There could be others with similar names that are also missing.
thinking
**Computing exact matches**

I think I can mention some examples, but the focus is really on finding only the missing exact matches. The solution would involve correcting the file path to reflect those exact matches. To compute the exact list, I might want to exclude `__init__.py` and any files in `_archive`, limiting my search to a maximum depth of 1. I could use a shell script with `find -maxdepth 1`, possibly combined with a `while` loop to output the count and candidates.
codex
The raw tree dump was too noisy because `rg --files` included archived subdirectories. I’m tightening the scope to the literal surface the user named, `compute/lib/*.py`, and matching it only against exact sibling test names of the form `compute/tests/test_<module>.py`.
exec
/bin/zsh -lc 'tmp_lib=$(mktemp); tmp_tests=$(mktemp); find compute/lib -maxdepth 1 -type f -name '"'*.py' | sort > \""'$tmp_lib"; find compute/tests -maxdepth 1 -type f -name '"'test_*.py' | sort > \""'$tmp_tests"; printf '"'LIB_COUNT '; wc -l < \""'$tmp_lib"; printf '"'TEST_COUNT '; wc -l < \""'$tmp_tests"; printf '"'MISSING_COUNT '; while IFS= read -r lib; do base="'$(basename "$lib" .py); test="compute/tests/test_${base}.py"; [ -f "$test" ] || printf '"'%s\\n' \""'$lib"; done < "$tmp_lib" | tee /tmp/missing_compute_tests.txt | wc -l; printf '"'\\nFIRST_200_MISSING\\n'; sed -n '1,200p' /tmp/missing_compute_tests.txt; rm -f \""'$tmp_lib" "$tmp_tests"' in /Users/raeez/chiral-bar-cobar succeeded in 1.72s:
      65

FIRST_200_MISSING
compute/lib/__init__.py
compute/lib/abjm_holographic_datum.py
compute/lib/alpha_g_simple_lie_verification_engine.py
compute/lib/arithmetic_comparison_test.py
compute/lib/bar_graph_complex_bridge_engine.py
compute/lib/bethe_tq_relation_engine.py
compute/lib/bv_brst_purity_engine.py
compute/lib/cohft_dr_hierarchy_engine.py
compute/lib/cohft_givental_rmatrix_engine.py
compute/lib/cohft_string_genus2_engine.py
compute/lib/cohft_toprec_string_engine.py
compute/lib/cohft_virasoro_constraints_engine.py
compute/lib/coxeter_anomaly_test.py
compute/lib/delta_fg_degree_pattern_engine.py
compute/lib/dmod_counterexample_search_engine.py
compute/lib/dmod_filtration_ss_engine.py
compute/lib/dmod_kl_purity_engine.py





thinking
**Evaluating compute engines**

I need to figure out if `__init__.py` should be included in the count, so I might need to inspect its content. There are also files like `*_test.py`, which could be in the lib directory. The user mentioned compute engines, so it's important to clarify if files like `arithmetic_comparison_test.py` are tests or actual engines. I should determine the expected scope based on actual content, treating `compute/lib/*.py` as compute engines, though care is needed with files named `_test.py`.
thinking
**Considering unfinished work audit**

The user wants an audit for unfinished work, which likely means identifying any module without exact test file counts. I think I might include `_test.py` files, but I should probably exclude `__init__.py` since it’s not an engine. However, the user might want it because of the literal glob pattern. I need to inspect `__init__.py` for clarity. It seems there may be some non-exact test names that cover modules like `dmod_purity_char_variety_engine.py`, so it’s crucial to focus on finding exact matches for file names, and maybe renaming existing tests could fix any discrepancies.
thinking
**Seeking exact fixes for tests**

I need to examine cases where there are similar tests with non-matching names. The user specifically asked for an exact fix, not just a diagnosis. It’s important to identify any modules with existing tests that don’t precisely match the expected test file names. I think this entails not just finding gaps but also suggesting specific renames or adjustments to ensure everything aligns properly. This will help address the user's request more effectively.
thinking
**Identifying missing tests**

I need to determine if each missing module has near-match tests. If it does, the solution might be to rename `test_x.py` to `test_x_engine.py` or add alias coverage. If there aren't near-matches, I’ll create a new test file. I should compute near-match mappings, especially for modules ending in `_engine.py`, and check if tests exist without the `_engine` suffix. I'll systematically inspect all 65 modules to identify any potential near matches.
thinking
**Generating file names**

The final fix should include renaming any existing near-match tests. First, I’ll need the actual file names to do this accurately. To generate the necessary mappings, I can use a shell script. This should help me identify potential files that need to be renamed, making sure nothing is missed in the process. I’m working to ensure everything aligns correctly so I can present a comprehensive solution for the user.
codex
I’ve reduced the literal missing set to 65 files. Before I report anything, I’m checking the second-order cases the user explicitly asked me not to miss: modules that lack an exact `test_<module>.py` but already have a near-match test under a different basename, because those need a rename fix, not a vague “add tests” placeholder.
exec
/bin/zsh -lc 'while IFS= read -r lib; do base=$(basename "$lib" .py); stem_engine=${base%_engine}; stem_test=${base%_test}; printf '"'%s|' \""'$lib"; for cand in "compute/tests/test_${stem_engine}.py" "compute/tests/test_${stem_test}.py"; do [ -f "$cand" ] && printf '"'%s;' \""'$cand"; done; printf '"'\\n'; done < /tmp/missing_compute_tests.txt" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
compute/lib/w4_primary_projection.py|
compute/lib/w_algebra_transport_propagation.py|
compute/lib/wp_koszulness_definitive_engine.py|compute/tests/test_wp_koszulness_definitive.py;


thinking
**Inspecting near-match tests**

It sounds like I need to look closely at the near-match tests. First, I should inspect the first line of each candidate file to identify any missing candidates. I might script a read operation to check these lines. I also need to verify that the tests target the same module by examining their import statements — I can’t just assume near-match names correspond. A simple script could helps me handle this by checking each near-match pair and printing essential details, like function definitions and module paths.
thinking
**Gathering near-match evidence**

I’m thinking about using `rg -n "<base>" testfile` to look for strong evidence of near-match pairs. If I find a match, that’s a good sign; if not, it might indicate differences. There are about 42 near-match pairs, and I hope to keep the output manageable and concise. I'll also gather mappings and check if the candidate tests import the module correctly, ensuring to read the actual file contents instead of just filenames. A script will help streamline this process.
exec
/bin/zsh -lc "while IFS='|' read -r lib matches; do [ -n \""'$matches" ] || continue; base=$(basename "$lib" .py); test=${matches%;}; printf '"'LIB %s\\n' \""'$lib"; sed -n '"'1,5p' \""'$lib"; printf '"'TEST %s\\n' \""'$test"; rg -n "$base|from compute'"\\.lib\\.|import compute\\.lib\\.|from compute\\.lib import|import compute\\.lib\" \""'$test" || true; printf '"'---\\n'; done < <(while IFS= read -r lib; do base="'$(basename "$lib" .py); stem_engine=${base%_engine}; stem_test=${base%_test}; printf '"'%s|' \""'$lib"; for cand in "compute/tests/test_${stem_engine}.py" "compute/tests/test_${stem_test}.py"; do [ -f "$cand" ] && printf '"'%s;' \""'$cand"; done; printf '"'\\n'; done < /tmp/missing_compute_tests.txt)" in /Users/raeez/chiral-bar-cobar succeeded in 173ms:
LIB compute/lib/dmod_mixed_hodge_bar_engine.py
r"""D-module purity and mixed Hodge structure on the bar complex.

MATHEMATICAL CONTEXT:

The bar complex B(A) = bigoplus_n (s^{-1}A_+)^{otimes n} carries a WEIGHT
TEST compute/tests/test_dmod_mixed_hodge_bar.py
1:"""Tests for dmod_mixed_hodge_bar_engine.py.
29:from compute.lib.dmod_mixed_hodge_bar_engine import (
846:        from compute.lib.dmod_mixed_hodge_bar_engine import ce_rank_koszulness_signal
---
LIB compute/lib/dmod_purity_char_variety_engine.py
"""D-module purity and characteristic variety engine.

Computes characteristic varieties Ch(FH_X(A)) of factorization homology
D-modules for chiral algebras on curves, and verifies the Lagrangian
(purity) condition from thm:koszul-equivalences-meta item (xii).
TEST compute/tests/test_dmod_purity_char_variety.py
1:"""Tests for compute/lib/dmod_purity_char_variety_engine.py.
34:from compute.lib.dmod_purity_char_variety_engine import (
exec
/bin/zsh -lc "while IFS='|' read -r lib matches; do [ -z \""'$matches" ] || continue; printf '"'LIB %s\\n' \""'$lib"; sed -n '"'1,5p' \""'$lib"; printf '"'---\\n'; done < <(while IFS= read -r lib; do base="'$(basename "$lib" .py); stem_engine=${base%_engine}; stem_test=${base%_test}; printf '"'%s|' \""'$lib"; for cand in "compute/tests/test_${stem_engine}.py" "compute/tests/test_${stem_test}.py"; do [ -f "$cand" ] && printf '"'%s;' \""'$cand"; done; printf '"'\\n'; done < /tmp/missing_compute_tests.txt)" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
"""W_3 Miura diagnostic: minimal test bed for the OPE extraction pipeline.

Computes the W_3 structure constant C_333^2 from the sl_3 quantum Miura
transformation with 2 free bosons and compares against the exact
Zamolodchikov bootstrap result:
---
LIB compute/lib/w4_ds_ope.py
"""W_4 DS OPE coefficient extraction via Miura transform.

Fills structural gap H3: Extract the 4 free OPE coefficients from the
principal Drinfeld-Sokolov W_4 algebra for MC4 verification.

---
LIB compute/lib/w4_primary_projection.py
"""BPZ primary projection for W_4 Miura generators.

The raw Miura output W4_raw is NOT a primary field — it contains
T-descendant (d²T) and Λ-composite (:TT: - 3/10 d²T) contamination.

---





thinking
**Inspecting modules and tests**

I need to check each missing module to see if `__init__.py` contains any logic. It turns out it does, so it could count as an engine. We might need to include it since it isn’t just empty. However, matching test `test___init__.py` feels a bit off. But given the user's insistence on matching tests, I think I should add `compute/tests/test___init__.py`. Alternatively, moving the logic to a named module could be a better fix. It’s essential to determine how to proceed, and I believe we should classify the severity as medium for this unfinished work.
thinking
**Assessing test severity**

I'm considering whether to assign a "HIGH" severity for foundational package initializers or core engines. The user’s focus is on missing test audits, but I think severity could depend on the module's role. I see "HIGH" applying to core modules or those claiming completeness without tests. For instance, the docstring in `__init__.py` states it's for the computational kernel, suggesting "HIGH." On the other hand, `mc_crossing_theorem_engine.py` has some coverage, possibly making it "MEDIUM" instead. The challenge here is the missing exact matching file rather than a lack of coverage.
thinking
**Categorizing test severity**

I can assign severity based on the presence of nearby test coverage. A "HIGH" severity would apply if there’s no exact match and no nearby test, particularly for modules claiming completeness or foundational significance in their docstrings. If there's no exact match but a near-match test imports the module, that could be "MEDIUM," as it's more about naming or coverage drift than total absence. For "LOW," perhaps the `_test.py` modules have near-match tests, indicating findings, but they aren't complete.
thinking
**Analyzing module tests**

The user wants a harsher approach, possibly suggesting `MEDIUM` or `LOW` severity instead of `HIGH` unless it’s foundational. I need to compute line numbers accurately. Each file starts at line 1 with a docstring, so I’ll focus on line 1 for exact references. I'll also look for `__init__.py` and renaming paths for tests. It’s vital to check for existing tests that might cover functionality under different module names. The user requires precise matching test files, not just any references, so I'll need to investigate naming drift too.
thinking
**Searching for module references**

I need to search all 65 basenames across the compute and tests directories to see where they’re referenced. This is important for determining how to fix any issues. Even if some modules lack near-match files, there could still be broader integration tests that import them. To be thorough, I’ll use `rg` to check each basename. It’ll be helpful to output whether each is referenced elsewhere, which will guide my approach for the fixes. I’ll also script the counting of matching test references.
codex
I’ve separated total-absence cases from naming-drift cases. One more pass is necessary to avoid false positives: some modules without a matching filename may still be imported by broader integration tests, and those need a different fix than modules with zero test references anywhere.
exec
/bin/zsh -lc 'while IFS= read -r lib; do base=$(basename "$lib" .py); printf '"'%s\\n' \""'$lib"; rg -l "$base" compute/tests || true; printf '"'---\\n'; done < /tmp/missing_compute_tests.txt" in /Users/raeez/chiral-bar-cobar succeeded in 1.16s:
compute/tests/test_rectification_kappa_cross_engine.py
compute/tests/test_arithmetic_comparison.py
---
compute/lib/bar_graph_complex_bridge_engine.py
compute/tests/test_bar_graph_complex_bridge.py
---
compute/lib/bethe_tq_relation_engine.py
compute/tests/test_bethe_tq_relation.py
---
compute/lib/bv_brst_purity_engine.py
compute/tests/test_bv_brst_purity.py
---
compute/lib/cohft_dr_hierarchy_engine.py
compute/tests/test_cohft_dr_hierarchy.py
---
compute/lib/cohft_givental_rmatrix_engine.py
compute/tests/test_cohft_givental_rmatrix.py
---
compute/lib/cohft_string_genus2_engine.py
compute/tests/test_cohft_string_genus2.py



thinking
**Deciding on test fixes**

I need to figure out whether to create a dedicated exact-match test or rename a broader test designed for related results. If the broader test is meant as the module's direct unit test, maybe renaming it is acceptable; however, the user has specifically asked for an exact fix.

I could compute the 65 findings and suggest either renaming or adding a dedicated test, depending on whether the current file imports the module and whether specific assertions exist in the broader tests.
thinking
**Verifying the rename fix**

It seems plausible to go ahead with renaming the fix. I might need to double-check by reading the first line of the test file, just to be sure. Although we already have the import lines, which might be sufficient for what I need. It’s good to cross-verify, though—can’t be too careful! I want to ensure everything is accurate for the user’s request.
thinking
**Identifying modules for testing**

I'm thinking about identifying modules without near-match tests but with some test references. I estimate there might be around 15 of those, and I'll need to inspect them more closely. Also, I want to look at modules that don’t have any test references at all. It seems essential to compute their categories and maybe counts. I'll consider using a script for this task to streamline everything. Let's dive in!
exec
/bin/zsh -lc 'while IFS= read -r lib; do base=$(basename "$lib" .py); exact="compute/tests/test_${base}.py"; stem_engine=${base%_engine}; stem_test=${base%_test}; near='"''; for cand in \"compute/tests/test_"'${stem_engine}.py" "compute/tests/test_${stem_test}.py"; do [ -f "$cand" ] && near="$near$cand;"; done; refs=$(rg -l "$base" compute/tests | tr '"'\\n' ';'); printf '%s|near=%s|refs=%s\\n' \""'$lib" "$near" "$refs"; done < /tmp/missing_compute_tests.txt' in /Users/raeez/chiral-bar-cobar succeeded in 1.16s:
compute/lib/bethe_tq_relation_engine.py|near=compute/tests/test_bethe_tq_relation.py;|refs=compute/tests/test_bethe_tq_relation.py;
compute/lib/bv_brst_purity_engine.py|near=compute/tests/test_bv_brst_purity.py;|refs=compute/tests/test_bv_brst_purity.py;
compute/lib/cohft_dr_hierarchy_engine.py|near=compute/tests/test_cohft_dr_hierarchy.py;|refs=compute/tests/test_cohft_dr_hierarchy.py;
compute/lib/cohft_givental_rmatrix_engine.py|near=compute/tests/test_cohft_givental_rmatrix.py;|refs=compute/tests/test_cohft_givental_rmatrix.py;
compute/lib/cohft_string_genus2_engine.py|near=compute/tests/test_cohft_string_genus2.py;|refs=compute/tests/test_cohft_string_genus2.py;
compute/lib/cohft_toprec_string_engine.py|near=compute/tests/test_cohft_toprec_string.py;|refs=compute/tests/test_cohft_toprec_string.py;
compute/lib/cohft_virasoro_constraints_engine.py|near=compute/tests/test_cohft_virasoro_constraints.py;|refs=compute/tests/test_cohft_virasoro_constraints.py;
compute/lib/coxeter_anomaly_test.py|near=compute/tests/test_coxeter_anomaly.py;|refs=compute/tests/test_coxeter_anomaly.py;
compute/lib/delta_fg_degree_pattern_engine.py|near=compute/tests/test_delta_fg_degree_pattern.py;|refs=compute/tests/test_delta_fg_degree_pattern.py;
compute/lib/dmod_counterexample_search_engine.py|near=compute/tests/test_dmod_counterexample_search.py;|refs=compute/tests/test_dmod_counterexample_search.py;
compute/lib/dmod_filtration_ss_engine.py|near=compute/tests/test_dmod_filtration_ss.py;|refs=compute/tests/test_dmod_filtration_ss.py;
compute/lib/dmod_kl_purity_engine.py|near=compute/tests/test_dmod_kl_purity.py;|refs=compute/tests/test_dmod_kl_purity.py;
compute/lib/dmod_mixed_hodge_bar_engine.py|near=compute/tests/test_dmod_mixed_hodge_bar.py;|refs=compute/tests/test_dmod_mixed_hodge_bar.py;
compute/lib/dmod_purity_char_variety_engine.py|near=compute/tests/test_dmod_purity_char_variety.py;|refs=compute/tests/test_dmod_purity_char_variety.py;
compute/lib/e8_lattice_bar.py|near=|refs=compute/tests/test_bar_cohomology_lattice_explicit_engine.py;compute/tests/test_master_integration.py;compute/tests/test_lattice_instanton_bar.py;compute/tests/test_extended_families.py;compute/tests/test_e8_lattice.py;
compute/lib/euler_koszul_moments.py|near=|refs=
compute/lib/feynman_integral_engine.py|near=|refs=
compute/lib/formality_obstruction_loop4_engine.py|near=compute/tests/test_formality_obstruction_loop4.py;|refs=compute/tests/test_formality_obstruction_loop4.py;
compute/lib/genus1_arithmetic_shadow.py|near=|refs=
compute/lib/graph_complex_cohomology_engine.py|near=|refs=


thinking
**Inspecting modules for fixes**

I think I need to inspect broader reference lines for modules that don’t have near-match tests but do have references. It might help to mention splitting from those files first, yet looking at the initial reference lines seems better. There are specific modules, like init.py and various others, without near-match tests but still have references. Also, I'll check if near-match tests mistakenly import incorrect modules, like `test_modular_periodicity.py` importing the wrong one. It's possible other near-match tests could also be failing.
thinking
**Verifying near-match pairs**

I need to check all the near-match pairs to see if `rg -n "$base"` yields results in the test files. The previous output listed all tests and their corresponding `rg` results with line numbers. Except for `test_modular_periodicity.py`, did each test include the exact base string? I noticed `test_integrable_genus2.py` did not include it; instead, it referenced `compute.lib.integrable_genus2_engine`. It seems modular_periodicity_test is the anomaly, so I'll also look into other tests, like `test_formality_obstruction_loop4.py`, and broaden the reference lines for those without near matches.
codex
I’ve isolated the genuinely tricky drift cases. These are modules with no exact test file but some scattered test references elsewhere, plus one case where a near-match filename exists but targets a different module entirely. I’m reading those cross-references now so the fixes name the right destination file instead of hand-waving.
exec
/bin/zsh -lc "for base in __init__ abjm_holographic_datum e8_lattice_bar graph_complex_orientation_database lattice_genus2_theta mc4_stage4_resolution mc5_genus_geq2_strategies modular_bootstrap_shadow modular_periodicity_test multigen_universality_attack niemeier_multichannel poincare_duality_engine siegel_eisenstein toroidal_bar w3_bar_extended w4_ds_ope w_algebra_transport_propagation; do printf 'BASE %s\\n' \""'$base"; rg -n "$base" compute/tests || true; printf '"'---\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 236ms:
---
BASE mc5_genus_geq2_strategies
compute/tests/test_mc5_higher_genus.py:7:  test_mc5_genus_geq2_strategies.py
---
BASE modular_bootstrap_shadow
compute/tests/test_conformal_bootstrap_mc_engine.py:64:    modular_bootstrap_shadow_verification,
compute/tests/test_conformal_bootstrap_mc_engine.py:472:        data = modular_bootstrap_shadow_verification(Rational(1))
compute/tests/test_conformal_bootstrap_mc_engine.py:479:        data = modular_bootstrap_shadow_verification(Rational(24))
compute/tests/test_conformal_bootstrap_mc_engine.py:485:            data = modular_bootstrap_shadow_verification(c_val)
compute/tests/test_conformal_bootstrap_mc_engine.py:491:            data = modular_bootstrap_shadow_verification(c_val)
---
BASE modular_periodicity_test
compute/tests/test_modular_periodicity_conjecture.py:29:from compute.lib.modular_periodicity_test import (
---
BASE multigen_universality_attack
compute/tests/test_multigen_universality_proof.py:40:from compute.lib.multigen_universality_attack import (
---
BASE niemeier_multichannel
compute/tests/test_multichannel_shadow.py:37:from compute.lib.niemeier_multichannel import (
compute/tests/test_multichannel_shadow.py:38:    niemeier_multichannel_atlas,

thinking
**Analyzing module coverage**

I'm looking into `lattice_genus2_theta`, and it seems the only relevant part is a mention in the docstring on line 15, which means there's no import. Similarly, `poincare_duality_engine.py` only matches a comment line in `test_poincare_duality_bar_engine.py`, showing zero direct coverage too. I think I should classify them as high-priority. For `modular_bootstrap_shadow.py`, I suspect test functions reference `modular_bootstrap_shadow_verification`. I need to check import lines in `test_conformal_bootstrap_mc_engine.py` to confirm. Also, `__init__.py` matches false positives due to method names and comments, indicating zero coverage overall.
exec
/bin/zsh -lc "for base in __init__ abjm_holographic_datum e8_lattice_bar graph_complex_orientation_database lattice_genus2_theta mc4_stage4_resolution mc5_genus_geq2_strategies modular_bootstrap_shadow modular_periodicity_test multigen_universality_attack niemeier_multichannel poincare_duality_engine siegel_eisenstein toroidal_bar w3_bar_extended w4_ds_ope w_algebra_transport_propagation; do printf 'BASE %s\\n' \""'$base"; rg -n "from .*${base}|import .*${base}" compute/tests || true; printf '"'---\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 248ms:
compute/tests/test_bottleneck_bar_cobar_curved.py:59:from compute.lib.mc4_stage4_resolution import (
compute/tests/test_mc4_defect_vanishing.py:25:from compute.lib.mc4_stage4_resolution import verify_stage4_defect_vanishing, count_vanishing_defects
---
BASE mc5_genus_geq2_strategies
---
BASE modular_bootstrap_shadow
---
BASE modular_periodicity_test
compute/tests/test_modular_periodicity_conjecture.py:29:from compute.lib.modular_periodicity_test import (
---
BASE multigen_universality_attack
compute/tests/test_multigen_universality_proof.py:40:from compute.lib.multigen_universality_attack import (
---
BASE niemeier_multichannel
compute/tests/test_multichannel_shadow.py:37:from compute.lib.niemeier_multichannel import (
---
BASE poincare_duality_engine
---
BASE siegel_eisenstein
compute/tests/test_leech_chi12_projection.py:17:from compute.lib.siegel_eisenstein import (
exec
/bin/zsh -lc "sed -n '1,80p' compute/tests/test_poincare_duality_bar_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' compute/tests/test_mc5_higher_genus.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' compute/tests/test_conformal_bootstrap_mc_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
"""Unified test suite for MC5 higher-genus bridge: BV/BRST = bar at g >= 2.

Consolidates tests from:
  test_mc5_frontier_modules.py
  test_mc5_genus2_redteam.py
  test_mc5_genus2_defense.py
  test_mc5_genus_geq2_strategies.py

All tests compute real mathematics -- no string-checking tests.
All arithmetic is exact (sympy.Rational).

Organization:
  I.   Arakelov-Bar structure (theta chars, prime form, Arnold defect, Hodge)
  II.  Clutching induction (sewing, degeneration, induction tower)
  III. Universality defense (kappa uniqueness, antisymmetry, Schur)
  IV.  Convergence and A-hat genus (Bernoulli, generating function, radius)
  V.   Cross-family universality (F_g ratios, complementarity, spot checks)
  VI.  Proof strategies (clutching, excision, Schottky, TFT, deformation)
  VII. Full defense battery and quantitative probes
"""
 succeeded in 52ms:
r"""Tests for the conformal bootstrap as a projection of the MC equation.

Verifies:
  1. MC equation at (0,4) = crossing equation for 4-point functions
  2. Q^contact = 10/[c(5c+22)] via three independent paths
  3. Ising model (c=1/2): MC predictions vs exact BPZ results
  4. Free boson (c=1): Wick contraction and crossing symmetry
  5. Hellerman bound Delta <= c/12 + O(1) from kappa = c/2
  6. Genus-1 MC = torus partition function constraint
  7. Modular bootstrap compatibility with shadow tower
  8. Cardy formula from the genus-1 shadow
  9. Shadow tower gap bounds
 10. Cross-family landscape scan

AP compliance:
  - AP10: Every numerical result verified by 2+ independent paths.
  - AP1: kappa(Vir_c) = c/2 verified independently.
  - AP24: Virasoro complementarity sum checked.
  - AP38: All numerical values derived from first principles.
"""
 succeeded in 52ms:
"""Tests for poincare_duality_bar_engine: Poincare duality for the bar complex
at genus g.

Verification structure (40+ tests):

I.    Genus 0: sl_2 explicit bar cohomology dimensions (Riordan correction)
II.   Genus 0: Koszul-dual CE side and duality offset
III.  Genus 1: Heisenberg curvature and torus partition function
IV.   Genus 1: scalar-shadow PD identity F_1(H) + F_1(H^!) = 0
V.    Genus g: Mumford / Serre duality on the Hodge bundle
VI.   Genus g: scalar PD identity for standard families (multi-path)
VII.  Character rationality and spectral radius
VIII. Euler-characteristic generating function (A-hat consistency)
IX.   DR cycle / Pixton: PD sign, involution compatibility
X.    Ayala-Francis: scalar PD for KM, free fields, AP24 Virasoro
XI.   Landscape table cross-checks
XII.  Top-level summary (all seven tasks as one marker each)

Ground truth cross-references:
  chapters/theory/poincare_duality.tex         (thm:bar-computes-dual)




thinking
**Assessing test coverage issues**

I'm realizing that `mc5_genus_geq2_strategies.py` isn't imported, which means there's a lack of coverage since the relevant tests are targeting something else. It also seems that `poincare_duality_engine.py` isn't tested, as the focus is on a different module. I need to check `modular_bootstrap_shadow.py` too, since it looks like it's not imported. We really should ensure that all modules are correctly referenced and covered in tests. This could apply to other modules with similar issues as well.
thinking
**Identifying test coverage gaps**

I'm looking at some modules that have near matches but may not have the correct targets or imports. I've already checked the first five lines of these modules, which is a good start. I might mention that the problem could stem from the docstring or test drift. I need to create a detailed findings list with categories and fixes, including around 65 lines. A report file could help check counts, and I can use a shell script to format the output by category. The severity for categories would also need to be assigned manually.
thinking
**Classifying test coverage modules**

I'm identifying modules that fall into the `[MEDIUM]` category. These modules don’t have an exact-match test file, but they do have broader or misnamed test files that import them. This means some coverage exists, but we’re missing a dedicated matching test file. The solution would be to rename or split these into distinct files. There might also be a `[LOW]` severity for `__init__.py`, which I should note for further action.
thinking
**Classifying theorem coverage**

I'm considering classifying foundational theorem or engine modules with zero coverage as HIGH and others with broad or misnamed coverage as MEDIUM. I don't think I'll classify any as LOW or CRITICAL because the audit surface consists of unfinished test files, not false theorems. I might need to count categories and programmatically determine actual import coverage using pattern matching. Also, I should note that `arithmetic_comparison_test.py` is a near match but imports the module exactly, which seems like it fits in MEDIUM. Would the user expect CRITICAL or HIGH? That might be harsh.
exec
/bin/zsh -lc 'while IFS= read -r lib; do base=$(basename "$lib" .py); import_refs=$(rg -l "from .*${base}|import .*${base}" compute/tests | tr '"'\\n' ';'); any_refs="'$(rg -l "$base" compute/tests | tr '"'\\n' ';'); printf '%s|imports=%s|refs=%s\\n' \""'$lib" "$import_refs" "$any_refs"; done < /tmp/missing_compute_tests.txt' in /Users/raeez/chiral-bar-cobar succeeded in 2.29s:
compute/lib/alpha_g_simple_lie_verification_engine.py|imports=compute/tests/test_alpha_g_simple_lie_verification.py;|refs=compute/tests/test_alpha_g_simple_lie_verification.py;
compute/lib/arithmetic_comparison_test.py|imports=compute/tests/test_rectification_kappa_cross_engine.py;compute/tests/test_arithmetic_comparison.py;|refs=compute/tests/test_rectification_kappa_cross_engine.py;compute/tests/test_arithmetic_comparison.py;
compute/lib/bar_graph_complex_bridge_engine.py|imports=compute/tests/test_bar_graph_complex_bridge.py;|refs=compute/tests/test_bar_graph_complex_bridge.py;
compute/lib/bethe_tq_relation_engine.py|imports=compute/tests/test_bethe_tq_relation.py;|refs=compute/tests/test_bethe_tq_relation.py;
compute/lib/bv_brst_purity_engine.py|imports=compute/tests/test_bv_brst_purity.py;|refs=compute/tests/test_bv_brst_purity.py;
compute/lib/cohft_dr_hierarchy_engine.py|imports=compute/tests/test_cohft_dr_hierarchy.py;|refs=compute/tests/test_cohft_dr_hierarchy.py;
compute/lib/cohft_givental_rmatrix_engine.py|imports=compute/tests/test_cohft_givental_rmatrix.py;|refs=compute/tests/test_cohft_givental_rmatrix.py;
compute/lib/cohft_string_genus2_engine.py|imports=compute/tests/test_cohft_string_genus2.py;|refs=compute/tests/test_cohft_string_genus2.py;
compute/lib/cohft_toprec_string_engine.py|imports=compute/tests/test_cohft_toprec_string.py;|refs=compute/tests/test_cohft_toprec_string.py;
compute/lib/cohft_virasoro_constraints_engine.py|imports=compute/tests/test_cohft_virasoro_constraints.py;|refs=compute/tests/test_cohft_virasoro_constraints.py;
compute/lib/coxeter_anomaly_test.py|imports=compute/tests/test_coxeter_anomaly.py;|refs=compute/tests/test_coxeter_anomaly.py;
compute/lib/delta_fg_degree_pattern_engine.py|imports=compute/tests/test_delta_fg_degree_pattern.py;|refs=compute/tests/test_delta_fg_degree_pattern.py;
compute/lib/dmod_counterexample_search_engine.py|imports=compute/tests/test_dmod_counterexample_search.py;|refs=compute/tests/test_dmod_counterexample_search.py;
compute/lib/dmod_filtration_ss_engine.py|imports=compute/tests/test_dmod_filtration_ss.py;|refs=compute/tests/test_dmod_filtration_ss.py;
compute/lib/dmod_kl_purity_engine.py|imports=compute/tests/test_dmod_kl_purity.py;|refs=compute/tests/test_dmod_kl_purity.py;
compute/lib/dmod_mixed_hodge_bar_engine.py|imports=compute/tests/test_dmod_mixed_hodge_bar.py;|refs=compute/tests/test_dmod_mixed_hodge_bar.py;
compute/lib/dmod_purity_char_variety_engine.py|imports=compute/tests/test_dmod_purity_char_variety.py;|refs=compute/tests/test_dmod_purity_char_variety.py;
compute/lib/e8_lattice_bar.py|imports=compute/tests/test_bar_cohomology_lattice_explicit_engine.py;compute/tests/test_lattice_instanton_bar.py;compute/tests/test_master_integration.py;compute/tests/test_extended_families.py;compute/tests/test_e8_lattice.py;|refs=compute/tests/test_bar_cohomology_lattice_explicit_engine.py;compute/tests/test_lattice_instanton_bar.py;compute/tests/test_master_integration.py;compute/tests/test_extended_families.py;compute/tests/test_e8_lattice.py;
compute/lib/euler_koszul_moments.py|imports=|refs=
compute/lib/feynman_integral_engine.py|imports=|refs=






thinking
**Considering module structure**

I’m thinking about potentially using some broad imported modules, which could be a medium solution. It seems we might not need the LOW findings. I wonder if there’s a need to fix the path with `__init__.py`. Maybe we could create `compute/tests/test___init__.py`, but for a cleaner approach, I could move the initializer logic into `compute/lib/core.py` and add `compute/tests/test_core.py`. However, the user asked for an exact fix since it’s an audit, not a change request.
thinking
**Analyzing module structure**

I'm thinking about including `__init__.py` since it's an actual file, and I need to read its contents. There's no exact test file for it, which makes this a bit tricky. I should verify there are no false positives in near-match tests for names. For example, with `graph_complex_orientation_database.py`, I see it's imported in `test_graph_complex_orientation.py`, so it’s a medium match. It’s important to check the line numbers, especially the first lines for shebangs or blank lines, since I often find docstrings there. Using line 1 for findings could be beneficial, and generating a report in `/tmp` may streamline my analysis.
thinking
**Creating findings report**

I need to consider using a shell script to produce sorted findings based on severity and fix suggestions by category. This could then be copied into a final report, though it might end up being quite lengthy. Outputting the results as a code block could help clarify things. I think obtaining exact lines will be critical. Maybe the simplest approach would be to create a report file in the workspace, even if the user didn't specifically ask for that.
thinking
**Organizing findings**

I need to create a list of findings, keeping it to 65 lines, which feels manageable. If I add a summary and a header, that would make it 67 lines total. It would be great to have one finding per line using flat bullets. I should order the findings by severity, prioritizing HIGH and then MEDIUM, and maybe skip LOW. I want to ensure I provide concise fixes for each absence, especially for high direct coverage.
thinking
**Clarifying fixes for tests**

I’m thinking about how to address comment references in tests. It might be best to say "do not rely on [test file] comment mentions." The user likely wants specific fixes, so I could suggest creating `compute/tests/test_feynman_integral_engine.py` for clarity. Maybe I should note any no-import modules with something like, "FIX: create compute/tests/test_<module>.py; no current test imports this module." For modules imported incorrectly, I could say to rename those files or add the correct imports. I want to provide clear, actionable steps!
thinking
**Considering test file renaming**

I’m looking at the file `modular_periodicity_test.py`. It seems there's a direct import in `test_modular_periodicity_conjecture.py`, so renaming it to `test_modular_periodicity_test.py` could be a good move since it's module-specific. I should definitely inspect the first lines of `test_modular_periodicity_conjecture.py` first to be sure. I’m also thinking about renaming `test_w3_extended.py` and `test_toroidal.py` if their titles suggest they clearly test modules. It would make sense to do that!
exec
/bin/zsh -lc "sed -n '1,60p' compute/tests/test_modular_periodicity_conjecture.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
"""Tests for modular periodicity conjecture analysis.

Investigates conj:modular-periodicity-minimal from chiral_hochschild_koszul.tex.

Key findings:
1. Step 1 (T-matrix periodicity) is UNCONDITIONAL — verified for all tested models.
2. Step 2 (weight-space periodicity) FAILS — the convolution with 1/eta destroys
   exact eventual periodicity. dim V_{r,s,[k]} grows monotonically for all k.
3. The theta-function NUMERATOR has exact periodicity (period dividing 2pq).
4. The periodicity defect dim[k+N] - dim[k] grows subexponentially (like partition
   numbers), NOT zero. The claim in the evidence that the tail sum is "empty for
   k sufficiently large" is incorrect.
5. The conjecture may still hold at the bar COHOMOLOGY level (with the differential),
   but this cannot be tested without explicit OPE data.

Refined conjecture candidate: For bar COHOMOLOGY (not chain) dimensions,
exact N-periodicity holds because the bar differential respects the Virasoro
module structure and quotients out the non-periodic growth from 1/eta.

References:
exec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_e8_lattice.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_graph_complex_orientation.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
"""Tests for E8 lattice VOA bar complex.

Ground truth from comp:E8-generators, comp:E8-bar-deg2, comp:E8-curvature,
comp:E8-koszul-dual in detailed_computations.tex.
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.e8_lattice_bar import (
    E8_DATA,
    e8_central_charge,
    e8_generator_count,
    e8_bar_deg2_type_counts,
    e8_bar_diff_type_I,
    e8_bar_diff_type_II,
    e8_bar_diff_type_III,
    e8_nonzero_diff_count,
    e8_curvature,
    e8_curvature_sources,
 succeeded in 51ms:
"""
Tests for the Kontsevich graph complex orientation database.

Tests are organized by:
  1. Graph construction and basic invariants
  2. Automorphism group computation
  3. Graph enumeration and counts
  4. Edge contraction
  5. d^2 = 0 verification (the critical test)
  6. Euler characteristic
  7. Cross-checks and consistency
"""

import pytest
from fractions import Fraction
from collections import Counter

from compute.lib.graph_complex_orientation_database import (
    Graph,
    double_banana, dumbbell, theta, triple_banana, k4, k33, petersen,
exec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_toroidal.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_multichannel_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_w3_extended.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_mc4_defect_vanishing.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""MC4 defect vanishing: D_N = 0 at all finite stages N ≥ 3.

THEOREM: For every N ≥ 3, the defect
  D_{s,t;u;m,n}(N) = C^res_{s,t;u;m,n}(N) - C^DS_{s,t;u;m,n}(N) = 0
on the entire seed packet I_N.

PROOF: W_N = W(sl_N, f_prin) is the principal DS reduction of sl_N-hat.
By the DS-KD intertwining theorem (thm:ds-koszul-intertwine), the OPE
structure constants of W_N (= C^res) equal the DS-extracted structure
constants (= C^DS). Therefore D = 0 identically.

This resolves ALL finite-stage W-infinity MC4 conjectures:
  conj:winfty-stage4-ward-inheritance (RESOLVED by W4 rigidity)
  conj:winfty-stage4-visible-borcherds-transport (RESOLVED)
  conj:winfty-stage4-visible-diagonal-normalization (RESOLVED)
  conj:winfty-stage5-* (ALL 20 conjectures: RESOLVED by induction)

The remaining MC4 content: does the inverse system {W_N}_{N>=3}
with D_N = 0 assemble into a coherent H-level/factorization target?
This is conj:w-infty-bar (the W-infinity large-N coupling).
 succeeded in 53ms:
r"""Tests for multi-channel shadow extraction for lattice VOAs.

Comprehensive test suite covering:
  1. All 24 Niemeier lattices have scalar shadow kappa = 24
  2. Per-factor shadow data correctness (kappa_aff, dim, h, etc.)
  3. D16+E8 and 3E8 (same |R|=720) distinguished by Channel 1
  4. A11+D7+E6 and 4E6 (same |R|=288) distinguished by Channel 1
  5. All 5 |R|-collision pairs distinguished by Channel 1
  6. All 10 rank-collision pairs distinguished by Coxeter number
  7. Every pair of Niemeier lattices distinguished by SOME channel
  8. Minimal distinguishing channel set identified
  9. kappa_aff injectivity on ADE types
  10. Kappa decomposition analysis
"""

import pytest
from fractions import Fraction
from sympy import Rational

from compute.lib.multichannel_shadow import (
 succeeded in 53ms:
"""Tests for toroidal/elliptic bar complex."""

import pytest
from sympy import pi, Symbol

from compute.lib.toroidal_bar import (
    eisenstein_q_expansion,
    zeta_laurent_coefficients,
    elliptic_bar_diff_deg,
    elliptic_curvature,
    elliptic_vs_rational,
    bar_decomposition_by_weight,
    fay_d_squared_zero,
    verify_toroidal,
)


class TestEisenstein:
    def test_e2_coeffs(self):
        coeffs = eisenstein_q_expansion(2, 4)
 succeeded in 53ms:
"""Tests for W_3 bar complex extended computation (w3_bar_extended.py).

Verifies:
1. PBW basis dimensions match the generating function
2. All generator-pair OPE products match ground truth
3. Skew symmetry W_{(0)}T = 2*dW
4. DS complementarity c + c' = 100
5. Bar chain group dimensions (combinatorial)
6. Known bar cohomology ground truth H^1=2, H^2=5, H^3=16, H^4=52

The bar cohomology values come from the CHIRAL bar complex (involving
configuration space forms and residue calculus). The current module
verifies all algebraic ingredients but does not yet implement the
full chiral bar differential needed to independently compute H^n.
"""

import pytest
import numpy as np

from compute.lib.w3_bar_extended import (

thinking
**Renaming test files**

I'm confirming some tests that need renaming for clarity and dedication. 

I will rename `test_e8_lattice.py` to match `e8_lattice_bar.py`, and similarly for `test_graph_complex_orientation.py` and the others to maintain consistency. 

For the `test_mc4_defect_vanishing.py`, I might rename it to `test_mc4_stage4_resolution.py`, since it's theorem-specific. Additionally, I need to address `test_multichannel_shadow.py`, as it references a different module, and create a `test_niemeier_multichannel.py` for accuracy. 

I should double-check `test_transport_to_transpose.py` to see if it needs adjusting too.
exec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_alpha_g_simple_lie_verification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_transport_to_transpose.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_integrable_genus2.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Tests for alpha_g_simple_lie_verification_engine.py.

Verifies alpha_g = 2*rank + 4*dim*h^v for all 31 simple Lie algebras
in types A_1--A_8, B_2--B_8, C_3--C_8, D_4--D_8, G_2, F_4, E_6, E_7, E_8.

MULTI-PATH VERIFICATION:
  Path 1: [DC] Direct computation from formula 2*rank + 4*dim*h^v
  Path 2: [CF] Cross-family consistency (B_n/C_n share dim, differ in h^v)
  Path 3: [LC] Limiting/boundary cases (A_1=sl_2, smallest of each type)
  Path 4: Classical dim/h^v cross-check against rank formulas
  Path 5: Isomorphism checks (B_2=C_2, D_3=A_3)
  Path 6: Decomposition: alpha_g = rank_contribution + curvature_contribution

References:
  Bourbaki, Lie Groups and Lie Algebras, Ch. IV-VI (Tables)
  Humphreys, Introduction to Lie Algebras, Table p. 66
  Kac, Infinite-Dimensional Lie Algebras, Table Aff 1 (dual Coxeter numbers)
"""

import pytest
 succeeded in 53ms:
"""Tests for conj:type-a-transport-to-transpose investigation.

Tests the conjecture: at generic level, for type A,
    (W^k(sl_N, f_lambda))^! = W^{k^v_lambda}(sl_N, f_{lambda^t})
with k^v = -k - 2N and lambda^t = partition transpose.

Three parts:
  (A) Transport-closure of hook vertices = Par(N).
  (B) Central charge complementarity c + c' is level-independent.
  (C) Generator spectrum, ghost constant, and level transform compatibility.
"""

import pytest
from fractions import Fraction

from compute.lib.transport_to_transpose import (
    TransposeConjectureEngine,
    affine_kappa,
    central_charge_sl_N,
    complementarity_constant,
 succeeded in 53ms:
r"""Tests for the integrable hierarchy approach to genus-2 free energy.

MULTI-PATH VERIFICATION for F_2 across:
    Path 1: Direct A-hat formula (kappa * lambda_2^FP)
    Path 2: Integrable hierarchy (KdV / Boussinesq / Toda / Gelfand-Dickey)
    Path 3: Matrix model (Gaussian / cubic potential)
    Path 4: Graph sum (from w3_genus2.py and multichannel_genus2.py)
    Path 5: Topological recursion (EO on shadow spectral curve)

KEY RESULTS TESTED:
    1. lambda_2^FP = 7/5760 (exact, from Bernoulli numbers)
    2. F_2/F_1 = 7/240 (universal ratio, independent of algebra)
    3. KdV F_2 = (c/2) * 7/5760 for Virasoro (all three paths agree)
    4. Toda F_2 = 3(k+2)/4 * 7/5760 for V_k(sl_2) (uniform-weight)
    5. Boussinesq F_2^{diag} = 5c/6 * 7/5760 for W_3 (per-channel)
    6. W_3 cross-channel correction delta_F_2 = (c+204)/(16c) (graph sum)
    7. Multi-generator universality FAILS at genus 2 for W_3
    8. Additivity: F_2(A_1 + A_2) = F_2(A_1) + F_2(A_2)
    9. F_2 > 0 for all kappa > 0 (positivity from A-hat)
   10. Heisenberg = simplest test case (class G, exact)
exec
/bin/zsh -lc "sed -n '1,30p' compute/tests/test_multigen_universality_proof.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Tests for the attempted multi-generator universality proof.

THE ATTEMPTED PROOF (three pillars):

PILLAR 1 — MC equation (D² = 0).
The bar-intrinsic MC element Θ_A = D_A - d_0 satisfies the MC equation
for ALL modular Koszul algebras (thm:mc2-bar-intrinsic). At genus g,
the MC equation decomposes over stable graphs. The "Class II" graphs
(those with genus-0 vertices of valence ≥ 3, carrying higher-arity
shadow data S_3, S_4, ...) are forced to sum to zero by D² = 0.

PILLAR 2 — Heisenberg linearity.
For Heisenberg, all shadow data S_n = 0 for n ≥ 3 (class G). The
genus-g free energy F_g^{Heis}(κ) = κ · λ_g^FP is EXACTLY LINEAR in κ.
The "Class I" graphs (all vertex genera ≥ 1) give the full answer.
Any graph amplitude that is κ-INDEPENDENT must therefore vanish
(otherwise F_g would have a nonzero constant term). For multi-channel
algebras with r channels, such κ-independent terms would be multiplied
by r — but since they're 0, this is harmless. The κ-LINEAR terms
produce κ_total · λ_g^FP.
exec
/bin/zsh -lc "sed -n '31,70p' compute/tests/test_multigen_universality_proof.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
for that failed proof attempt rather than a proof certificate.
"""

import pytest
from fractions import Fraction

import sys
sys.path.insert(0, '.')

from compute.lib.multigen_universality_attack import (
    lambda_fp,
    w3_kappas,
    w3_quartic_shadows,
    w3_cubic_shadows,
    decisive_test_genus2,
    verify_heisenberg_linearity,
    mathematical_diagnosis,
    class_II_single_channel,
    genus2_planted_forest_correction,
)


thinking
**Inspecting test files**

I’m focused on improving the various test files and considering renaming them for clarity. I see that `test_poincare_duality_bar_engine.py` imports a different module, so it needs some inspection. There's a need to rename `test_sft_graph_complex.py` and check if `test_transport_to_transpose.py` aligns with its dedicated function. I’m thinking about potentially adding new test files based on the inspections, as well as fixing or creating specific files to keep things organized without breaking existing naming conventions.
thinking
**Planning exact fixes**

I’m looking at how to implement the fastest fixes by potentially renaming dedicated suites for clarity. I might compute severity counts: High 15 and Medium 50, and I see the need to order these by severity, starting with HIGH. It’s clear I’ve checked 1,325 files with 65 findings, resulting in a FAIL verdict. I wonder if I should include the exact rule in my summary. While the user wants a specific format for the lines, I might keep it concise without an intro, ensuring the lines are correctly formatted and possibly grouped by severity.
exec
/bin/zsh -lc "sed -n '31,50p' compute/tests/test_multichannel_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    _channel_1b,
    _channel_1c,
    _channel_1d,
    _channel_full,
    _num_roots,
)
from compute.lib.niemeier_multichannel import (
    niemeier_multichannel_atlas,
    build_discrimination_matrix,
    full_discrimination_report,
    resolve_collision_pairs,
    rank_collision_analysis,
    verify_kappa_aff_injectivity,
    channel_1_shadow_table,
    kappa_decomposition_analysis,
    verify_all_pairwise_distinguished,
    verify_minimal_channel,
)
from compute.lib.niemeier_shadow_atlas import (
    ALL_NIEMEIER_LABELS,

thinking
**Organizing test files**

I'm realizing that test_multichannel_shadow.py imports the exact module and a broader one, but I think it makes sense to keep the name since it's covering two modules. Splitting out the niemeier_multichannel assertions into a dedicated test_niemeier_multichannel.py would be beneficial. I see similar needs for test_siegel_eisenstein.py since multiple suites import it. For t_theta and w_algebra_transport_propagation, I might also consider adding dedicated files. I need to check specifics around test_transport_to_transpose.
exec
/bin/zsh -lc "sed -n '1,50p' compute/tests/test_transport_to_transpose.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""Tests for conj:type-a-transport-to-transpose investigation.

Tests the conjecture: at generic level, for type A,
    (W^k(sl_N, f_lambda))^! = W^{k^v_lambda}(sl_N, f_{lambda^t})
with k^v = -k - 2N and lambda^t = partition transpose.

Three parts:
  (A) Transport-closure of hook vertices = Par(N).
  (B) Central charge complementarity c + c' is level-independent.
  (C) Generator spectrum, ghost constant, and level transform compatibility.
"""

import pytest
from fractions import Fraction

from compute.lib.transport_to_transpose import (
    TransposeConjectureEngine,
    affine_kappa,
    central_charge_sl_N,
    complementarity_constant,


thinking
**Structuring the summary**

The user requested a summary only, so I might include this within a verdict line. I’m considering using a structure without a pass/fail indication. The verdict could be a simple "FAIL" if findings are greater than zero. It sounds good to consider adding a line before the summary, perhaps labeled `## Summary` in markdown format. I need to ensure that my final response doesn’t include any commentary on methodology.
thinking
**Considering script generation**

I’m thinking of setting N to 1325 and 65 for a good starting point. It might help to mention the file and line numbers as well. Using a script could generate a sorted list of final lines, which helps avoid mistakes since manually writing 65 lines could be error-prone. I could create a temporary categorization map in my analysis, but careful manual crafting is also manageable. Ultimately, I’ll balance between using shell scripts for raw line templates and manual input. Let’s get scripting!
exec
/bin/zsh -lc "cat <<'EOF' >/tmp/missing_audit_report.txt
[HIGH] compute/lib/__init__.py:1 — PROBLEM: The package initializer contains kernel logic but has no matching "'`compute/tests/test___init__.py`, and no current test imports it directly. FIX: add `compute/tests/test___init__.py` with direct imports and initializer-level assertions.
[HIGH] compute/lib/euler_koszul_moments.py:1 — PROBLEM: This module has no matching `compute/tests/test_euler_koszul_moments.py`, and no current test imports it directly. FIX: add `compute/tests/test_euler_koszul_moments.py` with direct imports and module-scoped assertions.
[HIGH] compute/lib/feynman_integral_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_feynman_integral_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_feynman_integral_engine.py` with direct imports and module-scoped assertions.
[HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
[HIGH] compute/lib/graph_complex_cohomology_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_graph_complex_cohomology_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_graph_complex_cohomology_engine.py` with direct imports and graph-complex cohomology assertions.
[HIGH] compute/lib/lattice_genus2_theta.py:1 — PROBLEM: This module has no matching `compute/tests/test_lattice_genus2_theta.py`; the only current hit is a narrative mention in `test_theorem_genus2_sl3_partition_engine.py`, not an import. FIX: add `compute/tests/test_lattice_genus2_theta.py` with direct imports and theta-series assertions.
[HIGH] compute/lib/mc4_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_mc4_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_mc4_diagnostic.py` with direct imports and diagnostic-state assertions.
[HIGH] compute/lib/mc5_genus_geq2_strategies.py:1 — PROBLEM: This strategy module has no matching `compute/tests/test_mc5_genus_geq2_strategies.py`; `test_mc5_higher_genus.py` only names it in the docstring and does not import it. FIX: add `compute/tests/test_mc5_genus_geq2_strategies.py` with direct imports and strategy-level checks.
[HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
[HIGH] compute/lib/ope_corrected_sewing.py:1 — PROBLEM: This module has no matching `compute/tests/test_ope_corrected_sewing.py`, and no current test imports it directly. FIX: add `compute/tests/test_ope_corrected_sewing.py` with direct imports and sewing-correction assertions.
[HIGH] compute/lib/poincare_duality_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_poincare_duality_engine.py`; `test_poincare_duality_bar_engine.py` targets a different module and only mentions this file in its header. FIX: add `compute/tests/test_poincare_duality_engine.py` with direct imports and engine-level Poincare-duality assertions.
[HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
[HIGH] compute/lib/w3_h2_sl3_decomposition_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_w3_h2_sl3_decomposition_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_h2_sl3_decomposition_engine.py` with direct imports and decomposition assertions.
[HIGH] compute/lib/w3_miura_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_w3_miura_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_miura_diagnostic.py` with direct imports and Miura-diagnostic assertions.
[HIGH] compute/lib/w4_primary_projection.py:1 — PROBLEM: This module has no matching `compute/tests/test_w4_primary_projection.py`, and no current test imports it directly. FIX: add `compute/tests/test_w4_primary_projection.py` with direct imports and primary-projection assertions.
[MEDIUM] compute/lib/abjm_holographic_datum.py:1 — PROBLEM: No exact matching test file exists; ABJM-specific checks are buried in broader twisted-holography suites instead of `compute/tests/test_abjm_holographic_datum.py`. FIX: add `compute/tests/test_abjm_holographic_datum.py` and move the ABJM-only assertions out of `test_twisted_holography_comparison_engine.py`.
[MEDIUM] compute/lib/alpha_g_simple_lie_verification_engine.py:1 — PROBLEM: The engine is tested only through the misnamed file `compute/tests/test_alpha_g_simple_lie_verification.py`, so the exact `test_<module>.py` contract is missing. FIX: rename `compute/tests/test_alpha_g_simple_lie_verification.py` to `compute/tests/test_alpha_g_simple_lie_verification_engine.py`.
[MEDIUM] compute/lib/arithmetic_comparison_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_arithmetic_comparison.py`, but the exact matching file `compute/tests/test_arithmetic_comparison_test.py` is missing. FIX: rename `compute/tests/test_arithmetic_comparison.py` to `compute/tests/test_arithmetic_comparison_test.py`.
[MEDIUM] compute/lib/bar_graph_complex_bridge_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bar_graph_complex_bridge.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bar_graph_complex_bridge.py` to `compute/tests/test_bar_graph_complex_bridge_engine.py`.
[MEDIUM] compute/lib/bethe_tq_relation_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bethe_tq_relation.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bethe_tq_relation.py` to `compute/tests/test_bethe_tq_relation_engine.py`.
[MEDIUM] compute/lib/bv_brst_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bv_brst_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bv_brst_purity.py` to `compute/tests/test_bv_brst_purity_engine.py`.
[MEDIUM] compute/lib/cohft_dr_hierarchy_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_dr_hierarchy.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_dr_hierarchy.py` to `compute/tests/test_cohft_dr_hierarchy_engine.py`.
[MEDIUM] compute/lib/cohft_givental_rmatrix_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_givental_rmatrix.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_givental_rmatrix.py` to `compute/tests/test_cohft_givental_rmatrix_engine.py`.
[MEDIUM] compute/lib/cohft_string_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_string_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_string_genus2.py` to `compute/tests/test_cohft_string_genus2_engine.py`.
[MEDIUM] compute/lib/cohft_toprec_string_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_toprec_string.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_toprec_string.py` to `compute/tests/test_cohft_toprec_string_engine.py`.
[MEDIUM] compute/lib/cohft_virasoro_constraints_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_virasoro_constraints.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_virasoro_constraints.py` to `compute/tests/test_cohft_virasoro_constraints_engine.py`.
[MEDIUM] compute/lib/coxeter_anomaly_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_coxeter_anomaly.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_coxeter_anomaly.py` to `compute/tests/test_coxeter_anomaly_test.py`.
[MEDIUM] compute/lib/delta_fg_degree_pattern_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_delta_fg_degree_pattern.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_delta_fg_degree_pattern.py` to `compute/tests/test_delta_fg_degree_pattern_engine.py`.
[MEDIUM] compute/lib/dmod_counterexample_search_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_counterexample_search.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_counterexample_search.py` to `compute/tests/test_dmod_counterexample_search_engine.py`.
[MEDIUM] compute/lib/dmod_filtration_ss_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_filtration_ss.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_filtration_ss.py` to `compute/tests/test_dmod_filtration_ss_engine.py`.
[MEDIUM] compute/lib/dmod_kl_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_kl_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_kl_purity.py` to `compute/tests/test_dmod_kl_purity_engine.py`.
[MEDIUM] compute/lib/dmod_mixed_hodge_bar_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_mixed_hodge_bar.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_mixed_hodge_bar.py` to `compute/tests/test_dmod_mixed_hodge_bar_engine.py`.
[MEDIUM] compute/lib/dmod_purity_char_variety_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_purity_char_variety.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_purity_char_variety.py` to `compute/tests/test_dmod_purity_char_variety_engine.py`.
[MEDIUM] compute/lib/e8_lattice_bar.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_e8_lattice.py`. FIX: rename `compute/tests/test_e8_lattice.py` to `compute/tests/test_e8_lattice_bar.py`.
[MEDIUM] compute/lib/formality_obstruction_loop4_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_formality_obstruction_loop4.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_formality_obstruction_loop4.py` to `compute/tests/test_formality_obstruction_loop4_engine.py`.
[MEDIUM] compute/lib/graph_complex_orientation_database.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_graph_complex_orientation.py`. FIX: rename `compute/tests/test_graph_complex_orientation.py` to `compute/tests/test_graph_complex_orientation_database.py`.
[MEDIUM] compute/lib/holographic_dmod_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_holographic_dmod_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_holographic_dmod_purity.py` to `compute/tests/test_holographic_dmod_purity_engine.py`.
[MEDIUM] compute/lib/integrable_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_integrable_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_integrable_genus2.py` to `compute/tests/test_integrable_genus2_engine.py`.
[MEDIUM] compute/lib/kac_chevalley_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_kac_chevalley.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_kac_chevalley.py` to `compute/tests/test_kac_chevalley_test.py`.
[MEDIUM] compute/lib/lattice_genus2_universality_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_lattice_genus2_universality.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_lattice_genus2_universality.py` to `compute/tests/test_lattice_genus2_universality_engine.py`.
[MEDIUM] compute/lib/mc4_stage4_resolution.py:1 — PROBLEM: No exact matching test file exists; the direct unit coverage lives in `compute/tests/test_mc4_defect_vanishing.py`. FIX: rename `compute/tests/test_mc4_defect_vanishing.py` to `compute/tests/test_mc4_stage4_resolution.py`.
[MEDIUM] compute/lib/mc_crossing_theorem_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mc_crossing_theorem.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mc_crossing_theorem.py` to `compute/tests/test_mc_crossing_theorem_engine.py`.
[MEDIUM] compute/lib/mg_genus2_clutching_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_genus2_clutching.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_genus2_clutching.py` to `compute/tests/test_mg_genus2_clutching_engine.py`.
[MEDIUM] compute/lib/mg_harer_stability_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_harer_stability.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_harer_stability.py` to `compute/tests/test_mg_harer_stability_engine.py`.
[MEDIUM] compute/lib/mg_kuranishi_parity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_kuranishi_parity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_kuranishi_parity.py` to `compute/tests/test_mg_kuranishi_parity_engine.py`.
[MEDIUM] compute/lib/mg_tautological_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_tautological_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_tautological_purity.py` to `compute/tests/test_mg_tautological_purity_engine.py`.
[MEDIUM] compute/lib/mg_w3_genus2_graph_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_w3_genus2_graph.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_w3_genus2_graph.py` to `compute/tests/test_mg_w3_genus2_graph_engine.py`.
[MEDIUM] compute/lib/modular_periodicity_test.py:1 — PROBLEM: The dedicated coverage sits in `compute/tests/test_modular_periodicity_conjecture.py`, while `compute/tests/test_modular_periodicity.py` targets a different module. FIX: rename `compute/tests/test_modular_periodicity_conjecture.py` to `compute/tests/test_modular_periodicity_test.py`.
[MEDIUM] compute/lib/multigen_universality_attack.py:1 — PROBLEM: The module is covered through the misnamed dedicated suite `compute/tests/test_multigen_universality_proof.py`, so the exact `test_<module>.py` file is still missing. FIX: rename `compute/tests/test_multigen_universality_proof.py` to `compute/tests/test_multigen_universality_attack.py`.
[MEDIUM] compute/lib/n2_sca_chiral_bar_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_n2_sca_chiral_bar.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_n2_sca_chiral_bar.py` to `compute/tests/test_n2_sca_chiral_bar_engine.py`.
[MEDIUM] compute/lib/n2_sca_chiral_bar_weight_graded_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_n2_sca_chiral_bar_weight_graded.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_n2_sca_chiral_bar_weight_graded.py` to `compute/tests/test_n2_sca_chiral_bar_weight_graded_engine.py`.
[MEDIUM] compute/lib/niemeier_multichannel.py:1 — PROBLEM: No exact matching test file exists; `compute/tests/test_multichannel_shadow.py` mixes `niemeier_multichannel.py` assertions with a different module. FIX: add `compute/tests/test_niemeier_multichannel.py` and move the Niemeier-specific assertions out of `test_multichannel_shadow.py`.
[MEDIUM] compute/lib/offdiag_newton_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_offdiag_newton.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_offdiag_newton.py` to `compute/tests/test_offdiag_newton_test.py`.
[MEDIUM] compute/lib/operadic_koszul_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_operadic_koszul_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_operadic_koszul_genus2.py` to `compute/tests/test_operadic_koszul_genus2_engine.py`.
[MEDIUM] compute/lib/ordered_trace_invariant_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_ordered_trace_invariant.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_ordered_trace_invariant.py` to `compute/tests/test_ordered_trace_invariant_engine.py`.
[MEDIUM] compute/lib/rectangular_w_algebra_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_rectangular_w_algebra.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_rectangular_w_algebra.py` to `compute/tests/test_rectangular_w_algebra_engine.py`.
[MEDIUM] compute/lib/sft_graph_complex_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_sft_graph_complex.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_sft_graph_complex.py` to `compute/tests/test_sft_graph_complex_engine.py`.
[MEDIUM] compute/lib/siegel_eisenstein.py:1 — PROBLEM: No exact matching test file exists; coefficient and product checks are scattered across several Siegel and E8 suites instead of `compute/tests/test_siegel_eisenstein.py`. FIX: add `compute/tests/test_siegel_eisenstein.py` and move the direct module checks there.
[MEDIUM] compute/lib/tautological_genus2_numerical_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_tautological_genus2_numerical.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_tautological_genus2_numerical.py` to `compute/tests/test_tautological_genus2_numerical_engine.py`.
[MEDIUM] compute/lib/toroidal_bar.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_toroidal.py`. FIX: rename `compute/tests/test_toroidal.py` to `compute/tests/test_toroidal_bar.py`.
[MEDIUM] compute/lib/vertex_algebra_extensions_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_vertex_algebra_extensions.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_vertex_algebra_extensions.py` to `compute/tests/test_vertex_algebra_extensions_engine.py`.
[MEDIUM] compute/lib/w3_bar_extended.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_w3_extended.py`. FIX: rename `compute/tests/test_w3_extended.py` to `compute/tests/test_w3_bar_extended.py`.
[MEDIUM] compute/lib/w4_ds_ope.py:1 — PROBLEM: No exact matching test file exists; direct `w4_ds_ope.py` assertions are scattered across multiple W4 suites and mixed with `w4_ds_ope_extraction.py`. FIX: add `compute/tests/test_w4_ds_ope.py` and move the direct Miura/Wick assertions there.
[MEDIUM] compute/lib/w_algebra_transport_propagation.py:1 — PROBLEM: No exact matching test file exists; direct checks of this module are mixed into broader transpose and DS suites. FIX: add `compute/tests/test_w_algebra_transport_propagation.py` and move the direct module assertions there.
[MEDIUM] compute/lib/wp_koszulness_definitive_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_wp_koszulness_definitive.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_wp_koszulness_definitive.py` to `compute/tests/test_wp_koszulness_definitive_engine.py`.
EOF
wc -l /tmp/missing_audit_report.txt' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
      65 /tmp/missing_audit_report.txt

thinking
**Verifying missing modules**

I'm thinking I need to verify that all missing modules are included in the list. A good idea would be to compare the generated list with the actual missing list by extracting the file names. This way, I can easily see what’s missing and ensure everything is accounted for. Let’s go ahead and make that comparison to avoid any issues later on!
codex
I have the full 65-line finding set assembled. I’m doing one final reconciliation pass now against the live missing-module list so the output is exhaustive with no dropped or duplicated modules.
exec
/bin/zsh -lc "comm -3 <(cut -d' ' -f2 /tmp/missing_audit_report.txt | cut -d: -f1 | sort) <(sort /tmp/missing_compute_tests.txt)" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

exec
/bin/zsh -lc 'cat /tmp/missing_audit_report.txt' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
[HIGH] compute/lib/__init__.py:1 — PROBLEM: The package initializer contains kernel logic but has no matching `compute/tests/test___init__.py`, and no current test imports it directly. FIX: add `compute/tests/test___init__.py` with direct imports and initializer-level assertions.
[HIGH] compute/lib/euler_koszul_moments.py:1 — PROBLEM: This module has no matching `compute/tests/test_euler_koszul_moments.py`, and no current test imports it directly. FIX: add `compute/tests/test_euler_koszul_moments.py` with direct imports and module-scoped assertions.
[HIGH] compute/lib/feynman_integral_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_feynman_integral_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_feynman_integral_engine.py` with direct imports and module-scoped assertions.
[HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
[HIGH] compute/lib/graph_complex_cohomology_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_graph_complex_cohomology_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_graph_complex_cohomology_engine.py` with direct imports and graph-complex cohomology assertions.
[HIGH] compute/lib/lattice_genus2_theta.py:1 — PROBLEM: This module has no matching `compute/tests/test_lattice_genus2_theta.py`; the only current hit is a narrative mention in `test_theorem_genus2_sl3_partition_engine.py`, not an import. FIX: add `compute/tests/test_lattice_genus2_theta.py` with direct imports and theta-series assertions.
[HIGH] compute/lib/mc4_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_mc4_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_mc4_diagnostic.py` with direct imports and diagnostic-state assertions.
[HIGH] compute/lib/mc5_genus_geq2_strategies.py:1 — PROBLEM: This strategy module has no matching `compute/tests/test_mc5_genus_geq2_strategies.py`; `test_mc5_higher_genus.py` only names it in the docstring and does not import it. FIX: add `compute/tests/test_mc5_genus_geq2_strategies.py` with direct imports and strategy-level checks.
[HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
[HIGH] compute/lib/ope_corrected_sewing.py:1 — PROBLEM: This module has no matching `compute/tests/test_ope_corrected_sewing.py`, and no current test imports it directly. FIX: add `compute/tests/test_ope_corrected_sewing.py` with direct imports and sewing-correction assertions.
[HIGH] compute/lib/poincare_duality_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_poincare_duality_engine.py`; `test_poincare_duality_bar_engine.py` targets a different module and only mentions this file in its header. FIX: add `compute/tests/test_poincare_duality_engine.py` with direct imports and engine-level Poincare-duality assertions.
[HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
[HIGH] compute/lib/w3_h2_sl3_decomposition_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_w3_h2_sl3_decomposition_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_h2_sl3_decomposition_engine.py` with direct imports and decomposition assertions.
[HIGH] compute/lib/w3_miura_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_w3_miura_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_miura_diagnostic.py` with direct imports and Miura-diagnostic assertions.
[HIGH] compute/lib/w4_primary_projection.py:1 — PROBLEM: This module has no matching `compute/tests/test_w4_primary_projection.py`, and no current test imports it directly. FIX: add `compute/tests/test_w4_primary_projection.py` with direct imports and primary-projection assertions.
[MEDIUM] compute/lib/abjm_holographic_datum.py:1 — PROBLEM: No exact matching test file exists; ABJM-specific checks are buried in broader twisted-holography suites instead of `compute/tests/test_abjm_holographic_datum.py`. FIX: add `compute/tests/test_abjm_holographic_datum.py` and move the ABJM-only assertions out of `test_twisted_holography_comparison_engine.py`.
[MEDIUM] compute/lib/alpha_g_simple_lie_verification_engine.py:1 — PROBLEM: The engine is tested only through the misnamed file `compute/tests/test_alpha_g_simple_lie_verification.py`, so the exact `test_<module>.py` contract is missing. FIX: rename `compute/tests/test_alpha_g_simple_lie_verification.py` to `compute/tests/test_alpha_g_simple_lie_verification_engine.py`.
[MEDIUM] compute/lib/arithmetic_comparison_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_arithmetic_comparison.py`, but the exact matching file `compute/tests/test_arithmetic_comparison_test.py` is missing. FIX: rename `compute/tests/test_arithmetic_comparison.py` to `compute/tests/test_arithmetic_comparison_test.py`.
[MEDIUM] compute/lib/bar_graph_complex_bridge_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bar_graph_complex_bridge.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bar_graph_complex_bridge.py` to `compute/tests/test_bar_graph_complex_bridge_engine.py`.
[MEDIUM] compute/lib/bethe_tq_relation_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bethe_tq_relation.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bethe_tq_relation.py` to `compute/tests/test_bethe_tq_relation_engine.py`.
codex
- [HIGH] compute/lib/__init__.py:1 — PROBLEM: The package initializer contains kernel logic but has no matching `compute/tests/test___init__.py`, and no current test imports it directly. FIX: add `compute/tests/test___init__.py` with direct imports and initializer-level assertions.
- [HIGH] compute/lib/euler_koszul_moments.py:1 — PROBLEM: This module has no matching `compute/tests/test_euler_koszul_moments.py`, and no current test imports it directly. FIX: add `compute/tests/test_euler_koszul_moments.py` with direct imports and module-scoped assertions.
- [HIGH] compute/lib/feynman_integral_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_feynman_integral_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_feynman_integral_engine.py` with direct imports and module-scoped assertions.
- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
- [HIGH] compute/lib/graph_complex_cohomology_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_graph_complex_cohomology_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_graph_complex_cohomology_engine.py` with direct imports and graph-complex cohomology assertions.
- [HIGH] compute/lib/lattice_genus2_theta.py:1 — PROBLEM: This module has no matching `compute/tests/test_lattice_genus2_theta.py`; the only current hit is a narrative mention in `test_theorem_genus2_sl3_partition_engine.py`, not an import. FIX: add `compute/tests/test_lattice_genus2_theta.py` with direct imports and theta-series assertions.
- [HIGH] compute/lib/mc4_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_mc4_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_mc4_diagnostic.py` with direct imports and diagnostic-state assertions.
- [HIGH] compute/lib/mc5_genus_geq2_strategies.py:1 — PROBLEM: This strategy module has no matching `compute/tests/test_mc5_genus_geq2_strategies.py`; `test_mc5_higher_genus.py` only names it in the docstring and does not import it. FIX: add `compute/tests/test_mc5_genus_geq2_strategies.py` with direct imports and strategy-level checks.
- [HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
- [HIGH] compute/lib/ope_corrected_sewing.py:1 — PROBLEM: This module has no matching `compute/tests/test_ope_corrected_sewing.py`, and no current test imports it directly. FIX: add `compute/tests/test_ope_corrected_sewing.py` with direct imports and sewing-correction assertions.
- [HIGH] compute/lib/poincare_duality_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_poincare_duality_engine.py`; `test_poincare_duality_bar_engine.py` targets a different module and only mentions this file in its header. FIX: add `compute/tests/test_poincare_duality_engine.py` with direct imports and engine-level Poincare-duality assertions.
- [HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
- [HIGH] compute/lib/w3_h2_sl3_decomposition_engine.py:1 — PROBLEM: This engine has no matching `compute/tests/test_w3_h2_sl3_decomposition_engine.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_h2_sl3_decomposition_engine.py` with direct imports and decomposition assertions.
- [HIGH] compute/lib/w3_miura_diagnostic.py:1 — PROBLEM: This diagnostic module has no matching `compute/tests/test_w3_miura_diagnostic.py`, and no current test imports it directly. FIX: add `compute/tests/test_w3_miura_diagnostic.py` with direct imports and Miura-diagnostic assertions.
- [HIGH] compute/lib/w4_primary_projection.py:1 — PROBLEM: This module has no matching `compute/tests/test_w4_primary_projection.py`, and no current test imports it directly. FIX: add `compute/tests/test_w4_primary_projection.py` with direct imports and primary-projection assertions.
- [MEDIUM] compute/lib/abjm_holographic_datum.py:1 — PROBLEM: No exact matching test file exists; ABJM-specific checks are buried in broader twisted-holography suites instead of `compute/tests/test_abjm_holographic_datum.py`. FIX: add `compute/tests/test_abjm_holographic_datum.py` and move the ABJM-only assertions out of `test_twisted_holography_comparison_engine.py`.
- [MEDIUM] compute/lib/alpha_g_simple_lie_verification_engine.py:1 — PROBLEM: The engine is tested only through the misnamed file `compute/tests/test_alpha_g_simple_lie_verification.py`, so the exact `test_<module>.py` contract is missing. FIX: rename `compute/tests/test_alpha_g_simple_lie_verification.py` to `compute/tests/test_alpha_g_simple_lie_verification_engine.py`.
- [MEDIUM] compute/lib/arithmetic_comparison_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_arithmetic_comparison.py`, but the exact matching file `compute/tests/test_arithmetic_comparison_test.py` is missing. FIX: rename `compute/tests/test_arithmetic_comparison.py` to `compute/tests/test_arithmetic_comparison_test.py`.
- [MEDIUM] compute/lib/bar_graph_complex_bridge_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bar_graph_complex_bridge.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bar_graph_complex_bridge.py` to `compute/tests/test_bar_graph_complex_bridge_engine.py`.
- [MEDIUM] compute/lib/bethe_tq_relation_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bethe_tq_relation.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bethe_tq_relation.py` to `compute/tests/test_bethe_tq_relation_engine.py`.
- [MEDIUM] compute/lib/bv_brst_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_bv_brst_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_bv_brst_purity.py` to `compute/tests/test_bv_brst_purity_engine.py`.
- [MEDIUM] compute/lib/cohft_dr_hierarchy_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_dr_hierarchy.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_dr_hierarchy.py` to `compute/tests/test_cohft_dr_hierarchy_engine.py`.
- [MEDIUM] compute/lib/cohft_givental_rmatrix_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_givental_rmatrix.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_givental_rmatrix.py` to `compute/tests/test_cohft_givental_rmatrix_engine.py`.
- [MEDIUM] compute/lib/cohft_string_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_string_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_string_genus2.py` to `compute/tests/test_cohft_string_genus2_engine.py`.
- [MEDIUM] compute/lib/cohft_toprec_string_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_toprec_string.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_toprec_string.py` to `compute/tests/test_cohft_toprec_string_engine.py`.
- [MEDIUM] compute/lib/cohft_virasoro_constraints_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_cohft_virasoro_constraints.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_cohft_virasoro_constraints.py` to `compute/tests/test_cohft_virasoro_constraints_engine.py`.
- [MEDIUM] compute/lib/coxeter_anomaly_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_coxeter_anomaly.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_coxeter_anomaly.py` to `compute/tests/test_coxeter_anomaly_test.py`.
- [MEDIUM] compute/lib/delta_fg_degree_pattern_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_delta_fg_degree_pattern.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_delta_fg_degree_pattern.py` to `compute/tests/test_delta_fg_degree_pattern_engine.py`.
- [MEDIUM] compute/lib/dmod_counterexample_search_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_counterexample_search.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_counterexample_search.py` to `compute/tests/test_dmod_counterexample_search_engine.py`.
- [MEDIUM] compute/lib/dmod_filtration_ss_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_filtration_ss.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_filtration_ss.py` to `compute/tests/test_dmod_filtration_ss_engine.py`.
- [MEDIUM] compute/lib/dmod_kl_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_kl_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_kl_purity.py` to `compute/tests/test_dmod_kl_purity_engine.py`.
- [MEDIUM] compute/lib/dmod_mixed_hodge_bar_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_mixed_hodge_bar.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_mixed_hodge_bar.py` to `compute/tests/test_dmod_mixed_hodge_bar_engine.py`.
- [MEDIUM] compute/lib/dmod_purity_char_variety_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_dmod_purity_char_variety.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_dmod_purity_char_variety.py` to `compute/tests/test_dmod_purity_char_variety_engine.py`.
- [MEDIUM] compute/lib/e8_lattice_bar.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_e8_lattice.py`. FIX: rename `compute/tests/test_e8_lattice.py` to `compute/tests/test_e8_lattice_bar.py`.
- [MEDIUM] compute/lib/formality_obstruction_loop4_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_formality_obstruction_loop4.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_formality_obstruction_loop4.py` to `compute/tests/test_formality_obstruction_loop4_engine.py`.
- [MEDIUM] compute/lib/graph_complex_orientation_database.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_graph_complex_orientation.py`. FIX: rename `compute/tests/test_graph_complex_orientation.py` to `compute/tests/test_graph_complex_orientation_database.py`.
- [MEDIUM] compute/lib/holographic_dmod_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_holographic_dmod_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_holographic_dmod_purity.py` to `compute/tests/test_holographic_dmod_purity_engine.py`.
- [MEDIUM] compute/lib/integrable_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_integrable_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_integrable_genus2.py` to `compute/tests/test_integrable_genus2_engine.py`.
- [MEDIUM] compute/lib/kac_chevalley_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_kac_chevalley.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_kac_chevalley.py` to `compute/tests/test_kac_chevalley_test.py`.
- [MEDIUM] compute/lib/lattice_genus2_universality_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_lattice_genus2_universality.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_lattice_genus2_universality.py` to `compute/tests/test_lattice_genus2_universality_engine.py`.
- [MEDIUM] compute/lib/mc4_stage4_resolution.py:1 — PROBLEM: No exact matching test file exists; the direct unit coverage lives in `compute/tests/test_mc4_defect_vanishing.py`. FIX: rename `compute/tests/test_mc4_defect_vanishing.py` to `compute/tests/test_mc4_stage4_resolution.py`.
- [MEDIUM] compute/lib/mc_crossing_theorem_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mc_crossing_theorem.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mc_crossing_theorem.py` to `compute/tests/test_mc_crossing_theorem_engine.py`.
- [MEDIUM] compute/lib/mg_genus2_clutching_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_genus2_clutching.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_genus2_clutching.py` to `compute/tests/test_mg_genus2_clutching_engine.py`.
- [MEDIUM] compute/lib/mg_harer_stability_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_harer_stability.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_harer_stability.py` to `compute/tests/test_mg_harer_stability_engine.py`.
- [MEDIUM] compute/lib/mg_kuranishi_parity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_kuranishi_parity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_kuranishi_parity.py` to `compute/tests/test_mg_kuranishi_parity_engine.py`.
- [MEDIUM] compute/lib/mg_tautological_purity_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_tautological_purity.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_tautological_purity.py` to `compute/tests/test_mg_tautological_purity_engine.py`.
- [MEDIUM] compute/lib/mg_w3_genus2_graph_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_mg_w3_genus2_graph.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_mg_w3_genus2_graph.py` to `compute/tests/test_mg_w3_genus2_graph_engine.py`.
- [MEDIUM] compute/lib/modular_periodicity_test.py:1 — PROBLEM: The dedicated coverage sits in `compute/tests/test_modular_periodicity_conjecture.py`, while `compute/tests/test_modular_periodicity.py` targets a different module. FIX: rename `compute/tests/test_modular_periodicity_conjecture.py` to `compute/tests/test_modular_periodicity_test.py`.
- [MEDIUM] compute/lib/multigen_universality_attack.py:1 — PROBLEM: The module is covered through the misnamed dedicated suite `compute/tests/test_multigen_universality_proof.py`, so the exact `test_<module>.py` file is still missing. FIX: rename `compute/tests/test_multigen_universality_proof.py` to `compute/tests/test_multigen_universality_attack.py`.
- [MEDIUM] compute/lib/n2_sca_chiral_bar_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_n2_sca_chiral_bar.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_n2_sca_chiral_bar.py` to `compute/tests/test_n2_sca_chiral_bar_engine.py`.
- [MEDIUM] compute/lib/n2_sca_chiral_bar_weight_graded_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_n2_sca_chiral_bar_weight_graded.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_n2_sca_chiral_bar_weight_graded.py` to `compute/tests/test_n2_sca_chiral_bar_weight_graded_engine.py`.
- [MEDIUM] compute/lib/niemeier_multichannel.py:1 — PROBLEM: No exact matching test file exists; `compute/tests/test_multichannel_shadow.py` mixes `niemeier_multichannel.py` assertions with a different module. FIX: add `compute/tests/test_niemeier_multichannel.py` and move the Niemeier-specific assertions out of `test_multichannel_shadow.py`.
- [MEDIUM] compute/lib/offdiag_newton_test.py:1 — PROBLEM: This module is covered through `compute/tests/test_offdiag_newton.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_offdiag_newton.py` to `compute/tests/test_offdiag_newton_test.py`.
- [MEDIUM] compute/lib/operadic_koszul_genus2_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_operadic_koszul_genus2.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_operadic_koszul_genus2.py` to `compute/tests/test_operadic_koszul_genus2_engine.py`.
- [MEDIUM] compute/lib/ordered_trace_invariant_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_ordered_trace_invariant.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_ordered_trace_invariant.py` to `compute/tests/test_ordered_trace_invariant_engine.py`.
- [MEDIUM] compute/lib/rectangular_w_algebra_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_rectangular_w_algebra.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_rectangular_w_algebra.py` to `compute/tests/test_rectangular_w_algebra_engine.py`.
- [MEDIUM] compute/lib/sft_graph_complex_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_sft_graph_complex.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_sft_graph_complex.py` to `compute/tests/test_sft_graph_complex_engine.py`.
- [MEDIUM] compute/lib/siegel_eisenstein.py:1 — PROBLEM: No exact matching test file exists; coefficient and product checks are scattered across several Siegel and E8 suites instead of `compute/tests/test_siegel_eisenstein.py`. FIX: add `compute/tests/test_siegel_eisenstein.py` and move the direct module checks there.
- [MEDIUM] compute/lib/tautological_genus2_numerical_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_tautological_genus2_numerical.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_tautological_genus2_numerical.py` to `compute/tests/test_tautological_genus2_numerical_engine.py`.
- [MEDIUM] compute/lib/toroidal_bar.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_toroidal.py`. FIX: rename `compute/tests/test_toroidal.py` to `compute/tests/test_toroidal_bar.py`.
- [MEDIUM] compute/lib/vertex_algebra_extensions_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_vertex_algebra_extensions.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_vertex_algebra_extensions.py` to `compute/tests/test_vertex_algebra_extensions_engine.py`.
- [MEDIUM] compute/lib/w3_bar_extended.py:1 — PROBLEM: No exact matching test file exists; the dedicated suite is still named `compute/tests/test_w3_extended.py`. FIX: rename `compute/tests/test_w3_extended.py` to `compute/tests/test_w3_bar_extended.py`.
- [MEDIUM] compute/lib/w4_ds_ope.py:1 — PROBLEM: No exact matching test file exists; direct `w4_ds_ope.py` assertions are scattered across multiple W4 suites and mixed with `w4_ds_ope_extraction.py`. FIX: add `compute/tests/test_w4_ds_ope.py` and move the direct Miura/Wick assertions there.
- [MEDIUM] compute/lib/w_algebra_transport_propagation.py:1 — PROBLEM: No exact matching test file exists; direct checks of this module are mixed into broader transpose and DS suites. FIX: add `compute/tests/test_w_algebra_transport_propagation.py` and move the direct module assertions there.
- [MEDIUM] compute/lib/wp_koszulness_definitive_engine.py:1 — PROBLEM: This engine is covered through `compute/tests/test_wp_koszulness_definitive.py`, but the exact matching file is missing. FIX: rename `compute/tests/test_wp_koszulness_definitive.py` to `compute/tests/test_wp_koszulness_definitive_engine.py`.

## Summary
Checked: 1325 | Findings: 65 | Verdict: FAIL
tokens used
136,801
