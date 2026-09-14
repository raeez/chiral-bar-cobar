from pathlib import Path
root=Path(__file__).resolve().parents[4]/'research-candidates/cbc_native026/candidate007/cbc'
def change(path,fn):
 p=root/path;s=p.read_text();p.write_text(fn(s))
def region(s,start,end,new):
 a=s.index(start);b=s.index(end,a);return s[:a]+new+'\n\n'+s[b:]
def statement(s,label,new):
 at=s.index('\\label{'+label+'}')
 a=s.rfind('\\begin{',0,at)
 # All selected statements have an immediately following proof.
 b=s.index('\\end{proof}',at)+len('\\end{proof}')
 return s[:a]+new+s[b:]
change('chapters/theory/chiral_modules.tex',lambda s:region(s,r'\begin{theorem}[DS reduction intertwines',r'\section{Genus-graded module categories}',r'''\begin{theorem}[Module bars after the subregular Poisson quotient]
\label{thm:ds-koszul-intertwine}
For the explicitly augmented differential associative algebras
$A_R=R[J,U,p,v_0]$ and $K_R=R_{C_R}$, and any differential $A_R$-module $M$, there are chain quasi-isomorphisms
\begin{equation}\label{eq:ds-kd-square}
 B(A_R;M)\ \rightleftarrows\ B(K_R;K_R\otimes_{A_R}M).
\end{equation}
They are the tensorwise maps of Theorem~\ref{thm:cbc28-module-bar}, compatible with the bar comodule structures.
For the augmentation module, they give
\begin{equation}\label{eq:ds-bar-commute}
 H^{-n}B(K_R;K_R\otimes_{A_R}R)\simeq\Lambda_R^nR^4.
\end{equation}
\end{theorem}
\begin{proof}
The explicit polynomial coordinate change gives the $A_R$-linear contraction of $K_R$ onto $A_R$.
Theorem~\ref{thm:cbc28-module-bar} extends it to the module bars using finite tensor length.
Corollary~\ref{cor:cbc28-bar-cohomology} computes the augmentation case.
\end{proof}

A comparison for general affine vertex modules on a curve must additionally construct the configuration-space bar operations, the reduction functor on their coalgebra targets, and the natural comparison map.
Vanishing of DS cohomology on an individual module does not establish vanishing on meromorphic sections over configuration spaces or their completed totalization.
The normal-product obstruction~\eqref{eq:cbc28-associator} also prevents replacing those operations by an ordinary associative bar on the unreduced states.

\begin{proposition}[The coefficientwise Euler identity]
\label{cor:ds-character-compatibility}
Suppose a BRST complex $C^\bullet$ has an auxiliary weight grading, each weight subcomplex is bounded and finite-dimensional, and $H^j(C)=0$ for $j\ne0$.
Then, coefficientwise in that grading,
\begin{equation}\label{eq:ds-character}
 \operatorname{ch}H^0(C)=\sum_j(-1)^j\operatorname{ch}C^j.
\end{equation}
\end{proposition}
\begin{proof}
For each weight, the exact sequences of cycles and boundaries cancel their dimensions in the finite alternating sum.
Only cohomology remains, and the hypothesis puts it in degree zero.
\end{proof}
The identity uses the actual affine and ghost gradings.
It supplies no formula obtained by dividing an affine character by a finite root product unless that product has separately been proved to be the relevant ghost supercharacter.

\begin{remark}[Reduction and a reflected cobar target]
\label{cor:ds-bar-level-shift}
The full-vertex comparison sought at the algebra level is
\begin{equation}\label{eq:ds-bar-level-shift}
 H^0_{\mathrm{DS}}\bigl(B^{\mathrm{ch}}(V^k(\mathfrak g))\bigr)
 \simeq B^{\mathrm{ch}}(\mathcal W^k(\mathfrak g)).
\end{equation}
This equation requires defined curved bar targets and a natural comparison; it is not implied by~\eqref{eq:ds-kd-square}.
A reflected conclusion would further require a compatible cobar map to
\begin{equation}\label{eq:ds-cobar-dual}
 \mathcal W^{k'}(\mathfrak g),\qquad k'=-k-2h^\vee.
\end{equation}
In the subregular $\mathfrak{sl}_3$ case, Proposition~\ref{prop:cbc28-nonembedding} excludes simultaneous vertex augmentations at these two levels.
Thus an augmented comparison on that full carrier cannot supply the proposed reflection.
A curved construction must specify its additional operations and their compatibility with reduction.
\end{remark}'''))
change('chapters/theory/chiral_modules.tex',lambda s:s.replace(r'''The Koszul dual level
shift $k \mapsto -k - 2h^\vee$ commutes with DS
(Theorem~\ref{thm:ds-koszul-intertwine}), so the conformal block
duality of Proposition~\ref{prop:conformal-block-duality} descends
through the BRST reduction.''',r'''A reflected conformal-block comparison would require a reduction map compatible with the global coinvariant functors and the reflected vertex carrier.
Theorem~\ref{thm:ds-koszul-intertwine} concerns the explicitly stated associative $C_2$-quotient modules and supplies no such global descent.'''))
change('chapters/examples/w_algebras_deep.tex',lambda s:region(s,r'\begin{remark}[DS reduction as Koszul duality datum:',r'\subsection{\texorpdfstring{$\mathcal{W}_3$ bar complex: degree-3 computation}',r'''\begin{remark}[Reduction and bar operations]
\label{rem:ds-is-the-duality-datum}
A BRST resolution and a bar construction have different defining operations.
The former uses an odd derivation of the affine--ghost vertex algebra; the latter must specify multiplication, collision coefficients, and its coalgebra differential.
For the subregular algebra, the full vertex inclusion is Theorem~\ref{thm:cbc27-subregular-map}, while the associative quotient and its module bars are Theorems~\ref{thm:cbc28-c2-reduction} and~\ref{thm:ds-koszul-intertwine}.
The nonzero normal-product associator explains why these two constructions cannot be identified before taking the quotient.
Neither orbit transpose nor the affine level reflection supplies the missing curved coalgebra map.
\end{remark}

\subsection{DS reduction and the vacuum products}
\label{sec:ds-bar-intertwining}

\begin{computation}[A scalar test for a proposed principal comparison]
\label{comp:ds-bar-sl3-w3}
For the principal $\mathfrak{sl}_3$ reduction, the DS charge is
$c_{\mathrm{DS}}=2-24(k+2)^2/(k+3)$, whereas the affine Sugawara charge is $c_{\mathrm{aff}}=8k/(k+3)$.
At $k=0$, these are $-30$ and $0$.
Consequently a rule that sends the affine Sugawara field to the principal conformal field cannot preserve its third product:
\[
 (S_{\mathrm{aff}})_{(3)}S_{\mathrm{aff}}=0,\qquad
 (T_{\mathrm{DS}})_{(3)}T_{\mathrm{DS}}=-15\mathbf1.
\]
A unital vertex map preserving these named fields would force $0=-15\mathbf1$.
An actual DS construction uses ghosts and a conformal improvement; it cannot replace these data by a projection of affine currents onto the principal strong generators.
For subregular $\mathfrak{sl}_3$, the precise improvement and its BRST homotopy are~\eqref{eq:cbc27-stress-homotopy}.
The affine-chart collision map of Proposition~\ref{prop:cbc27-collision-map} then preserves every individual mode product.
This modewise statement has an explicit carrier and does not assert a completed bar comparison.
\end{computation}'''))
# These two references use the actual labels present in the preceding construction.
p=root/'chapters/theory/subregular_ds.tex'
print('stress/collision labels:',[l for l in p.read_text().splitlines() if '\\label{' in l and ('stress' in l or 'collision' in l)])
# Consistent object type for the revised target definition.
for p in root.rglob('*.tex'):
 s=p.read_text();t=s.replace(r'Proposition~\ref{prop:winfty-factorization-package}',r'Definition~\ref{prop:winfty-factorization-package}').replace(r'Proposition~\textup{\ref{prop:winfty-factorization-package}}',r'Definition~\textup{\ref{prop:winfty-factorization-package}}')
 if t!=s:p.write_text(t)
