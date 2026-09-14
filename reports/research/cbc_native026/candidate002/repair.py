from pathlib import Path
import json
r=Path(__file__).resolve().parents[4]
c=r/'research-candidates/cbc_native026/candidate002/cbc';p=c.parent/'proof';records=[]
def replace(path,old,new):
 f=c/path;t=f.read_text();n=t.count(old);assert n>0,(path,old[:80]);f.write_text(t.replace(old,new));records.append({'path':str(path),'old':old,'new':new,'count':n})
def region(path,start,end,new):
 t=(c/path).read_text();a=t.index(start);b=t.index(end,a);replace(path,t[a:b],new)
supp=(c/'chapters/theory/reduction_obstructions.tex').read_text();cut=supp.index('\\section{Form degree in higher interaction terms}')
(c/'chapters/theory/reduction_parameters.tex').write_text(supp[:cut])
(c/'chapters/theory/form_degree.tex').write_text(supp[cut:])
w='chapters/examples/w_algebras_framework.tex'
region(w,'\\begin{theorem}[\\texorpdfstring{$\\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent;', '\\begin{remark}[Reduction maps and twisting morphisms]', r'''\input{chapters/theory/reduction_parameters}

\begin{remark}[The chiral dual after quantum reduction]
\label{thm:w-algebra-koszul-main}
\label{eq:w-koszul-main}\label{eq:ff-level-shift}
For a simple Lie algebra $\mathfrak g$ and principal nilpotent $f$, the proposed curved chiral comparison is
\[
 \mathcal W^k(\mathfrak g,f)^!\simeq\mathcal W^{-k-2h^\vee}(\mathfrak g,f).
\]
Its construction requires the affine--ghost collision complex, a unital reduced target, and a comparison that commutes with the reduction differential and all collision maps.
No such map is supplied by replacing a free-field state space with its cohomology.
The actual polynomial comparison is Theorem~\ref{thm:cbc26-polynomial-ds}.
Proposition~\ref{prop:cbc26-conformal-reflection} excludes a conformal vertex isomorphism under reflection for generic Virasoro parameters.
The curved chiral comparison above therefore needs a separately specified notion of equivalence and preserved structures.
At critical level the Sugawara conformal vector is undefined, so a limiting assertion additionally requires a construction over the level parameter.
\end{remark}

''')
ff='chapters/examples/free_fields.tex'
text=(c/ff).read_text();start=text.index('\\begin{proposition}[Fiber data and genus-one cohomology]');end=text.index('\\begin{conjecture}[Modular anomaly for general chiral',start)
torus=text[start:end]
region(ff,'\\begin{theorem}[Modular invariance and anomaly cancellation;', '\\section{Explicit low-degree computations}', '\\input{chapters/theory/elliptic_normalizations}\n\n'+torus+'\n')
bv='chapters/connections/bv_brst.tex'
replace(bv,'At genus~$1$, Theorem~\\ref{thm:genus-universality} gives $F_1 = \\kappa/24$.  For $\\cA = \\mathrm{Vir}_c$, $F_1 = c/24 = \\operatorname{tr}(\\Theta_{\\mathrm{Vir}_c}^{(1)}) = (c/2)\\cdot(1/12)$, encoding the Mumford isomorphism.', 'The Bernoulli coefficient of Theorem~\\ref{thm:genus-universality} is $F_1=\\kappa/24$.\nFor $\\kappa=C/2$, it gives $F_1=C/48$, while the vacuum-energy exponent in $q^{L_0-C/24}$ is $-C/24$.\nProposition~\\ref{prop:cbc26-genus-one-normalization} computes both values.\nAn identification with a Hodge integral or a trace requires its separately specified map and normalization.')
cc='chapters/connections/concordance.tex'
region(cc,'\\item \\emph{BV-BRST.}\n  The CG BV formalism', '\\item \\emph{Monoidal bar-cobar.}', r'''\item \emph{BV-BRST.}
  Theorem~\ref{thm:cbc26-finite-bv} constructs a polynomial BV differential and its Koszul quotient map under a regular-sequence hypothesis.
  A comparison between field-theory observables and a chiral bar complex requires the actual observable complex, collision target, coefficient maps, coordinate descent, and a chain morphism.
  The filtered criterion of Theorem~\ref{thm:brst-bar-genus0} applies only after these data are supplied.
  The polynomial quotient map alone does not construct those curvewise data.
''')
# Each old hypothesis reference is now routed to the statement that contains it.
replace(cc,'\\ref{thm:algebraic-string-dictionary}','\\ref{thm:brst-bar-genus0} and Corollary~\\ref{cor:string-amplitude-genus0}')
kp='chapters/theory/koszul_pair_structure.tex'
region(kp,'The RTT relations in the Yangian give rise to the $\\alpha^4$ term:', '\\subsection{The holographic interpretation}', '\\input{chapters/theory/form_degree}\n\n')
replace(kp,'The theorematic input is the boundary-side Koszul/module package; bulk reconstruction remains a downstream MC5 task.', 'Bulk reconstruction requires an explicit complex of bulk observables and a comparison with the boundary construction.')
# Do not let the changed W label be cited as a proved theorem.
for f in c.rglob('*.tex'):
 t=f.read_text()
 for old,new in [
   ('Theorem~\\ref{thm:w-algebra-koszul-main}', 'the proposed comparison in Remark~\\ref{thm:w-algebra-koszul-main}'),
   ('Theorem~\\textup{\\ref{thm:w-algebra-koszul-main}}', 'Remark~\\textup{\\ref{thm:w-algebra-koszul-main}}')]:
  if old in t:
   replace(f.relative_to(c),old,new);t=f.read_text()
refs=c/'bibliography/references.tex';text=refs.read_text();text=text.replace('\\end{thebibliography}', '\\bibitem{DLMF26} NIST Digital Library of Mathematical Functions, \\S23.18, Eq.~23.18.5, \\url{https://dlmf.nist.gov/23.18.E5}.\n\\end{thebibliography}');refs.write_text(text)
main=p/'comparison_main.tex';text=main.read_text();text=text.replace('\\begin{thebibliography}', '\\input{../cbc/chapters/theory/elliptic_normalizations}\n\\input{../cbc/chapters/theory/reduction_obstructions}\n\\begin{thebibliography}');text=text.replace('\\end{thebibliography}', '\\bibitem{DLMF26} NIST Digital Library of Mathematical Functions, \\S23.18, Eq.~23.18.5, \\url{https://dlmf.nist.gov/23.18.E5}.\n\\end{thebibliography}');main.write_text(text)
Path(__file__).with_name('replacements.json').write_text(json.dumps(records,indent=2)+'\n')
print('Successor replacement records',len(records))
