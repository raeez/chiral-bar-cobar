# C12_kac_moody (564s)

- [CRITICAL] `chapters/examples/kac_moody.tex:133` — PROBLEM: `\kappa` is introduced here as the affine modular characteristic, but the same chapter reuses `\kappa` for the Casimir element at `521-523` and `649-651`, and for the Killing form at `572`. Three different objects collapse into one symbol. FIX: reserve `\kappa(\widehat{\fg}_k)` or `\kappa_{\mathrm{KM}}` for the scalar invariant; rename the Casimir element to `\Omega_{\fg}` in the curvature formulas (`m_0=\frac{k+h^\vee}{2h^\vee}\Omega_{\fg}`); rename the Killing form in `572` to `\kappa_{\fg}` or `K_{\mathfrak{sl}_2}`.

- [CRITICAL] `chapters/examples/kac_moody.tex:2094` — PROBLEM: `r(z) = \Omega/(k+2)\,z` parses as `(\Omega/(k+2))z`, not `\Omega/((k+2)z)`; the same typo recurs at `2263` and `2357`. FIX: rewrite them as `r(z)=\Omega/((k+2)\,z)` and `r_{ij}=\Omega/((k+2)\,z_{ij})`.

- [HIGH] `chapters/examples/kac_moody.tex:497` — PROBLEM: `thm:level-shifting-abstract` duplicates the general affine level-shift theorem later stated at `1104-1119`, and its proof is only a forward pointer. FIX: delete the theorem/proof block at `497-512` and replace it with a short roadmap remark pointing to `thm:universal-kac-moody-koszul`.

- [HIGH] `chapters/examples/kac_moody.tex:4133` — PROBLEM: `\section{Open problems and conjectures}` appears before later proved material (`thm:oper-bar-h0` at `4292` onward). The chapter announces a conjectural lane and then resumes theorem-proof exposition. FIX: move `4133-4287` to the end of the chapter and merge it into one final `\section{Open Problems}` after `6063`.

- [HIGH] `chapters/examples/kac_moody.tex:4500` — PROBLEM: a second `\section{Open questions}` interrupts the flow immediately before the proved section `The affine cubic shadow and critical-level emergence` at `4528`. FIX: move `4500-4526` into the same final end-of-chapter open-problems section and start `4528` with a forcing transition such as `The remaining local calculation is the affine cubic shadow.`

- [MEDIUM] `chapters/examples/kac_moody.tex:199` — PROBLEM: `\textup{(};` is malformed punctuation; the same defect recurs at `1312` as `\textup{(}:`. FIX: rewrite both clauses as ordinary prose, e.g. `at every genus; all currents $J^a$ have conformal weight~$1$, so ...` and `via $\mathrm{obs}_g=\kappa(\widehat{\fg}_k)\lambda_g$; all currents share conformal weight~$1$, so ...`.

- [MEDIUM] `chapters/examples/kac_moody.tex:1626` — PROBLEM: `for exceptional types. The full shadow obstruction tower data.` is a sentence fragment. FIX: replace `1624-1626` with `These consistency checks determine the remaining shadow obstruction data for the exceptional types.`

- [MEDIUM] `chapters/examples/kac_moody.tex:5787` — PROBLEM: the section opener is a fragment, not a sentence. FIX: replace `5787-5790` with `This section gives the gauge-theoretic interpretation of the affine vertex algebra: its PVA $\lambda$-bracket is the Poisson bracket of 3d holomorphic-topological Chern--Simons theory on $\Sigma \times \mathbb{R}_t$.`

- [LOW] `chapters/examples/kac_moody.tex:18` — PROBLEM: `This is the content of the assertion that gauge theory is simpler than gravity` drops a slogan into an otherwise mathematical opening. FIX: replace `18-21` with `This contrast is precise: for the Virasoro algebra (Chapter~\ref{chap:w-algebras}), no Jacobi relation annihilates the quartic term, so the tower does not terminate.`

- [LOW] `chapters/examples/kac_moody.tex:1635` — PROBLEM: `\label{tab:exceptional-shadow-data}` sits inside a proposition block without a `table`/`caption`, and I found no `\ref{tab:exceptional-shadow-data}` in the TeX tree. FIX: delete line `1635`; if a table reference is actually needed later, wrap the tabular block in a real `table` environment and attach the label to its caption.

- [LOW] `chapters/examples/kac_moody.tex:2370` — PROBLEM: the remark carries two labels, `rem:category-O-affine` and `rem:bgg-kl-bridge`, and I found no `\ref{...}` to either in the TeX tree. This is dead anchor clutter. FIX: keep one canonical label only, preferably `\label{rem:bgg-kl-bridge}`, and delete the other.

- [LOW] `chapters/examples/kac_moody.tex:3017` — PROBLEM: the coined adjective `theorematic` is ugly and repeated at `3175`, `3295`, and `4219`. FIX: replace it with plain words: `main remaining gap` at `3017`, `proved general-rank identification` at `3175`, `no proved equal-rank statement` at `3295`, and `with target the \emph{semisimplified tilting quotient}` at `4219`.

## Summary
Checked: 6074 | Findings: 12 | Verdict: FAIL


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
session id: 019d83fd-f588-7301-9890-4912187db4a7
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


MISSION: COSMETIC & AESTHETIC AUDIT of chapters/examples/kac_moody.tex

Read the entire file. Audit for:

1. **AI slop vocabulary** (AP29): moreover, additionally, notably, crucially, remarkably,
   interestingly, furthermore, delve, leverage, tapestry, cornerstone, "it is worth noting".
   FIX: rewrite each occurrence without the slop word.

2. **Em dashes** (---  or U+2014): FORBIDDEN.
   FIX: replace with colon, semicolon, or separate sentence.

3. **Markdown in LaTeX** (AP121): backtick numerals, **bold**, _italic_.
   FIX: use $...$, \textbf, \emph.

4. **Chapter opening quality**: Does the chapter open with the PROBLEM (CG deficiency opening)?
   Or does it open with "In this chapter we..." (AP106/AP109)?
   FIX: rewrite the opening to state the deficiency/problem first.

5. **Passive voice hedging** in mathematical statements: "it can be shown", "one might expect",
   "it seems reasonable". If the math is clear, STATE it. If not, mark conjecture.
   FIX: active voice or explicit conjecture.

6. **Notation consistency**: Are macros used consistently? Any bare \kappa without family?
   Any bare \Omega/z without level k? Any undefined macros?
   FIX: add family superscript, level prefix, or macro definition.

7. **Dead code**: commented-out sections >10 lines, unused labels, TODOs/FIXMEs.
   FIX: delete dead code or resolve TODOs.

8. **Redundancy**: Same theorem stated in multiple places with different wording.
   FIX: state once, cite elsewhere.

9. **Transition quality**: Does each section force the next? Or do transitions use
   "We now turn to..." signpost language (AP109)?
   FIX: mathematical necessity transitions.

10. **Typography**: double spaces, inconsistent spacing around operators, broken LaTeX
    environments, mismatched braces.
    FIX: fix each instance.

Report EVERY finding with exact line number and exact fix.
mcp startup: no servers
codex
Using `deep-beilinson-audit` as the working mode. I’m starting by reading the entire target file and its local structure so the findings stay grounded in exact lines, then I’ll pressure-test each requested cosmetic surface against the manuscript’s own conventions.
collab spawn_agent(call_Mw2gtGpohoxvQaraxVx9JCIO, prompt="Read the entire file `chapters/examples/kac_moody.tex` and audit it for the user’s requested cosmetic/aesthetic issues o…")
spawn_agent(call_Mw2gtGpohoxvQaraxVx9JCIO, prompt="Read the entire file `chapters/examples/kac_moody.tex` and audit it for the user’s requested cosmetic/aesthetic issues o…") pending init:
  agent: 019d83fe-2fa8-7830-98e8-f27b6be2239d
mcp startup: no servers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
\label{chap:kac-moody}

The Heisenberg algebra is abelian: its shadow tower terminates at
degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
The first nonabelian chiral algebra is
$\widehat{\mathfrak{g}}_k$, and the question that
governs this chapter is whether the Lie bracket destroys the
finiteness of the obstruction tower or preserves it.
%
It preserves it. The Lie bracket of~$\fg$ appears as the
cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
degree~$3$; the Jacobi identity forces the quartic shadow to vanish;
the tower terminates (class~$L$, $r_{\max} = 3$). Gauge symmetry
introduces noncommutativity but not infinite obstruction complexity:
the structure constants of~$\fg$ produce exactly one new shadow
beyond the Gaussian, and the Jacobi identity is the mechanism that
kills the rest. This is the content of the assertion that gauge
theory is simpler than gravity; for the Virasoro algebra
(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '200,400p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds
unconditionally, cf.\ Theorem~D\textup{)};
(iii)~the Sugawara construction at non-critical level gives a Virasoro
element in the PVA, so Khan--Zeng~\cite{KZ25} topological resonance
reduction applies and the shadow obstruction tower simplifies.
\end{remark}

\begin{remark}[Genus-two shell profile: Kac--Moody]
\label{rem:km-genus-two-shells}
\index{Kac--Moody!genus-two shells}
\index{genus-two shells!Lie/tree archetype}
In the genus-two shell decomposition
(Construction~\ref{const:vol1-genus-two-shells}),
the Lie/tree archetype sees two of the three shells:
$\Theta^{(2)}_{\mathrm{loop} \circ \mathrm{loop}}$ (iterated
non-separating loop) and
$\Theta^{(2)}_{\mathrm{sep} \circ \mathrm{loop}}$ (mixed
separating/non-separating clutching), but NOT the planted-forest
shell $\Theta^{(2)}_{\mathrm{pf}}$. This is because strict
formality (Theorem~\ref{thm:km-strictification}) kills all
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '261,520p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
 succeeded in 53ms:
\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
\label{chap:kac-moody}

The Heisenberg algebra is abelian: its shadow tower terminates at
degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
The first nonabelian chiral algebra is
$\widehat{\mathfrak{g}}_k$, and the question that
governs this chapter is whether the Lie bracket destroys the
finiteness of the obstruction tower or preserves it.
%
It preserves it. The Lie bracket of~$\fg$ appears as the
cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
degree~$3$; the Jacobi identity forces the quartic shadow to vanish;
the tower terminates (class~$L$, $r_{\max} = 3$). Gauge symmetry
introduces noncommutativity but not infinite obstruction complexity:
the structure constants of~$\fg$ produce exactly one new shadow
beyond the Gaussian, and the Jacobi identity is the mechanism that
kills the rest. This is the content of the assertion that gauge
theory is simpler than gravity; for the Virasoro algebra
(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the
 succeeded in 53ms:
(iii)~\emph{strictly formal} by
Theorem~\ref{thm:km-strictification}: the archetype of
strictification, with no higher homotopy corrections at any genus
(Corollary~\ref{cor:strictification-comparison}(iii));
(iv)~genus tower with $\kappa = \dim(\mathfrak{g})\cdot(k + h^\vee)/(2h^\vee)$, Lie/tree shadow
archetype, terminates at $r = 3$.
\end{remark}

\section{The Kac--Moody bar complex}%
\label{sec:km-bar-complex}

Let $\mathfrak{g}$ be a finite-dimensional simple Lie algebra with
Killing form $(\cdot,\cdot)$ and dual Coxeter number~$h^\vee$.
The affine Kac--Moody chiral algebra $\widehat{\mathfrak{g}}_k$
at level $k \neq -h^\vee$ is generated by currents
$J^a(z)$, $a = 1, \ldots, \dim \mathfrak{g}$, with OPE
\[
 J^a(z)\,J^b(w) \;=\; \frac{k\,(a,b)}{(z-w)^2}
 \;+\; \frac{f^{ab}{}_c \, J^c(w)}{z-w}
 \;+\; \text{regular},
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '400,800p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
satisfying the OPE:
\begin{equation}\label{eq:affine-kac-moody-ope}
J^a(z) J^b(w) \sim \frac{k \kappa^{ab}}{(z-w)^2} + \frac{{f^{ab}}_c J^c(w)}{z-w}
\end{equation}
where $\kappa^{ab} = \kappa_{\mathfrak{g}}(T^a, T^b)$ is the normalized invariant bilinear form on $\mathfrak{g}$ (normalized so that long roots have squared length $2$), ${f^{ab}}_c$ are the structure constants, and $\sim$ means ``has singular part.'' In an orthonormal basis with $\kappa^{ab} = \delta^{ab}$, this reduces to the familiar form $k\delta^{ab}/(z-w)^2$.
\end{definition}

\begin{definition}[Chiral algebra perspective]\label{def:chiral-kac-moody}
Following Beilinson--Drinfeld, the affine Kac--Moody chiral algebra $\widehat{\mathfrak{g}}_k$ at level $k$ on a smooth curve $X$ is the $\mathcal{D}_X$-module:
\begin{equation}
\widehat{\mathfrak{g}}_k = \mathcal{U}_k(\mathfrak{g}) := \left(\mathfrak{g} \otimes_{\mathbb{C}} \mathcal{D}_X\right) / \langle [x \otimes P, y \otimes Q] - [x,y] \otimes PQ - k \cdot \kappa_{\mathfrak{g}}(x,y) \cdot P(Q) \rangle
\end{equation}
where $P, Q \in \mathcal{D}_X$ are differential operators and $P(Q)$ denotes the action of $P$ on $Q$ as a function.
\end{definition}

\begin{theorem}[Equivalence of perspectives \cite{FBZ04, BD04}; \ClaimStatusProvedElsewhere]\label{thm:vertex-chiral-equivalence}
For $X = \mathbb{A}^1$ with coordinate $z$, the vertex algebra $V_k(\mathfrak{g})$ and the chiral algebra $\widehat{\mathfrak{g}}_k$ encode the same mathematical structure. The dictionary is:
\begin{align}
J^a_n &\longleftrightarrow x^a \otimes t^n \in L\mathfrak{g} \quad \text{(loop algebra element)} \\
T(z) = \sum_n L_n z^{-n-2} &\longleftrightarrow \text{Sugawara stress tensor}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '800,1200p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\end{itemize}

The currents are given by explicit formulas:
\begin{align}
e_{\alpha_i}(z) &= \beta_{\alpha_i}(z) \\
e_{-\alpha_i}(z) &= \text{differential polynomial in } \beta_{\alpha_i}, \gamma_{\alpha_i}, \phi_i, \partial\phi_i \\
h_i(z) &= -\alpha_i(\phi)(z) + \text{screening charge corrections}
\end{align}
\end{theorem}

\subsection{Level-shifting duality}

\begin{theorem}[Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k}; \ClaimStatusProvedHere]\label{thm:sl3-koszul-dual}
\begin{equation}
(\widehat{\mathfrak{sl}}_{3,k})^! \simeq \widehat{\mathfrak{sl}}_{3,-k-6}
\end{equation}
The shift is $-k - 2h^\vee = -k - 6$ since $h^\vee = 3$ for $\mathfrak{sl}_3$.
\end{theorem}

\begin{proof}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1200,1600p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

Therefore $k^* = -k - 2h^\vee$, and the cobar OPE~\eqref{eq:cobar-ope} becomes:
\begin{equation}
J^{a,*}(z) J^{b,*}(w) \sim \frac{(-k-2h^\vee)(J^a, J^b)}{(z-w)^2} + \frac{f^{ab}{}_{c}\, J^{c,*}(w)}{z-w}
\end{equation}
which is precisely the OPE of $\widehat{\mathfrak{g}}_{-k-2h^\vee}$. (For $\mathfrak{sl}_2$: $-k-2 \cdot 2 = -k-4$, matching Theorem~\ref{thm:sl2-koszul-dual}.)

\emph{Step~4: Functorial uniqueness.}
The cobar construction $\Omega(\bar{B}(\widehat{\mathfrak{g}}_k))$ is characterized by a universal property: for any chiral algebra~$\mathcal{A}$,
\begin{equation}
\mathrm{Hom}_{\text{ChirAlg}}\bigl(\Omega(\bar{B}(\widehat{\mathfrak{g}}_k)),\, \mathcal{A}\bigr) \cong \mathrm{Hom}_{\text{Coalg}}\bigl(\bar{B}(\widehat{\mathfrak{g}}_k),\, \bar{B}(\mathcal{A})\bigr)
\end{equation}
This determines $(\widehat{\mathfrak{g}}_k)^!$ uniquely up to quasi-isomorphism. Since we have identified the dual bar OPE as having the structure constants $f^{ab}{}_c$ at level $-k-2h^\vee$, the Koszul dual algebra is the chiral Chevalley--Eilenberg algebra $(\widehat{\mathfrak{g}}_k)^! = \mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$, with modular characteristic $\kappa(\widehat{\mathfrak{g}}_{-k-2h^\vee})$. (This is not the same object as $\widehat{\mathfrak{g}}_{-k-2h^\vee}$ itself; the Koszul dual and the Feigin--Frenkel level-reflected algebra share the same~$\kappa$ but differ as chiral algebras.) Bar-cobar inversion $\Omega(\bar{B}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ recovers the original algebra at level~$k$.

\emph{Consistency checks.}
\begin{enumerate}
\item \emph{Involutivity}: The level involution $k \mapsto -k - 2h^\vee$ is involutive: $-(-k-2h^\vee) - 2h^\vee = k$. At the level of modular characteristics, $\kappa((\widehat{\mathfrak{g}}_k)^{!!}) = \kappa(\widehat{\mathfrak{g}}_k)$. \checkmark
\item \emph{Critical level fixed point}: At $k = -h^\vee$, the dual level is $-(-h^\vee) - 2h^\vee = -h^\vee$, so the critical level is a fixed point of the duality involution. This is the critical specialization of the internal level-shift formula (Proposition~\ref{prop:verdier-level-identification}) and is compatible with the external Feigin--Frenkel critical-level package (Theorem~\ref{thm:critical-level-structure}). \checkmark
\item \emph{Explicit verification}: For $\mathfrak{sl}_2$ (Theorem~\ref{thm:sl2-koszul-dual}) and $\mathfrak{sl}_3$ (\S\ref{sec:sl3-computation}), the low-degree bar complex computations confirm the predicted dual level. \checkmark
\end{enumerate}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1600,2000p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
The simple-pole channel $\kappa_{\mathrm{sp}} =
\dim(\fg)/2$ depends only on the Lie algebra~$\fg$ (via the
structure constants $f^{ab}{}_c$), not on the level, so
$\kappa_{\mathrm{sp}}' = \kappa_{\mathrm{sp}}$.
For the double-pole channel:
\[
\kappa_{\mathrm{dp}}'
= \frac{(-k - 2h^\vee) \cdot \dim\fg}{2h^\vee}
= -\frac{k \cdot \dim\fg}{2h^\vee}
 - \frac{2h^\vee \cdot \dim\fg}{2h^\vee}
= -\kappa_{\mathrm{dp}} - \dim\fg
= -\kappa_{\mathrm{dp}} - 2\kappa_{\mathrm{sp}}.
\]
In matrix form this is~\eqref{eq:ff-shear}.
\end{proof}

\subsection{Exceptional types: shadow data for $E_6$, $E_7$, $E_8$}%
\label{sec:exceptional-shadow-data}
\index{E6@$E_6$!shadow data}
\index{E7@$E_7$!shadow data}
codex
I’ve read the opening half of `chapters/examples/kac_moody.tex`. The chapter starts with a real deficiency opening rather than the banned “In this chapter we…” pattern, so the next pass is hunting line-level cosmetic failures and second-order drift deeper in the file.
exec
/bin/zsh -lc 'wc -l chapters/examples/kac_moody.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '781,1040p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '521,780p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    6074 chapters/examples/kac_moody.tex
 succeeded in 52ms:
m_0 = \frac{k+h^\vee}{2h^\vee} \cdot \kappa, \qquad m_1^2(a) = [m_0, a] = m_2(m_0, a) - m_2(a, m_0)
\end{equation}
where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
\end{definition}

\subsection{The Wakimoto perspective}

\begin{definition}[Wakimoto module]\label{def:wakimoto}
\index{Wakimoto representation|textbf}
The Wakimoto module $\mathcal{M}_{\mathrm{Wak}}$ at critical level is the free field algebra
\begin{equation}
\mathcal{M}_{\mathrm{Wak}} = \mathrm{Free}[\beta_\alpha, \gamma_\alpha, \phi_i]
\end{equation}
generated by a $\beta$-$\gamma$ system $(\beta_\alpha, \gamma_\alpha)$ of conformal weights $(1, 0)$ for each positive root $\alpha \in \Delta_+$, together with $r = \mathrm{rank}(\mathfrak{g})$ free bosons $\phi_i$ for the Cartan generators. The currents $J^a = f^a(\beta, \gamma, \phi, \partial\phi)$ are explicit differential polynomials determined by the Wakimoto construction.
\end{definition}

\begin{theorem}[Wakimoto realization is Koszul dual; \ClaimStatusProvedHere]\label{thm:wakimoto-koszul}
At critical level $k = -h^\vee$, the Wakimoto free field realization provides the Koszul dual resolution:
\begin{equation}
\bar{B}(\widehat{\mathfrak{g}}_{-h^\vee}) \;\simeq\; \bar{B}(\mathcal{M}_{\mathrm{Wak}})^{Q_{\mathrm{DS}}}
 succeeded in 52ms:

\begin{definition}[\texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} generators]
Current generators:
\begin{itemize}
\item Cartan currents: $h_1(z), h_2(z)$
\item Root currents: $e_{\alpha}(z)$ for $\alpha \in \Delta_+$, and $e_{-\alpha}(z)$ for $-\alpha \in \Delta_-$
\end{itemize}
with OPEs determined by the $\mathfrak{sl}_3$ structure constants and level $k$.
\end{definition}

\subsection{\texorpdfstring{Critical level: $k = -3$}{Critical level: k = -3}}

\begin{theorem}[Wakimoto for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} \cite{Frenkel-Kac-Wakimoto92}; \ClaimStatusProvedElsewhere]\label{thm:w3-wakimoto-sl3}
At $k = -3$, the Wakimoto module uses:
\begin{itemize}
\item $(\beta_{\alpha_1}, \gamma_{\alpha_1})$: $\beta$-$\gamma$ system for root $\alpha_1$
\item $(\beta_{\alpha_2}, \gamma_{\alpha_2})$: $\beta$-$\gamma$ system for root $\alpha_2$
\item $(\beta_{\alpha_1+\alpha_2}, \gamma_{\alpha_1+\alpha_2})$: $\beta$-$\gamma$ system for root $\alpha_1+\alpha_2$
\item $\phi_1, \phi_2$: free bosons for the Cartan
\end{itemize}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2000,2400p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
$\bar{B}^n = \Gamma(\overline{C}_{n+1}(X),\, \mathfrak{g}^{\boxtimes(n+1)} \otimes \mathcal{L}_k \otimes \Omega^n_{\log})$
and choose a basis using decorated trees.

