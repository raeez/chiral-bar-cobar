# F08_prerequisites_thm_D (852s)

- [CRITICAL] chapters/theory/higher_genus_foundations.tex:5380-5405 — PROBLEM: The proof of `thm:genus-universality` jumps from “one-variable recursion”, “same propagator”, and “same Hodge bundle” to `\Gamma_{\cA,g}=\kappa(\cA)\lambda_g` for all `g`, but no cited result proves that those hypotheses uniquely force the `\lambda_g` class. The same file later states at 5730-5776 that scalar saturation does not determine which genus-`g` class appears. FIX: split the theorem now. Keep only the proved genus-1 statement `\mathrm{obs}_1(\cA)=\kappa(\cA)\lambda_1`; move the all-genera factorization to a conjecture/conditional theorem until a separate clutching-uniqueness proposition is actually proved and cited at 5394-5405.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:2659-2696,2729-2738 — PROBLEM: Theorem D is tagged `\ClaimStatusProvedHere`, but parts (i) and (ii) are only as strong as `thm:genus-universality`; once the all-genera proof above fails, the flagship theorem is overstated on its main uniform-weight lane. FIX: rewrite Theorem D so the unconditional claim is genus-1 only, or mark parts (i)(a) and (ii) as conditional pending the missing universality proof; then propagate that narrower status to concordance and guide surfaces that currently advertise Theorem D as fully proved.

- [CRITICAL] chapters/connections/concordance.tex:5939-5947,6017-6025 — PROBLEM: `thm:family-index` defines `\mathcal D_{\cA}^{(g)}:=\kappa(\cA)\cdot\mathbb E` as a `K_0`-class, i.e. “`\kappa` copies of the Hodge bundle”, and then claims the top Chern class determines that `K`-class uniquely. Neither step is justified: a complex scalar is not a bundle multiplicity in `K_0`, and a top Chern class does not uniquely determine a `K`-theory class. FIX: delete the definition of `\mathcal D_{\cA}^{(g)}` and restate the theorem only as the scalar GRR/Faber-Pandharipande identity `F_g(\cA)=\kappa(\cA)\int_{\overline{\mathcal M}_{g,1}}\psi^{2g-2}\lambda_g` plus the generating series; also remove the downstream “canonical identification” language at 6205-6218.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2741-2744 — PROBLEM: The proof of Theorem D cites `thm:anomaly-koszul` for general additivity, but `thm:anomaly-koszul` is explicitly about the matter-ghost system and itself imports additivity from `cor:kappa-additivity`. The dependency is backwards. FIX: replace line 2741 with `Part~(iv) is Corollary~\ref{cor:kappa-additivity}; the anomaly-cancellation specialization is Theorem~\ref{thm:anomaly-koszul}.`

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2703-2716; chapters/theory/higher_genus_foundations.tex:5425-5429 — PROBLEM: The duality clause overclaims scope. The theorem text says “affine Kac--Moody and free-field algebras”, but the cited proof only covers affine KM plus a `\mathcal W` formula; for the `\mathcal W` part it cites `thm:wn-obstruction`, which is only the principal `\mathcal W_N=\mathcal W(\mathfrak{sl}_N)` theorem, not the general `\mathcal W(\mathfrak g)` statement used in the text. The sentence `\kappa=0` iff critical level is unscoped and contradicted by the `\mathcal W` clause itself. FIX: cite `cor:general-w-obstruction` with its generic-level hypothesis `k\neq -h^\vee`; narrow the first sentence to families actually proved; and replace line 2716 by `For affine Kac--Moody, \kappa=0 iff k=-h^\vee. For principal \mathcal W^k(\mathfrak g,f_{\mathrm{prin}}) at generic level, \kappa=0 iff c=0.`

- [HIGH] chapters/examples/genus_expansions.tex:1913-1927 — PROBLEM: `thm:universal-generating-function` is marked `\ClaimStatusProvedHere`, but its proof is only `By Theorem~\ref{thm:genus-universality}(iii)...`. If the all-genera scalar factorization is unsupported, this theorem is unsupported too. FIX: downgrade the theorem to the proved genus-1 statement `F_1=\kappa/24` with an explicit conditional all-genera clause, or supply an independent proof from a separately proved all-genera factorization and the Bernoulli series identity.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:514-633 — PROBLEM: `prop:genus-g-curvature-package` is tagged `\ClaimStatusProvedHere`, but part (iv) is not proved there; the proof simply forwards to `thm:genus-universality` and `thm:family-index`. That makes an early “package” proposition advertise as locally proved what is actually deferred. FIX: split off part (iv) into a later corollary after the universality/GRR results, or keep only parts (i)-(iii) in this proposition and mark the scalar-package summary as proved elsewhere or conditional.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:5893-5894 — PROBLEM: `cor:kappa-additivity` proves additivity of `\kappa` by invoking `thm:genus-universality`, even though the actual argument only needs genus-1 curvature. This creates an unnecessary hidden dependence on the broken all-genera theorem. FIX: rewrite the proof to stop after the genus-1 argument for `\kappa(\mathcal A\otimes\mathcal B)=\kappa(\mathcal A)+\kappa(\mathcal B)`; keep the `\mathrm{obs}_g` sentence only as a corollary on the repaired scalar lane.

- [LOW] chapters/theory/higher_genus_foundations.tex:5312,594,4541,4545 — PROBLEM: Raw `\textup{(LOCAL)}` markers remain inside theorem/proposition statements on the exact proof surface being cited. These are unresolved drafting artifacts, not mathematical scope. FIX: delete each marker and replace it with an explicit scope sentence only where a real restriction is intended.

- [LOW] chapters/theory/higher_genus_foundations.tex:4559-4560 — PROBLEM: The provenance note for `thm:mumford-formula` says the claim is “proved in `\cite{Mumford83}`”, but the theorem title cites `FP03` and the concordance proof at chapters/connections/concordance.tex:6097-6098 says Mumford initiated the theory and Faber--Pandharipande completed the evaluation. The manuscript is internally inconsistent about the source of the imported theorem. FIX: change 4559-4560 to `This claim is used here as an external theorem, proved in \cite{FP03}, building on Mumford’s GRR framework \cite{Mumford83}.`

Circularity check: no live 2-cycle remains. chapters/theory/higher_genus_foundations.tex:5403-5405 explicitly says `thm:genus-universality` does not invoke `thm:family-index`, while chapters/connections/concordance.tex:6010-6025 makes `thm:family-index` depend on `thm:genus-universality`. The failure is a proof gap plus downstream status inflation, not a current circular citation.

## Summary
Checked: 10 | Findings: 10 | Verdict: FAIL


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
session id: 019d83e2-80cb-7532-aa0b-07b349db8522
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

For Theorem D: trace the FULL proof chain. Start from obs_g = kappa*lambda_g. What is cited? Is each cited result proved? Is there circularity (thm:genus-universality <-> thm:family-index)?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers

thinking
**Examining audit for Theorem D**

I see the user wants to check the exhaust audit surface, especially focusing on Theorem D. It seems important to look at surrounding references and cited theorems in other files. I'll need to find the label for Theorem D in the target file and trace citations recursively, which could take some time. It’s also essential to read the target file along with the definitions and theorems it cites to identify any issues precisely. A targeted LaTeX compile might be necessary for unresolved references.
codex
Using `deep-beilinson-audit` for the theorem-chain audit and likely `claim-surface-sync` if the proof/status surface drifts. I’m starting by reading the live theorem surface, its labels, and the cited dependencies before I make any claims.

thinking
**Opening skill files**

I need to access and read the relevant skill files. This is straightforward, but I want to ensure I'm opening the right ones. I’ll check through the options to find what I need. It's all about making sure I have the correct information to work with and avoiding any confusion. Alright, let’s get started on this task and see what skills I can pull up for review!
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 490ms:
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

 succeeded in 566ms:
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

 succeeded in 577ms:
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
**Planning file operations**

I need to load necessary files and might consider using parallel execution to locate target theorem labels. The developer suggests that I use the explorer for all codebase questions, which makes me think I should spawn an explorer agent for tracing dependencies. However, I can also read the files myself, but maybe starting with the explorer is the better approach. It's important to note that I shouldn't delegate parallel tasks unless the user explicitly asks for that. So, I’ll focus on executing commands to read the required files and find the theorem labels.
codex
I’ve loaded the audit workflow. Next I’m mapping the theorem surface: the target chapter, the concordance/registry entries for Theorem D, and every label the proof chain points to.
exec
/bin/zsh -lc 'rg -n "Theorem D|thm:genus-universality|thm:family-index|obs_g|lambda_g|higher_genus_modular_koszul" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 323ms:
chapters/theory/higher_genus_modular_koszul.tex:488:$\mathrm{obs}_g = \kappa(\cA) \cdot \lambda_g$ for
chapters/theory/higher_genus_modular_koszul.tex:490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
chapters/theory/higher_genus_modular_koszul.tex:2436: (Theorem~\ref{thm:genus-universality}).
chapters/theory/higher_genus_modular_koszul.tex:2541:On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
chapters/theory/higher_genus_modular_koszul.tex:2543:(Theorem~\ref{thm:genus-universality}).
chapters/theory/higher_genus_modular_koszul.tex:2597: \sum_{g \geq 1} \kappa(\cA)\lambda_g,
chapters/theory/higher_genus_modular_koszul.tex:2678: $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
chapters/theory/higher_genus_modular_koszul.tex:2729:Theorem~\ref{thm:genus-universality} identifies that trace with
chapters/theory/higher_genus_modular_koszul.tex:2730:$\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
chapters/theory/higher_genus_modular_koszul.tex:2732:Part~(i) is Theorem~\ref{thm:genus-universality} for
chapters/theory/higher_genus_modular_koszul.tex:2740:Theorem~\ref{thm:genus-universality}(ii).
chapters/theory/higher_genus_modular_koszul.tex:2749:\index{Lagrangian self-intersection!Theorem D}
chapters/theory/higher_genus_modular_koszul.tex:2797:\mathrm{obs}_g=\kappa\cdot\lambda_g
chapters/theory/higher_genus_modular_koszul.tex:2804:Theorem~\ref{thm:genus-universality}; the second arrow is the
chapters/theory/higher_genus_modular_koszul.tex:2806:series. In particular, Theorem~\ref{thm:family-index} is downstream of
chapters/theory/higher_genus_modular_koszul.tex:2809:$\mathrm{obs}_g=\kappa\cdot\lambda_g$ (uniform-weight;
chapters/theory/higher_genus_modular_koszul.tex:2811:Theorem~\ref{thm:genus-universality}); generating function via
chapters/theory/higher_genus_modular_koszul.tex:2816:to $\kappa\cdot(\hat{A}(ix)-1)$ (Theorem~\ref{thm:family-index}).
chapters/theory/higher_genus_modular_koszul.tex:2844:\lambda_g^{\mathrm{FP}}
chapters/theory/higher_genus_modular_koszul.tex:2849:F_g(\cA) = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}.
 succeeded in 379ms:
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
 succeeded in 413ms:
     1	# Theorem Registry
     2	
     3	Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.
     4	
     5	This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.
     6	
     7	## Snapshot
     8	
     9	| Metric | Value |
    10	|---|---:|
    11	| ProvedHere claims | 2809 |
    12	| Total tagged claims | 3615 |
    13	| Active files in `main.tex` | 85 |
    14	| Total `.tex` files scanned | 128 |
    15	
    16	## Status Totals
    17	
    18	| Status | Count |
    19	|---|---:|
    20	| `ProvedHere` | 2809 |
 succeeded in 755ms:
     1	\chapter{Concordance with primary literature}
     2	\label{chap:concordance}
     3	
     4	\index{concordance|textbf}
     5	
     6	This chapter is the constitution of the monograph. When chapters
     7	disagree, this chapter governs. It records the five main theorems
     8	with their precise status and locates every result against the
     9	prior literature: what is proved, what is conditional, what
    10	remains conjectural.
    11	
    12	The governing principle is falsification: every claim in these three
    13	volumes is presumed false until it appears below with an explicit
    14	status tag and a proof reference or independent verification trail.
    15	A theorem that contradicts the concordance is not a theorem; it is an
    16	error in the chapter that states it. Omission from this chapter is
    17	itself a verdict: what is not recorded here has not survived scrutiny.
    18	The concordance does not summarize the monograph; the monograph
    19	approximates the concordance.
    20	

thinking
**Analyzing proof requirements**

I realize we need to focus more on Theorem D and family-index, specifically around lines 5243 and 5769. It seems important to check related definitions and ensure we have a solid proof chain throughout. I might need to use the rg tool for labeling and to open up relevant contexts. It would help to read the cited dependencies as well, such as scalar lane definitions. Compiling references could be helpful, so I’ll search within the file around theorem labels.
codex
The chapter is huge and Theorem D is referenced all over it. I’m narrowing to the canonical statement, its proof, the scalar-lane definition it depends on, and the exact imported results used in the proof chain.
exec
/bin/zsh -lc "rg -n \"label\\{thm:genus-universality\\}|label\\{thm:family-index\\}|label\\{def:scalar-lane\\}|label\\{thm:theorem-d-roadmap\\}|label\\{prop:scalar-lane-trace\\}|label\\{prop:lambda-generator-uniqueness\\}|label\\{prop:normalized-clutching-functional\\}|label\\{prop:universal-trace-map\\}|label\\{prop:obstruction-space-one-dimensional\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5380,5485p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5160,5865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5900,6245p'" in /Users/raeez/chiral-bar-cobar succeeded in 274ms:
  5900	\emph{Duality.}
  5901	$\Delta_{\cA^!}(x)=\Delta_\cA(x)$ for all Koszul pairs:
  5902	the spectral discriminant is self-dual. For
  5903	$\widehat{\mathfrak{sl}}_2$: the zero at $1/k$ corresponds
  5904	to level~$k$; the zero at $1/(k{+}4)$ corresponds to the
  5905	dual level $-k-4$. The product of the two zeros is
  5906	$1/(k(k{+}4))$; their sum is $(2k{+}4)/(k(k{+}4))=2/k+2/(k{+}4)
  5907	\to 0$ as $k\to\infty$.
  5908	
  5909	\emph{Rank.}
  5910	$\operatorname{rank}(\Delta_\cA)
  5911	=\deg\Delta_\cA
  5912	=\dim H^1_{\mathrm{cyc,prim}}(\cA)$: the number of independent
  5913	genus-$1$ deformation directions. Rank~$1$ for algebras with
  5914	one-dimensional deformation space (Heisenberg, Virasoro,
  5915	$\beta\gamma$); rank~$2$ for $\widehat{\mathfrak{sl}}_2$ and
  5916	$\mathcal W_3$.
  5917	\end{computation}
  5918	
  5919	\subsection{The index theorem for genus expansions}
 succeeded in 299ms:
2527:\label{def:scalar-lane}
 succeeded in 586ms:
  5380	MC2-2 conditionally on MC2-1 via the Getzler--Kapranov Feynman
  5381	transform: clutching is built into the dg~Lie structure
  5382	of $\Gmod$. MC2-1 is resolved by
  5383	Theorem~\ref{thm:cyclic-linf-graph}. The remaining MC2-3
  5384	scalar-trace input is unconditional only at genus~$1$ and is
  5385	proved at all genera on the uniform-weight lane
  5386	(Theorem~\ref{thm:genus-universality},
  5387	Theorem~\ref{thm:tautological-line-support}); for
  5388	general multi-weight algebras the scalar formula receives the
  5389	cross-channel correction at $g \geq 2$
  5390	\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)},
  5391	while all free-field algebras remain
  5392	exact by Proposition~\ref{prop:free-field-scalar-exact}.
  5393	\end{remark}
  5394	
  5395	\begin{proposition}[Tautological-line support criterion;
  5396	\ClaimStatusProvedHere]\label{prop:tautological-line-support-criterion}
  5397	\index{MC2!tautological-line support criterion}
  5398	In the setting of
  5399	Proposition~\textup{\ref{prop:mc2-reduction-principle}}, fix genus~$g$
 succeeded in 660ms:
  5160	\index{MC2!reduction principle}
  5161	Let $\cA$ be a modular Koszul chiral algebra. Assume that the
  5162	bar-intrinsic complex $\Defcyc(\cA)$ of
  5163	Definition~\ref{def:cyclic-deformation-bar} exists as a complete cyclic
  5164	$L_\infty$-algebra, and let $\{W_g\}_{g \geq 0}$ be finite-dimensional
  5165	coefficient spaces chosen from
  5166	$R\Gamma(\overline{\mathcal{M}}_{g,\bullet}, \mathbb{Q})$ for the
  5167	modular-operadic package of
  5168	Theorem~\ref{thm:universal-theta}. Then:
  5169	\begin{enumerate}[label=\textup{(\roman*)}]
  5170	\item the universal Maurer--Cartan problem for $\Theta_{\cA}$ is posed
  5171	 on the genus-completed convolution algebra
  5172	 $\widehat{L}_W = \prod_{g \geq 0}\Defcyc(\cA)\otimes W_g$, and its
  5173	 genus-$g$ equation is a finite sum;
  5174	\item extending a partial solution through genus~$g-1$ to genus~$g$ is
  5175	 obstructed by a class in
  5176	 $H^2(\Defcyc(\cA), l_1) \otimes W_g$;
  5177	\item if $H^2(\Defcyc(\cA), l_1) \cong \mathbb{C}$, then the
  5178	 genus-$g$ extension problem has a single obstruction channel valued
  5179	 in~$W_g$.

thinking
**Searching for theorem details**

I need to find the theorem statement and proof for genus-universality. I'm thinking about searching around line 5243 in the registry. Actually, I should also look near lines 2480-2850. I've noticed the definition of a scalar-lane at line 2527, so it might be beneficial to explore the context around those lines. Let’s open the text around 2480-2850 to see the theorem and roadmap related to it.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2480,2865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:genus-universality|prop:lambda-generator|prop:normalized-trace|prop:clutching|prop:family-index|prop:free-energy-ahat|cor:free-energy-ahat|thm:mumford-formula|thm:universal-generating-function|thm:tautological-line-support|thm:multi-weight-genus-expansion|prop:free-field-scalar-exact" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3320,3465p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4300,4475p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2480	 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
  2481	 \bigr);
  2482	 \]
  2483	\item $\kappa(\cA) \in \mathbb{C}$ is the
  2484	 \emph{scalar modular characteristic}
  2485	 (Definition~\ref{def:scalar-modular-package}),
  2486	 the first characteristic number of~$\Theta_{\cA}$
  2487	 under the trace map
  2488	 $\Defcyc(\cA) \to \mathbb{C}$;
  2489	\item $\Delta_{\cA}(x) = \prod_{i}(1 - \lambda_i x)$ is the
  2490	 \emph{spectral discriminant}
  2491	 (Theorem~\ref{thm:ds-bar-gf-discriminant});
  2492	\item $\Pi_{\cA} = (M_{\cA}, Q_{\cA}, G_{\cA})$ is the
  2493	 \emph{periodicity profile}
  2494	 (Remark~\ref{rem:periodicity-triple});
  2495	\item $\mathcal{H}_{\cA} := \{C_g(\cA)\}_{g \geq 0}$ is the
  2496	 \emph{ambient modular deformation family}, the genus-graded
  2497	 system of curved deformation complexes.
  2498	\end{enumerate}
  2499	
 succeeded in 50ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2436: (Theorem~\ref{thm:genus-universality}).
