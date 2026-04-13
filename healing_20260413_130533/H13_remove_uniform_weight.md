# H13_remove_uniform_weight (890s)

Added a research remark in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22641) that sharpens the uniform-weight question for Theorem D and C2. It now separates the proved all-weight free-energy statement
`F_g = \kappa \lambda_g^{\mathrm{FP}} + \delta F_g^{\mathrm{cross}}`
from the still-missing class-valued lift needed to remove the hypothesis from the cohomological obstruction theorem and MC2/C2. The remark also makes the compute state explicit, explains why a genus-independent modified `\kappa` is the wrong invariant, and corrects the premise that `\beta\gamma` has nonzero cross-channel correction. I also repaired the stale table note later in the chapter at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32103) so `\beta\gamma` is treated as the free-field exact exception and the `\mathcal W_3` row is marked as scalar-part-only.

I regenerated metadata (`metadata/census.json`, `metadata/claims.jsonl`, `metadata/label_index.json`, `metadata/theorem_registry.md`) and ran the narrow compute falsifiers. `pytest` passed on 297 W₃/multi-weight tests plus 42 `\beta\gamma` cross-channel tests. Pending propagation surface, if you want the same research-programme wording mirrored across the bridge volumes: [holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:166) and [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4).

## Fortification Report
Theorem D
- PRIMARY PROOF: sound on its stated uniform-weight scope.
- SECONDARY PROOF: written.
- TECHNIQUE: bar-intrinsic shadow tower plus GRR/family-index route.
- CONDITION STATUS: uniform-weight all genera; genus-1 universal for all families; multi-weight free-energy correction theorem proved, but class-valued removal remains open.
- CONFIDENCE: high.

Theorem C2
- PRIMARY PROOF: sound on its current conditional scope.
- SECONDARY PROOF: sketched.
- TECHNIQUE: bar-intrinsic MC2 plus comparison through tautological-line support; upgrade route now stated via mixed-channel class lift.
- CONDITION STATUS: conditional on replacing one-channel line support by a mixed-channel support theorem / class-valued correction package.
- CONFIDENCE: medium.


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
session id: 019d869e-53b6-7e12-8608-5a7889597076
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.
Your mission is threefold:

1. HEAL: find remaining wounds (gaps, weaknesses, fragilities) and repair them
2. FORTIFY: for every main result, construct an ALTERNATIVE proof path that provides
   REDUNDANCY — if one proof fails, the other stands independently
3. UPGRADE: where a result is conditional, investigate whether the condition can be
   REMOVED by new mathematical insight, alternative technique, or reformulation

You have WRITE access. Make edits. Write new proofs. Add remarks.
The standard is: every theorem that can have two independent proofs MUST have two.
</task>

<action_safety>
Keep edits within assigned scope. After every substantial edit, re-read and verify.
New proofs must be mathematically rigorous — no hand-waving, no "by analogy."
If you cannot complete a proof: write a detailed proof SKETCH with the key steps
identified and the remaining gap precisely named.
</action_safety>

<completeness_contract>
For each theorem in your scope:
1. Verify the PRIMARY proof is now sound (after rectification)
2. Write or sketch a SECONDARY proof via a different technique
3. If conditional: investigate removing the condition
4. State confidence level for each proof path
</completeness_contract>

<structured_output_contract>
End with:
## Fortification Report
For each theorem:
  - PRIMARY PROOF: [sound/repaired/gap-remaining]
  - SECONDARY PROOF: [written/sketched/identified/blocked]
  - TECHNIQUE: [what alternative method]
  - CONDITION STATUS: [unconditional/conditional-on-X/research-programme-Y]
  - CONFIDENCE: [high/medium/low]
</structured_output_contract>


RESEARCH: Can uniform-weight be removed from Theorem D and C2?

TARGET: chapters/theory/higher_genus_modular_koszul.tex (add Research Remark)

The uniform-weight condition restricts to families where all generators have the same
conformal weight. Multi-weight families (W_N for N>=3, betagamma) have delta_F_g^cross ≠ 0.

INVESTIGATE:
1. What is the STRUCTURE of delta_F_g^cross? Is it computable?
2. Can obs_g = kappa*lambda_g + delta_F_g^cross be stated as a THEOREM with the
   correction term explicitly given?
3. Is there a modified kappa (kappa_eff?) that absorbs the correction?
4. What is the current state of multi-weight computations? Check compute/lib/ for
   any engines that compute delta_F_g^cross.

Write a Research Remark with: (a) what's known, (b) what's computable,
(c) the precise obstruction to removal, (d) a research programme if the condition
can be weakened.
mcp startup: no servers
codex
Using `frontier-research` for the condition-removal investigation and `beilinson-rectify` for the manuscript repair. First step is to read the required constitutional surfaces and locate every live reference to Theorem D, C2, uniform-weight, and any `delta_F_g^cross` compute support before drafting the new remark.
collab spawn_agent(call_oxLXpHmzyrRlcKOGJ39uGYaG, prompt="<task>Find the exact locations and surrounding context for Theorem D, C2, uniform-weight condition, and any existing dis…")
mcp startup: no servers
spawn_agent(call_oxLXpHmzyrRlcKOGJ39uGYaG, prompt="<task>Find the exact locations and surrounding context for Theorem D, C2, uniform-weight condition, and any existing dis…") pending init:
  agent: 019d869e-a76e-7dc3-a786-1ee349aa7390
collab spawn_agent(call_4PnwSnXwAMiCm0SBH7LFV4ww, prompt="<task>Inspect `compute/lib/` and nearby tests/notes for any engine, helper, oracle, or terminology related to `delta_F_g…")
spawn_agent(call_4PnwSnXwAMiCm0SBH7LFV4ww, prompt="<task>Inspect `compute/lib/` and nearby tests/notes for any engine, helper, oracle, or terminology related to `delta_F_g…") pending init:
  agent: 019d869e-a78d-7512-a118-deb963680694
mcp startup: no servers
collab spawn_agent(call_o7h9XWIqMeOVLXl7dnvgybhM, prompt="<task>Search across Vol I, Vol II, and Vol III for shared statements about uniform-weight, Theorem D, C2, `obs_g = kappa…")
spawn_agent(call_o7h9XWIqMeOVLXl7dnvgybhM, prompt="<task>Search across Vol I, Vol II, and Vol III for shared statements about uniform-weight, Theorem D, C2, `obs_g = kappa…") pending init:
  agent: 019d869e-a881-7672-9962-79efd032b095
mcp startup: no servers
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "uniform-weight" -n' in /Users/raeez/chiral-bar-cobar succeeded in 91ms:
_20260413_111534/R04_higher_genus_modular_koszul.md:8441:-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:8449:+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:8466: uniform-weight algebras. For multi-generator algebras
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:8498: $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:8974:-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:8982:+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:8999: uniform-weight algebras. For multi-generator algebras
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:9031: $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:9724:-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:9732:+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:9749: uniform-weight algebras. For multi-generator algebras
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:9781: $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:10478:-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:10486:+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:10503: uniform-weight algebras. For multi-generator algebras
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:10535: $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:11209:-proved uniform-weight lane, while Theorem~\ref{thm:family-index}
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:11217:+trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:11234: uniform-weight algebras. For multi-generator algebras
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:11266: $\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1052

healing_20260413_132214/H04_thm_D_alt_proof.md:8:Theorem D
healing_20260413_132214/H04_thm_D_alt_proof.md:95:TARGET: chapters/theory/higher_genus_modular_koszul.tex (add Remark near Theorem D)
healing_20260413_132214/H04_thm_D_alt_proof.md:117:I’m locking the Theorem D claim surface in `chapters/theory/higher_genus_modular_koszul.tex` and reading the required constitutional files first. I’ll verify the current theorem statement and nearby conventions, then draft a GRR-based alternative proof path that is genuinely independent of the shadow tower route.
healing_20260413_132214/H04_thm_D_alt_proof.md:251:I’m using `beilinson-rectify` for the theorem-surface repair and `cross-volume-propagation` after the edit because `\mathrm{obs}_g=\kappa\lambda_g` is a shared formula surface. Next I’m reading the Theorem D lane, its local dependencies, and existing GRR/Hodge references before drafting the remark.
healing_20260413_132214/H04_thm_D_alt_proof.md:253:Fortifying Theorem D with an independent GRR-based proof path requires local proof-surface audit, then a scoped edit, then cross-volume and style verification.
healing_20260413_132214/H04_thm_D_alt_proof.md:254:  → Inspect Theorem D in higher_genus_modular_koszul.tex and identify local dependencies, conventions, and insertion point for an alternative-proof remark
healing_20260413_132214/H04_thm_D_alt_proof.md:428:I notice that there's an existing remark labeled [Alternative proof via GRR] around line 3029. The task asks me to add a remark near Theorem D, which makes me think the current remark might need some adjustments to align with the requested proof path. I should definitely check lines 2860 to 3085 to see what's going on, as the user might expect something that's still missing. I’ll start by taking a closer look at Theorem D and the existing remark.
healing_20260413_132214/H04_thm_D_alt_proof.md:430:There is already a GRR remark in the Theorem D lane, but I need to check whether it actually satisfies the requested independence standard. I’m reading that block closely now and will tighten it if it still leans on the shadow construction too heavily or overstates the family-index input.
healing_20260413_132214/H04_thm_D_alt_proof.md:892:Scope lock: `chapters/theory/higher_genus_modular_koszul.tex`, Theorem D lane around `rem:theorem-d-alt-grr`, formula `\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g`, uniform-weight scalar lane. I’m about to replace the current remark with a stricter Hodge/GRR proof path that cites the bar-family surface `\eqref{eq:bar-family}` directly and states its independence from `\Theta_\cA` and the shadow route.
healing_20260413_132214/H04_thm_D_alt_proof.md:992: \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
healing_20260413_132214/H04_thm_D_alt_proof.md:993: \index{Hodge bundle!alternative proof of Theorem D}
healing_20260413_132214/H04_thm_D_alt_proof.md:1076: \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
healing_20260413_132214/H04_thm_D_alt_proof.md:1077: \index{Hodge bundle!alternative proof of Theorem D}
healing_20260413_132214/H04_thm_D_alt_proof.md:1164:The current text might be sufficient, but I need to check if referencing `Theorem\ref{thm:genus-universality}` is odd due to the remark in theorem D. Maybe I can also mention "or Theorem\ref{thm:family-index}". The user specifically mentioned not using `thm:genus-universality`, but the remark serves as an alternative proof for the uniform-weight clause of Theorem D, which I now think might actually be `Theorem\ref{thm:genus-universality}`. So, updating the remark to say "without using Theorem\ref{thm:genus-universality} as input" seems fine.
healing_20260413_132214/H04_thm_D_alt_proof.md:1175:\index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
healing_20260413_132214/H04_thm_D_alt_proof.md:1176:\index{Hodge bundle!alternative proof of Theorem D}
healing_20260413_132214/H04_thm_D_alt_proof.md:1210: \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
healing_20260413_132214/H04_thm_D_alt_proof.md:1211: \index{Hodge bundle!alternative proof of Theorem D}
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
exec
/bin/zsh -lc 'rg -n "delta_F" -n "cross" -n "multi-weight" -n "obs_g" compute/lib | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: cross: No such file or directory (os error 2)
rg: multi-weight: No such file or directory (os error 2)
rg: obs_g: No such file or directory (os error 2)
compute/lib/rectification_delta_f2_verify_engine.py:1:r"""Independent verification engine for delta_F_2^{grav}(W_N).
compute/lib/rectification_delta_f2_verify_engine.py:5:    delta_F_2^{grav}(W_N, c) = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c)
compute/lib/rectification_delta_f2_verify_engine.py:24:The cross-channel part (mixed channels) is delta_F_2^cross.
compute/lib/rectification_delta_f2_verify_engine.py:477:def delta_F2_grav_graph_sum(N: int, c: Fraction) -> Fraction:
compute/lib/rectification_delta_f2_verify_engine.py:478:    """Compute delta_F_2^{grav}(W_N, c) by summing over all 7 genus-2 graphs.
compute/lib/rectification_delta_f2_verify_engine.py:494:def delta_F2_grav_per_graph(N: int, c: Fraction) -> Dict[str, Dict[str, Fraction]]:
compute/lib/rectification_delta_f2_verify_engine.py:495:    """Per-graph decomposition of delta_F_2^{grav}(W_N, c)."""
compute/lib/rectification_delta_f2_verify_engine.py:522:    """Claimed: delta_F_2^{grav}(W_N, c) = B(N) + A(N)/c."""
compute/lib/rectification_delta_f2_verify_engine.py:784:def delta_F2_grav_symbolic(N: int, c: Fraction) -> Fraction:
compute/lib/rectification_delta_f2_verify_engine.py:785:    """Compute delta_F_2^{grav} using the algebraic/symbolic expressions.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
418:**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).
581:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
Plan update
Scoped the job to the theorem surface and compute support before editing. I’m gathering repository evidence in parallel, then I’ll draft the research remark, propagate if needed, and run narrow verification.
  → Collect theorem/context evidence from required files and target chapter
  • Inspect compute support for multi-weight correction terms
  • Draft and insert research remark in target chapter
  • Check cross-volume propagation surface and verify final wording
exec
/bin/zsh -lc 'rg -n "multi[-_]weight" -n "delta_F_g" -n "delta_F_g''^cross" -n "delta_F_g" compute/lib | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: delta_F_g: No such file or directory (os error 2)
rg: delta_F_g^cross: No such file or directory (os error 2)
rg: delta_F_g: No such file or directory (os error 2)
compute/lib/phantom_m5_koszul_dual_engine.py:102:  AP32  multi-weight algebras receive cross-channel corrections at g >= 2
compute/lib/rectification_delta_f2_verify_engine.py:7:This engine is built FROM SCRATCH with ZERO imports from the multi-weight
compute/lib/rectification_delta_f2_verify_engine.py:48:    thm:multi-weight-genus-expansion, AP27, Faber-Pandharipande
compute/lib/bcov_mc_complete_proof_engine.py:159:    AP32: scalar formula holds at all genera for uniform-weight; fails multi-weight
compute/lib/mumford_chiodo_multiweight_engine.py:1:r"""Mumford-Chiodo formula for multi-weight Hodge classes at genus 2.
compute/lib/curved_sc_higher_genus_engine.py:166:- thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex): delta_F_g^cross
compute/lib/curved_sc_higher_genus_engine.py:753:    for the W_3 algebra (thm:multi-weight-genus-expansion(vi)).
compute/lib/curved_sc_higher_genus_engine.py:759:    - R-matrix independent (thm:multi-weight-genus-expansion(v)).
compute/lib/curved_sc_higher_genus_engine.py:760:    - Vanishes iff uniform-weight (thm:multi-weight-genus-expansion(iv)).
compute/lib/curved_sc_higher_genus_engine.py:797:    correction vanishes at all genera (thm:multi-weight-genus-expansion(iv)).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "obs_g" chapters' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '390,440p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
- B65. RETRACTED (degree is correct; arity banned). AP176.
- B66. RETRACTED (degree is correct; arity banned). AP176.
- B67. RETRACTED (degree is correct; arity banned). AP176.
- B68. "S_2 = c/12, which is the Virasoro central charge itself." DOUBLE ERROR: S_2 = c/2 (not c/12), and the central charge is c (not c/12). AP177.
- B69. `pi_3(BU) = \Z`. CORRECT: `pi_3(BU) = 0` (Bott periodicity: pi_{odd}(BU) = 0). Confusion with pi_3(U) = Z. AP181.
- B70. `\kappa_{\mathrm{ch}} = h^{1,1}` for local surfaces. CORRECT: `\kappa_{\mathrm{ch}} = \chi(S)/2`. These differ when h^{0,2} != 0 (e.g., K3: h^{1,1}=20 but chi/2=12). AP182.
- B71. McKay quiver of Z_3 = K_{3,3}. CORRECT: 3 copies of the oriented 3-cycle. K_{3,3} is undirected bipartite. AP183.
- B72. "Excision of [0,1] at t gives B(A) tensor B(A)." CORRECT: excision gives B_L tensor_A B_R = B(A) (one copy, tensor over A). Coproduct is Delta: B(A) -> B(A) tensor B(A) (two copies, plain tensor). AP184.
- B73. "pi_4(BU) = Z provides native E_2 for CY_4." CORRECT: pi_4(BU) = Z is the obstruction GROUP, not a guarantee. AP185.

## Opus 4.6 Quirks and Failure Modes

Model-specific failure patterns observed across ~100 Opus 4.6 agent invocations. These are not generic anti-patterns (see AP catalog below) but recurrent behaviours of this specific model on this specific manuscript. Source: opus_46_failure_modes_wave12.md (FM1-FM22).

**FM1. Generic-formula reaching ("pretty version" attractor).** Opus falls back to the canonical textbook form when memory is uncertain. For affine KM, training-data weight makes `Omega/z` the default; the level-prefixed `k*Omega/z` is less prevalent. Evidence: AP126/AP141, 42+ instances. Counter: append to every r-matrix prompt: "After writing ANY r-matrix, substitute k=0 and verify r vanishes. Do not proceed until k=0 -> r=0."

**FM2. Level-prefix dropping on summarisation.** When Opus summarises a displayed formula from an earlier file read, it omits scalar prefactors even if the source had them. Lost prefixes: k, c/2, kappa, 1/(2*pi*i). Counter: re-Read the source lines verbatim before typing; do not rely on context cache.

**FM3. Bosonic/fermionic conformal-anomaly conflation.** `c_bg` and `c_bc` look structurally similar (both polynomial in lambda with centre at 1/2) and satisfy c_bg+c_bc=0. Opus swaps them under pressure. Counter: after writing any ghost central charge, substitute lambda=2 AND lambda=1 and verify c_bc(2)=-26, c_bg(2)=+26, sum=0 pointwise.

exec
/bin/zsh -lc 'rg -n "delta_F" -g"*.py" compute lib | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: lib: No such file or directory (os error 2)
compute/lib/rectification_delta_f2_verify_engine.py:1:r"""Independent verification engine for delta_F_2^{grav}(W_N).
compute/lib/rectification_delta_f2_verify_engine.py:5:    delta_F_2^{grav}(W_N, c) = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c)
compute/lib/rectification_delta_f2_verify_engine.py:24:The cross-channel part (mixed channels) is delta_F_2^cross.
compute/lib/rectification_delta_f2_verify_engine.py:477:def delta_F2_grav_graph_sum(N: int, c: Fraction) -> Fraction:
compute/lib/rectification_delta_f2_verify_engine.py:478:    """Compute delta_F_2^{grav}(W_N, c) by summing over all 7 genus-2 graphs.
compute/lib/rectification_delta_f2_verify_engine.py:494:def delta_F2_grav_per_graph(N: int, c: Fraction) -> Dict[str, Dict[str, Fraction]]:
compute/lib/rectification_delta_f2_verify_engine.py:495:    """Per-graph decomposition of delta_F_2^{grav}(W_N, c)."""
compute/lib/rectification_delta_f2_verify_engine.py:522:    """Claimed: delta_F_2^{grav}(W_N, c) = B(N) + A(N)/c."""
compute/lib/rectification_delta_f2_verify_engine.py:784:def delta_F2_grav_symbolic(N: int, c: Fraction) -> Fraction:
compute/lib/rectification_delta_f2_verify_engine.py:785:    """Compute delta_F_2^{grav} using the algebraic/symbolic expressions.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "obs_g"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 417

healing_20260413_132214/H04_thm_D_alt_proof.md:100:1. obs_g is a cohomology class on M-bar_g. The Hodge bundle E has c_1(E) = lambda_1.
healing_20260413_132214/H04_thm_D_alt_proof.md:258:/bin/zsh -lc "rg -n \"thm:genus-universality|def:scalar-lane|obs_g|lambda_g|GRR|Grothendieck|Faltings|Mumford|Hodge bundle|universal curve|pi_\\*|R\\pi_\\*\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H04_thm_D_alt_proof.md:262:    (?:thm:genus-universality|def:scalar-lane|obs_g|lambda_g|GRR|Grothendieck|Faltings|Mumford|Hodge bundle|universal curve|pi_\*|R\pi_\*)
healing_20260413_132214/H04_thm_D_alt_proof.md:337:/bin/zsh -lc "rg -n 'thm:genus-universality|def:scalar-lane|obs_g|lambda_g|Faltings|Mumford|Grothendieck|Riemann-Roch|Hodge bundle|universal curve|R\\\\pi_\\*|pi_\\*' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_132214/H04_thm_D_alt_proof.md:360:/bin/zsh -lc "rg -n 'lambda_g|Hodge bundle|Mumford|Faltings|GRR|Grothendieck|Riemann-Roch|obs_g' chapters/theory chapters/connections chapters/examples appendices | head -n 300" in /Users/raeez/chiral-bar-cobarexec
healing_20260413_132214/H04_thm_D_alt_proof.md:361:/bin/zsh -lc "rg -n 'thm:genus-universality|obs_g\\s*=\\s*\\\\kappa|\\\\mathrm\\{obs\\}_g\\s*=\\s*\\\\kappa|lambda_g' ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups | head -n 300" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
CLAUDE.md:67:Every formula of the form `F_g = ... lambda_g ...` or `obs_g = ...` MUST be followed within the same sentence by ONE of:
CLAUDE.md:202:4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower).
CLAUDE.md:204:NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" — they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.
CLAUDE.md:329:- B26. `obs_g = \kappa * \lambda_g` untagged. CORRECT: append (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta F_g^cross). AP32.
CLAUDE.md:418:**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).
CLAUDE.md:505:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
CLAUDE.md:567:AP32: Genus-1 != all-genera. obs_1=kappa*lambda_1 unconditional. Multi-weight g>=2: scalar formula FAILS. **Every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Untagged = violation.**
CLAUDE.md:738:Trigger: any theorem statement, any obs_g / F_g / lambda_g formula, any universal quantifier.
wave2_audit_20260413_001942/D13_genus_1_vs_all.md:109:Find EVERY obs_g or F_g formula. For each: is it tagged (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta)? Any untagged formulas (AP32)?
wave2_audit_20260413_001942/D13_genus_1_vs_all.md:122:I’m considering using shell rg for easier searches, but the instructions say to prefer explorers for codebase questions. I should spawn explorers to search across three repos, though I’m unsure if they can access sibling directories outside the current workspace. Since the task involves searching formulas like obs_g and F_g across volumes, I'll likely need to use exec commands for cross-volume search. Let’s see how I can manage this!
wave2_audit_20260413_001942/D13_genus_1_vs_all.md:124:Using `deep-beilinson-audit` for a cross-volume AP32 sweep. First step is to locate every `obs_g` and `F_g` surface across the three chapter trees, then read each occurrence in context and classify only grounded findings with exact fixes.
wave2_audit_20260413_001942/D13_genus_1_vs_all.md:150:/bin/zsh -lc 'rg -n "AP32|uniform-weight|obs_g|F_g" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "delta_F" -n "delta_F_g" -n "delta_F_g''^"' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: delta_F_g: No such file or directory (os error 2)
rg: delta_F_g^: No such file or directory (os error 2)
thinking
**Gathering skill files**

I think I need to open the skill files, probably to get some important information. I might use exec_command to read the minimal sections of these skills. Using multi_tool_use.parallel could help for running those commands simultaneously. Also, updating the commentary might be a good idea to mention gathering compute and theorem surfaces. So, I’ll go ahead with exec_command for these skill files and see what I can uncover!
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "modular characteristic" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
190: the modular characteristic~$\kappa$, the cubic coefficient~$\alpha$,
1738:realising the modular characteristic package as a Chern--Weil
2029:Before the extension appendices, the modular characteristic was
3035:The modular characteristic separates $V^\natural$ from all
3866: The modular characteristic is the scalar projection of the
4293:a factored polynomial in the modular characteristic~$\kappa = S_2$
4462:(\ClaimStatusConjectured) identifies the modular characteristic
4510: & Dual modular characteristic
4772:the modular characteristic $\kappa(\cA)$, which is the
4781:The modular characteristic theorem (Theorem~D,
4899:\index{modular characteristic!polysemy}%
4902: \item $\kappa(\cA)$: the \emph{modular characteristic} (Theorem~D), defined by $F_1 = \kappa \cdot \lambda_1^{\mathrm{FP}}$. Intrinsic to the chiral algebra~$\cA$.
4907:These coincide for Heisenberg ($\kappa = k$), Virasoro ($\kappa = c/2$), and affine KM at generic level ($\kappa = \dim(\mathfrak{g})(k{+}h^\vee)/(2h^\vee)$). They diverge for K3-fibered CY$_3$ (where (ii) and (iv) differ by a factor of $5/0 = \infty$) and for non-compact toric CY$_3$ (where (ii) and (iii) differ by a factor of $12$). The modular characteristic $\kappa(\cA)$ in the sense of (i) is the intrinsic invariant; the others are geometric proxies valid in restricted contexts.
5912:of the modular characteristic hierarchy parallels $\kappa(\cA)$ as the first
6799: theorem (Theorem~C) and the modular characteristic constraint
7820:(obstruction = modular characteristic $\times$ Hodge class).}
8008:modular characteristic $\kappa(\cA)$.
8057:\emph{deformation theory}: the modular characteristic
9722: complementarity, modular characteristic,
10886: modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$),
codex
I’m collecting the theorem surface and the compute/oracle surface separately so the remark can distinguish established results from computable but unpublished structure. After that I’ll draft the remark against the live wording in the target chapter rather than from memory.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
2950:\index{Lagrangian self-intersection!Theorem D}
3031:\index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
3032:\index{Hodge bundle!alternative proof of Theorem D}
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/frontier-research/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "delta_F"' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
---
name: frontier-research
description: Use for new theorem architecture, research synthesis, or frontier programme design. Keep work local by default. Delegate or swarm only when the user explicitly authorizes it. This is the Codex-native equivalent of the frontier and research-swarm workflows from `CLAUDE.md`.
---

# Frontier Research

Frontier work is allowed only after the proved core, the conditional bridge, and the conjectural extension are separated sharply.

## Workflow

1. Partition the topic into:
   proved core,
   compute-backed evidence,
   conditional bridge,
   conjectural extension,
   heuristic picture.
2. Read the live theorem surface before synthesizing new structure.
3. Name the exact blocker for every missing implication.
4. Prefer the strongest narrower programme statement that survives hostile rereading.
 succeeded in 52ms:
---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the full target file
- the directly cited dependencies

 succeeded in 52ms:
Total output lines: 3520

CLAUDE.md:505:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
CLAUDE.md:543:**pole/weight** (AP19, AP21, AP27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.
CLAUDE.md:579:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
wave2_audit_20260413_001942/D13_genus_1_vs_all.md:163:489:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
wave2_audit_20260413_001942/D13_genus_1_vs_all.md:164:507:**pole/weight** (AP19, AP21, AP27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.
wave2_audit_20260413_001942/D13_genus_1_vs_all.md:167:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
wave2_audit_20260413_001942/S11_bv_brst_to_body.md:140:CLAUDE.md:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:298:CLAUDE.md:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:302:audit_campaign_20260412_231034/T05_thm_C2.md:181:CLAUDE.md:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:304:audit_campaign_20260412_231034/T06_thm_D.md:140:CLAUDE.md:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:308:rectification_20260412_233715/R18_cobar_construction.md:467:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:915:CLAUDE.md:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
COMMIT_MESSAGE.txt:28:- delta_F_2(W_3) = (c+204)/(16c) propagated (resolves
wave2_audit_20260413_001942/M08_genus2.md:53:Explicit genus-2: 7 stable graphs, 2x2 period matrix, first multi-variable delta_F_g^cross?
wave2_audit_20260413_001942/B06_MC_bridge.md:178:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:584:./audit_campaign_20260412_231034/T06_thm_D.md:266:/bin/zsh -lc "rg -n \"thm:genus-universality|def:scalar-lane|delta F_g\\\\"'^'"\\\\{\\\\mathrm\\\\{cross\\\\}\\\\}|delta_F_g\\\\"'^cross|UNIFORM-WEIGHT|ALL-WEIGHT|genus universality|Theorem D|F_1 = '"\\\\kappa/24|F_1\\\\s*=\\\\s*\\\\kappa/24|F_1\\\\s*=\\\\s*\\\\\\\\kappa/24|lambda_g\\\\"'^'"\\\\{\\\\mathrm\\\\{FP\\\\}\\\\}|obs_g\\(|\\\\\\mathrm\\{obs\\}_g\" chapters/theory/higher_genus_modular_koszul.tex chapters/frame/guide_to_main_results.tex chapters" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:585:./audit_campaign_20260412_231034/T06_thm_D.md:271:    (?:thm:genus-universality|def:scalar-lane|delta F_g\^\{\mathrm\{cross\}\}|delta_F_g\^cross|UNIFORM-WEIGHT|ALL-WEIGHT|genus universality|Theorem D|F_1 = \kappa/24|F_1\s*=\s*\kappa/24|F_1\s*=\s*\\kappa/24|lambda_g\^\{\mathrm\{FP\}\}|obs_g\(|\\mathrm\{obs\}_g)
AGENTS.md:550:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4760,4835p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
a Poisson vertex algebra $V$ (the classical shadow of a
chiral algebra) determines a stable-graph modular deformation
complex $\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(V)$,
and the genus-$1$ obstruction is the variational modular class
$\mathrm{Mod}(V) = [\Delta_{\mathrm{cyc}} P_\Pi]$.
For the $\mathcal{W}_3$ PVA, $\mathrm{Mod}(V) = 0$
(Volume~II, Theorem~N). The lift freedom is one-dimensional,
generated by the central-parameter direction: the unique
deformation that produces the quantized $\mathcal{W}_3$
at central charge $c = c(k)$. This connects Volume~II's
PVA descent (Theorem~G) with Volume~I's shadow obstruction tower
(the degree-$2$ projection $\Theta_\cA^{\leq 2}$ recovers
the modular characteristic $\kappa(\cA)$, which is the
quantized value of the classical variational class).
\end{remark}


\section[Towards modular homotopy theory]{Towards modular homotopy theory for factorization algebras on curves}
\label{sec:modular-koszul-programme}
\index{modular Koszul duality!project}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2880,3050p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \textup{(UNIFORM-WEIGHT)}.
 At genus~$1$ this holds unconditionally for all families;
 at genus $g \geq 2$ with multi-weight algebras, the scalar
 formula fails and a cross-channel correction
 $\delta F_g^{\mathrm{cross}}$ is required
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
\item \emph{Duality.}
 Under Koszul duality, $\kappa$ satisfies a duality constraint:
 $\kappa(\cA) + \kappa(\cA^!) = 0$ for affine Kac--Moody and
 free-field algebras. For the principal $\mathcal{W}$-algebra
 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
 K_\fg \cdot \varrho(\fg)$
 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
 $m_1, \ldots, m_r$ the exponents;
 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
collab wait(call_uaomAMc3MVqmWnsVCtRDXEh2)
  receivers: 019d869e-a76e-7dc3-a786-1ee349aa7390, 019d869e-a78d-7512-a118-deb963680694, 019d869e-a881-7672-9962-79efd032b095
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '150,220p' compute/lib/curved_sc_higher_genus_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
- Cohomological grading (|d| = +1), bar uses desuspension (AP45).
- kappa(H_k) = k (AP39, AP1).
- kappa(Vir_c) = c/2 (AP48).
- Bar propagator d log E(z,w) is weight 1 (AP27).
- Deconcatenation Delta[a1|...|an] = sum_{i=0}^n [a1|...|ai] tensor [ai+1|...|an].
- Faber-Pandharipande: lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!.
- Curvature: d_fib^2 = kappa * omega_g (fiberwise), D^{(g)}^2 = 0 (corrected).
- Curved coalgebra: (C, d, Delta, m_0) with d coderivation, d^2 = m_0 insertion.

References
----------
- thm:bar-swiss-cheese (en_koszul_duality.tex): SC coalgebra structure at genus 0
- rem:sc-higher-genus (en_koszul_duality.tex): Curved SC at higher genus
- thm:quantum-diff-squares-zero (higher_genus_complementarity.tex): D^{(g)}^2 = 0
- thm:bar-modular-operad (bar_cobar_adjunction_curved.tex): FCom-algebra structure
- thm:modular-characteristic (higher_genus_modular_koszul.tex): kappa controls genus tower
- thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex): delta_F_g^cross
"""

