# R19_coderived_models (341s)

Edited [chapters/theory/coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex) only.

The coderived definitions were already substantively correct. I made that explicit in both the abstract and factorization definitions by stating the cone criterion for Verdier localization and by ruling out the naive “mod `\operatorname{Im}(d)`” reading. I also replaced the misleading “coacyclic quotients `M/\operatorname{coacyc}(M)`” language in `def:curved-weak-equiv` with the intrinsic cone/coacyclic Verdier-localization criterion.

For `prop:coderived-adequacy(a)`, the proof was already independent of `Theorem~\ref{thm:higher-genus-inversion}`; I made that independence explicit in the proof, identifying the actual inputs as the strict curvature-zero Chevalley--Cousin comparison and Positselski’s filtered coacyclicity criterion. I re-read the modified sections in context, diffed the file, and confirmed the referenced labels still exist. I did not run a full TeX build.

## Rectification Summary
- [FIXED] finding 1 — kept the Verdier-quotient definition, added explicit cone/coacyclic characterization at both coderived definitions, and removed the misleading quotient notation in `def:curved-weak-equiv` that could be read as “boundaries mod `\operatorname{Im}(d)`.”
- [FIXED] finding 2 — kept `prop:coderived-adequacy(a)` as proved, and made the proof explicitly non-circular by stating that it does not use `thm:higher-genus-inversion`, only the strict Chevalley--Cousin quasi-isomorphism and Positselski’s filtered criterion.


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
session id: 019d868c-4019-7281-a752-2bdc2f019db2
--------
user
<task>
You are a RECTIFICATION agent for a research mathematics manuscript on operadic Koszul duality.
Your mission: fix the specific findings below with the STRONGEST technical choice.
Hierarchy: (1) strengthen proof > (2) add missing lemma > (3) narrow claim to match proof > (4) mark conditional.
NEVER weaken when you can strengthen. NEVER leave a gap unfixed.
</task>

<action_safety>
Only edit the specific file(s) assigned. Do not touch other files.
Make the MINIMUM truthful edit that resolves each finding.
After each edit, re-read surrounding context to verify coherence.
</action_safety>

<verification_loop>
After all edits, re-read the modified sections and verify:
1. Each finding is resolved
2. No new inconsistencies introduced
3. Theorem status tags match the actual proof status
4. All \ref and \label are valid
</verification_loop>

<completeness_contract>
Address EVERY finding listed. Do not stop at the first fix.
For each finding, state: FIXED (how) or CANNOT_FIX (why, what narrower claim survives).
</completeness_contract>

<structured_output_contract>
End with:
## Rectification Summary
- [FIXED] finding — what was done
- [NARROWED] finding — claim narrowed to X
- [CONDITIONAL] finding — marked conditional on Y
- [BLOCKED] finding — cannot fix because Z
</structured_output_contract>


TARGET: chapters/theory/coderived_models.tex

FINDINGS TO FIX:

1. [CRITICAL T12] Lines ~75, ~545: The coderived category is defined as Verdier quotient
   by coacyclic objects. But bv_brst.tex:1945 treats it as "boundaries mod Im(d)".
   FIX: Verify the definition here is correct and consistent. If it is, the bv_brst proof
   is using the wrong characterization.

2. [CRITICAL T02] Lines ~247-270: prop:coderived-adequacy(a) invokes thm:higher-genus-inversion,
   creating circular dependency.
   FIX: Break the circularity. Prove coderived-adequacy independently, or mark it conditional.

Read the file, verify both findings, fix.
mcp startup: no servers

thinking
**Managing file edits**

I think we can ask the explorer to read the necessary files and targeted surface before trusting the summary. But first, I need the exact text for the patches. I could use exec_command to open file lines when editing, although having the explorer cover them isn’t ideal. Perhaps it’s allowed since editing needs context. I should identify exact sections and line numbers and use exec_command to inspect those specific snippets for patching. It's crucial to edit only the assigned files without affecting others.
codex
Using `beilinson-rectify` for the local theorem/proof repair, with `multi-path-verify` only for the definition check. I’m first reading the required constitutional surfaces plus the exact target and dependency points to lock the claim surface before editing.
collab spawn_agent(call_w1lK8gcirAxBpxAmbPSsCR7F, prompt="Read and summarize only the parts of these files relevant to the assigned rectification in chapters/theory/coderived_mod…")
spawn_agent(call_w1lK8gcirAxBpxAmbPSsCR7F, prompt="Read and summarize only the parts of these files relevant to the assigned rectification in chapters/theory/coderived_mod…") pending init:
  agent: 019d868c-b49a-79d3-b3ab-7adda65fd5e5
Plan update
  → Read constitutional and target surfaces; lock definitions, labels, and dependency graph for the two findings
  • Edit chapters/theory/coderived_models.tex with the minimum truthful fix for both findings
  • Re-read modified sections and run narrow verification for labels/refs/coherence
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'rg -n "coderived" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
508:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
exec
/bin/zsh -lc "sed -n '450,560p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
**FM24. B-cycle monodromy i^2 error.** When hbar contains a factor of pi*i (from a non-standard convention), the formula q = e^{2*pi*i*hbar} gives q = e^{2*pi*i*pi*i/(k+2)} = e^{-2*pi^2/(k+2)}, which is a REAL number less than 1, not a root of unity. The i^2 = -1 turns an imaginary exponential into a real exponential. This error propagates silently because q still "looks like" a parameter. Counter: after defining q = e^{2*pi*i*hbar}, substitute a specific integer k and verify q is on the unit circle (|q| = 1).

**FM25. The SC^{ch,top} disaster of 2025-2026 (Opus 4.6 structural confabulation).** Opus constructed an elaborate but FALSE framework claiming B(A) is an SC^{ch,top}-coalgebra. The chain of errors:

(1) WRONG: "The bar differential is the closed/holomorphic color of SC." TRUTH: The bar differential d_B comes from the chiral product (OPE residues at FM boundary strata). It is the differential of a dg coalgebra over (ChirAss)^!, NOT a "color" of SC. Having operations that USE FM_k(C) geometry does not make d_B an "E_2 color" — it is a single degree-1 map, not a parametrized family of operations.

(2) WRONG: "The deconcatenation coproduct is the open/topological color of SC." TRUTH: Deconcatenation is the cofree tensor coalgebra structure on T^c(V). It is coassociative. This makes B(A) an E_1-coassociative coalgebra. It is NOT a separate "color" of a two-colored operad.

(3) WRONG: "Together, d_B and Delta make B(A) an SC-coalgebra." TRUTH: A dg coassociative coalgebra (differential + coproduct) is a SINGLE-colored E_1 dg coalgebra. Having two structures does not make it two-colored. SC is two-colored (bulk + boundary); B(A) is one object, not a pair.

(4) WRONG: "The SC structure on B(A) is dual to the SC structure on (Z^{der}(A), A)." TRUTH: B(A) is an INPUT to the Hochschild computation. The derived center C^bullet_ch(A,A) is computed FROM B(A) via the convolution Hom(B(A), A). The SC structure emerges in the OUTPUT (the derived center pair), not on the INPUT (the bar complex). The passage B(A) → C^bullet_ch(A,A) is the Hochschild construction, not an operadic duality.

(5) WRONG: "E_1-chiral = E_1-topological (on R)." TRUTH: E_1-chiral means operations from ordered configurations on a CURVE (2-real-dimensional, holomorphic structure). E_1-topological means operations from Conf_k(R) (1-real-dimensional). A chiral algebra on a curve X is a factorization algebra on a real 2-manifold sensitive to holomorphic structure. Calling the bar complex "E_1" without "chiral" conflates these. The bar complex is over (ChirAss)^!, NOT (Ass)^!.

(6) WRONG: "The Steinberg analogy: B(A) presents SC as the Steinberg variety presents the Hecke algebra." TRUTH: Retired. The Steinberg variety is a geometric object in the representation theory of reductive groups. The bar complex is a coalgebra computing the derived center. These are unrelated constructions at different categorical levels.

Counter: NEVER write B(A) and SC^{ch,top} in the same sentence attributing SC to B(A). The SC structure lives on (C^bullet_ch(A,A), A). The bar complex is over (ChirAss)^!, single-colored, E_1-chiral-coassociative.