2439: (Theorem~\ref{thm:universal-generating-function}).
2543:(Theorem~\ref{thm:genus-universality}).
2547:Theorem~\ref{thm:multi-weight-genus-expansion}; all free-field algebras are exact exceptions by
2548:Proposition~\ref{prop:free-field-scalar-exact}.
2729:Theorem~\ref{thm:genus-universality} identifies that trace with
2732:Part~(i) is Theorem~\ref{thm:genus-universality} for
2738:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
2740:Theorem~\ref{thm:genus-universality}(ii).
2804:Theorem~\ref{thm:genus-universality}; the second arrow is the
2811:Theorem~\ref{thm:genus-universality}); generating function via
2812:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
2823:\label{cor:free-energy-ahat-genus}
2881:Theorem~\ref{thm:universal-generating-function}.
2919:of Corollary~\ref{cor:free-energy-ahat-genus} is the
2940:Corollary~\ref{cor:free-energy-ahat-genus}: the left-hand side
3184:Theorem~\ref{thm:genus-universality}. The GUE free energy
3345:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3768:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
 succeeded in 52ms:
  3320	 the full scalar trace is
  3321	 $\operatorname{tr}(\Theta_{\cA})
  3322	 = \sum_{g \geq 1} \kappa(\cA) \lambda_g$;
  3323	\item it is compatible with clutching morphisms of stable curves;
  3324	\item under Verdier/Koszul duality, $\Theta_{\cA}$ is sent to
  3325	 $\Theta_{\cA^!}$.
  3326	\end{enumerate}
  3327	This is Theorem~\ref{thm:master-theta} (MC2).
  3328	\end{theorem}
  3329	
  3330	\begin{proof}
  3331	\emph{Bar-intrinsic construction.}
  3332	The genus-completed bar differential
  3333	$D_\cA = \dzero + \sum_{g \geq 1} \hbar^g d_\cA^{(g)}$
  3334	exists by the modular operad structure of the bar complex
  3335	(Theorem~\ref{thm:bar-modular-operad}), and satisfies
  3336	$D_\cA^2 = 0$
  3337	(Theorem~\ref{thm:bar-modular-operad}(iii)).
  3338	Define $\Theta_\cA := D_\cA - \dzero$. Since
  3339	$\dzero^2 = 0$ and $D_\cA^2 = 0$, expanding
 succeeded in 60ms:
  4300	 \kappa(\cA) \cdot \eta \otimes \Lambda,
  4301	 \qquad
  4302	 \Lambda := \sum_{g \geq 1} \lambda_g \;\in\; \Gmod,
  4303	 \end{equation}
  4304	 where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  4305	 Hodge bundle on~$\overline{\mathcal{M}}_g$.
  4306	
  4307	\item \emph{MC equation is trivially satisfied.}
  4308	 In the minimal model, $l_1^{\mathrm{tr}} = 0$ and all genus-$g$
  4309	 components of $\Theta^{\min}$ lie in $\mathbb{C}\!\cdot\!\eta$.
  4310	 The obstructions vanish at every degree $n \geq 2$ by
  4311	 graded antisymmetry of $L_\infty$-operations: in the
  4312	 desuspension $s^{-1}\mathcal{H}$, the class
  4313	 $s^{-1}\eta$ has degree~$1$ \textup{(}odd\textup{)}, so
  4314	 $l_n^{\mathrm{tr}}(\eta, \ldots, \eta) = 0$ for $n \geq 2$
  4315	 since permuting two identical odd-degree entries
  4316	 in the bar coalgebra $T^c(s^{-1}\mathcal{H})$ introduces
  4317	 a sign $(-1)$.
  4318	 This argument uses \emph{only} the one-dimensionality
  4319	 of $\mathcal{H}^2$ and the parity of $s^{-1}\eta$, not the
exec
/bin/zsh -lc "rg -n \"label\\{thm:genus-universality\\}|Genus universality|tautological support theorem|tautological line support\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
9580:\index{MC2!tautological line support}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9520,9725p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7680,7865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7900,8125p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
  9520	\index{scalar saturation!structural origin}
  9521	\index{modular characteristic!K-theoretic hierarchy}
  9522	\index{determinant line bundle!and scalar saturation}
  9523	The virtual bar family
  9524	\begin{equation}\label{eq:virtual-bar-family}
  9525	\mathcal{V}_{\cA}
  9526	\;:=\;
  9527	[R\pi_{g*} \bar{B}^{(g)}(\cA)]
  9528	\;\in\; K_0(\overline{\mathcal{M}}_g)
  9529	\end{equation}
  9530	explains both scalar saturation and the non-scalar hierarchy.
  9531	The MC class~$\Theta_{\cA}$ inhabits a rank-one object
  9532	($H^2_{\mathrm{cyc}} = \mathbb{C}\cdot\eta$), so its only
  9533	characteristic number is $\kappa = c_1(\det\mathcal{V}_{\cA})$.
  9534	The non-scalar invariants $\Delta_{\cA}$ and $\Pi_{\cA}$ arise
  9535	from the level direction (monodromy of bar cohomology around the
  9536	critical level), which sees the full bundle~$\mathcal{V}_{\cA}$:
  9537	
  9538	\begin{center}\renewcommand{\arraystretch}{1.3}
  9539	\begin{tabular}{@{}lll@{}}
 succeeded in 51ms:
  7680	\;=\;
  7681	c_g(\cA)\ell_g(\tau_g)
  7682	\;=\;
  7683	c_g(\cA),
  7684	\]
  7685	which is part~\textup{(ii)}.
  7686	Part~\textup{(iii)} is immediate: under the line-support hypothesis,
  7687	the coefficient of $\tau_g$ is uniquely determined by
  7688	$\ell_g(o_g(\cA))$, so requiring
  7689	$o_g(\cA)=\kappa(\cA)\tau_g$ is exactly the same as requiring
  7690	$\ell_g(o_g(\cA))=\kappa(\cA)$.
  7691	\end{proof}
  7692	
  7693	\begin{remark}[Reduction consequence for MC2]
  7694	\label{rem:mc2-reduction-consequence}
  7695	Proposition~\ref{prop:mc2-reduction-principle} turns MC2 into a
  7696	three-package extension problem:
  7697	(1)~construct the cyclic $L_\infty$ model $\Defcyc(\cA)$;
  7698	(2)~realize the modular-operadic clutching package over
  7699	$\overline{\mathcal{M}}_{g,\bullet}$;
 succeeded in 52ms:
  7900	$\dim H^2_{\mathrm{cyc}}(\cA,\cA) = 1$, the universal MC element
  7901	has minimal projection concentrated on a single cyclic line:
  7902	\[
  7903	\Theta_{\cA}^{\min} = \eta \otimes \Gamma_{\cA}
  7904	\qquad
  7905	\text{for a unique }\Gamma_{\cA}\in\widehat{\Gmod}.
  7906	\]
  7907	On the proved uniform-weight lane one further has
  7908	\[
  7909	\Gamma_{\cA} = \kappa(\cA)\Lambda,
  7910	\qquad
  7911	\Theta_{\cA}^{\min}
  7912	= \kappa(\cA) \cdot \eta \otimes \Lambda.
  7913	\]
  7914	In particular, one-channelity alone does not force the full
  7915	universal MC class to be determined by~$\kappa$.
  7916	The hypothesis $\dim H^2_{\mathrm{cyc}} = 1$ is established
  7917	for Kac--Moody algebras
  7918	\textup{(}Theorem~\textup{\ref{thm:mc2-1-km}}\textup{(ii)}\textup{)},
  7919	at all non-admissible, non-critical levels

thinking
**Searching for theorem details**

I need to find details about the theorem labeled "thm:genus-universality," possibly around the reference number 11700. It seems like there might be a connection to registry line 5243, which could correspond to a specific file line. However, it’s odd that my search didn’t return the label. Maybe it’s hidden or split in some way. I think I should search more thoroughly to uncover the exact label.
codex
I have the downstream proof surfaces. Now I’m locating the canonical Theorem D statement itself and reading its proof, not just the places that cite it, because several later “proofs” appear to lean on it as a black box.
exec
/bin/zsh -lc 'rg -n -C 3 "genus universality|genus-universality|Genus universality" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'BEGIN{p=0} /thm:genus-universality/{p=1} p{print NR \":\" "'$0; if (++c>220) exit}'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:genus-universality\\)|thm:genus-universality\\}|Theorem D|modular characteristic theorem|Genus universality theorem|universal-generating-function\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
487-of~$\mathbf{B}_X(\cA)$, whose scalar shadow is
488-$\mathrm{obs}_g = \kappa(\cA) \cdot \lambda_g$ for
489-uniform-weight algebras
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
491-genus-$1$ identity $\mathrm{obs}_1 = \kappa(\cA) \cdot \lambda_1$ is
492-unconditional.
493-\end{enumerate}
--
2433-\item The \emph{obstruction invariant}
2434- $\kappa(\cA) \in \mathbb{C}$, the scalar controlling genus-$1$
2435- fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
2436: (Theorem~\ref{thm:genus-universality}).
2437-\item The \emph{genus tower} $\{F_g(\cA)\}_{g \geq 1}$, the sequence
2438- of free energies determined by the bar complex at genus~$g$
2439- (Theorem~\ref{thm:universal-generating-function}).
--
2540-
2541-On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
2542-is proved at all genera
2543:(Theorem~\ref{thm:genus-universality}).
 succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2436: (Theorem~\ref{thm:genus-universality}).
2439: (Theorem~\ref{thm:universal-generating-function}).
2543:(Theorem~\ref{thm:genus-universality}).
2661:\index{modular characteristic theorem|textbf}
2729:Theorem~\ref{thm:genus-universality} identifies that trace with
2732:Part~(i) is Theorem~\ref{thm:genus-universality} for
2738:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
2740:Theorem~\ref{thm:genus-universality}(ii).
2749:\index{Lagrangian self-intersection!Theorem D}
2761:\index{modular characteristic theorem!as integrability condition}%
2793:\index{modular characteristic theorem!model presentation}
2804:Theorem~\ref{thm:genus-universality}; the second arrow is the
2811:Theorem~\ref{thm:genus-universality}); generating function via
2812:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
2881:Theorem~\ref{thm:universal-generating-function}.
3184:Theorem~\ref{thm:genus-universality}. The GUE free energy
3345:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3768:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3820:Theorem~\ref{thm:genus-universality}(ii)).
 succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
491:genus-$1$ identity $\mathrm{obs}_1 = \kappa(\cA) \cdot \lambda_1$ is
492:unconditional.
493:\end{enumerate}
494:
495:\noindent The following are \emph{consequences} of the axioms above,
496:proved by the main theorems:
497:\begin{enumerate}[label=\textup{(MK\arabic*$_\infty$)},start=4]
498:\item\label{MK:inversion-htpy}
499:\emph{(Bar-cobar inversion; Theorem~\textup{\ref{thm:higher-genus-inversion}}.)}
500:$\boldsymbol{\Omega}_X \mathbf{B}_X(\cA) \simeq \cA$
501:on the Koszul locus in
502:$\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))$.
503:
504:\item\label{MK:complementarity-htpy}
505:\emph{(Lagrangian complementarity; Theorem~\textup{\ref{thm:quantum-complementarity-main}}.)}
506:The complementarity complex
507:$\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})$
508:decomposes as
509:$\mathbf{C}_g \simeq \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$,

thinking
**Investigating metadata confusion**

I’m looking at metadata line 5243, and there might be some confusion because line numbers could have shifted or become stale. It specifically mentions the label `thm:genus-universality`, but that might be gone now if the current file has changed. I need to verify if there's an unresolved reference, which could be major. Before jumping to conclusions, I'll read the actual file contents and possibly use a `grep` command to search the whole repository.
codex
The canonical label may itself be broken. I’m checking whether `thm:genus-universality` is actually defined anywhere in the repo or whether the chapter is citing a theorem label that does not exist in live source.
exec
/bin/zsh -lc "rg -n \"\\\\label\\s*\\{thm:genus-universality\\}\" ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "genus-universality" .' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:family-index" .' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\label\s*\{thm:genus-universality\})
       ^^
error: unrecognized escape sequence
 succeeded in 66ms:
./audit_campaign_20260412_231034/T06_thm_D.md:3:- [CRITICAL] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2695) — Theorem D is not proved end-to-end as written. Its proof imports `thm:genus-universality`, but the load-bearing step there, [higher_genus_foundations.tex:5326](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5326), invokes `thm:family-index` to identify `\mathrm{obs}_g` with `\lambda_g`; the proof of `thm:family-index` then starts from `thm:genus-universality` at [concordance.tex:6010](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6010). This is a direct circular dependency on the main all-genera step.
./audit_campaign_20260412_231034/T06_thm_D.md:266:/bin/zsh -lc "rg -n \"thm:genus-universality|def:scalar-lane|delta F_g\\\\"'^'"\\\\{\\\\mathrm\\\\{cross\\\\}\\\\}|delta_F_g\\\\"'^cross|UNIFORM-WEIGHT|ALL-WEIGHT|genus universality|Theorem D|F_1 = '"\\\\kappa/24|F_1\\\\s*=\\\\s*\\\\kappa/24|F_1\\\\s*=\\\\s*\\\\\\\\kappa/24|lambda_g\\\\"'^'"\\\\{\\\\mathrm\\\\{FP\\\\}\\\\}|obs_g\\(|\\\\\\mathrm\\{obs\\}_g\" chapters/theory/higher_genus_modular_koszul.tex chapters/frame/guide_to_main_results.tex chapters" in /Users/raeez/chiral-bar-cobarexec
./audit_campaign_20260412_231034/T06_thm_D.md:271:    (?:thm:genus-universality|def:scalar-lane|delta F_g\^\{\mathrm\{cross\}\}|delta_F_g\^cross|UNIFORM-WEIGHT|ALL-WEIGHT|genus universality|Theorem D|F_1 = \kappa/24|F_1\s*=\s*\kappa/24|F_1\s*=\s*\\kappa/24|lambda_g\^\{\mathrm\{FP\}\}|obs_g\(|\\mathrm\{obs\}_g)
./audit_campaign_20260412_231034/T06_thm_D.md:422:/bin/zsh -lc "rg -n -F 'thm:genus-universality' chapters/theory/higher_genus_modular_koszul.tex chapters chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobarexec
./audit_campaign_20260412_231034/T06_thm_D.md:447:chapters/theory/higher_genus_modular_koszul.tex:490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
./audit_campaign_20260412_231034/T06_thm_D.md:448:chapters/theory/higher_genus_modular_koszul.tex:2404: (Theorem~\ref{thm:genus-universality}).
./audit_campaign_20260412_231034/T06_thm_D.md:449:chapters/theory/higher_genus_modular_koszul.tex:2511:(Theorem~\ref{thm:genus-universality}).
./audit_campaign_20260412_231034/T06_thm_D.md:450:chapters/theory/higher_genus_modular_koszul.tex:2695:Part~(i) is Theorem~\ref{thm:genus-universality} for
./audit_campaign_20260412_231034/T06_thm_D.md:451:chapters/theory/higher_genus_modular_koszul.tex:2703:Theorem~\ref{thm:genus-universality}(ii).
./audit_campaign_20260412_231034/T06_thm_D.md:452:chapters/theory/higher_genus_modular_koszul.tex:2760:Theorem~\ref{thm:genus-universality}); generating function via
./audit_campaign_20260412_231034/T06_thm_D.md:453:chapters/theory/higher_genus_modular_koszul.tex:3133:Theorem~\ref{thm:genus-universality}. The GUE free energy
./audit_campaign_20260412_231034/T06_thm_D.md:454:chapters/theory/higher_genus_modular_koszul.tex:3294:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
./audit_campaign_20260412_231034/T06_thm_D.md:455:chapters/theory/higher_genus_modular_koszul.tex:3688:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
./audit_campaign_20260412_231034/T06_thm_D.md:456:chapters/theory/higher_genus_modular_koszul.tex:3740:Theorem~\ref{thm:genus-universality}(ii)).
./audit_campaign_20260412_231034/T06_thm_D.md:457:chapters/theory/higher_genus_modular_koszul.tex:5306:(Theorem~\ref{thm:genus-universality},
./audit_campaign_20260412_231034/T06_thm_D.md:458:chapters/theory/higher_genus_modular_koszul.tex:7707:(Theorem~\ref{thm:genus-universality}).
./audit_campaign_20260412_231034/T06_thm_D.md:459:chapters/theory/higher_genus_modular_koszul.tex:7863:Theorem~\ref{thm:genus-universality} identifies the scalar trace
./audit_campaign_20260412_231034/T06_thm_D.md:460:chapters/theory/higher_genus_modular_koszul.tex:8011:Theorem~\ref{thm:genus-universality} identifies
./audit_campaign_20260412_231034/T06_thm_D.md:461:chapters/theory/higher_genus_modular_koszul.tex:8435:by Theorem~\ref{thm:genus-universality}\textup{(iii)}.
./audit_campaign_20260412_231034/T06_thm_D.md:462:chapters/theory/higher_genus_modular_koszul.tex:9515:Theorem~\textup{\ref{thm:genus-universality}}, then the full
 succeeded in 51ms:
Total output lines: 400

./wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:311:rectification_20260412_233715/R03_higher_genus_foundations.md:180:/bin/zsh -lc "rg -n \"thm:genus-universality|thm:family-index|cor:bar-cohomology-koszul-dual|center local system|C0|Step 3|d_fib|R\\"'^q '"\\\\pi_\\*|spectral sequence|EGA base change\" chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:312:rectification_20260412_233715/R03_higher_genus_foundations.md:183:    (?:thm:genus-universality|thm:family-index|cor:bar-cohomology-koszul-dual|center local system|C0|Step 3|d_fib|R\^q \pi_\*|spectral sequence|EGA base change)
./wave2_audit_20260413_001942/S05_foundations_to_complementarity.md:1473:  4712	Index & GRR: scalar genus series $= \kappa(\cA) \cdot (\hat{A}(ix) - 1)$; genus-$1$ unconditional & \textbf{Proved} & Thm~\ref{thm:family-index} \\[2pt]
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:1396:   660	\phantomsection\label{thm:family-index}
./main.tex:1562: % thm:family-index now defined in guide_to_main_results.tex
./metadata/dependency_graph.dot:253:  thm_family_index [label="thm:family-index\ntheorem [Pr]\nFamily index theorem for genus expansion...", style=filled, fillcolor="#c8e6c9"];
./metadata/theorem_registry.md:2369:| `thm:family-index` | `theorem` | 5769 | Family index theorem for genus expansions |
./metadata/label_index.json:46878:  "thm:family-index": {
./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:682:   660	\phantomsection\label{thm:family-index}
./chapters/examples/heisenberg_eisenstein.tex:1738:confirming Theorem~\ref{thm:family-index} directly from the shadow
./metadata/claims.jsonl:240:{"label": "thm:family-index", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5769, "title": "Family index theorem for genus expansions", "labels_in_block": ["thm:family-index", "eq:modular-deformation-complex-concordance", "eq:family-index-grr", "eq:family-index-generating"], "refs_in_block": ["thm:genus-universality"]}
./metadata/claims.jsonl:625:{"label": "prop:thqg-X-free-energy-ahat", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/thqg_fredholm_partition_functions.tex", "line": 1425, "title": "Free energy: $\\hat{A}$-genus verification", "refs_in_block": ["thm:family-index"]}
./metadata/claims.jsonl:2728:{"label": "prop:chain-level-curvature-operator", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_foundations.tex", "line": 626, "title": "Chain-level curvature operator", "labels_in_block": ["prop:chain-level-curvature-operator", "eq:chain-curvature-operator", "eq:chern-weil-step1", "eq:chern-weil-projection"], "refs_in_block": ["prop:genus-g-curvature-package", "eq:chain-curvature-operator", "thm:family-index"]}
./metadata/claims.jsonl:2803:{"label": "thm:curvature-self-contraction", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_foundations.tex", "line": 6695, "title": "Curvature from loop contraction", "labels_in_block": ["thm:curvature-self-contraction", "eq:self-contraction-trace", "eq:kappa-self-contraction", "eq:qme-genus1"], "refs_in_block": ["thm:quantum-master-equation", "thm:family-index"]}
./metadata/claims.jsonl:2845:{"label": "thm:explicit-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 4082, "title": "Explicit universal MC class", "labels_in_block": ["thm:explicit-theta", "eq:theta-minimal", "eq:theta-chain", "eq:theta-genus1", "eq:l2-vanishes", "eq:genus-g-recursion", "eq:theta-generating-function"], "refs_in_block": ["thm:mc2-1-km", "thm:cyclic-rigidity-generic", "thm:algebraic-family-rigidity", "cor:km-minimal-linf", "prop:cyclic-ce-identification", "constr:linf-from-graphs", "thm:family-index"]}
./standalone/introduction_full_survey.tex:4545:and~\ref{thm:family-index}). For a free fermion, this is the
./chapters/examples/genus_expansions.tex:169:This identification reflects the family index theorem (Theorem~\ref{thm:family-index}): $F_g$ is the GRR pushforward of the Todd class. For general $\kappa$: $\sum_g F_g x^{2g} = \kappa(\mathrm{Td}_{\mathrm{even}}(ix) - 1)$.
./chapters/examples/genus_expansions.tex:1904:index theorem (Theorem~\ref{thm:family-index}) shows that

thinking
**Auditing the theorem**

I see the target file mentions a theorem, but it looks like Theorem D is referenced while its proof refers to a theorem in a higher-level context. I need to review the entire chain, starting with both the theorem and its proof, alongside any dependencies like the genus curvature package and universality recursion. Also, could there be issues with the compute tests? The user is asking for a manuscript audit, so focusing on relevant files should be sufficient. I'll examine the higher_genus_foundations too, specifically around lines 5200-5425.
codex
The live `thm:genus-universality` is not in the target chapter at all; it lives in [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex). I’m now tracing its proof chain directly, because Theorem D in the target chapter is only as strong as that upstream proof.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5240,5425p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5368,5455p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "eq:genus-universality|prop:genus-g-curvature-package|prop:curvature-coefficient-extraction|prop:scalar-shadow-recursion|rem:genus-1-verification|cor:kappa-additivity|thm:multi-generator-universality|thm:mumford-formula|thm:universal-generating-function|thm:anomaly-koszul|thm:family-index" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5840,6185p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5240	\textup{(LOCAL)}.
  5241	\end{proof}
  5242	
  5243	\begin{remark}[Chern character reformulation]
  5244	\label{rem:chern-character-mumford}
  5245	Mumford's relation $c(\mathbb{E}) \cdot c(\mathbb{E}^\vee) = 1$
  5246	is equivalent to $\operatorname{ch}(\mathbb{E} \oplus \mathbb{E}^\vee)$ being
  5247	concentrated in degree~$0$, since $\mathbb{E} \oplus \mathbb{E}^\vee
  5248	= \mathcal{H}^1_{\mathrm{dR}}$ has trivial Chern character.
  5249	Via the Newton identities relating power sums to elementary symmetric
  5250	functions, all $\lambda$-class products are determined by the
  5251	Bernoulli-number weighted traces
  5252	$\operatorname{ch}_k(\mathbb{E}) = B_k \cdot \kappa_k / k!$
  5253	(where $\kappa_k$ are the Miller--Morita--Mumford classes),
  5254	giving the full multiplicative structure of the obstruction ring.
  5255	\end{remark}
  5256	
  5257	\begin{example}[Heisenberg case]\label{ex:heisenberg-obs-squares}
  5258	For the Heisenberg algebra with
  5259	$\operatorname{obs}_g = \kappa \cdot \lambda_g$ Theorem~\ref{thm:obstruction-nilpotent-all-genera} gives
 succeeded in 51ms:
  5368	The genus-$1$ class fixes the scalar coefficient. By definition of
  5369	$\kappa(\cA)$ from the genus-$1$ curvature and because
  5370	$H^2(\overline{\mathcal{M}}_{1,1}) \cong \mathbb{Q}\cdot\lambda_1$,
  5371	one has
  5372	\[
  5373	\mathrm{obs}_1(\cA)
  5374	\;=\;
  5375	\kappa(\cA)\cdot\lambda_1
  5376	\qquad
  5377	\textup{(g=1 only; all-weight at g=1 is unconditional)}.
  5378	\]
  5379	
  5380	On the scalar lane, the shadow obstruction tower is one-dimensional:
  5381	the scalar part of the Maurer--Cartan element has the form
  5382	$\eta \otimes \Gamma_\cA$ for a genus series
  5383	$\Gamma_\cA = \sum_{g \geq 1}\Gamma_{\cA,g}$.
  5384	The obstruction recursion
  5385	\textup{(}Construction~\textup{\ref{constr:obstruction-recursion}}\textup{)}
  5386	is therefore a one-variable recursion.
  5387	Every edge in every stable-graph contribution carries the standard
 succeeded in 52ms:
194:(Theorem~\ref{thm:family-index}).
515:\label{prop:genus-g-curvature-package}
598: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
633:(Theorem~\ref{thm:family-index}).
665: $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ \textup{(}Proposition~\textup{\ref{prop:genus-g-curvature-package}(iv))}
715:Proposition~\ref{prop:genus-g-curvature-package}(i).
798:(Proposition~\ref{prop:genus-g-curvature-package}\textup{(ii)}).
1018:Proposition~\textup{\ref{prop:genus-g-curvature-package}(ii))}:
1074:(Theorem~\ref{thm:family-index}). The scalar $\kappa(\cA)$ is the
3432:(Theorem~\ref{thm:universal-generating-function}).
4138:\textup{(Theorem~\ref{thm:universal-generating-function})}. Then the fiberwise
4181:Theorem~\ref{thm:universal-generating-function}.
4539:\label{thm:mumford-formula}
5183:Theorem~\ref{thm:multi-generator-universality}.
5306:curvature, such that \begin{equation}\label{eq:genus-universality}
5317:Theorem~\ref{thm:multi-generator-universality}.
5403:which is exactly \eqref{eq:genus-universality}. This argument uses
5405:does not invoke Theorem~\ref{thm:family-index}.
5431:(Theorem~\ref{thm:mumford-formula}).
5883:\begin{corollary}[Additivity of the obstruction coefficient; \ClaimStatusProvedHere]\label{cor:kappa-additivity}
 succeeded in 53ms:
  5840	\label{cor:anomaly-ratio}
  5841	\index{anomaly ratio|textbf}
  5842	For any $\mathcal{W}$-algebra $\mathcal{W}^k(\mathfrak{g})$, the obstruction coefficient $\kappa$ and central charge $c$ are related by
  5843	\begin{equation}\label{eq:anomaly-ratio}
  5844	\frac{\kappa(\mathcal{W}^k(\mathfrak{g}))}{c(\mathcal{W}^k(\mathfrak{g}))} = \varrho(\mathfrak{g}) := \sum_{i=1}^r \frac{1}{m_i + 1}
  5845	\end{equation}
  5846	where $m_1, \ldots, m_r$ are the exponents of $\mathfrak{g}$. The ratio $\varrho(\mathfrak{g})$ is a root-system invariant independent of the level~$k$.
  5847	
  5848	For Kac--Moody algebras $\widehat{\mathfrak{g}}_k$ (before DS reduction), $\kappa/c = (k+h^\vee)^2/(2h^\vee k)$, which depends on the level. The level-independence of $\kappa/c$ is specific to $\mathcal{W}$-algebras and reflects the DS reduction.
  5849	\end{corollary}
  5850	
  5851	\begin{proof}
  5852	From Theorem~\ref{thm:genus-universality}(ii): $\kappa = c \cdot \varrho(\mathfrak{g})$. Since $\varrho$ depends only on the exponents of $\mathfrak{g}$, it is independent of $k$.
  5853	\end{proof}
  5854	
  5855	\begin{corollary}[\texorpdfstring{$\kappa$}{kappa}-periodicity under level shift; \ClaimStatusProvedHere]
  5856	\label{cor:kappa-periodicity}
  5857	\index{obstruction coefficient!periodicity}
  5858	For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.
  5859	\end{corollary}

thinking
**Investigating theorem anomalies**

This seems important. There’s a token indicating local scope in the theorem statement at line 5312, which might be a formatting issue or an unfinished remark—definitely worth noting. 

In Part (iii), the Faber-Pandharipande formula seems to reference Theorem but only evaluates the integral. To link free energy with the integral, I might need the universal-generating-function or family-index. I’ll need to check Theorem and the proof for that universal-generating-function reference. 

I might also need to clarify the family-index reference in the proof.
codex
The direct `genus-universality <-> family-index` loop appears to have been cut in live source: the proof of `thm:genus-universality` now explicitly says it does not invoke `thm:family-index`. I’m checking whether the replacement argument is actually a proof or just a weaker slogan with missing uniqueness input.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6360,6415p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5160,5205p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3360,3465p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4515,4568p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6360	\sum_{g \geq 1}
  6361	\left(\int_{\overline{\mathcal{M}}_{g,1}}
  6362	\psi^{2g-2}\, c_g(\mathbb{E})\right) x^{2g}
  6363	\;=\;
  6364	\kappa(\cA) \cdot \Bigl(\frac{x/2}{\sin(x/2)} - 1\Bigr)
  6365	\end{equation}
  6366	is an explicit Hodge integral series, whose closed form
  6367	$(x/2)/\sin(x/2)$ is the Wick rotation of the $\hat{A}$-genus
  6368	\textup{(}Remark~\textup{\ref{rem:A-hat-genus})}. For arbitrary
  6369	modular Koszul algebras, the unconditional scalar specialization is
  6370	the genus-$1$ identity
  6371	$F_1(\cA)=\kappa(\cA)/24$
  6372	\textup{(g=1 only; all-weight at g=1 is unconditional)}.
  6373	\end{proposition}
  6374	
  6375	\begin{proof}
  6376	Equation~\eqref{eq:grr-bridge} combines
  6377	Theorem~\ref{thm:genus-universality}
  6378	($\mathrm{obs}_g = \kappa \cdot \lambda_g$ $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ ) with
  6379	the Faber--Pandharipande formula
 succeeded in 51ms:
  5160	\begin{remark}[Comparison with the dimensional argument]
  5161	\label{rem:mumford-vs-dimension}
  5162	For $g \leq 2$, Theorem~\textup{\ref{thm:obstruction-nilpotent}}
  5163	established $\lambda_g^2 = 0$ \textup{(LOCAL)} by the weaker observation that
  5164	$\mathrm{CH}^{2g}(\overline{\mathcal{M}}_g) = 0$ when
  5165	$2g > 3g - 3$, i.e., $g < 3$.
  5166	Mumford's relation is strictly stronger: it proves
  5167	$\lambda_g^2 = 0$ \textup{(LOCAL)} for \emph{all} genera, including $g = 3$
  5168	(where $\lambda_3^2 \in \mathrm{CH}^6(\overline{\mathcal{M}}_3)$
  5169	with $\dim \overline{\mathcal{M}}_3 = 6$, so the dimensional
  5170	argument fails) and all $g \geq 4$.
  5171	\end{remark}
  5172	
  5173	\begin{remark}[Multi-generator nilpotence]\label{rem:multi-generator-nilpotence}
  5174	\index{obstruction class!nilpotence!multi-generator}
  5175	For multi-generator algebras,
  5176	$\mathrm{obs}_1 = \kappa \cdot \lambda_1$
  5177	\textup{(g=1 only; all-weight at g=1 is unconditional)}
  5178	(Proposition~\ref{prop:multi-generator-obstruction}\textup{(a)}),
  5179	so $(\mathrm{obs}_1)^2 = \kappa^2 \cdot \lambda_1^2 = 0$
 succeeded in 51ms:
  3360	$\mathcal{A}_3^{(g)}
  3361	= \pi^2 \sum_{\alpha\beta}
  3362	 (\operatorname{Im}\Omega)^{-1}_{\alpha\beta}
  3363	 \omega_\alpha \wedge \bar\omega_\beta$.
  3364	Since $\omega_g = (i/2)\sum_{\alpha\beta}
  3365	(\operatorname{Im}\Omega)^{-1}_{\alpha\beta}
  3366	\omega_\alpha \wedge \bar\omega_\beta$,
  3367	we have $\sum_{\alpha\beta}(\cdots) = (2/i)\omega_g
  3368	= -2i\,\omega_g$, giving
  3369	\begin{equation}\label{eq:cross-term-result}
  3370	\mathcal{A}_3^{(g)} = -2\pi^2 i\cdot\omega_g.
  3371	\end{equation}
  3372	
  3373	\emph{Normalization reconciliation.}
  3374	The coefficient $-2\pi^2 i$ in~\eqref{eq:cross-term-result}
  3375	differs from~$2\pi i$
  3376	in~\eqref{eq:arnold-general-result-final} by a factor
  3377	of~$-\pi$. The discrepancy traces to the
  3378	precise normalization of the distributional residue and
  3379	the Cauchy kernel on a compact Riemann surface.
 succeeded in 51ms:
  4515	\begin{remark}[Provenance and citation]
  4516	This theorem is imported and treated as \ClaimStatusProvedElsewhere. Standard
  4517	descriptions of tautological generators and low-genus cohomology structure for
  4518	$\overline{\mathcal{M}}_{g,n}$ are classical in the moduli-space literature;
  4519	see~\cite{Mumford83}.
  4520	\end{remark}
  4521	
  4522	\begin{definition}[Hodge bundle]
  4523	\label{def:hodge-bundle}
  4524	\index{Hodge bundle|textbf}
  4525	The \emph{Hodge bundle} $\mathbb{E} \to \overline{\mathcal{M}}_{g,n}$ is the rank-$g$ vector bundle whose fiber over $[(\Sigma_g; p_1, \ldots, p_n)]$ is:
  4526	\begin{equation}
  4527	\mathbb{E}_{[\Sigma_g]} = H^0(\Sigma_g, \Omega^1_{\Sigma_g})
  4528	\end{equation}
  4529	the space of holomorphic differentials.
  4530	
  4531	The Chern classes:
  4532	\begin{equation}
  4533	\lambda_i = c_i(\mathbb{E}) \in H^{2i}(\overline{\mathcal{M}}_{g,n}, \mathbb{Q})
  4534	\end{equation}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '500,820p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2460,2585p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"constr:obstruction-recursion|rem:propagator-weight-universality|prop:multi-generator-obstruction|thm:heisenberg-obs|thm:kac-moody-obs|thm:vir-genus1-curvature|thm:wn-obstruction\" chapters/theory/higher_genus_foundations.tex chapters/examples -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1000,1115p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   500	H^1(\Sigma_g, \C)
   501	\;\xrightarrow{\;\text{MC}\;}
   502	Z^1(\operatorname{Def}_{\mathrm{cyc}}(\cA)_{\mathrm{model}})
   503	\;\xrightarrow{\;\text{global}\;}
   504	R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})
   505	\;\xrightarrow{\;\mathrm{tr}\;}
   506	R\Gamma(\overline{\mathcal{M}}_g, \mathbb{Q}).
   507	\]
   508	Fiber-period parameters live in $H^1(\Sigma_g,\C)$, not on moduli
   509	($H^1(\mathcal{M}_g,\mathbb{Q})=0$ for $g\geq 2$ by Harer).
   510	They become moduli classes via the Kodaira--Spencer map
   511	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
   512	\end{remark}
   513	
   514	\begin{proposition}[The genus-$g$ curvature package; \ClaimStatusProvedHere]
   515	\label{prop:genus-g-curvature-package}
   516	\index{curvature package!genus-g@genus-$g$|textbf}
   517	Let $\cA$ be a cyclic chiral algebra on a smooth projective
   518	curve~$X$ of genus~$g \geq 1$, and let
   519	$\{\omega_1,\ldots,\omega_g\}$ be the normalized abelian
 succeeded in 52ms:
  2460	\[\langle T(z) T(w) \rangle_2 = \frac{c/2}{(z-w)^4} + f(\Omega) + O(z-w)\]
  2461	where $f(\Omega) = c \cdot E_4(\Omega) + \cdots$ is a regular function encoding the
  2462	genus~2 geometry. In the bar complex, these corrections contribute to the
  2463	curvature $m_0^{(2)}$ and to the higher operations $m_k^{(2)}$.
  2464	
  2465	\subsubsection{\texorpdfstring{$W$-algebras at genus 2}{$\mathcal{W}$-algebras at genus 2}}
  2466	
  2467	Following Arakawa's theory, the genus-$g$ correlation functions of a
  2468	$W$-algebra with generators $W^{(k)}$ of weight~$k$ involve Siegel modular
  2469	forms $C_j^{(k)}(\Omega)$ depending on the period matrix $\Omega \in \mathcal{H}_g$.
  2470	The OPE singularity structure (pole orders $\leq 2k$) remains genus-independent,
  2471	but the correlation functions' regular parts depend on $\Omega$.
  2472	
  2473	The \emph{pattern}: genus $g$ introduces Siegel modular forms of weight
  2474	$\leq g(g+1)/2$, matching the dimension of the Siegel upper half-space
  2475	$\mathcal{H}_g$ (not $\mathcal{M}_g$, whose dimension is $3g-3$; these coincide
  2476	for $g \leq 3$ but differ for $g \geq 4$ due to the Schottky problem).
  2477	
  2478	\subsection{The bar complex perspective}
  2479	
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:4791:\begin{theorem}[Heisenberg obstruction at genus \texorpdfstring{$g$}{g}; \ClaimStatusProvedHere]\label{thm:heisenberg-obs}
chapters/theory/higher_genus_foundations.tex:4870:\begin{theorem}[Kac--Moody obstruction at genus \texorpdfstring{$g$}{g}; \ClaimStatusProvedHere]\label{thm:kac-moody-obs}
chapters/theory/higher_genus_foundations.tex:4917:by the same mechanism as in the Heisenberg case (Theorem~\ref{thm:heisenberg-obs}, Step~5).
chapters/theory/higher_genus_foundations.tex:4939:$\text{obs}_g = k \cdot \lambda_g$ in agreement with Theorem~\ref{thm:heisenberg-obs}.
chapters/theory/higher_genus_foundations.tex:4995:\textup{(}Remark~\textup{\ref{rem:propagator-weight-universality}}\textup{)}.
chapters/theory/higher_genus_foundations.tex:5018:for both channels (Remark~\ref{rem:propagator-weight-universality}).
chapters/theory/higher_genus_foundations.tex:5064:bar complex (Remark~\ref{rem:propagator-weight-universality}).
chapters/theory/higher_genus_foundations.tex:5178:(Proposition~\ref{prop:multi-generator-obstruction}\textup{(a)}),
chapters/theory/higher_genus_foundations.tex:5353:from the genus-$1$ curvature (Theorem~\ref{thm:heisenberg-obs}).
chapters/theory/higher_genus_foundations.tex:5385:\textup{(}Construction~\textup{\ref{constr:obstruction-recursion}}\textup{)}
chapters/theory/higher_genus_foundations.tex:5390:(Remark~\ref{rem:propagator-weight-universality}).
chapters/theory/higher_genus_foundations.tex:5410:(Remark~\ref{rem:propagator-weight-universality}).
chapters/theory/higher_genus_foundations.tex:5417:(Proposition~\ref{prop:multi-generator-obstruction}).
chapters/theory/higher_genus_foundations.tex:5420:(Heisenberg: Theorem~\ref{thm:heisenberg-obs};
chapters/theory/higher_genus_foundations.tex:5421:Kac--Moody: Theorem~\ref{thm:kac-moody-obs};
chapters/theory/higher_genus_foundations.tex:5422:Virasoro: Theorem~\ref{thm:vir-genus1-curvature}).
chapters/theory/higher_genus_foundations.tex:5427:(Theorem~\ref{thm:wn-obstruction}), and
chapters/theory/higher_genus_foundations.tex:5548:(Remark~\ref{rem:propagator-weight-universality},
chapters/theory/higher_genus_foundations.tex:5549:Proposition~\ref{prop:multi-generator-obstruction}(b)).
chapters/theory/higher_genus_foundations.tex:5671:(Remark~\ref{rem:propagator-weight-universality}),
 succeeded in 51ms:
  1000	
  1001	\subsection{The Hodge bundle and the period matrix}
  1002	\label{subsec:hodge-curvature-origin}
  1003	\index{Hodge bundle!and curvature}
  1004	
  1005	The Hodge bundle $\mathbb{E} = \pi_*\omega_\pi$ over
  1006	$\overline{\mathcal{M}}_g$ has fiber
  1007	$H^0(\Sigma_g, \Omega^1)$, a $g$-dimensional vector space.
  1008	Choose a symplectic basis
  1009	$\{A_k, B_k\}_{k=1}^g \subset H_1(\Sigma_g, \mathbb{Z})$ and
  1010	normalize: $\oint_{A_l} \omega_k = \delta_{kl}$. The period matrix
  1011	$\tau_{kl} = \oint_{B_l} \omega_k \in \mathfrak{H}_g$ determines
  1012	the propagator~\eqref{eq:elliptic-propagator} and its higher-genus
  1013	generalizations.
  1014	
  1015	The fiberwise bar differential squares to the Arnold defect
  1016	contracted with the OPE data of~$\cA$
  1017	\textup{(}Theorem~\textup{\ref{thm:quantum-arnold-relations},}
  1018	Proposition~\textup{\ref{prop:genus-g-curvature-package}(ii))}:
  1019	\begin{equation}\label{eq:arnold-defect-hg}
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2168,2248p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5678,5778p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1568,1618p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4784,4908p'" in /Users/raeez/chiral-bar-cobar succeeded in 83ms:
  1568	where the exponent $2n$ reflects the conformal weight $h_T = 2$ of the
  1569	generator (each copy of $T$ contributes weight~$2$ to the tensor product).
  1570	The genus-1 propagator is~\eqref{eq:genus1-propagator}
  1571	and the differential is~\eqref{eq:genus1-diff}, with the OPE data of the
  1572	Virasoro algebra replacing that of $\widehat{\mathfrak{sl}}_2$.
  1573	
  1574	\subsubsection{Curvature theorem}
  1575	
  1576	\begin{theorem}[Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc}; \ClaimStatusProvedHere]
  1577	\label{thm:vir-genus1-curvature}
  1578	The genus-1 differential satisfies:
  1579	\begin{equation}\label{eq:vir-genus1-dsquared}
  1580	(d^{(1)})^2 = \frac{c}{2} \cdot \omega_1 \cdot \operatorname{id}
  1581	\end{equation}
  1582	where $\omega_1 \in H^2(\overline{\mathcal{M}}_{1,1})$ is the fundamental class.
  1583	Equivalently, the genus-1 obstruction coefficient is
  1584	$\kappa(\mathrm{Vir}_c) = c/2$, in agreement with the genus universality
  1585	theorem (Theorem~\ref{thm:genus-universality}).
  1586	\end{theorem}
  1587	
 succeeded in 102ms:
  5678	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5679	with $\delta F_2(\cW_3) = (c{+}204)/(16c) \neq 0$.
  5680	The identification
  5681	$\Gamma_{\cA} = \kappa(\cA)\Lambda$ fails for multi-weight
  5682	algebras.
  5683	\end{remark}
  5684	
  5685	\begin{remark}[Propagator weight universality]%
  5686	\label{rem:propagator-weight-universality}%
  5687	\index{propagator weight universality|textbf}%
  5688	\index{bar complex!propagator weight}%
  5689	\index{prime form!weight of d log}%
  5690	The bar complex propagator is $d\log E(z,w)$, where $E(z,w)$
  5691	is the prime form on a Riemann surface. The prime form is a
  5692	section of $K^{-1/2} \boxtimes K^{-1/2}$
  5693	(cf.\ the critical pitfall in~\S\ref{sec:conventions}),
  5694	so $d\log E = dE/E$ has weight~$1$ in both variables,
  5695	\emph{regardless} of the conformal weight of the fields being sewed.
  5696	
  5697	This observation has two consequences:
 succeeded in 102ms:
  2168	contributing its own vacuum leakage. The general formula
  2169	for all $N$ validates the Master Table entry
  2170	(Table~\ref{tab:master-invariants}).
  2171	
  2172	\begin{theorem}[Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN}; \ClaimStatusProvedHere]
  2173	\label{thm:wn-obstruction}
  2174	For the principal $\mathcal{W}$-algebra
  2175	$\mathcal{W}_N^k = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
  2176	at generic level $k \neq -N$, the genus-1 obstruction coefficient is:
  2177	\begin{equation}\label{eq:wn-kappa}
  2178	\kappa(\mathcal{W}_N^k) = c \sum_{s=2}^{N} \frac{1}{s}
  2179	= c \cdot (H_N - 1)
  2180	\end{equation}
  2181	where $c = c(\mathcal{W}_N^k)$ is the central charge and
  2182	$H_N = \sum_{j=1}^N 1/j$ is the $N$-th harmonic number.
  2183	\end{theorem}
  2184	
  2185	\begin{proof}
  2186	The proof has three ingredients.
  2187	
 succeeded in 96ms:
  4784	
  4785	Combining with Step 2 gives the stated formula.
  4786	\end{proof}
  4787	
  4788	\subsection{Example 1: Heisenberg algebra, level shift obstruction}
  4789	\label{subsec:heisenberg-obstruction}
  4790	
  4791	\begin{theorem}[Heisenberg obstruction at genus \texorpdfstring{$g$}{g}; \ClaimStatusProvedHere]\label{thm:heisenberg-obs}
  4792	For the Heisenberg vertex algebra $\mathcal{H}_\kappa$ at level $\kappa$, the 
  4793	genus-$g$ obstruction is :
  4794	\begin{equation}
  4795	\text{obs}_g^{\mathcal{H}} = \kappa \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g, \mathbb{C})
  4796	\qquad \end{equation}
  4797	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle \textup{(LOCAL)}.
  4798	
  4799	Explicitly:
  4800	\begin{itemize}
  4801	\item $g=1$: $\text{obs}_1 = \kappa \cdot \lambda_1$ \textup{(g=1 only; all-weight at g=1 is unconditional)} where $\lambda_1 = c_1(\mathbb{E}) \in H^2(\overline{\mathcal{M}}_{1,1})$
  4802	\item $g=2$: $\text{obs}_2 = \kappa \cdot \lambda_2 = \kappa \cdot c_2(\mathbb{E})$ \item $g \geq 3$: $\text{obs}_g = \kappa \cdot \lambda_g$ \end{itemize}
  4803	\end{theorem}
