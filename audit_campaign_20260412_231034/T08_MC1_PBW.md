# T08_MC1_PBW (622s, gpt-5.4)

- [CRITICAL] [higher_genus_modular_koszul.tex:994](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:994) — The genus-1 Kac--Moody proof explicitly allows `d_1^{PBW}` of enrichment classes to land in the concentrated genus-0 sector (`E_1(g=0) \oplus \mathcal E_1`). The later proofs at [1292](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1292), [1472](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1472), [801](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:801), and [1709](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1709) then kill the enrichment and conclude `E_\infty(g)=E_\infty(0)` without controlling those mixed maps. That comparison is not proved.

- [CRITICAL] [higher_genus_modular_koszul.tex:1011](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1011) — The proof says `d_1^{PBW}` is built from the bracket of the truncated loop algebra, then immediately reidentifies the enrichment as `C^*(\fg,M_h)` and invokes Whitehead for semisimple `\fg` at [1027](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1027). That reduction is not justified by the text. The same unsupported move reappears at [1294](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1294) and [1776](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1776). Whitehead applies to `\fg`, not automatically to the truncated current algebra that the proof itself names.

- [HIGH] [higher_genus_modular_koszul.tex:1050](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1050) — The displayed `d_2` computation does not hit the invariant class it claims to kill. The surviving class is `\kappa^{ab}(J^a_{-1}\otimes J^b_{-1})\otimes\alpha`, but the computed image is `k\dim(\fg)\,J^c_{-1}\otimes\alpha`, a different target. The all-genera repetition at [1346](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1346) has the same defect. This step also requires `k\neq0`, while the theorem statement [1210](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1210) includes generic `k\notin\Sigma(\fg)`, and the cited genericity theorem [kac_moody.tex:983](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:983) excludes special values via `\lambda=k+h^\vee`, not by removing `k=0`.

- [HIGH] [higher_genus_modular_koszul.tex:1264](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1264) — Inference: the factorization `\mathcal E_g^{*,h}\cong M_h\otimes H^{1,0}(\Sigma_g)` is asserted but not proved, and it is hard to reconcile with the chain groups written at [955](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:955), which use `\Omega^{n-1}_{\log}` in bar degree `n`. For `n>2`, the regular contribution should depend on bar degree and allow multiple global 1-forms, not a single `H^{1,0}` factor. This unsupported factorization is then reused in the Virasoro, principal-`\mathcal W`, and universal proofs.

- [HIGH] [concordance.tex:1842](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1842) — Downstream propagation is overstated. Concordance packages `prop:pbw-universality` as an MC1 citation for universal `V_k(\fg)`, `\mathrm{Vir}_c`, and `\mathcal W^k(\fg)`, but [chiral_koszul_pairs.tex:1314](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1314) only proves genus-0 chiral Koszulness of freely strongly generated vertex algebras. It does not prove the all-genera PBW concentration used elsewhere for MC1, including [editorial_constitution.tex:193](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:193).

- [MEDIUM] [higher_genus_modular_koszul.tex:1486](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1486) — The Virasoro proof misquotes its own cited input. It says `\dim M_h=p(h-2)` by `comp:virasoro-vacuum`, but [bar_complex_tables.tex:278](/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:278) gives `\dim \bar V_h=p_{\ge2}(h)=p(h)-p(h-1)`; at `h=5` the table gives `2`, while `p(3)=3`. This is not fatal by itself, but the cited step is false as written.

- [LOW] [higher_genus_modular_koszul.tex:1380](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1380) — The repeated appeal to `H^{0,1}(\Sigma_g)` “antiholomorphic forms” sits outside the algebraic bar-complex surface actually written, which uses logarithmic forms [higher_genus_modular_koszul.tex:955](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:955) on a smooth projective curve [higher_genus_modular_koszul.tex:534](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:534). This is a scope/convention leak even if the core theorem were repairable.

## Summary
Instances checked: 15 | Violations found: 7 | Verdict: FAIL


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
session id: 019d8388-3412-7cb0-bc20-b98fd79b5153
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


MISSION: FALSIFY the proof of MC1: PBW theorem. Find the proof. Check completeness and correctness of the PBW filtration.

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
Using `deep-beilinson-audit` for this turn because the task is an adversarial proof audit, not a local wording check. I’m first locating `MC1` and loading the required constitutional files plus the exact theorem/proof surface and its cited dependencies.
collab spawn_agent(call_YXuAKhwPNwOl3OZa6CFo0ITE, prompt="<task>Locate the proof surface for MC1: PBW theorem in this repository. Find the exact file(s), theorem label/environmen…")
spawn_agent(call_YXuAKhwPNwOl3OZa6CFo0ITE, prompt="<task>Locate the proof surface for MC1: PBW theorem in this repository. Find the exact file(s), theorem label/environmen…") pending init:
  agent: 019d8388-8e18-7d40-84a7-2951897027d6
