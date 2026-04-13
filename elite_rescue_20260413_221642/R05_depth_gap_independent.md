# R05_depth_gap_independent (853s)

**Finding**
- `SERIOUS`: `βγ(λ=0)` was stale in the compute layer: it was classified as class `G` / `d_alg=0` in [depth_classification.py](/Users/raeez/chiral-bar-cobar/compute/lib/depth_classification.py:457), contradicting the manuscript depth-gap surface at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18003) and the existing βγ edge engines. I fixed the classifier and synced the direct tests in [test_depth_classification.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_depth_classification.py:162). No further surviving discrepancies showed up on this `d_alg` surface.

**Status**
- Overall theorem `d_alg ∈ {0,1,2,∞}`, no finite `d_alg ≥ 3`: primary proof is `ProvedHere` at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18003), resting on Riccati algebraicity and the quadratic discriminant dichotomy at [17774](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17774). Alternative proof is also written there: the shadow-Lie raising operator `D_𝔔` forces an infinite even-degree tail when `S_4 ≠ 0` at [17965](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17965). Literature cross-check: no direct published analogue found; this looks manuscript-internal. Confidence: `high`.
- Heisenberg `d_alg=0`: primary witness is [heisenberg_eisenstein.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:1526). Alternative proof is computational: Swiss-cheese `m_3=m_4=0`. Literature cross-check: none direct. Confidence: `high`.
- Affine `\widehat{sl}_2` `d_alg=1`: primary witness is the Jacobi quartic-vanishing proposition at [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:4913). Alternative proof is computational: Swiss-cheese class `L`, `S_4=0`, depth `3`. Literature cross-check: classical Jacobi mechanism is consistent, but I did not find a published depth-gap theorem. Confidence: `high`.
- `βγ` `d_alg=2`: primary witness is the global depth theorem at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1182), with the global-contact summary reused in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17931). Alternative proof is computational: Swiss-cheese `m_3=0`, `m_4≠0`, and the `λ=0` edge engine still gives depth `4`. Literature cross-check: no direct published analogue found; this lane appears manuscript-internal. Confidence: `medium-high`.
- Virasoro `d_alg=∞`: primary witness is [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:3188), reinforced by the Riccati lane at [17960](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17960). Alternative proof is computational: Swiss-cheese `m_3≠0` and infinite shadow-depth. Literature cross-check: framework confirmed, direct trichotomy theorem not found. Confidence: `high`.

**Verification**
- Exact recursion sanity check from the manuscript formula: with `(κ,α,S_4)=(1,2,3)`, the recursion gives `S_5=-36/5`; with `(1,0,3)`, it gives `S_5=0`, `S_6=-6`. This matches the written non-cancellation split.
- Tests passed:
  - `python3 -m pytest compute/tests/test_depth_classification.py` → `132 passed`
  - `python3 -m pytest compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseHeisenbergM3::test_heisenberg_class_G compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseAffineSl2::test_class_L compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseBetagamma::test_class_C compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseVirasoroM3::test_virasoro_shadow_depth_infinite` → `4 passed`
  - `python3 -m pytest compute/tests/test_betagamma_shadow_full.py::TestEdgeCases::test_lambda_0_weight_0_generator` → `1 passed`
- AP grep on the modified compute files found no `AP126`, `AP132`, `AP29`, or `AP165` hits.
- Framework literature checked:
  - [Francis–Gaitsgory, *Chiral Koszul Duality*, Thm. 1.2.4](https://sites.math.northwestern.edu/~jnkf/writ/chiral.pdf): explicitly presented as a generalization of BD04 Thm. 3.4.9 and a conceptual proof of BD04 Thm. 4.8.1.1. Convention check: chiral/factorization objects are coalgebraic, matching the repo’s bar-side discipline.
  - [Lurie, *Higher Algebra*, Thm. 5.3.1.14 and Cor. 5.3.1.15](https://www.math.ias.edu/~lurie/papers/HA.pdf): centralizers exist, and the `E_k` center carries `E_{k+1}` structure. Convention check: this supports the derived-center lane, not SC-structure on the bar complex.
  - [PTVV, *Shifted Symplectic Structures*, Thm. 0.4 / 2.5](https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf): mapping stacks inherit shifted symplectic forms from oriented sources. Convention check: relevant to the complementarity/derived-center output, not to the `d_alg` gap proof itself.
  - `CG`, `CFG`, and `Costello-Li`: not checked to theorem-number granularity in this turn, and I did not find a direct published theorem there matching the depth-gap trichotomy.


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
session id: 019d88a4-201d-75b3-a7f4-2ea494e14911
--------
user
<task>
You are an ELITE RESCUE agent. Your focus: the latest 50-100 commits across a 3-volume,
4,700-page mathematical manuscript. This session deployed 592 Codex agents producing
63+ commits across: adversarial audit (105+250), rectification (25+20), platonic upgrade (20),
healing (40), plus relaunches. Every main theorem (A-D, H, MC1-5) was attacked, repaired,
and upgraded. You now operate on the CURRENT state — all those fixes are on disk.

Your mission:
1. HEAL remaining wounds from the session
2. PROVIDE alternative proof routes for REDUNDANCY (multiplicity of proof)
3. CROSS-CHECK against published literature (BD, FG, CG, Lurie, PTVV, CFG, Costello-Li)
4. DERIVE key results via INDEPENDENT methodology to confirm correctness
5. UPGRADE mathematical strength wherever possible
6. VERIFY cross-domain and cross-approach consistency

Run `git log --oneline -50` in the assigned repo to see recent work.
Read AGENTS.md and CLAUDE.md for the constitutional framework.
Read the actual .tex files — they reflect ALL session work.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs. Label hypotheses.
When citing literature: give paper, theorem number, and convention check.
</grounding_rules>

<completeness_contract>
For each result in your scope: state PRIMARY proof status, ALTERNATIVE proof (written/sketched/identified),
LITERATURE cross-check (confirmed/discrepant/not-checked), and CONFIDENCE (high/medium/low).
</completeness_contract>

<verification_loop>
After edits: re-read modified sections, grep for AP126/AP132/AP29/AP165 violations.
Run relevant tests if in compute scope.
</verification_loop>


INDEPENDENT VERIFICATION: d_alg in {0,1,2,inf}, gap at 3.

1. Algebraic: the MC relation at degree 4 forces S_4 = f(kappa, S_3); show non-cancellation
2. Representation-theoretic: shadow Lie algebra Jacobi identity (from P10 alternative)
3. Computational: verify d_alg for Heis (0), sl_2 KM (1), betagamma (2), Vir (inf)
   using compute engines. Run all four tests.

Document the triple verification.
mcp startup: no servers
codex
Scope is the current post-session manuscript surface, with emphasis on the `d_alg ∈ {0,1,2,inf}` claim and its triple verification. I’m starting by reading the required constitutional files, the recent commit window, and the skill workflows that match this job: `deep-beilinson-audit`, `multi-path-verify`, and `build-surface`.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' AGENTS.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git log --oneline -50' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,719pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,681pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~319pp). Total ~4,719pp, 121K+ tests, 3,500+ tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
 succeeded in 51ms:
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

 succeeded in 50ms:
1a7ac45 MC5 harmonic factorization: prop:harmonic-factorization proves delta_r^harm mechanism (AP203 resolved)
8421a1d AP225 RESOLVED: Theorem D all-genera universality proved via GRR + Arakelov-Faltings
e37cc33 Topologization chain-level: gauge rectification proves E_3 on original BRST complex for affine KM (AP210 resolved)
41ddfc4 Residual lollipop→tadpole: 10 instances in higher_genus_modular_koszul.tex + standalones
02336ae Final gaps + elite rescue: 85 source files rectified across theory, examples, connections
f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
a93cb61 MC3 completion extension: conditional proof via Neeman/BvdB compact generation (AP233 resolved)
a09a633 Theorem H FM-tower spectral sequence: configuration-space collapse proved (AP222 resolved)
a46ee3d Koszul (viii) freeness DISPROVED: ChirHoch*(A) is NOT free polynomial (AP217 resolved)
55b2a24 SC-formality operadic proof: both directions without bilinear form (AP218 resolved)
07c7b9f Terminology: lollipop → tadpole across all Feynman diagram contexts (11 files)
c60db7e Final synchronisation: straggler audit reports and build artifacts
3fda149 Build artifacts: standalone PDFs synchronised, campaign script
da352b5 Makefile: icloud target reorganised into subject-sorted subfolders
5284950 Makefile: add all 14 new standalone papers to the standalone build target
b7bd5df Waves B-E + resume complete: 579/737 agents succeeded, 1,362 output files with content
bd28be8 release pdf
ecd3776 Agent campaign reports and build artifacts: final session synchronisation
1237d59 release pdf
d606b85 Condition removal research reports: H13-H17 from the healing campaign
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
The commit window confirms the current branch already contains the rescue-wave fixes, including `f2a6e1e` for the depth-gap theorem and later synchronization work. Next I’m locking the live claim surface: concordance, theorem registry, red-team summary, then the exact `.tex` and compute modules carrying `d_alg`, `S_4`, and the four family tests.
Plan update
Audit and verify the depth-gap claim on the current post-session surface, then repair any surviving inconsistencies and document proof redundancy with compute and literature cross-checks.
  → Read required constitutional and status files, then locate all live manuscript and compute surfaces for d_alg, S_4, and related theorems
  • Audit the manuscript proofs and theorem status for the depth-gap claim, including alternative proof routes and literature anchors
  • Run the four compute verifications for Heisenberg, sl_2 KM, betagamma, and Vir, then classify any discrepancies
  • Patch remaining wounds in source/tests if needed, propagate any live-surface fixes, and rerun narrow verification plus AP greps
  • Produce a grounded rescue report with proof status, alternative routes, literature cross-checks, and confidence levels
exec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
exec
/bin/zsh -lc "rg -n \"d_alg|depth gap|gap at 3|S_4|prop:depth-gap|thm:depth-gap|Jacobi|shadow Lie algebra|Heisenberg|beta.?gamma|Virasoro\" chapters compute tests metadata -g '*.tex' -g '*.py' -g '*.md'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
Total output lines: 9466

rg: tests: No such file or directory (os error 2)
chapters/examples/deformation_quantization.tex:53:The configuration spaces here are the same ones that defined the Heisenberg bar differential (\S\ref{sec:frame-bar-deg2}), now with marked boundary points replacing interior points.
chapters/examples/deformation_quantization.tex:103:where $P_k$ are bidifferential operators, satisfying Jacobi and Leibniz.
chapters/examples/deformation_quantization.tex:117:\item The Jacobi identity of the PVA ensures vanishing of $o_3$ (the cubic quantization obstruction). Higher obstructions $o_r$ for $r \geq 4$ are governed by the shadow obstruction tower of the quantized algebra and do not automatically vanish. (Koszulness of the quantized algebra is a separate property from shadow obstruction tower termination; both finite and infinite shadow depth algebras can be Koszul.)
chapters/examples/deformation_quantization.tex:379:At $\hbar^4$, there are 105 graphs, encoding higher associativity constraints (Stasheff polytopes), Jacobi identity corrections for the Poisson bracket, and the first appearance of 4-ary operations in the $A_\infty$ structure.
chapters/examples/deformation_quantization.tex:442:\subsection{Example 1: Heisenberg algebra}
chapters/examples/deformation_quantization.tex:481:The Jacobi identity $[J^a, [J^b, J^c]] + \text{cyclic} = 0$ holds exactly at all levels (it is an identity in the Lie algebra), so the OPE receives no corrections. However, the transferred $A_\infty$ structure on bar cohomology acquires higher operations $m_3, m_4, \ldots$ from integration over $\overline{C}_3(X), \overline{C}_4(X), \ldots$, encoding the curved $A_\infty$ structure at higher genus.
chapters/examples/deformation_quantization.tex:483:\subsection{\texorpdfstring{Example 3: $\beta\gamma$ system}{Example 3: system}}
chapters/examples/deformation_quantization.tex:494:The $\beta\gamma$ system is a \emph{free} theory: its OPE receives no quantum corrections to the singular terms. The singular part is exactly $1/(z-w)$ to all orders in $\hbar$. Nontrivial higher operations $m_n$ for $n \geq 3$ arise not from corrections to this OPE, but from the geometry of configuration space integrals when the $\beta\gamma$ system is coupled to a background (e.g., via background charge $Q$).
chapters/examples/deformation_quantization.tex:496:The $\beta\gamma$ system is Koszul dual to the $bc$ ghost system: $(\beta\gamma)^! \cong \mathcal{F}_{bc}$. This is a bosonic-to-fermionic ghost system duality realized through chiral Koszul duality (distinct from the standard boson-fermion correspondence/bosonization). The duality is visible at the level of configuration space integrals:
chapters/examples/deformation_quantization.tex:498:where $K_{\text{cobar}} \in H^n_{D}(\overline{C}_n, \mathcal{F}^{!\boxtimes n})$ is the local cohomology class supported on the boundary, and the symplectic (antisymmetric) pairing of $\beta\gamma$ dualizes under Verdier duality to the anticommuting (fermionic) pairing. See Section~\ref{sec:fermion-boson-koszul} for the complete computation.
chapters/examples/deformation_quantization.tex:753:At $\hbar^2$, the associativity condition (Jacobi identity for the star product) produces an obstruction class in $H^2(\mathfrak{g}, S^2\mathfrak{g})$. For semisimple $\mathfrak{g}$, this cohomology vanishes, so the obstruction is trivial and quantization proceeds to all orders (this is the content of Kontsevich's formality theorem applied to the current algebra).
chapters/examples/deformation_quantization.tex:1048:\subsection{Chiral star product: explicit Heisenberg computation}
chapters/examples/deformation_quantization.tex:1050:\begin{computation}[Heisenberg chiral star product through \texorpdfstring{$\hbar^3$}{3}]
chapters/examples/deformation_quantization.tex:1052:\index{Heisenberg algebra!star product}
chapters/examples/deformation_quantization.tex:1053:\index{deformation quantization!Heisenberg}
chapters/examples/deformation_quantization.tex:1055:For the Heisenberg algebra $\mathcal{H}_\kappa$ with Coisson
chapters/examples/deformation_quantization.tex:1083:For $a = a_{-1}|0\rangle$ (the basic Heisenberg mode):

thinking
**Improving search strategies**

I realize my previous attempts at using "rg" output were too broad and not hitting the target. I need to focus on locating specific files for prop:depth-gap-trichotomy, S4, and others. Using "rg" on theorem labels and tests sounds like the way forward. I'll also consider computing modules and potentially test names. Searching in files like higher_genus_modular_koszul.tex and w_algebras makes sense. Let's fine-tune my search and locate those exact resources!
codex
The registry puts the algebraic depth-gap proposition in `higher_genus_modular_koszul.tex` around line `17787`, so the live core is there. I’m narrowing from the broad grep noise to the exact theorem/proof blocks and the compute tests that already claim to witness the four family depths.
exec
/bin/zsh -lc "sed -n '17680,18080p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:depth-gap-trichotomy|d_alg|gap at 3|depth gap|S_4 =|shadow Lie algebra|Jacobi identity|P10|alternative" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/kac_moody.tex chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters/examples/virasoro.tex chapters/examples/w_algebras.tex chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"depth-gap|d_alg|shadow_depth|Heisenberg|Affine_sl2|betagamma|Virasoro|loop_exactness_order|nonformality_depth|shadow_tower_terminates\" compute/tests compute/lib -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
at $m = 0$, $a_0^2 = 4\kappa^2$;
at $m = 1$, $2a_0 a_1 = 12\kappa\alpha$;
at $m = 2$,
$a_1^2 + 2a_0 a_2 = 9\alpha^2 + 16\kappa S_4$.
These match the coefficients of~$Q_L(t)$
(Definition~\ref{def:shadow-metric}) at
orders~$0$, $1$, $2$ respectively.
For $m \geq 3$, the convolution identity
$\sum_{i+j=m} a_i a_j = 0$ is exactly the
recursion~\eqref{eq:single-line-inversion} at
degree $r = m + 2$: the MC equation forces all
higher Taylor coefficients of $F^2 - Q_L$ to vanish.
\end{proof}

\begin{remark}[Riccati ODE reformulation]
\label{rem:riccati-ode}
\index{Riccati ODE|textbf}
\index{shadow generating function!Riccati ODE}
Set $U(t) := \sum_{r \geq 3} S_r\,t^r$ (the nonlinear part, removing
$\mathrm{Sh}_2$). The algebraic relation~\eqref{eq:riccati-algebraic-relation}
 exited 2 in 51ms:
rg: chapters/examples/virasoro.tex: No such file or directory (os error 2)
chapters/examples/w_algebras.tex:956:alternative perspective on W-algebras that complements the
chapters/examples/w_algebras.tex:1392:\begin{remark}[Wakimoto alternative]
chapters/examples/w_algebras.tex:1554:\emph{uncurved} at genus~0 ($\dzero^2 = 0$, reflecting the Jacobi identity) with
chapters/examples/w_algebras.tex:4441: $S_4(V_k(\mathfrak{sl}_N)) = 0$ \textup{(}Jacobi identity kills the
chapters/examples/w_algebras.tex:4470:by the Jacobi identity. DS reduction introduces composite
chapters/examples/w_algebras.tex:5258:Affine & $3$ (Lie) & Jacobi identity &
chapters/examples/w_algebras.tex:7130:for affine KM the Jacobi identity forces $S_4 = 0$ (class~L),
chapters/examples/beta_gamma.tex:2716:$\Delta = 8\kappa S_4 = 0$ and $\rho = 0$
chapters/connections/concordance.tex:2206: $S_4$ is created from zero (Jacobi identity no longer applies),
chapters/connections/concordance.tex:3528:conformal weight of~$W$ and is fixed by the Jacobi identity
chapters/connections/concordance.tex:3945:All are class~$\mathbf{L}$ (shadow depth~$3$): $S_3 = 1$, $S_4 = 0$,
chapters/connections/concordance.tex:4007:$\Leftrightarrow$ $\lambda$-Jacobi identity; inner Virasoro element
chapters/connections/concordance.tex:4081:At genus~$0$: WDVV equations = Jacobi identity of the MC bracket
chapters/connections/concordance.tex:7221:\ref{prop:depth-gap-trichotomy}
chapters/connections/concordance.tex:7222: & Algebraic depth gap:
chapters/connections/concordance.tex:7225: \textup{(}Proposition~\ref{prop:depth-gap-trichotomy}\textup{)}
chapters/connections/concordance.tex:7717:$\fg$-invariant component, the Jacobi identity creates
chapters/connections/concordance.tex:8062:the discriminant $\Delta = 8\kappa S_4 = 0$.
chapters/connections/concordance.tex:9810:& Algebraic depth gap:
 succeeded in 51ms:
Total output lines: 9941

compute/lib/bc_euler_product_shadow_engine.py:48:CAUTION (AP9):  kappa != c/2 in general (AP48 for non-Virasoro).
compute/lib/bc_euler_product_shadow_engine.py:173:    r"""Compute Virasoro shadow coefficients S_2, ..., S_{max_r} at central charge c.
compute/lib/bc_euler_product_shadow_engine.py:184:        raise ValueError("Virasoro shadow coefficients undefined at c=0.")
compute/lib/bc_euler_product_shadow_engine.py:207:    """Virasoro shadow coefficients via float recursion (faster for large max_r)."""
compute/lib/bc_euler_product_shadow_engine.py:209:        raise ValueError(f"Virasoro shadow undefined at c={c_val}")
compute/lib/bc_euler_product_shadow_engine.py:232:    """Heisenberg: S_2 = k, S_r = 0 for r >= 3 (class G)."""
compute/lib/bc_isomonodromic_shadow_engine.py:65:   d log sqrt(Q).  For the Virasoro shadow, tau_Jimbo = tau_shadow
compute/lib/bc_isomonodromic_shadow_engine.py:131:    """Virasoro at central charge c (possibly complex)."""
compute/lib/bc_isomonodromic_shadow_engine.py:145:        name='Virasoro', kappa=kappa, alpha=alpha, S4=S4, Delta=Delta,
compute/lib/bc_isomonodromic_shadow_engine.py:221:    So disc < 0 when kappa, Delta > 0 (class M, Virasoro): complex conjugate branch points.
compute/lib/bc_isomonodromic_shadow_engine.py:234:    """Branch points for the Virasoro shadow at central charge c."""
compute/lib/genus_expansion.py:165:        # Virasoro case: c + c' = 26
compute/lib/genus_expansion.py:209:    "Heisenberg": ("kappa", lambda kappa: kappa * lambda_fp(1)),
compute/lib/genus_expansion.py:214:    "Virasoro": ("c", lambda c: c / 2 * lambda_fp(1)),
compute/lib/euler_product_from_mc.py:66:  (a) The shadow terminates early (Heisenberg: trivial case), or
compute/lib/euler_product_from_mc.py:630:# 7. Heisenberg moment L-function
compute/lib/euler_product_from_mc.py:634:    r"""For Heisenberg (c=1), the shadow terminates at r=2.
compute/lib/euler_product_from_mc.py:636:    kappa(Heisenberg) = k (the level) = 1 for rank-1 free boson at level k=1.


thinking
**Verifying theorems and proofs**

I'm thinking about the need to audit the exact theorem for correctness. I might think about cross-checking relevant literature and searching for specific example proofs related to Heisenberg, KM, betagamma, and Virasoro. I also want to compute engines for four tests, possibly checking if `guide_to_main_results` has a four-test interface. The user wants to cross-check against published works, so I’ll focus on those results while considering depth-gap verification and ensuring accurate comparisons with known facts.
thinking
**Exploring proof alternatives**

I need to think about finding alternative proof routes for the main theorem. The user explicitly mentioned "INDEPENDENT VERIFICATION: d_alg in {0,1,2,inf}, gap at 3," focusing on the depth-gap claim. I can audit this thoroughly, address any issues, and run tests while cross-checking the literature. It might also be useful to inspect concordance around the depth gap and compare the theorem's surface with the guide. I'll need to search for exact cross-volume hits to help with this.
codex
The core proof is explicit: one recursion-based proof and one shadow-Lie-weight proof are already written in `higher_genus_modular_koszul.tex`. I’m now checking whether those proofs are actually supported by the example chapters and compute layer, and whether the status/wording drifts anywhere else in Vols I–III.
exec
/bin/zsh -lc "sed -n '7200,7265p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3928,3965p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '140,240p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"prop:depth-gap-trichotomy|d_\\{\\\\mathrm\\{alg\\}\\}|d_alg|depth gap|gap at 3|no \\\\"'$d_'"\\{\\\\mathrm\\{alg\\}\\} = 3\\\\"'$|'"\\{0,\\\\, 1,\\\\, 2,\\\\, \\\\infty\\}\" chapters compute metadata /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' -g '*.py' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\ref{prop:shadow-tower-three-lenses}
 & Three equivalent descriptions of $S_r(\cA)$:
 algebraic (shadow), geometric (formality obstruction),
 holographic (boundary-bulk correction)
 & bar-intrinsic MC $+$ formality identification
 $+$ derived-centre factorization \\
\ref{def:generating-depth}
 & Generating depth $d_{\mathrm{gen}}$ vs algebraic depth
 $d_{\mathrm{alg}}$: formal distinction~;
 Virasoro $d_{\mathrm{gen}} = 3$,
 $d_{\mathrm{alg}} = \infty$
 & depth decomposition $+$ class~M tower non-termination \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: structural propositions and depth classification}} \\
\hline
\ref{prop:sc-formal-iff-class-g}
 & SC-formality characterises class~$\mathbf{G}$:
 $\cA$ is Swiss-cheese formal iff class~$\mathbf{G}$
 \textup{(}Proposition~\ref{prop:sc-formal-iff-class-g}\textup{)}
 succeeded in 50ms:
$\Defcyc(L_1 \oplus L_2)
= \Defcyc(L_1) \oplus \Defcyc(L_2)$
by Proposition~\ref{prop:independent-sum-factorization},
giving $d_{\mathrm{alg}} \leq 2$), or they couple
($\alpha \neq 0$ on the mixed sector, activating the
cubic pump and forcing $d_{\mathrm{alg}} = \infty$).
Hence $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$
(Remark~\ref{rem:contact-stratum-separation}).
Depths $d \geq 5$ in the decomposition
$d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$
(Theorem~\ref{thm:depth-decomposition})
are purely arithmetic.

