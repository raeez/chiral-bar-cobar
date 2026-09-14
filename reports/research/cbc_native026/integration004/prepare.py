from pathlib import Path
import shutil,json,re,hashlib
root=Path.cwd();base=root/'research-candidates/cbc_native026/candidate002';dest=root/'research-candidates/cbc_native026/candidate004';report=root/'reports/research/cbc_native026/candidate004';report.mkdir(exist_ok=True)
for d in ['cbc','proof']:
 if not(dest/d).exists():shutil.copytree(base/d,dest/d)
c=dest/'cbc';th=c/'chapters/theory';changes=[]
def edit(p,old,new):
 s=p.read_text();assert old in s,(p,old[:60]);p.write_text(s.replace(old,new));changes.append({'path':str(p.relative_to(dest)),'old':old,'new':new})
aff=Path('/Users/raeez/mathematics/worktrees/frontier-cbc-affine-ds-026-20260914/research-candidates/cbc_affine_ds026/affine_ds.tex');rel=Path('/Users/raeez/mathematics/worktrees/frontier-cbc-relative-p1-026-20260914/research-candidates/cbc_relative_p1026/proof/relative_comparison.tex');uni=rel.parent/'dependencies/unital_chains.tex';ep=root/'research-candidates/cbc_native026/candidate003/proof/elliptic_propagator.tex'
for name,p in [('affine_ds_global',aff),('unital_p1_chains',uni),('relative_p1_comparison',rel),('elliptic_propagator',ep)]:shutil.copyfile(p,th/(name+'.tex'))
edit(th/'affine_ds_global.tex',r'\cite{Arakawa}',r'\cite{AffineDSArakawa026}');edit(th/'affine_ds_global.tex',r'\cite{Frenkel}',r'\cite{AffineDSFrenkel026}')
edit(th/'relative_p1_comparison.tex','Coordinate descent and the differential are specified in the first appendix.',r'Coordinate descent and the differential are specified in Section~\ref{sec:cbc26-unital-p1}.')
edit(th/'elliptic_propagator.tex',r'f,d\bar z',r'f\,d\bar z')
aff_input=r'''\begingroup
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\Vir}{\operatorname{Vir}}
\providecommand{\Aut}{\operatorname{Aut}}
\input{chapters/theory/affine_ds_global}
\endgroup
'''
edit(c/'chapters/examples/w_algebras_framework.tex',r'\input{chapters/theory/reduction_parameters}',r'\input{chapters/theory/reduction_parameters}'+'\n\n'+aff_input)
edit(c/'chapters/examples/w_algebras_framework.tex',r'\subsection{\texorpdfstring{The solution: curved $A_\infty$ Koszul duality}{The solution: curved A infty Koszul duality}}','')
edit(c/'chapters/examples/free_fields.tex',r'\input{chapters/theory/elliptic_normalizations}',r'\input{chapters/theory/elliptic_normalizations}'+'\n\n'+r'\input{chapters/theory/elliptic_propagator}')
edit(c/'chapters/connections/bv_brst.tex',r'\input{chapters/theory/ds_chain_comparisons}',r'''\input{chapters/theory/ds_chain_comparisons}

\section{Unital Virasoro chiral chains on the projective line}
\label{sec:cbc26-unital-p1}
\input{chapters/theory/unital_p1_chains}
\input{chapters/theory/relative_p1_comparison}''')
# Correct the directly reviewed modular example by an actual scalar pairing.
p=c/'chapters/examples/free_fields.tex';s=p.read_text();start=s.index(r'\begin{example}[One-loop two-point amplitude]');end=s.index(r'\end{example}',start)+len(r'\end{example}')
edit(p,s[start:end],r'''\begin{example}[A scalar pairing on a complex torus]
For $f\in C^\infty(E_\tau)$ and $\beta\in\Omega^{0,1}(E_\tau)$, define
\[
 \mathcal P_\tau(f,\beta)=\int_{E_\tau}f\,H_\tau(\beta)\,\nu_\tau,
\]
with $H_\tau$ and $\nu_\tau$ as in Theorem~\ref{thm:ep-homotopy}.
This bilinear functional is well-defined because the kernel is locally integrable and its convolution with a smooth form is smooth.
Under an isomorphism $\phi_\gamma:E_\tau\to E_{\gamma\tau}$,
\[
 \mathcal P_\tau(\phi_\gamma^*f,\phi_\gamma^*\beta)
 =\mathcal P_{\gamma\tau}(f,\beta).
\]
Indeed, both $H$ and the normalized area form commute with pullback, so the identity follows by change of variables.
An amplitude of vertex insertions requires maps from those insertions to the displayed coefficient spaces and compatibility with this pairing.
\end{example}''')
# Keep reflected W comparisons as precise missing constructions, with actual DS map named.
p=c/'chapters/examples/w_algebras_framework.tex';s=p.read_text()
for label,title in [('thm:w-koszul-precise','Reflected and critical W-algebra comparisons'),('thm:w3-koszul-dual','The reflected W-three comparison')]:
 pos=s.index(r'\label{'+label+'}');start=s.rfind(r'\begin{theorem}',0,pos);end=s.index(r'\end{proof}',pos)+len(r'\end{proof}')
 new=r'''\begin{remark}['''+title+r''']\label{'''+label+r'''}
The parameter reflection $k\mapsto-k-2h^\vee$ specifies a proposed curved chiral comparison, as in Remark~\ref{thm:w-algebra-koszul-main}.
The reflected central-charge sum for $\mathfrak{sl}_3$ is $100$ by Proposition~\ref{cor:anomaly-duality-w}.
For $\mathfrak{sl}_2$, Theorem~\ref{thm:affine-comparison} and Proposition~\ref{prop:global-descent} construct the actual noncritical reduction map into the full affine--ghost complex, with its specified coordinate action.
Neither this reduction quasi-isomorphism nor the scalar reflected sum identifies a Koszul dual at the reflected parameter.
Such an identification requires a specified chiral bar construction and a map compatible with its reduction and collision differentials.
At critical level the displayed conformal vector has a pole; specialization requires a family of complexes over the level parameter and a base-change argument.
Feigin--Frenkel reciprocity of shifted parameters is a different transformation from reflection.
\end{remark}'''
 edit(p,s[start:end],new);s=p.read_text()
