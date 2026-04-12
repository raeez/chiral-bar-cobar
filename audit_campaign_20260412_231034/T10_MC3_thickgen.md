# T10_MC3_thickgen (489s, gpt-5.4)

- [CRITICAL] `chapters/examples/yangians_computations.tex:3071` — Step 2 of `thm:shifted-prefundamental-generation` says the `\lambda=0` specialization makes the Baxter spectral constraint vacuous, so one gets a Yangian-equivariant short exact sequence for all `a,b`. The cited source says the opposite: `prop:baxter-yangian-equivariance` requires `b=a-(\lambda+1)/2`, so at `\lambda=0` one still needs `b=a-1/2` (`2924-2941`, `2977-2986`). The same false “vacuous” claim is repeated at `3222-3224`. This invalidates the load-bearing step for type-A layer-3 generation and undercuts `thm:mc3-type-a-resolution` and `cor:mc3-all-types`.

- [CRITICAL] `chapters/examples/yangians_computations.tex:3125` — Step 4 and the closing sentence of `thm:shifted-prefundamental-generation` jump from finite-dimensional strata to a theorem about compact objects of the completed shifted category, using sectorwise spectral stabilization and a finite BGG filtration for every object. But the same file later marks extension of sectorwise control to the completed/coderived MC3 domain as conjectural (`2633-2649`), and earlier says that beyond finite-length/polynomial subcategories the right framework is localizing generation in a completion, not literal thick generation in `D^b(\mathcal O)` (`1949-1972`). No proved result is cited that gives finite standard filtrations or identifies compacts of `\widehat D(\mathcal O^{\mathrm{sh}}_{\le 0})` with that thick closure. The theorem’s conclusion is therefore not established.

- [HIGH] `chapters/examples/yangians_computations.tex:3507` — The pro-Weyl recovery theorem on the MC3 critical path is tagged `\ClaimStatusProvedHere` but has no `\label{thm:pro-weyl-recovery}` and no proof body; the same proofless/label-less pattern occurs for the shifted-envelope Baxter theorem at `2871-2889` (later cited as `thm:baxter-exact-triangles`, but no such label is present). Downstream status is incoherent: `chapters/examples/yangians_drinfeld_kohno.tex:1013,1717,2186` still cites pro-Weyl as conjectural, while `chapters/theory/introduction.tex:2084-2086` advertises the type-A package as proved.

- [HIGH] `chapters/examples/yangians_computations.tex:3440` — `prop:categorical-cg-typeA` imports `prop:baxter-yangian-equivariance` from the `Y(\mathfrak{sl}_2)`/Verma setting to arbitrary weight lines in `V_{\omega_i}(a)\otimes L^-_i(b)` without re-establishing the spectral hypothesis or the claimed embeddings. Since item (i) of `thm:mc3-type-a-resolution` depends on this proposition (`3808-3819`), the Baxter-exact-triangle component of the type-A reduction is under-justified even before the completion step.

- [MEDIUM] `chapters/examples/yangians_computations.tex:3146` — The manuscript’s answer to the non-type-A condition is `conj:rank-independence-step2` (Lemma L), but the hypothesis is not sharply formalized. It asks that the type-A generation theorem “lifts” to a maximal-rank type-A Levi and then “lowers back” via Hernandez block separation, without specifying the actual functors, filtrations, or exact compatibility statements. So the text does identify a condition, but only at slogan level; it is not yet a theorem-like, falsifiable assumption.

## Summary
The intended split is clear in the text: MC3a/MC3b are stated as all-types unconditional, and MC3c is stated as type-A unconditional and non-type-A conditional on `conj:rank-independence-step2`. The audit result is that this split is not actually proved: the type-A layer-3 proof fails at a direct spectral-constraint contradiction and then overreaches into a completed-domain argument the file itself still treats as conjectural.

Instances checked: 26 | Violations found: 5 | Verdict: FAIL


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
session id: 019d8388-33d3-7fc2-afcf-dd3ad9299f15
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


MISSION: FALSIFY the proof of MC3: thick generation. Check: (a) type A unconditional, outside type A conditional—is this correctly stated? (b) what is the condition? (c) layer 3 shifted prefundamental generation?

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.
mcp startup: no servers
codex
I’m auditing the MC3 thick-generation claim as a falsification exercise. I’ll first load the required constitutional files, then locate the theorem statement/proof in `chapters/`, trace every cited dependency, and only report discrepancies that survive re-checking against the source.
exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 50ms:
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
# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
 succeeded in 52ms:
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
**Searching for theorem MC3**

I'm looking to locate theorem MC3, which I think might be in a chapter related to modular Koszul theory. I need to consider whether I should use an update plan for this. It seems that I'm likely going to use commentary with that plan. I should also note the possibility of using something like deep-beilinson-audit. Alright, I'll get started on this search and send my commentary!
codex
I’ve loaded the constitutional files and the audit skill. Next I’m fixing the exact surface for `MC3`, locating the theorem statement/proof and every imported dependency before I start the falsification pass.
exec
/bin/zsh -lc 'rg -n "MC3|thick generation|prefundamental|layer 3|shifted prefundamental|type A" chapters metadata appendices -S' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 538