codex
The load-bearing upstream theorem is now in view. The proof is not circular through `thm:family-index`, but the replacement argument looks dangerously under-specified: it jumps from “one-variable recursion” and “same propagator” to the exact class `\lambda_g` without a cited uniqueness theorem. I’m checking whether that uniqueness statement exists anywhere or is simply missing.
exec
/bin/zsh -lc "rg -n \"one-variable recursion|same Hodge line|clutching maps .* force|force.*lambda_g|uniqueness.*lambda_g|tautological line|Gamma_\\\\cA,g|scalar shadow-tower recursion|Construction~\\\\ref\\{constr:obstruction-recursion\\}\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{constr:obstruction-recursion\\}|Construction\\[Obstruction recursion|obstruction recursion\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '820,835p'" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:one-variable recursion|same Hodge line|clutching maps .* force|force.*lambda_g|uniqueness.*lambda_g|tautological line|Gamma_\cA,g|scalar shadow-tower recursion|Construction~\ref\{constr:obstruction-recursion\})
                                                                                                                                   ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '7280,7375p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:11231:The obstruction recursion
chapters/theory/higher_genus_modular_koszul.tex:12103:$\cA^{\mathrm{sh}}$ makes the obstruction recursion explicit:
chapters/theory/higher_genus_modular_koszul.tex:12611:\label{constr:obstruction-recursion}
chapters/theory/higher_genus_modular_koszul.tex:14590:The following algorithm instantiates the obstruction recursion
chapters/theory/higher_genus_modular_koszul.tex:14863:then the obstruction recursion
chapters/theory/higher_genus_modular_koszul.tex:29899:%% 4. The obstruction recursion
chapters/theory/higher_genus_modular_koszul.tex:29902:\subsubsection{The obstruction recursion and shadow depth
chapters/theory/higher_genus_modular_koszul.tex:29909:\index{obstruction recursion!tower|textbf}
chapters/theory/higher_genus_modular_koszul.tex:30175:and the obstruction recursion form a single
chapters/theory/higher_genus_modular_koszul.tex:30200:abstractly by the obstruction recursion
chapters/theory/higher_genus_foundations.tex:5384:The obstruction recursion
 succeeded in 50ms:
   820	| `thm:heisenberg-obs` | `theorem` | 4725 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
   821	| `thm:kac-moody-obs` | `theorem` | 4807 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
   822	| `thm:w3-obstruction` | `theorem` | 4927 | \texorpdfstring{$W_3$}{W3} fiberwise obstruction |
   823	| `comp:w3-obs-explicit` | `computation` | 4988 | Explicit genus-$1$ value of the $W_3$ obstruction |
   824	| `thm:obstruction-nilpotent` | `theorem` | 5010 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
   825	| `thm:obstruction-nilpotent-all-genera` | `theorem` | 5039 | Nilpotence of obstruction (all genera) |
   826	| `cor:mumford-multiplicative` | `corollary` | 5127 | Mumford multiplicative relations for obstruction classes |
   827	| `thm:genus-universality` | `theorem` | 5243 | Genus universality |
   828	| `prop:multi-generator-obstruction` | `proposition` | 5652 | Multi-generator edge universality |
   829	| `prop:f2-quartic-dependence` | `proposition` | 5700 | Genus-$2$ quartic dependence |
   830	| `cor:anomaly-ratio` | `corollary` | 5761 | Anomaly ratio identity |
   831	| `cor:kappa-periodicity` | `corollary` | 5777 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
   832	| `cor:kappa-additivity` | `corollary` | 5806 | Additivity of the obstruction coefficient |
   833	| `cor:kappa-sum-wn` | `corollary` | 5827 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
   834	| `cor:critical-level-universality` | `corollary` | 5850 | Universal genus-$1$ criticality criterion; scalar-lane collapse |
   835	| `cor:tautological-class-map` | `corollary` | 5886 | Tautological class map on the scalar lane; universal genus-$1$ class |
 succeeded in 51ms:
  7280	cutting map.
  7281	\end{proof}
  7282	
  7283	\begin{remark}[Conceptual cohesion]%
  7284	\label{rem:log-clutching-cohesion}
  7285	\index{clutching kernel!logarithmic!conceptual role}
  7286	The logarithmic clutching kernel is the geometric hinge of the
  7287	modular package: stable-curve gluing lives on the Deligne--Mumford
  7288	side, while configuration-space compactification lives on the
  7289	logarithmic Fulton--MacPherson side. The kernel
  7290	$K^{\mathrm{log}}$ is designed to make them interact
  7291	functorially. Together with the genus-universality theorem
  7292	(Theorem~\ref{thm:genus-universality}) and the stable-graph bar
  7293	differential (Lemma~\ref{lem:stable-graph-d-squared}), the
  7294	logarithmic clutching kernels would provide the geometric
  7295	foundation for the modular completion of the bar complex.
  7296	Note that Theorem~\ref{thm:planted-forest-tropicalization}
  7297	identifies the planted-forest coefficient algebra
  7298	$\mathbb{G}_{\mathrm{pf}}$ with the chain algebra on
  7299	$\operatorname{Trop}(\FM_n(C|D))$; the degeneration formula

thinking
**Examining theorem details**

I need to check the theorem registry for the stale line number, but I think I might not need to look at the file itself. The registry line 827 seems related to higher genus foundations, which isn't my target, so it might be okay. I could read around the file header, but that doesn’t seem important right now. I should focus on examining the target theorem proof chain, possibly regarding universal generating functions and anomaly Koszul, perhaps in higher genus foundations. Time to search!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6270,6915p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:universal-generating-function\\}|label\\{thm:anomaly-koszul\\}|Universal generating function|Anomaly cancellation under tensor product|anomaly-koszul\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:modular-characteristic\\}|label\\{thm:genus-universality\\}|label\\{thm:family-index\\}|label\\{thm:universal-generating-function\\}|label\\{thm:anomaly-koszul\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  6270	conclusion is universal for arbitrary modular Koszul algebras. This
  6271	constrains the deformation space $Q_g(\cA^!)$
  6272	\textup{(}Theorem~\ref{thm:obs-def-pairing-explicit}\textup{)} to have
  6273	a complementary Hodge type.
  6274	\end{remark}
  6275	
  6276	\begin{proposition}[Scalar obstruction lifting criterion; \ClaimStatusProvedHere]
  6277	\label{prop:obstruction-lifting}
  6278	\index{obstruction!lifting criterion}
  6279	A modular Koszul chiral algebra $\cA$ on the proved scalar lane lifts
  6280	from genus~$g$ to genus~$g+1$ at the scalar level
  6281	\textup{(}i.e., $\mathrm{obs}_{g+1}(\cA) = 0$ in the scalar
  6282	obstruction group\textup{)} if and only if $\kappa(\cA) = 0$.
  6283	Equivalently:
  6284	\begin{enumerate}[label=\textup{(\roman*)}]
  6285	\item If $\kappa \neq 0$, the scalar obstruction classes
  6286	 $\mathrm{obs}_g(\cA)$ are nonzero for every genus $g \geq 1$;
  6287	\item If $\kappa = 0$, the scalar obstruction classes vanish for all
  6288	 genera on the proved scalar lane.
  6289	\end{enumerate}
 succeeded in 53ms:
chapters/theory/higher_genus_modular_koszul.tex:2741:Part~(iv) is Theorem~\ref{thm:anomaly-koszul}.
chapters/theory/higher_genus_modular_koszul.tex:2814:(Theorem~\ref{thm:anomaly-koszul}).
 succeeded in 53ms:
chapters/theory/higher_genus_foundations.tex:5298:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
chapters/connections/concordance.tex:5928:\ClaimStatusProvedHere]\label{thm:family-index}
chapters/theory/higher_genus_modular_koszul.tex:2660:\label{thm:modular-characteristic}

thinking
**Investigating missing labels**

