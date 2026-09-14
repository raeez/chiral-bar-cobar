from pathlib import Path
import re, json, hashlib

ROOT=Path(__file__).resolve().parents[3]
C=ROOT/'research-candidates/cbc_native026/cbc'
P=ROOT/'research-candidates/cbc_native026/proof'
records=[]

def replace(path, old, new, count=1):
    f=C/path
    text=f.read_text()
    actual=text.count(old)
    assert actual==count, (path,old[:100],actual,count)
    f.write_text(text.replace(old,new))
    records.append({'path':str(path),'old':old,'new':new,'occurrences':count})

def region(path,start,end,new):
    text=(C/path).read_text()
    a=text.index(start); b=text.index(end,a)
    replace(path,text[a:b],new)

geometry=(P/'consumer_geometry.tex').read_text()
cut=geometry.index('\\subsection{The differential graded Lie algebra of connections}')
amplitude=geometry[geometry.index('\\subsection{Marked curves'):cut]
connections=geometry[cut:]
(C/'chapters/theory/insertion_integrals.tex').write_text(amplitude)
(C/'chapters/theory/mc_transport.tex').write_text(connections)
bv='chapters/connections/bv_brst.tex'
text=(C/bv).read_text()
a=text.index('\\subsection{Augmentations and the relative coordinate carrier}')
b=text.index('\\subsection{The chain map}',a)
(P/'augmentation_relative.tex').write_text(text[a:b])
region(bv,'\\begin{theorem}[Genus-\\texorpdfstring{$0$}{0} amplitudes','\\begin{remark}[Genus-$1$ partition function]', '\\input{chapters/theory/insertion_integrals}\n\n')
region(bv,'\\subsection{Anomaly duality from complementarity}','\\section{Holomorphic-topological field theories}', '\\input{chapters/theory/ds_chain_comparisons}\n\n')
replace(bv, 'Theorems~\\ref{thm:bar-semi-infinite-km} and~\\ref{thm:bar-semi-infinite-w} construct filtered comparisons under their specified coefficient, target, symbol-map, and correction hypotheses.', 'Theorem~\\ref{thm:bar-semi-infinite-km} constructs a filtered comparison under its coefficient, target, symbol-map, and correction hypotheses.\nTheorem~\\ref{thm:bar-semi-infinite-w} transports an actual equivariant map between specified double complexes.\nTheorem~\\ref{thm:cbc26-polynomial-ds} constructs the polynomial reduction and its associative bar maps.')
replace(bv, 'By Theorem~\\ref{thm:anomaly-koszul}, $d_{\\mathrm{bar}}^2 = 0$ for $\\cA_{\\mathrm{tot}} = \\cA_{\\mathrm{matter}} \\otimes \\cA_{\\mathrm{ghost}}$ if and only if $\\kappa_{\\mathrm{tot}} = 0$ (equivalently, $c = 26$ for the bosonic string).  When $\\kappa_{\\mathrm{tot}} \\neq 0$, the universal MC class $\\Theta_\\cA = \\kappa \\cdot \\eta \\otimes \\Lambda$ (Theorem~\\ref{thm:explicit-theta}) curves the bar complex at every genus.', 'On the algebraic matter--ghost state space, Theorem~\\ref{thm:vir-square} gives $Q^2=(c-26)\\sum_{n>0}(n^3-n)c_{-n}c_n/12$.\nThe reduced chiral construction based on an augmentation kernel does not apply to this vertex algebra by Proposition~\\ref{prop:vir-no-augmentation}.\nAn alternative chiral target must specify its unit and collision maps before an anomaly operator can be transported.\nThe required operator identity is Proposition~\\ref{prop:cbc26-square-transport}.')
region(bv,'At genus $g \\geq 1$, the BRST complex requires additional data:', '\\end{remark}', 'A genus-$g$ comparison requires complexes over the stated curve or moduli space, with compatible coefficient maps, anomaly operators, and clutching maps.\nProposition~\\ref{prop:cbc26-horizontal-comparison} proves the transport statement for bounded flat bundle complexes.\nExample~\\ref{ex:cbc26-torus-monodromy} gives a genus-one obstruction to inferring global cohomology from fiberwise data.\nFor the matter--ghost vertex algebra, a unital collision construction must also avoid the augmentation obstruction of Proposition~\\ref{prop:vir-no-augmentation}.\n')
# Preserve the full accepted operator block and its independent source.
kp='chapters/theory/koszul_pair_structure.tex'
region(kp,'\\section{The Chern--Simons structure in non-quadratic Koszul duality}','\\subsection{Physical interpretation: quantum groups and Chern--Simons}', '\\section{Connections and Maurer--Cartan transport}\n\n\\input{chapters/theory/mc_transport}\n\n')
replace(kp,'The MC equation for the Koszul dual coalgebra has the form of a deformed flatness equation (preceding theorem).', 'Corollary~\\ref{thm:cs-koszul-general} gives a flat connection after an actual $L_\\infty$ map to its de Rham carrier is supplied.')