**FM26. False operad self-duality claim.** Opus claimed "(SC^{ch,top})^! ~ SC^{ch,top}" (Koszul self-dual) in thm:SC-self-duality, misciting Livernet [Liv06] (which proves Koszulity, not self-duality). The manuscript's OWN compute engine (sc_koszul_dual_cooperad_engine.py) computes SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!, manifestly different from SC = (Com, Ass) with closed dim = 1. The error: confusing "the duality FUNCTOR is an involution on SC-algebras" with "the OPERAD is self-dual." These are different: (P^!)^! ~ P (tautological for Koszul operads) does NOT mean P^! ~ P. Counter: before claiming any operad is self-dual, verify dim P(n) = dim P^!(n) at all degrees.

codex
I’ve scoped the task to two local issues in [chapters/theory/coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex): the coderived-definition surface and the proof dependency at `prop:coderived-adequacy`. Next I’m reading the rectification skill instructions and then I’ll patch only once the dependency graph is explicit.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc 'rg -n "coderived" -n chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3:\label{app:coderived}
4:\index{coderived category|textbf}
10:Positselski's theory of coderived and contraderived
14:\S\ref{subsec:chiral-coderived-contraderived}.
17:\label{subsec:coderived-abstract}
20:(for the coderived case) or exact direct products
76:\label{def:coderived-contraderived-abstract}
77:\index{coderived category!abstract definition|textbf}
79:The \emph{coderived category} and \emph{contraderived category}
85: \label{eq:coderived-abstract}\\
126:\index{conilpotent coalgebra!coderived reduction}
130:CDG-comodule is coacyclic, so the coderived category coincides
143:the coderived category reduces to the ordinary derived
149:\label{rem:coderived-bar-cobar}
150:\index{bar-cobar adjunction!coderived formulation}
156:Theorem~\ref{thm:conilpotent-reduction} applies: the coderived
166:coderived category
181:\label{sec:coderived-models}
182:\index{coderived category!relative models|textbf}
184:The full theory of coderived categories of factorization algebras
exec
/bin/zsh -lc "sed -n '170,320p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\simeq D^{\mathrm{ctr}}(\barB^{(g)}(\cA)\text{-}\mathrm{contra})$
\textup{(}Theorem~\ref{thm:positselski-chiral-proved}\textup{)} is the chiral
incarnation of the comodule-contramodule correspondence
\eqref{eq:co-contra-equivalence}.
\end{remark}

%%% ---------------------------------------------------------------
%%% Relative curved models adequate for the present monograph
%%% ---------------------------------------------------------------

\subsection{Relative curved models}
\label{sec:coderived-models}
\index{coderived category!relative models|textbf}

The full theory of coderived categories of factorization algebras
on $\operatorname{Ran}(X)$ is not yet available in the literature;
its development is part of the Stratum~II programme
(Remark~\ref{rem:two-strata}). Nevertheless, the off-Koszul
statements in this monograph (where the bar-cobar counit is
a curved equivalence rather than a quasi-isomorphism) require

exec
/bin/zsh -lc "sed -n '1,160p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\section{Coderived and contraderived categories}
\label{app:coderived}
\index{coderived category|textbf}
\index{contraderived category|textbf}

The bar-cobar adjunction at higher genus produces curved complexes
($d^2 \neq 0$), for which ordinary cohomological derived methods
are no longer the right invariant.
Positselski's theory of coderived and contraderived
categories~\cite{Positselski11} provides the correct
replacement. This appendix collects the definitions and key results
needed in this monograph; the chiral specialization appears in
\S\ref{subsec:chiral-coderived-contraderived}.

\subsection{Abstract definitions}
\label{subsec:coderived-abstract}

Let $\mathsf{A}$ be an abelian category with exact direct sums
(for the coderived case) or exact direct products
exec
/bin/zsh -lc 'rg -n "coderived" chapters/physics/bv_brst.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: chapters/physics/bv_brst.tex: IO error for operation on chapters/physics/bv_brst.tex: No such file or directory (os error 2)
thinking
**Considering the approach for file inspection**

I’m contemplating whether to involve subagents since the user didn't ask for it. The skill suggests using them only when explicitly requested, but there's guidance for using the explorer for codebase questions. I think we can go ahead and inspect the target file ourselves, probably a safe choice given the developer's high-level instruction. I’ll try to read relevant lines and definitions while keeping track of the file size. Let's consider using `rg` for efficient searching!
exec
/bin/zsh -lc "rg -n \"coderived|coacyclic|higher-genus-inversion|coderived-adequacy|Verdier quotient|boundary|Im\\\\(d\\\\)\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3:\label{app:coderived}
4:\index{coderived category|textbf}
10:Positselski's theory of coderived and contraderived
14:\S\ref{subsec:chiral-coderived-contraderived}.
17:\label{subsec:coderived-abstract}
20:(for the coderived case) or exact direct products
57:\label{def:coacyclic-contraacyclic}
58:\index{coacyclic object|textbf}
62:\item A CDG-comodule $M$ is \emph{coacyclic} if it belongs to the
76:\label{def:coderived-contraderived-abstract}
77:\index{coderived category!abstract definition|textbf}
79:The \emph{coderived category} and \emph{contraderived category}
80:of a CDG-coalgebra $(C, d, h)$ are the Verdier quotients:
85: \label{eq:coderived-abstract}\\
93:object is coacyclic (resp.\ contraacyclic), so there are natural
126:\index{conilpotent coalgebra!coderived reduction}
130:CDG-comodule is coacyclic, so the coderived category coincides
143:the coderived category reduces to the ordinary derived
149:\label{rem:coderived-bar-cobar}
150:\index{bar-cobar adjunction!coderived formulation}
exec
/bin/zsh -lc "sed -n '500,620p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,340p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\section{Coderived and contraderived categories}
\label{app:coderived}
\index{coderived category|textbf}
\index{contraderived category|textbf}

The bar-cobar adjunction at higher genus produces curved complexes
($d^2 \neq 0$), for which ordinary cohomological derived methods
are no longer the right invariant.
Positselski's theory of coderived and contraderived
categories~\cite{Positselski11} provides the correct
replacement. This appendix collects the definitions and key results
needed in this monograph; the chiral specialization appears in
\S\ref{subsec:chiral-coderived-contraderived}.

\subsection{Abstract definitions}
\label{subsec:coderived-abstract}

Let $\mathsf{A}$ be an abelian category with exact direct sums
(for the coderived case) or exact direct products
 succeeded in 53ms:
the coaugmentation filtration on~$C$ is exhaustive.
\end{definition}

\begin{example}[The bar complex as curved factorization coalgebra]
\label{ex:bar-fact-CDG}
\index{bar complex!as curved factorization coalgebra}
The bar construction
$C = \barB^{\mathrm{fact}}(\cA)$ of a complete augmented chiral
algebra~$\cA$ is the prototypical curved factorization coalgebra.
We verify each axiom:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Factorization coalgebra.}
 The coalgebra structure comes from NAP duality on
 Fulton--MacPherson compactifications
 (Theorem~\ref{thm:coalgebra-via-NAP}). The coaugmentation
 $\varepsilon \colon C \to \omega_X$ is the projection to bar
 degree zero.
\item \emph{CDG structure.}
 The differential~$d$ and curvature
 $h = \mcurv{g}$ are established in
exec
/bin/zsh -lc 'ls chapters/physics' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
ls: chapters/physics: No such file or directory
exec
/bin/zsh -lc 'ls chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
connections
examples
frame
theory
exec
/bin/zsh -lc "rg --files -g 'bv_brst.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex
collab wait(call_ft0f5zr29FsGfvZPaU6jL7Kh)
  receivers: 019d868c-b49a-79d3-b3ab-7adda65fd5e5
