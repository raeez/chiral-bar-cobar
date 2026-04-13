# H23_vol2_bar_cobar_review_heal (350s)



---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar-vol2
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d86b9-94cc-7f40-b126-a9c121161453
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


HEAL the bar-cobar review chapter.

TARGET: ~/chiral-bar-cobar-vol2/chapters/theory/bar-cobar-review.tex

This chapter reviews Vol I results for Vol II readers. After rectification:
1. Verify Theorem A stated with correct Verdier convention (algebra level)
2. Verify Theorem B stated with on-locus qi + off-locus coderived
3. Verify Theorem C with g>=1 for C1, curved qualifier for C0
4. Verify Theorem D with non-circular proof path noted
5. Verify MC2 correctly attributes g^{mod} carrier
6. Add a "What changed in Vol I" remark listing the rectifications

Fix all stale claims.
mcp startup: no servers
codex
Targeting [chapters/theory/bar-cobar-review.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/bar-cobar-review.tex) and using `vol2-beilinson-rectification` first. I’m reading the live chapter, the current dirty surface, and the relevant skill instructions before I edit anything.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 M chapters/connections/3d_gravity.tex
exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
---
name: vol2-beilinson-rectification
description: Use when the user asks to audit, rectify, fortify, fix, tighten, or converge a Vol II chapter, theorem, proof, introduction, appendix, or the live manuscript surface. Do not use for purely local copyedits with no mathematical or structural truth conditions.
---

# Vol II Beilinson Rectification

Run the full local rectification loop on the live surface.

## Inputs

- exact target file or theorem if given
- otherwise the smallest live surface implied by the user prompt

## Mandatory loop

1. Start with a short progress update naming the target and first verification step.
2. Register a nontrivial task in `update_plan`.
3. Read before editing:
   - target file
 exited 1 in 51ms:
sed: chapters/theory/bar-cobar-review.tex: No such file or directory

thinking
**Locating file paths**

I might need to check if the file path is different somehow. It feels a bit confusing. I think I should use a tool like `rg` to help locate the file. Maybe I also need to update my plan if the file is missing? Let’s explore that a bit more and see how I can search effectively. I definitely want to make sure I’m on the right track!
codex
The named target path does not exist as written, so I’m locating the live chapter and its inclusion path before touching anything. After that I’ll lock the theorem surfaces and record the hostile-pass findings in the audit ledger.
Plan update
Rectifying and fortifying the Vol II bar-cobar review chapter requires reading the live surface, auditing the theorem statements against the requested conventions, repairing the chapter, recording findings, and then running a narrow verification/build pass.
  → Locate the live bar-cobar review chapter and read its surrounding manuscript context plus active input map
  • Audit theorem statements/proofs against the requested Theorems A-D, MC2, and stale-claim surfaces; record findings in compute/audit/linear_read_notes.md
  • Edit the chapter to repair statements, add alternative proof paths/remarks, and add a Vol I changes remark
  • Run targeted verification (greps/build checks), re-audit the modified surface, and summarize theorem-by-theorem fortification status
exec
/bin/zsh -lc "rg --files | rg 'bar.*cobar.*review|review.*bar.*cobar|bar-cobar'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\input\\{|bar-cobar-review|bar cobar|Bar-Cobar|Theorem A|Theorem B|Theorem C|Theorem D|MC2' main.tex chapters" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/bar-cobar-review.tex
 succeeded in 50ms:
main.tex:1204:\input{chapters/frame/preface}
main.tex:1206:\input{chapters/theory/introduction}
main.tex:1242:\input{chapters/theory/foundations}
main.tex:1243:\input{chapters/theory/locality}
main.tex:1244:\input{chapters/theory/axioms}
main.tex:1245:\input{chapters/theory/equivalence}
main.tex:1246:\input{chapters/theory/bv-construction}
main.tex:1247:\input{chapters/theory/factorization_swiss_cheese}
main.tex:1248:\input{chapters/theory/raviolo}
main.tex:1249:\input{chapters/theory/raviolo-restriction}
main.tex:1250:\input{chapters/theory/fm-calculus}
main.tex:1251:\input{chapters/theory/orientations}
main.tex:1252:\input{chapters/theory/fm-proofs}
main.tex:1253:\input{chapters/theory/pva-descent-repaired}
main.tex:1254:\input{chapters/theory/pva-expanded-repaired}
main.tex:1289:\input{chapters/connections/bar-cobar-review}
main.tex:1290:\input{chapters/connections/line-operators}
main.tex:1291:\input{chapters/connections/ordered_associative_chiral_kd_core}
main.tex:1292:\input{chapters/connections/dg_shifted_factorization_bridge}
main.tex:1293:\input{chapters/connections/thqg_gravitational_yangian}
 succeeded in 51ms:
\documentclass[11pt]{memoir}
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{2}

% ==========================================
% FONTS: EB Garamond (matching Volume I)
% ==========================================

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\frenchspacing

\usepackage[
 cmintegrals,
 cmbraces,
 noamssymbols
]{newtxmath}
\usepackage{ebgaramond}

exec
/bin/zsh -lc "sed -n '1,280p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- chapters/connections/bar-cobar-review.tex main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\providecommand{\IC}{\mathrm{IC}}

\section{The bar complex as twisting morphism classifier}
\label{sec:bar_cobar}

The bar complex~$\barB(\cA)$ classifies \emph{twisting morphisms}:
universal couplings between the boundary algebra~$\cA$ and its
Koszul dual~$\cA^!$. It is the coalgebraic shadow of the open
factorization category (Part~\ref{part:swiss-cheese},
\S\ref{subsec:categorical-open-sector}), not the universal bulk
(which is the chiral derived center of
\S\ref{sec:chiral_hochschild}). The bar--cobar duality for $\Ainf$
chiral algebras extends the quadratic theory of
Gui--Li--Zeng~\cite{GLZ22} to the non-quadratic setting.

\begin{remark}[$E_1$ primacy of the bar--cobar review]
\label{rem:bar-cobar-e1-primacy}
This chapter is natively $E_1$ content. The bar differential is
built from collision residues on ordered configurations, and the
deconcatenation coproduct preserves the linear ordering.
 succeeded in 51ms:
# Linear Read Notes

## 2026-04-13 - V2-AP26 Part Reference Rectification

- Target: `chapters/connections/conclusion.tex`, mirrored `.claude/worktrees/*/chapters/connections/conclusion.tex`
- Status: COMPLETE

### Findings

1. `2026-04-13-001`
   Severity: `MODERATE`
   Class: `D/W`
   Location: `chapters/connections/conclusion.tex:987-990` and mirrored `.claude/worktrees/*/chapters/connections/conclusion.tex`
   Issue: the frontier summary still hardcoded `Part~VII` and `Parts~I--VI`, violating `V2-AP26` after the seven-part restructuring.
   Fix: replaced the hardcoded prose with `Part~\ref{part:frontier}` and `Parts~\ref{part:swiss-cheese}--\ref{part:gravity}` in the live file and in each mirrored worktree copy that still advertised the stale text.
   Status: `FIXED`

### Verification

- Ran `grep -rn 'Part~[IVXL]' chapters/` before patching to isolate the live violation.
 succeeded in 50ms:


thinking
**Searching for theorems**

I need to read more of the chapter beyond 280 lines, as it might encompass important theorem summaries. I should search for theorem labels and compare them to the results in Volume I. It’s likely that there are theorems labeled A-D, including MC2 statements in this chapter. I’ll need to inspect the relevant sections around those theorems. Using "rg" on this file for labels and theorem names would be helpful!
codex
I’ve located the live chapter at [chapters/connections/bar-cobar-review.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bar-cobar-review.tex); it is active in `main.tex` and currently clean. Next I’m isolating the Theorem A–D / MC2 statements in this chapter and matching them against the imported Vol I labels before I edit.
exec
/bin/zsh -lc "sed -n '280,760p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'thm:bar-cobar-adjunction|thm:bar-cobar-inversion|thm:complementarity|thm:modular-characteristic|mc2|g\\"'^'"\\{mod\\}|Verdier|coderived|curved' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Theorem A|Theorem B|Theorem C|Theorem D|MC2|Verdier|coderived|curved|non-circular|What changed|Vol I' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
binary trees gives the formula. The sum converges in the
filtration-complete topology ensured by tameness
(Definition~\ref{def:tameness}).
\end{proof}

\begin{remark}[Content]
\label{rem:c-linearity-content}
The $c$-linearity theorem states that the
field-dependent part of $m_k$ (the ``backreaction'') is
universal, independent of the central charge, while the
scalar contact term is controlled by a single coupling
constant. Finite presentation states that one binary
operation and one homotopy produce the entire infinite
tower. The tower may not truncate ($m_k \ne 0$ for all
$k \ge 3$ generically), but the generating data are finite.
Both results specialise to concrete formulas in examples:
for the Virasoro algebra, see
Theorem~\ref{thm:gravity-c-linearity} and
Theorem~\ref{thm:gravity-finite-presentation}.
\end{remark}
 succeeded in 51ms:
373:\textup{(}via Verdier duality; note
731: the bar complex is \emph{uncurved}.
1309:For curved $A_\infty$ algebras (where $m_0 \neq 0$, i.e., a curvature term), the bar--cobar formalism extends by including a \emph{curved differential}:
1318:This controls \emph{curved deformations} of chiral algebras, relevant for non-flat connections in quantum field theory.
1569:differential, Arnold relations, Verdier intertwining) and uses the
1621: Verdier duality $\mathbb{D}_{\operatorname{Ran}}$ produces the
1754:$\cA \mapsto \cA^!_{\mathrm{ch}}$ via Verdier duality
1818: Theorems~\textup{\ref{thm:bar-cobar-adjunction}}
1915:Theorem~\ref{thm:bar-cobar-adjunction}, unconditional by
2155:the curved bar equation.
2156:The curved bar equation $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$
2278: whose bar coalgebra is identified with the Verdier dual:
2391:determined by the Verdier intertwining
2413:non-formal; the higher operations \emph{are} the curved bar
3718:\subsection{The genus tower: curved $\R$-factorization}
3724:of~$\Sigma_g$, and the fiberwise bar differential becomes curved:
3725:\begin{equation}\label{eq:curved-R-fact}
3733:\label{prop:curved-R-factorization}
3789:Theorem~\ref{thm:rosetta-curved}\textup{(c)}.
3808:deforms the $\Eone$ structure into a curved $\Ainf$ structure
 succeeded in 50ms:
373:\textup{(}via Verdier duality; note
731: the bar complex is \emph{uncurved}.
1309:For curved $A_\infty$ algebras (where $m_0 \neq 0$, i.e., a curvature term), the bar--cobar formalism extends by including a \emph{curved differential}:
1318:This controls \emph{curved deformations} of chiral algebras, relevant for non-flat connections in quantum field theory.
1569:differential, Arnold relations, Verdier intertwining) and uses the
1621: Verdier duality $\mathbb{D}_{\operatorname{Ran}}$ produces the
1754:$\cA \mapsto \cA^!_{\mathrm{ch}}$ via Verdier duality
2155:the curved bar equation.
2156:The curved bar equation $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$
2278: whose bar coalgebra is identified with the Verdier dual:
2391:determined by the Verdier intertwining
2413:non-formal; the higher operations \emph{are} the curved bar
3718:\subsection{The genus tower: curved $\R$-factorization}
3724:of~$\Sigma_g$, and the fiberwise bar differential becomes curved:
3725:\begin{equation}\label{eq:curved-R-fact}
3733:\label{prop:curved-R-factorization}
3789:Theorem~\ref{thm:rosetta-curved}\textup{(c)}.
3808:deforms the $\Eone$ structure into a curved $\Ainf$ structure
3834:At genus $g \geq 1$, this produces a \emph{curved} raviolo vertex
3837:curved quasi-isomorphism, recovering $\cA$ in the coderived


