# F03_definitions_shadow (555s)

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:12248` — PROBLEM: `def:shadow-postnikov-tower` is not a valid formal definition when introduced. It defines `\Theta_\cA^{\le r}` inside `\mathfrak g^{\mathrm{amb}}_\cA/F^{r+1}`, but `\mathfrak g^{\mathrm{amb}}_\cA` is not defined until `31197`, and the same tower is later captioned in `\gAmod/F^{r+1}` at `12459-12462`. The carrier is undefined at the moment of definition and inconsistent inside the same local block. FIX: move Definition `def:ambient-modular-complementarity-algebra` (`31197-31217`) to immediately before `12195`, then choose one carrier and use it everywhere. If the tower is ambient, change `12459-12462` and `12478-12480` from `\gAmod` to `\mathfrak g^{\mathrm{amb}}_\cA`; if it is coinvariant, replace `12212-12301` by `\gAmod` and delete `\mathfrak g^{\mathrm{amb}}_\cA` from the tower definition.

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:16616` — PROBLEM: the formal classification says finite shadow depths `5,6,7,\dots` occur and “every finite value is realized,” but Proposition `prop:depth-gap-trichotomy` later proves `d_{\mathrm{alg}}\in\{0,1,2,\infty\}` and “no finite `d_{\mathrm{alg}}\ge 3` is realized” at `17621-17645`. This is an internal contradiction on the same theorem surface. FIX: delete `16616-16630` and replace them with: “These four classes are exhaustive and mutually exclusive. By Proposition~\ref{prop:depth-gap-trichotomy}, the only algebraic depths are `0,1,2,\infty`, corresponding to `\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}`.” If a different notion of depth is intended, introduce it under a new symbol and prove the comparison before using it.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:37` — PROBLEM: `\Theta_\cA`, its truncations, and the Maurer--Cartan equation are used as if already formal, but the first bar-intrinsic definition of `\Theta_\cA` is at `3774-3798`, the first formal shadow-tower definition is at `12248-12300`, and the first named master-equation definition is at `31031-31056`. The opening is foundationally backward. FIX: insert immediately after line `36` a local definition block: “Set `\Theta_\cA:=D_\cA-\dzero\in\mathfrak g_\cA^{\mathrm{mod}}`. For `r\ge2`, let `\Theta_\cA^{\le r}:=\pi_{\le r}(\Theta_\cA)\in \MC(\mathfrak g_\cA^{\mathrm{mod}}/F^{r+1})`; the inverse system `(\Theta_\cA^{\le2}\to\Theta_\cA^{\le3}\to\cdots)` is the shadow obstruction tower. The strict MC equation is `[\dzero,\Theta_\cA]+\tfrac12[\Theta_\cA,\Theta_\cA]=0`.” Then keep the later theorem as the proof, not the first definition.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:59` — PROBLEM: `\gAmod` and `\Definfmod(\cA)` are invoked before they are defined. The strict model appears only at `10179-10224` and the two-level convention only at `10831-10908`, so the opening asks the reader to accept undefined carrier algebras on trust. FIX: add a notation import before line `59`: “`\mathfrak g_\cA^{\mathrm{mod}}:=\prod_{2g-2+n>0}\Hom_{\Sigma_n}(C_*(\overline{\mathcal M}_{g,n}),\End_\cA(n))` is the strict modular convolution dg Lie algebra; `\Definfmod(\cA)` is the homotopy-invariant modular deformation `L_\infty`-algebra, with `\mathfrak g_\cA^{\mathrm{mod}}` as strict model.” Cite Definition~\ref{def:modular-convolution-dg-lie} and Remark~\ref{rem:two-level-convention} there.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:52` — PROBLEM: the obstruction class is placed in `H^2(\cA^{\mathrm{sh}}_{r+1,0})` before the shadow algebra `\cA^{\mathrm{sh}}` is defined at `12501-12549`. The target of the obstruction map is undefined at first use. FIX: either move Definition~\ref{def:shadow-algebra} before line `52`, or rewrite `52-55` as “the obstruction classes land in the degree-`r+1`, genus-`0` piece of the shadow algebra to be defined in Definition~\ref{def:shadow-algebra}” and postpone the displayed cohomology target until after `12501`.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:136` — PROBLEM: the four classes `\mathsf{G},\mathsf{L},\mathsf{C},\mathsf{M}` are used 16k lines before their formal definition at `16562-16637`, and the notation changes from `\mathsf{}` here to `\mathbf{}` in the definition at `16586-16610`. This is both a forward-definition failure and a notation drift on a load-bearing classification. FIX: insert a local definition immediately before line `121` with the four classes and their depth criteria, and standardize to one macro everywhere, e.g. replace the opening `\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}` by the same `\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}` used at `16586-16610`.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:180` — PROBLEM: `\Theta_\cA^{E_1}` is used as a known object, but the ordered carrier `{\gAmod}^{E_1}` and the averaging map `\operatorname{av}\colon{\gAmod}^{E_1}\twoheadrightarrow\gAmod` are not introduced here; they are defined only in `chapters/theory/e1_modular_koszul.tex:233-288`, and the opening does not cite that definition. FIX: after line `179` add: “Here `{\gAmod}^{E_1}` is the ordered modular convolution dg Lie algebra of Definition~\ref{def:e1-modular-convolution}, `\Theta_\cA^{E_1}\in\MC({\gAmod}^{E_1})` is Theorem~\ref{thm:e1-mc-element}, and `\operatorname{av}(\Theta_\cA^{E_1})=\Theta_\cA` by \eqref{eq:e1-to-einfty-projection}.”

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:450` — PROBLEM: this file references `thm:universal-MC`, but the local theorem is `thm:universal-theta` at `3575-3604`. The label `thm:universal-MC` lives outside the theory chapter in `chapters/connections/concordance.tex:5344-5360` and is also duplicated as a phantom label in `main.tex:1746`. The reference is therefore an unstable external alias, not a local theorem anchor. FIX: replace every in-file `\ref{thm:universal-MC}` with `\ref{thm:universal-theta}`; then delete the duplicate phantom label `\label{thm:universal-MC}` from `main.tex:1746` so the theorem label exists exactly once on an actual theorem surface.

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:12284` — PROBLEM: the shadow-tower definition identifies the truncation with a scalar, `\Theta_\cA^{\le2}=\kappa(\cA)`, even though the same file later gives the actual degree-2 truncation as `\Theta_\cA^{\le2}=\kappa\cdot\eta\otimes\Lambda` at `29803-29805`. A Maurer--Cartan truncation is not literally a scalar. FIX: replace `12284-12285` with “`\pi_2(\Theta_\cA^{\le2})=\kappa(\cA)`; more explicitly, on the scalar lane `\Theta_\cA^{\le2}=\kappa(\cA)\,\eta\otimes\Lambda`.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:449` — PROBLEM: Definition~\ref{def:modular-koszul-homotopy} makes the Maurer--Cartan datum optional by writing “and (when constructed) a genus-completed Maurer--Cartan datum `\Theta_\cA`.” A foundational definition cannot hide a core datum behind an optional parenthesis and then rely on it later as if it were part of the structure. FIX: remove the optional clause from Data item D3 and move the MC datum to the consequence list, e.g. add after MK5: “When Theorem~\ref{thm:universal-theta} applies, the object carries a canonical genus-completed Maurer--Cartan class `\Theta_\cA`.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:2648` — PROBLEM: the full modular package says Theorem~\ref{thm:mc2-bar-intrinsic} gives the universal MC class “in particular, for every such `\cA` with simple Lie symmetry,” but Theorem~\ref{thm:mc2-bar-intrinsic} as stated at `3779-3780` assumes only a modular Koszul chiral algebra with non-degenerate invariant form. The prose falsely narrows the theorem’s scope. FIX: delete “with simple Lie symmetry” from `2650-2651`; if a narrower corollary is intended, cite that corollary instead of the full theorem.

## Summary
Checked: 11 | Findings: 10 | Verdict: FAIL


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
session id: 019d87f4-65e3-7811-9947-945ac88c837b
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


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_modular_koszul.tex

Check: is the shadow tower Theta_A formally defined? Are G/L/C/M classes defined before use? Is the MC equation stated as a definition before being invoked in proofs? Is the convolution algebra g^{E1} and g^{mod} defined?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers


thinking
**Planning code exploration**

I’m considering how to approach exploring the codebase. The developer recommends using explorers for codebase questions, but I might still need to read file contents myself. I’ll use the explorer to locate definitions and dependencies, focusing on the target files and imports. I probably need to run line-numbered reads and utilize tools like rg and sed. I’ll make sure to provide commentary updates before proceeding and acknowledge the request in my first step. Let’s plan this out!
thinking
**Deciding on reference checks**

I'm considering using unresolved reference checks through LaTeX compilation. If building is necessary, I might use build-surface, but I'll decide after reading through. I wonder if I need to cross-volume since the audit focuses on one file, yet hidden imports could come from elsewhere. I’ll prioritize definitions and use deep-beilinson-audit, possibly skipping claim-surface-sync. I'll read constitutional files and leverage parallel execution with tools like `rg --files` or `sed -n` for efficiency. Let's figure this out!
codex
Using `deep-beilinson-audit` for a hostile theorem-surface review. I’m starting by reading the constitutional files and the target chapter with line numbers, then I’ll trace each requested object/claim back to its first actual definition before I allow it in the audit.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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

 succeeded in 53ms:
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
 succeeded in 53ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 52ms:
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

 succeeded in 50ms:
     1	\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
     2	
     3	%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
     4	
     5	Bar-cobar inversion (Theorem~B) proves that
     6	$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
     7	rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
     8	The proof uses one fact: the bar differential squares to zero.
     9	At genus~$g \geq 1$, this fact fails fiberwise.
    10	The bar complex $\barB^{(g)}(\cA)$ acquires curvature
    11	\[
    12	 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
    13	\]
    14	%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
    15	where $\omega_g = c_1(\lambda)$ is the Hodge class on
    16	$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
    17	characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
    18	The fiberwise differential no longer squares to zero; cobar inversion,
    19	as stated, does not extend.
    20	


thinking
**Evaluating audit requirements**

The user is asking for specific contents, potentially using `texfot`, but checking for unresolved references with `rg -n` could be easier to find labels across the repo. It seems I need to produce findings about order and hidden imports without checking every line of the file, especially since there might be thousands of lines and numerous claims. It’s crucial to search for all mentions like Theta, g^mod, and others, ensuring all references and definitions are formally defined.
thinking
**Planning exact fixes**

Okay, the user wants an exact fix, not just a diagnosis, so I need to propose a precise sentence or structure to insert. It seems I should provide line-specific fix directions, but I don’t necessarily need to apply them. Since "exact fix" implies I might need specific wording, I could offer a concise solution. I also think it’s important to use an update plan after I get sufficient context. Let’s proceed with a progress update and a clear plan!
codex
I’ve got the target opening and the governing repo conventions. Next I’m tracing every first use of `\Theta_\cA`, the shadow tower, the G/L/C/M classes, the Maurer–Cartan equation, and the `E_1`/modular convolution algebras to determine whether this chapter defines them, imports them cleanly, or simply assumes them.
Plan update
Foundation audit of higher_genus_modular_koszul.tex focused on definition order, hidden imports, and theorem-surface grounding.
  → Map first-use sites in the target file for Theta_A, shadow tower, G/L/C/M, Maurer-Cartan equation, g^{E1}, and g^{mod}
  • Read the target file at each first-use site and inspect the cited labels that are supposed to supply the missing foundations
  • Check for unresolved or weakly imported references and second-order dependency gaps around the foundational claims
  • Assemble only re-verified findings with exact fixes and final verdict


thinking
**Considering file searches**

I need to run an rg command across the file and repository for labels, using parallel commands. The developer suggests using the explorer for codebase questions, although we’ve already started manually. The user emphasizes grounding claims in the actual file contents, but I wonder if we can still utilize explorer results. It might be efficient to locate relevant labels quickly with explorer, then read through manually. It's a bit tricky with the directives on when to use subagents too.
thinking
**Deciding on tool usage**

I need to stick to the guideline that says I should only use subagents if the user specifically requests parallel or delegated tasks. So, I won't use subagents. Instead, I’ll carry on with executing the tool and search within the target file for relevant patterns using rg. It's straightforward, and I think this approach aligns well with the user’s needs while also following the directives I have. Let's get searching!
exec
/bin/zsh -lc "rg -n \"Theta_|shadow tower|\\\\mathsf\\{|Maurer--Cartan|MC element|g\\\\"'^'"\\{E_1\\}|g\\\\"'^'"\\{mod\\}|gAmod|Definfmod|two-level-convention|def:shadow-algebra|def:modular-bar-hamiltonian|def:shadow-postnikov-tower|thm:mc2-bar-intrinsic|thm:e1-mc-element|def:modular-convolution-dg-lie|def:modular-characteristic-package\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(def:shadow-algebra|def:modular-bar-hamiltonian|def:shadow-postnikov-tower|thm:mc2-bar-intrinsic|thm:e1-mc-element|def:modular-convolution-dg-lie|def:modular-characteristic-package|subsec:two-level-convention|thm:single-line-dichotomy|prop:depth-gap-trichotomy)\\}\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '260,620p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Theta_|shadow tower|\mathsf\{|Maurer--Cartan|MC element|g\^\{E_1\}|g\^\{mod\}|gAmod|Definfmod|two-level-convention|def:shadow-algebra|def:modular-bar-hamiltonian|def:shadow-postnikov-tower|thm:mc2-bar-intrinsic|thm:e1-mc-element|def:modular-convolution-dg-lie|def:modular-characteristic-package)
                           ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/theory/e1_modular_koszul.tex:291:\label{thm:e1-mc-element}
chapters/theory/higher_genus_modular_koszul.tex:2613:\label{def:modular-characteristic-package}
chapters/theory/higher_genus_modular_koszul.tex:3775:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:10180:\label{def:modular-convolution-dg-lie}
chapters/theory/higher_genus_modular_koszul.tex:10829:\label{subsec:two-level-convention}
chapters/theory/higher_genus_modular_koszul.tex:12249:\label{def:shadow-postnikov-tower}
chapters/theory/higher_genus_modular_koszul.tex:12502:\label{def:shadow-algebra}
chapters/theory/higher_genus_modular_koszul.tex:17615:\label{prop:depth-gap-trichotomy}
chapters/theory/higher_genus_modular_koszul.tex:18496:\label{thm:single-line-dichotomy}
chapters/theory/higher_genus_modular_koszul.tex:30995:\label{def:modular-bar-hamiltonian}
 succeeded in 51ms:
   260	
   261	\begin{proof}
   262	The argument has three steps.
   263	
   264	\emph{Step~1: MCG acts on the bar differential.}
   265	The genus-completed bar differential
   266	$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
   267	is built from the modular operad structure on
   268	$\{\overline{\mathcal{M}}_{g,n}\}$
   269	(Theorem~\ref{thm:bar-modular-operad}).
   270	At genus~$g$, the component $d_\cA^{(g)}$ is defined by
   271	summing over boundary strata of
   272	$\overline{\mathcal{M}}_{g,n}$, with each stratum
   273	contributing an integral of OPE data against the
   274	logarithmic propagator along the corresponding edge.
   275	The mapping class group
   276	$\mathrm{MCG}(\Sigma_g)$ acts on the Teichm\"uller space
   277	$\mathcal{T}_{g,n}$, and the moduli space
   278	$\overline{\mathcal{M}}_{g,n} = \overline{\mathcal{T}}_{g,n}
   279	/ \mathrm{MCG}$ is the orbifold quotient.

thinking
**Searching for definitions**

I need to gather more details about definitions around line 2613. I should focus on searching specific line numbers, especially if kappa is defined much later. It might be helpful to look closer to line 620 where the definition seems to continue. I plan to search for specific terms like "convolution," "two-level-convention," and "mathsf." My approach will be to use rg with fixed strings or separate queries to pinpoint line numbers of the first uses.
codex
The opening already shows a structural risk: this chapter invokes `\Theta_\cA`, the Maurer–Cartan equation, the four shadow classes, and `\gAmod` before any local definition appears. I’m now checking whether those imports are at least explicit and whether the cited labels actually define the objects they are being asked to carry.
exec
/bin/zsh -lc "rg -n -e 'Theta_\\\\cA' -e 'shadow tower' -e 'Maurer--Cartan' -e 'MC element' -e '\\\\mathsf\\{G\\}' -e '\\\\mathsf\\{L\\}' -e '\\\\mathsf\\{C\\}' -e '\\\\mathsf\\{M\\}' -e 'gAmod' -e 'Definfmod' -e 'two-level-convention' -e 'g\\"'^'"\\{E_1\\}' -e 'g\\"'^'"\\{mod\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2580,2665p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10140,10250p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3740,3815p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 949

34:%% FORCED CONSEQUENCE: the MC element and its degree projections.
37:Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
41: d_0 \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0
44:Existence of the MC element is not a theorem to be proved; it is a
46:$\Theta_\cA$ carries.
54:do not obstruct existence of~$\Theta_\cA$; they obstruct its
60:dg~Lie algebra~$\gAmod$, a strict model of the homotopy-invariant
61:$L_\infty$-algebra $\Definfmod(\cA)$
62:(\S\ref{subsec:two-level-convention}). The weight filtration on
63:$\gAmod$ controls the extension tower: each finite truncation
64:$\Theta_\cA^{\leq r}$ is a graph sum through degree~$r$, with vertex
70:Five constructions govern $\Theta_\cA$.
75: The MC element $\Theta_\cA$ lives in an infinite-dimensional
82: degree-$r$, genus-$g$ projections of~$\Theta_\cA$.
88: computes \emph{how}: $\Theta_\cA^{\leq r}$ is a sum over
94: The graph-sum formula produces $\Theta_\cA^{\leq r}$ but gives
98: (D_\cA\Theta_\cA^{\leq r}
 succeeded in 51ms:
  2580	forgets the algebraic presentation; the Hilbert
  2581	factorization forgets the locally convex topology; the
  2582	coderived shadow retains only cohomological invariants.
  2583	The chain~\eqref{eq:platonic-chain-theory} is the
  2584	\emph{modular form datum} of~$\cA$.
  2585	\end{remark}
  2586	
  2587	\begin{lemma}[$E_2$ collapse at higher genus]\label{lem:e2-higher-genus}
  2588	\ClaimStatusProvedHere
  2589	For a Koszul chiral algebra $\cA$ on a genus-$g$ curve, the PBW
  2590	spectral sequence
  2591	$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g \barB_g(\cA))$
  2592	degenerates at~$E_2$.
  2593	\end{lemma}
  2594	
  2595	\begin{proof}
  2596	The PBW filtration is a filtration by chiral algebras, and the
  2597	Koszulness hypothesis ensures that the associated graded is a
  2598	Koszul complex in the classical sense. The $d_r$ differential
  2599	for $r \geq 2$ maps between PBW-graded components separated
 succeeded in 50ms:
  3740	$\mathrm{obs}_g
  3741	= \sum_{\substack{g_1+g_2=g \\ g_1,g_2 \geq 1}} d_{g_1} \circ d_{g_2}$
  3742	commutes with all chiral products, hence
  3743	$\mu_0^{(g)} \in Z(\cA)$.
  3744	\textup{(}This argument also appears in the proof of
  3745	Theorem~\textup{\ref{thm:genus-graded-koszul}}, Step~4.\textup{)}
  3746	\end{proof}
  3747	
  3748	\subsubsection*{The bar-intrinsic construction: resolution of MC2}
  3749	
  3750	The genus-$0$ bar differential $\dzero$ sees only tree-level
  3751	data: the $A_\infty$ operations, the collision locus, the
  3752	factorization on $\mathbb{P}^1$. Everything the chiral algebra
  3753	knows beyond genus~$0$ is encoded in one object.
  3754	The element $\Theta_\cA := D_\cA - \dzero$ is the positive-genus
  3755	part of the genus-completed bar differential $D_\cA$
  3756	(Theorem~\ref{thm:bar-modular-operad}); it is the unique
  3757	correction that restores $D_\cA^2 = 0$ over all genera
  3758	simultaneously. The Maurer--Cartan equation
  3759	$\dzero\Theta_\cA + \Theta_\cA\,\dzero + \Theta_\cA^2 = 0$
 succeeded in 51ms:
 10140	bar-intrinsic construction
 10141	(Theorem~\ref{thm:mc2-bar-intrinsic};
 10142	Theorem~\ref{thm:recursive-existence}).
 10143	
 10144	These five theorems are aspects of a single object: the modular Koszul chiral
 10145	algebra (Definition~\ref{def:modular-koszul-chiral}). Every chiral
 10146	algebra in Part~\ref{part:physics-bridges} is an instance of this structure.
 10147	The computations that follow (bar cohomology, genus expansions,
 10148	discriminants, complementarity sums) are invariants of the modular characteristic
 10149	package $\mathcal{C}_{\cA} = (\Theta_{\cA}, \kappa(\cA),
 10150	\Delta_{\cA}, \Pi_{\cA}, \mathcal{H}_{\cA})$
 10151	(Definition~\ref{def:full-modular-package}).
 10152	What one algebra sees as
 10153	deformation, its dual sees as obstruction: the Lagrangian
 10154	principle at work, algebra by algebra, genus by genus.
 10155	
 10156	
 10157	%================================================================
 10158	% THE MODULAR BAR-HAMILTONIAN AND THE EXTENSION TOWER
 10159	%================================================================
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30970,31070p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12220,12580p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10800,10910p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17580,18560p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30970	Theorem~\ref{thm:rectification-meta} controls the
 30971	homotopy-coherent passage between strict and $\infty$-models.
 30972	Theorem~\ref{thm:platonic-recovery} recovers the
 30973	six-fold package of Lie conformal data.
 30974	The modular factorization adjunction
 30975	$U^{\mathrm{mod}}_X \dashv
 30976	\operatorname{Prim}^{\mathrm{mod}}$
 30977	(Theorem~\ref{thm:platonic-adjunction})
 30978	completes the circle by identifying the universal
 30979	recipient of all MC data.
 30980	\end{remark}
 30981	
 30982	
 30983	\subsection{The graph sum that realizes the tower}
 30984	\label{subsec:modular-bar-hamiltonian}
 30985	
 30986	The shadow obstruction tower
 30987	(Definition~\ref{def:shadow-postnikov-tower}) is defined
 30988	abstractly by the obstruction recursion
 30989	(Construction~\ref{constr:obstruction-recursion}).
 succeeded in 52ms:
 12220	\emph{separated}
 12221	($\bigcap_{N} F^N = 0$),
 12222	\emph{complete} (the completion
 12223	$\widehat{\mathfrak{g}}^{\mathrm{amb}}
 12224	= \varprojlim_N \mathfrak{g}^{\mathrm{amb}}/F^{N+1}$
 12225	equals the product of weight-$w$ components), and
 12226	\emph{pronilpotent}
 12227	($[F^{N_1}, F^{N_2}] \subseteq F^{N_1 + N_2 - 2}$;
 12228	the shift $-2$ is from degree reduction upon gluing two
 12229	external legs).
 12230	\end{definition}
 12231	
 12232	\begin{definition}[Extension tower]
 12233	\label{def:extension-tower}
 12234	The \emph{modular extension tower} of $\cA$ is the inverse system
 12235	\begin{equation}
 12236	\label{eq:extension-tower}
 12237	\mathcal{E}_{\cA}(N)
 12238	:=
 12239	\operatorname{MC}\bigl(
 succeeded in 51ms:
 10800	 The shadow obstruction tower measures the
 10801	 obstruction to formality
 10802	 (Theorem~\ref{thm:shadow-formality-identification}).
 10803	\item \emph{Gauge equivalence.}
 10804	 Two MC elements
 10805	 $\Theta, \Theta' \in \MC(\Definfmod(\cA))$ are gauge
 10806	 equivalent if and only if they lie in the same
 10807	 connected component of the Deligne--Getzler--Hinich
 10808	 $\infty$-groupoid $\MC_\bullet(\Definfmod(\cA))$.
 10809	 The $1$-simplices (gauge transformations) involve all
 10810	 higher brackets $\ell_n$ ($n \geq 3$), not just the
 10811	 strict differential and bracket. In the strict model,
 10812	 gauge equivalence reduces to the classical exponential
 10813	 action of degree-$0$ elements; the $L_\infty$
 10814	 gauge groupoid is the homotopy-invariant enlargement
 10815	 that persists across quasi-isomorphic replacements.
 10816	\end{enumerate}
 10817	The strict form~\eqref{eq:strict-mc} suffices for \emph{existence}
 10818	of MC elements and for the obstruction-recursion tower
 10819	(Construction~\ref{constr:obstruction-recursion}). The $L_\infty$
 succeeded in 51ms:
 17580	The second term $2\Delta\,t^2 = 16\kappa S_4\,t^2$
 17581	is the \emph{interaction correction}.
 17582	
 17583	Shadow depth $r_{\max} = \infty$ does not entail infinite
 17584	algebraic complexity.
 17585	Class~$\mathbf{M}$ has algebraic degree~$2$
 17586	over $k(c)[t]$: one rational parameter $\Delta$ controls
 17587	the entire infinite tower. The spectral curve
 17588	$\Sigma_L := \{H^2 = t^4 Q_L(t)\}$ in the
 17589	$(t,H)$-plane is rational (genus~$0$); the recursion operator
 17590	$S_r \mapsto S_{r+1}$ is the Higgs field whose
 17591	characteristic equation is~$\Sigma_L$.
 17592	\end{corollary}
 17593	
 17594	\begin{proof}
 17595	$(2\kappa + 3\alpha t)^2 = 4\kappa^2 + 12\kappa\alpha\,t
 17596	+ 9\alpha^2 t^2$. Adding $2\Delta\,t^2 = 16\kappa S_4\,t^2$
 17597	gives $Q_L(t)$.
 17598	\end{proof}
 17599	

thinking
**Looking into shadow depth classification**

I need to keep inspecting the definition of shadow depth classification. I want to see if the terms G/L/C/M are actually defined before I use them or if they come up later. It's important to clarify these labels so I can use them correctly. I wonder what the proper definitions are and if they’re easily accessible. Let's keep exploring this!
exec
/bin/zsh -lc "rg -n 'def:shadow-depth-classification|shadow depth classification|class~\\\\mathbf\\{G\\}|class~\\\\mathsf\\{G\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '250,340p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{def:shadow-depth-classification\\}|label\\{thm:nms-finite-termination\\}|label\\{thm:universal-theta\\}|label\\{thm:universal-MC\\}|label\\{thm:genus-universality\\}|label\\{thm:modular-homotopy-convolution\\}|label\\{prop:geometric-modular-operadic-mc\\}|label\\{rem:modular-cyc-strictification\\}|label\\{constr:obstruction-recursion\\}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15690,15840p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2487:genus-$0$ data. The shadow depth classification
2489:(Definition~\ref{def:shadow-depth-classification})
11273:%% The operadic complexity and shadow depth classification below
12353:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}
16563:\label{def:shadow-depth-classification}
16767:\index{BPS particles!shadow depth classification}%
16771:The shadow depth classification reflects this decomposition:
16884:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
17159:degree-$3$ projection of the shadow depth classification:
17259:(Definition~\ref{def:shadow-depth-classification}).
17301:The shadow depth classification is a property of the algebra
17645:of Definition~\textup{\ref{def:shadow-depth-classification}}.
27676:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}\textup{)}
28572:(Definition~\textup{\ref{def:shadow-depth-classification}})
29877:(Definition~\ref{def:shadow-depth-classification}):
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3576:\label{thm:universal-theta}
chapters/theory/higher_genus_modular_koszul.tex:5561:\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
chapters/theory/higher_genus_modular_koszul.tex:10939:\label{thm:modular-homotopy-convolution}
chapters/theory/higher_genus_modular_koszul.tex:13003:\label{constr:obstruction-recursion}
chapters/theory/higher_genus_modular_koszul.tex:16563:\label{def:shadow-depth-classification}
 succeeded in 52ms:
   250	\prod_{\substack{g,n \\ 2g-2+n > 0}}
   251	\operatorname{Hom}\!\bigl(
   252	\cM_{\Ass}(g,n),\,
   253	\operatorname{End}_{\cA}(n)
   254	\bigr).
   255	\end{equation}
   256	The Hom carries no $\Sigma_n$-equivariance; this is the structural
   257	distinction from $\gAmod =
   258	\prod \operatorname{Hom}_{\Sigma_n}(\cM_\Com(g,n),
   259	\operatorname{End}_\cA(n))$
   260	(Definition~\ref{def:modular-convolution-dg-lie}), whose Hom-source
   261	uses the symmetric cooperad $\mathrm{Sym}^c$ obtained from $T^c$ by external
   262	$\Sigma_n$-coinvariants. The dg~Lie structure is inherited from
   263	$F\!\Ass$: $D$ from $D_{F\!\Ass}$, $[-,-]$ from ribbon-graph
   264	composition.
   265	The \emph{averaging map}
   266	\begin{equation}
   267	\label{eq:e1-to-einfty-projection}
   268	\operatorname{av}\colon
   269	{\gAmod}^{E_1}
 succeeded in 52ms:
 15690	\begin{remark}[The shadow obstruction tower as $L_\infty$-formality
 15691	obstruction: the homotopy-invariant statement]
 15692	\label{rem:shadow-tower-linfty-formality}
 15693	\index{formality!homotopy-invariant statement}
 15694	\index{shadow obstruction tower!$L_\infty$-formality obstruction}
 15695	Theorem~\ref{thm:shadow-formality-identification} identifies
 15696	the shadow obstruction tower with the formality obstruction tower for
 15697	the genus-$0$ part of $\gAmod$. The correct formulation
 15698	is at the homotopy-invariant level, not at the level of the
 15699	strict model.
 15700	
 15701	Let $\mathfrak{h}$ be the minimal $L_\infty$-model
 15702	of $\Definfmod(\cA)$, i.e., the transferred structure
 15703	$(\cA^{\mathrm{sh}}, \{\ell_n^{\mathrm{sh}}\})$
 15704	of Proposition~\ref{prop:shadow-algebra-linfty}.
 15705	Then $\Definfmod(\cA)$ is \emph{formal} (quasi-isomorphic to
 15706	its cohomology with trivial differential and the descended
 15707	Lie bracket) if and only if $\ell_n^{\mathrm{sh}} = 0$ for all
 15708	$n \geq 3$. The shadow obstruction tower measures the
 15709	deviation from formality:

thinking
**Investigating theorems**

I need to output my findings and gather specific problems related to the theorem or universal-theta and thm:universal-MC. I notice that the earlier definition at page 449 references theorem thm:universal-MC, but I'm questioning if that label even exists. I think it might be a case of unresolved references. So, I'll search for that label to clarify the situation. It's interesting how these connections can sometimes be tricky!
codex
A second-order issue has appeared: the chapter doesn’t just front-load undefined objects; some of the later “definitions” depend on labels that may not exist or may define a different object than the prose claims. I’m checking those now before I treat them as real imports.
exec
/bin/zsh -lc "rg -n 'label\\{thm:universal-MC\\}|ref\\{thm:universal-MC\\}|label\\{thm:universal-theta\\}|ref\\{thm:universal-theta\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{rem:modular-cyc-strictification\\}|ref\\{rem:modular-cyc-strictification\\}|label\\{thm:genus-induction-strict\\}|ref\\{thm:genus-induction-strict\\}|label\\{thm:bar-modular-operad\\}|ref\\{thm:bar-modular-operad\\}|label\\{thm:prism-higher-genus\\}|ref\\{thm:prism-higher-genus\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{def:e1-modular-convolution\\}|label\\{eq:e1-to-einfty-projection\\}|label\\{thm:fcom-coinvariant-fass\\}|label\\{thm:fass-d-squared-zero\\}' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3550,3665p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
175:\label{thm:fass-d-squared-zero}
194:\label{thm:fcom-coinvariant-fass}
234:\label{def:e1-modular-convolution}
267:\label{eq:e1-to-einfty-projection}
 succeeded in 51ms:
450:\textup{(}Theorem~\textup{\ref{thm:universal-MC}} for the
673:(Theorem~\ref{thm:universal-theta}).
2649:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2662: (Theorem~\ref{thm:universal-theta}):
2709:(Theorems~\ref{thm:universal-MC}
2710:and~\ref{thm:universal-theta}).
2805:Theorem~\ref{thm:universal-theta}, made unconditional by
2824:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
3576:\label{thm:universal-theta}
3651:Theorem~\ref{thm:universal-theta} extends the canonical twisting
5004:The proof of Theorem~\ref{thm:universal-theta} assembles:
5538:Theorem~\ref{thm:universal-theta}. Then:
8137:In particular, Theorem~\ref{thm:universal-theta}
8195:Theorem~\textup{\ref{thm:universal-theta}} with the stated scalar
8232: $\Theta_{\cA}$ of Theorem~\ref{thm:universal-theta};
8245:modular-operadic clutching identities. Theorem~\ref{thm:universal-theta}
8255:$\Theta_{\cA}$ (Theorems~\ref{thm:universal-theta}
10064:Theorem~\textup{\ref{thm:universal-theta}} \textup{(MC2)} holds
10132:(Theorem~\ref{thm:universal-theta}) is established
14318:(Theorem~\ref{thm:universal-theta}). By
 succeeded in 51ms:
26:(Theorem~\ref{thm:bar-modular-operad}).
269:(Theorem~\ref{thm:bar-modular-operad}).
302:(Theorem~\ref{thm:prism-higher-genus}(ii)) is
562:(Theorem~\ref{thm:prism-higher-genus}).
726:(Theorem~\ref{thm:bar-modular-operad}), (3)~Verdier duality commutes
3611:(Theorem~\ref{thm:bar-modular-operad}), and satisfies
3613:(Theorem~\ref{thm:bar-modular-operad}(iii)).
3723:Theorem~\textup{\ref{thm:genus-induction-strict}}.
3756:(Theorem~\ref{thm:bar-modular-operad}); it is the unique
3762:(Theorem~\ref{thm:genus-induction-strict}) holds by the locality
3784:\textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},
3945: of Theorem~\ref{thm:bar-modular-operad}(i)--(ii) in
3953: This is Theorem~\ref{thm:bar-modular-operad}(iii), itself
3954: proved via Theorem~\ref{thm:prism-higher-genus}:
4117: (Theorem~\ref{thm:bar-modular-operad},
4124: (Theorem~\ref{thm:prism-higher-genus},
5691:(Theorem~\ref{thm:prism-higher-genus}(i)) by summing
12485:(Remark~\ref{rem:modular-cyc-strictification}), carries an $L_\infty$
13356:(Theorem~\ref{thm:bar-modular-operad}).
13705:Theorem~\ref{thm:bar-modular-operad}, so the total differential
 succeeded in 51ms:
  3550	The spectral discriminant
  3551	$\Delta_{\cA}(x) = \prod_i (1 - \lambda_i x)$
  3552	depends only on the quadratic OPE data of the Koszul pair and is invariant
  3553	under Drinfeld--Sokolov reduction.
  3554	In particular, $\Delta_{\cA}$ is a separate non-scalar invariant:
  3555	it is not determined by $\kappa(\cA)$ alone.
  3556	\end{theorem}
  3557	
  3558	\begin{proof}
  3559	This is Theorem~\ref{thm:ds-bar-gf-discriminant}.
  3560	\end{proof}
  3561	
  3562	\begin{remark}[\texorpdfstring{$K$}{K}-theoretic hierarchy]\label{rem:spectral-characteristic-programme}
  3563	\index{spectral discriminant!K-theoretic hierarchy}
  3564	Setting $\mathcal{V}=[R\pi_{g*}\bar{B}^{(g)}(\cA)]\in
  3565	K_0(\overline{\mathcal{M}}_g)$: $c_1(\det\mathcal{V})$
  3566	recovers~$\kappa$, $\operatorname{ch}(\mathcal{V})$
  3567	recovers~$\Delta_{\cA}$, and the holonomy recovers~$\Pi_{\cA}$.
  3568	See Remark~\ref{rem:structural-saturation}.
  3569	\end{remark}

thinking
**Searching for labels**

I'm discovering a reference to `thm:universal-MC`, but there's no label attached to it. I need to search for any mentions of `thm:universal-MC` and check for labels. It’s possible that this is an unresolved reference. Maybe I should build a check or grep for all existing labels. The user wants grounded file contents, so if the label exists somewhere else, it might not be an issue. I'll conduct a global search to find out.
exec
/bin/zsh -lc "rg -n 'label\\{thm:universal-MC\\}' chapters appendices ." in /Users/raeez/chiral-bar-cobar succeeded in 65ms:
./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:683:   661	\phantomsection\label{thm:universal-MC}
chapters/connections/concordance.tex:5345:\ClaimStatusProvedHere]\label{thm:universal-MC}
chapters/connections/outlook.tex:661:\phantomsection\label{thm:universal-MC}
./healing_20260413_132214/H11_SC_formal_alt.md:13232:\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:24398:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:35562:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:46727:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:57892:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:69055:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:80218:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:91356:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:102539:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:113712:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:124906:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:136113:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:147306:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:158482:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:169659:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:180841:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}
./healing_20260413_132214/H11_SC_formal_alt.md:191943:-\newlabel{thm:universal-MC}{{K.7.1}{2704}{Practical recommendations}{section*.331}{}}

thinking
**Identifying citation issues**

I see that in this chapter, the first use at line 180 lacks an accompanying import citation for def:e1-modular-convolution. Instead, it only has a proposition reference and a theorem reference. I really need to fix this by adding an explicit import line that mentions `{\gAmod}^{E_1}` along with the averaging map before that first usage. It seems pretty important to address, so I’ll make sure to get it right!
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1738,1752p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5328,5360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{def:modular-deformation-complex\\}|ref\\{def:modular-deformation-complex\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3650,3695p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3661:\textup{(}Definition~\textup{\ref{def:modular-deformation-complex})}.}
 succeeded in 52ms:
  1738	 \phantomsection\label{rem:four-levels}%
  1739	 \phantomsection\label{subsec:anomaly-koszul}%
  1740	 \phantomsection\label{subsec:vassiliev}%
  1741	 \phantomsection\label{rem:en-scope}%
  1742	 \phantomsection\label{rem:proof-roadmaps}%
  1743	 \phantomsection\label{rem:structural-gaps}%
  1744	 \phantomsection\label{rem:cat-o-generation-obstruction}%
  1745	 % --- Concordance theorems/conjectures ---
  1746	 \phantomsection\label{thm:universal-MC}%
  1747	 \phantomsection\label{thm:volume-one-concrete-modular-datum}%
  1748	 \phantomsection\label{thm:master-theta}%
  1749	 \phantomsection\label{thm:master-pbw}%
  1750	 \phantomsection\label{thm:discriminant-spectral}%
  1751	 \phantomsection\label{thm:lagrangian-complementarity}%
  1752	 \phantomsection\label{thm:anomaly-koszul}%
 succeeded in 51ms:
  5328	(Theorem~\ref{thm:lattice-sewing}), is \ClaimStatusProvedHere{} (promoted from conjecture).
  5329	Targets (C$_{\mathrm{an}}$) and~(D$_{\mathrm{an}}$) remain \ClaimStatusConjectured{}.
  5330	The programme is recorded here to fix definitions and their
  5331	relationship to the algebraic proved core.
  5332	On the derived-algebraic side, Nafcha proves a gluing formula for
  5333	chiral homology on families of stable curves [arXiv:2603.30037],
  5334	complementing the analytic HS-sewing criterion: Nafcha's formula
  5335	operates on derived categories of D-modules on the Ran space;
  5336	HS-sewing operates on Hilbert-space trace-class estimates.
  5337	
  5338	\subsection{The universal Maurer--Cartan class}
  5339	
  5340	The genus tower $\{\barB^{(g)}(\cA)\}_{g \geq 0}$
  5341	(Theorem~\ref{thm:master-tower}) is controlled by a universal
  5342	obstruction.
  5343	
  5344	\begin{theorem}[Universal MC class;
  5345	\ClaimStatusProvedHere]\label{thm:universal-MC}
  5346	\index{Maurer--Cartan class!universal}
  5347	For a modular Koszul chiral algebra $\cA$ with non-degenerate
 succeeded in 52ms:
  3650	\index{modular twisting cochain|textbf}
  3651	Theorem~\ref{thm:universal-theta} extends the canonical twisting
  3652	morphism $\pi \colon \barB_X(\cA) \to \cA$ of genus-$0$ bar-cobar
  3653	duality (Proposition~\ref{prop:universal-twisting-adjunction}) to
  3654	higher genus by a single algebraic step:
  3655	\emph{promoting the twisting morphism from flat to curved, and from
  3656	the convolution algebra $\mathrm{Hom}(\barB, \cA)$ to the modular
  3657	convolution algebra
  3658	$\operatorname{Def}^{\mathrm{mod}}(\cA) =
  3659	\prod_{g,n} \mathrm{Hom}_{\Sigma_n}(C_*(\overline{\mathcal{M}}_{g,n}),
  3660	\operatorname{End}_\cA(g,n))$
  3661	\textup{(}Definition~\textup{\ref{def:modular-deformation-complex})}.}
  3662	
  3663	\emph{Precise formulation.}
  3664	Define the \emph{modular twisting cochain}
  3665	\begin{equation}\label{eq:modular-twisting-cochain}
  3666	\tau_{\mathrm{mod}}
  3667	\;:=\;
  3668	\pi \;+\; \sum_{g \geq 1} \hbar^{g}\,
  3669	\Theta_\cA^{(g)}

thinking
**Searching for missing module**

I'm trying to figure out if `def:modular-deformation-complex` is missing. I'll conduct a search to see if it exists anywhere in the repository. It could turn up something interesting or necessary for my work. I need to inspect the labeling closely to determine if I can find it or if it’s indeed absent. It feels a bit like a treasure hunt, and I wonder what I'll discover!
exec
/bin/zsh -lc "rg -n 'label\\{def:modular-deformation-complex\\}' chapters appendices main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_hochschild_koszul.tex:2819:\label{def:modular-deformation-complex}

thinking
**Inspecting definitions for clarity**

I need to check the definition in another file to see if there’s a mismatch with g_mod. It might not be necessary, but if it's being referenced before the local g_mod definition, it could be causing some hidden import issues. So, it seems relevant to read through the definition. I want to make sure I understand all the details to avoid any complications down the line.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '2800,2855p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2800	legs carry deformation inputs, internal edges carry the Szeg\H{o}
  2801	propagator $S(z,w)$, and internal vertices carry $A_\infty$
  2802	operations. The homotopy Jacobi identity is the Ward identity,
  2803	mediated by Stokes' theorem on $\ConfigSpace{k}$. At
  2804	$L > 0$ (loop level), $L = g$
  2805	loop diagrams produce the genus-$g$ obstruction; the cyclic pairing ensures the BV QME order by
  2806	order~\cite{costello-renormalization}.
  2807	\end{remark}
  2808	
  2809	\subsection{The modular deformation complex}
  2810	\label{subsec:modular-deformation-complex}
  2811	\index{modular deformation complex|textbf}
  2812	
  2813	The genus-$0$ cyclic deformation complex
  2814	$\Defcyc(\cA)$ (Definition~\ref{def:cyclic-deformation-elementary})
  2815	is the tree-level shadow of a modular quantum $L_\infty$-algebra.
  2816	The modular version assembles all genera:
  2817	
  2818	\begin{definition}[Modular deformation complex]
  2819	\label{def:modular-deformation-complex}

thinking
**Inspecting code definitions**

I'm thinking this might be a hidden import from chiral_hochschild_koszul, but the target file later defines a modular convolution dg Lie algebra. That could be okay, yet if I'm using `Def^{mod}` before the local definition, it might not be ideal. I need to assess the severity of this. It seems I should check the lines around `def:shadow-depth-classification` around 16563 to get more context and make a better decision.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16540,16640p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 16540	and~\ref{prop:linfty-obstruction-5-6} respectively.
 16541	Part~(iii) follows from the explicit verification tables in
 16542	those propositions: for classes $\mathbf{G}$,
 16543	$\mathbf{L}$, $\mathbf{C}$, all three quantities vanish at
 16544	degrees $5$, $6$, $7$ because the tower terminates
 16545	earlier. For class $\mathbf{M}$, all three are nonzero
 16546	because $\Delta \neq 0$ forces $S_k \neq 0$ for all
 16547	$k \geq 4$
 16548	(Theorem~\ref{thm:single-line-dichotomy}).
 16549	
 16550	The tree count at degree~$7$ for the stable-graph route is
 16551	$(2 \cdot 8 - 5)!! = 11!! = 10395$: this is the number of
 16552	trivalent trees with $8$ external legs, which are the
 16553	fully resolved genus-$0$ stable graphs contributing to the
 16554	bracket $\ell_7^{(0)}$. The agreement with the HPL
 16555	route ($C_6 = 132$ planar trees) and the Feynman transform
 16556	route ($C_7 = 429$ binary trees on $8$ leaves) is a
 16557	consequence of the universal property
 16558	(Theorem~\ref{thm:shadow-formality-identification},
 16559	Step~$3$).



thinking
**Inspecting MC Equation Order**

I need to take a closer look at the definition order of the MC equation. Okay, I’ll consider how the different components are arranged and if that aligns with standard conventions. It seems important because any mix-up in order could lead to misunderstandings or errors in calculations. This could affect any results or applications derived from it. Let’s clarify everything to ensure accuracy.
thinking
**Investigating theorem dependencies**

I need to find the first proof that uses the MC equation before Theorem 3774 or Definition 31031. I should search for `\begin{proof}` before line 3774, which might hint at a forward dependency rather than an undefined equation. It looks like there's a proposition statement on line 236 that includes Theta and a reference to the universal MC element before the theorem appears much later. Forward references are acceptable in math, but it raises concerns if definitions are truly made before use. I’ll consider inserting an "Imported foundations" block for clarity.
thinking
**Inspecting local context**

I think I should take a closer look at the local context around line 673, especially where `\Theta_\cA^{\le2}` appears. I’m considering searching through lines 640 to 700 to see if there's another use of the full modular characteristic package before the theorem. This might help clarify the dependencies or further define the concepts at play. Understanding the surrounding content could be crucial for my analysis! Let's dive in and find out what’s there.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '640,690p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   640	An algebra satisfying both the axioms and their consequences is a
   641	\emph{modular Koszul chiral algebra}.
   642	\end{definition}
   643	
   644	\begin{remark}[Axioms versus consequences]\label{rem:mk-axioms-vs-consequences}
   645	Only MK1--MK3 are axioms; MK4 and MK5 are
   646	consequences proved (Theorems~\ref{thm:higher-genus-inversion} and
   647	\ref{thm:quantum-complementarity-main}) and are not axioms. For
   648	modular Koszul chiral algebras with simple Lie symmetry, MK6 and MK7
   649	are further theorematic consequences of the universal MC package
   650	(Lemma~\ref{lem:mk67-from-mc2}). MK8 is the remaining
   651	ordered-factorization open problem.
   652	\end{remark}
   653	
   654	\begin{remark}[Logical structure]\label{rem:mk-axiom-relations}
   655	The definition separates \emph{hypotheses} (MK1--MK3) from
   656	\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
   657	There is no circularity. The dg axioms MK1--MK3 present the homotopy axioms
   658	\ref{MK:koszul-htpy}, \ref{MK:verdier-htpy},
   659	and~\ref{MK:modular-htpy} of

thinking
**Inspecting definitions in code**

I notice that MK6 at line 671 is using `Defcyc(\cA)\widehat{\otimes}\Gmod` before either Gmod or Defcyc is defined. This might mean they were defined earlier, but it could also be a hidden import. However, the user seems focused on specific foundational objects, so perhaps this isn't a critical point. I think it’s important to check the e1 modular convolution definition around line 234 for further context.
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '228,290p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   228	ribbon-forgetting step is absorbed into the identification of the
   229	target at the Hom-level, where $\operatorname{End}_\cA(n)$ sees only
   230	external legs.
   231	\end{proof}
   232	
   233	\begin{definition}[$E_1$ modular convolution dg~Lie algebra]
   234	\label{def:e1-modular-convolution}
   235	\ClaimStatusProvedHere
   236	\index{E1 algebra@$E_1$-algebra!modular convolution|textbf}
   237	\index{modular convolution dg Lie algebra!E1@$E_1$ (ordered)}
   238	Let $\cA$ be a cyclic $E_1$-chiral algebra
   239	(Definition~\ref{def:e1-chiral}).
   240	The degree-$n$ component of the ordered bar complex is the tensor
   241	coalgebra $T^c(s^{-1}\bar\cA)$ built on the augmentation ideal
   242	$\bar\cA = \ker(\varepsilon)$, with $n$ linearly ordered external
   243	legs and deconcatenation coproduct (distinct from the coshuffle
   244	coproduct of $\mathrm{Sym}^c$). The modular grading is supplied
   245	separately by $\cM_{\Ass}(g,n)$ above.
   246	\begin{equation}
   247	\label{eq:e1-modular-convolution}





thinking
**Identifying notation inconsistencies**

I'm noticing that the notation changes from `\mathsf{G}` to `\mathbf{G}`. This shift could potentially confuse the user, and it seems like a flag for notation drift. I should check if both styles are used consistently throughout. It looks like this could be a low to medium issue. Since the user specifically asked for an exact fix, I need to clarify that classes are later defined with `\mathbf`, but the opening uses `\mathsf`. That's definitely notation drift.
thinking
**Assessing notation and definitions**

I should consistently use `\mathbf` and change various line numbers accordingly. Since the user asked for definitions, that seems critical. There's a notation mismatch to address. I need to check if `shadow tower Theta_A` is formally defined. The definition appears at line 12248, but earlier, line 121 states "The tower Theta_A forces three questions," and line 36 introduces Theta_A. It looks like I need to insert a formal definition after line 47 for clarity.
thinking
**Analyzing definitions and equations**

I’m looking at the expression for \(\Theta_\cA^{\le r}\) and notice it seems exact. Line 39 uses `d_0 Theta + 1/2[Theta,Theta]=0`, but the equation is later written as `D\Theta + 1/2[...] = 0`. This inconsistency between `d_0` and `D_\cA` might not be a major issue, but it could help if I unify how I introduce these equations. I could add a clear definition for `[D,\Theta] + ...` in the opening and refer back to Theorem thm:mc2-bar-intrinsic while keeping operator notation consistent.
thinking
**Evaluating trace operation findings**

I'm looking into the definition of the trace operation or Theta component, but I want to make sure not to overwhelm the user. They've asked for an exhaustive audit, indicating we might need to cover 8-12 findings instead of just 4. I'll check early sections for any hidden imports, like classes that aren’t defined before use, and ensure I reference the modular characteristic package correctly. It's also important to investigate if any proofs reference classes earlier in the document, since it could be critical.
thinking
**Inspecting shadow depth classes**

I notice that the theorem around 15701 mentions the four shadow depth classes before its formal definition at 16563, which could be a potential issue. The user asked for an overview, but there's a contradiction between lines 16562 and 17614 that needs mentioning. I need to check line 60 regarding `gAmod`, which refers to an undefined notation. A possible fix could be moving the relevant definitions and remarks to precede line 59 or replacing those lines with a clearer cross-reference. The user is looking for an exact solution.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5530,5595p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5530	\index{MC2!reduction principle}
  5531	Let $\cA$ be a modular Koszul chiral algebra. Assume that the
  5532	bar-intrinsic complex $\Defcyc(\cA)$ of
  5533	Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
  5534	$L_\infty$-algebra, and let $\{W_g\}_{g \geq 0}$ be finite-dimensional
  5535	coefficient spaces chosen from
  5536	$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
  5537	modular-operadic package of
  5538	Theorem~\ref{thm:universal-theta}. Then:
  5539	\begin{enumerate}[label=\textup{(\roman*)}]
  5540	\item the universal Maurer--Cartan problem for $\Theta_{\cA}$ is posed
  5541	 on the genus-completed convolution algebra
  5542	 $\widehat{L}_W = \prod_{g \geq 0}\Defcyc(\cA)\otimes W_g$, and its
  5543	 genus-$g$ equation is a finite sum;
  5544	\item extending a partial solution through genus~$g-1$ to genus~$g$ is
  5545	 obstructed by a class in
  5546	 $H^2(\Defcyc(\cA), l_1) \otimes W_g$;
  5547	\item if $H^2(\Defcyc(\cA), l_1) \cong \mathbb{C}$, then the
  5548	 genus-$g$ extension problem has a single obstruction channel valued
  5549	 in~$W_g$.
exec
/bin/zsh -lc "rg -n 'label\\{rem:modular-cyc-strictification\\}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:2044:\label{rem:modular-cyc-strictification}

thinking
**Updating progress on tasks**

I want to check cross-file hidden imports, but first, I need to see if the theorem `thm:genus-universality` label exists and where. I think searching in the same file might help, but it’s not absolutely necessary. It might be a good idea to use `update_plan` for tracking progress. I believe steps 1 and 2 are completed, and step 3 is still in progress, so it's time to update!
Plan update
Mapped first-use sites and traced the cited foundational labels across the target file and direct dependencies. I’m now consolidating the surviving issues, with emphasis on forward-definition failures, carrier ambiguity, and internal contradictions.
  ✓ Map first-use sites in the target file for Theta_A, shadow tower, G/L/C/M, Maurer-Cartan equation, g^{E1}, and g^{mod}
  ✓ Read the target file at each first-use site and inspect the cited labels that are supposed to supply the missing foundations
  → Check for unresolved or weakly imported references and second-order dependency gaps around the foundational claims
  • Assemble only re-verified findings with exact fixes and final verdict

thinking
**Inspecting code references**

I need to take a closer look at the code, specifically around line 2709 concerning "thm:universal-MC." There might be semantically incorrect references there. It sounds like a good idea to search in the area of lines 2695 to 2715 to gather more context. I'm trying to ensure I get everything right, and a more thorough inspection will help clarify any issues that might be lurking there!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2698,2715p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2698	 boundary degeneration on~$\overline{\mathcal{M}}_{g,n}$;
  2699	\item \emph{Non-scalar}: $\kappa(\cA)$ is only the first shadow;
  2700	 the full package contains strictly more information
  2701	 (cf.\ the spectral data of level~(2) in
  2702	 Remark~\ref{rem:characteristic-hierarchy}).
  2703	\end{enumerate}
  2704	
  2705	\smallskip\noindent
  2706	The cyclic $L_\infty$-algebra $\Defcyc(\cA)$ is constructed
  2707	by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
  2708	is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
  2709	(Theorems~\ref{thm:universal-MC}
  2710	and~\ref{thm:universal-theta}).
  2711	\end{definition}
  2712	
  2713	\begin{definition}[Uniform-weight lane (scalar lane)]
  2714	\label{def:scalar-lane}
  2715	\label{def:uniform-weight-lane}
codex
The foundational surface is mostly established now. I’m doing one last pass for non-obvious failures that hide behind “defined later” language: theorem-label drift, carrier mismatches, and any proved statement in this file that quietly contradicts another statement in the same file.
exec
/bin/zsh -lc "rg -n 'higher_genus_modular_koszul\\.tex' suspicious_proved_claim_dependencies.csv master_claim_ledger_filtered.csv label_status_conflicts.csv 2>/dev/null" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theta_\\\\cA\\"'^'"\\{\\\\leq 2\\}|= \\\\kappa\\(\\\\cA\\)|operatorname\\{MC\\}\\(\\\\gAmod/F\\"'^'"\\{3\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'd_alg|kappa_d|r_max|every finite value is realized|finite depths .* realized|d \\in \\{2,3,4,5' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'mathsf\\{G\\}|mathbf\\{G\\}|mathsf\\{L\\}|mathbf\\{L\\}|mathsf\\{C\\}|mathbf\\{C\\}|mathsf\\{M\\}|mathbf\\{M\\}' chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:d_alg|kappa_d|r_max|every finite value is realized|finite depths .* realized|d \in \{2,3,4,5)
                                                                                      ^^
error: unrecognized escape sequence
 succeeded in 52ms:
12: d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
397: \arrow[r, phantom, "\scriptstyle \dfib^{\,2} = \kappa(\cA) \cdot \omega_g"]
488:$\mathrm{obs}_g = \kappa(\cA) \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}) for
491:genus-$1$ identity $\mathrm{obs}_1 = \kappa(\cA) \cdot \lambda_1$ is
565:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
2567: $\dfib^{\,2} = \kappa(\cA)\,\omega_g$ forces
2622: fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
2728:On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
2754: $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g\cdot\operatorname{id}$ and the
2866: $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
2906: $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
2967:The curvature $d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$
3121:F_g(\cA) = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}
3187:\item The genus-$1$ identity $F_1(\cA) = \kappa(\cA)/24$ of
3197:$\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$ of
3220:$F_1(\cA) = \kappa(\cA)/24$. Clauses (i)--(iii) then follow
3429:matrix size $N^2 = \kappa(\cA)$:
3431:F_g(\cA) \;=\; F_g^{\mathrm{GUE}}(N^2 = \kappa(\cA))
3461:$N^2 = \kappa(\cA)$ matches the two term by term.
3624:= \kappa(\cA)\lambda_1$.
 exited 2 in 52ms:

 succeeded in 51ms:
136: (class~$\mathsf{G}$, Gaussian).
138: (class~$\mathsf{L}$, Lie).
140: depth~$4$ (class~$\mathsf{C}$, contact).
144: (class~$\mathsf{M}$, mixed).
155: partition $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is the
172:(class~$\mathsf{G}$, formal, quadratic)
507:$\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})$
509:$\mathbf{C}_g \simeq \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$,
511:\colon \mathbf{C}_g \to \mathbf{C}_g)$ and
2488:$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
4519:$\mathsf{G}^{\pm}_{\mathrm{mod}}(\cA)$ with mixed propagators
4553: For finite-depth algebras (classes $\mathsf{G}$, $\mathsf{L}$,
4554: $\mathsf{C}$), the truncation
4559: For class~$\mathsf{M}$ (Virasoro, $\mathcal{W}_N$), the
4592:Depth termination: for classes $\mathsf{G}$, $\mathsf{L}$,
4593:$\mathsf{C}$, the obstruction classes $o_{r+1}(\cA) = 0$
5917:$C_g$ for $\mathbf{C}_g(\cA)$ with strict involution $\sigma$,
5940: $\mathbf{L}_g \subset C_g^+$ and
5941: $\mathbf{L}_g^! \subset C_g^-$ such that:
5945: H^*(\mathbf{L}_g) = L_g,

thinking
**Inspecting CSV issues**

It seems like the rg for CSV failed due to possibly absent files, but that's alright since we have enough data to work with. I should check `label_status_conflicts.csv`, even if it may not be needed. There's this potential issue with the imprecision of `\Theta^{≤2}=\kappa(\cA)` appearing multiple times. The user specifically requested an exact fix for lines 29803 and 29847, so I could cite those while referencing line 12284 for the correct formula. I'll make sure to look around lines 29795-29805 to gather everything needed.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29796,29808p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 29796	 \;=\;
 29797	 -\,\frac{\kappa}{6\pi}
 29798	 \int_{\Sigma_g}
 29799	 \bigl(|\nabla \sigma|^2 + R_{g_0}\,\sigma\bigr)\,
 29800	 d\mu_{g_0}
 29801	\end{equation}
 29802	is the evaluation of the degree-$2$ shadow
 29803	$\Theta_\cA^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 29804	\textup{(}where $\eta$ is the cyclic pairing and $\Lambda$ the
 29805	modular graph class\textup{)} against the conformal
 29806	deformation~$\sigma$.
 29807	
 29808	\item The coefficient $\kappa/(6\pi)$ involves the modular
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12190,12235p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 12190	algebra its pronilpotent completion), an extension tower (to define
 12191	the MC locus at each finite truncation order), and the shadow
 12192	obstruction tower itself (the sequence of truncated MC elements
 12193	whose inverse limit is~$\Theta_\cA$).
 12194	
 12195	\begin{definition}[Weight filtration]
 12196	\label{def:weight-filtration-tower}
 12197	\index{weight filtration!definition|textbf}
 12198	Each component of the modular convolution algebra carries a
 12199	\emph{tridegree} $(g, r, d)$, where
 12200	$g \geq 0$ is the loop genus (genus label on the stable graph),
 12201	$r \geq 2$ is the degree (number of external half-edges), and
 12202	$d \geq 0$ is the planted-forest depth (codimension of the
 12203	log-FM boundary stratum in the sense of
 12204	Definition~\ref{def:vol1-rigid-planted-forest-depth-filtration}).
 12205	Define the \emph{total weight}
 12206	\[
 12207	w(g, r, d) \;:=\; 2g - 2 + r + d.
 12208	\]
 12209	The stability condition $2g - 2 + n > 0$ ensures $w \geq 1$.

thinking
**Searching for definitions**

I see there's a term, `g^{amb}`, that's been introduced without a formal definition. My next step is to search for its definition to understand what it means and how it applies. It’s important to clarify terms so I'm accurately conveying information. I'll check various reliable sources to ensure I find the best possible explanation for `g^{amb}`. Let’s see what I can uncover!
exec
/bin/zsh -lc "rg -n 'g\\"'^'"\\{\\\\mathrm\\{amb\\}\\}|ambient modular convolution|label\\{def:.*amb' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
31032:\label{def:ambient-master-equation}
31198:\label{def:ambient-modular-complementarity-algebra}
31675:\label{def:ordered-ambient-algebra}
exec
/bin/zsh -lc "rg -n '\\\\mathfrak\\{g\\}\\"'^'"\\{\\\\mathrm\\{amb\\}\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12212:F^N\mathfrak{g}^{\mathrm{amb}}_{\cA}
12214:\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
12219:($\mathfrak{g}^{\mathrm{amb}} = F^1$),
12224:= \varprojlim_N \mathfrak{g}^{\mathrm{amb}}/F^{N+1}$
12240:\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{N+1}
12266:$\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{r+1}$,
31112:\in \operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA})$
31121:\operatorname{MC}(\mathfrak{g}^{\mathrm{amb}}_{\cA}).
31125:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ by $\Theta_{\cA}$; the genus
31164:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
31203:\mathfrak{g}^{\mathrm{amb}}_{\cA}
31320: $\mathfrak{g}^{\mathrm{amb}}_{\cA}$
31323: contributes to $F^w\mathfrak{g}^{\mathrm{amb}}_{\cA}$.
31342:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ through the Hom functor.
31429:$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
31701:\mathfrak{g}^{\mathrm{amb}}_\cA.
31712:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ of
31758:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$
31959:$\mathfrak{g}^{\mathrm{amb}}_{\cA}$ could use

thinking
**Investigating definitions**

I'm noticing there's no definition label, so I feel like I need to inspect around 31198. There might be something about ambient modular complementarity algebra, perhaps defining g^{amb}. I think I should search around the references from 31190 to 31215 to see if there's more information or context I can find to clarify things. It's always good to ensure I have a complete understanding!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31188,31218p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31188	\end{enumerate}
 31189	\end{remark}
 31190	
 31191	\subsection{The carrier algebra}
 31192	\label{subsec:carrier-algebra}
 31193	
 31194	The graph sum~\eqref{eq:modular-bar-hamiltonian} lives in a specific
 31195	graded vector space.
 31196	
 31197	\begin{definition}[Ambient modular complementarity algebra]
 31198	\label{def:ambient-modular-complementarity-algebra}
 31199	The \emph{carrier} for the modular bar--Hamiltonian is the filtered
 31200	completed graded vector space
 31201	\begin{equation}
 31202	\label{eq:ambient-modular-complementarity-algebra}
 31203	\mathfrak{g}^{\mathrm{amb}}_{\cA}
 31204	:=
 31205	\bigl(L_{\cA} \oplus K_{\cA} \oplus L_{\cA^!}\bigr)
 31206	\widehat\otimes \mathbb{G}_{\mathrm{st}}
 31207	\widehat\otimes \mathbb{G}_{\mathrm{pf}},










thinking
**Identifying a definition issue**

I see that `\mathfrak g^{amb}_A` is only defined at line 31197, but it's used at line 12212. This indicates a problem with the hidden import or ordering. The shadow obstruction tower definition actually uses `\mathfrak g^{amb}_A/F^{r+1}` almost 19,000 lines earlier than its definition, which is a big deal. The fix needs to either move the definition up before line 12195 or rewrite the tower to use `\gAmod` first. This could be critical because the shadow tower's formal definition relies on an undefined ambient carrier. It’s great that I've pinpointed this!
thinking
**Deciding on a definition fix**

I need to either define `\mathfrak g^{amb}` first and show how it projects to `gAmod`, or replace the lines from 12195 to 12301 with the existing coinvariant carrier `\gAmod`. Since the user is asking for an exact fix, I could suggest adding a definition at line 12195, taking it from Definition 31197, or moving that definition entirely. Then I need to decide on a single carrier to stick with. If the shadow tower uses the ambient carrier, I'll update relevant captions; if it uses the coinvariant carrier, I’ll replace `\mathfrak g^{amb}` accordingly. I should also check what the opening line states regarding `\gAmod` and ensure all details align properly.
thinking
**Organizing findings and checks**

I’m considering a way to summarize my findings for a report. I might need to search for definitions and previous occurrences of certain elements, like `\cA^{sh}`, from before line 12501. I think I can count the number of lines checked, perhaps stating something like "Checked: 18 anchors | Findings: 9 | Verdict: FAIL." It's important to be clear about what I'm reporting, as the contract specifies certain terms. I'll make sure my summary stays concise but informative.
thinking
**Structuring findings by severity**

I need to organize my findings based on severity, which will help clarify the issues. I think starting with [CRITICAL] and then following with HIGH, and so on, makes sense. It's essential to stick to a clear format, like `[SEVERITY] file:line — PROBLEM: ... FIX: ...`. This way, anyone reviewing the report can easily understand both the severity of the problems and the corresponding fixes. Consistency in the format will ensure clarity in my communication.
thinking
**Addressing duplicate labels**

I’m encountering a problem with a duplicate phantom label in the document that clashes with a real theorem. The issue arises from a label in main.tex conflicting with one in the concordance file. The user wants an audit, so I should reference both files to provide a clear fix. I might also calculate how many files I've checked and mention that. It’s crucial to ensure all claims are well-supported by the document contents I've reviewed.
thinking
**Citing definitions and findings**

I should probably mention where definitions occur later in the text. Each finding can cite not just the target line but also refer to the appropriate line number later on. That way, it’s grounded in the document and makes it easier for the user to follow along. Clear references will help ensure everything is accurately tracked, which should improve the overall clarity and usefulness of my findings. This way, I can make my response much more valuable!
thinking
**Investigating duplicate labels**

I need to look into the issue regarding the duplicate label `thm:universal-MC`. It seems like I might find relevant information in a target file at line 450 or in the main file at line 1746. I'm wondering about the severity level of this issue as it looks high. It's important to clarify this because I want to ensure accurate handling of the situation. Let's see what I uncover!
thinking
**Evaluating theorem revisions**

I need to remove the optional clause from Data item D3 and then relocate the MC datum to the consequence list. For instance, I want to add that when Theorem\ref{thm:universal-theta} applies, the object will carry a canonical genus-completed Maurer–Cartan class `\Theta_\cA`.  

I noticed a problem in the full modular package regarding Theorem\ref{thm:mc2-bar-intrinsic}, which claims it gives the universal MC class. However, it only applies to a modular Koszul chiral algebra, which is misrepresented in the prose.
thinking
**Analyzing verdict details**

I need to determine a verdict, which is FAIL. It might help to mention the findings: "Checked: 11 | Findings: 10 | Verdict: FAIL." I should have around 25 lines, but 10 bullets could make it over 30 lines. I want to keep each bullet concise but thorough.  

I need to ensure no unsupported statements, especially regarding specific labels and the local theorem. I'm also noting potential issues with definitions and ambiguities, particularly around the terms used for certain equations and their references. Finally, it’s crucial to format everything as a precise bullet list.
thinking
**Finalizing summary details**

The user requested a summary that highlights specific problem-fix pairs formatted with critical attention. I should consider ending the summary without a bullet. I need to check the final answer length, aiming for around 25 to 30 lines. I realize each bullet could wrap into multiple lines, making it possible to stay under 70 lines, but I'm estimating the final text will likely be about 45 to 50 lines. I also want to ensure clarity by excluding file ranges in the summary line, keeping it straightforward with just the necessary numbers.
codex
- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:12248` — PROBLEM: `def:shadow-postnikov-tower` is not a valid formal definition when introduced. It defines `\Theta_\cA^{\le r}` inside `\mathfrak g^{\mathrm{amb}}_\cA/F^{r+1}`, but `\mathfrak g^{\mathrm{amb}}_\cA` is not defined until `31197`, and the same tower is later captioned in `\gAmod/F^{r+1}` at `12459-12462`. The carrier is undefined at the moment of definition and inconsistent inside the same local block. FIX: move Definition `def:ambient-modular-complementarity-algebra` (`31197-31217`) to immediately before `12195`, then choose one carrier and use it everywhere. If the tower is ambient, change `12459-12462` and `12478-12480` from `\gAmod` to `\mathfrak g^{\mathrm{amb}}_\cA`; if it is coinvariant, replace `12212-12301` by `\gAmod` and delete `\mathfrak g^{\mathrm{amb}}_\cA` from the tower definition.

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:16616` — PROBLEM: the formal classification says finite shadow depths `5,6,7,\dots` occur and “every finite value is realized,” but Proposition `prop:depth-gap-trichotomy` later proves `d_{\mathrm{alg}}\in\{0,1,2,\infty\}` and “no finite `d_{\mathrm{alg}}\ge 3` is realized” at `17621-17645`. This is an internal contradiction on the same theorem surface. FIX: delete `16616-16630` and replace them with: “These four classes are exhaustive and mutually exclusive. By Proposition~\ref{prop:depth-gap-trichotomy}, the only algebraic depths are `0,1,2,\infty`, corresponding to `\mathbf{G},\mathbf{L},\mathbf{C},\mathbf{M}`.” If a different notion of depth is intended, introduce it under a new symbol and prove the comparison before using it.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:37` — PROBLEM: `\Theta_\cA`, its truncations, and the Maurer--Cartan equation are used as if already formal, but the first bar-intrinsic definition of `\Theta_\cA` is at `3774-3798`, the first formal shadow-tower definition is at `12248-12300`, and the first named master-equation definition is at `31031-31056`. The opening is foundationally backward. FIX: insert immediately after line `36` a local definition block: “Set `\Theta_\cA:=D_\cA-\dzero\in\mathfrak g_\cA^{\mathrm{mod}}`. For `r\ge2`, let `\Theta_\cA^{\le r}:=\pi_{\le r}(\Theta_\cA)\in \MC(\mathfrak g_\cA^{\mathrm{mod}}/F^{r+1})`; the inverse system `(\Theta_\cA^{\le2}\to\Theta_\cA^{\le3}\to\cdots)` is the shadow obstruction tower. The strict MC equation is `[\dzero,\Theta_\cA]+\tfrac12[\Theta_\cA,\Theta_\cA]=0`.” Then keep the later theorem as the proof, not the first definition.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:59` — PROBLEM: `\gAmod` and `\Definfmod(\cA)` are invoked before they are defined. The strict model appears only at `10179-10224` and the two-level convention only at `10831-10908`, so the opening asks the reader to accept undefined carrier algebras on trust. FIX: add a notation import before line `59`: “`\mathfrak g_\cA^{\mathrm{mod}}:=\prod_{2g-2+n>0}\Hom_{\Sigma_n}(C_*(\overline{\mathcal M}_{g,n}),\End_\cA(n))` is the strict modular convolution dg Lie algebra; `\Definfmod(\cA)` is the homotopy-invariant modular deformation `L_\infty`-algebra, with `\mathfrak g_\cA^{\mathrm{mod}}` as strict model.” Cite Definition~\ref{def:modular-convolution-dg-lie} and Remark~\ref{rem:two-level-convention} there.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:52` — PROBLEM: the obstruction class is placed in `H^2(\cA^{\mathrm{sh}}_{r+1,0})` before the shadow algebra `\cA^{\mathrm{sh}}` is defined at `12501-12549`. The target of the obstruction map is undefined at first use. FIX: either move Definition~\ref{def:shadow-algebra} before line `52`, or rewrite `52-55` as “the obstruction classes land in the degree-`r+1`, genus-`0` piece of the shadow algebra to be defined in Definition~\ref{def:shadow-algebra}” and postpone the displayed cohomology target until after `12501`.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:136` — PROBLEM: the four classes `\mathsf{G},\mathsf{L},\mathsf{C},\mathsf{M}` are used 16k lines before their formal definition at `16562-16637`, and the notation changes from `\mathsf{}` here to `\mathbf{}` in the definition at `16586-16610`. This is both a forward-definition failure and a notation drift on a load-bearing classification. FIX: insert a local definition immediately before line `121` with the four classes and their depth criteria, and standardize to one macro everywhere, e.g. replace the opening `\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}` by the same `\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}` used at `16586-16610`.

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:180` — PROBLEM: `\Theta_\cA^{E_1}` is used as a known object, but the ordered carrier `{\gAmod}^{E_1}` and the averaging map `\operatorname{av}\colon{\gAmod}^{E_1}\twoheadrightarrow\gAmod` are not introduced here; they are defined only in `chapters/theory/e1_modular_koszul.tex:233-288`, and the opening does not cite that definition. FIX: after line `179` add: “Here `{\gAmod}^{E_1}` is the ordered modular convolution dg Lie algebra of Definition~\ref{def:e1-modular-convolution}, `\Theta_\cA^{E_1}\in\MC({\gAmod}^{E_1})` is Theorem~\ref{thm:e1-mc-element}, and `\operatorname{av}(\Theta_\cA^{E_1})=\Theta_\cA` by \eqref{eq:e1-to-einfty-projection}.”