\emph{Step~2: Differentials.}
For each basis element $\omega \in \bar{B}^n$, compute $d(\omega) = \sum_{i<j} \mathrm{Res}_{z_i=z_j}[\omega]$ by residue calculus, obtaining the matrix of $d^n: \bar{B}^n \to \bar{B}^{n+1}$.

\emph{Step~3: Curvature.}
Set $m_0 = (k+h^\vee) \cdot (\text{Casimir})$ and verify the curved $A_\infty$ relation $m_1^2(a) = [m_0, a]$ for all generators $a$.

\emph{Step~4: Cobar.}
Dualize $\bar{B}^n \mapsto (\bar{B}^n)^\vee$, reverse the grading, twist the differential by curvature, and form $(\widehat{\mathfrak{g}}_k)^! = \Omega(\bar{B}(\widehat{\mathfrak{g}}_k))$.

\emph{Step~5: Extraction.}
The generators are $H^1((\widehat{\mathfrak{g}}_k)^!)$, the relations
are $\operatorname{Im}(d^2) \subset (\bar{B}^2)^\vee$. The OPE of
the dual generators $J^{a*}$ is determined by the residue pairing:
$J^{a*}_{(0)} J^{b*} = f^{ab}_c J^{c*}$ (inherited from the
structure constants of~$\mathfrak{g}$, since the Lie bracket is
level-independent) and $J^{a*}_{(1)} J^{b*} = (-k - 2h^\vee)
\delta^{ab}$ (from the dual curvature $m_0^! = -(k + h^\vee)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2400,2800p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\emph{Step~1.}
The Koszul dual
$(\widehat{\mathfrak{g}}_k)^! = \mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$
is identified in Theorem~\ref{thm:universal-kac-moody-koszul} (\ClaimStatusProvedHere).

\emph{Step~2.}
The Kazhdan--Lusztig equivalence \cite{KL93}
(\ClaimStatusProvedElsewhere) identifies, for $k$ a positive integer:
\[
\mathcal{O}_k^{\mathrm{int}}(\widehat{\mathfrak{g}})
\;\simeq\;
\mathcal{C}(U_q(\mathfrak{g})), \qquad
q = e^{\pi i/(k + h^\vee)},
\]
where $\mathcal{C}(U_q(\mathfrak{g}))$ is the semisimplified tilting
category (Definition~\ref{def:tilting-module}), not the full
representation category $\mathrm{Rep}(U_q(\mathfrak{g}))$.
Applied to the Koszul dual level $k' = -k - 2h^\vee$:
\[
q' = e^{\pi i/(k' + h^\vee)}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2800,3200p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
every bar degree is finite-dimensional. Because the reduced bar
construction is positively graded, only finitely many bar degrees
contribute to a fixed conformal-weight sector. Hence the induced
spectral sequence is finite in every fixed weight sector and
therefore converges after finitely many pages there. The later
character theorems make this finite-page control explicit in the
Kac--Wakimoto setting.

For (ii): when $X_{L_k} = \overline{\mathbb{O}} \neq \{0\}$,
the reduced quotient is a positive-dimensional Poisson variety.
Construction~\ref{constr:li-bar-spectral-sequence},
Theorem~\ref{thm:associated-variety-koszulness}, and
Proposition~\ref{prop:large-orbit-obstruction} show that the
reduced Li--bar page sees the Poisson-bracket-induced $d_1$
surface, while nilradical contributions remain as separate
obstructions on the full associated graded. This gives a
bar-side source of additional differentials and off-diagonal
cohomology, but it does not identify those groups with Ext in the
ordinary admissible module category.
\end{proof}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3200,3600p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
computes the vacuum admissible character. Together with the
standard admissible character package for the second simple
module and the modular transformation law, this determines the
modular $S$-matrix; together with the standard semisimple
Verlinde formalism for this rational admissible category, this
yields the fusion ring as follows.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{S-matrix.} The two admissible simples
 $L_0 = L_{-1/2}(\mathfrak{sl}_2)$ (vacuum) and
 $L_1$ (non-vacuum, $h = 3/8$) have modular S-matrix
 \begin{equation}\label{eq:admissible-s-matrix}
 S = \frac{1}{\sqrt{2}}
 \begin{pmatrix}
 1 & 1 \\[3pt]
 1 & -1
 \end{pmatrix}.
 \end{equation}
 This is the unique unitary symmetric matrix satisfying
 $(SS^*)^2 = I$ and $S_{0j} > 0$ for all~$j$, determined
 by the modular transformation of the vacuum character from

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3600,4000p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
$\widehat{\mathfrak{g}}_{-h^\vee}$, which is identified with
the algebra of functions on the space of $\mathfrak{g}^\vee$-opers
on the formal disc
via the Feigin--Frenkel isomorphism.

Part (iii): Arakawa proves that $H^i_{\mathrm{DS}} = 0$ for
$i \neq 0$ on admissible modules, and the $H^0$ is simple
when non-zero (since DS sends composition series to
composition series and the admissible simples form a finite
collection).
\end{proof}

\begin{proposition}[Bar complex via Whittaker resolution;
\ClaimStatusProvedHere]
\label{prop:bar-whittaker}
\index{Whittaker module!bar complex}
\index{bar complex!Whittaker resolution}
Let $M$ be a module in the admissible category
$\mathrm{KL}_k$ at admissible level~$k$ and
$\chi$ a non-degenerate character.

thinking
**Examining file analysis**

I've got a file with 6074 lines and maybe around 50k tokens, which feels a bit overwhelming! Since the user wants exact line numbers and fixes, I can search for patterns across the file. I might not need to read the entire thing, so running sed to handle chunks seems practical. I'll need to focus on auditing for cosmetic issues like banned words, markdown, and consistency patterns. Given the size, I expect there could be numerous findings!
thinking
**Planning exhaustive audit**

The user wants a comprehensive report on the findings, which might produce a lot but could still be manageable. To tackle this, I should gather line numbers for specific patterns using tools like rg with multiple queries. Given there’s no network access, I’ll need to inspect macro definitions too, looking for any undefined macros present in the context of the file. Running a LaTeX compile or checking logs might be useful if needed, but it seems like the focus should be on cosmetic issues.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4000,4400p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

\begin{remark}[Critical level for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3}]
At $k = -h^\vee = -3$, the curvature vanishes. The Feigin--Frenkel center $\mathfrak{z}(\widehat{\mathfrak{sl}}_{3,-3})$ is a polynomial algebra in $2$ generators (corresponding to the $2$ fundamental invariants of $\mathfrak{sl}_3$, of degrees $2$ and $3$), consistent with the Wakimoto realization (Theorem~\ref{thm:w3-wakimoto-sl3}).
\end{remark}

\subsection{Spectral sequence collapse}

\begin{theorem}[Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k}; \ClaimStatusProvedHere]
\label{thm:sl3-genus1-inversion}
For generic level $k$ (i.e., $k+3 \notin \mathbb{Q}_{\leq 0}$), the genus-1 bar-cobar adjunction:
\begin{equation}
\Omega\bigl(\barB^{(1)}(\widehat{\mathfrak{sl}}_{3,k})\bigr) \xrightarrow{\;\sim\;} \widehat{\mathfrak{sl}}_{3,k}
\end{equation}
is a quasi-isomorphism. The spectral sequence collapses at $E_2$.
\end{theorem}

\begin{proof}
This is Theorem~\ref{thm:higher-genus-inversion} for $g=1$, $\mathfrak{g}=\mathfrak{sl}_3$.

\emph{Step~1: Weight filtration and $E_1$ page.}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4400,4800p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
decomposition (Proposition~\ref{prop:whitehead-spectral-decomposition})
extends to all~$n$. Any global curve-level or de~Rham enhancement
requires additional Beilinson--Drinfeld / localization input and is not
proved by this theorem alone.
\end{remark}

\subsection{The oper space at critical level: summary}
\label{subsec:oper-critical-summary}
\index{opers!critical level summary}

The bar complex of the affine algebra at critical level
$k = -h^\vee$ occupies a distinguished position in the theory.
By Corollary~\ref{cor:critical-level-universality}, the bar
complex $\barB(\widehat{\fg}_{-h^\vee})$ is \emph{uncurved}:
the curvature $m_0$ vanishes because the Sugawara construction
degenerates at the critical level. The first two cohomology
groups have been identified:

\begin{itemize}
\item $H^0(\barB(\widehat{\fg}_{-h^\vee}))
codex
The file is much larger than the first pass suggested: `chapters/examples/kac_moody.tex` is 6,074 lines. I’m continuing linearly through the rest of it, but I’m also running targeted pattern scans in parallel so the audit catches both obvious slop and buried second-order issues.
exec
/bin/zsh -lc "sed -n '1041,1560p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\label{conj:sl2-bar-spin-representations}
\ClaimStatusConjectured
\index{bar complex!$\widehat{\mathfrak{sl}}_2$!spin representation|textbf}
\index{Garland--Lepowsky concentration!representation-theoretic refinement}
For each $n \geq 1$, the bar cohomology
$H^n(\bar{B}^\bullet(\widehat{\mathfrak{sl}}_{2,k}))$
at generic level~$k$ carries a natural
$\mathfrak{sl}_2$-module structure
\textup{(}from the adjoint action of~$\mathfrak{sl}_2$
on its negative loop algebra\textup{)},
and this module is isomorphic to the spin-$n$
irreducible representation~$V_n$ of~$\mathfrak{sl}_2$:
\begin{equation}\label{eq:sl2-bar-spin-n}
 H^n\bigl(\bar{B}^\bullet(\widehat{\mathfrak{sl}}_{2,k})\bigr)
 \;\cong\; V_n
 \qquad(n \geq 1),
\end{equation}
where $\dim V_n = 2n + 1$. The Garland--Lepowsky
concentration theorem gives $\dim H^n = 2n + 1$
\textup{(}Remark~\textup{\ref{rem:garland-lepowsky-sl2}}),
exec
/bin/zsh -lc 'rg -n "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|We now turn to|one might expect|it can be shown|it seems reasonable|---|—|`|'"\\*\\*|_[A-Za-z]|TODO|FIXME\" chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1561,2080p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: unmatched "
 succeeded in 51ms:
This is a genuine feature:
$\kappa$ is the modular characteristic of the
\emph{full} chiral algebra (tracking both
the double-pole and simple-pole channels),
while $c/2$ is the modular characteristic
of the Virasoro subalgebra alone (which
sees only the Sugawara stress tensor).
\item \emph{Anti-symmetry.}
$\kappa(\widehat{\fg}_{-k-2h^\vee})
= (-k - 2h^\vee + h^\vee)\dim(\fg)/(2h^\vee)
= -(k + h^\vee)\dim(\fg)/(2h^\vee) = -\kappa$,
confirming $\kappa + \kappa' = 0$.
\end{enumerate}
\end{computation}

\begin{proposition}[Feigin--Frenkel shear on channel
pair; \ClaimStatusProvedHere]
\label{prop:ff-channel-shear}
\index{Feigin--Frenkel duality!shear matrix}
\index{channel decomposition!Feigin--Frenkel transformation}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4800,5200p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{cyclic slice!from affine OPE}

\begin{proposition}[Affine cyclic slice data;
\ClaimStatusProvedHere]\label{prop:affine-cyclic-slice-data}
The affine current algebra $\widehat{\mathfrak{g}}_k$ has OPE
\begin{equation}\label{eq:affine-ope-full}
J^a(z)\,J^b(w)
\;\sim\;
\frac{k\,\kappa^{ab}}{(z-w)^2}
\;+\;
\frac{f^{ab}{}_{c}\,J^c(w)}{z-w}\,.
\end{equation}
On the strict current-level sector
$V_{\mathrm{aff}} = \mathfrak{g}[1] \oplus \mathbb{C}\,K[1]$
\textup{(Definition~\textup{\ref{def:affine-strict-current-sector}})},
the shadow calculus data
\textup{(Setup~\textup{\ref{setup:nms-cyclic-slice}})} are
determined by the two poles of~\eqref{eq:affine-ope-full}:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The \emph{Hessian} \textup{(from the double pole)}:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5200,5600p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{Swiss-cheese!critical level deformation}
At the critical level $k = -h^\vee$ for $\fg$ simple of rank~$r$
with exponents $m_1 \le \cdots \le m_r$, the SC deformation complex
governing the chiral Swiss-cheese pair
$\bigl(\ChirHoch^*(\widehat{\fg}_{-h^\vee}),\, \widehat{\fg}_{-h^\vee}\bigr)$
exhibits the following structure:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Degree-$0$ jump)}\quad
 $\ChirHoch^0(\widehat{\fg}_{-h^\vee})
 = \mathfrak{z}(\widehat{\fg}_{-h^\vee})
 \cong \mathrm{Fun}(\mathrm{Op}_{\fg^\vee}(D))
 \cong \bC[\Theta_1, \ldots, \Theta_r]$,
 jumping from $\bC$ at generic level to
 the infinite-dimensional Feigin--Frenkel center.
\item \textup{(Degree-$1$ jump)}\quad
 $\ChirHoch^1(\widehat{\fg}_{-h^\vee})$ also jumps: at generic level it equals~$\fg$
 \textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km}}\textup{)};
 at critical level the Beilinson--Drinfeld comparison
 \textup{(}Theorem~\textup{\ref{thm:affine-periodicity-critical}}\textup{)}
 gives the full odd-degree Gelfand--Fuchs component
thinking
**Debugging command issues**

It looks like the rg command didn't run correctly because of a backtick problem. I think I need to rerun it using single quotes to escape properly. I'll also focus on running patterns separately. I still need to continue reading beyond line 2080, as there are many lines to go through. Also, I should just wait on the explorer — it may not be ready for polling yet.
collab wait(call_Pi3ChQUCZ4VyVzLbxiBts6No)
  receivers: 019d83fe-2fa8-7830-98e8-f27b6be2239d
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5600,6000p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
We combine the simply-laced data of
Proposition~\ref{prop:exceptional-shadow-invariants} with the
non-simply-laced data of Proposition~\ref{prop:nsl-shadow-tower}
into a single table covering all five exceptional types.

\begin{proposition}[Complete exceptional shadow data; \ClaimStatusProvedHere]%
\label{prop:complete-exceptional-shadow}
\index{exceptional Lie algebra!complete shadow data}
For every exceptional simple Lie algebra
$\fg \in \{G_2, F_4, E_6, E_7, E_8\}$ at non-critical affine
level $k \neq -h^\vee$, the shadow obstruction tower data is as follows.
\begin{center}
\renewcommand{\arraystretch}{1.4}
\begin{tabular}{lccccccc}
\toprule
$\fg$ & $\dim$ & $r$ & $h$ & $h^\vee$ & $r^\vee$
 & $\kappa(\widehat{\fg}_k)$ & Class \\
\midrule
$G_2$ & $14$ & $2$ & $6$ & $4$ & $3$
 & $7(k+4)/4$ & L \\
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6000,6400p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 \;=\;
 \frac{(-k - 2h + h)\,d}{2h}
 \;=\;
 \frac{(-k - h)\,d}{2h}.
\]
Summing:
\[
 \kappa(\widehat{V}_k(\fg)) + \kappa(\widehat{V}_{k'}(\fg))
 \;=\;
 \frac{(k + h)\,d}{2h}
 \;+\;
 \frac{(-k - h)\,d}{2h}
 \;=\; 0.
\]

For the Verlinde swap: at genus~$1$,
$\dim\mathcal{V}_1(\mathfrak{sl}_N, k) = \binom{N+k-1}{N-1}$.
The identity $\binom{N+k-1}{N-1} = \binom{N+k-1}{k-1}$ is equivalent
to $\binom{n}{a} = \binom{n}{n-a}$ with $n = N+k-1$, $a = N-1$,
which gives $\dim\mathcal{V}_1(\mathfrak{sl}_N, k)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6400,6800p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "notably|crucially|importantly|significantly|essentially" chapters/examples/kac_moody.tex' in /Users/raeez/chiral-bar-cobarwait(call_Pi3ChQUCZ4VyVzLbxiBts6No) timed out:
 succeeded in 51ms:
873:(Table~\ref{tab:bar-dimensions}) are significantly smaller
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '---' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: unrecognized flag ---
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\-{3}' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '"'`'"' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
193:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \widehat{\mathfrak{g}}_k)$
404:where $\kappa^{ab} = \kappa_{\mathfrak{g}}(T^a, T^b)$ is the normalized invariant bilinear form on $\mathfrak{g}$ (normalized so that long roots have squared length $2$), ${f^{ab}}_c$ are the structure constants, and $\sim$ means ``has singular part.'' In an orthonormal basis with $\kappa^{ab} = \delta^{ab}$, this reduces to the familiar form $k\delta^{ab}/(z-w)^2$.
945:\item The ``critical-first'' spectral sequence with
950:\item The ``curvature-first'' spectral sequence with
3301:``dimension'' is replaced by the rank of the space of
codex
The next pass is moving through the middle of the file, where the risk shifts from obvious slop to drift: repeated theorem restatements, weak transitions, and notation surfaces that look locally fine but diverge from the chapter’s own opening conventions.
exec
/bin/zsh -lc "rg -n '---|—|\\*\\*|"'`'"' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2081,2600p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2601,3120p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|we now turn to|one might expect|it can be shown|it seems reasonable|todo|fixme' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: unrecognized flag ---|—|\*\*|`
 succeeded in 53ms:
while the full universal class is Lie/tree with
$\mathfrak{C} \ne 0$, $o_4 = 0$.
\end{remark}

\begin{computation}[Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$; \ClaimStatusProvedHere]
\label{comp:sl2-collision-residue-kz}
\index{collision residue!sl2 explicit@$\mathfrak{sl}_2$ explicit}
\index{r-matrix@$r$-matrix!from collision residue}
\index{KZ connection!from collision residue}
\index{Arnold relation!CYBE verification}
We compute the genus-$0$, degree-$2$ collision residue
$\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
for $\cA = \widehat{\mathfrak{sl}}_{2,k}$ and verify that it
yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
governing the Knizhnik--Zamolodchikov equation.

\emph{Step~1: OPE data.}
Let $\{e, h, f\}$ be the standard basis of $\mathfrak{sl}_2$
with Killing form normalised so that $\kappa(e,f) = 1$,
$\kappa(h,h) = 2$, and $\kappa(e,e) = \kappa(f,f) = \kappa(e,h)
 succeeded in 53ms:
\index{Verlinde formula!bar complex derivation}
By Proposition~\ref{prop:conformal-blocks-bar}, the space of
conformal blocks for $\widehat{\mathfrak{sl}}_2$ at level~$k$
with insertions $L(j_1\Lambda_1), \ldots, L(j_r\Lambda_1)$
at points $x_1, \ldots, x_r \in \mathbb{P}^1$ is:
\[
\dim \mathbb{V}\bigl(
\widehat{\mathfrak{sl}}_{2,k};\,
L(j_1\Lambda_1), \ldots, L(j_r\Lambda_1);\, \mathbb{P}^1
\bigr)
= N_{j_1 \cdots j_r}^{(k)}
\]
where $N_{j_1 \cdots j_r}^{(k)}$ is the iterated fusion
coefficient, computed by the Verlinde formula:
\begin{equation}\label{eq:verlinde-sl2}
N_{j_1 \cdots j_r}^{(k)}
= \sum_{m=0}^{k}
\prod_{i=1}^{r}
\frac{S_{j_i,m}}{S_{0,m}},
\qquad
 exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'TODO|FIXME' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '  ' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:




thinking
**Identifying writing improvements with line references**

I'm narrowing down concrete cosmetic fixes like replacing the AI slur “significantly” at line 873 and suggesting clearer chapter signposting by citing exact line numbers. I’m also flagging passive voice or unclear transitions in key paragraphs, highlighting notation consistency issues, and aiming to provide precise fix texts referencing line locations. Let’s explore these actionable editorial notes with clear start lines and suggested rephrasing.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/kac_moody.tex | sed -n '840,880p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   840	\end{computation}
   841	
   842	\begin{lemma}[Bar chain groups are level-independent; \ClaimStatusProvedHere]%
   843	\label{lem:bar-dims-level-independent}
   844	\index{bar complex!level-independence}
   845	The dimensions $\dim(\bar{B}^n(\widehat{\mathfrak{g}}_k))$ depend on
   846	$\mathfrak{g}$ but are \emph{independent of the level~$k$}. This is
   847	immediate from the construction: the bar chain groups
   848	\[
   849	\bar{B}^n(\widehat{\mathfrak{g}}_k)
   850	= \Gamma\!\bigl(\overline{C}_{n+1}(X),\;
   851	 \mathfrak{g}^{\boxtimes(n+1)} \otimes \Omega^n_{\log}\bigr)
   852	\]
   853	involve only the Lie algebra $\mathfrak{g}$ (via its generators
   854	$J^a$, $a = 1, \ldots, \dim\mathfrak{g}$) and the geometry of the
   855	configuration space $\overline{C}_{n+1}(X)$. Neither ingredient
   856	depends on~$k$. In particular, the chain-group dimension
   857	is $\dim(\bar{B}^n) = (\dim\mathfrak{g})^n \cdot (n-1)!$,
   858	the product of the generator factor $(\dim\mathfrak{g})^n$
   859	(one copy of $\mathfrak{g}$ per configuration point) and


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'Omega["'^'"\\n]*\\/z' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
765:same object in the equivalent form $k\Omega_{\mathrm{tr}}/z$, where

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/kac_moody.tex | sed -n '740,780p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   740	The $r$-matrix $r(z) = \Omega/((k{+}h^\vee)\,z)$ satisfies the classical
   741	Yang--Baxter equation, which reduces via partial fractions to
   742	the infinitesimal braid relation
   743	$[\Omega_{ij}, \Omega_{ik} + \Omega_{jk}] = 0$
   744	for all distinct triples $(i,j,k)$
   745	(Proposition~\ref{prop:cybe-from-mc}).
   746	
   747	\emph{Convention.}
   748	This chapter uses the \emph{KZ normalization} throughout:
   749	\[
   750	r^{\mathrm{KZ}}(z) = \frac{\Omega}{(k+h^\vee)\,z},
   751	\qquad
   752	\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b,
   753	\]
   754	where $\kappa^{ab}$ is the inverse Killing form and the
   755	denominator $k + h^\vee$ is the Sugawara shift. This is the
   756	normalization in which the KZ connection takes the standard form
   757	$\nabla^{\mathrm{KZ}} = d - \sum_{i < j} r(z_{ij})\, dz_{ij}$
   758	(Computation~\ref{comp:sl2-collision-residue-kz}).
   759	At $k = 0$ the non-abelian Lie bracket persists, so the collision

thinking
**Searching for unused labels**

I need to find unused labels in the file. But those "unused labels" might be scattered throughout the file or the repository, right? I could search the whole repo for label references, looking out for duplicates or labels that are never referenced. That seems like a lot. However, the user only asked for an audit of the file regarding dead code, specifically unused labels. I should focus on searching for labels defined in the file that aren't referenced anywhere. But I also need to consider the repo due to the user's request.
thinking
**Considering potential findings**

I’m thinking I should only produce findings if I'm confident, especially regarding actual issues. There could be many issues, and I need exact line numbers. I’m planning to use `nl -ba` to help, and while I don’t need to cover every potential issue across 6000 lines, thoroughness is key. My focus will be on collecting likely issues from the first 3000 lines, like the duplicate labels which may cause redundancy. I’ll need to think about the best way to fix that.
thinking
**Evaluating audit findings**

Since the audit focuses on diagnosis and fixing, I could suggest deleting one label and rewriting cross-references to the canonical label. However, the user is looking for an exact fix, not just a diagnosis. If I don't apply edits, the exact fix will be a concrete replacement. The user asked for an audit, not a patch, so I’ll only output findings. There are many instances of bare \(\kappa\) without qualifiers, which may need to be assessed for consistency.
thinking
**Assessing bare \(\kappa\) usage**

The task asks if there are any bare \(\kappa\) without family, and indeed, there are many instances. I might need to report those where the scope is ambiguous across multiple families in the same sentence or section, but there may be too many occurrences to list them all — potentially dozens. A potential general fix could involve defining \(\kappa_{\mathrm{KM}}(\widehat{\fg}_k)\) at first introduction or adding family notation. However, the user wants every finding with exact line numbers, so it seems I may need to treat each occurrence as a finding, especially if they're inconsistent.
thinking
**Considering bare kappa issues**

I'm thinking about how to handle cases of bare \kappa without family, level k, or macro definitions. It might be a good idea to look for all occurrences, possibly hundreds, which could be daunting. The user wants a complete audit, so listing each finding seems necessary, even if it might be extensive. I could use scripting with regex patterns to find them efficiently, but I'm concerned about the volume of findings and how to present them. I'll need to categorize and structure the output appropriately.
thinking
**Auditing user requests**

The user explicitly wants every finding, which means I might end up with more than 70 lines. But if it's exhaustive, I think that's okay. I could consider focusing mainly on cosmetic and aesthetic issues, rather than every single notation, but consistency matters too. I'll need to script an audit to help generate line numbers for relevant patterns, potentially using shell commands like `rg -n` or `grep -nP`. It’ll be important to run safe commands as I look through the file.
codex
I’ve hit the heavy theorem core of the chapter. The main risk here is no longer wording polish alone; it’s rhetorical overclaiming wrapped around repeated restatements of the same level-shift package, so I’m now isolating exact duplicate surfaces and notation drift rather than just banned tokens.
exec
/bin/zsh -lc "sed -n '3121,3640p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3641,4160p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i -- 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|delve|leverage|tapestry|cornerstone|it is worth noting|we now turn to|one might expect|it can be shown|it seems reasonable' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '---|—|\\*\\*|"'`|TODO|FIXME'"' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$E_1$ page & $\bigoplus_{w \in \mathcal{W}} \mathcal{M}(w \cdot \lambda)$
& same \\
$d_1$ & $0$ (Verma modules irreducible) & $\neq 0$ (singular vectors) \\
$E_2$ page & $= E_1$ (full $\mathcal{W}$ sum) &
$\mathcal{W}_{\mathrm{adm}}$ survivors \\
Result & Weyl--Kac & Kac--Wakimoto \\
\bottomrule
\end{tabular}
\end{center}
On the manuscript's bar surface, admissible-level singular-vector
cancellation leaves a finite admissible Weyl packet; for the fully
worked $\widehat{\mathfrak{sl}}_2$ example at $k=-1/2$ this is exactly
the two-term formula of Theorem~\ref{thm:kw-bar-spectral}. In general
rank, the resulting finite-sum character formula is the external
Kac--Wakimoto theorem recorded below.
\end{remark}

\begin{theorem}[Kac--Wakimoto character formula in general rank;
\ClaimStatusProvedElsewhere]
\label{thm:kw-bar-general-rank}
 succeeded in 52ms:
$d_0 = Q_{\mathrm{DS}}$, giving $E_1^{p,q} =
H^q_{\mathrm{DS}}(\bar{B}_p(M))$. The $d_1$ differential is
the induced bar differential on DS cohomology.

For the degeneration: by hypothesis,
$H^i_{\mathrm{DS}}(M) = 0$ for $i \neq 0$. Since each
$\bar{B}_p(M)$ is built from tensor products within the
admissible category $\mathrm{KL}_k$ (which is closed under
tensor products by Arakawa~\cite{Arakawa17}),
the DS vanishing $H^i_{\mathrm{DS}} = 0$ for $i > 0$ extends
from $M$ to each $\bar{B}_p(M)$. Thus $E_1^{p,q} = 0$ for
$q > 0$, and the $d_1$ differential on the surviving row
$E_1^{p,0} = H^0_{\mathrm{DS}}(\bar{B}_p(M)) = \bar{B}_{W,p}(M^W)$
is the $\mathcal{W}^k$-bar differential, giving
$E_2^{p,0} = H^p(\bar{B}_W(M^W))$.
\end{proof}

\section{\texorpdfstring{Genus-1 pipeline for $\widehat{\mathfrak{sl}}_2$}{Genus-1 pipeline for sl-2}}
\label{sec:sl2-genus-one-pipeline}
\index{genus-1 pipeline!Kac--Moody}
 exited 1 in 52ms:

 succeeded in 51ms:
193:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \widehat{\mathfrak{g}}_k)$
404:where $\kappa^{ab} = \kappa_{\mathfrak{g}}(T^a, T^b)$ is the normalized invariant bilinear form on $\mathfrak{g}$ (normalized so that long roots have squared length $2$), ${f^{ab}}_c$ are the structure constants, and $\sim$ means ``has singular part.'' In an orthonormal basis with $\kappa^{ab} = \delta^{ab}$, this reduces to the familiar form $k\delta^{ab}/(z-w)^2$.
945:\item The ``critical-first'' spectral sequence with
950:\item The ``curvature-first'' spectral sequence with
3301:``dimension'' is replaced by the rank of the space of