thinking
**Searching for theorem labels**

I need to gather more information on theorem labels, specifically looking for "thm:bar-cobar-adjunction." I’m wondering if there’s an underscore or hyphen mismatch because I’ve found "thm:bar_cobar_adjunction." Also, earlier searches suggested that references to "thm:bar-cobar-adjunction" might be broken, so I’ll need to inspect around line 1800. It seems like using a tool to check for labels and reference mismatches would be a good idea to clarify this.
thinking
**Verifying Theorem A**

I need to verify Theorem A with the correct Verdier convention at the algebra level. It seems like there could be a summary section for the theorems near the beginning or later in the document that includes Theorems A to D. My next step is to search for that section to ensure I have the right details and information needed for verification.
exec
/bin/zsh -lc "rg -n 'Theorem~A|Theorem A|thm:bar[-_]cobar|thm:complement|thm:modular|thm:bar-terminality|thm:duality-involution|MC2|Theta' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1500,2050p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2050,2500p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
205:(Theorem~A): $d_Q$ encodes the internal differential $m_1$,
320:\label{thm:bar_cobar_adjunction}
405:The bar-cobar adjunction (Theorem~\ref{thm:bar_cobar_adjunction})
445:By Theorem~\ref{thm:bar_cobar_adjunction}, there is a natural
625:This is exactly the content of Volume~I Theorem~A: the bar differential squares to zero, equivalently, the $\Ainf$ relations hold.
631:\textbf{Step 5: Pullback.} For any twisting morphism $\tau: \cC \to \cA$ (equivalently, a coalgebra map $f_\tau: \cC \to \barB(\cA)$ by Theorem~\ref{thm:bar-terminality}), the pullback $f_\tau^* \cE_{\mathrm{univ}}$ is a chiral $\cA$-module on $\cC$:
696:(Theorem~\ref{thm:duality-involution}) interchanges
765:\label{thm:bar-terminality}
919:Theorem~\ref{thm:bar-terminality}: $\tau$ determines a unique
1132:Theorem~\ref{thm:bar-terminality}.
1172:twisting morphism~$\Theta_\cA$
1180:is the cogenerator projection of~$\Theta_\cA$; the
1182:product parametrized by~$\Theta_\cA$; the genus-$g$ curvature
1184:extension of~$\Theta_\cA$; the five theorems of Volume~I
1189:object $\Theta_\cA$ suffices: it is the terminal twisting morphism,
1355:By Volume~I, Theorem~A, the bar differential $d_{\barB}$ satisfies
1620: $\operatorname{Ran}(X)$ constructed in Volume~I, Theorem~A\@.
1699:(Theorem~\ref{thm:duality-involution}).
1721:locus \textup{(}Theorem~\textup{\ref{thm:duality-involution})}.
1747:(Theorem~\ref{thm:duality-involution}).
 succeeded in 51ms:
(Lurie~\cite{HA}, \S5.5.4.10), factorisation homology
on $\bR$ is the identity:
$\int_{\bR} A \simeq A$.
This holds because $\bR$ is contractible and has no
boundary where augmentation could impose conditions.
The geometric point: $\bR$ is the \emph{universal cover}
of all compact $1$-manifolds, and factorisation homology
on the universal cover is the algebra itself (no
identifications, no coinvariants, no derived tensor
products).

\textbf{Part (iv).}
The $\otimes$-excision property of
Ayala--Francis~\cite{AF15} (Theorem~3.24) states that
for a collar-gluing $M = M_L \cup_{M_0} M_R$ of manifolds
with boundary, factorisation homology satisfies
$\int_M A \simeq \int_{M_L} A \otimes_{\int_{M_0} A}
\int_{M_R} A$.
Applied to $[0,1] = [0,t] \cup_{\{t\}} [t,1]$, this gives
$B(A) \simeq B(k,A,A) \otimes_A B(A,A,k)$, a derived tensor
 succeeded in 50ms:
\providecommand{\Steinb}{\mathfrak{S}}

\begin{theorem}[Formal bar model for the Lagrangian self-intersection;
\ClaimStatusProvedHere]
\label{thm:bar-is-self-intersection}
\index{bar complex!as Lagrangian self-intersection|textbf}
\index{Lagrangian!self-intersection!bar complex|textbf}
\index{Steinberg!as bar complex|textbf}
Let $\cM$ be a $(-2)$-shifted symplectic derived stack and
$\cL \hookrightarrow \cM$ a Lagrangian. Write
$B = \cO(\cL)$ for the algebra of functions on~$\cL$.
Then:
\begin{enumerate}[label=\textup{(\roman*)},leftmargin=2em]
\item The derived self-intersection
 $\Steinb := \cL \times_{\cM}^h \cL$
 carries a $(-1)$-shifted symplectic structure
 \textup{(}PTVV \cite{PTVV13}, Theorem~2.9\textup{)}.
\item The derived tensor product
 $\cO(\Steinb)=B\otimes^{\mathbb L}_{\cO(\cM)}B$
 admits, in the formal neighborhood of~$\cL$, a standard

thinking
**Investigating theorem section**

I need to find the summary section for the theorem, probably around line 1172. I'm looking for the "five main theorems" that might be mentioned. It makes sense to inspect the content between lines 1120 and 1200 to ensure I catch everything relevant. There could be some important details in that range that I'm wanting to dig into. Let's see what I can uncover in that section!
exec
/bin/zsh -lc "sed -n '1080,1225p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '4040,4125p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
companion to it.
\end{remark}

\begin{remark}[The boundary path]
\label{rem:boundary-path}
Volume~I's recovery diagram in the deformation-theory chapter identifies three
paths from the bar complex to the modular homotopy type:
the algebraic, geometric, and Getzler--Kapranov routes.
The canonicity theorem adds a fourth path running in the
\emph{reverse} direction: given the modular homotopy type,
the bar-cobar adjunction produces a canonical tensor
coalgebra model, and the $\Eone$-structure is automatic.
Physically, this is the statement that the universal
boundary condition is determined by the bulk: the
no-open-to-closed rule of the Swiss-cheese operad, read
backwards, says that the open color is a functor of
the closed color. The diagram closes into a circle:
modular homotopy type and $\R$-factorization determine
each other.
\end{remark}
 succeeded in 52ms:
the representing object for the formal moduli problem associated
to the deformation theory of~$\cA$.
\end{theorem}

\begin{proof}
The convolution dg Lie algebra
$\mathrm{Conv}(\cC, \cA)
= \Hom(s^{-1}\bar{\cC},\, \cA)$
is complete: its underlying graded vector space is a product, not
a sum, because $\cC$ is conilpotent. Concretely, the coradical
filtration $F_\bullet\cC$ dualizes to an inverse-limit filtration
$F^\bullet\mathrm{Conv}(\cC, \cA)
= \varprojlim_k \Hom(\cC/F_k\cC, \cA)$, and completeness is the
statement that $\mathrm{Conv}(\cC, \cA)
= \varprojlim_k \mathrm{Conv}(\cC, \cA)/F^k$.

For complete dg Lie algebras, the simplicial Maurer--Cartan functor
$\MC_\bullet$ is well-defined: its $n$-simplices are MC elements
in $\mathfrak{g} \otimes \Omega_n$, where $\Omega_n$ is the
Sullivan algebra of polynomial forms on the standard
exec
/bin/zsh -lc "rg -n 'Theorem A|Theorem B|Theorem C|Theorem D|MC2|five main theorems|What changed in Vol I|rectification' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1385:By the rectification theorem (Theorem~\ref{thm:rectification}),
4079:The five main theorems of modular Koszul duality (Vol~I) are projections of a single Maurer--Cartan element $\Theta_\cA \in \mathrm{MC}(\gAmod)$:
codex
I’ve isolated the review chapter’s summary table and some stale internal references. The next pass is against the Vol I source itself, because the requested fixes are about imported theorem scope and convention rather than local prose alone.
exec
/bin/zsh -lc "rg -n '\\\\label\\{.*(theorem-a|bar-cobar|inversion|complementarity|modular|mc2|theta|gmod|g\\"'^'"\\{mod\\})' ../chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'thm:.*A|thm:.*B|thm:.*C|thm:.*D|constr:.*five-theorems|mc2' ../chiral-bar-cobar/chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Theorem A|Bar--cobar adjunction|Verdier|coderived|curved bar equation|modular characteristic|MC2|g\\"'^'"\\{mod\\}|Theta_\\\\cA|Theta' ../chiral-bar-cobar/chapters ../chiral-bar-cobar/main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 823

../chiral-bar-cobar/chapters/examples/w3_holographic_datum.tex:146:(Theorem~\ref{thm:mc2-bar-intrinsic}), the element
../chiral-bar-cobar/chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
../chiral-bar-cobar/chapters/examples/deformation_quantization.tex:147:For coisson algebras, the classical Kontsevich formality theorem ensures the vanishing of all higher obstructions at the operadic level: the $E_2$-operad (governing Poisson structures) is formal, so the deformation problem is unobstructed. Theorem~\ref{thm:geometric-equals-operadic-bar} lifts this to the curve $X$: the same object as the operadic bar construction is computed via the geometric bar complex, so formality propagates from the classical to the chiral setting. Gauge equivalence follows from the standard deformation-theoretic argument: different choices of Maurer--Cartan element in the same gauge orbit give isomorphic deformations.
../chiral-bar-cobar/chapters/examples/deformation_quantization.tex:260:Theorem~\ref{thm:chiral-formality} (\ClaimStatusProvedElsewhere,
../chiral-bar-cobar/chapters/examples/deformation_quantization.tex:543:By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
../chiral-bar-cobar/chapters/examples/deformation_quantization.tex:635:theorem (Theorem~\ref{thm:chiral-formality}, \ClaimStatusProvedElsewhere,
../chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:270:(Theorem~\ref{thm:explicit-theta}). At $c = 0$ (the Witt algebra),
../chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:2026:Theorem~\ref{thm:explicit-theta}, deforming the BGG
../chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:2239: complex acquires curvature $m_0^{(g)} = \kappa(\cA) \cdot \lambda_g$ (Theorem~\ref{thm:genus-universality}), which deforms the BGG
../chiral-bar-cobar/chapters/frame/guide_to_main_results.tex:85: Thm~\ref{thm:mc2-bar-intrinsic} \\[4pt]
../chiral-bar-cobar/chapters/frame/guide_to_main_results.tex:126: Thms~\ref{thm:e1-theorem-A-modular}--\ref{thm:e1-theorem-H-modular} \\[4pt]
../chiral-bar-cobar/chapters/frame/guide_to_main_results.tex:147: (Theorem~\ref{thm:mc2-bar-intrinsic}).
../chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:208:field theory (Theorem~\ref{thm:shadow-cohft}): $D^2=0$ on the
../chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:206:\textbf{H}~(Theorem~\ref{thm:hochschild-polynomial-growth}): $\mathrm{ChirHoch}^*(\mathcal{H}_k) = (\mathbb{C}, \mathbb{C}, \mathbb{C})$ concentrated in degrees $\{0, 1, 2\}$; Hilbert polynomial $P(t) = 1 + t + t^2$.
../chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:207:\textbf{Center}~(Theorem~\ref{thm:operadic-center-hochschild}): $C^\bullet_{\mathrm{ch}}(\mathcal{H}_k, \mathcal{H}_k)$ is the operadic center; the bar coproduct (deconcatenation) provides the coassociative $E_1$-coalgebra structure, and the outer derivation $D(\alpha) = \mathbf{1}$ is the nontrivial class in $\mathrm{ChirHoch}^1$.
../chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:1811:full homotopy completion (Theorem~\ref{thm:mc2-bar-intrinsic}).
../chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:1850: by Theorem~\ref{thm:mc2-bar-intrinsic}; for Heisenberg
../chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:1866:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}). The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 succeeded in 51ms:
../chiral-bar-cobar/chapters/examples/landscape_census.tex:1312:\begin{remark}[Exceptional and non-simply-laced complementarity]\label{rem:e8-complementarity}
../chiral-bar-cobar/chapters/examples/landscape_census.tex:3721:\begin{remark}[Complementarity at each genus]\label{rem:genus-complementarity}
../chiral-bar-cobar/chapters/examples/symmetric_orbifolds.tex:207:\ClaimStatusConjectured]\label{conj:symn-inversion}
../chiral-bar-cobar/chapters/examples/symmetric_orbifolds.tex:215:partial]\label{rem:symn-complementarity}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:90:\label{def:analytic-theta-datum}%
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:915:\begin{theorem}[Unimodular lattice self-duality; \ClaimStatusProvedHere]\label{thm:lattice:unimodular-self-dual}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1048:\begin{equation}\label{eq:lattice:kappa-complementarity}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1531:\begin{corollary}[Unimodular case; \ClaimStatusProvedHere]\label{cor:lattice:hochschild-unimodular}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1596:\begin{theorem}[Modular invariance; \ClaimStatusProvedHere]\label{thm:lattice:modular-invariance}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1727:\label{prop:lattice:niemeier-theta-decomposition}%
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1733:\begin{equation}\label{eq:niemeier-theta-decomposition}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3171:\label{thm:e1-inversion-principle}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3179:\begin{equation}\label{eq:e1-inversion}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3616:\label{sec:lattice:factorization-bar-cobar}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3729: \begin{equation}\label{eq:lattice:fact-bar-cobar}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:4300:\begin{equation}\label{eq:lattice:level-k-bar-cobar}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5073:\label{rem:xyz-quasi-modular}
../chiral-bar-cobar/chapters/examples/yangians_computations.tex:1675:\label{rem:bar-cobar-kazhdan-candidate}
../chiral-bar-cobar/chapters/examples/yangians_computations.tex:4990:\begin{equation}\label{eq:modular-YB-identification}
../chiral-bar-cobar/chapters/examples/yangians_computations.tex:5072:\label{rem:yangian-baxter-rees-modular}
 succeeded in 51ms:
Total output lines: 6461

../chiral-bar-cobar/main.tex:517:\newcommand{\Thetaenv}{\Theta^{\mathrm{env}}} % envelope-shadow functor
../chiral-bar-cobar/main.tex:744:$\Theta_\cA \in \gAmod$ satisfying
../chiral-bar-cobar/main.tex:745:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$
../chiral-bar-cobar/main.tex:748:\textup{(A)}~bar-cobar adjunction with Verdier intertwining;
../chiral-bar-cobar/main.tex:807:shadow obstruction tower, modular characteristic,
../chiral-bar-cobar/main.tex:919: Verdier duality on $\operatorname{Ran}(X)$. The logarithm exists
../chiral-bar-cobar/main.tex:932: The modular characteristic $\kappa(\cA)$ is universal, additive,
../chiral-bar-cobar/main.tex:952:class~$\Theta_\cA$, proved by the bar-intrinsic construction
../chiral-bar-cobar/main.tex:987:% Cobar construction, distributions, Verdier duality, genus 1, Koszul pairs.
../chiral-bar-cobar/main.tex:994:% bar-cobar inversion (Theorem A), Ran-space perspective, categorical logarithm.
../chiral-bar-cobar/main.tex:1065:% obstruction tower kappa -> Delta -> [C] -> o^(r) -> Theta. The
../chiral-bar-cobar/main.tex:1076:The modular characteristic~$\kappa(\cA) = \mathrm{av}(r(z))$ is the
../chiral-bar-cobar/main.tex:1090:Maurer--Cartan element~$\Theta_\cA$, proved by the bar-intrinsic
../chiral-bar-cobar/main.tex:1159:% programme: bar complex, Koszul dual, genus tower, modular characteristic.
../chiral-bar-cobar/main.tex:1203:configuration spaces and Verdier duality acts by $R$-matrix
../chiral-bar-cobar/main.tex:1305:% holographic datum H(W_3) = (A, A!, C, r(z), Theta_A, nabla^hol).
../chiral-bar-cobar/main.tex:1445:% r(z) = Res^coll_{0,2}(Theta_A) --- realized in seven independent
../chiral-bar-cobar/main.tex:1454:$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$,

thinking
**Searching for theorem summaries**

I'm facing a challenge with search results being too broad. I need to find specific, relevant sections of Volume I, particularly the theorem A summary. It might help to consider using imported labels in cross-references. I should inspect the early introduction in main.tex to summarize theorems A-D and check on the `higher_genus_foundations` section. I might want to look into specific theorem labels, like `thm:e1-theorem-A-modular`, to guide my search on the main results.
exec
/bin/zsh -lc "sed -n '730,770p' ../chiral-bar-cobar/main.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2510,2665p' ../chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'e1-theorem-A-modular|e1-theorem-B-modular|e1-theorem-C-modular|e1-theorem-D-modular|thm:mc2-bar-intrinsic|thm:off-koszul-ran-inversion|thm:bar-cobar-isomorphism-main|thm:quantum-complementarity-main|thm:modular-characteristic|g\\"'^'"\\{mod\\}|eq:completed-tensor-gmod' ../chiral-bar-cobar/chapters ../chiral-bar-cobar/main.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
The differential includes:
\begin{enumerate}
\item Bar differential (OPE contractions)
\item Boundary operator (degeneration $\Sigma_2 \rightsquigarrow \Sigma_1$)
\item \emph{New:} Integration over moduli with Eisenstein series insertions
\end{enumerate}

\subsubsection{The cocycle}

The genus 2 cocycle for our example is:
\begin{align}
c_2 &= \int_{\mathcal{M}_2} \int_{\Sigma_2^2} 
\operatorname{Tr}_{\Sigma_2}(a(z_1) \otimes a^*(z_2)) \\
&\quad \cdot E_4(\Omega) \cdot d\mu_{\text{WP}}
- \kappa \cdot (\text{boundary terms})
\end{align}

\emph{Cocycle condition.} $d^{(2)} c_2 = 0$ involves:
\begin{itemize}
\item Genus 1 boundary: $\partial \Sigma_2 \supset \Sigma_1$
 succeeded in 51ms:
The ordered bar complex
$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$
carries a deconcatenation coproduct, an $R$-matrix,
and Yangian structure; the symmetric bar
$B^\Sigma(\cA)$ on $\operatorname{Ran}(X)$ is its
$\Sigma_n$-coinvariant shadow.
For $\mathsf{E}_\infty$-chiral algebras, a formality bridge
gives a quasi-isomorphism between ordered and symmetric
chiral homologies; for genuinely $\mathsf{E}_1$-chiral
algebras the kernel of averaging is non-trivial,
carrying $\operatorname{GRT}_1$-dependent data from the
Drinfeld associator.

A Maurer--Cartan element
$\Theta_\cA \in \gAmod$ satisfying
$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$
in the modular convolution $\Linf$-algebra governs five
theorems:
\textup{(A)}~bar-cobar adjunction with Verdier intertwining;
\textup{(B)}~bar-cobar inversion on the Koszul locus;
 succeeded in 52ms:
Total output lines: 682

../chiral-bar-cobar/main.tex:953:(Theorem~\ref{thm:mc2-bar-intrinsic});
../chiral-bar-cobar/main.tex:1091:construction (Theorem~\ref{thm:mc2-bar-intrinsic}).
../chiral-bar-cobar/chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
../chiral-bar-cobar/chapters/examples/deformation_quantization.tex:817:and~\ref{thm:quantum-complementarity-main}) address the
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:356:(Theorem~\ref{thm:quantum-complementarity-main}; this is nonzero, since the full MC elements do \emph{not} sum to zero for $\mathcal{W}$-algebras). The Miura embedding
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:1960:In the language of Theorem~\ref{thm:mc2-bar-intrinsic}, the zero locus
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2346: Koszul conductor (Theorem~\textup{\ref{thm:quantum-complementarity-main}}).
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2533: (Theorem~\textup{\ref{thm:mc2-bar-intrinsic}})
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2615:(Theorem~\ref{thm:mc2-bar-intrinsic}) depends
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2732:(Theorem~\ref{thm:mc2-bar-intrinsic}),
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3283: by Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3618:\textup{(}Theorem~\ref{thm:mc2-bar-intrinsic}\textup{)} carries, in
../chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:5456:$\Theta_{\cA}$: Theorem~\ref{thm:mc2-bar-intrinsic}
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:211:Theorem~\ref{thm:mc2-bar-intrinsic},
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:1958: (Theorem~\ref{thm:quantum-complementarity-main}).
../chiral-bar-cobar/chapters/examples/lattice_foundations.tex:3620:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is stated for any
../chiral-bar-cobar/chapters/examples/beta_gamma.tex:337:(Theorem~\ref{thm:mc2-bar-intrinsic}). At degree~$2$,
exec
/bin/zsh -lc "sed -n '1900,2065p' ../chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
\section{The \texorpdfstring{$E_1$}{E1} five main theorems at
all genera}
\label{sec:e1-five-theorems}
\index{five main theorems!E1@$E_1$ (ordered)!all genera|textbf}

The genus-$0$ theory promoted each $E_\infty$ shadow invariant to
an $E_1$ shadow at the same degree: the scalar $\kappa$ to the
spectral $r$-matrix, the cubic shadow $\mathfrak{C}$ to the
Drinfeld associator. The genus tower so far still uses the
commutative modular operad $\cM_\Com$; the promotion is incomplete
until the same replacement happens at every genus. The genus-$g$
ordered bar complex on $\cM_\Ass$ supplies the missing structure:
the $r$-matrix acts on internal edges, the associator controls
vertex reordering, and the genus-$g$ partition function acquires a
ribbon surface decomposition invisible to $\Sigma_n$-coinvariants.
The five theorems $\mathrm{A}^{E_1}$--$\mathrm{H}^{E_1}$ below
extend the bar--cobar package at all cyclic genera $(g,n)$ with
$2g-2+n>0$.

