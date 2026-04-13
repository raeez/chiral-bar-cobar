# U10_missing_computations (867s)

- [CRITICAL] `compute/lib/shadow_zeta_engine.py:7` — PROBLEM: The executable genus formula is wrong on the live surface: line 7 states `F_g(kappa) = kappa^g * b_g`, lines 18-22 specialize this to `F_2 = 7*kappa^2/5760`, and line 110 returns `kappa ** g * shadow_b_g(g)`. That is incompatible with the repo’s linear genus convention already used in `compute/lib/universal_shadow_tower_engine.py:466-481`. FIX: change the definition to `F_g(kappa) = kappa * b_g`, update lines 18-22 and 85-109 to `F_2 = 7*kappa/5760`, change line 110 to `return kappa * shadow_b_g(g)`, and rewrite the convergence paragraph so `kappa` is a global linear prefactor rather than a genus-dependent power.

- [CRITICAL] `compute/lib/quantum_group_shadow.py:197` — PROBLEM: The affine `sl_2` r-matrix surface is internally inconsistent. The docstring says “actual shadow coefficient” is `Omega/((k+h^v) z)` at line 205, but the function returns `poles={1: 1}` at line 220, i.e. bare `Omega/z`. That also conflicts with `compute/lib/collision_residue_identification.py:132-133`, which uses the trace-form convention `k*Omega/z`. FIX: add an explicit `convention` parameter with only `trace_form` and `kz`; return `k` in the trace-form branch and `1/(k+h^v)` in the KZ branch; add tests for `k=0` and `k=-h^v`; and implement the bridge identity in code instead of leaving both normalizations to drift in prose.

- [CRITICAL] `compute/lib/theorem_dk0_evaluation_bridge_engine.py:138` — PROBLEM: This file writes the KZ connection as `... Omega_{ij} d log(z_i - z_j)`. The same KZ-with-`d log` misuse also appears in `compute/lib/primitive_kernel_full.py:874`, `compute/lib/theorem_three_way_r_matrix_engine.py:394`, and `compute/lib/shadow_mzv_engine.py:923`. That directly violates census item C28, which separates the Arnold `d log` form from the KZ connection form. FIX: replace every KZ formula with `nabla_KZ = d + sum r_{ij} dz_{ij}` or, expanded, `d - (1/(k+h^v)) sum Omega_{ij} dz_{ij}/(z_i-z_j)`; reserve `d log(z_i-z_j)` for bar/Arnold code paths only; and add a grep-backed regression test that fails on `KZ` combined with `d log`.

- [HIGH] `compute/lib/collision_residue_identification.py:338` — PROBLEM: The affine `sl_2` verification never computes the C13 Sugawara split. The file advertises `kappa = 3(k+2)/4` at lines 132-133 and 842, but `scalar_trace()` at lines 345-347 only records `tr(r)=3k`. The shift from `av(r)` to full `kappa` is left implicit instead of being verified. FIX: add explicit functions for `kappa_dp = av(r) = k*dim(g)/(2h^v)` and `kappa_full = kappa_dp + dim(g)/2`, then assert `kappa_full == 3*(k+2)/4` on sample levels.

- [HIGH] `compute/lib/true_formula_census_verifier.py:6` — PROBLEM: The dedicated census verifier explicitly stops at `C10`. `compute/lib/landscape_census_verification.py:3-11` only promises numerical table entries, so it does not close the gap for structural items like C14, C15, C24, C28, and C29. FIX: extend `true_formula_census_verifier.py` through `C31`, or add a new `compute/lib/true_formula_census_verifier_v2.py` that imports per-formula checks and emits one canonical pass/fail report for all 31 census items.

- [HIGH] `compute/lib/k3_cy_a2_verification_engine.py:103` — PROBLEM: In the files I read, the exact C14/C15 formulas appear only as convention docstrings like this one: `B(A) = T^c(s^{-1} A-bar)` and `|s^{-1}v| = |v|-1`. The same pattern repeats in `ordered_chirhoch_sl3_elliptic_engine.py:84-85` and related files, but I did not find an executable verifier for the augmentation ideal or desuspension sign. FIX: add `compute/lib/bar_complex_census_verifier.py` that builds a toy augmented algebra, forms `T^c(s^{-1}\bar A)`, checks deconcatenation, rejects `A` in place of `\bar A`, and asserts the grading shift on basis elements.

- [HIGH] `compute/lib/shadow_cohft_tautological.py:24` — PROBLEM: This module hard-codes the same wrong `kappa^g` law in two places: line 24 says `tau_{g,0}(H_k) = kappa^g * lambda_g`, and line 198 repeats `tau_{g,0} = kappa^g * lambda_g^{FP}`. That contradicts the linear genus formula already implemented in `compute/lib/universal_shadow_tower_engine.py:466-481`. FIX: change both occurrences to `kappa * lambda_g^{FP}` if this is the scalar free-energy/CohFT surface; if a pre-collapse graph weight is intended instead, rename the object and document the final collapse step explicitly so it is not advertised as the scalar theorem.

- [MEDIUM] `compute/lib/theorem_shadow_conformal_block_engine.py:343` — PROBLEM: In the files I read, C24 is not directly verified. This file implements the specialized contour formula `S_r = (1/(2*pi*i*r)) ...`, while `compute/lib/chiral_zeta_virasoro_engine.py:36` only cites C24 in a docstring. I did not find a standalone check of the canonical coefficient rule `[z^{n-1}]f(z) = (1/(2*pi*i)) ∮ f(z) dz / z^n`, nor a negative test for the forbidden `1/(2*pi)` normalization. FIX: add `compute/lib/cauchy_integral_normalization_engine.py` with exact monomial coefficient tests, a failing branch for the missing-`i` normalization, and the `F_1 = kappa/24` sanity recovery.

- [MEDIUM] `compute/lib/theorem_bv_brst_o3_obstruction_engine.py:234` — PROBLEM: The file uses the higher-genus matrix formula `(Im Omega)^{-1}_{ij}` at line 234 and again at lines 977-979, and separately writes the genus-1 scalar surface at lines 236-237. That is good notation, but I did not find a dedicated verifier for census item C29 proving the `g=1` collapse from matrix to scalar while preventing scalarization at `g>=2`. FIX: add `compute/lib/period_matrix_collapse_verifier.py` that checks `((Im Omega)^{-1})_{11} = 1/Im(tau)` in genus 1, retains full matrix dependence in genus 2, and fails if a higher-genus formula collapses to a scalar.

- [LOW] `compute/lib/universal_shadow_tower_engine.py:468` — PROBLEM: The docstring still says `F_2 = 7*kappa^2/5760` even though the code immediately below is linear in `kappa` at lines 474-481. This is local documentation drift on a load-bearing formula. FIX: change line 468 to `F_2 = 7*kappa/5760` and add a small regression test that compares the docstring examples against `compute_free_energies`.

## Summary
Checked: 31 | Findings: 10 | Verdict: FAIL


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
session id: 019d840a-fa35-7d03-b1cc-0c25381f4d78
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

For each formula in the census (C1-C31 in CLAUDE.md): is there a compute engine in compute/lib/ that verifies it? For each missing engine: flag it.

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers

thinking
**Evaluating planning needs**

I want to ensure everything is grounded correctly. I'll likely need to read relevant files, starting with an explorer to identify locations, then maybe open them manually using shell commands. It seems like I should use the commentary tool for frequent updates and maybe an update plan since this involves substantial work. I need to produce a thorough audit to identify each formula C1-C31 in CLAUDE.md and check if the compute engine in compute/lib verifies them. I’ll inspect compute/lib for modules.
codex
I’m auditing the formula census against the live compute surface, with the goal of identifying every unfinished verification lane in `compute/lib/` and giving an exact remediation for each gap. I’ll first read the governing census and the compute library inventory, then map each `C1–C31` item to concrete verifier code or a missing engine.
collab spawn_agent(call_1MZ4Q3M0UKdJwdkujQHlEt7u, prompt="Inspect /Users/raeez/chiral-bar-cobar/CLAUDE.md and identify the full C1-C31 formula census locations, including exact l…")
mcp startup: no servers
spawn_agent(call_1MZ4Q3M0UKdJwdkujQHlEt7u, prompt="Inspect /Users/raeez/chiral-bar-cobar/CLAUDE.md and identify the full C1-C31 formula census locations, including exact l…") pending init:
  agent: 019d840b-364d-7741-ba2c-62040917528c
collab spawn_agent(call_ScG8W4UIclmokaoxNPVLDt94, prompt="Inspect /Users/raeez/chiral-bar-cobar/compute/lib and produce an inventory of verification engines/modules with exact fi…")
spawn_agent(call_ScG8W4UIclmokaoxNPVLDt94, prompt="Inspect /Users/raeez/chiral-bar-cobar/compute/lib and produce an inventory of verification engines/modules with exact fi…") pending init:
  agent: 019d840b-3650-70a0-887f-07d355ec5667
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C[0-3][0-9]" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit_campaign_20260412_230832
audit_campaign_20260412_231034
bibliography
bp_self_duality.pdf
chapters
chiral_chern_weil.pdf
 succeeded in 51ms:
219:Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).
237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
243:**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.
245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
247:**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).
249:**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).
251:**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.
253:**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).
255:**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).
257:**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).
259:**C20. Bershadsky-Polyakov Koszul conductor.** `K_BP = c(k) + c(-k-6) = 196`. Self-dual level k=-3. Wrong: K_BP=76 (corrected in Wave 7); K_BP=2 (AP140, confusing with ghost constant C_{(2,1)}=2).
261:**C21. Igusa cusp form / BKM kappa.** `wt(Phi_10) = 10 = 2*kappa_BKM(K3xE)`, so `kappa_BKM(K3xE) = 5`. Phi_10 = Delta_5^2. Wrong: kappa_BKM = 10 (identifies kappa with full weight); kappa_BKM = 2.
263:**C22. Dedekind eta.** `eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)`. Prefactor q^{1/24} ESSENTIAL for modular weight 1/2 transformation. Wrong: dropping q^{1/24}; q^{1/12} prefactor.
265:**C23. Bicoloured partitions.** `1/eta^2 = q^{-1/12} sum p_{-2}(n) q^n`, coefficients `(1, 2, 5, 10, 20, ...)` (OEIS A002513). Wrong: triangular (1,3,6,10,...) (AP135); ordinary partitions (1,1,2,3,5,...).
267:**C24. Cauchy integral normalization.** `[z^{n-1}] f(z) = (1/(2*pi*i)) * contour_integral f(z) dz/z^n`. Wrong: 1/(2*pi) (missing i gives zero for real integrands, AP120). Sanity: F_1 = kappa/24.
269:**C25. MC equation.** `d*Theta + (1/2)[Theta, Theta] = 0`. QME: `hbar*Delta*S + (1/2){S,S} = 0`. Wrong: drop the 1/2 (except odd parity); sign flip.
271:**C26. G/L/C/M classification.** G (r=2, Heis), L (r=3, aff KM), C (r=4, betagamma), M (r=inf, Vir/W_N). Shadow depth != Koszulness.
273:**C27. Chiral Hochschild of Vir.** `ChirHoch^*(Vir_c)` concentrated in degrees {0,1,2}; polynomial Hilbert series. This is AMPLITUDE (topological), NOT virtual dimension (arithmetic) (AP134). NOT C[Theta] (AP94). NOT Gelfand-Fuchs (GF infinite, AP95).
Plan update
Running a repository-grounded audit of the formula census versus `compute/lib/`, then re-checking any candidate gaps against exact file contents before reporting findings.
  → Read the governing census and repo-wide audit context (`CLAUDE.md`, concordance, theorem registry, red-team summary) to lock scope and formula list
  • Inventory `compute/lib/` verification engines and map them against each `C1-C31` census item
  • Re-verify each gap against exact file contents, then produce severity-ranked findings with exact fixes
exec
/bin/zsh -lc 'ls compute' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
__init__.py
__pycache__
audit
lib
results
scratch
scripts
state
tests
verified
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"C[0-3][0-9]\\.\" CLAUDE.md | head" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
243:**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.
245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
247:**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).
249:**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).
251:**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.
253:**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).
255:**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).
257:**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).

exec
/bin/zsh -lc 'ls compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
ainfty_transferred_structure.py
algebraic_family_rigidity.py
thinking
**Planning file reading**

I’m thinking about how to read multiple files efficiently by using parallel execution commands. It seems like using `rg`, and maybe `sed` or `nl`, could be useful here. I need to read specific files like CLAUDE, concordance, theorem_registry, and red_team_summary. I should also consider listing `compute/lib`. It could help to leverage parallel processing again to speed things up. Let’s see how this works out!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"C1\\.\" CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
221:**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
exec
/bin/zsh -lc 'rg -l "verification" compute/lib | head' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/cusp_form_shadow_arity.py
compute/lib/genus3_landscape.py
compute/lib/bc_isomonodromic_shadow_engine.py
compute/lib/bar_cohomology_koszul_criterion.py
compute/lib/bc_euler_product_shadow_engine.py
compute/lib/mc5_disk_local.py
compute/lib/beilinson_auditor.py
compute/lib/frontier_verifications.py
compute/lib/chirhoch_bershadsky_polyakov_engine.py
compute/lib/n2_free_field_shadow.py
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"C2\\.\" CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
223:**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"C[3-8]\\.\" CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
225:**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).
227:**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.
229:**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).
231:**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).
233:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
235:**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).
codex
I’ve locked the audit surface to the formula census plus the live compute layer. Next I’m reading the canonical sources and enumerating `compute/lib/` so the findings are tied to exact text, not repo folklore.
exec
/bin/zsh -lc 'rg -n "C1-C31|True Formula Census|# Kappa|# r-matrix|# Central charges|# Bar complex|# Complementarity|# Combinatorial / numerical|C1|C31" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"landscape_census|kappa|r\\"'^KM|r'"\\"'^Vir|B'"\\(A\\)|F_1|F_2|Delta =|S_2 =|K\\(|sl_2 bar H\\"'^2|genus-2 stable graphs|1/eta'"\\"'^2|alpha_g|d_alg" chapters/connections/concordance.tex metadata/theorem_registry.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg --files compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
217:## True Formula Census
219:Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).
221:**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
243:**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.
245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
247:**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).
249:**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).
251:**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.
253:**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).
255:**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).
257:**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).
281:**C31. Bershadsky-Polyakov complementarity conductor.** `kappa(BP) + kappa(BP^!) = 98/3` (NOT 1/3). `varrho_BP = 1/6`. Checks: K_BP = c(k) + c(-k-6) = 196 (cross-check C20); at self-dual level k=-3, kappa(BP) = 49/3. Wrong: kappa(BP)+kappa(BP^!)=1/3 (off by factor 98); varrho_BP=1/2 (confusing with rank-1 value).
373:- B52. `kappa(BP) + kappa(BP^!) = 1/3`. CORRECT: `98/3`. AP140/C31.
488:| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
823:AP144: Convention coexistence without bridge. Different chapters independently develop conventions for the same object (r-matrix: trace-form k*Omega/z vs KZ Omega/((k+h^v)*z); kappa: several families). The conventions agree at generic parameter values but diverge at boundary values (k=0, k=-h^v). When multiple conventions coexist, a BRIDGE IDENTITY must be stated explicitly at every site, and boundary behavior must be checked in EACH convention separately. The r-matrix normalization issue (C9/C13/AP126 inconsistency, resolved April 2026) is the canonical example. After introducing ANY convention for a shared object, grep all three volumes for alternative conventions of the same object and install bridge identities.
 exited 2 in 51ms:
Total output lines: 327

rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
metadata/theorem_registry.md:555:| `prop:comp-n2-kappa` | `proposition` | 1089 | Modular characteristic |
metadata/theorem_registry.md:653:| `prop:kappa-universality-en` | `proposition` | 825 | Kappa universality across $n$ |
metadata/theorem_registry.md:665:| `thm:en-shadow-tower` | `theorem` | 2681 | $\En$ shadow obstruction tower: universality of $\kappa$ and formality collapse |
metadata/theorem_registry.md:831:| `cor:kappa-periodicity` | `corollary` | 5777 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
metadata/theorem_registry.md:832:| `cor:kappa-additivity` | `corollary` | 5806 | Additivity of the obstruction coefficient |
metadata/theorem_registry.md:833:| `cor:kappa-sum-wn` | `corollary` | 5827 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
metadata/theorem_registry.md:1015:| `rem:delta-f2-graph-decomposition` | `remark` | 21827 | $\delta F_2$ graph-stratum decomposition |
metadata/theorem_registry.md:1022:| `rem:large-n-delta-f2-planar` | `remark` | 22668 | Large-$N$ and 't~Hooft limit of $\delta F_2$ |
metadata/theorem_registry.md:1072:| `prop:symn-kappa-linearity` | `proposition` | 27043 | Symmetric orbifold kappa linearity |
metadata/theorem_registry.md:1073:| `rem:symmetric-orbifold-kappa` | `remark` | 27127 | Symmetric orbifold kappa: four independent verifications |
metadata/theorem_registry.md:1369:| `prop:bp-kappa` | `proposition` | 260 | Modular characteristic of $\mathcal{B}^k$;\ |
metadata/theorem_registry.md:1554:| `thm:heisenberg-genus2-obstruction` | `theorem` | 561 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
metadata/theorem_registry.md:1565:| `thm:heisenberg-modular-cooperad` | `theorem` | 2115 | CT-$2$ for Heisenberg: modular cooperad on $\Cop(\cH_\kappa)$ |
metadata/theorem_registry.md:1625:| `prop:kappa-anti-symmetry-ff` | `proposition` | 5821 | Kappa anti-symmetry under Feigin--Frenkel involution |
metadata/theorem_registry.md:1627:#### `chapters/examples/landscape_census.tex` (21)
metadata/theorem_registry.md:1666:| `rem:lattice:koszul-dual-kappa` | `remark` | 1039 | Koszul dual kappa for non-unimodular lattices |
metadata/theorem_registry.md:1706:| `prop:level1-kappa-reduction` | `proposition` | 208 | Level-$1$ $\kappa$ reduction |
 succeeded in 51ms:
Total output lines: 1332

compute/lib/theorem_hca_pillar_a_engine.py
compute/lib/bar_cohomology_koszul_criterion.py
compute/lib/cusp_form_shadow_arity.py
compute/lib/bc_isomonodromic_shadow_engine.py
compute/lib/theorem_transport_transpose_sl4_engine.py
compute/lib/arithmetic_comparison_test.py
compute/lib/admissible_sl3_d1_poisson_engine.py
compute/lib/bc_selberg_class_engine.py
compute/lib/s3_framing_obstruction.py
compute/lib/yangian_residue.py
compute/lib/cy_elliptic_genus_k3e_engine.py
compute/lib/cy_n4sca_k3_engine.py
compute/lib/rademacher_kloosterman.py
compute/lib/bc_matrix_model_shadow_engine.py
compute/lib/verdier_hecke_bridge.py
compute/lib/analytic_verifications.py
compute/lib/cumulant_algebra.py
compute/lib/minimal_model_l_functions.py
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba CLAUDE.md | sed -n '210,290p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   210	A (algebra) -- B(A) (bar coalgebra) -- A^i=H*(B(A)) (dual coalgebra) -- A^!=((A^i)^v) (dual algebra) -- Z^der_ch(A) (derived center = bulk). Omega(B(A))=A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.
   211	
   212	## Key Constants
   213	
   214	kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(Heis)=k. kappa(W_N)=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j. Vir^!=Vir_{26-c}. Self-dual at c=13. kappa+kappa'=0 (KM/free), 13 (Vir). QME: hbar*Delta*S+(1/2){S,S}=0. sl_2 bar H^2=5 (not 6). Desuspension: |s^{-1}v|=|v|-1, NOT +1. eta(q)=q^{1/24}*prod(1-q^n). Bar propagator d log E(z,w): ALWAYS weight 1. Prime form: section of K^{-1/2} boxtimes K^{-1/2}. FM_n(X): blowup along diagonals, NOT complement. Grading: COHOMOLOGICAL (|d|=+1). Curved A-inf: m_1^2(a)=[m_0,a]. Bar d^2=0 always; curvature appears as m_1^2 != 0.
   215	alpha_g = 2*rank + 4*dim*h^v (universal Hilbert-series growth, all simple types). d_alg in {0,1,2,inf} (depth gap: 3 impossible, prop:depth-gap-trichotomy). kappa(BP)+kappa(BP^!)=98/3 (self-dual k=-3).
   216	
   217	## True Formula Census
   218	
   219	Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).
   220	
   221	**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
   222	
   223	**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
   224	
   225	**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).
   226	
   227	**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.
   228	
   229	**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).

exec
/bin/zsh -lc "sed -n '1,160p' compute/lib/true_formula_census_verifier.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""True Formula Census verification engine.

Independently recomputes the canonical Wave 12-2 formulas used in the
standard landscape census and cross-checks them against the census values.

Checks covered:
  C01. kappa(Heis_k) = k
  C02. kappa(Vir_c) = c/2
  C03. kappa(V_k(g)) = dim(g) * (k + h^vee) / (2 * h^vee)
  C04. kappa(W_N) = c * (H_N - 1)
  C05. c_bc(lambda) = 1 - 3 * (2 * lambda - 1)^2
  C06. c_bg(lambda) = 2 * (6 * lambda^2 - 6 * lambda + 1)
  C07. E_8 fundamental irrep dimensions
  C08. H_N = sum_{j=1}^N 1/j exactly
  C09. Complementarity sums by family
  C10. K_BP = 196 for Bershadsky-Polyakov W_3^(2)

Anti-pattern coverage:
  AP1   family-specific kappa formulas
  AP24  complementarity is not universal across families
thinking
**Inspecting compute files**

I need to read the outputs, but they might be truncated. It sounds like I'm looking for specific compute files relevant to formulas C1-C31. I'll likely check CLAUDE C1-C31 in context with all the formula lines. Mapping the formulas is essential. Since the search showed C1-C19 and C31, I should focus on section 217-281. I’ll plan to open those lines and maybe explore even more if necessary.
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/kappa_cross_verification.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Cross-verification engine for the modular characteristic kappa(A).

kappa(A) is the single most important invariant in the modular Koszul duality
programme: it appears in F_g = kappa * lambda_g^FP at ALL genera, controls the
genus-1 obstruction obs_1 = kappa * lambda_1, and is the leading coefficient
of the shadow obstruction tower.

ERROR HISTORY (AP1): kappa formulas have been wrong 19 times in this project's
history. Each error propagated to 10-47 files. This engine provides FIVE
independent computation methods for every kappa value, so that any single-method
error is caught by cross-verification.

THE FIVE METHODS:

  Method 1 -- GENUS-1 BAR COMPLEX: kappa = 24 * F_1(A).
    Compute F_1 from the genus-1 graph sum (single vertex, single self-sewing
    edge = torus partition function). Then kappa = F_1 / lambda_1^FP = 24*F_1.

  Method 2 -- OPE RESIDUE / KILLING FORM:
    For Virasoro-type: kappa = (1/2) Res_{z=0} z * <T(z)T(0)> = c/2.
codex
The census is at `CLAUDE.md` §`True Formula Census`; I’ve confirmed the canonical formula block and now I’m drilling into which of those formulas have an actual verifier module versus only manuscript prose. Next step is a direct file-by-file match against `compute/lib/`.
exec
/bin/zsh -lc "sed -n '217,281p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
## True Formula Census

Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).

**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).

**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).

**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).

**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.

**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).

**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).

**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).

**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).

collab wait(call_rf9pixlbfgB81JjMHjnuQq6q)
  receivers: 019d840b-364d-7741-ba2c-62040917528c, 019d840b-3650-70a0-887f-07d355ec5667
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/landscape_census_verification.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Full landscape census verification engine.

Independently recomputes EVERY numerical entry in the landscape census
(chapters/examples/landscape_census.tex) and flags any discrepancy.

Tables verified:
  1. tab:master-invariants — c, c+c', kappa for all families
  2. tab:shadow-tower-census — archetype class, r_max
  3. tab:free-energy-landscape — F_1, F_2, kappa at specific k/c
  4. tab:shadow-invariants-landscape — S_3, S_4, Delta, rho, kappa+kappa'
  5. tab:rmatrix-census — r-matrix pole structure

Anti-pattern coverage:
  AP1  — kappa formulas recomputed from first principles per family
  AP5  — cross-family consistency checks
  AP9  — explicit qualifiers for every kappa
  AP10 — cross-check tests, not single-family hardcodes
  AP24 — complementarity sum NOT assumed zero
  AP39 — S_2 vs kappa explicitly distinguished
  AP48 — kappa != c/2 for general VOAs

thinking
**Summarizing formula census and compute verification**

I'm compiling a concise table listing each C-numbered formula from CLAUDE.md lines 219-281, with columns for line number, formula/topic summary, and any notes about compute verification. I'll highlight entries referencing compute files or verification, especially C16, and note relevant references like C13’s to local .tex files, making sure to present everything clearly in plain text with appropriate file and line references.
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/utils.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""Graded vector spaces, tensor products, cohomological sign conventions.

CONVENTION: This monograph uses COHOMOLOGICAL grading (|d| = +1).
Bar construction uses DESUSPENSION: B(A) = T^c(s^{-1}A-bar, d).
Suspension: sV = V[-1] under V[n]^k = V^{k+n}.
Koszul sign rule: swapping elements of degrees p and q gives (-1)^{pq}.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

import sympy
from sympy import Matrix, Rational, binomial, factorial, bernoulli, zeros


# ---------------------------------------------------------------------------
# Graded vector space
exec
/bin/zsh -lc 'rg -l "verification" compute/lib | grep -i engine' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/bc_euler_product_shadow_engine.py
compute/lib/theorem_thm_d_multiweight_frontier_engine.py
compute/lib/chirhoch_bershadsky_polyakov_engine.py
compute/lib/celestial_arithmetic_engine.py
compute/lib/rectification_delta_f2_verify_engine.py
compute/lib/theorem_abedin_niu_yangian_engine.py
compute/lib/theorem_holographic_c13_entanglement_engine.py
compute/lib/theorem_sklyanin_poisson_cohomology_engine.py
compute/lib/hh_heisenberg_e3_engine.py
compute/lib/cy_lattice_voa_k3_engine.py
compute/lib/theorem_bridgeland_shadow_engine.py
compute/lib/agt_nekrasov_shadow_engine.py
compute/lib/bc_motivic_integration_shadow_engine.py
compute/lib/sc_homotopy_koszul_engine.py
compute/lib/cohft_givental_rmatrix_engine.py
compute/lib/agt_su3_nekrasov_engine.py
compute/lib/theorem_w4_full_ope_delta_f2_engine.py
compute/lib/twisted_holography_engine.py
compute/lib/theorem_bv_sewing_engine.py
compute/lib/bc_bridgeland_stability_engine.py
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/lie_algebra.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
"""Lie algebra data from Cartan matrices.

Provides structure constants, Killing forms, root systems for simple Lie algebras.

CRITICAL DISTINCTION (non-simply-laced):
  h  = Coxeter number (periodicity of bar cohomology)
  h* = dual Coxeter number (Sugawara, FF involution, level shifts)
  For simply-laced: h = h*. Otherwise they differ.

Uses the Chevalley-Serre presentation with structure constants computed
from the Cartan matrix via the Chevalley basis algorithm.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Matrix, Rational, sqrt, eye, sympify

codex
**True Formula Census Location**
- The CLAUDE.md census runs from `CLAUDE.md:219` through `CLAUDE.md:281`, with each C-number’s canonical formula, sanity checks, and forbidden variants spelled out in that block.

C# | Line | Formula / Topic | Compute verification note  
---|---|---|---  
C1 | `CLAUDE.md:221` | Heisenberg kappa: `kappa(H_k)=k`, checked at `k=0` and `k=1`. | –  
C2 | `CLAUDE.md:223` | Virasoro kappa: `kappa(Vir_c)=c/2`, self-dual at `c=13`. | –  
C3 | `CLAUDE.md:225` | Affine KM kappa: `dim(g)(k+h^v)/(2h^v)` with k=0 and `k=-h^v` checks. | –  
C4 | `CLAUDE.md:227` | Principal `W_N` kappa: `c*(H_N-1)` with `H_N=sum_{j=1}^N 1/j`. | –  
C5 | `CLAUDE.md:229` | Fermionic `bc` central charge: `1-3(2λ-1)^2`, lambda-tested. | –  
C6 | `CLAUDE.md:231` | Bosonic `betagamma` central charge: `2(6λ^2-6λ+1)`, lambda-tested. | –  
C7 | `CLAUDE.md:233` | `c_betagamma + c_bc = 0` (ghost complementarity). | –  
C8 | `CLAUDE.md:235` | Vir self-dual point: `kappa+kappa'=13` under `c↦26-c`, fixed at `c=13`. | –  
C9 | `CLAUDE.md:237` | Affine KM classical `r(z)` in trace-form `k*Ω/z` and KZ `Ω/((k+h^v)z)` with bridge and averaging; includes forbidden bare forms. | –  
C10 | `CLAUDE.md:239` | Heisenberg classical `r(z)=k/z`, abelian limit checked. | –  
C11 | `CLAUDE.md:241` | Virasoro classical `r(z)=(c/2)/z^3 + 2T/z`, notes on d-log absorption. | –  
C12 | `CLAUDE.md:243` | Pole absorption rule `pole_r = pole_OPE -1` (Heis 1/z^2→1/z, Vir 1/z^4→1/z^3). | –  
C13 | `CLAUDE.md:245` | Averaging identity; `av(r)` gives double-pole contribution and `dim(g)/2` Sugawara shift; references `kac_moody.tex`, `introduction.tex`, `higher_genus_modular_koszul.tex`. | –  
C14 | `CLAUDE.md:247` | Bar complex uses augmentation ideal: `B(A)=T^c(s^{-1}\bar A)`. | –  
C15 | `CLAUDE.md:249` | Desuspension grading: `|s^{-1}v|=|v|-1`. | –  
C16 | `CLAUDE.md:251` | `E_8` fundamental dimensions list; adjoint `248`; sum `7056003287`. | Verified via `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.  
C17 | `CLAUDE.md:253` | `W_N` weight range: generators in `{2,…,N}`. | –  
C18 | `CLAUDE.md:255` | Koszul complementarity values for each family (`0`, `13`, `250/3`, `196`). | –  
C19 | `CLAUDE.md:257` | Harmonic number definition `H_N = ∑_{j=1}^N 1/j` with AP136 warning. | –  
C20 | `CLAUDE.md:259` | Bershadsky-Polyakov conductor `K_BP = c(k)+c(-k-6)=196`, self-dual `k=-3`. | –  
C21 | `CLAUDE.md:261` | Igusa cusp form weight relation `wt(Φ_10)=10=2*kappa_BKM`. | –  
C22 | `CLAUDE.md:263` | Dedekind eta: `η(τ)=q^{1/24}∏_{n≥1}(1-q^n)` pre-factor required. | –  
C23 | `CLAUDE.md:265` | `1/η^2` coefficients `(1,2,5,10,20,…)` (bicoloured partitions). | –  
C24 | `CLAUDE.md:267` | Cauchy integral normalization `[z^{n-1}]f = (1/(2πi))∮f dz/z^n`; sanity `F_1=kappa/24`. | –  
C25 | `CLAUDE.md:269` | Maurer–Cartan and quantum master equations with 1/2 factors. | –  
C26 | `CLAUDE.md:271` | G/L/C/M classification by `r` and shadow depth. | –  
C27 | `CLAUDE.md:273` | `ChirHoch^*(Vir_c)` supported in degrees `{0,1,2}`; topological amplitude (not virtual dimension). | –  
C28 | `CLAUDE.md:275` | Arnold form vs KZ connection distinction; KZ uses `dz_{ij}` while Arnold uses `dlog`. | –  
C29 | `CLAUDE.md:277` | Genus-1 period matrix collapses: `(Im Ω)^{-1}` scalar at `g=1`, matrix for `g≥2`. | –  
C30 | `CLAUDE.md:279` | Discriminant `Δ=8*kappa*S_4`, linear in `kappa`. | –  
C31 | `CLAUDE.md:281` | BP complementarity `kappa(BP)+kappa(BP^!)=98/3`, `varrho_BP=1/6`; cross-check with `K_BP=196`. | –

Let me know if you’d like extraction of the corresponding “wrong variants” or blacklist references for any entry.
wait(call_rf9pixlbfgB81JjMHjnuQq6q) 1 agents complete:
  019d840b-364d-7741-ba2c-62040917528c completed: "**True Formula Census Location**
- The CLAUDE.md census runs from `CLAUDE.md:219` through `CLAUDE.md:281`, with each C-n…"

exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/f2_kappa_verification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""F_2 = 7*kappa/5760 verification engine for all standard chiral algebra families.

Computes and tabulates the genus-2 free energy F_2 = 7*kappa/5760 across the
standard landscape.  The formula follows from Theorem D (uniform-weight):

    F_g = kappa * lambda_g,    lambda_2 = 7/5760.

(UNIFORM-WEIGHT: scalar formula valid for single-weight families.  Multi-weight
families at g >= 2 require the cross-channel correction delta F_g^cross.)

Families and kappa sources (all from landscape_census.tex, cross-checked
against compute/ engines):

  Heisenberg H_k:        kappa = k                     [C1]
  Virasoro Vir_c:         kappa = c/2                   [C2]
  Affine sl_2 at level k: kappa = dim(sl_2)*(k+h^v)/(2*h^v) = 3(k+2)/4   [C3]
  Principal W_3:          kappa = c*(H_3 - 1) = 5c/6   [C4, H_3 = 11/6]
  Bosonic betagamma:      kappa = c_bg/2 = 6*lam^2 - 6*lam + 1   [C6]
  Free fermion (bc, lam=1/2): kappa = 1/4               [user-specified]
  Leech lattice:          kappa = 24                    [rank-24 even unimodular]
thinking
**Deciding on agents**

I need to think about whether I should compute the inventory with a second agent later. But wait, it looks like I only got a result from the first agent, and maybe the second one's not finished yet. Should I wait again, or should I just open the process to check? It's a little confusing! I'll figure it out step by step; I just want to make sure I get this right.
codex
I’ve got the exact `C1–C31` census block with line anchors. Now I’m matching those entries against concrete verifier code, not filename vibes, so the remaining work is to open the candidate modules and check whether they actually encode the census formulas.
collab wait(call_YF1nKvRIQtbeZySX06TQSXvP)
  receivers: 019d840b-3650-70a0-887f-07d355ec5667
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/rectification_delta_f2_verify_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Independent verification engine for delta_F_2^{grav}(W_N).

ADVERSARIAL RED-TEAM VERIFICATION of the claim:

    delta_F_2^{grav}(W_N, c) = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c)

This engine is built FROM SCRATCH with ZERO imports from the multi-weight
cross-channel engine. Every computation is independent.

MATHEMATICAL SETUP
==================

The genus-2 stable graph sum for the gravitational-only W_N Frobenius
algebra computes:

    F_2(W_N, c) = sum_{Gamma} (1/|Aut(Gamma)|)
                  * sum_{sigma: E(Gamma) -> {2,3,...,N}} A(Gamma, sigma)

where A(Gamma, sigma) is the product of:
  - Propagators: prod_e  w(sigma(e)) / c   where w(j) = conformal weight j

thinking
**Preparing module inventory summary**

I'm putting together a clear, bullet-pointed list of key verification modules and helper libraries with clickable file paths including line numbers, focusing on canonical formulas and verification engines as requested. This will provide a neat overview referencing docstrings without adding unnecessary planning details.
codex
- `compute/lib/true_formula_census_verifier.py:1` – standalone engine that recomputes every canonical “True Formula Census” entry (the C1–C10 canonical kappa/central-charge/harmonic-number/complementarity data) with exact rational arithmetic and flags any drift; docstring lists the AP-n anti‑patterns it guards, so it is clearly an explicit formula verifier.  
- `compute/lib/kappa_cross_verification.py:1` – adversarial engine that recomputes every family’s modular characteristic κ via five totally independent routes (genus‑1 bar complex, OPE residue, character asymptotics, shadow metric, complementarity) and insists that all routes agree; it acts as a cross-check harness for the kappa formulas.  
- `compute/lib/landscape_census_verification.py:1` – megascope that recomputes every table in `chapters/examples/landscape_census.tex` (master invariants, shadow towers, free energies, r‑matrices, etc.) using independent central charge/κ computations and reports discrepancies, so it is the master verification engine for the published census.  
- `compute/lib/f2_kappa_verification_engine.py:1` – focused verifier for the genus‑2 relation \(F_2 = 7\kappa/5760\); it tabulates that formula across Heisenberg, Virasoro, affine, W_3, betagamma, free-fermion, and Leech lattice families with exact arithmetic and logs the cross-checks noted in the docstring.  
- `compute/lib/rectification_delta_f2_verify_engine.py:1` – independent red-team that reconstructs the full genus‑2 stable graph sum for the gravitational W_N Frobenius algebra from scratch, confirming the stated \(\delta F_2^{\mathrm{grav}}(W_N,c)\) formula without reusing the main multi-weight engine; it even derives Bernoulli numbers and graph automorphisms internally.  
- Helper libraries: `compute/lib/utils.py:1` supplies graded-vector-space, chain-complex, Koszul-sign, Bernoulli, and partition-number utilities that the verifiers reuse, while `compute/lib/lie_algebra.py:1` provides Cartan matrices, root-system data, and Killing-form offsets needed to keep the affine/Virasoro/W family calculations consistent.
wait(call_YF1nKvRIQtbeZySX06TQSXvP) 1 agents complete:
  019d840b-3650-70a0-887f-07d355ec5667 completed: "- `compute/lib/true_formula_census_verifier.py:1` – standalone engine that recomputes every canonical “True Formula Cens…"

thinking
**Verifying claimed files**

I think it’s interesting that there are agent claims about certain files needing verification. It seems likely that there are modules to check. I might need to inspect these candidate modules manually since I can’t fully trust the agent — there’s a chance it could be hallucinating. Although, the explorer is authoritative. The user wants actual file contents, so I'll open these files and use the command to filter for specific contents.
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/kappa_cross_verification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/true_formula_census_verifier.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/landscape_census_verification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files compute/lib | rg 'true_formula_census_verifier|kappa_cross_verification|landscape_census_verification|f2_kappa_verification_engine|utils\\.py|lie_algebra\\.py"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Cross-verification engine for the modular characteristic kappa(A).

kappa(A) is the single most important invariant in the modular Koszul duality
programme: it appears in F_g = kappa * lambda_g^FP at ALL genera, controls the
genus-1 obstruction obs_1 = kappa * lambda_1, and is the leading coefficient
of the shadow obstruction tower.

ERROR HISTORY (AP1): kappa formulas have been wrong 19 times in this project's
history. Each error propagated to 10-47 files. This engine provides FIVE
independent computation methods for every kappa value, so that any single-method
error is caught by cross-verification.

THE FIVE METHODS:

  Method 1 -- GENUS-1 BAR COMPLEX: kappa = 24 * F_1(A).
    Compute F_1 from the genus-1 graph sum (single vertex, single self-sewing
    edge = torus partition function). Then kappa = F_1 / lambda_1^FP = 24*F_1.

  Method 2 -- OPE RESIDUE / KILLING FORM:
    For Virasoro-type: kappa = (1/2) Res_{z=0} z * <T(z)T(0)> = c/2.
 succeeded in 53ms:
"""True Formula Census verification engine.

Independently recomputes the canonical Wave 12-2 formulas used in the
standard landscape census and cross-checks them against the census values.

Checks covered:
  C01. kappa(Heis_k) = k
  C02. kappa(Vir_c) = c/2
  C03. kappa(V_k(g)) = dim(g) * (k + h^vee) / (2 * h^vee)
  C04. kappa(W_N) = c * (H_N - 1)
  C05. c_bc(lambda) = 1 - 3 * (2 * lambda - 1)^2
  C06. c_bg(lambda) = 2 * (6 * lambda^2 - 6 * lambda + 1)
  C07. E_8 fundamental irrep dimensions
  C08. H_N = sum_{j=1}^N 1/j exactly
  C09. Complementarity sums by family
  C10. K_BP = 196 for Bershadsky-Polyakov W_3^(2)

Anti-pattern coverage:
  AP1   family-specific kappa formulas
  AP24  complementarity is not universal across families
 succeeded in 50ms:
compute/lib/true_formula_census_verifier.py
compute/lib/kappa_cross_verification.py
compute/lib/utils.py
compute/lib/landscape_census_verification.py
compute/lib/f2_kappa_verification_engine.py
compute/lib/lie_algebra.py
 succeeded in 51ms:
r"""Full landscape census verification engine.

Independently recomputes EVERY numerical entry in the landscape census
(chapters/examples/landscape_census.tex) and flags any discrepancy.

Tables verified:
  1. tab:master-invariants — c, c+c', kappa for all families
  2. tab:shadow-tower-census — archetype class, r_max
  3. tab:free-energy-landscape — F_1, F_2, kappa at specific k/c
  4. tab:shadow-invariants-landscape — S_3, S_4, Delta, rho, kappa+kappa'
  5. tab:rmatrix-census — r-matrix pole structure

Anti-pattern coverage:
  AP1  — kappa formulas recomputed from first principles per family
  AP5  — cross-family consistency checks
  AP9  — explicit qualifiers for every kappa
  AP10 — cross-check tests, not single-family hardcodes
  AP24 — complementarity sum NOT assumed zero
  AP39 — S_2 vs kappa explicitly distinguished
  AP48 — kappa != c/2 for general VOAs

thinking
**Checking coverage and formulas**

I need to assess the coverage and identify any missing formulas. This could involve inspecting the f2 engine for potential gaps or details I might have overlooked. It's crucial to ensure everything is accounted for, so I’ll delve into the various elements involved. I want to make sure that I don’t overlook anything important in this process. Let's explore each aspect carefully to see what’s there!
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/f2_kappa_verification_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/lie_algebra.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' compute/lib/bc_exceptional_categorical_zeta_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""F_2 = 7*kappa/5760 verification engine for all standard chiral algebra families.

Computes and tabulates the genus-2 free energy F_2 = 7*kappa/5760 across the
standard landscape.  The formula follows from Theorem D (uniform-weight):

    F_g = kappa * lambda_g,    lambda_2 = 7/5760.

(UNIFORM-WEIGHT: scalar formula valid for single-weight families.  Multi-weight
families at g >= 2 require the cross-channel correction delta F_g^cross.)

Families and kappa sources (all from landscape_census.tex, cross-checked
against compute/ engines):

  Heisenberg H_k:        kappa = k                     [C1]
  Virasoro Vir_c:         kappa = c/2                   [C2]
  Affine sl_2 at level k: kappa = dim(sl_2)*(k+h^v)/(2*h^v) = 3(k+2)/4   [C3]
  Principal W_3:          kappa = c*(H_3 - 1) = 5c/6   [C4, H_3 = 11/6]
  Bosonic betagamma:      kappa = c_bg/2 = 6*lam^2 - 6*lam + 1   [C6]
  Free fermion (bc, lam=1/2): kappa = 1/4               [user-specified]
  Leech lattice:          kappa = 24                    [rank-24 even unimodular]
 succeeded in 53ms:
"""Lie algebra data from Cartan matrices.

Provides structure constants, Killing forms, root systems for simple Lie algebras.

CRITICAL DISTINCTION (non-simply-laced):
  h  = Coxeter number (periodicity of bar cohomology)
  h* = dual Coxeter number (Sugawara, FF involution, level shifts)
  For simply-laced: h = h*. Otherwise they differ.

Uses the Chevalley-Serre presentation with structure constants computed
from the Cartan matrix via the Chevalley basis algorithm.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Matrix, Rational, sqrt, eye, sympify

 succeeded in 51ms:
r"""Categorical zeta functions for exceptional Lie types G₂, F₄, E₆, E₇, E₈.

Mathematical foundation
-----------------------
For each simple Lie algebra g, the categorical zeta function of the
Drinfeld-Kohno category is the Dirichlet series:

    ζ^{DK}_g(s) = Σ_{λ dominant, V_λ nontrivial} dim(V_λ)^{-s}

This module implements the Weyl dimension formula and categorical zeta
for the five exceptional simple Lie algebras, extending bc_categorical_zeta_engine.py
(which handles types A, B, C, D) to the exceptional types.

Key structural data:
    G₂: rank 2, |Φ⁺| = 6,  σ_c = 2/6  = 1/3
    F₄: rank 4, |Φ⁺| = 24, σ_c = 4/24 = 1/6
    E₆: rank 6, |Φ⁺| = 36, σ_c = 6/36 = 1/6
    E₇: rank 7, |Φ⁺| = 63, σ_c = 7/63 = 1/9
    E₈: rank 8, |Φ⁺| = 120, σ_c = 8/120 = 1/15








thinking
**Mapping compute engines**

I realize we have a lot of relevant modules to consider. I need to create an exhaustive mapping from C1 to C31 to verify computation and library verification. It's essential to determine which engines are missing. I might use search commands to map the C numbers or relevant formulas to specific files and create an internal table for tracking.

The user wants detailed findings on each census formula's missing engine. Some might already have engines while others don't, so this needs to be thorough and accurate. I need to inspect all candidate files, keeping in mind that with 31 formulas, many may lack a compute engine. I need to confirm whether each engine exists or not.
thinking
**Identifying engine issues**

I need to consider that there could be existing engines that are incomplete or incorrect. I should identify second-order failures where the engine is present but doesn't adequately cover the formula or boundary checks. There might be mistakes with labeled C numbers or formulas as well.

To tackle this, I'll likely run `grep` across the compute/library for both formulas and C numbers. I might build a clear mapping from C1 to C31 for thorough checks. Using regex keywords makes sense, and perhaps leveraging a shell script could simplify the process instead of Python, especially since the developer recommended against using Python for read/write tasks.
thinking
**Mapping with shell tools**

I think mapping the 31 items might work well with a shell tool like `rg`, though a script could potentially make things easier. I can use a command like `rg -n "C01|C1|kappa\(Heis|..."` in the compute/lib directory. I want to ensure the search isn’t overly extensive, so I could adjust it to `rg -n "C0[1-9]|C1[0-9]|C2[0-9]|C3[01]"`.

However, since formulas might not always cite C numbers, I may need to do a keyword search focused on canonical formula strings. I could also consider using a shell loop for better efficiency. I just need to ensure I get actual results.
thinking
**Building a verification matrix**

I think we need to create a matrix for verification. It seems that C1 to C4 are likely handled by true_formula_census_verifier, kappa_cross_verification, and landscape_census_verification. For C5 to C7, the true_formula_census_verifier might cover central charges, along with landscape_census_verification. C8's verification could involve true_formula_census_verifier, possibly relating to complementarity with Virasoro dual c, and landscape_census as well. As for C9, it might relate to an affine KM r-matrix, so I should check if a compute engine can verify that.
thinking
**Searching for mathematical references**

I’m looking into various mathematical concepts and potentially relevant files. For C22, I want to find something related to the Dedekind eta function, like `ramanujan_verifications.py` or `1/eta`. Then for C23, I need to explore bicoloured partitions, possibly using `lattice_shadow.py` or something similar. As for C24, I'm considering normalization linked to the Cauchy integral, which might connect with `bc_explicit_formula_engine.py`. Finally, for C25, I’ll need to verify mechanics involving multiple MC engines, referencing files like `convolution_linf_algebra.py` and others.
thinking
**Deciding on formula mapping**

I’m considering that if a formula is missing a corresponding engine, I should flag it. It might make sense to group findings like C11-C13 together due to the same missing r-matrix verifier. However, it could be more thorough to report one finding per missing engine or formula cluster. I really need to make a decision on this. Also, I plan to inspect the compute files using rg.
thinking
**Searching for references**

I need to find the exact presence of keywords. Using regex on each C number could be the easiest approach. I’ll start by searching for references between C11 and C31 in the known modules. That could help me pinpoint what I’m looking for and streamline the process. It's essential to get this right to ensure I have accurate data at hand, so I'll focus on these ranges carefully.
codex
I’ve confirmed the repo already has a dedicated census verifier, but its own docstring stops at `C10`. I’m now checking whether later census entries are covered elsewhere by actual code, or only by broad claims like “every numerical entry” in secondary engines.
exec
/bin/zsh -lc "rg -n \"k\\*Omega/z|Omega/\\(\\(k\\+h\\"'^v'"\\)\\*z\\)|r\\"'^Heis|r'"\\"'^Vir|pole_r = pole_OPE - 1|T'"\\"'^c'"\\(s\\"'^{-1} A-bar'"\\)|\\|s\\"'^{-1} v'"\\| = \\|v\\| - 1|\\{2, 3, \\.\\.\\., N\\}|Phi_10|q\\"'^'"\\{1/24\\}|1/eta\\"'^2|2'"\\*pi\\*i|d\\*Theta \\+ \\(1/2\\)\\[Theta, Theta\\]|ChirHoch\\"'^'"\\*\\(Vir|d log\\(z_i-z_j\\)|Im Omega|Delta = 8|98/3|196|7056003287\" compute/lib" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "C0?1|C0?2|C0?3|C0?4|C0?5|C0?6|C0?7|C0?8|C0?9|C10|C11|C12|C13|C14|C15|C16|C17|C18|C19|C20|C21|C22|C23|C24|C25|C26|C27|C28|C29|C30|C31" compute/lib' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:k\*Omega/z|Omega/\(\(k\+h\^v\)\*z\)|r\^Heis|r\^Vir|pole_r = pole_OPE - 1|T\^c\(s\^{-1} A-bar\)|\|s\^{-1} v\| = \|v\| - 1|\{2, 3, \.\.\., N\}|Phi_10|q\^\{1/24\}|1/eta\^2|2\*pi\*i|d\*Theta \+ \(1/2\)\[Theta, Theta\]|ChirHoch\^\*\(Vir|d log\(z_i-z_j\)|Im Omega|Delta = 8|98/3|196|7056003287)
                                                                                          ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
Total output lines: 1858

compute/lib/knot_invariant_shadow_engine.py:13:via MC3):
compute/lib/knot_invariant_shadow_engine.py:74:* concordance.tex: MC3 (DK bridge)
compute/lib/mc5_higher_genus.py:1:"""MC5 higher-genus bridge: unified module for BV/BRST = bar at genus g >= 2.
compute/lib/mc5_higher_genus.py:38:  concordance.tex (Front F, MC5), higher_genus_foundations.tex,
compute/lib/mc5_higher_genus.py:410:    MC5-RED: this is NEGATIVE for ALL g >= 2 (lambda_g decreasing).
compute/lib/theorem_thm_d_multiweight_frontier_engine.py:118:def grav_C3(i: int, j: int, k: int, c: Fraction) -> Fraction:
compute/lib/theorem_thm_d_multiweight_frontier_engine.py:151:        return grav_C3(channels[0], channels[1], channels[2], c)
compute/lib/theorem_thm_d_multiweight_frontier_engine.py:156:        c3 = grav_C3(a, b, m, c)
compute/lib/mc5_disk_local.py:1:"""MC5 disk-local packet: BV-BRST = bar at the chain level on C₂ and C₃.
compute/lib/mc5_disk_local.py:47:def bar_differential_C2(ope_coeffs: Dict[int, object]) -> Dict[int, object]:
compute/lib/mc5_disk_local.py:62:def brst_bracket_C2(ope_coeffs: Dict[int, object]) -> Dict[int, object]:
compute/lib/mc5_disk_local.py:77:def verify_C2_identification(ope_coeffs: Dict[int, object]) -> Dict[str, object]:
compute/lib/mc5_disk_local.py:79:    bar = bar_differential_C2(ope_coeffs)
compute/lib/mc5_disk_local.py:80:    brst = brst_bracket_C2(ope_coeffs)
compute/lib/mc5_disk_local.py:100:def bar_differential_C3_arnold(
compute/lib/mc5_disk_local.py:140:def brst_bracket_C3(
compute/lib/mc5_disk_local.py:169:def verify_C3_identification(
compute/lib/mc5_disk_local.py:175:    bar = bar_differential_C3_arnold(ope_ab, ope_bc, ope_ac)

thinking
**Narrowing keyword searches**

I need to narrow down my approach a bit. I'm considering creating a mapping script that uses shell to search for candidate keywords and count the files. I can use `rg -n -F` to run searches separately, perhaps with shell arrays to organize things. Then, I might apply `nl -ba` on a selected set of candidate files. I could also run targeted queries like `rg -n -F "q^{1/24}" compute/lib` to be more precise.
codex
The first pass already found real coverage for some later census items, but it also exposed a likely structural hole: broad “landscape” engines cover many numerical tables, while several canonical formulas are structural and may have no dedicated verifier at all. I’m separating the audit into verified coverage, partial coverage, and genuinely missing lanes now.
exec
/bin/zsh -lc 'rg -n -F "1/eta''^2" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "ChirHoch''^*(Vir_c)" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "d*Theta + (1/2)[Theta, Theta]" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "q''^{1/24}" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "2*pi*i" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Im Omega" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/cy_modular_k3e_engine.py:848:    d(1) = 36 ... NO, these are from 1/eta^24 * 1/phi_{10,1}.
compute/lib/cy_bps_spectrum_k3e_engine.py:779:    # at Delta = 4n. But psi_1 is NOT simply 1/eta^24 — it receives
compute/lib/bc_niemeier_l_values_engine.py:332:    We need: Z = Theta * (1/eta^24).
compute/lib/bc_niemeier_l_values_engine.py:333:    1/eta^24 = q^{-1}/prod(1-q^m)^{24} = q^{-1} * sum_n p_{-24}(n) q^n
compute/lib/critical_line_atlas.py:941:      d_arith = 1 (the partition function 1/eta^2 is quasi-modular)
compute/lib/critical_line_atlas.py:960:            {'position': Fraction(1, 2), 'source': 'zeta(s) from 1/eta^2'},
compute/lib/bicoloured_partition_engine.py:1:r"""Bicoloured partition numbers and 1/eta^2 q-expansion engine.
compute/lib/bicoloured_partition_engine.py:81:# Bicoloured partition numbers p_{-2}(n) = coefficients of 1/eta^2
compute/lib/darith_full_landscape_engine.py:344:            "Path1: Z = 1/eta^2 (up to q-power): single eta quotient",
compute/lib/shadow_kloosterman_engine.py:15:   The Rademacher expansion of 1/eta^24 involves Kloosterman sums Kl(n,1;c).
compute/lib/shadow_kloosterman_engine.py:706:    For 1/eta^24: nu = 11 (weight 12 - 1 = 11), m = -1 (polar term).
 succeeded in 50ms:
compute/lib/theorem_thm_h_e3_rectification_engine.py:305:    ChirHoch^*(Vir_c) is CONCENTRATED in degrees {0, 1, 2}
compute/lib/chiral_hochschild_engine.py:571:    NOTE: Per Theorem H (AP94/AP95), ChirHoch^*(Vir_c) is
compute/lib/chiral_hochschild_engine.py:575:    (ChirHoch^*(Vir_c) = C[Theta] with |Theta|=2, unbounded)
compute/lib/chriss_ginzburg_universal.py:630:            # model (ChirHoch^*(Vir_c) = C[Theta], unbounded) is
 succeeded in 50ms:
compute/lib/wild_quiver_chiral_engine.py:706:    d*Theta + (1/2)[Theta, Theta] = 0 has NO SOLUTION in the formal
 succeeded in 50ms:
Total output lines: 265

compute/lib/cy_lattice_voa_k3_engine.py:116:  - eta(q) = q^{1/24} * prod_{n>=1}(1-q^n) (AP46: include q^{1/24})
compute/lib/mock_modular_admissible_engine.py:82:  - eta(tau) = q^{1/24} prod(1-q^n)  (AP46: q^{1/24} is NOT optional)
compute/lib/mock_modular_admissible_engine.py:274:    This is the PRODUCT part of eta(tau) = q^{1/24} * prod(1-q^n).
compute/lib/k3_relative_chiral.py:77:  - eta(q) = q^{1/24} * prod(1-q^n) (AP46: include q^{1/24})
compute/lib/k3_relative_chiral.py:1234:    Meanwhile, 1/eta(q)^{24} = q^{-1} * prod(1-q^k)^{-24} (AP46: eta includes q^{1/24}).
compute/lib/elliptic_genus_deep_engine.py:47:  - eta(q) = q^{1/24} * prod_{n>=1}(1 - q^n)  [AP46: include q^{1/24}!]
compute/lib/elliptic_genus_deep_engine.py:133:    r"""Coefficients c[n] of eta(tau) = q^{1/24} * sum c[n] q^n.
compute/lib/cy_mathieu_moonshine_engine.py:58:  - eta(q) = q^{1/24} * prod(1 - q^n)  [AP46: include q^{1/24}]
compute/lib/cy_mathieu_moonshine_engine.py:287:    Note: eta(tau) = q^{1/24} * prod(1-q^n) (AP46).
compute/lib/cy_mathieu_moonshine_engine.py:288:    This returns the product WITHOUT the q^{1/24} prefactor.
compute/lib/bc_langlands_reciprocity_shadow_engine.py:318:    WARNING (AP46): eta(q) = q^{1/24} prod_{n>=1}(1-q^n).  The q^{1/24}
compute/lib/cy_wallcrossing_engine.py:117:- eta(q) = q^{1/24} * prod(1-q^n) (AP46)
compute/lib/cy_wallcrossing_engine.py:124:AP46: eta(q) includes q^{1/24}; never drop this factor.
compute/lib/cy_wallcrossing_engine.py:1507:    NOTE: eta(q)^{24} = q * prod(1-q^n)^{24} (from eta = q^{1/24} prod(1-q^n), AP46).
compute/lib/offdiag_newton_test.py:30:  (up to q^{1/24} normalization; z is the off-diagonal sewing parameter).
compute/lib/factorization_homology_explicit_engine.py:357:    Heisenberg H_1 in d=1: chi(q) = q^{1/24} * 1/eta(q) (with the c/24 factor)
compute/lib/factorization_homology_explicit_engine.py:358:                                  = 1/phi(q) (Euler function) up to q^{1/24}
compute/lib/bv_bar_class_m_engine.py:41:  - eta(q) = q^{1/24} * prod(1-q^n) (AP46: q^{1/24} is NOT optional)
 succeeded in 50ms:
compute/lib/bv_bar_genus2_comparison.py:34:    log det'(Delta_{Sigma_2}) = genus-independent + (1/6) log det(Im Omega)
compute/lib/bv_bar_genus2_comparison.py:479:    # Z_2(Heis) = det(Im Omega)^{k/2} * |chi_10(Omega)|^{-k/...}
compute/lib/coderived_artifact.py:21:  Z_exact = (det Im Omega)^{-1/2} (det'_zeta Delta)^{-1/2} for Heisenberg.
compute/lib/coderived_artifact.py:755:    Z_2 = 1 / |det(Im Omega_2)|^c * |Phi_{10}(Omega_2)|^{-c/5}
compute/lib/coderived_artifact.py:758:    and det(Im Omega_2) is the determinant of the imaginary part
compute/lib/coderived_artifact.py:762:    Z_2 = Theta_Siegel(Omega_2)^{2c} / (det(Im Omega_2))^{c/2} / (some normalization)
compute/lib/coderived_artifact.py:777:    # Z_2 = |theta|^{2c} / det(Im Omega)^{c/2}
compute/lib/coderived_artifact.py:865:    - Genus 2: Z_2 = Theta_Siegel^{2c} / det(Im Omega)^{c/2}, depends on 3 complex parameters
compute/lib/genus2_unfolding_erasure.py:321:      Z_2(Omega) = (det Im Omega)^{-k/2} * det(1 - K_Bergman)^{-k}
compute/lib/genus2_unfolding_erasure.py:645:      Z_2(Omega) = det(Im Omega)^{-k/2} / prod_{n>=1} det(1 - q1^n ... )^k
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:234:      P_harm = sum_{i,j} (Im Omega)^{-1}_{ij} omega_i(z) * bar{omega_j(w)}
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:978:      P_harm = sum_{i,j=1}^{2} (Im Omega)^{-1}_{ij} omega_i(z) omega_j(w)
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:1045:                'proportional to (Im Omega)^{-1}_{ij}. '
compute/lib/theorem_mc5_analytic_rectification_engine.py:16:    Z_g(H_k) = det(Im Omega)^{-k/2} * |det'_zeta Delta|^{-k}
compute/lib/theorem_mc5_analytic_rectification_engine.py:35:      Z_g(H_r; Omega) = det(Im Omega)^{-r/2}
compute/lib/theorem_mc5_analytic_rectification_engine.py:415:    """Genus-2 Heisenberg via the Siegel theta / det(Im Omega) formula.
compute/lib/theorem_mc5_analytic_rectification_engine.py:418:      Z_g^{full}(H_r; Omega) = det(Im Omega)^{-r/2}
compute/lib/theorem_mc5_analytic_rectification_engine.py:423:    At genus 2, Omega is 2x2 and det(Im Omega) = product of eigenvalues
compute/lib/theorem_mc5_analytic_rectification_engine.py:461:    3. Siegel theta / det(Im Omega)
compute/lib/theorem_nafcha_gluing_engine.py:392:      Z_2(H_k) = (det Im Omega_2)^{-k/2} * (det'_zeta Delta_{Sigma_2})^{-k/2}
 succeeded in 52ms:
Total output lines: 963

compute/lib/cy_mathieu_moonshine_engine.py:57:  - q = e^{2*pi*i*tau}, y = e^{2*pi*i*z}
compute/lib/cy_mathieu_moonshine_engine.py:1092:    cover (since eta(tau+1) = e^{2*pi*i/24} * eta(tau)).
compute/lib/cy_n4sca_k3_engine.py:96:  - q = e^{2*pi*i*tau}, y = e^{2*pi*i*z}
compute/lib/moonshine_shadow_depth.py:695:      J(tau) = sum_{c>0, -c<d<=0, (c,d)=1} e^{-2*pi*i*(a*tau+b)/(c*tau+d)} / (c*tau+d)^0
compute/lib/rademacher_kloosterman.py:86:    K(m, n; c) = Sum_{d mod c, gcd(d,c)=1} exp(2*pi*i*(m*d + n*d')/c)
compute/lib/rademacher_kloosterman.py:144:    factors as exp(2*pi*i*(m*d+n*d')/(c1*c2)) = exp(2*pi*i*(m*\bar{c2}*d1+n*\bar{c2}*d1')/c1)
compute/lib/rademacher_kloosterman.py:145:                                                * exp(2*pi*i*(m*\bar{c1}*d2+n*\bar{c1}*d2')/c2).
compute/lib/rademacher_kloosterman.py:381:    K^rho_{ij}(m,n;c) = Sum_{d mod c, (c,d)=1} rho(gamma)_{ij} * e^{2*pi*i*(m*d + n*a)/c}
compute/lib/rademacher_kloosterman.py:419:    # T = diag(e^{2*pi*i*(h_k - c_eff/24)})
compute/lib/rademacher_kloosterman.py:436:        # the key is the phase e^{2*pi*i*(m*d_val + n*a)/c}.
compute/lib/rademacher_kloosterman.py:440:        #   K^rho_{ij}(m,n;c) = Sum_{d} [rho(S)]_{ij} * e^{2*pi*i*(m*d + n*d')/c}
compute/lib/rademacher_kloosterman.py:536:    K_c(alpha, beta) = Sum_{d mod c, gcd(d,c)=1} e^{2*pi*i*(alpha*d + beta*d')/c}
compute/lib/rademacher_kloosterman.py:648:        # For the Ising model, the vacuum character in q-expansion with q = e^{2*pi*i*tau}:
compute/lib/modular_forms_shadow_engine.py:62:  q = e^{2*pi*i*tau}
compute/lib/modular_forms_shadow_engine.py:156:                 = -(kappa/24) * 2*pi*i*tau + kappa * sum_{m>=1} sigma_{-1}(m) q^m
compute/lib/modular_forms_shadow_engine.py:180:    # d/dtau log eta = -(1/24) E_2*(tau) (up to 2*pi*i factor)
compute/lib/modular_forms_shadow_engine.py:183:    # More precisely: (2*pi*i)^{-1} d/dtau (-kappa * log eta)
compute/lib/modular_forms_shadow_engine.py:493:    The Serre derivative is theta = q d/dq = (1/(2*pi*i)) d/dtau.



thinking
**Collecting candidate files**

I'm looking at search results to find relevant files for missing formulas. For C22, the Dedekind eta has many engines, and I need to decide if there's a specific compute engine that verifies the formula. For C23, there's a file named `bicoloured_partition_engine.py` that I should inspect. C24 has the term `2*pi*i` appearing many times, but I might need to search for a more targeted term to avoid overwhelming results. I'll try using specific search commands for better accuracy.
thinking
**Exploring Cauchy Normalization Verification**

I need to check if any module explicitly verifies Cauchy normalization. It seems the MC equation might only be mentioned in the wild_quiver file, rather than having a dedicated generic verifier. I should confirm there's no exact engine by searching the compute/lib directory. I might open the convolution_linf_algebra.py file next and search for the MC equation.

It could be helpful to create a compact dataset of candidate coverage, perhaps using shell loops or targeted grep to inspect key files relevant to various conditions.
thinking
**Inspecting Key Engines**

I need to inspect several files to see if they relate to specific classifications. For example, the theorem_concordance_rectification_engine.py might relate to C26, so I should check around the class map. The bc_twisted_holography_zeta_engine.py could potentially correspond to C22, but that might be an overreach. 

I also plan to check moonshine_kappa_resolution_engine.py and cy_elliptic_genus_k3e_engine.py for information on C21, especially searching for `kappa_BKM = 5`. Additionally, I’ll look for `98/3` and `196`, using targeted queries for these keywords.
exec
/bin/zsh -lc 'rg -n -F "kappa_BKM" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "98/3" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "{2, 3, ..., N}" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "H_N - 1" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Phi_10" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "G/L/C/M" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/twisted_sugra_shadow_engine.py:304:      kappa(A) = 3, kappa_BCOV = 0, kappa_MacMahon = 0, kappa_BKM = 5.
compute/lib/twisted_sugra_shadow_engine.py:334:    (iv)  kappa_BKM: weight of automorphic form (for K3-fibered)
 succeeded in 51ms:
compute/lib/theorem_thm_d_multiweight_frontier_engine.py:834:    which depends only on the CONFORMAL WEIGHT SPECTRUM {2, 3, ..., N},
compute/lib/rectification_delta_f2_verify_engine.py:254:    Channels are labeled by conformal weights: i, j, k in {2, 3, ..., N}.
compute/lib/dirichlet_sewing.py:187:    Weight multiset W = {2, 3, ..., N}, so
compute/lib/analytic_langlands_shadow_engine.py:615:    parts from {d_1, ..., d_{N-1}} = {2, 3, ..., N}.
compute/lib/penner_matrix_model_delta_f2_engine.py:15:{h_1, h_2, ..., h_{N-1}} = {2, 3, ..., N} of the W_N generators.
compute/lib/penner_matrix_model_delta_f2_engine.py:36:where the eigenvalues are FIXED at the conformal weights {2, 3, ..., N}:
compute/lib/penner_matrix_model_delta_f2_engine.py:45:supported at {2, 3, ..., N}. This suggests that delta_F_2 is the
compute/lib/penner_matrix_model_delta_f2_engine.py:261:    For eigenvalues {2, 3, ..., N}:
compute/lib/euler_koszul_engine.py:116:    """W_N algebra: W = {2, 3, ..., N}."""
compute/lib/complementarity_cross_verification.py:385:    For W_N: weights {2, 3, ..., N}, kappa_ghost = -sum_{h=2}^N (6h^2-6h+1).
compute/lib/complementarity_cross_verification.py:395:    """Generator conformal weights for principal W_N: {2, 3, ..., N}."""
compute/lib/quartic_residue_engine.py:281:    Strong generators have weights {2, 3, ..., N}.
compute/lib/quartic_residue_engine.py:794:    """Weight multiset for W_N: {2, 3, ..., N}."""
compute/lib/e8_koszul_conductor_engine.py:34:For sl_N: spins = {2, 3, ..., N}, so varrho = H_N - 1 = sum_{j=2}^{N} 1/j.
compute/lib/galois_cross_channel_engine.py:884:    A triple (W_i, W_j, W_k) with i, j, k in {2, 3, ..., N} is:
compute/lib/a2_polynomial_combinatorics_engine.py:20:weights {2, 3, ..., N} of the W_N generators.
compute/lib/delta_f4_engine.py:15:  2. For each graph, summing over channel assignments {2, 3, ..., N}^{|E|}
compute/lib/delta_f4_engine.py:41:weights {2, 3, ..., N}. The power sums S_k = sum_{j=2}^{N} j^k
compute/lib/delta_f4_engine.py:459:        N: rank of W_N algebra (channels are {2, 3, ..., N})
compute/lib/ds_arithmetic_defect.py:247:    For sl_N: {2, 3, ..., N} (Virasoro at N=2, W_3 at N=3, etc.).
 succeeded in 51ms:
compute/lib/sl3_subregular_bar.py:37:  Path 3 (complementarity): kappa(k) + kappa(-k-6) = rho * K_BP = 98/3, with K_BP = 196.
compute/lib/sl3_subregular_bar.py:193:    K_BP = 196 (constant). rho = 1/6. So the sum = 98/3.
compute/lib/sl3_subregular_bar.py:196:    Given kappa(k') = rho * c(k'), we can solve for kappa(k) = 98/3 - kappa(k').
compute/lib/sl3_subregular_bar.py:282:    The kappa sum: kappa(k) + kappa(k') = 98/3 = rho * K.
compute/lib/sl3_subregular_bar.py:299:        "kappa_sum_value": Rational(98, 3),  # AP140: corrected from 1/3; (1/6)*196=98/3
compute/lib/sl3_subregular_bar.py:680:    # AP140: corrected from 1/3 to 98/3
compute/lib/sl3_subregular_bar.py:681:    results["kappa sum = 98/3"] = simplify(dual["kappa_sum"] - Rational(98, 3)) == 0
compute/lib/theorem_w_algebra_chapter_rectification_engine.py:174:    kappa(k) + kappa(k') = 196/6 = 98/3.
compute/lib/ds_bar_commutation.py:594:    # Kappa sum = 98/3 = rho*K_BP = (1/6)*196
compute/lib/ds_bar_commutation.py:595:    results["sl_3 minimal: kappa sum = 98/3"] = (
compute/lib/ds_bar_commutation.py:641:    results["sl_3 Koszul dual: kappa sum = 98/3"] = simplify(kd_21.kappa_sum - Rational(98, 3)) == 0
compute/lib/theorem_ap49_superconformal_engine.py:10:  BP   (W(sl3,fmin)):kappa = c/6,         k -> -k-6,    comp sum = 98/3 (FKR conv)
compute/lib/theorem_ap49_superconformal_engine.py:305:    """kappa(k) + kappa(-k-6) = varrho * K = 196/6 = 98/3."""
compute/lib/theorem_ap49_superconformal_engine.py:587:    Path 3: Complementarity sum = 98/3
compute/lib/bp_koszul_conductor_engine.py:23:    kappa_BP(k) + kappa_BP(-k-6) = varrho_BP * K_BP = 98/3
compute/lib/bp_koszul_conductor_engine.py:78:# Kappa complementarity sum: varrho * K = (1/6) * 196 = 98/3.
compute/lib/bp_koszul_conductor_engine.py:79:# VERIFIED: [DC] (1/6) * 196 = 98/3;
compute/lib/bp_koszul_conductor_engine.py:80:# [LT] chapters/examples/bershadsky_polyakov.tex, eq. `eq:bp-complementarity`, gives 98/3.
compute/lib/bp_koszul_conductor_engine.py:156:    r"""Kappa complementarity: kappa_BP(k) + kappa_BP(-k-6) = varrho * K_BP = 98/3."""
compute/lib/bp_koszul_conductor_engine.py:159:    # [CF] equals varrho_BP * K_BP = 98/3.
 succeeded in 50ms:
Total output lines: 363

compute/lib/cy_elliptic_genus_k3e_engine.py:1323:        sum_{N>=0} p^N Z(Sym^N(K3); tau, z) = 1/Phi_10(Omega)
compute/lib/cy_elliptic_genus_k3e_engine.py:1324:    where Phi_10 is the Igusa cusp form (weight 10 Siegel modular
compute/lib/cy_elliptic_genus_k3e_engine.py:1335:        siegel_connection="DMVV formula -> 1/Phi_10 (Igusa cusp form)",
compute/lib/coderived_artifact.py:757:    where Phi_10 is the Igusa cusp form of weight 10 on Sp(4, Z),
compute/lib/coderived_artifact.py:808:    2. Siegel cusp forms (e.g., the weight-10 Igusa cusp form Phi_10)
compute/lib/cy_grand_atlas_k3e_engine.py:26:  BPS from DVV: 1/Phi_10           (Igusa cusp form inverse)
compute/lib/cy_grand_atlas_k3e_engine.py:1426:            "title": "Does Z^sh(K3xE) relate to 1/Phi_10?",
compute/lib/cy_grand_atlas_k3e_engine.py:1429:                "1/Phi_10 both encode BPS data. The leading asymptotics match: "
compute/lib/cy_grand_atlas_k3e_engine.py:1434:                "genus expansion and the Fourier-Jacobi expansion of 1/Phi_10. "
compute/lib/cy_bps_spectrum_k3e_engine.py:574:# Section 4: DVV formula -- 1/4-BPS degeneracies from 1/Phi_10
compute/lib/cy_bps_spectrum_k3e_engine.py:655:    # The Fourier-Jacobi expansion of 1/Phi_10:
compute/lib/cy_bps_spectrum_k3e_engine.py:656:    #   1/Phi_10 = sum_{m >= -1} psi_m(tau, z) p^m
compute/lib/cy_bps_spectrum_k3e_engine.py:777:    # More precisely: in the expansion 1/Phi_10 = sum psi_m p^m,
compute/lib/cy_bps_spectrum_k3e_engine.py:871:    # From the expansion of the first FJ coefficient of 1/Phi_10:
compute/lib/cy_bps_spectrum_k3e_engine.py:878:    # Actually, the first FJ coefficient psi_1 of 1/Phi_10 is:
compute/lib/cy_bps_spectrum_k3e_engine.py:895:    # which is NOT the same as the coefficient of 1/Phi_10.
compute/lib/cy_modular_k3e_engine.py:34:    Z_BPS(Omega) = 1/Phi_10(Omega)
compute/lib/cy_modular_k3e_engine.py:36:where Phi_10 = chi_10 (with possible sign convention).
 succeeded in 50ms:
Total output lines: 470

compute/lib/celestial_arithmetic_engine.py:67:   - kappa(W_N) = c * (H_N - 1), NOT c/2 for N > 2 (AP9).
compute/lib/celestial_arithmetic_engine.py:85:kappa = c * (H_N - 1) diverges logarithmically.
compute/lib/celestial_arithmetic_engine.py:353:    The TOTAL celestial kappa (all spins) is c * (H_N - 1) for truncation to N.
compute/lib/celestial_arithmetic_engine.py:1097:    """Total kappa(W_N) = c(W_N, k) * (H_N - 1) as N varies.
compute/lib/celestial_arithmetic_engine.py:1437:    kappa_total = c(W_N, k) * (H_N - 1)
compute/lib/celestial_arithmetic_engine.py:1438:    At fixed k > 0: c(N) ~ -N^3, H_N - 1 ~ ln(N)
compute/lib/celestial_arithmetic_engine.py:1442:    But the NORMALIZED kappa_total / c = H_N - 1 ~ ln(N).
compute/lib/celestial_arithmetic_engine.py:1465:        "normalized_divergence": "kappa/c = H_N - 1 ~ ln(N)",
compute/lib/twisted_holography_engine.py:389:    kappa = c * (H_N - 1) where H_N is the N-th harmonic number.
compute/lib/twisted_holography_engine.py:391:    AP1/AP9: kappa(W_N) = c*(H_N - 1) != c/2 for N >= 3.
compute/lib/twisted_holography_engine.py:779:    For W^k(sl_N): kappa = c*(H_N - 1) (AP1/AP9).
compute/lib/twisted_holography_engine.py:780:    F_1 = kappa/24 = c*(H_N - 1)/24.
compute/lib/ap5_cross_volume_checker.py:21:    4.  AP136  -- ``\\kappa(W_N) = c(H_N - 1)``  (NOT ``H_{N-1}``)
compute/lib/ap5_cross_volume_checker.py:153:    # 4. AP136 -- kappa(W_N) = c(H_N - 1), NOT c H_{N-1}
compute/lib/rectification_delta_f2_verify_engine.py:319:    """Total kappa(W_N) = sum_{j=2}^{N} c/j = c * (H_N - 1)."""
compute/lib/rectification_delta_f2_verify_engine.py:531:    """kappa(W_N) = c * (H_N - 1) = c * sum_{j=2}^N 1/j."""
compute/lib/rectification_delta_f2_verify_engine.py:536:    """H_N - 1 = sum_{j=2}^N 1/j."""
compute/lib/rectification_delta_f2_verify_engine.py:565:    Let H1 = H_N - 1 = sum 1/j, H2 = sum 1/j^2, H3 = sum 1/j^3.
 succeeded in 51ms:
Total output lines: 248

compute/lib/bc_grand_atlas_v3_engine.py:1216:                        "(G/L/C/M) classifies code families: G=repetition, L=CSS, "
compute/lib/theorem_bridgeland_shadow_engine.py:30:(B) G/L/C/M = BRIDGELAND WALL-CHAMBER STRUCTURE.
compute/lib/coxeter_anomaly_test.py:13:type (n>=5), correlating with the G/L/C/M shadow depth classification.
compute/lib/genus_tower_l_hierarchy.py:954:    """Shadow depth classification: G/L/C/M.
compute/lib/local_p1p1_shadow.py:829:    shadow_class_1: str       # G/L/C/M for direction 1
compute/lib/local_p1p1_shadow.py:830:    shadow_class_2: str       # G/L/C/M for direction 2
compute/lib/local_p1p1_shadow.py:831:    shadow_class_diag: str    # G/L/C/M for diagonal direction
compute/lib/bc_motivic_integration_shadow_engine.py:53:  - Shadow depth classification: G/L/C/M (thm:single-line-dichotomy)
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:117:      - shadow class (G/L/C/M)
compute/lib/modular_koszul_engine.py:11:  4. Shadow metric Q_L, discriminant Delta, depth class G/L/C/M
compute/lib/theorem_gz_frontier_engine.py:934:                 'different generator lines lie in different G/L/C/M classes'),
compute/lib/twisted_holography_engine.py:1221:    5. Shadow depth classification (G/L/C/M)
compute/lib/bar_gf_universality_engine.py:54:  shadow_metric_census.py -- G/L/C/M classification
compute/lib/linf_bracket_engine.py:9:for the Virasoro algebra and all four archetype classes (G/L/C/M).
compute/lib/bc_qnm_shadow_engine.py:1180:    The four shadow classes G/L/C/M produce qualitatively different
compute/lib/pixton_genus3_shadow_engine.py:575:# Section 7: Cross-family comparison (G/L/C/M)
compute/lib/bc_matrix_model_deep_engine.py:1206:    """Classify shadow depth class (G/L/C/M)."""
compute/lib/theorem_open_closed_rectification_engine.py:1079:    """Shadow archetype classification G/L/C/M and its open/closed content.

thinking
**Searching for targeted equations**

Okay, I need to refine my search a bit more. I think I might have missed the C24 and MC equations. I'll search for fixed strings with proper escaping. For instance, I could use commands like `rg -n -F "1/(2*pi*i)" compute/lib`, and also check for `rg -n -F "[Theta, Theta]" compute/lib`. That should help me pinpoint what I'm looking for more effectively!
exec
/bin/zsh -lc 'rg -n -F "1/(2*pi*i)" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "[Theta, Theta]" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "pole_r = pole_OPE - 1" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "T''^c(s''^{-1} A-bar)" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "|s''^{-1} v| = |v| - 1" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "varrho_BP = 1/6" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/bc_isomonodromic_shadow_engine.py:27:   The RH factorization index kappa_RH = (1/(2*pi*i)) * oint d log det Y
compute/lib/bc_isomonodromic_shadow_engine.py:462:    kappa_RH = (1/(2*pi*i)) * oint d log det Y
compute/lib/modular_forms_shadow_engine.py:493:    The Serre derivative is theta = q d/dq = (1/(2*pi*i)) d/dtau.
compute/lib/modular_forms_shadow_engine.py:516:    where D = (1/(2*pi*i)) d/dtau = q d/dq is the normalized derivative.
compute/lib/resurgence_trans_series_engine.py:946:    # F_g ~ S_1/(2*pi*i) * A_1^{-2g} * (2g-1)! at leading order in hbar-plane.
compute/lib/shadow_mzv_engine.py:1227:      Order 1: coefficient involves 1/(2*pi*i) -- the linking number
compute/lib/resurgence_arithmetic_frontier_engine.py:882:        S_r^{(1)} = (1/(2*pi*i)) * oint sqrt(Q_L(t)) / t^{r+1} dt
compute/lib/bc_shadow_zeta_zeros_engine.py:549:        (1/(2*pi*i)) * oint (zeta'/zeta)(s) ds = N - P
compute/lib/bc_shadow_zeta_zeros_engine.py:570:        """Compute (1/(2*pi*i)) * integral of zeta'/zeta along segment."""
compute/lib/frontier_defect_explicit_engine.py:1161:    On a punctured region, [Omega] = (1/(2*pi*i)) * int_gamma Omega.
compute/lib/frontier_defect_explicit_engine.py:1183:    Res_{s_0}(Omega) = (1/(2*pi*i)) * int_{|s-s_0|=r} Omega(s) ds
compute/lib/bc_nc_chernweil_shadow_engine.py:337:    """Integrated first Chern class: c_1 = (1/(2*pi*i)) oint F.
compute/lib/bc_period_torelli_shadow_engine.py:103:    tau(c) ~ (1/(2*pi*i)) * N * log(c) + tau_0 + O(c)
compute/lib/bc_period_torelli_shadow_engine.py:958:        tau(c) ~ (1/(2*pi*i)) * N * log(c) + tau_0 + O(c)
compute/lib/bc_period_torelli_shadow_engine.py:970:    This is NOT of the form (1/(2*pi*i))*N*log(c) -- it is a POLE, not a log.
compute/lib/bc_period_torelli_shadow_engine.py:1040:        tau(c) ~ (1/(2*pi*i)) * N * log(c - c_LY) + tau_0
compute/lib/theorem_genus2_sl3_partition_engine.py:659:    where delta = -(1/(2*pi*i)) * log(w).
compute/lib/bc_residue_atlas_engine.py:305:        # (1/(2*pi*i)) * (real + i*imag) = (imag + i*(-real)) / (2*pi)
compute/lib/bc_residue_atlas_engine.py:307:        # Wait: 1/(2*pi*i) = -i/(2*pi), so:
compute/lib/resurgence_deep_engine.py:753:    S_r ~ S_1/(2*pi*i) * omega_1^{-r} * Gamma(r - 1/2) / Gamma(r+1) * ...
 succeeded in 51ms:
compute/lib/theorem_open_closed_rectification_engine.py:1057:    (a) Pure closed: D Theta + 1/2 [Theta, Theta] + hbar Delta(Theta) = 0
compute/lib/bcov_mc_complete_proof_engine.py:774:            mc_quantity="[Theta, Theta]^{(g,0)}",
compute/lib/pixton_mc_relations.py:4:equation D*Theta + (1/2)[Theta, Theta] = 0. Tests conj:pixton-from-shadows:
compute/lib/celestial_ope_shadow_projections_engine.py:16:The MC equation D*Theta + (1/2)[Theta, Theta] = 0 decomposes by arity at
compute/lib/tensor_harrison_bar_engine.py:1209:    The MC equation d(Theta) + (1/2)[Theta, Theta] = 0 makes sense because
compute/lib/theorem_pixton_generation_g4_engine.py:7:via the MC equation D*Theta + (1/2)[Theta, Theta] = 0. At genus 4:
compute/lib/bc_derived_moduli_shadow_engine.py:6:the space of solutions Theta_A satisfying D*Theta + (1/2)[Theta, Theta] = 0.
compute/lib/eulerian_weight_mc_engine.py:21:2. Whether the MC equation DTheta + (1/2)[Theta, Theta] = 0 respects
compute/lib/eulerian_weight_mc_engine.py:636:    The bracket term [Theta, Theta] at genus 1, arity 0 involves
compute/lib/eulerian_weight_mc_engine.py:645:    Therefore: [Theta, Theta] at arity 0 involves ONLY weight-2 components,
compute/lib/eulerian_weight_mc_engine.py:1072:    2. The MC equation DTheta + (1/2)[Theta, Theta] = 0 does NOT decompose
compute/lib/integrable_shadow_c3.py:68:   shadow tower: D*Theta + (1/2)[Theta, Theta] = 0.
compute/lib/string_field_theory_bar_engine.py:18:   D*Theta + (1/2)[Theta, Theta] = 0 in the modular convolution algebra.
compute/lib/string_field_theory_bar_engine.py:773:        D * Theta + (1/2) [Theta, Theta] = 0
compute/lib/string_field_theory_bar_engine.py:777:        {S, S}         <-->   [Theta, Theta] (Lie bracket)
compute/lib/string_field_theory_bar_engine.py:793:        "bar_equation": "D * Theta + (1/2) [Theta, Theta] = 0",
compute/lib/string_field_theory_bar_engine.py:796:            "antibracket_{S,S}": "[Theta, Theta] (Lie bracket in g^mod_A)",
compute/lib/theorem_stokes_mc_engine.py:21:    The MC equation D Theta + (1/2)[Theta, Theta] = 0 constrains the alien
compute/lib/theorem_stokes_mc_engine.py:381:    The MC equation D Theta + (1/2)[Theta, Theta] = 0 in the genus-graded
compute/lib/chiral_ope_bootstrap.py:727:      D*Theta + (1/2)[Theta, Theta] = 0
 succeeded in 52ms:
compute/lib/quantum_group_shadow.py:187:    # AP19: pole_r = pole_OPE - 1 via d-log absorption
compute/lib/quantum_group_shadow.py:246:    # AP19: pole_r = pole_OPE - 1 via d-log absorption
compute/lib/quantum_group_shadow.py:471:    # AP19: pole_r = pole_OPE - 1 via d-log absorption
compute/lib/quantum_group_shadow.py:1064:    # AP19: pole_r = pole_OPE - 1 via d-log absorption
compute/lib/quantum_group_shadow.py:1113:    # AP19: pole_r = pole_OPE - 1 via d-log absorption
compute/lib/quantum_group_shadow.py:1381:    # AP19: pole_r = pole_OPE - 1 via d-log absorption
compute/lib/quantum_group_shadow.py:1392:    # AP19: pole_r = pole_OPE - 1 via d-log absorption
compute/lib/bc_free_fermion_shadow_tower.py:106:    #   [LT] AP19: pole_r = pole_OPE - 1
compute/lib/collision_residue_identification.py:20:      One d log factor absorbs one pole, so pole_r = pole_OPE - 1.
 succeeded in 51ms:
compute/lib/k3_cy_a2_verification_engine.py:103:  - Bar complex: B(A) = T^c(s^{-1} A-bar), augmentation ideal (AP132)
compute/lib/ordered_chirhoch_sl3_elliptic_engine.py:84:  - B^{ord}(A) = T^c(s^{-1} A-bar) with augmentation ideal (AP132)
compute/lib/ordered_chirhoch_arity4_derham_engine.py:65:  - B^{ord}(A) = T^c(s^{-1} A-bar) with AUGMENTATION IDEAL (AP132)
compute/lib/w_infinity_chiral_qg_engine.py:79:  - Bar: B(A) = T^c(s^{-1} A-bar), deconcatenation coproduct (AP132, AP22).
 succeeded in 51ms:
compute/lib/k3_cy_a2_verification_engine.py:104:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)
compute/lib/ordered_chirhoch_sl3_elliptic_engine.py:85:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)
compute/lib/ordered_chirhoch_yangian_engine.py:61:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22).
compute/lib/ordered_chirhoch_arity4_derham_engine.py:66:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)
 succeeded in 51ms:
compute/lib/bp_koszul_conductor_engine.py:19:    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)
compute/lib/bp_koszul_conductor_engine.py:148:    varrho_BP = 1/6 (anomaly ratio from strong-generator data).
compute/lib/bp_koszul_conductor_engine.py:151:    # [CF] varrho_BP = 1/6 matches the BP anomaly-ratio proposition.
compute/lib/universal_shadow_tower_engine.py:236:    """kappa_BP(k) = varrho_BP * c_BP(k) where varrho_BP = 1/6.
compute/lib/universal_shadow_tower_engine.py:238:    The anomaly ratio varrho_BP = 1/6 is computed from strong generators:



thinking
**Inspecting candidate modules**

I need to look at some candidate modules to check if they actually verify structural formulas. For C14-C15, I found only docstrings in the cross-volume/K3 engines, which might not qualify as a generic verifier. I must decide if that counts as verification. If those modules use the formulas computationally, then it could count. But if it’s just commentary, it might not be enough. I'll need to inspect the relevant files around those functions to confirm.
thinking
**Determining formula engine presence**

I think I should figure out which formulas have direct engines since the search gave me explicit file names and functions. For those that are missing a direct engine, I need stronger evidence, like using the `true_formula_census_verifier.py` that only covers C01-C10. If an explicit engine doesn’t show up with `rg`, and I only find prose references instead of executable checks, then we can declare it missing. I should be careful when claiming absence and ground my conclusions in the actual file contents.
thinking
**Assessing formula verification**

I found in `true_formula_census_verifier.py` that it only covers formulas up to C10, and when I targeted `rg` over compute/lib for keywords related to C24, I only got results for generic contour-normalization uses, not a specific verifier. Is that enough evidence? It could be. I need to perform exact searches for some formulas to confirm their absence. The likely missing candidates include C12, possibly covered by `quantum_group_shadow.py` and `collision_residue_identification.py`, as well as C13, which might be verified by `hh_heisenberg_e3_engine.py`. I need to check the actual code to confirm.
codex
I’m at the point where the remaining risk is subtle overcounting: several files mention a formula in prose without actually verifying it. I’m delegating one pass to map `C1–C31` into `verified / partial / none`, then I’ll re-check the disputed entries against the live files before reporting.
collab spawn_agent(call_BorGRTrMeLfXO3rnOgNqpHYk, prompt="Audit /Users/raeez/chiral-bar-cobar/compute/lib for actual compute-engine coverage of CLAUDE.md C1-C31. For each C-numbe…")
spawn_agent(call_BorGRTrMeLfXO3rnOgNqpHYk, prompt="Audit /Users/raeez/chiral-bar-cobar/compute/lib for actual compute-engine coverage of CLAUDE.md C1-C31. For each C-numbe…") pending init:
  agent: 019d840d-fcf5-7913-9b82-6563547cf202
mcp startup: no servers

thinking
**Planning CLAUDE formula audit**

I’m outlining a multi-step plan to identify CLAUDE C1-C31 formulas from the CLAUDE doc, search for their references in the compute/lib directory, and classify coverage by mapping formula definitions to verifying code lines. To do this well, I need to read the CLAUDE section on "True Formula Census" closely before searching with regex on compute/lib to compile a thorough audit.
Plan update
Collect CLAUDE C1-C31 formula definitions and then inspect compute/lib for coverage evidence before summarizing the audit.
  → Open CLAUDE.md to extract the C1-C31 true formula census entries for precise reference
  • Search through compute/lib for references or implementations that verify each C-number and note file/line evidence
  • Summarize coverage for all C1-C31 entries, classifying VERIFIED/PARTIAL/NONE with explicit citations
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C[0-9][0-9]?" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
219:Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).
221:**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
223:**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
225:**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).
227:**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.
229:**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).
231:**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).
233:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
235:**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).
237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
243:**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.
245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
247:**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).
249:**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).
251:**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.
253:**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).
255:**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).
257:**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).
exec
/bin/zsh -lc "sed -n '1,240p' compute/lib/hh_heisenberg_e3_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' compute/lib/genus2_formality_obstruction_virasoro_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' compute/lib/collision_residue_identification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' compute/lib/wn_central_charge_canonical.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Explicit E_3 structure on HH*(H_k): Gerstenhaber bracket verification.

Computes the Hochschild cohomology HH*(H_k) of the Heisenberg vertex
algebra at level k and verifies the E_3 algebra structure explicitly,
including the Gerstenhaber bracket on low-degree groups.

MATHEMATICAL CONTENT:

The Heisenberg vertex algebra H_k has a single bosonic generator J of
conformal weight 1 with OPE J(z)J(w) ~ k/(z-w)^2.  It is the simplest
chiral algebra: abelian (class G), Koszul, with kappa(H_k) = k and
classical r-matrix r^Heis(z) = k/z.

Hochschild cohomology HH*(H_k) = Ext_{ChirAlg}(H_k, H_k) decomposes:

  HH^0(H_k) = Z(H_k) = C           (center = scalars, the vacuum)
  HH^1(H_k) = Der(H_k)/Inn(H_k)    (outer derivations)
  HH^2(H_k) = Def(H_k)             (first-order deformations)

For H_k specifically:
 succeeded in 51ms:
r"""Genus-2 formality obstruction for Virasoro via stable graph decomposition.

Determines which of the 7 genus-2 stable graphs (AP123: exactly 7, NOT 6)
contribute nontrivially to the formality obstruction for Virasoro (class M),
and whether the genus-2 obstruction is independent of genus-1.

MATHEMATICAL FRAMEWORK
======================

Virasoro Vir_c is class M: shadow depth r = infinity, all m_k nonzero,
Delta = 8*kappa*S_4 != 0 for generic c.

Shadow data (from theorem_ainfty_nonformality_class_m_engine.py):
    kappa(Vir_c) = c/2                        (C2, AP1)
    S_3 = 2                                    (c-independent)
    S_4 = -(5c+22)/(10c)                       (c-dependent)
    S_5 = -48/(c^2(5c+22))                     (c-dependent)

r-matrix (AP19, AP126, C11): r^Vir(z) = (c/2)/z^3 + 2T/z
    OPE pole order 4, r-matrix pole order 3 (d-log absorbs one pole).
 succeeded in 52ms:
"""Collision-residue identification: r(z) = Res^coll_{0,2}(Theta_A).

Verifies the Yangian-shadow theorem: the dg-shifted Yangian r-matrix
r(z) controlling the binary OPE of A! is the binary collision residue
of the full modular MC class Theta_A.

NOTATION DISAMBIGUATION (see Remark rem:three-r-matrices in
e1_modular_koszul.tex):

This module works with the *full OPE data* r^{OPE}(z) -- the complete
singular part of the OPE phi_i(z) phi_j(w), valued in A ⊗ A.  The
BinaryRMatrix class records the collision r-matrix after the one-pole
absorption coming from the d log kernel.  It also keeps the underlying
OPE pole order for comparison.

  - r^{OPE}(z) = full singular OPE in A ⊗ A.
      For Virasoro: leading pole is (c/2)/z^4.
      For Heisenberg: kappa/z^2.
  - r^{coll}(z) = Res^coll_{0,2}(Theta_A) in A! ⊗ A!.
      One d log factor absorbs one pole, so pole_r = pole_OPE - 1.
 succeeded in 51ms:
r"""Canonical W_N central charge formula — single source of truth.

The correct Fateev-Lukyanov formula for the principal W-algebra W^k(sl_N)
obtained by quantum Drinfeld-Sokolov reduction is:

    c(W_N, k) = (N-1) - N(N^2-1)(k+N-1)^2/(k+N)

This is the ONLY correct formula. The simpler expression
``(N-1)(1 - N(N+1)/(k+N))`` is WRONG — it gives c+c' = 2(N-1) under
Feigin-Frenkel duality k' = -k-2N, but the correct complementarity is
c+c' = 2(N-1) + 4N(N^2-1) (Freudenthal-de Vries identity).

Decisive test: at N=2, k=1, the correct formula gives c = -7
(standard Virasoro from DS(sl_2, k=1)). The wrong formula gives c = -1.

Source: w_algebras.tex line 2815.

XVER-34 independently verified: kappa+kappa' = 13 for Virasoro (171 tests).
The simple formula gives kappa+kappa' = 1. WRONG.

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
ainfty_transferred_structure.py
algebraic_family_rigidity.py

thinking
**Planning formula coverage audit**

I’m preparing to audit compute coverage for CLAUDE C1-C31 by identifying scripts that verify their formulas. I’ll start by reviewing the `true_formula_census_verifier.py` file since it might collect coverage data per formula. I'll check its first 200 lines to better understand how it classifies and verifies formulas.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/true_formula_census_verifier.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
"""True Formula Census verification engine.

Independently recomputes the canonical Wave 12-2 formulas used in the
standard landscape census and cross-checks them against the census values.

Checks covered:
  C01. kappa(Heis_k) = k
  C02. kappa(Vir_c) = c/2
  C03. kappa(V_k(g)) = dim(g) * (k + h^vee) / (2 * h^vee)
  C04. kappa(W_N) = c * (H_N - 1)
  C05. c_bc(lambda) = 1 - 3 * (2 * lambda - 1)^2
  C06. c_bg(lambda) = 2 * (6 * lambda^2 - 6 * lambda + 1)
  C07. E_8 fundamental irrep dimensions
  C08. H_N = sum_{j=1}^N 1/j exactly
  C09. Complementarity sums by family
  C10. K_BP = 196 for Bershadsky-Polyakov W_3^(2)

Anti-pattern coverage:
  AP1   family-specific kappa formulas
  AP24  complementarity is not universal across families

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '200,400p' compute/lib/true_formula_census_verifier.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
) -> Fraction:
    """Recover kappa from an r-matrix with an explicit level prefix.

    AP126/AP141 guard:
      The bare form Omega / z is forbidden. The level prefix must remain
      visible, and the k = 0 specialization must force vanishing.
    """
    if level_prefix is None:
        raise ValueError(
            "AP126/AP141: missing explicit level prefix in r-matrix; "
            "bare Omega/z is forbidden"
        )
    level = _as_fraction(level_prefix)
    kernel = _as_fraction(averaged_kernel)
    if level == 0:
        return Fraction(0)
    return level * kernel


def validate_e8_fundamental_dimensions(candidate: Iterable[int]) -> bool:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '400,800p' compute/lib/true_formula_census_verifier.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    computed = {
        "W_3(c=1)": kappa_w_n(3, 1),
        "W_4(c=1)": kappa_w_n(4, 1),
        "W_5(c=1)": kappa_w_n(5, 1),
    }
    return _make_result("C04", "Principal W_N kappa", expected, computed)


def verify_C05() -> ResultDict:
    """C05. Canonical formula: c_bc(lambda) = 1 - 3 * (2 lambda - 1)^2.

    Anti-pattern guard:
      AP129: reciprocal or sign swaps fail at lambda = 2.
      The bosonic string ghost check must return c_bc(2) = -26.

    Citation:
      True Formula Census Wave 12-2 C5 and landscape_census.tex.
    """
    expected = {
        "lambda=1/2": Fraction(1),
thinking
**Inspecting files for review**

I need to check several Python files, including `extended_ferm_ghost.py` and `bicoloured_partition_engine.py`. There are others on my list too like `bp_koszul_conductor_engine.py` and `chiral_hochschild_engine.py`, along with `shadow_depth_cross_verification.py` and `cy_second_quantization_engine.py`. I’m also considering `quantum_group_shadow.py`, `mc5_disk_local.py`, and `theorem_mc5_analytic_rectification_engine.py`. It seems like a good plan to do targeted inspections on these files. Let's get started!
exec
/bin/zsh -lc "sed -n '1,260p' compute/lib/chiral_hochschild_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' compute/lib/bicoloured_partition_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' compute/lib/extended_ferm_ghost.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/bp_koszul_conductor_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Bicoloured partition numbers and 1/eta^2 q-expansion engine.

MATHEMATICAL FRAMEWORK
======================

The Dedekind eta function is:

    eta(tau) = q^{1/24} * prod_{n >= 1} (1 - q^n),   q = e^{2*pi*i*tau}

The inverse square 1/eta(tau)^2 has q-expansion:

    1/eta(tau)^2 = q^{-1/12} * sum_{n >= 0} p_{-2}(n) * q^n

where p_{-2}(n) are the **bicoloured partition numbers** (OEIS A000712):
the number of partitions of n into parts of 2 colours.

Equivalently, the generating function for bicoloured partitions is:

    sum_{n >= 0} p_{-2}(n) * q^n = prod_{n >= 1} 1/(1 - q^n)^2

 succeeded in 52ms:
"""Chiral Hochschild cohomology engine — computational Theorem H.

Computes ChirHoch*(A) for all standard families beyond Heisenberg,
making Theorem H fully computational.

THEOREM H (thm:hochschild-polynomial-growth): For chirally Koszul A,
ChirHoch*(A) is concentrated in degrees {0, 1, 2} (quadratic regime)
with polynomial P_A(t) = dim Z(A) + dim ChirHoch^1(A)·t + dim Z(A!)·t².

MATHEMATICAL CONTENT — THREE COHOMOLOGY GROUPS:

  ChirHoch^0(A) = Z(A)         the CENTER of A
  ChirHoch^1(A) = Der(A)/Inn(A) outer derivations modulo inner
  ChirHoch^2(A) = Z(A!)^∨       dual of center of Koszul dual

For the QUADRATIC regime (Heisenberg, affine KM, βγ, bc, free fermion),
all three groups are finite-dimensional and the polynomial P_A(t) is
a complete invariant of ChirHoch*.

DERIVATION ANALYSIS (ChirHoch^1):
 succeeded in 52ms:
"""Extended fermion-ghost duality: computational verification.

Conjecture conj:extended-ferm-ghost (free_fields.tex) posits a derived
fermionic system F^bullet that is Koszul dual to the derived
betagamma-bc system B^bullet.

PROVED BASE CASES:
  thm:betagamma-bc-koszul   — (betagamma)^! = bc and (bc)^! = betagamma
                               (two-generator duality, dim V = 2)
  thm:single-fermion-boson-duality — F^! = Sym^ch(gamma) and vice versa
                                      (single-generator, dim V = 1)

CONJECTURED EXTENSION:
  The derived fermionic system F^bullet has generators:
    psi^(0)  of weight h = 1/2  (standard fermion)
    psi^(1)  of weight h = 3/2  (weight-1 descendant)
    psi^(-1) of weight h = -1/2 (weight-(-1) ancestor)
  with OPE: psi^(i)(z) psi^(j)(w) = delta_{i+j,0}/(z-w) + regular.

  The derived betagamma-bc system B^bullet is:
 succeeded in 51ms:
r"""Bershadsky-Polyakov Koszul conductor and complementarity: exact Fraction arithmetic.

MATHEMATICAL CONTENT
====================

The Bershadsky-Polyakov algebra W^k(sl_3, f_{(2,1)}) is the DS reduction of
affine sl_3 at the MINIMAL nilpotent orbit.  Its central charge, Feigin-Frenkel
dual level, Koszul conductor, anomaly ratio, and modular characteristic are
computed here in exact rational arithmetic.

Formulas:

    c_BP(k) = 2 - 24(k+1)^2 / (k+3)

    k' = -k - 6     (Feigin-Frenkel dual; h^v(sl_3) = 3, Dynkin shift)

    K_BP = c_BP(k) + c_BP(-k-6) = 196   (level-independent)

    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C1[0-9]" -n compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_holographic_c13_entanglement_engine.py:100:S4_C13 = Rational(10, 1131)  # 10/[13*(5*13+22)] = 10/[13*87]
compute/lib/theorem_holographic_c13_entanglement_engine.py:101:DELTA_C13 = Rational(40, 87)  # 8 * (13/2) * 10/1131 = 40/87
compute/lib/theorem_holographic_c13_entanglement_engine.py:109:F1_C13 = Rational(13, 48)  # kappa * lambda_1
compute/lib/theorem_holographic_c13_entanglement_engine.py:110:F2_C13 = Rational(91, 11520)  # kappa * lambda_2
compute/lib/theorem_holographic_c13_entanglement_engine.py:111:F3_C13 = Rational(403, 1935360)  # kappa * lambda_3
compute/lib/theorem_holographic_c13_entanglement_engine.py:452:    Delta = DELTA_C13
compute/lib/theorem_holographic_c13_entanglement_engine.py:499:    S4 = S4_C13
compute/lib/theorem_holographic_c13_entanglement_engine.py:678:    ratio = path1 / F1_C13
compute/lib/gerstenhaber_sl2_bracket_engine.py:92:  CLAUDE.md C9, C13, AP126
compute/lib/hh_heisenberg_e3_engine.py:47:  CLAUDE.md C1, C10, C13: kappa(H_k) = k, r^Heis(z) = k/z, av(r) = kappa
compute/lib/hh_heisenberg_e3_engine.py:70:        r_matrix_coeff: coefficient in r^Heis(z) = k/z (CLAUDE.md C10)
compute/lib/hh_heisenberg_e3_engine.py:85:    r^Heis(z) = k/z (CLAUDE.md C10: level prefix mandatory, AP126).
compute/lib/hh_heisenberg_e3_engine.py:91:        r_matrix_coeff=k,  # C10: r^Heis(z) = k/z, coefficient is k
compute/lib/hh_heisenberg_e3_engine.py:585:    CLAUDE.md C10: level prefix mandatory (AP126).
compute/lib/hh_heisenberg_e3_engine.py:603:    """Verify av(r(z)) = kappa at arity 2 (CLAUDE.md C13).
compute/lib/entanglement_entropy_engine.py:39:  CLAUDE.md census C1-C6, C8, C18, C19; AP68
compute/lib/entanglement_entropy_engine.py:54:    """H_n = sum_{j=1}^{n} 1/j.  [C19: CLAUDE.md]
compute/lib/twisted_holography_comparison_engine.py:32:  [C17]   Costello, "Holography and Koszul duality: the example of the M2
compute/lib/twisted_holography_comparison_engine.py:82:            of CS-matter). Costello [C17] identifies boundary = Yangian(gl_N).
compute/lib/twisted_holography_comparison_engine.py:249:    Extracted from the published papers [CG18, C17, CP20, CDG20].

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/irregular_kz_stokes_virasoro_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Irregular KZ Stokes matrices for the Virasoro algebra at arity 2.

THE IRREGULAR KZ ODE
====================

The KZ connection for Virasoro at arity 2 uses the classical r-matrix
(C11, trace-form convention, AP126 verified):

    r^{Vir}(z) = (c/2)/z^3 + 2T/z

The KZ ODE on a module M is:

    d Phi/dz = A(z) Phi,    A(z) = (c/2)/z^3 * Id + 2/z * rho(T)

where rho(T) is the representation of L_0 on M.  The singularity at
z = 0 is IRREGULAR of Poincare rank r = 2 (leading pole order 3,
minus 1 for the standard convention).

SCALAR CASE (eigenvalue sectors)
================================
thinking
**Inspecting quantum parameters**

I need to take a closer look at several components: `shadow_depth_cross_verification`, `cy_second_quantization_engine`, `quantum_group_shadow`, and `mc5_disk_local`. There might also be a need to consider the `theorem_mc5_analytic_rectification_engine` or the period matrix. It feels like there's a lot to unpack here, and I'm hoping to clarify their roles to ensure everything works properly. Let's see what I find as I dig into these!
exec
/bin/zsh -lc "sed -n '1,240p' compute/lib/shadow_depth_cross_verification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' compute/lib/quantum_group_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/mc5_disk_local.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/cy_second_quantization_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Shadow depth cross-verification engine: 4 independent methods for G/L/C/M classification.

The shadow depth classification G/L/C/M is a central structural invariant
of the shadow obstruction tower (thm:shadow-archetype-classification).
This module cross-verifies the classification using FOUR independent methods:

    METHOD 1 — DIRECT SHADOW COMPUTATION:
        Compute S_2, S_3, S_4, S_5, ... from the OPE data via the convolution
        recursion.  r_max = max{r : S_r != 0} (or infinity if none vanish).

    METHOD 2 — CRITICAL DISCRIMINANT:
        Delta = 8*kappa*S_4.
        Delta = 0 => tower terminates (G or L).
        Delta != 0 => tower is infinite (M).
        Class C: stratum separation (quartic contact on charged stratum).

    METHOD 3 — SHADOW METRIC FACTORIZATION:
        Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.
        Perfect square => G or L.
        Irreducible => M.
 succeeded in 53ms:
r"""Quantum group shadow engine: R-matrices, Yangians, and KZ connections
from the shadow obstruction tower.

The central insight: quantum group structures ARE the shadow obstruction tower, read
through the collision residue lens.  Specifically:

  1. r(z) = Res^{coll}_{0,2}(Theta_A)  -- the classical r-matrix is the
     binary collision residue of the MC element Theta_A.

  2. R(z) = 1 + hbar*r(z) + hbar^2*r_2(z) + ...  -- the quantum R-matrix
     is the quantization of r(z), with genus-1 correction r_2.

  3. Y(g) generators emerge from the arity-n shadow projections:
     - Level 0 from arity-2 (kappa)
     - Level 1 from arity-3 (cubic shadow C)
     - Level 2 from arity-4 (quartic shadow Q)

  4. Baxter Q-operator from higher-arity shadows encodes TQ relations.

  5. The shadow connection nabla^sh restricts to the KZ connection on
 succeeded in 53ms:
r"""Second quantization bridge: Sym^N action on the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

The DMVV formula (Dijkgraaf-Moore-Verlinde-Verlinde 1997) connects the
single-copy K3 elliptic genus to the second-quantized BPS partition function:

    sum_{N>=0} p^N chi(Sym^N(K3), tau, z) = 1/Phi_10(Omega)

where Phi_10 is the weight-10 Igusa cusp form on Sp(4,Z), and
Omega = ((tau, z), (z, sigma)) with p = e^{2*pi*i*sigma}.

THE GAP: kappa_ch = 3 vs kappa_BPS = 5
=======================================

Two distinct modular characteristics appear (AP20, AP48):

(a) kappa_ch = kappa(Omega^ch(K3 x E)) = 3 = dim_C(K3 x E).
    This is the single-copy shadow tower invariant.
 succeeded in 53ms:
"""MC5 disk-local packet: BV-BRST = bar at the chain level on C₂ and C₃.

This module verifies conj:disk-local-perturbative-fm — the identification
of local perturbative BRST brackets with bar residue operations on FM
compactification strata.

The key identity (genus 0, disk-local):
  Q_{BRST}(a ⊗ b) = d_bar(a ⊗ b)

where:
  - Q_{BRST} is the BV-BRST differential from Vol II (3d HT theory)
  - d_bar is the bar differential from Vol I (configuration space residues)
  - Both act on B²(A) = s⁻¹A ⊗ s⁻¹A (bar degree 2)

ON C₂ STRATA:
  d_bar(a ⊗ b) = Res_{z₁→z₂} η₁₂ · a(z₁)b(z₂)
               = Σ_n a_{(n)}b  (n-th products from OPE)
  Q_{BRST}(a ⊗ b) = {S, a ⊗ b}  (BV antibracket with action)
               = Σ_n a_{(n)}b  (perturbative Feynman rules)

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "verify_C1[1-9]" -n compute/lib' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"CLAUDE\\.md C11\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/irregular_kz_stokes_virasoro_engine.py:188:#   source:                  CLAUDE.md C11

thinking
**Planning verification coverage analysis**

I'm figuring out how to systematically check which formulas from C11 to C31 have actual executable verification scripts, beyond just docstring mentions, by searching the compute/lib directory for references to each C formula and any verifying code or tests. This way I can clarify coverage and find explicit verifiers like the known `true_formula_census_verifier` for C1–C10.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -l "True Formula Census" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/true_formula_census_verifier.py
codex
The compute surface definitely verifies several “later” census items already: `C21`, `C23`, `C26`, `C30`, and BP’s `C31` all have live executable engines. The entries still under dispute are the structural formulas where the repo has many references but maybe no single falsifiable verifier: bar/desuspension, Cauchy normalization, Arnold-vs-KZ, and the period-matrix collapse.
exec
/bin/zsh -lc "sed -n '1,240p' compute/lib/k3_cy_a2_verification_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/theorem_mc5_analytic_rectification_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' compute/lib/theorem_thm_h_e3_rectification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Verification engine for Theorem CY-A_2 applied to K3 surfaces.

Traces the CY-to-chiral functor Phi: CY_2-Cat -> E_2-ChirAlg
applied to C = D^b(Coh(K3)) and verifies all invariants.

MATHEMATICAL FRAMEWORK
======================

Theorem CY-A_2 (Vol III, thm:cy-to-chiral) constructs
  Phi: CY_2-Cat -> E_2-ChirAlg
such that:
  (i)  Phi(C) has generating fields in bijection with HH^{bullet+1}(C)
  (ii) B(Phi(C)) ~ CC_bullet(C) as factorization coalgebras

For C = D^b(Coh(K3)):

1. HOCHSCHILD COHOMOLOGY (HKR, Example ex:hh-k3 in cy_categories.tex):
   By HKR: HH^p(D^b(Coh(X))) = oplus_{q+r=p} H^q(X, Omega^{n-r}_X)
   For K3 (n=2, CY_2 so T_X = Omega^1_X):
     HH^0 = H^0(O_X) + H^2(T_X) = k + k                  dim 2
 succeeded in 53ms:
r"""MC5 Analytic Rectification Engine: Moriwaki + Nafcha + AMT combined.

Combines three independent frameworks with the manuscript's MC5 (HS-sewing):
  1. Moriwaki [2602.08729, 2603.06491]: Sym(Bergman) = ind-Hilb(Heis),
     conformally flat factorization homology in IndHilb.
  2. Nafcha [2603.30037]: Chiral homology gluing formula for
     factorization algebras.
  3. Adamo-Moriwaki-Tanimoto [2407.18222]: Conformal OS axioms for
     unitary full VOAs.

MATHEMATICAL FRAMEWORK:

  THE GENUS-2 HEISENBERG PARTITION FUNCTION (3 paths):

  Path 1: Fredholm determinant (thm:heisenberg-sewing).
    Z_g(H_k) = det(Im Omega)^{-k/2} * |det'_zeta Delta|^{-k}
    At genus 2 via separating degeneration:
      Z_2^{sep}(H_1; tau_1, tau_2, w) = eta(q_1)^{-1} * eta(q_2)^{-1}
                                        * prod_{n>=1}(1-w^n)^{-1}
    The last factor is the cross-sewing Fredholm determinant.
exec
/bin/zsh -lc 'rg -n -F "1/Im(tau)" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"matrix form\" compute/lib | rg 'Im Omega|period'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "(Im Omega)''^{-1}_{ij}" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
r"""Theorem H E_3 rectification engine: De Leger, AKL, Griffin cross-check.

Deep rectification of Theorem H (ChirHoch amplitude [0,2], dim <= 4,
Koszul-functorial) against three recent papers:

PER AP94/AP95: Theorem H asserts that ChirHoch^*(A) for any standard
chirally Koszul A (quadratic or W-algebra regime) has COHOMOLOGICAL
AMPLITUDE concentrated in degrees {0, 1, 2} with TOTAL DIMENSION
bounded by 4 (AP134: amplitude, NOT virtual dimension).

This engine historically assumed the Gelfand-Fuchs polynomial-ring
model C[Theta_1, ..., Theta_r] for W-algebras (infinite-dimensional,
unbounded growth), which is the CONTINUOUS cohomology of the Witt
Lie algebra and a DIFFERENT functor from chiral Hochschild. That
model has been excised. ChirHoch for W-algebras is bounded by
Theorem H just like the quadratic regime.

  1. De Leger [2512.20167]: E_{n+1}-action on Hochschild-Pirashvili cochains.
     SC(P)-algebra from a colored operad P and an algebra A.
     When P = E_n, SC(P) ~ SC_n (Swiss-cheese). For n=2: SC(E_2) ~ SC_2,
 succeeded in 51ms:
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:234:      P_harm = sum_{i,j} (Im Omega)^{-1}_{ij} omega_i(z) * bar{omega_j(w)}
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:978:      P_harm = sum_{i,j=1}^{2} (Im Omega)^{-1}_{ij} omega_i(z) omega_j(w)
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:1045:                'proportional to (Im Omega)^{-1}_{ij}. '
compute/lib/bv_bar_class_c_engine.py:281:      P_harm = sum_{i,j=1}^{g} (Im Omega)^{-1}_{ij} omega_i(z) omega_j(w)
 exited 1 in 53ms:

 succeeded in 53ms:
compute/lib/bv_bar_class_m_engine.py:305:      delta_4^{contact,harm} = [10/(c(5c+22))] * (c/2) * (1/Im(tau))
compute/lib/bv_bar_class_m_engine.py:364:        'moduli_dependence': '1/Im(tau)',
compute/lib/bv_bar_class_m_engine.py:379:    Returns the coefficient of 1/Im(tau) in the quartic discrepancy.
compute/lib/bv_bar_class_m_engine.py:383:    contact_coeff = Q_contact * kap  # coefficient of 1/Im(tau)
compute/lib/bv_bar_class_m_engine.py:445:    However, there is a subtlety: the coefficient 1/Im(tau) is a
compute/lib/bv_bar_class_m_engine.py:452:    The moduli dependence 1/Im(tau) is a smooth function on M_{1,0},
compute/lib/bv_bar_class_m_engine.py:457:    In this tensor product, Q^contact tensor (1/Im(tau)) could
compute/lib/bv_bar_class_m_engine.py:461:    VERDICT: The coboundary question REDUCES to whether 1/Im(tau)
compute/lib/bv_bar_class_m_engine.py:464:    on the Hodge bundle. The function 1/Im(tau) is NOT holomorphic
compute/lib/bv_bar_class_m_engine.py:484:        'moduli_factor': '1/Im(tau)',
compute/lib/bv_bar_class_m_engine.py:489:            'delta_4 is proportional to Q^contact * (1/Im(tau)). '
compute/lib/bv_bar_class_m_engine.py:492:            '1/Im(tau) is a smooth but NON-holomorphic function on M_{1,0}. '
compute/lib/bv_bar_class_m_engine.py:735:    where A_1 = 1/Im(tau) is the Arakelov weight-1 function on M_{1,0}.
compute/lib/bv_bar_class_m_engine.py:756:    The Arakelov weight factor 1/Im(tau) is characteristic of genus-1
compute/lib/bv_bar_class_m_engine.py:869:            delta_4 = Rational(5) / (5 * c_val + 22)  # coefficient of 1/Im(tau)
compute/lib/bv_bar_class_m_engine.py:882:            'delta_4_coeff': delta_4,  # coefficient of 1/Im(tau)
compute/lib/bv_bar_class_m_engine.py:929:      P_harm = (1/Im(tau)) * (n=0 mode)
compute/lib/bv_bar_class_m_engine.py:1159:    where P_harm = 1/Im(tau) (absorbing the differential form factors).
compute/lib/bv_bar_class_m_engine.py:1208:    Note: the 1/Im(tau) factor is related to E_2*(tau):
compute/lib/bv_bar_class_m_engine.py:1210:    So 1/Im(tau) = (pi/3)(E_2(tau) - E_2*(tau)).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\(c/2\\)/z\\"'^3 '"\\+ 2T/z\" -n compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/ds_shadow_tower_sl2_engine.py:166:    The r-matrix is r^Vir(z) = (c/2)/z^3 + 2T/z  (AP126: c/2 prefix).
compute/lib/celestial_ope_shadow_projections_engine.py:63:   The r-matrix is r(z) = (c/2)/z^3 + 2T/z (AP19: pole orders one less
compute/lib/celestial_ope_shadow_projections_engine.py:427:    the r-matrix r(z) = (c/2)/z^3 + 2T/z has TWO pole terms (AP19).
compute/lib/celestial_ope_shadow_projections_engine.py:1079:    The r-matrix r(z) = (c/2)/z^3 + 2T/z (AP19) has two terms.
compute/lib/theorem_open_closed_rectification_engine.py:475:        # r-matrix (pole order one less): r(z) = (c/2)/z^3 + 2T/z
compute/lib/theorem_open_closed_rectification_engine.py:617:                "r_matrix": "(c/2)/z^3 + 2T/z",
compute/lib/twisted_holography_engine.py:1267:    For Virasoro: r(z) = (c/2)/z^3 + 2T/z (higher poles from L_{-2} and L_0).
compute/lib/cy_n4sca_k3_engine.py:491:            'description': 'Virasoro: r ~ (c/2)/z^3 + 2T/z',
compute/lib/mzv_bar_complex.py:548:      r(z) = (c/2)/z^3 + 2T/z  (NOT (c/2)/z^4 + 2T/z^2 + dT/z)
compute/lib/coha_bar_bridge_engine.py:647:            "r_matrix": "(c/2)/z^3 + 2T/z (AP19: bar absorbs a pole)",
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:839:    r^{cl}(z) = (c/2)/z^3 + 2T/z  (pole order 3 after AP19 d-log).
compute/lib/elliptic_genus_deep_engine.py:412:            'description': 'Virasoro sector: r(z) ~ (c/2)/z^3 + 2T/z',
compute/lib/celestial_koszul_ope.py:506:            r(z) = (c/2)/z^3 + 2T/z
compute/lib/celestial_koszul_ope.py:577:    Result: r(z) = (c/2)/z^3 + 2T/z.
compute/lib/celestial_koszul_ope.py:593:    The T-line part is the Virasoro r-matrix: (c/2)/z^3 + 2T/z.
compute/lib/celestial_chiral_comparison_engine.py:748:    r-matrix (AP19): (c/2)/z^3 + 2T/z
compute/lib/quantum_group_shadow.py:36:    For Virasoro Vir_c:   r(z) = (c/2)/z^3 + 2T/z
compute/lib/quantum_group_shadow.py:234:        r(z) = (c/2)/z^3 + 2T/z
compute/lib/ainfty_structure_maps_engine.py:1087:      r(z) = (c/2)/z^3 + 2T/z
compute/lib/theorem_w3_holographic_datum_engine.py:22:   TT channel: (c/2)/z^3 + 2T/z (Virasoro subsector, poles {3,1}).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1000,1200p' compute/lib/landscape_census_verification.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    # = 40*174/((5c+22)(152-5c)) = 6960/((5c+22)(152-5c))
    check = simplify(disc_sum - expected)

    results.append(VerificationResult(
        entry_name=f"Vir c={c_val}",
        field_name="Delta complementarity",
        table_value=expected,
        computed_value=disc_sum,
        method="Delta(c) + Delta(26-c)",
        passed=check == 0,
    ))

    return results


def verify_anomaly_ratio_wN() -> List[VerificationResult]:
    """Verify anomaly ratio sigma = H_N - 1 for small N."""
    results = []
    expected = {
        2: Rational(1, 2),

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/landscape_census_verification.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Full landscape census verification engine.

Independently recomputes EVERY numerical entry in the landscape census
(chapters/examples/landscape_census.tex) and flags any discrepancy.

Tables verified:
  1. tab:master-invariants — c, c+c', kappa for all families
  2. tab:shadow-tower-census — archetype class, r_max
  3. tab:free-energy-landscape — F_1, F_2, kappa at specific k/c
  4. tab:shadow-invariants-landscape — S_3, S_4, Delta, rho, kappa+kappa'
  5. tab:rmatrix-census — r-matrix pole structure

Anti-pattern coverage:
  AP1  — kappa formulas recomputed from first principles per family
  AP5  — cross-family consistency checks
  AP9  — explicit qualifiers for every kappa
  AP10 — cross-check tests, not single-family hardcodes
  AP24 — complementarity sum NOT assumed zero
  AP39 — S_2 vs kappa explicitly distinguished
  AP48 — kappa != c/2 for general VOAs




thinking
**Analyzing verification functions for formulas C1–C11**

I’m sifting through a large file to identify which functions explicitly verify formulas C1 through C11, looking closely at key verifiers like `true_formula_census_verifier` and `landscape_census_verification`. I want to track down line numbers for documentation and confirm if there’s dedicated code verifying r-matrix formulas beyond pole structure checks. This careful mapping will clarify verification coverage per formula.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "def verify_" compute/lib/landscape_census_verification.py' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
691:def verify_kappa_affine_formula(type_: str, rank: int, k: Rational) -> List[VerificationResult]:
743:def verify_kappa_virasoro(c_val: Rational) -> List[VerificationResult]:
777:def verify_free_energy_entry(entry: FreeEnergyEntry) -> List[VerificationResult]:
818:def verify_koszul_conductor_wN() -> List[VerificationResult]:
859:def verify_w3_complementarity(c_val: Rational) -> List[VerificationResult]:
880:def verify_wN_kappa_complementarity(N: int) -> List[VerificationResult]:
921:def verify_virasoro_shadow_invariants(c_val: Rational) -> List[VerificationResult]:
988:def verify_discriminant_complementarity(c_val: Rational) -> List[VerificationResult]:
1015:def verify_anomaly_ratio_wN() -> List[VerificationResult]:
1038:def verify_ap39_s2_vs_kappa() -> List[VerificationResult]:
1102:def verify_rmatrix_pole_census() -> List[VerificationResult]:
1134:def verify_betagamma_kappa_bc_duality() -> List[VerificationResult]:
1157:def verify_e8_anomaly_ratio() -> List[VerificationResult]:
1191:def verify_kappa_wN_formula() -> List[VerificationResult]:

thinking
**Investigating theorem details**

I’m considering if I need to look into the C29 partial. There's something intriguing about the theorem_mc5_analytic_rectification not mentioning the (Im Ω)^-1 collapse. I found out that the `theorem_bv_brst_o3_obstruction_engine` might use a matrix. But I need to confirm if the compute engine verifies at g=2. I’m wondering if it's only partial, so I think I'll focus on lines 220 and beyond to clarify.
thinking
**Assessing census verification needs**

I’m thinking about the lack of a dedicated census verifier. It could still count as partial verification because files use a formula. The user wants to flag missing engines, and I need to be strict about that. Should I create a coverage table in the final summary? They only asked for findings, so maybe just a note about what's covered will suffice. I'll focus on line numbers and pull exact references for clarity. Keeping it concise is essential!
thinking
**Gathering line numbers and coverage info**

I’m considering using `nl -ba` on candidate files to get exact line numbers, especially for main coverage files and any global gaps. I need to gather specific lines from documents like CLAUDE and the candidate engines. I might look into various files like `true_formula_census_verifier.py` and `landscape_census_verification.py`, among others. I should identify missing or partial formulas and systematically map each C formula to its verification status. This will help ensure nothing slips through the cracks!
thinking
**Verifying central charge status**

It looks like I've verified `wn_central_charge_canonical` and `true_formula` for C04, and they seem good. But there are no findings for that one. I need to clarify the status for C5 regarding the central charge, so I should check if there's additional information needed there. It’s important to ensure that every detail aligns correctly, so I’ll make sure nothing is overlooked while I wrap this up!
thinking
**Investigating code functions**

I'm considering whether I need to look at actual code. It might help to inspect further lines around the affine-specific functions, especially if they return collision residue with the level. I think I should search within `collision_residue_identification.py` for `r(z)` or any related functions. Additionally, there's something about `binary_r_matrix` I need to explore, so I’ll search for terms like `affine_sl2` and `affine` within that file. Let's see what comes up!
exec
/bin/zsh -lc "sed -n '160,320p' compute/lib/quantum_group_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,520p' compute/lib/collision_residue_identification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"affine_sl2|r\\(z\\)|collision residue|k\\*Omega|Omega/z|kappa = dim\\(g\\)\" compute/lib/collision_residue_identification.py compute/lib/quantum_group_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    def evaluate(self, z: Any) -> Any:
        """Evaluate r(z) as a symbolic expression."""
        result = S.Zero
        for k, coeff in self.poles.items():
            result += coeff / z**k
        return result

    @property
    def leading_pole(self) -> int:
        """Order of the leading pole in r(z)."""
        return max(self.poles.keys()) if self.poles else 0


def heisenberg_r_matrix(k=None) -> ClassicalRMatrix:
    r"""r-matrix for Heisenberg H_k: r(z) = k/z.

    The Heisenberg is abelian, so the r-matrix is a scalar multiple
    of 1/z.  The OPE has a double pole, and the collision-residue
    r-matrix absorbs one pole order via d-log.

 succeeded in 53ms:
    elif algebra_type == "affine_slN":
        k = Fraction(params["k"])
        N = params["N"]
        h_vee = Fraction(N)
        dim_g = Fraction(N * N - 1)
        return dim_g * (k + h_vee) / (2 * h_vee)
    elif algebra_type == "virasoro":
        c = Fraction(params["c"])
        return c / Fraction(2)
    elif algebra_type == "betagamma":
        lam = Fraction(params.get("lambda", 1))
        c = Fraction(2) * (6 * lam * lam - 6 * lam + 1)
        return c / Fraction(2)
    else:
        raise ValueError(f"Unknown algebra type: {algebra_type}")


# ========================================================================
# Binary r-matrix from OPE (the twisting morphism at arity 2)
# ========================================================================
 succeeded in 51ms:
compute/lib/quantum_group_shadow.py:5:through the collision residue lens.  Specifically:
compute/lib/quantum_group_shadow.py:7:  1. r(z) = Res^{coll}_{0,2}(Theta_A)  -- the classical r-matrix is the
compute/lib/quantum_group_shadow.py:8:     binary collision residue of the MC element Theta_A.
compute/lib/quantum_group_shadow.py:10:  2. R(z) = 1 + hbar*r(z) + hbar^2*r_2(z) + ...  -- the quantum R-matrix
compute/lib/quantum_group_shadow.py:11:     is the quantization of r(z), with genus-1 correction r_2.
compute/lib/quantum_group_shadow.py:32:  Its binary collision residue on Conf_2(C) gives r(z):
compute/lib/quantum_group_shadow.py:34:    For Heisenberg H_k:   r(z) = k/z               (abelian, trivial CYBE)
compute/lib/quantum_group_shadow.py:35:    For affine sl_2(k):   r(z) = Omega/z            (classical r-matrix, CYBE)
compute/lib/quantum_group_shadow.py:36:    For Virasoro Vir_c:   r(z) = (c/2)/z^3 + 2T/z
compute/lib/quantum_group_shadow.py:135:# 1. Classical r-matrix from shadow (collision residue)
compute/lib/quantum_group_shadow.py:140:    r"""Classical r-matrix r(z) = Res^{coll}_{0,2}(Theta_A).
compute/lib/quantum_group_shadow.py:142:    The binary collision residue of the MC element Theta_A on Conf_2(C).
compute/lib/quantum_group_shadow.py:145:        r(z) = sum_{k} r_k / z^k
compute/lib/quantum_group_shadow.py:161:        """Evaluate r(z) as a symbolic expression."""
compute/lib/quantum_group_shadow.py:169:        """Order of the leading pole in r(z)."""
compute/lib/quantum_group_shadow.py:174:    r"""r-matrix for Heisenberg H_k: r(z) = k/z.
compute/lib/quantum_group_shadow.py:197:def affine_sl2_r_matrix(k=None) -> ClassicalRMatrix:
compute/lib/quantum_group_shadow.py:198:    r"""r-matrix for affine sl_2 at level k: r(z) = Omega/z.
compute/lib/quantum_group_shadow.py:205:        r(z) = (1/(k + h^v)) * Omega / z
compute/lib/quantum_group_shadow.py:209:    The CYBE is satisfied by the classical r-matrix Omega/z

thinking
**Mapping verifying functions to C numbers**

I’m matching each verifying function in the large verifier file to its corresponding C number formula, focusing on how these functions cover formula verification across the landscape, and pinpointing exact line ranges to cite for detailed checking, especially around C11’s r-matrix verification.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/landscape_census_verification.py | sed -n '1080,1145p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1080	        field_name="AP39: S_2 vs kappa",
  1081	        table_value="S_2 != kappa",
  1082	        computed_value=f"S_2={S2_sl3}, kappa={kappa_sl3}",
  1083	        method="AP39 regression",
  1084	        passed=S2_sl3 != kappa_sl3,
  1085	        notes="AP39: for rank > 1, S_2 and kappa always differ",
  1086	    ))
  1087	
  1088	    # Virasoro: S_2 = c/2 = kappa. This is the ONLY standard family where they coincide.
  1089	    results.append(VerificationResult(
  1090	        entry_name="Vir_c",
  1091	        field_name="AP39: S_2 == kappa",
  1092	        table_value="S_2 = kappa for Virasoro",
  1093	        computed_value="c/2 = c/2",
  1094	        method="AP39 confirmation",
  1095	        passed=True,
  1096	        notes="AP39: Virasoro is the unique single-generator family where S_2 = kappa",
  1097	    ))
  1098	
  1099	    return results
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C11" compute/lib > /tmp/c11matches && cat /tmp/c11matches' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/irregular_kz_stokes_virasoro_engine.py:7:(C11, trace-form convention, AP126 verified):
compute/lib/irregular_kz_stokes_virasoro_engine.py:156:    C11 (Virasoro classical r-matrix, CLAUDE.md)
compute/lib/irregular_kz_stokes_virasoro_engine.py:188:#   source:                  CLAUDE.md C11
compute/lib/koszul_conductor_table_engine.py:76:# Virasoro  (C2, C8, C11)
compute/lib/w_infinity_chiral_qg_engine.py:78:    Virasoro: r^{coll}(z) = (c/2)/z^3 + 2T/z  (C11).
compute/lib/w_infinity_chiral_qg_engine.py:183:        # so OPE mode T_{(3)}T = 3! * (c/12) = c/2.  Correct (C11).
compute/lib/w_infinity_chiral_qg_engine.py:696:        # VERIFIED: 6 * c/12 = c/2.  Correct (C11).
compute/lib/w_infinity_chiral_qg_engine.py:860:        The Virasoro r-matrix (collision-residue convention, C11):
compute/lib/w_infinity_chiral_qg_engine.py:887:        # r-matrix components (C11, AP19)
compute/lib/w_infinity_chiral_qg_engine.py:902:                "The r-matrix has cubic + simple poles (C11). "
compute/lib/w_infinity_chiral_qg_engine.py:930:      r_2(z) = (c/2)/z^3 + 2T/z  (Virasoro, C11)
compute/lib/w_infinity_chiral_qg_engine.py:966:        r_2(z) = (c/2)/z^3 + 2T/z  (C11).
compute/lib/ds_sl2_vir_shadow_transition_engine.py:35:    landscape_census.tex: kappa formulas C1-C4, r-matrix C9-C11
compute/lib/genus2_formality_obstruction_virasoro_engine.py:19:r-matrix (AP19, AP126, C11): r^Vir(z) = (c/2)/z^3 + 2T/z
compute/lib/theorem_preface_positioning_engine.py:18:  C11 -- Borcherds identity at n=0 gives Jacobi
exec
/bin/zsh -lc "nl -ba compute/lib/quantum_group_shadow.py | sed -n '190,230p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,920p' compute/lib/collision_residue_identification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/collision_residue_identification.py | sed -n '300,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   190	        poles={1: k},
   191	        max_pole=1,
   192	        dim_g=1,
   193	        parameter=k,
   194	    )
   195	
   196	
   197	def affine_sl2_r_matrix(k=None) -> ClassicalRMatrix:
   198	    r"""r-matrix for affine sl_2 at level k: r(z) = Omega/z.
   199	
   200	    Here Omega is the Casimir in sl_2 tensor sl_2.  In the basis
   201	    {e, h, f} with standard structure constants:
   202	        Omega = e tensor f + f tensor e + (1/2) h tensor h
   203	
   204	    Normalized by the level: the actual shadow coefficient is
   205	        r(z) = (1/(k + h^v)) * Omega / z
   206	
   207	    where h^v = 2 is the dual Coxeter number of sl_2.
   208	
   209	    The CYBE is satisfied by the classical r-matrix Omega/z
 succeeded in 53ms:
   300	            if order > 0 and coeff != 0:
   301	                self.ope_pole_orders[pair] = order
   302	                self.pole_orders[pair] = self._absorbed_pole_order(order)
   303	                self.coefficients[pair] = coeff
   304	
   305	    def r_value(self, gen_i: str, gen_j: str) -> Dict:
   306	        """Return the r-matrix component r_{ij}(z).
   307	
   308	        Returns dict with:
   309	          - pole_order: the order of the collision r-matrix pole
   310	          - ope_pole_order: the order of the source OPE pole
   311	          - coefficient: the leading coefficient
   312	          - formula: human-readable string representation
   313	        """
   314	        pair = (gen_i, gen_j)
   315	        if pair not in self.coefficients:
   316	            return {
   317	                'pole_order': 0,
   318	                'ope_pole_order': 0,
   319	                'coefficient': Fraction(0),
 succeeded in 53ms:
            'kappa': self.kappa,
        }

    # ------------------------------------------------------------------
    # (d) Verification: collision residue = r-matrix
    # ------------------------------------------------------------------

    def verify_identification(self) -> Dict:
        """Verify the Yangian-shadow theorem: r(z) = Res^coll_{0,2}(Theta_A).

        For each pair of generators, compare:
          (1) The collision residue from Theta_A (the bar-intrinsic MC element)
          (2) The r-matrix from the known OPE

        They should match exactly: this is the content of the identification
        theorem.
        """
        coll = self.collision_residue()
        r_known = self.known_r_matrix()

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C13" compute/lib > /tmp/c13 && cat /tmp/c13' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_holographic_c13_entanglement_engine.py:100:S4_C13 = Rational(10, 1131)  # 10/[13*(5*13+22)] = 10/[13*87]
compute/lib/theorem_holographic_c13_entanglement_engine.py:101:DELTA_C13 = Rational(40, 87)  # 8 * (13/2) * 10/1131 = 40/87
compute/lib/theorem_holographic_c13_entanglement_engine.py:109:F1_C13 = Rational(13, 48)  # kappa * lambda_1
compute/lib/theorem_holographic_c13_entanglement_engine.py:110:F2_C13 = Rational(91, 11520)  # kappa * lambda_2
compute/lib/theorem_holographic_c13_entanglement_engine.py:111:F3_C13 = Rational(403, 1935360)  # kappa * lambda_3
compute/lib/theorem_holographic_c13_entanglement_engine.py:452:    Delta = DELTA_C13
compute/lib/theorem_holographic_c13_entanglement_engine.py:499:    S4 = S4_C13
compute/lib/theorem_holographic_c13_entanglement_engine.py:678:    ratio = path1 / F1_C13
compute/lib/hh_heisenberg_e3_engine.py:47:  CLAUDE.md C1, C10, C13: kappa(H_k) = k, r^Heis(z) = k/z, av(r) = kappa
compute/lib/hh_heisenberg_e3_engine.py:603:    """Verify av(r(z)) = kappa at arity 2 (CLAUDE.md C13).
compute/lib/gerstenhaber_sl2_bracket_engine.py:92:  CLAUDE.md C9, C13, AP126
compute/lib/averaging_kernel_engine.py:22:Verification anchors (C13, PE-1):
compute/lib/koszul_conductor_table_engine.py:110:# Affine Kac-Moody  V_k(g)  (C3, C9, C13)
compute/lib/theorem_preface_positioning_engine.py:20:  C13 -- Bar propagator d log E(z,w) has weight 1 (AP27)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '560,640p' compute/lib/hh_heisenberg_e3_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
        cup_graded_commutative=cup_gc,
        cup_associative=cup_assoc,
        cup_unital=cup_unit,
        bracket_degree=bracket_degree(),
        bracket_hh0_hh1_zero=br_01.is_zero(),
        bracket_hh1_hh1_zero=br_11.is_zero(),
        bracket_hh1_hh2_zero=br_12.is_zero(),
        all_brackets_zero=all_br_zero,
        graded_antisymmetry=gr_antisym,
        graded_jacobi=gr_jacobi,
        leibniz_rule=leibniz,
        e3_linking_trivial=e3_link_triv,
        browder_well_defined=browder_wd,
        is_gerstenhaber_algebra=is_gerst,
        is_e3_algebra=is_e3,
    )


# ============================================================
# 8. r-MATRIX AND KAPPA CONSISTENCY
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/hh_heisenberg_e3_engine.py | sed -n '600,660p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   600	
   601	
   602	def averaging_map_check(k: Any = 1) -> bool:
   603	    """Verify av(r(z)) = kappa at arity 2 (CLAUDE.md C13).
   604	
   605	    For abelian Heisenberg: av(k/z) = k = kappa(H_k).
   606	    The averaging map extracts the coefficient of 1/z, which is k.
   607	    """
   608	    kap = kappa_heisenberg(k)
   609	    # For Heisenberg (abelian), av(r) = coefficient of 1/z in r = k
   610	    av_r = k  # r(z) = k/z, so residue at z=0 is k
   611	    return av_r == kap
   612	
   613	
   614	# ============================================================
   615	# 9. DEGREE SHIFT VERIFICATION
   616	# ============================================================
   617	
   618	def verify_all_degree_shifts() -> Dict[Tuple[int, int], int]:
   619	    """Verify |[a,b]| = |a| + |b| - 1 for all basis pairs.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/theorem_virasoro_spectral_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
exec
/bin/zsh -lc "rg -n \"Cauchy|coefficient extraction|\\[z\\"'^'"\\{n-1\\}\\]|\\[z\\"'^n'"\\]|contour integral normalization\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/frontier_verifications.py:92:    r"""Additive (Cauchy) convolution: (f * g)(n) = sum_{a+b=n} f(a)g(b).
compute/lib/cy_mathieu_moonshine_engine.py:94:    """Cauchy product truncated to nmax terms."""
compute/lib/cy_mathieu_moonshine_engine.py:416:    """Cauchy product for Fraction lists."""
compute/lib/bc_motivic_integration_shadow_engine.py:1369:    Path 2: Motivic zeta coefficient extraction
compute/lib/shadow_channel_decomposition.py:430:# The Cauchy-Schwarz shadow inequality (NEW)
compute/lib/shadow_channel_decomposition.py:434:    """The Cauchy-Schwarz inequality for the shadow algebra.
compute/lib/theorem_thm_d_multiweight_frontier_engine.py:680:    """Cauchy-Schwarz quantity for propagator values 1/j, j=2..N.
compute/lib/theorem_thm_d_multiweight_frontier_engine.py:686:    but the analogous Cauchy-Schwarz quantity for the propagator WEIGHTS alone.
compute/lib/local_p1p1_shadow.py:396:    Uses the dual Cauchy identity (exact).
compute/lib/local_p1p1_shadow.py:1412:           vanishes by the Cauchy-Schwarz equality condition.
compute/lib/w4_ope_miura.py:1387:    # ----- Primary coefficient extraction -----
compute/lib/w4_ope_miura.py:1975:    """Complete stage-4 coefficient extraction pipeline.
compute/lib/shadow_cohft_rmatrix_engine.py:143:    # Solve R'(z) = f'(z) R(z), R(0) = 1 via Cauchy product
compute/lib/bc_quantum_modularity_shadow_engine.py:1087:        # Simple 1/eps leading coefficient extraction
compute/lib/w5_shadow_tower.py:626:    This is ≥ 0 by Cauchy-Schwarz, with equality iff all
compute/lib/cy_grand_atlas_k3e_engine.py:178:    """Cauchy product truncated to nmax terms."""
compute/lib/ce_vs_chiral_bar_reconciliation_engine.py:378:    conformal-weight dims are coefficient extractions of the Koszul dual
compute/lib/bc_subconvexity_engine.py:47:    Path 5: Cauchy integral formula consistency
compute/lib/bc_subconvexity_engine.py:464:    """Ratio M_4 / M_2^2. For bounded functions, this is <= 1 by Cauchy-Schwarz.
compute/lib/elliptic_genus_deep_engine.py:120:    """Cauchy product (convolution) truncated to nmax terms."""
exec
/bin/zsh -lc 'rg -n -F "F_1 = kappa/24" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "31/967680" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "7/5760" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/pixton_genus3_shadow_engine.py:686:    The Faber-Pandharipande lambda_3^FP = 31/967680 gives the intersection
compute/lib/pixton_genus3_shadow_engine.py:1127:    All should give 31/967680.
compute/lib/cy_elliptic_genus_k3e_engine.py:839:      g=3: (31/32)(1/42)/720 = 31/967680
compute/lib/cy_elliptic_genus_k3e_engine.py:885:      F_3 = 3 * 31/967680 = 31/322560
compute/lib/cy_n4sca_k3_engine.py:1542:    F_3 = 2 * 31/967680 = 31/483840
compute/lib/k3_relative_chiral.py:409:      F_3 = 2 * 31/967680 = 31/483840
compute/lib/k3_relative_chiral.py:1067:      F_3 = 2 * 31/967680 = 31/483840
compute/lib/rectification_delta_f2_verify_engine.py:85:      g=3: 31/967680
compute/lib/pixton_mc_relations.py:116:      g=1: 1/24, g=2: 7/5760, g=3: 31/967680, g=4: 127/154828800.
compute/lib/pixton_mc_relations.py:978:    Scalar level: F_3 = kappa * lambda_3^FP = kappa * 31/967680.
compute/lib/pixton_mc_relations.py:1025:    # Genus 3: F_3 = kappa * 31/967680
compute/lib/bv_bar_genus2_comparison.py:120:      lambda_3 = 31/967680
compute/lib/theorem_genus4_virasoro_engine.py:122:      g=3: 31/967680
compute/lib/higher_genus_graph_sum_engine.py:83:        g=3:  31/967680
compute/lib/bc_twisted_holography_zeta_engine.py:242:        g=3: 31/967680
compute/lib/cy_grand_atlas_k3e_engine.py:536:      F_3 = 3 * 31/967680 = 31/322560
compute/lib/pixton_genus3_engine.py:734:      F_3 = kappa * lambda_3^FP = kappa * 31/967680
compute/lib/pixton_genus3_engine.py:743:    return _lambda_fp_exact(3)  # = 31/967680
compute/lib/genus4_landscape.py:84:      g=3: 31/967680
compute/lib/genus4_landscape.py:337:    l3 = lambda_fp(3)  # 31/967680
 succeeded in 53ms:
Total output lines: 438

compute/lib/moonshine_shadow_depth.py:702:    - The shadow obstruction tower at genus 1 gives F_1 = kappa/24 = 1/2.
compute/lib/modular_forms_shadow_engine.py:152:    At the scalar level: F_1 = kappa/24 (constant, weight 0).
compute/lib/cy_n4sca_k3_engine.py:51:  (b) Character: F_1 = kappa/24 = 2/24 = 1/12 matches the genus-1 anomaly
compute/lib/cy_n4sca_k3_engine.py:597:      F_1 = kappa/24.  From the elliptic genus Z_{K3}(tau, 0) = 24:
compute/lib/local_p1p1_shadow.py:854:        should give F_1 = kappa/24 = 2/24 = 1/12.
compute/lib/bv_bar_genus2_comparison.py:28:  where F_1 = kappa/24 and F_2 = kappa * 7/5760 (if BV = bar).
compute/lib/bv_bar_genus2_comparison.py:738:      The identification with F_1 = kappa/24 is essentially PROVED
compute/lib/bv_bar_genus2_comparison.py:1087:      C_{1, 0} = F_1 = kappa/24 (the genus-1 partition function)
compute/lib/bv_bar_genus2_comparison.py:1090:    Wait, for a FREE field, the genus-1 partition function is F_1 = kappa/24,
compute/lib/pixton_mc_relations.py:1019:    # Genus 1: F_1 = kappa/24 (the initial data)
compute/lib/twisted_holography_engine.py:676:        F_1 = kappa/24 = k/24.
compute/lib/twisted_holography_engine.py:680:        lambda_1^FP = 1/24, so F_1 = kappa/24.
compute/lib/twisted_holography_engine.py:780:    F_1 = kappa/24 = c*(H_N - 1)/24.
compute/lib/twisted_holography_engine.py:847:    F_1 = kappa/24 = -N^2/24.
compute/lib/twisted_holography_engine.py:1191:    Path 1: Annulus trace. F_1 = kappa/24.
compute/lib/k3_relative_chiral.py:188:    F_1 = kappa/24.  From the partition function:
compute/lib/k3_relative_chiral.py:1164:    Path 2 (Witten genus): W(K3) = chi(K3) = 24. F_1 = kappa/24.
compute/lib/k3_relative_chiral.py:1168:      No: F_1 = kappa/24, and kappa = 2, so F_1 = 2/24 = 1/12.
 succeeded in 52ms:
Total output lines: 964

compute/lib/theorem_holographic_c13_entanglement_engine.py:600:      F_2 = (13/2) * (7/5760) = 91/11520
compute/lib/theorem_holographic_c13_entanglement_engine.py:647:    F_2 = kappa * lambda_2 = (13/2) * (7/5760) = 91/11520.
compute/lib/theorem_holographic_c13_entanglement_engine.py:653:              lambda_2 = (2^3 - 1)/2^3 * |B_4|/4! = (7/8)*(1/30)/24 = 7/5760
compute/lib/cy_elliptic_genus_k3e_engine.py:838:      g=2: (7/8)(1/30)/24 = 7/5760
compute/lib/cy_elliptic_genus_k3e_engine.py:884:      F_2 = 3 * 7/5760 = 7/1920
compute/lib/cy_n4sca_k3_engine.py:707:    F_2 = 2 * 7/5760 = 7/2880
compute/lib/cy_n4sca_k3_engine.py:1541:    F_2 = 2 * 7/5760 = 7/2880
compute/lib/k3_relative_chiral.py:408:      F_2 = 2 * 7/5760 = 7/2880
compute/lib/k3_relative_chiral.py:1066:      F_2 = 2 * 7/5760 = 7/2880
compute/lib/rectification_delta_f2_verify_engine.py:84:      g=2: 7/5760
compute/lib/rectification_delta_f2_verify_engine.py:566:    Let lambda = lambda_2^FP = 7/5760.
compute/lib/rectification_delta_f2_verify_engine.py:574:    lam2 = lambda_fp_independent(2)  # 7/5760
compute/lib/mumford_chiodo_multiweight_engine.py:68:  int kappa_1*lambda_2   = 7/5760     = lambda_2^FP
compute/lib/mumford_chiodo_multiweight_engine.py:292:    """Verify lambda_2^FP = 7/5760."""
compute/lib/mumford_chiodo_multiweight_engine.py:583:    At h = 1: I(1) = (1/2 - 1/2)*1/240 + 2*1/2*7/5760 - 0 = 7/5760 = lambda_2^FP.  CHECK.
compute/lib/mumford_chiodo_multiweight_engine.py:615:    # Integral should give lambda_2^FP = 7/5760
compute/lib/mumford_chiodo_multiweight_engine.py:619:        assert I_1 == Fraction(7, 5760), f"I(1) = {I_1} != 7/5760 for P = {P_val}"
compute/lib/pixton_mc_relations.py:116:      g=1: 1/24, g=2: 7/5760, g=3: 31/967680, g=4: 127/154828800.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "verify" compute/lib/theorem_virasoro_spectral_r_matrix_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
870:    """Extract kappa from the r-matrix and verify consistency.
900:def verify_skew_symmetry(c: Fraction) -> Dict[str, bool]:
936:def verify_bosonic_parity(c: Fraction) -> Dict[str, bool]:
1091:    parity = verify_bosonic_parity(c)
1094:    skew = verify_skew_symmetry(c)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '840,960p' compute/lib/theorem_virasoro_spectral_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    which after d log absorption gives (c/2)/z^3 in r(z).

    For Heisenberg: the OPE has only z^{-2}, so r(z) = k/z, and R_2 = 0.
    For affine KM: the OPE has z^{-2} and z^{-1}, so r(z) = Omega/z,
        and R_2 = 0 (no z^{-3} pole).
    For Virasoro: R_2 = -c/4, NONZERO for c != 0.

    This is the first visible R-matrix correction distinguishing
    class M from classes G/L/C.
    """
    R_2 = -c / 4
    R_4 = c ** 2 / 32
    R_6 = -c ** 3 / 384

    return {
        "R_2": R_2,
        "R_4": R_4,
        "R_6": R_6,
        "nonzero_for_c_neq_0": c != 0,
        "class_M_signature": c != 0,


thinking
**Evaluating r-matrix verification**

I’m checking if this file explicitly verifies the full Virasoro r-matrix expression tied to classification C11, but it seems to focus more on associated properties like odd poles and extracting kappa rather than an explicit assert comparing to the canonical formula. I’ll look for a separate verifying script, maybe in `rmatrix_landscape.py`, by searching for verify functions referencing `r^Vir`. There’s a lot here! Let’s explore further to find a direct verification.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "def verify" compute/lib/rmatrix_landscape.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
123:    def verify_ap19(self) -> Dict[str, bool]:
141:    def verify_bosonic_parity(self) -> Dict[str, bool]:
710:def verify_ibr(Omega: np.ndarray, n: int, atol: float = 1e-10) -> Dict[str, float]:
736:def verify_casimir_symmetry(Omega: np.ndarray, n: int,
thinking
**Inspecting code details**

I see that the search results point to `chiral_zeta_virasoro_engine.py`, specifically line 36 mentioning C24. I think it’s important to inspect this line closely. Maybe it references some form of verification or calculation, possibly using the Cauchy integral. Let's open that file to check exactly how it’s implemented and what it does. I’m curious to figure this out!
exec
/bin/zsh -lc "sed -n '1,220p' compute/lib/chiral_zeta_virasoro_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1320,1395p' compute/lib/string_field_theory_bar_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '960,1035p' compute/lib/topological_recursion_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' compute/lib/lambda_g_faber_pandharipande_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

    return result


# ============================================================================
# 10. Comprehensive verification functions
# ============================================================================

def verify_F1_all_families() -> Dict[str, Dict[str, Any]]:
    """Verify F_1 = kappa/24 for all standard families.

    F_1 = kappa * lambda_1^FP = kappa / 24.
    This is the UNIVERSAL prediction from both:
      - Theorem D (shadow obstruction tower)
      - EO recursion on the shadow spectral curve (via Bergman tau)
    """
    families = {
        'Vir_c1': virasoro_exact(1),
        'Vir_c10': virasoro_exact(10),
        'Vir_c13': virasoro_exact(13),
 succeeded in 51ms:
r"""Chiral zeta function Z_A(s) for Virasoro at c = 25.

Defines and analyzes the Dirichlet series

    Z_A(s) = sum_{g >= 1} F_g(Vir_{25}) * g^{-s}

where

    F_g = kappa * lambda_g^FP    (UNIFORM-WEIGHT)

with kappa(Vir_{25}) = 25/2 and the Faber-Pandharipande lambda_g integral

    lambda_g^FP = ((2^{2g-1} - 1) / 2^{2g-1}) * |B_{2g}| / (2g)!.

The lambda_g^FP coefficients decay geometrically:

    lambda_{g+1}^FP / lambda_g^FP  ->  1 / (2*pi)^2  ~  0.02533

so |F_g| ~ C * (kappa / (2*pi)^2)^g * (correction), and the Dirichlet series
Z_A(s) converges absolutely for ALL s in C.  The chiral zeta function is
 succeeded in 51ms:
"""Faber-Pandharipande intersection numbers lambda_g^FP.

Computes the tautological integral

    lambda_g^FP = int_{M-bar_{g,1}} psi^{2g-2} lambda_g
               = (2^{2g-1} - 1) |B_{2g}| / (2^{2g-1} (2g)!)

for g = 1, ..., 10 using exact rational (Fraction) arithmetic.

Generating function: sum_{g>=1} lambda_g^FP x^{2g} = (x/2)/sin(x/2) - 1.

References:
  - Faber, "A conjectural description of the tautological ring" (1999)
  - Faber-Pandharipande, "Hodge integrals and moduli" (2000)
  - Mumford, "Towards an enumerative geometry of the moduli space of curves"
"""

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial
 succeeded in 51ms:
            "sft_type": "free / quadratic",
            "max_vertex_arity": 2,
            "ainfty_formal": True,
        },
        "L": {
            "shadow_depth": 3,
            "example": "Affine KM (sl_2, sl_3, ...)",
            "sft_type": "cubic / Chern-Simons-like",
            "max_vertex_arity": 3,
            "ainfty_formal": True,
        },
        "C": {
            "shadow_depth": 4,
            "example": "beta-gamma",
            "sft_type": "quartic / contact",
            "max_vertex_arity": 4,
            "ainfty_formal": True,
        },
        "M": {
            "shadow_depth": "infinity",
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "def virasoro_rmatrix" -n compute/lib/rmatrix_landscape.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
315:def virasoro_rmatrix(c: Fraction = Fraction(26)) -> FamilyRMatrix:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '302,380p' compute/lib/rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
        fam.add_channel(
            f"{gi}{gj}", gi, gj,
            ope_poles={1: Fraction(1)},  # structure constant (nonzero)
            description=f"{gi}(z){gj}(w) ~ f^{{...}} J/(z-w)"
        )

    return fam


# ========================================================================
# 4. Virasoro at central charge c
# ========================================================================

def virasoro_rmatrix(c: Fraction = Fraction(26)) -> FamilyRMatrix:
    r"""Virasoro algebra at central charge c.

    OPE:  T(z) T(w) ~ (c/2)/(z-w)^4  +  2T(w)/(z-w)^2  +  dT(w)/(z-w)

    OPE poles: {4: c/2, 2: 2, 1: 1}
    r-matrix poles: {3: c/2, 1: 2}
exec
/bin/zsh -lc "sed -n '320,390p' compute/lib/theorem_shadow_conformal_block_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,140p' compute/lib/theorem_shadow_conformal_block_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

    Parameters:
        c_val: central charge
        max_r: maximum arity

    Returns:
        dict {r: S_r} for r = 2 to max_r
    """
    max_n = max_r - 2
    a = sqrt_QL_taylor_coefficients(c_val, max_n, exact)
    S = {}
    for n in range(len(a)):
        r = n + 2
        S[r] = a[n] / r
        if exact:
            S[r] = cancel(S[r])
    return S


# ============================================================================
 succeeded in 52ms:
r"""Shadow coefficients as conformal block integrals: spectral curve periods.

MATHEMATICAL CONTENT:

The closed-form generating function G[F](xi) = kappa*(xi/(2*sin(xi/2)) - 1)
packages all genus-g free energies F_g. Each F_g = kappa * lambda_g^FP is
an integral over M_bar_g of the Faber-Pandharipande lambda class.

Meanwhile, the shadow coefficient S_r is the r-th projection of the MC
element Theta_A.  The shadow metric Q_L(t) controls the tower via

    H(t) = t^2 * sqrt(Q_L(t)) = sum_{r>=2} r * S_r * t^r

so that S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t)).

INVESTIGATION (five questions):

(a) S_r = a_{r-2}/r where a_n is the n-th Taylor coefficient of sqrt(Q_L).
    Is a_n an integral over Conf_n(C)?

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "__name__" -n compute/lib/rmatrix_landscape.py' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "verify_" compute/lib/rmatrix_landscape.py' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
123:    def verify_ap19(self) -> Dict[str, bool]:
141:    def verify_bosonic_parity(self) -> Dict[str, bool]:
710:def verify_ibr(Omega: np.ndarray, n: int, atol: float = 1e-10) -> Dict[str, float]:
736:def verify_casimir_symmetry(Omega: np.ndarray, n: int,
816:        ap19 = fam.verify_ap19()
821:        bp = fam.verify_bosonic_parity()
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '800,860p' compute/lib/rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    lines.append("AP19: pole orders = OPE poles - 1 (d log absorption)")
    lines.append("=" * 72)

    for family_key, fam in landscape.items():
        lines.append(f"\n--- {fam.name} ---")
        lines.append(f"  Generators: {fam.generators}")
        lines.append(f"  kappa(A) = {fam.kappa}")
        for ch_name, ch in fam.channels.items():
            ope_str = str(ch['ope_poles']) if ch['ope_poles'] else "{} (regular)"
            r_str = str(ch['rmatrix_poles']) if ch['rmatrix_poles'] else "{} (entirely regular)"
            lines.append(f"  Channel {ch_name}:")
            lines.append(f"    OPE poles: {ope_str}")
            lines.append(f"    r-matrix poles: {r_str}")
            lines.append(f"    AP19 shift: max pole {ch['ope_max_pole']} -> {ch['rmatrix_max_pole']}")

        # AP19 verification
        ap19 = fam.verify_ap19()
        all_pass = all(ap19.values())
        lines.append(f"  AP19 verification: {'PASS' if all_pass else 'FAIL'}")


thinking
**Investigating incorrect formula**

I'm addressing a serious issue here; this isn't just about missing engines. It seems there's an incorrect formula in the compute/lib section. The user is asking for an adversarial audit and to hunt down subtle errors, so this finding is significant. I need to look closely at the lines around 460 to fully understand the problem. I’ll make sure to go through that carefully to get the details right!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/rmatrix_landscape.py | sed -n '300,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   300	    ]
   301	    for (gi, gj) in off_diag_pairs:
   302	        fam.add_channel(
   303	            f"{gi}{gj}", gi, gj,
   304	            ope_poles={1: Fraction(1)},  # structure constant (nonzero)
   305	            description=f"{gi}(z){gj}(w) ~ f^{{...}} J/(z-w)"
   306	        )
   307	
   308	    return fam
   309	
   310	
   311	# ========================================================================
   312	# 4. Virasoro at central charge c
   313	# ========================================================================
   314	
   315	def virasoro_rmatrix(c: Fraction = Fraction(26)) -> FamilyRMatrix:
   316	    r"""Virasoro algebra at central charge c.
   317	
   318	    OPE:  T(z) T(w) ~ (c/2)/(z-w)^4  +  2T(w)/(z-w)^2  +  dT(w)/(z-w)
   319	
codex
A more serious problem has shown up beyond “missing lanes”: at least one live compute module appears to record the wrong genus-2 scalar formula (`kappa^2` instead of linear `kappa`). I’m checking whether that is a docstring slip or executable logic drift before I include it as a finding.
exec
/bin/zsh -lc "nl -ba compute/lib/universal_shadow_tower_engine.py | sed -n '452,490p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '452,490p' compute/lib/universal_shadow_tower_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 58ms:
    max_n = max_arity - 2
    a_coeffs = _sqrt_ql_coefficients_with_a0(a0, q1, q2, max_n)

    coeffs: Dict[int, Fraction] = {}
    for n in range(max_n + 1):
        r = n + 2
        coeffs[r] = a_coeffs[n] / r

    return coeffs


def compute_free_energies(kappa: Fraction, max_genus: int = 5) -> Dict[int, Fraction]:
    """Compute free energies F_1..F_{max_genus} (UNIFORM-WEIGHT).

    F_g = kappa * lambda_g^FP.

    VERIFIED: [DC] F_1 = kappa/24; F_2 = 7*kappa^2/5760;
    [LT] thm:theorem-d (higher_genus_modular_koszul.tex).

    NOTE (AP32): These are UNIFORM-WEIGHT formulas.  For multi-weight
 succeeded in 58ms:
   452	    max_n = max_arity - 2
   453	    a_coeffs = _sqrt_ql_coefficients_with_a0(a0, q1, q2, max_n)
   454	
   455	    coeffs: Dict[int, Fraction] = {}
   456	    for n in range(max_n + 1):
   457	        r = n + 2
   458	        coeffs[r] = a_coeffs[n] / r
   459	
   460	    return coeffs
   461	
   462	
   463	def compute_free_energies(kappa: Fraction, max_genus: int = 5) -> Dict[int, Fraction]:
   464	    """Compute free energies F_1..F_{max_genus} (UNIFORM-WEIGHT).
   465	
   466	    F_g = kappa * lambda_g^FP.
   467	
   468	    VERIFIED: [DC] F_1 = kappa/24; F_2 = 7*kappa^2/5760;
   469	    [LT] thm:theorem-d (higher_genus_modular_koszul.tex).
   470	
   471	    NOTE (AP32): These are UNIFORM-WEIGHT formulas.  For multi-weight
exec
/bin/zsh -lc 'rg -n -F "F_2 = 7*kappa''^2/5760" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "kappa''^2/5760" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/shadow_zeta_engine.py:19:  b_2 = 7/5760       =>  F_2 = 7*kappa^2/5760
compute/lib/universal_shadow_tower_engine.py:468:    VERIFIED: [DC] F_1 = kappa/24; F_2 = 7*kappa^2/5760;
 succeeded in 53ms:
compute/lib/shadow_zeta_engine.py:19:  b_2 = 7/5760       =>  F_2 = 7*kappa^2/5760
compute/lib/genus2_boundary_strata.py:592:      ell_0 = kappa * 7/5760 - kappa^2/5760
compute/lib/universal_shadow_tower_engine.py:468:    VERIFIED: [DC] F_1 = kappa/24; F_2 = 7*kappa^2/5760;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/rmatrix_landscape.py | sed -n '110,150p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   110	                    ope_poles: Dict[int, Any], description: str = ""):
   111	        """Add an OPE channel and compute its r-matrix poles."""
   112	        rmatrix_poles = ope_to_rmatrix_poles(ope_poles)
   113	        self.channels[channel_name] = {
   114	            'gen_i': gen_i,
   115	            'gen_j': gen_j,
   116	            'ope_poles': ope_poles,
   117	            'rmatrix_poles': rmatrix_poles,
   118	            'ope_max_pole': max_pole_order(ope_poles),
   119	            'rmatrix_max_pole': max_pole_order(rmatrix_poles),
   120	            'description': description,
   121	        }
   122	
   123	    def verify_ap19(self) -> Dict[str, bool]:
   124	        """Verify AP19 for all channels: r-matrix max pole = OPE max pole - 1.
   125	
   126	        Returns {channel_name: passes} for each channel.
   127	        """
   128	        results = {}
   129	        for name, ch in self.channels.items():

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C14" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/theorem_preface_positioning_engine.py:21:  C14 -- r-matrix pole orders one less than OPE (AP19)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ker\\(epsilon\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_hca_pillar_a_engine.py:213:        epsilon(j) = 0 (Jacobi identity), so j is in ker(epsilon).
compute/lib/virasoro_bar_zhu.py:7:data of V, including the vacuum module V_+ = ker(epsilon) where epsilon
compute/lib/en_bar_coproduct_engine.py:10:where P^{!,c} is the Koszul dual cooperad and \bar{A} = ker(epsilon) is the
compute/lib/bar_cohomology_genus1_engine.py:284:    (The augmentation ideal V_+ = ker(epsilon) excludes only |0> at h=0.)
compute/lib/kl_ncomplex_sl2.py:23:    The (reduced) bar complex B_n(u_q) = I^{otimes n} where I = ker(epsilon)
compute/lib/kl_ncomplex_sl2.py:404:    The reduced bar complex B_n(u_q) = I^{otimes n} where I = ker(epsilon)
compute/lib/kl_ncomplex_sl2.py:458:        """Set up a basis for the augmentation ideal I = ker(epsilon).
compute/lib/celestial_ope_sln_shadow_engine.py:60:    AP132: Bar complex uses augmentation ideal bar{A} = ker(epsilon).
compute/lib/e1_from_chiral_bar_engine.py:458:    uses the AUGMENTATION IDEAL. The reduced bar complex uses A_bar = ker(epsilon),
thinking
**Inspecting potential bugs**

I see that I need to inspect `shadow_zeta_engine.py` and possibly `genus2_boundary_strata.py` because there might be bugs directly affecting performance. The user mentioned that something's missing with the engine, but these could be formula issues that aren't immediately obvious. I should definitely mark this with a [CRITICAL] tag. It's vital to look closely at the exact context to understand what's going wrong!
exec
/bin/zsh -lc "sed -n '1,80p' compute/lib/shadow_zeta_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/shadow_zeta_engine.py | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/genus2_boundary_strata.py | sed -n '580,605p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '580,605p' compute/lib/genus2_boundary_strata.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   580	      The relevant integral is int_{M-bar_{0,4}} 1 = 1 (since dim = 1).
   581	      But the handle operator inserts kappa each time, so:
   582	      ell_2 / 8 = kappa^2 * 1/8 * (combinatorial factor)
   583	
   584	    For the scalar sum to work:
   585	      ell_0 + ell_2/8 = kappa * 7/5760
   586	
   587	    The banana amplitude for Heisenberg is:
   588	      ell_2 = kappa^2 * (1/720)  [from double contraction of Killing form]
   589	      ell_2 / 8 = kappa^2 / 5760
   590	
   591	    And the smooth contribution:
   592	      ell_0 = kappa * 7/5760 - kappa^2/5760
   593	
   594	    Note: at the scalar level for the UNIVERSAL genus expansion,
   595	    F_2 = kappa * 7/5760 exactly, regardless of decomposition.
   596	    The decomposition below is the graph-by-graph accounting.
   597	    """
   598	    kappa = _kappa_heisenberg(k)
   599	    F2 = _F2_universal(kappa)
 succeeded in 50ms:
r"""Shadow zeta engine: Z_A(s) = sum_{g=1}^{infty} F_g * g^{-s}.

The shadow zeta function encodes the genus tower of a chiral algebra A
into a single Dirichlet-type series.  At uniform weight with parameter
kappa = kappa(A), the genus-g free energy is

    F_g(kappa) = kappa^g * b_g

where b_g are universal rational coefficients determined by the formula

    b_g = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)

with B_{2g} the Bernoulli numbers.  Equivalently,

    b_g = (1 - 2^{1-2g}) * |B_{2g}| / (2g)!

SANITY CHECKS:
  b_1 = 1/24         =>  F_1 = kappa/24
  b_2 = 7/5760       =>  F_2 = 7*kappa^2/5760
  # VERIFIED [DC] direct computation from Bernoulli  [LT] Faber-Pandharipande (1999)
 succeeded in 50ms:
     1	r"""Shadow zeta engine: Z_A(s) = sum_{g=1}^{infty} F_g * g^{-s}.
     2	
     3	The shadow zeta function encodes the genus tower of a chiral algebra A
     4	into a single Dirichlet-type series.  At uniform weight with parameter
     5	kappa = kappa(A), the genus-g free energy is
     6	
     7	    F_g(kappa) = kappa^g * b_g
     8	
     9	where b_g are universal rational coefficients determined by the formula
    10	
    11	    b_g = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)
    12	
    13	with B_{2g} the Bernoulli numbers.  Equivalently,
    14	
    15	    b_g = (1 - 2^{1-2g}) * |B_{2g}| / (2g)!
    16	
    17	SANITY CHECKS:
    18	  b_1 = 1/24         =>  F_1 = kappa/24
    19	  b_2 = 7/5760       =>  F_2 = 7*kappa^2/5760
    20	  # VERIFIED [DC] direct computation from Bernoulli  [LT] Faber-Pandharipande (1999)
 succeeded in 51ms:
      The relevant integral is int_{M-bar_{0,4}} 1 = 1 (since dim = 1).
      But the handle operator inserts kappa each time, so:
      ell_2 / 8 = kappa^2 * 1/8 * (combinatorial factor)

    For the scalar sum to work:
      ell_0 + ell_2/8 = kappa * 7/5760

    The banana amplitude for Heisenberg is:
      ell_2 = kappa^2 * (1/720)  [from double contraction of Killing form]
      ell_2 / 8 = kappa^2 / 5760

    And the smooth contribution:
      ell_0 = kappa * 7/5760 - kappa^2/5760

    Note: at the scalar level for the UNIVERSAL genus expansion,
    F_2 = kappa * 7/5760 exactly, regardless of decomposition.
    The decomposition below is the graph-by-graph accounting.
    """
    kappa = _kappa_heisenberg(k)
    F2 = _F2_universal(kappa)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/bar_complex.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
"""Bar complex of a chiral algebra as an explicit chain complex.

For a chiral algebra A with OPE data, the bar complex is:
  B-bar(A) = (T^c(s^{-1}A-bar), d_bar)

where A-bar = A / C*vacuum (remove vacuum), and d_bar is determined by:
  - Simple pole residues -> Lie bracket component
  - Double pole residues -> curvature m_0

Bar degree n: B-bar^n = (s^{-1}A-bar)^{tensor n} / Arnold relations.

Arnold relations on FM_{n+1}(P^1):
  eta_{ij} wedge eta_{jk} + eta_{jk} wedge eta_{ki} + eta_{ki} wedge eta_{ij} = 0
reduce the dimension.  On C_n(P^1), dim H^{n-1}(C_n, C) = (n-1)! for the
top-degree cohomology relevant to bar degree n-1.

GRADING: Cohomological, |d| = +1.  Bar differential has bar-degree -1
(it maps B-bar^n -> B-bar^{n-1}).  In the internal (conformal weight) grading,
d has degree +1.

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "A_bar" compute/lib/bar_complex.py' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Addressing formula issues**

I think there's a problem with the docstring and some formulas may be incorrect, which is a serious issue if the user is looking for an audit. I should consider documenting these errors as low to medium severity. I also want to investigate kappa^g patterns, which might relate to the census formula C24/F2 linearity. I’ll need to look into the functions in shadow_zeta_engine.py to see if they involve kappa^g as well, just to be thorough.
exec
/bin/zsh -lc "sed -n '80,180p' compute/lib/shadow_zeta_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"kappa\\"'^g|kappa '"\\*\\* g|F_g\\(kappa\\) = kappa\\"'^g|free_energy'"\\(|shadow zeta\" compute/lib/shadow_zeta_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3:The shadow zeta function encodes the genus tower of a chiral algebra A
7:    F_g(kappa) = kappa^g * b_g
30:  The shadow zeta Z_A(s) = sum F_g * g^{-s} inherits this convergence:
86:    r"""Universal coefficient b_g in F_g = kappa^g * b_g.
106:    F_g(kappa) = kappa^g * b_g
110:    return kappa ** g * shadow_b_g(g)
164:    """Result of convergence analysis for the shadow zeta series."""
178:    r"""Analyze convergence of the shadow zeta series at given kappa.
201:    # For F_g = kappa^g * b_g, |F_{g+1}/F_g| -> |kappa|/(2*pi)^2
257:    """Print a full shadow zeta report for Virasoro at central charge c."""
 succeeded in 51ms:

# ---------------------------------------------------------------------------
# Shadow free energy coefficients b_g
# ---------------------------------------------------------------------------

def shadow_b_g(g: int) -> Fraction:
    r"""Universal coefficient b_g in F_g = kappa^g * b_g.

    Formula: b_g = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    # VERIFIED [DC] direct computation  [LT] Faber-Pandharipande (1999)
    # VERIFIED [CF] cross-check: b_1=1/24 matches C24; b_2=7/5760 matches B37
    """
    if g < 1:
        raise ValueError(f"Genus must be >= 1, got {g}")
    B2g = bernoulli_even(g)
    abs_B2g = abs(B2g)
    power = 2 ** (2 * g - 1)
    numerator_factor = Fraction(power - 1, power)
    factorial_2g = Fraction(math.factorial(2 * g))
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"T\\"'^c" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/theorem_abedin_niu_yangian_engine.py:64:    [T^a, T^b] = f^{ab}_c T^c
compute/lib/theorem_abedin_niu_yangian_engine.py:181:        [T^a, T^b] = f^{ab}_c T^c           (g bracket)
compute/lib/theorem_abedin_niu_yangian_engine.py:257:        [T^a, T^b] = f^{ab}_c T^c
compute/lib/theorem_abedin_niu_yangian_engine.py:265:        # [T^a, T^b] = f^{ab}_c T^c
compute/lib/theorem_abedin_niu_yangian_engine.py:283:        # f^{ac}_b means the structure constant with [T^a, T^c] = f^{ac}_d T^d,
compute/lib/theorem_abedin_niu_yangian_engine.py:287:        # all c such that [T^a, T^c] has a T^b component.
compute/lib/theorem_abedin_niu_yangian_engine.py:299:                    # Does [T^a, T^c] = ... contain T^b?
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:155:    (ad(T^a))^b_c = f^{ab}_c  where [T^a, T^b] = f^{ab}_c T^c.
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:158:    8x8 matrices satisfy [ad(T^a), ad(T^b)] = f^{ab}_c ad(T^c) by
compute/lib/theorem_sl3_yangian_r_matrix_engine.py:174:    r"""Verify [ad(T^a), ad(T^b)] = f^{ab}_c ad(T^c) in the adjoint."""
compute/lib/mg_kuranishi_parity_engine.py:362:        T^c(s^{-1}H) introduces a sign (-1).
compute/lib/elliptic_genus_deep_engine.py:296:    The bar complex B(A) = T^c(s^{-1} Abar, d_bar) where Abar = A/C|0>.
compute/lib/bar_complex.py:4:  B-bar(A) = (T^c(s^{-1}A-bar), d_bar)
compute/lib/ap5_cross_volume_checker.py:22:    5.  AP132  -- ``T^c(s^{-1}\\bar A)`` augmentation-ideal bar complex
compute/lib/ap5_cross_volume_checker.py:30:    13. AP132  -- bar complex missing augmentation: ``T^c(s^{-1} A)``
compute/lib/ap5_cross_volume_checker.py:162:    # 5. AP132 -- augmentation ideal bar complex T^c(s^{-1} \bar A)
compute/lib/ap5_cross_volume_checker.py:165:        description="T^c(s^{-1} bar A) augmentation-ideal bar complex",
compute/lib/ap5_cross_volume_checker.py:167:        # \bar{A} or \bar A inside T^c(s^{-1} ...)
compute/lib/ap5_cross_volume_checker.py:257:        description="T^c(s^{-1} A) without bar (AP132 violation)",
compute/lib/ap5_cross_volume_checker.py:259:        # Match T^c(s^{-1} A) where the A has no \bar prefix.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,220p' compute/lib/ap5_cross_volume_checker.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""AP5 cross-volume consistency checker.

Automates the AP5 mandate from CLAUDE.md: "Grep ALL THREE volumes for variant
forms after every correction."  Historically this was a manual agent sweep
(Wave 6-2, Wave 8-5); this module turns it into a deterministic compute-layer
check that can run continuously.

The engine scans Vol I (chiral-bar-cobar), Vol II (chiral-bar-cobar-vol2), and
Vol III (calabi-yau-quantum-groups) for a library of canonical regex patterns
drawn directly from the anti-pattern catalog in CLAUDE.md.  For each pattern
the caller supplies an expected per-volume frequency (either an exact integer,
a bound ``(low, high)``, or ``"any"``).  The engine reports every pattern
whose observed frequency falls outside the declared envelope, giving a
human-readable drift report suitable for CI or for a pre-commit hook.

Canonical formulas covered (fifteen, each annotated with its governing AP):

    1.  AP126  -- bare ``\\Omega/z`` without level prefix ``k``
    2.  AP1    -- ``\\kappa(V_k(\\fg))`` (affine KM canonical form)
    3.  AP1    -- ``\\kappa(H_k) = k`` (Heisenberg, Vol I convention)
thinking
**Auditing critical logic**

Oh no, it looks like there's a mistake in the executable logic! It's using kappa raised to the power of g, which is pretty critical to note. I need to consider this as a significant issue. I should probably check for more wrong modules as well. It might be a good idea to search for `kappa ** g` since there could be several instances. I'll audit the census formula lane and search across the compute/lib directory for any mentions of `kappa ** g` or `kappa^g`.
exec
/bin/zsh -lc "rg -n \"kappa \\*\\* g|kappa\\"'^g|F_g'"\\(kappa\\) = kappa\\"'^g|F_g = kappa'"\\"'^g" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"7\\*kappa\\"'^2/5760|kappa'"\\"'^2 / 5760|kappa '"\\*\\* 2 / Rational\\(5760\\)|kappa\\*\\*2.*5760\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/bc_connes_spectral_shadow_engine.py:1232:    Simplified: amplitude ~ kappa^g * symmetry_factor for loop order g.
compute/lib/bc_connes_spectral_shadow_engine.py:1238:        amp = family.kappa ** g.loop_order * g.symmetry_factor
compute/lib/shadow_cohft_tautological.py:24:     Heisenberg: tau_{g,0}(H_k) = kappa^g * lambda_g (pure Hodge)
compute/lib/shadow_cohft_tautological.py:198:      G (Gaussian, r_max=2):  tau_{g,0} = kappa^g * lambda_g^{FP}
compute/lib/analytic_langlands_shadow_engine.py:1245:        # For now, compute the leading asymptotic: S_g ~ kappa^g * polynomial
compute/lib/shadow_zeta_engine.py:7:    F_g(kappa) = kappa^g * b_g
compute/lib/shadow_zeta_engine.py:86:    r"""Universal coefficient b_g in F_g = kappa^g * b_g.
compute/lib/shadow_zeta_engine.py:106:    F_g(kappa) = kappa^g * b_g
compute/lib/shadow_zeta_engine.py:110:    return kappa ** g * shadow_b_g(g)
compute/lib/shadow_zeta_engine.py:201:    # For F_g = kappa^g * b_g, |F_{g+1}/F_g| -> |kappa|/(2*pi)^2
compute/lib/theorem_higher_dim_modular_operad_engine.py:842:        weight = kappa ** gr.num_edges / Fraction(gr.automorphism_order())
compute/lib/theorem_higher_dim_modular_operad_engine.py:989:        fass_raw = kappa ** gr.num_edges * Fraction(ribbon_count, aut)
compute/lib/theorem_higher_dim_modular_operad_engine.py:991:        fass_normalized = kappa ** gr.num_edges / Fraction(aut)
compute/lib/chriss_ginzburg_universal.py:766:                "genus_g": f"g-loop: kappa^g * lambda_g correction",
compute/lib/modular_deformation_package.py:165:        return kappa ** gamma.num_edges
compute/lib/modular_deformation_package.py:1080:        amp = kappa ** gamma.num_edges / Fraction(gamma.automorphism_order())
compute/lib/stable_graph_enumeration.py:705:    return kappa ** graph.num_edges
compute/lib/stable_graph_enumeration.py:770:        amp = kappa ** gamma.num_edges
compute/lib/theorem_analytic_realization_obstruction_engine.py:609:      F_g = int_{M_g} c_1(det)^g = kappa^g * int lambda_1^g
compute/lib/shadow_hierarchy_engine.py:910:        F_shadow = kappa * sum_g lambda_g / kappa^g
 succeeded in 52ms:
compute/lib/shadow_zeta_engine.py:19:  b_2 = 7/5760       =>  F_2 = 7*kappa^2/5760
compute/lib/genus2_boundary_strata.py:589:      ell_2 / 8 = kappa^2 / 5760
compute/lib/genus2_boundary_strata.py:706:    # Banana: kappa^2 / 5760
compute/lib/genus2_boundary_strata.py:964:      At the scalar level: F_2^{Delta_irr} = kappa^2 / 5760
compute/lib/genus2_boundary_strata.py:977:    banana = kappa ** 2 / Rational(5760)
compute/lib/universal_shadow_tower_engine.py:468:    VERIFIED: [DC] F_1 = kappa/24; F_2 = 7*kappa^2/5760;

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar A" compute/lib/tensor_harrison_bar_engine.py' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

thinking
**Inspecting modules for issues**

I see there could be many problematic modules, and I should consider including some. The task is specifically about computing census formulas. However, the user wants to examine every weakness—even the subtle ones—so yes, I’ll include them. I need to inspect `shadow_cohft_tautological.py` since there might be an issue with `kappa^g * lambda_g`. I should search for the exact lines because this could contradict Theorem D. I'll make sure to note the line numbers.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "AP132" compute/lib/tensor_harrison_bar_engine.py' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

codex
The audit is now in two buckets: missing verifiers, and active formula drift inside compute modules. The latter is worse: several files still encode the old `kappa^g` genus-growth law instead of the linear `F_g = kappa * lambda_g^{FP}` census formula.
exec
/bin/zsh -lc "nl -ba compute/lib/shadow_cohft_tautological.py | sed -n '190,210p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/stable_graph_enumeration.py | sed -n '764,772p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/stable_graph_enumeration.py | sed -n '700,710p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/shadow_cohft_tautological.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   764	
   765	    At the scalar level, ell_Gamma = kappa^{|E(Gamma)|}.
   766	    """
   767	    total = Fraction(0)
   768	    for gamma in graphs:
   769	        aut = gamma.automorphism_order()
   770	        amp = kappa ** gamma.num_edges
   771	        total += amp / Fraction(aut)
   772	    return total
 succeeded in 53ms:
     1	r"""Shadow CohFT tautological class engine.
     2	
     3	Extracts tautological classes on M-bar_{g,n} from shadow obstruction tower data.
     4	This module bridges shadow obstruction tower computations (algebra) with intersection
     5	theory on moduli spaces of curves (geometry).
     6	
     7	The shadow CohFT maps:
     8	    shadow obstruction tower data --> tautological classes on M-bar_{g,n}
     9	
    10	KEY OBJECTS:
    11	
    12	1. Tautological classes:
    13	   - lambda_i = c_i(E) where E is the Hodge bundle (rank g)
    14	   - psi_j = c_1(L_j) where L_j is the cotangent line at marking j
    15	   - kappa_a = pi_*(psi_{n+1}^{a+1}) Mumford-Morita-Miller classes
    16	
    17	   Known intersection numbers:
    18	     int_{M-bar_{1,1}} psi_1 = 1/24
    19	     int_{M-bar_{2,0}} lambda_2 = 1/240  (Faber)
    20	     int_{M-bar_{g,0}} lambda_g lambda_{g-1} = |B_{2g}|/(2g) * |B_{2g-2}|/(2g-2) * 1/(2g-2)!
 succeeded in 53ms:
   190	
   191	    The map is determined by:
   192	      - kappa(A) = modular characteristic (genus-1 scalar)
   193	      - C(A) = cubic shadow (genus-0 structure constant)
   194	      - Q(A) = quartic contact shadow
   195	      - Higher shadow coefficients S_r for r >= 5
   196	
   197	    Shadow depth classification:
   198	      G (Gaussian, r_max=2):  tau_{g,0} = kappa^g * lambda_g^{FP}
   199	      L (Lie/tree, r_max=3):  contributions from cubic C
   200	      C (Contact, r_max=4):   quartic contact term
   201	      M (Mixed, r_max=inf):   full infinite tower
   202	    """
   203	
   204	    def __init__(self, kappa_val, cubic=Rational(0), quartic=Rational(0),
   205	                 shadow_class='G', name='generic'):
   206	        """Initialize shadow tautological map.
   207	
   208	        Parameters
   209	        ----------
 succeeded in 53ms:
   700	    product of edge contributions divided by the automorphism factor.
   701	
   702	    This is the leading term in the shadow obstruction tower expansion. The full
   703	    amplitude involves integration over vertex moduli M_{g(v),val(v)}.
   704	    """
   705	    return kappa ** graph.num_edges
   706	
   707	
   708	def heisenberg_free_energy(g: int, k: Fraction = Fraction(1),
   709	                           d: int = 1) -> Fraction:
   710	    """F_g(H_k^d) = kappa(H_k^d) * lambda_g^FP.

thinking
**Assessing formula verification coverage**

I'm piecing together how to verify C14-C31 formulas by checking for existing compute-engine scripts and references, aiming to classify each formula’s coverage as Verified, Partial, or None based on concrete code evidence like regex checks or dedicated verification modules. I want to confirm if the canonical formula C14 is truly covered by the `ap5` checker by examining relevant code lines to support its verification status.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/ap5_cross_volume_checker.py | sed -n '150,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   150	        expected={"vol1": "any", "vol2": "any", "vol3": "any"},
   151	    ),
   152	
   153	    # 4. AP136 -- kappa(W_N) = c(H_N - 1), NOT c H_{N-1}
   154	    CanonicalFormula(
   155	        key="ap136_wn_harmonic_wrong",
   156	        description="W_N kappa written with H_{N-1} (forbidden, AP136)",
   157	        ap_tag="AP136",
   158	        pattern=r"\\kappa\s*\(\s*W_N\s*\)[^\n]{0,40}H_\{\s*N\s*-\s*1\s*\}",
   159	        expected={"vol1": 0, "vol2": 0, "vol3": 0},
   160	    ),
   161	
   162	    # 5. AP132 -- augmentation ideal bar complex T^c(s^{-1} \bar A)
   163	    CanonicalFormula(
   164	        key="ap132_bar_augmentation_present",
   165	        description="T^c(s^{-1} bar A) augmentation-ideal bar complex",
   166	        ap_tag="AP132",
   167	        # \bar{A} or \bar A inside T^c(s^{-1} ...)
   168	        pattern=r"T\^c\(\s*s\^\{-1\}\s*\\bar\s*\{?A\}?\s*\)",
   169	        expected={"vol1": "any", "vol2": "any", "vol3": "any"},

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "CANONICAL_FORMULAS" -n compute/lib/ap5_cross_volume_checker.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
38:    -   Patterns are stored in a single ``CANONICAL_FORMULAS`` table so
124:CANONICAL_FORMULAS: Tuple[CanonicalFormula, ...] = (
315:            formulas if formulas is not None else CANONICAL_FORMULAS
639:    "CANONICAL_FORMULAS",
thinking
**Evaluating graph computations**

It seems like stable graph enumeration might not be entirely wrong. I’m thinking it could be calculating graph amplitudes apart from the final free energies, but there's potential subtlety there. The user mentioned computing engine verification of formulas, so I might need to address these claims about drift since they seem to overreach. My final answer length is limited, so I could include just 2-3 key formula drift findings. I may inspect the C21 engine and explorer results soon.
collab wait(call_8WSmkEmNYkQEDInjXAGHTlGt)
  receivers: 019d840d-fcf5-7913-9b82-6563547cf202
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '300,360p' compute/lib/ap5_cross_volume_checker.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    """

    def __init__(
        self,
        vol1_path: Optional[Path] = None,
        vol2_path: Optional[Path] = None,
        vol3_path: Optional[Path] = None,
        formulas: Optional[Sequence[CanonicalFormula]] = None,
    ) -> None:
        self.volumes: Dict[str, Path] = {
            "vol1": Path(vol1_path) if vol1_path else DEFAULT_VOL1,
            "vol2": Path(vol2_path) if vol2_path else DEFAULT_VOL2,
            "vol3": Path(vol3_path) if vol3_path else DEFAULT_VOL3,
        }
        self.formulas: Tuple[CanonicalFormula, ...] = tuple(
            formulas if formulas is not None else CANONICAL_FORMULAS
        )
        self._results: List[CheckResult] = []

    # ------------------------------------------------------------------
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C15" compute/lib/ap5_cross_volume_checker.py' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "desuspension" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_hca_pillar_a_engine.py:62:- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
compute/lib/bc_euler_product_shadow_engine.py:45:  - Cohomological grading (|d| = +1), bar uses desuspension.
compute/lib/pva_deformation_cy3.py:55:  - Bar uses desuspension (AP45)
compute/lib/theorem_langlands_fle_bridge_engine.py:83:- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
compute/lib/theorem_bethe_mc_engine.py:77:- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
compute/lib/bc_connes_spectral_shadow_engine.py:88:  - Cohomological grading (|d| = +1), bar uses desuspension.
compute/lib/sc_koszul_dual_cooperad_engine.py:18:  where F^c is the cofree cooperad, s^{-1} is the operadic desuspension,
compute/lib/sc_koszul_dual_cooperad_engine.py:94:  - Operadic desuspension s^{-1} shifts degree DOWN by 1 (AP45)
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:70:- Cohomological grading (|d| = +1), bar uses desuspension (AP45)
compute/lib/bar_gf_universality_engine.py:42:  - Cohomological grading (|d| = +1), bar uses desuspension (AP45).
compute/lib/coha_bar_bridge_engine.py:93:  - Bar uses desuspension: B(A) = T^c(s^{-1} A_bar)
compute/lib/bar_cohomology_virasoro_explicit_engine.py:59:  - Bar degree k uses desuspension: |s^{-1}v| = |v| - 1 (AP45)
compute/lib/bar_cohomology_virasoro_explicit_engine.py:78:  AP45 (desuspension lowers degree)
compute/lib/cumulant_algebra.py:746:    the desuspension and Arnold relations.
compute/lib/cy_n4sca_k3_engine.py:1128:    AP45: desuspension LOWERS degree: |s^{-1}v| = |v| - 1.
compute/lib/cy_n4sca_k3_engine.py:1164:    # by the desuspension in the bar construction, since s^{-1} only shifts
compute/lib/feynman_integral_engine.py:47:    - Bar uses desuspension
compute/lib/curved_sc_higher_genus_engine.py:150:- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
compute/lib/curved_sc_higher_genus_engine.py:257:        """Sum of conformal weights (before desuspension shift)."""
compute/lib/curved_sc_higher_genus_engine.py:262:        """Cohomological degree after desuspension: sum(|a_i| - 1) = sum|a_i| - n.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '660,720p' compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    """Verify that Koszul duality decomposes along the product C x R.

    Vol II factorization_swiss_cheese.tex, Remark rem:CG-koszul (line 1611):
    - R-direction: E_1 Koszul duality (bar-cobar for associative algebras)
    - Sigma_g-direction: chiral Koszul duality (Vol I Theorem A)
    - Combined: Swiss-cheese Koszul duality

    This decomposition is the content of the Ayala-Francis framework [AF15]
    applied to the product FM_k(C) x Conf_k(R).

    Returns: dict with verification.
    """
    return {
        "R_direction": {
            "type": "E_1 Koszul duality",
            "source": "Ayala-Francis, Lurie HA Thm 5.4.5.9",
            "content": "bar-cobar for associative algebras",
        },
        "C_direction": {
            "type": "chiral Koszul duality",
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '720,780p' compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    bar_degree = n * deg_J - n  # = 3 - 3 = 0

    # The bar complex element [s^{-1}J | s^{-1}J | s^{-1}J] has
    # cohomological degree 0 and bar degree (tensor length) 3.

    return {
        "deg_J": deg_J,
        "deg_s_inv_J": deg_s_inv_J,
        "AP45_verified": deg_s_inv_J == 0,
        "bar_element_3_fold_degree": bar_degree,
        "convention": "desuspension LOWERS degree by 1",
    }


# ============================================================================
# Section 13: Shadow depth classification
# ============================================================================

def verify_shadow_depth_classification():
    """Verify the four-class shadow depth classification.

thinking
**Confirming conventions and dimension checks**

I'm reviewing the function verifying C15 related to desuspension conventions by checking code around line 697. I want to clarify any overlap or confusion between C16 and C07 about E8 fundamental dimensions by cross-referencing the CLAUDE snippet listings in the specified line ranges. I'll use precise line inspections to ensure the classification and mappings are correct.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '219,350p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).

**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).

**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).

**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).

**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.

**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).

**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).

**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).

**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).

**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/true_formula_census_verifier.py | sed -n '330,460p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   330	    Anti-pattern guard:
   331	      AP1: Virasoro is the unique standard family with kappa = c / 2.
   332	      AP24: the Virasoro complementarity sum is 13, not 0.
   333	
   334	    Citation:
   335	      True Formula Census Wave 12-2 C2 and landscape_census.tex.
   336	    """
   337	    expected = {
   338	        "c=0": Fraction(0),
   339	        "c=13": Fraction(13, 2),
   340	        "c=26": Fraction(13),
   341	    }
   342	    computed = {
   343	        "c=0": kappa_virasoro(0),
   344	        "c=13": kappa_virasoro(13),
   345	        "c=26": kappa_virasoro(26),
   346	    }
   347	    return _make_result("C02", "Virasoro kappa", expected, computed)
   348	
   349	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/true_formula_census_verifier.py | sed -n '452,640p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   452	def verify_C07() -> ResultDict:
   453	    """C07. Canonical data: the E_8 fundamental dimensions form a fixed set.
   454	
   455	    Anti-pattern guard:
   456	      Wave 10-8 / AP-style memory pollution inserted 779247, which is not
   457	      a fundamental E_8 dimension.
   458	
   459	    Citation:
   460	      True Formula Census Wave 12-2 C16; Bourbaki tables; local E_8 engines.
   461	    """
   462	    expected = E8_FUNDAMENTAL_DIMENSIONS
   463	    computed = compute_e8_fundamental_dimensions()
   464	    result = _make_result("C07", "E_8 fundamental dimensions", expected, computed)
   465	    result["passed"] = result["passed"] and validate_e8_fundamental_dimensions(computed)
   466	    return result
   467	
   468	
   469	def verify_C08() -> ResultDict:
   470	    """C08. Canonical formula: H_N = sum_{j=1}^N 1 / j exactly.
   471	
wait(call_8WSmkEmNYkQEDInjXAGHTlGt) timed out:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C17" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/twisted_holography_comparison_engine.py:32:  [C17]   Costello, "Holography and Koszul duality: the example of the M2
compute/lib/twisted_holography_comparison_engine.py:82:            of CS-matter). Costello [C17] identifies boundary = Yangian(gl_N).
compute/lib/twisted_holography_comparison_engine.py:249:    Extracted from the published papers [CG18, C17, CP20, CDG20].
compute/lib/twisted_holography_comparison_engine.py:300:    """Costello's M2 brane setup from [C17].
compute/lib/twisted_holography_comparison_engine.py:566:    """Compare Costello's M2 brane [C17] with our framework."""
compute/lib/twisted_holography_comparison_engine.py:924:    Costello [C17]: boundary = Yangian(gl_N), Koszul dual = U_{hbar}(Diff(C) x gl_N).
compute/lib/koszul_conductor_table_engine.py:156:# Principal W_N algebras  (C4, C17, C19)
compute/lib/theorem_preface_positioning_engine.py:24:  C17 -- D_Ran(B(A)) = A^!_infty (Verdier), NOT A (AP25)
collab wait(call_I4BJuFZ6uUws9Z8xu6HgoTHW)
  receivers: 019d840d-fcf5-7913-9b82-6563547cf202
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "W_N.*weight" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/chirhoch_bershadsky_polyakov_engine.py:482:    which is absent in principal W_N (where the lowest-weight generator
compute/lib/rectification_delta_f2_verify_engine.py:27:  - Channels: T (weight 2), W_3 (weight 3), ..., W_N (weight N)
compute/lib/wn_channel_refined.py:4:generating fields W_2 = T, W_3, ..., W_N of conformal weights 2, 3, ..., N.
compute/lib/agt_nekrasov_shadow_engine.py:1023:    For the principal W_N algebra with generators of weights 2, 3, ..., N:
compute/lib/shadow_cohft_rmatrix_engine.py:58:For W_N with N-1 primaries of weights h_1, ..., h_{N-1}:
compute/lib/shadow_cohft_rmatrix_engine.py:642:    For W_N with primaries of weights 2, 3, ..., N:
compute/lib/theorem_pva_deformation_quantization_frontier_engine.py:551:    For the W_N algebra with generators T, W_3, ..., W_N (weights 2, 3, ..., N),
compute/lib/dirichlet_sewing.py:298:    sl_N -> W_N. The j-th factor removes modes at conformal weight j.
compute/lib/mg_kuranishi_parity_engine.py:983:    W_N has generators W_2 = T, W_3, ..., W_N of weights 2, 3, ..., N.
compute/lib/mg_kuranishi_parity_engine.py:1003:    Key finding: for N >= 3, W_N has generators of MULTIPLE weights
compute/lib/higher_w_shadows.py:3:W_N (principal DS reduction of sl_N-hat) has N-1 generators of weights 2, 3, ..., N.
compute/lib/w_infinity_string_engine.py:17:     B(W_N) stabilizes at each weight as N increases.  Stabilization
compute/lib/w_infinity_string_engine.py:362:    """Dimension of weight-w sector of bar cohomology H^*(B(W_N)) at weight w.
compute/lib/bar_cohomology_wn_universal_engine.py:7:W_N has (N-1) strong generators of conformal weights 2, 3, ..., N.
compute/lib/bar_cohomology_wn_universal_engine.py:96:    W_N has strong generators of conformal weights 2, 3, ..., N.
compute/lib/bar_cohomology_wn_universal_engine.py:500:    """Ratio chi_{sl_N}(q) / chi_{W_N}(q) at each weight.
compute/lib/bar_cohomology_wn_universal_engine.py:527:    """dim V-bar_h(W_N) as a function of N for fixed weight h."""
compute/lib/bv_bar_coderived_engine.py:633:    W_N has generators W_2 = T (weight 2), W_3 (weight 3), ..., W_N (weight N).
compute/lib/integrable_genus2_engine.py:679:    The W_N algebra has N-1 generators of conformal weights 2, 3, ..., N.
compute/lib/integrable_genus2_engine.py:689:    For W_N with N >= 3, the generators have DIFFERENT conformal weights,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,160p' compute/lib/wn_channel_refined.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
"""Channel-refined modular characteristic for W_N algebras.

The W_N algebra (principal DS reduction of sl_N-hat at level k) has N-1
generating fields W_2 = T, W_3, ..., W_N of conformal weights 2, 3, ..., N.

The scalar modular characteristic is:
    kappa(W_N) = c * (H_N - 1)
where H_N = 1 + 1/2 + ... + 1/N is the N-th harmonic number and c is
the central charge.

CHANNEL REFINEMENT (concordance.tex, Future 4):
Each generator W_j contributes a channel kappa_j to the total:
    kappa_j = c / j
from the self-coupling W_j(z)W_j(w) ~ (c/j) / (z-w)^{2j} + ...

The channel-refined characteristic is the vector:
    kappa_tilde_N = (kappa_2, kappa_3, ..., kappa_N) = (c/2, c/3, ..., c/N)

Key properties:
    1. Total: sum_{j=2}^N kappa_j = c * (H_N - 1) = kappa(W_N)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "def verify" compute/lib/wn_channel_refined.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
182:def verify_cross_term_vanishing(N: int) -> bool:
255:def verify_sugawara_channel(N: int, level) -> Dict[str, object]:
346:def verify_w4_consistency() -> Dict[str, bool]:
377:def verify_sigma_consistency(max_N: int = 4) -> Dict[str, bool]:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '180,260p' compute/lib/wn_channel_refined.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:


def verify_cross_term_vanishing(N: int) -> bool:
    """Verify that all off-diagonal cross-terms vanish."""
    matrix = cross_term_matrix(N)
    return all(matrix[(i, j)] == 0
               for i in range(2, N + 1)
               for j in range(2, N + 1)
               if i != j)


# ---------------------------------------------------------------------------
# Pole-order argument for cross-term vanishing
# ---------------------------------------------------------------------------

def ope_max_pole_order(i: int, j: int) -> int:
    """Maximum pole order in W_i(z) W_j(w) OPE.

    For i == j: pole order 2i (from the 2-point function normalization).
    For i != j: pole order i + j - 1 (conformal weight bound).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '260,360p' compute/lib/wn_channel_refined.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    but the curvature kappa_2 = c_DS / 2 still holds because T is normalized
    the same way.
    """
    k = sympify(level)
    c = wn_central_charge(N, k)
    kap2 = channel_kappa(2, c)
    return {
        "central_charge": c,
        "kappa_2": kap2,
        "equals_c_over_2": simplify(kap2 - c / 2) == 0,
    }


# ---------------------------------------------------------------------------
# Specific W_N algebras
# ---------------------------------------------------------------------------

def w3_channel_data(central_charge=None) -> Dict[str, object]:
    """Channel data for W_3: generators T (spin 2), W (spin 3).

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '60,200p' compute/lib/koszul_conductor_table_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
def heisenberg_dual_kappa(k: Fraction) -> Fraction:
    """kappa(H_k^!) = -k.  Complementarity: kappa + kappa' = 0.  (C18)"""
    return -Fraction(k)


def heisenberg_K_cc() -> Fraction:
    """c + c' = 1 + 1 = 2 for Heisenberg (both sides c=1)."""
    return Fraction(2)


def heisenberg_K_kk(k: Fraction) -> Fraction:
    """K_kk = kappa + kappa' = 0.  (C18: KM/Heis/lattice/free)"""
    return heisenberg_kappa(k) + heisenberg_dual_kappa(k)


# ---------------------------------------------------------------------------
# Virasoro  (C2, C8, C11)
# ---------------------------------------------------------------------------

def virasoro_c(c: Fraction) -> Fraction:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "def verify" compute/lib/koszul_conductor_table_engine.py' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C18" compute/lib/complementarity_cross_verification.py' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "K_kk" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/koszul_conductor_table_engine.py:7:  K_kk(A) = kappa(A) + kappa(A^!)  (Koszul conductor)
compute/lib/koszul_conductor_table_engine.py:9:The Koszul conductor K_kk is the invariant called K(A) in the monograph
compute/lib/koszul_conductor_table_engine.py:12:  K_kk = 0       for KM, Heisenberg, lattice, free families
compute/lib/koszul_conductor_table_engine.py:13:  K_kk = 13      for Virasoro
compute/lib/koszul_conductor_table_engine.py:14:  K_kk = 250/3   for W_3
compute/lib/koszul_conductor_table_engine.py:15:  K_kk = 196     for Bershadsky-Polyakov
compute/lib/koszul_conductor_table_engine.py:70:def heisenberg_K_kk(k: Fraction) -> Fraction:
compute/lib/koszul_conductor_table_engine.py:71:    """K_kk = kappa + kappa' = 0.  (C18: KM/Heis/lattice/free)"""
compute/lib/koszul_conductor_table_engine.py:104:def virasoro_K_kk(c: Fraction) -> Fraction:
compute/lib/koszul_conductor_table_engine.py:105:    """K_kk = kappa + kappa' = c/2 + (26-c)/2 = 13.  (C18)"""
compute/lib/koszul_conductor_table_engine.py:150:def km_K_kk(dim_g: int, h_v: int, k: Fraction) -> Fraction:
compute/lib/koszul_conductor_table_engine.py:151:    """K_kk = kappa + kappa' = 0 for affine KM.  (C18)"""
compute/lib/koszul_conductor_table_engine.py:174:def wn_K_kk(c: Fraction, c_dual: Fraction, n: int) -> Fraction:
compute/lib/koszul_conductor_table_engine.py:175:    """K_kk = kappa(W_N, c) + kappa(W_N, c')."""
compute/lib/koszul_conductor_table_engine.py:180:# W_2 = Vir: c' = 26 - c, K_kk = 13.
compute/lib/koszul_conductor_table_engine.py:181:# W_3: c' = 250/3 - c  (from K_kk = 250/3 at all c).
compute/lib/koszul_conductor_table_engine.py:182:# General W_N: K_kk = K_N is a constant independent of c.
compute/lib/koszul_conductor_table_engine.py:189:      W_2: c + c' = 26,  K_kk = 26 * (3/2 - 1) = 26 * 1/2 = 13
compute/lib/koszul_conductor_table_engine.py:190:      W_3: K_kk = 250/3 (C18)
compute/lib/koszul_conductor_table_engine.py:207:      W_3: c + c' = 100  (derived from K_kk = 250/3 and H_3 - 1 = 5/6)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '600,720p' compute/lib/koszul_conductor_table_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
                         k_bp: Fraction = Fraction(1),
                         lattice_rank: int = 8,
                         ) -> Dict[str, Dict[str, Fraction]]:
    """Build the full Koszul conductor table for all families.

    Returns dict of family -> {c, c_dual, K_cc, kappa, kappa_dual, K_kk}.
    Parameters allow evaluating at specific points.
    """
    table = {}

    # Heisenberg
    k_heis = k_km  # use same level for convenience
    table["Heisenberg"] = {
        "c": heisenberg_c(),
        "c_dual": heisenberg_c(),
        "K_cc": heisenberg_K_cc(),
        "K_kk": heisenberg_K_kk(k_heis),
    }

    # Virasoro
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C21" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_preface_positioning_engine.py:28:  C21 -- Visibility formula g_min(S_r) = floor(r/2) + 1
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "kappa_BKM" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/twisted_sugra_shadow_engine.py:304:      kappa(A) = 3, kappa_BCOV = 0, kappa_MacMahon = 0, kappa_BKM = 5.
compute/lib/twisted_sugra_shadow_engine.py:334:    (iv)  kappa_BKM: weight of automorphic form (for K3-fibered)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Phi_10" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/cy_elliptic_genus_k3e_engine.py:1323:        sum_{N>=0} p^N Z(Sym^N(K3); tau, z) = 1/Phi_10(Omega)
compute/lib/cy_elliptic_genus_k3e_engine.py:1324:    where Phi_10 is the Igusa cusp form (weight 10 Siegel modular
compute/lib/cy_elliptic_genus_k3e_engine.py:1335:        siegel_connection="DMVV formula -> 1/Phi_10 (Igusa cusp form)",
compute/lib/coderived_artifact.py:757:    where Phi_10 is the Igusa cusp form of weight 10 on Sp(4, Z),
compute/lib/coderived_artifact.py:808:    2. Siegel cusp forms (e.g., the weight-10 Igusa cusp form Phi_10)
compute/lib/cy_grand_atlas_k3e_engine.py:26:  BPS from DVV: 1/Phi_10           (Igusa cusp form inverse)
compute/lib/cy_grand_atlas_k3e_engine.py:1426:            "title": "Does Z^sh(K3xE) relate to 1/Phi_10?",
compute/lib/cy_grand_atlas_k3e_engine.py:1429:                "1/Phi_10 both encode BPS data. The leading asymptotics match: "
compute/lib/cy_grand_atlas_k3e_engine.py:1434:                "genus expansion and the Fourier-Jacobi expansion of 1/Phi_10. "
compute/lib/cy_shadow_siegel_bridge_engine.py:7:obstruction tower and the Igusa cusp form Phi_10, building on the structural
compute/lib/cy_shadow_siegel_bridge_engine.py:9:does NOT directly produce Phi_10). Here we compute the precise BRIDGE.
compute/lib/cy_shadow_siegel_bridge_engine.py:18:(b) Igusa cusp form Phi_10(Omega), a FUNCTION on H_2 (the genus-2 Siegel
compute/lib/cy_shadow_siegel_bridge_engine.py:20:    Its reciprocal 1/Phi_10 is the DVV BPS partition function.
compute/lib/cy_shadow_siegel_bridge_engine.py:61:For K3 x E: Z_2 is related to 1/Phi_10 via DVV, and F_2 is the result
compute/lib/cy_shadow_siegel_bridge_engine.py:74:1/Phi_10              | FULL genus-2 BPS partition function (DVV)
compute/lib/cy_shadow_siegel_bridge_engine.py:75:Shadow depth (class M)| Infinite product structure of Phi_10
compute/lib/cy_shadow_siegel_bridge_engine.py:82:1/Phi_10 is SECOND-QUANTIZED (DMVV symmetric product formula):
compute/lib/cy_shadow_siegel_bridge_engine.py:84:  1/Phi_10(Omega) = sum_{N>=0} p^N chi(Sym^N(K3); tau, z)
compute/lib/cy_shadow_siegel_bridge_engine.py:100:  Dijkgraaf-Verlinde-Verlinde (1997): Z_BPS = 1/Phi_10, hep-th/9608096
compute/lib/cy_shadow_siegel_bridge_engine.py:258:    """Object (b): data about Phi_10 on H_2.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/cy_second_quantization_engine.py | sed -n '820,880p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   820	    r"""Compute kappa_BPS / kappa_ch and verify = 5/3.
   821	
   822	    kappa_BPS = chi(K3)/4 - 1 = 24/4 - 1 = 5
   823	    kappa_ch = dim_C(K3 x E) = 3
   824	
   825	    Ratio = 5/3.
   826	
   827	    This ratio has a clean interpretation:
   828	    - The numerator 5 = chi(K3)/4 - 1 = h^{1,1}(K3)/4 + 1
   829	      (since h^{1,1}(K3) = 20, h^{2,0} = h^{0,2} = 1)
   830	      Actually: chi(K3) = 2 + 20 + 2 = 24 (from Hodge diamond).
   831	      chi/4 = 6. So 5 = 6 - 1.
   832	    - The denominator 3 = dim_C(K3 x E).
   833	
   834	    Alternative interpretation:
   835	    kappa_BPS = weight(Phi_10)/2 = 10/2 = 5.
   836	    kappa_ch = dim_C = 3.
   837	    """
   838	    kappa_bps = F(CHI_K3, 4) - 1  # = 24/4 - 1 = 5
   839	    kappa_ch = F(KAPPA_CH_K3E)     # = 3
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"q\\"'^'"\\{1/24\\}\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/cy_lattice_voa_k3_engine.py:116:  - eta(q) = q^{1/24} * prod_{n>=1}(1-q^n) (AP46: include q^{1/24})
compute/lib/bc_twisted_holography_zeta_engine.py:43:  - Dedekind eta: eta(q) = q^{1/24} * prod(1-q^n) (AP46)
compute/lib/bc_twisted_holography_zeta_engine.py:331:    r"""Dedekind eta function: eta(tau) = q^{1/24} * prod_{n>=1} (1 - q^n).
compute/lib/bc_twisted_holography_zeta_engine.py:333:    AP46: the q^{1/24} prefactor is NOT optional.
compute/lib/bc_twisted_holography_zeta_engine.py:345:    # q^{1/24}
compute/lib/bc_twisted_holography_zeta_engine.py:363:    Careful (AP46): eta(tau) = q^{1/24} prod(1-q^n).
compute/lib/bc_twisted_holography_zeta_engine.py:364:    So prod(1-q^n) = eta(tau) / q^{1/24} = eta(tau) * q^{-1/24}.
compute/lib/bc_twisted_holography_zeta_engine.py:374:        Z(tau) = q^{-c/24} / prod_{n>=1}(1-q^n) = q^{-c/24} / (eta/q^{1/24})
compute/lib/k3_relative_chiral.py:77:  - eta(q) = q^{1/24} * prod(1-q^n) (AP46: include q^{1/24})
compute/lib/k3_relative_chiral.py:1234:    Meanwhile, 1/eta(q)^{24} = q^{-1} * prod(1-q^k)^{-24} (AP46: eta includes q^{1/24}).
compute/lib/cy_elliptic_genus_k3e_engine.py:46:  - eta(q) = q^{1/24} * prod(1-q^n) [AP46: include q^{1/24}]
compute/lib/cy_mathieu_moonshine_engine.py:58:  - eta(q) = q^{1/24} * prod(1 - q^n)  [AP46: include q^{1/24}]
compute/lib/cy_mathieu_moonshine_engine.py:287:    Note: eta(tau) = q^{1/24} * prod(1-q^n) (AP46).
compute/lib/cy_mathieu_moonshine_engine.py:288:    This returns the product WITHOUT the q^{1/24} prefactor.
compute/lib/cy_n4sca_k3_engine.py:100:  - eta(q) = q^{1/24} prod(1-q^n) (AP46)
compute/lib/cy_n4sca_k3_engine.py:211:    eta(tau) = q^{1/24} * sum c[n] q^n  (AP46: the q^{1/24} is separate).
compute/lib/rademacher_kloosterman.py:589:               = q^{1/24} * sum_n a_2(n) q^n
compute/lib/rademacher_kloosterman.py:625:    # 1/eta(q) = q^{-1/24} / prod(1-q^n) -> prod(1-q^n) = q^{1/24} * eta
compute/lib/rademacher_kloosterman.py:735:    Since chi_{r,s} = q^{h-c/24} * sum a(n)q^n, and 1/eta = q^{1/24} * sum p(n)q^n,
compute/lib/rademacher_kloosterman.py:753:    # eta(q) = q^{1/24} * prod(1-q^n), so 1/eta = q^{-1/24} * sum p(n)q^n
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '230,270p' compute/lib/ordered_trace_invariant_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    """
    q = cmath.exp(1j * PI * tau)
    result = 1.0 + 0.0j
    for n in range(1, n_terms + 1):
        sgn = (-1) ** n
        q_pow = q ** (n * n)
        result += 2.0 * sgn * q_pow * cmath.cos(2 * n * PI * z)
    return result


def eta_dedekind(tau: complex, n_terms: int = 200) -> complex:
    r"""Dedekind eta function.

    eta(tau) = q^{1/24} prod_{n=1}^{infty} (1 - q^n)

    where q = e^{2*pi*i*tau}.  The q^{1/24} is ESSENTIAL (C22/FM13).
    """
    q = cmath.exp(TWO_PI_I * tau)
    # q^{1/24}
    prefactor = cmath.exp(TWO_PI_I * tau / 24.0)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/ordered_trace_invariant_engine.py | sed -n '230,270p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   230	    """
   231	    q = cmath.exp(1j * PI * tau)
   232	    result = 1.0 + 0.0j
   233	    for n in range(1, n_terms + 1):
   234	        sgn = (-1) ** n
   235	        q_pow = q ** (n * n)
   236	        result += 2.0 * sgn * q_pow * cmath.cos(2 * n * PI * z)
   237	    return result
   238	
   239	
   240	def eta_dedekind(tau: complex, n_terms: int = 200) -> complex:
   241	    r"""Dedekind eta function.
   242	
   243	    eta(tau) = q^{1/24} prod_{n=1}^{infty} (1 - q^n)
   244	
   245	    where q = e^{2*pi*i*tau}.  The q^{1/24} is ESSENTIAL (C22/FM13).
   246	    """
   247	    q = cmath.exp(TWO_PI_I * tau)
   248	    # q^{1/24}
   249	    prefactor = cmath.exp(TWO_PI_I * tau / 24.0)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,220p' compute/lib/bicoloured_partition_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Bicoloured partition numbers and 1/eta^2 q-expansion engine.

MATHEMATICAL FRAMEWORK
======================

The Dedekind eta function is:

    eta(tau) = q^{1/24} * prod_{n >= 1} (1 - q^n),   q = e^{2*pi*i*tau}

The inverse square 1/eta(tau)^2 has q-expansion:

    1/eta(tau)^2 = q^{-1/12} * sum_{n >= 0} p_{-2}(n) * q^n

where p_{-2}(n) are the **bicoloured partition numbers** (OEIS A000712):
the number of partitions of n into parts of 2 colours.

Equivalently, the generating function for bicoloured partitions is:

    sum_{n >= 0} p_{-2}(n) * q^n = prod_{n >= 1} 1/(1 - q^n)^2

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"1/\\(2\\*pi\\*i\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/bc_isomonodromic_shadow_engine.py:27:   The RH factorization index kappa_RH = (1/(2*pi*i)) * oint d log det Y
compute/lib/bc_isomonodromic_shadow_engine.py:462:    kappa_RH = (1/(2*pi*i)) * oint d log det Y
compute/lib/modular_forms_shadow_engine.py:493:    The Serre derivative is theta = q d/dq = (1/(2*pi*i)) d/dtau.
compute/lib/modular_forms_shadow_engine.py:516:    where D = (1/(2*pi*i)) d/dtau = q d/dq is the normalized derivative.
compute/lib/resurgence_trans_series_engine.py:946:    # F_g ~ S_1/(2*pi*i) * A_1^{-2g} * (2g-1)! at leading order in hbar-plane.
compute/lib/resurgence_arithmetic_frontier_engine.py:882:        S_r^{(1)} = (1/(2*pi*i)) * oint sqrt(Q_L(t)) / t^{r+1} dt
compute/lib/shadow_mzv_engine.py:1227:      Order 1: coefficient involves 1/(2*pi*i) -- the linking number
compute/lib/bc_shadow_zeta_zeros_engine.py:549:        (1/(2*pi*i)) * oint (zeta'/zeta)(s) ds = N - P
compute/lib/bc_shadow_zeta_zeros_engine.py:570:        """Compute (1/(2*pi*i)) * integral of zeta'/zeta along segment."""
compute/lib/bc_nc_chernweil_shadow_engine.py:337:    """Integrated first Chern class: c_1 = (1/(2*pi*i)) oint F.
compute/lib/bc_period_torelli_shadow_engine.py:103:    tau(c) ~ (1/(2*pi*i)) * N * log(c) + tau_0 + O(c)
compute/lib/bc_period_torelli_shadow_engine.py:958:        tau(c) ~ (1/(2*pi*i)) * N * log(c) + tau_0 + O(c)
compute/lib/bc_period_torelli_shadow_engine.py:970:    This is NOT of the form (1/(2*pi*i))*N*log(c) -- it is a POLE, not a log.
compute/lib/bc_period_torelli_shadow_engine.py:1040:        tau(c) ~ (1/(2*pi*i)) * N * log(c - c_LY) + tau_0
compute/lib/shadow_singularity_map.py:979:    # G(t) = (1/(2*pi*i)) * integral disc(G)/(t'-t) dt'
compute/lib/shadow_singularity_map.py:980:    #       = (1/(2*pi*i)) * (-2*pi*i) * integral dt'/(t'-t)
compute/lib/resurgence_deep_engine.py:753:    S_r ~ S_1/(2*pi*i) * omega_1^{-r} * Gamma(r - 1/2) / Gamma(r+1) * ...
compute/lib/frontier_defect_explicit_engine.py:1161:    On a punctured region, [Omega] = (1/(2*pi*i)) * int_gamma Omega.
compute/lib/frontier_defect_explicit_engine.py:1183:    Res_{s_0}(Omega) = (1/(2*pi*i)) * int_{|s-s_0|=r} Omega(s) ds
compute/lib/theorem_analytic_o1_attack_engine.py:1112:      F_g = lim_{cusp} (-1/(2*pi*i) * d/dtau * log Z_g)|_{leading}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '700,780p' compute/lib/theorem_shadow_conformal_block_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    """
    Delta = 8 * kappa_val * S4_val
    Delta_simple = simplify(Delta)

    if Delta_simple == 0:
        S3_simple = simplify(S3_val)
        if S3_simple == 0:
            return 'G', 2, "Degenerate spectral curve (y = constant)"
        else:
            return 'L', 3, "Perfect-square spectral curve (double branch point)"
    else:
        return 'M', float('inf'), "Irreducible spectral curve (two distinct branch points)"


# ============================================================================
# 10. Numerical verification suite
# ============================================================================

def verify_cauchy_formula_numerically(r, c_num, n_points=10000):
    """Verify S_r = (1/(2*pi*i*r)) * oint sqrt(Q_L(z)) / z^{r-1} dz numerically.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "MC" compute/lib | head' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_hca_pillar_a_engine.py:5:    The Moore complex V = MC^bullet(U; A) admits a structure of a homotopy
compute/lib/theorem_hca_pillar_a_engine.py:369:# 3.  HCA OPERATIONS F_n AND THE MC ELEMENT Phi
compute/lib/theorem_hca_pillar_a_engine.py:392:        At arity 2: the MC equation at arity 2 gives [d_M, F_2] = 0.
compute/lib/theorem_hca_pillar_a_engine.py:393:        At higher arity: F_n is a chain map iff it's part of an MC element.
compute/lib/theorem_hca_pillar_a_engine.py:410:    The MC equation D Phi + (1/2)[Phi, Phi] = 0 decomposes by arity:
compute/lib/theorem_hca_pillar_a_engine.py:427:        """The MC equation at arity n, as a symbolic expression.
compute/lib/theorem_hca_pillar_a_engine.py:828:    intertwining the Cech MC element with the genus-0 bar MC element.
compute/lib/theorem_hca_pillar_a_engine.py:1052:    morphism between Cech and bar MC elements).  MS24 provides the
compute/lib/cusp_form_shadow_arity.py:61:  This is the MC-framework manifestation of the Ramanujan conjecture:
compute/lib/frontier_verifications.py:5:TASK 1: MC recursion destroys multiplicativity — deeper analysis.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"d\\*Theta\" -n compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_shadow_tower_physics_bridge_engine.py:1140:        d*Theta_{g=1} + [Theta_{g=0}, Theta_{g=1}] = 0
compute/lib/categorical_shadow_engine.py:761:      - degree 1: the MC equation data (d*Theta + 1/2[Theta,Theta] = 0)
compute/lib/wild_quiver_chiral_engine.py:706:    d*Theta + (1/2)[Theta, Theta] = 0 has NO SOLUTION in the formal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1120,1165p' compute/lib/theorem_shadow_tower_physics_bridge_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
        if n < 3:
            residuals[r] = Fraction(0)
            continue

        # a_j = (j+2)*S_{j+2}, a_0 = 2*kappa
        def a(j):
            return (j + 2) * tower.get(j + 2, Fraction(0))

        total = 2 * a(0) * a(n)
        for j in range(1, n):
            total += a(j) * a(n - j)
        residuals[r] = total

    return residuals


def mc_verification_genus1_scalar(N: int) -> Dict[str, Fraction]:
    r"""Verify the genus-1 MC equation for affine sl_N.

    At genus 1, the MC equation gives:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/depth_classification.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""G/L/C/M depth classification and total depth decomposition d = 1 + d_arith + d_alg.

The shadow depth of a modular Koszul chiral algebra decomposes as

    d(A) = 1 + d_arith(A) + d_alg(A)

where:
    d_alg  = algebraic (homotopy) depth: how far the transferred A_infinity
             products m_n extend before vanishing.
             G: d_alg = 0  (all m_n = 0 for n >= 3)
             L: d_alg = 1  (m_3 != 0, m_n = 0 for n >= 4)
             C: d_alg = 2  (m_3, m_4 != 0, m_n = 0 for n >= 5)
             M: d_alg = infinity  (m_n != 0 for infinitely many n)

    d_arith = arithmetic depth: the number of independent holomorphic Hecke
              eigenforms in the Roelcke-Selberg spectral decomposition of
              the partition function Z(tau, bar{tau}) on M_{1,1}.

For even unimodular lattice VOAs of rank r >= 8:
    d_arith = 2 + dim S_{r/2}(SL(2,Z))
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ChirHoch" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 714

compute/lib/bc_derived_moduli_shadow_engine.py:363:    ChirHoch* polynomial in degrees {0,1,2}).
compute/lib/hh_heisenberg_e3_engine.py:45:  De Leger, arXiv:2512.20167: SC(E_2) ~ SC_2 gives E_3 on ChirHoch
compute/lib/ds_chirhoch_compatibility_engine.py:1:r"""DS-ChirHoch compatibility engine: falsification test FT-4.
compute/lib/ds_chirhoch_compatibility_engine.py:7:maps ChirHoch^1(V_k(sl_2)) = sl_2 to ChirHoch^1(Vir_c) = 0.
compute/lib/ds_chirhoch_compatibility_engine.py:11:  (A) prop:chirhoch1-affine-km: ChirHoch^1(V_k(g)) = g (generic k).
compute/lib/ds_chirhoch_compatibility_engine.py:12:  (B) chirhoch_virasoro(): ChirHoch^1(Vir_c) = 0 (generic c).
compute/lib/ds_chirhoch_compatibility_engine.py:15:    DS_*: ChirHoch^1(V_k(sl_2)) -> ChirHoch^1(Vir_{c(k)})
compute/lib/ds_chirhoch_compatibility_engine.py:21:ChirHoch^1(V_k(sl_2)) = sl_2 is spanned by three outer derivations
compute/lib/ds_chirhoch_compatibility_engine.py:54:ChirHoch^1(Vir_c) = 0.
compute/lib/ds_chirhoch_compatibility_engine.py:72:ChirHoch^1(W_N) = 0 for the principal W-algebra.
compute/lib/ds_chirhoch_compatibility_engine.py:78:  chi(ChirHoch^1(V_k(sl_2))) = 3
compute/lib/ds_chirhoch_compatibility_engine.py:79:  chi(ChirHoch^1(Vir_c)) = 0
compute/lib/ds_chirhoch_compatibility_engine.py:92:  ChirHoch^1(V_k(sl_N)) = sl_N, dim = N^2 - 1
compute/lib/ds_chirhoch_compatibility_engine.py:93:  ChirHoch^1(W_N) = 0 (all derivations inner for N >= 2)
compute/lib/ds_chirhoch_compatibility_engine.py:181:    chirhoch1_contribution: int  # 0 (all become trivial in ChirHoch^1)
compute/lib/ds_chirhoch_compatibility_engine.py:237:    ChirHoch^1(W_N) = 0.
compute/lib/ds_chirhoch_compatibility_engine.py:293:      dim_source: dim ChirHoch^1(V_k(sl_N)) = N^2 - 1
compute/lib/ds_chirhoch_compatibility_engine.py:294:      dim_target: dim ChirHoch^1(W_N) = 0
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "verify" compute/lib/chiral_hochschild_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
1032:def verify_additivity_under_tensor(
1074:def verify_euler_char_additivity(
1319:def verify_theorem_h_complete(data: ChiralAlgebraData) -> Dict[str, Any]:
1373:def verify_universal_polynomial() -> Dict[str, Any]:
1410:def verify_km_h1_equals_dim_g() -> Dict[str, Any]:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1310,1360p' compute/lib/chiral_hochschild_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
        'w5': wN_data(5),
    }
    return {name: compute_chirhoch(data) for name, data in families.items()}


# ============================================================
# Section 12: Verification suite
# ============================================================

def verify_theorem_h_complete(data: ChiralAlgebraData) -> Dict[str, Any]:
    """Complete Theorem H verification for one family.

    Checks:
    1. Concentration in {0, 1, 2} (quadratic) or non-negativity (W-algebra)
    2. Polynomial P_A(t) has correct coefficients
    3. Koszul functoriality: P_A determines P_{A!}
    4. Deformations are unobstructed
    5. Euler characteristic
    """
    result = compute_chirhoch(data)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dz_\\{ij\\}\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/theorem_w3_commuting_hamiltonians_engine.py:841:    #   H_i = sum_j [h_j/z_{ij}^2 + d/dz_{ij}]
compute/lib/en_koszul_bridge.py:191:    the numerators are all equal (= dz_{ij} ^ dz_{jk}) and the sum of the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "nabla_KZ" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/mzv_bar_complex.py:989:      nabla_KZ = d - 1/(k + h^v) * sum_{i<j} Omega_{ij} / (z_i - z_j)
compute/lib/theorem_dk0_evaluation_bridge_engine.py:138:    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
compute/lib/e1_nonsplitting_obstruction_engine.py:666:        nabla_KZ = d - (1/(k+h^v)) (Omega_12 dlog(z12) + Omega_23 dlog(z23))
compute/lib/primitive_kernel_full.py:874:        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
compute/lib/primitive_kernel_full.py:881:        nabla_KZ = d - (1/(k+N)) * Omega_{12} * d log(z_1 - z_2)
compute/lib/primitive_kernel_full.py:885:    At genus 0, this gives nabla_KZ.
compute/lib/kz_shadow_connection.py:4:  nabla_KZ = d - Sigma_{i<j} Omega_{ij}/(z_i - z_j)
compute/lib/kz_shadow_connection.py:502:      nabla^{shadow}_{0,2} = nabla_KZ
compute/lib/kz_shadow_connection.py:595:        'identification': 'nabla^{shadow}_{0,2} = nabla_KZ (thm:yangian-shadow-theorem)',
compute/lib/kz_shadow_connection.py:1068:            'kz': 'KZ connection nabla_KZ = d - 1/(k+h^v) sum Omega_{ij}/(z_i-z_j)',
compute/lib/geometric_langlands_shadow_engine.py:874:      nabla_KZ = d - Omega/(k+2) * sum_{i<j} dz_i/(z_i - z_j)
compute/lib/geometric_langlands_shadow_engine.py:993:      nabla_KZ = d - (1/(k+2)) sum_{i<j} Omega_{ij} d(z_i-z_j)/(z_i-z_j)
compute/lib/dmod_filtration_ss_engine.py:439:    nabla_KZ = d - 1/(k+2) sum_{i<j} Omega_{ij} d log(z_i - z_j)
compute/lib/theorem_mc5_analytic_rectification_engine.py:593:    4. The KZ connection nabla_KZ = d - (1/3) sum Omega_{ij}/(z_i-z_j) dz_i
compute/lib/theorem_mc5_analytic_rectification_engine.py:1432:      nabla_KZ = d - (Omega / (3z)) dz
compute/lib/chriss_ginzburg_universal.py:20:           ->  nabla_KZ    (KZ connection)
compute/lib/kz_conformal_blocks.py:1540:            'identification': 'nabla^sh_{0,2} = nabla_KZ (PROVED)',
compute/lib/kz_conformal_blocks.py:1552:        'identification': 'nabla^sh_{0,2} = nabla_KZ (PROVED)',
compute/lib/hitchin_shadow_engine.py:49:       nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij}/(z_i - z_j)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' compute/lib/kz_shadow_connection.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
"""KZ connection from shadow obstruction tower: the proved recovery theorem.

The shadow obstruction tower at genus 0 produces the KZ connection:
  nabla_KZ = d - Sigma_{i<j} Omega_{ij}/(z_i - z_j)

This is the arity-2 shadow connection.  Higher arities give
L_infinity corrections from collision geometry on FM_n.

The CYBE for r(z) = Omega/z follows from the Arnold relation on FM_3.

KEY PROVED IDENTIFICATIONS (thm:yangian-shadow-theorem):
  (1) r(z) = Res^{coll}_{0,2}(Theta_A) = Omega/z
  (2) KZ connection = shadow connection at genus 0, arity 2
  (3) CYBE follows from Arnold relation on FM_3(C)
  (4) IBR (infinitesimal braid relation) = flatness of KZ

For V_k(sl_N) on P^1 with n marked points z_1,...,z_n:
  dPhi/dz_i = 1/(k+h^v) * Sigma_{j != i} Omega_{ij}/(z_i - z_j) * Phi

where Phi(z_1,...,z_n) is the conformal block (n-point correlator)
wait(call_I4BJuFZ6uUws9Z8xu6HgoTHW) timed out:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "connection" compute/lib/kz_shadow_connection.py | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1:"""KZ connection from shadow obstruction tower: the proved recovery theorem.
3:The shadow obstruction tower at genus 0 produces the KZ connection:
6:This is the arity-2 shadow connection.  Higher arities give
13:  (2) KZ connection = shadow connection at genus 0, arity 2
27:Higher-arity shadow connections:
36:  holographic_shadow_connection.py (Heisenberg/Arnold/flatness basics)
193:# 2. KZ connection matrix
196:def kz_connection_matrix(
202:    """KZ connection matrices A_i = (1/(k+h^v)) Sigma_{j!=i} Omega_{ij}/(z_i-z_j).
234:        raise ValueError(f"kz_connection_matrix not implemented for {lie_type} rep_dim={rep_dim}")
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/kz_shadow_connection.py | sed -n '193,250p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   193	# 2. KZ connection matrix
   194	# =========================================================================
   195	
   196	def kz_connection_matrix(
   197	    lie_type: str,
   198	    level: Fraction,
   199	    z_points: List[complex],
   200	    rep_dim: int = 2,
   201	) -> List[np.ndarray]:
   202	    """KZ connection matrices A_i = (1/(k+h^v)) Sigma_{j!=i} Omega_{ij}/(z_i-z_j).
   203	
   204	    The KZ system: dPhi/dz_i = A_i * Phi, where Phi is a vector in
   205	    V_1 tensor ... tensor V_n.
   206	
   207	    Args:
   208	        lie_type: 'sl2' or 'sl3'
   209	        level: the level k
   210	        z_points: list of n marked points [z_1, ..., z_n]
   211	        rep_dim: dimension of the representation (2 for fundamental of sl_2)
   212	
exec
/bin/zsh -lc "rg -n \"desusp|s\\"'^{-1}|degree shift|augmentation ideal|A-bar|deconcatenation" compute/lib/bar_complex.py compute/lib/curved_ainfty_bar_complex.py compute/lib/ordered_modular_bar.py compute/lib/bar_complex.py compute/lib/bar_presentation_koszul_dual_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' compute/lib/bar_complex.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/curved_ainfty_bar_complex.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/ordered_modular_bar.py" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:desusp|s\^{-1}|degree shift|augmentation ideal|A-bar|deconcatenation)
                  ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
"""Bar complex of a chiral algebra as an explicit chain complex.

For a chiral algebra A with OPE data, the bar complex is:
  B-bar(A) = (T^c(s^{-1}A-bar), d_bar)

where A-bar = A / C*vacuum (remove vacuum), and d_bar is determined by:
  - Simple pole residues -> Lie bracket component
  - Double pole residues -> curvature m_0

Bar degree n: B-bar^n = (s^{-1}A-bar)^{tensor n} / Arnold relations.

Arnold relations on FM_{n+1}(P^1):
  eta_{ij} wedge eta_{jk} + eta_{jk} wedge eta_{ki} + eta_{ki} wedge eta_{ij} = 0
reduce the dimension.  On C_n(P^1), dim H^{n-1}(C_n, C) = (n-1)! for the
top-degree cohomology relevant to bar degree n-1.

GRADING: Cohomological, |d| = +1.  Bar differential has bar-degree -1
(it maps B-bar^n -> B-bar^{n-1}).  In the internal (conformal weight) grading,
d has degree +1.

 succeeded in 53ms:
"""Curved A-infinity structures and bar complex d^2=0 verification.

The critical structural fact: d^2_bar = 0 ALWAYS (even when m_1^2 != 0).
For curved A-infinity (m_0 != 0): m_1^2(a) = [m_0, a] (graded commutator).

At genus 0: m_0=0, strict A-infinity, d^2=0 trivially.
At genus g>=1: m_0=kappa*omega_g, curved A-infinity, d^2=0 non-trivially.
The curvature m_1^2 = kappa*E_2*omega_1 at genus 1 (Arnold defect).

The hierarchy:
  1. Strict A-infinity (m_0=0): m_1^2=0, no curvature. Bar is ordinary dg coalgebra.
  2. Curved A-infinity (m_0!=0): m_1^2!=0 but d^2_bar=0. Bar is curved dg coalgebra.
  3. At genus 0: m_0=0, Arnold exact on P^1.
  4. At genus 1: m_0=kappa*omega_1 (Arakelov form), m_1^2=kappa*E_2*omega_1.
  5. At genus g: m_0=kappa*omega_g (Mumford class).

The A-infinity relations:
  Sum_{r+s+t=n} (-1)^{rs+t} m_{r+1+t}(a_1,...,a_r, m_s(a_{r+1},...,a_{r+s}), ..., a_n) = 0

At n=0: m_1(m_0) = 0  (m_0 is a cycle)
 succeeded in 52ms:
"""Genus-1 modular R-matrix corrections for the ordered bar complex.

Computes the genus-1 correction r₁(z; τ) to the binary R-matrix for
standard families.  At genus 0, r₀(z) = r(z) is the collision residue
of the universal MC element Θ_A.  At genus 1, the R-matrix acquires a
correction from the Weierstrass ℘-function (double-pole propagator on
the elliptic curve E_τ).

KEY RESULTS:
  1. Heisenberg: r₁(z; τ) = k · ℘(z; τ) (scalar, Weierstrass ℘)
     av(r₁) = κ · λ₁ where λ₁ is the first tautological class.
  2. Affine sl_2: r₁(z; τ) has a Casimir part + non-Casimir corrections.
  3. Modular R-matrix: R^mod(z; ℏ) = r₀(z) + ℏ² r₁(z; τ) + O(ℏ⁴)
     is a deformation of the genus-0 R-matrix.

The genus-1 correction measures the obstruction to extending the
genus-0 R-matrix data to higher genus.  For Heisenberg, the correction
is proportional to the Weierstrass ℘-function, reflecting the
replacement of 1/z² by ℘(z; τ) when passing from C to E_τ.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"Im\\s+Omega\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/bv_bar_genus2_comparison.py:34:    log det'(Delta_{Sigma_2}) = genus-independent + (1/6) log det(Im Omega)
compute/lib/bv_bar_genus2_comparison.py:479:    # Z_2(Heis) = det(Im Omega)^{k/2} * |chi_10(Omega)|^{-k/...}
compute/lib/coderived_artifact.py:21:  Z_exact = (det Im Omega)^{-1/2} (det'_zeta Delta)^{-1/2} for Heisenberg.
compute/lib/coderived_artifact.py:755:    Z_2 = 1 / |det(Im Omega_2)|^c * |Phi_{10}(Omega_2)|^{-c/5}
compute/lib/coderived_artifact.py:758:    and det(Im Omega_2) is the determinant of the imaginary part
compute/lib/coderived_artifact.py:762:    Z_2 = Theta_Siegel(Omega_2)^{2c} / (det(Im Omega_2))^{c/2} / (some normalization)
compute/lib/coderived_artifact.py:777:    # Z_2 = |theta|^{2c} / det(Im Omega)^{c/2}
compute/lib/coderived_artifact.py:865:    - Genus 2: Z_2 = Theta_Siegel^{2c} / det(Im Omega)^{c/2}, depends on 3 complex parameters
compute/lib/genus2_unfolding_erasure.py:321:      Z_2(Omega) = (det Im Omega)^{-k/2} * det(1 - K_Bergman)^{-k}
compute/lib/genus2_unfolding_erasure.py:645:      Z_2(Omega) = det(Im Omega)^{-k/2} / prod_{n>=1} det(1 - q1^n ... )^k
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:234:      P_harm = sum_{i,j} (Im Omega)^{-1}_{ij} omega_i(z) * bar{omega_j(w)}
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:978:      P_harm = sum_{i,j=1}^{2} (Im Omega)^{-1}_{ij} omega_i(z) omega_j(w)
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:1045:                'proportional to (Im Omega)^{-1}_{ij}. '
compute/lib/theorem_mc5_analytic_rectification_engine.py:16:    Z_g(H_k) = det(Im Omega)^{-k/2} * |det'_zeta Delta|^{-k}
compute/lib/theorem_mc5_analytic_rectification_engine.py:35:      Z_g(H_r; Omega) = det(Im Omega)^{-r/2}
compute/lib/theorem_mc5_analytic_rectification_engine.py:415:    """Genus-2 Heisenberg via the Siegel theta / det(Im Omega) formula.
compute/lib/theorem_mc5_analytic_rectification_engine.py:418:      Z_g^{full}(H_r; Omega) = det(Im Omega)^{-r/2}
compute/lib/theorem_mc5_analytic_rectification_engine.py:423:    At genus 2, Omega is 2x2 and det(Im Omega) = product of eigenvalues
compute/lib/theorem_mc5_analytic_rectification_engine.py:461:    3. Siegel theta / det(Im Omega)
compute/lib/theorem_nafcha_gluing_engine.py:392:      Z_2(H_k) = (det Im Omega_2)^{-k/2} * (det'_zeta Delta_{Sigma_2})^{-k/2}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "1/Im" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/bv_bar_coderived_engine.py:30:  As a scalar acting on the bar complex: omega_1 acts as 1/Im(tau)
compute/lib/bv_bar_coderived_engine.py:73:  - omega_1 acts as 1/Im(tau) on scalar sections of the bar complex
compute/lib/bv_bar_coderived_engine.py:128:      As scalar on bar complex sections: omega_1 acts as 1/Im(tau)
compute/lib/bv_bar_coderived_engine.py:136:    omega_1_scalar: str  # '1/Im(tau)'
compute/lib/bv_bar_coderived_engine.py:143:    The curvature m_0 = kappa * omega_1 where omega_1 acts as 1/Im(tau)
compute/lib/bv_bar_coderived_engine.py:185:        omega_1_scalar='1/Im(tau)',
compute/lib/bv_bar_coderived_engine.py:278:      The harmonic propagator P_harm = 1/Im(tau) is EXACTLY the
compute/lib/bv_bar_coderived_engine.py:350:    delta_4_coeff = kap * Q_contact  # coefficient of 1/Im(tau)
compute/lib/bv_bar_coderived_engine.py:351:    m_0_coeff = kap                  # coefficient of 1/Im(tau)
compute/lib/bv_bar_coderived_engine.py:566:    1. Compute delta_4 coefficient (of 1/Im(tau))
compute/lib/bv_bar_coderived_engine.py:587:        delta_4_coeff = Q_contact * kap  # coefficient of 1/Im(tau) in delta_4
compute/lib/bv_bar_coderived_engine.py:588:        m_0_coeff = kap                  # coefficient of 1/Im(tau) in m_0
compute/lib/bv_bar_coderived_engine.py:723:                   = S_r * (1/Im(tau))^{r/2-1}
compute/lib/bv_bar_coderived_engine.py:726:      (1/Im(tau))^{r/2-1} = (m_0 / kappa)^{r/2-1}
compute/lib/bv_bar_coderived_engine.py:729:    At arity 4 (r=4): delta_4 ~ S_4 * (1/Im(tau))^1 = S_4 * m_0 / kappa.
compute/lib/bv_bar_coderived_engine.py:732:    At arity 6 (r=6): delta_6 ~ S_6 * (1/Im(tau))^2 = S_6 * (m_0/kappa)^2
compute/lib/bv_bar_coderived_engine.py:771:        # Even arity r: delta_r ~ S_r * (1/Im(tau))^{r/2-1}
compute/lib/bv_bar_class_m_engine.py:305:      delta_4^{contact,harm} = [10/(c(5c+22))] * (c/2) * (1/Im(tau))
compute/lib/bv_bar_class_m_engine.py:364:        'moduli_dependence': '1/Im(tau)',
compute/lib/bv_bar_class_m_engine.py:379:    Returns the coefficient of 1/Im(tau) in the quartic discrepancy.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '20,90p' compute/lib/bv_bar_coderived_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

THE KEY COMPUTATION:
  The harmonic obstruction at (g=1, n=4) is:
    delta_4 = Q^contact * kappa / Im(tau)

  The curvature at genus 1 is:
    m_0 = kappa * omega_1

  The Arakelov form on E_tau is omega_1 = i dz ^ dz-bar / (2 Im(tau)).
  Integrated over E_tau: int omega_1 = 1.
  As a scalar acting on the bar complex: omega_1 acts as 1/Im(tau)
  (the modulus-dependent normalization).

  Therefore:
    delta_4 = Q^contact * kappa / Im(tau) = Q^contact * m_0

  The harmonic obstruction IS proportional to the curvature, with
  coefficient Q^contact (a pure algebraic constant depending only on c).

CONSEQUENCE FOR D^co:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Delta = 8" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 752

compute/lib/celestial_arithmetic_engine.py:445:    Delta = 8 * kappa * S_4 = 8 * (c/2) * 10/[c*(5c+22)] = 40/(5c+22).
compute/lib/celestial_arithmetic_engine.py:1373:    Path 4 (discriminant): Delta = 8*kappa*S_4 = 40/(5c+22).
compute/lib/theorem_holographic_c13_entanglement_engine.py:32:   Delta = 8*kappa*S_4 = 40/87.
compute/lib/theorem_holographic_c13_entanglement_engine.py:368:    Delta = 8*kappa*S_4 = 8*(13/2)*(10/1131) = 40/87.
compute/lib/theorem_holographic_c13_entanglement_engine.py:869:    Delta = 8 * kappa * S4
compute/lib/moonshine_shadow_depth.py:271:    """Delta = 8*kappa*S_4 = 0 for all Niemeier lattice VOAs."""
compute/lib/moonshine_shadow_depth.py:388:    Delta = 8 * kappa * S_4 = 8 * 12 * 5/1704 = 480/1704 = 20/71.
compute/lib/k3_relative_chiral.py:514:    # Critical discriminant: Delta = 8*kappa*S_4
compute/lib/bc_isomonodromic_shadow_engine.py:140:        Delta = 8 * kappa * S4
compute/lib/bc_isomonodromic_shadow_engine.py:160:        Delta = 8 * kappa * S4
compute/lib/bc_isomonodromic_shadow_engine.py:1044:    Delta = 8 * kappa * S4
compute/lib/bc_isomonodromic_shadow_engine.py:1072:    Delta = 8 * kappa * S4
compute/lib/bc_isomonodromic_shadow_engine.py:1099:    Delta = 8 * kappa * S4
compute/lib/cohft_givental_rmatrix_engine.py:393:    where Delta = 8*kappa*S4, the full parallel transport is:
compute/lib/cy_n4sca_k3_engine.py:93:  (c) The critical discriminant Delta = 8*kappa*S_4 != 0
compute/lib/cy_n4sca_k3_engine.py:1218:    The critical discriminant Delta = 8*kappa*S_4 is nonzero because
compute/lib/bc_matrix_model_shadow_engine.py:66:  with Delta = 8*kappa*S_4
compute/lib/bc_matrix_model_shadow_engine.py:1128:    Delta = 8 * kappa * S4
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,80p' compute/lib/discriminant_atlas.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Critical discriminant atlas: Delta = 8*kappa*S_4 for all standard families.

The critical discriminant Delta classifies shadow depth on each 1D primary
slice of the cyclic deformation complex:

    Delta = 0   <=>  Q_L(t) is a perfect square  <=>  tower terminates (G/L)
    Delta != 0  <=>  Q_L(t) is irreducible       <=>  tower infinite   (M)

The shadow metric on a primary line L is:

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

where kappa = modular characteristic, alpha = cubic shadow,
S_4 = quartic shadow, Delta = 8*kappa*S_4.

Discriminant complementarity (Virasoro family):

    Delta(Vir_c) + Delta(Vir_{26-c}) = 6960 / [(5c+22)(152-5c)]

with universal numerator 6960 = 2^4 * 3 * 5 * 29 = 40 * 174.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"kappa\\(BP\" compute/lib" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/sl3_subregular_bar.py:15:  2. kappa(BP_k) = (k-15)/(6(k+3)), verified by three independent paths.
compute/lib/sl3_subregular_bar.py:19:  6. The kappa deficit kappa(V_k(sl_3)) - kappa(BP_k) is a RATIONAL FUNCTION
compute/lib/sl3_subregular_bar.py:313:      2. The kappa deficit D(k) = kappa(V) - kappa(BP) is a rational function of k,
compute/lib/sl3_subregular_bar.py:569:    """Analyze the kappa deficit D(k) = kappa(V_k(sl_3)) - kappa(BP_k).
compute/lib/theorem_w_algebra_chapter_rectification_engine.py:166:    kappa(BP, k) = (1/6) * (2 - 24(k+1)^2/(k+3))
compute/lib/theorem_ap49_superconformal_engine.py:268:    """kappa(BP_k) = varrho * c = c(k)/6.
compute/lib/bershadsky_polyakov_bar.py:547:    kappa(BP_k) = rho * c(k) = (1/6) * c_BP(k)
compute/lib/ds_arithmetic_transformation_engine.py:179:    So kappa(BP) = (1/6) * c(BP).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "BP" compute/lib/koszul_conductor_table_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
28:  C20. K_BP = c_BP(k) + c_BP(-k-6) = 196
346:    c_BP(k) = -3*(3k+1)*(3k+7) / (k+3) = 2 - 24*(k+1)*(k+4)/(k+3)
349:      c_BP(k) = (25 + 24*k + 6*k^2) / (k+3) ... need to verify.
351:    Actually from C20: K_BP = c(k) + c(-k-6) = 196, self-dual at k=-3.
352:    We can derive: c_BP(k) via the formula that gives c(-3) = 98 (half of 196).
360:    Actually "self-dual at k=-3" means the Koszul dual of BP at k=-3 is
361:    BP at k'=-(-3)-6 = -3.  So k=-3 is a fixed point of k -> -k-6.
365:    Let me use: c_BP(k) = 2(9*k^2 + 24*k + 25) / (2*(k+3))
369:      c_BP(k) = -(6*k^2 + 32*k + 41) / (k + 3)
384:    Let me try: c_BP(k) = 2 - 24*(k+1)*(k+4)/(k+3)
394:    The real BP central charge (from Arakawa, 2005):
395:      c_BP(k) = -3(2k+3)(6k+7)/(k+3)
411:    From C20: K_BP = 196 and it is stated as c(k)+c(-k-6)=196.
413:    K_BP=196 must be specifically kappa+kappa', not c+c'.
415:    Re-reading C20: "K_BP = c(k) + c(-k-6) = 196".  But C18 defines
419:    Let me just provide the known K_kk = 196 for BP and leave the explicit
421:    without deriving it from first principles for BP.
425:    # c_BP(k) = (2/3)*(3k+1)*(3k+4)/(k+3) - 1  ... try another.
428:    # kappa.  For BP, kappa_BP(k) = ... is complicated.
431:    # c_BP(k) = 2 - 24*(k+1)^2/(k+3)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "98/3" compute/lib' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/sl3_subregular_bar.py:37:  Path 3 (complementarity): kappa(k) + kappa(-k-6) = rho * K_BP = 98/3, with K_BP = 196.
compute/lib/sl3_subregular_bar.py:193:    K_BP = 196 (constant). rho = 1/6. So the sum = 98/3.
compute/lib/sl3_subregular_bar.py:196:    Given kappa(k') = rho * c(k'), we can solve for kappa(k) = 98/3 - kappa(k').
compute/lib/sl3_subregular_bar.py:282:    The kappa sum: kappa(k) + kappa(k') = 98/3 = rho * K.
compute/lib/sl3_subregular_bar.py:299:        "kappa_sum_value": Rational(98, 3),  # AP140: corrected from 1/3; (1/6)*196=98/3
compute/lib/sl3_subregular_bar.py:680:    # AP140: corrected from 1/3 to 98/3
compute/lib/sl3_subregular_bar.py:681:    results["kappa sum = 98/3"] = simplify(dual["kappa_sum"] - Rational(98, 3)) == 0
compute/lib/theorem_w_algebra_chapter_rectification_engine.py:174:    kappa(k) + kappa(k') = 196/6 = 98/3.
compute/lib/ds_bar_commutation.py:594:    # Kappa sum = 98/3 = rho*K_BP = (1/6)*196
compute/lib/ds_bar_commutation.py:595:    results["sl_3 minimal: kappa sum = 98/3"] = (
compute/lib/ds_bar_commutation.py:641:    results["sl_3 Koszul dual: kappa sum = 98/3"] = simplify(kd_21.kappa_sum - Rational(98, 3)) == 0
compute/lib/theorem_ap49_superconformal_engine.py:10:  BP   (W(sl3,fmin)):kappa = c/6,         k -> -k-6,    comp sum = 98/3 (FKR conv)
compute/lib/theorem_ap49_superconformal_engine.py:305:    """kappa(k) + kappa(-k-6) = varrho * K = 196/6 = 98/3."""
compute/lib/theorem_ap49_superconformal_engine.py:587:    Path 3: Complementarity sum = 98/3
compute/lib/bp_koszul_conductor_engine.py:23:    kappa_BP(k) + kappa_BP(-k-6) = varrho_BP * K_BP = 98/3
compute/lib/bp_koszul_conductor_engine.py:78:# Kappa complementarity sum: varrho * K = (1/6) * 196 = 98/3.
compute/lib/bp_koszul_conductor_engine.py:79:# VERIFIED: [DC] (1/6) * 196 = 98/3;
compute/lib/bp_koszul_conductor_engine.py:80:# [LT] chapters/examples/bershadsky_polyakov.tex, eq. `eq:bp-complementarity`, gives 98/3.
compute/lib/bp_koszul_conductor_engine.py:156:    r"""Kappa complementarity: kappa_BP(k) + kappa_BP(-k-6) = varrho * K_BP = 98/3."""
compute/lib/bp_koszul_conductor_engine.py:159:    # [CF] equals varrho_BP * K_BP = 98/3.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,120p' compute/lib/bp_koszul_conductor_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
r"""Bershadsky-Polyakov Koszul conductor and complementarity: exact Fraction arithmetic.

MATHEMATICAL CONTENT
====================

The Bershadsky-Polyakov algebra W^k(sl_3, f_{(2,1)}) is the DS reduction of
affine sl_3 at the MINIMAL nilpotent orbit.  Its central charge, Feigin-Frenkel
dual level, Koszul conductor, anomaly ratio, and modular characteristic are
computed here in exact rational arithmetic.

Formulas:

    c_BP(k) = 2 - 24(k+1)^2 / (k+3)

    k' = -k - 6     (Feigin-Frenkel dual; h^v(sl_3) = 3, Dynkin shift)

    K_BP = c_BP(k) + c_BP(-k-6) = 196   (level-independent)

    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '138,220p' compute/lib/bp_koszul_conductor_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    """
    k = Fraction(k)
    # VERIFIED: [DC] direct sum c_BP(k) + c_BP(-k-6);
    # [CF] equals the level-independent conductor K_BP = 196.
    return c_BP(k) + c_BP(dual_level(k))


def kappa_BP(k: Union[int, Fraction]) -> Fraction:
    r"""Modular characteristic kappa_BP(k) = varrho_BP * c_BP(k).

    varrho_BP = 1/6 (anomaly ratio from strong-generator data).
    """
    # VERIFIED: [DC] kappa_BP = varrho_BP * c_BP by definition;
    # [CF] varrho_BP = 1/6 matches the BP anomaly-ratio proposition.
    return VARRHO_BP * c_BP(k)


def kappa_complementarity(k: Union[int, Fraction]) -> Fraction:
    r"""Kappa complementarity: kappa_BP(k) + kappa_BP(-k-6) = varrho * K_BP = 98/3."""
    k = Fraction(k)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/true_formula_census_verifier.py | sed -n '300,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   300	        "reference": TRUE_FORMULA_CENSUS_REFERENCES[code],
   301	    }
   302	
   303	
   304	def verify_C01() -> ResultDict:
   305	    """C01. Canonical formula: kappa(Heis_k) = k.
   306	
   307	    Anti-pattern guard:
   308	      AP1: do not import the Virasoro factor 1/2 into Heisenberg.
   309	      AP126/AP141: any Heisenberg r-matrix must keep the level prefix.
   310	
   311	    Citation:
   312	      True Formula Census Wave 12-2 C1 and landscape_census.tex.
   313	    """
   314	    expected = {
   315	        "k=0": Fraction(0),
   316	        "k=1": Fraction(1),
   317	        "k=5/2": Fraction(5, 2),
   318	    }
   319	    computed = {
codex
**Coverage**

- C1 – Verified: `compute/lib/true_formula_census_verifier.py:304-324` runs `verify_C01` and compares `kappa(H_k)` against exact samples with the canonical “kappa=k” checks and AP guards.  
- C2 – Verified: `compute/lib/true_formula_census_verifier.py:327-347` computes `kappa(Vir_c)=c/2` for \(c=0,13,26\) and flags AP/ complementarity guards.  
- C3 – Verified: `compute/lib/true_formula_census_verifier.py:350-382` checks `kappa(V_k(g))=dim(g)(k+h^\vee)/(2h^\vee)` for \(\mathfrak{sl}_2,\mathfrak{sl}_3,\mathfrak{so}_5\) against Sugawara shifts.  
- C4 – Verified: `compute/lib/true_formula_census_verifier.py:385-405` evaluates `kappa(W_N)=c(H_N-1)` for \(N=3,4,5\) and forbids the \(H_{N-1}\) trap.  
- C5 – Verified: `compute/lib/true_formula_census_verifier.py:408-426` recomputes \(c_{bc}=1-3(2\lambda-1)^2\) for \(\lambda=1/2,2\).  
- C6 – Verified: `compute/lib/true_formula_census_verifier.py:429-448` recomputes \(c_{\beta\gamma}=2(6\lambda^2-6\lambda+1)\) for \(\lambda=1/2,3/2,2\).  
- C7 – Verified: `compute/lib/true_formula_census_verifier.py:452-466` recomputes the eight E₈ dimensions via Weyl/formula and validates them against the canonical tuple.  
- C8 – Verified: `compute/lib/true_formula_census_verifier.py:469-497` tests the harmonic-number formula \(H_N=\sum_{j=1}^N 1/j\) with rational arithmetic and type checks.  
- C9 – Verified: `compute/lib/true_formula_census_verifier.py:500-530` confirms family-specific complementarity sums (Heisenberg, KM, bc/βγ, Virasoro).  
- C10 – Verified: `compute/lib/true_formula_census_verifier.py:533-551` checks \(K_{BP}=196\) via \(bp\_koszul\_conductor\) evaluations at \(k=0,-3\).  
- C11 – Verified: `compute/lib/rmatrix_landscape.py:315-355` encodes \(r^{Vir}(z)=(c/2)/z^3+2T/z\) and `FamilyRMatrix.verify_ap19` (`:123-139`) plus the main report (`:816-825`) verify the pole shift in an executable loop.  
- C12 – Verified: the same `FamilyRMatrix.verify_ap19` (`compute/lib/rmatrix_landscape.py:123-139`) and `landscape_census_verification.py:1102-1129` implement the \(pole_r=pole_{OPE}-1\) check across all sample families.  
- C13 – Verified: `compute/lib/hh_heisenberg_e3_engine.py:602-611` implements `averaging_map_check`, computing \(av(k/z)=k\) and matching it to `kappa(H_k)` (C13).  
- C14 – Verified: `compute/lib/ap5_cross_volume_checker.py:162-170` includes `CanonicalFormula("ap132_bar_augmentation_present")`, enforcing `T^c(s^{-1}\bar A)` across the tree.  
- C15 – Verified: `compute/lib/theorem_vol2_swiss_cheese_rectification_engine.py:694-740`’s `verify_desuspension_convention` exhibits \( |s^{-1}J| = |J|-1\) and checks bar degrees via the Heisenberg example.  
- C16 – Verified: `compute/lib/true_formula_census_verifier.py:452-466` (same as C7) recomputes and validates the E₈ fundamental dimensions.  
- C17 – Verified: `compute/lib/wn_channel_refined.py:4-43` defines the Wₙ generator weights \(2,\dots,N\), and `verify_cross_term_vanishing` (`:182-227`) loops over `range(2,N+1)` to certify the channel structure is exactly those spins.  
- C18 – Verified: `compute/lib/koszul_conductor_table_engine.py:68-200` defines \(K_{kk}=kappa+kappa'\) for every family and `:600-678` builds the full table, exhibiting 0 (G/L/free), 13 (Virasoro), 250/3 (W₃), 196 (BP) etc.  
- C19 – Verified: `compute/lib/true_formula_census_verifier.py:469-497` checks harmonic numbers (same as C8).  
- C20 – Verified: `compute/lib/true_formula_census_verifier.py:533-551` (same as C10) ensures \(K_{BP}=196\).  
- C21 – Verified: `compute/lib/cy_second_quantization_engine.py:820-870` derives \(kappa_{BKM}=weight(\Phi_{10})/2=10/2=5\) as part of the kappa_BPS ratio checks.  
- C22 – Verified: `compute/lib/ordered_trace_invariant_engine.py:240-255` implements `eta_dedekind` and multiplies the \(q^{1/24}\) prefactor with \(\prod_{n\ge1}(1-q^n)\).  
- C23 – Verified: `compute/lib/bicoloured_partition_engine.py:1-120` derives \(1/\eta^2=q^{-1/12}\sum p_{-2}(n)q^n\) via both convolution and direct product expansion and asserts the OEIS A000712 sequence \((1,2,5,10,20,\dots)\).  
- C24 – Verified: `compute/lib/theorem_shadow_conformal_block_engine.py:706-737` numerically integrates \(S_r=(1/(2\pi i r))\oint \sqrt{Q_L(z)}/z^{r-1}dz\), explicitly using the \(1/(2\pi i)\) normalization that matches the Cauchy formula.  
- C25 – Verified: `compute/lib/theorem_shadow_tower_physics_bridge_engine.py:1128-1146`’s `mc_verification_genus1_scalar` asserts \(d^*\Theta_{g=1} + [\Theta_{g=0},\Theta_{g=1}] = 0\) (the MC equation) and records `mc_satisfied = 1`.  
- C26 – Verified: `compute/lib/depth_classification.py:1-60` spells out the G/L/C/M depth rules, the algebraic depths \(d_{alg}=0,1,2,\infty\), and the discriminant/alpha dichotomy that distinguishes them.  
- C27 – Verified: `compute/lib/chiral_hochschild_engine.py:1319-1348`’s `verify_theorem_h_complete` enforces Theorem H by computing each family’s `ChirHoch` dimensions and checking concentration in \(\{0,1,2\}\).  
- C28 – Verified: `compute/lib/kz_shadow_connection.py:196-250` defines the KZ matrices \(A_i=\frac{1}{k+h^\vee}\sum_{j\ne i}\Omega_{ij}/(z_i-z_j)\) and hence the connection \(d\Phi/A_i\) with \(\mathrm{d}z_{ij}\) terms (not \(d\log\)).  
- C29 – Verified: `compute/lib/bv_bar_coderived_engine.py:5-25` shows that at genus 1 the Arakelov form \(\omega_1\) acts as the scalar \(1/\mathrm{Im}(\tau)\), so \((\mathrm{Im}\,\Omega)^{-1}\) collapses to \(1/\mathrm{Im}(\tau)\).  
- C30 – Verified: `compute/lib/discriminant_atlas.py:1-53` defines `critical_discriminant(kappa,S4)=8*kappa*S4`, builds the shadow metric, and cites the accompanying discriminant complementarity identities.  
- C31 – Verified: `compute/lib/bp_koszul_conductor_engine.py:1-120` derives \(c_{BP}\), \(varrho_{BP}=1/6\), \(K_{BP}=196\), and `kappa_complementarity(k)=kappa(k)+kappa(-k-6)`; `verify_all` (`:138-220`) checks that this sum equals \((1/6)\cdot196=98/3\) for many \(k\) and matches the Feigin–Frenkel involution.
context compacted

thinking
**Gathering exact line numbers**

I need to finalize the answer by ensuring the file and line numbers match the actual file contents. Some candidate lines haven't been confirmed yet, so I might need to run a few more commands for accuracy. It sounds like using multi_tool_use.parallel could be helpful since multiple developer tools can run simultaneously. I'll also consider running exec commands in the commentary to gather the exact line numbers I need. Let's get started on that!
codex
I’ve isolated the main audit lanes. I’m pinning exact line numbers now so the findings only cite file contents I can defend directly.
exec
/bin/zsh -lc "nl -ba compute/lib/chiral_zeta_virasoro_engine.py | sed -n '30,45p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/true_formula_census_verifier.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/k3_cy_a2_verification_engine.py | sed -n '96,110p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_bv_brst_o3_obstruction_engine.py | sed -n '228,238p;972,982p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   228	
   229	    At genus g, the Hodge decomposition of the BV propagator is:
   230	      P(z,w) = P_bar(z,w) + P_exact(z,w) + P_harm(z,w)
   231	    where:
   232	      P_bar = d log E(z,w) / (2*pi*i)  (meromorphic, the bar propagator)
   233	      P_exact = dbar-exact              (drops in Dolbeault cohomology)
   234	      P_harm = sum_{i,j} (Im Omega)^{-1}_{ij} omega_i(z) * bar{omega_j(w)}
   235	
   236	    At genus 1 on E_tau:
   237	      P_harm = dz * d(bar w) / (2 * Im(tau))
   238	
   972	
   973	@dataclass(frozen=True)
   974	class Genus2Extension:
   975	    """O3 analysis at genus 2.
   976	
   977	    At genus 2, the harmonic propagator has dimension 2:
   978	      P_harm = sum_{i,j=1}^{2} (Im Omega)^{-1}_{ij} omega_i(z) omega_j(w)
   979	    where Omega is the 2x2 period matrix.
   980	
 succeeded in 53ms:
    96	
    97	   This is the AVERAGED r-matrix (arity-2 shadow).  The full E_1
    98	   r-matrix requires the ordered bar complex data.
    99	
   100	CONVENTIONS:
   101	  - kappa_ch always subscripted (AP113)
   102	  - r-matrix carries level prefix (AP126)
   103	  - Bar complex: B(A) = T^c(s^{-1} A-bar), augmentation ideal (AP132)
   104	  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)
   105	  - Grading: cohomological, |d| = +1
   106	
   107	SOURCES:
   108	  - Vol III cy_to_chiral.tex: Theorem CY-A_2 (thm:cy-to-chiral)
   109	  - Vol III cy_categories.tex: Example ex:hh-k3, Theorem thm:cy-d-d2
   110	  - Vol III cy_to_chiral.tex: Conjecture conj:cy-kappa-identification
 succeeded in 53ms:
     1	"""True Formula Census verification engine.
     2	
     3	Independently recomputes the canonical Wave 12-2 formulas used in the
     4	standard landscape census and cross-checks them against the census values.
     5	
     6	Checks covered:
     7	  C01. kappa(Heis_k) = k
     8	  C02. kappa(Vir_c) = c/2
     9	  C03. kappa(V_k(g)) = dim(g) * (k + h^vee) / (2 * h^vee)
    10	  C04. kappa(W_N) = c * (H_N - 1)
    11	  C05. c_bc(lambda) = 1 - 3 * (2 * lambda - 1)^2
    12	  C06. c_bg(lambda) = 2 * (6 * lambda^2 - 6 * lambda + 1)
    13	  C07. E_8 fundamental irrep dimensions
    14	  C08. H_N = sum_{j=1}^N 1/j exactly
    15	  C09. Complementarity sums by family
    16	  C10. K_BP = 196 for Bershadsky-Polyakov W_3^(2)
    17	
    18	Anti-pattern coverage:
    19	  AP1   family-specific kappa formulas
    20	  AP24  complementarity is not universal across families
 succeeded in 53ms:
    30	  5. Evaluates Z_A(s) at special integer points s = 0, 1, 2, 3, 4.
    31	
    32	Manuscript references:
    33	    Theorem D (uniform-weight): F_g = kappa * lambda_g (higher_genus_modular_koszul.tex)
    34	    modular_shadow_zeta_engine.py: canonical lambda_g^FP formula
    35	    CLAUDE.md C2: kappa(Vir_c) = c/2
    36	    CLAUDE.md C24: Cauchy integral normalization => F_1 = kappa/24
    37	
    38	CAUTION (AP1):  kappa(Vir_c) = c/2.  At c = 25: kappa = 25/2.  NOT c = 25.
    39	CAUTION (AP32): All F_g formulas here are UNIFORM-WEIGHT.
    40	CAUTION (AP119): Series is Gevrey-0 (geometric decay, NOT factorial).
    41	                 Borel summation is unnecessary; direct Pade suffices.
    42	"""
    43	
    44	from __future__ import annotations
    45	
codex
I’ve confirmed the census-verifier cutoff and the bar/desuspension issue. I’m pulling the conflicting live formulas next, since those are the highest-risk unfinished surfaces.
exec
/bin/zsh -lc "nl -ba compute/lib/collision_residue_identification.py | sed -n '128,145p;338,356p;838,846p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/shadow_zeta_engine.py | sed -n '1,130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/shadow_cohft_tautological.py | sed -n '1,35p;190,205p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_shadow_conformal_block_engine.py | sed -n '338,360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/universal_shadow_tower_engine.py | sed -n '463,486p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/quantum_group_shadow.py | sed -n '190,225p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/mc5_disk_local.py | sed -n '1,35p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   190	        poles={1: k},
   191	        max_pole=1,
   192	        dim_g=1,
   193	        parameter=k,
   194	    )
   195	
   196	
   197	def affine_sl2_r_matrix(k=None) -> ClassicalRMatrix:
   198	    r"""r-matrix for affine sl_2 at level k: r(z) = Omega/z.
   199	
   200	    Here Omega is the Casimir in sl_2 tensor sl_2.  In the basis
   201	    {e, h, f} with standard structure constants:
   202	        Omega = e tensor f + f tensor e + (1/2) h tensor h
   203	
   204	    Normalized by the level: the actual shadow coefficient is
   205	        r(z) = (1/(k + h^v)) * Omega / z
   206	
   207	    where h^v = 2 is the dual Coxeter number of sl_2.
   208	
   209	    The CYBE is satisfied by the classical r-matrix Omega/z
 succeeded in 52ms:
   128	    The leading singularity is the double pole with coefficient k * delta^{ab}.
   129	    The Casimir tensor Omega = sum_a J^a tensor J_a has trace = dim(sl_2) = 3.
   130	
   131	    For the binary collision r-matrix, the d log factor absorbs one pole:
   132	      r(z) = k * Omega / z
   133	    The scalar trace is kappa = dim(g) * (k + h^v) / (2 * h^v) = 3(k+2)/4.
   134	
   135	    The collision residue of Theta_A at arity 2 extracts the double-pole
   136	    coefficient, and the resulting r-matrix has simple pole.
   137	    """
   138	    if k + 2 == 0:
   139	        raise ValueError("Critical level k = -2: Sugawara undefined")
   140	
   141	    dim_g = Fraction(3)
   142	    h_vee = Fraction(2)
   143	
   144	    return OPEData(
   145	        name=f"sl_2(k={k})",
   338	    def scalar_trace(self) -> Fraction:
   339	        """The scalar trace of the r-matrix: sum_i r_{ii}(z)|_{coeff}.
 succeeded in 52ms:
     1	r"""Shadow zeta engine: Z_A(s) = sum_{g=1}^{infty} F_g * g^{-s}.
     2	
     3	The shadow zeta function encodes the genus tower of a chiral algebra A
     4	into a single Dirichlet-type series.  At uniform weight with parameter
     5	kappa = kappa(A), the genus-g free energy is
     6	
     7	    F_g(kappa) = kappa^g * b_g
     8	
     9	where b_g are universal rational coefficients determined by the formula
    10	
    11	    b_g = (2^{2g-1} - 1) * |B_{2g}| / (2^{2g-1} * (2g)!)
    12	
    13	with B_{2g} the Bernoulli numbers.  Equivalently,
    14	
    15	    b_g = (1 - 2^{1-2g}) * |B_{2g}| / (2g)!
    16	
    17	SANITY CHECKS:
    18	  b_1 = 1/24         =>  F_1 = kappa/24
    19	  b_2 = 7/5760       =>  F_2 = 7*kappa^2/5760
    20	  # VERIFIED [DC] direct computation from Bernoulli  [LT] Faber-Pandharipande (1999)
 succeeded in 52ms:
     1	r"""Shadow CohFT tautological class engine.
     2	
     3	Extracts tautological classes on M-bar_{g,n} from shadow obstruction tower data.
     4	This module bridges shadow obstruction tower computations (algebra) with intersection
     5	theory on moduli spaces of curves (geometry).
     6	
     7	The shadow CohFT maps:
     8	    shadow obstruction tower data --> tautological classes on M-bar_{g,n}
     9	
    10	KEY OBJECTS:
    11	
    12	1. Tautological classes:
    13	   - lambda_i = c_i(E) where E is the Hodge bundle (rank g)
    14	   - psi_j = c_1(L_j) where L_j is the cotangent line at marking j
    15	   - kappa_a = pi_*(psi_{n+1}^{a+1}) Mumford-Morita-Miller classes
    16	
    17	   Known intersection numbers:
    18	     int_{M-bar_{1,1}} psi_1 = 1/24
    19	     int_{M-bar_{2,0}} lambda_2 = 1/240  (Faber)
    20	     int_{M-bar_{g,0}} lambda_g lambda_{g-1} = |B_{2g}|/(2g) * |B_{2g-2}|/(2g-2) * 1/(2g-2)!
 succeeded in 52ms:
   463	def compute_free_energies(kappa: Fraction, max_genus: int = 5) -> Dict[int, Fraction]:
   464	    """Compute free energies F_1..F_{max_genus} (UNIFORM-WEIGHT).
   465	
   466	    F_g = kappa * lambda_g^FP.
   467	
   468	    VERIFIED: [DC] F_1 = kappa/24; F_2 = 7*kappa^2/5760;
   469	    [LT] thm:theorem-d (higher_genus_modular_koszul.tex).
   470	
   471	    NOTE (AP32): These are UNIFORM-WEIGHT formulas.  For multi-weight
   472	    algebras at g >= 2, add delta_F_g^cross correction.
   473	    """
   474	    # F_g = kappa * lambda_g^FP (linear in kappa).
   475	    # Convention follows genus2_multichannel.py:
   476	    #   F2_scalar = kappa_total * lambda_fp(2) = kappa * 7/5760.
   477	    # F_1 = kappa/24, F_2 = 7*kappa/5760.
   478	
   479	    result: Dict[int, Fraction] = {}
   480	    for g in range(1, max_genus + 1):
   481	        result[g] = kappa * lambda_fp(g)
   482	    return result
 succeeded in 52ms:
   338	
   339	# ============================================================================
   340	# 3. Cauchy contour integral representation (exact via residue)
   341	# ============================================================================
   342	
   343	def shadow_via_cauchy_integral(r, c_val=None):
   344	    """S_r via the Cauchy integral formula:
   345	
   346	        S_r = (1/(2*pi*i*r)) * oint sqrt(Q_L(z)) / z^{r-1} dz
   347	            = a_{r-2} / r
   348	
   349	    This is the RESIDUE at z=0 of sqrt(Q_L(z)) / z^{r-1}, divided by r.
   350	
   351	    Computation: expand sqrt(Q_L(z)) as a Taylor series in z around 0,
   352	    then the residue picks out the coefficient of z^{r-2}.
   353	
   354	    Parameters:
   355	        r: arity (>= 2)
   356	        c_val: central charge (default: symbolic c)
   357	    """
 succeeded in 51ms:
     1	"""MC5 disk-local packet: BV-BRST = bar at the chain level on C₂ and C₃.
     2	
     3	This module verifies conj:disk-local-perturbative-fm — the identification
     4	of local perturbative BRST brackets with bar residue operations on FM
     5	compactification strata.
     6	
     7	The key identity (genus 0, disk-local):
     8	  Q_{BRST}(a ⊗ b) = d_bar(a ⊗ b)
     9	
    10	where:
    11	  - Q_{BRST} is the BV-BRST differential from Vol II (3d HT theory)
    12	  - d_bar is the bar differential from Vol I (configuration space residues)
    13	  - Both act on B²(A) = s⁻¹A ⊗ s⁻¹A (bar degree 2)
    14	
    15	ON C₂ STRATA:
    16	  d_bar(a ⊗ b) = Res_{z₁→z₂} η₁₂ · a(z₁)b(z₂)
    17	               = Σ_n a_{(n)}b  (n-th products from OPE)
    18	  Q_{BRST}(a ⊗ b) = {S, a ⊗ b}  (BV antibracket with action)
    19	               = Σ_n a_{(n)}b  (perturbative Feynman rules)
    20	
codex
I’ve got the live contradictions. I’m anchoring them against the census lines now so the mismatch is explicit rather than implied.
exec
/bin/zsh -lc "nl -ba CLAUDE.md | sed -n '221,281p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   221	**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
   222	
   223	**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
   224	
   225	**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).
   226	
   227	**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.
   228	
   229	**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).
   230	
   231	**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).
   232	
   233	**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
   234	
   235	**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).
   236	
   237	**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
   238	
   239	**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
   240	
exec
/bin/zsh -lc "nl -ba compute/lib/landscape_census_verification.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "1/Im(tau)" compute/lib/theorem_bv_brst_o3_obstruction_engine.py compute/lib/bv_bar_class_c_engine.py compute/lib/theorem_mc5_analytic_rectification_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     1	r"""Full landscape census verification engine.
     2	
     3	Independently recomputes EVERY numerical entry in the landscape census
     4	(chapters/examples/landscape_census.tex) and flags any discrepancy.
     5	
     6	Tables verified:
     7	  1. tab:master-invariants — c, c+c', kappa for all families
     8	  2. tab:shadow-tower-census — archetype class, r_max
     9	  3. tab:free-energy-landscape — F_1, F_2, kappa at specific k/c
    10	  4. tab:shadow-invariants-landscape — S_3, S_4, Delta, rho, kappa+kappa'
    11	  5. tab:rmatrix-census — r-matrix pole structure
    12	
    13	Anti-pattern coverage:
    14	  AP1  — kappa formulas recomputed from first principles per family
    15	  AP5  — cross-family consistency checks
    16	  AP9  — explicit qualifiers for every kappa
    17	  AP10 — cross-check tests, not single-family hardcodes
    18	  AP24 — complementarity sum NOT assumed zero
    19	  AP39 — S_2 vs kappa explicitly distinguished
    20	  AP48 — kappa != c/2 for general VOAs
 succeeded in 53ms:
compute/lib/bv_bar_class_c_engine.py:1160:      F_1 = kappa * sum_n P_n = kappa * [sum_{n>=1} n*q^n/(1-q^n) + 1/Im(tau)]
compute/lib/bv_bar_class_c_engine.py:1161:          = kappa * [E_2(tau)/24 - 1/24 + 1/Im(tau)]
compute/lib/bv_bar_class_c_engine.py:1166:    The harmonic contribution 1/Im(tau) is part of the Eisenstein
compute/lib/bv_bar_class_c_engine.py:1220:        'P_harm_zero_mode_value': '1/Im(tau)',
compute/lib/bv_bar_class_c_engine.py:1258:      delta_4^harm(Vir) proportional to Q^contact * kappa * (1/Im(tau))
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:597:      This is proportional to 1/Im(tau), which is non-holomorphic.
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:687:        # This is proportional to 1/Im(tau), which is:
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:833:      P_harm(0) = 1/Im(tau)
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:838:    This gives a NONZERO discrepancy proportional to 1/Im(tau).
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:841:    no zero-mode contribution from 1/Im(tau)).
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:854:            'The zero-mode contribution is Q^contact * 1/Im(tau).'
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:861:            'P_harm contributes at n=0 with weight 1/Im(tau). '
exec
/bin/zsh -lc 'rg -n -F "(Im Omega)''^{-1}" compute/lib/theorem_bv_brst_o3_obstruction_engine.py compute/lib/bv_bar_class_c_engine.py compute/lib/theorem_mc5_analytic_rectification_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
compute/lib/bv_bar_class_c_engine.py:281:      P_harm = sum_{i,j=1}^{g} (Im Omega)^{-1}_{ij} omega_i(z) omega_j(w)
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:234:      P_harm = sum_{i,j} (Im Omega)^{-1}_{ij} omega_i(z) * bar{omega_j(w)}
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:978:      P_harm = sum_{i,j=1}^{2} (Im Omega)^{-1}_{ij} omega_i(z) omega_j(w)
compute/lib/theorem_bv_brst_o3_obstruction_engine.py:1045:                'proportional to (Im Omega)^{-1}_{ij}. '


thinking
**Considering findings and weaknesses**

I think I need to cover only the missing engine findings, but the user wants me to address every weakness. Including wrong formulas could be beneficial, and while I can't cover all 31 individually, I can state that I've checked them all and found N. I should support N with reliable data without false positives. Mapping which formulas are covered versus missing could be useful, along with a summary of findings. It’s essential to audit each formula and possibly create a matrix for thoroughness. I'll reason through each formula based on my searches.
thinking
**Evaluating formula coverage**

I’ve found that the kappa formulas C1-C4 are covered by the true_formula_census_verifier and kappa_cross_verification, which is great. For C5-C7, the central charges and complementarity are also well covered by both the true_formula_census_verifier and extended_ferm_ghost. However, C8, related to Vir's self-duality, might be handled by kappa_cross_verification or landscape_census_verification, but I’m not entirely sure. C9's affine KM r-matrix coverage is inconsistent, while C10’s Heis r-matrix has coverage in collision_residue_identification and possibly quantum_group_shadow. Lastly, C11’s Vir r-matrix shows coverage in both quantum_group_shadow and collision_residue_identification, which seems acceptable.
codex
I’ve got enough for the hard failures. I’m doing one last sweep for the “missing engine” claims so I don’t overstate an absence that the repo actually already covers.
exec
/bin/zsh -lc 'rg -n -F "d + sum r_{ij} dz_{ij}" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "d log(z_i - z_j)" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "T''^c(s''^{-1} A-bar)" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "|s''^{-1} v| = |v| - 1" compute/lib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "1/(2*pi*i)" compute/lib' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 53ms:
compute/lib/k3_cy_a2_verification_engine.py:104:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)
compute/lib/ordered_chirhoch_sl3_elliptic_engine.py:85:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)
compute/lib/ordered_chirhoch_yangian_engine.py:61:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22).
compute/lib/ordered_chirhoch_arity4_derham_engine.py:66:  - Desuspension: |s^{-1} v| = |v| - 1 (AP22)
 succeeded in 53ms:
compute/lib/modular_forms_shadow_engine.py:493:    The Serre derivative is theta = q d/dq = (1/(2*pi*i)) d/dtau.
compute/lib/modular_forms_shadow_engine.py:516:    where D = (1/(2*pi*i)) d/dtau = q d/dq is the normalized derivative.
compute/lib/bc_isomonodromic_shadow_engine.py:27:   The RH factorization index kappa_RH = (1/(2*pi*i)) * oint d log det Y
compute/lib/bc_isomonodromic_shadow_engine.py:462:    kappa_RH = (1/(2*pi*i)) * oint d log det Y
compute/lib/resurgence_arithmetic_frontier_engine.py:882:        S_r^{(1)} = (1/(2*pi*i)) * oint sqrt(Q_L(t)) / t^{r+1} dt
compute/lib/resurgence_trans_series_engine.py:946:    # F_g ~ S_1/(2*pi*i) * A_1^{-2g} * (2g-1)! at leading order in hbar-plane.
compute/lib/shadow_mzv_engine.py:1227:      Order 1: coefficient involves 1/(2*pi*i) -- the linking number
compute/lib/bc_shadow_zeta_zeros_engine.py:549:        (1/(2*pi*i)) * oint (zeta'/zeta)(s) ds = N - P
compute/lib/bc_shadow_zeta_zeros_engine.py:570:        """Compute (1/(2*pi*i)) * integral of zeta'/zeta along segment."""
compute/lib/resurgence_deep_engine.py:753:    S_r ~ S_1/(2*pi*i) * omega_1^{-r} * Gamma(r - 1/2) / Gamma(r+1) * ...
compute/lib/shadow_singularity_map.py:979:    # G(t) = (1/(2*pi*i)) * integral disc(G)/(t'-t) dt'
compute/lib/shadow_singularity_map.py:980:    #       = (1/(2*pi*i)) * (-2*pi*i) * integral dt'/(t'-t)
compute/lib/frontier_defect_explicit_engine.py:1161:    On a punctured region, [Omega] = (1/(2*pi*i)) * int_gamma Omega.
compute/lib/frontier_defect_explicit_engine.py:1183:    Res_{s_0}(Omega) = (1/(2*pi*i)) * int_{|s-s_0|=r} Omega(s) ds
compute/lib/resurgence_shadow_complete.py:626:        F_g ~ S_1/(2*pi*i) * A^{-2g} * Gamma(2g) * (1 + c_1/(2g) + ...)
compute/lib/resurgence_shadow_complete.py:658:    #   F_g ~ S_1/(2*pi*i) * A^{-g} * Gamma(g) * (1 + corrections)
compute/lib/resurgence_shadow_complete.py:893:        F_g ~ S_1/(2*pi*i) * A_1^{-g} * Gamma(g)
compute/lib/elliptic_genus_shadow_engine.py:479:    where prime is the heat operator D = (1/(2*pi*i)) d/dtau - (1/(4*pi*i)^2) d^2/dz^2
compute/lib/bc_residue_atlas_engine.py:305:        # (1/(2*pi*i)) * (real + i*imag) = (imag + i*(-real)) / (2*pi)
compute/lib/bc_residue_atlas_engine.py:307:        # Wait: 1/(2*pi*i) = -i/(2*pi), so:
 succeeded in 53ms:
compute/lib/celestial_arithmetic_engine.py:74:AP19 WARNING: The bar construction extracts residues along d log(z_i - z_j),
compute/lib/theorem_gz_frontier_engine.py:395:        #   w = sum_{i<j} gamma_{ij} d log(z_i - z_j)
compute/lib/theorem_gz_frontier_engine.py:401:        # Then w = -2h/(n-2) * sum_{i<j} d log(z_i - z_j)
compute/lib/bv_bar_class_m_engine.py:516:    where eta_{ij} = d log(z_i - z_j).
compute/lib/mzv_bar_complex.py:38:AP19 WARNING: The bar complex extracts RESIDUES along d log(z_i - z_j).
compute/lib/mzv_bar_complex.py:443:    The bar amplitude extracts the propagator form d log(z_i - z_j),
compute/lib/mzv_bar_complex.py:447:    The bar propagator is d log(z_i - z_j) = dz/(z_i - z_j).
compute/lib/mzv_bar_complex.py:550:    The bar propagator d log(z_i - z_j) extracts the residue, absorbing one
compute/lib/shadow_mzv_engine.py:923:    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
compute/lib/virasoro_bar_zhu.py:1110:    # - The differential D uses d log(z_i - z_j) forms, which are
compute/lib/theorem_dk0_evaluation_bridge_engine.py:138:    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
compute/lib/exceptional_yangian_engine.py:788:    extracts residues along d log(z_i - z_j), which absorbs one power.
compute/lib/heisenberg_bar_explicit_engine.py:14:The bar differential uses the d log kernel eta_{ij} = d log(z_i - z_j).
compute/lib/heisenberg_bar_explicit_engine.py:32:    OPE data. The d log form eta_{ij} = d log(z_i - z_j) provides the
compute/lib/theorem_open_closed_rectification_engine.py:984:    The bar construction extracts residues along d log(z_i - z_j).
compute/lib/celestial_koszul_ope.py:79:CAUTION (AP19): The bar construction extracts residues along d log(z_i - z_j),
compute/lib/primitive_kernel_full.py:874:        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
compute/lib/etale_descent_engine.py:13:      eta^(0) = d log(z_i - z_j) is universal and omega_X^reg depends on
compute/lib/kz_shadow_connection.py:328:    where eta_{ij} = d log(z_i - z_j).
compute/lib/dmod_purity_char_variety_engine.py:37:the bar differential extracts residues via d log(z_i - z_j) = dz/(z-w).
 succeeded in 53ms:
compute/lib/k3_cy_a2_verification_engine.py:103:  - Bar complex: B(A) = T^c(s^{-1} A-bar), augmentation ideal (AP132)
compute/lib/ordered_chirhoch_sl3_elliptic_engine.py:84:  - B^{ord}(A) = T^c(s^{-1} A-bar) with augmentation ideal (AP132)
compute/lib/w_infinity_chiral_qg_engine.py:79:  - Bar: B(A) = T^c(s^{-1} A-bar), deconcatenation coproduct (AP132, AP22).
compute/lib/ordered_chirhoch_arity4_derham_engine.py:65:  - B^{ord}(A) = T^c(s^{-1} A-bar) with AUGMENTATION IDEAL (AP132)
codex
A subtler failure surfaced: multiple compute modules still write KZ with `d log(z_i-z_j)` rather than `dz_{ij}`. I’m opening representative sites to confirm the exact live statement before I include it.
exec
/bin/zsh -lc "nl -ba compute/lib/theorem_dk0_evaluation_bridge_engine.py | sed -n '132,145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/theorem_three_way_r_matrix_engine.py | sed -n '388,398p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/shadow_mzv_engine.py | sed -n '918,928p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/primitive_kernel_full.py | sed -n '868,878p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   918	
   919	    # The KZ parameter is kappa_KZ = kappa(A) for the shadow connection
   920	    # The associator involves 1/kappa_KZ as the coupling.
   921	    # Shadow curvature kappa = S_2 determines the genus-0 binary amplitude:
   922	    #   r(z) = kappa * Omega / z  (the r-matrix is kappa-proportional)
   923	    # The KZ equation: dPhi = (1/kappa) * sum Omega_{ij} d log(z_i - z_j) * Phi
   924	    # So the associator expansion parameter is 1/kappa.
   925	
   926	    shadow_mzv = {}
   927	
   928	    # Weight 2: kappa determines the scale
 succeeded in 53ms:
   388	        In tensor notation: r^{cl}(z) = (sum_a t^a tensor t^a) * k / ((k + h^v) z)
   389	        Wait -- the KZ normalization involves the denominator (k + h^v).
   390	
   391	        Actually, the r-matrix from the PVA is r^{cl}(z) = Omega * 1/z,
   392	        where Omega = sum_a t^a tensor t^a is the Casimir tensor.
   393	        The normalization 1/(k + h^v) comes from the KZ equation, which
   394	        is nabla = d - (1/(k+h^v)) sum_{j != i} Omega_{ij} d log(z_i - z_j).
   395	
   396	        The collision residue of Theta_A extracts the NORMALIZED r-matrix,
   397	        which includes the 1/(k + h^v) factor from the bar normalization.
   398	
 succeeded in 53ms:
   132	# =========================================================================
   133	
   134	@dataclass
   135	class KZData:
   136	    """Data for the KZ connection associated to V_k(g).
   137	
   138	    nabla_KZ = d - (1/(k+h^v)) * sum_{i<j} Omega_{ij} d log(z_i - z_j)
   139	
   140	    For two-point (z = z_1 - z_2):
   141	        dPsi/dz = [Omega / ((k+h^v) * z)] * Psi
   142	    """
   143	    lie_type: str = "sl2"
   144	    level: float = 1.0
   145	
 succeeded in 53ms:
   868	
   869	def kz_connection_data(N: int, k: Fraction, n_points: int = 2
   870	                       ) -> Dict[str, Any]:
   871	    """KZ connection data for affine sl_N at level k.
   872	
   873	    The KZ connection at genus 0 with n marked points is:
   874	        nabla_KZ = d - (1/kappa) * sum_{i<j} Omega_{ij} * d log(z_i - z_j)
   875	
   876	    where:
   877	        kappa_KZ = k + h^v  (the shifted level for KZ)
   878	        Omega_{ij} = sum_a t^a_i t^a_j  (Casimir insertion at points i, j)






thinking
**Evaluating formula issues**

This is a significant discovery. It seems C28 not only lacks an engine, but also has active false formulas in many compute files. The task involves auditing each formula in the census and addressing any wrong or unfinished formulas. The user wants precise fixes listed across several representative files. While I might not cover every occurrence, I will focus on providing comprehensive findings and possibly highlight the most critical errors in the audit. It's important to represent the audit surface thoroughly.
thinking
**Exploring grep hits for dlog KZ**

I'm considering whether we can exhaust all grep hits for dlog KZ. The rg results show numerous files, which feels overwhelming. The user wants every finding, but I need to keep the final answer within 50-70 lines. It's tough to balance being exhaustive with being concise. Maybe I can report a cluster of findings from multiple files as one, although the format asks for one file:line per finding. I could focus on a few high-severity cases while still ensuring distinct issues are addressed.
thinking
**Addressing dlog KZ implications for C28**

Not every occurrence of dlog KZ is necessary to discuss, but the issue does directly affect C28 since it's a census formula. I think one finding per impacted formula should be sufficient. I might want to use a clear format like `[CRITICAL] compute/lib/theorem_dk0_evaluation_bridge_engine.py:138 — PROBLEM: The file states KZ as ... dlog ... directly contradicting C28.` This pattern seems to repeat in other files, such as primitive_kernel_full.py:874, theorem_three_way_r_matrix_engine.py:394, and shadow_mzv_engine.py:923.
thinking
**Structuring findings clearly**

I think it might be better to organize my findings using missing formula numbers instead of files. Each finding should mention the specific census items affected. 

The potential findings include issues like:  
1. The broken linear genus tower affecting sanity.  
2. An inconsistent affine KM r-matrix normalization.  
3. Missing Sugawara shift verification.  
4. The full census engine issue beyond C10.  
5. Lack of executable verifiers for certain items.  

There are about 10 findings in total that seem important to address!
thinking
**Verifying missing surfaces**

I'm thinking we might need to search for formulas like C17 and C21 to ensure we’re not missing any surfaces. We've previously summarized findings from the explorer and other searches. However, I'd still like to double-check that C17 is fully covered. It’s always better to verify and make sure everything is accounted for, even if it feels repetitive! Let's keep our bases covered.
thinking
**Checking for missing surfaces**

I think it would be wise to ensure that there aren’t any additional missing surfaces. I could use the “rg” tool for key unique strings, perhaps? So, it seems like I should conduct a quick parallel process for C17, C21, C25, C26, C27, C30, and C31 to check everything properly. It’s important to cover all bases here!
codex
The remaining risk is omission. I’m doing a short confirmatory sweep on the census items I was inclined to mark “covered” so the final list doesn’t miss another missing engine.
exec
/bin/zsh -lc 'rg -n -F "Delta = 8*kappa*S_4" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Phi_10" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "{2, 3, ..., N}" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "varrho_BP = 1/6" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "G (r=2, Heis), L (r=3, aff KM), C (r=4, betagamma), M (r=inf, Vir/W_N)" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "ChirHoch''^*(Vir_c)" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "d*Theta + (1/2)[Theta,Theta] = 0" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/celestial_arithmetic_engine.py:1373:    Path 4 (discriminant): Delta = 8*kappa*S_4 = 40/(5c+22).
compute/lib/theorem_holographic_c13_entanglement_engine.py:32:   Delta = 8*kappa*S_4 = 40/87.
compute/lib/theorem_holographic_c13_entanglement_engine.py:368:    Delta = 8*kappa*S_4 = 8*(13/2)*(10/1131) = 40/87.
compute/lib/k3_relative_chiral.py:514:    # Critical discriminant: Delta = 8*kappa*S_4
compute/lib/theorem_class_l_generating_function_engine.py:995:    For class L: S_4 = 0, so Delta = 8*kappa*S_4 = 0.
compute/lib/theorem_class_l_generating_function_engine.py:1007:    r"""Critical discriminant for class L: Delta = 8*kappa*S_4 = 0.
compute/lib/cy_grand_atlas_k3e_engine.py:549:    Delta = 8*kappa*S_4 (critical discriminant).
compute/lib/cy_grand_atlas_k3e_engine.py:586:      (b) The critical discriminant Delta = 8*kappa*S_4 != 0
compute/lib/theorem_niemeier_shadow_discrimination_engine.py:344:    """Delta = 8*kappa*S_4 = 0 for all Niemeier lattice VOAs."""
compute/lib/nonsimplylaced_bar.py:526:    discriminant = 0  # Delta = 8*kappa*S_4 = 0
compute/lib/bar_gf_universality_engine.py:981:    """Shadow discriminant Delta = 8*kappa*S_4 for all standard families.
compute/lib/bc_arakelov_shadow_height_engine.py:279:    """Critical discriminant Delta = 8*kappa*S_4.
compute/lib/moonshine_shadow_depth.py:271:    """Delta = 8*kappa*S_4 = 0 for all Niemeier lattice VOAs."""
compute/lib/moonshine_shadow_tower.py:48:       This is nonzero, so Delta = 8*kappa*S_4 = 8*12*(5/1704) = 20/71 != 0.
compute/lib/ds_shadow_tower_sl2_engine.py:10:    Delta = 8*kappa*S_4 = 0.  Finite shadow tower, depth 3.
compute/lib/ds_shadow_tower_sl2_engine.py:15:    Delta = 8*kappa*S_4 = 40/(5c+22) != 0 generically.
compute/lib/cy_wallcrossing_engine.py:1220:        Delta = 8*kappa*S_4 (critical discriminant)
compute/lib/padic_shadow_iwasawa_engine.py:112:    with kappa = c/2, alpha = 2 (c-independent), S_4 = 10/(c(5c+22)), Delta = 8*kappa*S_4.
compute/lib/padic_shadow_iwasawa_engine.py:215:    Delta = 8*kappa*S_4 = 0, so the shadow metric is a perfect square.
compute/lib/ds_nonprincipal_shadows.py:549:    where Delta = 8*kappa*S_4.
 succeeded in 52ms:
compute/lib/theorem_thm_d_multiweight_frontier_engine.py:834:    which depends only on the CONFORMAL WEIGHT SPECTRUM {2, 3, ..., N},
compute/lib/rectification_delta_f2_verify_engine.py:254:    Channels are labeled by conformal weights: i, j, k in {2, 3, ..., N}.
compute/lib/dirichlet_sewing.py:187:    Weight multiset W = {2, 3, ..., N}, so
compute/lib/analytic_langlands_shadow_engine.py:615:    parts from {d_1, ..., d_{N-1}} = {2, 3, ..., N}.
compute/lib/euler_koszul_engine.py:116:    """W_N algebra: W = {2, 3, ..., N}."""
compute/lib/complementarity_cross_verification.py:385:    For W_N: weights {2, 3, ..., N}, kappa_ghost = -sum_{h=2}^N (6h^2-6h+1).
compute/lib/complementarity_cross_verification.py:395:    """Generator conformal weights for principal W_N: {2, 3, ..., N}."""
compute/lib/penner_matrix_model_delta_f2_engine.py:15:{h_1, h_2, ..., h_{N-1}} = {2, 3, ..., N} of the W_N generators.
compute/lib/penner_matrix_model_delta_f2_engine.py:36:where the eigenvalues are FIXED at the conformal weights {2, 3, ..., N}:
compute/lib/penner_matrix_model_delta_f2_engine.py:45:supported at {2, 3, ..., N}. This suggests that delta_F_2 is the
compute/lib/penner_matrix_model_delta_f2_engine.py:261:    For eigenvalues {2, 3, ..., N}:
compute/lib/galois_cross_channel_engine.py:884:    A triple (W_i, W_j, W_k) with i, j, k in {2, 3, ..., N} is:
compute/lib/e8_koszul_conductor_engine.py:34:For sl_N: spins = {2, 3, ..., N}, so varrho = H_N - 1 = sum_{j=2}^{N} 1/j.
compute/lib/quartic_residue_engine.py:281:    Strong generators have weights {2, 3, ..., N}.
compute/lib/quartic_residue_engine.py:794:    """Weight multiset for W_N: {2, 3, ..., N}."""
compute/lib/delta_f4_engine.py:15:  2. For each graph, summing over channel assignments {2, 3, ..., N}^{|E|}
compute/lib/delta_f4_engine.py:41:weights {2, 3, ..., N}. The power sums S_k = sum_{j=2}^{N} j^k
compute/lib/delta_f4_engine.py:459:        N: rank of W_N algebra (channels are {2, 3, ..., N})
compute/lib/a2_polynomial_combinatorics_engine.py:20:weights {2, 3, ..., N} of the W_N generators.
compute/lib/theorem_large_n_delta_f2_engine.py:489:    So the eigenvalues are {2, 3, ..., N}.
 succeeded in 52ms:
compute/lib/cy_elliptic_genus_k3e_engine.py:1323:        sum_{N>=0} p^N Z(Sym^N(K3); tau, z) = 1/Phi_10(Omega)
compute/lib/cy_elliptic_genus_k3e_engine.py:1324:    where Phi_10 is the Igusa cusp form (weight 10 Siegel modular
compute/lib/cy_elliptic_genus_k3e_engine.py:1335:        siegel_connection="DMVV formula -> 1/Phi_10 (Igusa cusp form)",
compute/lib/cy_shadow_siegel_bridge_engine.py:7:obstruction tower and the Igusa cusp form Phi_10, building on the structural
compute/lib/cy_shadow_siegel_bridge_engine.py:9:does NOT directly produce Phi_10). Here we compute the precise BRIDGE.
compute/lib/cy_shadow_siegel_bridge_engine.py:18:(b) Igusa cusp form Phi_10(Omega), a FUNCTION on H_2 (the genus-2 Siegel
compute/lib/cy_shadow_siegel_bridge_engine.py:20:    Its reciprocal 1/Phi_10 is the DVV BPS partition function.
compute/lib/cy_shadow_siegel_bridge_engine.py:61:For K3 x E: Z_2 is related to 1/Phi_10 via DVV, and F_2 is the result
compute/lib/cy_shadow_siegel_bridge_engine.py:74:1/Phi_10              | FULL genus-2 BPS partition function (DVV)
compute/lib/cy_shadow_siegel_bridge_engine.py:75:Shadow depth (class M)| Infinite product structure of Phi_10
compute/lib/cy_shadow_siegel_bridge_engine.py:82:1/Phi_10 is SECOND-QUANTIZED (DMVV symmetric product formula):
compute/lib/cy_shadow_siegel_bridge_engine.py:84:  1/Phi_10(Omega) = sum_{N>=0} p^N chi(Sym^N(K3); tau, z)
compute/lib/cy_shadow_siegel_bridge_engine.py:100:  Dijkgraaf-Verlinde-Verlinde (1997): Z_BPS = 1/Phi_10, hep-th/9608096
compute/lib/cy_shadow_siegel_bridge_engine.py:258:    """Object (b): data about Phi_10 on H_2.
compute/lib/cy_shadow_siegel_bridge_engine.py:260:    Phi_10 is the unique Siegel cusp form of weight 10 on Sp(4,Z).
compute/lib/cy_shadow_siegel_bridge_engine.py:296:      k = 10: dim = 1 (spanned by chi_{10} = Phi_10)
compute/lib/cy_shadow_siegel_bridge_engine.py:326:    r"""Phi_10 = chi_10 is the UNIQUE Siegel cusp form of weight 10.
compute/lib/cy_shadow_siegel_bridge_engine.py:328:    dim S_{10}(Sp(4,Z)) = 1, so Phi_10 is unique up to scalar.
compute/lib/cy_shadow_siegel_bridge_engine.py:359:      At genus 2: Z_2(Omega) is related to 1/Phi_10 via DVV.
compute/lib/cy_shadow_siegel_bridge_engine.py:384:            return "Z_2(Omega) related to 1/Phi_10 via DVV"
 succeeded in 51ms:

 succeeded in 51ms:
compute/lib/bp_koszul_conductor_engine.py:19:    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)
compute/lib/bp_koszul_conductor_engine.py:148:    varrho_BP = 1/6 (anomaly ratio from strong-generator data).
compute/lib/bp_koszul_conductor_engine.py:151:    # [CF] varrho_BP = 1/6 matches the BP anomaly-ratio proposition.
compute/lib/universal_shadow_tower_engine.py:236:    """kappa_BP(k) = varrho_BP * c_BP(k) where varrho_BP = 1/6.
compute/lib/universal_shadow_tower_engine.py:238:    The anomaly ratio varrho_BP = 1/6 is computed from strong generators:
 succeeded in 51ms:
compute/lib/chiral_hochschild_engine.py:571:    NOTE: Per Theorem H (AP94/AP95), ChirHoch^*(Vir_c) is
compute/lib/chiral_hochschild_engine.py:575:    (ChirHoch^*(Vir_c) = C[Theta] with |Theta|=2, unbounded)
compute/lib/theorem_thm_h_e3_rectification_engine.py:305:    ChirHoch^*(Vir_c) is CONCENTRATED in degrees {0, 1, 2}
compute/lib/chriss_ginzburg_universal.py:630:            # model (ChirHoch^*(Vir_c) = C[Theta], unbounded) is
 succeeded in 52ms:




thinking
**Analyzing code findings**

I didn't find results for exact strings like MC and GLCM due to formatting issues. I'm starting to wonder if there’s a missing engine for C25 or C26. Although there's no exact match, the Delta search yielded some results. A new insight suggests that KZ may be miswritten in several files, indicating a stronger issue with C28 than a missing engine. We have specific lines from multiple files and could propose a grep-driven fix based on the user's request for an exact solution.
thinking
**Summarizing findings for clarity**

I could state that there are conflicts with `CLAUDE.md:267-277` for C24/C29, which isn't an issue. It would be smart to include [HIGH] findings from `compute/lib/true_formula_census_verifier.py:6` and highlight that `compute/lib/landscape_census_verification.py:3` deals only with numerical data, supporting the missing formula engines claim. Another critical finding is that many compute files miswrite KZ with dlog as a connection, which should be marked as CRITICAL. I'll plan around nine findings and consider incorporating line numbers for additional clarity.
thinking
**Clarifying formula engine status**

I think I should clarify that not every formula is missing an engine; it's only specific ones. It's important to be precise about which formulas are affected so that the user understands the context without any confusion. I want to make sure I highlight the exact formulas that have issues while avoiding any unnecessary uncertainty. This way, I can deliver a clear and concise message that assists the user effectively.
codex
I found the KZ misuse cluster. I’m doing one final spot-check on the MC/classification surfaces so I can close the audit without leaving an obvious census item unaccounted for.
exec
/bin/zsh -lc "nl -ba compute/lib/shadow_depth_cross_verification.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/chiral_hochschild_engine.py | sed -n '568,580p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/bp_koszul_conductor_engine.py | sed -n '1,30p;140,155p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "G (Gaussian" compute/lib/shadow_cohft_tautological.py compute/lib/shadow_depth_cross_verification.py compute/lib/theorem_shadow_conformal_block_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "(1/2)[Theta,Theta]" compute/lib | head -n 20' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   568	    Derivation: c-deformation T(z) → T(z) + ε·∂_c T(z).
   569	    This is unobstructed because Vir_c exists at all c.
   570	
   571	    NOTE: Per Theorem H (AP94/AP95), ChirHoch^*(Vir_c) is
   572	    concentrated in degrees {0,1,2} with total dim <= 4,
   573	    with dim ChirHoch^0 = dim ChirHoch^1 = dim ChirHoch^2 = 1
   574	    at generic c.  The historical "polynomial-ring" model
   575	    (ChirHoch^*(Vir_c) = C[Theta] with |Theta|=2, unbounded)
   576	    is REFUTED: that is continuous Lie cohomology of the
   577	    Witt algebra (Gelfand-Fuchs), a DIFFERENT functor.
   578	    The derivation analysis below captures ChirHoch^1.
   579	
   580	    Result: dim ChirHoch^1(Vir_c) = 1 (c-deformation class).
 succeeded in 51ms:
     1	r"""Bershadsky-Polyakov Koszul conductor and complementarity: exact Fraction arithmetic.
     2	
     3	MATHEMATICAL CONTENT
     4	====================
     5	
     6	The Bershadsky-Polyakov algebra W^k(sl_3, f_{(2,1)}) is the DS reduction of
     7	affine sl_3 at the MINIMAL nilpotent orbit.  Its central charge, Feigin-Frenkel
     8	dual level, Koszul conductor, anomaly ratio, and modular characteristic are
     9	computed here in exact rational arithmetic.
    10	
    11	Formulas:
    12	
    13	    c_BP(k) = 2 - 24(k+1)^2 / (k+3)
    14	
    15	    k' = -k - 6     (Feigin-Frenkel dual; h^v(sl_3) = 3, Dynkin shift)
    16	
    17	    K_BP = c_BP(k) + c_BP(-k-6) = 196   (level-independent)
    18	
    19	    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)
    20	
 succeeded in 52ms:
     1	r"""Shadow depth cross-verification engine: 4 independent methods for G/L/C/M classification.
     2	
     3	The shadow depth classification G/L/C/M is a central structural invariant
     4	of the shadow obstruction tower (thm:shadow-archetype-classification).
     5	This module cross-verifies the classification using FOUR independent methods:
     6	
     7	    METHOD 1 — DIRECT SHADOW COMPUTATION:
     8	        Compute S_2, S_3, S_4, S_5, ... from the OPE data via the convolution
     9	        recursion.  r_max = max{r : S_r != 0} (or infinity if none vanish).
    10	
    11	    METHOD 2 — CRITICAL DISCRIMINANT:
    12	        Delta = 8*kappa*S_4.
    13	        Delta = 0 => tower terminates (G or L).
    14	        Delta != 0 => tower is infinite (M).
    15	        Class C: stratum separation (quartic contact on charged stratum).
    16	
    17	    METHOD 3 — SHADOW METRIC FACTORIZATION:
    18	        Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.
    19	        Perfect square => G or L.
    20	        Irreducible => M.
 succeeded in 51ms:
compute/lib/shadow_cohft_tautological.py:198:      G (Gaussian, r_max=2):  tau_{g,0} = kappa^g * lambda_g^{FP}
 succeeded in 52ms:
compute/lib/twisted_holography_engine.py:248:    These are the arity-2 projection of D*Theta + (1/2)[Theta,Theta] = 0.
compute/lib/twisted_holography_engine.py:941:    1. MC equation: D*Theta + (1/2)[Theta,Theta] = 0
compute/lib/twisted_holography_engine.py:1098:    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 at arity 2 gives:
compute/lib/twisted_holography_engine.py:1124:    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 projected to arity 2:
compute/lib/lattice_model_shadow_engine.py:24:   The MC equation D*Theta + (1/2)[Theta,Theta] = 0, projected to the
compute/lib/bcov_mc_complete_proof_engine.py:293:    The MC equation D(Theta) + (1/2)[Theta,Theta] = 0 at (g,0):
compute/lib/resurgence_arithmetic_frontier_engine.py:793:    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 constrains
compute/lib/cy_grand_atlas_k3e_engine.py:1090:            "mc_equation": "D*Theta + (1/2)[Theta,Theta] = 0",
compute/lib/grand_synthesis_engine.py:973:            'this IS our MC equation D*Theta + (1/2)[Theta,Theta] = 0.'
compute/lib/eulerian_weight_mc_engine.py:553:    r"""Analyze whether the MC equation DTheta + (1/2)[Theta,Theta] = 0
compute/lib/string_field_theory_bar_engine.py:36:   Bar: D*Theta + (1/2)[Theta,Theta] = 0
compute/lib/large_n_twisted_holography.py:168:    Flatness: (nabla)^2 = 0 follows from MC equation D*Theta + (1/2)[Theta,Theta] = 0
compute/lib/large_n_twisted_holography.py:850:    from the single MC equation D*Theta + (1/2)[Theta,Theta] = 0.
compute/lib/costello_2loop_qcd_engine.py:555:    The MC equation D*Theta + (1/2)[Theta,Theta] = 0 at (g=2, n=0)
compute/lib/analytic_langlands_shadow_engine.py:1127:    The Ecalle bridge equation: the MC equation D*Theta + (1/2)[Theta,Theta] = 0
compute/lib/analytic_langlands_shadow_engine.py:1161:        'mc_constraint': 'D*Theta + (1/2)[Theta,Theta] = 0',
compute/lib/csft_from_bar.py:854:        "CSFT_master_equation": "MC equation: D Theta + (1/2)[Theta,Theta] = 0",
compute/lib/theorem_pixton_ideal_mc_engine.py:297:    # CORRECTED: The MC equation D*Theta + (1/2)[Theta,Theta] = 0 at (g,n)
compute/lib/csft_vertex_engine.py:1353:    Path 1: MC equation D Theta + (1/2)[Theta,Theta] = 0
compute/lib/csft_vertex_engine.py:1364:            "equation": "D Theta + (1/2)[Theta,Theta] = 0",

thinking
**Analyzing coefficient extraction**

I’m considering mentioning that I found no compute/lib file that explicitly implements the C24 coefficient-extraction identity. This seems acceptable since we actually ran a command and checked for the specific phrase and saw no dedicated file by that name. It feels like a valid inference, but I still want to acknowledge that it’s based on our search findings. The user has allowed us to access file contents for reading, which gives some ground for this claim.
codex
- [CRITICAL] `compute/lib/shadow_zeta_engine.py:7` — PROBLEM: The executable genus formula is wrong on the live surface: line 7 states `F_g(kappa) = kappa^g * b_g`, lines 18-22 specialize this to `F_2 = 7*kappa^2/5760`, and line 110 returns `kappa ** g * shadow_b_g(g)`. That is incompatible with the repo’s linear genus convention already used in `compute/lib/universal_shadow_tower_engine.py:466-481`. FIX: change the definition to `F_g(kappa) = kappa * b_g`, update lines 18-22 and 85-109 to `F_2 = 7*kappa/5760`, change line 110 to `return kappa * shadow_b_g(g)`, and rewrite the convergence paragraph so `kappa` is a global linear prefactor rather than a genus-dependent power.

- [CRITICAL] `compute/lib/quantum_group_shadow.py:197` — PROBLEM: The affine `sl_2` r-matrix surface is internally inconsistent. The docstring says “actual shadow coefficient” is `Omega/((k+h^v) z)` at line 205, but the function returns `poles={1: 1}` at line 220, i.e. bare `Omega/z`. That also conflicts with `compute/lib/collision_residue_identification.py:132-133`, which uses the trace-form convention `k*Omega/z`. FIX: add an explicit `convention` parameter with only `trace_form` and `kz`; return `k` in the trace-form branch and `1/(k+h^v)` in the KZ branch; add tests for `k=0` and `k=-h^v`; and implement the bridge identity in code instead of leaving both normalizations to drift in prose.

- [CRITICAL] `compute/lib/theorem_dk0_evaluation_bridge_engine.py:138` — PROBLEM: This file writes the KZ connection as `... Omega_{ij} d log(z_i - z_j)`. The same KZ-with-`d log` misuse also appears in `compute/lib/primitive_kernel_full.py:874`, `compute/lib/theorem_three_way_r_matrix_engine.py:394`, and `compute/lib/shadow_mzv_engine.py:923`. That directly violates census item C28, which separates the Arnold `d log` form from the KZ connection form. FIX: replace every KZ formula with `nabla_KZ = d + sum r_{ij} dz_{ij}` or, expanded, `d - (1/(k+h^v)) sum Omega_{ij} dz_{ij}/(z_i-z_j)`; reserve `d log(z_i-z_j)` for bar/Arnold code paths only; and add a grep-backed regression test that fails on `KZ` combined with `d log`.

- [HIGH] `compute/lib/collision_residue_identification.py:338` — PROBLEM: The affine `sl_2` verification never computes the C13 Sugawara split. The file advertises `kappa = 3(k+2)/4` at lines 132-133 and 842, but `scalar_trace()` at lines 345-347 only records `tr(r)=3k`. The shift from `av(r)` to full `kappa` is left implicit instead of being verified. FIX: add explicit functions for `kappa_dp = av(r) = k*dim(g)/(2h^v)` and `kappa_full = kappa_dp + dim(g)/2`, then assert `kappa_full == 3*(k+2)/4` on sample levels.

- [HIGH] `compute/lib/true_formula_census_verifier.py:6` — PROBLEM: The dedicated census verifier explicitly stops at `C10`. `compute/lib/landscape_census_verification.py:3-11` only promises numerical table entries, so it does not close the gap for structural items like C14, C15, C24, C28, and C29. FIX: extend `true_formula_census_verifier.py` through `C31`, or add a new `compute/lib/true_formula_census_verifier_v2.py` that imports per-formula checks and emits one canonical pass/fail report for all 31 census items.

- [HIGH] `compute/lib/k3_cy_a2_verification_engine.py:103` — PROBLEM: In the files I read, the exact C14/C15 formulas appear only as convention docstrings like this one: `B(A) = T^c(s^{-1} A-bar)` and `|s^{-1}v| = |v|-1`. The same pattern repeats in `ordered_chirhoch_sl3_elliptic_engine.py:84-85` and related files, but I did not find an executable verifier for the augmentation ideal or desuspension sign. FIX: add `compute/lib/bar_complex_census_verifier.py` that builds a toy augmented algebra, forms `T^c(s^{-1}\bar A)`, checks deconcatenation, rejects `A` in place of `\bar A`, and asserts the grading shift on basis elements.

- [HIGH] `compute/lib/shadow_cohft_tautological.py:24` — PROBLEM: This module hard-codes the same wrong `kappa^g` law in two places: line 24 says `tau_{g,0}(H_k) = kappa^g * lambda_g`, and line 198 repeats `tau_{g,0} = kappa^g * lambda_g^{FP}`. That contradicts the linear genus formula already implemented in `compute/lib/universal_shadow_tower_engine.py:466-481`. FIX: change both occurrences to `kappa * lambda_g^{FP}` if this is the scalar free-energy/CohFT surface; if a pre-collapse graph weight is intended instead, rename the object and document the final collapse step explicitly so it is not advertised as the scalar theorem.

- [MEDIUM] `compute/lib/theorem_shadow_conformal_block_engine.py:343` — PROBLEM: In the files I read, C24 is not directly verified. This file implements the specialized contour formula `S_r = (1/(2*pi*i*r)) ...`, while `compute/lib/chiral_zeta_virasoro_engine.py:36` only cites C24 in a docstring. I did not find a standalone check of the canonical coefficient rule `[z^{n-1}]f(z) = (1/(2*pi*i)) ∮ f(z) dz / z^n`, nor a negative test for the forbidden `1/(2*pi)` normalization. FIX: add `compute/lib/cauchy_integral_normalization_engine.py` with exact monomial coefficient tests, a failing branch for the missing-`i` normalization, and the `F_1 = kappa/24` sanity recovery.

- [MEDIUM] `compute/lib/theorem_bv_brst_o3_obstruction_engine.py:234` — PROBLEM: The file uses the higher-genus matrix formula `(Im Omega)^{-1}_{ij}` at line 234 and again at lines 977-979, and separately writes the genus-1 scalar surface at lines 236-237. That is good notation, but I did not find a dedicated verifier for census item C29 proving the `g=1` collapse from matrix to scalar while preventing scalarization at `g>=2`. FIX: add `compute/lib/period_matrix_collapse_verifier.py` that checks `((Im Omega)^{-1})_{11} = 1/Im(tau)` in genus 1, retains full matrix dependence in genus 2, and fails if a higher-genus formula collapses to a scalar.

- [LOW] `compute/lib/universal_shadow_tower_engine.py:468` — PROBLEM: The docstring still says `F_2 = 7*kappa^2/5760` even though the code immediately below is linear in `kappa` at lines 474-481. This is local documentation drift on a load-bearing formula. FIX: change line 468 to `F_2 = 7*kappa/5760` and add a small regression test that compares the docstring examples against `compute_free_energies`.

## Summary
Checked: 31 | Findings: 10 | Verdict: FAIL
tokens used
284,874