# Separate actual polynomial BV operator from the unconstructed native residue operator.
p=c/'chapters/theory/koszul_pair_structure.tex';s=p.read_text();start=s.index(r'\begin{theorem}[BV structure on bar complex');end=s.index(r'\end{proof}',start)+len(r'\end{proof}')
edit(p,s[start:end],r'''\begin{proposition}[A polynomial Batalin--Vilkovisky operator]
\label{prop:cbc26-polynomial-laplacian}
On $K=\mathbb C[x_1,\ldots,x_n]\otimes\Lambda(\eta_1,\ldots,\eta_n)$, with $|x_i|=0$ and $|\eta_i|=-1$, use left odd derivatives and put
\[
 \Delta=\sum_i\partial_{x_i}\partial_{\eta_i}.
\]
This operator has degree one, order at most two, and square zero.
Its derived odd bracket has $\{x_i,\eta_j\}=\delta_{ij}$.
For every polynomial $S(x)$, one has $\Delta S=\{S,S\}=0$, and $D=\{S,-\}$ satisfies $D\Delta+\Delta D=0$.
Thus $S$ solves the polynomial quantum master equation $\tfrac12\{S,S\}+\hbar\Delta S=0$.
\end{proposition}
\begin{proof}
The even derivatives commute and distinct odd derivatives anticommute; equal odd derivatives square to zero.
Pairing indices in $\Delta^2$ proves its vanishing.
Each summand is a composition of two derivations and hence has order at most two.
Expanding $\Delta(fg)$ gives the degree-one derived bracket; evaluation on generators yields the stated brackets, which determine its biderivation extension.
Both $\Delta S$ and $\{S,S\}$ vanish since $S$ contains no $\eta$.
In $D\Delta+\Delta D$, the terms with a derivative left on the input cancel by odd anticommutation, while the remaining Hessian coefficients $\partial_i\partial_jS$ are symmetric and multiply the antisymmetric derivatives $\partial_{\eta_i}\partial_{\eta_j}$.
Their sum is zero.
\end{proof}

\begin{remark}[A chiral Batalin--Vilkovisky comparison]\label{thm:bv-structure-bar}
The polynomial operator above is defined on its displayed finite generator algebra.
A residue operator on a chiral configuration complex requires a domain, a cyclic pairing, its degree and second-order identity, and compatibility with every collision map.
The Arnold relations alone do not specify these data or an interacting master action.
An identification with the polynomial model requires the actual coefficient and operator maps.
\end{remark}''')
s=p.read_text();start=s.index('For non-quadratic algebras, the master action is:');end=s.index(r'\section{Open questions}',start)
edit(p,s[start:end],r'''Higher interactions on a three-manifold require operations with output in $\Omega^3(M)$, together with a specified cyclic pairing and differential compatibility.
Proposition~\ref{prop:cbc26-quartic-degree} constructs a contracted three-form and distinguishes it from the vanishing fourfold wedge.
The ordinary $\mathfrak{sl}_2$ connection $e\,dx+f\,dy$ has curvature $h\,dx\wedge dy$ independently of a level parameter.
A critical-level abelianization must therefore change the carrier or construct a comparison that explains this curvature.

''')
# Citations carry explicit separate keys in this integration.
p=c/'bibliography/references.tex';bib=r'''\bibitem{AffineDSArakawa026} T. Arakawa, \emph{Introduction to W-algebras and their representation theory}, Perspectives in Lie Theory, Springer INdAM Series \textbf{19} (2017), 179--250. \url{https://arxiv.org/abs/1605.00138}. Locators refer to version2.
\bibitem{AffineDSFrenkel026} E. Frenkel, \emph{Vertex algebras and algebraic curves}, S\'eminaire Bourbaki, Exp.~875, Ast\'erisque \textbf{276} (2002), 299--339. \url{https://arxiv.org/abs/math/0007054}. Locators refer to version4.
\bibitem{BD026} A. Beilinson and V. Drinfeld, \emph{Chiral Algebras}, AMS Colloquium Publications51,2004. \url{https://math.uchicago.edu/~drinfeld/langlands/chiral/}.
\bibitem{Frenkel026} E. Frenkel, \emph{Vertex algebras and algebraic curves}, S\'eminaire Bourbaki, expos\'e875,2000. \url{https://math.berkeley.edu/~frenkel/BOOK/bourbaki.pdf}.
\bibitem{DLMFell} NIST Digital Library of Mathematical Functions, \S23.2, Eq.~23.2.5, and \S23.8, Eq.~23.8.2. \url{https://dlmf.nist.gov/23.2.E5}; \url{https://dlmf.nist.gov/23.8.E2}.
''';edit(p,r'\end{thebibliography}',bib+r'\end{thebibliography}')
# Standalone wrapper retains earlier proofs and appends the actual new maps.
p=dest/'proof/comparison_main.tex';s=p.read_text();idx=s.index(r'\begin{thebibliography}')
extra=r'''\input{../cbc/chapters/theory/elliptic_propagator}
\begingroup
\providecommand{\Res}{\operatorname{Res}}\providecommand{\Vir}{\operatorname{Vir}}\providecommand{\Aut}{\operatorname{Aut}}
\input{../cbc/chapters/theory/affine_ds_global}
\endgroup
\section{Unital Virasoro chiral chains on the projective line}\label{sec:cbc26-unital-p1}
\input{../cbc/chapters/theory/unital_p1_chains}
\input{../cbc/chapters/theory/relative_p1_comparison}
''';s=s[:idx]+extra+s[idx:];s=s.replace(r'\end{thebibliography}',bib+r'\end{thebibliography}');p.write_text(s)
(report/'integration-edits.json').write_text(json.dumps(changes,indent=2)+'\n')
(report/'input-source-record.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [aff,rel,uni,ep]},indent=2)+'\n')
print('prepared',len(changes),'edits')