chapters/examples/w_algebras_deep.tex:2243:\index{transport closure!type A}
appendices/nonlinear_modular_shadows.tex:74:\label{rem:nms-prefundamental-cg}
appendices/nonlinear_modular_shadows.tex:75:\index{shadow tower!prefundamental compatibility}
appendices/nonlinear_modular_shadows.tex:77:$Q_\cA$ at degrees~$2$, $3$, $4$) interacts with the MC3
appendices/nonlinear_modular_shadows.tex:78:prefundamental programme as follows. By the prefundamental
appendices/nonlinear_modular_shadows.tex:80:Theorem~\ref{thm:shifted-prefundamental-generation}), the
appendices/nonlinear_modular_shadows.tex:88:restricts naturally to the prefundamental evaluation-stable sector.
metadata/dependency_graph.dot:297:  conj_standard_tower_mc5_reduction [label="conj:standard-tower-mc5-reduction\nconjecture [Co]\nStandard-tower MC5 reduction after MC3 a...", style=filled, fillcolor="#fff9c4"];
metadata/dependency_graph.dot:773:  thm_thqg_V_mc3_thick_generation [label="thm:thqg-V-mc3-thick-generation\ntheorem [Pr]\nType-$A$ MC3 reduction via the gravitati...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:992:  thm_derived_realization_negative_prefundamental [label="thm:derived-realization-negative-prefundamental\ntheorem [Pr]\nDerived realization of negative prefunda...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1793:  prop_yangian_dk2_thick_generation [label="prop:yangian-dk2-thick-generation\nproposition [Pr]\nDK-2 reduction to thick generation, cond...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1819:  thm_shifted_prefundamental_generation [label="thm:shifted-prefundamental-generation\ntheorem [Pr]\n$E_1$-chiral thick generation for $Y(\ma...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1821:  prop_prefundamental_clebsch_gordan [label="prop:prefundamental-clebsch-gordan\nproposition [Pr]\nUniversal prefundamental Clebsch--Gordan", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1824:  prop_categorical_cg_typeA [label="prop:categorical-cg-typeA\nproposition [Pr]\nCategorical prefundamental CG decomposit...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1827:  thm_mc3_type_a_resolution [label="thm:mc3-type-a-resolution\ntheorem [Pr]\nType-$A$ MC3 reduction to the compact-co...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1828:  thm_mc3_arbitrary_type [label="thm:mc3-arbitrary-type\ntheorem [Pr]\nCategorical prefundamental CG decomposit...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1829:  cor_mc3_all_types [label="cor:mc3-all-types\ncorollary [Pr]\nThree-layer MC3 status after categorical...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1830:  conj_mc3_automatic_generalization [label="conj:mc3-automatic-generalization\nconjecture [Co]\nType-independence of the remaining MC3 c...", style=filled, fillcolor="#fff9c4"];
exec
/bin/zsh -lc 'rg -n "mc3" -S .' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1077

./CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
./CLAUDE.md:571:AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.
./CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
./CLAUDE.md:919:**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).
./metadata/dependency_graph.dot:297:  conj_standard_tower_mc5_reduction [label="conj:standard-tower-mc5-reduction\nconjecture [Co]\nStandard-tower MC5 reduction after MC3 a...", style=filled, fillcolor="#fff9c4"];
./metadata/dependency_graph.dot:773:  thm_thqg_V_mc3_thick_generation [label="thm:thqg-V-mc3-thick-generation\ntheorem [Pr]\nType-$A$ MC3 reduction via the gravitati...", style=filled, fillcolor="#c8e6c9"];
./metadata/dependency_graph.dot:1827:  thm_mc3_type_a_resolution [label="thm:mc3-type-a-resolution\ntheorem [Pr]\nType-$A$ MC3 reduction to the compact-co...", style=filled, fillcolor="#c8e6c9"];
./metadata/dependency_graph.dot:1828:  thm_mc3_arbitrary_type [label="thm:mc3-arbitrary-type\ntheorem [Pr]\nCategorical prefundamental CG decomposit...", style=filled, fillcolor="#c8e6c9"];
./metadata/dependency_graph.dot:1829:  cor_mc3_all_types [label="cor:mc3-all-types\ncorollary [Pr]\nThree-layer MC3 status after categorical...", style=filled, fillcolor="#c8e6c9"];
./metadata/dependency_graph.dot:1830:  conj_mc3_automatic_generalization [label="conj:mc3-automatic-generalization\nconjecture [Co]\nType-independence of the remaining MC3 c...", style=filled, fillcolor="#fff9c4"];
./metadata/dependency_graph.dot:1864:  conj_mc3_formal_moduli_reformulation [label="conj:mc3-formal-moduli-reformulation\nconjecture [Co]\nFormal moduli reformulation of MC3", style=filled, fillcolor="#fff9c4"];
./metadata/dependency_graph.dot:1968:  thm_rtt_all_types [label="thm:rtt-all-types\ntheorem [Pr]\nRTT presentation and MC3 for all simple ...", style=filled, fillcolor="#c8e6c9"];
./metadata/dependency_graph.dot:4160:  thm_thqg_V_mc3_thick_generation -> cor_dk23_all_types;
./metadata/dependency_graph.dot:4161:  thm_thqg_V_mc3_thick_generation -> thm_mc3_type_a_resolution;
./metadata/dependency_graph.dot:4162:  thm_thqg_V_mc3_thick_generation -> conj_dk_compacts_completion;
./metadata/dependency_graph.dot:4631:  conj_rank_independence_step2 -> thm_mc3_arbitrary_type;
./metadata/dependency_graph.dot:4637:  thm_mc3_type_a_resolution -> prop_prefundamental_clebsch_gordan;
./metadata/dependency_graph.dot:4638:  thm_mc3_type_a_resolution -> thm_shifted_prefundamental_generation;
codex
The target surface is now clear: `chapters/examples/yangians_computations.tex` carries the MC3 proof chain, with `cor:mc3-all-types` summarizing the three-layer status and `thm:mc3-type-a-resolution` carrying the type-A layer-3 argument. I’m reading those blocks in full with their direct dependencies, then I’ll attack whether the proved-here tags outrun what the proofs actually establish.
exec
/bin/zsh -lc "rg -n \"label\\{cor:dk23-all-types\\}|label\\{thm:shifted-prefundamental-generation\\}|label\\{prop:prefundamental-clebsch-gordan\\}|label\\{prop:categorical-cg-typeA\\}|label\\{thm:mc3-type-a-resolution\\}|label\\{thm:mc3-arbitrary-type\\}|label\\{cor:mc3-all-types\\}|label\\{conj:rank-independence-step2\\}|label\\{rem:lemma-L-status\\}|label\\{thm:catO-thick-generation\\}\" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/connections/concordance.tex chapters/theory/introduction.tex -n -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '1710,1865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3720,4065p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2990,3465p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2078,2092p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4335,4385p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1710	 core; and
  1711	\item compatibility of the bar-cobar unit and counit with
  1712	 factorization products after passing through that comparison.
  1713	\end{enumerate}
  1714	
  1715	Concretely, the bar-cobar adjunction itself provides the intrinsic
  1716	bar-side unit and counit
  1717	$\eta\colon \mathrm{id} \to \Omega \circ \barB$ and counit
  1718	$\varepsilon\colon \barB \circ \Omega \to \mathrm{id}$ are
  1719	quasi-isomorphisms on Koszul objects
  1720	\textup{(}Theorem~\textup{\ref{thm:e1-chiral-koszul-duality})}.
  1721	On evaluation modules, the proved DK-1 theorem shows that these
  1722	adjunction maps match the expected evaluation-level identifications.
  1723	Beyond that locus, however, neither the bar-comodule/quantum-group
  1724	comparison nor its factorization-monoidal/quasi-inverse enhancement is
  1725	automatic from bar-cobar alone.
  1726	\end{remark}
  1727	
  1728	\begin{lemma}[Monoidal extension to thick closures;
  1729	\ClaimStatusProvedHere]
 succeeded in 52ms:
chapters/examples/yangians_computations.tex:1592:\label{thm:catO-thick-generation}
chapters/examples/yangians_computations.tex:3040:\label{thm:shifted-prefundamental-generation}
chapters/examples/yangians_computations.tex:3148:\label{conj:rank-independence-step2}
chapters/examples/yangians_computations.tex:3174:\label{rem:lemma-L-status}
chapters/examples/yangians_computations.tex:3309:\label{prop:prefundamental-clebsch-gordan}%
chapters/examples/yangians_computations.tex:3411:\label{prop:categorical-cg-typeA}%
chapters/examples/yangians_computations.tex:3765:\label{thm:mc3-type-a-resolution}
chapters/examples/yangians_computations.tex:3844:\label{thm:mc3-arbitrary-type}% backward compat
chapters/examples/yangians_computations.tex:3991:\label{cor:mc3-all-types}%
chapters/examples/yangians_drinfeld_kohno.tex:878:\label{cor:dk23-all-types}
 succeeded in 50ms:
  3720	 conjectural packages reduce to a single remaining
  3721	 compact-completion packet
  3722	 (Theorem~\ref{thm:mc3-type-a-resolution}).
  3723	 The proof proceeds through: (1)~the prefundamental Clebsch--Gordan
  3724	 closure
  3725	 (Proposition~\ref{prop:prefundamental-clebsch-gordan}:
  3726	 $V_n \otimes L^- \cong \bigoplus L^-(\mathrm{shifted})$) lifts the
  3727	 Baxter TQ relations to exact triangles;
  3728	 (2)~the chromatic/conformal-weight filtration reduces
  3729	 shifted-prefundamental generation to countable finite-dimensional
  3730	 strata;
  3731	 (3)~Mittag--Leffler ($R^1\varprojlim = 0$) on Weyl module
  3732	 truncation towers recovers standards as derived inverse limits;
  3733	 (4)~spectral sequence degeneration on weight strata, together
  3734	 with the Francis--Gaitsgory pro-nilpotent completion formalism,
  3735	 isolates the last remaining compact/completed comparison problem:
  3736	 one still needs the compact-core extension of the bar-cobar
  3737	 equivalence and its comparison with the desired completed
  3738	 category.
  3739	 %
 succeeded in 50ms:
  2990	symbolically and numerically for $\lambda = 1, \ldots, 50$).
  2991	\end{proof}
  2992	
  2993	\begin{corollary}[Naturality on
  2994	$\mathcal{O}_{\mathrm{poly}}$; \ClaimStatusProvedHere]
  2995	\label{cor:baxter-naturality-opoly}
  2996	Under the spectral
  2997	constraint~\eqref{eq:baxter-spectral-constraint}, the
  2998	assignment
  2999	$M(\lambda) \mapsto
  3000	[\textup{SES}~\eqref{eq:baxter-ses-yangian}]$
  3001	defines a natural exact sequence of functors on
  3002	$\mathcal{O}_{\mathrm{poly}}(Y(\mathfrak{sl}_2))$.
  3003	\end{corollary}
  3004	
  3005	\begin{proof}
  3006	On $\mathcal{O}_{\mathrm{poly}}$, Verma modules are the simple
  3007	objects and $\Hom(M(\lambda), M(\mu)) = 0$ for $\lambda \neq \mu$,
  3008	$\End(M(\lambda)) = \mathbb{C}$. Since all Hom spaces are at most
  3009	$1$-dimensional, naturality of the SES maps with respect to
 succeeded in 51ms:
  2078	\end{center}
  2079	
  2080	\noindent\textbf{MC1} (PBW concentration): Bar cohomology of every standard-landscape chiral algebra concentrates in PBW degrees, proved for all standard families by explicit computation.
  2081	
  2082	\noindent\textbf{MC2} (Universal MC class): $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ exists for every modular Koszul chiral algebra by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of its finite-order projections. When $\dim H^2_{\mathrm{cyc}} = 1$, the MC element collapses to $\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Corollary~\ref{cor:scalar-saturation}).
  2083	
  2084	\noindent\textbf{MC3} (Thick generation): Proved for all simple types on the evaluation-generated core via multiplicity-free $\ell$-weights~\cite{ChariMoura06} (Theorem~\ref{thm:categorical-cg-all-types}), with DK comparison proved separately (Corollary~\ref{cor:dk23-all-types}, Corollary~\ref{cor:mc3-all-types}). For type~$A$, shifted-prefundamental generation and pro-Weyl recovery are also proved (Theorem~\ref{thm:mc3-type-a-resolution}). DK-4/5 (extension beyond evaluation modules) is downstream.
  2085	
  2086	 The proof decomposes into three layers: MC3a (evaluation core, all types, unconditional), MC3b (categorical thick generation, all types, unconditional), and MC3c (full category~$\mathcal{O}$, type~$A$ unconditional; other types conditional on Conjecture~\ref{conj:rank-independence-step2}, the rank-independence lift-and-lower conjecture for shifted prefundamental representations; see Remark~\ref{rem:lemma-L-status} for the dependency chain).
  2087	
  2088	\noindent\textbf{MC4} ($\mathcal{W}_\infty$ closure and completed bar-cobar): The completed bar-cobar problem asks whether finite-stage Koszul duality passes to inverse limits. Two complementary mechanisms cover the entire standard landscape:
  2089	
  2090	\smallskip
  2091	\noindent\emph{Mechanism~1: strong filtration.}
  2092	If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic. The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}). This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 succeeded in 52ms:
  4335	is the converse via the Hitchin variation of Hodge structure.
  4336	
  4337	\paragraph{Three-lens identification of the shadow tower.}
  4338	Proposition~\ref{prop:shadow-tower-three-lenses} identifies
  4339	three equivalent readings of the degree-$r$ shadow
  4340	$S_r(\cA)$: algebraic (bar-intrinsic MC projection),
  4341	geometric (genus-$0$ transferred $L_\infty$ formality
  4342	obstruction), and holographic (boundary-bulk correction
  4343	in the derived-centre factorization).
  4344	
  4345	\paragraph{Generating depth versus algebraic depth.}
  4346	Definition~\ref{def:generating-depth} formalizes the
  4347	distinction mandated: the generating depth
  4348	$d_{\mathrm{gen}}(\cA)$ is the smallest degree at which
  4349	higher operations are recursively determined, while the
  4350	algebraic depth $d_{\mathrm{alg}}(\cA)$ is the smallest
  4351	degree beyond which all operations vanish. Virasoro:
  4352	$d_{\mathrm{gen}} = 3$ (finite), $d_{\mathrm{alg}} = \infty$
  4353	(class~M). Bare $d(\cA)$ without subscript is forbidden.
  4354	


thinking
**Checking proof for BGG**

I need to check if BGG is proved for the category O^{sh}_{<=0}. I’m not entirely sure, but it could be that the proof only applies to polynomial categories or under certain finite length assumptions. There’s a lot to consider here, and I wonder what specific criteria I should be looking for. Let’s dive deeper into this to find clear answers!
thinking
**Searching mathematical proofs**

I need to inspect the full proof related to categorical properties like `prop:categorical-cg-typeA` and the proposition `prop:baxter-yangian-equivariance`. I also want to look into the theorem `thm:baxter-exact-triangles-opoly` and the proposition `dk2-thick-generation-typeA`. Additionally, I should check the theorem `thm:eval-core-identification` and possibly the theorem `thm:catO-thick-generation`. My next step is to search for their locations and use relevant excerpts from rg.
codex
I’m now drilling into the load-bearing steps: the type-A categorical CG lift, the Baxter equivariance input, the finite-dimensional generation theorem, and the pro-Weyl/BGG claims that Step 3 and the final sentence of `thm:shifted-prefundamental-generation` silently rely on. This is where scope inflation or missing hypotheses would show up.
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3460,3725p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{prop:dk2-thick-generation-typeA\\}|label\\{prop:baxter-yangian-equivariance\\}|label\\{thm:baxter-exact-triangles-opoly\\}|label\\{thm:eval-core-identification\\}|label\\{prop:character-cg-all-types\\}|label\\{thm:catO-thick-generation\\}|label\\{Weyl truncation|Mittag--Leffler|finite filtration by standards|BGG|standard lies|compact objects are the thick idempotent-complete closure|separated pro-completed shifted category|block decomposition|highest \\\\ell-weight ratio|generic spectral parameters\" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/examples/yangians_foundations.tex chapters/theory/derived_langlands.tex -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '1088,1198p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '1230,1665p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '840,930p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{prop:dk2-thick-generation-typeA\}|label\{prop:baxter-yangian-equivariance\}|label\{thm:baxter-exact-triangles-opoly\}|label\{thm:eval-core-identification\}|label\{prop:character-cg-all-types\}|label\{thm:catO-thick-generation\}|label\{Weyl truncation|Mittag--Leffler|finite filtration by standards|BGG|standard lies|compact objects are the thick idempotent-complete closure|separated pro-completed shifted category|block decomposition|highest \ell-weight ratio|generic spectral parameters)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  1088	 fundamental result of Chari--Moura~\cite{ChariMoura06}.
  1089	 The multiplicity-free property ensures that the tensor product
  1090	 $V_{\omega_i}(a) \otimes V_{\omega_j}(b)$
  1091	 has a composition series whose successive quotients are
  1092	 $\ell$-weight-separated at generic spectral parameters, enabling
  1093	 the categorical Clebsch--Gordan decomposition
  1094	 \textup{(}Theorem~\textup{\ref{thm:categorical-cg-all-types}}\textup{)}.
  1095	
  1096	\item \emph{MC3 categorical closure.}
  1097	 The multiplicity-free $\ell$-weight property, combined with the
  1098	 Francis--Gaitsgory pro-nilpotent completion and the DK comparison
  1099	 on compacts, yields:
  1100	 \begin{enumerate}[label=\textup{(\alph*)}]
  1101	 \item Prefundamental representations $L_i^\pm(a)$ exist as
  1102	 limits of evaluation modules in the Borel subalgebra
  1103	 $Y_q^+(\fg)$ for all simple~$\fg$
  1104	 \textup{(}Hernandez--Jimbo~\cite{HJ12}\textup{)}.
  1105	 \item The Baxter TQ relation
  1106	 $t(u)\, Q_i(u) = a_i(u)\, Q_i(u - 1) + d_i(u)\, Q_i(u + 1)$
  1107	 holds for the transfer-matrix eigenvalues, where
 succeeded in 51ms:
  1230	\label{sec:yangian-category-O}
  1231	\index{Yangian!category O}
  1232	
  1233	We first fix the ambient category.
  1234	
  1235	\begin{definition}[Yangian category \texorpdfstring{$\mathcal{O}$}{O}]
  1236	\label{def:yangian-category-O}
  1237	\index{Yangian!category O!definition}
  1238	For $\fg = \mathfrak{sl}_N$, the \emph{Yangian category~$\mathcal{O}$}
  1239	$\mathcal{O}_{Y_\hbar(\mathfrak{sl}_N)}$ is the full subcategory of
  1240	$Y_\hbar(\mathfrak{sl}_N)$-modules~$M$ satisfying:
  1241	\begin{enumerate}[label=\textup{(\roman*)}]
  1242	\item $M$ is finitely generated over~$Y_\hbar(\mathfrak{sl}_N)$;
  1243	\item $M$ has a weight decomposition
  1244	 $M = \bigoplus_{\mu \in \mathfrak{h}^*} M_\mu$ with
  1245	 finite-dimensional weight spaces;
  1246	\item the set of weights of~$M$ is contained in a finite union
  1247	 of cones $\{\mu \leq \lambda_i\}$ for the dominance order.
  1248	\end{enumerate}
  1249	The \emph{polynomial subcategory}
 succeeded in 52ms:
  3460	= V_{\omega_i}(a) \otimes L^-_i(b)$
  3461	(where $d = \dim V_{\omega_i}$) with successive quotients
  3462	$F_j / F_{j-1} \cong L^-_i(\mathrm{shift} = \mu_j)$ for
  3463	some ordering of the weights.
  3464	
  3465	\emph{Step~2: Block separation.}
  3466	Each summand $L^-_i(\mathrm{shift} = \mu)$ carries a distinct
  3467	$\ell$-highest weight $\Psi^-_{i,\mu}$ encoding the full
  3468	weight vector~$\mu$. For $\mu \neq \nu$ in
  3469	$\operatorname{wt}(V_{\omega_i})$, the $\ell$-weight ratio
  3470	$\Psi^-_{i,\mu} / \Psi^-_{i,\nu}$ is a monomial~$x^{\mu - \nu}$
  3471	with $\mu - \nu \neq 0$ in the weight lattice.
  3472	By the block criterion for category~$\mathcal{O}^{\mathrm{sh}}$
  3473	\cite{Hernandez05, HJZ25}: two simple highest-$\ell$-weight
  3474	modules lie in the same block only if their $\ell$-weight ratio
  3475	is a product of shifted simple root contributions. For
  3476	generic spectral parameters (avoiding a discrete resonance set
  3477	where $\mu - \nu$ aligns with the normalized $R$-matrix
  3478	denominator), the monomial~$x^{\mu - \nu}$ admits no such
  3479	factorization, so $L^-_i(\mathrm{shift} = \mu)$ and
 succeeded in 51ms:
   840	product of the $\operatorname{Ran}_1$ intertwining on each factor.
   841	The same cosheaf descent as part~(i) extends from disjoint to
   842	arbitrary opens.
   843	
   844	\emph{Part~(iii): module equivalence.}
   845	On evaluation objects, the module bar functor is an equivalence by
   846	DK-1 (Theorem~\ref{thm:factorization-dk-eval}). The
   847	evaluation-generated core
   848	$\operatorname{Fact}_{\Eone}^{\mathrm{gen}}(\cA)$ is the
   849	smallest full stable idempotent-complete braided monoidal subcategory
   850	containing all evaluation objects. Since the module bar functor
   851	is exact and braided monoidal with reversal
   852	(Theorem~\ref{thm:monoidal-module-koszul}), it preserves shifts,
   853	cones, direct summands, and ordered tensor products. Therefore, by
   854	Proposition~\ref{prop:yangian-dk3-generated-core}, any natural
   855	isomorphism between the identity and
   856	$\Omega_{\mathrm{mod}} \circ \barB_{\mathrm{mod}}$ that holds on
   857	evaluation generators extends to the full generated core.
   858	
   859	The braiding reversal $R \mapsto R^{-1}$ is

thinking
**Locating theorem labels**

I've encountered a challenge with the rg search; perhaps I don't need to rerun it. I still need to locate several labels, like `prop:baxter-yangian-equivariance` and others. I wonder if some theorems might have different labels. It would be good to check the details of the pro-Weyl theorem, as well as inspect `prop:character-cg-all-types`, which might have been renamed. I should confirm by searching for the specific labels and references to ensure I gather accurate details.
exec
/bin/zsh -lc "rg -n \"label\\{prop:baxter-yangian-equivariance\\}|label\\{thm:baxter-exact-triangles-opoly\\}|label\\{thm:eval-core-identification\\}|label\\{prop:character-cg-all-types\\}|label\\{thm:pro-weyl-recovery\\}|label\\{thm:baxter-exact-triangles\\}|label\\{prop:yangian-bar-loop-weight\\}|label\\{thm:sectorwise-spectral-convergence\\}|label\\{thm:h-level-factorization-kd\\}|label\\{prop:yangian-koszul\\}\" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex -n -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3500,3565p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2780,3015p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '560,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '760,845p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/yangians_drinfeld_kohno.tex:692:\label{thm:sectorwise-spectral-convergence}
chapters/examples/yangians_drinfeld_kohno.tex:741:\label{thm:h-level-factorization-kd}
chapters/examples/yangians_computations.tex:2006:\label{prop:yangian-bar-loop-weight}
chapters/examples/yangians_computations.tex:2764:\label{thm:eval-core-identification}
chapters/examples/yangians_computations.tex:2832:\label{thm:baxter-exact-triangles-opoly}
chapters/examples/yangians_computations.tex:2921:\label{prop:baxter-yangian-equivariance}
chapters/examples/yangians_computations.tex:4145:\label{prop:character-cg-all-types}
 succeeded in 50ms:
  3500	\cong \bigoplus_\mu L^-_i(\mathrm{shift} = \mu)$.
  3501	The character identity
  3502	(Proposition~\ref{prop:prefundamental-clebsch-gordan}) confirms
  3503	that the direct sum accounts for the full character with no
  3504	remainder.
  3505	\end{proof}
  3506	
  3507	\begin{theorem}[Pro-Weyl recovery of ordinary standards in type~$A$; \ClaimStatusProvedHere]
  3508	\index{Weyl module!pro-Weyl tower}
  3509	\index{standard module!pro-Weyl recovery}
  3510	For $\fg = \mathfrak{sl}_N$ with $N \ge 2$ and a rational highest
  3511	$\ell$-weight~$\Psi$, let
  3512	$\Psi_{\leq m}$ denote its truncation to finite Drinfeld divisor
  3513	data and $W_m := W(\Psi_{\leq m})$ the local Weyl module.
  3514	Then the ordinary standard module is recovered as a derived
  3515	inverse limit
  3516	\[
  3517	M(\Psi) \;\simeq\; R\varprojlim_m\, W_m
  3518	\]
  3519	inside a separated completion of~$\mathcal{O}$.
 succeeded in 50ms:
  2780	\;\xrightarrow{\;\sim\;}\;
  2781	D^b\bigl(\operatorname{Rep}_{\mathrm{fd}}
  2782	 (Y_{-\hbar}(\mathfrak{sl}_N))\bigr)^{\mathrm{op}},
  2783	\end{equation}
  2784	and DK-2/DK-3 are resolved for the evaluation-generated core
  2785	at all~$N$.
  2786	\end{theorem}
  2787	
  2788	\begin{proof}
  2789	\emph{$(\supseteq)$:}
  2790	Every finite-dimensional simple $Y_\hbar(\mathfrak{sl}_N)$-module
  2791	lies in $\mathcal{D}_\hbar^{\mathrm{eval}}$ by
  2792	Proposition~\ref{prop:dk2-thick-generation-typeA}.
  2793	Since $\operatorname{Rep}_{\mathrm{fd}}$ is Artinian, every
  2794	object has a finite composition series with simple factors in
  2795	$\mathcal{D}_\hbar^{\mathrm{eval}}$.
  2796	Lemma~\ref{lem:composition-thick-generation} then gives
  2797	$D^b(\operatorname{Rep}_{\mathrm{fd}}) \subset
  2798	\mathcal{D}_\hbar^{\mathrm{eval}}$.
  2799	
 succeeded in 50ms:
   760	 \textup{(}automatic by
   761	 Theorem~\textup{\ref{thm:sectorwise-spectral-convergence}}
   762	 when~\ref{h2:sectorwise} holds\textup{)}.
   763	\end{enumerate}
   764	Then:
   765	\begin{enumerate}[label=\textup{(\roman*)}]
   766	\item The factorization bar-cobar counit
   767	 \[
   768	 \varepsilon^{\mathrm{fact}}\colon
   769	 \Omega^{\mathrm{fact}}(\barB^{\mathrm{fact}}(\cA)) \to \cA
   770	 \]
   771	 is a quasi-isomorphism of factorization algebras on
   772	 $\operatorname{Ran}(X)$.
   773	\item The factorization Verdier intertwining
   774	 $\mathbb{D}_{\mathrm{Ran}}\,
   775	 \barB^{\mathrm{fact}}(\cA)
   776	 \simeq (\cA^!)_\infty$
   777	 holds at the factorization level (factorization \emph{algebra}, not coalgebra).
   778	\item The module bar functor
   779	 \[
 succeeded in 50ms:
   560	\label{prop:yangian-dk3-generated-core}
   561	Let
   562	\[
   563	\operatorname{Fact}_{\Eone}^{\mathrm{gen}}(\mathcal{Y}(\mathfrak{g}))
   564	\subset \operatorname{Fact}_{\Eone}(\mathcal{Y}(\mathfrak{g})),
   565	\qquad
   566	\operatorname{Fact}_{\Eone}^{\mathrm{gen}}(U_q(\mathfrak{g}))
   567	\subset \operatorname{Fact}_{\Eone}(U_q(\mathfrak{g}))
   568	\]
   569	be the smallest full stable idempotent-complete braided monoidal
   570	subcategories containing all ordered tensor products of evaluation
   571	objects. Assume there exist exact braided monoidal functors
   572	\[
   573	KZ_{\mathrm{fact}}^{\mathrm{gen}}\colon
   574	\operatorname{Fact}_{\Eone}^{\mathrm{gen}}(\mathcal{Y}(\mathfrak{g}))
   575	\to
   576	\operatorname{Fact}_{\Eone}^{\mathrm{gen}}(U_q(\mathfrak{g}))^{\mathrm{op}},
   577	\]
   578	\[
   579	LZ_{\mathrm{fact}}^{\mathrm{gen}}\colon


thinking
**Searching for theorem label**

I still need the exact theorem label for pro-Weyl; it might be `thm:pro-weyl-recovery`, but it seems I'm not finding it since no label is visible around the theorem. I’m wondering if the label could be absent altogether. It’s a bit perplexing, and I’ll need to do some searching to figure this out. Let's see if I can dig deeper to find the information I need.
thinking
**Investigating theorem label**

I need to check around line 3507 since the theorem seems to lack a label. That’s definitely a bit suspicious. I should search for the label “thm:pro-weyl-recovery” to see if it might be mentioned elsewhere. It would be useful to use “rg” for that. Getting to the bottom of this is important! Let’s dig into the details and find out what's going on here.
codex
A structural issue is emerging: several MC3 steps are being justified by nearby remarks or narrative summaries rather than a directly cited proved theorem with a visible label. I’m checking whether those supporting statements actually exist as formal claims, or whether the proof is leaning on unlabelled or downgraded material.
exec
/bin/zsh -lc "rg -n \"pro-weyl-recovery|label\\{thm:pro-weyl-recovery\\}|label\\{conj:thm:pro-weyl-recovery\\}|label\\{conj:pro-weyl-recovery\\}|Conjecture~\\\\ref\\{thm:pro-weyl-recovery\\}|Theorem~\\\\ref\\{thm:pro-weyl-recovery\\}\" chapters/examples/yangians_computations.tex -n -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"finite filtration by standards|BGG|standard module|ordinary standard|Verma module.*finite filtration by standards|every object of.*O\\"'^'"\\{\\\\mathrm\\{sh\\}\\}.*finite filtration\" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/theory/derived_langlands.tex -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"separated pro-completed shifted category|\\\\widehat\\{D\\}\\(\\\\mathcal\\{O\\}\\"'^'"\\{\\\\mathrm\\{sh\\}\\}_\\{\\\\leq 0\\}|compact objects.*thick idempotent-complete closure|localizing subcategories with compact generation|heart-capture-criterion|standard-capture-criterion|sectorwise-localizing-generation\" chapters/examples/yangians_computations.tex -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{prop:heart-capture-criterion\\}|label\\{prop:standard-capture-criterion\\}|label\\{cor:sectorwise-localizing-generation\\}|label\\{lem:fd-thick-closure\\}|label\\{rem:fd-thick-closure-implications\\}\" chapters/examples/yangians_computations.tex -n -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3526:\label{rem:pro-weyl-recovery-typeA}
3528:Conjecture~\ref{thm:pro-weyl-recovery} is resolved.
3569: \textup{(}Theorem~\ref{thm:pro-weyl-recovery}\textup{)}.
3695: \textup{(}Conjecture~\textup{\ref{thm:pro-weyl-recovery}}\textup{)}:
 exited 2 in 52ms:
rg: regex parse error:
    (?:finite filtration by standards|BGG|standard module|ordinary standard|Verma module.*finite filtration by standards|every object of.*O\^\{\mathrm\{sh\}\}.*finite filtration)
                                                                                                                                               ^^
error: unrecognized escape sequence
 succeeded in 50ms:
1920:\label{lem:fd-thick-closure}
1947:\label{rem:fd-thick-closure-implications}
2545:\label{prop:heart-capture-criterion}
2565:\label{prop:standard-capture-criterion}
2590:\label{cor:sectorwise-localizing-generation}
 exited 2 in 51ms:
rg: regex parse error:
    (?:separated pro-completed shifted category|\widehat\{D\}\(\mathcal\{O\}\^\{\mathrm\{sh\}\}_\{\leq 0\}|compact objects.*thick idempotent-complete closure|localizing subcategories with compact generation|heart-capture-criterion|standard-capture-criterion|sectorwise-localizing-generation)
                                                               ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n -F "finite filtration by standards" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/theory/derived_langlands.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "localizing subcategories with compact generation" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "separated pro-completed shifted category" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "BGG" chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex chapters/theory/derived_langlands.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/yangians_computations.tex:3140:a finite filtration by standards (BGG), and each standard lies in
 exited 1 in 50ms:

 succeeded in 50ms:
3679: localizing subcategories with compact generation. The
 succeeded in 52ms:
chapters/theory/derived_langlands.tex:1142:\item The induced map on Ext groups recovers BGG multiplicities:
chapters/theory/derived_langlands.tex:1200:cohomology is computed by the BGG resolution
chapters/examples/yangians_computations.tex:1263:BGG-type resolution theory on the intrinsic bar-comodule surface. On
chapters/examples/yangians_computations.tex:1268:\begin{theorem}[Yangian BGG resolution; \ClaimStatusProvedHere]
chapters/examples/yangians_computations.tex:1270:\index{BGG resolution!Yangian}
chapters/examples/yangians_computations.tex:1295: read as the dual BGG resolution of $L(\lambda)(-a)$.
chapters/examples/yangians_computations.tex:1522:BGG resolution of a Verma module $M(\lambda, a)$ by direct sums of
chapters/examples/yangians_computations.tex:2300: BGG category~$\mathcal{O}$ for $\mathfrak{gl}_M$, which has
chapters/examples/yangians_computations.tex:2308: Kazhdan--Lusztig polynomials (via BGG reciprocity:
chapters/examples/yangians_computations.tex:2348:to all finite-dimensional modules (different blocks of BGG
chapters/examples/yangians_computations.tex:2382:\noindent\textbf{Strategy~I\@: Highest-weight filtration and BGG
chapters/examples/yangians_computations.tex:2385:\begin{proposition}[BGG resolution criterion for thick generation;
chapters/examples/yangians_computations.tex:2388:\index{BGG resolution!thick generation}
chapters/examples/yangians_computations.tex:2412:\begin{remark}[BGG resolution via spectral parameter extensions]
chapters/examples/yangians_computations.tex:2414:\index{BGG resolution!spectral parameter}
chapters/examples/yangians_computations.tex:2419:orbit produces the classical BGG resolution, all of whose terms are
chapters/examples/yangians_computations.tex:2422:For non-dominant $\lambda$, the classical BGG resolution is
chapters/examples/yangians_computations.tex:2531:the Weyl group orbit), recovering the classical BGG resolution
chapters/examples/yangians_computations.tex:2627:I (BGG) & Finite evaluation resolution of Verma modules
chapters/examples/yangians_computations.tex:3140:a finite filtration by standards (BGG), and each standard lies in
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2368,2610p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Type-A resolution of pro-Weyl recovery" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:pro-weyl-recovery\\}|label\\{conj:thm:pro-weyl-recovery\\}|label\\{conj:pro-weyl-recovery\\}|begin\\{theorem\\}\\[Pro-Weyl recovery|begin\\{conjecture\\}\\[Pro-Weyl recovery\" chapters/examples/yangians_computations.tex -n -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '1888,1965p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2368	equivariance proved on~$\mathcal{O}_{\mathrm{poly}}$
  2369	(Proposition~\ref{prop:baxter-yangian-equivariance}) does
  2370	\emph{not} extend to~$L^-$ by thick generation from
  2371	$\mathcal{O}_{\mathrm{poly}}$. A separate argument
  2372	is needed: either the $\lambda = 0$ specialization
  2373	(which avoids the spectral constraint entirely) or an
  2374	explicit pro-Weyl approximation of~$L^-$ by objects in
  2375	$\mathcal{O}_{\mathrm{poly}}$. Since $p(k)$ grows
  2376	superpolynomially (Hardy--Ramanujan), no finite-length
  2377	resolution of~$L^-$ by evaluation modules exists.
  2378	\end{remark}
  2379	
  2380	\medskip
  2381	
  2382	\noindent\textbf{Strategy~I\@: Highest-weight filtration and BGG
  2383	resolution.}
  2384	
  2385	\begin{proposition}[BGG resolution criterion for thick generation;
  2386	\ClaimStatusProvedHere]
  2387	\label{prop:bgg-criterion}
 succeeded in 51ms:
3507:\begin{theorem}[Pro-Weyl recovery of ordinary standards in type~$A$; \ClaimStatusProvedHere]
 succeeded in 51ms:
3525:\begin{remark}[Type-A resolution of pro-Weyl recovery]
 succeeded in 51ms:
  1888	
  1889	Whether $\mathcal{O} = \mathcal{O}_{\mathrm{poly}}$ is an open
  1890	question; see Corollary~\ref{cor:dk-partial-conj}.
  1891	If $\mathcal{O} \supsetneq \mathcal{O}_{\mathrm{poly}}$, the
  1892	additional modules could either be genuinely irrelevant to DK or
  1893	could indicate missing structure on the quantum group side; the
  1894	present framework does not distinguish these possibilities.
  1895	\end{remark}
  1896	
  1897	\begin{remark}[DK ladder after the finite-dimensional theorem]
  1898	\label{rem:dk-fd-synthesis}
  1899	DK-0/1: proved for all simple~$\fg$. DK-2/3: the thick-generation
  1900	statements for finite-dimensional Yangian representations are proved
  1901	\textup{(}Proposition~\ref{prop:dk2-thick-generation-typeA} and
  1902	Theorem~\ref{thm:catO-thick-generation}\textup{)}, but promotion of
  1903	evaluation-locus DK beyond the generators is only conditional on the
  1904	ambient extension/comparison package of
  1905	Theorem~\ref{conj:dk-fd-typeA}; a separate H-level sectorwise route
  1906	exists at all simple types
  1907	\textup{(}Corollary~\ref{cor:dk23-all-types}\textup{)}. Extension

thinking
**Checking inspection timelines**

I think I need to look into the line after 1965. It's possible there's something important there that needs my attention. Maybe there are specific details or changes that occurred after that year that could affect what I’m analyzing. I'm not entirely sure where to start, but I want to make sure I'm thorough. Let’s see what information I can gather about events or regulations post-1965 to have a clearer overview!
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '1946,2008p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1946	\begin{remark}[Implications for the generation problem]
  1947	\label{rem:fd-thick-closure-implications}
  1948	\index{thick generation!scope limitation}
  1949	Lemma~\ref{lem:fd-thick-closure} shows that the literal generation
  1950	question
  1951	$\mathcal{C}_{\mathrm{eval}} \stackrel{?}{=}
  1952	D^b(\mathcal{O}_{Y_\hbar(\mathfrak{sl}_N)})$
  1953	has a \emph{positive} answer when restricted to
  1954	$\mathcal{O}_{\mathrm{poly}}$ or to $N = 2$ (where all simples are
  1955	finite-dimensional), and a \emph{negative} answer if the full
  1956	category~$\mathcal{O}$ contains genuine infinite-length objects.
  1957	The correct target for extending beyond
  1958	$\mathcal{O}_{\mathrm{poly}}$ is therefore not literal thick
  1959	generation in $D^b(\mathcal{O})$, but one of:
  1960	\begin{enumerate}[label=\textup{(\alph*)}]
  1961	\item the statement
  1962	 $\operatorname{thick}(\text{evaluation modules}) =
  1963	 D^b(\mathcal{O}_{\mathrm{poly}})$
  1964	 (matching the proved scope);
  1965	\item \emph{localizing} generation in an Ind- or
codex
There’s now a concrete proof-surface problem: the file contains a `\ClaimStatusProvedHere` theorem for pro-Weyl recovery with no visible `\label{thm:pro-weyl-recovery}` and no proof body at all. I’m checking whether MC3’s proof can survive without that theorem, or whether later statements are silently depending on an unproved placeholder.
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2868,2955p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "O''^{'"\\mathrm{sh}}_{\\leq 0}\" chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\label\\{def:.*shifted.*\\}|anti-dominant shifted envelope|shifted envelope|separated completion|compact objects|completed anti-dominant shifted envelope|highest-weight category\" chapters/examples/yangians_computations.tex -n -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '4040,4170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Theorem~\\ref{thm:shifted-prefundamental-generation}\" chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_drinfeld_kohno.tex -S" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
  2868	the SES with respect to the tensor product associator.
  2869	\end{proof}
  2870	
  2871	\begin{theorem}[Baxter exact triangles on shifted envelope
  2872	\texorpdfstring{$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$}{Osh};
  2873	\ClaimStatusProvedHere]
  2874	\index{Baxter relation!exact triangle lift!shifted envelope}
  2875	Theorem~\textup{\ref{thm:baxter-exact-triangles-opoly}} extends
  2876	from $\mathcal{O}_{\mathrm{poly}}$ to the full anti-dominant
  2877	shifted envelope
  2878	$\mathcal{O}^{\mathrm{sh}}_{\leq 0}
  2879	:= \bigoplus_{\mu \leq 0} \mathcal{O}_\mu$
  2880	for $\fg = \mathfrak{sl}_N$ at general~$N$.
  2881	Concretely, for each node~$i \in I$ and finite-dimensional companion
  2882	module $M_{k,x}^{(i)}$, there is a distinguished triangle
  2883	\[
  2884	A^-_{k,x,y} \to M_{k,x}^{(i)} \otimes L(\Psi_{i,x}/\Psi_{i,y})
  2885	\to A^+_{k,x,y} \to
  2886	\]
  2887	whose $K_0$-class recovers the formula of Zhang~\cite{Zhang24},
 exited 2 in 50ms:
rg: regex parse error:
    (?:\label\{def:.*shifted.*\}|anti-dominant shifted envelope|shifted envelope|separated completion|compact objects|completed anti-dominant shifted envelope|highest-weight category)
       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
chapters/examples/yangians_foundations.tex:802:(Theorem~\ref{thm:shifted-prefundamental-generation},
chapters/examples/yangians_drinfeld_kohno.tex:324:(Theorem~\ref{thm:shifted-prefundamental-generation})
chapters/examples/yangians_drinfeld_kohno.tex:1012:(Theorem~\ref{thm:shifted-prefundamental-generation}),
chapters/examples/yangians_drinfeld_kohno.tex:1726: Theorem~\ref{thm:shifted-prefundamental-generation}, these
 succeeded in 52ms:
  4040	\subsection{Landscape of the MC3 extension}
  4041	\label{sec:mc3-extension-landscape}
  4042	
  4043	\begin{conjecture}[Type-independence of the remaining MC3 completion mechanisms;
  4044	 \ClaimStatusConjectured]
  4045	\label{conj:mc3-automatic-generalization}
  4046	\label{conj:mc3-proof-step-analysis}% backward compatibility (renamed from prop:)
  4047	Let~$\mathfrak{g}$ be simple. Assume that, beyond the all-types
  4048	categorical CG theorem and the evaluation-generated-core DK
  4049	equivalence, the following packets are available in the relevant
  4050	shifted/completed category:
  4051	\begin{enumerate}[label=\textup{(\roman*)}]
  4052	\item shifted-prefundamental generation on the relevant compact core;
  4053	\item the Mittag--Leffler / pro-Weyl hypotheses on the Weyl truncation
  4054	 towers;
  4055	\item a compatible compact-completion formalism carrying compact-core
  4056	 equivalences to the desired completed category.
  4057	\end{enumerate}
  4058	Then, once package~(i) and DK-2/3 on the evaluation-generated core are
  4059	in place, the remaining pro-Weyl and completion arguments of the

thinking
**Inspecting references and conjectures**

I need to look into the references in concordance, maybe searching for different wording related to cor:mc3-all-types could help. I might not need to go beyond what I've already read, but it’s important to check if the Theorem around shifted-prefundamental-generation is referred to as a conjecture elsewhere. There could be status drift here, so I’ll look for instances where it's labeled conjecture, possibly searching for phrases like "Conjecture\ref{thm:shifted-prefundamental-generation}". This feels like a relevant investigation to pursue.
exec
/bin/zsh -lc "rg -n -F \"Conjecture~\\ref{thm:pro-weyl-recovery}\" chapters -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Conjecture~\\ref{thm:shifted-prefundamental-generation}\" chapters -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"Theorem~\\ref{thm:pro-weyl-recovery}\" chapters -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "full anti-dominant shifted envelope" chapters/examples/yangians_computations.tex -S' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/yangians_computations.tex:3194:Conjecture~\ref{thm:shifted-prefundamental-generation} is fully
 succeeded in 52ms:
chapters/examples/yangians_computations.tex:3528:Conjecture~\ref{thm:pro-weyl-recovery} is resolved.
chapters/examples/yangians_drinfeld_kohno.tex:1013:pro-Weyl recovery (Conjecture~\ref{thm:pro-weyl-recovery}), and
chapters/examples/yangians_drinfeld_kohno.tex:1717: Conjecture~\ref{thm:pro-weyl-recovery}, these are
chapters/examples/yangians_drinfeld_kohno.tex:2186: \textup{(}Conjecture~\ref{thm:pro-weyl-recovery}\textup{)}:
 succeeded in 51ms:
chapters/examples/yangians_drinfeld_kohno.tex:2188: Theorem~\ref{thm:pro-weyl-recovery}, the Weyl truncation tower
chapters/examples/yangians_computations.tex:3569: \textup{(}Theorem~\ref{thm:pro-weyl-recovery}\textup{)}.
 exited 1 in 51ms:


thinking
**Clarifying proof positions**

It seems I need to investigate if proof is relying on a hidden assumption since it doesn't directly cite the information. I should verify if it's sufficient or if this could still remain unproved. It might be helpful to locate the definition of `\widehat D(\mathcal{O}^{sh}_{<=0})` to clarify everything. Let's see if searching with simpler, fixed strings might lead to better results.
codex
The proof chain is accumulating second-order problems, not just local gaps: there are stale `Conjecture~\ref{...}` references to now-`theorem` labels, and at least one unlabeled/no-proof pro-Weyl theorem sitting directly on the MC3 critical path. I’m now checking whether the category-theoretic hypotheses used in the last sentence of `thm:shifted-prefundamental-generation` are actually established for the completed shifted category, rather than only for finite truncation sectors.
exec
/bin/zsh -lc 'rg -n -F "completed anti-dominant shifted envelope" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "finite-length highest-weight category" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "compact part recovers the evaluation-generated factorization core" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "separated completion" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "compact objects are the thick idempotent-complete closure" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "every object of" chapters/examples/yangians_computations.tex | rg -n -F "finite filtration by standards"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3775: completed anti-dominant shifted envelope
 succeeded in 52ms:
3047:the compact objects are the thick idempotent-complete closure of
 exited 1 in 52ms:

 succeeded in 52ms:
3519:inside a separated completion of~$\mathcal{O}$.
3534:$M(\Psi) \simeq R\varprojlim_m W_m$ inside the separated completion
3697: $R\varprojlim_m W_m$ inside a separated completion, where
3791: separated completion, proved via Mittag--Leffler
 succeeded in 52ms:
2568:Let $\cA$ be a finite-length highest-weight category with finite
2596:finite-length highest-weight category. If in each sector the
 exited 1 in 51ms:


thinking
**Inspecting mathematical definitions**

I'm thinking I should check the definition of shifted envelope and sectorwise localizing generation to figure out if theorem 3038 indeed uses localizing generation instead of thick generation. I might explore information from around 2590 onward, as that could provide enough insight. I also want to look into later remarks around 3679 regarding localizing generation. There could be a mismatch between the theorem's use of compact objects in a completed category versus proof methods for localizing generation. I'll examine sections around 2610-2670 for strategies and theorem summaries.
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2610,2668p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2610	follows.
  2611	\end{proof}
  2612	
  2613	\begin{remark}[Assessment and interaction of the four strategies]
  2614	\label{rem:cat-O-strategies-assessment}
  2615	\index{thick generation!strategy comparison}
  2616	\begin{center}
  2617	\renewcommand{\arraystretch}{1.2}
  2618	\begin{tabular}{lll}
  2619	\textbf{Strategy} & \textbf{Reduces to} & \textbf{Scope} \\
  2620	\hline
  2621	IV (sectorwise) & Current algebra $E_1$ computation
  2622	 & All types \\
  2623	III (KL reduction) & Finite global dimension +
  2624	 Verma $\in \mathcal{C}_{\mathrm{eval}}$ & Type $A$ \\
  2625	II (t-structure) & \textbf{Proved}: $\mathfrak{sl}_2$ + $\mathcal{O}_{\mathrm{poly}}$
  2626	 (Thm.~\ref{thm:catO-thick-generation}) & Type $A$ \\
  2627	I (BGG) & Finite evaluation resolution of Verma modules
  2628	 & All types \\
  2629	\end{tabular}

thinking
**Analyzing Strategy IV**

I'm finding it interesting that Strategy IV resolves DK-2/3 using evaluation-generated core bypassing thick generation. But there's a concern regarding whether the arguments were solely based on evaluation-generated core and not considering a broader domain.

I need to check the hidden assumption related to thm:eval-core-identification and take a look at the relevant section around line 2764. It seems like I might need the full theorem statement to clarify if it's about Rep_fd only and not O_sh. Let's inspect the earlier lines for more context.
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2738,2788p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2738	\item At $p = 200$: $\dim E_1^{0,200}(\mathfrak{sl}_2) = 159{,}733$,
  2739	 $\dim E_1^{0,200}(\mathfrak{sl}_3) = 98{,}874{,}604$
  2740	 (not polynomial);
  2741	\item Observed growth constants converge to $\pi\sqrt{r/12}$
  2742	 within $8\%$ at $p = 500$ for all types including the
  2743	 exceptional algebras $G_2$, $F_4$, $E_{6,7,8}$;
  2744	\item Same-rank algebras ($A_2$, $B_2$, $G_2$: all rank~$2$)
  2745	 confirm identical leading constant, different subleading;
  2746	\item Departure points from $A_1$: $p = 5$ for $A_2$,
  2747	 $p = 7$ for $C_2$, $p = 11$ for $G_2$ (matching manuscript).
  2748	\end{itemize}
  2749	Sectorwise finiteness for all simply-laced lattice
  2750	VOAs ($A_1$--$A_3$, $D_4$--$D_5$, $E_6$--$E_8$) is verified at the
  2751	lattice-bar sector level ($93$~tests,
  2752	\texttt{compute/lib/sectorwise\_finiteness.py}),
  2753	and the sub-exponential vs.\ exponential growth discrimination is
  2754	checked via least-squares fitting of $\log d_n$ to both $c \cdot n$
  2755	and $C \cdot \sqrt{n}$ models.
  2756	\end{computation}
  2757	




thinking
**Analyzing conjectures and proof**

I'm looking at how the spectral sequence stabilization applies, as well as the extension of root-weight decomposition and loop filtration. There's a conjecture about this extension, which seems critical. The theorem mentions "ProvedHere," but there's a residual question in the conjecture.

The user specifically asks about type A unconditional versus conditional, and I need to confirm whether my statements align correctly with the conjecture and lemma regarding rank-independence. A quick audit is necessary to check if my understanding is accurate.
thinking
**Evaluating type-A conditions**

I need to check if the type-A unconditional claim is overstated because the theorem on shifted prefundamental generation has issues. This could mean that the claim for unconditional type-A layer 3 isn’t actually secured.

The manuscript mentions unconditional in type A and conditions elsewhere, referencing Lemma L, but that seems unjustified since it has unsupported steps. I have to dig into conjectural rank-independence and Lemma L's status, as their conditions are quite vague and may not serve as formal hypotheses. It's essential to figure out if there's an actual lift/lower mechanism involved.
thinking
**Assessing the condition's precision**

It seems like there’s no specified functor or exact map, and I can't see a categorical lift from g^A to g. This makes the condition not mathematically sharp, which could indicate a high severity issue. The statement outside type A relies on a vague conjectural "lift-and-lower hypothesis," rather than a clear formal condition, rendering the reference to "conditional on Lemma L" quite weak.

I should evaluate this further and cite the relevant lines for clarity. The precision of this condition definitely feels insufficient.
thinking
**Considering strategy inspection**

I think I need to examine line 2631, especially noting that the sector-wise strategy beyond the core seems to be more of a conjecture at this point. It's important to scrutinize these assumptions to ensure we're on the right track. I find myself questioning how much we can rely on these projections and if there are better data points or insights we should consider to refine our approach. Let's make sure we have a solid foundation moving forward!
exec
/bin/zsh -lc "rg -n -F \"\\widehat{\\mathcal{O}}"'^{'"\\mathrm{sh}}_{\\leq 0}\" chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\widehat{D}(\\mathcal{O}"'^{'"\\mathrm{sh}}_{\\leq 0}\" chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "compact objects" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "anti-dominant shifted envelope" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3776: $\widehat{\mathcal{O}}^{\mathrm{sh}}_{\leq 0}$.
3820: $\widehat{\mathcal{O}}^{\mathrm{sh}}_{\leq 0}$ at a cofinal
 succeeded in 51ms:
3046:$\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g})))$,
3161:$\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g})))$,
3198:$\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$ are the thick
3783: $\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g})))$
4005: of~$\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$\textup{)}}:
 succeeded in 52ms:
3775: completed anti-dominant shifted envelope
 succeeded in 52ms:
3047:the compact objects are the thick idempotent-complete closure of
3197:problem to countable finite-dimensional strata: compact objects of
3691: the compact objects of a completed anti-dominant shifted

thinking
**Investigating mathematical definitions**

I’m exploring an issue related to definitions—specifically, how the theorem uses categories that might not be clearly defined. I should search for `\mathcal{O}^{\mathrm{sh}}_{\leq 0}` in possible definitions, like in theorem 2871, which might describe it as a direct sum. I also need to inspect the references across chapters, particularly the type A layer 3 unconditional mentioned in the introduction. It seems important to identify any overstatements, especially regarding "MC3 proved for all simple types." So, I plan to search chapters for that phrase.
exec
/bin/zsh -lc 'rg -n -F "MC3 is proved for all simple types" chapters -S' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Thick generation (MC3): Proved for all simple types" chapters -S' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "MC3 proved for all simple types" chapters -S' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"MC3 & Thick generation & \\textbf{proved}\" chapters/theory/introduction.tex chapters/frame/preface_sections10_13_draft.tex chapters/connections/editorial_constitution.tex chapters/connections/outlook.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_introduction_supplement_body.tex:1737:MC3 is proved for all simple types on the evaluation-generated core
chapters/connections/concordance.tex:1887:\textbf{MC3 is proved for all simple types on the
 exited 1 in 52ms:

 succeeded in 51ms:
chapters/connections/concordance.tex:9595:& MC3 proved for all simple types on the
chapters/theory/nilpotent_completion.tex:1281: remains inviolable (MC3 proved for all simple types on the evaluation-generated core; MC4 proved). The BV/BRST physics dictionary
 succeeded in 51ms:
chapters/theory/introduction.tex:2074:MC3 & Thick generation & \textbf{proved} & CG all types + eval-core DK (Cor.~\ref{cor:mc3-all-types}); DK-4/5 downstream \\[2pt]

thinking
**Analyzing data interpretation**

I need to consider that claiming line 2074 could be an overstatement since the table indicates MC3 proved it, but the text below clarifies the layers. It might be a medium case. I should probably read `chapters/connections/concordance.tex` around lines 1887 or 9595 to see if there's a stronger argument. Additionally, mentioning propagation drift might not be necessary, so I’ll check the output around 1880 to gather more information.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1878,1895p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1878	 cluster-tilting structure.
  1879	 Types $E_8$, $F_4$ (non-folded route): hardest cases,
  1880	 potentially requiring Coulomb branch geometry
  1881	 (Braverman--Finkelberg--Nakajima).
  1882	
  1883	\begin{construction}[MC3 status by Dynkin type]
  1884	\label{constr:mc3-difficulty-gradient-concordance}
  1885	\index{MC3!status by type|textbf}
  1886	\index{Dynkin type!MC3 status}
  1887	\textbf{MC3 is proved for all simple types on the
  1888	evaluation-generated core.}
  1889	Package~(i) (categorical CG) uses multiplicity-free
  1890	$q$-characters \cite{FrenkelMukhin01, Nakajima04, ChariMoura06}
  1891	transferred to Yangians via~\cite{GTL17}
  1892	(Theorem~\ref{thm:categorical-cg-all-types}).
  1893	Thick generation of $\mathrm{Rep}_{\mathrm{fd}}$ by evaluation
  1894	modules holds for all types
  1895	(Corollary~\ref{cor:dk2-thick-generation-all-types}).



thinking
**Analyzing spectral constraints**

I’m checking the Step 2 analysis where each term supposedly acquires a factor of λ_i=0, so it vanishes. But that seems wrong since the λ=0 specialization doesn’t remove the 1/2 term! I need to verify if there’s a different coproduct and weight pairing involved in sl_N. They cite this as λ=0 specialization, which contradicts earlier sections. This finding is crucial because it alters Step 2’s SES for all a,b, indicating that theorem 3038 fails and challenges the entire concept of "rank-independent Baxter stability."
thinking
**Considering generalization possibilities**

I’m wondering about how to generalize the concepts from sl2 to higher ranks. It seems like there might be unique challenges or new features that I need to consider as I move forward. Maybe there are specific behaviors or characteristics in higher rank structures that differ significantly from sl2. I’m curious about what those differences might be, and how they could change the overall framework we’re working with. I'll need to explore this further!
thinking
**Inspecting theorem language**

I need to take a closer look at the pro-Weyl theorem and consider mentioning downstream propagation if there’s a missing label on it. I’m thinking about checking specific lines around 1008-1014 and 1713 to see if there are any strong overclaims. It seems like I might uncover some important details that could clarify or strengthen my argument regarding this theorem. Let's dig into it!
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '1004,1018p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '1710,1728p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '2180,2191p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2082,2087p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1004	Corollary~\ref{cor:dk23-all-types} resolve the
  1005	evaluation-generated-core DK comparison surface
  1006	\textup{(}traditionally packaged as DK-2/3\textup{)} at all types.
  1007	The four conjectures of
  1008	Remark~\ref{rem:corrected-mc3-frontier}(b)
  1009	(Baxter exact triangles
  1010	(Conjecture~\ref{thm:baxter-exact-triangles}),
  1011	shifted-prefundamental generation
  1012	(Theorem~\ref{thm:shifted-prefundamental-generation}),
  1013	pro-Weyl recovery (Conjecture~\ref{thm:pro-weyl-recovery}), and
  1014	DK on compacts
  1015	(Conjecture~\ref{conj:dk-compacts-completion}))
  1016	concern the extension \emph{beyond} this core to
  1017	infinite-dimensional modules via a completed or coderived
  1018	enhancement.
 succeeded in 51ms:
  1710	of Theorem~\ref{thm:factorization-positselski}.
  1711	
  1712	The four conjectures of
  1713	Remark~\ref{rem:corrected-mc3-frontier}(b) concern modules
  1714	that lie in the ind-completion but not in the generated core:
  1715	\begin{enumerate}[label=\textup{(\alph*)}]
  1716	\item \emph{Standard modules} $M(\Psi)$: by
  1717	 Conjecture~\ref{thm:pro-weyl-recovery}, these are
  1718	 pro-Weyl limits $R\varprojlim_m W_m$, where each~$W_m$ is
  1719	 compact (evaluation-generated). The pro-object
  1720	 $\{W_m\}$ defines an object of $\operatorname{Pro}(\mathcal{C})
  1721	 \hookrightarrow \operatorname{Ind}(\mathcal{C})$
  1722	 via the canonical functor
  1723	 $\operatorname{Pro}(\mathcal{C}) \to
  1724	 \operatorname{Ind}(\mathcal{C})^{\mathrm{op}}$.
  1725	\item \emph{Prefundamental modules} $L^-_{i,a}$: by
  1726	 Theorem~\ref{thm:shifted-prefundamental-generation}, these
  1727	 are compact generators of the completed shifted category.
  1728	 In the ind-completed factorization category, $L^-_{i,a}$
 succeeded in 50ms:
  2180	\textup{(}Corollary~\ref{cor:completed-bar-cobar-yangian}\textup{)}
  2181	also clarifies the bar-side setting for the remaining MC3 extension
  2182	conjectures
  2183	(Conjecture~\ref{conj:mc3-formal-moduli-reformulation}):
  2184	\begin{enumerate}[label=\textup{(\roman*)}]
  2185	\item \emph{Pro-Weyl recovery}
  2186	 \textup{(}Conjecture~\ref{thm:pro-weyl-recovery}\textup{)}:
  2187	 on the theorematic type-$A$ surface of
  2188	 Theorem~\ref{thm:pro-weyl-recovery}, the Weyl truncation tower
  2189	 $\{W_m\}$ can be viewed inside the completed bar/factorization
  2190	 setting supplied by Corollary~\ref{cor:completed-bar-cobar-yangian}.
  2191	 What the completed bar-cobar theorem does \emph{not} by itself prove
 succeeded in 52ms:
  2082	\noindent\textbf{MC2} (Universal MC class): $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ exists for every modular Koszul chiral algebra by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of its finite-order projections. When $\dim H^2_{\mathrm{cyc}} = 1$, the MC element collapses to $\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Corollary~\ref{cor:scalar-saturation}).
  2083	
  2084	\noindent\textbf{MC3} (Thick generation): Proved for all simple types on the evaluation-generated core via multiplicity-free $\ell$-weights~\cite{ChariMoura06} (Theorem~\ref{thm:categorical-cg-all-types}), with DK comparison proved separately (Corollary~\ref{cor:dk23-all-types}, Corollary~\ref{cor:mc3-all-types}). For type~$A$, shifted-prefundamental generation and pro-Weyl recovery are also proved (Theorem~\ref{thm:mc3-type-a-resolution}). DK-4/5 (extension beyond evaluation modules) is downstream.
  2085	
  2086	 The proof decomposes into three layers: MC3a (evaluation core, all types, unconditional), MC3b (categorical thick generation, all types, unconditional), and MC3c (full category~$\mathcal{O}$, type~$A$ unconditional; other types conditional on Conjecture~\ref{conj:rank-independence-step2}, the rank-independence lift-and-lower conjecture for shifted prefundamental representations; see Remark~\ref{rem:lemma-L-status} for the dependency chain).
  2087	