\begin{theorem}[Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "sed -n '520,620p' ../chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2840,2915p' ../chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
The Heisenberg complementarity
of~\S\ref{sec:frame-complementarity} generalizes to a Lagrangian
polarization:

\begin{theorem}[Quantum complementarity as Lagrangian polarization; \ClaimStatusProvedHere]
\label{thm:quantum-complementarity-main}
\label{thm:quantum-complementarity}
\index{deformation-obstruction complementarity|textbf}
\index{Lagrangian!complementarity|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, with $\mathcal{A}$ a sheaf of chiral algebras in
the sense of Beilinson--Drinfeld \cite[Chapter 3]{BD04} and $\mathcal{A}^!$
its Koszul dual (Theorem~\ref{thm:chiral-koszul-duality}).
Write $\mathbf{C}_g(\cA)$, $\mathbf{Q}_g(\cA)$, $\mathbf{Q}_g(\cA^!)$
for the ambient complex and homotopy eigenspaces of
Definition~\textup{\ref{def:complementarity-complexes}}.

 succeeded in 51ms:
class~$\Theta_\cA$ require data beyond~$\kappa$;
see Definition~\ref{def:full-modular-package}).

\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
\label{thm:modular-characteristic}
\index{modular characteristic theorem|textbf}
\index{kappa@$\kappa$!as first characteristic number|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

Let $\cA$ be a modular Koszul chiral algebra
(Definition~\ref{def:modular-koszul-chiral}). Its scalar modular
characteristic package
(Definition~\ref{def:scalar-modular-package}) is controlled by one
number, the genus-$1$ curvature coefficient
$\kappa(\cA) \in \mathbb{C}$. More precisely:

\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Universality.}
 \begin{enumerate}[label=\textup{(\alph*)}]
exec
/bin/zsh -lc "rg -n 'bar-cobar-isomorphism-main|off-koszul-ran-inversion|quantum-complementarity-main|modular-characteristic|mc2-bar-intrinsic|theorem-a-summary|Theorem~A|Theorem~B|Theorem~C|Theorem~D' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2230,2460p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
205:(Theorem~A): $d_Q$ encodes the internal differential $m_1$,
625:This is exactly the content of Volume~I Theorem~A: the bar differential squares to zero, equivalently, the $\Ainf$ relations hold.
711:(Volume~I, Theorem~D), with
728: Theorem~D).
736:\item The complementarity theorem (Vol~I, Theorem~C) gives
1015:$\delta\kappa(f)$ is determined by the change in the genus-$1$ bar obstruction class (Volume~I, Theorem~D). For the Virasoro algebra, $\kappa = c/2$ and the anomaly is $\delta\kappa = \delta c/2$; for affine algebras, the relation between $\kappa$ and $c$ is more involved (see the formula $\kappa = \dim\fg \cdot (k+h^\vee)/(2h^\vee)$ above).
1355:By Volume~I, Theorem~A, the bar differential $d_{\barB}$ satisfies
1620: $\operatorname{Ran}(X)$ constructed in Volume~I, Theorem~A\@.
2280: (Theorem~A intertwining). It exists unconditionally for
2326: (Volume~I, Theorem~C).
2393:(Theorem~A): $\cA^!_\infty$ is the algebra whose bar coalgebra is
2691: (Vol~I, Theorem~D), not to the bar differential $m_k$ for
2714:via Vol~I Theorem~D. The associated graded $\mathrm{gr}^2\cL$
3500: & transverse Lagrangians (Vol~I, Theorem~C) \\
3620:\textup{(}Vol~I, Theorem~B\textup{)} is the Morita equivalence
3745: characteristic of Volume~I, Theorem~D.
3775:Part~(ii) is Volume~I, Theorem~D, applied to the universal
3811:complementarity theorem (Theorem~C) constrains the curvatures:
3819:the $\hat{A}$-genus (Volume~I, Theorem~D\textsubscript{scal}).
3838:category of Positselski (Volume~I, Theorem~B(b)). The curvature
 succeeded in 52ms:
\text{for } q \neq 0.
\end{equation}
\end{definition}

This is a single condition. Twelve consequences radiate from it, each
illuminating a different face of the same concentration. They are not
independent characterizations assembled by coincidence; they are one
phenomenon seen from twelve angles:

\begin{theorem}[The Koszul dodecahedron;
{\upshape Vol~I, Koszul equivalence theorem}]
\label{thm:koszul-dodecahedron}
For a chiral algebra~$\cA$ with PBW filtration, the following are
equivalent\textup{:}\footnote{Items \textup{(i)--(x)} are
unconditionally equivalent. Item~\textup{(xi)}
\textup{(}Lagrangian transversality\textup{)} is conditional on
perfectness and nondegeneracy hypotheses for the pairing on the
ambient complex. Item~\textup{(xii)} \textup{(}Hodge
purity\textup{)} is fully proved for the semisimple-residue class
\textup{(}Theorem~\textup{\ref{thm:semisimple-purity}):}
exec
/bin/zsh -lc "sed -n '2460,2860p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
of non-trivial differentials, which is at
most~$\mathfrak{L}(\cA)$.
\end{proof}

\begin{theorem}[One-loop Koszul criterion;
\ClaimStatusProvedElsewhere]
\label{thm:one-loop-koszul}
\index{one-loop Koszul criterion|textbf}
\index{Koszulness!one-loop criterion|textbf}
\index{BV-BRST!one-loop exactness|textbf}
Let\/ $\cA$ be the boundary chiral algebra of a 3d
holomorphic-topological gauge theory whose BV-BRST
quantization is one-loop exact \textup{(}i.e.\ the
BV master equation is solved at tree level plus one loop,
with no higher-loop corrections to the effective action\textup{)}.
Then $\cA$ is chirally Koszul:
\[
H^{p,q}\bigl(\barB(\cA)\bigr) = 0 \quad \text{for } q \neq 0.
\]
In particular, the bar complex is cogenerated in degree~$1$,



thinking
**Inspecting target file**

I'm noticing the target file is large, and it might contain some outdated claims. I need to take a closer look around the later lines, especially 3600, to see if there are mentions of the curved Swiss-cheese. It seems like Theorems B and C could be repeated in that section. So, I’ll search through the lines from 3580 to 3850 for clarity. Let's ensure everything is accurate and up-to-date!
thinking
**Clarifying theorem changes**

I need to determine the exact changes requested. First, I'll verify Theorems A, B, C, and D, ensuring they align with the proper conventions and proofs. I should also ensure MC2 correctly attributes the g^{mod} carrier. Additionally, I want to add a note about what's changed in Volume I, listing the corrections.

It seems there might be a summary section in the bar-cobar review that needs precise wording, so I’ll search for relevant terms and consider creating a new section that summarizes these five theorems with exact specifications.
thinking
**Inspecting specific lines**

I need to take a closer look at the text around line 3800, as it references Theorems B, C, and D. It seems a search within the range of 3780 to 3850 will help me gather the necessary context. By doing this, I can ensure I fully understand how these theorems are presented and interrelated. This should give me clearer insight into any revisions or points of confusion that need addressing.
codex
The Vol I comparison surface confirms the requested scope shifts: Theorem A is Verdier-to-the big dual, Theorem B is `qi` on the Koszul locus but coderived off it, Theorem C’s Lagrangian statement is genuinely `g ≥ 1`, and Theorem D is downstream of MC2 rather than a proof source for it. I’m now patching the review chapter so those distinctions are explicit where Vol II readers actually see them.
exec
/bin/zsh -lc "sed -n '3720,3865p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3865,4025p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '4988,5058p' ../chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

At genus~$0$: $d_{\barB}^2 = 0$, $\Delta$ is
coassociative, $\R$-factorization is exact. At genus $g \geq 1$,
the propagator acquires monodromy from the period matrix
of~$\Sigma_g$, and the fiberwise bar differential becomes curved:
\begin{equation}\label{eq:curved-R-fact}
\dfib^{\,2} = \kappa(\cA) \cdot \omega_g,
\end{equation}
where $\kappa(\cA)$ is the modular characteristic and $\omega_g$ is
the Arakelov $(1,1)$-form on $\Sigma_g$.

\begin{proposition}[Curved $\R$-factorization at higher genus;
\ClaimStatusProvedHere]
\label{prop:curved-R-factorization}
Let $\cA$ be a chiral algebra on a genus-$g$ curve $\Sigma_g$.
The genus-$g$ bar complex $\barB^{(g)}(\cA)$ satisfies:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The coproduct $\Delta$ is coassociative
 (independent of genus: it is the tensor coalgebra structure
 and depends on no propagator data).
 succeeded in 51ms:
 coalgebra structure at genus~$g$ is therefore carried by
 $(\barB^{(g)}(\cA), \Dg{g}, \Delta)$
 (Volume~I, Remark~\ref{V1-rem:sc-higher-genus}\textup{(iii)}).
\item For a Koszul pair $(\cA, \cA^!)$ in the affine lineage,
 the curvatures satisfy $\kappa(\cA) + \kappa(\cA^!) = 0$
 (Volume~I, Theorem~C, Feigin--Frenkel involution); for
 $\mathcal{W}$-algebras the sum
 $\kappa(\cA) + \kappa(\cA^!) = \rho_\cA \cdot K$ is in
 general nonzero (Volume~I, Theorem~D). In the affine
 lineage the residual fibrewise curvatures cancel on
 $\barB^{(g)}(\cA) \otimes \barB^{(g)}(\cA^!)$, while in the
 $\mathcal{W}$-lineage the tensor product retains a residual
 fibrewise curvature. In both cases the period-corrected
 differential supplies the genuine $E_1$ dg coalgebra
 structure on the tensor product.
\end{enumerate}
\end{theorem}

\begin{proof}
\textbf{Part~(i).}
 succeeded in 51ms:
\textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.
The Eulerian weight-$1$ channel
$\kappa_{TT} = c/2$ is the Virasoro contribution; the weight-$2$
channel $\kappa_{WW} = c/3$ is the $W$-field contribution. For
$\cW_N$ in general, $\kappa = c \cdot (H_N - 1)$ where
$H_N = \sum_{j=1}^{N} 1/j$ is the harmonic number, and the
channel at Eulerian weight~$j$ contributes $c/j$.
\end{remark}

\begin{remark}[Proof components for MC2]\label{rem:mc2-status}
\index{universal Maurer--Cartan class!proof history}
The proof of Theorem~\ref{thm:universal-theta} assembles:
(i)~the scalar shadow $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic});
(ii)~the determinant line bundle with $c_1=\kappa\cdot\lambda$
(Remark~\ref{rem:homotopy-native-d});
(iii)~the spectral discriminant $\Delta_{\cA}(x)$
(Theorem~\ref{thm:spectral-characteristic});
(iv)~the cyclic deformation algebra on bar coderivations
(Proposition~\ref{prop:genus0-cyclic-coderivation}), with
MC2-1 resolved for KM by Theorem~\ref{thm:mc2-1-km}.

thinking
**Inspecting Theorem A**