from __future__ import annotations
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "Theorem D" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/tests/test_factorization_modular_engine.py:25:  Vol I: concordance.tex (Theorem D), configuration_spaces.tex (FM)
compute/tests/test_factorization_modular_engine.py:446:    """Verify kappa values across families match Theorem D."""
compute/lib/genus_one_bridge.py:148:    d²_B = k·ω_g (Vol I Theorem D, Vol II foundations.tex:1603).
compute/lib/celestial_holography_engine.py:32:  Vol I: concordance.tex (Theorem D, MC5)
compute/lib/celestial_holography_engine.py:62:    equals kappa(A) * omega_g by Vol I Theorem D.
compute/audit/linear_read_notes.md:1002:   Issue: the W-algebra complementarity sentence said `κ + κ^! = ρ · K (Volume I, Theorem D)`. This was (a) tautological (K := κ + κ^!), (b) used the wrong symbol ρ (should be ϱ if referring to the exponent-sum invariant), and (c) attributed to Theorem D (leading coefficient) instead of Theorem C (complementarity).
compute/tests/test_celestial_holography_engine.py:17:  Vol I: higher_genus_modular_koszul.tex, concordance.tex (Theorem D)
compute/audit/algebraic_integration/factorization_over_mg.md:14:- The vector bundle V_A on M_{1,1} exists and its first Chern class is c_1(V_A) = kappa(A) * lambda_1 (Theorem D). This captures ONE scalar from the partition function.
compute/audit/algebraic_integration/factorization_over_mg.md:65:This is Theorem D of the manuscript at genus 1. It captures exactly ONE number: kappa(A). For Heisenberg: kappa = k (NOT k/2; see AP39/AP48). For Virasoro: kappa = c/2. For affine sl_2 at level k: kappa = dim(sl_2)*(k+h^v)/(2*h^v) = 3(k+2)/4 (NOT 3k/(2(k+2))).
compute/audit/algebraic_integration/factorization_over_mg.md:413:| Does c_1(V_A) determine epsilon^c_s? | No (c_1 = kappa, one number) | Theorem D |
compute/audit/algebraic_integration/factorization_over_mg.md:442:- **Theorem D** (genus universality): obs_g = kappa * lambda_g. The scalar projection.
compute/lib/genus2_graph_sum.py:46:Theorem D (higher_genus_modular_koszul.tex): F_g(A) = kappa(A) * lambda_g^FP
compute/lib/genus2_graph_sum.py:157:    (Theorem D) relates to the A-hat genus via the exponential formula
compute/lib/genus2_graph_sum.py:684:# (C) The RELATION between them: Theorem D says F_g = kappa * lambda_g^FP
compute/lib/genus2_graph_sum.py:689:# NOT use the graph enumeration; the relation (C) is Theorem D.
compute/lib/genus2_graph_sum.py:809:    This is Theorem D: the scalar-level genus-g coefficient of the
compute/lib/genus2_graph_sum.py:926:    the one whose partition function is determined by Theorem D. The
compute/lib/genus2_graph_sum.py:927:    FIRST-PRINCIPLES DERIVATION of Theorem D goes through the Mumford
compute/lib/genus2_graph_sum.py:1000:                 'HODGE CohFT (Theorem D). The orbifold Euler characteristic '
compute/lib/genus2_obstruction_engine.py:34:This is proved by Theorem D (modular characteristic) combined with the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "modular characteristic" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
836:| `thm:genus1-universal-curvature` | `theorem` | 4159 | Universal genus-1 curvature via the modular characteristic |
1796:| `prop:symn-kappa` | `proposition` | 87 | Symmetric orbifold modular characteristic |
1817:| `prop:kappa-bps-decomposition` | `proposition` | 2871 | The BPS modular characteristic |
1965:| `thm:n2-kappa` | `theorem` | 5160 | $N=2$ modular characteristic |
2465:| `thm:ent-btz-entropy` | `theorem` | 711 | BTZ entropy from the modular characteristic |
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '1220,1300p' chapters/connections/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\index{five main theorems!E1@$E_1$ variant!Theorem A}
$\Cobar \dashv \Barch\colon
\mathsf{Alg}^{E_1}_{\mathrm{ch}} \rightleftarrows
\mathsf{Coalg}^{E_1}_{\mathrm{ch}}$.
Koszul exchange acts by $R^{-1}(z)$
\textup{(}Theorem~\textup{\ref{thm:opposite}}).
\end{theorem}

\begin{proof}
Ordered bar--cobar equivalence (\S\ref{sec:setup}) plus
opposite-duality (Theorem~\ref{thm:opposite}).
\end{proof}

\begin{theorem}[Theorem~$\mathrm{B}^{E_1}$; \ClaimStatusProvedHere]
% label removed: thm:e1-theorem-B
\index{five main theorems!E1@$E_1$ variant!Theorem B}
On the $E_1$ Koszul locus,
$\Cobar(\Barch(\cA)) \xrightarrow{\sim} \cA$.
The $E_1$ Koszul dual is
$\cA^{!,E_1} := H^*(\Barch(\cA))^\vee$.
exec
/bin/zsh -lc 'rg -n "delta_F" compute/lib/curved_sc_higher_genus_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
129:6. MULTI-WEIGHT CORRECTION: delta_F_g^cross lives in the CLOSED sector of
135:   IRRELEVANT for delta_F_g^cross.
166:- thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex): delta_F_g^cross
677:    delta_F_g^cross arises from mixed-channel boundary graphs of M_{g,n}.
684:    Therefore delta_F_g^cross lives ENTIRELY in the CLOSED sector.
750:    r"""Cross-channel correction delta_F_2(W_3) = (c + 204) / (16c).
764:        raise ValueError("c = 0 is critical; delta_F_2 diverges")
769:    r"""Decomposition of delta_F_2(W_3) into graph contributions.
772:        delta_F_2(W_3) = 3/c + 9/(2c) + 1/16 + 21/(4c)
794:    """Verify that delta_F_2^cross = 0 for uniform-weight algebras.
799:    For non-uniform weights, delta_F_2^cross is generically nonzero.
exec
/bin/zsh -lc "sed -n '120,200p' compute/lib/curved_sc_higher_genus_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "modular-characteristic" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
   because the holomorphic propagator obeys the exact Arnold relation at every
   genus (Fay trisecant identity). The expansion is:
       D^{(g)} = d_0 + sum_k t_k d_k
   where t_k are period coordinates on M_g and d_k are correction operators
   built from A-cycle integrals. Each d_k is a coderivation of Delta (period
   integrals commute with interval splitting). Therefore D^{(g)} is a
   coderivation of Delta, and D^{(g)}^2 = 0, so (B^{(g)}, D^{(g)}, Delta) is
   a genuine (non-curved) dg SC^{ch,top}-coalgebra.

6. MULTI-WEIGHT CORRECTION: delta_F_g^cross lives in the CLOSED sector of
   the SC cooperad. It arises from mixed-channel boundary graphs of M_{g,0}
   (arity 0, no marked points). The mixed sector dim (k-1)! * C(k+m, m) of
   SC^{ch,top,!} counts operations with k closed and m open inputs. The
   cross-channel correction has k = 0 (genus-g, no insertions) -- it is
   a genus-level phenomenon, not an arity-level one. The mixed sector is
   IRRELEVANT for delta_F_g^cross.

7. MODULAR EXTENSION: The genus tower {B^{(g,n)}(A)}_{2g-2+n>0} is an algebra
   over FCom (Feynman transform of commutative modular operad) by
   thm:bar-modular-operad. The SC^{ch,top} structure at each genus is
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '2700,2775p' chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
901:| `thm:modular-characteristic` | `theorem` | 2844 | Modular characteristic |
 succeeded in 51ms:
Critical string
 & $\cA = \mathrm{Vir}_{26}$, $\cA^! = \mathrm{Vir}_0$ (maximally asymmetric dual scalar sector under G4)
\end{tabular}
\end{center}


\subsection{The six-shadow synthesis}
% label removed: subsec:thqg-six-shadow

\begin{definition}[Modular cumulant transform]
% label removed: def:thqg-modular-cumulant
\index{modular cumulant transform}
The \emph{modular cumulant transform} of a gravitational input $\cA$ is
the sextuple
\begin{equation}% label removed: eq:thqg-modular-cumulant
M(\cA) = \bigl(
\hat{T}^c(\cA),\;
D_\cA,\;
\tau_\cA,\;
r_\cA(z),\;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '870,920p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
| `cor:feynman-duality-qch` | `corollary` | 7095 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 7152 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 7180 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 7230 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (264)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:mcg-equivariance-tower` | `proposition` | 237 | MCG-equivariance of the genus tower |
| `thm:genus-graded-koszul` | `theorem` | 325 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 356 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 687 | Free-field examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 729 | Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 771 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `lem:pbw-weightwise-g-module` | `lemma` | 914 | Weightwise reduction of the genus enrichment to \texorpdfstring{$\fg$}{g}-modules |
| `lem:pbw-mixed-factorization` | `lemma` | 973 | Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)} |
| `thm:pbw-genus1-km` | `theorem` | 1021 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 1339 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 1364 | PBW degeneration at all genera for Kac--Moody |
exec
/bin/zsh -lc "sed -n '640,820p' compute/lib/curved_sc_higher_genus_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

# ============================================================================
# 5. SC MIXED SECTOR DIMENSION AND CROSS-CHANNEL CLASSIFICATION
# ============================================================================

def sc_mixed_sector_dim(k: int, m: int) -> int:
    r"""Dimension of the mixed sector of the SC^{ch,top,!} cooperad.

    SC^{ch,top,!}(k closed, m open; open) has dimension (k-1)! * C(k+m, m)
    for k >= 1, m >= 0.

    This counts the number of independent mixed operations with k closed inputs,
    m open inputs, and open output.
    """
    if k < 1 or m < 0:
        return 0
    return factorial(k - 1) * comb(k + m, m)


def sc_closed_sector_dim(k: int) -> int:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "obs_g"' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: IO error for operation on raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
 succeeded in 51ms:
compute/audit/beilinson_audit_vol2_preface_wave11.md:26:- **MODERATE -- "Theorem C2" is cited as a Vol I input (line 268--277).** The preface says "Theorem~D and the scalar part~C2 of Theorem~C are tagged uniform-weight." This is AP32-compliant tagging: every occurrence of obs_g, F_g, lambda_g downstream "inherits the explicit tag from its Vol~I source." Good. No violation here -- logging as a positive finding that AP32 was properly absorbed.
compute/audit/beilinson_audit_vol2_preface_wave11.md:120:| AP32 (obs_g / F_g / lambda_g carry explicit uniform-weight tag) | lines 268--277, 537--539, 660--663 | INTEGRATED, all three occurrences tagged |
compute/audit/algebraic_integration/factorization_over_mg.md:442:- **Theorem D** (genus universality): obs_g = kappa * lambda_g. The scalar projection.
exec
/bin/zsh -lc 'head -n 120 compute/lib/rectification_delta_f2_verify_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls raeeznotes' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "lambda_g" chapters' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:
ls: raeeznotes: No such file or directory
 succeeded in 51ms:
chapters/examples/w-algebras-stable.tex:904:scalar formula $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$
chapters/examples/w-algebras-stable.tex:933:extends to all genera: $F_g(c^*) = (\alpha_2/4)\lambda_g^{\mathrm{FP}}
chapters/examples/w-algebras-stable.tex:934:= (13/2)\lambda_g^{\mathrm{FP}}$.
chapters/examples/examples-worked.tex:1362:  $\mathrm{obs}_g = \kappa\, \lambda_g$ (uniform-wt) \\
chapters/examples/examples-worked.tex:4963:  The genus tower at the scalar level is $F_g = (c/2) \cdot \lambda_g^{\mathrm{FP}}$.
chapters/examples/examples-complete-proved.tex:907:$F_g(V_k(\fg)) = \kappa(V_k(\fg)) \int_{\overline{\mathcal{M}}_g} \lambda_g$ by the algebraic-family rigidity theorem
chapters/examples/rosetta_stone.tex:58:The Heisenberg algebra~$\cH_k$ has shadow depth $r_{\max} = 2$ (class~G), so $\Theta^{\mathrm{oc}}$ terminates at degree~2. Every projection is computed in closed form: curvature $\kappa = k$, spectral $R$-matrix $R(z) = e^{k\hbar/z}$, genus tower $F_g = k\,\lambda_g^{\mathrm{FP}}$. The line category is $\cC_{\mathrm{line}} \simeq \cH_{-k}\text{-mod}$ (via $Y(\mathfrak{u}(1)) \simeq \cH_{-k}$); the derived center is the free boson bulk; the complementarity involution $k \mapsto -k$ closes the triangle (note: the Koszul dual $\cH_k^! = \Sym^{\mathrm{ch}}(V^*)$ is not $\cH_{-k}$).
chapters/examples/rosetta_stone.tex:1242:k \sum_{g \ge 1} \hbar^{2g}\, \lambda_g^{\mathrm{FP}} \cdot \omega_g,
chapters/examples/rosetta_stone.tex:1510:is $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ at all genera (Theorem~\ref{thm:ahat-lagrangian}), with the free energy
chapters/examples/rosetta_stone.tex:2029:\lambda_g^{\mathrm{FP}}$ at all genera (Volume~I, Theorem~D).
chapters/examples/rosetta_stone.tex:7034:$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Volume~I, Theorem~D\textsubscript{scal})
chapters/examples/rosetta_stone.tex:7039:\lambda_g^{\mathrm{FP}}
chapters/examples/rosetta_stone.tex:7055:$\lambda_g^{\mathrm{FP}}$ &
chapters/examples/rosetta_stone.tex:7093: \lambda_g^{\mathrm{FP}}\, x^{2g}
chapters/examples/rosetta_stone.tex:7104:$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}} \cdot
chapters/examples/rosetta_stone.tex:7106:with $\lambda_g^{\mathrm{FP}} > 0$
chapters/examples/rosetta_stone.tex:7142:coefficient $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ .
chapters/examples/rosetta_stone.tex:7241:$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ (equation~\eqref{eq:faber-pandharipande}),
chapters/connections/thqg_gravitational_s_duality.tex:1664:= K(\cA) \cdot \lambda_g^{\mathrm{FP}},
chapters/connections/thqg_gravitational_s_duality.tex:1666:\lambda_g^{\mathrm{FP}}
exec
/bin/zsh -lc "sed -n '80,140p' compute/lib/phantom_m5_koszul_dual_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
   - P(2) = 8
   - P(3) = 26
   - P(N) ~ 6N^2 for large N (quadratic growth)
   The RESIDUAL complementarity P(N) is the "irreducible anomaly"
   that cannot be cancelled by any matter content -- it is a
   topological invariant of the M5 brane stack.

5. GENUS TOWER SIGN STRUCTURE:
   For N >= 3: kappa(M5_N^!) = (2-N)^3 < 0.
   This means F_g(M5_N^!) = kappa^! * lambda_g^FP < 0 for ALL genera.
   A negative genus expansion has no perturbative interpretation as
   a physical theory.  This is the strongest argument that M5_N^!
   for N >= 3 is a "phantom" -- it does not correspond to any unitary QFT.

CONVENTIONS
===========

  AP1   kappa formulas are family-specific; never copy
  AP9   kappa(A) != c(A)/2 in general
  AP20  kappa intrinsic to A, not the physical system
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls archive' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit
metadata
misc
notes
orphaned_stubs
patches
previews
raeeznotes
raeeznotes83
raeeznotes_absorbed
references
session_artifacts
source_notes
source_tex
split_originals
standalone
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "obs_g" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/modular_trace.tex:22: %: obs_g = kappa * lambda_g is proved unconditionally at genus 1.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls archive/raeeznotes' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
common_agent_errors_archive.md
concordance.tex
configuration_spaces_archive.tex
higher_genus_modular_koszul.tex
modular_bar.py
modular_pva_quantization.tex
preface_interweaving_plan.md
raeeznotes100
raeeznotes101.md
raeeznotes102.md
raeeznotes103.md
raeeznotes104.md
raeeznotes105.md
raeeznotes105_112_beilinson_audit.md
raeeznotes105_112_master_catalogue.md
raeeznotes106.md
raeeznotes107.md
raeeznotes108.md
raeeznotes109.md
raeeznotes110.md
exec
/bin/zsh -lc 'rg -n "obs_g" compute -g"*.py"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/motivic_shadow_partition_engine.py:94:obs_g(A) = kappa(A) * lambda_g inherits this Hodge type.
compute/lib/motivic_shadow_partition_engine.py:367:    By the analysis above, the shadow class obs_g(A) = kappa(A) * lambda_g
compute/lib/multigen_universality_proof.py:194:    print("  - obs_g = kappa * lambda_g at g >= 2 for W_N, N >= 3 (OPEN)")
compute/lib/mg_kuranishi_parity_engine.py:3:FRONTIER COMPUTATION.  The current proof that obs_g = kappa * lambda_g
compute/lib/mg_kuranishi_parity_engine.py:293:    Parity argument works: obs_g = kappa * lambda_g PROVED at all genera.
compute/lib/mg_kuranishi_parity_engine.py:306:            "obs_g = kappa * lambda_g is PROVED at all genera."
compute/lib/mg_kuranishi_parity_engine.py:329:            "obs_g = kappa * lambda_g is PROVED at all genera on the "
compute/lib/mg_kuranishi_parity_engine.py:759:      - obs_g = kappa * lambda_g is PROVED at all genera.
compute/lib/multichannel_universality.py:19:obs_g = κ(A) · λ_g holds for all multi-generator algebras.
compute/lib/theorem_w3_holographic_datum_engine.py:360:def obs_genus1(c: Fraction) -> Fraction:
compute/lib/theorem_w3_holographic_datum_engine.py:370:    return obs_genus1(c)
compute/lib/theorem_w3_holographic_datum_engine.py:681:                'obs_1': obs_genus1(c),
compute/lib/bc_derived_moduli_shadow_engine.py:304:        directions to the genus-g obstruction class obs_g.
compute/lib/curvature_genus_bridge.py:200:      obs_g = kappa * lambda_g  (Hodge class)
compute/lib/curvature_genus_bridge.py:201:      (obs_g)^2 = 0  by Mumford's relation (PROVED)
compute/lib/curvature_genus_bridge.py:204:      obs_g = sum_h kappa_h * lambda_g^{(h)}
compute/lib/curvature_genus_bridge.py:219:            "obstruction_formula": "obs_g = (c/2)*lambda_g^{(2)} + (c/3)*lambda_g^{(3)}",
compute/lib/curvature_genus_bridge.py:235:            "obstruction_formula": "obs_g = sum kappa_h * lambda_g^{(h)}",
compute/lib/curvature_genus_bridge.py:244:    """Check whether (obs_g)^2 = 0 by the dimensional argument.
compute/lib/curvature_genus_bridge.py:246:    (obs_g)^2 lives in H^{4g}(M-bar_g).
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "obs_g"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/bcov_e1_shadow_engine.py:442:    Theta_A onto the scalar lane: obs_g(A) = kappa(A) * lambda_g.
compute/lib/costello_li_extended_geometries.py:528:      - Vol I convention: kappa = leading coefficient in obs_g = kappa * a_hat_g.
compute/lib/kodaira_spencer_e1_engine.py:130:algebras (dim HH_1 > 1), the all-genera formula obs_g = kappa * lambda_g
compute/lib/kodaira_spencer_e1_engine.py:501:        """obs_g(A_{KS}) = kappa * lambda_g on the scalar lane."""
compute/lib/kodaira_spencer_e1_engine.py:549:        F_g^{KS}(X) = obs_g(A_{KS}(X)) = sum_r contributions from arity r
compute/lib/kodaira_spencer_e1_engine.py:931:    F_g^{BCOV}(X) = obs_g(A_{KS}(X))
notes/research_decorated_cw_complex.md:182:classes). These are the genus-g obstructions obs_g(A_X) = kappa * lambda_g
notes/research_decorated_cw_complex.md:491:    obs_g = kappa * lambda_g, and no 3-cells are needed.
notes/research_tropical_cy_gross_siebert.md:105:The higher-genus corrections (beyond genus 0) are not captured by the classical Gross-Siebert scattering diagram. They require "punctured log GW invariants" (Gross-Siebert 2021). In the QVCG language, the genus-g obstruction obs_g receives contributions from all arities (the genus grading and the arity filtration are independent; the leading term on the uniform-weight lane is kappa * lambda_g). The full MC element Theta_A requires the "quantum" scattering diagram, which incorporates all genera.
notes/theory_qvcg_koszul.tex:630:$\obs_g(A_X) + \obs_g(A^!_X) = \kappa_{\mathrm{ch}}(A_X) \cdot \lambda_g +
compute/tests/test_kodaira_spencer_e1_engine.py:336:        """obs_g = curvature at genus g (they are the same thing)."""
notes/research_synthesis_combinatorial_datum.md:498:**Data:** The genus-g amplitudes obs_g = kappa * lambda_g, encoding the full
chapters/theory/modular_trace.tex:22: %: obs_g = kappa * lambda_g is proved unconditionally at genus 1.
compute/tests/test_s3_framing_chain_level.py:383:            obs_group = EnFromFraming.framing_obstruction_group(d)
compute/tests/test_s3_framing_chain_level.py:388:                assert obs_group == expected, f"d={d}: expected {expected}, got {obs_group}"
compute/tests/test_s3_framing_chain_level.py:392:                assert obs_trivial == (obs_group == "0"), \
compute/tests/test_s3_framing_chain_level.py:393:                    f"d={d}: trivial={obs_trivial} but group={obs_group}"
notes/research_vertex_enriched_scattering.md:606:- In the shadow obstruction tower language: the genus-g correction obs_g(A_X)
notes/physics_bv_brst_cy.tex:296: \item \textbf{Genus $g$} ($\hbar^{2g-2}$): on the uniform-weight lane, the genus-$g$ anomaly is $\obs_g(A) = \kappa_{\mathrm{ch}}(A) \cdot \lambda_g$, where $\lambda_g$ is the top Chern class of the Hodge bundle on $\overline{\cM}_{g,1}$ (for multi-weight algebras at $g \geq 2$, cross-channel corrections appear; Vol~I). The BV-BRST complex has vanishing \emph{scalar} curvature at genus $g$ if and only if $\kappa_{\mathrm{ch}}(A) = 0$.
notes/VISION.md:100:- Genus g: the full shadow obstruction tower obs_g = kappa * lambda_g
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls archive/raeeznotes/raeeznotes100' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
informal_claim_harvest.csv
label_status_conflicts.csv
master_claim_ledger_filtered.csv
provisionally_dismissed_claims.csv
red_team_summary.md
suspicious_proved_claim_dependencies.csv
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '260,330p' notes/physics_bv_brst_cy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[QME = MC for $\Theta_A$]
\label{thm:qme-mc}
Let $A = A_\cC = \Phi(\cC)$ be the quantum chiral algebra associated to a CY category $\cC$ via the functor of Vol~III. Let $\Theta_A$ be the universal Maurer--Cartan element of $A$ (Vol~I). Then the quantum master equation \eqref{eq:qme} for the BV action $S$ of the open string field theory on any brane $\cF \in \cC$ is equivalent to the Maurer--Cartan equation
\begin{equation}\label{eq:mc-equation}
 d\Theta_A + \frac{1}{2}[\Theta_A, \Theta_A] = \kappa_{\mathrm{ch}}(A) \cdot \omega