\paragraph{Non-simply-laced Kac--Moody shadow verification.}
The shadow obstruction tower computation extends to all non-simply-laced
Kac--Moody algebras: $B_2 = \mathfrak{so}(5)$, $C_2 = \mathfrak{sp}(4)$,
$G_2$, $B_3 = \mathfrak{so}(7)$, and $F_4$.
All are class~$\mathbf{L}$ (shadow depth~$3$): $S_3 = 1$, $S_4 = 0$,
$\Delta = 0$, independent of type and rank. The distinction
$h \neq h^\vee$ for non-simply-laced types (e.g.\ $B_2$: $h = 4$,
 succeeded in 51ms:
simple types on the evaluation-generated core; the residual DK-4/5
(extension beyond evaluation modules) is downstream.
\begin{enumerate}[label=\textbf{MC\arabic*},leftmargin=3em]
\item \textbf{PBW concentration}: proved for all standard families
 (Proposition~\ref{prop:pbw-universality}).
\item \textbf{Bar-intrinsic MC element}: $\Theta_\cA := D_\cA - \dzero$
 is automatically MC because $D_\cA^2 = 0$
 (Theorem~\ref{thm:mc2-bar-intrinsic}).
\item \textbf{All-types MC3 reduction}: categorical prefundamental
 Clebsch--Gordan closure and the DK comparison on the
 evaluation-generated core are proved for all simple Lie types
 (Corollary~\ref{cor:mc3-all-types}).
\item \textbf{Completion towers}: strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}).
 MC4 splits into MC4$^+$ (positive towers, solved) and
 MC4$^0$ (resonant towers, reduced to finite resonance).
\item \textbf{Sewing at all genera}: general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}).
\end{enumerate}

 exited 2 in 51ms:
rg: regex parse error:
    (?:prop:depth-gap-trichotomy|d_\{\mathrm\{alg\}\}|d_alg|depth gap|gap at 3|no \\{\mathrm\{alg\}\} = 3\$|\{0,\, 1,\, 2,\, \infty\})
                                     ^^
error: unrecognized escape sequence

thinking
**Rethinking cross-volume search**

I need to simplify the cross-volume search, and I’m wondering if using fixed string regex might help. I should also consider needing the exact lines in volume 2 and volume 3. It feels like there might be a more efficient approach out there that could make things easier. Okay, I’ll keep these ideas in mind while figuring out how to proceed with this search.
exec
/bin/zsh -lc 'rg -n -F "prop:depth-gap-trichotomy" . /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 58ms:
Total output lines: 310