I’m finding it interesting that there are no labels for "universal-generating-function" or "anomaly-koszul" in the current files. I need to search for what's missing, which means the target theorem related to "modular-characteristic" may be citing undefined labels. I'll have to verify this across the entire repository, maybe even conduct a broader search to find any clues or related information. It seems like there's a bit of a gap that I need to fill in!
codex
Two labels used in the target proof may be broken. I’ve confirmed `thm:genus-universality` exists upstream, but `thm:universal-generating-function` and `thm:anomaly-koszul` did not show up in the first pass. I’m checking whether they exist anywhere live or whether Theorem D is citing phantom labels.
exec
/bin/zsh -lc "rg -n \"\\\\label\\{thm:(universal-generating-function|anomaly-koszul)\\}\" chapters appendices metadata -g '*.tex' -g '*.md' -g '*.json*'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{thm:(universal-generating-function|anomaly-koszul)\})
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n "thm:universal-generating-function|thm:anomaly-koszul" .' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Universal generating function|Anomaly cancellation|additivity under tensor product|tensor product.*kappa|family index theorem follows|hatA|A-hat" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./wave2_audit_20260413_001942/S10_examples_to_wn.md:300:main.tex:1537: \phantomsection\label{thm:universal-generating-function}% % genus_expansions.tex (8 refs)
./audit_campaign_20260412_231034/T12_MC5_BV_bar.md:689:   667	\phantomsection\label{thm:anomaly-koszul}
./wave2_audit_20260413_001942/S06_intro_to_body.md:341:/bin/zsh -lc "rg -n '\\\\label\\{(thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-characteristic|thm:riccati-algebraicity|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:mc2-bar-intrinsic|thm:bar-nilpotency-complete|prop:pole-decomposition|thm:fundamental-twisting-morphisms|thm:bar-concentration|thm:koszul-equivalences-meta|thm:universal-generating-function|thm:spectral-characteristic|thm:hochschild-polynomial-growth|lem:chirhoch-descent|thm:e1-primacy|thm:thqg-swiss-cheese|cor:shadow-visibility-genus|rem:two-orthogonal-axes|thm:central-charge-complementarity)\\}' chapters appendices metadata" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./wave2_audit_20260413_001942/S06_intro_to_body.md:366:chapters/examples/genus_expansions.tex:1913:\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
./audit_campaign_20260412_231034/T17_chirhoch1_KM.md:673: \textup{(}Theorem~\textup{\ref{thm:universal-generating-function}}\textup{)}:
./wave2_audit_20260413_001942/S12_ordered_to_symmetric.md:871:/bin/zsh -lc "rg -n '\\\\label\\{thm:higher-genus-inversion\\}|\\\\label\\{thm:bar-modular-operad\\}|\\\\label\\{thm:universal-theta\\}|\\\\label\\{thm:universal-MC\\}|\\\\label\\{thm:mc2-full-resolution\\}|\\\\label\\{thm:genus-universality\\}|\\\\label\\{thm:universal-generating-function\\}|\\\\label\\{thm:quantum-complementarity-main\\}|\\\\label\\{thm:riccati-algebraicity\\}|\\\\label\\{prop:depth-gap-trichotomy\\}|\\\\label\\{thm:single-line-dichotomy\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/S12_ordered_to_symmetric.md:922:/bin/zsh -lc "rg -n '\\\\label\\{thm:higher-genus-inversion\\}|\\\\label\\{thm:bar-modular-operad\\}|\\\\label\\{thm:genus-universality\\}|\\\\label\\{thm:universal-generating-function\\}|\\\\label\\{thm:quantum-complementarity-main\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/S12_ordered_to_symmetric.md:1004:/bin/zsh -lc "grep -nF '\\label{thm:universal-generating-function}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:
./wave2_audit_20260413_001942/S12_ordered_to_symmetric.md:1163: 31845	(Theorem~\ref{thm:universal-generating-function},
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:925:/bin/zsh -lc "rg -n 'thm:universal-generating-function|Theorem~\\\\ref\\{thm:universal-generating-function\\}|universal-generating-function|multi-generator-universality|genus-universality' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:934:2439: (Theorem~\ref{thm:universal-generating-function}).
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:941:2738:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:945:2812:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:946:2881:Theorem~\ref{thm:universal-generating-function}.
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:1090:/bin/zsh -lc "rg -n '\\\\label\\{thm:universal-generating-function\\}|universal generating function' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:1118:I need to locate a specific label that might not be in the snippet. I’ll search for `label{thm:universal-generating-function}` using a fixed string approach, possibly with the `F` option. I think using `rg -F` could help with that. It feels like a smart way to narrow down my search and find the exact label I need. Let's dive into this and see what I can uncover!
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:1120:/bin/zsh -lc "rg -n -F '\\label{thm:universal-generating-function}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:1129:2439: (Theorem~\ref{thm:universal-generating-function}).
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:1130:2738:Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:1131:2812:Bernoulli residues (Theorem~\ref{thm:universal-generating-function});
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:1059:\index{A-hat genus@$\hat{A}$-genus!geometric derivation}
chapters/theory/higher_genus_foundations.tex:5894:The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
chapters/theory/higher_genus_foundations.tex:6368:\textup{(}Remark~\textup{\ref{rem:A-hat-genus})}. For arbitrary
chapters/theory/higher_genus_modular_koszul.tex:2743:under tensor product and $\kappa(\mathbb{C}) = 0$ (the trivial
chapters/theory/higher_genus_modular_koszul.tex:2824:\index{free energy!A-hat genus@$\hat{A}$-genus|textbf}
chapters/theory/higher_genus_modular_koszul.tex:2825:\index{A-hat genus@$\hat{A}$-genus!scalar free energy|textbf}
chapters/theory/higher_genus_modular_koszul.tex:13884: kernel through the A-hat genus:
chapters/theory/higher_genus_modular_koszul.tex:26451:\index{A-hat genus@$\hat{A}$-genus!shadow generating function}
chapters/connections/concordance.tex:6238:and the family index theorem follows.
codex
`thm:universal-generating-function` is live in [genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex), but `thm:anomaly-koszul` is not in theory; it lives in [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex). I’m reading both because Theorem D currently imports them as if they were clean upstream theorem dependencies.
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1900,1978p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '1850,1905p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1900	\index{A-hat genus@$\hat{A}$-genus}
  1901	The generating function $(x/2)/\sin(x/2)$ is the Wick rotation of the
  1902	$\hat{A}$-genus: $\hat{A}(x) = (x/2)/\sinh(x/2)$, related by the
  1903	substitution $x \mapsto ix$. This is not a coincidence: the family
  1904	index theorem (Theorem~\ref{thm:family-index}) shows that
  1905	the genus expansion is the Gro\-then\-dieck--Rie\-mann--Roch pushforward of
  1906	the Todd class of the universal curve, and $(x/2)/\sin(x/2)$ is the
  1907	even part of the Wick-rotated Todd class. The positivity of all coefficients
  1908	($\lambda_g^{\mathrm{FP}} > 0$ for all~$g$), in contrast to the
  1909	alternating-sign $\hat{A}$-expansion, reflects the Hodge index
  1910	theorem on $\overline{\mathcal{M}}_g$.
  1911	\end{remark}
  1912	
  1913	\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
  1914	\index{genus expansion!universal generating function}
  1915	\index{obstruction coefficient!generating function}
  1916	For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
  1917	weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
  1918	\begin{equation}\label{eq:universal-generating-function}
  1919	\sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
exec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '225,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2648,2745p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1850	The correct bridge between holomorphic and topological frameworks is Chern--Simons gauge equivalence, not merely restriction from complex curves to $S^1$: Cattaneo--Mnev~\cite{CattaneoMnev10} establish that configuration space integrals on $3$-manifolds produce Vassiliev invariants via BV integration, and the comparison map involves the CS partition function (not a pointwise restriction of propagators).
  1851	
  1852	\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
  1853	The conjecture asserts that the dg Lie algebras controlling
  1854	holomorphic (chiral bar) and topological (Kontsevich integral)
  1855	deformation problems are quasi-isomorphic.
  1856	(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
  1857	\end{remark}
  1858	
  1859	\subsection{Anomaly cancellation and Koszul structure}
  1860	\label{subsec:anomaly-koszul}
  1861	\index{anomaly!Koszul-theoretic}
  1862	
  1863	\begin{theorem}[Anomaly cancellation as Koszul constraint;
  1864	\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
  1865	\index{anomaly cancellation!Koszul constraint}
  1866	For the matter-ghost system
  1867	$\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$:
  1868	\begin{enumerate}[label=\textup{(\roman*)}]
  1869	\item The obstruction coefficient is additive:
 succeeded in 52ms:
  2648	degeneration a chain map, to each consistency relation a chain
  2649	homotopy. Passing to cohomology recovers the classical
  2650	modular-functor package; for $\widehat{\fg}_k$ at integrable level, $H^0(V_{g,n})$ is the
  2651	Tsuchiya--Ueno--Yamada space of conformal blocks
  2652	(Remark~\ref{rem:chain-vs-classical-mf}). The degree-$2$ projection
  2653	of $\Theta_\cA$ is the scalar $\kappa(\cA)$ that controls the
  2654	entire genus tower (the spectral discriminant~$\Delta_\cA$,
  2655	periodicity profile~$\Pi_\cA$, and full MC
  2656	class~$\Theta_\cA$ require data beyond~$\kappa$;
  2657	see Definition~\ref{def:full-modular-package}).
  2658	
  2659	\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
  2660	\label{thm:modular-characteristic}
  2661	\index{modular characteristic theorem|textbf}
  2662	\index{kappa@$\kappa$!as first characteristic number|textbf}
  2663	\textup{[}Regime: curved-central
  2664	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  2665	
  2666	Let $\cA$ be a modular Koszul chiral algebra
  2667	(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
 succeeded in 52ms:
   225	 Definition~\ref{def:modular-convolution-dg-lie} is the strict model.
   226	 \emph{Design constraint}:
   227	 $\operatorname{hom}_\alpha$ extends to $\infty$-morphisms in either
   228	 slot separately but not both simultaneously~\cite[Section~6]{RNW19}.
   229	
   230	\item \textbf{Global collision geometry} (Pillar~C). The natural
   231	 compactification for punctured curves and nodal degenerations
   232	 is \emph{logarithmic Fulton--MacPherson}
   233	 $\overline{\operatorname{FM}}_n(X|D)$ on simple normal crossings pairs
   234	 $(X, D)$, in the sense of Mok~\cite{Mok25}. Ordinary FM
   235	 compactification is the special case $D = \emptyset$.
   236	\end{enumerate}
   237	
   238	\subsection*{Family index theorem}
   239	
   240	\begin{theorem}[Family index theorem for genus expansions;
   241	\ClaimStatusProvedHere]\label{thm:guide-family-index}
   242	\index{index theorem!modular deformation|textbf}
   243	\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
   244	Let $\cA$ be a Koszul chiral algebra with obstruction coefficient




thinking
**Evaluating build order**

I’m trying to figure out if I need to determine the build order. I think I can still compile, but there’s a potential issue with what I’m calling a "foundation audit." This might highlight a hidden import as a finding. I need to get the exact fix and consider citing a specific line from a .tex file, or I may need to move the theorem upstream into the theory file.
thinking
**Assessing theorem structure**

I'm evaluating the architecture of the theorem cited on line 2738, as it seems poor. I wonder if there's a proof in higher genus foundations. It references the universal generating function, which doesn’t make it independent. The main proof relies on an example theorem but is affected by a hidden structural weakness. The severity of this issue might be medium to high. A better fix could be to replace the citation with a more self-contained proof from related propositions or theorems.
thinking
**Identifying proof gaps**

I think the exact fix for the theorem involves promoting certain lines in the document to immediately after the genus-universality theorem in higher genus foundations. Then I would cite that local theorem from a specific section. Additionally, there seems to be a significant gap in the genus-universality proof between lines 5380 and 5405. I should check for any uniqueness theorems elsewhere, but prior searches yielded nothing. This could be critical since the proof lacks the necessary uniqueness conditions for the genre-g coefficient class.
thinking
**Evaluating tautological criteria**

I need to check `prop:tautological-line-support-criterion` and `thm:tautological-line-support` to see if it can apply to uniform-weight lanes. It does, but the proof relies on `thm:genus-universality`, which creates a circular reference. A potential solution might be to prove the hypothesis from `prop:tautological-line-support-criterion` first, which could then let me derive `thm:genus-universality`. If that doesn't work, I might need to restrict the theorem to just g=1 until we have a proper uniqueness proof.
codex
I’ve found one scope leak already: the upstream duality clause cites `thm:wn-obstruction`, but that live theorem only proves the `\mathfrak{sl}_N` principal `\mathcal W_N` case, while the statement is written for general principal `\mathcal W^k(\mathfrak g,f_{\mathrm{prin}})`. I’m verifying whether a general-type theorem exists elsewhere or whether this is an actual overclaim.
exec
/bin/zsh -lc "rg -n \"general-w-obstruction|principal .*W.*exponents|varrho\\(\\\\mathfrak\\{g\\}\\)|sum_{i=1}.*m_i|W_N\\"'^k'"\\(\\\\mathfrak\\{sl\\}_N\\)|W\\"'^k'"\\(\\\\mathfrak\\{g\\}, f_\\{\\\\mathrm\\{prin\\}\\}\\)\" chapters/examples/w_algebras.tex chapters/examples/w_algebras_deep.tex chapters/examples/landscape_census.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:general-w-obstruction|principal .*W.*exponents|varrho\(\mathfrak\{g\}\)|sum_{i=1}.*m_i|W_N\^k\(\mathfrak\{sl\}_N\)|W\^k\(\mathfrak\{g\}, f_\{\mathrm\{prin\}\}\))
                                                              ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2310,2352p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2310	\begin{equation}\label{eq:general-w-kappa}
  2311	\kappa(\mathcal{W}^k(\mathfrak{g})) = c \sum_{i=1}^{r} \frac{1}{m_i + 1}
  2312	\end{equation}
  2313	where $c = c(\mathcal{W}^k(\mathfrak{g}))$ is the central charge.
  2314	\end{corollary}
  2315	
  2316	\begin{proof}
  2317	The proof of Theorem~\ref{thm:wn-obstruction} applies verbatim: $\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ has $r$ generators $W^{(m_i + 1)}$ of conformal weights $h_i = m_i + 1$ ($i = 1, \ldots, r$), arising from the Casimir invariants of $\mathfrak{g}$ via Drinfeld--Sokolov reduction~\cite{FL88}. In the Zamolodchikov normalization, the leading OPE pole is $W^{(h_i)}_{(2h_i - 1)} W^{(h_i)} = c/h_i$ (the same free field argument as Step~1 of Theorem~\ref{thm:wn-obstruction} applies: the Miura transform gives $W^{(h_i)}$ with leading term $\sum (\partial\phi_j)^{h_i}$, producing a factor $1/h_i$ in the Wick contraction). Cross-term vanishing (Step~2) holds by orthogonality of generators of distinct conformal weights. Summing over generators and promoting to genus~$1$ via the $B$-cycle mechanism (Step~3):
  2318	\[
  2319	\kappa = \sum_{i=1}^{r} \frac{c}{m_i + 1} = c \sum_{i=1}^{r} \frac{1}{m_i + 1}. \qedhere
  2320	\]
  2321	\end{proof}
  2322	
  2323	\begin{remark}[Values for classical and exceptional types]\label{rem:general-w-kappa-values}
  2324	\index{obstruction coefficient!classical types}
  2325	The harmonic sum $\varrho(\mathfrak{g}) = \sum_{i=1}^r 1/(m_i + 1)$, so that $\kappa = c \cdot \varrho(\mathfrak{g})$, takes the following values:
  2326	\begin{center}
  2327	\renewcommand{\arraystretch}{1.3}
  2328	\begin{tabular}{lccl}
  2329	\toprule
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2238,2268p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2238	\end{equation}
  2239	The $B$-cycle quasi-periodicity at genus~1
  2240	(equation~\eqref{eq:B-cycle-quasi-periodicity}) promotes each
  2241	scalar curvature $c/s$ to $(c/s) \cdot \omega_1$ independently, by
  2242	the same mechanism as
  2243	Theorems~\ref{thm:vir-genus1-curvature}
  2244	and~\ref{thm:w3-genus1-curvature}. Summing over generators:
  2245	\begin{equation}
  2246	(d^{(1)})^2 = c \cdot (H_N - 1) \cdot \omega_1 \cdot \operatorname{id}
  2247	\end{equation}
  2248	By definition, $\kappa(\mathcal{W}_N^k)$ is the coefficient of
  2249	$\omega_1$ in $(d^{(1)})^2$, so
  2250	$\kappa = c \cdot (H_N - 1)$. This is consistent with the
  2251	genus universality theorem
  2252	(Theorem~\ref{thm:genus-universality}): at genus~$1$,
  2253	$\mathrm{obs}_1 = \kappa \cdot \lambda_1$ unconditionally.
  2254	For $N = 2$ (Virasoro, uniform weight), the factorization
  2255	$\mathrm{obs}_g = \kappa \cdot \lambda_g$ holds at all genera;
  2256	for $N \geq 3$ (multi-weight), the scalar formula \emph{fails}
  2257	at genus $g \geq 2$: the free energy receives a cross-channel
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1238,1265p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1238	\label{cor:anomaly-ratio-ds}
  1239	\index{anomaly ratio!DS reduction}
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

thinking
**Exploring theorem references**

I'm diving into the genus-universality theorem, specifically part (ii), which cites the wn-obstruction theorem. It seems there could also be a corollary related to the general-w-obstruction. I want to do a search to gather more details about these specific theorems and their connections. Understanding these could certainly clarify their implications better!
exec
/bin/zsh -lc "rg -n \"label\\{cor:general-w-obstruction\\}|label\\{cor:anomaly-ratio-ds\\}|general W-algebra obstruction coefficient|General W\" chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2298,2316p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2161:\subsection{\texorpdfstring{General $\mathcal{W}_N$: obstruction coefficient formula}{General WN: obstruction coefficient formula}}
2306:\label{cor:general-w-obstruction}
 succeeded in 53ms:
  2298	Since $\kappa = c \cdot (H_N - 1)$ and $\kappa' = c' \cdot (H_N - 1)$:
  2299	$\kappa + \kappa' = (H_N - 1)(c + c')$.
  2300	The complementarity sum $c + c' = 2(N{-}1)(2N^2{+}2N{+}1)$
  2301	is level-independent
  2302	(Theorem~\ref{thm:central-charge-complementarity}).
  2303	\end{proof}
  2304	
  2305	\begin{corollary}[Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)}; \ClaimStatusProvedHere]
  2306	\label{cor:general-w-obstruction}
  2307	\index{obstruction coefficient!general W-algebra}
  2308	\index{W-algebra@$\mathcal{W}$-algebra!general obstruction coefficient}
  2309	Let $\mathfrak{g}$ be a simple Lie algebra of rank~$r$ with exponents $m_1, \ldots, m_r$. The principal $\mathcal{W}$-algebra $\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ at generic level $k \neq -h^\vee$ has obstruction coefficient:
  2310	\begin{equation}\label{eq:general-w-kappa}
  2311	\kappa(\mathcal{W}^k(\mathfrak{g})) = c \sum_{i=1}^{r} \frac{1}{m_i + 1}
  2312	\end{equation}
  2313	where $c = c(\mathcal{W}^k(\mathfrak{g}))$ is the central charge.
  2314	\end{corollary}
  2315	
  2316	\begin{proof}

thinking
**Checking the modular-characteristic theorem**

I think I need to check if the modular-characteristic theorem, specifically its part (iii), covers free-field algebras and duality. I wonder if it might tie into the anomaly theorem or perhaps related concepts like additivity. It seems like this could be okay. I'll look into it further to clarify how these ideas transition and connect with each other!
codex
Another scope mismatch is emerging in the target theorem itself: its duality clause adds “free-field algebras,” but the cited upstream theorem only spells out affine Kac–Moody, principal `\mathcal W`, and the abelian Heisenberg case. I’m checking whether the rest of the free-field lane is actually proved elsewhere or whether this is an unsupported enlargement.
exec
/bin/zsh -lc "rg -n \"free-field algebras|free fermion|beta\\\\gamma|fermion-all-genera|ghost.*kappa|kappa\\(bc|kappa\\(beta|kappa\\(\\beta\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '4768,4805p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:free-field algebras|free fermion|beta\gamma|fermion-all-genera|ghost.*kappa|kappa\(bc|kappa\(beta|kappa\(\beta)
                                            ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5322,5358p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4768	 The genus-graded bar complex
  4769	 $\barB^{(g)}(\cA)$ organizes the algebraic genus decomposition and
  4770	 the higher-genus correction package
  4771	 \textup{(}Theorem~\textup{\ref{thm:genus-universality})}.
  4772	\item \emph{Boundary factorization = clutching law.}
  4773	 The genus-graded bar classes satisfy the modular-operadic clutching
  4774	 identities along boundary divisors of
  4775	 $\overline{\mathcal{M}}_{g,n}$, so their separating and
  4776	 non-separating residues are expressed in terms of lower-genus bar
  4777	 classes
  4778	 \textup{(}Theorem~\textup{\ref{thm:genus-induction-strict})}.
  4779	\end{enumerate}
  4780	\end{theorem}
  4781	
  4782	\begin{proof}
  4783	Each clause references its proof:
  4784	(i)~Theorems~\ref{thm:bar-semi-infinite-km}
  4785	and~\ref{thm:brst-bar-genus0};
  4786	(ii)~Corollaries~\ref{cor:anomaly-duality-km}
  4787	and~\ref{cor:anomaly-duality-w},
 succeeded in 51ms:
  5322	$\kappa(\widehat{\mathfrak{g}}_k) = \frac{(k+h^\vee)\dim\mathfrak{g}}{2h^\vee}$,\;
  5323	$\kappa(\mathrm{Vir}_c) = \frac{c}{2}$.
  5324	\item[\textup{(ii)}] \emph{Duality.}
  5325	For affine Kac--Moody algebras $\widehat{\mathfrak{g}}_k$ with Feigin--Frenkel dual
  5326	$\widehat{\mathfrak{g}}_{-k-2h^\vee}$: $\kappa(\mathcal{A}^!) = -\kappa(\mathcal{A})$.
  5327	For $\mathcal{W}$-algebras $\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ obtained by Drinfeld--Sokolov
  5328	reduction: $\kappa(\mathcal{A}^!) = \varrho(\mathfrak{g})\, K - \kappa(\mathcal{A})$, where
  5329	$K = c(\mathcal{A}) + c(\mathcal{A}^!)$ is the complementarity constant
  5330	(Remark~\ref{rem:vir-vs-km-complementarity}) and
  5331	$\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i + 1}$ is the exponent sum
  5332	($m_1, \ldots, m_r$ the exponents of~$\mathfrak{g}$; for $\mathcal{W}_N = \mathcal{W}(\mathfrak{sl}_N)$,
  5333	$\varrho = H_N - 1 = \sum_{s=2}^{N} 1/s$).
  5334	In particular, $\kappa + \kappa' = 0$ for affine Kac--Moody algebras
  5335	(by the Feigin--Frenkel involution
  5336	$k \mapsto -k - 2h^\vee$, which gives
  5337	$\kappa' = -\kappa$; note that the $\varrho$-formula
  5338	applies to $\mathcal{W}$-algebras, not to affine Kac--Moody
  5339	algebras directly),
  5340	$\kappa + \kappa' = 13$ for the Virasoro algebra
  5341	($\varrho = 1/2$, $K = 26$),
exec
/bin/zsh -lc 'rg -nF "fermion-all-genera" chapters/examples/free_fields.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -nF "free-field algebras" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nF \"kappa(\\mathcal{F}\" chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:5897:For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2547:Theorem~\ref{thm:multi-weight-genus-expansion}; all free-field algebras are exact exceptions by
chapters/theory/higher_genus_modular_koszul.tex:2705: free-field algebras. For the principal $\mathcal{W}$-algebra
chapters/theory/higher_genus_modular_koszul.tex:5391:while all free-field algebras remain
chapters/theory/higher_genus_modular_koszul.tex:29691: Kac--Moody and free-field algebras;
 succeeded in 53ms:
chapters/examples/free_fields.tex:174:Modular characteristic $\kappa(\mathcal{F}) = c/2 = 1/4$.
chapters/examples/free_fields.tex:230: $\kappa(\mathcal{F}) = c/2 = 1/4$.
chapters/examples/free_fields.tex:321:$\kappa(\mathcal{F}) = 1/4$ is fixed.
chapters/examples/free_fields.tex:364:with $\kappa(\mathcal{F}) = 1/4$
chapters/examples/free_fields.tex:396:= \frac{\kappa(\mathcal{F})}{\kappa(\mathcal{H}_k)}
chapters/examples/free_fields.tex:478: $\kappa(\mathcal{F}^!) = -1/4$.
chapters/examples/free_fields.tex:481: $\kappa(\mathcal{F}) + \kappa(\mathcal{F}^!) = 0$.
chapters/examples/free_fields.tex:500:$\kappa(\mathcal{F}^!) = c'/2 = -1/4$.
chapters/examples/free_fields.tex:645:$\kappa(\mathcal{F}^!)$ & $-1/4$ \\
chapters/examples/free_fields.tex:686: $\kappa(\mathcal{F}^{\otimes d}) = d/4$\textup{)}.
chapters/examples/free_fields.tex:5470:$\kappa(\mathcal{F}) = 1/4$.
chapters/examples/free_fields.tex:5487: $\kappa(\mathcal{F}) + \kappa(\mathcal{F}^!) = 0$ &
chapters/examples/free_fields.tex:5491: $\kappa(\mathcal{F}) = c/2 = 1/4$ \\
codex
The free-field clause is at least not pure invention: the repo does contain explicit free-field formulas, including `\kappa(\mathcal F)+\kappa(\mathcal F^!)=0`. I’m checking whether the target theorem simply cites the wrong upstream result or whether it also misses the needed free-field theorem reference.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '460,505p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:fermion-all-genera\\}|fermion-all-genera|beta-gamma.*all genera|all-genera\" chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   460	
   461	\subsubsection{Koszul duality and complementarity}
   462	\label{sec:fermion-complementarity}%
   463	\index{free fermion!Koszul duality}%
   464	\index{free fermion!complementarity}%
   465	
   466	\begin{proposition}[Free fermion complementarity;
   467	\ClaimStatusProvedHere]
   468	\label{prop:fermion-complementarity}
   469	The free fermion and its Koszul dual satisfy:
   470	\begin{enumerate}
   471	\item\label{item:fermion-kd}
   472	 Koszul dual:
   473	 $\mathcal{F}^! = \mathrm{Sym}^{\mathrm{ch}}(\gamma)$
   474	 \textup{(}Theorem~\textup{\ref{thm:single-fermion-boson-duality}}\textup{)},
   475	 with one bosonic generator $\gamma$ of conformal weight $h_\gamma = 1/2$.
   476	\item\label{item:fermion-kappa-dual}
   477	 Dual modular characteristic:
   478	 $\kappa(\mathcal{F}^!) = -1/4$.
   479	\item\label{item:fermion-complementarity-sum}
 succeeded in 51ms:
chapters/examples/beta_gamma.tex:1858: global all-genera content is encoded by the variation of
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5468,5495p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  5468	\index{free fermion!five-theorem verification}
  5469	Shadow archetype: G (Gaussian, $r_{\max} = 2$).
  5470	$\kappa(\mathcal{F}) = 1/4$.
  5471	Central charge $c = 1/2$.
  5472	\begin{center}
  5473	\small
  5474	\renewcommand{\arraystretch}{1.3}
  5475	\begin{tabular}{lll}
  5476	\toprule
  5477	\emph{Theorem} & \emph{Projection of $\Theta_{\mathcal{F}}$}
  5478	 & \emph{Content} \\
  5479	\midrule
  5480	A (bar-cobar) &
  5481	 $\Theta_\mathcal{F}\big|_{\hbar=0} = \tau$ &
  5482	 $\mathcal{F}^! = \mathrm{Sym}^{\mathrm{ch}}(\gamma)$ (Thm~\ref{thm:single-fermion-boson-duality}) \\
  5483	B (inversion) &
  5484	 $\Omega(\barBgeom(\mathcal{F})) \simeq \mathcal{F}$ &
  5485	 Bar collapses (Thm~\ref{thm:fermion-bar-complex-genus-0}) \\
  5486	C (complementarity) &
  5487	 $\kappa(\mathcal{F}) + \kappa(\mathcal{F}^!) = 0$ &

thinking
**Considering theorem D issues**

I’m thinking I should find out why theorem D isn’t self-contained since it references other file theorems. That in itself isn't a problem, but I wonder if there's a mismatch with AGENTS. Theorem D's statement mentions that it applies to all genera and uniform weight, which brings up questions about clarity and consistency. I need to dig deeper into this to clarify the relationships between the theorems.
codex
The next weak point is part `(iii)` of `thm:genus-universality`: the proof dismisses it with “Part (iii) is the Faber–Pandharipande evaluation,” but that external theorem only evaluates the universal Hodge integral. I’m checking whether this file ever proves the missing bridge from `\mathrm{obs}_g=\kappa\lambda_g` to `F_g=\kappa\lambda_g^{FP}` or merely assumes it.
exec
/bin/zsh -lc "rg -n \"F_g\\(|free energy|lambda_g\\"'^'"\\{FP\\}|\\psi\\"'^'"\\{2g-2\\}|define .*F_g|F_g :=|obstruction.*free energy|free energy .* obstruction\" chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4088,4196p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5006:for multi-weight algebras: the free energy receives a nonvanishing
5052:(Theorem~\ref{thm:w3-genus1-curvature}). The genus-$1$ free energy is
5359:On the scalar lane (Definition~\ref{def:scalar-lane}), the genus-$g$ free energy is $F_g = \kappa \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$,
5553:($\mathcal{W}_N$, $N \geq 3$): the free energy receives a
5579:The genus-$g$ free energy decomposes as
5582:F_g(\cA)
5629:demonstrates that the integrated free energy deviates from the
5644:\begin{remark}[Multi-generator free energy: structural diagnosis]%
5676:$F_g(\cA) = \kappa\cdot\lambda_g^{\mathrm{FP}}
5723:Indeed, the scalar formula \emph{fails}: the free energy receives
5750:at $g \geq 2$ for multi-weight algebras: the free energy receives
5781:The genus-$2$ free energy, computed as a graph sum over the seven
5827:vertex terms in the summed free energy.
5858:For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.
5876:the full higher-genus factorization \emph{fails}: the free energy
5934:$\mathrm{obs}_g(\mathcal{A}) = 0$ and $F_g(\mathcal{A}) = 0$ for all
6327:Chern--Simons benchmark lane. The genus-$g$ free energy
6328:$F_g = \kappa \cdot \lambda_g^{FP}$ is therefore a tautological
6353:F_g(\cA) \;=\; \kappa(\cA) \cdot
6358:\sum_{g \geq 1} F_g(\cA)\, x^{2g}
 succeeded in 52ms:
  4088	\]
  4089	with the curvature appearing as a central correction in $\dfib$, not as a failure
  4090	of nilpotence of $\Dg{1}$.
  4091	
  4092	The genus-1 differential satisfies:
  4093	\begin{equation}
  4094	\Dg{1}^{\,2} = 0
  4095	\end{equation}
  4096	
  4097	This requires careful cancellation between:
  4098	\begin{enumerate}
  4099	\item Genus-0 Arnold relations (exact)
  4100	\item Genus-1 corrections (from $E_2$)
  4101	\item Holomorphic anomaly compensation
  4102	\end{enumerate}
  4103	\end{theorem}
  4104	
  4105	\begin{proof}
  4106	Write $\Dg{1} = d_r + d_e + d_m$ for the residue, elliptic, and modular components. Expanding $\Dg{1}^{\,2} = (d_r + d_e + d_m)^2$ yields six terms: three diagonal ($d_r^2, d_e^2, d_m^2$) and three anticommutators ($\{d_r, d_e\}, \{d_r, d_m\}, \{d_e, d_m\}$).
  4107	
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '186,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '620,705p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   186	$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g \in
   187	H^*(\overline{\mathcal{M}}_g)$ for
   188	uniform-weight algebras, where $\lambda_g = c_g(\mathbb{E})$ is
   189	the top Chern class of the Hodge bundle; at genus~$1$ the same
   190	scalar formula is \textup{(g=1 only; all-weight at g=1 is unconditional)}
   191	for all families
   192	(Theorem~\ref{thm:genus-universality}). The generating
   193	function of these classes on the uniform-weight scalar lane is $\kappa(\cA) \cdot (\hat{A}(i\hbar) - 1)$
   194	(Theorem~\ref{thm:family-index}).
   195	
   196	The fiberwise curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ is the
   197	scalar projection of the full MC element
   198	(cf.\ Remark~\ref{rem:mc-uncurving} for the
   199	uncurving mechanism). The
   200	modular cyclic deformation complex
   201	(Definition~\ref{def:modular-cyclic-deformation-complex}) is a
   202	Maurer--Cartan family parameterized by genus~$g$ and point
   203	configurations. The universal MC element
   204	$\Theta_\cA \in \mathrm{MC}(\gAmod)$ projects, at each genus~$g$, to:
   205	the curvature~$\kappa(\cA)$ at the scalar level; the curved
 succeeded in 51ms:
   620	contracting with the OPE data of~$\cA$ extracts the
   621	self-contraction trace~$\kappa(\cA)$, giving
   622	$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$.
   623	Part~(iii): the Fay trisecant identity implies that the
   624	holomorphic part
   625	$\partial_z\!\log E$ alone satisfies the exact Arnold
   626	relation, so $\Dg{g}$ built from the holomorphic propagator
   627	squares to zero (Theorem~\ref{thm:quantum-diff-squares-zero}).
   628	Part~(iv): the scalar factorization
   629	\eqref{eq:obstruction-hodge} is Theorem~\ref{thm:genus-universality},
   630	and the generating series
   631	\eqref{eq:family-index-package} is its
   632	Grothendieck--Riemann--Roch refinement
   633	(Theorem~\ref{thm:family-index}).
   634	\end{proof}
   635	
   636	\begin{proposition}[Chain-level curvature operator; \ClaimStatusProvedHere]
   637	\label{prop:chain-level-curvature-operator}
   638	\index{curvature!chain-level operator|textbf}
   639	\index{Arakelov form!as chain representative}