\end{equation}
for $\Theta_A$ in the chiral deformation complex of $A$.
\end{theorem}

\begin{remark}
The identification proceeds through the following dictionary:
\begin{center}
\renewcommand{\arraystretch}{1.4}
\begin{tabular}{lll}
 \textbf{BV-BRST} & \textbf{Chiral bar complex} & \textbf{Identification} \\
 \hline
 Field $\alpha \in \mathfrak{F}$ & Bar element $\alpha \in B(A)$ & Same underlying vector space \\
 BV action $S(\alpha)$ & MC element $\Theta_A$ & $S = \Tr(\Theta_A)$ \\
 CY pairing $\langle -,- \rangle$ & Factorization coproduct & $\omega_{\BV} = \Delta_B^*\omega_{\mathrm{CY}}$ \\
 $\{S,S\} = 0$ (CME) & $[\Theta_A, \Theta_A] = 0$ at genus 0 & Classical $\Ainf$ relations \\
exec
/bin/zsh -lc 'head -n 80 compute/lib/mumford_chiodo_multiweight_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Mumford-Chiodo formula for multi-weight Hodge classes at genus 2.

PURPOSE: Compute c_k(E_h) for h = 1, 2, 3 at genus 2, where
E_h = R^0 pi_* omega^{otimes h} is the bundle of weight-h differentials
on Mbar_g.  This is the crux of op:multi-generator-universality.

=== MATHEMATICAL FRAMEWORK ===

1. Mumford's GRR (1983, Thm 5.10) gives ch_k(E_h) as a polynomial in h:

   ch_k(E_h) = B_{k+1}(h)/(k+1)! * kappa_k   [interior, smooth fibers]
             + (boundary corrections from delta_irr and delta_i)

   where B_n(x) is the n-th Bernoulli polynomial.

2. The Mumford isomorphism gives c_1(E_h) = e(h) * lambda_1 where
   e(h) = 6h^2 - 6h + 1.  This is EXACT on all of Mbar_g (including boundary).

3. At genus 2, the Chow ring R^*(Mbar_2) is generated (rationally) by
   lambda_1, lambda_2, delta_irr, delta_1 subject to known relations.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "uniform-weight" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "uniform-weight" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w-algebras-frontier.tex:378:For Virasoro ($N = 2$, uniform-weight), the scalar formula
chapters/examples/w-algebras-stable.tex:903:For uniform-weight algebras (Virasoro, $N = 2$) the
chapters/examples/w-algebras-stable.tex:932:For $N = 2$ (Virasoro, uniform-weight), the scalar formula
chapters/frame/preface.tex:290:(\textsc{uniform-weight} at $g \ge 2$, unconditional at $g = 1$;
chapters/frame/preface.tex:650:Theorem~D, \textsc{uniform-weight} at $g \ge 2$, with
chapters/frame/preface.tex:663:coefficients (\textsc{uniform-weight}): $F_1 = \kappa/24$
chapters/frame/preface_trimmed.tex:363:carry uniform-weight scope at $g \ge 2$, with a cross-channel
chapters/theory/foundations.tex:847:uniform-weight lane, Theorem~D of Volume~I) and the
chapters/theory/factorization_swiss_cheese.tex:847:(on the uniform-weight lane). The MC equation
chapters/connections/modular_pva_quantization_frontier.tex:1774:genus $0$ (spherical slab), uniform-weight, and on the locus
chapters/connections/modular_pva_quantization_frontier.tex:1781:conjectural at $g\ge 1$, and the uniform-weight restriction on
chapters/connections/conclusion.tex:2091:holds for uniform-weight modular Koszul algebras. For multi-weight
chapters/connections/thqg_ht_bbl_extensions.tex:933:uniform-weight scalar package, the genus expansion is controlled by
chapters/connections/thqg_fredholm_partition_functions.tex:1532:$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ \textup{(}uniform-weight\textup{)} is verified
chapters/connections/thqg_fredholm_partition_functions.tex:1585: On the proved uniform-weight scalar lane this specializes to
chapters/connections/thqg_fredholm_partition_functions.tex:1600:algebras on the uniform-weight scalar lane.
chapters/connections/thqg_fredholm_partition_functions.tex:1608:uniform-weight scalar lane
chapters/connections/thqg_fredholm_partition_functions.tex:1633:On the proved uniform-weight Gaussian lane,
chapters/connections/thqg_fredholm_partition_functions.tex:2528:\textup{(}uniform-weight\textup{)}
chapters/connections/3d_gravity.tex:330:\label{rem:uniform-weight-thesis}
exec
/bin/zsh -lc "sed -n '1,120p' compute/tests/test_theorem_genus2_w3_partition_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Tests for genus-2 shadow free energy of W_3.

Multi-path verification of the first non-affine genus-2 computation.
W_3 has generators T (weight 2), W (weight 3) -- multi-weight, so
the scalar formula F_g = kappa * lambda_g FAILS at genus >= 2.

The full decomposition (thm:multi-weight-genus-expansion):
  F_2(W_3) = kappa * lambda_2^FP + delta_F_2^cross
  where delta_F_2^cross = (c + 204)/(16c).

AP1: kappa(W_3) = 5c/6, NOT c/2.
AP10: cross-family consistency prevents hardcoded wrong values.
AP39: kappa != c/2 for non-Virasoro families.

Ground truth:
  thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex),
  prop:universal-gravitational-cross-channel,
  thm:propagator-variance, multichannel_genus2.py,
  theorem_thm_d_multiweight_frontier_engine.py.
"""
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2950:\index{Lagrangian self-intersection!Theorem D}
3031:\index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
3032:\index{Hodge bundle!alternative proof of Theorem D}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2840,3005p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2840	class~$\Theta_\cA$ require data beyond~$\kappa$;
  2841	see Definition~\ref{def:full-modular-package}).
  2842	
  2843	\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
  2844	\label{thm:modular-characteristic}
  2845	\index{modular characteristic theorem|textbf}
  2846	\index{kappa@$\kappa$!as first characteristic number|textbf}
  2847	\textup{[}Regime: curved-central
  2848	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  2849	
  2850	Let $\cA$ be a modular Koszul chiral algebra
  2851	(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
  2852	characteristic package
  2853	(Definition~\ref{def:scalar-modular-package}) is controlled by one
  2854	number, the genus-$1$ curvature coefficient
  2855	$\kappa(\cA) \in \mathbb{C}$. More precisely:
  2856	
  2857	\begin{enumerate}[label=\textup{(\roman*)}]
  2858	\item \emph{Universality.}
  2859	 \begin{enumerate}[label=\textup{(\alph*)}]
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "modular characteristic" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
49:the modular characteristic $\kappa(\cA)$ at degree~$2$,
2363:\item Theorem~D \textup{(}modular characteristic
2609:\begin{definition}[Scalar modular characteristic package]
2612:\index{modular characteristic package!scalar|textbf}
2615:\emph{scalar modular characteristic package} of~$\cA$ consists of:
2639:\begin{definition}[Full modular characteristic package]
2641:\index{modular characteristic package!full|textbf}
2649:\emph{full modular characteristic package} is the quintuple
2668: \emph{scalar modular characteristic}
2807:\begin{remark}[The modular characteristic hierarchy]
2810:\index{modular characteristic!hierarchy|textbf}
2845:\index{modular characteristic theorem|textbf}
2962:\index{modular characteristic theorem!as integrability condition}%
2994:\index{modular characteristic theorem!model presentation}
3760:$\Theta_\cA$: the modular characteristic $\kappa$ at degree~$2$,
4345:\item \emph{Theorem~D} (modular characteristic~$\kappa$):
4914:(level equals modular characteristic). For rank-$d$ lattice VOAs,
4958:\index{modular characteristic!W3 channel decomposition@$\cW_3$ channel decomposition}
4960:$W$ \textup{(}weight~$3$\textup{)}, the modular characteristic
8477:The non-scalar modular characteristic package
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/holomorphic_topological.tex | sed -n '150,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   150	\begin{equation}\label{eq:ht-theta}
   151	\Theta_{\cA_T}
   152	\;:=\; D_{\cA_T} - d_0
   153	\;\in\; \MC(\gAmod)
   154	\end{equation}
   155	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}
   156	satisfies
   157	$D_{\cA_T}\,\Theta_{\cA_T}
   158	+ \tfrac{1}{2}[\Theta_{\cA_T},\Theta_{\cA_T}] = 0$
   159	because $D_{\cA_T}^{\,2} = 0$. The finite-order projections
   160	$\Theta_{\cA_T}^{\leq r}$ are the shadow obstruction tower
   161	\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower}}\textup{)};
   162	the scalar shadow on the uniform-weight locus is
   163	$\kappa(\cA_T) \cdot \lambda_g$
   164	\textup{(}Theorem~\textup{\ref{thm:genus-universality}};
   165	uniform-weight, with multi-weight correction
   166	$\delta F_g^{\mathrm{cross}}$
   167	off this locus per
   168	Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
   169	\end{theorem}

wait(call_uaomAMc3MVqmWnsVCtRDXEh2) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2330,2405p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bigrading).
\end{proof}

\begin{theorem}[Three-tier logical architecture of
 modular Koszul duality;
 \ClaimStatusProvedHere]\label{thm:three-tier-architecture}
\index{three-tier architecture|textbf}
\index{modular Koszul duality!logical architecture|textbf}
The modular Koszul engine decomposes into three tiers
of decreasing generality and increasing analytic
content. At each tier, the listed results follow
from the stated input alone.

\smallskip\noindent
\textbf{Tier~0} \textup{(topological input:
$D_\cA^2 = 0$)}.
\begin{enumerate}[label=\textup{(0.\arabic*)}]
\item The universal MC element
 $\Theta_\cA := D_\cA - \dzero
 \in \MC(\gAmod)$ exists at all genera
thinking
**Summarizing relevant delta F cross verification tests and engines**

I'll gather key files and tests that verify delta F cross formulas, multi-weight corrections, and uniform weight cases across genera. I plan to detail main engines handling these corrections and mention tests focusing on formula accuracy, positivity of cross terms, and support from Hodge classes, ensuring I highlight minimal but essential surfaces and references.
exec
/bin/zsh -lc "sed -n '450,540p' compute/tests/test_theorem_genus4_multiweight_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        """Growth ratios F4/F3 and F3/F2 are well-defined and positive."""
        results = cross_channel_growth()
        for c_val, data in results.items():
            assert data['ratio_F3_F2'] is not None and data['ratio_F3_F2'] > 0
            assert data['ratio_F4_F3'] is not None and data['ratio_F4_F3'] > 0


# ============================================================================
# PATH 15: Cross-genus lambda_g^FP consistency
# ============================================================================

class TestCrossGenusConsistency:
    """Cross-genus consistency of lambda_g^FP and the correction tower."""

    def test_genus2_baseline(self):
        """delta_F_2(W_3) = (c+204)/(16c) at c=50."""
        c = Fraction(50)
        assert delta_F2_W3(c) == Fraction(254, 800)

    def test_genus3_baseline(self):
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "C2" chapters/connections/holomorphic_topological.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "uniform-weight" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
489:uniform-weight algebras
2712:\label{def:uniform-weight-lane}
2714:\index{uniform-weight lane|see{scalar lane}}
2716:\emph{uniform-weight lane} (or \emph{scalar lane}) if every
2864: \textup{(}uniform-weight; unconditional at $g = 1$\textup{)}.
2916:trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
2933:uniform-weight algebras. For multi-generator algebras
3012:$\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
3033:There is a second proof route to the uniform-weight clause of
3058:$R^0\pi_*\omega_\pi^{\otimes h}$ do not enter on the uniform-weight
3084:This is a second proof route for the uniform-weight clause of
3162:\textup{[}Regime: curved-central; uniform-weight at $g \geq 2$.\textup{]}
3226:asserted at~$g \geq 2$ is uniform-weight (scalar lane); for
3438:On the uniform-weight locus, the planted-forest correction
3587: $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
3620:On the proved uniform-weight lane, the same theorem upgrades this to
3636:on the proved uniform-weight lane via the explicit completion
3806: $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
4050:On the proved uniform-weight lane, the same theorem upgrades this to
4251:only on the proved uniform-weight lane. That collapse concerns the \emph{parametrization} of the minimal
codex
The initial repository scans are still running. While they finish, I’ve confirmed the applicable workflows: split the result into proved core, compute-backed evidence, conditional bridge, and conjectural extension, then state the blocker for condition removal explicitly in the remark.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n "C_2"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w-algebras-stable.tex:1709:& \textbf{$\mathfrak{sp}_4$ (type $C_2$)} \\
chapters/examples/w-algebras-w3.tex:293: + C_2(\ell,\mu)\,\Lambda
chapters/examples/examples-worked.tex:3766:  & $C_2(\mathrm{adj})$
chapters/examples/examples-worked.tex:3786:Here $C_2(\mathrm{adj})$ is the eigenvalue of the quadratic
chapters/examples/examples-worked.tex:3788:normalised so that $C_2(\mathrm{adj}) = h^\vee$ for any
compute/symmetric_point_catalan.py:313:  r=3 (k=7):  C_2 = 2
chapters/examples/rosetta_stone.tex:5465: using $\Omega_{12} = \tfrac{1}{2}(C_2^{\mathrm{total}}
chapters/examples/rosetta_stone.tex:5466: - C_2^{(1)} - C_2^{(2)})$ with $C_2^{\mathrm{adj}} = 2$
chapters/examples/rosetta_stone.tex:5712:(C_2^{\mathrm{total}} - \sum_i C_2^{(i)})$
chapters/examples/rosetta_stone.tex:5713:with $C_2^{\mathrm{adj}} = 2$).
chapters/connections/spectral-braiding-core.tex:1322:$\mathfrak{so}_5 \cong B_2$ and $\mathfrak{sp}_4 \cong C_2$,
chapters/connections/spectral-braiding-core.tex:1326:\begin{computation}[$B_2$ and $C_2$ collision residues;
chapters/connections/spectral-braiding-core.tex:1381:The Langlands dual $\fg^L = \mathfrak{sp}_4$ (type~$C_2$)
chapters/connections/spectral-braiding-core.tex:1403: Hence $k^L = 2k$ for $B_2 \to C_2$.
chapters/connections/spectral-braiding-core.tex:1407: r^{C_2}(z)
chapters/connections/spectral-braiding-core.tex:1409: 2k\,\Omega^{C_2}/z,
chapters/connections/spectral-braiding-core.tex:1411:with $\Omega^{C_2}$ the Casimir of $\mathfrak{sp}_4$ in
chapters/connections/spectral-braiding-core.tex:1441:$\Omega^2 = C_2(\fg)\,\mathrm{id}$ on irreducible representations
chapters/connections/spectral-braiding-frontier.tex:807:2 \cdot C_2(\mathrm{adj})
chapters/connections/spectral-braiding-frontier.tex:810:where $C_2(\mathrm{adj}) = 2h^\vee = 4$ for
collab wait(call_rjSmY3um8rdRwP0mjYVcXQEb)
  receivers: 019d869e-a76e-7dc3-a786-1ee349aa7390, 019d869e-a78d-7512-a118-deb963680694, 019d869e-a881-7672-9962-79efd032b095
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2690,2755p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item \emph{Dualizable}: the duality $\cA \leftrightarrow \cA^!$
 acts on each component
 ($\kappa + \kappa' = K$, $\Delta_{\cA^!}$ determined by
 $\Delta_{\cA}$, etc.);
\item \emph{Modular}: compatible with clutching and
 boundary degeneration on~$\overline{\mathcal{M}}_{g,n}$;
\item \emph{Non-scalar}: $\kappa(\cA)$ is only the first shadow;
 the full package contains strictly more information
 (cf.\ the spectral data of level~(2) in
 Remark~\ref{rem:characteristic-hierarchy}).
\end{enumerate}

\smallskip\noindent
The cyclic $L_\infty$-algebra $\Defcyc(\cA)$ is constructed
by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
(Theorems~\ref{thm:universal-MC}
and~\ref{thm:universal-theta}).
\end{definition}

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "multi-weight" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2729:universally. For general multi-weight algebras at $g \geq 2$,
2731:Theorem~\ref{thm:multi-weight-genus-expansion}; all free-field algebras are exact exceptions by
2882: at genus $g \geq 2$ with multi-weight algebras, the scalar
4979:\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
5744:general multi-weight algebras the scalar formula receives the
5746:\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)},
8183:multi-weight families with simple Lie symmetry, parts
8660:for multi-weight $\mathcal{W}$-algebras, sharp periods
8726:uniform-weight scalar lane. For general multi-weight
8761:general multi-weight families, including principal
8813: general for multi-weight families.
9196:tautological-purity gap for multi-weight families.
9385:multi-weight examples.
10043:for arbitrary multi-weight families.
10060:For arbitrary multi-weight families, only the genus-$1$ comparison is
13246:uniform-weight lane; for multi-weight algebras at $g \geq 2$,
13250:(Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}).
14947:multi-weight one-channel families, must
22276:\label{thm:multi-weight-genus-expansion}
22279:\index{multi-weight genus expansion|textbf}%
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C_2" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2554:Rationality, $C_2$-cofiniteness, and semisimple Zhu algebra remain
3064:\item \emph{$C_2$-cofiniteness}: orthogonal to Koszulness; Koszul duality maps $C_2$-cofinite to non-$C_2$-cofinite.
3936:Kac--Moody algebras: $B_2 = \mathfrak{so}(5)$, $C_2 = \mathfrak{sp}(4)$,
3944:(10 for~$B_2$, 10 for~$C_2$, 14 for~$G_2$).
3945:Langlands duality $B_2 \leftrightarrow C_2$ preserves

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '22260,22460p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Collecting all such graphs gives the restriction to the
non-separating divisor
$\delta_{\mathrm{irr}} =
\xi_{\mathrm{nsep}}(\overline{\cM}_{g-1,n+2})$,
yielding axiom~(iii).

Axioms~(i)--(iii) make $(\Omega^\cA, V, \eta)$ a CohFT
without unit in the sense of
Pandharipande--Pixton--Zvonkine. The unit axiom
$\Omega_{0,3}(\mathbf{1}, v, w) = \eta(v,w)$ holds when the
vacuum vector of~$\cA$ lies in~$V$ and $\ell_2^{(0)}$
restricts to a unital multiplication on~$V$ (satisfied for
all standard families).
\end{proof}

\begin{theorem}[Multi-weight genus expansion; \ClaimStatusProvedHere]
\label{thm:multi-weight-genus-expansion}
\label{thm:multi-generator-universality}
\index{multi-generator obstruction!genus expansion|textbf}%
\index{multi-weight genus expansion|textbf}%
thinking
**Summarizing tests and engine coverage for cross-channel positivity**

I’m gathering all relevant files and tests related to cross-channel delta_F_g positivity, especially focusing on W3 multi-weight formulas and their verification in various `compute/lib` engines and `compute/tests`. There’s substantial coverage for genus 2-4 W3 cases, but no general formula or engine beyond those, revealing gaps in higher genus and multi-weight general delta_F_g^cross computations. I’m noting key files, specific tests verifying positivity and formula correctness, and identifying limited generality beyond W3, plus absence of a broad multi-channel obstruction computation. This builds a solid summary highlighting current coverage and missing pieces.
exec
/bin/zsh -lc 'rg -n "delta_F" compute/lib/compute/tests/test_theorem_genus4_multiweight_engine.py' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: compute/lib/compute/tests/test_theorem_genus4_multiweight_engine.py: IO error for operation on compute/lib/compute/tests/test_theorem_genus4_multiweight_engine.py: No such file or directory (os error 2)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3000,3085p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\sum_{g \ge 1} F_g x^{2g}
=
\kappa\cdot(\hat{A}(ix)-1)
\]
The bar-intrinsic shadow tower is the common source.
The first implication is the scalar-trace identification of
Theorem~\ref{thm:genus-universality}; the second is the downstream
GRR/family-index identification of the same scalar series on the
virtual bar family. Theorem~\ref{thm:family-index} is therefore the
index-theoretic reformulation of the scalar output, not the
load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
\emph{Step~B} (M-level): universality
$\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
unconditional at $g{=}1$,
Theorem~\ref{thm:genus-universality}); generating function via
Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
duality $\kappa+\kappa'=\varrho\cdot K$; additivity
\textup{(}Corollary~\textup{\ref{cor:kappa-additivity}}\textup{)};
matter-ghost cancellation
\textup{(}Theorem~\textup{\ref{thm:anomaly-koszul}}\textup{)}.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem C2" -n chapters' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '1100,1145p' compute/lib/theorem_vicedo_envelope_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
        genus_2_cross_channel=g2_ext.delta_f2_cross,
    )


# ---------------------------------------------------------------------------
# 14. Obstruction analysis: what blocks genus extension
# ---------------------------------------------------------------------------

@dataclass
class ObstructionAnalysis:
    r"""Analysis of the precise obstruction to extending Vicedo's construction
    to all genera.

    Vicedo constructs the genus-0 prefactorization algebra.  The obstruction
    to extending to genus g is:
      obs_g(A) = kappa(A) * lambda_g (for uniform-weight algebras)
      obs_g(A) = kappa(A) * lambda_g + delta_F_g^cross (for multi-weight)

    The shadow obstruction tower IS the systematic expansion of this
    obstruction.  At each arity r, the shadow Theta^{<=r} captures the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C2" -n chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
3595:This is Theorem~\ref{thm:master-theta} (MC2).
3596:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3743:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3769:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3772:\index{MC2!bar-intrinsic proof}
3773:\index{MC2!full generality}
3830:\begin{remark}[Scope of MC2 in this chapter]
3831:\index{MC2!coinvariant scope}
3832:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4104:\index{MC2!foundational dependency chain}
4158:\index{Kontsevich--Soibelman!alternative construction of MC2}
4228:installed, it furnishes an alternative proof path to MC2.
4233:\index{MC2!bar-intrinsic perspective}
4234:\index{MC2!two regimes}
4235:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4397:\index{MC2!functoriality|textbf}
4988:\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
4998:MC2-1 resolved for KM by Theorem~\ref{thm:mc2-1-km}.
5070: of the MC2 package at Step~1.
5089: All MC2 Step-$1$--$3$ computations are verified for
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~C" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2382:\item Theorem~C \textup{(}complementarity\textup{)}
4374:\item \emph{Theorem~C} (complementarity):
4382: and the Kodaira--Spencer identification from Theorem~C.
4390:$\;\Longrightarrow\;$ Theorem~C.
4492:expression of Theorem~C: the two dual sides
10098:Theorem~C
13313:(IV) from Theorem~A(ii), Theorem~C, and the shadow homotopy
14847:Theorem~C is the averaged form of complementarity in the ordered
30868:\item \emph{Complementarity}: the Lagrangian decomposition of Theorem~C is the polarization into $\cA$-side and $\cA^!$-side components (under perfectness hypotheses).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4350,4420p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (Corollary~\ref{cor:shadow-extraction}(i));
\item the shadow obstruction tower $\Theta_\cA^{\leq r}$
 at all finite degrees, with the all-degree master equation
 $\nabla_H(\operatorname{Sh}_r) + \mathfrak{o}^{(r)} = 0$
 holding unconditionally
 (Theorem~\ref{thm:recursive-existence}).
\end{itemize}

\smallskip\noindent
\emph{Tier~2: consequences of~$D_\cA^2 = 0$ plus PBW
concentration at all genera.}
The following require~\ref{MK:koszul} (genus-$0$
Koszulity) plus~\ref{MK:modular} (PBW concentration at all
genera). For the standard landscape,~\ref{MK:modular}
\emph{follows from}~\ref{MK:koszul} by PBW propagation
(Theorem~\ref{thm:pbw-propagation}), so no independent
verification of~\ref{MK:modular} is needed:
\begin{itemize}
\item \emph{Theorem~B at genus~$g \geq 1$}
 (bar-cobar inversion): proved by induction on~$g$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2340,2385p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2340	content. At each tier, the listed results follow
  2341	from the stated input alone.
  2342	
  2343	\smallskip\noindent
  2344	\textbf{Tier~0} \textup{(topological input:
  2345	$D_\cA^2 = 0$)}.
  2346	\begin{enumerate}[label=\textup{(0.\arabic*)}]
  2347	\item The universal MC element
  2348	 $\Theta_\cA := D_\cA - \dzero
  2349	 \in \MC(\gAmod)$ exists at all genera
  2350	 \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
  2351	\item The shadow obstruction tower
  2352	 $\Theta_\cA^{\leq r}$ exists at all finite degrees,
  2353	 with $\Theta_\cA = \varprojlim_r
  2354	 \Theta_\cA^{\leq r}$
  2355	 \textup{(Theorem~\ref{thm:recursive-existence})}.
  2356	\item The shadow algebra
  2357	 $\cA^{\mathrm{sh}} =
  2358	 H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ carries
  2359	 a graded Lie bracket with
exec
/bin/zsh -lc 'rg -n "delta_F_2_cross" compute/tests/test_pva_deformation_comparison_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1314:        assert obs["delta_F_2_cross"] == Fraction(0)
1322:            assert obs["delta_F_2_cross"] == Fraction(0)
1331:        assert obs["delta_F_2_cross"] == Fraction(0)
1350:            assert obs["delta_F_2_cross"] == expected
1351:            assert obs["delta_F_2_cross"] > 0  # Strictly positive
1367:        assert obs["delta_F_2_cross"] == expected
1561:        assert bridge["genus_2"]["delta_F_2_cross"] > 0
1703:            assert obs["delta_F_2_cross"] > 0, f"delta_F_2 not positive at c={c}"
1718:            path2 = obs["delta_F_2_cross"]
1727:            delta = obs["delta_F_2_cross"]
1736:        delta = obs["delta_F_2_cross"]
1771:        assert sl2_obs["delta_F_2_cross"] == Fraction(0)
1774:        assert w3_obs["delta_F_2_cross"] != Fraction(0)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '24870,24895p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '1,140p' chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 24870	\centering
 24871	\begin{tikzpicture}[x=1.8cm, y=1.6cm]
 24872	% ---- Column headers ----
 24873	\node[font=\footnotesize\scshape] at (0,4.3) {codim $0$};
 24874	\node[font=\footnotesize\scshape] at (2,4.3) {codim $1$};
 24875	\node[font=\footnotesize\scshape] at (5,4.3) {codim $2$};
 24876	\node[font=\footnotesize\scshape] at (8,4.3) {codim $3$};
 24877	%
 24878	% ---- A: Smooth genus-2 ----
 24879	\node[gv] (A) at (0,3.4) {$2$};
 24880	\node[font=\scriptsize, below=2pt] at (A.south)
 24881	 {$\mathrm{A}$\;\tiny$|\mathrm{Aut}|\!=\!1$};
 24882	%
 24883	% ---- B: delta_irr (genus-1, one self-loop) ----
 24884	\node[gv] (B) at (1.5,3.4) {$1$};
 24885	\draw[sloop] (B) to[out=50,in=130,looseness=6] (B);
 24886	\node[font=\scriptsize, below=2pt] at (B.south)
 24887	 {$\mathrm{B}:\;\delta_{\mathrm{irr}}$\;\tiny$|\mathrm{Aut}|\!=\!2$};
 24888	%
 24889	% ---- C: delta_1 (two genus-1, one bridge) ----
 succeeded in 50ms:
\chapter{Modular Koszul Duality and CY Geometry}
\label{ch:modular-koszul-bridge}

A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.


%% ===================================================================
%% SECTION 1: CY modular convolution algebra
%% ===================================================================

\section{The modular convolution algebra for CY categories}
\label{sec:modular-conv-cy}

Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d$ and let $A_\cC = \Phi(\cC)$ denote the image under the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral} (Theorem~CY-A is proved for $d = 2$; $d = 3$ is the Vol~III programme, AP-CY6). The bar coalgebra $B(A_\cC)$ is a factorization coalgebra on $\Ran(C)$ for a fixed smooth projective curve $C$, with bar differential $d_B = d_1 + d_2 + \cdots$ where $d_k$ lowers bar degree by $k - 1$.

\begin{definition}[CY modular convolution algebra]
\label{def:cy-modular-convolution}
The \emph{CY modular convolution algebra} of the pair $(B(A_\cC), A_\cC)$ is the graded vector space
\[
 \mathrm{Conv}_{\mathrm{str}}\bigl(B(A_\cC), A_\cC\bigr)
exec
/bin/zsh -lc "sed -n '1300,1375p' compute/tests/test_pva_deformation_comparison_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


# =========================================================================
# PART 17: GENUS-2 QUANTIZATION OBSTRUCTION TESTS
# =========================================================================

class TestGenus2Obstructions:
    """Tests for genus-2 quantization obstructions."""

    def test_heisenberg_genus2(self):
        k = Fraction(3)
        obs = quantization_obstruction_genus2("heisenberg", k=k)
        kap = kappa_heisenberg(k)
        assert obs["F_2_scalar"] == kap * Fraction(7, 5760)
        assert obs["delta_F_2_cross"] == Fraction(0)
        assert obs["uniform_weight"] is True

    def test_sl2_genus2_uniform_weight(self):
        """sl_2 is uniform-weight (all weight 1): no cross-channel."""
        for k_int in [1, 3, 5]:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C0" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

thinking
**Summarizing verification and references**

I’m preparing to mention the key tests verifying multi-weight cross positivity and delta cross in various test files, and noting the gaps where no general computing engines exist beyond certain cases. I'll include general results limited to W3 and genus 4, mention known formulas and observations, and highlight differences between uniform and multi-weight cases. I plan to gather precise line numbers from files like `curved_sc_higher_genus_engine.py` using commands like `nl -ba` to ensure accurate referencing in a final detailed summary, which will also cover these points and include suggestions, while noting that no code edits were made.
exec
/bin/zsh -lc "nl -ba compute/lib/curved_sc_higher_genus_engine.py | sed -n '110,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 74ms:
   110	   - d^2 = m_0 (the curvature) is the UNIQUE element such that d^2(x) = m_0 * x
   111	     for the coaugmentation coideal.
   112	   - The structure is governed by the CURVED bar complex formalism
   113	     (Positselski, "Two kinds of derived categories, Koszul duality, and
   114	     comodule-contramodule correspondence").
   115	   The SC^{ch,top} structure persists in the CURVED sense: (B^{(g)}, d, Delta)
   116	   is a curved SC^{ch,top}-coalgebra.
   117	
   118	5. THE CORRECTED DIFFERENTIAL D^{(g)}: Built from the holomorphic propagator
   119	   h_{ij} = partial_{z_i} log E(z_i, z_j) (prime form). Satisfies D^{(g)}^2 = 0
   120	   because the holomorphic propagator obeys the exact Arnold relation at every
   121	   genus (Fay trisecant identity). The expansion is:
   122	       D^{(g)} = d_0 + sum_k t_k d_k
   123	   where t_k are period coordinates on M_g and d_k are correction operators
   124	   built from A-cycle integrals. Each d_k is a coderivation of Delta (period
   125	   integrals commute with interval splitting). Therefore D^{(g)} is a
   126	   coderivation of Delta, and D^{(g)}^2 = 0, so (B^{(g)}, D^{(g)}, Delta) is
   127	   a genuine (non-curved) dg SC^{ch,top}-coalgebra.
   128	
   129	6. MULTI-WEIGHT CORRECTION: delta_F_g^cross lives in the CLOSED sector of
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "C2" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/curved_sc_higher_genus_engine.py | sed -n '640,820p'" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
55: C2: shifted-symplectic/BV upgrade conditional on the
58: & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
346: C2 is the shifted-symplectic/BV upgrade, conditional on the
1377: status; the proved core (Theorems~A--D,\,H, MC2) is unaffected.
1382:is MC2 (proved by the bar-intrinsic construction,
1679:\item \emph{Zero risk}: Theorems~A--D,\,H, MC2 bar-intrinsic
1862:\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
2012:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
2935: & bar-intrinsic MC (MC2) \\[2pt]
3339:MC2 & $D^2 = 0$ & Bar-intrinsic MC element: $\Theta_\cA := D_\cA - d_0$
4805: & Lagrangian complementarity; C2 shifted-symplectic upgrade & C2: \textbf{Conditional} & \ref{thm:quantum-complementarity-main}, \\
5211:Component~(5) is the principal open structural problem (MC2 is proved
5407:ingredients already supported by the current MC2 surface: the
5952:(Part of the MC2 theorem package; the universal class exists by
9724:& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
 succeeded in 52ms:
   640	
   641	# ============================================================================
   642	# 5. SC MIXED SECTOR DIMENSION AND CROSS-CHANNEL CLASSIFICATION
   643	# ============================================================================
   644	
   645	def sc_mixed_sector_dim(k: int, m: int) -> int:
   646	    r"""Dimension of the mixed sector of the SC^{ch,top,!} cooperad.
   647	
   648	    SC^{ch,top,!}(k closed, m open; open) has dimension (k-1)! * C(k+m, m)
   649	    for k >= 1, m >= 0.
   650	
   651	    This counts the number of independent mixed operations with k closed inputs,
   652	    m open inputs, and open output.
   653	    """
   654	    if k < 1 or m < 0:
   655	        return 0
   656	    return factorial(k - 1) * comb(k + m, m)
   657	
   658	
   659	def sc_closed_sector_dim(k: int) -> int:
exec
/bin/zsh -lc "nl -ba compute/lib/rectification_delta_f2_verify_engine.py | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
     1	r"""Independent verification engine for delta_F_2^{grav}(W_N).
     2	
     3	ADVERSARIAL RED-TEAM VERIFICATION of the claim:
     4	
     5	    delta_F_2^{grav}(W_N, c) = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c)
     6	
     7	This engine is built FROM SCRATCH with ZERO imports from the multi-weight
     8	cross-channel engine. Every computation is independent.
     9	
    10	MATHEMATICAL SETUP
    11	==================
    12	
    13	The genus-2 stable graph sum for the gravitational-only W_N Frobenius
    14	algebra computes:
    15	
    16	    F_2(W_N, c) = sum_{Gamma} (1/|Aut(Gamma)|)
    17	                  * sum_{sigma: E(Gamma) -> {2,3,...,N}} A(Gamma, sigma)
    18	
    19	where A(Gamma, sigma) is the product of:
    20	  - Propagators: prod_e  w(sigma(e)) / c   where w(j) = conformal weight j
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '40,80p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
 & Strict quasi-isomorphism on the Koszul locus
 $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
 \textup{(}Thms~\ref{thm:higher-genus-inversion},
 \ref{thm:bar-cobar-inversion-qi}\textup{)}; off the locus,
 the counit is an unconditional coderived coacyclic-equivalence,
 promoted back to an ordinary quasi-isomorphism on collapse loci
 & \ClaimStatusProvedHere \\
\textbf{C} & Complementarity
 & C0: coderived fiber-center identification unconditional,
 ordinary-derived only on the flat perfect locus
 \textup{(}Thm~\ref{thm:fiber-center-identification}\textup{)}.
 C1: homotopy eigenspace decomposition for all~$g$, with
 duality/Lagrangian only for $g \geq 1$ and genus~$0$
 treated separately
 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)}.
 C2: shifted-symplectic/BV upgrade conditional on the
 uniform-weight perfectness package
 \textup{(}Thm~\ref{thm:shifted-symplectic-complementarity}\textup{)}
 & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
\textbf{D} & Modular characteristic
exec
/bin/zsh -lc "nl -ba compute/lib/theorem_vicedo_envelope_engine.py | sed -n '1105,1145p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1105	# 14. Obstruction analysis: what blocks genus extension
  1106	# ---------------------------------------------------------------------------
  1107	
  1108	@dataclass
  1109	class ObstructionAnalysis:
  1110	    r"""Analysis of the precise obstruction to extending Vicedo's construction
  1111	    to all genera.
  1112	
  1113	    Vicedo constructs the genus-0 prefactorization algebra.  The obstruction
  1114	    to extending to genus g is:
  1115	      obs_g(A) = kappa(A) * lambda_g (for uniform-weight algebras)
  1116	      obs_g(A) = kappa(A) * lambda_g + delta_F_g^cross (for multi-weight)
  1117	
  1118	    The shadow obstruction tower IS the systematic expansion of this
  1119	    obstruction.  At each arity r, the shadow Theta^{<=r} captures the
  1120	    contribution of r-vertex graphs to the genus-g amplitude.
  1121	
  1122	    WHAT BLOCKS THE EXTENSION:
  1123	    1. At genus 0: nothing blocks.  The Nishinaka-Vicedo envelope exists.
  1124	    2. At genus 1: kappa * lambda_1 is the obstruction.  This is UNIVERSAL

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "multi-weight" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
505:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
543:**pole/weight** (AP19, AP21, AP27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.
865:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
thinking
**Summarizing cross-volume references**

I'll organize key file and line references across Volumes I, II, and III that mention uniform weight, Theorem D, C2, and multi-weight cross-channel corrections, highlighting variations in wording and noting that edits to these concepts would need consistent updates across these cross-referenced sections.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba CLAUDE.md | sed -n '490,520p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   490	**FM32. RTT sign convention dependence.** The level-1 RTT commutation relation sign depends on the R-matrix convention: additive R(u) = uI + Psi*P gives [t_{ij}, t_{kl}] = Psi(delta_{il} t_{kj} - delta_{kj} t_{il}); Molev's 1-P/u convention gives the opposite sign. Counter: always state which R-matrix convention before writing RTT relations.
   491	
   492	**FM33. Quantum determinant column ordering.** The central quantum determinant qdet T(u) for Y(gl_N) uses DECREASING column index ordering in the column determinant (j=N-1 leftmost, j=0 rightmost). The "left-to-right in j" ordering (j=0 leftmost) is NOT central at N >= 3 (coincidentally agrees at N=2). Counter: always specify column ordering when writing qdet formulas. Cite Molev Theorem 1.6.4 for the correct convention.
   493	
   494	**FM34. Heat equation prefactor diagonal vs off-diagonal.** The genus-g heat equation d/dOmega_{ab} Theta = coefficient * d^2/(dz_a dz_b) Theta has prefactor 1/(4πi) for a=b (diagonal) and 1/(2πi) for a≠b (off-diagonal). The factor of 2 comes from the symmetric matrix chain rule: d/dOmega_{aa} = (1/2) d/d(Omega_{aa} as independent variable). Writing 1/(2πi) uniformly is a notational convention that absorbs the factor into the matrix derivative, but produces wrong numerical results when Omega_{aa} is treated as an independent variable in computations.
   495	
   496	**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."
   497	
   498	## Theorem Status
   499	
   500	| Thm | Status | Key result |
   501	|-----|--------|------------|
   502	| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
   503	| B | PROVED | Bar-cobar inversion: Omega(B(A)) -> A qi on Koszul locus |
   504	| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
   505	| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
   506	| H | PROVED | ChirHoch*(A) polynomial Hilbert series, concentrated in cohomological degrees {0,1,2} |
   507	| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
   508	| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
   509	| Koszul | 10+1+1 | 10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir) |
codex
**Cross-Volume Hits**
- `chapters/theory/higher_genus_modular_koszul.tex:2843-2946` (Vol I) states Theorem D (modular characteristic) as the genus‑free-energy universality, explicitly spelling out `obs_g = κ·λ_g` on the proved uniform‑weight lane, the uniform‑weight generating-function `F_g = κ` closed form, and the multi‑weight correction `δF_g^{\mathrm{cross}}` that reappears for $g\ge2$ (§(i)–(iv) plus the ensuing routing remark).
- `chapters/connections/holomorphic_topological.tex:150-169` (Vol II) recasts the same scalar theorem: the shadow obstruction tower on the uniform‑weight locus gives `κ·λ_g` (Theorem D/`thm:genus-universality`) and the multi‑weight departure introduces the same `δF_g^{\mathrm{cross}}` correction off that locus, so the wording is already mirrored in the HT/physics chapter.
- `chapters/connections/modular_koszul_bridge.tex:1-36` (Vol III) opens the bridge by restating complementarity (Theorem C) and Theorem D together with the uniform‑weight law, while `:72-116` (first part of Section 2) relays the scalar complementarity clause C2: the uniform‑weight condition is mandatory, and multi‑weight cases at $g\ge2$ inherit the `δF_g^{\mathrm{cross}}` correction when `obs_g = κ_{\mathrm{ch}}·λ_g` is asserted (Proposition in Section 2 carries the same correction note).
- `notes/physics_bv_brst_cy.tex:284-309` (Vol III notes) repeats the loop from the BV/BRST viewpoint: the genus‑$g$ anomaly on the uniform‑weight lane is `obs_g = κ_{\mathrm{ch}}·λ_g`, with the text explicitly reminding that multi‑weight algebras at $g\ge2$ require the Vol I cross‑channel correction.

**Wording Variants**
- Vol I’s Theorem D bundle uses “modular characteristic package” language, tags the generating function itself as `(UNIFORM-WEIGHT)`, and highlights the routing `Θ_A ⇒ obs_g = κλ_g ⇒ F_g = κ·(hat A−1)` chain.
- Vol II frames the same statement in physics terms (“scalar shadow on the uniform-weight locus” with “multi-weight correction off this locus”), but still cites Theorem D and mentions `δF_g^{\mathrm{cross}}`.
- Vol III’s bridge response splits complementarity into C1/C2, calls out C2 as the uniform‑weight-only scalar sum, and then asserts the same cross‑channel correction before transporting it down to CY categories and anomaly cancellations.

**Propagation?**
- Yes. Because the uniform‑weight/`obs_g = κλ_g` clause and its `δF_g^{\mathrm{cross}}` caveat are explicitly re-stated in Vol II HT text, the Vol III modular bridge, and even in the BV/BRST notes, any revision of the uniform-weight scope, tagging, or correction language in Vol I’s Theorem D/C2 must be mirrored in these locations (each already references the same condition by reference names, line ranges, and the δ‑term).
wait(call_rjSmY3um8rdRwP0mjYVcXQEb) 1 agents complete:
  019d869e-a881-7672-9962-79efd032b095 completed: "**Cross-Volume Hits**
- `chapters/theory/higher_genus_modular_koszul.tex:2843-2946` (Vol I) states Theorem D (modular ch…"
collab wait(call_zGJXtE9BnPlvv3MQ7QbWSQ0c)
  receivers: 019d869e-a76e-7dc3-a786-1ee349aa7390, 019d869e-a78d-7512-a118-deb963680694
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
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
**Summarizing delta_F_g^cross engines and gaps**

I collected key files in compute/lib and tests that calculate or verify delta_F_g^cross and multi-weight corrections, including `curved_sc_higher_genus_engine.py`, `theorem_vicedo_envelope_engine.py`, and `rectification_delta_f2_verify_engine.py`, with line references where available. Tests like `test_theorem_genus4_multiweight_engine.py` demonstrate some cross-channel verifications, especially for W3 and genus 2 gravitational cases. However, there are notable gaps: no general engines or formulas for families W_N beyond N=3 at genus ≥3, and limited coverage for multi-weight corrections across general genus or families. Uniform-weight cross channels are mostly verified only for specific cases like W3. I focused the survey on relevant compute/lib and test files referencing delta, cross terms, and genus contributions, reporting what exists and where future engine or test expansions are needed.
exec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_w3_stokes_resurgence_engine.py | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
     1	r"""Tests for W_3 Stokes resurgence engine.
     2	
     3	40+ tests covering:
     4	  - kappa formulas (AP1, AP9, multi-path verification)
     5	  - Cross-channel corrections delta_F_g (exact, verified against graph sum)
     6	  - Full genus expansion F_g = kappa * lambda_g^FP + delta_F_g^cross
     7	  - Borel transform structure and singularities
     8	  - Stokes constants (scalar, cross, full)
     9	  - Instanton action invariance under multi-weight structure
    10	  - MC equation / bridge equation constraints
    11	  - Koszul duality c <-> 100 - c
    12	  - Self-dual point c = 50
    13	  - Per-channel decomposition
    14	  - Multi-c comparison
    15	
    16	Each test uses at least 2 independent verification paths (multi-path mandate).
    17	"""
    18	
    19	import math
    20	import cmath

thinking
**Summarizing cross-channel corrections and verification gaps**

I'll organize the information into four parts: files/functions found with line references, what each computes, whether they explicitly cover multi-weight corrections, and where verification gaps exist—highlighting that cross-channel data beyond W3 genus 3 and gravitational genus 2 is missing and suggesting next steps for extending coverage and tests.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2980,3065p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2980	(Remark~\ref{rem:chain-vs-classical-mf}). The full Chern
  2981	character recovers the spectral
  2982	discriminant~$\Delta_{\cA}$
  2983	(Remark~\ref{rem:spectral-characteristic-programme});
  2984	the flat connection furnishes the bar-side comparison surface for
  2985	the KZ/Hitchin package on that
  2986	integrable affine lane; the factorization structure recovers the modular
  2987	functor (Theorem~\ref{thm:chain-modular-functor},
  2988	Conjecture~\ref{conj:categorical-modular-kd}).
  2989	\end{remark}
  2990	
  2991	\begin{remark}[Proof routing for Theorem~D;
  2992	Convention~\ref{conv:proof-architecture}]
  2993	\label{rem:theorem-d-model}
  2994	\index{modular characteristic theorem!model presentation}
  2995	\[
  2996	\Theta_\cA \text{ and its shadow tower}
  2997	\Longrightarrow
  2998	\mathrm{obs}_g=\kappa\cdot\lambda_g
  2999	\Longrightarrow
codex
1) **Files/functions found**  
- `compute/lib/curved_sc_higher_genus_engine.py` (lines 118‑814) lays out the SC cooperad story, locates `delta_F_g^cross` in the closed sector, records the modular characteristic, and exposes helpers such as `classify_cross_channel_sector`, `delta_f2_w3`, `delta_f2_w3_decomposition`, and `delta_f2_general_uniform_weight_vanishes` (uniform-weight case vs. multi-weight) that you can cite in a remark about multi-weight corrections.  
- `compute/lib/rectification_delta_f2_verify_engine.py` (lines 1‑49) is an independent “red‑team” graph‑sum engine for the genus‑2 gravitational `F_2(W_N)` expansion; it separates the diagonal (kappa·λ_2) and cross‑channel contributions and computes `delta_F_2^cross` by brute‑force over the seven stable graphs.  
- `compute/lib/theorem_vicedo_envelope_engine.py` (lines 1108‑1134) packages the obstruction analysis: uniform weight gives `obs_g = κ·λ_g`, while multi‑weight adds `delta_F_g^cross` at genus ≥2, so the shadow tower is the obstruction.  
- `compute/lib/mumford_chiodo_multiweight_engine.py` (docstring and framework) supplies the background on why higher‑weight Hodge classes do not sneak into the bar complex and prepares the tautological infrastructure needed for multi‑channel corrections.

2) **What they compute**  
- The curved SC engine computes Bernoulli/FP numbers, closed‑sector dimensions, and explicitly the `delta_F_2(W_3)` decomposition with graph contributions, plus a utility that flags uniform‑ versus non‑uniform‑weight lists (so you can argue when the correction vanishes).  
- The rectification engine recomputes the genus‑2 graph sums, including propagator/vertex data and automorphism weights, verifying the formula  
  `δF_2^{grav}(W_N,c) = (N−2)(N+3)/96 + (N−2)(3N^3+14N^2+22N+33)/(24c)`  
  and isolating the cross‑channel piece from mixed channel assignments.  
- Vicedo’s obstruction analysis acts as the “F_g bookkeeping” API: it records whether the genus obstruction terminates and, crucially, notes that multi‑weight families pick up a `delta_F_g^cross` term beyond the scalar `κ·λ_g`.  
- The Mumford–Chiodo engine builds the Hodge intersection numbers that would be needed if other weights ever appeared in the graph sum, so you can point to it when justifying why the correction is combinatorial rather than Hodge‑class noise.

3) **Multi-weight corrections explicitly addressed**  
- `curved_sc_higher_genus_engine.py` and `delta_f2_w3`/`delta_f2_w3_decomposition` document the W₃ cross‑channel correction, say it vanishes exactly under uniform weight (lines 749‑813), and highlight that every mixed‑channel graph lives solely in the closed sector.  
- `rectification_delta_f2_verify_engine.py` is dedicated to computing the cross‑channel part for W_N at genus 2, so the formula is independently reproducible (lines 1‑49).  
- The obstruction analysis in `theorem_vicedo_envelope_engine.py` explicitly adds `delta_F_g^cross` to `obs_g` whenever weights differ (lines 1115‑1134).  
- Multiple tests call these helpers:  
  * `compute/tests/test_theorem_genus2_w3_partition_engine.py:1‑44` confirms the W₃ case via five verification paths.  
  * `compute/tests/test_theorem_w3_stokes_resurgence_engine.py:1‑70` exercises delta‑F₉/ cross contributions, genus expansions, and Stokes data for W₃ at several genera.  
  * `compute/tests/test_theorem_genus4_multiweight_engine.py:430‑510` shows `δF_g^cross > 0` for W₃ at g=2,3,4 while affine/sl₂ (uniform-weight) stays at zero.  
  * `compute/tests/test_pva_deformation_comparison_engine.py:1300‑1345` proves that Virasoro/sl₂/heisenberg have zero cross correction and that W₃’s `δF_2 = (c+204)/(16c)` is positive and matches the obstruction output, including the self-dual point check.

4) **Verification gaps**  
- The only explicit cross‑channel expansions in compute/lib are W₃ (genus 2‑4) and the genus‑2 gravitational `δF_2^{grav}(W_N)` graph sum. There is no analogous engine/test that computes `δF_g^cross` for general W_N or other multi-weight families at g ≥ 3, nor any aggregator that promotes the W₃ data to a more general pattern.  
- Aside from the general uniform‑weight vanishing check (`delta_f2_general_uniform_weight_vanishes`), there isn’t a reusable API that, given a list of weights and kappa values, spits out the `δF_g^cross` correction for arbitrary genus; every nonuniform example still relies on family‑specific computations (W₃ or genus‑2 graph sums).  
- If the manuscript remark needs broader support, suggest adding (a) a family‑agnostic multi‑channel graph‑sum engine that can be parameterized by the weight spectrum and genus, or (b) extra tests/notes that document how similar cross corrections appear (or vanish) in the other families you care about, so that the remark isn’t just W₃‑centric.
wait(call_zGJXtE9BnPlvv3MQ7QbWSQ0c) 1 agents complete:
  019d869e-a78d-7512-a118-deb963680694 completed: "1) **Files/functions found**  
- `compute/lib/curved_sc_higher_genus_engine.py` (lines 118‑814) lays out the SC cooperad…"
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '22420,22640p'" in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
 22420	
 22421	The theorem identifies the exact boundary. The diagonal part of
 22422	the genus expansion is universal; the cross-channel correction
 22423	$\delta F_g^{\mathrm{cross}}$ is the sole obstruction to the
 22424	scalar formula at genus $g \geq 2$. For interacting multi-weight
 22425	algebras ($\cW_3$ being the first witness), this obstruction is
 22426	nonzero: the scalar formula fails. The forced question is
 22427	whether any multi-weight algebra escapes. The answer is yes, and
 22428	the escapees are precisely the free fields. This is not an
 22429	accident but a theorem, and its proof reveals a triple redundancy
 22430	that deserves scrutiny: three independent mechanisms, each
 22431	drawing on a different structural feature of the free-field OPE,
 22432	all force the same vanishing. When a single conclusion admits
 22433	three independent proofs from three independent sources, the
 22434	conclusion is not a coincidence but a consequence of the
 22435	factorization structure itself.
 22436	
 22437	\begin{proposition}[Free-field exactness of the scalar formula;
 22438	\ClaimStatusProvedHere]
 22439	\label{prop:free-field-scalar-exact}
collab wait(call_MCaHYwfFTdPDsU1tBGzo6d9b)
  receivers: 019d869e-a76e-7dc3-a786-1ee349aa7390

thinking
**Organizing research remark insertion and key references**

I’m gathering where to insert a research remark about multi-weight corrections and cross-channel invariants, with recommended spots near `rem:multi-gen-independence` and related propositions. I’m also collecting file excerpts and line ranges summarizing Theorem D, conditions C2, and uniform weight concepts from multiple locations to include as bullet points in the final message.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2810,2865p'" in /Users/raeez/chiral-bar-cobar succeeded in 74ms:
  2810	\index{modular characteristic!hierarchy|textbf}
  2811	The package~$\mathcal{C}_{\cA}$ \eqref{eq:full-package-quintuple}
  2812	has three logarithmic levels:
  2813	(1)~scalar: $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic}),
  2814	exponential $=$ modular period~$N$;
  2815	(2)~spectral: $\Delta_{\cA}(x)$
  2816	(Theorem~\ref{thm:spectral-characteristic}),
  2817	exponential $=$ periodicity profile~$\Pi_{\cA}$;
  2818	(3)~shadow obstruction tower / full MC: $\Theta_{\cA}^{\leq r}$, $\Defcyc(\cA)$
  2819	(Definition~\ref{def:shadow-postnikov-tower};
  2820	Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
  2821	at scalar level),
  2822	exponential $=$ modular automorphy.
  2823	See Table~\ref{tab:master-invariants}.
  2824	\end{remark}
  2825	
  2826	\medskip
  2827	Via the Feynman transform of the Getzler--Kapranov modular operad
  2828	$\{\overline{\mathcal{M}}_{g,n}\}_{g,n}$, the genus tower
  2829	assembles into a chain-level modular functor

thinking
**Summarizing theorem references and insertion points**

I’m gathering detailed references across multiple files for the theorem map, multi-weight cross-channel language, and suggested research remark insertion points, organizing them into clear sections with file paths and line numbers to help the user integrate or extend the material effectively.
codex
**Required Files**
- `CLAUDE.md:418-505` enforces the FM8 uniform-weight template before any `obs_g`/`F_g` formula and records the status table where D is “obs_g = κ·λ_g (uniform-weight; multi-weight: +δF_g^cross)”—a reminder that every Theorem‑D citation must carry the proved uniform-weight lane plus its cross-channel obstruction.  
- `chapters/connections/concordance.tex:40-68` repeats the status map: C0/C1 proved, C2 (“shifted-symplectic/BV upgrade”) conditional on the uniform-weight perfectness package, and D “obs_g = κλ_g on the proved uniform-weight lane; genus‑1 universal; multi-weight g ≥ 2 has δF_g^cross.”  
- `metadata/theorem_registry.md:901` lists `thm:modular-characteristic` (line 2844 of `chapters/theory/higher_genus_modular_koszul.tex`) as Theorem D, linking the registry directly to the formal statement in the target file.  
- `archive/raeeznotes/raeeznotes100/red_team_summary.md:1-70` provides the overall risk/status profile for Volumes I/II (e.g., 3,801 ProvedHere, 327 conjectured, 116 conditional) but does not add any new Theorem D/rigidity details—still useful for situational awareness of audit pressure.

**Theorem/Location Map**
- Theorem D is flagged in the three-tier architecture summary and stated formally in `chapters/theory/higher_genus_modular_koszul.tex:2338-2366` (Tier 0 list) and in the full modular‑characteristic theorem at `:2843-2885`, where part (i)(a) spells out `obs_g = κ(𝒜)·λ_g` (uniform-weight, unconditional at g=1).  
- C2 appears as the conditional part of Complementarity in `chapters/connections/concordance.tex:40-57` (“shifted-symplectic/BV upgrade conditional on uniform-weight perfectness”) and is governed by `Thm \ref{thm:shifted-symplectic-complementarity}` within `chapters/theory/higher_genus_modular_koszul.tex` (the referenced theorem lives nearby in the same file).  
- The uniform-weight lane is defined (and its genus‑g consequence stated) in `chapters/theory/higher_genus_modular_koszul.tex:2706-2744` (Definition \ref{def:scalar-lane}); it notes that scalar statements prove at all genera under the uniform-weight hypothesis, while multi-weight algebras require the cross-channel correction from Thm \ref{thm:multi-weight-genus-expansion}.

**Multi-Weight Language**
- Theorem \ref{thm:multi-weight-genus-expansion} and the ensuing narrative (`chapters/theory/higher_genus_modular_koszul.tex:22276-22444`) spell out the diagonal scalar formula, the `δF_g^{cross}` decomposition, genus‑1 vanishing, uniform-weight universality, R‑matrix independence, and the explicit genus‑2 correction (the formula for `𝒲_3`).  
- Following that theorem, `:22421-22595` emphasizes the physical boundary between uniform-weight and interacting multi-weight families, proves the free-field vanishing `δF_g^{cross} = 0` (`prop:free-field-scalar-exact`), and explicitly resolves `Open Problem \ref{op:multi-generator-universality}` in the negative for interacting cases (`rem:multi-gen-independence` at `:22597-22632`).  
- `CLAUDE.md:498-506` reiterates the same multi-weight correction in the status table, and `concordance.tex:40-57` references the cross-channel term in the summary for D, reinforcing that any multi-weight citation must mention `δF_g^{cross}`.

**Research Remark Point**
- The narrative right after `rem:multi-gen-independence` (`chapters/theory/higher_genus_modular_koszul.tex:22597-22632`) is already steering toward new invariants (`δF_g^{cross}`) and explicitly resolves the multi-generator universality question; this location is therefore a natural landing spot for a Research Remark that surveys open directions for computing or structurally interpreting `δF_g^{cross}` (e.g., its dependence on graph strata, large‑c limits, or analogues of the free-field triple redundancy).  
- Alternatively, the uniform-weight lane discussion around `rem:theorem-d-alt-grr` (`:2991-3068`) already frames multiple proof routes (shadow tower, GRR) for Theorem D’s scalar clause, so a Research Remark there could sketch potential generalizations (e.g., how multi-weight propagators break the Hodge coupling) while keeping the focus on uniform-weight versus cross-channel behavior.
wait(call_MCaHYwfFTdPDsU1tBGzo6d9b) 1 agents complete:
  019d869e-a76e-7dc3-a786-1ee349aa7390 completed: "**Required Files**
- `CLAUDE.md:418-505` enforces the FM8 uniform-weight template before any `obs_g`/`F_g` formula and r…"
codex
I have the theorem map now: the chapter already separates the proved uniform-weight lane from the multi-weight correction, and there is existing compute support for W₃ and genus‑2 graph sums. I’m reading the exact local wording around Theorem D, C2, and the existing multi-weight theorem so the new remark sits on the strongest live surface and doesn’t drift from concordance.
exec
/bin/zsh -lc "sed -n '418,506p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).

**FM9. Harmonic-number off-by-one.** Opus confuses `H_{N-1} = sum_{j=1}^{N-1} 1/j` with `H_N - 1 = sum_{j=2}^{N} 1/j`. At N=2, H_1=1 but H_2-1=1/2. CLAUDE.md itself had this error. Counter: after any harmonic-number shift, evaluate at N=2 AND N=3 and compare numerically.

**FM10. Hardcoded part number drift (`Part~IV` vs `\ref{part:...}`).** Cross-volume references as hardcoded roman numerals break silently on reorganisation. Counter: after any Edit, grep `Part~[IVX]+|Chapter~[0-9]+` in the file and replace with `\ref{part:...}`.

**FM11. Sugawara shift missing in av(r(z)) = kappa.** For abelian Heisenberg, `av(r) = kappa` holds cleanly. For non-abelian KM, `av(r) + dim(g)/2 = kappa(V_k(g))`. Opus writes the abelian form universally. Counter: before writing av(r)=kappa, state the family (abelian vs non-abelian).

**FM12. Mid-response truncation on long audit tasks.** Opus truncates between fix and report when both are requested in the same turn. Counter: separate fix execution from report writing across two tool calls.

**FM13. Auto-completion to the majority-variant.** Opus auto-completes to the most common training-data form even when the manuscript uses a different convention. Example: `eta(q) = prod(1-q^n)` (missing q^{1/24}). Counter: break the formula across multiple lines and annotate each term's convention.

**FM14. AP125 label/environment mismatch on tag changes.** Downgrading a theorem to a conjecture changes `\begin{theorem}` to `\begin{conjecture}` but forgets to rename `thm:foo` to `conj:foo`. Counter: atomic 3-step edit -- rename environment, rename label, grep-and-replace all refs, in the same tool-call batch.

**FM15. Duplicate labels across volumes.** Parallel agents independently create labels with the same natural name across volumes. Counter: before creating `\label{foo}`, grep all three volumes; if match, prefix with v1/v2/v3.

**FM16. Silent kappa-family conflation.** Opus picks kappa from the most recently-mentioned family when context shifts. Counter: every kappa formula carries an explicit family superscript; bare `\kappa` forbidden in mathematical contexts.

**FM17. Amplitude/dimension conflation for ChirHoch.** Opus conflates "cohomological amplitude [0,2]" (topological) with "virtual dimension 2" (arithmetic). Counter: any sentence mentioning ChirHoch and a numerical invariant must choose explicitly.

 succeeded in 53ms:
    1032 CLAUDE.md
   11454 chapters/connections/concordance.tex
    3481 metadata/theorem_registry.md
     119 archive/raeeznotes/raeeznotes100/red_team_summary.md
   35061 chapters/theory/higher_genus_modular_koszul.tex
   51147 total
exec
/bin/zsh -lc "sed -n '40,68p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '890,910p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 78ms:
| `cor:unconditional-allgenera-km` | `corollary` | 1572 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1624 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1724 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1774 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1836 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `prop:hook-pbw` | `proposition` | 1997 | Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses |
| `thm:pbw-propagation` | `theorem` | 2089 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | 2248 | Locality of the collision differential |
| `thm:three-tier-architecture` | `theorem` | 2335 | Three-tier logical architecture of modular Koszul duality |
| `lem:e2-higher-genus` | `lemma` | 2584 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 2736 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 2844 | Modular characteristic |
| `cor:free-energy-ahat-genus` | `corollary` | 3085 | Scalar free energy as $\hat{A}$-genus |
| `prop:gue-universality` | `proposition` | 3411 | GUE universality |
| `rem:shadow-tr-pf-decomposition-identity` | `remark` | 3494 | Shadow/topological-recursion/planted-forest decomposition |
| `thm:spectral-characteristic` | `theorem` | 3532 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 3565 | Universal modular Maurer--Cartan class |
| `prop:curvature-centrality-general` | `proposition` | 3702 | Centrality of higher-genus curvature |
| `thm:mc2-bar-intrinsic` | `theorem` | 3764 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 4275 | Shadow extraction |
 succeeded in 79ms:
 & Strict quasi-isomorphism on the Koszul locus
 $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
 \textup{(}Thms~\ref{thm:higher-genus-inversion},
 \ref{thm:bar-cobar-inversion-qi}\textup{)}; off the locus,
 the counit is an unconditional coderived coacyclic-equivalence,
 promoted back to an ordinary quasi-isomorphism on collapse loci
 & \ClaimStatusProvedHere \\
\textbf{C} & Complementarity
 & C0: coderived fiber-center identification unconditional,
 ordinary-derived only on the flat perfect locus
 \textup{(}Thm~\ref{thm:fiber-center-identification}\textup{)}.
 C1: homotopy eigenspace decomposition for all~$g$, with
 duality/Lagrangian only for $g \geq 1$ and genus~$0$
 treated separately
 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)}.
 C2: shifted-symplectic/BV upgrade conditional on the
 uniform-weight perfectness package
 \textup{(}Thm~\ref{thm:shifted-symplectic-complementarity}\textup{)}
 & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
