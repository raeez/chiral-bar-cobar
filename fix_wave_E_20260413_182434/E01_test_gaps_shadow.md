# E01_test_gaps_shadow (427s)

- `PROBLEM at` [compute/lib/genus1_arithmetic_shadow.py](/Users/raeez/chiral-bar-cobar/compute/lib/genus1_arithmetic_shadow.py:1): missing smoke-test coverage for the genus-1 arithmetic shadow engine.
  `EXACT edit applied`: created [compute/tests/test_genus1_arithmetic_shadow.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:1) with four verified smoke tests at [line 9](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:9), [line 17](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:17), [line 25](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:25), and [line 31](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:31) covering the Heisenberg Euler product, Virasoro Euler defect, divisor-sum sewing coefficients, and `Xi_H(1)` plus exact `βγ` Euler-Koszul behavior.

- `PROBLEM at` [compute/lib/modular_bootstrap_shadow.py](/Users/raeez/chiral-bar-cobar/compute/lib/modular_bootstrap_shadow.py:1): missing smoke-test coverage for the modular bootstrap shadow engine.
  `EXACT edit applied`: created [compute/tests/test_modular_bootstrap_shadow.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:1) with four verified smoke tests at [line 19](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:19), [line 27](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:27), [line 41](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:41), and [line 51](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:51) covering `lambda_g^{FP}` low-genus values, Virasoro shadow data at `c=13` and `c=24`, the Monster genus-2 planted-forest correction, and Ising modular/fusion data plus `F_1=1/96`.

- `PROBLEM at` [compute/lib/shadow_painleve.py](/Users/raeez/chiral-bar-cobar/compute/lib/shadow_painleve.py:1): missing smoke-test coverage for the shadow Painleve engine.
  `EXACT edit applied`: created [compute/tests/test_shadow_painleve.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:1) with five verified smoke tests at [line 18](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:18), [line 27](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:27), [line 34](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:34), [line 50](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:50), and [line 58](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:58) covering closed-form metric coefficients/discriminant, the origin Schwarzian potential, the `Delta=0` trivial classification, Virasoro self-dual `c=13` parameters, and a multichannel `PVI` plus tau-normalization smoke check.

`pytest compute/tests/test_genus1_arithmetic_shadow.py compute/tests/test_modular_bootstrap_shadow.py compute/tests/test_shadow_painleve.py` passed: `13 passed in 0.54s`.

Scope check: the original missing-test scan is now silent.

Out-of-scope defects observed but not edited because you restricted changes to the missing test files: [compute/lib/shadow_painleve.py:279](/Users/raeez/chiral-bar-cobar/compute/lib/shadow_painleve.py:279) and [compute/lib/shadow_painleve.py:663](/Users/raeez/chiral-bar-cobar/compute/lib/shadow_painleve.py:663).


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
session id: 019d87a8-b753-7192-a328-4949637fc201
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


