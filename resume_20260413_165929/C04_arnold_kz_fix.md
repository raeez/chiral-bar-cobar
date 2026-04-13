# C04_arnold_kz_fix (828s)

**Applied**
- PROBLEM at [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:4740), [same file](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7235), and [same file](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7542): the standalone still wrote KZ/shadow connections as `... d\log(...)` and later dropped `dz` entirely. EXACT edit applied: `\Omega_{ij}\,d\log(z_i-z_j)` -> `(\Omega_{ij}/(z_i-z_j))\,d(z_i-z_j)`, `\sum r_{ij}(z_{ij})\,d\log(z_{ij})` -> `\sum r_{ij}(z_{ij})\,dz_{ij}`, clarified `r_{ij}(z)=\Omega_{ij}/((h^\vee+k)z)`, and `d-\hbar\Omega/z` -> `d-(\hbar\Omega/z)\,dz`.
- PROBLEM at [ordered_bar_descent_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py:29), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py:275), and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py:360): Kohno/bar flat-connection comments used `d log(z)`. EXACT edit applied: rewrote them to `r(z)\,d(z)` or `dz_{ij}/z_{ij}`.
- PROBLEM at [dmod_filtration_ss_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/dmod_filtration_ss_engine.py:439), [theorem_dk0_evaluation_bridge_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_dk0_evaluation_bridge_engine.py:138), [primitive_kernel_full.py](/Users/raeez/chiral-bar-cobar/compute/lib/primitive_kernel_full.py:874), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/primitive_kernel_full.py:881), [theorem_three_way_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_three_way_r_matrix_engine.py:394), [twisted_gauge_defects_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_gauge_defects_engine.py:1283), [geometric_langlands_shadow_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/geometric_langlands_shadow_engine.py:1231), [kz_monodromy_arithmetic_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/kz_monodromy_arithmetic_engine.py:978), and [ordered_chiral_jones_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_chiral_jones_engine.py:25): KZ docstrings/strings still taught `\Omega\,d\log(z)`. EXACT edit applied: rewrote each to rational `dz/z` form, i.e. `(\Omega_{ij}/(z_i-z_j))\,d(z_i-z_j)`; in [ordered_chiral_jones_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_chiral_jones_engine.py:208) I also corrected the AP117 explanation to say `d\log(z_i-z_j)` is the Arnold bar coefficient, not the connection one-form.
- PROBLEM at [holographic_shadow_connection.py](/Users/raeez/chiral-bar-cobar/compute/lib/holographic_shadow_connection.py:7), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/holographic_shadow_connection.py:43), [large_n_twisted_holography.py](/Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py:166), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py:679), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py:697), [twisted_holography_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_engine.py:904), [hitchin_shadow_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/hitchin_shadow_engine.py:777), [twisted_holography_mc.py](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:58), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:718), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:787), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:819), [test_holographic_shadow_connection.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_holographic_shadow_connection.py:55), and [test_twisted_holography_mc.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_twisted_holography_mc.py:281): shadow/Heisenberg connection docs still used `d-\kappa\sum dlog(z_{ij})`. EXACT edit applied: rewrote them to `dz/z` form or `r(z_{ij})\,dz_{ij}` throughout.
- PROBLEM at [theorem_swiss_cheese_kontsevich_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_swiss_cheese_kontsevich_engine.py:468) and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_swiss_cheese_kontsevich_engine.py:477): the displayed/returned connection form was `kappa * d log(z1-z2)`. EXACT edit applied: changed both to `kappa * d(z1 - z2)/(z1 - z2)`.
- PROBLEM at [dmod_purity_char_variety_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/dmod_purity_char_variety_engine.py:671) and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/dmod_purity_char_variety_engine.py:713): the Heisenberg flat connection was still described with `d log(z_i-z_j)`. EXACT edit applied: `d + k * sum d log(z_i - z_j)` -> `d + k * sum d(z_i - z_j)/(z_i - z_j)`.
- PROBLEM at [e1_nonsplitting_obstruction_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/e1_nonsplitting_obstruction_engine.py:666): the `sl_2` KZ line still used `Omega_12 dlog(z12)` and `Omega_23 dlog(z23)`. EXACT edit applied: rewrote it as `(Omega_12/z12) dz12 + (Omega_23/z23) dz23`.
- PROBLEM at [bc_mzv_shadow_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:572) and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:1354): the KZ diagonal 1-form was still written with `d log`. EXACT edit applied: rewrote it as `dz/z - dz/(1-z)`.

**Blocked**
- PROBLEM at [bar-cobar-review.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2606), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2868), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:3246), [thqg_celestial_holography_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:615), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:1083), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:1289), [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:342), [log_ht_monodromy_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1525), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1787), [log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1402), [twisted_holography_quantum_gravity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1908), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1936), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2240), [introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1535), [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:1780), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1197), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1339), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5075), [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2524), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2667), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2750), [thqg_line_operators_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:502), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1112), and [preface_full_survey.tex](/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:514): verified AP117 violations remain. No edit applied because sibling repos are outside the writable root and the sandbox rejects those writes.
- PROBLEM at [log_ht_monodromy_engine.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:6), [same file](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:194), [same file](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:579), [holographic_ht_engine.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:925), [non_simply_laced_rmatrix.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/non_simply_laced_rmatrix.py:1031), and [test_semisimple_purity.py](/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_semisimple_purity.py:41): verified AP117 compute/docstring violations remain. No edit applied for the same sandbox reason.
- PROBLEM at [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:713) and [theory_drinfeld_chiral_center.tex](/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:372), [same file](/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:493): verified Vol III manuscript/notes violations remain. No edit applied because that repo is outside the writable root.
- PROBLEM at [kazhdan_lusztig_shadow.py](/Users/raeez/calabi-yau-quantum-groups/compute/lib/kazhdan_lusztig_shadow.py:332) and [twisted_holography_cy3_engine.py](/Users/raeez/calabi-yau-quantum-groups/compute/lib/twisted_holography_cy3_engine.py:779): verified Vol III compute/docstring violations remain. No edit applied because that repo is outside the writable root.

**Verification**
Targeted AP117 grep is now clean in `/Users/raeez/chiral-bar-cobar` except for unrelated arithmetic `d\log\Lambda(s)` connections on the `s`-line, and `python3 -m py_compile` passed on all edited Python files.


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
session id: 019d87e8-04a4-7de1-a227-4071f0647ddc
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Fix Arnold form vs KZ connection confusion (AP117).
Search ALL volumes for 'd\\log' near 'connection' or 'KZ' or '\\nabla'.
Connection is r(z)dz, NOT r(z) d log(z). Arnold d log(z_i-z_j) is bar coefficient only.
Fix each instance.
mcp startup: no servers
codex
Using `deep-beilinson-audit` plus `cross-volume-propagation`: I’m first reading the required repo-level constitutional files, then I’ll scan all three volumes for `d\log` used as a connection/KZ form and patch only the concrete confused instances.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits

 succeeded in 51ms:
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
 succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
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

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

codex
I’ve loaded the constitutional surface. Next step is a cross-volume grep to isolate live places where `d\\log` is being used as a connection form rather than as the Arnold/bar coefficient.
exec
/bin/zsh -lc "rg -n -C 3 -P '(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log|\\\\mathrm\\{d\\}\\\\log|\\\\operatorname\\{dlog\\}|dlog)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 3 -P '(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log|\\\\mathrm\\{d\\}\\\\log|\\\\operatorname\\{dlog\\}|dlog)' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 877

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex-141-\end{corollary}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex-142-
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex-143-\begin{proof}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:144:The conifold quiver has a single pair of bifundamental arrows. The OPE of the associated chiral algebra has poles of maximal order $2$ (simple pole in the $r$-matrix after the $d\log$ absorption ), so $S_r = 0$ for $r \geq 3$. The modular characteristic is $\kappa_{\mathrm{ch}} = \DT_{(1,0)} = 1$ (the single compact curve class).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex-145-\end{proof}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex-146-
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex-147-\noindent\textit{Verification}: 124 tests in \texttt{conifold\_bar\_complex.py} covering both-chamber bar complex dimensions through degree $12$, pentagon identity, gauge transformation at degrees $2$--$6$, and shadow depth classification.
--
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-91-\item $p_{\max}(A)$, the maximal pole order of generator-on-generator
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-92-OPEs (cf.\ Vol~I, Definition~\ref{def:p-max});
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-93-\item $k_{\max}(A) = p_{\max}(A) - 1$, the collision depth of $r_{CY}$
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:94:itself, after $d\log$-absorption (cf.\ Vol~I,
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-95-Definition~\ref{def:k-max});
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-96-\item $r_{\max}(A)$, the shadow depth, the degree at which the
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-97-obstruction tower $\Theta_A^{\leq r}$ terminates (Vol~I,
--
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-311- \;\in\; \cH(Q,W) \otimes \cH(Q,W) \,[\![z^{-1}]\!],
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-312-\]
 succeeded in 50ms:
Total output lines: 4229

/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-22-This is the E_1 core: ordered, associative, noncommutative. The bar complex, the Koszul dual, the line category.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-23-
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-24-### Rung 2: E_2 — Holomorphic + braided (1 complex dim) [Parts III-IV]
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:25:- **Formal disk D** (1 cpx dim, no boundary): Vertex algebra / chiral algebra. Holomorphic factorisation on FM_n(C). The OPE poles become A_inf operations via dlog extraction.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-26-- **Curve X** (1 cpx dim, no boundary): Chiral algebra on a curve. Ran space. Chiral homology = derived global sections of B(A) on Ran(X).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-27-- **Half-plane H** (1 cpx dim, boundary R = dH): Swiss-cheese geometry. Two-colour bar complex. Three collision types: bulk-bulk (FM_k(C)), boundary-boundary (Conf_m^<(R)), bulk-to-boundary (interior points approaching R).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-28-- **Disk D with boundary S^1**: Boundary conditions. Annular bar complex.
--
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-214-V2-AP32: Standalone-document artifact leak. Chapter .tex files \input{}'d into main.tex MUST NOT contain \title{}, \begin{abstract}, \tableofcontents, \date{}, \author{}. These cause silent rendering artifacts. Grep chapters/ for these after any file creation.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-215-V2-AP33: RECTIFICATION-FLAG must NOT become permanent debt. Every flag needs resolution or a tracked TODO with owner. Grep for RECTIFICATION-FLAG at session end; zero tolerance for unresolved flags.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-216-V2-AP34: Divided-power convention in lambda-brackets. Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12). W3: c/3*lambda^5 wrong, correct c/360.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:217:V2-AP35: Unresolved logical connectives after correction. When correcting a formula, audit ALL "therefore"/"hence"/"it follows" within 5 lines. A correction that changes the conclusion but leaves "therefore" pointing to old reasoning is a non-sequitur worse than the original error.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-218-
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-219-### From 100-Commit Archaeology (V2-AP36-39, April 2026)
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md-220-V2-AP36: Terminology rename atomicity. When renaming terminology X -> Y: (1) enumerate ALL variant forms (X, "X tower", "X Postnikov", compound forms), (2) grep all three volumes including compute/, audit/, *.md, (3) complete ALL replacements in a SINGLE commit, (4) verify zero residual hits before committing. The "shadow Postnikov tower" -> "shadow obstruction tower" rename required 5 commits (114 + 27 + 4 + 1 + 1 files). Follow-up cleanup commits are evidence of incomplete propagation.
--
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md-59-
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md-60-## Programme Identity
exec
/bin/zsh -lc "rg -n -C 3 -P '(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log|\\\\mathrm\\{d\\}\\\\log|\\\\operatorname\\{dlog\\}|dlog)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 8269

/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-650-
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-651-\begin{proof}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-652-The Gauss--Manin connection acts on bar elements by variation
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:653:of the bar propagator $d\log E(z,w)$ with respect to moduli.
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-654-The variation is a holomorphic $(1,0)$-form on~$\overline\cM_g$
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-655-valued in operators on~$H_q$; the HS bound on the pair-of-pants
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-656-multiplication controls the operator norm of these
--
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-1868-The Virasoro algebra~$\Vir_c$ has $\dim H_n = p(n)$.  The OPE
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-1869-$T(z)T(w) \sim (c/2)(z-w)^{-4} + 2T(w)(z-w)^{-2}
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-1870-+ \partial T(w)(z-w)^{-1}$
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:1871:is quartic (the $r$-matrix has cubic pole by $d\log$-absorption,
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-1872-per the pole relation $\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$).
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-1873-Repeated normal products give $|C| \leq K(n+1)^2$ with
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-1874-$N = 2$.  The criterion applies at every central charge~$c$.
--
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-2543-component of the propagator vanishes on~$\bC$.
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex-2544-

thinking
**Evaluating connection formulas**