exec
/bin/zsh -lc 'rg -n "coderived" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
32:all-genera coderived comparison of
33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
1853:Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
1861:curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
1862:class~$\mathsf{M}$ BV and bar models in the coderived category even
1899: & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
1908:powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
1915:\begin{theorem}[BV$=$bar in the coderived category;
1917:\label{thm:bv-bar-coderived}%
1918:\index{BV algebra!bar complex identification!coderived category|textbf}%
1919:\index{coderived category!BV/bar identification|textbf}%
1994:becomes an isomorphism in the coderived quotient
2001:of Definition~\ref{def:coderived-fact}. This is the required
2002:coderived comparison. The provisional localization is not needed
2006:\begin{remark}[Harmonic mechanism behind the coderived comparison]
2007:\label{rem:bv-bar-coderived-higher-genus}%
2008:\index{coderived category!higher-genus validity}%
2012:Theorem~\ref{thm:bv-bar-coderived}. The proof has two inputs:
2029:\begin{remark}[Why the coderived category is inevitable]
2030:\label{rem:bv-bar-coderived-why}
exec
/bin/zsh -lc "sed -n '1850,2105p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
class~C at genus~$1$. This is the local model for the
all-genera harmonic-decoupling hypothesis used in
Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
factors through the same composite free-field sector, the quartic
and higher chain-level corrections vanish. For class~$\mathsf{M}$, the
quartic harmonic discrepancy
$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
\kappa / \mathrm{Im}(\tau)$ is not cancelled by the Fay trisecant
identity. Proposition~\ref{prop:chain-level-three-obstructions}
shows that the full harmonic discrepancy still factors through the
curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
class~$\mathsf{M}$ BV and bar models in the coderived category even
though the strict chain-level comparison remains open.
\end{remark}

\begin{remark}[BV sewing at the chain level: class-by-class status;
 \ClaimStatusProvedHere]%
\label{rem:bv-sewing-chain-level-classes}%
\index{BV algebra!sewing operator identification|textbf}%
exec
/bin/zsh -lc 'rg -n "thm:higher-genus-inversion" -n' in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
Total output lines: 1122

wave2_audit_20260413_001942/C09_higher_genus_complementarity.md:1089:  4204	Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
metadata/dependency_graph.dot:2853:  thm_higher_genus_inversion [label="thm:higher-genus-inversion\ntheorem [Pr]\nHigher genus inversion", style=filled, fillcolor="#c8e6c9"];
audit_campaign_20260412_231034/T12_MC5_BV_bar.md:1037:   693	(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:551:  2218	Theorem~\ref{thm:higher-genus-inversion} derives inversion
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:832:   593	or complementarity. Theorems~\ref{thm:higher-genus-inversion}
wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:872:chapters/theory/coderived_models.tex:266:Theorem~\ref{thm:higher-genus-inversion}, hence a weak equivalence
relaunch_20260413_111534/R13_introduction.md:409:   563	 Theorem~\ref{thm:higher-genus-inversion}).
metadata/label_index.json:49298:  "thm:higher-genus-inversion": {
metadata/theorem_registry.md:782:| `thm:higher-genus-inversion` | `theorem` | 4316 | Higher genus inversion |
metadata/claims.jsonl:239:{"label": "conj:categorical-modular-kd", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/concordance.tex", "line": 5435, "title": "Categorical modular Koszul duality", "refs_in_block": ["subsec:coderived-ran", "thm:higher-genus-inversion", "rem:chain-vs-classical-mf", "rem:spectral-characteristic-programme"]}
metadata/claims.jsonl:255:{"label": "prop:descent-fan", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 9794, "title": "Descent fan structure", "refs_in_block": ["thm:bar-cobar-isomorphism-main", "thm:higher-genus-inversion", "thm:riccati-algebraicity", "constr:shadow-epstein-eisenstein", "eq:constrained-epstein-fe", "thm:sewing-hecke-reciprocity"]}
metadata/claims.jsonl:2147:{"label": "thm:bar-cobar-inversion-qi", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 1606, "title": "Bar-cobar inversion: strict on the Koszul locus, coderived off it", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "sec:i-adic-completion", "def:koszul-chiral-algebra", "thm:higher-genus-inversion", "thm:pbw-allgenera-km", "thm:pbw-allgenera-principal-w", "prop:coderived-bar-degree-spectral-sequence", "thm:bar-cobar-spectral-sequence", "thm:spectral-sequence-collapse", "rem:sl2-admissible", "rem:virasoro-module-koszul-minimal", "cor:bar-cobar-inverse", "thm:positselski-chiral-proved", "thm:full-derived-module-equiv-proved"]}
metadata/claims.jsonl:2272:{"label": "thm:chiral-homology-recovery", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 3504, "title": "Chiral homology recovery", "labels_in_block": ["thm:chiral-homology-recovery", "eq:chiral-homology-bar", "eq:center-sheaf-bar", "eq:ambient-from-bar", "eq:chiral-homology-tower"], "refs_in_block": ["thm:quantum-complementarity-main", "thm:higher-genus-inversion"]}
metadata/claims.jsonl:2683:{"label": "thm:fourier-four-properties", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/theory/fourier_seed.tex", "line": 918, "title": "The four properties of the Fourier transform", "refs_in_block": ["thm:bar-cobar-isomorphism-main", "thm:higher-genus-inversion", "thm:quantum-complementarity-main", "thm:modular-characteristic"]}
metadata/claims.jsonl:2746:{"label": "thm:higher-genus-inversion", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 4316, "title": "Higher genus inversion", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "thm:modular-characteristic", "thm:multi-weight-genus-expansion", "def:modular-koszul-chiral"]}
metadata/claims.jsonl:2774:{"label": "thm:genus-extension-hierarchy", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_foundations.tex", "line": 804, "title": "Genus extension hierarchy", "refs_in_block": ["thm:mc2-bar-intrinsic", "app:coderived-models", "thm:koszul-equivalences-meta", "thm:higher-genus-inversion", "thm:general-hs-sewing"], "cites_in_block": ["Zhu96"]}
metadata/claims.jsonl:2852:{"label": "cor:feynman-duality-qch", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_foundations.tex", "line": 7095, "title": "Duality of quantum chiral homology", "labels_in_block": ["cor:feynman-duality-qch", "eq:double-feynman"], "refs_in_block": ["thm:higher-genus-inversion"]}
metadata/claims.jsonl:2860:{"label": "prop:standard-examples-modular-koszul", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 687, "title": "Free-field examples are modular pre-Koszul", "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral", "thm:higher-genus-inversion", "thm:quantum-complementarity-main", "conv:heisenberg-kappa-notation"]}
exec
/bin/zsh -lc 'rg -n "coderived" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
253:| `thm:bar-cobar-inversion-qi` | `theorem` | 1606 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
532:#### `chapters/theory/coderived_models.tex` (7)
536:| `prop:coderived-adequacy` | `proposition` | 244 | Adequacy |
537:| `prop:coderived-bar-degree-spectral-sequence` | `proposition` | 306 | Coderived bar-degree spectral sequence |
2349:| `thm:bv-bar-coderived` | `theorem` | 1917 | BV$=$bar in the coderived category |
2793:| `prop:thqg-X-coderived-fredholm-G` | `proposition` | 2107 | Coderived = Fredholm for class~G |
exec
/bin/zsh -lc "sed -n '500,560p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 293 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 354 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 387 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 469 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 545 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 665 | Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 935 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 1095 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1313 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1456 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1534 | Explicit cobar-bar augmentation |
| `prop:cobar-modular-shadow` | `proposition` | 1807 | Cobar as modular shadow carrier |
| `thm:cobar-cech` | `theorem` | 1819 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1867 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1888 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1978 | Topology |
| `thm:poincare-verdier` | `theorem` | 2037 | Bar-cobar Verdier pairing |
| `thm:curved-mc-cobar` | `theorem` | 2140 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 2165 | Curvature of the affine bar complex |
exec
/bin/zsh -lc 'rg -n "thm:higher-genus-inversion" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
782:| `thm:higher-genus-inversion` | `theorem` | 4316 | Higher genus inversion |
exec
/bin/zsh -lc 'rg -n "coderived" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
696: in the coderived category $D^{\mathrm{co}}$ for all shadow classes
697: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
1943:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
1955: BV=bar in the coderived category is proved for all four shadow
1956: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
3303: (Theorem~\ref{thm:bv-bar-coderived});
4184: coderived category.
4718:$B_{\mathrm{mod}}$ & Inversion on Koszul locus; coderived & Proved on Koszul locus; & Thm~\ref{thm:higher-genus-inversion}, \\
4719: & persistence off it & coderived persistence conjectural & \S\ref{subsec:coderived-ran} \\[2pt]
4835:\subsection{The coderived Ran-space formalism}
4836:\label{subsec:coderived-ran}
4855:intrinsic coderived/contraderived bar-coalgebra framework of
4863:their coderived/contraderived invariants remain nontrivial. The
4864:coderived framework is built to retain that information without
4867:The provisional coderived category
4869:(Definition~\ref{def:provisional-coderived},
4870:Proposition~\ref{prop:coderived-adequacy})
4873:foundations, the coderived and derived categories agree.
4933:Appendix~\ref{app:coderived},
4934:\S\ref{subsec:coderived-ran-formalism} develops the coderived
exec
/bin/zsh -lc "sed -n '1,200p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
exec
/bin/zsh -lc 'ls raeeznotes' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
ls: raeeznotes: No such file or directory
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
bibliography
bp_self_duality.pdf
exec
/bin/zsh -lc 'ls archive' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "sed -n '1,200p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
wait(call_ft0f5zr29FsGfvZPaU6jL7Kh) timed out:
exec
/bin/zsh -lc 'rg -n "coderived" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
exec
/bin/zsh -lc "sed -n '220,360p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item The associated graded map
 $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
 strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
 \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
\item The induced map on coacyclic quotients
 $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
 isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
 generated by totalizations of short exact sequences
 (Positselski~\cite{Positselski11}).
\end{enumerate}
The equivalence of (i) and (ii) holds for bounded-below filtrations
by~\cite[Proposition~3.5]{Positselski11}.
\end{definition}

\begin{definition}[Provisional coderived category]
\label{def:provisional-coderived}
\index{coderived category!provisional|textbf}
The \emph{provisional coderived category} $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
is the localization of the category of filtered curved factorization
models (Definition~\ref{def:filtered-curved-model}) at the weak
codex
The target file has the two exact pressure points: the abstract/factorization coderived definitions are already written as Verdier quotients by coacyclics, and `prop:coderived-adequacy(a)` currently proves the counit by filtered associated-graded acyclicity. I’m now checking the external dependency claims so I can remove the circularity without changing more surface than necessary.
exec
/bin/zsh -lc "sed -n '620,780p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1920,1975p' chapters/physics/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "higher-genus-inversion" chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:higher-genus-inversion|prop:coderived-adequacy|coderived-adequacy|higher-genus-inversion\" -S chapters/theory/coderived_models.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{definition}[Coderived and contraderived factorization categories]
\label{def:coderived-fact}
\index{coderived category!factorization|textbf}
\index{contraderived category!factorization|textbf}
The \emph{coderived} and \emph{contraderived factorization
categories} of a curved factorization coalgebra $(C, d, h)$
on~$X$ are the Verdier quotients
\begin{align}
D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})
 &:= \mathrm{Hot}(C\text{-}\mathrm{CoFact})
 \,\big/\, \mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}},
 \label{eq:coderived-fact}\\