I need to look closely at Theorem A, specifically the canonical statement found in Volume I on chiral koszul pairs, around page 4004. It's important to ensure I understand the details fully, as this theorem might have implications for my current work. I want to gather clear insights from it and see how it applies to the topics I'm exploring. Let's see what interesting conclusions I can draw from my examination of that theorem!
exec
/bin/zsh -lc "sed -n '3988,4088p' ../chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$t^3$. This nonvanishing defect is the kinematic signature of
nonquadraticity and feeds directly into the MC4 completion
programme
(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
\end{remark}

\subsection{Geometric bar-cobar duality (Theorem~A)}
\label{sec:theorem-a-statement}

The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
is unconditionally a factorization algebra
(Chapter~\ref{chap:NAP-koszul-derivation}).
Theorem~A identifies the conditions under which $\cA^!_\infty$ is
\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.

\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
\label{thm:bar-cobar-isomorphism-main}
\index{bar-cobar duality!main theorem|textbf}
\index{Theorem A|textbf}
\textup{[}Regime: quadratic on the Koszul locus
exec
/bin/zsh -lc "sed -n '908,980p' ../chiral-bar-cobar/chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3760,3815p' ../chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
factorization coderived/contraderived comparison for comodules and
contramodules over the same curved factorization coalgebra~$C$, and
then explains separately how this comparison interfaces with the
Koszul-locus generated-core duality of
Theorem~\ref{thm:h-level-factorization-kd}.
\end{remark}

\begin{theorem}[Off-Koszul bar-cobar inversion on Ran;
\ClaimStatusProvedHere]
\label{thm:off-koszul-ran-inversion}
\index{bar-cobar inversion!off-Koszul|textbf}
\index{coderived category!bar-cobar inversion}
Let $\cA$ be a complete augmented chiral algebra on~$X$ with
$\barB_X^{\mathrm{fact}}(\cA)$ having finite-dimensional graded
pieces. Then the bar-cobar counit
\[
\Omega_X \barB_X(\cA) \longrightarrow \cA
\]
is an isomorphism in
$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$,
 succeeded in 52ms:
$\Theta_\cA$: the modular characteristic $\kappa$ at degree~$2$,
the cubic shadow $\mathfrak{C}$ at degree~$3$, the quartic
resonance $\mathfrak{Q}$ at degree~$4$, and all higher
obstructions in the Postnikov tower of
Definition~\ref{def:shadow-postnikov-tower}.
There is no separate construction for each invariant; there is
$\Theta_\cA$, and the invariants are what remain after
forgetting all but finitely many degrees.

\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
\label{thm:mc2-bar-intrinsic}
\index{universal Maurer--Cartan class!bar-intrinsic construction}
\index{MC2!bar-intrinsic proof}
\index{MC2!full generality}
Let $\cA$ be a modular Koszul chiral algebra on a smooth
projective curve~$X$ with non-degenerate invariant form.
Write
$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
for the genus-completed bar differential
\textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},


thinking
**Reviewing mathematical proofs**

I’m thinking I might need to read more on the MC2 theorem to explore alternative proofs. I should inspect the target file for any inaccuracies in the summaries, especially checking if there are tables that don't match up. The references to "Vol I, Theorem A" seem to differ from imported labels, so I could add a review section summarizing each theorem and its alternative proof statuses. The user wants the review chapter reinforced. I'll need to document my findings in the audit notes and make necessary edits afterward.
thinking
**Verifying definitions and attributions**

I need to search for definitions of `\gAmod` to verify the MC2 attribution correctly. The target seems to indicate that `\Theta_\cA \in MC(\gAmod)` already, but the user is asking to ensure that it properly attributes the g^{mod} carrier. I might need to clarify if `\Theta_\cA` belongs to the completed coinvariant modular convolution algebra, not just the modular deformation complex. I'll inspect the specific line in the target document where it mentions `\Theta_\cA` and consider adding a remark to attribute the carrier accurately.
exec
/bin/zsh -lc "rg -n 'gAmod|Gmod|Defcyc|geometric-modular-operadic-mc|completed coinvariant modular convolution algebra' ../chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '5538,5598p' ../chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\gAmod|\\\\Gmod|Defcyc|Theta_\\\\cA|MC\\(' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
100:where $\MC(\cdot)$ denotes Maurer--Cartan elements (solutions of $d\alpha + \frac{1}{2}[\alpha, \alpha] = 0$) in the convolution dg Lie algebra (the strict model $\Convstr$ of the homotopy-invariant $L_\infty$-algebra $\Convinf$; Convention~\ref{conv:vol2-strict-models}).
1172:twisting morphism~$\Theta_\cA$
1180:is the cogenerator projection of~$\Theta_\cA$; the
1182:product parametrized by~$\Theta_\cA$; the genus-$g$ curvature
1184:extension of~$\Theta_\cA$; the five theorems of Volume~I
1189:object $\Theta_\cA$ suffices: it is the terminal twisting morphism,
3826:D^{(g)}_\cA\,\Theta_\cA^{(g)} + \sum_{g_1 + g_2 = g} \tfrac{1}{2}\bigl[\Theta_\cA^{(g_1)},\, \Theta_\cA^{(g_2)}\bigr] = 0,
4079:The five main theorems of modular Koszul duality (Vol~I) are projections of a single Maurer--Cartan element $\Theta_\cA \in \mathrm{MC}(\gAmod)$:
 succeeded in 51ms:
 genus-$g$ equation is a finite sum;
\item extending a partial solution through genus~$g-1$ to genus~$g$ is
 obstructed by a class in
 $H^2(\Defcyc(\cA), l_1) \otimes W_g$;
\item if $H^2(\Defcyc(\cA), l_1) \cong \mathbb{C}$, then the
 genus-$g$ extension problem has a single obstruction channel valued
 in~$W_g$.
\end{enumerate}
\end{proposition}

\begin{proof}
Apply Proposition~\ref{prop:genus-completed-mc-framework} with
$L=\Defcyc(\cA)$. This gives parts~\textup{(i)} and~\textup{(ii)}.
Part~\textup{(iii)} is exactly
Corollary~\ref{cor:one-dim-obstruction}.
\end{proof}

\begin{proposition}[Geometric modular-operadic MC framework;
\ClaimStatusProvedHere]\label{prop:geometric-modular-operadic-mc}
\index{MC2!geometric modular-operadic framework}
 succeeded in 51ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
60:dg~Lie algebra~$\gAmod$, a strict model of the homotopy-invariant
63:$\gAmod$ controls the extension tower: each finite truncation
78: $\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
446:$\Defcyc(\cA)$
671:$\Theta_{\cA}\in\operatorname{MC}(\Defcyc(\cA)\widehat{\otimes}\Gmod)$
2349: \in \MC(\gAmod)$ exists at all genera
2358: H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ carries
2663: \Defcyc(\cA) \;\widehat{\otimes}\;
2672: $\Defcyc(\cA) \to \mathbb{C}$;
2703:The cyclic $L_\infty$-algebra $\Defcyc(\cA)$ is constructed
2719:$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
2773: \Defcyc(\cA) \;\widehat{\otimes}\;
2818:(3)~shadow obstruction tower / full MC: $\Theta_{\cA}^{\leq r}$, $\Defcyc(\cA)$
3474:element~$\Theta_\cA \in \MC(\gAmod)$:
3495:in~$\gAmod$, not by the KdV hierarchy.
3575:there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
3580: \Defcyc(\cA) \;\widehat{\otimes}\;
3625:Clutching is automatic from the Feynman structure on~$\Gmod$
3626:(Proposition~\ref{prop:geometric-modular-operadic-mc}(c)).
codex
I found a second class of wounds in the same chapter: several local references still point to non-existent hyphenated labels like `thm:bar-cobar-adjunction`. I’m folding those into the same patch so the fortified statements also compile against the live labels.
exec
/bin/zsh -lc "rg -n 'thm:bar-cobar-adjunction|thm:bar-cobar-inversion-qi|thm:bar-terminality|thm:cobar-initiality|thm:bar-cobar-adjunction|thm:bar_cobar_adjunction' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
320:\label{thm:bar_cobar_adjunction}
405:The bar-cobar adjunction (Theorem~\ref{thm:bar_cobar_adjunction})
445:By Theorem~\ref{thm:bar_cobar_adjunction}, there is a natural
631:\textbf{Step 5: Pullback.} For any twisting morphism $\tau: \cC \to \cA$ (equivalently, a coalgebra map $f_\tau: \cC \to \barB(\cA)$ by Theorem~\ref{thm:bar-terminality}), the pullback $f_\tau^* \cE_{\mathrm{univ}}$ is a chiral $\cA$-module on $\cC$:
765:\label{thm:bar-terminality}
842:\label{thm:cobar-initiality}
914:Theorem~\ref{thm:cobar-initiality}: a twisting morphism
919:Theorem~\ref{thm:bar-terminality}: $\tau$ determines a unique
988:(Theorem~\ref{thm:cobar-initiality}).
1131:Theorem~\ref{thm:cobar-initiality} in place of
1132:Theorem~\ref{thm:bar-terminality}.
1818: Theorems~\textup{\ref{thm:bar-cobar-adjunction}}
1915:Theorem~\ref{thm:bar-cobar-adjunction}, unconditional by
4071:Theorem~\ref{thm:bar-cobar-adjunction}), and the FM--Stokes--Arnold
exec
/bin/zsh -lc "sed -n '740,940p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:bar-terminality\\}|\\\\label\\{thm:cobar-initiality\\}|\\\\label\\{thm:bar_cobar_adjunction\\}|\\\\label\\{thm:bar-cobar-inversion-qi\\}' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 hence negates~$\kappa$. The tensor product
 $\barB^{(g)}(\hat{\fg}_k) \otimes
 \barB^{(g)}(\hat{\fg}_{-k-2h^\vee})$ has vanishing total
 curvature at every genus.
\end{itemize}
\end{example}

\subsection{The universal property: initiality, terminality, and formal moduli}
\label{subsec:universal-property-twisting}

The classifying-space theorem
(Theorem~\ref{thm:bar-representability}) identifies the bar complex
as the representing object for a formal moduli functor. The
present subsection refines this in two directions: first, it
isolates the \emph{set-level} universal properties
(terminality of bar, initiality of cobar) that underlie the
representability; second, it promotes the representability to the
full Lurie--Pridham correspondence between formal moduli problems
and complete dg Lie algebras. The result is the platonic form of
the bar--cobar adjunction: a single bifunctor of twisting morphisms,
 succeeded in 51ms:
320:\label{thm:bar_cobar_adjunction}
765:\label{thm:bar-terminality}
842:\label{thm:cobar-initiality}





thinking
**Considering theorem organization**

I’m thinking it might be helpful to add a new subsection early in the document. It could summarize the "Vol I theorem package and fortification notes." In that part, I’d plan to review theorems A-D and MC2 with clear statements, along with those redundant proof routes. I want to make sure it’s structured well so that users can easily follow along with the materials for better clarity.
thinking
**Structuring proof routes**

I’m mapping out the spectral sequence, Verdier pairing, and involution splitting, while considering Lagrangian decomposition in my secondary route. I'm looking at the determinant line bundle or universal generating function once I identify the scalar shadow. There’s also an older theorem to consider. I realize the user wants a structured output rather than a file, so perhaps adding remarks like "Proof routes" could work. I'll add a theorem remark for clarity and address changes within Volume I as needed.
thinking
**Clarifying complementarity theorem**

I'm analyzing the affine Kac-Moody example, specifically focusing on the complementarity theorem from Volume I. It states that κ(k) + κ(k') = 0, and I wonder if there's an issue with this at genus 0. While it's clear for genus g ≥ 1, the physical interpretation links Theorem C to curvatures across all genera. I think I need to clarify the Lagrangian statement is for g ≥ 1, and the scalar curvature relation for genus 0 might actually relate to Theorem D. Let's dive deeper into that!
thinking
**Analyzing Theorem C details**

In Volume I, Theorem C outlines the H-level decomposition for each genus g ≥ 0 and the S-level, with specific values for Q_0(A) and Q_0(A^!) as H^0 and 0, respectively. The scalar relation for κ might actually be better described by Theorem D. In my summary, I note that Theorem C deals with a complementary Lagrangian decomposition of the center local system, stating κ + κ' = K(A). It seems the user prefers focusing on Theorem C specifically for g ≥ 1 and clarifying terms for C0.
thinking
**Evaluating the patching process**

I’m considering using a command like `rg -n "TheoremC|VolI, TheoremC|VolumeI, TheoremC"` to address stale claims in the context provided. It seems important to inspect the context for each occurrence to ensure accuracy and relevance. I'll make sure to gather all the necessary information to patch any claims that have become outdated or inaccurate. This approach should help clarify the situation and ensure everything is up to date!
exec
/bin/zsh -lc "sed -n '690,750p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3795,3950p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Volume~I, Theorem~C|Vol~I, Theorem~C|Theorem~C\\)' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$\Dg{g}^{\,2} = 0$ and the Leibniz identity for $\Delta$. The
factor-$2$ discrepancy from~(iii) is exactly the cohomological
obstruction that the Fay correction $\delta_{\mathrm{per}}$
cancels at every interior splitting; a single algebraic
identity in $H^{1}(\Sigma_g)\otimes H^{1}(\Sigma_g)$ controls
both square-zero and the coderivation property.
\end{proof}