mcp startup: no servers
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg -n \"MC1|PBW theorem|\\\\label\\{(thm|prop|lem|conj):["'^}]*pbw|Poincare[- ]Birkhoff[- ]Witt|Poincar'"\\\\'e[- ]Birkhoff[- ]Witt|PBW\" chapters CLAUDE.md metadata/theorem_registry.md chapters/connections/concordance.tex raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 exited 2 in 51ms:
/Users/raeez/chiral-bar-cobar
rg: regex parse error:
    (?:MC1|PBW theorem|\label\{(thm|prop|lem|conj):[^}]*pbw|Poincare[- ]Birkhoff[- ]Witt|Poincar\'e[- ]Birkhoff[- ]Witt|PBW)
                       ^^
error: unrecognized escape sequence
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
audit_campaign_20260412_230832
audit_campaign_20260412_231034
bibliography
bp_self_duality.pdf
chapters

exec
/bin/zsh -lc 'rg -n "PBW" -n' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 3449

CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
CLAUDE.md:766:AP64: CE weight vs PBW degree produce different sequences. Always specify grading.
CLAUDE.md:775:AP75: Koszulness = PBW degree concentration, NOT conformal weight grading.
metadata/dependency_graph.dot:209:  thm_pbw_recurrence [label="thm:pbw-recurrence\ntheorem [Pr]\nPBW recurrence theorem for
metadata/dependency_graph.dot:292:  thm_master_pbw [label="thm:master-pbw\ntheorem [Pr]\nHigher-genus PBW concentration for the s...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:357:  thm_frontier_weyl_pbw_linear_sewing [label="thm:frontier-weyl-pbw-linear-sewing\ntheorem [Pr]\nAssociativity, PBW, and exact linear Wey...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:566:  thm_pbw_slodowy_collapse [label="thm:pbw-slodowy-collapse\ntheorem [Pr]\nPBW--Slodowy collapse", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1053:  prop_sl3_pbw_ss [label="prop:sl3-pbw-ss\nproposition [Pr]\nPBW spectral sequence for \texorpdfstrin...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1057:  prop_pbw_e2_from_vacuum_module [label="prop:pbw-e2-from-vacuum-module\nproposition [Pr]\nPBW \texorpdfstring{$E_2$}{E_2} from vac...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1519:  prop_n2_koszulness [label="prop:n2-koszulness\nproposition [Pr]\nPBW Koszulness of the $\mathcal{N}=2$ SC...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:1696:  thm_w_pbw_slodowy_collapse [label="thm:w-pbw-slodowy-collapse\ntheorem [Pr]\nPBW--Slodowy collapse", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2085:  thm_uniform_pbw_bridge [label="thm:uniform-pbw-bridge\ntheorem [Pr]\nUniform PBW bridge from MC1 to MC4", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2210:  thm_pbw_regular_tensor [label="thm:pbw-regular-tensor\ntheorem [Pr]\nPBW-regular tensor theorem", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2390:  thm_pbw_koszulness_criterion [label="thm:pbw-koszulness-criterion\ntheorem [Pr]\nPBW criterion for chiral Koszulness", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2398:  prop_pbw_universality [label="prop:pbw-universality\nproposition [Pr]\nPBW universality", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2823:  thm_holo_comp_weyl_sewing [label="thm:holo-comp-weyl-sewing\ntheorem [Pr]\nWeyl associativity, PBW, and linear sewi...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2926:  thm_pbw_allgenera_principal_w [label="thm:pbw-allgenera-principal-w\ntheorem [Pr]\nPBW concentration at all genera for prin...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2927:  thm_pbw_genus1_km [label="thm:pbw-genus1-km\ntheorem [Pr]\nPBW degeneration at genus~\texorpdfstrin...", style=filled, fillcolor="#c8e6c9"];
thinking
**Resolving errors and updates**

I need to recover from the regex error and then read through the theorem. It might be useful to update my plan since this is a multi-step task. I'll continue updating my commentary as needed. Maybe I should wait for the explorer. Also, I need to check the skill instructions. We haven't opened the SKILL.md for the deep-beilinson-audit skill yet. I think I’ll do both the commentary update and the plan update.
codex
I’ve loaded the constitutional surfaces and the red-team ledger. Next I’m isolating the exact `MC1` PBW theorem/proof, then I’ll trace every cited dependency and attack the filtration argument step by step for hidden assumptions and scope leakage.
Plan update
Audit plan for falsifying MC1: PBW theorem without modifying files.
  → Read the audit skill instructions and locate the exact MC1/PBW theorem surface with statement and proof lines
  • Read the full theorem, proof, and every cited dependency in context
  • Attack each proof step for logical gaps, missing hypotheses, scope inflation, and boundary-value failures
  • Re-verify each candidate finding against the source and produce severity-ordered report
exec
/bin/zsh -lc 'rg -n "MC1"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md:491:| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
metadata/dependency_graph.dot:2085:  thm_uniform_pbw_bridge [label="thm:uniform-pbw-bridge\ntheorem [Pr]\nUniform PBW bridge from MC1 to MC4", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:149:| `thm:uniform-pbw-bridge` | `theorem` | 1919 | Uniform PBW bridge from MC1 to MC4 |
AGENTS.md:552:| MC1-4 | PROVED | PBW, MC element, thick gen, completion tower |
metadata/claims.jsonl:2007:{"label": "thm:uniform-pbw-bridge", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_curved.tex", "line": 1919, "title": "Uniform PBW bridge from MC1 to MC4"}
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1129:Koszulness from MC1, and the principal level-shift theorem) give the
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/examples/w_algebras_deep.tex:1379: PBW (MC1, principal) \\
FRONTIER.md:21:### MC1-MC4 proved; MC5 partially proved
FRONTIER.md:25:| **MC1** | PROVED | PBW concentration, all standard families (prop:pbw-universality) |
chapters/examples/bar_complex_tables.tex:1749:\index{MC1!algorithmic verification}
chapters/examples/bar_complex_tables.tex:1769:MC1 concentration ($E_2^{p,q} = 0$ for $q \neq 0$) therefore
standalone/introduction_full_survey.tex:4841:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera while the genuswise BV/BRST/bar identification remains conjectural. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
standalone/introduction_full_survey.tex:4847:MC1 & PBW concentration & \textbf{proved} & all standard families \\[2pt]
standalone/introduction_full_survey.tex:4855:\noindent\textbf{MC1} (PBW concentration): Bar cohomology of every standard-landscape chiral algebra concentrates in PBW degrees, proved for all standard families by explicit computation.
standalone/introduction_full_survey.tex:4873:The coefficient-stability criterion (Theorem~\ref{thm:coefficient-stability-criterion}) reduces convergence to finite matrix stabilization; the uniform PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1 to MC4. The problem splits into MC4$^+$ (positive towers, solved by weight stabilization; Theorem~\ref{thm:stabilized-completion-positive}) and MC4$^0$ (resonant towers, reduced to a finite-dimensional problem by Theorem~\ref{thm:resonance-filtered-bar-cobar}). The remaining example-specific task is coefficient stabilization on finite windows and H-level target identification.
chapters/theory/higher_genus_modular_koszul.tex:1826:In particular, \textup{MC1} implies \textup{MK3} unconditionally
standalone/survey_modular_koszul_duality.tex:7780:Master conjectures MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural. MC3 holds for all simple types on the evaluation-generated core via multiplicity-free $\ell$-weights (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual problem DK-4/5 (extension beyond evaluation modules) is downstream.
standalone/survey_modular_koszul_duality.tex:7783:\noindent\textbf{MC1} (PBW concentration).
exec
/bin/zsh -lc 'rg -n "MC1" -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1129:Koszulness from MC1, and the principal level-shift theorem) give the
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/examples/w_algebras_deep.tex:1379: PBW (MC1, principal) \\
chapters/frame/preface_sections10_13_draft.tex:368:MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera; the genus-$0$ algebraic BRST/bar comparison is proved; BV=bar in the coderived category is proved for all four shadow classes (including class~M). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional.
chapters/frame/preface_sections10_13_draft.tex:372:\noindent\emph{MC1} (PBW concentration).
standalone/programme_summary.tex:2229:MC1 through MC4 are proved; MC5 is partially proved, with
standalone/programme_summary.tex:2234:\subsection{MC1: PBW concentration}
chapters/examples/bar_complex_tables.tex:1749:\index{MC1!algorithmic verification}
chapters/examples/bar_complex_tables.tex:1769:MC1 concentration ($E_2^{p,q} = 0$ for $q \neq 0$) therefore
chapters/theory/higher_genus_modular_koszul.tex:1826:In particular, \textup{MC1} implies \textup{MK3} unconditionally
chapters/frame/guide_to_main_results.tex:75:\textbf{MC1 (PBW)} &
chapters/frame/guide_to_main_results.tex:131:MC1 through MC4 are proved. MC5 is partially proved: the analytic
standalone/survey_track_a_compressed.tex:941:Master conjectures MC1 through MC4 are \emph{proved} (PBW
chapters/frame/preface.tex:4103:(MC1--MC5) organise the logical spine. MC1 through MC4 are
chapters/frame/preface.tex:4110:\noindent\emph{MC1} (PBW concentration).
chapters/connections/editorial_constitution.tex:141:MC1 & PBW concentration
chapters/connections/editorial_constitution.tex:157:resolved load-bearing layers (the MC1 entry theorem and the MC2
chapters/connections/editorial_constitution.tex:176:bridge from MC1 (Theorem~\ref{thm:uniform-pbw-bridge}).
chapters/connections/editorial_constitution.tex:206:\emph{This resolves MC1 for the standard finite-type interacting
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC1' chapters metadata/theorem_registry.md chapters/connections/concordance.tex && rg -n -i 'PBW theorem|poincare-birkhoff-witt|poincar[eé]-birkhoff-witt|\\bPBW\\b' chapters metadata/theorem_registry.md chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
Total output lines: 1122

metadata/theorem_registry.md:149:| `thm:uniform-pbw-bridge` | `theorem` | 1919 | Uniform PBW bridge from MC1 to MC4 |
chapters/connections/concordance.tex:1838:\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
chapters/connections/concordance.tex:1842: MC1 (PBW concentration) holds unconditionally for universal
chapters/connections/concordance.tex:1924: PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1
chapters/connections/concordance.tex:1981:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
chapters/connections/concordance.tex:3252:MC1 & PBW filtration & Genus-$0$ bar complex is formal:
chapters/connections/concordance.tex:9593:& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
chapters/connections/concordance.tex:11128: MC1 through MC4 are proved. MC5 is only partially
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1129:Koszulness from MC1, and the principal level-shift theorem) give the
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/examples/w_algebras_deep.tex:1379: PBW (MC1, principal) \\
chapters/examples/bar_complex_tables.tex:1749:\index{MC1!algorithmic verification}
chapters/examples/bar_complex_tables.tex:1769:MC1 concentration ($E_2^{p,q} = 0$ for $q \neq 0$) therefore
chapters/frame/preface_sections10_13_draft.tex:368:MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera; the genus-$0$ algebraic BRST/bar comparison is proved; BV=bar in the coderived category is proved for all four shadow classes (including class~M). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional.
chapters/frame/preface_sections10_13_draft.tex:372:\noindent\emph{MC1} (PBW concentration).
chapters/frame/guide_to_main_results.tex:75:\textbf{MC1 (PBW)} &
chapters/frame/guide_to_main_results.tex:131:MC1 through MC4 are proved. MC5 is partially proved: the analytic
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{theorem\\}.*PBW\" -n" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


exec
/bin/zsh -lc "rg -n \"\\\\begin\\{theorem\\}.*MC1\"" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

thinking
**Searching for theorem details**

I’m trying to locate the master theorem, which I believe relates to the MC1 entry. I might find it in the editorial constitution or related examples. The search output suggests looking at theorem registry line 2410, so I should open that file. Explorer might help me pinpoint the exact location. I need the complete statement and proof along with its dependencies, possibly within the chapters or examples. Let's wait and see what I can find!
collab wait(call_hjY9Z05Csr3XNvkslgiwkJRG)
  receivers: 019d8388-8e18-7d40-84a7-2951897027d6
exec
/bin/zsh -lc "sed -n '150,260p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 & \textbf{Partially proved} (HS-sewing; genus-$0$ algebraic) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
The historical five-master-conjecture package now consists of two
resolved load-bearing layers (the MC1 entry theorem and the MC2
universal $\Theta_\cA$ package) together with the fully resolved
MC3: \textbf{proved for all simple types} on the evaluation-generated
core. The all-types categorical prefundamental
Clebsch--Gordan closure and the DK comparison on the
evaluation-generated core are proved uniformly
\textup{(}Theorem~\ref{thm:categorical-cg-all-types},
Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
proves shifted-prefundamental generation and pro-Weyl recovery
\textup{(}Theorems~\ref{thm:shifted-prefundamental-generation},
\ref{thm:pro-weyl-recovery}\textup{)}. The residual DK-4/5
problem (extension and completion beyond evaluation modules;
Conjecture~\ref{conj:dk-compacts-completion}) is
exec
/bin/zsh -lc 'rg -n -A20 "label{thm:master-pbw" chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:label{thm:master-pbw)
             ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc 'rg -n "master-pbw" -n chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
24:(Theorems~\ref{thm:master-pbw},
194: finite-type interacting families]\label{thm:master-pbw}
449:downstream of Theorem~\textup{\ref{thm:master-pbw}},
477:Theorem~\ref{thm:master-pbw} is the \emph{entry theorem}: together
548:Theorem~\ref{thm:master-pbw} $\to$ Future~2;
798:MC1 & \textbf{Proved} (Thm~\ref{thm:master-pbw})
exec
/bin/zsh -lc 'rg -n "thm:pbw-allgenera" -n chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
743: Theorem~\textup{\ref{thm:pbw-allgenera-km}};}
746: Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}};}
751: Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}.}
757:Theorems~\ref{thm:pbw-allgenera-km}
758:and~\ref{thm:pbw-allgenera-virasoro}.
766:MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
771:\label{thm:pbw-allgenera-principal-w}
897:Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
898:Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
900:Theorem~\ref{thm:pbw-allgenera-principal-w}).
1197:\label{thm:pbw-allgenera-km}
1434:Theorem~\ref{thm:pbw-allgenera-km}.
1446:\label{thm:pbw-allgenera-virasoro}
1584:Theorem~\ref{thm:pbw-allgenera-virasoro}.
1644:Theorem~\ref{thm:pbw-allgenera-principal-w}.
1860:(Theorem~\ref{thm:pbw-allgenera-km}).
exec
/bin/zsh -lc "sed -n '1180,1320p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
and \textup{MK5} \textup{(}complementarity\textup{)} hold
at genus~$1$ without any conditional hypothesis.
\end{corollary}

\begin{proof}
MK1 (genus-$0$ Koszulity):
Theorem~\ref{thm:km-chiral-koszul}.
MK2 (Verdier):
Theorem~\ref{thm:verdier-bar-cobar}.
MK3 (modular Koszulity at $g = 1$):
Theorem~\ref{thm:pbw-genus1-km}.
MK4 and MK5 follow from MK1--MK3 by
Theorems~\ref{thm:higher-genus-inversion}
and~\ref{thm:quantum-complementarity-main}.
\end{proof}

\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
\label{thm:pbw-allgenera-km}
\index{PBW spectral sequence!all-genera degeneration|textbf}
\index{modular Koszul chiral algebra!unconditional all genera}
exec
/bin/zsh -lc "sed -n '1320,1520p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{Step~3: Killing-form contraction kills
invariants.}

The surviving $\fg$-invariant enrichment classes live in
$M_h^{\fg} \otimes H^{1,0}(\Sigma_g)$, where $M_h^{\fg}$
is spanned by the Killing-form contractions
$\kappa^{ab} \in (\fg \otimes \fg)^{\fg}$ and their
higher-weight analogs (Casimir elements in
$(\fg^{\otimes n})^{\fg}$).

The $d_2^{\mathrm{PBW}}$ differential, the $(1)$-product
contraction, which lowers PBW degree by~$2$ and
involves the level~$k$, acts on the $\fg$-factor of
the enrichment independently of the
$H^{1,0}(\Sigma_g)$ multiplicity. At genus~$g$, the
invariant enrichment at bar degree~$2$, weight~$2$, is
\[
\kappa^{ab}(J^a_{-1} \otimes J^b_{-1})
\;\otimes\; H^{1,0}(\Sigma_g),
\]
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1180,1520p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1180	and \textup{MK5} \textup{(}complementarity\textup{)} hold
  1181	at genus~$1$ without any conditional hypothesis.
  1182	\end{corollary}
  1183	
  1184	\begin{proof}
  1185	MK1 (genus-$0$ Koszulity):
  1186	Theorem~\ref{thm:km-chiral-koszul}.
  1187	MK2 (Verdier):
  1188	Theorem~\ref{thm:verdier-bar-cobar}.
  1189	MK3 (modular Koszulity at $g = 1$):
  1190	Theorem~\ref{thm:pbw-genus1-km}.
  1191	MK4 and MK5 follow from MK1--MK3 by
  1192	Theorems~\ref{thm:higher-genus-inversion}
  1193	and~\ref{thm:quantum-complementarity-main}.
  1194	\end{proof}
  1195	
  1196	\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
  1197	\label{thm:pbw-allgenera-km}
  1198	\index{PBW spectral sequence!all-genera degeneration|textbf}
  1199	\index{modular Koszul chiral algebra!unconditional all genera}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1520,1660p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1520	
  1521	No further mechanism is needed: neither a Kac--Moody-style Killing
  1522	contraction nor the quartic-pole term $T_{(3)}T = c/2$ is required.
  1523	The enrichment dies already by the $L_0$-action.
  1524	
  1525	The same argument applies to the antiholomorphic factor
  1526	$H^{0,1}(\Sigma_g)$, since $L_0$ acts only on the vertex-algebra
  1527	factor. Hence the full $H^1(\Sigma_g,\bC)$-enrichment is eliminated.
  1528	By bounded-below convergence
  1529	\textup{(}\ref{item:pbw-bounded} of
  1530	Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}, the spectral
  1531	sequence converges in each bidegree, yielding
  1532	$E_\infty(g) = E_\infty(0)$.
  1533	
  1534	The computation module
  1535	\texttt{compute/lib/virasoro\_pbw\_genus1.py}
  1536	verifies through conformal weight~$10$ that
  1537	$\dim M_h = p(h-2)$,
  1538	$L_0 = h \cdot \mathrm{id}_{M_h}$,
  1539	the full $\mathfrak{sl}_2$ commutator $[L_1, L_{-1}] = 2L_0$,
wait(call_hjY9Z05Csr3XNvkslgiwkJRG) timed out:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1656,1960p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1656	\begin{theorem}[Universal PBW enrichment-killing for chiral
  1657	 algebras with conformal vector; \ClaimStatusProvedHere]
  1658	\label{thm:pbw-universal-semisimple}
  1659	\index{PBW spectral sequence!unique-weight-2 criterion|textbf}
  1660	\index{PBW spectral sequence!universal semisimple enrichment-killing|textbf}
  1661	\index{modular Koszul chiral algebra!unique-weight-2 criterion|textbf}
  1662	\index{modular Koszul chiral algebra!semisimple enrichment-killing|textbf}
  1663	\textup{[Regime: curved-central
  1664	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1665	
  1666	Let $\cA$ be a chiral algebra defined by local OPE relations,
  1667	admitting a PBW filtration by conformal weight, and satisfying:
  1668	\begin{enumerate}[label=\textup{(\alph*)}]
  1669	\item the augmentation ideal $\bar{V}_\cA$ is
  1670	 positively graded: every homogeneous state has
  1671	 conformal weight $h \geq h_{\min} > 0$;
  1672	\item among all generators, exactly one has conformal
  1673	 weight~$2$, namely the stress tensor~$T$, with
  1674	 $T_{(1)} = L_0$.
  1675	\end{enumerate}

thinking
**Searching for theorem details**

I need to consider polling later, but for now, I’m diving into the manual. I think the MC1 entry theorem could likely be thm:master-pbw from the chapters/examples/kac_moody.tex file. I should search for that exact label to confirm. It’s interesting to think about how it all connects, and I want to ensure I get the right information for this theorem!
codex
The search surface is large, but it already narrows the likely entry theorem to `thm:master-pbw`. I’m now reading that theorem and the local proof context in full, then I’ll descend into each cited PBW family theorem and the filtration criterion it relies on.
exec
/bin/zsh -lc "sed -n '150,320p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:master-pbw\\}|begin\\{theorem\\}\\[.*master-pbw|thm:master-pbw|master-pbw\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,320p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,320p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The Feigin--Frenkel shift
$k \mapsto -k - 2h^\vee$ is Verdier duality on
configuration spaces
(Theorem~\ref{thm:bar-cobar-verdier}).
In the WZW model, this shift exchanges holomorphic
and anti-holomorphic sectors; geometrically, it reverses
worldsheet orientation. The same involution governs modular
$S$-transformations of $\widehat{\mathfrak{g}}_k$-characters, the
$q \mapsto q^{-1}$ symmetry of $U_q(\mathfrak{g})$ at
$q = e^{\pi i/(k+h^\vee)}$
(Theorem~\ref{thm:km-quantum-groups}), and 4d S-duality on circles.
Each is a projection of Verdier duality on the Fulton--MacPherson
compactification.

\begin{remark}[Shadow obstruction tower for Kac--Moody]\label{rem:km-master-mc}
For $\widehat{\mathfrak{g}}_k$ at generic level, the shadow
obstruction tower in the modular convolution algebra
$\mathfrak{g}^{\mathrm{mod}}_\cA$
(Definition~\ref{def:modular-convolution-dg-lie}) has scalar
minimal package $\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$
 succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:1052:Theorem~\ref{thm:master-pbw} (MC1 for principal $\mathcal{W}$-algebras).
chapters/examples/w_algebras_deep.tex:1152: \textup{(}Theorem~\textup{\ref{thm:master-pbw})},
chapters/examples/w_algebras_deep.tex:1226:Theorem~\ref{thm:master-pbw} (MC1 for principal
chapters/theory/higher_genus_modular_koszul.tex:28752:By PBW concentration (Theorem~\ref{thm:master-pbw}),
chapters/connections/outlook.tex:664:\phantomsection\label{thm:master-pbw}
chapters/theory/bar_cobar_adjunction_inversion.tex:3792:(Theorem~\ref{thm:master-pbw}). The Virasoro algebra has a
chapters/connections/editorial_constitution.tex:24:(Theorems~\ref{thm:master-pbw},
chapters/connections/editorial_constitution.tex:194: finite-type interacting families]\label{thm:master-pbw}
chapters/connections/editorial_constitution.tex:449:downstream of Theorem~\textup{\ref{thm:master-pbw}},
chapters/connections/editorial_constitution.tex:477:Theorem~\ref{thm:master-pbw} is the \emph{entry theorem}: together
chapters/connections/editorial_constitution.tex:548:Theorem~\ref{thm:master-pbw} $\to$ Future~2;
chapters/connections/editorial_constitution.tex:798:MC1 & \textbf{Proved} (Thm~\ref{thm:master-pbw})
 succeeded in 51ms:
In the three-pillar architecture
(\S\ref{sec:concordance-three-pillars}):
(i)~the \v{C}ech complex of $\mathcal{W}_N$ has secondary Borcherds
operations $j'_{(p,q,r)} \neq 0$ at \emph{all} degrees; this is
the mixed archetype, the only case where the
$\mathrm{Ch}_\infty$-structure is genuinely infinite. The quintic
forced obstruction ($o^{(5)}_{\mathrm{Vir}} \neq 0$) is the
statement that the degree-$5$ secondary Borcherds operation is
non-trivializable;
(ii)~the convolution $sL_\infty$-algebra
$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
all transferred brackets $\ell_k^{\mathrm{tr}} \neq 0$ for $k \geq 3$.
Homotopy invariance (Theorem~\ref{thm:shadow-homotopy-invariance})
guarantees that the shadow obstruction tower is an invariant of
$\mathcal{W}_N$ up to quasi-isomorphism; the contact Virasoro invariant
$Q^{\mathrm{contact}}_{\mathrm{Vir}} = 10/[c(5c+22)]$ is its
weight-$4$ shadow;
(iii)~the Virasoro element provides topological resonance reduction
(Khan--Zeng~\cite{KZ25}): the 3d theory is fully topological, and
log-FM degeneration geometry governs the higher-genus shadow
 succeeded in 51ms:
 & \textbf{Partially proved} (HS-sewing; genus-$0$ algebraic) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
The historical five-master-conjecture package now consists of two
resolved load-bearing layers (the MC1 entry theorem and the MC2
universal $\Theta_\cA$ package) together with the fully resolved
MC3: \textbf{proved for all simple types} on the evaluation-generated
core. The all-types categorical prefundamental
Clebsch--Gordan closure and the DK comparison on the
evaluation-generated core are proved uniformly
\textup{(}Theorem~\ref{thm:categorical-cg-all-types},
Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
proves shifted-prefundamental generation and pro-Weyl recovery
\textup{(}Theorems~\ref{thm:shifted-prefundamental-generation},
\ref{thm:pro-weyl-recovery}\textup{)}. The residual DK-4/5
problem (extension and completion beyond evaluation modules;
Conjecture~\ref{conj:dk-compacts-completion}) is
exec
/bin/zsh -lc 'rg -n "pbw-genus1-km" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
907:\label{thm:pbw-genus1-km}
1190:Theorem~\ref{thm:pbw-genus1-km}.
1230:(Theorem~\ref{thm:pbw-genus1-km}) establishes a
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '840,940p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   840	\[
   841	\bigoplus_{2 \leq h \leq H}
   842	M_h \otimes H^{1,0}(\Sigma_g),
   843	\]
   844	the matrix of $d_2^{\mathrm{PBW}}$ is block upper triangular:
   845	\begin{enumerate}[label=\textup{(\roman*)}]
   846	\item the diagonal block on conformal weight~$h$ can only come from
   847	 weight-$2$ states, hence only from the stress tensor~$T$;
   848	\item all contributions from states of weight $> 2$ land in higher
   849	 conformal weights and are therefore strictly above the diagonal.
   850	\end{enumerate}
   851	But $T_{(1)} = L_0$, so on $M_h$ one has
   852	\[
   853	T_{(1)}\big|_{M_h}
   854	\;=\;
   855	L_0\big|_{M_h}
   856	\;=\;
   857	h \cdot \mathrm{id}_{M_h}.
   858	\]
   859	Consequently the diagonal block of $d_2^{\mathrm{PBW}}$ on
collab wait(call_IPzNS2whsffKW31NlIG7TTON)
  receivers: 019d8388-8e18-7d40-84a7-2951897027d6
exec
/bin/zsh -lc 'rg -n "pbw-koszulness-criterion" -n chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
874:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)},
939:Theorem~\ref{thm:pbw-koszulness-criterion}.
1065:Theorem~\ref{thm:pbw-koszulness-criterion}), the
1375:Theorem~\ref{thm:pbw-koszulness-criterion}), the spectral
1530:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}, the spectral
1753:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}
1808:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)},
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '150,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   150	 & \textbf{Partially proved} (HS-sewing; genus-$0$ algebraic) \\
   151	\bottomrule
   152	\end{tabular}
   153	\end{center}
   154	
   155	\noindent
   156	The historical five-master-conjecture package now consists of two
   157	resolved load-bearing layers (the MC1 entry theorem and the MC2
   158	universal $\Theta_\cA$ package) together with the fully resolved
   159	MC3: \textbf{proved for all simple types} on the evaluation-generated
   160	core. The all-types categorical prefundamental
   161	Clebsch--Gordan closure and the DK comparison on the
   162	evaluation-generated core are proved uniformly
   163	\textup{(}Theorem~\ref{thm:categorical-cg-all-types},
   164	Corollary~\ref{cor:dk23-all-types}\textup{)}. Type~$A$
   165	proves shifted-prefundamental generation and pro-Weyl recovery
   166	\textup{(}Theorems~\ref{thm:shifted-prefundamental-generation},
   167	\ref{thm:pro-weyl-recovery}\textup{)}. The residual DK-4/5
   168	problem (extension and completion beyond evaluation modules;
   169	Conjecture~\ref{conj:dk-compacts-completion}) is