D^{\mathrm{ctr}}(C\text{-}\mathrm{ContraFact})
 &:= \mathrm{Hot}(C\text{-}\mathrm{ContraFact})
 \,\big/\, \mathrm{Acycl}^{\mathrm{ctr}}_{\mathrm{fact}}.
 \label{eq:contraderived-fact}
\end{align}
When $h = 0$ and $C$ is conilpotent,
Theorem~\ref{thm:conilpotent-reduction} gives
 exited 1 in 51ms:

 exited 1 in 51ms:
sed: chapters/physics/bv_brst.tex: No such file or directory
 succeeded in 51ms:
chapters/examples/deformation_quantization.tex:816:Theorems~B and~C (Theorems~\ref{thm:higher-genus-inversion}
chapters/theory/coderived_models.tex:244:\label{prop:coderived-adequacy}
chapters/theory/coderived_models.tex:771:(Proposition~\ref{prop:coderived-adequacy}(b)) provides the
chapters/examples/lattice_foundations.tex:1950:\item \emph{Theorem~B} (Theorem~\ref{thm:higher-genus-inversion}).
chapters/examples/beta_gamma.tex:433:(Theorem~\ref{thm:higher-genus-inversion}).
chapters/examples/yangians_drinfeld_kohno.tex:1602:(Theorem~\ref{thm:higher-genus-inversion}(a)). When $h = 0$,
chapters/examples/yangians_drinfeld_kohno.tex:8119:(Theorem~\ref{thm:higher-genus-inversion} on the Koszul
chapters/examples/kac_moody.tex:3777:The proof is an instance of Theorem~\ref{thm:higher-genus-inversion} (higher genus bar-cobar inversion), specialized to $g=1$ and $\mathfrak{g} = \mathfrak{sl}_2$. We verify the hypotheses.
chapters/examples/kac_moody.tex:3805:The quasi-isomorphism $\Omega(\barB^{(1)}) \xrightarrow{\sim} \widehat{\mathfrak{sl}}_{2,k}$ then follows from the general inversion theorem (Theorem~\ref{thm:higher-genus-inversion}), whose hypotheses are verified by the Koszul property (Ext-vanishing) and the completeness of the weight filtration.
chapters/examples/kac_moody.tex:4017:This is Theorem~\ref{thm:higher-genus-inversion} for $g=1$, $\mathfrak{g}=\mathfrak{sl}_3$.
chapters/examples/genus_expansions.tex:458:\item \emph{Theorem~B} (Bar-Cobar Inversion, Theorem~\ref{thm:higher-genus-inversion}):
chapters/examples/w_algebras.tex:1223:Theorem~\ref{thm:higher-genus-inversion} applied to the principal
chapters/connections/outlook.tex:34: \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
chapters/frame/guide_to_main_results.tex:41: Thm~\ref{thm:higher-genus-inversion} \\[4pt]
chapters/connections/thqg_introduction_supplement_body.tex:221: (Theorem~\ref{thm:higher-genus-inversion}).
chapters/frame/heisenberg_frame.tex:1338:(Theorem~\ref{thm:higher-genus-inversion})
chapters/frame/heisenberg_frame.tex:4583:(Theorem~\ref{thm:higher-genus-inversion}):
chapters/connections/concordance.tex:39: \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
chapters/connections/concordance.tex:264: and~\ref{thm:higher-genus-inversion}).}
chapters/connections/concordance.tex:4718:$B_{\mathrm{mod}}$ & Inversion on Koszul locus; coderived & Proved on Koszul locus; & Thm~\ref{thm:higher-genus-inversion}, \\

thinking
**Evaluating theorem details**

I found an interesting note in the higher_genus_complementarity, specifically between lines 4429-4430, which discusses the absence of circular dependence on a proposition. I need to inspect those theorem lines closely to fully understand what this implies. It's always intriguing to dig deeper into the details, and I want to ensure I'm grasping the full context surrounding this note. Let's check the surrounding lines for more clarity!
exec
/bin/zsh -lc "sed -n '4350,4445p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[j_!j^*C \longrightarrow C \longrightarrow i_*i^*C \xrightarrow{+1}.\]
Both outer terms are acyclic, hence $C$ is acyclic. Therefore $f$ is a
quasi-isomorphism.
\end{proof}

\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
\index{bar-cobar inversion!higher genus}
\textup{[}Regime: curved-central on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

\smallskip\noindent
The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.

Let $\cA$ be a modular pre-Koszul chiral algebra
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
axioms \textup{MK1--MK3)}.
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Koszul locus.}
For each genus $g \geq 0$, the bar-cobar counit is a
quasi-isomorphism:
exec
/bin/zsh -lc 'rg -n "higher-genus" chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
154:(Convention~\ref{conv:higher-genus-differentials}).
204: Convention~\textup{\ref{conv:higher-genus-differentials}});
254: Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
643:capture the curved factorization theory; on the higher-genus
exec
/bin/zsh -lc 'rg -n "prop:coderived-adequacy" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4870:Proposition~\ref{prop:coderived-adequacy})

exec
/bin/zsh -lc "sed -n '4850,4895p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

On the Koszul locus this is an equivalence: $\exp \circ \log = \mathrm{id}$
on the convergence domain. When curvature is present (that is,
when the categorical logarithm acquires non-trivial monodromy), the
theorem-level statement moves from ordinary derived categories to the
intrinsic coderived/contraderived bar-coalgebra framework of
Positselski~\cite{Positselski11}. The logarithm/analytic-continuation
language is heuristic motivation only; the proved categorical content
is the bar-coalgebra comparison, with ordinary derived reduction only
on the flat finite-type completed-dual loci singled out in the
bar-cobar foundations.

Curved bar objects can lose ordinary cohomological visibility while
their coderived/contraderived invariants remain nontrivial. The
coderived framework is built to retain that information without
promoting the monodromy metaphor itself into a theorem.