\begin{remark}[Physical interpretation]
The curvature $\kappa(\cA) \cdot \omega_g$ is the conformal
anomaly of the 3d HT theory compactified on~$\Sigma_g$. At genus
$0$, there is no anomaly ($\omega_0 = 0$) and the
$\R$-factorization is exact. At genus $g \geq 1$, the anomaly
deforms the $\Eone$ structure into a curved $\Ainf$ structure
whose curvature is controlled by the Hodge bundle
$\mathbb{E} \to \overline{\mathcal{M}}_g$. Volume~I's
complementarity theorem (Theorem~C) constrains the curvatures:
$\kappa(\cA) + \kappa(\cA^!) = K(\cA)$, where $K(\cA)$ is a
level-independent \emph{complementarity constant}. For algebras
in the affine lineage (Kac--Moody, free fields, lattice VOAs,
 succeeded in 51ms:
\MC_\bullet\!\bigl(\mathrm{Conv}(\cC, \hat{\fg}_k)\bigr)
\;\simeq\;
\mathrm{Map}_{\mathrm{CoAlg}}(\cC, \barB(\hat{\fg}_k))
\]
for any conilpotent coalgebra~$\cC$, and the Koszul duality
involution $(\cA^!)^! \simeq \cA$
(Theorem~\ref{thm:duality-involution}) interchanges
the two classifying spaces:
$\barB(\hat{\fg}_k)^! \simeq \barB(\hat{\fg}_{-k-2h^\vee})$.

\medskip\noindent
\textbf{Genus $g \geq 1$: the conformal anomaly as gerbe.}
At genus~$g \geq 1$, the tautological bundle acquires curvature
$\kappa \cdot \omega_g$ (Construction~\ref{constr:tautological-bundle}).
The modular characteristic $\kappa(\hat{\fg}_k)$ is defined in
Volume~I as the leading coefficient of the bar obstruction; for
the affine lineage it equals the level for the Heisenberg algebra
and involves the Sugawara central charge for non-abelian~$\fg$.
Explicitly, $\kappa(\cH_k) = k$ for the Heisenberg ($\dim\fg = 1$),
while for simple~$\fg$ the modular characteristic is
 succeeded in 51ms:
736:\item The complementarity theorem (Vol~I, Theorem~C) gives
2326: (Volume~I, Theorem~C).
3500: & transverse Lagrangians (Vol~I, Theorem~C) \\
3811:complementarity theorem (Theorem~C) constrains the curvatures:
3870: (Volume~I, Theorem~C, Feigin--Frenkel involution); for
3937:(Volume~I, Theorem~C), where $K(\cA)$ is the complementarity

thinking
**Evaluating theorem references**

I'm considering how to reference Theorems C and D while ensuring I'm accurate based on the user's mention of Theorem C with g≥1. It seems that Theorem C applies for g≥1 and may connect to Theorem D regarding the affine κ cancellation. I think I can phrase it in a way that highlights the connection, like mentioning it on the g≥1 complementarity surface. I need to double-check the context around line 2326 to ensure everything aligns properly.
exec
/bin/zsh -lc "sed -n '2290,2345p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3478,3512p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
 of the bigrading. This is the BGS criterion chiralized.

\item \textbf{Hochschild concentration.}
 Chiral Hochschild cohomology $\mathrm{ChirHoch}^n(\cA)$ vanishes
 outside degrees $\{0, 1, 2\}$ at generic level (the critical level
 $k = -h^\vee$ is excluded because $\dim \mathrm{ChirHoch}^0$ can be
 infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
 The polynomial growth of~$\mathrm{ChirHoch}^\bullet$ is the Hochschild
 shadow of bar concentration.

\item \textbf{Factorization homology.}
 $\int_{\Sigma_g} \cA$ is concentrated in degree~$0$ for all genera.
 The higher cohomology of factorization homology measures the failure
 of Koszulness; its vanishing is the global shadow of the local
 concentration.

\item \textbf{Barr--Beck--Lurie.}
 The comparison functor for the bar-cobar monad is an equivalence on
 the fiber: the abstract monadicity theorem applies without
 correction.
 succeeded in 50ms:
 & has a linear free resolution \\
\textup{(v)} Ext diagonal &
 $\mathrm{Tor}^{\cO(\Mvac)}_{p,q}(\cO(\cL_b), \cO(\cL_b)) = 0$ \\
 & for $p \neq q$ \\
\textup{(vi)} Hochschild conc. &
 $T^*[-1]\cL_b$ is formal: the formal bulk model \\
 & from the boundary has no higher corrections \\
\textup{(vii)} Factorization hom. &
 $\int_{\Sigma_g} \Steinb_b$ is concentrated: \\
 & the global self-intersection has no excess \\
\textup{(viii)} Barr--Beck--Lurie &
 Descent for comodules over the \\
 & formal bar/Koszul model of $\Steinb_b$ \\
 & is effective (no correction terms) \\
\textup{(ix)} Kac--Shapovalov &
 $\det G_h \neq 0$: the intersection pairing \\
 & on $\Steinb_b$ is non-degenerate \\
\textup{(x)} Stratum acyclicity &
 Each FM boundary stratum meets $\Steinb_b$ \\
 & in a smooth (acyclic) piece \\

thinking
**Reviewing theorem references**

I see that the theorem in question indicates a conditional aspect. I might consider adding g≥1, which could be okay. However, the user might be looking for Theorem C in the review package instead of these occurrences. I should check where Theorem B appears, particularly at line 3620, since the context might be outdated. I'll search around line 3600 to see if I can find relevant details.
exec
/bin/zsh -lc "sed -n '3590,3645p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2660,2735p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Step~3 of the proof of Theorem~\ref{thm:semisimple-purity}), giving
bar concentration. The counterexample to the converse is
Proposition~\ref{prop:purity-failure-virasoro}: Virasoro is Koszul
(PBW universality, Vol~I) but not collision-pure (the non-split
MHM extension between weights~$4$ and~$2$ produces a non-trivial
$d_2$).
\end{proof}

\begin{proposition}[Purity for the Koszul examples;
\ClaimStatusProvedHere]
\label{prop:purity-koszul-examples}
The purity criterion holds for the three Koszul examples:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textbf{Free $\beta\gamma$:} All OPE poles are simple
 ($\beta(z)\gamma(w) \sim (z-w)^{-1}$). The collision strata
 are smooth (codimension-one normal crossings along each
 diagonal $z_i = z_j$). The IC complex is the constant sheaf,
 which is pure.

\item \textbf{Landau--Ginzburg:} The superpotential~$W$ gives
 succeeded in 51ms:
Let $\cA$ be chirally Koszul, and let
$\Steinb_b = \cL_b \times_{\Mvac}^h \cL_b$ be the derived
Lagrangian self-intersection as in
Conjecture~\textup{\ref{conj:koszul-lagrangian-concentration}}.
Then the \emph{self-intersection groupoid}
$\Steinb_b \rightrightarrows \cL_b$, with source and target maps
$s,t\colon \Steinb_b \to \cL_b$ given by the two projections, is
\emph{expected to be étale}: both $s$ and~$t$ are expected to be
quasi-isomorphisms of derived stacks.
\end{conjecture}

\begin{remark}[Evidence]
This is again heuristic. If the global self-intersection groupoid is
indeed governed by the formal bar/Koszul model of
Theorem~\ref{thm:bar-is-self-intersection}, then chiral Koszulness
should force the higher Tor terms to vanish, leaving only the expected
degree-zero intersection. On that picture, the projections
$s,t\colon \Steinb_b \to \cL_b$ have no higher fibers and are therefore
expected to be étale. Turning this into a theorem would require the
same missing global geometric input as

thinking
**Exploring references**

I think it would be helpful to check the beginning of the file or look closely at relevant sections around 1818 and 1915 to fix any references. It might also be useful to search for Theorem A Verdier. I should explore information from about 1800 to 1930 to ensure I have a full understanding of the context. Let's see what I can find in those timeframes!
exec
/bin/zsh -lc "sed -n '1790,1935p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
$(\cA^!)^! \simeq \cA$.
\end{proof}

The following theorem makes this precise.

\begin{theorem}[The Steinberg presentation;
\ClaimStatusProvedHere]
\label{thm:steinberg-presentation}
\index{Steinberg presentation|textbf}
\index{bar complex!as chiral Steinberg variety|textbf}
Let\/ $\cA$ be a chiral algebra on a smooth curve~$X$ satisfying the
recognition conditions
\textup{(}Theorem~\textup{\ref{thm:recognition})}.
The bar complex $\barB(\cA)$ is an $E_1$ dg coassociative
coalgebra: the bar differential encodes the $A_\infty$ chiral
structure, the deconcatenation coproduct encodes topological
factorization
\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
The $\SCchtop$ structure emerges in the chiral derived center
pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$.
exec
/bin/zsh -lc "sed -n '4048,4105p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
The canonicity theorem adds a fourth path running in the
\emph{reverse} direction: given the modular homotopy type,
the bar-cobar adjunction produces a canonical tensor
coalgebra model, and the $\Eone$-structure is automatic.
Physically, this is the statement that the universal
boundary condition is determined by the bulk: the
no-open-to-closed rule of the Swiss-cheese operad, read
backwards, says that the open color is a functor of
the closed color. The diagram closes into a circle:
modular homotopy type and $\R$-factorization determine
each other.
\end{remark}

\begin{remark}[MC5 genus-zero bridge]
\label{rem:mc5-bridge-pointer}%
\label{rem:mc5-genus-zero-bridge}%
The genus-$0$ BV-BRST/bar
identification: the $A_\infty$ operations $\{m_k\}$ from Feynman
diagram integrals over $\FM_k(\C) \times \Conf_k^{<}(\R)$
coincide with the cogenerator projection of the bar differential




thinking
**Correcting construction details**

I definitely need to make corrections in this construction. It would be good to add an alternative proof remark right after it and maybe include a "What changed in Vol I" comment nearby. I should also correct the reference from `Steinberg presentation` to `thm:bar_cobar_adjunction`. I'll need to adjust `rem:mc5-bridge-pointer` for clarity and ensure local references to Theorem A/B are accurate. While user mentioned stale claims, a precise review rather than edits to all occurrences may help. Some stale claims need fixing, and I might want to clarify the relationship between Theorems C and D.
thinking
**Clarifying theorem references**

I might not need to edit every mention, but I should identify specific local references to Theorem A at lines 205 and 625. Those are general statements about the bar differential from Volume I Theorem A, which is acceptable. However, it seems line 625 inaccurately states that the bar differential squares to zero. This claim might not align with the geometric bar-cobar duality in Theorem A. I need to fix this stale claim and clarify how it relates to the summary of Theorem A in main.tex.
thinking
**Refining theorem identification**

For line 205, my remark about the Vol I bar differential needs adjustment. Instead of saying "from Vol I (Theorem A)," it would be clearer to indicate "from Vol I bar-construction theorem/genus-zero bar coalgebra package." This aligns better with the user's request for a correct reference to Theorem A with the right Verdier convention. It's crucial to avoid misattributing d^2=0 to Theorem A, as it leads to stale claims. I need to fix this for clarity.
thinking
**Inspecting theorem occurrences**

I notice there are several occurrences at lines 205, 625, 2280, and 2393, and maybe even more. I need to inspect these lines and correct any issues. It's important to search for all instances of `TheoremA` and `VolumeI, TheoremA` to check their context. Getting this right is crucial, so I'll take my time to ensure everything is accurate. I'll focus on finding and addressing any discrepancies here.
exec
/bin/zsh -lc "rg -n 'Theorem~A|Volume~I, Theorem~A|Vol~I, Theorem~A|Theorem~A intertwining|Theorem A' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '190,215p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2368,2410p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
205:(Theorem~A): $d_Q$ encodes the internal differential $m_1$,
625:This is exactly the content of Volume~I Theorem~A: the bar differential squares to zero, equivalently, the $\Ainf$ relations hold.
1355:By Volume~I, Theorem~A, the bar differential $d_{\barB}$ satisfies
1620: $\operatorname{Ran}(X)$ constructed in Volume~I, Theorem~A\@.
2280: (Theorem~A intertwining). It exists unconditionally for
2393:(Theorem~A): $\cA^!_\infty$ is the algebra whose bar coalgebra is
4000: The bar-cobar adjunction \textup(Volume~I, Theorem~A\textup)
 succeeded in 53ms:
\Res_{D_{\{i, \ldots, i+k-1\}}} \sim m_k(a_i, \ldots, a_{i+k-1}),
\end{equation}
which is precisely the action of $d_{A_\infty}$.

Summing all contributions:
\begin{equation}
d_{\overline{B}}^2 = 0 + 0 + 0 + 0 + 0 + 0 = 0.
\end{equation}
\end{proof}

\begin{remark}[Identification with Vol~I bar differential]
\label{rem:bar-differential-vol1-identification}
The three-part decomposition $d_{\overline{B}} = d_Q + d_{\mathrm{res}}
+ d_{A_\infty}$ is the geometric presentation of the single bar
coderivation $d_B$ on $T^c(s^{-1}\bar{\cA})$ from Vol~I
(Theorem~A): $d_Q$ encodes the internal differential $m_1$,
$d_{\mathrm{res}}$ the binary product $m_2$ via FM collision
residues, and $d_{A_\infty}$ the higher operations $m_{k \geq 3}$.
The six-term computation above is thus an independent geometric
verification of Vol~I's algebraic $d_B^2 = 0$; the two results
 succeeded in 50ms:
 $B(A) = T^c(s^{-1}\bar{A})$ has cohomology in degree~$1$;
\item Formality $=$ the $\Ainf$ minimal model is formal
 (Keller's classicality);
\item Small resolution $=$ the Koszul resolution
 $A^! \otimes_{A^{!\text{-comod}}} A^!
 \xrightarrow{\sim} A$ (Priddy);
\item Ext diagonal $=$ $\Ext^{p,q}_A(k,k) = 0$ for $p \neq q$
 (the BGS criterion).
\end{itemize}
The chiral theory is not a generalization that weakens these
conditions; it is a \emph{lift} that reveals their geometric origin.
Concentration of bar cohomology, in the classical setting, is a
combinatorial miracle. In the chiral setting, it is a consequence
of the Arnold cancellation on FM compactifications: the boundary
strata of $\FM_k(X)$ produce exact sequences, and Koszulness
is the statement that these exact sequences have no higher
cohomology. The ``miracle'' of classical Koszulness is the shadow
of the geometry of configuration spaces.
\end{remark}

exec
/bin/zsh -lc "sed -n '1338,1366p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1608,1632p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
 $\Delta[a_1|\cdots|a_n]
 = \sum_{i=0}^{n}
 [a_1|\cdots|a_i]
 \otimes [a_{i+1}|\cdots|a_n]$,
 encoding the $E_1$ (topological) coalgebra structure;
\end{enumerate}
is an $E_1$ dg coassociative coalgebra: $d_{\barB}$ is a
coderivation of $\Delta$, encoding the compatibility between
the holomorphic collision data on $\FM_k(X)$ and the topological
ordering data on $\Conf_k^{<}(\R)$.
\end{theorem}

\begin{proof}
The proof assembles three ingredients, all established earlier in
this volume and in Volume~I.

\medskip\noindent\textbf{Step 1: The bar differential.}
By Volume~I, Theorem~A, the bar differential $d_{\barB}$ satisfies
$d_{\barB}^2 = 0$ (via the Arnold cancellation on $\FM_k(X)$) and
endows $\barB_X(\cA)$ with the structure of a dg coalgebra
 succeeded in 52ms:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{The Francis--Gaitsgory bar complex}
 $\barB^{\mathrm{FG}}(\cA)$. This retains only the zeroth
 product $a_{(0)}b$ (the chiral Lie bracket), discarding all
 higher OPE poles. It is the bar complex of $\cA$ viewed as a
 chiral Lie algebra; its Koszul dual is the Francis--Gaitsgory
 chiral Lie Koszul dual $\cA^!_{\mathrm{FG}}$.

\item \emph{The symmetric bar complex}
 $\barBch(\cA) = \barB^{\Sigma}(\cA)$. This uses all OPE
 products $\{a_{(n)}b\}_{n \ge 0}$ and takes
 $\Sigma_n$-coinvariants: it is the factorisation coalgebra on
 $\operatorname{Ran}(X)$ constructed in Volume~I, Theorem~A\@.
 Verdier duality $\mathbb{D}_{\operatorname{Ran}}$ produces the
 chiral Koszul dual $\cA^!_{\mathrm{ch}}$.

\item \emph{The ordered bar complex}
 $\barB^{\mathrm{ord}}(\cA)$. This uses all OPE products but
 retains the linear ordering on insertions: no
 $\Sigma_n$-quotient. It is the cofree coalgebra


thinking
**Refining mathematical terms**

The user asked for the correct Verdier convention, so I need to be more precise: “the bar functor produces the factorization coalgebra; Verdier then gives the homotopy dual algebra.” I could tweak it to include that “its Verdier dual is the homotopy dual factorization algebra, formal to A^!_ch on the Koszul locus,” which aligns things nicely. Also, I should avoid calling out Theorem A when referencing the bar differential and use "genus-zero bar construction theorem" instead, as it keeps it clearer.
thinking
**Clarifying theorem references**

In the 4000 remark, item (ii) mentions "bar-cobar adjunction (Volume I, Theorem A) and bar-cobar inversion (Volume I, Theorem B)," which is good. If I decide to include an exact theorem package remark, that could work too. However, I think it might be worth mentioning Theorem B in relation to the coderived off locus for better clarity. This would help in understanding the context better without losing detail.
exec
/bin/zsh -lc "rg -n 'Volume~I, Theorem~B|Vol~I, Theorem~B|Theorem~B\\)' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
3620:\textup{(}Vol~I, Theorem~B\textup{)} is the Morita equivalence
3838:category of Positselski (Volume~I, Theorem~B(b)). The curvature
4001: and bar-cobar inversion \textup(Volume~I, Theorem~B\textup)
exec
/bin/zsh -lc "sed -n '3830,3850p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '3988,4010p' chapters/connections/bar-cobar-review.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

\begin{remark}[Raviolo at higher genus]
The raviolo construction (Appendix~\ref{def:raviolo-restriction})
restricts the $\R$-factorization to a time-slice $t_0 \in \R$.
At genus $g \geq 1$, this produces a \emph{curved} raviolo vertex
algebra: the bar-cobar counit
$\varepsilon\colon \Omegach(\barB^{(g)}(\cA)) \to \cA$ is a
curved quasi-isomorphism, recovering $\cA$ in the coderived
category of Positselski (Volume~I, Theorem~B(b)). The curvature
$m_0 = \kappa(\cA) \cdot \omega_g$ of the raviolo algebra
is the genus-$g$ quantum correction to the vertex algebra
structure.
\end{remark}

\begin{theorem}[Curved $E_1$ dg coalgebras at higher genus;
\ClaimStatusProvedHere]
\label{thm:curved-swiss-cheese}
At genus $g \geq 1$, the bar complex
$\barB^{(g)}(\cA)$ supports an $E_1$ dg coassociative coalgebra structure
under the period-corrected differential, not under the bare
 succeeded in 51ms:
\textup{(}Volume~I, canonical $\R$-factorization theorem\textup{)}]
\label{prop:R-canonical-vol2}%
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Uniqueness of the coproduct.}
 The bar complex $\barB(\cA) = T^c(s^{-1}\bar{\cA})$ is a
 cofree conilpotent coalgebra. The deconcatenation
 coproduct is the unique coassociative coproduct on a cofree
 coalgebra \textup(it is characterized by the projection to
 cogenerators\textup). Every coderivation of the cofree
 coalgebra is likewise determined by its cogenerator projection.
 There is no room for a second compatible $\Eone$-structure.