thinking
**Exploring theorem connections**

I'm checking how the universal generating function relates to genus-universality (iii), noting that this part is the Faber-Pandharipande formula, so it isn't circular. However, I wonder if there's an overlooked step from `obs_g` to free energy. I should investigate around line 5579 to see how the multi-weight theorem might define free energy decomposition. Perhaps I need to find an explicit definition earlier in the file related to F_g.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5568,5595p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{def:free-energy|free energy\" chapters/theory/higher_genus_foundations.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5006:for multi-weight algebras: the free energy receives a nonvanishing
5052:(Theorem~\ref{thm:w3-genus1-curvature}). The genus-$1$ free energy is
5359:On the scalar lane (Definition~\ref{def:scalar-lane}), the genus-$g$ free energy is $F_g = \kappa \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$,
5553:($\mathcal{W}_N$, $N \geq 3$): the free energy receives a
5579:The genus-$g$ free energy decomposes as
5629:demonstrates that the integrated free energy deviates from the
5644:\begin{remark}[Multi-generator free energy: structural diagnosis]%
5723:Indeed, the scalar formula \emph{fails}: the free energy receives
5750:at $g \geq 2$ for multi-weight algebras: the free energy receives
5781:The genus-$2$ free energy, computed as a graph sum over the seven
5827:vertex terms in the summed free energy.
5858:For affine Kac--Moody $\widehat{\mathfrak{g}}_k$, the obstruction coefficient is periodic under level shift: $\kappa(\widehat{\mathfrak{g}}_{k+n}) = \kappa(\widehat{\mathfrak{g}}_k) + n \cdot d/(2h^\vee)$ for $n \in \mathbb{Z}$. In particular, the free energy $F_g$ is a linear function of $k$ with slope $\lambda_g^{FP} \cdot d/(2h^\vee)$ For $\mathcal{W}$-algebras, $\kappa$ is a rational function of $k$ (through its dependence on the DS central charge), and the periodicity statement becomes: $\kappa(\mathcal{W}^{k+n}(\mathfrak{g})) - \kappa(\mathcal{W}^k(\mathfrak{g}))$ is a rational function of $k$ with poles only at $k = -h^\vee$.
5876:the full higher-genus factorization \emph{fails}: the free energy
6327:Chern--Simons benchmark lane. The genus-$g$ free energy
 succeeded in 52ms:
  5568	(resolved)]%
  5569	\label{op:multi-generator-universality}%
  5570	\index{multi-generator obstruction!resolution|textbf}%
  5571	\index{cross-channel correction!resolution of universality|textbf}%
  5572	\textbf{Resolved negatively at genus~$\boldsymbol{2}$.}
  5573	For multi-weight families such as\/ $\mathcal{W}_N^k$ with
  5574	$N \geq 3$, the scalar formula
  5575	$\mathrm{obs}_g = \kappa \cdot \lambda_g$
  5576	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5577	receives a nonvanishing
  5578	\emph{cross-channel correction} at $g \geq 2$.
  5579	The genus-$g$ free energy decomposes as
  5580	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5581	\begin{equation}\label{eq:multi-weight-decomposition-op}
  5582	F_g(\cA)
  5583	\;=\;
  5584	\kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
  5585	\;+\;
  5586	\delta F_g^{\mathrm{cross}}(\cA),
  5587	\end{equation}









thinking
**Evaluating theorem findings**

I’m starting to assess if there’s no issue with theorems related to family-index and genus-universality. If they don't depend on each other, then there might not be a cycle. I think I should summarize that there are no findings, but also mention that the lack of circularity isn’t a finding either. Maybe I’ll output something like “Checked: 8 | Findings: X | Verdict: FAIL.” The user asked about circularity, so it may be helpful to clarify the gaps in the proof.
thinking
**Determining exact fixes**

I’m considering whether to cite line 5380 or 5394, as I see that rewriting the theorem to reflect the proven scope could be necessary. The user is asking for an exact fix, and since we can’t guarantee that a proof exists, the minimal truthful fix would be to narrow the theorem. I want to ensure I approach this responsibly and provide a clear solution that meets the user's request.
thinking
**Counting findings for accuracy**

I'm considering how many files I've actually reviewed, and it looks like I've checked 11 files total: CLAUDE, concordance, theorem_registry, and a few others. I’m thinking I might say I closely read around 8 files for accuracy. However, I’m also pondering if I should include the CLAUDE file. I know this summary doesn't need to be exact, but I want to make sure my count reflects what I've done. I'll also verify specific theorem statements next.
thinking
**Summarizing findings and conclusions**

I’m thinking about how to summarize the findings, particularly regarding the absence of any direct circularity in live proofs. I might say, “The failure is a lack of proof, not a cycle.” Since the user explicitly asked, I’m considering adding a line to my summary that reads, “Verdict: FAIL (no direct genus-universality <-> family-index loop, but genus-universality still has an unproved all-genera step).” I’ll also need to gather precise line references for each finding soon.
thinking
**Considering the theorem status**

I’m thinking that if we’re already reporting on the target theorem’s status drift, maybe the fix for the upstream theorem could involve syncing the concordance with the theorem registry. I want to ensure I mention the exact fix since it’s essential to keep everything clear. I’ll focus on how to keep this aligned within the findings related to status drift. Keeping track of these details is crucial for accuracy!
thinking
**Evaluating structural implications**

I'm noticing that some parts of the document use a proposition as if it’s foundational. This proposition includes theorem D and family-index, which appears in part (iv), but it's actually much earlier in the file. The proof of this proposition relies on a later theorem, which feels misleading and creates a structural inversion. It seems crucial to clarify this connection to avoid confusion. Let’s make sure everything aligns properly for better understanding!
thinking
**Analyzing genus-g curvature package**

I’m examining the "genus-g curvature package" labeled as `ProvedHere`. Its part (iv) references `obs_g = κ λ_g` and includes generating series, but the proof is simply citing Theorem genus-universality and family-index, lacking a clear proof. I think it might be better to separate part (iv) or retitle it as a summary remark. This adjustment will clarify things, especially since the user is looking for hidden imports and theorem statuses. I need to verify exact line numbers, too.
thinking
**Exploring genus1 universal curvature**

I’m looking into the theorem genus1-universal-curvature, specifically how it uses the universal-generating-function to define κ, which might create a circular dependency related to genus1 geometry. This theorem isn’t directly in the chain, but part (i) of genus-universality references explicit genus-1 theorems like `heisenberg-obs` and `kac-moody-obs`, which sometimes cite genus-universality themselves. I need to check the family-index theorem’s Step 2 formula for hidden issues. I might also look into the theorem `prop:complementarity-genus-series` to ensure the universal generating-function proof isn’t cyclic.
thinking
**Checking dependencies for universal-generating-function**

I want to see if the universal-generating-function depends on the family-index theorem. The proof at line 1927 relies solely on genus-universality and the complementarity genus series. I think it's worth checking the `prop:complementarity-genus-series` to confirm it’s independent and doesn’t reference the family-index. This will help clarify whether there’s an underlying dependency issue I need to worry about. Let’s investigate that to ensure everything stands independently.
codex
I’ve got the main defects. I’m doing one last pass on the generating-function lane to avoid a false positive: if `thm:universal-generating-function` is independent of `thm:family-index`, I won’t call that circular. Then I’ll consolidate the surviving findings with exact fixes.
exec
/bin/zsh -lc "rg -n \"label\\{prop:complementarity-genus-series\\}|complementarity genus series\" chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1828,1878p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1878:\begin{proposition}[Central charge genus series; \ClaimStatusProvedHere]\label{prop:complementarity-genus-series}
 succeeded in 53ms:
  1828	\subsection{Bernoulli asymptotics and convergence}\label{subsec:bernoulli-asymptotics}
  1829	
  1830	\begin{proposition}[Convergence of the genus expansion; \ClaimStatusProvedHere]\label{prop:genus-expansion-convergence}
  1831	For any fixed $\kappa \neq 0$, the genus expansion $\sum_{g=1}^\infty F_g(\cA)$ converges absolutely. More precisely:
  1832	\begin{equation}\label{eq:Fg-asymptotics}
  1833	|F_g(\cA)| \sim \frac{2|\kappa|}{(2\pi)^{2g}} \quad \text{as } g \to \infty
  1834	\end{equation}
  1835	so the series converges geometrically with ratio $1/(2\pi)^2 \approx 0.025$.
  1836	\end{proposition}
  1837	
  1838	\begin{proof}
  1839	The Bernoulli numbers satisfy the classical asymptotic formula:
  1840	\[
  1841	|B_{2g}| \sim \frac{2 \cdot (2g)!}{(2\pi)^{2g}} \quad \text{as } g \to \infty
  1842	\]
  1843	(this follows from the functional equation for the Riemann zeta function,
  1844	\[
  1845	\zeta(2g) = (-1)^{g+1} \frac{(2\pi)^{2g} B_{2g}}{2(2g)!},
  1846	\]
  1847	combined with $\zeta(2g) \to 1$). Therefore:
context compacted
codex
Auditing the full proof chain around Theorem D now. I’m re-reading the exact line ranges for each candidate finding to pin the file:line references and remove anything that does not survive a hostile re-check.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5290,5435p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2650,2750p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '500,650p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5920,6035p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5290	\hline
  5291	Virasoro $(c)$ & $\frac{c}{2} \lambda_g$ & Conformal anomaly \\
  5292	\hline
  5293	\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
  5294	\hline
  5295	\end{tabular}
  5296	\end{table}
  5297	
  5298	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5299	\index{genus universality theorem|textbf}
  5300	\textup{[Regime: curved-central on the Koszul locus; all genera
  5301	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5302	
  5303	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5304	all have the \emph{same} conformal weight. There exists a
  5305	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5306	curvature, such that \begin{equation}\label{eq:genus-universality}
  5307	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5308	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5309	\quad \text{for all } g \geq 1,
 succeeded in 52ms:
   500	H^1(\Sigma_g, \C)
   501	\;\xrightarrow{\;\text{MC}\;}
   502	Z^1(\operatorname{Def}_{\mathrm{cyc}}(\cA)_{\mathrm{model}})
   503	\;\xrightarrow{\;\text{global}\;}
   504	R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})
   505	\;\xrightarrow{\;\mathrm{tr}\;}
   506	R\Gamma(\overline{\mathcal{M}}_g, \mathbb{Q}).
   507	\]
   508	Fiber-period parameters live in $H^1(\Sigma_g,\C)$, not on moduli
   509	($H^1(\mathcal{M}_g,\mathbb{Q})=0$ for $g\geq 2$ by Harer).
   510	They become moduli classes via the Kodaira--Spencer map
   511	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
   512	\end{remark}
   513	
   514	\begin{proposition}[The genus-$g$ curvature package; \ClaimStatusProvedHere]
   515	\label{prop:genus-g-curvature-package}
   516	\index{curvature package!genus-g@genus-$g$|textbf}
   517	Let $\cA$ be a cyclic chiral algebra on a smooth projective
   518	curve~$X$ of genus~$g \geq 1$, and let
   519	$\{\omega_1,\ldots,\omega_g\}$ be the normalized abelian
 succeeded in 52ms:
  2650	modular-functor package; for $\widehat{\fg}_k$ at integrable level, $H^0(V_{g,n})$ is the
  2651	Tsuchiya--Ueno--Yamada space of conformal blocks
  2652	(Remark~\ref{rem:chain-vs-classical-mf}). The degree-$2$ projection
  2653	of $\Theta_\cA$ is the scalar $\kappa(\cA)$ that controls the
  2654	entire genus tower (the spectral discriminant~$\Delta_\cA$,
  2655	periodicity profile~$\Pi_\cA$, and full MC
  2656	class~$\Theta_\cA$ require data beyond~$\kappa$;
  2657	see Definition~\ref{def:full-modular-package}).
  2658	
  2659	\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
  2660	\label{thm:modular-characteristic}
  2661	\index{modular characteristic theorem|textbf}
  2662	\index{kappa@$\kappa$!as first characteristic number|textbf}
  2663	\textup{[}Regime: curved-central
  2664	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  2665	
  2666	Let $\cA$ be a modular Koszul chiral algebra
  2667	(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
  2668	characteristic package
  2669	(Definition~\ref{def:scalar-modular-package}) is controlled by one
 succeeded in 52ms:
  5920	
  5921	The appearance of the $\hat{A}$-genus in the Heisenberg genus
  5922	expansion (Theorem~\ref{thm:universal-generating-function})
  5923	and the Bernoulli asymptotics of $F_g(\cA)$ are not coincidental:
  5924	they are the output of a Grothendieck--Riemann--Roch computation
  5925	on the universal curve.
  5926	
  5927	\begin{theorem}[Family index theorem for genus expansions;
  5928	\ClaimStatusProvedHere]\label{thm:family-index}
  5929	\index{index theorem!modular deformation|textbf}
  5930	\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
  5931	Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
  5932	$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
  5933	\overline{\mathcal{M}}_g$ be the universal curve with relative
  5934	dualizing sheaf~$\omega_\pi$, and let
  5935	$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
  5936	The following holds for uniform-weight modular Koszul algebras
  5937	at all genera; the genus-$1$ statements are unconditional for
  5938	all families, including multi-generator.
  5939	Define the \emph{modular deformation complex} of~$\cA$ at genus~$g$ by
codex
I’ve narrowed the live defects to the proof-bearing lines now. I’m checking the cited downstream theorems and registry/concordance surfaces so the fixes point to the exact wrong dependency, not a paraphrase.
exec
/bin/zsh -lc 'rg -n "cor:kappa-additivity|thm:anomaly-koszul|thm:wn-obstruction|cor:general-w-obstruction|thm:modular-characteristic|thm:genus-universality|thm:family-index" chapters metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 370

metadata/theorem_registry.md:827:| `thm:genus-universality` | `theorem` | 5243 | Genus universality |
metadata/theorem_registry.md:832:| `cor:kappa-additivity` | `corollary` | 5806 | Additivity of the obstruction coefficient |
metadata/theorem_registry.md:878:| `thm:modular-characteristic` | `theorem` | 2543 | Modular characteristic |
metadata/theorem_registry.md:1839:| `thm:wn-obstruction` | `theorem` | 2173 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
metadata/theorem_registry.md:1841:| `cor:general-w-obstruction` | `corollary` | 2306 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
metadata/theorem_registry.md:2369:| `thm:family-index` | `theorem` | 5769 | Family index theorem for genus expansions |
metadata/theorem_registry.md:2414:| `thm:anomaly-koszul` | `theorem` | 1864 | Anomaly cancellation as Koszul constraint |
chapters/examples/w_algebras_deep.tex:2646:propagator (Theorem~\ref{thm:genus-universality}).
chapters/examples/w_algebras_deep.tex:4075:Theorem~\ref{thm:wn-obstruction}). Diagonality of the
chapters/examples/w_algebras_deep.tex:4081:= c(H_N - 1)$ recovers Theorem~\ref{thm:wn-obstruction}.
chapters/examples/symmetric_orbifolds.tex:13:(Corollary~\ref{cor:kappa-additivity}) and the fact that twisted
chapters/examples/lattice_foundations.tex:1138: and Corollary~\ref{cor:kappa-additivity}),
chapters/examples/beta_gamma.tex:1225:(Theorem~\ref{thm:genus-universality}), the genus-$g$ curvature
chapters/examples/landscape_census.tex:34:theorem (Theorem~\ref{thm:genus-universality}), a pattern visible
chapters/examples/landscape_census.tex:50:(Theorem~\ref{thm:genus-universality};
chapters/examples/landscape_census.tex:661:(Theorem~\ref{thm:genus-universality}; );
chapters/examples/landscape_census.tex:1077:(see Theorem~\ref{thm:genus-universality}(ii)).
chapters/examples/landscape_census.tex:1195:The Faber--Pandharipande $\lambda_g$ formula (Theorem~\ref{thm:genus-universality}(iii))
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '1835,1905p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '6340,6425p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2160,2325p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1835	Lie algebras~\cite{BarNatan95}.
  1836	\end{proof}
  1837	
  1838	\begin{remark}[Scope]\label{rem:vassiliev-scope}
  1839	Proposition~\ref{prop:vassiliev-genus0} establishes the genus-$0$
  1840	weight system extraction. The Feynman transform of $\mathrm{Com}$
  1841	recovers the full graph complex computing Vassiliev invariants
  1842	(Getzler--Kapranov \cite{GeK98}), and our identification
  1843	$\barB^{\mathrm{full}} \simeq \mathrm{FT}$
  1844	(Theorem~\ref{thm:prism-higher-genus}) extends this to Koszul
  1845	chiral algebras. The gap at higher genus is the passage from
  1846	complex curves to real $1$-manifolds: our propagators are
  1847	holomorphic, while Kontsevich's are real. Comparing requires an
  1848	analytic continuation argument from holomorphic to topological
  1849	Feynman transforms.
  1850	The correct bridge between holomorphic and topological frameworks is Chern--Simons gauge equivalence, not merely restriction from complex curves to $S^1$: Cattaneo--Mnev~\cite{CattaneoMnev10} establish that configuration space integrals on $3$-manifolds produce Vassiliev invariants via BV integration, and the comparison map involves the CS partition function (not a pointwise restriction of propagators).
  1851	
  1852	\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
  1853	The conjecture asserts that the dg Lie algebras controlling
  1854	holomorphic (chiral bar) and topological (Kontsevich integral)
 succeeded in 52ms:

 succeeded in 51ms:
  2160	
  2161	\subsection{\texorpdfstring{General $\mathcal{W}_N$: obstruction coefficient formula}{General WN: obstruction coefficient formula}}
  2162	\label{sec:wn-obstruction}
  2163	\index{obstruction coefficient!general W_N@general $\mathcal{W}_N$}
  2164	
  2165	The Virasoro ($N = 2$) and $\mathcal{W}_3$ ($N = 3$) genus-1 pipelines
  2166	reveal a pattern in the obstruction coefficients: $\kappa = c/2$ and
  2167	$\kappa = c/2 + c/3 = 5c/6$ respectively, with each generator
  2168	contributing its own vacuum leakage. The general formula
  2169	for all $N$ validates the Master Table entry
  2170	(Table~\ref{tab:master-invariants}).
  2171	
  2172	\begin{theorem}[Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN}; \ClaimStatusProvedHere]
  2173	\label{thm:wn-obstruction}
  2174	For the principal $\mathcal{W}$-algebra
  2175	$\mathcal{W}_N^k = \mathcal{W}^k(\mathfrak{sl}_N, f_{\mathrm{prin}})$
  2176	at generic level $k \neq -N$, the genus-1 obstruction coefficient is:
  2177	\begin{equation}\label{eq:wn-kappa}
  2178	\kappa(\mathcal{W}_N^k) = c \sum_{s=2}^{N} \frac{1}{s}
  2179	= c \cdot (H_N - 1)