The provisional coderived category
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
(Definition~\ref{def:provisional-coderived},
thinking
**Evaluating theorem dependencies**

Interesting! I’m looking into whether the theorem no longer relies on some findings. It seems there's a mention of a circular dependency in lines 247-270, but the current proof doesn't directly invoke that theorem. I should check the definitions, especially regarding the BD theorem and others mentioned. The user noted that those lines might reference the theorem, so I need to inspect the exact line numbers carefully. It’s puzzling!
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '236,300p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   236	\index{coderived category!provisional|textbf}
   237	The \emph{provisional coderived category} $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
   238	is the localization of the category of filtered curved factorization
   239	models (Definition~\ref{def:filtered-curved-model}) at the weak
   240	equivalences of Definition~\ref{def:curved-weak-equiv}.
   241	\end{definition}
   242	
   243	\begin{proposition}[Adequacy; \ClaimStatusProvedHere]
   244	\label{prop:coderived-adequacy}
   245	The provisional coderived category is adequate for the following
   246	constructions in this monograph:
   247	\begin{enumerate}[label=\textup{(\alph*)}]
   248	\item The curved bar-cobar counit
   249	 $\Omega_X \bar{B}_X(\cA) \to \cA$ is a coacyclic-equivalence:
   250	 its cone is coacyclic, hence it is an isomorphism
   251	 in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
   252	 algebra~$\cA$ satisfying the Chevalley--Cousin condition.
   253	\item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
   254	 Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
   255	 filtrations making each genus component a filtered curved model.
exec
/bin/zsh -lc "rg --files -g 'bv_brst.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:coderived-adequacy|def:coderived-contraderived-abstract|def:coderived-fact|coderived-adequacy|coderived and contraderived" metadata/theorem_registry.md chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex
 succeeded in 52ms:
chapters/connections/concordance.tex:4870:Proposition~\ref{prop:coderived-adequacy})
metadata/theorem_registry.md:536:| `prop:coderived-adequacy` | `proposition` | 244 | Adequacy |
codex
I found an important repository clue: `higher_genus_complementarity.tex` already contains a remark explicitly stating that the off-locus coderived upgrade is kept separate so `Theorem~ref{thm:higher-genus-inversion}` does not depend on `prop:coderived-adequacy(a)`. I’m checking whether [coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex) still needs a local clarification to make that separation explicit and to eliminate the “boundaries mod `Im(d)`” mischaracterization.

thinking
**Inspecting historical context**

I need to look into the historical facts surrounding bv_brst around 1945. This could involve researching key events, references, or significant details related to that time period. I’m curious about what I might discover regarding its relevance or implications. Let’s see what sources I can find! There’s a lot that could be explored, and I want to ensure I gather the right information for my inquiry.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1928,1965p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1928	 B^{(g)}(\cA)
  1929	\]
  1930	be the comparison morphism of filtered curved
  1931	factorization models
  1932	obtained by replacing the BV propagator with its Hodge
  1933	decomposition relative to the bar propagator. Then:
  1934	\begin{enumerate}[label=\textup{(\roman*)}]
  1935	\item for every genus $g \geq 0$,
  1936	\[
  1937	 C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
  1938	 \;\simeq_{D^{\mathrm{co}}}\;
  1939	 B^{(g)}(\cA);
  1940	\]
  1941	\item if $\cA$ lies in class~$\mathsf{G}$ or~$\mathsf{L}$, then
  1942	 $f_g$ is a weak equivalence of filtered curved models in the sense
  1943	 of Definition~\ref{def:curved-weak-equiv};
  1944	\item if $\cA$ lies in class~$\mathsf{C}$ and harmonic decoupling
  1945	 holds, then $f_g$ is a weak equivalence of filtered curved models;
  1946	\item if $\cA$ lies in class~$\mathsf{M}$, then for every $r \geq 4$
  1947	 the harmonic discrepancy satisfies
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1965,2015p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1965	d\log E + [d_{\mathrm{fib}}, h] + P_{\mathrm{harm}}.
  1966	\]
  1967	The commutator term contributes only a chain homotopy, so the
  1968	failure of~$f_g$ to intertwine the two curved differentials is the
  1969	harmonic discrepancy
  1970	$\delta^{\mathrm{harm}} = \sum_{r \geq 4}\delta_r^{\mathrm{harm}}$.
  1971	Proposition~\ref{prop:chain-level-three-obstructions} gives the
  1972	class-by-class description of this discrepancy.
  1973	
  1974	If $\cA$ lies in class~$\mathsf{G}$ or~$\mathsf{L}$, all harmonic
  1975	discrepancies vanish. Hence $f_g$ intertwines the curved
  1976	differentials on the nose. On the PBW-associated graded, the map is
  1977	the genus-$0$ comparison on each weight piece, hence a
  1978	quasi-isomorphism. By Definition~\ref{def:curved-weak-equiv}, $f_g$
  1979	is a weak equivalence of filtered curved models. The same argument
  1980	applies to class~$\mathsf{C}$ under harmonic decoupling.
  1981	
  1982	Now assume $\cA$ lies in class~$\mathsf{M}$, and let
  1983	$K_g := \operatorname{cone}(f_g)$. By
  1984	Proposition~\ref{prop:chain-level-three-obstructions}, every
codex
- `CLAUDE.md:508-540` flags MC5 as “analytic proved, coderived proved, chain-level conjectural,” so the BV=bar comparison in the coderived category (Thm `thm:bv-bar-coderived`) is treated as repository-wide proved content for all four shadow classes while chain-level agreement remains open for class M; this reinforces that the coderived passage (rather than a stricter derived equivalence) is the accepted status for higher-genus bar‐cobar comparisons.  
- `chapters/theory/coderived_models.tex:1-160` lays out the ambient homotopy theory: CDG‑coalgebras/comodules, the definitions of coacyclic objects (thick closure under short exact sequences plus ∞-sums) and the coderived category as the Verdier quotient, explaining why the ordinary derived category is insufficient when curvature \(h\neq0\).  
- `chapters/theory/coderived_models.tex:220-360` and `:244-320` define the “provisional coderived category” of filtered curved factorization models, prove `prop:coderived-adequacy` (the bar‑cobar counit becomes coacyclic because the Ran-Cousin filtration kills the curved correction, so the cone lies in the thick subcategory) and the companion bar-degree spectral sequence for coacyclicity; these are the local ingredients needed before appealing to any higher-genus inversion statement.  
- `chapters/connections/bv_brst.tex:1853-2070` explains the physical role of coderived localization: all harmonic discrepancies factor through curvature, so for class M the cone is coacyclic (Defn `def:coacyclic-fact`) and `thm:bv-bar-coderived` becomes an isomorphism in the coderived quotient; the surrounding remarks stress that the BV and bar complexes satisfy the same curved relation \(d^2 = m_0\) and that the coderived category is the minimal ambient that admits both without choosing a strictification.  
- `chapters/connections/concordance.tex:4855-4885` records the dependency chain: the provisional coderived category (`def:provisional-coderived`, `prop:coderived-adequacy`) is needed to keep curved objects visible while the bar-cobar story moves from genus 0 to higher genus, and Theorem `thm:higher-genus-inversion` is invoked only after the antecedent MK hypotheses (Koszulity, Verdier compatibility, PBW) have been independently established, so the “non-circular logical chain” is explicitly noted.  
- `metadata/theorem_registry.md:532-538` lists `prop:coderived-adequacy` and its companions from `chapters/theory/coderived_models.tex`, while `metadata/theorem_registry.md:782` records `thm:higher-genus-inversion` as a proved theorem at line 4316, ensuring the registry knows both labels and their statuses.  
- `archive/raeeznotes/raeeznotes100/red_team_summary.md:74-110` flags “proved-here claims with suspicious dependencies” (e.g., clusters in `bar_cobar_adjunction_inversion.tex`), so any rectification of `prop:coderived-adequacy` must keep that risk in mind and avoid importing unproved or conditional labels without justification.
exec
/bin/zsh -lc "rg -n \"Im\\(d\\)|boundaries|boundary|Verdier quotient|coacyclic|coderived quotient\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
29:the bar differential collects OPE residues along FM boundary strata.
39:coacyclic. The stronger chain-level statement is unconditional for
67:iterated residues on FM boundary strata
1261:The physical content (Gaiotto's framework, boundary chiral
1262:algebras, HT boundary conditions, W-algebras from Higgs branches)
1269:\label{rem:boundary-chiral-algebra-bv}%
1270:\label{rem:bar-cobar-ht-boundary}%
1877:non-separating boundary divisor
1905:\kappa / \operatorname{Im}(\tau)$ is not a coboundary
1909:resulting comparison cone is coacyclic in the sense of
1910:Definition~\ref{def:coacyclic-fact}. The remaining open question is
1953:and the cone of $f_g$ is coacyclic.
1991:Definition~\ref{def:coacyclic-fact}, these totalizations are
1992:coacyclic. Since the coacyclic subcategory is thick and closed
1993:under extensions,~$K_g$ itself is coacyclic. Therefore~$f_g$
1994:becomes an isomorphism in the coderived quotient
2021: $m_0$-power torsion and its cone is coacyclic in the sense of
2022: Definition~\ref{def:coacyclic-fact}.
2054:comparison cone to be coacyclic.
2059:using the bulk propagator, while the boundary theory is computed
exec
/bin/zsh -lc "sed -n '4858,4905p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "coderived|coacyclic|prop:coderived-adequacy|higher-genus-inversion" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is the bar-coalgebra comparison, with ordinary derived reduction only
on the flat finite-type completed-dual loci singled out in the
bar-cobar foundations.