exec
/bin/zsh -lc "rg -n \"label\\{thm:baxter-exact-triangles\\}|label\\{conj:thm:baxter-exact-triangles\\}|Conjecture~\\\\ref\\{thm:baxter-exact-triangles\\}|Theorem~\\\\ref\\{thm:baxter-exact-triangles\\}\" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex -n -S" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Searching for missing labels**

I'm noticing there's no label found, but the text does reference something called Conjecture\ref{thm:baxter-exact-triangles}. It sounds like there might be a missing label here. I think I should search for the exact string `thm:baxter-exact-triangles` to see if references exist despite the missing label. I’m already at 2894 and 3579, so exploring this fixed string feels like a logical next step!
exec
/bin/zsh -lc 'rg -n -F "thm:baxter-exact-triangles" chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/yangians_computations.tex:2832:\label{thm:baxter-exact-triangles-opoly}
chapters/examples/yangians_computations.tex:2875:Theorem~\textup{\ref{thm:baxter-exact-triangles-opoly}} extends
chapters/examples/yangians_computations.tex:2894:Conjecture~\ref{thm:baxter-exact-triangles} is proved at generic
chapters/examples/yangians_computations.tex:3030:Conjecture~\ref{thm:baxter-exact-triangles} and a first step
chapters/examples/yangians_computations.tex:3579:Conjectures~\ref{thm:baxter-exact-triangles}--\ref{conj:dk-compacts-completion}
chapters/examples/yangians_computations.tex:3684: \textup{(}Conjecture~\textup{\ref{thm:baxter-exact-triangles}}\textup{)}:
chapters/examples/yangians_computations.tex:3818: (Theorem~\ref{thm:baxter-exact-triangles-opoly}), this gives
chapters/examples/yangians_drinfeld_kohno.tex:1010:(Conjecture~\ref{thm:baxter-exact-triangles}),
chapters/examples/yangians_drinfeld_kohno.tex:1731: Conjecture~\ref{thm:baxter-exact-triangles}).
chapters/examples/yangians_drinfeld_kohno.tex:1759: \textup{(}Conjecture~\textup{\ref{thm:baxter-exact-triangles}}\textup{)}





