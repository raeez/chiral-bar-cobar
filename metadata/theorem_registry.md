# Theorem Registry

Auto-generated on 2026-07-11 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` and `\ClaimStatusProvedElsewhere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| Proved surface claims | 2105 |
| Total tagged claims | 4683 |
| Active files in `main.tex` | 141 |
| Total `.tex` files scanned | 156 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1666 |
| `ProvedElsewhere` | 439 |
| `Conjectured` | 363 |
| `Conditional` | 1785 |
| `Heuristic` | 29 |
| `Open` | 77 |
| `Definitional` | 324 |

## Proved Surface By Environment

| Environment | Count |
|---|---:|
| `theorem` | 843 |
| `proposition` | 666 |
| `corollary` | 208 |
| `lemma` | 165 |
| `computation` | 78 |
| `remark` | 78 |
| `definition` | 44 |
| `construction` | 19 |
| `calculation` | 4 |

## Proved Surface By Part

| Part | Count |
|---|---:|
| Frame | 23 |
| Part I: Theory | 1057 |
| Part II: Examples | 490 |
| Part III: Connections | 297 |
| Appendices | 238 |

## Most Populated Proved Files

| File | Proved surface claims |
|---|---:|
| `chapters/theory/higher_genus_modular_koszul.tex` | 134 |
| `chapters/connections/arithmetic_shadows.tex` | 122 |
| `chapters/theory/ordered_associative_chiral_kd.tex` | 101 |
| `appendices/ordered_associative_chiral_kd.tex` | 97 |
| `chapters/theory/configuration_spaces.tex` | 65 |
| `appendices/nonlinear_modular_shadows.tex` | 58 |
| `chapters/examples/kac_moody.tex` | 52 |
| `chapters/theory/higher_genus_foundations.tex` | 50 |
| `chapters/examples/free_fields.tex` | 49 |
| `chapters/examples/yangians_computations.tex` | 47 |
| `chapters/examples/yangians_foundations.tex` | 47 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 42 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 41 |
| `chapters/theory/higher_genus_complementarity.tex` | 41 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 40 |
| `chapters/examples/lattice_foundations.tex` | 39 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 35 |
| `chapters/theory/bar_construction.tex` | 35 |
| `chapters/theory/chiral_modules.tex` | 34 |
| `chapters/theory/en_koszul_duality.tex` | 33 |

## Complete Proved Registry

### Frame (23)

#### `chapters/frame/heisenberg_frame.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:frame-arnold` | `proposition` | `ProvedHere` | 568 | 1 | 0 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | `ProvedHere` | 946 | 1 | 0 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | `ProvedHere` | 1048 | 0 | 0 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | `ProvedElsewhere` | 1258 | 0 | 0 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | `ProvedElsewhere` | 1517 | 0 | 0 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | `ProvedElsewhere` | 1539 | 0 | 0 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | `ProvedElsewhere` | 1687 | 0 | 0 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | `ProvedElsewhere` | 1887 | 0 | 0 | Quantum complementarity for Heisenberg |
| `prop:frame-drinfeld-classical-limit` | `proposition` | `ProvedHere` | 2229 | 1 | 0 | Classical limit and vanishing check |
| `thm:frame-fermion-bar` | `theorem` | `ProvedElsewhere` | 2422 | 1 | 0 | Free fermion bar complex; see Theorem~\ref{thm:fermion-bar-complex-genus-0} |
| `thm:rosetta-sl2-swiss` | `theorem` | `ProvedHere` | 2905 | 2 | 0 | $\mathfrak{sl}_2$ bar complex as $E_1$-chiral coassociative coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | `ProvedHere` | 2977 | 3 | 0 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | `ProvedHere` | 3027 | 0 | 0 | Verdier level identification for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} |
| `prop:rosetta-sl2-pva` | `proposition` | `ProvedHere` | 3131 | 3 | 0 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | `ProvedHere` | 3169 | 2 | 0 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | `ProvedHere` | 4103 | 1 | 0 | Odd current $R$-matrix from the bar complex |

#### `chapters/frame/preface.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:preface-arnold` | `proposition` | `ProvedHere` | 72 | 1 | 0 | The three-point Arnold relation |
| `prop:preface-associative-bar-three` | `proposition` | `ProvedHere` | 183 | 0 | 0 | Arity-three associative bar cancellation |
| `thm:preface-point-bar-cobar` | `theorem` | `ProvedElsewhere` | 205 | 0 | 1 | Bar--cobar resolution, Loday--Vallette |
| `thm:preface-quadratic-recognition` | `theorem` | `ProvedElsewhere` | 239 | 0 | 1 | Quadratic Koszul recognition, Loday--Vallette |
| `thm:preface-enhanced-ran-reconstruction` | `theorem` | `ProvedElsewhere` | 288 | 0 | 1 | Enhanced associative Ran reconstruction, Francis--Gaitsgory |
| `prop:preface-mc-formal` | `proposition` | `ProvedHere` | 492 | 0 | 0 | Maurer--Cartan identity |
| `thm:preface-bdsk-benchmarks` | `theorem` | `ProvedElsewhere` | 542 | 0 | 1 | Bakalov--De Sole--Kac benchmarks |

### Part I: Theory (1057)

#### `chapters/theory/algebraic_foundations.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:quadratic-koszul` | `theorem` | `ProvedElsewhere` | 448 | 1 | 3 | Classical Koszul models; {} \cite{Priddy70,BGS96,LV12} |
| `thm:convolution-master-identification` | `theorem` | `ProvedElsewhere` | 666 | 3 | 2 | Convolution = master object identification |
| `cor:theta-twisting-morphism` | `corollary` | `ProvedElsewhere` | 778 | 3 | 2 | MC element = twisting morphism |
| `prop:universal-twisting-adjunction` | `proposition` | `ProvedElsewhere` | 885 | 0 | 1 | Universal twisting morphisms {\cite{LV12}} |
| `thm:operadic-homotopy-convolution` | `theorem` | `ProvedElsewhere` | 1056 | 1 | 1 | Operadic identification of the convolution algebra |
| `cor:quillen-equivalence-chiral` | `corollary` | `ProvedElsewhere` | 1119 | 0 | 1 | Quillen equivalence for chiral bar-cobar |
| `cor:shadow-algebra-homotopy-invariant` | `corollary` | `ProvedElsewhere` | 1159 | 0 | 1 | Homotopy invariance of the shadow algebra |
| `prop:circ-associative` | `proposition` | `ProvedHere` | 1311 | 0 | 1 | Associativity of the composition product |
| `thm:chiral-ran` | `theorem` | `ProvedElsewhere` | 1479 | 1 | 1 | Chiral algebras on Ran space |
| `thm:operadic-bar` | `theorem` | `ProvedElsewhere` | 1804 | 0 | 1 | Operadic bar complex \cite{LV12} |
| `thm:com-lie` | `theorem` | `ProvedElsewhere` | 1919 | 2 | 4 | Com--Lie Koszul duality {\cite{GK94,LV12}} |
| `prop:quadratic-presentations-com-lie` | `proposition` | `ProvedElsewhere` | 2005 | 0 | 1 | Quadratic presentations~\cite{LV12} |
| `prop:orthogonal` | `proposition` | `ProvedHere` | 2014 | 0 | 0 | Orthogonality |
| `thm:chiral-factorization` | `theorem` | `ProvedElsewhere` | 2161 | 0 | 1 | Chiral algebras are factorization algebras |
| `thm:excision-factorization` | `theorem` | `ProvedElsewhere` | 2264 | 1 | 2 | Excision property |
| `thm:factorization-cosheaf` | `theorem` | `ProvedElsewhere` | 2291 | 1 | 1 | Factorization algebras are cosheaves for Weiss covers |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (41)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:curvature-central` | `theorem` | `ProvedHere` | 378 | 0 | 0 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `thm:completion-necessity` | `theorem` | `ProvedHere` | 439 | 0 | 0 | State-space direct sum and weight completion |
| `thm:filtered-cooperads` | `theorem` | `ProvedElsewhere` | 613 | 0 | 1 | Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}) |
| `thm:conilpotency-convergence` | `theorem` | `ProvedElsewhere` | 726 | 0 | 2 | Algebraic bar--cobar resolution and fixed-coalgebra correspondence |
| `comp:virasoro-spectral-r-matrix` | `computation` | `ProvedHere` | 867 | 1 | 0 | Primary-state Virasoro Ward factor |
| `lem:degree-cutoff` | `lemma` | `ProvedHere` | 1049 | 1 | 0 | Degree cutoff: finite MC equation at each stage |
| `prop:mc4-reduction-principle` | `proposition` | `ProvedHere` | 1300 | 0 | 0 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | `ProvedHere` | 1389 | 1 | 0 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | `ProvedHere` | 1429 | 1 | 0 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | `ProvedHere` | 1469 | 2 | 0 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | `ProvedHere` | 1518 | 5 | 0 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | `ProvedHere` | 1575 | 3 | 0 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | `ProvedHere` | 1639 | 0 | 0 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | `ProvedHere` | 1703 | 4 | 0 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | `ProvedHere` | 1742 | 1 | 0 | Comparison with a completed target by compatible finite quotients |
| `thm:completed-twisting-representability` | `theorem` | `ProvedHere` | 2112 | 0 | 0 | Completed twisting representability |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | `ProvedHere` | 3148 | 0 | 0 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | `ProvedHere` | 3247 | 0 | 0 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | `ProvedHere` | 3290 | 1 | 0 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-stage5-transport-target-3` | `proposition` | `ProvedElsewhere` | 5146 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} transport target-\texorpdfstring{$3$}{3} ladder identities |
| `prop:winfty-stage5-transport-target-4` | `proposition` | `ProvedElsewhere` | 5161 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} transport target-\texorpdfstring{$4$}{4} ladder identities |
| `prop:winfty-stage5-transport-target5-35` | `proposition` | `ProvedElsewhere` | 5205 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} transport singleton from \texorpdfstring{$W^{(3)}W^{(5)}$}{W3W5} |
| `prop:winfty-stage5-transport-target5-45` | `proposition` | `ProvedElsewhere` | 5222 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} transport singleton from \texorpdfstring{$W^{(4)}W^{(5)}$}{W4W5} |
| `thm:twisting-mc` | `theorem` | `ProvedElsewhere` | 5808 | 1 | 1 | Twisting by MC elements {\cite{LV12}} |
| `thm:genus-zero-strict` | `theorem` | `ProvedHere` | 6239 | 1 | 0 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | `ProvedHere` | 6251 | 4 | 0 | Strict nilpotence for the corrected genus tower |
| `thm:bar-modular-operad` | `theorem` | `ProvedHere` | 6363 | 2 | 1 | Bar complex as algebra over the modular operad |
| `thm:glz-curved` | `theorem` | `ProvedElsewhere` | 6647 | 0 | 2 | GLZ, Theorem 5.3 |
| `cor:genus-expansion-converges` | `corollary` | `ProvedHere` | 6792 | 1 | 0 | Genus expansion convergence |
| `thm:mixed-boundary-sseq` | `theorem` | `ProvedHere` | 7146 | 0 | 0 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | `ProvedHere` | 7170 | 0 | 0 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | `ProvedHere` | 7218 | 0 | 0 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | `ProvedHere` | 7247 | 0 | 0 | Universality |
| `prop:sugawara-contraction` | `proposition` | `ProvedHere` | 7265 | 0 | 0 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | `ProvedHere` | 7329 | 0 | 0 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | `ProvedHere` | 7345 | 0 | 0 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | `ProvedHere` | 7391 | 0 | 0 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | `ProvedHere` | 7440 | 1 | 0 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | `ProvedHere` | 7484 | 1 | 0 | Diagonal GKO transgression |
| `lem:bcac-curved-MC-on-nearby-cycle` | `lemma` | `ProvedHere` | 7912 | 3 | 1 | Curved Maurer--Cartan on the nearby cycle |
| `lem:bcac-triple-intersection-cocycle-splits` | `lemma` | `ProvedHere` | 8070 | 0 | 1 | Triple-intersection cocycle splits on $H_n\cap H_m$ |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (42)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-convergence` | `theorem` | `ProvedHere` | 68 | 0 | 0 | Finite-window convergence of the bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | `ProvedHere` | 397 | 1 | 1 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | `ProvedHere` | 515 | 0 | 1 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | `ProvedHere` | 588 | 0 | 0 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | `ProvedHere` | 632 | 4 | 0 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | `ProvedHere` | 700 | 2 | 1 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `prop:unit-counit-normalization-bci` | `proposition` | `ProvedHere` | 1131 | 0 | 0 | Unit and counit of the twisting adjunction |
| `prop:bar-cobar-object-firewall-bci` | `proposition` | `ProvedHere` | 1232 | 0 | 0 | Five objects and their canonical morphisms |
| `thm:omega-bar-not-verdier-koszul-dual` | `theorem` | `ProvedHere` | 1273 | 0 | 0 | Reconstruction--Verdier comparison |
| `lem:bar-cobar-associated-graded` | `lemma` | `ProvedHere` | 1775 | 0 | 0 | Associated graded |
| `thm:bar-cobar-inversion-functorial` | `theorem` | `ProvedHere` | 1982 | 0 | 0 | Naturality of universal reconstruction |
| `lem:complete-filtered-comparison` | `lemma` | `ProvedHere` | 2051 | 0 | 0 | Complete filtered comparison lemma |
| `prop:lagrangian-perfectness` | `proposition` | `ProvedHere` | 2602 | 4 | 0 | Perfectness for the standard landscape |
| `prop:subexponential-growth-automatic` | `proposition` | `ProvedHere` | 3708 | 0 | 0 | Tensor-bar counterexample to automatic subexponential growth |
| `cor:finiteness-criterion-reduction` | `corollary` | `ProvedHere` | 3734 | 1 | 0 | Independent growth and geometry obligations |
| `thm:ks-centrality` | `theorem` | `ProvedHere` | 3912 | 0 | 0 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | `ProvedHere` | 3955 | 0 | 0 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | `ProvedHere` | 4007 | 1 | 0 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | `ProvedHere` | 4042 | 0 | 0 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | `ProvedHere` | 4088 | 2 | 0 | Quadratic cone at the scalar basepoint |
| `prop:eta-hessian-transfer` | `proposition` | `ProvedHere` | 4182 | 0 | 0 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | `ProvedHere` | 4218 | 0 | 0 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | `ProvedHere` | 4268 | 0 | 1 | Admissible cyclic rigidity |
| `thm:cech-hca` | `theorem` | `ProvedElsewhere` | 4699 | 0 | 1 | \v{C}ech complex as homotopy chiral algebra |
| `prop:cech-two-element-strict` | `proposition` | `ProvedHere` | 4936 | 1 | 0 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | `ProvedHere` | 5274 | 0 | 0 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | `ProvedHere` | 5334 | 1 | 0 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | `ProvedHere` | 5372 | 0 | 0 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | `ProvedHere` | 5394 | 1 | 0 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | `ProvedHere` | 5492 | 1 | 0 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | `ProvedHere` | 5540 | 2 | 0 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | `ProvedHere` | 5563 | 0 | 0 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | `ProvedHere` | 5608 | 1 | 0 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | `ProvedHere` | 5639 | 1 | 0 | Repeated roots are extension classes |
| `thm:common-core-exact-sequences-inv` | `theorem` | `ProvedHere` | 5710 | 1 | 0 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | `ProvedHere` | 5742 | 2 | 0 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | `ProvedHere` | 5816 | 2 | 0 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | `ProvedHere` | 5856 | 0 | 0 | Explicit coprime-locus projectors |
| `thm:geometric-lift-datum-consequences-inv` | `theorem` | `ProvedHere` | 5960 | 4 | 0 | Divisor-core consequences of lift data |
| `prop:primary-quotient-filtration-lift-inv` | `proposition` | `ProvedHere` | 6013 | 1 | 0 | Primary quotient filtration from lift data |
| `thm:geometric-common-core-factorization-inv` | `theorem` | `ProvedHere` | 6046 | 1 | 0 | Geometric common-core factorization |
| `thm:geometric-ds-common-core-inv` | `theorem` | `ProvedHere` | 6083 | 1 | 0 | Drinfeld--Sokolov common-core transport under lift data |

#### `chapters/theory/bar_construction.tex` (35)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-NAP-homology` | `theorem` | `ProvedHere` | 428 | 1 | 2 | Bar construction as NAP homology |
| `prop:ordered-bar-local-differential-identities` | `proposition` | `ProvedHere` | 870 | 11 | 0 | Ordered bar differential and local identities |
| `prop:ordered-bar-carrier-ran-factorisation` | `proposition` | `ProvedHere` | 1128 | 5 | 0 | Ordered bar carrier and ordered Ran factorisation |
| `lem:ddr-preserves-log` | `lemma` | `ProvedHere` | 1428 | 0 | 1 | $d_{\mathrm{form}}$ preserves logarithmic forms |
| `prop:bar-residue-coordinate-independence` | `proposition` | `ProvedHere` | 1716 | 3 | 0 | Coordinate independence of the collision-residue bar differential |
| `cor:ordered-bar-differential-base-change` | `corollary` | `ProvedHere` | 1791 | 1 | 1 | \'{E}tale and holonomic base-change naturality of the ordered bar differential |
| `lem:sign-compatibility` | `lemma` | `ProvedHere` | 2016 | 1 | 0 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | `ProvedHere` | 2106 | 5 | 0 | Nilpotency of bar differential |
| `thm:bar-sign-coherence` | `theorem` | `ProvedHere` | 2282 | 9 | 0 | Bar sign theorem |
| `prop:pole-decomposition` | `proposition` | `ProvedHere` | 2394 | 4 | 0 | Pole decomposition of the bar differential |
| `cor:ordered-arnold-borcherds-residue-cancellation` | `corollary` | `ProvedHere` | 2506 | 12 | 0 | Ordered Arnold--Borcherds residue cancellation |
| `prop:operator-valued-collision-residue-trace` | `proposition` | `ProvedHere` | 2612 | 6 | 0 | Operator-valued collision residue and scalar trace |
| `thm:stokes-config` | `theorem` | `ProvedHere` | 2818 | 2 | 0 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | `ProvedHere` | 2918 | 0 | 0 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | `ProvedHere` | 2960 | 1 | 0 | Arnold relations |
| `cor:cohomology-config` | `corollary` | `ProvedElsewhere` | 3013 | 1 | 2 | Cohomology of configuration spaces {\cite{Arnold69}} |
| `comp:deg0` | `computation` | `ProvedHere` | 3029 | 0 | 0 | Degree 0 |
| `comp:deg1-general` | `computation` | `ProvedHere` | 3058 | 2 | 0 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | `ProvedHere` | 3301 | 1 | 0 | Bar construction is functorial |
| `prop:model-independence` | `proposition` | `ProvedHere` | 3355 | 0 | 0 | Based comparison of bar models |
| `thm:coassociativity-complete` | `theorem` | `ProvedHere` | 3419 | 0 | 0 | Coassociativity |
| `thm:counit-axioms` | `theorem` | `ProvedHere` | 3486 | 0 | 0 | Counit axioms |
| `thm:diff-is-coderivation` | `theorem` | `ProvedHere` | 3554 | 3 | 1 | Differential is coderivation |
| `lem:orientation` | `lemma` | `ProvedHere` | 3651 | 1 | 1 | Orientation convention |
| `lem:residue-properties` | `lemma` | `ProvedHere` | 3677 | 2 | 0 | Residue properties |
| `lem:LV-sign-comparison` | `lemma` | `ProvedHere` | 3723 | 4 | 1 | Geometric--operadic sign comparison |
| `thm:geometric-equals-operadic-bar` | `theorem` | `ProvedHere` | 4070 | 2 | 3 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | `ProvedHere` | 4180 | 4 | 0 | Arbitrary-mode ordered residue formula |
| `thm:bd-ope-residue-full-poles` | `theorem` | `ProvedHere` | 4268 | 4 | 1 | BD chiral operation and full OPE residue |
| `thm:bar-uniqueness-functoriality` | `theorem` | `ProvedElsewhere` | 4366 | 0 | 0 | Uniqueness and functoriality |
| `thm:ordered-bar-complete-conilpotent-functor` | `theorem` | `ProvedHere` | 4476 | 5 | 0 | Ordered bar as a complete conilpotent functor |
| `prop:dgla-axioms-k3-convolution` | `proposition` | `ProvedHere` | 4753 | 2 | 0 | dGLA axioms for $\mathfrak{C}_{\mathbf{H}_{\Delta_5}}$ |
| `thm:MC-hbar3-hbar4-k3` | `theorem` | `ProvedHere` | 4851 | 2 | 0 | Finite Maurer--Cartan window at $\hbar^3,\hbar^4$ |
| `thm:MC-hbar7-hbar12-k3` | `theorem` | `ProvedHere` | 4884 | 1 | 0 | Finite Maurer--Cartan criterion through $\hbar^{12}$ |
| `lem:bc-polar-support-phi-K3` | `lemma` | `ProvedElsewhere` | 4944 | 0 | 0 | Polar support of the K3 elliptic genus |

#### `chapters/theory/chern_weil_level_shift_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:level-shift-universality` | `theorem` | `ProvedHere` | 195 | 2 | 0 | Level-shift universality with convention separation |
| `prop:shift-appears-universally` | `proposition` | `ProvedHere` | 305 | 1 | 0 | Universal occurrence of $k + \hv$ |
| `thm:h-dual-coxeter-coincidence` | `theorem` | `ProvedHere` | 399 | 2 | 0 | Dual Coxeter coincidence |
| `thm:trace-KZ-convention-bridge` | `theorem` | `ProvedHere` | 477 | 4 | 0 | Trace--KZ convention bridge |
| `cor:level-shift-universal-convention-bridge` | `corollary` | `ProvedHere` | 564 | 3 | 0 | $r$-matrix convention bridge with explicit $k=0$ check |

#### `chapters/theory/chiral_center_theorem.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:endch-spectral-variable-layering` | `remark` | `ProvedHere` | 108 | 0 | 0 | Three layers of chiral spectral variables |
| `prop:pre-lie-chiral` | `proposition` | `ProvedHere` | 268 | 0 | 1 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | `ProvedHere` | 283 | 0 | 1 | Full brace identity |
| `prop:chirhoch1-affine-km` | `proposition` | `ProvedHere` | 658 | 0 | 0 | Affine inner-direction firewall |
| `prop:gerstenhaber-sl2-bracket` | `proposition` | `ProvedHere` | 725 | 1 | 0 | Affine Gerstenhaber bracket on inner directions |

#### `chapters/theory/chiral_climax_platonic.tex` (12)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:arnold-three-term-forms-platonic` | `lemma` | `ProvedElsewhere` | 115 | 0 | 0 | Arnold three-term form identity |
| `thm:arnold-cohomology-platonic` | `theorem` | `ProvedElsewhere` | 151 | 1 | 0 | Arnold 1969 |
| `prop:arnold-flatness-platonic` | `proposition` | `ProvedElsewhere` | 205 | 2 | 0 | Arnold flatness |
| `rem:connconf-initial-platonic` | `remark` | `ProvedHere` | 281 | 4 | 0 | Universal coefficient property |
| `ex:kz-of-vk-g-platonic` | `computation` | `ProvedElsewhere` | 342 | 0 | 0 | Affine Kac--Moody KZ window |
| `thm:kohno-monodromy-platonic` | `theorem` | `ProvedElsewhere` | 658 | 1 | 0 | Kohno 1987 |
| `thm:drinfeld-associator-platonic` | `theorem` | `ProvedElsewhere` | 696 | 0 | 0 | Drinfeld $1989$ |
| `cor:climax-drinfeld-kohno-platonic` | `corollary` | `ProvedElsewhere` | 760 | 2 | 0 | Affine Arnold window and Drinfeld--Kohno |
| `cor:climax-verlinde-platonic` | `corollary` | `ProvedElsewhere` | 786 | 0 | 0 | Verlinde formula on a modular tensor category |
| `cor:climax-arnold-common-root-platonic` | `corollary` | `ProvedHere` | 829 | 1 | 0 | Arnold universal coefficient map |
| `prop:cclimax-SK-spinor` | `proposition` | `ProvedHere` | 1399 | 1 | 0 | Saito--Kurokawa spinor coefficients of \(\Delta_{10}\) for \(p\leq37\) |
| `rem:cclimax-ap-extension` | `remark` | `ProvedHere` | 1448 | 0 | 0 | Extended coefficient window |

#### `chapters/theory/chiral_hochschild_koszul.tex` (40)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:theorem-h-kdh-criterion` | `proposition` | `ProvedHere` | 447 | 2 | 0 | Cohomology of a family support datum |
| `prop:cohochschild-transport-scope-theorem-h` | `proposition` | `ProvedHere` | 478 | 3 | 0 | coHochschild transport scope |
| `lem:arnold-three-point-hochschild` | `lemma` | `ProvedElsewhere` | 513 | 1 | 1 | Three-point Arnold relation |
| `thm:chiral-hochschild-differential` | `theorem` | `ProvedHere` | 537 | 2 | 0 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | `ProvedHere` | 688 | 3 | 0 | chiral Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | `ProvedHere` | 748 | 1 | 0 | chiral Hochschild spectral sequence |
| `lem:hochschild-shift-computation` | `lemma` | `ProvedHere` | 935 | 2 | 0 | Perfect-pairing criterion |
| `lem:totalization-amplitude` | `lemma` | `ProvedHere` | 972 | 0 | 0 | Support under a convergent filtration |
| `prop:fm-tower-collapse` | `proposition` | `ProvedHere` | 1127 | 3 | 0 | Incidence-compatible collision retracts |
| `prop:theorem-h-finite-window-collision-retracts` | `proposition` | `ProvedHere` | 1203 | 3 | 0 | Support from finite-window collision retracts |
| `prop:chirhoch-sharp-hilbert` | `proposition` | `ProvedHere` | 1246 | 2 | 0 | Hilbert series of a family support model |
| `cor:chirhoch-heisenberg` | `corollary` | `ProvedElsewhere` | 1330 | 0 | 1 | Rank-one even superboson bounded cohomology |
| `prop:heisenberg-theorem-h-window-limit` | `proposition` | `ProvedHere` | 1371 | 0 | 0 | Heisenberg finite-window complexes and their inverse limit |
| `cor:chirhoch-virasoro-hilbert` | `corollary` | `ProvedElsewhere` | 1519 | 0 | 1 | Virasoro bounded cohomology |
| `lem:chiral-homotopy-transport` | `lemma` | `ProvedHere` | 1559 | 0 | 5 | The pure-braid Koszul complex and the Arnold algebra |
| `prop:heisenberg-two-point-residue-twisted-acyclicity` | `proposition` | `ProvedHere` | 1676 | 4 | 0 | Two-point Heisenberg residue-twisted Arnold contraction |
| `prop:heisenberg-two-point-weight-one-polynomial-residue` | `proposition` | `ProvedHere` | 1740 | 3 | 0 | Two-point Heisenberg weight-one polynomial residue contraction |
| `prop:heisenberg-two-point-single-oscillator-residue` | `proposition` | `ProvedHere` | 1814 | 3 | 0 | Two-point Heisenberg single-oscillator arbitrary-mode residue contraction |
| `prop:heisenberg-two-point-single-mode-polynomial-residue` | `proposition` | `ProvedHere` | 1891 | 3 | 0 | Two-point Heisenberg single-mode polynomial arbitrary-mode residue contraction |
| `prop:heisenberg-two-point-mixed-mode-residue-formula` | `proposition` | `ProvedHere` | 1973 | 1 | 0 | Two-point Heisenberg mixed-mode residue formula |
| `thm:hochschild-concentration-E1` | `theorem` | `ProvedHere` | 2072 | 2 | 0 | Ordered chiral Hochschild support |
| `thm:boson-fermion-lattice` | `theorem` | `ProvedElsewhere` | 3363 | 0 | 1 | Boson-fermion correspondence via lattice VOA; {} \cite{FK80} |
| `comp:boson-hochschild` | `computation` | `ProvedElsewhere` | 3432 | 2 | 1 | Rank-one even superboson benchmark |
| `prop:genus0-cyclic-coderivation` | `proposition` | `ProvedHere` | 3564 | 2 | 2 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | `ProvedHere` | 3658 | 1 | 0 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `def:modular-cyclic-deformation-complex` | `definition` | `ProvedHere` | 3901 | 0 | 0 | Modular cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | `ProvedHere` | 3960 | 1 | 0 | Genus truncation |
| `prop:fay-trisecant` | `proposition` | `ProvedElsewhere` | 4406 | 0 | 1 | Fay trisecant identity with prime-form normalisation {\cite[Corollary~2.5 |
| `prop:stokes-regularity-FM` | `proposition` | `ProvedHere` | 4446 | 1 | 5 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | `ProvedHere` | 4532 | 6 | 1 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | `ProvedHere` | 4656 | 2 | 0 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | `ProvedHere` | 4839 | 1 | 2 | Strictification principle for modular deformation theory |
| `prop:non-scalar-criterion` | `proposition` | `ProvedHere` | 5858 | 1 | 0 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | `ProvedHere` | 6026 | 0 | 0 | Denominator obstruction to stabilization |
| `thm:geometric-depth-smooth` | `theorem` | `ProvedHere` | 6345 | 0 | 2 | Sharp geometric depth on smooth moduli |
| `thm:string-field-theory-hochschild` | `theorem` | `ProvedElsewhere` | 6768 | 0 | 1 | String field theory from Hochschild {\cite{Zwi93}} |
| `thm:HH-config-space-formula` | `theorem` | `ProvedHere` | 6925 | 3 | 0 | Fulton--MacPherson model for chiral Hochschild cochains |
| `prop:hochschild-cech-ss` | `proposition` | `ProvedHere` | 7502 | 0 | 0 | chiral Hochschild--\v{C}ech spectral sequence |
| `prop:ambient-self-duality` | `proposition` | `ProvedHere` | 7673 | 1 | 0 | Self-duality of the kernel fibre |
| `prop:one-sided-isotropy` | `proposition` | `ProvedHere` | 7712 | 1 | 0 | One-sided isotropy criterion |

#### `chapters/theory/chiral_koszul_pairs.tex` (23)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:ordinary-fundamental-twisting-morphisms` | `theorem` | `ProvedElsewhere` | 393 | 0 | 1 | Fundamental theorem of ordinary twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | `ProvedHere` | 957 | 5 | 0 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | `ProvedHere` | 1040 | 6 | 1 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | `ProvedHere` | 1095 | 5 | 0 | Virasoro chiral Koszulness |
| `prop:ainfty-formality-implies-koszul` | `proposition` | `ProvedHere` | 1435 | 1 | 2 | Formality implies chiral Koszulness |
| `thm:ext-diagonal-vanishing` | `theorem` | `ProvedHere` | 1543 | 1 | 1 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | `ProvedHere` | 1580 | 2 | 0 | PBW universality |
| `prop:li-bar-poisson-differential` | `proposition` | `ProvedHere` | 2113 | 1 | 0 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | `ProvedHere` | 2184 | 4 | 0 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | `ProvedHere` | 2286 | 1 | 0 | Nilradical obstruction at degenerate admissible levels |
| `prop:d-module-purity-km` | `proposition` | `ProvedHere` | 3841 | 0 | 0 | $\cD$-module purity for affine Kac--Moody under localization weights |
| `prop:minimal-model-non-koszul` | `proposition` | `ProvedHere` | 4935 | 0 | 0 | Minimal model non-Koszulness |
| `def:primitive-generating-series` | `definition` | `ProvedHere` | 5011 | 0 | 0 | Primitive generating series |
| `def:completion-hilbert-series` | `definition` | `ProvedHere` | 5033 | 0 | 0 | Completion Hilbert series |
| `def:primitive-defect-series` | `definition` | `ProvedHere` | 5053 | 0 | 0 | Primitive defect series |
| `def:completion-entropy` | `definition` | `ProvedHere` | 5074 | 0 | 0 | Koszul radius and completion entropy |
| `prop:cumulant-window-inversion` | `proposition` | `ProvedHere` | 5133 | 0 | 0 | Cumulant-to-window inversion |
| `thm:yangian-self-dual` | `theorem` | `ProvedHere` | 5612 | 2 | 0 | Type-A Yangian quadratic shadow |
| `prop:yangian-koszul-general` | `proposition` | `ProvedHere` | 5679 | 1 | 5 | Yangian ordered-bar Koszulness in finite windows |
| `lem:completion-convergence` | `lemma` | `ProvedHere` | 6064 | 0 | 1 | Completion convergence |
| `lem:operadic-koszul-transfer` | `lemma` | `ProvedElsewhere` | 6706 | 0 | 2 | Operadic Koszulness transfer \cite{LV12} |
| `prop:bar-neq-quasiprimary` | `proposition` | `ProvedHere` | 7144 | 1 | 0 | Bar cohomology and quasi-primary count |
| `prop:ff-involution-uniqueness` | `proposition` | `ProvedHere` | 7449 | 1 | 0 | Uniqueness of the Feigin--Frenkel involution |

#### `chapters/theory/chiral_modules.tex` (34)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fock-fusion-product` | `proposition` | `ProvedHere` | 241 | 1 | 1 | Fusion product of Heisenberg Fock modules |
| `cor:conformal-block-dim-invariance` | `corollary` | `ProvedHere` | 970 | 2 | 0 | Dimension invariance on the finite-type Verdier surface |
| `prop:generic-irreducibility` | `proposition` | `ProvedElsewhere` | 1687 | 1 | 3 | Generic irreducibility {\cite{Kac,FF84}} |
| `thm:kazhdan-lusztig-equivalence` | `theorem` | `ProvedElsewhere` | 1788 | 0 | 3 | Kazhdan--Lusztig equivalence {\cite{KL93}} |
| `thm:bgg-reciprocity` | `theorem` | `ProvedElsewhere` | 1891 | 0 | 2 | BGG reciprocity for affine algebras {\cite{BGG76, KT95}} |
| `prop:tilting-bar` | `proposition` | `ProvedHere` | 1966 | 1 | 0 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | `ProvedHere` | 2031 | 3 | 2 | Verma module bar complex |
| `thm:zhu-correspondence` | `theorem` | `ProvedElsewhere` | 2183 | 0 | 1 | Zhu's correspondence {\cite{Zhu96}} |
| `cor:virasoro-zhu-koszul` | `corollary` | `ProvedHere` | 2300 | 0 | 1 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | `ProvedHere` | 2335 | 1 | 4 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `thm:arakawa-rationality` | `theorem` | `ProvedElsewhere` | 2424 | 1 | 2 | Arakawa's rationality criterion for admissible affine simples {\cite{Arakawa17,Zhu96}} |
| `lem:free-chiral-module-structure` | `lemma` | `ProvedHere` | 2831 | 0 | 0 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | `ProvedHere` | 2866 | 0 | 0 | Augmented module bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | `ProvedHere` | 2931 | 2 | 0 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | `ProvedHere` | 2948 | 0 | 0 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | `ProvedHere` | 2988 | 0 | 0 | Koszul dual coalgebras linearize module resolutions |
| `cor:character-koszul` | `corollary` | `ProvedHere` | 3049 | 1 | 0 | Character formula for Koszul case |
| `thm:ainfty-module` | `theorem` | `ProvedElsewhere` | 3088 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} module structure {\cite{Kadeishvili80}} |
| `thm:linfty-cochains` | `theorem` | `ProvedElsewhere` | 3127 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} structure on cochains {\cite{KontsevichSoibelman}} |
| `thm:chiral-gerstenhaber` | `theorem` | `ProvedElsewhere` | 3144 | 0 | 2 | Chiral Gerstenhaber algebra {\cite{Ger63,Tamarkin00}} |
| `thm:weyl-kac-denominator` | `theorem` | `ProvedElsewhere` | 3170 | 0 | 1 | Denominator identity for trivial module {\cite{Kac}} |
| `prop:bgg-sl2-level1` | `proposition` | `ProvedElsewhere` | 3500 | 0 | 1 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda-0)} {\cite{BGG76}} |
| `prop:shapovalov-koszul` | `proposition` | `ProvedHere` | 3956 | 1 | 1 | Shapovalov form under Koszul duality |
| `prop:virasoro-kac-koszul` | `proposition` | `ProvedHere` | 4235 | 0 | 2 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | `ProvedHere` | 4338 | 0 | 0 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | `ProvedHere` | 4397 | 0 | 2 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:4463` | `calculation` | `ProvedHere` | 4463 | 0 | 0 | Boson vacuum module |
| `thm:beilinson-bernstein` | `theorem` | `ProvedElsewhere` | 4575 | 0 | 1 | Beilinson--Bernstein {\cite{BB81}} |
| `thm:chiral-localization` | `theorem` | `ProvedElsewhere` | 4607 | 0 | 1 | Chiral localization {\cite{FG06}} |
| `prop:affine-hecke-kd` | `proposition` | `ProvedElsewhere` | 4717 | 1 | 2 | Affine Hecke algebra and Koszul duality {\cite{BGS96}} |
| `prop:bar-singular-support` | `proposition` | `ProvedHere` | 4771 | 1 | 1 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | `ProvedHere` | 4825 | 2 | 1 | DS reduction commutes with the module bar construction on the exact lane |
| `cor:ds-character-compatibility` | `corollary` | `ProvedHere` | 4958 | 1 | 0 | Characters under DS reduction |
| `prop:heisenberg-fusion-splitting` | `proposition` | `ProvedHere` | 5729 | 3 | 0 | Heisenberg fusion splitting |

#### `chapters/theory/climax_theorem.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `cor:climax-drinfeld-kohno` | `corollary` | `ProvedHere` | 152 | 0 | 0 | Drinfeld--Kohno along $A \mapsto U_q$ |
| `cor:climax-borcherds` | `corollary` | `ProvedHere` | 169 | 0 | 0 | Borcherds along $A \mapsto V_\Lambda$ |
| `cor:climax-verlinde` | `corollary` | `ProvedHere` | 185 | 0 | 0 | Verlinde along $A \mapsto \mathrm{RCFT}$ |

