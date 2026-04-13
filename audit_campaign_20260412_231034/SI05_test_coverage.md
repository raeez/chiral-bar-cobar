# SI05_test_coverage (267s, gpt-5.4)

- [HIGH] compute/lib/euler_koszul_moments.py:1 — Exact companion test `compute/tests/test_euler_koszul_moments.py` is absent, and `rg -n "euler_koszul_moments" compute/tests` returned no hits.
- [HIGH] compute/lib/feynman_integral_engine.py:1 — Exact companion test `compute/tests/test_feynman_integral_engine.py` is absent, and `rg -n "feynman_integral_engine" compute/tests` returned no hits.
- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — Exact companion test `compute/tests/test_genus1_arithmetic_shadow.py` is absent, and `rg -n "genus1_arithmetic_shadow" compute/tests` returned no hits.
- [HIGH] compute/lib/graph_complex_cohomology_engine.py:1 — Exact companion test `compute/tests/test_graph_complex_cohomology_engine.py` is absent, and `rg -n "graph_complex_cohomology_engine" compute/tests` returned no hits.
- [HIGH] compute/lib/lattice_genus2_theta.py:1 — Exact companion test `compute/tests/test_lattice_genus2_theta.py` is absent; the only hit in `compute/tests` is a textual mention at `compute/tests/test_theorem_genus2_sl3_partition_engine.py:15`, not an import/use site.
- [MEDIUM] compute/lib/abjm_holographic_datum.py:1 — Exact companion test `compute/tests/test_abjm_holographic_datum.py` is absent; the module appears indirectly exercised in `compute/tests/test_twisted_holography_comparison_engine.py:937` and `compute/tests/test_twisted_holography_engine.py:651`.
- [MEDIUM] compute/lib/e8_lattice_bar.py:1 — Exact companion test `compute/tests/test_e8_lattice_bar.py` is absent; the module is imported indirectly in multiple tests, e.g. `compute/tests/test_e8_lattice.py:10` and `compute/tests/test_bar_cohomology_lattice_explicit_engine.py:607`.
- [MEDIUM] compute/lib/graph_complex_orientation_database.py:1 — Exact companion test `compute/tests/test_graph_complex_orientation_database.py` is absent; the module is imported indirectly at `compute/tests/test_graph_complex_orientation.py:18`.
- [LOW] compute/lib/alpha_g_simple_lie_verification_engine.py:1 — Exact companion test `compute/tests/test_alpha_g_simple_lie_verification_engine.py` is absent, but same-stem test `compute/tests/test_alpha_g_simple_lie_verification.py` exists.
- [LOW] compute/lib/arithmetic_comparison_test.py:1 — Exact companion test `compute/tests/test_arithmetic_comparison_test.py` is absent, but same-stem test `compute/tests/test_arithmetic_comparison.py` exists.
- [LOW] compute/lib/bar_graph_complex_bridge_engine.py:1 — Exact companion test `compute/tests/test_bar_graph_complex_bridge_engine.py` is absent, but same-stem test `compute/tests/test_bar_graph_complex_bridge.py` exists.
- [LOW] compute/lib/bethe_tq_relation_engine.py:1 — Exact companion test `compute/tests/test_bethe_tq_relation_engine.py` is absent, but same-stem test `compute/tests/test_bethe_tq_relation.py` exists.
- [LOW] compute/lib/bv_brst_purity_engine.py:1 — Exact companion test `compute/tests/test_bv_brst_purity_engine.py` is absent, but same-stem test `compute/tests/test_bv_brst_purity.py` exists.
- [LOW] compute/lib/cohft_dr_hierarchy_engine.py:1 — Exact companion test `compute/tests/test_cohft_dr_hierarchy_engine.py` is absent, but same-stem test `compute/tests/test_cohft_dr_hierarchy.py` exists.
- [LOW] compute/lib/cohft_givental_rmatrix_engine.py:1 — Exact companion test `compute/tests/test_cohft_givental_rmatrix_engine.py` is absent, but same-stem test `compute/tests/test_cohft_givental_rmatrix.py` exists.
- [LOW] compute/lib/cohft_string_genus2_engine.py:1 — Exact companion test `compute/tests/test_cohft_string_genus2_engine.py` is absent, but same-stem test `compute/tests/test_cohft_string_genus2.py` exists.
- [LOW] compute/lib/cohft_toprec_string_engine.py:1 — Exact companion test `compute/tests/test_cohft_toprec_string_engine.py` is absent, but same-stem test `compute/tests/test_cohft_toprec_string.py` exists.
- [LOW] compute/lib/cohft_virasoro_constraints_engine.py:1 — Exact companion test `compute/tests/test_cohft_virasoro_constraints_engine.py` is absent, but same-stem test `compute/tests/test_cohft_virasoro_constraints.py` exists.
- [LOW] compute/lib/coxeter_anomaly_test.py:1 — Exact companion test `compute/tests/test_coxeter_anomaly_test.py` is absent, but same-stem test `compute/tests/test_coxeter_anomaly.py` exists.
- [LOW] compute/lib/delta_fg_degree_pattern_engine.py:1 — Exact companion test `compute/tests/test_delta_fg_degree_pattern_engine.py` is absent, but same-stem test `compute/tests/test_delta_fg_degree_pattern.py` exists.
- [LOW] compute/lib/dmod_counterexample_search_engine.py:1 — Exact companion test `compute/tests/test_dmod_counterexample_search_engine.py` is absent, but same-stem test `compute/tests/test_dmod_counterexample_search.py` exists.
- [LOW] compute/lib/dmod_filtration_ss_engine.py:1 — Exact companion test `compute/tests/test_dmod_filtration_ss_engine.py` is absent, but same-stem test `compute/tests/test_dmod_filtration_ss.py` exists.
- [LOW] compute/lib/dmod_kl_purity_engine.py:1 — Exact companion test `compute/tests/test_dmod_kl_purity_engine.py` is absent, but same-stem test `compute/tests/test_dmod_kl_purity.py` exists.
- [LOW] compute/lib/dmod_mixed_hodge_bar_engine.py:1 — Exact companion test `compute/tests/test_dmod_mixed_hodge_bar_engine.py` is absent, but same-stem test `compute/tests/test_dmod_mixed_hodge_bar.py` exists.
- [LOW] compute/lib/dmod_purity_char_variety_engine.py:1 — Exact companion test `compute/tests/test_dmod_purity_char_variety_engine.py` is absent, but same-stem test `compute/tests/test_dmod_purity_char_variety.py` exists.
- [LOW] compute/lib/formality_obstruction_loop4_engine.py:1 — Exact companion test `compute/tests/test_formality_obstruction_loop4_engine.py` is absent, but same-stem test `compute/tests/test_formality_obstruction_loop4.py` exists.
- [LOW] compute/lib/holographic_dmod_purity_engine.py:1 — Exact companion test `compute/tests/test_holographic_dmod_purity_engine.py` is absent, but same-stem test `compute/tests/test_holographic_dmod_purity.py` exists.
- [LOW] compute/lib/integrable_genus2_engine.py:1 — Exact companion test `compute/tests/test_integrable_genus2_engine.py` is absent, but same-stem test `compute/tests/test_integrable_genus2.py` exists.
- [LOW] compute/lib/kac_chevalley_test.py:1 — Exact companion test `compute/tests/test_kac_chevalley_test.py` is absent, but same-stem test `compute/tests/test_kac_chevalley.py` exists.