Curved bar objects can lose ordinary cohomological visibility while
their coderived/contraderived invariants remain nontrivial. The
coderived framework is built to retain that information without
promoting the monodromy metaphor itself into a theorem.

The provisional coderived category
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
(Definition~\ref{def:provisional-coderived},
Proposition~\ref{prop:coderived-adequacy})
provides a working substitute within the scope of this monograph.
On the flat finite-type locus singled out in the bar-cobar
foundations, the coderived and derived categories agree.
Bar-cobar inversion there is genus~$0$ unconditional and, at higher
genus, unconditional on the CFT-type standard landscape except
integer-spin $\beta\gamma$ by
Theorem~\ref{thm:pbw-propagation}; in general it remains
 exited 2 in 50ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
chapters/connections/concordance.tex:39: \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
chapters/connections/concordance.tex:264: and~\ref{thm:higher-genus-inversion}).}
chapters/connections/concordance.tex:696: in the coderived category $D^{\mathrm{co}}$ for all shadow classes
chapters/connections/concordance.tex:697: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
chapters/connections/concordance.tex:1943:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
chapters/connections/concordance.tex:1955: BV=bar in the coderived category is proved for all four shadow
chapters/connections/concordance.tex:1956: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/concordance.tex:3303: (Theorem~\ref{thm:bv-bar-coderived});
chapters/connections/concordance.tex:4184: coderived category.
chapters/connections/concordance.tex:4718:$B_{\mathrm{mod}}$ & Inversion on Koszul locus; coderived & Proved on Koszul locus; & Thm~\ref{thm:higher-genus-inversion}, \\
chapters/connections/concordance.tex:4719: & persistence off it & coderived persistence conjectural & \S\ref{subsec:coderived-ran} \\[2pt]
chapters/connections/concordance.tex:4835:\subsection{The coderived Ran-space formalism}
chapters/connections/concordance.tex:4836:\label{subsec:coderived-ran}
chapters/connections/concordance.tex:4855:intrinsic coderived/contraderived bar-coalgebra framework of
chapters/connections/concordance.tex:4863:their coderived/contraderived invariants remain nontrivial. The
chapters/connections/concordance.tex:4864:coderived framework is built to retain that information without
chapters/connections/concordance.tex:4867:The provisional coderived category
chapters/connections/concordance.tex:4869:(Definition~\ref{def:provisional-coderived},
chapters/connections/concordance.tex:4870:Proposition~\ref{prop:coderived-adequacy})
exec
/bin/zsh -lc "sed -n '528,545p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
| `lem:obs-def-pairing` | `lemma` | 3278 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 3326 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3405 | Curved differential formula |

#### `chapters/theory/coderived_models.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 244 | Adequacy |
| `prop:coderived-bar-degree-spectral-sequence` | `proposition` | 306 | Coderived bar-degree spectral sequence |
| `thm:stratified-conservative-restriction` | `theorem` | 654 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 730 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 780 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 807 | Factorization co-contra correspondence |
| `thm:off-koszul-ran-inversion` | `theorem` | 901 | Off-Koszul bar-cobar inversion on Ran |

#### `chapters/theory/computational_methods.tex` (17)

exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '890,985p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   890	for $C = \barB^{\mathrm{fact}}(\cA)$ with sectorwise finiteness
   891	\textup{(}hypothesis~\ref{h2:sectorwise}\textup{)}, it records the
   892	factorization coderived/contraderived comparison for comodules and
   893	contramodules over the same curved factorization coalgebra~$C$, and
   894	then explains separately how this comparison interfaces with the
   895	Koszul-locus generated-core duality of
   896	Theorem~\ref{thm:h-level-factorization-kd}.
   897	\end{remark}
   898	
   899	\begin{theorem}[Off-Koszul bar-cobar inversion on Ran;
   900	\ClaimStatusProvedHere]
   901	\label{thm:off-koszul-ran-inversion}
   902	\index{bar-cobar inversion!off-Koszul|textbf}
   903	\index{coderived category!bar-cobar inversion}
   904	Let $\cA$ be a complete augmented chiral algebra on~$X$ with
   905	$\barB_X^{\mathrm{fact}}(\cA)$ having finite-dimensional graded
   906	pieces. Then the bar-cobar counit
   907	\[
   908	\Omega_X \barB_X(\cA) \longrightarrow \cA
   909	\]

thinking
**Inspecting mathematical concepts**

I'm thinking about this theorem that proves off-Koszul inversion. I wonder if prop adequacy could be applied, but it seems not directly. Maybe there’s a connection with circularity if I use a theorem for higher genus inversion? It looks like I need to inspect line 545 in the target material for a specific definition. I’ll check the lines around 540-550 to get clearer insights on this!
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '536,550p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   536	 (the cross terms cancel by the graded Leibniz rule).
   537	\end{enumerate}
   538	Conilpotence holds because the bar construction is cofree
   539	conilpotent: $C = T^c(s^{-1}\bar{\cA})$ with the coradical
   540	filtration exhaustive by completeness of~$\cA$
   541	(Proposition~\ref{prop:bar-fh}).
   542	\end{example}
   543	
   544	\begin{remark}[The CDG tensor product formula]
   545	\label{rem:curvature-factorization}
   546	\index{CDG-coalgebra!tensor product}
   547	Given CDG-coalgebras $(C_1, d_1, h_1)$ and $(C_2, d_2, h_2)$,
   548	the tensor product $C_1 \otimes C_2$ carries the CDG structure
   549	$d = d_1 \otimes 1 + 1 \otimes d_2$,
   550	$h = h_1 \otimes \varepsilon_2 + \varepsilon_1 \otimes h_2$.

thinking
**Inspecting mathematical concepts**

I'm thinking that addressing the issue would definitely help with consistency and rule out naive quotients. I need to search for the phrase "coacyclic quotients" since it's relevant here. This is within the target, and it seems like it should be fixed. I might also need to check the usage of Positselski's theorem, specifically Proposition 3.5, to see if it's about the equivalence between associated graded quasi-iso and isomorphism in the Verdier quotient. For now, I think I'll wait a bit longer for exploration.
collab wait(call_kCcHT21IaMrSzxrVGdLVqp6Q)
  receivers: 019d868c-b49a-79d3-b3ab-7adda65fd5e5
wait(call_kCcHT21IaMrSzxrVGdLVqp6Q) 1 agents complete:
  019d868c-b49a-79d3-b3ab-7adda65fd5e5 completed: "- `CLAUDE.md:508-540` flags MC5 as “analytic proved, coderived proved, chain-level conjectural,” so the BV=bar compariso…"


thinking
**Considering technical edits**

I think making changes could strengthen technical correctness and help clarify the definitions. I wonder if T12 wants a fix because the internal definition and its later usage seems a bit ambiguous. It sounds like I should patch the definition for `curved-weak-equiv(ii)` and maybe include a remark to differentiate between the cone criterion and boundaries. As for the edit, it states that the image of `f` is an isomorphism, and that the cone of `f` is coacyclic.
thinking
**Considering code verification steps**