I'm delving into the connection represented by `r(z_{ij}) dz_{ij}`. I think Arnold's dlog might just be a bar coefficient. I’ll need to update every instance where the connection uses r(z) dlog. It might also be necessary to adjust normalization if the formula incorporates Omega or r_{ij}. I need to clarify the exact conventions from my sources, so I'll search for AP117 and look for specific statements related to that.
codex
The broad `d\\log` sweep is noisy, so I’m narrowing to the AP117 surface: files where `d\\log` appears in the same local paragraph as `connection`, `KZ`, or `\\nabla`, then I’ll patch only the genuine connection-form confusions.
exec
/bin/zsh -lc "rg -n -C 3 -P '(connection|KZ|\\\\nabla).{0,120}(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log)|(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log).{0,120}(connection|KZ|\\\\nabla)' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 3 -P '(connection|KZ|\\\\nabla).{0,120}(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log)|(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log).{0,120}(connection|KZ|\\\\nabla)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex-1286-\]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex-1287-Thus the affine soft tower has no nonzero terms beyond the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex-1288-leading KZ-form term and the cubic shadow:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:1289:$\nabla = d - \frac{1}{k+h^\vee}\sum_{i<j} \Omega_{ij} d\log(z_i - z_j)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex-1290-- S_3(\widehat{\mathfrak{g}}_k)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex-1291-On the affine Kac--Moody comparison surface, the leading degree-$2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex-1292-term is the KZ connection form, and the resulting finite-depth affine
--
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex-2664-\;\otimes\; \mathbf{1}_{E_1(2)},
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex-2665-\end{equation}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex-2666-where $\Omega_{12}$ acts on the two open-colour tensor factors
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2667:and $d\log(u_1 - u_2)$ is the KZ connection form on the ordered
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex-2668-configuration space $\Conf_2^{\mathrm{ord}}(\A^1)$ of the two
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex-2669-spectral parameters. The closed-colour input $z$ has been
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex-2670-absorbed into the spectral difference $u_1 - u_2$ by
--
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex-76- \SN_n^2 = I_{(\ds+\Theta_n)\Gamma_n+\MC(\Gamma_n)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex-77- \]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex-78- Hence flatness is equivalent to a supportwise Maurer-Cartan hierarchy and yields a recursive obstruction theory for higher collision homotopies.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:79: \item In a quasi-linear interacting three-dimensional holomorphic-topological theory with anomaly-free perturbation theory, renormalized compactified graph integrals on mixed logarithmic configuration spaces produce an analytic logarithmic superconnection of the same form, and its flatness is a compactified-Stokes identity.
exec
/bin/zsh -lc "rg -n -C 3 -P '(connection|KZ|\\\\nabla).{0,120}(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log)|(d\\\\log|d\\\\,\\\\log|d\\\\"'!'"\\\\log|d\\s*log).{0,120}(connection|KZ|\\\\nabla)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-369-\[
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-370- R \;=\; \mathcal{P}\exp\Bigl(\int_\gamma \Omega_{\mathrm{KZ}}\Bigr) \;\in\; \Uq(\frakg) \hat{\otimes} \Uq(\frakg)
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-371-\]
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:372:where $\Omega_{\mathrm{KZ}} = \sum_a I^a \otimes I_a \cdot d\log(z_1 - z_2)/(k + h^\vee)$ is the KZ connection and $\gamma$ is the winding path. This is the Drinfeld--Kohno theorem at the level of the factorization algebra.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-373-\end{remark}
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-374-
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-375-
--
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-490-
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-491-\smallskip\noindent\textbf{(b) Drinfeld--Kohno theorem.} Drinfeld (1989) and Kohno (1987) proved that the monodromy representation of the KZ equations
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-492-\[
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:493: \nabla_{\mathrm{KZ}} \;=\; d - \frac{1}{k + h^\vee} \sum_{i < j} \Omega_{ij}\, d\log(z_i - z_j)
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-494-\]
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-495-(where $\Omega_{ij} = \sum_a I^a_i \otimes I_{a,j}$ is the Casimir) gives a representation of the braid group $B_n$ that factors through $\Uq(\frakg)$ at $q = e^{\pi i / (k + h^\vee)}$.
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex-496-
--
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-710-The identification of Construction~\ref{constr:three-parameter-hbar}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-711-fails if any of the three parameters carries a hidden $2\pi i$ or
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex-712-$1/n!$. In particular, the KZ parameter is conventionally normalized
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:713:so that the connection $\nabla = d - \hbar^{-1}\sum_i r_{ij}\,d\log(z_i
 succeeded in 51ms:
Total output lines: 7779

/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_230832/F19_arnold_KZ.md-51-
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_230832/F19_arnold_KZ.md-52-MISSION: Verify every instance of Arnold vs KZ across all .tex files.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_230832/F19_arnold_KZ.md-53-
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_230832/F19_arnold_KZ.md:54:CANONICAL: KZ: sum r_{ij} dz_{ij}, NOT d log
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_230832/F19_arnold_KZ.md-55-CHECKS: Arnold form is bar coeff, NOT connection (AP117)
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_230832/F19_arnold_KZ.md-56-
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_230832/F19_arnold_KZ.md-57-STEPS:
--
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl-272-{"label": "prop:compactified-ternary-two-channel", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/feynman_diagrams.tex", "line": 370, "title": "Two-channel reduction after compactifying the\n ternary packet"}
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl-273-{"label": "cor:genus0-compactified-ternary-two-channel", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/feynman_diagrams.tex", "line": 410, "title": "Genus-\\texorpdfstring{$0$}{0} post-compactification ternary target", "refs_in_block": ["thm:brst-bar-genus0"]}
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl-274-{"label": "cor:genus0-standard-chart-two-residues", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/feynman_diagrams.tex", "line": 428, "title": "Standard-chart form of the remaining genus-\\texorpdfstring{$0$}{0}\n packet", "refs_in_block": ["thm:brst-bar-genus0"]}
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl:275:{"label": "prop:m04-standard-log-basis", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/feynman_diagrams.tex", "line": 449, "title": "Standard logarithmic basis on\n \\texorpdfstring{$\\overline{M}_{0,4}$}{M_0,4}"}
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl-276-{"label": "cor:genus0-two-coefficient-packet", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/feynman_diagrams.tex", "line": 496, "title": "Two-coefficient form of the remaining genus-\\texorpdfstring{$0$}{0}\n compactified packet", "refs_in_block": ["thm:brst-bar-genus0"]}
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl-277-{"label": "cor:genus0-named-coefficient-packet", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/feynman_diagrams.tex", "line": 555, "title": "Named coefficient form of the remaining genus-\\texorpdfstring{$0$}{0}\n compactified packet", "refs_in_block": ["thm:brst-bar-genus0", "def:genus0-mc5-coefficient-packet"]}
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl-278-{"label": "thm:loop-genus-formula", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/connections/feynman_diagrams.tex", "line": 611, "title": "Graph loop number and genus; {} \\cite{costello-renormalization}", "cites_in_block": ["costello-renormalization"]}
--
/Users/raeez/chiral-bar-cobar/AGENTS.md-442-```
/Users/raeez/chiral-bar-cobar/AGENTS.md-443-type: [connection 1-form / KZ / Arnold / bar propagator]



thinking
**Deciding scope for document edits**

The user indicates we should edit only assigned files, suggesting we focus on the compute documentation too if there's any confusion. I need to decide how to manage the scope effectively, possibly referencing the F19 audit which identified 15 violations in the .tex files. It seems the task requires searching across all volumes, including new compute libraries. I'll aim to find and correct issues using a practical approach, potentially leveraging scripting for thoroughness.
thinking
**Searching for formula patterns**

I think we should also consider including `archive` and `notes` if they're still live. I'm planning to search more specifically for wrong formula patterns like `\nabla.*d\log` and `KZ.*d\log`, as well as variations like `connection.*d\log` and `d\log.*connection`. I'll look for phrases like "connection form ... d\log" too. The goal is to target our search within live directories to make sure we catch everything necessary.
thinking
**Refining the search method**

I’m noticing that the search results don’t directly connect KZ with dlog. There are numerous mentions of dlog, but not necessarily linked to KZ. I could refine my search to target lines that specifically include KZ or its connections. It’s possible there are relevant entries in the working notes. I should create a list of files that match certain patterns while excluding audit, metadata, and healing to reduce noise. Using a command like `rg -l` for each repository sounds like a good plan.
codex
I’ve got a prior F19 audit inside Vol I that matches this AP exactly. I’m using it as a candidate list, then re-reading each live file in context to avoid “fixing” audit artifacts or already-correct logarithmic-boundary language.
exec
/bin/zsh -lc "rg -l -P '(\\\\nabla["'^'"\\n]{0,120}d\\\\log|KZ["'^'"\\n]{0,120}d\\\\log|connection["'^'"\\n]{0,120}d\\\\log|d\\\\log["'^'"\\n]{0,120}(KZ|connection|\\\\nabla))' /Users/raeez/chiral-bar-cobar --glob '"'!audit_campaign*'"' --glob '"'!healing_*'"' --glob '"'!metadata/*'"' --glob '"'!compute/audit/*'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -l -P '(\\\\nabla["'^'"\\n]{0,120}d\\\\log|KZ["'^'"\\n]{0,120}d\\\\log|connection["'^'"\\n]{0,120}d\\\\log|d\\\\log["'^'"\\n]{0,120}(KZ|connection|\\\\nabla))' /Users/raeez/chiral-bar-cobar-vol2 --glob '"'!audit_campaign*'"' --glob '"'!healing_*'"' --glob '"'!metadata/*'"' --glob '"'!compute/audit/*'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -l -P '(\\\\nabla["'^'"\\n]{0,120}d\\\\log|KZ["'^'"\\n]{0,120}d\\\\log|connection["'^'"\\n]{0,120}d\\\\log|d\\\\log["'^'"\\n]{0,120}(KZ|connection|\\\\nabla))' /Users/raeez/calabi-yau-quantum-groups --glob '"'!audit_campaign*'"' --glob '"'!healing_*'"' --glob '"'!metadata/*'"' --glob '"'!compute/audit/*'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/D15_hardcoded_parts.md
/Users/raeez/chiral-bar-cobar/resume_20260413_163457/S16_v1_to_v2_bridge.md
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex
/Users/raeez/chiral-bar-cobar/fix_wave_C_20260413_175943/C04_arnold_kz_fix.md
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U10_missing_computations.md
/Users/raeez/chiral-bar-cobar/fix_wave_C_20260413_175943/C01_bare_omega_v1.md
/Users/raeez/chiral-bar-cobar/fix_wave_C_20260413_175943/C10_rmatrix_xvol_consistency.md
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/S14_standalone_to_main.md
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/F18_dangling_refs_v2.md
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/D05_rmatrix_level.md
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A17_fix_status_mismatch_v2.md
/Users/raeez/chiral-bar-cobar/fix_wave_D_20260413_182434/D15_e1_einf_v2.md
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md
/Users/raeez/chiral-bar-cobar/resume_20260413_165929/F18_dangling_refs_v2.md
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B15_stale_cross_vol_refs_v3.md
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/standalone/stokes_gap_kzb_regularity.tex
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex
/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex

thinking
**Clarifying spectral variables**

I’m figuring out that this seems specific to the connection in spectral variables, rather than a general logarithmic connection based on the standard logarithm base. It's interesting to see how these elements interact—I'm curious how this might affect outcomes or further connections in related fields. It makes me wonder how I can better articulate these connections in a clear way. Just need to explore this a bit more!
codex
I’m now doing the line-by-line verification pass from the F19 candidate set. The key filter is: only `d\\log(z_i-z_j)` used as a KZ/shadow connection gets changed; genuine boundary-log terms like `dt/t` in plumbing coordinates stay.
exec
/bin/zsh -lc "sed -n '730,750p;2248,2260p;5088,5104p;6548,6556p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '740,748p;2178,2186p;2418,2425p;4858,4872p' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '108,122p;7480,7494p;952,964p;3448,3490p;230,242p;188,198p' chapters/theory/quantum_corrections.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/theory/e1_modular_koszul.tex chapters/frame/heisenberg_frame.tex chapters/connections/thqg_preface_supplement.tex appendices/_sl2_yangian_insert.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Motivic interpretation of ordered-to-symmetric descent]
\label{rem:motivic-interpretation}
\index{motivic interpretation!ordered bar complex}
\index{descent!motivic content}
\index{mixed Tate motives!configuration space periods}
The averaging map
$\mathrm{av}\colon\Barchord(A)\to\Barch(A)$
is a motivic projection: it kills precisely the transcendental
arithmetic content of the configuration-space integrals.

The ordered configuration space
$\mathrm{Conf}_k^{\mathrm{ord}}(\mathbb{C})$
carries a canonical mixed Hodge structure whose periods are
the iterated integrals of the Knizhnik--Zamolodchikov connection.
The $R$-matrix monodromy of
Proposition~\ref{sec:r-matrix-descent-vol1} is computed by these
periods, and the resulting transcendental data is stratified by
degree:
\begin{itemize}
\item At degree~$2$: the monodromy $R(z)$ of the flat connection
 succeeded in 51ms:
degree:
\begin{itemize}
\item At degree~$2$: the monodromy $R(z)$ of the flat connection
$\nabla = d - r(z)\,dz$ involves $2\pi i$, a period of
the Lefschetz motive~$\mathbb{L}$ (weight~$1$).

\item At degree~$3$: the Drinfeld associator
$\Phi_{\mathrm{KZ}}$
(the monodromy of the KZ connection on
constant~$k$ as the value of $d$ on the ground field copy
inside the symmetric bar. In the ordered complex the constant
is collected upstream in $m_0$, and the corresponding holonomy
on ordered configuration space is the R-matrix
$R(z)=e^{k\hbar/z}$
(Theorem~\ref{thm:heisenberg-rmatrix}).
The three pictures are equivalent presentations of the same
genus-zero datum $\kappa(\cH_k)=k$.
\end{remark}
$\mathcal{F}_{bc}$ has generators $b,c$ of weights
$(\lambda,1{-}\lambda)$ with
 exited 1 in 52ms:
sed: chapters/connections/thqg_preface_supplement.tex: No such file or directory

More precisely, we can view $d$ as a connection on the graded vector bundle:
\[\mathcal{E} = \bigoplus_{n,k} \mathcal{A}^{\boxtimes n} \otimes \Omega^k_{\log}\]

The flatness condition $d^2 = 0$ is equivalent to the Maurer--Cartan equation:
\[d\omega + \frac{1}{2}[\omega, \omega] = 0\]

where $\omega = \sum_{i<j} t_{ij}\, \eta_{ij}$ is the residue-valued logarithmic coefficient in the geometric bar differential, with $t_{ij} \in \mathrm{End}(\mathcal{A}^{\otimes n})$ acting on the $i$-th and $j$-th tensor factors via the chiral bracket and $\eta_{ij} = d\log(z_i - z_j)$ the Arnold form. The Arnold relations are precisely the conditions ensuring this equation holds.

\subsubsection{Concrete computation}

We verify this for $n = 3$. The differential acts on $a_1 \otimes a_2 \otimes a_3 \otimes \eta_{12}$ as:
\[d(a_1 \otimes a_2 \otimes a_3 \otimes \eta_{12}) = a_1 \otimes a_2 \otimes a_3 \otimes d\eta_{12} + \text{residue terms}\]

For $d^2 = 0$, we need:
At $z_1 = z_2$ (i.e.\ $u = 0$), the first and third terms
each have a simple pole in~$u$, with residues $\zeta(v)$ and
$\zeta(w) = \zeta(-v) = -\zeta(v)$ respectively; the second
term is regular. So the residue of~$S$ at $u = 0$ vanishes.

thinking
**Improving file command**

I've realized the previous command wasn’t effective because it handled multiple files without proper separators. Clearly, I need to refine my approach. I want to identify the correct path for the thqg_preface_supplement, possibly located in chapters/frame, but I need to ensure that the current context matches. The output got mixed up due to the interleaving of results from multiple files. I’ll use line numbering to keep things organized and possibly employ multi_tool parallel for efficiency.
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '952,966p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '7480,7496p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/quantum_corrections.tex | sed -n '108,122p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '3450,3492p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/_sl2_yangian_insert.tex | sed -n '188,198p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --files -g 'thqg_preface_supplement.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '736,748p;2248,2260p;5090,5104p;6548,6556p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/ordered_associative_chiral_kd.tex | sed -n '740,748p;2178,2188p;2418,2425p;4860,4872p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   108	
   109	More precisely, we can view $d$ as a connection on the graded vector bundle:
   110	\[\mathcal{E} = \bigoplus_{n,k} \mathcal{A}^{\boxtimes n} \otimes \Omega^k_{\log}\]
   111	
   112	The flatness condition $d^2 = 0$ is equivalent to the Maurer--Cartan equation:
   113	\[d\omega + \frac{1}{2}[\omega, \omega] = 0\]
   114	
   115	where $\omega = \sum_{i<j} t_{ij}\, \eta_{ij}$ is the residue-valued logarithmic coefficient in the geometric bar differential, with $t_{ij} \in \mathrm{End}(\mathcal{A}^{\otimes n})$ acting on the $i$-th and $j$-th tensor factors via the chiral bracket and $\eta_{ij} = d\log(z_i - z_j)$ the Arnold form. The Arnold relations are precisely the conditions ensuring this equation holds.
   116	
   117	\subsubsection{Concrete computation}
   118	
   119	We verify this for $n = 3$. The differential acts on $a_1 \otimes a_2 \otimes a_3 \otimes \eta_{12}$ as:
   120	\[d(a_1 \otimes a_2 \otimes a_3 \otimes \eta_{12}) = a_1 \otimes a_2 \otimes a_3 \otimes d\eta_{12} + \text{residue terms}\]
   121	
   122	For $d^2 = 0$, we need:
 succeeded in 51ms:
  7480	\textup{(}Theorem~\textup{\ref{thm:shadow-connection})} restricts to
  7481	the open stratum $\mathrm{Conf}_n(\mathbb{P}^1) \subset
  7482	\overline{\mathcal{M}}_{0,n}$ as
  7483	\begin{equation}\label{eq:kz-from-shadow}
  7484	\nabla^{\mathrm{KZ}}
  7485	= d - \frac{1}{k + h^\vee}
  7486	 \sum_{1 \le i < j \le n}
  7487	 \Omega_{ij}\, d(z_i - z_j)/(z_i - z_j)
  7488	\end{equation}
  7489	after choosing an affine coordinate on $\mathbb{P}^1$ and
  7490	fixing $z_n = \infty$. Here $\Omega_{ij} = \sum_a T^a_i \otimes (T_a)_j$
  7491	is the Casimir operator acting on the $i$-th and $j$-th tensor factors
  7492	of $V_1 \otimes \cdots \otimes V_{n-1}$.
  7493	
  7494	The KZ equation $\nabla^{\mathrm{KZ}} F = 0$ is therefore the
  7495	genus-$0$ flat-section equation of the shadow connection,
  7496	restricted to configuration space and evaluated in the representation
 succeeded in 51ms:
   952	neighbourhood of the $n$-fold diagonal in $D^n$. On a global
   953	curve $X$ of genus $g \ge 1$, the ordered chiral homology
   954	acquires additional structure from the Hodge bundle: the
   955	fiberwise differential satisfies
   956	$d^2_{\mathrm{fib}} = r(z) \cdot \omega_g$
   957	(matrix-valued in $\operatorname{End}(V^{\otimes 2})
   958	\otimes H^{2}(\overline{\cM}_g)$ at degree~$2$), which upon
   959	$\Sigma_2$-averaging reduces to the scalar curvature
   960	$d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$ of
   961	the symmetric theory.
   962	\end{remark}
   963	
   964	\begin{example}[Ordered chiral Hochschild of the Heisenberg]
   965	\label{ex:ord-ch-hoch-heisenberg}
   966	\index{Heisenberg algebra!ordered chiral Hochschild}
 succeeded in 50ms:
   188	\;+\;
   189	\susp^{-1}x\otimes \susp^{-1}[y,z].
   190	\]
   191	(The sign $+$ on the second term arises from $(-1)^{|\susp^{-1}x|}$.)
   192	The full bar differential on three-point ordered configurations
   193	incorporates the monodromy of the flat connection
   194	$\nabla=d-r(z_{ij})\,dz_{ij}$ on
   195	$\operatorname{Conf}_3^{\mathrm{ord}}(\bC)$, and the condition
   196	$d^2=0$ for this corrected differential is precisely the CYBE~\eqref{eq:cybe-sl2}.
   197	
   198	For $r(z)=\hbar\,\Omega/z$, the three commutator terms are:
 succeeded in 50ms:
  3450	\eta_{ij}
  3451	\;=\;
  3452	d\log(z_i - z_j)
  3453	\;=\;
  3454	\frac{dz_i - dz_j}{z_i - z_j}.
  3455	\end{equation}
  3456	The two forms are distinct: $\eta_{ij}$ is the logarithmic
  3457	Arnold one-form, weight~$1$ under conformal rescaling, which
  3458	lives in $H^1(\mathrm{Conf}_2(\bC))$ and serves as the
  3459	bar-complex coefficient; the propagator
  3460	$k\,dz_i/(z_i - z_j)^2$ is weight~$2$ and is the actual Feynman
  3461	propagator of the perturbative expansion. They are related by
  3462	the identity $dz_i/(z_i - z_j)^2 = -\partial_{z_i}(1/(z_i - z_j))$,
  3463	but this is not the Arnold form~$\eta_{ij}$: the Arnold form is
  3464	the bar-complex coefficient appearing in
  3465	$d_{\mathrm{res}}^2 = 0$, while the propagator is the physical
  3466	two-point function whose collision residue feeds the bar
  3467	differential. In the bar-complex formalism of
  3468	Section~\ref{sec:bar-complex-introduction},
  3469	$\eta_{ij}$ is the generator of the cohomology of
 exited 1 in 51ms:

 succeeded in 51ms:
   736	$\mathrm{av}\colon\Barchord(A)\to\Barch(A)$
   737	is a motivic projection: it kills precisely the transcendental
   738	arithmetic content of the configuration-space integrals.
   739	
   740	The ordered configuration space
   741	$\mathrm{Conf}_k^{\mathrm{ord}}(\mathbb{C})$
   742	carries a canonical mixed Hodge structure whose periods are
   743	the iterated integrals of the Knizhnik--Zamolodchikov connection.
   744	The $R$-matrix monodromy of
   745	Proposition~\ref{sec:r-matrix-descent-vol1} is computed by these
   746	periods, and the resulting transcendental data is stratified by
   747	degree:
   748	\begin{itemize}
  2248	\begin{equation}\label{eq:heisenberg-delta-ordered}
  2249	\Delta[\susp^{-1}J \,|\, \cdots \,|\, \susp^{-1}J]
  2250	\;=\;
  2251	\sum_{i=0}^{n}
  2252	[\susp^{-1}J \,|\, \cdots \,|\, \susp^{-1}J]_{i}
  2253	\;\otimes\;
  2254	[\susp^{-1}J \,|\, \cdots \,|\, \susp^{-1}J]_{n-i},
 succeeded in 51ms:
   740	degree:
   741	\begin{itemize}
   742	\item At degree~$2$: the monodromy $R(z)$ of the flat connection
   743	$\nabla = d - r(z)\,dz$ involves $2\pi i$, a period of
   744	the Lefschetz motive~$\mathbb{L}$ (weight~$1$).
   745	
   746	\item At degree~$3$: the Drinfeld associator
   747	$\Phi_{\mathrm{KZ}}$
   748	(the monodromy of the KZ connection on
  2178	constant~$k$ as the value of $d$ on the ground field copy
  2179	inside the symmetric bar. In the ordered complex the constant
  2180	is collected upstream in $m_0$, and the corresponding holonomy
  2181	on ordered configuration space is the R-matrix
  2182	$R(z)=e^{k\hbar/z}$
  2183	(Theorem~\ref{thm:heisenberg-rmatrix}).
  2184	The three pictures are equivalent presentations of the same
  2185	genus-zero datum $\kappa(\cH_k)=k$.
  2186	\end{remark}
  2187	
  2188	\begin{theorem}[Collision residue and $R$-matrix;

thinking
**Searching for audit corrections**

It looks like some lines for the audit candidates have been corrected, but there’s a chance the line numbers are now out of sync. I need to search within the ordered_associative_chiral_kd file for specific terms `d\log` and `\nabla`. I’ll utilize the rg tool to help me with this. I just need to ensure I’m thorough and get the right information here!
exec
/bin/zsh -lc "rg -n 'd\\\\log|d log|\\\\nabla|KZ|connection' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'd\\\\log|d log|\\\\nabla|KZ|connection' appendices/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'd\\\\log|d log|\\\\nabla|KZ|connection' chapters/frame/heisenberg_frame.tex chapters/theory/quantum_corrections.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/theory/e1_modular_koszul.tex appendices/_sl2_yangian_insert.tex chapters/connections/arithmetic_shadows.tex standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
355:The surplus is the $R$-matrix: the monodromy of the flat connection
389:$(s^{-1}\bar A)^{\otimes n}$, with flat connection induced by the
401:flat connection.
415:\subsection*{The spectral Kohno connection}
417:\begin{construction}[$R$-matrix as monodromy of the Kohno connection]
422:\index{Kohno connection}
426:\mathcal{O}(*\Delta)$. By the bar kernel convention (the $d\log$
430:These residues define a flat connection on the trivial bundle
433:\begin{equation}\label{eq:kohno-connection}
434:\nabla
442:and $r_{ij}(z_{ij})\,dz_{ij}$ is the connection $1$-form
451:\nabla^2
473:Hence $\nabla$ is flat.
481:The \emph{$R$-matrix} is the monodromy of $\nabla$ around~$\gamma$:
485:\operatorname{Mon}_\gamma(\nabla)
499:winds around $z_j$ with all other points fixed). The flat connection
500:$\nabla$ induces a monodromy representation
551:exchanges $z_i$ and $z_{i+1}$. The monodromy of the flat connection
552:$\nabla$ (eq.~\eqref{eq:kohno-connection}) along this path decomposes
558: from the flat connection on ordered configuration space.
 succeeded in 51ms:
353:the $R$-matrix. The $R$-matrix arises from the flat connection
386:$(s^{-1}\bar A)^{\otimes n}$, with flat connection induced by the
398:flat connection.
412:\subsection*{The spectral Kohno connection}
414:\begin{construction}[$R$-matrix as monodromy of the Kohno connection]
419:\index{Kohno connection}
423:\mathcal{O}(*\Delta)$. By the bar kernel convention (the $d\log$
427:These residues define a flat connection on the trivial bundle
430:\begin{equation}\label{eq:kohno-connection}
431:\nabla
439:and $r_{ij}(z_{ij})\,dz_{ij}$ is the connection $1$-form
445:\nabla^2
451:\,d\log(z_{ij})\wedge d\log(z_{jk})
467:Hence $\nabla$ is flat.
475:The \emph{$R$-matrix} is the monodromy of $\nabla$ around~$\gamma$:
479:\operatorname{Mon}_\gamma(\nabla)
493:winds around $z_j$ with all other points fixed). The flat connection
494:$\nabla$ induces a monodromy representation
545:exchanges $z_i$ and $z_{i+1}$. The monodromy of the flat connection
546:$\nabla$ (eq.~\eqref{eq:kohno-connection}) along this path decomposes
 succeeded in 50ms:
appendices/_sl2_yangian_insert.tex:32:By the $d\log$ absorption principle (the bar complex uses $d\log(z{-}w)$
appendices/_sl2_yangian_insert.tex:193:incorporates the monodromy of the flat connection
appendices/_sl2_yangian_insert.tex:194:$\nabla=d-r(z_{ij})\,dz_{ij}$ on
appendices/_sl2_yangian_insert.tex:230:\textup{(}the parallel transport of the connection
appendices/_sl2_yangian_insert.tex:231:$\nabla=d-r^{\mathrm{coll}}(z)\,dz$ on
appendices/_sl2_yangian_insert.tex:588:the collision residue~\eqref{eq:sl2-collision-residue}: the $d\log$
chapters/theory/e1_modular_koszul.tex:16:associator $\Phi_{\mathrm{KZ}}$. At every degree the $E_\infty$
chapters/theory/e1_modular_koszul.tex:49:spectral $r$-matrix, the KZ associator, and the ordered genus tower.
chapters/theory/e1_modular_koszul.tex:130:configuration spaces of the curve, and the KZ associator
chapters/theory/e1_modular_koszul.tex:131:$\Phi_{\mathrm{KZ}}$ at degree~$3$ is the monodromy of a
chapters/theory/e1_modular_koszul.tex:132:flat connection on $C_3^{\mathrm{ord}}(\mathbb{P}^1
chapters/theory/e1_modular_koszul.tex:419: $\mathfrak{C}(\cA) = \operatorname{av}(\Phi_{\mathrm{KZ}})$
chapters/theory/e1_modular_koszul.tex:422: in the full KZ associator.
chapters/theory/e1_modular_koszul.tex:869:the KZ connection, and the chiral differential are encoded in
chapters/theory/e1_modular_koszul.tex:934:(ii) When $S(z) \neq \tau$, the monodromy of the KZ connection
chapters/theory/e1_modular_koszul.tex:936:$\Phi_{\mathrm{KZ}} \in \exp(\hat{\mathfrak{t}}_3)$,
chapters/theory/e1_modular_koszul.tex:983:The degree-$2$ flat connection is
chapters/theory/e1_modular_koszul.tex:984:$\nabla = d + k\,dw/w$ with monodromy $e^{2\pi i k}$;
chapters/theory/e1_modular_koszul.tex:1003:% AP27: bar propagator weight 1 (d log E is weight 1).
chapters/theory/e1_modular_koszul.tex:1010:place of $1/z$, and the KZ connection is replaced by the



thinking
**Isolating formula issues**

I'm trying to pinpoint wrong occurrences in Volume I. The search results show many formulas using `dz`, but I suspect some are incorrect. 

For example, in appendices line 2220, it suggests `\nabla = d - r^{coll}(z)\,dz/z`, which I think should connect to `r(z)dz` instead. That could lead to `k dz/z^2`, which doesn’t seem right. 

Also, line 2445 mentions `\nabla = d - \Theta\,d(z_1-z_2)/(z_1-z_2)`, and I wonder if this should involve `r(z)\,dz` or even `\Theta d\log(z)`. I need to check the context thoroughly!
thinking
**Inspecting context for formulas**

I really need to take a closer look at the context here. In appendices line 2650, the formula `\nabla = d - r(z_1-z_2)\,d(z_1-z_2)` might actually be correct if `r` includes `1/z`, so that's a possibility. 

Then, line 984 from e1_modular_koszul suggests `\nabla = d + k\,dw/w`, but that seems off. I think it should be `d + (k/w)\,dw` or `d - (k/w)\,dw`, depending on the sign. 

Additionally, in the KZB formula, I need to double-check if it uses `\wp_1(z_i-z_j,\tau)\,dz_{ij}` or `d\log E`, particularly in line 1029. That seems likely correct, maybe involving `r^{E_\tau}(z) dz`.

In the ordered_associative_chiral_kd, line 5234 looks currently correct, but I want to verify lines around 5225 and check line 8334 for potential issues related to the log derivative. I need to use commands to examine the formulas in those ranges and figure out if any current lines in Volume I are incorrect!
thinking
**Inspecting logs for audit**

I think I need to be careful since there seems to be a recurring issue identified during the audit. The user specifically asked about searching for "dlog" in connection/KZ/nabla, so it makes sense to limit the search to those areas. I could utilize the previous audit along with a manual search of current files using a command like `rg -n 'd\\\\log' ...` to identify any occurrences. However, it's possible that the current files are already mostly correct. It seems I need to examine the exact lines in Vol I closely.
codex
The Vol I surface is partly already corrected, so I’m checking for residual drift rather than replaying the old audit blindly. I’ve already confirmed `quantum_corrections.tex` is talking about the bar differential, not a KZ one-form, and `yangians_drinfeld_kohno.tex` is already on `d(z_i-z_j)/(z_i-z_j)` rather than bare `d\\log`.
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '978,990p;1026,1036p;1824,1834p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/ordered_associative_chiral_kd.tex | sed -n '4884,4920p;2442,2448p;2218,2226p;2648,2652p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'd\\\\log|d log|\\\\nabla|KZ|connection' chapters/connections/thqg_introduction_supplement.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/ordered_associative_chiral_kd.tex | sed -n '5224,5260p;6680,6692p;6888,6894p;8338,8354p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/survey_modular_koszul_duality.tex | sed -n '4734,4758p;7228,7244p;7538,7546p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   978	translation $D(J) = \mathbf{1}$; inner derivations vanish
   979	because $J_{(0)}J = 0$);
   980	$\mathrm{HH}^2 = \bC$ (the level deformation cocycle
   981	$\phi_k(J \otimes J) = k \cdot \mathbf{1}$, the unique
   982	deformation $J(z)J(w) \sim (k + \epsilon)/(z-w)^2$).
   983	The degree-$2$ flat connection is
   984	$\nabla = d + k\,dw/w$ with monodromy $e^{2\pi i k}$;
   985	for generic $k \notin \bZ$, the twisted de~Rham cohomology
   986	of~$\bC^\times$ vanishes and $\mathrm{HH}^2$ is
   987	one-dimensional. Total dimension: $1 + 1 + 1 = 3$.
   988	Since $\cH_k$ is $\Einf$-chiral, the averaging map is a
   989	quasi-isomorphism and the symmetric chiral Hochschild gives
   990	the same answer
  1026	\textbf{KZB connection.} At degree $n$, with
  1027	$\hbar = 1/(k + h^\vee) = 1/(k+2)$ for $\mathfrak{sl}_2$:
  1028	\begin{equation}\label{eq:v1-kzb-conn}
  1029	  \nabla_{\mathrm{KZB}}
  1030	  = d
  1031	  - \hbar \sum_{i < j}
  1032	  \Omega_{ij}\,\wp_1(z_{ij}, \tau)\,dz_{ij}
 succeeded in 51ms:
  2218	\emph{derived} from the local OPE via analytic continuation:
  2219	it is the monodromy of the flat connection
  2220	$\nabla = d - r^{\mathrm{coll}}(z)\,dz/z$, not independent
  2221	input. The Yang--Baxter equation is satisfied trivially
  2222	because $R(z)$ is scalar \textup{(}$\cH_k$ has rank~$1$\textup{)}.
  2223	\end{theorem}
  2224	
  2225	\begin{proof}
  2226	The OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole.
  2442	Hence $d = 0$ in the reduced complex.
  2443	
  2444	\item \emph{R-matrix.} The connection
  2445	$\nabla = d - \Theta\,d(z_1{-}z_2)/(z_1{-}z_2)$ on
  2446	$\operatorname{Conf}_2^{\mathrm{ord}}(\bC)$ has monodromy
  2447	\begin{equation}\label{eq:bg-rmatrix}
  2448	R \;=\; \exp(2\pi i\,\Theta) \;=\; \id + 2\pi i\,\Theta,
  2648	
  2649	For the R-matrix: the connection is
  2650	$\nabla = d - r(z_1-z_2)\,d(z_1 - z_2)$, and the monodromy around
  2651	$z_1 = z_2$ is $\exp(2\pi i \cdot r)$. On the lattice sector
 succeeded in 51ms:
4:% connection, Yangian extraction, and Arnold-to-YBE proof as
192:\nabla^{\mathrm{hol}}\bigr).
207:\item The modular shadow connection
208: $\nabla^{\mathrm{hol}}_{g,n} = d - \operatorname{Sh}_{g,n}(\Theta_\cA)$:
209: flat connection on the derived coinvariant / protected-state package,
212: (constructed in \S\ref{subsec:thqg-intro-shadow-connection-construction}).
223:\input{chapters/connections/thqg_introduction_supplement_body}
 succeeded in 50ms:
  4734	The KZ connection on $\operatorname{Conf}_n(\mathbb C)$ with values
  4735	in $\mathfrak g^{\otimes n}$ is
  4736	\[
  4737	\nabla_{\mathrm{KZ}}
  4738	\;=\;
  4739	d\;-\;\hbar\sum_{i<j}
  4740	\Omega_{ij}\,d\log(z_i-z_j).
  4741	\]
  4742	Its monodromy representation
  4743	$\pi_1(\operatorname{Conf}_n(\mathbb C))\to
  4744	\operatorname{Aut}(V^{\otimes n})$
  4745	is compared by the affine Drinfeld--Kohno theorem with the
  4746	corresponding quantum-group representation category. In the
  4747	shadow obstruction tower:
  4748	\[
  4749	\nabla_{\mathrm{KZ}}
  4750	\;=\;
  4751	\operatorname{Sh}_{0,n}(\Theta_{\widehat{\mathfrak g}_k}):
  4752	\]
  4753	on the affine Kac--Moody comparison surface, the KZ connection is
 succeeded in 50ms:
  5224	
  5225	\begin{definition}[KZ connection]
  5226	\ClaimStatusProvedHere
  5227	\label{def:kz-connection}
  5228	\index{KZ connection|textbf}
  5229	On the trivial bundle over $\mathrm{Conf}_n(\mathbb{C})$ with fibre
  5230	$V_1 \otimes \cdots \otimes V_n$ (finite-dimensional
  5231	$\mathfrak{g}$-modules), the \emph{Knizhnik--Zamolodchikov connection}
  5232	is
  5233	\begin{equation}\label{eq:kz}
  5234	\nabla_{\mathrm{KZ}}
  5235	\;=\;
  5236	d
  5237	\;-\;
  5238	\frac{\hbar}{2\pi i}
  5239	\sum_{1 \leq i < j \leq n}
  5240	\Omega_{ij}\,d(z_i - z_j)/(z_i - z_j),
  5241	\end{equation}
  5242	where $\hbar = \pi i/(k + h^\vee)$ and $\Omega_{ij}$ denotes the
  5243	Casimir acting in the $(i,j)$ tensor slots.


thinking
**Evaluating user search results**

I'm wondering if the user is searching through all volumes rather than computing. It's possible there are numerous tests in the current repository, particularly in volumes two and three. I'll look at specific files and lines where certain functions and tests might be present. I think I need to decide whether to include compute surfaces since they're straightforward. It'll be important to verify this; I might need to inspect volumes and read the current inconsistencies in the .tex files.
thinking
**Planning for edits**

I need to consider what to do before making any edits. Maybe I can connect some formula types, like KZ and Arnold. I think I should provide a verdict of ACCEPT. Then, I'll work on a commentary using a concise template, possibly incorporating canonical forms to keep things organized. It seems like a solid plan to ensure clarity in my edits!
codex
```text
type: [KZ / connection 1-form / Arnold]
form: [KZ and shadow connections written as sum r_{ij}(z_{ij}) dz_{ij}; Arnold retained only as d log(z_i-z_j) bar coefficient]
connection: r(z)dz NOT d log; KZ: sum r_{ij} dz_{ij}; Arnold: d log(z_i-z_j) (bar coeff)
AP27 propagator weight: 1? [Y]
AP130 fiber-base: form lives on [fiber for Arnold/bar coefficient, base for connection], correctly distinguished? [Y]
verdict: ACCEPT
```

thinking
**Inspecting current contexts**

I need to take a closer look at Volume II and check the current contexts. It's important that I read around the candidate lines to gather all the relevant information. I want to make sure I'm considering everything properly before moving forward. There might be essential details or connections that I could miss if I don't verify what's happening in that volume. Let's dive in and see what I can find!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex | sed -n '608,620p;1078,1086p;1286,1293p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex | sed -n '2602,2610p;2865,2872p;3244,3250p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex | sed -n '339,346p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   608	\item A single datum, the level $k$, determines the entire scalar modular partition function:
   609	 \begin{equation}
   610	 % label removed: eq:heisenberg-full-reconstruction
   611	 Z_{\mathcal{H}_k}(\h)
   612	 = k \cdot \sum_{g=1}^{\infty} \h^{2g-2} \cdot
   613	 \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}.
   614	 \end{equation}
   615	\item The shadow connection $\nabla^{\mathrm{hol}}_{0,n} = d - \kappa \cdot \omega^{(2)}$
   616	 is flat, where $\omega^{(2)} = \sum_{i<j} d\log(z_i - z_j)$ is the Arnold class.
   617	\item All higher soft theorems vanish: $S_r = 0$ for $r \geq 3$.
   618	\end{enumerate}
   619	\end{theorem}
   620	
  1078	\begin{remark}[KZ connection]
  1079	% label removed: rem:kz-connection
  1080	For affine algebras $\widehat{\mathfrak{g}}_k$, on the affine Kac--Moody
  1081	comparison surface the leading soft factor gives the KZ connection form:
  1082	\[
  1083	\nabla^{\mathrm{KZ}}_n = d - \frac{1}{k + h^\vee} \sum_{i < j}
  1084	\Omega_{ij} \, d\log(z_i - z_j),
 succeeded in 51ms:
  2602	Let $\cA$ be a chiral algebra on a smooth curve~$X$. For each
  2603	$k \geq 2$, the OPE of~$\cA$ determines an \emph{OPE-weighted
  2604	local system} $\cL_{\cA}$ on $\Conf_k(\C)$, whose fiber at
  2605	$(z_1,\ldots,z_k)$ is $\cA^{\otimes k}$ with flat connection
  2606	$\nabla = d - \sum_{i<j} \Omega_{ij}\, d\log(z_i - z_j)$
  2607	of KZ type, where $\Omega_{ij} \in \End(\cA^{\otimes k})$ is
  2608	the OPE residue acting on factors~$i,j$. Flatness
  2609	$\nabla^2 = 0$ follows from OPE associativity
  2610	(the singular parts satisfy the infinitesimal braid relations).
  2865	Recall from Definition~\ref{def:rational-smooth-collision}
  2866	that the OPE-weighted local system
  2867	$\cL_\cA$ on $\Conf_k(\C)$ has a flat connection
  2868	$\nabla = d - \sum_{i<j}\Omega_{ij}\,d\log(z_i - z_j)$,
  2869	and its collision filtration
  2870	$\cL^{\leq 0} \subset \cL^{\leq 1} \subset \cdots$
  2871	is indexed by pole order along the boundary divisors of
  2872	$\FM_k^{\mathrm{alg}}(\C)$.
  3244	A second categorical point concerns the OPE-weighted local
  3245	system~$\cL_\cA$. The connection
  3246	$\nabla = d - \sum_{i<j}\Omega_{ij}\,d\log(z_i - z_j)$
 succeeded in 51ms:
   339	constructions all produce the same braid group representation:
   340	\begin{enumerate}[label=\textup{(\arabic*)}]
   341	\item \textbf{KZ monodromy.} The monodromy of the Knizhnik--Zamolodchikov
   342	 connection $\nabla^{\mathrm{KZ}} = d - (1/(k+2))\sum_{i<j}\Omega_{ij}\,d\log(z_i-z_j)$
   343	 on $V_{j_1}\otimes\cdots\otimes V_{j_n}$ around the discriminant
   344	 divisor. (This is the bar-coefficient realization; the connection
   345	 $1$-form is $\sum r_{ij}\,dz_{ij}$.)
   346	\item \textbf{Quantum Casimir eigenvalues.} The eigenvalues of
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1522,1528p;1635,1640p;1783,1789p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '1399,1405p;1508,1513p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex | sed -n '1906,1910p;1933,1938p;2238,2242p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1532,1536p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex | sed -n '1778,1783p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1522	The KZ connection at level~$k\neq -2$ on
  1523	$\Conf_2(\CC)$ with two fundamental insertions is
  1524	\[
  1525	 \nabla \;=\; d \;-\; \frac{1}{k+2}\,\Omega_{12}\,d\log(z_1-z_2).
  1526	\]
  1527	Since $\Omega_{12}$ is diagonalizable, parallel transport around
  1528	the generator $\gamma$ of $\pi_1(\Conf_2(\CC))\cong\ZZ$
  1635	 $\exp\!\bigl(-\frac{2\pi i}{k+2}\,\Omega_{12}\bigr)$ as computed in~\eqref{eq:conf2-monodromy}.
  1636	\item \emph{Infinity boundary} ($w\to\infty$ with $u$ bounded).
  1637	 In the coordinate $s=1/w$, the connection is regular at $s=0$
  1638	 because the KZ form $d\log(z_1-z_2)=d\log u$ has no pole in~$w$.
  1639	 Hence the local monodromy around $D_\infty$ is trivial.
  1640	\item \emph{Corner stratum} ($u\to 0$ and $w\to\infty$ simultaneously).
  1783	\begin{theorem}[Reduced HT connection equals KZ connection; \ClaimStatusProvedHere]
  1784	\label{thm:reduced-equals-kz}
  1785	In the setting of Proposition~\textup{\ref{prop:affine-resolved}}, the reduced logarithmic flat connection on $H_n = H^0(E_n[[\h]], Q_n)$ is the Knizhnik--Zamolodchikov connection:
  1786	\[
  1787	 \A_n \;=\; \frac{1}{k + h^\vee}\sum_{1 \leq i < j \leq n} \rho_{ij}(\Omega)\, d\log(z_i - z_j),
  1788	\]
  1789	where $\rho_{ij}$ acts in the $i$-th and $j$-th tensor factors of\/ $V_1 \otimes \cdots \otimes V_n$.
 succeeded in 51ms:
  1399	The KZ connection at level~$k\neq -2$ on
  1400	$\Conf_2(\CC)$ with two fundamental insertions is
  1401	\[
  1402	 \nabla \;=\; d \;-\; \frac{1}{k+2}\,\Omega_{12}\,d\log(z_1-z_2).
  1403	\]
  1404	Since $\Omega_{12}$ is diagonalizable, parallel transport around
  1405	the generator $\gamma$ of $\pi_1(\Conf_2(\CC))\cong\ZZ$
  1508	 $\exp\!\bigl(-\frac{2\pi i}{k+2}\,\Omega_{12}\bigr)$ as computed in~\eqref{eq:conf2-monodromy}.
  1509	\item \emph{Infinity boundary} ($w\to\infty$ with $u$ bounded).
  1510	 In the coordinate $s=1/w$, the connection is regular at $s=0$
  1511	 because the KZ form $d\log(z_1-z_2)=d\log u$ has no pole in~$w$.
  1512	 Hence the local monodromy around $D_\infty$ is trivial.
  1513	\item \emph{Corner stratum} ($u\to 0$ and $w\to\infty$ simultaneously).
 succeeded in 50ms:
  1906	 (Theorem~\ref{thm:thqg-ks-koszul-btt}).
  1907	\item $\nabla^{\mathrm{hol}}_{\mathrm{KS}}$: at genus~$0$, the shadow
  1908	 connection is $d - r_{\mathrm{KS}}^{(ij)} d\log(z_i - z_j)$, which
  1909	 is the Gauss--Manin connection on the moduli of complex structures.
  1910	\end{enumerate}
  1933	The shadow connection at genus~$0$ is determined by the binary
  1934	coupling $\Theta_{\mathrm{KS}}^{\le 2}$, which is the
  1935	Schouten--Nijenhuis bracket. The formula
  1936	$\nabla_{0,n} = d - \sum_{i<j} r^{(ij)}(z_i - z_j)\,d\log(z_i - z_j)$
  1937	specializes to the stated expression with $r_{\mathrm{KS}}(z)
  1938	= \Omega_{\PV}^{\sn}/z$.
  2238	where $P^! = (H^\bullet(\barB(P)))^\vee$ is the classical Koszul
  2239	dual PVA, $r^{\mathrm{cl}}(z)$ is the classical $r$-matrix, and
  2240	$\nabla^{\mathrm{cl}} = d - r^{\mathrm{cl}} \cdot d\log(z)$ is
  2241	the classical KZ connection.
  2242	\end{proposition}
 succeeded in 50ms:
  1532	for $r(z) = k\,\Omega/z$.
  1533	On the affine Kac--Moody comparison surface, the mixed MC component
  1534	along the spectral parameter identifies with the KZ connection
  1535	$\nabla = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$.
  1536	$\alpha_T^{\mathrm{op}}$ encodes the Yangian coproduct on
 succeeded in 51ms:
  1778	$\cA = \widehat{\fg}_k$ at non-critical level, the connection
  1779	is the KZ connection
  1780	$\nabla_{\mathrm{KZ}} = d - \Omega\, d\log(z_1 - z_2)/(k + h^\vee)$
  1781	on the strip, which on the annulus becomes
  1782	$\nabla_{\mathrm{KZ}}^{\mathrm{ell}} = d - \Omega\, \varpi(z;\tau)/(k + h^\vee)$,
  1783	where $\varpi(z;\tau) = \partial_z \log \theta_1(z;\tau)$

thinking
**Searching for candidates**

I need to find more candidates for Volume II, specifically looking at items like rosetta_stone, spectral-braiding-core, thqg_line_operators_extensions, and standalone/preface. It's a bit of a task to inspect these, but it seems necessary to ensure I have the right components. I’ll take my time here to confirm what fits best in the context I'm working with. Let’s see what else I can discover in this search!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '2664,2670p;2744,2751p;2523,2528p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex | sed -n '1194,1200p;1336,1341p;5073,5076p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex | sed -n '499,504p;1109,1113p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py | sed -n '1,10p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex | sed -n '512,516p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex | sed -n '770,775p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/standalone/stokes_gap_kzb_regularity.tex | sed -n '151,154p;208,211p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py | sed -n '923,927p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_semisimple_purity.py | sed -n '39,43p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2523	\;=\;
  2524	\Omega_{12}\,d\log(z_1 - z_2).
  2525	\end{equation}
  2526	This is the KZ connection form $A_2$ of
  2527	Theorem~\ref{thm:derived-additive-kz} at $n = 2$.
  2528	The operation $\mu_{2,0}(a_1, a_2)$ is obtained by integrating
  2664	\;\otimes\; \mathbf{1}_{E_1(2)},
  2665	\end{equation}
  2666	where $\Omega_{12}$ acts on the two open-colour tensor factors
  2667	and $d\log(u_1 - u_2)$ is the KZ connection form on the ordered
  2668	configuration space $\Conf_2^{\mathrm{ord}}(\A^1)$ of the two
  2669	spectral parameters. The closed-colour input $z$ has been
  2670	absorbed into the spectral difference $u_1 - u_2$ by
  2744	where the holomorphic weight form $\omega_k^{\mathrm{hol}}$ is
  2745	the KZ connection form on $k$ marked points:
  2746	\begin{equation}\label{eq:KZ-weight-form}
  2747	\omega_k^{\mathrm{hol}}(z_1, \ldots, z_k)
  2748	\;=\;
  2749	\sum_{1 \le i < j \le k}
  2750	\Omega_{ij}\,d\log(z_i - z_j),
 succeeded in 51ms:
  1194	double-pole OPE: $k/(z-w)^2 \cdot d\log(z-w)
  1195	\leadsto k/z$).
  1196	The connection on $\Conf_2^{\mathrm{ord}}(\C)$ is
  1197	$\nabla = d - k \cdot d\log(z)$,
  1198	and the monodromy is $\exp(-2\pi i k)$.
  1199	The spectral $R$-matrix on modules is
  1200	\begin{equation}\label{eq:heisenberg-hydrogen-R}
  1336	$d\log$ kernel absorbs one power from the double-pole OPE:
  1337	$k/(z-w)^2 \cdot d\log(z-w) \leadsto k/z$). The
  1338	connection on $\Conf_2^{\mathrm{ord}}(\bC)$ is
  1339	$\nabla = d - k\, d\log(z)$, and the monodromy around
  1340	the generator $\gamma$ is $\exp(-2\pi i k)$. The spectral
  1341	$R$-matrix on modules is
  5073	of the KZ connection at \emph{every} non-critical level, not
  5074	only at integrable level: the singularity structure is
  5075	logarithmic because the connection form involves $d\log$
  5076	kernels.
 succeeded in 51ms:
   499	(Theorem~\ref{thm:Koszul_dual_Yangian}). The
   500	$R$-matrix $R(z)=\exp(k\,\Omega/(z(k{+}2)))$ is the
   501	explicit spectral braid kernel associated with the KZ connection
   502	$\nabla=d-\Omega\,d\log(z)/(k+2)$
   503	(Computation~\ref{comp:line-op-sl2}). This monodromy
   504	representation is compared by the affine Drinfeld--Kohno theorem
  1109	\end{equation}
  1110	This is the standard Drinfeld--Kohno computation
  1111	(\cite{Dri89}, Theorem 3.2; \cite{KL93}): the monodromy
  1112	of the logarithmic connection $d-\hbar\,\Omega\,d\log z$
  1113	around $z=0$ is $e^{2\pi i\hbar\,\Omega}=q^{2\Omega}$.
 succeeded in 52ms:
     1	"""Log HT Monodromy Engine: KZ connections, braid relations, and Yang-Baxter.
     2	
     3	Implements chain-level computations for the logarithmic holomorphic-topological
     4	monodromy chapter (log_ht_monodromy_core.tex), verifying:
     5	
     6	1. KZ connection flatness: (d - sum Omega_{ij} dlog(z_ij))^2 = 0
     7	2. Infinitesimal braid relations: [Omega_{12}, Omega_{13} + Omega_{23}] = 0
     8	3. Bar insertion identity at arity 2
     9	4. Classical Yang-Baxter equation for rational r-matrices
    10	
 succeeded in 51ms:
   512	and contributes trivially to the CYBE; the collision residue
   513	r-matrix is $r(z) = k\,\Omega/z$.
   514	The KZ connection $\nabla_{\mathrm{KZ}} = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$ is
   515	the flat connection on conformal blocks on the affine Kac--Moody
   516	comparison surface. Its monodromy is compared by the affine
 succeeded in 52ms:
   770	 \nabla_\fS \;=\; d \;+\; \frac{1}{k+2}\,\Omega\,\frac{dz}{z},
   771	\]
   772	where $\Omega = e \ot f + f \ot e + \tfrac{1}{2} h \ot h$ is the split Casimir of $\mathfrak{sl}_2$.
   773	
   774	The connection is regular singular at $z = 0$ with residue $\Omega/(k+2)$. The regularity follows from bar-kernel absorption: the $d\log$ kernel absorbs one pole from the $z^{-2}$ OPE singularity $J^a(w)J^b(z) \sim k\kappa^{ab}/(w-z)^2 + f^{ab}_c J^c(z)/(w-z)$, so the collision $r$-matrix has a simple pole $r(z) = k\,\Omega/z + O(1)$ at level~$k$ The overall normalization $(k+2)^{-1}$ from Theorem~\ref{thm:reduced-equals-kz} converts this to the residue $\Omega/(k+2)$, and the $d\log z$ kernel absorbs the pole from $dz/z$, producing the claimed form.
   775	\end{construction}
 succeeded in 52ms:
   923	    r"""Verify flatness of nabla^hol at genus 0, arity n.
   924	
   925	    For the Heisenberg shadow connection nabla = d - kappa sum q_i q_j dlog(z_i - z_j):
   926	    Flatness follows from the Arnold relation
   927	    eta_12 ^ eta_23 + eta_23 ^ eta_31 + eta_31 ^ eta_12 = 0
    39	    """Compute the effective OPE residue operator Omega^eff_{ij}.
    40	
    41	    For the KZ connection nabla = d - sum Omega_{ij} dlog(z_i - z_j),
    42	    the effective residue is Omega^eff = Omega minus scalar/curvature part.
    43	
 succeeded in 52ms:
   151	In plumbing coordinates, the KZB connection form decomposes as
   152	\[
   153	\nabla^{\KZB} = \sum_{e \in E(\Gamma)} \Omega_e\, d\log(t_e)
   154	  + \nabla^{\mathrm{smooth}}
   208	  The Bernard elliptic KZB in the $q$-expansion
   209	  ($q = e^{2\pi i \tau}$) as $\tau \to i\infty$.
   210	  Verify the connection form is $\Omega\, d\log(q) +
   211	  (\text{holomorphic in }q)$ for all~$k$.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex | sed -n '710,716p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   710	\label{rem:three-hbar-sanity}
   711	The identification of Construction~\ref{constr:three-parameter-hbar}
   712	fails if any of the three parameters carries a hidden $2\pi i$ or
   713	$1/n!$. In particular, the KZ parameter is conventionally normalized
   714	so that the connection $\nabla = d - \hbar^{-1}\sum_i r_{ij}\,d\log(z_i
   715	- z_j)$ has integer monodromy on the configuration space; the DNP
   716	parameter is normalized so that the loop algebra has bracket
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex | sed -n '369,373p;491,495p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/compute/lib/kazhdan_lusztig_shadow.py | sed -n '328,334p'; nl -ba /Users/raeez/calabi-yau-quantum-groups/compute/lib/twisted_holography_cy3_engine.py | sed -n '777,781p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   369	\[
   370	 R \;=\; \mathcal{P}\exp\Bigl(\int_\gamma \Omega_{\mathrm{KZ}}\Bigr) \;\in\; \Uq(\frakg) \hat{\otimes} \Uq(\frakg)
   371	\]
   372	where $\Omega_{\mathrm{KZ}} = \sum_a I^a \otimes I_a \cdot d\log(z_1 - z_2)/(k + h^\vee)$ is the KZ connection and $\gamma$ is the winding path. This is the Drinfeld--Kohno theorem at the level of the factorization algebra.
   373	\end{remark}
   491	\smallskip\noindent\textbf{(b) Drinfeld--Kohno theorem.} Drinfeld (1989) and Kohno (1987) proved that the monodromy representation of the KZ equations
   492	\[
   493	 \nabla_{\mathrm{KZ}} \;=\; d - \frac{1}{k + h^\vee} \sum_{i < j} \Omega_{ij}\, d\log(z_i - z_j)
   494	\]
   495	(where $\Omega_{ij} = \sum_a I^a_i \otimes I_{a,j}$ is the Casimir) gives a representation of the braid group $B_n$ that factors through $\Uq(\frakg)$ at $q = e^{\pi i / (k + h^\vee)}$.
 succeeded in 50ms:
   328	
   329	    The E_2-shadow obstruction tower of ĝ_k produces braiding via the Drinfeld-Kohno
   330	    mechanism.  The KZ connection on the space of conformal blocks is:
   331	
   332	      ∇_KZ = d - (1/(k + h∨)) Σ_{a<b} Ω_{ab} d log(z_a - z_b)
   333	
   334	    where Ω_{ab} = Σ_A t^A_a ⊗ t^A_b is the Casimir in the a,b slots.
   777	    """The genus-0 E₁ shadow connection nabla^{E₁}_{0,n}.
   778	
   779	    nabla^{E₁}_{0,n} = d - sum_{i<j} r_{CY}(z_i - z_j) dlog(z_i - z_j)
   780	
   781	    For the affine Yangian with r(z) = phi_3/z³ + ...:

thinking
**Searching for surfaces**

I'm thinking I need to search for the compute surfaces in Volume I. It seems logical to start with a targeted list and then maybe do some inspection on those surfaces. I wonder what kind of information I might uncover as I dive into it! It sounds like an interesting task that could lead to some valuable insights. I'll stay focused on gathering what I need to get the best results.
exec
/bin/zsh -lc "nl -ba compute/lib/dmod_filtration_ss_engine.py | sed -n '437,442p'; nl -ba compute/lib/geometric_langlands_shadow_engine.py | sed -n '1229,1233p'; nl -ba compute/lib/theorem_swiss_cheese_kontsevich_engine.py | sed -n '467,478p'; nl -ba compute/lib/ordered_bar_descent_engine.py | sed -n '273,276p;358,361p'; nl -ba compute/lib/kz_monodromy_arithmetic_engine.py | sed -n '975,981p'; nl -ba compute/tests/test_holographic_shadow_connection.py | sed -n '54,56p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   437	    """KZ connection data for V_k(sl_2) on n points.
   438	
   439	    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
   440	
   441	    where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
   442	    factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
  1229	            ),
  1230	            'geom_langlands': (
  1231	                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
  1232	                'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
  1233	            ),
   467	        # Monodromy phase from KZ connection
   468	        # The connection form is omega = kappa * d log(z_1 - z_2)
   469	        # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
   470	        monodromy_phase = cmath.exp(1j * math.pi * kappa)
   471	
   472	        return {
   473	            'path_type': 'braid',
   474	            'n_points': n,
   475	            'monodromy_phase': monodromy_phase,

thinking
**Searching for compute files**

I’m thinking it might be helpful to find more compute files in Volume I. I should search for "rg -l" in the compute/lib/tests directory, specifically looking for dlog with connection/KZ/nabla. This will help me gather a list of relevant files. Let’s get started on that! It's essential to ensure I cover all the necessary bases to find what I'm looking for.
exec
/bin/zsh -lc "rg -l -P '(\\\\nabla["'^'"\\n]{0,120}d\\s*log|\\\\nabla["'^'"\\n]{0,120}dlog|KZ["'^'"\\n]{0,120}d\\s*log|connection["'^'"\\n]{0,120}d\\s*log|d\\s*log["'^'"\\n]{0,120}(KZ|connection|\\\\nabla)|dlog["'^'"\\n]{0,120}(KZ|connection|\\\\nabla))' compute/lib compute/tests standalone chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/theorem_index.tex
compute/tests/test_shadow_connection.py
standalone/e1_primacy_ordered_bar.tex
compute/tests/test_arithmetic_shadow_connection.py
compute/lib/ordered_chiral_jones_engine.py
compute/lib/theorem_gz_frontier_engine.py
compute/lib/twisted_holography_mc.py
compute/lib/twisted_gauge_defects_engine.py
compute/tests/test_universal_chiral_algebra_engine.py
compute/tests/test_arithmetic_comparison_explicit_engine.py
compute/lib/shadow_mzv_engine.py
compute/lib/theorem_dk0_evaluation_bridge_engine.py
compute/lib/arithmetic_shadow_connection.py
compute/lib/arithmetic_comparison_explicit_engine.py
compute/lib/arithmetic_packet_connection.py
compute/lib/e1_nonsplitting_obstruction_engine.py
compute/lib/primitive_kernel_full.py
compute/lib/dmod_purity_char_variety_engine.py
compute/lib/pbw_saito_comparison.py
compute/lib/geometric_langlands_shadow_engine.py

thinking
**Refining calculations**

I’m returning to the arithmetic packet connections. It seems like the dlog is creating confusion for me and isn’t relevant to Arnold or KZ. I should focus on selecting just KZ or maybe the difference z_i-z_j. Perhaps I can refine this further by searching for terms like `dlog(z` or `d log(z` in connection with KZ or nabla. For volume, I’ll compute libraries as needed.
exec
/bin/zsh -lc "rg -l -P '(\\\\nabla["'^'"\\n]{0,160}d\\s*log\\(z|\\\\nabla["'^'"\\n]{0,160}dlog\\(z|KZ["'^'"\\n]{0,160}d\\s*log\\(z|connection["'^'"\\n]{0,160}d\\s*log\\(z|d\\s*log\\(z["'^'"\\n]{0,160}(KZ|connection|\\\\nabla)|dlog\\(z["'^'"\\n]{0,160}(KZ|connection|\\\\nabla))' compute/lib compute/tests chapters appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/tests/test_arithmetic_shadow_connection.py
compute/lib/ordered_chiral_jones_engine.py
compute/lib/twisted_holography_mc.py
compute/lib/twisted_gauge_defects_engine.py
compute/lib/shadow_mzv_engine.py
compute/lib/theorem_dk0_evaluation_bridge_engine.py
compute/lib/arithmetic_shadow_connection.py
compute/lib/e1_nonsplitting_obstruction_engine.py
compute/lib/primitive_kernel_full.py
compute/lib/dmod_purity_char_variety_engine.py
compute/lib/dmod_filtration_ss_engine.py
compute/lib/geometric_langlands_shadow_engine.py
compute/lib/bc_mzv_shadow_engine.py
compute/lib/theorem_swiss_cheese_kontsevich_engine.py
compute/lib/kz_monodromy_arithmetic_engine.py
compute/lib/ordered_bar_descent_engine.py
exec
/bin/zsh -lc "rg -n -P '(\\\\nabla["'^'"\\n]{0,120}d\\\\log|KZ["'^'"\\n]{0,120}d\\\\log|connection["'^'"\\n]{0,120}d\\\\log|d\\\\log["'^'"\\n]{0,120}(KZ|connection|\\\\nabla))' chapters appendices standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/survey_modular_koszul_duality.tex:5216:scattering connection $d - d\log\varphi(s)$
chapters/connections/arithmetic_shadows.tex:11295:= \Lambda_\chi^{E_\chi}\,(\nabla v + d\log\Lambda_\chi
chapters/connections/arithmetic_shadows.tex:11328:logarithmic connections $d - d\log\Lambda_j$ on rank-one
chapters/connections/arithmetic_shadows.tex:11400:connection is $d - d\log\varphi$.

thinking
**Searching for survey data**

I’m noticing that the direct regression couldn’t catch the survey KZ because the formula spread across lines. It seems that mainly arithmetic and survey scattering are involved, which might not be relevant. I think I should focus on patching the survey for the explicit lines that are opened. It might be worth searching for the exact `d\log` near KZ in standalone surveys and consider looking into other standalone surveys as well.
exec
/bin/zsh -lc "rg -n 'KZ|d\\\\log|\\\\nabla' standalone/survey_modular_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
127:$d\log(z_i - z_j)$, and the bar differential becomes an integral
147:\eta_{12} \;=\; d\log(z_1 - z_2) \;=\; \frac{dz_1 - dz_2}{z_1 - z_2}\,.
178:$\eta_{ij} \mapsto \eta_{ij} + d\log\frac{w(z_i) - w(z_j)}{z_i - z_j}$.
179:Near the diagonal this becomes $d\log w'(z_i)$: the standard cocycle for
258:d\log(z_i-z_j)
415:The logarithmic form $\eta_{ij}=d\log(z_i-z_j)$ is the integral
424:$d\log$ well-defined on products.
571:obstruction tower~$\Theta_{\cA}$: at degree~$3$, the KZ associator
672:under the logarithmic kernel $d\log(z-w)$ (the bar differential
753:$\eta_{12}=d\log(z_1-z_2)$ is globally defined on~$\mathbb P^1$,
811:d\log E(z_1,z_2)
879:The bar propagator $d\log E(z,w)$ absorbs one pole order
880:(the $d\log$ measure sends $z^{-n}$ to $z^{-(n-1)}$), so the
900:D_g\;=\;d_{\mathrm{fib}}+\nabla^{\mathrm{GM}}
919:+[d_{\mathrm{fib}},\nabla^{\mathrm{GM}}]
920:+(\nabla^{\mathrm{GM}})^2
1183:correction~$\nabla^{\mathrm{GM}}$, and the clutching morphisms at
2716:Flat sections $\nabla s=0$
3114:\nabla_H(\mathrm{Sh}_r(\cA))+o^{(r)}(\cA)=0,
3117:where $\nabla_H$ is the Hodge covariant derivative (the linearised

thinking
**Searching for patterns**

I think I should check for the symbolic string `kappa * dz12/(z1-z2)` first. It might help to look in the current repo compute for `d log(z` in the connection docs. I'll search using `rg -n "d log\\(z"` among other patterns. 

Maybe a more straightforward search like `rg -n 'd log\\(z|dlog\\(z'` in compute/lib and compute/tests will help. Although, I might need to be exhaustive in the current repo to find relevant details.
exec
/bin/zsh -lc "rg -n 'd ?log\\(z|dlog\\(z' compute/lib compute/tests" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/celestial_arithmetic_engine.py:74:AP19 WARNING: The bar construction extracts residues along d log(z_i - z_j),
compute/lib/celestial_arithmetic_engine.py:287:    AP19: The bar construction uses d log(z-w), reducing pole orders by 1.
compute/lib/celestial_arithmetic_engine.py:972:        Res_{z=w}[f(z) d log(z-w)] = f(w). So the r-matrix is a
compute/lib/twisted_holography_engine.py:904:      nabla is just d - kappa * sum dlog(z_i - z_j).
compute/lib/theorem_gz_frontier_engine.py:395:        #   w = sum_{i<j} gamma_{ij} d log(z_i - z_j)
compute/lib/theorem_gz_frontier_engine.py:401:        # Then w = -2h/(n-2) * sum_{i<j} d log(z_i - z_j)
compute/lib/bv_bar_class_m_engine.py:197:    The bar complex extracts these via the logarithmic kernel d log(z-w).
compute/lib/bv_bar_class_m_engine.py:516:    where eta_{ij} = d log(z_i - z_j).
compute/lib/theorem_open_closed_rectification_engine.py:139:        The bar differential extracts residue along d log(z-w),
compute/lib/theorem_open_closed_rectification_engine.py:984:    The bar construction extracts residues along d log(z_i - z_j).
compute/lib/arithmetic_comparison_test.py:395:    nabla^arith_H = d - dlog(zeta(s)*zeta(s+1)) ds.
compute/lib/arithmetic_comparison_test.py:433:    nabla^arith_aff = d - dlog(zeta(s)*zeta(s-1)) ds.
compute/tests/test_twisted_holography_mc.py:281:    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
compute/tests/test_lattice_shadow.py:506:        because d log(z-w) absorbs one power (AP19).
compute/tests/test_bottleneck_yangians.py:290:        # The propagator eta_{12} = d log(z_1 - z_2) has Res_{z1=z2} = 1
compute/lib/celestial_koszul_ope.py:59:      and the extraction is r(z) = Res^{coll} Theta via d log(z-w)).
compute/lib/celestial_koszul_ope.py:79:CAUTION (AP19): The bar construction extracts residues along d log(z_i - z_j),
compute/lib/celestial_koszul_ope.py:534:        - Simple pole f^{abc}/(z-w) through d log(z-w) gives f^{abc}/z
compute/lib/celestial_koszul_ope.py:535:        - Double pole k delta_{ab}/(z-w)^2 through d log(z-w) gives k delta_{ab}/z
compute/lib/celestial_koszul_ope.py:572:    Wait: the simple pole dT/(z-w) through d log(z-w) gives dT * d log(z-w).

thinking
**Considering textual replacements**

I'm thinking about how to handle some generic textual replacements. For instance, changing `nabla = d - ... d log(z_i - z_j)` to `nabla = d - ... dz_{ij}/(z_i - z_j)` seems reasonable, but it's tricky since the variable notation varies. It doesn't seem straightforward, so manual adjustments might be necessary. Perhaps I could use a script to identify the exact lines needing updates, so I can patch them carefully, especially if there aren’t too many.
exec
/bin/zsh -lc "rg -n -P '(nabla|KZ|connection).{0,120}d ?log\\(z|d ?log\\(z.{0,120}(nabla|KZ|connection)' compute/lib compute/tests standalone chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/tests/test_arithmetic_shadow_connection.py:537:        The connection form dlog(zeta(s)*zeta(s+1)) has a pole at s=1
compute/tests/test_twisted_holography_mc.py:281:    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
compute/lib/ordered_chiral_jones_engine.py:25:     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
compute/lib/ordered_chiral_jones_engine.py:203:      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
compute/lib/ordered_chiral_jones_engine.py:208:    AP117: connection 1-form uses d log(z_i - z_j), which is the
compute/lib/twisted_holography_mc.py:58:  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
compute/lib/twisted_holography_mc.py:718:      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
compute/lib/twisted_holography_mc.py:787:    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
compute/lib/twisted_holography_mc.py:790:      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
compute/lib/twisted_holography_mc.py:819:      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
compute/lib/twisted_holography_mc.py:820:      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
compute/lib/arithmetic_comparison_test.py:395:    nabla^arith_H = d - dlog(zeta(s)*zeta(s+1)) ds.
compute/lib/arithmetic_comparison_test.py:433:    nabla^arith_aff = d - dlog(zeta(s)*zeta(s-1)) ds.
compute/lib/twisted_gauge_defects_engine.py:1283:      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
compute/tests/test_holographic_shadow_connection.py:55:    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
compute/tests/test_arithmetic_comparison_explicit_engine.py:80:    nabla^arith = d - d log(zeta(s)*zeta(s+1)) ds.
compute/lib/twisted_holography_engine.py:904:      nabla is just d - kappa * sum dlog(z_i - z_j).
compute/lib/shadow_mzv_engine.py:923:    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
compute/lib/holographic_shadow_connection.py:7:  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
compute/lib/holographic_shadow_connection.py:43:    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)


thinking
**Considering documentation edits**

Wow, there’s a lot to think about here! The user is asking for all volumes, so I need to consider editing all the compute libraries despite the potential workload. It seems feasible to target specific patches across many files, possibly around 20 or more. However, I first need to clarify whether the assigned files include these compute libraries. If there are issues, I could focus on patching only comments or docstrings for simplicity. I must keep final findings manageable but detailed as the user wants each issue listed comprehensively.
thinking
**Planning targeted searches**

I need to find a balance, making sure not to overwhelm while meeting the requirement, which probably comes first. Using flat bullets could help organize my findings. I should confirm the search lists for Vol II and Vol III compute as well. We already have the main .tex list, so I need to focus on the compute sections. I’ll use a targeted search pattern to look through Vol II and III with the specific regex across these volumes.
exec
/bin/zsh -lc "rg -n -P '(nabla|KZ|connection).{0,120}d ?log\\(z|d ?log\\(z.{0,120}(nabla|KZ|connection)' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '(nabla|KZ|connection).{0,120}d ?log\\(z|d ?log\\(z.{0,120}(nabla|KZ|connection)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:6:1. KZ connection flatness: (d - sum Omega_{ij} dlog(z_ij))^2 = 0
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:194:    nabla = d - (Omega_12 dlog(z_12) + Omega_13 dlog(z_13) + Omega_23 dlog(z_23))
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:579:      nabla = d - Omega_12 dlog(z12) - Omega_13 dlog(z13) - Omega_23 dlog(z23)
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:925:    For the Heisenberg shadow connection nabla = d - kappa sum q_i q_j dlog(z_i - z_j):
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/non_simply_laced_rmatrix.py:1031:    #   nabla = d - k * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_semisimple_purity.py:41:    For the KZ connection nabla = d - sum Omega_{ij} dlog(z_i - z_j),
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_vol2_preface_wave11.md:66:- **POSITIVE -- AP117 connection-vs-Arnold (lines 86--92, 373--377).** "The form eta_12 = d log(z_1 - z_2) is a bar-construction coefficient... it is not the connection form of a flat bundle. The KZ connection on conformal blocks... is the one-form Omega dz/(k + h^v), with a rational one-form in z, not a logarithmic one-form in z_1 - z_2." This is AP117 stated perfectly. PASS.
 succeeded in 50ms:
/Users/raeez/calabi-yau-quantum-groups/compute/lib/kazhdan_lusztig_shadow.py:332:      ∇_KZ = d - (1/(k + h∨)) Σ_{a<b} Ω_{ab} d log(z_a - z_b)
/Users/raeez/calabi-yau-quantum-groups/compute/lib/twisted_holography_cy3_engine.py:779:    nabla^{E₁}_{0,n} = d - sum_{i<j} r_{CY}(z_i - z_j) dlog(z_i - z_j)




thinking
**Investigating patterns and patches**

I'm considering how to proceed with Volume II. I might need to ignore the audit file and instead search through the .tex files in volume 2 that I haven’t inspected yet for specific patterns. There are additional files beyond the main list of 12 that I could check. I'll look at the outputs from previous targeted searches since they provided exact lines to patch. 

I’ll inspect specific files like rosetta_stone and twisted_holography_quantum_gravity to see if I need to patch any incorrect explanations. If I don't address this, it could leave residual confusion.
thinking
**Deciding on patches and edits**

Since I'm already editing the log_ht_monodromy_frontier, I need to consider whether I can patch the explanatory sentence in the current Volume II. I'm unsure if it's outside the root. A minimal edit could be changing the connection to "and the connection one-form is Ω dz/((k+2)z)" or perhaps just removing the dlog mention.

I’ll also search the Volume II manuscript for occurrences of `d\log` in connection formulas to ensure accuracy. It seems necessary to check Volume III too. 

Lastly, there's this big question: can we edit sibling repositories? I should test patching a Volume II file to see if it goes through. If it fails due to sandbox restrictions, I’ll need to rethink that approach. I might try applying a harmless comment to see if that works.
thinking
**Checking write permissions**

I'm considering that there might still be a way to check for write permissions. I could use the exec_command `test -w /Users/...` to see if I have write access from the operating system, rather than just the sandbox limitations. 

I can check if the file is writable using the shell, but I’m unsure if the sandbox would still restrict applying patches. I might try using `touch` in Volume II, but instructions suggest using apply_patch before any edits.
thinking
**Evaluating patch application**

I’m considering that discussing file permissions instead of the sandbox might not be relevant. It seems like apply_patch could indicate if something is disallowed. I might want to actually patch across multiple files, but first, it would be smart to gather a precise edit plan. Using update_plan with the detailed steps could really help streamline the process before I dive in. Let's see how it goes!
Plan update
Candidate surfaces are now verified in context. I’m patching the remaining live AP117 violations across manuscript and compute surfaces, then I’ll rerun a targeted cross-volume grep to confirm no residual `d\log` KZ/connection formulas remain.
  → Patch verified Vol I AP117 manuscript and compute surfaces
  • Patch verified Vol II AP117 manuscript and compute surfaces
  • Patch verified Vol III AP117 manuscript and compute surfaces
  • Re-run targeted cross-volume grep for residual AP117 violations

thinking
**Building a patch list**

I need to create a patch list for Volume I and inspect candidate compute files in the targeted list. I'll search for the exact content that needs changing, gathering line info and what to replace. It seems relevant snippets from my previous output might be enough for context, though I’ll want to ensure I gather the surrounding lines for the apply_patch. My potential patch set includes segments from several files that I'll need to open for further inspection.
exec
/bin/zsh -lc "nl -ba compute/lib/kz_monodromy_arithmetic_engine.py | sed -n '975,981p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_swiss_cheese_kontsevich_engine.py | sed -n '463,478p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/twisted_holography_mc.py | sed -n '54,60p;714,721p;784,791p;816,821p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/ordered_bar_descent_engine.py | sed -n '24,31p;272,276p;358,361p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/ordered_chiral_jones_engine.py | sed -n '20,26p;200,209p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_holographic_shadow_connection.py | sed -n '52,56p'; nl -ba compute/lib/holographic_shadow_connection.py | sed -n '1,9p;40,44p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/large_n_twisted_holography.py | sed -n '162,167p;676,699p'; nl -ba compute/lib/twisted_holography_engine.py | sed -n '900,905p'; nl -ba compute/tests/test_twisted_holography_mc.py | sed -n '278,282p'; nl -ba compute/lib/hitchin_shadow_engine.py | sed -n '773,778p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_dk0_evaluation_bridge_engine.py | sed -n '134,140p'; nl -ba compute/lib/theorem_three_way_r_matrix_engine.py | sed -n '390,395p'; nl -ba compute/lib/primitive_kernel_full.py | sed -n '870,881p'; nl -ba compute/lib/e1_nonsplitting_obstruction_engine.py | sed -n '662,667p'; nl -ba compute/lib/dmod_purity_char_variety_engine.py | sed -n '667,713p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   975	    """Verify the identification: KZ connection = shadow connection at genus 0.
   976	
   977	    The genus-0 arity-2 shadow connection on Conf_n(C) is:
   978	      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
   979	
   980	    This is EXACTLY the KZ connection. The identification:
   981	      r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
 succeeded in 50ms:
    54	  Quantum R-matrix: R(z) = 1 - hbar*P/z + O(hbar^2)
    55	  This satisfies the quantum YBE:
    56	    R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
    57	
    58	  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
    59	  gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
    60	  This is the Drinfeld-Kohno theorem, which in our framework is the statement
   714	      R(z) = 1 - hbar*P/z + hbar^2*(P^2/z^2 - ...) + ...
   715	      = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
   716	
   717	    The Drinfeld-Kohno theorem: monodromy of the KZ connection
   718	      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
   719	    gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
   720	    """
   721	    r = extract_collision_residue(A)
   784	def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
   785	    """Shadow connection nabla^{hol}_{0,n} at genus 0.
   786	
   787	    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
   788	
 succeeded in 51ms:
   463	        # AP41 (Vol II): R(z) = exp(kappa*hbar/z) for Heisenberg
   464	        z1, z2 = z_config[0], z_config[1]
   465	        dz = z1 - z2
   466	
   467	        # Monodromy phase from KZ connection
   468	        # The connection form is omega = kappa * d log(z_1 - z_2)
   469	        # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
   470	        monodromy_phase = cmath.exp(1j * math.pi * kappa)
   471	
   472	        return {
   473	            'path_type': 'braid',
   474	            'n_points': n,
   475	            'monodromy_phase': monodromy_phase,
   476	            'kappa': kappa,
   477	            'connection_form': f'kappa * d log(z1 - z2)',
   478	            'r_matrix_consistent': True,
 succeeded in 50ms:
    24	The bar complex at tensor degree n defines a local system on
    25	Conf_n^{ord}(C). To descend to Conf_n(C), one needs a Sigma_n-
    26	equivariant structure: the R-MATRIX.
    27	
    28	The R-matrix R(z) is the monodromy of the Kohno connection:
    29	  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
    30	where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
    31	
   272	        # where P_{12} is the permutation operator... no.
   273	
   274	        # Let me be precise.
   275	        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
   276	        # where r_{ij} = Omega inserted in slots i,j.
   358	        # Hmm, but that's for modules. For the BAR COMPLEX:
   359	        # The bar complex fibre at (z_1, z_2) is V x V = g x g.
   360	        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
   361	        # where r_{12}(z) : V x V -> V x V.
 succeeded in 52ms:
    20	   AP22: desuspension s^{-1} lowers degree by 1.
    21	
    22	2. KZ FLAT BUNDLE on Conf_3(C):
    23	   The ordered configuration space Conf_3(C) carries the KZ flat bundle
    24	   L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
    25	     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
    26	   where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
   200	    r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
   201	
   202	    The KZ connection is:
   203	      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
   204	
   205	    where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
   206	
   207	    AP148: KZ convention r(z) = Omega/((k+h^v)*z).
   208	    AP117: connection 1-form uses d log(z_i - z_j), which is the
   209	           Arnold form (bar-construction coefficient).
 succeeded in 50ms:
    52	# ========================================================================
    53	
    54	class TestHeisenbergFlatness:
    55	    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
    56	
     1	"""Holographic shadow connection: flat connections from the shadow obstruction tower.
     2	
     3	Verifies the geometric construction: the genus-0 shadow of the MC element
     4	Theta_A produces flat connections on conformal blocks.  For each standard
     5	family the shadow connection specialises to a classical object:
     6	
     7	  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
     8	                     (cor:shadow-connection-heisenberg)
     9	  - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
    40	class HeisenbergShadowConnection:
    41	    """Shadow connection for rank-1 Heisenberg at level kappa.
    42	
    43	    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
    44	
 succeeded in 51ms:
   162	class ShadowConnection:
   163	    """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
   164	
   165	    At genus 0, arity 2: specializes to KZ connection for affine algebras.
   166	    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
   167	
   676	def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
   677	    """The shadow connection at genus 0, arity 2.
   678	
   679	    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
   680	    For affine algebras this is the KZ connection at the scalar level.
   681	    Flatness is automatic (scalar on configuration space of 2 points).
   682	    """
   683	    kap = kappa_from_data(A)
   684	    is_affine = (A.dim > 0 and A.dual_coxeter > 0)
   685	    return ShadowConnection(
   686	        genus=0,
   687	        arity=2,
   688	        kappa_value=kap,
   689	        is_kz_type=is_affine,
 succeeded in 51ms:
   134	@dataclass
   135	class KZData:
   136	    """Data for the KZ connection associated to V_k(g).
   137	
   138	    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
   139	
   140	    For two-point (z = z_1 - z_2):
   390	
   391	        Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
   392	        where Omega = sum_a t^a tensor t^a is the Casimir tensor.
   393	        The normalization 1/(k + h^v) comes from the KZ equation, which
   394	        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
   395	
   870	                       ) -> Dict[str, Any]:
   871	    """KZ connection data for affine sl_N at level k.
   872	
   873	    The KZ connection at genus 0 with n marked points is:
   874	        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
   875	
   876	    where:

thinking
**Searching for updates**

I think I need to search for the `connection_form` or perhaps `d log(z1 - z2)` to check for any updates related to those tests. It seems like I'm looking through the current repository to find relevant information. It’s important to ensure everything is up to date, especially since I want to make sure the tests function properly. Let’s get that search going!
exec
/bin/zsh -lc "rg -n \"kappa \\* d log\\(z1 - z2\\)|dlog\\(z_i - z_j\\)|d log\\(z_i - z_j\\)|dlog\\(z12\\)|d log\\(z_1 - z_2\\)|dlog\\(z_1 - z_2\\)\" compute" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/bv_bar_class_m_engine.py:516:    where eta_{ij} = d log(z_i - z_j).
compute/lib/large_n_twisted_holography.py:166:    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
compute/lib/large_n_twisted_holography.py:679:    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
compute/lib/large_n_twisted_holography.py:718:    where omega_ij = dlog(z_i - z_j).
compute/lib/exceptional_yangian_engine.py:788:    extracts residues along d log(z_i - z_j), which absorbs one power.
compute/lib/theorem_gz_frontier_engine.py:395:        #   w = sum_{i<j} gamma_{ij} d log(z_i - z_j)
compute/lib/theorem_gz_frontier_engine.py:401:        # Then w = -2h/(n-2) * sum_{i<j} d log(z_i - z_j)
compute/lib/virasoro_bar_zhu.py:1110:    # - The differential D uses d log(z_i - z_j) forms, which are
compute/lib/theorem_open_closed_rectification_engine.py:984:    The bar construction extracts residues along d log(z_i - z_j).
compute/lib/twisted_holography_engine.py:904:      nabla is just d - kappa * sum dlog(z_i - z_j).
compute/lib/celestial_arithmetic_engine.py:74:AP19 WARNING: The bar construction extracts residues along d log(z_i - z_j),
compute/lib/mzv_bar_complex.py:38:AP19 WARNING: The bar complex extracts RESIDUES along d log(z_i - z_j).
compute/lib/mzv_bar_complex.py:443:    The bar amplitude extracts the propagator form d log(z_i - z_j),
compute/lib/mzv_bar_complex.py:447:    The bar propagator is d log(z_i - z_j) = dz/(z_i - z_j).
compute/lib/mzv_bar_complex.py:485:        # kappa * int_{M_{0,4}} d log(z_1 - z_2) wedge d log(z_3 - z_4)
compute/lib/mzv_bar_complex.py:550:    The bar propagator d log(z_i - z_j) extracts the residue, absorbing one
compute/lib/shadow_mzv_engine.py:923:    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
compute/lib/holographic_shadow_connection.py:7:  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
compute/lib/holographic_shadow_connection.py:43:    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
compute/lib/holographic_shadow_connection.py:110:        follows from the fact that dlog(z_i - z_j) ^ dlog(z_j - z_k) is

thinking
**Clarifying findings focus**

The user has asked for findings. I think it makes sense to focus on the manuscripts and the most direct compute libraries. But the completeness contract says it should be exhaustive, which is tricky. It seems "all volumes" might refer to three manuscripts rather than the compute layer. The user probably means to search the LaTeX volumes, not all code. Since there’s a mention of AP117 and a mathematical phrase, I might consider updating a few exposed compute files, but that’s optional.
codex
I’ve isolated the manuscript violations cleanly. Before I fan out the full patch set, I’m testing whether the sibling volume trees are writable in this sandbox; if they are, I’ll patch Vol II and Vol III in the same pass, otherwise I’ll finish Vol I and report the exact external files blocked by sandboxing.
codex
The sandbox blocks writes outside `/Users/raeez/chiral-bar-cobar`, so Vol II and Vol III cannot be edited from this session. I’m finishing the full current-repo AP117 cleanup now and I’ll include the exact blocked external files and line references in the close-out.
exec
/bin/zsh -lc "rg -n \"connection_form|kappa \\* dz12|kappa \\* d log\\(z1 - z2\\)|d - kappa \\* sum dlog|dlog\\(z_i - z_j\\)|d log\\(z_i - z_j\\)\" compute/tests compute/lib | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/celestial_arithmetic_engine.py:74:AP19 WARNING: The bar construction extracts residues along d log(z_i - z_j),
compute/lib/theorem_open_closed_rectification_engine.py:984:    The bar construction extracts residues along d log(z_i - z_j).
compute/lib/theorem_gz_frontier_engine.py:395:        #   w = sum_{i<j} gamma_{ij} d log(z_i - z_j)
compute/lib/theorem_gz_frontier_engine.py:401:        # Then w = -2h/(n-2) * sum_{i<j} d log(z_i - z_j)
compute/lib/bv_bar_class_m_engine.py:516:    where eta_{ij} = d log(z_i - z_j).
compute/lib/mzv_bar_complex.py:38:AP19 WARNING: The bar complex extracts RESIDUES along d log(z_i - z_j).
compute/lib/mzv_bar_complex.py:443:    The bar amplitude extracts the propagator form d log(z_i - z_j),
compute/lib/mzv_bar_complex.py:447:    The bar propagator is d log(z_i - z_j) = dz/(z_i - z_j).
compute/lib/mzv_bar_complex.py:550:    The bar propagator d log(z_i - z_j) extracts the residue, absorbing one
compute/lib/modular_koszul_engine.py:161:    connection_form_expr: Any = None
compute/lib/modular_koszul_engine.py:431:    # connection_form = Q'/(2Q) where Q = Q_L(t)
compute/lib/modular_koszul_engine.py:447:        'connection_form_expr': conn,
compute/lib/modular_koszul_engine.py:679:        connection_form_expr=s5['connection_form_expr'],
compute/lib/twisted_holography_engine.py:904:      nabla is just d - kappa * sum dlog(z_i - z_j).
compute/tests/test_shadow_connection.py:30:    connection_form,
compute/tests/test_shadow_connection.py:31:    connection_form_from_data,
compute/tests/test_shadow_connection.py:46:    virasoro_connection_form,
compute/tests/test_shadow_connection.py:56:    w3_wline_connection_form,
compute/tests/test_shadow_connection.py:146:    def test_connection_form_definition(self):
compute/tests/test_shadow_connection.py:149:        omega = connection_form(Q)


thinking
**Evaluating Kohno connection formula**

I'm trying to clarify the Kohno connection formula, which is `d - \sum hbar r_{ij}(z_{ij}) dz_{ij}`. It seems like `r_{ij}` might be defined as Omega in slots i and j. I'm contemplating if the formula should actually be `hbar * r_{ij}/z_{ij} * dz_{ij}` if `r_{ij}` is a constant Omega. I really need to inspect the semantics of this, especially around line 275 to confirm that.
thinking
**Considering patch strategy**

I’m realizing that because this patch is huge, it carries a risk of mistakes. It might be better to use smaller patches in groups instead. I could tackle one for the survey and another for the compute files. Starting with the current manuscript in the repo and the compute group seems more manageable. I’ll have to trust the lines and use apply_patch for those multi-file updates. Let's proceed thoughtfully!
codex
I’ve cut the current-repo scope down to live AP117 teaching surfaces only: manuscript formulas plus compute docstrings/comments that explicitly present `d\\log(z_i-z_j)` as a KZ or shadow connection form. I’m patching those now.
file update
M /Users/raeez/chiral-bar-cobar/compute/lib/dmod_filtration_ss_engine.py
@@ -438,3 +438,3 @@
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
M /Users/raeez/chiral-bar-cobar/compute/lib/ordered_chiral_jones_engine.py
@@ -24,3 +24,3 @@
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
@@ -202,3 +202,3 @@
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
@@ -207,4 +207,4 @@
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
M /Users/raeez/chiral-bar-cobar/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -977,3 +977,3 @@
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -137,3 +137,3 @@
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
M /Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py
@@ -28,3 +28,3 @@
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
@@ -274,3 +274,3 @@
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
@@ -359,3 +359,3 @@
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
M /Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py
@@ -165,3 +165,3 @@
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
@@ -678,3 +678,3 @@
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
@@ -696,3 +696,3 @@
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
M /Users/raeez/chiral-bar-cobar/compute/lib/primitive_kernel_full.py
@@ -873,3 +873,3 @@
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
@@ -880,3 +880,3 @@
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
M /Users/raeez/chiral-bar-cobar/compute/tests/test_holographic_shadow_connection.py
@@ -54,3 +54,3 @@
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -393,3 +393,3 @@
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
M /Users/raeez/chiral-bar-cobar/compute/lib/dmod_purity_char_variety_engine.py
@@ -670,3 +670,3 @@
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
@@ -712,3 +712,3 @@
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
M /Users/raeez/chiral-bar-cobar/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -665,3 +665,3 @@
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
M /Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex
@@ -4739,3 +4739,3 @@
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
@@ -7234,3 +7234,3 @@
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
@@ -7238,4 +7238,4 @@
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
@@ -7541,3 +7541,3 @@
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -467,3 +467,3 @@
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
@@ -476,3 +476,3 @@
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
M /Users/raeez/chiral-bar-cobar/compute/lib/twisted_gauge_defects_engine.py
@@ -1282,3 +1282,3 @@
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
M /Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py
@@ -57,3 +57,3 @@
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
@@ -717,3 +717,3 @@
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
@@ -786,6 +786,6 @@
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
@@ -818,4 +818,4 @@
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
M /Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_engine.py
@@ -903,3 +903,3 @@
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
M /Users/raeez/chiral-bar-cobar/compute/tests/test_twisted_holography_mc.py
@@ -280,3 +280,3 @@
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
M /Users/raeez/chiral-bar-cobar/compute/lib/geometric_langlands_shadow_engine.py
@@ -1230,3 +1230,3 @@
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
M /Users/raeez/chiral-bar-cobar/compute/lib/hitchin_shadow_engine.py
@@ -776,3 +776,3 @@
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
M /Users/raeez/chiral-bar-cobar/compute/lib/shadow_mzv_engine.py
@@ -922,3 +922,3 @@
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
M /Users/raeez/chiral-bar-cobar/compute/lib/holographic_shadow_connection.py
@@ -6,3 +6,3 @@
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
@@ -42,3 +42,3 @@
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
apply_patch(auto_approved=true) exited 0 in 135ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex
M /Users/raeez/chiral-bar-cobar/compute/lib/dmod_filtration_ss_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/geometric_langlands_shadow_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/kz_monodromy_arithmetic_engine.py
M /Users/raeez/chiral-bar-cobar/compute/tests/test_holographic_shadow_connection.py
M /Users/raeez/chiral-bar-cobar/compute/lib/holographic_shadow_connection.py
M /Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py
M /Users/raeez/chiral-bar-cobar/compute/lib/ordered_chiral_jones_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_dk0_evaluation_bridge_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/e1_nonsplitting_obstruction_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/dmod_purity_char_variety_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/primitive_kernel_full.py
M /Users/raeez/chiral-bar-cobar/compute/lib/shadow_mzv_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_three_way_r_matrix_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py
M /Users/raeez/chiral-bar-cobar/compute/lib/hitchin_shadow_engine.py
M /Users/raeez/chiral-bar-cobar/compute/lib/twisted_gauge_defects_engine.py
M /Users/raeez/chiral-bar-cobar/compute/tests/test_twisted_holography_mc.py
file update:
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;

file update:
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;

codex
The first patch wave is in. I’m rerunning the same AP117 grep against the current repo now; anything still showing up is either a missed live violation or a false positive I need to classify before I stop.
exec
/bin/zsh -lc "rg -n -P '(nabla|KZ|connection).{0,120}d ?log\\(z|d ?log\\(z.{0,120}(nabla|KZ|connection)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone /Users/raeez/chiral-bar-cobar/compute/lib /Users/raeez/chiral-bar-cobar/compute/tests" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_comparison_test.py:395:    nabla^arith_H = d - dlog(zeta(s)*zeta(s+1)) ds.
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_comparison_test.py:433:    nabla^arith_aff = d - dlog(zeta(s)*zeta(s-1)) ds.
/Users/raeez/chiral-bar-cobar/compute/tests/test_arithmetic_shadow_connection.py:537:        The connection form dlog(zeta(s)*zeta(s+1)) has a pole at s=1
/Users/raeez/chiral-bar-cobar/compute/tests/test_arithmetic_comparison_explicit_engine.py:80:    nabla^arith = d - d log(zeta(s)*zeta(s+1)) ds.
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_comparison_explicit_engine.py:225:      nabla^arith_H = d - d log(zeta(s)*zeta(s+1)) ds
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_shadow_connection.py:202:    But the connection form d log(zeta*zeta(s+1)) is regular at generic s.
/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:572:        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:1354:        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
file update:
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;

exec
/bin/zsh -lc "nl -ba compute/lib/bc_mzv_shadow_engine.py | sed -n '568,574p;1351,1356p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   568	        # The d-log form on M_{0,4} integrates to zeta(2) after regularization.
   569	        # The bar amplitude with a single internal edge (channel s, t, or u)
   570	        # weighted by the r-matrix gives:
   571	        #   ell_T = kappa * zeta(2)  (for the s-channel tree)
   572	        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
   573	        # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
   574	        z2 = mzv((2,))
  1351	
  1352	    if n == 4:
  1353	        # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
  1354	        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
  1355	        # Period: int_0^1 omega regularized = zeta(2).
  1356	        # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
file update:
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;

file update
M /Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py
@@ -571,3 +571,3 @@
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
@@ -1353,3 +1353,3 @@
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
apply_patch(auto_approved=true) exited 0 in 122ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py
file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;

file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;


thinking
**Re-evaluating repo search**

I think I need to rerun the current repository search using grep but focus specifically on the arithmetic zeta lines. I wonder if this approach will yield better results. It could help pinpoint any issues or relevant code snippets more efficiently. The search might need some refining. So, let's see if I can make this query more targeted to get the information I’m looking for!
exec
/bin/zsh -lc "rg -n -P '(nabla|KZ|connection).{0,120}d ?log\\(z|d ?log\\(z.{0,120}(nabla|KZ|connection)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/appendices /Users/raeez/chiral-bar-cobar/standalone /Users/raeez/chiral-bar-cobar/compute/lib /Users/raeez/chiral-bar-cobar/compute/tests" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/compute/tests/test_arithmetic_shadow_connection.py:537:        The connection form dlog(zeta(s)*zeta(s+1)) has a pole at s=1
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_comparison_test.py:395:    nabla^arith_H = d - dlog(zeta(s)*zeta(s+1)) ds.
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_comparison_test.py:433:    nabla^arith_aff = d - dlog(zeta(s)*zeta(s-1)) ds.
/Users/raeez/chiral-bar-cobar/compute/tests/test_arithmetic_comparison_explicit_engine.py:80:    nabla^arith = d - d log(zeta(s)*zeta(s+1)) ds.
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_shadow_connection.py:202:    But the connection form d log(zeta*zeta(s+1)) is regular at generic s.
/Users/raeez/chiral-bar-cobar/compute/lib/arithmetic_comparison_explicit_engine.py:225:      nabla^arith_H = d - d log(zeta(s)*zeta(s+1)) ds
file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;




thinking
**Considering git diff and edits**

I could use `git diff --unified=0 -- file...` or even `nl -ba` for changed sections. My goal is to gather exact lines and edits, possibly with commands like `git diff --unified=0 -- standalone/survey... compute/lib/...`. The potential output could be large, but I want the final answer to cite original line numbers. It's also important to note that for blocked files, no edits can be applied, so I'd have to mention that.
thinking
**Considering edits and blocked files**

I need to search external Vol II/III for any remaining findings, but I can't edit directly, so I'll need to list the problems at file:line and indicate that edits are blocked. The task is to fix them, but since I'm limited by the sandbox, I can still mention exact textual replacements. However, the user specifically wants the exact edits applied, so I should clarify which edits were not applied while still including the proposed changes for clarity.
thinking
**Verifying Python syntax**

I'm considering verifying that there are no syntax errors in the edited Python files. I'll run `python -m py_compile` on the changed compute libraries and tests. I might need to use `python3` for compatibility. I’ll list all the changed Python files in the current repository—there are probably around 20 files, which feels manageable. I don’t need to worry about the .tex files. So, let’s run `compileall` to check everything!
codex
The AP117 grep is now clean on the current repo except for arithmetic `d\\log\\Lambda(s)` connections on the `s`-line, which are a different class of log connection and not the Arnold/KZ confusion. I’m doing one narrow syntax check on the edited Python files, then I’ll assemble the exact findings list and the external-volume blockers.
exec
/bin/zsh -lc 'python3 -m py_compile compute/lib/dmod_filtration_ss_engine.py compute/lib/geometric_langlands_shadow_engine.py compute/lib/theorem_swiss_cheese_kontsevich_engine.py compute/lib/ordered_bar_descent_engine.py compute/lib/kz_monodromy_arithmetic_engine.py compute/tests/test_holographic_shadow_connection.py compute/lib/holographic_shadow_connection.py compute/lib/twisted_holography_mc.py compute/lib/ordered_chiral_jones_engine.py compute/lib/theorem_dk0_evaluation_bridge_engine.py compute/lib/e1_nonsplitting_obstruction_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/primitive_kernel_full.py compute/lib/shadow_mzv_engine.py compute/lib/twisted_holography_engine.py compute/lib/theorem_three_way_r_matrix_engine.py compute/lib/large_n_twisted_holography.py compute/lib/hitchin_shadow_engine.py compute/lib/twisted_gauge_defects_engine.py compute/tests/test_twisted_holography_mc.py compute/lib/bc_mzv_shadow_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;


thinking
**Considering git diff options**

I think I need to use `git diff --unified=0` for checking changed files. Maybe I can group the diffs. By specifying `-- <files>`, I can keep the output long, but still manageable, within 20,000 tokens. It's important to reference the final lines and exact edits applied. I could try using `git diff --unified=0 -- compute/lib/... standalone/...` for the entire repository. Alright, let’s proceed with making that call!
exec
/bin/zsh -lc 'git diff --unified=0 -- standalone/survey_modular_koszul_duality.tex compute/lib/dmod_filtration_ss_engine.py compute/lib/geometric_langlands_shadow_engine.py compute/lib/theorem_swiss_cheese_kontsevich_engine.py compute/lib/ordered_bar_descent_engine.py compute/lib/kz_monodromy_arithmetic_engine.py compute/tests/test_holographic_shadow_connection.py compute/lib/holographic_shadow_connection.py compute/lib/twisted_holography_mc.py compute/lib/ordered_chiral_jones_engine.py compute/lib/theorem_dk0_evaluation_bridge_engine.py compute/lib/e1_nonsplitting_obstruction_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/primitive_kernel_full.py compute/lib/shadow_mzv_engine.py compute/lib/twisted_holography_engine.py compute/lib/theorem_three_way_r_matrix_engine.py compute/lib/large_n_twisted_holography.py compute/lib/hitchin_shadow_engine.py compute/lib/twisted_gauge_defects_engine.py compute/tests/test_twisted_holography_mc.py compute/lib/bc_mzv_shadow_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a..ceaf14b 100644
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -572 +572 @@ def tree_amplitude_mzv(n: int, family: str = 'virasoro',
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
@@ -1354 +1354 @@ def period_matrix(n: int) -> Dict[str, Any]:
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9f..922a719 100644
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -439 +439 @@ def kz_connection_matrix(k: Rational, n: int,
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf31..21e9519 100644
--- a/compute/lib/dmod_purity_char_variety_engine.py
file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;


thinking
**Updating plans and statuses**

I need to clarify the status of my current repo and work on volume 2 and 3, which are blocked. I should reference the file and line as part of my intended changes, but I don't want to label it as "applied" just yet. It might be useful to update the plan's status and note what's blocked. This should help keep everything organized and clear for future reference!
Plan update
Current-repo AP117 surfaces are patched and the targeted grep is clean there except for unrelated arithmetic `d\log\Lambda(s)` connections. Vol II and Vol III remain read-only under the sandbox, so those fixes are blocked despite verification of the exact offending lines.
  ✓ Patch verified Vol I AP117 manuscript and compute surfaces
  • Patch verified Vol II AP117 manuscript and compute surfaces
  • Patch verified Vol III AP117 manuscript and compute surfaces
  ✓ Re-run targeted cross-volume grep for residual AP117 violations
file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;

exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py | sed -n '1,8p;192,196p;577,581p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py | sed -n '923,927p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/compute/lib/non_simply_laced_rmatrix.py | sed -n '1028,1032p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	"""Log HT Monodromy Engine: KZ connections, braid relations, and Yang-Baxter.
     2	
     3	Implements chain-level computations for the logarithmic holomorphic-topological
     4	monodromy chapter (log_ht_monodromy_core.tex), verifying:
     5	
     6	1. KZ connection flatness: (d - sum Omega_{ij} dlog(z_ij))^2 = 0
     7	2. Infinitesimal braid relations: [Omega_{12}, Omega_{13} + Omega_{23}] = 0
     8	3. Bar insertion identity at arity 2
   192	
   193	    The KZ connection:
   194	    nabla = d - (Omega_12 dlog(z_12) + Omega_13 dlog(z_13) + Omega_23 dlog(z_23))
   195	
   196	    Flatness F = 0 requires:
   577	
   578	    The KZ connection is:
   579	      nabla = d - Omega_12 dlog(z12) - Omega_13 dlog(z13) - Omega_23 dlog(z23)
   580	
   581	    Flatness requires:
   923	    r"""Verify flatness of nabla^hol at genus 0, arity n.
   924	
file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;








thinking
**Evaluating final edits**

I’m thinking about whether I need to compute for volume three, and it seems fairly straightforward. I might need to present the candidate lines for edits, but they haven't been applied yet. Maybe I should indicate them as blocked, specifying the exact edits and noting anything external that’s blocked. It would help to give the user a brief note about what's blocked. I should gather the current repo's changed file line numbers and ensure transparency while ignoring unrelated changes.
thinking
**Organizing findings**

I’m considering including file links in the final output, using absolute path targets for clarity. Since I want to keep things concise, a flat list could work, but with 23 findings plus blocked externals, it might get lengthy. So, I might group findings into "Applied in current repo" and "Blocked outside writable root," using bullets for each. Each bullet would summarize the problem and the exact edit. If there are multiple changes in the same file, I could cluster them to reduce the overall length.
thinking
**Grouping findings by file**

I'm noticing many compute files have similar docstring lines. The user mentioned needing a format where each finding includes "PROBLEM at file:line" and the exact edit applied, which implies a one-line approach for each logical finding. I think I can group findings by file, so each bullet point could contain multiple line references instead. Keeping it clear and not nesting the information should help present it neatly for the user!
thinking
**Considering file organization**

I’m planning to mention a syntax check and maybe verify with grep. That seems helpful! I need to decide whether to include an external blocked files list grouped by file. Should I not list every compute file outside the root? Maybe it makes sense to include them. It could be beneficial to group by file and refer to multiple lines. There’s a balance to strike in clarity versus completeness!
thinking
**Consolidating code edits**

I’m considering if I could group multiple compute files under one bullet point when the edit pattern is identical. For example, mentioning files like "dmod_filtration_ss_engine.py" and others that all had similar changes. I could note that the KZ docstrings used the expression `Omega d log(z)` and specify the exact edit made, which was rewriting to `(Omega/(z_i-z_j)) d(z_i-z_j)` while also correcting a related explanatory sentence. This way, I can significantly reduce length!
thinking
**Considering edits and format**

I'm thinking of using lines from diff for our edits, which seems like a fine approach. Maybe I could include information about the blocked volumes in a brief paragraph instead of making a bullet list for every compute file. It might make things clearer and more concise that way! Let's keep it straightforward while ensuring all necessary details are included. I want to present it effectively for the user.
thinking
**Clarifying repository status**

I need to mention that the current repository verification is clean except for the arithmetic `d\log \Lambda(s)` lines on the s-line, which I intentionally excluded. This detail is important! I'll also note that external volumes are blocked due to sandbox and approval policy. It’s good to remember not to start with "Done" or similar phrases; I could just say something like, "Current repo AP117 surfaces are fixed," which feels more direct.
codex
**Applied**
- PROBLEM at [survey_modular_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:4740), [same file](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7235), and [same file](/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:7542): the standalone still wrote KZ/shadow connections as `... d\log(...)` and later dropped `dz` entirely. EXACT edit applied: `\Omega_{ij}\,d\log(z_i-z_j)` -> `(\Omega_{ij}/(z_i-z_j))\,d(z_i-z_j)`, `\sum r_{ij}(z_{ij})\,d\log(z_{ij})` -> `\sum r_{ij}(z_{ij})\,dz_{ij}`, clarified `r_{ij}(z)=\Omega_{ij}/((h^\vee+k)z)`, and `d-\hbar\Omega/z` -> `d-(\hbar\Omega/z)\,dz`.
- PROBLEM at [ordered_bar_descent_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py:29), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py:275), and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_bar_descent_engine.py:360): Kohno/bar flat-connection comments used `d log(z)`. EXACT edit applied: rewrote them to `r(z)\,d(z)` or `dz_{ij}/z_{ij}`.
- PROBLEM at [dmod_filtration_ss_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/dmod_filtration_ss_engine.py:439), [theorem_dk0_evaluation_bridge_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_dk0_evaluation_bridge_engine.py:138), [primitive_kernel_full.py](/Users/raeez/chiral-bar-cobar/compute/lib/primitive_kernel_full.py:874), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/primitive_kernel_full.py:881), [theorem_three_way_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_three_way_r_matrix_engine.py:394), [twisted_gauge_defects_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_gauge_defects_engine.py:1283), [geometric_langlands_shadow_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/geometric_langlands_shadow_engine.py:1231), [kz_monodromy_arithmetic_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/kz_monodromy_arithmetic_engine.py:978), and [ordered_chiral_jones_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_chiral_jones_engine.py:25): KZ docstrings/strings still taught `\Omega\,d\log(z)`. EXACT edit applied: rewrote each to rational `dz/z` form, i.e. `(\Omega_{ij}/(z_i-z_j))\,d(z_i-z_j)`; in [ordered_chiral_jones_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/ordered_chiral_jones_engine.py:208) I also corrected the AP117 explanation to say `d\log(z_i-z_j)` is the Arnold bar coefficient, not the connection one-form.
- PROBLEM at [holographic_shadow_connection.py](/Users/raeez/chiral-bar-cobar/compute/lib/holographic_shadow_connection.py:7), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/holographic_shadow_connection.py:43), [large_n_twisted_holography.py](/Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py:166), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py:679), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/large_n_twisted_holography.py:697), [twisted_holography_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_engine.py:904), [hitchin_shadow_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/hitchin_shadow_engine.py:777), [twisted_holography_mc.py](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:58), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:718), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:787), [same file](/Users/raeez/chiral-bar-cobar/compute/lib/twisted_holography_mc.py:819), [test_holographic_shadow_connection.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_holographic_shadow_connection.py:55), and [test_twisted_holography_mc.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_twisted_holography_mc.py:281): shadow/Heisenberg connection docs still used `d-\kappa\sum dlog(z_{ij})`. EXACT edit applied: rewrote them to `dz/z` form or `r(z_{ij})\,dz_{ij}` throughout.
- PROBLEM at [theorem_swiss_cheese_kontsevich_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_swiss_cheese_kontsevich_engine.py:468) and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_swiss_cheese_kontsevich_engine.py:477): the displayed/returned connection form was `kappa * d log(z1-z2)`. EXACT edit applied: changed both to `kappa * d(z1 - z2)/(z1 - z2)`.
- PROBLEM at [dmod_purity_char_variety_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/dmod_purity_char_variety_engine.py:671) and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/dmod_purity_char_variety_engine.py:713): the Heisenberg flat connection was still described with `d log(z_i-z_j)`. EXACT edit applied: `d + k * sum d log(z_i - z_j)` -> `d + k * sum d(z_i - z_j)/(z_i - z_j)`.
- PROBLEM at [e1_nonsplitting_obstruction_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/e1_nonsplitting_obstruction_engine.py:666): the `sl_2` KZ line still used `Omega_12 dlog(z12)` and `Omega_23 dlog(z23)`. EXACT edit applied: rewrote it as `(Omega_12/z12) dz12 + (Omega_23/z23) dz23`.
- PROBLEM at [bc_mzv_shadow_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:572) and [same file](/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:1354): the KZ diagonal 1-form was still written with `d log`. EXACT edit applied: rewrote it as `dz/z - dz/(1-z)`.

**Blocked**
- PROBLEM at [bar-cobar-review.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2606), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:2868), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex:3246), [thqg_celestial_holography_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:615), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:1083), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:1289), [dnp_identification_master.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/dnp_identification_master.tex:342), [log_ht_monodromy_core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1525), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1787), [log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:1402), [twisted_holography_quantum_gravity.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1908), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:1936), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2240), [introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1535), [ordered_associative_chiral_kd_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:1780), [rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1197), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1339), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5075), [spectral-braiding-core.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2524), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2667), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:2750), [thqg_line_operators_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:502), [same file](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1112), and [preface_full_survey.tex](/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:514): verified AP117 violations remain. No edit applied because sibling repos are outside the writable root and the sandbox rejects those writes.
- PROBLEM at [log_ht_monodromy_engine.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:6), [same file](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:194), [same file](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/log_ht_monodromy_engine.py:579), [holographic_ht_engine.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/holographic_ht_engine.py:925), [non_simply_laced_rmatrix.py](/Users/raeez/chiral-bar-cobar-vol2/compute/lib/non_simply_laced_rmatrix.py:1031), and [test_semisimple_purity.py](/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_semisimple_purity.py:41): verified AP117 compute/docstring violations remain. No edit applied for the same sandbox reason.
- PROBLEM at [cy_holographic_datum_master.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:713) and [theory_drinfeld_chiral_center.tex](/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:372), [same file](/Users/raeez/calabi-yau-quantum-groups/notes/theory_drinfeld_chiral_center.tex:493): verified Vol III manuscript/notes violations remain. No edit applied because that repo is outside the writable root.
- PROBLEM at [kazhdan_lusztig_shadow.py](/Users/raeez/calabi-yau-quantum-groups/compute/lib/kazhdan_lusztig_shadow.py:332) and [twisted_holography_cy3_engine.py](/Users/raeez/calabi-yau-quantum-groups/compute/lib/twisted_holography_cy3_engine.py:779): verified Vol III compute/docstring violations remain. No edit applied because that repo is outside the writable root.

**Verification**
Targeted AP117 grep is now clean in `/Users/raeez/chiral-bar-cobar` except for unrelated arithmetic `d\log\Lambda(s)` connections on the `s`-line, and `python3 -m py_compile` passed on all edited Python files.
file update:
diff --git a/compute/lib/bc_mzv_shadow_engine.py b/compute/lib/bc_mzv_shadow_engine.py
index afd662a4d6efcf05bc5699d032c161d29b422237..ceaf14ba90f4a29559ad91e3bc0f6b7d517d82a9
--- a/compute/lib/bc_mzv_shadow_engine.py
+++ b/compute/lib/bc_mzv_shadow_engine.py
@@ -569,7 +569,7 @@
         # The bar amplitude with a single internal edge (channel s, t, or u)
         # weighted by the r-matrix gives:
         #   ell_T = kappa * zeta(2)  (for the s-channel tree)
-        # More precisely: the KZ regularized integral of d log(z)/(1-z) on [0,1]
+        # More precisely: the KZ regularized integral of dz/z - dz/(1-z) on [0,1]
         # gives -zeta(2).  The bar complex extracts this with the appropriate sign.
         z2 = mzv((2,))
         result['amplitude'] = kappa * z2
@@ -1351,7 +1351,7 @@
 
     if n == 4:
         # M_{0,4}: 1-dimensional, de Rham H^1 has dim 1 (after SL_2 reduction).
-        # Basis: omega = d log(z) - d log(1-z) (the KZ 1-form on the diagonal).
+        # Basis: omega = dz/z - dz/(1-z) (the KZ 1-form on the diagonal).
         # Period: int_0^1 omega regularized = zeta(2).
         # More precisely: the period of the d-log form on M_{0,4} is 2*pi*i
         # in H^1, but the MZV content comes from the real part.
diff --git a/compute/lib/dmod_filtration_ss_engine.py b/compute/lib/dmod_filtration_ss_engine.py
index 981df9ffcc4746e82819538d862fdde31c91496b..922a7190fab293e15214884b1986f7f3f6c64c9b
--- a/compute/lib/dmod_filtration_ss_engine.py
+++ b/compute/lib/dmod_filtration_ss_engine.py
@@ -436,7 +436,7 @@
                          reps: Optional[List[int]] = None) -> Dict[str, Any]:
     """KZ connection data for V_k(sl_2) on n points.
 
-    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - 1/(k+2) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} is the Casimir acting on the i-th and j-th tensor
     factors of V_{lambda_1} tensor ... tensor V_{lambda_n}.
diff --git a/compute/lib/dmod_purity_char_variety_engine.py b/compute/lib/dmod_purity_char_variety_engine.py
index 5cecf3160cd2362961f8243e629500038fd49821..21e951936b4935a9c1dd3ff0c4542a47c0de114d
--- a/compute/lib/dmod_purity_char_variety_engine.py
+++ b/compute/lib/dmod_purity_char_variety_engine.py
@@ -668,7 +668,7 @@
 
       FH_n(H_k) = O_{Conf_n} (free D-module, rank 1)
 
-    with the connection d + k * sum_{i<j} d log(z_i - z_j).
+    with the connection d + k * sum_{i<j} d(z_i - z_j)/(z_i - z_j).
 
     This is a FLAT connection (curvature = 0 at genus 0).
     The characteristic variety of a flat connection on a vector
@@ -710,7 +710,7 @@
         "curvature_genus_g": f"kappa * omega_g = {kappa} * omega_g",
         "shadow_depth": 2,  # class G, terminates at arity 2
         "note": ("Free D-module: Ch = zero section. Maximally pure. "
-                 "The flat connection d + k * sum d log(z_i - z_j) "
+                 "The flat connection d + k * sum d(z_i - z_j)/(z_i - z_j) "
                  "has trivial characteristic variety."),
     }
 
diff --git a/compute/lib/e1_nonsplitting_obstruction_engine.py b/compute/lib/e1_nonsplitting_obstruction_engine.py
index e156824fd24d707d4b86e095e07053e29e05c465..b594f602314f6bd67bbdf53e6de4e9168ef68be7
--- a/compute/lib/e1_nonsplitting_obstruction_engine.py
+++ b/compute/lib/e1_nonsplitting_obstruction_engine.py
@@ -663,7 +663,7 @@
     r"""Analyze the Drinfeld associator's position relative to ker(av).
 
     For sl_2 at level k, the KZ connection on Conf_3(C) is:
-        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
+        nabla_KZ = d - (1/(k+h^v)) ((Omega_12/z12) dz12 + (Omega_23/z23) dz23)
 
     The monodromy representation factors through the braid group B_3.
     The associator Phi_KZ is the regularized holonomy from 0 to 1
diff --git a/compute/lib/geometric_langlands_shadow_engine.py b/compute/lib/geometric_langlands_shadow_engine.py
index b446eff0f2c50045da9b86673d31f972c431ede2..e4e078c8ae1da536c55f07e2190f71b1fcb5fb31
--- a/compute/lib/geometric_langlands_shadow_engine.py
+++ b/compute/lib/geometric_langlands_shadow_engine.py
@@ -1228,7 +1228,7 @@
                 '(genus-0 binary shadow)'
             ),
             'geom_langlands': (
-                'KZ connection nabla = d - Omega/(k+h^v) dlog(z_i-z_j). '
+                'KZ connection nabla = d - (Omega/((k+h^v)(z_i-z_j))) d(z_i-z_j). '
                 'Monodromy = quantum group R-matrix (Kohno-Drinfeld).'
             ),
         },
diff --git a/compute/lib/hitchin_shadow_engine.py b/compute/lib/hitchin_shadow_engine.py
index 6d7f1c4ec6ac507b249561ea72e49cd1939b2844..76f382f70bb1616e7ba2b0d7a8268290bf28fc74
--- a/compute/lib/hitchin_shadow_engine.py
+++ b/compute/lib/hitchin_shadow_engine.py
@@ -774,7 +774,7 @@
     r"""Verify: shadow connection at genus 0, arity 2 = KZ connection.
 
     The shadow connection at genus 0, arity 2 is:
-        nabla^{sh}_{0,2} = d - kappa * (d log(z_i - z_j))
+        nabla^{sh}_{0,2} = d - (kappa/(z_i - z_j)) d(z_i - z_j)
 
     The KZ connection is:
         nabla_{KZ} = d - (1/(k+h^v)) * sum Omega_{ij} / (z_i - z_j) dz_j
diff --git a/compute/lib/holographic_shadow_connection.py b/compute/lib/holographic_shadow_connection.py
index d9c8ed3be39eefafabc51c3a66eece726ba27663..f3c95f2c1dac350268c45a2e805ce61084468579
--- a/compute/lib/holographic_shadow_connection.py
+++ b/compute/lib/holographic_shadow_connection.py
@@ -4,7 +4,7 @@
 Theta_A produces flat connections on conformal blocks.  For each standard
 family the shadow connection specialises to a classical object:
 
-  - Heisenberg:      nabla = d - kappa sum q_i q_j dlog(z_i - z_j)
+  - Heisenberg:      nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j)
                      (cor:shadow-connection-heisenberg)
   - Affine g_k:      nabla = d - 1/(k+h^v) sum Omega_ij / (z_i - z_j) dz_i
                      = KZ connection (thm:shadow-connection-kz)
@@ -40,7 +40,7 @@
 class HeisenbergShadowConnection:
     """Shadow connection for rank-1 Heisenberg at level kappa.
 
-    nabla = d - kappa * sum_{i<j} q_i q_j dlog(z_i - z_j)
+    nabla = d - kappa * sum_{i<j} q_i q_j d(z_i - z_j)/(z_i - z_j)
 
     Flat sections: f = prod_{i<j} (z_i - z_j)^{kappa q_i q_j}
     multiplied by delta_{sum q_i, 0}.
diff --git a/compute/lib/kz_monodromy_arithmetic_engine.py b/compute/lib/kz_monodromy_arithmetic_engine.py
index ba2bd49234e56be8361cae9dd0d670c1e6313f21..5d0fbee5d8e3e9d528e87b7cd26744db0f010373
--- a/compute/lib/kz_monodromy_arithmetic_engine.py
+++ b/compute/lib/kz_monodromy_arithmetic_engine.py
@@ -975,7 +975,7 @@
     """Verify the identification: KZ connection = shadow connection at genus 0.
 
     The genus-0 arity-2 shadow connection on Conf_n(C) is:
-      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla^{sh}_{0,2} = d - (1/kappa_KZ) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     This is EXACTLY the KZ connection. The identification:
       r(z) = Res^{coll}_{0,2}(Theta_A) = Omega / z
diff --git a/compute/lib/large_n_twisted_holography.py b/compute/lib/large_n_twisted_holography.py
index 7a7f08e6cc923dc0bb22954260adfaf5478dff19..a27c9163e098d81a0383eec043c4285c5dfd6ebc
--- a/compute/lib/large_n_twisted_holography.py
+++ b/compute/lib/large_n_twisted_holography.py
@@ -163,7 +163,7 @@
     """nabla^hol_{g,n} = d - Sh_{g,n}(Theta_A).
 
     At genus 0, arity 2: specializes to KZ connection for affine algebras.
-    nabla = d - kappa sum_{i<j} dlog(z_i - z_j) for Heisenberg.
+    nabla = d - kappa sum_{i<j} d(z_i - z_j)/(z_i - z_j) for Heisenberg.
 
     Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
     projected to genus 0, plus Arnold relation on C_bar_3(X).
@@ -676,7 +676,7 @@
 def shadow_connection_genus0_arity2(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 2.
 
-    nabla^hol_{0,2} = d - kappa * dlog(z_1 - z_2).
+    nabla^hol_{0,2} = d - (kappa/(z_1 - z_2)) d(z_1 - z_2).
     For affine algebras this is the KZ connection at the scalar level.
     Flatness is automatic (scalar on configuration space of 2 points).
     """
@@ -694,7 +694,7 @@
 def shadow_connection_genus0_arity3(A: ChiralAlgebraData) -> ShadowConnection:
     """The shadow connection at genus 0, arity 3.
 
-    nabla^hol_{0,3} = d - kappa * (dlog(z_12) + dlog(z_13) + dlog(z_23)).
+    nabla^hol_{0,3} = d - kappa * (dz_12/z_12 + dz_13/z_13 + dz_23/z_23).
     At the scalar level, flatness on C_3(X) uses the Arnold relation:
     dlog(z_12) ^ dlog(z_23) + dlog(z_12) ^ dlog(z_13) + dlog(z_13) ^ dlog(z_23) = 0.
 
diff --git a/compute/lib/ordered_bar_descent_engine.py b/compute/lib/ordered_bar_descent_engine.py
index 85279446d46af8c1299844d5d9ce9e41b74039f8..342c700c0f1d78bdf8ea72ab177df06d100118c4
--- a/compute/lib/ordered_bar_descent_engine.py
+++ b/compute/lib/ordered_bar_descent_engine.py
@@ -26,7 +26,7 @@
 equivariant structure: the R-MATRIX.
 
 The R-matrix R(z) is the monodromy of the Kohno connection:
-  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d log(z_i - z_j)
+  nabla = d - sum_{i<j} r_{ij}(z_i - z_j) d(z_i - z_j)
 where r(z) is the collision residue (pole orders ONE LESS than OPE, AP19).
 
 The R-twisted Sigma_n action on generators sigma_i is:
@@ -272,7 +272,7 @@
         # where P_{12} is the permutation operator... no.
 
         # Let me be precise.
-        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} d log(z_{ij})
+        # The Kohno connection is nabla = d - sum_{i<j} hbar * r_{ij} * dz_{ij}/z_{ij}
         # where r_{ij} = Omega inserted in slots i,j.
         # The tensor Omega in g x g has components Omega_{ab}
         # and r_{12} acts on g^{x n} as Omega_{ab} in the (1,2) factor.
@@ -357,7 +357,7 @@
 
         # Hmm, but that's for modules. For the BAR COMPLEX:
         # The bar complex fibre at (z_1, z_2) is V x V = g x g.
-        # The flat connection is nabla = d - r_{12}(z) dlog(z_1 - z_2)
+        # The flat connection is nabla = d - r_{12}(z) d(z_1 - z_2)
         # where r_{12}(z) : V x V -> V x V.
         # The collision residue from J^a(z)J^b(w) ~ k g^{ab}/(z-w)^2 is:
         # r(z)_{ab,cd} acts on basis vectors e_c x e_d to give
diff --git a/compute/lib/ordered_chiral_jones_engine.py b/compute/lib/ordered_chiral_jones_engine.py
index 79715960f746348fa20dffb2e5d25298fa127914..d5709345fb00f95e231cf5072a75b65229adb48d
--- a/compute/lib/ordered_chiral_jones_engine.py
+++ b/compute/lib/ordered_chiral_jones_engine.py
@@ -22,7 +22,7 @@
 2. KZ FLAT BUNDLE on Conf_3(C):
    The ordered configuration space Conf_3(C) carries the KZ flat bundle
    L_KZ with connection (for sl_2 at level k, kappa = k + h^v = k + 2):
-     nabla_KZ = d - (1/kappa) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+     nabla_KZ = d - (1/kappa) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
    where Omega_{ij} is the Casimir insertion on the (i,j) tensor factor.
    The flat sections are the KZ conformal blocks.
    AP117: connection form is Omega dz, NOT Omega d log z.
@@ -200,13 +200,13 @@
     r"""KZ connection matrices A_{ij} for sl_2 at level k on Conf_n(C).
 
     The KZ connection is:
-      nabla_KZ = d - sum_{i<j} A_{ij} d log(z_i - z_j)
+      nabla_KZ = d - sum_{i<j} (A_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where A_{ij} = Omega_{ij} / kappa, kappa = k + h^v = k + 2 for sl_2.
 
     AP148: KZ convention r(z) = Omega/((k+h^v)*z).
-    AP117: connection 1-form uses d log(z_i - z_j), which is the
-           Arnold form (bar-construction coefficient).
+    AP117: connection 1-form is (A_{ij}/(z_i - z_j)) d(z_i - z_j);
+           d log(z_i - z_j) is the Arnold bar coefficient.
 
     Returns list of (A_{ij}, (i,j)) pairs for all 0 <= i < j < n_points.
     The representation space is V^{tensor n_points} with V = C^2.
diff --git a/compute/lib/primitive_kernel_full.py b/compute/lib/primitive_kernel_full.py
index f34378e79ed4b97d6da42aeef94b742668543035..957e215444e07bf21c08b69b295ba426441d066a
--- a/compute/lib/primitive_kernel_full.py
+++ b/compute/lib/primitive_kernel_full.py
@@ -871,14 +871,14 @@
     """KZ connection data for affine sl_N at level k.
 
     The KZ connection at genus 0 with n marked points is:
-        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
+        nabla_KZ = d - (1/kappa) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) * d(z_i - z_j)
 
     where:
         kappa_KZ = k + h^v  (the shifted level for KZ)
         Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)
 
     For 2 points:
-        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
+        nabla_KZ = d - (1/(k+N)) * (Omega_{12}/(z_1 - z_2)) * d(z_1 - z_2)
 
     The KZ connection arises as the linearization of the primitive MC element:
         K_A -> FT(K_A) = Theta_A -> linearize -> nabla^mod_A
diff --git a/compute/lib/shadow_mzv_engine.py b/compute/lib/shadow_mzv_engine.py
index c1d23a6352499fc65e6831fb547c6c51664fda13..88175422dfd107334fe2d190ec0e9fd1e3299f1c
--- a/compute/lib/shadow_mzv_engine.py
+++ b/compute/lib/shadow_mzv_engine.py
@@ -920,7 +920,7 @@
     # The associator involves 1/kappa_KZ as the coupling.
     # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
     #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
-    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
+    # The KZ equation: dPhi = (1/kappa) * sum (Omega_{ij}/(z_i - z_j)) d(z_i - z_j) * Phi
     # So the associator expansion parameter is 1/kappa.
 
     shadow_mzv = {}
diff --git a/compute/lib/theorem_dk0_evaluation_bridge_engine.py b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
index 722398202a615e3d51a001878a6cc85f7454e15b..6012c5a81bff2b0d81db5dea03c9a934e32e7d34
--- a/compute/lib/theorem_dk0_evaluation_bridge_engine.py
+++ b/compute/lib/theorem_dk0_evaluation_bridge_engine.py
@@ -135,7 +135,7 @@
 class KZData:
     """Data for the KZ connection associated to V_k(g).
 
-    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
+    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     For two-point (z = z_1 - z_2):
         dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
diff --git a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
index 2107fb24ff5ff6c6cb22881666b0d6100126fae0..0e4a7427d428e409fb7189b2f464e7f423ff0211
--- a/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
+++ b/compute/lib/theorem_swiss_cheese_kontsevich_engine.py
@@ -465,7 +465,7 @@
         dz = z1 - z2
 
         # Monodromy phase from KZ connection
-        # The connection form is omega = kappa * d log(z_1 - z_2)
+        # The connection form is omega = (kappa/(z_1 - z_2)) d(z_1 - z_2)
         # Monodromy around a loop exchanging z_1, z_2 gives exp(pi*i*kappa)
         monodromy_phase = cmath.exp(1j * math.pi * kappa)
 
@@ -474,7 +474,7 @@
             'n_points': n,
             'monodromy_phase': monodromy_phase,
             'kappa': kappa,
-            'connection_form': f'kappa * d log(z1 - z2)',
+            'connection_form': f'kappa * d(z1 - z2)/(z1 - z2)',
             'r_matrix_consistent': True,
         }
 
diff --git a/compute/lib/theorem_three_way_r_matrix_engine.py b/compute/lib/theorem_three_way_r_matrix_engine.py
index 5704286ad02408997403956ea7e6ea8199a8d6ff..c782f2322b123b4ab7f6a6a4ddaeea58613249ab
--- a/compute/lib/theorem_three_way_r_matrix_engine.py
+++ b/compute/lib/theorem_three_way_r_matrix_engine.py
@@ -391,7 +391,7 @@
         Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
         where Omega = sum_a t^a tensor t^a is the Casimir tensor.
         The normalization 1/(k + h^v) comes from the KZ equation, which
-        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
+        is nabla = d - (1/(k+h^v)) sum_{j != i} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j).
 
         The collision residue of Theta_A extracts the NORMALIZED r-matrix,
         which includes the 1/(k + h^v) factor from the bar normalization.
diff --git a/compute/lib/twisted_gauge_defects_engine.py b/compute/lib/twisted_gauge_defects_engine.py
index f974c63d8d6562dec588ab4776e8fcee50b1ed38..c7645073e0e54143cc4ae1dcb32355f4462a3d5a
--- a/compute/lib/twisted_gauge_defects_engine.py
+++ b/compute/lib/twisted_gauge_defects_engine.py
@@ -1280,7 +1280,7 @@
     r"""KZ connection data for the defect system.
 
     The KZ connection on Conf_n(C) x V_1^{x n} is:
-      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} Omega_{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k + h^v)) sum_{i<j} (Omega_{ij}/(z_i - z_j)) d(z_i - z_j)
 
     where Omega_{ij} = sum_a T_a^(i) T_a^(j) is the Casimir acting on
     the i-th and j-th tensor factors.
diff --git a/compute/lib/twisted_holography_engine.py b/compute/lib/twisted_holography_engine.py
index 56379cfa405955337700157ed9a80dbd698e7a30..7ace9c7c84100f46fe7c1002fdfb8ea098431806
--- a/compute/lib/twisted_holography_engine.py
+++ b/compute/lib/twisted_holography_engine.py
@@ -901,7 +901,7 @@
 
     Singularity classification:
     - Heisenberg (depth 2): flat, no singularity.
-      nabla is just d - kappa * sum dlog(z_i - z_j).
+      nabla is just d - kappa * sum d(z_i - z_j)/(z_i - z_j).
     - Affine (depth 3): logarithmic singularities.
       nabla specializes to KZ connection at (0,2).
       Singularities at coinciding points z_i = z_j.
diff --git a/compute/lib/twisted_holography_mc.py b/compute/lib/twisted_holography_mc.py
index b99d6004c94b3d3a449b4100eec6331acb1aa3dd..9fcb9dc2f657c79b591f3fbe0321d57c04b6f319
--- a/compute/lib/twisted_holography_mc.py
+++ b/compute/lib/twisted_holography_mc.py
@@ -55,7 +55,7 @@
   This satisfies the quantum YBE:
     R_{12}(u) R_{13}(u+v) R_{23}(v) = R_{23}(v) R_{13}(u+v) R_{12}(u)
 
-  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij} d log(z_ij)
+  The monodromy of the KZ connection nabla_{0,n} = d - sum r^{ij}(z_ij) dz_ij
   gives the quantum group R-matrix of U_q(sl_2) where q = exp(pi*i/(k+2)).
   This is the Drinfeld-Kohno theorem, which in our framework is the statement
   that the genus-0 shadow connection monodromy = R-matrix.
@@ -715,7 +715,7 @@
       = (z - hbar*P) / z  (Yang R-matrix, exact to leading order)
 
     The Drinfeld-Kohno theorem: monodromy of the KZ connection
-      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{0,n} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
     gives the quantum group R-matrix of U_q(g) where q = exp(pi*i/(k+h^v)).
     """
     r = extract_collision_residue(A)
@@ -784,10 +784,10 @@
 def shadow_connection_genus0(A: ChiralAlgebraData, n: int) -> Dict[str, Any]:
     """Shadow connection nabla^{hol}_{0,n} at genus 0.
 
-    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d log(z_i - z_j)
+    nabla_{0,n} = d - sum_{i<j} r^{ij}(z_i - z_j) d(z_i - z_j)
 
     For affine sl_N at level k, this is the KZ connection:
-      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} Omega^{ij} d log(z_i - z_j)
+      nabla_{KZ} = d - (1/(k+h^v)) sum_{i<j} (Omega^{ij}/(z_i - z_j)) d(z_i - z_j)
 
     Flatness: (nabla_{0,n})^2 = 0
     This follows from the MC equation for Theta_A (thm:thqg-flatness).
@@ -816,8 +816,8 @@
     """Verify the KZ connection matches the genus-0 shadow connection.
 
     For affine sl_N at level k:
-      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij} d log(z_{ij})
-      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} Omega^{ij} d log(z_{ij})
+      nabla_{0,n}^{shadow} = d - sum_{i<j} r^{ij}(z_{ij}) dz_{ij}
+      nabla_{KZ} = d - (1/(k+N)) sum_{i<j} (Omega^{ij}/z_{ij}) dz_{ij}
 
     These match because:
       r^{coll}(z) = Omega/z  and the normalization factor 1/(k+h^v)
diff --git a/compute/tests/test_holographic_shadow_connection.py b/compute/tests/test_holographic_shadow_connection.py
index 62224a46502332f8e7b31aedb7cb0590b8519b08..20cbaedc20861ec6483fc9afaa5c1dc52f99a50f
--- a/compute/tests/test_holographic_shadow_connection.py
+++ b/compute/tests/test_holographic_shadow_connection.py
@@ -52,7 +52,7 @@
 # ========================================================================
 
 class TestHeisenbergFlatness:
-    """nabla = d - kappa sum q_i q_j dlog(z_i - z_j) is flat."""
+    """nabla = d - kappa sum q_i q_j d(z_i - z_j)/(z_i - z_j) is flat."""
 
     def test_flatness_n3_unit_charges(self):
         """Flatness for n=3 with charges (1,1,1)."""
diff --git a/compute/tests/test_twisted_holography_mc.py b/compute/tests/test_twisted_holography_mc.py
index d7b2acee34519ff7d56d028408064d4ef9acbd6f..0381f8a9ad0a4813b1697aba8f2ef8687029357a
--- a/compute/tests/test_twisted_holography_mc.py
+++ b/compute/tests/test_twisted_holography_mc.py
@@ -278,7 +278,7 @@
 # =========================================================================
 
 class TestShadowConnection:
-    """Test nabla^{hol}_{0,n} = d - sum r^{ij} d log(z_{ij})."""
+    """Test nabla^{hol}_{0,n} = d - sum r^{ij}(z_{ij}) dz_{ij}."""
 
     def test_shadow_connection_flat(self):
         """Flatness from MC equation (thm:thqg-flatness)."""
diff --git a/standalone/survey_modular_koszul_duality.tex b/standalone/survey_modular_koszul_duality.tex
index 6882a9577b88b4c8516a8872e9c24a924ad51f7b..466d87ad788c1a1c3d3d73d56f307fbd1cc1d5bf
--- a/standalone/survey_modular_koszul_duality.tex
+++ b/standalone/survey_modular_koszul_duality.tex
@@ -4737,7 +4737,7 @@
 \nabla_{\mathrm{KZ}}
 \;=\;
 d\;-\;\hbar\sum_{i<j}
-\Omega_{ij}\,d\log(z_i-z_j).
+\frac{\Omega_{ij}}{z_i-z_j}\,d(z_i-z_j).
 \]
 Its monodromy representation
 $\pi_1(\operatorname{Conf}_n(\mathbb C))\to
@@ -7232,12 +7232,12 @@
 \[
 \operatorname{Sh}_{0,n}(\Theta_{\widehat{\fg}_k})
 \;=\;
-\sum_{i<j}r_{ij}(z_i{-}z_j)\,d\log(z_i{-}z_j)
+\sum_{i<j}r_{ij}(z_i{-}z_j)\,dz_{ij}
 \;=\;
 \frac{1}{h^\vee+k}\sum_{i<j}\frac{\Omega_{ij}\,dz_{ij}}{z_{ij}}\,,
 \]
-where $r_{ij}$ denotes the propagator-weighted Casimir
-$\Omega_{ij}/(h^\vee{+}k)$, not the spectral $r$-matrix.
+where $r_{ij}(z)=\Omega_{ij}/((h^\vee{+}k)z)$ denotes the
+connection coefficient, not the Arnold form.
 Flatness of $\nabla_{\mathrm{KZ}}=d-\operatorname{Sh}_{0,n}$
 is the MC equation at genus~$0$ and degree~$n$. For
 $\cA=\operatorname{Vir}_c$, on the Virasoro degenerate-module
@@ -7539,7 +7539,7 @@
 $\mathfrak z(\widehat{\mathfrak g}_{-h^\vee})$ is the
 Feigin--Frenkel algebra of $\mathfrak{sl}_2$-opers.
 The monodromy of the KZ connection
-$\nabla_{\mathrm{KZ}} = d - \hbar\,\Omega/z$
+$\nabla_{\mathrm{KZ}} = d - (\hbar\,\Omega/z)\,dz$
 (with $\hbar = 1/(k{+}2)$)
 is compared with the quantum-group $R$-matrix of
 $U_q(\mathfrak{sl}_2)$ by the affine Drinfeld--Kohno package;

tokens used
453,543