exec
/bin/zsh -lc 'rg -n "MC1" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1838:\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
1842: MC1 (PBW concentration) holds unconditionally for universal
1924: PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1
1981:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
3252:MC1 & PBW filtration & Genus-$0$ bar complex is formal:
9593:& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
11128: MC1 through MC4 are proved. MC5 is only partially
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1820,1860p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1820	\item The MC3 categorical lift
  1821	 (Theorem~\ref{thm:categorical-cg-all-types}) proceeds one slot at a
  1822	 time. The prefundamental CG closure
  1823	 (Proposition~\ref{prop:prefundamental-clebsch-gordan}) works at the
  1824	 character level ($K_0$) precisely because characters live in one slot;
  1825	 the categorical lift requires both.
  1826	\item Any claim of two-sided functoriality for bulk/boundary/line
  1827	 constructions must be replaced by a homotopy-coherent correspondence
  1828	 formalism.
  1829	\end{itemize}
  1830	\end{remark}
  1831	
  1832	\begin{remark}[Three-pillar architecture and the MC open problems]
  1833	\label{rem:three-pillar-mc-unification}
  1834	\index{three-pillar architecture!MC open problems}
  1835	\index{MC open problems!three-pillar unification}
  1836	The three-pillar architecture determines the MC resolution strategy:
  1837	\begin{itemize}
  1838	\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
  1839	 element in the modular convolution $sL_\infty$-algebra; the