codex
The theorem surfaces are enough to show the logic defects. I’m checking the registry and one more dependency seam now, mainly to distinguish a real proof gap from a mere documentation mismatch.
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1905,1935p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6168,6235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '250,380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '820,885p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1905	the genus expansion is the Gro\-then\-dieck--Rie\-mann--Roch pushforward of
  1906	the Todd class of the universal curve, and $(x/2)/\sin(x/2)$ is the
  1907	even part of the Wick-rotated Todd class. The positivity of all coefficients
  1908	($\lambda_g^{\mathrm{FP}} > 0$ for all~$g$), in contrast to the
  1909	alternating-sign $\hat{A}$-expansion, reflects the Hodge index
  1910	theorem on $\overline{\mathcal{M}}_g$.
  1911	\end{remark}
  1912	
  1913	\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
  1914	\index{genus expansion!universal generating function}
  1915	\index{obstruction coefficient!generating function}
  1916	For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
  1917	weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
  1918	\begin{equation}\label{eq:universal-generating-function}
  1919	\sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
  1920	\end{equation}
  1921	with radius of convergence $|x| = 2\pi$, independent of $\mathcal{A}$.
  1922	For arbitrary modular Koszul algebras, the genus-$1$ coefficient
  1923	still satisfies $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
  1924	\end{theorem}
 succeeded in 51ms:
  6168	$\Theta_{\cA}$: it computes how the universal MC element
  6169	distributes its weight across genera. The Bernoulli numbers
  6170	appear because they are the Taylor coefficients of
  6171	$\operatorname{tr}(\Theta)$, not because of any formal group
  6172	coincidence. The formal group is additive because $\kappa$
  6173	itself is additive under tensor product
  6174	(Corollary~\ref{cor:kappa-additivity}), which in turn follows
  6175	from $\Theta_{\cA \otimes \cB} = \Theta_{\cA} + \Theta_{\cB}$
  6176	in the factorization algebra sense.
  6177	\end{remark}
  6178	
  6179	\begin{remark}[Scalar free energy package]
  6180	\label{rem:concordance-scalar-free-energy}
  6181	\index{free energy!concordance summary}
  6182	Corollary~\ref{cor:free-energy-ahat-genus} assembles
  6183	the scalar content of Theorem~D into a single formula:
  6184	$F(\cA;\hbar) = (\kappa/\hbar^2)\bigl[\hat{A}(i\hbar)-1\bigr]$
  6185	with $\hat{A}(ix) = (x/2)/\sin(x/2)$, convergent for
  6186	$|\hbar|<2\pi$, and admitting the infinite product
  6187	$(\hbar/2)/\sin(\hbar/2) = \prod_{n \geq 1}
 succeeded in 51ms:
   250	 for all $r \geq 2$.
   251	\end{enumerate}
   252	\end{proposition}
   253	
   254	\begin{proof}
   255	\eqref{item:fermion-kappa}:
   256	The free fermion has central charge $c = 1/2$ (a single real
   257	fermion of weight $h = 1/2$; standard from the Virasoro commutation
   258	relations).
   259	Then $\kappa = c/2 = 1/4$ by the universal formula
   260	$\kappa = c \cdot \rho$ with $\rho = 1/2$ for single-generator algebras
   261	(Theorem~\ref{thm:modular-characteristic}).
   262	
   263	\eqref{item:fermion-S3}:
   264	The cubic shadow $S_3$ is the degree-$3$ projection of
   265	$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
   266	element requires three fermion insertions on a three-point configuration
   267	space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
   268	is totally antisymmetric in labels. The cyclic permutation
   269	$(123) \mapsto (231)$ on $\overline{C}_3(X)$ acts on the logarithmic
 succeeded in 51ms:
   820	| `thm:heisenberg-obs` | `theorem` | 4725 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
   821	| `thm:kac-moody-obs` | `theorem` | 4807 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
   822	| `thm:w3-obstruction` | `theorem` | 4927 | \texorpdfstring{$W_3$}{W3} fiberwise obstruction |
   823	| `comp:w3-obs-explicit` | `computation` | 4988 | Explicit genus-$1$ value of the $W_3$ obstruction |
   824	| `thm:obstruction-nilpotent` | `theorem` | 5010 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
   825	| `thm:obstruction-nilpotent-all-genera` | `theorem` | 5039 | Nilpotence of obstruction (all genera) |
   826	| `cor:mumford-multiplicative` | `corollary` | 5127 | Mumford multiplicative relations for obstruction classes |
   827	| `thm:genus-universality` | `theorem` | 5243 | Genus universality |
   828	| `prop:multi-generator-obstruction` | `proposition` | 5652 | Multi-generator edge universality |
   829	| `prop:f2-quartic-dependence` | `proposition` | 5700 | Genus-$2$ quartic dependence |
   830	| `cor:anomaly-ratio` | `corollary` | 5761 | Anomaly ratio identity |
   831	| `cor:kappa-periodicity` | `corollary` | 5777 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
   832	| `cor:kappa-additivity` | `corollary` | 5806 | Additivity of the obstruction coefficient |
   833	| `cor:kappa-sum-wn` | `corollary` | 5827 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
   834	| `cor:critical-level-universality` | `corollary` | 5850 | Universal genus-$1$ criticality criterion; scalar-lane collapse |
   835	| `cor:tautological-class-map` | `corollary` | 5886 | Tautological class map on the scalar lane; universal genus-$1$ class |
   836	| `prop:bar-tautological-filtration` | `proposition` | 6010 | Bar spectral sequence and tautological filtration |
   837	| `thm:koszul-k0` | `theorem` | 6082 | Grothendieck group of Koszul chiral algebras |
   838	| `thm:obs-def-pairing-explicit` | `theorem` | 6112 | Obstruction-deformation pairing |
   839	| `prop:obstruction-lifting` | `proposition` | 6213 | Scalar obstruction lifting criterion |

thinking
**Inspecting lines for fixes**

I think I need to look at the cor:kappa-additivity lines and the critical-level universality lines to find the exact fix. There's a search around 5806 that I should check out. It's important to ensure that everything aligns correctly—so I'll spend some time examining these lines deeply. Hopefully, that will lead to a clear solution! Let’s see what I can uncover.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5795,5865p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '300,325p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5718,5788p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4688,4720p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5795	(at genus~$2$ or~$1$), $1$, $2$, $3$, or~$4$ from edges plus
  5796	markings. Only the banana has a genus-$0$ vertex of
  5797	valence~$4$, giving vertex factor~$S_4$.
  5798	The banana amplitude is
  5799	$\frac{1}{8}\,S_4 \cdot P^2 = \frac{S_4}{8\kappa^2}$
  5800	(since $P = 1/\kappa$),
  5801	confirming~\eqref{eq:f2-quartic-dep}.
  5802	\end{proof}
  5803	
  5804	\begin{remark}[Multi-channel resolution]%
  5805	\label{rem:multichannel-resolution}%
  5806	\index{multi-generator obstruction!multi-channel resolution}%
  5807	For a multi-generator algebra $\mathcal{W}_N$ with
  5808	$\kappa = \sum_{s=2}^N \kappa_s$, the \emph{total} quartic
  5809	$S_4^{\mathrm{total}} \neq S_4^{\mathrm{Vir}}(\kappa)$:
  5810	the $\mathcal{W}$-channel and mixed OPE contributions shift~$S_4$
  5811	away from the Virasoro value at the same~$\kappa$.
  5812	The scalar graph sum therefore gives
  5813	$F_2 \neq \kappa \cdot \lambda_2^{\mathrm{FP}}$
  5814	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}.
 succeeded in 53ms:
   300	\ClaimStatusProvedHere
   301	\index{four-test interface|textbf}
   302	The modular Koszul machine has a complete interface with
   303	$\overline{\mathcal{M}}_{g,n}$, consisting of four
   304	independent proved tests:
   305	\textup{(1)}~$D_\cA^2 = 0$ at all genera and degrees
   306	\textup{(}Theorems~\textup{\ref{thm:bar-modular-operad},
   307	\ref{thm:quantum-diff-squares-zero}}\textup{)};
   308	\textup{(2)}~$\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$
   309	for uniform-weight algebras at all genera,
   310	unconditionally at genus~$1$
   311	\textup{(}Theorem~\textup{\ref{thm:modular-characteristic}}\textup{)};
   312	\textup{(3)}~$Q_g(\cA)+Q_g(\cA^!)=H^*(\overline{\mathcal M}_g,\cZ_\cA)$:
   313	complementarity assembles the Koszul pair into a Lagrangian
   314	decomposition
   315	\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)};
   316	\textup{(4)}~sewing: genus-$g$ amplitudes converge from lower-genus data
   317	\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
   318	\end{remark}
   319	
 succeeded in 55ms:
  5718	OPE structure constants that are not controlled by~$\kappa$ alone.
  5719	Scalar saturation ($\dim H^2_{\mathrm{cyc}} = 1$) fixes the
  5720	$H^2$~direction to~$\eta$ but does not determine which
  5721	$\overline{\mathcal{M}}_g$~class appears at genus~$g$, since
  5722	the Kuranishi map vanishes by parity.
  5723	Indeed, the scalar formula \emph{fails}: the free energy receives
  5724	a cross-channel correction
  5725	(Open Problem~\ref{op:multi-generator-universality}, resolved
  5726	negatively; Theorem~\ref{thm:multi-weight-genus-expansion}).
  5727	\end{enumerate}
  5728	\end{remark}
  5729	
  5730	\begin{proposition}[Multi-generator edge universality; \ClaimStatusProvedHere]
  5731	\label{prop:multi-generator-obstruction}
  5732	\index{multi-generator obstruction}
  5733	Let $\cA$ be a modular Koszul chiral algebra with strong generators
  5734	of conformal weights $h_1, \ldots, h_r$.
  5735	\begin{enumerate}[label=\textup{(\alph*)}]
  5736	\item At genus~$1$,
  5737	$\mathrm{obs}_1(\cA) = \kappa(\cA) \cdot \lambda_1$
 succeeded in 53ms:
  4688	
  4689	The modular characteristic theorem (Theorem~D,
  4690	Theorem~\ref{thm:modular-characteristic}) establishes the scalar
  4691	logarithmic datum~$\kappa(\cA)$. This section identifies the six
  4692	components (five structural extensions and the Hochschild
  4693	cohomology theorem) needed to pass from the proved modular Koszul
  4694	core to modular homotopy theory for factorization algebras on
  4695	curves; that is, to complete the nilpotence-periodicity
  4696	correspondence
  4697	(Remark~\ref{rem:nilpotence-periodicity}) from the scalar level to
  4698	the full categorical level:
  4699	
  4700	\begin{center}
  4701	\renewcommand{\arraystretch}{1.3}
  4702	\begin{tabular}{@{}cp{4.4cm}p{3.8cm}p{4.6cm}@{}}
  4703	\toprule
  4704	\textbf{Label} & \textbf{Statement} & \textbf{Status} & \textbf{Reference} \\
  4705	\midrule
  4706	$A_{\mathrm{mod}}$ & Bar-cobar intertwined with Verdier, & \textbf{Proved} & Thm~\ref{thm:bar-cobar-isomorphism-main} \\
  4707	 & functorial over $\overline{\mathcal{M}}_{g,n}$ & & \\[2pt]

thinking
**Considering theorem inspection**

