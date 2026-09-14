from pathlib import Path
r=Path('research-candidates/cbc_native026/candidate007')
p=r/'cbc/chapters/examples/w_algebras_deep.tex';s=p.read_text()
a=s.index('\\emph{Step~2: the BV orbit identifies the Koszul dual.}')
b=s.index('\\subsubsection*{General theorem}',a)
s=s[:a]+r'''\emph{Orbit transpose and the vertex carrier.}
For $\mathfrak{sl}_3$, partition transpose gives
\begin{equation}\label{eq:w3-kd-explicit}
 (3)^t=(1,1,1).
\end{equation}
Reduction at the zero nilpotent is the identity operation on the affine algebra.
This combinatorial fact does not identify the principal W-algebra with an affine vertex algebra.
Their weight-one spaces have dimensions zero and eight, respectively
(Corollary~\ref{cor:cbc28-principal-affine}).
A proposed curved Koszul identification requires a separately defined dual carrier and a map to it.

The actual subregular comparison is the inclusion into the full affine--ghost complex in Theorem~\ref{thm:cbc27-subregular-map}.
Its $C_2$ quotient gives the associative bar map of Proposition~\ref{prop:ds-koszul-hierarchy}.
On the unreduced states, the nonzero associator~\eqref{eq:cbc28-associator} rules out replacing the collision operations by ordinary normal multiplication.
Thus residue identities must follow from the actual mode maps, not from orbit transpose or equality of dimensions.

\subsubsection*{Orbit pairs in rank four}

The orbit pairs are
\[
 (4)\longleftrightarrow(1^4),\qquad
 (3,1)\longleftrightarrow(2,1,1),\qquad
 (2,2)\longleftrightarrow(2,2).
\]
Proposition~\ref{prop:cbc28-sl4-centralizers} gives the corresponding generator weights.
The principal and zero reductions again have different weight-one dimensions, now zero and fifteen.
The orbit pairing alone therefore supplies neither a conformal isomorphism nor a reflected bar map.

'''+s[b:]
a=s.index('\\begin{theorem}[Factorization Koszul dual of')
b=s.index('\\end{proof}',a)+len('\\end{proof}')
s=s[:a]+r'''\begin{proposition}[Obstructions for a principal reduction tower;
\ClaimStatusProvedHere]\label{thm:winfty-factorization-kd}
Let $W_N^k=\mathcal W^k(\mathfrak{sl}_N,f_{\mathrm{prin}})$ be universal at noncritical level.
The orbit transpose $(N)^t=(1^N)$ does not give a conformal isomorphism from $W_N^k$ to a universal affine algebra.
Moreover, transition maps that delete the highest strong generator cannot define the full principal tower at all parameters.
\end{proposition}
\begin{proof}
The first assertion follows from the weight-one dimensions in Corollary~\ref{cor:cbc28-principal-affine}.
For the second, the $N=3$ transition would kill $W$.
At central charge $-30$, Proposition~\ref{prop:cbc28-truncation} excludes this map by its vacuum product.
\end{proof}

\begin{remark}[A completed principal comparison]
\label{eq:winfty-stage-kd}
A construction of $\varprojlim_N B^{\mathrm{ch}}(W_N)$ requires actual transition maps, their coefficient rings, and compatibility with all collision operations.
A bar--cobar comparison for that limit also requires a justified totalization and a proof controlling derived inverse limits.
The proposed reflected target $V^{-k-2N}(\mathfrak{sl}_N)$ requires a map from a defined curved Koszul dual.
Neither partition transpose nor deletion of the highest generator constructs these data.
The two proved obstructions above specify failures that an alternative construction must avoid.
\end{remark}'''+s[b:]
p.write_text(s)
# Correct the direct hook consumer and the stated principal parameter law.
p=r/'cbc/chapters/theory/koszul_pair_structure.tex';s=p.read_text();a=s.index('\\begin{theorem}[Feigin--Frenkel duality as S-duality,');b=s.index('\\end{theorem}',a)+len('\\end{theorem}')
s=s[:a]+r'''\begin{theorem}[Principal Feigin--Frenkel parameter relation;
\ClaimStatusProvedElsewhere]\label{thm:ff-s-duality}
For simply-laced $\mathfrak g$, the principal Feigin--Frenkel duality uses
\[
 (k+h^\vee)(k^\vee+h^\vee)=1,
 \qquad k^\vee=-h^\vee+\frac{1}{k+h^\vee}.
\]
Both shifted levels are nonzero.
This is the reciprocal parameter relation recorded in
\cite{Ara15}*{p.~566, footnote~1}.
It differs from the reflection $k\mapsto-k-2h^\vee$.
\end{theorem}'''+s[b:]
s=s.replace(r'$k^L = -h^{\vee}(\mathfrak{g}^L) + r^{\vee}/(k + h^{\vee}(\mathfrak{g}))$',r'$k^L = -h^{\vee}(\mathfrak{g}^L) + 1/(r^{\vee}(k + h^{\vee}(\mathfrak{g})))$')
a=s.index('The principal simply-laced case is Feigin--Frenkel');b=s.index('\\end{remark}',a)
s=s[:a]+r'''The principal reciprocal relation is the theorem above.
For the subregular $\mathfrak{sl}_3$ family, the proved constructions are the same-level affine--ghost map and the associative bar map after the $C_2$ quotient.
A comparison for an orbit-transposed pair must preserve its specified structures and address the vacuum and associator obstructions of
Propositions~\ref{prop:cbc28-nonembedding} and~\ref{prop:cbc28-bar-obstruction}.
'''+s[b:];p.write_text(s)
p=r/'cbc/chapters/connections/concordance.tex';s=p.read_text();a=s.index('  and the distinct non-principal orbit-duality transport problem');b=s.index('\\item \\textbf{MC2}',a)
s=s[:a]+r'''  and non-principal orbit-duality comparisons
  (Conjecture~\ref{conj:w-orbit-duality}).
  The subregular $\mathfrak{sl}_3$ family has the actual polynomial reduction map of
  Theorem~\ref{thm:cbc27-subregular-map} and the $C_2$-quotient bar comparison of
  Theorem~\ref{thm:cbc28-bar-comparison}.
  The latter does not retain the first-product operation, as shown by
  $\overline{(\partial J)_{(1)}U}=-U$ with $\overline{\partial J}=0$.
  A reflected chiral comparison must therefore supply additional operation data.
'''+s[b:];p.write_text(s)
# Keep the first proven bar map's name consistent in its direct callers.
print('Propagated the direct hierarchy and hook consumers')