exec
/bin/zsh -lc "nl -ba standalone/programme_summary.tex | sed -n '2220,2260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2220	\label{sec:mc-programme}
  2221	% ====================================================================
  2222	
  2223	The MC programme converts the geometric structure of the
  2224	bar complex into five concrete mathematical problems, each
  2225	asking whether a structural property of the universal MC
  2226	element~$\Theta_\cA$ persists under a specific operation:
  2227	PBW concentration, bar-intrinsic existence, categorical
  2228	generation, inverse-limit completion, and analytic sewing.
  2229	MC1 through MC4 are proved; MC5 is partially proved, with
  2230	the analytic HS-sewing package established at all genera
  2231	and the genuswise BV/BRST/bar identification conjectural.
  2232	
  2233	% ====================================================================
  2234	\subsection{MC1: PBW concentration}
  2235	\label{ssec:mc1}
  2236	% ====================================================================
  2237	
  2238	The PBW spectral sequence of~$B(\cA)$ collapses at~$E_2$
  2239	for every freely strongly generated chiral algebra. Free

thinking
**Structuring comprehensive theorem reference summary**

I’m organizing a clear final answer that includes primary file paths with line ranges for theorems and proofs, theorem labels and environments, cited dependencies with file paths and lines, plus any cross-volume duplicates with their locations. I’m also making sure to mention relevant status tags like `ClaimStatusProvedHere` near key labels and note aggregator references like `MC1` if they appear among duplicates, all while keeping the summary plain and concise.
codex
1) **Primary proof surface** – `chapters/theory/higher_genus_modular_koszul.tex:1196-1812` hosts the MC1 proofs: 
   - lines **1196‑1225** define `thm:pbw-allgenera-km` with its `\ClaimStatusProvedHere` tag; the accompanying proof runs through **1229‑1391**. 
   - lines **1445‑1533** contain `thm:pbw-allgenera-virasoro` plus lines **1471‑1543** for its proof. 
   - lines **1656‑1812** cover `thm:pbw-universal-semisimple` (unique-weight‑2 criterion) and its proof, which underpins the general principal‑$\mathcal{W}$ MC1 argument; the principal family corollary immediately follows.

2) **Theorems/environments** – MC1 is packaged as 
   - `\begin{theorem}[PBW degeneration at all genera for Kac–Moody; \ClaimStatusProvedHere]` (`thm:pbw-allgenera-km`, lines 1196‑1225), 
   - `\begin{theorem}[PBW degeneration at all genera for Virasoro; \ClaimStatusProvedHere]` (`thm:pbw-allgenera-virasoro`, lines 1445‑1468), 
   - `\begin{theorem}[Universal PBW enrichment-killing for chiral algebras with conformal vector; \ClaimStatusProvedHere]` (`thm:pbw-universal-semisimple`, lines 1656‑1706), together with the derived corollaries (lines 1393‑1654) that state the modular‑Koszul consequences.

3) **Cited dependencies (file + line)** – the proofs explicitly reference:
   - `chapters/theory/higher_genus_modular_koszul.tex:906‑927` `thm:pbw-genus1-km` (the genus‑1 Whitehead/Killing mechanism) used by the KM proof at line 1229. 
   - `chapters/theory/higher_genus_modular_koszul.tex:874‑906` `thm:pbw-koszulness-criterion` (bounded‑below convergence and PBW filtration control) cited in the KM conclusion (`lines 1374‑1377`), in the Virasoro conclusion (`1529‑1532`), and again when invoking the universal semisimple analysis (`1751‑1756`, `1808‑1809`). 
   - The Virasoro proof also flags `eq:e1-decomposition-genusg`/`eq:enrichment-factorization` (lines 1255‑1267) and `Computation~\ref{comp:virasoro-vacuum}` (line 1486‑1487) to control dimensions; 
   - The universal semisimple argument leans on the same factorization (`eq:enrichment-factorization`, lines 1264‑1267) plus the Whitehead‐CE vanishing referenced around lines 1769‑1787.

4) **Cross‑volume duplicates/status tags** – the MC1 bundle is summarized elsewhere: 
   - `chapters/connections/editorial_constitution.tex:193‑215` states `thm:master-pbw` with `\ClaimStatusProvedHere`, listing the three family theorems and `thm:pbw-universal-semisimple`. 
   - `chapters/connections/concordance.tex:1838‑1860` repeats the MC1 status (“MC1 (PBW concentration) holds unconditionally for …”, cites `prop:pbw-universality`). 
   - Survey/summary files such as `standalone/programme_summary.tex:2229‑2245` also restate “MC1 through MC4 are proved; MC1 (PBW concentration) …”.
wait(call_IPzNS2whsffKW31NlIG7TTON) 1 agents complete:
  019d8388-8e18-7d40-84a7-2951897027d6 completed: "1) **Primary proof surface** – `chapters/theory/higher_genus_modular_koszul.tex:1196-1812` hosts the MC1 proofs: 
   - l…"

thinking
**Verifying modules and theorems**