thinking
**Evaluating theorem 2871**

I notice that theorem 2871 indicates there's no formal proof or label available, which seems like a significant point. The proof for item (i) appears to be attempting to deduce itself, which raises questions about its validity. I wonder if this self-deduction could lead to issues within its argument structure. It feels like I'm uncovering something intriguing but confusing! Let's dig deeper and clarify what this means for understanding the theorem.
thinking
**Considering file specifications**

I'm thinking about how I could possibly use exact line numbers in the format of "single file:line." It seems like a straightforward way to reference specific parts of the code. This could help with pinpointing issues or making discussions clearer. I wonder if this format is standard practice, or if there are better ways to approach this! It’s definitely something worth exploring more.
thinking
**Clarifying findings and structure**

I want to make sure that I'm avoiding subjectivity when describing the conjecture. It names a condition but doesn't offer a checkable lift functor or lowering morphism, which seems fair. I need to reference line 3179 regarding a proposition, even though it’s labeled as a conjecture. I might mention that the resolution theorem isn't secure due to not all packages being fully proved. Finally, I'll create a findings list with a summary sentence indicating a verdict, ensuring there's no extra nesting in bullets.
thinking
**Considering file inclusion**

I'm pondering whether I need to include file links in the final answer. It might not be strictly necessary, but since it was requested, I could mention the file and line in a plain format. However, to make it more user-friendly, I should think about using clickable links instead. This way, it could enhance the overall presentation and accessibility for the user. Balancing necessity and clarity is key here!
thinking
**Refining proof accuracy**