I'm thinking about the need to inspect the `def:curved-weak-equiv` lines around 210, especially if there are patches involved. I'll need to verify labels and references, possibly using grep or ripgrep since there's only one file. I wonder: should I run `rg` for specific definitions? However, it seems like running latexmk might be overkill. Maybe it would be better to check for unmatched references with a simpler approach. Since no new labels were introduced, they should be valid. I could perform a local reread after edits to ensure everything is in order.
codex
I’ve verified the strong direction for both findings. The coderived definitions in this file are already the correct Verdier-localization definitions, but `def:curved-weak-equiv` still uses misleading quotient notation; I’m replacing that with explicit Verdier-quotient language and adding a short clarification that coderived localization is not “mod `Im(d)`.” I’m also making `prop:coderived-adequacy(a)` explicitly independent of `Theorem~ref{thm:higher-genus-inversion}` so the non-circular proof is visible in the local text itself.
Plan update
The definitions are substantively correct; the local repair is to remove misleading quotient notation, make the Verdier-localization criterion explicit on both coderived definitions, and add an explicit non-circularity sentence to prop:coderived-adequacy(a).
  ✓ Read constitutional and target surfaces; lock definitions, labels, and dependency graph for the two findings
  → Edit chapters/theory/coderived_models.tex with the minimum truthful fix for both findings
  • Re-read modified sections and run narrow verification for labels/refs/coherence
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '206,236p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   206	 decreasing filtration with $d(F^p) \subset F^p$,
   207	 $m_0 \in F^1$, and $\operatorname{gr}^0_{\mathcal{F}} d$ strict
   208	 ($(\operatorname{gr}^0 d)^2 = 0$).
   209	\end{enumerate}
   210	A morphism $f \colon (M, d, \mathcal{F}) \to (N, d', \mathcal{F}')$ is a
   211	filtration-preserving coalgebra map compatible with differentials and curvatures.
   212	\end{definition}
   213	
   214	\begin{definition}[Weak equivalence of curved models]
   215	\label{def:curved-weak-equiv}
   216	A morphism $f \colon M \to N$ of filtered curved factorization models
   217	is a \emph{weak equivalence} if it satisfies either of the following
   218	equivalent conditions:
   219	\begin{enumerate}[label=\textup{(\roman*)}]
   220	\item The associated graded map
   221	 $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
   222	 strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
   223	 \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
   224	\item The induced map on coacyclic quotients
   225	 $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an

thinking
**Clarifying mathematical notation**

I'm thinking about how the equivalence with Positselski Proposition 3.5 needs a bit more precision. It might be better to specify that it's "for bounded-below filtrations by the usual filtered-totalization criterion," instead of using direct quotient notation. I guess it’s important to articulate these details clearly to avoid any misunderstanding! I wonder if this will help improve the clarity of my explanation when discussing this proposition.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex
@@ -98,2 +98,9 @@
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
@@ -223,7 +230,7 @@
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
@@ -253,6 +260,6 @@
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
@@ -282,3 +289,6 @@
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
@@ -647,2 +657,8 @@
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
apply_patch(auto_approved=true) exited 0 in 48ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}

file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}

codex
The patch is in. I’m re-reading the four touched surfaces now: the abstract coderived definition, weak-equivalence definition, `prop:coderived-adequacy(a)`, and the factorization coderived definition, to make sure the Verdier-localization language is coherent and the non-circular proof reads cleanly in context.
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '214,292p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '76,108p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    76	\label{def:coderived-contraderived-abstract}
    77	\index{coderived category!abstract definition|textbf}
    78	\index{contraderived category!abstract definition|textbf}
    79	The \emph{coderived category} and \emph{contraderived category}
    80	of a CDG-coalgebra $(C, d, h)$ are the Verdier quotients:
    81	\begin{align}
    82	D^{\mathrm{co}}(C\text{-}\mathrm{comod})
    83	 &:= \mathrm{Hot}(C\text{-}\mathrm{comod})
    84	 \,\big/\, \mathrm{Acycl}^{\mathrm{co}}(C\text{-}\mathrm{comod}),
    85	 \label{eq:coderived-abstract}\\
    86	D^{\mathrm{ctr}}(C\text{-}\mathrm{contra})
    87	 &:= \mathrm{Hot}(C\text{-}\mathrm{contra})
    88	 \,\big/\,
    89	 \mathrm{Acycl}^{\mathrm{ctr}}(C\text{-}\mathrm{contra}).
    90	 \label{eq:contraderived-abstract}
    91	\end{align}
    92	These are triangulated categories. When $h = 0$, every acyclic
    93	object is coacyclic (resp.\ contraacyclic), so there are natural
    94	functors $D^{\mathrm{co}} \to D$ and $D^{\mathrm{ctr}} \to D$
    95	from the exotic to the ordinary derived category. When
 succeeded in 51ms:
   214	 $m_0 \in F^1$, and $\operatorname{gr}^0_{\mathcal{F}} d$ strict
   215	 ($(\operatorname{gr}^0 d)^2 = 0$).
   216	\end{enumerate}
   217	A morphism $f \colon (M, d, \mathcal{F}) \to (N, d', \mathcal{F}')$ is a
   218	filtration-preserving coalgebra map compatible with differentials and curvatures.
   219	\end{definition}
   220	
   221	\begin{definition}[Weak equivalence of curved models]
   222	\label{def:curved-weak-equiv}
   223	A morphism $f \colon M \to N$ of filtered curved factorization models
   224	is a \emph{weak equivalence} if it satisfies either of the following
   225	equivalent conditions:
   226	\begin{enumerate}[label=\textup{(\roman*)}]
   227	\item The associated graded map
   228	 $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
   229	 strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
   230	 \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
   231	\item In the ambient homotopy category, the cone
   232	 $\operatorname{cone}(f)$ belongs to the thick subcategory generated
   233	 by totalizations of short exact sequences and infinite direct sums;
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '622,650p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "def:coderived-contraderived-abstract|def:curved-weak-equiv|prop:coderived-adequacy|def:coderived-fact|thm:higher-genus-inversion" chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
76:\label{def:coderived-contraderived-abstract}
222:\label{def:curved-weak-equiv}
247:equivalences of Definition~\ref{def:curved-weak-equiv}.
251:\label{prop:coderived-adequacy}
291:Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
632:\label{def:coderived-fact}
766:(Definition~\ref{def:curved-weak-equiv}(i)) induces a
787:(Proposition~\ref{prop:coderived-adequacy}(b)) provides the
 succeeded in 51ms:
   622	 infinite direct products.
   623	\end{enumerate}
   624	This is the factorization analogue of
   625	Definition~\ref{def:coacyclic-contraacyclic}. The factorization
   626	structure enters through the ambient homotopy category (whose
   627	objects and morphisms respect the factorization isomorphisms), not
   628	through any additional axiom on the coacyclicity condition.
   629	\end{definition}
   630	
   631	\begin{definition}[Coderived and contraderived factorization categories]
   632	\label{def:coderived-fact}
   633	\index{coderived category!factorization|textbf}
   634	\index{contraderived category!factorization|textbf}
   635	The \emph{coderived} and \emph{contraderived factorization
   636	categories} of a curved factorization coalgebra $(C, d, h)$
   637	on~$X$ are the Verdier quotients
   638	\begin{align}
   639	D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})
   640	 &:= \mathrm{Hot}(C\text{-}\mathrm{CoFact})
   641	 \,\big/\, \mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}},
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}

exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '648,666p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   648	When $h = 0$ and $C$ is conilpotent,
   649	Theorem~\ref{thm:conilpotent-reduction} gives
   650	$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})
   651	\simeq D(C\text{-}\mathrm{CoFact})$.
   652	When $h \neq 0$, ordinary cohomological derived methods no longer
   653	capture the curved factorization theory; on the higher-genus
   654	bar-complex surfaces treated in this monograph the underlying bar
   655	objects are acyclic
   656	\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
   657	while $D^{\mathrm{co}}$ retains the full categorical information.
   658	Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
   659	becomes an isomorphism in
   660	$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
   661	in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
   662	Verdier localization by the factorization coacyclic thick
   663	subcategory, not a quotient by $\operatorname{Im}(d)$.
   664	\end{definition}
   665	
   666	\subsubsection*{Structural theorems}
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}


thinking
**Finalizing proof details**

I think everything looks good so far. I need to ensure that the equivalence of (i) and (ii) holds for bounded-below filtrations, as mentioned in Proposition 3.5. I’ll double-check that after the restatement. Alright, I also need to go back and open lines 292 onward to finish the proof. I'll focus on completing that to make sure I don’t miss any key details!
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '290,302p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   290	the filtered cone vanishes. This proof is independent of
   291	Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
   292	curvature-zero Cousin model together with Positselski's filtered
   293	coacyclicity criterion. By
   294	\cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
   295	curved object with acyclic associated graded is coacyclic.
   296	Therefore $K$ lies in the thick subcategory generated by
   297	totalizations of short exact sequences and infinite direct sums, so
   298	$\varepsilon$ is a coacyclic-equivalence and hence an isomorphism in
   299	$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
   300	
   301	For (b): the PBW filtration by conformal weight is exhaustive,
   302	decreasing, preserved by all three components of the bar differential,
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}


thinking
**Verifying references and labels**