./healing_20260413_132214/H11_SC_formal_alt.md:487:platonic_rectification_20260413_114523/P13_SC_formality_upgrade.md:162:CLAUDE.md:932:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:488:platonic_rectification_20260413_114523/P13_SC_formality_upgrade.md:215:932:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:493:relaunch_wave2_empties/S16_v1_to_v2_bridge.md:1822:/Users/raeez/chiral-bar-cobar/CLAUDE.md:949:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:495:platonic_rectification_20260413_114523/P07_thm_H_upgrade.md:1113:CLAUDE.md:932:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:497:audit_campaign_20260412_231034/T16_depth_gap.md:207:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:499:CLAUDE.md:949:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:500:audit_campaign_20260412_231034/T17_chirhoch1_KM.md:142:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:502:audit_campaign_20260412_231034/T17_chirhoch1_KM.md:145:audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:800:\ref{prop:depth-gap-trichotomy}
./healing_20260413_132214/H11_SC_formal_alt.md:1586:/Users/raeez/chiral-bar-cobar/CLAUDE.md:949:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1594:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:142:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1595:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:145:audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1596:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:163:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1597:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:205:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1598:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:209:audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1599:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:238:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1600:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:430:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
./healing_20260413_132214/H11_SC_formal_alt.md:1601:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T17_chirhoch1_KM.md:440:audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
exec
/bin/zsh -lc "rg -n -F \"d_{\\mathrm{alg}}\" chapters /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"d_alg\" compute -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:207:The $A_1$ case is verified by the base-case computation above ($\kappa_{\mathrm{ch}} = 1$, trivial Jacobi ring, $\mathrm{Cl}_4$-Morita-trivial category). For $N \geq 2$, the shadow class prediction is conditional on Conjecture~\ref{conj:ade-w-algebra}: if the output $\Phi(\MF(\widetilde{W}_{X_N}))$ is indeed the principal $\cW$-algebra $\cW(\mathfrak{g}_{X_N})$ of rank $\geq 2$, then the Vol~I shadow depth classification (depth gap trichotomy: $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$) places it in class M, since the principal $\cW$-algebra has non-vanishing higher operations at all degrees.
chapters/examples/lattice_foundations.tex:4870:$d_{\mathrm{alg}} = 0$
chapters/examples/beta_gamma.tex:2016:Its depth decomposition $d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}
chapters/examples/beta_gamma.tex:2022:$d_{\mathrm{alg}} = 2$
chapters/examples/heisenberg_eisenstein.tex:154:and $d_{\mathrm{alg}} = 0$, giving total depth $d = 2$; the
chapters/examples/yangians_foundations.tex:158:$d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$ of
chapters/examples/yangians_foundations.tex:162:of $r(z)$ and $d_{\mathrm{alg}}$ records the Drinfeld associator
chapters/examples/kac_moody.tex:4682:In the depth decomposition $d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$
chapters/examples/kac_moody.tex:4686:$L$-function of the adjoint representation) and $d_{\mathrm{alg}} = 0$,
chapters/examples/bar_complex_tables.tex:1504:d_{\mathrm{alg}}([J^a|J^b])
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:141:Class & $K_{A_\cC}(z)$ & $d_{\mathrm{alg}}(A_\cC)$ \\
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:150:Equivalently: $K_{A_\cC}(z) = 1$ iff the boundary coproduct is primitive iff $d_{\mathrm{alg}} = 0$ iff $\cC$ is class $\mathbf{G}$. The correspondence $K_{A_\cC}(z) = 1 \Longleftrightarrow \mathbf{G} \Longleftrightarrow d_{\mathrm{alg}} = 0$ is the CY analogue of the Vol~II biconditional.
chapters/frame/preface.tex:2737:The algebraic depth takes exactly four values: $d_{\mathrm{alg}}
chapters/frame/preface.tex:2740:family realises $d_{\mathrm{alg}} = 3$; the gap is forced by the
chapters/frame/preface.tex:2831:The algebraic depth $d_{\mathrm{alg}}(\cA)$ exhibits a gap:
chapters/frame/preface.tex:2832:$d_{\mathrm{alg}}\in\{0,1,2,\infty\}$, and no finite value
chapters/frame/preface.tex:2833:$d_{\mathrm{alg}}\ge 3$ is realized on the standard landscape
chapters/frame/preface.tex:2836:G ($d_{\mathrm{alg}}=0$), L ($d_{\mathrm{alg}}=1$),
chapters/frame/preface.tex:2837:C ($d_{\mathrm{alg}}=2$), M ($d_{\mathrm{alg}}=\infty$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1000: with $d_{\mathrm{alg}} = \infty$. The open question
 succeeded in 51ms:
Total output lines: 959

compute/lib/cy_n4sca_k3_engine.py:1223:    d_alg = infinity (the N=4 OPE has poles of arbitrarily high order
compute/lib/cy_n4sca_k3_engine.py:1252:        'd_alg': float('inf'),
compute/lib/cy_descent_theorem_engine.py:1187:    fits_in_picard_algebraic = total_rank <= 19  # Need room for polarization
compute/lib/cy_descent_theorem_engine.py:1193:        'fits_in_picard_algebraic': fits_in_picard_algebraic,
compute/lib/moonshine_shadow_depth.py:26:  Niemeier lattice VOAs: class G, kappa = 24, d_alg = 0
compute/lib/moonshine_shadow_depth.py:27:  Monster module V^natural: class M, kappa = 12, d_alg = infinity
compute/lib/moonshine_shadow_depth.py:294:        'd_alg': 0,
compute/lib/moonshine_shadow_depth.py:417:def monster_d_alg() -> float:
compute/lib/moonshine_shadow_depth.py:418:    """Algebraic depth d_alg(V^natural) = infinity.
compute/lib/moonshine_shadow_depth.py:497:        'd_alg': float('inf'),
compute/lib/moonshine_shadow_depth.py:528:      kappa = 24, class G, d_alg = 0, weight-1 generators
compute/lib/moonshine_shadow_depth.py:531:      kappa = 12, class M, d_alg = infinity, weight-2 generators
compute/lib/moonshine_shadow_depth.py:542:            'd_alg': 0,
compute/lib/moonshine_shadow_depth.py:551:            'd_alg': float('inf'),
compute/lib/pva_deformation_cy3.py:343:            'quantized_algebra': 'W_{1+infinity}(h1, h2, h3)',
compute/lib/pva_deformation_cy3.py:781:        'quantized_algebra': 'Conifold CoHA (E_1-type)',
compute/lib/pva_deformation_cy3.py:825:            'quantized_algebra_type': 'E_inf-chiral (vertex algebra)',
compute/lib/pva_deformation_cy3.py:826:            'quantized_algebra': 'W_{1+infinity}(h1, h2, h3)',
codex
I’m checking the example witnesses now. The theorem proof is only as good as the four archetypes it cites, so I’m reading the exact witness theorems for `G/L/C/M` rather than trusting the summary sentences.
exec
/bin/zsh -lc "rg -n \"prop:heisenberg-gaussian-termination|cor:heisenberg-postnikov-termination|d_{\\\\mathrm\\{alg\\}} = 0|shadow depth 2|S_3 = 0|S_4 = 0\" chapters/examples/heisenberg_eisenstein.tex chapters/frame/heisenberg_frame.tex chapters/examples/free_fields.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Jacobi identity kills the quartic obstruction|S_4 = 0|d_{\\\\mathrm\\{alg\\}} = 1|class~\\\\mathbf\\{L\\}|thm:affine|prop:affine-jacobi-quartic-vanishing\" chapters/examples/kac_moody.tex chapters/theory/higher_genus_modular_koszul.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:betagamma-global-depth|prop:betagamma-T-line-shadows|S_4 = -5/12|d_{\\\\mathrm\\{alg\\}} = 2|r_{\\\\max} = 4|stratum separation\" chapters/examples/beta_gamma.tex chapters/theory/higher_genus_modular_koszul.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"S_4 = 10/\\[c\\(5c\\{\\+\\}22\\)\\]|d_{\\\\mathrm\\{alg\\}} = \\\\infty|thm:vir-non-formality|prop:virasoro-shadow-ratio-riccati|class~\\\\mathbf\\{M\\}|infinite tail\" chapters/examples/free_fields.tex chapters/examples/w_algebras.tex chapters/theory/higher_genus_modular_koszul.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:thm:betagamma-global-depth|prop:betagamma-T-line-shadows|S_4 = -5/12|d_{\mathrm\{alg\}} = 2|r_{\max} = 4|stratum separation)
                                                                               ^
error: repetition quantifier expects a valid decimal
 exited 2 in 51ms:
rg: regex parse error:
    (?:prop:heisenberg-gaussian-termination|cor:heisenberg-postnikov-termination|d_{\mathrm\{alg\}} = 0|shadow depth 2|S_3 = 0|S_4 = 0)
                                                                                    ^
error: repetition quantifier expects a valid decimal
 exited 2 in 51ms:
rg: regex parse error:
    (?:Jacobi identity kills the quartic obstruction|S_4 = 0|d_{\mathrm\{alg\}} = 1|class~\mathbf\{L\}|thm:affine|prop:affine-jacobi-quartic-vanishing)
                                                                ^
error: repetition quantifier expects a valid decimal
 exited 2 in 51ms:
rg: regex parse error:
    (?:S_4 = 10/\[c\(5c\{\+\}22\)\]|d_{\mathrm\{alg\}} = \infty|thm:vir-non-formality|prop:virasoro-shadow-ratio-riccati|class~\mathbf\{M\}|infinite tail)
                                       ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n -F \"cor:heisenberg-postnikov-termination\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/heisenberg_eisenstein.tex:1431:Corollary~\ref{cor:heisenberg-postnikov-termination} below;
chapters/examples/heisenberg_eisenstein.tex:1526:\label{cor:heisenberg-postnikov-termination}
chapters/theory/higher_genus_foundations.tex:6305:(Corollary~\ref{cor:heisenberg-postnikov-termination}),
chapters/connections/frontier_modular_holography_platonic.tex:2392:Corollary~\textup{\ref{cor:heisenberg-postnikov-termination})}, the
chapters/connections/frontier_modular_holography_platonic.tex:2740: \textup{(}Corollary~\textup{\ref{cor:heisenberg-postnikov-termination})}.
exec
/bin/zsh -lc "rg -n -F \"thm:betagamma-global-depth\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:1166:Theorem~\ref{thm:betagamma-global-depth}.
chapters/examples/free_fields.tex:1182:\label{thm:betagamma-global-depth}
chapters/examples/free_fields.tex:5606:(Theorem~\ref{thm:betagamma-global-depth}):
chapters/theory/higher_genus_modular_koszul.tex:15292:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
chapters/theory/higher_genus_modular_koszul.tex:16996: Thm~\ref{thm:betagamma-global-depth} \\[3pt]
chapters/theory/higher_genus_modular_koszul.tex:17074: \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
chapters/theory/higher_genus_modular_koszul.tex:17140:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
chapters/theory/higher_genus_modular_koszul.tex:17944:Theorem~\ref{thm:betagamma-global-depth} gives
chapters/theory/higher_genus_modular_koszul.tex:19651:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
chapters/theory/ordered_associative_chiral_kd.tex:6755:Theorem~\textup{\ref*{thm:betagamma-global-depth}}\textup{)},
exec
/bin/zsh -lc "rg -n -F \"thm:vir-non-formality\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"prop:affine-jacobi-quartic-vanishing\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/kac_moody.tex:1675:(Proposition~\ref{prop:affine-jacobi-quartic-vanishing}), giving
chapters/examples/kac_moody.tex:4913:\ClaimStatusProvedHere]\label{prop:affine-jacobi-quartic-vanishing}
 succeeded in 52ms:
chapters/theory/ordered_associative_chiral_kd.tex:3188:\label{thm:vir-non-formality}
chapters/theory/ordered_associative_chiral_kd.tex:3343:Theorem~\ref{thm:vir-non-formality}. The coproduct column: the

thinking
**Checking theorems in documents**

I'm noticing that the BetaGamma theorem is in free_fields.tex instead of beta_gamma.tex, which is interesting! I need to inspect the specific line ranges for the exact witnesses referenced. Additionally, I might need to consider the Vir non-formality and the affine proposition. So, I’ll make sure to read the relevant segments carefully to gather all the necessary details. There's definitely a lot to explore here!
exec
/bin/zsh -lc "sed -n '1490,1555p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\mathfrak{C}_{\mathcal{H}} = 0,
\qquad
\mathfrak{o}_{\mathcal{H}}^{(4)} = 0,
\qquad
\mathfrak{Q}_{\mathcal{H}} = 0.
\end{equation}
Equivalently, through quartic order the universal class reduces to its
quadratic part:
\begin{equation}\label{eq:heisenberg-theta-quadratic}
\Theta_{\mathcal{H}}^{\le 4} = H_{\mathcal{H}}.
\end{equation}
\end{theorem}

\begin{proof}
The Heisenberg deformation problem is governed by a constant Poisson
structure: the OPE $J^i(z)\,J^j(w) \sim \kappa\,\delta^{ij}/(z-w)^2$
has no simple-pole term, so the corresponding $L_\infty$ structure on
the cyclic deformation complex carries $\ell_1^{\mathrm{tr}} = 0$
(the transferred differential vanishes on $V_{\mathcal{H}}$) and no
higher operations $\ell_n^{\mathrm{tr}}$ for $n \ge 2$ beyond the
exec
/bin/zsh -lc "sed -n '4900,4975p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1160,1225p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3188,3265p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
ad-invariance of the normalised Killing form. The equality of
all three terms is specific to the Lie/tree phase: it reflects the
fact that $\kappa$ is a \emph{cyclic} pairing for the Lie bracket,
the defining condition that makes $\mathfrak{g}$ a cyclic
$L_\infty$-algebra at the transferred binary level.
\end{proof}

\subsection{Jacobi identity kills the quartic obstruction}
\label{subsec:affine-jacobi-kills-quartic}
\index{Jacobi identity!quartic obstruction vanishing}
\index{quartic obstruction!Jacobi mechanism}

\begin{proposition}[Jacobi mechanism for quartic vanishing;
\ClaimStatusProvedHere]\label{prop:affine-jacobi-quartic-vanishing}
The quartic obstruction is the Hamiltonian self-bracket of the cubic:
\begin{equation}\label{eq:quartic-obstruction-self-bracket}
\mathfrak{o}_{\mathrm{aff}}^{(4)}
\;=\;
\tfrac{1}{2}\,
\bigl\{\mathfrak{C}_{\mathrm{aff}},
 succeeded in 50ms:
 \qquad (r \geq 2).
\]
This statement concerns only the one-dimensional slice generated by the
weight-changing class. It does not describe either the Virasoro T-line
of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
stratum that realizes the global depth-$4$ witness in
Theorem~\ref{thm:betagamma-global-depth}.
\end{proposition}

\begin{proof}
The weight-changing line satisfies the hypothesis of rank-one abelian
rigidity (Theorem~\ref{thm:betagamma-rank-one-rigidity}): all
transferred higher brackets $\ell_n^{\mathrm{tr}}|_L = 0$ for
$n \geq 2$. The shadow obstruction tower is therefore purely quadratic, and since
$\kappa|_{\mathrm{wc}} = 0$ (the weight-changing deformation does not
produce genus-$0$ curvature), the entire tower
vanishes.\qedhere
\end{proof}

\subsubsection{Stratum separation and the quintic vanishing}
 succeeded in 51ms:
\label{thm:vir-non-formality}
For generic central charge~$c$, the $\Ainf$ operation $m_k$ of the
ordered bar complex $\Barch(\mathrm{Vir}_c)$ is nonzero for all
$k \ge 3$. The Virasoro algebra is class~$\mathbf{M}$
\textup{(}infinite shadow depth\textup{)}.
\end{theorem}

\begin{proof}
The degree-$3$ associator is computed directly from the PVA
$\lambda$-bracket. The Stasheff identity at degree~$3$ requires
$m_3 = -A_3$ where
\[
A_3(T,T,T;\,\lambda_{12},\lambda_{23})
\;=\;
-\{T{}_{\lambda_{23}}\{T{}_{\lambda_{12}} T\}\}
\;=\;
\tfrac{c}{12}\,\lambda_{23}^3\,(2\lambda_{12} + \lambda_{23})
\;+\;(\text{$T$-dependent terms}).
\]
The scalar contact term $\frac{c}{12}\lambda_{23}^3(2\lambda_{12}

thinking
**Investigating the theorem**

I need to inspect the theorem `prop:betagamma-T-line-shadows` or quartic birth to confirm whether S3 is maybe 2 on the T-line. However, I see that the global witness is using S3=0 and S4=-5/12. This makes me think I should look into the proof details further. It sounds like there’s a bit to unravel here, and I want to get it right! Let's continue from the theorem.
exec
/bin/zsh -lc "sed -n '1225,1298p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
Hence the nonzero quartic class is genuinely mixed: it is invisible on
both isolated one-dimensional slices and appears only on the charged
stratum. The quartic contact class is the \emph{last} nontrivial global
shadow component.

\emph{Degree~$5$.}
The quintic obstruction is the Lie bracket
$o_5 = \{\mathfrak{C},\, Q^{\mathrm{contact}}\}_H$.
The quartic contact class lives on the charged stratum, while the cubic
shadow that survives on the standalone T-line does not contribute a
compatible input in the full two-channel complex. On the weight-changing
line the cubic vanishes altogether. Hence the global bracket
$o_5 = 0$.
The quartic contact class lives on a charged stratum whose
self-bracket exits the complex by rank-one rigidity; no further
obstruction propagates.

Therefore $r_{\max} = 4$: the tower terminates at the quartic level.\qedhere
\end{proof}
exec
/bin/zsh -lc 'rg -n -F "-5/12" chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4500,4530p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1985,2045p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: unrecognized flag -5
 succeeded in 50ms:
The tower converges ($\rho < 1$) for $N \geq 4$ at this level.
\end{proof}

\begin{remark}[DS reduction and arithmetic depth]
\label{rem:ds-arithmetic-depth}
\index{Drinfeld--Sokolov reduction!arithmetic depth}
\index{arithmetic depth!DS reduction}
The depth decomposition $d = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$
(Chapter~\ref{chap:arithmetic-shadows},
Theorem~\ref{thm:depth-decomposition}) is not preserved by DS
reduction in any simple way. Concretely:
\begin{enumerate}[label=\textup{(\roman*)}]
\item DS \emph{decreases} arithmetic depth:
 $d_{\mathrm{arith}}(\widehat{\mathfrak{sl}}_N) = 1$ while
 $d_{\mathrm{arith}}(\mathcal{W}_N) = 0$ at generic level.
 The shadow field of an affine algebra has one Eisenstein
 critical line; DS reduction collapses it.
\item DS \emph{increases} algebraic depth:
 $d_{\mathrm{alg}}(\widehat{\mathfrak{sl}}_N) = 1$
 (class~$L$, $r_{\max} = 3$) while
 succeeded in 50ms:
with no local nonlinear correction terms. Any failure of the modular
package at the $\beta\gamma$ level is therefore a failure of the
global gluing axioms, not of local algebra.

Compare with the Heisenberg system (Overture), where
$c_{\mathrm{Heis}} = 1$ already detects modular curvature. The
Heisenberg is \emph{not} Koszul self-dual
($\cH_k^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)$, not~$\cH_k$),
but its abelian OPE structure makes the two sides difficult to
distinguish at the level of shadow invariants. The $\beta\gamma$
system, also not self-dual ($(\beta\gamma)^{!} \simeq bc$),
separates the two sides of the holographic
correspondence cleanly.
\end{remark}


%% ================================================================
\section{The \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth and rank-one rigidity}
\label{sec:betagamma-quartic-birth}
\index{beta-gamma system@$\beta\gamma$ system!quartic birth}
exec
/bin/zsh -lc 'rg -n -- "-5/12" chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:15220: & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
chapters/theory/higher_genus_modular_koszul.tex:15242:$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
chapters/theory/higher_genus_modular_koszul.tex:15287:$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
chapters/theory/higher_genus_modular_koszul.tex:17021: $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
chapters/theory/higher_genus_modular_koszul.tex:17068:  S_4 = -5/12,\qquad
chapters/theory/higher_genus_modular_koszul.tex:17140:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
chapters/theory/higher_genus_modular_koszul.tex:17874:  S_4 = -5/12,\qquad
chapters/theory/higher_genus_modular_koszul.tex:17949:is the nonzero constant $S_4 = -5/12$.
chapters/theory/higher_genus_modular_koszul.tex:19285:$\beta\gamma_\lambda$ & $6\lambda^2 - 6\lambda + 1$ & $0$ & $-5/12$ & n/a
chapters/theory/higher_genus_modular_koszul.tex:19592: $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
chapters/theory/higher_genus_modular_koszul.tex:19650:$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$

thinking
**Searching for theorems**

I’m considering whether the actual theorem is in the free fields. I should look for the exact label around 15200 in higher genus modular Koszul to see if there's a summary table. However, I need to verify the source of -5/12 since it might only be mentioned in higher genus modular Koszul, not the example chapter. It seems like I might need to compute or test for verification instead of relying on the example chapter. I'll also search for `5/12` in free fields or beta gamma.
exec
/bin/zsh -lc "rg -n -- \"5/12|Q\\"'^'"\\{contact\\}|quartic contact\" chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/beta_gamma.tex:114:nontrivial interaction datum is the quartic contact shadow,
chapters/examples/beta_gamma.tex:123:The quartic contact shadow $\Theta^{\leq 4}$ is nontrivial:
chapters/examples/beta_gamma.tex:142:(the quartic contact shadow exists, even
chapters/examples/beta_gamma.tex:173:the quartic contact class arises as a codimension-$2$ residue on the
chapters/examples/beta_gamma.tex:199:(ii)~the bar complex with quartic contacts (strict model
chapters/examples/beta_gamma.tex:251:the quartic contact class descending from composite currents.
chapters/examples/beta_gamma.tex:348:contributes a nontrivial residue). At degree~$4$, the quartic contact
chapters/examples/beta_gamma.tex:2047:\paragraph{Step~3: Degree~$4$, quartic contact appears.}
chapters/examples/beta_gamma.tex:2050:with quartic contact invariant
chapters/examples/beta_gamma.tex:2142:the quartic contact invariant~$\mu_{\beta\gamma}$.
chapters/examples/beta_gamma.tex:2184: is the quartic contact corolla from the transferred operation~$m_3$,
chapters/examples/beta_gamma.tex:2207:nonzero: the quartic contact stratum of the planted-forest boundary
chapters/examples/beta_gamma.tex:2239:quartic contact corolla $K_{0,4}$ composes with the degree-$2$
chapters/examples/beta_gamma.tex:2287:quartic contact invariant that follows. These make explicit the
chapters/examples/beta_gamma.tex:2441:Hence the quartic contact invariant vanishes:
chapters/examples/beta_gamma.tex:2496:The quartic contact invariant
chapters/examples/beta_gamma.tex:2514:\subsection{Vanishing of the quartic contact invariant}
chapters/examples/beta_gamma.tex:2516:\begin{corollary}[Vanishing of the quartic contact invariant;
chapters/examples/beta_gamma.tex:2519:\index{quartic contact invariant!vanishing}
chapters/examples/beta_gamma.tex:2527:The quartic contact invariant vanishes identically on the weight-changing
exec
/bin/zsh -lc "sed -n '286,330p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{princ:guide-gravitational-primitivity}
\index{coproduct!gravitational primitivity|textbf}
For any principal Drinfeld--Sokolov reduction
$W_k(\fg) = H^0_{\mathrm{BRST}}(\widehat{\fg}_k, f_{\mathrm{prin}})$,
the HPL-transferred coproduct is strictly primitive at all degrees:
$\Delta_{z,n}^W = 0$ for all $n \ge 2$.
All nontrivial structure of the transferred dg-shifted Yangian
resides in the $\Ainf$ products $\{m_n^W\}_{n \ge 3}$ and in
the collision residue $r(z)$. The mechanism is a ghost-number
obstruction intrinsic to DS reduction.
\end{principle}

\begin{remark}[The four-test interface]
\label{rem:guide-four-test-interface}
\ClaimStatusProvedHere
\index{four-test interface|textbf}
The modular Koszul machine has a complete interface with
$\overline{\mathcal{M}}_{g,n}$, consisting of four
independent proved tests:
\textup{(1)}~$D_\cA^2 = 0$ at all genera and degrees

thinking
**Considering test execution**

The user asked to run all four tests, so I should think about executing one test per family. I might need to run four separately named tests, which could be from the same file or different ones. I want to check the candidate test file to be sure. It seems like `test_depth_classification.py` is likely focused on direct classification data, so I'll take a look at the relevant part of that file.
codex
The guide’s “four-test interface” is about the theorem machine, not the four family checks the user asked for. I’m isolating the compute-side family tests now so the numerical verification uses the right engines rather than a generic depth summary table.
exec
/bin/zsh -lc "sed -n '1,360p' compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/depth_classification.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
"""Tests for G/L/C/M depth classification and total depth decomposition.

Verifies:
    1. G/L/C/M classification for all 20 algebras
    2. Total depth formula d = 1 + d_arith + d_alg
    3. Kappa formulas computed from first principles (AP1)
    4. Delta = 8*kappa*S4 where applicable
    5. Cusp form dimension formula for SL(2,Z)
    6. Cross-checks against shadow_metric_census.py
    7. Lattice depth formula d = 3 + dim S_{r/2}
    8. Degenerate cases (kappa=0, weight-0 generators)
    9. Virasoro/W_N specific data
   10. Additivity and consistency cross-checks

Mathematical references:
    thm:depth-decomposition (arithmetic_shadows.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    def:shadow-depth-classification (higher_genus_modular_koszul.tex)
    eq:depth-cusp-formula (arithmetic_shadows.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
exec
/bin/zsh -lc "sed -n '1,220p' compute/lib/ds_shadow_tower_sl2_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '130,260p' compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""DS shadow tower transformation engine for sl_2.

Tracks shadow obstruction tower invariants (S_2, S_3, S_4, Delta)
for V_k(sl_2) BEFORE and AFTER Drinfeld-Sokolov reduction to Vir_c.

The class transition L -> M is the structural content:

  BEFORE (affine KM, class L):
    kappa = 3(k+2)/4,  S_3 = 1 (Killing 3-cocycle),  S_4 = 0 (Jacobi),
    Delta = 8*kappa*S_4 = 0.  Finite shadow tower, depth 3.

  AFTER (Virasoro, class M):
    c = 1 - 6(k+1)^2/(k+2)  (Fateev-Lukyanov),
    kappa = c/2,  S_3 = 2,  S_4 = 10/(c(5c+22)),
    Delta = 8*kappa*S_4 = 40/(5c+22) != 0 generically.
    Infinite shadow tower, depth infinity.

The quartic S_4 is created by the BRST differential coupling matter
to ghosts.  Its appearance is the non-commutativity of the DS-shadow
diagram at arity 4 (thm:ds-central-charge-additivity).
 succeeded in 52ms:
# ============================================================================

class TestSwissCheeseVirasoroM3:
    """Verify m_3^{SC} != 0 for Virasoro (class M).

    This is the CORE VERIFICATION of non-formality for class M.
    S_3 = 2 (c-independent) is the cubic shadow coefficient.
    """

    def test_m3_SC_nonzero_c26(self):
        """m_3^{SC} != 0 for Virasoro at c=26."""
        data = swiss_cheese_m3_virasoro(F(26))
        assert data["m3_SC_nonzero"] is True
        assert data["class"] == "M"

    def test_S3_equals_2_c26(self):
        """S_3 = 2 for Virasoro at c=26 (algebraic formula)."""
        data = swiss_cheese_m3_virasoro(F(26))
        assert data["S3_algebraic"] == F(2)


thinking
**Inspecting classification engines**

I’m noticing that the depth classification engine appears to classify directly from α and Δ, rather than computing m_n independently. The theorem_ainfty_nonformality_class_m_engine seems more straightforward with its Swiss-cheese operations. I think I need to take a closer look at the library behind the tests and search for relevant functions to clarify this further. There’s something intriguing about how these systems interact!
exec
/bin/zsh -lc "rg -n -F \"def swiss_cheese_m3_heisenberg\" compute/lib compute/tests -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/theorem_ainfty_nonformality_class_m_engine.py:321:def swiss_cheese_m3_heisenberg(k: Fraction, N: int = 20) -> Dict[str, Any]:
exec
/bin/zsh -lc "rg -n -F \"def swiss_cheese_m3_virasoro\" compute/lib compute/tests -g '*.py'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"def swiss_cheese_m4_betagamma\" compute/lib compute/tests -g '*.py'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"def swiss_cheese_m3_affine_sl2\" compute/lib compute/tests -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/theorem_ainfty_nonformality_class_m_engine.py:423:def swiss_cheese_m4_betagamma(N: int = 10) -> Dict[str, Any]:
 succeeded in 51ms:
compute/lib/theorem_ainfty_nonformality_class_m_engine.py:251:def swiss_cheese_m3_virasoro(c: Fraction, N: int = 20) -> Dict[str, Any]:
compute/lib/ainfty_structure_maps_engine.py:1457:def swiss_cheese_m3_virasoro(c: Fraction, N: int = 4) -> Dict[str, Any]:
 succeeded in 52ms:
compute/lib/theorem_ainfty_nonformality_class_m_engine.py:353:def swiss_cheese_m3_affine_sl2(k: Fraction, N: int = 20) -> Dict[str, Any]:

thinking
**Inspecting the theorem file**

I need to look into the functions within the `theorem_ainfty_nonformality_class_m_engine.py` file. It seems like there might be some relevant functions there that I need to inspect closely. I wonder if there are tests I should also consider that might relate to these functions. It’s important to ensure everything is accurate and working as expected. I'll take a careful look and maybe probe deeper into understanding those tests!
exec
/bin/zsh -lc "sed -n '470,740p' compute/lib/theorem_ainfty_nonformality_class_m_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,470p' compute/lib/theorem_ainfty_nonformality_class_m_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

    # S_3 = ratio
    S3 = T_1_T_scalar / T_3_T if T_3_T != F(0) else None

    return {
        "T_3_T": T_3_T,
        "T_1_T_scalar": T_1_T_scalar,
        "S3": S3,
    }


def swiss_cheese_m3_virasoro(c: Fraction, N: int = 20) -> Dict[str, Any]:
    r"""Compute Swiss-cheese m_3^{SC} for Virasoro, proving non-formality.

    The cubic shadow S_3 = 2 (c-independent) encodes the nonvanishing of
    m_3^{SC} for class M algebras. This is proved by THREE independent methods:

    Method 1 (OPE coefficient ratio):
      S_3 = (scalar projection of T_{(1)}T) / T_{(3)}T = 2*kappa / kappa = 2.
      This is a finite algebraic identity (no infinite sum needed).
 succeeded in 52ms:

def virasoro_quartic_shadow(c: Fraction) -> Dict[str, Any]:
    r"""Compute the quartic shadow S_4 and contact invariant Q^{contact} for Virasoro.

    S_4(Vir_c) = -(5c + 22) / (10c)
    Q^{contact}(Vir_c) = 10 / [c(5c + 22)]

    These are c-DEPENDENT (unlike S_3 = 2).
    S_4 diverges at c = 0 and at c = -22/5.

    The critical discriminant Delta = 8 kappa S_4:
      Delta = 8 * (c/2) * (-(5c+22)/(10c)) = -4(5c+22)/10 = -2(5c+22)/5

    Delta = 0 iff c = -22/5 (the c_{2,5} minimal model).
    For generic c: Delta != 0, so the tower is infinite (class M).
    """
    if c == F(0):
        return {
            "S4": None,
            "Q_contact": None,
exec
/bin/zsh -lc "sed -n '740,920p' compute/lib/theorem_ainfty_nonformality_class_m_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    Path B (Weight-4 bar differential):
      d_B(s^{-1}T | s^{-1}T) at weight 4 has a nonzero component proportional
      to 2T from the double-pole OPE term. This is the input to the
      three-channel tree sum that produces S_3.

    Path C (Shadow generating function consistency):
      H(t) = S_2 t^2 + S_3 t^3 + S_4 t^4 + ...
      S_2 = 2*kappa = c, S_3 = 2, S_4 = -(5c+22)/(10c).
      Verify: H(t)^2 / t^4 = Q_L(t) = (2kappa + 3*(S_3/3)*t)^2 + 2*Delta*t^2
      where Delta = 8*kappa*S_4.
      Check: q_0 = 4*kappa^2, q_1 = 12*kappa*(S_3/3) = 4*kappa*S_3,
      these coefficients are consistent.

    Path D (c-independence):
      Evaluate the OPE ratio at multiple c values; all give S_3 = 2.
    """
    kappa = c / F(2) if c != F(0) else F(0)

    # Path A: OPE coefficient ratio
    ope_data = virasoro_S3_ope_ratio(c)


thinking
**Evaluating compute engines**

I'm noticing that the current compute engine might have some inaccuracies. It mentions a formula for S4 that doesn’t match the manuscript's canonical form, which raises some questions. The user asked for a computational verification of d_alg, so I should use tests that assert class and shadow_depth, focusing on verifying the right side without relying on potentially incorrect formulas. There's also an independent compute engine to consider, so using both might give a more thorough verification for the user.
thinking
**Cross-checking engine files**

I can run at least one engine file and potentially another to cross-check results. Running all four tests might be possible by targeting specific pytest node IDs from one or two files, ensuring I capture one from each family. I should also inspect the `depth_classification` classify functions to understand family specifics. I’ll search for relevant segments around the classify_* definitions to ensure I’m gathering the necessary information for accurate verification.
exec
/bin/zsh -lc 'rg -n -F "def classify_heisenberg_generic" compute/lib/depth_classification.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
306:def classify_heisenberg_generic(level=1):
exec
/bin/zsh -lc 'rg -n -F "def classify_affine" compute/lib/depth_classification.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "def classify_betagamma" compute/lib/depth_classification.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "def classify_virasoro" compute/lib/depth_classification.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
381:def classify_affine(lie_type, level=1):
 succeeded in 50ms:
457:def classify_betagamma(weight):
 succeeded in 51ms:
508:def classify_virasoro(central_charge):
exec
/bin/zsh -lc "sed -n '300,560p' compute/lib/depth_classification.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


# ============================================================================
# The 20 algebras
# ============================================================================

def classify_heisenberg_generic(level=1):
    """Heisenberg at generic level k > 0.

    kappa = k, alpha = 0 (abelian OPE), S_4 = 0.
    Class G, r_max = 2.
    d_alg = 0, d_arith = 1 (single Eisenstein spectral component).
    d = 1 + 1 + 0 = 2.
    """
    k = Rational(level)
    return DepthClassification(
        name=f'Heisenberg H_{level}',
        kappa=k,
        alpha=Rational(0),
        S4=Rational(0),

thinking
**Investigating mathematical inconsistencies**

I'm checking the user task that involves verifying Heis 0, sl2 1, and betagamma 2, along with "Vir inf." It seems there's an inconsistency that needs addressing. I should inspect the relevant theorem or example regarding whether λ=0 is excluded due to positive grading. I noticed that comments in the code around AP18 indicate a weight-0 generator that could breach positive grading, yet the theorem doesn't seem to exclude it. I need to gather evidence, particularly in the manuscript regarding betagamma with λ=0.
codex
I found a live inconsistency in the compute layer: one classification engine treats `βγ` at `λ=0` as degenerate class `G`, while the theorem surface states the conformal-weight family `βγ_λ` realizes `d_alg=2` with no exclusion of `λ=0`. I’m checking the manuscript and tests around that boundary case before deciding whether to patch the engine or narrow the theorem surface.
exec
/bin/zsh -lc 'rg -n -F "class C" chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex chapters/theory/higher_genus_modular_koszul.tex | head -n 80' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "kappa(beta-gamma, lambda) = 6*lambda''^2 - 6*lambda + 1" compute/tests -g '"'*.py'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"betagamma_lam0\" compute/tests -g '*.py'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"lambda=0\" chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters/theory/higher_genus_modular_koszul.tex CLAUDE.md AGENTS.md compute/tests compute/lib -g '*.tex' -g '*.py' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:26265:$F_1(\cA)=\kappa(\cA)/24$. The $\psi$-class CohFT
chapters/examples/beta_gamma.tex:2670:\index{beta-gamma system@$\beta\gamma$ system!class C mechanism}
chapters/examples/beta_gamma.tex:2671:\index{stratum separation!class C mechanism}
chapters/examples/beta_gamma.tex:2672:\index{Sugawara construction!class C depth}
 succeeded in 51ms:
compute/tests/test_genus4_landscape.py:147:        """kappa(beta-gamma, lambda) = 6*lambda^2 - 6*lambda + 1."""
compute/tests/test_genus3_landscape.py:172:        """kappa(beta-gamma, lambda) = 6*lambda^2 - 6*lambda + 1."""
 succeeded in 51ms:
compute/tests/test_genus2_landscape.py:134:    def test_betagamma_lam0(self):
compute/tests/test_bc_holographic_tensor_shadow_engine.py:249:    def test_kappa_betagamma_lam0(self):
compute/tests/test_depth_classification.py:162:    def test_betagamma_lam0_degenerate(self):
compute/tests/test_depth_classification.py:610:    def test_betagamma_lam0_degenerate(self):
compute/tests/test_kappa_cross_family.py:340:    def test_betagamma_lam0(self):
compute/tests/test_bc_grand_unified_atlas_engine.py:173:    def test_kappa_betagamma_lam05(self):
compute/tests/test_bc_btz_form_factor_engine.py:148:    def test_betagamma_lam05_beta1(self):
compute/tests/test_genus3_landscape.py:677:    def test_betagamma_lam0(self):
compute/tests/test_theorem_quartic_contact_landscape_engine.py:502:    def test_betagamma_lam0_equals_lam1(self):
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:23469:%: from higher_genus_modular_koszul.tex:2888; lambda=0 -> 1, lambda=1/2 -> -1/2 verified
chapters/theory/higher_genus_modular_koszul.tex:23526:% lambda=0: kappa=1, F_1=1/24, F_2=7/5760.
chapters/theory/higher_genus_modular_koszul.tex:23527:% Census (landscape_census.tex:588, bc at lambda=0): F_1=-1/24, kappa=-1.
chapters/theory/higher_genus_modular_koszul.tex:23528:% But bc and betagamma are DIFFERENT: bc(lambda=0) has kappa=-1,
chapters/theory/higher_genus_modular_koszul.tex:23529:% betagamma(lambda=0) has kappa=1. At lambda=0: c_bg=2(0-0+1)=2, kappa=1. Check.
CLAUDE.md:560:| Critical level jump | PROVED | At k=-h^v: kappa=0, ALL monodromy trivial (integer eigenvalues), H^1 doubles (4→8), Koszulness fails, bar H* = Omega*(Op_g^v(D)). Spectral sequence: d_1 = lambda*[delta] vanishes at lambda=0 (prop:critical-level-ordered). 72 tests. |
CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
chapters/examples/free_fields.tex:5593: $\kappa = 6\lambda^2{-}6\lambda{+}1$;\; $= 1$ at $\lambda=0,1$;\; $= -\tfrac{1}{2}$ at $\lambda=\tfrac{1}{2}$ \\
compute/tests/test_bc_bridgeland_stability_engine.py:96:        """Beta-gamma at lambda=0.5: terminates at arity 4 (class C)."""
compute/tests/test_bc_bridgeland_stability_engine.py:716:        """Full analysis for beta-gamma at lambda=0.5."""
compute/tests/test_theorem_large_n_delta_f2_engine.py:815:        """c_wn_thooft at lambda=0 raises."""
compute/tests/test_genus2_landscape.py:135:        """kappa(bg, lambda=0) = 0 - 0 + 1 = 1."""
compute/tests/test_pro_weyl_sl2.py:650:        """lambda=0: Verma has weights 0, -2, -4, ...
compute/tests/test_shadow_tower_ope_recursion.py:1078:        """Beta-gamma lambda=0: c=2, kappa=1."""
compute/tests/test_shadow_tower_ope_recursion.py:1089:        """Beta-gamma lambda=1: c=2, kappa=1 (same as lambda=0)."""
compute/tests/test_shadow_tower_ope_recursion.py:1102:        """MC = sqrt(Q_L) at lambda=0, 1/4, 1/2, 2/3."""
compute/tests/test_bc_ode_im_shadow_engine.py:135:        lambda=0 => c=2, kappa=1 (symmetric under lambda <-> 1-lambda).
compute/lib/phantom_m5_koszul_dual_engine.py:72:   This is the shadow of the W_{1+infty}[lambda=0] = u(infty)_1 theory,
compute/lib/phantom_m5_koszul_dual_engine.py:512:    The dual algebra is W_{1+infty}[lambda=0] = u(infty)_1, the
compute/lib/phantom_m5_koszul_dual_engine.py:529:        "dual_algebra": "W_{1+inf}[lambda=0] = u(infty)_1 = free boson tower",

thinking
**Evaluating classification issues**

I see that a lot of compute libraries are recognizing bg λ=0 as class C. This makes me think that the special case for depth classification might actually be incorrect. I should inspect the related test lines around line 610 since AP18 mentions a degenerate due weight-0 generator, but I'm not entirely sure it links to class G. I should read through those tests to gain clarity.
exec
/bin/zsh -lc "sed -n '150,170p' compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '110,150p' compute/tests/test_betagamma_shadow_full.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,450p' compute/tests/test_betagamma_shadow_full.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '600,620p' compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
        assert a.degenerate
        assert a.kappa == 0

    def test_virasoro_c0_is_degenerate(self):
        """Virasoro c=0: kappa=0, uncurved. Still class M."""
        a = classify_virasoro(0)
        assert a.degenerate
        assert a.kappa == 0
        assert a.depth_class == 'M'

    def test_betagamma_lam0_degenerate(self):
        """betagamma lambda=0: weight-0 generator (AP18)."""
        a = classify_betagamma(0)
        assert a.degenerate
        assert a.kappa == 1  # formula gives kappa=1 even for lambda=0

    def test_ap31_kappa_zero_not_theta_zero(self):
        """AP31: kappa = 0 does NOT imply Theta_A = 0.

        For Virasoro c=0: kappa=0, alpha=2, Delta=40/22. The tower
 succeeded in 52ms:
    """Shadow data on the stress tensor primary line."""

    def test_S2_equals_kappa(self):
        """S_2 on T-line = kappa."""
        for lam_val in [0, Rational(1, 2), 1, 2]:
            assert S2_T_line(lam_val) == kappa(lam_val)

    def test_S3_universal(self):
        """S_3 = 2 on T-line, independent of lambda (Virasoro universal)."""
        for lam_val in [0, Rational(1, 2), 1, 2, Rational(1, 3)]:
            assert S3_T_line(lam_val) == 2

    def test_S4_lambda_1(self):
        """S_4 at lambda=1: c=2, S_4 = 10/(2*32) = 5/32."""
        assert S4_T_line(1) == Rational(5, 32)

    def test_S4_lambda_0(self):
        """S_4 at lambda=0: same as lambda=1 by weight symmetry."""
        assert S4_T_line(0) == Rational(5, 32)

 succeeded in 52ms:
        assert a.r_max == 2

    def test_betagamma_lam1_is_C(self):
        a = classify_betagamma(1)
        assert a.depth_class == 'C'
        assert a.r_max == 4

    def test_betagamma_lam_half_is_C(self):
        a = classify_betagamma(Rational(1, 2))
        assert a.depth_class == 'C'
        assert a.r_max == 4

    def test_betagamma_lam0_degenerate(self):
        a = classify_betagamma(0)
        assert a.depth_class == 'G'
        assert a.degenerate

    def test_virasoro_is_M(self):
        a = classify_virasoro(1)
        assert a.depth_class == 'M'
 succeeded in 52ms:
class TestEdgeCases:
    """AP18: lambda=0 (weight-0 generator), lambda=1/2, etc."""

    def test_lambda_0_weight_0_generator(self):
        """AP18: lambda=0 means gamma has weight 1, beta has weight 0.
        Weight-0 generator violates positive grading, but kappa is still defined."""
        data = evaluate_at_weight(0)
        assert data['c'] == 2
        assert data['kappa'] == 1
        assert data['depth'] == 4

    def test_lambda_half_self_symmetric(self):
        """lambda=1/2: beta and gamma both have weight 1/2 (symplectic boson).
        The system is self-symmetric under beta <-> gamma exchange."""
        data = evaluate_at_weight(Rational(1, 2))
        assert data['c'] == -1
        assert data['kappa'] == Rational(-1, 2)

    def test_lambda_negative(self):
        """lambda = -1: exotic weight. kappa and c well-defined."""









thinking
**Evaluating depth classification**

I’m thinking about how to deal with the inconsistency in the depth classification engine and that it might require patching the compute/lib/depth_classification.py file along with tests. The rg search shows only test_depth_classification mentioning the issue. I also need to include commentary on the edits and possibly do some verification first. It’s not clear if I need to run AP greps afterwards since we're only dealing with .py files, but confirming the necessary fixes seems crucial.
thinking
**Analyzing classify_betagamma**

I’m reflecting on the classify_betagamma function where w==0 should ideally still classify as C, with r_max=4 and d_alg=2, possibly keeping degenerate=True due to the AP18 weight-0 generator, but not class G. I need to check if d_arith is maybe 1 and if d_total equals 4. The theorem could allow for this, as it might pertain to the standard landscape. I’ll also need to patch the tests like test_betagamma_lam0_degenerate to assert these classifications, and consider updating the docstring for clear communication.
thinking
**Identifying patch needs**

I realize I need to focus on searching just those two items. There's definitely a patch required. Also, it seems like the depth_classification engine for classify_betagamma might be utilizing a placeholder, specifically S4=1 and delta=8*kap*1. I need to confirm that and see how this affects my approach to fixing the issues at hand. It's essential to ensure these details are addressed to improve the classification process properly.
thinking
**Searching for theorems**

I need to browse the internet for exact theorem numbers, possibly from arXiv or official papers, since the user explicitly wants me to cross-check the literature. I’m considering whether to use web searches for these primary sources. Specifically, I need to find theorem numbers that are relevant, like those related to derived center and Hochschild, rather than anything directly tied to published theorems. I should also look into supporting ingredients like the BD chiral algebra formalism.
thinking
**Citing theorems and literature**

I’m considering whether I should cite an exact theorem number, but the user specifically asked for both a paper and theorem number. For the literature cross-check, I can look into supporting literature like BD's "Chiral Algebras," focusing on relevant sections instead of exact theorem numbers. I might also check Costello-Gwilliam's volume one for a theorem on factorization algebras related to vertex or chiral aspects. Additionally, I need to look at Lurie’s Higher Algebra for any relevant theorems, particularly regarding the little cubes.
thinking
**Searching for literature proof**

The user is asking about providing proof status for different results, but I'm noticing a depth-gap in literature specifically. I could mention that for a literature cross-check, I might say it’s "not-checked," meaning no direct published theorem is found. I may need to search places like arXiv for relevant works. However, perhaps I should clarify that there isn’t a direct theorem related to the depth-gap trichotomy, even if supporting ingredients exist. I'll handle the broader framework later.
thinking
**Considering literature cross-checks**

I’m thinking about using local files or citations to back up claims instead of browsing the web, but the user specifically asked for a literature cross-check. The system suggests I must browse if the user requests verification. So, while I could look for exact theorem numbers related to Lurie or Costello-Li later, I first need to resolve any inconsistencies in computations. For instance, I've noticed the theorem_ainfty_nonformality_class_m_engine may have a sign/normalization error. I'll clarify that the computational suite needs to verify class values rather than formulas.
thinking
**Auditing test calculations**

I’m considering running tests from this file, focusing on class tests that might not be affected by the wrong S4 formula. There’s still a potential issue, though—should I patch that incorrect formula too? An audit seems necessary. I realize that the tests here include `TestVirasoroQuarticShadow`, which expects S4 to equal a specific formula, so I’ll need to ensure this aligns with the overall calculations. I must be thorough to avoid further complications.
thinking
**Evaluating compute tests**

I’m considering the compute engine used in tests that may mislead results. If I run `TestVirasoroQuarticShadow::test_S4_formula_c26`, it might pass with the wrong formula, which could conflict with the manuscript. The user didn't ask about this, but it might be a wound we need to heal. There could be other engines with the correct formulas, so I should explore those options and mention any residual risks later. I'll inspect tests in `test_theorem_ainfty_nonformality_class_m_engine.py` when necessary.
codex
I found a concrete compute wound and I’m fixing it now. The `depth_classification` engine currently misclassifies `βγ` at `λ=0` as class `G`; I’m patching it to match the theorem surface and the other compute engines, while keeping the AP18 degeneracy note.
file update
M /Users/raeez/chiral-bar-cobar/compute/lib/depth_classification.py
@@ -465,4 +465,5 @@
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
@@ -470,19 +471,2 @@
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
@@ -503,3 +487,9 @@
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/lib/depth_classification.py
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 

file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 

codex
I’m syncing the failing expectations in the direct test file to the corrected theorem-consistent behavior. After that I’ll run the four family tests plus an independent Swiss-cheese suite so the computational check is not relying on one classifier.
file update
M /Users/raeez/chiral-bar-cobar/compute/tests/test_depth_classification.py
@@ -161,5 +161,7 @@
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
@@ -614,2 +616,4 @@
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
apply_patch(auto_approved=true) exited 0 in 33ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/tests/test_depth_classification.py
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..1aa72bfc981b472604d715a73b881e1b4920e7b9
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.

file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..1aa72bfc981b472604d715a73b881e1b4920e7b9
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.


thinking
**Searching for classification references**

I need to revisit some modified sections and look for any other expectations related to `classify_betagamma(0)`. So far, I've only searched within `test_depth_classification`. It might be better to check the classification summary file for any references to `classify_betagamma(0)` and `depth_class == 'G'`. A quick search seems necessary, and I might also want to look at the git diff, possibly using `rg`, to see any relevant changes.
codex
The local fix is in place. I’m checking for any other stale expectations tied to `classify_betagamma(0)` before running the targeted pytest nodes, so the verification run reflects a coherent compute surface rather than one corrected file next to stale consumers.
exec
/bin/zsh -lc "sed -n '156,170p' compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '606,620p' compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '450,520p' compute/lib/depth_classification.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
        d_alg=0,
        d_arith=d_ar,
        d_total=d_tot,
        notes=f'Abelian primary line. k={k}, dim S_k={dim_cusp_forms_sl2z(k) if rank >= 8 and rank % 8 == 0 else "N/A"}.',
    )


def classify_betagamma(weight):
    """betagamma system at conformal weight lambda.

    kappa = 6*lambda^2 - 6*lambda + 1.
    On the weight-changing primary line: alpha = 0 (abelian).
    Quartic contact on CHARGED stratum: S_4 != 0.
    Classification requires stratum separation (rem:contact-stratum-separation).

    For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
    For lambda = 0: the weight-0 generator triggers the AP18 warning,
    but the global quartic/contact witness still gives class C.
    """
 succeeded in 52ms:

    def test_betagamma_lam_half_is_C(self):
        a = classify_betagamma(Rational(1, 2))
        assert a.depth_class == 'C'
        assert a.r_max == 4

    def test_betagamma_lam0_is_class_C_but_flagged(self):
        a = classify_betagamma(0)
        assert a.depth_class == 'C'
        assert a.r_max == 4
        assert a.d_alg == 2
        assert a.degenerate

    def test_virasoro_is_M(self):
        a = classify_virasoro(1)
 succeeded in 52ms:
        """Virasoro c=0: kappa=0, uncurved. Still class M."""
        a = classify_virasoro(0)
        assert a.degenerate
        assert a.kappa == 0
        assert a.depth_class == 'M'

    def test_betagamma_lam0_degenerate(self):
        """betagamma lambda=0: weight-0 generator (AP18)."""
        a = classify_betagamma(0)
        assert a.degenerate
        assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
        assert a.depth_class == 'C'
        assert a.d_alg == 2

    def test_ap31_kappa_zero_not_theta_zero(self):
exec
/bin/zsh -lc "rg -n -F \"classify_betagamma(0)\" compute -g '*.py'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/depth_classification.py:667:    algebras.append(classify_betagamma(0))
compute/tests/test_depth_classification.py:163:        a = classify_betagamma(0)
compute/tests/test_depth_classification.py:614:        a = classify_betagamma(0)
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..1aa72bfc981b472604d715a73b881e1b4920e7b9
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.




thinking
**Inspecting tests for consistency**

I need to check the `build_20_algebra_classification` around line 667 to see if any notes or summaries were affected. It's possible tests that expect the number of G vs C classes might change too. So I should run overall tests for consistency, maybe targeting specific tests, especially since changes could impact all tests in this file. I'll consider running `compute/tests/test_depth_classification.py` to make sure everything works correctly, even though it might include hundreds of tests.
thinking
**Evaluating test strategy**

I'm considering running the full file, which might be fast enough since there are around 90 tests. However, I could go for targeted tests to save time. The `build_20_algebra_classification` summary counts might have changed, but the class distribution could still lead to passing tests. If there's an update needed for `test_betagamma_lam0_degenerate`, I should check it. I’ll likely run eight specific tests, including one that confirms λ=0 at depth 4 for more evidence. But the user specified four tests, so I might prioritize those.
thinking
**Planning test execution**

I think the best approach is to run a few specific tests for comprehensive coverage. I'll start with the full file in `compute/tests/test_depth_classification.py` to ensure the classifier and patched boundary are working. Next, I’ll execute targeted tests from `compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py` focusing on the four class tests. Additionally, I want to run `compute/tests/test_betagamma_shadow_full.py::TestEdgeCases::test_lambda_0_weight_0_generator` to independently verify the λ=0 class C boundary, which feels like a solid strategy, but it's more than just the four tests the user mentioned.
codex
I’ve corrected the βγ boundary classification and I’m moving to verification. The first run is the direct `d_alg` suite; the second is an independent Swiss-cheese shadow-depth suite so the computational confirmation is not just one table lookup.
exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseHeisenbergM3::test_heisenberg_class_G compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseAffineSl2::test_class_L compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseBetagamma::test_class_C compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseVirasoroM3::test_virasoro_shadow_depth_infinite' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_betagamma_shadow_full.py::TestEdgeCases::test_lambda_0_weight_0_generator' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_depth_classification.py::TestDepthFormula::test_heisenberg_depth compute/tests/test_depth_classification.py::TestGLCMClassification::test_affine_sl2_is_L compute/tests/test_depth_classification.py::TestDepthFormula::test_betagamma_depth compute/tests/test_depth_classification.py::TestDepthFormula::test_virasoro_infinite_depth compute/tests/test_depth_classification.py::TestGLCMClassification::test_betagamma_lam0_is_class_C_but_flagged compute/tests/test_depth_classification.py::TestEdgeCases::test_betagamma_lam0_degenerate' in /Users/raeez/chiral-bar-cobar exited 4 in 855ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 5 items

============================ no tests ran in 0.40s =============================
ERROR: not found: /Users/raeez/chiral-bar-cobar/compute/tests/test_depth_classification.py::TestEdgeCases::test_betagamma_lam0_degenerate
(no match in any of [<Class TestEdgeCases>])

 succeeded in 998ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 4 items

compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py ....    [100%]

============================== 4 passed in 0.52s ===============================
 succeeded in 1.00s:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 1 item

compute/tests/test_betagamma_shadow_full.py .                            [100%]

============================== 1 passed in 0.53s ===============================
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..1aa72bfc981b472604d715a73b881e1b4920e7b9
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.


thinking
**Locating test commands**

I noticed that one command had the wrong node ID, so I need to rerun the direct d_alg suite with the correct node IDs. I should check if locating the class name for the edge test is necessary, but we might already have lambda0 from the full test if the node exists. I’ll look for `class TestDegenerateCases` or see if it’s within `TestDepthFormula`. I plan to rerun the targeted suite to avoid missing any nodes.
codex
The independent Swiss-cheese suite passed, and the dedicated `βγ, λ=0` edge-case engine passed. The direct classifier suite had a bad nodeid on my side, so I’m rerunning it cleanly rather than treating a collection error as evidence.
exec
/bin/zsh -lc 'rg -n -F "def test_betagamma_lam0_degenerate" compute/tests/test_depth_classification.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
612:    def test_betagamma_lam0_degenerate(self):
exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_depth_classification.py::TestDepthFormula::test_heisenberg_depth compute/tests/test_depth_classification.py::TestGLCMClassification::test_affine_sl2_is_L compute/tests/test_depth_classification.py::TestDepthFormula::test_betagamma_depth compute/tests/test_depth_classification.py::TestDepthFormula::test_virasoro_infinite_depth compute/tests/test_depth_classification.py::TestGLCMClassification::test_betagamma_lam0_is_class_C_but_flagged' in /Users/raeez/chiral-bar-cobar succeeded in 497ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 5 items

compute/tests/test_depth_classification.py .....                         [100%]

============================== 5 passed in 0.25s ===============================
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..1aa72bfc981b472604d715a73b881e1b4920e7b9
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.


thinking
**Evaluating test runs**

I think I should run the full `test_depth_classification.py` since the patch changed the class counts. Running the entire file might be better to catch any hidden failures, but maybe targeted tests plus edge cases could be okay too. Still, running the whole file seems safer, especially if it only takes a short time for around 50 tests. I’ll also consider if running `test_betagamma_shadow_full` is necessary, but it might be wise to do the full file anyway.
codex
The targeted nodes all pass now. I’m doing one broader pass on the patched classifier file itself so the fix is verified against its own full local consistency suite, not only the four hand-picked family checks.
exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_depth_classification.py' in /Users/raeez/chiral-bar-cobar exited 1 in 571ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 132 items

compute/tests/test_depth_classification.py ............................. [ 21%]
........................................................................ [ 76%]
.....F.........................                                          [100%]

=================================== FAILURES ===================================
___________________ TestConsistency.test_class_distribution ____________________

self = <compute.tests.test_depth_classification.TestConsistency object at 0x10af11310>
algebras = [DepthClassification(name='Heisenberg H_1', kappa=1, alpha=0, S4=0, delta=0, depth_class='G', r_max=2, d_alg=0, d_arit...d_alg=1, d_arith=1, d_total=3, degenerate=False, notes='dim(g)=14, h^v=4. Jacobi kills quartic on primary line.'), ...]

    def test_class_distribution(self, algebras):
        """Count class distribution."""
        counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..1aa72bfc981b472604d715a73b881e1b4920e7b9
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.


thinking
**Updating test distribution expectations**

I need to patch the test distribution expectations. It looks like counts C might now be 3, so I'll need to update that. I should search around line 700 for any relevant information and check the patch comments and expectations. I wonder if there are any other notes I could consider. It seems important to inspect the area around the failing test to ensure I address everything appropriately.
codex
The broader suite exposed exactly one stale expectation: the class-count summary still had `βγ, λ=0` counted under `G`. I’m updating that expectation and rerunning the full classifier file so the repaired boundary case is consistent all the way through.
exec
/bin/zsh -lc "sed -n '704,722p' compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
        assert len(algebras) == 20

    def test_class_distribution(self, algebras):
        """Count class distribution."""
        counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
        for a in algebras:
            counts[a.depth_class] += 1
        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
        #           L=4 (sl2, sl3, G2, E8 affine)
        #           C=2 (bg_lam1, bg_lam_half)
        #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
        assert counts['G'] == 7
        assert counts['L'] == 4
        assert counts['C'] == 2
        assert counts['M'] == 7

    def test_no_class_G_has_infinite_depth(self, algebras):
        for a in algebras:
            if a.depth_class == 'G':
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..1aa72bfc981b472604d715a73b881e1b4920e7b9
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.

file update
M /Users/raeez/chiral-bar-cobar/compute/tests/test_depth_classification.py
@@ -710,9 +710,9 @@
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
apply_patch(auto_approved=true) exited 0 in 30ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/compute/tests/test_depth_classification.py
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_depth_classification.py' in /Users/raeez/chiral-bar-cobar succeeded in 764ms:
============================= test session starts ==============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/raeez/chiral-bar-cobar
configfile: pyproject.toml
plugins: anyio-4.13.0
collected 132 items

compute/tests/test_depth_classification.py ............................. [ 21%]
........................................................................ [ 76%]
...............................                                          [100%]

============================= 132 passed in 0.44s ==============================
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

codex
The compute surface is stable again: the patched classifier file now passes in full, and the independent Swiss-cheese suite still passes. I’m finishing the verification loop with the requested AP greps and then moving to the literature cross-check and proof-status writeup.
exec
/bin/zsh -lc "rg -n -e \"\\\\Omega/z\" -e \"T\\"'^c'"\\(s\\"'^-1 A'"\\)\" -e \"notably|additionally|moreover|furthermore|crucially|remarkably|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|journey|navigate|—|---\" compute/lib/depth_classification.py compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- compute/lib/depth_classification.py compute/tests/test_depth_classification.py' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\Omega/z)|(?:T\^c\(s\^-1 A\))|(?:notably|additionally|moreover|furthermore|crucially|remarkably|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|journey|navigate|—|---)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21..7f5229c 100644
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@ def classify_betagamma(weight):
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
exec
/bin/zsh -lc 'rg -n -F "B(A) is a coalgebra over SC" compute/lib/depth_classification.py compute/tests/test_depth_classification.py' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):


thinking
**Rerunning grep command**

I need to rerun the grep command, but I should consider using a fixed-string option or making it simpler. Maybe using multiple flags with -F could work better. I want to make sure I’m doing this efficiently, so I’ll keep testing until I get it right. Finding the right command is important, and I want to ensure I’m on the right track to accomplish what I need. Let's try this approach!
exec
/bin/zsh -lc "rg -n -F -e '\\Omega/z' -e 'T"'^c(s''^{-1} A)'"' -e 'B(A) is a coalgebra over SC' compute/lib/depth_classification.py compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -i -e 'notably|additionally|moreover|furthermore|crucially|remarkably|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|journey|navigate|---|—' compute/lib/depth_classification.py compute/tests/test_depth_classification.py" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):



thinking
**Checking literature on E_n centers**

I’m considering whether there's any literature or theorems related to E_n centers and Hochschild. I’ll need to reference specific papers, theorem numbers, and ensure that everything checks out with conventions. Since my result isn't directly found in the literature, it might be useful to cite supporting items like the Beilinson-Drinfeld work on "Chiral Algebras," but I need to find the relevant theorem numbers to do that accurately.
thinking
**Searching for literature on d_alg gaps**

I need to find published literature on the d_alg gap, but my initial search for specific terms might not yield results. It's possible I could confirm the absence through a literature search, but it could be more efficient to check within a local bibliography file instead. Since the user is looking for published work, I'll search the local bib file for citations linked to BD, PTVV, and others to get relevant paper titles. I'll locate the bib keys first.
codex
I have the manuscript and compute surface aligned. The last substantive pass is the requested literature check: I’m identifying the exact cited primary sources and theorem numbers that support the framework, while separating that from the parts of the depth-gap trichotomy that appear to be genuinely new to the manuscript.
Plan update
Constitutional reads and live-surface audit are complete; compute verification found and repaired a real βγ boundary inconsistency. I’m now finishing the literature cross-check and final proof-status synthesis.
  ✓ Read required constitutional and status files, then locate all live manuscript and compute surfaces for d_alg, S_4, and related theorems
  → Audit the manuscript proofs and theorem status for the depth-gap claim, including alternative proof routes and literature anchors
  ✓ Run the four compute verifications for Heisenberg, sl_2 KM, betagamma, and Vir, then classify any discrepancies
  ✓ Patch remaining wounds in source/tests if needed, propagate any live-surface fixes, and rerun narrow verification plus AP greps
  • Produce a grounded rescue report with proof status, alternative routes, literature cross-checks, and confidence levels
exec
/bin/zsh -lc "rg -n \"Beilinson|Drinfeld|Francis|Gaitsgory|Costello|Gwilliam|Lurie|PTVV|Calaque|Li\" *.bib bibliography* refs* chapters -g '*.bib' -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: no matches found: *.bib
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):


thinking
**Locating bib files**

I need to use the command `rg --files` to locate bib files. It's a pretty straightforward approach! I wonder if there are any specific directories where these files might be more likely to be found, or if I need to search the entire system. Overall, I feel confident about using this command, but I’ll just double-check to make sure everything is set up correctly before diving in. Let’s see what I find!
exec
/bin/zsh -lc "rg --files -g '*.bib' -g '*bibliography*' -g '*refs*'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
fix_wave_B_20260413_171623/B14_stale_cross_vol_refs_v2.md
fix_wave_B_20260413_171623/B15_stale_cross_vol_refs_v3.md
fix_wave_B_20260413_171623/B08_fix_broken_refs_v3.md
audit_campaign_20260412_231034/XV12_part_refs.md
audit_campaign_20260412_231034/SI02_broken_refs_v2.md
audit_campaign_20260412_231034/SI01_broken_refs_v1.md
relaunch_wave2_empties/U07_forward_refs_v1.md
relaunch_wave2_empties/F17_dangling_refs_v1.md
relaunch_wave2_empties/F18_dangling_refs_v2.md
scripts/export_vol1_xrefs.py
fix_wave_A_20260413_112727/A12_fix_broken_refs_v1_rest.md
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md
fix_wave_A_20260413_112727/A20_fix_broken_refs_v2.md
wave2_audit_20260413_001942/U07_forward_refs_v1.md
wave2_audit_20260413_001942/F17_dangling_refs_v1.md
wave2_audit_20260413_001942/B18_bibliography_sync.md
wave2_audit_20260413_001942/F19_dangling_refs_v3.md
wave2_audit_20260413_001942/F18_dangling_refs_v2.md
relaunch_20260413_111534/U07_forward_refs_v1.md
relaunch_20260413_111534/F17_dangling_refs_v1.md
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc 'rg -n "Beilinson|Drinfeld|Francis|Gaitsgory|Costello|Gwilliam|Lurie|PTVV|Calaque|Li" standalone/references.bib' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
38:% Beilinson--Drinfeld: two keys used (BD, BD04)
40:  author    = {Beilinson, Alexander and Drinfeld, Vladimir},
62:@article{BelavinDrinfeld82,
63:  author  = {Belavin, Alexander A. and Drinfeld, Vladimir G.},
91:  author  = {Beilinson, Alexander and Ginzburg, Victor and Soergel, Wolfgang},
112:  author  = {Beilinson, Alexander and Schechtman, Vadim},
125:  author    = {Costello, Kevin and Gwilliam, Owen},
148:  author  = {Creutzig, Thomas and Linshaw, Andrew R. and Nakatsuka, Shigenori
156:@article{CostelloGaiotto2020,
157:  author  = {Costello, Kevin and Gaiotto, Davide},
189:  title   = {Line operators in {$3$d} holomorphic-topological gauge theory
195:@article{Drinfeld1985,
196:  author  = {Drinfeld, Vladimir G.},
204:@article{Drinfeld85,
205:  crossref = {Drinfeld1985},
209:  author  = {Drinfeld, Vladimir G. and Sokolov, Vladimir V.},
210:  title   = {Lie algebras and equations of {K}orteweg--de {V}ries type},
290:  author  = {Francis, John and Gaitsgory, Dennis},
363:  author  = {Gan, Wee Liang and Ginzburg, Victor},
412:  author = {Lurie, Jacob},
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):


thinking
**Inspecting bibliographic entries**

I think I need to take a closer look at the relevant bibliographic entries. It's important to ensure that the sources are accurate and appropriate for the content I’m working on. I wonder if I have every necessary detail in place and if anything needs updating or correcting. So, let's check the citations and make sure they're all lined up properly for the user's needs! This could help clarify things moving forward.
exec
/bin/zsh -lc "sed -n '38,150p' standalone/references.bib" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% Beilinson--Drinfeld: two keys used (BD, BD04)
@book{BD04,
  author    = {Beilinson, Alexander and Drinfeld, Vladimir},
  title     = {Chiral Algebras},
  series    = {AMS Colloquium Publications},
  volume    = {51},
  publisher = {American Mathematical Society},
  address   = {Providence, RI},
  year      = {2004},
}

@book{BD,
  crossref = {BD04},
}

@article{Belavin81,
  author  = {Belavin, Alexander A.},
  title   = {Dynamical symmetry of integrable quantum systems},
  journal = {Nuclear Phys. B},
  volume  = {180},
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc "sed -n '280,430p' standalone/references.bib" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

@article{FFR94,
  crossref = {FFR1994},
}

@article{FeiginFrenkel94,
  crossref = {FFR1994},
}

@article{FG12,
  author  = {Francis, John and Gaitsgory, Dennis},
  title   = {Chiral {K}oszul duality},
  journal = {Selecta Math. (N.S.)},
  volume  = {18},
  number  = {1},
  year    = {2012},
  pages   = {27--87},
}

@article{FG,
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc "sed -n '660,720p' standalone/references.bib" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  note      = {arXiv:0905.2621},
}

@article{Premet02,
  author  = {Premet, Alexander},
  title   = {Special transverse slices and their enveloping algebras},
  journal = {Adv. Math.},
  volume  = {170},
  year    = {2002},
  pages   = {1--55},
  note    = {With an appendix by S.~Skryabin},
}

@article{Priddy70,
  author  = {Priddy, Stewart},
  title   = {Koszul resolutions},
  journal = {Trans. Amer. Math. Soc.},
  volume  = {152},
  year    = {1970},
  pages   = {39--60},
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc 'rg -n "Costello, Kevin and Li|Costello.*Li|Li, Si" standalone/references.bib' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):



thinking
**Exploring theorem searches**

I could search the web for official PDFs or arXiv documents without quoting too much. A potential strategy might be to use direct queries with exact titles and theorem numbers straight from my memory. For example, I can search for "Francis Gaitsgory chiral Koszul duality theorem 4.1 pdf" or "Higher Algebra Deligne conjecture theorem 5.3.1.19 pdf." It's also worth looking into other theorem references like the PTVV shifted symplectic theorem. I might need to cross-check some theorems as I dig deeper.
thinking
**Searching for FG12 theorem numbers**

I’m looking to search online for information about FG12 theorem numbers. It’s important to find reliable sources that can provide the relevant details. I'll focus on keywords that specifically pertain to the theorem numbers I need to understand better. Once I have the search results, I'll analyze the findings to provide an accurate summary for myself and ensure I capture all the significant points. Let's see what I can find!
🌐 Searching the web...
🌐 Searched: Francis Gaitsgory Chiral Koszul duality theorem pdf

thinking
**Searching for theorem details**

The search results look good! I think I need to open the FG paper and find the theorem number in the PDF. I wonder if I can search within the PDF for the specific theorem lines or maybe even take a screenshot of those lines. I’m not quite sure whether to open the PDF or the HTML version first. Alright, let's see which option works best!
🌐 Searching the web...
🌐 Searched: https://sites.math.northwestern.edu/~jnkf/writ/chiral.pdf
🌐 Searching the web...
🌐 Searched: "Beilinson Drinfeld" "Chiral Algebras" PDF theorem 3.4.9

thinking
**Searching for references**

I’m considering using the FG reference along with BD theorem numbers and the AMS page for existence. That might be sufficient. I also need to look for Lurie’s work. I think a direct search result might lead me to an official PDF. So, I’ll put together a search query and open it up to find what I need. Let's see what I can uncover!
🌐 Searching the web...
🌐 Searched: site:math.ias.edu "Higher Algebra" "5.3.1.19"

thinking
**Searching for theorem numbers**

I'm working with a PDF and need to find specific theorem numbers. I could use the "find" function within the PDF to search for "Deligne." That seems like a straightforward approach to locate the information I need quickly. I want to make sure I get the right theorem numbers without any confusion, so that search will help narrow things down effectively! Let's see what I can find.
🌐 Searching the web...
🌐 Searched: 'Deligne' in https://www.math.ias.edu/~lurie/papers/HA.pdf

thinking
**Reviewing theorem details**

Okay, I’m feeling good about this! I have theorem 5.3.1.14 and corollary 5.3.1.15 that relate to centers and centralizers. I’m thinking I should also mention E_{k+1}. Plus, it seems I need to include the PTVV theorem, so I’ll need to search within the PTVV PDF for those relevant lines. Let’s make sure everything connects clearly!
🌐 Searching the web...
🌐 Searched: PTVV shifted symplectic structures theorem mapping stack arxiv pdf

thinking
**Searching for theorem reference**

I need to find the theorem number within PTVV. I think searching the PDF for "Theorem 2.5" could be helpful, particularly if it's related to the mapping stack theorem. It sounds like a good idea to open the Numdam PDF and look there. I want to ensure I have accurate information, so I'll keep my focus on locating that specific theorem. Let's see what I can find!
🌐 Searching the web...
🌐 Searched: https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf

thinking
**Searching for papers**

I’m thinking it might be a good idea to search for the names of papers by Costello and Li. My current plan is to use a search query like “Costello Li factorization algebra theorem vertex algebra.” This should help me find relevant information. I just want to ensure I get the right results and see what research studies are out there regarding their work. Let’s see what comes up!
🌐 Searching the web...
🌐 Searched: "Costello" "Li" factorization algebra theorem vertex algebra pdf

thinking
**Searching for references**

It looks like my search didn’t turn up much on Costello-Li, so I might not be able to use that information. I could try searching for "Costello Li" more broadly, but it seems like it might return quantum BCOV results, which may not be what I need. Instead, I think I’ll focus on searching “site:arxiv.org" with "Costello Li" to see if there are any relevant papers on factorization algebra. That seems like a solid plan!
🌐 Searching the web...
🌐 Searched: site:arxiv.org "Costello" "Li" factorization algebra



thinking
**Searching theorem numbers**

I'm assessing that the search tool isn't functioning well right now. I think it's best not to follow the Costello-Li lead for now. Instead, I might need to look into the specific theorem numbers in FG and check on Theorem 1.2.4. I wonder if I should explore the section around 4.8.1.1, but maybe that's not necessary. I could also consider looking for the theorem numbers related to `Calaque Haugseng Scheimbauer`, depending on the user's CFG details.
thinking
**Cross-checking literature**

I'm putting together a potential final cross-check table for the literature. For BD04, it's confirmed at the framework level through FG12's introduction, which cites BD Theorem 3.4.9 about the equivalence of chiral Lie algebras and factorization coalgebras on curves. It also mentions Theorem 4.8.1.1 concerning chiral homology of chiral envelopes. 

Then there’s FG12 Theorem 1.2.4, which confirms the chiral and factorization Koszul-duality framework and matches the repo’s requirement that bar objects are coalgebraic. The Lurie HA Theorem 5.3.1.14 and Corollary 5.3.1.15 discuss centralizers in symmetric monoidal categories, supporting the derived centering upgrade. Lastly, PTVV13 Theorems 0.4 and 2.5 detail the mapping stacks of oriented objects with shifted symplectic forms.
thinking
**Reviewing theorem proof**

I need to critically review the theorem proof because I found an inconsistency in the computations, but not in the theorem itself. I should examine the proof details for any gaps. For `Lemma 17767`, the first proof applies a recursion formula related to single-line inversion. It might be helpful to verify the coefficient calculations from this formula. I think I should inspect the recursion formula and compute directly from the closed form, possibly using symbolic computation. Let's search around `eq:single-line-inversion`.
codex
The literature pass is showing what I expected: the chiral/factorization and center/symplectic framework has direct published anchors, but the actual `d_alg` gap theorem looks manuscript-internal. I’m doing one last local check on the recursion formula used in the proof so the final report can separate “framework confirmed by literature” from “new argument verified internally and computationally.”
exec
/bin/zsh -lc 'rg -n -F "eq:single-line-inversion" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
17792:\begin{equation}\label{eq:single-line-inversion}
17829:recursion~\eqref{eq:single-line-inversion} at
17852:reproducing the MC recursion~\eqref{eq:single-line-inversion}.
17923:equation~\eqref{eq:single-line-inversion} at degree $r = 5$ gives
18248:of~\eqref{eq:single-line-inversion}
18267:(iv)~The recursion~\eqref{eq:single-line-inversion}
18764:On a primary line~$L$, the shadow obstruction tower has intrinsic OPE data at degrees $2$, $3$, $4$ only. All shadow coefficients $S_r$ for $r \geq 5$ are determined by the MC recursion~\eqref{eq:single-line-inversion} from the three initial values $(\kappa, \alpha, S_4)$. Equivalently, the shadow metric $Q_L$ is determined by three parameters, and its square root $\sqrt{Q_L}$ generates all higher shadows without further OPE input.
19947:the recursion~\eqref{eq:single-line-inversion} on~$L_T$
30279:that the MC recursion~\eqref{eq:single-line-inversion}
exec
/bin/zsh -lc "sed -n '17520,17720p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
while aspects~\textup{(ii)} and~\textup{(iii)} detect the
shadow depth class. The common notation~``$m_k$'' for both
\textup{(i)} and~\textup{(ii)} is a source of systematic
confusion (i)~lives on $H^*(\Barch)$,
(ii)~lives on~$\cA$, and (iii)~lives on~$\gAmod$.
Computational verification:
\texttt{compute/lib/theorem\_ainfty\_nonformality\_class\_m\_engine.py}.
\end{proposition}

\begin{proof}
Aspect~(i): Theorem~\ref{thm:koszul-equivalences-meta}(iii).
Aspect~(ii): for class~$\mathbf{G}$,
the SC operations on~$\cA$ vanish for $k \geq 3$ because
Heisenberg has trivial OPE beyond the Killing form.
For class~$\mathbf{L}$ (affine KM), $m_3^{\mathrm{SC}} \neq 0$
from the Jacobi cubic tree sum, but
$m_k^{\mathrm{SC}} = 0$ for $k \geq 4$ because the Jacobi
identity kills the quartic contact
(Proposition~\ref{prop:swiss-cheese-nonformality-by-class}).
For class~$\mathbf{C}$
exec
/bin/zsh -lc "python3 - <<'PY'
from fractions import Fraction as F
# Verify the degree-5/6 recursion numerically from H(t)=t"'^2*sqrt(Q) for sample parameters.
# Case alpha!=0,S4!=0
kappa=F(1); alpha=F(2); S4=F(3)
Delta=8*kappa*S4
# Expand sqrt((2k+3at)''^2+2Dt''^2) to t''^6 by direct series via sympy
import sympy as s
k,a,d,t=s.symbols('"'k a d t')
expr=s.sqrt((2*k+3*a*t)**2+2*d*t**2)
series=s.series(expr.subs({k:1,a:2,d:24}),t,0,7).removeO().expand()
print(series)
# Case alpha=0,S4"'!=0
expr2=s.sqrt((2*t*0+2)**2+2*24*t**2)
print(s.series(expr2,t,0,8).removeO().expand())
PY' in /Users/raeez/chiral-bar-cobar succeeded in 271ms:
-756*t**6 + 72*t**4 - 36*t**3 + 12*t**2 + 6*t + 2
216*t**6 - 36*t**4 + 12*t**2 + 2
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):


thinking
**Analyzing series discrepancies**

I'm trying to figure out why the series from sqrt Q isn't matching because of the powers of t. For k=1 and alpha=2, I calculated Q, and the resulting series seems weird. When I set H = t^2 sqrtQ, the coefficients S2=2 and S3=6 don’t line up as expected. I need to check the manuscript for definitions of H(t). Maybe I can verify the recursion calculations after looking at earlier equations, but maybe I won't need to if the theorem proof is accepted.
exec
/bin/zsh -lc "sed -n '17784,17808p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 t^2\sqrt{Q_L(t)}.
\end{equation}
The entire shadow obstruction tower on~$L$ is determined by three
genus-$0$ invariants $(\kappa, \alpha, S_4)$.
\end{theorem}

\begin{proof}
On~$L$ the master equation reduces to the recursion
\begin{equation}\label{eq:single-line-inversion}
 S_r
 \;=\;
 -\frac{P}{2r}
 \sum_{\substack{j + k = r + 2 \\ 3 \leq j \leq k}}
 c_{jk}\,jk\,S_j\,S_k,
 \qquad
 c_{jk} = \begin{cases} 1 & j < k, \\ 1/2 & j = k.\end{cases}
\end{equation}
The H-Poisson bracket
$\{S_j x^j,\,S_k x^k\}_H = jk\,P\,S_j S_k\,x^{j+k-2}$
and the eigenvalue identity
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):


thinking
**Verifying algebraic calculations**

I'm thinking about running a direct algebraic script to verify my results. For instance, when alpha, S4, and kappa are all equal to 1, recursion gives a nonzero S5. Meanwhile, if alpha is 0, S4 is 1, and kappa is 1, S5 ends up being 0 while S6 is nonzero at -2/3. It seems I might have enough info already, but I should check local notes and look up the Francis Gaitsgory theorem for relevant lines before finalizing everything.
🌐 Searching the web...
🌐 Searched: https://www.math.ias.edu/~lurie/papers/HA.pdf

thinking
**Searching for theorem details**

I see that I might have accessed a direct URL that led to a site instead. I need to find theorem 5.3.1.14, so I'll look for it within the PDF document. This means using the search function inside the PDF to locate the specific lines I need. I’ll take my time to make sure I get the right information!
🌐 Searching the web...
🌐 Searched: 'Theorem 5.3.1.14' in https://www.math.ias.edu/~lurie/papers/HA.pdf

thinking
**Searching for FG and theorems**

I think I need to explore some theorems that might be relevant to FG. Okay, so I'll do a search to find useful information, particularly around any lines associated with it. It’s important to keep my focus narrow to gather the most relevant data. I want to ensure that I cover everything properly, so being thorough is key. Let’s see what I uncover!
🌐 Searching the web...
🌐 Searched: 'Theorem 1.2.4' in https://sites.math.northwestern.edu/~jnkf/writ/chiral.pdf
🌐 Searching the web...
🌐 Searched: 'Theorem 0.4' in https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf

thinking
**Searching for resources**

I think it’s a good idea to search for the BD book PDF from AMS, especially since the user specifically requested it. I’m considering using the query `ams chiral algebras sample pdf 3.4.9`, although I wonder if that’s absolutely necessary if I haven’t checked other resources yet. Still, since the user is looking for something specific regarding theorem 3.4.9, I should definitely at least attempt to search. Let’s see what I can find!
🌐 Searching the web...
🌐 Searched: "Theorem 3.4.9" "Chiral Algebras"

thinking
**Evaluating test procedures**

I think it's probably fine to skip searching `class C`, since there are already many libraries we know to be consistent. I'm considering running `python3 -m pytest` on specific test files after applying the final patch to see if everything still passes. We already have the full depth classification suite passing, and the independent suite is running without needing the patch. Also, the earlier edge tests have passed, which is reassuring.
codex
I’m extracting one exact symbolic sanity check from the recursion itself: one mixed sample with `α≠0, S_4≠0`, and one contact sample with `α=0, S_4≠0`. That gives a tool-backed witness for the non-cancellation mechanism stated in the proof.
exec
/bin/zsh -lc "python3 - <<'PY'
from fractions import Fraction as F

def next_coeff(kappa, coeffs, r):
    P = F(1,1) / kappa
    total = F(0,1)
    for j in range(3, r):
        k = r + 2 - j
        if j > k or k < 3:
            continue
        c = F(1,2) if j == k else F(1,1)
        total += c * j * k * coeffs.get(j, F(0,1)) * coeffs.get(k, F(0,1))
    return -P * total / (2 * r)

# Mixed case: alpha "'!= 0, S4 != 0
coeffs = {2:F(1), 3:F(2), 4:F(3)}
print({'"'case':'mixed', 'S5': next_coeff(F(1), coeffs, 5)})
# Contact case: alpha = 0, S4 "'!= 0
coeffs = {2:F(1), 3:F(0), 4:F(3)}
coeffs[5] = next_coeff(F(1), coeffs, 5)
coeffs[6] = next_coeff(F(1), coeffs, 6)
print({'"'case':'contact', 'S5': coeffs[5], 'S6': coeffs[6]})
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
{'case': 'mixed', 'S5': Fraction(-36, 5)}
{'case': 'contact', 'S5': Fraction(0, 1), 'S6': Fraction(-6, 1)}
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):


thinking
**Checking witness details**

I think mentioning the exact witness would be helpful. I noticed that S6 equals -6 because S4 is 3, which doesn't follow the formula -2/3*S4^2/κ being equal to -6. It seems good to clarify that. Maybe I should check web results for the exact line numbers? I could open relevant pages for the theorem to have solid citations. Let’s see what I can find!
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: AMS Chiral Algebras Beilinson Drinfeld

thinking
**Updating plan for proofs**

I’m looking at the trichotomy found, which seems acceptable. I could mention that confidence is high since the theorem is backed by two manuscript proofs and two compute suites. I need to make a final mention about patching the compute engine. Should I update the plan for the final step? Maybe I should ensure that all steps are completed before finalizing. Let's go ahead and update the plan!
Plan update
The depth-gap surface has been audited, the compute inconsistency at βγ λ=0 was repaired, the relevant test suites pass, and the literature/framework cross-check has been gathered. Only the final rescue report remains.
  ✓ Read required constitutional and status files, then locate all live manuscript and compute surfaces for d_alg, S_4, and related theorems
  ✓ Audit the manuscript proofs and theorem status for the depth-gap claim, including alternative proof routes and literature anchors
  ✓ Run the four compute verifications for Heisenberg, sl_2 KM, betagamma, and Vir, then classify any discrepancies
  ✓ Patch remaining wounds in source/tests if needed, propagate any live-surface fixes, and rerun narrow verification plus AP greps
  → Produce a grounded rescue report with proof status, alternative routes, literature cross-checks, and confidence levels
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):


thinking
**Inspecting git status**

I think I need to inspect the git status to see which files have changed. It feels pretty important to mention that, especially if I'm keeping track of updates. Making sure I know what files have been modified or added can help me understand what’s going on with the project. So yeah, I'll definitely check that out to get a clearer picture of the current situation.
exec
/bin/zsh -lc 'git status --short compute/lib/depth_classification.py compute/tests/test_depth_classification.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 M compute/lib/depth_classification.py
 M compute/tests/test_depth_classification.py
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc "nl -ba compute/tests/test_depth_classification.py | sed -n '159,170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/depth_classification.py | sed -n '457,505p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   159	        assert a.depth_class == 'C'
   160	        assert a.r_max == 4
   161	
   162	    def test_betagamma_lam0_is_class_C_but_flagged(self):
   163	        a = classify_betagamma(0)
   164	        assert a.depth_class == 'C'
   165	        assert a.r_max == 4
   166	        assert a.d_alg == 2
   167	        assert a.degenerate
   168	
   169	    def test_virasoro_is_M(self):
   170	        a = classify_virasoro(1)
 succeeded in 51ms:
   457	def classify_betagamma(weight):
   458	    """betagamma system at conformal weight lambda.
   459	
   460	    kappa = 6*lambda^2 - 6*lambda + 1.
   461	    On the weight-changing primary line: alpha = 0 (abelian).
   462	    Quartic contact on CHARGED stratum: S_4 != 0.
   463	    Classification requires stratum separation (rem:contact-stratum-separation).
   464	
   465	    For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
   466	    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
   467	    For lambda = 0: the weight-0 generator triggers the AP18 warning,
   468	    but the global quartic/contact witness still gives class C.
   469	    """
   470	    w = Rational(weight)
   471	    kap = kappa_betagamma(weight)
   472	
   473	    # For the contact classification, we use the fact that the quartic
   474	    # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
   475	    # The single-line dichotomy doesn't directly apply because the quartic
   476	    # is on a different stratum. We assign class C by the global analysis.
exec
/bin/zsh -lc "nl -ba compute/tests/test_depth_classification.py | sed -n '612,720p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   612	    def test_betagamma_lam0_degenerate(self):
   613	        """betagamma lambda=0: weight-0 generator (AP18)."""
   614	        a = classify_betagamma(0)
   615	        assert a.degenerate
   616	        assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
   617	        assert a.depth_class == 'C'
   618	        assert a.d_alg == 2
   619	
   620	    def test_ap31_kappa_zero_not_theta_zero(self):
   621	        """AP31: kappa = 0 does NOT imply Theta_A = 0.
   622	
   623	        For Virasoro c=0: kappa=0, alpha=2, Delta=40/22. The tower
   624	        is still infinite (class M). Higher-arity shadows may be nonzero.
   625	        """
   626	        a = classify_virasoro(0)
   627	        assert a.kappa == 0
   628	        assert a.depth_class == 'M'  # NOT class G!
   629	        assert a.r_max is None  # infinite tower
   630	
   631	
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17767,17960p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 17767	The \emph{critical discriminant} of~$L$ is
 17768	\begin{equation}\label{eq:critical-discriminant}
 17769	 \Delta \;:=\; 8\,\kappa\,S_4
 17770	 \;=\; a_0\,a_2.
 17771	\end{equation}
 17772	\end{definition}
 17773	
 17774	\begin{theorem}[Riccati algebraicity: the shadow generating function
 17775	 is algebraic of degree~$2$]
 17776	\label{thm:riccati-algebraicity}
 17777	\label{thm:shadow-metric-existence}
 17778	\ClaimStatusProvedHere
 17779	\index{shadow generating function!algebraicity|textbf}
 17780	\index{Riccati algebraicity|textbf}
 17781	Let $L$, $S_r$, $Q_L$ be as in
 17782	Definition~\textup{\ref{def:shadow-metric}}.
 17783	Set $P = 1/\kappa$ and define the weighted shadow
 17784	generating function
 17785	$H(t) := \sum_{r \geq 2} r\,S_r\,t^r$.
 17786	The all-degree master equation
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17960,18005p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 17960	The closed form $H(t) = t^2\sqrt{Q_L(t)}$ with $Q_L = (2\kappa + 3\alpha\,t)^2 + 2\Delta\,t^2$
 17961	and $\Delta = 8\kappa S_4 \neq 0$ then gives the full conclusion:
 17962	$Q_L$ is not a perfect square, so $\sqrt{Q_L}$ has infinitely many
 17963	nonzero Taylor coefficients.
 17964	
 17965	\emph{Second proof: shadow Lie algebra weight structure.}
 17966	On the primary line $L = \Bbbk \cdot x$, the Hamiltonian model of
 17967	the shadow algebra has bracket
 17968	$\{x^j, x^k\}_H = jk\,P\,x^{j+k-2}$ with $P = \kappa^{-1}$.
 17969	The shadow elements $h := \kappa x^2$, $\mathfrak{C} := S_3 x^3$,
 17970	$\mathfrak{Q} := S_4 x^4$ act by
 17971	\[
 17972	 D_h(x^r) = 2r\,x^r,\qquad
 17973	 D_{\mathfrak{C}}(x^r) = 3r\,P\,S_3\,x^{r+1},\qquad
 17974	 D_{\mathfrak{Q}}(x^r) = 4r\,P\,S_4\,x^{r+2}.
 17975	\]
 17976	The operator $D_h$ is a semisimple grading, while
 17977	$D_{\mathfrak{Q}}$ raises degree by~$2$.
 17978	If $S_4 \neq 0$ then
 17979	\[
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):



thinking
**Finalizing findings**

I need to make sure I reference local files but not overload with them. It's important to mention "Riccati algebraicity plus discriminant dichotomy" as proof and include any alternatives if necessary. I think I should add a final note that states there are no remaining actionable findings on this surface. After that, I can conclude with something like "No further surviving discrepancies found on this d_alg surface." That should wrap it up nicely!
thinking
**Organizing Literature Review**

I’m considering the potential residual risks regarding the completed literature cross-check for CG/CFG/Costello-Li. It might be okay to start without an interjection, focusing on clarity. I think using markdown headers could help, possibly with four sections, but three may keep it concise. I'll label them as `**Finding**`, `**Status**`, and `**Verification**`. Under the Status section, I should include a shorter literature subpart. Ensuring no nested bullets is vital, aiming for around 12 clear points total.
codex
**Finding**
- `SERIOUS`: `βγ(λ=0)` was stale in the compute layer: it was classified as class `G` / `d_alg=0` in [depth_classification.py](/Users/raeez/chiral-bar-cobar/compute/lib/depth_classification.py:457), contradicting the manuscript depth-gap surface at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18003) and the existing βγ edge engines. I fixed the classifier and synced the direct tests in [test_depth_classification.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_depth_classification.py:162). No further surviving discrepancies showed up on this `d_alg` surface.

**Status**
- Overall theorem `d_alg ∈ {0,1,2,∞}`, no finite `d_alg ≥ 3`: primary proof is `ProvedHere` at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18003), resting on Riccati algebraicity and the quadratic discriminant dichotomy at [17774](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17774). Alternative proof is also written there: the shadow-Lie raising operator `D_𝔔` forces an infinite even-degree tail when `S_4 ≠ 0` at [17965](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17965). Literature cross-check: no direct published analogue found; this looks manuscript-internal. Confidence: `high`.
- Heisenberg `d_alg=0`: primary witness is [heisenberg_eisenstein.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:1526). Alternative proof is computational: Swiss-cheese `m_3=m_4=0`. Literature cross-check: none direct. Confidence: `high`.
- Affine `\widehat{sl}_2` `d_alg=1`: primary witness is the Jacobi quartic-vanishing proposition at [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:4913). Alternative proof is computational: Swiss-cheese class `L`, `S_4=0`, depth `3`. Literature cross-check: classical Jacobi mechanism is consistent, but I did not find a published depth-gap theorem. Confidence: `high`.
- `βγ` `d_alg=2`: primary witness is the global depth theorem at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1182), with the global-contact summary reused in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17931). Alternative proof is computational: Swiss-cheese `m_3=0`, `m_4≠0`, and the `λ=0` edge engine still gives depth `4`. Literature cross-check: no direct published analogue found; this lane appears manuscript-internal. Confidence: `medium-high`.
- Virasoro `d_alg=∞`: primary witness is [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:3188), reinforced by the Riccati lane at [17960](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17960). Alternative proof is computational: Swiss-cheese `m_3≠0` and infinite shadow-depth. Literature cross-check: framework confirmed, direct trichotomy theorem not found. Confidence: `high`.

**Verification**
- Exact recursion sanity check from the manuscript formula: with `(κ,α,S_4)=(1,2,3)`, the recursion gives `S_5=-36/5`; with `(1,0,3)`, it gives `S_5=0`, `S_6=-6`. This matches the written non-cancellation split.
- Tests passed:
  - `python3 -m pytest compute/tests/test_depth_classification.py` → `132 passed`
  - `python3 -m pytest compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseHeisenbergM3::test_heisenberg_class_G compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseAffineSl2::test_class_L compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseBetagamma::test_class_C compute/tests/test_theorem_ainfty_nonformality_class_m_engine.py::TestSwissCheeseVirasoroM3::test_virasoro_shadow_depth_infinite` → `4 passed`
  - `python3 -m pytest compute/tests/test_betagamma_shadow_full.py::TestEdgeCases::test_lambda_0_weight_0_generator` → `1 passed`
- AP grep on the modified compute files found no `AP126`, `AP132`, `AP29`, or `AP165` hits.
- Framework literature checked:
  - [Francis–Gaitsgory, *Chiral Koszul Duality*, Thm. 1.2.4](https://sites.math.northwestern.edu/~jnkf/writ/chiral.pdf): explicitly presented as a generalization of BD04 Thm. 3.4.9 and a conceptual proof of BD04 Thm. 4.8.1.1. Convention check: chiral/factorization objects are coalgebraic, matching the repo’s bar-side discipline.
  - [Lurie, *Higher Algebra*, Thm. 5.3.1.14 and Cor. 5.3.1.15](https://www.math.ias.edu/~lurie/papers/HA.pdf): centralizers exist, and the `E_k` center carries `E_{k+1}` structure. Convention check: this supports the derived-center lane, not SC-structure on the bar complex.
  - [PTVV, *Shifted Symplectic Structures*, Thm. 0.4 / 2.5](https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf): mapping stacks inherit shifted symplectic forms from oriented sources. Convention check: relevant to the complementarity/derived-center output, not to the `d_alg` gap proof itself.
  - `CG`, `CFG`, and `Costello-Li`: not checked to theorem-number granularity in this turn, and I did not find a direct published theorem there matching the depth-gap trichotomy.
file update:
diff --git a/compute/lib/depth_classification.py b/compute/lib/depth_classification.py
index 4423c21ef1b926e4dda7e88bbc0438e3a9690715..7f5229ca325e7f34841347523281da9416514680
--- a/compute/lib/depth_classification.py
+++ b/compute/lib/depth_classification.py
@@ -463,28 +463,12 @@
     Classification requires stratum separation (rem:contact-stratum-separation).
 
     For lambda = 0 or 1 (standard): kappa = 1, class C, r_max = 4.
-    For lambda = 1/2 (symplectic): kappa = -1/2, degenerate considerations.
-    For lambda = 0: weight-0 generator, violates positive grading (AP18).
+    For lambda = 1/2 (symplectic): kappa = -1/2, still class C.
+    For lambda = 0: the weight-0 generator triggers the AP18 warning,
+    but the global quartic/contact witness still gives class C.
     """
     w = Rational(weight)
     kap = kappa_betagamma(weight)
-    degen = (kap == 0)
-
-    if w == 0:
-        return DepthClassification(
-            name='betagamma (lambda=0)',
-            kappa=kap,
-            alpha=Rational(0),
-            S4=Rational(0),
-            delta=Rational(0),
-            depth_class='G',
-            r_max=2,
-            d_alg=0,
-            d_arith=0,
-            d_total=1,
-            degenerate=True,
-            notes='Weight-0 generator violates positive grading (AP18). kappa=1 but degenerate.',
-        )
 
     # For the contact classification, we use the fact that the quartic
     # contact invariant lives on a charged stratum with alpha = 0 but S_4 != 0.
@@ -501,7 +485,13 @@
         d_alg=2,
         d_arith=1,
         d_total=4,
-        notes=f'Stratum separation: alpha=0 on weight-changing line, quartic on charged stratum.',
+        degenerate=(w == 0),
+        notes=(
+            'Stratum separation: alpha=0 on the weight-changing line, '
+            'quartic on the charged stratum. '
+            'At lambda=0 the weight-0 generator triggers AP18, but the '
+            'global depth remains class C.'
+        ),
     )
 
 
diff --git a/compute/tests/test_depth_classification.py b/compute/tests/test_depth_classification.py
index 7514a968840731e55c0f68e1c63e07cc7ed3bc5d..7911fbfe33ef927410b98952a49c741f5ad4d3c2
--- a/compute/tests/test_depth_classification.py
+++ b/compute/tests/test_depth_classification.py
@@ -159,9 +159,11 @@
         assert a.depth_class == 'C'
         assert a.r_max == 4
 
-    def test_betagamma_lam0_degenerate(self):
+    def test_betagamma_lam0_is_class_C_but_flagged(self):
         a = classify_betagamma(0)
-        assert a.depth_class == 'G'
+        assert a.depth_class == 'C'
+        assert a.r_max == 4
+        assert a.d_alg == 2
         assert a.degenerate
 
     def test_virasoro_is_M(self):
@@ -612,6 +614,8 @@
         a = classify_betagamma(0)
         assert a.degenerate
         assert a.kappa == 1  # formula gives kappa=1 even for lambda=0
+        assert a.depth_class == 'C'
+        assert a.d_alg == 2
 
     def test_ap31_kappa_zero_not_theta_zero(self):
         """AP31: kappa = 0 does NOT imply Theta_A = 0.
@@ -704,13 +708,13 @@
         counts = {'G': 0, 'L': 0, 'C': 0, 'M': 0}
         for a in algebras:
             counts[a.depth_class] += 1
-        # Expected: G=7 (Heis, Heis_0, fermion, D4, E8, Leech, bg_lam0)
+        # Expected: G=6 (Heis, Heis_0, fermion, D4, E8, Leech)
         #           L=4 (sl2, sl3, G2, E8 affine)
-        #           C=2 (bg_lam1, bg_lam_half)
+        #           C=3 (bg_lam0, bg_lam1, bg_lam_half)
         #           M=7 (Vir_1, Vir_0, Vir_26, W3_50, W4_50, W3_2, W_inf)
-        assert counts['G'] == 7
+        assert counts['G'] == 6
         assert counts['L'] == 4
-        assert counts['C'] == 2
+        assert counts['C'] == 3
         assert counts['M'] == 7
 
     def test_no_class_G_has_infinite_depth(self, algebras):

tokens used
463,055