I see that the first bullet suggests a direct contradiction, which clearly breaks the step—this is good to note. For the second bullet, saying "the theorem's conclusion is not established" seems fair. The third bullet mentioning "proofless-pattern occurs" works too. I think I should specify lines during cross-references to make everything precise. Now, let's focus on crafting a final answer that is concise yet detailed enough to convey the necessary information.
codex
- [CRITICAL] `chapters/examples/yangians_computations.tex:3071` — Step 2 of `thm:shifted-prefundamental-generation` says the `\lambda=0` specialization makes the Baxter spectral constraint vacuous, so one gets a Yangian-equivariant short exact sequence for all `a,b`. The cited source says the opposite: `prop:baxter-yangian-equivariance` requires `b=a-(\lambda+1)/2`, so at `\lambda=0` one still needs `b=a-1/2` (`2924-2941`, `2977-2986`). The same false “vacuous” claim is repeated at `3222-3224`. This invalidates the load-bearing step for type-A layer-3 generation and undercuts `thm:mc3-type-a-resolution` and `cor:mc3-all-types`.

- [CRITICAL] `chapters/examples/yangians_computations.tex:3125` — Step 4 and the closing sentence of `thm:shifted-prefundamental-generation` jump from finite-dimensional strata to a theorem about compact objects of the completed shifted category, using sectorwise spectral stabilization and a finite BGG filtration for every object. But the same file later marks extension of sectorwise control to the completed/coderived MC3 domain as conjectural (`2633-2649`), and earlier says that beyond finite-length/polynomial subcategories the right framework is localizing generation in a completion, not literal thick generation in `D^b(\mathcal O)` (`1949-1972`). No proved result is cited that gives finite standard filtrations or identifies compacts of `\widehat D(\mathcal O^{\mathrm{sh}}_{\le 0})` with that thick closure. The theorem’s conclusion is therefore not established.