\item \emph{Canonicity of the presentation.}
 The bar-cobar adjunction \textup(Volume~I, Theorem~A\textup)
 and bar-cobar inversion \textup(Volume~I, Theorem~B\textup)
 guarantee that the tensor coalgebra presentation of the
 modular homotopy type is unique up to contractible choice.
 Any two bar models are connected by a zig-zag of
 quasi-isomorphisms of dg coalgebras, each preserving the
 $\Eone$-structure.
\item \emph{Survival at higher genus.}


thinking
**Formulating findings on proofs**

The remark regarding higher genus seems fine, but I'm unsure about conjectures—maybe I should keep it. I need to search for references related to Theorem D and include a non-circular proof path as the user requested. While I might not alter existing references, I could revise the construction table and clarify the line relating kappa and c. I’ve noticed some stale references in the chapter regarding Theorem A and issues with the compression of Theorem B, C, and D that I'll need to address.
thinking
**Addressing carrier specifications**

The MC2 carrier in the current construction is underspecified, listed only as `MC(\gAmod)` without explaining `\gAmod` in detail. I need to provide the exact carrier, and I’ve noticed broken internal references to a nonexistent label `thm:bar-cobar-adjunction`. Additionally, I see that the remark "What changed in Vol I" is missing, so I should add that. I'll also consider using `apply_patch` to update the audit ledger with the date 2026—though the current date is unknown, I can get it via the system command `date +%F`.
codex
I have the concrete patch set now: one theorem-package rectification, one carrier/MC2 clarification, one stale-label cleanup, and one explicit change-log remark for Vol I readers. I’m recording those findings in the audit ledger before editing the chapter itself.
exec
/bin/zsh -lc 'date +%F' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '220,320p' compute/audit/linear_read_notes.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
2026-04-13
 succeeded in 52ms:
- All 153 genus-1 tests pass.
- All 545 non-sl₃ tests pass (the sl₃ d² test failure is pre-existing and unrelated).
- Consistency checks: κ(V₁(sl₂)) = 9/4, κ(V₋₂(sl₂)) = 0 (critical level), κ(V₀(sl₂)) = 3/2.

## 2026-03-31 — Codex Bootstrap Audit

- Target: live Vol II surface (`main.tex`, active `\input` graph, dirty diff, build/test layer)
- Iteration: `0`
- Status: bootstrap pass completed; loop not yet converged

### Verification Run

- Read the Vol I rectification protocol in `~/chiral-bar-cobar/CLAUDE.md` and the live Vol II instruction surface in `AGENTS.md` and `CLAUDE.md`.
- Extracted the active `\input` map from `main.tex` and the dirty live-file surface from `git diff --name-only`.
- Ran `python3 -m pytest compute/tests/test_infrastructure.py compute/tests/test_conventions.py -q`: `68 passed in 5.17s`.
- Attempted `make fast`; the session was interrupted during pass 1.
- Ran a direct `pdflatex` follow-up pass, which exposed a corrupted `main.aux`.
- Ran `make clean`; the local artifacts cleared briefly, but a concurrent external build process repopulated `main.aux` and `.build_logs` before stable post-clean verification could be completed.

### Findings

thinking
**Updating notes entries**

I need to append a new entry to my notes, using an apply_patch method. Additionally, I should edit the notes before making any file edits or commentary. My first step will be to patch the audit notes. I might also use apply_patch to add entries. I'll check the location to see if I should append it near the top; it could go after the header or after the latest entry. Let's get started!
codex
I’m writing the audit entry now, then patching the chapter itself in one pass so the theorem-package fixes stay consistent across the local review surfaces.
file update
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
@@ -2,2 +2,49 @@
 
