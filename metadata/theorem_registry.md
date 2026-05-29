# Theorem Registry

Auto-generated on 2026-05-28 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` and `\ClaimStatusProvedElsewhere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| Proved surface claims | 2157 |
| Total tagged claims | 4124 |
| Active files in `main.tex` | 136 |
| Total `.tex` files scanned | 156 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1739 |
| `ProvedElsewhere` | 418 |
| `Conjectured` | 335 |
| `Conditional` | 1601 |
| `Heuristic` | 31 |
| `Open` | 0 |

## Proved Surface By Environment

| Environment | Count |
|---|---:|
| `theorem` | 935 |
| `proposition` | 710 |
| `corollary` | 239 |
| `lemma` | 140 |
| `computation` | 75 |
| `remark` | 56 |
| `calculation` | 2 |

## Proved Surface By Part

| Part | Count |
|---|---:|
| Frame | 20 |
| Part I: Theory | 1034 |
| Part II: Examples | 585 |
| Part III: Connections | 305 |
| Appendices | 213 |

## Most Populated Proved Files

| File | Proved surface claims |
|---|---:|
| `chapters/connections/arithmetic_shadows.tex` | 120 |
| `chapters/theory/higher_genus_modular_koszul.tex` | 96 |
| `chapters/theory/ordered_associative_chiral_kd.tex` | 92 |
| `appendices/ordered_associative_chiral_kd.tex` | 83 |
| `chapters/examples/w_algebras.tex` | 62 |
| `chapters/theory/configuration_spaces.tex` | 62 |
| `appendices/nonlinear_modular_shadows.tex` | 53 |
| `chapters/theory/higher_genus_foundations.tex` | 53 |
| `chapters/examples/kac_moody.tex` | 51 |
| `chapters/examples/free_fields.tex` | 50 |
| `chapters/theory/higher_genus_complementarity.tex` | 44 |
| `chapters/examples/w_algebras_deep.tex` | 43 |
| `chapters/examples/yangians_computations.tex` | 43 |
| `chapters/examples/yangians_foundations.tex` | 43 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 42 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 41 |
| `chapters/theory/chiral_modules.tex` | 39 |
| `chapters/theory/shadow_tower_higher_coefficients.tex` | 39 |
| `chapters/theory/en_koszul_duality.tex` | 37 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 35 |

## Complete Proved Registry

### Frame (20)

#### `chapters/frame/guide_to_main_results.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:guide-k3-master-L-value` | `theorem` | `ProvedElsewhere` | 695 | 0 | 0 | K3 paramodular L-value identity |

#### `chapters/frame/heisenberg_frame.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:frame-arnold` | `proposition` | `ProvedHere` | 556 | 1 | 0 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | `ProvedHere` | 924 | 3 | 0 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | `ProvedHere` | 1022 | 0 | 0 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | `ProvedElsewhere` | 1229 | 0 | 0 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | `ProvedElsewhere` | 1479 | 0 | 0 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | `ProvedElsewhere` | 1501 | 0 | 0 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | `ProvedElsewhere` | 1649 | 0 | 0 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | `ProvedElsewhere` | 1848 | 0 | 0 | Quantum complementarity for Heisenberg |
| `prop:frame-drinfeld-classical-limit` | `proposition` | `ProvedHere` | 2195 | 1 | 0 | Classical limit and vanishing check |
| `thm:frame-fermion-bar` | `theorem` | `ProvedElsewhere` | 2380 | 1 | 0 | Free fermion bar complex; see Theorem~\ref{thm:fermion-bar-complex-genus-0} |
| `thm:rosetta-sl2-swiss` | `theorem` | `ProvedHere` | 2857 | 2 | 0 | $\mathfrak{sl}_2$ bar complex as $E_1$-chiral coassociative coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | `ProvedHere` | 2929 | 3 | 0 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | `ProvedHere` | 2979 | 0 | 0 | Verdier level identification for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} |
| `prop:rosetta-sl2-pva` | `proposition` | `ProvedHere` | 3083 | 3 | 0 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | `ProvedHere` | 3121 | 4 | 0 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | `ProvedHere` | 4045 | 2 | 0 | Odd current $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | `ProvedHere` | 4960 | 2 | 0 | The Heisenberg center |

#### `chapters/frame/part_ii_platonic_introduction.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:part-ii-k3-master-L-value` | `theorem` | `ProvedElsewhere` | 765 | 1 | 0 | K3 master L-value identity for Part~II |

#### `chapters/frame/part_iii_platonic_introduction.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:part-iii-k3-master-L-value` | `theorem` | `ProvedElsewhere` | 616 | 1 | 0 | K3 master $L$-value identity on the atlas |

### Part I: Theory (1034)

#### `chapters/theory/algebraic_foundations.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:quadratic-koszul` | `theorem` | `ProvedElsewhere` | 393 | 1 | 3 | Classical Koszul models; {} \cite{Priddy70,BGS96,LV12} |
| `thm:convolution-master-identification` | `theorem` | `ProvedElsewhere` | 609 | 3 | 2 | Convolution = master object identification |
| `cor:theta-twisting-morphism` | `corollary` | `ProvedElsewhere` | 721 | 3 | 2 | MC element = twisting morphism |
| `prop:universal-twisting-adjunction` | `proposition` | `ProvedElsewhere` | 828 | 0 | 1 | Universal twisting morphisms {\cite{LV12}} |
| `thm:operadic-homotopy-convolution` | `theorem` | `ProvedElsewhere` | 999 | 1 | 1 | Operadic identification of the convolution algebra |
| `cor:quillen-equivalence-chiral` | `corollary` | `ProvedElsewhere` | 1062 | 0 | 1 | Quillen equivalence for chiral bar-cobar |
| `cor:shadow-algebra-homotopy-invariant` | `corollary` | `ProvedElsewhere` | 1102 | 0 | 1 | Homotopy invariance of the shadow algebra |
| `prop:circ-associative` | `proposition` | `ProvedHere` | 1254 | 0 | 1 | Associativity of the composition product |
| `thm:chiral-ran` | `theorem` | `ProvedElsewhere` | 1422 | 1 | 1 | Chiral algebras on Ran space |
| `thm:operadic-bar` | `theorem` | `ProvedElsewhere` | 1747 | 0 | 1 | Operadic bar complex \cite{LV12} |
| `thm:com-lie` | `theorem` | `ProvedElsewhere` | 1862 | 2 | 4 | Com--Lie Koszul duality {\cite{GK94,LV12}} |
| `prop:quadratic-presentations-com-lie` | `proposition` | `ProvedElsewhere` | 1948 | 0 | 1 | Quadratic presentations~\cite{LV12} |
| `prop:orthogonal` | `proposition` | `ProvedHere` | 1957 | 0 | 0 | Orthogonality |
| `thm:chiral-factorization` | `theorem` | `ProvedElsewhere` | 2104 | 0 | 1 | Chiral algebras are factorization algebras |
| `thm:excision-factorization` | `theorem` | `ProvedElsewhere` | 2207 | 1 | 2 | Excision property |
| `thm:factorization-cosheaf` | `theorem` | `ProvedElsewhere` | 2234 | 1 | 1 | Factorization algebras are cosheaves for Weiss covers |

#### `chapters/theory/all_tier_generating_function_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:all-tier-bivariate-generating-function` | `theorem` | `ProvedHere` | 105 | 4 | 0 | \label{thm:all-tier-bivariate-generating-function} Bivariate hypergeometric generating function for the Virasoro shadow tower |
| `thm:all-tier-laurent-stratification` | `theorem` | `ProvedHere` | 248 | 4 | 0 | \label{thm:all-tier-laurent-stratification} All-tier Laurent stratification of the Virasoro shadow tower at $c = \infty$ |
| `cor:tier-k-leading-coefficient` | `corollary` | `ProvedHere` | 315 | 1 | 0 | \label{cor:tier-k-leading-coefficient} Leading (highest-degree) coefficient of Tier-$K$ |
| `thm:tier-5-closed-form` | `theorem` | `ProvedHere` | 362 | 1 | 0 | \label{thm:tier-5-closed-form} Tier-5 closed form |
| `cor:tier-leading-denominator-pattern` | `corollary` | `ProvedHere` | 430 | 1 | 0 | \label{cor:tier-leading-denominator-pattern} Tier leading denominator pattern |
| `cor:tier-K-kummer-arithmetic` | `corollary` | `ProvedHere` | 464 | 1 | 0 | \label{cor:tier-K-kummer-arithmetic} Denominator support and characteristic numerator primes |
| `thm:all-tier-fuchsian-ode` | `theorem` | `ProvedHere` | 522 | 4 | 0 | \label{thm:all-tier-fuchsian-ode} Fuchsian ODE in $u$ for the bivariate generating function |
| `cor:three-disjoint-hz-iv-chains` | `corollary` | `ProvedHere` | 619 | 4 | 0 | \label{cor:three-disjoint-hz-iv-chains} Three derivations of the scalar formula |
| `thm:all-tier-closed-form-proved` | `theorem` | `ProvedHere` | 652 | 6 | 0 | \label{thm:all-tier-closed-form-proved} Scalar all-tier closed form |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (42)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:curvature-central` | `theorem` | `ProvedHere` | 385 | 0 | 0 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `thm:filtered-cooperads` | `theorem` | `ProvedElsewhere` | 680 | 0 | 1 | Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}) |
| `comp:virasoro-spectral-r-matrix` | `computation` | `ProvedHere` | 992 | 1 | 0 | Virasoro spectral R-matrix on primary states |
| `lem:degree-cutoff` | `lemma` | `ProvedHere` | 1174 | 1 | 0 | Degree cutoff: finite MC equation at each stage |
| `prop:standard-strong-filtration` | `proposition` | `ProvedHere` | 1364 | 2 | 0 | Standard weight truncations and the induced bar filtration |
| `prop:mc4-reduction-principle` | `proposition` | `ProvedHere` | 1486 | 0 | 0 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | `ProvedHere` | 1557 | 1 | 0 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | `ProvedHere` | 1596 | 1 | 0 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | `ProvedHere` | 1636 | 2 | 0 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | `ProvedHere` | 1685 | 5 | 0 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | `ProvedHere` | 1742 | 3 | 0 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | `ProvedHere` | 1806 | 0 | 0 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | `ProvedHere` | 1870 | 4 | 0 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | `ProvedHere` | 1909 | 1 | 0 | Comparison with a completed target by compatible finite quotients |
| `thm:completed-twisting-representability` | `theorem` | `ProvedHere` | 2279 | 0 | 0 | Completed twisting representability |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | `ProvedHere` | 3315 | 0 | 0 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | `ProvedHere` | 3414 | 0 | 0 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | `ProvedHere` | 3457 | 1 | 0 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-stage5-transport-target-3` | `proposition` | `ProvedElsewhere` | 5313 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} transport target-\texorpdfstring{$3$}{3} ladder identities |
| `prop:winfty-stage5-transport-target-4` | `proposition` | `ProvedElsewhere` | 5328 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} transport target-\texorpdfstring{$4$}{4} ladder identities |
| `prop:winfty-stage5-transport-target5-35` | `proposition` | `ProvedElsewhere` | 5372 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} transport singleton from \texorpdfstring{$W^{(3)}W^{(5)}$}{W3W5} |
| `prop:winfty-stage5-transport-target5-45` | `proposition` | `ProvedElsewhere` | 5389 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} transport singleton from \texorpdfstring{$W^{(4)}W^{(5)}$}{W4W5} |
| `thm:twisting-mc` | `theorem` | `ProvedElsewhere` | 5975 | 1 | 1 | Twisting by MC elements {\cite{LV12}} |
| `thm:genus-zero-strict` | `theorem` | `ProvedHere` | 6307 | 1 | 0 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | `ProvedHere` | 6319 | 4 | 0 | Strict nilpotence for the corrected genus tower |
| `thm:bar-modular-operad` | `theorem` | `ProvedHere` | 6431 | 2 | 1 | Bar complex as algebra over the modular operad |
| `thm:glz-curved` | `theorem` | `ProvedElsewhere` | 6711 | 0 | 2 | GLZ, Theorem 5.3 |
| `thm:fg-factorization-bar-cobar` | `theorem` | `ProvedElsewhere` | 6728 | 0 | 1 | FG, Theorem 7.2.1 |
| `cor:koszul-dual-cooperad` | `corollary` | `ProvedElsewhere` | 6764 | 1 | 1 | Koszul dual coalgebra {\cite{GK94}} |
| `cor:genus-expansion-converges` | `corollary` | `ProvedHere` | 6774 | 2 | 0 | Genus expansion convergence |
| `thm:mixed-boundary-sseq` | `theorem` | `ProvedHere` | 7109 | 0 | 0 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | `ProvedHere` | 7133 | 0 | 0 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | `ProvedHere` | 7181 | 0 | 0 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | `ProvedHere` | 7210 | 0 | 0 | Universality |
| `prop:sugawara-contraction` | `proposition` | `ProvedHere` | 7228 | 0 | 0 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | `ProvedHere` | 7292 | 0 | 0 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | `ProvedHere` | 7308 | 0 | 0 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | `ProvedHere` | 7354 | 0 | 0 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | `ProvedHere` | 7403 | 1 | 0 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | `ProvedHere` | 7447 | 1 | 0 | Diagonal GKO transgression |
| `lem:bcac-curved-MC-on-nearby-cycle` | `lemma` | `ProvedHere` | 7874 | 4 | 1 | Curved Maurer--Cartan on the nearby cycle |
| `lem:bcac-triple-intersection-cocycle-splits` | `lemma` | `ProvedHere` | 8022 | 0 | 1 | Triple-intersection cocycle splits on $H_n\cap H_m$ |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (41)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-convergence` | `theorem` | `ProvedHere` | 71 | 0 | 0 | Finite-window convergence of the bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | `ProvedHere` | 424 | 1 | 1 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | `ProvedHere` | 542 | 0 | 1 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | `ProvedHere` | 615 | 0 | 0 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | `ProvedHere` | 659 | 4 | 0 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | `ProvedHere` | 727 | 2 | 1 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `prop:unit-counit-normalization-bci` | `proposition` | `ProvedHere` | 1139 | 0 | 0 | Unit--counit normalization |
| `prop:finite-window-ml-inversion-bci` | `proposition` | `ProvedHere` | 1467 | 1 | 0 | Finite-window Mittag--Leffler inversion |
| `prop:bar-cobar-object-firewall-bci` | `proposition` | `ProvedHere` | 1549 | 0 | 0 | \texorpdfstring{$A/\bar B(A)/A^{\mathrm i}/A^!$}{A/B(A)/Ai/A!} firewall |
| `lem:bar-cobar-associated-graded` | `lemma` | `ProvedHere` | 2382 | 0 | 0 | Associated graded |
| `lem:pushforward-preserves-qi` | `lemma` | `ProvedElsewhere` | 2611 | 0 | 1 | Proper pushforward preserves quasi-isomorphisms |
| `lem:complete-filtered-comparison` | `lemma` | `ProvedHere` | 2758 | 0 | 0 | Complete filtered comparison lemma |
| `thm:fm-boundary-acyclicity` | `theorem` | `ProvedHere` | 3156 | 1 | 0 | FM boundary acyclicity |
| `prop:lagrangian-perfectness` | `proposition` | `ProvedHere` | 3368 | 4 | 0 | Perfectness for the standard landscape |
| `thm:ks-centrality` | `theorem` | `ProvedHere` | 4844 | 0 | 0 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | `ProvedHere` | 4887 | 0 | 0 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | `ProvedHere` | 4939 | 1 | 0 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | `ProvedHere` | 4974 | 0 | 0 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | `ProvedHere` | 5020 | 2 | 0 | Quadratic cone at the scalar basepoint |
| `prop:eta-hessian-transfer` | `proposition` | `ProvedHere` | 5114 | 0 | 0 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | `ProvedHere` | 5150 | 0 | 0 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | `ProvedHere` | 5200 | 0 | 1 | Admissible cyclic rigidity |
| `thm:cech-hca` | `theorem` | `ProvedElsewhere` | 5631 | 0 | 1 | \v{C}ech complex as homotopy chiral algebra |
| `prop:cech-two-element-strict` | `proposition` | `ProvedHere` | 5868 | 1 | 0 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | `ProvedHere` | 6206 | 0 | 0 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | `ProvedHere` | 6266 | 1 | 0 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | `ProvedHere` | 6304 | 0 | 0 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | `ProvedHere` | 6326 | 1 | 0 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | `ProvedHere` | 6424 | 1 | 0 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | `ProvedHere` | 6472 | 2 | 0 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | `ProvedHere` | 6495 | 0 | 0 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | `ProvedHere` | 6540 | 1 | 0 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | `ProvedHere` | 6571 | 1 | 0 | Repeated roots are extension classes |
| `thm:common-core-exact-sequences-inv` | `theorem` | `ProvedHere` | 6642 | 1 | 0 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | `ProvedHere` | 6674 | 2 | 0 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | `ProvedHere` | 6748 | 2 | 0 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | `ProvedHere` | 6788 | 0 | 0 | Explicit coprime-locus projectors |
| `thm:geometric-lift-datum-consequences-inv` | `theorem` | `ProvedHere` | 6892 | 4 | 0 | Divisor-core consequences of lift data |
| `prop:primary-quotient-filtration-lift-inv` | `proposition` | `ProvedHere` | 6945 | 1 | 0 | Primary quotient filtration from lift data |
| `thm:geometric-common-core-factorization-inv` | `theorem` | `ProvedHere` | 6978 | 1 | 0 | Geometric common-core factorization |
| `thm:geometric-ds-common-core-inv` | `theorem` | `ProvedHere` | 7015 | 1 | 0 | Drinfeld--Sokolov common-core transport under lift data |

#### `chapters/theory/bar_construction.tex` (24)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-NAP-homology` | `theorem` | `ProvedHere` | 406 | 1 | 2 | Bar construction as NAP homology |
| `lem:ddr-preserves-log` | `lemma` | `ProvedHere` | 810 | 0 | 1 | $d_{\mathrm{form}}$ preserves logarithmic forms |
| `lem:sign-compatibility` | `lemma` | `ProvedHere` | 1024 | 1 | 0 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | `ProvedHere` | 1114 | 8 | 0 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | `ProvedHere` | 1301 | 3 | 0 | Pole decomposition of the bar differential |
| `thm:stokes-config` | `theorem` | `ProvedHere` | 1463 | 2 | 0 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | `ProvedHere` | 1563 | 0 | 0 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | `ProvedHere` | 1605 | 3 | 0 | Arnold relations |
| `cor:cohomology-config` | `corollary` | `ProvedElsewhere` | 1654 | 1 | 2 | Cohomology of configuration spaces {\cite{Arnold69}} |
| `comp:deg0` | `computation` | `ProvedHere` | 1670 | 0 | 0 | Degree 0 |
| `comp:deg1-general` | `computation` | `ProvedHere` | 1699 | 2 | 0 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | `ProvedHere` | 1942 | 1 | 0 | Bar construction is functorial |
| `thm:coassociativity-complete` | `theorem` | `ProvedHere` | 2054 | 0 | 0 | Coassociativity |
| `thm:counit-axioms` | `theorem` | `ProvedHere` | 2121 | 0 | 0 | Counit axioms |
| `thm:diff-is-coderivation` | `theorem` | `ProvedHere` | 2189 | 3 | 1 | Differential is coderivation |
| `lem:orientation` | `lemma` | `ProvedHere` | 2286 | 1 | 1 | Orientation convention |
| `lem:residue-properties` | `lemma` | `ProvedHere` | 2312 | 2 | 0 | Residue properties |
| `thm:geometric-equals-operadic-bar` | `theorem` | `ProvedHere` | 2647 | 2 | 3 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | `ProvedHere` | 2756 | 0 | 1 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | `ProvedElsewhere` | 2841 | 0 | 0 | Uniqueness and functoriality |
| `prop:dgla-axioms-k3-convolution` | `proposition` | `ProvedHere` | 3100 | 2 | 0 | dGLA axioms for $\mathfrak{C}_{\mathbf{H}_{\Delta_5}}$ |
| `thm:MC-hbar3-hbar4-k3` | `theorem` | `ProvedHere` | 3196 | 2 | 0 | Finite Maurer--Cartan window at $\hbar^3,\hbar^4$ |
| `thm:MC-hbar7-hbar12-k3` | `theorem` | `ProvedHere` | 3229 | 1 | 0 | Finite Maurer--Cartan criterion through $\hbar^{12}$ |
| `lem:bc-polar-support-phi-K3` | `lemma` | `ProvedElsewhere` | 3289 | 0 | 0 | Polar support of the K3 elliptic genus |

#### `chapters/theory/chern_weil_level_shift_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:level-shift-universality` | `theorem` | `ProvedHere` | 191 | 2 | 0 | Level-shift universality with convention separation |
| `prop:shift-appears-universally` | `proposition` | `ProvedHere` | 301 | 1 | 0 | Universal occurrence of $k + \hv$ |
| `thm:h-dual-coxeter-coincidence` | `theorem` | `ProvedHere` | 395 | 2 | 0 | Dual Coxeter coincidence |
| `thm:trace-KZ-convention-bridge` | `theorem` | `ProvedHere` | 473 | 4 | 0 | Trace--KZ convention bridge |
| `cor:level-shift-universal-convention-bridge` | `corollary` | `ProvedHere` | 560 | 3 | 0 | $r$-matrix convention bridge with explicit $k=0$ check |

#### `chapters/theory/chiral_center_theorem.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:partial-comp-assoc` | `lemma` | `ProvedHere` | 251 | 1 | 0 | Associativity of partial compositions |
| `prop:geometric-algebraic-hochschild` | `proposition` | `ProvedHere` | 376 | 5 | 0 | Geometric--algebraic comparison for chiral Hochschild |
| `prop:pre-lie-chiral` | `proposition` | `ProvedHere` | 705 | 1 | 0 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | `ProvedHere` | 733 | 2 | 0 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | `ProvedHere` | 754 | 1 | 0 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | `ProvedHere` | 1403 | 2 | 0 | Chiral Deligne--Tamarkin |
| `prop:heisenberg-bv-structure` | `proposition` | `ProvedHere` | 2557 | 1 | 1 | BV algebra structure on $H^*(Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k))$ |
| `prop:chirhoch-cdr` | `proposition` | `ProvedElsewhere` | 2667 | 0 | 1 | Chiral Hochschild cohomology of commutative chiral algebras {\cite{MSV99}} |

#### `chapters/theory/chiral_climax_platonic.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:arnold-cohomology-platonic` | `theorem` | `ProvedElsewhere` | 151 | 1 | 0 | Arnold 1969 |
| `prop:arnold-flatness-platonic` | `proposition` | `ProvedElsewhere` | 202 | 2 | 0 | Arnold flatness |
| `lem:fm-residue-dbar-platonic` | `lemma` | `ProvedElsewhere` | 602 | 1 | 0 | FM residue presentation of $\dbar$ |
| `lem:pullback-presentation-nabla-platonic` | `lemma` | `ProvedHere` | 620 | 4 | 0 | Pullback presentation of $\nabla(A)$ |
| `thm:kohno-monodromy-platonic` | `theorem` | `ProvedElsewhere` | 667 | 1 | 0 | Kohno 1987 |
| `thm:drinfeld-associator-platonic` | `theorem` | `ProvedElsewhere` | 702 | 0 | 0 | Drinfeld $1989$ |
| `prop:cybe-equivalence-platonic` | `proposition` | `ProvedHere` | 735 | 3 | 0 | CYBE equivalence |
| `cor:climax-drinfeld-kohno-platonic` | `corollary` | `ProvedHere` | 769 | 2 | 0 | Drinfeld--Kohno from the climax |
| `cor:climax-borcherds-platonic` | `corollary` | `ProvedHere` | 824 | 2 | 0 | Borcherds product from the climax |
| `cor:climax-arnold-common-root-platonic` | `corollary` | `ProvedHere` | 855 | 3 | 0 | Arnold $1969$ as common root |
| `prop:cclimax-SK-spinor` | `proposition` | `ProvedHere` | 1704 | 1 | 0 | Saito--Kurokawa spinor Euler factors of $\Delta_{10}$ at $p \le 37$ |
| `rem:cclimax-ap-extension` | `remark` | `ProvedHere` | 1833 | 0 | 0 | First-principles $a_p(f_{18})$ for $p$ up to $79$, verified three independent ways |
| `rem:cclimax-sk-euler` | `remark` | `ProvedHere` | 1863 | 0 | 0 | Saito--Kurokawa Hecke eigenvalues and Euler factor at $s = 9.5$ |
| `rem:cclimax-monster-lusztig-conway-norton` | `remark` | `ProvedElsewhere` | 1931 | 0 | 0 | Monster Lusztig level $\ell_{\mathrm{Monster}} = 2$: Vol~I mirror of the Conway--Norton normalisation |
| `rem:cclimax-ap-extension-ii` | `remark` | `ProvedHere` | 2016 | 0 | 1 | First-principles $a_p(f_{18})$ extension for $p\in\{83, 89, 97, 101, 103, 107, 109, 113\}$ |
| `rem:cclimax-ap-extension-iii` | `remark` | `ProvedHere` | 2076 | 2 | 1 | First-principles $a_p(f_{18})$ extension for $p\in\{127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199\}$ |

#### `chapters/theory/chiral_hochschild_koszul.tex` (22)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | `ProvedHere` | 269 | 2 | 1 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | `ProvedHere` | 420 | 3 | 0 | chiral Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | `ProvedHere` | 480 | 1 | 0 | chiral Hochschild spectral sequence |
| `thm:boson-fermion-lattice` | `theorem` | `ProvedElsewhere` | 3446 | 0 | 1 | Boson-fermion correspondence via lattice VOA; {} \cite{FK80} |
| `comp:boson-hochschild` | `computation` | `ProvedHere` | 3502 | 0 | 0 | Boson chiral Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | `ProvedHere` | 3532 | 1 | 1 | Fermion chiral Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | `ProvedHere` | 3638 | 2 | 2 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | `ProvedHere` | 3732 | 1 | 0 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `prop:modular-deformation-truncation` | `proposition` | `ProvedHere` | 4034 | 1 | 0 | Genus truncation |
| `prop:fay-trisecant` | `proposition` | `ProvedElsewhere` | 4481 | 0 | 1 | Fay trisecant identity for the Szeg\H{o} kernel {\cite[Corollary~2.5 |
| `prop:stokes-regularity-FM` | `proposition` | `ProvedHere` | 4508 | 1 | 5 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | `ProvedHere` | 4594 | 6 | 1 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | `ProvedHere` | 4713 | 2 | 0 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | `ProvedHere` | 4899 | 1 | 2 | Strictification principle for modular deformation theory |
| `prop:non-scalar-criterion` | `proposition` | `ProvedHere` | 5916 | 1 | 0 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | `ProvedHere` | 6084 | 0 | 0 | Denominator obstruction to stabilization |
| `thm:geometric-depth-smooth` | `theorem` | `ProvedHere` | 6409 | 0 | 2 | Sharp geometric depth on smooth moduli |
| `thm:string-field-theory-hochschild` | `theorem` | `ProvedElsewhere` | 6827 | 0 | 1 | String field theory from Hochschild {\cite{Zwi93}} |
| `thm:HH-config-space-formula` | `theorem` | `ProvedHere` | 6978 | 3 | 0 | Fulton--MacPherson model for chiral Hochschild cochains |
| `prop:hochschild-cech-ss` | `proposition` | `ProvedHere` | 7579 | 0 | 0 | chiral Hochschild--\v{C}ech spectral sequence |
| `conj:ambient-self-duality` | `proposition` | `ProvedHere` | 7750 | 1 | 0 | Self-duality of the kernel fibre |
| `conj:one-sided-isotropy` | `proposition` | `ProvedHere` | 7789 | 1 | 0 | One-sided isotropy criterion |

#### `chapters/theory/chiral_koszul_pairs.tex` (28)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:filtered-comparison` | `lemma` | `ProvedHere` | 661 | 0 | 1 | Filtered comparison |
| `cor:three-bijections` | `corollary` | `ProvedHere` | 816 | 0 | 1 | Three bijections for chiral twisting morphisms |
| `prop:bar-universal-property` | `proposition` | `ProvedElsewhere` | 907 | 0 | 1 | Universal property of bar construction {\cite{LV12}} |
| `thm:chiral-comparison-lemma` | `theorem` | `ProvedElsewhere` | 940 | 0 | 1 | Comparison lemma for chiral twisted products {\cite[Theorem~2.4.1 |
| `thm:pbw-koszulness-criterion` | `theorem` | `ProvedHere` | 1170 | 5 | 0 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | `ProvedHere` | 1253 | 6 | 1 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | `ProvedHere` | 1308 | 5 | 0 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | `ProvedHere` | 1352 | 6 | 0 | Bar cohomology computes the bar-dual coalgebra |
| `prop:ainfty-formality-implies-koszul` | `proposition` | `ProvedHere` | 1666 | 1 | 2 | Formality implies chiral Koszulness |
| `thm:ext-diagonal-vanishing` | `theorem` | `ProvedHere` | 1774 | 1 | 1 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | `ProvedHere` | 1811 | 2 | 0 | PBW universality |
| `prop:li-bar-poisson-differential` | `proposition` | `ProvedHere` | 2322 | 1 | 0 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | `ProvedHere` | 2393 | 4 | 0 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | `ProvedHere` | 2495 | 1 | 0 | Nilradical obstruction at degenerate admissible levels |
| `prop:d-module-purity-km` | `proposition` | `ProvedHere` | 4014 | 0 | 0 | $\cD$-module purity for affine Kac--Moody under localization weights |
| `prop:minimal-model-non-koszul` | `proposition` | `ProvedHere` | 5106 | 0 | 0 | Minimal model non-Koszulness |
| `prop:cumulant-window-inversion` | `proposition` | `ProvedHere` | 5304 | 0 | 0 | Cumulant-to-window inversion |
| `thm:yangian-self-dual` | `theorem` | `ProvedHere` | 5796 | 2 | 0 | Type-A Yangian quadratic shadow |
| `prop:yangian-koszul-general` | `proposition` | `ProvedHere` | 5863 | 1 | 5 | Yangian ordered-bar Koszulness in finite windows |
| `thm:coalgebra-axioms-verified` | `theorem` | `ProvedHere` | 6035 | 2 | 0 | Coalgebra structure on \texorpdfstring{$\mathcal{A}^{\mathrm i}_{\mathrm{cand}}$}{A-i-cand} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | `ProvedHere` | 6102 | 4 | 0 | Bar computes the intrinsic bar-dual coalgebra |
| `lem:completion-convergence` | `lemma` | `ProvedHere` | 6176 | 0 | 1 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | `ProvedHere` | 6212 | 7 | 0 | Circularity-free Koszul duality |
| `lem:operadic-koszul-transfer` | `lemma` | `ProvedElsewhere` | 6788 | 0 | 2 | Operadic Koszulness transfer \cite{LV12} |
| `prop:bar-neq-quasiprimary` | `proposition` | `ProvedHere` | 7203 | 2 | 0 | Bar cohomology $\neq$ quasi-primary count |
| `thm:structure-exchange` | `theorem` | `ProvedHere` | 7374 | 1 | 0 | Structure exchange on the finite quadratic lane |
| `thm:ainfty-duality-exchange` | `theorem` | `ProvedHere` | 7442 | 1 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} operations under Verdier pairing |
| `prop:ff-involution-uniqueness` | `proposition` | `ProvedHere` | 7494 | 1 | 0 | Uniqueness of the Feigin--Frenkel involution |

#### `chapters/theory/chiral_modules.tex` (39)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fock-fusion-product` | `proposition` | `ProvedHere` | 239 | 1 | 1 | Fusion product of Heisenberg Fock modules |
| `prop:conformal-blocks-bar` | `proposition` | `ProvedHere` | 686 | 3 | 0 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | `ProvedHere` | 818 | 7 | 0 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | `ProvedHere` | 930 | 2 | 0 | Dimension invariance on the finite-type Verdier surface |
| `prop:kzb-bar-complex` | `proposition` | `ProvedHere` | 995 | 2 | 0 | KZB connection from the bar complex |
| `thm:verlinde-bar` | `theorem` | `ProvedElsewhere` | 1059 | 6 | 1 | Verlinde formula via the bar complex {\cite{Verlinde}} |
| `prop:generic-irreducibility` | `proposition` | `ProvedElsewhere` | 1612 | 1 | 3 | Generic irreducibility {\cite{Kac,FF84}} |
| `thm:kazhdan-lusztig-equivalence` | `theorem` | `ProvedElsewhere` | 1713 | 0 | 3 | Kazhdan--Lusztig equivalence {\cite{KL93}} |
| `thm:bgg-reciprocity` | `theorem` | `ProvedElsewhere` | 1816 | 0 | 2 | BGG reciprocity for affine algebras {\cite{BGG76, KT95}} |
| `prop:tilting-bar` | `proposition` | `ProvedHere` | 1891 | 1 | 0 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | `ProvedHere` | 1956 | 4 | 0 | Verma module bar complex |
| `thm:zhu-correspondence` | `theorem` | `ProvedElsewhere` | 2107 | 0 | 1 | Zhu's correspondence {\cite{Zhu96}} |
| `cor:virasoro-zhu-koszul` | `corollary` | `ProvedHere` | 2224 | 0 | 1 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | `ProvedHere` | 2259 | 1 | 4 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `thm:arakawa-rationality` | `theorem` | `ProvedElsewhere` | 2348 | 1 | 2 | Arakawa's rationality criterion for admissible affine simples {\cite{Arakawa17,Zhu96}} |
| `lem:free-chiral-module-structure` | `lemma` | `ProvedHere` | 2755 | 0 | 0 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | `ProvedHere` | 2790 | 0 | 0 | Augmented module bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | `ProvedHere` | 2855 | 2 | 0 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | `ProvedHere` | 2872 | 0 | 0 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | `ProvedHere` | 2912 | 0 | 0 | Koszul dual coalgebras linearize module resolutions |
| `cor:character-koszul` | `corollary` | `ProvedHere` | 2968 | 1 | 0 | Character formula for Koszul case |
| `thm:ainfty-module` | `theorem` | `ProvedElsewhere` | 3007 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} module structure {\cite{Kadeishvili80}} |
| `thm:linfty-cochains` | `theorem` | `ProvedElsewhere` | 3046 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} structure on cochains {\cite{KontsevichSoibelman}} |
| `thm:chiral-gerstenhaber` | `theorem` | `ProvedElsewhere` | 3063 | 0 | 2 | Chiral Gerstenhaber algebra {\cite{Ger63,Tamarkin00}} |
| `thm:weyl-kac-denominator` | `theorem` | `ProvedElsewhere` | 3089 | 0 | 1 | Denominator identity for trivial module {\cite{Kac}} |
| `prop:bgg-sl2-level1` | `proposition` | `ProvedElsewhere` | 3419 | 0 | 1 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda-0)} {\cite{BGG76}} |
| `prop:shapovalov-koszul` | `proposition` | `ProvedHere` | 3875 | 1 | 1 | Shapovalov form under Koszul duality |
| `prop:virasoro-kac-koszul` | `proposition` | `ProvedHere` | 4154 | 0 | 2 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | `ProvedHere` | 4257 | 0 | 0 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | `ProvedHere` | 4316 | 0 | 2 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:4382` | `calculation` | `ProvedHere` | 4382 | 0 | 0 | Boson vacuum module |
| `thm:beilinson-bernstein` | `theorem` | `ProvedElsewhere` | 4494 | 0 | 1 | Beilinson--Bernstein {\cite{BB81}} |
| `thm:chiral-localization` | `theorem` | `ProvedElsewhere` | 4526 | 0 | 1 | Chiral localization {\cite{FG06}} |
| `prop:affine-hecke-kd` | `proposition` | `ProvedElsewhere` | 4636 | 1 | 2 | Affine Hecke algebra and Koszul duality {\cite{BGS96}} |
| `prop:bar-singular-support` | `proposition` | `ProvedHere` | 4690 | 1 | 1 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | `ProvedHere` | 4744 | 2 | 1 | DS reduction commutes with the module bar construction on the exact lane |
| `cor:ds-character-compatibility` | `corollary` | `ProvedHere` | 4877 | 1 | 0 | Characters under DS reduction |
| `thm:module-genus-tower` | `theorem` | `ProvedHere` | 5143 | 5 | 1 | Module tower from bar complex with insertions |
| `prop:heisenberg-fusion-splitting` | `proposition` | `ProvedHere` | 5614 | 3 | 0 | Heisenberg fusion splitting |

#### `chapters/theory/climax_theorem.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:climax-genus-zero` | `theorem` | `ProvedHere` | 43 | 0 | 0 | Climax of Vol~I, genus-zero form |
| `cor:climax-drinfeld-kohno` | `corollary` | `ProvedHere` | 124 | 0 | 0 | Drinfeld--Kohno along $A \mapsto U_q$ |
| `cor:climax-borcherds` | `corollary` | `ProvedHere` | 141 | 0 | 0 | Borcherds along $A \mapsto V_\Lambda$ |
| `cor:climax-verlinde` | `corollary` | `ProvedHere` | 157 | 0 | 0 | Verlinde along $A \mapsto \mathrm{RCFT}$ |

#### `chapters/theory/clutching_uniqueness_platonic.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:clutching-uniqueness-socle-projection` | `theorem` | `ProvedHere` | 220 | 2 | 3 | Clutching uniqueness on the socle |
| `cor:genus-2-explicit-match` | `corollary` | `ProvedHere` | 585 | 1 | 1 | Explicit match at genus $2$ |
| `lem:theorem-D-type-discipline` | `lemma` | `ProvedHere` | 837 | 0 | 0 | Type discipline in the identity $\mathrm{obs}_g=\kscal\cdot\lambda_g$ |
| `prop:theta-A-genus1` | `proposition` | `ProvedHere` | 893 | 2 | 2 | Genus-$1$ MC element |
| `prop:mc-direct-g1-verification` | `proposition` | `ProvedHere` | 1289 | 1 | 2 | $g=1$ direct MC verification |
| `prop:grr-verification-all-g` | `proposition` | `ProvedHere` | 1320 | 3 | 1 | GRR verification at all $g$ |

#### `chapters/theory/cobar_construction.tex` (24)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:schwartz-kernel-cobar` | `theorem` | `ProvedElsewhere` | 223 | 0 | 1 | Schwartz kernel theorem for cobar {\cite{Hormander}} |
| `lem:bar-holonomicity` | `lemma` | `ProvedHere` | 361 | 2 | 2 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | `ProvedHere` | 422 | 0 | 1 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | `ProvedHere` | 455 | 5 | 0 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | `ProvedHere` | 547 | 3 | 0 | Uncurved cobar nilpotence and curved square via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | `ProvedHere` | 710 | 0 | 0 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | `ProvedHere` | 841 | 3 | 0 | Uncurved distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | `ProvedHere` | 1098 | 0 | 0 | Sign consistency for the uncurved cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | `ProvedHere` | 1301 | 2 | 1 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | `ProvedHere` | 1569 | 2 | 1 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | `ProvedHere` | 1722 | 8 | 1 | Bar-cobar mutual inverses |
| `thm:kontsevich-formality` | `theorem` | `ProvedElsewhere` | 2048 | 0 | 1 | Kontsevich formality (1997) {\cite{Kon99}} |
| `thm:cobar-free` | `theorem` | `ProvedHere` | 2194 | 1 | 0 | Cobar as free chiral algebra |
| `lem:cobar-derivation-extension` | `lemma` | `ProvedHere` | 2417 | 2 | 1 | Cobar derivation extension |
| `thm:weak-topology` | `theorem` | `ProvedHere` | 2671 | 0 | 0 | Topology |
| `thm:cobar-ainfty` | `theorem` | `ProvedElsewhere` | 2856 | 0 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} structure on cobar {\cite{LV12}} |
| `thm:curved-mc-cobar` | `theorem` | `ProvedHere` | 2904 | 3 | 2 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | `ProvedHere` | 2954 | 1 | 0 | Affine modular curvature scalar |
| `thm:central-charge-cocycle` | `theorem` | `ProvedHere` | 3218 | 1 | 0 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | `ProvedHere` | 3324 | 3 | 0 | Genus 1 cobar extraction of the Heisenberg central extension |
| `thm:bar-complex-spectral-sequence` | `theorem` | `ProvedHere` | 3571 | 2 | 2 | Bar complex spectral sequence |
| `cor:spectral-degeneration` | `corollary` | `ProvedElsewhere` | 3656 | 1 | 1 | Degeneration {\cite{BGS96}} |
| `thm:koszul-necessary` | `theorem` | `ProvedElsewhere` | 4013 | 0 | 1 | Necessary conditions for chiral Koszul duality {\cite{FG12}} |
| `lem:deformation-space` | `lemma` | `ProvedHere` | 4267 | 1 | 0 | Deformation space under center transport |

