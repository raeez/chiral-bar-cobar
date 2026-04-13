# E04_test_gaps_rmatrix (768s)

**Findings**
- PROBLEM at [compute/lib/yangian_rmatrix_sl3.py](/Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_sl3.py:334): the raw affine `sl_3` residue surface claimed `r(z)=k*Omega/z`, but `r_matrix_fund` actually returned level-free `Omega/z`, and the AP19 prose inverted which OPE term survives. EXACT edit applied: `r_matrix_abstract` and `r_matrix_fund` now take an optional `k` and return/store the trace-form residue `k*Omega/z`; the AP19 explanation now says the double pole contributes and the bracket term drops; the `R_residue_at_zero` doc was narrowed to the normalized Yang `R` only. Regression checks were added at [compute/tests/test_yangian_rmatrix_sl3.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_sl3.py:249) for `k=0` vanishing and linear-in-`k` scaling.

- PROBLEM at [compute/lib/theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sl3_yangian_r_matrix_engine.py:341): the theorem-level `sl_3` engine had the same raw-residue drift, implementing `Omega/z` while presenting an affine level-`k` surface. EXACT edit applied: `r_matrix_fund` and `r_matrix_adj` now accept `k` and return `k*Omega/z`; the top-level mathematical description and the DNP comparison surface were updated to use matched level normalization. Regression checks were added at [compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:285).

- PROBLEM at [compute/lib/theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sl3_yangian_r_matrix_engine.py:504): the KZ Hamiltonian was divided by `kappa` instead of the canonical KZ denominator `k+h^vee`; commutativity still held, so the bug was masked by scale-invariant tests. EXACT edit applied: the parameter was renamed to `level_shift`, the formula/docstring now use `1/(k+h^vee)`, and `full_report` now passes `k + H_VEE` instead of `kappa`. A direct normalization test was added at [compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:419).

- PROBLEM at [compute/lib/yangian_rmatrix_arithmetic_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_arithmetic_engine.py:805): the YBE parameter sweep hit exact type `B/C` rational poles, causing runtime warnings, and the type `C` `_full_rmatrix` docstring advertised the wrong denominator sign. EXACT edit applied: added `_full_rmatrix_hits_pole()` and filtered the numerical YBE test points before evaluation; corrected the type `C` docstring from `u + kappa_R` to `u - kappa_R`. A no-warning regression was added at [compute/tests/test_yangian_rmatrix_arithmetic_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_arithmetic_engine.py:956).

Verification: `pytest -q compute/tests/test_yangian_rmatrix_sl3.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py` and the wider r-matrix suite both passed; final wide sweep: `1123 passed`.


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
session id: 019d87a8-b75a-78d2-b3bb-6bc15dc88fbe
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


Same for r_matrix engines.
mcp startup: no servers
codex
Scope is the `r_matrix` compute-engine surface: I’m loading the required repo invariants, then I’ll locate the engine files/tests, audit them adversarially, and patch only that assigned surface.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/compute-engine-scaffold/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
 succeeded in 50ms:
---
name: compute-engine-scaffold
description: Use when the task is to add or repair a compute engine together with tests and independent oracle checks. This is the Codex-native equivalent of `/compute-engine` from `CLAUDE.md`.
---

# Compute Engine Scaffold

Use this when a mathematical claim must land in the compute layer, not only in prose.

## Workflow

1. State the engine target precisely:
   formula,
   invariant,
   family,
   parameters,
   conventions.
2. Identify the canonical module.
   Implement the formula once there and import it elsewhere.
3. Build tests from independent sources, not from the engine output itself.
 succeeded in 50ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

 succeeded in 50ms:
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
**Locating engine files**

I need to announce that I'm using my skills here. I should locate the r_matrix engine files, and it looks like I might use the explorer for that, following my instructions. I'm considering spawning the explorer to find the canonical engine files, maybe while also using shell rg in parallel. It’s important that I read the exact files once I've identified them before making any edits. Let’s get started on the search!
codex
Using `compute-engine-scaffold` for the engine/test repair workflow and `multi-path-verify` for the formula audit. Next I’m locating the canonical `r_matrix` modules and their tests so the scope is explicit before any edit.
collab spawn_agent(call_pGi5gSdont96Pcsl2zgilacF, prompt="Find the canonical r_matrix compute-engine files and directly associated tests in /Users/raeez/chiral-bar-cobar. Report …")
mcp startup: no servers
spawn_agent(call_pGi5gSdont96Pcsl2zgilacF, prompt="Find the canonical r_matrix compute-engine files and directly associated tests in /Users/raeez/chiral-bar-cobar. Report …") pending init:
  agent: 019d87a9-20c6-7281-aab8-4c65271ae24a
exec
/bin/zsh -lc 'rg --files --hidden | rg "r_matrix|rmatrix|RMatrix|r-matrix|matrix"' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
wave2_audit_20260413_001942/J04_engine_r_matrix.md
wave2_audit_20260413_001942/D05_rmatrix_level.md
wave2_audit_20260413_001942/B08_rmatrix_bridge.md
virasoro_r_matrix.pdf
audit_campaign_20260412_230832/XV02_rmatrix_xvol.md
audit_campaign_20260412_230832/CE04_rmatrix.md
audit_campaign_20260412_231034/CE04_rmatrix.md
resume_20260413_165929/D05_rmatrix_level.md
audit_campaign_20260412_231034/XV02_rmatrix_xvol.md
standalone/virasoro_r_matrix.tex
standalone/cover_letter_virasoro_r_matrix.pdf
standalone/cover_letter_virasoro_r_matrix.tex
standalone/virasoro_r_matrix.pdf
relaunch_wave2_empties/D05_rmatrix_level.md
relaunch_20260413_111534/D05_rmatrix_level.md
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
compute/tests/test_matrix_rankin_selberg.py
compute/tests/test_matrix_model_cross_channel.py
compute/tests/test_cohft_givental_rmatrix.py
compute/tests/test_yangian_rmatrix_arithmetic_engine.py
exec
/bin/zsh -lc "rg -n --hidden --glob '"'!*.pdf'"' \"r_matrix|r-matrix|RMatrix|rmatrix|classical r\" ." in /Users/raeez/chiral-bar-cobar succeeded in 217ms:
Total output lines: 7257

./FRONTIER.md:192:7. virasoro_r_matrix.pdf (AP36: biconditional overclaim in Prop 5.1)
./FRONTIER.md:583:**Three-level contrast:** Generic (Koszul, infinite monodromy, center = C) vs Integrable (Koszul, finite monodromy, center = C^{k+1}) vs Critical (NOT Koszul, trivial monodromy, center = C[S_2] infinite). The entire r-matrix lives in ker(av) at critical level.
./FRONTIER.md:603:**rem:stokes-count-wN** in standalone. Stokes rays = 4N-4 for the W_N KZ connection at degree 2. The W_N-W_N OPE has pole order 2N; d-log absorption gives r-matrix pole 2N-1; Poincaré rank 2N-2; Stokes rays 2(2N-2) = 4N-4.
./FRONTIER.md:620:2. **Belavin r-matrix:** Pauli decomposition, NOT Weierstrass zeta (breaks CYBE). Two-step degeneration: elliptic → trigonometric → rational.
./FRONTIER.md:621:3. **Cross-volume r-matrix:** 3 discrepancies fixed (genus1_seven_faces, holographic_datum_master, log_ht_monodromy_core)
./FRONTIER.md:632:- belavin_rmatrix_verification (36): Pauli decomposition, CYBE, degeneration
./healing_20260413_132214/H20_remove_associator_dep.md:601:  5109	(equation~\eqref{eq:ek-vertex-rmatrix}) is likewise
./platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:314:\label{rem:rmatrix-baxter-connection}
./platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:337:\label{rem:rmatrix-baxter-connection}
./platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:635:- **Baxter/completion dependencies and bib keys nearby:** the Baxter constraint ties to `eq:baxter-ses-yangian` (the SES whose naturality was checked in `cor:baxter-naturality-opoly`), `prop:baxter-yangian-equivariance`, and `comp:sl2-rmatrix-ext` (Remark~\ref{rem:rmatrix-baxter-connection}); the type‑A Baxter package used in Step 2 is packaged in `rem:baxter-exact-triangles-typeA`; the prefundamental Clebsch–Gordan input is `prop:prefundamental-clebsch-gordan`; completion/compactification is flagged as conditional in `conj:dk-compacts-completion` (the remaining “compact/completion packet”); bibliographically the negative prefundamentals come from `\cite{HJZ25}`.
./platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:1221:I'm thinking about making some simple replacements, like changing "Conjecture" to "Theorem" in the text. I also need to look into `rem:rmatrix-baxter-connection` since it's close to the target and should be properly synced. This patch seems like it could be significant, so I want to be careful. I need to ensure that the apply_patch grammar is correct, so I'm crafting everything with the exact contexts in mind.
./platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:1299:  3018	\label{rem:rmatrix-baxter-connection}
./platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:1305:  3024	(Computation~\ref{comp:sl2-rmatrix-ext}, Step~3). Setting
./audit/vol2_chapters_unresolved_refs_report.md:134:- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:2339 — PROBLEM: `ref{thm:r-matrix-mixed-projection}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: thm:r-matrix-mixed-projection` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:2174`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{thm:r-matrix-mixed-projection}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:2174` and keep this reference unchanged.
./audit/vol2_chapters_unresolved_refs_report.md:151:- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1031 — PROBLEM: `eqref{eq:virasoro-r-matrix-explicit}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:virasoro-r-matrix-explicit` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:987`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:virasoro-r-matrix-explicit}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:987` and keep this reference unchanged.
./audit/vol2_chapters_unresolved_refs_report.md:155:- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1711 — PROBLEM: `eqref{eq:w3-r-matrix}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: eq:w3-r-matrix` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1684`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{eq:w3-r-matrix}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:1684` and keep this reference unchanged.
./audit/vol2_chapters_unresolved_refs_report.md:186:- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1088 — PROBLEM: `ref{sec:classical-r-matrix-explicit}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: sec:classical-r-matrix-explicit` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:10`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{sec:classical-r-matrix-explicit}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:10` and keep this reference unchanged.
./audit/vol2_chapters_unresolved_refs_report.md:189:- [CRITICAL] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1250 — PROBLEM: `ref{thm:virasoro-r-matrix}` has no live target in `~/chiral-bar-cobar-vol2/chapters/`; the same file still contains `% label removed: thm:virasoro-r-matrix` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:566`, so the anchor was deleted and the prose was not updated. FIX: restore `\label{thm:virasoro-r-matrix}` at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:566` and keep this reference unchanged.
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar

thinking
**Determining file scope**

I need to narrow down the assigned files based on the user’s mention of "r_matrix engines," which seems related to prior work on kappa engines. It’s possible the user is expecting an audit and fix for compute engines tied to r_matrix. I should be thorough and consider all r_matrix engine files, including canonical engine modules and tests. I need to identify those modules with potential issues and review the exact files we might be working with.
exec
/bin/zsh -lc 'rg -n "r_matrix"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 3601

healing_20260413_132214/H29_compute_test_heal.md:88:4. r_matrix engines: verify k=0 vanishing
resume_20260413_163457/S14_standalone_to_main.md:11:- [MEDIUM] [N1_koszul_meta.tex](/Users/raeez/chiral-bar-cobar/standalone/N1_koszul_meta.tex:34) — PROBLEM: unconditional `\newcommand`/` \DeclareMathOperator` preamble blocks remain widespread across the standalone surface: [N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:35), [N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:34), [N4_mc4_completion.tex](/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:33), [N5_mc5_sewing.tex](/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:33), [N6_shadow_formality.tex](/Users/raeez/chiral-bar-cobar/standalone/N6_shadow_formality.tex:33), [bp_self_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/bp_self_duality.tex:36), [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:37), [classification_trichotomy.tex](/Users/raeez/chiral-bar-cobar/standalone/classification_trichotomy.tex:33), [gaudin_from_collision.tex](/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:36), [garland_lepowsky.tex](/Users/raeez/chiral-bar-cobar/standalone/garland_lepowsky.tex:36), [genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/genus1_seven_faces.tex:33), [ordered_chiral_homology.tex](/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex:39), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:37), [programme_summary_section1.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_section1.tex:36), [seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/seven_faces.tex:32), [shadow_towers.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers.tex:32), [shadow_towers_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v2.tex:35), [three_parameter_hbar.tex](/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:34), [virasoro_r_matrix.tex](/Users/raeez/chiral-bar-cobar/standalone/virasoro_r_matrix.tex:33), and [w3_holographic_datum.tex](/Users/raeez/chiral-bar-cobar/standalone/w3_holographic_datum.tex:32). This violates the import-safe seam contract. FIX: change every custom symbol macro from `\newcommand` to `\providecommand`; replace shared-macro mutations like `\renewcommand{\Bbbk}`/`\renewcommand{\SS}` with local names; guard operator declarations with `\@ifundefined{...}{\DeclareMathOperator...}{}` or rewrite them as `\providecommand{\Res}{\operatorname{Res}}`.
resume_20260413_163457/S14_standalone_to_main.md:1357:- [MEDIUM] [N1_koszul_meta.tex](/Users/raeez/chiral-bar-cobar/standalone/N1_koszul_meta.tex:34) — PROBLEM: unconditional `\newcommand`/` \DeclareMathOperator` preamble blocks remain widespread across the standalone surface: [N2_mc3_all_types.tex](/Users/raeez/chiral-bar-cobar/standalone/N2_mc3_all_types.tex:35), [N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:34), [N4_mc4_completion.tex](/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:33), [N5_mc5_sewing.tex](/Users/raeez/chiral-bar-cobar/standalone/N5_mc5_sewing.tex:33), [N6_shadow_formality.tex](/Users/raeez/chiral-bar-cobar/standalone/N6_shadow_formality.tex:33), [bp_self_duality.tex](/Users/raeez/chiral-bar-cobar/standalone/bp_self_duality.tex:36), [chiral_chern_weil.tex](/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:37), [classification_trichotomy.tex](/Users/raeez/chiral-bar-cobar/standalone/classification_trichotomy.tex:33), [gaudin_from_collision.tex](/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:36), [garland_lepowsky.tex](/Users/raeez/chiral-bar-cobar/standalone/garland_lepowsky.tex:36), [genus1_seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/genus1_seven_faces.tex:33), [ordered_chiral_homology.tex](/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex:39), [programme_summary.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary.tex:37), [programme_summary_section1.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_section1.tex:36), [seven_faces.tex](/Users/raeez/chiral-bar-cobar/standalone/seven_faces.tex:32), [shadow_towers.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers.tex:32), [shadow_towers_v2.tex](/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v2.tex:35), [three_parameter_hbar.tex](/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:34), [virasoro_r_matrix.tex](/Users/raeez/chiral-bar-cobar/standalone/virasoro_r_matrix.tex:33), and [w3_holographic_datum.tex](/Users/raeez/chiral-bar-cobar/standalone/w3_holographic_datum.tex:32). This violates the import-safe seam contract. FIX: change every custom symbol macro from `\newcommand` to `\providecommand`; replace shared-macro mutations like `\renewcommand{\Bbbk}`/`\renewcommand{\SS}` with local names; guard operator declarations with `\@ifundefined{...}{\DeclareMathOperator...}{}` or rewrite them as `\providecommand{\Res}{\operatorname{Res}}`.
resume_20260413_163457/CE01_shadow_engines.md:562:    ahat_r_matrix_coefficients,
resume_20260413_163457/CE01_shadow_engines.md:584:    19	    ahat_r_matrix_coefficients,
resume_20260413_163457/CE01_shadow_engines.md:723:    19	    ahat_r_matrix_coefficients,
resume_20260413_163457/CE01_shadow_engines.md:1093:   142	    def test_ap141_r_matrix_k0(self):
elite_rescue_20260413_141402/X10_compute_manuscript_sync.md:63:Focus on: shadow_tower, koszul_conductor, bar_cohomology_sl2, r_matrix_km,
standalone/compute_chi_R.py:243:def r_matrix_eigenvalue(J, u, hbar=mpf(1)/4):
standalone/compute_chi_R.py:299:        lam = r_matrix_eigenvalue(J, u, hbar)
standalone/compute_chi_R.py:429:        l0 = r_matrix_eigenvalue(0, u_val, hbar)
standalone/compute_chi_R.py:430:        l1 = r_matrix_eigenvalue(1, u_val, hbar)
standalone/compute_chi_R.py:466:        l0 = r_matrix_eigenvalue(0, u_val, hbar)
standalone/compute_chi_R.py:467:        l1 = r_matrix_eigenvalue(1, u_val, hbar)
standalone/compute_chi_R.py:488:        l0 = r_matrix_eigenvalue(0, u_val, hbar)
standalone/compute_chi_R.py:620:        l0 = r_matrix_eigenvalue(0, u_val, hbar)
standalone/compute_chi_R.py:730:        lam_rat = r_matrix_eigenvalue(0, u_val, hbar)
healing_20260413_130533/H11_SC_formal_alt.md:591:wave2_audit_20260413_001942/S10_examples_to_wn.md:252:standalone/virasoro_r_matrix.tex:66:shadow coefficient $S_3(\Vir_c) = 2$ is independent of the central
exec
/bin/zsh -lc 'ls compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1347

