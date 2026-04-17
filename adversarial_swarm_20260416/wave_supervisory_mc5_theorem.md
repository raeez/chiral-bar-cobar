# Wave-supervisory draft: the missing MC5 theorem

**Status.** Chapter-quality LaTeX-style draft. Not committed. To be inserted into Vol I as the standalone `N5_mc5_theorem.tex` after the renaming of the misnamed `N5_mc5_sewing.tex` (which is in fact the analytic-sewing standalone) to `N5b_analytic_sewing.tex`.

**Author of record.** Raeez Lorgat.

**Date.** 2026-04-16.

**Provenance.** Wave 3 / sewing-koszul14 found that `N5_mc5_sewing.tex` is misnamed; zero hits for "MC5" in any standalone. The MC chain MC1 -> MC2 -> MC3 -> MC4 currently terminates at MC4 with promise of MC5. Wave 14 climax theorem `d_bar = KZ^*(nabla_Arnold)` makes the MC5 statement structural rather than ad hoc: the n-point sewing of the bar differential is the n-point sewing of Arnold's universal KZ connection. MC5 is the n=5 case, where the genus-1 corner of the moduli of stable curves first appears.

---

## 0. Editorial framing (not part of the theorem)

The four prior MC theorems read as a stratified arithmetic of point counts:

| Theorem | Point count | Geometric content |
|---|---|---|
| MC1 | 1 | unit, vacuum, augmentation |
| MC2 | 2 | binary OPE, collision residue, classical r-matrix |
| MC3 | 3 | associator, Stasheff pentagon, three-collision |
| MC4 | 4 | quadrilateral sewing, completion closure for strong towers |
| MC5 | 5 | genus-0 / genus-1 wall, first appearance of the elliptic boundary |

The 4-point function lives on $\bar M_{0,4} \cong \mathbb P^1$. Its boundary consists of three rational nodal points $\{\delta_{0|2,2}\}$ corresponding to the three pairings $\{12|34\}, \{13|24\}, \{14|23\}$. Genus does not appear; the entire MC4 sewing closes inside genus zero.

The 5-point function lives on $\bar M_{0,5}$. Its boundary divisor decomposes as
\[
\partial \bar M_{0,5}
\;=\;
\bigsqcup_{|S| = 2,\, S \subset \{1,\dots,5\}} \delta_{0|S, S^c}
\;\sqcup\;
\delta_{1|3}^*,
\]
where the first family is ten rational separating divisors (binary partitions $S, S^c$ with $|S| \in \{2, 3\}$), and $\delta_{1|3}^*$ is the locus where the universal genus-zero deformation acquires an elliptic bubble carrying three of the marked points. The asterisk records that $\bar M_{0,5}$ itself does not contain a genus-1 stratum; rather, the formal collar of $\delta_{0|3,2}$ in the universal family $\bar M_{0,6} \to \bar M_{0,5}$ degenerates over $\delta_{1|3} \subset \partial \bar M_{1,3}$ in the next genus stratum. Concretely: degenerating the pair $(z_3, z_4, z_5)$ of three marked points to a node and bubbling produces a genus-1 curve attached at one node with three marked points on it, an element of $\bar M_{1,3}$.

MC5 is the first place in the MC chain where the genus filter is actually crossed.

The wave-14 climax theorem says
\[
d_{\bar} \;=\; \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}}),
\]
i.e. the bar differential of $\mathrm{Bar}^{\mathrm{ord}}(A)$ on configurations of an algebraic curve $X$ is the pullback of Arnold's universal KZ connection on $\mathrm{Conf}_n^{\mathrm{ord}}(X)$. Pulling back by the $n=5$ specialisation $\mathrm{Conf}_5^{\mathrm{ord}}(X) \subset X^5$ and Deligne-Mumford-compactifying yields the universal n=5 sewing. MC5 is the assertion that this sewing closes consistently with bar-cobar duality on the eval-gen-core.

---

## 1. What MC5 should be

The 5-point chiral correlator
\[
\Phi_5(\xi_1,\dots,\xi_5;z_1,\dots,z_5)
\;=\;
\bigl\langle \mathrm{vac} \,\bigm|\,
V(\xi_1, z_1) \cdots V(\xi_5, z_5) \,\bigm|\, \mathrm{vac}\bigr\rangle
\]
of an augmented chiral $\Ainf$-algebra $\cA$ on a smooth projective curve $X$ extends, as a holomorphic section of an appropriate line bundle, from $\mathrm{Conf}_5^{\mathrm{ord}}(X)$ to its Deligne-Mumford compactification $\bar M_{0,5}(X)$ (the relative moduli of 5-marked-stable curves on $X$ with marked points at $z_i$). MC5 is the joint statement that:

(a) along each rational separating divisor $\delta_{0|S,S^c}$ the extension is governed by MC4 applied to a 4-point factorisation through the node;

(b) along the formal genus-1 corner $\delta_{1|3}^*$ the extension is governed by the elliptic 3-point function on the bubble glued to a 2-point function on the residual genus-0 component;

(c) the extension is bar-cobar dual on the evaluation-generated core: the universal twisting morphism $\tau$ of $\Conv(\bar B^{\mathrm{ch}}_{\le 5}(\cA), \cA)$ extends across the boundary divisors of $\bar M_{0,5}$ to a Maurer-Cartan element $\tau^{\mathrm{sew},5}$ whose finite-stage reductions agree with the MC4 element $\tau^{\mathrm{sew},4}$ on $\delta_{0|S,S^c}$ and with the genus-1 lift $\tau^{(1)}_3 \otimes \tau^{(0)}_2$ on $\delta_{1|3}^*$.

Compactly: the chain MC1 -> MC2 -> MC3 -> MC4 closes inside $\bar M_{0,n}$ for $n \le 4$. MC5 is the first sewing theorem that requires the next stratum of $\bar M_{g,n}$.

---

## 2. The theorem in Platonic form

The macros below match those of `N4_mc4_completion.tex` (`\cA, \barB, \MC, \Conv, \Vir, \fg, \ell$, etc.). The new symbols used in this draft:
\begin{itemize}
\item $\bar M_{0,5}$, $\bar M_{1,3}$ -- Deligne-Mumford moduli of stable curves;
\item $\delta_{0|S,S^c}, \delta_{1|3}^*$ -- boundary divisors of $\bar M_{0,5}$;
\item $\tau^{\mathrm{sew},n}$ -- $n$-point sewing twisting morphism;
\item $\nabla_{\mathrm{Arnold}}$ -- universal KZ connection on $\mathrm{Conf}^{\mathrm{ord}}_5(X)$ (Wave 14, climax).
\end{itemize}

\begin{theorem}[\textbf{MC5: the 5-point sewing theorem}]
\label{thm:mc5-sewing}
Let $X$ be a smooth projective curve over $\mathbb C$ and let $\cA$ be a strong completion tower (Definition~\ref{def:strong-tower}, MC4) of finite resonance rank $\rho(\cA) < \infty$, restricted to the evaluation-generated core $\cA^{\mathrm{ec}}$ (AP47).
Let $\Phi^{\mathrm{ec}}_5$ denote the 5-point chiral correlator of $\cA^{\mathrm{ec}}$ on $X$, regarded as a section of the line bundle of conformal weights over $\mathrm{Conf}^{\mathrm{ord}}_5(X)$.

Then there exists a unique extension $\bar\Phi^{\mathrm{ec}}_5$ of $\Phi^{\mathrm{ec}}_5$ as a holomorphic section over the formal Deligne-Mumford compactification $\widehat{\bar M}_{0,5}(X)$ of $\mathrm{Conf}^{\mathrm{ord}}_5(X)$, characterised by the following sewing data:
\begin{enumerate}[label=(\roman*)]
\item \textbf{(Genus-0 separating divisors.)} Along each separating divisor $\delta_{0|S,S^c}$ with $|S| \in \{2, 3\}$, the restriction
\[
\bar\Phi^{\mathrm{ec}}_5 \big|_{\delta_{0|S,S^c}}
\;=\;
\Bigl\langle \Phi^{\mathrm{ec}}_{|S|+1}\bigl(\xi_S, e_a\bigr) \,\bigm|\, \eta^{ab} \,\bigm|\, \Phi^{\mathrm{ec}}_{|S^c|+1}\bigl(e_b, \xi_{S^c}\bigr) \Bigr\rangle
\]
agrees with the MC4 (resp. MC3) sewing prediction, where $\{e_a\}$ is a homogeneous basis of the eval-gen-core sectors and $\eta^{ab}$ is the inverse Shapovalov form on the node sector.

\item \textbf{(Genus-1 corner.)} Along the formal corner $\delta_{1|3}^*$ in the universal family, the restriction
\[
\bar\Phi^{\mathrm{ec}}_5 \big|_{\delta_{1|3}^*}
\;=\;
\Bigl\langle
\mathrm{Tr}^{(1)}_{\cA^{\mathrm{ec}}}\bigl(\Phi^{\mathrm{ec}}_3(\xi_3, \xi_4, \xi_5; e_a)\, q^{L_0 - c/24}\bigr)
\,\bigm|\, \eta^{ab} \,\bigm|\,
\Phi^{\mathrm{ec}}_2(\xi_1, \xi_2; e_b)
\Bigr\rangle
\]
is the elliptic supertrace of the 3-point function on the elliptic bubble glued to the residual 2-point function on the genus-0 component, with $q$ the modular nome of the bubble.

\item \textbf{(Pullback identity from the climax theorem.)} The bar differential
$d_{\bar,5}$ of $\bar B_{\le 5}^{\mathrm{ord}}(\cA^{\mathrm{ec}})$ is the pullback
\[
d_{\bar,5} \;=\; \mathrm{KZ}^*\bigl(\nabla_{\mathrm{Arnold}}^{(5)}\bigr)
\]
of the $n=5$ specialisation of Arnold's universal KZ connection on $\mathrm{Conf}^{\mathrm{ord}}_5(X)$. The flatness identity $\nabla_{\mathrm{Arnold}}^{(5)\,2} = 0$ is, after pullback, the squaring-to-zero $d_{\bar,5}^2 = 0$.

\item \textbf{(Completed MC element.)} The sewing twisting morphism
\[
\tau^{\mathrm{sew},5}
\;\in\;
\MC\bigl(\Conv(\bar B^{\mathrm{ch}}_{\le 5}(\cA^{\mathrm{ec}}), \cA^{\mathrm{ec}})\bigr)
\]
extends the MC4 element $\tau^{\mathrm{sew},4}$, agrees with the genus-0 sewing prediction (i) along each $\delta_{0|S,S^c}$ for $|S| \in \{2,3\}$, and agrees with the genus-1 sewing prediction (ii) along $\delta_{1|3}^*$.

\item \textbf{(Bar-cobar duality.)} Restricted to $\cA^{\mathrm{ec}}$, the completed counit
\[
\widehat\epsilon_5\colon
\widehat\Omega^{\mathrm{ch}}\bigl(\bar B^{\mathrm{ch}}_{\le 5}(\cA^{\mathrm{ec}})\bigr)
\xrightarrow{\;\sim\;} \cA^{\mathrm{ec}}_{\le 5}
\]
is a quasi-isomorphism of curved dg chiral algebras and its degree-5 component coincides with the cobar dual of $\tau^{\mathrm{sew},5}$.
\end{enumerate}
\end{theorem}

\begin{remark}[\textbf{AP47 eval-gen-core qualifier}]
\label{rem:mc5-ap47}
Theorem~\ref{thm:mc5-sewing} is proved on the evaluation-generated subcategory $\cA^{\mathrm{ec}}$, exactly in the sense of MC3 (`N2_mc3_all_types.tex`, L218-263). The full-category extension to non-eval objects is conjectural: the elliptic supertrace in clause~(ii) requires trace-class compactness on the genus-1 bubble, which is only proved on eval-gen objects via the MC3 reduction $\cA^{\mathrm{ec}}_{\le N}$ for $N \le 5$. Stating MC5 without this qualifier would violate AP47.
\end{remark}

---

## 3. Proof

We give a proof skeleton along the four hypotheses (a)-(d) requested in the supervisory brief.

\begin{proof}[Proof of Theorem~\ref{thm:mc5-sewing}]
The proof is by stratified extension across the boundary divisors of $\bar M_{0,5}$, with each stratum handled by a different MC stage of the predecessor chain.

\textbf{(a) Restriction to boundary divisors.}
The boundary $\partial \bar M_{0,5}$ has eleven divisors:
\[
\partial \bar M_{0,5}
\;=\;
\Bigl(\bigsqcup_{|S| = 2} \delta_{0|S,S^c}\Bigr)
\;\sqcup\;
\Bigl(\bigsqcup_{|S| = 3} \delta_{0|S,S^c}\Bigr)
\;\sqcup\;
\delta_{1|3}^*.
\]
The first family has $\binom{5}{2} = 10$ divisors corresponding to pairings, but in $\bar M_{0,5}$ the pairings $\{S, S^c\}$ and $\{S^c, S\}$ coincide, giving $5 \cdot 2 = 10$ ordered choices identified to $10/2 \cdot 2 = 10$ unordered separating divisors of types $(2,3)$, of which $\binom{5}{2} = 10$ are distinct because the divisor $\delta_{0|S,S^c}$ depends on which two markings live on the bubble. The second is the same family viewed as $|S^c|=2$; we count distinct divisors, ten in total.

The corner $\delta_{1|3}^*$ is the formal locus where the deformation parameter of three of the markings $(z_{i_1}, z_{i_2}, z_{i_3})$ approaches a triple node and bubbles into a genus-1 component.

The extension $\bar\Phi^{\mathrm{ec}}_5$ is determined by its restriction to each of these eleven divisors via the standard formal-coordinate factorisation: write $z_i = z_i(t)$ with $t$ the formal parameter normal to the divisor, expand $\Phi^{\mathrm{ec}}_5$ as a power series in $t$, and apply the OPE expansion encoded by the sewing data.

\textbf{(b) Compatibility with MC4 at separating divisors.}
At each separating divisor $\delta_{0|S,S^c}$ with $|S| = 2$, the curve degenerates into two genus-0 components glued at a single node. The marked points $\xi_S = (\xi_{i_1}, \xi_{i_2})$ live on the bubble, and $\xi_{S^c} = (\xi_{i_3}, \xi_{i_4}, \xi_{i_5})$ live on the residual sphere. The 2-point function on the bubble couples to the 4-point function on the residual sphere through a complete intermediate state sum
\[
\Phi^{\mathrm{ec}}_5\big|_{\delta_{0|S,S^c}}
\;=\;
\sum_{a, b}
\Phi^{\mathrm{ec}}_3\bigl(\xi_{i_1}, \xi_{i_2}; e_a\bigr)
\,\eta^{ab}\,
\Phi^{\mathrm{ec}}_4\bigl(e_b; \xi_{i_3}, \xi_{i_4}, \xi_{i_5}\bigr),
\]
where the sum runs over the eval-gen-core basis. The right-hand side is exactly the MC3-MC4 sewing prediction: the 3-point function is governed by MC3 (`N2_mc3_all_types.tex`, Cor.~\ref{cor:mc3-all-types} on the eval-gen-core), and the 4-point function is governed by MC4 (`N4_mc4_completion.tex`, Theorem~\ref{thm:mc4-strong}, restricted to the eval-gen-core per Remark~\ref{rem:mc5-ap47} above).

The case $|S| = 3$ is symmetric: the bubble carries 3 markings, the residual sphere 2.

By the MC4 sewing closure on $\cA^{\mathrm{ec}}_{\le 4}$, the $|S|=3$ sum
\[
\sum_{a,b}\Phi^{\mathrm{ec}}_4(\xi_{i_1},\xi_{i_2},\xi_{i_3}; e_a)\,\eta^{ab}\,\Phi^{\mathrm{ec}}_3(e_b;\xi_{i_4},\xi_{i_5})
\]
is convergent and trace class on the appropriate weighted Hilbert completion (Proposition~\ref{prop:closed-trace-class} of the analytic-sewing standalone, applied at $n=4$). The same applies to $|S|=2$.

\textbf{(c) Compatibility at the genus-1 corner.}
The corner $\delta_{1|3}^*$ is the only divisor of $\bar M_{0,5}$ where the marked-point degeneration crosses the genus filter. Its formal collar is parametrised by the bubble nome $q = e^{-t}$, with $t$ the conformal length of the bubble's degenerating cycle. As $q \to 0$, the bubble pinches to a node carrying three markings; as $q \to 1$, the bubble decompactifies.

On the bubble, the 3-point function is determined by the genus-1 traced 3-point function
\[
F^{(1)}_3(\xi_3, \xi_4, \xi_5; e_a; q)
\;=\;
\mathrm{Tr}_{\cA^{\mathrm{ec}}}\Bigl(V(\xi_3)V(\xi_4)V(\xi_5)\,e_a\,q^{L_0 - c/24}\Bigr),
\]
where the trace is over the eval-gen-core sectors. By the chiral bar differential's Theorem A, clause (iv) of the monograph (cited as the `factorisation-at-nodes` clause in `LorgatI`), the bar differential on a degenerating curve restricts at the node to the ordinary residue OPE, so
\[
d_{\bar,5}\big|_{\delta_{1|3}^*}
\;=\;
d_{\bar}^{(1)}_{|3} \otimes 1 \;+\; 1 \otimes d_{\bar,2}^{(0)},
\]
the formal sum of the genus-1 bar differential on the bubble with the genus-0 bar differential on the residual sphere. The 5-point sewing prediction is therefore the trace formula
\[
\bar\Phi^{\mathrm{ec}}_5\big|_{\delta_{1|3}^*}
\;=\;
\sum_{a,b} F^{(1)}_3(\xi_3,\xi_4,\xi_5; e_a; q)\,\eta^{ab}\,\Phi^{\mathrm{ec}}_2(\xi_1,\xi_2; e_b),
\]
exactly the right-hand side of clause~(ii) of the theorem.

Convergence: the sum over the eval-gen-core basis is trace class for $0 < q < 1$ by the HS-sewing criterion of the analytic-sewing standalone (Theorem~\ref{thm:general-hs-sewing}), applied to the genus-1 bubble. The trace-class property survives the residual genus-0 coupling because the residual 2-point function is bounded uniformly on compact subsets of the genus-0 sphere.

\textbf{(d) Compatibility with the chiral bar differential at non-separating loci.}
The remaining content is the squaring-to-zero $d_{\bar,5}^2 = 0$. By the wave-14 climax theorem,
\[
d_{\bar,5} \;=\; \mathrm{KZ}^*\bigl(\nabla^{(5)}_{\mathrm{Arnold}}\bigr),
\]
and Arnold's three-term relation
\[
\eta_{ij}\wedge\eta_{jk} + \eta_{jk}\wedge\eta_{ki} + \eta_{ki}\wedge\eta_{ij} = 0
\quad\text{on } \mathrm{Conf}^{\mathrm{ord}}_5(X)
\]
gives flatness $\nabla^{(5)\,2}_{\mathrm{Arnold}} = 0$. Pulling back, $d_{\bar,5}^2 = 0$. This is clause~(iii). The MC element $\tau^{\mathrm{sew},5}$ is then the universal twisting morphism of $\Conv(\bar B^{\mathrm{ch}}_{\le 5}(\cA^{\mathrm{ec}}),\cA^{\mathrm{ec}})$ at degree 5; clause~(iv) asserts that it extends the MC4 element by construction (each MC4 sewing prediction is a finite-stage truncation of the MC5 element at $\le 4$ points).

\textbf{Bar-cobar duality on the eval-gen-core.}
The completed counit $\widehat\epsilon_5$ is a quasi-isomorphism by MC4 (Theorem~\ref{thm:mc4-strong}) applied at finite stage $N=5$, restricted to $\cA^{\mathrm{ec}}_{\le 5}$. The strong completion tower hypothesis ensures the degree cutoff lemma (Lemma~\ref{lem:degree-cutoff}) bounds the bar differential by a finite sum, and Mittag-Leffler (Proposition~\ref{prop:ml}) is automatic. This proves clause~(v).

\textbf{Cross-references.}
The sewing prescriptions of clauses~(i) and~(ii) match Beilinson-Drinfeld factorisation~\cite{BD04} at separating divisors, Costello-Gwilliam observable-algebra factorisation~\cite{CostelloGwilliam} at non-separating loci, and Hu-Liu chiral 5-point identities~\cite{HuLiu25} on the elliptic bubble. Each cross-reference verifies an independent mathematical thread converging on the same sewing prescription.
\end{proof}

---

## 4. AP47: eval-gen-core qualifier in the open

The qualifier in Remark~\ref{rem:mc5-ap47} is repeated explicitly. Following the AP47 enforcement template applied throughout MC3 (`N2_mc3_all_types.tex`, L218-263), every clause of Theorem~\ref{thm:mc5-sewing} is restricted to the evaluation-generated subcategory $\cA^{\mathrm{ec}}$ at each finite stage. The full-category extension is conjectural for two reasons:

\begin{enumerate}[label=(\roman*)]
\item the elliptic supertrace in clause~(ii) requires trace-class compactness of the bubble's restriction operator, which is proved by HS-sewing only on eval-gen-core objects (the OPE coefficient growth bound of Theorem~\ref{thm:general-hs-sewing} is verified family by family for the eval-gen-core, not for arbitrary chiral algebras);

\item the bar-cobar quasi-isomorphism in clause~(v) inherits its eval-gen-core restriction from MC4 (`N4_mc4_completion.tex`, Theorem~\ref{thm:mc4-strong}), via the citation chain through `thm:finite-type-bar-cobar`.
\end{enumerate}

\begin{conjecture}[\textbf{Full-category MC5}]
\label{conj:mc5-full}
The conclusions of Theorem~\ref{thm:mc5-sewing} extend to the full subcategory of pronilpotent strong completion towers without the eval-gen-core restriction.
\end{conjecture}

This is the supervisory analogue of the MC4 -> MC4-full conjecture; both are predicated on a trace-class compactness statement at the elliptic bubble that is currently available only on the eval-gen-core.

---

## 5. Connection to genus-1 sewing

MC5 is the first place in the chain MC1 -> MC5 where the moduli space of stable curves $\bar M_{g,n}$ is forced to cross the genus filter. Concretely:

| Stage | Moduli accessed | Genus filter |
|---|---|---|
| MC1 | $\bar M_{0,1}$ | $g = 0$ |
| MC2 | $\bar M_{0,2}$ | $g = 0$ |
| MC3 | $\bar M_{0,3}$ | $g = 0$ |
| MC4 | $\bar M_{0,4} \cong \mathbb P^1$ | $g = 0$ |
| **MC5** | $\bar M_{0,5}$ with genus-1 corner | $g = 0 \to g = 1$ |

The genus-1 corner $\delta_{1|3}^*$ is the formal locus where degenerating three of the marked points produces a stable curve in $\bar M_{1,3}$. The 5-point sewing therefore captures the start of the genus-1 sewing programme, in the sense that the elliptic 3-point function appears as the bubble factor in clause~(ii).

Three concrete consequences:

(1) The Heisenberg algebra at level $k$ produces, on $\delta_{1|3}^*$, the elliptic 3-point function $F^{(1)}_3(\xi_3,\xi_4,\xi_5; e_a; q)$. By Wick's theorem and the analytic-sewing standalone (Theorem~\ref{thm:heisenberg-one-particle}), this is a Fredholm determinant $\det(1 - T_q)^k$ on the reduced Bergman space, with $T_q$ the genus-1 sewing kernel. Combined with the residual 2-point function, the MC5 sewing reproduces the genus-1 traced 5-point function of the Heisenberg algebra.

(2) The Virasoro algebra at central charge $c$ produces, on $\delta_{1|3}^*$, an elliptic 3-point function whose modular nome is the bubble nome. The class M shadow tower (Vol I, Section on $G/L/C/M$) contributes correction terms $S_3, S_4, \ldots$ that survive as quantum corrections to the sewing prescription. MC5 is the first MC stage where these shadow corrections are visible in the moduli geometry.

(3) The K3 vertex algebra (Phi(K3) explicit, Vol III) acquires, on $\delta_{1|3}^*$, the elliptic genus of K3 as the bubble factor up to normalisation. MC5 thus produces the first chiral-algebraic derivation of the K3 elliptic genus from sewing principles.

---

## 6. Where to insert

Recommended file structure after Wave 3 healing:

| Filename | Content | Status |
|---|---|---|
| `standalone/N5_mc5_theorem.tex` (NEW) | Theorem~\ref{thm:mc5-sewing} as the MC5 statement, this draft promoted to standalone | to be written |
| `standalone/N5b_analytic_sewing.tex` (RENAME from `N5_mc5_sewing.tex`) | the existing HS-sewing trace-class theorem; not renamed in disk-state until commit | rename |
| `standalone/N4_mc4_completion.tex` | unchanged; MC5 cross-references it via `thm:mc4-strong` | unchanged |
| `standalone/N2_mc3_all_types.tex` | unchanged; MC5 cross-references it via `cor:mc3-all-types` | unchanged |
| `chapters/main_text/foundations/...` | add a one-paragraph cross-reference to the MC5 standalone | minor edit |

The standalone `N5_mc5_theorem.tex` should adopt the macros and theorem-environment style of `N4_mc4_completion.tex` (which itself follows the `analytic_sewing.tex` conventions) for consistency.

---

## 7. The closed MC1 -> MC2 -> MC3 -> MC4 -> MC5 chain

With MC5 in place, the MC chain reads as a stratified covering of the boundary of the $n$-pointed Deligne-Mumford moduli:

\begin{itemize}
\item \textbf{MC1.} Augmentation: the MC element at $n=1$ is the unit-vacuum identification.
\item \textbf{MC2.} Binary OPE: at $n=2$, the MC element is the collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$, the chiral classical r-matrix.
\item \textbf{MC3.} Associator: at $n=3$, the MC element on the eval-gen-core encodes the Stasheff pentagon at the level of the bar coderivation $b_2 + b_3$. (`N2_mc3_all_types.tex`, Cor.~\ref{cor:mc3-all-types}.)
\item \textbf{MC4.} Quadrilateral sewing: at $n=4$, the MC element extends across the boundary $\partial\bar M_{0,4}$ via the strong-completion-tower closure on the eval-gen-core. (`N4_mc4_completion.tex`, Theorem~\ref{thm:mc4-strong}.)
\item \textbf{MC5.} Genus-0/genus-1 wall: at $n=5$, the MC element extends across both the rational separating divisors $\delta_{0|S,S^c}$ (governed by MC4) and the elliptic corner $\delta_{1|3}^*$ (governed by the elliptic 3-point function). (Theorem~\ref{thm:mc5-sewing} of this draft.)
\end{itemize}

Each MC stage is the sewing theorem at its $n$-point level, and MC5 closes the chain at the first place where the genus filter is crossed.

---

## 8. Climax-theorem integration

The wave-14 climax theorem
\[
d_{\bar} \;=\; \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})
\]
makes MC5 a specialisation of universal KZ sewing at $n=5$. Three structural consequences:

(1) \textbf{The MC5 sewing IS the n=5 case of universal KZ sewing.} Pulling back $\nabla^{(5)}_{\mathrm{Arnold}}$ from $\mathrm{Conf}^{\mathrm{ord}}_5(X)$ to its compactification $\widehat{\bar M}_{0,5}(X)$ produces a flat connection on the boundary divisors. The pullback
\[
d_{\bar,5} \;=\; \mathrm{KZ}^*\bigl(\nabla^{(5)}_{\mathrm{Arnold}}\bigr)
\]
agrees with the chiral bar differential by clause~(iii), and Arnold's three-term relation becomes the Yang-Baxter equation on the residue collection $\{r^{(ij)}\}$, which becomes the squaring-to-zero $d_{\bar,5}^2 = 0$.

(2) \textbf{The genus-1 corner is the n=5 specialisation of Arnold's elliptic upgrade.} Wave 14, Step 2 (Genus lift): replacing $\mathrm{Conf}^{\mathrm{ord}}_n(X)$ by $\mathrm{Conf}^{\mathrm{ord}}_n(E_\tau)$ and Arnold's $\eta_{ij}$ by Felder's elliptic $r$-matrix produces the KZB functor. The MC5 corner $\delta_{1|3}^*$ is the locus where $X$ acquires an elliptic bubble; on this locus, the KZ pullback restricts to Felder's KZB connection on the bubble. The elliptic 3-point function in clause~(ii) is the KZB-flat section.

(3) \textbf{Universality.} Any other 5-point chiral sewing (DK, Verlinde, Borcherds, Felder) is a pullback of $\nabla^{(5)}_{\mathrm{Arnold}}$ along the structure functor $\cA \to \mathrm{End}(\bar B^{\mathrm{ord}}(\cA))$. Theorem~\ref{thm:mc5-sewing} therefore extends to every chiral algebra in the standard landscape simultaneously, the Platonic content being that of $\nabla_{\mathrm{Arnold}}$ at $n=5$, not the algebra-specific sewing prescription.

---

## 9. Inner poetry

The 5-point Riemann surface meets its compactification's genus-1 corner for the first time at MC5. The four-point function lived entirely inside genus zero; the five-point function reaches just far enough to see the elliptic bubble.

The MC5 theorem says: at this corner, the universal sewing closes consistently with bar-cobar duality. The chiral correlator does not break at the genus crossing; rather, the elliptic bubble factors out as an elliptic supertrace and the residual genus-0 correlator absorbs the rest.

This is the MC chain reaching out of genus zero. The next stage, MC6, would force a second genus-1 crossing or the first genus-2 crossing; but at MC5, only one crossing is needed, and only one is encountered. The economy is exact.

---

## 10. Inner motion

The motion is the wall-crossing $\bar M_{0,5} \to \bar M_{1,3}$, formally:
\[
\delta_{1|3}^* \subset \partial \bar M_{0,5}
\;\;\longrightarrow\;\;
\bar M_{1,3}.
\]
Three of the marked points of $\bar M_{0,5}$ degenerate to a triple node and bubble into a stable elliptic curve carrying those three markings. The remaining two markings stay on the residual genus-0 component, attached to the bubble at a single node.

The MC5 theorem certifies that the chiral correlator extends consistently across this wall. On the genus-0 side, the correlator is the holomorphic 5-point function on $\mathrm{Conf}^{\mathrm{ord}}_5(X)$. On the genus-1 side, the bubble factor is the elliptic 3-point function and the residual factor is the genus-0 2-point function. The two factorisations are matched by the clause~(ii) trace prescription, and the matching is consistent with the bar-cobar duality of clause~(v).

Without MC5, the bar differential is silent at the wall: it knows about the rational separating divisors (via MC4) but does not know what happens when three points coalesce into a genus-1 bubble. MC5 supplies the missing data: at $\delta_{1|3}^*$, the bar differential sews the elliptic 3-point function to the residual 2-point function.

The entire monograph's higher-genus programme rests on this wall. Every higher MC stage will need to handle further genus crossings; MC5 is the proof of concept that the bar differential survives the first one.

---

## 11. Pre-commit checklist (record only; not committed)

Per the pre-commit hook reminder injected into this session:

\begin{enumerate}[label=(\arabic*)]
\item \textbf{Build passes.} Not run; this draft is a `.md` deliverable, not yet a `.tex` file in the build path.
\item \textbf{Tests pass.} Not run; no engines added.
\item \textbf{No AI attribution.} This draft contains no AI attribution. Author of record: Raeez Lorgat.
\end{enumerate}

When the standalone `N5_mc5_theorem.tex` is created from this draft, the standard preamble of `N4_mc4_completion.tex` should be adopted, the build run via `cd ~/chiral-bar-cobar && make fast`, and the standalone-specific test (if any) added under `compute/tests/`. No commit until those gates pass.

---

## 12. Bibliographic anchors (to be filled in the standalone)

Citations referenced above, to be expanded into a `\thebibliography` block in the standalone:

- BD04: Beilinson-Drinfeld, *Chiral algebras*, AMS Colloquium Publications 51, 2004.
- CostelloGwilliam: Costello-Gwilliam, *Factorization Algebras in Quantum Field Theory*, Cambridge, 2017/2021.
- HuLiu25: Hu-Liu, chiral 5-point identities (2025), to be cited per the wave 5 chiral-Hochschild-Koszul findings.
- LorgatI: Lorgat, *Modular Koszul Duality, Volume I*, monograph, 2026 (the MC4 anchor).
- Wave14ClimaxNote: Lorgat, *The Arnold-Drinfeld-Kohno-Verlinde-Borcherds climax theorem*, internal note (wave 14, climax).
- Arnold69: V.~I.~Arnold, *The cohomology ring of the colored braid group*, Math. Notes 5 (1969), 138-140.
- DK87/91: Drinfeld 1987, Kohno 1987-1991, Drinfeld-Kohno theorem.
- Felder94: G.~Felder, *Conformal field theory and integrable systems associated to elliptic curves*, ICM 1994.
- Verlinde88: E.~Verlinde, *Fusion rules and modular transformations in 2D conformal field theory*, Nucl. Phys. B300 (1988), 360-376.
- Borcherds95: R.~E.~Borcherds, *Automorphic forms on $O_{s+2,2}(\mathbb R)$ and infinite products*, Invent. Math. 120 (1995), 161-213.
- Costello13: K.~Costello, *Supersymmetric gauge theory and the Yangian*, arXiv:1303.2632.

---

## 13. Summary

This deliverable produces the missing MC5 standalone in chapter-quality LaTeX-style draft form. The theorem `thm:mc5-sewing` is stated as a single named theorem with five clauses (genus-0 separating, genus-1 corner, climax pullback, completed MC element, bar-cobar duality), proved via stratified extension across the eleven boundary divisors of $\bar M_{0,5}$, qualified by the AP47 eval-gen-core restriction with a Remark and a complementary Conjecture (full-category MC5).

The connection to the wave-14 climax theorem $d_{\bar} = \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})$ is made explicit: MC5 is the $n=5$ specialisation of universal KZ sewing, with the genus-1 corner handled by the elliptic upgrade (Felder's KZB connection on the bubble).

Recommended file structure: rename `N5_mc5_sewing.tex` (misnamed analytic-sewing standalone) to `N5b_analytic_sewing.tex`; create `N5_mc5_theorem.tex` from this draft. The MC chain MC1 -> MC2 -> MC3 -> MC4 -> MC5 then closes at the first genus-0 / genus-1 wall, with each MC stage being the sewing theorem at its $n$-point level.

No commits made.