main='main.tex'
replace(main,'The genus-$0$\nbar/BRST comparison is proved, and the all-genera BV/BRST bridge is\nformulated as a downstream conjectural comparison in\nChapter~\\ref{ch:bv-brst}.', 'The Virasoro charge and its square are computed in\nChapter~\\ref{ch:bv-brst}.\nThe polynomial $\\mathfrak{sl}_2$ Hamiltonian reduction has explicit associative bar maps.\nThe chiral bar/BRST comparison requires a unital collision target, relative descent, and compatible chain maps.\nIts extension over curves further requires horizontal maps and clutching compatibility.')
intro='chapters/theory/introduction.tex'
replace(intro,'The bar complex is the BRST complex; Verdier duality is CPT.', 'A BRST interpretation requires a specified state complex and a compatible map from the chiral construction.\n  The Virasoro square and the augmentation obstruction are given in Chapter~\\ref{ch:bv-brst}.')
replace(intro,'The BRST resolution is complete.', 'The displayed counit concerns the stated bar--cobar construction.\n  A BRST resolution also requires its state-space comparison.')

w='chapters/examples/w_algebras_framework.tex'
region(w,'The physical content of this duality is anomaly cancellation:', '\\end{proof}', 'For the parameter reflection $t=k+h^\\vee\\mapsto-t$, Proposition~\\ref{cor:anomaly-duality-w} computes the central-charge sum.\nIt is $26$ for Virasoro and $100$ for $\\mathcal W_3$.\nThe corresponding scalars $\\kappa=c/2$ and $\\kappa=5c/6$ have sums $13$ and $250/3$.\nThese scalar identities require a separate comparison before they can describe anomaly operators or genuswise cohomology.\nThe polynomial reduction and its associative bar maps are constructed in Theorem~\\ref{thm:cbc26-polynomial-ds}.\n')
region(w,'\\begin{remark}[Canonical twisting morphism for $\\mathcal{W}$-algebras via DS]','\\begin{conjecture}[W-algebra Koszul duality for general nilpotent;', r'''\begin{remark}[Reduction maps and twisting morphisms]
\label{rem:w-twisting-morphism}
A differential $Q_{\mathrm{DS}}$ on the affine--ghost complex is a degree-one operator, rather than a degree-zero map from the reduced algebra to the affine algebra.
It therefore cannot define an arrow $\bar B(\mathcal W)\to\bar B(\widehat{\mathfrak g}_k)$ by bar functoriality.
For the polynomial reduction, the degree-zero maps are the explicit $i,p$ of Theorem~\ref{thm:cbc26-polynomial-ds}.
Their associative bar maps preserve tensor length and commute with the two components of the bar differential.
A chiral twisting morphism after quantum reduction requires the corresponding maps on the full collision complexes.
\end{remark}

''')