\textbf{D} & Modular characteristic
exec
/bin/zsh -lc "sed -n '1,90p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
**Inspecting target file sections**

I need to inspect the target file, focusing on the relevant sections. I might use a command like `rg` to locate specific theorem and remark labels. It could be useful to execute some commands for that. Reading the full file isn't feasible right now, but I could focus on the key sections. So, yeah, I might use `rg` for the label names to pinpoint where I need to look more closely.
exec
/bin/zsh -lc "rg -n \"thm:modular-characteristic|def:scalar-lane|thm:shifted-symplectic-complementarity|thm:multi-weight-genus-expansion|rem:multi-gen-independence|rem:theorem-d-alt-grr|uniform-weight|delta_F_g\\\\"'^'"\\{\\\\mathrm\\{cross\\}\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:thm:modular-characteristic|def:scalar-lane|thm:shifted-symplectic-complementarity|thm:multi-weight-genus-expansion|rem:multi-gen-independence|rem:theorem-d-alt-grr|uniform-weight|delta_F_g\^\{\mathrm\{cross\}\})
                                                                                                                                                                                                       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '2680,3075p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '22380,22660p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 82ms:
all~$i$ and all graphs:
\[
F_g^{\mathrm{diag}}(\cA)
\;=\;
\sum_{i=1}^r F_g(\cA_i)
\;=\;
\sum_{i=1}^r \kappa_i \cdot \lambda_g^{\mathrm{FP}}
\;=\;
\kappa(\cA) \cdot \lambda_g^{\mathrm{FP}},
\]
where the second equality uses single-channel universality
(Theorem~\ref{thm:genus-universality} at $g=1$, the
uniform-weight scalar lane for $g \geq 2$: each single-channel
component has a single generator and hence uniform weight).

\smallskip\noindent
(ii)~\emph{Decomposition.}
The full graph sum runs over all
channel assignments $\sigma \colon E(\Gamma) \to \{1,\ldots,r\}$:
$F_g(\cA) = \sum_\Gamma
 succeeded in 90ms:
 \emph{ambient modular deformation family}, the genus-graded
 system of curved deformation complexes.
\end{enumerate}

\smallskip\noindent
\emph{Essential characteristics.}
The package~$\mathcal{C}_{\cA}$ has four structural properties:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Functorial}: $\mathcal{C}$ is natural in morphisms
 of modular Koszul objects;
\item \emph{Dualizable}: the duality $\cA \leftrightarrow \cA^!$
 acts on each component
 ($\kappa + \kappa' = K$, $\Delta_{\cA^!}$ determined by
 $\Delta_{\cA}$, etc.);
\item \emph{Modular}: compatible with clutching and
 boundary degeneration on~$\overline{\mathcal{M}}_{g,n}$;
\item \emph{Non-scalar}: $\kappa(\cA)$ is only the first shadow;
 the full package contains strictly more information
 (cf.\ the spectral data of level~(2) in
 Remark~\ref{rem:characteristic-hierarchy}).

thinking
**Examining the multi-weight theorem**

