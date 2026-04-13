# C11_kappa_xvol_consistency (485s)

**Findings**

- PROBLEM at [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1919): the proof used the full affine KM symbol `\kappa(\widehat{\mathfrak g}_k)` for the double-pole contribution `\dim(\mathfrak g)k/(2h^\vee)`, then added the Sugawara term on the next line. That drops the required shift at the point of first assertion. EXACT edit applied: changed the first term to `\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k) = \dim(\mathfrak g)\cdot k/(2h^\vee)` and rewrote the sum as `\kappa(\widehat{\mathfrak g}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k) + \dim(\mathfrak g)/2 = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`.

- PROBLEM at [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130) and [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168): Vol III states the `\mathcal W_N` complementarity sum as `c(H_N - 1)`. For the sum, the canonical quantity is `(c+c')(H_N - 1) = K_N(H_N - 1)`. EXACT edit applied: not applied; sandbox blocks writes outside `/Users/raeez/chiral-bar-cobar`. Required edit is to replace `c \cdot (H_N - 1)` with `(c+c') \cdot (H_N - 1)` or `K_N \cdot (H_N - 1)` in both sentences.

- PROBLEM at [cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:909) and [bar_cobar_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80): Vol III introduces per-channel modular characteristics as `\kappa_s` and `\kappa_s^{\mathrm{eff}}`. That drifts from AP113’s Vol III `\kappa_{\mathrm{ch}}/\kappa_{\mathrm{cat}}/\kappa_{\mathrm{BKM}}/\kappa_{\mathrm{fiber}}` namespace. EXACT edit applied: not applied; sandbox blocks writes outside `/Users/raeez/chiral-bar-cobar`. Required edit is to rewrite these as contributions to `\kappa_{\mathrm{ch}}`, e.g. “the spin-`s` contribution to `\kappa_{\mathrm{ch}}` is `1/s`,” instead of introducing `\kappa_s`.

Vol II explicit family surfaces checked clean against the census; no edit was needed at [preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:977), [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1302), and [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1968).

**Verification**

Negative grep after the patch found no remaining Vol I full-KM dropped-shift hit, and no `\mathcal W_N` formula hit using `H_{N-1}` across the three volumes. I did not run a TeX build.


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
session id: 019d87b8-dffc-7953-b53f-1d9061cbe1e0
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


Cross-volume kappa formula consistency.
For each family: grep all three volumes for kappa formulas.
Verify each matches the canonical census. Especially check:
kappa(KM) includes Sugawara shift, kappa(W_N) uses H_N-1 not H_{N-1},
Vol III has subscripts (AP113). Fix inconsistencies.
mcp startup: no servers

thinking
**Planning workflow updates**

I need to access the skill documentation to follow the workflow correctly. I should start by providing a commentary update to acknowledge the process and detail the first steps. If there are substantial changes, I might also need to update the plan. Additionally, it seems likely I'll be using multi_tool_use.parallel to read files concurrently. Let's get started with that commentary!
codex
Cross-volume `\kappa` surfaces are the audit target. I’m loading the required constitutional files and the relevant skills first, then I’ll grep all three volumes for live formulas before touching anything.
exec
/bin/zsh -lc "sed -n '1,240p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
**Updating search strategy**

I need to update my plan and inspect cross-volume grep for kappa formulas across three volumes. I should identify specific files, like landscape_census.tex, and use rg for searching. Grepping for patterns related to kappa (KM), H_N, and any subscript issues could be essential. It seems I should use explorer subagents for codebase questions since this is a textual math repository, and ask them precisely for efficient searching. Spawning explorer agents for these tasks sounds like the best approach.
thinking
**Planning explorer agents**

I’m considering using parallel explorer agents for Volumes I, II, and III, but I’m not sure, maybe they can only access the current repo. I want to trust the results, but exec_command is also an option. The instructions say to prefer explorers over manual searches, which is good since I've already read some files for AGENTS. 

To be thorough, I think of using multiple explorers: one to map kappa formulas across all volumes, another focused on Volume III, and perhaps one for landscape_census/formulas. That should help me stay organized!
codex
I’ve loaded the constitutional layer and the two required skills: `multi-path-verify` for the formula checks and `cross-volume-propagation` for the duplicate sweep. Next I’m mapping every live `\kappa` formula in Vol I, Vol II, and Vol III, with special attention to KM, `W_N`, and bare Vol III notation.
collab spawn_agent(call_JDM9YIhTVhryDV8eh1iggewe, prompt="Search across /Users/raeez/calabi-yau-quantum-groups for live TeX occurrences of kappa formulas and bare \kappa usage. F…")
mcp startup: no servers
spawn_agent(call_JDM9YIhTVhryDV8eh1iggewe, prompt="Search across /Users/raeez/calabi-yau-quantum-groups for live TeX occurrences of kappa formulas and bare \kappa usage. F…") pending init:
  agent: 019d87b9-6cc4-71e0-9720-3e44ceb5341a
collab spawn_agent(call_LllUJSpJa40VVBIl0QdUXrEq, prompt="Search across /Users/raeez/chiral-bar-cobar and /Users/raeez/chiral-bar-cobar-vol2 for live TeX occurrences of kappa for…")
mcp startup: no servers
spawn_agent(call_LllUJSpJa40VVBIl0QdUXrEq, prompt="Search across /Users/raeez/chiral-bar-cobar and /Users/raeez/chiral-bar-cobar-vol2 for live TeX occurrences of kappa for…") pending init:
  agent: 019d87b9-6cc8-7451-8e4f-96b80f90b887
collab spawn_agent(call_S8PqvHcEFGVt8D8kZqMjsxyN, prompt="Read the canonical kappa formulas from /Users/raeez/chiral-bar-cobar/chapters/connections/landscape_census.tex and repor…")
mcp startup: no servers
spawn_agent(call_S8PqvHcEFGVt8D8kZqMjsxyN, prompt="Read the canonical kappa formulas from /Users/raeez/chiral-bar-cobar/chapters/connections/landscape_census.tex and repor…") pending init:
  agent: 019d87b9-6cdf-7663-a4a2-cca693f6ba86
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "kappa" --glob "*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 9184

working_notes_frontier_2026_04.tex:57:the genus expansion $F_g = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$
working_notes_frontier_2026_04.tex:84:$m_0 = \kappa(\cA) \cdot \omega_g$ from the Kodaira--Spencer
working_notes_frontier_2026_04.tex:93:= Q^{\mathrm{contact}} \cdot \frac{\kappa}{\mathrm{Im}(\tau)}
working_notes_frontier_2026_04.tex:133:$P_{\mathrm{harm}} = m_0/\kappa$ gives
working_notes_frontier_2026_04.tex:134:$\delta_4 = (Q^{\mathrm{contact}}/\kappa) \cdot m_0$.
working_notes_frontier_2026_04.tex:158:complex satisfies $d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$,
working_notes_frontier_2026_04.tex:187:genus expansion $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
working_notes_frontier_2026_04.tex:248:= \kappa(\cW_N) \cdot \lambda_g^{\mathrm{FP}}
working_notes_frontier_2026_04.tex:464:algebras with identical $\kappa$ but different higher-genus
main.tex:501:\newcommand{\dfib}{d_{\mathrm{fib}}} % fiberwise differential on fixed Sigma_g (CURVED: d^2 = kappa * omega_g)
main.tex:752:$\kappa(\cA) + \kappa(\cA^!) = K(\cA)$;
main.tex:754:$F_g = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}$
main.tex:932: The modular characteristic $\kappa(\cA)$ is universal, additive,
main.tex:944:But $\kappa(\cA)$ is only the \emph{linear} leading term.
main.tex:947:$\kappa \to \Delta \to \mathfrak{C} \to \mathfrak{Q} \to \cdots$,
main.tex:1076:% obstruction tower kappa -> Delta -> [C] -> o^(r) -> Theta. The
main.tex:1087:The modular characteristic~$\kappa(\cA) = \mathrm{av}(r(z))$ is the
main.tex:1095:$\kappa \to \Delta \to \mathfrak{C} \to \mathfrak{Q} \to \cdots$,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg --glob '*.tex' -n '\\\\kappa' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1508

/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:590:\subsubsection{(b) The modular anomaly from $\kappa_{\mathrm{ch}}(A_X)$}
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:592:In Volume~I, the modular characteristic $\kappa_{\mathrm{ch}}(A)$ of a chiral algebra
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:593:$A$ controls the genus-$g$ obstruction: $d_B^2 = \kappa_{\mathrm{ch}}(A) \cdot \omega_g$
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:595:$\kappa_{\mathrm{ch}}(A_X)$ equals the weight of the automorphic form (e.g., $\kappa_{\mathrm{BKM}} = 5$
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:612:$\kappa_{\mathrm{ch}}$ (degree 2, quadratic) & $\frac{1}{2}\sum_{\alpha \in \Delta_+^{\mathrm{re}}} \alpha$ \\
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:651:the bilinear form $\kappa_{\mathrm{ch}}$ on the Lie${}^*$-algebra $L_X$, restricted to
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:728:modular anomaly $\kappa_{\mathrm{ch}}(A_X)$ and the shadow obstruction tower $\Theta_{A_X}$, equals
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:757:\item Modular characteristic: $\kappa_{\mathrm{BKM}}(K3 \times E) = 5$ (the weight of $\Delta_5$; the single-copy chiral value is $\kappa_{\mathrm{ch}} = 3$).
/Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex:937: the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A_X) \cdot \omega_g$, and the
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:38:\title{Anomaly Cancellation and the Modular Characteristic $\kappa_{\mathrm{ch}}$\\
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:48:characteristic $\kappa_{\mathrm{ch}}$ for quantum vertex chiral groups $G(X)$ associated
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:49:to Calabi--Yau threefolds $X$. In Volume~I, $\kappa_{\mathrm{ch}}(\mathcal{A})$ is the
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:51:$\mathrm{obs}_g = \kappa_{\mathrm{ch}}(\mathcal{A}) \cdot \lambda_g$. For $G(X)$, the quantity
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:52:$\kappa_{\mathrm{ch}}$ acquires direct geometric and physical meaning through the
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:55:We examine four aspects: (1) the K3$\times E$ case where $\kappa_{\mathrm{BKM}} = 5$
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:59:case where the Heisenberg subalgebra of $W_{1+\infty}$ at self-dual level $c = 1$ gives $\kappa_{\mathrm{ch}}(\mathcal{H}_1) = 1$ (the Virasoro channel alone gives $\kappa_T = c/2 = 1/2$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty})$ diverges);
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:60:(3) the complementarity formula $\kappa_{\mathrm{ch}}(G(X)) + \kappa_{\mathrm{ch}}(G(X)^!)$ and its
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:62:$\kappa_{\mathrm{ch}} = \chi(X)/24$ (Heisenberg prediction) and
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

thinking
**Searching for data effectively**