__init__.py
__pycache__
_archive
a2_polynomial_combinatorics_engine.py
abjm_holographic_datum.py
admissible_deep_bar_engine.py
admissible_koszul_rank2_engine.py
admissible_level_bar_engine.py
admissible_sl3_d1_poisson_engine.py
admissible_sl3_d1_rank_engine.py
affine_km_sewing_engine.py
affine_sl2_shadow_tower.py
affine_sl3_shadow.py
agt_nekrasov_arithmetic_engine.py
agt_nekrasov_shadow_engine.py
agt_shadow_correspondence.py
agt_su3_nekrasov_engine.py
ainfty_structure_maps_engine.py
codex
The candidate surface is broad in `compute/lib` and `compute/tests`. I’m narrowing to the canonical r-matrix engines first, then I’ll audit line-by-line against the level-prefix and pole-order invariants before touching anything.
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_pva_classical_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_theorem_pva_classical_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/quantum_rmatrix_barcomplex.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""r-matrix landscape: explicit collision residues for 8 standard families.

The r-matrix r(z) = Res^{coll}_{0,2}(\Theta_A) is the binary collision
residue of the universal MC element.  By AP19 (the bar kernel absorbs
a pole), the bar construction extracts residues along d\log(z_i - z_j),
which absorbs one power of (z-w) from each OPE pole:

    OPE pole z^{-n}  --->  r-matrix pole z^{-(n-1)}

In particular, z^{-1} in the OPE becomes z^0 = regular and DROPS.

Families computed
-----------------
1. Heisenberg at level k:       r(z) = k/z
2. Affine sl_2 at level k:      r(z) = k * Omega_{sl_2} / z
3. Affine sl_3 at level k:      r(z) = k * Omega_{sl_3} / z
4. Virasoro at central charge c: r(z) = (c/2)/z^3 + 2T/z
5. W_3 (TT channel):            same as Virasoro
6. W_3 (WW channel):            r(z) = (c/3)/z^5 + 2T/z^3 + dT/z^2 + ...
7. betagamma:                    r(z) = 0 (entirely regular)
 succeeded in 52ms:
r"""PVA classical r-matrix extraction and KZ25 deformation-quantization bridge.

For a Poisson vertex algebra (PVA) with lambda-bracket
  {a_\lambda b} = \sum_{n \ge 0} \lambda^{(n)} c_n(a,b),
the classical r-matrix is the genus-0 binary seed of the shadow
obstruction tower:
  r^{cl}(z) = Res^{coll}_{0,2}(\Theta_A)|_{\hbar=0}.

KEY CONVENTION (AP44): \lambda^{(n)} = \lambda^n / n! is the divided
power.  The lambda-bracket coefficient at order n in \lambda is
a_{(n)}b / n!, NOT a_{(n)}b.  Equivalently:
    {a_\lambda b} = \sum_n (\lambda^n / n!) \, a_{(n)} b

The classical r-matrix is extracted from the lambda-bracket modes by:
    r^{cl}_{IJ}(z) = \sum_{n \ge 0} c_n(e_I, e_J) / z^{n+1}

where c_n = a_{(n)}b / n! is the divided-power lambda-bracket coefficient.
The full OPE mode a_{(n)}b differs from the lambda-bracket coefficient
by a factor n!:
    \text{OPE mode} = n! \times \text{lambda-bracket coefficient at } \lambda^n
 succeeded in 52ms:
r"""Tests for rmatrix_landscape.py: explicit r-matrices for 8 standard families.

AP19 verification (the bar kernel absorbs a pole):
  OPE pole z^{-n}  --->  r-matrix pole z^{-(n-1)}
  z^{-1} in OPE  --->  z^0 = regular, DROPS

Three verification axes:
  (A) AP19 pole orders for all 8 families
  (B) CYBE / infinitesimal braid relations for affine families
  (C) Skew-symmetry r_{12}(z) + r_{21}(-z) = 0 for Casimir-based families

Ground truth:
  - eq:virasoro-r-collision: r^Vir(z) = (c/2)/z^3 + 2T/z
  - prop:affine-r-mode: r^aff(z) = k*Omega/z
  - AP19 in CLAUDE.md
  - collision_residue_identification.py
  - test_rmatrix_poles_comprehensive.py
"""

from __future__ import annotations
 succeeded in 51ms:
r"""Tests for PVA classical r-matrix extraction and KZ25 bridge.

THEOREM (KZ25 classical-quantum bridge):
The classical r-matrix extracted from the PVA lambda-bracket is the
genus-0 binary seed of the shadow obstruction tower:
    r^{cl}(z) = Res^{coll}_{0,2}(\Theta_A)|_{\hbar=0}

VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):

    Path 1 (PVA extraction):    lambda-bracket -> OPE modes -> r-matrix poles
    Path 2 (AP19 cross-check):  OPE poles -> d-log shift -> collision poles
    Path 3 (rmatrix_landscape): compare with existing collision-residue engine
    Path 4 (CYBE):              classical Yang-Baxter from Jacobi identity
    Path 5 (kappa consistency): scalar trace of r-matrix matches kappa(A)

All formulas computed from first principles (AP1, AP3).
AP44 divided-power convention verified at every step.
Cross-family consistency verified (AP10).

References:
exec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_quantum_rmatrix_barcomplex.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Quantum group R-matrices from the bar complex: explicit computation for
all classical types.

The bar complex collision residue r(z) = Res^{coll}_{0,2}(\Theta_A) gives
the classical r-matrix.  Its quantization via the hbar-expansion of the
shadow obstruction tower produces the quantum R-matrix.

MATHEMATICAL FRAMEWORK
======================

1. CLASSICAL r-MATRIX (from bar complex collision residue)

   For affine g_k, the OPE has poles at z^{-2} (curvature) and z^{-1}
   (bracket).  The bar propagator d\log E(z,w) absorbs one power (AP19):

       r(z) = Omega / z     where Omega = sum_a T^a tensor T_a

   is the quadratic Casimir in g tensor g.

   In the fundamental representation of sl_N:
 succeeded in 52ms:
 M CLAUDE.md
 M Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
 M Makefile
 M N1_koszul_meta.pdf
 M N2_mc3_all_types.pdf
 M N3_e1_primacy.pdf
 M N4_mc4_completion.pdf
 M N5_mc5_sewing.pdf
 M N6_shadow_formality.pdf
 M README.md
 M appendices/_sl2_yangian_insert.tex
 M appendices/ordered_associative_chiral_kd.tex
 M bibliography/references.tex
 M bp_self_duality.pdf
 M chapters/connections/bv_brst.tex
 D chapters/connections/casimir_divisor_core_transport.tex
 M chapters/connections/concordance.tex
 D chapters/connections/dg_shifted_factorization_bridge.tex
 M chapters/connections/editorial_constitution.tex
 M chapters/connections/frontier_modular_holography_platonic.tex
 succeeded in 52ms:
r"""Tests for quantum R-matrices from the bar complex.

Comprehensive test suite for compute/lib/quantum_rmatrix_barcomplex.py.
Each test verifies ONE mathematical property.

Organization:
  1. q-number arithmetic (3 tests)
  2. Permutation and embedding (4 tests)
  3. Classical r-matrix / Casimir for all types (12 tests)
  4. CYBE (infinitesimal braid relations) (8 tests)
  5. Quantum R for U_q(sl_2) fundamental (6 tests)
  6. Quantum R for U_q(sl_3) fundamental (4 tests)
  7. Drinfeld-Kohno theorem (4 tests)
  8. Colored R-matrices (6 tests)
  9. Quasi-triangular structure (4 tests)
  10. Ribbon element / twist (4 tests)
  11. Yangian R-matrices (6 tests)
  12. Classical limit and hbar expansion (4 tests)
  13. Cross-checks with existing modules (4 tests)

exec
/bin/zsh -lc 'rg -n "rmatrix_landscape" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/CE04_rmatrix.md:5:- [MEDIUM] [compute/tests/test_theorem_three_way_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_three_way_r_matrix_engine.py:134) — This selected `r_matrix` test file hardcodes the affine `sl_2` residue as `\Omega/((k+2)z)` and expects `1/(k+2)` at [line 175](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_three_way_r_matrix_engine.py:175). Inference: the keyword slice therefore mixes KZ normalization here with the trace-form AP126 surface in `test_rmatrix_landscape.py`, so the user’s requested `k=0→0` check is not uniform across the selected tests. This file also has zero `# VERIFIED` tags.
audit_campaign_20260412_231034/CE04_rmatrix.md:6:- [MEDIUM] [compute/tests/test_rmatrix_landscape.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1013) — This file does enforce the trace-form AP126 boundary check: `r^{aff sl_2}(z)=k\Omega/z` and `k=0→0` are tested directly at [lines 1030](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1030) and [1050](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1050). But the same block hardcodes zero-level kappa expectations `0`, `3/2`, and `4` at [lines 1103](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1103)-[1105](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1105) with no `# VERIFIED` provenance, and grep found no `# VERIFIED` markers anywhere in the file.
audit_campaign_20260412_231034/CE04_rmatrix.md:267:compute/tests/test_rmatrix_landscape.py
audit_campaign_20260412_231034/CE04_rmatrix.md:280:The user wants me to read and verify a specific test file, likely related to the requested slice, which might involve checking multiple files. I think I should focus on the main AP126 test file, like `test_rmatrix_landscape.py`, and others such as `test_rmatrix_poles_comprehensive.py` and `test_theorem_pva_classical_r_matrix_engine.py`. The `-k` expression selects by any match of "r_matrix" or "rmatrix," so that could include quite a few files. The user specifically asks about the presence of level prefixes and hardcoded expected values. I'll need to inspect the relevant files carefully for these details.
audit_campaign_20260412_231034/CE04_rmatrix.md:293:/bin/zsh -lc "sed -n '960,1125p' compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/CE04_rmatrix.md:329:    Path 3 (rmatrix_landscape): compare with existing collision-residue engine
audit_campaign_20260412_231034/CE04_rmatrix.md:368:I need to gather specific findings with file references and descriptions. I wonder if I should use the explorer agent for this task, but maybe that's unnecessary. Still, it might be okay to proceed without it. I'll inspect `test_rmatrix_landscape.py` and focus on key assertions. I’ll also search for any VERIFIED comments as those could provide valuable insights. This approach should help me pinpoint the information I need!
audit_campaign_20260412_231034/CE04_rmatrix.md:370:I’ve confirmed one core module already: `test_rmatrix_landscape.py` does enforce the AP126/AP141 mechanical boundary check and distinguishes `r|_{k=0}=0` from `\kappa(k=0)\neq 0` for affine KM. I’m now checking whether those assertions are actually source-backed per AP10/AP128, because passing tests alone would not satisfy the repo’s own oracle discipline.
audit_campaign_20260412_231034/CE04_rmatrix.md:372:/bin/zsh -lc 'rg -n "VERIFIED|assert .*==|assert .*!=|Fraction'"\\(|k=0|AP126|AP141\" compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/CE04_rmatrix.md:375:/bin/zsh -lc "sed -n '1,260p' compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
audit_campaign_20260412_231034/CE04_rmatrix.md:439:r"""Tests for rmatrix_landscape.py: explicit r-matrices for 8 standard families.
audit_campaign_20260412_231034/CE04_rmatrix.md:463:I need to inspect the collect-only output, but it might be too slow. Maybe I could use a faster command like `python3 -m pytest compute/tests/test_rmatrix_landscape.py ...`? However, the user requested a full slice, so I’m just waiting for that to complete. I think I should note if the command doesn’t finish in a reasonable time. Polling every 30 seconds could work well to manage this.
audit_campaign_20260412_231034/CE04_rmatrix.md:581:# 13. Pole-order cross-checks with rmatrix_landscape
audit_campaign_20260412_231034/CE04_rmatrix.md:585:    """Cross-check r-matrix poles against rmatrix_landscape.py.
audit_campaign_20260412_231034/CE04_rmatrix.md:689:/bin/zsh -lc 'python3 -m pytest compute/tests/test_rmatrix_landscape.py compute/tests/test_theorem_pva_classical_r_matrix_engine.py compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py compute/tests/test_theorem_three_way_r_matrix_engine.py -q --tb=short 2>&1 | tail -40' in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/CE04_rmatrix.md:757:/bin/zsh -lc "nl -ba compute/tests/test_rmatrix_landscape.py | sed -n '1010,1108p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
audit_campaign_20260412_231034/CE04_rmatrix.md:863:/bin/zsh -lc 'rg -n "# VERIFIED:|VERIFIED:" compute/tests/test_rmatrix_landscape.py compute/tests/test_theorem_pva_classical_r_matrix_engine.py compute/tests/test_theorem_three_way_r_matrix_engine.py compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
audit_campaign_20260412_231034/CE04_rmatrix.md:937:The full keyword slice is not hanging outright; it is just much larger than the core subset. While that runs, I’ve confirmed the key structural split already: `test_rmatrix_landscape.py` enforces trace-form AP126 vanishing, but other selected files encode different normalizations and often do so without the mandated `# VERIFIED` source tags.
audit_campaign_20260412_231034/CE04_rmatrix.md:946:I’m considering around 1200 tests that might take about 6-7 minutes. I need to inspect the early lines in `test_rmatrix_landscape`, especially concerning the kappa formulas. I wonder if using rg might help since there are no verified comments yet. I need to assess severity levels, like whether a wrong expectation due to inconsistent normalization could be critical. If there’s a convention difference between KZ and trace-form, it could indicate a slice inconsistency. The user wants to check for specific findings too.
audit_campaign_20260412_231034/CE04_rmatrix.md:950:I’m thinking about checking whether another file uses KZ without a boundary check at k=0, like in `theorem_three_way`. I didn't find anything there, but I noticed that lines 171-176 might expect 1/(k+2) without mentioning the AP126 trace-form or bridge. Since a selected slice includes `test_rmatrix_landscape.py`, this discrepancy could cause an engine test suite to pass despite a k-prefactor bug. While it might not be mathematically incorrect to use KZ, I need to clarify that the k=0→0 point applies only to trace-form files.
collab wait(call_cybkiCTOkry8tGZ2dDkVmSdc)
  receivers: 019d87a9-20c6-7281-aab8-4c65271ae24a

thinking
**Summarizing canonical and wrapper r-matrix files**

I'll identify the canonical r-matrix compute-engine as `compute/lib/rmatrix_landscape.py` with its direct tests in `compute/tests/test_rmatrix_landscape.py`. I'll also mention wrapper modules like `theorem_pva_classical_r_matrix_engine.py` and `theorem_virasoro_spectral_r_matrix_engine.py` that use cross-check functions referencing the canonical module, plus their tests. I'll note other related wrappers such as `theorem_three_way_r_matrix_engine.py` and `elliptic_rmatrix_shadow.py` with its tests, highlighting duplicates or reimplementations, keeping the summary concise and focused on file paths and roles.
codex
**Canonical r-matrix engines**
- `compute/lib/rmatrix_landscape.py` serves as the canonical r-matrix engine: it defines the `FamilyRMatrix` data, exposes `verify_ap19`/`FamilyRMatrix.verify_ap19`, and is cross-checked by many downstream scripts (e.g., `theorem_pva_classical_r_matrix_engine`, `theorem_virasoro_spectral_r_matrix_engine`, and `elliptic_rmatrix_shadow.py` mention it explicitly as the source of the collision-residue formulas).
- The paired canonical test is `compute/tests/test_rmatrix_landscape.py`: it exercises the eight standard families, enforces the trace-form level-prefactor (`r=k·Ω/z`), and checks the AP126 k=0 vanishing plus the advertised pole orders.

**Duplicate/wrapper surfaces**
- `compute/lib/theorem_pva_classical_r_matrix_engine.py` and `compute/tests/test_theorem_pva_classical_r_matrix_engine.py` act as a wrapper: most of their “cross_check_with_rmatrix_landscape” logic just compares the PVA r-matrix to the canonical landscape data rather than rederiving it.
- `compute/lib/theorem_virasoro_spectral_r_matrix_engine.py` (and its test `compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py`) likewise reuses `rmatrix_landscape.py` for pole-order cross-checks; the computation is bespoke, but the verification surface delegates back to the canonical module.
- There are other specialized r-matrix engines (e.g., `compute/lib/theorem_three_way_r_matrix_engine.py`, `compute/lib/elliptic_rmatrix_shadow.py`, `compute/lib/theorem_sl3_yangian_r_matrix_engine.py`) that either reimplement a family-specific normalization or wrap `rmatrix_landscape.py` for consistency, so `rmatrix_landscape.py` remains the single source of truth for the general r-matrix data set.
wait(call_cybkiCTOkry8tGZ2dDkVmSdc) 1 agents complete:
  019d87a9-20c6-7281-aab8-4c65271ae24a completed: "**Canonical r-matrix engines**
- `compute/lib/rmatrix_landscape.py` serves as the canonical r-matrix engine: it defines …"


thinking
**Understanding r_matrix engines**

I need to clarify the exact scope here. The user mentioned "Same for r_matrix engines," which seems to refer to a previous task about kappa engines and their wrappers. I think we should audit both canonical and wrapper files as part of this. It looks like I'm expected to analyze all "r_matrix engines," potentially looking at many files. 

To be thorough, we might have to dive into specific files like theorem_virasoro_spectral_r_matrix_engine, and others. This could be a big task, but it’s manageable!
thinking
**Planning r_matrix audit**

I see that I could use `rg` (ripgrep) on the compute/lib and compute/tests directories. I might want to automate some grepping and run tests to pinpoint any failing cases. It’s essential to inspect all files to track down formulas that could be the cause. 

I’ll consider search patterns like `Omega / z` and `k*Omega/z` to catch any oddities. I should audit everything line-by-line, and since this is a sizeable task, I’ll create a detailed plan update to ensure I'm covering all bases.
codex
Plan for the `r_matrix` engine pass:

1. `in_progress` Enumerate the engine surface in `compute/lib` and `compute/tests`, then search for AP126/AP141/AP19 violations and normalization drift.
2. `pending` Read only the flagged engine/test files in context, verify each suspect formula against the canonical census and limiting cases.
3. `pending` Apply minimum truthful patches to the assigned compute files, keeping the canonical module single-sourced where possible.
4. `pending` Run the narrowest pytest slices that can falsify the fixes, then widen if a wrapper surface depends on them.
5. `pending` Return findings as `PROBLEM at file:line` plus the exact edit applied.
Plan update
  → Enumerate the r_matrix engine surface in compute/lib and compute/tests and search for AP126/AP141/AP19 violations.
  • Read flagged engine/test files in context and verify each suspect formula against canonical sources and limiting cases.
  • Apply minimum truthful patches to the assigned compute files.
  • Run the narrowest pytest slices that can falsify the fixes, widening only if needed.
  • Summarize findings as PROBLEM plus exact edit applied.

thinking
**Enumerating engine surfaces**

I need to examine the engine surfaces, possibly using `rg` to find suspicious patterns in compute/lib/tests. I'll search for all libraries and tests named rmatrix that might reference bare Omega/z or the k=0 absence check. If I'm editing any files, it’s crucial to read them thoroughly. So, I should create a list of lib/test files that include “rmatrix” in their names and use `rg` for that search. Let's get to it!
exec
/bin/zsh -lc "printf '%s
' compute/lib/*rmatrix*.py compute/lib/*r_matrix*.py compute/tests/*rmatrix*.py compute/tests/*r_matrix*.py | sed 's#"'^'"\\./##'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/belavin_rmatrix_verification_engine.py
compute/lib/cohft_givental_rmatrix_engine.py
compute/lib/elliptic_rmatrix_shadow.py
compute/lib/quantum_rmatrix_barcomplex.py
compute/lib/rmatrix_comparison_c3.py
compute/lib/rmatrix_landscape.py
compute/lib/shadow_cohft_rmatrix_engine.py
compute/lib/yangian_rmatrix_arithmetic_engine.py
compute/lib/yangian_rmatrix_sl3.py
compute/lib/penner_matrix_model_delta_f2_engine.py
compute/lib/theorem_pva_classical_r_matrix_engine.py
compute/lib/theorem_sl3_yangian_r_matrix_engine.py
compute/lib/theorem_three_way_r_matrix_engine.py
compute/lib/theorem_virasoro_spectral_r_matrix_engine.py
compute/tests/test_belavin_rmatrix_verification_engine.py
compute/tests/test_cohft_givental_rmatrix.py
compute/tests/test_elliptic_rmatrix_shadow.py
compute/tests/test_prefundamental_rmatrix.py
compute/tests/test_quantum_rmatrix_barcomplex.py
compute/tests/test_rmatrix_comparison_c3.py
exec
/bin/zsh -lc 'rg -n "rmatrix_landscape|cross_check_with_rmatrix_landscape|bar_r_matrix_pole_order|r_classical_pole_order|r1_coefficient|leveled_r_matrix_sl2|classical_r_matrix_fundamental|quantum_r_matrix_" compute/lib compute/tests' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Omega\\s*/\\s*z|Omega/z|k\\*Omega/z|k \\* Omega / z|k\\s*\\*\\s*Omega\\s*/\\s*z|r\\(z\\) = Omega / z|r\\(z\\)=Omega/z|r\\(z\\) = k/z|r\\(z\\) = k\\*Omega/z|critical level|k=0|AP126|AP141\" compute/lib compute/tests" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/bethe_ansatz_shadow.py:39:     Res^{coll}_{0,2}(Theta_A) for A = sl_2-hat_k (AP19, rmatrix_landscape.py).
compute/lib/bethe_ansatz_shadow.py:55:   - rmatrix_landscape.py: r(z) = Omega/z for affine sl_2
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:168:    def bar_r_matrix_pole_order(self, gen_i: str, gen_j: str) -> int:
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:785:    r_classical_pole_order: int   # pole order of r^cl(z) after d-log (AP19)
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:788:    r1_coefficient: Optional[Fraction]   # r^(1) coefficient if computable
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:792:def quantum_r_matrix_heisenberg(k: Fraction = Fraction(1)) -> QuantumRMatrixExpansion:
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:804:        r_classical_pole_order=1,
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:807:        r1_coefficient=Fraction(0),
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:812:def quantum_r_matrix_affine_sl2(k: Fraction = Fraction(1)) -> QuantumRMatrixExpansion:
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:828:        r_classical_pole_order=1,
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:831:        r1_coefficient=Fraction(0),
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:836:def quantum_r_matrix_virasoro(c: Fraction = Fraction(1)) -> QuantumRMatrixExpansion:
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:854:        r_classical_pole_order=3,
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:857:        r1_coefficient=-c / 4,
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:862:def quantum_r_matrix_w3(c: Fraction = Fraction(1)) -> QuantumRMatrixExpansion:
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:874:        r_classical_pole_order=5,  # maximum across all channels (WW)
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:877:        r1_coefficient=None,  # multi-channel, no single scalar
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:944:    heis = quantum_r_matrix_heisenberg()
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:952:    sl2 = quantum_r_matrix_affine_sl2()
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:960:    vir = quantum_r_matrix_virasoro()
 succeeded in 52ms:
Total output lines: 3209

compute/tests/test_operadic_deformation_engine.py:368:        """T37: At critical level (kappa = 0), obstruction vanishes."""
compute/tests/test_shadow_trace_formula_engine.py:801:        These are NOT equal for any w unless k=0. This is expected.
compute/tests/test_discriminant_atlas_complete.py:393:    """At critical level k = -h^vee, Sugawara is undefined."""
compute/tests/test_discriminant_atlas_complete.py:411:        """Near critical level, |c| is large."""
compute/tests/test_discriminant_atlas_complete.py:515:        """c_ghost(g, k) = dim*(h^v*k + (h^v-1)^2) - rank at k=0."""
compute/tests/test_discriminant_atlas_complete.py:518:            gc = ghost_central_charge(type_, rank)  # k=0 default
compute/tests/test_discriminant_atlas_complete.py:524:        # A_1: dim=3, h^v=2, rank=1. At k=0: 3*(2*0+1)-1 = 2
compute/tests/test_discriminant_atlas_complete.py:528:        # A_2: dim=8, h^v=3, rank=2. At k=0: 8*(3*0+(3-1)^2)-2 = 8*4-2 = 30
compute/tests/test_discriminant_atlas_complete.py:532:        # E_8: dim=248, h^v=30, rank=8. At k=0: 248*(30*0+29^2)-8 = 248*841-8 = 208560
compute/tests/test_ds_envelope_functor.py:134:        """c(Vir, k=0) = 1 - 6*1/2 = -2."""
compute/tests/test_ds_envelope_functor.py:583:        """The FF involution k' = -k - 2N has fixed point k = -N (critical level).
compute/tests/test_n2_superconformal_shadow.py:303:        """kappa(N=2, c=6) = 0 (critical level k=-4)."""
compute/tests/test_n2_superconformal_shadow.py:690:        """kappa(c=6) = 0 (critical level k=-4)."""
compute/tests/test_koszul_conductor_table_engine.py:108:    """Heisenberg H_k: c=1, kappa=k, K_kk=0."""
compute/tests/test_koszul_conductor_table_engine.py:119:        # VERIFIED: [DC] kappa(H_0)=0, [LC] k=0 limit trivial
compute/tests/test_koszul_conductor_table_engine.py:127:        # VERIFIED: [DC] kappa'=-k, [SY] K_kk=0 (C18)
compute/tests/test_koszul_conductor_table_engine.py:184:    """V_k(g): kappa=dim(g)*(k+h^v)/(2*h^v), K_kk=0."""
compute/tests/test_koszul_conductor_table_engine.py:187:        """kappa(V_0(sl2)) = dim(sl2)/2 = 3/2.  (C3: k=0 -> dim/2)"""