Excluded false positive: `compute/lib/__init__.py:1` is a package initializer, not a compute engine; the shell heuristic flags it only because it matches `compute/lib/*.py`.

## Summary
Instances checked: 30 | Violations found: 29 | Verdict: FAIL


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
session id: 019d83cb-0f23-74d3-a758-f2a84499d5f0
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


Find compute engines without matching test files. Run: ls compute/lib/*.py | while read f; do base=$(basename $f .py); if [ ! -f compute/tests/test_${base}.py ]; then echo MISSING: $f; fi; done | head -30.

Report every finding with file:line.
mcp startup: no servers



thinking
**Navigating coding instructions**

I need to respond as a coding agent and inspect the repository without making modifications. Following AGENTS' instructions is important. I might need to read key files before executing the run command, though the task isn't about mathematical edits. It's focused on computing engines, so I need to run the command and report findings. I'll likely use the deep-beilinson-audit skill and maybe open the skill file, ensuring I provide commentary first. Trusting results seems essential, but this action might be straightforward.
thinking
**Running command for missing files**

I need to run the command and then identify the line numbers for any missing files, as the user specifically wants a `file:line` format. When using `ls compute/lib/*.py`, I'll see which paths are missing corresponding tests. If a test file is absent, there isn't a file to reference, but I might report line 1 as representative since it indicates a broader issue. It's essential to check the actual file contents and summarize the command's output, ensuring every finding is reported correctly.
thinking
**Executing file check**

I’m considering using a command to identify missing test files by running `ls compute/lib/*.py` and checking for their corresponding test files. If a test file doesn't exist, I'll echo a message indicating it’s missing. For line numbers, I might just reference line 1 for each compute file. Using `nl` could help, but I want to confirm if just pulling line 1 is sufficient. I’ll aim to run this and get the necessary outputs first.
codex
Using `deep-beilinson-audit` for this turn because the request is an adversarial audit. I’m starting with the exact shell check you specified, then I’ll verify each reported engine against the filesystem and cite concrete `file:line` locations from the engine sources.
exec
/bin/zsh -lc 'ls compute/lib/*.py | while read f; do base=$(basename $f .py); if [ ! -f compute/tests/test_${base}.py ]; then echo MISSING: $f; fi; done | head -30' in /Users/raeez/chiral-bar-cobar succeeded in 2.12s:
MISSING: compute/lib/__init__.py
MISSING: compute/lib/abjm_holographic_datum.py
MISSING: compute/lib/alpha_g_simple_lie_verification_engine.py
MISSING: compute/lib/arithmetic_comparison_test.py
MISSING: compute/lib/bar_graph_complex_bridge_engine.py
MISSING: compute/lib/bethe_tq_relation_engine.py
MISSING: compute/lib/bv_brst_purity_engine.py
MISSING: compute/lib/cohft_dr_hierarchy_engine.py
MISSING: compute/lib/cohft_givental_rmatrix_engine.py
MISSING: compute/lib/cohft_string_genus2_engine.py
MISSING: compute/lib/cohft_toprec_string_engine.py
MISSING: compute/lib/cohft_virasoro_constraints_engine.py
MISSING: compute/lib/coxeter_anomaly_test.py
MISSING: compute/lib/delta_fg_degree_pattern_engine.py
MISSING: compute/lib/dmod_counterexample_search_engine.py
MISSING: compute/lib/dmod_filtration_ss_engine.py
MISSING: compute/lib/dmod_kl_purity_engine.py
MISSING: compute/lib/dmod_mixed_hodge_bar_engine.py
MISSING: compute/lib/dmod_purity_char_variety_engine.py
MISSING: compute/lib/e8_lattice_bar.py
codex
The initial scan produced no immediate rows, so I’m polling the command and then checking the directory layout directly to distinguish “no missing tests” from shell/glob edge cases.
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg --files compute/lib compute/tests' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
 succeeded in 52ms:
Total output lines: 2723

compute/tests/test_shadow_period_integral_engine.py
compute/tests/test_w6_shadow_tower.py
compute/tests/test_bc_topological_recursion_shadow_engine.py
compute/tests/test_mg_genus2_clutching.py
compute/tests/test_cohft_vertex_engine.py
compute/tests/test_shadow_tower_atlas.py
compute/tests/test_modular_master.py
compute/tests/test_exceptional_shadow_engine.py
compute/tests/test_pixton_planted_forest.py
compute/tests/test_core_pillars.py
compute/tests/test_gap_closure.py
compute/tests/test_bv_bar_class_c_engine.py
compute/tests/test_chiral_bar_cohomology.py
compute/tests/test_gap_d_allgenera.py
compute/tests/test_nonprincipal_ds_normalization.py
compute/tests/test_csft_from_bar.py
compute/tests/test_chiral_bar_differential.py
compute/tests/test_modular_entanglement_flow_engine.py



thinking
**Verifying test file matches**

I need to report findings, but I should verify any missing tests with the actual files since the command output is limited to 30 entries. The user asked me to find compute engines without corresponding test files, but this command likely only retrieves the first 30 entries. I need to check if any test files exist for each engine. I might consider noting that some engines have alternate test names that don’t follow the exact naming convention.
thinking
**Auditing compute engines**

I need to audit the "compute engines without matching test files," which means I’m looking for exact `test_${base}.py` files. However, I should note that some engines might have semantically similar tests that don't match the names. The user's command is clear about the criteria. I'll mention that some reported missing files could actually have corresponding tests that just aren't named exactly right, which might cause an over-report of missing tests. I'll clarify that my findings are based on the exact filename criterion and assess the severity of any discrepancies.
thinking
**Using the skill for guidance**

I think it’s a good idea to open the skill since the instructions say I should use it if the task clearly matches. Even if it might not seem necessary, I want to be thorough. I'll check the SKILL.md document now. Since there are no edits required, I can just stick to the instructions laid out in the skill. I’ll read just enough to get the guidance I need to proceed effectively!
codex
The shell check returned 30 candidate violations under the repo’s exact filename convention. I’m now verifying two things for each candidate: the engine file exists at the cited path, and `compute/tests/test_<base>.py` is genuinely absent so the final report has no false positives.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

exec
/bin/zsh -lc 'for f in compute/lib/__init__.py compute/lib/abjm_holographic_datum.py compute/lib/alpha_g_simple_lie_verification_engine.py compute/lib/arithmetic_comparison_test.py compute/lib/bar_graph_complex_bridge_engine.py compute/lib/bethe_tq_relation_engine.py compute/lib/bv_brst_purity_engine.py compute/lib/cohft_dr_hierarchy_engine.py compute/lib/cohft_givental_rmatrix_engine.py compute/lib/cohft_string_genus2_engine.py compute/lib/cohft_toprec_string_engine.py compute/lib/cohft_virasoro_constraints_engine.py compute/lib/coxeter_anomaly_test.py compute/lib/delta_fg_degree_pattern_engine.py compute/lib/dmod_counterexample_search_engine.py compute/lib/dmod_filtration_ss_engine.py compute/lib/dmod_kl_purity_engine.py compute/lib/dmod_mixed_hodge_bar_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/e8_lattice_bar.py compute/lib/euler_koszul_moments.py compute/lib/feynman_integral_engine.py compute/lib/formality_obstruction_loop4_engine.py compute/lib/genus1_arithmetic_shadow.py compute/lib/graph_complex_cohomology_engine.py compute/lib/graph_complex_orientation_database.py compute/lib/holographic_dmod_purity_engine.py compute/lib/integrable_genus2_engine.py compute/lib/kac_chevalley_test.py compute/lib/lattice_genus2_theta.py; do base=$(basename "$f" .py); t="compute/tests/test_${base}.py"; if [ -f "$t" ]; then echo PRESENT:$t; else echo ABSENT:$t; fi; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for f in compute/lib/__init__.py compute/lib/abjm_holographic_datum.py compute/lib/alpha_g_simple_lie_verification_engine.py compute/lib/arithmetic_comparison_test.py compute/lib/bar_graph_complex_bridge_engine.py compute/lib/bethe_tq_relation_engine.py compute/lib/bv_brst_purity_engine.py compute/lib/cohft_dr_hierarchy_engine.py compute/lib/cohft_givental_rmatrix_engine.py compute/lib/cohft_string_genus2_engine.py compute/lib/cohft_toprec_string_engine.py compute/lib/cohft_virasoro_constraints_engine.py compute/lib/coxeter_anomaly_test.py compute/lib/delta_fg_degree_pattern_engine.py compute/lib/dmod_counterexample_search_engine.py compute/lib/dmod_filtration_ss_engine.py compute/lib/dmod_kl_purity_engine.py compute/lib/dmod_mixed_hodge_bar_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/e8_lattice_bar.py compute/lib/euler_koszul_moments.py compute/lib/feynman_integral_engine.py compute/lib/formality_obstruction_loop4_engine.py compute/lib/genus1_arithmetic_shadow.py compute/lib/graph_complex_cohomology_engine.py compute/lib/graph_complex_orientation_database.py compute/lib/holographic_dmod_purity_engine.py compute/lib/integrable_genus2_engine.py compute/lib/kac_chevalley_test.py compute/lib/lattice_genus2_theta.py; do if [ -f "$f" ]; then line=$(sed -n '"'1p' \""'$f"); printf '"'%s:1:%s
' \""'$f" "$line"; else printf '"'MISSING_FILE:%s
' \""'$f"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 68ms:
ABSENT:compute/tests/test_graph_complex_cohomology_engine.py
ABSENT:compute/tests/test_graph_complex_orientation_database.py
ABSENT:compute/tests/test_holographic_dmod_purity_engine.py
ABSENT:compute/tests/test_integrable_genus2_engine.py
ABSENT:compute/tests/test_kac_chevalley_test.py
ABSENT:compute/tests/test_lattice_genus2_theta.py
 succeeded in 76ms:
compute/lib/formality_obstruction_loop4_engine.py:1:r"""Formality obstruction for chiral algebras from graph complex at loop order 4.
compute/lib/genus1_arithmetic_shadow.py:1:"""
compute/lib/graph_complex_cohomology_engine.py:1:"""
compute/lib/graph_complex_orientation_database.py:1:"""
compute/lib/holographic_dmod_purity_engine.py:1:r"""Holographic interpretation of D-module purity and its converse.
compute/lib/integrable_genus2_engine.py:1:r"""integrable_genus2_engine.py -- Integrable hierarchy approach to genus-2 free energy.
compute/lib/kac_chevalley_test.py:1:"""Kac-Chevalley test: does the Kac determinant factor through the
compute/lib/lattice_genus2_theta.py:1:r"""Genus-2 theta series for lattices: adversarial verification of F_2 = kappa * lambda_2^FP.
codex
The filename-convention violations are real: all 30 engine files exist, and all 30 corresponding `compute/tests/test_<base>.py` files are absent. I’m doing one more pass for second-order issues, namely whether any of these modules appear to have near-match tests under different names, so I can separate strict convention failures from likely untested engines.
exec
/bin/zsh -lc "sed -n '1,80p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 51ms:
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
 succeeded in 51ms:
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
**Evaluating test findings**

I'm looking at second-order issues with near-match tests. I could compute for each base and search for tests that contain a trimmed `_engine` or `_test`. My goal is to determine the severity of these findings—some might not be serious, while others could be categorized as LOW or HIGH depending on related tests. I need to check each candidate against tests with an efficient shell search, even though I thought about using Python. I’ll proceed with a shell loop.
thinking
**Classifying test file matches**

I'm considering whether to check if a file is imported or used, but the focus is on compute engines without matching test files. It might be best to classify them as MEDIUM due to convention violations. For instance, `alpha_g_simple_lie_verification_engine.py` could be MEDIUM since there's a near-match with `test_alpha_g_simple_lie_verification.py`. Others, like `arithmetic_comparison_test.py`, could be LOW due to naming issues. I should automate the search for similarly named tests by creating a shell loop to find tests without `_engine` or `_test`.
codex
I’ve isolated a second-order pattern: several “missing” engines do have plausibly corresponding tests under variant filenames, which means the strict `test_<base>.py` convention check is catching both genuine coverage gaps and naming-drift cases. I’m separating those now so the severity levels reflect actual risk rather than only filename mismatch.
exec
/bin/zsh -lc 'for f in compute/lib/__init__.py compute/lib/abjm_holographic_datum.py compute/lib/alpha_g_simple_lie_verification_engine.py compute/lib/arithmetic_comparison_test.py compute/lib/bar_graph_complex_bridge_engine.py compute/lib/bethe_tq_relation_engine.py compute/lib/bv_brst_purity_engine.py compute/lib/cohft_dr_hierarchy_engine.py compute/lib/cohft_givental_rmatrix_engine.py compute/lib/cohft_string_genus2_engine.py compute/lib/cohft_toprec_string_engine.py compute/lib/cohft_virasoro_constraints_engine.py compute/lib/coxeter_anomaly_test.py compute/lib/delta_fg_degree_pattern_engine.py compute/lib/dmod_counterexample_search_engine.py compute/lib/dmod_filtration_ss_engine.py compute/lib/dmod_kl_purity_engine.py compute/lib/dmod_mixed_hodge_bar_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/e8_lattice_bar.py compute/lib/euler_koszul_moments.py compute/lib/feynman_integral_engine.py compute/lib/formality_obstruction_loop4_engine.py compute/lib/genus1_arithmetic_shadow.py compute/lib/graph_complex_cohomology_engine.py compute/lib/graph_complex_orientation_database.py compute/lib/holographic_dmod_purity_engine.py compute/lib/integrable_genus2_engine.py compute/lib/kac_chevalley_test.py compute/lib/lattice_genus2_theta.py; do base=$(basename "$f" .py); stem=${base%_engine}; stem=${stem%_test}; echo "BASE:$base"; rg --files compute/tests | rg "/test_${stem}([._].*)?'"\\.py"'$|/test_.*${stem}.*'"\\.py"'$" || true; echo "--"; done' in /Users/raeez/chiral-bar-cobar succeeded in 408ms:
BASE:bv_brst_purity_engine
compute/tests/test_bv_brst_purity.py
--
BASE:cohft_dr_hierarchy_engine
compute/tests/test_cohft_dr_hierarchy.py
--
BASE:cohft_givental_rmatrix_engine
compute/tests/test_cohft_givental_rmatrix.py
--
BASE:cohft_string_genus2_engine
compute/tests/test_cohft_string_genus2.py
--
BASE:cohft_toprec_string_engine
compute/tests/test_cohft_toprec_string.py
--
BASE:cohft_virasoro_constraints_engine
compute/tests/test_cohft_virasoro_constraints.py
--
BASE:coxeter_anomaly_test
compute/tests/test_coxeter_anomaly.py

thinking
**Considering module tests**

I'm thinking about modules that don't have near-match tests. I wonder if their scores might be high because they are genuinely unpaired. However, there might be instances where some of these modules are included in broader tests. It could be useful to inspect this further to understand how they interact within the testing framework. Looking into these cases may reveal important insights!
codex
I’ve confirmed a split: 21 of the 30 are filename-drift cases with obvious near-match tests, while 9 currently show no obvious same-stem test file at all. I’m checking those 9 for indirect references in the test tree before assigning the highest severity.
exec
/bin/zsh -lc 'for stem in abjm_holographic_datum e8_lattice_bar euler_koszul_moments feynman_integral_engine genus1_arithmetic_shadow graph_complex_cohomology_engine graph_complex_orientation_database lattice_genus2_theta __init__; do echo "STEM:$stem"; rg -n "$stem" compute/tests || true; echo "--"; done' in /Users/raeez/chiral-bar-cobar succeeded in 147ms:
--
STEM:graph_complex_cohomology_engine
--
STEM:graph_complex_orientation_database
compute/tests/test_graph_complex_orientation.py:18:from compute.lib.graph_complex_orientation_database import (
--
STEM:lattice_genus2_theta
compute/tests/test_theorem_genus2_sl3_partition_engine.py:15:  lattice_genus2_theta.py, theorem_mc5_analytic_rectification_engine.py,
--
STEM:__init__
compute/tests/test_sn_bar_irrep_decomp_engine.py:575:            def __init__(self):
compute/tests/test_multi_weight_cross_channel_engine.py:503:            def __init__(self):
compute/tests/test_multi_weight_cross_channel_engine.py:519:            def __init__(self):
compute/tests/test_multi_weight_cross_channel_engine.py:555:            def __init__(self):
compute/tests/test_w4_ope_miura.py:30:# Load the module directly to avoid __init__.py import chain issues
compute/tests/test_w4_ope_miura.py:294:        """from_t and __init__ produce equivalent generators for matching t."""
compute/tests/test_w4_ope_miura.py:296:        # The __init__ path goes through alpha0_squared_from_c which may
--






thinking
**Evaluating import discrepancies**

Interesting. I notice some near-matches still have imports that I need to check. I should identify exact lines and adapt broad tests for classification. It might help to report strict filename mismatches and indirect references. For certain files like e8_lattice_bar, I've tested indirectly. I also need to consider low mentions of lattice_genus2_theta in comments. Overall, I should look into other near-match cases and compute line numbers for more significant insights. It's essential to document any findings effectively.
thinking
**Categorizing test references**

I could use the engine file and note the absent test path. It might help to gather line numbers for near-match tests to reference, possibly by using `rg -n` for specific test names. However, if I can mention exact existing test files in the description, I might not need to include line numbers. Since the user requested findings as file:line, I'll prioritize that. I should also decide on severity based on criteria like the absence of matching test files or indirect references from specific sources.
thinking
**Assessing import levels in tests**

I wonder if abjm_holographic_datum has explicit imports in tests, which could mean a lower rating. The graph_complex_orientation_database is imported by test_graph_complex_orientation.py, so that might also lower its significance. The e8_lattice_bar is heavily tested, which likely means a lower assessment too. I need to consider whether to include `__init__.py` since it's not an engine file; maybe I should exclude it? However, the user asked for every finding, so I need to report accordingly.
thinking
**Evaluating test file violations**

I’m working with a near-match test and noticing that the engine doesn’t have a matching test file, which feels like a genuine violation. The only potential false positive might be `__init__.py`, but it's included in the output because of the command run. The user wants a complete report, so I need to decide if I include it as a violation while noting it as a tooling false positive. Overall, it looks like I have 30 instances checked and maybe 29 violations, but I want to be careful in my reporting.
thinking
**Clarifying engine file violations**

Since `__init__.py` isn’t an actual engine file, I’m thinking that the command output might be too broad. I could mark it as a LOW violation since it's not really an engine, labeling it a "heuristic false positive." However, the output contract requires findings ordered by severity. I could include it as LOW and note that the shell heuristic overreports on package initializers. So, the summary might state 30 instances checked and 30 violations found, treating it like a violation.
thinking
**Investigating file classifications**

I'm considering whether there are non-engine modules among the files listed. These include `arithmetic_comparison_test.py`, `coxeter_anomaly_test.py`, and `kac_chevalley_test.py`, which all have names ending in `_test.py`. They're in a lib directory, so they might actually be library files misnamed as tests. It’s worth inspecting their content, especially the docstrings, to determine if they're compute engines. I’ll focus on the first few lines to evaluate their purpose more effectively.
codex
The main false-positive risk now is naming ambiguity inside `compute/lib`: `__init__.py` is clearly not an engine, and a few library modules themselves end in `_test.py`. I’m reading those headers so the final report distinguishes “missing convention test” from “module probably misclassified by the scan.”
exec
/bin/zsh -lc "sed -n '1,40p' compute/lib/__init__.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,40p' compute/lib/coxeter_anomaly_test.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,40p' compute/lib/kac_chevalley_test.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,40p' compute/lib/arithmetic_comparison_test.py" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
"""Chiral bar-cobar compute engine.

Core types and algebra constructors for the monograph's computational kernel.

Governing principle (Dual Imperative):
    Every computation serves a theorem. State the theorem FIRST, predict the
    answer, THEN compute. If mismatch: the THEORY is suspect, not the computation.
    Maximalist ambition (push for the most powerful results) is amplified by
    maximal truth-seeking (every numerical claim verified, every formula derived
    before it enters the manuscript). These are synergistic, not competing.

Usage:
    from compute.lib import OPEAlgebra, Generator
    from compute.lib import heisenberg_algebra, sl2_algebra, virasoro_algebra
    from compute.lib import GradedVectorSpace, ChainComplex
"""

# Core types
from compute.lib.utils import GradedVectorSpace, ChainComplex, partition_number, lambda_fp, F_g
from compute.lib.bar_complex import OPEAlgebra, Generator
 succeeded in 51ms:
"""Kac-Chevalley test: does the Kac determinant factor through the
Chevalley discriminant of the mode space?

For a Gram matrix G of dimension d with eigenvalues λ_1,...,λ_d:
  - Kac determinant = det(G) = ∏ λ_i  (A_0 invariant: product)
  - Chevalley discriminant = ∏_{i<j} (λ_i - λ_j)^2  (A_{d-1} invariant)
  - Characteristic polynomial discriminant = same as Chevalley discriminant

These are DIFFERENT invariants. The question is whether there is a
nontrivial algebraic relation between them as functions of c.

We test this at Virasoro levels 4 and 6, and W_3 level 4.
"""

from __future__ import annotations

from sympy import (
    Matrix, Rational, Symbol, expand, factor, simplify,
    poly, discriminant as sym_discriminant, resultant,
    sqrt, prod as symprod, Poly
 succeeded in 51ms:
"""Coxeter anomaly species: S_n representation theory of the shadow obstruction tower.

Tests two claims from raeeznotes95 against the established shadow obstruction tower:

CLAIM A (Coxeter anomaly): Shadow obstruction tower anomaly coefficients at arity n
carry a natural S_n sign-representation structure when lifted to multi-mode
variables m_1,...,m_n on the hyperplane sum(m_i) = 0. Specifically, the
sewing amplitude at arity n should be divisible by the Vandermonde
Delta_n = prod_{i<j}(m_i - m_j).

CLAIM B (Chevalley-shadow correlation): The Chevalley quotient geometry
Spec C[H_n]^{S_n} transitions from modular-curve type (n<=4) to cameral
type (n>=5), correlating with the G/L/C/M shadow depth classification.

METHOD: Lift the 1d shadow obstruction tower (virasoro_shadow_tower.py) to explicit
multi-mode variables and test S_n transformation properties directly.

Ground truth:
  - virasoro_shadow_tower.py: Sh_r coefficients on primary line
  - modular_shadow_tower.py: all-arity master equation
 succeeded in 51ms:
r"""
arithmetic_comparison_test.py — Attack on conj:arithmetic-comparison

Tests the arithmetic comparison conjecture: does the MC element Theta_A
CANONICALLY determine the arithmetic packet connection nabla^arith_A?

MATHEMATICAL ANALYSIS:

The conjecture (conj:arithmetic-comparison in arithmetic_shadows.tex) has
three parts:
  (i)   Theta_A canonically determines nabla^arith, functorially under qi
  (ii)  M_A^ss is the Hecke-semisimple quotient of activated graph amplitudes
  (iii) Res_{rho/2} Omega_A is computable from higher-genus MC data

PRECISE STATEMENT:
  Theta_A in MC(g^mod_A) is the bar-intrinsic MC element (thm:mc2-bar-intrinsic).
  nabla^arith is the meromorphic connection on M_A otimes O_C (def:arithmetic-
  packet-connection).  The conjecture: there exists a CANONICAL map
  Theta_A |-> nabla^arith, functorial under quasi-isomorphisms of chiral algebras.



thinking
**Verifying test files**

I’m realizing that the `_test.py` files are actually compute modules rather than test files. I might want to check the line numbers for near-match tests, though maybe it's not essential to include descriptions about alternative test files without line numbers. Citing the exact test file line could bolster my approach. It seems I have output with lines for some indirect references, and I should verify the counts for near-match and non-near-match categories to ensure accuracy.
thinking
**Classifying test files**

I’m working on classifying the tests and have identified a few with no exact matching test files or references in compute/tests, including `euler_koszul_moments`, `feynman_integral_engine`, and `genus1_arithmetic_shadow`. I think I should also look into `lattice_genus2_theta` since it has a comment mention. It might help to search specifically for relevant imports. I’ll check imports for modules such as `abjm`, `e8`, and `graph_complex_orientation_database` as well. For `abjm_holographic_datum`, I can't find a direct import related to an exact test. Let's analyze 9 of them more closely.
codex
The remaining risk classification depends on whether those 9 unmatched modules are actually exercised indirectly. I’m distinguishing direct imports from mere textual mentions so I don’t overstate “untested” when the module is covered through a broader integration test.
exec
/bin/zsh -lc 'for stem in abjm_holographic_datum e8_lattice_bar euler_koszul_moments feynman_integral_engine genus1_arithmetic_shadow graph_complex_cohomology_engine graph_complex_orientation_database lattice_genus2_theta; do echo "STEM:$stem"; rg -n "from .*${stem}|import .*${stem}|${stem}'"\\.\" compute/tests || true; echo \"--\"; done" in /Users/raeez/chiral-bar-cobar succeeded in 140ms:
--
STEM:graph_complex_cohomology_engine
--
STEM:graph_complex_orientation_database
compute/tests/test_graph_complex_orientation.py:18:from compute.lib.graph_complex_orientation_database import (
--
STEM:lattice_genus2_theta
compute/tests/test_theorem_genus2_sl3_partition_engine.py:15:  lattice_genus2_theta.py, theorem_mc5_analytic_rectification_engine.py,
--









thinking
**Checking test matches**

I need to inspect one file, probably just line 1, to verify exact matching tests for near-match cases and line numbers in alternate tests. The user specified using "head -30," so only the first 30 matches are reviewed. I'll mention this limited scope and note that the summary is "Instances checked: 30." It seems the verdict is a FAIL due to violations found, with specific counts for high, medium, and low-risk categories. Time to classify all 30 carefully!
thinking
**Inspecting import references**

I need to check if there are actual imports with different names. For `lattice_genus2_theta`, it only shows as a comment, so it’s likely high risk. I suspect `abjm_holographic_datum.py` is imported in tests without the `compute.lib.` prefix, indicating low to medium risk. For the medium category, I have files like `abjm_holographic_datum.py` and `e8_lattice_bar.py`, which have indirect imports covered under different names. I should classify these 21 files by severity since they may just be naming drift rather than a total lack of tests!
thinking
**Clarifying violation counts**

I need to clarify violation counts for the output. Should I mention "Instances checked: 30" and "Violations found: 30" or maybe 29? Since the `__init__` might be a false positive, it's tricky. If I count every command finding, I might go with 30, but if `__init__` isn’t a real violation, maybe I should say, "Violations found: 30 (29 real engine mismatches + 1 scan false positive)." The contract is simple, but I could list it as "Violations found: 30 | Verdict: FAIL" and note the false positive.
thinking
**Evaluating module tests**

I think there might be high-risk modules with no direct test references. The module `abjm_holographic_datum` has a direct import, whereas `lattice_genus2_theta` only has a comment mention. I should inspect the header of `compute/lib/lattice_genus2_theta.py` to understand its significance. The first line's docstring indicates it's an engine. I might need to search for imports using different object names from the module, since tests might import functions instead of the module name.
thinking
**Clarifying exclusions**

I think I need to mention that `__init__.py` might be excluded as a false positive. In that case, I could summarize by saying, "Excluded 1 false positive: compute/lib/__init__.py." But wait, should I include that in the output? The output contract didn’t specifically ask for this, so maybe I should reconsider including it. I want to keep it clear for the user, so I’ll think about how best to address that.
thinking
**Organizing summary lines**

I need to summarize 29 lines about 33 while keeping the total below 50-70 lines. That means I could go with 29 bullet points, possibly one exclusion for a total of 31 lines. I think I should order the lines by severity: high first, then medium, and lastly low. I'll mark the low ones if there's a convention drift. Specifically, it seems like I could break it down to 5 high, 3 medium, and 21 low. That's a more nuanced approach!
thinking
**Categorizing severity levels**

I'm thinking through how to categorize items based on severity. For the high category, I want to identify entries that have no exact matches or direct imports, like euler, feynman, and others. Medium would include items without exact matches but have indirect imports, such as abjm and e8_lattice_bar. For low, I consider those where an exact companion is absent, but a near-match exists, leading to about 21 entries. I’m wondering if more could fit in the medium section, especially with the `__init__` inclusion.
thinking
**Reviewing test classifications**

I'm considering how to classify tests. Should we include e8_lattice_bar as a medium instead of low, given that many tests import it? It seems reasonable. Abjm has no same-stem but is indirect, so that works. Graph_complex_orientation_database has a direct import but lacks same-stem, which is fine too. However, some low same-stem tests might have naming drift due to the `_engine` suffix being dropped. I think we should mention `test_arithmetic_comparison.py` as it has a corresponding same-stem test.
thinking
**Drafting findings summary**

The summary contract clearly states "Instances checked: N | Violations found: N | Verdict: PASS/FAIL." I think stating that "Instances checked: 30" could be beneficial, but it's not strictly necessary since the user specifically requested to run the command with "head -30." 

Including "Excluded scan false positive: compute/lib/__init__.py:1" before the summary seems like a good idea. It's important to make sure there's no extraneous commentary and to start directly with the findings. I'll draft this carefully.
codex
- [HIGH] compute/lib/euler_koszul_moments.py:1 — Exact companion test `compute/tests/test_euler_koszul_moments.py` is absent, and `rg -n "euler_koszul_moments" compute/tests` returned no hits.
- [HIGH] compute/lib/feynman_integral_engine.py:1 — Exact companion test `compute/tests/test_feynman_integral_engine.py` is absent, and `rg -n "feynman_integral_engine" compute/tests` returned no hits.
- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — Exact companion test `compute/tests/test_genus1_arithmetic_shadow.py` is absent, and `rg -n "genus1_arithmetic_shadow" compute/tests` returned no hits.
- [HIGH] compute/lib/graph_complex_cohomology_engine.py:1 — Exact companion test `compute/tests/test_graph_complex_cohomology_engine.py` is absent, and `rg -n "graph_complex_cohomology_engine" compute/tests` returned no hits.
- [HIGH] compute/lib/lattice_genus2_theta.py:1 — Exact companion test `compute/tests/test_lattice_genus2_theta.py` is absent; the only hit in `compute/tests` is a textual mention at `compute/tests/test_theorem_genus2_sl3_partition_engine.py:15`, not an import/use site.
- [MEDIUM] compute/lib/abjm_holographic_datum.py:1 — Exact companion test `compute/tests/test_abjm_holographic_datum.py` is absent; the module appears indirectly exercised in `compute/tests/test_twisted_holography_comparison_engine.py:937` and `compute/tests/test_twisted_holography_engine.py:651`.
- [MEDIUM] compute/lib/e8_lattice_bar.py:1 — Exact companion test `compute/tests/test_e8_lattice_bar.py` is absent; the module is imported indirectly in multiple tests, e.g. `compute/tests/test_e8_lattice.py:10` and `compute/tests/test_bar_cohomology_lattice_explicit_engine.py:607`.
- [MEDIUM] compute/lib/graph_complex_orientation_database.py:1 — Exact companion test `compute/tests/test_graph_complex_orientation_database.py` is absent; the module is imported indirectly at `compute/tests/test_graph_complex_orientation.py:18`.
- [LOW] compute/lib/alpha_g_simple_lie_verification_engine.py:1 — Exact companion test `compute/tests/test_alpha_g_simple_lie_verification_engine.py` is absent, but same-stem test `compute/tests/test_alpha_g_simple_lie_verification.py` exists.
- [LOW] compute/lib/arithmetic_comparison_test.py:1 — Exact companion test `compute/tests/test_arithmetic_comparison_test.py` is absent, but same-stem test `compute/tests/test_arithmetic_comparison.py` exists.
- [LOW] compute/lib/bar_graph_complex_bridge_engine.py:1 — Exact companion test `compute/tests/test_bar_graph_complex_bridge_engine.py` is absent, but same-stem test `compute/tests/test_bar_graph_complex_bridge.py` exists.
- [LOW] compute/lib/bethe_tq_relation_engine.py:1 — Exact companion test `compute/tests/test_bethe_tq_relation_engine.py` is absent, but same-stem test `compute/tests/test_bethe_tq_relation.py` exists.
- [LOW] compute/lib/bv_brst_purity_engine.py:1 — Exact companion test `compute/tests/test_bv_brst_purity_engine.py` is absent, but same-stem test `compute/tests/test_bv_brst_purity.py` exists.
- [LOW] compute/lib/cohft_dr_hierarchy_engine.py:1 — Exact companion test `compute/tests/test_cohft_dr_hierarchy_engine.py` is absent, but same-stem test `compute/tests/test_cohft_dr_hierarchy.py` exists.
- [LOW] compute/lib/cohft_givental_rmatrix_engine.py:1 — Exact companion test `compute/tests/test_cohft_givental_rmatrix_engine.py` is absent, but same-stem test `compute/tests/test_cohft_givental_rmatrix.py` exists.
- [LOW] compute/lib/cohft_string_genus2_engine.py:1 — Exact companion test `compute/tests/test_cohft_string_genus2_engine.py` is absent, but same-stem test `compute/tests/test_cohft_string_genus2.py` exists.
- [LOW] compute/lib/cohft_toprec_string_engine.py:1 — Exact companion test `compute/tests/test_cohft_toprec_string_engine.py` is absent, but same-stem test `compute/tests/test_cohft_toprec_string.py` exists.
- [LOW] compute/lib/cohft_virasoro_constraints_engine.py:1 — Exact companion test `compute/tests/test_cohft_virasoro_constraints_engine.py` is absent, but same-stem test `compute/tests/test_cohft_virasoro_constraints.py` exists.
- [LOW] compute/lib/coxeter_anomaly_test.py:1 — Exact companion test `compute/tests/test_coxeter_anomaly_test.py` is absent, but same-stem test `compute/tests/test_coxeter_anomaly.py` exists.
- [LOW] compute/lib/delta_fg_degree_pattern_engine.py:1 — Exact companion test `compute/tests/test_delta_fg_degree_pattern_engine.py` is absent, but same-stem test `compute/tests/test_delta_fg_degree_pattern.py` exists.
- [LOW] compute/lib/dmod_counterexample_search_engine.py:1 — Exact companion test `compute/tests/test_dmod_counterexample_search_engine.py` is absent, but same-stem test `compute/tests/test_dmod_counterexample_search.py` exists.
- [LOW] compute/lib/dmod_filtration_ss_engine.py:1 — Exact companion test `compute/tests/test_dmod_filtration_ss_engine.py` is absent, but same-stem test `compute/tests/test_dmod_filtration_ss.py` exists.
- [LOW] compute/lib/dmod_kl_purity_engine.py:1 — Exact companion test `compute/tests/test_dmod_kl_purity_engine.py` is absent, but same-stem test `compute/tests/test_dmod_kl_purity.py` exists.
- [LOW] compute/lib/dmod_mixed_hodge_bar_engine.py:1 — Exact companion test `compute/tests/test_dmod_mixed_hodge_bar_engine.py` is absent, but same-stem test `compute/tests/test_dmod_mixed_hodge_bar.py` exists.
- [LOW] compute/lib/dmod_purity_char_variety_engine.py:1 — Exact companion test `compute/tests/test_dmod_purity_char_variety_engine.py` is absent, but same-stem test `compute/tests/test_dmod_purity_char_variety.py` exists.
- [LOW] compute/lib/formality_obstruction_loop4_engine.py:1 — Exact companion test `compute/tests/test_formality_obstruction_loop4_engine.py` is absent, but same-stem test `compute/tests/test_formality_obstruction_loop4.py` exists.
- [LOW] compute/lib/holographic_dmod_purity_engine.py:1 — Exact companion test `compute/tests/test_holographic_dmod_purity_engine.py` is absent, but same-stem test `compute/tests/test_holographic_dmod_purity.py` exists.
- [LOW] compute/lib/integrable_genus2_engine.py:1 — Exact companion test `compute/tests/test_integrable_genus2_engine.py` is absent, but same-stem test `compute/tests/test_integrable_genus2.py` exists.
- [LOW] compute/lib/kac_chevalley_test.py:1 — Exact companion test `compute/tests/test_kac_chevalley_test.py` is absent, but same-stem test `compute/tests/test_kac_chevalley.py` exists.

Excluded false positive: `compute/lib/__init__.py:1` is a package initializer, not a compute engine; the shell heuristic flags it only because it matches `compute/lib/*.py`.

## Summary
Instances checked: 30 | Violations found: 29 | Verdict: FAIL
tokens used
47,727