I’m reviewing the section on the multi-weight theorem related to sed 22380. I think I need to find the actual line numbers for the theorem label to add more clarity. Maybe including additional context would make it easier to understand. Also, I might consider using rg with fixed strings for simplification instead. There seems to be a lot to unpack here, so I want to ensure I’m being thorough!
exec
/bin/zsh -lc 'rg -n -F "thm:shifted-symplectic-complementarity" chapters/theory/higher_genus_modular_koszul.tex; rg -n -F "thm:multi-weight-genus-expansion" chapters/theory/higher_genus_modular_koszul.tex; rg -n -F "rem:multi-gen-independence" chapters/theory/higher_genus_modular_koszul.tex; rg -n -F "rem:theorem-d-alt-grr" chapters/theory/higher_genus_modular_koszul.tex; rg -n -F "delta F_g''^{'"\\mathrm{cross}}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 102ms:
2731:Theorem~\ref{thm:multi-weight-genus-expansion}; all free-field algebras are exact exceptions by
4979:\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
5746:\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)},
13250:(Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}).
22276:\label{thm:multi-weight-genus-expansion}
22469:By Theorem~\ref{thm:multi-weight-genus-expansion}(ii), the scalar
22516:\textup{(}weight~$1$; cf.\ Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)},
22585:Theorem~\ref{thm:multi-weight-genus-expansion}(i)--(ii) gives
22612:Theorem~\ref{thm:multi-weight-genus-expansion} resolves
22643:Theorem~\ref{thm:multi-weight-genus-expansion}(i) reduces the
22698:(Theorem~\ref{thm:multi-weight-genus-expansion}(i)).
22764:Theorem~\ref{thm:multi-weight-genus-expansion}(iii));
22988:Theorem~\ref{thm:multi-weight-genus-expansion}(iii)).
24656:Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}: the
25365:(Theorem~\ref{thm:multi-weight-genus-expansion}).
25606:(Theorem~\ref{thm:multi-weight-genus-expansion}(vi),
22598:\label{rem:multi-gen-independence}%
3030:\label{rem:theorem-d-alt-grr}
2884: $\delta F_g^{\mathrm{cross}}$ is required
3229:$\delta F_g^{\mathrm{cross}}$ of

thinking
**Troubleshooting theorem search**

I’m trying to find the `shifted-symplectic-complementarity` theorem but getting a “not found” issue. It seems the command might not have worked properly because of using semicolons in a single string. My search only brings up other hits, which isn’t useful. I think I need to look for the theorem around labels by possibly using a command like `rg` with "shifted-symplectic". Let’s see if that helps!
codex
The target chapter is larger than a quick patch surface, so I’m locking the exact chunks: the theorem statement for D, the existing multi-weight correction theorem and its negative universality remark, and the C2 complementarity lane. Next I’m checking whether the chapter already has enough evidence to support a stronger theorem statement or only a research remark.
exec
/bin/zsh -lc 'rg -n "shifted-symplectic|BV upgrade|scalar BV|uniform-weight perfectness|C2" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 81ms:
3595:This is Theorem~\ref{thm:master-theta} (MC2).
3596:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3743:\subsubsection*{The bar-intrinsic construction: resolution of MC2}
3769:\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
3772:\index{MC2!bar-intrinsic proof}
3773:\index{MC2!full generality}
3830:\begin{remark}[Scope of MC2 in this chapter]
3831:\index{MC2!coinvariant scope}
3832:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
4104:\index{MC2!foundational dependency chain}
4158:\index{Kontsevich--Soibelman!alternative construction of MC2}
4228:installed, it furnishes an alternative proof path to MC2.
4233:\index{MC2!bar-intrinsic perspective}
4234:\index{MC2!two regimes}
4235:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4397:\index{MC2!functoriality|textbf}
4988:\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
4998:MC2-1 resolved for KM by Theorem~\ref{thm:mc2-1-km}.
5070: of the MC2 package at Step~1.
5089: All MC2 Step-$1$--$3$ computations are verified for
exec
/bin/zsh -lc "sed -n '24160,24480p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4900,5055p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$c \sim -N^4(1{-}\lambda)^2/\lambda$):
\[
\delta F_2
\;\sim\;
\frac{N^2}{96}
\;-\;
\frac{\lambda}{8(1{-}\lambda)^2}.
\]
The constant term $B(N) \sim N^2/96$ is the \emph{planar
cross-channel}: it grows quadratically with $N$, reflecting
the proliferation of mixed-channel assignments.
This $O(N^2)$ term is visible only for multi-weight algebras;
the scalar part $\kappa \cdot \lambda_2^{\mathrm{FP}}$ also
grows as $O(N^2)$ but with a different coefficient.
In the $W_{1+\infty}$ limit ($N \to \infty$, $c$ fixed),
both $B(N)$ and $A(N)/c$ diverge: the cross-channel
correction has no finite limit, and the scalar formula
$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ becomes
arbitrarily inadequate
\textup{(}\texttt{test\_theorem\_large\_n\_delta\_f2\_engine.py}\textup{)}.
 succeeded in 51ms:
\Theta^{\min}_{\mathrm{Vir}_{26-c}} = 13\,\eta\otimes\Lambda$
\textup{(}complementarity sum, fixed point at $c = 13$\textup{)}.
\end{corollary}

\begin{proof}
Each line specializes the universal formula
$\kappa(\cA) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$ to the
relevant Lie algebra and level. For W-algebras, $\kappa$ is
the anomaly ratio $\varrho(\mathfrak{g}) = \sum_i 1/(m_i+1)$ times
the central charge $c$
(Theorem~\ref{thm:wn-obstruction}).
For Virasoro, $\rho(\mathfrak{sl}_2) = 1/2$, so $\kappa = c/2$.
For $\mathcal{W}_3$, $\rho(\mathfrak{sl}_3) = 5/6$, so
$\kappa = 5c/6$. For Heisenberg, $\kappa = k$ directly
(level equals modular characteristic). For rank-$d$ lattice VOAs,
$\kappa = d$ by additivity
(Corollary~\ref{cor:kappa-additivity}).
The duality formulas follow from $\kappa(\cA) + \kappa(\cA^!) = 0$
(Theorem~\ref{thm:modular-characteristic}(iii)) for KM, and from
$c + c' = 26$ with $\kappa = c/2$ for Virasoro.

thinking
**Searching for theorem statement**

I need to locate the statement for theorem C2 related to shifted-symplectic complementarity. It seems I might not find it because the label might be different in the resources I'm checking. I think I'll try searching specifically for "shifted-symplectic complementarity" to see if that yields better results. Let’s explore this further and see what I can uncover!
exec
/bin/zsh -lc 'rg -n -i "shifted.*symplectic|symplectic.*complementarity|BV pairing|scalar BV pairing|uniform-weight perfect" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
514:Lagrangian for the shifted symplectic pairing
5978:For a linear shifted symplectic complex, the PTVV non-degeneracy
6076:\item the cross Verdier/BV pairing induces a quasi-isomorphism
6199:\item the seed-level Verdier/BV pairing extends to a chain map
6323: the cross Verdier/BV pairing on
6482: the cross Verdier/BV pairing on
6641:\item the cross Verdier/BV pairing on
10102:shifted-symplectic pairing from Verdier duality, and the deformation
11833: internal edges via the cyclic Verdier/BV pairing;
30643:datum is the restriction of the shifted-symplectic
exec
/bin/zsh -lc "sed -n '8060,8215p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10028,10140p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
comparison
(Propositions~\ref{prop:tautological-line-support-criterion}
through~\ref{prop:one-channel-normalization-criterion}).
Once packages~(1)--(2) exist, package~(3) is a finite
reduction to one normalized scalar check. What remains open beyond
the proved uniform-weight lane is whether that check forces the
all-genera coefficient to be $\kappa(\cA)\Lambda$.
\end{remark}

\begin{theorem}[MC2 completion under explicit hypotheses; \ClaimStatusProvedHere]
\label{thm:mc2-conditional-completion}
\index{MC2!completion under explicit hypotheses}
Let $\cA$ be a modular Koszul chiral algebra with simple Lie
symmetry~$\mathfrak{g}$. Assume:
\begin{enumerate}[label=\textup{(MC2-\arabic*)}]
\item\label{mc2-hyp:cyclic}
 The cyclic deformation complex $\Defcyc(\cA)$ exists as a cyclic
 $L_\infty$-algebra on bar coderivations, with
 $H^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g}) \cong \mathbb{C}$
 \textup{(}confirmed for all simple~$\mathfrak{g}$ by
 succeeded in 51ms:
\index{tautological ring!MC2-3 verification}
The clutching/trace criterion of
Proposition~\ref{prop:tautological-line-support-criterion}
still gives a plausible independent route to the all-genera scalar
trace package.
\textup{(}a\textup{)} The Feynman transform produces classes in
$R^*(\overline{\mathcal{M}}_g)$ (Mumford~\cite{Mumford83}).
\textup{(}b\textup{)} Clutching determines $o_g|_{\delta_h}$ from
lower-genus data by induction, with base case
$o_1=\kappa\lambda_1$.
\textup{(}c\textup{)} If Pixton-type relations separate the
relevant one-channel sector, then
Proposition~\ref{prop:tautological-line-support-criterion}
would recover $o_g=\kappa\lambda_g$.
At present this remains a route, not a completed independent proof,
for arbitrary multi-weight families.
\end{remark}

\begin{corollary}[MC2 comparison gauntlet collapses on the proved
scalar lane; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "sed -n '14900,14980p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\Theta_{\cA}^{\min}
= \kappa(\cA)\eta\otimes\Lambda$.
\end{proof}

\begin{remark}[Scope: scalar saturation vs.\ bar-intrinsic existence]
\label{rem:scalar-saturation-scope-v2}
\index{scalar saturation|textbf}
\index{shadow obstruction tower!scalar vs.\ all-degree}
\index{MC2!two regimes}
Theorem~\textup{\ref{thm:theta-direct-derivation}} is the
\emph{proved scalar-lane} case: it applies when
$\dim H^2(\Defcyc(\cA)) = 1$ at each genus
\textup{(}one-channel\textup{)} and the all-genera scalar trace
package is already proved \textup{(}uniform-weight families such as
Heisenberg and generic affine Kac--Moody\textup{)}. In that
setting, the minimal formula
$\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$ is
\emph{proved}.

For multi-channel families \textup{(}or at special parameters

thinking
**Inspecting theorem statements**

I need to take a closer look at the theorem's multi-weight statement, particularly around the range of 22276 to 22324. It seems important to understand the nuances in those sections. I'll dive into it and see what it entails and how it relates to what I'm working on. This will help ensure everything aligns correctly as I progress. Let’s see what insights I can find!
exec
/bin/zsh -lc "sed -n '22260,22340p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Collecting all such graphs gives the restriction to the
non-separating divisor
$\delta_{\mathrm{irr}} =
\xi_{\mathrm{nsep}}(\overline{\cM}_{g-1,n+2})$,
yielding axiom~(iii).

Axioms~(i)--(iii) make $(\Omega^\cA, V, \eta)$ a CohFT
without unit in the sense of
Pandharipande--Pixton--Zvonkine. The unit axiom
$\Omega_{0,3}(\mathbf{1}, v, w) = \eta(v,w)$ holds when the
vacuum vector of~$\cA$ lies in~$V$ and $\ell_2^{(0)}$
restricts to a unital multiplication on~$V$ (satisfied for
all standard families).
\end{proof}

\begin{theorem}[Multi-weight genus expansion; \ClaimStatusProvedHere]
\label{thm:multi-weight-genus-expansion}
\label{thm:multi-generator-universality}
\index{multi-generator obstruction!genus expansion|textbf}%
\index{multi-weight genus expansion|textbf}%
exec
/bin/zsh -lc "sed -n '22340,22435p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \end{equation}
 where\/ $\delta F_2^{\mathrm{sun}}$ collects the sunset
 \textup{(}graph~D\textup{)},
 $\delta F_2^{\theta}$ the theta graph~F, and\/
 $\delta F_2^{\mathrm{bl}}$ the bridge-loop~E.
 For $\cW_3$ with generators $T$
 \textup{(}weight~$2$\textup{)} and $W$
 \textup{(}weight~$3$\textup{)}\textup{:}
 \begin{equation}\label{eq:w3-genus2-cross}
 \delta F_2(\cW_3) \;=\; \frac{3}{c} + \frac{9}{2c}
 + \frac{1}{16} + \frac{21}{4c}
 \;=\; \frac{c + 204}{16c},
 \end{equation}
 the first closed-form cross-channel correction at
 genus\/~$\geq 2$
 \textup{(}Computation~\textup{\ref{comp:w3-genus2-multichannel}}).
\end{enumerate}
In particular, the scalar formula
$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$
holds at all genera if and only if\/~$\cA$ is uniform-weight or

thinking
**Investigating compute modules**

I need to inspect compute and library functions closely, possibly using tools like `rg` and `sed`. It’s important to consider if I should mention any formulas related to `kappa_eff` and evidence of obstruction. I’ll search through relevant compute modules and use `exec_command` for efficient searching. There might be new remarks regarding theorem C2, which could be complex due to variables like genus and channel combinatorics. Gathering evidence about `kappa_eff` is essential, especially if it’s nonexistent.
codex
The compute surface already looks strong enough to support a precise remark, but not a theorem removing the condition. I’m checking two sharper points now: whether the correction has a family-agnostic formula anywhere, and whether the existing formulas rule out absorbing it into a genus-independent `\kappa_{\mathrm{eff}}`.
exec
/bin/zsh -lc 'rg -n "delta_f2|delta_F|cross-channel|uniform-weight|kappa_eff|effective kappa|obs_g|multi-weight" compute/lib/curved_sc_higher_genus_engine.py compute/lib/rectification_delta_f2_verify_engine.py compute/lib/theorem_vicedo_envelope_engine.py compute/lib/mumford_chiodo_multiweight_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/rectification_delta_f2_verify_engine.py:1:r"""Independent verification engine for delta_F_2^{grav}(W_N).
compute/lib/rectification_delta_f2_verify_engine.py:5:    delta_F_2^{grav}(W_N, c) = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c)
compute/lib/rectification_delta_f2_verify_engine.py:7:This engine is built FROM SCRATCH with ZERO imports from the multi-weight
compute/lib/rectification_delta_f2_verify_engine.py:8:cross-channel engine. Every computation is independent.
compute/lib/rectification_delta_f2_verify_engine.py:24:The cross-channel part (mixed channels) is delta_F_2^cross.
compute/lib/rectification_delta_f2_verify_engine.py:48:    thm:multi-weight-genus-expansion, AP27, Faber-Pandharipande
compute/lib/rectification_delta_f2_verify_engine.py:474:# Full genus-2 cross-channel correction
compute/lib/rectification_delta_f2_verify_engine.py:477:def delta_F2_grav_graph_sum(N: int, c: Fraction) -> Fraction:
compute/lib/rectification_delta_f2_verify_engine.py:478:    """Compute delta_F_2^{grav}(W_N, c) by summing over all 7 genus-2 graphs.
compute/lib/rectification_delta_f2_verify_engine.py:480:    This is the MIXED (cross-channel) part of the genus-2 free energy,
compute/lib/rectification_delta_f2_verify_engine.py:494:def delta_F2_grav_per_graph(N: int, c: Fraction) -> Dict[str, Dict[str, Fraction]]:
compute/lib/rectification_delta_f2_verify_engine.py:495:    """Per-graph decomposition of delta_F_2^{grav}(W_N, c)."""
compute/lib/rectification_delta_f2_verify_engine.py:522:    """Claimed: delta_F_2^{grav}(W_N, c) = B(N) + A(N)/c."""
compute/lib/rectification_delta_f2_verify_engine.py:784:def delta_F2_grav_symbolic(N: int, c: Fraction) -> Fraction:
compute/lib/rectification_delta_f2_verify_engine.py:785:    """Compute delta_F_2^{grav} using the algebraic/symbolic expressions.
compute/lib/rectification_delta_f2_verify_engine.py:798:    """Extract B(N) = lim_{c->inf} delta_F_2^{grav}(W_N, c).
compute/lib/rectification_delta_f2_verify_engine.py:818:    """Extract A(N) = coefficient of 1/c in delta_F_2^{grav}(W_N, c).
compute/lib/rectification_delta_f2_verify_engine.py:862:def newton_interpolate_delta_F2(N: int, num_points: int = 6
compute/lib/rectification_delta_f2_verify_engine.py:864:    """Extract the rational function delta_F_2 = P(c)/Q(c) by interpolation.
compute/lib/rectification_delta_f2_verify_engine.py:866:    Since delta_F_2 = B + A/c, we can verify by computing at 2 c-values
exec
/bin/zsh -lc "sed -n '1,220p' compute/lib/rectification_delta_f2_verify_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '720,835p' compute/lib/curved_sc_higher_genus_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

    def corrected_flat_at_genus(self, g: int) -> bool:
        """D^{(g)}^2 = 0 at all genera."""
        return True

    def full_differential_flat(self) -> bool:
        """D_A^2 = 0 for the full genus-completed differential."""
        return True

    def genus_tower_summary(self) -> List[Dict[str, Any]]:
        """Summary of the SC structure at each genus."""
        result = []
        for g in range(self.genus_max + 1):
            curv = self.curvature_at_genus(g)
            result.append({
                'genus': g,
                'curvature': curv,
                'is_curved': curv != Fraction(0),
                'corrected_flat': True,
                'num_period_corrections': g,
 succeeded in 52ms:
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
exec
/bin/zsh -lc "sed -n '1100,1155p' compute/lib/theorem_vicedo_envelope_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        genus_2_cross_channel=g2_ext.delta_f2_cross,
    )


# ---------------------------------------------------------------------------
# 14. Obstruction analysis: what blocks genus extension
# ---------------------------------------------------------------------------

@dataclass
class ObstructionAnalysis:
    r"""Analysis of the precise obstruction to extending Vicedo's construction
    to all genera.

    Vicedo constructs the genus-0 prefactorization algebra.  The obstruction
    to extending to genus g is:
      obs_g(A) = kappa(A) * lambda_g (for uniform-weight algebras)
      obs_g(A) = kappa(A) * lambda_g + delta_F_g^cross (for multi-weight)

    The shadow obstruction tower IS the systematic expansion of this
    obstruction.  At each arity r, the shadow Theta^{<=r} captures the

thinking
**Exploring formulas and proposals**

I need to analyze the obstruction and see if I should look into the W_N genus2 formula. Maybe it could relate to the `delta_F2^grav` theorem rather than being general. I’ll search for "Research Programme" in the text. Additionally, I should check remarks around 24200 and 27200 for insights on cross-channel growth and generating functions. There may be exact theorems about the general W_N formula at genus2 that I need to inspect further.
exec
/bin/zsh -lc "rg -n \"delta_F_2\\"'^'"\\{grav\\}|large-\\"'$N'"\\"'$ behaviour|no closed-form|cross-channel growth|spectral curve obstruction|W_N Frobenius manifold|kappa_eff" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
24421:admits no closed-form expression in one variable.
27310:cross-channel growth of
27362:For $\cW_3$ the cross-channel growth rate at fixed~$c$ is

thinking
**Investigating gravitational data**

I'm considering searching for "grav" and wondering if something might be preventing the results from appearing. Maybe I should inspect nearby lines between 24080 and 24440 since I've already looked at some of those. It seems like I need to apply the W_N formula and search specifically for `delta F_2^{\mathrm{grav}}`. Looks like there's a bit of uncertainty in my approach, but I'll see what I can find!
exec
/bin/zsh -lc 'rg -n -F "delta F_2''^{'"\\mathrm{grav}}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
23503:$\delta F_2^{\mathrm{grav}}(\cW_4) = (7c{+}2148)/(48c)$
23602:- \delta F_2^{\mathrm{grav}}$ is $3$--$30\%$ of the
23604:at $c = 1$, $\delta F_2^{\mathrm{HS}} / \delta F_2^{\mathrm{grav}}
23606:$\delta F_2^{\mathrm{HS}} / \delta F_2^{\mathrm{grav}}
23668:$\delta F_2^{\mathrm{grav}}(\cW_5) = (c{+}434)/(4c)$
23743:$R(c) = \delta F_2^{\mathrm{grav}} + R_{\mathrm{HS}}(c)$,
23895: \delta F_2^{\mathrm{grav}}(\cW_N, c)
23904: \delta F_2^{\mathrm{grav}}(\cW_N, c)
23911: $\delta F_2^{\mathrm{grav}}(\cW_N, c) = 0$ for all\/ $c > 0$
23918: $\delta F_2^{\mathrm{grav}}(\cW_N, c) > 0$.
23924: $\delta F_2^{\mathrm{grav}} = B(N) + A(N)/c$.
23934: \delta F_2^{\mathrm{grav}}
23940: \delta F_2^{\mathrm{grav}}
23946: \delta F_2^{\mathrm{grav}}
23964: \delta F_2^{\mathrm{grav}}(\cW_N, c)
24069:$\delta F_2^{\mathrm{grav}} \leq \delta F_2$,
exec
/bin/zsh -lc "sed -n '23880,23975p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Let\/ $\cW_N$ be the principal\/ $\cW$-algebra with strong generators
$W^{(2)}, W^{(3)}, \ldots, W^{(N)}$ at conformal weights
$2, 3, \ldots, N$. The \emph{gravitational Frobenius algebra}
of\/ $\cW_N$ is the rank-$(N{-}1)$ Frobenius algebra with
per-channel inverse Zamolodchikov metric
$\eta^{(j)(j)} = j/c$ and structure constants
$C^{\mathrm{grav}}_{(i)(j)(k)} = c\,\delta_{ijk}^{\mathrm{even}}$
\textup{(}nonzero only when the number of odd-weight indices
is even, reflecting the\/ $\mathbb{Z}_2$ parity of
odd-spin generators\textup{)}.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Closed-form formula.}
 The genus-$2$ gravitational cross-channel correction is
 \begin{equation}\label{eq:universal-grav-cross-N}
 \boxed{
 \delta F_2^{\mathrm{grav}}(\cW_N, c)
 \;=\;
 \frac{(N{-}2)(N{+}3)}{96}
 \;+\;
 \frac{(N{-}2)(3N^3 + 14N^2 + 22N + 33)}{24c}.

thinking
**Inspecting gravitational formula**

I'm looking at this explicit closed-form formula for genus 2 gravitational cross-channel, and it seems solid. I want to check more lines around the proposition label to ensure everything is accurate, but I wonder if the proof might actually be unnecessary. I'll search for that specific label to reference it properly. Let’s make sure I understand the context fully before moving forward.
exec
/bin/zsh -lc 'rg -n -B 3 -A 2 -F "eq:universal-grav-cross-N" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
23890-\begin{enumerate}[label=\textup{(\roman*)}]
23891-\item \emph{Closed-form formula.}
23892- The genus-$2$ gravitational cross-channel correction is
23893: \begin{equation}\label{eq:universal-grav-cross-N}
23894- \boxed{
23895- \delta F_2^{\mathrm{grav}}(\cW_N, c)
--
23900- }
23901- \end{equation}
23902- Equivalently,
23903: \begin{equation}\label{eq:universal-grav-cross-N-combined}
23904- \delta F_2^{\mathrm{grav}}(\cW_N, c)
23905- \;=\;
exec
/bin/zsh -lc "sed -n '23860,23895p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
each higher-spin self-coupling
$g_{(j)(j)(j+1)}$ for $j = 3, \ldots, N{-}1$ contributes
one independent quadratic extension, and the $\mathbb{Z}_2$
parity of odd-spin generators prevents the
$g_{(j)(j)(j)}$ coupling from introducing further
irrationality when $j$ is odd.
The proof proceeds via odd-power classification on genus-$2$
stable graphs, an abstract $\mathbb{F}_2$-coordinate model
with one coordinate per higher-spin weight, and a rank
computation showing that each weight contributes exactly one
$\mathbb{F}_2$-independent discriminant.
\end{remark}

\begin{proposition}[Universal gravitational cross-channel formula
for~$\cW_N$; \ClaimStatusProvedHere]%
\label{prop:universal-gravitational-cross-channel}%
\index{cross-channel correction!universal $N$-formula|textbf}%
\index{W-algebra@$\mathcal{W}$-algebra!gravitational cross-channel|textbf}%
\index{multi-weight genus expansion!universal formula}%
\index{gravitational Frobenius algebra|textbf}%
exec
/bin/zsh -lc 'rg -n "kappa_eff|effective kappa|absorbs the correction|absorb.*correction|renormalized kappa|modified kappa|cross-channel.*kappa|single number|no closed-form expression in one variable|irreducibly bivariate" chapters/theory/higher_genus_modular_koszul.tex compute/lib/' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 387

compute/lib/bc_nc_distance_shadow_engine.py:58:    AP20: kappa(A) is intrinsic to A; kappa_eff is different
compute/lib/twisted_holography_engine.py:49:  AP29: delta_kappa != kappa_eff (two different objects)
compute/lib/twisted_holography_engine.py:964:    AP29: kappa_eff = kappa(matter) + kappa(ghost) = c/2 + (-13).
compute/lib/twisted_holography_engine.py:965:    Cancellation at c = 26: kappa_eff = 26/2 - 13 = 0.
compute/lib/bv_bar_class_m_engine.py:528:    to a combination that absorbs the harmonic correction?
compute/lib/curved_sc_higher_genus_engine.py:1003:    """Verify that anomaly cancellation (kappa_eff = 0) gives flat bar complex.
compute/lib/curved_sc_higher_genus_engine.py:1010:    At the critical dimension c = 26: kappa_eff = 26/2 + (-13) = 0.
compute/lib/curved_sc_higher_genus_engine.py:1012:    AP29: kappa_eff = kappa(matter) + kappa(ghost), not kappa + kappa!.
compute/lib/curved_sc_higher_genus_engine.py:1014:    kappa_eff = kappa_matter + kappa_ghost
compute/lib/curved_sc_higher_genus_engine.py:1015:    curv_eff = kappa_eff * lambda_fp(genus) if genus >= 1 else Fraction(0)
compute/lib/curved_sc_higher_genus_engine.py:1019:        'kappa_eff': kappa_eff,
compute/lib/curved_sc_higher_genus_engine.py:1021:        'anomaly_cancelled': kappa_eff == Fraction(0),
compute/lib/bcov_mc_complete_proof_engine.py:155:    AP20: kappa is intrinsic to A, not to a system; kappa != kappa_eff
compute/lib/bcov_mc_complete_proof_engine.py:158:    AP29: delta_kappa = kappa - kappa' != kappa_eff = kappa(matter) + kappa(ghost)
compute/lib/bc_connes_spectral_shadow_engine.py:60:  AP20: kappa(A) vs kappa_eff distinction.
compute/lib/lattice_model_shadow_engine.py:1236:    kappa_eff = shadow_coeffs[max_arity]
compute/lib/lattice_model_shadow_engine.py:1240:        return np.sqrt(abs(kappa_eff)) * (2 * n + 1)
compute/lib/lattice_model_shadow_engine.py:1244:        C = (abs(kappa_eff) * gamma_func(1.5) * gamma_func(1 + 1.0 / M)

thinking
**Inspecting the search result**

I just found a file called `theorem_multi_weight_generating_function_engine.py`, which could potentially hold some valuable insights regarding the obstruction related to single variable or `kappa_eff`. I need to take a closer look at this file to understand how it connects to what I’m trying to achieve. There’s likely some important information in there that could help clarify things further! Let's dive into this and see what I can uncover.
exec
/bin/zsh -lc "sed -n '1,140p' compute/lib/theorem_multi_weight_generating_function_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "irreducibly bivariate|single number|kappa_eff|not generated by|hatA|closed-form" compute/lib/theorem_multi_weight_generating_function_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Multi-weight cross-channel generating function analysis.

THEOREM-PROVING ENGINE: analyzes the generating function structure of
the cross-channel corrections delta_F_g^{cross}(W_N, c) at genera 2, 3, 4.

MATHEMATICAL SETUP
==================

For multi-weight modular Koszul algebras (W_N with N-1 generators of
conformal weights 2, 3, ..., N), the genus expansion has the form:

    F_g(A) = kappa(A) * lambda_g^FP + delta_F_g^cross(A)

The cross-channel correction vanishes for uniform-weight algebras (N=2,
Virasoro) and is generically nonzero for N >= 3.

KNOWN DATA (from prior engines, all PROVED by graph sum + verification):

  Genus 2 (W_N universal):
    delta_F_2(W_N, c) = B_2(N) + A_2(N)/c
 succeeded in 52ms:
67:     as f(c) * g(hbar). It is an irreducibly bivariate function.
117:# Cross-channel correction data: closed-form formulas from prior engines
537:    Test: does sum_g delta_F_g * hbar^{2g} = f(hbar, c) for some closed-form f?
846:    """Master analysis: does delta_F_g have a closed-form generating function?
886:            'delta_F_g(c, hbar) is an irreducibly bivariate function: '
exec
/bin/zsh -lc "sed -n '1,120p' compute/lib/betagamma_genus2_cross_channel_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '840,915p' compute/lib/theorem_multi_weight_generating_function_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Betagamma genus-2 cross-channel engine: Mumford vanishing theorem.

THEOREM (betagamma cross-channel vanishing)
===========================================

For the bosonic betagamma system at conformal weights (lambda, 1-lambda),
the cross-channel correction vanishes at ALL genera:

    delta_F_g^cross(betagamma, lambda) = 0    for all g >= 1.

Consequently the scalar formula holds exactly:

    F_g(betagamma, lambda) = kappa(lambda) * lambda_g^FP

where kappa(lambda) = c_bg(lambda)/2 = 6*lambda^2 - 6*lambda + 1 and
lambda_g^FP is the Faber--Pandharipande intersection number.

PROOF SKETCH
============

 succeeded in 51ms:

# ============================================================================
# 10. MASTER SUMMARY
# ============================================================================

def generating_function_verdict() -> Dict[str, object]:
    """Master analysis: does delta_F_g have a closed-form generating function?

    Collects evidence from all analysis modules.
    """
    ratio = ratio_analysis_W3()
    denom = denominator_analysis_W3()
    leading = leading_coefficient_analysis_W3()
    ahat = test_ahat_ansatz_W3()
    sep = test_separability_W3()
    factorial = test_factorial_growth_W3()

    verdict = {
        'ratio_constant': ratio['ratio_32_constant'],
        'ratio_polynomial': ratio['ratio_32_polynomial_in_c'],
codex
One point is now clear enough to lock before writing: the repo does not support the premise that `\beta\gamma` has nonzero `\delta F_g^{\mathrm{cross}}`. The live theorem surface and compute layer both treat `\beta\gamma` as a multi-weight free-field exact exception with `\delta F_g^{\mathrm{cross}}=0`, so the new remark has to separate interacting multi-weight families from free-field multi-weight exceptions.



thinking
**Deciding on research remarks**

I need to figure out the best way to show the user if there’s a misunderstanding. I should look for existing research remarks regarding multi-generation independence. It might make sense to insert a Research Remark after `rem:multi-gen-independence`, especially since that follows the statement decomposition and relates to Theorem D and C2 condition removal. There's also a negative universality remark, so it would help to survey the current state early on. Let's clarify this!
thinking
**Refining remark placements**

I’m considering where to place a remark—maybe near `rem:theorem-d-alt-grr` or `rem:mc2-status`, perhaps next to Theorem D. The remark could explain how Theorem D and C2 can be adjusted from uniform-weight to explicit decomposition, but C2 remains restricted due to tautological-line support. Since the multi-weight theorem relates closely to these concepts, adding it near 22600 makes sense for citation. However, because the user requested a Research Remark, any location might work as long as I reference D and C2. I should investigate the current state of multi-weight computations too.
thinking
**Investigating gravitational formulas**

I'm looking into the W_N gravitational Frobenius and aiming for a genus-2 explicit closed-form universal formula. I know there's an exact explicit formula for W_3 when g=2, but I need to check if there are explicit formulas for g=3 and g=4 as well. I'll inspect the contents of compute/lib/multi_weight_genus_tower or theorem_multi_weight_generating_function_engine. It's essential to search the manuscript for those g=3 and g=4 formulas to see what I can find there!
exec
/bin/zsh -lc 'rg -n "Pixton|tautological line|one-channel sector|all-genera scalar trace package|multi-weight families" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:tautological-line-support" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9820,10035p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5803:one-channel sector.
6072: so $\mathbf{D}_g$ and $\mathbf{D}_g^!$ are one-channel sectors of
6097:chain-model construction on the MC2 one-channel sector of
6226:differential-closed spans realize the one-channel sector and whose
6830:In particular, once the one-channel sector admits such a root-string
8028:the tautological line $\mathbb{C}\lambda_g$ and matching one normalized
8064:tautological line via clutching/trace isolation, then reduce
8103: tautological line
8182: tautological line, by
8190:multi-weight families with simple Lie symmetry, parts
8768:general multi-weight families, including principal
8820: general for multi-weight families.
9153:where $\Gamma_{\cA}$ denotes the tautological line coefficient
9203:tautological-purity gap for multi-weight families.
9944:\index{MC2!tautological line support}
10045:\textup{(}c\textup{)} If Pixton-type relations separate the
10046:relevant one-channel sector, then
10050:for arbitrary multi-weight families.
10067:For arbitrary multi-weight families, only the genus-$1$ comparison is
22275:Pandharipande--Pixton--Zvonkine. The unit axiom
 succeeded in 50ms:
\begin{remark}[Evidence and scope of
Conjecture~\ref{conj:scalar-saturation-universality}]
\label{rem:scalar-saturation-evidence}
\index{scalar saturation!evidence}
\index{universal Maurer--Cartan class!evidence for universality}
The conjecture is proved at generic level for all vertex algebras
with simple symmetry (Theorem~\ref{thm:cyclic-rigidity-generic}),
at all non-critical levels for algebraic families with rational
OPE coefficients
(Theorem~\ref{thm:algebraic-family-rigidity}),
and on the standard Lie-theoretic landscape in the weaker
effective-\(\Gamma\)-quadruple form
(Corollary~\ref{cor:effective-quadruple}).
The algebraic-family theorem subsumes the generic-level result
and extends it to admissible parameter values only for the
already verified algebraic-family objects in the standard
Lie-theoretic landscape \textup{(}not for the live audit surface
of simple admissible quotients\textup{)}.
What remains open outside the proved uniform-weight scalar lane is
the tautological-purity step
 succeeded in 52ms:
5279:Theorem~\ref{thm:tautological-line-support},
5750:Theorem~\ref{thm:tautological-line-support}); for
8107: Theorem~\textup{\ref{thm:tautological-line-support}}.\textup{]}
8183: Theorem~\textup{\ref{thm:tautological-line-support}}.
8205:Theorem~\ref{thm:tautological-line-support}.
8210:of Theorem~\ref{thm:tautological-line-support}.
9943:\ClaimStatusProvedHere]\label{thm:tautological-line-support}
10066:MC2-3 by Theorem~\textup{\ref{thm:tautological-line-support}}.
10075:Theorem~\ref{thm:tautological-line-support}, and

thinking
**Inspecting multi-weight families**

I find line 31971 interesting as it mentions multi-weight families and their relation to parameters like $\mathcal{W}_3$ and $\beta\gamma$ when λ≠1/2. I’m wondering if I need to check if delta is nonzero, too. It may involve families with multiple generators. I think I'll also look around line 31960 since it could be relevant—possibly regarding cross-volume. I’ll definitely inspect this further later!
codex
I’ve now pinned the C2 blocker more precisely. For Theorem D, the scalar free-energy correction is already a theorem on the multi-weight surface; for C2, the missing piece is stronger: a class-valued lift of the mixed-channel graph sum into the tautological obstruction space, not just a scalar evaluation.
exec
/bin/zsh -lc "sed -n '1,220p' compute/lib/mumford_chiodo_multiweight_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Mumford-Chiodo formula for multi-weight Hodge classes at genus 2.

PURPOSE: Compute c_k(E_h) for h = 1, 2, 3 at genus 2, where
E_h = R^0 pi_* omega^{otimes h} is the bundle of weight-h differentials
on Mbar_g.  This is the crux of op:multi-generator-universality.

=== MATHEMATICAL FRAMEWORK ===

1. Mumford's GRR (1983, Thm 5.10) gives ch_k(E_h) as a polynomial in h:

   ch_k(E_h) = B_{k+1}(h)/(k+1)! * kappa_k   [interior, smooth fibers]
             + (boundary corrections from delta_irr and delta_i)

   where B_n(x) is the n-th Bernoulli polynomial.

2. The Mumford isomorphism gives c_1(E_h) = e(h) * lambda_1 where
   e(h) = 6h^2 - 6h + 1.  This is EXACT on all of Mbar_g (including boundary).

3. At genus 2, the Chow ring R^*(Mbar_2) is generated (rationally) by
   lambda_1, lambda_2, delta_irr, delta_1 subject to known relations.
exec
/bin/zsh -lc "rg -n -F \"beta\\gamma\" chapters/theory/higher_genus_modular_koszul.tex | head -n 20" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '31950,31995p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
701:\item the free fermion algebra $\mathcal{F}$ and the $\beta\gamma$-$bc$
2207:The $\beta\gamma$-$bc$ system at non-integer spin
2210:$\beta\gamma$ ghost with $\lambda = 0$ or $1$\textup{)},
2480:\textup{(}the entire standard landscape except integer-spin $\beta\gamma$, where hypothesis~\textup{(a)} fails\textup{)},
2723:($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.
3225:$\beta\gamma$/$bc$, and $K3 \times E$). The universality
3331:\begin{remark}[$\beta\gamma$ and $bc$: ghost slabs]
3333:\index{beta-gamma system@$\beta\gamma$ system!Brown--Henneaux}%
3335:For the $\beta\gamma$ system of conformal weight~$\lambda$,
3336:$\kappa(\beta\gamma) = c_{\beta\gamma}/2
3340:$\kappa_{\mathrm{tot}}(\beta\gamma\,{\otimes}\,bc) = 0$
3346:$\beta\gamma$-$bc$ slab is Koszul self-dual with
3567:The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
4276:at~$3$, $\beta\gamma$ at~$4$; Virasoro at~$\infty$),
12349:$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
12422: {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
12739:($\beta\gamma$); the Virasoro tower is infinite.
13825:$\beta\gamma$ & $\checkmark$ & gauge-trivial & $\checkmark$ (quartic) \\
13830:For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
13835:$\mu_{\beta\gamma} = 0$
 succeeded in 50ms:
 & $0$ & $\tfrac{31}{967680}$ & G \\
\hline
$\widehat{\mathfrak{sl}}_{2,k=1}$ & $\tfrac{9}{4}$ & $\tfrac{7}{2560}$
 & $\tfrac{133}{432}$ & $\tfrac{31}{430080}$ & L \\
\hline
$V_{E_8}$ & $8$ & $\tfrac{7}{720}$
 & $0$ & $\tfrac{31}{120960}$ & G \\
\hline
$\mathrm{Vir}_{25}$ & $\tfrac{25}{2}$ & $\tfrac{35}{2304}$
 & $\tfrac{5}{16}$ & $\tfrac{155}{387072}$ & M \\
\hline
$\mathcal{W}_{3,c{=}50}$\textsuperscript{$\ddagger$} & $\tfrac{125}{3}$ & $\tfrac{875}{17280}$
 & $-\tfrac{5}{24}$ & $\tfrac{775}{580608}$ & M \\
\hline
$\beta\gamma_{\lambda=1}$ & $1$ & $\tfrac{7}{5760}$
 & $0$ & $\tfrac{31}{967680}$ & C \\
\hline
\end{tabular}
}% end small
\end{table}

thinking
**Considering data consistency**

The user wants to fortify something, and I think we might need to address this inconsistency as part of the healing process. However, the table remark could be unrelated to the main target. I'll need to look around line 31971 to fully understand what's happening. It's possible that the table for scalar-lane values is outdated. Adding a remark might hinge on clarifying the beta-gamma relationship, so I’ll look at the surrounding lines for more context.
codex
I found a live drift inside the same chapter: one later table note still says multi-weight `\beta\gamma` is conditional at `g\ge2`, while the proved free-field exactness theorem earlier in the file says `\delta F_g^{\mathrm{cross}}(\beta\gamma)=0` for all genera. I’m reading that local block now; if it is just stale wording, I’ll repair it in the same pass so the new remark doesn’t sit on a contradictory surface.
exec
/bin/zsh -lc "sed -n '31955,31990p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$V_{E_8}$ & $8$ & $\tfrac{7}{720}$
 & $0$ & $\tfrac{31}{120960}$ & G \\
\hline
$\mathrm{Vir}_{25}$ & $\tfrac{25}{2}$ & $\tfrac{35}{2304}$
 & $\tfrac{5}{16}$ & $\tfrac{155}{387072}$ & M \\
\hline
$\mathcal{W}_{3,c{=}50}$\textsuperscript{$\ddagger$} & $\tfrac{125}{3}$ & $\tfrac{875}{17280}$
 & $-\tfrac{5}{24}$ & $\tfrac{775}{580608}$ & M \\
\hline
$\beta\gamma_{\lambda=1}$ & $1$ & $\tfrac{7}{5760}$
 & $0$ & $\tfrac{31}{967680}$ & C \\
\hline
\end{tabular}
}% end small
\end{table}

\noindent
The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
these are conditional at $g \geq 2$

thinking
**Inspecting wording**

