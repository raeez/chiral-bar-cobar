from pathlib import Path
root=Path(__file__).resolve().parents[4]/'research-candidates/cbc_native026/candidate007/cbc'
def change(path,fn):
 p=root/path;s=p.read_text();p.write_text(fn(s))
def region(s,start,end,new):
 a=s.index(start);b=s.index(end,a);return s[:a]+new+'\n\n'+s[b:]
def statement(s,label,new):
 at=s.index('\\label{'+label+'}');a=s.rfind('\\begin{',0,at);b=s.index('\\end{proof}',at)+len('\\end{proof}');return s[:a]+new+s[b:]
change('chapters/examples/w_algebras_deep.tex',lambda s:s.replace('prop:cbc27-collision-map','prop:cbc27-binary'))
change('chapters/examples/w_algebras_framework.tex',lambda s:statement(s,'prop:log-w-modules',r'''\begin{proposition}[Exactness and module invariants]
\label{prop:log-w-modules}
Exactness of a functor between module categories does not by itself imply preservation of indecomposability, projectives, or extension groups.
\end{proposition}
\begin{proof}
The forgetful functor from $\mathbb C[x]$-modules to vector spaces is exact.
The indecomposable module $\mathbb C[x]/(x^2)$ maps to a direct sum of two one-dimensional vector spaces.
Moreover, the free resolution
$0\to\mathbb C[x]\xrightarrow{x}\mathbb C[x]\to\mathbb C\to0$
gives $\operatorname{Ext}^1_{\mathbb C[x]}(\mathbb C,\mathbb C)=\mathbb C$, whereas the corresponding vector-space Ext group vanishes.
Conversely, the exact functor that equips a vector space with zero $x$-action sends the projective object $\mathbb C$ to the nonprojective $\mathbb C[x]$-module $\mathbb C$.
\end{proof}
Thus logarithmic DS comparisons require additional hypotheses on the actual module categories and functors.
The induced-module bar comparison of Theorem~\ref{thm:ds-koszul-intertwine} applies to its stated $C_2$ quotient; it does not assert preservation of logarithmic vertex extensions or projective covers.'''))
change('chapters/examples/kac_moody_framework.tex',lambda s:statement(s,'prop:ds-admissible',r'''\begin{proposition}[An exact functor applied to a resolution]
\label{prop:ds-admissible}
Let $F:\mathcal C\to\mathcal D$ be an exact functor of abelian categories, and let $P^\bullet\to M$ be a resolution in $\mathcal C$.
Then $F(P^\bullet)\to F(M)$ is a resolution in $\mathcal D$.
Identifying it with a specified bar resolution of $F(M)$ requires a chain comparison in $\mathcal D$.
\end{proposition}
\begin{proof}
Exactness preserves the short exact sequences of cycles and boundaries, and hence the vanishing of all nonzero cohomology of the augmented resolution.
It does not specify any map to a different resolution.
\end{proof}
For a DS application, both the precise subcategory on which reduction is exact and membership of every resolution term in that subcategory must be established.
Theorem~\ref{thm:ds-koszul-intertwine} supplies a comparison for its explicitly induced $C_2$-quotient modules.
It makes no claim that general meromorphic bar terms on configuration spaces belong to an admissible affine module category.'''))
change('chapters/examples/kac_moody_framework.tex',lambda s:statement(s,'prop:bar-whittaker',r'''\begin{proposition}[The row-vanishing spectral sequence]
\label{prop:bar-whittaker}
Let $C^{p,q}$ be a first-quadrant double complex of vector spaces, with horizontal and vertical differentials $d_h,d_v$ satisfying $d_hd_v+d_vd_h=0$.
The total complex, with its finite diagonal sums, has a convergent spectral sequence
\begin{equation}\label{eq:whittaker-ss}
 E_1^{p,q}=H^q(C^{p,\bullet},d_v)\ \Longrightarrow\ H^{p+q}(\operatorname{Tot}C).
\end{equation}
If the vertical cohomology vanishes for $q\ne0$, it collapses at $E_2$ and its abutment is the cohomology of the surviving row with the induced $d_h$.
\end{proposition}
\begin{proof}
Filter by $p$.
Each total degree has a finite filtration, so the associated spectral sequence converges without an inverse-limit assumption.
After $E_1$, the only possible differential is the horizontal map on the row $q=0$; all higher differentials have a zero source or target.
\end{proof}
To apply this statement to a BRST and bar construction one must construct the double complex, check its boundedness or replace it by a justified convergent totalization, and identify the surviving row with the desired bar operations.
Vanishing alone does not supply that identification.
The finite-length argument in Theorem~\ref{thm:ds-koszul-intertwine} proves a different, explicit comparison on the subregular associative quotient.'''))
change('chapters/theory/higher_genus.tex',lambda s:region(s,'The genus-by-genus bar complexes assemble into a single spectral sequence',r'\subsection{Spectral sequence = genus expansion}',r'''A genus filtration on a defined total chiral complex gives a spectral sequence once its differential preserves the filtration and the convergence hypotheses are verified.
Its pages depend on that differential and filtration.
Adjoining a BRST differential does not automatically move a collapse from $E_1$ to $E_2$: one must construct the double complex, identify its surviving row, and control its totalization.
Proposition~\ref{prop:bar-whittaker} states a precise row-vanishing criterion.
Theorem~\ref{thm:ds-koszul-intertwine} concerns the subregular associative quotient and supplies no universal collapse page for the full genus filtration.'''))
change('chapters/examples/genus_expansions.tex',lambda s:region(s,r'The $\widehat{\mathfrak{sl}}_2$ genus-$2$ computation',r'\subsection{\texorpdfstring{$\mathcal{W}_3$ genus-2 bar differential}',r'''The Virasoro OPE determines local collision coefficients on a genus-two curve after a coordinate and a meromorphic kernel have been specified.
Turning these coefficients into a global bar differential requires descent, the transition laws of the conformal field, and compatibility at every boundary divisor.

\begin{proposition}[A local Virasoro residue]
\label{thm:virasoro-genus2-bar}
Let $\xi$ be a collision coordinate and $f(\xi)$ a holomorphic germ.
For the universal Virasoro field,
\begin{equation}\label{eq:vir-d2-genus2}
 \operatorname{Res}_{\xi=0}f(\xi)Y(T,\xi)T\,d\xi
 =\frac{c}{12}f^{(3)}(0)\mathbf1+2f'(0)T+f(0)\partial T.
\end{equation}
\end{proposition}
\begin{proof}
The singular OPE is $(c/2)\xi^{-4}\mathbf1+2\xi^{-2}T+\xi^{-1}\partial T$.
Multiplication by the Taylor series of $f$ and extraction of the coefficient of $\xi^{-1}$ gives the formula, including the factor $1/3!$ in the central term.
\end{proof}

\begin{remark}[From local residues to a genus-two class]
\label{cor:virasoro-genus2-curvature}
A formula for a class on $\overline{\mathcal M}_2$ requires a global construction that carries these local residues to cohomology.
For example, a normalized comparison with the Hodge class would have to establish
\begin{equation}\label{eq:vir-obs2}
 \mathrm{obs}_2(\mathrm{Vir}_c)=\frac c2\lambda_2.
\end{equation}
This remains a required identification of classes in this construction; it does not follow from the local coefficient $T_{(3)}T=c/2$ alone.
If that identification and the normalized scalar evaluation $\lambda_2\mapsto7/5760$ are supplied, their composition gives
\begin{equation}\label{eq:vir-F2}
 F_2(\mathrm{Vir}_c)=\frac{7c}{11520}.
\end{equation}
The displayed scalar is the consequence of those two specified maps.
\end{remark}

\begin{remark}[The reduction map and genus-two descent]
\label{rem:virasoro-genus2-ds}
The principal $\mathfrak{sl}_2$ comparison is a map into the full affine--ghost complex with its improved conformal vector.
A genus-two comparison must extend it over the chosen curve and intertwine the specified kernels and their boundary operations.
The associative quotient comparison of Theorem~\ref{thm:ds-koszul-intertwine} does not perform this descent.
\end{remark}'''))
change('chapters/examples/examples_summary.tex',lambda s:region(s,r'\emph{Explanation via DS reduction and Wakimoto.}',r'\end{proof}',r'''\emph{Scope of the generating-function calculation.}
The displayed algebraic functions have the stated common branch locus by their formulas.
This numerical identity does not construct a DS or Wakimoto map between their bar carriers.
BRST cohomology is not, in general, a rational operation on an ungraded generating function: ranks of the differentials must also be known.
Theorem~\ref{thm:ds-koszul-intertwine} supplies an actual comparison only for the specified subregular associative quotient modules.
A corresponding statement for these vertex algebras requires its own map and grading-compatible cohomology calculation.'''))
change('chapters/examples/examples_summary.tex',lambda s:statement(s,'prop:linear-relation-functorial',r'''\begin{proposition}[Linear dependence and an exact triangle]
\label{prop:linear-relation-functorial}
A linear relation among graded Euler characteristics does not by itself produce an exact triangle of the complexes involved.
\end{proposition}
\begin{proof}
Let $X=\mathbb C$ in degree zero and let $Y$ have zero differential with one copy of $\mathbb C$ in degree $-1$ and two copies in degree zero.
Then $\chi(X)=\chi(Y)=1$.
An exact triangle $X\to Y\to0\to X[1]$ would force its first map to be a quasi-isomorphism, but $H^{-1}(X)=0$ and $H^{-1}(Y)=\mathbb C$.
Thus the Euler relation $\chi(Y)=\chi(X)+\chi(0)$ does not supply that triangle.
\end{proof}
In particular, a functorial interpretation of the generating-function relation~\eqref{eq:discriminant-linear-relation} requires actual maps and an identification of their mapping cone.
The desired DS--Wakimoto diagram may be denoted schematically by
\begin{equation}\label{eq:wakimoto-ds-triangle}
 B(\widehat{\mathfrak{sl}}_{2,k})\longrightarrow B(\mathrm{Vir}_c),
 \qquad B(\widehat{\mathfrak{sl}}_{2,k})\longrightarrow B(\beta\gamma\otimes\mathcal H).
\end{equation}
These arrows are construction targets on the full vertex bar carrier, not consequences of the scalar relation.
The actual quotient-level module map in Theorem~\ref{thm:ds-koszul-intertwine} has a different domain and does not construct this triangle.'''))