Find and create missing test files for shadow tower engines.
ls compute/lib/*shadow*.py | while read f; do test=compute/tests/test_$(basename $f); [ ! -f "$test" ] && echo "MISSING: $test"; done
For each missing test: create a basic test file that imports the engine and runs at least
3 smoke tests with verified expected values.
mcp startup: no servers



thinking
**Assessing coding tasks**

I need to act as a coding agent and first acknowledge the user's request about finding and creating missing test files for shadow tower engines. It seems I might be using the compute-engine-scaffold skill since the task involves adding tests and potentially independent checks. It makes sense to check the required files before proceeding to ensure I’m on the right track. I’ll need to inspect the repository and locate the missing tests to address this task effectively.
thinking
**Using tools for codebase tasks**

I think I should use an explorer sub-agent for codebase questions, as the instructions emphasize that I should always prefer explorers for those tasks. I need to spawn the explorer to find missing tests and relevant engine APIs, but I can use shell commands too. It seems building context with the codebase is essential, and using multi-tool parallel might help with reading multiple files at once. I’ll also provide frequent updates and ensure to check required files before making any substantial changes.
thinking
**Finalizing test discovery and templates**

I need to specify the exact scope before diving into reasoning. It might be a good idea to run a command for discovering missing tests, and I may want to fill in PE templates beforehand, focusing on critical areas like formulas in tests for shadow tower engines. Since the user requested verified expected values, I might need independent sources and comments noting verified values, potentially using the compute-engine-scaffold skill. It could be helpful to include comments, even if they aren’t strictly necessary.
codex
Using `compute-engine-scaffold` for the missing engine tests, with `multi-path-verify` discipline for expected values. I’m first reading the required repo constitution files and enumerating the missing `shadow` engine tests so the edits stay scoped and the test values are grounded.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/compute-engine-scaffold/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 50ms:
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
 succeeded in 52ms:
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
exec
/bin/zsh -lc 'ls compute/lib/*shadow*.py | while read f; do test=compute/tests/test_$(basename "$f"); [ ! -f "$test" ] && echo "MISSING: $test"; done' in /Users/raeez/chiral-bar-cobar exited 1 in 482ms:
MISSING: compute/tests/test_genus1_arithmetic_shadow.py
MISSING: compute/tests/test_modular_bootstrap_shadow.py
MISSING: compute/tests/test_shadow_painleve.py

thinking
**Inspecting engine files**

I need to take a look at the missing engine files and any existing similar tests. It might help to use an explorer sub-agent for this codebase issue. I think I should spawn an explorer to inspect the missing modules and recommend tests plus APIs. Additionally, I could read through relevant files and look for existing tests for similar engines. Maybe using the `rg` tool to find shadow tests could work too. I'll keep the user updated on my progress!
codex
I’ve confirmed three missing test files: `compute/tests/test_genus1_arithmetic_shadow.py`, `compute/tests/test_modular_bootstrap_shadow.py`, and `compute/tests/test_shadow_painleve.py`. Next I’m reading those engines and nearby test patterns so the new tests use the real public API and independent expected values.
collab spawn_agent(call_TOfaqCC2C8DtiBlw8dj7pwCj, prompt="Inspect the missing shadow engine tests in /Users/raeez/chiral-bar-cobar. Read only the relevant engine modules and near…")
spawn_agent(call_TOfaqCC2C8DtiBlw8dj7pwCj, prompt="Inspect the missing shadow engine tests in /Users/raeez/chiral-bar-cobar. Read only the relevant engine modules and near…") pending init:
  agent: 019d87a9-3228-7132-8c7d-2c38fdcbec09
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N3_e1_primacy.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
audit_campaign_20260413_163450

exec
/bin/zsh -lc 'ls compute/tests' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1411

__init__.py
__pycache__
conftest.py
test_a2_polynomial_combinatorics_engine.py
test_admissible_deep_bar_engine.py
test_admissible_koszul_rank2_engine.py
test_admissible_level_bar_engine.py
test_admissible_sl3_d1_poisson_engine.py
test_admissible_sl3_d1_rank_engine.py
test_adversarial_audit.py
test_adversarial_core_math.py
test_affine_km_sewing_engine.py
test_affine_sl2_shadow_tower.py
test_affine_sl3_shadow.py
test_agt_nekrasov_arithmetic_engine.py
test_agt_nekrasov_shadow_engine.py
test_agt_shadow_correspondence.py
test_agt_su3_nekrasov_engine.py
exec
/bin/zsh -lc 'ls compute/lib | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/genus1_arithmetic_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
"""
genus1_arithmetic_shadow.py — The genus-1 arithmetic shadow of Θ_A.

SYNTHESIS: Three genus-1 invariants of a chiral algebra A sit in a triangle:

                     ε^c_s(A)
                    /         \
                   /           \
    Koszul duality/             \Rankin-Selberg
                 /               \
    S_A(u) -------- sewing -------- F^conn_A(q)

Left edge: Connected Dirichlet-sewing lift (prime side)
  S_A(u) = Σ a_A(N) N^{-u} = ζ(u+1) Σ_i (ζ(u) - H_{w_i-1}(u))
  Has Euler product iff all weights = 1 (Heisenberg, βγ)

Right edge: Benjamin-Chang constrained Epstein (zero side)
  ε^c_s = Σ_{Δ∈S} (2Δ)^{-s}
  Poles at s = (1+z_n)/2 where z_n are nontrivial zeta zeros
  Functional equation from ζ(2s)/ζ(2s-1) ratio
thinking
**Searching for engine files**

I’m planning to use a multi-tool approach to read engine files and list any existing tests that might be related to shadow aspects. I need to identify the exact files involved here. So, I’ll run some commands like `rg` or `ls` to locate what I need. This step seems pretty straightforward, but I want to make sure I’m targeting the right files! Let's get started!
exec
/bin/zsh -lc 'ls compute/lib/*shadow*.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' compute/lib/genus1_arithmetic_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files compute/tests | rg 'shadow|painleve|bootstrap'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/affine_sl2_shadow_tower.py
compute/lib/affine_sl3_shadow.py
compute/lib/agt_nekrasov_shadow_engine.py
compute/lib/agt_shadow_correspondence.py
compute/lib/analytic_langlands_shadow_engine.py
compute/lib/analytic_shadow_partition_engine.py
compute/lib/arithmetic_shadow_connection.py
compute/lib/arity6_shadow.py
compute/lib/barnes_wall_48_shadow_engine.py
compute/lib/bc_adams_shadow_ktheory_engine.py
compute/lib/bc_arakelov_shadow_height_engine.py
compute/lib/bc_baxter_q_shadow_engine.py
compute/lib/bc_bootstrap_shadow_zeros_engine.py
compute/lib/bc_bott_periodicity_shadow_engine.py
compute/lib/bc_bridgeland_shadow_stability_engine.py
compute/lib/bc_bsd_shadow_engine.py
compute/lib/bc_calogero_moser_shadow_engine.py
compute/lib/bc_casimir_shadow_engine.py
compute/lib/bc_categorified_zeta_shadow_engine.py
compute/lib/bc_celestial_deep_shadow_engine.py
 succeeded in 52ms:
r"""Shadow Painleve engine: isomonodromic deformations from the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

The shadow generating function H(t) = t^2 * sqrt(Q_L(t)) is algebraic of
degree 2.  Here Q_L(t) = q_0 + q_1*t + q_2*t^2 is the shadow metric with

    q_0 = 4*kappa^2,  q_1 = 12*kappa*alpha,  q_2 = 9*alpha^2 + 2*Delta

where Delta = 8*kappa*S_4 is the critical discriminant.

THE SCHRODINGER ODE
===================

The shadow connection nabla^sh = d - (Q_L'/(2*Q_L)) dt has flat sections
Phi(t) = sqrt(Q_L(t)/Q_L(0)).  Promoting this logarithmic connection to a
second-order Schrodinger equation via the Liouville substitution psi =
Phi^{-1/2} * u gives:

 succeeded in 52ms:
"""
genus1_arithmetic_shadow.py — The genus-1 arithmetic shadow of Θ_A.

SYNTHESIS: Three genus-1 invariants of a chiral algebra A sit in a triangle:

                     ε^c_s(A)
                    /         \
                   /           \
    Koszul duality/             \Rankin-Selberg
                 /               \
    S_A(u) -------- sewing -------- F^conn_A(q)

Left edge: Connected Dirichlet-sewing lift (prime side)
  S_A(u) = Σ a_A(N) N^{-u} = ζ(u+1) Σ_i (ζ(u) - H_{w_i-1}(u))
  Has Euler product iff all weights = 1 (Heisenberg, βγ)

Right edge: Benjamin-Chang constrained Epstein (zero side)
  ε^c_s = Σ_{Δ∈S} (2Δ)^{-s}
  Poles at s = (1+z_n)/2 where z_n are nontrivial zeta zeros
  Functional equation from ζ(2s)/ζ(2s-1) ratio
 succeeded in 52ms:
r"""Modular bootstrap constraints from the shadow obstruction tower.

The conformal bootstrap constrains CFT data via crossing symmetry and
unitarity.  The MODULAR bootstrap constrains the partition function
Z(tau) = sum_i |chi_i(q)|^2 by demanding SL(2,Z) invariance.  The shadow
tower from the Maurer-Cartan equation provides ADDITIONAL, independent
constraints that intersect the modular bootstrap polytope.

MATHEMATICAL FRAMEWORK
======================

1. MODULAR INVARIANCE:
   Z(tau) = sum_{i,j} M_{ij} chi_i(q) chi_j(q-bar)
   where M is a modular invariant matrix (non-negative integers, M_{00}=1).
   For diagonal theories: M = I, so Z = sum_i |chi_i|^2.

   Under SL(2,Z) generators:
     S: tau -> -1/tau, chi_i(-1/tau) = sum_j S_{ij} chi_j(tau)
     T: tau -> tau+1, chi_i(tau+1) = T_{ii} chi_i(tau) = e^{2pi i (h_i - c/24)} chi_i(tau)

 succeeded in 51ms:
Total output lines: 366

compute/tests/test_shadow_trace_formula_engine.py
compute/tests/test_bc_weil_explicit_shadow_engine.py
compute/tests/test_virasoro_shadow_tower.py
compute/tests/test_borcherds_shadow_operations.py
compute/tests/test_non_simply_laced_shadows.py
compute/tests/test_bc_genus34_shadow_graph_engine.py
compute/tests/test_shadow_tower_asymptotics.py
compute/tests/test_bc_categorified_zeta_shadow_engine.py
compute/tests/test_bc_derived_moduli_shadow_engine.py
compute/tests/test_shadow_connection.py
compute/tests/test_agt_nekrasov_shadow_engine.py
compute/tests/test_shadow_cohft_independent.py
compute/tests/test_bh_entropy_shadow_cohft.py
compute/tests/test_bc_topological_recursion_shadow_engine.py
compute/tests/test_w3_2d_shadow_metric.py
compute/tests/test_n2_superconformal_shadow.py
compute/tests/test_virasoro_shadow_duality.py
compute/tests/test_shadow_motivic_hodge_engine.py
exec
/bin/zsh -lc "sed -n '200,400p' compute/lib/genus1_arithmetic_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    The key connection between S_A(u) and Benjamin-Chang ε^c_s.

    At the self-dual radius R=1:
      ε^1_s(R=1) = 4ζ(2s)  (scalar primary sum)
      S_H(u) = ζ(u)ζ(u+1)  (connected sewing lift)

    These are related by:
      ε^1_s = 4ζ(2s) = Dirichlet series over SCALAR PRIMARIES
      S_H(u) = ζ(u)ζ(u+1) = Dirichlet series over SEWING AMPLITUDES

    The connecting transform is:
      ε^1_s = 4 Σ k^{-2s}  (sum over lattice points k)
      S_H(u) = Σ σ_{-1}(N) N^{-u}  (sum over levels N)

    The passage from ε to S goes through:
      1. Extract scalar primaries (strip descendants via |η|^{2c})
      2. Take logarithm (connected part)
      3. Mellin transform in the q-variable

    So: S_A = Mellin_q(log(η^{-2c} · Z_A))  vs  ε^c_s = Mellin_y(η^{2c} · Z_A)
exec
/bin/zsh -lc 'rg -n "genus1_arithmetic_shadow" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/SI05_test_coverage.md:5:- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — Exact companion test `compute/tests/test_genus1_arithmetic_shadow.py` is absent, and `rg -n "genus1_arithmetic_shadow" compute/tests` returned no hits.
audit_campaign_20260412_231034/SI05_test_coverage.md:196:/bin/zsh -lc 'for f in compute/lib/__init__.py compute/lib/abjm_holographic_datum.py compute/lib/alpha_g_simple_lie_verification_engine.py compute/lib/arithmetic_comparison_test.py compute/lib/bar_graph_complex_bridge_engine.py compute/lib/bethe_tq_relation_engine.py compute/lib/bv_brst_purity_engine.py compute/lib/cohft_dr_hierarchy_engine.py compute/lib/cohft_givental_rmatrix_engine.py compute/lib/cohft_string_genus2_engine.py compute/lib/cohft_toprec_string_engine.py compute/lib/cohft_virasoro_constraints_engine.py compute/lib/coxeter_anomaly_test.py compute/lib/delta_fg_degree_pattern_engine.py compute/lib/dmod_counterexample_search_engine.py compute/lib/dmod_filtration_ss_engine.py compute/lib/dmod_kl_purity_engine.py compute/lib/dmod_mixed_hodge_bar_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/e8_lattice_bar.py compute/lib/euler_koszul_moments.py compute/lib/feynman_integral_engine.py compute/lib/formality_obstruction_loop4_engine.py compute/lib/genus1_arithmetic_shadow.py compute/lib/graph_complex_cohomology_engine.py compute/lib/graph_complex_orientation_database.py compute/lib/holographic_dmod_purity_engine.py compute/lib/integrable_genus2_engine.py compute/lib/kac_chevalley_test.py compute/lib/lattice_genus2_theta.py; do base=$(basename "$f" .py); t="compute/tests/test_${base}.py"; if [ -f "$t" ]; then echo PRESENT:$t; else echo ABSENT:$t; fi; done' in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/SI05_test_coverage.md:197:/bin/zsh -lc 'for f in compute/lib/__init__.py compute/lib/abjm_holographic_datum.py compute/lib/alpha_g_simple_lie_verification_engine.py compute/lib/arithmetic_comparison_test.py compute/lib/bar_graph_complex_bridge_engine.py compute/lib/bethe_tq_relation_engine.py compute/lib/bv_brst_purity_engine.py compute/lib/cohft_dr_hierarchy_engine.py compute/lib/cohft_givental_rmatrix_engine.py compute/lib/cohft_string_genus2_engine.py compute/lib/cohft_toprec_string_engine.py compute/lib/cohft_virasoro_constraints_engine.py compute/lib/coxeter_anomaly_test.py compute/lib/delta_fg_degree_pattern_engine.py compute/lib/dmod_counterexample_search_engine.py compute/lib/dmod_filtration_ss_engine.py compute/lib/dmod_kl_purity_engine.py compute/lib/dmod_mixed_hodge_bar_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/e8_lattice_bar.py compute/lib/euler_koszul_moments.py compute/lib/feynman_integral_engine.py compute/lib/formality_obstruction_loop4_engine.py compute/lib/genus1_arithmetic_shadow.py compute/lib/graph_complex_cohomology_engine.py compute/lib/graph_complex_orientation_database.py compute/lib/holographic_dmod_purity_engine.py compute/lib/integrable_genus2_engine.py compute/lib/kac_chevalley_test.py compute/lib/lattice_genus2_theta.py; do if [ -f "$f" ]; then line=$(sed -n '"'1p' \""'$f"); printf '"'%s:1:%s
audit_campaign_20260412_231034/SI05_test_coverage.md:208:compute/lib/genus1_arithmetic_shadow.py:1:"""
audit_campaign_20260412_231034/SI05_test_coverage.md:318:/bin/zsh -lc 'for f in compute/lib/__init__.py compute/lib/abjm_holographic_datum.py compute/lib/alpha_g_simple_lie_verification_engine.py compute/lib/arithmetic_comparison_test.py compute/lib/bar_graph_complex_bridge_engine.py compute/lib/bethe_tq_relation_engine.py compute/lib/bv_brst_purity_engine.py compute/lib/cohft_dr_hierarchy_engine.py compute/lib/cohft_givental_rmatrix_engine.py compute/lib/cohft_string_genus2_engine.py compute/lib/cohft_toprec_string_engine.py compute/lib/cohft_virasoro_constraints_engine.py compute/lib/coxeter_anomaly_test.py compute/lib/delta_fg_degree_pattern_engine.py compute/lib/dmod_counterexample_search_engine.py compute/lib/dmod_filtration_ss_engine.py compute/lib/dmod_kl_purity_engine.py compute/lib/dmod_mixed_hodge_bar_engine.py compute/lib/dmod_purity_char_variety_engine.py compute/lib/e8_lattice_bar.py compute/lib/euler_koszul_moments.py compute/lib/feynman_integral_engine.py compute/lib/formality_obstruction_loop4_engine.py compute/lib/genus1_arithmetic_shadow.py compute/lib/graph_complex_cohomology_engine.py compute/lib/graph_complex_orientation_database.py compute/lib/holographic_dmod_purity_engine.py compute/lib/integrable_genus2_engine.py compute/lib/kac_chevalley_test.py compute/lib/lattice_genus2_theta.py; do base=$(basename "$f" .py); stem=${base%_engine}; stem=${stem%_test}; echo "BASE:$base"; rg --files compute/tests | rg "/test_${stem}([._].*)?'"\\.py"'$|/test_.*${stem}.*'"\\.py"'$" || true; echo "--"; done' in /Users/raeez/chiral-bar-cobar succeeded in 408ms:
audit_campaign_20260412_231034/SI05_test_coverage.md:347:/bin/zsh -lc 'for stem in abjm_holographic_datum e8_lattice_bar euler_koszul_moments feynman_integral_engine genus1_arithmetic_shadow graph_complex_cohomology_engine graph_complex_orientation_database lattice_genus2_theta __init__; do echo "STEM:$stem"; rg -n "$stem" compute/tests || true; echo "--"; done' in /Users/raeez/chiral-bar-cobar succeeded in 147ms:
audit_campaign_20260412_231034/SI05_test_coverage.md:495:I’m working on classifying the tests and have identified a few with no exact matching test files or references in compute/tests, including `euler_koszul_moments`, `feynman_integral_engine`, and `genus1_arithmetic_shadow`. I think I should also look into `lattice_genus2_theta` since it has a comment mention. It might help to search specifically for relevant imports. I’ll check imports for modules such as `abjm`, `e8`, and `graph_complex_orientation_database` as well. For `abjm_holographic_datum`, I can't find a direct import related to an exact test. Let's analyze 9 of them more closely.
audit_campaign_20260412_231034/SI05_test_coverage.md:499:/bin/zsh -lc 'for stem in abjm_holographic_datum e8_lattice_bar euler_koszul_moments feynman_integral_engine genus1_arithmetic_shadow graph_complex_cohomology_engine graph_complex_orientation_database lattice_genus2_theta; do echo "STEM:$stem"; rg -n "from .*${stem}|import .*${stem}|${stem}'"\\.\" compute/tests || true; echo \"--\"; done" in /Users/raeez/chiral-bar-cobar succeeded in 140ms:
audit_campaign_20260412_231034/SI05_test_coverage.md:559:- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — Exact companion test `compute/tests/test_genus1_arithmetic_shadow.py` is absent, and `rg -n "genus1_arithmetic_shadow" compute/tests` returned no hits.
wave2_audit_20260413_001942/U11_test_gaps.md:6:- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:539:compute/lib/genus1_arithmetic_shadow.py|near=|refs=
wave2_audit_20260413_001942/U11_test_gaps.md:1089:[HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:1169:[HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:1190:- [HIGH] compute/lib/genus1_arithmetic_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_genus1_arithmetic_shadow.py`, and no current test imports it directly. FIX: add `compute/tests/test_genus1_arithmetic_shadow.py` with direct imports and module-scoped assertions.
fix_wave_C_20260413_175943/C08_sc_self_dual_fix.md:250:/Users/raeez/chiral-bar-cobar/compute/lib/genus1_arithmetic_shadow.py-203-      ε^1_s(R=1) = 4ζ(2s)  (scalar primary sum)
compute/lib/genus_tower_l_hierarchy.py:55:  rankin_selberg_bridge.py, genus1_arithmetic_shadow.py.
compute/lib/genus1_arithmetic_shadow.py:2:genus1_arithmetic_shadow.py — The genus-1 arithmetic shadow of Θ_A.

exec
/bin/zsh -lc 'rg -n "modular_bootstrap_shadow" -n' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
wave2_audit_20260413_001942/U11_test_gaps.md:11:- [HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:554:/bin/zsh -lc "for base in __init__ abjm_holographic_datum e8_lattice_bar graph_complex_orientation_database lattice_genus2_theta mc4_stage4_resolution mc5_genus_geq2_strategies modular_bootstrap_shadow modular_periodicity_test multigen_universality_attack niemeier_multichannel poincare_duality_engine siegel_eisenstein toroidal_bar w3_bar_extended w4_ds_ope w_algebra_transport_propagation; do printf 'BASE %s\\n' \""'$base"; rg -n "$base" compute/tests || true; printf '"'---\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 236ms:
wave2_audit_20260413_001942/U11_test_gaps.md:559:BASE modular_bootstrap_shadow
wave2_audit_20260413_001942/U11_test_gaps.md:560:compute/tests/test_conformal_bootstrap_mc_engine.py:64:    modular_bootstrap_shadow_verification,
wave2_audit_20260413_001942/U11_test_gaps.md:561:compute/tests/test_conformal_bootstrap_mc_engine.py:472:        data = modular_bootstrap_shadow_verification(Rational(1))
wave2_audit_20260413_001942/U11_test_gaps.md:562:compute/tests/test_conformal_bootstrap_mc_engine.py:479:        data = modular_bootstrap_shadow_verification(Rational(24))
wave2_audit_20260413_001942/U11_test_gaps.md:563:compute/tests/test_conformal_bootstrap_mc_engine.py:485:            data = modular_bootstrap_shadow_verification(c_val)
wave2_audit_20260413_001942/U11_test_gaps.md:564:compute/tests/test_conformal_bootstrap_mc_engine.py:491:            data = modular_bootstrap_shadow_verification(c_val)
wave2_audit_20260413_001942/U11_test_gaps.md:579:I'm looking into `lattice_genus2_theta`, and it seems the only relevant part is a mention in the docstring on line 15, which means there's no import. Similarly, `poincare_duality_engine.py` only matches a comment line in `test_poincare_duality_bar_engine.py`, showing zero direct coverage too. I think I should classify them as high-priority. For `modular_bootstrap_shadow.py`, I suspect test functions reference `modular_bootstrap_shadow_verification`. I need to check import lines in `test_conformal_bootstrap_mc_engine.py` to confirm. Also, `__init__.py` matches false positives due to method names and comments, indicating zero coverage overall.
wave2_audit_20260413_001942/U11_test_gaps.md:581:/bin/zsh -lc "for base in __init__ abjm_holographic_datum e8_lattice_bar graph_complex_orientation_database lattice_genus2_theta mc4_stage4_resolution mc5_genus_geq2_strategies modular_bootstrap_shadow modular_periodicity_test multigen_universality_attack niemeier_multichannel poincare_duality_engine siegel_eisenstein toroidal_bar w3_bar_extended w4_ds_ope w_algebra_transport_propagation; do printf 'BASE %s\\n' \""'$base"; rg -n "from .*${base}|import .*${base}" compute/tests || true; printf '"'---\\n'; done" in /Users/raeez/chiral-bar-cobar succeeded in 248ms:
wave2_audit_20260413_001942/U11_test_gaps.md:587:BASE modular_bootstrap_shadow
wave2_audit_20260413_001942/U11_test_gaps.md:675:I'm realizing that `mc5_genus_geq2_strategies.py` isn't imported, which means there's a lack of coverage since the relevant tests are targeting something else. It also seems that `poincare_duality_engine.py` isn't tested, as the focus is on a different module. I need to check `modular_bootstrap_shadow.py` too, since it looks like it's not imported. We really should ensure that all modules are correctly referenced and covered in tests. This could apply to other modules with similar issues as well.
wave2_audit_20260413_001942/U11_test_gaps.md:1094:[HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:1174:[HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:1195:- [HIGH] compute/lib/modular_bootstrap_shadow.py:1 — PROBLEM: This module has no matching `compute/tests/test_modular_bootstrap_shadow.py`, and `test_conformal_bootstrap_mc_engine.py` exercises a different engine instead of importing this file. FIX: add `compute/tests/test_modular_bootstrap_shadow.py` with direct imports and modular-bootstrap assertions.
compute/lib/conformal_bootstrap_mc_engine.py:984:def modular_bootstrap_shadow_verification(c_val):
compute/tests/test_conformal_bootstrap_mc_engine.py:64:    modular_bootstrap_shadow_verification,
compute/tests/test_conformal_bootstrap_mc_engine.py:472:        data = modular_bootstrap_shadow_verification(Rational(1))
compute/tests/test_conformal_bootstrap_mc_engine.py:479:        data = modular_bootstrap_shadow_verification(Rational(24))
compute/tests/test_conformal_bootstrap_mc_engine.py:485:            data = modular_bootstrap_shadow_verification(c_val)
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Modular bootstrap constraints from the shadow obstruction tower.

The conformal bootstrap constrains CFT data via crossing symmetry and
unitarity.  The MODULAR bootstrap constrains the partition function
Z(tau) = sum_i |chi_i(q)|^2 by demanding SL(2,Z) invariance.  The shadow
tower from the Maurer-Cartan equation provides ADDITIONAL, independent
constraints that intersect the modular bootstrap polytope.

MATHEMATICAL FRAMEWORK
======================

1. MODULAR INVARIANCE:
   Z(tau) = sum_{i,j} M_{ij} chi_i(q) chi_j(q-bar)
   where M is a modular invariant matrix (non-negative integers, M_{00}=1).
   For diagonal theories: M = I, so Z = sum_i |chi_i|^2.

   Under SL(2,Z) generators:
     S: tau -> -1/tau, chi_i(-1/tau) = sum_j S_{ij} chi_j(tau)
     T: tau -> tau+1, chi_i(tau+1) = T_{ii} chi_i(tau) = e^{2pi i (h_i - c/24)} chi_i(tau)

thinking
**Exploring tests and functions**

I need to further inspect existing tests like "kappa_painleve_engine" or "arithmetic_shadow_connection." It could help to use "rg" for test patterns and possibly look into an explorer. I might also need to explore functions related to the public API. Inspecting the bottom sections of engines sounds like a good plan. I should consider importing functions and dataclasses, and I’ll search for definitions to gather more information.
exec
/bin/zsh -lc "rg -n '"'^def |''^class '"' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'^def |''^class '"' compute/lib/genus1_arithmetic_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '"'^def |''^class '"' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
93:def kappa_virasoro(c_val):
100:def kappa_affine_km(k_val, h_dual, dim_g):
107:def lambda_fp(g: int) -> Rational:
118:def F_g(kappa_val, g: int):
123:def virasoro_shadow_data(c_val):
144:def shadow_planted_forest_genus2(kappa_val, S_3_val):
155:def minimal_model_data(p: int, q: int) -> Dict[str, Any]:
219:def ising_model_data() -> Dict[str, Any]:
276:def verify_S_squared(S: np.ndarray, tol: float = 1e-10) -> Tuple[bool, np.ndarray]:
288:def verify_ST_cubed(S: np.ndarray, T: np.ndarray,
301:def verify_S_unitarity(S: np.ndarray, tol: float = 1e-10) -> Tuple[bool, np.ndarray]:
315:def verify_S_symmetry(S: np.ndarray, tol: float = 1e-10) -> bool:
324:def verlinde_fusion(S: np.ndarray) -> np.ndarray:
345:def verify_fusion_integrality(N: np.ndarray, tol: float = 1e-8) -> bool:
353:def ising_fusion_rules() -> Dict[str, int]:
375:def shadow_genus1_constraint(kappa_val):
386:def shadow_genus2_constraint(kappa_val, S_3_val):
402:def shadow_wdvv_constraint(kappa_val, S_3_val, S_4_val, dim_V: int = 1):
425:def hellerman_bound(c_val: float) -> float:
442:def friedan_keller_bound(c_val: float) -> float:
 succeeded in 50ms:
65:def _zeta_reg(u):
73:class ChiralArithmeticShadow:
145:def W_family(N):
153:def triangle_analysis(family, n_li=10, n_sewing=20):
198:def bc_bridge_analysis():
263:def quartic_interacting_analysis():
321:def two_variable_L_analysis():
 succeeded in 51ms:
227:def shadow_metric_poly(kappa, alpha, Delta):
240:def shadow_metric_coefficients(kappa, alpha, Delta):
248:def shadow_metric_discriminant(kappa, alpha, Delta):
256:def schwarzian_potential_symbolic():
279:def schwarzian_potential_verify():
299:def schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val, t_val):
318:class SingularityData:
327:def classify_singularities(kappa_val, alpha_val, Delta_val):
468:def singularity_count(kappa_val, alpha_val, Delta_val):
481:def fuchsian_type(kappa_val, alpha_val, Delta_val):
509:def painleve_type(kappa_val, alpha_val, Delta_val):
555:def painleve_type_multichannel(channels):
596:def heun_from_shadow_multichannel(kappa_T, alpha_T, Delta_T,
663:def shadow_tau_function_genus_expansion(kappa_val, r_max=20, g_max=10):
696:def tau_function_log_series(kappa_val, g_max=10):
706:def jmu_hamiltonian(kappa_val, alpha_val, Delta_val, t_val):
730:def jmu_tau_from_connection(kappa_val, alpha_val, Delta_val, t_val):
748:def hypergeometric_parameters(kappa_val, alpha_val, Delta_val):
875:def shadow_deformation_system(c_val):
934:def matrix_model_potential(kappa_val, alpha_val, Delta_val, t_val):
exec
/bin/zsh -lc "sed -n '200,400p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
                           * math.sin(math.pi * r1 * r2 / q)
                           * math.sin(math.pi * s1 * s2 / p))

    # T-matrix
    c_float = float(c)
    T_mat = np.zeros((n_prim, n_prim), dtype=complex)
    for i, (_, _, h) in enumerate(primaries):
        h_float = float(h)
        T_mat[i, i] = np.exp(2j * np.pi * (h_float - c_float / 24.0))

    return {
        'p': p, 'q': q, 'c': c,
        'primaries': primaries,
        'n_primaries': n_prim,
        'S': S_mat,
        'T': T_mat,
    }


def ising_model_data() -> Dict[str, Any]:
exec
/bin/zsh -lc "sed -n '1,240p' compute/tests/test_arithmetic_shadow_connection.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_shadow_bootstrap_attack.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_kappa_painleve_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
#!/usr/bin/env python3
"""
test_shadow_bootstrap_attack.py — MC-enhanced bootstrap attack on scattering matrix.

T1-T15:  Narain universality theorem
T16-T25: Shadow-moment tower
T26-T35: Moment-Li bridge
T36-T45: MC-enhanced bootstrap and Virasoro constraints
T46-T55: Residue analysis and the bootstrap closure
"""

import pytest
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from shadow_bootstrap_attack import (
    narain_epstein_analytic, narain_epstein_direct, verify_narain_universality,
    narain_zero_universality,
    shadow_moment, shadow_moment_tower, shadow_moment_generating_function,
 succeeded in 52ms:
#!/usr/bin/env python3
r"""
test_arithmetic_shadow_connection.py — Tests for arithmetic packet connection nabla^arith.

T1-T6:   Packet construction for standard families
T7-T12:  Connection form computation
T13-T18: Flatness verification
T19-T24: Singular divisor structure
T25-T30: Frontier defect form and gauge criterion
T31-T36: Verdier involution and complementarity
T37-T42: Miura splitting for W_N
T43-T48: Depth decomposition
T49-T55: Semisimplicity and unipotence verification
"""

import pytest
import math
import cmath
import sys
import os
 succeeded in 52ms:
r"""Tests for kappa_painleve_engine.py -- kappa-deformed Painleve I.

Covers the seven tasks:
  1. Numerical solution of kappa-P_I at kappa = 1, 13, 24
  2. Tritronquee asymptotics
  3. Stokes multipliers (Kapaev)
  4. Dispersionless limit
  5. Fredholm / kernel structure (benchmarks vs. Airy)
  6. Isomonodromic deformation
  7. Random matrix / beta-ensemble identification

Plus:
  - Rescaling theorem (the load-bearing identity): cross-verification via two
    independent integration paths.
  - Multi-path verification of all published constants.
  - Anti-pattern guards (AP24, AP39, AP48 for kappa values).

Total: 50+ tests.
"""

exec
/bin/zsh -lc "sed -n '400,800p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


def shadow_wdvv_constraint(kappa_val, S_3_val, S_4_val, dim_V: int = 1):
    """WDVV constraint from MC at (0,4).

    For 1-dimensional V (Virasoro, Heisenberg): WDVV is automatic
    (a single associativity equation in 1D is trivially satisfied).

    For dim V >= 2: WDVV = Jacobi identity for the cubic shadow.
    The quartic shadow S_4 is then determined by WDVV + MC.

    Returns True if WDVV is satisfied.
    """
    if dim_V == 1:
        # 1D associativity is trivially satisfied
        return True
    # For higher dimensions, WDVV involves the cubic structure constants
    # and constrains S_4.  Not implemented for general case.
    return None


exec
/bin/zsh -lc "sed -n '800,1200p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    }


# =========================================================================
# 10. Genus-2 Sp(4,Z) constraints
# =========================================================================

def genus2_sp4z_constraint_count(n_primaries: int) -> int:
    """Number of independent Sp(4,Z) constraints at genus 2.

    The genus-2 partition function Z_2(Omega) has n^2 coefficients
    (for n primaries in the diagonal theory).
    Sp(4,Z) has generators S, T, U (10-dimensional group).
    The number of constraints from Sp(4,Z) invariance is large.

    For a diagonal theory: Z_2 = sum_i chi_i^2 (schematic).
    The Sp(4,Z) constraints are:
      n_constraints = dim(Sp(4,Z)) - dim(stabilizer)
                    ~ 10 independent conditions

thinking
**Gathering engine file content**

I realize I need more than the first 260 lines of the missing engine files — I might need all functions to effectively test them. The existing tests seem inadequate, which is concerning. I should focus on using straightforward functions with precise formulas to achieve accurate results. However, I'll need to wait for the explorer tool to help me gather the right information before proceeding. Let's ensure I have everything for the best outcome!
collab wait(call_Game6b1cuWist1pHUaXhTmKd)
  receivers: 019d87a9-3228-7132-8c7d-2c38fdcbec09
exec
/bin/zsh -lc "sed -n '1,200p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Shadow Painleve engine: isomonodromic deformations from the shadow obstruction tower.

MATHEMATICAL FRAMEWORK
======================

The shadow generating function H(t) = t^2 * sqrt(Q_L(t)) is algebraic of
degree 2.  Here Q_L(t) = q_0 + q_1*t + q_2*t^2 is the shadow metric with

    q_0 = 4*kappa^2,  q_1 = 12*kappa*alpha,  q_2 = 9*alpha^2 + 2*Delta

where Delta = 8*kappa*S_4 is the critical discriminant.

THE SCHRODINGER ODE
===================

The shadow connection nabla^sh = d - (Q_L'/(2*Q_L)) dt has flat sections
Phi(t) = sqrt(Q_L(t)/Q_L(0)).  Promoting this logarithmic connection to a
second-order Schrodinger equation via the Liouville substitution psi =
Phi^{-1/2} * u gives:

exec
/bin/zsh -lc "sed -n '200,400p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
from typing import Any, Dict, List, Optional, Sequence, Tuple

from sympy import (
    Abs, I, Matrix, Poly, Rational, S, Symbol,
    cancel, conjugate, cos, diff, expand, factor,
    im, integrate, log, numer, denom, oo, pi, re, simplify,
    sin, solve, sqrt, symbols, together, collect, series,
    binomial, gamma, factorial, bernoulli, exp, atan2,
    Function, Eq,
)

# =========================================================================
# Symbols
# =========================================================================

c_sym = Symbol('c')
t_sym = Symbol('t')
lam_sym = Symbol('lambda')
kappa_sym = Symbol('kappa')
alpha_sym = Symbol('alpha')
exec
/bin/zsh -lc "sed -n '400,800p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
                rho1 = (1 + sqrt_di) / 2
                rho2 = (1 - sqrt_di) / 2
                result.append(SingularityData(
                    location=t0,
                    type='regular',
                    rank=0,
                    indicial_exponents=(rho1, rho2),
                    is_finite=True
                ))

    # Point at infinity: substitute t = 1/s, u(t) = w(s)
    # u'' = s^4 w'' + 2*s^3 w'  (standard transformation)
    # The equation s^4 w'' + 2*s^3 w' - V(1/s)*w = 0
    # V(1/s) = 8*kappa^2*Delta / Q_L(1/s)^2
    # Q_L(1/s) = q0 + q1/s + q2/s^2 = (q0*s^2 + q1*s + q2)/s^2
    # V(1/s) = 8*kappa^2*Delta * s^4 / (q0*s^2 + q1*s + q2)^2
    # So the equation in s: s^4*w'' + 2*s^3*w' = V(1/s)*w = 8*kappa^2*Delta*s^4/(...)^2 * w
    # Dividing by s^4: w'' + 2/s*w' = 8*kappa^2*Delta/(q0*s^2+q1*s+q2)^2 * w
    # At s=0: the RHS ~ 8*kappa^2*Delta/q2^2 (finite, nonzero if Delta,q2 != 0)
    # The LHS has w'' + 2/s*w', which has a regular singular point at s=0.
exec
/bin/zsh -lc "sed -n '800,1200p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

    # Wait -- let's recompute.  c_0 = 8*kappa^2*Delta / Qp^2.
    # Qp(t_+) = q1 + 2*q2*t_+ = sqrt(disc) (from quadratic formula).
    # So Qp_+^2 = disc = -32*kappa^2*Delta.
    # c0_+ = 8*kappa^2*Delta / (-32*kappa^2*Delta) = -1/4.
    # Indicial: rho*(rho-1) = -1/4, so rho^2 - rho + 1/4 = 0,
    # (rho - 1/2)^2 = 0, rho = 1/2 (double root!).

    # This means each zero of Q_L is an APPARENT singularity with
    # exponents {1/2, 1/2} (logarithmic case).  Actually, the double
    # indicial root means either a regular solution or a logarithmic
    # solution at that point.

    # For sqrt(Q_L) at a simple zero: sqrt(Q) ~ sqrt(Q'(t0)*(t-t0))
    # = sqrt(Q'(t0)) * (t-t0)^{1/2}, which has exponent 1/2.
    # So the indicial exponent 1/2 is correct.

    # Hypergeometric parameters:
    # At z=0 (corresponding to t=t_-): exponents {rho1, rho2} = {1/2, 1/2}
    # At z=1 (corresponding to t=t_+): exponents {sigma1, sigma2} = {1/2, 1/2}
exec
/bin/zsh -lc "sed -n '1200,1600p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
            # Simplified Euler step (RK4 on complex contour is more involved)
            k1_u = dt_complex * v
            k1_v = dt_complex * V1 * u

            u += k1_u
            v += k1_v

        results.append((u, v))

    # Monodromy matrix: columns are the transported fundamental solutions
    M = [[results[0][0], results[1][0]],
         [results[0][1], results[1][1]]]

    trace = M[0][0] + M[1][1]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]

    # Eigenvalues from trace and det
    disc_M = trace**2 - 4 * det
    sqrt_disc_M = cmath.sqrt(disc_M)
    eig1 = (trace + sqrt_disc_M) / 2
exec
/bin/zsh -lc 'rg -n "shadow_painleve" -n compute/tests' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "shadow_painleve"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/U11_test_gaps.md:14:- [HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:1097:[HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:1177:[HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
wave2_audit_20260413_001942/U11_test_gaps.md:1198:- [HIGH] compute/lib/shadow_painleve.py:1 — PROBLEM: This module has no matching `compute/tests/test_shadow_painleve.py`, and no current test imports it directly. FIX: add `compute/tests/test_shadow_painleve.py` with direct imports and Painleve-shadow assertions.
compute/lib/shadow_painleve.py:1282:def full_shadow_painleve_analysis(c_val):
compute/lib/shadow_painleve.py:1495:    data = full_shadow_painleve_analysis(0.5)
compute/lib/shadow_painleve.py:1502:    data = full_shadow_painleve_analysis(13.0)
compute/lib/kappa_painleve_engine.py:176:shadow_painleve.py            -- shadow connection / Heun (different ODE family)
compute/lib/bc_painleve_shadow_engine.py:55:   theorem (rigid Fuchsian), not a deficiency.  The existing shadow_painleve.py
compute/lib/bc_painleve_shadow_engine.py:73:    shadow_painleve.py -- base infrastructure
compute/lib/quantum_spectral_curve.py:9:equation (shadow_painleve.py, Section 1):
compute/lib/quantum_spectral_curve.py:88:    shadow_painleve.py -- Schwarzian potential, singularity classification
exec
/bin/zsh -lc "sed -n '1,200p' compute/tests/test_conformal_bootstrap_mc_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
wait(call_Game6b1cuWist1pHUaXhTmKd) timed out:
codex
The missing surfaces are concrete now. I’m extracting tests from formulas the engines already state explicitly, not from their own output, so each new file gets smoke coverage with independent expected values and at least one limiting-case check.
exec
/bin/zsh -lc "sed -n '260,420p' compute/lib/genus1_arithmetic_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '560,980p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '860,1020p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,520p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,860p' compute/lib/modular_bootstrap_shadow.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,560p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '980,1500p' compute/lib/shadow_painleve.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# The quartic shadow as first interacting correction
# =============================================================================

def quartic_interacting_analysis():
    """
    The weight-level S_A(u) captures the FREE-FIELD arithmetic shadow.
    The quartic resonance class Q^contact is the FIRST INTERACTING correction.

    Free field: spectrum determined by weights alone → S_A(u)
    Interacting: OPE structure constants modify the sewing operator

    The shadow depth classification:
      G (depth 2): free-field exact (Heisenberg, quadratic OPE)
      L (depth 3): tree-level correction (affine, cubic OPE)
      C (depth 4): contact correction (βγ, quartic OPE)
      M (depth ∞): infinite tower (Virasoro, all-order OPE)

    DEEP POINT: The Euler-Koszul defect order correlates with shadow depth
    but is NOT identical. The Euler defect measures the arithmetic structure
    of the CHARACTER. The shadow depth measures the OPE complexity.
 succeeded in 51ms:

    For c < 1: the intersection should contain exactly the minimal models
    (discrete spectrum).

    For c >= 1: continuous families are possible (e.g., Narain moduli space
    for c = 1, 2, ...).

    Returns analysis of the intersection.
    """
    kappa = c_val / 2.0

    # Shadow constraints
    F1 = kappa / 24.0
    S_3 = 2.0  # Virasoro cubic
    delta_pf = 2.0 * (20.0 - kappa) / 48.0

    # For c < 1: check which minimal models have this central charge
    minimal_models_at_c = []
    if c_val < 1:
        for m in range(3, 100):
 succeeded in 51ms:
    Liouville-transformed Schrodinger equation is:

        u'' - V(t) * u = 0

    where V(t) = (1/2)(Q_L'/Q_L)' - (1/4)(Q_L'/Q_L)^2

    For Q_L quadratic, this simplifies to:

        V(t) = (q_0*q_2 - q_1^2/4) / Q_L(t)^2
             = -disc(Q_L) / (4 * Q_L^2)
             = 8*kappa^2*Delta / Q_L^2

    Returns a symbolic expression in (kappa_sym, alpha_sym, Delta_sym, t_sym).
    """
    Q = shadow_metric_poly(kappa_sym, alpha_sym, Delta_sym)
    disc = shadow_metric_discriminant(kappa_sym, alpha_sym, Delta_sym)
    return -disc / (4 * Q**2)


def schwarzian_potential_verify():
 succeeded in 51ms:
    for i in range(3):
        T[i, i] = np.exp(2j * np.pi * (h_vals[i] - c_float / 24.0))

    return {
        'p': 4, 'q': 3, 'c': c,
        'primaries': primaries,
        'n_primaries': 3,
        'S': S,
        'T': T,
    }


# =========================================================================
# 2. Modular group relations verification
# =========================================================================

def verify_S_squared(S: np.ndarray, tol: float = 1e-10) -> Tuple[bool, np.ndarray]:
    """Verify S^2 = C (charge conjugation matrix).

    For minimal models with all self-conjugate representations, C = I.
 succeeded in 51ms:
    Combined with Sp(4,Z) invariance of Z_2(Omega), this gives additional
    constraints on the spectrum.

    The genus-2 partition function:
      Z_2(Omega) = sum_{i,j} M_{ij}^{(2)} chi_i chi_j
    is invariant under Sp(4,Z).

    The shadow constraint: F_2(A) = kappa * lambda_2^FP + delta_pf.
    For Virasoro: F_2 = c/2 * 7/5760 + 2*(20-c/2)/48.

    The improvement over genus-1 alone:
    - Genus-2 modular constraints cut deeper into the allowed region
    - The planted-forest term delta_pf provides arithmetic content
      not visible at genus 1

    Quantitative bound (numerical estimate):
    """
    kappa = c_val / 2.0
    F2_shadow = float(F_g(Rational(c_val) / 2 if isinstance(c_val, int) else kappa, 2))
    delta_pf = float(shadow_planted_forest_genus2(kappa, 2.0))
 succeeded in 51ms:

    The number of apparent parameters (accessory parameters) increases
    with the number of channels and singularities.

    Parameters:
        channels: list of (kappa, alpha, Delta) tuples, one per channel.

    Returns:
        Painleve type string.
    """
    n_channels = len(channels)

    if n_channels == 1:
        return painleve_type(*channels[0])

    # For 2 channels: the 2x2 system has additional singular points from
    # the inter-channel coupling.  The generic case has 4+ singularities
    # on P^1, giving Painleve VI.
    if n_channels == 2:
        # Check if both channels have nontrivial Delta
 succeeded in 51ms:
    Delta = 40.0 / (5 * c_val + 22)

    q0 = c_val**2  # 4*(c/2)^2
    q1 = 12 * c_val  # 12*(c/2)*2
    q2 = 36 + 2 * Delta  # 9*4 + 2*Delta

    return {
        'c': c_val,
        'kappa': kappa,
        'potential_type': 'complex_cubic' if Delta > 0 else 'real_cubic',
        'cut_type': 'complex' if Delta > 0 else 'real',
        'q0': q0,
        'q1': q1,
        'q2': q2,
        'Delta': Delta,
        'genus_0_free_energy': kappa * q0,  # placeholder
    }


# =========================================================================
exec
/bin/zsh -lc "nl -ba compute/lib/genus1_arithmetic_shadow.py | sed -n '30,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    30	   u-slice: Dirichlet-sewing lift S_A(u) (prime side)
    31	
    32	2. EULER-KOSZUL CRITERION:
    33	   A is Euler-Koszul iff S_A(u) factors as product of shifted ζ-functions.
    34	   Heisenberg: exact. Vir/W_N: finitely defective. Generic Epstein (h(D)≥2): NOT.
    35	   Defect = 1 - 1/ζ(u) for Virasoro — concentrated in critical strip.
    36	
    37	3. PRIME-SIDE Li COEFFICIENTS λ̃_n(A):
    38	   From Ξ_A(u) = (u-1)S_A(u), regularized at u=1.
    39	   Heisenberg: positive for n≤6, negative for n≥7.
    40	   Virasoro/W_N: all negative, exponentially growing.
    41	   NOT the same as zero-side Li coefficients for 4ζ(2s).
    42	
    43	4. SHADOW DEPTH ↔ EULER DEFECT:
    44	   G (depth 2): D_A = 1 (exact Euler-Koszul)
    45	   L (depth 3): D_A = 1 - O(1/ζ)
    46	   C (depth 4): D_A = 1 - O(1/ζ²)
    47	   M (depth ∞): infinite defect tower
    48	
    49	The weight-level arithmetic shadow captures the free-field / character level.
exec
/bin/zsh -lc "nl -ba compute/lib/modular_bootstrap_shadow.py | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	r"""Modular bootstrap constraints from the shadow obstruction tower.
     2	
     3	The conformal bootstrap constrains CFT data via crossing symmetry and
     4	unitarity.  The MODULAR bootstrap constrains the partition function
     5	Z(tau) = sum_i |chi_i(q)|^2 by demanding SL(2,Z) invariance.  The shadow
     6	tower from the Maurer-Cartan equation provides ADDITIONAL, independent
     7	constraints that intersect the modular bootstrap polytope.
     8	
     9	MATHEMATICAL FRAMEWORK
    10	======================
    11	
    12	1. MODULAR INVARIANCE:
    13	   Z(tau) = sum_{i,j} M_{ij} chi_i(q) chi_j(q-bar)
    14	   where M is a modular invariant matrix (non-negative integers, M_{00}=1).
    15	   For diagonal theories: M = I, so Z = sum_i |chi_i|^2.
    16	
    17	   Under SL(2,Z) generators:
    18	     S: tau -> -1/tau, chi_i(-1/tau) = sum_j S_{ij} chi_j(tau)
    19	     T: tau -> tau+1, chi_i(tau+1) = T_{ii} chi_i(tau) = e^{2pi i (h_i - c/24)} chi_i(tau)
    20	
exec
/bin/zsh -lc 'rg -n "shadow_genus1_constraint" -n compute/lib/modular_bootstrap_shadow.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
375:def shadow_genus1_constraint(kappa_val):
596:            entry['F_1'] = float(shadow_genus1_constraint(shadow_data['kappa']))
724:    F1 = shadow_genus1_constraint(kappa)
exec
/bin/zsh -lc 'rg -n "shadow_genus2_constraint" compute/lib/modular_bootstrap_shadow.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
386:def shadow_genus2_constraint(kappa_val, S_3_val):
exec
/bin/zsh -lc 'rg -n "shadow_metric_coefficients" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
240:def shadow_metric_coefficients(kappa, alpha, Delta):
623:    q0_T, q1_T, q2_T = shadow_metric_coefficients(kappa_T, alpha_T, Delta_T)
627:    q0_W, q1_W, q2_W = shadow_metric_coefficients(kappa_W, alpha_W, Delta_W)
722:    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)
736:    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)
904:    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, Delta)
952:    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)
1026:    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta)
1163:    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)

exec
/bin/zsh -lc 'rg -n "shadow_metric_discriminant" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
248:def shadow_metric_discriminant(kappa, alpha, Delta):
275:    disc = shadow_metric_discriminant(kappa_sym, alpha_sym, Delta_sym)
288:    disc = shadow_metric_discriminant(kappa_sym, alpha_sym, Delta_sym)
exec
/bin/zsh -lc 'rg -n "shadow_tau_function_genus_expansion" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
663:def shadow_tau_function_genus_expansion(kappa_val, r_max=20, g_max=10):
702:    Fg = shadow_tau_function_genus_expansion(kappa_val, g_max=g_max)
exec
/bin/zsh -lc 'rg -n "jmu_tau_from_connection" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
730:def jmu_tau_from_connection(kappa_val, alpha_val, Delta_val, t_val):
exec
/bin/zsh -lc 'rg -n "fuchsian_type" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
481:def fuchsian_type(kappa_val, alpha_val, Delta_val):
1290:    ftype = fuchsian_type(kappa, alpha, Delta)
1303:        'fuchsian_type': ftype,
1355:        'fuchsian_type': 'hypergeometric (Gauss)',
1498:    print(f"  Fuchsian type: {data['fuchsian_type']}")
1505:    print(f"  Fuchsian type: {data['fuchsian_type']}")
exec
/bin/zsh -lc 'rg -n "painleve_type" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
509:def painleve_type(kappa_val, alpha_val, Delta_val):
555:def painleve_type_multichannel(channels):
573:        return painleve_type(*channels[0])
1291:    ptype = painleve_type(kappa, alpha, Delta)
1304:        'painleve_type': ptype,
1406:        'painleve_type': 'PVI' if heun['n_singularities'] >= 4 else 'degenerate',
1499:    print(f"  Painleve type: {data['painleve_type']}")
1506:    print(f"  Painleve type: {data['painleve_type']}")
1514:    print(f"  Painleve type: {w3['painleve_type']}")
exec
/bin/zsh -lc 'rg -n "classify_singularities" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
327:def classify_singularities(kappa_val, alpha_val, Delta_val):
474:    sings = classify_singularities(kappa_val, alpha_val, Delta_val)
490:    sings = classify_singularities(kappa_val, alpha_val, Delta_val)
1289:    sings = classify_singularities(kappa, alpha, Delta)
exec
/bin/zsh -lc 'rg -n "singularity_count" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
468:def singularity_count(kappa_val, alpha_val, Delta_val):
exec
/bin/zsh -lc 'rg -n "hypergeometric_parameters" compute/lib/shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
748:def hypergeometric_parameters(kappa_val, alpha_val, Delta_val):
1292:    hyp = hypergeometric_parameters(kappa, alpha, Delta)



thinking
**Considering test dependencies**

I need to think about dependencies and speed while avoiding heavy tests; I’ll stick to basic smoke tests. For `genus1_arithmetic_shadow.py`, I consider potential tests like `test_heisenberg_S_matches_zeta_product_at_u2`, where HEISENBERG.S(2) should equal zeta(2) times zeta(3). I verified the [DC] definition with weights [1] and the [CF] Heisenberg exact Euler-Koszul from the docstring. I might use mp.almosteq. Another test is `test_virasoro_S_matches_single_weight_formula`, confirming VIRASORO.S(2) as zeta(3) times (zeta(2)-1).
thinking
**Planning tests for accuracy**

The user wanted smoke tests to ensure verified expected values. I’m considering testing functions like shadow_planted_forest_genus2 and shadow_genus2_constraint, using hardcoded expected values from independent formulas. This helps guard against potential docstring drift, which seems valuable. I could also examine functions like minimal_model_shadow_check and watch numeric functions with floats versus rationals, using Rational for precision. I'll detail tests focusing on rational or integer value parameters to maintain accuracy and confirm identities or parameters in the results.
thinking
**Structuring smoke tests**

I verified the formulas and noted that for self-dual cases with c=13, the Heisenberg_shadow_params function returns (1,0,0). I think it might be beneficial to separate this into two tests, but I need at least three smoke tests total. One idea is to create a test for when delta is zero, where the Heisenberg parameters yield Fuchsian and Painlevé types as 'trivial' with possibly one ordinary singularity. It's essential to confirm these results.
collab wait(call_ZO5i0VI6RFOCXvAWrq0kWyzw)
  receivers: 019d87a9-3228-7132-8c7d-2c38fdcbec09
thinking
**Summarizing missing shadow tests and module details**

I’m putting together a clear summary of missing test files for shadow-related modules like `genus1_arithmetic_shadow.py` and `modular_bootstrap_shadow.py`. I’ll highlight each module’s public API with line references, candidate test expectations with doc and code line details, and note import quirks like heavy `sympy` and `mpmath` usage. Though some existing tests indirectly cover related functions, no direct test files exist. I’ll close with suggested next steps to add those missing tests while keeping the message concise and user-friendly.
codex
**Missing Shadow Tests**

- `compute/lib/genus1_arithmetic_shadow.py` (no `compute/tests/test_genus1_arithmetic_shadow.py`, e.g. audit log `wave2_audit_20260413_001942/U11_test_gaps.md` highlights the hole).
  - Public API (lines 73‑134): `ChiralArithmeticShadow` with `S(u)`, `Xi(u)`, `euler_defect(u)`, `is_euler_koszul()`, `sewing_coefficients(...)`, and surface-moment helpers; standard factories `HEISENBERG`, `VIRASORO`, `BETA_GAMMA`, `W_family`.
  - Candidate smoke tests:
    1. Heisenberg shadow: `S_H(2)` should equal `ζ(2)*ζ(3)` (per doc’s “S_H(u) = ζ(u)ζ(u+1)” triangle, lines 30‑47) and `euler_defect(2)` should return `1`.
    2. Virasoro defect: instantiate `ChiralArithmeticShadow("Virasoro", [2])` and verify `euler_defect(3) == 1 - 1/ζ(3)` (since `D_A(u)=1-1/ζ(u)` for weights >1, documented same section).
    3. `is_euler_koszul()` is `True` for `HEISENBERG` and `False` for `VIRASORO`; the doc’s Euler-Koszul triangle (lines 32‑47) drives the expectation.
    4. `sewing_coefficients` for `HEISENBERG` should start `[1, 3/2, 4/3]` because `a_N = Σ_{d|N} (count/d)` with one weight ≤m.
    5. `surface_minors(alpha=2, max_size=2)` for `HEISENBERG` reduces to explicit determinants built from `S(2)=ζ(2)ζ(3)` and `S(3)=ζ(3)ζ(4)`, so assertions can compare to those known products.
  - Import/setup quirks: the module immediately sets `mp.dps = 40` (line 54‑58), so tests should either tolerate high-precision floating-point comparisons or reset precision if they touch other `mpmath` users; also relies on `mpmath`/`numpy` for matrices/determinants.

- `compute/lib/modular_bootstrap_shadow.py` (no `compute/tests/test_modular_bootstrap_shadow.py`; the same audit file flags this gap and notes `test_conformal_bootstrap_mc_engine.py` exercises a different engine).
  - Public API highlights:
    - `kappa_virasoro`, `kappa_affine_km`, `lambda_fp`, `F_g`, `virasoro_shadow_data`, `shadow_planted_forest_genus2` (lines 93‑150).
    - Minimal-model data builders, modular-group verifiers, fusion helpers (`verify_S_squared`, `verlinde_fusion`, etc.).
    - Shadow constraints (`shadow_genus1_constraint`, `shadow_genus2_constraint`, `shadow_gap_bound_*`, `combined_shadow_bootstrap_bound`, etc.) around lines 375‑646.
    - Monster/minimal-model-orbit helpers and WDVV/crossing helpers later on.
  - Candidate smoke tests:
    1. `kappa_virasoro(24)` returns `12` and `kappa_affine_km(1, 2, 3)` matches the dimension-level formula (line 100‑105).
    2. `virasoro_shadow_data(24)` yields `S_4 = 10/(24·142)` and `Delta = 8·kappa·S_4 = 20/71` (lines 123‑140), so test for those rationals.
    3. `shadow_genus1_constraint(kappa)` at `kappa=Rational(1, 4)` yields `1/96`, and `shadow_genus2_constraint` with `S_3=2` produces the expected rational `7/23040 + 79/96` (line 386‑393).
    4. `hellerman_bound(2.0)` equals `2/12 + 0.4736` and `friedan_keller_bound(2.0)` adds `0.1*log(2)/2` (lines 455‑467); compare floats within a small tolerance.
    5. `ising_model_data()` → `S` is symmetric/unitary (`verify_S_symmetry`, `verify_S_unitarity`) and `verify_fusion_integrality(verlinde_fusion(S))` returns `True` (lines 210‑320); this mirrors the modular constraints section.
  - Import/setup quirks: mixes `sympy.Rational` with `numpy` arrays, so tests should stay in exact arithmetic (use `sympy.Rational` for inputs) when checking rational outputs and tolerate small floating-point tolerances when invoking `numpy`-based verifiers.

- `compute/lib/shadow_painleve.py` (no `compute/tests/test_shadow_painleve.py`; audit log stresses “Painleve-shadow assertions” are missing).
  - Public API highlights:
    - Shadow-metric helpers (`shadow_metric_poly`, `shadow_metric_coefficients`, `shadow_metric_discriminant`, `schwarzian_potential_*`) around lines 215‑310.
    - ODE/singularity builders (`classify_singularities`, `singularity_count`, `fuchsian_type`, `painleve_type`, `painleve_type_multichannel`) lines 327‑570.
    - Tau-function, JMU output, hypergeometric connectors, deformation system, matrix-model potenials, etc. (lines 663‑1200+), culminating in high-level summaries (`full_shadow_painleve_analysis`, `shadow_ode_classification_summary`).
  - Candidate smoke tests:
    1. `shadow_metric_coefficients(2, 3, 5)` returns `(16, 72, 91)` and `shadow_metric_discriminant(2, 3, 5)` is `-640`, confirming the quadratic data (lines 240‑254).
    2. `schwarzian_potential_numeric` with those parameters and `t=0` gives `8·kappa²·Delta/q0² = 0.625`, matching the doc’s `8κ²Δ/Q_L²` story (line 288‑304).
    3. `classify_singularities` with `Delta=0` yields a single `'ordinary'` point at infinity and `fuchsian_type` returns `'trivial'` (lines 327‑490), reflecting the “Class G/L → trivial ODE” narrative lines 1‑150.
    4. `painleve_type_multichannel([(1,1,1),(1,2,3)])` returns `'PVI'`, since two nonzero Δ channels produce a genuine Painlevé VI system (lines 555‑595).
    5. `shadow_tau_function_genus_expansion(1)` gives `F_1=1/24`, `F_2=7/5760` and `jmu_tau_from_connection(1,1,0,0)` returns `1` (lines 663‑739), aligning with the documented genus expansion and tau formula.
  - Import/setup quirks: heavy use of `sympy` plus `cmath`/`math` means tests should stay in exact rational contexts when possible; many helpers return complex data structures (`SingularityData`, complex-valued potentials), so tests ought to compare key numeric components rather than entire objects.

Next steps: add dedicated smoke test files under `compute/tests/` that import each module directly, cover the bullet points above, and keep `mpmath`/`sympy` tolerances in mind.
wait(call_ZO5i0VI6RFOCXvAWrq0kWyzw) 1 agents complete:
  019d87a9-3228-7132-8c7d-2c38fdcbec09 completed: "**Missing Shadow Tests**

- `compute/lib/genus1_arithmetic_shadow.py` (no `compute/tests/test_genus1_arithmetic_shadow.p…"

thinking
**Verifying shadow_genus2_constraint**

The explorer has suggested some candidates, but it seems there was an incorrect expected value for the shadow_genus2_constraint at kappa=1/4, perhaps around 79/96, which looks odd. I think the explorer might have misread the formula, so I'll need to verify that myself. I should consider using an update plan as we have all the context and substantial work to draw from. Let’s create a commentary plan with three steps before making any edits.
codex
Plan:
1. Add three new test files, one per missing `shadow` engine, and keep each file limited to smoke coverage on the documented public API.
2. Use independent expected values: direct closed formulas, limiting cases, and known special families (`Heisenberg`, `Virasoro`, `Ising`, `Monster`, `Delta=0`).
3. Run the narrowest pytest slice on just the new files, fix any test-surface issues inside those files only, then report each problem and exact edit.

thinking
**Inspecting formulas and computation methods**

I need to check the exact formulas and look for any mismatches or bugs in the engine or test expectations. I wonder if using Python would be helpful, or maybe a shell with one-liners could work too. I definitely need to verify those formulas. Using the exec command with Python might be a good approach for computing values, though it won't be suitable for file writing. So, let's go with the shell for computation!
codex
I’ve started the verification pass against the actual formulas now. Before I write the files I’m checking the concrete rationals each test will assert, because a few docstrings in this area are inconsistent and I don’t want the new tests to inherit that drift.
exec
/bin/zsh -lc "python - <<'PY'
from sympy import Rational
from compute.lib.modular_bootstrap_shadow import lambda_fp, shadow_genus2_constraint, shadow_planted_forest_genus2, virasoro_shadow_data
print('lambda1', lambda_fp(1))
print('lambda2', lambda_fp(2))
print('monster genus2 delta', shadow_planted_forest_genus2(Rational(12), Rational(2)))
print('monster genus2 total', shadow_genus2_constraint(Rational(12), Rational(2)))
print('vir13', virasoro_shadow_data(Rational(13)))
print('vir24', virasoro_shadow_data(Rational(24)))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "python - <<'PY'
from sympy import Rational
from compute.lib.modular_bootstrap_shadow import ising_model_data, verify_S_squared, verify_S_unitarity, verify_S_symmetry, verlinde_fusion, verify_fusion_integrality
import numpy as np
ising = ising_model_data()
print('c', ising['c'])
print('n', ising['n_primaries'])
print('squared', verify_S_squared(ising['S'])[0])
print('unitarity', verify_S_unitarity(ising['S'])[0])
print('symmetry', verify_S_symmetry(ising['S']))
N = verlinde_fusion(ising['S'])
print('integrality', verify_fusion_integrality(N))
print('N[1,1,:]', N[1,1,:])
print('N[1,2,:]', N[1,2,:])
print('N[2,2,:]', N[2,2,:])
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
import mpmath as mp
from compute.lib.genus1_arithmetic_shadow import HEISENBERG, VIRASORO, BETA_GAMMA
mp.mp.dps = 50
print('H S2', HEISENBERG.S(mp.mpf(2)))
print('expected', mp.zeta(2)*mp.zeta(3))
print('Vir S2', VIRASORO.S(mp.mpf(2)))
print('Vir defect3', VIRASORO.euler_defect(mp.mpf(3)))
print('1-1/zeta3', 1 - 1/mp.zeta(3))
print('Heis sewing', HEISENBERG.sewing_coefficients(3))
print('Xi1', HEISENBERG.Xi(mp.mpf(1)))
print('BG defect2', BETA_GAMMA.euler_defect(mp.mpf(2)))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
from compute.lib.shadow_painleve import (
    shadow_metric_coefficients, shadow_metric_discriminant,
    schwarzian_potential_numeric, schwarzian_potential_verify,
    heisenberg_shadow_params, virasoro_shadow_params,
    classify_singularities, singularity_count, fuchsian_type,
    painleve_type, painleve_type_multichannel,
    shadow_tau_function_genus_expansion, jmu_tau_from_connection,
)
print('coeffs', shadow_metric_coefficients(2,3,5))
print('disc', shadow_metric_discriminant(2,3,5))
print('pot0', schwarzian_potential_numeric(2,3,5,0))
print('verify diff', schwarzian_potential_verify()[2])
print('heis2', heisenberg_shadow_params(2))
print('vir13', virasoro_shadow_params(13))
print('classify delta0', classify_singularities(*heisenberg_shadow_params(2)))
print('count delta0', singularity_count(*heisenberg_shadow_params(2)))
print('fuchs delta0', fuchsian_type(*heisenberg_shadow_params(2)))
print('pain delta0', painleve_type(*heisenberg_shadow_params(2)))
print('pain multi', painleve_type_multichannel([(1,1,1),(1,2,3)]))
print('tau genus', shadow_tau_function_genus_expansion(1, g_max=3))
print('jmu tau at 0', jmu_tau_from_connection(1,1,0,0))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
 exited 127 in 51ms:
zsh:1: command not found: python
 exited 127 in 51ms:
zsh:1: command not found: python
codex
The local shell only has `python3`, not `python`. I’m re-running the formula checks with `python3` and then I’ll write the tests.
exec
/bin/zsh -lc "python3 - <<'PY'
from sympy import Rational
from compute.lib.modular_bootstrap_shadow import lambda_fp, shadow_genus2_constraint, shadow_planted_forest_genus2, virasoro_shadow_data
print('lambda1', lambda_fp(1))
print('lambda2', lambda_fp(2))
print('monster genus2 delta', shadow_planted_forest_genus2(Rational(12), Rational(2)))
print('monster genus2 total', shadow_genus2_constraint(Rational(12), Rational(2)))
print('vir13', virasoro_shadow_data(Rational(13)))
print('vir24', virasoro_shadow_data(Rational(24)))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import mpmath as mp
from compute.lib.genus1_arithmetic_shadow import HEISENBERG, VIRASORO, BETA_GAMMA
mp.mp.dps = 50
print('H S2', HEISENBERG.S(mp.mpf(2)))
print('expected', mp.zeta(2)*mp.zeta(3))
print('Vir S2', VIRASORO.S(mp.mpf(2)))
print('Vir defect3', VIRASORO.euler_defect(mp.mpf(3)))
print('1-1/zeta3', 1 - 1/mp.zeta(3))
print('Heis sewing', HEISENBERG.sewing_coefficients(3))
print('Xi1', HEISENBERG.Xi(mp.mpf(1)))
print('BG defect2', BETA_GAMMA.euler_defect(mp.mpf(2)))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.modular_bootstrap_shadow import ising_model_data, verify_S_squared, verify_S_unitarity, verify_S_symmetry, verlinde_fusion, verify_fusion_integrality
ising = ising_model_data()
print('c', ising['c'])
print('n', ising['n_primaries'])
print('squared', verify_S_squared(ising['S'])[0])
print('unitarity', verify_S_unitarity(ising['S'])[0])
print('symmetry', verify_S_symmetry(ising['S']))
N = verlinde_fusion(ising['S'])
print('integrality', verify_fusion_integrality(N))
print('N[1,1,:]', N[1,1,:])
print('N[1,2,:]', N[1,2,:])
print('N[2,2,:]', N[2,2,:])
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.shadow_painleve import (
    shadow_metric_coefficients, shadow_metric_discriminant,
    schwarzian_potential_numeric, schwarzian_potential_verify,
    heisenberg_shadow_params, virasoro_shadow_params,
    classify_singularities, singularity_count, fuchsian_type,
    painleve_type, painleve_type_multichannel,
    shadow_tau_function_genus_expansion, jmu_tau_from_connection,
)
print('coeffs', shadow_metric_coefficients(2,3,5))
print('disc', shadow_metric_discriminant(2,3,5))
print('pot0', schwarzian_potential_numeric(2,3,5,0))
print('verify diff', schwarzian_potential_verify()[2])
print('heis2', heisenberg_shadow_params(2))
print('vir13', virasoro_shadow_params(13))
print('classify delta0', classify_singularities(*heisenberg_shadow_params(2)))
print('count delta0', singularity_count(*heisenberg_shadow_params(2)))
print('fuchs delta0', fuchsian_type(*heisenberg_shadow_params(2)))
print('pain delta0', painleve_type(*heisenberg_shadow_params(2)))
print('pain multi', painleve_type_multichannel([(1,1,1),(1,2,3)]))
print('tau genus', shadow_tau_function_genus_expansion(1, g_max=3))
print('jmu tau at 0', jmu_tau_from_connection(1,1,0,0))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 273ms:
lambda1 1/24
lambda2 7/5760
monster genus2 delta 1/3
monster genus2 total 167/480
vir13 {'c': 13, 'kappa': 13/2, 'S_3': 2, 'S_4': 10/1131, 'Delta': 40/87, 'shadow_class': 'M'}
vir24 {'c': 24, 'kappa': 12, 'S_3': 2, 'S_4': 5/1704, 'Delta': 20/71, 'shadow_class': 'M'}
 succeeded in 270ms:
c 1/2
n 3
squared True
unitarity True
symmetry True
integrality True
N[1,1,:] [1. 0. 1.]
N[1,2,:] [0. 1. 0.]
N[2,2,:] [ 1.00000000e+00  0.00000000e+00 -1.11022302e-16]
 succeeded in 351ms:
/Users/raeez/chiral-bar-cobar/compute/lib/genus1_arithmetic_shadow.py:9: SyntaxWarning: "\R" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\R"? A raw string is also an option.
  Koszul duality/             \Rankin-Selberg
H S2 1.9773043502972961181970854414851255720821514666601
expected 1.9773043502972961181970854414851255720821514666601
Vir S2 0.77524744713770183279734727997367558131716517431964
Vir defect3 0.16809262741929253131687372117846926558294360226627
1-1/zeta3 0.16809262741929253131687372117846926558294360226627
Heis sewing [mpf('1.0'), mpf('1.5'), mpf('1.3333333333333333333333333333333333333333333333333324')]
Xi1 1.6449340668482264364724151666460251892189499012068
BG defect2 1.0
 succeeded in 451ms:
coeffs (16, 72, 91)
disc -640
pot0 0.625
verify diff (8*Delta*kappa**2 - (2*Delta + 9*alpha**2)*(2*Delta*t**2 + (3*alpha*t + 2*kappa)**2) + 3*(2*Delta*t + 3*alpha*(3*alpha*t + 2*kappa))**2)/(2*Delta*t**2 + (3*alpha*t + 2*kappa)**2)**2
heis2 (1.0, 0.0, 0.0)
vir13 (6.5, 2.0, 0.45977011494252873)
classify delta0 [SingularityData(location=(inf+0j), type='ordinary', rank=0, indicial_exponents=(0, 1), is_finite=False)]
count delta0 {'regular': 0, 'irregular': 0, 'ordinary': 1, 'apparent': 0}
fuchs delta0 trivial
pain delta0 trivial
pain multi PVI
tau genus {1: 1/12, 2: 1/240, 3: 1/6048}
jmu tau at 0 1.0



thinking
**Evaluating testing scope**

I noticed an issue with the shadow_tau_function_genus_expansion where F_1 equals 1/12 instead of 1/24, indicating a discrepancy in the formula that seems to be a bug. The user requested a basic test file that imports the engine and runs at least three smoke tests with verified expected values. I realize we’re limited to editing only assigned files, which seem to involve creating missing tests rather than editing the engine directly. Testing with wrong engine outputs could lead to failure, but it’s a situation we need to discuss further.
thinking
**Deciding on test approach**

I’m considering how to find tests that pass while using verified expected values. If there's a bug in the engine, we might not want to include that broken function in the smoke tests, especially since there are other passing functions available. The user has requested that I function both as an auditor and a fixer. It seems the main goal is to create the missing test files rather than auditing the engine and potentially discovering more bugs. I’ll need to ensure we only choose passing tests and consider simplifying some expressions, like for `schwarzian_potential_verify`, to determine if they lead to zero differences.
thinking
**Exploring symbolic identity**

I'm thinking about how I might demonstrate symbolic identity by simplifying after substitution. I could use sympy.simplify on the differentiation expression, which isn't zero yet. If the results show a discrepancy, it could hint at a bug in the engine function. Maybe I should compute the final result separately to see if it simplifies to zero when factored. I’ll quickly check both the manual simplification and the factoring options in sympy to confirm the behavior.
codex
One engine surfaced a real defect during verification: `shadow_tau_function_genus_expansion(1)` currently returns `F_1 = 1/12`, not the canonical `1/24`. Because the task scope is the missing test files only, I’m keeping the new tests on stable APIs that already match the verified formulas and I’ll call out that out-of-scope bug explicitly at the end.
exec
/bin/zsh -lc "python3 - <<'PY'
from sympy import simplify, factor
from compute.lib.shadow_painleve import schwarzian_potential_verify
expr = schwarzian_potential_verify()[2]
print('simplify', simplify(expr))
print('factor', factor(expr))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.modular_bootstrap_shadow import minimal_model_shadow_check
print(minimal_model_shadow_check(4,3))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.modular_bootstrap_shadow import hellerman_bound, friedan_keller_bound, shadow_gap_bound_genus1, shadow_gap_bound_genus2, combined_shadow_bootstrap_bound
for c in [0.5, 2.0, 24.0]:
    print(c, hellerman_bound(c), friedan_keller_bound(c), shadow_gap_bound_genus1(c), shadow_gap_bound_genus2(c), combined_shadow_bootstrap_bound(c))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 352ms:
{'model': 'M(4,3)', 'c': 1/2, 'c_float': 0.5, 'kappa': 1/4, 'n_primaries': 3, 'S_squared_ok': True, 'ST_cubed_ok': True, 'S_unitary_ok': True, 'fusion_integer_ok': np.True_, 'F_1': 1/96, 'actual_gap': 0.0625, 'shadow_data': {'c': 1/2, 'kappa': 1/4, 'S_3': 2, 'S_4': 40/49, 'Delta': 80/49, 'shadow_class': 'M'}}
 succeeded in 353ms:
0.5 inf inf 0.041666666666666664 270.8988095238095 {'c': 0.5, 'hellerman': inf, 'shadow_genus1': 0.041666666666666664, 'shadow_genus2': 270.8988095238095, 'actual_gap': 0.0625}
2.0 0.6402666666666667 0.6749240256946639 -0.33333333333333337 64.80952380952381 {'c': 2.0, 'hellerman': 0.6402666666666667, 'shadow_genus1': -0.33333333333333337, 'shadow_genus2': 64.80952380952381}
24.0 2.4736000000000002 2.4868418909597834 1.5 3.7857142857142856 {'c': 24.0, 'hellerman': 2.4736000000000002, 'shadow_genus1': 1.5, 'shadow_genus2': 3.7857142857142856, 'actual_gap': 2.0}
 succeeded in 582ms:
simplify (8*Delta*kappa**2 - (2*Delta + 9*alpha**2)*(2*Delta*t**2 + (3*alpha*t + 2*kappa)**2) + 3*(2*Delta*t + 3*alpha*(3*alpha*t + 2*kappa))**2)/(2*Delta*t**2 + (3*alpha*t + 2*kappa)**2)**2
factor 2*(2*Delta*t + 9*alpha**2*t + 6*alpha*kappa)**2/(2*Delta*t**2 + 9*alpha**2*t**2 + 12*alpha*kappa*t + 4*kappa**2)**2

thinking
**Assessing a potential issue**

I see the potential issue where jmu_tau_from_connection with Delta 0 and t 0 returns 1.0, which is interesting. There’s no heavy numerical integration needed but I need to create files using apply_patch. Before I dive into editing those, I should ensure to update the commentary to explain what I'm planning to change. It’s important to have that context for anyone reviewing this later! Let’s keep things organized as I go through this process.
codex
I’ve finished the pre-edit verification and I’m writing only the three missing test files now. The assertions are staying on stable functions that already match the verified formulas; I’m avoiding the out-of-scope broken helpers so the new smoke suite is truthful rather than ornamental.
file update
A /Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py
import pytest

from compute.lib.shadow_painleve import (
    classify_singularities,
    fuchsian_type,
    heisenberg_shadow_params,
    jmu_tau_from_connection,
    painleve_type,
    painleve_type_multichannel,
    schwarzian_potential_numeric,
    shadow_metric_coefficients,
    shadow_metric_discriminant,
    singularity_count,
    virasoro_shadow_params,
)


def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
    kappa, alpha, delta = 2, 3, 5
    expected_coeffs = (16, 72, 91)
    expected_discriminant = -640
    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant


def test_schwarzian_potential_numeric_matches_origin_value():
    value = schwarzian_potential_numeric(2, 3, 5, 0)
    expected = 5.0 / 8.0
    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
    assert value == pytest.approx(expected)


def test_delta_zero_classification_is_trivial():
    params = heisenberg_shadow_params(2)
    singularities = classify_singularities(*params)
    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
    assert singularities[0].type == "ordinary"
    assert not singularities[0].is_finite
    assert singularity_count(*params) == {
        "regular": 0,
        "irregular": 0,
        "ordinary": 1,
        "apparent": 0,
    }
    assert fuchsian_type(*params) == "trivial"
    assert painleve_type(*params) == "trivial"


def test_virasoro_shadow_params_match_self_dual_c13_values():
    kappa, alpha, delta = virasoro_shadow_params(13)
    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
    assert kappa == pytest.approx(6.5)
    assert alpha == pytest.approx(2.0)
    assert delta == pytest.approx(40.0 / 87.0)


def test_multichannel_and_tau_normalization_smoke_checks():
    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)
A /Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py
import mpmath as mp

from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO


mp.mp.dps = 50


def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
    u = mp.mpf(2)
    expected = mp.zeta(u) * mp.zeta(u + 1)
    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")


def test_virasoro_defect_matches_one_minus_inverse_zeta():
    u = mp.mpf(3)
    expected = 1 - 1 / mp.zeta(u)
    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
    assert not VIRASORO.is_euler_koszul()


def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
    assert HEISENBERG.sewing_coefficients(3) == expected


def test_xi_regularization_and_beta_gamma_exactness():
    expected_xi = mp.zeta(2)
    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
    assert BETA_GAMMA.is_euler_koszul()
    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
A /Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py
import pytest
from sympy import Rational

from compute.lib.modular_bootstrap_shadow import (
    ising_model_data,
    lambda_fp,
    minimal_model_shadow_check,
    shadow_genus2_constraint,
    shadow_planted_forest_genus2,
    verify_S_squared,
    verify_S_symmetry,
    verify_S_unitarity,
    verlinde_fusion,
    verify_fusion_integrality,
    virasoro_shadow_data,
)


def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
    expected_lambda1 = Rational(1, 24)
    expected_lambda2 = Rational(7, 5760)
    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
    assert lambda_fp(1) == expected_lambda1
    assert lambda_fp(2) == expected_lambda2


def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
    vir13 = virasoro_shadow_data(Rational(13))
    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
    assert vir13["kappa"] == Rational(13, 2)
    assert vir13["S_4"] == Rational(10, 1131)
    assert vir13["Delta"] == Rational(40, 87)

    vir24 = virasoro_shadow_data(Rational(24))
    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
    assert vir24["kappa"] == Rational(12)
    assert vir24["S_4"] == Rational(5, 1704)
    assert vir24["Delta"] == Rational(20, 71)


def test_monster_genus2_constraint_matches_planted_forest_formula():
    kappa = Rational(12)
    cubic = Rational(2)
    expected_delta_pf = Rational(1, 3)
    expected_genus2 = Rational(167, 480)
    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2


def test_ising_modular_data_and_shadow_check_match_known_values():
    ising = ising_model_data()
    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
    assert ising["c"] == Rational(1, 2)
    assert ising["n_primaries"] == 3
    assert verify_S_squared(ising["S"])[0]
    assert verify_S_unitarity(ising["S"])[0]
    assert verify_S_symmetry(ising["S"])

    fusion = verlinde_fusion(ising["S"])
    assert verify_fusion_integrality(fusion)
    assert fusion[1, 1, 0] == pytest.approx(1.0)
    assert fusion[1, 1, 2] == pytest.approx(1.0)
    assert fusion[1, 2, 1] == pytest.approx(1.0)

    check = minimal_model_shadow_check(4, 3)
    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
    assert check["F_1"] == Rational(1, 96)
    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
apply_patch(auto_approved=true) exited 0 in 28ms:
Success. Updated the following files:
A compute/tests/test_genus1_arithmetic_shadow.py
A compute/tests/test_modular_bootstrap_shadow.py
A compute/tests/test_shadow_painleve.py
file update:
diff --git a/compute/tests/test_genus1_arithmetic_shadow.py b/compute/tests/test_genus1_arithmetic_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..4a03855a21aa5e50be839923ca5978055f9831b8
--- /dev/null
+++ b/compute/tests/test_genus1_arithmetic_shadow.py
@@ -0,0 +1,36 @@
+import mpmath as mp
+
+from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO
+
+
+mp.mp.dps = 50
+
+
+def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
+    u = mp.mpf(2)
+    expected = mp.zeta(u) * mp.zeta(u + 1)
+    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
+    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
+    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")
+
+
+def test_virasoro_defect_matches_one_minus_inverse_zeta():
+    u = mp.mpf(3)
+    expected = 1 - 1 / mp.zeta(u)
+    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
+    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
+    assert not VIRASORO.is_euler_koszul()
+
+
+def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
+    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
+    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
+    assert HEISENBERG.sewing_coefficients(3) == expected
+
+
+def test_xi_regularization_and_beta_gamma_exactness():
+    expected_xi = mp.zeta(2)
+    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
+    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
+    assert BETA_GAMMA.is_euler_koszul()
+    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
diff --git a/compute/tests/test_modular_bootstrap_shadow.py b/compute/tests/test_modular_bootstrap_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..e38f589d171d11e507394bdc2a34d5dc37fbef10
--- /dev/null
+++ b/compute/tests/test_modular_bootstrap_shadow.py
@@ -0,0 +1,69 @@
+import pytest
+from sympy import Rational
+
+from compute.lib.modular_bootstrap_shadow import (
+    ising_model_data,
+    lambda_fp,
+    minimal_model_shadow_check,
+    shadow_genus2_constraint,
+    shadow_planted_forest_genus2,
+    verify_S_squared,
+    verify_S_symmetry,
+    verify_S_unitarity,
+    verlinde_fusion,
+    verify_fusion_integrality,
+    virasoro_shadow_data,
+)
+
+
+def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
+    expected_lambda1 = Rational(1, 24)
+    expected_lambda2 = Rational(7, 5760)
+    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
+    assert lambda_fp(1) == expected_lambda1
+    assert lambda_fp(2) == expected_lambda2
+
+
+def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
+    vir13 = virasoro_shadow_data(Rational(13))
+    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
+    assert vir13["kappa"] == Rational(13, 2)
+    assert vir13["S_4"] == Rational(10, 1131)
+    assert vir13["Delta"] == Rational(40, 87)
+
+    vir24 = virasoro_shadow_data(Rational(24))
+    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
+    assert vir24["kappa"] == Rational(12)
+    assert vir24["S_4"] == Rational(5, 1704)
+    assert vir24["Delta"] == Rational(20, 71)
+
+
+def test_monster_genus2_constraint_matches_planted_forest_formula():
+    kappa = Rational(12)
+    cubic = Rational(2)
+    expected_delta_pf = Rational(1, 3)
+    expected_genus2 = Rational(167, 480)
+    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
+    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
+    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2
+
+
+def test_ising_modular_data_and_shadow_check_match_known_values():
+    ising = ising_model_data()
+    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
+    assert ising["c"] == Rational(1, 2)
+    assert ising["n_primaries"] == 3
+    assert verify_S_squared(ising["S"])[0]
+    assert verify_S_unitarity(ising["S"])[0]
+    assert verify_S_symmetry(ising["S"])
+
+    fusion = verlinde_fusion(ising["S"])
+    assert verify_fusion_integrality(fusion)
+    assert fusion[1, 1, 0] == pytest.approx(1.0)
+    assert fusion[1, 1, 2] == pytest.approx(1.0)
+    assert fusion[1, 2, 1] == pytest.approx(1.0)
+
+    check = minimal_model_shadow_check(4, 3)
+    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
+    assert check["F_1"] == Rational(1, 96)
+    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
diff --git a/compute/tests/test_shadow_painleve.py b/compute/tests/test_shadow_painleve.py
new file mode 100644
index 0000000000000000000000000000000000000000..0a5e6be2c86d55fd1deaca7b9d18fd588bf85243
--- /dev/null
+++ b/compute/tests/test_shadow_painleve.py
@@ -0,0 +1,61 @@
+import pytest
+
+from compute.lib.shadow_painleve import (
+    classify_singularities,
+    fuchsian_type,
+    heisenberg_shadow_params,
+    jmu_tau_from_connection,
+    painleve_type,
+    painleve_type_multichannel,
+    schwarzian_potential_numeric,
+    shadow_metric_coefficients,
+    shadow_metric_discriminant,
+    singularity_count,
+    virasoro_shadow_params,
+)
+
+
+def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
+    kappa, alpha, delta = 2, 3, 5
+    expected_coeffs = (16, 72, 91)
+    expected_discriminant = -640
+    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
+    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
+    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant
+
+
+def test_schwarzian_potential_numeric_matches_origin_value():
+    value = schwarzian_potential_numeric(2, 3, 5, 0)
+    expected = 5.0 / 8.0
+    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
+    assert value == pytest.approx(expected)
+
+
+def test_delta_zero_classification_is_trivial():
+    params = heisenberg_shadow_params(2)
+    singularities = classify_singularities(*params)
+    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
+    assert singularities[0].type == "ordinary"
+    assert not singularities[0].is_finite
+    assert singularity_count(*params) == {
+        "regular": 0,
+        "irregular": 0,
+        "ordinary": 1,
+        "apparent": 0,
+    }
+    assert fuchsian_type(*params) == "trivial"
+    assert painleve_type(*params) == "trivial"
+
+
+def test_virasoro_shadow_params_match_self_dual_c13_values():
+    kappa, alpha, delta = virasoro_shadow_params(13)
+    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
+    assert kappa == pytest.approx(6.5)
+    assert alpha == pytest.approx(2.0)
+    assert delta == pytest.approx(40.0 / 87.0)
+
+
+def test_multichannel_and_tau_normalization_smoke_checks():
+    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
+    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
+    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)

file update:
diff --git a/compute/tests/test_genus1_arithmetic_shadow.py b/compute/tests/test_genus1_arithmetic_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..4a03855a21aa5e50be839923ca5978055f9831b8
--- /dev/null
+++ b/compute/tests/test_genus1_arithmetic_shadow.py
@@ -0,0 +1,36 @@
+import mpmath as mp
+
+from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO
+
+
+mp.mp.dps = 50
+
+
+def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
+    u = mp.mpf(2)
+    expected = mp.zeta(u) * mp.zeta(u + 1)
+    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
+    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
+    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")
+
+
+def test_virasoro_defect_matches_one_minus_inverse_zeta():
+    u = mp.mpf(3)
+    expected = 1 - 1 / mp.zeta(u)
+    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
+    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
+    assert not VIRASORO.is_euler_koszul()
+
+
+def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
+    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
+    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
+    assert HEISENBERG.sewing_coefficients(3) == expected
+
+
+def test_xi_regularization_and_beta_gamma_exactness():
+    expected_xi = mp.zeta(2)
+    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
+    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
+    assert BETA_GAMMA.is_euler_koszul()
+    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
diff --git a/compute/tests/test_modular_bootstrap_shadow.py b/compute/tests/test_modular_bootstrap_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..e38f589d171d11e507394bdc2a34d5dc37fbef10
--- /dev/null
+++ b/compute/tests/test_modular_bootstrap_shadow.py
@@ -0,0 +1,69 @@
+import pytest
+from sympy import Rational
+
+from compute.lib.modular_bootstrap_shadow import (
+    ising_model_data,
+    lambda_fp,
+    minimal_model_shadow_check,
+    shadow_genus2_constraint,
+    shadow_planted_forest_genus2,
+    verify_S_squared,
+    verify_S_symmetry,
+    verify_S_unitarity,
+    verlinde_fusion,
+    verify_fusion_integrality,
+    virasoro_shadow_data,
+)
+
+
+def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
+    expected_lambda1 = Rational(1, 24)
+    expected_lambda2 = Rational(7, 5760)
+    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
+    assert lambda_fp(1) == expected_lambda1
+    assert lambda_fp(2) == expected_lambda2
+
+
+def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
+    vir13 = virasoro_shadow_data(Rational(13))
+    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
+    assert vir13["kappa"] == Rational(13, 2)
+    assert vir13["S_4"] == Rational(10, 1131)
+    assert vir13["Delta"] == Rational(40, 87)
+
+    vir24 = virasoro_shadow_data(Rational(24))
+    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
+    assert vir24["kappa"] == Rational(12)
+    assert vir24["S_4"] == Rational(5, 1704)
+    assert vir24["Delta"] == Rational(20, 71)
+
+
+def test_monster_genus2_constraint_matches_planted_forest_formula():
+    kappa = Rational(12)
+    cubic = Rational(2)
+    expected_delta_pf = Rational(1, 3)
+    expected_genus2 = Rational(167, 480)
+    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
+    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
+    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2
+
+
+def test_ising_modular_data_and_shadow_check_match_known_values():
+    ising = ising_model_data()
+    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
+    assert ising["c"] == Rational(1, 2)
+    assert ising["n_primaries"] == 3
+    assert verify_S_squared(ising["S"])[0]
+    assert verify_S_unitarity(ising["S"])[0]
+    assert verify_S_symmetry(ising["S"])
+
+    fusion = verlinde_fusion(ising["S"])
+    assert verify_fusion_integrality(fusion)
+    assert fusion[1, 1, 0] == pytest.approx(1.0)
+    assert fusion[1, 1, 2] == pytest.approx(1.0)
+    assert fusion[1, 2, 1] == pytest.approx(1.0)
+
+    check = minimal_model_shadow_check(4, 3)
+    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
+    assert check["F_1"] == Rational(1, 96)
+    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
diff --git a/compute/tests/test_shadow_painleve.py b/compute/tests/test_shadow_painleve.py
new file mode 100644
index 0000000000000000000000000000000000000000..0a5e6be2c86d55fd1deaca7b9d18fd588bf85243
--- /dev/null
+++ b/compute/tests/test_shadow_painleve.py
@@ -0,0 +1,61 @@
+import pytest
+
+from compute.lib.shadow_painleve import (
+    classify_singularities,
+    fuchsian_type,
+    heisenberg_shadow_params,
+    jmu_tau_from_connection,
+    painleve_type,
+    painleve_type_multichannel,
+    schwarzian_potential_numeric,
+    shadow_metric_coefficients,
+    shadow_metric_discriminant,
+    singularity_count,
+    virasoro_shadow_params,
+)
+
+
+def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
+    kappa, alpha, delta = 2, 3, 5
+    expected_coeffs = (16, 72, 91)
+    expected_discriminant = -640
+    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
+    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
+    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant
+
+
+def test_schwarzian_potential_numeric_matches_origin_value():
+    value = schwarzian_potential_numeric(2, 3, 5, 0)
+    expected = 5.0 / 8.0
+    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
+    assert value == pytest.approx(expected)
+
+
+def test_delta_zero_classification_is_trivial():
+    params = heisenberg_shadow_params(2)
+    singularities = classify_singularities(*params)
+    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
+    assert singularities[0].type == "ordinary"
+    assert not singularities[0].is_finite
+    assert singularity_count(*params) == {
+        "regular": 0,
+        "irregular": 0,
+        "ordinary": 1,
+        "apparent": 0,
+    }
+    assert fuchsian_type(*params) == "trivial"
+    assert painleve_type(*params) == "trivial"
+
+
+def test_virasoro_shadow_params_match_self_dual_c13_values():
+    kappa, alpha, delta = virasoro_shadow_params(13)
+    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
+    assert kappa == pytest.approx(6.5)
+    assert alpha == pytest.approx(2.0)
+    assert delta == pytest.approx(40.0 / 87.0)
+
+
+def test_multichannel_and_tau_normalization_smoke_checks():
+    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
+    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
+    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)


thinking
**Running pytest for new files**

I need to run pytest on some new files. I’m wondering if there might be issues with imports or if something’s failing due to a broken package path or functions. Should I have some commentary ready before I dive into the substantial work? Maybe I’ve already covered some of this. It seems important to run the narrowest pytest I can manage first. I plan to use exec_command for this!
codex
The three missing test files are in place. I’m running only those new pytest slices now to catch any API mismatches and keep the follow-up edits, if any, inside the new files.
exec
/bin/zsh -lc 'pytest compute/tests/test_genus1_arithmetic_shadow.py compute/tests/test_modular_bootstrap_shadow.py compute/tests/test_shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 752ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 13 items

compute/tests/test_genus1_arithmetic_shadow.py ....                      [ 30%]
compute/tests/test_modular_bootstrap_shadow.py ....                      [ 61%]
compute/tests/test_shadow_painleve.py .....                              [100%]

============================== 13 passed in 0.54s ==============================
file update:
diff --git a/compute/tests/test_genus1_arithmetic_shadow.py b/compute/tests/test_genus1_arithmetic_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..4a03855a21aa5e50be839923ca5978055f9831b8
--- /dev/null
+++ b/compute/tests/test_genus1_arithmetic_shadow.py
@@ -0,0 +1,36 @@
+import mpmath as mp
+
+from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO
+
+
+mp.mp.dps = 50
+
+
+def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
+    u = mp.mpf(2)
+    expected = mp.zeta(u) * mp.zeta(u + 1)
+    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
+    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
+    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")
+
+
+def test_virasoro_defect_matches_one_minus_inverse_zeta():
+    u = mp.mpf(3)
+    expected = 1 - 1 / mp.zeta(u)
+    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
+    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
+    assert not VIRASORO.is_euler_koszul()
+
+
+def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
+    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
+    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
+    assert HEISENBERG.sewing_coefficients(3) == expected
+
+
+def test_xi_regularization_and_beta_gamma_exactness():
+    expected_xi = mp.zeta(2)
+    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
+    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
+    assert BETA_GAMMA.is_euler_koszul()
+    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
diff --git a/compute/tests/test_modular_bootstrap_shadow.py b/compute/tests/test_modular_bootstrap_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..e38f589d171d11e507394bdc2a34d5dc37fbef10
--- /dev/null
+++ b/compute/tests/test_modular_bootstrap_shadow.py
@@ -0,0 +1,69 @@
+import pytest
+from sympy import Rational
+
+from compute.lib.modular_bootstrap_shadow import (
+    ising_model_data,
+    lambda_fp,
+    minimal_model_shadow_check,
+    shadow_genus2_constraint,
+    shadow_planted_forest_genus2,
+    verify_S_squared,
+    verify_S_symmetry,
+    verify_S_unitarity,
+    verlinde_fusion,
+    verify_fusion_integrality,
+    virasoro_shadow_data,
+)
+
+
+def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
+    expected_lambda1 = Rational(1, 24)
+    expected_lambda2 = Rational(7, 5760)
+    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
+    assert lambda_fp(1) == expected_lambda1
+    assert lambda_fp(2) == expected_lambda2
+
+
+def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
+    vir13 = virasoro_shadow_data(Rational(13))
+    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
+    assert vir13["kappa"] == Rational(13, 2)
+    assert vir13["S_4"] == Rational(10, 1131)
+    assert vir13["Delta"] == Rational(40, 87)
+
+    vir24 = virasoro_shadow_data(Rational(24))
+    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
+    assert vir24["kappa"] == Rational(12)
+    assert vir24["S_4"] == Rational(5, 1704)
+    assert vir24["Delta"] == Rational(20, 71)
+
+
+def test_monster_genus2_constraint_matches_planted_forest_formula():
+    kappa = Rational(12)
+    cubic = Rational(2)
+    expected_delta_pf = Rational(1, 3)
+    expected_genus2 = Rational(167, 480)
+    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
+    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
+    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2
+
+
+def test_ising_modular_data_and_shadow_check_match_known_values():
+    ising = ising_model_data()
+    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
+    assert ising["c"] == Rational(1, 2)
+    assert ising["n_primaries"] == 3
+    assert verify_S_squared(ising["S"])[0]
+    assert verify_S_unitarity(ising["S"])[0]
+    assert verify_S_symmetry(ising["S"])
+
+    fusion = verlinde_fusion(ising["S"])
+    assert verify_fusion_integrality(fusion)
+    assert fusion[1, 1, 0] == pytest.approx(1.0)
+    assert fusion[1, 1, 2] == pytest.approx(1.0)
+    assert fusion[1, 2, 1] == pytest.approx(1.0)
+
+    check = minimal_model_shadow_check(4, 3)
+    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
+    assert check["F_1"] == Rational(1, 96)
+    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
diff --git a/compute/tests/test_shadow_painleve.py b/compute/tests/test_shadow_painleve.py
new file mode 100644
index 0000000000000000000000000000000000000000..0a5e6be2c86d55fd1deaca7b9d18fd588bf85243
--- /dev/null
+++ b/compute/tests/test_shadow_painleve.py
@@ -0,0 +1,61 @@
+import pytest
+
+from compute.lib.shadow_painleve import (
+    classify_singularities,
+    fuchsian_type,
+    heisenberg_shadow_params,
+    jmu_tau_from_connection,
+    painleve_type,
+    painleve_type_multichannel,
+    schwarzian_potential_numeric,
+    shadow_metric_coefficients,
+    shadow_metric_discriminant,
+    singularity_count,
+    virasoro_shadow_params,
+)
+
+
+def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
+    kappa, alpha, delta = 2, 3, 5
+    expected_coeffs = (16, 72, 91)
+    expected_discriminant = -640
+    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
+    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
+    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant
+
+
+def test_schwarzian_potential_numeric_matches_origin_value():
+    value = schwarzian_potential_numeric(2, 3, 5, 0)
+    expected = 5.0 / 8.0
+    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
+    assert value == pytest.approx(expected)
+
+
+def test_delta_zero_classification_is_trivial():
+    params = heisenberg_shadow_params(2)
+    singularities = classify_singularities(*params)
+    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
+    assert singularities[0].type == "ordinary"
+    assert not singularities[0].is_finite
+    assert singularity_count(*params) == {
+        "regular": 0,
+        "irregular": 0,
+        "ordinary": 1,
+        "apparent": 0,
+    }
+    assert fuchsian_type(*params) == "trivial"
+    assert painleve_type(*params) == "trivial"
+
+
+def test_virasoro_shadow_params_match_self_dual_c13_values():
+    kappa, alpha, delta = virasoro_shadow_params(13)
+    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
+    assert kappa == pytest.approx(6.5)
+    assert alpha == pytest.approx(2.0)
+    assert delta == pytest.approx(40.0 / 87.0)
+
+
+def test_multichannel_and_tau_normalization_smoke_checks():
+    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
+    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
+    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)


thinking
**Checking test coverage**

I need to run a command to identify any missing tests. It seems like I might not be getting any output from the original command, so I should verify that first. Checking the git diff might be a good idea too, focusing only on the files that were assigned and changed. Maybe I'll run that original command again just to be sure it works as intended.
codex
The new slice passed cleanly: all 13 tests in the three added files are green. I’m doing one last scope check against the original missing-test query and then I’ll summarize the exact problems and edits.
exec
/bin/zsh -lc 'git diff -- compute/tests/test_genus1_arithmetic_shadow.py compute/tests/test_modular_bootstrap_shadow.py compute/tests/test_shadow_painleve.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc 'ls compute/lib/*shadow*.py | while read f; do test=compute/tests/test_$(basename "$f"); [ ! -f "$test" ] && echo "MISSING: $test"; done' in /Users/raeez/chiral-bar-cobar exited 1 in 645ms:

file update:
diff --git a/compute/tests/test_genus1_arithmetic_shadow.py b/compute/tests/test_genus1_arithmetic_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..4a03855a21aa5e50be839923ca5978055f9831b8
--- /dev/null
+++ b/compute/tests/test_genus1_arithmetic_shadow.py
@@ -0,0 +1,36 @@
+import mpmath as mp
+
+from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO
+
+
+mp.mp.dps = 50
+
+
+def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
+    u = mp.mpf(2)
+    expected = mp.zeta(u) * mp.zeta(u + 1)
+    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
+    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
+    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")
+
+
+def test_virasoro_defect_matches_one_minus_inverse_zeta():
+    u = mp.mpf(3)
+    expected = 1 - 1 / mp.zeta(u)
+    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
+    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
+    assert not VIRASORO.is_euler_koszul()
+
+
+def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
+    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
+    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
+    assert HEISENBERG.sewing_coefficients(3) == expected
+
+
+def test_xi_regularization_and_beta_gamma_exactness():
+    expected_xi = mp.zeta(2)
+    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
+    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
+    assert BETA_GAMMA.is_euler_koszul()
+    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
diff --git a/compute/tests/test_modular_bootstrap_shadow.py b/compute/tests/test_modular_bootstrap_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..e38f589d171d11e507394bdc2a34d5dc37fbef10
--- /dev/null
+++ b/compute/tests/test_modular_bootstrap_shadow.py
@@ -0,0 +1,69 @@
+import pytest
+from sympy import Rational
+
+from compute.lib.modular_bootstrap_shadow import (
+    ising_model_data,
+    lambda_fp,
+    minimal_model_shadow_check,
+    shadow_genus2_constraint,
+    shadow_planted_forest_genus2,
+    verify_S_squared,
+    verify_S_symmetry,
+    verify_S_unitarity,
+    verlinde_fusion,
+    verify_fusion_integrality,
+    virasoro_shadow_data,
+)
+
+
+def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
+    expected_lambda1 = Rational(1, 24)
+    expected_lambda2 = Rational(7, 5760)
+    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
+    assert lambda_fp(1) == expected_lambda1
+    assert lambda_fp(2) == expected_lambda2
+
+
+def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
+    vir13 = virasoro_shadow_data(Rational(13))
+    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
+    assert vir13["kappa"] == Rational(13, 2)
+    assert vir13["S_4"] == Rational(10, 1131)
+    assert vir13["Delta"] == Rational(40, 87)
+
+    vir24 = virasoro_shadow_data(Rational(24))
+    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
+    assert vir24["kappa"] == Rational(12)
+    assert vir24["S_4"] == Rational(5, 1704)
+    assert vir24["Delta"] == Rational(20, 71)
+
+
+def test_monster_genus2_constraint_matches_planted_forest_formula():
+    kappa = Rational(12)
+    cubic = Rational(2)
+    expected_delta_pf = Rational(1, 3)
+    expected_genus2 = Rational(167, 480)
+    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
+    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
+    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2
+
+
+def test_ising_modular_data_and_shadow_check_match_known_values():
+    ising = ising_model_data()
+    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
+    assert ising["c"] == Rational(1, 2)
+    assert ising["n_primaries"] == 3
+    assert verify_S_squared(ising["S"])[0]
+    assert verify_S_unitarity(ising["S"])[0]
+    assert verify_S_symmetry(ising["S"])
+
+    fusion = verlinde_fusion(ising["S"])
+    assert verify_fusion_integrality(fusion)
+    assert fusion[1, 1, 0] == pytest.approx(1.0)
+    assert fusion[1, 1, 2] == pytest.approx(1.0)
+    assert fusion[1, 2, 1] == pytest.approx(1.0)
+
+    check = minimal_model_shadow_check(4, 3)
+    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
+    assert check["F_1"] == Rational(1, 96)
+    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
diff --git a/compute/tests/test_shadow_painleve.py b/compute/tests/test_shadow_painleve.py
new file mode 100644
index 0000000000000000000000000000000000000000..0a5e6be2c86d55fd1deaca7b9d18fd588bf85243
--- /dev/null
+++ b/compute/tests/test_shadow_painleve.py
@@ -0,0 +1,61 @@
+import pytest
+
+from compute.lib.shadow_painleve import (
+    classify_singularities,
+    fuchsian_type,
+    heisenberg_shadow_params,
+    jmu_tau_from_connection,
+    painleve_type,
+    painleve_type_multichannel,
+    schwarzian_potential_numeric,
+    shadow_metric_coefficients,
+    shadow_metric_discriminant,
+    singularity_count,
+    virasoro_shadow_params,
+)
+
+
+def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
+    kappa, alpha, delta = 2, 3, 5
+    expected_coeffs = (16, 72, 91)
+    expected_discriminant = -640
+    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
+    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
+    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant
+
+
+def test_schwarzian_potential_numeric_matches_origin_value():
+    value = schwarzian_potential_numeric(2, 3, 5, 0)
+    expected = 5.0 / 8.0
+    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
+    assert value == pytest.approx(expected)
+
+
+def test_delta_zero_classification_is_trivial():
+    params = heisenberg_shadow_params(2)
+    singularities = classify_singularities(*params)
+    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
+    assert singularities[0].type == "ordinary"
+    assert not singularities[0].is_finite
+    assert singularity_count(*params) == {
+        "regular": 0,
+        "irregular": 0,
+        "ordinary": 1,
+        "apparent": 0,
+    }
+    assert fuchsian_type(*params) == "trivial"
+    assert painleve_type(*params) == "trivial"
+
+
+def test_virasoro_shadow_params_match_self_dual_c13_values():
+    kappa, alpha, delta = virasoro_shadow_params(13)
+    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
+    assert kappa == pytest.approx(6.5)
+    assert alpha == pytest.approx(2.0)
+    assert delta == pytest.approx(40.0 / 87.0)
+
+
+def test_multichannel_and_tau_normalization_smoke_checks():
+    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
+    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
+    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)


thinking
**Clarifying git diff usage**

I’m thinking about why the output is empty; it might be because untracked files aren't showing without using --no-index. Actually, I recall that git diff doesn’t show untracked files. I should check with git status or ls -l instead. I know what changed, and I might need line numbers. To get those, I can use nl -ba. Ultimately, I want a final report in the format: PROBLEM at file:line, then the exact edit applied. Line numbers will be crucial for the new files!
codex
I’ve confirmed the original gap finder is now silent, so the missing-test surface is closed. I’m grabbing exact line numbers from the three new files for the final audit-style report.
exec
/bin/zsh -lc 'nl -ba compute/tests/test_modular_bootstrap_shadow.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'nl -ba compute/tests/test_shadow_painleve.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'nl -ba compute/tests/test_genus1_arithmetic_shadow.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	import pytest
     2	
     3	from compute.lib.shadow_painleve import (
     4	    classify_singularities,
     5	    fuchsian_type,
     6	    heisenberg_shadow_params,
     7	    jmu_tau_from_connection,
     8	    painleve_type,
     9	    painleve_type_multichannel,
    10	    schwarzian_potential_numeric,
    11	    shadow_metric_coefficients,
    12	    shadow_metric_discriminant,
    13	    singularity_count,
    14	    virasoro_shadow_params,
    15	)
    16	
    17	
    18	def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
    19	    kappa, alpha, delta = 2, 3, 5
    20	    expected_coeffs = (16, 72, 91)
 succeeded in 51ms:
     1	import pytest
     2	from sympy import Rational
     3	
     4	from compute.lib.modular_bootstrap_shadow import (
     5	    ising_model_data,
     6	    lambda_fp,
     7	    minimal_model_shadow_check,
     8	    shadow_genus2_constraint,
     9	    shadow_planted_forest_genus2,
    10	    verify_S_squared,
    11	    verify_S_symmetry,
    12	    verify_S_unitarity,
    13	    verlinde_fusion,
    14	    verify_fusion_integrality,
    15	    virasoro_shadow_data,
    16	)
    17	
    18	
    19	def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
    20	    expected_lambda1 = Rational(1, 24)
 succeeded in 51ms:
     1	import mpmath as mp
     2	
     3	from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO
     4	
     5	
     6	mp.mp.dps = 50
     7	
     8	
     9	def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
    10	    u = mp.mpf(2)
    11	    expected = mp.zeta(u) * mp.zeta(u + 1)
    12	    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
    13	    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
    14	    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")
    15	
    16	
    17	def test_virasoro_defect_matches_one_minus_inverse_zeta():
    18	    u = mp.mpf(3)
    19	    expected = 1 - 1 / mp.zeta(u)
    20	    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
file update:
diff --git a/compute/tests/test_genus1_arithmetic_shadow.py b/compute/tests/test_genus1_arithmetic_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..4a03855a21aa5e50be839923ca5978055f9831b8
--- /dev/null
+++ b/compute/tests/test_genus1_arithmetic_shadow.py
@@ -0,0 +1,36 @@
+import mpmath as mp
+
+from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO
+
+
+mp.mp.dps = 50
+
+
+def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
+    u = mp.mpf(2)
+    expected = mp.zeta(u) * mp.zeta(u + 1)
+    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
+    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
+    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")
+
+
+def test_virasoro_defect_matches_one_minus_inverse_zeta():
+    u = mp.mpf(3)
+    expected = 1 - 1 / mp.zeta(u)
+    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
+    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
+    assert not VIRASORO.is_euler_koszul()
+
+
+def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
+    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
+    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
+    assert HEISENBERG.sewing_coefficients(3) == expected
+
+
+def test_xi_regularization_and_beta_gamma_exactness():
+    expected_xi = mp.zeta(2)
+    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
+    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
+    assert BETA_GAMMA.is_euler_koszul()
+    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
diff --git a/compute/tests/test_modular_bootstrap_shadow.py b/compute/tests/test_modular_bootstrap_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..e38f589d171d11e507394bdc2a34d5dc37fbef10
--- /dev/null
+++ b/compute/tests/test_modular_bootstrap_shadow.py
@@ -0,0 +1,69 @@
+import pytest
+from sympy import Rational
+
+from compute.lib.modular_bootstrap_shadow import (
+    ising_model_data,
+    lambda_fp,
+    minimal_model_shadow_check,
+    shadow_genus2_constraint,
+    shadow_planted_forest_genus2,
+    verify_S_squared,
+    verify_S_symmetry,
+    verify_S_unitarity,
+    verlinde_fusion,
+    verify_fusion_integrality,
+    virasoro_shadow_data,
+)
+
+
+def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
+    expected_lambda1 = Rational(1, 24)
+    expected_lambda2 = Rational(7, 5760)
+    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
+    assert lambda_fp(1) == expected_lambda1
+    assert lambda_fp(2) == expected_lambda2
+
+
+def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
+    vir13 = virasoro_shadow_data(Rational(13))
+    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
+    assert vir13["kappa"] == Rational(13, 2)
+    assert vir13["S_4"] == Rational(10, 1131)
+    assert vir13["Delta"] == Rational(40, 87)
+
+    vir24 = virasoro_shadow_data(Rational(24))
+    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
+    assert vir24["kappa"] == Rational(12)
+    assert vir24["S_4"] == Rational(5, 1704)
+    assert vir24["Delta"] == Rational(20, 71)
+
+
+def test_monster_genus2_constraint_matches_planted_forest_formula():
+    kappa = Rational(12)
+    cubic = Rational(2)
+    expected_delta_pf = Rational(1, 3)
+    expected_genus2 = Rational(167, 480)
+    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
+    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
+    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2
+
+
+def test_ising_modular_data_and_shadow_check_match_known_values():
+    ising = ising_model_data()
+    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
+    assert ising["c"] == Rational(1, 2)
+    assert ising["n_primaries"] == 3
+    assert verify_S_squared(ising["S"])[0]
+    assert verify_S_unitarity(ising["S"])[0]
+    assert verify_S_symmetry(ising["S"])
+
+    fusion = verlinde_fusion(ising["S"])
+    assert verify_fusion_integrality(fusion)
+    assert fusion[1, 1, 0] == pytest.approx(1.0)
+    assert fusion[1, 1, 2] == pytest.approx(1.0)
+    assert fusion[1, 2, 1] == pytest.approx(1.0)
+
+    check = minimal_model_shadow_check(4, 3)
+    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
+    assert check["F_1"] == Rational(1, 96)
+    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
diff --git a/compute/tests/test_shadow_painleve.py b/compute/tests/test_shadow_painleve.py
new file mode 100644
index 0000000000000000000000000000000000000000..0a5e6be2c86d55fd1deaca7b9d18fd588bf85243
--- /dev/null
+++ b/compute/tests/test_shadow_painleve.py
@@ -0,0 +1,61 @@
+import pytest
+
+from compute.lib.shadow_painleve import (
+    classify_singularities,
+    fuchsian_type,
+    heisenberg_shadow_params,
+    jmu_tau_from_connection,
+    painleve_type,
+    painleve_type_multichannel,
+    schwarzian_potential_numeric,
+    shadow_metric_coefficients,
+    shadow_metric_discriminant,
+    singularity_count,
+    virasoro_shadow_params,
+)
+
+
+def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
+    kappa, alpha, delta = 2, 3, 5
+    expected_coeffs = (16, 72, 91)
+    expected_discriminant = -640
+    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
+    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
+    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant
+
+
+def test_schwarzian_potential_numeric_matches_origin_value():
+    value = schwarzian_potential_numeric(2, 3, 5, 0)
+    expected = 5.0 / 8.0
+    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
+    assert value == pytest.approx(expected)
+
+
+def test_delta_zero_classification_is_trivial():
+    params = heisenberg_shadow_params(2)
+    singularities = classify_singularities(*params)
+    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
+    assert singularities[0].type == "ordinary"
+    assert not singularities[0].is_finite
+    assert singularity_count(*params) == {
+        "regular": 0,
+        "irregular": 0,
+        "ordinary": 1,
+        "apparent": 0,
+    }
+    assert fuchsian_type(*params) == "trivial"
+    assert painleve_type(*params) == "trivial"
+
+
+def test_virasoro_shadow_params_match_self_dual_c13_values():
+    kappa, alpha, delta = virasoro_shadow_params(13)
+    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
+    assert kappa == pytest.approx(6.5)
+    assert alpha == pytest.approx(2.0)
+    assert delta == pytest.approx(40.0 / 87.0)
+
+
+def test_multichannel_and_tau_normalization_smoke_checks():
+    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
+    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
+    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)


thinking
**Considering test coverage issues**

I've created a new test file with smoke tests covering various components, like Heisenberg and Virasoro. However, I'm noting that the problem specifies reporting issues at "file:line," but for missing files, I’m unsure how to cite that correctly. I’m thinking it would be straightforward to say which engine file is missing coverage by using `PROBLEM at compute/lib/genus1_arithmetic_shadow.py:1`. It might also help to include clickable links for clarity.
codex
- `PROBLEM at` [compute/lib/genus1_arithmetic_shadow.py](/Users/raeez/chiral-bar-cobar/compute/lib/genus1_arithmetic_shadow.py:1): missing smoke-test coverage for the genus-1 arithmetic shadow engine.
  `EXACT edit applied`: created [compute/tests/test_genus1_arithmetic_shadow.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:1) with four verified smoke tests at [line 9](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:9), [line 17](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:17), [line 25](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:25), and [line 31](/Users/raeez/chiral-bar-cobar/compute/tests/test_genus1_arithmetic_shadow.py:31) covering the Heisenberg Euler product, Virasoro Euler defect, divisor-sum sewing coefficients, and `Xi_H(1)` plus exact `βγ` Euler-Koszul behavior.

- `PROBLEM at` [compute/lib/modular_bootstrap_shadow.py](/Users/raeez/chiral-bar-cobar/compute/lib/modular_bootstrap_shadow.py:1): missing smoke-test coverage for the modular bootstrap shadow engine.
  `EXACT edit applied`: created [compute/tests/test_modular_bootstrap_shadow.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:1) with four verified smoke tests at [line 19](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:19), [line 27](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:27), [line 41](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:41), and [line 51](/Users/raeez/chiral-bar-cobar/compute/tests/test_modular_bootstrap_shadow.py:51) covering `lambda_g^{FP}` low-genus values, Virasoro shadow data at `c=13` and `c=24`, the Monster genus-2 planted-forest correction, and Ising modular/fusion data plus `F_1=1/96`.

- `PROBLEM at` [compute/lib/shadow_painleve.py](/Users/raeez/chiral-bar-cobar/compute/lib/shadow_painleve.py:1): missing smoke-test coverage for the shadow Painleve engine.
  `EXACT edit applied`: created [compute/tests/test_shadow_painleve.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:1) with five verified smoke tests at [line 18](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:18), [line 27](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:27), [line 34](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:34), [line 50](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:50), and [line 58](/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_painleve.py:58) covering closed-form metric coefficients/discriminant, the origin Schwarzian potential, the `Delta=0` trivial classification, Virasoro self-dual `c=13` parameters, and a multichannel `PVI` plus tau-normalization smoke check.

`pytest compute/tests/test_genus1_arithmetic_shadow.py compute/tests/test_modular_bootstrap_shadow.py compute/tests/test_shadow_painleve.py` passed: `13 passed in 0.54s`.

Scope check: the original missing-test scan is now silent.

Out-of-scope defects observed but not edited because you restricted changes to the missing test files: [compute/lib/shadow_painleve.py:279](/Users/raeez/chiral-bar-cobar/compute/lib/shadow_painleve.py:279) and [compute/lib/shadow_painleve.py:663](/Users/raeez/chiral-bar-cobar/compute/lib/shadow_painleve.py:663).
file update:
diff --git a/compute/tests/test_genus1_arithmetic_shadow.py b/compute/tests/test_genus1_arithmetic_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..4a03855a21aa5e50be839923ca5978055f9831b8
--- /dev/null
+++ b/compute/tests/test_genus1_arithmetic_shadow.py
@@ -0,0 +1,36 @@
+import mpmath as mp
+
+from compute.lib.genus1_arithmetic_shadow import BETA_GAMMA, HEISENBERG, VIRASORO
+
+
+mp.mp.dps = 50
+
+
+def test_heisenberg_shadow_matches_exact_euler_product_at_u2():
+    u = mp.mpf(2)
+    expected = mp.zeta(u) * mp.zeta(u + 1)
+    # VERIFIED: [DC] weights=[1] gives S_H(u)=zeta(u)zeta(u+1); [CF] genus-1 triangle docstring states the same exact factorization.
+    assert abs(HEISENBERG.S(u) - expected) < mp.mpf("1e-30")
+    assert abs(HEISENBERG.euler_defect(u) - mp.mpf(1)) < mp.mpf("1e-30")
+
+
+def test_virasoro_defect_matches_one_minus_inverse_zeta():
+    u = mp.mpf(3)
+    expected = 1 - 1 / mp.zeta(u)
+    # VERIFIED: [DC] weight multiset [2] subtracts H_1(u)=1 in the definition of S_A; [LC] the docstring records the Virasoro defect as 1-1/zeta(u).
+    assert abs(VIRASORO.euler_defect(u) - expected) < mp.mpf("1e-30")
+    assert not VIRASORO.is_euler_koszul()
+
+
+def test_heisenberg_sewing_coefficients_start_with_divisor_sums():
+    expected = [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(4) / 3]
+    # VERIFIED: [DC] for weights=[1], a_N=sigma_{-1}(N)=sum_{d|N} 1/d; [LC] N=1,2,3 give 1, 1+1/2, 1+1/3.
+    assert HEISENBERG.sewing_coefficients(3) == expected
+
+
+def test_xi_regularization_and_beta_gamma_exactness():
+    expected_xi = mp.zeta(2)
+    # VERIFIED: [DC] Xi_H(1)=zeta(2)*(u-1)zeta(u)|_{u=1}; [LC] lim_{u->1}(u-1)zeta(u)=1.
+    assert abs(HEISENBERG.Xi(mp.mpf(1)) - expected_xi) < mp.mpf("1e-30")
+    assert BETA_GAMMA.is_euler_koszul()
+    assert abs(BETA_GAMMA.euler_defect(mp.mpf(2)) - mp.mpf(1)) < mp.mpf("1e-30")
diff --git a/compute/tests/test_modular_bootstrap_shadow.py b/compute/tests/test_modular_bootstrap_shadow.py
new file mode 100644
index 0000000000000000000000000000000000000000..e38f589d171d11e507394bdc2a34d5dc37fbef10
--- /dev/null
+++ b/compute/tests/test_modular_bootstrap_shadow.py
@@ -0,0 +1,69 @@
+import pytest
+from sympy import Rational
+
+from compute.lib.modular_bootstrap_shadow import (
+    ising_model_data,
+    lambda_fp,
+    minimal_model_shadow_check,
+    shadow_genus2_constraint,
+    shadow_planted_forest_genus2,
+    verify_S_squared,
+    verify_S_symmetry,
+    verify_S_unitarity,
+    verlinde_fusion,
+    verify_fusion_integrality,
+    virasoro_shadow_data,
+)
+
+
+def test_lambda_fp_matches_low_genus_faber_pandharipande_values():
+    expected_lambda1 = Rational(1, 24)
+    expected_lambda2 = Rational(7, 5760)
+    # VERIFIED: [DC] lambda_fp uses the Bernoulli/Faber-Pandharipande formula; [LC] g=1 and g=2 recover the canonical 1/24 and 7/5760 coefficients.
+    assert lambda_fp(1) == expected_lambda1
+    assert lambda_fp(2) == expected_lambda2
+
+
+def test_virasoro_shadow_data_matches_self_dual_and_monster_values():
+    vir13 = virasoro_shadow_data(Rational(13))
+    # VERIFIED: [DC] kappa=c/2, S_4=10/(c(5c+22)), Delta=8*kappa*S_4; [LC] c=13 is the self-dual Virasoro point.
+    assert vir13["kappa"] == Rational(13, 2)
+    assert vir13["S_4"] == Rational(10, 1131)
+    assert vir13["Delta"] == Rational(40, 87)
+
+    vir24 = virasoro_shadow_data(Rational(24))
+    # VERIFIED: [DC] same closed formulas; [CF] c=24 gives the Monster scalar lane with kappa=12.
+    assert vir24["kappa"] == Rational(12)
+    assert vir24["S_4"] == Rational(5, 1704)
+    assert vir24["Delta"] == Rational(20, 71)
+
+
+def test_monster_genus2_constraint_matches_planted_forest_formula():
+    kappa = Rational(12)
+    cubic = Rational(2)
+    expected_delta_pf = Rational(1, 3)
+    expected_genus2 = Rational(167, 480)
+    # VERIFIED: [DC] delta_pf=S_3(10S_3-kappa)/48 and F_2=kappa*7/5760+delta_pf; [LC] Monster has kappa=12, S_3=2.
+    assert shadow_planted_forest_genus2(kappa, cubic) == expected_delta_pf
+    assert shadow_genus2_constraint(kappa, cubic) == expected_genus2
+
+
+def test_ising_modular_data_and_shadow_check_match_known_values():
+    ising = ising_model_data()
+    # VERIFIED: [LT] Ising is M(4,3) with c=1/2 and three primaries; [DC] the BPZ S-matrix satisfies S^2=I and unitarity in this normalization.
+    assert ising["c"] == Rational(1, 2)
+    assert ising["n_primaries"] == 3
+    assert verify_S_squared(ising["S"])[0]
+    assert verify_S_unitarity(ising["S"])[0]
+    assert verify_S_symmetry(ising["S"])
+
+    fusion = verlinde_fusion(ising["S"])
+    assert verify_fusion_integrality(fusion)
+    assert fusion[1, 1, 0] == pytest.approx(1.0)
+    assert fusion[1, 1, 2] == pytest.approx(1.0)
+    assert fusion[1, 2, 1] == pytest.approx(1.0)
+
+    check = minimal_model_shadow_check(4, 3)
+    # VERIFIED: [LT] Ising gap is h_sigma=1/16; [DC] F_1=kappa/24=(1/4)/24=1/96.
+    assert check["F_1"] == Rational(1, 96)
+    assert check["actual_gap"] == pytest.approx(1.0 / 16.0)
diff --git a/compute/tests/test_shadow_painleve.py b/compute/tests/test_shadow_painleve.py
new file mode 100644
index 0000000000000000000000000000000000000000..0a5e6be2c86d55fd1deaca7b9d18fd588bf85243
--- /dev/null
+++ b/compute/tests/test_shadow_painleve.py
@@ -0,0 +1,61 @@
+import pytest
+
+from compute.lib.shadow_painleve import (
+    classify_singularities,
+    fuchsian_type,
+    heisenberg_shadow_params,
+    jmu_tau_from_connection,
+    painleve_type,
+    painleve_type_multichannel,
+    schwarzian_potential_numeric,
+    shadow_metric_coefficients,
+    shadow_metric_discriminant,
+    singularity_count,
+    virasoro_shadow_params,
+)
+
+
+def test_shadow_metric_coefficients_and_discriminant_match_closed_form():
+    kappa, alpha, delta = 2, 3, 5
+    expected_coeffs = (16, 72, 91)
+    expected_discriminant = -640
+    # VERIFIED: [DC] q0=4kappa^2, q1=12kappa alpha, q2=9alpha^2+2Delta and disc=q1^2-4q0q2; [LC] substituting (2,3,5) gives (16,72,91) and -640.
+    assert shadow_metric_coefficients(kappa, alpha, delta) == expected_coeffs
+    assert shadow_metric_discriminant(kappa, alpha, delta) == expected_discriminant
+
+
+def test_schwarzian_potential_numeric_matches_origin_value():
+    value = schwarzian_potential_numeric(2, 3, 5, 0)
+    expected = 5.0 / 8.0
+    # VERIFIED: [DC] V(0)=8kappa^2 Delta/Q_L(0)^2; [LC] Q_L(0)=4kappa^2 so (8*4*5)/16^2=5/8.
+    assert value == pytest.approx(expected)
+
+
+def test_delta_zero_classification_is_trivial():
+    params = heisenberg_shadow_params(2)
+    singularities = classify_singularities(*params)
+    # VERIFIED: [DC] Heisenberg has Delta=0 so V=0 and the Schrodinger equation is u''=0; [LC] the module returns only the ordinary point at infinity.
+    assert singularities[0].type == "ordinary"
+    assert not singularities[0].is_finite
+    assert singularity_count(*params) == {
+        "regular": 0,
+        "irregular": 0,
+        "ordinary": 1,
+        "apparent": 0,
+    }
+    assert fuchsian_type(*params) == "trivial"
+    assert painleve_type(*params) == "trivial"
+
+
+def test_virasoro_shadow_params_match_self_dual_c13_values():
+    kappa, alpha, delta = virasoro_shadow_params(13)
+    # VERIFIED: [DC] Virasoro uses kappa=c/2, alpha=2, Delta=40/(5c+22); [LC] c=13 gives 13/2, 2, 40/87.
+    assert kappa == pytest.approx(6.5)
+    assert alpha == pytest.approx(2.0)
+    assert delta == pytest.approx(40.0 / 87.0)
+
+
+def test_multichannel_and_tau_normalization_smoke_checks():
+    # VERIFIED: [DC] two nontrivial channels promote the classifier to PVI; [LC] tau(t)=sqrt(Q(t)/Q(0)) gives tau(0)=1.
+    assert painleve_type_multichannel([(1, 1, 1), (1, 2, 3)]) == "PVI"
+    assert jmu_tau_from_connection(1, 1, 0, 0) == pytest.approx(1.0)

tokens used
111,527