#### `chapters/theory/clutching_uniqueness_platonic.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:mumford-hodge-clutching-top-chern` | `lemma` | `ProvedElsewhere` | 112 | 0 | 1 | Mumford clutching formula for Hodge top Chern classes |
| `thm:clutching-uniqueness-socle-projection` | `theorem` | `ProvedHere` | 234 | 2 | 3 | Clutching uniqueness on the socle |
| `cor:genus-2-explicit-match` | `corollary` | `ProvedHere` | 602 | 1 | 1 | Explicit match at genus $2$ |
| `lem:theorem-D-type-discipline` | `lemma` | `ProvedHere` | 855 | 0 | 0 | Type discipline in the identity $\mathrm{obs}_g=\kscal\cdot\lambda_g$ |
| `prop:theta-A-genus1` | `proposition` | `ProvedHere` | 912 | 2 | 2 | Genus-$1$ MC element |
| `prop:mc-direct-g1-verification` | `proposition` | `ProvedHere` | 1308 | 1 | 2 | $g=1$ direct MC verification |
| `prop:grr-verification-all-g` | `proposition` | `ProvedHere` | 1339 | 3 | 1 | GRR verification at all $g$ |

#### `chapters/theory/cobar_construction.tex` (24)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:schwartz-kernel-cobar` | `theorem` | `ProvedElsewhere` | 220 | 0 | 1 | Schwartz kernel theorem for cobar {\cite{Hormander}} |
| `lem:bar-holonomicity` | `lemma` | `ProvedHere` | 360 | 2 | 2 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | `ProvedHere` | 421 | 0 | 1 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | `ProvedHere` | 454 | 5 | 0 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | `ProvedHere` | 546 | 3 | 0 | Uncurved cobar nilpotence and curved square via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | `ProvedHere` | 709 | 0 | 0 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | `ProvedHere` | 840 | 3 | 0 | Uncurved distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | `ProvedHere` | 1098 | 0 | 0 | Sign consistency for the uncurved cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | `ProvedHere` | 1301 | 2 | 1 | Fermion-boson Koszul duality |
| `lem:verdier-bar-square-zero-toy` | `lemma` | `ProvedHere` | 1716 | 0 | 0 | Square-zero fibre verification: the dual of the bar coalgebra is the completed quadratic dual |
| `thm:kontsevich-formality` | `theorem` | `ProvedElsewhere` | 2060 | 0 | 1 | Kontsevich formality (1997) {\cite{Kon99}} |
| `thm:complete-conilpotent-cobar-functor` | `theorem` | `ProvedHere` | 2224 | 4 | 0 | Complete conilpotent chiral cobar functor |
| `thm:cobar-free` | `theorem` | `ProvedHere` | 2314 | 1 | 0 | Cobar as free chiral algebra |
| `lem:cobar-derivation-extension` | `lemma` | `ProvedHere` | 2547 | 2 | 1 | Cobar derivation extension |
| `thm:weak-topology` | `theorem` | `ProvedHere` | 2956 | 0 | 0 | Topology |
| `thm:cobar-ainfty` | `theorem` | `ProvedElsewhere` | 3147 | 0 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} structure on cobar {\cite{LV12}} |
| `thm:curved-mc-cobar` | `theorem` | `ProvedHere` | 3195 | 3 | 2 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | `ProvedHere` | 3246 | 1 | 0 | Affine modular curvature scalar |
| `thm:central-charge-cocycle` | `theorem` | `ProvedHere` | 3500 | 1 | 0 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | `ProvedHere` | 3606 | 3 | 0 | Genus 1 cobar extraction of the Heisenberg central extension |
| `thm:bar-complex-spectral-sequence` | `theorem` | `ProvedHere` | 3853 | 2 | 2 | Bar complex spectral sequence |
| `cor:spectral-degeneration` | `corollary` | `ProvedElsewhere` | 3938 | 1 | 1 | Degeneration {\cite{BGS96}} |
| `thm:koszul-necessary` | `theorem` | `ProvedElsewhere` | 4295 | 0 | 1 | Necessary conditions for chiral Koszul duality {\cite{FG12}} |
| `lem:deformation-space` | `lemma` | `ProvedHere` | 4556 | 1 | 0 | Deformation space under center transport |

#### `chapters/theory/coderived_models.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:co-contra-correspondence-appendix` | `theorem` | `ProvedElsewhere` | 110 | 1 | 1 | Comodule-contramodule correspondence |
| `thm:conilpotent-reduction` | `theorem` | `ProvedElsewhere` | 132 | 1 | 1 | Conilpotent reduction |

#### `chapters/theory/compact_completed_mc3_comparison_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:compact-completed-mc3-comparison` | `theorem` | `ProvedHere` | 167 | 3 | 0 | Compact/completed MC3 comparison |
| `prop:compact-approximation-exists` | `proposition` | `ProvedHere` | 318 | 2 | 0 | Finite-window approximation exists |
| `lem:dense-thick-generation-lifting` | `lemma` | `ProvedElsewhere` | 410 | 0 | 0 | Finite-window dense generation lifting |
| `thm:mc3-full-DK-in-completed-category` | `theorem` | `ProvedHere` | 445 | 3 | 0 | MC3 generation in the completed finite-window category |
| `cor:comparison-gap-resolved-completed` | `corollary` | `ProvedHere` | 499 | 4 | 0 | Compact/completed comparison inside the finite-window ambient |

#### `chapters/theory/computational_methods.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:comp-sqrt-recursion` | `lemma` | `ProvedHere` | 88 | 2 | 0 | Taylor recursion for the formal square root |
| `thm:comp-denom-pattern` | `theorem` | `ProvedHere` | 196 | 1 | 0 | Denominator theorem |
| `prop:comp-shadow-connection-properties` | `proposition` | `ProvedHere` | 246 | 0 | 0 | Properties of the shadow connection |
| `thm:comp-shadow-asymptotics` | `theorem` | `ProvedHere` | 373 | 0 | 0 | Shadow asymptotics |
| `prop:comp-borel-summability` | `proposition` | `ProvedHere` | 473 | 0 | 0 | Borel summability |
| `prop:comp-mc-recursion` | `proposition` | `ProvedHere` | 523 | 0 | 0 | MC recursion |
| `thm:comp-alg-rec-equivalence` | `theorem` | `ProvedHere` | 552 | 2 | 0 | Algebraic--recursive equivalence |
| `thm:comp-ds-consistency` | `theorem` | `ProvedHere` | 619 | 0 | 0 | DS transfer consistency |
| `thm:comp-zhu-c-dependence` | `theorem` | `ProvedHere` | 769 | 0 | 0 | $c$-dependence for simple quotients |
| `prop:comp-explicit-theta-sl2` | `proposition` | `ProvedHere` | 909 | 0 | 0 | Explicit $\Theta$ for $\AffKM{sl}_2$ |
| `thm:comp-siegel-weil-e8` | `theorem` | `ProvedElsewhere` | 1020 | 0 | 0 | Siegel--Weil for $E_8$ |
| `thm:comp-e8-three-way` | `theorem` | `ProvedHere` | 1052 | 0 | 0 | $E_8$ genus-$2$ agreement |
| `prop:comp-n2-kappa` | `proposition` | `ProvedHere` | 1204 | 0 | 0 | Modular characteristic |
| `prop:comp-n2-spectral-flow` | `proposition` | `ProvedHere` | 1267 | 0 | 0 | Spectral flow invariance |
| `thm:comp-genus2-cross` | `theorem` | `ProvedHere` | 1315 | 0 | 0 | Cross-consistency at genus~$2$ |
| `thm:s3-virasoro-c-independent` | `theorem` | `ProvedHere` | 1553 | 0 | 0 | $c$-independence of $S_3$ for Virasoro |