I'm considering using a manual grep to get comprehensive results, as we need to ensure trust in what we find. It might be helpful to execute a command to perform an accurate grep ourselves. The system indicates we should read the exact files we interact with, but I haven't pinpointed those yet. I think I’ll use rg and check the git status to identify changes, gathering exact line numbers and leveraging the workspace path to volumes II and III.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg --pcre2 -n '\\\\kappa(?"'!_)'"' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:65:ZERO TOLERANCE in Vol III. Before writing ANY `\kappa`:
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_cy_to_chiral_wave13.md:27:Grep of `\kappa` across all 1547 lines: **every occurrence is subscripted.** Scanned 43 hits across lines {4, 43, 207, 236, 338, 368, 481, 536, 539, 543-549, 555-557, 630, 683, 787-788, 1127-1139, 1156, 1163, 1192, 1205, 1246-1249, 1276, 1285-1309, 1324-1341, 1367, 1430-1432, 1471-1473, 1483-1497, 1510-1519}. All subscripts: `\kappa_{\mathrm{ch}}` (dominant), `\kappa_{\mathrm{BKM}}`, `\kappa_{\mathrm{BCOV}}`, `\kappa_{\mathrm{MacMahon}}`. Zero bare `\kappa`. **Wave 9-9 is clean.** The polysemy remark (line 1510-1520) explicitly disambiguates the four roles, consistent with Vol III kappa-spectrum mandate.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:61:- **F-m2 (line 112-115 spectrum.** `\operatorname{Spec}_{\kappa}(X) = \{2, 3, 5, 24\}` -- check CLAUDE.md's enumeration (identical: 2=cat, 3=ch, 5=BKM, 24=fiber). Matches. No issue.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:180:- **C-S2 (AP113, kappa subscripts).** Count: I find kappa_ch (lines 28, 84, 93, 108 implicit, 113), kappa_BKM (85, 94, 113), kappa_cat (111, 119), kappa_fiber (115). I do NOT find any BARE kappa. GOOD. AP113 compliance is PASSING in the preface. Line 106 writes "$\kappa$-mismatch" (bare kappa in the phrase "kappa-mismatch") -- but this is describing the SPECTRUM, not identifying a specific kappa. Borderline; in the same sentence kappa_ch and kappa_BKM are both named, so the phrase is scoping. Accept. Line 106 also writes "$\operatorname{Spec}_\kappa(X)$" (bare kappa subscript on Spec), which is naming the spectrum as a whole, not a specific kappa. Accept. Overall AP113 PASS.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:410:Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:423: on $(\C^2)^{\otimes 4}$ is \emph{not} satisfied. The obstruction scales as $O(\kappa^2)$ and is antisymmetric.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:424: \item At $\kappa = 0$ (the permutation limit, $R(z) = P$), the ZTE is trivially satisfied (Kapranov--Voevodsky).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:429:Parts~(i) and~(iii) are verified symbolically and numerically. Part~(ii) is computed by explicit matrix multiplication on the charge-$2$ sector of $(\C^2)^{\otimes 4}$ (dimension~$6$): the difference $\mathrm{LHS} - \mathrm{RHS}$ is nonzero at $O(\kappa^2)$, verified at multiple spectral parameter values and confirmed by symbolic expansion in $\kappa$. See \texttt{compute/lib/zamolodchikov\_tetrahedron\_engine.py} ($34$ tests).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex:557:relevant for fibered CY manifolds). Bare $\kappa$ without
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:2188: \item The MacMahon exponent (sometimes written $\kappa_{\mathrm{ch}}$ in the MNOP formula $Z_{\DT,0} = M(-q)^{\chi(X)}$): the exponent $\chi_{\mathrm{top}}(X)$ in the degree-zero DT partition function. Equals $\chi_{\mathrm{top}}(S)/2$ for $\mathrm{Tot}(K_S)$. This is NOT a modular characteristic; it is the topological Euler characteristic, and must not be given a $\kappa$ subscript.
/Users/raeez/calabi-yau-quantum-groups/notes/audit_red8_wall_crossing.md:163:(b) Replace or qualify the RG analogy. In the RG analogy, scheme independence holds because the beta function is universal at leading order. Here, there is no analogue: the leading-order truncation ($\kappa$, the modular characteristic) is gauge-invariant, but the first correction (the cubic shadow $C$) is already discontinuous. The analogy would require $\Theta^{\leq r}_A$ to be "approximately" gauge-invariant for large $r$, with errors decreasing as $r$ increases. Is this true? If so, state and prove it. If not, the analogy fails.
/Users/raeez/calabi-yau-quantum-groups/notes/audit_red8_wall_crossing.md:210:But $\Theta^{\leq 2}_A$ is the *arity-2* truncation, identified with the modular characteristic $\kappa$ in Section 6.1. The charge $\gamma_1 + \gamma_2$ is a *composite* charge with two constituents -- this is an arity-2 datum (it takes two BPS particles to form it). So the jump of $\Omega(\gamma_1 + \gamma_2)$ *is* a jump at arity 2, and $\Theta^{\leq 2}_A$ should indeed see it.
/Users/raeez/calabi-yau-quantum-groups/notes/audit_red8_wall_crossing.md:212:The confusion is that the example seems to equate "arity" with "number of constituents in a bound state," but the shadow obstruction tower arity decomposition (eq. 6.1) is indexed by the moduli space $\overline{\mathcal{M}}_{g,n}$ -- arity $r$ means $n = r$ marked points. The relationship between "number of BPS constituents" and "number of marked points on a curve" is not explained in the note. If a 2-center bound state corresponds to arity 2, then yes, $\Theta^{\leq 2}_A$ jumps. But the claim in Section 6.1 is that $\Theta^{\leq 2}_A = \kappa$, the modular characteristic -- which is a tree-level (genus-zero) datum that should NOT depend on bound state formation.
/Users/raeez/calabi-yau-quantum-groups/notes/audit_red8_wall_crossing.md:214:Either the identification $\Theta^{\leq 2}_A = \kappa$ is wrong, or the example is wrong. They are inconsistent.
/Users/raeez/calabi-yau-quantum-groups/notes/audit_red8_wall_crossing.md:218:Clarify the relationship between arity and BPS constituents. If the arity-$r$ piece of $\Theta_A$ encodes $r$-center BPS states, then $\Theta^{\leq 2}_A \neq \kappa$ (it also includes 2-center data). If $\Theta^{\leq 2}_A = \kappa$, then the conifold jump must appear at arity 3 or higher, and the example must be corrected.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3459:JT uses $\kappa$-class intersections (Weil--Petersson
/Users/raeez/calabi-yau-quantum-groups/notes/research_lattice_voa_ktheory.md:95:- $\Theta^{\leq 2}$: $\kappa(\mathcal{W}_{1+\infty})$ and the Heisenberg OPE.
/Users/raeez/calabi-yau-quantum-groups/notes/research_lattice_voa_ktheory.md:141:$\kappa(A_X)$ and the Weyl vector $\rho$.
/Users/raeez/calabi-yau-quantum-groups/notes/research_lattice_voa_ktheory.md:200:$\Delta = 8\kappa S_4 = 0$ (Gaussian class in the taxonomy of Vol I).
/Users/raeez/calabi-yau-quantum-groups/notes/research_lattice_voa_ktheory.md:278:| 2 | Binary bar differential $d_2$ (binary OPE) | $\Theta^{\leq 2}$ (modular char. $\kappa$) |
exec
/bin/zsh -lc 'rg -n "kappa" chapters/connections/landscape_census.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: chapters/connections/landscape_census.tex: IO error for operation on chapters/connections/landscape_census.tex: No such file or directory (os error 2)
exec
/bin/zsh -lc 'ls chapters' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
connections
examples
frame
theory
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '400,450p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
At the level of quantum toroidal algebras, the $E_3$ Koszul duality of Conjecture~\ref{conj:e3-koszul-duality}(ii) predicts the parameter-inversion symmetry
\[
 U_{q,t}(\widehat{\widehat{\fgl}}_1)^! \;\simeq\; U_{q^{-1}, t^{-1}}(\widehat{\widehat{\fgl}}_1),
\]
which is the conjectural Koszul duality of Chapter~\ref{ch:quantum-groups} (Definition~\ref{def:qgf-four-regimes}, toroidal regime). The $E_3$ framework provides the geometric origin of this parameter inversion: it is the Verdier duality on $\C^3$ factorization coalgebras.
\end{remark}

\begin{theorem}[The Zamolodchikov tetrahedron equation fails for the Yang $R$-matrix]
\label{thm:zte-failure}
\ClaimStatusProvedHere{}
Let $R(z) = (z \cdot \mathrm{Id} + \kappa \cdot P)/(z + \kappa)$ be the Yang $R$-matrix on $\C^2 \otimes \C^2$ with $\kappa = h_1 h_2 h_3$, and define the $3$-particle $S$-operator
\[
 S_{ijk}(u_i, u_j, u_k) \;=\; R_{ij}(u_i - u_j) \, R_{ik}(u_i - u_k) \, R_{jk}(u_j - u_k)
\]
acting on $(\C^2)^{\otimes 3}$. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item The Yang--Baxter equation $R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}$ is satisfied (positive control).
 \item The Zamolodchikov tetrahedron equation
 \[
  S_{012} \, S_{013} \, S_{023} \, S_{123}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"kappa\\\\(\\\\cH\" --glob \"*.tex\"" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:kappa\(\cH)
              ^^
error: unrecognized escape sequence
codex
The search surface is wide enough that I’m doing it in parallel: explorers are cataloguing the live formula claims while I run a direct grep pass for the exact edit surface and line references. After that I’ll decide the minimum truthful patch set.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' '\\\\kappa|kappa\\(' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 269

 M AGENTS.md
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
 M appendices/nonlinear_modular_shadows.tex
 M appendices/ordered_associative_chiral_kd.tex
 M appendices/spectral_higher_genus.tex
 M bibliography/references.tex
 M bp_self_duality.pdf
 M chapters/connections/arithmetic_shadows.tex
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'H_\\{N-1\\}|H_N - 1|H_N-1|dim\\(\\\\fg\\)\\(k\\+h\\"'^'"\\\\vee\\)/(2h\\"'^'"\\\\vee)|dim\\(g\\)\\(k\\+h\\"'^v'"\\)/(2h\\"'^v)|dim'"\\(\\\\fg\\)k/(2h\\"'^'"\\\\vee)|dim\\(g\\)k/(2h\\"'^v)'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 5002

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:38:kappa(K3 x E) = 3 vs 5 contradiction arose from conflating kappa_ch and kappa_BKM. Full spectrum: {2,3,5,24}.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:65:ZERO TOLERANCE in Vol III. Before writing ANY `\kappa`:
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:72:     write \kappa_\bullet to satisfy the grep regex (the bullet denotes
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:77:- chiral algebra A_C / Phi(C) -> `\kappa_{\mathrm{ch}}`
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:78:- Borcherds-Kac-Moody / Igusa weight -> `\kappa_{\mathrm{BKM}}`
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:79:- Holomorphic Euler char chi(O_X) -> `\kappa_{\mathrm{cat}}`
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:80:- Lattice rank / fiber structure -> `\kappa_{\mathrm{fiber}}`
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:143:Birational flop X -> X^+ is a derived equivalence; it PRESERVES kappa_ch. Koszul dual A -> A^! has `kappa(A) + kappa(A^!) = K` (family-dependent conductor). Forbidden conflations:
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:147:"kappa(A_X) + kappa(A_{X^+}) = 0"  WRONG (flops preserve kappa)
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:148:"kappa(A_X) = kappa(A_{X^+})"      RIGHT (flop is autoequivalence)
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:196:AP-CY10: Flop != Koszul dual. Birational flop X->X^+ is derived equivalence PRESERVING kappa. Koszul dual A^! has kappa(A)+kappa(A^!)=rho_K. Flop exchanges chambers; Koszul exchanges algebra/coalgebra. kappa(A_X)=kappa(A_{X+}) for flop, NOT kappa(A_X)+kappa(A_{X+})=0.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:646:- Never write `kappa(K3 x E) = 5` unqualified.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:662:kappa(H_k) = k
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:663:kappa(Vir_c) = c/2
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:664:kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:665:kappa(W_N) = c*(H_N - 1),  H_N = sum_{j=1}^N 1/j
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:719:kappa(K3 x E) = 5                     # unqualified Vol III kappa
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:58:At genus `g >= 1`, the curved structure is essential: the non-vanishing of higher `A_infinity` operations is the curved bar structure `d^2 = kappa(A) * omega_g`. Formality fails because the logarithm acquires monodromy.
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:110:% W_N kappa formula: kappa_ch(W_N^k) = c(W_N^k) * (H_N - 1) where
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:120:$\mathcal{W}_N^k$ ($\mathfrak{sl}_N$) & $c$ & $c(H_N - 1)$ &
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:121: $H_N - 1 = \sum_{j=1}^{N-1} 1/(j+1)$ \\
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:167:$\mathcal{W}_N^k$ & $(H_N - 1) K_N / 2$ & $K_N$
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:333: \kappa_{\mathrm{ch}}(\mathcal{W}_N) = c \cdot (H_N - 1),
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:336:As $N \to \infty$, $H_N - 1 \sim \log N + \gamma - 1$ diverges, and
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:570: $\varrho = H_N - 1 \to \infty$. The formulas disagree for the
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:250:Here $K_N = 4N^3 - 2N - 2$ and $\varrho_N = c \cdot (H_N - 1)/ c =
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:251:H_N - 1$ where $H_N = \sum_{i=1}^N 1/i$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:633:$K_N/c^*_N = 2(H_N - 1)$ equals~$1$ only at $N = 2$ (where
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:840:Here $K_{\mathcal{W}_N} = \kappa + \kappa^! = (H_N - 1)\alpha_N$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:856:\;=\; (H_N - 1)\,\alpha_N,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:860:$K_N/c_N^* = 2(H_N - 1)$ equals~$1$ if and only if $N = 2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:867:$\kappa(\mathcal{W}_{N,c}) = c\,(H_N - 1)$, where $H_N - 1
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:872:$\kappa(\mathcal{W}_{N,\alpha_N - c}) = (\alpha_N - c)(H_N - 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:873:The sum is $K_N = \alpha_N(H_N - 1)$, independent of~$c$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:874:The ratio $K_N/c_N^* = 2(H_N - 1) = 1$ iff $H_N = 3/2$, which
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:896:the curvature $\kappa(\cW_{N,c^*}) = c^*(H_N - 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:897:= \tfrac{1}{2}\alpha_N(H_N - 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1240:= (H_N - 1) \cdot \alpha_N$, where $H_N = \sum_{j=1}^N 1/j$
exec
/bin/zsh -lc "rg -n --glob '*.tex' '(bare kappa|kappa_ch|kappa_cat|kappa_BKM|kappa_fiber|\\\\kappa_[A-Za-z]+|\\\\kappa\\b)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/main.tex:381:Bare~$\kappa$ is forbidden; the subscript records the
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:1143:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2694:% RECTIFICATION-FLAG: The value kappa_ch = 3 is asserted but not derived from
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2699:% structure. The decomposition 5 = 3 + 2 is numerically correct if kappa_ch = 3
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2700:% is accepted, but the derivation of kappa_ch = 3 is missing.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2715:% PROMOTE-TO-MANUSCRIPT: CONJECTURAL. The decomposition kappa_BPS = kappa_ch + chi(O_S) for
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2716:% CY3 = S x E requires an independent derivation of kappa_ch. For K3 x E: kappa_ch = 3
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2718:% For Enriques x E: kappa_BPS = 4 and chi(O_{Enr}) = 1, so kappa_ch(Enr) = 3.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:2719:% Before promoting: derive kappa_ch from the CDR bar complex independently.
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3459:JT uses $\kappa$-class intersections (Weil--Petersson
/Users/raeez/calabi-yau-quantum-groups/notes/theory_6d_hcs_chiral_qg.tex:145:%         kappa_ch(A^{orb}) = 2 (already matching smooth K3).
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:57:% The finite quantity is the Heisenberg subalgebra's kappa_ch = c = 1.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:59:case where the Heisenberg subalgebra of $W_{1+\infty}$ at self-dual level $c = 1$ gives $\kappa_{\mathrm{ch}}(\mathcal{H}_1) = 1$ (the Virasoro channel alone gives $\kappa_T = c/2 = 1/2$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty})$ diverges);
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:109:% Heisenberg rank d level 1: c = d, kappa_ch = d, rho = 1.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:110:% W_N kappa formula: kappa_ch(W_N^k) = c(W_N^k) * (H_N - 1) where
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:339:$\kappa_j = c/j$ for the spin-$j$ generator. The physically
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:347: \kappa_T = \frac{1}{2}, \quad
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:351:The stress-energy channel alone gives $\kappa_T = c/2 = 1/2$.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:364:The finite and well-defined quantity is $\kappa_T = c/2$. For
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:365:$c = 1$, $\kappa_T = 1/2$. This is the modular characteristic of
exec
/bin/zsh -lc 'ls chapters/connections' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
arithmetic_shadows.tex
bv_brst.tex
concordance.tex
editorial_constitution.tex
entanglement_modular_koszul.tex
feynman_connection.tex
feynman_diagrams.tex
frontier_modular_holography_platonic.tex
genus1_seven_faces.tex
genus_complete.tex
holographic_codes_koszul.tex
holographic_datum_master.tex
master_concordance.tex
outlook.tex
poincare_computations.tex
semistrict_modular_higher_spin_w3.tex
subregular_hook_frontier.tex
thqg_entanglement_programme.tex
thqg_introduction_supplement.tex
thqg_introduction_supplement_body.tex
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'kappa\\\\(\\\\cH' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:kappa\\(\\cH)
    ^
error: unclosed group
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '350,420p' /Users/raeez/calabi-yau-quantum-groups/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
via the Drinfeld center. Steps~(1) and~(2) are unconditional;
step~(3) is conditional on the chain-level
$\mathbb{S}^3$-framing.

For~$\C^3$, the Jordan quiver gives
$\C^3 \to \cW_{1+\infty} \to
\Rep^{\Etwo}(Y(\widehat{\fgl}_1))$:
the critical cohomological Hall algebra $\CoHA(Q)$ is the
$\Eone$-sector, and the Drinfeld center recovers the full
braided structure. For a general toric $\CY_3$ with
fan~$\Sigma$, quiver charts indexed by Bridgeland stability
chambers give local chiral algebras; wall-crossing is
conjecturally Maurer--Cartan gauge equivalence with the global
chiral algebra as homotopy colimit. When~$\Phi$ exists,
the Borcherds--Kac--Moody denominator identity equals the bar
Euler product.

The prototype $K3 \times E$ reveals that a single $\CY_3$
admits multiple chiral algebraizations with distinct modular
characteristics. The $\kappa_\bullet$-spectrum
exec
/bin/zsh -lc 'rg -n "landscape_census" -l' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
foundation_audit_chapters_report.md
healing_20260413_132214/SUMMARY.md
AGENTS.md
healing_20260413_132214/H12_complementarity_alt.md
chapters/examples/w_algebras_deep.tex
chapters/examples/lattice_foundations.tex
fix_wave_E_20260413_182434/E04_test_gaps_rmatrix.md
rectification_20260412_233715/R21_standalone_e1_primacy.md
CLAUDE.md
rectification_20260412_233715/R03_higher_genus_foundations.md
healing_20260413_132214/H13_remove_uniform_weight.md
healing_20260413_132214/H33_landscape_census_verify.md
fix_wave_E_20260413_182434/E03_test_gaps_central.md
fix_wave_E_20260413_182434/E05_test_gaps_misc.md
fix_wave_E_20260413_182434/E08_stub_chapters_v1.md
audit_campaign_20260412_230832/F14_averaging.md
wave2_audit_20260413_001942/J22_engine_dolbeault.md
audit_campaign_20260412_230832/F12_MC_equation.md
healing_20260413_132214/H14_remove_koszul_locus.md
relaunch_20260413_111534/XV07_yangian_xvol.md
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"kappa\\\\(\\\\\\\\cH\" --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
tmp_standalone_audit/survey_v2_xr.tex:448:\mathrm{av}\bigl(r^{\cH}(z)\bigr)=k=\kappa(\cH_k).
tmp_standalone_audit/survey_v2_xr.tex:453:Complementarity (free-field branch, sum $=0$; contrast Virasoro where sum $=13$): $\kappa(\cH_k)+\kappa(\cH_k^!)=k+(-k)=0$.
tmp_standalone_audit/survey_v2_xr.tex:2429:=\kappa(\cH_k)$. Averaging loses nothing. Koszul dual:
tmp_standalone_audit/survey_v2_xr.tex:2433:$\kappa(\cH_k)+\kappa(\cH_k^!)=k+(-k)=0$.
working_notes.tex:7057:$\kappa(\cH_\kappa) = \kappa$.  The Koszul dual is
working_notes.tex:7059:$\kappa(\cH_\kappa^!) = -\kappa$.
tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:253:$\kappa(\cH_k) = k$, $\kappa(\cH_k^!) = -k$,
tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:254:$\kappa(\cH_k) + \kappa(\cH_k^!) = 0$ (the free-field/KM
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:253:$\kappa(\cH_k) = k$, $\kappa(\cH_k^!) = -k$,
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:254:$\kappa(\cH_k) + \kappa(\cH_k^!) = 0$ (the free-field/KM
standalone/N3_e1_primacy.tex:497:\item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
appendices/ordered_associative_chiral_kd.tex:2066:$\kappa(\cH_k)=k$ of the Vol.~I landscape census.
appendices/ordered_associative_chiral_kd.tex:2161:genus-zero datum $\kappa(\cH_k)=k$.
chapters/examples/heisenberg_eisenstein.tex:23:\textbf{Modular characteristic} & $\kappa(\cH_\kappa) = \kappa$ \\
chapters/examples/heisenberg_eisenstein.tex:25:$\kappa(\cH_\kappa^!) = -\kappa$ \\
chapters/examples/heisenberg_eisenstein.tex:307:it has modular characteristic $\kappa(\cH_\kappa^!) = -\kappa$, giving
standalone/programme_summary.tex:513:\kappa(\cH_k)\,.
standalone/programme_summary.tex:620:\kappa(\cH_k) = k\,,
standalone/sc_chtop_pva_descent.tex:1253:The modular characteristic is $\kappa(\cH_k) = k$: the same
chapters/connections/thqg_introduction_supplement_body.tex:766: weighted by spin: $\kappa(\cH_k) = k$ for bosons,
exec
/bin/zsh -lc 'find . -name landscape_census.tex -print' in /Users/raeez/chiral-bar-cobar succeeded in 302ms:
./chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a074cd40/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ab4d244b/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a7a899b6/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ad4860d3/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-abc99e5a/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ab0fb328/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a618b30c/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a35dd0a7/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ae5ffa93/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a6b91d46/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a001fc1b/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a716d31f/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a78e4d88/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a7c35613/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a506436b/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a6d629eb/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/chapters/examples/landscape_census.tex

thinking
**Narrowing grep output**

I have a huge grep output with lots of notes, so I need to narrow it down to just live surfaces, possibly from chapters and standalones. The user asked for kappa formulas from all three volumes, and I’m thinking we should focus on live TeX in the chapters plus any main standalones. It feels vital to do this exhaustively within the assigned scope, especially checking the kappa formula consistency across volumes, while noting any issues in non-writable volumes.
collab wait(call_uXJZpdG2P3XZTmyRetV9FphC)
  receivers: 019d87b9-6cc8-7451-8e4f-96b80f90b887, 019d87b9-6cc4-71e0-9720-3e44ceb5341a, 019d87b9-6cdf-7663-a4a2-cca693f6ba86

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'kappa\\\\(\\\\cH_k\\\\) = ["'^k]*k/2'"' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
     1	\chapter*{Summary of Part IV}
     2	\label{ch:landscape-census}
     3	\addcontentsline{toc}{chapter}{Summary of Part IV}
     4	
     5	The complementarity sum $c + c' = 2d$ holds for every Kac--Moody
     6	algebra. The universal generating function $x/\sin x$ governs the
     7	$\hat{A}$-genus across all standard families. The spectral
     8	discriminant $\Delta(x) = 1 - 2x - 3x^2$ is shared by
     9	$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$, three
    10	algebras with no apparent algebraic relation. These are the patterns
    11	that organize the landscape, and they are visible only in the census.
    12	
    13	Each chiral algebra in the standard landscape is determined, up to
    14	archetype, by a finite set of shadow invariants: the scalar
    15	$\kappa$, the cubic and quartic shadow coefficients $S_3$ and $S_4$,
    16	and the critical discriminant $\Delta = 8\kappa S_4$. The
    17	vanishing locus of these invariants stratifies the census into the
    18	four archetype classes G/L/C/M, just as electron configuration
    19	stratifies the periodic table into orbital blocks: $S_3 = S_4 = 0$
    20	characterizes Gaussian algebras (class~G), $S_3 \neq 0$ with
thinking
**Organizing kappa usage findings**

I'll gather and classify key live TeX occurrences of kappa formulas, noting canonical versus suspect use—especially highlighting subscripting and bare `\kappa` cases that might violate AP113. I want to focus on main files like `main.tex`, `k3_times_e.tex`, and `physics_anomaly_cancellation`, sampling key lines with precise line numbers and capturing relevant context around each hit for a clear, concise summary.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '70,125p' /Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{Review: the modular characteristic in Volume~I}
\label{sec:review}
%% ====================================================================

We recall the essential structures from Vol~I (Modular Koszul Duality)
that enter the CY quantum group story.

\subsection{The genus tower and $\kappa_{\mathrm{ch}}$}
%: In this note we write $\kappa_{\mathrm{ch}}$ for the modular characteristic
% of a chiral algebra (Vol~I notation: $\kappa_{\mathrm{ch}}$). All kappa in Vol~III subscripted.

For a modular Koszul chiral algebra $\mathcal{A}$, the universal
Maurer--Cartan element
$\Theta_\mathcal{A} \in \mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_\mathcal{A})$
has a scalar projection at degree~2, the \emph{modular characteristic}
$\kappa_{\mathrm{ch}}(\mathcal{A})$, which controls the genus-$g$ obstruction class:
\begin{equation}\label{eq:obs-g}
 \mathrm{obs}_g(\mathcal{A})
 = \kappa_{\mathrm{ch}}(\mathcal{A}) \cdot \lambda_g
 \in H^{2g}(\Mbar_g, \mathbb{Q}),
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "H_{N-1}" chapters/examples/w_algebras_deep.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:H_{N-1})
          ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc 'rg -n "Heisenberg" -n chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
37:\noindent\emph{The Master Table below collects the invariants computed throughout Part~\ref{part:physics-bridges}. For the Heisenberg algebra, these invariants were derived in Chapter~\ref{ch:heisenberg-frame}; for each subsequent algebra, the corresponding chapter provides the complete computation.}
81:\multicolumn{6}{|c|}{\textit{Heisenberg \textup{(}curved abelian\textup{)}}} \\
83:Heisenberg $\mathcal{H}_\kappa$
197:$\operatorname{ek} = 0$ for Heisenberg, affine $V_k(\fg)$,
274:Heisenberg $\mathcal{H}_\kappa$ & G & 2 & --- & \S\ref{ch:heisenberg-frame} \\
530:$\max\operatorname{pole}(r) = 2h - 1$: the Heisenberg
609:\multicolumn{5}{|c|}{\textit{Heisenberg}} \\
839:Leech lattice VOA, the $24$ weight-$1$ Heisenberg generators
1039:\item[\textbf{T1.}] \emph{Unconditional} (free fields, Heisenberg):
1072:\noindent\textsuperscript{$\dagger$}The Heisenberg is the abelian Kac--Moody case ($h^\vee = 0$);
1115:Heisenberg $\cH_\kappa$ & \checkmark & (ii),(ix) & PBW universality \\
1202:For the Heisenberg algebra at level $\kappa = 1$ (single free boson, $c = 1$),
1207:In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.
1221:The anomaly ratio $\varrho(\cA) := \kappa(\cA)/c(\cA)$ measures how much of the conformal anomaly survives from the Lie bracket's cyclic deformation. For the rank-$d$ Heisenberg algebra $\cH_1^{\oplus d}$ at level~$1$, $\varrho = d/d = 1$: the Polyakov formula $F_1 = c/24$ and the shadow formula $F_1 = \kappa/24$ coincide because $\kappa = c = d$. For all other standard families, $\varrho \neq 1$:
1289: The Heisenberg is the abelian curved case, with
1292: The Heisenberg entry $c + c' = \text{---}$ reflects the fact that
1373:\item \emph{Heisenberg}: Koszul dual is the commutative chiral algebra
1650:Heisenberg $\cH_k$
1777:closed-form generating functions (Heisenberg, free fermion, $bc$,
1811:\item \emph{Heisenberg} ($d = 1$, commutative):
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '520,580p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\emph{Derived categories of coherent sheaves}. The algebraic input. For a smooth projective CY manifold $X$, the bounded derived category $D^b(\mathrm{Coh}(X))$ is CY of dimension~$d$ with the CY trace induced by Serre duality. Homological mirror symmetry identifies $\Fuk(X) \simeq D^b(\mathrm{Coh}(X^\vee))$; under $\Phi$, this becomes an equivalence $A_{\Fuk(X)} \simeq A_{D^b(\mathrm{Coh}(X^\vee))}$ of quantum chiral algebras, providing a consistency check between the symplectic and algebraic sides. When $D^b(\mathrm{Coh}(X))$ admits a full exceptional collection, the CY-to-chiral functor reduces to a quiver-with-potential computation: the critical CoHA of the quiver (Chapter~\ref{ch:toric-coha}). Bridgeland stability conditions parametrize the space of t-structures on $D^b(\mathrm{Coh}(X))$; wall-crossing in the stability manifold corresponds to mutations of the bar complex, and the global chiral algebra is assembled as a homotopy colimit over stability chambers (Programme~A).

\emph{Matrix factorizations}. The Landau--Ginzburg input. A polynomial $W \colon \mathbb{C}^n \to \mathbb{C}$ gives a CY category $\mathrm{MF}(W)$ of dimension $n - 2$. For ADE singularities $W = x^N + y^2 + z^2 + w^2$ in four variables, $\mathrm{MF}(W)$ is CY of dimension~$2$ and $\Phi$ (Theorem~CY-A$_2$) produces chiral algebras related to $\mathcal{W}_N$-algebras. The LG/CY correspondence $\mathrm{MF}(W) \simeq D^b(\mathrm{Coh}(X_W))$ provides a further consistency check against the derived-category side. For non-ADE singularities (unimodal, bimodal), the resulting chiral algebras are expected to be new objects not realized by the standard Lie-theoretic landscape of Volume~I.

\emph{Quantum group representations} (Chapter~\ref{ch:quantum-group-reps}). The representation-theoretic target. The braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$ is what the CY programme aims to realize: Conjecture~CY-C predicts that $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{Rep}^{E_2}(A_\cC)$ for a CY category $\cC(\mathfrak{g}, q)$. The Kazhdan--Lusztig equivalence $\mathrm{Rep}_q(\mathfrak{g}) \simeq \mathrm{KL}_k(\mathfrak{g})$ at roots of unity is the prototype: the Volume~I bar complex $B(V_k(\mathfrak{g}))$ encodes the quantum group $R$-matrix in its degree-$(1,1)$ component, and the DK bridge (Volume~II, MC3 for all simple types) recovers the quantum group categorical structure. The affine Yangian realization (Chapter~\ref{ch:toric-coha}) provides the $E_1$-sector; the Drinfeld center (Chapter~\ref{ch:drinfeld-center}) provides the $E_2$-enhancement.

In addition to the four standard families, the toroidal and elliptic algebras chapter (Chapter~\ref{chap:toroidal-elliptic}) develops the $K3 \times E$ programme in full: the generalized root datum, the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ with its Igusa cusp form denominator identity, the shadow--Siegel gap theorem, thirteen structural results (K3-1 through K3-13), all ten research programmes (A through J), and the DDCA--toroidal bridge identifying the deformed double current algebra as the rational degeneration of the quantum toroidal algebra (Conjecture~\ref{conj:ddca-toroidal-bridge}). The K3 double current algebra $\fg_{K3}$, discussed in the DDCA--toroidal bridge of Chapter~\ref{ch:k3-times-e}, provides the K3 analogue of the DDCA, replacing $\bC[u,v]$ with $H^*(S,\bC)$. The toric CY$_3$ CoHA chapter (Chapter~\ref{ch:toric-coha}) develops the affine Yangian and $\mathcal{W}_{1+\infty}$ side: the Jordan quiver gives $Y(\widehat{\mathfrak{gl}}_1) \simeq \mathcal{W}_{1+\infty}$, the toric fan is the Dynkin data, and the shuffle algebra presentation connects to the KZ equations of Volume~I.

\section{Guide for the reader}
\label{sec:guide}

Part~\ref{part:cy-categories} establishes the categorical foundations: CY categories, cyclic $\Ainf$-structures, the Hochschild calculus, and the $E_1$/$E_2$/$E_n$ chiral hierarchy with the framing obstruction tower. Part~\ref{part:bridge} constructs the bridge functor $\Phi$ from CY categories to quantum chiral algebras and proves Theorems CY-A (for $d = 2$) and CY-D, with the identification of automorphic correction and shadow obstruction tower as the main structural comparison. Part~\ref{part:examples} treats quantum groups and their braided factorization structure, including the Drinfeld center as the bulk algebra. Part~\ref{part:connections} works through the standard landscape: the toroidal and elliptic algebras chapter develops the $K3 \times E$ programme (K3-1 through K3-13, programmes A through J), alongside toric CY3 CoHAs, Fukaya categories, derived categories, matrix factorizations (ADE singularities and W-algebras), and quantum group representations (Kazhdan--Lusztig, affine Yangians, critical CoHAs). Part~\ref{part:frontier} connects to the geometric Langlands programme and to Volumes~I and~II via the bar-cobar bridge and the modular Koszul bridge. Open frontier material is kept separate from these chapters.

\section{Conventions and notation}
\label{sec:conventions-intro}

This volume inherits the conventions of Volumes~I and~II; we record here the points where the CY setting introduces additional notation or where conventions differ across the literature. A comprehensive conventions appendix is Appendix~\ref{app:conventions}.

\emph{Grading.} All grading is cohomological: differentials have degree $+1$. The bar construction uses desuspension $s^{-1}$, with $|s^{-1}v| = |v| - 1$ (matching Volume~I; see signs\_and\_shifts.tex therein). The CY dimension~$d$ enters as a cohomological shift: the CY trace $\mathrm{Tr} \colon \HH_\bullet(\cC) \to k[-d]$ is a map of degree $-d$.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"H_\\{N-1\\}\" chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4845:- N\,H_{N-1}(u)
4846:+ H_{N-1}(u{-}1)
exec
/bin/zsh -lc 'rg -n "kappa" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
15:$\kappa$, the cubic and quartic shadow coefficients $S_3$ and $S_4$,
16:and the critical discriminant $\Delta = 8\kappa S_4$. The
24:structure of the MC element $\Theta_\cA$: once $\kappa$ and $S_4$
32:The scalar modular characteristic $\kappa(\widehat{\fg}_k) = td/2h^\vee$
33:and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
48:obstruction coefficient $\kappa(\cA)$ from the genus universality
49:theorem $\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
68: & $\boldsymbol{\kappa(\cA)}$ & \textbf{Status} \\
83:Heisenberg $\mathcal{H}_\kappa$
85: & $1$ & ---\textsuperscript{$\dagger$} & $\kappa$ & PH \\
201:This is independent of shadow depth~$\kappa_d$
210:(Theorem~\ref{thm:mc2-bar-intrinsic}). The scalar $\kappa(\cA)$ is
220: &= \bigl(\cH_\kappa,\;
222: \kappa/z\bigr), &
229:% Omega/((k+h^v)z) with Omega = sum kappa^{ab} I_a otimes I_b;
274:Heisenberg $\mathcal{H}_\kappa$ & G & 2 & --- & \S\ref{ch:heisenberg-frame} \\
278:Niemeier $V_\Lambda$ (all 24; $\kappa = 24$) & G & 2 & ---; blind to root system & Thm~\ref{thm:lattice:niemeier-shadow-universality} \\
316:Monster $V^\natural$ ($c = 24$, $\kappa = 12$) & M & $\infty$ & Griess algebra at weight~$2$; $\Delta \neq 0$ & Rem~\ref{rem:lattice:monster-shadow} \\
586:\caption{Free energies $F_1 = \kappa/24$ and $F_2 = 7\kappa/5760$ for $21$ standard families}
594: & $\boldsymbol{\kappa}$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\kappa\\\\(\\\\mathcal\\{W\\}_N\\\\)' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '140,230p' /Users/raeez/calabi-yau-quantum-groups/notes/audit_red8_wall_crossing.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

**Severity: MEDIUM (expository/conceptual gap, not mathematical error)**

### The problem

Proposition 6.1 proves that the truncation $\Theta^{\leq r}_A(t)$ is discontinuous at walls for $r < \infty$. Section 6.3 then presents this as a *feature*, analogizing it with renormalization scheme dependence. But this framing obscures a serious conceptual problem:

**The full MC element $\Theta_A$ is the only gauge-invariant object, and it cannot be computed.**

The shadow obstruction tower is the computational handle on $\Theta_A$ -- one computes $\Theta^{\leq r}_A$ order-by-order and hopes the tower converges. But Proposition 6.1 says that every finite truncation is discontinuous at walls. This means:

(a) Any finite-order computation of the MC element *depends on the chamber* -- you must choose a stability condition before computing. The result is not intrinsic.

(b) The "UV completion" $\Theta_A$ that restores gauge invariance requires *infinitely many* arity contributions. In practice, only arities 2-4 are computable (the moduli spaces $\overline{\mathcal{M}}_{g,n}$ become intractable beyond small $g$ and $n$).

(c) The renormalization group analogy (Section 6.3) is misleading. In QFT, the running coupling at a given energy scale is a *measurable* quantity -- scheme-dependent but physically meaningful. Here, the truncation $\Theta^{\leq r}_A$ at a given arity is *not* physically meaningful because it jumps discontinuously. A quantity that is discontinuous as a function of moduli is not "scheme-dependent" -- it is simply not well-defined as a function on moduli space.

The honest statement is: the MC gauge equivalence interpretation of wall-crossing is a beautiful structural observation, but it converts a *computational* problem (determine BPS degeneracies) into a *non-computational* one (compute the full MC element). The denominator identity $\Phi_X$ is the gauge-invariant datum, but it is *already known* independently (it is the DT partition function / automorphic form). The MC framework does not produce $\Phi_X$ -- it *assumes* it.

### What is needed
exec
/bin/zsh -lc 'rg -n "H_N" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
730:$K_N = 4N^3 - 2N - 2$ and $\varrho_N = H_N - 1$; explicitly:
1258:where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
1416:General $\mathcal{W}_N$: $\kappa = c \cdot (H_N - 1)$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\kappa\\(\\\\mathcal\\{W\\}_N' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/nonlinear_modular_shadows.tex:3901:$\kappa(\mathcal{W}_N)(c(k)) + \kappa_{\mathrm{ghosts}}(k) = \kappa(\hat{\mathfrak{sl}}_N)(k)$
chapters/examples/w_algebras_deep.tex:913:$\kappa(\mathcal{W}_N) =
chapters/examples/w_algebras_deep.tex:917:\operatorname{tr}\kappa(\mathcal{W}_N)
chapters/examples/w_algebras_deep.tex:926:\operatorname{tr}\kappa(\mathcal{W}_N)
chapters/examples/w3_composite_fields.tex:13:$\kappa(\mathcal{W}_N)$. This section carries out the derivation in
chapters/examples/genus_expansions.tex:2325:\kappa(\mathcal{W}_N^k) + \kappa(\mathcal{W}_N^{k'}) = (c + c') \cdot (H_N - 1)
chapters/examples/genus_expansions.tex:3096:\kappa(\mathcal{W}_N^k) + \kappa(\mathcal{W}_N^{k'}) = 2(N{-}1)(2N^2{+}2N{+}1) \cdot (H_N - 1)
chapters/examples/w_algebras.tex:142:identification $\Gamma_{\mathcal{W}_N}=\kappa(\mathcal{W}_N)\Lambda$
chapters/examples/w_algebras.tex:2178:\kappa(\mathcal{W}_N^k) = c \sum_{s=2}^{N} \frac{1}{s}
chapters/examples/w_algebras.tex:2248:By definition, $\kappa(\mathcal{W}_N^k)$ is the coefficient of
chapters/examples/w_algebras.tex:2288:\kappa(\mathcal{W}_N^k) + \kappa(\mathcal{W}_N^{k'})
chapters/examples/w_algebras.tex:2624:$\kappa(\mathcal{W}_N) = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:2836:\item $\kappa(\mathcal{W}_N^k) = c \cdot (H_N - 1)$
chapters/examples/w_algebras.tex:4447: $C(N,k) = \kappa(V_k(\mathfrak{sl}_N)) - \kappa(\mathcal{W}_N^k)$
chapters/examples/w_algebras.tex:4474:$\kappa(\mathcal{W}_N^k) = c(\mathcal{W}_N^k) \cdot (H_N - 1)$,
chapters/theory/higher_genus_foundations.tex:5943:\kappa(\mathcal{W}_N^k) + \kappa(\mathcal{W}_N^{k'}) = (H_N - 1) \cdot K_N
chapters/theory/higher_genus_foundations.tex:5959:By Theorem~\ref{thm:genus-universality}(ii), $\kappa(\mathcal{W}_N^k) = c \cdot \varrho(\mathfrak{sl}_N)$ where $\varrho(\mathfrak{sl}_N) = \sum_{s=2}^N 1/s = H_N - 1$. Under the Feigin--Frenkel involution $k \mapsto k' = -k - 2N$, $c \mapsto c' = K_N - c$, so $\kappa' = (K_N - c)(H_N - 1)$ and $\kappa + \kappa' = K_N(H_N - 1)$.
chapters/theory/higher_genus_foundations.tex:6050:$\kappa(\mathcal{W}_N^k) = c \cdot (H_N - 1)$. Each produces the
chapters/theory/computational_methods.tex:617:$C(N,k) = \kappa(\AffKM{sl}_N, k) - \kappa(\mathcal{W}_N, k)$
chapters/theory/computational_methods.tex:624:In general, $\kappa(\mathcal{W}_N, k) = (H_N - 1)\cdot c(\mathcal{W}_N, k)$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3420,3475p' /Users/raeez/calabi-yau-quantum-groups/working_notes.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathfrak{sl}_6$ (26 orbits), including the first non-hook
orbit $(2,2)$ in $\mathfrak{sl}_4$ and the self-transpose
surprise $(3,2,1)$ in $\mathfrak{sl}_6$ (level-independent
complementarity despite being classified as ``non-even'').
Butson [arXiv:2508.18248] proves inverse Hamiltonian reduction
for all orbits in type~A, extending the transport graph from
hook-type to the full Hasse diagram.

\subsection{The shadow genus expansion as matrix model}

The closed-form generating function
$G[F](\xi) = \kappa_{\mathrm{ch}} \cdot (\xi/(2\sin(\xi/2)) - 1)
= \kappa_{\mathrm{ch}} \cdot (\sqrt{\hat{A}(i\xi)} - 1)$
packages all genus-$g$ free energies. It is meromorphic with
simple poles at $\xi = 2\pi n$ and universal Stokes constants
$S_n / S_1 = (-1)^{n+1} n$.

The genus expansion equals the GUE matrix model free energy at
$N^2 = \kappa_{\mathrm{ch}}(\cA)$ (Proposition~\ref{prop:gue-universality}).
The spectral curve $y^2 = Q_L(t)$ carries Eynard--Orantin
exec
/bin/zsh -lc 'rg -n "H_{N-1}" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:H_{N-1})
          ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '580,640p' /Users/raeez/calabi-yau-quantum-groups/notes/theory_denominator_bar_euler.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\kappa\\(\\\\widehat' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \sum_\gamma \chi(\widetilde{B}_\gamma)\, q^\gamma
 = q^{\rho} \cdot \sum_\gamma \chi(B_\gamma)\, q^\gamma
 = q^{\rho} \prod_{\alpha \in \Delta_+}(1 - q^\alpha)^{\mult(\alpha)}
\end{equation}
which is $e^{-2\pi i\langle\rho,z\rangle} \prod_\alpha (1 - q^\alpha)^{\mult(\alpha)} = \Phi_X(z)$.
\end{construction}

The shift by $\rho$ is not an arbitrary normalization: it is forced by the
\emph{modular anomaly} of the chiral algebra. Specifically:

\subsubsection{(b) The modular anomaly from $\kappa_{\mathrm{ch}}(A_X)$}

In Volume~I, the modular characteristic $\kappa_{\mathrm{ch}}(A)$ of a chiral algebra
$A$ controls the genus-$g$ obstruction: $d_B^2 = \kappa_{\mathrm{ch}}(A) \cdot \omega_g$
on $\overline{\mathcal{M}}_g$. For the chiral algebra $A_X$ of a CY3,
$\kappa_{\mathrm{ch}}(A_X)$ equals the weight of the automorphic form (e.g., $\kappa_{\mathrm{BKM}} = 5$
for $K3 \times E$).

The Weyl vector $\rho$ is the genus-0 manifestation of this anomaly.
The formula $(\rho, \delta_i) = -(\delta_i, \delta_i)/2$ for all simple
 succeeded in 52ms:
Total output lines: 230

tmp_standalone_audit/survey_v2_xr.tex:539:\kappa(\widehat\fg_k)
tmp_standalone_audit/survey_v2_xr.tex:553:$\kappa(\widehat\fg_k)+\kappa(\widehat\fg_k^!)=0$
tmp_standalone_audit/survey_v2_xr.tex:724:\kappa(\widehat{\mathfrak g}_k)=\frac{(k+h^\vee)\dim\mathfrak g}{2h^\vee}.
tmp_standalone_audit/survey_v2_xr.tex:2527:\kappa(\widehat\fg_k)=\kappa_{\mathrm{dp}}+\frac{\dim\fg}{2}
tmp_standalone_audit/survey_v2_xr.tex:2537:$\kappa(\widehat\fg_k)+\kappa(\widehat\fg_k^!)=0$.
appendices/combinatorial_frontier.tex:611:has $\kappa(\cA^!) = \kappa(\widehat{\mathfrak{g}}_{-k-2h^\vee})$,
chapters/examples/deformation_quantization.tex:1153:$m_0(\widehat{\fg}_k) = \kappa(\widehat{\fg}_k)\cdot\omega_1$
chapters/examples/deformation_quantization.tex:1155:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$
appendices/ordered_associative_chiral_kd.tex:3756:-\kappa(\widehat{\mathfrak{g}}_k)
chapters/examples/w_algebras_deep.tex:5195:\kappa(N{=}2) = \kappa(\widehat{\mathfrak{sl}}_{2,k})
chapters/examples/w_algebras_deep.tex:5196:+ \kappa(\psi\bar\psi) - \kappa(\widehat{U(1)}).
chapters/examples/w_algebras_deep.tex:5199:$\kappa(\widehat{\mathfrak{sl}}_{2,k}) = 3(k+2)/4$
chapters/examples/w_algebras_deep.tex:5202:$\kappa(\widehat{U(1)}) = k/2 + 1$ (Heisenberg at the
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:314:\kappa(\widehat\fg_k) \;=\; \frac{(k+h^\vee)\dim\fg}{2h^\vee}
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:319:\kappa(\widehat\fg_k) \;+\; \kappa(\widehat\fg_k^!)
chapters/examples/y_algebras.tex:719:$\kappa(\widehat{\mathfrak{gl}}(N)_{\Psi'})
chapters/examples/level1_bridge.tex:52: $\kappa(\widehat{\fg}_1) = \operatorname{rank}(\fg)$
chapters/examples/level1_bridge.tex:151:\kappa(\widehat{\fg}_k)
exec
/bin/zsh -lc "rg -n \"H_\\{N-1\\}\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\kappa\\(\\\\mathrm\\{Vir' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
working_notes.tex:1754:$\kappa(\mathrm{Vir}_{26-c}) = 0$.  The genuine dual is
tmp_standalone_audit/survey_v2_xr.tex:737:\kappa(\mathrm{Vir}_c)=c/2.
tmp_standalone_audit/survey_v2_xr.tex:740:$\kappa(\mathrm{Vir}_{26-c})=(26-c)/2$; the two sum to~$13$, not zero.
tmp_standalone_audit/survey_v2_xr.tex:1626:constant: $\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c})=13$ and
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:4462:$\kappa(\mathrm{Vir}_c) = c/2$.
chapters/examples/w_algebras_deep.tex:3541:(analogous to $\kappa(\mathrm{Vir}_c) = 0$ at $c=0$).
chapters/examples/w_algebras_deep.tex:3601:For $N = 0$: $\kappa(\mathrm{Vir}_{13}) = 13/2$
staging/for_ordered_assoc__glN_miura_spin2.tex:454:$\kappa(\mathrm{Vir}_c) = c/2$.
appendices/branch_line_reductions.tex:1063:\(\kappa(\mathrm{Vir}_c)=c/2\) by
appendices/branch_line_reductions.tex:1088:\(\kappa(\mathrm{Vir}_c)=c/2\).
staging/combined_for_ordered_assoc.tex:442:$\kappa(\mathrm{Vir}_c) = c/2$.
staging/combined_for_ordered_assoc.tex:653:$\kappa(\mathrm{Vir}_c) = c/2$.
chapters/examples/minimal_model_examples.tex:566:$\kappa(\mathrm{Vir}_c) = c/2 = 1/4$,
appendices/nonlinear_modular_shadows.tex:1398:$S_{\mathrm{Vir}}$ around the scalar $\kappa(\mathrm{Vir}_c) = c/2$.
chapters/examples/free_fields.tex:4572:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/connections/editorial_constitution.tex:1882: $\kappa(\mathrm{Vir}_c) = c/2$ and
chapters/connections/editorial_constitution.tex:1897:is the computation $\kappa(\mathrm{Vir}_c) = c/2$
chapters/examples/moonshine.tex:35: + \kappa(\mathrm{Vir}_2)
chapters/examples/moonshine.tex:246:\kappa(V^\natural) + \kappa(\mathrm{Vir}_2)
chapters/examples/moonshine.tex:252:the universal Virasoro complementarity sum + \kappa(\mathrm{Vir}_{26-c})
exec
/bin/zsh -lc 'rg -n "Sugawara" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1188: Critical level breaks the Sugawara construction, not free strong
1295: its central charge is not defined by the Sugawara construction.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,20p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{The $K3 \times E$ Tower and the Igusa Cusp Form}
\label{ch:k3-times-e}

The threefold $K3 \times E$ is a fibration of a CY$_2$ over a CY$_1$. Does its chiral algebra decompose accordingly? A naive Fubini argument would predict $A_{K3 \times E} \simeq A_{K3} \otimes A_E$, and the modular characteristic would split additively as $\kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$. But the Oberdieck--Pixton DT partition function of $K3 \times E$ is $C / (\Delta_5)^2$, where $\Delta_5$ is the Gritsenko--Nikulin automorphic form of weight~$5$ on $\mathrm{O}^+(3,2)$. The weight $5$ does not match the sum $3$: $5 \neq 2 + 1$.

Two different modular characteristics are in play, and conflating them is the source of the subscripted-$\kappa_{\bullet}$ confusion that was introduced to prevent. The chiral de Rham complex gives $\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C$, honestly additive over the fibration. The Borcherds lift weight gives $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, which is not a modular characteristic of any constructed chiral algebra: it is a weight attached to a generalized Borcherds--Kac--Moody superalgebra $\mathfrak{g}_{\Delta_5}$ through its denominator identity. The chiral algebra $A_{K3 \times E}$ of a putative CY-to-chiral functor at $d = 3$ is not constructed.

This chapter treats $K3 \times E$ as the prototype for the $d = 3$ programme. The concrete object of study is the BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, together with the Oberdieck--Pixton theorem identifying its denominator with the Igusa cusp form. The goal is to understand how much of the Vol~I bar-cobar apparatus survives in the $d = 3$ regime, where the CY-to-chiral functor is conjectural: which identities among root multiplicities, genus-$g$ partition functions, and lattice theta series are genuinely theorems versus conjectural identifications awaiting the $d = 3$ functor. The chapter concludes with the K3 double current algebra $\fg_{K3}$ (Definition~\ref{def:k3-double-current-algebra}), the K3 analogue of the double current algebra $\fg \otimes \bC[u,v]$ in which the polynomial ring is replaced by $H^*(S,\bC)$ and the polynomial residue pairing by the Mukai pairing; the resulting finite-dimensional Lie algebra serves as the classical limit of the conjectural ``K3 Yangian'' whose quantization is governed by the Maulik--Okounkov $R$-matrix (Theorem~\ref{thm:k3e-mo-rmatrix}).

\section{The CY3 geometry}
\label{sec:k3e-geometry}

Let $(E, e_0)$ be an elliptic curve with an $N$-torsion point and $S$ a K3 surface with elliptic fibration $\pi \colon S \to \mathbb{P}^1$ admitting sections $s_1, s_2 \colon \mathbb{P}^1 \to S$ with $s_2$ of order $N$ relative to $s_1$. The product $S \times E$ admits a free $\mathbb{Z}/N\mathbb{Z}$-action
\[
 (s, e) \longmapsto (s + s_2(\pi(s)), e + e_0),
\]
and the quotient $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$ is a projective Calabi--Yau threefold.

\begin{definition}[The DT zeta function]
\label{def:dt-zeta-k3e}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n '\\\\kappa' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 3939

compute/audit/sl3_rtt_latex_output.tex:48:$J^a(z)\,J^b(w) \sim k\,\kappa^{ab}/(z-w)^2 + f^{ab}{}_c\,J^c(w)/(z-w)$
compute/audit/non_simply_laced_rmatrix_report.tex:30:$\kappa = \operatorname{Killing}/(2h^\vee)$.
compute/audit/non_simply_laced_rmatrix_report.tex:37:The split Casimir $\Omega = \sum_{a,b} \kappa^{ab}\, t_a \otimes t_b \in \mathfrak{g} \otimes \mathfrak{g}$
compute/audit/non_simply_laced_rmatrix_report.tex:45: = \frac{e_\alpha \otimes f_\alpha + f_\alpha \otimes e_\alpha}{\kappa(e_\alpha, f_\alpha)}.
compute/audit/non_simply_laced_rmatrix_report.tex:47:The key non-simply-laced feature: $\kappa(e_\alpha, f_\alpha)$ depends on the root length.
compute/audit/non_simply_laced_rmatrix_report.tex:52:Root & $C_2$ type & $\kappa(e_\alpha, f_\alpha)$ & Casimir coeff $= 1/\kappa$ \\
compute/audit/non_simply_laced_rmatrix_report.tex:64:where $B = \kappa|_{\mathfrak{h}}$ is the restriction of the Killing form to
compute/audit/non_simply_laced_rmatrix_report.tex:97:\item The OPE double pole $k\kappa_{ab}/(z{-}w)^2$ becomes
compute/audit/non_simply_laced_rmatrix_report.tex:98: $k\kappa_{ab}/z$ after the d-log kernel absorbs one power.
compute/audit/non_simply_laced_rmatrix_report.tex:123: R_{12}(z) = \frac{k}{z} \sum_{a,b} \kappa^{ab}\,
compute/audit/non_simply_laced_rmatrix_report.tex:149:$\kappa(V_k, k{=}1)$ & $20/3$ & $20/3$ \\
compute/audit/non_simply_laced_rmatrix_report.tex:168: $\kappa(k) + \kappa(-k-6) = 0$, verified.
compute/audit/non_simply_laced_rmatrix_report.tex:211:$\Omega = \kappa^{-1}$ & \checkmark \\
compute/audit/non_simply_laced_rmatrix_report.tex:216:$\kappa(k{=}1) = 20/3$ & \checkmark \\
compute/audit/non_simply_laced_rmatrix_report.tex:217:$\kappa(k{=}{-}3) = 0$ (critical level) & \checkmark \\
compute/audit/non_simply_laced_rmatrix_report.tex:218:FF duality $\kappa(k) + \kappa(-k{-}6) = 0$ & \checkmark \\
main.tex:1024:characteristic~$\kappa(\cA)$ is the leading scalar that
main.tex:1056:$\kappa(\cA) \cdot \omega_g$ on~$\overline{\mathcal{M}}_g$
exec
/bin/zsh -lc 'rg -n "Sugawara shift" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n \"dim\\(g\\)/2\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n \"dim\\(g\\)\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\kappa\\(\\\\mathrm\\{Vir}_c\\\\) = c' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar
 exited 2 in 52ms:
rg: regex parse error:
    (?:\\kappa\(\\mathrm\{Vir}_c\\) = c)
                                       ^
error: unopened group
thinking
**Summarizing and classifying kappa occurrences**

I’m gathering canonical and suspect instances of `\kappa` usage across several TeX files, noting subscripted vs. bare forms and local definitions. I’ll organize them into bullet lists by file and line number, clearly marking AP113 violations with bare `\kappa` and emphasizing the instruction not to edit. The final response will include classifications, representative examples, and paths with line references for clarity.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\kappa\\(\\\\mathrm\\{Vir}_c\\) = c' --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
standalone/sc_chtop_pva_descent.tex:1459:$\kappa(\mathrm{Vir}_c) = c/2$ (since $\cW_2 = \mathrm{Vir}$).
standalone/ordered_chiral_homology.tex:4775:$\kappa(\mathrm{Vir}_c) = c/2$ (census C2). The
standalone/ordered_chiral_homology.tex:4989:$\kappa(\mathrm{Vir}_c) = c/2$.
appendices/nonlinear_modular_shadows.tex:1398:$S_{\mathrm{Vir}}$ around the scalar $\kappa(\mathrm{Vir}_c) = c/2$.
standalone/five_theorems_modular_koszul.tex:905: $\kappa(\mathrm{Vir}_c) = c/2$,\;
staging/for_ordered_assoc__glN_miura_spin2.tex:454:$\kappa(\mathrm{Vir}_c) = c/2$.
appendices/ordered_associative_chiral_kd.tex:3302:By Vol~I Theorem~D, $\kappa(\mathrm{Vir}_c) = c/2$. The Koszul
staging/combined_for_ordered_assoc.tex:442:$\kappa(\mathrm{Vir}_c) = c/2$.
staging/combined_for_ordered_assoc.tex:653:$\kappa(\mathrm{Vir}_c) = c/2$.
standalone/survey_modular_koszul_duality.tex:8033:This is $\kappa(\mathrm{Vir}_c) = c/2$ emerging from a
standalone/introduction_full_survey.tex:2088:$\kappa(\mathrm{Vir}_c) = c/2$ for Virasoro
standalone/three_dimensional_quantum_gravity.tex:233:$\kappa(\mathrm{Vir}_c) = c/2$
standalone/three_dimensional_quantum_gravity.tex:506:$\kappa(\mathrm{Vir}_c) = c/2$. The stress-tensor backreaction
standalone/three_dimensional_quantum_gravity.tex:761:\item $S_2 = \kappa(\mathrm{Vir}_c) = c/2$: the curvature of the
standalone/three_dimensional_quantum_gravity.tex:1020:$\kappa(\mathrm{Vir}_c) = c/2$ and
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:4462:$\kappa(\mathrm{Vir}_c) = c/2$.
chapters/examples/w_algebras.tex:1584:$\kappa(\mathrm{Vir}_c) = c/2$, in agreement with the genus universality
chapters/examples/w_algebras.tex:2743: $\kappa(\mathrm{Vir}_c) = c/2$, anomaly ratio $\varrho = 1/2$.
chapters/examples/w_algebras.tex:3477:\item $\kappa(\mathrm{Vir}_c) = c/2$
chapters/examples/w_algebras.tex:4734:$\kappa(\mathrm{Vir}_c) = c/2$.
codex
**Kappa Canonical**
- `main.tex:360-385` records the `\kappa_\bullet` spectrum for `K3×E` (cat/ch/ch/BKM/fiber), explicitly warns bare `\kappa` is forbidden, and defines all occurrences as subscripted modular characteristics; canonical flagship for AP113 compliance.
- `chapters/examples/k3_times_e.tex:1-13` contrasts the additive chiral kappa (`\kappa_{\mathrm{ch}}(K3\times E)=3`) with the Borcherds weight (`\kappa_{\mathrm{BKM}}=5`); both modular characteristics appear with their subscripts plus contextual definitions (chiral shadow vs automorphic weight).
- `notes/physics_anomaly_cancellation.tex:70-115` (table and genus-tower discussion) lists the family formulas—Heisenberg `\kappa_{\mathrm{ch}}=d`, Kac–Moody `((k+h^\vee)\dim\mathfrak g)/(2h^\vee)`, Virasoro `c/2`, and $\mathcal W_N$ `c(H_N-1)`—all subscripted, matching the Volume I conventions and serving as canonical references for family-wise kappa data.
- `notes/theory_denominator_bar_euler.tex:590-621` ties the modular anomaly to `\kappa_{\mathrm{ch}}(A_X)` and to the Weyl vector, again with the subscripted modular characteristic and a clear dictionary between shadow-obstruction levels and its contributions.

**AP113 / bare `\kappa` to check**
- `chapters/theory/en_factorization.tex:410-429` introduces a bare `\kappa` (the Yang $R$-matrix parameter $\kappa=h_1h_2h_3$) inside a theorem; since this volume forbids un-subscripted modular characteristics, flag for review even if the symbol is a general parameter.
- `notes/audit_red8_wall_crossing.md:205-220` refers to “the leading-order truncation (`\kappa`, the modular characteristic)” in a critique; because the reference to the modular characteristic lacks a qualifier, it violates AP113 and should be rewritten to `\kappa_{\mathrm{ch}}` (or another subscripted variant) to keep the notation unambiguous.
- `working_notes.tex:3455-3470` mentions “JT uses `\kappa`-class intersections” (a bare `\kappa` used in a heuristic comparison); while this is a noun phrase, the guidance in Vol III insists on subscripted modular characteristics whenever the symbol appears, so this note remains a suspect spot to rephrase.

No edits were made; these hits mark the current live occurrences for follow-up.
wait(call_uXJZpdG2P3XZTmyRetV9FphC) 1 agents complete:
  019d87b9-6cc4-71e0-9720-3e44ceb5341a completed: "**Kappa Canonical**
- `main.tex:360-385` records the `\kappa_\bullet` spectrum for `K3×E` (cat/ch/ch/BKM/fiber), explici…"
exec
/bin/zsh -lc "rg -n \"dim\\(g\\)\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


exec
/bin/zsh -lc "rg -n \"dim\\\\fg\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

thinking
**Evaluating responses**

I’m wondering why only one result came back. Wait, maybe the wait function returns whichever finished first? It seems to have returned a status for just one. I think I need to wait again for the rest to come through. It’s interesting how asynchronous calls like this can sometimes be tricky to manage. I just want to make sure I’m getting all the information I need!
codex
The first explorer came back with the Vol III surface. It confirms the main manuscript is mostly AP113-clean, but there are still bare-`\kappa` suspect spots outside the flagship examples and a few family-formula tables to cross-check against Vol I.
collab wait(call_YOSHpCZRVPDw6RmDOIdHTbe2)
  receivers: 019d87b9-6cc8-7451-8e4f-96b80f90b887, 019d87b9-6cdf-7663-a4a2-cca693f6ba86
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '20,50p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
characterizes Gaussian algebras (class~G), $S_3 \neq 0$ with
$S_4 = 0$ singles out affine Kac--Moody (class~L), and $\Delta \neq 0$
forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
(class~M). The classification is not imposed but forced by the
structure of the MC element $\Theta_\cA$: once $\kappa$ and $S_4$
are computed, the archetype is determined.

% Regimes I--III : census spans all families (Convention~\ref{conv:regime-tags}).
The table below records the full set of computed invariants for every
Koszul chiral algebra treated in Part~\ref{part:physics-bridges}. Read horizontally, each row
is a complete portrait of one algebra; read vertically, the columns
expose the structural regularities that no single example can reveal.
The scalar modular characteristic $\kappa(\widehat{\fg}_k) = td/2h^\vee$
and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
theorem (Theorem~\ref{thm:genus-universality}), a pattern visible
only across the full landscape.

\noindent\emph{The Master Table below collects the invariants computed throughout Part~\ref{part:physics-bridges}. For the Heisenberg algebra, these invariants were derived in Chapter~\ref{ch:heisenberg-frame}; for each subsequent algebra, the corresponding chapter provides the complete computation.}

\section*{Master table of computed invariants}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/landscape_census.tex | sed -n '20,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    20	characterizes Gaussian algebras (class~G), $S_3 \neq 0$ with
    21	$S_4 = 0$ singles out affine Kac--Moody (class~L), and $\Delta \neq 0$
    22	forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
    23	(class~M). The classification is not imposed but forced by the
    24	structure of the MC element $\Theta_\cA$: once $\kappa$ and $S_4$
    25	are computed, the archetype is determined.
    26	
    27	% Regimes I--III : census spans all families (Convention~\ref{conv:regime-tags}).
    28	The table below records the full set of computed invariants for every
    29	Koszul chiral algebra treated in Part~\ref{part:physics-bridges}. Read horizontally, each row
    30	is a complete portrait of one algebra; read vertically, the columns
    31	expose the structural regularities that no single example can reveal.
    32	The scalar modular characteristic $\kappa(\widehat{\fg}_k) = td/2h^\vee$
    33	and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
    34	theorem (Theorem~\ref{thm:genus-universality}), a pattern visible
    35	only across the full landscape.
    36	
    37	\noindent\emph{The Master Table below collects the invariants computed throughout Part~\ref{part:physics-bridges}. For the Heisenberg algebra, these invariants were derived in Chapter~\ref{ch:heisenberg-frame}; for each subsequent algebra, the corresponding chapter provides the complete computation.}
    38	
    39	\section*{Master table of computed invariants}
exec
/bin/zsh -lc "rg -n \"\\\\dim\\\\fg\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'cH_k' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1040,1110p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
415:$\cH_k$ ($JJ$)
1650:Heisenberg $\cH_k$
 succeeded in 52ms:
  1040	 Koszulness is elementary ($d_{\mathrm{bracket}} = 0$ or $\dim V \le 2$).
  1041	 All invariants follow by direct computation.
  1042	\item[\textbf{T1$\frac{1}{2}$.}] \emph{Unconditional via PBW}
  1043	 (Kac--Moody and Virasoro at all genera):
  1044	 Koszulness proved via the PBW spectral sequence
  1045	 (Theorems~\ref{thm:km-chiral-koszul}
  1046	 and~\ref{thm:virasoro-chiral-koszul}); higher-genus PBW concentration
  1047	 proved unconditionally for Kac--Moody and Virasoro
  1048	 (Theorems~\ref{thm:pbw-allgenera-km}
  1049	 and~\ref{thm:pbw-allgenera-virasoro}).
  1050	 All invariants follow from the main theorems.
  1051	\item[\textbf{T2.}] \emph{Unconditional higher-spin finite type}
  1052	 (principal finite-type $\mathcal{W}$-algebras):
  1053	 Koszulness is proved via the PBW spectral sequence in the finite-type
  1054	 cases, and higher-genus PBW concentration is now unconditional at all
  1055	 genera by Theorem~\ref{thm:pbw-allgenera-principal-w}.
  1056	\item[\textbf{DK-core.}] \emph{$\Eone$-Yangian regime}:
  1057	 the proved content is the chain-level $\Eone$-bar-cobar / DK square
  1058	 and the evaluation-locus factorization comparison
  1059	 \textup{(}Theorems~\ref{thm:e1-chiral-koszul-duality},
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/landscape_census.tex | sed -n '1620,1675p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1620	an imaginary quadratic field $K_L = \bQ(\sqrt{D_0})$ and,
  1621	via the Dedekind factorization, a Dirichlet $L$-function
  1622	$L(s, \chi_d)$
  1623	(Theorem~\ref{thm:shadow-epstein-zeta},
  1624	Remark~\ref{rem:shadow-field}).
  1625	For class~$\mathbf{G}$ and~$\mathbf{L}$ algebras,
  1626	$\Delta = 0$ and the Epstein zeta degenerates.
  1627	Table~\ref{tab:shadow-l-functions} records the shadow field data
  1628	for all standard families at representative central charges.
  1629	
  1630	\begin{table}[ht]
  1631	\centering
  1632	\caption{Shadow field and Epstein $L$-function data}
  1633	\label{tab:shadow-l-functions}
  1634	\index{shadow field!standard families}
  1635	\renewcommand{\arraystretch}{1.4}
  1636	{\small
  1637	\begin{tabular}{|l|c|c|c|c|c|}
  1638	\hline
  1639	\textbf{Family}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/free_fields.tex | sed -n '5435,5460p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5435	\index{main theorems!free field verification}
  5436	\index{Chriss--Ginzburg structure principle!free fields}
  5437	Each free-field archetype verifies all five main theorems as projections
  5438	of the universal MC element
  5439	$\Theta_\cA \in \MC(\gAmod)$
  5440	(Theorem~\ref{thm:mc2-bar-intrinsic}). The verification tables below
  5441	organize the proved data per family; the shadow archetype column
  5442	refers to the classification of
  5443	Table~\ref{tab:shadow-tower-census}.
  5444	\end{remark}
  5445	
  5446	\subsubsection{Heisenberg: five-theorem verification}
  5447	
  5448	\begin{computation}[Five projections of $\Theta_{\cH_k}$;
  5449	\ClaimStatusProvedHere]
  5450	\label{comp:heisenberg-five-theorems}
  5451	\index{Heisenberg algebra!five-theorem verification}
  5452	Shadow archetype: G (Gaussian, $r_{\max} = 2$).
  5453	$\kappa(\cH_k) = k$.
  5454	Central charge $c = 1$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/thqg_celestial_holography_extensions.tex | sed -n '600,655p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   600	Let $\cA = \mathcal{H}_k$ be the Heisenberg algebra at level $k \neq 0$.
   601	(This is a Gaussian algebra with shadow depth~$2$ and, for the
   602	Heisenberg family, lies on the proved scalar lane in Vol~I.)
   603	Then:
   604	\begin{enumerate}[label=\textup{(\roman*)}]
   605	\item $r_{\max}(\mathcal{H}_k) = 2$ (Gaussian shadow depth).
   606	\item $J^2(\mathcal{H}_k) = J^\infty(\mathcal{H}_k) = \C \cdot \kappa$, with
   607	 $\kappa(\mathcal{H}_k) = k$.
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
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '200,245p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   200	$\operatorname{ek} = N{-}1$ for $\cW_N$.
   201	This is independent of shadow depth~$\kappa_d$
   202	(Theorem~\ref{thm:shadow-euler-independence}).
   203	\end{remark}
   204	
   205	\medskip
   206	
   207	\noindent\textbf{The shadow obstruction tower as organizing frame.}
   208	Every entry in Table~\ref{tab:master-invariants} is a projection of the
   209	universal MC element $\Theta_\cA \in \MC(\gAmod)$
   210	(Theorem~\ref{thm:mc2-bar-intrinsic}). The scalar $\kappa(\cA)$ is
   211	the degree-$2$ projection; the complementarity sum $c + c'$ is the
   212	ambient shadow at genus~$0$; the Koszul dual is obtained via
   213	Verdier duality on the bar coalgebra.
   214	The seed datum for each family is its modular Koszul triple
   215	$\mathfrak{T} = (\cA, \cA^!, r(z))$
   216	(Definition~\ref{def:modular-koszul-triple}):
   217	\begin{equation}\label{eq:census-triples}
   218	\begin{aligned}
   219	\mathfrak{T}_{\cH}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/kac_moody.tex | sed -n '1290,1325p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1290	$\overline{C}_n(X)$ by induction on the number of internal edges.
  1291	
  1292	\emph{Consistency.}
  1293	For $\fg = \mathfrak{sl}_2$ ($h^\vee = 2$):
  1294	$k \mapsto -k - 4$, matching
  1295	Theorem~\ref{thm:sl2-koszul-dual}.
  1296	For $\fg = \mathfrak{sl}_3$ ($h^\vee = 3$):
  1297	$k \mapsto -k - 6$, matching
  1298	\S\ref{sec:sl3-computation}.
  1299	\end{proof}
  1300	
  1301	\begin{remark}[Higher-genus extension of the level identification]
  1302	\label{rem:level-shift-higher-genus}
  1303	\index{level identification!higher genus}
  1304	The identification~\eqref{eq:verdier-level-shift} is a genus-$0$
  1305	statement: it determines the Koszul dual \emph{level} from the
  1306	binary collision data on~$\overline{C}_2(X)$. The extension to
  1307	higher genera is automatic: once the dual level $k^* = -k - 2h^\vee$
  1308	is determined, the modular characteristic
  1309	$\kappa(\widehat{\fg}_k) = \dim(\fg)(k + h^\vee)/(2h^\vee)$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/examples/examples-complete-conditional.tex | sed -n '320,350p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   320	\begin{proposition}[Curvature for $\widehat{\mathfrak{sl}}_2$;
   321	\ClaimStatusProvedHere]
   322	\label{prop:su2-curvature}
   323	The genus-$1$ curvature
   324	(Volume~I, Theorem~D, the modular characteristic) evaluates to
   325	\begin{equation}\label{eq:su2-curvature}
   326	\kappa(\widehat{\mathfrak{sl}}_2, k) = \frac{3(k + 2)}{4},
   327	\end{equation}
   328	where $3 = \dim(\mathfrak{sl}_2)$ and $h^\vee = 2$ is the
   329	dual Coxeter number. By complementarity (Volume~I, Theorem~C):
   330	\begin{equation}
   331	\kappa(\widehat{\mathfrak{sl}}_{2,k})
   332	+ \kappa(\widehat{\mathfrak{sl}}_{2,-k-4}) = 0.
   333	\end{equation}
   334	The Koszul dual level is $k' = -k - 2h^\vee = -k - 4$
   335	(Feigin--Frenkel involution).
   336	\end{proposition}
   337	
   338	\begin{proof}
   339	The central charge of $\widehat{\mathfrak{sl}}_2$ at level~$k$
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1240,1285p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1240	For any principal $\mathcal{W}$-algebra $\mathcal{W}^k(\fg)$ of a simple Lie algebra~$\fg$ with exponents $m_1, \ldots, m_r$, the anomaly ratio $\varrho(\mathcal{W}^k(\fg)) = \sum_{i=1}^r 1/(m_i + 1)$ is independent of the level~$k$. In particular:
  1241	$\varrho(\mathrm{Vir}) = 1/(1+1) = 1/2$,
  1242	$\varrho(\mathcal{W}_3) = 1/2 + 1/3 = 5/6$,
  1243	$\varrho(\mathcal{W}_4) = 1/2 + 1/3 + 1/4 = 13/12$.
  1244	The ratio $\varrho > 1$ for $\mathcal{W}_N$ with $N \geq 4$: the modular characteristic exceeds the central charge. The ratio $\varrho(\mathcal{W}_\infty) = \sum_{m=1}^\infty 1/(m+1) = \infty$: the divergence is the harmonic series.
  1245	\end{corollary}
  1246	
  1247	\begin{proof}
  1248	By Theorem~\ref{thm:genus-universality}(ii), the modular characteristic of $\mathcal{W}^k(\fg)$ is $\kappa = c \cdot \sum_{i=1}^r 1/(m_i+1)$. Since $\varrho = \kappa/c$, the ratio depends only on the exponents of~$\fg$, not on~$k$. The special values follow by direct substitution.
  1249	\end{proof}
  1250	
  1251	\begin{corollary}[Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio; \ClaimStatusProvedHere]
  1252	\label{cor:genus1-anomaly-ratio}
  1253	\index{anomaly ratio!genus-1 free energy}
  1254	For any $\mathcal{W}$-algebra $\mathcal{W}^k(\mathfrak{g})$ with central charge $c \neq 0$, the genus-$1$ free energy satisfies
  1255	\begin{equation}\label{eq:F1-over-c}
  1256	\frac{F_1(\mathcal{W}^k(\mathfrak{g}))}{c} = \frac{\varrho(\mathfrak{g})}{24}
  1257	\end{equation}
  1258	where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
  1259	\end{corollary}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/w_algebras.tex | sed -n '1550,1605p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1550	to the torus $E_\tau$ and computes all three main-theorem invariants,
  1551	paralleling \S\ref{sec:sl2-genus-one-pipeline}.
  1552	
  1553	Unlike the Kac--Moody bar complex, which is
  1554	\emph{uncurved} at genus~0 ($\dzero^2 = 0$, reflecting the Jacobi identity) with
  1555	genus-1 curvature $\mcurv{1} = (k+h^\vee)\cdot\omega_1$ arising entirely from the $B$-cycle
  1556	monodromy, the Virasoro bar complex is already curved at genus~0
  1557	($m_0 = c/2$, reflecting the quartic pole). The $B$-cycle monodromy at
  1558	genus~1 promotes this scalar curvature to a cohomology class on
  1559	$\overline{\mathcal{M}}_{1,1}$.
  1560	
  1561	\subsubsection{Genus-1 bar complex}
  1562	
  1563	The genus-1 bar complex is:
  1564	\begin{equation}\label{eq:vir-genus1-bar}
  1565	\barB^{(1),n}(\mathrm{Vir}_c) = \Gamma\bigl(\overline{C}_n(E_\tau),\;
  1566	 \omega_{E_\tau}^{\otimes 2n} \otimes \Omega^n_{\log}\bigr)
  1567	\end{equation}
  1568	where the exponent $2n$ reflects the conformal weight $h_T = 2$ of the
  1569	generator (each copy of $T$ contributes weight~$2$ to the tensor product).
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '720,750p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   720	${}^\dagger$For $\beta\gamma$ and $bc$: $\Delta = 0$ and $\rho = 0$ on the primary
   721	(weight-changing) line by stratum separation
   722	(Remark~\ref{rem:contact-stratum-separation}); the quartic contact invariant
   723	$\mathfrak{Q}^{\mathrm{contact}} \neq 0$ lives on a charged stratum.
   724	Both two-generator free-field systems share the same stratum separation
   725	mechanism and class~C shadow depth.
   726	The Virasoro discriminant complementarity is
   727	$\Delta(c) + \Delta(26{-}c) = 6960/[(5c{+}22)(152{-}5c)]$
   728	(Corollary~\ref{cor:discriminant-atlas}(ii)).
   729	The Koszul conductor for $\mathcal{W}_N$ is
   730	$K_N = 4N^3 - 2N - 2$ and $\varrho_N = H_N - 1$; explicitly:
   731	$K_2 = 26$, $K_3 = 100$, $K_4 = 246$, $K_5 = 488$.
   732	The self-dual central charges are $c^* = K_N/2$: $c^* = 13$ for Virasoro,
   733	$c^* = 50$ for $\mathcal{W}_3$, $c^* = 123$ for $\mathcal{W}_4$.
   734	${}^\S$For the Monster module $V^\natural$: the complementarity
   735	sum $\kappa + \kappa' = 13$ is the Virasoro-sector value
   736	($\kappa(V^\natural) = 12$, $\kappa(\mathrm{Vir}_2) = 1$; sum $= 13$),
   737	since $\dim V_1^\natural = 0$ forces $\kappa = c/2 = 12$
   738	.
   739	
wait(call_YOSHpCZRVPDw6RmDOIdHTbe2) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/w_algebras.tex | sed -n '2600,2665p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2600	
  2601	\begin{remark}[Scope: AGT correspondence]
  2602	A proof requires localization on the instanton moduli space and identification of contributions with W-algebra matrix elements; see Alday--Gaiotto--Tachikawa~\cite{AGT09}. The gauge-theory comparison depends on the MC5 sewing machinery and is deferred to that context.
  2603	\end{remark}
  2604	
  2605	\begin{theorem}[AGT shadow correspondence;
  2606	\ClaimStatusProvedHere]%
  2607	\label{thm:agt-shadow-correspondence}%
  2608	\index{AGT correspondence!shadow tower interpretation|textbf}%
  2609	\index{Nekrasov partition function!genus expansion}%
  2610	\index{shadow tower!AGT correspondence}%
  2611	The shadow obstruction tower of $\mathcal{W}_N$ controls the universal
  2612	\textup{(}representation-independent\textup{)} part of the
  2613	Nekrasov genus expansion. Specifically, for
  2614	$\mathrm{SU}(N)$ gauge theory with $\Omega$-background
  2615	$(\epsilon_1, \epsilon_2)$:
  2616	\begin{enumerate}[label=\textup{(\roman*)}]
  2617	\item \textup{(Parameter identification.)}
  2618	The central charge is
  2619	$c = (N{-}1)(1 + N(N{+}1)(b + 1/b)^2)$ where
collab wait(call_y0otqiIq0jX1WpcOdoyzA4Rw)
  receivers: 019d87b9-6cc8-7451-8e4f-96b80f90b887, 019d87b9-6cdf-7663-a4a2-cca693f6ba86
exec
/bin/zsh -lc "rg -n \"\\\\cH\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\cH)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"\\\\\\\\cH\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
219:\mathfrak{T}_{\cH}
220: &= \bigl(\cH_\kappa,\;
415:$\cH_k$ ($JJ$)
1115:Heisenberg $\cH_\kappa$ & \checkmark & (ii),(ix) & PBW universality \\
1221:The anomaly ratio $\varrho(\cA) := \kappa(\cA)/c(\cA)$ measures how much of the conformal anomaly survives from the Lie bracket's cyclic deformation. For the rank-$d$ Heisenberg algebra $\cH_1^{\oplus d}$ at level~$1$, $\varrho = d/d = 1$: the Polyakov formula $F_1 = c/24$ and the shadow formula $F_1 = \kappa/24$ coincide because $\kappa = c = d$. For all other standard families, $\varrho \neq 1$:
1573:$\cH + \mathrm{Vir}$
1650:Heisenberg $\cH_k$
2794:Heisenberg $\cH_\kappa$
2832:$\cH_\kappa$ is the exterior algebra on $V^*$, giving
2833:$\dim (\cH_\kappa^!)_n = p(n{-}2)$ (partitions);
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/examples/w-algebras-stable.tex | sed -n '840,910p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   840	Here $K_{\mathcal{W}_N} = \kappa + \kappa^! = (H_N - 1)\alpha_N$
   841	is the complementarity sum
   842	(Proposition~\ref{prop:complementarity-sum-formula} below),
   843	and the critical central charge $c_{\mathrm{crit}} = \alpha_N$
   844	is the matter-ghost cancellation point for $\mathcal{W}_N$ strings.
   845	The $\mathcal{W}_3$ self-dual point $c = 50$ plays the role for
   846	higher-spin gravity that $c = 13$ plays for pure gravity.
   847	\end{remark}
   848	
   849	\begin{proposition}[Complementarity sum formula; \ClaimStatusProvedHere]
   850	\label{prop:complementarity-sum-formula}
   851	\index{complementarity sum!general formula|textbf}
   852	For the principal $\mathcal{W}_N$ algebra at central charge~$c$,
   853	\begin{equation}\label{eq:complementarity-sum-formula}
   854	K_N \;:=\; \kappa(\mathcal{W}_{N,c})
   855	 + \kappa(\mathcal{W}_{N,\alpha_N - c})
   856	\;=\; (H_N - 1)\,\alpha_N,
   857	\end{equation}
   858	where $H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number
   859	and $\alpha_N = 2(N{-}1)(2N^2{+}2N{+}1)$. The ratio
codex
The canonical κ formulas live in `chapters/examples/landscape_census.tex` (there is no `chapters/connections/landscape_census.tex`), so the line references below point there.

- Heisenberg: the master-table row makes the obstruction coefficient the level parameter itself (κ(ℋκ)=κ) and the modular Koszul triple lists the chiral seed as (ℋκ, Sym⁽ch⁾(V⁎), κ/z). See `chapters/examples/landscape_census.tex:81-85` for the table and `:217-223` for the triple that fixes the κ-level.  
- Virasoro: the universality discussion states κ(Vir_c)=c/2, the Vir row in the table records that same ratio, and the Vir modular triple forces the 2nd-order pole c/(2z³)+2T/z. See `chapters/examples/landscape_census.tex:32-34` (statement of κ formulas) and `:140-143` plus `:239-242` for the status/table/triple entries.  
- Affine Kac–Moody: the same paragraph gives κ(𝔤̂ₖ)=t·d/(2h∨) with t=k+h∨, and the general affine section/row reiterates the Feigin–Frenkel shift k↦−k−2h∨; the Koszul triple uses k·Ω₍tr₎/z while the KZ normalization shows Ω/(k+h∨)z (the bridge note records κ₍tr₎=k vs. κ₍KZ₎=k+h∨). See `chapters/examples/landscape_census.tex:32-34`, `:88-117`, and the convention note `:227-235`.  
- 𝒲_N: the general 𝒲-algebra entry records κ=c·(H_N−1) and the anomaly-ratio discussion spells out that this is the correct harmonic sum (not H_{N−1}). See `chapters/examples/landscape_census.tex:1416` for the formula and `:730-733` plus `:1258` for the remarks tying κ/c=H_N−1 (the paragraph explicitly insists on H_N−1).

Notes:
- The “Sugawara”-style normalization shift between the trace-form triple (k·Ωₜᵣ/z) and the KZ triple (Ω/(k+h∨)z) is spelled out in `chapters/examples/landscape_census.tex:227-235`, so the “Sugawara shift” is the k↦k+h∨ reconciliation there.  
- The harmonic-number comment in `chapters/examples/landscape_census.tex:730-733` and `:1258` repeatedly uses H_N−1 for the 𝒲_N anomaly ratio, thereby ruling out any H_{N−1} variant in this canonical census.
wait(call_y0otqiIq0jX1WpcOdoyzA4Rw) 1 agents complete:
  019d87b9-6cdf-7663-a4a2-cca693f6ba86 completed: "The canonical κ formulas live in `chapters/examples/landscape_census.tex` (there is no `chapters/connections/landscape_c…"
codex
Heisenberg  
- `chapters/examples/free_fields.tex:5453` pulls the five-theorem verification table and simply states `$\kappa(\cH_k)=k$` as the scalar obstruction on the Gaussian lane—matches the canonical landscape C1 value. (canonical)  
- `chapters/connections/thqg_celestial_holography_extensions.tex:606-617` flags the quadratic jet/value $J^2= \C\cdot \kappa$ and spells out `$\kappa(\mathcal{H}_k)=k$` again while reconstructing the genus‑0 scalar partition function. (canonical)

Affine Kac–Moody  
- `chapters/examples/kac_moody.tex:1299-1319` reviews the higher-genus extension of level identification and gives the universal genus‑one obstruction `$\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)$` with anti‑symmetry under $k\mapsto -k-2h^\vee$. (canonical)  
- `chapters/examples/examples-complete-conditional.tex:326-335` proves the same formula for $\mathfrak{sl}_2$, writing `$\kappa(\widehat{\mathfrak{sl}}_2,k)=3(k+2)/4$` alongside the complementarity sum—again the expected canonical value. (canonical)

Virasoro  
- `chapters/examples/w_algebras.tex:1576-1586` (Theorem 5.2) shows the genus‑1 differential satisfies $(d^{(1)})^2=(c/2)\omega_1$ and concludes `$\kappa(\mathrm{Vir}_c)=c/2$`, in line with the universal genus rule. (canonical)  
- `chapters/examples/w-algebras-stable.tex:867-874` records the general $\mathcal{W}_N$ curvature $\kappa(\mathcal{W}_{N,c})=c(H_N-1)$ and, via $H_2-1=1/2$, recovers the Virasoro special case. (canonical)

$\mathcal{W}_N$  
- `chapters/examples/w_algebras.tex:2623-2634` (AGT shadow correspondence, Part (i)) states `$\kappa(\mathcal{W}_N)=c\cdot(H_N-1)$` and uses that harmonic-number factor to control the universal genus expansion—again the canonical formula listed in C1–C4. (canonical)  
- `chapters/examples/w-algebras-stable.tex:849-874` proves the complementarity sum $K_N=\kappa(\mathcal{W}_{N,c})+\kappa(\mathcal{W}_{N,\alpha_N-c})=(H_N-1)\alpha_N$ by splitting $\kappa(\mathcal{W}_{N,c})=c(H_N-1)$ and $\kappa(\mathcal{W}_{N,\alpha_N-c})=(\alpha_N-c)(H_N-1)$—all consistent with the canonical harmonic-number formula. (canonical)

Search coverage: both Vol I (`/Users/raeez/chiral-bar-cobar`) and Vol II (`/Users/raeez/chiral-bar-cobar-vol2`) TeX sources were scanned for these explicit formula statements, and all hits align with the approved canonical values; no suspect variants surfaced.
collab wait(call_UWnNM07UkvMJ5ypqPBb3dbrc)
  receivers: 019d87b9-6cc8-7451-8e4f-96b80f90b887
wait(call_UWnNM07UkvMJ5ypqPBb3dbrc) 1 agents complete:
  019d87b9-6cc8-7451-8e4f-96b80f90b887 completed: "Heisenberg  
- `chapters/examples/free_fields.tex:5453` pulls the five-theorem verification table and simply states `$\k…"




thinking
**Inspecting for formula issues**

The explorer didn’t find any suspect variants, but a manual search might reveal problems, particularly in volume III notes. I’ll probably need to use targeted searches for KM formula variants and bare kappa. While there may not be explicit wrong formulas in the chapters, the user wants to find and fix any issues, so I need to ensure I'm thorough across all three volumes, including notes. This seems vital to help prevent future audits!
thinking
**Addressing kappa formula inconsistencies**

I can only make fixes in Volume I due to permissions, but I'm not sure if the notes in Volume III are writable. I need to report any blocks and inspect the current repo for specific files. The task is focused on ensuring cross-volume kappa formula consistency for each family, which involves verifying that all formulas match the canonical census. I'll need to perform exact searches, checking both chapters and notes for any discrepancies!
thinking
**Running targeted searches for kappa formulas**

I need to run a targeted search using rg for both chapters and standalone files to find any suspect variants. I'll focus on patterns like `k/(2h` and also look for `H_{N-1}` near kappa to identify potential issues. Then, I should check Volume III for instances of bare kappa in the live chapters. For example, `bar_cobar_bridge.tex` might use `\kappa_{\mathrm{ch}}(W_N)`, but I need to assess if occurrences in `cy_to_chiral.tex` are okay, given they’re not modular characteristics.
thinking
**Clarifying subscript restrictions**

I see that AP113 states approved subscripts must form a closed set, and bare kappa isn't allowed for modular characters. But I'm wondering if other uses of kappa might be acceptable? The user mentioned the importance of formula consistency, so I should consider this carefully. It may be possible to overlook non-modular parameter for bare kappa unless it's ambiguous. I might need to use an update plan with specific steps to clarify this.
codex
I have enough context to lock the task surface.

1. `Scope lock` — audit every live family formula surface for Heisenberg, Virasoro, affine KM, and `\mathcal W_N` across Vol I, Vol II, Vol III; treat Vol III AP113 notation as part of the same surface.
2. `Verification` — check each family against the canonical census in [landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex), using formula text plus boundary checks.
3. `Patch set` — apply the smallest truthful edits only where the live source still drifts: wrong formula, ambiguous `H_{N-1}`/`H_N-1`, or bare Vol III modular `\kappa`.
4. `Propagation + verify` — re-grep the edited surfaces and run targeted negative greps for the bad variants.

I’m now narrowing the exact file list and line-level edits.
Plan update
  ✓ Map live kappa formula surfaces across Vol I/II/III and isolate any drifts from the canonical census
  → Read the exact files that need changes and verify each suspect occurrence in context
  • Apply minimum truthful edits in writable scope and document blocked cross-volume fixes outside writable roots
  • Run targeted verification greps and summarize findings with exact edits

thinking
**Checking kappa formula references**

I’m looking into the grep results for H_N vs H_{N-1}. It seems I didn’t find any wrong kappa formula—just references to H_{N-1} in harmonic polynomials that aren’t relevant. Now, I should search for the affine formula to see if there’s a missing +h shift in the chapters and standalone sections. There must be something I can investigate further to clarify this. Let's keep digging!
exec
/bin/zsh -lc "rg -n --glob '*.tex' '(?<"'![A-Za-z])'"\\\\kappa\\(["'^)]*Kac|'"\\\\kappa\\(["'^)]*'"\\\\widehat|\\\\kappa\\(["'^)]*'"\\\\fg|\\\\kappa\\(["'^)]*'"\\\\mathfrak\\{g\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'dim\\(["'^)]*'"\\)\\s*\\(k\\+h\\"'^|dim'"\\(["'^)]*'"\\)\\s*k/(2h\\"'^|'"\\\\dim\\s*\\\\fg.*k\\+h\\"'^|'"\\\\dim\\s*\\\\fg.*k/(2h\\"'^|'"\\\\frac\\{\\\\dim\\(["'^}]+'"\\)k\\}|\\\\frac\\{k\\\\dim' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:dim\([^)]*\)\s*\(k\+h\^|dim\([^)]*\)\s*k/(2h\^|\\dim\s*\\fg.*k\+h\^|\\dim\s*\\fg.*k/(2h\^|\\frac\{\\dim\([^}]+\)k\}|\\frac\{k\\dim)
                                                ^
error: unclosed group
 exited 2 in 52ms:
rg: regex parse error:
    (?:(?<![A-Za-z])\\kappa\([^)]*Kac|\\kappa\([^)]*\\widehat|\\kappa\([^)]*\\fg|\\kappa\([^)]*\\mathfrak\{g\})
       ^^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'H_\\{N-1\\}.*kappa|kappa.*H_\\{N-1\\}|\\\\kappa\\(["'^)]*W[''^)]*'"\\).*H_\\{N-1\\}|H_N - 1|H_N-1' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:110:% W_N kappa formula: kappa_ch(W_N^k) = c(W_N^k) * (H_N - 1) where
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:120:$\mathcal{W}_N^k$ ($\mathfrak{sl}_N$) & $c$ & $c(H_N - 1)$ &
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:121: $H_N - 1 = \sum_{j=1}^{N-1} 1/(j+1)$ \\
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:167:$\mathcal{W}_N^k$ & $(H_N - 1) K_N / 2$ & $K_N$
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:333: \kappa_{\mathrm{ch}}(\mathcal{W}_N) = c \cdot (H_N - 1),
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:336:As $N \to \infty$, $H_N - 1 \sim \log N + \gamma - 1$ diverges, and
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:570: $\varrho = H_N - 1 \to \infty$. The formulas disagree for the
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:250:Here $K_N = 4N^3 - 2N - 2$ and $\varrho_N = c \cdot (H_N - 1)/ c =
/Users/raeez/calabi-yau-quantum-groups/notes/theory_qvcg_koszul.tex:251:H_N - 1$ where $H_N = \sum_{i=1}^N 1/i$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:633:$K_N/c^*_N = 2(H_N - 1)$ equals~$1$ only at $N = 2$ (where
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:840:Here $K_{\mathcal{W}_N} = \kappa + \kappa^! = (H_N - 1)\alpha_N$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:856:\;=\; (H_N - 1)\,\alpha_N,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:860:$K_N/c_N^* = 2(H_N - 1)$ equals~$1$ if and only if $N = 2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:867:$\kappa(\mathcal{W}_{N,c}) = c\,(H_N - 1)$, where $H_N - 1
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:872:$\kappa(\mathcal{W}_{N,\alpha_N - c}) = (\alpha_N - c)(H_N - 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:873:The sum is $K_N = \alpha_N(H_N - 1)$, independent of~$c$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:874:The ratio $K_N/c_N^* = 2(H_N - 1) = 1$ iff $H_N = 3/2$, which
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:896:the curvature $\kappa(\cW_{N,c^*}) = c^*(H_N - 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:897:= \tfrac{1}{2}\alpha_N(H_N - 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1240:= (H_N - 1) \cdot \alpha_N$, where $H_N = \sum_{j=1}^N 1/j$

thinking
**Improving search strategies**

I need to refine my search for the KM formula by using simpler patterns. It seems like looking for occurrences of `(k+h` might be more effective than `k/`. I think I could try using `rg -n "\\kappa\\([^)]*\\) = .*k"` to pinpoint relevant formulas as well. Additionally, I should consider looking for any incorrect formulas in the current repository by searching `k/(2h` in all the tex files.
codex
I’ve finished the first-pass sweep: the `\mathcal W_N` surfaces are overwhelmingly consistent, including the `H_N-1` guardrails. I’m now pressure-testing the affine KM surfaces for dropped `+h^\vee` shifts and narrowing Vol III to genuine AP113 violations rather than unrelated `\kappa` parameters.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'k/(2h\\"'^|k'"\\}/\\{2h\\"'^|'"\\\\frac\\{["'^}]*k[''^}]*'"\\}\\{2h\\"'^|dim'"\\(["'^)]*'"\\)k/(2h\\"'^|'"\\\\dim\\(["'^)]*'"\\)k/(2h\\"'^|'"\\\\frac\\{\\\\dim\\(["'^)]*'"\\)k\\}\\{2h\\"'^'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'Bare\\~?\\\\kappa|bare \\\\kappa|Bare \\\\kappa|unqualified.*\\\\kappa|without subscript|AP113|\\\\kappa_[A-Za-z]+' /Users/raeez/calabi-yau-quantum-groups/main.tex /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/notes /Users/raeez/calabi-yau-quantum-groups/working_notes.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\kappa\\(["'^)]*(V_k|'"\\\\widehat\\{|\\\\mathfrak\\{sl\\}_2|\\\\fg|Kac--Moody|affine)' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:k/(2h\^|k\}/\{2h\^|\\frac\{[^}]*k[^}]*\}\{2h\^|dim\([^)]*\)k/(2h\^|\\dim\([^)]*\)k/(2h\^|\\frac\{\\dim\([^)]*\)k\}\{2h\^)
                                                                    ^
error: unclosed group
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:1143:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:59:case where the Heisenberg subalgebra of $W_{1+\infty}$ at self-dual level $c = 1$ gives $\kappa_{\mathrm{ch}}(\mathcal{H}_1) = 1$ (the Virasoro channel alone gives $\kappa_T = c/2 = 1/2$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty})$ diverges);
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:339:$\kappa_j = c/j$ for the spin-$j$ generator. The physically
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:347: \kappa_T = \frac{1}{2}, \quad
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:351:The stress-energy channel alone gives $\kappa_T = c/2 = 1/2$.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:364:The finite and well-defined quantity is $\kappa_T = c/2$. For
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:365:$c = 1$, $\kappa_T = 1/2$. This is the modular characteristic of
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:378: match $\kappa_T = 1/2$.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:399: = \frac{\kappa_T}{24} \cdot \frac{1}{\varrho(\mathrm{Vir})}
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:400: = \frac{\kappa_T}{\varrho \cdot 24}.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:527:The complementarity constraint $\kappa_N + \kappa_N'$ for each of these
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:909:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80: \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:86: \kappa_s = \frac{c}{s} = \frac{1}{s},
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:88: \kappa_s^{\mathrm{eff}} = s \cdot \kappa_s = 1 \quad \text{(constant per MacMahon level)}.
 succeeded in 51ms:
Total output lines: 410

/Users/raeez/chiral-bar-cobar-vol2/compute/audit/non_simply_laced_rmatrix_report.tex:149:$\kappa(V_k, k{=}1)$ & $20/3$ & $20/3$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:465:$\kappa(\widehat{\fg}_k)
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:468:$\kappa(\widehat{\fg}_k) + \kappa(\widehat{\fg}_{-k-2h^\vee})
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:977:$\kappa(\widehat{\fg}_k) = \dim\fg\,(k + h^\vee)/(2h^\vee)$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:978:Feigin--Frenkel: $\kappa(\widehat{\fg}_k)
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:979:+ \kappa(\widehat{\fg}_{-k-2h^\vee}) = 0$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1249:  characteristic $\kappa = \kappa(V_k(\fg))
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1302:$\kappa(V_k(\fg)) = \dim(\fg)(k + h^\vee)/(2h^\vee)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2321:    \kappa(V_k(\mathfrak{sl}_2)) \cdot \lambda_1
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2559:  $\kappa' = \kappa(V_{-k-4}(\mathfrak{sl}_2))
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3756:  $\kappa(\fg) + \kappa(\fg)^! = 0$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3759:  $\kappa(V_k(\fg)) = \dim(\fg)(k + h^\vee)/(2h^\vee)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3767:  & $\kappa(V_k(\fg))$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4169:  $\kappa(N{=}2) = \kappa(\widehat{\mathfrak{sl}}_{2,k})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4170:  + \kappa(\psi\bar\psi) - \kappa(\widehat{U(1)})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:744:\kappa(\widehat{\mathfrak{sl}}_2, k) = \frac{3(k + 2)}{4},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:749:\kappa(\widehat{\mathfrak{sl}}_{2,k})
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:750:+ \kappa(\widehat{\mathfrak{sl}}_{2,-k-4}) = 0.

thinking
**Searching for patterns**

I’m looking into the pattern `\dim(\mathfrak g)\cdot k/(2h^\vee)` in the current repository and making a note of it. However, it seems like I might be mistaken unless I’m considering it explicitly as a double-pole channel. I really want to make sure I get this right, so I should search more targeted information to clarify my understanding! Let’s keep exploring this and check back to ensure everything aligns correctly.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'dim\\(\\\\mathfrak\\{g\\}\\)\\s*\\\\cdot\\s*k/(2h\\"'^'"\\\\vee)|dim\\(\\\\fg\\)\\s*\\\\cdot\\s*k/(2h\\"'^'"\\\\vee)|\\\\frac\\{\\\\dim\\(\\\\mathfrak\\{g\\}\\)\\\\cdot k\\}\\{2h\\"'^'"\\\\vee\\}|\\\\frac\\{k\\\\dim\\(\\\\mathfrak\\{g\\}\\)\\}\\{2h\\"'^'"\\\\vee\\}|\\\\frac\\{k\\\\dim\\\\mathfrak\\{g\\}\\}\\{2h\\"'^'"\\\\vee\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1890,1935p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '900,925p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '72,95p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '330,370p' /Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
structure of~$L_0$ with the adjoint representation
of~$\mathfrak{g}$. The bar differential has leading term
$d_2(sa\,|\,sb) = s[a,b]$, so $l_2$ on generators is the adjoint
bracket. The invariant form on $\widehat{\mathfrak{g}}_k$ is
$\kappa_k$, which restricts to the level-$k$ normalized Killing
form on~$\mathfrak{g}$.

(ii)\enspace
On the adjoint representation, $C_2 = \sum_i \mathrm{ad}(e_i)
\circ\mathrm{ad}(e^i)$ has eigenvalue~$2h^\vee$ (standard: the
Casimir eigenvalue on the adjoint representation equals twice the
dual Coxeter number for simple~$\mathfrak{g}$).

(iii)\enspace
By Proposition~\ref{prop:cyclic-ce-identification},
$H^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g})\cong
H^3(\mathfrak{g})\cong\mathbb{C}$, generated by the Killing
$3$-cocycle $\phi(a,b,c)=\kappa_{\mathfrak{g}}([a,b],c)$. This is the unique
infinitesimal cyclic deformation direction: it defines
an~$l_3$ bracket on~$L_0$ satisfying all homotopy Jacobi
 succeeded in 51ms:
\end{enumerate}
The shadow tower is class~$\mathbf{G}$ (Gaussian, $r_{\mathrm{max}} = 2$): $C = 0$, $Q = 0$, $\Delta = 8\kappa_{\mathrm{ch}} S_4 = 0$.

\noindent\textit{Verification}: 115 tests in \texttt{c3\_grand\_verification.py}; 98 tests in \texttt{c3\_shadow\_tower.py}.
\end{theorem}


\begin{remark}[Per-channel $\kappa_{\mathrm{ch}}$ and MacMahon decomposition]
\label{rem:c3-per-channel}
The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.

At $N = 1$, all three constructions (envelope, shuffle algebra, crystal melting) produce Heisenberg. The CoHA character is $M(q)$ (plane partitions), exceeding the $\cW$-algebra character $P(q)$ (ordinary partitions):
\[
 \frac{M(q)}{P(q)} \;=\; \prod_{n \geq 2}(1-q^n)^{-(n-1)}.
\]
This ratio counts the higher-spin contributions.

\noindent\textit{Verification}: 87 tests in \texttt{c3\_envelope\_comparison.py}; 50 tests in \texttt{macmahon\_shadow\_decomposition.py}.
\end{remark}

 succeeded in 51ms:
 \frac{1}{M(q)},
 \qquad
 M(q) = \prod_{n \geq 1} \frac{1}{(1-q^n)^n}.
 \]
 \item The modular characteristic is $\kappa_{\mathrm{ch}} = 1$, verified by five independent paths:
 \begin{enumerate}[label=(\alph*)]
 \item genus-$1$ free energy: $F_1 = \kappa_{\mathrm{ch}} / 24 = 1/24$;
 \item degree-$0$ MacMahon exponent: $\log M(q) = \sum \sigma_2(k) q^k / k$ matches $\kappa_{\mathrm{ch}} = 1$;
 \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
 \item Hodge-theoretic: via the categorical trace $\chi^{\CY}(\mathrm{Perf}(\mathbb{C}^3))$;
 \item complementarity: $\kappa_{\mathrm{ch}}(\mathbb{C}^3) + \kappa_{\mathrm{ch}}(\text{dual}) = 0$ (free-field anti-symmetry).
 \end{enumerate}
 \item Per-channel modular characteristics: for the spin-$s$ channel of $W_{1+\infty}$,
 \[
 \kappa_s = \frac{c}{s} = \frac{1}{s},
 \qquad
 \kappa_s^{\mathrm{eff}} = s \cdot \kappa_s = 1 \quad \text{(constant per MacMahon level)}.
 \]
 This constancy is the shadow-DT Rosetta stone: each energy level contributes equally to the modular characteristic, and the MacMahon function $M(q) = \prod (1 - q^n)^{-n}$ is the partition function of a system with effective $\kappa_{\mathrm{ch}} = 1$ per energy level.
\end{enumerate}
 succeeded in 51ms:

From Vol~I, the modular characteristic of $\mathcal{W}_N$ is
\begin{equation}\label{eq:kappa-wn}
 \kappa_{\mathrm{ch}}(\mathcal{W}_N) = c \cdot (H_N - 1),
 \qquad H_N = \sum_{j=1}^N \frac{1}{j}.
\end{equation}
As $N \to \infty$, $H_N - 1 \sim \log N + \gamma - 1$ diverges, and
the total $\kappa_{\mathrm{ch}}(\mathcal{W}_\infty)$ diverges with it. However,
the \emph{per-channel} modular characteristics are finite:
$\kappa_j = c/j$ for the spin-$j$ generator. The physically
meaningful quantity is the modular characteristic at fixed central
charge.

At the \emph{self-dual level} $c = 1$ (corresponding to a single free
boson, the simplest realization), the individual channel contributions
are
\begin{equation}\label{eq:kappa-channels-c1}
 \kappa_T = \frac{1}{2}, \quad
 \kappa_{W^{(3)}} = \frac{1}{3}, \quad
 \kappa_{W^{(4)}} = \frac{1}{4}, \quad \ldots


thinking
**Identifying formula inconsistencies**

I see that volume III uses kappa_s and kappa_T, and if AP113 only approved subscripts, that could lead to issues. I need to find any incorrect formulas in writable Volume I. I found one suspicious formula in `chiral_hochschild_koszul.tex`, but its context mentions an ambiguous use of the same symbol for different contributions. This could be a real problem, so I think I might need to rename terms for clarity and ensure truthful edits. I’ll look for other similar ambiguities as well.
thinking
**Exploring double-pole channels**

I think I need to search for references to the "double-pole channel" along with the kappa symbol. Specifically, I should look for patterns like `\kappa.*double-pole`. This will help me track down any relevant formulas or instances where the double-pole might be discussed. So let's see what I find in the results and make sure everything aligns correctly with my previous findings. It’s crucial to clarify any ambiguities I come across!
exec
/bin/zsh -lc "sed -n '1914,1928p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '936,960p' standalone/survey_modular_koszul_duality_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '420,435p' standalone/survey_track_a_compressed.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'double-pole channel|simple-pole channel|Sugawara shift|\\\\kappa_\\{\\\\mathrm\\{dp\\}\\}|\\\\kappa_\\{dp\\}|\\\\kappa\\(\\\\widehat\\{\\\\mathfrak\\{g\\}\\}_k\\) = .*k/(2h\\"'^'"\\\\vee)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(viii)--(ix) confirm this independently for
$\mathfrak{sl}_2$, $\mathfrak{sl}_3$,
$\mathfrak{sp}_4$, and~$\mathfrak{g}_2$.

(iv)\enspace
The two-channel decomposition extracts
$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
double-pole channel and $\dim(\mathfrak{g})/2$ from the
simple-pole channel. Their sum gives
$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
formula of Theorem~\ref{thm:modular-characteristic}.
\end{proof}

\begin{definition}[Cyclic deformation complex: bar-intrinsic
 form]
 succeeded in 51ms:
\medskip
\noindent\textbf{Curvature computation: Kac--Moody.}\enspace
For $\widehat{\fg}_k$, the curvature receives the
trace over the adjoint representation:
\[
\kappa(\widehat{\mathfrak g}_k)=\frac{(k+h^\vee)\dim\mathfrak g}{2h^\vee}.
\]
The derivation proceeds by the averaging map identity. In the
trace-form convention, the $r$-matrix is $r^{\mathrm{KM}}(z)=k\Omega/z$,
where $\Omega=\sum_a t^a\otimes t^a$ is the Casimir of the Killing
form (at $k=0$, $r=0$; correct). The double-pole channel
gives $\mathrm{av}(r(z))=k\dim\fg/(2h^\vee)$. The simple-pole
self-contraction through the adjoint Casimir eigenvalue $2h^\vee$
contributes an additional $\dim\fg/2$. Together:
\[
\kappa(\widehat\fg_k)=\underbrace{\frac{k\dim\fg}{2h^\vee}}_{\text{double-pole}}+\underbrace{\frac{\dim\fg}{2}}_{\text{simple-pole Sugawara shift}}=\frac{(k+h^\vee)\dim\fg}{2h^\vee}.
\]
Sanity checks: $k=0$ gives $\kappa=\dim\fg/2$ (not zero; the
Lie bracket persists and the simple-pole channel contributes).
$k=-h^\vee$ gives $\kappa=0$ (critical level: Sugawara undefined,
 succeeded in 51ms:
the level-full Casimir form
\[
r(z)\;=\;k\,\Omega/z,\qquad\Omega=\sum_a J^a\otimes J_a
\]. Averaging collapses the Casimir
to its trace:
\[
\mathrm{av}(k\Omega/z)\;=\;\frac{k\dim\mathfrak g}{2h^\vee}\;=\;\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k),
\qquad
\kappa(\widehat{\mathfrak g}_k)\;=\;\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)+\frac{\dim\mathfrak g}{2}.
\]
The Casimir tensor structure, invisible to~$\kappa$, is the data
that builds the Yangian.

\subsection*{1.8.\enspace The Kac--Moody OPE}

The affine Kac--Moody algebra $\widehat{\mathfrak g}_k$ has OPE
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/main.tex:1235:% obs_g = kappa * lambda_g for Heisenberg; Sugawara shift for Kac--Moody.
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:537:\;=\;\kappa_{\mathrm{dp}},
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:540:\;=\;\kappa_{\mathrm{dp}}+\frac{\dim\fg}{2}
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:543:The $\dim(\fg)/2$ term is the Sugawara shift: the
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:2523:Sugawara shift:
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:2525:\mathrm{av}(k\,\Omega/z)=\frac{k\dim\fg}{2h^\vee}=\kappa_{\mathrm{dp}},
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/survey_v2_xr.tex:2527:\kappa(\widehat\fg_k)=\kappa_{\mathrm{dp}}+\frac{\dim\fg}{2}
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:719:scalar; together with the Sugawara shift by the dual Coxeter
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2999:scalar, and the Sugawara shift by the dual Coxeter number~$h^\vee$
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:4076:$\mathrm{av}(r(z)) = \kappa_{\mathrm{dp}}
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1921:double-pole channel and $\dim(\mathfrak{g})/2$ from the
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1922:simple-pole channel. Their sum gives
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:2286:  the Sugawara shift).
/Users/raeez/chiral-bar-cobar/staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:9015:genus~$0$. The agreement is forced: the Sugawara shift
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:918:constants~$f^{ab}{}_c$ (the ``simple-pole channel'').
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:944:Only the double-pole channel contributes (the structure constants
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:953:Only the simple-pole channel contributes (the Killing form
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1000:\emph{Step~1: Curvature from the double-pole channel.}\enspace
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1018:\emph{Step~2: Curvature from the simple-pole channel.}
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1038:Normalizing by $2h^\vee = 4$, the simple-pole channel
exec
/bin/zsh -lc "sed -n '5046,5053p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1339,1361p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1508,1518p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 $l_2$ bracket and the cyclic pairing, acts as $2h^\vee\cdot\operatorname{id}$
 on the generators. From this:
 $\kappa(\cA) = \dim(\mathfrak{g})\cdot(k+h^\vee)/(2h^\vee)$.
 For $\mathfrak{sl}_2$ at level~$k$, the two-channel decomposition
 gives $\kappa = 3k/4$ (double-pole channel) $+ 3/2$
 (simple-pole channel) $= 3(k+2)/4$,
 matching the explicit genus-$2$ computation
 (Theorem~\ref{thm:sl2-genus2-curvature}).
 succeeded in 51ms:
\begin{definition}[Double-pole and simple-pole channel
decomposition]\label{def:channel-decomposition}
\index{channel decomposition!double-pole/simple-pole}
\index{modular characteristic!channel decomposition}
For $\widehat{\fg}_k$ with $\fg$ simple, the modular
characteristic $\kappa(\widehat{\fg}_k) =
\dim(\fg)(k + h^\vee)/(2h^\vee)$
(Theorem~\ref{thm:modular-characteristic}) decomposes into
\emph{double-pole} and \emph{simple-pole} channels:
\begin{equation}\label{eq:kappa-dp-sp}
\kappa = \kappa_{\mathrm{dp}} + \kappa_{\mathrm{sp}},
\qquad
\kappa_{\mathrm{dp}}
:= \frac{k \cdot \dim\fg}{2h^\vee},
\qquad
\kappa_{\mathrm{sp}}
:= \frac{\dim\fg}{2}.
\end{equation}
Here $\kappa_{\mathrm{dp}}$ is the vacuum leakage from the
double-pole OPE term $k(J^a, J^b)/(z-w)^2$ (the level
 succeeded in 52ms:
\notag \\
&= \frac{k + h^\vee}{2h^\vee}\cdot\dim(\fg).
\label{eq:km-dfib-squared-trace}
\end{align}
Equivalently: the double-pole channel contributes
$\kappa_{\mathrm{dp}} = k\cdot\dim(\fg)/(2h^\vee)$
and the simple-pole channel contributes
$\kappa_{\mathrm{sp}} = \dim(\fg)/2$
(the self-contraction trace
$h^\vee\cdot\dim(\fg)/(2h^\vee) = \dim(\fg)/2$),
recovering~\eqref{eq:kappa-dp-sp}. Therefore:
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\kappa\\(["'^)]*'"\\) = ["'^'"\\n]*k/(2h\\"'^'"\\\\vee)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Investigating regex issues**

I'm thinking there might be a regex mismatch due to backslashes. It could be beneficial to try using a fixed string instead. I'll need to search for `k/(2h^\vee)` across the repository to see how it's appearing. This should help me pinpoint where the problem lies so I can adjust accordingly. I hope this approach leads me to the right solution!
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'k/(2h\\"'^'"\\\\vee)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Their sum gives|extracts.*double-pole channel|double-pole channel\\) \\+' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/standalone" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1922:simple-pole channel. Their sum gives



thinking
**Inspecting Volume III Issues**

I need to focus on the main live surfaces of Volume III, especially regarding AP113 issues. I'll search for specific files and see where terms like κ_s appear. There are candidates in chapters like "cy_to_chiral.tex" and "bar_cobar_bridge.tex" that use κ_s. I also see some notes mentioning κ_j, κ_T, and κ_N that may not be approved. I wonder if I should report these chapter hits and mention the notes as well, given the user's interest in all three volumes.
thinking
**Considering Cross-Volume Inconsistencies**

I’m thinking about creating a note in the current repository to summarize any blocked cross-volume inconsistencies. But since the user specifically asked to only edit assigned files, I wonder if creating a new note might not align with that guideline. I need to be cautious here. I also contemplate checking if there are any issues in Volume II related to AP113. It seems there might not be any, but I’ll verify if Volume III has the KM and W_N formula in the relevant chapters.
thinking
**Searching for KM in Volume III**

I need to look for the Kac-Moody formula in Volume III chapters. A promising candidate is the `notes/physics_anomaly_cancellation.tex` file, particularly around lines 103-125. I'll check those lines to confirm if the formula is there. It's important to ensure I read the context properly to avoid missing any relevant details. Let's dive into that section and see what we find related to KM!
codex
The affine KM sweep found one genuine wording error in Vol I: a theorem proof reused full `\kappa` for the double-pole contribution before adding the Sugawara term. Vol II’s explicit KM and `\mathcal W_N` family formulas look clean; the remaining drift is in Vol III notation, where per-channel modular characteristics are written with non-approved subscripts like `\kappa_s` and `\kappa_T`.
exec
/bin/zsh -lc "sed -n '100,128p' /Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '236,246p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '122,136p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '374,386p' /Users/raeez/calabi-yau-quantum-groups/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
where $\lambda_g^{\mathrm{FP}}$ is the Faber--Pandharipande evaluation.
At genus~1: $F_1 = \kappa_{\mathrm{ch}}/24$.

\subsection{The master table of $\kappa_{\mathrm{ch}}$ values}

The anomaly ratio $\varrho(\mathcal{A}) := \kappa_{\mathrm{ch}}(\mathcal{A})/c(\mathcal{A})$
encodes how much of the conformal anomaly survives:
\begin{center}
%: kappa values verified against Vol I landscape_census.tex.
% Heisenberg rank d level 1: c = d, kappa_ch = d, rho = 1.
% W_N kappa formula: kappa_ch(W_N^k) = c(W_N^k) * (H_N - 1) where
% H_N = sum_{j=1}^{N} 1/j is the harmonic number.
\begin{tabular}{lccc}
\textbf{Algebra} & $c$ & $\kappa_{\mathrm{ch}}$ & $\varrho$ \\ \hline
$\mathcal{H}^{\oplus d}$ (Heisenberg, rank $d$, level 1) & $d$ & $d$ & $1$ \\
$\widehat{\mathfrak{g}}_k$ (Kac--Moody) &
 $\frac{k \dim\mathfrak{g}}{k+h^\vee}$ &
 $\frac{(k+h^\vee)\dim\mathfrak{g}}{2h^\vee}$ &
 $\frac{(k+h^\vee)^2}{2kh^\vee}$ \\
$\mathrm{Vir}_c$ (Virasoro) & $c$ & $c/2$ & $1/2$ \\
 succeeded in 51ms:
 \]
 as a direct sum of $\pm 1$ eigenspaces for the Verdier involution induced by Serre duality on $D^b(\Coh(\cC))$. This is unconditional in the CY$_2$ case.
\end{enumerate}
\begin{enumerate}[label=\textup{(C2$^{\mathrm{CY}}$)}]
 \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes),
 \[
 \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}.
 \]
 Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
\end{enumerate}
\end{theorem}

\begin{proof}[Sketch]
(C1$^{\mathrm{CY}}$): the eigenspace decomposition is the $\Phi$-image of Vol~I Theorem~C1. The functor $\Phi$ is compatible with the Verdier involution (Chapter~\ref{ch:cy-to-chiral}, Proposition on Serre-functor intertwining), so the direct sum decomposition of Vol~I pulls back to a decomposition of $Q_g^n(A_\cC) \oplus Q_g^n(A_{\cC^!})$ indexed by Serre eigenvalues.

 succeeded in 51ms:
\begin{proof}[Attribution]
Parts (i), (iii), (iv) are Vol~I/II results (\S\ref{sec:k3e-cross-volume}, items K3-1 through K3-13, proved in the K3 modular-tower chapter of Vol~I and in Part~III of Vol~II's 3D quantum gravity treatment). Part (ii) is the Borcherds lift of Borcherds (1998); its use as a modular characteristic is the observation of AP-CY8, not a theorem of Vol~III. The conditionality propagates from Theorem~\ref{thm:cy-shadow-cohft}.
\end{proof}

\begin{remark}[Kappa-spectrum verification for $K3 \times E$]
\label{rem:kappa-spectrum-k3xe-bridge}
Substitute $d = 2$ for $K3$ into the CY-D formula $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$: this gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2$. Tensor-product additivity (Proposition~\ref{prop:kappa-non-multiplicative}) for the chiral de Rham complex then determines $\kappa_{\mathrm{ch}}(K3 \times E) = 3$ (namely, the value $2$ for $K3$ combined additively with the value $1$ for the elliptic curve $E$ yields $3$). Note: this is additivity of the modular characteristic under product factorization, not the Koszul-dual scalar sum of Theorem~\ref{thm:cy-complementarity-d2} (C2$^{\mathrm{CY}}$); the two operations are distinct and should not be confused. The value $\kappa_{\mathrm{BKM}} = 5$ is the Borcherds weight, independently equal to half the weight of $\Phi_{10}$; this corresponds to the BKM superalgebra $\mathfrak{g}_{\Delta_5}$, not to the chiral algebra of $K3 \times E$. The four members of the spectrum $\{\kappa_{\mathrm{cat}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \kappa_{\mathrm{fiber}}\} = \{2, 3, 5, 24\}$ each arise from a distinct chiral algebraization: bare kappa is forbidden in Vol~III.
\end{remark}

\subsection{Toric CY$_3$ and the DT CohFT}

 succeeded in 51ms:
$\kappa_{\mathrm{ch}} = 3$
(chiral shadow from the Vol~I shadow tower),
$\kappa_{\mathrm{BKM}} = 5$
(Borcherds weight of the Igusa cusp form~$\Delta_5$,
so $\mathrm{wt}(\Phi_{10}) = 2\kappa_{\mathrm{BKM}}$),
$\kappa_{\mathrm{fiber}} = 24$
(lattice rank).
Bare~$\kappa$ is forbidden; the subscript records the
geometric provenance.
For $d \geq 3$ the CY chiral algebra is $\Eone$;
the effective framing obstruction
$\Obs_{\mathrm{eff}}(d) \in \pi_d(BU)$ or $\pi_d(B\Sp)$
is $8$-periodic by Bott periodicity and trivial when
codex
A concrete Vol III formula drift surfaced in [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex): the text describes the `\mathcal W_N` complementarity sum as `c(H_N-1)`, but the sum should be the conductor-weighted quantity `(c+c')(H_N-1)=K_N(H_N-1)`. I’m checking whether that wording repeats elsewhere in Vol III before I patch the writable Vol I side and document the blocked Vol III fixes.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\kappa_[sTNj]|\\\\kappa_s|\\\\kappa_T|\\\\kappa_N|\\\\kappa_j' /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'scalar sum .*c ?\\\\cdot ?\\(H_N - 1\\)|scalar sum .*c ?\\(H_N - 1\\)|for \\\\cW_N.*c ?\\\\cdot ?\\(H_N - 1\\)|for \\\\cW_N.*c ?\\(H_N - 1\\)|equals c ?\\\\cdot ?\\(H_N - 1\\)|equals c ?\\(H_N - 1\\)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'W_N.*H_\\{N-1\\}|H_\\{N-1\\}.*W_N|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\mathcal\\{W\\}_N\\).*H_\\{N-1\\}|\\\\kappa\\(\\\\mathcal\\{W\\}_N\\).*H_\\{N-1\\}' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80: \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:86: \kappa_s = \frac{c}{s} = \frac{1}{s},
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:88: \kappa_s^{\mathrm{eff}} = s \cdot \kappa_s = 1 \quad \text{(constant per MacMahon level)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:909:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168: \item Under the CY uniform-weight hypothesis (which is \emph{not} generically satisfied for compact CY$_3$: the chiral de Rham complex has fields in weights $\{1/2, 1, 3/2, 2, \ldots\}$), and scope (the Koszul conductor is family-dependent: free-field/KM gives $K = 0$, Virasoro gives $K = 26$ with scalar sum $13$, $\cW_N$ gives $K_N = 4N^3 - 2N - 2$ with scalar sum $c (H_N - 1)$),
 exited 1 in 52ms:



thinking
**Identifying Vol III Issues**

I’m looking at some issues in Vol III. First, in modular_koszul_bridge.tex line 130, the complementarity sum should say c(H_N-1) instead of K_N(H_N-1). Then, the scalar sum in line 168 needs a similar fix. I also see AP113 notation concerns in bar_cobar_bridge.tex and cy_to_chiral.tex with references to subscripts like `\kappa_s`. These seem to be non-approved in the current chapters. I need to determine if there are any bare κ in these volumes.
thinking
**Assessing kappa notation**

I’m considering whether `higher_genus_modular_koszul.tex:5050` should use `kappa = 3k/4` as a partial double-pole expression. It could work, but to maintain consistency, I might introduce `\kappa_{\mathrm{dp}}`. The user asked specifically about "kappa(KM)" concerning the Sugawara shift. It might be okay to leave the expression as it is since it's explicit, but tightening it sounds better. I could edit to reflect `\kappa_{\mathrm{dp}} = 3k/4` and `\kappa_{\mathrm{sp}} = 3/2` if necessary. I'll also check for related lines to avoid confusion.
codex
Before the edit, I’m locking the formula against the census and the cross-volume surface.

```text
PE-2: kappa formula write
family: affine KM
kappa written: kappa_dp(\widehat{\mathfrak g}_k) = dim(\mathfrak g) k/(2h^\vee), and kappa(\widehat{\mathfrak g}_k) = dim(\mathfrak g)(k+h^\vee)/(2h^\vee)
census: chapters/examples/landscape_census.tex:32-34, 88-117 = kappa(V_k(\mathfrak g)) = dim(\mathfrak g)(k+h^\vee)/(2h^\vee) with double-pole part separated from the Sugawara shift
match? Y
at k=0: dim(\mathfrak g)/2 expected dim(\mathfrak g)/2
at k=-h^\vee (KM): 0 expected 0
at c=13 (Vir): NA
AP136 (W_N N=2): NA
wrong variants avoided: NOT dim(\mathfrak g)k/(2h^\vee) as the full kappa; NOT c/2; NOT H_{N-1}
verdict: ACCEPT
```

```text
PE-8: cross-volume formula
formula: affine KM kappa decomposition into double-pole contribution plus Sugawara shift
Vol I: explicit kappa_dp / kappa_sp decomposition in chapters/examples/kac_moody.tex:1339-1361, 1508-1518; one ambiguous proof line in chapters/theory/chiral_hochschild_koszul.tex:1919-1923
Vol II: canonical full formula only; no dropped shift found on explicit family surfaces
Vol III: complementarity wording drift in chapters/connections/modular_koszul_bridge.tex:130,168; AP113-style per-channel notation drift in chapters/theory/cy_to_chiral.tex:909 and chapters/connections/bar_cobar_bridge.tex:80-88
consistent? N
canonical vol: Vol I landscape_census + Kac--Moody chapter
others updated same session? Vol I yes; Vol II no change needed; Vol III blocked by sandbox permissions
convention conversion: OPE/bridge only; applied Y
verdict: ACCEPT
```

I’m editing the one writable ambiguous KM line now, then I’ll re-grep the bad variants and report the blocked Vol III fixes explicitly.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex
@@ -1919,6 +1919,7 @@
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex
file update:
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 65da7b71836ccd80a9f893ee8345d5f31ae436ca..d549cf8dde796adb7aa3899224c31d8281236f58
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -1917,10 +1917,11 @@
 
 (iv)\enspace
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
 \end{proof}
 

file update:
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 65da7b71836ccd80a9f893ee8345d5f31ae436ca..d549cf8dde796adb7aa3899224c31d8281236f58
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -1917,10 +1917,11 @@
 
 (iv)\enspace
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
 \end{proof}
 

codex
The patch is in. I’m doing a narrow falsification pass now: negative grep for the dropped-shift KM variant, negative grep for `H_{N-1}` on `\mathcal W_N`, and a focused Vol III re-grep so the blocked issues are precise rather than hand-wavy.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1916,1926p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\kappa\\(\\\\widehat\\{\\\\mathfrak\\{g\\}\\}_k\\) = \\\\dim\\(\\\\mathfrak\\{g\\}\\)\\\\cdot k/\\(2h\\"'^'"\\\\vee\\)|\\\\kappa\\(\\\\widehat\\{\\\\fg\\}_k\\) = \\\\dim\\(\\\\fg\\)\\\\cdot k/\\(2h\\"'^'"\\\\vee\\)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'W_N.*H_\\{N-1\\}|H_\\{N-1\\}.*W_N|\\\\kappa\\(\\\\mathcal\\{W\\}_N\\).*H_\\{N-1\\}|\\\\kappa_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\mathcal\\{W\\}_N\\).*H_\\{N-1\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1916	$\mathfrak{sp}_4$, and~$\mathfrak{g}_2$.
  1917	
  1918	(iv)\enspace
  1919	The two-channel decomposition extracts
  1920	$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
  1921	double-pole channel and $\dim(\mathfrak{g})/2$ from the
  1922	simple-pole channel. Their sum gives
  1923	$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
  1924	= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
  1925	formula of Theorem~\ref{thm:modular-characteristic}.
  1926	\end{proof}
 exited 1 in 51ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex | sed -n '78,89p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '906,912p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '126,171p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   906	
   907	\begin{remark}[Per-channel $\kappa_{\mathrm{ch}}$ and MacMahon decomposition]
   908	\label{rem:c3-per-channel}
   909	The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
   910	
   911	At $N = 1$, all three constructions (envelope, shuffle algebra, crystal melting) produce Heisenberg. The CoHA character is $M(q)$ (plane partitions), exceeding the $\cW$-algebra character $P(q)$ (ordinary partitions):
   912	\[
 succeeded in 52ms:
    78	 \item genus-$1$ free energy: $F_1 = \kappa_{\mathrm{ch}} / 24 = 1/24$;
    79	 \item degree-$0$ MacMahon exponent: $\log M(q) = \sum \sigma_2(k) q^k / k$ matches $\kappa_{\mathrm{ch}} = 1$;
    80	 \item channel decomposition: $\sum_{s \geq 1} \kappa_s^{\mathrm{eff}} = \sum_{s \geq 1} s \cdot (1/s) = \sum 1 = +\infty$ (at finite $N$, $\kappa_{\mathrm{ch}}(W_N) = c(H_N - 1)$; the total $\kappa_{\mathrm{ch}}(W_{1+\infty}, c=1) = \kappa_{\mathrm{ch}}(H_1) = 1$);
    81	 \item Hodge-theoretic: via the categorical trace $\chi^{\CY}(\mathrm{Perf}(\mathbb{C}^3))$;
    82	 \item complementarity: $\kappa_{\mathrm{ch}}(\mathbb{C}^3) + \kappa_{\mathrm{ch}}(\text{dual}) = 0$ (free-field anti-symmetry).
    83	 \end{enumerate}
    84	 \item Per-channel modular characteristics: for the spin-$s$ channel of $W_{1+\infty}$,
    85	 \[
    86	 \kappa_s = \frac{c}{s} = \frac{1}{s},
    87	 \qquad
    88	 \kappa_s^{\mathrm{eff}} = s \cdot \kappa_s = 1 \quad \text{(constant per MacMahon level)}.
    89	 \]
 succeeded in 50ms:
   126	 \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes),
   127	 \[
   128	 \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}.
   129	 \]
   130	 Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
   131	\end{enumerate}
   132	\end{theorem}
   133	
   134	\begin{proof}[Sketch]
   135	(C1$^{\mathrm{CY}}$): the eigenspace decomposition is the $\Phi$-image of Vol~I Theorem~C1. The functor $\Phi$ is compatible with the Verdier involution (Chapter~\ref{ch:cy-to-chiral}, Proposition on Serre-functor intertwining), so the direct sum decomposition of Vol~I pulls back to a decomposition of $Q_g^n(A_\cC) \oplus Q_g^n(A_{\cC^!})$ indexed by Serre eigenvalues.
   136	
   137	(C2$^{\mathrm{CY}}$): under uniform weight, Vol~I Theorem~C2 gives $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for the Heisenberg/free-field classes. For K3, $\cA_{K3}$ is the $\cN = 4$ superconformal algebra with $c = 6$, and all generators sit at conformal weights $\{1/2, 1, 3/2, 2\}$; the uniform-weight lane of interest is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$, where $\kappa_{\mathrm{ch}} = 2$ is attained. The Verdier involution under the $K3$ Mukai lattice self-duality $\Lambda_{K3} \simeq \Lambda_{K3}^\vee$ acts by a sign on odd-degree Hochschild classes, giving $\kappa_{\mathrm{ch}}' = -2$. The sum vanishes.
   138	\end{proof}
   139	
   140	\begin{remark}[Verification against CY-D]
   141	\label{rem:cy-d2-cy-d-check}
   142	Substituting $d = 2$ (K3) into $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ (Theorem~\ref{thm:cy-modular-characteristic}) gives $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$, which agrees with the independently verified chiral de Rham computation (\S\ref{sec:cy-trace-kappa}, Proposition~\ref{prop:kappa-k3}). Theorem~\ref{thm:cy-complementarity-d2} is therefore consistent with the five-path verification of $\kappa_{\mathrm{ch}}(K3) = 2$ (compute/lib/modular\_cy\_characteristic.py, $80$ tests).
   143	\end{remark}
   144	
   145	\begin{remark}[Categorical complementarity]
file update:
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 65da7b71836ccd80a9f893ee8345d5f31ae436ca..d549cf8dde796adb7aa3899224c31d8281236f58
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -1917,10 +1917,11 @@
 
 (iv)\enspace
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
 \end{proof}
 



thinking
**Considering grep usage**

I'm thinking about whether to use KM negative grep only for Volume I due to the specific pattern in the current repo. Should I run it across all three volumes instead? Maybe a simpler approach like `rg -n 'k/(2h\^\\vee).*kappa'` for all volumes could work, but I wonder if that’s actually necessary. I need to balance specificity with efficiency, so I'll weigh my options carefully!
thinking
**Reviewing version changes**

I need to look at the second volume, where one ambiguous line from the first volume has been fixed. It’s essential to review the differences, so I’ll use git diff for the file that was touched. This approach should help me see what has changed and ensure everything is accurate. My goal is to keep everything clear and make sure those adjustments are spot on!
exec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 65da7b7..d549cf8 100644
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -1917,10 +1917,11 @@ $\mathfrak{sp}_4$, and~$\mathfrak{g}_2$.
 
 (iv)\enspace
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
 \end{proof}
 
file update:
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 65da7b71836ccd80a9f893ee8345d5f31ae436ca..d549cf8dde796adb7aa3899224c31d8281236f58
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -1917,10 +1917,11 @@
 
 (iv)\enspace
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
 \end{proof}
 






thinking
**Considering verification options**

I'm thinking about whether I should run TeX lint, but maybe that's not necessary. Targeted verification could be enough, and maybe using build-surface skill might help, but the user didn't specifically ask for a build. Should I run a minimal build or latexmk on the file? It might be overkill, though verifying syntax seems important, especially since I've changed line wrap in math. I might want to check the git status for touched files too.
thinking
**Reviewing file issues**

I’m thinking there might be other files in the current repository that could have similar ambiguous misuse, but a search for "extracts" found only one, which is a relief. I wonder if I need to patch the current repository standalones. Maybe it's not necessary to mention that Volume II's explicit family formulas matched the census since no edit is needed there. For the blocked Volume III, I could note that "EXACT edit required but blocked by sandbox." Should I also consider editing Volume III via apply_patch?
thinking
**Considering file path limitations**

I'm wondering if attempting to use apply_patch on a direct file path outside of the root will be rejected. We might be able to demonstrate this, but it doesn't seem necessary. The user did ask for fixes, though. Maybe we should try it since apply_patch can edit any readable file? However, the instructions indicate that editing files in other directories requires approval, which is never given, so the command would likely be rejected. I could mention that it's blocked instead.
thinking
**Considering findings presentation**

I need to mention core chapter issues and note duplicate collision surfaces in my working notes. The user asked for findings to be formatted as “PROBLEM at file:line” along with the exact edit applied. But we didn't actually edit those, so that could get cumbersome. Maybe I should limit findings to live main surfaces and list duplicated note surfaces as pending collision surfaces after the findings. The AGENTS cross-volume rule suggests to either update genuine duplicates or leave pending names untouched.
thinking
**Considering physics notes**

I’m reviewing the notes from volume III, particularly looking at the physics anomaly cancellation. It’s interesting that the per-channel notation drift is consistent, which might satisfy some pending notes. I wonder if I should mention that no inconsistencies were found in volume II. Including a verification summary line could be useful too. Lastly, I might consider updating the plan to finalize everything clearly and neatly.
Plan update
  ✓ Map live kappa formula surfaces across Vol I/II/III and isolate any drifts from the canonical census
  ✓ Read the exact files that need changes and verify each suspect occurrence in context
  ✓ Apply minimum truthful edits in writable scope and document blocked cross-volume fixes outside writable roots
  → Run targeted verification greps and summarize findings with exact edits
file update:
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 65da7b71836ccd80a9f893ee8345d5f31ae436ca..d549cf8dde796adb7aa3899224c31d8281236f58
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -1917,10 +1917,11 @@
 
 (iv)\enspace
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
 \end{proof}
 



thinking
**Evaluating duplicate findings**

I see that `modular_koszul_bridge.tex` has the same wrong formula at lines 130 and 168, and I'm wondering if I could cover both lines in one finding. The user asked for specific format with "PROBLEM at file:line," so it feels like I could list them together but also be cautious about separating them as distinct occurrences. I also wonder if there might be another issue in Volume I. Searching for a specific wrong variant yields no hits, which could be due to the negative grep returning exit 1.
thinking
**Editing math notation and verification**

Okay, I need to replace `c\cdot(H_N -1)` with `(c+c')\cdot(H_N -1)=K_N(H_N -1)`—that seems precise. I should note there were no `H_{N-1}` hits across the three volumes, which serves as a verification. I might also mention that no edits are needed for Volume II, providing a few examples.

I'll include line references from earlier, like [preface.tex] line 977 and [examples-worked.tex] line 1302. Should I finalize with sections for `Findings` and `Verification` while keeping it concise and using flat bullets? I’ll ensure clickable absolute links with line numbers. 

I’ll aim for a final answer of around 12-18 lines.
codex
**Findings**

- PROBLEM at [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:1919): the proof used the full affine KM symbol `\kappa(\widehat{\mathfrak g}_k)` for the double-pole contribution `\dim(\mathfrak g)k/(2h^\vee)`, then added the Sugawara term on the next line. That drops the required shift at the point of first assertion. EXACT edit applied: changed the first term to `\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k) = \dim(\mathfrak g)\cdot k/(2h^\vee)` and rewrote the sum as `\kappa(\widehat{\mathfrak g}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k) + \dim(\mathfrak g)/2 = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)`.

- PROBLEM at [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130) and [modular_koszul_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:168): Vol III states the `\mathcal W_N` complementarity sum as `c(H_N - 1)`. For the sum, the canonical quantity is `(c+c')(H_N - 1) = K_N(H_N - 1)`. EXACT edit applied: not applied; sandbox blocks writes outside `/Users/raeez/chiral-bar-cobar`. Required edit is to replace `c \cdot (H_N - 1)` with `(c+c') \cdot (H_N - 1)` or `K_N \cdot (H_N - 1)` in both sentences.

- PROBLEM at [cy_to_chiral.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:909) and [bar_cobar_bridge.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:80): Vol III introduces per-channel modular characteristics as `\kappa_s` and `\kappa_s^{\mathrm{eff}}`. That drifts from AP113’s Vol III `\kappa_{\mathrm{ch}}/\kappa_{\mathrm{cat}}/\kappa_{\mathrm{BKM}}/\kappa_{\mathrm{fiber}}` namespace. EXACT edit applied: not applied; sandbox blocks writes outside `/Users/raeez/chiral-bar-cobar`. Required edit is to rewrite these as contributions to `\kappa_{\mathrm{ch}}`, e.g. “the spin-`s` contribution to `\kappa_{\mathrm{ch}}` is `1/s`,” instead of introducing `\kappa_s`.

Vol II explicit family surfaces checked clean against the census; no edit was needed at [preface.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:977), [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1302), and [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1968).

**Verification**

Negative grep after the patch found no remaining Vol I full-KM dropped-shift hit, and no `\mathcal W_N` formula hit using `H_{N-1}` across the three volumes. I did not run a TeX build.
file update:
diff --git a/chapters/theory/chiral_hochschild_koszul.tex b/chapters/theory/chiral_hochschild_koszul.tex
index 65da7b71836ccd80a9f893ee8345d5f31ae436ca..d549cf8dde796adb7aa3899224c31d8281236f58
--- a/chapters/theory/chiral_hochschild_koszul.tex
+++ b/chapters/theory/chiral_hochschild_koszul.tex
@@ -1917,10 +1917,11 @@
 
 (iv)\enspace
 The two-channel decomposition extracts
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
+$\kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})\cdot k/(2h^\vee)$ from the
 double-pole channel and $\dim(\mathfrak{g})/2$ from the
 simple-pole channel. Their sum gives
-$\kappa(\widehat{\mathfrak{g}}_k) = \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
+$\kappa(\widehat{\mathfrak{g}}_k) = \kappa_{\mathrm{dp}}(\widehat{\mathfrak{g}}_k) + \dim(\mathfrak{g})/2
+= \dim(\mathfrak{g})(k+h^\vee)/(2h^\vee)$, matching the
 formula of Theorem~\ref{thm:modular-characteristic}.
 \end{proof}
 

tokens used
149,615