#### `chapters/theory/coderived_models.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:conilpotent-reduction` | `theorem` | `ProvedElsewhere` | 132 | 1 | 1 | Conilpotent reduction |

#### `chapters/theory/compact_completed_mc3_comparison_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:compact-completed-mc3-comparison` | `theorem` | `ProvedHere` | 165 | 3 | 0 | Compact/completed MC3 comparison |
| `prop:compact-approximation-exists` | `proposition` | `ProvedHere` | 306 | 2 | 0 | Finite-window approximation exists |
| `lem:dense-thick-generation-lifting` | `lemma` | `ProvedElsewhere` | 398 | 0 | 0 | Finite-window dense generation lifting |
| `thm:mc3-full-DK-in-completed-category` | `theorem` | `ProvedHere` | 433 | 3 | 0 | MC3 generation in the completed finite-window category |
| `cor:comparison-gap-resolved-completed` | `corollary` | `ProvedHere` | 487 | 4 | 0 | Compact/completed comparison inside the finite-window ambient |

#### `chapters/theory/computational_methods.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:comp-denom-pattern` | `theorem` | `ProvedHere` | 177 | 1 | 0 | Denominator theorem |
| `prop:comp-shadow-connection-properties` | `proposition` | `ProvedHere` | 227 | 0 | 0 | Properties of the shadow connection |
| `thm:comp-shadow-asymptotics` | `theorem` | `ProvedHere` | 354 | 0 | 0 | Shadow asymptotics |
| `prop:comp-borel-summability` | `proposition` | `ProvedHere` | 454 | 0 | 0 | Borel summability |
| `prop:comp-mc-recursion` | `proposition` | `ProvedHere` | 504 | 0 | 0 | MC recursion |
| `thm:comp-alg-rec-equivalence` | `theorem` | `ProvedHere` | 533 | 2 | 0 | Algebraic--recursive equivalence |
| `thm:comp-ds-consistency` | `theorem` | `ProvedHere` | 600 | 3 | 0 | DS transfer consistency |
| `prop:comp-ce-bar` | `proposition` | `ProvedHere` | 705 | 1 | 0 | CE reduction |
| `thm:comp-zhu-c-dependence` | `theorem` | `ProvedHere` | 739 | 0 | 0 | $c$-dependence for simple quotients |
| `thm:comp-three-way-bar` | `theorem` | `ProvedHere` | 832 | 3 | 0 | Three-way agreement for bar cohomology |
| `prop:comp-explicit-theta-sl2` | `proposition` | `ProvedHere` | 870 | 0 | 0 | Explicit $\Theta$ for $\AffKM{sl}_2$ |
| `thm:comp-siegel-weil-e8` | `theorem` | `ProvedElsewhere` | 981 | 0 | 0 | Siegel--Weil for $E_8$ |
| `thm:comp-e8-three-way` | `theorem` | `ProvedHere` | 1013 | 0 | 0 | $E_8$ genus-$2$ agreement |
| `prop:comp-n2-kappa` | `proposition` | `ProvedHere` | 1165 | 0 | 0 | Modular characteristic |
| `prop:comp-n2-spectral-flow` | `proposition` | `ProvedHere` | 1228 | 0 | 0 | Spectral flow invariance |
| `thm:comp-genus2-cross` | `theorem` | `ProvedHere` | 1276 | 0 | 0 | Cross-consistency at genus~$2$ |
| `thm:s3-virasoro-c-independent` | `theorem` | `ProvedHere` | 1514 | 0 | 0 | $c$-independence of $S_3$ for Virasoro |

#### `chapters/theory/configuration_spaces.tex` (62)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:FM` | `theorem` | `ProvedElsewhere` | 249 | 0 | 1 | Fulton--MacPherson compactification at genus \texorpdfstring{$g$}{g} \cite{FM94} |
| `thm:boundary-higher-genus` | `theorem` | `ProvedElsewhere` | 422 | 2 | 2 | Boundary strata of \texorpdfstring{$\overline{\mathcal{M}}_{g,n}$}{M-bar(g,n)} {\cite{DeligneM69,Knudsen83}} |
| `thm:local-coords-boundary` | `theorem` | `ProvedHere` | 548 | 0 | 0 | Local holomorphic coordinates near a collision divisor |
| `thm:normal-crossings` | `theorem` | `ProvedHere` | 637 | 0 | 0 | Normal crossings |
| `thm:closure-relations` | `theorem` | `ProvedHere` | 747 | 0 | 0 | Closure relations |
| `cor:dimension-strata` | `corollary` | `ProvedElsewhere` | 778 | 0 | 1 | Boundary divisors in the FM compactification \cite{FM94} |
| `thm:boundary-stratification` | `theorem` | `ProvedElsewhere` | 800 | 0 | 1 | Boundary stratification \cite{FM94} |
| `thm:log-complex` | `theorem` | `ProvedHere` | 876 | 0 | 1 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | `ProvedHere` | 914 | 4 | 1 | Arnold relations and KZ flatness |
| `prop:arnold-higher-genus` | `proposition` | `ProvedHere` | 1046 | 5 | 4 | Higher-genus correction to the Arnold-only presentation |
| `prop:twisting-morphism-propagator` | `proposition` | `ProvedHere` | 1355 | 4 | 0 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | `ProvedHere` | 1431 | 1 | 0 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | `ProvedHere` | 1470 | 2 | 0 | Residue operations |
| `prop:residue-local` | `proposition` | `ProvedHere` | 1540 | 1 | 0 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | `ProvedHere` | 1626 | 1 | 0 | Residue sequence |
| `thm:FM-functorial` | `theorem` | `ProvedElsewhere` | 1673 | 0 | 1 | Functoriality of FM compactification |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1694` | `remark` | `ProvedElsewhere` | 1694 | 0 | 1 | Provenance and citation |
| `thm:FM-operad` | `theorem` | `ProvedElsewhere` | 1701 | 0 | 2 | Universal property: FM right-module structure {\cite{FM94,LV12}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1722` | `remark` | `ProvedElsewhere` | 1722 | 0 | 2 | Provenance and citation |
| `thm:fact-homology` | `theorem` | `ProvedElsewhere` | 1744 | 0 | 3 | Factorization homology via configuration spaces {\cite{AF15,CG17,BD04}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1758` | `remark` | `ProvedElsewhere` | 1758 | 0 | 3 | Provenance and citation |
| `thm:bordered-fm-properties` | `theorem` | `ProvedHere` | 2419 | 2 | 0 | Properties of the bordered FM compactification |
| `lem:nested-blowup-commutativity` | `lemma` | `ProvedElsewhere` | 2497 | 0 | 1 | Nested blowup commutativity |
| `prop:four-type-boundary` | `proposition` | `ProvedHere` | 2518 | 2 | 0 | Four-type boundary decomposition |
| `prop:fundamental-group-genera` | `proposition` | `ProvedElsewhere` | 3589 | 0 | 2 | Fundamental group across genera \cite{Arnold69,Brieskorn73} |
| `thm:fm-associahedron` | `theorem` | `ProvedElsewhere` | 3699 | 0 | 1 | FM compactification and associahedra {\cite{Sta63}} |
| `prop:eta` | `proposition` | `ProvedHere` | 3706 | 1 | 0 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:os-cohomology-config` | `theorem` | `ProvedElsewhere` | 3751 | 0 | 2 | Cohomology via Orlik--Solomon {\cite{Arnold69,OS80}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3765` | `remark` | `ProvedElsewhere` | 3765 | 0 | 2 | Provenance and citation |
| `thm:NBC` | `theorem` | `ProvedElsewhere` | 3792 | 0 | 1 | NBC basis theorem {\cite{OS80}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3801` | `remark` | `ProvedElsewhere` | 3801 | 0 | 1 | Provenance and citation |
| `thm:chiral-as-fact` | `theorem` | `ProvedElsewhere` | 3920 | 0 | 1 | Chiral algebras as factorization algebras \cite{BD04} |
| `thm:fact-monoidal-corrected` | `theorem` | `ProvedElsewhere` | 3938 | 0 | 2 | Factorization monoidal structure {\cite{BD04,CG17}} |
| `thm:elliptic-compactification` | `theorem` | `ProvedElsewhere` | 3981 | 0 | 1 | Elliptic compactification {\cite{Fay73}} |
| `prop:elliptic-arnold-relations` | `proposition` | `ProvedElsewhere` | 4018 | 0 | 1 | Elliptic correction to the Arnold relation \cite{Fay73} |
| `lem:orientation-compatibility` | `lemma` | `ProvedHere` | 4195 | 0 | 0 | Orientation compatibility |
| `thm:stokes-config-spaces` | `theorem` | `ProvedElsewhere` | 4221 | 0 | 1 | Stokes on configuration spaces \cite{FM94} |
| `prop:operadic-structure` | `proposition` | `ProvedHere` | 4256 | 0 | 0 | Operadic structure |
| `thm:chiral-algebra-objects` | `theorem` | `ProvedElsewhere` | 4282 | 0 | 1 | Chiral algebras as algebra objects \cite{BD04} |
| `thm:nbc-basis-optimality` | `theorem` | `ProvedHere` | 4296 | 3 | 0 | Exact NBC reduction for the affine OS component |
| `prop:nbc-sparsity` | `proposition` | `ProvedHere` | 4354 | 0 | 0 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | `ProvedHere` | 4376 | 2 | 1 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | `ProvedHere` | 4416 | 2 | 0 | Arnold relations on affine boundary screens |
| `thm:permutohedral-cell-complex` | `theorem` | `ProvedHere` | 4454 | 0 | 0 | Permutohedral cell complex of the compactified real line |
| `thm:complexity-bounds` | `theorem` | `ProvedHere` | 4516 | 0 | 0 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | `ProvedHere` | 4539 | 2 | 0 | Finite-window spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | `ProvedHere` | 4600 | 2 | 0 | Residue evaluation complexity |
| `thm:arnold-jacobi` | `theorem` | `ProvedElsewhere` | 4729 | 3 | 1 | Arnold relation $\Leftrightarrow$ simple-pole Jacobi on the affine screen \cite{LV12} |
| `cor:arnold-operadic` | `corollary` | `ProvedElsewhere` | 4760 | 0 | 1 | Operadic associativity \cite{LV12} |
| `thm:arnold-orlik-solomon` | `theorem` | `ProvedHere` | 4770 | 0 | 0 | Arnold--Orlik--Solomon circuit relations |
| `cor:bar-d-squared-zero` | `corollary` | `ProvedHere` | 4803 | 2 | 0 | Bar differential squares to zero |
| `thm:elliptic-logarithmic-forms` | `theorem` | `ProvedElsewhere` | 4820 | 0 | 1 | Elliptic logarithmic forms \cite{Fay73} |
| `thm:normal-crossings-preservation` | `theorem` | `ProvedHere` | 4838 | 1 | 1 | Normal crossings preservation |
| `thm:complete-coordinates` | `theorem` | `ProvedHere` | 5076 | 0 | 0 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | `ProvedHere` | 5129 | 0 | 0 | Normal bundle formula |
| `prop:transition-functions` | `proposition` | `ProvedElsewhere` | 5198 | 0 | 1 | Transition functions \cite{FM94} |
| `thm:normal-crossings-verified` | `theorem` | `ProvedHere` | 5276 | 0 | 0 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5487` | `computation` | `ProvedElsewhere` | 5487 | 0 | 0 | Explicit examples |
| `thm:chiral-ran-Dmod` | `theorem` | `ProvedElsewhere` | 5608 | 0 | 2 | Chiral algebras ↔ D-modules on Ran space {\cite{BD04,FG12}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5614` | `remark` | `ProvedElsewhere` | 5614 | 0 | 3 | Provenance and citation |
| `thm:chiral-homology-ran` | `theorem` | `ProvedElsewhere` | 5624 | 0 | 2 | Chiral homology via Ran space {\cite{BD04,CG17}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5632` | `remark` | `ProvedElsewhere` | 5632 | 0 | 3 | Provenance and citation |

#### `chapters/theory/conformal_anomaly_rigidity_platonic.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:casimir-nonvanishing` | `lemma` | `ProvedHere` | 165 | 0 | 2 | Nonvanishing and integrality of $\Cas$ |
| `thm:conformal-anomaly-rigidity` | `theorem` | `ProvedHere` | 209 | 3 | 0 | Conformal-anomaly rigidity |
| `thm:c-zero-coproduct-is-constant` | `theorem` | `ProvedHere` | 267 | 2 | 4 | Coproduct is constant at $c = 0$ |
| `prop:spectral-parameter-forced-at-nonzero-c` | `proposition` | `ProvedHere` | 305 | 3 | 0 | Spectral parameter is forced at $c \neq 0$ |
| `thm:universal-coefficient` | `theorem` | `ProvedHere` | 329 | 1 | 0 | Universality of the coefficient |
| `cor:chiralization-obstructed-away-from-c-zero` | `corollary` | `ProvedHere` | 370 | 4 | 0 | Chiralisation is obstructed away from $c = 0$ |
| `rem:comparison-with-ktheory-anomaly` | `remark` | `ProvedElsewhere` | 396 | 1 | 0 | Comparison with the Virasoro \texorpdfstring{$\kappa$}{kappa}-conductor |

#### `chapters/theory/derived_langlands.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:ff-center-dl` | `theorem` | `ProvedElsewhere` | 302 | 0 | 2 | Feigin--Frenkel center |
| `thm:kl-equivalence` | `theorem` | `ProvedElsewhere` | 1167 | 0 | 2 | Kazhdan--Lusztig--Finkelberg equivalence on the semisimplified target |
| `thm:fg-localization` | `theorem` | `ProvedElsewhere` | 1412 | 0 | 1 | Frenkel--Gaitsgory localization |
| `thm:dl-pseudocharacter-delta10` | `theorem` | `ProvedHere` | 3431 | 4 | 0 | Four-dimensional Chenevier determinant on $\Tpar_1$ for $\Delta_{10}$ |
| `thm:dl-chenevier-nonreduced-delta5` | `theorem` | `ProvedHere` | 3695 | 1 | 0 | Chenevier determinant on the non-reduced deformation ring $R^{\mathrm{def}}_{\Delta_5}$ |

#### `chapters/theory/e1_modular_koszul.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | `ProvedHere` | 232 | 0 | 1 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | `ProvedHere` | 251 | 1 | 1 | — |
| `prop:e1-nonsplitting-obstruction` | `proposition` | `ProvedHere` | 444 | 1 | 2 | $E_1$ canonical section obstruction |
| `prop:e1-nonsplitting-genus1` | `proposition` | `ProvedHere` | 549 | 3 | 0 | $E_1$ genus-one modular-section obstruction |
| `prop:symmetric-descent-e1mkd` | `proposition` | `ProvedHere` | 984 | 0 | 0 | Symmetric descent |
| `cor:r-matrix-sigma2-symmetric` | `corollary` | `ProvedHere` | 1840 | 1 | 0 | $r$-matrix $\Sigma_2$-symmetry on the four archetypes |
| `thm:e1-formality-bridge` | `theorem` | `ProvedHere` | 2193 | 0 | 0 | Formality bridge |
| `thm:e1-formality-failure` | `theorem` | `ProvedHere` | 2232 | 1 | 0 | Formality failure for genuinely $\Eone$-chiral algebras |
| `thm:e1-mc-finite-degree` | `theorem` | `ProvedHere` | 2345 | 1 | 0 | $E_1$ MC equation at finite degree |
| `rem:ribbon-structure-count` | `remark` | `ProvedHere` | 2467 | 0 | 0 | Ribbon structure count |
| `prop:sn-irrep-decomposition-bar` | `proposition` | `ProvedHere` | 3337 | 0 | 1 | $\Sigma_n$-irreducible decomposition of the ordered bar complex |
| `lem:bare-graph-no-thooft` | `lemma` | `ProvedHere` | 3446 | 0 | 0 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | `ProvedHere` | 3467 | 0 | 0 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | `ProvedHere` | 3509 | 0 | 0 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | `ProvedHere` | 3531 | 1 | 0 | Exact $N^{\chi}$ weighting from traced open color |

#### `chapters/theory/en_koszul_duality.tex` (37)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:arnold-presentation` | `theorem` | `ProvedElsewhere` | 296 | 1 | 1 | Arnold presentation {\cite{Arnold69}}; \texorpdfstring{$\bC \cong \bR^2$}{C = R2} |
| `thm:totaro-presentation` | `theorem` | `ProvedElsewhere` | 313 | 0 | 2 | Totaro presentation, general \texorpdfstring{$n$}{n} {\cite{Totaro96, Coh76}} |
| `prop:fm-boundary-strata` | `proposition` | `ProvedElsewhere` | 398 | 0 | 2 | Boundary strata and operadic structure |
| `prop:linking-sphere-residue` | `proposition` | `ProvedHere` | 525 | 1 | 0 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | `ProvedHere` | 600 | 2 | 1 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `thm:en-koszul-duality` | `theorem` | `ProvedElsewhere` | 753 | 0 | 3 | \texorpdfstring{$\En$}{En} Koszul duality |
| `thm:af-pkd` | `theorem` | `ProvedElsewhere` | 854 | 0 | 1 | Poincar\'e--Koszul duality, AF {\cite{AF15}} |
| `thm:en-d-squared` | `theorem` | `ProvedElsewhere` | 964 | 1 | 1 | \texorpdfstring{$d^2 = 0$}{d squared = 0} for the \texorpdfstring{$\En$}{En} bar complex |
| `prop:kappa-universality-en` | `proposition` | `ProvedHere` | 1011 | 0 | 0 | Kappa universality across $n$ |
| `thm:knudsen-higher-enveloping` | `theorem` | `ProvedElsewhere` | 1117 | 0 | 1 | Higher enveloping algebras |
| `thm:e2-formality` | `theorem` | `ProvedElsewhere` | 1147 | 0 | 2 | Formality of \texorpdfstring{$\Etwo$}{E2} |
| `prop:en-formality` | `proposition` | `ProvedElsewhere` | 1182 | 1 | 2 | \texorpdfstring{$\En$}{En} formality for \texorpdfstring{$n \geq 2$}{n >= 2} |
| `thm:willwacher-wheels` | `theorem` | `ProvedElsewhere` | 1237 | 0 | 1 | Wheel cocycles and $\mathrm{grt}_1$ |
| `prop:shadow-gc2-bridge` | `proposition` | `ProvedHere` | 1260 | 1 | 0 | Shadow obstruction tower to $\mathrm{GC}_2$ bridge |
| `thm:bar-swiss-cheese` | `theorem` | `ProvedHere` | 1521 | 4 | 0 | Bar complex as $\Eone$-chiral coassociative coalgebra |
| `prop:sc-koszul-dual-three-sectors` | `proposition` | `ProvedHere` | 1829 | 1 | 0 | Koszul dual cooperad of \texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}: three sectors |
| `cor:convolution-factorization` | `corollary` | `ProvedHere` | 1871 | 2 | 0 | Convolution algebra factorization |
| `prop:operadic-center-existence` | `proposition` | `ProvedHere` | 1983 | 1 | 0 | Existence of the operadic center |
| `thm:operadic-center-hochschild` | `theorem` | `ProvedHere` | 2036 | 7 | 2 | The operadic center of $\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex |
| `prop:braces-from-center` | `proposition` | `ProvedHere` | 2585 | 2 | 0 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | `ProvedHere` | 2634 | 5 | 1 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | `ProvedHere` | 2710 | 2 | 0 | Terminality of the center |
| `cor:center-functor` | `corollary` | `ProvedHere` | 2799 | 1 | 0 | The fiberwise center section |
| `thm:topologization` | `theorem` | `ProvedHere` | 3238 | 4 | 2 | Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}} |
| `thm:coset-conformal-inheritance` | `theorem` | `ProvedHere` | 4327 | 0 | 1 | Coset conformal inheritance |
| `prop:sugawara-gauge-rectification` | `proposition` | `ProvedHere` | 4474 | 6 | 1 | Chain-level $\Ethree^{\mathrm{top}}$ for affine Kac--Moody via gauge rectification |
| `prop:e3-via-dunn` | `proposition` | `ProvedHere` | 4951 | 4 | 3 | $\Ethree^{\mathrm{top}}$ via Dunn additivity, bypassing the Higher Deligne Conjecture |
| `thm:e3-cs` | `theorem` | `ProvedElsewhere` | 5125 | 1 | 2 | The $\Ethree$-algebra and Chern--Simons |
| `thm:cfg` | `theorem` | `ProvedElsewhere` | 5161 | 0 | 1 | Costello--Francis--Gwilliam~\cite{CFG25} |
| `lem:en-formality-deformation-classification` | `lemma` | `ProvedHere` | 5286 | 0 | 4 | Formality reduction for $\En$-deformations of commutative algebras |
| `prop:e3-explicit-sl2` | `proposition` | `ProvedHere` | 5898 | 5 | 0 | Explicit $\Ethree$ operations on $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\mathfrak{sl}_2))$ |
| `prop:chiral-p3-structure` | `proposition` | `ProvedHere` | 6440 | 1 | 1 | The chiral $\Pthree$ structure |
| `thm:chiral-e3-structure` | `theorem` | `ProvedHere` | 6527 | 7 | 3 | Structure of the chiral $\Ethree$-algebra |
| `lem:bv-p3-commutativity` | `lemma` | `ProvedHere` | 6788 | 3 | 0 | Commutativity of the BV operator and the chiral $\Pthree$ bracket |
| `prop:chiral-e3-dmod` | `proposition` | `ProvedHere` | 6929 | 1 | 1 | The $\cD$-module structure |
| `thm:chiral-e3-cfg` | `theorem` | `ProvedHere` | 7015 | 6 | 0 | Formal disk restriction recovers CFG |
| `prop:khan-zeng-topological` | `proposition` | `ProvedHere` | 7233 | 3 | 2 | Topological enhancement via Sugawara |

#### `chapters/theory/existence_criteria.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:existence-four-loci` | `proposition` | `ProvedHere` | 155 | 1 | 0 | Four loci in the existence problem |
| `prop:recognition-not-existence` | `proposition` | `ProvedHere` | 226 | 0 | 0 | Recognition targets are not existence criteria |
| `thm:quadratic-have-duals` | `theorem` | `ProvedElsewhere` | 271 | 1 | 2 | Quadratic finite-dual coalgebras exist \cite{LV12, Priddy70} |
| `thm:completed-koszul-dual` | `theorem` | `ProvedElsewhere` | 561 | 0 | 1 | Completed Koszul dual \cite{Positselski11} |
| `prop:finite-stage-obstruction-classes` | `proposition` | `ProvedHere` | 641 | 1 | 0 | Finite-stage obstruction classes |
| `thm:completion-convergence-criteria` | `theorem` | `ProvedHere` | 773 | 0 | 0 | Finite-window convergence criterion |
| `prop:kac-moody-koszul-duals` | `proposition` | `ProvedElsewhere` | 1051 | 1 | 2 | Affine Kac--Moody existence criterion \cite{FBZ04, Feigin-Frenkel} |

#### `chapters/theory/fourier_seed.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | `ProvedHere` | 61 | 0 | 0 | Three properties of the propagator |
| `prop:fourier-com-lie-duality` | `proposition` | `ProvedHere` | 222 | 0 | 0 | — |
| `comp:fourier-heisenberg-n2` | `computation` | `ProvedHere` | 269 | 2 | 0 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | `ProvedHere` | 318 | 2 | 0 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | `ProvedHere` | 347 | 4 | 0 | Heisenberg bar seed |
| `prop:fourier-propagator-degeneration` | `proposition` | `ProvedHere` | 560 | 0 | 2 | Degeneration of the propagator |
| `comp:fourier-km-bar` | `computation` | `ProvedHere` | 806 | 0 | 0 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | `ProvedHere` | 827 | 1 | 1 | — |
| `thm:fourier-specialization` | `theorem` | `ProvedHere` | 871 | 0 | 1 | Specialization |

#### `chapters/theory/genus_2_ddybe_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:genus-2-kzb-connection-platonic` | `theorem` | `ProvedElsewhere` | 167 | 0 | 2 | Flat KZB connection on $\overline{\cM}_{2,n}\times\HHH_2$ |
| `thm:fay-trisecant-genus-2-specific` | `theorem` | `ProvedElsewhere` | 252 | 1 | 1 | Fay trisecant, three-term Szeg\H{o} form |
| `cor:g2-chi-minus-12` | `corollary` | `ProvedHere` | 650 | 1 | 0 | $\chi=-12$ from rank-$4$ KZB local system |

#### `chapters/theory/higher_genus_complementarity.tex` (44)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:theorem-c-object-firewall` | `proposition` | `ProvedHere` | 205 | 0 | 0 | Object firewall for Theorem~C |
| `lem:involution-splitting` | `lemma` | `ProvedHere` | 378 | 0 | 0 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | `ProvedHere` | 434 | 2 | 0 | Perfectness criterion for the strict flat relative bar family |
| `lem:genus-filtration` | `lemma` | `ProvedHere` | 936 | 1 | 0 | Genus filtration |
| `thm:ss-quantum` | `theorem` | `ProvedHere` | 1000 | 3 | 0 | Spectral sequence for quantum corrections |
| `thm:verdier-duality-config-complete` | `theorem` | `ProvedHere` | 1271 | 2 | 1 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | `ProvedHere` | 1344 | 3 | 0 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | `ProvedHere` | 1384 | 5 | 0 | Spectral sequence duality |
| `thm:ss-genus-stratification` | `theorem` | `ProvedHere` | 2528 | 2 | 0 | External genus grading of the modular flat bar object |
| `cor:vanishing-quantum` | `corollary` | `ProvedHere` | 2731 | 1 | 0 | Vanishing results |
| `thm:fermion-boson-koszul-hg` | `theorem` | `ProvedHere` | 3145 | 0 | 0 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | `ProvedHere` | 3665 | 0 | 0 | BD 3.4.12: genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | `ProvedHere` | 3715 | 0 | 1 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | `ProvedHere` | 3728 | 0 | 2 | Normal crossings persist at higher genus |
| `lem:relative-diagonal` | `lemma` | `ProvedHere` | 3829 | 0 | 0 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | `ProvedHere` | 3869 | 0 | 1 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | `ProvedHere` | 3897 | 0 | 0 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | `ProvedHere` | 3919 | 1 | 0 | Chevalley--Cousin at boundary |
| `lem:graded-acyclic` | `lemma` | `ProvedHere` | 4206 | 0 | 1 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | `ProvedHere` | 4294 | 0 | 0 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | `ProvedHere` | 4321 | 4 | 1 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | `ProvedHere` | 4349 | 0 | 0 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | `ProvedHere` | 4385 | 0 | 1 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | `ProvedHere` | 4412 | 3 | 0 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | `ProvedHere` | 4473 | 1 | 1 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | `ProvedHere` | 4519 | 0 | 1 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | `ProvedHere` | 4558 | 1 | 0 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | `ProvedHere` | 4587 | 0 | 1 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | `ProvedHere` | 4615 | 0 | 0 | Algebra structure from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | `ProvedHere` | 4643 | 4 | 0 | Diagram commutes |
| `lem:extension-across-boundary-qi` | `lemma` | `ProvedHere` | 4750 | 0 | 0 | Extension across boundary |
| `lem:e2-collapse-higher-genus` | `lemma` | `ProvedHere` | 4884 | 1 | 0 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | `ProvedHere` | 4962 | 0 | 1 | Pants decomposition as excision |
| `thm:ambient-complementarity-tangent` | `theorem` | `ProvedHere` | 5274 | 0 | 0 | Ambient complementarity in tangent form |
| `prop:legendre-duality-potentials` | `proposition` | `ProvedHere` | 5802 | 0 | 0 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | `ProvedHere` | 5817 | 0 | 0 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | `ProvedHere` | 5847 | 0 | 0 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | `ProvedHere` | 5871 | 0 | 0 | Criterion for fake complementarity |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | `ProvedHere` | 6146 | 1 | 0 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | `ProvedHere` | 6232 | 0 | 0 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | `ProvedHere` | 6276 | 0 | 0 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | `ProvedHere` | 6353 | 4 | 0 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | `ProvedHere` | 6437 | 2 | 0 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | `ProvedHere` | 6506 | 1 | 0 | First nonlinear determinant anomaly |