#### `chapters/theory/configuration_spaces.tex` (65)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:FM` | `theorem` | `ProvedElsewhere` | 252 | 0 | 1 | Fulton--MacPherson compactification at genus \texorpdfstring{$g$}{g} \cite{FM94} |
| `thm:boundary-higher-genus` | `theorem` | `ProvedElsewhere` | 425 | 2 | 2 | Boundary strata of \texorpdfstring{$\overline{\mathcal{M}}_{g,n}$}{M-bar(g,n)} {\cite{DeligneM69,Knudsen83}} |
| `thm:local-coords-boundary` | `theorem` | `ProvedHere` | 551 | 0 | 0 | Local holomorphic coordinates near a collision divisor |
| `thm:normal-crossings` | `theorem` | `ProvedHere` | 640 | 0 | 0 | Normal crossings |
| `thm:closure-relations` | `theorem` | `ProvedHere` | 750 | 0 | 0 | Closure relations |
| `cor:dimension-strata` | `corollary` | `ProvedElsewhere` | 781 | 0 | 1 | Boundary divisors in the FM compactification \cite{FM94} |
| `thm:boundary-stratification` | `theorem` | `ProvedElsewhere` | 803 | 0 | 1 | Boundary stratification \cite{FM94} |
| `thm:log-complex` | `theorem` | `ProvedHere` | 885 | 0 | 1 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | `ProvedHere` | 923 | 3 | 1 | Arnold relations and KZ flatness |
| `prop:arnold-higher-genus` | `proposition` | `ProvedHere` | 1064 | 5 | 4 | Higher-genus correction to the affine Arnold scalar presentation |
| `prop:twisting-morphism-propagator` | `proposition` | `ProvedHere` | 1373 | 4 | 0 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | `ProvedHere` | 1449 | 1 | 0 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | `ProvedHere` | 1488 | 2 | 0 | Residue operations |
| `prop:residue-local` | `proposition` | `ProvedHere` | 1558 | 1 | 0 | Residue computation in local coordinates |
| `rem:residues-and-ope` | `remark` | `ProvedHere` | 1591 | 0 | 0 | Residues and OPE: pole absorption by the propagator |
| `thm:residue-sequence` | `theorem` | `ProvedHere` | 1645 | 1 | 0 | Residue sequence |
| `thm:FM-functorial` | `theorem` | `ProvedElsewhere` | 1692 | 0 | 1 | Functoriality of FM compactification |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1713` | `remark` | `ProvedElsewhere` | 1713 | 0 | 1 | Provenance and citation |
| `thm:FM-operad` | `theorem` | `ProvedElsewhere` | 1720 | 0 | 2 | Universal property: FM right-module structure {\cite{FM94,LV12}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1741` | `remark` | `ProvedElsewhere` | 1741 | 0 | 2 | Provenance and citation |
| `thm:fact-homology` | `theorem` | `ProvedElsewhere` | 1763 | 0 | 3 | Factorization homology via configuration spaces {\cite{AF15,CG17,BD04}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1777` | `remark` | `ProvedElsewhere` | 1777 | 0 | 3 | Provenance and citation |
| `def:log-fm-compactification` | `definition` | `ProvedElsewhere` | 1853 | 0 | 1 | Logarithmic FM compactification \cite{Mok25} |
| `rem:boundary-ordering-associahedron` | `remark` | `ProvedHere` | 2293 | 0 | 0 | Boundary ordering and the associahedron |
| `thm:bordered-fm-properties` | `theorem` | `ProvedHere` | 2463 | 2 | 0 | Properties of the bordered FM compactification |
| `lem:nested-blowup-commutativity` | `lemma` | `ProvedElsewhere` | 2541 | 0 | 1 | Nested blowup commutativity |
| `prop:four-type-boundary` | `proposition` | `ProvedHere` | 2562 | 2 | 0 | Fixed and relative boundary decomposition |
| `prop:fundamental-group-genera` | `proposition` | `ProvedElsewhere` | 3676 | 0 | 2 | Fundamental group across genera \cite{Arnold69,Brieskorn73} |
| `thm:fm-associahedron` | `theorem` | `ProvedElsewhere` | 3797 | 0 | 1 | FM compactification and associahedra {\cite{Sta63}} |
| `prop:eta` | `proposition` | `ProvedHere` | 3804 | 1 | 0 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:os-cohomology-config` | `theorem` | `ProvedElsewhere` | 3849 | 0 | 2 | Cohomology via Orlik--Solomon {\cite{Arnold69,OS80}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3863` | `remark` | `ProvedElsewhere` | 3863 | 0 | 2 | Provenance and citation |
| `thm:NBC` | `theorem` | `ProvedElsewhere` | 3890 | 0 | 1 | NBC basis theorem {\cite{OS80}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3899` | `remark` | `ProvedElsewhere` | 3899 | 0 | 1 | Provenance and citation |
| `thm:chiral-as-fact` | `theorem` | `ProvedElsewhere` | 4018 | 0 | 1 | Chiral algebras as factorization algebras \cite{BD04} |
| `thm:fact-monoidal-corrected` | `theorem` | `ProvedElsewhere` | 4036 | 0 | 2 | Factorization monoidal structure {\cite{BD04,CG17}} |
| `thm:elliptic-compactification` | `theorem` | `ProvedElsewhere` | 4079 | 0 | 1 | Elliptic compactification {\cite{Fay73}} |
| `prop:elliptic-arnold-relations` | `proposition` | `ProvedElsewhere` | 4122 | 0 | 1 | Elliptic correction to the Arnold relation \cite{Fay73} |
| `lem:orientation-compatibility` | `lemma` | `ProvedHere` | 4300 | 0 | 0 | Orientation compatibility |
| `thm:stokes-config-spaces` | `theorem` | `ProvedElsewhere` | 4326 | 0 | 1 | Stokes on configuration spaces \cite{FM94} |
| `prop:operadic-structure` | `proposition` | `ProvedHere` | 4361 | 0 | 0 | Operadic structure |
| `thm:chiral-algebra-objects` | `theorem` | `ProvedElsewhere` | 4387 | 0 | 1 | Chiral algebras as algebra objects \cite{BD04} |
| `thm:nbc-basis-optimality` | `theorem` | `ProvedHere` | 4401 | 3 | 0 | Exact NBC reduction for the affine OS component |
| `prop:nbc-sparsity` | `proposition` | `ProvedHere` | 4459 | 0 | 0 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | `ProvedHere` | 4481 | 1 | 1 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | `ProvedHere` | 4524 | 2 | 0 | Arnold relations on affine boundary screens |
| `thm:permutohedral-cell-complex` | `theorem` | `ProvedHere` | 4562 | 0 | 0 | Permutohedral cell complex of the compactified real line |
| `thm:complexity-bounds` | `theorem` | `ProvedHere` | 4624 | 0 | 0 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | `ProvedHere` | 4647 | 2 | 0 | Finite-window spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | `ProvedHere` | 4708 | 2 | 0 | Residue evaluation complexity |
| `thm:arnold-jacobi` | `theorem` | `ProvedElsewhere` | 4837 | 3 | 1 | Arnold relation $\Leftrightarrow$ simple-pole Jacobi on the affine screen \cite{LV12} |
| `cor:arnold-operadic` | `corollary` | `ProvedElsewhere` | 4868 | 0 | 1 | Operadic associativity \cite{LV12} |
| `thm:arnold-orlik-solomon` | `theorem` | `ProvedHere` | 4878 | 0 | 0 | Arnold--Orlik--Solomon circuit relations |
| `cor:bar-d-squared-zero` | `corollary` | `ProvedHere` | 4911 | 4 | 0 | Affine scalar residue differential squares to zero |
| `thm:elliptic-logarithmic-forms` | `theorem` | `ProvedElsewhere` | 4933 | 0 | 1 | Elliptic logarithmic forms \cite{Fay73} |
| `thm:normal-crossings-preservation` | `theorem` | `ProvedHere` | 4960 | 1 | 1 | Normal crossings preservation |
| `thm:complete-coordinates` | `theorem` | `ProvedHere` | 5198 | 0 | 0 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | `ProvedHere` | 5251 | 0 | 0 | Normal bundle formula |
| `prop:transition-functions` | `proposition` | `ProvedElsewhere` | 5320 | 0 | 1 | Transition functions \cite{FM94} |
| `thm:normal-crossings-verified` | `theorem` | `ProvedHere` | 5398 | 0 | 0 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5609` | `computation` | `ProvedElsewhere` | 5609 | 0 | 0 | Explicit examples |
| `thm:chiral-ran-Dmod` | `theorem` | `ProvedElsewhere` | 5730 | 0 | 2 | Chiral algebras ↔ D-modules on Ran space {\cite{BD04,FG12}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5736` | `remark` | `ProvedElsewhere` | 5736 | 0 | 3 | Provenance and citation |
| `thm:chiral-homology-ran` | `theorem` | `ProvedElsewhere` | 5746 | 0 | 2 | Chiral homology via Ran space {\cite{BD04,CG17}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5754` | `remark` | `ProvedElsewhere` | 5754 | 0 | 3 | Provenance and citation |

#### `chapters/theory/conformal_anomaly_rigidity_platonic.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:casimir-nonvanishing` | `lemma` | `ProvedHere` | 165 | 0 | 2 | Nonvanishing and integrality of $\Cas$ |
| `thm:conformal-anomaly-rigidity` | `theorem` | `ProvedHere` | 209 | 2 | 0 | Conformal-anomaly rigidity |
| `thm:c-zero-coproduct-is-constant` | `theorem` | `ProvedHere` | 267 | 1 | 4 | Coproduct is constant at $c = 0$ |
| `prop:spectral-parameter-forced-at-nonzero-c` | `proposition` | `ProvedHere` | 305 | 3 | 0 | Spectral parameter is forced at $c \neq 0$ |
| `thm:universal-coefficient` | `theorem` | `ProvedHere` | 329 | 1 | 0 | Universality of the coefficient |
| `cor:chiralization-obstructed-away-from-c-zero` | `corollary` | `ProvedHere` | 370 | 4 | 0 | Chiralisation is obstructed away from $c = 0$ |
| `rem:comparison-with-ktheory-anomaly` | `remark` | `ProvedElsewhere` | 396 | 1 | 0 | Comparison with the Virasoro \texorpdfstring{$\kappa$}{kappa}-conductor |

#### `chapters/theory/derived_langlands.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:ff-center-dl` | `theorem` | `ProvedElsewhere` | 307 | 0 | 2 | Feigin--Frenkel center |
| `thm:kl-equivalence` | `theorem` | `ProvedElsewhere` | 1223 | 0 | 2 | Kazhdan--Lusztig--Finkelberg equivalence on the semisimplified target |
| `thm:fg-localization` | `theorem` | `ProvedElsewhere` | 1468 | 0 | 1 | Frenkel--Gaitsgory localization |
| `thm:dl-pseudocharacter-delta10` | `theorem` | `ProvedHere` | 3500 | 4 | 0 | Four-dimensional Chenevier determinant on $\Tpar_1$ for $\Delta_{10}$ |
| `thm:dl-chenevier-nonreduced-delta5` | `theorem` | `ProvedHere` | 3764 | 1 | 0 | Chenevier determinant on the non-reduced deformation ring $R^{\mathrm{def}}_{\Delta_5}$ |

#### `chapters/theory/e1_modular_koszul.tex` (19)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:ribbon-modular-operad` | `definition` | `ProvedElsewhere` | 171 | 0 | 2 | Ribbon modular operad {\cite{GeK98,CG17}} |
| `def:feynman-transform-ass` | `definition` | `ProvedElsewhere` | 242 | 0 | 0 | Feynman transform of the associative modular operad |
| `thm:fass-d-squared-zero` | `theorem` | `ProvedHere` | 271 | 0 | 1 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | `ProvedHere` | 290 | 1 | 1 | — |
| `prop:e1-nonsplitting-obstruction` | `proposition` | `ProvedHere` | 487 | 1 | 2 | $E_1$ canonical section obstruction |
| `prop:e1-nonsplitting-genus1` | `proposition` | `ProvedHere` | 595 | 3 | 0 | $E_1$ genus-one modular-section obstruction |
| `prop:symmetric-descent-e1mkd` | `proposition` | `ProvedHere` | 1039 | 0 | 0 | Symmetric descent |
| `prop:elliptic-kzb-flatness-jacobi` | `proposition` | `ProvedElsewhere` | 2133 | 1 | 2 | Elliptic KZB flatness and scope |
| `thm:e1-formality-bridge` | `theorem` | `ProvedHere` | 2355 | 0 | 0 | Formality bridge |
| `thm:e1-formality-failure` | `theorem` | `ProvedHere` | 2394 | 1 | 0 | Formality failure for genuinely $\Eone$-chiral algebras |
| `rem:ribbon-structure-count` | `remark` | `ProvedHere` | 2646 | 0 | 0 | Ribbon structure count |
| `constr:kz-associator-e1-shadow` | `construction` | `ProvedHere` | 2969 | 0 | 0 | KZ associator as degree-$3$ $E_1$ shadow of $\hat\fg_k$ |
| `constr:modular-r-matrix-genus1` | `construction` | `ProvedHere` | 3026 | 0 | 0 | Formal ordered degree-$2$ shadow series |
| `rem:lie-associative-dichotomy` | `remark` | `ProvedHere` | 3536 | 0 | 0 | Lie/associative dichotomy in the averaging kernel |
| `prop:sn-irrep-decomposition-bar` | `proposition` | `ProvedHere` | 3562 | 0 | 1 | $\Sigma_n$-irreducible decomposition of the ordered bar complex |
| `lem:bare-graph-no-thooft` | `lemma` | `ProvedHere` | 3672 | 0 | 0 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | `ProvedHere` | 3693 | 0 | 0 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | `ProvedHere` | 3735 | 0 | 0 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | `ProvedHere` | 3757 | 1 | 0 | Exact $N^{\chi}$ weighting from traced open color |

#### `chapters/theory/en_koszul_duality.tex` (33)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:arnold-presentation` | `theorem` | `ProvedElsewhere` | 300 | 1 | 1 | Arnold presentation {\cite{Arnold69}}; \texorpdfstring{$\bC \cong \bR^2$}{C = R2} |
| `thm:totaro-presentation` | `theorem` | `ProvedElsewhere` | 317 | 0 | 2 | Totaro presentation, general \texorpdfstring{$n$}{n} {\cite{Totaro96, Coh76}} |
| `prop:fm-boundary-strata` | `proposition` | `ProvedElsewhere` | 402 | 0 | 2 | Boundary strata and operadic structure |
| `prop:linking-sphere-residue` | `proposition` | `ProvedHere` | 529 | 1 | 0 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | `ProvedHere` | 604 | 2 | 1 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `thm:en-koszul-duality` | `theorem` | `ProvedElsewhere` | 758 | 0 | 3 | \texorpdfstring{$\En$}{En} Koszul duality |
| `thm:af-pkd` | `theorem` | `ProvedElsewhere` | 859 | 0 | 1 | Poincar\'e--Koszul duality, AF {\cite{AF15}} |
| `thm:en-d-squared` | `theorem` | `ProvedElsewhere` | 969 | 1 | 1 | \texorpdfstring{$d^2 = 0$}{d squared = 0} for the \texorpdfstring{$\En$}{En} bar complex |
| `prop:kappa-universality-en` | `proposition` | `ProvedHere` | 1016 | 0 | 0 | Kappa universality across $n$ |
| `thm:knudsen-higher-enveloping` | `theorem` | `ProvedElsewhere` | 1122 | 0 | 1 | Higher enveloping algebras |
| `thm:e2-formality` | `theorem` | `ProvedElsewhere` | 1152 | 0 | 2 | Formality of \texorpdfstring{$\Etwo$}{E2} |
| `prop:en-formality` | `proposition` | `ProvedElsewhere` | 1187 | 1 | 2 | \texorpdfstring{$\En$}{En} formality for \texorpdfstring{$n \geq 2$}{n >= 2} |
| `thm:willwacher-wheels` | `theorem` | `ProvedElsewhere` | 1242 | 0 | 1 | Wheel cocycles and $\mathrm{grt}_1$ |
| `prop:shadow-gc2-bridge` | `proposition` | `ProvedHere` | 1265 | 1 | 0 | Shadow obstruction tower to $\mathrm{GC}_2$ bridge |
| `prop:sc-chtop-boundary-relation-ledger` | `proposition` | `ProvedHere` | 1478 | 6 | 0 | $\mathsf{SC}^{\mathrm{ch,top}}$ boundary-relation ledger |
| `thm:bar-swiss-cheese` | `theorem` | `ProvedHere` | 1622 | 3 | 0 | Bar complex as $\Eone$-chiral coassociative coalgebra |
| `prop:sc-koszul-dual-three-sectors` | `proposition` | `ProvedHere` | 1928 | 1 | 0 | Koszul dual cooperad of \texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}: three sectors |
| `cor:convolution-factorization` | `corollary` | `ProvedHere` | 1970 | 2 | 0 | Convolution algebra factorization |
| `prop:operadic-center-existence` | `proposition` | `ProvedHere` | 2082 | 1 | 0 | Existence of the operadic center |
| `thm:operadic-center-hochschild` | `theorem` | `ProvedHere` | 2135 | 6 | 2 | The operadic center of $\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex |
| `prop:braces-from-center` | `proposition` | `ProvedHere` | 2683 | 2 | 0 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | `ProvedHere` | 2732 | 5 | 1 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | `ProvedHere` | 2811 | 1 | 0 | Terminality of the center |
| `cor:center-functor` | `corollary` | `ProvedHere` | 2900 | 1 | 0 | The fiberwise center section |
| `constr:sugawara-antighost` | `construction` | `ProvedHere` | 4144 | 4 | 0 | The Sugawara antighost contraction for affine Kac--Moody |
| `thm:coset-conformal-inheritance` | `theorem` | `ProvedHere` | 4566 | 0 | 1 | Coset conformal inheritance |
| `thm:cfg` | `theorem` | `ProvedElsewhere` | 5402 | 0 | 1 | Costello--Francis--Gwilliam~\cite{CFG25} |
| `lem:en-formality-deformation-classification` | `lemma` | `ProvedHere` | 5527 | 0 | 4 | Formality reduction for $\En$-deformations of commutative algebras |
| `prop:chiral-p3-structure` | `proposition` | `ProvedHere` | 6723 | 1 | 1 | The chiral $\Pthree$ structure |
| `thm:chiral-e3-structure` | `theorem` | `ProvedHere` | 6810 | 3 | 4 | Structure of the chiral $\Ethree$-algebra |
| `lem:bv-p3-commutativity` | `lemma` | `ProvedHere` | 7070 | 2 | 2 | Commutativity of the BV operator and the chiral $\Pthree$ bracket |
| `prop:chiral-e3-dmod` | `proposition` | `ProvedHere` | 7214 | 1 | 1 | The $\cD$-module structure |
| `thm:chiral-e3-cfg` | `theorem` | `ProvedHere` | 7300 | 4 | 3 | Formal disk restriction recovers CFG |

#### `chapters/theory/existence_criteria.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:existence-four-loci` | `proposition` | `ProvedHere` | 169 | 1 | 1 | Four loci in the existence problem |
| `prop:recognition-not-existence` | `proposition` | `ProvedHere` | 238 | 0 | 0 | Recognition targets are not existence criteria |
| `prop:finite-stage-obstruction-classes` | `proposition` | `ProvedHere` | 727 | 1 | 0 | Finite-stage obstruction classes |
| `thm:completion-convergence-criteria` | `theorem` | `ProvedHere` | 859 | 1 | 0 | Finite-window convergence for the universal resolution |
| `prop:kac-moody-koszul-duals` | `proposition` | `ProvedElsewhere` | 1134 | 1 | 2 | Affine Kac--Moody existence criterion \cite{FBZ04, Feigin-Frenkel} |

#### `chapters/theory/fourier_seed.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | `ProvedHere` | 61 | 0 | 0 | Three properties of the propagator |
| `prop:fourier-com-lie-duality` | `proposition` | `ProvedHere` | 237 | 0 | 0 | — |
| `comp:fourier-heisenberg-n2` | `computation` | `ProvedHere` | 284 | 1 | 0 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | `ProvedHere` | 333 | 2 | 0 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | `ProvedHere` | 362 | 4 | 0 | Heisenberg bar seed |
| `prop:fourier-propagator-degeneration` | `proposition` | `ProvedHere` | 584 | 0 | 2 | Degeneration of the propagator |
| `comp:fourier-km-bar` | `computation` | `ProvedHere` | 830 | 0 | 0 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | `ProvedHere` | 851 | 1 | 1 | — |
| `thm:fourier-specialization` | `theorem` | `ProvedHere` | 896 | 0 | 1 | Specialization |

#### `chapters/theory/genus_2_ddybe_platonic.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:genus-2-kzb-connection-platonic` | `theorem` | `ProvedElsewhere` | 170 | 0 | 2 | Flat KZB connection on $\overline{\cM}_{2,n}\times\HHH_2$ |
| `thm:fay-trisecant-genus-2-specific` | `theorem` | `ProvedElsewhere` | 255 | 0 | 1 | Fay trisecant, normalised Szeg\H{o}/prime-form form |
| `thm:g2-face-model-bypass-scope-restricted` | `theorem` | `ProvedHere` | 394 | 4 | 1 | Exact diagonal/separating degeneration to Felder DYBE |
| `cor:g2-chi-minus-12` | `corollary` | `ProvedHere` | 685 | 1 | 0 | $\chi=-12$ from rank-$4$ KZB local system |

#### `chapters/theory/higher_genus_complementarity.tex` (41)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:theorem-c-object-firewall` | `proposition` | `ProvedHere` | 399 | 0 | 0 | Object firewall for Theorem~C |
| `lem:involution-splitting` | `lemma` | `ProvedHere` | 623 | 0 | 0 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | `ProvedHere` | 679 | 2 | 0 | Perfectness criterion for the strict flat relative bar family |
| `lem:genus-filtration` | `lemma` | `ProvedHere` | 1241 | 1 | 0 | Genus filtration |
| `thm:ss-quantum` | `theorem` | `ProvedHere` | 1305 | 3 | 0 | Spectral sequence for quantum corrections |
| `thm:verdier-duality-config-complete` | `theorem` | `ProvedHere` | 1577 | 4 | 1 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | `ProvedHere` | 1656 | 3 | 0 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | `ProvedHere` | 1696 | 5 | 0 | Spectral sequence duality |
| `thm:ss-genus-stratification` | `theorem` | `ProvedHere` | 3002 | 2 | 0 | External genus grading of the modular flat bar object |
| `thm:fermion-boson-koszul-hg` | `theorem` | `ProvedHere` | 3690 | 0 | 0 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | `ProvedHere` | 4250 | 0 | 0 | BD 3.4.12: genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | `ProvedHere` | 4300 | 0 | 1 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | `ProvedHere` | 4313 | 0 | 2 | Normal crossings persist at higher genus |
| `lem:relative-diagonal` | `lemma` | `ProvedHere` | 4414 | 0 | 0 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | `ProvedHere` | 4454 | 0 | 1 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | `ProvedHere` | 4482 | 0 | 0 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | `ProvedHere` | 4504 | 1 | 0 | Chevalley--Cousin at boundary |
| `lem:graded-acyclic` | `lemma` | `ProvedHere` | 4791 | 0 | 1 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | `ProvedHere` | 4879 | 0 | 0 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | `ProvedHere` | 4906 | 4 | 1 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | `ProvedHere` | 4934 | 0 | 0 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | `ProvedHere` | 4970 | 0 | 1 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | `ProvedHere` | 5000 | 3 | 0 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | `ProvedHere` | 5053 | 1 | 1 | Geometric bar and factorization chains |
| `lem:DR-verdier-compat` | `lemma` | `ProvedHere` | 5105 | 0 | 1 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | `ProvedHere` | 5144 | 1 | 0 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | `ProvedHere` | 5173 | 0 | 1 | Geometric bar as factorization chains |
| `lem:diagram-commutes-AF` | `lemma` | `ProvedHere` | 5229 | 4 | 0 | Diagram commutes |
| `lem:extension-across-boundary-qi` | `lemma` | `ProvedHere` | 5336 | 0 | 0 | Extension across boundary |
| `lem:e2-collapse-higher-genus` | `lemma` | `ProvedHere` | 5470 | 1 | 0 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | `ProvedHere` | 5548 | 0 | 1 | Pants decomposition as excision |
| `thm:ambient-complementarity-tangent` | `theorem` | `ProvedHere` | 5916 | 0 | 0 | Ambient complementarity in tangent form |
| `prop:legendre-duality-potentials` | `proposition` | `ProvedHere` | 6452 | 0 | 0 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | `ProvedHere` | 6467 | 0 | 0 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | `ProvedHere` | 6497 | 0 | 0 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | `ProvedHere` | 6521 | 0 | 0 | Criterion for fake complementarity |
| `thm:holo-comp-fourier-transport` | `theorem` | `ProvedHere` | 6913 | 0 | 0 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | `ProvedHere` | 6957 | 0 | 0 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | `ProvedHere` | 7034 | 4 | 0 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | `ProvedHere` | 7118 | 2 | 0 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | `ProvedHere` | 7187 | 1 | 0 | First nonlinear determinant anomaly |

#### `chapters/theory/higher_genus_foundations.tex` (50)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | `ProvedHere` | 1121 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | `ProvedHere` | 1222 | 0 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | `ProvedHere` | 1317 | 0 | 0 | Pentagon identity |
| `thm:higher-associahedron-m5` | `theorem` | `ProvedElsewhere` | 1355 | 0 | 1 | Higher associahedron identity for \texorpdfstring{$m_5$}{m5} {\cite{Sta63}} |
| `thm:catalan-parenthesization` | `theorem` | `ProvedElsewhere` | 1367 | 0 | 1 | Catalan identity at higher levels {\cite{Sta97}} |
| `thm:verdier-NAP` | `theorem` | `ProvedElsewhere` | 1399 | 1 | 2 | Verdier duality = NAP duality {\cite{AF15,KS90}} |
| `thm:cobar-ainfty-complete` | `theorem` | `ProvedHere` | 1489 | 2 | 1 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | `ProvedHere` | 1601 | 6 | 1 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | `ProvedHere` | 1748 | 0 | 0 | Verdier duality of operations |
| `thm:geometric-com-lie-enhancement` | `theorem` | `ProvedElsewhere` | 1835 | 0 | 1 | Geometric enhancement of Com-Lie |
| `thm:ainfty-com-lie-interchange` | `theorem` | `ProvedElsewhere` | 1873 | 0 | 1 | Maximal vs.\ trivial \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:cobar-resolution-scoped` | `theorem` | `ProvedElsewhere` | 2120 | 2 | 1 | Cobar resolution on the Koszul locus {\cite{LV12}} |
| `thm:genus-graded-mc` | `theorem` | `ProvedElsewhere` | 2180 | 2 | 2 | Maurer--Cartan = deformations {\cite{Kon03,Ger63}} |
| `prop:yangian-from-deformation` | `proposition` | `ProvedElsewhere` | 2208 | 0 | 1 | Yangian from deformation {\cite{Drinfeld85}} |
| `prop:deforming-heisenberg` | `proposition` | `ProvedHere` | 2235 | 1 | 0 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | `ProvedHere` | 2269 | 0 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | `ProvedHere` | 2303 | 0 | 0 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | `ProvedHere` | 2323 | 1 | 0 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | `ProvedHere` | 2339 | 1 | 0 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:moduli-structure` | `theorem` | `ProvedElsewhere` | 2958 | 0 | 2 | Structure of \texorpdfstring{$\overline{\mathcal{M}}_{g,n}$}{M-bar(g,n)} {\cite{DeligneM69,Knudsen83}} |
| `thm:universal-curve-fibration` | `theorem` | `ProvedElsewhere` | 2980 | 0 | 1 | Universal curve fibration {\cite{Knudsen83}} |
| `thm:period-matrix-properties` | `theorem` | `ProvedElsewhere` | 3894 | 0 | 1 | Properties of the period matrix {\cite{Fay73}} |
| `thm:theta-properties` | `theorem` | `ProvedElsewhere` | 3938 | 0 | 1 | Theta function properties {\cite{Fay73}} |
| `thm:prime-form-properties` | `theorem` | `ProvedElsewhere` | 3975 | 0 | 1 | Prime form properties {\cite{Fay73}} |
| `thm:modular-vs-quasi` | `theorem` | `ProvedElsewhere` | 4393 | 0 | 1 | Modular vs quasi-modular {\cite{KP84}} |
| `thm:theta-zero` | `theorem` | `ProvedElsewhere` | 4451 | 0 | 1 | Theta zero values {\cite{Fay73}} |
| `thm:eta-properties-genus1` | `theorem` | `ProvedHere` | 4487 | 1 | 0 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:odd-even-g2` | `theorem` | `ProvedElsewhere` | 5148 | 0 | 1 | Odd vs even characteristics {\cite{Fay73}} |
| `thm:theta-g3` | `theorem` | `ProvedElsewhere` | 5282 | 0 | 1 | Theta characteristics at genus 3 {\cite{Fay73}} |
| `thm:mmm-classes` | `theorem` | `ProvedElsewhere` | 5498 | 0 | 2 | Tautological Hodge and boundary classes {\cite{Mumford83}} |
| `__unlabeled_chapters/theory/higher_genus_foundations.tex:5524` | `remark` | `ProvedElsewhere` | 5524 | 0 | 1 | Tautological scope |
| `thm:mumford-formula` | `theorem` | `ProvedElsewhere` | 5551 | 0 | 1 | Faber--Pandharipande $\lambda_g$ formula {\cite{FP03}} |
| `thm:obstruction-general` | `theorem` | `ProvedHere` | 5760 | 0 | 0 | Maurer--Cartan obstruction |
| `thm:obstruction-nilpotent` | `theorem` | `ProvedElsewhere` | 5965 | 1 | 0 | Square of the Hodge shadow |
| `cor:mumford-multiplicative` | `corollary` | `ProvedElsewhere` | 6012 | 0 | 0 | Exterior-power form of the Mumford relation |
| `prop:lambda-g-clutching` | `proposition` | `ProvedElsewhere` | 6195 | 1 | 0 | Clutching formulas for the Hodge Euler class |
| `prop:f2-quartic-dependence` | `proposition` | `ProvedHere` | 6661 | 1 | 0 | Genus-$2$ quartic dependence |
| `cor:kappa-periodicity` | `corollary` | `ProvedHere` | 6736 | 0 | 0 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `prop:bar-tautological-filtration` | `proposition` | `ProvedHere` | 7016 | 4 | 1 | Bar spectral sequence and tautological filtration |
| `thm:obs-def-pairing-explicit` | `theorem` | `ProvedElsewhere` | 7125 | 1 | 0 | Poincar\'e pairing for the Hodge shadow |
| `lem:stable-graph-d-squared` | `lemma` | `ProvedHere` | 7477 | 0 | 0 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | `ProvedHere` | 7539 | 2 | 0 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | `ProvedHere` | 7577 | 1 | 0 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | `ProvedHere` | 7619 | 0 | 0 | Extremal pages |
| `thm:loop-order-collapse` | `theorem` | `ProvedHere` | 7848 | 3 | 0 | Loop-order convergence and finite-depth collapse bound |
| `cor:loop-decomposition-bar` | `corollary` | `ProvedHere` | 7894 | 1 | 0 | Associated graded by loop order |
| `thm:feynman-involution` | `theorem` | `ProvedElsewhere` | 7931 | 0 | 1 | Feynman involution \textup{\cite[Theorem~5.2 |
| `thm:virtual-euler-char` | `theorem` | `ProvedHere` | 8009 | 1 | 0 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | `ProvedHere` | 8037 | 0 | 2 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | `ProvedHere` | 8087 | 0 | 0 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (134)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:genus-window-ml-passage` | `lemma` | `ProvedHere` | 370 | 0 | 0 | Finite-window Mittag--Leffler passage |
| `thm:pbw-allgenera-principal-w` | `theorem` | `ProvedHere` | 996 | 7 | 0 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `lem:pbw-weightwise-g-module` | `lemma` | `ProvedHere` | 1138 | 0 | 0 | Weightwise reduction of the genus enrichment to \texorpdfstring{$\fg$}{g}-modules |
| `lem:pbw-mixed-factorization` | `lemma` | `ProvedHere` | 1197 | 1 | 0 | Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)} |
| `thm:pbw-genus1-km` | `theorem` | `ProvedHere` | 1245 | 7 | 1 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `thm:pbw-allgenera-km` | `theorem` | `ProvedHere` | 1587 | 8 | 0 | PBW degeneration at all genera for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | `ProvedHere` | 1858 | 7 | 0 | PBW degeneration at all genera for Virasoro |
| `thm:pbw-universal-semisimple` | `theorem` | `ProvedHere` | 2093 | 3 | 0 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `prop:hook-pbw` | `proposition` | `ProvedHere` | 2254 | 1 | 0 | Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses |
| `thm:pbw-propagation` | `theorem` | `ProvedHere` | 2346 | 3 | 0 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | `ProvedHere` | 2503 | 0 | 0 | Locality of the collision differential |
| `lem:e2-higher-genus` | `lemma` | `ProvedHere` | 2913 | 0 | 0 | $E_2$ collapse at higher genus |
| `comp:heisenberg-g2-fp-grr-check` | `computation` | `ProvedHere` | 4090 | 1 | 2 | Genus-$2$ Heisenberg FP--GRR check |
| `prop:genus-completed-mc-framework` | `proposition` | `ProvedHere` | 6421 | 0 | 0 | Genus-completed MC algebra |
| `prop:cyclic-ce-identification` | `proposition` | `ProvedHere` | 6500 | 0 | 0 | Cyclic CE cohomology identification |
| `thm:convolution-dg-lie-structure` | `theorem` | `ProvedHere` | 11448 | 0 | 1 | dg~Lie structure from the modular operad |
| `thm:operadic-homotopy-convolution-modular` | `theorem` | `ProvedElsewhere` | 12176 | 1 | 3 | Operadic homotopy convolution {\cite[Theorem~4.1 |
| `cor:deformation-functoriality` | `corollary` | `ProvedElsewhere` | 12505 | 0 | 1 | Functoriality of the modular deformation functor {\cite[Theorem~5.1 |
| `lem:rational-orbifold-chains-stabilizer-pushforward` | `lemma` | `ProvedHere` | 12738 | 0 | 0 | Rational orbifold chains, stabilisers, and pushforward |
| `lem:local-log-boundary-coordinates-gysin-residue` | `lemma` | `ProvedHere` | 12785 | 0 | 0 | Local log-boundary coordinates and the Gysin residue |
| `lem:first-local-log-residue-computations` | `lemma` | `ProvedHere` | 12848 | 1 | 0 | First local logarithmic residue computations |
| `lem:local-snc-residue-signs` | `lemma` | `ProvedHere` | 12928 | 0 | 0 | Local SNC residue signs and nested Gysin functoriality |
| `lem:proper-pushforward-orientation-twists` | `lemma` | `ProvedHere` | 12989 | 0 | 0 | Proper pushforward and orientation twists |
| `lem:local-nested-log-cocomposition` | `lemma` | `ProvedHere` | 13110 | 2 | 0 | Local nested logarithmic cocomposition |
| `lem:local-two-edge-logfm-sign-cancellation` | `lemma` | `ProvedHere` | 13195 | 3 | 0 | Two-edge determinant sign and codimension-two cancellation |
| `lem:local-snc-excess-intersection-vanishes` | `lemma` | `ProvedHere` | 13255 | 1 | 0 | Local SNC excess-intersection term vanishes |
| `lem:finite-groupoid-reynolds-normalisation` | `lemma` | `ProvedHere` | 13386 | 0 | 0 | Finite groupoid/Reynolds normalisation |
| `lem:completed-reynolds-descent-ordered-arity` | `lemma` | `ProvedHere` | 13454 | 1 | 0 | Completed Reynolds descent in each ordered arity |
| `lem:R-twisted-completed-coinvariants` | `lemma` | `ProvedHere` | 13534 | 0 | 0 | $R$-twisted completed coinvariants |
| `prop:av-kernel-rmatrix-associator-strata` | `proposition` | `ProvedHere` | 13623 | 2 | 0 | Averaging-kernel strata for $r$-matrix and associator data |
| `lem:mok-crossing-count-base-change` | `lemma` | `ProvedHere` | 14597 | 0 | 0 | Mok crossing count is stable under logarithmic base change |
| `lem:refined-mok-codimension-bookkeeping` | `lemma` | `ProvedHere` | 14740 | 0 | 0 | Refined Mok codimension bookkeeping |
| `lem:log-filtered-completion-associated-graded-cobar` | `lemma` | `ProvedHere` | 14793 | 0 | 0 | Filtered completion and associated graded log cobar |
| `prop:first-logfm-coherence-obstructions` | `proposition` | `ProvedHere` | 15690 | 4 | 0 | First log-FM coherence obstructions |
| `thm:logfm-obstruction-criterion` | `theorem` | `ProvedHere` | 15760 | 2 | 0 | Obstruction criterion for the signed log-FM package |
| `thm:empty-boundary-logfm-obstructions-vanish` | `theorem` | `ProvedHere` | 15824 | 3 | 0 | Empty-boundary FM obstruction vanishing |
| `const:vol1-genus-two-shells` | `construction` | `ProvedHere` | 16055 | 0 | 0 | Genus-two shell decomposition |
| `const:vol1-genus-spectral-sequence` | `construction` | `ProvedHere` | 16125 | 3 | 0 | Genus spectral sequence |
| `def:shadow-algebra` | `definition` | `ProvedHere` | 16584 | 1 | 0 | Shadow algebra |
| `lem:shadow-bracket-well-defined` | `lemma` | `ProvedHere` | 16656 | 0 | 0 | Well-definedness of the descended bracket |
| `thm:ds-complementarity-tower-main` | `theorem` | `ProvedHere` | 16898 | 1 | 0 | DS shadow-reflection tower |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | `ProvedHere` | 17766 | 1 | 0 | Stable-graph pronilpotent completion |
| `cor:metaplectic-square-root` | `corollary` | `ProvedHere` | 18267 | 1 | 0 | Determinantal half-density |
| `lem:graph-sum-truncation` | `lemma` | `ProvedHere` | 19597 | 3 | 0 | Graph-sum truncation criterion |
| `prop:shadow-coefficient-rationality` | `proposition` | `ProvedHere` | 20851 | 0 | 0 | Shadow coefficient rationality |
| `def:shadow-depth-classification` | `definition` | `ProvedHere` | 20952 | 2 | 0 | Shadow depth classification |
| `cor:shadow-depth-koszul-invariance` | `corollary` | `ProvedHere` | 21522 | 0 | 0 | Shadow depth under Koszul duality |
| `cor:gaussian-decomposition` | `corollary` | `ProvedHere` | 22015 | 0 | 0 | Gaussian decomposition |
| `lem:depth-three-impossible` | `lemma` | `ProvedHere` | 22068 | 1 | 0 | Impossibility of $d_{\mathrm{alg}} = 3$ |
| `prop:no-finite-depth-beyond-contact` | `proposition` | `ProvedHere` | 22152 | 4 | 0 | No finite multi-channel depth beyond contact |
| `prop:hankel-extraction` | `proposition` | `ProvedHere` | 22442 | 1 | 0 | Hankel extraction of the quartic contact invariant |
| `cor:signed-shadow-measure` | `corollary` | `ProvedHere` | 22595 | 1 | 0 | Universal signed measure |
| `thm:shadow-epstein-zeta` | `theorem` | `ProvedHere` | 22677 | 2 | 2 | The Epstein zeta function of the shadow metric |
| `prop:t-line-autonomy` | `proposition` | `ProvedHere` | 24151 | 1 | 0 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | `ProvedHere` | 24209 | 1 | 0 | Inter-channel coupling on sublines |
| `cor:virasoro-shadow-radius` | `corollary` | `ProvedHere` | 24575 | 2 | 0 | Virasoro shadow growth rate |
| `prop:critical-cubic-convergence` | `proposition` | `ProvedHere` | 25052 | 3 | 0 | Critical cubic convergence threshold |
| `prop:virasoro-bottleneck` | `proposition` | `ProvedHere` | 25141 | 0 | 0 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | `ProvedHere` | 25370 | 1 | 0 | Koszul exchange of shadow regimes |
| `prop:koszul-conductor-wn` | `proposition` | `ProvedHere` | 25447 | 1 | 0 | Koszul conductor of \texorpdfstring{$\cW_N$}{WN} |
| `prop:propagator-universality` | `proposition` | `ProvedHere` | 25603 | 2 | 0 | Propagator universality |
| `cor:analytic-shadow-realization` | `corollary` | `ProvedHere` | 26589 | 2 | 0 | Analytic shadow realization |
| `constr:tautological-evaluation-map` | `construction` | `ProvedHere` | 26628 | 0 | 0 | Tautological evaluation map |
| `lem:cross-channel-graph-support` | `lemma` | `ProvedHere` | 27487 | 1 | 0 | Support of the cross-channel graph sum |
| `rem:delta-f2-graph-decomposition` | `remark` | `ProvedHere` | 28193 | 1 | 0 | $\delta F_2$ graph-stratum decomposition |
| `comp:w3-genus3-cross` | `computation` | `ProvedHere` | 28249 | 2 | 0 | $\cW_3$ genus-$3$ cross-channel |
| `comp:w3-genus4-cross` | `computation` | `ProvedHere` | 28324 | 0 | 0 | $\cW_3$ genus-$4$ cross-channel |
| `comp:w4-full-ope-cross` | `computation` | `ProvedHere` | 28423 | 4 | 1 | $\cW_4$ full-OPE cross-channel correction |
| `rem:w4-irrational-cross-channel` | `remark` | `ProvedHere` | 28568 | 4 | 1 | $\cW_4$: the first irrational cross-channel correction |
| `comp:w5-full-ope-cross` | `computation` | `ProvedHere` | 28600 | 5 | 0 | $\cW_5$ full-OPE cross-channel correction |
| `prop:universal-gravitational-cross-channel` | `proposition` | `ProvedHere` | 28837 | 1 | 0 | Universal gravitational cross-channel formula for~$\cW_N$ |
| `rem:large-n-delta-f2-planar` | `remark` | `ProvedHere` | 29104 | 1 | 0 | Large-$N$ and 't~Hooft limit of $\delta F_2$ |
| `prop:cross-channel-growth` | `proposition` | `ProvedHere` | 29226 | 0 | 0 | Cross-channel growth |
| `prop:self-loop-vanishing` | `proposition` | `ProvedHere` | 30151 | 0 | 0 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | `ProvedHere` | 30187 | 1 | 0 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | `ProvedHere` | 30368 | 1 | 0 | Genus-$1$ two-point function from MC |
| `prop:dressed-propagator-resolution` | `proposition` | `ProvedHere` | 30739 | 1 | 0 | Dressed propagator coefficient and symmetry |
| `thm:pixton-mc-genus2` | `theorem` | `ProvedHere` | 31296 | 2 | 0 | Pixton--MC bridge at genus~$2$ |
| `thm:pixton-mc-genus3` | `theorem` | `ProvedHere` | 31361 | 2 | 0 | Pixton--MC bridge at genus~$3$ |
| `prop:mumford-from-mc-explicit` | `proposition` | `ProvedHere` | 31438 | 1 | 0 | Mumford formula from MC |
| `calc:fp-numbers` | `calculation` | `ProvedHere` | 31467 | 0 | 0 | Faber--Pandharipande numbers through genus~$6$ |
| `thm:genus4-stable-graph-census` | `theorem` | `ProvedHere` | 31591 | 0 | 0 | Genus-$4$ stable graph census |
| `thm:genus4-free-energy` | `theorem` | `ProvedHere` | 31620 | 1 | 0 | Genus-$4$ formal genus coefficient |
| `prop:genus4-spectral-sequence` | `proposition` | `ProvedHere` | 31642 | 0 | 0 | Genus-$4$ spectral sequence |
| `thm:bar-macmahon` | `theorem` | `ProvedHere` | 31691 | 0 | 0 | Bar--MacMahon correspondence |
| `prop:conifold-dt-gv` | `proposition` | `ProvedHere` | 31718 | 0 | 0 | Conifold DT and GV |
| `prop:tropical-shadow-amplitudes` | `proposition` | `ProvedHere` | 31775 | 0 | 0 | Tropical shadow amplitudes |
| `prop:tropical-period-theta` | `proposition` | `ProvedHere` | 31799 | 0 | 0 | Tropical theta function |
| `prop:fp-genus-decay-for-double` | `proposition` | `ProvedHere` | 31860 | 1 | 0 | Faber--Pandharipande genus decay |
| `prop:shadow-schwarzian` | `proposition` | `ProvedHere` | 32824 | 2 | 0 | Spectral Schr\"odinger potential |
| `cor:shadow-schrodinger-singularities` | `corollary` | `ProvedHere` | 32870 | 1 | 0 | Singularity classification |
| `prop:shadow-voros-classical` | `proposition` | `ProvedHere` | 33012 | 0 | 0 | Classical Voros period |
| `def:v1-cyclically-admissible` | `definition` | `ProvedHere` | 33273 | 1 | 1 | Cyclically admissible Lie conformal algebra |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | `ProvedHere` | 33309 | 2 | 0 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:hgmk-finite-jet-rigidity` | `proposition` | `ProvedHere` | 33390 | 1 | 0 | Finite-jet rigidity |
| `prop:hgmk-polynomial-level-dependence` | `proposition` | `ProvedHere` | 33413 | 1 | 0 | Polynomial level dependence |
| `thm:cubic-gauge-triviality` | `theorem` | `ProvedHere` | 33566 | 1 | 0 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | `ProvedHere` | 33674 | 1 | 0 | Independent sum factorization |
| `prop:symn-kappa-linearity` | `proposition` | `ProvedHere` | 33732 | 2 | 2 | Symmetric orbifold kappa linearity |
| `rem:symmetric-orbifold-kappa` | `remark` | `ProvedHere` | 33812 | 1 | 1 | Symmetric orbifold kappa: four independent derivations |
| `prop:genus0-curve-independence` | `proposition` | `ProvedHere` | 34509 | 1 | 0 | Genus-$0$ curve-independence |
| `def:stable-graph-coefficient-algebra` | `definition` | `ProvedHere` | 36217 | 0 | 0 | Oriented stable-graph coefficient algebra |
| `lem:stable-graph-coefficient-d-square-zero` | `lemma` | `ProvedHere` | 36254 | 2 | 0 | Stable-graph coefficient differential squares to zero |
| `def:logarithmic-fulton-macpherson-compactification` | `definition` | `ProvedElsewhere` | 36294 | 1 | 0 | Logarithmic Fulton--MacPherson compactification |
| `lem:mok-face-differential-square-zero` | `lemma` | `ProvedHere` | 36405 | 1 | 0 | Mok face differential squares to zero |
| `lem:planted-forest-dpf-square-zero` | `lemma` | `ProvedHere` | 36492 | 1 | 0 | Planted-forest differential squares to zero |
| `lem:planted-forest-first-codim-two-sign` | `lemma` | `ProvedHere` | 36545 | 1 | 0 | First planted-forest codimension-two sign check |
| `lem:logfm-first-low-boundary-computations` | `lemma` | `ProvedHere` | 36590 | 4 | 0 | First five low-boundary computations in the log-FM face complex |
| `def:logfm-tropicalization` | `definition` | `ProvedElsewhere` | 36719 | 1 | 1 | Tropicalisation of a logarithmic FM space |
| `lem:mok-planted-forest-boundary-dictionary` | `lemma` | `ProvedElsewhere` | 36760 | 0 | 2 | Mok boundary dictionary for planted forests |
| `lem:relative-universal-family-logfm-boundary-dictionary` | `lemma` | `ProvedElsewhere` | 36809 | 1 | 3 | Relative universal-family log-FM boundary dictionary |
| `prop:logfm-reduces-ordinary-fm` | `proposition` | `ProvedElsewhere` | 36880 | 1 | 2 | Ordinary FM as the \texorpdfstring{$D=\emptyset$}{D=empty} case |
| `def:planar-planted-forest-coefficient-algebra` | `definition` | `ProvedHere` | 37111 | 1 | 0 | Planar planted-forest coefficient algebra |
| `def:ordered-ambient-algebra` | `definition` | `ProvedHere` | 37301 | 2 | 0 | Ordered ambient algebra |
| `thm:convolution-d-squared-zero` | `theorem` | `ProvedHere` | 37367 | 2 | 0 | Square-zero: convolution level |
| `prop:2d-convergence` | `proposition` | `ProvedHere` | 38345 | 0 | 2 | Two-dimensional convergence |
| `thm:verlinde-polynomial-family` | `theorem` | `ProvedHere` | 38987 | 2 | 0 | Verlinde polynomial family |
| `prop:g2-degree0` | `proposition` | `ProvedHere` | 39348 | 0 | 0 | Degree-$0$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree1` | `proposition` | `ProvedHere` | 39403 | 1 | 0 | Degree-$1$ ordered chiral homology on $\Sigma_2$ |
| `thm:fay-trisecant-identity-kzb` | `theorem` | `ProvedElsewhere` | 39692 | 0 | 1 | Fay trisecant identity |
| `prop:g2-degree2` | `proposition` | `ProvedHere` | 39774 | 0 | 0 | Degree-$2$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-conformal-block-degree` | `proposition` | `ProvedHere` | 39873 | 2 | 0 | Genus-$2$ conformal block decomposition by degree |
| `prop:genus-g-euler-general` | `proposition` | `ProvedHere` | 39934 | 2 | 0 | Euler characteristic of degree-$2$ KZB local systems: general rank and genus |
| `prop:g2-euler-n` | `proposition` | `ProvedHere` | 40028 | 2 | 0 | Euler characteristic at low degrees, genus~$2$ |
| `prop:g2-nonsep-degen` | `proposition` | `ProvedHere` | 40246 | 1 | 0 | Non-separating degeneration: $\Sigma_2 \to E_\tau$ |
| `prop:g2-sep-degen` | `proposition` | `ProvedHere` | 40360 | 1 | 1 | Separating degeneration: $\Sigma_2 \to E_\tau \cup E_{\tau'}$ |
| `cons:lifted-spectral-package` | `construction` | `ProvedHere` | 40713 | 0 | 0 | Lifted spectral cover package |
| `thm:determinantal-branch-formula` | `theorem` | `ProvedHere` | 40740 | 0 | 0 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | `ProvedHere` | 40776 | 0 | 0 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | `ProvedHere` | 40807 | 0 | 0 | Common-sheet multiplication law |
| `rem:visible-discriminant-misses` | `remark` | `ProvedHere` | 40824 | 0 | 0 | What the visible discriminant misses |
| `thm:spectral-hierarchy` | `theorem` | `ProvedHere` | 40872 | 3 | 0 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | `ProvedHere` | 40908 | 0 | 0 | First cubic obstruction |
| `cor:hgmk-abar5-twentyeight-stratum` | `corollary` | `ProvedHere` | 42404 | 0 | 1 | Genus-$5$ octachotomy analogue: the twenty-eight-stratum ambient tower on $\AbarFive$ |

#### `chapters/theory/higher_kummer_arithmetic_duality_platonic.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:higher-kummer-z-g-presence` | `theorem` | `ProvedHere` | 36 | 2 | 0 | Kummer-irregular primes in the Bernoulli window |

#### `chapters/theory/hochschild_cohomology.tex` (27)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:hochschild-classical-comparison` | `theorem` | `ProvedElsewhere` | 186 | 0 | 1 | Comparison with classical theory {\cite{BD04}} |
| `thm:bar-spectral-sequence-hochschild` | `theorem` | `ProvedElsewhere` | 479 | 0 | 2 | Bar spectral sequence {\cite{BD04,CG17}} |
| `thm:hochschild-chain-complex` | `theorem` | `ProvedHere` | 622 | 0 | 1 | Chiral Hochschild chain model is a chain complex |
| `lem:cyclic-commutes` | `lemma` | `ProvedHere` | 705 | 0 | 0 | Cyclic operator commutes with the chiral Hochschild differential |
| `thm:connes-exact-sequence` | `theorem` | `ProvedElsewhere` | 737 | 0 | 2 | Connes mixed-complex structure {\cite{Connes85,Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:753` | `remark` | `ProvedElsewhere` | 753 | 0 | 2 | Provenance and citation |
| `cor:connes-SBI` | `corollary` | `ProvedElsewhere` | 760 | 1 | 2 | Connes SBI exact sequence {\cite{Connes85,Loday98}} |
| `thm:HC-spectral-sequence` | `theorem` | `ProvedElsewhere` | 771 | 1 | 2 | Chiral Hochschild-cyclic spectral sequence {\cite{Connes85,Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:795` | `remark` | `ProvedElsewhere` | 795 | 0 | 2 | Provenance and citation |
| `thm:E2-page-formula` | `theorem` | `ProvedElsewhere` | 808 | 0 | 1 | Second-page formula {\cite{Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:830` | `remark` | `ProvedElsewhere` | 830 | 0 | 1 | Provenance and citation |
| `comp:morita-free-generator` | `computation` | `ProvedHere` | 1171 | 0 | 0 | The free rank-one generator |
| `prop:morita-equivalence-compact-gen` | `theorem` | `ProvedHere` | 1191 | 0 | 3 | Derived Morita reconstruction from one generator |
| `prop:endofunctor-bimodule` | `proposition` | `ProvedElsewhere` | 1303 | 0 | 2 | Endofunctor--bimodule equivalence {\cite{Toen07,BZFN10}} |
| `cor:identity-diagonal` | `corollary` | `ProvedHere` | 1347 | 1 | 0 | Identity functor $=$ diagonal bimodule |
| `thm:derived-center-hochschild` | `theorem` | `ProvedHere` | 1366 | 3 | 0 | Derived center $=$ categorical Hochschild cohomology $=$ algebraic Hochschild cochains via a thick generator |
| `cor:continuous-center-compact-generator` | `corollary` | `ProvedHere` | 1435 | 2 | 0 | Continuous center from a compact generator |
| `thm:morita-invariance-HH` | `theorem` | `ProvedHere` | 1478 | 2 | 0 | Morita invariance of algebraic Hochschild cohomology |
| `prop:explicit-morita-transfer` | `proposition` | `ProvedHere` | 1514 | 2 | 0 | Bimodule realization of Morita transfer |
| `thm:excision` | `theorem` | `ProvedElsewhere` | 1680 | 0 | 1 | Excision; {\cite[Theorem~3.18 |
| `thm:circle-fh-hochschild` | `theorem` | `ProvedHere` | 1698 | 1 | 0 | Factorization homology on $S^1$ $=$ algebraic Hochschild chains |
| `prop:monodromy-standard` | `proposition` | `ProvedHere` | 1859 | 0 | 0 | Monodromy for standard families |
| `lem:chi3-ordered-collision-algebra` | `lemma` | `ProvedElsewhere` | 2143 | 1 | 1 | The ordered three-point collision algebra {\cite{Arnold69}} |
| `thm:chi3-mukai-hochschild-pairing` | `theorem` | `ProvedHere` | 4011 | 2 | 0 | The Mukai pairing criterion for the three-point class |
| `cor:chi3-mukai-nondegeneracy` | `corollary` | `ProvedHere` | 4050 | 0 | 0 | Perfectness on the three-point and degree-zero lines |
| `thm:chirhoch3-seven-path-comparison` | `theorem` | `ProvedHere` | 4097 | 1 | 0 | Comparison of realizations by chain homotopy |
| `cor:chirhoch3-seven-fold-confirmation` | `corollary` | `ProvedHere` | 4160 | 3 | 0 | Nonvanishing transported by the comparison maps |

#### `chapters/theory/infinite_fingerprint_classification.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `cor:quadrichotomy-depth-shift` | `corollary` | `ProvedHere` | 624 | 0 | 0 | Quadrichotomy as depth shift |
| `thm:quadrichotomy-is-coarse-projection` | `theorem` | `ProvedHere` | 636 | 1 | 0 | Quadrichotomy is a coarse projection; strengthening of Proposition~\ref{prop:coarse-projection-functor} |
| `thm:DS-fingerprint-transport` | `theorem` | `ProvedHere` | 767 | 1 | 7 | DS transport of the fingerprint; closes FM\textup{108} |
| `calc:fingerprint-stratum-separation` | `calculation` | `ProvedHere` | 921 | 0 | 0 | Fingerprint witness-row separation |
| `cor:fingerprint-separates-landscape` | `corollary` | `ProvedHere` | 949 | 2 | 0 | Witness-row separation on the standard landscape |
| `thm:schellekens-structured-subset` | `theorem` | `ProvedHere` | 981 | 1 | 0 | Structured-subset derivation of the holomorphic \texorpdfstring{$c=24$}{c=24} census; closes AP\textup{290} |

#### `chapters/theory/introduction.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:intro-core-ordered-bar-type-correct` | `lemma` | `ProvedHere` | 197 | 1 | 0 | Type correctness of the core ordered-bar datum |
| `thm:central-charge-complementarity` | `theorem` | `ProvedHere` | 1754 | 1 | 1 | Central charge complementarity |
| `prop:intro-scalar-packages-not-formal` | `proposition` | `ProvedHere` | 3855 | 0 | 0 | Three scalar functors and their comparison maps |

#### `chapters/theory/kappa_conductor.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:platonic-conductor` | `theorem` | `ProvedHere` | 283 | 1 | 0 | Finite $bc$-spin sum |
| `cor:K-BP` | `corollary` | `ProvedHere` | 407 | 0 | 0 | Bershadsky--Polyakov |

#### `chapters/theory/koszul_pair_structure.tex` (22)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | `ProvedHere` | 369 | 0 | 0 | Well-definedness of the chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | `ProvedHere` | 419 | 1 | 0 | Relative exactness of the two-sided chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | `ProvedHere` | 503 | 1 | 0 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | `ProvedHere` | 562 | 1 | 0 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | `ProvedHere` | 656 | 1 | 0 | Properties of cup product |
| `thm:chiral-gerstenhaber-kps` | `theorem` | `ProvedElsewhere` | 703 | 0 | 3 | Chiral Gerstenhaber algebra {\cite{Ger63, Tamarkin00}} |
| `thm:ainfty-chiral-hochschild` | `theorem` | `ProvedHere` | 737 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} operations from the chiral brace model |
| `thm:linfty-chiral-hochschild` | `theorem` | `ProvedElsewhere` | 787 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} structure {\cite{LV12}} |
| `prop:admissible-levels-permuted` | `proposition` | `ProvedHere` | 1158 | 0 | 1 | Numerical admissible data under the level reflection |
| `thm:mc-quadratic` | `theorem` | `ProvedHere` | 1256 | 0 | 0 | Maurer--Cartan correspondence, quadratic case |
| `thm:chiral-yangian-km` | `theorem` | `ProvedHere` | 1348 | 0 | 0 | Affine Kac--Moody as chiral algebra |
| `thm:chiral-yangian` | `theorem` | `ProvedElsewhere` | 1372 | 0 | 2 | Critical centre and Yangian deformation data {\cite{Drinfeld85,Feigin-Frenkel}} |
| `thm:feigin-frenkel-bar` | `theorem` | `ProvedElsewhere` | 1505 | 0 | 1 | Feigin--Frenkel centre {\cite{FF}} |
| `thm:w-algebra-sl4` | `theorem` | `ProvedElsewhere` | 1581 | 0 | 1 | Structure of \texorpdfstring{$\mathcal{W}(\mathfrak{sl}_4, e_{subreg})$}{W(sl4, e\_subreg)} {\cite{KRW}} |
| `thm:ff-s-duality` | `theorem` | `ProvedElsewhere` | 1589 | 0 | 1 | Feigin--Frenkel duality as S-duality, principal simply-laced case |
| `thm:koszul-equivalence-categories` | `theorem` | `ProvedElsewhere` | 1650 | 0 | 1 | Koszul equivalence of categories {\cite{BGS96}} |
| `thm:linf-mc-flatness` | `theorem` | `ProvedHere` | 1918 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan equation from a transferred \texorpdfstring{$A_\infty$}{A-infinity} model |
| `thm:ordered-shuffle` | `theorem` | `ProvedHere` | 2344 | 1 | 0 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | `ProvedHere` | 2386 | 0 | 0 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | `ProvedHere` | 2416 | 2 | 0 | Enveloping duality |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | `ProvedHere` | 2570 | 1 | 0 | chiral Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-FG-shadow` | `theorem` | `ProvedElsewhere` | 2774 | 0 | 1 | Commutator-shadow theorem |

#### `chapters/theory/koszulness_moduli_scheme.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `v1-cor:kms-exceptional-PBW` | `corollary` | `ProvedElsewhere` | 1124 | 0 | 1 | Exceptional-type Yangian PBW input via GRW18 |

#### `chapters/theory/mc3_five_family_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:mc3-finite-window-upgrade-boundary` | `proposition` | `ProvedElsewhere` | 113 | 4 | 0 | Finite-window upgrade boundary |
| `thm:mc3-evaluation-core-five-family` | `theorem` | `ProvedHere` | 222 | 1 | 0 | MC3 on the evaluation-generated core, five-family mechanism |
| `prop:mc3-type-A-asymptotic-prefundamentals-platonic` | `proposition` | `ProvedHere` | 366 | 0 | 0 | Asymptotic prefundamentals: rational type~$A$ |
| `prop:mc3-type-BCD-reflection-shapovalov-platonic` | `proposition` | `ProvedHere` | 417 | 0 | 0 | Reflection-equation Shapovalov: twisted B/C/D |
| `prop:mc3-uniform-chari-moura-platonic` | `proposition` | `ProvedHere` | 463 | 0 | 0 | Chari--Moura multiplicity-free $\ell$-weights: classical and simply-laced exceptional types |
| `prop:mc3-uniform-chari-moura-nonsimplylaced-platonic` | `proposition` | `ProvedElsewhere` | 493 | 0 | 0 | Multiplicity-free $\ell$-weights: non-simply-laced exceptional types $G_2, F_4$ |
| `prop:mc3-elliptic-theta-divisor-platonic` | `proposition` | `ProvedHere` | 561 | 0 | 0 | Elliptic Bethe / DYBE: theta-divisor complement |
| `prop:mc3-super-parity-balance-platonic` | `proposition` | `ProvedHere` | 596 | 1 | 0 | Super-Yangian parity-balance: $Y_\hbar(\mathfrak{gl}_{m\|n})$ |
| `prop:baxter-retraction-type-A-artifact` | `proposition` | `ProvedHere` | 727 | 6 | 0 | Baxter hyperplane as a type-$A$ rational artifact |

#### `chapters/theory/mc5_class_m_chain_level_platonic.tex` (10)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:mc5-class-m-chain-level-pro-ambient` | `theorem` | `ProvedHere` | 218 | 3 | 1 | MC5 class $\mathsf{M}$ pro-ambient comparison on a strict Mittag--Leffler tower |
| `cor:mc5-class-m-chain-level-on-inverse-limit` | `corollary` | `ProvedHere` | 432 | 2 | 0 | Chain-level MC5 class $\mathsf{M}$ on the inverse limit |
| `thm:mc5-class-m-topological-chain-level-j-adic` | `theorem` | `ProvedHere` | 542 | 4 | 0 | MC5 class $\mathsf{M}$ in the $J$-adic topological ambient |
| `prop:ambient-equivalence` | `proposition` | `ProvedHere` | 610 | 5 | 0 | Ambient comparison for chain-level MC5 |
| `lem:curve-H20-vanishing` | `lemma` | `ProvedElsewhere` | 782 | 0 | 0 | Curve-fibre Hodge dimension |
| `prop:central-m0-vacuum-proportionality` | `proposition` | `ProvedHere` | 811 | 0 | 0 | Sub-argument (b): vacuum-proportionality uniqueness of the central degree-2 curvature |
| `lem:sl2-sl2-splitting` | `lemma` | `ProvedElsewhere` | 1043 | 0 | 3 | $SL_2\times SL_2$ splitting of the bi-filtration |
| `lem:sl2-admissible-splitting` | `lemma` | `ProvedElsewhere` | 1587 | 0 | 3 | $\mathfrak{sl}_2^{\oplus\mathrm{adm}}$ splitting of the Malcev ladder |
| `thm:mc5-infty-one-obstruction-tower` | `theorem` | `ProvedHere` | 2629 | 0 | 3 | $(\infty,1)$-bar--cobar inversion on $\Perf(\AbarTwo)$: the obstruction tower |
| `thm:mc5-bridgeland-slicing-reads-obstruction-tower` | `theorem` | `ProvedHere` | 2678 | 3 | 4 | Bridgeland slicing reads the obstruction tower |

#### `chapters/theory/mc5_genus0_genus1_wall_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:mc5-g0g1-wall-five-point-sewing` | `theorem` | `ProvedHere` | 169 | 4 | 0 | MC5 5-point sewing with genus-one clutching |
| `cor:mc5-g0g1-heisenberg-elliptic-function` | `corollary` | `ProvedHere` | 510 | 2 | 0 | Heisenberg elliptic function at the wall |
| `cor:mc5-g0g1-k3-elliptic-genus` | `corollary` | `ProvedHere` | 590 | 1 | 1 | K3 elliptic genus at the wall |

#### `chapters/theory/motivic_shadow_full_class_m_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:w3-w-line-motivic-rationality` | `proposition` | `ProvedHere` | 270 | 0 | 0 | \label{prop:w3-w-line-motivic-rationality} $\cW_3$ W-line explicit rationality |
| `thm:bp-motivic-rationality-arakawa` | `theorem` | `ProvedHere` | 319 | 1 | 0 | \label{thm:bp-motivic-rationality-arakawa}BP T-line motivic rationality in Arakawa convention |
| `prop:bp-fl-convention-caveat` | `proposition` | `ProvedHere` | 357 | 1 | 0 | \label{prop:bp-fl-convention-caveat}FL-convention Koszul conductor: distinct constant |

#### `chapters/theory/motivic_shadow_tower.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:shadow-tower-motivic-lift` | `theorem` | `ProvedHere` | 218 | 0 | 0 | \label{thm:shadow-tower-motivic-lift}Motivic lift of Arnold-period shadow coefficients |
| `thm:grt-motivic-coaction` | `theorem` | `ProvedHere` | 301 | 1 | 0 | \label{thm:grt-motivic-coaction}Motivic coaction on the Arnold shadow-period envelope |
| `prop:s4-vir-mot` | `proposition` | `ProvedHere` | 382 | 0 | 0 | \label{prop:s4-vir-mot}Motivic lift of $S_4(\Vir_c)$ |
| `prop:s5-vir-mot` | `proposition` | `ProvedHere` | 421 | 0 | 0 | \label{prop:s5-vir-mot}Motivic lift of $S_5(\Vir_c)$ |
| `thm:virasoro-motivic-rationality-all-r` | `theorem` | `ProvedHere` | 525 | 1 | 0 | \label{thm:virasoro-motivic-rationality-all-r}Virasoro motivic rationality: weighted tower and manuscript boundary |
| `rem:characteristic-primes-are-riccati-arithmetic` | `remark` | `ProvedHere` | 689 | 0 | 0 | \label{rem:characteristic-primes-are-riccati-arithmetic}Characteristic primes of the shadow tower are Riccati-recurrence integers |
| `thm:kappa-vs-beta-split` | `theorem` | `ProvedHere` | 821 | 0 | 0 | \label{thm:kappa-vs-beta-split}Motivic kappa, modular beta |

#### `chapters/theory/nilpotent_completion.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:geom-conilpotent` | `proposition` | `ProvedHere` | 117 | 0 | 0 | Collision trees and coradical degree |
| `thm:completion-convergence` | `theorem` | `ProvedHere` | 172 | 1 | 0 | Finite-window convergence |
| `thm:completed-bar-cobar` | `theorem` | `ProvedHere` | 301 | 1 | 0 | Completed finite-window bar--cobar inversion |
| `thm:koszul-dual-characterization` | `theorem` | `ProvedHere` | 357 | 2 | 0 | Essential image of finite-window bar towers |
| `thm:BD-chiral-homology` | `theorem` | `ProvedElsewhere` | 436 | 0 | 1 | BD chiral homology \cite{BD04} |
| `prop:practical-convergence` | `proposition` | `ProvedHere` | 562 | 0 | 0 | Weight-window convergence |
| `thm:CG-renorm` | `theorem` | `ProvedElsewhere` | 608 | 0 | 1 | Costello--Gwilliam renormalization \cite{CG17} |
| `thm:stabilized-completion-positive` | `theorem` | `ProvedHere` | 704 | 0 | 0 | Stabilized completion for positive towers |
| `lem:finite-resonance-tensor-exact` | `lemma` | `ProvedHere` | 811 | 0 | 0 | Exact tensoring with a finite resonance tower |
| `thm:resonance-filtered-bar-cobar` | `theorem` | `ProvedHere` | 847 | 3 | 0 | Resonance-filtered completed bar/cobar |
| `prop:resonance-ss-degeneration` | `proposition` | `ProvedHere` | 963 | 1 | 0 | Resonance spectral sequence degeneration |
| `prop:resonance-ranks-standard` | `proposition` | `ProvedHere` | 990 | 2 | 0 | Resonance ranks of the standard families |
| `cor:virasoro-resonance-ss` | `corollary` | `ProvedHere` | 1065 | 1 | 0 | Virasoro resonance spectral sequence |
| `thm:platonic-completion` | `theorem` | `ProvedHere` | 1145 | 6 | 0 | Resonance completion |
| `rem:nc-brown-deligne` | `remark` | `ProvedElsewhere` | 1655 | 0 | 2 | Brown's motivic MZV dimensions through weight~$12$ |
| `prop:nc-massey-triple-rrr-E8` | `proposition` | `ProvedHere` | 2426 | 0 | 4 | Associator-free chain-level triple Massey product |
| `prop:nc-delta-n-explicit-higher` | `proposition` | `ProvedHere` | 2807 | 3 | 2 | Explicit recurrence for $\delta^{(n)}$ at $n \ge 7$ |

#### `chapters/theory/ordered_associative_chiral_kd.tex` (101)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:bicom-e` | `lemma` | `ProvedHere` | 268 | 0 | 0 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | `ProvedHere` | 395 | 0 | 0 | Ordered chiral shuffle theorem |
| `prop:r-matrix-descent-vol1` | `proposition` | `ProvedHere` | 701 | 3 | 0 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | `ProvedHere` | 849 | 4 | 0 | Pole-free descent is naive |
| `prop:symmetric-descent` | `proposition` | `ProvedHere` | 886 | 2 | 0 | Symmetric descent and ordered surplus |
| `thm:opposite` | `theorem` | `ProvedHere` | 1069 | 0 | 0 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | `ProvedHere` | 1110 | 1 | 0 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | `ProvedHere` | 1155 | 0 | 0 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | `ProvedHere` | 1175 | 1 | 0 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | `ProvedHere` | 1242 | 0 | 0 | — |
| `prop:one-defect` | `proposition` | `ProvedHere` | 1269 | 0 | 0 | — |
| `thm:tangent=K` | `theorem` | `ProvedHere` | 1291 | 0 | 0 | Tangent identification |
| `cor:infdual` | `corollary` | `ProvedHere` | 1328 | 2 | 0 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | `ProvedHere` | 1360 | 2 | 0 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | `ProvedHere` | 1412 | 3 | 0 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | `ProvedHere` | 1445 | 1 | 0 | Diagonal correspondence |
| `cor:unit` | `corollary` | `ProvedHere` | 1493 | 2 | 0 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | `ProvedHere` | 1511 | 1 | 0 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | `ProvedHere` | 1547 | 2 | 0 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | `ProvedHere` | 1579 | 1 | 0 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | `ProvedHere` | 1605 | 1 | 0 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | `ProvedHere` | 1630 | 1 | 0 | Cap action |
| `thm:pair-of-pants` | `theorem` | `ProvedHere` | 1693 | 1 | 0 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | `ProvedHere` | 1731 | 4 | 0 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | `ProvedHere` | 1785 | 1 | 0 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | `ProvedHere` | 1834 | 2 | 0 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | `ProvedHere` | 1864 | 12 | 0 | Master theorem |
| `def:ordered-real-config` | `definition` | `ProvedHere` | 1960 | 0 | 0 | Ordered real configuration space |
| `prop:ordered-real-config-topology` | `proposition` | `ProvedHere` | 1975 | 0 | 0 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | `ProvedHere` | 2457 | 1 | 0 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | `ProvedHere` | 2571 | 1 | 0 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | `ProvedHere` | 2658 | 0 | 0 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | `ProvedHere` | 2717 | 0 | 0 | Formality: class~G, shadow depth~$2$ |
| `thm:drinfeld-yangian-sl2` | `theorem` | `ProvedHere` | 2857 | 6 | 0 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | `ProvedHere` | 2947 | 0 | 0 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | `ProvedHere` | 2983 | 3 | 0 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | `ProvedHere` | 3035 | 3 | 0 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | `ProvedHere` | 3076 | 7 | 0 | Classical limit |
| `thm:central-extension-invisible` | `theorem` | `ProvedHere` | 3167 | 0 | 0 | Central extension is invisible to the ordered double bar |
| `thm:two-colour-double-kd` | `theorem` | `ProvedHere` | 3242 | 1 | 0 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | `ProvedHere` | 3270 | 2 | 0 | Non-redundancy of the two colours |
| `prop:vir-collision-residue` | `proposition` | `ProvedHere` | 3349 | 2 | 0 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | `ProvedHere` | 3384 | 2 | 0 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | `ProvedHere` | 3413 | 0 | 0 | Gravitational Yangian collapse |
| `prop:grav-yangian-curvature` | `proposition` | `ProvedHere` | 3547 | 1 | 0 | Gravitational Yangian curvature |
| `thm:root-space-one-dim-v1` | `theorem` | `ProvedHere` | 4173 | 0 | 0 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | `ProvedHere` | 4222 | 0 | 0 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | `ProvedHere` | 4288 | 0 | 0 | Dynkin coefficient via the beta integral |
| `thm:sl3-triangle-coefficient` | `theorem` | `ProvedHere` | 4919 | 0 | 0 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | `ProvedHere` | 5003 | 0 | 0 | Serre relations from root-space vanishing |
| `thm:sl4-quadrilateral` | `theorem` | `ProvedHere` | 5201 | 1 | 0 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:annular-bar-differential` | `theorem` | `ProvedHere` | 5491 | 1 | 0 | Annular bar differential |
| `thm:annular-HH` | `theorem` | `ProvedHere` | 5584 | 3 | 0 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | `ProvedHere` | 5707 | 1 | 0 | Curvature--braiding dichotomy at genus~$1$ |
| `def:kz-connection` | `definition` | `ProvedHere` | 5895 | 0 | 0 | KZ connection |
| `def:kzb-connection` | `definition` | `ProvedHere` | 5969 | 0 | 0 | KZB connection |
| `thm:b-cycle-quantum-group` | `theorem` | `ProvedHere` | 6037 | 2 | 0 | Quantum-group parameter from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | `ProvedElsewhere` | 6299 | 3 | 0 | Drinfeld--Kohno on the affine evaluation surface; {} for monodromy, {} for ordered reduction |
| `thm:yangian-quantum-group` | `theorem` | `ProvedHere` | 6394 | 2 | 0 | Affine genus-one monodromy readout |
| `prop:dk-q-convention-bridge` | `proposition` | `ProvedHere` | 6458 | 2 | 0 | Quantum-group convention bridge for DK/KZ readouts |
| `cor:sl2-root-of-unity` | `corollary` | `ProvedHere` | 6542 | 0 | 0 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | `ProvedHere` | 6583 | 1 | 0 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `def:ordered-tridegree` | `definition` | `ProvedHere` | 6718 | 0 | 0 | Ordered tridegree |
| `thm:ordered-depth-spectrum` | `theorem` | `ProvedHere` | 6749 | 0 | 0 | Ordered pole-depth spectrum |
| `thm:ordered-AOS` | `theorem` | `ProvedHere` | 6808 | 2 | 0 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | `ProvedHere` | 6887 | 2 | 0 | Averaging and surplus |
| `prop:ker-av-schur-weyl` | `proposition` | `ProvedHere` | 7118 | 0 | 0 | Kernel of the Reynolds projector: general simple Lie algebras |
| `thm:elliptic-spectral-dichotomy` | `theorem` | `ProvedHere` | 7372 | 2 | 0 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `thm:bg-ordered-bar` | `theorem` | `ProvedHere` | 7580 | 0 | 0 | Free-field ordered bar complexes |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | `ProvedHere` | 7762 | 1 | 0 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | `ProvedHere` | 7828 | 0 | 0 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | `ProvedHere` | 7887 | 2 | 0 | Ordered Koszul dual of lattice algebras |
| `constr:evaluation-map` | `construction` | `ProvedHere` | 7995 | 0 | 0 | Evaluation homomorphism |
| `comp:sl2-eval` | `computation` | `ProvedHere` | 8042 | 1 | 0 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | `ProvedHere` | 8108 | 0 | 0 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | `ProvedHere` | 8156 | 1 | 0 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | `ProvedHere` | 8198 | 1 | 0 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | `ProvedHere` | 8247 | 2 | 0 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `thm:drinfeld-classification` | `theorem` | `ProvedElsewhere` | 8296 | 0 | 0 | Drinfeld classification |
| `prop:eval-drinfeld` | `proposition` | `ProvedHere` | 8319 | 0 | 0 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | `ProvedHere` | 8386 | 2 | 0 | Line category as finite-dimensional modules |
| `thm:eval-braiding` | `theorem` | `ProvedHere` | 8466 | 0 | 0 | Braiding from the $R$-matrix |
| `thm:grothendieck-yangian` | `theorem` | `ProvedElsewhere` | 8511 | 0 | 0 | Grothendieck ring of Yangian modules |
| `prop:r-matrix-eigenvalue` | `proposition` | `ProvedHere` | 8573 | 0 | 0 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | `ProvedHere` | 8600 | 1 | 0 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | `ProvedHere` | 8699 | 1 | 0 | $\mathsf{E}_1$ ordered bar landscape |
| `lem:coprod-T-miura` | `lemma` | `ProvedHere` | 10636 | 1 | 1 | Miura inversion of the spectral coproduct at spin~$2$ |
| `prop:spin3-miura-coprod` | `proposition` | `ProvedHere` | 10719 | 2 | 0 | Spin-$3$ Miura coproduct |
| `lem:miura-triangularity-under-Delta` | `lemma` | `ProvedHere` | 10768 | 1 | 0 | Miura triangularity under the Drinfeld coproduct |
| `lem:qdet-central-all-N` | `lemma` | `ProvedElsewhere` | 11924 | 0 | 1 | Centrality of the quantum determinant at rank $N$ |
| `thm:FG-shadow-vol2` | `theorem` | `ProvedElsewhere` | 12141 | 0 | 0 | Comm\-utator-shadow theorem |
| `thm:ordered-associative-modular-mc` | `theorem` | `ProvedElsewhere` | 12227 | 0 | 0 | Associative modular Maurer--Cartan class |
| `thm:ordered-associative-ds-principal` | `theorem` | `ProvedElsewhere` | 12267 | 0 | 0 | Reduction commutes with associative chiral duality \textup{(}principal case\textup{)} |
| `prop:dual-number-bialgebra-obstruction` | `proposition` | `ProvedHere` | 12363 | 0 | 0 | The dual-number obstruction |
| `prop:bar-is-coderived-chiral-bialgebra` | `proposition` | `ProvedHere` | 12465 | 1 | 0 | The ordered bar complex is a chiral coalgebra |
| `prop:r-matrix-stable-envelope` | `proposition` | `ProvedHere` | 13032 | 0 | 0 | $R$-matrix comparison |
| `thm:e3-identification-km` | `theorem` | `ProvedHere` | 13093 | 1 | 0 | $\mathsf{E}_3$ identification for affine Kac--Moody |
| `prop:critical-level-ordered` | `proposition` | `ProvedHere` | 13193 | 0 | 0 | Critical level: monodromy trivialises, Koszulness fails, center jumps |
| `comp:ds-w3-degree2-rtt-miura-witness` | `computation` | `ProvedHere` | 13337 | 1 | 0 | Finite DS--Miura coproduct window at $\cW_3$ |
| `rem:bernard-heat-identity-zeta` | `remark` | `ProvedElsewhere` | 13473 | 2 | 2 | Bernard heat identity for the Weierstrass $\zeta$ |
| `rem:kzb-n-point-dynamical-closure` | `remark` | `ProvedElsewhere` | 13542 | 3 | 3 | $n \geq 3$ KZB flatness: Felder dynamical shift + Halphen--Ramanujan |

#### `chapters/theory/periodic_cdg_admissible.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:universal-pbw-koszul-admissible-parameters` | `proposition` | `ProvedHere` | 74 | 1 | 0 | Universal PBW--Koszul lane at admissible parameters |

#### `chapters/theory/poincare_duality.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:verdier-config` | `theorem` | `ProvedElsewhere` | 247 | 0 | 1 | Verdier duality for configuration spaces; {} \cite{KS90} |
| `thm:dual-differentials` | `theorem` | `ProvedHere` | 337 | 1 | 0 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | `ProvedHere` | 505 | 1 | 0 | Bar coalgebra and Verdier algebra |
| `thm:bar-computes-dual` | `theorem` | `ProvedHere` | 584 | 5 | 0 | Bar coalgebra, quadratic model, and Verdier algebra |
| `comp:bar-dual-low-degrees` | `computation` | `ProvedHere` | 699 | 0 | 0 | Degree 0 and 1 |

#### `chapters/theory/poincare_duality_quantum.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:universal-defect-construction` | `theorem` | `ProvedElsewhere` | 284 | 0 | 1 | Finite-type Ext model for the defect algebra {\cite{LV12}} |
| `__unlabeled_chapters/theory/poincare_duality_quantum.tex:371` | `calculation` | `ProvedElsewhere` | 371 | 0 | 1 | Yangian structure constants {\cite{Drinfeld85}} |
| `thm:ff-center` | `theorem` | `ProvedElsewhere` | 421 | 0 | 2 | Feigin--Frenkel center {\cite{Feigin-Frenkel,BD04}} |
| `thm:fact-homology-quantum` | `theorem` | `ProvedElsewhere` | 494 | 0 | 2 | Factorization homology and the bar complex {\cite{Francis2013,HA}} |
| `prop:chiral-operad-genus0` | `proposition` | `ProvedHere` | 539 | 0 | 3 | Genus-zero identification |
| `def:feynman-transform` | `definition` | `ProvedElsewhere` | 767 | 0 | 1 | Feynman transform |
| `thm:prism-higher-genus` | `theorem` | `ProvedHere` | 823 | 3 | 1 | Prism principle: higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | `ProvedHere` | 895 | 0 | 0 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | `ProvedHere` | 920 | 2 | 0 | The loop expansion is the genus expansion |
| `cor:feynman-transform-involution` | `corollary` | `ProvedElsewhere` | 1089 | 0 | 1 | Feynman transform involution {\cite{GeK98}} |
| `thm:modular-convolution-structure` | `theorem` | `ProvedHere` | 1168 | 0 | 1 | dg~Lie structure |
| `thm:vol1-genus-completion` | `theorem` | `ProvedHere` | 1208 | 1 | 0 | Genus completion |
| `prop:vol1-structure-as-MC` | `proposition` | `ProvedHere` | 1256 | 2 | 0 | The algebra structure as MC element |
| `prop:log-forms-conformal-invariance` | `proposition` | `ProvedElsewhere` | 1297 | 0 | 1 | Forced by conformal invariance {\cite{BPZ84}} |
| `lem:sign-consistency-bar` | `lemma` | `ProvedElsewhere` | 1336 | 0 | 1 | Sign consistency for bar differential {\cite{LV12}} |
| `thm:bar-cobar-adjunction-operadic` | `theorem` | `ProvedElsewhere` | 1352 | 1 | 1 | Bar-cobar adjunction {\cite{LV12}} |
| `thm:partition` | `theorem` | `ProvedHere` | 1368 | 0 | 2 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:genus-refined-linfty` | `definition` | `ProvedHere` | 791 | 1 | 0 | Genus-refined $L_\infty$ operations |
| `thm:quantum-linfty-master` | `theorem` | `ProvedHere` | 839 | 3 | 0 | Quantum $L_\infty$ master equation |
| `thm:non-renormalization-tree` | `theorem` | `ProvedElsewhere` | 950 | 0 | 1 | Non-renormalization at tree level |
| `cor:exact-r-matrix` | `corollary` | `ProvedElsewhere` | 981 | 2 | 0 | Collision residue normalization for standard-family $r$-matrices |
| `prop:two-element-strict` | `proposition` | `ProvedHere` | 1107 | 2 | 0 | Two-element covers are strict |
| `prop:jacobiator-nullhomotopic` | `proposition` | `ProvedElsewhere` | 1184 | 2 | 1 | Jacobiator is nullhomotopic |

#### `chapters/theory/shadow_L_function_platonic.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:shadow-L-series` | `definition` | `ProvedHere` | 78 | 0 | 0 | \label{def:shadow-L-series}Shadow Dirichlet series |
| `prop:shL-convergence-half-plane` | `proposition` | `ProvedHere` | 103 | 0 | 0 | \label{prop:shL-convergence-half-plane}Formal uniqueness and analytic growth datum |
| `def:hurwitz-lerch-shadow` | `definition` | `ProvedHere` | 128 | 0 | 0 | \label{def:hurwitz-lerch-shadow}Hurwitz--Lerch admissibility |
| `thm:kummer-congruence-prediction` | `theorem` | `ProvedElsewhere` | 362 | 3 | 0 | \label{thm:kummer-congruence-prediction}Bernoulli--Kummer witnesses for the genus slots |

#### `chapters/theory/shadow_tower_higher_coefficients.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:sth-virasoro-local-product` | `theorem` | `ProvedHere` | 77 | 1 | 0 | Virasoro local product |
| `thm:sth-virasoro-ward-correlators` | `theorem` | `ProvedHere` | 102 | 4 | 0 | Sphere Ward correlators |
| `thm:sth-level-four-gram` | `theorem` | `ProvedHere` | 167 | 0 | 0 | Level-four vacuum Gram matrix |
| `cor:sth-lambda-norm` | `corollary` | `ProvedHere` | 212 | 1 | 0 | The Zamolodchikov quasi-primary norm |

#### `chapters/theory/shadow_tower_other_class_M_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:bp-tline-rational` | `proposition` | `ProvedHere` | 307 | 1 | 0 | BP $T$-line: rationality in $k$ |
| `cor:bp-tline-koszul-conductor` | `corollary` | `ProvedHere` | 330 | 0 | 0 | BP $T$-line: Koszul conductor, Feigin--Frenkel duality |
| `prop:bp-jline-gaussian` | `proposition` | `ProvedHere` | 345 | 0 | 0 | BP $J$-line: Gaussian, depth 2 |
| `prop:wn-line-decomposition` | `proposition` | `ProvedHere` | 388 | 0 | 0 | $W_N$ line decomposition of $\kappa$ |
| `prop:w-infinity-line-decomposition` | `proposition` | `ProvedHere` | 470 | 1 | 0 | $W_\infty\lbrack\mu\rbrack$ line-by-line decomposition |
| `prop:super-yangian-kappa` | `proposition` | `ProvedHere` | 544 | 0 | 0 | Super-Yangian modular characteristic |
| `prop:super-yangian-tline-shadow` | `proposition` | `ProvedHere` | 566 | 0 | 0 | Super-Yangian $T$-line: Virasoro shadow with graded parity |
| `cor:super-yangian-tline-asymptotic` | `corollary` | `ProvedHere` | 620 | 0 | 0 | Super-Yangian leading $T$-line asymptotic |
| `rem:wp-cross-channel-quartic` | `remark` | `ProvedHere` | 903 | 0 | 0 | Cross-channel quartic on the $T$-$W$ mixed line |

#### `chapters/theory/shadow_tower_quadrichotomy_platonic.tex` (31)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:spectral-hyperelliptic-pf` | `theorem` | `ProvedHere` | 735 | 3 | 0 | Spectral hyperelliptic curve and Picard--Fuchs |
| `cor:branch-points-instantons` | `corollary` | `ProvedHere` | 788 | 0 | 0 | Branch points and inverse-root actions |
| `thm:stokes-line-c-S` | `theorem` | `ProvedHere` | 812 | 0 | 0 | Virasoro branch-root radius and caesura |
| `thm:S6-Vir-closed` | `theorem` | `ProvedHere` | 891 | 2 | 0 | Formal order-six relation coefficient |
| `thm:riccati-U` | `theorem` | `ProvedHere` | 939 | 2 | 0 | Riccati-on-$U$ master equation |
| `prop:c1-riccati-mc` | `proposition` | `ProvedHere` | 975 | 3 | 0 | C1: Riccati MC element |
| `thm:borel-summability-classM` | `theorem` | `ProvedHere` | 1051 | 2 | 0 | C3: Algebraic continuation of the class M metric series |
| `thm:c4-shadow-feynman-gk` | `theorem` | `ProvedHere` | 1133 | 0 | 0 | C4: Shadow--Feynman as $\partial^{2} = 0$ at $b_1 = L$ |
| `prop:c5-hardy-ramanujan-cardy` | `proposition` | `ProvedHere` | 1250 | 0 | 0 | Universal Virasoro vacuum growth |
| `thm:c5-zwegers-mu-shadow-explicit` | `theorem` | `ProvedHere` | 1299 | 1 | 0 | Obstruction to a generic Zwegers $\mu$-shadow for $\Vir_c$ |
| `prop:universal-base-CA-six` | `proposition` | `ProvedElsewhere` | 1362 | 0 | 0 | Universal exponential base on the class M $T$-line |
| `prop:w3-Wline-twelve` | `proposition` | `ProvedElsewhere` | 1392 | 0 | 0 | $\cW_3$ second lane $C^{W{\rm-line}}_{\cW_3} = 12$ |
| `prop:virasoro-inverse-root-field` | `proposition` | `ProvedElsewhere` | 1428 | 0 | 0 | Virasoro inverse-root field |
| `prop:lee-yang-phase` | `proposition` | `ProvedElsewhere` | 1443 | 0 | 0 | Lee--Yang pole at $c = -22/5$ |
| `prop:double-root-phase` | `proposition` | `ProvedHere` | 1454 | 1 | 0 | Secondary rational zero at $c = -83/20$ |
| `prop:omega-large-c-expansion` | `proposition` | `ProvedHere` | 1486 | 2 | 0 | Large-$c$ expansion of the Virasoro branch root |
| `prop:beta-N-per-spin-lane` | `proposition` | `ProvedElsewhere` | 1506 | 1 | 0 | $\beta_N = 12 (H_N - 1)$ per-spin lane |
| `prop:wp-triplet-T-Cartan-line` | `proposition` | `ProvedElsewhere` | 1521 | 1 | 0 | $\cW(p)$ triplet $T$-line and Cartan-line shadows |
| `prop:critical-ff-companion-shadow` | `proposition` | `ProvedElsewhere` | 1560 | 3 | 0 | Critical Feigin--Frenkel companion |
| `prop:stqp-312-factor` | `proposition` | `ProvedHere` | 1800 | 3 | 0 | $c_{2d} = -214$ shadow-tower decomposition |
| `rem:stqp-mock-weight` | `remark` | `ProvedElsewhere` | 1926 | 0 | 0 | Mock-modular shadow weight from $c = -214$; Siegel weight $5$ |
| `rem:stqp-cardy` | `remark` | `ProvedElsewhere` | 1961 | 1 | 0 | Cardy counting at $c = -214$ |
| `prop:stqp-signature` | `proposition` | `ProvedHere` | 2112 | 0 | 0 | Hyperbolic Cartan signature $(2,1)$ for $\mathbf H_{\Delta_5}$ |
| `prop:stqp-unitary-spectrum` | `proposition` | `ProvedHere` | 2210 | 1 | 0 | Positive-energy unitary spectrum |
| `cor:stqp-real-imag-dichotomy` | `corollary` | `ProvedHere` | 2271 | 0 | 0 | Real-root / imaginary-root dichotomy |
| `rem:stqp-ceff-unitarity` | `remark` | `ProvedHere` | 2296 | 3 | 0 | Effective central charge unitarity reading $c_{\mathrm{eff}} = -166$ |
| `prop:stqp-theta-p-clustering` | `proposition` | `ProvedHere` | 2440 | 1 | 0 | Observed Fricke-node counts for the 22 primes $p \le 79$ |
| `prop:stqp-gauss-kuzmin` | `proposition` | `ProvedHere` | 2552 | 0 | 0 | Nearest-node deviation statistic on the $22$-prime sample |
| `prop:stqp-gauss-kuzmin-asymptotic` | `proposition` | `ProvedHere` | 2577 | 0 | 0 | Fixed-node Sato--Tate limit and the failure of a $\sqrt p$ law |
| `thm:stqp-fricke-z8-phase-leading` | `theorem` | `ProvedElsewhere` | 2740 | 2 | 0 | $\mathbb Z/8$ half-angle nodes and Sato--Tate leading term |
| `thm:stqp-fricke-z8-phase-subleading` | `theorem` | `ProvedHere` | 2816 | 2 | 0 | $\mathbb Z/8$-phase subleading correction: the $\cos(2\theta^*_k)$ curvature term |

#### `chapters/theory/shadow_tower_sub_subleading_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:phi-laurent` | `definition` | `ProvedHere` | 105 | 0 | 0 | \label{def:phi-laurent}Rescaled Phi and its Laurent data |
| `lem:phi-recurrence` | `lemma` | `ProvedHere` | 118 | 0 | 0 | \label{lem:phi-recurrence}Phi-recurrence |
| `prop:gamma-recurrence` | `proposition` | `ProvedHere` | 150 | 1 | 0 | \label{prop:gamma-recurrence}Gamma recurrence |
| `lem:gamma-source-ratio-closed-form` | `lemma` | `ProvedHere` | 180 | 1 | 0 | \label{lem:gamma-source-ratio-closed-form}Source-ratio closed form |
| `thm:shadow-tower-sub-subleading-closed-form` | `theorem` | `ProvedHere` | 244 | 2 | 0 | \label{thm:shadow-tower-sub-subleading-closed-form} Sub-subleading Virasoro shadow asymptotic |
| `lem:gamma-numerator-quartic-polynomial` | `lemma` | `ProvedHere` | 367 | 0 | 0 | \label{lem:gamma-numerator-quartic-polynomial}Gamma numerator polynomial |
| `lem:gamma-numerator-irreducible` | `lemma` | `ProvedHere` | 395 | 0 | 0 | \label{lem:gamma-numerator-irreducible}Irreducibility over $\mathbb{Q}$ |
| `rem:gamma-691-emergence-sporadic` | `remark` | `ProvedHere` | 415 | 0 | 0 | \label{rem:gamma-691-emergence-sporadic}The $691$ at $r = 8$ is a modular coincidence |
| `rem:gamma-irregular-primes-dense-but-structureless` | `remark` | `ProvedHere` | 439 | 0 | 0 | \label{rem:gamma-irregular-primes-dense-but-structureless} Irregular primes appear densely but structurelessly |

#### `chapters/theory/spectral_sequences.tex` (14)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:early-pages` | `theorem` | `ProvedElsewhere` | 79 | 0 | 0 | Identification of early pages |
| `thm:classical-convergence` | `theorem` | `ProvedElsewhere` | 124 | 0 | 1 | Classical convergence theorem \cite{Weibel94} |
| `prop:first-quadrant` | `proposition` | `ProvedElsewhere` | 166 | 0 | 0 | First quadrant spectral sequences |
| `thm:zeeman` | `theorem` | `ProvedElsewhere` | 195 | 0 | 0 | Zeeman comparison theorem |
| `thm:spectral-sequence-filtered-dg` | `theorem` | `ProvedElsewhere` | 214 | 2 | 0 | Spectral sequence of a filtered dg Lie algebra |
| `prop:complete-filt-convergence` | `proposition` | `ProvedElsewhere` | 244 | 0 | 2 | Convergence for complete filtrations \cite{Weibel94, Boardman-conditional} |
| `thm:bar-ss` | `theorem` | `ProvedHere` | 277 | 1 | 0 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | `ProvedHere` | 329 | 2 | 0 | Degeneration for Koszul algebras |
| `thm:genus-ss` | `theorem` | `ProvedElsewhere` | 384 | 0 | 1 | Genus spectral sequence \cite{BD04} |
| `thm:genus-ss-convergence` | `theorem` | `ProvedElsewhere` | 437 | 0 | 2 | Convergence of genus spectral sequence \cite{Weibel94, BD04} |
| `thm:chevalley-cousin-ss` | `theorem` | `ProvedElsewhere` | 481 | 0 | 2 | Chevalley--Cousin spectral sequence \cite{Har77, KS90} |
| `thm:cousin-resolution` | `theorem` | `ProvedElsewhere` | 517 | 0 | 1 | Cousin resolution for holonomic D-modules \cite{KS90} |
| `prop:bar-ss-mult` | `proposition` | `ProvedElsewhere` | 549 | 0 | 1 | Bar spectral sequence is multiplicative \cite{LV12} |
| `thm:mult-ss-conv` | `theorem` | `ProvedElsewhere` | 562 | 0 | 1 | Convergence of multiplicative spectral sequences \cite{Weibel94} |

#### `chapters/theory/theorem_A_infinity_2.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:A-square-zero-bar-cobar` | `computation` | `ProvedHere` | 321 | 1 | 0 | The first square-zero algebra |
| `cor:no-dual-from-barcobar-counit` | `corollary` | `ProvedHere` | 515 | 4 | 0 | Typed comparison of reconstruction and Verdier duality |
| `prop:A-module-completion-firewall` | `proposition` | `ProvedHere` | 580 | 2 | 0 | Module transport along the bar--cobar counit |
| `lem:archetype-H123-witness` | `lemma` | `ProvedHere` | 643 | 0 | 0 | Positive local finiteness passes to the reduced bar |
| `prop:A-universal-chain-homotopy` | `proposition` | `ProvedHere` | 796 | 0 | 0 | Rescaling identity for a deformation retract |
| `cor:eight-cor-counit-qi` | `corollary` | `ProvedElsewhere` | 934 | 2 | 0 | Universal reconstruction in the enhanced Ran ambient |
| `thm:hackney-robertson-model` | `theorem` | `ProvedElsewhere` | 1270 | 0 | 1 | Hackney--Robertson--Yau model structure on simplicial properads |

#### `chapters/theory/theorem_B_scope_platonic.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:weight-filtration-basics` | `lemma` | `ProvedHere` | 223 | 0 | 0 | Filtration basics |
| `lem:virasoro-mode-pair-no-raw-limit` | `lemma` | `ProvedHere` | 311 | 0 | 0 | A Virasoro state family in the weight completion |
| `prop:class-m-mode-family-obstruction-package` | `proposition` | `ProvedHere` | 338 | 0 | 0 | A completed comparison series and its discrete support |
| `lem:total-weight-rees-finite-cdg-tower` | `lemma` | `ProvedHere` | 532 | 2 | 0 | Strict total-weight Rees tower criterion |
| `lem:hom-cone-ml-rees-towers` | `lemma` | `ProvedHere` | 633 | 1 | 1 | Hom-cone Mittag--Leffler for strict finite-window towers |
| `prop:chiral-positselski-raw-direct-sum-class-M-false` | `proposition` | `ProvedHere` | 806 | 3 | 0 | State-family separation for the class-\(\mathsf M\) presentation |
| `rem:theorem-B-chain-level-G-L-attribution` | `remark` | `ProvedElsewhere` | 835 | 1 | 1 | Universal reconstruction for the standard families |
| `lem:ff-center-finite-weight-windows` | `lemma` | `ProvedHere` | 913 | 2 | 0 | Finite Feigin--Frenkel weight windows |
| `lem:tbsp-bar-valpha1-first-terms` | `lemma` | `ProvedHere` | 1872 | 1 | 0 | First three bar degrees |
| `lem:tbsp-bar-ss-collapse` | `lemma` | `ProvedElsewhere` | 2062 | 0 | 0 | Collapse of the two-sided bar spectral sequence |
| `prop:tbsp-homotopy-n4-valpha1` | `proposition` | `ProvedElsewhere` | 2094 | 0 | 0 | Bar degree \(4\) |
| `prop:tbsp-homotopy-n6-valpha1` | `proposition` | `ProvedElsewhere` | 2128 | 0 | 0 | Bar degree \(6\) |
| `cor:tbsp-homotopy-all-n-valpha1` | `corollary` | `ProvedElsewhere` | 2139 | 0 | 0 | Uniform two-sided contraction |

#### `chapters/theory/theorem_C_refinements_platonic.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:theorem-C-stable-genus-zero` | `proposition` | `ProvedHere` | 695 | 1 | 0 | Stable genus-zero specialization |

#### `chapters/theory/theorem_h_off_koszul_platonic.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:theorem-h-off-koszul-explicit-correction` | `theorem` | `ProvedHere` | 290 | 0 | 0 | Collision-depth tail exact sequence |
| `lem:theorem-h-degree-three-boundary` | `lemma` | `ProvedHere` | 361 | 2 | 0 | Degree-three boundary for a depth-zero cutoff at two |
| `cor:concentration-iff-defect-zero` | `corollary` | `ProvedHere` | 384 | 1 | 0 | Exact Hilbert tail for the cutoff $m=2$ |
| `prop:theorem-h-finite-window-kdh-retracts` | `proposition` | `ProvedHere` | 421 | 1 | 0 | Compatible finite-window retracts of the positive-depth complex |

#### `chapters/theory/three_hochschild_unification_platonic.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:three-hochschild-complexes` | `definition` | `ProvedElsewhere` | 55 | 1 | 2 | The three comparison complexes |
| `rem:hochschild-variant-firewall-table` | `remark` | `ProvedHere` | 94 | 0 | 0 | Hochschild variant firewall table |

#### `chapters/theory/three_invariants.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:three-invariants-relations` | `proposition` | `ProvedHere` | 221 | 3 | 0 | Relations and independence |
| `rem:fingerprint-koszul-symmetry` | `remark` | `ProvedHere` | 612 | 0 | 0 | Functorial symmetry under Koszul duality |
| `thm:five-class-stratum` | `theorem` | `ProvedHere` | 627 | 2 | 0 | Five-class stratum |
| `prop:coarse-projection-functor` | `proposition` | `ProvedHere` | 676 | 1 | 0 | Coarse projection functor |
| `cor:quadrichotomy-as-projection` | `corollary` | `ProvedHere` | 702 | 1 | 0 | Quadrichotomy $G/L/C/M$ as lossy projection |

#### `chapters/theory/topologization_chain_level_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:QG1-remainder` | `proposition` | `ProvedHere` | 244 | 5 | 0 | Explicit $Q$-variation of $G_1$ |
| `rem:NO-assoc` | `remark` | `ProvedElsewhere` | 322 | 2 | 1 | Normal-ordering associativity |
| `prop:eta-i-primitive` | `proposition` | `ProvedHere` | 334 | 3 | 0 | $\eta_1^{(\mathrm i)}$ is a $Q$-primitive of $R_{\mathrm{ghost}}$ |
| `prop:eta-ii-primitive` | `proposition` | `ProvedHere` | 397 | 2 | 0 | $\eta_1^{(\mathrm{ii})}$ is a $Q$-primitive of $R_{\mathrm{self}}$ |
| `cor:eta-primitive` | `corollary` | `ProvedHere` | 421 | 0 | 0 | $\eta_1$ is a $Q$-primitive of $R_1 := R_{\mathrm{ghost}} + R_{\mathrm{self}}$ |
| `thm:sugawara-antighost-primitive-chain-level` | `theorem` | `ProvedHere` | 433 | 5 | 0 | Sugawara antighost primitive, chain level |
| `prop:translation-inv-tildeG` | `proposition` | `ProvedHere` | 467 | 0 | 0 | Translation invariance of $\widetilde G_1$ |
| `prop:eta-formula-sl2-k1-explicit` | `proposition` | `ProvedHere` | 564 | 3 | 0 | $\eta_1$ formula at sl$_2$ level $1$ |
| `prop:critical-level-collapse` | `proposition` | `ProvedHere` | 621 | 1 | 1 | Critical-level collapse to $\Etwo^{\mathrm{top}}$ |

#### `chapters/theory/universal_conductor_K_platonic.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:uc-r-twisted-dg-lie-descent` | `theorem` | `ProvedHere` | 289 | 2 | 0 | Finite-window $R$-twisted descent for the differential and bracket |
| `thm:uc-universal-conductor` | `theorem` | `ProvedHere` | 416 | 6 | 0 | \textbf{Universal conductor as ordered-to-symmetric descent} |
| `thm:uc-trinity` | `theorem` | `ProvedHere` | 521 | 4 | 0 | \textbf{Three descriptions of the image} |
| `prop:uc-kernel-dimension` | `proposition` | `ProvedHere` | 597 | 1 | 0 | Schur--Weyl kernel count |
| `thm:uc-degree-two-rmatrix-kernel` | `theorem` | `ProvedHere` | 621 | 2 | 0 | Degree-two conductor kernel and ordered \texorpdfstring{$r$}{r}-matrix data |
| `thm:uc-kernel-archetypes` | `theorem` | `ProvedHere` | 719 | 4 | 0 | Named kernel witnesses by archetype |
| `thm:uc-landscape-universality` | `theorem` | `ProvedHere` | 844 | 2 | 0 | Constructed universality map on \texorpdfstring{$G/L/C/M$}{G/L/C/M} census rows |
| `thm:uc-K-Atiyah` | `theorem` | `ProvedHere` | 922 | 0 | 0 | Ordered-Koszul boundary for Vol~III comparisons |
| `cor:uc-K-heisenberg` | `corollary` | `ProvedHere` | 1019 | 0 | 0 | Heisenberg scalar packages |
| `cor:uc-K-affine-KM` | `corollary` | `ProvedHere` | 1041 | 0 | 0 | Affine Kac--Moody scalar packages |
| `cor:uc-K-betagamma` | `corollary` | `ProvedHere` | 1070 | 2 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} Verdier scalar sums |
| `cor:uc-K-virasoro` | `corollary` | `ProvedHere` | 1096 | 0 | 0 | Virasoro scalar packages |
| `cor:uc-K-lattice` | `corollary` | `ProvedHere` | 1361 | 1 | 0 | Lattice matter presentation |

#### `chapters/theory/virasoro_motivic_purity_all_r_platonic.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `ex:vmpar-q-rational-families` | `remark` | `ProvedHere` | 171 | 1 | 0 | Standard landscape families with $\mathbb{Q}$-rational OPE |
| `thm:virasoro-s-r-motivic-purity-all-r` | `theorem` | `ProvedHere` | 200 | 3 | 0 | \label{thm:virasoro-s-r-motivic-purity-all-r}Virasoro shadow-tower motivic purity, all $r \geq 2$ via master-equation recursion |
| `thm:class-M-motivic-purity-algebras-with-Q-rational-OPE` | `theorem` | `ProvedHere` | 312 | 2 | 0 | \label{thm:class-M-motivic-purity-algebras-with-Q-rational-OPE} Motivic purity on an $F$-rational finite-recurrence lane |
| `prop:mzv-would-enter-at-what-weight` | `proposition` | `ProvedHere` | 405 | 1 | 0 | \label{prop:mzv-would-enter-at-what-weight} Virasoro shadow coefficients contain no odd-zeta of any weight |

#### `chapters/theory/z_g_kummer_bernoulli_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:z-g-closed-form-polynomial` | `theorem` | `ProvedHere` | 60 | 1 | 0 | $Z_g(k)$ closed form |
| `thm:z-g-polynomial-form` | `theorem` | `ProvedHere` | 146 | 2 | 0 | Polynomial factorisation of $Z_g$ |
| `thm:z-g-leading-coefficient-bernoulli` | `theorem` | `ProvedHere` | 209 | 3 | 0 | Hurwitz--Bernoulli leading coefficient |
| `thm:z-g-kummer-congruence` | `theorem` | `ProvedHere` | 324 | 4 | 0 | Irregular-prime witnesses |
| `thm:z-g-s-r-arithmetic-duality` | `theorem` | `ProvedHere` | 528 | 3 | 0 | $Z_g$ vs $S_r(\Vir_c)$ arithmetic duality at the Bernoulli-leading Kummer pair |

### Part II: Examples (490)

#### `chapters/examples/bar_complex_tables.tex` (18)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | `ProvedHere` | 743 | 1 | 0 | Serre tensors are quadratic syzygies, not the dual algebra |
| `comp:sl3-casimir-decomp` | `computation` | `ProvedHere` | 1070 | 0 | 0 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | `ProvedHere` | 1151 | 0 | 0 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | `ProvedHere` | 1487 | 1 | 0 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | `ProvedHere` | 1803 | 1 | 0 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | `ProvedHere` | 1849 | 3 | 0 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | `ProvedHere` | 1921 | 0 | 1 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | `ProvedHere` | 1972 | 1 | 0 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | `ProvedHere` | 2109 | 1 | 0 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | `ProvedHere` | 2145 | 1 | 0 | Bar differential as BGG differential |
| `prop:G2-bar-dims` | `proposition` | `ProvedHere` | 2575 | 2 | 0 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | `ProvedHere` | 2779 | 0 | 0 | Virasoro curvature survives the degree-\texorpdfstring{$3$}{3} residue |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | `ProvedHere` | 2993 | 1 | 0 | Heisenberg bar complex: adjacent residues and central class |
| `prop:km-generic-acyclicity` | `proposition` | `ProvedHere` | 3056 | 1 | 0 | Universal Kac--Moody acyclicity; critical centre separated |
| `prop:w3-vacuum-dichotomy` | `proposition` | `ProvedHere` | 3096 | 2 | 0 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | `ProvedHere` | 3465 | 1 | 0 | Free fermion symmetric bar shadow: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | `ProvedHere` | 3670 | 1 | 0 | \texorpdfstring{$E_8$}{E_8} affine pre-quotient Koszul acyclicity |
| `prop:universal-dim-formula` | `proposition` | `ProvedHere` | 4023 | 2 | 0 | Free PBW bar dimension envelope |

#### `chapters/examples/bershadsky_polyakov.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:bp-ope-normal-form` | `proposition` | `ProvedElsewhere` | 226 | 0 | 2 | Feigin--Semikhatov OPE normal form for BP |
| `prop:bp-central-charge` | `proposition` | `ProvedHere` | 301 | 3 | 1 | BP central charge |
| `thm:bp-koszul-conductor-polynomial` | `theorem` | `ProvedHere` | 370 | 0 | 0 | Bershadsky--Polyakov central-charge conductor identity |
| `prop:sl3-conductor-shift-formula` | `proposition` | `ProvedHere` | 491 | 3 | 0 | Unified shift formula for $\mathfrak{sl}_3$ central-charge conductors |
| `prop:bp-jline-depth` | `proposition` | `ProvedHere` | 840 | 0 | 0 | J-line shadow depth |

#### `chapters/examples/beta_gamma.tex` (24)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:beta-gamma-modes` | `proposition` | `ProvedElsewhere` | 506 | 0 | 1 | Mode algebra \cite{FBZ04} |
| `thm:beta-gamma-stress` | `theorem` | `ProvedElsewhere` | 516 | 0 | 1 | Stress tensor and central charge \cite{FBZ04} |
| `thm:betagamma-fermion-koszul` | `theorem` | `ProvedHere` | 795 | 0 | 1 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | `ProvedHere` | 866 | 0 | 0 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | `ProvedHere` | 922 | 0 | 0 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | `ProvedHere` | 946 | 0 | 0 | — |
| `thm:cobar-fermions` | `theorem` | `ProvedHere` | 977 | 0 | 0 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | `ProvedHere` | 1016 | 3 | 0 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:physical-bosonization` | `theorem` | `ProvedElsewhere` | 1048 | 1 | 1 | Physical bosonization \cite{FBZ04} |
| `thm:beta-gamma-bar` | `theorem` | `ProvedHere` | 1133 | 1 | 0 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `thm:beta-gamma-universal` | `theorem` | `ProvedElsewhere` | 1183 | 0 | 1 | Universal property of \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} \cite{FBZ04} |
| `prop:betagamma-E1-page` | `proposition` | `ProvedHere` | 1785 | 0 | 1 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-interval-compactification` | `proposition` | `ProvedElsewhere` | 2066 | 0 | 1 | Interval compactification produces the full $\beta\gamma$ algebra {\cite{CDG20}, \S4.2} |
| `prop:mumford-exponent-complementarity` | `proposition` | `ProvedHere` | 2170 | 1 | 0 | Mumford exponent complementarity |
| `thm:betagamma-quartic-birth` | `theorem` | `ProvedHere` | 2512 | 3 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | `ProvedHere` | 2560 | 2 | 0 | $\beta\gamma$ weight-changing line is shadow-trivial |
| `lem:betagamma-ell2-vanishing` | `lemma` | `ProvedHere` | 2829 | 0 | 0 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | `ProvedHere` | 2876 | 3 | 0 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | `ProvedHere` | 2985 | 1 | 0 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | `ProvedHere` | 3020 | 0 | 0 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | `ProvedHere` | 3050 | 1 | 0 | Pure contact boundary law |
| `prop:betagamma-sugawara-class-c` | `proposition` | `ProvedHere` | 3130 | 2 | 0 | Why $\beta\gamma$ is class~$\mathsf{C}$: standard conformal-weight family |
| `prop:betagamma-translation-coproduct` | `proposition` | `ProvedHere` | 3247 | 0 | 0 | Translation and coproduct |
| `prop:betagamma-vortex-comodule` | `proposition` | `ProvedHere` | 3325 | 1 | 0 | $\bar{B}(\cA)$-comodule structure on vortex lines |

#### `chapters/examples/chiral_moonshine_unified.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:bar-euler-hilbert` | `proposition` | `ProvedHere` | 235 | 1 | 0 | Primitive bar-Euler product |
| `thm:moonshine-bar-euler-master` | `theorem` | `ProvedHere` | 295 | 4 | 0 | Denominator/bar-Euler comparison criterion |
| `thm:conway-chiral-structure` | `theorem` | `ProvedElsewhere` | 575 | 1 | 0 | Conway chiral input |

#### `chapters/examples/deformation_quantization.tex` (26)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:kontsevich-star-product` | `theorem` | `ProvedElsewhere` | 52 | 0 | 1 | Kontsevich 1997 \cite{Kon03} |
| `thm:chiral-quantization` | `theorem` | `ProvedHere` | 243 | 0 | 0 | Local coisson quantization and global obstruction |
| `thm:chiral-kontsevich` | `theorem` | `ProvedHere` | 338 | 2 | 0 | Local Kontsevich--chiral comparison |
| `thm:kontsevich-explicit-formula` | `theorem` | `ProvedElsewhere` | 463 | 0 | 1 | Explicit formula \cite{Kon03} |
| `thm:stokes-associativity` | `theorem` | `ProvedElsewhere` | 481 | 0 | 1 | Stokes' theorem yields associativity \cite{Kon03} |
| `thm:bar-computes-deformation` | `theorem` | `ProvedHere` | 544 | 1 | 0 | Chiral deformation complex from the bar construction |
| `prop:mc-star-product` | `proposition` | `ProvedHere` | 616 | 0 | 0 | MC elements and filtered chiral products |
| `lem:defq-shifted-obstruction-cocycle` | `lemma` | `ProvedHere` | 647 | 1 | 0 | Shifted obstruction cocycle |
| `thm:deformation-genus-expansion` | `theorem` | `ProvedHere` | 892 | 1 | 0 | Modular correction package |
| `thm:chiral-formality` | `theorem` | `ProvedElsewhere` | 964 | 0 | 3 | Local \texorpdfstring{$\Etwo$}{E2} formality input \cite{Tamarkin00, FG12} |
| `prop:ainfty-operations-config` | `proposition` | `ProvedElsewhere` | 1001 | 0 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} operations \cite{Kon03} |
| `thm:master-identity-deformation` | `theorem` | `ProvedElsewhere` | 1018 | 0 | 1 | Deformation-complex dictionary \cite{Kon03} |
| `thm:obstruction-quantization` | `theorem` | `ProvedElsewhere` | 1194 | 0 | 1 | Obstruction theory \cite{Kon03} |
| `prop:kontsevich-mzv` | `proposition` | `ProvedElsewhere` | 1483 | 0 | 1 | Configuration space periods and associator coefficients \cite{Kon03} |
| `prop:jacobi-nilpotent` | `proposition` | `ProvedHere` | 1897 | 1 | 0 | Cofree Jacobi coderivation square |
| `lem:dcrit-boundary-linear` | `lemma` | `ProvedHere` | 2289 | 1 | 0 | dCrit for boundary-linear $W$ |
| `thm:boundary-linear-lg` | `theorem` | `ProvedHere` | 2387 | 3 | 0 | Boundary-linear LG theorem |
| `prop:defq-data-firewall` | `proposition` | `ProvedHere` | 2745 | 2 | 0 | Classical, quantum, chiral, and centre data are distinct |
| `prop:defq-C1-existence` | `proposition` | `ProvedHere` | 2908 | 1 | 0 | C1 -- formal pole structure under the \(R\)-matrix hypothesis |
| `thm:defq-C2-CYBE` | `theorem` | `ProvedHere` | 2934 | 2 | 0 | Dynamical CYBE for \texorpdfstring{$r(u,Z)$}{r(u,Z)} -- chain-level |
| `thm:defq-C3-lie-bialgebra` | `theorem` | `ProvedHere` | 3006 | 2 | 0 | C3 -- Lie bialgebra |
| `thm:defq-kazhdan-classical-limit` | `theorem` | `ProvedHere` | 3061 | 3 | 0 | Formal classical-limit criterion, Vol~I form |
| `thm:defq-super-kontsevich-formality` | `theorem` | `ProvedElsewhere` | 3153 | 0 | 0 | Finite-truncation super-Kontsevich formality |
| `thm:defq-star-product-specialisation` | `theorem` | `ProvedHere` | 3210 | 2 | 0 | Root-of-unity specialization criterion |
| `thm:defq-unified-motivic-origin` | `theorem` | `ProvedElsewhere` | 3246 | 0 | 0 | Associator coefficients and MZV periods |
| `thm:defq-grt1-equivariance` | `theorem` | `ProvedElsewhere` | 3282 | 0 | 0 | $\mathrm{GRT}_1$-action on formality choices |

#### `chapters/examples/deformation_quantization_examples.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:coisson-coalgebra` | `theorem` | `ProvedElsewhere` | 105 | 0 | 1 | Coisson = \texorpdfstring{$(\chirPois)^c$}{(chirPois)c}-coalgebra; {} \cite{BD04} |
| `thm:pinf-formality` | `theorem` | `ProvedElsewhere` | 127 | 2 | 2 | Formality for \texorpdfstring{$\Pinf$}{P-infinity}-chiral; {} \cite{Kon03,FG12} |
| `thm:obstructions` | `theorem` | `ProvedElsewhere` | 189 | 1 | 1 | Obstruction classes; {} \cite{Kon03} |
| `thm:green-schwarz` | `theorem` | `ProvedElsewhere` | 221 | 0 | 1 | Green--Schwarz mechanism; {} \cite{Pol98} |
| `thm:mc-quantization` | `theorem` | `ProvedElsewhere` | 244 | 0 | 2 | MC elements and quantization; {} \cite{Kon03,KontsevichSoibelman} |
| `prop:lattice-one-step` | `proposition` | `ProvedHere` | 474 | 1 | 0 | Lattice deformation is one-step |
| `constr:superpotential-ainfty` | `construction` | `ProvedElsewhere` | 647 | 0 | 1 | Superpotential $A_\infty$ structure; {} \cite{DNP25} |
| `prop:chiral-dcrit` | `proposition` | `ProvedElsewhere` | 698 | 1 | 1 | Chiral enhancement of the derived critical locus; {} \cite{DNP25} |

#### `chapters/examples/exceptional_yangian_koszul_duality_platonic.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:finite-rtt-trace-pairing-nondegenerate` | `proposition` | `ProvedHere` | 128 | 0 | 0 | Trace duality for the coefficient space |
| `__unlabeled_chapters/examples/exceptional_yangian_koszul_duality_platonic.tex:170` | `lemma` | `ProvedHere` | 170 | 0 | 0 | Permutation-kernel benchmark |
| `prop:exceptional-yangian-type-separation` | `proposition` | `ProvedHere` | 191 | 0 | 0 | Objects entering the exceptional RTT problem |
| `prop:exceptional-yangian-template` | `proposition` | `ProvedHere` | 235 | 4 | 0 | Quadratic RTT duality criterion |
| `lem:exceptional-finite-window-promotion` | `lemma` | `ProvedHere` | 321 | 0 | 0 | Passage from finite windows to the completed algebra |
| `prop:exceptional-yangian-ordered-bar-averaging` | `proposition` | `ProvedHere` | 342 | 0 | 0 | Ordered bar information under averaging |
| `thm:exceptional-yangian-pbw-grw18` | `proposition` | `ProvedElsewhere` | 373 | 1 | 1 | Guay--Regelskis--Wendlandt |
| `rem:exceptional-yangian-three-table-quarantine` | `remark` | `ProvedHere` | 891 | 3 | 0 | Passage from root data to exceptional duality |

#### `chapters/examples/free_fields.tex` (49)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fermion-shadow-metric` | `proposition` | `ProvedHere` | 599 | 1 | 0 | Shadow metric of the free fermion |
| `prop:fermion-rmatrix` | `proposition` | `ProvedHere` | 735 | 0 | 0 | Free fermion $r$-matrix |
| `thm:fermion-sewing` | `theorem` | `ProvedHere` | 856 | 1 | 0 | Free fermion sewing |
| `prop:bc-general-spin-class-c` | `proposition` | `ProvedElsewhere` | 1125 | 1 | 0 | $bc$ ghost system at general spin: class~C for all $\lambda$ |
| `thm:single-fermion-boson-duality` | `theorem` | `ProvedHere` | 1174 | 0 | 0 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | `ProvedHere` | 1261 | 1 | 0 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | `ProvedHere` | 1330 | 1 | 0 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | `ProvedHere` | 1404 | 0 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-deformation-channels` | `proposition` | `ProvedHere` | 1534 | 1 | 0 | $\beta\gamma$ deformation complex |
| `comp:betagamma-shadow-weights` | `computation` | `ProvedHere` | 1721 | 2 | 0 | $\beta\gamma$ shadow obstruction tower: special weight table |
| `prop:betagamma-weight-symmetry` | `proposition` | `ProvedHere` | 1757 | 1 | 0 | Weight symmetry $\neq$ Koszul duality |
| `thm:heisenberg-bar` | `theorem` | `ProvedHere` | 1847 | 4 | 0 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | `ProvedHere` | 1873 | 0 | 0 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | `ProvedHere` | 1932 | 0 | 0 | Heisenberg curved cobar structure |
| `thm:lattice-voa-bar` | `theorem` | `ProvedHere` | 2004 | 0 | 0 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | `ProvedHere` | 2036 | 0 | 0 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | `ProvedHere` | 2071 | 0 | 0 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | `ProvedHere` | 2110 | 0 | 0 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | `ProvedHere` | 2175 | 0 | 0 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | `ProvedHere` | 2203 | 1 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `thm:heisenberg-koszul-dual-early` | `theorem` | `ProvedHere` | 2502 | 1 | 4 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | `ProvedHere` | 2544 | 1 | 0 | Heisenberg module-comodule equivalence |
| `lem:fock-module-simplicity` | `lemma` | `ProvedHere` | 2688 | 0 | 0 | Fock module simplicity |
| `prop:fock-bar-resolution` | `proposition` | `ProvedHere` | 2707 | 2 | 0 | Fock module bar resolution |
| `cor:fock-character-koszul` | `corollary` | `ProvedHere` | 2813 | 2 | 0 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | `ProvedHere` | 2855 | 1 | 0 | Ext groups between Fock modules |
| `thm:heisenberg-not-self-dual` | `theorem` | `ProvedHere` | 3389 | 1 | 1 | Heisenberg is not self-dual |
| `thm:rhagavendran-heisenberg` | `theorem` | `ProvedElsewhere` | 3510 | 0 | 1 | Heisenberg duality \cite{CG17} |
| `thm:heisenberg-genus-g` | `theorem` | `ProvedHere` | 3587 | 6 | 0 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | `ProvedHere` | 3901 | 0 | 0 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | `ProvedHere` | 4015 | 2 | 0 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | `ProvedHere` | 4300 | 4 | 0 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | `ProvedHere` | 4455 | 0 | 0 | Heisenberg geometric bar differential |
| `lem:bar-dims-partitions` | `lemma` | `ProvedHere` | 4510 | 2 | 0 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | `ProvedHere` | 4581 | 0 | 0 | Heisenberg level inversion: curved duality |
| `prop:spin-structure-count` | `proposition` | `ProvedElsewhere` | 4702 | 0 | 2 | Spin structure count |
| `thm:fermion-genus1-partition` | `theorem` | `ProvedHere` | 4756 | 2 | 0 | Free fermion genus-1 partition functions |
| `prop:ising-fermion` | `proposition` | `ProvedElsewhere` | 5104 | 0 | 1 | Ising $=$ free fermion |
| `prop:bosonization` | `proposition` | `ProvedElsewhere` | 5165 | 0 | 2 | Bosonization formula |
| `thm:virasoro-moduli` | `theorem` | `ProvedHere` | 5434 | 0 | 1 | Critical Virasoro descent at $c = 26$ |
| `prop:moduli-degeneration` | `proposition` | `ProvedHere` | 5543 | 0 | 0 | Boundary-residue differential on moduli forms |
| `thm:brst-cohomology` | `theorem` | `ProvedElsewhere` | 5619 | 0 | 1 | Critical bosonic BRST complex \cite{Pol98} |
| `thm:genus-g-chiral-homology` | `theorem` | `ProvedHere` | 5794 | 3 | 0 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:bar-string-integrand` | `theorem` | `ProvedHere` | 6070 | 1 | 0 | Bar classes on moduli and boundary factorization |
| `thm:modular-anomaly` | `theorem` | `ProvedElsewhere` | 6193 | 0 | 0 | Belavin--Knizhnik anomaly condition |
| `thm:w-classical-integrability` | `theorem` | `ProvedElsewhere` | 6480 | 0 | 1 | Classical \texorpdfstring{$\mathcal{W}$}{W}-algebra integrability |
| `thm:filtered-bar-complex` | `theorem` | `ProvedHere` | 6874 | 0 | 0 | Filtered bar complex |
| `thm:curved-koszul-duality` | `theorem` | `ProvedElsewhere` | 6905 | 0 | 1 | Curved Koszul duality \cite{Positselski11} |
| `prop:massive-chiral-contractible` | `proposition` | `ProvedElsewhere` | 6943 | 0 | 0 | Massive chirals have contractible bar complexes |

#### `chapters/examples/genus_expansions.tex` (18)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `__unlabeled_chapters/examples/genus_expansions.tex:294` | `corollary` | `ProvedHere` | 294 | 0 | 0 | Lattice-independence of genus expansion |
| `prop:sl2-complementarity-all-genera` | `proposition` | `ProvedHere` | 701 | 0 | 0 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:integrable-level-independence` | `proposition` | `ProvedElsewhere` | 802 | 3 | 0 | Level-independence at integrable levels |
| `prop:km-genus2-propagator` | `proposition` | `ProvedHere` | 919 | 4 | 1 | Non-abelian genus-2 propagator |
| `prop:w3-genus4-cross-channel` | `proposition` | `ProvedHere` | 1622 | 0 | 0 | Genus-4 cross-channel correction |
| `comp:w4-w5-grav-cross` | `computation` | `ProvedHere` | 1691 | 1 | 0 | Universal gravitational cross-channel: $\cW_4$ and $\cW_5$ specializations |
| `comp:w4-full-ope-examples` | `computation` | `ProvedHere` | 1768 | 2 | 1 | $\cW_4$ full-OPE cross-channel: the first irrational correction |
| `prop:genus-expansion-convergence` | `proposition` | `ProvedHere` | 1971 | 1 | 0 | Convergence of the scalar genus expansion |
| `prop:complementarity-genus-series` | `proposition` | `ProvedHere` | 2037 | 1 | 0 | Central charge genus series |
| `prop:bar-verlinde-asymptotics` | `proposition` | `ProvedHere` | 2193 | 1 | 1 | Scalar bar coefficient and Verlinde determinant curvature |
| `prop:vir-complementarity` | `proposition` | `ProvedHere` | 2426 | 0 | 0 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | `ProvedHere` | 2548 | 0 | 0 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `prop:bc-betagamma-complementarity` | `proposition` | `ProvedHere` | 2774 | 0 | 0 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:universal-fe-ratios` | `proposition` | `ProvedHere` | 3035 | 1 | 0 | Universal free-energy ratios |
| `def:free-chiral-boundary-character` | `definition` | `ProvedElsewhere` | 4189 | 0 | 1 | Free chiral boundary character |
| `prop:neumann-character` | `proposition` | `ProvedElsewhere` | 4204 | 0 | 1 | Neumann pure-gauge character |
| `prop:dirichlet-character-genus` | `proposition` | `ProvedElsewhere` | 4225 | 0 | 1 | Dirichlet character |
| `prop:multi-chiral-product-characters` | `proposition` | `ProvedElsewhere` | 4306 | 0 | 0 | Multi-chiral product formulas |

#### `chapters/examples/heisenberg_eisenstein.tex` (14)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:heisenberg-standard-family-ledger` | `proposition` | `ProvedHere` | 116 | 8 | 0 | Heisenberg ordered-bar and scalar computation ledger |
| `prop:heisenberg-gaussian-termination` | `proposition` | `ProvedHere` | 229 | 0 | 0 | Gaussian shadow termination for Heisenberg |
| `prop:heisenberg-r-matrix` | `proposition` | `ProvedHere` | 516 | 0 | 0 | Heisenberg $r$-matrix |
| `prop:eisenstein-modular` | `proposition` | `ProvedElsewhere` | 666 | 0 | 1 | Modular transformation laws \cite{Kac} |
| `thm:heisenberg-genus-zero` | `theorem` | `ProvedElsewhere` | 703 | 1 | 1 | Genus zero correlation functions \cite{FBZ04} |
| `thm:heisenberg-genus-one-complete` | `theorem` | `ProvedHere` | 735 | 0 | 0 | Genus-1 Heisenberg bar kernels |
| `thm:heisenberg-genus-two` | `theorem` | `ProvedHere` | 860 | 0 | 0 | Genus-2 Heisenberg kernel |
| `thm:heisenberg-all-genus` | `theorem` | `ProvedHere` | 1117 | 0 | 0 | Heisenberg at general genus |
| `prop:modular-weight-formula` | `proposition` | `ProvedElsewhere` | 1200 | 0 | 2 | Eisenstein normalization and scalar scope \cite{Igusa62,Klingen67} |
| `thm:eta-appearance` | `theorem` | `ProvedHere` | 1237 | 0 | 0 | Partition-function normalizations and determinant line |
| `prop:multi-boson-eisenstein` | `proposition` | `ProvedHere` | 1673 | 0 | 0 | Multi-boson elliptic coefficients |
| `thm:heisenberg-exact-linearity` | `theorem` | `ProvedHere` | 1982 | 1 | 0 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | `ProvedHere` | 2022 | 3 | 0 | Heisenberg shadow obstruction tower: finite termination at degree~$2$ |
| `prop:heisenberg-open-sector` | `proposition` | `ProvedHere` | 2499 | 0 | 1 | Completed Fock open sector for Heisenberg |

#### `chapters/examples/kac_moody.tex` (52)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:km-genus1-hessian` | `computation` | `ProvedHere` | 471 | 2 | 0 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `prop:affine-standard-family-ledger` | `proposition` | `ProvedHere` | 553 | 8 | 0 | Affine standard-family computation ledger |
| `thm:critical-level-structure` | `theorem` | `ProvedElsewhere` | 664 | 0 | 1 | Feigin--Frenkel center at critical level \cite{Feigin-Frenkel} |
| `thm:vertex-chiral-equivalence` | `theorem` | `ProvedElsewhere` | 774 | 0 | 2 | Equivalence of perspectives \cite{FBZ04, BD04} |
| `prop:km-critical-separation` | `proposition` | `ProvedHere` | 896 | 5 | 0 | Critical-level separation of affine invariants |
| `thm:geometric-ope-kac-moody` | `theorem` | `ProvedHere` | 998 | 2 | 0 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | `ProvedHere` | 1052 | 2 | 0 | Level-shifting duality, abstract form |
| `rem:km-central-charge-sum` | `remark` | `ProvedHere` | 1099 | 1 | 0 | Central charge sum |
| `thm:wakimoto-brst-full-nondegenerate` | `theorem` | `ProvedHere` | 1274 | 0 | 3 | Wakimoto BRST exactness on the generic nonresonant locus |
| `thm:sl2-critical` | `theorem` | `ProvedElsewhere` | 1622 | 0 | 1 | Critical level simplification for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} \cite{Feigin-Frenkel} |
| `thm:sl2-koszul-dual` | `theorem` | `ProvedHere` | 1645 | 1 | 0 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:w3-wakimoto-sl3` | `theorem` | `ProvedElsewhere` | 1844 | 0 | 1 | Wakimoto for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} \cite{Frenkel-Kac-Wakimoto92} |
| `thm:sl3-koszul-dual` | `theorem` | `ProvedHere` | 1863 | 2 | 0 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | `ProvedHere` | 1907 | 1 | 0 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | `ProvedHere` | 1946 | 3 | 0 | Curved level decomposition of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | `ProvedHere` | 2046 | 1 | 0 | Critical-level curved spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | `ProvedHere` | 2134 | 0 | 0 | Generic level-independence on the curvature-flat comparison surface |
| `thm:universal-kac-moody-koszul` | `theorem` | `ProvedHere` | 2274 | 1 | 0 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | `ProvedHere` | 2317 | 1 | 0 | Killing form via structure constants |
| `thm:principal-w-algebra-structure` | `theorem` | `ProvedElsewhere` | 3178 | 0 | 2 | Principal \texorpdfstring{$\mathcal{W}$}{W}-algebra structure \cite{FF, Ara07} |
| `thm:km-higher-genus-corrections` | `theorem` | `ProvedHere` | 3238 | 3 | 0 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | `ProvedHere` | 3323 | 1 | 0 | Closed-form current presentation in the Koszul dual |
| `thm:km-quantum-groups` | `theorem` | `ProvedHere` | 3736 | 2 | 1 | Quantum-group parameter inversion |
| `prop:spectral-flow-koszul` | `proposition` | `ProvedElsewhere` | 3947 | 0 | 1 | Spectral flow and Koszul duality \cite{Kac} |
| `thm:admissible-rep-theory` | `theorem` | `ProvedElsewhere` | 4126 | 1 | 2 | Representation theory at admissible level \cite{KW88, Arakawa17} |
| `prop:bar-admissible` | `proposition` | `ProvedHere` | 4152 | 4 | 0 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | `ProvedHere` | 4224 | 4 | 0 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-general-rank` | `theorem` | `ProvedElsewhere` | 4524 | 1 | 1 | Kac--Wakimoto character formula in general rank |
| `prop:ds-admissible` | `proposition` | `ProvedElsewhere` | 4861 | 2 | 1 | DS reduction at admissible level \cite{Arakawa17} |
| `prop:whittaker-ds` | `proposition` | `ProvedElsewhere` | 4942 | 0 | 3 | Whittaker modules and DS reduction \cite{Arakawa17} |
| `prop:bar-whittaker` | `proposition` | `ProvedHere` | 5000 | 1 | 1 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | `ProvedHere` | 5101 | 2 | 0 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-genus1-curvature` | `theorem` | `ProvedHere` | 5436 | 4 | 0 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:affine-cubic-normal-form` | `theorem` | `ProvedHere` | 6212 | 0 | 0 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | `ProvedHere` | 6248 | 2 | 0 | Affine shadow obstruction tower: finite termination at degree~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | `ProvedHere` | 6286 | 2 | 0 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | `ProvedHere` | 6329 | 1 | 0 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | `ProvedHere` | 6399 | 3 | 0 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | `ProvedHere` | 6447 | 5 | 0 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | `ProvedHere` | 6504 | 2 | 0 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | `ProvedHere` | 6581 | 5 | 0 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | `ProvedHere` | 6667 | 2 | 0 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | `ProvedHere` | 6703 | 1 | 0 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | `ProvedHere` | 6883 | 2 | 0 | Vanishing of the genus loop on the affine cubic |
| `prop:km-cubic-shadow-level-independence` | `proposition` | `ProvedHere` | 6949 | 1 | 0 | Level-independence of the cubic shadow product |
| `prop:nsl-shadow-tower` | `proposition` | `ProvedHere` | 7074 | 2 | 0 | Non-simply-laced shadow obstruction tower |
| `prop:complete-exceptional-shadow` | `proposition` | `ProvedHere` | 7255 | 2 | 0 | Complete exceptional shadow data |
| `prop:exceptional-anomaly-ratios` | `proposition` | `ProvedHere` | 7344 | 1 | 0 | Anomaly ratios for exceptional principal $\mathcal{W}$-algebras |
| `prop:affine-cs-action` | `proposition` | `ProvedElsewhere` | 7466 | 0 | 2 | The holomorphic-topological Chern--Simons action |
| `prop:level-rank-boundary-voa` | `proposition` | `ProvedElsewhere` | 7597 | 0 | 1 | Level-rank duality for boundary VOAs |
| `cor:level-rank-bar-intertwining` | `corollary` | `ProvedHere` | 7613 | 1 | 0 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | `ProvedHere` | 7642 | 0 | 0 | Kappa anti-symmetry under the critical-level reflection |

#### `chapters/examples/landscape_census.tex` (14)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:census-conductor-row-count` | `proposition` | `ProvedHere` | 1607 | 1 | 0 | Conductor-domain census count |
| `prop:fateev-lukyanov-canonical` | `proposition` | `ProvedHere` | 3751 | 0 | 1 | Fateev--Lukyanov central-charge formula; canonical form |
| `cor:subexp-free-field` | `corollary` | `ProvedHere` | 4592 | 1 | 0 | Sub-exponential growth in the computed rows |
| `cor:algebraicity-koszul` | `corollary` | `ProvedHere` | 4610 | 1 | 0 | Closed forms for computed interacting rows |
| `thm:ds-spectral-branch-preservation` | `theorem` | `ProvedHere` | 4804 | 0 | 0 | Divisor-core form of DS sub-discriminance |
| `prop:ds-invariant-discriminant` | `proposition` | `ProvedHere` | 4918 | 0 | 0 | A2 divisor-core calculation |
| `thm:discriminant-linear-dependence` | `theorem` | `ProvedHere` | 5527 | 2 | 0 | Linear dependence in the rank-one branch family |
| `lem:bar-deg2-symmetric-square` | `lemma` | `ProvedHere` | 5768 | 1 | 0 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | `ProvedHere` | 5819 | 0 | 0 | Exponential growth rate in a finite-character Kac--Moody chart |
| `thm:dominant-branch-point` | `theorem` | `ProvedHere` | 5843 | 1 | 0 | Dominant branch point in a finite-character Kac--Moody chart |
| `prop:canonical-prs-coefficient-cm214` | `proposition` | `ProvedElsewhere` | 6868 | 0 | 0 | Pope--Romans--Shen projector coefficient at $c=-214$ |
| `prop:canonical-monster-atlas-values` | `proposition` | `ProvedElsewhere` | 6907 | 0 | 0 | Monster ATLAS character values at reference conjugacy classes |
| `prop:canonical-oberdieck-phi01` | `proposition` | `ProvedElsewhere` | 7004 | 0 | 0 | Half K3 Jacobi coefficients and the doubled OP trace |
| `prop:canonical-bcov-quintic` | `proposition` | `ProvedElsewhere` | 7058 | 0 | 0 | BCOV genus-$1$ and genus-$2$ constant-map contributions on the quintic mirror |

#### `chapters/examples/lattice_foundations.tex` (39)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:analytic-theta-datum` | `definition` | `ProvedHere` | 108 | 2 | 0 | Analytic theta-datum |
| `thm:lattice-sewing` | `theorem` | `ProvedHere` | 137 | 4 | 0 | Lattice sewing envelope |
| `lem:lattice:cocycle-class` | `lemma` | `ProvedHere` | 444 | 0 | 0 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | `ProvedHere` | 608 | 2 | 0 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `prop:lattice-standard-cocycle-ledger` | `proposition` | `ProvedHere` | 650 | 4 | 0 | Lattice cocycle and ordered-bar ledger |
| `thm:lattice:frenkel-kac` | `theorem` | `ProvedElsewhere` | 746 | 1 | 3 | Frenkel--Kac--Segal; {} \cite{FK80,Se81} |
| `prop:lattice-k3-mukai-lane-separation` | `proposition` | `ProvedHere` | 912 | 0 | 0 | K3 Mukai lane separation |
| `thm:lattice:bar-structure` | `theorem` | `ProvedHere` | 1031 | 2 | 0 | Lattice bar complex structure |
| `comp:lattice:bar-A2` | `computation` | `ProvedHere` | 1097 | 0 | 0 | \texorpdfstring{$A_2$}{A_2} bar complex |
| `prop:lattice:bar-D4` | `proposition` | `ProvedHere` | 1128 | 0 | 0 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | `ProvedHere` | 1151 | 2 | 0 | \texorpdfstring{$E_8$}{E8} bar coalgebra and discriminant-trivial self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | `ProvedHere` | 1199 | 2 | 0 | Unimodular lattice bar-coalgebra self-duality |
| `thm:lattice:koszul-dual` | `theorem` | `ProvedHere` | 1262 | 0 | 0 | Dual coalgebra of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | `ProvedHere` | 1327 | 1 | 0 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | `ProvedHere` | 1584 | 0 | 0 | Tensor product from direct sum |
| `cor:lattice:kunneth` | `corollary` | `ProvedElsewhere` | 1609 | 2 | 1 | K\"unneth for bar complexes \cite{LV12} |
| `prop:lattice:sublattice` | `proposition` | `ProvedHere` | 1629 | 0 | 0 | Sublattice maps |
| `thm:lattice:overlattice` | `theorem` | `ProvedElsewhere` | 1683 | 0 | 1 | Overlattice vertex algebra \cite{FLM88} |
| `thm:lattice:hochschild` | `proposition` | `ProvedHere` | 1950 | 1 | 0 | Charge decomposition of the lattice cochain model |
| `prop:lattice:genus-1` | `proposition` | `ProvedHere` | 2074 | 0 | 0 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | `ProvedHere` | 2097 | 0 | 0 | Modular invariance |
| `prop:lattice:niemeier-theta-decomposition` | `proposition` | `ProvedHere` | 2236 | 0 | 0 | Niemeier theta series decomposition |
| `prop:lattice:self-dual-criterion` | `proposition` | `ProvedHere` | 2514 | 1 | 0 | Discriminant-trivial module-envelope criterion |
| `prop:lattice:D4-triality` | `proposition` | `ProvedHere` | 2541 | 2 | 0 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | `ProvedHere` | 2580 | 1 | 0 | Lattice twisted-sector charge inversion on the bar surface |
| `prop:lattice:deformation-properties` | `proposition` | `ProvedHere` | 2767 | 2 | 0 | Deformation properties |
| `comp:lattice:e1-bar-A2` | `computation` | `ProvedHere` | 2872 | 2 | 0 | \texorpdfstring{$\Eone$}{E1} bar complex for deformed \texorpdfstring{$A_2$}{A_2} |
| `prop:lattice:ordering-cycle-phase` | `proposition` | `ProvedHere` | 2953 | 1 | 0 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | `ProvedHere` | 3585 | 2 | 0 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | `ProvedHere` | 3662 | 3 | 0 | \texorpdfstring{$\Eone$}{E1} adjacent-root bar quotient |
| `prop:lattice:screening-structure` | `proposition` | `ProvedHere` | 3913 | 3 | 0 | Screening current structure |
| `prop:lattice:genus1-simple-pole` | `proposition` | `ProvedHere` | 5283 | 0 | 0 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | `ProvedHere` | 5300 | 2 | 0 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | `ProvedHere` | 5409 | 2 | 0 | Lattice shadow obstruction tower: termination at weight~$2$ |
| `thm:lattice:e1-hochschild` | `proposition` | `ProvedHere` | 5485 | 3 | 0 | $\Eone$ lattice charge-shift complex |
| `prop:xxx-shadow-data` | `proposition` | `ProvedHere` | 5649 | 2 | 0 | XXX shadow data |
| `prop:transfer-matrix-shadow-dict` | `proposition` | `ProvedHere` | 5688 | 0 | 0 | Transfer matrix--shadow dictionary |
| `prop:xxz-shadow-data` | `proposition` | `ProvedHere` | 5745 | 0 | 0 | XXZ shadow data |
| `prop:shadow-cardy-corrections` | `proposition` | `ProvedHere` | 5812 | 0 | 0 | Shadow hierarchy and Cardy corrections |

#### `chapters/examples/level1_bridge.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:level1-kappa-reduction` | `proposition` | `ProvedHere` | 232 | 2 | 0 | Level-$1$ $\kappa$ reduction |
| `prop:level1-cubic-vanishing` | `proposition` | `ProvedHere` | 328 | 1 | 0 | Cubic shadow vanishing at level~$1$ |
| `comp:level1-ade-bridge` | `computation` | `ProvedHere` | 448 | 1 | 0 | Level-$1$ bridge data for the simply-laced series |

#### `chapters/examples/logarithmic_w_algebras.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:wp-algebra` | `definition` | `ProvedElsewhere` | 95 | 0 | 2 | Triplet algebra |
| `prop:wp-kappa` | `proposition` | `ProvedHere` | 205 | 1 | 1 | Virasoro-line $\kappa$ for $\cW(p)$ |
| `prop:wp-c2-cofinite` | `proposition` | `ProvedElsewhere` | 297 | 0 | 1 | $C_2$-cofiniteness of $\cW(p)$ |
| `rem:wp-c2-vs-koszul` | `remark` | `ProvedHere` | 313 | 2 | 1 | $C_2$-cofiniteness vs rationality vs Koszulness |
| `prop:wp-not-free-strong` | `proposition` | `ProvedHere` | 358 | 1 | 0 | No finite free strong generation |
| `prop:wp-modules` | `proposition` | `ProvedElsewhere` | 531 | 0 | 2 | Module category of $\cW(p)$ |

#### `chapters/examples/minimal_model_examples.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:tricritical-s-matrix` | `proposition` | `ProvedElsewhere` | 258 | 0 | 1 | Tricritical Ising S-matrix \cite{BPZ84} |
| `prop:potts-quantum-dim` | `proposition` | `ProvedElsewhere` | 400 | 0 | 1 | Three-state Potts quantum dimensions \cite{Verlinde} |
| `thm:fusion-bar-torus` | `theorem` | `ProvedHere` | 432 | 2 | 0 | Fusion from bar complex on the torus |
| `thm:minimal-model-characters` | `theorem` | `ProvedElsewhere` | 492 | 0 | 1 | Virasoro minimal model characters \cite{FF84} |
| `prop:ising-koszul-dual` | `proposition` | `ProvedHere` | 670 | 0 | 0 | Koszul dual complementarity |
| `prop:ising-free-energies` | `proposition` | `ProvedHere` | 709 | 0 | 0 | Ising scalar free energies |

#### `chapters/examples/minimal_model_fusion.tex` (20)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:verlinde-general` | `theorem` | `ProvedElsewhere` | 67 | 0 | 1 | Verlinde formula, general form \cite{Verlinde} |
| `thm:wn-s-matrix` | `theorem` | `ProvedElsewhere` | 106 | 0 | 3 | \texorpdfstring{$W_N$}{W_N} modular S-matrix; {} \cite{Zhu96,Ara07} |
| `thm:w3-minimal-complete` | `theorem` | `ProvedHere` | 128 | 0 | 0 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | `ProvedHere` | 262 | 0 | 0 | Structure of Grothendieck ring |
| `thm:fusion-3-4-complete` | `theorem` | `ProvedElsewhere` | 303 | 0 | 1 | Virasoro fusion rules for \texorpdfstring{$\mathcal{M}(4,3)$}{M(4,3)} \cite{BPZ84} |
| `prop:quantum-dim-formula` | `proposition` | `ProvedElsewhere` | 337 | 0 | 1 | Quantum dimension formula \cite{Verlinde} |
| `thm:wn-verlinde` | `theorem` | `ProvedElsewhere` | 369 | 0 | 1 | \texorpdfstring{$W_N$}{W_N} Verlinde formula \cite{Verlinde} |
| `comp:m54-primaries` | `computation` | `ProvedHere` | 410 | 0 | 0 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | `ProvedHere` | 434 | 0 | 0 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | `ProvedHere` | 469 | 2 | 0 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | `ProvedHere` | 494 | 1 | 1 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | `ProvedHere` | 573 | 0 | 0 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | `ProvedHere` | 600 | 2 | 0 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | `ProvedHere` | 660 | 2 | 0 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | `ProvedHere` | 683 | 1 | 0 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | `ProvedHere` | 710 | 3 | 0 | Fusion ring as polynomial quotient |
| `prop:fusion-quantum-group` | `proposition` | `ProvedElsewhere` | 738 | 0 | 2 | Connection to quantum group \cite{KL93} |
| `thm:minimal-model-mtc` | `theorem` | `ProvedElsewhere` | 780 | 2 | 1 | Minimal models form modular tensor categories |
| `comp:twist-5-4` | `computation` | `ProvedHere` | 806 | 0 | 0 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `thm:mtc-tqft` | `theorem` | `ProvedElsewhere` | 831 | 0 | 1 | MTC determines a 3d TQFT \cite{RT91} |

#### `chapters/examples/n2_superconformal.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:n2-standard-family-ledger` | `proposition` | `ProvedElsewhere` | 99 | 1 | 0 | $\mathcal N=2$ standard-family ledger |
| `rem:n2-kazama-suzuki` | `remark` | `ProvedElsewhere` | 131 | 0 | 1 | Kazama--Suzuki coset |

#### `chapters/examples/shadow_tower_extended_families.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:canonical-two-point-norms` | `proposition` | `ProvedElsewhere` | 38 | 0 | 2 | Canonical two-point norms |
| `prop:fateev-lukyanov-alpha` | `proposition` | `ProvedElsewhere` | 67 | 0 | 1 | Zamolodchikov-normalized $WW$ OPE |
| `thm:bp-other-lines` | `theorem` | `ProvedElsewhere` | 181 | 0 | 0 | BP charged-line OPE packet |
| `cor:bp-feigin-frenkel-complementarity` | `corollary` | `ProvedHere` | 203 | 1 | 0 | BP reflected central sum |
| `thm:denominator-factorization-pattern` | `theorem` | `ProvedHere` | 277 | 1 | 0 | OPE denominator factorization |

#### `chapters/examples/symmetric_orbifolds.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:symn-averaging-kernel` | `proposition` | `ProvedHere` | 80 | 1 | 0 | Ordered data and symmetric shadow |
| `prop:symn-kappa` | `proposition` | `ProvedHere` | 196 | 0 | 0 | Identity-sector modular characteristic |
| `prop:symn-twist-vanishing` | `proposition` | `ProvedHere` | 290 | 1 | 0 | Twist weights and the identity vacuum |
| `prop:symn-shadow-depth` | `proposition` | `ProvedHere` | 439 | 0 | 0 | Diagonal shadow depth of the fixed-point sector |
| `thm:symn-dmvv-product` | `theorem` | `ProvedElsewhere` | 567 | 0 | 1 | DMVV product formula; {} \cite{DMVV97} |
| `prop:symn-cycle-index-plethystic` | `proposition` | `ProvedHere` | 588 | 2 | 1 | Cycle-index and plethystic normalization |
| `prop:symn-dmvv-kappa` | `proposition` | `ProvedHere` | 662 | 3 | 0 | DMVV does not compute ordered-bar $\kappa$ |
| `prop:symn-hecke-form` | `proposition` | `ProvedElsewhere` | 881 | 0 | 1 | DMVV Hecke-operator form; {} \cite{DMVV97} |
| `prop:symn-hecke-kappa` | `proposition` | `ProvedHere` | 951 | 2 | 0 | Hecke operators and the identity scalar |

#### `chapters/examples/w3_composite_fields.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | `ProvedElsewhere` | 64 | 1 | 2 | Level-four calculation and normalized $WW$ coupling |
| `thm:w-w-ope-complete` | `theorem` | `ProvedElsewhere` | 132 | 1 | 2 | Zamolodchikov $W$--$W$ OPE |
| `prop:w3-ope-mode-normalization` | `proposition` | `ProvedHere` | 165 | 1 | 0 | OPE-to-mode normalization |
| `cor:w3-mode-commutator` | `corollary` | `ProvedElsewhere` | 192 | 0 | 0 | Zamolodchikov mode algebra |
| `prop:lambda-zero-highest-weight` | `proposition` | `ProvedHere` | 211 | 3 | 0 | Action of $\Lambda_0$ |
| `thm:w3-kac-level1` | `theorem` | `ProvedHere` | 233 | 5 | 0 | Level-one Shapovalov matrix |

#### `chapters/examples/w3_holographic_datum.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:w3hol-conductor` | `theorem` | `ProvedHere` | 289 | 1 | 0 | Reflected principal central sum |
| `prop:w3hol-lambda-on-primaries` | `proposition` | `ProvedHere` | 364 | 0 | 0 | Action of \texorpdfstring{$\Lambda_0$}{Lambda0} on primaries |
| `cor:w3hol-lambda-roots` | `corollary` | `ProvedHere` | 396 | 0 | 0 | The conformal roots of \texorpdfstring{$\Lambda_0$}{Lambda0} |

#### `chapters/examples/w_algebras.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:arakawa-variety-intersection` | `theorem` | `ProvedElsewhere` | 63 | 0 | 2 | Associated varieties under DS reduction |
| `prop:w3-central-charge` | `proposition` | `ProvedHere` | 110 | 2 | 0 | $\mathcal W_3$ central charge |
| `thm:w-subregular-appell` | `theorem` | `ProvedHere` | 338 | 0 | 0 | Subregular Appell identity |
| `thm:w-pbw-slodowy-collapse` | `theorem` | `ProvedHere` | 386 | 0 | 0 | Filtered PBW bar-collapse criterion |
| `thm:w-bar-curvature` | `theorem` | `ProvedHere` | 488 | 0 | 0 | Bar differential and transferred curvature |
| `thm:feigin-frenkel-center` | `theorem` | `ProvedElsewhere` | 516 | 0 | 0 | Feigin--Frenkel centre |
| `thm:w-universal-gravitational-cubic` | `theorem` | `ProvedHere` | 534 | 0 | 0 | Primary-action cubic tensor |
| `prop:schwarzian-central-charge` | `proposition` | `ProvedElsewhere` | 896 | 0 | 0 | Schwarzian transformation law |

#### `chapters/examples/w_algebras_deep.tex` (12)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:wn-central-companion-deep` | `theorem` | `ProvedHere` | 124 | 1 | 1 | Fateev--Lukyanov central charge and reflected sum |
| `comp:miura-w3` | `computation` | `ProvedElsewhere` | 258 | 0 | 0 | Quantum Miura operator |
| `comp:w-infty-shadow-tower` | `computation` | `ProvedElsewhere` | 275 | 0 | 1 | Universal \(W_3\) OPE packet |
| `prop:gram-wt4` | `proposition` | `ProvedHere` | 307 | 0 | 0 | Weight-four Virasoro Gram matrix |
| `cor:lambda-qp` | `corollary` | `ProvedHere` | 341 | 0 | 0 | The weight-four quasi-primary |
| `prop:bp-ope-deep` | `proposition` | `ProvedElsewhere` | 389 | 0 | 0 | BP OPE normalization |
| `thm:bp-central-companion-deep` | `theorem` | `ProvedHere` | 411 | 0 | 0 | BP central companion |
| `comp:w3-arnold-deg3` | `computation` | `ProvedElsewhere` | 704 | 0 | 0 | Arnold relation |
| `prop:wn-character-primitive` | `proposition` | `ProvedHere` | 850 | 1 | 0 | Generic principal character |
| `comp:wn-stabilization-windows` | `computation` | `ProvedHere` | 866 | 0 | 0 | Coefficient stabilization |
| `prop:winfty-macmahon-deep` | `proposition` | `ProvedHere` | 877 | 0 | 0 | MacMahon factorization |
| `thm:walgdeep-divisor-rule` | `theorem` | `ProvedHere` | 1113 | 0 | 0 | Pure \(A\)-type rank arithmetic |

#### `chapters/examples/y_algebras.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:y-triality` | `remark` | `ProvedElsewhere` | 152 | 0 | 1 | $S_3$ triality |
| `comp:y-special-cases-c` | `computation` | `ProvedHere` | 264 | 2 | 0 | Special cases of the central charge |
| `thm:y111-central-charge` | `theorem` | `ProvedHere` | 302 | 1 | 0 | $c(Y_{1,1,1}) = 0$ |
| `thm:y-shadow-depth` | `theorem` | `ProvedHere` | 546 | 1 | 0 | Shadow depth of $Y$-algebras |
| `rem:y-algebra-depth-classification` | `remark` | `ProvedHere` | 602 | 0 | 0 | Depth classification mechanism for $Y$-algebras |
| `comp:y111-collision-residue` | `computation` | `ProvedHere` | 652 | 0 | 0 | {Collision residue for $Y_{1,1,1}[\Psi |
| `comp:y-wn-specialization` | `computation` | `ProvedHere` | 771 | 1 | 0 | $Y_{0,0,N} \simeq \cW_N \times \mathfrak{gl}(1)$ |
| `comp:y-affine-specialization` | `computation` | `ProvedHere` | 793 | 1 | 0 | $Y_{N,0,0} \simeq \widehat{\mathfrak{gl}}(N)$ |

#### `chapters/examples/yangians_computations.tex` (47)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bfn` | `theorem` | `ProvedElsewhere` | 37 | 0 | 1 | BFN construction |
| `prop:yangian-scalar-gauge-selfdual` | `proposition` | `ProvedHere` | 420 | 0 | 0 | Scalar-gauge inverse and sign reversal |
| `prop:yangian-rank-dependence` | `proposition` | `ProvedHere` | 615 | 0 | 0 | Finite-window rank dependence of the Yangian bar complex |
| `comp:sl3-yangian-from-ordered-bar` | `computation` | `ProvedHere` | 664 | 1 | 0 | The \texorpdfstring{$\mathfrak{sl}_3$}{sl3} KZ residue and fundamental Yang seed |
| `thm:quantum-rmatrix-shadow` | `theorem` | `ProvedHere` | 997 | 1 | 0 | Fundamental quantum \texorpdfstring{$R$}{R}-matrix and classical residue |
| `prop:colored-rmatrix` | `proposition` | `ProvedElsewhere` | 1071 | 2 | 0 | Colored $R$-matrices and Casimir eigenvalues |
| `prop:eval-module-bar` | `proposition` | `ProvedHere` | 1402 | 0 | 0 | Evaluation quotient bar complex |
| `prop:dk2-thick-generation-typeA` | `proposition` | `ProvedHere` | 1680 | 0 | 1 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `lem:composition-thick-generation` | `lemma` | `ProvedHere` | 1796 | 0 | 0 | Thick generation from finite composition series |
| `lem:monoidal-thick-extension` | `lemma` | `ProvedHere` | 2155 | 0 | 0 | Monoidal extension to thick closures |
| `lem:fd-thick-closure` | `lemma` | `ProvedHere` | 2349 | 0 | 0 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | `ProvedHere` | 2435 | 0 | 2 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | `ProvedHere` | 2686 | 1 | 0 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | `ProvedHere` | 2817 | 2 | 0 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | `ProvedHere` | 2975 | 0 | 0 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | `ProvedHere` | 2995 | 1 | 0 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | `ProvedHere` | 3020 | 1 | 0 | Sectorwise localizing generation |
| `prop:lqt-e1-subexponential-growth` | `proposition` | `ProvedHere` | 3092 | 0 | 0 | Sub-exponential growth of the \texorpdfstring{$E_1$}{E_1} page |
| `thm:baxter-exact-triangles-opoly` | `theorem` | `ProvedHere` | 3258 | 2 | 1 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `thm:baxter-exact-triangles` | `theorem` | `ProvedHere` | 3299 | 4 | 1 | Baxter exact triangles on shifted envelope \texorpdfstring{$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$}{Osh} |
| `prop:baxter-yangian-equivariance` | `proposition` | `ProvedHere` | 3370 | 0 | 0 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | `ProvedHere` | 3443 | 3 | 0 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `comp:thick-generation-sl2` | `computation` | `ProvedHere` | 3848 | 1 | 0 | Thick generation obstruction analysis for \texorpdfstring{$Y(\mathfrak{sl}_2)$}{Y(sl_2)} |
| `prop:prefundamental-clebsch-gordan` | `proposition` | `ProvedHere` | 3922 | 0 | 0 | Universal prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | `ProvedHere` | 3960 | 0 | 0 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | `ProvedHere` | 3973 | 2 | 0 | $K_0$ generation for all simple types |
| `prop:categorical-cg-typeA` | `proposition` | `ProvedHere` | 4022 | 2 | 2 | Categorical prefundamental CG decomposition, type~$A$ |
| `thm:mc3-arbitrary-type` | `theorem` | `ProvedHere` | 4521 | 1 | 6 | Categorical prefundamental CG decomposition, all types |
| `prop:e8-root-uniformity` | `proposition` | `ProvedHere` | 5035 | 0 | 0 | $E_8$ relevant-root uniformity |
| `prop:character-cg-all-types` | `proposition` | `ProvedHere` | 5045 | 0 | 0 | Character-level Clebsch--Gordan for all simple types |
| `prop:monopole-hilbert-decomp` | `proposition` | `ProvedElsewhere` | 5350 | 0 | 1 | Hilbert space decomposition |
| `prop:dirichlet-character` | `proposition` | `ProvedElsewhere` | 5370 | 0 | 1 | Dirichlet boundary character |
| `prop:gauge-koszul-dual-shifted-cotangent` | `proposition` | `ProvedElsewhere` | 5441 | 0 | 1 | Koszul dual of gauge boundary chiral algebra |
| `def:yangian-additive-spectral-kernel` | `definition` | `ProvedHere` | 5644 | 0 | 0 | Additive spectral kernel on the polynomial core |
| `thm:yangian-vector-seed-propagation` | `theorem` | `ProvedHere` | 5658 | 1 | 0 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | `ProvedHere` | 5688 | 0 | 0 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | `ProvedHere` | 5711 | 0 | 0 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | `ProvedHere` | 5726 | 0 | 0 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | `ProvedHere` | 5777 | 1 | 0 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | `ProvedHere` | 5802 | 0 | 0 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | `ProvedHere` | 5829 | 0 | 0 | Derived realization of the Baxter--Rees family |
| `def:yangian-exact-support-dg-lie` | `definition` | `ProvedHere` | 5874 | 0 | 0 | Exact-support deformation dg Lie algebra |
| `thm:yangian-H2-reduction` | `theorem` | `ProvedHere` | 5896 | 1 | 0 | $H^2$-reduction to the three-leg sector |
| `def:yangian-baxter-KS-class` | `definition` | `ProvedHere` | 5966 | 0 | 0 | Baxter--Kodaira--Spencer class |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | `ProvedHere` | 5982 | 0 | 0 | Concrete cocycle |
| `thm:u-zeta-8-PBW-wall-crossing` | `theorem` | `ProvedHere` | 6126 | 2 | 0 | Formal PBW increment past the De Concini--Kac wall $N = \ell/2 = 4$ |
| `rem:u-zeta-8-PBW-plateau` | `remark` | `ProvedHere` | 6162 | 0 | 0 | Plateau and the Lusztig Frobenius kernel |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (30)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:dk0-four-path` | `computation` | `ProvedHere` | 312 | 0 | 0 | Four-path Drinfeld--Kohno verification |
| `prop:finite-stage-tangent` | `proposition` | `ProvedHere` | 2067 | 0 | 1 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | `ProvedHere` | 2148 | 0 | 0 | Mittag-Leffler for finite RTT bar windows |
| `lem:yangian-fd-fundamental-generation` | `lemma` | `ProvedHere` | 3388 | 2 | 0 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | `ProvedHere` | 3418 | 1 | 2 | Finite-dimensional quantum-loop factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | `ProvedHere` | 3588 | 0 | 2 | Type-\texorpdfstring{$A$}{A} quantum-loop fundamental packet is generated by the vector evaluation line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | `ProvedHere` | 3716 | 0 | 2 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | `ProvedHere` | 3754 | 0 | 1 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-tower-mc4-criterion` | `proposition` | `ProvedHere` | 4812 | 4 | 0 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | `ProvedHere` | 4875 | 5 | 0 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | `ProvedHere` | 4910 | 0 | 0 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | `ProvedHere` | 4964 | 4 | 0 | Standard RTT tower satisfies the M-level MC4 package |
| `prop:free-propagator-matching` | `proposition` | `ProvedHere` | 6939 | 2 | 0 | Free/Heisenberg propagator matching |
| `prop:affine-propagator-matching` | `proposition` | `ProvedHere` | 6987 | 0 | 0 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `prop:rmatrix-pole-landscape` | `proposition` | `ProvedHere` | 7078 | 2 | 0 | The collision-residue $r$-matrix across the standard landscape |
| `prop:bosonic-parity-constraint` | `proposition` | `ProvedHere` | 7185 | 0 | 0 | Bosonic parity constraint on $r$-matrix poles |
| `prop:cybe-from-mc` | `proposition` | `ProvedHere` | 7228 | 3 | 0 | CYBE from bar-complex MC equation |
| `prop:rmatrix-from-bar-coproduct` | `proposition` | `ProvedHere` | 7340 | 6 | 1 | KZ-normalized quantum $R$-matrix from ordered bar transport |
| `thm:spectral-derived-additive-kz` | `theorem` | `ProvedHere` | 8512 | 0 | 0 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | `ProvedHere` | 8610 | 1 | 0 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | `ProvedHere` | 8656 | 0 | 0 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | `ProvedHere` | 8729 | 1 | 0 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | `ProvedHere` | 8812 | 0 | 0 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | `ProvedHere` | 8868 | 0 | 0 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | `ProvedHere` | 8910 | 1 | 0 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | `ProvedHere` | 8945 | 0 | 0 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | `ProvedHere` | 8999 | 0 | 0 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | `ProvedHere` | 9070 | 0 | 0 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | `ProvedHere` | 9094 | 0 | 0 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | `ProvedHere` | 9133 | 0 | 0 | Exact free transport |

#### `chapters/examples/yangians_foundations.tex` (47)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:super-berezinian-central-automorphism` | `proposition` | `ProvedElsewhere` | 104 | 1 | 3 | Nazarov centrality and super-trace complementarity |
| `prop:drinfeld-rtt-presentation-comparison` | `proposition` | `ProvedElsewhere` | 419 | 0 | 1 | Drinfeld--RTT presentation comparison map |
| `thm:yangian-e1` | `theorem` | `ProvedHere` | 747 | 3 | 0 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | `ProvedHere` | 886 | 3 | 0 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | `ProvedHere` | 936 | 2 | 0 | Finite-window Yangian inverse-kernel duality |
| `cor:sl3-finite-rtt-dual` | `corollary` | `ProvedHere` | 1048 | 2 | 0 | \texorpdfstring{$Y_\hbar(\mathfrak{sl}_3)$}{Yh(sl3)} finite-window RTT dual |
| `cor:yangian-classical-self-dual` | `corollary` | `ProvedHere` | 1101 | 0 | 0 | RTT associated-graded classical limit |
| `prop:yangian-completed-bar-finite-pieces` | `proposition` | `ProvedHere` | 1932 | 0 | 0 | Finite-window bar conilpotence for Yangian completions |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | `ProvedHere` | 2161 | 3 | 0 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | `ProvedHere` | 2316 | 0 | 0 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | `ProvedHere` | 2420 | 1 | 0 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | `ProvedHere` | 2438 | 0 | 0 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | `ProvedHere` | 2468 | 0 | 0 | Explicit coefficient formula for the fundamental monodromy series |
| `prop:dg-shifted-rtt-boundary-support-bound` | `proposition` | `ProvedHere` | 2530 | 3 | 0 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | `ProvedHere` | 2594 | 3 | 0 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | `ProvedHere` | 2680 | 2 | 0 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | `ProvedHere` | 2777 | 2 | 0 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | `ProvedHere` | 2847 | 1 | 0 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | `ProvedHere` | 2916 | 1 | 0 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | `ProvedHere` | 2953 | 1 | 0 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | `ProvedHere` | 3009 | 1 | 0 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | `ProvedHere` | 3069 | 2 | 0 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | `ProvedHere` | 3130 | 7 | 0 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | `ProvedHere` | 3229 | 2 | 0 | Standard type-A fundamental line operator has the standard local residue |
| `prop:gauge-theory-koszul-dual` | `proposition` | `ProvedElsewhere` | 3505 | 0 | 0 | Gauge theory $\cA^!$ as shifted cotangent loop algebra |
| `thm:gauge-theory-yangian-structure` | `theorem` | `ProvedElsewhere` | 3544 | 0 | 1 | Full dg-shifted Yangian structure on $\cA^!$ |
| `def:three-layers-ordered-theory` | `definition` | `ProvedHere` | 3616 | 1 | 0 | Three layers of the ordered theory |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | `ProvedHere` | 3658 | 0 | 0 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | `ProvedHere` | 3685 | 1 | 0 | Stabilized completed bar/cobar recovery |
| `thm:shifted-rtt-mc-descent` | `theorem` | `ProvedHere` | 3746 | 0 | 0 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | `ProvedHere` | 3835 | 0 | 0 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | `ProvedHere` | 3880 | 0 | 0 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | `ProvedHere` | 3928 | 0 | 0 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | `ProvedHere` | 3944 | 1 | 0 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | `ProvedHere` | 3975 | 0 | 0 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | `ProvedHere` | 4008 | 0 | 0 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | `ProvedHere` | 4045 | 0 | 0 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | `ProvedHere` | 4070 | 0 | 0 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | `ProvedHere` | 4142 | 1 | 0 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | `ProvedHere` | 4191 | 0 | 0 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | `ProvedHere` | 4217 | 0 | 0 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | `ProvedHere` | 4244 | 0 | 0 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | `ProvedHere` | 4266 | 0 | 0 | Kleinian associated graded at the nilpotent point |
| `thm:kzb-as-bar-cobar-alpha` | `theorem` | `ProvedElsewhere` | 4404 | 0 | 0 | KZB as elliptic bar--cobar twisting at leading $\alpha$ |
| `prop:elliptic-coproduct-coassoc-fay` | `proposition` | `ProvedHere` | 4437 | 0 | 0 | Elliptic coproduct is Fay-coassociative |
| `thm:felder-R-half-braiding` | `theorem` | `ProvedHere` | 4464 | 0 | 0 | Felder $R$-matrix as half-braiding |
| `prop:sl2-elliptic-yangian-triangle` | `proposition` | `ProvedHere` | 4483 | 0 | 0 | $\slnn{2}$ elliptic triangle coherence at order $\hbar$ |

### Part III: Connections (297)

#### `chapters/connections/arithmetic_shadows.tex` (122)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:shadow-spectral-correspondence` | `theorem` | `ProvedHere` | 194 | 0 | 0 | Shadow--spectral correspondence |
| `prop:divisor-sum-decomposition` | `proposition` | `ProvedHere` | 323 | 0 | 0 | Divisor-sum decomposition |
| `cor:sewing-euler-product` | `corollary` | `ProvedElsewhere` | 348 | 1 | 0 | Euler product of the sewing determinant |
| `prop:sewing-trace-formula` | `proposition` | `ProvedHere` | 361 | 1 | 0 | Sewing trace formula |
| `thm:sewing-selberg-formula` | `theorem` | `ProvedHere` | 399 | 2 | 0 | Regularized sewing--Selberg formula |
| `thm:narain-universality` | `theorem` | `ProvedHere` | 460 | 1 | 0 | Pure-sector rank-one Narain identity |
| `thm:e8-epstein` | `theorem` | `ProvedHere` | 495 | 0 | 0 | $E_8$ Epstein factorization |
| `__unlabeled_chapters/connections/arithmetic_shadows.tex:516` | `remark` | `ProvedHere` | 516 | 1 | 0 | Zero-location input for the $E_8$ factors |
| `prop:z2-epstein` | `proposition` | `ProvedHere` | 527 | 0 | 0 | $\bZ^2$ Epstein zeta |
| `prop:leech-epstein` | `proposition` | `ProvedHere` | 551 | 1 | 0 | Leech Epstein constituent factorization |
| `__unlabeled_chapters/connections/arithmetic_shadows.tex:601` | `remark` | `ProvedHere` | 601 | 1 | 0 | Functional-equation centres of constituents |
| `prop:niemeier-multichannel` | `proposition` | `ProvedHere` | 821 | 1 | 0 | Multi-channel Niemeier discrimination |
| `prop:shadow-arithmetic-factorization` | `proposition` | `ProvedHere` | 908 | 0 | 0 | Shadow--arithmetic factorization |
| `prop:leading-hecke-identification` | `proposition` | `ProvedElsewhere` | 1215 | 1 | 0 | Leading-order Hecke identification |
| `prop:hecke-all-orders` | `proposition` | `ProvedHere` | 1242 | 0 | 0 | Hecke-span stability criterion |
| `prop:period-shadow-dictionary` | `proposition` | `ProvedHere` | 1295 | 3 | 0 | Period--shadow dictionary under Hecke-span stability |
| `comp:period-shadow-vz` | `computation` | `ProvedHere` | 1381 | 0 | 0 | $V_{\bZ}$: the Gaussian archetype |
| `comp:period-shadow-ve8` | `computation` | `ProvedHere` | 1400 | 1 | 0 | $V_{E_8}$: the Lie/tree archetype |
| `comp:period-shadow-leech` | `computation` | `ProvedHere` | 1422 | 1 | 0 | $V_{\mathrm{Leech}}$: the Ramanujan archetype |
| `comp:period-shadow-rank24-comparison` | `computation` | `ProvedHere` | 1475 | 0 | 0 | $D_{16}^+ \oplus D_{16}^+$ vs.\ $E_8^3$: same depth, different coefficient |
| `comp:period-shadow-rank2` | `computation` | `ProvedHere` | 1494 | 1 | 0 | $V_{\bZ^2}$ and $V_{A_2}$: Dedekind zeta at depth~$2$ |
| `thm:spectral-decomposition-principle` | `theorem` | `ProvedHere` | 1520 | 3 | 0 | Spectral decomposition under Hecke-span stability |
| `prop:growth-rate-dictionary` | `proposition` | `ProvedHere` | 1609 | 0 | 0 | Growth-rate dictionary |
| `thm:bg-vir-coincidence` | `theorem` | `ProvedElsewhere` | 1635 | 0 | 0 | $\beta\gamma$--Virasoro rate coincidence |
| `prop:self-referentiality-criterion` | `proposition` | `ProvedHere` | 1653 | 2 | 0 | Self-referentiality criterion |
| `cor:conformal-vector-infinite-depth` | `corollary` | `ProvedHere` | 1729 | 1 | 0 | Primitive conformal vector and infinite shadow depth |
| `thm:shadow-tower-asymptotics` | `theorem` | `ProvedHere` | 1759 | 0 | 0 | Shadow obstruction tower leading asymptotics |
| `cor:rigorous-infinite-depth` | `corollary` | `ProvedHere` | 1791 | 2 | 0 | Rigorous Virasoro infinite shadow depth |
| `__unlabeled_chapters/connections/arithmetic_shadows.tex:1814` | `remark` | `ProvedHere` | 1814 | 0 | 0 | Depth decomposition |
| `prop:bg-primary-counting` | `proposition` | `ProvedElsewhere` | 1838 | 0 | 0 | $\beta\gamma$ primary-counting function |
| `thm:refined-shadow-spectral` | `theorem` | `ProvedHere` | 1851 | 0 | 0 | Refined shadow--spectral correspondence |
| `prop:ising-d-arith` | `proposition` | `ProvedHere` | 1881 | 0 | 0 | Ising model: $d_{\mathrm{arith}} = 0$ |
| `rem:ising-arithmetic-paradox` | `remark` | `ProvedHere` | 1911 | 1 | 0 | The Ising arithmetic paradox |
| `rem:non-unimodular` | `remark` | `ProvedHere` | 1979 | 0 | 0 | Non-unimodular lattices |
| `rem:vnatural-class-m` | `remark` | `ProvedHere` | 2196 | 1 | 0 | The moonshine module: same $\kappa$, self-loop test |
| `thm:interacting-gram-positivity` | `theorem` | `ProvedHere` | 2288 | 1 | 0 | Interacting Gram positivity criterion |
| `cor:virasoro-interacting-gram` | `corollary` | `ProvedHere` | 2336 | 1 | 0 | — |
| `thm:shadow-resonance-locus` | `theorem` | `ProvedHere` | 2351 | 1 | 0 | Sign defect and resonance are distinct |
| `thm:shadow-spectral-measure` | `theorem` | `ProvedHere` | 2406 | 2 | 0 | Shadow spectral measure |
| `prop:carleman-virasoro` | `proposition` | `ProvedHere` | 2512 | 1 | 0 | Carleman rigidity |
| `prop:shadow-periods` | `proposition` | `ProvedHere` | 2562 | 1 | 0 | Shadow amplitudes are periods |
| `prop:universal-stokes-constants` | `proposition` | `ProvedHere` | 2845 | 0 | 0 | Universal Stokes constants |
| `prop:gevrey-zero-degree` | `proposition` | `ProvedHere` | 2878 | 0 | 0 | Weighted Riccati degree growth |
| `prop:padic-convergence` | `proposition` | `ProvedHere` | 2942 | 0 | 0 | $p$-adic convergence radius |
| `rem:kummer-kubota-leopoldt` | `remark` | `ProvedHere` | 2968 | 0 | 0 | Kummer congruences and the Kubota--Leopoldt $p$-adic $L$-function |
| `thm:shadow-mzv-dictionary` | `theorem` | `ProvedHere` | 3073 | 1 | 1 | Shadow--MZV period dictionary |
| `thm:partition-modular-classification` | `theorem` | `ProvedHere` | 3343 | 1 | 0 | Benchmark partition-function modular classes |
| `prop:quasi-modular-propagator` | `proposition` | `ProvedHere` | 3422 | 1 | 0 | Quasi-modular content from the genus-$1$ propagator |
| `prop:hecke-eigenvalue-extraction` | `proposition` | `ProvedHere` | 3497 | 1 | 0 | Hecke eigenvalues from partition data |
| `prop:tau-large-primes` | `proposition` | `ProvedHere` | 3536 | 1 | 0 | Ramanujan $\tau(p)$ at primes $83 \leq p \leq 113$ |
| `prop:tau-primes-211-229` | `proposition` | `ProvedHere` | 3603 | 0 | 0 | Ramanujan $\tau(p)$ at primes $p\in\{211,223,227,229\}$ |
| `prop:moment-matrix-negativity` | `proposition` | `ProvedHere` | 3720 | 0 | 0 | Eisenstein moment minor |
| `thm:shadow-eisenstein` | `theorem` | `ProvedElsewhere` | 3888 | 0 | 0 | The genus-$1$ amplitude Mellin transform is Eisenstein |
| `rem:shadow-eisenstein-numerical-check` | `remark` | `ProvedHere` | 4101 | 3 | 0 | The value at $s = 0$ separates the two Dirichlet series |
| `thm:shadow-bps` | `theorem` | `ProvedHere` | 5069 | 2 | 0 | Leading plethystic shadow of the Virasoro obstruction tower |
| `cor:shadow-fredholm` | `corollary` | `ProvedElsewhere` | 5337 | 0 | 0 | Shadow Fredholm determinant |
| `prop:mc-bracket-determines-atoms` | `proposition` | `ProvedHere` | 5587 | 2 | 0 | MC bracket in a two-atom spectral ansatz |
| `rem:mc-ramanujan-bridge` | `remark` | `ProvedHere` | 5641 | 2 | 0 | The bridge to the Ramanujan bound |
| `prop:koszul-field-criterion` | `proposition` | `ProvedHere` | 5872 | 2 | 0 | Koszul field-preservation criterion |
| `prop:heisenberg-koszul-epstein` | `proposition` | `ProvedHere` | 6113 | 1 | 0 | Degenerate case: Heisenberg |
| `comp:virasoro-c1-koszul-epstein` | `computation` | `ProvedHere` | 6166 | 0 | 0 | Virasoro at $c = 1$: numerical Koszul--Epstein value |
| `comp:fe-minimal-models` | `computation` | `ProvedHere` | 6191 | 1 | 0 | Functional equation for all unitary minimal models |
| `thm:spectral-continuation-bridge` | `theorem` | `ProvedHere` | 6272 | 3 | 0 | Hecke-equivariant MC element under finite-span stability |
| `thm:schur-complement-quartic` | `theorem` | `ProvedHere` | 6518 | 1 | 0 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | `ProvedHere` | 6577 | 0 | 0 | — |
| `prop:on-off-line-distinction` | `proposition` | `ProvedHere` | 6654 | 1 | 0 | — |
| `prop:li-criterion-failure` | `proposition` | `ProvedHere` | 7064 | 2 | 1 | Structural failure of the Li criterion for the sewing lift |
| `prop:pure-spin-s-schur` | `proposition` | `ProvedHere` | 7210 | 1 | 0 | — |
| `prop:prime-side-defect-formula` | `proposition` | `ProvedHere` | 7318 | 1 | 0 | — |
| `thm:finite-miura-defect` | `theorem` | `ProvedHere` | 7388 | 2 | 0 | Finite Miura defect at genus one |
| `prop:bracket-hodge-index` | `proposition` | `ProvedHere` | 8003 | 0 | 0 | Bracket positivity and the Hodge index |
| `prop:lattice-ramanujan` | `proposition` | `ProvedHere` | 8129 | 0 | 1 | Ramanujan bound for lattice spectral measures |
| `prop:shadow-symmetric-power` | `proposition` | `ProvedHere` | 8171 | 0 | 0 | Prime-local shadow--symmetric power criterion |
| `rem:serre-reduction` | `remark` | `ProvedElsewhere` | 8220 | 1 | 5 | The Serre--Langlands reduction |
| `thm:petersson-identification` | `theorem` | `ProvedHere` | 8353 | 1 | 0 | Petersson identification under finite Hecke span |
| `prop:rigidity-threshold` | `proposition` | `ProvedHere` | 8479 | 1 | 0 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | `ProvedHere` | 8579 | 2 | 1 | Lattice Ramanujan from rigidity hypotheses |
| `prop:stieltjes-signed-universal` | `proposition` | `ProvedHere` | 8781 | 1 | 0 | Weighted Virasoro signed Stieltjes obstruction |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | `ProvedHere` | 8820 | 0 | 0 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | `ProvedHere` | 8883 | 3 | 0 | Shadow arithmetic trichotomy |
| `prop:genus1-weight-bound` | `proposition` | `ProvedHere` | 8957 | 0 | 0 | Weight bound for genus-$1$ shadow projections |
| `rem:quasimodular-obstruction` | `remark` | `ProvedHere` | 8980 | 3 | 1 | Quasi-modular obstruction to naive multiplicativity |
| `thm:mc-recursion-moment` | `theorem` | `ProvedHere` | 9108 | 0 | 0 | MC recursion on moment $L$-functions |
| `thm:hecke-newton-lattice` | `theorem` | `ProvedHere` | 9253 | 5 | 0 | Hecke--Newton closure for lattice VOAs under finite Hecke span |
| `thm:non-lattice-ramanujan` | `theorem` | `ProvedHere` | 9355 | 0 | 1 | Non-lattice Ramanujan implication |
| `prop:mc-constraint-counting` | `proposition` | `ProvedHere` | 9870 | 2 | 0 | MC constraint counting |
| `thm:hecke-verdier-commutation` | `theorem` | `ProvedHere` | 10109 | 0 | 0 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | `ProvedHere` | 10148 | 4 | 0 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | `ProvedHere` | 10222 | 0 | 1 | Theta decomposition bridge |
| `rem:davenport-heilbronn-koszul` | `remark` | `ProvedElsewhere` | 10345 | 0 | 0 | Class-group obstruction and on-line zeros |
| `prop:sewing-spectral-bridge` | `proposition` | `ProvedHere` | 10408 | 3 | 1 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | `ProvedHere` | 10514 | 1 | 0 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | `ProvedHere` | 10561 | 0 | 0 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | `ProvedHere` | 10652 | 2 | 2 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | `ProvedHere` | 10828 | 1 | 0 | Genus-one saddle triviality |
| `cor:first-scattering-pole` | `corollary` | `ProvedHere` | 11025 | 1 | 0 | Regularized nonvanishing at the first scattering pole |
| `thm:scattering-coupling-factorization` | `theorem` | `ProvedHere` | 11126 | 5 | 0 | Scattering coupling factorization |
| `prop:hecke-defect-lattice` | `proposition` | `ProvedHere` | 11391 | 1 | 0 | Vanishing of the Hecke defect under finite Hecke span |
| `thm:packet-connection-flatness` | `theorem` | `ProvedHere` | 11898 | 0 | 0 | Flatness and divisor independence |
| `cor:lattice-packet-diagonal` | `corollary` | `ProvedHere` | 11965 | 1 | 0 | Lattice transparency |
| `prop:gauge-criterion-scattering` | `proposition` | `ProvedHere` | 12032 | 0 | 0 | Gauge criterion for scattering access |
| `rem:arithmetic-comparison-sharpening` | `remark` | `ProvedHere` | 12142 | 0 | 0 | Sharpening of the arithmetic comparison conjecture |
| `prop:miura-packet-splitting` | `proposition` | `ProvedHere` | 12216 | 5 | 0 | — |
| `prop:genus2-non-diagonal` | `proposition` | `ProvedHere` | 12582 | 0 | 0 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | `ProvedHere` | 12626 | 1 | 0 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | `ProvedHere` | 12826 | 0 | 1 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | `ProvedHere` | 12858 | 2 | 2 | B\"ocherer bridge under three-shell reconstruction |
| `rem:genus2-definitive-scope` | `remark` | `ProvedHere` | 12992 | 2 | 0 | Definitive scope of genus-$2$ arithmetic access |
| `rem:leech-weight12-sk` | `remark` | `ProvedHere` | 13048 | 0 | 3 | Leech weight-$12$ cusp line is Saito--Kurokawa |
| `thm:leech-chi12-projection` | `theorem` | `ProvedHere` | 13072 | 2 | 2 | Leech $\chi_{12}$-projection and Waldspurger consequence under three-shell reconstruction |
| `thm:prime-locality-obstructions` | `theorem` | `ProvedHere` | 13405 | 4 | 0 | Precise obstructions to prime-locality |
| `thm:riccati-determinacy` | `theorem` | `ProvedHere` | 13609 | 0 | 0 | Weighted Riccati determinacy |
| `prop:shadow-not-selberg` | `proposition` | `ProvedHere` | 13656 | 1 | 0 | The genus-$1$ amplitude series is not in the Selberg class |
| `thm:fricke-ldp-sub-leading` | `theorem` | `ProvedHere` | 14274 | 1 | 0 | Fricke LDP sub-leading correction at each node |
| `thm:shimura-waldspurger-higher-weights` | `theorem` | `ProvedElsewhere` | 14372 | 1 | 1 | Shimura--Waldspurger constants are period ratios |
| `thm:YD-delta-7-8-9` | `theorem` | `ProvedHere` | 14436 | 2 | 0 | $\delta^{(n)}$ for $n \in \{7, 8, 9, 10, 11, 12\}$ |
| `thm:humbert-heegner-filter-g-geq-3` | `proposition` | `ProvedHere` | 14763 | 1 | 0 | Humbert--Heegner filter beyond genus $2$: proved boundary |
| `thm:mu-32-refinement` | `theorem` | `ProvedHere` | 14934 | 1 | 0 | $\mu_{16}\to\mu_{32}$ gerbe refinement is not a consequence of the Bruinier lcm datum near the quadruple Humbert wall |
| `thm:as-monster-k3-cplus-product-invariant` | `theorem` | `ProvedHere` | 15154 | 2 | 1 | Monster--K$3$ $c_+$-product comparison |
| `cor:as-monster-196884-as-cplus-weighted` | `remark` | `ProvedHere` | 15253 | 1 | 1 | Monster $196884$ is not a $c_+$-weighted K$3$ elliptic-genus coefficient |
| `thm:YD-delta-13-16` | `theorem` | `ProvedHere` | 15592 | 2 | 0 | $\delta^{(n)}$ for $n \in \{13, 14, 15, 16\}$ |
| `thm:n-2-root-unity-vol-I-face` | `theorem` | `ProvedHere` | 15847 | 0 | 0 | $N = 2$ root-of-unity: $324$ is not a PBW dimension |

#### `chapters/connections/bv_brst.tex` (12)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bv-bar-geometric` | `theorem` | `ProvedElsewhere` | 340 | 3 | 1 | Genus-$0$ BV complex and geometric bar complex; {} \cite{CG17} |
| `thm:brst-physical-states` | `theorem` | `ProvedElsewhere` | 641 | 0 | 2 | BRST cohomology on a nilpotent gauge-fixed complex; {} \cite{CG17,Polchinski1998} |
| `thm:log-form-ghost-law` | `theorem` | `ProvedHere` | 677 | 1 | 0 | Coordinate cocycle for collision logarithmic forms |
| `lem:brst-nilpotence` | `lemma` | `ProvedElsewhere` | 777 | 0 | 1 | BRST nilpotence; {} \cite{FGZ86} |
| `rem:ghost-superghost-koszul` | `remark` | `ProvedElsewhere` | 1190 | 0 | 2 | The ghost--superghost Koszul involution |
| `prop:chain-level-three-obstructions` | `proposition` | `ProvedHere` | 2056 | 0 | 1 | Three chain-level obstructions and harmonic factorization |
| `comp:v1-burns-koszul-datum` | `computation` | `ProvedElsewhere` | 2873 | 0 | 0 | Burns space Koszul datum |
| `rem:non-cy-scope` | `remark` | `ProvedElsewhere` | 2991 | 1 | 0 | Scope and status |
| `rem:bvbrst-6d-hcs-quartic` | `remark` | `ProvedElsewhere` | 3161 | 0 | 2 | Holomorphic Chern--Simons and the five-dimensional $\Omega$-background |
| `prop:bvbrst-cech-cocycle` | `proposition` | `ProvedHere` | 3334 | 0 | 0 | Kummer cocycle for an eighth root |
| `thm:bvbrst-heegner-all-order` | `theorem` | `ProvedElsewhere` | 3421 | 0 | 1 | Gritsenko--Nikulin product for \texorpdfstring{$\Delta _5$}{Delta 5} |
| `thm:bvbrst-allloop-resummation` | `theorem` | `ProvedHere` | 3827 | 3 | 0 | Fourier resummation of the Igusa product |

#### `chapters/connections/concordance.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:finite-jet-rigidity` | `proposition` | `ProvedHere` | 1077 | 1 | 0 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | `ProvedHere` | 1101 | 1 | 0 | Polynomial level dependence |
| `prop:vol2-relative-holographic-bridge` | `proposition` | `ProvedElsewhere` | 5366 | 1 | 0 | Relative holographic deformation bridge |
| `prop:vol2-ribbon-thooft-bridge` | `proposition` | `ProvedElsewhere` | 5387 | 3 | 0 | Ribbon/'t~Hooft bridge |
| `comp:spectral-discriminants-standard` | `computation` | `ProvedHere` | 6885 | 0 | 0 | Spectral discriminants of standard families |
| `rem:concord-retraction` | `remark` | `ProvedElsewhere` | 13173 | 0 | 0 | Central charges for $\mathcal T[A_1, \Sigma_{0,24} |

#### `chapters/connections/editorial_constitution.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:master-pbw` | `theorem` | `ProvedElsewhere` | 203 | 4 | 0 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `prop:vassiliev-genus0` | `proposition` | `ProvedHere` | 1852 | 1 | 1 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |

#### `chapters/connections/entanglement_modular_koszul.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:ent-twist-dimension` | `lemma` | `ProvedElsewhere` | 180 | 1 | 1 | Twist operator dimension |
| `thm:ent-scalar-entropy` | `theorem` | `ProvedHere` | 206 | 6 | 0 | Entanglement entropy at the scalar level |
| `rem:ent-negative` | `remark` | `ProvedHere` | 1675 | 2 | 0 | Negative formal coefficient at $c_{\mathrm{eff}} = -166$ |
| `prop:ent-real-root` | `proposition` | `ProvedHere` | 1707 | 3 | 0 | Real-root unitary submodule entanglement |
| `prop:ent-kl-scope` | `proposition` | `ProvedHere` | 2079 | 0 | 2 | Knill--Laflamme scope for finite-stage topological entanglement |

#### `chapters/connections/feynman_connection.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:loop-genus-correspondence` | `theorem` | `ProvedElsewhere` | 139 | 0 | 1 | Loop-genus correspondence; {} \cite{costello-renormalization} |
| `thm:swiss-cheese-chiral-DT-feynman` | `theorem` | `ProvedElsewhere` | 391 | 1 | 2 | Swiss-cheese / chiral Deligne--Tamarkin |

#### `chapters/connections/feynman_diagrams.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | `ProvedHere` | 275 | 0 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `thm:kontsevich-formality-feynman` | `theorem` | `ProvedElsewhere` | 372 | 1 | 1 | Kontsevich formality |
| `prop:compactified-ternary-two-channel` | `proposition` | `ProvedHere` | 524 | 1 | 0 | Two-channel reduction for a compactified logarithmic ternary packet |
| `prop:m04-standard-log-basis` | `proposition` | `ProvedHere` | 621 | 0 | 0 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `thm:loop-genus-formula` | `theorem` | `ProvedElsewhere` | 793 | 0 | 1 | Graph loop number and ribbon genus; {} \cite{costello-renormalization} |
| `thm:mk-tree-level` | `theorem` | `ProvedElsewhere` | 1054 | 1 | 0 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure-vol1` | `theorem` | `ProvedHere` | 1082 | 5 | 1 | Formal all-genus stable-graph expansion |
| `prop:feyn-nekrasov-self-dual` | `proposition` | `ProvedElsewhere` | 1797 | 0 | 0 | Self-dual AGT block on \texorpdfstring{$\Sigma_{0,24}$}{Sigma 0,24} |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (35)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | `ProvedHere` | 130 | 6 | 0 | Protected dual transform and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | `ProvedHere` | 246 | 4 | 0 | Protected transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | `ProvedHere` | 306 | 2 | 0 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | `ProvedHere` | 347 | 4 | 0 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | `ProvedHere` | 408 | 2 | 0 | Scalar fixed-point rigidity on a full scalar package and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | `ProvedHere` | 532 | 2 | 0 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | `ProvedHere` | 651 | 2 | 0 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | `ProvedHere` | 775 | 1 | 0 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | `ProvedHere` | 846 | 6 | 0 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | `ProvedHere` | 984 | 5 | 0 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | `ProvedHere` | 1071 | 1 | 0 | The first nonlinear holographic anomaly |
| `prop:pva-degree-constraint` | `proposition` | `ProvedElsewhere` | 2471 | 0 | 1 | PVA degree constraint and the inevitability of $2{+}1$ dimensions |
| `cor:shadow-connection-heisenberg` | `corollary` | `ProvedElsewhere` | 2909 | 1 | 0 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | `ProvedHere` | 2930 | 2 | 0 | Shadow connection for Virasoro and BPZ on the degenerate-representation surface |
| `comp:holographic-ss-vir` | `computation` | `ProvedHere` | 3108 | 1 | 0 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | `ProvedHere` | 3152 | 1 | 0 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | `ProvedHere` | 3176 | 1 | 0 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | `ProvedHere` | 3262 | 1 | 0 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | `ProvedHere` | 3297 | 0 | 0 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | `ProvedHere` | 3339 | 0 | 0 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | `ProvedHere` | 3430 | 0 | 0 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | `ProvedHere` | 3487 | 0 | 0 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | `ProvedHere` | 3583 | 1 | 0 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | `ProvedHere` | 3642 | 0 | 0 | Holographic datum for $\mathcal W_3$ |
| `cor:critical-dimensions` | `corollary` | `ProvedHere` | 3888 | 0 | 0 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | `ProvedHere` | 3999 | 1 | 0 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | `ProvedHere` | 4028 | 1 | 0 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | `ProvedHere` | 4069 | 0 | 0 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | `ProvedHere` | 4099 | 0 | 0 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | `ProvedHere` | 4218 | 1 | 0 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | `ProvedHere` | 4359 | 0 | 0 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | `ProvedHere` | 4545 | 0 | 0 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | `ProvedHere` | 4684 | 0 | 0 | Lifts as relative MC elements |
| `cor:holographic-deformation-cohomology` | `corollary` | `ProvedElsewhere` | 4721 | 0 | 0 | — |
| `comp:burns-space-holographic-datum` | `computation` | `ProvedHere` | 6029 | 1 | 2 | Burns space holographic modular Koszul datum |

#### `chapters/connections/genus1_seven_faces.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:g1sf-b-cycle-monodromy` | `theorem` | `ProvedHere` | 1464 | 2 | 0 | $B$-cycle monodromy of the collision residue |

#### `chapters/connections/genus_complete.tex` (20)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:elliptic-bar` | `theorem` | `ProvedElsewhere` | 265 | 1 | 1 | Elliptic bar complex; {} \cite{FBZ04} |
| `prop:bulk-from-boundary` | `proposition` | `ProvedElsewhere` | 1353 | 0 | 3 | Algebraic closed sector from the boundary; {} \cite{BD04,FG12,CG17} |
| `prop:sewing-universal-property` | `proposition` | `ProvedHere` | 2002 | 0 | 0 | Universal property of the sewing envelope |
| `prop:hs-trace-class` | `proposition` | `ProvedHere` | 2051 | 3 | 0 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | `ProvedHere` | 2082 | 0 | 0 | General HS-sewing criterion |
| `cor:hs-sewing-standard-landscape` | `corollary` | `ProvedElsewhere` | 2130 | 0 | 0 | Standard landscape |
| `cor:hs-implies-gram` | `corollary` | `ProvedHere` | 2169 | 3 | 0 | Diagonal positive sewing implies Gram positivity |
| `thm:heisenberg-one-particle-sewing` | `theorem` | `ProvedHere` | 2192 | 0 | 0 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | `ProvedHere` | 2283 | 1 | 0 | Finite-window conilpotency and completed pro-conilpotency |
| `thm:dirichlet-weight-formula` | `theorem` | `ProvedHere` | 2592 | 0 | 0 | — |
| `cor:virasoro-mode-removal` | `corollary` | `ProvedHere` | 2649 | 2 | 0 | — |
| `thm:euler-koszul-criterion` | `theorem` | `ProvedHere` | 2708 | 2 | 0 | — |
| `comp:euler-koszul-defect-table` | `computation` | `ProvedHere` | 2745 | 2 | 0 | Euler--Koszul defect table for the standard landscape |
| `prop:zeta-zeros-defect-derivative` | `proposition` | `ProvedHere` | 2837 | 0 | 0 | — |
| `thm:li-closed-form` | `theorem` | `ProvedHere` | 2877 | 0 | 0 | — |
| `thm:li-asymptotics` | `theorem` | `ProvedHere` | 2911 | 2 | 0 | First Li coefficient and finite sign computation |
| `thm:surface-moment-positivity` | `theorem` | `ProvedHere` | 3051 | 0 | 0 | Gram positivity |
| `cor:virasoro-gram-ratio` | `corollary` | `ProvedHere` | 3074 | 0 | 0 | Virasoro sewing deficit |
| `thm:sewing-rkhs` | `theorem` | `ProvedHere` | 3116 | 2 | 0 | Sewing RKHS |
| `prop:benjamin-chang-bridge` | `proposition` | `ProvedHere` | 3229 | 0 | 1 | — |

#### `chapters/connections/holographic_codes_koszul.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:hc-projection-not-kl` | `proposition` | `ProvedHere` | 368 | 0 | 0 | Independence of symplectic projection and Knill--Laflamme recovery |
| `prop:hc-theorem-h-scope` | `proposition` | `ProvedHere` | 544 | 0 | 0 | Curve-level Hochschild support and physical transport |

#### `chapters/connections/holographic_datum_master.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:hdm-sts-sklyanin-bracket` | `theorem` | `ProvedElsewhere` | 1012 | 0 | 1 | Semenov-Tian-Shansky Sklyanin bracket |
| `thm:hdm-face-6` | `theorem` | `ProvedHere` | 1039 | 1 | 1 | Face~6: Sklyanin bracket; \ (identification with classical limit of collision residue); \ (Sklyanin bracket: Semenov-Tian-Shansky 1983) |
| `prop:hdm-binary-residue-not-bulk` | `proposition` | `ProvedHere` | 2905 | 0 | 0 | Counter-scope: the binary residue does not determine the closed-sector algebra |
| `prop:hdm-finality-central-kernel` | `proposition` | `ProvedHere` | 3326 | 0 | 0 | Counter-scope: projections alone do not imply finality |

#### `chapters/connections/master_concordance.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:typed-verdier-koszul-firewall` | `theorem` | `ProvedHere` | 69 | 2 | 0 | The five objects and their ambient categories |
| `prop:master-oca-bmodel` | `proposition` | `ProvedElsewhere` | 406 | 0 | 1 | HKR on an affine chart; $$, physical realization $$ |
| `lem:master-oca-sheafy-hkr-extension` | `lemma` | `ProvedElsewhere` | 461 | 1 | 3 | HKR for smooth affine and smooth projective schemes; $$ |
| `cor:master-oca-rozansky-witten-k3` | `corollary` | `ProvedHere` | 515 | 1 | 0 | Hochschild cohomology of $K3$; $$ |
| `cor:master-oca-k3-hilbert-hierarchy` | `corollary` | `ProvedHere` | 566 | 1 | 1 | Hochschild dimensions of K3 Hilbert schemes; $$ |
| `cor:master-oca-bmodel-elliptic` | `corollary` | `ProvedHere` | 621 | 1 | 0 | Hochschild cohomology of an elliptic curve; $$ |
| `cor:master-oca-quintic` | `corollary` | `ProvedHere` | 693 | 1 | 0 | Hochschild cohomology of the quintic threefold; $$ |
| `cor:master-oca-bmodel-schouten` | `corollary` | `ProvedElsewhere` | 762 | 1 | 3 | Schouten--Nijenhuis bracket as closed-colour $\mathsf{SC}^{\mathrm{ch,top}}$-brace; $$, physical realization $$ |
| `lem:master-scalar-non-faithfulness` | `lemma` | `ProvedHere` | 811 | 0 | 0 | A fibre of the graded Euler series; $$ |
| `thm:master-scalar-nonfaithful-witness-c16` | `theorem` | `ProvedHere` | 845 | 1 | 2 | A rank-$16$ graded-character fibre; $$ |
| `lem:master-delta-cartan-window` | `lemma` | `ProvedHere` | 1040 | 0 | 1 | Classical double of the zero abelian Lie bialgebra; $$ |
| `lem:master-epsilon-cartan-window` | `lemma` | `ProvedHere` | 1069 | 0 | 1 | Heisenberg current algebra from a bilinear form; $$ |
| `thm:master-vir-26-bc-brst-topologisation` | `theorem` | `ProvedElsewhere` | 1182 | 1 | 1 | Bosonic-string BRST identities at matter central charge $26$; $$ |
| `thm:master-generalized-matter-ghost-brst` | `theorem` | `ProvedHere` | 1252 | 1 | 1 | Conformal-weight constraint for the reparametrization BRST current; $$ |
| `cor:master-screening-brst-c-lt-minus-1` | `corollary` | `ProvedElsewhere` | 1333 | 1 | 1 | Felder screening complexes; $$ |
| `thm:master-n2-topological-twist-topologisation` | `theorem` | `ProvedElsewhere` | 1354 | 1 | 1 | $N=2$ topological-twist identities; $$ |
| `cor:master-n2-twist-kazama-suzuki` | `corollary` | `ProvedElsewhere` | 1422 | 1 | 1 | Kazama--Suzuki cosets and the two twists; $$ |

#### `chapters/connections/master_reconstruction.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:mr-primitive-chart-circularity` | `remark` | `ProvedHere` | 239 | 0 | 0 | Geometric and chart presentations |
| `thm:mr-morita` | `theorem` | `ProvedHere` | 395 | 2 | 1 | $F_0$-reconstruction: factorization Morita |
| `prop:mr-factorization-ew-lines` | `proposition` | `ProvedHere` | 673 | 1 | 0 | Factorization Eilenberg--Watts for intrinsic lines |
| `thm:mr-drinfeld-double` | `theorem` | `ProvedElsewhere` | 733 | 0 | 1 | Categorical Drinfeld-center formation from line data |
| `thm:mr-modular` | `theorem` | `ProvedElsewhere` | 776 | 0 | 1 | Genus-zero restriction of a full modular functor |
| `prop:mr-scalar-fibre-multiplicity` | `proposition` | `ProvedHere` | 829 | 1 | 0 | Multiplicity in a scalar fibre |
| `lem:mr-rescaling-contraction` | `lemma` | `ProvedHere` | 1554 | 0 | 0 | Rescaling a contraction |

#### `chapters/connections/semistrict_modular_higher_spin_w3.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:finite-degree-polynomial-pva-chapter` | `theorem` | `ProvedHere` | 124 | 2 | 1 | Finite-degree theorem for polynomial PVAs |
| `cor:semistrictity-classical-W3-chapter` | `corollary` | `ProvedHere` | 179 | 2 | 1 | Semistrictity of the classical $W_3$ bulk |
| `prop:tree-identity-semistrict-chapter` | `proposition` | `ProvedHere` | 210 | 1 | 0 | Tree identity for semistrict cyclic theories |
| `prop:canonical-central-hodge-shadow-lift-chapter` | `proposition` | `ProvedHere` | 309 | 0 | 0 | Canonical central Hodge-shadow lift |
| `prop:clutching-duality-shadow-lift-chapter` | `proposition` | `ProvedHere` | 350 | 1 | 0 | Clutching additivity and duality symmetry |
| `thm:fiber-decomposition-shadow-base-point-chapter` | `theorem` | `ProvedHere` | 392 | 0 | 0 | Fiber decomposition over the shadow base point |
| `cor:shadow-centered-reduction-chapter` | `corollary` | `ProvedHere` | 424 | 2 | 0 | Shadow-centered reduction |
| `thm:finite-degree-convolution-chapter` | `theorem` | `ProvedHere` | 465 | 0 | 0 | Finite-degree convolution theorem |
| `thm:quadratic-cubic-twisting-theorem-chapter` | `theorem` | `ProvedHere` | 517 | 1 | 0 | Quadratic-cubic twisting theorem |
| `prop:admissibility-finite-slices-chapter` | `proposition` | `ProvedHere` | 603 | 0 | 0 | Admissibility and finite-dimensional weight slices |
| `thm:cubic-weight-recursion-chapter` | `theorem` | `ProvedHere` | 626 | 4 | 0 | Cubic weight recursion around the shadow base point |
| `cor:cubic-obstruction-classes-chapter` | `corollary` | `ProvedHere` | 664 | 1 | 0 | Cubic obstruction classes |
| `prop:stable-graph-identity-chapter` | `proposition` | `ProvedHere` | 677 | 1 | 0 | Stable-graph identity for semistrict modular theories |
| `prop:well-definedness-completed-boundary-model-chapter` | `proposition` | `ProvedHere` | 736 | 2 | 0 | Well-definedness of the completed boundary model |
| `thm:main-semistrict-modular-higher-spin-package-chapter` | `theorem` | `ProvedHere` | 766 | 8 | 0 | Classical $W_3$ semistrict modular higher-spin package |
| `cor:platonic-reduction-W3-frontier` | `corollary` | `ProvedHere` | 813 | 1 | 0 | Finite semistrict reduction of the classical $W_3$ frontier |

#### `chapters/connections/subregular_hook_frontier.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:transport-propagation` | `proposition` | `ProvedHere` | 303 | 0 | 0 | Transport propagation lemma |
| `prop:hook-ghost-constant` | `proposition` | `ProvedHere` | 373 | 0 | 0 | Hook ghost constant |
| `prop:ds-bar-hook-commutation` | `proposition` | `ProvedElsewhere` | 425 | 0 | 2 | Hook-type data visible before DS/bar comparison |
| `thm:canonical-degree-detection` | `theorem` | `ProvedHere` | 481 | 0 | 0 | Generator-degree detection in an OPE normal form |
| `thm:full-raw-coefficient-packet` | `theorem` | `ProvedHere` | 642 | 2 | 0 | Exact Bell recursion for the full singular packet |
| `thm:miura-product-formula` | `theorem` | `ProvedHere` | 800 | 0 | 0 | Subregular Miura product formula |
| `thm:subregular-appell-formula` | `theorem` | `ProvedHere` | 837 | 0 | 0 | Subregular Appell formula |
| `prop:bp-fs-normal-form-opes` | `proposition` | `ProvedElsewhere` | 888 | 0 | 1 | Bershadsky--Polyakov OPEs in Feigin--Semikhatov normal form |
| `thm:bp-strict` | `theorem` | `ProvedHere` | 914 | 3 | 0 | Quadratic OPE degree of Bershadsky--Polyakov |
| `comp:bp-kappa-three-paths` | `computation` | `ProvedHere` | 939 | 2 | 1 | Bershadsky--Polyakov scalar audit |
| `prop:bp-complementarity-constant` | `proposition` | `ProvedHere` | 989 | 2 | 0 | Standard Bershadsky--Polyakov central-charge conductor |
| `prop:w4-fs-normal-form-ope` | `proposition` | `ProvedElsewhere` | 1156 | 0 | 1 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} OPE in Feigin--Semikhatov normal form |
| `thm:w4-cubic` | `theorem` | `ProvedHere` | 1191 | 1 | 0 | Cubic OPE degree in \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} |
| `thm:unbounded-canonical-degree` | `theorem` | `ProvedHere` | 1328 | 1 | 0 | Unbounded symbolic OPE degree in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | `ProvedHere` | 1378 | 0 | 0 | Triangular primary-renormalization theorem |

#### `chapters/connections/thqg_entanglement_theory.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:thqg-ent-algebraic-sector` | `remark` | `ProvedHere` | 16 | 0 | 3 | Algebraic-sector identification for the entanglement register |

#### `chapters/connections/thqg_introduction_supplement.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:supp-algebraic-physical-bulk-separation` | `proposition` | `ProvedHere` | 340 | 1 | 0 | Algebraic datum versus physical bulk |

#### `chapters/connections/thqg_introduction_supplement_body.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:thqg-intro-four-layer-separation` | `proposition` | `ProvedHere` | 323 | 1 | 0 | Four-layer separation |
| `thm:thqg-intro-quartic-linfty` | `theorem` | `ProvedElsewhere` | 434 | 1 | 0 | Quartic obstruction $=$ $L_\infty$ bracket |
| `prop:thqg-intro-flatness` | `proposition` | `ProvedElsewhere` | 553 | 0 | 0 | Flatness of the shadow connection |
| `thm:thqg-intro-hs-general` | `theorem` | `ProvedElsewhere` | 1630 | 1 | 0 | General HS-sewing criterion |
| `thm:thqg-intro-heisenberg-sewing` | `theorem` | `ProvedElsewhere` | 1651 | 1 | 0 | Heisenberg sewing |
| `rem:thqg-intro-algebraic-sector-vs-dynamical-metric` | `remark` | `ProvedHere` | 2124 | 1 | 3 | Algebraic sector versus dynamical-metric path integral |

#### `chapters/connections/thqg_open_closed_realization.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:thqg-oc-algebraic-sector` | `remark` | `ProvedHere` | 24 | 2 | 3 | Algebraic sector identification |
| `prop:bd-algebraic-bridge` | `proposition` | `ProvedHere` | 216 | 3 | 1 | Bridge: BD chiral operad $\leftrightarrow$ algebraic $\mathcal{E}\!\mathit{nd}^{\mathrm{ch}}$ |
| `thm:thqg-brace-dg-algebra` | `theorem` | `ProvedHere` | 358 | 8 | 0 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | `ProvedHere` | 631 | 4 | 0 | Universal open/closed pair (chiral Swiss-cheese theorem) |
| `prop:thqg-universal-action-not-reconstruction` | `proposition` | `ProvedHere` | 723 | 2 | 0 | Typed physical-bulk comparison |
| `rem:thqg-oc-physical` | `remark` | `ProvedHere` | 780 | 1 | 0 | Bulk, Verdier dual, and bar-cobar inverse |
| `prop:mixed-sector-bulk-boundary` | `proposition` | `ProvedHere` | 807 | 2 | 0 | Mixed sector encodes bulk-to-boundary module structure |
| `prop:thqg-swiss-cheese-no-yangian-coproduct` | `proposition` | `ProvedHere` | 844 | 1 | 0 | Yangian coproducts require line-category data |
| `thm:thqg-local-global-bridge` | `theorem` | `ProvedHere` | 911 | 7 | 0 | Local-global bridge |
| `cor:thqg-intrinsic-bulk` | `corollary` | `ProvedHere` | 1005 | 1 | 0 | The intrinsic categorical center |
| `thm:thqg-hochschild-register-separation` | `theorem` | `ProvedHere` | 1047 | 8 | 0 | Separation of Hochschild, trace, THH, BV, and Koszul duality |
| `thm:thqg-annulus-trace` | `theorem` | `ProvedHere` | 1190 | 2 | 5 | Annulus trace theorem |
| `prop:thqg-occ-CD-ANm1-24` | `proposition` | `ProvedHere` | 2556 | 0 | 0 | Chacaltana--Distler central charges for $\mathcal T\lbrack A_{N-1}, \Sigma_{0,24}\rbrack$ |

#### `chapters/connections/vertical_equivalence_level_0.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:vel0-quartic-anomaly` | `theorem` | `ProvedHere` | 102 | 4 | 3 | Quartic Pontryagin-type form for the 6d $\hCS$ one-loop obstruction |
| `lem:vel0-admissible-g` | `lemma` | `ProvedHere` | 195 | 2 | 0 | Admissible gauge dg-Lie at level $0$ |

### Appendices (238)

#### `appendices/_sl2_yangian_insert.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:ordered-bar-sl2` | `computation` | `ProvedHere` | 86 | 0 | 0 | Degree-$2$ ordered bar complex of $\widehat{\mathfrak{sl}}_2$ |
| `prop:ybe-from-d-squared` | `proposition` | `ProvedHere` | 164 | 1 | 0 | $d^2=0$ is the classical Yang--Baxter equation |
| `thm:yang-r-matrix` | `theorem` | `ProvedHere` | 227 | 0 | 0 | Yang $R$-matrix from the ordered bar complex |
| `thm:rtt-sl2` | `theorem` | `ProvedHere` | 307 | 5 | 1 | RTT presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `constr:gauss-sl2` | `construction` | `ProvedHere` | 379 | 0 | 0 | Gauss decomposition and Drinfeld generators |
| `thm:pbw-sl2` | `theorem` | `ProvedHere` | 429 | 1 | 1 | PBW basis of $Y_\hbar(\mathfrak{sl}_2)$ |
| `cor:hilbert-sl2` | `corollary` | `ProvedHere` | 475 | 1 | 0 | Hilbert series |
| `constr:eval-sl2` | `construction` | `ProvedHere` | 499 | 0 | 0 | Evaluation modules |
| `prop:eval-tensor-sl2` | `proposition` | `ProvedHere` | 521 | 1 | 0 | Tensor products and Yang--Baxter |

#### `appendices/arnold_relations.tex` (10)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:arnold-relations-appendix` | `theorem` | `ProvedElsewhere` | 19 | 2 | 3 | Arnold relations \cite{Arnold69} |
| `prop:arnold-genus-split-appendix` | `proposition` | `ProvedHere` | 64 | 1 | 3 | Configuration-space relation packages |
| `prop:operadic-equivalence-arnold` | `proposition` | `ProvedHere` | 138 | 2 | 0 | Affine screen residue cancellation |
| `thm:bar-d-squared-arnold` | `theorem` | `ProvedHere` | 173 | 3 | 0 | Affine bar square: Arnold forms plus Borcherds coefficients |
| `lem:OS-cohomology-arnold` | `lemma` | `ProvedElsewhere` | 238 | 1 | 1 | OS computes cohomology \cite{OS80} |
| `cor:bar-d-squared-zero-arnold` | `corollary` | `ProvedHere` | 264 | 1 | 0 | Affine simple-pole bar differential |
| `thm:arnold-iff-nilpotent` | `theorem` | `ProvedHere` | 293 | 2 | 0 | Affine Arnold form relation and triple-residue nilpotency |
| `thm:arnold-general-n` | `theorem` | `ProvedElsewhere` | 386 | 0 | 2 | Arnold relations for \texorpdfstring{$n$}{n} affine points \cite{Arnold69, OS80} |
| `thm:config-boundary-relations` | `theorem` | `ProvedHere` | 427 | 0 | 1 | Configuration-space boundary relations |
| `cor:dres-squared-global` | `corollary` | `ProvedHere` | 459 | 4 | 0 | \texorpdfstring{$d_{\mathrm{res}}^2$}{d-res squared} and global corrections |

#### `appendices/branch_line_reductions.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:first-obstruction-traceless-quadratic` | `theorem` | `ProvedHere` | 316 | 0 | 0 | First obstruction is traceless and quadratic |
| `cor:filtered-lift-vanishing` | `corollary` | `ProvedHere` | 389 | 1 | 0 | Vanishing criterion for filtered lifts |
| `lem:positive-weight-contraction` | `lemma` | `ProvedHere` | 457 | 0 | 0 | Positive-weight contraction |
| `thm:vir-positive-weight-acyclic` | `theorem` | `ProvedHere` | 474 | 1 | 0 | Positive-weight Virasoro sectors are acyclic |
| `cor:vir-localization-reduced-spectral` | `corollary` | `ProvedHere` | 493 | 1 | 0 | Localization to reduced spectral sectors |
| `prop:odd-sheet-rigidity` | `proposition` | `ProvedHere` | 521 | 2 | 0 | Odd-sheet rigidity for one-line reductions |
| `cor:mu2-centered-at-13` | `corollary` | `ProvedHere` | 562 | 1 | 0 | The genus-\(2\) one-line coefficient is centered at \texorpdfstring{$13$}{13} |
| `lem:universal-branch-moments` | `lemma` | `ProvedHere` | 625 | 1 | 0 | Universal branch moments |
| `thm:hodge-depth-formula` | `theorem` | `ProvedHere` | 687 | 1 | 0 | Depth formula |
| `lem:separating-hodge-splitting` | `lemma` | `ProvedHere` | 720 | 1 | 0 | Separating Hodge splitting |
| `lem:nonseparating-hodge-extension` | `lemma` | `ProvedHere` | 762 | 0 | 0 | Nonseparating Hodge extension |
| `thm:genus-two-transparency` | `theorem` | `ProvedHere` | 801 | 3 | 0 | Genus-\(2\) transparency on a one-line branch quotient |
| `cor:vir-genus-two-vanishing` | `corollary` | `ProvedHere` | 845 | 1 | 0 | Virasoro genus-\(2\) coefficient vanishes in the one-line quotient |
| `cor:first-primitive-genus-three` | `corollary` | `ProvedHere` | 857 | 1 | 0 | The first primitive traceless coefficient begins in genus \texorpdfstring{$3$}{3} |
| `lem:genus-three-rose-unique` | `lemma` | `ProvedHere` | 875 | 1 | 0 | Uniqueness of the primitive rose in genus \texorpdfstring{$3$}{3} |
| `thm:pure-branch-primitive-coefficient` | `theorem` | `ProvedHere` | 905 | 3 | 0 | Pure-branch primitive coefficient on a rank-two sheet |
| `thm:first-primitive-top-hodge-layer` | `theorem` | `ProvedHere` | 1000 | 3 | 0 | First primitive top-Hodge layer |

#### `appendices/combinatorial_frontier.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:virasoro-spurious-recurrence` | `remark` | `ProvedHere` | 989 | 1 | 0 | Depth-$3$ spurious Virasoro recurrence |
| `prop:virasoro-pade` | `proposition` | `ProvedHere` | 1022 | 1 | 0 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dual_methodology.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:abstract-bar-cobar` | `theorem` | `ProvedElsewhere` | 25 | 0 | 2 | Abstract bar-cobar equivalence \cite{FG12, HA} |
| `thm:abstract-rh` | `theorem` | `ProvedElsewhere` | 96 | 0 | 1 | Abstract Riemann--Hilbert \cite{KS90} |
| `thm:geometric-infty-operads` | `theorem` | `ProvedHere` | 162 | 0 | 0 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |
| `thm:glz-quadratic-duality-scope` | `theorem` | `ProvedElsewhere` | 238 | 0 | 1 | Gui--Li--Zeng quadratic duality: scope |

#### `appendices/hochschild_conventions.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:hochschild-crosswalk` | `proposition` | `ProvedHere` | 26 | 5 | 0 | Three Hochschild theories: type signatures, scope, and comparison rules |
| `rem:hochschild-circle-restriction-firewall` | `remark` | `ProvedElsewhere` | 135 | 0 | 5 | Circle and restriction firewall |
| `rem:bzfn-ambient-not-dial` | `remark` | `ProvedElsewhere` | 174 | 0 | 1 | BZFN ambient discipline |

#### `appendices/homotopy_transfer.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:htt` | `theorem` | `ProvedElsewhere` | 69 | 0 | 2 | Homotopy transfer theorem \cite{LV12, Kadeishvili80} |
| `lem:sdr-existence` | `lemma` | `ProvedHere` | 146 | 0 | 0 | Existence of SDR |
| `thm:tree-formula` | `theorem` | `ProvedElsewhere` | 209 | 0 | 1 | Tree formula for transferred operations \cite{LV12} |
| `rem:tree-level` | `remark` | `ProvedHere` | 225 | 1 | 0 | Tree-level only |
| `prop:transfer-signs` | `proposition` | `ProvedElsewhere` | 259 | 0 | 1 | Sign computation \cite{LV12} |
| `thm:minimal-model-existence` | `theorem` | `ProvedElsewhere` | 284 | 0 | 1 | Existence of minimal models \cite{Kadeishvili80} |
| `cor:formality` | `corollary` | `ProvedElsewhere` | 296 | 0 | 2 | Formality \cite{DGMS75, Kon99} |
| `thm:htt-operadic` | `theorem` | `ProvedElsewhere` | 339 | 0 | 1 | Homotopy transfer for operadic algebras \cite{LV12} |
| `prop:linf-relations` | `proposition` | `ProvedElsewhere` | 380 | 0 | 1 | \texorpdfstring{$\Linf$}{L-infinity}-relations for transferred structure \cite{LV12} |
| `thm:linf-minimal-unique` | `theorem` | `ProvedElsewhere` | 404 | 0 | 1 | Uniqueness of minimal \texorpdfstring{$\Linf$}{L-infinity}-model \cite{LV12} |
| `thm:chiral-htt` | `theorem` | `ProvedHere` | 455 | 5 | 0 | Chiral homotopy transfer |
| `prop:transfer-bar` | `proposition` | `ProvedElsewhere` | 498 | 1 | 1 | Transferred structure and bar complex \cite{LV12} |
| `prop:trees-boundary-strata` | `proposition` | `ProvedHere` | 618 | 1 | 1 | Trees as boundary strata |

#### `appendices/koszul_reference.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:genus-graded-mc-appendix` | `theorem` | `ProvedElsewhere` | 268 | 5 | 0 | Genus-graded MC elements parametrize deformations |
| `lem:conilpotency-necessary` | `lemma` | `ProvedHere` | 506 | 0 | 0 | Algebraic and completed conilpotency |
| `lem:connectedness-augmentation` | `lemma` | `ProvedHere` | 545 | 0 | 0 | Connectedness characterizes augmentation |
| `thm:curvature-central-appendix` | `theorem` | `ProvedHere` | 657 | 0 | 1 | Central curvature and internal strictness |

#### `appendices/nonlinear_modular_shadows.tex` (58)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `def:nms-modular-convolution-lie` | `definition` | `ProvedHere` | 118 | 2 | 1 | Modular convolution dg~Lie algebra |
| `rem:nms-linfty-enrichment` | `remark` | `ProvedElsewhere` | 164 | 2 | 1 | The modular $L_\infty$ enrichment |
| `thm:nms-mc-principle` | `theorem` | `ProvedHere` | 184 | 1 | 0 | Algebra structure $=$ Maurer--Cartan element |
| `thm:nms-shadow-tower-mc` | `theorem` | `ProvedHere` | 401 | 0 | 0 | Shadow obstruction tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | `ProvedHere` | 441 | 1 | 0 | Standard-family evaluations of the universal class |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | `ProvedHere` | 556 | 0 | 0 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | `ProvedHere` | 610 | 0 | 0 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | `ProvedHere` | 656 | 0 | 0 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | `ProvedHere` | 665 | 0 | 0 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | `ProvedHere` | 686 | 1 | 0 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | `ProvedHere` | 701 | 0 | 0 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | `ProvedHere` | 800 | 2 | 0 | Quartic shadow master equations |
| `prop:nms-quartic-closure-envelope` | `proposition` | `ProvedHere` | 952 | 0 | 0 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | `ProvedHere` | 982 | 0 | 0 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | `ProvedHere` | 1002 | 1 | 0 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | `ProvedHere` | 1080 | 0 | 0 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | `ProvedHere` | 1104 | 0 | 0 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | `ProvedHere` | 1197 | 2 | 0 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | `ProvedHere` | 1242 | 1 | 0 | Weight-changing projection of the quartic contact |
| `cor:nms-betagamma-boundary-law` | `corollary` | `ProvedHere` | 1267 | 0 | 0 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | `ProvedHere` | 1284 | 3 | 0 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | `ProvedHere` | 1313 | 0 | 0 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | `ProvedHere` | 1362 | 0 | 0 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | `ProvedHere` | 1400 | 1 | 0 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | `ProvedHere` | 1428 | 0 | 0 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | `ProvedHere` | 1500 | 1 | 0 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | `ProvedHere` | 1560 | 1 | 0 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `prop:nms-w3-visible-resonance-factor` | `proposition` | `ProvedHere` | 1599 | 1 | 0 | Visible quartic resonance factor for \texorpdfstring{$\mathcal W_3$}{W3} |
| `thm:nms-w3-full-quartic-gram` | `theorem` | `ProvedHere` | 1641 | 1 | 0 | Full $\mathcal W_3$ quartic Gram determinant |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | `ProvedHere` | 1714 | 1 | 0 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | `ProvedHere` | 1732 | 0 | 0 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | `ProvedHere` | 1748 | 2 | 0 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | `ProvedHere` | 1857 | 1 | 0 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | `ProvedHere` | 1909 | 0 | 0 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | `ProvedHere` | 1933 | 2 | 0 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behavior` | `corollary` | `ProvedHere` | 2021 | 1 | 0 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | `ProvedHere` | 2093 | 0 | 0 | Functoriality and duality through quartic order |
| `thm:nms-all-degree-master-equation` | `theorem` | `ProvedHere` | 2226 | 2 | 0 | All-degree master equation |
| `cor:nms-quintic-master-equation` | `corollary` | `ProvedHere` | 2262 | 1 | 0 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | `ProvedHere` | 2284 | 5 | 0 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | `ProvedHere` | 2308 | 0 | 0 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | `ProvedHere` | 2327 | 3 | 0 | Finite termination for primitive archetypes |
| `prop:nms-genus-loop-properties` | `proposition` | `ProvedHere` | 2442 | 1 | 0 | Basic properties of the genus loop operator |
| `thm:nms-genus-loop-model-families` | `theorem` | `ProvedHere` | 2510 | 0 | 0 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | `ProvedHere` | 2601 | 0 | 0 | The modular invariant hierarchy beyond $\hat{A}$ |
| `def:nms-degree-r-resonance-class` | `definition` | `ProvedHere` | 2792 | 1 | 0 | Degree-$r$ contact bundle and resonance class |
| `thm:nms-bipartite-complementarity` | `theorem` | `ProvedHere` | 3038 | 1 | 0 | Bipartite complementarity principle |
| `thm:nms-bipartite-vanishing` | `theorem` | `ProvedHere` | 3150 | 1 | 0 | Bipartite vanishing theorem |
| `thm:reduced-weight-finiteness` | `theorem` | `ProvedHere` | 3500 | 1 | 0 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | `ProvedHere` | 3588 | 1 | 0 | Window locality |
| `cor:exact-stabilization` | `corollary` | `ProvedHere` | 3610 | 1 | 0 | Exact stabilization |
| `def:nms-kappa-matrix` | `definition` | `ProvedHere` | 3744 | 0 | 0 | Kappa matrix and propagator |
| `lem:nms-euler-inversion` | `lemma` | `ProvedHere` | 3786 | 1 | 0 | Euler inversion |
| `prop:kac-shadow-singularity` | `proposition` | `ProvedHere` | 3873 | 1 | 0 | Kac-shadow singularity principle |
| `thm:shadow-subalgebra-autonomy` | `theorem` | `ProvedHere` | 4192 | 3 | 0 | Shadow subalgebra autonomy |
| `cor:w-line-alternating-vanishing` | `corollary` | `ProvedHere` | 4267 | 0 | 0 | $W$-line alternating vanishing |
| `def:nms-mc-moduli-curve` | `definition` | `ProvedHere` | 4446 | 0 | 0 | MC moduli curve |
| `thm:nms-mc-moduli-curve-structure` | `theorem` | `ProvedHere` | 4469 | 1 | 0 | MC moduli curve structure |

#### `appendices/ordered_associative_chiral_kd.tex` (97)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:bicom-e` | `lemma` | `ProvedHere` | 230 | 0 | 0 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | `ProvedHere` | 320 | 0 | 0 | Ordered chiral shuffle theorem |
| `constr:r-matrix-covering-vol1` | `construction` | `ProvedHere` | 432 | 0 | 0 | The covering-space frame |
| `prop:r-matrix-descent-vol1` | `proposition` | `ProvedHere` | 609 | 3 | 0 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | `ProvedHere` | 755 | 4 | 0 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | `ProvedHere` | 911 | 0 | 0 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | `ProvedHere` | 953 | 1 | 0 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | `ProvedHere` | 985 | 0 | 0 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | `ProvedHere` | 996 | 1 | 0 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | `ProvedHere` | 1061 | 0 | 0 | — |
| `prop:one-defect` | `proposition` | `ProvedHere` | 1088 | 0 | 0 | — |
| `thm:tangent=K` | `theorem` | `ProvedHere` | 1110 | 0 | 0 | Tangent identification |
| `cor:infdual` | `corollary` | `ProvedHere` | 1147 | 2 | 0 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | `ProvedHere` | 1170 | 2 | 0 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | `ProvedHere` | 1222 | 3 | 0 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | `ProvedHere` | 1255 | 1 | 0 | Diagonal correspondence |
| `cor:unit` | `corollary` | `ProvedHere` | 1303 | 2 | 0 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | `ProvedHere` | 1321 | 1 | 0 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | `ProvedHere` | 1350 | 2 | 0 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | `ProvedHere` | 1382 | 1 | 0 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | `ProvedHere` | 1408 | 1 | 0 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | `ProvedHere` | 1428 | 1 | 0 | Cap action |
| `thm:pair-of-pants` | `theorem` | `ProvedHere` | 1483 | 1 | 0 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | `ProvedHere` | 1521 | 4 | 0 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | `ProvedHere` | 1575 | 1 | 0 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | `ProvedHere` | 1624 | 2 | 0 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | `ProvedHere` | 1648 | 12 | 0 | Master theorem |
| `def:ordered-real-config` | `definition` | `ProvedHere` | 1777 | 0 | 0 | Ordered real configuration space |
| `prop:ordered-real-config-topology` | `proposition` | `ProvedHere` | 1792 | 0 | 0 | Topology of ordered real configurations |
| `def:ordered-hol-config` | `definition` | `ProvedHere` | 1816 | 0 | 0 | Ordered holomorphic configuration space |
| `constr:sc-operation-space` | `construction` | `ProvedHere` | 1843 | 0 | 0 | The SC$^{\mathrm{ch,top}}$ operation space |
| `constr:ordered-fm-compact` | `construction` | `ProvedHere` | 1913 | 0 | 0 | Ordered Fulton--MacPherson compactification |
| `constr:planted-forests` | `construction` | `ProvedHere` | 1959 | 0 | 0 | Boundary stratification by planted forests |
| `constr:bar-diff-collision` | `construction` | `ProvedHere` | 2001 | 0 | 0 | Bar differential |
| `constr:deconcatenation` | `construction` | `ProvedHere` | 2071 | 0 | 0 | Deconcatenation coproduct |
| `lem:deconcatenation-coderivation` | `lemma` | `ProvedHere` | 2116 | 0 | 0 | Coderivation compatibility |
| `constr:covering-space` | `construction` | `ProvedHere` | 2169 | 0 | 0 | Ordered-to-unordered covering |
| `thm:heisenberg-ordered-bar` | `theorem` | `ProvedHere` | 2294 | 1 | 0 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | `ProvedHere` | 2408 | 0 | 0 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | `ProvedHere` | 2475 | 0 | 0 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | `ProvedHere` | 2536 | 0 | 0 | Formality: class~G, shadow depth~$2$ |
| `thm:bg-ordered-bar` | `theorem` | `ProvedHere` | 2655 | 0 | 0 | Free-field ordered bar complexes |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | `ProvedHere` | 2836 | 1 | 0 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | `ProvedHere` | 2902 | 0 | 0 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | `ProvedHere` | 2961 | 2 | 0 | Ordered Koszul dual of lattice algebras |
| `thm:drinfeld-yangian-sl2` | `theorem` | `ProvedHere` | 3063 | 6 | 0 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | `ProvedHere` | 3153 | 0 | 0 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | `ProvedHere` | 3189 | 3 | 0 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | `ProvedHere` | 3241 | 3 | 0 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | `ProvedHere` | 3282 | 7 | 0 | Classical limit |
| `prop:vir-collision-residue` | `proposition` | `ProvedHere` | 3371 | 2 | 0 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | `ProvedHere` | 3401 | 1 | 0 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | `ProvedHere` | 3428 | 0 | 0 | Gravitational Yangian collapse |
| `prop:grav-yangian-curvature` | `proposition` | `ProvedHere` | 3544 | 0 | 0 | Gravitational Yangian curvature |
| `thm:central-extension-invisible` | `theorem` | `ProvedHere` | 3676 | 0 | 0 | Central extension is invisible to the open-colour double bar |
| `thm:two-colour-double-kd` | `theorem` | `ProvedHere` | 3742 | 1 | 0 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | `ProvedHere` | 3776 | 2 | 0 | Non-redundancy of the two colours |
| `def:spectral-drinfeld-class-app` | `definition` | `ProvedHere` | 4153 | 0 | 0 | Spectral Drinfeld class at filtration $p$ |
| `thm:root-space-one-dim-v1` | `theorem` | `ProvedHere` | 4204 | 0 | 0 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | `ProvedHere` | 4253 | 0 | 0 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | `ProvedHere` | 4319 | 0 | 0 | Dynkin coefficient via the beta integral |
| `thm:sl3-triangle-coefficient` | `theorem` | `ProvedHere` | 4638 | 0 | 0 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | `ProvedHere` | 4722 | 0 | 0 | Serre relations from root-space vanishing |
| `thm:sl4-quadrilateral` | `theorem` | `ProvedHere` | 4918 | 1 | 0 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `def:kz-connection` | `definition` | `ProvedHere` | 5175 | 0 | 0 | KZ connection |
| `def:kzb-connection` | `definition` | `ProvedHere` | 5250 | 0 | 0 | KZB connection |
| `thm:b-cycle-quantum-group` | `theorem` | `ProvedHere` | 5318 | 1 | 0 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno-appendix` | `theorem` | `ProvedElsewhere` | 5445 | 2 | 0 | Drinfeld--Kohno; {} for monodromy, {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | `ProvedHere` | 5526 | 0 | 0 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | `ProvedHere` | 5597 | 0 | 0 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | `ProvedHere` | 5638 | 1 | 0 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `def:ordered-tridegree` | `definition` | `ProvedHere` | 5770 | 0 | 0 | Ordered tridegree |
| `thm:ordered-depth-spectrum` | `theorem` | `ProvedHere` | 5801 | 0 | 0 | Ordered pole-depth spectrum |
| `thm:ordered-AOS` | `theorem` | `ProvedHere` | 5860 | 2 | 0 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | `ProvedHere` | 5939 | 1 | 0 | Averaging and surplus |
| `thm:FG-shadow-vol2` | `theorem` | `ProvedElsewhere` | 6231 | 0 | 0 | Comm\-utator-shadow theorem |
| `thm:ordered-associative-modular-mc` | `theorem` | `ProvedElsewhere` | 6314 | 0 | 0 | Associative modular Maurer--Cartan class |
| `thm:ordered-associative-ds-principal` | `theorem` | `ProvedElsewhere` | 6354 | 0 | 0 | Reduction commutes with associative chiral duality \textup{(}principal case\textup{)} |
| `prop:r-matrix-stable-envelope` | `proposition` | `ProvedHere` | 6898 | 0 | 0 | $R$-matrix comparison |
| `constr:evaluation-map` | `construction` | `ProvedHere` | 6999 | 0 | 0 | Evaluation homomorphism |
| `comp:sl2-eval` | `computation` | `ProvedHere` | 7046 | 0 | 0 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | `ProvedHere` | 7090 | 0 | 0 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | `ProvedHere` | 7138 | 1 | 0 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | `ProvedHere` | 7180 | 0 | 0 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | `ProvedHere` | 7215 | 0 | 0 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `thm:drinfeld-classification` | `theorem` | `ProvedElsewhere` | 7244 | 0 | 0 | Drinfeld classification |
| `prop:eval-drinfeld` | `proposition` | `ProvedHere` | 7267 | 0 | 0 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | `ProvedHere` | 7334 | 2 | 0 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | `ProvedHere` | 7395 | 0 | 0 | Braiding from the $R$-matrix |
| `thm:grothendieck-yangian` | `theorem` | `ProvedElsewhere` | 7440 | 0 | 0 | Grothendieck ring of Yangian modules |
| `def:annular-bar` | `definition` | `ProvedHere` | 7506 | 1 | 0 | Annular bar complex |
| `thm:annular-bar-differential` | `theorem` | `ProvedHere` | 7551 | 1 | 0 | Annular bar differential |
| `thm:annular-HH` | `theorem` | `ProvedHere` | 7644 | 3 | 0 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | `ProvedHere` | 7744 | 1 | 0 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:elliptic-spectral-dichotomy` | `theorem` | `ProvedHere` | 7903 | 2 | 0 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `prop:r-matrix-eigenvalue` | `proposition` | `ProvedHere` | 8106 | 0 | 0 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | `ProvedHere` | 8122 | 1 | 0 | Yang $R$-matrix for $\mathfrak{sl}_N$ |

#### `appendices/q_convention_bridge_appendix.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:q-convention-bridge-main` | `theorem` | `ProvedHere` | 73 | 0 | 0 | Q-convention bridge |
| `thm:q-bridge-cocycle` | `theorem` | `ProvedHere` | 275 | 0 | 0 | Q-bridge as Z/2-cover cocycle |

#### `appendices/signs_and_shifts.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:graded-jacobi` | `proposition` | `ProvedHere` | 66 | 0 | 0 | Graded Jacobi identity |
| `lem:composition-signs` | `lemma` | `ProvedElsewhere` | 117 | 0 | 1 | Sign rule for compositions \cite{LV12} |
| `prop:duality-grading` | `proposition` | `ProvedHere` | 195 | 0 | 0 | Duality and grading reversal |
| `prop:susp-diff` | `proposition` | `ProvedHere` | 319 | 0 | 0 | Suspension and differentials |
| `cor:iterated-susp` | `corollary` | `ProvedElsewhere` | 347 | 0 | 1 | Iterated suspension \cite{LV12} |
| `prop:susp-koszul` | `proposition` | `ProvedElsewhere` | 374 | 0 | 1 | Suspension and Koszul duality \cite{LV12} |
| `prop:det-properties` | `proposition` | `ProvedElsewhere` | 403 | 0 | 1 | Properties of determinant lines \cite{Weibel94} |
| `lem:det-ordering` | `lemma` | `ProvedElsewhere` | 435 | 0 | 1 | Determinant and ordering \cite{Weibel94} |
| `prop:det-config` | `proposition` | `ProvedElsewhere` | 458 | 0 | 1 | Determinant lines on configuration spaces \cite{FM94} |
| `prop:det-residue` | `proposition` | `ProvedElsewhere` | 500 | 0 | 1 | Determinant and residues \cite{Har77} |
| `thm:det-bar-cobar-signs` | `theorem` | `ProvedElsewhere` | 515 | 0 | 1 | Determinant conventions and bar-cobar signs \cite{LV12} |
| `prop:master-sign` | `proposition` | `ProvedElsewhere` | 659 | 1 | 1 | Master sign formula {\cite{LV12}} |
| `prop:orient-fm` | `proposition` | `ProvedElsewhere` | 742 | 0 | 1 | Orientation system on FM compactification \cite{FM94} |
| `lem:residue-orient` | `lemma` | `ProvedElsewhere` | 772 | 0 | 2 | Residue and orientation \cite{FM94, Har77} |
| `prop:LV-conversion-complete` | `proposition` | `ProvedHere` | 1199 | 0 | 0 | Loday--Vallette conversion |

#### `appendices/spectral_higher_genus.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:degeneration-special-c` | `theorem` | `ProvedElsewhere` | 128 | 0 | 2 | Degeneration at \texorpdfstring{$E_2$}{E2} \cite{FLM88, FBZ04} |

#### `appendices/type_system.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:type-composition` | `proposition` | `ProvedHere` | 355 | 1 | 0 | Composition rule |
| `prop:type-meetjoin` | `proposition` | `ProvedHere` | 386 | 0 | 0 | Meet and join of packages |
| `prop:type-lattice-wellformed` | `proposition` | `ProvedHere` | 490 | 2 | 0 | Package-lattice well-formedness |