+## 2026-04-13 - Bar-Cobar Review Fortification
+
+- Target: `chapters/connections/bar-cobar-review.tex`
+- Status: IN PROGRESS
+
+### Findings
+
+1. `2026-04-13-002`
+   Severity: `SERIOUS`
+   Class: `D`
+   Location: `chapters/connections/bar-cobar-review.tex:205-210`, `:625`, `:1355`, `:1620`, `:2280-2413`, `:4079-4088`
+   Issue: the review chapter still advertised stale Theorem A language from earlier Vol I drafts. It conflated the genus-zero bar differential package with Main Theorem A and repeatedly treated Verdier duality as landing directly on a bar coalgebra or on the classical dual, whereas the current Vol I convention is algebra-level: `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` is the homotopy Koszul dual factorization algebra, formal to the classical dual only on the Koszul locus.
+   Fix: rewrite the theorem-package summaries so Theorem A is stated with the algebra-level Verdier convention, and retarget the bar-differential/collision statements to the genus-zero bar-construction package rather than to Main Theorem A.
+   Status: `PENDING`
+
+2. `2026-04-13-003`
+   Severity: `SERIOUS`
+   Class: `D`
+   Location: `chapters/connections/bar-cobar-review.tex:4083-4087`, related higher-genus summary prose at `:3811-3819`, `:3870-3944`
+   Issue: the local review of Theorems B--D and C still compressed away critical scope qualifiers. Theorem B was stated only as a quasi-isomorphism, omitting the off-Koszul coderived inversion. Theorem C was written as though the Lagrangian decomposition had a uniform genus-zero/genus-positive form, obscuring the `g >= 1` Lagrangian statement and the pointed/curved genus-zero base case. Theorem D was summarized without noting the non-circular proof route now used in Vol I.
+   Fix: update the review table/remarks so Theorem B carries the on-locus quasi-isomorphism plus off-locus coderived clause, Theorem C explicitly separates the `g >= 1` Lagrangian statement from the genus-zero base case, and Theorem D records the scalar-shadow/determinant-line proof path as the non-circular route.
+   Status: `PENDING`
+
+3. `2026-04-13-004`
+   Severity: `MODERATE`
+   Class: `C/D`
+   Location: `chapters/connections/bar-cobar-review.tex:4079-4089`
+   Issue: MC2 was advertised only as `\Theta_\cA \in \MC(\gAmod)`, without identifying the actual completed carrier used by the current Vol I proof, namely the genus-completed coinvariant modular convolution algebra `G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod) \cong \gAmod`.
+   Fix: add the carrier identification and the comparison between the strict shorthand `\gAmod` and the completed tensor-product presentation.
+   Status: `PENDING`
+
+4. `2026-04-13-005`
+   Severity: `MODERATE`
+   Class: `C`
+   Location: `chapters/connections/bar-cobar-review.tex:1818`, `:1915`, `:4071`
+   Issue: several local references still point to the nonexistent label `thm:bar-cobar-adjunction` rather than the live local label `thm:bar_cobar_adjunction`.
+   Fix: retarget the broken references to the live label.
+   Status: `PENDING`
+
+5. `2026-04-13-006`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/connections/bar-cobar-review.tex` near the Vol I theorem-package summary
+   Issue: the review chapter did not tell Vol II readers which Vol I statements were rectified after the original review prose was drafted, so the local summary surface still looked complete even where conventions had shifted.
+   Fix: add a dedicated `What changed in Vol I` remark listing the theorem-package rectifications relevant to this review chapter.
+   Status: `PENDING`
+
 ## 2026-04-13 - V2-AP26 Part Reference Rectification
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md
file update:
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f572fa16b47db47c77ffd7e849e341137059e7f6..376d786b3767c5ac28e49fb1ba3c357240e13a24
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,52 @@
 # Linear Read Notes
 
+## 2026-04-13 - Bar-Cobar Review Fortification
+
+- Target: `chapters/connections/bar-cobar-review.tex`
+- Status: IN PROGRESS
+
+### Findings
+
+1. `2026-04-13-002`
+   Severity: `SERIOUS`
+   Class: `D`
+   Location: `chapters/connections/bar-cobar-review.tex:205-210`, `:625`, `:1355`, `:1620`, `:2280-2413`, `:4079-4088`
+   Issue: the review chapter still advertised stale Theorem A language from earlier Vol I drafts. It conflated the genus-zero bar differential package with Main Theorem A and repeatedly treated Verdier duality as landing directly on a bar coalgebra or on the classical dual, whereas the current Vol I convention is algebra-level: `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` is the homotopy Koszul dual factorization algebra, formal to the classical dual only on the Koszul locus.
+   Fix: rewrite the theorem-package summaries so Theorem A is stated with the algebra-level Verdier convention, and retarget the bar-differential/collision statements to the genus-zero bar-construction package rather than to Main Theorem A.
+   Status: `PENDING`
+
+2. `2026-04-13-003`
+   Severity: `SERIOUS`
+   Class: `D`
+   Location: `chapters/connections/bar-cobar-review.tex:4083-4087`, related higher-genus summary prose at `:3811-3819`, `:3870-3944`
+   Issue: the local review of Theorems B--D and C still compressed away critical scope qualifiers. Theorem B was stated only as a quasi-isomorphism, omitting the off-Koszul coderived inversion. Theorem C was written as though the Lagrangian decomposition had a uniform genus-zero/genus-positive form, obscuring the `g >= 1` Lagrangian statement and the pointed/curved genus-zero base case. Theorem D was summarized without noting the non-circular proof route now used in Vol I.
+   Fix: update the review table/remarks so Theorem B carries the on-locus quasi-isomorphism plus off-locus coderived clause, Theorem C explicitly separates the `g >= 1` Lagrangian statement from the genus-zero base case, and Theorem D records the scalar-shadow/determinant-line proof path as the non-circular route.
+   Status: `PENDING`
+
+3. `2026-04-13-004`
+   Severity: `MODERATE`
+   Class: `C/D`
+   Location: `chapters/connections/bar-cobar-review.tex:4079-4089`
+   Issue: MC2 was advertised only as `\Theta_\cA \in \MC(\gAmod)`, without identifying the actual completed carrier used by the current Vol I proof, namely the genus-completed coinvariant modular convolution algebra `G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod) \cong \gAmod`.
+   Fix: add the carrier identification and the comparison between the strict shorthand `\gAmod` and the completed tensor-product presentation.
+   Status: `PENDING`
+
+4. `2026-04-13-005`
+   Severity: `MODERATE`
+   Class: `C`
+   Location: `chapters/connections/bar-cobar-review.tex:1818`, `:1915`, `:4071`
+   Issue: several local references still point to the nonexistent label `thm:bar-cobar-adjunction` rather than the live local label `thm:bar_cobar_adjunction`.
+   Fix: retarget the broken references to the live label.
+   Status: `PENDING`
+
+5. `2026-04-13-006`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/connections/bar-cobar-review.tex` near the Vol I theorem-package summary
+   Issue: the review chapter did not tell Vol II readers which Vol I statements were rectified after the original review prose was drafted, so the local summary surface still looked complete even where conventions had shifted.
+   Fix: add a dedicated `What changed in Vol I` remark listing the theorem-package rectifications relevant to this review chapter.
+   Status: `PENDING`
+
 ## 2026-04-13 - V2-AP26 Part Reference Rectification
 
 - Target: `chapters/connections/conclusion.tex`, mirrored `.claude/worktrees/*/chapters/connections/conclusion.tex`

file update:
diff --git a/compute/audit/linear_read_notes.md b/compute/audit/linear_read_notes.md
index f572fa16b47db47c77ffd7e849e341137059e7f6..376d786b3767c5ac28e49fb1ba3c357240e13a24
--- a/compute/audit/linear_read_notes.md
+++ b/compute/audit/linear_read_notes.md
@@ -1,5 +1,52 @@
 # Linear Read Notes
 
+## 2026-04-13 - Bar-Cobar Review Fortification
+
+- Target: `chapters/connections/bar-cobar-review.tex`
+- Status: IN PROGRESS
+
+### Findings
+
+1. `2026-04-13-002`
+   Severity: `SERIOUS`
+   Class: `D`
+   Location: `chapters/connections/bar-cobar-review.tex:205-210`, `:625`, `:1355`, `:1620`, `:2280-2413`, `:4079-4088`
+   Issue: the review chapter still advertised stale Theorem A language from earlier Vol I drafts. It conflated the genus-zero bar differential package with Main Theorem A and repeatedly treated Verdier duality as landing directly on a bar coalgebra or on the classical dual, whereas the current Vol I convention is algebra-level: `\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)` is the homotopy Koszul dual factorization algebra, formal to the classical dual only on the Koszul locus.
+   Fix: rewrite the theorem-package summaries so Theorem A is stated with the algebra-level Verdier convention, and retarget the bar-differential/collision statements to the genus-zero bar-construction package rather than to Main Theorem A.
+   Status: `PENDING`
+
+2. `2026-04-13-003`
+   Severity: `SERIOUS`
+   Class: `D`
+   Location: `chapters/connections/bar-cobar-review.tex:4083-4087`, related higher-genus summary prose at `:3811-3819`, `:3870-3944`
+   Issue: the local review of Theorems B--D and C still compressed away critical scope qualifiers. Theorem B was stated only as a quasi-isomorphism, omitting the off-Koszul coderived inversion. Theorem C was written as though the Lagrangian decomposition had a uniform genus-zero/genus-positive form, obscuring the `g >= 1` Lagrangian statement and the pointed/curved genus-zero base case. Theorem D was summarized without noting the non-circular proof route now used in Vol I.
+   Fix: update the review table/remarks so Theorem B carries the on-locus quasi-isomorphism plus off-locus coderived clause, Theorem C explicitly separates the `g >= 1` Lagrangian statement from the genus-zero base case, and Theorem D records the scalar-shadow/determinant-line proof path as the non-circular route.
+   Status: `PENDING`
+
+3. `2026-04-13-004`
+   Severity: `MODERATE`
+   Class: `C/D`
+   Location: `chapters/connections/bar-cobar-review.tex:4079-4089`
+   Issue: MC2 was advertised only as `\Theta_\cA \in \MC(\gAmod)`, without identifying the actual completed carrier used by the current Vol I proof, namely the genus-completed coinvariant modular convolution algebra `G^1(\Defcyc(\cA)\widehat{\otimes}\Gmod) \cong \gAmod`.
+   Fix: add the carrier identification and the comparison between the strict shorthand `\gAmod` and the completed tensor-product presentation.
+   Status: `PENDING`
+
+4. `2026-04-13-005`
+   Severity: `MODERATE`
+   Class: `C`
+   Location: `chapters/connections/bar-cobar-review.tex:1818`, `:1915`, `:4071`
+   Issue: several local references still point to the nonexistent label `thm:bar-cobar-adjunction` rather than the live local label `thm:bar_cobar_adjunction`.
+   Fix: retarget the broken references to the live label.
+   Status: `PENDING`
+
+5. `2026-04-13-006`
+   Severity: `MODERATE`
+   Class: `D/W`
+   Location: `chapters/connections/bar-cobar-review.tex` near the Vol I theorem-package summary
+   Issue: the review chapter did not tell Vol II readers which Vol I statements were rectified after the original review prose was drafted, so the local summary surface still looked complete even where conventions had shifted.
+   Fix: add a dedicated `What changed in Vol I` remark listing the theorem-package rectifications relevant to this review chapter.
+   Status: `PENDING`
+
 ## 2026-04-13 - V2-AP26 Part Reference Rectification
 
 - Target: `chapters/connections/conclusion.tex`, mirrored `.claude/worktrees/*/chapters/connections/conclusion.tex`

ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 4:15 PM.
tokens used
194,507