ht='chapters/connections/holomorphic_topological.tex'
region(ht,'\\begin{theorem}[Open-string bar identification;', '\\begin{conjecture}[Closed-string cobar identification;', r'''\begin{proposition}[The Virasoro differential on a boundary vacuum]
\label{thm:open-string-bar}
For the universal Virasoro vacuum module $M_C$ with the full weight-$(2,-1)$ ghost carrier of Theorem~\ref{thm:vir-square}, the charge $Q$ defines a cochain complex if and only if $C=26$.
At $C=26$, the augmentation-kernel chiral target for $M_C\otimes bc$ does not exist.
The fixed relative fiber is not preserved by the coordinate flow $z\mapsto z/(1+sz)$ when $s\ne0$.
\end{proposition}

\begin{proof}
The nonzero vector $\mathbf1\otimes b_{-2}\Omega$ detects the square in Theorem~\ref{thm:vir-square}.
The collision identity $b_{(0)}c=\mathbf1$ proves the augmentation assertion in Proposition~\ref{prop:vir-no-augmentation}.
The relative state $v=c_{-1}c_1\Omega$ transforms to $v-sc_0c_1\Omega$ by Proposition~\ref{prop:vir-relative-target-obstruction}, which proves the last assertion.
\end{proof}

A boundary theory must specify its state complex and boundary condition before its states can be compared with chiral chains.
Theorem~\ref{thm:bar-semi-infinite-km} supplies a filtered criterion after the coefficient and symbol maps are constructed.
Theorem~\ref{thm:bar-semi-infinite-w} applies a second differential only to an actual equivariant comparison with the stated finite totalization.
The explicit associative comparison in Theorem~\ref{thm:cbc26-polynomial-ds} concerns the polynomial reduction.

''')
region(ht,'\\begin{remark}[Evidence]\nOpen sector:', '\\subsection{Factorization and dimensional reduction}', r'''\begin{remark}[Boundary and bulk comparison maps]
An open-sector comparison requires the actual boundary state complex, unital collision target, and compatible chain maps.
A closed-sector comparison additionally requires a bulk observable complex and an open--closed map.
For an integral formula, Stokes' theorem applies only after the insertion map and a closed integration functional have been constructed, as in Proposition~\ref{thm:genus0-amplitude-bar}.
\end{remark}

''')
region(ht,'\\begin{theorem}[AGT 2D side: bar complex = semi-infinite complex;', '\\begin{conjecture}[AGT 4D--2D bridge via bar-cobar;', r'''\begin{proposition}[Central charges under principal level reflection]
\label{thm:agt-2d-bar}
For the principal $\mathfrak{sl}_2$ and $\mathfrak{sl}_3$ central-charge formulas, reflection $k+h^\vee\mapsto-(k+h^\vee)$ gives sums $26$ and $100$, respectively.
The half-central-charge sum in the Virasoro case is $13$.
\end{proposition}

\begin{proof}
Substitute the two root systems in Proposition~\ref{cor:anomaly-duality-w}.
\end{proof}

The parameter reflection in this proposition differs from the reciprocal parameter relation in Feigin--Frenkel duality.
Neither scalar relation defines the semi-infinite differential or a comparison with four-dimensional observables.

''')
replace(ht,'The 2D side is proved (Theorem~\\ref{thm:agt-2d-bar}); the 4D--2D bridge is proved in specific cases \\cite{SV13,MO19}.  Remaining coefficient identities belong to MC4; the bulk identification to MC5 (Chapter~\\ref{chap:concordance}, Conjecture~\\ref{conj:master-bv-brst}).', 'Proposition~\\ref{thm:agt-2d-bar} computes the indicated two-dimensional scalar formulas.\nThe bar comparison requires a specified chiral target and chain maps.\nA comparison with four-dimensional observables further requires their construction and an equivariant map to that target.')