change('chapters/theory/bar_cobar_construction.tex',lambda s:region(s,r'\begin{remark}[Transition maps for the',r'\begin{proposition}[Higher-spin ideal criterion',r'''\begin{remark}[Transition maps and vacuum terms]
\label{rem:winfty-factorization-route}
The quotient criteria below assume actual ideals and compatible finite-stage maps.
When a generator $W$ has $W_{(5)}W=(c/3)\mathbf1$ with $c\ne0$, the vertex ideal generated by $W$ contains the vacuum.
Its quotient is therefore zero.
Thus deleting the weight-three generator cannot supply the stage-$3$ to stage-$2$ map in a nonzero unital tower with this normalization.
Any alternative factorization target must specify transition data compatible with these vacuum products.
\end{remark}'''))
change('chapters/examples/w_algebras_deep.tex',lambda s:s.replace(r'''The finite-$N$ ingredients
are available from the DS--KD intertwining theorem
(Theorem~\ref{thm:ds-koszul-intertwine}), but the passage to the
colimit involves analytic subtleties (completions, convergence of
the bar differential on infinite-dimensional chain spaces) that
lie outside the algebraic framework of this monograph.''',r'''The finite-stage curved bar maps and the transition maps are themselves required inputs.
Theorem~\ref{thm:ds-koszul-intertwine} proves an associative module comparison only after the subregular $C_2$ quotient.
The full principal limit requires its own collision maps, topology, and convergence proof.'''))