- [HIGH] `chapters/examples/yangians_computations.tex:3507` — The pro-Weyl recovery theorem on the MC3 critical path is tagged `\ClaimStatusProvedHere` but has no `\label{thm:pro-weyl-recovery}` and no proof body; the same proofless/label-less pattern occurs for the shifted-envelope Baxter theorem at `2871-2889` (later cited as `thm:baxter-exact-triangles`, but no such label is present). Downstream status is incoherent: `chapters/examples/yangians_drinfeld_kohno.tex:1013,1717,2186` still cites pro-Weyl as conjectural, while `chapters/theory/introduction.tex:2084-2086` advertises the type-A package as proved.

- [HIGH] `chapters/examples/yangians_computations.tex:3440` — `prop:categorical-cg-typeA` imports `prop:baxter-yangian-equivariance` from the `Y(\mathfrak{sl}_2)`/Verma setting to arbitrary weight lines in `V_{\omega_i}(a)\otimes L^-_i(b)` without re-establishing the spectral hypothesis or the claimed embeddings. Since item (i) of `thm:mc3-type-a-resolution` depends on this proposition (`3808-3819`), the Baxter-exact-triangle component of the type-A reduction is under-justified even before the completion step.

- [MEDIUM] `chapters/examples/yangians_computations.tex:3146` — The manuscript’s answer to the non-type-A condition is `conj:rank-independence-step2` (Lemma L), but the hypothesis is not sharply formalized. It asks that the type-A generation theorem “lifts” to a maximal-rank type-A Levi and then “lowers back” via Hernandez block separation, without specifying the actual functors, filtrations, or exact compatibility statements. So the text does identify a condition, but only at slogan level; it is not yet a theorem-like, falsifiable assumption.

## Summary
The intended split is clear in the text: MC3a/MC3b are stated as all-types unconditional, and MC3c is stated as type-A unconditional and non-type-A conditional on `conj:rank-independence-step2`. The audit result is that this split is not actually proved: the type-A layer-3 proof fails at a direct spectral-constraint contradiction and then overreaches into a completed-domain argument the file itself still treats as conjectural.

Instances checked: 26 | Violations found: 5 | Verdict: FAIL
tokens used
152,422