thinking
**Planning a comprehensive test strategy**

The user wants to identify and fix issues in one go, but I realize there might be hidden bugs beyond just the failing tests. An adversarial audit could be useful here. My plan is to run all the rmatrix tests first to check for failures and then narrow down to the specific compute/tests names. I'll focus on running pytest for the rmatrix-related tests since this could involve quite a bit. It's a substantial task, but I’ll make sure to provide updates along the way!
codex
I have the compute surface now. I’m running the r-matrix-focused pytest slice next to expose concrete failures, then I’ll verify whether each one is a genuine formula bug or just a stale expectation before patching.
exec
/bin/zsh -lc 'pytest -q compute/tests/test_rmatrix_landscape.py compute/tests/test_theorem_pva_classical_r_matrix_engine.py compute/tests/test_quantum_rmatrix_barcomplex.py compute/tests/test_belavin_rmatrix_verification_engine.py compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py compute/tests/test_theorem_three_way_r_matrix_engine.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py compute/tests/test_yangian_rmatrix_sl3.py compute/tests/test_elliptic_rmatrix_shadow.py compute/tests/test_rmatrix_comparison_c3.py compute/tests/test_rmatrix_poles_comprehensive.py' in /Users/raeez/chiral-bar-cobar succeeded in 3.52s:
........................................................................ [  6%]
........................................................................ [ 12%]
........................................................................ [ 19%]
........................................................................ [ 25%]
........................................................................ [ 32%]
........................................................................ [ 38%]
........................................................................ [ 45%]
........................................................................ [ 51%]
........................................................................ [ 58%]
........................................................................ [ 64%]
........................................................................ [ 70%]
........................................................................ [ 77%]
........................................................................ [ 83%]
........................................................................ [ 90%]
........................................................................ [ 96%]
.....................................                                    [100%]
=============================== warnings summary ===============================
compute/tests/test_yangian_rmatrix_arithmetic_engine.py::TestYangBaxterEquation::test_ybe_coefficient_relations_so5
compute/tests/test_yangian_rmatrix_arithmetic_engine.py::TestLandscape::test_landscape_completeness
compute/tests/test_yangian_rmatrix_arithmetic_engine.py::TestLandscape::test_landscape_ybe_all_pass




thinking
**Conducting an audit for issues**

I need to perform an adversarial audit to uncover issues that tests might not catch. There's a warning in the yangian_rmatrix_arithmetic_engine suggesting a potential bug. Since the user mentioned similar concerns for the r_matrix engines, I should inspect those warnings and possible latent issues. I'll look for obvious formula drift in the documentation, audit engine modules for suspicious formulas, and search for any concerning patterns like "Omega/z" in the actual code files. I'll make sure to cover everything within my assigned scope.
thinking
**Evaluating quantum rmatrix issues**

I’m looking at the quantum_rmatrix_barcomplex, where the docstring states r(z) = Omega/z. The function classical_r_matrix_fundamental returns Omega/z, independent of k, which raises questions about its parameterization by level. The AGENTS mention affine KM and KZ conventions which mix KZ quantum q with classical r=Omega/z but seem to lack clarity around the level aspect. I’m reflecting on whether the compute engine is intended for quantum groups independent of level or if it's using a normalized classical r-matrix where level is encoded by hbar.
thinking
**Clarifying conventions for r-matrix**

I’m noticing that the AGENTS AP126 states that a level prefix is mandatory in the compute engine for writing the affine KM r-matrix. However, the KZ convention allows for the expression as Omega/((k+h^v)z). I need to ensure I understand the exact scope here. It seems crucial to clarify when the level prefix is necessary and how it interacts with the conventions being discussed, as this could affect my implementation decisions.
thinking
**Inspecting compute/lib files**

I’m thinking I could use grep to find bare Omega/z in the rmatrix modules. I want to focus on the compute/lib files list and check for any suspicious lines. My approach will involve using a command like `rg -n "Omega / z|Omega/z|k\\*Omega|k \\* Omega|\\(k\\+h|hbar\\*Omega|r\\(z\\)"` to scan those files for relevant patterns. This should help in identifying any potential issues.
codex
The test slice is green. I’m in the hostile reread phase now: looking for latent formula/convention bugs that tests currently miss, especially level-normalization drift and numerical pathologies signaled by runtime warnings.
exec
/bin/zsh -lc "rg -n \"Omega\\s*/\\s*z|Omega/z|k\\s*\\*\\s*Omega|\\(k\\+h\\"'^vee'"\\)|\\(k\\+h\\"'^v'"\\)|hbar\\s*\\*\\s*Omega|r\\(z\\) =|critical level|k=0\" compute/lib/rmatrix_landscape.py compute/lib/theorem_pva_classical_r_matrix_engine.py compute/lib/quantum_rmatrix_barcomplex.py compute/lib/belavin_rmatrix_verification_engine.py compute/lib/theorem_virasoro_spectral_r_matrix_engine.py compute/lib/theorem_three_way_r_matrix_engine.py compute/lib/theorem_sl3_yangian_r_matrix_engine.py compute/lib/yangian_rmatrix_arithmetic_engine.py compute/lib/yangian_rmatrix_sl3.py compute/lib/elliptic_rmatrix_shadow.py compute/lib/rmatrix_comparison_c3.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/rmatrix_comparison_c3.py:55:   The Drinfeld-Kohno theorem: monodromy of KZ_2 = exp(pi*i * Omega/(k+h^vee))
compute/lib/rmatrix_comparison_c3.py:57:   q = exp(pi*i/(k+h^vee)).
compute/lib/elliptic_rmatrix_shadow.py:3:At genus 0, the collision residue r(z) = Res^{coll}_{0,2}(\Theta_A) gives
compute/lib/elliptic_rmatrix_shadow.py:4:the rational r-matrix r(z) = \Omega/z for affine Lie algebras.  At genus 1,
compute/lib/elliptic_rmatrix_shadow.py:32:    R^{ell}(z,\tau) \to R^{trig}(z)            \to R^{rat}(z) = 1 + \Omega/z
compute/lib/elliptic_rmatrix_shadow.py:401:    # ... the precise normalization ensures r(z) ~ Omega/z as z -> 0.
compute/lib/elliptic_rmatrix_shadow.py:555:    r"""Rational r-matrix for sl_2: r(z) = \Omega / z (4x4).
compute/lib/elliptic_rmatrix_shadow.py:560:    r^{rat}(z) = (E\otimes F + F\otimes E + H\otimes H/2) / z = \Omega / z.
compute/lib/elliptic_rmatrix_shadow.py:622:            # so r^{trig}(z/L) ~ L * Omega/z = L * r^{rat}(z)
compute/lib/elliptic_rmatrix_shadow.py:755:        A_z = r^{ell}(z,\tau) / (k+h^v)
compute/lib/elliptic_rmatrix_shadow.py:756:        A_\tau = \wp(z,\tau) \Omega / (2\pi i (k+h^v))
compute/lib/elliptic_rmatrix_shadow.py:1005:        r^{ell}(z) = \Omega/z + O(1)
compute/lib/elliptic_rmatrix_shadow.py:1103:    The modular characteristic kappa = dim(g)(k+h^v)/(2h^v).
compute/lib/elliptic_rmatrix_shadow.py:1117:    # z * r(z) ~ k * Omega, so extract the Casimir eigenvalue
compute/lib/elliptic_rmatrix_shadow.py:1127:    # And tr_1(k*Omega) = k * C_2 * I
compute/lib/elliptic_rmatrix_shadow.py:1197:        r^{ell}(z) = \Omega/z + r_0(\tau) + r_1(\tau) z + ...
compute/lib/elliptic_rmatrix_shadow.py:1214:        r0 = r_ell - Omega / z_small
compute/lib/yangian_rmatrix_sl3.py:5:residue of the MC element, yielding the r-matrix r(z) = k\Omega/z where
compute/lib/yangian_rmatrix_sl3.py:13:      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
compute/lib/yangian_rmatrix_sl3.py:334:    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_virasoro_spectral_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,910p' compute/lib/yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_three_way_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
        'ybe_errors': ybe_errors,
        'max_ybe_error': max(ybe_errors) if ybe_errors else 0.0,
        'test_params': test_params,
        'passes': max(ybe_errors) < 1e-8 if ybe_errors else True,
    }


def _ybe_numerical_error(lie_type: str, n: int, u: float, v: float) -> float:
    """Compute the YBE residual ||LHS - RHS|| at given (u, v)."""
    data = lie_algebra_data(lie_type, n)
    N = data['fund_dim']

    R_uv = _full_rmatrix(lie_type, n, u - v)
    R_u = _full_rmatrix(lie_type, n, u)
    R_v = _full_rmatrix(lie_type, n, v)

    R12 = _embed_12(R_uv, N)
    R13 = _embed_13(R_u, N)
    R23 = _embed_23(R_v, N)

 succeeded in 50ms:
r"""Virasoro spectral R-matrix from OPE collision residues.

Computes the spectral R-matrix for the Virasoro algebra on Verma module
weight spaces, by extracting collision residues from the OPE and computing
the path-ordered exponential of the resulting connection on Conf_2^ord(C).

MATHEMATICAL FRAMEWORK
======================

1. THE VIRASORO OPE AND COLLISION RESIDUE (AP19)

   The Virasoro OPE is:
       T(z) T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)

   By AP19 (d log absorption), the bar construction extracts residues along
   d log(z_i - z_j), which absorbs one power of (z-w):
       r^{coll}(z) = (c/2)/z^3 + 2T/z

   The z^{-4} pole becomes z^{-3}, the z^{-2} pole becomes z^{-1},
   and the z^{-1} pole becomes z^0 = regular (DROPS).
 succeeded in 52ms:
r"""sl_3 Yangian R-matrix from the ordered bar complex — first rank-2 extraction.

Extracts R(z) from the ordered bar complex of the affine Kac--Moody algebra
\widehat{sl}_3 at level k and verifies it against the Dimofte--Niu--Py (DNP)
dg-shifted Yangian construction.

This engine goes beyond the existing yangian_rmatrix_sl3.py by:

  (1) Computing the Casimir tensor in BOTH the fundamental (dim 3) and
      adjoint (dim 8) representations of sl_3.

  (2) Constructing the multi-point KZ Hamiltonians and verifying their
      commutativity (the infinitesimal braid relations, IBR).

  (3) Computing Verlinde fusion rules for sl_3 at small levels k = 1, 2, 3.

  (4) Comparing with the DNP dg-shifted Yangian construction:
      DNP r(z) = MK Res^{coll}_{0,2}(Theta_A) at genus 0.

Mathematical content
 succeeded in 52ms:
r"""Three-way cross-check of r-matrices: DNP25, KZ25, GZ26, and bar collision residue.

THEOREM (three-way r-matrix consistency):
The collision residue r(z) = Res^{coll}_{0,2}(Theta_A) can be computed from four
independent perspectives, all of which must agree:

  (1) BAR COLLISION RESIDUE (our framework):
      r(z) = Res^{coll}_{0,2}(Theta_A), extracted from the bar complex differential.
      The d log kernel absorbs one pole order (AP19): if the OPE has max pole
      order p, then r(z) has max pole order p - 1.

  (2) PVA LAMBDA-BRACKET (KZ25 / Gui-Li-Zeng):
      r^{cl}(z) is the classical r-matrix extracted from the PVA lambda-bracket
      {a_lambda b} by the substitution lambda -> 1/z (with divided-power
      convention AP44).  At tree level: r(z) = r^{cl}(z).

  (3) DNP25 MC ELEMENT:
      r(z) is the MC element of the dg-shifted Yangian on A^!_line.
      It satisfies the A_infinity Yang-Baxter equation.
      For strict algebras (m_k = 0 for k >= 3): CYBE.

thinking
**Searching for formula**

I’m considering searching within the repository for the type C formula. I think using a tool like `rg` could be effective for that. It should allow me to search quickly and efficiently. I'll just need to make sure I specify what I’m looking for clearly to get the right results. It’s all about optimizing the search process to find the formula I need without getting lost in too much information.
codex
I found one concrete formula drift already: the type `C` branch in `yangian_rmatrix_arithmetic_engine.py` documents `u + κ_R` but implements `u - κ_R`. I’m verifying that against the repo’s other orthogonal/symplectic conventions before patching, because that’s a real sign-level risk rather than a cosmetic mismatch.
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Tests for yangian_rmatrix_arithmetic_engine.py.

Verification axes:
  Path 1: Direct R-matrix computation from Yangian coproduct
  Path 2: Shadow extraction from Theta_A (kappa and Casimir)
  Path 3: Yang-Baxter equation self-consistency
  Path 4: Representation-theoretic eigenvalue computation

Ground truth sources:
  - Molev, "Yangians and classical Lie algebras", AMS 2007.
  - Chari-Pressley, "A Guide to Quantum Groups", Cambridge 1994.
  - Jimbo, "A q-difference analogue of U(g)", Lett. Math. Phys. 1985.
  - Belavin-Drinfeld, "Solutions of the classical YBE" (1982).
  - landscape_census.tex (kappa formulas)
  - AP19 (bar kernel absorbs a pole)
  - AP39 (C_2 != kappa for rank > 1)
"""

import math

 succeeded in 51ms:
r"""Yangian R-matrix from the bar complex for sl_3 --- first non-sl_2 extraction.

Extracts R(z) = Res^{coll}_{0,2}(\Theta_A) for the sl_3 affine Kac--Moody
algebra at level k. The bar propagator d\log E(z,w) extracts the collision
residue of the MC element, yielding the r-matrix r(z) = k\Omega/z where
\Omega is the quadratic Casimir tensor in sl_3 \otimes sl_3 (AP19: one pole
order below the OPE).

Mathematical structure
---------------------
* OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
* r-matrix (collision residue of bar):
      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
  This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
* R-matrix (perturbative in 1/\kappa):
      R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
  where \kappa = 4(k+3)/3 = dim(sl_3)(k+h^\vee)/(2 h^\vee).
* In the fundamental representation (V = C^3):
      R^{fund}(z) = I + P/z   (Yang R-matrix, at leading order)
  where P is the permutation operator on V \otimes V.
exec
/bin/zsh -lc "rg -n \"u \\+ kappa_R|u - kappa_R|Type C|sp2N|symplectic|I - P/u - K/\\(u|I - P/u \\+ Q/\\(u\" compute/lib compute/tests chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2119

chapters/examples/deformation_quantization.tex:498:where $K_{\text{cobar}} \in H^n_{D}(\overline{C}_n, \mathcal{F}^{!\boxtimes n})$ is the local cohomology class supported on the boundary, and the symplectic (antisymmetric) pairing of $\beta\gamma$ dualizes under Verdier duality to the anticommuting (fermionic) pairing. See Section~\ref{sec:fermion-boson-koszul} for the complete computation.
chapters/examples/deformation_quantization.tex:1819:canonical symplectic form.
appendices/nonlinear_modular_shadows.tex:7:symplectic form, and the two dual packages $\mathcal{Q}_g(\cA)$
appendices/nonlinear_modular_shadows.tex:466:That is only the linear shadow. The correct theorem is that there is a single formal moduli problem carrying a shifted symplectic structure, and the two dual deformation packages are Lagrangian inside it. The first-principles data are therefore not two vector spaces and a bookkeeping identity, but:
appendices/nonlinear_modular_shadows.tex:471:\item a cyclic pairing turning the total deformation problem into a shifted symplectic formal moduli problem.
appendices/nonlinear_modular_shadows.tex:548:If the cyclic pairing is perfect and bar--cobar duality identifies the normal complex of one side with the shifted dual tangent complex of the other, maximal isotropicity follows: the two sides are opposite polarizations of a single symplectic deformation problem.\qedhere
appendices/nonlinear_modular_shadows.tex:551:\begin{theorem}[Ambient complementarity as a shifted symplectic formal moduli problem; \ClaimStatusProvedElsewhere{} {\normalfont (see Theorem~\ref{thm:ambient-complementarity-fmp})}]
appendices/nonlinear_modular_shadows.tex:557:Then $\mathcal M_{\mathrm{comp}}(\cA)$ carries a canonical $(-1)$-shifted symplectic structure, and the one-sided deformation problems of $\cA$ and of $\cA^!$ define Lagrangian maps
appendices/nonlinear_modular_shadows.tex:570:\item a shifted symplectic pairing on that problem,
appendices/nonlinear_modular_shadows.tex:583:Let $\mathcal M$ be a pointed $(-1)$-shifted symplectic formal moduli problem, and let
appendices/nonlinear_modular_shadows.tex:609:Because $i_+$ is Lagrangian, the normal complex of $\mathcal L_+$ in $\mathcal M$ is canonically identified with $T^*[-1]\mathcal L_+$. Formally along $\mathcal L_+$, the symplectic neighborhood theorem gives a pointed equivalence with the shifted cotangent bundle. Under this identification, $\mathcal L_+$ becomes the zero section. Since $\mathcal L_-$ is complementary to the zero section, it is the graph of a one-form $\alpha_+$. The graph of a one-form in a cotangent bundle is Lagrangian if and only if the one-form is closed, because the pullback of the canonical symplectic form is exactly $d\alpha_+$. In a pointed formal neighborhood every closed one-form is exact, which produces $S_+$.\qedhere
appendices/nonlinear_modular_shadows.tex:633:The two functions generate the same formal Lagrangian subspace of the same shifted symplectic ambient moduli problem, viewed from the two opposite cotangent charts. The coordinate change between these two charts is the formal Legendre transform.\qedhere
appendices/nonlinear_modular_shadows.tex:2050:\item The quadratic theory is the proved scalar and shifted-symplectic complementarity package.
chapters/examples/beta_gamma.tex:198:(i)~symplectic bosons on a curve (geometric/physical);
chapters/examples/beta_gamma.tex:329:$\lambda = 1/2$: $c = -1$ (symplectic bosons).
chapters/examples/beta_gamma.tex:474:\item Relations: $P \subset j_* j^*(N \boxtimes N)$ encode symplectic pairing:
chapters/examples/beta_gamma.tex:490:For $\mathcal{F}$: The dual of the Clifford relation $b \boxtimes c + c \boxtimes b$ is the Weyl/symplectic
chapters/examples/beta_gamma.tex:552:This is the symplectic pairing.

thinking
**Evaluating code implementation**

I think I’m realizing that it’s not about the implementation itself. There's no need to patch the formula unless I can verify it first. The warnings due to the poles might still warrant a patch, but I believe the documentation mismatch could be an issue on its own. Also, I noticed that the actual code in `yangian_rmatrix_sl3.py` returns `Omega / z` from the function `r_matrix_fundamental(z)`, even though the docstring claims it should return `k*Omega/z`. I really need to inspect the function around line 334.
exec
/bin/zsh -lc "sed -n '320,390p' compute/lib/yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

    d^{abc} = (1/2) tr(T^a {T^b, T^c}).

    For sl_2: d^{abc} = 0 (no cubic invariant).
    For sl_3: d^{abc} != 0 (unique cubic invariant).
    """
    return cubic_casimir_tensor_fund()


# ============================================================
# r-matrix from bar complex collision residue
# ============================================================

def r_matrix_abstract() -> Dict[str, object]:
    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.

    The bar construction for the affine KM algebra sl_3_k uses the
    propagator d\log E(z,w).  The collision residue (AP19) extracts the
    simple pole of the OPE: [a, b] (structure constants), NOT the
    double pole k g^{ab} (curvature).
exec
/bin/zsh -lc "sed -n '690,760p' compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,320p' compute/lib/belavin_rmatrix_verification_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '540,620p' compute/lib/elliptic_rmatrix_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    full_decomp = sl3_tensor_product(lam[0], lam[1], mu[0], mu[1])
    return {nu: mult for nu, mult in full_decomp.items() if nu in integrable}


# ============================================================
# DNP comparison
# ============================================================

def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
    r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.

    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
        r^{DNP}(z) = Omega/z
    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
    """
    return r_matrix_fund(z)


def dnp_comparison_report(z: complex) -> Dict[str, object]:
    r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 succeeded in 50ms:

    if abs(np.sin(PI * z)) < 1e-300:
        return np.full((4, 4), complex(float('inf')))

    cot_z = np.cos(PI * z) / np.sin(PI * z)
    csc_z = 1.0 / np.sin(PI * z)

    r = (PI * cot_z * 0.5 * np.kron(H, H)
         + PI * csc_z * np.kron(E, F)
         + PI * csc_z * np.kron(F, E))

    return r


def rational_r_matrix_sl2(z: complex) -> np.ndarray:
    r"""Rational r-matrix for sl_2: r(z) = \Omega / z (4x4).

    The simplest r-matrix, obtained as the rational degeneration
    of the trigonometric and then elliptic families.

 succeeded in 50ms:
    """
    r = np.zeros((4, 4), dtype=complex)
    for a in range(3):
        w_a = belavin_weight_function(z, tau, a + 1, n_terms)
        r += w_a * np.kron(SIGMAS[a], SIGMAS[a]) / 2.0
    return r


def leveled_r_matrix_sl2(z: complex, tau: complex, k: float,
                          n_terms: int = 80) -> np.ndarray:
    r"""Level-prefixed elliptic r-matrix: r^{ell}(z, tau) = k * r^{Belavin}(z, tau).

    AP126: k=0 -> r=0.  AP141: verify this after every construction.
    """
    return k * belavin_r_matrix_sl2(z, tau, n_terms)


# ============================================================
# 4. Trigonometric and rational r-matrices (degeneration targets)
# ============================================================
exec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Tests for Yangian R-matrix extraction from the bar complex for sl_3.

First non-sl_2 extraction of R(z) = Res^{coll}_{0,2}(\Theta_A).

Ground truth references:
    - sl3_bar.py: structure constants, Killing form, OPE data
    - yangian_residue_extraction.py: Yang R-matrix for sl_N, YBE, channel decomposition
    - yangians.tex: DK bridge, r-matrix = collision residue of bar MC element
    - landscape_census.tex: kappa(sl_3_k) = 4(k+3)/3

Tests organized by:
    1. Fundamental representation consistency (bracket, Killing form)
    2. Casimir tensor and identity Omega = P - I/N
    3. r-matrix pole structure (AP19 verification)
    4. Yang--Baxter equation (additive and multiplicative conventions)
    5. Unitarity and crossing
    6. Spectral decomposition (Sym^2 / Lambda^2)
    7. sl_2 reduction (embedding sl_2 -> sl_3)
    8. kappa dependence and large-kappa limit
    9. R(z) at special points (z = 0, z -> infinity)
 succeeded in 51ms:
r"""Tests for sl_3 Yangian R-matrix from the ordered bar complex.

First rank-2 computation of the Yangian R-matrix from the monograph's
framework, going beyond the well-studied sl_2 case.

Tests organized by:
    1. Fundamental representation consistency
    2. Adjoint representation consistency
    3. Casimir tensor — fundamental (Omega = P - I/3)
    4. Casimir tensor — adjoint (eigenvalue decomposition)
    5. r-matrix pole structure (AP19)
    6. Yang--Baxter equation (fundamental)
    7. Classical Yang--Baxter equation (both representations)
    8. Infinitesimal braid relations / KZ commutativity (n=3,4)
    9. Verlinde fusion rules (levels 1,2,3)
   10. DNP comparison
   11. sl_2 cross-check (rank-1 reduction)
   12. Spectral decomposition (Sym^2 / Lambda^2)
   13. Kappa formula and modular characteristic
   14. Cross-checks with yangian_rmatrix_sl3.py

thinking
**Considering test adjustments**

I’m thinking that the tests don’t check for k dependence, which seems like an oversight. It might be beneficial to add an optional k and adjust the tests accordingly. I also need to explore the theorem related to the sl3 yangian r-matrix engine, as it may face a similar issue. I should search the file for the r_matrix_fund signature and its associated tests to ensure everything aligns properly.
exec
/bin/zsh -lc "sed -n '280,360p' compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"def r_matrix_fund|def r_matrix_adj|r_matrix_fund\\(|r_matrix_adj\\(|Omega/z|k\\*Omega / z|k\\*Omega/z\" compute/lib/theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    """Permutation P on C^N otimes C^N: P(e_i otimes e_j) = e_j otimes e_i."""
    P = np.zeros((N * N, N * N))
    for i in range(N):
        for j in range(N):
            P[i * N + j, j * N + i] = 1.0
    return P


def verify_casimir_identity_fund() -> bool:
    r"""Verify Omega^{fund} = P - (1/3) I on C^3 otimes C^3."""
    Omega = casimir_tensor_fund()
    P = permutation_matrix(FUND_DIM)
    I = np.eye(FUND_DIM ** 2)
    return bool(np.allclose(Omega, P - I / FUND_DIM, atol=1e-10))


def adjoint_casimir_eigenvalues() -> Dict[str, object]:
    r"""Eigenvalue decomposition of Omega^{adj} on adj otimes adj.

    8 x 8 = 27 + 10 + 10* + 8 + 8 + 1.
 succeeded in 50ms:
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:30:  * The collision residue (AP19): r(z) = Omega/z where Omega is the
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:52:  * Classical Yang--Baxter equation for r(z) = Omega/z:
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:63:        DNP r(z) = Omega/z = MK bar collision residue.
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:339:def r_matrix_fund(z: complex) -> np.ndarray:
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:342:    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:348:def r_matrix_adj(z: complex) -> np.ndarray:
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:423:    r"""Verify the CYBE for r(z) = Omega/z in representation of dim N.
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:702:        r^{DNP}(z) = Omega/z
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:705:    return r_matrix_fund(z)
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:712:    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:717:    r_mk = r_matrix_fund(z)
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:727:        "r_MK": "Omega/z (bar collision residue)",
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:728:        "r_DNP": "Omega/z (A_infty structure on A^!)",
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:277:    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:280:        """r(z) = Omega/z has a single pole (AP19)."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:281:        r = r_matrix_fund(1.0)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:287:        r = r_matrix_fund(100.0)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:298:        r1 = r_matrix_adj(1.0)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:299:        r2 = r_matrix_adj(2.0)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:503:        """r^{MK}(z) = r^{DNP}(z) = Omega/z at genus 0."""
exec
/bin/zsh -lc "sed -n '740,930p' compute/lib/yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,760p' compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"_full_rmatrix\\(|ybe_coefficient_relations\\(|rmatrix_arithmetic_landscape|test_params|u =|v =|0\\.5|2\\.5|3\\.0\" compute/lib/yangian_rmatrix_arithmetic_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

    universal_check = abs(C2 - dim_g / N) < 1e-8

    return {
        'type': f'{lie_type}_{n}',
        'kappa': kappa,
        'C2': C2,
        'dim_g': dim_g,
        'dim_fund': N,
        'C2_equals_dim_g_over_N': universal_check,
        'dim_g_over_N': dim_g / N,
    }


# =========================================================================
# 4.  Yang-Baxter arithmetic
# =========================================================================

def ybe_coefficient_relations(lie_type: str, n: int,
                              max_total_order: int = 6
 succeeded in 52ms:
            f"CYBE failed for {lie_type}_{n}: "
            f"IBR1={result['ibr1_error']}, IBR2={result['ibr2_error']}"
        )

    def test_cybe_g2(self):
        """CYBE for G_2 in the 7-dim representation."""
        result = verify_cybe('G2', 2)
        assert result['passes'], f"CYBE failed for G_2: max_err={result['max_error']}"


# =========================================================================
# Section 6: Operator algebra tests
# =========================================================================

class TestOperatorAlgebra:
    """Tests for P, Q, K operator identities."""

    def test_P_squared_is_I(self):
        """P^2 = I for all N."""
        for N in [2, 3, 4, 5]:
 succeeded in 51ms:
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:65:    rmatrix_arithmetic_landscape,
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:209:        assert abs(C2[0, 0] - 3.0 / 2) < 1e-12
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:210:        assert abs(C2[1, 1] - 3.0 / 2) < 1e-12
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:344:        kappa_R = 2 - 0.5  # n - 1/2 = 1.5
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:353:        kappa_R = 3.0  # n+1 = 3
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:401:        assert abs(result['C2_fund'] - 3.0 / 2) < 1e-10
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:454:        # Use parameters that avoid the pole at u-v = kappa_R = n-1.
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:461:        params = [(2.5, 0.7), (5.0, 3.0), (10.0, 1.0), (4.2, 2.8), (7.7, 3.3)]
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:468:        for u, v in [(3.0, 1.0), (6.0, 2.0), (8.5, 4.5)]:
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:474:        result = ybe_coefficient_relations('A', 1, 4)
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:478:        result = ybe_coefficient_relations('B', 2, 4)
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:566:        for tau in [1j, 2j, 0.5 + 1j]:
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:573:        for tau in [1j, 0.5 + 1j]:
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:578:        for tau in [1j, 0.5 + 2j, 0.3 + 1.5j]:
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:585:        """At tau = i: theta_2(0,i) = theta_4(0,i) (square lattice symmetry)."""
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:601:        """Jacobi identity at the Gaussian CM point tau = i."""
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:606:        """Jacobi identity at the Eisenstein CM point tau = rho."""
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:611:        """At tau = i: theta_3 / theta_4 should be close to 2^{1/4}."""
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:748:        for angle in [0.1, 0.5, 1.0, 2.0]:
compute/tests/test_yangian_rmatrix_arithmetic_engine.py:809:        for k in [1.0, 3.0]:
exec
/bin/zsh -lc "rg -n \"w3_WW|dT/z\\"'^2|z'"\\"'^{-2}|z'"\\"'^'"\\{-2\\}\" compute/lib/rmatrix_landscape.py compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '340,450p' compute/lib/rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:w3_WW|dT/z\^2|z\^{-2}|z\^\{-2\})
                         ^
error: repetition quantifier expects a valid decimal
 succeeded in 50ms:
      generalized CYBE with the Virasoro algebra as the underlying
      Lie algebra; verified in Feigin-Fuchs / Belavin-Drinfeld).
    - Skew-symmetry: r(z) is an odd function of z (only odd poles).
    - Bosonic parity: poles at z^{-3} and z^{-1} only (both odd).
    """
    fam = FamilyRMatrix("Virasoro")
    fam.generators = [("T", Fraction(2))]
    fam.statistics = {"T": "bosonic"}
    fam.kappa = c / Fraction(2)

    fam.add_channel(
        "TT", "T", "T",
        ope_poles={4: c / 2, 2: Fraction(2), 1: Fraction(1)},
        description=f"T(z)T(w) ~ (c/2)/(z-w)^4 + 2T/(z-w)^2 + dT/(z-w)"
    )
    return fam