- [HIGH] `chapters/theory/higher_genus_modular_koszul.tex:450` — PROBLEM: this file references `thm:universal-MC`, but the local theorem is `thm:universal-theta` at `3575-3604`. The label `thm:universal-MC` lives outside the theory chapter in `chapters/connections/concordance.tex:5344-5360` and is also duplicated as a phantom label in `main.tex:1746`. The reference is therefore an unstable external alias, not a local theorem anchor. FIX: replace every in-file `\ref{thm:universal-MC}` with `\ref{thm:universal-theta}`; then delete the duplicate phantom label `\label{thm:universal-MC}` from `main.tex:1746` so the theorem label exists exactly once on an actual theorem surface.

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:12284` — PROBLEM: the shadow-tower definition identifies the truncation with a scalar, `\Theta_\cA^{\le2}=\kappa(\cA)`, even though the same file later gives the actual degree-2 truncation as `\Theta_\cA^{\le2}=\kappa\cdot\eta\otimes\Lambda` at `29803-29805`. A Maurer--Cartan truncation is not literally a scalar. FIX: replace `12284-12285` with “`\pi_2(\Theta_\cA^{\le2})=\kappa(\cA)`; more explicitly, on the scalar lane `\Theta_\cA^{\le2}=\kappa(\cA)\,\eta\otimes\Lambda`.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:449` — PROBLEM: Definition~\ref{def:modular-koszul-homotopy} makes the Maurer--Cartan datum optional by writing “and (when constructed) a genus-completed Maurer--Cartan datum `\Theta_\cA`.” A foundational definition cannot hide a core datum behind an optional parenthesis and then rely on it later as if it were part of the structure. FIX: remove the optional clause from Data item D3 and move the MC datum to the consequence list, e.g. add after MK5: “When Theorem~\ref{thm:universal-theta} applies, the object carries a canonical genus-completed Maurer--Cartan class `\Theta_\cA`.”

- [MEDIUM] `chapters/theory/higher_genus_modular_koszul.tex:2648` — PROBLEM: the full modular package says Theorem~\ref{thm:mc2-bar-intrinsic} gives the universal MC class “in particular, for every such `\cA` with simple Lie symmetry,” but Theorem~\ref{thm:mc2-bar-intrinsic} as stated at `3779-3780` assumes only a modular Koszul chiral algebra with non-degenerate invariant form. The prose falsely narrows the theorem’s scope. FIX: delete “with simple Lie symmetry” from `2650-2651`; if a narrower corollary is intended, cite that corollary instead of the full theorem.

## Summary
Checked: 11 | Findings: 10 | Verdict: FAIL
tokens used
162,472