I think there's stale wording that needs fixing. I should check if there are other stale beta-gamma conditional references in the file or repository. I’ll search for “beta\gamma” alongside “conditional” to see if there are more instances. Using the command “rg around `conditional at g`” might help identify where these issues are hiding. It's important to ensure clarity and avoid any confusion in the language.
exec
/bin/zsh -lc "rg -n \"beta\\\\gamma.*conditional|conditional at \\"'$g '"\\\\geq 2\\"'$|Multi-weight: .*g '"\\\\geq 2|delta_F_g\\"'^'"\\{\\\\mathrm\\{cross\\}\\}\\\\(\\\\beta\\\\gamma|free-field exact|prop:free-field-scalar-exact\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:beta\gamma.*conditional|conditional at $g \geq 2$|Multi-weight: .*g \geq 2|delta_F_g\^\{\mathrm\{cross\}\}\(\beta\gamma|free-field exact|prop:free-field-scalar-exact)
           ^^
error: unrecognized escape sequence

thinking
**Considering command options**

I'm thinking about how to use multiple fixed string regex patterns, possibly with the `-F` flag for simplicity. I might use `rg -n -F` for multiple patterns, but I wonder if I could consolidate it with a single exec using several `rg` calls. I want to be efficient and effective in how I approach this command execution. Let’s explore which method will yield the best results for the task at hand!
exec
/bin/zsh -lc 'rg -n -F "conditional at $g '"\\geq 2"'$" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F "Multi-weight: $F_g$ conditional at $g '"\\geq 2"'$" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F "delta_F_g''^{'"\\mathrm{cross}}(\\beta\\gamma\" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F \"prop:free-field-scalar-exact\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2732:Proposition~\ref{prop:free-field-scalar-exact}.
5757:exact by Proposition~\ref{prop:free-field-scalar-exact}.
22448:\label{prop:free-field-scalar-exact}
22625:Proposition~\ref{prop:free-field-scalar-exact}, the scalar formula

thinking
**Troubleshooting search parameters**

I’m trying to figure out why there are no matches. I wonder if the dollar signs in the shell are causing the issue, but it looks like that’s not the problem. I’ll try searching for “beta-gamma” and “free-field exact” as these might be enough. There’s also a stale line that could be the only issue. I should inspect around `rem:propagator-weight-universality` to see if that’s conditional or needs updating. I'll search by label too.
exec
/bin/zsh -lc 'rg -n -F "rem:propagator-weight-universality" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
28678:Remark~\ref{rem:propagator-weight-universality}).
28708:Remark~\ref{rem:propagator-weight-universality}).
31975:(Remark~\ref{rem:propagator-weight-universality}).
exec
/bin/zsh -lc "sed -n '28640,28725p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\kappa(\operatorname{Sym}^N(\cA))
= N \cdot \kappa(\cA)$.

\emph{Proof~$2$ \textup{(}DMVV/Borcherds product\textup{)}.}
The DMVV formula~\cite{DMVV97} gives
$\sum_{N \geq 0} p^N Z(\operatorname{Sym}^N(\cA);\tau)
= \prod_{n,m > 0}(1 - q^n p^m)^{-c(nm)}$.
The connected genus-$1$ free energy
$F_1(\operatorname{Sym}^N) = \kappa(\operatorname{Sym}^N)/24$
is extracted from the logarithm of the product at leading
$q$-order. The $N$-linear coefficient in
$\log \sum p^N Z = \chi(\cA) \sum_{N \geq 1}
\sigma_{-1}(N)\,p^N + \cdots$
identifies
$\kappa(\operatorname{Sym}^N) = N\cdot\kappa(\cA)$,
since subleading Hecke images contribute to the
partition function but not to the obstruction class.

\emph{Proof~$3$ \textup{(}Hecke operators\textup{)}.}
The symmetric orbifold partition function is the


thinking
**Considering proof modifications**

I'm thinking that I might not need to write new proofs if I'm blocked, but I should sketch some ideas instead. The user wants a Research Remark, and while I can't change theorem proofs, the final report should talk about the statuses of D and C2. I could refer to Theorem D's secondary proof via GRR and C2's comparison. However, I’m unsure if I need to write new proofs at all, especially since there’s already an alternative for D.
thinking
**Searching physics references**

I need to search for `delta_F_g^{\mathrm{cross}}` and `beta\gamma`, and see if there are any relevant mentions. I’m thinking about using exec across paths. I’ll also look for any references to theorem D. It might make sense to use commentary first before diving into my plan update, but I want to ensure I have enough context before doing that. Let’s get started!
codex
I have enough context to draft. The edit will do two things in one pass: add a research remark at the multi-weight theorem surface that cleanly separates what is proved, computed, and still conjectural for removing the uniform-weight hypothesis from Theorem D and C2, and repair the stale `\beta\gamma` note later in the chapter so the file stops contradicting its own free-field exactness theorem.

Pre-edit verification for the hot zones:

```text
PE-10 scope quantifier
genus: [all, with g=1 universal and g>=2 multi-weight correction]
degree: [n=0 for free-energy scalar package; obstruction classes in all genera]
AP32 weight tag: [(UNIFORM)/(ALL+delta)/NA]  tagged? [Y]
AP139 free-var audit: LHS vars:{g,\cA} RHS vars:{g,\cA} LHS⊇RHS? [Y]
AP36: [implies/iff]  if iff, converse proved same thm? [Y, only when citing thm:multi-weight-genus-expansion / identified as research programme otherwise]
verdict: ACCEPT
```

```text
PE-8 cross-volume formula
formula: [obs_g = kappa lambda_g on the uniform-weight lane; multi-weight correction delta_F_g^{cross}]
Vol I: [multiple hits, canonical theorem + multi-weight expansion]  Vol II: [uniform-weight + correction caveat]  Vol III: [bridge restatement of same caveat]
consistent? [Y, except beta-gamma stale wording found in Vol I local table note]
if not: canonical vol [I], others updated same session? [pending, will re-grep after edit]
convention conversion: [NA]
verdict: ACCEPT
```

```text
PE-7 label creation
environment: [remark]
label: \label{rem:theorem-d-c2-multiweight-programme}
prefix match (AP125): [Y]
AP124 duplicate check: Vol I:[0] Vol II:[0] Vol III:[0] total before:[0] after:[1] delta=1? [Y]
verdict: ACCEPT
```

thinking
**Checking for duplicates**

I need to perform an actual duplicate check using rg, and I realize I haven't done that yet. Before claiming zeros, it makes sense to run rg across the volumes. I should make sure to conduct a thorough search to cross-check any stale wording across those volumes. It's important to ensure everything is accurate before proceeding. Let’s go through this methodically!
exec
/bin/zsh -lc 'rg -n -F "rem:theorem-d-c2-multiweight-programme" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar exited 1 in 97ms:

exec
/bin/zsh -lc "rg -n \"beta\\\\gamma.*conditional at .*g|beta\\\\gamma.*delta F_g|multi-weight families .*beta\\\\gamma|beta\\\\gamma.*uniform-weight|free-field exact\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:beta\gamma.*conditional at .*g|beta\gamma.*delta F_g|multi-weight families .*beta\gamma|beta\gamma.*uniform-weight|free-field exact)
           ^^
error: unrecognized escape sequence
codex
I’m verifying the label uniqueness now and checking whether the `\beta\gamma` drift is local or cross-volume. If the stale wording appears elsewhere, I’ll either propagate the repair in this session or leave an explicit pending note naming the untouched collision surface.
exec
/bin/zsh -lc "rg -n -F \"beta\\\\gamma\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 189ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:360:$\beta\gamma$ & fixed & $0$ & (always self-dual) \\[2pt]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:371:The affine lineage ($\hat{\mathfrak{g}}_k$, $\cH_k$, $\beta\gamma$)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:657:C & $4$ & $\beta\gamma$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:686:C & $\beta\gamma$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:717:The $\beta\gamma$ system has $r_{\max} = 4$: the quartic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:718:contact invariant $\mathfrak{Q}^{\mathrm{contact}}_{\beta\gamma}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:2095:C & $\beta\gamma$ & $4$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:2097: & (contact-corrected Fredholm) & $\mathfrak{Q}_{\beta\gamma}$ \\[2pt]
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:237:For $\beta\gamma$/$bc$: the Koszul duality exchanges
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:238:statistics ($bc^! = \beta\gamma$, $\beta\gamma^! = bc$),
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:681: For $\beta\gamma$/$bc$: the Koszul duality exchanges
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:774: For $\beta\gamma$/$bc$: the Koszul duality exchanges
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:775: statistics ($bc^! = \beta\gamma$, $\beta\gamma^! = bc$),
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:857: For $\beta\gamma$/$bc$: the Koszul duality exchanges
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:858: statistics ($bc^! = \beta\gamma$, $\beta\gamma^! = bc$),
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:1030: For $\beta\gamma$/$bc$: the Koszul duality exchanges
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:1031: statistics ($bc^! = \beta\gamma$, $\beta\gamma^! = bc$),
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:1129: For $\beta\gamma$/$bc$: the Koszul duality exchanges
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:1130: statistics ($bc^! = \beta\gamma$, $\beta\gamma^! = bc$),
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:1233: For $\beta\gamma$/$bc$: the Koszul duality exchanges
exec
/bin/zsh -lc 'rg -n -F "free-field-scalar-exact" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 55

/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/S07_preface_to_intro.md:182:chapters/theory/introduction.tex:96:(Proposition~\ref{prop:free-field-scalar-exact}).
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/S07_preface_to_intro.md:225:/bin/zsh -lc "rg -n 'thm:modular-koszul-duality-main|thm:quantum-complementarity-main|thm:modular-characteristic|thm:genus-universality|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:riccati-algebraicity|prop:chirhoch1-affine-km|conj:v1-drinfeld-center-equals-bulk|thm:topologization|conj:topologization-general|warn:multiple-e1-chiral|princ:geometric-origin-hochschild|conv:three-hochschild' metadata/theorem_registry.md chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/S07_preface_to_intro.md:229:chapters/frame/preface.tex:1058:(Proposition~\ref{prop:free-field-scalar-exact}): the bar spectral
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/S07_preface_to_intro.md:239:chapters/frame/preface.tex:2972:(Proposition~\ref{prop:free-field-scalar-exact}).
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1375:(Proposition~\ref{prop:free-field-scalar-exact}).
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1432:    96	(Proposition~\ref{prop:free-field-scalar-exact}).
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1439:I need to verify if the `free-field-scalar-exact` proposition includes g≥1 or encompasses all genera. It’s not clear to me right now, so I think it’s crucial to take a moment to look into this further. Searching should help clarify, and I’ll pay attention to the details to ensure I understand how these elements interact. Let’s see what I can find!
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1441:/bin/zsh -lc "rg -n -F '\\label{prop:free-field-scalar-exact}' chapters/examples/genus_expansions.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/free_fields.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1442:chapters/theory/higher_genus_modular_koszul.tex:21948:\label{prop:free-field-scalar-exact}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1453:\label{prop:free-field-scalar-exact}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1785:    96	(Proposition~\ref{prop:free-field-scalar-exact}).
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC06_genus_0.md:1912: 21948	\label{prop:free-field-scalar-exact}
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R13_introduction.md:587:(Proposition~\ref{prop:free-field-scalar-exact}).
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R13_introduction.md:743:(Proposition~\ref{prop:free-field-scalar-exact}).
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C02_introduction.md:626:./wave2_audit_20260413_001942/S07_preface_to_intro.md:225:/bin/zsh -lc "rg -n 'thm:modular-koszul-duality-main|thm:quantum-complementarity-main|thm:modular-characteristic|thm:genus-universality|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:riccati-algebraicity|prop:chirhoch1-affine-km|conj:v1-drinfeld-center-equals-bulk|thm:topologization|conj:topologization-general|warn:multiple-e1-chiral|princ:geometric-origin-hochschild|conv:three-hochschild' metadata/theorem_registry.md chapters/frame/preface.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C02_introduction.md:628:./wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:1109:./wave2_audit_20260413_001942/S06_intro_to_body.md:341:/bin/zsh -lc "rg -n '\\\\label\\{(thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-characteristic|thm:riccati-algebraicity|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:mc2-bar-intrinsic|thm:bar-nilpotency-complete|prop:pole-decomposition|thm:fundamental-twisting-morphisms|thm:bar-concentration|thm:koszul-equivalences-meta|thm:universal-generating-function|thm:spectral-characteristic|thm:hochschild-polynomial-growth|lem:chirhoch-descent|thm:e1-primacy|thm:thqg-swiss-cheese|cor:shadow-visibility-genus|rem:two-orthogonal-axes|thm:central-charge-complementarity)\\}' chapters appendices metadata" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C02_introduction.md:631:./wave2_audit_20260413_001942/S06_intro_to_body.md:341:/bin/zsh -lc "rg -n '\\\\label\\{(thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-characteristic|thm:riccati-algebraicity|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:mc2-bar-intrinsic|thm:bar-nilpotency-complete|prop:pole-decomposition|thm:fundamental-twisting-morphisms|thm:bar-concentration|thm:koszul-equivalences-meta|thm:universal-generating-function|thm:spectral-characteristic|thm:hochschild-polynomial-growth|lem:chirhoch-descent|thm:e1-primacy|thm:thqg-swiss-cheese|cor:shadow-visibility-genus|rem:two-orthogonal-axes|thm:central-charge-complementarity)\\}' chapters appendices metadata" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:303:  5392	exact by Proposition~\ref{prop:free-field-scalar-exact}.
exec
/bin/zsh -lc 'rg -n -F "prop:cross-channel-growth" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F "prop:cross-channel-no-closed-form" chapters/theory/higher_genus_modular_koszul.tex
rg -n -F "rem:spectral-curve-obstruction" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
24271:\label{prop:cross-channel-growth}%
24419:\label{prop:cross-channel-no-closed-form}%
24341:\label{rem:spectral-curve-obstruction}%








thinking
**Considering remark placement**

I'm inspecting the best spot for a remark about "multi-gen-independence" and "cross-channel-no-closed-form." Since the remark refers to current state and research, placing it after "rem:multi-gen-independence" might work, as it introduces a new invariant. However, the later chapter discusses more about cross-channel growth which could enhance the remark if it's inserted after subsequent propositions. But since the user asked specifically about Theorems D and C2, I'll consider incorporating later results in the remark too. It's essential that the references compile correctly.
thinking
**Planning remark structure**

I could place the remark after "rem:multi-gen-independence" since it's where I resolve the open problem and identify a new invariant. The remark could explain that removing uniform weight means replacing the scalar theorem with a corrected version, and later propositions analyze "delta." It should carefully avoid claiming that Theorems D and C2 are unconditional; rather, I’ll state that D can be weakened to a proven free-energy statement, while C2 needs more work. I may structure the remark as concise paragraphs with an explicit list and include known results and research plans, using LaTeX for clarity.
thinking
**Considering compute modules**

I might need to mention the compute modules clearly, as the user is interested in the current state of compute/lib. I think it's important to include a note in the manuscript about this, but not to overwhelm with too much detail. Adding references in `\texttt{}` format could be helpful. I could say something like: "Current compute support is partial but concrete," listing specific modules and their functions. It may be a bit technical, but it fits in the research context.
thinking
**Structuring the research program**

It looks like they’re already using `\texttt{}` in remarks, which is great! I should consider enumerating the research program into clear sections: 

(a) lift mixed-channel graph sum to class-valued CohFT amplitudes,  
(b) prove clutching and R-matrix independence at class level,  
(c) identify the smallest tautological sector and replace MC2-3, and  
(d) prove semisimple/PPZ/Pixton separation to derive `obs_g`.  

Also, I think I should touch on the current state of multi-weight computations, including the universal genus-2 W_N gravitational formula and associated checks, noting that (b) is computable.
thinking
**Updating table notes**

I’m working through some technical details for the table regarding multi-weight families. Currently, I want to clarify that for interacting multi-weight families, the conditions apply at \(g \geq 2\). However, I need to change how I present the exceptions related to free-field multi-weight cases like \(\beta\gamma\). Also, I’m thinking about updating the footnote since it might not accurately reflect the conditions in the row for \(\mathcal{W}_{3,c=50}^{\ddagger}\). I need to ensure the scalar lane values are distinct from conditional ones.
thinking
**Revising notes on F_g**

I need to correct the interpretation of the W3 row values; they likely represent the scalar part `\kappa \lambda_g^FP`, not the actual total F_g. The footnote should specify this. The W3 row, with kappa=125/3 and F2=875/17280, indicates this scalar part. The total F_g differs due to the inclusion of delta. So, I'll revise the note to clarify these points about scalar values and interactions in multi-weight families, particularly for genus at g≥2.
thinking
**Clarifying multi-weight exceptions**

I’m examining the free-field multi-weight exceptions, including \beta\gamma, which are precise according to Proposition\ref{prop:free-field-scalar-exact}. The footnote should indicate that the interacting multi-weight row only records the scalar part \kappa \cdot \lambda_g^{FP} and adds \delta F_g^{\mathrm{cross}} for total free energy, clearing up the wording for W3. I need to check if this footnote has duplicates elsewhere or if there are any stale lines in cross-volume references that might need updates.
thinking
**Updating cross-volume notes**

I’m considering that maybe there's no need for propagation. However, the cross-volume rule states that after a mathematical change, I should search through all volumes to update any duplicates or leave a clear pending note if I find them. It’s crucial to keep everything aligned across the documentation, so I’ll follow this guideline and check if any notes require updating or if I need to mark something as pending. Keeping things organized is vital!
codex
I’m expanding the scope slightly to keep the claim surface coherent. Adding a new labeled remark will otherwise leave metadata drift behind, so I’m loading the claim-surface sync workflow before I edit.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:

thinking
**Considering metadata updates**

We changed the remark, but I’m not sure about the truth of the claim; maybe it’s just low priority. Adding a label definitely involves metadata, so I might update the theorem_registry if there’s a script available. I’ll need to inspect metadata files, particularly something like `label_index.json`. It's possible a manual edit isn't necessary, but I want to verify the metadata was generated correctly. I might run a script like `python3 scripts/extract_theorems.py` to regenerate it. Let me search for relevant scripts.
exec
/bin/zsh -lc "ls metadata | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "theorem_registry|label_index|claims.jsonl|metadata" scripts . | head -n 80' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
census.json
claims.jsonl
dependency_graph.dot
label_index.json
theorem_registry.md
verified_formulas.jsonl
 succeeded in 51ms:
scripts/healing_fortification_40.py:644:agent("H32_theorem_registry_rebuild", """REBUILD the theorem registry from scratch.
scripts/healing_fortification_40.py:646:TARGET: metadata/theorem_registry.md
./healing_20260413_132214/H04_thm_D_alt_proof.md:115:I'm thinking about whether I should create a label for a remark regarding theorem D. It seems like I might not need metadata unless a label is used, but if I create a label, it needs to be unique. If there’s no direct reference to it, I could avoid the label altogether. However, since it is close to theorem D, a label might be helpful, but I also want to minimize any potential issues.
./healing_20260413_132214/H04_thm_D_alt_proof.md:165:/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
./healing_20260413_132214/H04_thm_D_alt_proof.md:211:Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.
./healing_20260413_132214/H04_thm_D_alt_proof.md:245:- `metadata/theorem_registry.md`
./healing_20260413_132214/H04_thm_D_alt_proof.md:745:./metadata/label_index.json:9486:  "eq:bar-family": {
./healing_20260413_132214/H04_thm_D_alt_proof.md:882:I'm considering my options for compiling the LaTeX document. I could potentially use grep for searching or maybe just a simple `latexmk` command to compile it to PDF, but that seems too resource-intensive. A local grep approach might make more sense here. I’m also thinking about running a Python script to generate metadata, but I’m not convinced that’s the right move either. I guess I’ll need to weigh these options carefully.
./healing_20260413_132214/H04_thm_D_alt_proof.md:2143: M metadata/census.json
./healing_20260413_132214/H04_thm_D_alt_proof.md:2144: M metadata/claims.jsonl
./healing_20260413_132214/H04_thm_D_alt_proof.md:2145: M metadata/dependency_graph.dot
./healing_20260413_132214/H04_thm_D_alt_proof.md:2146: M metadata/label_index.json
./healing_20260413_132214/H04_thm_D_alt_proof.md:2147: M metadata/theorem_registry.md
./healing_20260413_132214/H07_MC5_alt_approach.md:176:/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
./healing_20260413_132214/H07_MC5_alt_approach.md:194:- `metadata/theorem_registry.md`
./healing_20260413_132214/H07_MC5_alt_approach.md:202:Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.
./healing_20260413_132214/H07_MC5_alt_approach.md:1464:For verification, I could run `git diff` to check changes, but it only shows the last patch. Running `git blame` might help, though it may not be necessary. I might also check the label in the metadata file.
./healing_20260413_132214/H07_MC5_alt_approach.md:1482:I need to put together a report in one paragraph, but it might be tricky since the build didn’t complete due to an unrelated error. I should mention that “metadata not regenerated” might not be necessary if there’s no label change. I’ll also need to include “PRIMARY PROOF sound” despite the build failure. It’s important to keep things concise while ensuring I cover what's required in the report. Let's do this!
./healing_20260413_132214/H02_thm_B_alt_proof.md:163:/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
./healing_20260413_132214/H02_thm_B_alt_proof.md:181:- `metadata/theorem_registry.md`

thinking
**Considering skill usage**

I think I need to use the build-surface skill, especially since the task involves verifying metadata regeneration and conducting targeted checks. It seems like loading that skill would be the right move here to ensure everything's set up properly. I want to make sure I’m approaching this task correctly, so I'll focus on getting the necessary tools ready for effective processing!
codex
The label surface is generated, so I’m treating metadata regeneration as part of verification rather than as optional cleanup. I’m loading the build-surface workflow and then making the edit.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
codex
I’m applying the chapter edit now. It adds the research remark at the multi-weight obstruction surface and rewrites the later table note so the file no longer misclassifies `\beta\gamma` as an interacting multi-weight obstruction case.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -22638,2 +22638,137 @@
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
@@ -31967,6 +32102,12 @@
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
@@ -31983,3 +32124,5 @@
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 40ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..02b5d813f848024c4cc33a7e2ae0b005841e5881
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..02b5d813f848024c4cc33a7e2ae0b005841e5881
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]


thinking
**Verifying content accuracy**

I need to verify the content around the remark I inserted and make some notes. It might be a good idea to grep for any forbidden formulas. I’m considering running rg for a new label, like a beta gamma note, and checking for any banned prose. I'll have to re-read the changed sections, and I might also need to run latex or generate some metadata. Making sure everything is clear here is essential!
codex
The patch is in. I’m re-reading the exact edited blocks now and then I’ll run the narrow checks: label/refs grep, metadata regeneration, and a lightweight search for theorem-surface drift introduced by the new notation.
exec
/bin/zsh -lc "sed -n '22600,22735p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{proof}

\begin{remark}[Resolution of the multi-generator universality problem]%
\label{rem:multi-gen-independence}%
\index{multi-generator obstruction!resolution}%
The three-step rigidity package
(A:~algebraic-family rigidity, B:~Kuranishi parity,
C:~Heisenberg calibration)
was designed to prove the scalar formula
$F_g(\cA) = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}$
at all genera. Steps~(A) and~(B) give
$\Theta_{\cA}^{\min} = \eta\otimes\Gamma_{\cA}$
(Theorem~\ref{thm:algebraic-family-rigidity}), but do not
identify the tautological coefficient~$\Gamma_{\cA}$.
Step~(C) gives $\Gamma_{\cH_\kappa} = \kappa\Lambda$ on
the uniform-weight lane.

Theorem~\ref{thm:multi-weight-genus-expansion} resolves
Open Problem~\textup{\ref{op:multi-generator-universality}}
in the \emph{negative} for interacting multi-weight algebras:
exec
/bin/zsh -lc "sed -n '31963,31992p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"beta\\gamma\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "rem:theorem-d-c2-multiweight-programme" chapters/theory/higher_genus_modular_koszul.tex metadata/theorem_registry.md metadata/label_index.json metadata/claims.jsonl' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
by gauge triviality\textup{)}, so their planted-forest shell is
zero at genus~$2$; however, class~$C$ has $S_4 \neq 0$, which
activates the planted-forest shell at genus~$3$
\textup{(}Corollary~\textup{\ref{cor:shadow-visibility-genus}}\textup{)}.

The shell activation does not bijectively determine the depth class:
$L$ and~$M$ share the pattern $(\neq 0, \neq 0, \neq 0)$, and
$G$ and~$C$ share $(0)$ in the pf column at genus~$2$.
The full depth classification requires the critical discriminant
$\Delta = 8\kappa S_4$
\textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)},
which distinguishes $L$ \textup{(}$\Delta = 0$\textup{)} from~$M$
\textup{(}$\Delta \neq 0$\textup{)}, and~$G$ \textup{(}$\alpha = 0$,
$\Delta = 0$\textup{)} from~$C$
\textup{(}stratum separation\textup{)}.
\end{theorem}

\begin{proof}
From the inductive genus determination
(Corollary above),
 succeeded in 51ms:
701:\item the free fermion algebra $\mathcal{F}$ and the $\beta\gamma$-$bc$
2207:The $\beta\gamma$-$bc$ system at non-integer spin
2210:$\beta\gamma$ ghost with $\lambda = 0$ or $1$\textup{)},
2480:\textup{(}the entire standard landscape except integer-spin $\beta\gamma$, where hypothesis~\textup{(a)} fails\textup{)},
2723:($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.
3225:$\beta\gamma$/$bc$, and $K3 \times E$). The universality
3331:\begin{remark}[$\beta\gamma$ and $bc$: ghost slabs]
3333:\index{beta-gamma system@$\beta\gamma$ system!Brown--Henneaux}%
3335:For the $\beta\gamma$ system of conformal weight~$\lambda$,
3336:$\kappa(\beta\gamma) = c_{\beta\gamma}/2
3340:$\kappa_{\mathrm{tot}}(\beta\gamma\,{\otimes}\,bc) = 0$
3346:$\beta\gamma$-$bc$ slab is Koszul self-dual with
3567:The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
4276:at~$3$, $\beta\gamma$ at~$4$; Virasoro at~$\infty$),
12349:$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
12422: {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
12739:($\beta\gamma$); the Virasoro tower is infinite.
13825:$\beta\gamma$ & $\checkmark$ & gauge-trivial & $\checkmark$ (quartic) \\
13830:For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
13835:$\mu_{\beta\gamma} = 0$
 succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:22641:\label{rem:theorem-d-c2-multiweight-programme}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..02b5d813f848024c4cc33a7e2ae0b005841e5881
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

exec
/bin/zsh -lc "sed -n '22735,22840p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 already for~$\cW_3$, the correction changes its $c$-power window
 with~$g$ and yields an irreducibly bivariate series in
 $(c,\hbar)$.
 A single number cannot absorb a genus tower with new asymptotics
 at each genus.
 One may introduce the bookkeeping quantity
 \[
 \kappa_g^{\mathrm{eff}}(\cA)
 \;:=\;
 \kappa(\cA)
 \;+\;
 \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
 \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
 \]
 but this depends on~$g$ and is not an invariant of~$\cA$.
 The natural replacement is the mixed-channel package
 $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
 or equivalently the full shadow obstruction tower, not a
 renormalized scalar.

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..02b5d813f848024c4cc33a7e2ae0b005841e5881
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]


thinking
**Checking metadata and git status**

I need to ensure everything looks okay, but it might be good to add a line break in the remark title. Before generating metadata, I should check if any files have been modified by the user. I can use the command `git status --short`. It's crucial to notice if there’s a dirty worktree because I want to avoid overwriting any unrelated metadata. If I regenerate it, I should ensure to update the files while keeping the necessary ones. Let’s check the existing status.
exec
/bin/zsh -lc 'git status --short -- chapters/theory/higher_genus_modular_koszul.tex metadata' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..02b5d813f848024c4cc33a7e2ae0b005841e5881
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]


thinking
**Considering metadata regeneration**

I'm cleaning up metadata now, which is great! I wonder if I need to run a `pkill` command first. Technically, if I'm just generating metadata, it might not be necessary. The developer mentioned not to chain commands with separators like `echo`, but could I use a semicolon? I think it’s better to keep things simpler since I likely won’t need to run LaTeX. I’ll probably just execute `python3 scripts/generate_metadata.py` without worrying about the `pkill` command. I'll proceed with that!
codex
The edited prose rereads cleanly. Next check is mechanical: regenerate metadata so the new remark label lands in the registry surface, then inspect only the touched metadata files and the new label entries.
exec
/bin/zsh -lc 'python3 scripts/generate_metadata.py' in /Users/raeez/chiral-bar-cobar succeeded in 365ms:
Generating metadata for chiral-bar-cobar monograph...
  Root: /Users/raeez/chiral-bar-cobar
  Active files (in main.tex): 85
  All .tex files: 128

  Extracted 3673 tagged claims from 128 files

Writing metadata to /Users/raeez/chiral-bar-cobar/metadata/
  claims.jsonl: 3673 claims
  census.json: PH=2845 PE=454 CJ=318 H=30 CD=23 O=3 total=3673
  dependency_graph.dot: 3673 nodes, 2229 edges
  label_index.json: 13209 labels
  theorem_registry.md: 2845 proved claims indexed
  verified_formulas.jsonl: 34 formulas

Done. Run 'make metadata' to regenerate.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..02b5d813f848024c4cc33a7e2ae0b005841e5881
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]


thinking
**Verifying metadata**

I need to check if the metadata has been updated and if the new label is present. A quick way to do this might be using a command like grep. It's a pretty handy tool for searching through files, but I want to be sure I'm using it correctly. Let’s see what I can find to confirm these changes! It's always good to double-check things.
exec
/bin/zsh -lc 'rg -n -F "rem:theorem-d-c2-multiweight-programme" metadata/theorem_registry.md metadata/label_index.json metadata/claims.jsonl' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short -- chapters/theory/higher_genus_modular_koszul.tex metadata' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex metadata/theorem_registry.md metadata/claims.jsonl metadata/label_index.json metadata/census.json metadata/dependency_graph.dot | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/label_index.json:37362:  "rem:theorem-d-c2-multiweight-programme": {
 succeeded in 51ms:
 M chapters/theory/higher_genus_modular_koszul.tex
 M metadata/census.json
 M metadata/claims.jsonl
 M metadata/label_index.json
 M metadata/theorem_registry.md
 succeeded in 51ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index f8a1748..02b5d81 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -17781,10 +17781,12 @@ this is the unique quartic cancellation:
 $o_4 = \tfrac12\{\mathfrak{C},\mathfrak{C}\}_H$ vanishes by the
 Jacobi identity for the affine bracket, so the raising operator
 $D_{\mathfrak{Q}}$ never appears. The remaining finite value
-$d_{\mathrm{alg}} = 2$ is the global contact boundary
-$\kappa = 0$, realized by the full $\beta\gamma_\lambda$ family;
-the primary-line Hamiltonian model above does not apply there
-because $P = \kappa^{-1}$ is undefined.
+$d_{\mathrm{alg}} = 2$ is not a single-line phenomenon: it is the
+global contact class realized by the full $\beta\gamma_\lambda$
+family, where stratum separation kills $r \geq 5$ only after the
+different primary directions are assembled. The one-variable
+primary-line Hamiltonian model above does not see that global
+mechanism.
 
 This is consistent with the primary proof. The proof of
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..02b5d813f848024c4cc33a7e2ae0b005841e5881
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \kappa_g^{\mathrm{eff}}(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

codex
There’s one notation hazard in the new remark. I used `\kappa_g^{\mathrm{eff}}` as a temporary bookkeeping symbol, but this repo already uses `\kappa_{\mathrm{eff}}` for matter-plus-ghost anomaly cancellation. I’m renaming that local placeholder now to avoid a false collision.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -22741,3 +22741,3 @@
  \[
- \kappa_g^{\mathrm{eff}}(\cA)
+ \widetilde{\kappa}_g(\cA)
  \;:=\;
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]


thinking
**Evaluating metadata regeneration**

I need to think about whether I should regenerate the metadata since the line numbers have changed. Even if just one line was modified without a label change, it might affect the overall context, but the line count could remain the same. However, since the metadata claims the line numbers are unaffected, I'm not totally sure it’s necessary. But, just to be cautious, I think it might be wise to run the generation again.
exec
/bin/zsh -lc 'python3 scripts/generate_metadata.py' in /Users/raeez/chiral-bar-cobar succeeded in 379ms:
Generating metadata for chiral-bar-cobar monograph...
  Root: /Users/raeez/chiral-bar-cobar
  Active files (in main.tex): 85
  All .tex files: 128

  Extracted 3673 tagged claims from 128 files

Writing metadata to /Users/raeez/chiral-bar-cobar/metadata/
  claims.jsonl: 3673 claims
  census.json: PH=2845 PE=454 CJ=318 H=30 CD=23 O=3 total=3673
  dependency_graph.dot: 3673 nodes, 2229 edges
  label_index.json: 13209 labels
  theorem_registry.md: 2845 proved claims indexed
  verified_formulas.jsonl: 34 formulas

Done. Run 'make metadata' to regenerate.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

codex
The notation collision is fixed. I’m doing one last grep pass for the specific local drift I corrected, then I’ll close with the verification state and theorem-scope report.
exec
/bin/zsh -lc "rg -n 'beta\\\\gamma.*conditional|conditional.*beta\\\\gamma' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F '\\widetilde{\\kappa}_g' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short -- chapters/theory/higher_genus_modular_koszul.tex metadata' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
22742: \widetilde{\kappa}_g(\cA)
 succeeded in 52ms:
 M chapters/theory/higher_genus_modular_koszul.tex
 M metadata/census.json
 M metadata/claims.jsonl
 M metadata/label_index.json
 M metadata/theorem_registry.md
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

exec
/bin/zsh -lc 'rg -n -F "rem:theorem-d-c2-multiweight-programme" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "The displayed $F_g$ values record the scalar term" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
22641:\label{rem:theorem-d-c2-multiweight-programme}
 exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n -F "Interacting multi-weight row: the displayed $F_g$" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
32125:${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

exec
/bin/zsh -lc 'rg -n -F "The displayed" chapters/theory/higher_genus_modular_koszul.tex | tail -n 5' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
32103:The displayed $F_g$ values record the scalar term
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]


thinking
**Considering updates for kappa**

I’m thinking I might need to add a line for `widetilde{kappa}`, but maybe it’s not necessary for the final version. It’s something to ponder. I might also need to update my plan statuses to show that they’re completed. It feels good to check things off the list! I want to ensure everything is organized and clear, so the final product is neat and accurate. Let's keep moving forward!
Plan update
Inserted the research remark, repaired the local beta-gamma drift in the same chapter, and regenerated metadata to keep the label surface synchronized. Narrow grep checks passed on the corrected drift and the new label.
  ✓ Collect theorem/context evidence from required files and target chapter
  ✓ Inspect compute support for multi-weight correction terms
  ✓ Draft and insert research remark in target chapter
  ✓ Check cross-volume propagation surface and verify final wording
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

codex
The prose and metadata surfaces are stable. I’m using one last falsifier from the compute layer now: a narrow pytest slice on the existing W₃/multi-weight engines, so the remark’s “what is computable” paragraph is backed by live local checks rather than just source inspection.
exec
/bin/zsh -lc "rg --files compute/tests | rg 'genus2_w3|genus4_multiweight|pva_deformation_comparison|betagamma|multi_weight_generating|delta_f2'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_theorem_genus2_w3_partition_engine.py compute/tests/test_theorem_genus4_multiweight_engine.py compute/tests/test_pva_deformation_comparison_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/tests/test_theorem_w4_full_ope_delta_f2_engine.py
compute/tests/test_theorem_multi_weight_generating_function_engine.py
compute/tests/test_bar_cohomology_betagamma_explicit_engine.py
compute/tests/test_theorem_delta_f2_intersection_engine.py
compute/tests/test_penner_matrix_model_delta_f2_engine.py
compute/tests/test_betagamma_determinant.py
compute/tests/test_w5_full_ope_delta_f2_engine.py
compute/tests/test_betagamma_shadow_depth.py
compute/tests/test_betagamma_shadow_full.py
compute/tests/test_betagamma_genus2_cross_channel_engine.py
compute/tests/test_betagamma_quartic_contact.py
compute/tests/test_betagamma_bar.py
compute/tests/test_theorem_genus4_multiweight_engine.py
compute/tests/test_theorem_genus2_w3_partition_engine.py
compute/tests/test_pva_deformation_comparison_engine.py
compute/tests/test_betagamma_epstein.py
compute/tests/test_theorem_large_n_delta_f2_engine.py
compute/tests/test_rectification_delta_f2_verify_engine.py
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]

 succeeded in 2.33s:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 297 items

compute/tests/test_theorem_genus2_w3_partition_engine.py ............... [  5%]
..............................................                           [ 20%]
compute/tests/test_theorem_genus4_multiweight_engine.py ................ [ 25%]
.........................................                                [ 39%]
compute/tests/test_pva_deformation_comparison_engine.py ................ [ 45%]
........................................................................ [ 69%]
........................................................................ [ 93%]
...................                                                      [100%]

============================= 297 passed in 1.55s ==============================
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]


thinking
**Running tests efficiently**

I'll consider running a betagamma cross-channel test because the remark mentions the betagamma engine. A narrow single test file could be quicker, so I think I'll execute `test_betagamma_genus2_cross_channel_engine.py`. It seems like a good way to keep the process focused and efficient. I want to make sure everything works smoothly without unnecessary complications.
codex
The W₃/multi-weight test slice passed cleanly. I’m adding one last `\beta\gamma` test file because the task text assumed nonzero cross-channel terms there, and the chapter now explicitly corrects that premise.
exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_betagamma_genus2_cross_channel_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 745ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 42 items

compute/tests/test_betagamma_genus2_cross_channel_engine.py ............ [ 28%]
..............................                                           [100%]

============================== 42 passed in 0.38s ==============================
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]





thinking
**Considering metadata checks**

I think I need to check metadata after tests, but it may not be necessary. I wonder if I should inspect the git diff specifically for our earlier remark that’s not unrelated to changes. It's possible I should note which metadata files were modified during regeneration since the current repo might be auto-generated. 

Maybe I should run a final cross-volume search? Theorem statements are unchanged, so it might not be needed, but I could check for label uniqueness instead. It could be worth mentioning that no cross-volume propagation was performed since no shared wording changed. I'll search to see if the new remark label appears only in the label index and not the theorem registry since it’s not tagged.
thinking
**Evaluating metadata changes**

It turns out the metadata diff included line number changes in an unrelated file due to a preexisting modification from a user. Regenerating metadata affects other files because of previous dirty edits. 

I need to be careful with my final note, mentioning that metadata was regenerated and that it updated the census, theorem registry, claims, and label index. I should check the line numbers of the modified sections, which include 22641 and 32103/32125, and link the file in the final report. 

I might also want to address the user's premise about the beta-gamma correction. The final report could include two sections and a Fortification Report. I'll mention that tests were run, and the metadata was regenerated, considering the theorem scope limited to D and C2. Lastly, I should evaluate the proof path statuses for Theorem D and C2.
thinking
**Assessing proof soundness**

Since we didn't alter the proof, I should describe it as `sound` or maybe "sound on the stated uniform-weight lane." The multi-weight correction theorem is now documented as part of the research route. Theorem D remains conditioned on uniform weight, but the primary proof on its stated scope appears sound. 

There’s a secondary proof already via GRR in the file; we didn't write a new one, but it fits within the scope. I might want to mention the existing `rem:theorem-d-alt-grr` technique. The condition status indicates uniform weight for all g and all families at g=1, with the multi-weight correction theorem proved. The cohomological lift remains conditional. 

My confidence level is high for the stated lane and medium for extension. However, the report requires a single confidence statement.
thinking
**Clarifying file updates**

I'm noticing that 297 + 42 equals 339, which is important. It looks like I need to mention the metadata files that changed due to regeneration: `metadata/census.json`, `claims.jsonl`, `label_index.json`, and `theorem_registry.md`. This seems good to highlight. Also, I need to ensure that I include a link to the target file for easy reference. I'll make a note of that!
exec
/bin/zsh -lc 'rg -n -F "delta F_g''^{'"\\mathrm{cross}}\" /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex /Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "delta F_g''^{'"\\mathrm{cross}}\" /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:85:at genus $g \geq 2$ for multi-weight algebras the scalar formula receives a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$ (ALL-WEIGHT, with cross-channel correction $\delta F_g^{\mathrm{cross}}$).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:109:where $K$ is the Koszul conductor and $\rho$ the anomaly ratio; this holds only on the \emph{uniform-weight lane} (all generators of $A$ of equal conformal weight), and at $g \geq 2$ multi-weight algebras incur a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$. This section transports both statements to CY categories via the functor $\Phi$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:178:Three independent obstructions block upgrading Conjecture~\ref{conj:cy-complementarity-d3} to a theorem: (a) AP-CY6, the chiral algebra $A_X$ is not constructed at $d = 3$; (b) the uniform-weight hypothesis fails for compact CY$_3$ (chiral de Rham is multi-weight, so gives $\delta F_g^{\mathrm{cross}} \neq 0$ at $g \geq 2$); (c) the BKM automorphic correction at $d = 3$ generates infinitely many imaginary root generators (\S\ref{sec:cy-shadow-cohft} below), so even stating the Koszul conductor $K_X$ requires resolving the degree-$r$ shadow identification of theory\_automorphic\_shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:342:For the full $\cN = 4$ algebra (multi-weight, generators at conformal weights $\{1/2, 1, 3/2, 2\}$), the scalar formula acquires a correction $\delta F_g^{\mathrm{cross}} \neq 0$ at $g \geq 2$ (ALL-WEIGHT, with cross-channel correction).
 succeeded in 51ms:
166:$\delta F_g^{\mathrm{cross}}$
1115:Multi-weight correction $\delta F_g^{\mathrm{cross}}$
1210: $\delta F_g^{\mathrm{cross}}$
1412: and the multi-weight correction $\delta F_g^{\mathrm{cross}}$
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..85dc7aa94c4ced3e1d0b93d5c54ee1c694add9d2
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]



thinking
**Evaluating theorem proofs**

I think I need to mention Theorem D and its primary proof, making sure it's sound, but there may still be a gap. Hmm, I’m not entirely sure if C2 is sound either? The current conditional statement of the theorem seems sound, but there’s also the aspect of removal being blocked. I’m wondering if the contract might fall within the scope of this removal issue and if that indeed leaves some kind of gap remaining.
thinking
**Analyzing proof confidence**

I'm looking into the proofs and corrections related to the current conditional scope. The primary proof is sound, and the secondary proof is sketched, which seems promising. For the technique, it's showing a mix of methods, but I should clarify that we need to replace one-channel support for a mixed-channel theorem. Confidence in the first proof is high, but somewhat medium for the second, which is reasonable considering the adjustments I might need to make. I'll keep it concise, under 70 lines!
codex
Added a research remark in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22641) that sharpens the uniform-weight question for Theorem D and C2. It now separates the proved all-weight free-energy statement
`F_g = \kappa \lambda_g^{\mathrm{FP}} + \delta F_g^{\mathrm{cross}}`
from the still-missing class-valued lift needed to remove the hypothesis from the cohomological obstruction theorem and MC2/C2. The remark also makes the compute state explicit, explains why a genus-independent modified `\kappa` is the wrong invariant, and corrects the premise that `\beta\gamma` has nonzero cross-channel correction. I also repaired the stale table note later in the chapter at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:32103) so `\beta\gamma` is treated as the free-field exact exception and the `\mathcal W_3` row is marked as scalar-part-only.

I regenerated metadata (`metadata/census.json`, `metadata/claims.jsonl`, `metadata/label_index.json`, `metadata/theorem_registry.md`) and ran the narrow compute falsifiers. `pytest` passed on 297 W₃/multi-weight tests plus 42 `\beta\gamma` cross-channel tests. Pending propagation surface, if you want the same research-programme wording mirrored across the bridge volumes: [holomorphic_topological.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:166) and [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4).

## Fortification Report
Theorem D
- PRIMARY PROOF: sound on its stated uniform-weight scope.
- SECONDARY PROOF: written.
- TECHNIQUE: bar-intrinsic shadow tower plus GRR/family-index route.
- CONDITION STATUS: uniform-weight all genera; genus-1 universal for all families; multi-weight free-energy correction theorem proved, but class-valued removal remains open.
- CONFIDENCE: high.

Theorem C2
- PRIMARY PROOF: sound on its current conditional scope.
- SECONDARY PROOF: sketched.
- TECHNIQUE: bar-intrinsic MC2 plus comparison through tautological-line support; upgrade route now stated via mixed-channel class lift.
- CONDITION STATUS: conditional on replacing one-channel line support by a mixed-channel support theorem / class-valued correction package.
- CONFIDENCE: medium.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index d0f7f11abcf533fa6891375481bc3331753c5b7a..33732ace51e8d70c39f26019aa094881cc7195e9
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -22636,6 +22636,141 @@
 new invariant.
 \end{remark}
 
+\begin{remark}[Research programme: removing the uniform-weight
+hypothesis from Theorem~D and C2]
+\label{rem:theorem-d-c2-multiweight-programme}
+\index{uniform-weight hypothesis!removal programme}
+\index{cross-channel correction!research programme}
+The present surface already splits into a proved numerical statement
+and an open class-level lift.
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item \emph{What is known.}
+ At the scalar free-energy level,
+ Theorem~\ref{thm:multi-weight-genus-expansion}(ii) already gives the
+ corrected all-weight formula
+ \[
+ F_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
+ \;+\;
+ \delta F_g^{\mathrm{cross}}(\cA)
+ \qquad (g \geq 1).
+ \]
+ Here $\delta F_1^{\mathrm{cross}} = 0$ universally, and
+ $\delta F_g^{\mathrm{cross}} = 0$ on the uniform-weight lane.
+ Proposition~\ref{prop:free-field-scalar-exact} shows that the
+ vanishing also persists for the all-weight free-field exceptions,
+ including~$\beta\gamma$.
+ Thus the first genuine obstruction is not multi-weight by itself
+ but interacting mixed-channel propagation, with~$\cW_3$ the first
+ explicit witness.
+ At the cohomological level, however,
+ Theorem~\ref{thm:tautological-line-support} still proves
+ $o_g = \kappa\lambda_g$ only on the one-channel
+ uniform-weight lane.
+
+\item \emph{What is computable.}
+ Construction~\ref{constr:cross-channel-graph-sum} makes
+ $\delta F_g^{\mathrm{cross}}$ a mixed-channel stable-graph sum on
+ $\overline{\cM}_{g,0}$.
+ This is concrete at genus~$2$:
+ Theorem~\ref{thm:multi-weight-genus-expansion}(vi) gives
+ \[
+ \delta F_2(\cW_3)
+ \;=\;
+ \frac{c + 204}{16c},
+ \]
+ and Proposition~\ref{prop:universal-gravitational-cross-channel}
+ gives the universal gravitational formula for~$\cW_N$.
+ The current compute layer already matches this division of labour:
+ \texttt{curved\_sc\_higher\_genus\_engine.py} records the
+ $\cW_3$ genus-$2$ decomposition,
+ \texttt{rectification\_delta\_f2\_verify\_engine.py} independently
+ re-derives the genus-$2$~$\cW_N$ formula from the seven stable graphs,
+ \texttt{theorem\_multi\_weight\_generating\_function\_engine.py}
+ and the genus-$3$/$4$ tests track the higher-genus
+ $\cW_3$ tower, and
+ \texttt{betagamma\_genus2\_cross\_channel\_engine.py} verifies the
+ free-field exact~$\beta\gamma$ exception.
+ What is not yet available is a family-agnostic all-genera engine
+ producing $\delta F_g^{\mathrm{cross}}$ from an arbitrary weight
+ spectrum and OPE package.
+
+\item \emph{The precise obstruction.}
+ The missing upgrade is not another scalar identity but a
+ class-valued lift.
+ To remove the uniform-weight hypothesis from Theorem~D one needs
+ classes
+ \[
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \;\in\;
+ W_g \subset R^*(\overline{\cM}_g)
+ \]
+ whose scalar evaluation is
+ $\delta F_g^{\mathrm{cross}}(\cA)$ and which are compatible with
+ clutching, Verdier/Koszul duality, and the cyclic
+ $L_\infty$ obstruction calculus.
+ Only after such a lift exists can one state
+ \[
+ o_g(\cA)
+ \;=\;
+ \kappa(\cA)\cdot\lambda_g
+ \;+\;
+ \delta o_g^{\mathrm{cross}}(\cA)
+ \]
+ as the cohomological replacement for the scalar theorem.
+ This is exactly the point where C2 remains blocked:
+ Theorem~\ref{thm:mc2-full-resolution} uses
+ Theorem~\ref{thm:tautological-line-support}, and that theorem
+ presently isolates only the one-channel tautological line.
+ The mixed-channel sector is visible numerically, but it has not
+ yet been promoted to the obstruction-class package required by
+ MC2-3.
+
+\item \emph{Can one absorb the correction into a modified
+ \texorpdfstring{$\kappa$}{kappa}?}
+ Not by a genus-independent scalar.
+ Proposition~\ref{prop:cross-channel-growth} and
+ Proposition~\ref{prop:cross-channel-no-closed-form} show that,
+ already for~$\cW_3$, the correction changes its $c$-power window
+ with~$g$ and yields an irreducibly bivariate series in
+ $(c,\hbar)$.
+ A single number cannot absorb a genus tower with new asymptotics
+ at each genus.
+ One may introduce the bookkeeping quantity
+ \[
+ \widetilde{\kappa}_g(\cA)
+ \;:=\;
+ \kappa(\cA)
+ \;+\;
+ \frac{\delta F_g^{\mathrm{cross}}(\cA)}{\lambda_g^{\mathrm{FP}}}
+ \qquad (\lambda_g^{\mathrm{FP}} \neq 0),
+ \]
+ but this depends on~$g$ and is not an invariant of~$\cA$.
+ The natural replacement is the mixed-channel package
+ $\{\kappa_i,\delta o_g^{\mathrm{cross}}\}_{i,g}$,
+ or equivalently the full shadow obstruction tower, not a
+ renormalized scalar.
+
+\item \emph{Research programme.}
+ A plausible route to weaken the hypothesis is:
+ first, lift Construction~\ref{constr:cross-channel-graph-sum}
+ from numbers to class-valued CohFT amplitudes on
+ $\overline{\cM}_{g,n}$;
+ second, prove clutching and $R$-matrix independence for the lifted
+ mixed-channel classes;
+ third, identify the smallest tautological sector containing them
+ and replace the one-channel line-support theorem by a mixed-channel
+ support theorem;
+ fourth, feed this replacement into
+ Theorem~\ref{thm:mc2-conditional-completion}.
+ At that point Theorem~D would become an all-weight statement with
+ explicit correction term, and C2 would cease to depend on the
+ uniform-weight hypothesis wherever the mixed-channel support
+ theorem is proved.
+\end{enumerate}
+\end{remark}
+
 % ================================================================
 % THE CROSS-CHANNEL GRAPH CALCULUS
 % ================================================================
@@ -31965,10 +32100,16 @@
 \end{table}
 
 \noindent
-The $F_g$ values are on the scalar lane ($F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$);
-for multi-weight families ($\mathcal{W}_3$, $\beta\gamma$ at $\lambda \neq 1/2$),
-these are conditional at $g \geq 2$
-(Remark~\ref{rem:propagator-weight-universality}).
+The displayed $F_g$ values record the scalar term
+$\kappa \cdot \lambda_g^{\mathrm{FP}}$.
+For scalar-lane families and the free-field exact exceptions,
+including~$\beta\gamma$, this equals the true genus-$g$
+free energy by Proposition~\ref{prop:free-field-scalar-exact}.
+For interacting multi-weight families such as~$\mathcal{W}_3$,
+the actual genus-$g$ free energy at $g \geq 2$ is this scalar term
+plus the cross-channel correction
+$\delta F_g^{\mathrm{cross}}$
+\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
 The planted-forest correction
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
 vanishes for class~G (where $S_3 = 0$) and
@@ -31981,7 +32122,9 @@
 nothing at genus~$2$).
 The universal ratios $F_2/F_1 = 7/240$ and
 $F_3/F_1 = 31/40320 = 31/8!$ are independent of~$\cA$.
-${}^{\ddagger}$Multi-weight: $F_g$ conditional at $g \geq 2$.
+${}^{\ddagger}$Interacting multi-weight row: the displayed $F_g$
+is the scalar part $\kappa \cdot \lambda_g^{\mathrm{FP}}$;
+add $\delta F_g^{\mathrm{cross}}$ to recover the total free energy.
 \end{remark}
 
 \begin{computation}[Genus-$3$ stable graph census; \ClaimStatusProvedHere]
@@ -33517,6 +33660,31 @@
 $\Omega_{12}$: this coupling has no genus-$1$ analogue.
 \end{remark}
 
+\begin{remark}[Face-model numerical verification]
+\label{rem:ddybe-face-model}
+The vertex-model formulation of
+Conjecture~\textup{\ref{conj:g2-ddybe}} involves the
+vertex-IRF correspondence, which introduces subtle
+shift-convention ambiguities. The \emph{face model}
+(IRF) formulation bypasses this: the Baxter--Felder
+Boltzmann weights $(\alpha, \beta, \gamma, \delta)$ are
+built from $\theta_1$ directly, satisfying the Fay
+trisecant identity
+$\alpha\beta - \gamma\delta =
+\theta_1(z - \eta)/\theta_1(z + \eta)$.
+At genus~$2$, $\theta_1$ is replaced by the genus-$2$
+odd theta function $\Theta[{{}^{1/2,0}_{1/2,0}}]$, and
+the doubly-dynamical YBE is verified numerically at
+generic off-diagonal period matrix $\Omega$ to relative
+error $< 10^{-12}$
+\textup{(}$29$ compute tests in
+\texttt{face\_model\_ddybe\_engine.py}\textup{)}.
+The genus-$2$ odd theta factorises at diagonal $\Omega$
+as $-\theta_1(x|\tau_1) \cdot \theta_3(0|\tau_2)$; the
+sign cancels in all Boltzmann-weight ratios, giving exact
+degeneration to two copies of the genus-$1$ DYBE.
+\end{remark}
+
 \begin{proposition}[Degree-$2$ ordered chiral homology on
 $\Sigma_2$]
 \label{prop:g2-degree2}

tokens used
276,934