I need to check if all my \ref and \label commands are valid. We didn’t add labels yet, and I might want to run a check with a TeX parser or use `rg` to see if specific labels exist. It seems like a good idea to ensure everything's correct, but verification already shows they should be valid. I could narrow my checks to specific referenced labels, but it might not be necessary. Running a `git diff` on the target file could help too.
codex
The local reread is coherent. I’m doing one last narrow verification pass now: diffing the file and checking the referenced label surfaces so I can confirm both findings are resolved without introducing a status or reference drift.
exec
/bin/zsh -lc 'git diff -- chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\label\\{thm:higher-genus-inversion\\}|\\\\label\\{def:coacyclic-fact\\}|\\\\label\\{def:coderived-contraderived-abstract\\}|\\\\label\\{def:coderived-fact\\}|\\\\label\\{prop:coderived-adequacy\\}\" chapters/theory/coderived_models.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 3019047..5e4c105 100644
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@ from the exotic to the ordinary derived category. When
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@ equivalent conditions:
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
 exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{thm:higher-genus-inversion\}|\label\{def:coacyclic-fact\}|\label\{def:coderived-contraderived-abstract\}|\label\{def:coderived-fact\}|\label\{prop:coderived-adequacy\})
       ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}

codex
The diff is scoped correctly. One quick label-check command had a regex escaping error; I’m rerunning it with fixed-string patterns rather than regex so the final verification is clean.
exec
/bin/zsh -lc "rg -n -F -e '\\label{thm:higher-genus-inversion}' -e '\\label{def:coacyclic-fact}' -e '\\label{def:coderived-contraderived-abstract}' -e '\\label{def:coderived-fact}' -e '\\label{prop:coderived-adequacy}' chapters/theory/coderived_models.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/coderived_models.tex:76:\label{def:coderived-contraderived-abstract}
chapters/theory/coderived_models.tex:251:\label{prop:coderived-adequacy}
chapters/theory/coderived_models.tex:604:\label{def:coacyclic-fact}
chapters/theory/coderived_models.tex:632:\label{def:coderived-fact}
chapters/theory/higher_genus_complementarity.tex:4355:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}


thinking
**Updating the plan**

I think I need to refine my plan to indicate that a full TeX build won't run. Perhaps a small syntax check could be useful, but maybe it's unnecessary for what I need. Narrow verification might suffice. I should also look into whether the patch affected the indentation around the theorem item lines 260-262, but maybe I can skip that. It might be worth checking for the new "quotient by Im(d)" phrase in the target, so I’ll search for that.
exec
/bin/zsh -lc "rg -n \"Im\\(d\\)|coacyclic quotients|Theorem~\\\\ref\\{thm:higher-genus-inversion\\}: it uses only\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}


thinking
**Reassessing regex match issues**

It looks like I ran into a problem with the regex not returning any matches. Maybe it’s related to the backslash or the way I formatted the string. I should consider using a fixed string instead. But honestly, it might not be that crucial right now. I guess the command might have had an issue due to escaping characters. Anyway, I've got enough to move forward and update my plan with step 3 completed!
Plan update
Patched only chapters/theory/coderived_models.tex, re-read all modified blocks in context, diffed the file, and confirmed the referenced labels still exist.
  ✓ Read constitutional and target surfaces; lock definitions, labels, and dependency graph for the two findings
  ✓ Edit chapters/theory/coderived_models.tex with the minimum truthful fix for both findings
  ✓ Re-read modified sections and run narrow verification for labels/refs/coherence
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}


thinking
**Compiling rectification summary**

I need to ensure the final response is concise, summarizing changes and statuses effectively. I should state that there was no build run. It's important to mention specific changes made in the document and provide verification details, such as the edited sections and any relevant file links. I'll note that Finding 1 addressed the ambiguous notation, while Finding 2 clarified the independence in a previously existing proof. After this, I’ll close with a structured summary of the findings.

## Rectification Summary
- FIXED: Finding 1
- FIXED: Finding 2
- No full TeX build run
codex
Edited [chapters/theory/coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex) only.

The coderived definitions were already substantively correct. I made that explicit in both the abstract and factorization definitions by stating the cone criterion for Verdier localization and by ruling out the naive “mod `\operatorname{Im}(d)`” reading. I also replaced the misleading “coacyclic quotients `M/\operatorname{coacyc}(M)`” language in `def:curved-weak-equiv` with the intrinsic cone/coacyclic Verdier-localization criterion.

For `prop:coderived-adequacy(a)`, the proof was already independent of `Theorem~\ref{thm:higher-genus-inversion}`; I made that independence explicit in the proof, identifying the actual inputs as the strict curvature-zero Chevalley--Cousin comparison and Positselski’s filtered coacyclicity criterion. I re-read the modified sections in context, diffed the file, and confirmed the referenced labels still exist. I did not run a full TeX build.

## Rectification Summary
- [FIXED] finding 1 — kept the Verdier-quotient definition, added explicit cone/coacyclic characterization at both coderived definitions, and removed the misleading quotient notation in `def:curved-weak-equiv` that could be read as “boundaries mod `\operatorname{Im}(d)`.”
- [FIXED] finding 2 — kept `prop:coderived-adequacy(a)` as proved, and made the proof explicitly non-circular by stating that it does not use `thm:higher-genus-inversion`, only the strict Chevalley--Cousin quasi-isomorphism and Positselski’s filtered criterion.
file update:
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 30190477a8f37a50b008c4ce484f6c52282dbb37..5e4c105b2d070fcb3103b0f27ed0bb2dddf296e8
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -96,6 +96,13 @@
 $h \neq 0$, the ordinary cohomological derived category no longer
 captures the curved theory, while $D^{\mathrm{co}}$ and
 $D^{\mathrm{ctr}}$ retain the relevant structure~\cite[\S\S3--4]{Positselski11}.
+Equivalently, a morphism in the homotopy category becomes an
+isomorphism in $D^{\mathrm{co}}$ \textup{(}resp.\
+$D^{\mathrm{ctr}}$\textup{)} exactly when its cone is coacyclic
+\textup{(}resp.\ contraacyclic\textup{)}. This is a Verdier
+localization by a thick subcategory, not a quotient by ordinary
+coboundaries such as $\operatorname{Im}(d)$; in the curved case,
+$d^2$ need not vanish on the chain level.
 \end{definition}
 
 \begin{theorem}[Comodule-contramodule correspondence;
@@ -221,11 +228,11 @@
  $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
  strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
  \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
-\item The induced map on coacyclic quotients
- $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
- isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
- generated by totalizations of short exact sequences
- (Positselski~\cite{Positselski11}).
+\item In the ambient homotopy category, the cone
+ $\operatorname{cone}(f)$ belongs to the thick subcategory generated
+ by totalizations of short exact sequences and infinite direct sums;
+ equivalently, $f$ becomes an isomorphism after Verdier localizing by
+ that thick subcategory \textup{(}Positselski~\cite{Positselski11}\textup{)}.
 \end{enumerate}
 The equivalence of (i) and (ii) holds for bounded-below filtrations
 by~\cite[Proposition~3.5]{Positselski11}.
@@ -251,10 +258,10 @@
  in $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ for every chiral
  algebra~$\cA$ satisfying the Chevalley--Cousin condition.
 \item The genus tower $\{\bar{B}^{(g)}(\cA)\}_{g \geq 0}$ of
- Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
- filtrations making each genus component a filtered curved model.
+Theorem~\textup{\ref{thm:prism-higher-genus}} has compatible
+filtrations making each genus component a filtered curved model.
 \item The Verdier involution $\sigma$ acts on filtered curved models
- and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
+and descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$,
  so the complementarity decomposition
  \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}
  holds in the provisional coderived category.
@@ -280,7 +287,10 @@
 Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
 Cousin-filtration argument gives that strict counit as a
 quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
-the filtered cone vanishes. By
+the filtered cone vanishes. This proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
+curvature-zero Cousin model together with Positselski's filtered
+coacyclicity criterion. By
 \cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
 curved object with acyclic associated graded is coacyclic.
 Therefore $K$ lies in the thick subcategory generated by
@@ -645,6 +655,12 @@
 objects are acyclic
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
 while $D^{\mathrm{co}}$ retains the full categorical information.
+Equivalently, a morphism in $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
+becomes an isomorphism in
+$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$ exactly when its cone lies
+in $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$. Again, this is a
+Verdier localization by the factorization coacyclic thick
+subcategory, not a quotient by $\operatorname{Im}(d)$.
 \end{definition}
 
 \subsubsection*{Structural theorems}

tokens used
91,811