thinking
**Identifying textual and formatting issues**

I'm gathering a shortlist of real textual concerns like abrupt section transitions, some awkward phrasing such as “significantly” at line 873, unclear roadmap in the introduction, possible markup issues from unmatched braces around line 186-190, and opportunities for clearer signposting—aiming to deliver a focused set of actionable feedback points on the document's flow and style.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '150,210p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\textup\\{\\(\\};' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
199:\textup{(}; all currents $J^a$ have conformal weight~$1$, so
codex
There are already concrete defects, not just style drift. One of them is an actual malformed token in math mode near line 193, and the middle sections keep restating the same admissible-level package with different rhetoric instead of forcing the next section mathematically.
exec
/bin/zsh -lc "sed -n '4161,4680p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4681,5200p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '\\\\kappa(?"'![_''^{])'"' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '(?<"'![A-Za-z])'"\\\\Omega/(?"'!'"\\()|\\\\Omega/z|r\\(z\\) = \\\\Omega/' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
5:degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
12:cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
62: $\kappa(\widehat{\fg}_k)
64: $\kappa + \kappa' = 0$ (affine KM)
85:$\kappa(\widehat{\fg}_k)$ &
88: $\kappa(x,[y,z])$ (Lie bracket) \\
92: (sharing $\kappa$ with $\widehat{\fg}_{-k-2h^\vee}$) \\
93:Complementarity & $\kappa + \kappa' = 0$ (affine KM) \\
133:$\kappa = \dim(\mathfrak{g}) \cdot (k + h^\vee)/(2h^\vee)$
137:$\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$. The strict model $\Convstr$ carries a nonzero cubic shadow at degree~$3$
169:minimal package $\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$
171:$\kappa = \dim(\mathfrak{g})\cdot(k+h^\vee)/(2h^\vee)$, while
177:At critical level $k = -h^\vee$, $\kappa = 0$ and the bar complex
200:the scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds
235:At level~$k$ with $\kappa=3(k+2)/4$, the genus-$1$ deformation
242:\kappa
265:(iv)~genus tower with $\kappa = \dim(\mathfrak{g})\cdot(k + h^\vee)/(2h^\vee)$, Lie/tree shadow
511:This is proved as Theorem~\ref{thm:universal-kac-moody-koszul} below: the bar complex of $\widehat{\mathfrak{g}}_k$ is computed via residues on FM compactifications (Step~1), the curvature $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is identified from the double-pole OPE (Step~2), the cobar OPE recovers the level $-k - 2h^\vee$ structure constants (Step~3), and the result is characterized by functorial uniqueness (Step~4).
521:m_0 = \frac{k+h^\vee}{2h^\vee} \cdot \kappa, \qquad m_1^2(a) = [m_0, a] = m_2(m_0, a) - m_2(a, m_0)
523:where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
 succeeded in 52ms:
$L$-function of the adjoint representation) and $d_{\mathrm{alg}} = 0$,
giving total depth $d = 3$; this is the Lie class $L$.
\end{remark}

\subsection{The affine primitive kernel}
\label{subsec:affine-primitive-kernel}
\index{primitive kernel!affine Kac--Moody}

\begin{proposition}[Affine primitive kernel;
\ClaimStatusProvedHere]
\label{prop:affine-primitive-kernel}
The primitive logarithmic modular kernel
\textup{(}Definition~\textup{\ref{def:primitive-log-modular-kernel})}
of $\widehat{\mathfrak{g}}_k$ at non-critical level is
\begin{equation}\label{eq:affine-primitive-kernel}
\mathfrak{K}_{\mathrm{aff}}
\;=\;
K_{0,2}^{\mathrm{aff}} + K_{0,3}^{\mathrm{aff}} + K_{1,1}^{\mathrm{aff}},
\end{equation}
where:
 succeeded in 52ms:
\end{remark}

\begin{conjecture}[KL-I: periodic CDG structure;
\ClaimStatusConjectured]\label{conj:kl-periodic-cdg}
At admissible level $k = -h^\vee + p/q$ ($p, q$ coprime positive integers,
$q \geq h^\vee$), the bar complex $\barB(\widehat{\fg}_k)$ acquires a
periodic CDG structure with period dividing $2q$:
\[
\barB^{n+2q}(\widehat{\fg}_k) \;\cong\; \barB^n(\widehat{\fg}_k)
\quad \text{for all } n \gg 0,
\]
where $q = e^{\pi i/(k+h^\vee)} = e^{\pi i q/p}$.
(Contributing to Conjecture~\ref{conj:master-dk-kl}.)
\end{conjecture}

\begin{conjecture}[KL-II: coderived lift and semisimplified target;
\ClaimStatusConjectured]\label{conj:kl-coderived}
Assuming Conjecture~\textup{\ref{conj:kl-periodic-cdg}}, the
coderived category of the periodic bar complex identifies with the
quantum group side in a form whose H-level shadow is the
 succeeded in 53ms:
90:$r$-matrix $r(z)$ & $\Omega/\bigl((k{+}h^\vee)\,z\bigr)$ (Casimir, KZ normalisation, Comp.~\ref{comp:sl2-collision-residue-kz}) \\
740:The $r$-matrix $r(z) = \Omega/((k{+}h^\vee)\,z)$ satisfies the classical
2076:$r(z) = \Omega/((k{+}h^\vee)\,z)$ (the Casimir $r$-matrix, governing the KZ equation),
2094:yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
2357:$r$-matrix $r(z) = \Omega/(k+2)\,z$ with simple pole and no
3416:$r(z) = \Omega/\bigl((k{+}h^\vee)\,z\bigr)$ is well-defined and the
5490: $r(z) = \Omega/\bigl((k{+}h^\vee)\,z\bigr)$ with a simple pole at
5636:$r$-matrix $r(z) = \Omega/\bigl((k{+}h^\vee)\,z\bigr)$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/kac_moody.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     1	\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
     2	\label{chap:kac-moody}
     3	
     4	The Heisenberg algebra is abelian: its shadow tower terminates at
     5	degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
     6	The first nonabelian chiral algebra is
     7	$\widehat{\mathfrak{g}}_k$, and the question that
     8	governs this chapter is whether the Lie bracket destroys the
     9	finiteness of the obstruction tower or preserves it.
    10	%
    11	It preserves it. The Lie bracket of~$\fg$ appears as the
    12	cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
    13	degree~$3$; the Jacobi identity forces the quartic shadow to vanish;
    14	the tower terminates (class~$L$, $r_{\max} = 3$). Gauge symmetry
    15	introduces noncommutativity but not infinite obstruction complexity:
    16	the structure constants of~$\fg$ produce exactly one new shadow
    17	beyond the Gaussian, and the Jacobi identity is the mechanism that
    18	kills the rest. This is the content of the assertion that gauge
    19	theory is simpler than gravity; for the Virasoro algebra
    20	(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the


thinking
**Summarizing key document fixes**

I'll note three main issues in chapters/examples/kac_moody.tex: adding a roadmap sentence after line 34 to improve section orientation, correcting a stray `\textup{(};` bracket near line 199 with suggested fix text, and replacing “significantly” at line 873 with “noticeably” along with a smoother phrasing example. This summary will include clear bullet points referencing file paths, line numbers, and proposed corrections.

codex
- **Opening roadmap** – `chapters/examples/kac_moody.tex:4-35`: the first paragraphs jump straight into the obstruction story without telling the reader what comes next. Please insert a brief roadmap after line 34, e.g. “We start by exhibiting the modular Koszul triple and the five-theorem table, then spell out the affine bar complex, move through the concrete \(\widehat{\mathfrak{sl}}_2\) and \(\widehat{\mathfrak{sl}}_3\) computations, and finally explore the genus‑one and exceptional-type consequences.” That keeps the opening narrative-friendly and better signposted.

- **Broken LaTeX token** – `chapters/examples/kac_moody.tex:199`: the remark currently reads `\textup{(}; all currents…` which leaves an orphaned `\textup{(}` and produces a stray “(”. Replace that fragment with a well-formed clause, e.g. `\textup{(}all currents \(J^a\) have conformal weight~1, so…\textup{)};` or simply drop the `\textup{(}`/`\textup{)}` pair and keep “…the strict dg Lie model is the full \(L_\infty\)-structure at every genus; all currents …”.

- **AI-slop wording** – `chapters/examples/kac_moody.tex:873`: the phrase “are significantly smaller” in the lemma text is flagged as banned vocabulary. Reword to something more neutral, for example “are noticeably smaller than the chain-group dimensions,” or “grow much more slowly than the chain groups,” to keep the prose compliant.
thinking
**Deciding on bare kappa definitions**

The output for bare kappa search is quite large, so I need to determine how to approach this. While some bare kappa elements are inconsistent, many actually use the function `\kappa(\widehat{\fg}_k)`. The user is interested in whether there are any bare kappa instances without family. I believe it might be best to report the first problematic definitions where bare kappa is introduced generically and ensure consistent use within the local scope. However, addressing every instance might be overkill.
thinking
**Clustering notation references**

Since there are a lot of references, I could consider reporting clusters that reference the same introduced notation. However, the user specifically requested the exact line numbers. Maybe starting with the line number for each cluster would be sufficient. I realize that I need to continue working through to the final chunk, lines 5201-6074. I also think I should search for things like em dashes within those lines while I work on the rest.
codex
The file is still generating repeated notation drift: the same chapter-level shorthand `\kappa` gets reintroduced as if it were local each time, which means the audit has to treat those as separate defects, not a single stylistic preference. I’m finishing the last quarter now and then I’ll collapse the results into verified line-specific fixes only.
exec
/bin/zsh -lc "sed -n '5201,5720p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
At the critical level $k = -h^\vee$ for $\fg$ simple of rank~$r$
with exponents $m_1 \le \cdots \le m_r$, the SC deformation complex
governing the chiral Swiss-cheese pair
$\bigl(\ChirHoch^*(\widehat{\fg}_{-h^\vee}),\, \widehat{\fg}_{-h^\vee}\bigr)$
exhibits the following structure:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Degree-$0$ jump)}\quad
 $\ChirHoch^0(\widehat{\fg}_{-h^\vee})
 = \mathfrak{z}(\widehat{\fg}_{-h^\vee})
 \cong \mathrm{Fun}(\mathrm{Op}_{\fg^\vee}(D))
 \cong \bC[\Theta_1, \ldots, \Theta_r]$,
 jumping from $\bC$ at generic level to
 the infinite-dimensional Feigin--Frenkel center.
\item \textup{(Degree-$1$ jump)}\quad
 $\ChirHoch^1(\widehat{\fg}_{-h^\vee})$ also jumps: at generic level it equals~$\fg$
 \textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km}}\textup{)};
 at critical level the Beilinson--Drinfeld comparison
 \textup{(}Theorem~\textup{\ref{thm:affine-periodicity-critical}}\textup{)}
 gives the full odd-degree Gelfand--Fuchs component
 $\bigoplus_{i=1}^{r} P_i \otimes \bC[\Theta_1, \ldots, \Theta_r]$,
exec
/bin/zsh -lc "rg -n -- '%.*TODO|%.*FIXME|"'^%.*$'"' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5721,6074p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- 'We now turn to|we now turn to|In this chapter we|in this chapter we|It can be shown|it can be shown|one might expect|it seems reasonable' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
10:%
770:%: r(z) lives on C_2(X), not over a point. The formal disk
771:% carries completion data; the homotopy retract A^1 -> pt is additional
772:% data, not an identity.
5780:%% ================================================================
 succeeded in 52ms:
anomaly ratio formula (Theorem~D and
Chapter~\ref{chap:w-algebras}).
\end{proof}