ff='chapters/examples/free_fields.tex'
region(ff,'The three conjectural identifications each involve curved Koszul duality', '\\end{remark}', 'A same-family central-charge reflection does not compute bar or semi-infinite cohomology.\nFor the actual critical Virasoro vacuum charge, Corollary~\\ref{cor:virasoro-semi-infinite} gives absolute degrees $0,3$ and relative degrees $0,2$.\nThe vacuum PBW character in Theorem~\\ref{thm:virasoro-chiral-koszul} counts conformal states.\nAny other proposed semi-infinite growth formula requires its own differential and a cohomology calculation.\n')
region(ff,'\\begin{theorem}[Algebraic string theory dictionary;', '\\begin{corollary}[Genus-zero amplitude comparison with compatible pairings;', r'''\begin{proposition}[State complexes, central coefficients, and insertion maps]
\label{thm:algebraic-string-dictionary}
The following statements use separate, specified carriers.
\begin{enumerate}[label=\textup{(\roman*)}]
\item On a nonzero restricted Virasoro module tensored with the conformal ghost module, the full charge is nilpotent exactly at matter central charge $26$.
\item The parameter reflection of Proposition~\ref{cor:anomaly-duality-km} negates the affine scalar $a(k)$, while its Sugawara central charges sum to $2\dim\mathfrak g$.
For principal Virasoro parameters the reflected half-central charges sum to $13$ by Proposition~\ref{cor:anomaly-duality-w}.
\item The polynomial reduction admits the explicit associative bar quasi-isomorphisms of Theorem~\ref{thm:cbc26-polynomial-ds}.
\item Insertion integrals defined by Proposition~\ref{thm:genus0-amplitude-bar} descend to cohomology and retain multilinear dependence on the insertion classes.
\end{enumerate}
\end{proposition}

\begin{proof}
Part~(i) follows from the operator identity and its detecting vector in Theorem~\ref{thm:vir-square}.
Part~(ii) is the direct substitution in the two scalar propositions.
Part~(iii) uses the explicitly defined maps $i,p$ and their tensorwise bar maps.
Part~(iv) is the chain identity for the insertion map followed by Stokes' theorem.
\end{proof}

A chiral string comparison still requires a unital collision target, a relative sheaf carrier, and compatible symbol and correction maps.
Theorem~\ref{thm:brst-bar-genus0} states the filtered chain criterion.
For an affine comparison the full hypotheses of Theorem~\ref{thm:bar-semi-infinite-km} also remain necessary.
Quantum reduction further requires the equivariance and totalization data of Theorem~\ref{thm:bar-semi-infinite-w}.
Maps over moduli require compatible connections, pairings, and clutching operations.

''')
region(ff,'\\begin{theorem}[Modular anomaly for KM and \\texorpdfstring{$\\mathcal{W}$}{W}-algebras;', '\\begin{conjecture}[Modular anomaly for general chiral', r'''\begin{proposition}[Fiber data and genus-one cohomology]
\label{thm:modular-anomaly-km-w}
Isomorphism of the fibers of two flat complexes does not imply isomorphism of their genus-one cohomology.
In particular, a diskwise bar/BRST comparison without transition compatibility does not determine genus-one cohomology or a modular transformation law.
\end{proposition}

\begin{proof}
Example~\ref{ex:cbc26-torus-monodromy} gives rank-one local systems on the torus with identical fibers and cohomology dimensions $(1,2,1)$ or $(0,0,0)$.
The missing condition is the compatibility with transitions, or equivalently horizontality in Proposition~\ref{prop:cbc26-horizontal-comparison}.
\end{proof}

For a conformal matter module, the ghost square is still governed by $(c-26)/12$ in Theorem~\ref{thm:vir-square}.
A modular weight requires its own determinant line and automorphy factor.
The scalar $c/24$ in a vacuum energy does not construct that line or its transformation law.

''')