#### `chapters/theory/higher_genus_foundations.tex` (53)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | `ProvedHere` | 1355 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | `ProvedHere` | 1455 | 0 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | `ProvedHere` | 1550 | 0 | 0 | Pentagon identity |
| `thm:higher-associahedron-m5` | `theorem` | `ProvedElsewhere` | 1588 | 0 | 1 | Higher associahedron identity for \texorpdfstring{$m_5$}{m5} {\cite{Sta63}} |
| `thm:catalan-parenthesization` | `theorem` | `ProvedElsewhere` | 1600 | 0 | 1 | Catalan identity at higher levels {\cite{Sta97}} |
| `thm:verdier-NAP` | `theorem` | `ProvedElsewhere` | 1632 | 1 | 2 | Verdier duality = NAP duality {\cite{AF15,KS90}} |
| `thm:cobar-ainfty-complete` | `theorem` | `ProvedHere` | 1722 | 2 | 1 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | `ProvedHere` | 1834 | 9 | 1 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | `ProvedHere` | 1981 | 0 | 0 | Verdier duality of operations |
| `thm:geometric-com-lie-enhancement` | `theorem` | `ProvedElsewhere` | 2068 | 0 | 1 | Geometric enhancement of Com-Lie |
| `thm:ainfty-com-lie-interchange` | `theorem` | `ProvedElsewhere` | 2106 | 0 | 1 | Maximal vs.\ trivial \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:cobar-resolution-scoped` | `theorem` | `ProvedElsewhere` | 2350 | 2 | 1 | Cobar resolution on the Koszul locus {\cite{LV12}} |
| `thm:genus-graded-mc` | `theorem` | `ProvedElsewhere` | 2410 | 2 | 2 | Maurer--Cartan = deformations {\cite{Kon03,Ger63}} |
| `prop:yangian-from-deformation` | `proposition` | `ProvedElsewhere` | 2438 | 0 | 1 | Yangian from deformation {\cite{Drinfeld85}} |
| `prop:deforming-heisenberg` | `proposition` | `ProvedHere` | 2465 | 1 | 0 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | `ProvedHere` | 2499 | 0 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | `ProvedHere` | 2533 | 0 | 0 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | `ProvedHere` | 2553 | 1 | 0 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | `ProvedHere` | 2569 | 1 | 0 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:moduli-structure` | `theorem` | `ProvedElsewhere` | 3158 | 0 | 2 | Structure of \texorpdfstring{$\overline{\mathcal{M}}_{g,n}$}{M-bar(g,n)} {\cite{DeligneM69,Knudsen83}} |
| `thm:universal-curve-fibration` | `theorem` | `ProvedElsewhere` | 3180 | 0 | 1 | Universal curve fibration {\cite{Knudsen83}} |
| `thm:period-matrix-properties` | `theorem` | `ProvedElsewhere` | 4060 | 0 | 1 | Properties of the period matrix {\cite{Fay73}} |
| `thm:theta-properties` | `theorem` | `ProvedElsewhere` | 4104 | 0 | 1 | Theta function properties {\cite{Fay73}} |
| `thm:prime-form-properties` | `theorem` | `ProvedElsewhere` | 4141 | 0 | 1 | Prime form properties {\cite{Fay73}} |
| `thm:modular-vs-quasi` | `theorem` | `ProvedElsewhere` | 4534 | 0 | 1 | Modular vs quasi-modular {\cite{KP84}} |
| `thm:theta-zero` | `theorem` | `ProvedElsewhere` | 4592 | 0 | 1 | Theta zero values {\cite{Fay73}} |
| `thm:eta-properties-genus1` | `theorem` | `ProvedHere` | 4617 | 0 | 0 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:genus1-d-squared` | `theorem` | `ProvedHere` | 4727 | 1 | 0 | Nilpotency at genus 1 |
| `thm:odd-even-g2` | `theorem` | `ProvedElsewhere` | 5038 | 0 | 1 | Odd vs even characteristics {\cite{Fay73}} |
| `thm:theta-g3` | `theorem` | `ProvedElsewhere` | 5172 | 0 | 1 | Theta characteristics at genus 3 {\cite{Fay73}} |
| `thm:mmm-classes` | `theorem` | `ProvedElsewhere` | 5378 | 0 | 2 | Tautological Hodge and boundary classes {\cite{Mumford83}} |
| `__unlabeled_chapters/theory/higher_genus_foundations.tex:5404` | `remark` | `ProvedElsewhere` | 5404 | 0 | 1 | Tautological scope |
| `thm:mumford-formula` | `theorem` | `ProvedElsewhere` | 5431 | 0 | 1 | Faber--Pandharipande $\lambda_g$ formula {\cite{FP03}} |
| `thm:obstruction-general` | `theorem` | `ProvedHere` | 5632 | 3 | 0 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | `ProvedHere` | 5686 | 0 | 1 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `prop:scalar-obstruction-hodge-euler` | `proposition` | `ProvedHere` | 6282 | 1 | 0 | Scalar obstruction equals Hodge Euler class |
| `lem:k-theoretic-globalization-bar` | `lemma` | `ProvedHere` | 6448 | 0 | 0 | $K$-theoretic globalization of the scalar bar class |
| `prop:lambda-g-clutching` | `proposition` | `ProvedHere` | 6851 | 2 | 0 | Clutching formulas for the Hodge Euler class |
| `prop:clutching-uniqueness` | `proposition` | `ProvedHere` | 6941 | 1 | 2 | Clutching uniqueness of the Hodge Euler class, socle scope |
| `prop:f2-quartic-dependence` | `proposition` | `ProvedHere` | 7873 | 1 | 0 | Genus-$2$ quartic dependence |
| `cor:kappa-periodicity` | `corollary` | `ProvedHere` | 7949 | 0 | 0 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `prop:bar-tautological-filtration` | `proposition` | `ProvedHere` | 8216 | 3 | 1 | Bar spectral sequence and tautological filtration |
| `lem:stable-graph-d-squared` | `lemma` | `ProvedHere` | 8781 | 0 | 0 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | `ProvedHere` | 8843 | 2 | 0 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | `ProvedHere` | 8881 | 1 | 0 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | `ProvedHere` | 8923 | 0 | 0 | Extremal pages |
| `thm:loop-order-collapse` | `theorem` | `ProvedHere` | 9173 | 3 | 0 | Loop-order convergence and finite-depth collapse bound |
| `cor:loop-decomposition-bar` | `corollary` | `ProvedHere` | 9219 | 1 | 0 | Associated graded by loop order |
| `thm:feynman-involution` | `theorem` | `ProvedElsewhere` | 9256 | 0 | 1 | Feynman involution \textup{\cite[Theorem~5.2 |
| `thm:virtual-euler-char` | `theorem` | `ProvedHere` | 9330 | 1 | 0 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | `ProvedHere` | 9358 | 0 | 2 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | `ProvedHere` | 9408 | 0 | 0 | Weight system map |
| `thm:log-clutching-degeneration` | `theorem` | `ProvedElsewhere` | 9607 | 0 | 1 | Logarithmic clutching from degeneration geometry |

#### `chapters/theory/higher_genus_modular_koszul.tex` (96)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:genus-window-ml-passage` | `lemma` | `ProvedHere` | 333 | 0 | 0 | Finite-window Mittag--Leffler passage |
| `thm:pbw-allgenera-principal-w` | `theorem` | `ProvedHere` | 920 | 8 | 0 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `lem:pbw-weightwise-g-module` | `lemma` | `ProvedHere` | 1062 | 0 | 0 | Weightwise reduction of the genus enrichment to \texorpdfstring{$\fg$}{g}-modules |
| `lem:pbw-mixed-factorization` | `lemma` | `ProvedHere` | 1121 | 1 | 0 | Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)} |
| `thm:pbw-genus1-km` | `theorem` | `ProvedHere` | 1169 | 7 | 1 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `thm:pbw-allgenera-km` | `theorem` | `ProvedHere` | 1511 | 8 | 0 | PBW degeneration at all genera for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | `ProvedHere` | 1775 | 8 | 0 | PBW degeneration at all genera for Virasoro |
| `thm:pbw-universal-semisimple` | `theorem` | `ProvedHere` | 1998 | 4 | 0 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `prop:hook-pbw` | `proposition` | `ProvedHere` | 2159 | 1 | 0 | Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses |
| `thm:pbw-propagation` | `theorem` | `ProvedHere` | 2251 | 4 | 0 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | `ProvedHere` | 2410 | 0 | 0 | Locality of the collision differential |
| `lem:e2-higher-genus` | `lemma` | `ProvedHere` | 2808 | 0 | 0 | $E_2$ collapse at higher genus |
| `prop:genus-completed-mc-framework` | `proposition` | `ProvedHere` | 6363 | 0 | 0 | Genus-completed MC algebra |
| `prop:cyclic-ce-identification` | `proposition` | `ProvedHere` | 6442 | 0 | 0 | Cyclic CE cohomology identification |
| `thm:convolution-dg-lie-structure` | `theorem` | `ProvedHere` | 11452 | 2 | 1 | dg~Lie structure from the modular operad |
| `thm:operadic-homotopy-convolution-modular` | `theorem` | `ProvedElsewhere` | 12116 | 1 | 3 | Operadic homotopy convolution {\cite[Theorem~4.1 |
| `cor:deformation-functoriality` | `corollary` | `ProvedElsewhere` | 12445 | 0 | 1 | Functoriality of the modular deformation functor {\cite[Theorem~5.1 |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | `ProvedHere` | 13092 | 2 | 1 | First two weights |
| `lem:shadow-bracket-well-defined` | `lemma` | `ProvedHere` | 13949 | 0 | 0 | Well-definedness of the descended bracket |
| `thm:ds-complementarity-tower-main` | `theorem` | `ProvedHere` | 14181 | 1 | 0 | DS complementarity tower |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | `ProvedHere` | 14986 | 1 | 0 | Stable-graph pronilpotent completion |
| `thm:finite-rank-spectral-reduction` | `theorem` | `ProvedHere` | 15037 | 3 | 0 | Finite-rank spectral reduction |
| `cor:metaplectic-square-root` | `corollary` | `ProvedHere` | 15444 | 2 | 0 | Determinantal half-density |
| `prop:critical-locus-complementarity` | `proposition` | `ProvedHere` | 16204 | 1 | 0 | Critical-locus form of complementarity |
| `lem:graph-sum-truncation` | `lemma` | `ProvedHere` | 16683 | 3 | 0 | Graph-sum truncation criterion |
| `prop:shadow-coefficient-rationality` | `proposition` | `ProvedHere` | 17929 | 0 | 0 | Shadow coefficient rationality |
| `cor:shadow-depth-koszul-invariance` | `corollary` | `ProvedHere` | 18600 | 0 | 0 | Shadow depth under Koszul duality |
| `cor:gaussian-decomposition` | `corollary` | `ProvedHere` | 19085 | 0 | 0 | Gaussian decomposition |
| `lem:depth-three-impossible` | `lemma` | `ProvedHere` | 19138 | 1 | 0 | Impossibility of $d_{\mathrm{alg}} = 3$ |
| `prop:hankel-extraction` | `proposition` | `ProvedHere` | 19444 | 1 | 0 | Hankel extraction of the quartic contact invariant |
| `cor:signed-shadow-measure` | `corollary` | `ProvedHere` | 19595 | 2 | 0 | Universal signed measure |
| `thm:shadow-epstein-zeta` | `theorem` | `ProvedHere` | 19677 | 2 | 2 | The Epstein zeta function of the shadow metric |
| `prop:t-line-autonomy` | `proposition` | `ProvedHere` | 21149 | 1 | 0 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | `ProvedHere` | 21206 | 2 | 0 | Inter-channel coupling on sublines |
| `cor:virasoro-shadow-radius` | `corollary` | `ProvedHere` | 21573 | 2 | 0 | Virasoro shadow growth rate |
| `prop:critical-cubic-convergence` | `proposition` | `ProvedHere` | 22050 | 3 | 0 | Critical cubic convergence threshold |
| `prop:virasoro-bottleneck` | `proposition` | `ProvedHere` | 22139 | 1 | 0 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | `ProvedHere` | 22366 | 1 | 0 | Koszul exchange of shadow regimes |
| `prop:koszul-conductor-wn` | `proposition` | `ProvedHere` | 22443 | 1 | 0 | Koszul conductor of \texorpdfstring{$\cW_N$}{WN} |
| `prop:propagator-universality` | `proposition` | `ProvedHere` | 22587 | 3 | 0 | Propagator universality |
| `cor:analytic-shadow-realization` | `corollary` | `ProvedHere` | 23569 | 2 | 0 | Analytic shadow realization |
| `rem:delta-f2-graph-decomposition` | `remark` | `ProvedHere` | 25104 | 1 | 0 | $\delta F_2$ graph-stratum decomposition |
| `comp:w3-genus3-cross` | `computation` | `ProvedHere` | 25160 | 2 | 0 | $\cW_3$ genus-$3$ cross-channel |
| `comp:w3-genus4-cross` | `computation` | `ProvedHere` | 25235 | 0 | 0 | $\cW_3$ genus-$4$ cross-channel |
| `comp:w4-full-ope-cross` | `computation` | `ProvedHere` | 25334 | 4 | 1 | $\cW_4$ full-OPE cross-channel correction |
| `rem:w4-irrational-cross-channel` | `remark` | `ProvedHere` | 25479 | 4 | 1 | $\cW_4$: the first irrational cross-channel correction |
| `comp:w5-full-ope-cross` | `computation` | `ProvedHere` | 25511 | 5 | 0 | $\cW_5$ full-OPE cross-channel correction |
| `prop:universal-gravitational-cross-channel` | `proposition` | `ProvedHere` | 25748 | 1 | 0 | Universal gravitational cross-channel formula for~$\cW_N$ |
| `rem:large-n-delta-f2-planar` | `remark` | `ProvedHere` | 26015 | 1 | 0 | Large-$N$ and 't~Hooft limit of $\delta F_2$ |
| `prop:cross-channel-growth` | `proposition` | `ProvedHere` | 26137 | 0 | 0 | Cross-channel growth |
| `prop:self-loop-vanishing` | `proposition` | `ProvedHere` | 27058 | 0 | 0 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | `ProvedHere` | 27094 | 1 | 0 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | `ProvedHere` | 27272 | 1 | 0 | Genus-$1$ two-point function from MC |
| `prop:dressed-propagator-resolution` | `proposition` | `ProvedHere` | 27647 | 1 | 0 | Dressed propagator coefficient and symmetry |
| `thm:pixton-mc-genus2` | `theorem` | `ProvedHere` | 28198 | 2 | 0 | Pixton--MC bridge at genus~$2$ |
| `thm:pixton-mc-genus3` | `theorem` | `ProvedHere` | 28261 | 3 | 0 | Pixton--MC bridge at genus~$3$ |
| `prop:mumford-from-mc-explicit` | `proposition` | `ProvedHere` | 28336 | 1 | 0 | Mumford formula from MC |
| `thm:spectral-curve-from-shadow` | `theorem` | `ProvedHere` | 28391 | 1 | 0 | Spectral curve from shadow metric |
| `thm:genus4-stable-graph-census` | `theorem` | `ProvedHere` | 28465 | 0 | 0 | Genus-$4$ stable graph census |
| `thm:genus4-free-energy` | `theorem` | `ProvedHere` | 28494 | 1 | 0 | Genus-$4$ free energy |
| `prop:genus4-spectral-sequence` | `proposition` | `ProvedHere` | 28515 | 0 | 0 | Genus-$4$ spectral sequence |
| `thm:bar-macmahon` | `theorem` | `ProvedHere` | 28564 | 0 | 0 | Bar--MacMahon correspondence |
| `prop:conifold-dt-gv` | `proposition` | `ProvedHere` | 28591 | 0 | 0 | Conifold DT and GV |
| `prop:tropical-shadow-amplitudes` | `proposition` | `ProvedHere` | 28642 | 0 | 0 | Tropical shadow amplitudes |
| `prop:tropical-period-theta` | `proposition` | `ProvedHere` | 28665 | 0 | 0 | Tropical theta function |
| `prop:fp-genus-decay-for-double` | `proposition` | `ProvedHere` | 28726 | 1 | 0 | Faber--Pandharipande genus decay |
| `prop:shadow-schwarzian` | `proposition` | `ProvedHere` | 29675 | 2 | 0 | Spectral Schr\"odinger potential |
| `cor:shadow-schrodinger-singularities` | `corollary` | `ProvedHere` | 29721 | 1 | 0 | Singularity classification |
| `prop:shadow-voros-classical` | `proposition` | `ProvedHere` | 29863 | 0 | 0 | Classical Voros period |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | `ProvedHere` | 30151 | 2 | 1 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:hgmk-finite-jet-rigidity` | `proposition` | `ProvedHere` | 30231 | 1 | 0 | Finite-jet rigidity |
| `prop:hgmk-polynomial-level-dependence` | `proposition` | `ProvedHere` | 30254 | 1 | 0 | Polynomial level dependence |
| `thm:cubic-gauge-triviality` | `theorem` | `ProvedHere` | 30401 | 1 | 0 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | `ProvedHere` | 30509 | 1 | 0 | Independent sum factorization |
| `prop:symn-kappa-linearity` | `proposition` | `ProvedHere` | 30567 | 3 | 2 | Symmetric orbifold kappa linearity |
| `rem:symmetric-orbifold-kappa` | `remark` | `ProvedHere` | 30648 | 2 | 1 | Symmetric orbifold kappa: four independent derivations |
| `prop:genus0-curve-independence` | `proposition` | `ProvedHere` | 31338 | 1 | 0 | Genus-$0$ curve-independence |
| `prop:chriss-ginzburg-structure` | `proposition` | `ProvedHere` | 32843 | 2 | 0 | MC structure principle |
| `thm:convolution-d-squared-zero` | `theorem` | `ProvedHere` | 33452 | 1 | 0 | Square-zero: convolution level |
| `cor:genus-base-cases` | `corollary` | `ProvedHere` | 33769 | 0 | 0 | Base cases |
| `prop:2d-convergence` | `proposition` | `ProvedHere` | 34319 | 0 | 2 | Two-dimensional convergence |
| `thm:verlinde-polynomial-family` | `theorem` | `ProvedHere` | 34931 | 2 | 0 | Verlinde polynomial family |
| `prop:g2-degree0` | `proposition` | `ProvedHere` | 35292 | 0 | 0 | Degree-$0$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree1` | `proposition` | `ProvedHere` | 35346 | 1 | 0 | Degree-$1$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree2` | `proposition` | `ProvedHere` | 35676 | 1 | 0 | Degree-$2$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-conformal-block-degree` | `proposition` | `ProvedHere` | 35773 | 2 | 0 | Genus-$2$ conformal block decomposition by degree |
| `prop:genus-g-euler-general` | `proposition` | `ProvedHere` | 35834 | 2 | 0 | Euler characteristic of degree-$2$ KZB local systems: general rank and genus |
| `prop:g2-euler-n` | `proposition` | `ProvedHere` | 35928 | 2 | 0 | Euler characteristic at low degrees, genus~$2$ |
| `prop:g2-nonsep-degen` | `proposition` | `ProvedHere` | 36146 | 6 | 0 | Non-separating degeneration: $\Sigma_2 \to E_\tau$ |
| `prop:g2-sep-degen` | `proposition` | `ProvedHere` | 36259 | 3 | 1 | Separating degeneration: $\Sigma_2 \to E_\tau \cup E_{\tau'}$ |
| `thm:determinantal-branch-formula` | `theorem` | `ProvedHere` | 36639 | 0 | 0 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | `ProvedHere` | 36675 | 0 | 0 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | `ProvedHere` | 36706 | 0 | 0 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | `ProvedHere` | 36770 | 3 | 0 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | `ProvedHere` | 36806 | 0 | 0 | First cubic obstruction |
| `cor:hgmk-abar5-twentyeight-stratum` | `corollary` | `ProvedHere` | 38299 | 0 | 1 | Genus-$5$ octachotomy analogue: the twenty-eight-stratum ambient tower on $\AbarFive$ |

#### `chapters/theory/higher_kummer_arithmetic_duality_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:higher-kummer-z-g-presence` | `theorem` | `ProvedHere` | 49 | 2 | 0 | Kummer-irregular primes witnessed on the $Z_g$ side |
| `thm:higher-kummer-s-r-absence-through-r-13` | `theorem` | `ProvedHere` | 147 | 3 | 0 | Higher Kummer-irregular primes absent from $S_r(\Vir_c)$ through $r = 13$ |
| `thm:higher-kummer-refined-duality` | `theorem` | `ProvedHere` | 256 | 3 | 0 | Finite Bernoulli--Virasoro separation through $r = 13$ |

#### `chapters/theory/hochschild_cohomology.tex` (20)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:hochschild-classical-comparison` | `theorem` | `ProvedElsewhere` | 194 | 0 | 1 | Comparison with classical theory {\cite{BD04}} |
| `thm:bar-spectral-sequence-hochschild` | `theorem` | `ProvedElsewhere` | 518 | 0 | 2 | Bar spectral sequence {\cite{BD04,CG17}} |
| `thm:hochschild-chain-complex` | `theorem` | `ProvedHere` | 654 | 1 | 1 | Chiral Hochschild chain model is a chain complex |
| `lem:cyclic-commutes` | `lemma` | `ProvedHere` | 734 | 0 | 0 | Cyclic operator commutes with the chiral Hochschild differential |
| `thm:connes-exact-sequence` | `theorem` | `ProvedElsewhere` | 766 | 0 | 2 | Connes mixed-complex structure {\cite{Connes85,Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:782` | `remark` | `ProvedElsewhere` | 782 | 0 | 2 | Provenance and citation |
| `cor:connes-SBI` | `corollary` | `ProvedElsewhere` | 789 | 1 | 2 | Connes SBI exact sequence {\cite{Connes85,Loday98}} |
| `thm:HC-spectral-sequence` | `theorem` | `ProvedElsewhere` | 800 | 1 | 2 | Chiral Hochschild-cyclic spectral sequence {\cite{Connes85,Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:824` | `remark` | `ProvedElsewhere` | 824 | 0 | 2 | Provenance and citation |
| `thm:E2-page-formula` | `theorem` | `ProvedElsewhere` | 837 | 0 | 1 | Second-page formula {\cite{Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:859` | `remark` | `ProvedElsewhere` | 859 | 0 | 1 | Provenance and citation |
| `prop:morita-equivalence-compact-gen` | `proposition` | `ProvedElsewhere` | 1195 | 0 | 3 | Morita equivalence {\cite{Keller06,Toen07}} |
| `prop:endofunctor-bimodule` | `proposition` | `ProvedElsewhere` | 1270 | 0 | 2 | Endofunctor--bimodule equivalence {\cite{Toen07,BZFN10}} |
| `cor:identity-diagonal` | `corollary` | `ProvedHere` | 1302 | 1 | 0 | Identity functor $=$ diagonal bimodule |
| `thm:derived-center-hochschild` | `theorem` | `ProvedHere` | 1321 | 4 | 0 | Derived center $=$ categorical Hochschild cohomology $=$ algebraic Hochschild cochains via a compact generator |
| `thm:morita-invariance-HH` | `theorem` | `ProvedHere` | 1412 | 1 | 0 | Morita invariance of algebraic Hochschild cohomology |
| `prop:explicit-morita-transfer` | `proposition` | `ProvedHere` | 1444 | 0 | 0 | Explicit Morita transfer |
| `thm:excision` | `theorem` | `ProvedElsewhere` | 1619 | 0 | 1 | Excision; {\cite[Theorem~3.18 |
| `thm:circle-fh-hochschild` | `theorem` | `ProvedHere` | 1637 | 2 | 0 | Factorization homology on $S^1$ $=$ algebraic Hochschild chains |
| `prop:monodromy-standard` | `proposition` | `ProvedHere` | 1797 | 0 | 0 | Monodromy for standard families |

#### `chapters/theory/infinite_fingerprint_classification.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `cor:quadrichotomy-depth-shift` | `corollary` | `ProvedHere` | 588 | 0 | 0 | Quadrichotomy as depth shift |
| `thm:quadrichotomy-is-coarse-projection` | `theorem` | `ProvedHere` | 600 | 2 | 0 | Quadrichotomy is a coarse projection; strengthening of Proposition~\ref{prop:coarse-projection-functor} |
| `thm:DS-fingerprint-transport` | `theorem` | `ProvedHere` | 696 | 1 | 7 | DS transport of the fingerprint; closes FM\textup{108} |
| `cor:fingerprint-separates-landscape` | `corollary` | `ProvedHere` | 847 | 3 | 0 | Completeness on the standard landscape |
| `thm:schellekens-structured-subset` | `theorem` | `ProvedHere` | 879 | 1 | 0 | Structured-subset derivation of the holomorphic \texorpdfstring{$c=24$}{c=24} census; closes AP\textup{290} |

#### `chapters/theory/introduction.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:central-charge-complementarity` | `theorem` | `ProvedHere` | 1367 | 1 | 1 | Central charge complementarity |

#### `chapters/theory/kappa_conductor.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:platonic-conductor` | `theorem` | `ProvedHere` | 181 | 2 | 0 | Canonical ghost scalar |

#### `chapters/theory/koszul_pair_structure.tex` (22)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | `ProvedHere` | 359 | 0 | 0 | Well-definedness of the chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | `ProvedHere` | 409 | 1 | 0 | Relative exactness of the two-sided chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | `ProvedHere` | 489 | 1 | 0 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | `ProvedHere` | 515 | 1 | 0 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | `ProvedHere` | 592 | 1 | 0 | Properties of cup product |
| `thm:chiral-gerstenhaber-kps` | `theorem` | `ProvedElsewhere` | 635 | 0 | 3 | Chiral Gerstenhaber algebra {\cite{Ger63, Tamarkin00}} |
| `thm:ainfty-chiral-hochschild` | `theorem` | `ProvedHere` | 669 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} operations from the chiral brace model |
| `thm:linfty-chiral-hochschild` | `theorem` | `ProvedElsewhere` | 719 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} structure {\cite{LV12}} |
| `prop:admissible-levels-permuted` | `proposition` | `ProvedHere` | 1137 | 0 | 1 | Numerical admissible data under the level reflection |
| `thm:mc-quadratic` | `theorem` | `ProvedHere` | 1235 | 0 | 0 | Maurer--Cartan correspondence, quadratic case |
| `thm:chiral-yangian-km` | `theorem` | `ProvedHere` | 1327 | 0 | 0 | Affine Kac--Moody as chiral algebra |
| `thm:chiral-yangian` | `theorem` | `ProvedElsewhere` | 1351 | 0 | 2 | Critical centre and Yangian deformation data {\cite{Drinfeld85,Feigin-Frenkel}} |
| `thm:feigin-frenkel-bar` | `theorem` | `ProvedElsewhere` | 1484 | 0 | 1 | Feigin--Frenkel centre {\cite{FF}} |
| `thm:w-algebra-sl4` | `theorem` | `ProvedElsewhere` | 1560 | 0 | 1 | Structure of \texorpdfstring{$\mathcal{W}(\mathfrak{sl}_4, e_{subreg})$}{W(sl4, e\_subreg)} {\cite{KRW}} |
| `thm:ff-s-duality` | `theorem` | `ProvedElsewhere` | 1568 | 0 | 1 | Feigin--Frenkel duality as S-duality, principal simply-laced case |
| `thm:koszul-equivalence-categories` | `theorem` | `ProvedElsewhere` | 1629 | 0 | 1 | Koszul equivalence of categories {\cite{BGS96}} |
| `thm:linf-mc-flatness` | `theorem` | `ProvedHere` | 1897 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan equation from a transferred \texorpdfstring{$A_\infty$}{A-infinity} model |
| `thm:ordered-shuffle` | `theorem` | `ProvedHere` | 2317 | 1 | 0 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | `ProvedHere` | 2359 | 0 | 0 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | `ProvedHere` | 2389 | 2 | 0 | Enveloping duality |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | `ProvedHere` | 2543 | 1 | 0 | chiral Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-FG-shadow` | `theorem` | `ProvedElsewhere` | 2747 | 0 | 1 | Commutator-shadow theorem |

#### `chapters/theory/koszulness_moduli_scheme.tex` (14)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `v1-thm:kms-moduli` | `theorem` | `ProvedHere` | 315 | 10 | 4 | Koszulness moduli, finite-stage representability |
| `v1-cor:kms-grt-invariant` | `corollary` | `ProvedHere` | 530 | 3 | 0 | Associator-independence of the Koszulness property |
| `v1-thm:kms-fourteen-unconditional` | `theorem` | `ProvedHere` | 582 | 10 | 0 | Fourteen admissible characterisations on their home chart |
| `v1-prop:kms-at-chart` | `proposition` | `ProvedHere` | 730 | 2 | 1 | Alekseev--Torossian chart |
| `v1-prop:kms-hodge-betti-chart` | `proposition` | `ProvedHere` | 824 | 2 | 3 | Hodge--Betti chart |
| `v1-prop:kms-elliptic-chart` | `proposition` | `ProvedHere` | 879 | 2 | 1 | Enriquez elliptic chart |
| `v1-prop:kms-kontsevich-chart` | `proposition` | `ProvedHere` | 933 | 3 | 1 | Kontsevich integral chart |
| `v1-thm:kms-koszulness-is-grt-invariant` | `theorem` | `ProvedHere` | 1001 | 5 | 2 | Koszulness is $\mathrm{GRT}_1$-invariant; admissible characterisations are charts |
| `v1-thm:kms-virasoro-noncircular` | `theorem` | `ProvedHere` | 1037 | 0 | 4 | Virasoro Koszulness, non-circular |
| `v1-cor:kms-exceptional-PBW` | `corollary` | `ProvedElsewhere` | 1206 | 0 | 1 | Exceptional-type Yangian PBW input via GRW18 |
| `v1-thm:kms-meta-koszulness` | `theorem` | `ProvedHere` | 1247 | 2 | 1 | Meta-Koszulness |
| `rem:kms-K3-placement` | `remark` | `ProvedHere` | 1444 | 4 | 0 | K3 chart placement on the Koszulness moduli object |
| `rem:kms-grt-transport-312` | `remark` | `ProvedHere` | 1478 | 3 | 0 | $\mathrm{GRT}_1$-transport of the K3 central charge |
| `rem:kms-humbert-cocycle` | `remark` | `ProvedHere` | 1505 | 0 | 0 | Humbert-$H_1$ monodromy as K3 chart-compatibility data |

#### `chapters/theory/mc3_five_family_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:mc3-finite-window-upgrade-boundary` | `proposition` | `ProvedElsewhere` | 113 | 4 | 0 | Finite-window upgrade boundary |
| `thm:mc3-evaluation-core-five-family` | `theorem` | `ProvedHere` | 208 | 1 | 0 | MC3 on the evaluation-generated core, five-family mechanism |
| `prop:mc3-type-A-asymptotic-prefundamentals-platonic` | `proposition` | `ProvedHere` | 352 | 0 | 0 | Asymptotic prefundamentals: rational type~$A$ |
| `prop:mc3-type-BCD-reflection-shapovalov-platonic` | `proposition` | `ProvedHere` | 403 | 0 | 0 | Reflection-equation Shapovalov: twisted B/C/D |
| `prop:mc3-uniform-chari-moura-platonic` | `proposition` | `ProvedHere` | 449 | 0 | 0 | Chari--Moura multiplicity-free $\ell$-weights: classical and simply-laced exceptional types |
| `prop:mc3-uniform-chari-moura-nonsimplylaced-platonic` | `proposition` | `ProvedElsewhere` | 479 | 0 | 0 | Multiplicity-free $\ell$-weights: non-simply-laced exceptional types $G_2, F_4$ |
| `prop:mc3-elliptic-theta-divisor-platonic` | `proposition` | `ProvedHere` | 547 | 0 | 0 | Elliptic Bethe / DYBE: theta-divisor complement |
| `prop:mc3-super-parity-balance-platonic` | `proposition` | `ProvedHere` | 582 | 1 | 0 | Super-Yangian parity-balance: $Y_\hbar(\mathfrak{gl}_{m\|n})$ |
| `prop:baxter-retraction-type-A-artifact` | `proposition` | `ProvedHere` | 713 | 3 | 0 | Baxter hyperplane as a type-$A$ rational artifact |

#### `chapters/theory/mc5_class_m_chain_level_platonic.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:curve-H20-vanishing` | `lemma` | `ProvedElsewhere` | 759 | 0 | 0 | Curve-fibre Hodge dimension |
| `prop:central-m0-vacuum-proportionality` | `proposition` | `ProvedHere` | 788 | 0 | 0 | Sub-argument (b): vacuum-proportionality uniqueness of the central degree-2 curvature |
| `lem:sl2-sl2-splitting` | `lemma` | `ProvedElsewhere` | 1015 | 0 | 3 | $SL_2\times SL_2$ splitting of the bi-filtration |
| `lem:sl2-admissible-splitting` | `lemma` | `ProvedElsewhere` | 1560 | 0 | 3 | $\mathfrak{sl}_2^{\oplus\mathrm{adm}}$ splitting of the Malcev ladder |
| `thm:mc5-infty-one-obstruction-tower` | `theorem` | `ProvedHere` | 2602 | 0 | 3 | $(\infty,1)$-bar--cobar inversion on $\Perf(\AbarTwo)$: the obstruction tower |
| `thm:mc5-bridgeland-slicing-reads-obstruction-tower` | `theorem` | `ProvedHere` | 2651 | 3 | 4 | Bridgeland slicing reads the obstruction tower |

#### `chapters/theory/mc5_genus0_genus1_wall_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:mc5-g0g1-wall-five-point-sewing` | `theorem` | `ProvedHere` | 169 | 4 | 0 | MC5 5-point sewing with genus-one clutching |
| `cor:mc5-g0g1-heisenberg-elliptic-function` | `corollary` | `ProvedHere` | 510 | 2 | 0 | Heisenberg elliptic function at the wall |
| `cor:mc5-g0g1-k3-elliptic-genus` | `corollary` | `ProvedHere` | 590 | 2 | 1 | K3 elliptic genus at the wall |

#### `chapters/theory/motivic_shadow_full_class_m_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:w3-w-line-motivic-rationality` | `proposition` | `ProvedHere` | 268 | 0 | 0 | \label{prop:w3-w-line-motivic-rationality} $\cW_3$ W-line explicit rationality |
| `thm:bp-motivic-rationality-arakawa` | `theorem` | `ProvedHere` | 317 | 1 | 0 | \label{thm:bp-motivic-rationality-arakawa}BP T-line motivic rationality in Arakawa convention |
| `prop:bp-fl-convention-caveat` | `proposition` | `ProvedHere` | 355 | 1 | 0 | \label{prop:bp-fl-convention-caveat}FL-convention Koszul conductor: distinct constant |

#### `chapters/theory/motivic_shadow_tower.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:shadow-tower-motivic-lift` | `theorem` | `ProvedHere` | 218 | 0 | 0 | \label{thm:shadow-tower-motivic-lift}Motivic lift of Arnold-period shadow coefficients |
| `thm:grt-motivic-coaction` | `theorem` | `ProvedHere` | 301 | 1 | 0 | \label{thm:grt-motivic-coaction}Motivic coaction on the Arnold shadow-period envelope |
| `prop:s4-vir-mot` | `proposition` | `ProvedHere` | 382 | 0 | 0 | \label{prop:s4-vir-mot}Motivic lift of $S_4(\Vir_c)$ |
| `prop:s5-vir-mot` | `proposition` | `ProvedHere` | 421 | 0 | 0 | \label{prop:s5-vir-mot}Motivic lift of $S_5(\Vir_c)$ |
| `thm:virasoro-motivic-rationality-all-r` | `theorem` | `ProvedHere` | 525 | 1 | 0 | \label{thm:virasoro-motivic-rationality-all-r}Virasoro motivic rationality: weighted tower and manuscript boundary |
| `rem:characteristic-primes-are-riccati-arithmetic` | `remark` | `ProvedHere` | 691 | 0 | 0 | \label{rem:characteristic-primes-are-riccati-arithmetic}Characteristic primes of the shadow tower are Riccati-recurrence integers |
| `thm:kappa-vs-beta-split` | `theorem` | `ProvedHere` | 823 | 0 | 0 | \label{thm:kappa-vs-beta-split}Motivic kappa, modular beta |

#### `chapters/theory/nilpotent_completion.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:geom-conilpotent` | `proposition` | `ProvedHere` | 118 | 0 | 0 | Collision trees and coradical degree |
| `thm:completion-convergence` | `theorem` | `ProvedHere` | 173 | 2 | 0 | Finite-window convergence |
| `thm:completed-bar-cobar` | `theorem` | `ProvedHere` | 304 | 1 | 0 | Completed finite-window bar--cobar inversion |
| `thm:koszul-dual-characterization` | `theorem` | `ProvedHere` | 360 | 3 | 0 | Essential image of finite-window bar towers |
| `thm:BD-chiral-homology` | `theorem` | `ProvedElsewhere` | 438 | 0 | 1 | BD chiral homology \cite{BD04} |
| `prop:practical-convergence` | `proposition` | `ProvedHere` | 564 | 0 | 0 | Weight-window convergence |
| `thm:CG-renorm` | `theorem` | `ProvedElsewhere` | 610 | 0 | 1 | Costello--Gwilliam renormalization \cite{CG17} |
| `thm:stabilized-completion-positive` | `theorem` | `ProvedHere` | 706 | 0 | 0 | Stabilized completion for positive towers |
| `lem:finite-resonance-tensor-exact` | `lemma` | `ProvedHere` | 813 | 0 | 0 | Exact tensoring with a finite resonance tower |
| `thm:resonance-filtered-bar-cobar` | `theorem` | `ProvedHere` | 849 | 3 | 0 | Resonance-filtered completed bar/cobar |
| `prop:resonance-ss-degeneration` | `proposition` | `ProvedHere` | 965 | 1 | 0 | Resonance spectral sequence degeneration |
| `prop:resonance-ranks-standard` | `proposition` | `ProvedHere` | 992 | 2 | 0 | Resonance ranks of the standard families |
| `cor:virasoro-resonance-ss` | `corollary` | `ProvedHere` | 1067 | 1 | 0 | Virasoro resonance spectral sequence |
| `thm:platonic-completion` | `theorem` | `ProvedHere` | 1147 | 6 | 0 | Resonance completion |
| `prop:nc-massey-triple-rrr-E8` | `proposition` | `ProvedHere` | 2628 | 0 | 4 | Associator-free chain-level triple Massey product |
| `prop:nc-delta-n-explicit-higher` | `proposition` | `ProvedHere` | 3008 | 3 | 2 | Explicit recurrence for $\delta^{(n)}$ at $n \ge 7$ |

#### `chapters/theory/ordered_associative_chiral_kd.tex` (92)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:bicom-e` | `lemma` | `ProvedHere` | 235 | 0 | 0 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | `ProvedHere` | 319 | 0 | 0 | Ordered chiral shuffle theorem |
| `prop:r-matrix-descent-vol1` | `proposition` | `ProvedHere` | 585 | 4 | 0 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | `ProvedHere` | 731 | 5 | 0 | Pole-free descent is naive |
| `prop:symmetric-descent` | `proposition` | `ProvedHere` | 766 | 2 | 0 | Symmetric descent and ordered surplus |
| `thm:opposite` | `theorem` | `ProvedHere` | 949 | 0 | 0 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | `ProvedHere` | 990 | 1 | 0 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | `ProvedHere` | 1041 | 0 | 0 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | `ProvedHere` | 1061 | 1 | 0 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | `ProvedHere` | 1128 | 0 | 0 | — |
| `prop:one-defect` | `proposition` | `ProvedHere` | 1155 | 0 | 0 | — |
| `thm:tangent=K` | `theorem` | `ProvedHere` | 1177 | 0 | 0 | Tangent identification |
| `cor:infdual` | `corollary` | `ProvedHere` | 1214 | 2 | 0 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | `ProvedHere` | 1246 | 2 | 0 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | `ProvedHere` | 1298 | 3 | 0 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | `ProvedHere` | 1331 | 1 | 0 | Diagonal correspondence |
| `cor:unit` | `corollary` | `ProvedHere` | 1379 | 2 | 0 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | `ProvedHere` | 1397 | 1 | 0 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | `ProvedHere` | 1433 | 2 | 0 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | `ProvedHere` | 1465 | 1 | 0 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | `ProvedHere` | 1491 | 1 | 0 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | `ProvedHere` | 1516 | 1 | 0 | Cap action |
| `thm:pair-of-pants` | `theorem` | `ProvedHere` | 1579 | 1 | 0 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | `ProvedHere` | 1617 | 4 | 0 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | `ProvedHere` | 1671 | 1 | 0 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | `ProvedHere` | 1720 | 2 | 0 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | `ProvedHere` | 1750 | 12 | 0 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | `ProvedHere` | 1861 | 0 | 0 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | `ProvedHere` | 2343 | 1 | 0 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | `ProvedHere` | 2457 | 0 | 0 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | `ProvedHere` | 2538 | 0 | 0 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | `ProvedHere` | 2597 | 0 | 0 | Formality: class~G, shadow depth~$2$ |
| `thm:drinfeld-yangian-sl2` | `theorem` | `ProvedHere` | 2736 | 6 | 0 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | `ProvedHere` | 2826 | 0 | 0 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | `ProvedHere` | 2862 | 3 | 0 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | `ProvedHere` | 2914 | 3 | 0 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | `ProvedHere` | 2955 | 7 | 0 | Classical limit |
| `thm:central-extension-invisible` | `theorem` | `ProvedHere` | 3046 | 0 | 0 | Central extension is invisible to the ordered double bar |
| `thm:two-colour-double-kd` | `theorem` | `ProvedHere` | 3121 | 1 | 0 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | `ProvedHere` | 3149 | 2 | 0 | Non-redundancy of the two colours |
| `prop:vir-collision-residue` | `proposition` | `ProvedHere` | 3228 | 2 | 0 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | `ProvedHere` | 3263 | 2 | 0 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | `ProvedHere` | 3292 | 0 | 0 | Gravitational Yangian collapse |
| `prop:grav-yangian-curvature` | `proposition` | `ProvedHere` | 3426 | 1 | 0 | Gravitational Yangian curvature |
| `thm:grav-coproduct-primitive` | `theorem` | `ProvedHere` | 3532 | 0 | 0 | Gravitational coproduct primitivity |
| `thm:root-space-one-dim-v1` | `theorem` | `ProvedHere` | 4079 | 0 | 0 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | `ProvedHere` | 4128 | 1 | 0 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | `ProvedHere` | 4194 | 0 | 0 | Dynkin coefficient via the beta integral |
| `thm:sl3-triangle-coefficient` | `theorem` | `ProvedHere` | 4826 | 0 | 0 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | `ProvedHere` | 4910 | 0 | 0 | Serre relations from root-space vanishing |
| `thm:sl4-quadrilateral` | `theorem` | `ProvedHere` | 5108 | 1 | 0 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:annular-bar-differential` | `theorem` | `ProvedHere` | 5398 | 1 | 0 | Annular bar differential |
| `thm:annular-HH` | `theorem` | `ProvedHere` | 5491 | 3 | 0 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | `ProvedHere` | 5614 | 1 | 0 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:b-cycle-quantum-group` | `theorem` | `ProvedHere` | 5944 | 2 | 0 | Quantum-group parameter from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | `ProvedElsewhere` | 6206 | 3 | 0 | Drinfeld--Kohno on the affine evaluation surface; {} for monodromy, {} for ordered reduction |
| `thm:yangian-quantum-group` | `theorem` | `ProvedHere` | 6301 | 2 | 0 | Affine genus-one monodromy readout |
| `cor:sl2-root-of-unity` | `corollary` | `ProvedHere` | 6385 | 0 | 0 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | `ProvedHere` | 6426 | 1 | 0 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | `ProvedHere` | 6588 | 0 | 0 | Ordered pole-depth spectrum |
| `thm:ordered-AOS` | `theorem` | `ProvedHere` | 6647 | 2 | 0 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | `ProvedHere` | 6726 | 2 | 0 | Averaging and surplus |
| `prop:ker-av-schur-weyl` | `proposition` | `ProvedHere` | 6898 | 0 | 0 | Kernel of the Reynolds projector: general simple Lie algebras |
| `thm:elliptic-spectral-dichotomy` | `theorem` | `ProvedHere` | 7152 | 3 | 0 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `thm:bg-ordered-bar` | `theorem` | `ProvedHere` | 7362 | 0 | 0 | Free-field ordered bar complexes |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | `ProvedHere` | 7543 | 1 | 0 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | `ProvedHere` | 7609 | 1 | 0 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | `ProvedHere` | 7669 | 2 | 0 | Ordered Koszul dual of lattice algebras |
| `comp:sl2-eval` | `computation` | `ProvedHere` | 7823 | 2 | 0 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | `ProvedHere` | 7884 | 0 | 0 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | `ProvedHere` | 7932 | 1 | 0 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | `ProvedHere` | 7974 | 1 | 0 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | `ProvedHere` | 8023 | 2 | 0 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `thm:drinfeld-classification` | `theorem` | `ProvedElsewhere` | 8072 | 0 | 0 | Drinfeld classification |
| `prop:eval-drinfeld` | `proposition` | `ProvedHere` | 8095 | 0 | 0 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | `ProvedHere` | 8162 | 2 | 0 | Line category as finite-dimensional modules |
| `thm:eval-braiding` | `theorem` | `ProvedHere` | 8242 | 0 | 0 | Braiding from the $R$-matrix |
| `thm:grothendieck-yangian` | `theorem` | `ProvedElsewhere` | 8287 | 0 | 0 | Grothendieck ring of Yangian modules |
| `prop:r-matrix-eigenvalue` | `proposition` | `ProvedHere` | 8349 | 0 | 0 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | `ProvedHere` | 8376 | 1 | 0 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | `ProvedHere` | 8475 | 1 | 0 | $\mathsf{E}_1$ ordered bar landscape |
| `lem:coprod-T-miura` | `lemma` | `ProvedHere` | 10351 | 1 | 1 | Miura inversion of the spectral coproduct at spin~$2$ |
| `prop:spin3-miura-coprod` | `proposition` | `ProvedHere` | 10434 | 2 | 0 | Spin-$3$ Miura coproduct |
| `lem:qdet-central-all-N` | `lemma` | `ProvedElsewhere` | 11530 | 0 | 1 | Centrality of the quantum determinant at rank $N$ |
| `thm:FG-shadow-vol2` | `theorem` | `ProvedElsewhere` | 11746 | 0 | 0 | Comm\-utator-shadow theorem |
| `thm:ordered-associative-modular-mc` | `theorem` | `ProvedElsewhere` | 11832 | 0 | 0 | Associative modular Maurer--Cartan class |
| `thm:ordered-associative-ds-principal` | `theorem` | `ProvedElsewhere` | 11872 | 0 | 0 | Reduction commutes with associative chiral duality \textup{(}principal case\textup{)} |
| `prop:r-matrix-stable-envelope` | `proposition` | `ProvedHere` | 12712 | 0 | 0 | $R$-matrix comparison |
| `thm:e3-identification-km` | `theorem` | `ProvedHere` | 12773 | 1 | 0 | $\mathsf{E}_3$ identification for affine Kac--Moody |
| `prop:critical-level-ordered` | `proposition` | `ProvedHere` | 12902 | 0 | 0 | Critical level: monodromy trivialises, Koszulness fails, center jumps |
| `rem:bernard-heat-identity-zeta` | `remark` | `ProvedElsewhere` | 13109 | 2 | 2 | Bernard heat identity for the Weierstrass $\zeta$ |
| `rem:kzb-n-point-dynamical-closure` | `remark` | `ProvedElsewhere` | 13178 | 3 | 3 | $n \geq 3$ KZB flatness: Felder dynamical shift + Halphen--Ramanujan |

#### `chapters/theory/periodic_cdg_admissible.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:universal-pbw-koszul-admissible-parameters` | `proposition` | `ProvedHere` | 74 | 1 | 0 | Universal PBW--Koszul lane at admissible parameters |

#### `chapters/theory/poincare_duality.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:verdier-config` | `theorem` | `ProvedElsewhere` | 240 | 0 | 1 | Verdier duality for configuration spaces; {} \cite{KS90} |
| `thm:dual-differentials` | `theorem` | `ProvedHere` | 330 | 1 | 0 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | `ProvedHere` | 489 | 1 | 0 | Bar coalgebra and post-Verdier algebra |
| `thm:bar-computes-dual` | `theorem` | `ProvedHere` | 566 | 6 | 0 | Bar coalgebra, Koszul-dual coalgebra, and Verdier-dual algebra |
| `comp:bar-dual-low-degrees` | `computation` | `ProvedHere` | 670 | 0 | 0 | Degree 0 and 1 |

#### `chapters/theory/poincare_duality_quantum.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:universal-defect-construction` | `theorem` | `ProvedElsewhere` | 270 | 0 | 1 | Finite-type Ext model for the defect algebra {\cite{LV12}} |
| `__unlabeled_chapters/theory/poincare_duality_quantum.tex:356` | `calculation` | `ProvedElsewhere` | 356 | 0 | 1 | Yangian structure constants {\cite{Drinfeld85}} |
| `thm:ff-center` | `theorem` | `ProvedElsewhere` | 406 | 0 | 2 | Feigin--Frenkel center {\cite{Feigin-Frenkel,BD04}} |
| `thm:fact-homology-quantum` | `theorem` | `ProvedElsewhere` | 479 | 0 | 2 | Factorization homology and the bar complex {\cite{Francis2013,HA}} |
| `prop:chiral-operad-genus0` | `proposition` | `ProvedHere` | 524 | 0 | 3 | Genus-zero identification |
| `thm:prism-higher-genus` | `theorem` | `ProvedHere` | 808 | 3 | 1 | Prism principle: higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | `ProvedHere` | 880 | 0 | 0 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | `ProvedHere` | 905 | 2 | 0 | The loop expansion is the genus expansion |
| `cor:feynman-transform-involution` | `corollary` | `ProvedElsewhere` | 1075 | 0 | 1 | Feynman transform involution {\cite{GeK98}} |
| `thm:modular-convolution-structure` | `theorem` | `ProvedHere` | 1154 | 0 | 1 | dg~Lie structure |
| `thm:vol1-genus-completion` | `theorem` | `ProvedHere` | 1194 | 1 | 0 | Genus completion |
| `prop:vol1-structure-as-MC` | `proposition` | `ProvedHere` | 1242 | 2 | 0 | The algebra structure as MC element |
| `prop:log-forms-conformal-invariance` | `proposition` | `ProvedElsewhere` | 1283 | 0 | 1 | Forced by conformal invariance {\cite{BPZ84}} |
| `lem:sign-consistency-bar` | `lemma` | `ProvedElsewhere` | 1322 | 0 | 1 | Sign consistency for bar differential {\cite{LV12}} |
| `thm:bar-cobar-adjunction-operadic` | `theorem` | `ProvedElsewhere` | 1338 | 1 | 1 | Bar-cobar adjunction {\cite{LV12}} |
| `thm:partition` | `theorem` | `ProvedHere` | 1354 | 0 | 2 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:quantum-linfty-master` | `theorem` | `ProvedHere` | 835 | 4 | 0 | Quantum $L_\infty$ master equation |
| `thm:non-renormalization-tree` | `theorem` | `ProvedElsewhere` | 946 | 0 | 1 | Non-renormalization at tree level |
| `cor:exact-r-matrix` | `corollary` | `ProvedElsewhere` | 977 | 2 | 0 | Collision residue normalization for standard-family $r$-matrices |
| `prop:two-element-strict` | `proposition` | `ProvedHere` | 1103 | 2 | 0 | Two-element covers are strict |
| `prop:jacobiator-nullhomotopic` | `proposition` | `ProvedElsewhere` | 1181 | 2 | 1 | Jacobiator is nullhomotopic |
| `prop:borcherds-shadow-identification` | `proposition` | `ProvedHere` | 1587 | 4 | 2 | Secondary Borcherds operations and the first shadow obstructions |

#### `chapters/theory/shadow_L_function_platonic.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:shL-convergence-half-plane` | `proposition` | `ProvedHere` | 103 | 0 | 0 | \label{prop:shL-convergence-half-plane}Formal uniqueness and analytic growth datum |
| `thm:kummer-congruence-prediction` | `theorem` | `ProvedElsewhere` | 357 | 3 | 0 | \label{thm:kummer-congruence-prediction}Bernoulli--Kummer witnesses for the genus slots |

#### `chapters/theory/shadow_tower_higher_coefficients.tex` (39)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:virasoro-shadow-recurrence` | `theorem` | `ProvedHere` | 203 | 0 | 0 | \label{thm:virasoro-shadow-recurrence}Virasoro weighted shadow recurrence |
| `thm:s6-virasoro-closed-form` | `theorem` | `ProvedHere` | 282 | 1 | 0 | \label{thm:s6-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_6(\Vir_c)$ |
| `thm:s7-virasoro-closed-form` | `theorem` | `ProvedHere` | 349 | 0 | 0 | \label{thm:s7-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_7(\Vir_c)$ |
| `thm:s8-virasoro-closed-form` | `theorem` | `ProvedHere` | 418 | 2 | 0 | \label{thm:s8-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_8(\Vir_c)$ |
| `prop:sth-boundary-checks` | `proposition` | `ProvedHere` | 542 | 3 | 0 | \label{prop:sth-boundary-checks}Weighted boundary values through weight 8 |
| `prop:sth-leading-asymp` | `proposition` | `ProvedHere` | 602 | 0 | 0 | \label{prop:sth-leading-asymp}Leading large-$c$ asymptotic coefficient for the weighted tower |
| `thm:shadow-exponential-base-Virasoro` | `theorem` | `ProvedHere` | 670 | 1 | 0 | \label{thm:shadow-exponential-base-Virasoro} The shadow-exponential base of Virasoro is $C_\Vir = 6$ |
| `prop:W3-T-line-matches-Vir-subleading` | `proposition` | `ProvedHere` | 768 | 0 | 0 | \label{prop:W3-T-line-matches-Vir-subleading} $\cW_3$ $T$-line subleading asymptotic matches Virasoro |
| `thm:shadow-series-closed-form-Virasoro` | `theorem` | `ProvedHere` | 855 | 0 | 0 | \label{thm:shadow-series-closed-form-Virasoro} Closed-form Virasoro shadow series |
| `thm:shadow-series-closed-form-Virasoro-subleading` | `theorem` | `ProvedHere` | 909 | 0 | 0 | \label{thm:shadow-series-closed-form-Virasoro-subleading} Closed-form subleading Virasoro shadow series |
| `thm:pole-doubling-all-k` | `theorem` | `ProvedHere` | 1005 | 0 | 0 | \label{thm:pole-doubling-all-k} Pole-doubling pattern for all $k$ |
| `prop:phi-k-leading-coefficient-arithmetic` | `proposition` | `ProvedHere` | 1052 | 0 | 0 | \label{prop:phi-k-leading-coefficient-arithmetic} Arithmetic of the leading $\varphi_k$ coefficient |
| `thm:w3-wline-closed-form` | `theorem` | `ProvedHere` | 1507 | 3 | 0 | \label{thm:w3-wline-closed-form} $W_3$ $W$-line integer sequence closed form |
| `thm:w3-wline-exponential-base` | `theorem` | `ProvedHere` | 1559 | 3 | 0 | \label{thm:w3-wline-exponential-base} $W$-line shadow-exponential base $C_{W_3}^{W\text{-line}} = 12$ |
| `thm:w3-wline-generating-function` | `theorem` | `ProvedHere` | 1599 | 4 | 0 | \label{thm:w3-wline-generating-function} Exact generating-function closed form for the $W$-line sequence |
| `cor:w3-wline-self-consistency` | `corollary` | `ProvedHere` | 1651 | 1 | 0 | \label{cor:w3-wline-self-consistency} Riccati self-consistency at the radius of convergence |
| `prop:sth-virasoro-rational-through-8` | `proposition` | `ProvedHere` | 1957 | 2 | 0 | \label{prop:sth-virasoro-rational-through-8}No motivic period enters Virasoro through weight 8 |
| `prop:sth-summary` | `proposition` | `ProvedHere` | 2022 | 4 | 0 | \label{prop:sth-summary}Closed-form weighted Virasoro spectrum through weight 8 |
| `thm:s-r-kummer-absent-through-r-11` | `theorem` | `ProvedHere` | 2084 | 5 | 0 | \label{thm:s-r-kummer-absent-through-r-11}The Bernoulli-leading Kummer pair $\{691, 3617\}$ is absent from $\widehat S^{\rm wt}_r(\Vir_c)$ through $r = 11$ |
| `thm:s9-virasoro-closed-form` | `theorem` | `ProvedHere` | 2339 | 3 | 0 | \label{thm:s9-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_9(\Vir_c)$ |
| `thm:s10-virasoro-closed-form` | `theorem` | `ProvedHere` | 2404 | 1 | 0 | \label{thm:s10-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_{10}(\Vir_c)$ |
| `thm:s11-virasoro-closed-form` | `theorem` | `ProvedHere` | 2456 | 1 | 0 | \label{thm:s11-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_{11}(\Vir_c)$ |
| `thm:shadow-tower-asymptotic-closed-form` | `theorem` | `ProvedHere` | 2495 | 1 | 0 | \label{thm:shadow-tower-asymptotic-closed-form}Closed form for the leading asymptotic |
| `cor:virasoro-23-smoothness` | `corollary` | `ProvedHere` | 2568 | 1 | 0 | \label{cor:virasoro-23-smoothness}Every leading numerator is $\{2, 3\}$-smooth |
| `cor:virasoro-motivic-purity-r-leq-11` | `corollary` | `ProvedHere` | 2598 | 4 | 0 | \label{cor:virasoro-motivic-purity-r-leq-11}Motivic purity through weight 11 (SPECIAL CASE of Theorem~\ref{thm:virasoro-motivic-rationality-all-r}) |
| `lem:subleading-combinatorial-identity` | `lemma` | `ProvedHere` | 2671 | 0 | 0 | \label{lem:subleading-combinatorial-identity}Combinatorial identity for the subleading source |
| `thm:shadow-tower-subleading-closed-form` | `theorem` | `ProvedHere` | 2697 | 2 | 0 | \label{thm:shadow-tower-subleading-closed-form}Closed form for the subleading asymptotic |
| `cor:subleading-characteristic-primes` | `corollary` | `ProvedHere` | 2817 | 2 | 0 | \label{cor:subleading-characteristic-primes}Riccati- arithmetic primes of the subleading layer |
| `thm:shadow-tower-sub-subleading-closed-form-inline` | `theorem` | `ProvedElsewhere` | 2881 | 0 | 0 | \label{thm:shadow-tower-sub-subleading-closed-form-inline} Closed form for the sub-subleading asymptotic |
| `lem:sub-subleading-cubic-identity` | `lemma` | `ProvedHere` | 2952 | 0 | 0 | \label{lem:sub-subleading-cubic-identity} Cubic combinatorial identity |
| `cor:kummer-emergence-at-r-8` | `corollary` | `ProvedHere` | 2999 | 0 | 0 | \label{cor:kummer-emergence-at-r-8}Emergence of the Kummer-irregular prime $691$ at $\Gamma_{8}$ |
| `cor:tier-3-characteristic-primes` | `corollary` | `ProvedHere` | 3051 | 0 | 0 | \label{cor:tier-3-characteristic-primes}Tier-3 prime content through $r = 11$ |
| `thm:shadow-tower-tier-4-closed-form` | `theorem` | `ProvedHere` | 3091 | 0 | 0 | \label{thm:shadow-tower-tier-4-closed-form}Closed form for the Tier-4 sub-sub-subleading asymptotic |
| `lem:quintic-combinatorial` | `lemma` | `ProvedHere` | 3151 | 0 | 0 | \label{lem:quintic-combinatorial}Quintic combinatorial identities |
| `thm:kummer-laurent-depth-controlled` | `theorem` | `ProvedHere` | 3241 | 1 | 0 | \label{thm:kummer-laurent-depth-controlled} Laurent-depth-controlled Kummer emergence |
| `cor:bernoulli-leading-duality-sharpness` | `corollary` | `ProvedHere` | 3358 | 1 | 0 | \label{cor:bernoulli-leading-duality-sharpness} Sharpness of the Bernoulli-leading arithmetic duality |
| `lem:floor-parity-subadditive` | `lemma` | `ProvedHere` | 3471 | 0 | 0 | \label{lem:floor-parity-subadditive}Parity subadditivity of the floor |
| `cor:floor-shift-j-plus-k` | `corollary` | `ProvedHere` | 3498 | 1 | 0 | \label{cor:floor-shift-j-plus-k}Floor shift on the index set of the shadow recurrence |
| `thm:s-r-rational-denominator-pattern` | `theorem` | `ProvedHere` | 3519 | 5 | 0 | \label{thm:s-r-rational-denominator-pattern}Rational denominator pattern for the weighted Virasoro shadow tower |

#### `chapters/theory/shadow_tower_other_class_M_platonic.tex` (11)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:w3-tline-virasoro-inheritance` | `proposition` | `ProvedHere` | 126 | 0 | 0 | $W_3$ $T$-line: full inheritance of the Virasoro tower |
| `cor:w3-tline-asymptotic` | `corollary` | `ProvedHere` | 155 | 1 | 0 | $T$-line asymptotic, $W_3$ |
| `prop:bp-tline-rational` | `proposition` | `ProvedHere` | 295 | 1 | 0 | BP $T$-line: rationality in $k$ |
| `cor:bp-tline-koszul-conductor` | `corollary` | `ProvedHere` | 318 | 0 | 0 | BP $T$-line: Koszul conductor, Feigin--Frenkel duality |
| `prop:bp-jline-gaussian` | `proposition` | `ProvedHere` | 333 | 0 | 0 | BP $J$-line: Gaussian, depth 2 |
| `prop:wn-line-decomposition` | `proposition` | `ProvedHere` | 376 | 0 | 0 | $W_N$ line decomposition of $\kappa$ |
| `prop:w-infinity-line-decomposition` | `proposition` | `ProvedHere` | 458 | 1 | 0 | $W_\infty\lbrack\mu\rbrack$ line-by-line decomposition |
| `prop:super-yangian-kappa` | `proposition` | `ProvedHere` | 532 | 0 | 0 | Super-Yangian modular characteristic |
| `prop:super-yangian-tline-shadow` | `proposition` | `ProvedHere` | 554 | 0 | 0 | Super-Yangian $T$-line: Virasoro shadow with graded parity |
| `cor:super-yangian-tline-asymptotic` | `corollary` | `ProvedHere` | 608 | 0 | 0 | Super-Yangian leading $T$-line asymptotic |
| `rem:wp-cross-channel-quartic` | `remark` | `ProvedHere` | 891 | 0 | 0 | Cross-channel quartic on the $T$-$W$ mixed line |

#### `chapters/theory/shadow_tower_quadrichotomy_platonic.tex` (32)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:mc-recursion-line` | `lemma` | `ProvedElsewhere` | 204 | 1 | 0 | MC recursion, line-restricted |
| `prop:vir-shadow-r5` | `proposition` | `ProvedElsewhere` | 226 | 2 | 2 | Virasoro shadow coefficients through $r = 5$ |
| `thm:riccati-master` | `theorem` | `ProvedHere` | 329 | 1 | 0 | Riccati master equation |
| `prop:riccati-three-presentations` | `proposition` | `ProvedHere` | 378 | 4 | 0 | Three equivalent presentations |
| `thm:spectral-hyperelliptic-pf` | `theorem` | `ProvedHere` | 716 | 3 | 0 | Spectral hyperelliptic curve and Picard--Fuchs |
| `cor:branch-points-instantons` | `corollary` | `ProvedHere` | 769 | 0 | 0 | Branch points and inverse-root actions |
| `thm:stokes-line-c-S` | `theorem` | `ProvedHere` | 793 | 0 | 0 | Virasoro branch-root radius and caesura |
| `thm:S6-Vir-closed` | `theorem` | `ProvedHere` | 872 | 2 | 0 | Shadow coefficient $S_6(\Vir_c)$ closed form |
| `thm:riccati-U` | `theorem` | `ProvedHere` | 909 | 2 | 0 | Riccati-on-$U$ master equation |
| `prop:c1-riccati-mc` | `proposition` | `ProvedHere` | 945 | 3 | 0 | C1: Riccati MC element |
| `thm:borel-summability-classM` | `theorem` | `ProvedHere` | 1021 | 2 | 0 | C3: Algebraic continuation of the class M metric series |
| `thm:c4-shadow-feynman-gk` | `theorem` | `ProvedHere` | 1103 | 0 | 0 | C4: Shadow--Feynman as $\partial^{2} = 0$ at $b_1 = L$ |
| `prop:c5-hardy-ramanujan-cardy` | `proposition` | `ProvedHere` | 1217 | 0 | 0 | Universal Virasoro vacuum growth |
| `thm:c5-zwegers-mu-shadow-explicit` | `theorem` | `ProvedHere` | 1266 | 1 | 0 | Obstruction to a generic Zwegers $\mu$-shadow for $\Vir_c$ |
| `prop:universal-base-CA-six` | `proposition` | `ProvedElsewhere` | 1329 | 0 | 0 | Universal exponential base on the class M $T$-line |
| `prop:w3-Wline-twelve` | `proposition` | `ProvedElsewhere` | 1359 | 0 | 0 | $\cW_3$ second lane $C^{W{\rm-line}}_{\cW_3} = 12$ |
| `prop:virasoro-inverse-root-field` | `proposition` | `ProvedElsewhere` | 1395 | 0 | 0 | Virasoro inverse-root field |
| `prop:lee-yang-phase` | `proposition` | `ProvedElsewhere` | 1410 | 0 | 0 | Lee--Yang pole at $c = -22/5$ |
| `prop:double-root-phase` | `proposition` | `ProvedHere` | 1421 | 1 | 0 | Secondary rational zero at $c = -83/20$ |
| `prop:omega-large-c-expansion` | `proposition` | `ProvedHere` | 1453 | 2 | 0 | Large-$c$ expansion of the Virasoro branch root |
| `prop:beta-N-per-spin-lane` | `proposition` | `ProvedElsewhere` | 1473 | 1 | 0 | $\beta_N = 12 (H_N - 1)$ per-spin lane |
| `prop:wp-triplet-T-Cartan-line` | `proposition` | `ProvedElsewhere` | 1488 | 1 | 0 | $\cW(p)$ triplet $T$-line and Cartan-line shadows |
| `prop:critical-ff-companion-shadow` | `proposition` | `ProvedElsewhere` | 1527 | 3 | 0 | Critical Feigin--Frenkel companion |
| `prop:stqp-312-factor` | `proposition` | `ProvedHere` | 1766 | 3 | 0 | $c_{2d} = -214$ shadow-tower decomposition |
| `prop:stqp-signature` | `proposition` | `ProvedHere` | 2076 | 0 | 0 | Hyperbolic Cartan signature $(2,1)$ for $\mathbf H_{\Delta_5}$ |
| `prop:stqp-unitary-spectrum` | `proposition` | `ProvedHere` | 2174 | 1 | 0 | Positive-energy unitary spectrum |
| `cor:stqp-real-imag-dichotomy` | `corollary` | `ProvedHere` | 2235 | 0 | 0 | Real-root / imaginary-root dichotomy |
| `prop:stqp-theta-p-clustering` | `proposition` | `ProvedHere` | 2403 | 1 | 0 | Observed Fricke-node counts for the 22 primes $p \le 79$ |
| `prop:stqp-gauss-kuzmin` | `proposition` | `ProvedHere` | 2515 | 0 | 0 | Nearest-node deviation statistic on the $22$-prime sample |
| `conj:stqp-gauss-kuzmin-asymptotic` | `proposition` | `ProvedHere` | 2540 | 0 | 0 | Fixed-node Sato--Tate limit and the failure of a $\sqrt p$ law |
| `thm:stqp-fricke-z8-phase-leading` | `theorem` | `ProvedElsewhere` | 2703 | 2 | 0 | $\mathbb Z/8$ half-angle nodes and Sato--Tate leading term |
| `thm:stqp-fricke-z8-phase-subleading` | `theorem` | `ProvedHere` | 2779 | 2 | 0 | $\mathbb Z/8$-phase subleading correction: the $\cos(2\theta^*_k)$ curvature term |

#### `chapters/theory/shadow_tower_sub_subleading_platonic.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
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

#### `chapters/theory/theorem_A_infinity_2.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:archetype-H123-witness` | `lemma` | `ProvedHere` | 579 | 0 | 2 | Archetype witnesses for (H1)--(H3) |
| `prop:fg-ambient-properties` | `proposition` | `ProvedElsewhere` | 1326 | 0 | 2 | $\Fact(X)$ is stable, presentable, symmetric monoidal at the $(\infty,2)$-level |
| `thm:hackney-robertson-model` | `theorem` | `ProvedElsewhere` | 1407 | 1 | 2 | Hackney--Robertson factorization properad model structure |

#### `chapters/theory/theorem_B_scope_platonic.tex` (11)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:weight-filtration-basics` | `lemma` | `ProvedHere` | 99 | 0 | 0 | Filtration basics |
| `lem:total-weight-rees-finite-cdg-tower` | `lemma` | `ProvedHere` | 282 | 2 | 0 | Strict total-weight Rees tower criterion |
| `lem:finite-window-derham-realization-positselski` | `lemma` | `ProvedHere` | 352 | 2 | 1 | Finite-window de Rham realisation for Positselski |
| `lem:hom-cone-ml-rees-towers` | `lemma` | `ProvedHere` | 382 | 1 | 1 | Hom-cone Mittag--Leffler for strict finite-window towers |
| `prop:strict-rlim-verdier-quotient` | `proposition` | `ProvedHere` | 433 | 1 | 0 | $R\!\varprojlim$ commutes with the Verdier quotient under strict ML |
| `prop:completed-second-kind-generator-preservation` | `proposition` | `ProvedHere` | 471 | 2 | 0 | Second-kind acyclicity is preserved by the strict completion |
| `rem:theorem-B-chain-level-G-L-attribution` | `remark` | `ProvedElsewhere` | 691 | 1 | 0 | Chain-level class G and L: external attribution |
| `lem:bar-differential-preserves-monodromy-filtration` | `lemma` | `ProvedHere` | 1863 | 4 | 1 | Bar differential preserves the monodromy-refined filtration |
| `lem:tbsp-bar-valpha1-first-terms` | `lemma` | `ProvedHere` | 3417 | 3 | 2 | First three terms of $B^{\mathrm{ch}}_X(V_{\alpha_1})$ |
| `prop:tbsp-homotopy-n4-valpha1` | `proposition` | `ProvedElsewhere` | 3933 | 0 | 1 | Degree $n=4$ in the two-sided model |
| `prop:tbsp-homotopy-n6-valpha1` | `proposition` | `ProvedElsewhere` | 3992 | 0 | 1 | Degree $n=6$ and absence of a new obstruction |

#### `chapters/theory/theorem_h_off_koszul_platonic.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:theorem-h-off-koszul-explicit-correction` | `theorem` | `ProvedHere` | 290 | 0 | 0 | Off-Koszul high-degree exact sequence |
| `cor:concentration-iff-defect-zero` | `corollary` | `ProvedHere` | 387 | 1 | 0 | Exact defect Hilbert tail |

#### `chapters/theory/three_invariants.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:three-invariants-relations` | `proposition` | `ProvedHere` | 221 | 3 | 0 | Relations and independence |
| `thm:five-class-stratum` | `theorem` | `ProvedHere` | 625 | 2 | 0 | Five-class stratum |
| `prop:coarse-projection-functor` | `proposition` | `ProvedHere` | 674 | 1 | 0 | Coarse projection functor |
| `cor:quadrichotomy-as-projection` | `corollary` | `ProvedHere` | 700 | 1 | 0 | Quadrichotomy $G/L/C/M$ as lossy projection |

#### `chapters/theory/topologization_chain_level_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:QG1-remainder` | `proposition` | `ProvedHere` | 237 | 5 | 0 | Explicit $Q$-variation of $G_1$ |
| `prop:eta-i-primitive` | `proposition` | `ProvedHere` | 326 | 3 | 0 | $\eta_1^{(\mathrm i)}$ is a $Q$-primitive of $R_{\mathrm{ghost}}$ |
| `prop:eta-ii-primitive` | `proposition` | `ProvedHere` | 389 | 2 | 0 | $\eta_1^{(\mathrm{ii})}$ is a $Q$-primitive of $R_{\mathrm{self}}$ |
| `cor:eta-primitive` | `corollary` | `ProvedHere` | 413 | 0 | 0 | $\eta_1$ is a $Q$-primitive of $R_1 := R_{\mathrm{ghost}} + R_{\mathrm{self}}$ |
| `thm:sugawara-antighost-primitive-chain-level` | `theorem` | `ProvedHere` | 425 | 5 | 0 | Sugawara antighost primitive, chain level |
| `prop:translation-inv-tildeG` | `proposition` | `ProvedHere` | 459 | 0 | 0 | Translation invariance of $\widetilde G_1$ |
| `thm:chain-level-E3-top-class-L` | `theorem` | `ProvedHere` | 482 | 1 | 1 | Chain-level $\Ethree^{\mathrm{top}}$ for class $L$ |
| `prop:eta-formula-sl2-k1-explicit` | `proposition` | `ProvedHere` | 541 | 3 | 0 | $\eta_1$ formula at sl$_2$ level $1$ |
| `prop:critical-level-collapse` | `proposition` | `ProvedHere` | 598 | 1 | 1 | Critical-level collapse to $\Etwo^{\mathrm{top}}$ |

#### `chapters/theory/universal_conductor_K_platonic.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:uc-universal-conductor` | `theorem` | `ProvedHere` | 194 | 3 | 0 | \textbf{Universal conductor as ordered-to-symmetric descent} |
| `thm:uc-trinity` | `theorem` | `ProvedHere` | 270 | 2 | 0 | \textbf{Three descriptions of the image} |
| `prop:uc-kernel-dimension` | `proposition` | `ProvedHere` | 329 | 1 | 0 | Schur--Weyl kernel count |
| `thm:uc-kernel-archetypes` | `theorem` | `ProvedHere` | 354 | 4 | 0 | Named kernel witnesses by archetype |
| `thm:uc-landscape-universality` | `theorem` | `ProvedHere` | 479 | 2 | 0 | Constructed universality map on \texorpdfstring{$G/L/C/M$}{G/L/C/M} census rows |
| `thm:uc-K-Atiyah` | `theorem` | `ProvedHere` | 557 | 0 | 0 | Ordered-Koszul boundary for Vol~III comparisons |
| `cor:uc-K-heisenberg` | `corollary` | `ProvedHere` | 650 | 0 | 0 | Heisenberg scalar packages |
| `cor:uc-K-affine-KM` | `corollary` | `ProvedHere` | 671 | 0 | 0 | Affine Kac--Moody scalar packages |
| `cor:uc-K-betagamma` | `corollary` | `ProvedHere` | 698 | 2 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} Verdier scalar sums |
| `cor:uc-K-virasoro` | `corollary` | `ProvedHere` | 724 | 0 | 0 | Virasoro scalar packages |
| `cor:uc-K-WN` | `corollary` | `ProvedHere` | 745 | 0 | 0 | Principal \texorpdfstring{$W_N$}{WN} scalar packages |
| `cor:uc-K-BP` | `corollary` | `ProvedHere` | 782 | 0 | 0 | Bershadsky--Polyakov scalar packages |
| `prop:uc-K3-BKM-scalar-separation` | `proposition` | `ProvedElsewhere` | 832 | 3 | 0 | K3/BKM scalar and taxonomy separation |
| `cor:uc-family-wise-kappa-bucket` | `corollary` | `ProvedHere` | 886 | 9 | 0 | Family-wise scalar complementarity |
| `cor:uc-K-lattice` | `corollary` | `ProvedHere` | 930 | 0 | 0 | Lattice matter presentation |

#### `chapters/theory/virasoro_motivic_purity.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:denominator-structure` | `proposition` | `ProvedHere` | 331 | 6 | 0 | \label{prop:denominator-structure}Denominator of $\widehat S^{\rm wt}_r(\Vir_c)$ |

#### `chapters/theory/virasoro_motivic_purity_all_r_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:virasoro-s-r-motivic-purity-all-r` | `theorem` | `ProvedHere` | 198 | 3 | 0 | \label{thm:virasoro-s-r-motivic-purity-all-r}Virasoro shadow-tower motivic purity, all $r \geq 2$ via master-equation recursion |
| `thm:class-M-motivic-purity-algebras-with-Q-rational-OPE` | `theorem` | `ProvedHere` | 310 | 2 | 0 | \label{thm:class-M-motivic-purity-algebras-with-Q-rational-OPE} Motivic purity on an $F$-rational finite-recurrence lane |
| `prop:mzv-would-enter-at-what-weight` | `proposition` | `ProvedHere` | 403 | 1 | 0 | \label{prop:mzv-would-enter-at-what-weight} Virasoro shadow coefficients contain no odd-zeta of any weight |

#### `chapters/theory/z_g_kummer_bernoulli_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:z-g-closed-form-polynomial` | `theorem` | `ProvedHere` | 60 | 1 | 0 | $Z_g(k)$ closed form |
| `thm:z-g-polynomial-form` | `theorem` | `ProvedHere` | 146 | 2 | 0 | Polynomial factorisation of $Z_g$ |
| `thm:z-g-leading-coefficient-bernoulli` | `theorem` | `ProvedHere` | 209 | 4 | 0 | Hurwitz--Bernoulli leading coefficient |
| `thm:z-g-kummer-congruence` | `theorem` | `ProvedHere` | 324 | 4 | 0 | Irregular-prime witnesses |
| `thm:z-g-s-r-arithmetic-duality` | `theorem` | `ProvedHere` | 528 | 3 | 0 | $Z_g$ vs $S_r(\Vir_c)$ arithmetic duality at the Bernoulli-leading Kummer pair |

### Part II: Examples (585)

#### `chapters/examples/bar_complex_tables.tex` (18)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | `ProvedHere` | 737 | 1 | 0 | Serre tensors are quadratic syzygies, not the dual algebra |
| `comp:sl3-casimir-decomp` | `computation` | `ProvedHere` | 1059 | 0 | 0 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | `ProvedHere` | 1140 | 0 | 0 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | `ProvedHere` | 1476 | 1 | 0 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | `ProvedHere` | 1792 | 1 | 0 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | `ProvedHere` | 1838 | 4 | 0 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | `ProvedHere` | 1910 | 0 | 1 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | `ProvedHere` | 1961 | 1 | 0 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | `ProvedHere` | 2097 | 1 | 0 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | `ProvedHere` | 2133 | 1 | 0 | Bar differential as BGG differential |
| `prop:G2-bar-dims` | `proposition` | `ProvedHere` | 2562 | 2 | 0 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | `ProvedHere` | 2766 | 0 | 0 | Virasoro curvature survives the degree-\texorpdfstring{$3$}{3} residue |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | `ProvedHere` | 2980 | 1 | 0 | Heisenberg bar complex: adjacent residues and central class |
| `prop:km-generic-acyclicity` | `proposition` | `ProvedHere` | 3043 | 1 | 0 | Universal Kac--Moody acyclicity; critical centre separated |
| `prop:w3-vacuum-dichotomy` | `proposition` | `ProvedHere` | 3083 | 2 | 0 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | `ProvedHere` | 3452 | 1 | 0 | Free fermion symmetric bar shadow: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | `ProvedHere` | 3657 | 1 | 0 | \texorpdfstring{$E_8$}{E_8} affine pre-quotient Koszul acyclicity |
| `prop:universal-dim-formula` | `proposition` | `ProvedHere` | 4010 | 2 | 0 | Free PBW bar dimension envelope |

#### `chapters/examples/bershadsky_polyakov.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:bp-central-charge` | `proposition` | `ProvedHere` | 305 | 4 | 1 | BP central charge |
| `thm:bp-koszul-conductor-polynomial` | `theorem` | `ProvedHere` | 365 | 0 | 0 | Bershadsky--Polyakov central-charge conductor identity |
| `prop:sl3-conductor-shift-formula` | `proposition` | `ProvedHere` | 488 | 3 | 0 | Unified shift formula for $\mathfrak{sl}_3$ central-charge conductors |
| `prop:bp-kappa` | `proposition` | `ProvedHere` | 617 | 2 | 0 | Modular characteristic of $\mathcal{B}^k$ |
| `prop:bp-jline-depth` | `proposition` | `ProvedHere` | 843 | 0 | 0 | J-line shadow depth |

#### `chapters/examples/beta_gamma.tex` (24)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:beta-gamma-modes` | `proposition` | `ProvedElsewhere` | 493 | 0 | 1 | Mode algebra \cite{FBZ04} |
| `thm:beta-gamma-stress` | `theorem` | `ProvedElsewhere` | 503 | 0 | 1 | Stress tensor and central charge \cite{FBZ04} |
| `thm:betagamma-fermion-koszul` | `theorem` | `ProvedHere` | 681 | 0 | 1 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | `ProvedHere` | 752 | 1 | 0 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | `ProvedHere` | 809 | 0 | 0 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | `ProvedHere` | 833 | 0 | 0 | — |
| `thm:cobar-fermions` | `theorem` | `ProvedHere` | 864 | 0 | 0 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | `ProvedHere` | 903 | 3 | 0 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:physical-bosonization` | `theorem` | `ProvedElsewhere` | 935 | 1 | 1 | Physical bosonization \cite{FBZ04} |
| `thm:beta-gamma-bar` | `theorem` | `ProvedHere` | 1020 | 1 | 0 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `thm:beta-gamma-universal` | `theorem` | `ProvedElsewhere` | 1070 | 0 | 1 | Universal property of \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} \cite{FBZ04} |
| `prop:betagamma-E1-page` | `proposition` | `ProvedHere` | 1669 | 0 | 1 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-interval-compactification` | `proposition` | `ProvedElsewhere` | 1950 | 0 | 1 | Interval compactification produces the full $\beta\gamma$ algebra {\cite{CDG20}, \S4.2} |
| `prop:mumford-exponent-complementarity` | `proposition` | `ProvedHere` | 2054 | 1 | 0 | Mumford exponent complementarity |
| `thm:betagamma-quartic-birth` | `theorem` | `ProvedHere` | 2395 | 3 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | `ProvedHere` | 2443 | 2 | 0 | $\beta\gamma$ weight-changing line is shadow-trivial |
| `lem:betagamma-ell2-vanishing` | `lemma` | `ProvedHere` | 2712 | 0 | 0 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | `ProvedHere` | 2759 | 4 | 0 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | `ProvedHere` | 2868 | 1 | 0 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | `ProvedHere` | 2903 | 0 | 0 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | `ProvedHere` | 2933 | 1 | 0 | Pure contact boundary law |
| `prop:betagamma-sugawara-class-c` | `proposition` | `ProvedHere` | 3013 | 2 | 0 | Why $\beta\gamma$ is class~$\mathsf{C}$: standard conformal-weight family |
| `prop:betagamma-translation-coproduct` | `proposition` | `ProvedHere` | 3130 | 0 | 0 | Translation and coproduct |
| `prop:betagamma-vortex-comodule` | `proposition` | `ProvedHere` | 3208 | 1 | 0 | $\bar{B}(\cA)$-comodule structure on vortex lines |

#### `chapters/examples/chiral_moonshine_unified.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:bar-euler-hilbert` | `proposition` | `ProvedHere` | 235 | 1 | 0 | Primitive bar-Euler product |
| `thm:moonshine-bar-euler-master` | `theorem` | `ProvedHere` | 295 | 4 | 0 | Denominator/bar-Euler comparison criterion |
| `thm:conway-chiral-structure` | `theorem` | `ProvedElsewhere` | 567 | 1 | 0 | Conway chiral input |

#### `chapters/examples/deformation_quantization.tex` (26)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:kontsevich-star-product` | `theorem` | `ProvedElsewhere` | 52 | 0 | 1 | Kontsevich 1997 \cite{Kon03} |
| `thm:chiral-quantization` | `theorem` | `ProvedHere` | 240 | 0 | 0 | Local coisson quantization and global obstruction |
| `thm:chiral-kontsevich` | `theorem` | `ProvedHere` | 335 | 2 | 0 | Local Kontsevich--chiral comparison |
| `thm:kontsevich-explicit-formula` | `theorem` | `ProvedElsewhere` | 460 | 0 | 1 | Explicit formula \cite{Kon03} |
| `thm:stokes-associativity` | `theorem` | `ProvedElsewhere` | 478 | 0 | 1 | Stokes' theorem yields associativity \cite{Kon03} |
| `thm:bar-computes-deformation` | `theorem` | `ProvedHere` | 541 | 1 | 0 | Chiral deformation complex from the bar construction |
| `prop:mc-star-product` | `proposition` | `ProvedHere` | 604 | 0 | 0 | MC elements and filtered chiral products |
| `lem:defq-shifted-obstruction-cocycle` | `lemma` | `ProvedHere` | 635 | 1 | 0 | Shifted obstruction cocycle |
| `thm:deformation-genus-expansion` | `theorem` | `ProvedHere` | 880 | 1 | 0 | Modular correction package |
| `thm:chiral-formality` | `theorem` | `ProvedElsewhere` | 952 | 0 | 3 | Local \texorpdfstring{$\Etwo$}{E2} formality input \cite{Tamarkin00, FG12} |
| `prop:ainfty-operations-config` | `proposition` | `ProvedElsewhere` | 989 | 0 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} operations \cite{Kon03} |
| `thm:master-identity-deformation` | `theorem` | `ProvedElsewhere` | 1006 | 0 | 1 | Deformation-complex dictionary \cite{Kon03} |
| `thm:obstruction-quantization` | `theorem` | `ProvedElsewhere` | 1182 | 0 | 1 | Obstruction theory \cite{Kon03} |
| `prop:kontsevich-mzv` | `proposition` | `ProvedElsewhere` | 1412 | 0 | 1 | Configuration space periods and associator coefficients \cite{Kon03} |
| `prop:jacobi-nilpotent` | `proposition` | `ProvedHere` | 1826 | 1 | 0 | Cofree Jacobi coderivation square |
| `lem:dcrit-boundary-linear` | `lemma` | `ProvedHere` | 2216 | 1 | 0 | dCrit for boundary-linear $W$ |
| `thm:boundary-linear-lg` | `theorem` | `ProvedHere` | 2314 | 3 | 0 | Boundary-linear LG theorem |
| `prop:defq-data-firewall` | `proposition` | `ProvedHere` | 2653 | 2 | 0 | Classical, quantum, chiral, and centre data are distinct |
| `prop:defq-C1-existence` | `proposition` | `ProvedHere` | 2814 | 1 | 0 | C1 -- formal pole structure under the \(R\)-matrix hypothesis |
| `thm:defq-C2-CYBE` | `theorem` | `ProvedHere` | 2840 | 2 | 0 | Dynamical CYBE for \texorpdfstring{$r(u,Z)$}{r(u,Z)} -- chain-level |
| `thm:defq-C3-lie-bialgebra` | `theorem` | `ProvedHere` | 2912 | 2 | 0 | C3 -- Lie bialgebra |
| `thm:defq-kazhdan-classical-limit` | `theorem` | `ProvedHere` | 2967 | 5 | 0 | Formal classical-limit criterion, Vol~I form |
| `thm:defq-super-kontsevich-formality` | `theorem` | `ProvedElsewhere` | 3056 | 0 | 0 | Finite-truncation super-Kontsevich formality |
| `thm:defq-star-product-specialisation` | `theorem` | `ProvedHere` | 3113 | 2 | 0 | Root-of-unity specialization criterion |
| `thm:defq-unified-motivic-origin` | `theorem` | `ProvedElsewhere` | 3148 | 0 | 0 | Associator coefficients and MZV periods |
| `thm:defq-grt1-equivariance` | `theorem` | `ProvedElsewhere` | 3184 | 0 | 0 | $\mathrm{GRT}_1$-action on formality choices |

#### `chapters/examples/deformation_quantization_examples.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:coisson-coalgebra` | `theorem` | `ProvedElsewhere` | 96 | 0 | 1 | Coisson = \texorpdfstring{$(\chirPois)^c$}{(chirPois)c}-coalgebra; {} \cite{BD04} |
| `thm:pinf-formality` | `theorem` | `ProvedElsewhere` | 118 | 2 | 2 | Formality for \texorpdfstring{$\Pinf$}{P-infinity}-chiral; {} \cite{Kon03,FG12} |
| `thm:obstructions` | `theorem` | `ProvedElsewhere` | 180 | 1 | 1 | Obstruction classes; {} \cite{Kon03} |
| `thm:green-schwarz` | `theorem` | `ProvedElsewhere` | 212 | 0 | 1 | Green--Schwarz mechanism; {} \cite{Pol98} |
| `thm:mc-quantization` | `theorem` | `ProvedElsewhere` | 235 | 0 | 2 | MC elements and quantization; {} \cite{Kon03,KontsevichSoibelman} |
| `prop:lattice-one-step` | `proposition` | `ProvedHere` | 465 | 1 | 0 | Lattice deformation is one-step |
| `prop:chiral-dcrit` | `proposition` | `ProvedElsewhere` | 686 | 1 | 1 | Chiral enhancement of the derived critical locus; {} \cite{DNP25} |

#### `chapters/examples/exceptional_yangian_koszul_duality_platonic.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:exceptional-yangian-type-separation` | `proposition` | `ProvedHere` | 144 | 0 | 0 | Type separation for Yangian-facing claims |
| `prop:exceptional-yangian-template` | `proposition` | `ProvedHere` | 210 | 4 | 2 | Finite-window inverse-kernel criterion |
| `lem:exceptional-finite-window-promotion` | `lemma` | `ProvedHere` | 281 | 2 | 0 | Finite-window evidence and tower promotion |
| `prop:exceptional-yangian-ordered-bar-averaging` | `proposition` | `ProvedHere` | 307 | 1 | 0 | Ordered bar data before symmetric averaging |
| `thm:exceptional-yangian-pbw-grw18` | `proposition` | `ProvedElsewhere` | 357 | 1 | 1 | Scope of Guay--Regelskis--Wendlandt |
| `cor:exceptional-yangian-graded` | `corollary` | `ProvedHere` | 377 | 1 | 0 | Exceptional current-algebra dimensions |
| `prop:exceptional-fundamental-packet-scope` | `proposition` | `ProvedHere` | 423 | 1 | 0 | Fundamental packets are not RTT certificates |
| `prop:exceptional-yangian-koszul-E6` | `proposition` | `ProvedHere` | 472 | 2 | 0 | $E_6$ RTT implication criterion |
| `prop:exceptional-yangian-koszul-E7` | `proposition` | `ProvedHere` | 513 | 1 | 0 | $E_7$ RTT implication criterion |
| `prop:exceptional-yangian-koszul-E8` | `proposition` | `ProvedHere` | 547 | 1 | 0 | $E_8$ RTT implication criterion |
| `prop:exceptional-yangian-koszul-F4` | `proposition` | `ProvedHere` | 584 | 1 | 0 | $F_4$ RTT implication criterion |
| `prop:exceptional-yangian-koszul-G2` | `proposition` | `ProvedHere` | 624 | 1 | 0 | $G_2$ RTT implication criterion |
| `thm:exceptional-yangian-koszul-duality-all-five-types` | `theorem` | `ProvedHere` | 666 | 9 | 0 | Exceptional-type Yangian Koszul duality: exact obligations |
| `cor:exceptional-yangian-all-simple` | `corollary` | `ProvedHere` | 730 | 1 | 2 | All-simple-type statement remains conditional |
| `prop:exceptional-yangian-no-dk-root-k3-promotion` | `proposition` | `ProvedHere` | 762 | 7 | 0 | Drinfeld--Kohno, roots of unity, and K3 do not promote the exceptional RTT statement |

#### `chapters/examples/free_fields.tex` (50)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fermion-shadow-metric` | `proposition` | `ProvedHere` | 590 | 1 | 0 | Shadow metric of the free fermion |
| `prop:fermion-rmatrix` | `proposition` | `ProvedHere` | 703 | 2 | 0 | Free fermion $r$-matrix |
| `thm:fermion-sewing` | `theorem` | `ProvedHere` | 825 | 1 | 0 | Free fermion sewing |
| `prop:bc-general-spin-class-c` | `proposition` | `ProvedElsewhere` | 1089 | 1 | 0 | $bc$ ghost system at general spin: class~C for all $\lambda$ |
| `thm:single-fermion-boson-duality` | `theorem` | `ProvedHere` | 1138 | 0 | 0 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | `ProvedHere` | 1225 | 1 | 0 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | `ProvedHere` | 1294 | 1 | 0 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | `ProvedHere` | 1351 | 0 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-deformation-channels` | `proposition` | `ProvedHere` | 1481 | 1 | 0 | $\beta\gamma$ deformation complex |
| `comp:betagamma-shadow-weights` | `computation` | `ProvedHere` | 1668 | 2 | 0 | $\beta\gamma$ shadow obstruction tower: special weight table |
| `prop:betagamma-weight-symmetry` | `proposition` | `ProvedHere` | 1704 | 1 | 0 | Weight symmetry $\neq$ Koszul duality |
| `thm:heisenberg-bar` | `theorem` | `ProvedHere` | 1794 | 6 | 0 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | `ProvedHere` | 1820 | 0 | 0 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | `ProvedHere` | 1879 | 1 | 0 | Heisenberg curved cobar structure |
| `thm:lattice-voa-bar` | `theorem` | `ProvedHere` | 1951 | 0 | 0 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | `ProvedHere` | 1983 | 0 | 0 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | `ProvedHere` | 2018 | 0 | 0 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | `ProvedHere` | 2057 | 0 | 0 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | `ProvedHere` | 2122 | 0 | 0 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | `ProvedHere` | 2150 | 1 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `thm:heisenberg-koszul-dual-early` | `theorem` | `ProvedHere` | 2446 | 3 | 3 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | `ProvedHere` | 2487 | 1 | 0 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | `ProvedHere` | 2624 | 2 | 0 | Fock module bar resolution |
| `cor:fock-character-koszul` | `corollary` | `ProvedHere` | 2729 | 2 | 0 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | `ProvedHere` | 2771 | 1 | 0 | Ext groups between Fock modules |
| `thm:heisenberg-not-self-dual` | `theorem` | `ProvedHere` | 3285 | 1 | 1 | Heisenberg is not self-dual |
| `thm:rhagavendran-heisenberg` | `theorem` | `ProvedElsewhere` | 3377 | 0 | 1 | Heisenberg duality \cite{CG17} |
| `thm:heisenberg-genus-g` | `theorem` | `ProvedHere` | 3449 | 6 | 0 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | `ProvedHere` | 3758 | 0 | 0 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | `ProvedHere` | 3872 | 2 | 0 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | `ProvedHere` | 4157 | 5 | 0 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | `ProvedHere` | 4311 | 0 | 0 | Heisenberg geometric bar differential |
| `lem:bar-dims-partitions` | `lemma` | `ProvedHere` | 4366 | 3 | 0 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | `ProvedHere` | 4437 | 0 | 0 | Heisenberg level inversion: curved duality |
| `prop:spin-structure-count` | `proposition` | `ProvedElsewhere` | 4552 | 0 | 2 | Spin structure count |
| `thm:fermion-genus1-partition` | `theorem` | `ProvedHere` | 4606 | 2 | 0 | Free fermion genus-1 partition functions |
| `prop:ising-fermion` | `proposition` | `ProvedElsewhere` | 4948 | 0 | 1 | Ising $=$ free fermion |
| `prop:bosonization` | `proposition` | `ProvedElsewhere` | 5009 | 0 | 2 | Bosonization formula |
| `thm:virasoro-moduli` | `theorem` | `ProvedHere` | 5182 | 0 | 1 | Critical Virasoro descent at $c = 26$ |
| `prop:moduli-degeneration` | `proposition` | `ProvedHere` | 5291 | 0 | 0 | Boundary-residue differential on moduli forms |
| `thm:brst-cohomology` | `theorem` | `ProvedElsewhere` | 5367 | 0 | 1 | Critical bosonic BRST complex \cite{Pol98} |
| `thm:genus-g-chiral-homology` | `theorem` | `ProvedHere` | 5542 | 3 | 0 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:bar-string-integrand` | `theorem` | `ProvedHere` | 5811 | 1 | 0 | Bar classes on moduli and boundary factorization |
| `thm:modular-anomaly` | `theorem` | `ProvedElsewhere` | 5934 | 0 | 0 | Belavin--Knizhnik anomaly condition |
| `thm:w-classical-integrability` | `theorem` | `ProvedElsewhere` | 6221 | 0 | 1 | Classical \texorpdfstring{$\mathcal{W}$}{W}-algebra integrability |
| `comp:fermion-five-theorems` | `computation` | `ProvedHere` | 6351 | 2 | 0 | Five projections of $\Theta_{\mathcal{F}}$ |
| `comp:lattice-five-theorems` | `computation` | `ProvedHere` | 6511 | 0 | 0 | Five projections of $\Theta_{V_\Lambda}$ |
| `thm:filtered-bar-complex` | `theorem` | `ProvedHere` | 6611 | 0 | 0 | Filtered bar complex |
| `thm:curved-koszul-duality` | `theorem` | `ProvedElsewhere` | 6642 | 0 | 1 | Curved Koszul duality \cite{Positselski11} |
| `prop:massive-chiral-contractible` | `proposition` | `ProvedElsewhere` | 6680 | 0 | 0 | Massive chirals have contractible bar complexes |

#### `chapters/examples/genus_expansions.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `__unlabeled_chapters/examples/genus_expansions.tex:289` | `corollary` | `ProvedHere` | 289 | 0 | 0 | Lattice-independence of genus expansion |
| `prop:sl2-complementarity-all-genera` | `proposition` | `ProvedHere` | 689 | 0 | 0 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:integrable-level-independence` | `proposition` | `ProvedElsewhere` | 790 | 3 | 0 | Level-independence at integrable levels |
| `prop:km-genus2-propagator` | `proposition` | `ProvedHere` | 904 | 5 | 0 | Non-abelian genus-2 propagator |
| `prop:w3-genus4-cross-channel` | `proposition` | `ProvedHere` | 1590 | 1 | 0 | Genus-4 cross-channel correction |
| `comp:w4-w5-grav-cross` | `computation` | `ProvedHere` | 1660 | 1 | 0 | Universal gravitational cross-channel: $\cW_4$ and $\cW_5$ specializations |
| `comp:w4-full-ope-examples` | `computation` | `ProvedHere` | 1734 | 2 | 1 | $\cW_4$ full-OPE cross-channel: the first irrational correction |
| `prop:genus-expansion-convergence` | `proposition` | `ProvedHere` | 1932 | 1 | 0 | Convergence of the scalar genus expansion |
| `prop:complementarity-genus-series` | `proposition` | `ProvedHere` | 1998 | 1 | 0 | Central charge genus series |
| `prop:bar-verlinde-asymptotics` | `proposition` | `ProvedHere` | 2147 | 1 | 1 | Bar free energy and Verlinde determinant curvature |
| `prop:vir-complementarity` | `proposition` | `ProvedHere` | 2378 | 0 | 0 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | `ProvedHere` | 2499 | 0 | 0 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `prop:bc-betagamma-complementarity` | `proposition` | `ProvedHere` | 2725 | 0 | 0 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:universal-fe-ratios` | `proposition` | `ProvedHere` | 2982 | 1 | 0 | Universal free-energy ratios |
| `prop:neumann-character` | `proposition` | `ProvedElsewhere` | 4127 | 0 | 1 | Neumann pure-gauge character |
| `prop:dirichlet-character-genus` | `proposition` | `ProvedElsewhere` | 4148 | 0 | 1 | Dirichlet character |
| `prop:multi-chiral-product-characters` | `proposition` | `ProvedElsewhere` | 4229 | 0 | 0 | Multi-chiral product formulas |

#### `chapters/examples/heisenberg_eisenstein.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:heisenberg-gaussian-termination` | `proposition` | `ProvedHere` | 124 | 1 | 0 | Gaussian shadow termination for Heisenberg |
| `prop:heisenberg-r-matrix` | `proposition` | `ProvedHere` | 411 | 1 | 0 | Heisenberg $r$-matrix |
| `prop:eisenstein-modular` | `proposition` | `ProvedElsewhere` | 557 | 0 | 1 | Modular transformation laws \cite{Kac} |
| `thm:heisenberg-genus-zero` | `theorem` | `ProvedElsewhere` | 594 | 1 | 1 | Genus zero correlation functions \cite{FBZ04} |
| `thm:heisenberg-genus-one-complete` | `theorem` | `ProvedHere` | 626 | 0 | 0 | Genus-1 Heisenberg bar kernels |
| `thm:heisenberg-genus-two` | `theorem` | `ProvedHere` | 751 | 0 | 0 | Genus-2 Heisenberg kernel |
| `thm:heisenberg-all-genus` | `theorem` | `ProvedHere` | 989 | 1 | 0 | Heisenberg at general genus |
| `prop:modular-weight-formula` | `proposition` | `ProvedElsewhere` | 1071 | 0 | 2 | Eisenstein normalization and scalar scope \cite{Igusa62,Klingen67} |
| `thm:eta-appearance` | `theorem` | `ProvedHere` | 1108 | 0 | 0 | Partition-function normalizations and determinant line |
| `prop:multi-boson-eisenstein` | `proposition` | `ProvedHere` | 1530 | 0 | 0 | Multi-boson elliptic coefficients |
| `thm:heisenberg-exact-linearity` | `theorem` | `ProvedHere` | 1834 | 1 | 0 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | `ProvedHere` | 1874 | 3 | 0 | Heisenberg shadow obstruction tower: finite termination at degree~$2$ |
| `prop:heisenberg-open-sector` | `proposition` | `ProvedHere` | 2337 | 0 | 1 | Completed Fock open sector for Heisenberg |

#### `chapters/examples/kac_moody.tex` (51)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:km-genus1-hessian` | `computation` | `ProvedHere` | 457 | 2 | 0 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `thm:critical-level-structure` | `theorem` | `ProvedElsewhere` | 548 | 0 | 1 | Feigin--Frenkel center at critical level \cite{Feigin-Frenkel} |
| `thm:vertex-chiral-equivalence` | `theorem` | `ProvedElsewhere` | 658 | 0 | 2 | Equivalence of perspectives \cite{FBZ04, BD04} |
| `prop:km-critical-separation` | `proposition` | `ProvedHere` | 780 | 5 | 0 | Critical-level separation of affine invariants |
| `thm:geometric-ope-kac-moody` | `theorem` | `ProvedHere` | 877 | 2 | 0 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | `ProvedHere` | 931 | 2 | 0 | Level-shifting duality, abstract form |
| `thm:wakimoto-brst-full-nondegenerate` | `theorem` | `ProvedHere` | 1152 | 0 | 3 | Wakimoto BRST exactness on the generic nonresonant locus |
| `thm:sl2-critical` | `theorem` | `ProvedElsewhere` | 1490 | 0 | 1 | Critical level simplification for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} \cite{Feigin-Frenkel} |
| `thm:sl2-koszul-dual` | `theorem` | `ProvedHere` | 1513 | 1 | 0 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:w3-wakimoto-sl3` | `theorem` | `ProvedElsewhere` | 1707 | 0 | 1 | Wakimoto for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} \cite{Frenkel-Kac-Wakimoto92} |
| `thm:sl3-koszul-dual` | `theorem` | `ProvedHere` | 1726 | 2 | 0 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | `ProvedHere` | 1770 | 2 | 0 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | `ProvedHere` | 1810 | 4 | 0 | Curved level decomposition of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | `ProvedHere` | 1911 | 1 | 0 | Critical-level curved spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | `ProvedHere` | 1999 | 0 | 0 | Generic level-independence on the curvature-flat comparison surface |
| `thm:universal-kac-moody-koszul` | `theorem` | `ProvedHere` | 2139 | 1 | 0 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | `ProvedHere` | 2182 | 1 | 0 | Killing form via structure constants |
| `thm:principal-w-algebra-structure` | `theorem` | `ProvedElsewhere` | 3039 | 0 | 2 | Principal \texorpdfstring{$\mathcal{W}$}{W}-algebra structure \cite{FF, Ara07} |
| `thm:km-higher-genus-corrections` | `theorem` | `ProvedHere` | 3099 | 3 | 0 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | `ProvedHere` | 3184 | 1 | 0 | Closed-form current presentation in the Koszul dual |
| `thm:km-quantum-groups` | `theorem` | `ProvedHere` | 3597 | 3 | 1 | Quantum-group parameter inversion |
| `prop:spectral-flow-koszul` | `proposition` | `ProvedElsewhere` | 3807 | 0 | 1 | Spectral flow and Koszul duality \cite{Kac} |
| `thm:bar-verlinde-recovery` | `theorem` | `ProvedElsewhere` | 3883 | 0 | 0 | Verlinde recovery from the bar complex |
| `thm:admissible-rep-theory` | `theorem` | `ProvedElsewhere` | 3973 | 1 | 2 | Representation theory at admissible level \cite{KW88, Arakawa17} |
| `prop:bar-admissible` | `proposition` | `ProvedHere` | 3999 | 4 | 0 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | `ProvedHere` | 4071 | 4 | 0 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-general-rank` | `theorem` | `ProvedElsewhere` | 4371 | 1 | 1 | Kac--Wakimoto character formula in general rank |
| `prop:ds-admissible` | `proposition` | `ProvedElsewhere` | 4704 | 2 | 1 | DS reduction at admissible level \cite{Arakawa17} |
| `prop:whittaker-ds` | `proposition` | `ProvedElsewhere` | 4785 | 0 | 3 | Whittaker modules and DS reduction \cite{Arakawa17} |
| `prop:bar-whittaker` | `proposition` | `ProvedHere` | 4843 | 1 | 1 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | `ProvedHere` | 4931 | 4 | 0 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-genus1-curvature` | `theorem` | `ProvedHere` | 5262 | 5 | 0 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:affine-cubic-normal-form` | `theorem` | `ProvedHere` | 6036 | 0 | 0 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | `ProvedHere` | 6072 | 2 | 0 | Affine shadow obstruction tower: finite termination at degree~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | `ProvedHere` | 6110 | 2 | 0 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | `ProvedHere` | 6153 | 1 | 0 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | `ProvedHere` | 6223 | 3 | 0 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | `ProvedHere` | 6271 | 5 | 0 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | `ProvedHere` | 6328 | 2 | 0 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | `ProvedHere` | 6405 | 5 | 0 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | `ProvedHere` | 6491 | 2 | 0 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | `ProvedHere` | 6527 | 1 | 0 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | `ProvedHere` | 6707 | 2 | 0 | Vanishing of the genus loop on the affine cubic |
| `prop:km-cubic-shadow-level-independence` | `proposition` | `ProvedHere` | 6773 | 1 | 0 | Level-independence of the cubic shadow product |
| `prop:nsl-shadow-tower` | `proposition` | `ProvedHere` | 6898 | 3 | 0 | Non-simply-laced shadow obstruction tower |
| `prop:complete-exceptional-shadow` | `proposition` | `ProvedHere` | 7080 | 3 | 0 | Complete exceptional shadow data |
| `prop:exceptional-anomaly-ratios` | `proposition` | `ProvedHere` | 7170 | 1 | 0 | Anomaly ratios for exceptional principal $\mathcal{W}$-algebras |
| `prop:affine-cs-action` | `proposition` | `ProvedElsewhere` | 7292 | 0 | 2 | The holomorphic-topological Chern--Simons action |
| `prop:level-rank-boundary-voa` | `proposition` | `ProvedElsewhere` | 7423 | 0 | 1 | Level-rank duality for boundary VOAs |
| `cor:level-rank-bar-intertwining` | `corollary` | `ProvedHere` | 7439 | 1 | 0 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | `ProvedHere` | 7468 | 0 | 0 | Kappa anti-symmetry under Feigin--Frenkel involution |

#### `chapters/examples/landscape_census.tex` (18)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:minimal-model-class-transport` | `proposition` | `ProvedHere` | 817 | 0 | 0 | Minimal-model class transport |
| `prop:virasoro-shadow-canonical` | `proposition` | `ProvedHere` | 874 | 1 | 0 | Virasoro shadow-tower coefficients; canonical values |
| `prop:census-conductor-row-count` | `proposition` | `ProvedHere` | 1033 | 2 | 0 | Conductor-domain census count |
| `prop:fateev-lukyanov-canonical` | `proposition` | `ProvedHere` | 2977 | 1 | 1 | Fateev--Lukyanov central-charge formula; canonical form |
| `cor:subexp-free-field` | `corollary` | `ProvedHere` | 3799 | 3 | 0 | Sub-exponential growth in the computed rows |
| `cor:algebraicity-koszul` | `corollary` | `ProvedHere` | 3815 | 2 | 0 | Closed forms for computed interacting rows |
| `thm:ds-spectral-branch-preservation` | `theorem` | `ProvedHere` | 4009 | 0 | 0 | Divisor-core form of DS sub-discriminance |
| `prop:ds-invariant-discriminant` | `proposition` | `ProvedHere` | 4123 | 0 | 0 | A2 divisor-core calculation |
| `thm:discriminant-linear-dependence` | `theorem` | `ProvedHere` | 4730 | 2 | 0 | Linear dependence in the rank-one branch family |
| `lem:bar-deg2-symmetric-square` | `lemma` | `ProvedHere` | 4955 | 1 | 0 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | `ProvedHere` | 5006 | 0 | 0 | Exponential growth rate in a finite-character Kac--Moody chart |
| `thm:dominant-branch-point` | `theorem` | `ProvedHere` | 5030 | 1 | 0 | Dominant branch point in a finite-character Kac--Moody chart |
| `prop:landscape-k3-bkm-taxonomy` | `proposition` | `ProvedElsewhere` | 5913 | 1 | 0 | K3/BKM scalar invariants and Hall--Drinfeld taxonomy |
| `prop:canonical-prs-coefficient-cm214` | `proposition` | `ProvedElsewhere` | 6033 | 0 | 0 | Pope--Romans--Shen projector coefficient at $c=-214$ |
| `prop:canonical-monster-atlas-values` | `proposition` | `ProvedElsewhere` | 6072 | 0 | 0 | Monster ATLAS character values at reference conjugacy classes |
| `prop:canonical-bruinier-heegner-chern` | `proposition` | `ProvedElsewhere` | 6125 | 0 | 0 | Bruinier Heegner Chern-class values at rank-$5$ and rank-$2$ paramodular cusps |
| `prop:canonical-oberdieck-phi01` | `proposition` | `ProvedElsewhere` | 6187 | 0 | 0 | Half K3 Jacobi coefficients and the doubled OP trace |
| `prop:canonical-bcov-quintic` | `proposition` | `ProvedElsewhere` | 6241 | 0 | 0 | BCOV genus-$1$ and genus-$2$ constant-map contributions on the quintic mirror |

#### `chapters/examples/lattice_foundations.tex` (35)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:lattice-sewing` | `theorem` | `ProvedHere` | 134 | 4 | 0 | Lattice sewing envelope |
| `lem:lattice:cocycle-class` | `lemma` | `ProvedHere` | 441 | 0 | 0 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | `ProvedHere` | 605 | 2 | 0 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:frenkel-kac` | `theorem` | `ProvedElsewhere` | 678 | 1 | 3 | Frenkel--Kac--Segal; {} \cite{FK80,Se81} |
| `thm:lattice:bar-structure` | `theorem` | `ProvedHere` | 930 | 2 | 0 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | `ProvedHere` | 1027 | 0 | 0 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | `ProvedHere` | 1050 | 2 | 0 | \texorpdfstring{$E_8$}{E8} bar coalgebra and discriminant-trivial self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | `ProvedHere` | 1097 | 2 | 0 | Unimodular lattice bar-coalgebra self-duality |
| `thm:lattice:koszul-dual` | `theorem` | `ProvedHere` | 1160 | 0 | 0 | Dual coalgebra of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | `ProvedHere` | 1213 | 1 | 0 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | `ProvedHere` | 1469 | 0 | 0 | Tensor product from direct sum |
| `cor:lattice:kunneth` | `corollary` | `ProvedElsewhere` | 1494 | 2 | 1 | K\"unneth for bar complexes \cite{LV12} |
| `prop:lattice:sublattice` | `proposition` | `ProvedHere` | 1514 | 0 | 0 | Sublattice maps |
| `thm:lattice:overlattice` | `theorem` | `ProvedElsewhere` | 1568 | 0 | 1 | Overlattice vertex algebra \cite{FLM88} |
| `thm:lattice:hochschild` | `theorem` | `ProvedHere` | 1834 | 0 | 0 | Lattice chiral Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | `ProvedHere` | 1879 | 0 | 0 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | `ProvedHere` | 1921 | 0 | 0 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | `ProvedHere` | 1944 | 0 | 0 | Modular invariance |
| `prop:lattice:niemeier-theta-decomposition` | `proposition` | `ProvedHere` | 2083 | 0 | 0 | Niemeier theta series decomposition |
| `prop:lattice:self-dual-criterion` | `proposition` | `ProvedHere` | 2361 | 1 | 0 | Discriminant-trivial module-envelope criterion |
| `prop:lattice:D4-triality` | `proposition` | `ProvedHere` | 2388 | 2 | 0 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | `ProvedHere` | 2427 | 1 | 0 | Lattice twisted-sector charge inversion on the bar surface |
| `prop:lattice:deformation-properties` | `proposition` | `ProvedHere` | 2614 | 2 | 0 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | `ProvedHere` | 2800 | 1 | 0 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | `ProvedHere` | 3432 | 2 | 0 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | `ProvedHere` | 3509 | 3 | 0 | \texorpdfstring{$\Eone$}{E1} adjacent-root bar quotient |
| `prop:lattice:screening-structure` | `proposition` | `ProvedHere` | 3753 | 2 | 0 | Screening current structure |
| `prop:lattice:genus1-simple-pole` | `proposition` | `ProvedHere` | 5123 | 0 | 0 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | `ProvedHere` | 5140 | 2 | 0 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | `ProvedHere` | 5249 | 2 | 0 | Lattice shadow obstruction tower: termination at weight~$2$ |
| `thm:lattice:e1-hochschild` | `theorem` | `ProvedHere` | 5326 | 1 | 0 | $\Eone$ lattice chiral Hochschild complex |
| `prop:xxx-shadow-data` | `proposition` | `ProvedHere` | 5429 | 3 | 0 | XXX shadow data |
| `prop:transfer-matrix-shadow-dict` | `proposition` | `ProvedHere` | 5468 | 0 | 0 | Transfer matrix--shadow dictionary |
| `prop:xxz-shadow-data` | `proposition` | `ProvedHere` | 5518 | 0 | 0 | XXZ shadow data |
| `prop:shadow-cardy-corrections` | `proposition` | `ProvedHere` | 5585 | 0 | 0 | Shadow hierarchy and Cardy corrections |

#### `chapters/examples/level1_bridge.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:level1-kappa-reduction` | `proposition` | `ProvedHere` | 228 | 4 | 0 | Level-$1$ $\kappa$ reduction |
| `prop:level1-cubic-vanishing` | `proposition` | `ProvedHere` | 325 | 1 | 0 | Cubic shadow vanishing at level~$1$ |
| `comp:level1-ade-bridge` | `computation` | `ProvedHere` | 445 | 1 | 0 | Level-$1$ bridge data for the simply-laced series |

#### `chapters/examples/logarithmic_w_algebras.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:wp-kappa` | `proposition` | `ProvedHere` | 205 | 1 | 1 | Virasoro-line $\kappa$ for $\cW(p)$ |
| `prop:wp-c2-cofinite` | `proposition` | `ProvedElsewhere` | 295 | 0 | 1 | $C_2$-cofiniteness of $\cW(p)$ |
| `prop:wp-not-free-strong` | `proposition` | `ProvedHere` | 337 | 1 | 0 | No finite free strong generation |
| `prop:wp-modules` | `proposition` | `ProvedElsewhere` | 506 | 0 | 2 | Module category of $\cW(p)$ |

#### `chapters/examples/minimal_model_examples.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:tricritical-s-matrix` | `proposition` | `ProvedElsewhere` | 258 | 0 | 1 | Tricritical Ising S-matrix \cite{BPZ84} |
| `prop:potts-quantum-dim` | `proposition` | `ProvedElsewhere` | 400 | 0 | 1 | Three-state Potts quantum dimensions \cite{Verlinde} |
| `thm:fusion-bar-torus` | `theorem` | `ProvedHere` | 432 | 3 | 0 | Fusion from bar complex on the torus |
| `thm:minimal-model-characters` | `theorem` | `ProvedElsewhere` | 492 | 0 | 1 | Virasoro minimal model characters \cite{FF84} |
| `prop:ising-koszul-dual` | `proposition` | `ProvedHere` | 665 | 1 | 0 | Koszul dual complementarity |
| `prop:ising-free-energies` | `proposition` | `ProvedHere` | 705 | 0 | 0 | Ising scalar free energies |

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
| `prop:fusion-ring-p-2` | `proposition` | `ProvedHere` | 680 | 1 | 0 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | `ProvedHere` | 707 | 3 | 0 | Fusion ring as polynomial quotient |
| `prop:fusion-quantum-group` | `proposition` | `ProvedElsewhere` | 735 | 0 | 2 | Connection to quantum group \cite{KL93} |
| `thm:minimal-model-mtc` | `theorem` | `ProvedElsewhere` | 777 | 2 | 1 | Minimal models form modular tensor categories |
| `comp:twist-5-4` | `computation` | `ProvedHere` | 803 | 0 | 0 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `thm:mtc-tqft` | `theorem` | `ProvedElsewhere` | 828 | 0 | 1 | MTC determines a 3d TQFT \cite{RT91} |

#### `chapters/examples/n2_superconformal.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:n2-kappa` | `proposition` | `ProvedHere` | 208 | 1 | 0 | Modular characteristic of the $\mathcal{N}=2$ SCA;\ |
| `prop:n2-complementarity` | `proposition` | `ProvedHere` | 257 | 0 | 0 | Complementarity for the $\mathcal{N}=2$ SCA;\ |
| `prop:n2-koszulness` | `proposition` | `ProvedHere` | 303 | 1 | 1 | PBW Koszulness of the $\mathcal{N}=2$ SCA;\ |

#### `chapters/examples/shadow_tower_extended_families.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:canonical-two-point-norms` | `proposition` | `ProvedElsewhere` | 76 | 1 | 4 | Canonical two-point norms |
| `prop:fateev-lukyanov-alpha` | `proposition` | `ProvedElsewhere` | 146 | 0 | 1 | Fateev--Lukyanov $W \cdot W$ coefficient at weight four |
| `thm:w3-s3-s4-tline` | `theorem` | `ProvedHere` | 176 | 0 | 0 | $\cW_3$ closed forms: $T$-line |
| `thm:w3-w-line-s4-zamolodchikov` | `theorem` | `ProvedHere` | 205 | 3 | 0 | $\cW_3$ closed forms: $W$-line with Zamolodchikov denominator |
| `thm:bp-t-line-rational-k` | `theorem` | `ProvedHere` | 282 | 2 | 0 | BP closed forms: $T$-line rational in $k$ |
| `thm:bp-other-lines` | `theorem` | `ProvedHere` | 346 | 1 | 0 | BP $J$-line and $G^\pm$ line |
| `cor:bp-feigin-frenkel-complementarity` | `corollary` | `ProvedHere` | 396 | 1 | 0 | Feigin--Frenkel complementarity on BP $T$-line |
| `thm:super-yangian-fermionic-line-sign` | `theorem` | `ProvedHere` | 517 | 0 | 0 | Super-Yangian $\mathfrak{gl}(1\|1)$ fermionic-line sign |

#### `chapters/examples/symmetric_orbifolds.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:symn-averaging-kernel` | `proposition` | `ProvedHere` | 80 | 1 | 0 | Ordered data and symmetric shadow |
| `prop:symn-kappa` | `proposition` | `ProvedHere` | 194 | 0 | 0 | Identity-sector modular characteristic |
| `prop:symn-twist-vanishing` | `proposition` | `ProvedHere` | 287 | 1 | 0 | Twist weights and the identity vacuum |
| `prop:symn-shadow-depth` | `proposition` | `ProvedHere` | 437 | 0 | 0 | Diagonal shadow depth of the fixed-point sector |
| `prop:symn-cycle-index-plethystic` | `proposition` | `ProvedHere` | 579 | 2 | 1 | Cycle-index and plethystic normalization |
| `prop:symn-dmvv-kappa` | `proposition` | `ProvedHere` | 653 | 3 | 0 | DMVV does not compute ordered-bar $\kappa$ |
| `prop:symn-hecke-kappa` | `proposition` | `ProvedHere` | 935 | 2 | 0 | Hecke operators and the identity scalar |

#### `chapters/examples/w3_composite_fields.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | `ProvedElsewhere` | 81 | 2 | 2 | Virasoro composite and Fateev--Lukyanov coefficient |
| `prop:lambda-modes` | `proposition` | `ProvedHere` | 161 | 0 | 0 | Mode expansion |
| `thm:c-scaling` | `theorem` | `ProvedHere` | 212 | 0 | 0 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | `ProvedElsewhere` | 310 | 1 | 1 | Zamolodchikov normalization checks |
| `thm:w-w-ope-complete` | `theorem` | `ProvedElsewhere` | 356 | 1 | 1 | \texorpdfstring{$W$}{W}-\texorpdfstring{$W$}{W} OPE complete expansion \cite{Zamolodchikov} |
| `prop:lambda23-quasiprimary` | `proposition` | `ProvedElsewhere` | 503 | 2 | 0 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | `ProvedElsewhere` | 522 | 0 | 0 | Weight-6 Gram determinant |
| `prop:W-squared-qp` | `proposition` | `ProvedHere` | 572 | 1 | 0 | Finite-window quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | `ProvedElsewhere` | 610 | 0 | 0 | Visible norm of \texorpdfstring{$\Xi_W$}{XiW} |
| `thm:w3-null-level1` | `theorem` | `ProvedHere` | 668 | 2 | 0 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | `ProvedHere` | 771 | 0 | 0 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | `ProvedHere` | 826 | 2 | 0 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | `ProvedHere` | 868 | 2 | 0 | Kac determinant vanishing locus at level~1 |
| `thm:w3-kac-general` | `theorem` | `ProvedElsewhere` | 885 | 1 | 2 | \texorpdfstring{$W_3$}{W_3} Kac determinant: general structure |
| `comp:w3-gram-level2` | `computation` | `ProvedHere` | 925 | 2 | 0 | Level-2 Gram matrix |

#### `chapters/examples/w3_holographic_datum.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:w3hol-conductor` | `theorem` | `ProvedHere` | 324 | 1 | 0 | Koszul conductor and self-dual point |
| `thm:w3hol-r-channels` | `theorem` | `ProvedHere` | 448 | 1 | 0 | Channel-by-channel \texorpdfstring{$r$}{r}-matrix |
| `prop:w3hol-lambda-on-primaries` | `proposition` | `ProvedElsewhere` | 514 | 0 | 0 | Action of \texorpdfstring{$\Lambda_0$}{Lambda 0} on primaries |
| `cor:w3hol-lambda-roots` | `corollary` | `ProvedHere` | 547 | 0 | 0 | Roots of \texorpdfstring{$\Lambda_0$}{Lambda 0} on the conformal axis |
| `prop:w3hol-deltaF3-finite-window` | `proposition` | `ProvedElsewhere` | 610 | 2 | 0 | Genus-3 finite stable-graph correction |
| `thm:w3hol-Q-T` | `theorem` | `ProvedHere` | 782 | 1 | 0 | Weighted shadow metric on the \texorpdfstring{$T$}{T}-line |
| `thm:w3hol-Q-W` | `theorem` | `ProvedHere` | 813 | 1 | 0 | Shadow metric on the \texorpdfstring{$W$}{W}-line |
| `thm:w3hol-commuting-differentials` | `theorem` | `ProvedHere` | 900 | 1 | 0 | Commuting differentials at \texorpdfstring{$N=3$}{N=3} |

#### `chapters/examples/w_algebras.tex` (62)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:w3-genus1-hessian` | `computation` | `ProvedHere` | 326 | 0 | 0 | The $\mathcal W_3$ genus-$1$ Hessian |
| `comp:w-entropy-ladder` | `computation` | `ProvedHere` | 368 | 1 | 0 | Completion entropy ladder |
| `prop:slodowy-properties` | `proposition` | `ProvedElsewhere` | 889 | 0 | 1 | Properties of the Slodowy slice |
| `thm:slodowy-quantization` | `theorem` | `ProvedElsewhere` | 921 | 0 | 3 | Quantization of Slodowy slices \textup{(}Gan--Ginzburg, Premet\textup{)} |
| `thm:arakawa-variety-intersection` | `theorem` | `ProvedElsewhere` | 973 | 0 | 2 | Arakawa's geometric localization for DS reduction |
| `thm:brst-properties` | `theorem` | `ProvedElsewhere` | 1104 | 0 | 1 | Properties of BRST cohomology \cite{FF} |
| `thm:generators-screening` | `theorem` | `ProvedElsewhere` | 1116 | 0 | 1 | Generators via screening \cite{Frenkel-Kac-Wakimoto92} |
| `thm:gko-coset` | `theorem` | `ProvedElsewhere` | 1185 | 0 | 1 | GKO coset for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} \cite{GKO85} |
| `thm:w-geometric-ope` | `theorem` | `ProvedHere` | 1276 | 0 | 1 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | `ProvedHere` | 1355 | 1 | 0 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `prop:virasoro-from-sl2` | `proposition` | `ProvedElsewhere` | 1503 | 0 | 1 | Virasoro from \texorpdfstring{$\mathfrak{sl}_2$}{sl2} \cite{FF} |
| `thm:virasoro-self-duality` | `theorem` | `ProvedHere` | 1578 | 2 | 0 | Virasoro quadratic self-duality |
| `prop:w3-central-charge` | `proposition` | `ProvedElsewhere` | 2045 | 0 | 1 | Central charge from level \cite{Zamolodchikov} |
| `thm:w3-wakimoto` | `theorem` | `ProvedElsewhere` | 2061 | 1 | 1 | Wakimoto realization of \texorpdfstring{$\mathcal{W}_3$}{W3} \cite{Frenkel-Kac-Wakimoto92} |
| `thm:feigin-frenkel-center` | `theorem` | `ProvedElsewhere` | 2707 | 0 | 1 | Feigin--Frenkel: centers at critical level \cite{Feigin-Frenkel} |
| `thm:w-ainfty-ops` | `theorem` | `ProvedHere` | 2857 | 2 | 0 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `prop:w-module-structure` | `proposition` | `ProvedElsewhere` | 3227 | 0 | 1 | Structure of \texorpdfstring{$\mathcal{W}$}{W}-algebra modules \cite{Arakawa17} |
| `prop:w3-topological-enhancement` | `proposition` | `ProvedElsewhere` | 3529 | 1 | 1 | Topological enhancement in the $\mathcal{W}_3$ case |
| `prop:w3-3d-action` | `proposition` | `ProvedElsewhere` | 3659 | 2 | 1 | 3d HT Poisson sigma model for $\mathcal{W}_3$ {\cite{KhanZeng25}} |
| `prop:w3-cc-arithmetic` | `proposition` | `ProvedElsewhere` | 3703 | 3 | 0 | Central-charge arithmetic and the genus-1 computation |
| `prop:virasoro-beltrami-phase-space` | `proposition` | `ProvedElsewhere` | 3764 | 0 | 1 | Beltrami--quadratic-differential phase space; {} \cite{KhanZeng25} |
| `prop:schwarzian-central-charge` | `proposition` | `ProvedElsewhere` | 3786 | 0 | 1 | Schwarzian cocycle and central charge; {} \cite{KhanZeng25} |
| `prop:virasoro-3d-gravity-action` | `proposition` | `ProvedElsewhere` | 3805 | 3 | 1 | The 3d Virasoro gravity action; {} \cite{KhanZeng25} |
| `thm:w-universal-gravitational-cubic` | `theorem` | `ProvedHere` | 3927 | 0 | 0 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | `ProvedHere` | 3982 | 1 | 0 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | `ProvedHere` | 4019 | 1 | 0 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | `ProvedHere` | 4102 | 1 | 0 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-w3-mixed-shadow` | `theorem` | `ProvedHere` | 4576 | 2 | 0 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w3-two-dim-hessian-cubic` | `proposition` | `ProvedHere` | 4640 | 2 | 0 | Two-dimensional Hessian and universal cubic |
| `thm:w3-quartic-channel-decomposition` | `theorem` | `ProvedHere` | 4668 | 2 | 0 | $\mathcal{W}_3$ quartic channel decomposition |
| `prop:w3-denominator-filtration` | `proposition` | `ProvedHere` | 4729 | 2 | 0 | Denominator filtration by $W$-charge |
| `prop:rho-decreasing-with-N` | `proposition` | `ProvedHere` | 4873 | 1 | 0 | Asymptotic $T$-line shadow growth at fixed positive level |
| `prop:w-w3-weight6-resonance` | `proposition` | `ProvedHere` | 5000 | 1 | 0 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | `ProvedHere` | 5067 | 1 | 0 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | `ProvedHere` | 5093 | 0 | 0 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-virasoro-quintic-forced` | `theorem` | `ProvedHere` | 5287 | 2 | 0 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | `ProvedHere` | 5344 | 1 | 0 | Explicit quintic shadow for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | `ProvedHere` | 5911 | 2 | 0 | $\mathcal{W}_3$ quintic obstruction |
| `prop:w3-wline-ring-relations` | `proposition` | `ProvedHere` | 6132 | 2 | 0 | Autonomous $W$-line ring relations |
| `thm:w-finite-degree-polynomial-pva` | `theorem` | `ProvedHere` | 6428 | 0 | 1 | Finite-degree theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | `ProvedHere` | 6466 | 2 | 0 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | `ProvedHere` | 6508 | 1 | 0 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | `ProvedHere` | 6535 | 0 | 0 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | `ProvedHere` | 6611 | 2 | 0 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | `ProvedHere` | 6636 | 3 | 0 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | `ProvedHere` | 6670 | 1 | 0 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | `ProvedHere` | 6708 | 1 | 0 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | `ProvedHere` | 6728 | 6 | 0 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `prop:miura-degree-sharp` | `proposition` | `ProvedHere` | 6812 | 1 | 0 | Miura degree bound is sharp |
| `thm:w-pbw-slodowy-collapse` | `theorem` | `ProvedHere` | 6964 | 0 | 0 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | `ProvedHere` | 7025 | 1 | 0 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-degree-detection` | `theorem` | `ProvedHere` | 7134 | 0 | 0 | Canonical degree detection |
| `thm:w-bp-strict` | `theorem` | `ProvedHere` | 7160 | 1 | 0 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | `ProvedHere` | 7208 | 1 | 0 | $\mathcal{W}_4^{(2)}$ has canonical degree~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | `ProvedHere` | 7267 | 1 | 0 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | `ProvedHere` | 7326 | 0 | 0 | Subregular Appell formula |
| `thm:w-unbounded-canonical-degree` | `theorem` | `ProvedHere` | 7364 | 4 | 0 | Unbounded canonical degree |
| `cor:w-subregular-degree-staircase` | `corollary` | `ProvedHere` | 7393 | 2 | 0 | The subregular degree staircase |
| `thm:w-subregular-classification` | `theorem` | `ProvedHere` | 7435 | 7 | 0 | Subregular classification |
| `prop:sl3-nilpotent-shadow-data` | `proposition` | `ProvedHere` | 7521 | 0 | 1 | $\mathfrak{sl}_3$ nilpotent orbits: shadow data |
| `prop:sl4-hook-shadow-data` | `proposition` | `ProvedHere` | 7571 | 0 | 0 | $\mathfrak{sl}_4$ hook-type shadow data |
| `thm:ds-shadow-functor-degree2` | `theorem` | `ProvedHere` | 7613 | 1 | 0 | DS shadow functor at degree~$2$ on computed type-$A$ rows |

#### `chapters/examples/w_algebras_deep.tex` (43)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:jet-flag` | `theorem` | `ProvedElsewhere` | 145 | 0 | 1 | Jet bundle realization \cite{BD04} |
| `thm:w-cdr` | `theorem` | `ProvedElsewhere` | 184 | 0 | 1 | \texorpdfstring{$\mathcal{W}$}{W}-algebras as chiral de Rham \cite{Arakawa17} |
| `thm:w-bar-coalg` | `theorem` | `ProvedHere` | 214 | 2 | 0 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:screen-res` | `theorem` | `ProvedElsewhere` | 276 | 0 | 1 | Screening resolution \cite{Frenkel-Kac-Wakimoto92} |
| `thm:w-toda` | `theorem` | `ProvedElsewhere` | 469 | 0 | 1 | \texorpdfstring{$\mathcal{W}$}{W}-algebras and Toda systems \cite{FF} |
| `thm:master-commutative-square` | `theorem` | `ProvedHere` | 1651 | 3 | 2 | Master commutative square for DS reduction |
| `prop:w3-deg3-vacuum` | `proposition` | `ProvedHere` | 2071 | 2 | 0 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `thm:transport-closure-type-a` | `theorem` | `ProvedHere` | 2590 | 1 | 0 | Transport-closure in type $A$ |
| `prop:abelian-locus-type-a` | `proposition` | `ProvedHere` | 3537 | 0 | 0 | Abelian locus in type~$A$ |
| `prop:abelianity-complementarity-independence` | `proposition` | `ProvedHere` | 3580 | 1 | 0 | Independence of abelianity and same-family duality |
| `prop:bfn-slodowy-dimensions` | `proposition` | `ProvedHere` | 3611 | 0 | 1 | BFN--Slodowy dimension matching |
| `prop:svir-3d-sugra-action` | `proposition` | `ProvedElsewhere` | 3755 | 0 | 0 | SuperVirasoro 3d HT lift |
| `thm:winfty-scalar` | `theorem` | `ProvedHere` | 3916 | 0 | 0 | One-dimensional scalar cyclic line for $\mathcal{W}_\infty$ |
| `prop:gram-wt4` | `proposition` | `ProvedHere` | 4063 | 0 | 0 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | `ProvedHere` | 4128 | 0 | 0 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | `ProvedHere` | 4171 | 2 | 0 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:higher-w-gravitational-cubic` | `proposition` | `ProvedHere` | 4370 | 1 | 0 | Gravitational cubic for $\Walg_N$ |
| `prop:higher-w-parity` | `proposition` | `ProvedHere` | 4413 | 0 | 0 | $\mathbb{Z}_2$ parity and the cubic shadow |
| `prop:weight-4-exchange-upgrade` | `proposition` | `ProvedHere` | 4472 | 1 | 0 | Weight-$4$ exchange spectrum upgrade at rank~$3$ |
| `prop:virasoro-primitive` | `proposition` | `ProvedHere` | 4776 | 1 | 0 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | `ProvedHere` | 4837 | 1 | 0 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | `ProvedHere` | 4878 | 1 | 0 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | `ProvedHere` | 4981 | 0 | 0 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | `ProvedHere` | 5014 | 1 | 0 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | `ProvedHere` | 5035 | 1 | 0 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | `ProvedHere` | 5067 | 0 | 0 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | `ProvedHere` | 5174 | 0 | 0 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | `ProvedHere` | 5210 | 2 | 0 | $\Walg_\infty$ bar-window series and Koszul entropy |
| `thm:n2-kappa` | `theorem` | `ProvedHere` | 5456 | 1 | 0 | $N=2$ modular characteristic |
| `prop:n2-koszul-duality` | `proposition` | `ProvedHere` | 5512 | 0 | 0 | $N=2$ Koszul duality |
| `prop:n2-channel-decomposition` | `proposition` | `ProvedHere` | 5583 | 0 | 0 | $N=2$ channel decomposition |
| `prop:n2-bosonic-shadow-metric` | `proposition` | `ProvedHere` | 5616 | 0 | 0 | $N=2$ bosonic shadow metric |
| `prop:n2-minimal-models` | `proposition` | `ProvedHere` | 5661 | 1 | 0 | $N=2$ minimal model shadow data |
| `thm:walgdeep-gaiotto-siegel-weight` | `theorem` | `ProvedHere` | 6213 | 4 | 0 | Borcherds / Siegel weight for class-$\mathcal S$ $A_{N-1}$ on $\Sigma_{0,24}$ |
| `thm:walgdeep-N6-reanchoring` | `theorem` | `ProvedHere` | 6439 | 2 | 0 | $N = 6$ umbral re-anchoring to $6 D_4$ |
| `lem:walgdeep-rank-arithmetic` | `lemma` | `ProvedHere` | 6521 | 0 | 0 | Rank arithmetic of $(24/N) A_{N-1}$ |
| `thm:walgdeep-N6-reanchor-A5-4-D4` | `theorem` | `ProvedHere` | 6541 | 2 | 2 | $N=6$ re-anchor to $A_5^4 D_4$ |
| `thm:walgdeep-N7-N8-re-anchor` | `theorem` | `ProvedHere` | 6745 | 2 | 7 | $N = 7$ and $N = 8$ re-anchors; ladder continuity $k_N^{\mathrm{int}} = N + 3$ |
| `thm:walgdeep-divisor-rule` | `theorem` | `ProvedHere` | 6925 | 1 | 1 | Corrected divisor rule for naive umbral labelling |
| `thm:walgdeep-substitute-anchors` | `theorem` | `ProvedHere` | 6987 | 1 | 0 | Substitute Niemeier anchors at $N \in \{8, 12\}$ via rank-gluing |
| `thm:walgdeep-N24-conway` | `theorem` | `ProvedHere` | 7048 | 0 | 0 | $N = 24$ escape to Conway moonshine via Leech |
| `thm:walgdeep-N9-N12-re-anchor` | `theorem` | `ProvedHere` | 7209 | 2 | 8 | $N \in \{9, 10, 11, 12\}$ re-anchors; ladder continuity $k_N^{\mathrm{int}} = N + 3$ across the Coxeter-void |
| `thm:walgdeep-N13-N24-ladder` | `theorem` | `ProvedHere` | 7474 | 3 | 4 | $N \in \{13, \ldots, 24\}$ ladder; four-regime completion terminating at the Leech escape |

#### `chapters/examples/y_algebras.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:y-central-charge` | `theorem` | `ProvedHere` | 209 | 1 | 0 | {Central charge of $Y_{N_1,N_2,N_3}[\Psi |
| `comp:y-special-cases-c` | `computation` | `ProvedHere` | 237 | 2 | 0 | Special cases of the central charge |
| `thm:y111-central-charge` | `theorem` | `ProvedHere` | 275 | 1 | 0 | $c(Y_{1,1,1}) = 0$ |
| `prop:y-koszul-dual` | `proposition` | `ProvedHere` | 434 | 2 | 0 | {Koszul dual of $Y_{N_1,N_2,N_3}[\Psi |
| `thm:y-shadow-depth` | `theorem` | `ProvedHere` | 500 | 1 | 0 | Shadow depth of $Y$-algebras |
| `comp:y111-collision-residue` | `computation` | `ProvedHere` | 584 | 1 | 0 | {Collision residue for $Y_{1,1,1}[\Psi |
| `comp:y-wn-specialization` | `computation` | `ProvedHere` | 692 | 1 | 0 | $Y_{0,0,N} \simeq \cW_N \times \mathfrak{gl}(1)$ |
| `comp:y-affine-specialization` | `computation` | `ProvedHere` | 714 | 1 | 0 | $Y_{N,0,0} \simeq \widehat{\mathfrak{gl}}(N)$ |

#### `chapters/examples/yangians_computations.tex` (43)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bfn` | `theorem` | `ProvedElsewhere` | 37 | 0 | 1 | BFN construction |
| `conj:yangian-spectral-selfdual` | `proposition` | `ProvedHere` | 419 | 0 | 0 | Scalar-gauge inverse and sign reversal |
| `prop:yangian-rank-dependence` | `proposition` | `ProvedHere` | 614 | 0 | 0 | Finite-window rank dependence of the Yangian bar complex |
| `comp:sl3-yangian-from-ordered-bar` | `computation` | `ProvedHere` | 663 | 1 | 0 | The \texorpdfstring{$\mathfrak{sl}_3$}{sl3} KZ residue and fundamental Yang seed |
| `thm:quantum-rmatrix-shadow` | `theorem` | `ProvedHere` | 996 | 1 | 0 | Fundamental quantum \texorpdfstring{$R$}{R}-matrix and classical residue |
| `prop:colored-rmatrix` | `proposition` | `ProvedElsewhere` | 1070 | 2 | 0 | Colored $R$-matrices and Casimir eigenvalues |
| `prop:eval-module-bar` | `proposition` | `ProvedHere` | 1401 | 0 | 0 | Evaluation quotient bar complex |
| `prop:dk2-thick-generation-typeA` | `proposition` | `ProvedHere` | 1679 | 0 | 1 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `lem:composition-thick-generation` | `lemma` | `ProvedHere` | 1795 | 0 | 0 | Thick generation from finite composition series |
| `lem:monoidal-thick-extension` | `lemma` | `ProvedHere` | 2154 | 0 | 0 | Monoidal extension to thick closures |
| `lem:fd-thick-closure` | `lemma` | `ProvedHere` | 2348 | 0 | 0 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | `ProvedHere` | 2434 | 0 | 2 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | `ProvedHere` | 2685 | 1 | 0 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | `ProvedHere` | 2816 | 2 | 0 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | `ProvedHere` | 2974 | 0 | 0 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | `ProvedHere` | 2994 | 1 | 0 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | `ProvedHere` | 3019 | 1 | 0 | Sectorwise localizing generation |
| `prop:lqt-e1-subexponential-growth` | `proposition` | `ProvedHere` | 3091 | 0 | 0 | Sub-exponential growth of the \texorpdfstring{$E_1$}{E_1} page |
| `thm:baxter-exact-triangles-opoly` | `theorem` | `ProvedHere` | 3257 | 2 | 1 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `thm:baxter-exact-triangles` | `theorem` | `ProvedHere` | 3298 | 4 | 1 | Baxter exact triangles on shifted envelope \texorpdfstring{$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$}{Osh} |
| `prop:baxter-yangian-equivariance` | `proposition` | `ProvedHere` | 3369 | 0 | 0 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | `ProvedHere` | 3442 | 3 | 0 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `prop:prefundamental-clebsch-gordan` | `proposition` | `ProvedHere` | 3920 | 0 | 0 | Universal prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | `ProvedHere` | 3958 | 0 | 0 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | `ProvedHere` | 3971 | 2 | 0 | $K_0$ generation for all simple types |
| `prop:categorical-cg-typeA` | `proposition` | `ProvedHere` | 4020 | 2 | 2 | Categorical prefundamental CG decomposition, type~$A$ |
| `thm:mc3-arbitrary-type` | `theorem` | `ProvedHere` | 4519 | 1 | 6 | Categorical prefundamental CG decomposition, all types |
| `prop:e8-root-uniformity` | `proposition` | `ProvedHere` | 5033 | 0 | 0 | $E_8$ relevant-root uniformity |
| `prop:character-cg-all-types` | `proposition` | `ProvedHere` | 5043 | 0 | 0 | Character-level Clebsch--Gordan for all simple types |
| `prop:monopole-hilbert-decomp` | `proposition` | `ProvedElsewhere` | 5348 | 0 | 1 | Hilbert space decomposition |
| `prop:dirichlet-character` | `proposition` | `ProvedElsewhere` | 5368 | 0 | 1 | Dirichlet boundary character |
| `prop:gauge-koszul-dual-shifted-cotangent` | `proposition` | `ProvedElsewhere` | 5439 | 0 | 1 | Koszul dual of gauge boundary chiral algebra |
| `thm:yangian-vector-seed-propagation` | `theorem` | `ProvedHere` | 5648 | 1 | 0 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | `ProvedHere` | 5678 | 0 | 0 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | `ProvedHere` | 5701 | 0 | 0 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | `ProvedHere` | 5716 | 0 | 0 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | `ProvedHere` | 5767 | 1 | 0 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | `ProvedHere` | 5792 | 0 | 0 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | `ProvedHere` | 5819 | 0 | 0 | Derived realization of the Baxter--Rees family |
| `thm:yangian-H2-reduction` | `theorem` | `ProvedHere` | 5886 | 1 | 0 | $H^2$-reduction to the three-leg sector |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | `ProvedHere` | 5972 | 0 | 0 | Concrete cocycle |
| `thm:u-zeta-8-PBW-wall-crossing` | `theorem` | `ProvedHere` | 6112 | 2 | 0 | Formal PBW increment past the De Concini--Kac wall $N = \ell/2 = 4$ |
| `rem:u-zeta-8-PBW-plateau` | `remark` | `ProvedHere` | 6148 | 0 | 0 | Plateau and the Lusztig Frobenius kernel |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (30)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:dk0-four-path` | `computation` | `ProvedHere` | 312 | 0 | 0 | Four-path Drinfeld--Kohno verification |
| `prop:finite-stage-tangent` | `proposition` | `ProvedHere` | 2014 | 0 | 1 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | `ProvedHere` | 2095 | 0 | 0 | Mittag-Leffler for finite RTT bar windows |
| `lem:yangian-fd-fundamental-generation` | `lemma` | `ProvedHere` | 3335 | 2 | 0 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | `ProvedHere` | 3365 | 1 | 2 | Finite-dimensional quantum-loop factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | `ProvedHere` | 3535 | 0 | 2 | Type-\texorpdfstring{$A$}{A} quantum-loop fundamental packet is generated by the vector evaluation line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | `ProvedHere` | 3663 | 0 | 2 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | `ProvedHere` | 3701 | 0 | 1 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-tower-mc4-criterion` | `proposition` | `ProvedHere` | 4759 | 4 | 0 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | `ProvedHere` | 4822 | 5 | 0 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | `ProvedHere` | 4857 | 0 | 0 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | `ProvedHere` | 4911 | 4 | 0 | Standard RTT tower satisfies the M-level MC4 package |
| `prop:free-propagator-matching` | `proposition` | `ProvedHere` | 6882 | 2 | 0 | Free/Heisenberg propagator matching |
| `prop:affine-propagator-matching` | `proposition` | `ProvedHere` | 6927 | 0 | 0 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `prop:rmatrix-pole-landscape` | `proposition` | `ProvedHere` | 7018 | 2 | 0 | The collision-residue $r$-matrix across the standard landscape |
| `prop:bosonic-parity-constraint` | `proposition` | `ProvedHere` | 7124 | 0 | 0 | Bosonic parity constraint on $r$-matrix poles |
| `prop:cybe-from-mc` | `proposition` | `ProvedHere` | 7167 | 4 | 0 | CYBE from bar-complex MC equation |
| `prop:rmatrix-from-bar-coproduct` | `proposition` | `ProvedHere` | 7280 | 6 | 1 | KZ-normalized quantum $R$-matrix from ordered bar transport |
| `thm:spectral-derived-additive-kz` | `theorem` | `ProvedHere` | 8476 | 0 | 0 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | `ProvedHere` | 8574 | 1 | 0 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | `ProvedHere` | 8620 | 0 | 0 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | `ProvedHere` | 8693 | 1 | 0 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | `ProvedHere` | 8776 | 0 | 0 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | `ProvedHere` | 8832 | 0 | 0 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | `ProvedHere` | 8874 | 1 | 0 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | `ProvedHere` | 8909 | 0 | 0 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | `ProvedHere` | 8963 | 0 | 0 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | `ProvedHere` | 9034 | 0 | 0 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | `ProvedHere` | 9058 | 0 | 0 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | `ProvedHere` | 9097 | 0 | 0 | Exact free transport |

#### `chapters/examples/yangians_foundations.tex` (43)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:super-berezinian-central-automorphism` | `proposition` | `ProvedElsewhere` | 104 | 1 | 3 | Nazarov centrality and super-trace complementarity |
| `thm:yangian-e1` | `theorem` | `ProvedHere` | 542 | 3 | 0 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | `ProvedHere` | 681 | 3 | 0 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | `ProvedHere` | 723 | 2 | 0 | Finite-window Yangian inverse-kernel duality |
| `cor:yangian-classical-self-dual` | `corollary` | `ProvedHere` | 833 | 0 | 0 | RTT associated-graded classical limit |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | `ProvedHere` | 1811 | 4 | 0 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | `ProvedHere` | 1966 | 0 | 0 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | `ProvedHere` | 2070 | 1 | 0 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | `ProvedHere` | 2088 | 0 | 0 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | `ProvedHere` | 2118 | 0 | 0 | Explicit coefficient formula for the fundamental monodromy series |
| `prop:dg-shifted-rtt-boundary-support-bound` | `proposition` | `ProvedHere` | 2180 | 3 | 0 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | `ProvedHere` | 2244 | 3 | 0 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | `ProvedHere` | 2330 | 2 | 0 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | `ProvedHere` | 2427 | 2 | 0 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | `ProvedHere` | 2497 | 1 | 0 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | `ProvedHere` | 2566 | 1 | 0 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | `ProvedHere` | 2603 | 1 | 0 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | `ProvedHere` | 2659 | 1 | 0 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | `ProvedHere` | 2719 | 2 | 0 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | `ProvedHere` | 2780 | 7 | 0 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | `ProvedHere` | 2879 | 3 | 0 | Standard type-A fundamental line operator has the standard local residue |
| `prop:gauge-theory-koszul-dual` | `proposition` | `ProvedElsewhere` | 3155 | 0 | 0 | Gauge theory $\cA^!$ as shifted cotangent loop algebra |
| `thm:gauge-theory-yangian-structure` | `theorem` | `ProvedElsewhere` | 3194 | 0 | 1 | Full dg-shifted Yangian structure on $\cA^!$ |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | `ProvedHere` | 3308 | 0 | 0 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | `ProvedHere` | 3335 | 1 | 0 | Stabilized completed bar/cobar recovery |
| `thm:shifted-rtt-mc-descent` | `theorem` | `ProvedHere` | 3396 | 0 | 0 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | `ProvedHere` | 3485 | 0 | 0 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | `ProvedHere` | 3530 | 0 | 0 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | `ProvedHere` | 3578 | 0 | 0 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | `ProvedHere` | 3594 | 1 | 0 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | `ProvedHere` | 3625 | 0 | 0 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | `ProvedHere` | 3658 | 0 | 0 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | `ProvedHere` | 3695 | 0 | 0 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | `ProvedHere` | 3720 | 0 | 0 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | `ProvedHere` | 3792 | 1 | 0 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | `ProvedHere` | 3841 | 0 | 0 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | `ProvedHere` | 3867 | 0 | 0 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | `ProvedHere` | 3894 | 0 | 0 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | `ProvedHere` | 3916 | 0 | 0 | Kleinian associated graded at the nilpotent point |
| `thm:kzb-as-bar-cobar-alpha` | `theorem` | `ProvedElsewhere` | 4054 | 0 | 0 | KZB as elliptic bar--cobar twisting at leading $\alpha$ |
| `prop:elliptic-coproduct-coassoc-fay` | `proposition` | `ProvedHere` | 4087 | 0 | 0 | Elliptic coproduct is Fay-coassociative |
| `thm:felder-R-half-braiding` | `theorem` | `ProvedHere` | 4114 | 0 | 0 | Felder $R$-matrix as half-braiding |
| `prop:sl2-elliptic-yangian-triangle` | `proposition` | `ProvedHere` | 4133 | 0 | 0 | $\slnn{2}$ elliptic triangle coherence at order $\hbar$ |

### Part III: Connections (305)

#### `chapters/connections/arithmetic_shadows.tex` (120)

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
| `prop:niemeier-multichannel` | `proposition` | `ProvedHere` | 820 | 1 | 0 | Multi-channel Niemeier discrimination |
| `prop:shadow-arithmetic-factorization` | `proposition` | `ProvedHere` | 907 | 0 | 0 | Shadow--arithmetic factorization |
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
| `thm:partition-modular-classification` | `theorem` | `ProvedHere` | 3338 | 1 | 0 | Benchmark partition-function modular classes |
| `prop:quasi-modular-propagator` | `proposition` | `ProvedHere` | 3403 | 1 | 0 | Quasi-modular content from the genus-$1$ propagator |
| `prop:hecke-eigenvalue-extraction` | `proposition` | `ProvedHere` | 3478 | 1 | 0 | Hecke eigenvalues from partition data |
| `prop:tau-large-primes` | `proposition` | `ProvedHere` | 3517 | 1 | 0 | Ramanujan $\tau(p)$ at primes $83 \leq p \leq 113$ |
| `prop:tau-primes-211-229` | `proposition` | `ProvedHere` | 3584 | 0 | 0 | Ramanujan $\tau(p)$ at primes $p\in\{211,223,227,229\}$ |
| `prop:moment-matrix-negativity` | `proposition` | `ProvedHere` | 3701 | 0 | 0 | Eisenstein moment minor |
| `thm:shadow-eisenstein` | `theorem` | `ProvedElsewhere` | 3869 | 0 | 0 | The genus-$1$ amplitude Mellin transform is Eisenstein |
| `rem:shadow-eisenstein-numerical-check` | `remark` | `ProvedHere` | 4082 | 3 | 0 | The value at $s = 0$ separates the two Dirichlet series |
| `thm:shadow-bps` | `theorem` | `ProvedHere` | 5046 | 2 | 0 | Leading plethystic shadow of the Virasoro obstruction tower |
| `cor:shadow-fredholm` | `corollary` | `ProvedElsewhere` | 5314 | 0 | 0 | Shadow Fredholm determinant |
| `prop:mc-bracket-determines-atoms` | `proposition` | `ProvedHere` | 5564 | 2 | 0 | MC bracket in a two-atom spectral ansatz |
| `rem:mc-ramanujan-bridge` | `remark` | `ProvedHere` | 5618 | 2 | 0 | The bridge to the Ramanujan bound |
| `prop:koszul-field-criterion` | `proposition` | `ProvedHere` | 5849 | 2 | 0 | Koszul field-preservation criterion |
| `prop:heisenberg-koszul-epstein` | `proposition` | `ProvedHere` | 6090 | 1 | 0 | Degenerate case: Heisenberg |
| `comp:virasoro-c1-koszul-epstein` | `computation` | `ProvedHere` | 6143 | 0 | 0 | Virasoro at $c = 1$: numerical Koszul--Epstein value |
| `comp:fe-minimal-models` | `computation` | `ProvedHere` | 6168 | 1 | 0 | Functional equation for all unitary minimal models |
| `thm:spectral-continuation-bridge` | `theorem` | `ProvedHere` | 6249 | 3 | 0 | Hecke-equivariant MC element under finite-span stability |
| `thm:schur-complement-quartic` | `theorem` | `ProvedHere` | 6495 | 1 | 0 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | `ProvedHere` | 6554 | 0 | 0 | — |
| `prop:on-off-line-distinction` | `proposition` | `ProvedHere` | 6631 | 1 | 0 | — |
| `prop:li-criterion-failure` | `proposition` | `ProvedHere` | 7041 | 2 | 1 | Structural failure of the Li criterion for the sewing lift |
| `prop:pure-spin-s-schur` | `proposition` | `ProvedHere` | 7187 | 1 | 0 | — |
| `prop:prime-side-defect-formula` | `proposition` | `ProvedHere` | 7295 | 1 | 0 | — |
| `thm:finite-miura-defect` | `theorem` | `ProvedHere` | 7365 | 2 | 0 | Finite Miura defect at genus one |
| `prop:bracket-hodge-index` | `proposition` | `ProvedHere` | 7980 | 0 | 0 | Bracket positivity and the Hodge index |
| `prop:lattice-ramanujan` | `proposition` | `ProvedHere` | 8106 | 0 | 1 | Ramanujan bound for lattice spectral measures |
| `prop:shadow-symmetric-power` | `proposition` | `ProvedHere` | 8148 | 0 | 0 | Prime-local shadow--symmetric power criterion |
| `thm:petersson-identification` | `theorem` | `ProvedHere` | 8299 | 1 | 0 | Petersson identification under finite Hecke span |
| `prop:rigidity-threshold` | `proposition` | `ProvedHere` | 8424 | 1 | 0 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | `ProvedHere` | 8524 | 2 | 1 | Lattice Ramanujan from rigidity hypotheses |
| `prop:stieltjes-signed-universal` | `proposition` | `ProvedHere` | 8726 | 1 | 0 | Weighted Virasoro signed Stieltjes obstruction |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | `ProvedHere` | 8765 | 0 | 0 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | `ProvedHere` | 8828 | 3 | 0 | Shadow arithmetic trichotomy |
| `prop:genus1-weight-bound` | `proposition` | `ProvedHere` | 8902 | 0 | 0 | Weight bound for genus-$1$ shadow projections |
| `thm:mc-recursion-moment` | `theorem` | `ProvedHere` | 9045 | 0 | 0 | MC recursion on moment $L$-functions |
| `thm:hecke-newton-lattice` | `theorem` | `ProvedHere` | 9190 | 5 | 0 | Hecke--Newton closure for lattice VOAs under finite Hecke span |
| `thm:non-lattice-ramanujan` | `theorem` | `ProvedHere` | 9289 | 0 | 1 | Non-lattice Ramanujan implication |
| `prop:mc-constraint-counting` | `proposition` | `ProvedHere` | 9804 | 2 | 0 | MC constraint counting |
| `thm:hecke-verdier-commutation` | `theorem` | `ProvedHere` | 10043 | 0 | 0 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | `ProvedHere` | 10082 | 4 | 0 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | `ProvedHere` | 10156 | 0 | 1 | Theta decomposition bridge |
| `rem:davenport-heilbronn-koszul` | `remark` | `ProvedElsewhere` | 10272 | 0 | 0 | Class-group obstruction and on-line zeros |
| `prop:sewing-spectral-bridge` | `proposition` | `ProvedHere` | 10335 | 3 | 1 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | `ProvedHere` | 10440 | 1 | 0 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | `ProvedHere` | 10487 | 0 | 0 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | `ProvedHere` | 10578 | 2 | 2 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | `ProvedHere` | 10752 | 1 | 0 | Genus-one saddle triviality |
| `cor:first-scattering-pole` | `corollary` | `ProvedHere` | 10949 | 1 | 0 | Regularized nonvanishing at the first scattering pole |
| `thm:scattering-coupling-factorization` | `theorem` | `ProvedHere` | 11050 | 5 | 0 | Scattering coupling factorization |
| `prop:hecke-defect-lattice` | `proposition` | `ProvedHere` | 11315 | 1 | 0 | Vanishing of the Hecke defect under finite Hecke span |
| `thm:packet-connection-flatness` | `theorem` | `ProvedHere` | 11822 | 0 | 0 | Flatness and divisor independence |
| `cor:lattice-packet-diagonal` | `corollary` | `ProvedHere` | 11889 | 1 | 0 | Lattice transparency |
| `prop:gauge-criterion-scattering` | `proposition` | `ProvedHere` | 11956 | 0 | 0 | Gauge criterion for scattering access |
| `rem:arithmetic-comparison-sharpening` | `remark` | `ProvedHere` | 12066 | 0 | 0 | Sharpening of the arithmetic comparison conjecture |
| `prop:miura-packet-splitting` | `proposition` | `ProvedHere` | 12140 | 5 | 0 | — |
| `prop:genus2-non-diagonal` | `proposition` | `ProvedHere` | 12506 | 0 | 0 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | `ProvedHere` | 12550 | 1 | 0 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | `ProvedHere` | 12750 | 0 | 1 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | `ProvedHere` | 12782 | 3 | 2 | B\"ocherer bridge under three-shell reconstruction |
| `rem:genus2-definitive-scope` | `remark` | `ProvedHere` | 12917 | 2 | 0 | Definitive scope of genus-$2$ arithmetic access |
| `rem:leech-weight12-sk` | `remark` | `ProvedHere` | 12973 | 0 | 3 | Leech weight-$12$ cusp line is Saito--Kurokawa |
| `thm:leech-chi12-projection` | `theorem` | `ProvedHere` | 12997 | 2 | 2 | Leech $\chi_{12}$-projection and Waldspurger consequence under three-shell reconstruction |
| `thm:prime-locality-obstructions` | `theorem` | `ProvedHere` | 13330 | 4 | 0 | Precise obstructions to prime-locality |
| `thm:riccati-determinacy` | `theorem` | `ProvedHere` | 13534 | 0 | 0 | Weighted Riccati determinacy |
| `prop:shadow-not-selberg` | `proposition` | `ProvedHere` | 13581 | 2 | 0 | The genus-$1$ amplitude series is not in the Selberg class |
| `thm:fricke-ldp-sub-leading` | `theorem` | `ProvedHere` | 13995 | 1 | 0 | Fricke LDP sub-leading correction at each node |
| `thm:shimura-waldspurger-higher-weights` | `theorem` | `ProvedElsewhere` | 14093 | 1 | 1 | Shimura--Waldspurger constants are period ratios |
| `thm:YD-delta-7-8-9` | `theorem` | `ProvedHere` | 14157 | 2 | 0 | $\delta^{(n)}$ for $n \in \{7, 8, 9, 10, 11, 12\}$ |
| `thm:humbert-heegner-filter-g-geq-3` | `proposition` | `ProvedHere` | 14483 | 1 | 0 | Humbert--Heegner filter beyond genus $2$: proved boundary |
| `thm:mu-32-refinement` | `theorem` | `ProvedHere` | 14654 | 1 | 0 | $\mu_{16}\to\mu_{32}$ gerbe refinement is not a consequence of the Bruinier lcm datum near the quadruple Humbert wall |
| `thm:as-monster-k3-cplus-product-invariant` | `theorem` | `ProvedHere` | 14874 | 3 | 1 | Monster--K$3$ $c_+$-product comparison |
| `cor:as-monster-196884-as-cplus-weighted` | `remark` | `ProvedHere` | 14974 | 1 | 1 | Monster $196884$ is not a $c_+$-weighted K$3$ elliptic-genus coefficient |
| `thm:YD-delta-13-16` | `theorem` | `ProvedHere` | 15313 | 2 | 0 | $\delta^{(n)}$ for $n \in \{13, 14, 15, 16\}$ |
| `thm:n-2-root-unity-vol-I-face` | `theorem` | `ProvedHere` | 15566 | 0 | 0 | $N = 2$ root-of-unity: $324$ is not a PBW dimension |

#### `chapters/connections/bv_brst.tex` (10)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bv-bar-geometric` | `theorem` | `ProvedElsewhere` | 340 | 3 | 1 | Genus-$0$ BV complex and geometric bar complex; {} \cite{CG17} |
| `thm:brst-physical-states` | `theorem` | `ProvedElsewhere` | 561 | 0 | 2 | BRST cohomology on a nilpotent gauge-fixed complex; {} \cite{CG17,Polchinski1998} |
| `thm:log-form-ghost-law` | `theorem` | `ProvedHere` | 597 | 1 | 0 | Coordinate cocycle for collision logarithmic forms |
| `lem:brst-nilpotence` | `lemma` | `ProvedElsewhere` | 697 | 0 | 1 | BRST nilpotence; {} \cite{FGZ86} |
| `rem:ghost-superghost-koszul` | `remark` | `ProvedElsewhere` | 1110 | 0 | 2 | The ghost--superghost Koszul involution |
| `prop:chain-level-three-obstructions` | `proposition` | `ProvedHere` | 1970 | 1 | 1 | Three chain-level obstructions and harmonic factorization |
| `comp:v1-burns-koszul-datum` | `computation` | `ProvedElsewhere` | 2761 | 0 | 0 | Burns space Koszul datum |
| `rem:non-cy-scope` | `remark` | `ProvedElsewhere` | 2879 | 1 | 0 | Scope and status |
| `rem:bvbrst-6d-hcs-quartic` | `remark` | `ProvedElsewhere` | 3049 | 0 | 5 | 6d holomorphic Chern--Simons quartic anomaly polynomial |
| `prop:bvbrst-kreimer-count` | `proposition` | `ProvedElsewhere` | 3846 | 1 | 2 | Kreimer count matches |

#### `chapters/connections/concordance.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:glz-special-case` | `proposition` | `ProvedHere` | 688 | 1 | 0 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | `ProvedHere` | 718 | 0 | 1 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | `ProvedHere` | 1023 | 1 | 0 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | `ProvedHere` | 1047 | 1 | 0 | Polynomial level dependence |
| `prop:vol2-relative-holographic-bridge` | `proposition` | `ProvedElsewhere` | 4953 | 1 | 0 | Relative holographic deformation bridge |
| `prop:vol2-ribbon-thooft-bridge` | `proposition` | `ProvedElsewhere` | 4974 | 3 | 0 | Ribbon/'t~Hooft bridge |
| `comp:spectral-discriminants-standard` | `computation` | `ProvedHere` | 6428 | 0 | 0 | Spectral discriminants of standard families |
| `rem:concord-retraction` | `remark` | `ProvedElsewhere` | 12696 | 0 | 0 | Central charges for $\mathcal T[A_1, \Sigma_{0,24} |

#### `chapters/connections/editorial_constitution.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:master-pbw` | `theorem` | `ProvedElsewhere` | 202 | 4 | 0 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `prop:vassiliev-genus0` | `proposition` | `ProvedHere` | 1829 | 1 | 1 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |

#### `chapters/connections/entanglement_modular_koszul.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:ent-twist-dimension` | `lemma` | `ProvedElsewhere` | 149 | 1 | 1 | Twist operator dimension |
| `thm:ent-scalar-entropy` | `theorem` | `ProvedHere` | 175 | 6 | 0 | Entanglement entropy at the scalar level |
| `rem:ent-negative` | `remark` | `ProvedHere` | 1581 | 2 | 0 | Negative formal coefficient at $c_{\mathrm{eff}} = -166$ |
| `prop:ent-real-root` | `proposition` | `ProvedHere` | 1613 | 3 | 0 | Real-root unitary submodule entanglement |
| `prop:ent-kl-scope` | `proposition` | `ProvedHere` | 1979 | 0 | 2 | Knill--Laflamme scope for finite-stage topological entanglement |

#### `chapters/connections/feynman_connection.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:loop-genus-correspondence` | `theorem` | `ProvedElsewhere` | 138 | 0 | 1 | Loop-genus correspondence; {} \cite{costello-renormalization} |
| `thm:swiss-cheese-chiral-DT-feynman` | `theorem` | `ProvedElsewhere` | 386 | 1 | 2 | Swiss-cheese / chiral Deligne--Tamarkin |

#### `chapters/connections/feynman_diagrams.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | `ProvedHere` | 275 | 1 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `thm:kontsevich-formality-feynman` | `theorem` | `ProvedElsewhere` | 372 | 1 | 1 | Kontsevich formality |
| `prop:compactified-ternary-two-channel` | `proposition` | `ProvedHere` | 524 | 0 | 0 | Two-channel reduction after compactifying the ternary packet |
| `prop:m04-standard-log-basis` | `proposition` | `ProvedHere` | 611 | 0 | 0 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `thm:loop-genus-formula` | `theorem` | `ProvedElsewhere` | 783 | 0 | 1 | Graph loop number and ribbon genus; {} \cite{costello-renormalization} |
| `thm:mk-tree-level` | `theorem` | `ProvedElsewhere` | 1044 | 1 | 0 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure-vol1` | `theorem` | `ProvedHere` | 1072 | 5 | 1 | Formal all-genus stable-graph expansion |
| `prop:feyn-nekrasov-self-dual` | `proposition` | `ProvedElsewhere` | 1846 | 0 | 0 | Self-dual AGT block on \texorpdfstring{$\Sigma_{0,24}$}{Sigma 0,24} |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (35)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | `ProvedHere` | 127 | 6 | 0 | Protected dual transform and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | `ProvedHere` | 243 | 4 | 0 | Protected transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | `ProvedHere` | 303 | 2 | 0 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | `ProvedHere` | 344 | 4 | 0 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | `ProvedHere` | 405 | 2 | 0 | Scalar fixed-point rigidity on a full scalar package and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | `ProvedHere` | 528 | 2 | 0 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | `ProvedHere` | 647 | 2 | 0 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | `ProvedHere` | 771 | 1 | 0 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | `ProvedHere` | 842 | 6 | 0 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | `ProvedHere` | 980 | 5 | 0 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | `ProvedHere` | 1067 | 1 | 0 | The first nonlinear holographic anomaly |
| `prop:pva-degree-constraint` | `proposition` | `ProvedElsewhere` | 2390 | 0 | 1 | PVA degree constraint and the inevitability of $2{+}1$ dimensions |
| `cor:shadow-connection-heisenberg` | `corollary` | `ProvedElsewhere` | 2820 | 1 | 0 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | `ProvedHere` | 2841 | 2 | 0 | Shadow connection for Virasoro and BPZ on the degenerate-representation surface |
| `comp:holographic-ss-vir` | `computation` | `ProvedHere` | 3019 | 1 | 0 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | `ProvedHere` | 3063 | 1 | 0 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | `ProvedHere` | 3087 | 1 | 0 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | `ProvedHere` | 3172 | 1 | 0 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | `ProvedHere` | 3202 | 0 | 0 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | `ProvedHere` | 3244 | 1 | 0 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | `ProvedHere` | 3335 | 0 | 0 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | `ProvedHere` | 3392 | 0 | 0 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | `ProvedHere` | 3488 | 1 | 0 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | `ProvedHere` | 3547 | 0 | 0 | Holographic datum for $\mathcal W_3$ |
| `cor:critical-dimensions` | `corollary` | `ProvedHere` | 3792 | 0 | 0 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | `ProvedHere` | 3903 | 1 | 0 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | `ProvedHere` | 3932 | 1 | 0 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | `ProvedHere` | 3973 | 0 | 0 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | `ProvedHere` | 4003 | 0 | 0 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | `ProvedHere` | 4122 | 1 | 0 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | `ProvedHere` | 4263 | 0 | 0 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | `ProvedHere` | 4446 | 0 | 0 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | `ProvedHere` | 4585 | 0 | 0 | Lifts as relative MC elements |
| `cor:holographic-deformation-cohomology` | `corollary` | `ProvedElsewhere` | 4622 | 0 | 0 | — |
| `comp:burns-space-holographic-datum` | `computation` | `ProvedHere` | 6048 | 1 | 2 | Burns space holographic modular Koszul datum |

#### `chapters/connections/genus1_seven_faces.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:g1sf-b-cycle-monodromy` | `theorem` | `ProvedHere` | 1441 | 2 | 0 | $B$-cycle monodromy of the collision residue |

#### `chapters/connections/genus_complete.tex` (25)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:elliptic-bar` | `theorem` | `ProvedElsewhere` | 115 | 1 | 1 | Elliptic bar complex; {} \cite{FBZ04} |
| `thm:master-tower` | `theorem` | `ProvedHere` | 357 | 1 | 0 | Master tower of boundary residues |
| `thm:chain-modular-functor` | `theorem` | `ProvedHere` | 471 | 6 | 1 | Chain-level boundary-residue modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | `ProvedHere` | 565 | 1 | 0 | Verdier-dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | `ProvedHere` | 890 | 3 | 0 | Bar complex defines tautological moduli integrals |
| `thm:poincare-extended` | `theorem` | `ProvedElsewhere` | 998 | 2 | 2 | Poincaré--Verdier duality for genus pieces; {} \cite{BD04,FG12} |
| `prop:bulk-from-boundary` | `proposition` | `ProvedElsewhere` | 1081 | 0 | 3 | Algebraic closed sector from the boundary; {} \cite{BD04,FG12,CG17} |
| `prop:sewing-universal-property` | `proposition` | `ProvedHere` | 1719 | 0 | 0 | Universal property of the sewing envelope |
| `prop:hs-trace-class` | `proposition` | `ProvedHere` | 1768 | 3 | 0 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | `ProvedHere` | 1799 | 0 | 0 | General HS-sewing criterion |
| `cor:hs-sewing-standard-landscape` | `corollary` | `ProvedElsewhere` | 1847 | 0 | 0 | Standard landscape |
| `cor:hs-implies-gram` | `corollary` | `ProvedHere` | 1886 | 3 | 0 | Diagonal positive sewing implies Gram positivity |
| `thm:heisenberg-one-particle-sewing` | `theorem` | `ProvedHere` | 1909 | 0 | 0 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | `ProvedHere` | 2000 | 1 | 0 | Finite-window conilpotency and completed pro-conilpotency |
| `thm:dirichlet-weight-formula` | `theorem` | `ProvedHere` | 2306 | 0 | 0 | — |
| `cor:virasoro-mode-removal` | `corollary` | `ProvedHere` | 2363 | 2 | 0 | — |
| `thm:euler-koszul-criterion` | `theorem` | `ProvedHere` | 2422 | 2 | 0 | — |
| `comp:euler-koszul-defect-table` | `computation` | `ProvedHere` | 2459 | 2 | 0 | Euler--Koszul defect table for the standard landscape |
| `prop:zeta-zeros-defect-derivative` | `proposition` | `ProvedHere` | 2551 | 0 | 0 | — |
| `thm:li-closed-form` | `theorem` | `ProvedHere` | 2591 | 0 | 0 | — |
| `thm:li-asymptotics` | `theorem` | `ProvedHere` | 2625 | 2 | 0 | First Li coefficient and finite sign computation |
| `thm:surface-moment-positivity` | `theorem` | `ProvedHere` | 2765 | 0 | 0 | Gram positivity |
| `cor:virasoro-gram-ratio` | `corollary` | `ProvedHere` | 2788 | 0 | 0 | Virasoro sewing deficit |
| `thm:sewing-rkhs` | `theorem` | `ProvedHere` | 2830 | 2 | 0 | Sewing RKHS |
| `prop:benjamin-chang-bridge` | `proposition` | `ProvedHere` | 2943 | 0 | 1 | — |

#### `chapters/connections/grand_unification_platonic.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:grand-unification-platonic` | `theorem` | `ProvedHere` | 99 | 3 | 2 | Grand Unification, chiral bar--cobar |
| `cor:gu-theorem-a-platonic` | `corollary` | `ProvedHere` | 208 | 3 | 0 | Theorem~A is the adjunction itself |
| `cor:gu-theorem-b-platonic` | `corollary` | `ProvedHere` | 225 | 2 | 0 | Theorem~B is Positselski localisation |
| `cor:gu-theorem-c-platonic` | `corollary` | `ProvedHere` | 240 | 4 | 0 | Theorem~C is the scalar invariant of the double |
| `cor:gu-theorem-d-platonic` | `corollary` | `ProvedHere` | 264 | 4 | 0 | Theorem~D is obstruction-tower universality |
| `cor:gu-L1-platonic` | `corollary` | `ProvedHere` | 304 | 2 | 0 | L1; chain-level ensemble via genus-$g$ trace |
| `cor:gu-L3-platonic` | `corollary` | `ProvedHere` | 369 | 1 | 3 | L3; $(\infty,1)$-categorical adjunction |
| `prop:L1-trace-identity-platonic` | `proposition` | `ProvedHere` | 470 | 3 | 1 | L1 trace identity |
| `thm:pr-alpha-X-local-global` | `theorem` | `ProvedHere` | 881 | 1 | 7 | Local-global gluing of $\mathrm{pr}_{\alpha_X}$ |

#### `chapters/connections/holographic_codes_koszul.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:hc-projection-not-kl` | `proposition` | `ProvedHere` | 359 | 0 | 0 | Symplectic projection is not Knill--Laflamme recovery |
| `prop:hc-theorem-h-scope` | `proposition` | `ProvedHere` | 536 | 1 | 0 | Theorem H is not a physical bulk-vanishing theorem |

#### `chapters/connections/holographic_datum_master.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:hdm-face-6` | `theorem` | `ProvedHere` | 996 | 2 | 1 | Face~6: Sklyanin bracket; \ (identification with classical limit of collision residue); \ (Sklyanin bracket: Semenov-Tian-Shansky 1983) |
| `prop:hdm-binary-residue-not-bulk` | `proposition` | `ProvedHere` | 2853 | 0 | 0 | Counter-scope: the binary residue does not determine the closed-sector algebra |
| `prop:hdm-finality-central-kernel` | `proposition` | `ProvedHere` | 3271 | 0 | 0 | Counter-scope: projections alone do not imply finality |

#### `chapters/connections/master_concordance.tex` (19)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:master-oca-bmodel` | `proposition` | `ProvedHere` | 254 | 1 | 3 | OCA discharge for the 3d B-model on $T^*\mathbb{A}^n$ via HKR; $$ |
| `lem:master-oca-sheafy-hkr-extension` | `lemma` | `ProvedHere` | 337 | 1 | 4 | OCA extension: smooth affine and smooth projective via sheafy HKR; $$ on smooth affine, $$ on smooth projective on full Costello--Gwilliam BV identification |
| `cor:master-oca-rozansky-witten-k3` | `corollary` | `ProvedHere` | 398 | 1 | 0 | OCA for Rozansky--Witten on $T^*K3$; $$ on the HKR / Hodge identification, $$ on the Rozansky--Witten bulk identification |
| `cor:master-oca-k3-hilbert-hierarchy` | `corollary` | `ProvedHere` | 453 | 2 | 1 | OCA hierarchy across K3 Hilbert schemes via Mukai--C{\u a}ld{\u a}raru + Göttsche; $$ on the total-dim count, $$ on the hyperk{\"a}hler B-model bulk identification |
| `cor:master-oca-bmodel-elliptic` | `corollary` | `ProvedHere` | 514 | 1 | 0 | OCA for 3d B-model on $T^*E$ via sheafy HKR; $$ on the HKR / Hodge identification, $$ on the Rozansky--Witten bulk identification |
| `cor:master-oca-quintic` | `corollary` | `ProvedHere` | 586 | 1 | 0 | OCA for the quintic CY 3-fold; $$ on HKR/Hodge, $$ on B-model bulk identification |
| `cor:master-oca-bmodel-schouten` | `corollary` | `ProvedHere` | 650 | 1 | 4 | Schouten--Nijenhuis bracket as closed-colour $\mathsf{SC}^{\mathrm{ch,top}}$-brace; $$ |
| `lem:master-scalar-non-faithfulness` | `lemma` | `ProvedHere` | 700 | 0 | 0 | Scalar non-faithfulness; $$ |
| `thm:master-scalar-nonfaithful-witness-c16` | `theorem` | `ProvedHere` | 727 | 2 | 2 | Heterotic non-faithfulness witness at $c = 16$; $$ |
| `lem:master-delta-cartan-window` | `lemma` | `ProvedHere` | 935 | 1 | 2 | $\delta$ at the abelian Cartan window: trivial Drinfeld doubling with Mukai pairing; $$ on the classical Drinfeld-double formalism |
| `lem:master-epsilon-cartan-window` | `lemma` | `ProvedHere` | 1004 | 1 | 2 | $\varepsilon$ at the abelian Cartan window: lattice Heisenberg current algebra on $E$; $$ |
| `lem:master-tau-cartan-window` | `lemma` | `ProvedHere` | 1054 | 2 | 3 | $\tau$ at the abelian Cartan window: lattice Heisenberg trace as leading-order $\Delta_5^{-2}$ contribution; $$ on the lattice Heisenberg part |
| `thm:master-vir-26-bc-brst-topologisation` | `theorem` | `ProvedHere` | 1195 | 1 | 2 | Raw chain-level T1--T5 discharge for $\mathrm{Vir}_{26}$ via bosonic-string BRST; $$ |
| `thm:master-generalized-matter-ghost-brst` | `theorem` | `ProvedHere` | 1305 | 1 | 1 | Generalised matter-ghost BRST T1--T5 discharge at arbitrary matter central charge $c \geq -1$; $$ |
| `cor:master-per-spin-antighost-linear-Winf` | `corollary` | `ProvedHere` | 1432 | 1 | 0 | Per-spin antighost commutativity for linear $\cW_\infty[0 |
| `cor:master-screening-brst-c-lt-minus-1` | `corollary` | `ProvedHere` | 1500 | 2 | 1 | T1--T5 in the weight-completed ambient for matter at $c_{\mathfrak A} < -1$ via Felder screening BRST; $$ on the weight-completed Fock module |
| `thm:master-n2-topological-twist-topologisation` | `theorem` | `ProvedHere` | 1547 | 2 | 1 | Raw chain-level T1--T5 discharge for N=2 superconformal VOAs via topological twist; $$ |
| `cor:master-n2-twist-kazama-suzuki` | `corollary` | `ProvedHere` | 1647 | 1 | 0 | Kazama--Suzuki coset T1--T5 discharge via N=2 worldsheet topological twist; $$ |
| `cor:master-n2-twist-cy-sigma` | `corollary` | `ProvedHere` | 1697 | 1 | 1 | Calabi--Yau sigma model T1--T5 discharge via N=2 worldsheet topological twist; $$ |

#### `chapters/connections/master_reconstruction.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:mr-morita` | `theorem` | `ProvedHere` | 215 | 0 | 2 | $F_0$-reconstruction: Morita |
| `cor:mr-B` | `corollary` | `ProvedHere` | 734 | 0 | 0 | Theorem~B as bar--cobar inversion at the centre level; \ on Koszul locus |
| `cor:mr-C` | `corollary` | `ProvedHere` | 748 | 1 | 0 | Theorem~C as scalar shadow at the family-stratum ceiling; \ on Koszul locus |
| `cor:mr-D` | `corollary` | `ProvedHere` | 764 | 0 | 0 | Theorem~D as obstruction tower on $\Mbar_{g,n}$ |
| `cor:mr-H` | `corollary` | `ProvedHere` | 780 | 0 | 0 | Theorem~H as $F_2$-concentration |

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
| `cor:platonic-reduction-W3-frontier` | `corollary` | `ProvedHere` | 813 | 1 | 0 | Finite semistrict reduction of the $W_3$ frontier |

#### `chapters/connections/subregular_hook_frontier.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:pbw-slodowy-collapse` | `theorem` | `ProvedHere` | 81 | 0 | 0 | PBW--Slodowy collapse |
| `cor:principal-w-completed-koszul` | `corollary` | `ProvedHere` | 148 | 1 | 0 | Principal affine \texorpdfstring{$W$}{W}-algebras are completed Koszul |
| `prop:transport-propagation` | `proposition` | `ProvedHere` | 287 | 0 | 0 | Transport propagation lemma |
| `prop:hook-ghost-constant` | `proposition` | `ProvedHere` | 359 | 0 | 0 | Hook ghost constant |
| `thm:canonical-degree-detection` | `theorem` | `ProvedHere` | 502 | 0 | 0 | Generator-degree detection of canonical degree |
| `thm:full-raw-coefficient-packet` | `theorem` | `ProvedHere` | 670 | 2 | 0 | Exact Bell recursion for the full singular packet |
| `thm:miura-product-formula` | `theorem` | `ProvedHere` | 828 | 0 | 0 | Subregular Miura product formula |
| `thm:subregular-appell-formula` | `theorem` | `ProvedHere` | 865 | 0 | 0 | Subregular Appell formula |
| `thm:bp-strict` | `theorem` | `ProvedHere` | 937 | 3 | 0 | Bershadsky--Polyakov is strict in canonical normal form |
| `thm:w4-cubic` | `theorem` | `ProvedHere` | 1185 | 2 | 0 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} has canonical degree $3$ |
| `thm:unbounded-canonical-degree` | `theorem` | `ProvedHere` | 1330 | 4 | 0 | Unbounded canonical degree in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | `ProvedHere` | 1394 | 0 | 0 | Triangular primary-renormalization theorem |
| `prop:nilpotent-transport-typeA` | `proposition` | `ProvedHere` | 1619 | 0 | 5 | Nilpotent transport for type $A$ |

#### `chapters/connections/thqg_entanglement_theory.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:thqg-ent-algebraic-sector` | `remark` | `ProvedHere` | 16 | 2 | 3 | Algebraic-sector identification for the entanglement register |

#### `chapters/connections/thqg_introduction_supplement.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:supp-algebraic-physical-bulk-separation` | `proposition` | `ProvedHere` | 303 | 0 | 0 | Algebraic datum versus physical bulk |

#### `chapters/connections/thqg_introduction_supplement_body.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:thqg-intro-four-layer-separation` | `proposition` | `ProvedHere` | 307 | 1 | 0 | Four-layer separation |
| `thm:thqg-intro-quartic-linfty` | `theorem` | `ProvedElsewhere` | 418 | 1 | 0 | Quartic obstruction $=$ $L_\infty$ bracket |
| `prop:thqg-intro-flatness` | `proposition` | `ProvedElsewhere` | 537 | 0 | 0 | Flatness of the shadow connection |
| `thm:thqg-intro-hs-general` | `theorem` | `ProvedElsewhere` | 1610 | 1 | 0 | General HS-sewing criterion |
| `thm:thqg-intro-heisenberg-sewing` | `theorem` | `ProvedElsewhere` | 1631 | 1 | 0 | Heisenberg sewing |
| `rem:thqg-intro-algebraic-sector-vs-dynamical-metric` | `remark` | `ProvedHere` | 2090 | 1 | 3 | Algebraic sector versus dynamical-metric path integral |

#### `chapters/connections/thqg_open_closed_realization.tex` (12)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:thqg-oc-algebraic-sector` | `remark` | `ProvedHere` | 24 | 2 | 3 | Algebraic sector identification |
| `prop:bd-algebraic-bridge` | `proposition` | `ProvedHere` | 166 | 3 | 1 | Bridge: BD chiral operad $\leftrightarrow$ algebraic $\mathcal{E}\!\mathit{nd}^{\mathrm{ch}}$ |
| `thm:thqg-brace-dg-algebra` | `theorem` | `ProvedHere` | 307 | 10 | 0 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | `ProvedHere` | 570 | 4 | 0 | Universal open/closed pair (chiral Swiss-cheese theorem) |
| `prop:thqg-universal-action-not-reconstruction` | `proposition` | `ProvedHere` | 655 | 1 | 0 | Typed physical-bulk comparison |
| `prop:mixed-sector-bulk-boundary` | `proposition` | `ProvedHere` | 731 | 2 | 0 | Mixed sector encodes bulk-to-boundary module structure |
| `prop:thqg-swiss-cheese-no-yangian-coproduct` | `proposition` | `ProvedHere` | 768 | 1 | 0 | Yangian coproducts require line-category data |
| `thm:thqg-local-global-bridge` | `theorem` | `ProvedHere` | 835 | 7 | 0 | Local-global bridge |
| `cor:thqg-intrinsic-bulk` | `corollary` | `ProvedHere` | 929 | 2 | 0 | The intrinsic categorical center |
| `thm:thqg-hochschild-register-separation` | `theorem` | `ProvedHere` | 969 | 8 | 0 | Separation of Hochschild, trace, THH, BV, and Koszul duality |
| `thm:thqg-annulus-trace` | `theorem` | `ProvedHere` | 1106 | 11 | 5 | Annulus trace theorem |
| `prop:thqg-occ-CD-ANm1-24` | `proposition` | `ProvedHere` | 2435 | 0 | 0 | Chacaltana--Distler central charges for $\mathcal T\lbrack A_{N-1}, \Sigma_{0,24}\rbrack$ |

#### `chapters/connections/vertical_equivalence_level_0.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:vel0-quartic-anomaly` | `theorem` | `ProvedHere` | 89 | 4 | 3 | Quartic Pontryagin-type form for the 6d $\hCS$ one-loop obstruction |
| `lem:vel0-admissible-g` | `lemma` | `ProvedHere` | 182 | 2 | 0 | Admissible gauge dg-Lie at level $0$ |

### Appendices (213)

#### `appendices/_sl2_yangian_insert.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:ordered-bar-sl2` | `computation` | `ProvedHere` | 86 | 0 | 0 | Degree-$2$ ordered bar complex of $\widehat{\mathfrak{sl}}_2$ |
| `prop:ybe-from-d-squared` | `proposition` | `ProvedHere` | 164 | 1 | 0 | $d^2=0$ is the classical Yang--Baxter equation |
| `thm:yang-r-matrix` | `theorem` | `ProvedHere` | 227 | 0 | 0 | Yang $R$-matrix from the ordered bar complex |
| `thm:rtt-sl2` | `theorem` | `ProvedHere` | 307 | 5 | 1 | RTT presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:pbw-sl2` | `theorem` | `ProvedHere` | 429 | 1 | 1 | PBW basis of $Y_\hbar(\mathfrak{sl}_2)$ |
| `cor:hilbert-sl2` | `corollary` | `ProvedHere` | 475 | 1 | 0 | Hilbert series |
| `prop:eval-tensor-sl2` | `proposition` | `ProvedHere` | 521 | 1 | 0 | Tensor products and Yang--Baxter |

#### `appendices/arnold_relations.tex` (10)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:arnold-relations-appendix` | `theorem` | `ProvedElsewhere` | 19 | 2 | 3 | Arnold relations \cite{Arnold69} |
| `prop:arnold-genus-split-appendix` | `proposition` | `ProvedHere` | 64 | 1 | 3 | Configuration-space relation packages |
| `prop:operadic-equivalence-arnold` | `proposition` | `ProvedHere` | 138 | 2 | 0 | Affine screen residue cancellation |
| `thm:bar-d-squared-arnold` | `theorem` | `ProvedHere` | 173 | 3 | 0 | Affine bar square |
| `lem:OS-cohomology-arnold` | `lemma` | `ProvedElsewhere` | 235 | 1 | 1 | OS computes cohomology \cite{OS80} |
| `cor:bar-d-squared-zero-arnold` | `corollary` | `ProvedHere` | 261 | 1 | 0 | Affine simple-pole bar differential |
| `thm:arnold-iff-nilpotent` | `theorem` | `ProvedHere` | 288 | 2 | 0 | Affine Arnold and triple-residue nilpotency |
| `thm:arnold-general-n` | `theorem` | `ProvedElsewhere` | 378 | 0 | 2 | Arnold relations for \texorpdfstring{$n$}{n} affine points \cite{Arnold69, OS80} |
| `thm:config-boundary-relations` | `theorem` | `ProvedHere` | 419 | 0 | 1 | Configuration-space boundary relations |
| `cor:dres-squared-global` | `corollary` | `ProvedHere` | 451 | 4 | 0 | \texorpdfstring{$d_{\mathrm{res}}^2$}{d-res squared} and global corrections |

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

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:virasoro-pade` | `proposition` | `ProvedHere` | 990 | 1 | 0 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dual_methodology.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:abstract-bar-cobar` | `theorem` | `ProvedElsewhere` | 25 | 0 | 2 | Abstract bar-cobar equivalence \cite{FG12, HA} |
| `thm:abstract-rh` | `theorem` | `ProvedElsewhere` | 96 | 0 | 1 | Abstract Riemann--Hilbert \cite{KS90} |
| `thm:geometric-infty-operads` | `theorem` | `ProvedHere` | 162 | 0 | 0 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |
| `thm:glz-quadratic-duality-scope` | `theorem` | `ProvedElsewhere` | 236 | 0 | 1 | Gui--Li--Zeng quadratic duality: scope |

#### `appendices/hochschild_conventions.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:hochschild-crosswalk` | `proposition` | `ProvedHere` | 26 | 7 | 0 | Three Hochschild theories: type signatures, scope, and comparison rules |

#### `appendices/homotopy_transfer.tex` (12)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:htt` | `theorem` | `ProvedElsewhere` | 69 | 0 | 2 | Homotopy transfer theorem \cite{LV12, Kadeishvili80} |
| `lem:sdr-existence` | `lemma` | `ProvedHere` | 146 | 0 | 0 | Existence of SDR |
| `thm:tree-formula` | `theorem` | `ProvedElsewhere` | 209 | 0 | 1 | Tree formula for transferred operations \cite{LV12} |
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
| `thm:curvature-central-appendix` | `theorem` | `ProvedHere` | 657 | 1 | 1 | Central curvature and internal strictness |

#### `appendices/nonlinear_modular_shadows.tex` (53)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:nms-mc-principle` | `theorem` | `ProvedHere` | 184 | 2 | 0 | Algebra structure $=$ Maurer--Cartan element |
| `thm:nms-shadow-tower-mc` | `theorem` | `ProvedHere` | 401 | 1 | 0 | Shadow obstruction tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | `ProvedHere` | 441 | 1 | 0 | Standard-family evaluations of the universal class |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | `ProvedHere` | 546 | 0 | 0 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | `ProvedHere` | 600 | 0 | 0 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | `ProvedHere` | 646 | 0 | 0 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | `ProvedHere` | 655 | 0 | 0 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | `ProvedHere` | 676 | 1 | 0 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | `ProvedHere` | 691 | 0 | 0 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | `ProvedHere` | 790 | 2 | 0 | Quartic shadow master equations |
| `prop:nms-quartic-closure-envelope` | `proposition` | `ProvedHere` | 942 | 0 | 0 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | `ProvedHere` | 972 | 0 | 0 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | `ProvedHere` | 992 | 1 | 0 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | `ProvedHere` | 1067 | 0 | 0 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | `ProvedHere` | 1091 | 0 | 0 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | `ProvedHere` | 1184 | 2 | 0 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | `ProvedHere` | 1229 | 1 | 0 | Weight-changing projection of the quartic contact |
| `cor:nms-betagamma-boundary-law` | `corollary` | `ProvedHere` | 1254 | 0 | 0 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | `ProvedHere` | 1271 | 3 | 0 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | `ProvedHere` | 1300 | 0 | 0 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | `ProvedHere` | 1349 | 0 | 0 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | `ProvedHere` | 1387 | 1 | 0 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | `ProvedHere` | 1415 | 0 | 0 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | `ProvedHere` | 1487 | 1 | 0 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | `ProvedHere` | 1547 | 1 | 0 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `prop:nms-w3-visible-resonance-factor` | `proposition` | `ProvedHere` | 1586 | 1 | 0 | Visible quartic resonance factor for \texorpdfstring{$\mathcal W_3$}{W3} |
| `thm:nms-w3-full-quartic-gram` | `theorem` | `ProvedHere` | 1628 | 1 | 0 | Full $\mathcal W_3$ quartic Gram determinant |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | `ProvedHere` | 1701 | 1 | 0 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | `ProvedHere` | 1719 | 0 | 0 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | `ProvedHere` | 1735 | 2 | 0 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | `ProvedHere` | 1844 | 1 | 0 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | `ProvedHere` | 1896 | 0 | 0 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | `ProvedHere` | 1920 | 2 | 0 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behavior` | `corollary` | `ProvedHere` | 2008 | 3 | 0 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | `ProvedHere` | 2081 | 0 | 0 | Functoriality and duality through quartic order |
| `thm:nms-all-degree-master-equation` | `theorem` | `ProvedHere` | 2214 | 2 | 0 | All-degree master equation |
| `cor:nms-quintic-master-equation` | `corollary` | `ProvedHere` | 2250 | 1 | 0 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | `ProvedHere` | 2272 | 5 | 0 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | `ProvedHere` | 2296 | 0 | 0 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | `ProvedHere` | 2315 | 3 | 0 | Finite termination for primitive archetypes |
| `prop:nms-genus-loop-properties` | `proposition` | `ProvedHere` | 2430 | 1 | 0 | Basic properties of the genus loop operator |
| `thm:nms-genus-loop-model-families` | `theorem` | `ProvedHere` | 2498 | 0 | 0 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | `ProvedHere` | 2579 | 0 | 0 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-bipartite-complementarity` | `theorem` | `ProvedHere` | 3014 | 1 | 0 | Bipartite complementarity principle |
| `thm:nms-bipartite-vanishing` | `theorem` | `ProvedHere` | 3126 | 1 | 0 | Bipartite vanishing theorem |
| `thm:reduced-weight-finiteness` | `theorem` | `ProvedHere` | 3475 | 1 | 0 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | `ProvedHere` | 3563 | 1 | 0 | Window locality |
| `cor:exact-stabilization` | `corollary` | `ProvedHere` | 3585 | 1 | 0 | Exact stabilization |
| `lem:nms-euler-inversion` | `lemma` | `ProvedHere` | 3761 | 1 | 0 | Euler inversion |
| `prop:kac-shadow-singularity` | `proposition` | `ProvedHere` | 3848 | 1 | 0 | Kac-shadow singularity principle |
| `thm:shadow-subalgebra-autonomy` | `theorem` | `ProvedHere` | 4167 | 4 | 0 | Shadow subalgebra autonomy |
| `cor:w-line-alternating-vanishing` | `corollary` | `ProvedHere` | 4243 | 1 | 0 | $W$-line alternating vanishing |
| `thm:nms-mc-moduli-curve-structure` | `theorem` | `ProvedHere` | 4445 | 1 | 0 | MC moduli curve structure |

#### `appendices/ordered_associative_chiral_kd.tex` (83)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:bicom-e` | `lemma` | `ProvedHere` | 223 | 0 | 0 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | `ProvedHere` | 313 | 0 | 0 | Ordered chiral shuffle theorem |
| `prop:r-matrix-descent-vol1` | `proposition` | `ProvedHere` | 592 | 4 | 0 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | `ProvedHere` | 736 | 5 | 0 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | `ProvedHere` | 887 | 0 | 0 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | `ProvedHere` | 929 | 1 | 0 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | `ProvedHere` | 961 | 0 | 0 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | `ProvedHere` | 972 | 1 | 0 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | `ProvedHere` | 1037 | 0 | 0 | — |
| `prop:one-defect` | `proposition` | `ProvedHere` | 1064 | 0 | 0 | — |
| `thm:tangent=K` | `theorem` | `ProvedHere` | 1086 | 0 | 0 | Tangent identification |
| `cor:infdual` | `corollary` | `ProvedHere` | 1123 | 2 | 0 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | `ProvedHere` | 1146 | 2 | 0 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | `ProvedHere` | 1198 | 3 | 0 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | `ProvedHere` | 1231 | 1 | 0 | Diagonal correspondence |
| `cor:unit` | `corollary` | `ProvedHere` | 1279 | 2 | 0 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | `ProvedHere` | 1297 | 1 | 0 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | `ProvedHere` | 1326 | 2 | 0 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | `ProvedHere` | 1358 | 1 | 0 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | `ProvedHere` | 1384 | 1 | 0 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | `ProvedHere` | 1404 | 1 | 0 | Cap action |
| `thm:pair-of-pants` | `theorem` | `ProvedHere` | 1459 | 1 | 0 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | `ProvedHere` | 1497 | 4 | 0 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | `ProvedHere` | 1551 | 1 | 0 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | `ProvedHere` | 1600 | 2 | 0 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | `ProvedHere` | 1624 | 12 | 0 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | `ProvedHere` | 1768 | 0 | 0 | Topology of ordered real configurations |
| `lem:deconcatenation-coderivation` | `lemma` | `ProvedHere` | 2092 | 0 | 0 | Coderivation compatibility |
| `thm:heisenberg-ordered-bar` | `theorem` | `ProvedHere` | 2270 | 1 | 0 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | `ProvedHere` | 2384 | 0 | 0 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | `ProvedHere` | 2449 | 0 | 0 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | `ProvedHere` | 2510 | 0 | 0 | Formality: class~G, shadow depth~$2$ |
| `thm:bg-ordered-bar` | `theorem` | `ProvedHere` | 2628 | 0 | 0 | Free-field ordered bar complexes |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | `ProvedHere` | 2808 | 1 | 0 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | `ProvedHere` | 2874 | 1 | 0 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | `ProvedHere` | 2934 | 2 | 0 | Ordered Koszul dual of lattice algebras |
| `thm:drinfeld-yangian-sl2` | `theorem` | `ProvedHere` | 3036 | 6 | 0 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | `ProvedHere` | 3126 | 0 | 0 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | `ProvedHere` | 3162 | 3 | 0 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | `ProvedHere` | 3214 | 3 | 0 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | `ProvedHere` | 3255 | 7 | 0 | Classical limit |
| `prop:vir-collision-residue` | `proposition` | `ProvedHere` | 3344 | 2 | 0 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | `ProvedHere` | 3374 | 1 | 0 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | `ProvedHere` | 3401 | 0 | 0 | Gravitational Yangian collapse |
| `prop:grav-yangian-curvature` | `proposition` | `ProvedHere` | 3517 | 0 | 0 | Gravitational Yangian curvature |
| `thm:central-extension-invisible` | `theorem` | `ProvedHere` | 3649 | 0 | 0 | Central extension is invisible to the open-colour double bar |
| `thm:two-colour-double-kd` | `theorem` | `ProvedHere` | 3715 | 1 | 0 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | `ProvedHere` | 3749 | 2 | 0 | Non-redundancy of the two colours |
| `thm:root-space-one-dim-v1` | `theorem` | `ProvedHere` | 4177 | 0 | 0 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | `ProvedHere` | 4226 | 1 | 0 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | `ProvedHere` | 4292 | 0 | 0 | Dynkin coefficient via the beta integral |
| `thm:sl3-triangle-coefficient` | `theorem` | `ProvedHere` | 4611 | 0 | 0 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | `ProvedHere` | 4695 | 0 | 0 | Serre relations from root-space vanishing |
| `thm:sl4-quadrilateral` | `theorem` | `ProvedHere` | 4891 | 1 | 0 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:b-cycle-quantum-group` | `theorem` | `ProvedHere` | 5291 | 1 | 0 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno-appendix` | `theorem` | `ProvedElsewhere` | 5418 | 2 | 0 | Drinfeld--Kohno; {} for monodromy, {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | `ProvedHere` | 5499 | 0 | 0 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | `ProvedHere` | 5570 | 0 | 0 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | `ProvedHere` | 5611 | 1 | 0 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | `ProvedHere` | 5774 | 0 | 0 | Ordered pole-depth spectrum |
| `thm:ordered-AOS` | `theorem` | `ProvedHere` | 5833 | 2 | 0 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | `ProvedHere` | 5912 | 1 | 0 | Averaging and surplus |
| `thm:FG-shadow-vol2` | `theorem` | `ProvedElsewhere` | 6203 | 0 | 0 | Comm\-utator-shadow theorem |
| `thm:ordered-associative-modular-mc` | `theorem` | `ProvedElsewhere` | 6286 | 0 | 0 | Associative modular Maurer--Cartan class |
| `thm:ordered-associative-ds-principal` | `theorem` | `ProvedElsewhere` | 6326 | 0 | 0 | Reduction commutes with associative chiral duality \textup{(}principal case\textup{)} |
| `prop:r-matrix-stable-envelope` | `proposition` | `ProvedHere` | 6870 | 0 | 0 | $R$-matrix comparison |
| `comp:sl2-eval` | `computation` | `ProvedHere` | 7017 | 0 | 0 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | `ProvedHere` | 7061 | 0 | 0 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | `ProvedHere` | 7109 | 1 | 0 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | `ProvedHere` | 7151 | 0 | 0 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | `ProvedHere` | 7186 | 0 | 0 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `thm:drinfeld-classification` | `theorem` | `ProvedElsewhere` | 7215 | 0 | 0 | Drinfeld classification |
| `prop:eval-drinfeld` | `proposition` | `ProvedHere` | 7238 | 0 | 0 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | `ProvedHere` | 7305 | 2 | 0 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | `ProvedHere` | 7366 | 0 | 0 | Braiding from the $R$-matrix |
| `thm:grothendieck-yangian` | `theorem` | `ProvedElsewhere` | 7411 | 0 | 0 | Grothendieck ring of Yangian modules |
| `thm:annular-bar-differential` | `theorem` | `ProvedHere` | 7522 | 1 | 0 | Annular bar differential |
| `thm:annular-HH` | `theorem` | `ProvedHere` | 7615 | 3 | 0 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | `ProvedHere` | 7715 | 1 | 0 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:elliptic-spectral-dichotomy` | `theorem` | `ProvedHere` | 7874 | 2 | 0 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `prop:r-matrix-eigenvalue` | `proposition` | `ProvedHere` | 8077 | 0 | 0 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | `ProvedHere` | 8093 | 1 | 0 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | `ProvedHere` | 8249 | 1 | 0 | $\mathsf{E}_1$ ordered bar landscape |

#### `appendices/q_convention_bridge_appendix.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:q-convention-bridge-main` | `theorem` | `ProvedHere` | 73 | 0 | 0 | Q-convention bridge |
| `thm:q-bridge-cocycle` | `theorem` | `ProvedHere` | 275 | 0 | 0 | Q-bridge as Z/2-cover cocycle |

#### `appendices/signs_and_shifts.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:graded-jacobi` | `proposition` | `ProvedHere` | 40 | 0 | 0 | Graded Jacobi identity |
| `lem:composition-signs` | `lemma` | `ProvedElsewhere` | 91 | 0 | 1 | Sign rule for compositions \cite{LV12} |
| `prop:duality-grading` | `proposition` | `ProvedHere` | 169 | 0 | 0 | Duality and grading reversal |
| `prop:susp-diff` | `proposition` | `ProvedHere` | 293 | 0 | 0 | Suspension and differentials |
| `cor:iterated-susp` | `corollary` | `ProvedElsewhere` | 321 | 0 | 1 | Iterated suspension \cite{LV12} |
| `prop:susp-koszul` | `proposition` | `ProvedElsewhere` | 348 | 0 | 1 | Suspension and Koszul duality \cite{LV12} |
| `prop:det-properties` | `proposition` | `ProvedElsewhere` | 377 | 0 | 1 | Properties of determinant lines \cite{Weibel94} |
| `lem:det-ordering` | `lemma` | `ProvedElsewhere` | 409 | 0 | 1 | Determinant and ordering \cite{Weibel94} |
| `prop:det-config` | `proposition` | `ProvedElsewhere` | 432 | 0 | 1 | Determinant lines on configuration spaces \cite{FM94} |
| `prop:det-residue` | `proposition` | `ProvedElsewhere` | 474 | 0 | 1 | Determinant and residues \cite{Har77} |
| `thm:det-bar-cobar-signs` | `theorem` | `ProvedElsewhere` | 489 | 0 | 1 | Determinant conventions and bar-cobar signs \cite{LV12} |
| `prop:master-sign` | `proposition` | `ProvedElsewhere` | 633 | 1 | 1 | Master sign formula {\cite{LV12}} |
| `prop:orient-fm` | `proposition` | `ProvedElsewhere` | 716 | 0 | 1 | Orientation system on FM compactification \cite{FM94} |
| `lem:residue-orient` | `lemma` | `ProvedElsewhere` | 746 | 0 | 2 | Residue and orientation \cite{FM94, Har77} |
| `prop:LV-conversion-complete` | `proposition` | `ProvedHere` | 1159 | 0 | 0 | Loday--Vallette conversion |

#### `appendices/spectral_higher_genus.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:degeneration-special-c` | `theorem` | `ProvedElsewhere` | 128 | 0 | 2 | Degeneration at \texorpdfstring{$E_2$}{E2} \cite{FLM88, FBZ04} |

#### `appendices/type_system.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:type-composition` | `proposition` | `ProvedHere` | 305 | 1 | 0 | Composition rule |
| `prop:type-meetjoin` | `proposition` | `ProvedHere` | 336 | 0 | 0 | Meet and join of packages |
| `prop:type-lattice-wellformed` | `proposition` | `ProvedHere` | 440 | 3 | 0 | Package-lattice well-formedness |