# ========================================================================
# 5. W_3 (TT channel) -- same as Virasoro
exec
/bin/zsh -lc "rg -n \"r_matrix_fund\\(|r_matrix_abstract\\(|R_residue_at_zero|full_extraction_report|formula\" compute/lib/yangian_rmatrix_sl3.py compute/tests/test_yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/yangian_rmatrix_sl3.py:333:def r_matrix_abstract() -> Dict[str, object]:
compute/lib/yangian_rmatrix_sl3.py:358:        "formula": "r(z) = k*Omega / z",
compute/lib/yangian_rmatrix_sl3.py:363:def r_matrix_fund(z: complex) -> np.ndarray:
compute/lib/yangian_rmatrix_sl3.py:574:    # Hmm, let me use the standard formula C_2 = dim(adj)/(2*dim(rep)) for fund.
compute/lib/yangian_rmatrix_sl3.py:775:def R_residue_at_zero() -> np.ndarray:
compute/lib/yangian_rmatrix_sl3.py:843:def full_extraction_report(k=None) -> Dict[str, object]:
compute/lib/yangian_rmatrix_sl3.py:867:        "r_matrix_formula": "r(z) = k*Omega/z where Omega = P - I/3",
compute/lib/yangian_rmatrix_sl3.py:868:        "R_matrix_formula": "R(z) = z*I + P (Yang, additive)",
compute/lib/yangian_rmatrix_sl3.py:937:    report = full_extraction_report(k=1)
compute/tests/test_yangian_rmatrix_sl3.py:84:    R_residue_at_zero,
compute/tests/test_yangian_rmatrix_sl3.py:87:    full_extraction_report,
compute/tests/test_yangian_rmatrix_sl3.py:228:        info = r_matrix_abstract()
compute/tests/test_yangian_rmatrix_sl3.py:247:        info = r_matrix_abstract()
compute/tests/test_yangian_rmatrix_sl3.py:252:        r = r_matrix_fund(100.0)
compute/tests/test_yangian_rmatrix_sl3.py:441:    """Verify kappa formula and large-kappa behavior."""
compute/tests/test_yangian_rmatrix_sl3.py:443:    def test_kappa_formula_k1(self):
compute/tests/test_yangian_rmatrix_sl3.py:447:    def test_kappa_formula_k0(self):
compute/tests/test_yangian_rmatrix_sl3.py:451:    def test_kappa_formula_critical(self):
compute/tests/test_yangian_rmatrix_sl3.py:505:    def test_R_residue_at_zero_is_P(self):
compute/tests/test_yangian_rmatrix_sl3.py:507:        P_res = R_residue_at_zero()

thinking
**Investigating matrix functions**

I’m thinking about patching `r_matrix_abstract(k=1)` and `r_matrix_fund(z,k=1)` and then updating my report. I should double-check the tests, particularly `R_residue_at_zero`, to see if it utilizes `r_matrix`. It’s important to inspect the relevant functions to ensure everything aligns correctly. Making sure the code runs as it should is my priority, so let’s dig into those parts and confirm what’s going on!
exec
/bin/zsh -lc "sed -n '760,880p' compute/lib/yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        norm = verify_ybe_fundamental(z1, z2, z3)
        results[f"YBE at ({z1}, {z2}, {z3})"] = norm < 1e-10
    return results


# ============================================================
# R-matrix at infinity and z = 0
# ============================================================

def R_at_infinity() -> np.ndarray:
    """R(z) -> I as z -> infinity (unitarity at infinity)."""
    N = FUND_DIM
    return np.eye(N * N, dtype=complex)


def R_residue_at_zero() -> np.ndarray:
    """Residue of R(z) = I + P/z at z = 0 is P (the permutation).

    This is the collision residue of the bar construction: the
    permutation operator P exchanges the two tensor factors.





thinking
**Evaluating potential patches**

I'm considering adding an optional `k` parameter to several functions with a default of 1 and updating tests. While this might be a bigger change, it seems manageable. I see potential fix candidates like `belavin_rmatrix_verification_engine.py` and `elliptic_rmatrix_shadow.py`, both involving level-free rational/trigonometric functions, which is fine. I need to ensure I only edit the assigned files, which likely includes specific engine files and tests, as the user hinted at that. This approach seems plausible and contained.
thinking
**Evaluating function parameters**

I'm looking into using an optional `k` parameter in the `_matrix_engine`. I want to ensure that it's being used truthfully, so I need to inspect the function. The existing tests are only calling `r_matrix_fund(z)`, which doesn’t include `k`. To align documentation and functions, we might need to adjust the module, but doing so could break the DNP comparison. Clarifying that these sl3 Yangian modules work in normalized units could be simpler than changing everything. I'll also consider the user's mention about formula enforcement being a priority.
thinking
**Considering helper functions**

I'm thinking about adding helper functions and an optional `k` parameter to better meet expectations. Keeping a default of `k=1` preserves universal normalized behavior for DNP comparisons. I wonder if I should check `theorem_three_way_r_matrix_engine.py`, which uses KZ instead of trace, for possible insights. Although it mentions \(1/(k+h^v)\), which seems fine, I noticed some inconsistencies in notes about collision vs. PVA. I might need to run a static cross-check script for `r_matrix` functions at `k=0` and see if I can add missing parameters in the code.
thinking
**Analyzing k value implications**

I'm considering that if `k=0`, then `r` vanishes, but I'm not sure about the implications for DNP. It seems the DNP Yangian universal \(Omega/z\) might remain independent of `k`. However, the file I'm looking at is focused on the ordered bar complex of affine KM at level `k`, and I need to verify this against the DNP dg-shifted Yangian. It feels like there's a lot to unravel in how these elements interconnect!
thinking
**Considering DNP Comparison**

I'm thinking about a patch for the DNP comparison that would involve comparing normalized residues. I wonder if I could define a function like `dnp_r_matrix_genus0(z, k=1)` that returns `k*Omega/z`. But then again, I realize that the DNP Yangian r-matrix might be level-free, so I'm contemplating how that intertwines with my approach. It's interesting to consider how different parameters could affect the outcome!
exec
/bin/zsh -lc "sed -n '330,370p' compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        """For sl_3 shadow expansion: R_2 = Omega^2."""
        coeffs = yang_rmatrix_coefficients('A', 2, max_order=4)
        Omega = slN_casimir(3)
        assert np.allclose(coeffs[2], Omega @ Omega, atol=1e-12)

    def test_typeB_R2_proportional_to_Q(self):
        """For so_{2n+1}: R_k = kappa_R^{k-1} Q for k >= 2."""
        coeffs = yang_rmatrix_coefficients('B', 2, max_order=4)
        N = 5  # so_5
        d = N * N
        Q = np.zeros((d, d), dtype=complex)
        for i in range(N):
            for k in range(N):
                Q[i * N + i, k * N + k] = 1.0
        kappa_R = 2 - 0.5  # n - 1/2 = 1.5
        assert np.allclose(coeffs[2], kappa_R * Q, atol=1e-10)
        assert np.allclose(coeffs[3], kappa_R ** 2 * Q, atol=1e-10)

    def test_typeC_R2_proportional_to_K(self):
        """For sp_{2n}: R_k = -kappa_R^{k-1} K for k >= 2."""


thinking
**Reviewing normalization process**

I'm considering the possible need for level normalization but maybe there's no need to complicate it. Perhaps I can just set k=1 and update report strings to indicate that adjustment. It might get messy, though, so I'm thinking of simply patching the core r-matrix functions and adding necessary tests, while keeping the DNP comparison unchanged with k=1. I’ll inspect theorem_sl3 tests and see if there's anything to address. There’re some potential documentation bugs in theorem_three_way_r_matrix_engine and theorem_virasoro_spectral_r_matrix_engine, too.
thinking
**Planning r-matrix edits**

I see that I might need to include PE-1 commentary before making edits, especially since this involves the r-matrix formulas and is pretty crucial. I'll be focusing on the sl3 r_matrix functions and potentially the Type C docstring, ensuring to provide commentary with PE-1 for the affine KM sl3 trace-form. I need to ensure the exact template is included. It's true that for `_full_rmatrix`, it might not require AP126, but for sl3, PE-1 is definitely necessary.
codex
Pre-edit verification for the affine `sl_3` trace-form writes:

```text
family: [affine KM sl_3]  r(z): [k*Omega/z]  level param: [k]  OPE pole: [2]  r pole: [1]
convention: [trace-form]
AP126 (trace-form): r|_{k=0} = [0]  expected: 0  match? [Y]
AP141 grep: bare \Omega/z in scope: [Y]  allowed? [N for raw affine residue; only normalized Yangian surfaces may stay level-free]
critical-level (KM): r|_{k=-h^v} = [-3*Omega/z for sl_3]
source: [CLAUDE.md HZ-1 / AGENTS.md C9-C11 / compute/lib/rmatrix_landscape.py]
verdict: [ACCEPT]
```

I’m patching the sl\_3 engines to make the raw affine residue level-aware, and patching the Yangian arithmetic engine to stop evaluating exactly at its rational poles while aligning the type `C` docstring with the implemented convention.

thinking
**Planning file edits**

I need to edit some files and determine exactly which lines need changes. For `yangian_rmatrix_sl3.py`, I want to add an optional k to `r_matrix_abstract` and `r_matrix_fund`. I should also update docstrings and comments, maybe including the formula string. It might help to include k in the `full_extraction_report`. I wonder if R_residue_at_zero is relevant. I should search for occurrences of `Omega/z` in the file to see if any updates are needed.
exec
/bin/zsh -lc "rg -n \"Omega/z|k\\*Omega|simple pole of the OPE|double pole|collision residue\" compute/lib/yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5:residue of the MC element, yielding the r-matrix r(z) = k\Omega/z where
12:* r-matrix (collision residue of bar):
330:# r-matrix from bar complex collision residue
334:    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
337:    propagator d\log E(z,w).  The collision residue (AP19) extracts the
338:    simple pole of the OPE: [a, b] (structure constants), NOT the
339:    double pole k g^{ab} (curvature).
358:        "formula": "r(z) = k*Omega / z",
364:    """r-matrix in the fundamental representation: r(z) = k*Omega / z.
742:    The collision residue Res^{coll}_{0,2}(\Theta_A) = r(z) is a consequence.
778:    This is the collision residue of the bar construction: the
867:        "r_matrix_formula": "r(z) = k*Omega/z where Omega = P - I/3",

thinking
**Updating lines in code**

I realize I need to update lines 337-339 because they’re incorrect. It’s important to ensure the accuracy of my code, so I'll make sure to take a close look at those lines. I’m also thinking about searching around lines 742 and 778, as they might contain relevant information to help me with these updates. It feels like a step in the right direction, so I’ll dive in and figure it out!
exec
/bin/zsh -lc "sed -n '730,790p' compute/lib/yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    diff = R @ P_asym - (z - 1) * P_asym
    return float(np.linalg.norm(diff))


# ============================================================
# Bar complex d^2 = 0 implies YBE
# ============================================================

def bar_d_squared_implies_ybe() -> Dict[str, object]:
    r"""Conceptual verification: d^2 = 0 on the bar complex implies YBE.

    The bar complex differential D satisfies D^2 = 0 (proved: thm:convolution-d-squared-zero).
    The collision residue Res^{coll}_{0,2}(\Theta_A) = r(z) is a consequence.
    The YBE for r(z) (and hence R(z)) is a formal consequence of D^2 = 0
    applied to the arity-3 component of the MC equation.

    This is NOT an independent proof of YBE; it is a STRUCTURAL EXPLANATION
    of WHY the Yang-Baxter equation holds: it is the arity-3 projection
    of the Maurer-Cartan equation D\Theta + (1/2)[\Theta, \Theta] = 0.


thinking
**Evaluating documentation issues**

I'm noticing some potential errors in the documentation for R_residue_at_zero. It seems like it might be misrepresenting "collision residue" when it should refer to the residue of the normalized Yang R. I could consider making a patch since the raw collision residue is kΩ, not P. I’ll also look into correcting the documentation and checking for mistakes in the `theorem_sl3_yangian_r_matrix_engine.py` file. This could lead to improvements!
exec
/bin/zsh -lc "rg -n \"Omega/z|k\\*Omega|simple pole|double pole|collision residue|R\\(z\\) = I \\+ P/z|R\\(z\\) = u I \\+ P|KZ Hamiltonians\" compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
12:  (2) Constructing the multi-point KZ Hamiltonians and verifying their
30:  * The collision residue (AP19): r(z) = Omega/z where Omega is the
43:  * KZ Hamiltonians for n points in representation V:
52:  * Classical Yang--Baxter equation for r(z) = Omega/z:
63:        DNP r(z) = Omega/z = MK bar collision residue.
336:# R-matrix from bar collision residue
342:    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
423:    r"""Verify the CYBE for r(z) = Omega/z in representation of dim N.
465:# KZ Hamiltonians and infinitesimal braid relations (IBR)
702:        r^{DNP}(z) = Omega/z
703:    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
712:    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
727:        "r_MK": "Omega/z (bar collision residue)",
728:        "r_DNP": "Omega/z (A_infty structure on A^!)",

thinking
**Evaluating the KZ Hamiltonian**

