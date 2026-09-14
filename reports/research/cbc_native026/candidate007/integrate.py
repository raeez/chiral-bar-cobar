from pathlib import Path
r=Path('research-candidates/cbc_native026/candidate007')
def replace_block(path,start,end,new):
 p=r/path;s=p.read_text();a=s.index(start);b=s.index(end,a)+len(end);p.write_text(s[:a]+new+s[b:])
p=r/'cbc/chapters/theory/subregular_ds.tex';s=p.read_text().replace('\\S1, pp.~3--5','\\S1, pp.~3--6');p.write_text(s)
p=r/'cbc/chapters/examples/w_algebras_framework.tex';s=p.read_text();s=s.replace('\\input{chapters/theory/subregular_ds}','\\input{chapters/theory/subregular_ds}\n\\input{chapters/theory/subregular_bar}')
a=s.index('A proof requires: (1)~DS reduction');b=s.index('\\end{remark}',a)
s=s[:a]+r'''The orbit-indexed comparison requires a choice of coefficient ring, a dual coalgebra, and maps between the two reduction complexes.
For the subregular $\mathfrak{sl}_3$ family, Theorem~\ref{thm:cbc27-subregular-map} constructs the same-level reduction map.
Theorem~\ref{thm:cbc28-bar-comparison} constructs an associative bar comparison after the explicit $C_2$ quotient.
Propositions~\ref{prop:cbc28-nonembedding} and~\ref{prop:cbc28-bar-obstruction} give the vacuum and associator obstructions on the full vertex carrier.
A reflected chiral equivalence must account for these operations before specialization or completion.
'''+s[b:]
a=s.index('Nilpotent orbits are partially ordered by closure:');b=s.index('\\end{remark}',a)
s=s[:a]+r'''Nilpotent orbits are partially ordered by closure.
Reduction at the zero nilpotent gives the universal affine algebra.
Principal reduction in type $A_{n-1}$ has strong generators of weights $2,\ldots,n$.
For $\mathfrak{sl}_3$, the subregular reduction is the four-generator algebra $W_k$.
The actual map is
\[
 W_k\lhook\joinrel\longrightarrow
 V^k(\mathfrak{sl}_3)\otimes F_{bc}^{\otimes2},
 \qquad H^0(C_k,D)\simeq W_k.
\]
The first arrow is Theorem~\ref{thm:cbc27-subregular-map}.
An inclusion into the bare affine algebra cannot hold at every level:
Proposition~\ref{prop:cbc28-nonembedding} excludes even a unital map $W_0\to V^0(\mathfrak{sl}_3)$.
Orbit closure therefore does not define the displayed algebras as a chain of vertex subalgebras.
'''+s[b:]
a=s.index('\\begin{remark}[Hook-type evidence');b=s.index('\\end{remark}',a)+len('\\end{remark}')
s=s[:a]+r'''\begin{remark}[Hook orbits and reduction maps]
\label{rem:hook-type-evidence}
\index{W-algebra@$\mathcal{W}$-algebra!hook type}
For a hook partition $(n-r,1^r)$, transpose gives $(r+1,1^{n-r-1})$.
This is a statement about nilpotent orbits.
The case $(2,1)$ has the explicit reduction and Poisson-quotient bar maps in
Theorems~\ref{thm:cbc27-subregular-map} and~\ref{thm:cbc28-bar-comparison}.
Its unreduced normal product has the nonzero associator~\eqref{eq:cbc28-associator}.
Maps for other hook pairs require their own differential, coefficient action, and comparison of the two carriers.
Partition transpose alone supplies none of these maps.
\end{remark}'''+s[b:];p.write_text(s)
replace_block(Path('cbc/chapters/theory/chiral_koszul_pairs.tex'),r'\begin{example}[Bershadsky--Polyakov algebra]',r'\end{example}',r'''\begin{example}[Bershadsky--Polyakov algebra]
\label{ex:bp-algebra}
The universal subregular reduction of $\mathfrak{sl}_3$ is the polynomial family
$W_R$ over $R=\mathbb C[k]$ of Theorem~\ref{thm:cbc27-subregular-map}.
It has four even strong generators $J,U,P,V$.
For $k\ne-3$, the conformal generators $J,G^+,G^-,T$ have weights $1,3/2,3/2,2$.
Their integer-order singular products are~\eqref{eq:cbc27-j-products}--\eqref{eq:cbc27-g-products}.
The polynomial family and its cohomology use algebraic direct sums.
The conformal presentation only inverts $k+3$.

Changing the base to the central charge gives the rank-two algebra
$\mathbb C[c,t]/(6t^2+(c-25)t+24)$ in~\eqref{eq:cbc28-central-base}.
Its discriminant is $(c-1)(c-49)$.
Neither a square root of $c$ nor an adic completion enters this construction.
The need for further bar operations comes from the explicit normal-product associator~\eqref{eq:cbc28-associator}.
After the stated $C_2$ quotient, Theorem~\ref{thm:cbc28-bar-comparison} gives an actual associative bar quasi-isomorphism.
\end{example}''')
p=r/'cbc/chapters/theory/chiral_koszul_pairs.tex';s=p.read_text().replace(r'Bershadsky--Polyakov & 4 & I + $\sqrt{c}$-adic & Fractional exponents',r'Bershadsky--Polyakov & 4 & Algebraic level family & Four even fields');p.write_text(s)
p=r/'cbc/chapters/examples/w_algebras_deep.tex';s=p.read_text();a=s.index('\\begin{remark}[Frontier discipline]');b=s.index('\\end{remark}',a)+len('\\end{remark}')
s=s[:a]+r'''\begin{remark}[Reduction and vertex inclusions]
The nilpotent orbit determines a reduction complex and its degree-zero cohomology.
It does not determine an inclusion into the bare affine algebra.
At level zero, such an inclusion for subregular $\mathfrak{sl}_3$ contradicts the vacuum product $J_{(1)}J=\mathbf1$
(Proposition~\ref{prop:cbc28-nonembedding}).
The strict reduction map instead lands in the affine--ghost complex.
\end{remark}'''+s[b:]
a=s.index('\\begin{proposition}[DS hierarchy and Koszul duality;');b=s.index('\\end{proof}',a)+len('\\end{proof}')
s=s[:a]+r'''\begin{proposition}[Subregular reduction and associative bars;
\ClaimStatusProvedHere]\label{prop:ds-koszul-hierarchy}
For the universal subregular $\mathfrak{sl}_3$ family over $\mathbb C[k]$, the reduction induces
\[
 B(R_{W_R})\xrightarrow{\ B(i)\ }B(R_{C_R})
\]
as a quasi-isomorphism of direct-sum differential coalgebras with the augmentations of Theorem~\ref{thm:cbc28-bar-comparison}.
Their cohomology is the exterior algebra on four classes of degree $-1$.
On the full vertex carrier, the normal-product bar already fails at length three:
\[
 b_2^2(sJ\otimes sJ\otimes sU)=2s\bigl(:(\partial J)U:\bigr)\ne0.
\]
\end{proposition}
\begin{proof}
The polynomial inclusion, projection, and contraction are those of Theorem~\ref{thm:cbc28-c2-reduction}.
Theorem~\ref{thm:cbc28-bar-comparison} extends the two maps letterwise to the associative bars.
Corollary~\ref{cor:cbc28-bar-cohomology} computes their cohomology.
The final identity is Proposition~\ref{prop:cbc28-bar-obstruction} and holds before taking the quotient.
\end{proof}

\begin{remark}[Orbit transpose and a reflected chiral target]
For a nilpotent $f$ of a simple Lie algebra, the proposed relation
\[
 (\mathcal W^k(\mathfrak g,f))^!\simeq
 \mathcal W^{-k-2h^\vee}(\mathfrak g^\vee,f^{\mathrm{BV}})
\]
requires a specified curved chiral dual and a map between the two coefficient systems.
The same-level reduction and its $C_2$ quotient do not define this cross-level map.
In the subregular $\mathfrak{sl}_3$ case, the vacuum coefficients prevent augmentations on both reflected factors, and the normal product fails associativity.
These are explicit equations that any proposed extension must address.
\end{remark}'''+s[b:]
# Replace the sl4 table and its unsupported numerical bar counts with the computed centralizers.
a=s.index('\\begin{computation}[DS hierarchy for \\texorpdfstring{$\\mathfrak{sl}_4$}');b=s.index('\\end{computation}',a)+len('\\end{computation}')
s=s[:a]+r'''\begin{computation}[Nilpotent reductions for $\mathfrak{sl}_4$]
\label{comp:sl4-ds-hierarchy}
\index{sl4@$\mathfrak{sl}_4$!nilpotent orbits}
Proposition~\ref{prop:cbc28-sl4-centralizers} computes the orbit dimensions and strong generator weights for all five partitions.
For the subregular partition $(3,1)$, the centralizer has dimension five and generator weights $1,2,2,2,3$.
For the minimal partition $(2,1,1)$, the centralizer has dimension nine and weights $1^4,(3/2)^4,2$.
All fields are even.

Partition transpose gives the orbit pairs
\[
 (1^4)\longleftrightarrow(4),\qquad
 (2,1,1)\longleftrightarrow(3,1),\qquad
 (2,2)\longleftrightarrow(2,2).
\]
The corresponding universal vertex algebras have different generator weights.
A vertex comparison requires a map and its preserved structures in addition to this orbit pairing.
For the principal and zero orbits, Corollary~\ref{cor:cbc28-principal-affine} excludes a conformal isomorphism.

If the generator weights, counted with multiplicity, are $d_1,\ldots,d_m$, their universal vacuum series is
\[
 \prod_{i=1}^m\prod_{r\geq0}(1-q^{d_i+r})^{-1}.
\]
This follows from the ordered PBW monomials.
It counts states rather than tensor-bar chain groups or their cohomology.
\end{computation}'''+s[b:]
p.write_text(s)
# Correct the sl4 duplicate using its actual centralizer.
replace_block(Path('cbc/chapters/theory/koszul_pair_structure.tex'),r'\begin{theorem}[Structure of \texorpdfstring{$\mathcal{W}(\mathfrak{sl}_4, e_{subreg})$}', 'The fractional weights require orbifold constructions on configuration spaces.',r'''\begin{theorem}[Subregular $\mathfrak{sl}_4$ generator weights;
\ClaimStatusProvedHere]\label{thm:w-algebra-sl4}
At noncritical level $k\ne-4$, the universal subregular reduction has five even strong generators of weights $1,2,2,2,3$.
Its vertex products have integer-order poles.
\end{theorem}
\begin{proof}
The centralizer basis in Proposition~\ref{prop:cbc28-sl4-centralizers} has grading degrees $0,-1,-1,-1,-2$.
Kac--Wakimoto's PBW theorem gives the five displayed weights and even parity.
Integer-order poles are part of the vertex algebra locality relation.
\end{proof}''')
p=r/'cbc/chapters/theory/higher_genus.tex';s=p.read_text();a=s.index('Non-principal $\\mathcal{W}$-algebras (Bershadsky--Polyakov,');b=s.index('For $\\mathcal{W}_\\infty$',a)
s=s[:a]+r'''For the universal Bershadsky--Polyakov family, a vertex augmentation exists exactly at $k=-3/2$
(Proposition~\ref{prop:cbc28-nonembedding}).
Thus hypothesis~(a), stated using an augmentation ideal, does not apply at other levels.
At $k=-3/2$, the weight-one symmetry is one-dimensional abelian, so the stated semisimple hypothesis does not follow.
Its trivial-coefficient Lie algebra cohomology has $H^1(\mathbb C,\mathbb C)=\mathbb C$:
the one-generator Chevalley--Eilenberg differential is zero.
The ordinary normal-product bar also fails by~\eqref{eq:cbc28-associator}.
An all-genus comparison requires its actual chiral complex and additional structure.
'''+s[b:];p.write_text(s)
# Add both new proof and its already existing primary reference to the standalone entry.
for name in ['proof/comparison_main.tex','proof/subregular_main.tex']:
 p=r/name;s=p.read_text().replace('\\input{../cbc/chapters/theory/subregular_ds}','\\input{../cbc/chapters/theory/subregular_ds}\n\\input{../cbc/chapters/theory/subregular_bar}')
 if name.endswith('subregular_main.tex'):
  bib=r'''\bibitem{AffineDSArakawa026} T. Arakawa, \emph{Introduction to W-algebras and their representation theory}, Perspectives in Lie Theory, Springer INdAM Series \textbf{19} (2017), 179--250. \url{https://arxiv.org/abs/1605.00138}. Locators refer to version 2.
'''
  s=s.replace('\\end{thebibliography}',bib+'\\end{thebibliography}')
 p.write_text(s)
print('Integrated initial connected corrections')