I’ve located higher_genus_modular_koszul, which is great! I wonder if I really need to do a manual search for more. But I do need the actual file contents to check out the relevant ranges and dependencies. It seems the pbw-koszulness-criterion might not be in the same file. The lines in higher_genus_modular_koszul suggest it might be a local theorem. I’ll also need to verify the information in the original theorem_registry. Let’s open the relevant sections!
codex
The actual MC1 proof surface is in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1196), not the summary theorem in the constitution chapter. I’m reading the full Kac–Moody, Virasoro, and semisimple/`W` proofs with line numbers, then I’ll trace every cited result they import.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '696,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '188,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '900,1825p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   696	\begin{theorem}[PBW criterion for chiral Koszulness; \ClaimStatusProvedHere]
   697	\label{thm:pbw-koszulness-criterion}
   698	\index{Koszul property!PBW criterion|textbf}
   699	\textup{[Regime: filtered-complete
   700	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   701	
   702	Let $\cA$ be a chiral algebra with PBW filtration
   703	$F_0 \subset F_1 \subset \cdots \subset \cA$
   704	such that the associated graded
   705	$\operatorname{gr}_F \cA$ is a commutative chiral algebra
   706	(equivalently, a vertex Poisson algebra).
   707	Suppose:
   708	\begin{enumerate}
   709	\item\label{item:pbw-flat} The filtration is \emph{flat}: each $F_p/F_{p-1}$ is a free
   710	 $\cO_X$-module of finite rank in each conformal weight.
   711	\item\label{item:pbw-classical-koszul} The associated graded $\operatorname{gr}_F \cA$
   712	 is classically Koszul: the Koszul complex
   713	 $\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA$
   714	 is acyclic in positive degrees.
   715	\item\label{item:pbw-bounded} For each bar degree $n$ and conformal weight $h$, the
 succeeded in 52ms:
   188	while the tree-level amplitude pairing requires the additional
   189	hypothesis isolated in
   190	Corollary~\ref{cor:string-amplitude-genus0}. Periodicity is an
   191	orthogonal weak flank, not a link in this dependency chain.
   192	
   193	\begin{theorem}[Higher-genus PBW concentration for the standard
   194	 finite-type interacting families]\label{thm:master-pbw}
   195	\ClaimStatusProvedHere{}
   196	The genus-$g$ PBW spectral sequence concentrates at all genera for the
   197	three standard finite-type interacting families treated in the proved
   198	core: affine Kac--Moody
   199	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
   200	Virasoro
   201	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}}\textup{)},
   202	and principal finite-type $\mathcal{W}$-algebras, including higher
   203	$\mathcal{W}_N$
   204	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}\textup{)}.
   205	
   206	\emph{This resolves MC1 for the standard finite-type interacting
   207	families. Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
 succeeded in 51ms:
   900	Theorem~\ref{thm:pbw-allgenera-principal-w}).
   901	Open: non-principal families; the $\mathcal{W}_\infty$
   902	inverse-limit package
   903	(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
   904	\end{remark}
   905	
   906	\begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
   907	\label{thm:pbw-genus1-km}
   908	\index{PBW spectral sequence!genus-1 degeneration|textbf}
   909	\index{modular Koszul chiral algebra!genus-1 unconditional}
   910	\textup{[Regime: curved-central
   911	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   912	
   913	For any simple Lie algebra~$\fg$ and generic level
   914	$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
   915	genus-$1$ bar complex
   916	$\bar{B}^{(1)}(\widehat{\fg}_k)$ has concentrated
   917	$E_\infty$ page: the enrichment from $H^1(E_\tau)$
   918	is eliminated by~$d_1$ and~$d_2$
   919	\textup{(}non-trivial $\fg$-modules at~$E_2$

thinking
**Searching for references**

I need to locate line references and the actual content of the principal W theorem or its corollary. It seems like the specific theorem, such as "thm:pbw-allgenera-principal-w" hasn’t appeared in my previous searches. I’ll look into it to ensure I get the accurate information. Let’s see what I can find so I can provide a clear explanation! This should help clarify any uncertainties related to the theorem.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '760,830p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1810,1875p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:pbw-allgenera-principal-w\\}|label\\{thm:pbw-allgenera-km\\}|label\\{thm:pbw-allgenera-virasoro\\}|label\\{thm:pbw-universal-semisimple\\}|label\\{comp:virasoro-vacuum\\}|label\\{thm:km-chiral-koszul\\}|label\\{thm:virasoro-chiral-koszul\\}|label\\{thm:w-algebra-koszul-main\\}|label\\{thm:bar-cobar-spectral-sequence\\}\" chapters/theory chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   760	
   761	By completeness of the filtration and the bounded-below hypothesis,
   762	the spectral sequence converges:
   763	$E_\infty = \operatorname{gr} H^*(K)$.
   764	Since $E_\infty$ is concentrated in degree~$0$,
   765	we conclude $H^n(K) = 0$ for $n > 0$.
   766	\end{proof}
   767	
   768	\begin{remark}[Relation to classical Koszulness]
   769	\label{rem:classical-to-chiral-koszul}
   770	The PBW criterion reduces chiral Koszulness to the classical statement that $\operatorname{gr}_F \cA$ is Koszul.
   771	For Kac--Moody and Virasoro algebras, $\operatorname{gr}_F \cA$ is a polynomial algebra (Koszul by Priddy's theorem); semisimplicity of $\mathfrak{g}$ is not required.
   772	\end{remark}
   773	
   774	\begin{theorem}[Affine Kac--Moody algebras are chiral Koszul; \ClaimStatusProvedHere]
   775	\label{thm:km-chiral-koszul}
   776	\index{Kac--Moody algebra!chiral Koszulness|textbf}
   777	\textup{[Regime: curved-central
   778	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   779	
 succeeded in 51ms:
  1810	
  1811	The antiholomorphic factor is handled identically.
  1812	\end{proof}
  1813	
  1814	\begin{proposition}[Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses;
  1815	 \ClaimStatusProvedHere]
  1816	\label{prop:hook-pbw}
  1817	\index{W-algebra@$\mathcal{W}$-algebra!hook-type!PBW hypotheses|textbf}
  1818	\index{PBW spectral sequence!hook-type W-algebras|textbf}
  1819	For $N \geq 3$ and $1 \leq r \leq N-2$, the hook-type
  1820	$\mathcal{W}$-algebra
  1821	$\mathcal{W}^k(\mathfrak{sl}_N, f_{(N-r,\,1^r)})$ at generic level
  1822	satisfies hypotheses~\textup{(a)--(b)} of
  1823	Theorem~\textup{\ref{thm:pbw-universal-semisimple}}. When
  1824	$r \leq N-3$, the centralizer $\mathfrak{g}^f$ contains a
  1825	semisimple Levi factor, and hypothesis~\textup{(c)} holds as well.
  1826	In particular, \textup{MC1} implies \textup{MK3} unconditionally
  1827	for these algebras.
  1828	\end{proposition}
  1829	
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:771:\label{thm:pbw-allgenera-principal-w}
chapters/theory/higher_genus_modular_koszul.tex:1197:\label{thm:pbw-allgenera-km}
chapters/theory/higher_genus_modular_koszul.tex:1446:\label{thm:pbw-allgenera-virasoro}
chapters/theory/higher_genus_modular_koszul.tex:1658:\label{thm:pbw-universal-semisimple}
chapters/theory/bar_cobar_adjunction_inversion.tex:2024:\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
chapters/examples/bar_complex_tables.tex:278:\begin{computation}[Virasoro vacuum module: low-weight states]\label{comp:virasoro-vacuum}
chapters/examples/w_algebras.tex:309:\begin{theorem}[\texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent; \ClaimStatusProvedHere]\label{thm:w-algebra-koszul-main}
chapters/theory/chiral_koszul_pairs.tex:775:\label{thm:km-chiral-koszul}
chapters/theory/chiral_koszul_pairs.tex:830:\label{thm:virasoro-chiral-koszul}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '740,905p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '830,900p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/bar_complex_tables.tex | sed -n '260,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   740	\item affine Kac--Moody algebras $\widehat{\mathfrak{g}}_k$ at generic
   741	 level \textup{(}$k \notin \mathbb{Q}_{< 0}$ minus finitely many
   742	 points\textup{)}, \emph{now unconditional by
   743	 Theorem~\textup{\ref{thm:pbw-allgenera-km}};}
   744	\item the Virasoro algebra $\mathrm{Vir}_c$ at generic central charge
   745	 $c$, \emph{now unconditional by
   746	 Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}};}
   747	\item principal finite-type $\mathcal{W}$-algebras
   748	 $\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ at generic level,
   749	 in particular higher $\mathcal{W}_N$
   750	 , \emph{now unconditional by
   751	 Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}.}
   752	\end{enumerate}
   753	\end{proposition}
   754	
   755	\begin{proof}
   756	The Kac--Moody and Virasoro statements are exactly
   757	Theorems~\ref{thm:pbw-allgenera-km}
   758	and~\ref{thm:pbw-allgenera-virasoro}.
   759	
 succeeded in 52ms:
   830	\label{thm:virasoro-chiral-koszul}
   831	\index{Virasoro algebra!chiral Koszulness|textbf}
   832	\textup{[Regime: curved-central\textup{;}
   833	Convention~\textup{\ref{conv:regime-tags}}.]}
   834	
   835	For any central charge $c \in \bC$, the Virasoro vertex algebra
   836	$\mathrm{Vir}_c$ is chiral Koszul.
   837	\end{theorem}
   838	
   839	\begin{proof}
   840	The PBW filtration on $\mathrm{Vir}_c$ is defined by the
   841	number of Virasoro mode applications:
   842	\[
   843	F_p = \operatorname{span}\{L_{-n_1} \cdots L_{-n_r}
   844	|0\rangle : r \leq p,\; n_i \geq 2\}.
   845	\]
   846	
   847	\emph{Hypothesis~\ref{item:pbw-flat}.}
   848	Each $F_p/F_{p-1} \cong S^p(V)$ where
   849	$V = \bigoplus_{n \geq 2} \bC \cdot L_{-n}$
 succeeded in 52ms:
   260	$2$ & $0$ & $(z\!-\!w)^{-3}$ & (absent) \\
   261	$1$ & $2T$ & $(z\!-\!w)^{-2}$ & conformal weight \\
   262	$0$ & $\partial T$ & $(z\!-\!w)^{-1}$ & translation
   263	\end{tabular}
   264	\end{center}
   265	
   266	\emph{Key difference from Kac--Moody:} the affine Lie algebra $\widehat{\mathfrak{g}}_k$ has OPE poles up to order~$2$, while the Virasoro has a quartic pole. This extra pole produces the curvature element $m_0 = (c/2)\cdot\mathbf{1}$ in the $A_\infty$ structure (cf.\ Computation~\ref{comp:virasoro-bar-diff} below).
   267	This curvature $m_0 = c/2$ is the scalar component of the
   268	universal Maurer--Cartan class
   269	$\Theta_{\mathrm{Vir}_c}^{\min} = (c/2)\cdot\eta\otimes\Lambda$
   270	(Theorem~\ref{thm:explicit-theta}). At $c = 0$ (the Witt algebra),
   271	$\Theta_{\mathrm{Vir}_0}^{\min} = 0$ and the bar complex is
   272	uncurved; this does not determine the higher-degree shadow obstruction tower. At
   273	general~$c$, the scalar curvature propagates to genus~$1$ universally
   274	and, for this single-generator algebra, to all genera via the Hodge classes
   275	$\lambda_g$.
   276	\end{computation}
   277	
   278	\begin{computation}[Virasoro vacuum module: low-weight states]\label{comp:virasoro-vacuum}
   279	The augmentation ideal $\bar{V} = V/\mathbb{C}\cdot|0\rangle$ of the Virasoro vacuum module has a basis of states created by $L_{-n}$ (for $n \geq 2$) applied to the vacuum:



thinking
**Evaluating computation discrepancies**

I'm noticing a discrepancy in the computation table, specifically regarding p_{\ge2}(h) = p(h) - p(h-1) for h=5. It shows a mismatch since p(3) should equal 3, not 2. This could have medium to high severity since it indicates a potential misinterpretation of the source. Even if it's not essential to the proof, it might still affect the logic if p(h-2) is used implicitly. Additionally, I've spotted some concerns in thm:master-pbw about the proof status.
thinking
**Investigating theorem proof status**

I’m wondering if this repository sometimes omits proofs for summary theorems. I should find out if a proof is provided later since user has requested it. The theorem thm:master-pbw lacks a direct proof, which could be a critical issue since it was specifically asked for. However, if it's just a restatement with proper citations, maybe it’s not a significant problem. The citation might suffice as a proof if it's from the referenced family theorems, but I need to clarify the ClaimStatusProvedHere.
thinking
**Assessing theorem proof validity**

I'm considering that if the family theorems are in the same volume, the "proved here" status might be acceptable for the theorem as an index theorem summarizing information. However, in a code review mindset, I need to prioritize looking for bugs or regressions. This issue might be deemed minor if it doesn't present an actual falsehood. On a more serious note, I have concerns about the genus-1 Kac-Moody proof, specifically that Step 1 claims the enrichment cochains aren't d0-exact, which raises questions.
codex
I’ve got the full proof bodies now. There is already one concrete internal mismatch in the Virasoro proof surface, and I’m checking whether it’s only cosmetic or whether it masks a deeper filtration error. Next I’m tracing the unsupported decomposition/factorization claims and every imported reference they lean on.
exec
/bin/zsh -lc 'rg -n "eq:e1-decomposition-genusg|eq:enrichment-factorization|eq:e1-decomposition-genus1|enrichment factorization|PBW spectral sequence concentrates at all genera for the three standard|thm:master-pbw|thm:pbw-genus1-km" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{rem:ds-hierarchy-summary\\}|label\\{def:modular-koszul-chiral\\}|label\\{thm:higher-genus-inversion\\}|label\\{thm:quantum-complementarity-main\\}|label\\{thm:modular-characteristic\\}\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '680,740p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:3792:(Theorem~\ref{thm:master-pbw}). The Virasoro algebra has a
chapters/theory/higher_genus_modular_koszul.tex:814:\eqref{eq:e1-decomposition-genusg} and
chapters/theory/higher_genus_modular_koszul.tex:815:\eqref{eq:enrichment-factorization}. Here
chapters/theory/higher_genus_modular_koszul.tex:907:\label{thm:pbw-genus1-km}
chapters/theory/higher_genus_modular_koszul.tex:931:enrichment factorization, Whitehead acyclicity, and the
chapters/theory/higher_genus_modular_koszul.tex:974:\begin{equation}\label{eq:e1-decomposition-genus1}
chapters/theory/higher_genus_modular_koszul.tex:1190:Theorem~\ref{thm:pbw-genus1-km}.
chapters/theory/higher_genus_modular_koszul.tex:1230:(Theorem~\ref{thm:pbw-genus1-km}) establishes a
chapters/theory/higher_genus_modular_koszul.tex:1255:\begin{equation}\label{eq:e1-decomposition-genusg}
chapters/theory/higher_genus_modular_koszul.tex:1264:\begin{equation}\label{eq:enrichment-factorization}
chapters/theory/higher_genus_modular_koszul.tex:1480:\eqref{eq:e1-decomposition-genusg} and
chapters/theory/higher_genus_modular_koszul.tex:1481:\eqref{eq:enrichment-factorization}. Here
chapters/theory/higher_genus_modular_koszul.tex:1709:The enrichment factorization~\eqref{eq:enrichment-factorization}
chapters/theory/higher_genus_modular_koszul.tex:1866:The structural input is the enrichment factorization
chapters/theory/higher_genus_modular_koszul.tex:1868:(\ref{eq:enrichment-factorization}), which separates local OPE
chapters/theory/higher_genus_modular_koszul.tex:1938:factorization~\eqref{eq:enrichment-factorization},
chapters/theory/higher_genus_modular_koszul.tex:28752:By PBW concentration (Theorem~\ref{thm:master-pbw}),
 succeeded in 51ms:
chapters/examples/w_algebras.tex:522:\label{rem:ds-hierarchy-summary}
chapters/theory/higher_genus_modular_koszul.tex:535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
chapters/theory/higher_genus_modular_koszul.tex:2628:\label{thm:modular-characteristic}
chapters/theory/higher_genus_complementarity.tex:456:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 succeeded in 52ms:
   680	(Proposition~\ref{prop:dg-shifted-comparison}).
   681	\end{enumerate}
   682	For simple Lie symmetry, MK6--MK7 follow from
   683	Lemma~\ref{lem:mk67-from-mc2}. MK8 remains programmatic.
   684	\end{remark}
   685	
   686	\begin{proposition}[Free-field examples are modular pre-Koszul; \ClaimStatusProvedHere]
   687	\label{prop:standard-examples-modular-koszul}
   688	\index{modular Koszul chiral algebra!examples}
   689	\textup{[Regime: quadratic
   690	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   691	
   692	The following chiral algebras satisfy the antecedent axioms
   693	\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
   694	Theorems~\textup{\ref{thm:higher-genus-inversion}}
   695	and~\textup{\ref{thm:quantum-complementarity-main}} then supply
   696	\textup{MK4--MK5}, so they are modular Koszul:
   697	\begin{enumerate}[label=\textup{(\alph*)}]
   698	\item the Heisenberg algebra $\mathcal{H}_\kappa$
   699	 (Convention~\textup{\ref{conv:heisenberg-kappa-notation}}) at any




thinking
**Reviewing mathematical concepts**

I'm thinking about reading proof of a specific theorem. I want to check if I need to look at the continuation after 1812, though that seems not relevant. I might also need to explore the definition of modular-koszul-chiral MK3 and check its exact scope to see if genus 0 is included. I should probably read the lines around the definition too, just to get a better understanding of everything involved.
thinking
**Examining theorem aspects**

I need to examine the theorem related to the pbw-koszulness criterion. There's a potential issue regarding the filtration induced by F and whether F_i on the bar complex has been adequately defined. The user asked for a reading and report, so I could run commands to check the compute scripts for verifying claims about matrix ranks or other computations. It seems running scripts for evidence gathering is fine, focusing on verification for the user’s request.
thinking
**Investigating theorem details**

I need to think about whether direct computation is truly necessary unless the claim depends on it. I might run tests to check boundaries or counterexamples if they seem useful. Some potential issues to investigate include the lack of proof in the master-pbw summary theorem, which may inflate its status. Additionally, in the Kac-Moody proof, only H^{1,0} is used at first, and later H^{0,1} is added. I need to verify if antiholomorphic forms should even appear in this context, especially regarding the algebraic curve and complex de Rham forms.
thinking
**Clarifying algebraic de Rham representations**

On a smooth projective complex curve, the algebraic de Rham H^1_dR is represented by algebraic 1-forms alongside forms of the second kind, rather than literally by H^{0,1}. Since this is related to chiral algebra on algebraic curves, invoking antiholomorphic forms could be a mismatch in category or convention. However, if the theorem pertains to curved-central topology, I need to check if that's permissible. They do mention smooth projective curves and FM compactification, which are important considerations.
exec
/bin/zsh -lc "rg -n \"Sigma\\(\\\\fg\\)|\\\\Sigma\\(\\\\fg\\)|generic level|critical level|k \\\\notin \\\\Sigma\\(\\\\fg\\)\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"H\\"'^'"\\{0,1\\}|antiholomorphic|Omega\\"'^'"\\{n-1\\}_\\\\log|smooth projective curve|algebraic de Rham|H\\"'^'"\\{1,0\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Whitehead|Chevalley--Eilenberg theorem|truncated loop algebra|C\\"'^'"\\*\\(\\\\fg, M_h\\)|Lie bracket of the truncated loop algebra|current algebra\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:H\^\{0,1\}|antiholomorphic|Omega\^\{n-1\}_\log|smooth projective curve|algebraic de Rham|H\^\{1,0\})
                                                 ^^
error: unrecognized escape sequence
 exited 2 in 50ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:1715:by Whitehead vanishing \textup{(}for semisimple~$\fg$\textup{)}.
chapters/theory/chiral_koszul_pairs.tex:2546:current algebra bracket. The chain of implications is:
chapters/theory/chiral_koszul_pairs.tex:2563:identically zero; the current algebra is abelian. An abelian
chapters/theory/chiral_koszul_pairs.tex:2564:current algebra at level~$k$ is Heisenberg, which is class~$G$.
chapters/theory/chiral_koszul_pairs.tex:3209:\index{Whitehead's second lemma!application to Poisson rigidity}
chapters/theory/chiral_koszul_pairs.tex:3240:only at the $E_0$ level. Whitehead's second lemma gives
chapters/theory/chiral_koszul_pairs.tex:3283:for such brackets lies outside the scope of Whitehead's lemma:
chapters/examples/kac_moody.tex:259:(i)~the WZW model / affine current algebra (geometric/physical);
chapters/examples/kac_moody.tex:1230:\textup{(}the external tensor power of the current algebra sheaf
chapters/examples/kac_moody.tex:4313:Whitehead lemma gives $H^0 = S^\bullet(\fg[t^{-1}])^\fg$.
chapters/examples/kac_moody.tex:4399:(Chapter~\ref{ch:derived-langlands}); the Whitehead spectral
chapters/examples/kac_moody.tex:4804:The affine current algebra $\widehat{\mathfrak{g}}_k$ has OPE
chapters/theory/higher_genus_modular_koszul.tex:896:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
chapters/theory/higher_genus_modular_koszul.tex:920:by Whitehead; the Killing-form invariant
chapters/theory/higher_genus_modular_koszul.tex:931:enrichment factorization, Whitehead acyclicity, and the
chapters/theory/higher_genus_modular_koszul.tex:1011:Lie bracket of the truncated loop algebra
chapters/theory/higher_genus_modular_koszul.tex:1027:semisimple, the Whitehead--Chevalley--Eilenberg theorem
chapters/theory/higher_genus_modular_koszul.tex:1076:We exhibit the interplay of Whitehead vanishing and
chapters/theory/higher_genus_modular_koszul.tex:1110: Whitehead's theorem gives
chapters/theory/higher_genus_modular_koszul.tex:1127:three by the bracket isomorphism, five by Whitehead, one by the
codex
I’m testing the two main attack surfaces now: whether the “enrichment” really splits the way the proof says, and whether Whitehead is being applied to the right Lie algebra. Those are the places most likely to hide a false reduction.
exec
/bin/zsh -lc "rg -n -F 'antiholomorphic' chapters/theory/higher_genus_modular_koszul.tex && rg -n -F 'H"'^{0,1}'"' chapters/theory/higher_genus_modular_koszul.tex && rg -n -F 'Omega"'^{n-1}_{'"\\log}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'k \\notin \\Sigma(\\fg)' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/kac_moody.tex && rg -n -F '\\Sigma(\\fg)' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'C"'^*('"\\fg, M_h)' chapters/theory/higher_genus_modular_koszul.tex && rg -n -F 'truncated loop algebra' chapters/theory/higher_genus_modular_koszul.tex && rg -n -F 'Whitehead--Chevalley--Eilenberg theorem' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
882:The same argument applies to the antiholomorphic factor
1380:\emph{Note on antiholomorphic forms.}
1382:(antiholomorphic $1$-forms) contributes additional
1525:The same argument applies to the antiholomorphic factor
1686:and similarly on the antiholomorphic factor. Consequently the entire
1750:The antiholomorphic factor $H^{0,1}(\Sigma_g)$ is handled
1811:The antiholomorphic factor is handled identically.
29175:antiholomorphic modes), this is a Fredholm determinant.
883:$H^{0,1}(\Sigma_g)$, since $L_0$ acts only on the vertex-algebra
1381:The enrichment from $H^{0,1}(\Sigma_g) \cong \bC^g$
1526:$H^{0,1}(\Sigma_g)$, since $L_0$ acts only on the vertex-algebra
1750:The antiholomorphic factor $H^{0,1}(\Sigma_g)$ is handled
956:\cA^{\boxtimes n} \otimes \Omega^{n-1}_{\log}\bigr).
 succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:781:$k \notin \Sigma(\fg)$ (the finite exceptional set of
chapters/theory/higher_genus_modular_koszul.tex:914:$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
chapters/theory/higher_genus_modular_koszul.tex:1210:generic level $k \notin \Sigma(\fg)$, the PBW spectral sequence
chapters/theory/chiral_koszul_pairs.tex:781:$k \notin \Sigma(\fg)$ (the finite exceptional set of
chapters/theory/chiral_koszul_pairs.tex:1296:$H^0(X, \omega_X)$ produce the exceptional set $\Sigma(\fg)$ of
chapters/theory/higher_genus_modular_koszul.tex:914:$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
chapters/theory/higher_genus_modular_koszul.tex:1210:generic level $k \notin \Sigma(\fg)$, the PBW spectral sequence
 succeeded in 51ms:
1298:where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
1011:Lie bracket of the truncated loop algebra
1027:semisimple, the Whitehead--Chevalley--Eilenberg theorem
1302:Whitehead--Chevalley--Eilenberg theorem gives

thinking
**Inspecting chiral pairs**

I need to dive deeper into the chiral Koszul pairs related to the exceptional set Sigma(g). I wonder what specific aspects I should focus on to understand their properties better. There’s definitely a lot of detail here, and I’m curious about how they interact with one another and any unique characteristics that might arise from the exceptional set. This could be an intriguing area to explore, so I’ll make sure to gather sufficient information.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1288,1306p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '510,535p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '522,565p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1288	
  1289	\smallskip\noindent\textbf{Classical precedent.}
  1290	On the formal disk $\hat{D}$, this reduces to the
  1291	Beilinson--Ginzburg--Soergel criterion for $\operatorname{Zhu}(\cA)$
  1292	\cite{BGS96}.
  1293	On $\bP^1$, diagonal vanishing follows from PBW since
  1294	$H^1(\bP^1, \cO) = 0$.
  1295	At genus $g \geq 1$, the Hodge-theoretic contributions from
  1296	$H^0(X, \omega_X)$ produce the exceptional set $\Sigma(\fg)$ of
  1297	Theorem~\ref{thm:bar-cohomology-level-independence} where diagonal
  1298	vanishing may fail.
  1299	
  1300	\end{theorem}
  1301	
  1302	\begin{proof}
  1303	Forward: $E_2$-collapse concentrates $H^*(\barBgeom(\cA))$ on
  1304	the diagonal $p = q$; since the bar resolution computes Ext,
  1305	$\operatorname{Ext}^{p,q}(\omega_X, \omega_X) = 0$ for
  1306	$p \neq q$.
 succeeded in 52ms:
   510	$\chi \colon \mathfrak{m}^+ \to \bC$ determined by $e$:
   511	\begin{equation}\label{eq:general-ds}
   512	\mathcal{W}^k(\fg, e) = H^0\!\bigl(
   513	\widehat{\fg}_k \otimes \mathcal{F}_{\mathrm{gh}}(\mathfrak{m}^+),\;
   514	Q_{\mathrm{DS}}^{(\chi)}\bigr).
   515	\end{equation}
   516	The generators of $\mathcal{W}^k(\fg, e)$ have conformal weights
   517	determined by the eigenvalues of $\operatorname{ad}(h)/2$ on the
   518	centralizer $\fg^e$: each $x \in \fg^e$ of $\operatorname{ad}(h)$-eigenvalue
   519	$2j$ contributes a strong generator of conformal weight $j + 1$.
   520	
   521	\begin{remark}[The DS hierarchy]
   522	\label{rem:ds-hierarchy-summary}
   523	Nilpotent orbits are partially ordered by closure: $e = 0$ gives $\mathcal{W}^k(\fg, 0) = \widehat{\fg}_k$; $e = e_{\mathrm{prin}}$ gives $\mathcal{W}_N$ (generators of spins $d_i + 1$). For $\fg = \mathfrak{sl}_3$: $\widehat{\mathfrak{sl}}_{3,k} \supset \mathcal{W}^k(\mathfrak{sl}_3, f_{\min}) \supset \mathcal{W}_3$ (Computation~\ref{comp:sl3-ds-hierarchy}). The principal row is proved; the minimal/subregular and hook-type rows provide the leading non-principal audit corridor, with explicit local computations and a proved transport mechanism, but their full duality transport remains conditional or conjectural (Theorem~\ref{thm:hook-transport-corridor}, Conjecture~\ref{conj:bp-duality}, Conjecture~\ref{conj:type-a-transport-to-transpose}).
   524	\end{remark}
   525	
   526	\begin{definition}[Barbasch--Vogan dual orbit]
   527	\label{def:bv-dual}
   528	\index{Barbasch--Vogan duality|textbf}
   529	For a nilpotent orbit $\mathbb{O}_e \subset \fg$, the
 succeeded in 52ms:
   522	Theorem~\ref{thm:quantum-complementarity-main}.
   523	\end{definition}
   524	
   525	\begin{remark}[Model independence]\label{rem:model-independence}
   526	Any two admissible dg presentations of the same factorization
   527	object are connected by a contractible space of quasi-isomorphisms,
   528	so the homotopy axioms \ref{MK:koszul-htpy}--\ref{MK:modular-htpy}
   529	are invariants of the factorization algebra, not of a
   530	chosen model. Definition~\ref{def:modular-koszul-chiral} provides
   531	the dg model used throughout.
   532	\end{remark}
   533	
   534	\begin{definition}[Modular pre-Koszul chiral algebra: dg model of
   535	 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
   536	Let $X$ be a smooth projective curve over $\mathbb{C}$.
   537	A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
   538	algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
   539	the following data and satisfying the following axioms.
   540	
   541	\smallskip\noindent\textbf{Data.}

thinking
**Searching for mathematical concepts**

I’m looking into the definition of modular Koszul chiral and considering fiberwise differentials, though I’m not sure if that’s relevant. I also need to locate the theorem on bar cohomology level independence to understand if 0 holds in Sigma. It feels a bit tricky, and I’m aware I need to double-check the links between these concepts to provide the best response. Let’s focus on getting all the relevant information!
exec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cohomology-level-independence\\}|bar-cohomology-level-independence|exceptional set \\\\Sigma\\(\\\\fg\\)\" chapters/theory/chiral_koszul_pairs.tex chapters/examples/kac_moody.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:782:Theorem~\textup{\ref{thm:bar-cohomology-level-independence}}),
chapters/theory/chiral_koszul_pairs.tex:1297:Theorem~\ref{thm:bar-cohomology-level-independence} where diagonal
chapters/examples/kac_moody.tex:975:\label{thm:bar-cohomology-level-independence}
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '950,1045p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   950	\item The ``curvature-first'' spectral sequence with
   951	$E_1^{p,q} = H^{p+q}(\bar{B}^\bullet,\, \delta)$,
   952	converging to $H^*(\bar{B}^\bullet, d_k)$, with $d_1$ induced
   953	by $d_{\mathrm{crit}}$.
   954	\end{enumerate}
   955	\end{corollary}
   956	
   957	\begin{proof}
   958	Standard spectral sequence theory for a bicomplex
   959	\cite[Ch.~5]{Weibel94}. The convergence follows from
   960	the finite-dimensionality of $\bar{B}^n$ (Lemma~\ref{lem:bar-dims-level-independent}).
   961	\end{proof}
   962	
   963	\begin{remark}[Interpretation of the bicomplex]
   964	\label{rem:bicomplex-interpretation}
   965	\index{bar complex!bicomplex!interpretation}
   966	The decomposition~\eqref{eq:bar-level-decomp} reflects the level-independence of bar chain groups (Lemma~\ref{lem:bar-dims-level-independent}): $d_{\mathrm{crit}}$ encodes $\mathfrak{g}$-structure constants, $\delta$ encodes the central extension, and $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is the degree-$0$ component of $(k + h^\vee)\delta$.
   967	\begin{enumerate}[label=\textup{(\roman*)}]
   968	\item At $k = -h^\vee$: $\delta$ vanishes and the bar complex is uncurved with differential $d_{\mathrm{crit}}$.
   969	\item For generic $k \neq -h^\vee$: the critical-first spectral sequence relates bar cohomology at generic and critical levels.













thinking
**Clarifying a concept**

I'm noticing that line 1047 mentions "non-degeneracy of the Killing form at generic level." There's a bit of confusion here because it seems to conflate the concept of non-degeneracy of the Killing form with the idea of level. In reality, the Killing form is non-degenerate no matter the level, so I need to clarify that point. It's essential to present this correctly to avoid any misunderstandings.
thinking
**Clarifying weight contributions**

I'm considering if the setup could be established elsewhere, but maybe it's not that necessary. I'm confused about the claims regarding weight generators and their contributions on earlier versus later pages related to conformal weight. I need to look into the PBW degree and how it influences page indexing. In the theorem about pbw-universal-semisimple proof, it mentions unique generators with specific conformal weight, which seems to tie into the shifting and contributions. It feels a bit tangled right now!
thinking
**Evaluating cohomology concepts**

I'm considering the relationship between d1 from genus0 part and enrichment when it comes to creating different cohomology. I notice that there's a lack of clarity about whether they established a block upper-triangular differential with a zero map between genus0 and enrichment. There's also something about the quotient spectral sequence linked to genus0 being preserved, which raises questions about the stability of these components. Understanding this relationship could be crucial for deeper insights.
thinking
**Analyzing proof inconsistencies**

I'm diving into the proofs and finding that they only analyze the subcomplex formed by enrichment classes, but an earlier Kac-Moody proof states that part of d1 from enrichment lands in the genus0 sector. This might mean eliminating enrichment isn’t enough to show the full spectral sequence equals genus0, which could undermine all the PBW theorems. I need to re-verify. It seems there's a potential internal inconsistency, and I should check for lemmas that could clarify this further.
thinking
**Identifying theorem issues**

I'm looking at the potential issues with the theorem statement about principal finite-type W. The proof uses generator weights from the DS hierarchy and mentions that every other homogeneous state has a conformal weight greater than 2, but I see the augmentation ideal contains descendants like L_{-1}T of weight 3. I wonder about composites of weight 2, like a normal ordered product of a weight 1 generator, which wouldn't fit into principal W. There’s also a dimension mismatch in the Virasoro proof, and I need to confirm details in the summary theorem since there’s no proof body, but inline references could cover that.
thinking
**Checking proof sources**

The user asked for proof, and I realize the actual proof is located elsewhere; the summary theorem doesn’t provide one. This isn’t a core flaw, but I need to look into whether thm: pbw-allgenera-principal-w or its corollary has a “ProvedHere” note. It seems there isn't a separate later-page or extension analysis, even though the preamble hints at one. The proof states, "This theorem uses ... only to eliminate explicit genus-enrichment block,” which is interesting!
thinking
**Considering proof mechanisms**

I’m thinking about computing d2 at k=0 in line 1350, which becomes 0, so the invariant isn't killed. That might demonstrate that the proof mechanism fails at the included boundary. While the theorem may still hold through different means, this shows a significant gap in the proof audit. It’s interesting how nuances in equations can lead to such different implications in mathematical proofs!
thinking
**Analyzing theorem details**

I need to quote specific lines and infer that for n > 2, the regular factor should depend on the bar degree rather than a single genus vector space. This could be a valuable inference. I also want to check if the principal W theorem references the pbw-universal-semisimple theorem. The statement seems to eliminate explicit genus-enrichment, but the proof doesn’t cite it directly. I should examine the complete proof of the pbw-universal-semisimple theorem for any contradictions while keeping an eye on mixed differential issues.
thinking
**Verifying compute module**

I should verify if the compute module exists within lines 1534-1542. It seems like a good idea to search through the file for this information. However, since the user asked for reading and reporting, I want to make sure I'm focusing on providing a clear summary or report instead of getting too caught up in checking each line. I’ll balance the need for verification with the task of reporting back comprehensively.
thinking
**Evaluating generator findings**

I see that the uniqueness of the weight2 generator and d1 identification is crucial. Whitehead seems to have misapplied certain maps, leading to some overclaims in part (c). My critical findings address that and I think I need to re-verify actual lines for the principal W proof, which seems to be lacking deeper analysis on later pages. It mentions at pages 777-779 that the absence of differentials/extensions is supplied by a family-specific argument.
thinking
**Considering propagation concepts**

I’m thinking about how to respond to the user's question about downstream propagation. Perhaps instead of referencing it as a separate finding, I could approach it more as part of the propagation surface. It’s an interesting angle to explore, and I wonder how best to convey that idea concisely. Let’s see how I can present this in a way that’s clear and helpful for the user!
thinking
**Clarifying class targeting**

Okay, to effectively target a class in E2, it seems like I need d2 from a certain cycle to successfully hit it. I need to keep this in mind as I consider how to approach this task. It's interesting how the mechanics of targeting can vary based on cycles, and I want to ensure I fully understand this concept before proceeding. Let’s explore this aspect further to ensure accuracy!
thinking
**Evaluating theorem status**

I’m thinking about adding a significant finding regarding status propagation. For example, in [editorial_constitution.tex:193], the `thm:master-pbw` is tagged as `ClaimStatusProvedHere` even though it lacks a proof block. It only aggregates the three family theorems. Since the PBW proofs are incomplete, the summary theorem and concordance claims in [concordance.tex:1842] and [concordance.tex:1924] appear to be status-inflated. I might need to search line numbers using `nl` next. Let's check those areas.
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '193,216p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1918,1928p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1836,1848p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1918	 positive RTT towers, coefficient stabilization
  1919	 (Theorem~\ref{thm:coefficient-stability-criterion}) reduces
  1920	 completion to finite truncations. MC4$^0$ concerns algebras with
  1921	 finite resonance rank (Virasoro, non-quadratic
  1922	 $\mathcal{W}_N$) and is reduced to a finite-dimensional problem
  1923	 by Theorem~\ref{thm:resonance-filtered-bar-cobar}. The uniform
  1924	 PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1
  1925	 to MC4: uniform PBW degeneration plus quotient stabilization
  1926	 implies completed bar-cobar duality.
  1927	 The \emph{general theorem} (strong completion-tower
  1928	 theorem) is proved unconditionally. What remains is
 succeeded in 51ms:
   193	\begin{theorem}[Higher-genus PBW concentration for the standard
   194	 finite-type interacting families]\label{thm:master-pbw}
   195	\ClaimStatusProvedHere{}
   196	The genus-$g$ PBW spectral sequence concentrates at all genera for the
   197	three standard finite-type interacting families treated in the proved
   198	core: affine Kac--Moody
   199	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
   200	Virasoro
   201	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}}\textup{)},
   202	and principal finite-type $\mathcal{W}$-algebras, including higher
   203	$\mathcal{W}_N$
   204	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}\textup{)}.
   205	
   206	\emph{This resolves MC1 for the standard finite-type interacting
   207	families. Theorem~\textup{\ref{thm:pbw-universal-semisimple}}
   208	isolates the common unique-weight-$2$ $d_2$ mechanism behind the
   209	Virasoro and principal finite-type $\mathcal{W}$ arguments; for chiral
   210	algebras with semisimple Lie symmetry satisfying
   211	hypotheses~\textup{(a)--(c)}, the enrichment-killing is unconditional
   212	via Whitehead vanishing plus $L_0$ invertibility. The resolved status
 succeeded in 51ms:
  1836	The three-pillar architecture determines the MC resolution strategy:
  1837	\begin{itemize}
  1838	\item \emph{MC1 and MC2}: Pillar~B realizes every algebra as an MC
  1839	 element in the modular convolution $sL_\infty$-algebra; the
  1840	 finite-order projections $\Theta_\cA^{\leq r}$ (the proved shadow
  1841	 obstruction tower) are the constructive content.
  1842	 MC1 (PBW concentration) holds unconditionally for universal
  1843	 algebras $V_k(\fg)$, $\mathrm{Vir}_c$, $\mathcal{W}^k(\fg)$
  1844	 (Proposition~\ref{prop:pbw-universality}). For simple quotients
  1845	 $L_k(\fg)$ at admissible levels, PBW concentration fails at
  1846	 $\mathrm{rk}(\fg) \geq 2$ with denominator $q \geq 3$: the
  1847	 abelian Cartan subalgebra contributes $\mathrm{rk}(\fg)$ classes
  1848	 to $H^2(\barB)$

thinking
**Inspecting proof requirements**

I’m wondering if this could be an issue of misstatement on my part. The user is asking for MC1 proof, but I'm not sure it’s necessary unless there's a direct propagation issue to address. I think I should take some time to inspect the propagation details to confirm whether the proof is actually needed here. It’s all a bit confusing, but it's essential to clarify this first!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1314,1350p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1314	\begin{proposition}[PBW universality; \ClaimStatusProvedHere]
  1315	\label{prop:pbw-universality}
  1316	\index{Koszul property!PBW universality}
  1317	\index{vertex algebra!freely strongly generated}
  1318	
  1319	A vertex algebra~$\cA$ is \emph{freely strongly generated} if it
  1320	admits strong generators $\{a^i\}_{i \in I}$ whose normally ordered
  1321	monomials
  1322	$:\!\partial^{n_1} a^{i_1} \cdots \partial^{n_r} a^{i_r}\!:$
  1323	form a PBW basis; equivalently,
  1324	$\operatorname{gr}_F \cA \cong \operatorname{Sym}^{\mathrm{ch}}(V)$
  1325	where $V$ is the $\cD_X$-module spanned by the generators.
  1326	
  1327	Every freely strongly generated vertex algebra is chirally Koszul.
  1328	\end{proposition}
  1329	
  1330	\begin{proof}
  1331	The three hypotheses of Theorem~\ref{thm:pbw-koszulness-criterion}
  1332	hold: (1)~flatness of $F_p/F_{p-1} \cong S^p(V)$ by the PBW basis;
  1333	(2)~classical Koszulness of $\operatorname{gr}_F \cA \cong

thinking
**Checking concordance definitions**

I’m considering whether finding five concordances using prop:pbw-universality might imply that MC1 is defined within genus0. It’s important to check the context around line 1842 because this could clarify if concordance has a different meaning related to MC1 and MC2 pillar. I’ll dive into that context to understand it better and see if my assumptions hold true. Let’s see what I uncover!
codex
- [CRITICAL] [higher_genus_modular_koszul.tex:994](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:994) — The genus-1 Kac--Moody proof explicitly allows `d_1^{PBW}` of enrichment classes to land in the concentrated genus-0 sector (`E_1(g=0) \oplus \mathcal E_1`). The later proofs at [1292](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1292), [1472](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1472), [801](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:801), and [1709](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1709) then kill the enrichment and conclude `E_\infty(g)=E_\infty(0)` without controlling those mixed maps. That comparison is not proved.

- [CRITICAL] [higher_genus_modular_koszul.tex:1011](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1011) — The proof says `d_1^{PBW}` is built from the bracket of the truncated loop algebra, then immediately reidentifies the enrichment as `C^*(\fg,M_h)` and invokes Whitehead for semisimple `\fg` at [1027](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1027). That reduction is not justified by the text. The same unsupported move reappears at [1294](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1294) and [1776](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1776). Whitehead applies to `\fg`, not automatically to the truncated current algebra that the proof itself names.

- [HIGH] [higher_genus_modular_koszul.tex:1050](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1050) — The displayed `d_2` computation does not hit the invariant class it claims to kill. The surviving class is `\kappa^{ab}(J^a_{-1}\otimes J^b_{-1})\otimes\alpha`, but the computed image is `k\dim(\fg)\,J^c_{-1}\otimes\alpha`, a different target. The all-genera repetition at [1346](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1346) has the same defect. This step also requires `k\neq0`, while the theorem statement [1210](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1210) includes generic `k\notin\Sigma(\fg)`, and the cited genericity theorem [kac_moody.tex:983](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:983) excludes special values via `\lambda=k+h^\vee`, not by removing `k=0`.

- [HIGH] [higher_genus_modular_koszul.tex:1264](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1264) — Inference: the factorization `\mathcal E_g^{*,h}\cong M_h\otimes H^{1,0}(\Sigma_g)` is asserted but not proved, and it is hard to reconcile with the chain groups written at [955](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:955), which use `\Omega^{n-1}_{\log}` in bar degree `n`. For `n>2`, the regular contribution should depend on bar degree and allow multiple global 1-forms, not a single `H^{1,0}` factor. This unsupported factorization is then reused in the Virasoro, principal-`\mathcal W`, and universal proofs.

- [HIGH] [concordance.tex:1842](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1842) — Downstream propagation is overstated. Concordance packages `prop:pbw-universality` as an MC1 citation for universal `V_k(\fg)`, `\mathrm{Vir}_c`, and `\mathcal W^k(\fg)`, but [chiral_koszul_pairs.tex:1314](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1314) only proves genus-0 chiral Koszulness of freely strongly generated vertex algebras. It does not prove the all-genera PBW concentration used elsewhere for MC1, including [editorial_constitution.tex:193](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:193).

- [MEDIUM] [higher_genus_modular_koszul.tex:1486](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1486) — The Virasoro proof misquotes its own cited input. It says `\dim M_h=p(h-2)` by `comp:virasoro-vacuum`, but [bar_complex_tables.tex:278](/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:278) gives `\dim \bar V_h=p_{\ge2}(h)=p(h)-p(h-1)`; at `h=5` the table gives `2`, while `p(3)=3`. This is not fatal by itself, but the cited step is false as written.

- [LOW] [higher_genus_modular_koszul.tex:1380](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1380) — The repeated appeal to `H^{0,1}(\Sigma_g)` “antiholomorphic forms” sits outside the algebraic bar-complex surface actually written, which uses logarithmic forms [higher_genus_modular_koszul.tex:955](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:955) on a smooth projective curve [higher_genus_modular_koszul.tex:534](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:534). This is a scope/convention leak even if the core theorem were repairable.

## Summary
Instances checked: 15 | Violations found: 7 | Verdict: FAIL
tokens used
127,587