I see that this file definitely needs a patch, and I should inspect the functions and tests. I'm curious about the r_matrix_fund and the KZ Hamiltonian, which seems to use 1/kappa, but I wonder if it should actually use 1/(k+h^\vee). The introduction references H_i=(1/kappa) sum Ω/(z_i-z_j), which appears incorrect. It looks like the KZ coefficient should follow the same structure. I need to dive deeper into the implementation. Time to search for `kz_hamiltonian`.
exec
/bin/zsh -lc "sed -n '460,560p' compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"1/kappa|1 / kappa|1/\\(k\\+|1 / \\(k\\+|k\\+3|kappa\" compute/lib/theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    comm = O12 @ (O13 + O23) - (O13 + O23) @ O12
    return float(np.linalg.norm(comm))


# ============================================================
# KZ Hamiltonians and infinitesimal braid relations (IBR)
# ============================================================

def _omega_ij(n: int, i: int, j: int, Omega_2: np.ndarray, dim_rep: int) -> np.ndarray:
    r"""Casimir tensor Omega_{ij} embedded in V^{otimes n}.

    Places the 2-body Casimir Omega in the (i,j) slots of the
    n-fold tensor product, with identity in all other slots.
    """
    d = dim_rep
    result = np.zeros((d ** n, d ** n), dtype=complex)

    for idx_row in np.ndindex(*([d] * n)):
        for idx_col in np.ndindex(*([d] * n)):
            match = True
 succeeded in 51ms:
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:26:    - landscape_census.tex: kappa(sl_3_k) = 4(k+3)/3.
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:37:    kappa_sl3,
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:380:        kv = float(kappa_sl3(1))
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:387:        kv = float(kappa_sl3(2))
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:396:        kv = float(kappa_sl3(1))
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:400:    def test_kz_kappa_independence(self):
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:401:        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:404:            kv = float(kappa_sl3(k))
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:606:    """Kappa formula kappa(sl_3_k) = 4(k+3)/3."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:608:    def test_kappa_k1(self):
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:609:        assert kappa_sl3(1) == Rational(16, 3)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:611:    def test_kappa_k0(self):
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:612:        assert kappa_sl3(0) == Rational(4)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:614:    def test_kappa_critical(self):
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:615:        """At critical level k = -h^vee = -3: kappa = 0."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:616:        assert kappa_sl3(-3) == 0
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:618:    def test_kappa_ff_duality(self):
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:619:        """Feigin-Frenkel: kappa(k) + kappa(-k - 2h^vee) = 0."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:622:        assert kappa_sl3(k) + kappa_sl3(k_dual) == 0
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:657:    def test_kappa_matches(self):

thinking
**Verifying KZ Hamiltonian**

I'm noticing that the KZ Hamiltonian uses 1/kappa in both the documentation and the implementation, which seems potentially incorrect. I need to double-check this by looking at the repository. Also, in the theorem_three_way_r_matrix_engine, KZ appears to use 1/(k+h^v). It's worth searching for more information on that to ensure clarity and accuracy. I want to make sure everything lines up and that I'm not missing something crucial here.
exec
/bin/zsh -lc "rg -n \"KZ Hamiltonian|1/\\(k \\+|1/\\(k\\+|1 / \\(k \\+|1 / \\(k\\+|kappa\" compute/lib/theorem_three_way_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
45:    GZ26: H_i = (1/(k + h^v)) sum_{j != i} Omega_{ij} / z_{ij}.
116:def kappa_heisenberg(k: Fraction) -> Fraction:
117:    r"""kappa(H_k) = k."""
121:def kappa_affine_sl2(k: Fraction) -> Fraction:
122:    r"""kappa(sl_2, k) = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4."""
126:def kappa_virasoro(c: Fraction) -> Fraction:
127:    r"""kappa(Vir_c) = c/2.  WARNING (AP48): specific to Virasoro."""
131:def kappa_w3(c: Fraction) -> Fraction:
132:    r"""kappa(W_3) = c * (H_3 - 1) where H_3 = 1 + 1/2 + 1/3 = 11/6.
134:    So kappa(W_3) = c * (11/6 - 1) = c * 5/6.
189:        The prefactor is 1/(k + h^v) = 1/(k + 2).
393:        The normalization 1/(k + h^v) comes from the KZ equation, which
394:        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
397:        which includes the 1/(k + h^v) factor from the bar normalization.
654:        KZ Hamiltonian: H_i = (1/(k + h^v)) sum_{j != i} Omega_{ij} / z_{ij}.
694:        r"""Verify [H_i, H_j] = 0 for KZ Hamiltonians (consistency check).
1140:    r"""Verify that the KZ Hamiltonians built from r(z) = Omega/((k+2)z) commute.



thinking
**Identifying potential bugs**

I’m noticing that the theorem_sl3 engine using 1/kappa likely has a bug! It seems tests aren’t catching this because commutativity is scale-invariant. We need to fix this to use `k_plus_hvee` or potentially rename the parameter. This is a significant finding. I could patch the file and add tests to ensure the coefficient matches the canonical \(1/(k+3)\) instead of \(1/\kappa\). Additionally, the KZ Hamiltonian and rescaling could be more important than r_matrix scaling. I'll have to dig into `yangian_rmatrix_sl3.py` as it seems to use a potentially flawed representation.
thinking
**Planning patches for improvements**

I think I might have a clearer path for the patch set. 

In `theorem_sl3_yangian_r_matrix_engine.py`, I need to modify the raw r-matrix to accept level `k` and return `kΩ/z`. I also want to adjust the KZ Hamiltonian normalization to `1/(k+h^vee)` instead of `1/kappa` while adding some tests for k=0 vanishing, linear scaling, and ensuring KZ normalization matches `1/(k+3)` in a simple example.

For `yangian_rmatrix_sl3.py`, I plan to fix the raw bar collision residue helpers and clarify the documentation regarding poles. Then in `yangian_rmatrix_arithmetic_engine.py`, I need to address some sign mismatches and add tests to suppress warnings. I might not need to patch the theorem_sl3 DNP comparison if the default for `r_matrix_fund` is working properly.
thinking
**Updating documentation and reports**

I notice that the file introduction and documentation still refer to `Omega/z`. Since we’re patching the raw r-matrix to `kΩ/z`, we definitely need to update those docs and any report strings. It’d make clarity a lot better for users. I should also rephrase the DNP comparison to mention it is "after unit-level normalization." This will help keep everything aligned and consistent, which is super important to avoid confusion later on!
exec
/bin/zsh -lc "sed -n '800,870p' compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
def spectral_decomposition_fund() -> Dict[str, object]:
    r"""Spectral decomposition of R(z) = z I + P on C^3 otimes C^3.

    3 x 3 = Sym^2(3) + Lambda^2(3) = 6 + 3*.
    P|_{Sym} = +1, P|_{Lambda} = -1.
    R|_{Sym} = z+1, R|_{Lambda} = z-1.
    Omega|_{Sym} = 2/3, Omega|_{Lambda} = -4/3.
    """
    P = permutation_matrix(FUND_DIM)
    I = np.eye(FUND_DIM ** 2)
    P_sym = (I + P) / 2
    P_asym = (I - P) / 2
    Omega = casimir_tensor_fund()

    c2_sym = np.trace(Omega @ P_sym).real / np.trace(P_sym).real
    c2_asym = np.trace(Omega @ P_asym).real / np.trace(P_asym).real

    return {
        "sym_dim": int(np.trace(P_sym).real),
        "asym_dim": int(np.trace(P_asym).real),
exec
/bin/zsh -lc "sed -n '360,430p' compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    def test_cybe_adj(self):
        """CYBE in the adjoint representation (64x64 Casimir)."""
        Omega = casimir_tensor_adj()
        assert verify_cybe(Omega, ADJ_DIM, 1.5, 2.7) < 1e-10

    def test_cybe_adj_complex(self):
        Omega = casimir_tensor_adj()
        assert verify_cybe(Omega, ADJ_DIM, 1.0 + 0.5j, 2.0 - 0.3j) < 1e-10


# ============================================================
# 8. KZ commutativity / IBR
# ============================================================

class TestKZCommutativity:
    """Infinitesimal braid relations: [H_i, H_j] = 0."""

    def test_kz_n3_fund(self):
        """KZ commutativity at 3 points, fundamental rep."""
        Omega = casimir_tensor_fund()
exec
/bin/zsh -lc "sed -n '220,270p' compute/tests/test_yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# 3. r-matrix pole structure (AP19)
# ============================================================

class TestRMatrixPoleStructure:
    """Verify the r-matrix has the correct pole structure (AP19)."""

    def test_single_pole(self):
        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
        info = r_matrix_abstract()
        assert info["pole_order"] == 1

    def test_residue_is_omega(self):
        """Residue of r(z) at z = 0 is Omega = P - I/3."""
        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
        Omega = casimir_tensor_fund()
        P = permutation_matrix_3()
        I9 = np.eye(9)
        assert np.allclose(Omega, P - I9 / 3, atol=1e-10)

    def test_ope_pole_orders_vs_rmatrix(self):

thinking
**Updating test documentation**

I need to update the test docstrings to reflect `k*Omega/z`. That's a good step forward! I'm also considering patching the `yangian_rmatrix_arithmetic_engine.py` tests since previous warnings might disappear without altering the tests themselves. However, I might want to add a new test as well. I'll search for reference lines related to `_full_rmatrix` starting from line 887 and inspect them closely. Let's see what I can find there!
exec
/bin/zsh -lc "sed -n '880,930p' compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# =========================================================================

class TestSpecificValues:
    """Regression tests for specific computed values."""

    def test_sl2_yang_rmatrix_at_u3(self):
        """R(3) = 3I + P for sl_2 is a specific 4x4 matrix."""
        R = _full_rmatrix('A', 1, 3.0)
        P = _permutation_matrix(2)
        I4 = _identity_tensor(2)
        expected = 3.0 * I4 + P
        assert np.allclose(R, expected)

    def test_so5_rmatrix_trace(self):
        """tr(R(5.0)) for so_5 should have a specific value."""
        R = _full_rmatrix('B', 2, 5.0)
        tr = np.trace(R)
        # R(u) = I - P/u + Q/(u - 3/2) for so_5 (kappa_R = 2 - 1/2 = 3/2)
        # tr(I) = 25, tr(P) = 5, tr(Q) = 5
        # tr(R(5)) = 25 - 5/5 + 5/(5-1.5) = 25 - 1 + 5/3.5 = 24 + 10/7
exec
/bin/zsh -lc "rg -n \"\\['test_params'\\]|test_params\" compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Considering updates to functions**

I'm thinking about updating `full_report` since there don't seem to be many callers. That's good! I should search for `r_matrix_adj` as it appears to be used only in tests. It might be beneficial to add an optional parameter `k` to both functions. This could enhance their flexibility. Overall, it sounds like optimizing these functions would improve the code without affecting too many existing parts.
codex
I’ve isolated three concrete fixes worth landing: two sl\_3 engine inconsistencies on the raw affine residue/KZ normalization, and one Yangian arithmetic warning surface caused by evaluating exactly at rational poles. I’m editing only those engine/test files now.

thinking
**Inspecting patch sections**

I need to focus on preparing smaller patches. I should carefully inspect the exact sections in the test_theorem_sl3 code. It's crucial to search thoroughly around the relevant parts to ensure everything is accurate. I want to be meticulous to avoid any mistakes that could lead to issues later on. Let's make sure we're targeting the right areas for the patch!
codex
The patch partly missed current file context. I’m reopening the exact sections and reapplying as surgical hunks so I don’t touch unrelated surface.
exec
/bin/zsh -lc "sed -n '930,980p' compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,720p' compute/tests/test_yangian_rmatrix_arithmetic_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,330p' compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    """Cross-family and cross-method consistency checks."""

    def test_typeBC_isomorphism_rank2(self):
        """so_5 = sp_4 as Lie algebras: dim(g) and h^vee should match."""
        data_B = lie_algebra_data('B', 2)
        data_C = lie_algebra_data('C', 2)
        assert data_B['dim_g'] == data_C['dim_g']
        assert data_B['dual_coxeter'] == data_C['dual_coxeter']

    def test_kappa_additivity_heisenberg(self):
        """For direct sums: kappa is additive.  Check for sl_2 + sl_2."""
        k1 = modular_characteristic('A', 1, 1.0)
        # kappa(sl_2 + sl_2) should be 2 * kappa(sl_2) if levels match.
        assert abs(2 * k1 - 2 * 9.0 / 4) < 1e-12

    def test_ybe_and_cybe_consistency(self):
        """If CYBE holds, YBE should also hold (YBE is quantization of CYBE)."""
        for lie_type, n in [('A', 1), ('A', 2), ('B', 2), ('C', 2)]:
            cybe = verify_cybe(lie_type, n)
            ybe = ybe_coefficient_relations(lie_type, n, 4)
 succeeded in 52ms:
        ev = adjoint_casimir_eigenvalues()
        expected_evals = [-6.0, -3.0, 0.0, 2.0]
        expected_mults = [1, 16, 20, 27]
        assert len(ev["eigenvalues"]) == 4
        for e_exp, m_exp, e_got, m_got in zip(
                expected_evals, expected_mults,
                ev["eigenvalues"], ev["multiplicities"]):
            assert abs(e_got - e_exp) < 0.5, f"Expected eigenvalue {e_exp}, got {e_got}"
            assert m_got == m_exp, f"Expected mult {m_exp}, got {m_got}"
        assert ev["total_dim"] == 64


# ============================================================
# 5. r-matrix pole structure (AP19)
# ============================================================

class TestRMatrixPoleStructure:
    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""

    def test_single_pole_fund(self):
 succeeded in 52ms:
        assert abs(R[0, 0] - q) < 1e-12
        assert abs(R[3, 3] - q) < 1e-12
        assert abs(R[1, 1] - 1.0) < 1e-12
        assert abs(R[2, 2] - 1.0) < 1e-12
        assert abs(R[1, 2] - (q - 1.0 / q)) < 1e-12

    def test_jimbo_ybe(self):
        """Jimbo R-matrix satisfies the quantum Yang-Baxter equation.

        QYBE: R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}
        (using the constant R-matrix, with proper 3-fold embeddings).
        """
        q = np.exp(2j * np.pi / 5)
        R = trigonometric_rmatrix_sl2(q)
        N = 2
        # Proper embeddings into V^{tensor 3}
        R12 = _embed_12(R, N)
        R23 = _embed_23(R, N)
        R13 = _embed_13(R, N)
        lhs = R12 @ R13 @ R23

thinking
**Patching files cautiously**

I need to patch everything carefully, but first, I should check for any import warnings. It seems there aren't any warnings at the moment. Now, I’ll start patching the files one by one, beginning with `compute/lib/yangian_rmatrix_sl3.py`. I'm making sure to take it step by step to avoid any issues. Being meticulous here is key!
file update
M /Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_sl3.py
@@ -332,12 +332,12 @@
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
@@ -358,2 +358,3 @@
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
@@ -362,3 +363,3 @@
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
@@ -367,2 +368,3 @@
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
@@ -372,3 +374,3 @@
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
@@ -777,4 +779,4 @@
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_sl3.py
file update:
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 

file update:
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 

file update
M /Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_sl3.py
@@ -226,3 +226,3 @@
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
@@ -231,4 +231,3 @@
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
@@ -249,2 +248,13 @@
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
apply_patch(auto_approved=true) exited 0 in 27ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_sl3.py
file update:
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update:
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)


thinking
**Patching the engine**

I need to patch the theorem_sl3 engine and carefully inspect some specific lines to make sure everything's working as it should. I want to ensure that I apply the patch correctly and avoid any mistakes that could lead to issues down the line. It's crucial to be precise in this process, as even small errors can have significant consequences. I'll take my time with this to get it right!
file update
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -29,5 +29,6 @@
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
@@ -43,3 +44,3 @@
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
@@ -62,3 +63,4 @@
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
@@ -338,13 +340,14 @@
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
@@ -353,3 +356,3 @@
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
@@ -502,6 +505,6 @@
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
@@ -517,3 +520,3 @@
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
@@ -522,3 +525,3 @@
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
@@ -531,3 +534,3 @@
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
@@ -697,13 +700,12 @@
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
@@ -711,3 +713,3 @@
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
@@ -716,4 +718,4 @@
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
@@ -726,4 +728,4 @@
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
@@ -843,5 +845,5 @@
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
apply_patch(auto_approved=true) exited 0 in 29ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update
M /Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -276,6 +276,6 @@
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
@@ -284,2 +284,13 @@
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
@@ -296,3 +307,3 @@
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
@@ -379,3 +390,3 @@
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
@@ -386,3 +397,3 @@
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
@@ -395,3 +406,3 @@
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
@@ -399,7 +410,7 @@
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
@@ -407,2 +418,10 @@
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)


thinking
**Inspecting patch details**

I'm looking into patching the arithmetic engine and tests. I might need to check the import block to see if there's a need for warnings. It's probably crucial to ensure everything runs smoothly! I think I'll use the apply_patch function for this process. I'll make sure to double-check my steps to avoid any oversights. Let's keep track of the details carefully as I move forward with this patching process!
file update
M /Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -804,3 +804,3 @@
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
@@ -808,2 +808,8 @@
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
@@ -845,2 +851,17 @@
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
@@ -850,3 +871,3 @@
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
M /Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -19,2 +19,3 @@
 import math
+import warnings
 
@@ -954,2 +955,13 @@
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_arithmetic_engine.py
M /Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

exec
/bin/zsh -lc "rg -n \"r\\(z\\) = \\\\sum_a T\\"'^a|r'"\\(z\\) = Omega/z|r\\(z\\) = k\\\\Omega/z|simple pole of the OPE|double pole\" compute/lib/yangian_rmatrix_sl3.py compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:r\(z\) = \sum_a T\^a|r\(z\) = Omega/z|r\(z\) = k\Omega/z|simple pole of the OPE|double pole)
                                                       ^^
error: unrecognized escape sequence
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

exec
/bin/zsh -lc "sed -n '1,40p' compute/lib/yangian_rmatrix_sl3.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,70p' compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "r(z) = Omega/z" compute/lib/yangian_rmatrix_sl3.py compute/lib/theorem_sl3_yangian_r_matrix_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"r(z) = k\\\\Omega/z\" compute/lib/yangian_rmatrix_sl3.py compute/lib/theorem_sl3_yangian_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Yangian R-matrix from the bar complex for sl_3 --- first non-sl_2 extraction.

Extracts R(z) = Res^{coll}_{0,2}(\Theta_A) for the sl_3 affine Kac--Moody
algebra at level k. The bar propagator d\log E(z,w) extracts the collision
residue of the MC element, yielding the r-matrix r(z) = k\Omega/z where
\Omega is the quadratic Casimir tensor in sl_3 \otimes sl_3 (AP19: one pole
order below the OPE).

Mathematical structure
---------------------
* OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
* r-matrix (collision residue of bar):
      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
  This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
* R-matrix (perturbative in 1/\kappa):
      R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
  where \kappa = 4(k+3)/3 = dim(sl_3)(k+h^\vee)/(2 h^\vee).
* In the fundamental representation (V = C^3):
      R^{fund}(z) = I + P/z   (Yang R-matrix, at leading order)
  where P is the permutation operator on V \otimes V.
 succeeded in 51ms:
r"""sl_3 Yangian R-matrix from the ordered bar complex — first rank-2 extraction.

Extracts R(z) from the ordered bar complex of the affine Kac--Moody algebra
\widehat{sl}_3 at level k and verifies it against the Dimofte--Niu--Py (DNP)
dg-shifted Yangian construction.

This engine goes beyond the existing yangian_rmatrix_sl3.py by:

  (1) Computing the Casimir tensor in BOTH the fundamental (dim 3) and
      adjoint (dim 8) representations of sl_3.

  (2) Constructing the multi-point KZ Hamiltonians and verifying their
      commutativity (the infinitesimal braid relations, IBR).

  (3) Computing Verlinde fusion rules for sl_3 at small levels k = 1, 2, 3.

  (4) Comparing with the DNP dg-shifted Yangian construction:
      DNP r(z) = MK Res^{coll}_{0,2}(Theta_A) at genus 0.

Mathematical content
 succeeded in 50ms:
compute/lib/yangian_rmatrix_sl3.py:5:residue of the MC element, yielding the r-matrix r(z) = k\Omega/z where
 succeeded in 51ms:
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:53:  * Classical Yang--Baxter equation for r(z) = Omega/z:
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:64:        DNP r(z) = Omega/z in unit-level normalization.
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:426:    r"""Verify the CYBE for r(z) = Omega/z in representation of dim N.
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..8ec0ec2ef59267ae2b663058635f1687029b7214
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -330,16 +330,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +356,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +777,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update
M /Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_sl3.py
@@ -12,3 +12,4 @@
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_sl3.py
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

codex
The main code edits are in place. I’m running the narrow pytest slices for the touched r-matrix files now to verify both the new level-aware checks and the warning suppression.
exec
/bin/zsh -lc 'pytest -q compute/tests/test_yangian_rmatrix_sl3.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

 succeeded in 1.95s:
........................................................................ [ 20%]
........................................................................ [ 41%]
........................................................................ [ 62%]
........................................................................ [ 82%]
...........................................................              [100%]
347 passed in 1.64s
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)


thinking
**Evaluating test strategy**

I’m considering whether I need to rerun the broader rmatrix suite. I could run a full earlier slice to ensure there are no regressions. Since the changes were localized, it might suffice to run main related tests from earlier, specifically 1117. But just to be cautious, I’m thinking about running a smaller broader slice that includes tests like rmatrix_landscape, theorem_pva_classical, and others. Let's aim to run that same earlier big list to be thorough!
codex
The focused slices are green. I’m widening once across the broader r-matrix suite to make sure the sl\_3 and arithmetic fixes didn’t disturb any wrapper surfaces or downstream comparisons.
exec
/bin/zsh -lc 'pytest -q compute/tests/test_rmatrix_landscape.py compute/tests/test_theorem_pva_classical_r_matrix_engine.py compute/tests/test_quantum_rmatrix_barcomplex.py compute/tests/test_belavin_rmatrix_verification_engine.py compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py compute/tests/test_theorem_three_way_r_matrix_engine.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py compute/tests/test_yangian_rmatrix_sl3.py compute/tests/test_elliptic_rmatrix_shadow.py compute/tests/test_rmatrix_comparison_c3.py compute/tests/test_rmatrix_poles_comprehensive.py' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

 succeeded in 4.43s:
........................................................................ [  6%]
........................................................................ [ 12%]
........................................................................ [ 19%]
........................................................................ [ 25%]
........................................................................ [ 32%]
........................................................................ [ 38%]
........................................................................ [ 44%]
........................................................................ [ 51%]
........................................................................ [ 57%]
........................................................................ [ 64%]
........................................................................ [ 70%]
........................................................................ [ 76%]
........................................................................ [ 83%]
........................................................................ [ 89%]
........................................................................ [ 96%]
...........................................                              [100%]
1123 passed in 3.76s

thinking
**Inspecting code changes**

I need to inspect the git diff to summarize the exact edits and line numbers. Including file line references from the updated files seems important too. I think using "nl -ba" could help me get the line numbers. I might also want a summary of the git diff. So, the plan is to check out the relevant file diffs and gather all the necessary details for clarity.
exec
/bin/zsh -lc 'git diff -- compute/lib/yangian_rmatrix_sl3.py compute/tests/test_yangian_rmatrix_sl3.py compute/lib/theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py compute/lib/yangian_rmatrix_arithmetic_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_yangian_rmatrix_sl3.py | sed -n '223,270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py | sed -n '272,320p'; nl -ba compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py | sed -n '374,422p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/yangian_rmatrix_sl3.py | sed -n '1,30p'; nl -ba compute/lib/yangian_rmatrix_sl3.py | sed -n '333,380p'; nl -ba compute/lib/yangian_rmatrix_sl3.py | sed -n '774,785p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/yangian_rmatrix_arithmetic_engine.py | sed -n '800,890p'; nl -ba compute/tests/test_yangian_rmatrix_arithmetic_engine.py | sed -n '1,20p'; nl -ba compute/tests/test_yangian_rmatrix_arithmetic_engine.py | sed -n '930,970p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_sl3_yangian_r_matrix_engine.py | sed -n '20,60p'; nl -ba compute/lib/theorem_sl3_yangian_r_matrix_engine.py | sed -n '336,360p'; nl -ba compute/lib/theorem_sl3_yangian_r_matrix_engine.py | sed -n '500,535p'; nl -ba compute/lib/theorem_sl3_yangian_r_matrix_engine.py | sed -n '698,731p'; nl -ba compute/lib/theorem_sl3_yangian_r_matrix_engine.py | sed -n '830,848p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d..d0b31b9 100644
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@ For A = sl_3-hat_k at level k:
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@ For A = sl_3-hat_k at level k:
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 succeeded in 50ms:
   223	class TestRMatrixPoleStructure:
   224	    """Verify the r-matrix has the correct pole structure (AP19)."""
   225	
   226	    def test_single_pole(self):
   227	        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
   228	        info = r_matrix_abstract()
   229	        assert info["pole_order"] == 1
   230	
   231	    def test_residue_is_omega(self):
   232	        """Residue of the unit-level r-matrix is Omega = P - I/3."""
   233	        Omega = casimir_tensor_fund()
   234	        P = permutation_matrix_3()
   235	        I9 = np.eye(9)
   236	        assert np.allclose(Omega, P - I9 / 3, atol=1e-10)
   237	
   238	    def test_ope_pole_orders_vs_rmatrix(self):
   239	        """OPE has poles z^{-2} (curvature) and z^{-1} (bracket).
   240	        Bar propagator d log absorbs one power: r-matrix has z^{-1} only.
   241	        This is AP19: r-matrix poles are one order below OPE poles."""
   242	        # The OPE: J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c/(z-w)
 succeeded in 50ms:
     1	r"""Yangian R-matrix from the bar complex for sl_3 --- first non-sl_2 extraction.
     2	
     3	Extracts R(z) = Res^{coll}_{0,2}(\Theta_A) for the sl_3 affine Kac--Moody
     4	algebra at level k. The bar propagator d\log E(z,w) extracts the collision
     5	residue of the MC element, yielding the r-matrix r(z) = k\Omega/z where
     6	\Omega is the quadratic Casimir tensor in sl_3 \otimes sl_3 (AP19: one pole
     7	order below the OPE).
     8	
     9	Mathematical structure
    10	---------------------
    11	* OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
    12	* r-matrix (collision residue of bar):
    13	      r(z) = k * \sum_a T^a \otimes T_a / z
    14	  in  sl_3 \otimes sl_3 \otimes C((z))
    15	  This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
    16	* R-matrix (perturbative in 1/\kappa):
    17	      R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
    18	  where \kappa = 4(k+3)/3 = dim(sl_3)(k+h^\vee)/(2 h^\vee).
    19	* In the fundamental representation (V = C^3):
    20	      R^{fund}(z) = I + P/z   (Yang R-matrix, at leading order)
 succeeded in 50ms:
   800	            if a + b == 0:
   801	                continue  # trivial
   802	            residuals[(a, b)] = 0.0  # Will be filled by numerical check
   803	
   804	    # Numerical verification at many parameter points
   805	    candidate_params = [
   806	        (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
   807	        (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
   808	    ]
   809	    test_params = [
   810	        (u, v) for u, v in candidate_params
   811	        if not _full_rmatrix_hits_pole(lie_type, n, u)
   812	        and not _full_rmatrix_hits_pole(lie_type, n, v)
   813	        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
   814	    ]
   815	
   816	    ybe_errors = []
   817	    for u, v in test_params:
   818	        try:
   819	            err = _ybe_numerical_error(lie_type, n, u, v)
 succeeded in 51ms:
   272	# ============================================================
   273	# 5. r-matrix pole structure (AP19)
   274	# ============================================================
   275	
   276	class TestRMatrixPoleStructure:
   277	    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
   278	
   279	    def test_single_pole_fund(self):
   280	        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
   281	        r = r_matrix_fund(1.0)
   282	        Omega = casimir_tensor_fund()
   283	        assert np.allclose(r, Omega, atol=1e-14)
   284	
   285	    def test_k0_vanishes(self):
   286	        """AP126/AP141: the raw affine residue vanishes at k=0."""
   287	        r = r_matrix_fund(1.0, k=0)
   288	        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
   289	
   290	    def test_scales_linearly_with_level(self):
   291	        """Trace-form raw residue scales linearly in k."""
 succeeded in 51ms:
    20	Mathematical content
    21	--------------------
    22	
    23	For A = sl_3-hat_k at level k:
    24	
    25	  * h^vee(sl_3) = 3, dim(sl_3) = 8, rank = 2.
    26	  * kappa(sl_3_k) = dim(g)(k + h^vee) / (2 h^vee) = 4(k+3)/3.
    27	  * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
    28	    at hbar = 1/(k+3).
    29	
    30	  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
    31	    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
    32	    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
    33	    term becomes regular and drops.
    34	
    35	  * Casimir identity on the fundamental V = C^3:
    36	        Omega = P - (1/N) I,  N = 3
    37	    where P is the permutation operator.
    38	
    39	  * Casimir tensor on the adjoint (dim 8):
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)


thinking
**Reviewing git changes**

I’m thinking about getting the git diff for theorem_sl3 tests, focusing on the line numbers — that might be enough to track the changes. I should also check if there are any uncommitted changes by the user in those files. For that, it seems prudent to run `git status --short` to limit the output to just the touched files. This way, I can keep things concise and clear while understanding the current state.
exec
/bin/zsh -lc 'git status --short -- compute/lib/yangian_rmatrix_sl3.py compute/tests/test_yangian_rmatrix_sl3.py compute/lib/theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py compute/lib/yangian_rmatrix_arithmetic_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 M compute/lib/theorem_sl3_yangian_r_matrix_engine.py
 M compute/lib/yangian_rmatrix_arithmetic_engine.py
 M compute/lib/yangian_rmatrix_sl3.py
 M compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
 M compute/tests/test_yangian_rmatrix_arithmetic_engine.py
 M compute/tests/test_yangian_rmatrix_sl3.py
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)



thinking
**Running grep for findings**

I need to run a search for occurrences of `Omega/z` in the touched files, especially in `compute/lib/theorem_sl3_yangian_r_matrix_engine.py`. It might still have some instances due to unit normalization, which is fine, but I want to ensure accuracy. I need to collect findings and present them clearly, detailing the problem stated at each file and line, followed by the exact edit made. I should mention the tests I've run as well. I'll format the findings into a bullet list with absolute file links.
thinking
**Detailing exact findings**

I need to ensure I have the precise line numbers after the patch. I'll reference the line numbers from the `nl` command. For each finding, the first issue looks like it’s at `compute/lib/yangian_rmatrix_sl3.py:334-376`. I should clarify: PROBLEM at [compute/lib/yangian_rmatrix_sl3.py](/abs...:334) — it spoke about modeling \(k\Omega/z\) but returned a level-free version. I did an exact edit by adding an optional `k` parameter and updating the explanation accordingly. Then there's the second issue, potentially at `theorem_sl3_yangian_r_matrix_engine.py:30 and 504`, requiring separate mention.
codex
**Findings**
- PROBLEM at [compute/lib/yangian_rmatrix_sl3.py](/Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_sl3.py:334): the raw affine `sl_3` residue surface claimed `r(z)=k*Omega/z`, but `r_matrix_fund` actually returned level-free `Omega/z`, and the AP19 prose inverted which OPE term survives. EXACT edit applied: `r_matrix_abstract` and `r_matrix_fund` now take an optional `k` and return/store the trace-form residue `k*Omega/z`; the AP19 explanation now says the double pole contributes and the bracket term drops; the `R_residue_at_zero` doc was narrowed to the normalized Yang `R` only. Regression checks were added at [compute/tests/test_yangian_rmatrix_sl3.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_sl3.py:249) for `k=0` vanishing and linear-in-`k` scaling.

- PROBLEM at [compute/lib/theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sl3_yangian_r_matrix_engine.py:341): the theorem-level `sl_3` engine had the same raw-residue drift, implementing `Omega/z` while presenting an affine level-`k` surface. EXACT edit applied: `r_matrix_fund` and `r_matrix_adj` now accept `k` and return `k*Omega/z`; the top-level mathematical description and the DNP comparison surface were updated to use matched level normalization. Regression checks were added at [compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:285).

- PROBLEM at [compute/lib/theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/theorem_sl3_yangian_r_matrix_engine.py:504): the KZ Hamiltonian was divided by `kappa` instead of the canonical KZ denominator `k+h^vee`; commutativity still held, so the bug was masked by scale-invariant tests. EXACT edit applied: the parameter was renamed to `level_shift`, the formula/docstring now use `1/(k+h^vee)`, and `full_report` now passes `k + H_VEE` instead of `kappa`. A direct normalization test was added at [compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:419).

- PROBLEM at [compute/lib/yangian_rmatrix_arithmetic_engine.py](/Users/raeez/chiral-bar-cobar/compute/lib/yangian_rmatrix_arithmetic_engine.py:805): the YBE parameter sweep hit exact type `B/C` rational poles, causing runtime warnings, and the type `C` `_full_rmatrix` docstring advertised the wrong denominator sign. EXACT edit applied: added `_full_rmatrix_hits_pole()` and filtered the numerical YBE test points before evaluation; corrected the type `C` docstring from `u + kappa_R` to `u - kappa_R`. A no-warning regression was added at [compute/tests/test_yangian_rmatrix_arithmetic_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rmatrix_arithmetic_engine.py:956).

Verification: `pytest -q compute/tests/test_yangian_rmatrix_sl3.py compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py compute/tests/test_yangian_rmatrix_arithmetic_engine.py` and the wider r-matrix suite both passed; final wide sweep: `1123 passed`.
file update:
diff --git a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
index 48fe89d92c562b51074aa75bc28e1f59a9f384e3..d0b31b9eef760e962354b4040b065a0644ea4400
--- a/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/lib/theorem_sl3_yangian_r_matrix_engine.py
@@ -27,9 +27,10 @@
   * The ordered bar cohomology algebra is A^!_{line} = Y_hbar(sl_3)
     at hbar = 1/(k+3).
 
-  * The collision residue (AP19): r(z) = Omega/z where Omega is the
-    quadratic Casimir tensor.  The d log propagator absorbs one pole
-    order from the OPE: z^{-2} -> z^{-1}.
+  * The raw affine collision residue (AP19) is r(z) = k*Omega/z where
+    Omega is the quadratic Casimir tensor.  The d log propagator absorbs
+    one pole order from the OPE: z^{-2} -> z^{-1}; the z^{-1} bracket
+    term becomes regular and drops.
 
   * Casimir identity on the fundamental V = C^3:
         Omega = P - (1/N) I,  N = 3
@@ -41,7 +42,7 @@
     Omega eigenvalues: 2 (x27), 0 (x20), -3 (x16), -6 (x1).
 
   * KZ Hamiltonians for n points in representation V:
-        H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+        H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
     satisfy [H_i, H_j] = 0  (infinitesimal braid relations, IBR).
     This follows from the Casimir identity [Omega_{12}, Omega_{13}+Omega_{23}] = 0.
 
@@ -60,7 +61,8 @@
     At level 3: 10 integrable reps, 3 x 3 = 6 + 3*.
 
   * DNP comparison: for pure gauge (sl_3, CS level k):
-        DNP r(z) = Omega/z = MK bar collision residue.
+        DNP r(z) = Omega/z in unit-level normalization.
+        The raw affine collision residue is k*Omega/z.
         DNP A_infty YBE reduces to CYBE (no higher operations for KM).
         DNP non-renormalization = MK E_2-collapse = Koszulness of sl_3-hat_k.
 
@@ -336,22 +338,23 @@
 # R-matrix from bar collision residue
 # ============================================================
 
-def r_matrix_fund(z: complex) -> np.ndarray:
-    r"""r-matrix in the fundamental: r(z) = Omega^{fund}/z.
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the fundamental: r(z) = k*Omega^{fund}/z.
 
-    The bar collision residue Res^{coll}_{0,2}(Theta_A) = Omega/z.
+    The bar collision residue Res^{coll}_{0,2}(Theta_A) = k*Omega/z
+    in the trace-form convention.
     Single pole at z = 0 (AP19).
     """
-    return casimir_tensor_fund() / z
+    return complex(k) * casimir_tensor_fund() / z
 
 
-def r_matrix_adj(z: complex) -> np.ndarray:
-    r"""r-matrix in the adjoint: r(z) = Omega^{adj}/z.
+def r_matrix_adj(z: complex, k: complex = 1) -> np.ndarray:
+    r"""Raw affine residue in the adjoint: r(z) = k*Omega^{adj}/z.
 
     Same Casimir r-matrix formula but in the adjoint representation.
     Satisfies the CYBE in the adjoint.
     """
-    return casimir_tensor_adj() / z
+    return complex(k) * casimir_tensor_adj() / z
 
 
 def R_matrix_yang_fund(u: complex) -> np.ndarray:
@@ -500,10 +503,10 @@
 
 def kz_hamiltonian(n: int, site: int, z_vals: List[complex],
                    Omega_2: np.ndarray, dim_rep: int,
-                   kappa_val: complex) -> np.ndarray:
+                   level_shift: complex) -> np.ndarray:
     r"""KZ Hamiltonian H_i for n points at positions z_1,...,z_n.
 
-    H_i = (1/kappa) sum_{j != i} Omega_{ij} / (z_i - z_j)
+    H_i = (1/(k+h^vee)) sum_{j != i} Omega_{ij} / (z_i - z_j)
 
     The KZ equation is d Phi / d z_i = H_i Phi.
     """
@@ -515,12 +518,12 @@
         ii, jj = min(site, j), max(site, j)
         Omega_ij = _omega_ij(n, ii, jj, Omega_2, dim_rep)
         H += Omega_ij / (z_vals[site] - z_vals[j])
-    return H / kappa_val
+    return H / level_shift
 
 
 def verify_kz_commutativity(n: int, z_vals: List[complex],
                             Omega_2: np.ndarray, dim_rep: int,
-                            kappa_val: complex) -> float:
+                            level_shift: complex) -> float:
     r"""Verify [H_i, H_j] = 0 for all pairs i != j (IBR).
 
     The infinitesimal braid relations state that the KZ
@@ -529,7 +532,7 @@
 
     Returns: max Frobenius norm of [H_i, H_j] over all pairs.
     """
-    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, kappa_val)
+    Hs = [kz_hamiltonian(n, i, z_vals, Omega_2, dim_rep, level_shift)
           for i in range(n)]
     max_norm = 0.0
     for i in range(n):
@@ -695,27 +698,26 @@
 # DNP comparison
 # ============================================================
 
-def dnp_r_matrix_genus0(z: complex) -> np.ndarray:
+def dnp_r_matrix_genus0(z: complex, k: complex = 1) -> np.ndarray:
     r"""DNP dg-shifted Yangian r-matrix at genus 0 for sl_3.
 
-    For pure gauge theory (sl_3 at level k), the DNP r-matrix is:
-        r^{DNP}(z) = Omega/z
-    This is EXACTLY the MK bar collision residue (prop:dg-shifted-comparison).
+    This comparison engine uses the same level normalization as
+    r_matrix_fund; the unit-level case is Omega/z.
     """
-    return r_matrix_fund(z)
+    return r_matrix_fund(z, k=k)
 
 
-def dnp_comparison_report(z: complex) -> Dict[str, object]:
+def dnp_comparison_report(z: complex, k: complex = 1) -> Dict[str, object]:
     r"""Compare MK bar extraction with DNP dg-shifted Yangian for sl_3.
 
     Checks:
-    1. r^{MK}(z) = r^{DNP}(z) = Omega/z  (genus-0 agreement)
+    1. r^{MK}(z) = r^{DNP}(z) = k*Omega/z  (genus-0 agreement)
     2. Both satisfy CYBE
     3. A_infty YBE reduces to CYBE (no higher operations for KM)
     4. Non-renormalization = E_2-collapse = Koszulness
     """
-    r_mk = r_matrix_fund(z)
-    r_dnp = dnp_r_matrix_genus0(z)
+    r_mk = r_matrix_fund(z, k=k)
+    r_dnp = dnp_r_matrix_genus0(z, k=k)
     agreement = bool(np.allclose(r_mk, r_dnp, atol=1e-14))
 
     w = z + 1.0
@@ -724,8 +726,8 @@
 
     return {
         "genus_0_agreement": agreement,
-        "r_MK": "Omega/z (bar collision residue)",
-        "r_DNP": "Omega/z (A_infty structure on A^!)",
+        "r_MK": "k*Omega/z (bar collision residue)",
+        "r_DNP": "k*Omega/z (matched normalization)",
         "identification": "prop:dg-shifted-comparison",
         "CYBE_norm": cybe_norm,
         "CYBE_satisfied": cybe_norm < 1e-10,
@@ -841,9 +843,9 @@
     cybe_adj = verify_cybe(Omega_a, ADJ_DIM, 1.5, 2.7)
 
     kz_norm_3 = verify_kz_commutativity(
-        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(kappa))
+        3, [1.0, 2.5, 4.0], Omega_f, FUND_DIM, float(k + H_VEE))
 
-    dnp = dnp_comparison_report(1.5)
+    dnp = dnp_comparison_report(1.5, k=k)
     verl_k1 = verlinde_fusion(1, (1, 0), (1, 0))
 
     return {
diff --git a/compute/lib/yangian_rmatrix_arithmetic_engine.py b/compute/lib/yangian_rmatrix_arithmetic_engine.py
index 8b4c8d3dcdfc06af3654b2c7e038ef57d13fe606..68d0182f59af56f408a3f596f5f8f4223b206978
--- a/compute/lib/yangian_rmatrix_arithmetic_engine.py
+++ b/compute/lib/yangian_rmatrix_arithmetic_engine.py
@@ -802,10 +802,16 @@
             residuals[(a, b)] = 0.0  # Will be filled by numerical check
 
     # Numerical verification at many parameter points
-    test_params = [
+    candidate_params = [
         (3.7, 1.3), (5.2, 2.1), (7.1, 4.3), (2.8, 0.9),
         (10.0, 3.0), (4.5, 1.5), (6.3, 2.7),
     ]
+    test_params = [
+        (u, v) for u, v in candidate_params
+        if not _full_rmatrix_hits_pole(lie_type, n, u)
+        and not _full_rmatrix_hits_pole(lie_type, n, v)
+        and not _full_rmatrix_hits_pole(lie_type, n, u - v)
+    ]
 
     ybe_errors = []
     for u, v in test_params:
@@ -843,12 +849,27 @@
     return float(np.max(np.abs(lhs - rhs)))
 
 
+def _full_rmatrix_hits_pole(lie_type: str, n: int, u: complex,
+                            tol: float = 1e-12) -> bool:
+    """Check whether the rational R-matrix is singular at the given spectral value."""
+    if abs(u) < tol:
+        return True
+
+    if lie_type == 'B':
+        return abs(u - (n - 0.5)) < tol
+    if lie_type == 'C':
+        return abs(u - (n + 1.0)) < tol
+    if lie_type == 'D':
+        return abs(u - (n - 1.0)) < tol
+    return False
+
+
 def _full_rmatrix(lie_type: str, n: int, u: complex) -> np.ndarray:
     """Full R-matrix R(u) for a given type, in the fundamental representation.
 
     Type A: R(u) = uI + P (additive Yang).
     Types B,D: R(u) = I - P/u + Q/(u - kappa_R).
-    Type C: R(u) = I - P/u - K/(u + kappa_R).
+    Type C: R(u) = I - P/u - K/(u - kappa_R).
     G_2: R(u) = I + Omega/u (leading order approximation).
     """
     data = lie_algebra_data(lie_type, n)
diff --git a/compute/lib/yangian_rmatrix_sl3.py b/compute/lib/yangian_rmatrix_sl3.py
index 2f32843fdcc6e22bf5fc8094253553640a9bd863..5d6bcf9aeb109264212e40fc1ebd48ac59ee8f4c
--- a/compute/lib/yangian_rmatrix_sl3.py
+++ b/compute/lib/yangian_rmatrix_sl3.py
@@ -10,7 +10,8 @@
 ---------------------
 * OPE:  J^a(z) J^b(w) ~ k g^{ab}/(z-w)^2 + f^{abc} J^c(w)/(z-w)
 * r-matrix (collision residue of bar):
-      r(z) = \sum_a T^a \otimes T_a / z   in  sl_3 \otimes sl_3 \otimes C((z))
+      r(z) = k * \sum_a T^a \otimes T_a / z
+  in  sl_3 \otimes sl_3 \otimes C((z))
   This has a SINGLE pole at z=0 (AP19: bar absorbs one power).
 * R-matrix (perturbative in 1/\kappa):
       R(z) = 1 + r(z)/\kappa + O(1/\kappa^2)
@@ -330,16 +331,16 @@
 # r-matrix from bar complex collision residue
 # ============================================================
 
-def r_matrix_abstract() -> Dict[str, object]:
-    r"""The r-matrix r(z) = k*Omega/z extracted from the bar collision residue.
+def r_matrix_abstract(k: complex = 1) -> Dict[str, object]:
+    r"""The affine collision residue r(z) = k*Omega/z in the fundamental.
 
     The bar construction for the affine KM algebra sl_3_k uses the
-    propagator d\log E(z,w).  The collision residue (AP19) extracts the
-    simple pole of the OPE: [a, b] (structure constants), NOT the
-    double pole k g^{ab} (curvature).
+    propagator d\log E(z,w).  By AP19 the double pole
+    k g^{ab}/(z-w)^2 contributes the simple collision pole, while the
+    bracket term f^{ab}{}_c J^c/(z-w) shifts to a regular term and drops.
 
     The r-matrix lives in sl_3 \otimes sl_3 \otimes C((z)):
-        r(z) = sum_a T^a \otimes T_a / z
+        r(z) = k * sum_a T^a \otimes T_a / z
 
     where the sum is over a dual-basis pair: (T^a, T_b) = delta^a_b.
 
@@ -356,21 +357,23 @@
         "pole_location": 0,
         "representation": "fundamental (C^3)",
         "formula": "r(z) = k*Omega / z",
+        "level": k,
         "AP19_check": "OPE poles z^{-2}, z^{-1}; bar absorbs one; r-matrix has z^{-1} only",
     }
 
 
-def r_matrix_fund(z: complex) -> np.ndarray:
+def r_matrix_fund(z: complex, k: complex = 1) -> np.ndarray:
     """r-matrix in the fundamental representation: r(z) = k*Omega / z.
 
     Args:
         z: spectral parameter (nonzero).
+        k: affine level in the trace-form convention.
 
     Returns:
         9x9 complex matrix.
     """
     Omega = casimir_tensor_fund()
-    return Omega / z
+    return complex(k) * Omega / z
 
 
 # ============================================================
@@ -775,8 +778,8 @@
 def R_residue_at_zero() -> np.ndarray:
     """Residue of R(z) = I + P/z at z = 0 is P (the permutation).
 
-    This is the collision residue of the bar construction: the
-    permutation operator P exchanges the two tensor factors.
+    This is the residue of the normalized Yang R-matrix, not the raw
+    affine collision residue k*Omega/z.
     """
     return permutation_matrix_3()
 
diff --git a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
index 13f87c84d227dd6d87fa9afc7e4442e35d5fda98..2513fe9acf4cb0ebd14e0f0a0dca74e7d7d03752
--- a/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
+++ b/compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
@@ -274,14 +274,25 @@
 # ============================================================
 
 class TestRMatrixPoleStructure:
-    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
+    """The affine residue r(z) = k*Omega/z has a single pole at z=0 (AP19)."""
 
     def test_single_pole_fund(self):
-        """r(z) = Omega/z has a single pole (AP19)."""
+        """At unit level, r(z) = Omega/z has a single pole (AP19)."""
         r = r_matrix_fund(1.0)
         Omega = casimir_tensor_fund()
         assert np.allclose(r, Omega, atol=1e-14)
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: the raw affine residue vanishes at k=0."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_scales_linearly_with_level(self):
+        """Trace-form raw residue scales linearly in k."""
+        r1 = r_matrix_fund(1.0, k=1)
+        r3 = r_matrix_fund(1.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)
@@ -294,7 +305,7 @@
         assert np.allclose(Omega, P - np.eye(9) / 3, atol=1e-10)
 
     def test_adj_r_matrix_structure(self):
-        """r^{adj}(z) = Omega^{adj}/z has single pole."""
+        """r^{adj}(z) = k*Omega^{adj}/z has single pole."""
         r1 = r_matrix_adj(1.0)
         r2 = r_matrix_adj(2.0)
         assert np.allclose(r1, 2.0 * r2, atol=1e-10)
@@ -377,14 +388,14 @@
     def test_kz_n3_fund(self):
         """KZ commutativity at 3 points, fundamental rep."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
     def test_kz_n3_fund_different_z(self):
         """KZ commutativity at 3 points with different spectral params."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(2))
+        kv = float(2 + H_VEE)
         norm = verify_kz_commutativity(3, [0.5, 1.7, 3.2], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
@@ -393,18 +404,26 @@
 
         This tests all 6 pairs of Hamiltonians H_1,...,H_4."""
         Omega = casimir_tensor_fund()
-        kv = float(kappa_sl3(1))
+        kv = float(1 + H_VEE)
         norm = verify_kz_commutativity(4, [1.0, 2.0, 3.5, 5.0], Omega, FUND_DIM, kv)
         assert norm < 1e-10
 
-    def test_kz_kappa_independence(self):
-        """IBR holds for any kappa (it's a property of Omega, not kappa)."""
+    def test_kz_level_shift_independence(self):
+        """IBR holds for any nonzero KZ level shift (it's a property of Omega)."""
         Omega = casimir_tensor_fund()
         for k in [1, 2, 5, 10]:
-            kv = float(kappa_sl3(k))
+            kv = float(k + H_VEE)
             norm = verify_kz_commutativity(3, [1.0, 2.5, 4.0], Omega, FUND_DIM, kv)
             assert norm < 1e-10, f"IBR fails at k={k}"
 
+    def test_kz_hamiltonian_prefactor_matches_k_plus_hvee(self):
+        """KZ uses 1/(k+h^vee), not 1/kappa."""
+        Omega = casimir_tensor_fund()
+        z_vals = [1.0, 3.0]
+        H = kz_hamiltonian(2, 0, z_vals, Omega, FUND_DIM, float(1 + H_VEE))
+        expected = Omega / ((z_vals[0] - z_vals[1]) * float(1 + H_VEE))
+        assert np.allclose(H, expected, atol=1e-12)
+
 
 # ============================================================
 # 9. Verlinde fusion rules
diff --git a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
index 71a65a7ace3d797fb409ede89e6214070a4d5a18..5a1c58f7a9bc70dd9550d64bbb0a09b842acd8aa
--- a/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
+++ b/compute/tests/test_yangian_rmatrix_arithmetic_engine.py
@@ -17,6 +17,7 @@
 """
 
 import math
+import warnings
 
 import numpy as np
 import pytest
@@ -952,6 +953,17 @@
                     f"CYBE passes but YBE fails for {lie_type}_{n}"
                 )
 
+    def test_ybe_parameter_sweep_avoids_rational_pole_warnings(self):
+        """The YBE sweep should skip exact poles instead of emitting runtime warnings."""
+        with warnings.catch_warnings(record=True) as caught:
+            warnings.simplefilter("always", RuntimeWarning)
+            result_b = ybe_coefficient_relations('B', 2, 4)
+            result_c = ybe_coefficient_relations('C', 2, 4)
+        assert result_b['passes']
+        assert result_c['passes']
+        runtime_warnings = [w for w in caught if issubclass(w.category, RuntimeWarning)]
+        assert runtime_warnings == []
+
     def test_C2_times_N_equals_dim_g(self):
         """C_2(fund) * dim(fund) = dim(g) for all types."""
         for lie_type, n in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2), ('D', 3)]:
diff --git a/compute/tests/test_yangian_rmatrix_sl3.py b/compute/tests/test_yangian_rmatrix_sl3.py
index 2b314dd36b2911744c810da11a3bb36359fe503b..ec3b2575b184a95768527d4f6c17b2fef81d3b13
--- a/compute/tests/test_yangian_rmatrix_sl3.py
+++ b/compute/tests/test_yangian_rmatrix_sl3.py
@@ -224,13 +224,12 @@
     """Verify the r-matrix has the correct pole structure (AP19)."""
 
     def test_single_pole(self):
-        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
+        """r(z) = k*Omega/z has a SINGLE pole at z = 0 (AP19)."""
         info = r_matrix_abstract()
         assert info["pole_order"] == 1
 
     def test_residue_is_omega(self):
-        """Residue of r(z) at z = 0 is Omega = P - I/3."""
-        # r(z) = Omega/z, so Res_{z=0} r(z) = Omega
+        """Residue of the unit-level r-matrix is Omega = P - I/3."""
         Omega = casimir_tensor_fund()
         P = permutation_matrix_3()
         I9 = np.eye(9)
@@ -247,6 +246,17 @@
         info = r_matrix_abstract()
         assert "z^{-1} only" in info["AP19_check"]
 
+    def test_k0_vanishes(self):
+        """AP126/AP141: at k=0 the affine collision residue vanishes."""
+        r = r_matrix_fund(1.0, k=0)
+        assert np.allclose(r, np.zeros((9, 9)), atol=1e-14)
+
+    def test_linear_in_level(self):
+        """Trace-form residue scales linearly with the level k."""
+        r1 = r_matrix_fund(2.0, k=1)
+        r3 = r_matrix_fund(2.0, k=3)
+        assert np.allclose(r3, 3.0 * r1, atol=1e-12)
+
     def test_r_matrix_at_large_z(self):
         """r(z) -> 0 as z -> infinity."""
         r = r_matrix_fund(100.0)

tokens used
217,568