I might think about whether to include concordance status, but I’m not sure if it’s necessary. I should look into the theorem_registry and see if there’s a status claim. If there’s a mismatch, it could be worth mentioning registry lines. But then again, the theorem_registry just seems to be a label list without status. I think checking the cor:kappa-additivity lines for exact location is a critical step.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5860,5905p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  5860	
  5861	\begin{proof}
  5862	For KM: $\kappa = (k+h^\vee)d/(2h^\vee)$, which is linear in $k$ with slope $d/(2h^\vee)$. Level shift $k \to k+n$ adds $nd/(2h^\vee)$.
  5863	\end{proof}
  5864	
  5865	\begin{remark}[Universality principle]\label{rem:lambda-universality}
  5866	For algebras with generators of the same conformal weight
  5867	(Heisenberg, Virasoro, Kac--Moody), the factorization
  5868	$\mathrm{obs}_g = \kappa \cdot \lambda_g$ and the free-energy
  5869	formula $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ hold unconditionally at all genera. For multi-generator
  5870	algebras ($\mathcal{W}_N$, $N \geq 3$),
  5871	the genus-$1$ identity $F_1 = \kappa/24$
  5872	\textup{(g=1 only; all-weight at g=1 is unconditional)} is unconditional,
  5873	and the edge-level universality
  5874	(Remark~\ref{rem:propagator-weight-universality})
  5875	constrains the higher-genus structure;
  5876	the full higher-genus factorization \emph{fails}: the free energy
  5877	receives a cross-channel correction $\delta F_g^{\mathrm{cross}} \neq 0$
  5878	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5879	(Open Problem~\ref{op:multi-generator-universality}, resolved





thinking
**Evaluating theorem circularity**

I need to check aspects around the multi-weight theorem, but it might not be necessary. Including a part in Theorem D regarding conditionals seems sufficient. I can criticize the proof gap, especially considering the user explicitly asked about potential circularity. While there's likely no direct cycle, the proof chain still fails. I should summarize by noting that there's no direct theorem-theorem cycle found, highlighting the failure as an uncited uniqueness jump, as the user requested clarity on cited results.
thinking
**Structuring findings and summary**

The output should focus on findings and a summary, including maybe just the counts initially. It could also mention, “No direct circularity found,” but that might complicate the format the user specified. Despite that, I could add a concise extra sentence under the summary if needed. For counting, I might define N as the number of theorem surfaces or files checked, suggesting something like, “Checked: 9 | Findings: 8 | Verdict: FAIL.” I want to ensure I don't include any false positives among the findings!
thinking
**Analyzing proof claims**

If the family-index isn't well-defined, I can still draw on the universal-generating-function for the proof claim regarding the generating function. However, only part (ii) is safe if the theorem for the universal-generating-function is established via part (iii) of genus-universality. Part (iii) refers to the Faber-Pandharipande formula, which remains unaffected by the family-index concerns. I should note that the genus-universality theorem's part (iii) asserts that F_g = kappa * FP numbers on the scalar lane, relying on the Mumford formula for its proof.
thinking
**Considering citation clarity**

I need to think about how to present citations clearly. If the user asks whether each cited result is proven, I might need to adjust my response accordingly. It seems I should focus on listing only the problems in my final answer, while possibly clarifying that the findings about citations being proven may need to be included when they are acceptable. There’s a lot to keep in mind here!
thinking
**Investigating proofs further**

I’m wondering if there's more to uncover here. I think I might need to read the continuation of the family-index proof beyond 6035, so I'll inspect that. I wonder if the universal-generating-function proof is also valid. I definitely want to check the rest of the family-index proof to catch any potential issues. Plus, I should examine the theorem on genus-universality beyond its proof. Let’s take a closer look at the continuation starting from 6035.
codex
I found a real proof gap, not a cosmetic one. I’m reading the rest of the GRR proof now to see whether the manuscript quietly patches it later or compounds it with additional unsupported K-theory claims.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6035,6115p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Wick-rotated by the positivity|kappa\\(\\\\cA\\) \\\\cdot \\\\mathbb\\{E\\}|Theorem~\\\\ref\\{thm:family-index\\} is only the|does not invoke Theorem~\\\\ref\\{thm:family-index\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6235,6315p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6035	\emph{Step~2: Mumford's GRR computation.}
  6036	By Grothendieck--Riemann--Roch applied to the universal curve
  6037	$\pi \colon \overline{\mathcal{C}}_g \to \overline{\mathcal{M}}_g$
  6038	and the relative dualizing sheaf~$\omega_\pi$:
  6039	\begin{equation}\label{eq:mumford-grr}
  6040	\operatorname{ch}(\mathbb{E})
  6041	\;=\;
  6042	\operatorname{ch}(R^0\pi_*\omega_\pi)
  6043	\;=\;
  6044	1 + \pi_*\!\left(
  6045	 \operatorname{ch}(\omega_\pi) \cdot
  6046	 \operatorname{Td}(T_\pi)
  6047	\right),
  6048	\end{equation}
  6049	
  6050	Serre duality on the fibers gives
  6051	$R^1\pi_*\omega_\pi \cong (R^0\pi_*\mathcal{O})^\vee \cong \mathcal{O}$,
  6052	so $\operatorname{ch}(R\pi_*\omega_\pi) = \operatorname{ch}(\mathbb{E}) - 1$.
  6053	
  6054	Write $K = c_1(\omega_\pi)$ for the relative canonical class. Since
 exited 2 in 52ms:
rg: regex parse error:
    (?:Wick-rotated by the positivity|kappa\(\cA\) \cdot \mathbb\{E\}|Theorem~\ref\{thm:family-index\} is only the|does not invoke Theorem~\ref\{thm:family-index\})
                                             ^^
error: unrecognized escape sequence
 succeeded in 54ms:
  6235	\begin{example}[Heisenberg pairing]\label{ex:heisenberg-pairing}
  6236	For the Heisenberg algebra $\mathcal{H}_\kappa$:
  6237	\begin{align}
  6238	\text{obs}_g &= \kappa \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g)
  6239	\qquad \\
  6240	\text{def}_g &\in H^{4g-6}(\overline{\mathcal{M}}_g)
  6241	\end{align}
  6242	
  6243	The degrees are complementary under Poincar\'e duality: $\dim_{\mathbb{R}}(\overline{\mathcal{M}}_g) = 6g - 6$, so $H^{2g}$ pairs with $H^{6g-6-2g} = H^{4g-6}$.
  6244	
  6245	\emph{Note:} The deformation degree is $4g - 6$.
  6246	At $g = 1$, $4g - 6 = -2 < 0$, so $\text{def}_1 = 0$:
  6247	the genus-$1$ obstruction is uncompensated.
  6248	At $g = 2$, $\text{def}_2 \in H^2(\overline{\mathcal{M}}_2)$
  6249	(a $3$-dimensional space).
  6250	At $g = 3$, $\text{def}_3 \in H^6(\overline{\mathcal{M}}_3) = H^{\mathrm{top}} \cong \mathbb{C}$, so the deformation is a scalar.
  6251	For $g \geq 2$, the Poincar\'e duality pairing couples
  6252	$\text{obs}_g$ with $\text{def}_g$:
  6253	\begin{align}
  6254	\langle \text{obs}_g, \text{def}_g \rangle &= \int_{\mathcal{M}_g} (\kappa \cdot \lambda_g)
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6110,6135p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6110	\begin{align}
  6111	\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
  6112	&\;=\;
  6113	\sum_{g \geq 1}
  6114	\frac{2^{2g-1}-1}{2^{2g-1}} \cdot
  6115	\frac{|B_{2g}|}{(2g)!}\, x^{2g}
  6116	\notag \\
  6117	&\;=\;
  6118	\frac{x/2}{\sin(x/2)} - 1
  6119	\;=\; \hat{A}(ix) - 1,
  6120	\label{eq:bernoulli-a-hat}
  6121	\end{align}
  6122	where the second equality is the classical identity
  6123	$t/\sin t = \sum_{n \geq 0}
  6124	\frac{(2^{2n}-2)\,|B_{2n}|}{(2n)!}\,t^{2n}$
  6125	evaluated at $t = x/2$ (equivalently, the even part of
  6126	the Wick-rotated Todd class).
  6127	Multiplying by $\kappa(\cA)$ gives~(ii).
  6128	
  6129	The positivity of all coefficients









thinking
**Considering output findings**

I see that the output can be lengthy but still manageable. I wonder if we could include extra findings for every downstream advertisement, given that the user wants an exhaust surface. We can't literally exhaust the repository, but perhaps we could limit it to an audit surface. Yet, AGENTS mentions cross-volume. Maybe it's best to focus on the key downstream surfaces only. There's a lot to think about here!
thinking
**Clarifying output format**

I should mention that the same defect recurs at higher_genus_foundations.tex:594. Ideally, I want to keep the output format concise, using one line to reference multiple lines separated by commas, like this: "higher_genus_foundations.tex:5312,594". But wait, line 594 is in the same file, so I should just point out that it's higher_genus_foundations.tex:594 to be clear.
thinking
**Clarifying theorem issues**

I'm exploring a potential issue with Theorem D part (ii), which states that the generating function retrieves the $\hat A$-genus as the topological generating function with uniform weight. I'm checking lines 2695-2696, where the universal-generating-function theorem mentions uniform conformal weight. I need to understand if there is any confusion or ambiguity there, as these concepts can be quite intricate. Let's see if I can resolve this!
thinking
**Considering theorem gaps**

I’m recognizing that there’s a proof gap in the theorem for all genera, but the genus-1 part holds up well. However, since part (iv) of Theorem D relies on genus-1 additivity, I wonder if there might be an issue if cor:additivity isn't independent of the chain in Theorem D. That said, it seems likely to be okay. For now, I think I can set that concern aside.
thinking
**Reviewing citations**

I checked the files and counted a total of 9: target, foundations, concordance, genus_expansions, editorial_constitution, w_algebras, theorem_registry, guide_to_main_results, and free_fields. Yes, 9 files confirmed! The user specifically asked for line citations, which is important. I want to ensure my final answer is concise and includes all the relevant findings while delivering exactly what the user needs.
thinking
**Considering mathematical fixes**

I'm pondering the extension obs_g = kappa lambda_g for g>=2, which feels conjectural. Adjusting part (iii) similarly for genus-1 could be drastic, but perhaps necessary since there might be evidence for all genera via other theorems. 

I thought about inserting a new proposition about the uniqueness of the scalar Hodge class, but it lacks precision. The user needs an actionable fix, so I aim to refine the statement to its supported scope better. I'm getting ready to craft more precise modifications.
thinking
**Refining mathematical claims**

I'm considering replacing `for all g ≥ 1` with `for g = 1`. If I want to maintain a higher-genus claim, I might need to categorize it as conjectural or conditional and reference a strong scalar ansatz, but that applies to multi-generator cases, not uniform-weight. 

I think I should split the theorem into a proved genus-1 theorem and a separate conjecture on `all-genera-uniform-weight`. 

For example, I can articulate that there exists a scalar κ(A) defined by the genus-1 curvature, leading to a more accurate representation of the theorem and correcting the structure without being overly drastic.
thinking
**Exploring proposition possibilities**

I'm wondering about the existing proposition `prop:grr-bridge` at 6285, which discusses the "GRR bridge on the proved uniform-weight scalar lane." Could this potentially salvage the situation? I haven't read it yet, so I should inspect whether it establishes any uniqueness theorems.

However, since the user requested a foundational audit of the target file, if there's a way to salvage it later, that might not be an issue. I think I should search for definitions related to the "proved uniform-weight scalar lane" or similar terms.
thinking
**Investigating mathematical propositions**

I need to check if any propositions after 6285 clarify the uniqueness aspect. The line in the theorem registry mentions `prop:grr-bridge`, which seems connected to a "GRR bridge on the proved uniform-weight scalar lane" possibly built on a theorem. I should search for terms like "scalar lane" or "clutching maps for Hodge bundle force." However, there's also a possibility of checking the `cor:tautological-class-map` theorem around 6285 and maybe even 5886.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5883,5905p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6285,6335p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6285	\item If $\kappa \neq 0$, the scalar obstruction classes
  6286	 $\mathrm{obs}_g(\cA)$ are nonzero for every genus $g \geq 1$;
  6287	\item If $\kappa = 0$, the scalar obstruction classes vanish for all
  6288	 genera on the proved scalar lane.
  6289	\end{enumerate}
  6290	For arbitrary modular Koszul algebras, the universal genus-$1$
  6291	criterion $\mathrm{obs}_1(\cA) = 0 \iff \kappa(\cA) = 0$
  6292	\textup{(g=1 only; all-weight at g=1 is unconditional)} remains
  6293	valid. This does not identify the full higher-degree tower.
  6294	\end{proposition}
  6295	
  6296	\begin{proof}
  6297	On the proved scalar lane, Theorem~\ref{thm:genus-universality} gives
  6298	$\mathrm{obs}_g = \kappa \cdot \lambda_g$ with
  6299	$\lambda_g \neq 0$ for all $g \geq 1$.
  6300	Thus $\mathrm{obs}_g = 0$ for some $g$ iff $\kappa = 0$ iff
  6301	$\mathrm{obs}_g = 0$ for all $g$ on that scalar lane. For arbitrary
  6302	modular Koszul algebras, the universal genus-$1$ identity
  6303	$\mathrm{obs}_1 = \kappa \cdot \lambda_1$
  6304	\textup{(g=1 only; all-weight at g=1 is unconditional)} gives
 succeeded in 52ms:
  5883	\begin{corollary}[Additivity of the obstruction coefficient; \ClaimStatusProvedHere]\label{cor:kappa-additivity}
  5884	\index{obstruction coefficient!additivity}
  5885	For Koszul chiral algebras $\mathcal{A}$, $\mathcal{B}$ such that $\mathcal{A} \otimes \mathcal{B}$ is Koszul:
  5886	\begin{equation}\label{eq:kappa-additivity}
  5887	\kappa(\mathcal{A} \otimes \mathcal{B}) = \kappa(\mathcal{A}) + \kappa(\mathcal{B}).
  5888	\end{equation}
  5889	In particular, on the proved scalar lane,
  5890	$\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ for all $g \geq 1$.
  5891	\end{corollary}
  5892	
  5893	\begin{proof}
  5894	The singular part of the OPE of $\mathcal{A} \otimes \mathcal{B}$ is the sum of the singular parts of $\mathcal{A}$ and $\mathcal{B}$ (the tensor product acts on disjoint sets of fields). The genus-$1$ curvature, which determines $\kappa$ by Theorem~\ref{thm:genus-universality}, is therefore additive. Since the Faber--Pandharipande integral $\lambda_g^{\mathrm{FP}}$ is linear in $\kappa$, the factorization~\eqref{eq:genus-universality} gives $\mathrm{obs}_g(\mathcal{A} \otimes \mathcal{B}) = (\kappa(\mathcal{A}) + \kappa(\mathcal{B})) \cdot \lambda_g = \mathrm{obs}_g(\mathcal{A}) + \mathrm{obs}_g(\mathcal{B})$ \end{proof}
  5895	
  5896	\begin{example}
  5897	For a rank-$d$ lattice vertex algebra $V_\Lambda = \mathcal{H}_1^{\otimes d}$, additivity gives $\kappa(V_\Lambda) = d \cdot \kappa(\mathcal{H}_1) = d$, confirming the Master Table entry (Table~\ref{tab:master-invariants}). For the $bc$--$\beta\gamma$ system, $\kappa(bc \otimes \beta\gamma) = c/2 + (-c/2) = 0$ (since $\kappa(\beta\gamma) = -\kappa(bc)$ by Theorem~\ref{thm:fermion-all-genera}).
  5898	\end{example}
  5899	
  5900	\begin{corollary}[Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)}; \ClaimStatusProvedHere]
  5901	\label{cor:kappa-sum-wn}
  5902	\index{obstruction coefficient!W-algebra complementarity}

thinking
**Considering theorems and proofs**

I'm thinking about the potential issues with the theorem, especially concerning the `થm:genus-universality` section. It raises a red flag for me, particularly since it references the Faber-Pandharipande formula. The proof line 5430 refers back to the Mumford formula, and I wonder how that all connects. It seems there might be foundational discrepancies here that we need to scrutinize further. I want to make sure everything aligns correctly going forward!
codex
The GRR layer makes the main failure worse, not better: it reifies the unsupported scalar factorization into a fake K-theory object. I’m doing one last pass on the Faber–Pandharipande citation so the chain from `obs_g = κ λ_g` to the generating series is fully pinned down.
exec
/bin/zsh -lc 'rg -n "thm:mumford-formula|mumford-formula" chapters/theory/higher_genus_foundations.tex chapters/examples/genus_expansions.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4528,4565p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/higher_genus_foundations.tex:4539:\label{thm:mumford-formula}
chapters/theory/higher_genus_foundations.tex:5431:(Theorem~\ref{thm:mumford-formula}).
chapters/theory/higher_genus_foundations.tex:6380:(Theorem~\ref{thm:mumford-formula}):
chapters/connections/concordance.tex:6085:(Theorem~\ref{thm:mumford-formula}) evaluates the
chapters/examples/genus_expansions.tex:39:(Theorem~\ref{thm:mumford-formula}). The secondary Borcherds
chapters/examples/genus_expansions.tex:124:(Theorem~\ref{thm:mumford-formula}).
chapters/examples/genus_expansions.tex:319:(Theorem~\ref{thm:mumford-formula}) evaluates
chapters/examples/genus_expansions.tex:498:The Faber--Pandharipande formula (Theorem~\ref{thm:mumford-formula}) evaluates the integral:
chapters/examples/genus_expansions.tex:2125:By the genus universality theorem (Theorem~\ref{thm:genus-universality}) with $\kappa(\mathrm{Vir}_c) = c/2$ (Theorem~\ref{thm:vir-genus1-curvature}) and the Faber--Pandharipande formula (Theorem~\ref{thm:mumford-formula}).
chapters/examples/genus_expansions.tex:2419:(Theorem~\ref{thm:mumford-formula}) evaluates the
chapters/examples/genus_expansions.tex:2726:(Theorem~\ref{thm:mumford-formula}).
 succeeded in 50ms:
  4528	\end{equation}
  4529	the space of holomorphic differentials.
  4530	
  4531	The Chern classes:
  4532	\begin{equation}
  4533	\lambda_i = c_i(\mathbb{E}) \in H^{2i}(\overline{\mathcal{M}}_{g,n}, \mathbb{Q})
  4534	\end{equation}
  4535	are the \emph{$\lambda$-classes}. (The \emph{Mumford--Morita--Miller classes} $\kappa_i = \pi_*(\psi_{n+1}^{i+1}) \in H^{2i}(\overline{\mathcal{M}}_{g,n})$ are related but distinct: they are pushforwards of powers of the universal cotangent class.)
  4536	\end{definition}
  4537	
  4538	\begin{theorem}[Faber--Pandharipande $\lambda_g$ formula {\cite{FP03}}; \ClaimStatusProvedElsewhere]
  4539	\label{thm:mumford-formula}
  4540	\index{Faber--Pandharipande formula}
  4541	The top $\lambda$-class, paired with the appropriate $\psi$-class, evaluates to \textup{(LOCAL)}:
  4542	\begin{equation}\label{eq:faber-pandharipande}
  4543	\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}
  4544	\end{equation}
  4545	where $B_{2g}$ are Bernoulli numbers~\cite{FP03}. The integrand has degree $(2g-2)+g = 3g-2 = \dim\overline{\mathcal{M}}_{g,1}$. At $g = 1$: $\frac{1}{2} \cdot \frac{1/6}{2} = \frac{1}{24}$; at $g = 2$: $\frac{7}{8} \cdot \frac{1/30}{24} = \frac{7}{5760}$ \textup{(LOCAL)}.
  4546	\end{theorem}
  4547	





thinking
**Identifying theorem inconsistencies**

I’m trying to figure out if each cited result is supported. I noticed some inconsistencies regarding the theorem provenance, particularly with the remark stating it's proven in Mumford83, while another line says it’s completed by FP03. This indicates a contradiction. I think I need to adjust the remark to cite FP03 accurately while treating Mumford83 as a precursor. It’s all about ensuring internal consistency within the theorem's context, and it feels significant to correct this!
thinking
**Addressing theorem provenance**

I'm considering adding a note regarding the foundation file for lines 4559-4560. There's a conflict between the proof note stating it’s proven in Mumford83 and the theorem citing FP03. To fix this, I think I should replace the provenance note with “proved in Faber-Pandharipande [FP03], building on Mumford [Mumford83].” This seems reasonable, and even though we have eight findings already, I believe this adjustment is both worthwhile and subtle enough to enhance clarity.
thinking
**Formatting findings clearly**

The user wants the findings to be presented in a bulleted format, which I think is a good idea. It keeps everything organized and easy to read. 

I need to list around nine findings ordered by severity, starting with critical issues. I’ll format them like this: 

A. [CRITICAL] higher_genus_foundations.tex:5380-5405 — PROBLEM: unproved jump in the theorem; FIX: split the theorem and update references. 

B. [CRITICAL] higher_genus_modular_koszul.tex:2659-2745 — PROBLEM: missing proof for part (i) and (ii); FIX: downgrade theorem. 

This should keep it structured!
thinking
**Considering findings format**

I could keep it simple by using just numbers, like `Checked: 10 | Findings: 10 | Verdict: FAIL`. That seems good! But maybe I should include the specific file and line numbers, along with any ranges, to make it more precise. It's important to provide enough detail so anyone looking at the results can easily understand where things went awry. I'll keep this structure in mind as I finalize the report!
thinking
**Planning content structure**

I need to address the user’s request for specific file lines, so I’ll reference range 5730-5776 without being overly verbose. I'll start with the line number, then craft a bullet list with around 10 points, aiming for a clear summary of about 30 lines total. Each bullet point might be 2-3 lines, without any markdown links. I’ll keep it clear and concise, avoiding nested bullets but using semicolons for clarity. Let's get drafting!
codex
- [CRITICAL] chapters/theory/higher_genus_foundations.tex:5380-5405 — PROBLEM: The proof of `thm:genus-universality` jumps from “one-variable recursion”, “same propagator”, and “same Hodge bundle” to `\Gamma_{\cA,g}=\kappa(\cA)\lambda_g` for all `g`, but no cited result proves that those hypotheses uniquely force the `\lambda_g` class. The same file later states at 5730-5776 that scalar saturation does not determine which genus-`g` class appears. FIX: split the theorem now. Keep only the proved genus-1 statement `\mathrm{obs}_1(\cA)=\kappa(\cA)\lambda_1`; move the all-genera factorization to a conjecture/conditional theorem until a separate clutching-uniqueness proposition is actually proved and cited at 5394-5405.

- [CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:2659-2696,2729-2738 — PROBLEM: Theorem D is tagged `\ClaimStatusProvedHere`, but parts (i) and (ii) are only as strong as `thm:genus-universality`; once the all-genera proof above fails, the flagship theorem is overstated on its main uniform-weight lane. FIX: rewrite Theorem D so the unconditional claim is genus-1 only, or mark parts (i)(a) and (ii) as conditional pending the missing universality proof; then propagate that narrower status to concordance and guide surfaces that currently advertise Theorem D as fully proved.

- [CRITICAL] chapters/connections/concordance.tex:5939-5947,6017-6025 — PROBLEM: `thm:family-index` defines `\mathcal D_{\cA}^{(g)}:=\kappa(\cA)\cdot\mathbb E` as a `K_0`-class, i.e. “`\kappa` copies of the Hodge bundle”, and then claims the top Chern class determines that `K`-class uniquely. Neither step is justified: a complex scalar is not a bundle multiplicity in `K_0`, and a top Chern class does not uniquely determine a `K`-theory class. FIX: delete the definition of `\mathcal D_{\cA}^{(g)}` and restate the theorem only as the scalar GRR/Faber-Pandharipande identity `F_g(\cA)=\kappa(\cA)\int_{\overline{\mathcal M}_{g,1}}\psi^{2g-2}\lambda_g` plus the generating series; also remove the downstream “canonical identification” language at 6205-6218.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2741-2744 — PROBLEM: The proof of Theorem D cites `thm:anomaly-koszul` for general additivity, but `thm:anomaly-koszul` is explicitly about the matter-ghost system and itself imports additivity from `cor:kappa-additivity`. The dependency is backwards. FIX: replace line 2741 with `Part~(iv) is Corollary~\ref{cor:kappa-additivity}; the anomaly-cancellation specialization is Theorem~\ref{thm:anomaly-koszul}.`

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:2703-2716; chapters/theory/higher_genus_foundations.tex:5425-5429 — PROBLEM: The duality clause overclaims scope. The theorem text says “affine Kac--Moody and free-field algebras”, but the cited proof only covers affine KM plus a `\mathcal W` formula; for the `\mathcal W` part it cites `thm:wn-obstruction`, which is only the principal `\mathcal W_N=\mathcal W(\mathfrak{sl}_N)` theorem, not the general `\mathcal W(\mathfrak g)` statement used in the text. The sentence `\kappa=0` iff critical level is unscoped and contradicted by the `\mathcal W` clause itself. FIX: cite `cor:general-w-obstruction` with its generic-level hypothesis `k\neq -h^\vee`; narrow the first sentence to families actually proved; and replace line 2716 by `For affine Kac--Moody, \kappa=0 iff k=-h^\vee. For principal \mathcal W^k(\mathfrak g,f_{\mathrm{prin}}) at generic level, \kappa=0 iff c=0.`

- [HIGH] chapters/examples/genus_expansions.tex:1913-1927 — PROBLEM: `thm:universal-generating-function` is marked `\ClaimStatusProvedHere`, but its proof is only `By Theorem~\ref{thm:genus-universality}(iii)...`. If the all-genera scalar factorization is unsupported, this theorem is unsupported too. FIX: downgrade the theorem to the proved genus-1 statement `F_1=\kappa/24` with an explicit conditional all-genera clause, or supply an independent proof from a separately proved all-genera factorization and the Bernoulli series identity.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:514-633 — PROBLEM: `prop:genus-g-curvature-package` is tagged `\ClaimStatusProvedHere`, but part (iv) is not proved there; the proof simply forwards to `thm:genus-universality` and `thm:family-index`. That makes an early “package” proposition advertise as locally proved what is actually deferred. FIX: split off part (iv) into a later corollary after the universality/GRR results, or keep only parts (i)-(iii) in this proposition and mark the scalar-package summary as proved elsewhere or conditional.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:5893-5894 — PROBLEM: `cor:kappa-additivity` proves additivity of `\kappa` by invoking `thm:genus-universality`, even though the actual argument only needs genus-1 curvature. This creates an unnecessary hidden dependence on the broken all-genera theorem. FIX: rewrite the proof to stop after the genus-1 argument for `\kappa(\mathcal A\otimes\mathcal B)=\kappa(\mathcal A)+\kappa(\mathcal B)`; keep the `\mathrm{obs}_g` sentence only as a corollary on the repaired scalar lane.

- [LOW] chapters/theory/higher_genus_foundations.tex:5312,594,4541,4545 — PROBLEM: Raw `\textup{(LOCAL)}` markers remain inside theorem/proposition statements on the exact proof surface being cited. These are unresolved drafting artifacts, not mathematical scope. FIX: delete each marker and replace it with an explicit scope sentence only where a real restriction is intended.

- [LOW] chapters/theory/higher_genus_foundations.tex:4559-4560 — PROBLEM: The provenance note for `thm:mumford-formula` says the claim is “proved in `\cite{Mumford83}`”, but the theorem title cites `FP03` and the concordance proof at chapters/connections/concordance.tex:6097-6098 says Mumford initiated the theory and Faber--Pandharipande completed the evaluation. The manuscript is internally inconsistent about the source of the imported theorem. FIX: change 4559-4560 to `This claim is used here as an external theorem, proved in \cite{FP03}, building on Mumford’s GRR framework \cite{Mumford83}.`

Circularity check: no live 2-cycle remains. chapters/theory/higher_genus_foundations.tex:5403-5405 explicitly says `thm:genus-universality` does not invoke `thm:family-index`, while chapters/connections/concordance.tex:6010-6025 makes `thm:family-index` depend on `thm:genus-universality`. The failure is a proof gap plus downstream status inflation, not a current circular citation.

## Summary
Checked: 10 | Findings: 10 | Verdict: FAIL
tokens used
316,946