\begin{remark}[The Deligne--Cvitanovi\'c exceptional series]%
\label{rem:deligne-cvitanovic}
\index{Deligne--Cvitanovic series@Deligne--Cvitanovi\'c series!shadow data}
The exceptional Lie algebras fit into a parametric family
along the chain $A_1 \subset G_2 \subset F_4 \subset E_6
\subset E_7 \subset E_8$, parametrized by $h^\vee$
(Deligne \cite{Deligne96}, Cvitanovi\'c \cite{Cvitanovic08}).
At level $k = 1$, the $\kappa$ values along this chain are:
\[
\kappa(\widehat{\fg}_1)
\;=\; \frac{\dim(\fg)(1 + h^\vee)}{2h^\vee}
\;=\; \frac{9}{4},\;\; \frac{35}{4},\;\; \frac{260}{9},\;\; \frac{169}{4},\;\; \frac{2527}{36},\;\; \frac{1922}{15}
\]
The progression tracks the growth of $\dim(\fg)$ with $h^\vee$;
the shadow obstruction tower structure (class~L, depth~$3$ uniformly) is
constant along the entire chain, reflecting the universal role of
 exited 1 in 52ms:


thinking
**Conducting precise searches**

I'm aiming to look for any duplicate labels on the same line. It's important to be thorough here, so I want to run precise searches to ensure I don't miss anything. I think that checking for duplicates can help clarify things and prevent confusion later. Let's see what I find and hopefully resolve those duplicates effectively! This could streamline everything moving forward.
codex
The last quarter is cleaner on banned tokens, but it exposes a different problem: some sections are effectively documentation drift, with long theorematic restatements that add no new mathematics and a few genuinely malformed or ambiguous LaTeX tokens hiding inside them.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '180,205p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '\\\\begin\\{|\\\\end\\{' chapters/examples/kac_moody.tex | tail -n 40" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n '  ' chapters/examples/kac_moody.tex | head -n 200" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   180	
   181	\begin{remark}[Three-pillar interpretation: Kac--Moody]
   182	\label{rem:km-three-pillar}
   183	\index{Kac--Moody!three-pillar interpretation}
   184	In the three-pillar architecture
   185	(\S\ref{sec:concordance-three-pillars}):
   186	(i)~the \v{C}ech complex of affine Kac--Moody is a \emph{non-strict}
   187	homotopy chiral algebra with $F_3 \neq 0$
   188	(Example~\ref{ex:cech-hca-sl2}); the nontrivial $F_3$ is the Jacobiator
   189	homotopy witnessing the failure of the Jacobi identity at the chain level.
   190	This is the Lie/tree secondary Borcherds archetype:
   191	$j'_{(p,q,r)} \neq 0$ at degree~$3$ but all higher degrees vanish;
   192	(ii)~the convolution $sL_\infty$-algebra
   193	$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \widehat{\mathfrak{g}}_k)$
   194	is \emph{strictly formal}
   195	(Theorem~\ref{thm:km-strictification}): all transferred higher brackets
   196	vanish identically ($\ell_k^{\mathrm{tr}} = 0$ for $k \geq 3$),
   197	and the strict dg~Lie model \emph{is} the full $L_\infty$-structure
   198	at every genus
   199	\textup{(}; all currents $J^a$ have conformal weight~$1$, so
 succeeded in 52ms:
1:\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
2:\label{chap:kac-moody}
41:$k \neq -h^\vee$.}\label{tab:km-five-theorems}
78:Kac--Moody.}\label{tab:km-shadow-archetype}
107:\begin{equation}\label{eq:km-triple}
164:\begin{remark}[Shadow obstruction tower for Kac--Moody]\label{rem:km-master-mc}
182:\label{rem:km-three-pillar}
208:\label{rem:km-genus-two-shells}
232:\label{comp:km-genus1-hessian}
257:\label{rem:km-four-level}
270:\label{sec:km-bar-complex}
289:\begin{align}\label{eq:kac-moody-koszul-basic}
317:\begin{theorem}[Feigin--Frenkel center at critical level \cite{Feigin-Frenkel}; \ClaimStatusProvedElsewhere]\label{thm:critical-level-structure}
360:\begin{definition}[Loop algebra]\label{def:loop-algebra}
371:\begin{definition}[Affine Kac--Moody Lie algebra]\label{def:affine-kac-moody}
401:\begin{equation}\label{eq:affine-kac-moody-ope}
407:\begin{definition}[Chiral algebra perspective]\label{def:chiral-kac-moody}
415:\begin{theorem}[Equivalence of perspectives \cite{FBZ04, BD04}; \ClaimStatusProvedElsewhere]\label{thm:vertex-chiral-equivalence}
463:\begin{theorem}[Geometric OPE formula; \ClaimStatusProvedHere]\label{thm:geometric-ope-kac-moody}
491:\label{sec:km-koszul-abstract}
 succeeded in 50ms:
5811:\begin{proposition}[The holomorphic-topological Chern--Simons action;
5817:\begin{equation}\label{eq:affine-cs-action}
5828:\end{equation}
5833:\end{proposition}
5835:\begin{proof}
5841:\end{proof}
5843:\begin{remark}[Gauge transformations]
5848:\begin{align*}
5860:\end{align*}
5866:\end{remark}
5868:\begin{remark}[Bar complex as BRST complex]
5885:\end{remark}
5887:\begin{remark}[Ghost dictionary]
5893:\begin{center}
5895:\begin{tabular}{lll}
5905:\end{tabular}
5906:\end{center}
5915:\end{remark}
5927:\begin{proposition}[Level-rank duality for boundary VOAs;
5937:\begin{equation}\label{eq:level-rank-voa-iso}
 succeeded in 50ms:

codex
I’m now verifying the suspicious tokens against the rest of the repo rather than trusting local intuition. That matters here because some of these defects look cosmetic but are actually broken notation aliases or malformed labels that only show up when compared across nearby chapters.
exec
/bin/zsh -lc "rg -n -- '\\\\cC\\"'^'"\\{\\\\textup\\{"'!`'"\\}\\}|\\\\cC\\"'^'"\\{["'^}]*![''^}]*'"\\}' -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- 'remark\\[Evidence\\]|\\[Evidence\\]' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '\\\\verb\\|' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: -g: No such file or directory (os error 2)
rg: *.tex: No such file or directory (os error 2)
exec
/bin/zsh -lc "rg -n -- 'rem:category-O-affine|rem:bgg-kl-bridge|chap:kac-moody-koszul|chap:kac-moody|tab:exceptional-shadow-data'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
3451:\verb|compute/tests/test_admissible_koszul_rank2_engine.py|
 succeeded in 53ms:
1077:\begin{remark}[Evidence]
 succeeded in 51ms:
wave2_audit_20260413_001942/S10_examples_to_wn.md:655:    41	Chapter~\ref{chap:kac-moody-koszul}.
wave2_audit_20260413_001942/S09_examples_mutual.md:237:chapters/examples/kac_moody.tex:1:\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
wave2_audit_20260413_001942/S09_examples_mutual.md:418:     1	\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
wave2_audit_20260413_001942/S09_examples_mutual.md:419:     2	\label{chap:kac-moody}
metadata/label_index.json:462:  "chap:kac-moody": {
metadata/label_index.json:466:  "chap:kac-moody-koszul": {
metadata/label_index.json:29382:  "rem:bgg-kl-bridge": {
metadata/label_index.json:29726:  "rem:category-O-affine": {
metadata/label_index.json:44826:  "tab:exceptional-shadow-data": {
metadata/claims.jsonl:1292:{"label": "prop:exceptional-shadow-invariants", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/examples/kac_moody.tex", "line": 1589, "title": "Exceptional shadow invariants", "labels_in_block": ["prop:exceptional-shadow-invariants", "tab:exceptional-shadow-data"], "refs_in_block": ["prop:ff-channel-shear", "thm:shadow-archetype-classification"]}
wave2_audit_20260413_001942/S06_intro_to_body.md:737:  2392	\item \emph{Kac--Moody} (Ch.~\ref{chap:kac-moody}).
wave2_audit_20260413_001942/S04_shadow_to_examples.md:349:   228	% (Chapter~\ref{chap:kac-moody-koszul}), this reads
appendices/koszul_reference.tex:65:\emph{theorem} (proved in Chapter~\ref{chap:kac-moody-koszul}), not a
standalone/introduction_full_survey.tex:4712:(Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
standalone/introduction_full_survey.tex:4962:Kac--Moody (Ch.~\ref{chap:kac-moody}) &
audit_campaign_20260412_231034/XV15_E1_first_xvol.md:490:\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
audit_campaign_20260412_231034/XV15_E1_first_xvol.md:491:\label{chap:kac-moody}
audit_campaign_20260412_231034/F19_arnold_KZ.md:468:228-% (Chapter~\ref{chap:kac-moody-koszul}), this reads
audit_campaign_20260412_231034/F18_complementarity.md:936:   632	Chapter~\ref{chap:kac-moody}.
audit_campaign_20260412_231034/F05_r_KM.md:398:% (Chapter~\ref{chap:kac-moody-koszul}), this reads
exec
/bin/zsh -lc "rg -n --glob '*.tex' -- '\\\\cC\\"'^'"\\{\\\\textup\\{"'!`'"\\}\\}|\\\\cC\\"'^'"\\{["'^}]*![''^}]*'"\\}'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/lattice_foundations.tex:51:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, V_\Lambda)$ is
chapters/examples/deformation_quantization_examples.tex:720:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \dCrit(W))$ has
chapters/examples/kac_moody.tex:193:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \widehat{\mathfrak{g}}_k)$
chapters/examples/w_algebras.tex:160:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \mathcal{W}_N)$ has
chapters/examples/heisenberg_eisenstein.tex:127:$\operatorname{hom}_\alpha(\cC^{\textup{!`}}, \cH)$ has all higher
chapters/theory/higher_genus_modular_koszul.tex:10784:\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},\, \cA)
chapters/theory/higher_genus_modular_koszul.tex:10786:\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},\, \cA')
chapters/connections/outlook.tex:148: $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
chapters/connections/concordance.tex:1270: $\operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
chapters/connections/concordance.tex:1303: \operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
chapters/theory/bar_cobar_adjunction_curved.tex:6275:\mathrm{conil}\text{-}\mathrm{dg}\text{-}\cC^{\textup{!`}}_{\mathrm{ch}}\text{-}\mathrm{coalg}
chapters/theory/bar_cobar_adjunction_curved.tex:6280:dg~$\cC^{\textup{!`}}_{\mathrm{ch}}$-coalgebras, where:
chapters/theory/bar_cobar_adjunction_curved.tex:6295:\cC^{\textup{!`}}_{\mathrm{ch}}\text{-}\mathrm{coalg})$.
chapters/theory/algebraic_foundations.tex:544:$\cC = \cC^{\textup{!`}}_{\mathrm{ch}}$,




thinking
**Evaluating theorem restatements**

I’m considering whether to search for undefined macros or if I can use build or `texfot`, but perhaps it's unnecessary. I need to address redundancy in repeated theorem statements, especially around universal Koszul duality and others. 

I want clear examples where a theorem is stated differently, like Theorem 497 and Theorem 1104. For the user’s format, I might report both lines, but I'm stuck on how to best convey it. Maybe using a single file:line format could work—something like `[MEDIUM] chapters/examples/kac_moody.tex:497` while mentioning the redundancy.
thinking
**Identifying theorem redundancies**

I'm noticing another potential redundancy with Theorem 317, Theorem 4292, and Theorem 4352, along with a summary at 4407. Although Theorems 4292 and 4352 aren’t exact duplicates due to different contexts, the summary might be. The user mentioned they want instances of the same theorem stated in various ways, so I could report the duplication of `thm:universal-kac-moody-koszul` with `thm:level-shifting-abstract` and perhaps `thm:sl2-koszul-dual` and `thm:sl3-koszul-dual`. However, the latter two are just examples. Theorems 497 and 1104 do duplicate content. I might suggest demoting the earlier theorem or cross-referencing it with theorem 1104.
thinking
**Identifying redundancy in sections**

I’m seeing a potential redundancy with the `Open problems and conjectures` section at line 4145 and a later `Open questions` section at line 4508. Both sections cover similar topics, which might cause confusion if they present overlapping content. I need to consider if these sections can be consolidated or if I should clarify the distinctions between them. Keeping the user in mind, I want to ensure that the information is clear and accessible without unnecessary duplication.
thinking
**Refining chapter structure**

I'm realizing that inserting open questions before new results isn't great. I think I should move the “Open questions” section to the end of the chapter, after line 6063, and transition smoothly into the affine cubic shadow. This feels better quality-wise. I also wonder if starting each chapter should be evaluated. The user wants clear findings, so I shouldn't dwell on chapter openings. I'll look into the word "theorematic," which seems awkward and might clutter the text. So, I’ll search for its occurrences.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2088,2100p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i -- 'theorematic|package at generic|proved core of this chapter|invites natural extensions|This is the content of the assertion|the full shadow obstruction tower data\\.|The gauge-theoretic interpretation of the|shows that its PVA' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2348,2360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '4138,4168p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2088	\index{r-matrix@$r$-matrix!from collision residue}
  2089	\index{KZ connection!from collision residue}
  2090	\index{Arnold relation!CYBE verification}
  2091	We compute the genus-$0$, degree-$2$ collision residue
  2092	$\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
  2093	for $\cA = \widehat{\mathfrak{sl}}_{2,k}$ and verify that it
  2094	yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
  2095	governing the Knizhnik--Zamolodchikov equation.
  2096	
  2097	\emph{Step~1: OPE data.}
  2098	Let $\{e, h, f\}$ be the standard basis of $\mathfrak{sl}_2$
  2099	with Killing form normalised so that $\kappa(e,f) = 1$,
  2100	$\kappa(h,h) = 2$, and $\kappa(e,e) = \kappa(f,f) = \kappa(e,h)
 succeeded in 50ms:
18:kills the rest. This is the content of the assertion that gauge
1626:for exceptional types. The full shadow obstruction tower data.
3017:universal theorematic gap is the nilradical of the full
3175:bar spectral sequence alone, nor a theorematic general-rank
3295:level fails the required finiteness hypothesis below, no theorematic
4135:The proved core of this chapter (the universal Koszul dual, the
4137:$\widehat{\fg}_k$) invites natural extensions. Each open problem
4219:with theorematic target the \emph{semisimplified tilting quotient}
5787:The gauge-theoretic interpretation of the
 succeeded in 50ms:
  2348	 (the codimension-$1$ boundary of
  2349	 $\overline{\mathcal{M}}_{0,3}$);
  2350	\item Dualise via the level-shifted Killing form to obtain
  2351	 $r(z) \in \mathfrak{sl}_2^{\otimes 2}[z^{-1}]$.
  2352	\end{enumerate}
  2353	The CYBE is then the MC equation projected one further step:
  2354	genus~$0$, degree~$3$, codimension~$2$ boundary, via the Arnold
  2355	relation. The shadow obstruction tower of $\widehat{\mathfrak{sl}}_{2,k}$
  2356	terminates at degree~$3$ (Lie/tree archetype, $o_4 = 0$), so the
  2357	$r$-matrix $r(z) = \Omega/(k+2)\,z$ with simple pole and no
  2358	higher corrections is the \emph{complete} genus-$0$ shadow datum:
  2359	$\Theta^{\leq 3}_{0} = \Theta_{0}$.
  2360	\end{remark}
 succeeded in 53ms:
  4138	below arises from the geometry already established: the bar complex's
  4139	periodic structure at admissible level is forced by the denominator
  4140	formula; the braided monoidal equivalence is visible in the bar--cobar
  4141	adjunction's Verdier intertwining; and the coderived identification
  4142	with quantum groups is the categorical expression of the curvature's
  4143	role as a deformation variable. We state these as precise conjectures
  4144	with explicit hypotheses, separated from the proved theorems above.
  4145	
  4146	\subsection{Kazhdan--Lusztig equivalence from bar-cobar duality}
  4147	\label{subsec:kl-from-bar-cobar}
  4148	\index{Kazhdan--Lusztig equivalence!from bar-cobar}
  4149	
  4150	The chiral Koszul duality of Theorem~\ref{thm:universal-kac-moody-koszul}
  4151	and the module-level duality of Theorem~\ref{thm:e1-module-koszul-duality}
  4152	motivate a conjectural configuration-space route
  4153	(\ClaimStatusConjectured) to the Kazhdan--Lusztig
  4154	equivalence~\cite{KL93}.
  4155	
  4156	\begin{remark}[Conjectural route: KL equivalence from bar-cobar]%
  4157	\label{rem:kl-programme}

thinking
**Evaluating conjecture placement**

I’m considering whether lines 4135-4144 could work as an introduction to my conjectures. However, I'm uncertain about line 4508, which presents open questions — it feels problematic to include it before the results are fully discussed. I think it would be best to take a closer look at the lines around 4498-4535 to ensure everything flows logically. Let’s see if those lines fit better with the overall structure!
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '4498,4542p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2366,2375p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1618,1632p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- 'theorematic' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  4498	appear in Theorem~\ref{thm:fusion-bar-cobar}.
  4499	
  4500	\section{Open questions}
  4501	
  4502	\begin{question}
  4503	The genus-1 pipeline (\S\ref{sec:sl2-genus-one-pipeline}) shows that modular forms enter through $E_2$ via the $B$-cycle quasi-periodicity of the propagator. What is the complete structure at genus $g \geq 2$, where the propagator has $2g$ quasi-periodicity defects? Does the genus-$g$ partition function involve Siegel modular forms on $\mathfrak{H}_g$?
  4504	\end{question}
  4505	
  4506	\begin{question}
  4507	The exceptional types $E_6$, $E_7$, $E_8$ are treated in \S\ref{sec:exceptional-shadow-data} (Proposition~\ref{prop:exceptional-shadow-invariants}); the non-simply-laced types $B_2$, $G_2$, $F_4$ are treated in \S\ref{subsec:nsl-shadow-data} (Proposition~\ref{prop:nsl-shadow-tower}) and in the bar complex computations of \S\ref{sec:B2-details}--\S\ref{sec:G2-details}, all confirmed by 168 compute tests (\texttt{test\_non\_simply\_laced\_shadows.py}). Can the framework be extended further to affine algebras of twisted type or super Lie algebras?
  4508	\end{question}
  4509	
  4510	\begin{question}
  4511	What is the categorification? Is there a $2$-categorical Koszul
  4512	duality for affine Kac--Moody categories, lifting the module-level
  4513	duality of Theorem~\ref{thm:e1-module-koszul-duality} to a
  4514	$2$-functor on the $2$-category of module categories?
  4515	\end{question}
  4516	
  4517	\begin{question}
 succeeded in 50ms:
  2366	(Definition~\ref{def:category-O},
  2367	Definition~\ref{def:integrable-modules})
  2368	underlies the quantum group comparison.
  2369	
  2370	\begin{remark}[BGG reciprocity and the Kazhdan--Lusztig equivalence]\label{rem:category-O-affine}\label{rem:bgg-kl-bridge}
  2371	\index{BGG reciprocity!Kazhdan--Lusztig bridge}
  2372	\index{Kazhdan--Lusztig equivalence!BGG reciprocity}
  2373	BGG reciprocity for $\mathcal{O}_k(\widehat{\mathfrak{g}})$ states $[P_k(\lambda) : M_k(\mu)] = [M_k(\mu) : L_k(\lambda)]$. On the non-semisimple lift of the KL correspondence at $q = e^{\pi i/(k+h^\vee)}$, this maps to quantum group reciprocity:
  2374	\[
  2375	[P_q(\lambda) : \Delta_q(\mu)] = [\Delta_q(\mu) : L_q(\lambda)]
 succeeded in 50ms:
3017:universal theorematic gap is the nilradical of the full
3175:bar spectral sequence alone, nor a theorematic general-rank
3295:level fails the required finiteness hypothesis below, no theorematic
4219:with theorematic target the \emph{semisimplified tilting quotient}
 succeeded in 50ms:
  1618	\index{E6@$E_6$!shadow data}
  1619	\index{E7@$E_7$!shadow data}
  1620	\index{E8@$E_8$!shadow data}
  1621	\index{exceptional Lie algebra!modular characteristic}
  1622	\index{shadow archetype!exceptional types}
  1623	
  1624	The consistency checks of~\eqref{eq:km-kappa-derivation} verified
  1625	the universal formula $\kappa(\widehat{\fg}_k) = (k + h^\vee)\dim\fg/(2h^\vee)$
  1626	for exceptional types. The full shadow obstruction tower data.
  1627	
  1628	\begin{proposition}[Exceptional shadow invariants; \ClaimStatusProvedHere]%
  1629	\label{prop:exceptional-shadow-invariants}
  1630	For the simply-laced exceptional Lie algebras
  1631	$\fg \in \{E_6, E_7, E_8\}$, the affine Kac--Moody
  1632	algebra $\widehat{\fg}_k$ at non-critical level $k \neq -h^\vee$

thinking
**Inspecting grammar and jargon**

I noticed a fragment on line 1626 that creates a grammar issue. I should fix it by replacing it with a complete transition sentence. Additionally, I've spotted some awkward jargon, particularly "theorematic," at lines 3017, 3175, 3295, and 4219. Since the user requested an aesthetic audit, I’ll replace "theorematic" with "theorem-level" or "proved." I'll need to check the surrounding contexts on those lines for clarity. Let’s inspect!
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '3168,3180p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '3008,3020p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '4214,4222p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '3288,3300p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  3288	The genus-$g$ conformal block dimension for $L_{-1/2}(\mathfrak{sl}_2)$
  3289	with no insertions is $\dim \mathbb{V}(\Sigma_g) = d_0^{2-2g}
  3290	+ d_1^{2-2g} = 2$ for all $g \geq 1$. By
  3291	Proposition~\ref{conj:conformal-block-duality}(ii), any equality with
  3292	the corresponding count for~$\mathcal{A}^!$ would require a separate
  3293	rational braided categorical comparison on both sides. Since that
  3294	extra input is unavailable here, and in particular because the dual
  3295	level fails the required finiteness hypothesis below, no theorematic
  3296	equal-rank statement is obtained from the general Koszul package alone.
  3297	Since $L_{-7/2}(\mathfrak{sl}_2)$ is \emph{not}
  3298	$C_2$-cofinite, the conformal blocks at the dual level
  3299	require the logarithmic formalism
  3300	(Huang--Lepowsky--Zhang~\cite{HLZ}), and the
 succeeded in 52ms:
  3008	full non-reduced algebra $R_{L_{-4/3}}$
  3009	(Proposition~\ref{prop:large-orbit-obstruction}(ii)):
  3010	the null vectors of $L_{-4/3}(\mathfrak{sl}_2)$ contribute
  3011	nilpotent elements not visible on~$\mathcal{N}$, and
  3012	determining whether these produce off-diagonal bar
  3013	cohomology requires an explicit nilradical computation.
  3014	
  3015	This pattern holds for all types: reduced associated-variety
  3016	geometry may constrain the reduced Li--bar page, but the
  3017	universal theorematic gap is the nilradical of the full
  3018	non-reduced Li associated graded.
  3019	\end{example}
  3020	
 succeeded in 52ms:
  3168	This is the external Kac--Wakimoto character formula
  3169	\cite{KW88}. On the manuscript's bar-complex surface, the
  3170	preceding admissible analysis supplies the expected mechanism:
  3171	singular-vector embeddings produce the first bar differential,
  3172	and the surviving packet is organized by the admissible Weyl
  3173	group. What is \emph{not} proved here is a full internal
  3174	general-rank derivation of formula~\eqref{eq:kw-general} from the
  3175	bar spectral sequence alone, nor a theorematic general-rank
  3176	identification $E_2=E_\infty$ on that surface.
  3177	\end{proof}
  3178	
  3179	\begin{remark}[Admissible module counts]
  3180	\label{rem:admissible-module-count}
 succeeded in 50ms:
  4214	(Contributing to Conjecture~\ref{conj:master-dk-kl}.)
  4215	\end{conjecture}
  4216	
  4217	\begin{remark}[Categorical target]\label{rem:kl-conjecture-target}
  4218	Conjectures~\ref{conj:kl-periodic-cdg}--\ref{conj:kl-braided} are stated
  4219	with theorematic target the \emph{semisimplified tilting quotient}
  4220	$\mathcal{C}(U_q(\fg))$ (Remark~\ref{rem:kl-category-precision}),
  4221	obtained by quotienting out negligible morphisms.
  4222	At chain level one still expects a non-semisimple lift through the
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '5783,5792p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '4132,4145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '4300,4360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- 'This is the external Kac--Wakimoto character formula|This is Theorem~|This is an instance of Theorem~|This is Theorem~\\\\ref|This is the standard|This is the chiral analog' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  5783	\label{sec:affine-ht-chern-simons}
  5784	\index{Chern--Simons theory!holomorphic-topological}
  5785	\index{affine vertex algebra!as gauge theory}
  5786	
  5787	The gauge-theoretic interpretation of the
  5788	affine vertex algebra, showing that its PVA $\lambda$-bracket
  5789	is exactly the Poisson bracket of 3d holomorphic-topological (HT)
  5790	Chern--Simons theory on $\Sigma \times \mathbb{R}_t$.
  5791	
  5792	\subsection{The affine PVA \texorpdfstring{$\lambda$}{lambda}-bracket}
 succeeded in 53ms:
  4132	
  4133	\section{Open problems and conjectures}
  4134	
  4135	The proved core of this chapter (the universal Koszul dual, the
  4136	Feigin--Frenkel shadow, the genus-$1$ complementarity for all simple
  4137	$\widehat{\fg}_k$) invites natural extensions. Each open problem
  4138	below arises from the geometry already established: the bar complex's
  4139	periodic structure at admissible level is forced by the denominator
  4140	formula; the braided monoidal equivalence is visible in the bar--cobar
  4141	adjunction's Verdier intertwining; and the coderived identification
  4142	with quantum groups is the categorical expression of the curvature's
  4143	role as a deformation variable. We state these as precise conjectures
  4144	with explicit hypotheses, separated from the proved theorems above.
  4145	
 succeeded in 52ms:
  4300	\cong \mathfrak{z}(\widehat{\fg}_{-h^\vee})
  4301	\cong \mathrm{Fun}(\mathrm{Op}_{\fg^\vee}(D))
  4302	\end{equation}
  4303	where $\mathrm{Op}_{\fg^\vee}(D)$ is the space of $\fg^\vee$-opers
  4304	on the formal disc~$D$.
  4305	\end{theorem}
  4306	
  4307	\begin{proof}
  4308	At $k = -h^\vee$, $\kappa = 0$
  4309	(Corollary~\ref{cor:critical-level-universality}), so $\dfib^{\,2} = 0$
  4310	and the bar complex is a genuine cochain complex at every genus. The PBW spectral
  4311	sequence of Proposition~\ref{prop:km-generic-acyclicity} degenerates:
  4312	the $E_1$ page is $H^*(\fg;\, S^\bullet(\fg[t^{-1}]))$, and the
  4313	Whitehead lemma gives $H^0 = S^\bullet(\fg[t^{-1}])^\fg$.
  4314	This invariant ring is the center of the completed enveloping algebra,
  4315	which is the Feigin--Frenkel center $\mathfrak{z}$. The
  4316	Feigin--Frenkel isomorphism
  4317	$\mathfrak{z} \cong \mathrm{Fun}(\mathrm{Op}_{\fg^\vee}(D))$ is
  4318	\ClaimStatusProvedElsewhere{} \cite{Feigin-Frenkel, FG06}.
  4319	\end{proof}
 succeeded in 51ms:
507:This is the chiral analog of the classical Koszul duality between symmetric and exterior algebras, but curved by the level parameter.
820:This is Theorem~\ref{thm:universal-kac-moody-koszul} applied to $\mathfrak{g} = \mathfrak{sl}_3$ with $h^\vee = 3$. The explicit bar complex computation through degree~3 (Computation~\ref{comp:sl3-bar-dimensions}) is consistent: the bar differential on $\bar{B}^1$ extracts the OPE data with the double-pole coefficient $k$, and Verdier duality on the bar coalgebra produces the Koszul dual generators with double-pole coefficient $-k - 2 \cdot 3 = -k-6$. The curvature at non-critical levels satisfies $m_0 = \frac{k+3}{6}\cdot\kappa_{\mathfrak{sl}_3}$, vanishing precisely at $k = -3$.
1879:This is Theorem~\ref{thm:w-koszul-precise}\textup{(A)} restated in the
1988:For $\cA = \widehat{\mathfrak{g}}_k$, the genus-0 bar complex $\bar{B}^{(0)}$ is the configuration space bar complex on $\mathbb{P}^1$, which computes the Koszul dual $\widehat{\mathfrak{g}}_{-k-2h^\vee}$ (Theorem~\ref{thm:universal-kac-moody-koszul}). The genus-$g$ contribution $\bar{B}^{(g)}$ involves integration over $\overline{\mathcal{M}}_{g,n}$, producing cohomology classes in $H^*(\overline{\mathcal{M}}_g)$. The power $(k+h^\vee)^{2-2g}$ arises because each handle contributes a factor of the Casimir eigenvalue $(k+h^\vee)^{-1}$ from the propagator, and the Euler characteristic of a genus-$g$ surface with $n$ punctures gives exponent $2-2g-n$ (with the $n$-dependence absorbed into the $\mathrm{End}$ factor). This is the standard string theory genus expansion applied to the chiral algebra setting (cf.\ Theorem~\ref{thm:genus-induction-strict}).
3168:This is the external Kac--Wakimoto character formula
3850:This is an instance of Theorem~\ref{thm:quantum-complementarity-main} (Main Theorem~C), specialized to $\cA = \widehat{\mathfrak{sl}}_{2,k}$ at genus~$1$. We carry out each step explicitly.
3925:This is the standard relation between the Eisenstein series $E_2$ and the quasi-modular completion of the Weierstrass $\wp$-function. The Casimir sum $\sum_a J^a J_a = C_2$ contributes a factor of $\dim(\mathfrak{sl}_2) = 3$, giving $(k+2) \cdot 3 \cdot (-\pi^2/3) E_2 = -(k+2)\pi^2 E_2$. After absorbing the conventional normalization into the definition of $Z_1$, this yields the stated formula.
4017:This is Theorem~\ref{thm:higher-genus-inversion} for $g=1$, $\mathfrak{g}=\mathfrak{sl}_3$.
5836:This is the standard HT twist of 3d $\mathcal{N}=2$ Chern--Simons
5877:BRST variations above. This is Theorem~A (the bar-cobar

thinking
**Inspecting label usage**

I need to check the table label from line 1635 in the proposition environment, where it uses `\label{tab:exceptional-shadow-data}` outside of a table environment. Later, it references `Table\ref{tab:exceptional-shadow-data}`, which seems questionable. This label may refer to a proposition counter instead of a table. The user asked about unused labels, which might include this mislabeled one. To fix it, I could wrap it in a `table` environment or rename the label. However, the proposition already has a label.
exec
/bin/zsh -lc "rg -n -- '\\\\section\\{Open problems and conjectures\\}|\\\\section\\{Open questions\\}' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- 'ref\\{chap:kac-moody\\}|ref\\{chap:kac-moody-koszul\\}' chapters appendices standalone" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- 'ref\\{tab:exceptional-shadow-data\\}|ref\\{rem:bgg-kl-bridge\\}|ref\\{rem:category-O-affine\\}' chapters examples appendices standalone metadata chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- 'r\\(z\\) = \\\\Omega/\\(k\\+2\\)\\\\,z|\\\\Omega/\\(k\\+2\\)\\\\,z' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
4133:\section{Open problems and conjectures}
4500:\section{Open questions}
 exited 2 in 50ms:
rg: examples: No such file or directory (os error 2)
 succeeded in 51ms:
appendices/koszul_reference.tex:65:\emph{theorem} (proved in Chapter~\ref{chap:kac-moody-koszul}), not a
standalone/introduction_full_survey.tex:4712:(Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
standalone/introduction_full_survey.tex:4962:Kac--Moody (Ch.~\ref{chap:kac-moody}) &
chapters/examples/lattice_foundations.tex:12:(Chapter~\ref{chap:kac-moody-koszul}) have degenerate braiding:
chapters/examples/lattice_foundations.tex:4972:(Chapter~\ref{chap:kac-moody},
chapters/frame/heisenberg_frame.tex:1860:abelian (rank-$1$) structure. In Chapters~\ref{chap:kac-moody-koszul}
chapters/examples/heisenberg_eisenstein.tex:1546:Virasoro families (Chapter~\ref{chap:kac-moody},
chapters/examples/free_fields.tex:2602:is proved in Chapter~\ref{chap:kac-moody-koszul}: the low-degree bar
chapters/examples/free_fields.tex:4678:Chapter~\ref{chap:kac-moody-koszul}. The identification with string BRST
chapters/examples/free_fields.tex:5291:The WZW/Kac--Moody bar complex is computed in Chapter~\ref{chap:kac-moody-koszul}; the central charge is $c = k\dim\mathfrak{g}/(k + h^\vee)$.
chapters/examples/w_algebras.tex:41:Chapter~\ref{chap:kac-moody-koszul}.
chapters/examples/w_algebras.tex:107:(Chapter~\ref{chap:kac-moody-koszul}) to
chapters/examples/w_algebras.tex:1437:(Chapter~\ref{chap:kac-moody}), the chiral Koszul dual of
chapters/examples/landscape_census.tex:228:% (Chapter~\ref{chap:kac-moody-koszul}), this reads
chapters/examples/landscape_census.tex:284:$\widehat{\fg}_k$ (simply-laced: $A_n, D_n, E_{6,7,8}$) & L & 3 & $C$: Lie bracket & \S\ref{chap:kac-moody-koszul} \\
chapters/examples/bar_complex_tables.tex:4481:\underbrace{\text{OPE data}}_{\S\ref{chap:kac-moody}}
chapters/theory/algebraic_foundations.tex:335:The chiral enhancement appears in Chapter~\ref{ch:heisenberg-frame} (Heisenberg, double pole), \S\ref{sec:free-fermion} (free fermions, simple pole), and Chapter~\ref{chap:kac-moody-koszul} (Kac--Moody, mixed poles).
chapters/theory/existence_criteria.tex:526:For details, see Chapter~\ref{chap:kac-moody}.
chapters/connections/concordance.tex:632:Chapter~\ref{chap:kac-moody}.
chapters/connections/concordance.tex:7960:Chapter~\ref{chap:kac-moody} and the critical-level
 succeeded in 53ms:
2094:yields the Casimir $r$-matrix $r(z) = \Omega/(k+2)\,z$
2263:Set $r_{ij} = r(z_{ij}) = \Omega/(k+2)\,z_{ij}$ with
2357:$r$-matrix $r(z) = \Omega/(k+2)\,z$ with simple pole and no
exec
/bin/zsh -lc "rg -n -- 'ref\\{tab:exceptional-shadow-data\\}|ref\\{rem:bgg-kl-bridge\\}|ref\\{rem:category-O-affine\\}' chapters appendices standalone chapters/examples chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Exploring label detection**

I might also consider using ripgrep from the root to search the entire repository, especially since we didn't find any references before. Now, detecting all unused labels could be tricky since there might be many. I could compare labels to references with a script, but the user wants all of them, so I should probably use a shell command to extract labels from the file and see if they're referenced. Additionally, I might limit the search to `.tex` files, and using `awk` with `rg` should help. Let's focus on shell scripting for this.
codex
I’m checking label usage globally now. Cosmetic clutter in this chapter includes alias labels that don’t buy anything, and the only reliable way to call that is to compare each local label against the rest of the TeX tree, not just this file.
exec
/bin/zsh -lc 'labels=$(perl -ne '"'while(/\\\\label\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/examples/kac_moody.tex); for label in "'$labels; do count=$(rg -n --glob '"'*.tex' \"ref\\\\{"'$label'"\\\\}|eqref\\\\{"'$label'"\\\\}|autoref\\\\{"'$label'"\\\\}|cref\\\\{"'$label'"\\\\}|Cref\\\\{"'$label'"\\\\}|pageref\\\\{"'$label'"\\\\}|nameref\\\\{"'$label'"\\\\}|vref\\\\{"'$label'"\\\\}|Vref\\\\{"'$label'"\\\\}\" . | wc -l | tr -d ' '); if [ \""'$count" = "0" ]; then echo "$label"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
chap:kac-moody-koszul
chap:kac-moody
tab:km-five-theorems
tab:km-shadow-archetype
eq:km-triple
rem:km-master-mc
rem:km-three-pillar
rem:km-genus-two-shells
comp:km-genus1-hessian
rem:km-four-level
sec:km-bar-complex
eq:kac-moody-koszul-basic
thm:critical-level-structure
def:loop-algebra
def:affine-kac-moody
eq:affine-kac-moody-ope

thinking
**Evaluating script flaws and findings**

I seem to have a flaw in my script related to regex newlines, causing it to output all labels due to a regex error. I need a better shell script that uses fixed string search with `rg -n --fixed-strings "\\ref{$label}"` for selected labels, but probably not for all of them.

I should consider searching for double spaces or lines with `\item`. I've identified several potential issues, including wrong denominators, sentence fragments, duplicate labels, and redundant theorem statements that will need closer inspection.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '492,515p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1098,1120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   492	
   493	The level shift $k \mapsto -k - 2h^\vee$ is Verdier duality on configuration spaces: the Serre dual of the level-$k$ invariant form on $\overline{C}_{n+1}(X)$ is the level-$(-k-2h^\vee)$ form, the shift $2h^\vee$ arising from the adjoint Casimir eigenvalue.
   494	
   495	\subsection{The general pattern}
   496	
   497	\begin{theorem}[Level-shifting duality, abstract form; \ClaimStatusProvedHere]\label{thm:level-shifting-abstract}
   498	\index{Feigin--Frenkel duality|textbf}
   499	\index{level!shifted}
   500	\index{Kac--Moody algebra!Koszul dual}
   501	For the Heisenberg algebra, Koszul duality sends the Lie-type $\mathcal{H}_k$ to the Com-type $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ (\S\ref{sec:frame-koszul-dual}): the dual algebra changes type. For non-abelian Kac--Moody algebras, Koszul duality shifts the level: the Koszul dual is $(\widehat{\mathfrak{g}}_k)^! = \mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$, the chiral Chevalley--Eilenberg algebra at level $k' = -k - 2h^\vee$, sharing the same modular characteristic as $\widehat{\mathfrak{g}}_{k'}$ but distinct from it as a chiral algebra.
   502	
   503	For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$, there exists a quasi-isomorphism of complexes:
   504	\begin{equation}
   505	\bar{B}^{\mathrm{geom}}(\widehat{\mathfrak{g}}_k)^\vee \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}
   506	\end{equation}
   507	This is the chiral analog of the classical Koszul duality between symmetric and exterior algebras, but curved by the level parameter.
   508	\end{theorem}
   509	
   510	\begin{proof}
   511	This is proved as Theorem~\ref{thm:universal-kac-moody-koszul} below: the bar complex of $\widehat{\mathfrak{g}}_k$ is computed via residues on FM compactifications (Step~1), the curvature $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is identified from the double-pole OPE (Step~2), the cobar OPE recovers the level $-k - 2h^\vee$ structure constants (Step~3), and the result is characterized by functorial uniqueness (Step~4).
exec
/bin/zsh -lc "rg -n --fixed-strings '\\\\ref{rem:bgg-kl-bridge}' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\\\ref{tab:exceptional-shadow-data}' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1098	\end{remark}
  1099	
  1100	\section{\texorpdfstring{General $\widehat{\mathfrak{g}}$: functorial construction}{General g: functorial construction}}
  1101	
  1102	\subsection{Abstract setting}
  1103	
  1104	\begin{theorem}[Universal Koszul duality for affine Kac--Moody; \ClaimStatusProvedHere]\label{thm:universal-kac-moody-koszul}
  1105	\textup{[Regime: curved-central
  1106	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1107	
  1108	For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$, there is a canonical Koszul duality:
  1109	\begin{equation}
  1110	(\widehat{\mathfrak{g}}_k)^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}
  1111	\end{equation}
  1112	This duality:
  1113	\begin{enumerate}
  1114	\item Is functorial in $\mathfrak{g}$ (respects Lie algebra homomorphisms)
  1115	\item Preserves derived equivalences of module categories
  1116	\item Intertwines the level $k$ representation theory with level $-k-2h^\vee$ representation theory
  1117	\item Manifests as Langlands duality for $\mathfrak{g}$ in the critical level limit
 exited 1 in 52ms:

 exited 1 in 52ms:







thinking
**Revising chapter structure**

I’m thinking about improving the chapter by moving both sections to the end, right after line 6063. Another possibility is combining the first into a "Conjectural Extensions" section after all the proved results. I could list separate findings at lines 4133 and 4500, or maybe combine them for conciseness. However, if I need to keep it clear, separating might be better due to the specific lines. Let’s think it through!
thinking
**Reviewing formatting choices**

I'm considering how to format the user’s request for specific lines in a document. They mentioned wanting to note lines like 2094, 2263, and 2357, but I wonder if it would be clearer to separate these findings. The format states file:line singular, which makes this a bit tricky. Using multiple lines in one bullet might not work, so I’m thinking to separate them instead. I also noted some awkward jargon, like “theorematic,” that might need better phrasing. I need to decide what's acceptable to report and what might feel cliché.
thinking
**Evaluating content clarity**

There's a potential issue with line 18, where it says, "This is the content of the assertion that gauge theory is simpler than gravity." I’m not sure if it’s a pure mathematical transition or more of a rhetorical flourish. The user requested a certain quality for the chapter opening, focusing on its cosmetic aspects, which makes me consider whether to flag it as fluff. It’s a bit subjective, so maybe it shouldn’t be marked after all.
thinking
**Considering file parsing methods**

I could use `perl` to parse the file, but maybe it’s simpler to go with a `while read` loop and use `rg` for fixed string searching. This avoids complexity and lets me steer clear of regex with newlines. However, this might generate a lot of unused labels in the output, especially since many equation labels might not be referenced. I realized my previous script was flawed due to a regex error, making it less effective.
thinking
**Clarifying definitions**

It seems like the definition of channel decomposition around line 1342 uses `\kappa` as a scalar. I think that’s fine as long as it's clear in the context of the definition. However, the user specifically asked for exact line numbers, so I might need to report where the clusters begin instead. I'll make sure to provide that information clearly for the user!
thinking
**Considering notation consistency**

I’m wondering if the findings on line 133 are enough, especially since “Report EVERY finding” is tricky. Maybe I should focus on searching for instances of bare \kappa where multiple families collide, like on line 1212 where it refers to duality. However, there are many instances to consider. I might want to strengthen the treatment of notation consistency, especially with \kappa in mixed-family comparisons. Overall, I need to explore this thoroughly while being selective about findings.
exec
/bin/zsh -lc "rg -n -- '\\\\kappa\\s*=|\\\\kappa\\cdot|\\\\kappa\\b' chapters/examples/kac_moody.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
rg: regex parse error:
    (?:\\kappa\s*=|\\kappa\cdot|\\kappa\b)
                          ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -P '\\\\kappa\\s*=|\\\\kappa\\\\cdot|\\\\kappa\\b' chapters/examples/kac_moody.tex | head -n 120" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
5:degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
12:cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
62: $\kappa(\widehat{\fg}_k)
64: $\kappa + \kappa' = 0$ (affine KM)
85:$\kappa(\widehat{\fg}_k)$ &
88: $\kappa(x,[y,z])$ (Lie bracket) \\
92: (sharing $\kappa$ with $\widehat{\fg}_{-k-2h^\vee}$) \\
93:Complementarity & $\kappa + \kappa' = 0$ (affine KM) \\
133:$\kappa = \dim(\mathfrak{g}) \cdot (k + h^\vee)/(2h^\vee)$
137:$\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$. The strict model $\Convstr$ carries a nonzero cubic shadow at degree~$3$
169:minimal package $\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$
171:$\kappa = \dim(\mathfrak{g})\cdot(k+h^\vee)/(2h^\vee)$, while
177:At critical level $k = -h^\vee$, $\kappa = 0$ and the bar complex
200:the scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds
235:At level~$k$ with $\kappa=3(k+2)/4$, the genus-$1$ deformation
242:\kappa
265:(iv)~genus tower with $\kappa = \dim(\mathfrak{g})\cdot(k + h^\vee)/(2h^\vee)$, Lie/tree shadow
402:J^a(z) J^b(w) \sim \frac{k \kappa^{ab}}{(z-w)^2} + \frac{{f^{ab}}_c J^c(w)}{z-w}
404:where $\kappa^{ab} = \kappa_{\mathfrak{g}}(T^a, T^b)$ is the normalized invariant bilinear form on $\mathfrak{g}$ (normalized so that long roots have squared length $2$), ${f^{ab}}_c$ are the structure constants, and $\sim$ means ``has singular part.'' In an orthonormal basis with $\kappa^{ab} = \delta^{ab}$, this reduces to the familiar form $k\delta^{ab}/(z-w)^2$.
511:This is proved as Theorem~\ref{thm:universal-kac-moody-koszul} below: the bar complex of $\widehat{\mathfrak{g}}_k$ is computed via residues on FM compactifications (Step~1), the curvature $m_0 = (k+h^\vee)\kappa/(2h^\vee)$ is identified from the double-pole OPE (Step~2), the cobar OPE recovers the level $-k - 2h^\vee$ structure constants (Step~3), and the result is characterized by functorial uniqueness (Step~4).










thinking
**Addressing notation consistency**

I want to rename the Casimir element to either `\Omega_{\mathfrak g}` or `\Cas_{\mathfrak g}` to keep things clear in the bar-complex discussion. I'll leave `\kappa(\widehat{\fg}_k)` for the scalar modular characteristic. It's crucial to have precise line numbers, like 521 and 572, to track occurrences. The current chapter uses `\kappa` for three different concepts, which really creates confusion. So, I’ll ensure proper notation for each concept moving forward. Let's keep it clear!
thinking
**Clarifying chapter confusion**

I’m noticing some confusion from three meanings in the same chapter, and I need an exact fix. Line 2245 has a formula with the inverse Killing form, but I'm considering a rename. I might look for an `\Omega` r-matrix with a missing k. 

The user wants any bare `\Omega/z` without the level k, but we only have it with a denominator, which is fine. I could also search for an undefined macro, like `\Convstr`, and check line 137. 

The theorem duplication on line 497 stands out, along with another redundant theorem on line 1865 about principal W-algebras. I might check if the user is asking about the same theorem in different wording.
thinking
**Identifying potential issues**

I'm noticing a few potential issues in the text. For line 4407, a summary of oper critical levels repeats results from lines 4292-4352, but that could be okay as a summary subsection. Line 4140 has "bar--cobar" with a double hyphen instead of an en dash, which is standard in LaTeX. 

Line 4519 contains an awkward line break with "A chain-level local oper resolution," though it’s not a major concern. Line 1618 has a proposition with a table, but it uses `\begin{center}` instead of `table`, which might be fine aesthetically. The unused label `tab:` might be good enough. 

Line 5817 shows repeated indices in the action formula. Finally, line 5869 has a remark about the bar differential that could seem mathematically bold. Still, since the user is focusing on cosmetic changes, I could decide to ignore the last point.
thinking
**Checking for potential issues**

I need to check if line 2263 has a wrong denominator and inspect it further. I’ve already noted a possible issue with line 1626 being medium to low, and line 5787 could be low as well. There are other potential issues that I should look into: line 3017 looks theorematic as low, line 4500 has open questions at a structural high, and line 497 is a duplicate theorem with medium to high relevance. I need to examine these fragments carefully.
thinking
**Planning section adjustments**

I have an exact fix: I need to move both sections and perhaps use line 4133 as an anchor. The problem is that after line 4133, there are open problems, and then back to proved sections at lines 4292 and 4528, disrupting the transition order. So, I'll move lines 4133-4287 and 4500-4526 to a final `\section{Open Problems}` after 6063. 

I've got to address potential issues too. For instance, line 4143's language may seem generic or unnecessary. Line 497 might be a duplicate theorem of line 1104, so I’m considering replacing the theorem environment at lines 497-512 with a remark or proposition. Overall, clarity is key.
thinking
**Addressing label duplication**

I’ve spotted a potential issue with line 2370 regarding double unused labels. I need to fix this by deciding whether to keep only `\label{rem:bgg-kl-bridge}` or `\label{rem:category-O-affine}`. It’s important to resolve this duplication to keep things clear and organized. I’ll make sure to confirm which one is necessary for the context and remove the unused label accordingly! This should help streamline the document and avoid confusion later on.
thinking
**Evaluating canonical labels**

I need to choose a canonical label and think maybe the remark title "bridge" would be best as `rem:bgg-kl-bridge`. But I need to consider earlier definitions in the context of `category-O`. Since there are no external references, I can specify just one canonical label, favoring `\label{rem:bgg-kl-bridge}` and removing the duplicate. If future references use category O, the remark title should suffice. For now, I'll mark `rem:bgg-kl-bridge` as the better option. Also, for `tab:exceptional-shadow-data`, I could delete an unused line or actually add a `table` environment.
thinking
**Fixing theorematic coinage**

I’m spotting potential issues with certain theorematic expressions that need fixing. For example, in line 3017, I should change the phrase about the universal remaining gap to clarify it. For 3175, I could improve the wording to mention "proved general-rank identification $E_2=E_\infty$". In line 4219, it seems better to remove the adjective entirely and say "are stated with target...". 

I see that multiple lines, like 3017, 3175, 3295, and 4219, might be referenced together. I also suspect line 2094 has a formula typo, possibly repeating later in 2263 and 2357, so I'll format it accordingly.
thinking
**Inspecting notation collision**

I’m concerned about a potential critical issue with a notation collision around line 521. It seems like it might be important to inspect the surrounding lines, specifically from 518 to 523, to see what's going on. I'll take a closer look at that section to identify any conflicts or errors. Addressing this could be crucial for clarity and accuracy in the overall work. Let's see what I find in those lines!
thinking
**Evaluating symbols and clarity**

I’m noticing that the symbols like J^a \otimes J_a and \kappa are used confusingly. It seems like \kappa is applied both as a scalar characteristic and for other elements. Maybe I should mark it as [HIGH] or [CRITICAL] for review, especially for clarification in the audit. The chapter needs consistent naming, so I might rename some instances. I'll also check if I need to include line 572 in this inspection.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '128,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '647,652p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '568,574p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '518,525p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   647	The $A_\infty$ structure satisfies $m_1^2 \neq 0$ for $k \neq -h^\vee$ (the bar differential $d_{\bar{B}}$ itself always satisfies $d_{\bar{B}}^2 = 0$, but the curvature manifests in the internal differential). The residue of the double-pole OPE $e(z)f(w) \sim k/(z-w)^2 + h(w)/(z-w)$ contributes the curvature (cf.\ Definition~\ref{def:curved-koszul-km}):
   648	\begin{align}
   649	m_0 &= \frac{k + h^\vee}{2h^\vee} \cdot \kappa, \qquad m_1^2(a) = [m_0, a]
   650	\end{align}
   651	where $\kappa$ is the Casimir element.
   652	
 succeeded in 53ms:
   518	\begin{definition}[Curved Koszul complex]\label{def:curved-koszul-km}
   519	For $k \neq -h^\vee$, the $A_\infty$ structure has curvature:
   520	\begin{equation}
   521	m_0 = \frac{k+h^\vee}{2h^\vee} \cdot \kappa, \qquad m_1^2(a) = [m_0, a] = m_2(m_0, a) - m_2(a, m_0)
   522	\end{equation}
   523	where $\kappa = \sum_a J^a \otimes J_a$ is the Casimir element (the quadratic element in the universal enveloping algebra defined by the Killing form). This curvature vanishes precisely at $k = -h^\vee$ (critical level), where $m_1$ becomes a genuine differential.
   524	\end{definition}
   525	
 succeeded in 53ms:
   568	\section{\texorpdfstring{Explicit computation: $\widehat{\mathfrak{sl}}_2$}{Explicit computation: sl-2}}
   569	
   570	\subsection{Setup and generators}
   571	
   572	For $\mathfrak{g} = \mathfrak{sl}_2$, the data are: $h^\vee = 2$, $\dim(\mathfrak{sl}_2) = 3$, with the standard basis $\{e, f, h\}$ satisfying $[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$. The normalized invariant form is $(h,h) = 2$, $(e,f) = 1$ (the Killing form for $\mathfrak{sl}_2$ is $\kappa = 4 \cdot \text{tr}_{\text{fund}}$, but we use the standard normalization $(\theta|\theta) = 2$).
   573	
   574	\begin{definition}[\texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} at level \texorpdfstring{$k$}{k}]
 succeeded in 53ms:
   128	($r_{\max} = 3$), between the Gaussian families
   129	(Heisenberg, lattice, free fermion; $r_{\max} = 2$) and
   130	the contact/quartic archetype of $\beta\gamma$
   131	($r_{\max} = 4$). At generic level $k \neq -h^\vee$, the
   132	scalar curvature
   133	$\kappa = \dim(\mathfrak{g}) \cdot (k + h^\vee)/(2h^\vee)$
   134	controls the genus tower, and one-channel scalar saturation
   135	(Theorem~\ref{thm:theta-direct-derivation}) identifies the
   136	minimal scalar package
   137	$\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$. The strict model $\Convstr$ carries a nonzero cubic shadow at degree~$3$
   138	from the Lie bracket, but the Jacobi identity forces $o_4 = 0$
   139	and the tower terminates at $r = 3$. At the homotopy level,
   140	$\Definfmod(\widehat{\fg}_k)$ is

thinking
**Evaluating mathematical clarity**

I’m thinking about adopting either `\kappa_{\mathrm{KM}}` or always going with `\kappa(\widehat{\mathfrak g}_k`. There might be a potential for confusion with Heisenberg's `\mathcal H_\kappa` in certain lines, but it seems okay. I’m considering whether I need to fix the phrase about gauge theory in lines 18-20 since it feels like a flashy slogan that might dilute its seriousness. The exact fix could involve directly contrasting it with the Virasoro case instead. Let's look at those lines closely.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '14,24p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    14	the tower terminates (class~$L$, $r_{\max} = 3$). Gauge symmetry
    15	introduces noncommutativity but not infinite obstruction complexity:
    16	the structure constants of~$\fg$ produce exactly one new shadow
    17	beyond the Gaussian, and the Jacobi identity is the mechanism that
    18	kills the rest. This is the content of the assertion that gauge
    19	theory is simpler than gravity; for the Virasoro algebra
    20	(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the
    21	quartic Virasoro OPE, the tower does not terminate.
    22	
    23	The Feigin--Frenkel involution
    24	$k \mapsto -k - 2h^\vee$, the critical-level center, opers,




thinking
**Evaluating chapter quality**

I’m considering a report of low to medium quality. It doesn’t seem like AI-generated fluff but more of a rhetorical flourish. The user asked specifically about the chapter opening; it might be good, yet this particular phrase could use sharpening. There are some potential issues to address, like awkward jargon or long questions that don't fit markdown. I might also need to check for conflicts in notation and grouping in specific lines. Overall, there’s room for improvement!
thinking
**Assessing prose issues**

I’m focusing on prose-related potential issues in the document. For lines 4133 and 4500, I might improve by choosing one prominent problem from each. There are fragments in lines 1624-1626 and 5787-5790 that need attention, as well as duplicate labels and unused references in line 2370. A few items may be low to medium in concern, like duplicate theorems and proof placeholders. Some examples are acceptable, but there might be redundancy in the “Critical fixed point for principal W-algebras” proof that I should restate.
thinking
**Searching for issues**

I’m considering the possibility of double-checking if similar results appear in the W-algebras chapter, even though that wasn't specifically asked. I might choose to ignore it for now. Instead, I’ll focus on searching for the open problems section, particularly the parts in the middle of the chapter, like before sections 4288 and 4528. It's important to ensure everything is in order there and see if any issues need addressing.
thinking
**Analyzing potential issues**

I'm looking at the code and considering the possibility of unmatched braces, but that seems unlikely. I also checked for comments, and they don’t appear to be a problem. I'm wondering about grabbing data related to the "shadow obstruction tower" and some specific fragments that might hold key insights. Since the user requested every finding, I’ll aim to compile around 10 significant items and consider searching for some terms to ensure I’m thorough.
collab wait(call_cydAUxkvf6n5Ow5If85ZGlUT)
  receivers: 019d83fe-2fa8-7830-98e8-f27b6be2239d
wait(call_cydAUxkvf6n5Ow5If85ZGlUT) 1 agents complete:
  019d83fe-2fa8-7830-98e8-f27b6be2239d completed: "- **Opening roadmap** – `chapters/examples/kac_moody.tex:4-35`: the first paragraphs jump straight into the obstruction …"

thinking
**Fixing LaTeX issues**

I’ve finished reviewing my findings, and it looks like one might be invalid since it’s significantly smaller and not banned. The user asked for a list of slop words, so I can disregard that if it’s not valid. When checking the roadmap, I see that the chapter does indeed open with a problem, so that's not an issue. There's a broken LaTeX token at line 199, and I need to inspect it further for weird punctuation. This is an actual fix, so I should search for other occurrences.
codex
I’ve got enough grounded defects now to stop broad scanning and do verification. The last pass is checking each candidate against the exact local lines so the final list doesn’t contain soft or speculative complaints.
exec
/bin/zsh -lc "rg -n -- 'The full shadow obstruction tower data\\.|The gauge-theoretic interpretation of the|universal theorematic gap|theorematic general-rank|no theorematic|theorematic target' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '194,202p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '\\\\textup\\{\\(\\};|\\\\textup\\{\\):|\\\\textup\\{\\(\\}:|\\\\textup\\{\\);' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '\\\\Omega/\\(k\\+2\\)\\\\,z|\\\\Omega/\\(k\\+2\\)\\\\,z_\\{ij\\}|\\\\Omega/\\(k\\+2\\)\\\\,z_{ij}' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:\\Omega/\(k\+2\)\\,z|\\Omega/\(k\+2\)\\,z_\{ij\}|\\Omega/\(k\+2\)\\,z_{ij})
                                                                              ^
error: repetition quantifier expects a valid decimal
 succeeded in 53ms:
199:\textup{(}; all currents $J^a$ have conformal weight~$1$, so
1312:\textup{(}: all currents share conformal weight~$1$, so
 succeeded in 53ms:
   194	is \emph{strictly formal}
   195	(Theorem~\ref{thm:km-strictification}): all transferred higher brackets
   196	vanish identically ($\ell_k^{\mathrm{tr}} = 0$ for $k \geq 3$),
   197	and the strict dg~Lie model \emph{is} the full $L_\infty$-structure
   198	at every genus
   199	\textup{(}; all currents $J^a$ have conformal weight~$1$, so
   200	the scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds
   201	unconditionally, cf.\ Theorem~D\textup{)};
   202	(iii)~the Sugawara construction at non-critical level gives a Virasoro
 succeeded in 53ms:
1626:for exceptional types. The full shadow obstruction tower data.
3017:universal theorematic gap is the nilradical of the full
3175:bar spectral sequence alone, nor a theorematic general-rank
3295:level fails the required finiteness hypothesis below, no theorematic
4219:with theorematic target the \emph{semisimplified tilting quotient}
5787:The gauge-theoretic interpretation of the
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1308,1314p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1308	is determined, the modular characteristic
  1309	$\kappa(\widehat{\fg}_k) = \dim(\fg)(k + h^\vee)/(2h^\vee)$
  1310	(Theorem~\ref{thm:modular-characteristic}(i)) controls every genus
  1311	$g \geq 1$ via $\mathrm{obs}_g = \kappa \cdot \lambda_g$
  1312	\textup{(}: all currents share conformal weight~$1$, so
  1313	the scalar formula holds without a cross-channel correction,
  1314	cf.\ Theorem~D\textup{)}.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '2259,2265p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2259	\;+\;
  2260	\eta_{31} \wedge \eta_{12}
  2261	\;=\; 0.
  2262	\end{equation}
  2263	Set $r_{ij} = r(z_{ij}) = \Omega/(k+2)\,z_{ij}$ with
  2264	$z_{ij} = z_i - z_j$.
  2265	The CYBE






thinking
**Identifying section issues**

I need to find order issues in the open questions section around lines 4133 and 4500. It seems line 4133 might be less severe since it's followed by more theorems. I’m thinking I should report both, with a note about how after line 4288 and 4528, the focus returns to proofs. However, user wanted the exact line, so I may focus on 4500, as it's more jarring. The issue with line 4133 is related to the heading "Open problems and conjectures" being followed by more theorems, which doesn’t seem right. It should appear before open problems.
thinking
**Reporting line issues**

I’m considering reporting issues at lines 4133 and 4500 separately since they’re line-specific, and the user requested exact details. It makes sense to identify the same fix and also include the findings at line 1626, line 5787, line 199/1312 with malformed punctuation, duplicate theorems, duplicate labels, a table label, notation collisions, an r-matrix typo, and open problems order — about 11 total findings. I'm also contemplating a rhetorical slogan at line 18, though that might be less significant. I'll need to check the section on "Open problems and conjectures" at line 4133 for generic language.
thinking
**Verifying findings format**

I need to ensure that there are no AI errors or unnecessary markdown to consider. It sounds like I might want to mention that no occurrences were found, but since the user only wants findings and a summary, I'll present it as “Checked: 6074 | Findings: 11 | Verdict: FAIL.” I need to provide exact fixes clearly, like a specific example where `\kappa` is misused across different contexts. I think including the problematic line format will help clarify issues.
thinking
**Documenting issues and fixes**

I’ve found a couple of problems to address. For the first issue, we have an incorrect expression: `r(z) = \Omega/(k+2)\,z` actually means `(\Omega/(k+2))z`, not `\Omega/((k+2)z)`. I will correct this to `r(z)=\Omega/((k+2)\,z)` across the mentioned lines. 

Then for the second issue at line 199, there's a malformed parenthesis causing punctuation issues, and I can fix it by rewriting it for clarity. This should help make everything more readable!
thinking
**Choosing reference points**

I’m considering using line 133 since it's the first introduction of the bare scalar \(\kappa\). This could be important in the problem text, especially if there are later collisions discussed. However, I also need to think about including line 521 because that's where collision becomes a significant factor. I wonder if I should pick both or just one of these lines to ensure clarity for the user. It’s an important decision!
thinking
**Evaluating issues by severity**

I think I can specify “Checked: 6074 lines,” even though the contract says “Checked: N.” I need to order the issues by severity, starting with HIGH or CRITICAL. I might want to flag notation collision as critical if it obscures important formulas. The r-matrix malformed denominator could also be critical since it could lead to a wrong mathematical formula. There are also open questions and duplicate theorems that might need medium or low attention.
codex
- [CRITICAL] `chapters/examples/kac_moody.tex:133` — PROBLEM: `\kappa` is introduced here as the affine modular characteristic, but the same chapter reuses `\kappa` for the Casimir element at `521-523` and `649-651`, and for the Killing form at `572`. Three different objects collapse into one symbol. FIX: reserve `\kappa(\widehat{\fg}_k)` or `\kappa_{\mathrm{KM}}` for the scalar invariant; rename the Casimir element to `\Omega_{\fg}` in the curvature formulas (`m_0=\frac{k+h^\vee}{2h^\vee}\Omega_{\fg}`); rename the Killing form in `572` to `\kappa_{\fg}` or `K_{\mathfrak{sl}_2}`.

- [CRITICAL] `chapters/examples/kac_moody.tex:2094` — PROBLEM: `r(z) = \Omega/(k+2)\,z` parses as `(\Omega/(k+2))z`, not `\Omega/((k+2)z)`; the same typo recurs at `2263` and `2357`. FIX: rewrite them as `r(z)=\Omega/((k+2)\,z)` and `r_{ij}=\Omega/((k+2)\,z_{ij})`.

- [HIGH] `chapters/examples/kac_moody.tex:497` — PROBLEM: `thm:level-shifting-abstract` duplicates the general affine level-shift theorem later stated at `1104-1119`, and its proof is only a forward pointer. FIX: delete the theorem/proof block at `497-512` and replace it with a short roadmap remark pointing to `thm:universal-kac-moody-koszul`.

- [HIGH] `chapters/examples/kac_moody.tex:4133` — PROBLEM: `\section{Open problems and conjectures}` appears before later proved material (`thm:oper-bar-h0` at `4292` onward). The chapter announces a conjectural lane and then resumes theorem-proof exposition. FIX: move `4133-4287` to the end of the chapter and merge it into one final `\section{Open Problems}` after `6063`.

- [HIGH] `chapters/examples/kac_moody.tex:4500` — PROBLEM: a second `\section{Open questions}` interrupts the flow immediately before the proved section `The affine cubic shadow and critical-level emergence` at `4528`. FIX: move `4500-4526` into the same final end-of-chapter open-problems section and start `4528` with a forcing transition such as `The remaining local calculation is the affine cubic shadow.`

- [MEDIUM] `chapters/examples/kac_moody.tex:199` — PROBLEM: `\textup{(};` is malformed punctuation; the same defect recurs at `1312` as `\textup{(}:`. FIX: rewrite both clauses as ordinary prose, e.g. `at every genus; all currents $J^a$ have conformal weight~$1$, so ...` and `via $\mathrm{obs}_g=\kappa(\widehat{\fg}_k)\lambda_g$; all currents share conformal weight~$1$, so ...`.

- [MEDIUM] `chapters/examples/kac_moody.tex:1626` — PROBLEM: `for exceptional types. The full shadow obstruction tower data.` is a sentence fragment. FIX: replace `1624-1626` with `These consistency checks determine the remaining shadow obstruction data for the exceptional types.`

- [MEDIUM] `chapters/examples/kac_moody.tex:5787` — PROBLEM: the section opener is a fragment, not a sentence. FIX: replace `5787-5790` with `This section gives the gauge-theoretic interpretation of the affine vertex algebra: its PVA $\lambda$-bracket is the Poisson bracket of 3d holomorphic-topological Chern--Simons theory on $\Sigma \times \mathbb{R}_t$.`

- [LOW] `chapters/examples/kac_moody.tex:18` — PROBLEM: `This is the content of the assertion that gauge theory is simpler than gravity` drops a slogan into an otherwise mathematical opening. FIX: replace `18-21` with `This contrast is precise: for the Virasoro algebra (Chapter~\ref{chap:w-algebras}), no Jacobi relation annihilates the quartic term, so the tower does not terminate.`

- [LOW] `chapters/examples/kac_moody.tex:1635` — PROBLEM: `\label{tab:exceptional-shadow-data}` sits inside a proposition block without a `table`/`caption`, and I found no `\ref{tab:exceptional-shadow-data}` in the TeX tree. FIX: delete line `1635`; if a table reference is actually needed later, wrap the tabular block in a real `table` environment and attach the label to its caption.

- [LOW] `chapters/examples/kac_moody.tex:2370` — PROBLEM: the remark carries two labels, `rem:category-O-affine` and `rem:bgg-kl-bridge`, and I found no `\ref{...}` to either in the TeX tree. This is dead anchor clutter. FIX: keep one canonical label only, preferably `\label{rem:bgg-kl-bridge}`, and delete the other.

- [LOW] `chapters/examples/kac_moody.tex:3017` — PROBLEM: the coined adjective `theorematic` is ugly and repeated at `3175`, `3295`, and `4219`. FIX: replace it with plain words: `main remaining gap` at `3017`, `proved general-rank identification` at `3175`, `no proved equal-rank statement` at `3295`, and `with target the \emph{semisimplified tilting quotient}` at `4219`.

## Summary
Checked: 6074 | Findings: 12 | Verdict: FAIL
tokens used
189,499