cc='chapters/connections/concordance.tex'
region(cc,'\\begin{theorem}[Physical anomaly cancellation for KM and \\texorpdfstring{$\\mathcal{W}$}{W}-algebras;', '\\begin{conjecture}[Physical anomaly cancellation, higher genus;', r'''\begin{proposition}[Anomaly operators and scalar reflection]
\label{thm:anomaly-physical-km-w}
On the full conformal Virasoro ghost carrier, the anomaly operator vanishes exactly at matter central charge $26$.
Reflection of the principal Virasoro parameter pairs central charges $c,26-c$, whose half-central charges sum to $13$.
Reflection negates the affine scalar $a(k)$ of Proposition~\ref{cor:anomaly-duality-km}; the Sugawara half-central charges instead sum to $\dim\mathfrak g$.
The Maurer--Cartan equation for $\Omega^\bullet(M)\otimes\mathfrak g$ is the flatness equation on the trivial bundle of Theorem~\ref{thm:cs-koszul-km}.
\end{proposition}

\begin{proof}
Theorem~\ref{thm:vir-square} computes the anomaly and its nonzero detecting vector.
Propositions~\ref{cor:anomaly-duality-w} and~\ref{cor:anomaly-duality-km} give the scalar sums.
The last assertion follows by substituting the de Rham differential and Lie bracket into the Maurer--Cartan equation.
Transport to a different carrier requires the components of Proposition~\ref{thm:linf-mc-flatness}.
\end{proof}

''')
region(cc,'The genus-$0$ identifications of\nTheorem~\\textup{\\ref{thm:anomaly-physical-km-w}} extend to all', '\\end{conjecture}', r'''For a specified anomaly-free BRST sheaf complex and a separately constructed unital chiral-chain complex, there is a quasi-isomorphism over each moduli space of curves that is compatible with coordinate descent, the connections, pairings, anomaly operators, and clutching.
The genus-zero comparison and its compatibility with these structures are included in this assertion.
''')
region(cc,'Costello--Paquette \\cite{CP2020} conjecture (footnote~8) that', '\\end{remark}', r'''A comparison with twisted supergravity requires both the boundary algebraic comparison and a bulk observable complex.
The boundary comparison still needs its unital chiral carrier, coefficient maps, relative descent, and actual filtered chain map.
The polynomial Drinfeld--Sokolov reduction in Theorem~\ref{thm:cbc26-polynomial-ds} constructs an associative comparison on its declared carrier.
It supplies no chiral collision maps or bulk observables.
For a comparison over curves, Proposition~\ref{prop:cbc26-horizontal-comparison} identifies the additional horizontal chain equation.
''')
# Replace every inherited summary that misdescribes the double-complex theorem.
for path in [cc,'chapters/connections/genus_complete.tex']:
    f=C/path; text=f.read_text()
    old_phrases=[
      'The Kac--Moody and $\\mathcal W$ comparisons likewise retain the complete hypotheses of Theorems~\\ref{thm:bar-semi-infinite-km} and~\\ref{thm:bar-semi-infinite-w}.',
      'The Kac--Moody and $\\mathcal W$ comparisons in Theorems~\\ref{thm:bar-semi-infinite-km} and~\\ref{thm:bar-semi-infinite-w} also retain their full coefficient and filtered-map hypotheses.',
      'The Kac--Moody and Drinfeld--Sokolov comparisons likewise retain the complete coefficient, target, and filtered-map hypotheses of their cited comparison theorems.',
      'The filtered criteria of Theorems~\\ref{thm:brst-bar-genus0}, \\ref{thm:bar-semi-infinite-km}, and~\\ref{thm:bar-semi-infinite-w} start with specified source and target complexes.'
    ]
    for old in old_phrases:
      if old in (C/path).read_text():
        replace(path,old,'The affine criterion of Theorem~\\ref{thm:bar-semi-infinite-km} requires the actual coefficient and filtered chain maps.\nTheorem~\\ref{thm:bar-semi-infinite-w} further requires an equivariant map of specified double complexes and a valid totalization.\nTheorem~\\ref{thm:cbc26-polynomial-ds} constructs the polynomial reduction on its associative carrier.')
replace(cc,'Then the standard-tower MC5 packet closes.', 'Then the supplied comparison maps extend through the stated tower, compatibly with truncation, Verdier duality, and clutching.')
replace(cc,'standard-tower MC5 packet closes.', 'supplied comparison extends compatibly with truncation, Verdier duality, and clutching.')
replace(cc,'The exact\nMC5 attack chain is therefore: the disk-local packet of', 'The disk-local comparison of')
replace(cc,'Standard-tower MC5 closure on the canonical Yangian\nlocus;', 'Compatible comparisons on the canonical Yangian\nlocus;')
# Correct the page range of the verified primary reference.
refs='bibliography/references.tex'
text=(C/refs).read_text()
if '565--694' in text: replace(refs,'565--694','565--604',text.count('565--694'))

(ROOT/'reports/research/cbc_native026/native-replacements.json').write_text(json.dumps(records,indent=2)+'\n')
print('Applied',len(records),'replacement records')
