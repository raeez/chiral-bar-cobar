# Theorem Registry

Auto-generated on 2026-04-30 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` and `\ClaimStatusProvedElsewhere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| Proved surface claims | 2311 |
| Total tagged claims | 3876 |
| Active files in `main.tex` | 131 |
| Total `.tex` files scanned | 151 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1881 |
| `ProvedElsewhere` | 430 |
| `Conjectured` | 340 |
| `Conditional` | 1195 |
| `Heuristic` | 30 |
| `Open` | 0 |

## Proved Surface By Environment

| Environment | Count |
|---|---:|
| `theorem` | 1080 |
| `proposition` | 728 |
| `corollary` | 241 |
| `lemma` | 135 |
| `computation` | 75 |
| `remark` | 50 |
| `calculation` | 2 |

## Proved Surface By Part

| Part | Count |
|---|---:|
| Frame | 27 |
| Part I: Theory | 1184 |
| Part II: Examples | 584 |
| Part III: Connections | 286 |
| Appendices | 230 |

## Most Populated Proved Files

| File | Proved surface claims |
|---|---:|
| `chapters/connections/arithmetic_shadows.tex` | 121 |
| `chapters/theory/ordered_associative_chiral_kd.tex` | 110 |
| `chapters/theory/higher_genus_modular_koszul.tex` | 106 |
| `appendices/ordered_associative_chiral_kd.tex` | 94 |
| `chapters/theory/configuration_spaces.tex` | 69 |
| `chapters/examples/w_algebras.tex` | 66 |
| `chapters/examples/free_fields.tex` | 58 |
| `chapters/theory/higher_genus_foundations.tex` | 58 |
| `appendices/nonlinear_modular_shadows.tex` | 56 |
| `chapters/examples/kac_moody.tex` | 54 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 48 |
| `chapters/theory/higher_genus_complementarity.tex` | 48 |
| `chapters/examples/yangians_computations.tex` | 46 |
| `chapters/theory/en_koszul_duality.tex` | 46 |
| `chapters/examples/w_algebras_deep.tex` | 44 |
| `chapters/examples/yangians_foundations.tex` | 44 |
| `chapters/theory/chiral_modules.tex` | 44 |
| `chapters/theory/shadow_tower_higher_coefficients.tex` | 44 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 42 |
| `chapters/theory/chiral_koszul_pairs.tex` | 38 |

## Complete Proved Registry

### Frame (27)

#### `chapters/frame/guide_to_main_results.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:guide-k3-master-L-value` | `theorem` | `ProvedElsewhere` | 671 | 0 | 0 | K3 paramodular L-value identity |

#### `chapters/frame/heisenberg_frame.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:frame-arnold` | `proposition` | `ProvedHere` | 552 | 1 | 0 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | `ProvedHere` | 901 | 3 | 0 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | `ProvedHere` | 999 | 0 | 0 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | `ProvedElsewhere` | 1206 | 0 | 0 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | `ProvedElsewhere` | 1456 | 0 | 0 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | `ProvedElsewhere` | 1478 | 0 | 0 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | `ProvedElsewhere` | 1626 | 0 | 0 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | `ProvedElsewhere` | 1825 | 0 | 0 | Quantum complementarity for Heisenberg |
| `prop:frame-drinfeld-classical-limit` | `proposition` | `ProvedHere` | 2171 | 1 | 0 | Classical limit and vanishing check |
| `thm:frame-fermion-bar` | `theorem` | `ProvedElsewhere` | 2355 | 1 | 0 | Free fermion bar complex; see Theorem~\ref{thm:fermion-bar-complex-genus-0} |
| `thm:rosetta-sl2-swiss` | `theorem` | `ProvedHere` | 2809 | 2 | 0 | $\mathfrak{sl}_2$ bar complex as $E_1$-chiral coassociative coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | `ProvedHere` | 2881 | 3 | 0 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | `ProvedHere` | 2930 | 0 | 0 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | `ProvedHere` | 3013 | 3 | 0 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | `ProvedHere` | 3051 | 4 | 0 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | `ProvedHere` | 3974 | 2 | 0 | Odd current $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | `ProvedHere` | 4879 | 2 | 0 | The Heisenberg center |

#### `chapters/frame/part_ii_platonic_introduction.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:part-ii-motivic-purity-virasoro-r-le-8` | `theorem` | `ProvedHere` | 372 | 14 | 0 | Motivic purity of $S_r(\Vir_c)$ through $r \le 8$ |
| `thm:part-ii-moonshine-via-fingerprint` | `theorem` | `ProvedHere` | 510 | 2 | 0 | Moonshine via fingerprint twining |
| `thm:part-ii-k3-master-L-value` | `theorem` | `ProvedElsewhere` | 753 | 1 | 0 | K3 master L-value identity for Part~II |

#### `chapters/frame/part_iii_platonic_introduction.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:part-iii-grt-orbit-structure` | `theorem` | `ProvedHere` | 455 | 3 | 0 | $\GRT(\Q)$ acts on $\cM_{\ChirAlg}$ preserving the fingerprint stratification; the historical seven faces are $\Q$-rational orbit representatives |
| `thm:part-iii-k3-master-L-value` | `theorem` | `ProvedElsewhere` | 645 | 1 | 0 | K3 master $L$-value identity on the atlas |

#### `chapters/frame/part_iv_platonic_introduction.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:part-iv-grt-torsor-of-bridges` | `theorem` | `ProvedHere` | 365 | 5 | 3 | $\Face(\cA)$ carries a $\GRT_1(\Q)$ associator action; the fingerprint quotient has nine $\Q$-rational atlas charts |
| `thm:part-iv-celestial-is-holographic-image` | `theorem` | `ProvedHere` | 571 | 0 | 2 | Celestial factorization algebra is the Mellin-shadow image of $\Phol$; \ (internal identification); \ (celestial algebra construction: Pasterski--Shao--Strominger; Strominger $w_{1+\infty}$; Vol~II \texttt{V2-thm:uch-main}). Chain-level class-$M$ statement at $g \ge 1$ open, per Vol~II \texttt{V2-conj:uch-gravity-chain-level}. |
| `thm:part-iv-moonshine-via-holography` | `theorem` | `ProvedHere` | 780 | 1 | 5 | Monster $V^\natural$ as holographic $\Z/2$-orbifold; Dijkgraaf--Witten vanishing; \ (holographic framing of the orbifold as $\Etwo$-topological structure on the orbifold chiral Hochschild complex); \ (construction of $V^\natural$ as $\Z/2$-orbifold of $V_{\Lambda_{24}}$: Frenkel--Lepowsky--Meurman; Monster denominator identity: Borcherds; genus-zero property of McKay--Thompson series: Gannon) |

#### `chapters/frame/preface_sections2_4_draft.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:pref-k3-arthur-parametrisation` | `theorem` | `ProvedElsewhere` | 1327 | 4 | 0 | Arthur parametrisation of the K3 chiral bialgebra |

### Part I: Theory (1184)

#### `chapters/theory/algebraic_foundations.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:quadratic-koszul` | `theorem` | `ProvedElsewhere` | 391 | 1 | 3 | Classical Koszul models; {} \cite{Priddy70,BGS96,LV12} |
| `thm:convolution-master-identification` | `theorem` | `ProvedElsewhere` | 608 | 3 | 2 | Convolution = master object identification |
| `cor:theta-twisting-morphism` | `corollary` | `ProvedElsewhere` | 720 | 3 | 2 | MC element = twisting morphism |
| `prop:universal-twisting-adjunction` | `proposition` | `ProvedElsewhere` | 827 | 0 | 1 | Universal twisting morphisms {\cite{LV12}} |
| `thm:operadic-homotopy-convolution` | `theorem` | `ProvedElsewhere` | 998 | 1 | 1 | Operadic identification of the convolution algebra |
| `cor:quillen-equivalence-chiral` | `corollary` | `ProvedElsewhere` | 1061 | 0 | 1 | Quillen equivalence for chiral bar-cobar |
| `cor:shadow-algebra-homotopy-invariant` | `corollary` | `ProvedElsewhere` | 1101 | 0 | 1 | Homotopy invariance of the shadow algebra |
| `prop:circ-associative` | `proposition` | `ProvedHere` | 1253 | 0 | 1 | Associativity of the composition product |
| `thm:chiral-ran` | `theorem` | `ProvedElsewhere` | 1421 | 1 | 1 | Chiral algebras on Ran space |
| `thm:operadic-bar` | `theorem` | `ProvedElsewhere` | 1743 | 0 | 1 | Operadic bar complex \cite{LV12} |
| `thm:com-lie` | `theorem` | `ProvedElsewhere` | 1858 | 2 | 4 | Com--Lie Koszul duality {\cite{GK94,LV12}} |
| `prop:quadratic-presentations-com-lie` | `proposition` | `ProvedElsewhere` | 1943 | 0 | 1 | Quadratic presentations~\cite{LV12} |
| `prop:orthogonal` | `proposition` | `ProvedHere` | 1952 | 0 | 0 | Orthogonality |
| `thm:chiral-factorization` | `theorem` | `ProvedElsewhere` | 2098 | 0 | 1 | Chiral algebras are factorization algebras |
| `thm:excision-factorization` | `theorem` | `ProvedElsewhere` | 2201 | 1 | 2 | Excision property |
| `thm:factorization-cosheaf` | `theorem` | `ProvedElsewhere` | 2228 | 1 | 1 | Factorization algebras are cosheaves for Weiss covers |

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

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (48)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:curvature-central` | `theorem` | `ProvedHere` | 339 | 0 | 0 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `thm:filtered-cooperads` | `theorem` | `ProvedElsewhere` | 634 | 0 | 1 | Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}) |
| `__unlabeled_chapters/theory/bar_cobar_adjunction_curved.tex:648` | `remark` | `ProvedElsewhere` | 648 | 2 | 1 | Provenance and citation |
| `thm:filtered-to-curved` | `theorem` | `ProvedHere` | 676 | 3 | 0 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | `ProvedHere` | 745 | 4 | 1 | Conilpotency controls algebraic convergence |
| `comp:virasoro-spectral-r-matrix` | `computation` | `ProvedHere` | 945 | 1 | 0 | Virasoro spectral R-matrix on primary states |
| `lem:degree-cutoff` | `lemma` | `ProvedHere` | 1122 | 1 | 0 | Degree cutoff: finite MC equation at each stage |
| `prop:standard-strong-filtration` | `proposition` | `ProvedHere` | 1312 | 2 | 0 | Standard weight truncations and the induced bar filtration |
| `prop:mc4-reduction-principle` | `proposition` | `ProvedHere` | 1433 | 0 | 0 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | `ProvedHere` | 1504 | 1 | 0 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | `ProvedHere` | 1543 | 1 | 0 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | `ProvedHere` | 1583 | 2 | 0 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | `ProvedHere` | 1632 | 5 | 0 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | `ProvedHere` | 1689 | 3 | 0 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | `ProvedHere` | 1752 | 0 | 0 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | `ProvedHere` | 1816 | 4 | 0 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | `ProvedHere` | 1855 | 1 | 0 | Comparison with a completed target by compatible finite quotients |
| `thm:completed-twisting-representability` | `theorem` | `ProvedHere` | 2225 | 0 | 0 | Completed twisting representability |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | `ProvedHere` | 3261 | 0 | 0 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | `ProvedHere` | 3360 | 0 | 0 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | `ProvedHere` | 3403 | 1 | 0 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-stage5-transport-target-3` | `proposition` | `ProvedElsewhere` | 5257 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} transport target-\texorpdfstring{$3$}{3} ladder identities |
| `prop:winfty-stage5-transport-target-4` | `proposition` | `ProvedElsewhere` | 5272 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} transport target-\texorpdfstring{$4$}{4} ladder identities |
| `prop:winfty-stage5-transport-target5-35` | `proposition` | `ProvedElsewhere` | 5316 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} transport singleton from \texorpdfstring{$W^{(3)}W^{(5)}$}{W3W5} |
| `prop:winfty-stage5-transport-target5-45` | `proposition` | `ProvedElsewhere` | 5333 | 2 | 0 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} transport singleton from \texorpdfstring{$W^{(4)}W^{(5)}$}{W4W5} |
| `thm:twisting-mc` | `theorem` | `ProvedElsewhere` | 5924 | 1 | 1 | Twisting by MC elements {\cite{LV12}} |
| `thm:central-implies-strict` | `theorem` | `ProvedHere` | 6052 | 3 | 0 | Central curvature and the square-zero total model |
| `thm:genus-zero-strict` | `theorem` | `ProvedHere` | 6256 | 1 | 0 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | `ProvedHere` | 6268 | 4 | 0 | Strict nilpotence for the corrected genus tower |
| `thm:bar-modular-operad` | `theorem` | `ProvedHere` | 6380 | 2 | 1 | Bar complex as algebra over the modular operad |
| `cor:rectification-ch-infty` | `corollary` | `ProvedElsewhere` | 6569 | 2 | 2 | Rectification of $\mathrm{Ch}_\infty$-algebras |
| `thm:glz-curved` | `theorem` | `ProvedElsewhere` | 6659 | 0 | 2 | GLZ, Theorem 5.3 |
| `thm:fg-factorization-bar-cobar` | `theorem` | `ProvedElsewhere` | 6676 | 0 | 1 | FG, Theorem 7.2.1 |
| `cor:bar-computes-ext` | `corollary` | `ProvedElsewhere` | 6696 | 1 | 1 | Bar cohomology computes Ext |
| `cor:koszul-dual-cooperad` | `corollary` | `ProvedElsewhere` | 6712 | 1 | 1 | Koszul dual coalgebra {\cite{GK94}} |
| `cor:genus-expansion-converges` | `corollary` | `ProvedHere` | 6722 | 2 | 0 | Genus expansion convergence |
| `thm:mixed-boundary-sseq` | `theorem` | `ProvedHere` | 7057 | 0 | 0 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | `ProvedHere` | 7081 | 0 | 0 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | `ProvedHere` | 7129 | 0 | 0 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | `ProvedHere` | 7158 | 0 | 0 | Universality |
| `prop:sugawara-contraction` | `proposition` | `ProvedHere` | 7176 | 0 | 0 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | `ProvedHere` | 7240 | 0 | 0 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | `ProvedHere` | 7256 | 0 | 0 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | `ProvedHere` | 7302 | 0 | 0 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | `ProvedHere` | 7351 | 1 | 0 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | `ProvedHere` | 7395 | 1 | 0 | Diagonal GKO transgression |
| `thm:bcac-extension-obstruction-across-Hn` | `theorem` | `ProvedHere` | 7841 | 7 | 2 | Extension/obstruction formula for curved bar-cobar across $H_n$ |
| `thm:bcac-global-cech-descent` | `theorem` | `ProvedHere` | 7985 | 5 | 4 | Global curved bar-cobar inversion via \v Cech descent |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (42)

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
| `lem:bar-cobar-associated-graded` | `lemma` | `ProvedHere` | 2381 | 0 | 0 | Associated graded |
| `lem:pushforward-preserves-qi` | `lemma` | `ProvedElsewhere` | 2610 | 0 | 1 | Proper pushforward preserves quasi-isomorphisms |
| `lem:complete-filtered-comparison` | `lemma` | `ProvedHere` | 2750 | 0 | 0 | Complete filtered comparison lemma |
| `thm:fm-boundary-acyclicity` | `theorem` | `ProvedHere` | 3148 | 1 | 0 | FM boundary acyclicity |
| `prop:lagrangian-perfectness` | `proposition` | `ProvedHere` | 3360 | 4 | 0 | Perfectness for the standard landscape |
| `prop:subexponential-growth-automatic` | `proposition` | `ProvedHere` | 4593 | 0 | 0 | Sub-exponential growth is automatic |
| `thm:ks-centrality` | `theorem` | `ProvedHere` | 4817 | 0 | 0 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | `ProvedHere` | 4860 | 0 | 0 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | `ProvedHere` | 4911 | 1 | 0 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | `ProvedHere` | 4946 | 0 | 0 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | `ProvedHere` | 4992 | 2 | 0 | Quadratic cone at the scalar basepoint |
| `prop:eta-hessian-transfer` | `proposition` | `ProvedHere` | 5086 | 0 | 0 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | `ProvedHere` | 5122 | 0 | 0 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | `ProvedHere` | 5172 | 0 | 1 | Admissible cyclic rigidity |
| `thm:cech-hca` | `theorem` | `ProvedElsewhere` | 5603 | 0 | 1 | \v{C}ech complex as homotopy chiral algebra |
| `prop:cech-two-element-strict` | `proposition` | `ProvedHere` | 5840 | 1 | 0 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | `ProvedHere` | 6171 | 0 | 0 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | `ProvedHere` | 6231 | 1 | 0 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | `ProvedHere` | 6269 | 0 | 0 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | `ProvedHere` | 6291 | 1 | 0 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | `ProvedHere` | 6389 | 1 | 0 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | `ProvedHere` | 6437 | 2 | 0 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | `ProvedHere` | 6460 | 0 | 0 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | `ProvedHere` | 6505 | 1 | 0 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | `ProvedHere` | 6536 | 1 | 0 | Repeated roots are extension classes |
| `thm:common-core-exact-sequences-inv` | `theorem` | `ProvedHere` | 6607 | 1 | 0 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | `ProvedHere` | 6639 | 2 | 0 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | `ProvedHere` | 6713 | 2 | 0 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | `ProvedHere` | 6753 | 0 | 0 | Explicit coprime-locus projectors |
| `thm:geometric-lift-datum-consequences-inv` | `theorem` | `ProvedHere` | 6857 | 4 | 0 | Divisor-core consequences of lift data |
| `prop:primary-quotient-filtration-lift-inv` | `proposition` | `ProvedHere` | 6910 | 1 | 0 | Primary quotient filtration from lift data |
| `thm:geometric-common-core-factorization-inv` | `theorem` | `ProvedHere` | 6943 | 1 | 0 | Geometric common-core factorization |
| `thm:geometric-ds-common-core-inv` | `theorem` | `ProvedHere` | 6980 | 1 | 0 | Drinfeld--Sokolov common-core transport under lift data |

#### `chapters/theory/bar_construction.tex` (26)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-NAP-homology` | `theorem` | `ProvedHere` | 377 | 1 | 2 | Bar construction as NAP homology |
| `lem:ddr-preserves-log` | `lemma` | `ProvedHere` | 711 | 0 | 1 | $d_{\mathrm{form}}$ preserves logarithmic forms |
| `lem:sign-compatibility` | `lemma` | `ProvedHere` | 923 | 1 | 0 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | `ProvedHere` | 1013 | 8 | 0 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | `ProvedHere` | 1195 | 2 | 0 | Pole decomposition of the bar differential |
| `thm:stokes-config` | `theorem` | `ProvedHere` | 1288 | 2 | 0 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | `ProvedHere` | 1383 | 0 | 0 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | `ProvedHere` | 1425 | 3 | 0 | Arnold relations |
| `cor:cohomology-config` | `corollary` | `ProvedElsewhere` | 1454 | 1 | 2 | Cohomology of configuration spaces {\cite{Arnold69}} |
| `comp:deg0` | `computation` | `ProvedHere` | 1468 | 0 | 0 | Degree 0 |
| `comp:deg1-general` | `computation` | `ProvedHere` | 1497 | 2 | 0 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | `ProvedHere` | 1721 | 1 | 0 | Bar construction is functorial |
| `thm:coassociativity-complete` | `theorem` | `ProvedHere` | 1833 | 0 | 0 | Coassociativity |
| `thm:counit-axioms` | `theorem` | `ProvedHere` | 1900 | 0 | 0 | Counit axioms |
| `thm:diff-is-coderivation` | `theorem` | `ProvedHere` | 1968 | 3 | 1 | Differential is coderivation |
| `lem:orientation` | `lemma` | `ProvedHere` | 2061 | 1 | 1 | Orientation convention |
| `lem:residue-properties` | `lemma` | `ProvedHere` | 2087 | 2 | 0 | Residue properties |
| `thm:geometric-equals-operadic-bar` | `theorem` | `ProvedHere` | 2376 | 2 | 3 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | `ProvedHere` | 2483 | 3 | 1 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | `ProvedElsewhere` | 2555 | 0 | 0 | Uniqueness and functoriality |
| `prop:dgla-axioms-k3-convolution` | `proposition` | `ProvedHere` | 2813 | 2 | 0 | dGLA axioms for $\mathfrak{C}_{\mathbf{H}_{\Delta_5}}$ |
| `rem:theta-universal-MC-k3` | `remark` | `ProvedHere` | 2879 | 1 | 0 | Universal Maurer--Cartan element $\Theta_{\mathbf{H}_{\Delta_5}}$ |
| `thm:MC-hbar3-hbar4-k3` | `theorem` | `ProvedHere` | 2919 | 4 | 0 | MC verification at $\hbar^3,\hbar^4$ |
| `thm:MC-hbar7-hbar12-k3` | `theorem` | `ProvedHere` | 2962 | 2 | 0 | MC verification through weight $\hbar^{12}$ |
| `lem:bc-polar-support-phi-K3` | `lemma` | `ProvedElsewhere` | 3026 | 1 | 0 | Polar support of the K3 elliptic genus; cross-volume reference |
| `thm:bc-unconditional-depth-reduction` | `theorem` | `ProvedHere` | 3041 | 4 | 0 | Unconditional depth-reduction of the pentagon tower on the K3 side |

#### `chapters/theory/chern_weil_level_shift_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:level-shift-universality` | `theorem` | `ProvedHere` | 191 | 2 | 0 | Level-shift universality with convention separation |
| `prop:shift-appears-universally` | `proposition` | `ProvedHere` | 301 | 1 | 0 | Universal occurrence of $k + \hv$ |
| `thm:h-dual-coxeter-coincidence` | `theorem` | `ProvedHere` | 395 | 2 | 0 | Dual Coxeter coincidence |
| `thm:trace-KZ-convention-bridge` | `theorem` | `ProvedHere` | 473 | 4 | 0 | Trace--KZ convention bridge |
| `cor:ap126-healing-universal` | `corollary` | `ProvedHere` | 559 | 3 | 0 | universal healing |

#### `chapters/theory/chiral_center_theorem.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:partial-comp-assoc` | `lemma` | `ProvedHere` | 248 | 1 | 0 | Associativity of partial compositions |
| `prop:geometric-algebraic-hochschild` | `proposition` | `ProvedHere` | 373 | 5 | 0 | Geometric--algebraic comparison for chiral Hochschild |
| `prop:pre-lie-chiral` | `proposition` | `ProvedHere` | 702 | 1 | 0 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | `ProvedHere` | 730 | 2 | 0 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | `ProvedHere` | 751 | 1 | 0 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | `ProvedHere` | 1400 | 2 | 0 | Chiral Deligne--Tamarkin |
| `prop:heisenberg-bv-structure` | `proposition` | `ProvedHere` | 2534 | 1 | 1 | BV algebra structure on $H^*(Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k))$ |
| `prop:chirhoch-cdr` | `proposition` | `ProvedElsewhere` | 2643 | 0 | 1 | Chiral Hochschild cohomology of commutative chiral algebras {\cite{MSV99}} |

#### `chapters/theory/chiral_climax_platonic.tex` (12)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:arnold-cohomology-platonic` | `theorem` | `ProvedElsewhere` | 155 | 1 | 0 | Arnold 1969 |
| `prop:arnold-flatness-platonic` | `proposition` | `ProvedElsewhere` | 206 | 2 | 0 | Arnold flatness |
| `lem:fm-residue-dbar-platonic` | `lemma` | `ProvedElsewhere` | 606 | 1 | 0 | FM residue presentation of $\dbar$ |
| `lem:pullback-presentation-nabla-platonic` | `lemma` | `ProvedHere` | 624 | 4 | 0 | Pullback presentation of $\nabla(A)$ |
| `thm:kohno-monodromy-platonic` | `theorem` | `ProvedElsewhere` | 671 | 1 | 0 | Kohno 1987 |
| `thm:drinfeld-associator-platonic` | `theorem` | `ProvedElsewhere` | 706 | 0 | 0 | Drinfeld $1989$ |
| `prop:cybe-equivalence-platonic` | `proposition` | `ProvedHere` | 739 | 3 | 0 | CYBE equivalence |
| `cor:climax-drinfeld-kohno-platonic` | `corollary` | `ProvedHere` | 773 | 2 | 0 | Drinfeld--Kohno from the climax |
| `cor:climax-borcherds-platonic` | `corollary` | `ProvedHere` | 828 | 2 | 0 | Borcherds product from the climax |
| `cor:climax-arnold-common-root-platonic` | `corollary` | `ProvedHere` | 859 | 3 | 0 | Arnold $1969$ as common root |
| `rem:cclimax-monster-lusztig-conway-norton` | `remark` | `ProvedElsewhere` | 1978 | 0 | 0 | Monster Lusztig level $\ell_{\mathrm{Monster}} = 2$: Vol~I mirror of the Conway--Norton normalisation |
| `thm:cclimax-global-inversion-all-admissible` | `theorem` | `ProvedHere` | 2669 | 15 | 10 | Climax global inversion theorem for $\mathbf{H}_{\Delta_5}$ on $\overline{\mathcal{A}_2}$ |

#### `chapters/theory/chiral_hochschild_koszul.tex` (34)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | `ProvedHere` | 246 | 2 | 1 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | `ProvedHere` | 397 | 3 | 0 | chiral Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | `ProvedHere` | 456 | 1 | 0 | chiral Hochschild spectral sequence |
| `lem:hochschild-shift-computation` | `lemma` | `ProvedHere` | 600 | 5 | 0 | Fulton--MacPherson collapse and chiral Hochschild duality shift |
| `lem:totalization-amplitude` | `lemma` | `ProvedHere` | 702 | 4 | 0 | Per-bar-degree to totalization amplitude transport |
| `lem:chiral-quadratic-koszul` | `lemma` | `ProvedHere` | 848 | 2 | 1 | Quadratic-chiral Koszul transfer |
| `prop:fm-tower-collapse` | `proposition` | `ProvedHere` | 960 | 7 | 1 | Configuration-space collapse via FM-formality spectral sequence |
| `prop:chirhoch-sharp-hilbert` | `proposition` | `ProvedHere` | 1256 | 2 | 0 | Sharp bigraded Hilbert series of chiral Hochschild |
| `cor:chirhoch-heisenberg` | `corollary` | `ProvedHere` | 1295 | 1 | 0 | Heisenberg chiral Hochschild concentration |
| `lem:chiral-homotopy-transport` | `lemma` | `ProvedHere` | 1407 | 2 | 4 | Chiral transport of Shelton--Yuzvinsky contracting homotopy |
| `thm:hochschild-concentration-E1` | `theorem` | `ProvedHere` | 1585 | 6 | 1 | Ordered-bar chiral Hochschild concentration via ordered FM and pure braid Orlik--Solomon |
| `cor:hochschild-averaging-symmetric` | `corollary` | `ProvedHere` | 1645 | 2 | 0 | Averaging to symmetric ChirHoch |
| `lem:chirhoch-descent` | `lemma` | `ProvedHere` | 1809 | 5 | 0 | Chiral Hochschild descent |
| `thm:boson-fermion-lattice` | `theorem` | `ProvedElsewhere` | 3153 | 0 | 1 | Boson-fermion correspondence via lattice VOA; {} \cite{FK80} |
| `comp:boson-hochschild` | `computation` | `ProvedHere` | 3209 | 0 | 0 | Boson chiral Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | `ProvedHere` | 3235 | 1 | 1 | Fermion chiral Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | `ProvedHere` | 3341 | 2 | 2 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | `ProvedHere` | 3435 | 1 | 0 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `prop:modular-deformation-truncation` | `proposition` | `ProvedHere` | 3737 | 1 | 0 | Genus truncation |
| `prop:fay-trisecant` | `proposition` | `ProvedElsewhere` | 4184 | 0 | 1 | Fay trisecant identity for the Szeg\H{o} kernel {\cite[Corollary~2.5 |
| `prop:stokes-regularity-FM` | `proposition` | `ProvedHere` | 4211 | 1 | 5 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | `ProvedHere` | 4297 | 6 | 1 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | `ProvedHere` | 4416 | 2 | 0 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | `ProvedHere` | 4602 | 1 | 2 | Strictification principle for modular deformation theory |
| `prop:non-scalar-criterion` | `proposition` | `ProvedHere` | 5618 | 1 | 0 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | `ProvedHere` | 5773 | 0 | 0 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | `ProvedHere` | 5911 | 1 | 2 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-depth-smooth` | `theorem` | `ProvedHere` | 6043 | 0 | 2 | Sharp geometric depth on smooth moduli |
| `thm:string-field-theory-hochschild` | `theorem` | `ProvedElsewhere` | 6428 | 0 | 1 | String field theory from Hochschild {\cite{Zwi93}} |
| `thm:HH-config-space-formula` | `theorem` | `ProvedHere` | 6561 | 0 | 0 | HH* via configuration spaces |
| `prop:hochschild-cech-ss` | `proposition` | `ProvedHere` | 7156 | 0 | 0 | chiral Hochschild--\v{C}ech spectral sequence |
| `conj:ambient-self-duality` | `proposition` | `ProvedHere` | 7310 | 1 | 0 | Self-duality of the kernel fibre |
| `conj:one-sided-isotropy` | `proposition` | `ProvedHere` | 7349 | 1 | 0 | One-sided isotropy criterion |
| `conj:derived-critical-locus-chk` | `proposition` | `ProvedHere` | 7472 | 2 | 1 | Derived critical locus in a shifted cotangent chart |

#### `chapters/theory/chiral_koszul_pairs.tex` (38)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | `ProvedHere` | 325 | 5 | 1 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | `ProvedHere` | 497 | 2 | 0 | Right twisted tensor product as mapping cone |
| `prop:canonical-contracting-homotopy` | `proposition` | `ProvedHere` | 538 | 4 | 1 | Explicit contracting homotopy for the canonical universal pair |
| `lem:filtered-comparison` | `lemma` | `ProvedHere` | 667 | 0 | 1 | Filtered comparison |
| `lem:filtered-comparison-unit` | `lemma` | `ProvedHere` | 695 | 2 | 1 | Bar-side filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | `ProvedHere` | 746 | 11 | 1 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | `ProvedHere` | 822 | 0 | 1 | Three bijections for chiral twisting morphisms |
| `prop:bar-universal-property` | `proposition` | `ProvedElsewhere` | 913 | 0 | 1 | Universal property of bar construction {\cite{LV12}} |
| `thm:chiral-comparison-lemma` | `theorem` | `ProvedElsewhere` | 946 | 0 | 1 | Comparison lemma for chiral twisted products {\cite[Theorem~2.4.1 |
| `thm:pbw-koszulness-criterion` | `theorem` | `ProvedHere` | 1156 | 3 | 0 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | `ProvedHere` | 1234 | 6 | 1 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | `ProvedHere` | 1289 | 5 | 0 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | `ProvedHere` | 1333 | 6 | 0 | Bar cohomology computes the bar-dual coalgebra |
| `thm:bar-concentration` | `theorem` | `ProvedHere` | 1532 | 7 | 1 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | `ProvedHere` | 1647 | 1 | 2 | Formality implies chiral Koszulness |
| `thm:ext-diagonal-vanishing` | `theorem` | `ProvedHere` | 1752 | 1 | 1 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | `ProvedHere` | 1789 | 2 | 0 | PBW universality |
| `prop:li-bar-poisson-differential` | `proposition` | `ProvedHere` | 2289 | 1 | 0 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | `ProvedHere` | 2360 | 4 | 0 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | `ProvedHere` | 2462 | 1 | 0 | Nilradical obstruction at degenerate admissible levels |
| `prop:d-module-purity-km` | `proposition` | `ProvedHere` | 3958 | 0 | 0 | $\cD$-module purity for affine Kac--Moody algebras |
| `thm:virasoro-koszulness-non-circular-kp` | `theorem` | `ProvedHere` | 4832 | 0 | 5 | Virasoro Koszulness, non-circular |
| `thm:yangian-chart-inclusion-kp` | `theorem` | `ProvedHere` | 4897 | 1 | 0 | Yangian chart inclusion |
| `prop:minimal-model-non-koszul` | `proposition` | `ProvedHere` | 5009 | 0 | 0 | Minimal model non-Koszulness |
| `prop:cumulant-window-inversion` | `proposition` | `ProvedHere` | 5207 | 0 | 0 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | `ProvedHere` | 5263 | 6 | 0 | Geometric bar--cobar duality |
| `prop:bar-cobar-relative-extension` | `proposition` | `ProvedHere` | 5415 | 2 | 0 | Relative extension from relative Verdier base change |
| `thm:yangian-self-dual` | `theorem` | `ProvedHere` | 5681 | 2 | 0 | Type-A Yangian quadratic shadow |
| `prop:yangian-koszul-general` | `proposition` | `ProvedHere` | 5748 | 1 | 5 | Yangian ordered-bar Koszulness in finite windows |
| `thm:coalgebra-axioms-verified` | `theorem` | `ProvedHere` | 5920 | 2 | 0 | Coalgebra structure on \texorpdfstring{$\mathcal{A}^{\mathrm i}_{\mathrm{cand}}$}{A-i-cand} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | `ProvedHere` | 5987 | 4 | 0 | Bar computes the intrinsic bar-dual coalgebra |
| `lem:completion-convergence` | `lemma` | `ProvedHere` | 6061 | 0 | 1 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | `ProvedHere` | 6097 | 7 | 0 | Circularity-free Koszul duality |
| `lem:operadic-koszul-transfer` | `lemma` | `ProvedElsewhere` | 6673 | 0 | 2 | Operadic Koszulness transfer \cite{LV12} |
| `prop:bar-neq-quasiprimary` | `proposition` | `ProvedHere` | 7079 | 1 | 0 | Bar cohomology $\neq$ quasi-primary count |
| `thm:structure-exchange` | `theorem` | `ProvedHere` | 7245 | 1 | 0 | Structure exchange on the finite quadratic lane |
| `thm:ainfty-duality-exchange` | `theorem` | `ProvedHere` | 7313 | 1 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} operations under Verdier pairing |
| `prop:ff-involution-uniqueness` | `proposition` | `ProvedHere` | 7365 | 1 | 0 | Uniqueness of the Feigin--Frenkel involution |

#### `chapters/theory/chiral_modules.tex` (44)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fock-fusion-product` | `proposition` | `ProvedHere` | 213 | 1 | 1 | Fusion product of Heisenberg Fock modules |
| `prop:conformal-blocks-bar` | `proposition` | `ProvedHere` | 600 | 3 | 0 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | `ProvedHere` | 727 | 7 | 0 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | `ProvedHere` | 831 | 2 | 0 | Dimension invariance on the finite-type Verdier surface |
| `prop:kzb-bar-complex` | `proposition` | `ProvedHere` | 896 | 2 | 0 | KZB connection from the bar complex |
| `thm:verlinde-bar` | `theorem` | `ProvedElsewhere` | 960 | 6 | 1 | Verlinde formula via the bar complex {\cite{Verlinde}} |
| `conj:conformal-block-duality` | `proposition` | `ProvedHere` | 1052 | 2 | 0 | Conformal-block ranks from braided categorical duality |
| `conj:koszul-t-structures` | `proposition` | `ProvedHere` | 1376 | 2 | 0 | Highest-weight Koszul t-structure from bar linearity |
| `prop:generic-irreducibility` | `proposition` | `ProvedElsewhere` | 1511 | 1 | 3 | Generic irreducibility {\cite{Kac,FF84}} |
| `thm:kazhdan-lusztig-equivalence` | `theorem` | `ProvedElsewhere` | 1612 | 0 | 3 | Kazhdan--Lusztig equivalence {\cite{KL93}} |
| `thm:bgg-reciprocity` | `theorem` | `ProvedElsewhere` | 1715 | 0 | 2 | BGG reciprocity for affine algebras {\cite{BGG76, KT95}} |
| `prop:tilting-bar` | `proposition` | `ProvedHere` | 1790 | 1 | 0 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | `ProvedHere` | 1855 | 4 | 0 | Verma module bar complex |
| `thm:zhu-correspondence` | `theorem` | `ProvedElsewhere` | 2006 | 0 | 1 | Zhu's correspondence {\cite{Zhu96}} |
| `cor:virasoro-zhu-koszul` | `corollary` | `ProvedHere` | 2123 | 0 | 1 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | `ProvedHere` | 2158 | 1 | 4 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `thm:arakawa-rationality` | `theorem` | `ProvedElsewhere` | 2247 | 1 | 2 | Arakawa's rationality criterion for admissible affine simples {\cite{Arakawa17,Zhu96}} |
| `prop:logarithmic-bar` | `proposition` | `ProvedHere` | 2406 | 0 | 0 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | `ProvedHere` | 2500 | 5 | 1 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | `ProvedHere` | 2620 | 0 | 0 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | `ProvedHere` | 2655 | 0 | 0 | Augmented module bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | `ProvedHere` | 2720 | 2 | 0 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | `ProvedHere` | 2737 | 0 | 0 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | `ProvedHere` | 2777 | 0 | 0 | Koszul dual coalgebras linearize module resolutions |
| `cor:character-koszul` | `corollary` | `ProvedHere` | 2833 | 1 | 0 | Character formula for Koszul case |
| `thm:ainfty-module` | `theorem` | `ProvedElsewhere` | 2872 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} module structure {\cite{Kadeishvili80}} |
| `thm:linfty-cochains` | `theorem` | `ProvedElsewhere` | 2911 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} structure on cochains {\cite{KontsevichSoibelman}} |
| `thm:chiral-gerstenhaber` | `theorem` | `ProvedElsewhere` | 2928 | 0 | 2 | Chiral Gerstenhaber algebra {\cite{Ger63,Tamarkin00}} |
| `thm:weyl-kac-denominator` | `theorem` | `ProvedElsewhere` | 2953 | 0 | 1 | Denominator identity for trivial module {\cite{Kac}} |
| `prop:bgg-sl2-level1` | `proposition` | `ProvedElsewhere` | 3283 | 0 | 1 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda-0)} {\cite{BGG76}} |
| `prop:shapovalov-koszul` | `proposition` | `ProvedHere` | 3739 | 1 | 1 | Shapovalov form under Koszul duality |
| `prop:virasoro-kac-koszul` | `proposition` | `ProvedHere` | 4018 | 0 | 2 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | `ProvedHere` | 4121 | 0 | 0 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | `ProvedHere` | 4180 | 0 | 2 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:4246` | `calculation` | `ProvedHere` | 4246 | 0 | 0 | Boson vacuum module |
| `thm:beilinson-bernstein` | `theorem` | `ProvedElsewhere` | 4358 | 0 | 1 | Beilinson--Bernstein {\cite{BB81}} |
| `thm:chiral-localization` | `theorem` | `ProvedElsewhere` | 4390 | 1 | 1 | Chiral localization {\cite{FG06}} |
| `prop:affine-hecke-kd` | `proposition` | `ProvedElsewhere` | 4501 | 1 | 2 | Affine Hecke algebra and Koszul duality {\cite{BGS96}} |
| `prop:bar-singular-support` | `proposition` | `ProvedHere` | 4555 | 1 | 1 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | `ProvedHere` | 4609 | 2 | 1 | DS reduction commutes with the module bar construction on the exact lane |
| `cor:ds-character-compatibility` | `corollary` | `ProvedHere` | 4742 | 1 | 0 | Characters under DS reduction |
| `thm:module-genus-tower` | `theorem` | `ProvedHere` | 4941 | 5 | 1 | Module tower from bar complex with insertions |
| `prop:ext-bar-resolution` | `proposition` | `ProvedHere` | 5139 | 2 | 0 | Ext via bar resolution |
| `prop:heisenberg-fusion-splitting` | `proposition` | `ProvedHere` | 5412 | 3 | 0 | Heisenberg fusion splitting |

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

#### `chapters/theory/cobar_construction.tex` (28)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:schwartz-kernel-cobar` | `theorem` | `ProvedElsewhere` | 224 | 0 | 1 | Schwartz kernel theorem for cobar {\cite{Hormander}} |
| `lem:bar-holonomicity` | `lemma` | `ProvedHere` | 346 | 2 | 2 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | `ProvedHere` | 407 | 0 | 1 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | `ProvedHere` | 440 | 5 | 0 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | `ProvedHere` | 532 | 3 | 0 | Uncurved cobar nilpotence and curved square via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | `ProvedHere` | 695 | 0 | 0 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | `ProvedHere` | 825 | 3 | 0 | Uncurved distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | `ProvedHere` | 1078 | 1 | 0 | Sign consistency for the uncurved cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | `ProvedHere` | 1260 | 2 | 1 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | `ProvedHere` | 1528 | 2 | 1 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | `ProvedHere` | 1681 | 7 | 0 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | `ProvedHere` | 1762 | 5 | 1 | Explicit cobar-bar augmentation |
| `thm:kontsevich-formality` | `theorem` | `ProvedElsewhere` | 2011 | 0 | 1 | Kontsevich formality (1997) {\cite{Kon99}} |
| `thm:cobar-free` | `theorem` | `ProvedHere` | 2122 | 1 | 0 | Cobar as free chiral algebra |
| `lem:cobar-derivation-extension` | `lemma` | `ProvedHere` | 2346 | 2 | 1 | Cobar derivation extension |
| `thm:weak-topology` | `theorem` | `ProvedHere` | 2600 | 0 | 0 | Topology |
| `thm:poincare-verdier` | `theorem` | `ProvedHere` | 2703 | 2 | 0 | Bar-cobar Verdier pairing |
| `thm:cobar-ainfty` | `theorem` | `ProvedElsewhere` | 2783 | 0 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} structure on cobar {\cite{LV12}} |
| `thm:curved-mc-cobar` | `theorem` | `ProvedHere` | 2832 | 3 | 2 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | `ProvedHere` | 2882 | 0 | 0 | Curvature of the affine bar complex |
| `thm:central-charge-cocycle` | `theorem` | `ProvedHere` | 3127 | 1 | 0 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | `ProvedHere` | 3223 | 1 | 0 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | `ProvedHere` | 3364 | 1 | 0 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | `ProvedHere` | 3389 | 2 | 2 | Bar complex spectral sequence |
| `cor:spectral-degeneration` | `corollary` | `ProvedElsewhere` | 3474 | 1 | 1 | Degeneration {\cite{BGS96}} |
| `thm:essential-image-bar` | `theorem` | `ProvedHere` | 3486 | 3 | 0 | Essential image recognition with unit witness |
| `thm:koszul-necessary` | `theorem` | `ProvedElsewhere` | 3791 | 0 | 1 | Necessary conditions for chiral Koszul duality {\cite{FG12}} |
| `lem:deformation-space` | `lemma` | `ProvedHere` | 4023 | 3 | 0 | Deformation space |

#### `chapters/theory/coderived_models.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:conilpotent-reduction` | `theorem` | `ProvedElsewhere` | 132 | 1 | 1 | Conilpotent reduction |
| `thm:curved-chain-homotopy-trichotomy` | `theorem` | `ProvedHere` | 302 | 3 | 0 | Curved chain homotopy trichotomy |

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
| `prop:comp-ce-bar` | `proposition` | `ProvedHere` | 700 | 1 | 0 | CE reduction |
| `thm:comp-zhu-c-dependence` | `theorem` | `ProvedHere` | 734 | 0 | 0 | $c$-dependence for simple quotients |
| `thm:comp-three-way-bar` | `theorem` | `ProvedHere` | 827 | 3 | 0 | Three-way agreement for bar cohomology |
| `prop:comp-explicit-theta-sl2` | `proposition` | `ProvedHere` | 865 | 0 | 0 | Explicit $\Theta$ for $\AffKM{sl}_2$ |
| `thm:comp-siegel-weil-e8` | `theorem` | `ProvedElsewhere` | 976 | 0 | 0 | Siegel--Weil for $E_8$ |
| `thm:comp-e8-three-way` | `theorem` | `ProvedHere` | 1008 | 0 | 0 | $E_8$ genus-$2$ agreement |
| `prop:comp-n2-kappa` | `proposition` | `ProvedHere` | 1160 | 0 | 0 | Modular characteristic |
| `prop:comp-n2-spectral-flow` | `proposition` | `ProvedHere` | 1223 | 0 | 0 | Spectral flow invariance |
| `thm:comp-genus2-cross` | `theorem` | `ProvedHere` | 1271 | 0 | 0 | Cross-consistency at genus~$2$ |
| `thm:s3-virasoro-c-independent` | `theorem` | `ProvedHere` | 1509 | 0 | 0 | $c$-independence of $S_3$ for Virasoro |

#### `chapters/theory/configuration_spaces.tex` (69)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:FM` | `theorem` | `ProvedElsewhere` | 227 | 0 | 1 | Fulton--MacPherson compactification at genus \texorpdfstring{$g$}{g} \cite{FM94} |
| `thm:boundary-higher-genus` | `theorem` | `ProvedElsewhere` | 371 | 2 | 2 | Boundary strata of \texorpdfstring{$\overline{\mathcal{M}}_{g,n}$}{M-bar(g,n)} {\cite{DeligneM69,Knudsen83}} |
| `thm:local-coords-boundary` | `theorem` | `ProvedHere` | 495 | 0 | 0 | Local holomorphic coordinates near a collision divisor |
| `thm:normal-crossings` | `theorem` | `ProvedHere` | 584 | 0 | 0 | Normal crossings |
| `thm:closure-relations` | `theorem` | `ProvedHere` | 694 | 0 | 0 | Closure relations |
| `cor:dimension-strata` | `corollary` | `ProvedElsewhere` | 725 | 0 | 1 | Boundary divisors in the FM compactification \cite{FM94} |
| `thm:boundary-stratification` | `theorem` | `ProvedElsewhere` | 747 | 0 | 1 | Boundary stratification \cite{FM94} |
| `thm:log-complex` | `theorem` | `ProvedHere` | 822 | 0 | 1 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | `ProvedHere` | 860 | 4 | 1 | Arnold relations and KZ flatness |
| `prop:arnold-higher-genus` | `proposition` | `ProvedHere` | 988 | 5 | 4 | Higher-genus correction to the Arnold-only presentation |
| `prop:twisting-morphism-propagator` | `proposition` | `ProvedHere` | 1297 | 6 | 0 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | `ProvedHere` | 1368 | 1 | 0 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | `ProvedHere` | 1407 | 2 | 0 | Residue operations |
| `prop:residue-local` | `proposition` | `ProvedHere` | 1477 | 1 | 0 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | `ProvedHere` | 1563 | 1 | 0 | Residue sequence |
| `thm:FM-functorial` | `theorem` | `ProvedElsewhere` | 1610 | 0 | 1 | Functoriality of FM compactification |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1631` | `remark` | `ProvedElsewhere` | 1631 | 0 | 1 | Provenance and citation |
| `thm:FM-operad` | `theorem` | `ProvedElsewhere` | 1638 | 0 | 2 | Universal property: FM right-module structure {\cite{FM94,LV12}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1659` | `remark` | `ProvedElsewhere` | 1659 | 0 | 2 | Provenance and citation |
| `thm:fact-homology` | `theorem` | `ProvedElsewhere` | 1681 | 0 | 3 | Factorization homology via configuration spaces {\cite{AF15,CG17,BD04}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:1695` | `remark` | `ProvedElsewhere` | 1695 | 0 | 3 | Provenance and citation |
| `thm:bordered-fm-properties` | `theorem` | `ProvedHere` | 2356 | 2 | 0 | Properties of the bordered FM compactification |
| `lem:nested-blowup-commutativity` | `lemma` | `ProvedElsewhere` | 2434 | 0 | 1 | Nested blowup commutativity |
| `prop:four-type-boundary` | `proposition` | `ProvedHere` | 2455 | 2 | 0 | Four-type boundary decomposition |
| `prop:fundamental-group-genera` | `proposition` | `ProvedElsewhere` | 3526 | 0 | 2 | Fundamental group across genera \cite{Arnold69,Brieskorn73} |
| `thm:fm-associahedron` | `theorem` | `ProvedElsewhere` | 3636 | 0 | 1 | FM compactification and associahedra {\cite{Sta63,}} |
| `prop:eta` | `proposition` | `ProvedHere` | 3643 | 0 | 0 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:os-cohomology-config` | `theorem` | `ProvedElsewhere` | 3674 | 0 | 2 | Cohomology via Orlik--Solomon {\cite{Arnold69,OS80}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3688` | `remark` | `ProvedElsewhere` | 3688 | 0 | 2 | Provenance and citation |
| `thm:NBC` | `theorem` | `ProvedElsewhere` | 3715 | 0 | 1 | NBC basis theorem {\cite{OS80}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3724` | `remark` | `ProvedElsewhere` | 3724 | 0 | 1 | Provenance and citation |
| `thm:chiral-as-fact` | `theorem` | `ProvedElsewhere` | 3843 | 0 | 1 | Chiral algebras as factorization algebras \cite{BD04} |
| `thm:fact-monoidal-corrected` | `theorem` | `ProvedElsewhere` | 3861 | 0 | 2 | Factorization monoidal structure {\cite{BD04,CG17}} |
| `thm:elliptic-compactification` | `theorem` | `ProvedElsewhere` | 3904 | 0 | 1 | Elliptic compactification {\cite{Fay73}} |
| `prop:elliptic-arnold-relations` | `proposition` | `ProvedElsewhere` | 3941 | 0 | 1 | Elliptic correction to the Arnold relation \cite{Fay73} |
| `lem:orientation-compatibility` | `lemma` | `ProvedHere` | 4117 | 0 | 0 | Orientation compatibility |
| `thm:stokes-config-spaces` | `theorem` | `ProvedElsewhere` | 4143 | 0 | 1 | Stokes on configuration spaces \cite{FM94} |
| `prop:operadic-structure` | `proposition` | `ProvedHere` | 4178 | 0 | 0 | Operadic structure |
| `thm:chiral-algebra-objects` | `theorem` | `ProvedElsewhere` | 4204 | 0 | 1 | Chiral algebras as algebra objects \cite{BD04} |
| `thm:nbc-basis-optimality` | `theorem` | `ProvedHere` | 4217 | 0 | 1 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | `ProvedHere` | 4245 | 0 | 0 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | `ProvedHere` | 4267 | 2 | 1 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | `ProvedHere` | 4307 | 2 | 0 | Arnold relations on affine boundary screens |
| `thm:permutohedral-cell-complex` | `theorem` | `ProvedHere` | 4345 | 0 | 0 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | `ProvedHere` | 4385 | 0 | 0 | Complexity bounds |
| `prop:residue-evaluation-complexity` | `proposition` | `ProvedHere` | 4468 | 2 | 0 | Residue evaluation complexity |
| `thm:arnold-jacobi` | `theorem` | `ProvedElsewhere` | 4597 | 3 | 1 | Arnold relation $\Leftrightarrow$ simple-pole Jacobi on the affine screen \cite{LV12} |
| `cor:arnold-operadic` | `corollary` | `ProvedElsewhere` | 4628 | 0 | 1 | Operadic associativity \cite{LV12} |
| `thm:arnold-orlik-solomon` | `theorem` | `ProvedHere` | 4638 | 0 | 0 | Arnold--Orlik--Solomon circuit relations |
| `cor:bar-d-squared-zero` | `corollary` | `ProvedHere` | 4671 | 2 | 0 | Bar differential squares to zero |
| `thm:elliptic-logarithmic-forms` | `theorem` | `ProvedElsewhere` | 4688 | 0 | 1 | Elliptic logarithmic forms \cite{Fay73} |
| `thm:normal-crossings-preservation` | `theorem` | `ProvedHere` | 4706 | 1 | 1 | Normal crossings preservation |
| `thm:complete-coordinates` | `theorem` | `ProvedHere` | 4944 | 0 | 0 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | `ProvedHere` | 4997 | 0 | 0 | Normal bundle formula |
| `prop:transition-functions` | `proposition` | `ProvedElsewhere` | 5066 | 0 | 1 | Transition functions \cite{FM94} |
| `thm:normal-crossings-verified` | `theorem` | `ProvedHere` | 5144 | 0 | 0 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5341` | `computation` | `ProvedHere` | 5341 | 0 | 0 | Explicit examples |
| `thm:chiral-ran-Dmod` | `theorem` | `ProvedElsewhere` | 5443 | 0 | 2 | Chiral algebras ↔ D-modules on Ran space {\cite{BD04,FG12}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5449` | `remark` | `ProvedElsewhere` | 5449 | 0 | 3 | Provenance and citation |
| `thm:chiral-homology-ran` | `theorem` | `ProvedElsewhere` | 5459 | 0 | 2 | Chiral homology via Ran space {\cite{BD04,CG17}} |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5467` | `remark` | `ProvedElsewhere` | 5467 | 0 | 3 | Provenance and citation |
| `thm:confspaces-canonical-curve-HDeltaFive` | `theorem` | `ProvedHere` | 5611 | 0 | 5 | The canonical curve for $\mathbf{H}_{\Delta_5}$ |
| `prop:confspaces-ran-space-nod-smooth-regularisation` | `proposition` | `ProvedHere` | 5822 | 1 | 1 | C1. $\mathrm{Ran}(E^{\mathrm{nod,sm}}_{24})$ is a valid factorisation base |
| `thm:confspaces-factorisation-axiom-disjoint-opens` | `theorem` | `ProvedHere` | 5870 | 2 | 0 | C2. Factorisation axiom for $\mathbf{H}_{\Delta_5}$ on disjoint opens |
| `thm:confspaces-locality-homotopy-colimit` | `theorem` | `ProvedHere` | 5933 | 1 | 1 | C3. Locality and homotopy-colimit descent |
| `prop:confspaces-unit-axiom` | `proposition` | `ProvedHere` | 5970 | 0 | 0 | C3.~bis. Unit axiom |
| `thm:confspaces-co-associativity-nodal-coproduct` | `theorem` | `ProvedHere` | 5994 | 2 | 3 | C4. Co-associativity of the nodal local coproduct at chain level |
| `thm:confspaces-ran-space-cocycle-witness` | `theorem` | `ProvedHere` | 6076 | 2 | 1 | C5. Chain-level cocycle witness for the Ran-space class |
| `cor:confspaces-five-axioms-discharged` | `corollary` | `ProvedHere` | 6154 | 5 | 0 | Five axioms discharged at chain level |

#### `chapters/theory/conformal_anomaly_rigidity_platonic.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:casimir-nonvanishing` | `lemma` | `ProvedHere` | 165 | 0 | 2 | Nonvanishing and integrality of $\Cas$ |
| `thm:conformal-anomaly-rigidity` | `theorem` | `ProvedHere` | 209 | 3 | 0 | Conformal-anomaly rigidity |
| `thm:c-zero-coproduct-is-constant` | `theorem` | `ProvedHere` | 267 | 2 | 4 | Coproduct is constant at $c = 0$ |
| `prop:spectral-parameter-forced-at-nonzero-c` | `proposition` | `ProvedHere` | 305 | 3 | 0 | Spectral parameter is forced at $c \neq 0$ |
| `thm:universal-coefficient` | `theorem` | `ProvedHere` | 329 | 1 | 0 | Universality of the coefficient |
| `cor:forbidden-c-0-locus-chiralization` | `corollary` | `ProvedHere` | 370 | 4 | 0 | Chiralisation is obstructed away from $c = 0$ |
| `rem:comparison-with-ktheory-anomaly` | `remark` | `ProvedElsewhere` | 396 | 1 | 0 | Comparison with the Virasoro \texorpdfstring{$\kappa$}{kappa}-conductor |

#### `chapters/theory/derived_langlands.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:ff-center-dl` | `theorem` | `ProvedElsewhere` | 290 | 0 | 2 | Feigin--Frenkel center |
| `thm:kl-equivalence` | `theorem` | `ProvedElsewhere` | 1131 | 0 | 1 | Kazhdan--Lusztig equivalence on the semisimplified target |
| `thm:fg-localization` | `theorem` | `ProvedElsewhere` | 1360 | 0 | 1 | Frenkel--Gaitsgory localization |
| `thm:dl-C1-r-existence` | `theorem` | `ProvedHere` | 2882 | 1 | 2 | C1 -- existence and pole-order structure |
| `thm:dl-C2-CYBE` | `theorem` | `ProvedHere` | 2918 | 0 | 0 | C2 -- classical Yang--Baxter equation |
| `thm:dl-C3-lie-bialgebra` | `theorem` | `ProvedHere` | 2960 | 2 | 1 | C3 -- Lie bialgebra structure on $\frakg_{\Delta_5}$ |
| `thm:dl-kazhdan-classical-limit` | `theorem` | `ProvedHere` | 3007 | 5 | 0 | Kazhdan classical-limit theorem |
| `thm:dl-chenevier-nonreduced-delta5` | `theorem` | `ProvedHere` | 3548 | 1 | 0 | Chenevier determinant on the non-reduced deformation ring $R^{\mathrm{def}}_{\Delta_5}$ |
| `thm:dl-kazhdan-C1-mukai-eigenvalue` | `theorem` | `ProvedHere` | 4024 | 4 | 0 | Mukai-graded Hecke eigenvalue formula |

#### `chapters/theory/e1_modular_koszul.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | `ProvedHere` | 230 | 0 | 1 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | `ProvedHere` | 249 | 1 | 1 | — |
| `prop:e1-nonsplitting-obstruction` | `proposition` | `ProvedHere` | 442 | 1 | 2 | $E_1$ canonical section obstruction |
| `prop:e1-nonsplitting-genus1` | `proposition` | `ProvedHere` | 547 | 3 | 0 | $E_1$ genus-one modular-section obstruction |
| `prop:symmetric-descent` | `proposition` | `ProvedHere` | 982 | 0 | 0 | Symmetric descent |
| `cor:r-matrix-sigma2-symmetric` | `corollary` | `ProvedHere` | 1836 | 1 | 0 | $r$-matrix $\Sigma_2$-symmetry on the four archetypes |
| `thm:e1-formality-bridge` | `theorem` | `ProvedHere` | 2189 | 0 | 0 | Formality bridge |
| `thm:e1-formality-failure` | `theorem` | `ProvedHere` | 2228 | 1 | 0 | Formality failure for genuinely $\Eone$-chiral algebras |
| `thm:e1-mc-finite-degree` | `theorem` | `ProvedHere` | 2341 | 1 | 0 | $E_1$ MC equation at finite degree |
| `rem:ribbon-structure-count` | `remark` | `ProvedHere` | 2463 | 0 | 0 | Ribbon structure count |
| `prop:sn-irrep-decomposition-bar` | `proposition` | `ProvedHere` | 3331 | 0 | 1 | $\Sigma_n$-irreducible decomposition of the ordered bar complex |
| `lem:bare-graph-no-thooft` | `lemma` | `ProvedHere` | 3440 | 0 | 0 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | `ProvedHere` | 3461 | 0 | 0 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | `ProvedHere` | 3503 | 0 | 0 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | `ProvedHere` | 3525 | 1 | 0 | Exact $N^{\chi}$ weighting from traced open color |

#### `chapters/theory/e3_identification_chain_level_platonic.tex` (7)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:e3-identification-chain-level-associator-fixed` | `theorem` | `ProvedHere` | 410 | 5 | 3 | Chain-level $\Ethree$-identification, $\Phi = \Phi_{\KZ}$ |
| `prop:associator-dependence-explicit` | `proposition` | `ProvedHere` | 594 | 2 | 3 | Associator-dependence of the chain map |
| `thm:operad-level-to-algebra-level-lift` | `theorem` | `ProvedHere` | 740 | 4 | 4 | Operad-level to algebra-level formality lift |
| `cor:e3-solvable-unconditional` | `corollary` | `ProvedHere` | 868 | 2 | 3 | Chain-level identification for solvable~$\fg$ is unconditional |
| `prop:sl2-associator-test` | `proposition` | `ProvedHere` | 1062 | 3 | 4 | $\mathfrak{sl}_2$ associator-test |
| `thm:humbert-lusztig-mukai-8` | `theorem` | `ProvedHere` | 1245 | 1 | 0 | Humbert--Lusztig--Mukai triple coincidence on the $\mathcal{B}$-family |
| `cor:kl-equivalence-k3-bkm` | `corollary` | `ProvedHere` | 1364 | 2 | 0 | Kazhdan--Lusztig equivalence at $q_{\mathrm{K3}} = e^{2\pi i/8}$ |

#### `chapters/theory/en_koszul_duality.tex` (46)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:en-chiral-bridge` | `theorem` | `ProvedHere` | 156 | 3 | 1 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
| `thm:arnold-presentation` | `theorem` | `ProvedElsewhere` | 291 | 1 | 1 | Arnold presentation {\cite{Arnold69}}; \texorpdfstring{$\bC \cong \bR^2$}{C = R2} |
| `thm:totaro-presentation` | `theorem` | `ProvedElsewhere` | 308 | 0 | 2 | Totaro presentation, general \texorpdfstring{$n$}{n} {\cite{Totaro96, Coh76}} |
| `prop:fm-boundary-strata` | `proposition` | `ProvedElsewhere` | 393 | 0 | 2 | Boundary strata and operadic structure |
| `prop:linking-sphere-residue` | `proposition` | `ProvedHere` | 520 | 1 | 0 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | `ProvedHere` | 595 | 2 | 1 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `thm:en-koszul-duality` | `theorem` | `ProvedElsewhere` | 748 | 0 | 3 | \texorpdfstring{$\En$}{En} Koszul duality |
| `thm:af-pkd` | `theorem` | `ProvedElsewhere` | 849 | 0 | 1 | Poincar\'e--Koszul duality, AF {\cite{AF15}} |
| `thm:en-d-squared` | `theorem` | `ProvedElsewhere` | 959 | 1 | 1 | \texorpdfstring{$d^2 = 0$}{d squared = 0} for the \texorpdfstring{$\En$}{En} bar complex |
| `prop:kappa-universality-en` | `proposition` | `ProvedHere` | 1006 | 0 | 0 | Kappa universality across $n$ |
| `prop:shadow-stabilization` | `proposition` | `ProvedHere` | 1032 | 0 | 0 | Shadow stabilization threshold |
| `thm:knudsen-higher-enveloping` | `theorem` | `ProvedElsewhere` | 1090 | 0 | 1 | Higher enveloping algebras |
| `thm:e2-formality` | `theorem` | `ProvedElsewhere` | 1120 | 0 | 2 | Formality of \texorpdfstring{$\Etwo$}{E2} |
| `prop:en-formality` | `proposition` | `ProvedElsewhere` | 1151 | 1 | 2 | \texorpdfstring{$\En$}{En} formality for \texorpdfstring{$n \geq 2$}{n >= 2} |
| `thm:willwacher-wheels` | `theorem` | `ProvedElsewhere` | 1200 | 0 | 1 | Wheel cocycles and $\mathrm{grt}_1$ |
| `prop:shadow-gc2-bridge` | `proposition` | `ProvedHere` | 1223 | 1 | 0 | Shadow obstruction tower to $\mathrm{GC}_2$ bridge |
| `thm:bar-swiss-cheese` | `theorem` | `ProvedHere` | 1482 | 4 | 0 | Bar complex as $\Eone$-chiral coassociative coalgebra |
| `prop:sc-koszul-dual-three-sectors` | `proposition` | `ProvedHere` | 1790 | 1 | 0 | Koszul dual cooperad of \texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}: three sectors |
| `prop:operadic-center-existence` | `proposition` | `ProvedHere` | 1933 | 1 | 0 | Existence of the operadic center |
| `thm:operadic-center-hochschild` | `theorem` | `ProvedHere` | 1986 | 7 | 2 | The operadic center of $\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex |
| `thm:center-geometric-inevitability` | `theorem` | `ProvedHere` | 2336 | 4 | 0 | Geometric inevitability of the chiral center |
| `prop:braces-from-center` | `proposition` | `ProvedHere` | 2530 | 2 | 0 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | `ProvedHere` | 2579 | 5 | 1 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | `ProvedHere` | 2655 | 2 | 0 | Terminality of the center |
| `cor:center-functor` | `corollary` | `ProvedHere` | 2744 | 1 | 0 | The center functor |
| `thm:topologization` | `theorem` | `ProvedHere` | 3166 | 4 | 2 | Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}} |
| `thm:e-infinity-topologization` | `theorem` | `ProvedHere` | 3307 | 1 | 0 | $E_\infty$-Topologization via iterated Sugawara |
| `cor:e-ladder-vir-wn-winfty` | `corollary` | `ProvedHere` | 3331 | 2 | 0 | $E_n$ ladder specializations |
| `thm:e-infinity-topologization-master` | `theorem` | `ProvedHere` | 4022 | 9 | 1 | $\Einf$-topologization master theorem |
| `cor:virasoro-N-2-climax` | `corollary` | `ProvedHere` | 4272 | 1 | 0 | Virasoro ($N=2$) recovers the Volume~II climax |
| `cor:WN-E-Nplus1-top` | `corollary` | `ProvedHere` | 4292 | 1 | 0 | $\cW_N$ gives $E_{N+1}$-topological |
| `cor:Winfty-Einf-top` | `corollary` | `ProvedHere` | 4311 | 1 | 0 | $\cW_\infty$ gives $\Einf$-topological |
| `thm:coset-conformal-inheritance` | `theorem` | `ProvedHere` | 4388 | 0 | 1 | Coset conformal inheritance |
| `prop:sugawara-gauge-rectification` | `proposition` | `ProvedHere` | 4527 | 6 | 1 | Chain-level $\Ethree^{\mathrm{top}}$ for affine Kac--Moody via gauge rectification |
| `prop:e3-via-dunn` | `proposition` | `ProvedHere` | 5004 | 4 | 3 | $\Ethree^{\mathrm{top}}$ via Dunn additivity, bypassing the Higher Deligne Conjecture |
| `thm:e3-cs` | `theorem` | `ProvedElsewhere` | 5178 | 1 | 2 | The $\Ethree$-algebra and Chern--Simons |
| `thm:cfg` | `theorem` | `ProvedElsewhere` | 5214 | 0 | 1 | Costello--Francis--Gwilliam~\cite{CFG25} |
| `lem:en-formality-deformation-classification` | `lemma` | `ProvedHere` | 5337 | 0 | 4 | Formality reduction for $\En$-deformations of commutative algebras |
| `thm:e3-identification` | `theorem` | `ProvedHere` | 5435 | 9 | 6 | Identification of $\Ethree$-deformation families |
| `prop:e3-explicit-sl2` | `proposition` | `ProvedHere` | 5933 | 5 | 0 | Explicit $\Ethree$ operations on $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\mathfrak{sl}_2))$ |
| `prop:chiral-p3-structure` | `proposition` | `ProvedHere` | 6475 | 1 | 1 | The chiral $\Pthree$ structure |
| `thm:chiral-e3-structure` | `theorem` | `ProvedHere` | 6562 | 7 | 3 | Structure of the chiral $\Ethree$-algebra |
| `lem:bv-p3-commutativity` | `lemma` | `ProvedHere` | 6823 | 3 | 0 | Commutativity of the BV operator and the chiral $\Pthree$ bracket |
| `prop:chiral-e3-dmod` | `proposition` | `ProvedHere` | 6964 | 1 | 1 | The $\cD$-module structure |
| `thm:chiral-e3-cfg` | `theorem` | `ProvedHere` | 7050 | 5 | 0 | Formal disk restriction recovers CFG |
| `prop:khan-zeng-topological` | `proposition` | `ProvedHere` | 7263 | 3 | 2 | Topological enhancement via Sugawara |

#### `chapters/theory/existence_criteria.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:quadratic-have-duals` | `theorem` | `ProvedElsewhere` | 160 | 1 | 2 | Quadratic finite-dual coalgebras exist \cite{LV12, Priddy70} |
| `thm:completed-koszul-dual` | `theorem` | `ProvedElsewhere` | 435 | 0 | 1 | Completed Koszul dual \cite{Positselski11} |
| `thm:completion-convergence-criteria` | `theorem` | `ProvedHere` | 534 | 0 | 0 | Finite-window convergence criterion |
| `prop:kac-moody-koszul-duals` | `proposition` | `ProvedElsewhere` | 761 | 1 | 2 | Affine Kac--Moody existence criterion \cite{FBZ04, Feigin-Frenkel} |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | `ProvedHere` | 20 | 4 | 0 | Central filtered deformations as curved models |
| `thm:bar-convergence-fc` | `theorem` | `ProvedHere` | 249 | 7 | 0 | Finite-window convergence in the filtered and curved regimes |

#### `chapters/theory/fourier_seed.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | `ProvedHere` | 61 | 0 | 0 | Three properties of the propagator |
| `prop:fourier-com-lie-duality` | `proposition` | `ProvedHere` | 222 | 0 | 0 | — |
| `comp:fourier-heisenberg-n2` | `computation` | `ProvedHere` | 269 | 2 | 0 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | `ProvedHere` | 318 | 2 | 0 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | `ProvedHere` | 347 | 4 | 0 | Heisenberg bar seed |
| `prop:fourier-five-duality-objects` | `proposition` | `ProvedHere` | 409 | 4 | 0 | The five duality objects and the suspension |
| `prop:fourier-mukai-identification` | `proposition` | `ProvedHere` | 510 | 3 | 3 | Poincar\'e connection seed |
| `prop:fourier-propagator-degeneration` | `proposition` | `ProvedHere` | 560 | 0 | 2 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | `ProvedHere` | 618 | 1 | 4 | Degeneration of the Poincar\'e connection |
| `thm:fourier-recovery` | `theorem` | `ProvedHere` | 683 | 4 | 0 | Algebraic seed of the Fourier kernel |
| `comp:fourier-km-bar` | `computation` | `ProvedHere` | 806 | 0 | 0 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | `ProvedHere` | 827 | 1 | 1 | — |
| `thm:fourier-specialization` | `theorem` | `ProvedHere` | 871 | 0 | 1 | Specialization |

#### `chapters/theory/ftm_seven_fold_tfae_platonic.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:ftm-spoke-koszul-pbw` | `proposition` | `ProvedHere` | 272 | 4 | 0 | Spoke 1 |
| `prop:ftm-spoke-counit-pbw` | `proposition` | `ProvedHere` | 295 | 7 | 0 | Spoke 2 |
| `prop:ftm-spoke-unit-pbw` | `proposition` | `ProvedHere` | 326 | 6 | 0 | Spoke 3 |
| `prop:ftm-spoke-bar-conc-pbw` | `proposition` | `ProvedHere` | 392 | 7 | 0 | Spoke 5 |

#### `chapters/theory/genus_2_ddybe_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:genus-2-kzb-connection-platonic` | `theorem` | `ProvedElsewhere` | 167 | 0 | 2 | Flat KZB connection on $\overline{\cM}_{2,n}\times\HHH_2$ |
| `thm:fay-trisecant-genus-2-specific` | `theorem` | `ProvedElsewhere` | 252 | 1 | 1 | Fay trisecant, three-term Szeg\H{o} form |
| `cor:g2-chi-minus-12` | `corollary` | `ProvedHere` | 654 | 1 | 0 | $\chi=-12$ from rank-$4$ KZB local system |

#### `chapters/theory/higher_genus_complementarity.tex` (48)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:hodge-curvature-scalar-projection` | `proposition` | `ProvedHere` | 145 | 1 | 1 | Hodge curvature and scalar projection |
| `prop:theorem-c-object-firewall` | `proposition` | `ProvedHere` | 205 | 0 | 0 | Object firewall for Theorem~C |
| `lem:involution-splitting` | `lemma` | `ProvedHere` | 379 | 0 | 0 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | `ProvedHere` | 435 | 2 | 0 | Perfectness criterion for the strict flat relative bar family |
| `lem:genus-filtration` | `lemma` | `ProvedHere` | 936 | 1 | 0 | Genus filtration |
| `thm:ss-quantum` | `theorem` | `ProvedHere` | 1000 | 3 | 0 | Spectral sequence for quantum corrections |
| `thm:verdier-duality-config-complete` | `theorem` | `ProvedHere` | 1271 | 2 | 1 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | `ProvedHere` | 1344 | 3 | 0 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | `ProvedHere` | 1384 | 5 | 0 | Spectral sequence duality |
| `lem:finite-window-complementarity` | `lemma` | `ProvedHere` | 2375 | 2 | 0 | Finite-window complementarity and completed limit |
| `thm:ss-genus-stratification` | `theorem` | `ProvedHere` | 2529 | 1 | 0 | Spectral sequence as genus stratification |
| `cor:vanishing-quantum` | `corollary` | `ProvedHere` | 2715 | 1 | 0 | Vanishing results |
| `thm:fermion-boson-koszul-hg` | `theorem` | `ProvedHere` | 3076 | 0 | 0 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | `ProvedHere` | 3591 | 0 | 0 | BD 3.4.12: genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | `ProvedHere` | 3641 | 0 | 1 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | `ProvedHere` | 3654 | 0 | 2 | Normal crossings persist at higher genus |
| `lem:relative-diagonal` | `lemma` | `ProvedHere` | 3755 | 0 | 0 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | `ProvedHere` | 3795 | 0 | 1 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | `ProvedHere` | 3823 | 0 | 0 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | `ProvedHere` | 3845 | 1 | 0 | Chevalley--Cousin at boundary |
| `lem:graded-acyclic` | `lemma` | `ProvedHere` | 4132 | 0 | 1 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | `ProvedHere` | 4220 | 0 | 0 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | `ProvedHere` | 4247 | 4 | 1 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | `ProvedHere` | 4275 | 0 | 0 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | `ProvedHere` | 4311 | 0 | 1 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | `ProvedHere` | 4338 | 3 | 0 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | `ProvedHere` | 4399 | 1 | 1 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | `ProvedHere` | 4445 | 0 | 1 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | `ProvedHere` | 4484 | 1 | 0 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | `ProvedHere` | 4513 | 0 | 1 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | `ProvedHere` | 4541 | 0 | 0 | Algebra structure from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | `ProvedHere` | 4569 | 4 | 0 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | `ProvedHere` | 4601 | 8 | 1 | Open-stratum quasi-isomorphism |
| `lem:extension-across-boundary-qi` | `lemma` | `ProvedHere` | 4676 | 0 | 0 | Extension across boundary |
| `lem:e2-collapse-higher-genus` | `lemma` | `ProvedHere` | 4809 | 1 | 0 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | `ProvedHere` | 4887 | 0 | 1 | Pants decomposition as excision |
| `prop:e2-collapse-formality` | `proposition` | `ProvedHere` | 5024 | 2 | 1 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | `ProvedHere` | 5199 | 0 | 0 | Ambient complementarity in tangent form |
| `prop:legendre-duality-potentials` | `proposition` | `ProvedHere` | 5727 | 0 | 0 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | `ProvedHere` | 5742 | 0 | 0 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | `ProvedHere` | 5772 | 0 | 0 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | `ProvedHere` | 5796 | 0 | 0 | Criterion for fake complementarity |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | `ProvedHere` | 6070 | 1 | 0 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | `ProvedHere` | 6156 | 0 | 0 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | `ProvedHere` | 6200 | 0 | 0 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | `ProvedHere` | 6277 | 4 | 0 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | `ProvedHere` | 6360 | 2 | 0 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | `ProvedHere` | 6429 | 1 | 0 | First nonlinear holographic anomaly |

#### `chapters/theory/higher_genus_foundations.tex` (58)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | `ProvedHere` | 1342 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | `ProvedHere` | 1442 | 0 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | `ProvedHere` | 1537 | 0 | 0 | Pentagon identity |
| `thm:higher-associahedron-m5` | `theorem` | `ProvedElsewhere` | 1575 | 0 | 1 | Higher associahedron identity for \texorpdfstring{$m_5$}{m5} {\cite{Sta63}} |
| `thm:catalan-parenthesization` | `theorem` | `ProvedElsewhere` | 1587 | 0 | 1 | Catalan identity at higher levels {\cite{Sta97}} |
| `thm:verdier-NAP` | `theorem` | `ProvedElsewhere` | 1619 | 1 | 2 | Verdier duality = NAP duality {\cite{AF15,KS90}} |
| `thm:cobar-ainfty-complete` | `theorem` | `ProvedHere` | 1709 | 2 | 1 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | `ProvedHere` | 1821 | 9 | 1 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | `ProvedHere` | 1968 | 0 | 0 | Verdier duality of operations |
| `thm:geometric-com-lie-enhancement` | `theorem` | `ProvedElsewhere` | 2055 | 0 | 1 | Geometric enhancement of Com-Lie |
| `thm:ainfty-com-lie-interchange` | `theorem` | `ProvedElsewhere` | 2093 | 0 | 1 | Maximal vs.\ trivial \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:cobar-resolution-scoped` | `theorem` | `ProvedElsewhere` | 2333 | 2 | 1 | Cobar resolution on the Koszul locus {\cite{LV12}} |
| `thm:genus-graded-mc` | `theorem` | `ProvedElsewhere` | 2393 | 2 | 2 | Maurer--Cartan = deformations {\cite{Kon03,Ger63}} |
| `prop:yangian-from-deformation` | `proposition` | `ProvedElsewhere` | 2421 | 0 | 1 | Yangian from deformation {\cite{Drinfeld85}} |
| `prop:deforming-heisenberg` | `proposition` | `ProvedHere` | 2448 | 1 | 0 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | `ProvedHere` | 2482 | 0 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | `ProvedHere` | 2516 | 0 | 0 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | `ProvedHere` | 2536 | 1 | 0 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | `ProvedHere` | 2552 | 1 | 0 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | `ProvedHere` | 2909 | 5 | 0 | Bar-cobar isomorphism, retained for equation labels |
| `thm:moduli-structure` | `theorem` | `ProvedElsewhere` | 3141 | 0 | 2 | Structure of \texorpdfstring{$\overline{\mathcal{M}}_{g,n}$}{M-bar(g,n)} {\cite{DeligneM69,Knudsen83}} |
| `thm:universal-curve-fibration` | `theorem` | `ProvedElsewhere` | 3163 | 0 | 1 | Universal curve fibration {\cite{Knudsen83}} |
| `thm:period-matrix-properties` | `theorem` | `ProvedElsewhere` | 4043 | 0 | 1 | Properties of the period matrix {\cite{Fay73}} |
| `thm:theta-properties` | `theorem` | `ProvedElsewhere` | 4087 | 0 | 1 | Theta function properties {\cite{Fay73}} |
| `thm:prime-form-properties` | `theorem` | `ProvedElsewhere` | 4124 | 0 | 1 | Prime form properties {\cite{Fay73}} |
| `thm:genus-differential` | `theorem` | `ProvedHere` | 4197 | 6 | 0 | Leray decomposition of the corrected differential |
| `thm:concrete-quantum-differential` | `theorem` | `ProvedHere` | 4306 | 2 | 0 | Concrete quantum differential |
| `thm:modular-vs-quasi` | `theorem` | `ProvedElsewhere` | 4517 | 0 | 1 | Modular vs quasi-modular {\cite{KP84}} |
| `thm:theta-zero` | `theorem` | `ProvedElsewhere` | 4575 | 0 | 1 | Theta zero values {\cite{Fay73}} |
| `thm:eta-properties-genus1` | `theorem` | `ProvedHere` | 4600 | 0 | 0 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:genus1-d-squared` | `theorem` | `ProvedHere` | 4710 | 1 | 0 | Nilpotency at genus 1 |
| `thm:odd-even-g2` | `theorem` | `ProvedElsewhere` | 5012 | 0 | 1 | Odd vs even characteristics {\cite{Fay73}} |
| `thm:theta-g3` | `theorem` | `ProvedElsewhere` | 5142 | 0 | 1 | Theta characteristics at genus 3 {\cite{Fay73}} |
| `thm:e1-page-complete` | `theorem` | `ProvedHere` | 5231 | 3 | 0 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | `ProvedHere` | 5276 | 2 | 0 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:mmm-classes` | `theorem` | `ProvedElsewhere` | 5333 | 0 | 2 | Tautological Hodge and boundary classes {\cite{Mumford83}} |
| `__unlabeled_chapters/theory/higher_genus_foundations.tex:5359` | `remark` | `ProvedElsewhere` | 5359 | 0 | 1 | Tautological scope |
| `thm:mumford-formula` | `theorem` | `ProvedElsewhere` | 5386 | 0 | 1 | Faber--Pandharipande $\lambda_g$ formula {\cite{FP03}} |
| `thm:obstruction-general` | `theorem` | `ProvedHere` | 5587 | 3 | 0 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | `ProvedHere` | 5641 | 0 | 1 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `prop:scalar-obstruction-hodge-euler` | `proposition` | `ProvedHere` | 6244 | 1 | 0 | Scalar obstruction equals Hodge Euler class |
| `lem:k-theoretic-globalization-bar` | `lemma` | `ProvedHere` | 6410 | 0 | 0 | $K$-theoretic globalization of the scalar bar class |
| `prop:lambda-g-clutching` | `proposition` | `ProvedHere` | 6813 | 2 | 0 | Clutching formulas for the Hodge Euler class |
| `prop:clutching-uniqueness` | `proposition` | `ProvedHere` | 6903 | 1 | 2 | Clutching uniqueness of the Hodge Euler class, socle scope |
| `prop:f2-quartic-dependence` | `proposition` | `ProvedHere` | 7804 | 1 | 0 | Genus-$2$ quartic dependence |
| `cor:kappa-periodicity` | `corollary` | `ProvedHere` | 7881 | 0 | 0 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `prop:bar-tautological-filtration` | `proposition` | `ProvedHere` | 8110 | 3 | 1 | Bar spectral sequence and tautological filtration |
| `lem:stable-graph-d-squared` | `lemma` | `ProvedHere` | 8662 | 0 | 0 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | `ProvedHere` | 8724 | 2 | 0 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | `ProvedHere` | 8762 | 1 | 0 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | `ProvedHere` | 8804 | 0 | 0 | Extremal pages |
| `thm:loop-order-collapse` | `theorem` | `ProvedHere` | 9050 | 3 | 0 | Loop-order convergence and finite-depth collapse bound |
| `cor:loop-decomposition-bar` | `corollary` | `ProvedHere` | 9094 | 1 | 0 | Associated graded by loop order |
| `thm:feynman-involution` | `theorem` | `ProvedElsewhere` | 9131 | 0 | 1 | Feynman involution \textup{\cite[Theorem~5.2 |
| `thm:virtual-euler-char` | `theorem` | `ProvedHere` | 9205 | 1 | 0 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | `ProvedHere` | 9233 | 0 | 2 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | `ProvedHere` | 9283 | 0 | 0 | Weight system map |
| `thm:log-clutching-degeneration` | `theorem` | `ProvedElsewhere` | 9482 | 0 | 1 | Logarithmic clutching from degeneration geometry |

#### `chapters/theory/higher_genus_modular_koszul.tex` (106)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:pbw-allgenera-principal-w` | `theorem` | `ProvedHere` | 919 | 8 | 0 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `lem:pbw-weightwise-g-module` | `lemma` | `ProvedHere` | 1062 | 0 | 0 | Weightwise reduction of the genus enrichment to \texorpdfstring{$\fg$}{g}-modules |
| `lem:pbw-mixed-factorization` | `lemma` | `ProvedHere` | 1121 | 1 | 0 | Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)} |
| `thm:pbw-genus1-km` | `theorem` | `ProvedHere` | 1169 | 7 | 1 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `thm:pbw-allgenera-km` | `theorem` | `ProvedHere` | 1511 | 8 | 0 | PBW degeneration at all genera for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | `ProvedHere` | 1771 | 8 | 0 | PBW degeneration at all genera for Virasoro |
| `thm:pbw-universal-semisimple` | `theorem` | `ProvedHere` | 1985 | 4 | 0 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `prop:hook-pbw` | `proposition` | `ProvedHere` | 2146 | 1 | 0 | Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses |
| `thm:pbw-propagation` | `theorem` | `ProvedHere` | 2238 | 4 | 0 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | `ProvedHere` | 2397 | 0 | 0 | Locality of the collision differential |
| `lem:e2-higher-genus` | `lemma` | `ProvedHere` | 2796 | 0 | 0 | $E_2$ collapse at higher genus |
| `prop:genus-completed-mc-framework` | `proposition` | `ProvedHere` | 6332 | 0 | 0 | Genus-completed MC algebra |
| `prop:cyclic-ce-identification` | `proposition` | `ProvedHere` | 6411 | 0 | 0 | Cyclic CE cohomology identification |
| `thm:kappa-universal-class` | `theorem` | `ProvedHere` | 10962 | 3 | 1 | Universal $\kappa$ class: existence, uniqueness, specialization |
| `thm:convolution-dg-lie-structure` | `theorem` | `ProvedHere` | 11421 | 2 | 1 | dg~Lie structure from the modular operad |
| `thm:operadic-homotopy-convolution-modular` | `theorem` | `ProvedElsewhere` | 12085 | 1 | 3 | Operadic homotopy convolution {\cite[Theorem~4.1 |
| `cor:deformation-functoriality` | `corollary` | `ProvedElsewhere` | 12415 | 0 | 1 | Functoriality of the modular deformation functor {\cite[Theorem~5.1 |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | `ProvedHere` | 13062 | 2 | 1 | First two weights |
| `lem:shadow-bracket-well-defined` | `lemma` | `ProvedHere` | 13920 | 0 | 0 | Well-definedness of the descended bracket |
| `thm:ds-complementarity-tower-main` | `theorem` | `ProvedHere` | 14152 | 1 | 0 | DS complementarity tower |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | `ProvedHere` | 14957 | 1 | 0 | Stable-graph pronilpotent completion |
| `thm:finite-rank-spectral-reduction` | `theorem` | `ProvedHere` | 15008 | 3 | 0 | Finite-rank spectral reduction |
| `cor:metaplectic-square-root` | `corollary` | `ProvedHere` | 15415 | 2 | 0 | Determinantal half-density |
| `prop:critical-locus-complementarity` | `proposition` | `ProvedHere` | 16175 | 1 | 0 | Critical-locus form of complementarity |
| `lem:graph-sum-truncation` | `lemma` | `ProvedHere` | 16654 | 3 | 0 | Graph-sum truncation criterion |
| `prop:shadow-coefficient-rationality` | `proposition` | `ProvedHere` | 17898 | 0 | 0 | Shadow coefficient rationality |
| `cor:shadow-depth-koszul-invariance` | `corollary` | `ProvedHere` | 18569 | 1 | 0 | Shadow depth under Koszul duality |
| `lem:depth-three-impossible` | `lemma` | `ProvedHere` | 19108 | 1 | 0 | Impossibility of $d_{\mathrm{alg}} = 3$ |
| `prop:hankel-extraction` | `proposition` | `ProvedHere` | 19414 | 1 | 0 | Hankel extraction of the quartic contact invariant |
| `cor:signed-shadow-measure` | `corollary` | `ProvedHere` | 19565 | 2 | 0 | Universal signed measure |
| `thm:shadow-epstein-zeta` | `theorem` | `ProvedHere` | 19647 | 2 | 2 | The Epstein zeta function of the shadow metric |
| `prop:t-line-autonomy` | `proposition` | `ProvedHere` | 21152 | 1 | 0 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | `ProvedHere` | 21209 | 2 | 0 | Inter-channel coupling on sublines |
| `cor:virasoro-shadow-radius` | `corollary` | `ProvedHere` | 21576 | 2 | 0 | Virasoro shadow growth rate |
| `prop:critical-cubic-convergence` | `proposition` | `ProvedHere` | 22056 | 3 | 0 | Critical cubic convergence threshold |
| `prop:virasoro-bottleneck` | `proposition` | `ProvedHere` | 22145 | 1 | 0 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | `ProvedHere` | 22372 | 1 | 0 | Koszul exchange of shadow regimes |
| `prop:koszul-conductor-wn` | `proposition` | `ProvedHere` | 22449 | 1 | 0 | Koszul conductor of \texorpdfstring{$\cW_N$}{WN} |
| `prop:propagator-universality` | `proposition` | `ProvedHere` | 22593 | 3 | 0 | Propagator universality |
| `cor:analytic-shadow-realization` | `corollary` | `ProvedHere` | 23575 | 2 | 0 | Analytic shadow realization |
| `rem:delta-f2-graph-decomposition` | `remark` | `ProvedHere` | 25110 | 1 | 0 | $\delta F_2$ graph-stratum decomposition |
| `comp:w3-genus3-cross` | `computation` | `ProvedHere` | 25166 | 2 | 0 | $\cW_3$ genus-$3$ cross-channel |
| `comp:w3-genus4-cross` | `computation` | `ProvedHere` | 25241 | 0 | 0 | $\cW_3$ genus-$4$ cross-channel |
| `comp:w4-full-ope-cross` | `computation` | `ProvedHere` | 25340 | 4 | 1 | $\cW_4$ full-OPE cross-channel correction |
| `rem:w4-irrational-cross-channel` | `remark` | `ProvedHere` | 25485 | 4 | 1 | $\cW_4$: the first irrational cross-channel correction |
| `comp:w5-full-ope-cross` | `computation` | `ProvedHere` | 25517 | 5 | 0 | $\cW_5$ full-OPE cross-channel correction |
| `prop:universal-gravitational-cross-channel` | `proposition` | `ProvedHere` | 25754 | 1 | 0 | Universal gravitational cross-channel formula for~$\cW_N$ |
| `rem:large-n-delta-f2-planar` | `remark` | `ProvedHere` | 26021 | 1 | 0 | Large-$N$ and 't~Hooft limit of $\delta F_2$ |
| `prop:cross-channel-growth` | `proposition` | `ProvedHere` | 26143 | 0 | 0 | Cross-channel growth |
| `prop:self-loop-vanishing` | `proposition` | `ProvedHere` | 27064 | 0 | 0 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | `ProvedHere` | 27100 | 1 | 0 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | `ProvedHere` | 27278 | 1 | 0 | Genus-$1$ two-point function from MC |
| `prop:dressed-propagator-resolution` | `proposition` | `ProvedHere` | 27653 | 1 | 0 | Dressed propagator coefficient and symmetry |
| `thm:pixton-mc-genus2` | `theorem` | `ProvedHere` | 28204 | 2 | 0 | Pixton--MC bridge at genus~$2$ |
| `thm:pixton-mc-genus3` | `theorem` | `ProvedHere` | 28267 | 3 | 0 | Pixton--MC bridge at genus~$3$ |
| `prop:mumford-from-mc-explicit` | `proposition` | `ProvedHere` | 28342 | 1 | 0 | Mumford formula from MC |
| `thm:spectral-curve-from-shadow` | `theorem` | `ProvedHere` | 28397 | 1 | 0 | Spectral curve from shadow metric |
| `thm:genus4-stable-graph-census` | `theorem` | `ProvedHere` | 28471 | 0 | 0 | Genus-$4$ stable graph census |
| `thm:genus4-free-energy` | `theorem` | `ProvedHere` | 28500 | 1 | 0 | Genus-$4$ free energy |
| `prop:genus4-spectral-sequence` | `proposition` | `ProvedHere` | 28521 | 0 | 0 | Genus-$4$ spectral sequence |
| `thm:bar-macmahon` | `theorem` | `ProvedHere` | 28570 | 0 | 0 | Bar--MacMahon correspondence |
| `prop:conifold-dt-gv` | `proposition` | `ProvedHere` | 28597 | 0 | 0 | Conifold DT and GV |
| `prop:tropical-shadow-amplitudes` | `proposition` | `ProvedHere` | 28648 | 0 | 0 | Tropical shadow amplitudes |
| `prop:tropical-period-theta` | `proposition` | `ProvedHere` | 28671 | 0 | 0 | Tropical theta function |
| `prop:fp-genus-decay-for-double` | `proposition` | `ProvedHere` | 28732 | 1 | 0 | Faber--Pandharipande genus decay |
| `prop:shadow-schwarzian` | `proposition` | `ProvedHere` | 29681 | 2 | 0 | Spectral Schr\"odinger potential |
| `cor:shadow-schrodinger-singularities` | `corollary` | `ProvedHere` | 29718 | 1 | 0 | Singularity classification |
| `prop:shadow-voros-classical` | `proposition` | `ProvedHere` | 29860 | 0 | 0 | Classical Voros period |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | `ProvedHere` | 30146 | 2 | 1 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:finite-jet-rigidity` | `proposition` | `ProvedHere` | 30226 | 1 | 0 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | `ProvedHere` | 30249 | 1 | 0 | Polynomial level dependence |
| `thm:cubic-gauge-triviality` | `theorem` | `ProvedHere` | 30396 | 1 | 0 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | `ProvedHere` | 30504 | 1 | 0 | Independent sum factorization |
| `prop:symn-kappa-linearity` | `proposition` | `ProvedHere` | 30562 | 3 | 2 | Symmetric orbifold kappa linearity |
| `rem:symmetric-orbifold-kappa` | `remark` | `ProvedHere` | 30643 | 2 | 1 | Symmetric orbifold kappa: four independent derivations |
| `prop:genus0-curve-independence` | `proposition` | `ProvedHere` | 31333 | 1 | 0 | Genus-$0$ curve-independence |
| `prop:chriss-ginzburg-structure` | `proposition` | `ProvedHere` | 32837 | 2 | 0 | MC structure principle |
| `thm:convolution-d-squared-zero` | `theorem` | `ProvedHere` | 33446 | 1 | 0 | Square-zero: convolution level |
| `cor:genus-base-cases` | `corollary` | `ProvedHere` | 33763 | 0 | 0 | Base cases |
| `prop:2d-convergence` | `proposition` | `ProvedHere` | 34313 | 0 | 2 | Two-dimensional convergence |
| `prop:verlinde-from-ordered` | `proposition` | `ProvedElsewhere` | 34482 | 2 | 6 | Verlinde formula from ordered chiral homology |
| `rem:verlinde-from-ordered-scope` | `remark` | `ProvedElsewhere` | 34657 | 6 | 4 | Scope of \protect\ref{prop:verlinde-from-ordered}: what is proved elsewhere, what is conditional |
| `thm:verlinde-polynomial-family` | `theorem` | `ProvedHere` | 34925 | 2 | 0 | Verlinde polynomial family |
| `prop:g2-degree0` | `proposition` | `ProvedHere` | 35286 | 0 | 0 | Degree-$0$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree1` | `proposition` | `ProvedHere` | 35340 | 1 | 0 | Degree-$1$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree2` | `proposition` | `ProvedHere` | 35670 | 1 | 0 | Degree-$2$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-conformal-block-degree` | `proposition` | `ProvedHere` | 35767 | 2 | 0 | Genus-$2$ conformal block decomposition by degree |
| `prop:genus-g-euler-general` | `proposition` | `ProvedHere` | 35828 | 2 | 0 | Euler characteristic of degree-$2$ KZB local systems: general rank and genus |
| `prop:g2-euler-n` | `proposition` | `ProvedHere` | 35922 | 2 | 0 | Euler characteristic at low degrees, genus~$2$ |
| `prop:g2-nonsep-degen` | `proposition` | `ProvedHere` | 36140 | 6 | 0 | Non-separating degeneration: $\Sigma_2 \to E_\tau$ |
| `prop:g2-sep-degen` | `proposition` | `ProvedHere` | 36253 | 3 | 1 | Separating degeneration: $\Sigma_2 \to E_\tau \cup E_{\tau'}$ |
| `thm:determinantal-branch-formula` | `theorem` | `ProvedHere` | 36636 | 0 | 0 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | `ProvedHere` | 36672 | 0 | 0 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | `ProvedHere` | 36703 | 0 | 0 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | `ProvedHere` | 36767 | 3 | 0 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | `ProvedHere` | 36803 | 0 | 0 | The frontier is cubic |
| `thm:hgmk-abar3-bar-cobar-scope` | `theorem` | `ProvedElsewhere` | 37378 | 4 | 3 | Genus-$3$ bar--cobar scope and the hexachotomy $\to$ hexa-unipotent extension |
| `thm:hgmk-abar4-bar-cobar-scope` | `theorem` | `ProvedHere` | 37741 | 6 | 9 | Genus-$4$ bar--cobar scope: Schottky stratum as a new stratum class; deca-unipotent Malcev closure |
| `cor:hgmk-abar4-twenty-stratum` | `corollary` | `ProvedHere` | 37902 | 2 | 2 | Genus-$4$ octachotomy analogue: the twenty-stratum ambient tower on $\AbarFour$ |
| `thm:hgmk-abar5-bar-cobar-scope` | `theorem` | `ProvedHere` | 38117 | 5 | 12 | Genus-$5$ bar--cobar scope: Andreotti--Mayer codim-$3$ Jacobian locus meets the tri-unipotent NL-intersection; pentadeca-unipotent Malcev closure |
| `cor:hgmk-abar5-twentyeight-stratum` | `corollary` | `ProvedHere` | 38292 | 0 | 1 | Genus-$5$ octachotomy analogue: the twenty-eight-stratum ambient tower on $\AbarFive$ |
| `thm:hgmk-abar6-bar-cobar-scope` | `theorem` | `ProvedHere` | 38630 | 1 | 9 | Bar--cobar scope on $\AbarSix$: unconditional $21$-unipotent Malcev ladder with hexa-unipotent Andreotti--Mayer rung |
| `thm:hgmk-am-tightness-ladder-saturation` | `theorem` | `ProvedHere` | 40466 | 2 | 9 | AM tightness $\Rightarrow$ saturation of the mixed ladder at every $g\geq 6$ |
| `cor:hgmk-am-tight-iff-ladder-sat-2g-1` | `corollary` | `ProvedHere` | 40561 | 1 | 1 | AM tightness $\Leftrightarrow k_{\max}(g)$-ladder saturation at every $k\leq 2g-1$ |
| `thm:hgmk-bv-implies-am-tightness` | `theorem` | `ProvedHere` | 40647 | 1 | 3 | Beauville--Voisin for $\mathrm{Hilb}^{g-1}(K3)$ $\Rightarrow \AMtightG$ via Ciliberto--van~der~Geer |
| `thm:hgmk-am-tightness-g9-conditional` | `theorem` | `ProvedHere` | 40804 | 1 | 7 | Andreotti--Mayer tightness at $g=9$ from Beauville--Voisin at $S^{[8 |

#### `chapters/theory/higher_kummer_arithmetic_duality_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:higher-kummer-z-g-presence` | `theorem` | `ProvedHere` | 71 | 2 | 0 | Kummer-irregular primes witnessed on the $Z_g$ side |
| `thm:higher-kummer-s-r-absence-through-r-13` | `theorem` | `ProvedHere` | 180 | 6 | 0 | Higher Kummer-irregular primes absent from $S_r(\Vir_c)$ through $r = 13$ |
| `thm:higher-kummer-refined-duality` | `theorem` | `ProvedHere` | 312 | 3 | 0 | Refined $Z_g \leftrightarrow S_r$ arithmetic duality through $r = 13$ |

#### `chapters/theory/hochschild_cohomology.tex` (20)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:hochschild-classical-comparison` | `theorem` | `ProvedElsewhere` | 187 | 0 | 1 | Comparison with classical theory {\cite{BD04}} |
| `thm:bar-spectral-sequence-hochschild` | `theorem` | `ProvedElsewhere` | 512 | 0 | 2 | Bar spectral sequence {\cite{BD04,CG17}} |
| `thm:hochschild-chain-complex` | `theorem` | `ProvedHere` | 648 | 1 | 1 | Chiral Hochschild chain model is a chain complex |
| `lem:cyclic-commutes` | `lemma` | `ProvedHere` | 728 | 0 | 0 | Cyclic operator commutes with the chiral Hochschild differential |
| `thm:connes-exact-sequence` | `theorem` | `ProvedElsewhere` | 760 | 0 | 2 | Connes mixed-complex structure {\cite{Connes85,Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:776` | `remark` | `ProvedElsewhere` | 776 | 0 | 2 | Provenance and citation |
| `cor:connes-SBI` | `corollary` | `ProvedElsewhere` | 783 | 0 | 2 | Connes SBI exact sequence {\cite{Connes85,Loday98}} |
| `thm:HC-spectral-sequence` | `theorem` | `ProvedElsewhere` | 792 | 0 | 2 | Chiral Hochschild-cyclic spectral sequence {\cite{Connes85,Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:805` | `remark` | `ProvedElsewhere` | 805 | 0 | 2 | Provenance and citation |
| `thm:E2-page-formula` | `theorem` | `ProvedElsewhere` | 814 | 0 | 1 | Second-page formula {\cite{Loday98}} |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:828` | `remark` | `ProvedElsewhere` | 828 | 0 | 1 | Provenance and citation |
| `prop:morita-equivalence-compact-gen` | `proposition` | `ProvedElsewhere` | 1153 | 0 | 3 | Morita equivalence {\cite{Keller06,Toen07}} |
| `prop:endofunctor-bimodule` | `proposition` | `ProvedElsewhere` | 1228 | 0 | 2 | Endofunctor--bimodule equivalence {\cite{Toen07,BZFN10}} |
| `thm:derived-center-hochschild` | `theorem` | `ProvedHere` | 1278 | 4 | 0 | Derived center $=$ categorical Hochschild cohomology $=$ algebraic Hochschild cochains via a compact generator |
| `thm:morita-invariance-HH` | `theorem` | `ProvedHere` | 1369 | 1 | 0 | Morita invariance of algebraic Hochschild cohomology |
| `prop:explicit-morita-transfer` | `proposition` | `ProvedHere` | 1401 | 0 | 0 | Explicit Morita transfer |
| `thm:excision` | `theorem` | `ProvedElsewhere` | 1574 | 0 | 1 | Excision; {\cite[Theorem~3.18 |
| `thm:circle-fh-hochschild` | `theorem` | `ProvedHere` | 1592 | 2 | 0 | Factorization homology on $S^1$ $=$ algebraic Hochschild chains |
| `prop:monodromy-standard` | `proposition` | `ProvedHere` | 1752 | 0 | 0 | Monodromy for standard families |
| `thm:hpd-obstruction-k3e-relative-replacement` | `theorem` | `ProvedHere` | 2567 | 3 | 0 | Fano obstruction to absolute HPD on~$\mathrm{K3}\times E$; relative-HPD replacement over~$E$ |

#### `chapters/theory/infinite_fingerprint_classification.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:quadrichotomy-is-coarse-projection` | `theorem` | `ProvedHere` | 599 | 2 | 0 | Quadrichotomy is a coarse projection; strengthening of Proposition~\ref{prop:coarse-projection-functor} |
| `thm:DS-fingerprint-transport` | `theorem` | `ProvedHere` | 695 | 1 | 7 | DS transport of the fingerprint; closes FM\textup{108} |
| `cor:fingerprint-separates-landscape` | `corollary` | `ProvedHere` | 846 | 3 | 0 | Completeness on the standard landscape |
| `thm:schellekens-structured-subset` | `theorem` | `ProvedHere` | 878 | 1 | 0 | Structured-subset derivation of the holomorphic \texorpdfstring{$c=24$}{c=24} census; closes AP\textup{290} |
| `prop:schellekens-weight-two-threshold` | `proposition` | `ProvedHere` | 1065 | 4 | 0 | Uniform weight-two threshold across the three holomorphic \texorpdfstring{$c=24$}{c=24} machineries |

#### `chapters/theory/kappa_conductor.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:conductor-trinity` | `theorem` | `ProvedHere` | 113 | 7 | 0 | Scalar-conductor comparison |
| `thm:platonic-conductor` | `theorem` | `ProvedHere` | 181 | 2 | 0 | Canonical ghost scalar |

#### `chapters/theory/koszul_pair_structure.tex` (28)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:kps-scalar-verdier-sums` | `proposition` | `ProvedHere` | 195 | 3 | 0 | Scalar Verdier sums on the finite-type lane |
| `lem:chiral-enveloping-well-defined` | `lemma` | `ProvedHere` | 361 | 0 | 0 | Well-definedness of the chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | `ProvedHere` | 411 | 1 | 0 | Relative exactness of the two-sided chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | `ProvedHere` | 491 | 1 | 0 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | `ProvedHere` | 517 | 1 | 0 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | `ProvedHere` | 594 | 1 | 0 | Properties of cup product |
| `thm:chiral-gerstenhaber-kps` | `theorem` | `ProvedElsewhere` | 637 | 0 | 3 | Chiral Gerstenhaber algebra {\cite{Ger63, Tamarkin00}} |
| `thm:ainfty-chiral-hochschild` | `theorem` | `ProvedHere` | 671 | 2 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} operations from the chiral brace model |
| `thm:linfty-chiral-hochschild` | `theorem` | `ProvedElsewhere` | 721 | 0 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} structure {\cite{LV12}} |
| `prop:admissible-levels-permuted` | `proposition` | `ProvedHere` | 1138 | 0 | 1 | Numerical admissible data under the level reflection |
| `thm:mc-quadratic` | `theorem` | `ProvedHere` | 1233 | 0 | 0 | Maurer--Cartan correspondence, quadratic case |
| `thm:chiral-yangian-km` | `theorem` | `ProvedHere` | 1325 | 0 | 0 | Affine Kac--Moody as chiral algebra |
| `thm:chiral-yangian` | `theorem` | `ProvedElsewhere` | 1348 | 0 | 2 | Critical centre and Yangian deformation data {\cite{Drinfeld85,Feigin-Frenkel}} |
| `thm:feigin-frenkel-bar` | `theorem` | `ProvedElsewhere` | 1458 | 0 | 1 | Feigin--Frenkel centre {\cite{FF}} |
| `thm:w-algebra-sl4` | `theorem` | `ProvedElsewhere` | 1534 | 0 | 1 | Structure of \texorpdfstring{$\mathcal{W}(\mathfrak{sl}_4, e_{subreg})$}{W(sl4, e\_subreg)} {\cite{KRW}} |
| `thm:ff-s-duality` | `theorem` | `ProvedElsewhere` | 1542 | 0 | 1 | Feigin--Frenkel duality as S-duality, principal simply-laced case |
| `thm:koszul-equivalence-categories` | `theorem` | `ProvedElsewhere` | 1597 | 0 | 1 | Koszul equivalence of categories {\cite{BGS96}} |
| `thm:linf-mc-flatness` | `theorem` | `ProvedHere` | 1864 | 1 | 1 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan equation from a transferred \texorpdfstring{$A_\infty$}{A-infinity} model |
| `thm:ordered-shuffle` | `theorem` | `ProvedHere` | 2222 | 1 | 0 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | `ProvedHere` | 2264 | 0 | 0 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | `ProvedHere` | 2294 | 2 | 0 | Enveloping duality |
| `thm:ordered-bimod-bicomod` | `theorem` | `ProvedHere` | 2336 | 3 | 0 | Bimodule--bicomodule equivalence |
| `thm:ordered-diagonal` | `theorem` | `ProvedHere` | 2369 | 1 | 0 | Diagonal correspondence |
| `thm:ordered-HH-coHH-homology` | `theorem` | `ProvedHere` | 2417 | 2 | 0 | chiral Hochschild--coHochschild duality, homological version |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | `ProvedHere` | 2448 | 1 | 0 | chiral Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-pair-of-pants` | `theorem` | `ProvedHere` | 2498 | 1 | 0 | Ordered pair-of-pants algebra |
| `thm:ordered-master` | `theorem` | `ProvedHere` | 2522 | 4 | 0 | Master theorem: the ordered open trace formalism |
| `thm:ordered-FG-shadow` | `theorem` | `ProvedElsewhere` | 2613 | 0 | 1 | Commutator-shadow theorem |

#### `chapters/theory/koszulness_moduli_scheme.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `v1-thm:kms-moduli` | `theorem` | `ProvedHere` | 249 | 11 | 4 | Koszulness moduli, finite-stage representability |
| `v1-cor:kms-grt-invariant` | `corollary` | `ProvedHere` | 459 | 3 | 0 | Associator-independence of the Koszulness property |
| `v1-thm:kms-fourteen-unconditional` | `theorem` | `ProvedHere` | 511 | 10 | 0 | Fourteen admissible characterisations on their home chart |
| `v1-prop:kms-at-chart` | `proposition` | `ProvedHere` | 659 | 2 | 1 | Alekseev--Torossian chart |
| `v1-prop:kms-hodge-betti-chart` | `proposition` | `ProvedHere` | 753 | 2 | 3 | Hodge--Betti chart |
| `v1-prop:kms-elliptic-chart` | `proposition` | `ProvedHere` | 808 | 2 | 1 | Enriquez elliptic chart |
| `v1-prop:kms-kontsevich-chart` | `proposition` | `ProvedHere` | 862 | 3 | 1 | Kontsevich integral chart |
| `v1-thm:kms-koszulness-is-grt-invariant` | `theorem` | `ProvedHere` | 930 | 5 | 2 | Koszulness is $\mathrm{GRT}_1$-invariant; admissible characterisations are charts |
| `v1-thm:kms-virasoro-noncircular` | `theorem` | `ProvedHere` | 966 | 0 | 4 | Virasoro Koszulness, non-circular |
| `v1-thm:kms-yangian-embedding` | `theorem` | `ProvedHere` | 1070 | 3 | 3 | Yangian chart inclusion |
| `v1-cor:kms-exceptional-PBW` | `corollary` | `ProvedElsewhere` | 1130 | 1 | 1 | Exceptional-type Yangian PBW via GRW18 |
| `v1-thm:kms-meta-koszulness` | `theorem` | `ProvedHere` | 1169 | 2 | 1 | Meta-Koszulness |
| `rem:kms-K3-placement` | `remark` | `ProvedHere` | 1363 | 4 | 0 | K3 chart placement on the Koszulness moduli object |
| `rem:kms-grt-transport-312` | `remark` | `ProvedHere` | 1397 | 3 | 0 | $\mathrm{GRT}_1$-transport of the K3 central charge |
| `rem:kms-humbert-cocycle` | `remark` | `ProvedHere` | 1424 | 0 | 0 | Humbert-$H_1$ monodromy as K3 chart-compatibility data |

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

#### `chapters/theory/mc5_class_m_chain_level_platonic.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:curve-H20-vanishing` | `lemma` | `ProvedElsewhere` | 759 | 0 | 0 | Curve-fibre Hodge dimension |
| `prop:central-m0-vacuum-proportionality` | `proposition` | `ProvedHere` | 785 | 0 | 0 | Sub-argument (b): vacuum-proportionality uniqueness of the central degree-2 curvature |
| `lem:sl2-sl2-splitting` | `lemma` | `ProvedElsewhere` | 1012 | 1 | 3 | $SL_2\times SL_2$ splitting of the bi-filtration |
| `thm:mc5-wall-of-walls-strict-chain-level` | `theorem` | `ProvedHere` | 1052 | 5 | 8 | Strict chain-level bar-cobar inversion on the wall-of-walls in the Deligne--Malcev bi-unipotent pro-ambient |
| `cor:global-strict-bar-cobar-humbert-stratum` | `corollary` | `ProvedHere` | 1272 | 5 | 3 | Global strict chain-level bar-cobar inversion across the full Humbert stratum |
| `lem:sl2-admissible-splitting` | `lemma` | `ProvedElsewhere` | 1557 | 0 | 3 | $\mathfrak{sl}_2^{\oplus\mathrm{adm}}$ splitting of the Malcev ladder |
| `thm:mc5-admissible-heegner-strict-chain-level` | `theorem` | `ProvedHere` | 1599 | 5 | 7 | Strict chain-level bar-cobar inversion on the admissible Heegner union in the bi-unipotent Malcev ladder |
| `cor:global-strict-admissible-heegner` | `corollary` | `ProvedHere` | 1791 | 5 | 4 | Global chain-level bar-cobar inversion on the full admissible Heegner locus |
| `thm:codim3-heegner-transversality` | `theorem` | `ProvedHere` | 1988 | 2 | 4 | Codim-$3$ Heegner transversality on $\overline{\mathcal A_2}$ |
| `thm:codim4-admissible-heegner-emptiness` | `theorem` | `ProvedHere` | 2133 | 1 | 6 | Codim-$4$ admissible Heegner emptiness on $\overline{\mathcal A_2}$ |
| `cor:octachotomy-chain-level-ambient-tower` | `corollary` | `ProvedHere` | 2300 | 2 | 0 | Octachotomy closure of the chain-level ambient tower |
| `thm:universal-k-tower-malcev-closure` | `theorem` | `ProvedHere` | 2340 | 4 | 6 | Universal $k$-tower Malcev closure on $\overline{\mathcal A_g}$ |
| `thm:mc5-infty-one-obstruction-tower` | `theorem` | `ProvedHere` | 2600 | 0 | 3 | $(\infty,1)$-bar--cobar inversion on $\Perf(\AbarTwo)$: the obstruction tower |
| `thm:mc5-bridgeland-slicing-reads-obstruction-tower` | `theorem` | `ProvedHere` | 2649 | 3 | 4 | Bridgeland slicing reads the obstruction tower |
| `thm:mc5-compatibility-square` | `theorem` | `ProvedHere` | 2739 | 3 | 3 | Chain-level $\leftrightarrow$ $(\infty,1)$-categorical compatibility square |
| `thm:compat-data-torsor-uniqueness` | `theorem` | `ProvedHere` | 2922 | 4 | 8 | Uniqueness of the compatibility homotopy up to contractible choice |
| `thm:mc5-infty-two-adjunction` | `theorem` | `ProvedHere` | 3218 | 4 | 5 | $(\infty,2)$-adjunction $\Om\dashv\Bch$ with triangular 2-cell structure |

#### `chapters/theory/mc5_genus0_genus1_wall_platonic.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:mc5-g0g1-wall-five-point-sewing` | `theorem` | `ProvedHere` | 166 | 4 | 0 | MC5 5-point sewing at the genus-0/genus-1 wall |
| `cor:mc5-g0g1-heisenberg-elliptic-function` | `corollary` | `ProvedHere` | 505 | 3 | 0 | Heisenberg elliptic function at the wall |
| `cor:mc5-g0g1-k3-elliptic-genus` | `corollary` | `ProvedHere` | 586 | 2 | 1 | K3 elliptic genus at the wall |

#### `chapters/theory/motivic_shadow_full_class_m_platonic.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:shadow-tower-depth-1-rationality` | `theorem` | `ProvedHere` | 80 | 2 | 0 | \label{thm:shadow-tower-depth-1-rationality}Shadow residues are depth-$1$ Arnold data |
| `thm:e1-vs-e2-mzv-depth-distinction` | `theorem` | `ProvedHere` | 152 | 1 | 0 | \label{thm:e1-vs-e2-mzv-depth-distinction} $E_1$-chiral residue vs $E_2$-topological iterated integral |
| `thm:w-n-motivic-rationality-all-r` | `theorem` | `ProvedHere` | 229 | 2 | 0 | \label{thm:w-n-motivic-rationality-all-r}Principal $\cW_N$ motivic rationality in all weights |
| `prop:w3-w-line-motivic-rationality` | `proposition` | `ProvedHere` | 271 | 0 | 0 | \label{prop:w3-w-line-motivic-rationality} $\cW_3$ W-line explicit rationality |
| `thm:bp-motivic-rationality-arakawa` | `theorem` | `ProvedHere` | 320 | 1 | 0 | \label{thm:bp-motivic-rationality-arakawa}BP motivic rationality in Arakawa convention |
| `prop:bp-fl-convention-caveat` | `proposition` | `ProvedHere` | 369 | 1 | 0 | \label{prop:bp-fl-convention-caveat}FL-convention Koszul conductor: distinct constant |
| `thm:w-infty-motivic-rationality-all-r` | `theorem` | `ProvedHere` | 435 | 2 | 0 | \label{thm:w-infty-motivic-rationality-all-r} $\cW_{\infty}$ motivic rationality |
| `thm:class-m-motivic-rationality-full` | `theorem` | `ProvedHere` | 496 | 5 | 0 | \label{thm:class-m-motivic-rationality-full} Class M motivic rationality |

#### `chapters/theory/motivic_shadow_tower.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:shadow-tower-motivic-lift` | `theorem` | `ProvedHere` | 218 | 0 | 0 | \label{thm:shadow-tower-motivic-lift}Motivic lift of Arnold-period shadow coefficients |
| `thm:grt-motivic-coaction` | `theorem` | `ProvedHere` | 301 | 0 | 0 | \label{thm:grt-motivic-coaction}GRT motivic coaction on the shadow-period subspace |
| `prop:s4-vir-mot` | `proposition` | `ProvedHere` | 374 | 0 | 0 | \label{prop:s4-vir-mot}Motivic lift of $S_4(\Vir_c)$ |
| `prop:s5-vir-mot` | `proposition` | `ProvedHere` | 413 | 0 | 0 | \label{prop:s5-vir-mot}Motivic lift of $S_5(\Vir_c)$ |
| `thm:virasoro-motivic-rationality-all-r` | `theorem` | `ProvedHere` | 517 | 1 | 0 | \label{thm:virasoro-motivic-rationality-all-r}Virasoro motivic rationality: weighted tower and manuscript boundary |
| `rem:characteristic-primes-are-riccati-arithmetic` | `remark` | `ProvedHere` | 683 | 0 | 0 | \label{rem:characteristic-primes-are-riccati-arithmetic}Characteristic primes of the shadow tower are Riccati-recurrence integers |
| `cor:shadow-L-pole` | `corollary` | `ProvedHere` | 763 | 3 | 0 | \label{cor:shadow-L-pole}Motivic weight obstruction for the shadow $L$-function |
| `thm:kappa-vs-beta-split` | `theorem` | `ProvedHere` | 811 | 0 | 0 | \label{thm:kappa-vs-beta-split}Motivic kappa, modular beta |

#### `chapters/theory/nilpotent_completion.tex` (17)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:geom-conilpotent` | `proposition` | `ProvedHere` | 118 | 1 | 0 | Collision trees and coradical degree |
| `thm:completion-convergence` | `theorem` | `ProvedHere` | 146 | 2 | 0 | Finite-window convergence |
| `thm:completed-bar-cobar` | `theorem` | `ProvedHere` | 261 | 1 | 0 | Completed finite-window bar--cobar inversion |
| `thm:koszul-dual-characterization` | `theorem` | `ProvedHere` | 311 | 3 | 0 | Essential image of finite-window bar towers |
| `thm:BD-chiral-homology` | `theorem` | `ProvedElsewhere` | 389 | 0 | 1 | BD chiral homology \cite{BD04} |
| `prop:practical-convergence` | `proposition` | `ProvedHere` | 515 | 0 | 0 | Weight-window convergence |
| `thm:CG-renorm` | `theorem` | `ProvedElsewhere` | 539 | 0 | 1 | Costello--Gwilliam renormalization \cite{CG17} |
| `thm:stabilized-completion-positive` | `theorem` | `ProvedHere` | 635 | 0 | 0 | Stabilized completion for positive towers |
| `thm:resonance-filtered-bar-cobar` | `theorem` | `ProvedHere` | 746 | 1 | 0 | Resonance-filtered completed bar/cobar |
| `prop:resonance-ss-degeneration` | `proposition` | `ProvedHere` | 852 | 1 | 0 | Resonance spectral sequence degeneration |
| `prop:resonance-ranks-standard` | `proposition` | `ProvedHere` | 879 | 2 | 0 | Resonance ranks of the standard families |
| `cor:virasoro-resonance-ss` | `corollary` | `ProvedHere` | 950 | 1 | 0 | Virasoro resonance spectral sequence |
| `thm:platonic-completion` | `theorem` | `ProvedHere` | 1022 | 5 | 0 | Resonance completion |
| `thm:nc-grt1-super-torsor-delta5` | `theorem` | `ProvedHere` | 2020 | 4 | 0 | $\mathrm{GRT}_1^{\mathrm{super}}$-torsor structure on super-EK quantisations of $\mathfrak g_{\Delta_5}$ |
| `cor:nc-h-delta5-unique-up-to-grt1` | `corollary` | `ProvedHere` | 2170 | 2 | 0 | Uniqueness of $\mathbf H_{\Delta_5}$ up to $\mathrm{GRT}_1^{\mathrm{super}}$ |
| `prop:nc-massey-triple-rrr-E8` | `proposition` | `ProvedHere` | 2437 | 0 | 4 | Associator-free chain-level triple Massey product |
| `prop:nc-delta-n-explicit-higher` | `proposition` | `ProvedHere` | 2804 | 3 | 2 | Explicit recurrence for $\delta^{(n)}$ at $n \ge 7$ |

#### `chapters/theory/ordered_associative_chiral_kd.tex` (110)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:bicom-e` | `lemma` | `ProvedHere` | 235 | 0 | 0 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | `ProvedHere` | 319 | 0 | 0 | Ordered chiral shuffle theorem |
| `prop:r-matrix-descent-vol1` | `proposition` | `ProvedHere` | 585 | 4 | 0 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | `ProvedHere` | 731 | 5 | 0 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | `ProvedHere` | 898 | 0 | 0 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | `ProvedHere` | 939 | 1 | 0 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | `ProvedHere` | 990 | 0 | 0 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | `ProvedHere` | 1010 | 1 | 0 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | `ProvedHere` | 1077 | 0 | 0 | — |
| `prop:one-defect` | `proposition` | `ProvedHere` | 1104 | 0 | 0 | — |
| `thm:tangent=K` | `theorem` | `ProvedHere` | 1126 | 0 | 0 | Tangent identification |
| `cor:infdual` | `corollary` | `ProvedHere` | 1163 | 2 | 0 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | `ProvedHere` | 1195 | 2 | 0 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | `ProvedHere` | 1247 | 3 | 0 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | `ProvedHere` | 1280 | 1 | 0 | Diagonal correspondence |
| `cor:unit` | `corollary` | `ProvedHere` | 1328 | 2 | 0 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | `ProvedHere` | 1346 | 1 | 0 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | `ProvedHere` | 1382 | 2 | 0 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | `ProvedHere` | 1414 | 1 | 0 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | `ProvedHere` | 1440 | 1 | 0 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | `ProvedHere` | 1465 | 1 | 0 | Cap action |
| `thm:pair-of-pants` | `theorem` | `ProvedHere` | 1528 | 1 | 0 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | `ProvedHere` | 1566 | 4 | 0 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | `ProvedHere` | 1620 | 1 | 0 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | `ProvedHere` | 1669 | 2 | 0 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | `ProvedHere` | 1699 | 12 | 0 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | `ProvedHere` | 1817 | 0 | 0 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | `ProvedHere` | 2306 | 1 | 0 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | `ProvedHere` | 2421 | 0 | 0 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | `ProvedHere` | 2502 | 0 | 0 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | `ProvedHere` | 2561 | 0 | 0 | Formality: class~G, shadow depth~$2$ |
| `thm:drinfeld-yangian-sl2` | `theorem` | `ProvedHere` | 2700 | 6 | 0 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | `ProvedHere` | 2790 | 0 | 0 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | `ProvedHere` | 2826 | 3 | 0 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | `ProvedHere` | 2878 | 3 | 0 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | `ProvedHere` | 2919 | 7 | 0 | Classical limit |
| `thm:central-extension-invisible` | `theorem` | `ProvedHere` | 3010 | 0 | 0 | Central extension is invisible to the ordered double bar |
| `thm:two-colour-double-kd` | `theorem` | `ProvedHere` | 3085 | 1 | 0 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | `ProvedHere` | 3111 | 2 | 0 | Non-redundancy of the two colours |
| `prop:vir-collision-residue` | `proposition` | `ProvedHere` | 3190 | 2 | 0 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | `ProvedHere` | 3225 | 2 | 0 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | `ProvedHere` | 3254 | 0 | 0 | Gravitational Yangian collapse |
| `thm:vir-non-formality` | `theorem` | `ProvedHere` | 3321 | 0 | 0 | Virasoro non-formality |
| `prop:grav-yangian-curvature` | `proposition` | `ProvedHere` | 3387 | 1 | 0 | Gravitational Yangian curvature |
| `cor:gauge-gravity-dichotomy-ordered` | `corollary` | `ProvedHere` | 3432 | 4 | 0 | Gauge-gravity complexity dichotomy |
| `thm:grav-coproduct-primitive` | `theorem` | `ProvedHere` | 3491 | 0 | 0 | Gravitational coproduct primitivity |
| `thm:km-yangian` | `theorem` | `ProvedHere` | 3618 | 5 | 0 | Universal Kac--Moody Yangian theorem |
| `thm:root-space-one-dim-v1` | `theorem` | `ProvedHere` | 4013 | 0 | 0 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | `ProvedHere` | 4062 | 1 | 0 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | `ProvedHere` | 4128 | 0 | 0 | Dynkin coefficient via the beta integral |
| `thm:complete-strictification-v1` | `theorem` | `ProvedHere` | 4209 | 3 | 0 | Complete strictification for all simple Lie algebras |
| `thm:sl3-triangle-coefficient` | `theorem` | `ProvedHere` | 4737 | 0 | 0 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | `ProvedHere` | 4821 | 0 | 0 | Serre relations from root-space vanishing |
| `thm:sl3-rtt` | `theorem` | `ProvedHere` | 4872 | 4 | 0 | RTT presentation for $Y_\hbar(\mathfrak{sl}_3)$ from the ordered bar complex |
| `thm:sl3-strictification` | `theorem` | `ProvedHere` | 4946 | 2 | 0 | Vanishing of the spectral Drinfeld class for $\mathfrak{sl}_3$ |
| `thm:sl4-quadrilateral` | `theorem` | `ProvedHere` | 5019 | 1 | 0 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:B2-ordered-bar` | `theorem` | `ProvedHere` | 5106 | 1 | 0 | Ordered bar complexes and Yangian $R$-matrices for rank-$2$ non-$A$ types |
| `thm:annular-bar-differential` | `theorem` | `ProvedHere` | 5315 | 1 | 0 | Annular bar differential |
| `thm:annular-HH` | `theorem` | `ProvedHere` | 5408 | 3 | 0 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | `ProvedHere` | 5531 | 1 | 0 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:b-cycle-quantum-group` | `theorem` | `ProvedHere` | 5859 | 1 | 0 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | `ProvedHere` | 6116 | 2 | 0 | Drinfeld--Kohno; {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | `ProvedHere` | 6197 | 2 | 0 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | `ProvedHere` | 6271 | 0 | 0 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | `ProvedHere` | 6312 | 1 | 0 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | `ProvedHere` | 6474 | 0 | 0 | Ordered pole-depth spectrum |
| `thm:ordered-AOS` | `theorem` | `ProvedHere` | 6533 | 2 | 0 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | `ProvedHere` | 6612 | 2 | 0 | Averaging and surplus |
| `prop:ker-av-schur-weyl` | `proposition` | `ProvedHere` | 6778 | 0 | 0 | Kernel of the Reynolds projector: general simple Lie algebras |
| `thm:elliptic-spectral-dichotomy` | `theorem` | `ProvedHere` | 7032 | 3 | 0 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `thm:bg-ordered-bar` | `theorem` | `ProvedHere` | 7248 | 0 | 0 | Free-field ordered bar complexes |
| `thm:wakimoto-ordered-bar` | `theorem` | `ProvedHere` | 7326 | 1 | 0 | Wakimoto bar complex descent |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | `ProvedHere` | 7427 | 1 | 0 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | `ProvedHere` | 7493 | 1 | 0 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | `ProvedHere` | 7553 | 2 | 0 | Ordered Koszul dual of lattice algebras |
| `comp:sl2-eval` | `computation` | `ProvedHere` | 7707 | 2 | 0 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | `ProvedHere` | 7768 | 0 | 0 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | `ProvedHere` | 7816 | 1 | 0 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | `ProvedHere` | 7858 | 1 | 0 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | `ProvedHere` | 7907 | 2 | 0 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `thm:drinfeld-classification` | `theorem` | `ProvedElsewhere` | 7956 | 0 | 0 | Drinfeld classification |
| `prop:eval-drinfeld` | `proposition` | `ProvedHere` | 7979 | 0 | 0 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | `ProvedHere` | 8046 | 2 | 0 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | `ProvedHere` | 8107 | 0 | 0 | Braiding from the $R$-matrix |
| `thm:grothendieck-yangian` | `theorem` | `ProvedElsewhere` | 8152 | 0 | 0 | Grothendieck ring of Yangian modules |
| `prop:r-matrix-eigenvalue` | `proposition` | `ProvedHere` | 8214 | 0 | 0 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | `ProvedHere` | 8241 | 1 | 0 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | `ProvedHere` | 8340 | 1 | 0 | $\mathsf{E}_1$ ordered bar landscape |
| `thm:chiral-qg-equiv` | `theorem` | `ProvedHere` | 8841 | 2 | 0 | Chiral bialgebra equivalence on the Koszul locus |
| `cor:bar-encodes-all` | `corollary` | `ProvedHere` | 9045 | 1 | 0 | The ordered bar encodes all three structures |
| `thm:w-infty-chiral-qg` | `theorem` | `ProvedHere` | 9247 | 11 | 8 | $\cW_{1+\infty}\lbrack\Psi\rbrack$ as a chiral quantum group |
| `prop:w-infty-antipode-obstruction` | `proposition` | `ProvedHere` | 10039 | 4 | 0 | Yangian antipode on $\cW_{1+\infty}$: explicit formula and vertex Hopf obstruction |
| `lem:coprod-T-miura` | `lemma` | `ProvedHere` | 10204 | 1 | 1 | Miura inversion of the spectral coproduct at spin~$2$ |
| `prop:spin3-miura-coprod` | `proposition` | `ProvedHere` | 10287 | 2 | 0 | Spin-$3$ Miura coproduct |
| `thm:miura-cross-universality-monograph` | `theorem` | `ProvedHere` | 10336 | 3 | 1 | Miura cross-term universality |
| `prop:ff-screening-coproduct-obstruction` | `proposition` | `ProvedHere` | 10742 | 2 | 1 | Feigin--Frenkel screening is not chiral-coproduct-compatible on the Heisenberg parent |
| `rem:miura-ff-screening-structural-mirror` | `remark` | `ProvedHere` | 10890 | 2 | 0 | Structural mirror: the Miura cross-term and the Feigin--Frenkel screening obstruction share a single cohomological invariant |
| `thm:glN-chiral-qg` | `theorem` | `ProvedHere` | 11007 | 17 | 4 | $Y(\widehat{\mathfrak{gl}}_N)$ chiral quantum group for $N \geq 2$: unconditional at $N=2$, conditional on~\cite{JKL26} at $N \geq 3$ |
| `lem:qdet-central-all-N` | `lemma` | `ProvedElsewhere` | 11381 | 3 | 1 | Centrality of the quantum determinant at rank $N$ |
| `thm:FG-shadow-vol2` | `theorem` | `ProvedElsewhere` | 11598 | 0 | 0 | Comm\-utator-shadow theorem |
| `thm:ordered-associative-modular-mc` | `theorem` | `ProvedElsewhere` | 11685 | 0 | 0 | Associative modular Maurer--Cartan class |
| `thm:ordered-associative-ds-principal` | `theorem` | `ProvedElsewhere` | 11725 | 0 | 0 | Reduction commutes with associative chiral duality \textup{(}principal case\textup{)} |
| `thm:class-m-ds-transport` | `theorem` | `ProvedHere` | 12238 | 1 | 0 | Class~M persistence under DS transport |
| `thm:unshifted-identification` | `theorem` | `ProvedHere` | 12469 | 1 | 0 | Unshifted identification |
| `thm:factorisation-identification` | `theorem` | `ProvedHere` | 12513 | 0 | 0 | Factorisation identification on the Koszul locus |
| `prop:r-matrix-stable-envelope` | `proposition` | `ProvedHere` | 12556 | 0 | 0 | $R$-matrix comparison |
| `thm:e3-identification-km` | `theorem` | `ProvedHere` | 12617 | 1 | 0 | $\mathsf{E}_3$ identification for affine Kac--Moody |
| `prop:critical-level-ordered` | `proposition` | `ProvedHere` | 12746 | 0 | 0 | Critical level: monodromy trivialises, Koszulness fails, center jumps |
| `rem:bernard-heat-identity-zeta` | `remark` | `ProvedElsewhere` | 12953 | 2 | 2 | Bernard heat identity for the Weierstrass $\zeta$ |
| `rem:kzb-n-point-dynamical-closure` | `remark` | `ProvedElsewhere` | 13022 | 3 | 3 | $n \geq 3$ KZB flatness: Felder dynamical shift + Halphen--Ramanujan |

#### `chapters/theory/periodic_cdg_admissible.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:screening-adjoint-squares` | `lemma` | `ProvedHere` | 100 | 1 | 1 | Screening adjoints square to zero and satisfy quantum Serre |

#### `chapters/theory/poincare_duality.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:verdier-config` | `theorem` | `ProvedElsewhere` | 237 | 0 | 1 | Verdier duality for configuration spaces; {} \cite{KS90} |
| `thm:dual-differentials` | `theorem` | `ProvedHere` | 324 | 1 | 0 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | `ProvedHere` | 462 | 1 | 0 | Bar coalgebra and post-Verdier algebra |
| `thm:bar-computes-dual` | `theorem` | `ProvedHere` | 539 | 6 | 0 | Bar coalgebra, Koszul-dual coalgebra, and Verdier-dual algebra |
| `comp:bar-dual-low-degrees` | `computation` | `ProvedHere` | 643 | 0 | 0 | Degree 0 and 1 |

#### `chapters/theory/poincare_duality_quantum.tex` (21)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:defect-koszul` | `theorem` | `ProvedElsewhere` | 120 | 3 | 2 | Verdier defect and Koszul dual {\cite{LV12, Positselski11}} |
| `thm:curved-koszul` | `theorem` | `ProvedElsewhere` | 178 | 3 | 2 | Curved Koszul duality (algebraic form) {\cite{Positselski11, GLZ22}} |
| `thm:universal-defect-construction` | `theorem` | `ProvedElsewhere` | 268 | 0 | 1 | Finite-type Ext model for the defect algebra {\cite{LV12}} |
| `__unlabeled_chapters/theory/poincare_duality_quantum.tex:354` | `calculation` | `ProvedElsewhere` | 354 | 0 | 1 | Yangian structure constants {\cite{Drinfeld85}} |
| `thm:ff-center` | `theorem` | `ProvedElsewhere` | 404 | 0 | 2 | Feigin--Frenkel center {\cite{Feigin-Frenkel,BD04}} |
| `prop:bg-bar-coalg` | `proposition` | `ProvedHere` | 422 | 1 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex coalgebra |
| `thm:fact-homology-quantum` | `theorem` | `ProvedElsewhere` | 477 | 0 | 2 | Factorization homology and the bar complex {\cite{Francis2013,HA}} |
| `prop:chiral-operad-genus0` | `proposition` | `ProvedHere` | 522 | 0 | 3 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | `ProvedHere` | 566 | 5 | 3 | Prism principle: operadic identification |
| `thm:prism-higher-genus` | `theorem` | `ProvedHere` | 806 | 3 | 1 | Prism principle: higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | `ProvedHere` | 878 | 0 | 0 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | `ProvedHere` | 903 | 2 | 0 | The loop expansion is the genus expansion |
| `cor:prism-principle` | `corollary` | `ProvedHere` | 1029 | 3 | 0 | The prism principle |
| `cor:feynman-transform-involution` | `corollary` | `ProvedElsewhere` | 1073 | 0 | 1 | Feynman transform involution {\cite{GeK98}} |
| `thm:modular-convolution-structure` | `theorem` | `ProvedHere` | 1152 | 0 | 1 | dg~Lie structure |
| `thm:vol1-genus-completion` | `theorem` | `ProvedHere` | 1192 | 1 | 0 | Genus completion |
| `prop:vol1-structure-as-MC` | `proposition` | `ProvedHere` | 1240 | 2 | 0 | The algebra structure as MC element |
| `prop:log-forms-conformal-invariance` | `proposition` | `ProvedElsewhere` | 1281 | 0 | 1 | Forced by conformal invariance {\cite{BPZ84}} |
| `lem:sign-consistency-bar` | `lemma` | `ProvedElsewhere` | 1314 | 0 | 1 | Sign consistency for bar differential {\cite{LV12}} |
| `thm:bar-cobar-adjunction-operadic` | `theorem` | `ProvedElsewhere` | 1330 | 1 | 1 | Bar-cobar adjunction {\cite{LV12}} |
| `thm:partition` | `theorem` | `ProvedHere` | 1346 | 0 | 2 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:quantum-linfty-master` | `theorem` | `ProvedHere` | 748 | 4 | 0 | Quantum $L_\infty$ master equation |
| `thm:non-renormalization-tree` | `theorem` | `ProvedElsewhere` | 833 | 0 | 1 | Non-renormalization at tree level |
| `cor:exact-r-matrix` | `corollary` | `ProvedElsewhere` | 864 | 2 | 0 | Collision residue normalization for standard-family $r$-matrices |
| `prop:two-element-strict` | `proposition` | `ProvedHere` | 988 | 2 | 0 | Two-element covers are strict |
| `prop:jacobiator-nullhomotopic` | `proposition` | `ProvedElsewhere` | 1066 | 2 | 1 | Jacobiator is nullhomotopic |
| `prop:borcherds-shadow-identification` | `proposition` | `ProvedHere` | 1474 | 4 | 2 | Secondary Borcherds operations and the first shadow obstructions |

#### `chapters/theory/shadow_L_function_platonic.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:shL-convergence-half-plane` | `proposition` | `ProvedHere` | 103 | 0 | 0 | \label{prop:shL-convergence-half-plane}Formal uniqueness and analytic growth datum |
| `thm:kummer-congruence-prediction` | `theorem` | `ProvedElsewhere` | 357 | 3 | 0 | \label{thm:kummer-congruence-prediction}Bernoulli--Kummer witnesses for the genus slots |

#### `chapters/theory/shadow_tower_higher_coefficients.tex` (44)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:virasoro-shadow-recurrence` | `theorem` | `ProvedHere` | 203 | 0 | 0 | \label{thm:virasoro-shadow-recurrence}Virasoro weighted shadow recurrence |
| `thm:s6-virasoro-closed-form` | `theorem` | `ProvedHere` | 282 | 1 | 0 | \label{thm:s6-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_6(\Vir_c)$ |
| `thm:s7-virasoro-closed-form` | `theorem` | `ProvedHere` | 349 | 0 | 0 | \label{thm:s7-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_7(\Vir_c)$ |
| `thm:s8-virasoro-closed-form` | `theorem` | `ProvedHere` | 418 | 2 | 0 | \label{thm:s8-virasoro-closed-form}Closed form for $\widehat S^{\rm wt}_8(\Vir_c)$ |
| `prop:sth-boundary-checks` | `proposition` | `ProvedHere` | 542 | 3 | 0 | \label{prop:sth-boundary-checks}Weighted boundary values through weight 8 |
| `prop:sth-leading-asymp` | `proposition` | `ProvedHere` | 602 | 0 | 0 | \label{prop:sth-leading-asymp}Leading large-$c$ asymptotic coefficient for the weighted tower |
| `thm:shadow-exponential-base-Virasoro` | `theorem` | `ProvedHere` | 670 | 1 | 0 | \label{thm:shadow-exponential-base-Virasoro} The shadow-exponential base of Virasoro is $C_\Vir = 6$ |
| `thm:universal-class-M-C-is-6` | `theorem` | `ProvedHere` | 714 | 1 | 0 | \label{thm:universal-class-M-C-is-6} Universal class M shadow-exponential base |
| `prop:W3-T-line-matches-Vir-subleading` | `proposition` | `ProvedHere` | 771 | 0 | 0 | \label{prop:W3-T-line-matches-Vir-subleading} $\cW_3$ $T$-line subleading asymptotic matches Virasoro |
| `thm:shadow-series-closed-form-Virasoro` | `theorem` | `ProvedHere` | 851 | 0 | 0 | \label{thm:shadow-series-closed-form-Virasoro} Closed-form Virasoro shadow series |
| `thm:shadow-series-closed-form-Virasoro-subleading` | `theorem` | `ProvedHere` | 905 | 0 | 0 | \label{thm:shadow-series-closed-form-Virasoro-subleading} Closed-form subleading Virasoro shadow series |
| `thm:pole-doubling-all-k` | `theorem` | `ProvedHere` | 1001 | 0 | 0 | \label{thm:pole-doubling-all-k} Pole-doubling pattern for all $k$ |
| `prop:phi-k-leading-coefficient-arithmetic` | `proposition` | `ProvedHere` | 1048 | 0 | 0 | \label{prop:phi-k-leading-coefficient-arithmetic} Arithmetic of the leading $\varphi_k$ coefficient |
| `cor:arithmetic-uniformity-class-M` | `corollary` | `ProvedHere` | 1132 | 3 | 0 | \label{cor:arithmetic-uniformity-class-M} $\{2, 3\}$-adic arithmetic is uniform across universal class M stratum |
| `prop:C-A-inverse-radius` | `proposition` | `ProvedHere` | 1269 | 2 | 0 | \label{prop:C-A-inverse-radius} $C_\cA$ is the inverse radius of convergence of the shadow series |
| `thm:w3-wline-closed-form` | `theorem` | `ProvedHere` | 1487 | 3 | 0 | \label{thm:w3-wline-closed-form} $W_3$ $W$-line integer sequence closed form |
| `thm:w3-wline-exponential-base` | `theorem` | `ProvedHere` | 1539 | 3 | 0 | \label{thm:w3-wline-exponential-base} $W$-line shadow-exponential base $C_{W_3}^{W\text{-line}} = 12$ |
| `thm:w3-wline-generating-function` | `theorem` | `ProvedHere` | 1579 | 4 | 0 | \label{thm:w3-wline-generating-function} Exact generating-function closed form for the $W$-line sequence |
| `cor:w3-wline-self-consistency` | `corollary` | `ProvedHere` | 1631 | 1 | 0 | \label{cor:w3-wline-self-consistency} Riccati self-consistency at the radius of convergence |
| `prop:sth-virasoro-rational-through-8` | `proposition` | `ProvedHere` | 1937 | 2 | 0 | \label{prop:sth-virasoro-rational-through-8}No motivic period enters Virasoro through weight 8 |
| `prop:sth-summary` | `proposition` | `ProvedHere` | 1994 | 4 | 0 | \label{prop:sth-summary}Closed-form weighted Virasoro spectrum through weight 8 |
| `thm:s-r-kummer-absent-through-r-11` | `theorem` | `ProvedHere` | 2055 | 5 | 0 | \label{thm:s-r-kummer-absent-through-r-11}The Bernoulli-leading Kummer pair $\{691, 3617\}$ is absent from $\widehat S^{\rm wt}_r(\Vir_c)$ through $r = 11$ |
| `thm:s9-virasoro-closed-form` | `theorem` | `ProvedHere` | 2303 | 3 | 0 | \label{thm:s9-virasoro-closed-form}Closed form for $S_9(\Vir_c)$ |
| `thm:s10-virasoro-closed-form` | `theorem` | `ProvedHere` | 2366 | 1 | 0 | \label{thm:s10-virasoro-closed-form}Closed form for $S_{10}(\Vir_c)$ |
| `thm:s11-virasoro-closed-form` | `theorem` | `ProvedHere` | 2416 | 1 | 0 | \label{thm:s11-virasoro-closed-form}Closed form for $S_{11}(\Vir_c)$ |
| `thm:shadow-tower-asymptotic-closed-form` | `theorem` | `ProvedHere` | 2453 | 1 | 0 | \label{thm:shadow-tower-asymptotic-closed-form}Closed form for the leading asymptotic |
| `cor:virasoro-23-smoothness` | `corollary` | `ProvedHere` | 2523 | 1 | 0 | \label{cor:virasoro-23-smoothness}Every leading numerator is $\{2, 3\}$-smooth |
| `cor:virasoro-motivic-purity-r-leq-11` | `corollary` | `ProvedHere` | 2553 | 4 | 0 | \label{cor:virasoro-motivic-purity-r-leq-11}Motivic purity through weight 11 (SPECIAL CASE of Theorem~\ref{thm:virasoro-motivic-rationality-all-r}) |
| `lem:subleading-combinatorial-identity` | `lemma` | `ProvedHere` | 2624 | 0 | 0 | \label{lem:subleading-combinatorial-identity}Combinatorial identity for the subleading source |
| `thm:shadow-tower-subleading-closed-form` | `theorem` | `ProvedHere` | 2650 | 2 | 0 | \label{thm:shadow-tower-subleading-closed-form}Closed form for the subleading asymptotic |
| `cor:subleading-characteristic-primes` | `corollary` | `ProvedHere` | 2768 | 2 | 0 | \label{cor:subleading-characteristic-primes}Riccati- arithmetic primes of the subleading layer |
| `thm:shadow-tower-sub-subleading-closed-form-inline` | `theorem` | `ProvedElsewhere` | 2831 | 0 | 0 | \label{thm:shadow-tower-sub-subleading-closed-form-inline} Closed form for the sub-subleading asymptotic |
| `lem:sub-subleading-cubic-identity` | `lemma` | `ProvedHere` | 2902 | 0 | 0 | \label{lem:sub-subleading-cubic-identity} Cubic combinatorial identity |
| `cor:kummer-emergence-at-r-8` | `corollary` | `ProvedHere` | 2949 | 0 | 0 | \label{cor:kummer-emergence-at-r-8}Emergence of the Kummer-irregular prime $691$ at $\Gamma_{8}$ |
| `cor:tier-3-characteristic-primes` | `corollary` | `ProvedHere` | 3001 | 0 | 0 | \label{cor:tier-3-characteristic-primes}Tier-3 prime content through $r = 11$ |
| `thm:shadow-tower-tier-4-closed-form` | `theorem` | `ProvedHere` | 3040 | 0 | 0 | \label{thm:shadow-tower-tier-4-closed-form}Closed form for the Tier-4 sub-sub-subleading asymptotic |
| `lem:quintic-combinatorial` | `lemma` | `ProvedHere` | 3100 | 0 | 0 | \label{lem:quintic-combinatorial}Quintic combinatorial identities |
| `thm:kummer-laurent-depth-controlled` | `theorem` | `ProvedHere` | 3187 | 1 | 0 | \label{thm:kummer-laurent-depth-controlled} Laurent-depth-controlled Kummer emergence |
| `cor:bernoulli-leading-duality-sharpness` | `corollary` | `ProvedHere` | 3309 | 1 | 0 | \label{cor:bernoulli-leading-duality-sharpness} Sharpness of the Bernoulli-leading arithmetic duality |
| `lem:floor-parity-subadditive` | `lemma` | `ProvedHere` | 3411 | 0 | 0 | \label{lem:floor-parity-subadditive}Parity subadditivity of the floor |
| `cor:floor-shift-j-plus-k` | `corollary` | `ProvedHere` | 3438 | 1 | 0 | \label{cor:floor-shift-j-plus-k}Floor shift on the index set of the shadow recurrence |
| `thm:s-r-rational-denominator-pattern` | `theorem` | `ProvedHere` | 3459 | 5 | 0 | \label{thm:s-r-rational-denominator-pattern}Rational denominator pattern for the Virasoro shadow tower |
| `thm:phi-n-humbert-heegner-admissibility` | `theorem` | `ProvedHere` | 3990 | 3 | 0 | Humbert--Heegner admissibility filter; pentagon-tower polar cutoff; composite three-filter scope |
| `thm:phi-n-weight-11-12-13` | `theorem` | `ProvedHere` | 4077 | 3 | 0 | Explicit $\phi^{(11)},\phi^{(12)},\phi^{(13)}$ in the Brown canonical basis |

#### `chapters/theory/shadow_tower_other_class_M_platonic.tex` (20)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:shadow-tower-master-equation-classM` | `proposition` | `ProvedHere` | 56 | 2 | 0 | Shadow-tower master equation, class-M form |
| `prop:w3-tline-virasoro-inheritance` | `proposition` | `ProvedHere` | 128 | 2 | 0 | $W_3$ $T$-line: full inheritance of the Virasoro tower |
| `cor:w3-tline-asymptotic` | `corollary` | `ProvedHere` | 157 | 0 | 0 | $T$-line asymptotic, $W_3$ |
| `prop:w3-wline-closed-form` | `proposition` | `ProvedHere` | 176 | 1 | 0 | $W_3$ $W$-line: closed-form coefficients through $r = 10$ |
| `prop:w3-wline-leading-asymptotic` | `proposition` | `ProvedHere` | 218 | 1 | 0 | $W_3$ $W$-line leading large-$c$ behaviour |
| `prop:bp-tline-rational` | `proposition` | `ProvedHere` | 288 | 1 | 0 | BP $T$-line: rationality in $k$ |
| `cor:bp-tline-koszul-conductor` | `corollary` | `ProvedHere` | 311 | 0 | 0 | BP $T$-line: Koszul conductor, Feigin--Frenkel duality |
| `prop:bp-jline-gaussian` | `proposition` | `ProvedHere` | 326 | 1 | 0 | BP $J$-line: Gaussian, depth 2 |
| `prop:wn-line-decomposition` | `proposition` | `ProvedHere` | 369 | 0 | 0 | $W_N$ line decomposition of $\kappa$ |
| `prop:wn-tline-and-w-lines` | `proposition` | `ProvedHere` | 392 | 2 | 0 | $W_N$ $T$-line and principal $W$-lines |
| `prop:w-infinity-line-decomposition` | `proposition` | `ProvedHere` | 448 | 1 | 0 | $W_\infty\lbrack\mu\rbrack$ line-by-line decomposition |
| `thm:shadow-tower-w-infinity-asymptotic` | `theorem` | `ProvedHere` | 468 | 2 | 0 | $W_\infty\lbrack\mu\rbrack$ large-$c$ asymptotic on each line |
| `prop:super-yangian-kappa` | `proposition` | `ProvedHere` | 554 | 0 | 0 | Super-Yangian modular characteristic |
| `prop:super-yangian-tline-shadow` | `proposition` | `ProvedHere` | 576 | 1 | 0 | Super-Yangian $T$-line: Virasoro shadow with graded parity |
| `prop:super-yangian-fermionic-line` | `proposition` | `ProvedHere` | 599 | 1 | 0 | Super-Yangian fermionic-line shadow: sign-reversed Wick |
| `cor:super-yangian-tline-asymptotic` | `corollary` | `ProvedHere` | 628 | 0 | 0 | Super-Yangian leading $T$-line asymptotic |
| `thm:universal-asymptotic-factor` | `theorem` | `ProvedHere` | 644 | 3 | 0 | Universal asymptotic factor for class-M algebras |
| `cor:universal-asymptotic-factor` | `corollary` | `ProvedHere` | 714 | 0 | 0 | Universal asymptotic factor |
| `prop:wp-cartan-shadow-through-r6` | `proposition` | `ProvedHere` | 831 | 1 | 0 | $W(p)$ Cartan-line shadow coefficients through weight six |
| `rem:wp-cross-channel-quartic` | `remark` | `ProvedHere` | 948 | 0 | 0 | Cross-channel quartic on the $T$-$W$ mixed line |

#### `chapters/theory/shadow_tower_quadrichotomy_platonic.tex` (33)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:mc-recursion-line` | `lemma` | `ProvedElsewhere` | 178 | 1 | 0 | MC recursion, line-restricted |
| `prop:vir-shadow-r5` | `proposition` | `ProvedElsewhere` | 200 | 1 | 0 | Virasoro shadow coefficients through $r = 5$ |
| `thm:riccati-master` | `theorem` | `ProvedHere` | 275 | 1 | 0 | Riccati master equation |
| `prop:riccati-three-presentations` | `proposition` | `ProvedHere` | 324 | 4 | 0 | Three equivalent presentations |
| `thm:spectral-hyperelliptic-pf` | `theorem` | `ProvedHere` | 637 | 3 | 0 | Spectral hyperelliptic curve and Picard--Fuchs |
| `cor:branch-points-instantons` | `corollary` | `ProvedHere` | 690 | 0 | 0 | Branch points and inverse-root actions |
| `thm:stokes-line-c-S` | `theorem` | `ProvedHere` | 714 | 0 | 0 | Virasoro branch-root radius and caesura |
| `thm:S6-Vir-closed` | `theorem` | `ProvedHere` | 793 | 2 | 0 | Shadow coefficient $S_6(\Vir_c)$ closed form |
| `thm:riccati-U` | `theorem` | `ProvedHere` | 830 | 2 | 0 | Riccati-on-$U$ master equation |
| `prop:c1-riccati-mc` | `proposition` | `ProvedHere` | 866 | 3 | 0 | C1: Riccati MC element |
| `thm:borel-summability-classM` | `theorem` | `ProvedHere` | 942 | 2 | 0 | C3: Algebraic continuation of the class M metric series |
| `thm:c4-shadow-feynman-gk` | `theorem` | `ProvedHere` | 1024 | 0 | 0 | C4: Shadow--Feynman as $\partial^{2} = 0$ at $b_1 = L$ |
| `prop:c5-hardy-ramanujan-cardy` | `proposition` | `ProvedHere` | 1138 | 0 | 0 | Universal Virasoro vacuum growth |
| `thm:c5-zwegers-mu-shadow-explicit` | `theorem` | `ProvedHere` | 1187 | 1 | 0 | Obstruction to a generic Zwegers $\mu$-shadow for $\Vir_c$ |
| `prop:universal-base-CA-six` | `proposition` | `ProvedElsewhere` | 1250 | 0 | 0 | Universal exponential base on the class M $T$-line |
| `prop:w3-Wline-twelve` | `proposition` | `ProvedElsewhere` | 1280 | 0 | 0 | $\cW_3$ second lane $C^{W{\rm-line}}_{\cW_3} = 12$ |
| `prop:virasoro-inverse-root-field` | `proposition` | `ProvedElsewhere` | 1316 | 0 | 0 | Virasoro inverse-root field |
| `prop:lee-yang-phase` | `proposition` | `ProvedElsewhere` | 1331 | 0 | 0 | Lee--Yang pole at $c = -22/5$ |
| `prop:double-root-phase` | `proposition` | `ProvedHere` | 1342 | 1 | 0 | Secondary rational zero at $c = -83/20$ |
| `prop:omega-large-c-expansion` | `proposition` | `ProvedHere` | 1374 | 2 | 0 | Large-$c$ expansion of the Virasoro branch root |
| `prop:beta-N-per-spin-lane` | `proposition` | `ProvedElsewhere` | 1394 | 1 | 0 | $\beta_N = 12 (H_N - 1)$ per-spin lane |
| `prop:wp-triplet-T-Cartan-line` | `proposition` | `ProvedElsewhere` | 1409 | 1 | 0 | $\cW(p)$ triplet $T$-line and Cartan-line shadows |
| `prop:stqp-312-factor` | `proposition` | `ProvedHere` | 1635 | 3 | 0 | $c_{2d} = -214$ shadow-tower decomposition |
| `prop:stqp-signature` | `proposition` | `ProvedHere` | 1938 | 0 | 0 | Hyperbolic Cartan signature $(2,1)$ for $\mathbf H_{\Delta_5}$ |
| `prop:stqp-unitary-spectrum` | `proposition` | `ProvedHere` | 2036 | 1 | 0 | Positive-energy unitary spectrum |
| `cor:stqp-real-imag-dichotomy` | `corollary` | `ProvedHere` | 2097 | 0 | 0 | Real-root / imaginary-root dichotomy |
| `prop:stqp-fricke-mtc` | `proposition` | `ProvedElsewhere` | 2166 | 3 | 0 | Fricke-fixed unitary sub-MTC and $\mathbb Z/2$-grading |
| `prop:stqp-theta-p-clustering` | `proposition` | `ProvedHere` | 2258 | 2 | 0 | Fricke-phase clustering of Satake angles on the 22 primes $p \le 79$ |
| `prop:stqp-gauss-kuzmin` | `proposition` | `ProvedHere` | 2348 | 0 | 0 | Large-deviations Gauss-Kuzmin statistic near Fricke nodes on the $22$-prime sample |
| `thm:stqp-archimedean-sign` | `theorem` | `ProvedHere` | 2422 | 1 | 0 | Archimedean-$p = 2$ Arthur sign global consistency via Hilbert reciprocity |
| `thm:stqp-fricke-z8-phase-leading` | `theorem` | `ProvedHere` | 2550 | 2 | 0 | $\mathbb Z/8$-phase asymptotics: leading order at the Fricke nodes |
| `thm:stqp-fricke-z8-phase-subleading` | `theorem` | `ProvedHere` | 2632 | 2 | 0 | $\mathbb Z/8$-phase subleading correction: the $\cos(2\theta^*_k)$ curvature term |
| `thm:stqp-fricke-z8-ldp` | `theorem` | `ProvedHere` | 2689 | 4 | 0 | Large-deviations principle for Fricke-phase clustering around the 9 $\mathbb Z/8$-nodes |

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
| `lem:archetype-H123-witness` | `lemma` | `ProvedHere` | 366 | 0 | 2 | Archetype witnesses for (H1)--(H3) |
| `prop:fg-ambient-properties` | `proposition` | `ProvedElsewhere` | 884 | 0 | 2 | $\Fact(X)$ is stable, presentable, symmetric monoidal at the $(\infty,2)$-level |
| `thm:hackney-robertson-model` | `theorem` | `ProvedElsewhere` | 965 | 1 | 2 | Hackney--Robertson factorization properad model structure |

#### `chapters/theory/theorem_B_scope_platonic.tex` (11)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:total-weight-rees-finite-cdg-tower` | `lemma` | `ProvedHere` | 277 | 3 | 0 | Strict total-weight Rees tower |
| `lem:finite-window-derham-realization-positselski` | `lemma` | `ProvedHere` | 322 | 2 | 1 | Finite-window de Rham realisation for Positselski |
| `lem:hom-cone-ml-rees-towers` | `lemma` | `ProvedHere` | 352 | 1 | 1 | Hom-cone Mittag--Leffler for Rees towers |
| `prop:strict-rlim-verdier-quotient` | `proposition` | `ProvedHere` | 403 | 1 | 0 | $R\!\varprojlim$ commutes with the Verdier quotient under strict ML |
| `prop:completed-second-kind-generator-preservation` | `proposition` | `ProvedHere` | 441 | 2 | 0 | Second-kind acyclicity is preserved by the strict completion |
| `rem:theorem-B-chain-level-G-L-attribution` | `remark` | `ProvedElsewhere` | 659 | 1 | 0 | Chain-level class G and L: external attribution |
| `thm:wall-of-walls-obstruction` | `theorem` | `ProvedHere` | 2397 | 6 | 5 | Wall-of-walls obstruction: hidden structure at $H_i\cap H_j$ |
| `prop:tbsp-baily-borel-compatibility` | `proposition` | `ProvedHere` | 2959 | 1 | 3 | Baily--Borel boundary compatibility of the nearby-cycle comparison |
| `prop:tbsp-homotopy-n4-valpha1` | `proposition` | `ProvedElsewhere` | 3821 | 1 | 1 | Degree $n=4$ in the two-sided model |
| `prop:tbsp-homotopy-n6-valpha1` | `proposition` | `ProvedElsewhere` | 3880 | 2 | 0 | Degree $n=6$ and absence of a new obstruction |
| `thm:tbsp-theorem-B-vacuum` | `theorem` | `ProvedHere` | 3957 | 0 | 1 | Theorem B on vacuum |

#### `chapters/theory/three_invariants.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:three-invariants-relations` | `proposition` | `ProvedHere` | 188 | 2 | 0 | Relations and independence |
| `thm:fingerprint-completeness` | `theorem` | `ProvedHere` | 413 | 1 | 0 | Fingerprint completeness |
| `thm:five-class-stratum` | `theorem` | `ProvedHere` | 484 | 2 | 0 | Five-class stratum |
| `prop:coarse-projection-functor` | `proposition` | `ProvedHere` | 533 | 2 | 0 | Coarse projection functor |

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

#### `chapters/theory/universal_conductor_K_platonic.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:uc-universal-conductor` | `theorem` | `ProvedHere` | 176 | 3 | 0 | \textbf{Universal conductor as ordered-to-symmetric descent} |
| `thm:uc-trinity` | `theorem` | `ProvedHere` | 249 | 2 | 0 | \textbf{Three descriptions of the image} |
| `prop:uc-kernel-dimension` | `proposition` | `ProvedHere` | 307 | 1 | 0 | Schur--Weyl kernel count |
| `thm:uc-kernel-archetypes` | `theorem` | `ProvedHere` | 329 | 4 | 0 | Named kernel witnesses by archetype |
| `thm:uc-landscape-universality` | `theorem` | `ProvedHere` | 450 | 2 | 0 | Constructed universality map on census rows |
| `thm:uc-K-Atiyah` | `theorem` | `ProvedHere` | 522 | 0 | 0 | Ordered-Koszul boundary for Vol~III comparisons |
| `cor:uc-K-heisenberg` | `corollary` | `ProvedHere` | 615 | 0 | 0 | Heisenberg scalar packages |
| `cor:uc-K-affine-KM` | `corollary` | `ProvedHere` | 636 | 0 | 0 | Affine Kac--Moody scalar packages |
| `cor:uc-K-virasoro` | `corollary` | `ProvedHere` | 663 | 0 | 0 | Virasoro scalar packages |
| `cor:uc-K-WN` | `corollary` | `ProvedHere` | 684 | 0 | 0 | Principal \texorpdfstring{$W_N$}{WN} scalar packages |
| `cor:uc-K-BP` | `corollary` | `ProvedHere` | 721 | 0 | 0 | Bershadsky--Polyakov scalar packages |
| `prop:uc-K3-BKM-scalar-separation` | `proposition` | `ProvedElsewhere` | 771 | 2 | 0 | K3/BKM scalar separation |
| `cor:uc-K-lattice` | `corollary` | `ProvedHere` | 804 | 0 | 0 | Lattice matter presentation |

#### `chapters/theory/virasoro_motivic_purity.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:denominator-structure` | `proposition` | `ProvedHere` | 315 | 6 | 0 | \label{prop:denominator-structure}Denominator of $S_r(\Vir_c)$ |

#### `chapters/theory/virasoro_motivic_purity_all_r_platonic.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:virasoro-s-r-motivic-purity-all-r` | `theorem` | `ProvedHere` | 208 | 3 | 0 | \label{thm:virasoro-s-r-motivic-purity-all-r}Virasoro shadow-tower motivic purity, all $r \geq 2$ via master-equation recursion |
| `thm:class-M-motivic-purity-algebras-with-Q-rational-OPE` | `theorem` | `ProvedHere` | 319 | 2 | 0 | \label{thm:class-M-motivic-purity-algebras-with-Q-rational-OPE} Motivic purity for class-M chirally Koszul algebras with $\mathbb{Q}$-rational OPE |
| `cor:vmpar-concrete-Q-rational-families` | `corollary` | `ProvedHere` | 373 | 2 | 0 | \label{cor:vmpar-concrete-Q-rational-families} Concrete families with all-$r$ motivic purity |
| `prop:mzv-would-enter-at-what-weight` | `proposition` | `ProvedHere` | 417 | 1 | 0 | \label{prop:mzv-would-enter-at-what-weight} Virasoro shadow coefficients contain no odd-zeta of any weight |

#### `chapters/theory/z_g_kummer_bernoulli_platonic.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:z-g-closed-form-polynomial` | `theorem` | `ProvedHere` | 60 | 1 | 0 | $Z_g(k)$ closed form |
| `thm:z-g-polynomial-form` | `theorem` | `ProvedHere` | 146 | 2 | 0 | Polynomial factorisation of $Z_g$ |
| `thm:z-g-leading-coefficient-bernoulli` | `theorem` | `ProvedHere` | 209 | 4 | 0 | Hurwitz--Bernoulli leading coefficient |
| `thm:z-g-kummer-congruence` | `theorem` | `ProvedHere` | 324 | 4 | 0 | Irregular-prime witnesses |
| `thm:z-g-s-r-arithmetic-duality` | `theorem` | `ProvedHere` | 528 | 3 | 0 | $Z_g$ vs $S_r(\Vir_c)$ arithmetic duality at the Bernoulli-leading Kummer pair |

### Part II: Examples (584)

#### `chapters/examples/bar_complex_tables.tex` (18)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | `ProvedHere` | 729 | 1 | 0 | Serre tensors are quadratic syzygies, not the dual algebra |
| `comp:sl3-casimir-decomp` | `computation` | `ProvedHere` | 1051 | 0 | 0 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | `ProvedHere` | 1132 | 0 | 0 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | `ProvedHere` | 1463 | 1 | 0 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | `ProvedHere` | 1779 | 1 | 0 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | `ProvedHere` | 1825 | 4 | 0 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | `ProvedHere` | 1896 | 0 | 1 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | `ProvedHere` | 1947 | 1 | 0 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | `ProvedHere` | 2080 | 1 | 0 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | `ProvedHere` | 2116 | 1 | 0 | Bar differential as BGG differential |
| `prop:G2-bar-dims` | `proposition` | `ProvedHere` | 2581 | 2 | 0 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | `ProvedHere` | 2785 | 0 | 0 | Virasoro curvature survives the degree-\texorpdfstring{$3$}{3} residue |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | `ProvedHere` | 3000 | 1 | 0 | Heisenberg bar complex: adjacent residues and central class |
| `prop:km-generic-acyclicity` | `proposition` | `ProvedHere` | 3063 | 1 | 0 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | `ProvedHere` | 3098 | 2 | 0 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | `ProvedHere` | 3467 | 1 | 0 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | `ProvedHere` | 3677 | 1 | 0 | \texorpdfstring{$E_8$}{E_8} affine pre-quotient Koszul acyclicity |
| `prop:universal-dim-formula` | `proposition` | `ProvedHere` | 4030 | 2 | 0 | Universal bar complex dimension formula |

#### `chapters/examples/beta_gamma.tex` (20)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:beta-gamma-modes` | `proposition` | `ProvedElsewhere` | 320 | 0 | 1 | Mode algebra \cite{FBZ04} |
| `thm:beta-gamma-stress` | `theorem` | `ProvedElsewhere` | 330 | 0 | 1 | Stress tensor and central charge \cite{FBZ04} |
| `thm:betagamma-fermion-koszul` | `theorem` | `ProvedHere` | 490 | 0 | 1 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | `ProvedHere` | 543 | 1 | 0 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | `ProvedHere` | 589 | 0 | 0 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | `ProvedHere` | 612 | 0 | 0 | — |
| `thm:cobar-fermions` | `theorem` | `ProvedHere` | 640 | 0 | 0 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | `ProvedHere` | 679 | 3 | 0 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:physical-bosonization` | `theorem` | `ProvedElsewhere` | 711 | 1 | 1 | Physical bosonization \cite{FBZ04} |
| `thm:beta-gamma-bar` | `theorem` | `ProvedHere` | 768 | 1 | 0 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `thm:beta-gamma-universal` | `theorem` | `ProvedElsewhere` | 802 | 0 | 1 | Universal property of \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} \cite{FBZ04} |
| `prop:betagamma-bar-acyclicity` | `proposition` | `ProvedHere` | 1036 | 1 | 0 | Twisted Koszul acyclicity for \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-E1-page` | `proposition` | `ProvedHere` | 1397 | 0 | 1 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | `ProvedHere` | 1470 | 2 | 0 | Spectral sequence collapse |
| `prop:betagamma-interval-compactification` | `proposition` | `ProvedElsewhere` | 1674 | 0 | 1 | Interval compactification produces the full $\beta\gamma$ algebra {\cite{CDG20}, \S4.2} |
| `prop:mumford-exponent-complementarity` | `proposition` | `ProvedHere` | 1778 | 1 | 0 | Mumford exponent complementarity |
| `lem:betagamma-ell2-vanishing` | `lemma` | `ProvedHere` | 2392 | 0 | 0 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | `ProvedHere` | 2439 | 4 | 0 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `thm:betagamma-rank-one-rigidity` | `theorem` | `ProvedHere` | 2582 | 0 | 0 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | `ProvedHere` | 2612 | 1 | 0 | Pure contact boundary law |

#### `chapters/examples/chiral_moonshine_unified.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:bar-euler-hilbert` | `proposition` | `ProvedHere` | 172 | 1 | 0 | Primitive bar-Euler product |
| `thm:moonshine-bar-euler-master` | `theorem` | `ProvedHere` | 232 | 3 | 0 | Denominator/bar-Euler comparison criterion |
| `thm:conway-chiral-structure` | `theorem` | `ProvedElsewhere` | 491 | 1 | 0 | Conway chiral input |

#### `chapters/examples/deformation_quantization.tex` (25)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:kontsevich-star-product` | `theorem` | `ProvedElsewhere` | 52 | 0 | 1 | Kontsevich 1997 \cite{Kon03} |
| `thm:chiral-quantization` | `theorem` | `ProvedHere` | 166 | 0 | 0 | Local coisson quantization and global obstruction |
| `thm:chiral-kontsevich` | `theorem` | `ProvedHere` | 259 | 2 | 0 | Local Kontsevich--chiral comparison |
| `thm:kontsevich-explicit-formula` | `theorem` | `ProvedElsewhere` | 384 | 0 | 1 | Explicit formula \cite{Kon03} |
| `thm:stokes-associativity` | `theorem` | `ProvedElsewhere` | 396 | 0 | 1 | Stokes' theorem yields associativity \cite{Kon03} |
| `thm:bar-computes-deformation` | `theorem` | `ProvedHere` | 455 | 1 | 0 | Chiral deformation complex from the bar construction |
| `prop:mc-star-product` | `proposition` | `ProvedHere` | 510 | 0 | 0 | MC elements and filtered chiral products |
| `thm:deformation-genus-expansion` | `theorem` | `ProvedHere` | 680 | 1 | 0 | Modular correction package |
| `thm:chiral-formality` | `theorem` | `ProvedElsewhere` | 749 | 0 | 3 | Local \texorpdfstring{$\Etwo$}{E2} formality input \cite{Tamarkin00, FG12} |
| `prop:ainfty-operations-config` | `proposition` | `ProvedElsewhere` | 786 | 0 | 1 | \texorpdfstring{$A_\infty$}{A-infinity} operations \cite{Kon03} |
| `thm:master-identity-deformation` | `theorem` | `ProvedElsewhere` | 803 | 0 | 1 | Deformation-complex dictionary \cite{Kon03} |
| `thm:obstruction-quantization` | `theorem` | `ProvedElsewhere` | 960 | 0 | 1 | Obstruction theory \cite{Kon03} |
| `prop:kontsevich-mzv` | `proposition` | `ProvedElsewhere` | 1186 | 0 | 1 | Configuration space periods and associator coefficients \cite{Kon03} |
| `prop:jacobi-nilpotent` | `proposition` | `ProvedHere` | 1593 | 1 | 0 | Cofree Jacobi coderivation square |
| `lem:dcrit-boundary-linear` | `lemma` | `ProvedHere` | 1983 | 1 | 0 | dCrit for boundary-linear $W$ |
| `thm:boundary-linear-lg` | `theorem` | `ProvedHere` | 2080 | 3 | 0 | Boundary-linear LG theorem |
| `prop:defq-C1-existence` | `proposition` | `ProvedHere` | 2525 | 1 | 0 | C1 -- existence and pole structure |
| `thm:defq-C2-CYBE` | `theorem` | `ProvedHere` | 2551 | 2 | 0 | Dynamical CYBE for \texorpdfstring{$r(u,Z)$}{r(u,Z)} -- chain-level |
| `thm:defq-C3-lie-bialgebra` | `theorem` | `ProvedHere` | 2623 | 2 | 0 | C3 -- Lie bialgebra |
| `thm:defq-kazhdan-classical-limit` | `theorem` | `ProvedHere` | 2677 | 5 | 0 | Formal classical-limit criterion, Vol~I form |
| `thm:defq-super-kontsevich-formality` | `theorem` | `ProvedElsewhere` | 2764 | 0 | 0 | Finite-truncation super-Kontsevich formality |
| `thm:defq-star-product-specialisation` | `theorem` | `ProvedHere` | 2821 | 2 | 0 | Root-of-unity specialization criterion |
| `thm:defq-unified-motivic-origin` | `theorem` | `ProvedElsewhere` | 2856 | 0 | 0 | Associator coefficients and MZV periods |
| `thm:defq-grt1-equivariance` | `theorem` | `ProvedElsewhere` | 2892 | 0 | 0 | $\mathrm{GRT}_1$-action on formality choices |
| `thm:defq-unified-kontsevich-theorem` | `theorem` | `ProvedHere` | 2959 | 3 | 0 | Conditional formal comparison for \texorpdfstring{$\mathbf H_{\Delta_5}$}{H Delta 5} |

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

#### `chapters/examples/exceptional_yangian_koszul_duality_platonic.tex` (11)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `rem:exceptional-yangian-not` | `remark` | `ProvedElsewhere` | 96 | 1 | 1 | What this chapter is not |
| `prop:exceptional-yangian-template` | `proposition` | `ProvedHere` | 117 | 2 | 3 | Four-step template for Yangian Koszul duality |
| `thm:exceptional-yangian-pbw-grw18` | `theorem` | `ProvedElsewhere` | 194 | 0 | 1 | Exceptional-type Yangian PBW; \cite{GRW18} |
| `cor:exceptional-yangian-graded` | `corollary` | `ProvedHere` | 221 | 1 | 0 | Exceptional-type graded identification |
| `prop:exceptional-yangian-koszul-E6` | `proposition` | `ProvedHere` | 262 | 2 | 0 | $E_6$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-E7` | `proposition` | `ProvedHere` | 302 | 2 | 0 | $E_7$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-E8` | `proposition` | `ProvedHere` | 335 | 2 | 0 | $E_8$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-F4` | `proposition` | `ProvedHere` | 385 | 2 | 1 | $F_4$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-G2` | `proposition` | `ProvedHere` | 432 | 2 | 1 | $G_2$ Yangian Koszul duality |
| `thm:exceptional-yangian-koszul-duality-all-five-types` | `theorem` | `ProvedHere` | 477 | 7 | 1 | Exceptional-type Yangian Koszul duality, all five types |
| `cor:exceptional-yangian-all-simple` | `corollary` | `ProvedHere` | 507 | 2 | 1 | All-simple-type unconditional closure |

#### `chapters/examples/free_fields.tex` (58)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:fermion-shadow-metric` | `proposition` | `ProvedHere` | 366 | 1 | 0 | Shadow metric of the free fermion |
| `prop:fermion-rmatrix` | `proposition` | `ProvedHere` | 479 | 2 | 0 | Free fermion $r$-matrix |
| `thm:fermion-sewing` | `theorem` | `ProvedHere` | 601 | 1 | 0 | Free fermion sewing |
| `prop:bc-general-spin-class-c` | `proposition` | `ProvedElsewhere` | 865 | 1 | 0 | $bc$ ghost system at general spin: class~C for all $\lambda$ |
| `thm:single-fermion-boson-duality` | `theorem` | `ProvedHere` | 914 | 0 | 0 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | `ProvedHere` | 1001 | 1 | 0 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | `ProvedHere` | 1070 | 1 | 0 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | `ProvedHere` | 1127 | 0 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-deformation-channels` | `proposition` | `ProvedHere` | 1250 | 1 | 0 | $\beta\gamma$ deformation complex |
| `comp:betagamma-shadow-weights` | `computation` | `ProvedHere` | 1437 | 2 | 0 | $\beta\gamma$ shadow obstruction tower: special weight table |
| `prop:betagamma-weight-symmetry` | `proposition` | `ProvedHere` | 1473 | 1 | 0 | Weight symmetry $\neq$ Koszul duality |
| `thm:heisenberg-bar` | `theorem` | `ProvedHere` | 1563 | 6 | 0 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | `ProvedHere` | 1589 | 0 | 0 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | `ProvedHere` | 1648 | 1 | 0 | Heisenberg curved cobar structure |
| `thm:lattice-voa-bar` | `theorem` | `ProvedHere` | 1720 | 0 | 0 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | `ProvedHere` | 1749 | 0 | 0 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | `ProvedHere` | 1779 | 0 | 0 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | `ProvedHere` | 1818 | 0 | 0 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | `ProvedHere` | 1883 | 0 | 0 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | `ProvedHere` | 1907 | 0 | 0 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `thm:heisenberg-koszul-dual-early` | `theorem` | `ProvedHere` | 2202 | 3 | 3 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | `ProvedHere` | 2243 | 1 | 0 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | `ProvedHere` | 2380 | 2 | 0 | Fock module bar resolution |
| `cor:fock-character-koszul` | `corollary` | `ProvedHere` | 2485 | 2 | 0 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | `ProvedHere` | 2527 | 1 | 0 | Ext groups between Fock modules |
| `thm:heisenberg-not-self-dual` | `theorem` | `ProvedHere` | 3033 | 1 | 1 | Heisenberg is not self-dual |
| `thm:rhagavendran-heisenberg` | `theorem` | `ProvedElsewhere` | 3125 | 0 | 1 | Heisenberg duality \cite{CG17} |
| `prop:bar-bv-free-fields` | `proposition` | `ProvedHere` | 3149 | 2 | 0 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | `ProvedHere` | 3192 | 6 | 0 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | `ProvedHere` | 3501 | 0 | 0 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | `ProvedHere` | 3615 | 2 | 0 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | `ProvedHere` | 3900 | 5 | 0 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | `ProvedHere` | 4054 | 0 | 0 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | `ProvedHere` | 4109 | 3 | 0 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | `ProvedHere` | 4180 | 0 | 0 | Heisenberg level inversion: curved duality |
| `prop:spin-structure-count` | `proposition` | `ProvedElsewhere` | 4295 | 0 | 2 | Spin structure count |
| `thm:fermion-genus1-partition` | `theorem` | `ProvedHere` | 4349 | 2 | 0 | Free fermion genus-1 partition functions |
| `prop:ising-fermion` | `proposition` | `ProvedElsewhere` | 4691 | 0 | 1 | Ising $=$ free fermion |
| `prop:bosonization` | `proposition` | `ProvedElsewhere` | 4752 | 0 | 2 | Bosonization formula |
| `thm:virasoro-moduli` | `theorem` | `ProvedHere` | 4925 | 0 | 1 | Critical Virasoro descent at $c = 26$ |
| `prop:moduli-degeneration` | `proposition` | `ProvedHere` | 5034 | 0 | 0 | Boundary-residue differential on moduli forms |
| `thm:brst-cohomology` | `theorem` | `ProvedElsewhere` | 5103 | 0 | 1 | BRST cohomology \cite{Pol98} |
| `thm:genus-g-chiral-homology` | `theorem` | `ProvedHere` | 5272 | 3 | 1 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:bar-string-integrand` | `theorem` | `ProvedHere` | 5515 | 2 | 0 | Bar classes on moduli and boundary factorization |
| `thm:amplitude-factorization` | `theorem` | `ProvedElsewhere` | 5567 | 1 | 2 | String amplitude factorization \cite{Pol98} |
| `thm:modular-anomaly` | `theorem` | `ProvedElsewhere` | 5626 | 1 | 2 | Modular invariance and anomaly cancellation |
| `thm:modular-invariance` | `theorem` | `ProvedHere` | 5643 | 2 | 1 | Modular invariance of bar complex |
| `thm:modular-classification` | `theorem` | `ProvedElsewhere` | 5766 | 0 | 2 | Complete modular invariance classification \cite{Zhu96, MooreSeiberg89} |
| `thm:wakimoto-bar` | `theorem` | `ProvedHere` | 5799 | 3 | 0 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | `ProvedHere` | 5812 | 1 | 0 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | `ProvedHere` | 5817 | 1 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-classical-integrability` | `theorem` | `ProvedElsewhere` | 5839 | 0 | 1 | Classical \texorpdfstring{$\mathcal{W}$}{W}-algebra integrability |
| `thm:w-integrability` | `theorem` | `ProvedHere` | 5844 | 2 | 0 | Higher \texorpdfstring{$A_\infty$}{A-infinity} corrections in quantum \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `comp:fermion-five-theorems` | `computation` | `ProvedHere` | 5967 | 2 | 0 | Five projections of $\Theta_{\mathcal{F}}$ |
| `comp:lattice-five-theorems` | `computation` | `ProvedHere` | 6127 | 0 | 0 | Five projections of $\Theta_{V_\Lambda}$ |
| `thm:filtered-bar-complex` | `theorem` | `ProvedHere` | 6208 | 0 | 0 | Filtered bar complex |
| `thm:curved-koszul-duality` | `theorem` | `ProvedElsewhere` | 6239 | 0 | 1 | Curved Koszul duality \cite{Positselski11} |
| `prop:massive-chiral-contractible` | `proposition` | `ProvedElsewhere` | 6272 | 0 | 0 | Massive chirals have contractible bar complexes |

#### `chapters/examples/genus_expansions.tex` (21)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `__unlabeled_chapters/examples/genus_expansions.tex:273` | `corollary` | `ProvedHere` | 273 | 0 | 0 | Lattice-independence of genus expansion |
| `prop:sl2-complementarity-all-genera` | `proposition` | `ProvedHere` | 659 | 0 | 0 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:integrable-level-independence` | `proposition` | `ProvedElsewhere` | 759 | 3 | 0 | Level-independence at integrable levels |
| `prop:km-genus2-propagator` | `proposition` | `ProvedHere` | 865 | 5 | 0 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | `ProvedHere` | 919 | 4 | 0 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | `ProvedHere` | 1140 | 5 | 0 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | `ProvedHere` | 1280 | 3 | 0 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `prop:w3-genus4-cross-channel` | `proposition` | `ProvedHere` | 1551 | 1 | 0 | Genus-4 cross-channel correction |
| `comp:w4-w5-grav-cross` | `computation` | `ProvedHere` | 1621 | 1 | 0 | Universal gravitational cross-channel: $\cW_4$ and $\cW_5$ specializations |
| `comp:w4-full-ope-examples` | `computation` | `ProvedHere` | 1695 | 2 | 1 | $\cW_4$ full-OPE cross-channel: the first irrational correction |
| `prop:genus-expansion-convergence` | `proposition` | `ProvedHere` | 1893 | 1 | 0 | Convergence of the scalar genus expansion |
| `prop:complementarity-genus-series` | `proposition` | `ProvedHere` | 1959 | 1 | 0 | Central charge genus series |
| `prop:bar-verlinde-asymptotics` | `proposition` | `ProvedHere` | 2108 | 1 | 1 | Bar free energy and Verlinde determinant curvature |
| `prop:vir-complementarity` | `proposition` | `ProvedHere` | 2315 | 0 | 0 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | `ProvedHere` | 2422 | 0 | 0 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `prop:bc-betagamma-complementarity` | `proposition` | `ProvedHere` | 2648 | 0 | 0 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:universal-fe-ratios` | `proposition` | `ProvedHere` | 2905 | 1 | 0 | Universal free-energy ratios |
| `prop:neumann-character` | `proposition` | `ProvedElsewhere` | 4002 | 0 | 1 | Neumann pure-gauge character |
| `prop:dirichlet-character-genus` | `proposition` | `ProvedElsewhere` | 4023 | 0 | 1 | Dirichlet character |
| `thm:boundary-characters-bar-hilbert` | `theorem` | `ProvedHere` | 4053 | 0 | 1 | Boundary characters as bar Hilbert series |
| `prop:multi-chiral-product-characters` | `proposition` | `ProvedElsewhere` | 4095 | 0 | 0 | Multi-chiral product formulas |

#### `chapters/examples/heisenberg_eisenstein.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:heisenberg-gaussian-termination` | `proposition` | `ProvedHere` | 125 | 1 | 0 | Gaussian shadow termination for Heisenberg |
| `prop:heisenberg-r-matrix` | `proposition` | `ProvedHere` | 318 | 1 | 0 | Heisenberg $r$-matrix |
| `prop:eisenstein-modular` | `proposition` | `ProvedElsewhere` | 464 | 0 | 1 | Modular transformation laws \cite{Kac} |
| `thm:heisenberg-genus-zero` | `theorem` | `ProvedElsewhere` | 501 | 1 | 1 | Genus zero correlation functions \cite{FBZ04} |
| `thm:heisenberg-genus-one-complete` | `theorem` | `ProvedHere` | 532 | 0 | 0 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | `ProvedHere` | 638 | 0 | 0 | Genus-2 Heisenberg kernel |
| `thm:heisenberg-all-genus` | `theorem` | `ProvedHere` | 861 | 1 | 0 | Heisenberg at general genus |
| `prop:modular-weight-formula` | `proposition` | `ProvedElsewhere` | 943 | 0 | 2 | Eisenstein normalization and scalar scope \cite{Igusa62,Klingen67} |
| `thm:eta-appearance` | `theorem` | `ProvedHere` | 980 | 0 | 0 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | `ProvedHere` | 1043 | 0 | 2 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | `ProvedHere` | 1372 | 0 | 0 | Multi-boson elliptic coefficients |
| `thm:heisenberg-exact-linearity` | `theorem` | `ProvedHere` | 1677 | 1 | 0 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | `ProvedHere` | 1717 | 3 | 0 | Heisenberg shadow obstruction tower: finite termination at degree~$2$ |
| `prop:heisenberg-primitive-kernel` | `proposition` | `ProvedHere` | 2053 | 2 | 0 | Heisenberg primitive kernel |
| `prop:heisenberg-open-sector` | `proposition` | `ProvedHere` | 2179 | 0 | 1 | Completed Fock open sector for Heisenberg |

#### `chapters/examples/kac_moody.tex` (54)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:km-genus1-hessian` | `computation` | `ProvedHere` | 293 | 2 | 0 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `thm:critical-level-structure` | `theorem` | `ProvedElsewhere` | 382 | 0 | 1 | Feigin--Frenkel center at critical level \cite{Feigin-Frenkel} |
| `thm:vertex-chiral-equivalence` | `theorem` | `ProvedElsewhere` | 480 | 0 | 2 | Equivalence of perspectives \cite{FBZ04, BD04} |
| `prop:km-critical-separation` | `proposition` | `ProvedHere` | 591 | 5 | 0 | Critical-level separation of affine invariants |
| `thm:geometric-ope-kac-moody` | `theorem` | `ProvedHere` | 688 | 1 | 0 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | `ProvedHere` | 722 | 2 | 0 | Level-shifting duality, abstract form |
| `thm:wakimoto-brst-full-nondegenerate` | `theorem` | `ProvedHere` | 923 | 0 | 3 | Wakimoto BRST exactness on the generic nonresonant locus |
| `thm:sl2-critical` | `theorem` | `ProvedElsewhere` | 1251 | 0 | 1 | Critical level simplification for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} \cite{Feigin-Frenkel} |
| `thm:sl2-koszul-dual` | `theorem` | `ProvedHere` | 1269 | 1 | 0 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:w3-wakimoto-sl3` | `theorem` | `ProvedElsewhere` | 1458 | 0 | 1 | Wakimoto for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} \cite{Frenkel-Kac-Wakimoto92} |
| `thm:sl3-koszul-dual` | `theorem` | `ProvedHere` | 1477 | 2 | 0 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | `ProvedHere` | 1521 | 2 | 0 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | `ProvedHere` | 1561 | 4 | 0 | Curved level decomposition of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | `ProvedHere` | 1662 | 1 | 0 | Critical-level curved spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | `ProvedHere` | 1750 | 0 | 0 | Generic level-independence on the curvature-flat comparison surface |
| `thm:universal-kac-moody-koszul` | `theorem` | `ProvedHere` | 1890 | 1 | 0 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | `ProvedHere` | 1933 | 1 | 0 | Killing form via structure constants |
| `prop:verdier-level-identification` | `proposition` | `ProvedHere` | 2027 | 3 | 1 | Verdier level identification |
| `thm:principal-w-algebra-structure` | `theorem` | `ProvedElsewhere` | 2762 | 0 | 2 | Principal \texorpdfstring{$\mathcal{W}$}{W}-algebra structure \cite{FF, Ara07} |
| `thm:km-higher-genus-corrections` | `theorem` | `ProvedHere` | 2822 | 3 | 0 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | `ProvedHere` | 2904 | 1 | 0 | Closed-form current presentation in the Koszul dual |
| `thm:km-quantum-groups` | `theorem` | `ProvedHere` | 3305 | 3 | 1 | Quantum-group parameter inversion |
| `prop:spectral-flow-koszul` | `proposition` | `ProvedElsewhere` | 3515 | 0 | 1 | Spectral flow and Koszul duality \cite{Kac} |
| `thm:bar-verlinde-recovery` | `theorem` | `ProvedElsewhere` | 3591 | 0 | 0 | Verlinde recovery from the bar complex |
| `thm:admissible-rep-theory` | `theorem` | `ProvedElsewhere` | 3681 | 1 | 2 | Representation theory at admissible level \cite{KW88, Arakawa17} |
| `prop:bar-admissible` | `proposition` | `ProvedHere` | 3707 | 4 | 0 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | `ProvedHere` | 3779 | 4 | 0 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-general-rank` | `theorem` | `ProvedElsewhere` | 4079 | 1 | 1 | Kac--Wakimoto character formula in general rank |
| `prop:ds-admissible` | `proposition` | `ProvedElsewhere` | 4412 | 2 | 1 | DS reduction at admissible level \cite{Arakawa17} |
| `prop:whittaker-ds` | `proposition` | `ProvedElsewhere` | 4493 | 0 | 3 | Whittaker modules and DS reduction \cite{Arakawa17} |
| `prop:bar-whittaker` | `proposition` | `ProvedHere` | 4551 | 1 | 1 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | `ProvedHere` | 4638 | 4 | 0 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `prop:sl2-genus1-partition` | `proposition` | `ProvedHere` | 4853 | 3 | 0 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | `ProvedHere` | 4925 | 5 | 0 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | `ProvedHere` | 5049 | 1 | 0 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:affine-cubic-normal-form` | `theorem` | `ProvedHere` | 5630 | 0 | 0 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | `ProvedHere` | 5666 | 2 | 0 | Affine shadow obstruction tower: finite termination at degree~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | `ProvedHere` | 5704 | 2 | 0 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | `ProvedHere` | 5746 | 1 | 0 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | `ProvedHere` | 5816 | 3 | 0 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | `ProvedHere` | 5864 | 5 | 0 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | `ProvedHere` | 5921 | 2 | 0 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | `ProvedHere` | 5998 | 5 | 0 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | `ProvedHere` | 6084 | 2 | 0 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | `ProvedHere` | 6120 | 1 | 0 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | `ProvedHere` | 6300 | 2 | 0 | Vanishing of the genus loop on the affine cubic |
| `prop:km-cubic-shadow-level-independence` | `proposition` | `ProvedHere` | 6365 | 1 | 0 | Level-independence of the cubic shadow product |
| `prop:nsl-shadow-tower` | `proposition` | `ProvedHere` | 6490 | 3 | 0 | Non-simply-laced shadow obstruction tower |
| `prop:complete-exceptional-shadow` | `proposition` | `ProvedHere` | 6635 | 3 | 0 | Complete exceptional shadow data |
| `prop:exceptional-anomaly-ratios` | `proposition` | `ProvedHere` | 6725 | 1 | 0 | Anomaly ratios for exceptional principal $\mathcal{W}$-algebras |
| `prop:affine-cs-action` | `proposition` | `ProvedElsewhere` | 6846 | 0 | 2 | The holomorphic-topological Chern--Simons action |
| `prop:level-rank-boundary-voa` | `proposition` | `ProvedElsewhere` | 6962 | 0 | 1 | Level-rank duality for boundary VOAs |
| `cor:level-rank-bar-intertwining` | `corollary` | `ProvedHere` | 6978 | 1 | 0 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | `ProvedHere` | 7007 | 0 | 0 | Kappa anti-symmetry under Feigin--Frenkel involution |

#### `chapters/examples/landscape_census.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:minimal-model-class-transport` | `proposition` | `ProvedHere` | 486 | 0 | 0 | Minimal-model class transport |
| `prop:virasoro-shadow-canonical` | `proposition` | `ProvedHere` | 543 | 1 | 0 | Virasoro shadow-tower coefficients; canonical values |

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
| `thm:lattice:direct-sum` | `theorem` | `ProvedHere` | 1468 | 0 | 0 | Tensor product from direct sum |
| `cor:lattice:kunneth` | `corollary` | `ProvedElsewhere` | 1493 | 2 | 1 | K\"unneth for bar complexes \cite{LV12} |
| `prop:lattice:sublattice` | `proposition` | `ProvedHere` | 1513 | 0 | 0 | Sublattice maps |
| `thm:lattice:overlattice` | `theorem` | `ProvedElsewhere` | 1567 | 0 | 1 | Overlattice vertex algebra \cite{FLM88} |
| `thm:lattice:hochschild` | `theorem` | `ProvedHere` | 1826 | 0 | 0 | Lattice chiral Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | `ProvedHere` | 1871 | 0 | 0 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | `ProvedHere` | 1913 | 0 | 0 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | `ProvedHere` | 1936 | 0 | 0 | Modular invariance |
| `prop:lattice:niemeier-theta-decomposition` | `proposition` | `ProvedHere` | 2075 | 0 | 0 | Niemeier theta series decomposition |
| `prop:lattice:self-dual-criterion` | `proposition` | `ProvedHere` | 2353 | 1 | 0 | Discriminant-trivial module-envelope criterion |
| `prop:lattice:D4-triality` | `proposition` | `ProvedHere` | 2380 | 2 | 0 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | `ProvedHere` | 2419 | 1 | 0 | Lattice twisted-sector charge inversion on the bar surface |
| `prop:lattice:deformation-properties` | `proposition` | `ProvedHere` | 2606 | 2 | 0 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | `ProvedHere` | 2792 | 1 | 0 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | `ProvedHere` | 3424 | 2 | 0 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | `ProvedHere` | 3501 | 3 | 0 | \texorpdfstring{$\Eone$}{E1} adjacent-root bar quotient |
| `prop:lattice:screening-structure` | `proposition` | `ProvedHere` | 3745 | 2 | 0 | Screening current structure |
| `prop:lattice:genus1-simple-pole` | `proposition` | `ProvedHere` | 5115 | 0 | 0 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | `ProvedHere` | 5132 | 2 | 0 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | `ProvedHere` | 5241 | 2 | 0 | Lattice shadow obstruction tower: termination at weight~$2$ |
| `thm:lattice:e1-hochschild` | `theorem` | `ProvedHere` | 5318 | 1 | 0 | $\Eone$ lattice chiral Hochschild complex |
| `prop:xxx-shadow-data` | `proposition` | `ProvedHere` | 5421 | 3 | 0 | XXX shadow data |
| `prop:transfer-matrix-shadow-dict` | `proposition` | `ProvedHere` | 5460 | 0 | 0 | Transfer matrix--shadow dictionary |
| `prop:xxz-shadow-data` | `proposition` | `ProvedHere` | 5510 | 0 | 0 | XXZ shadow data |
| `prop:shadow-cardy-corrections` | `proposition` | `ProvedHere` | 5577 | 0 | 0 | Shadow hierarchy and Cardy corrections |

#### `chapters/examples/level1_bridge.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:level1-kappa-reduction` | `proposition` | `ProvedHere` | 228 | 4 | 0 | Level-$1$ $\kappa$ reduction |
| `prop:level1-cubic-vanishing` | `proposition` | `ProvedHere` | 325 | 1 | 0 | Cubic shadow vanishing at level~$1$ |
| `comp:level1-ade-bridge` | `computation` | `ProvedHere` | 445 | 1 | 0 | Level-$1$ bridge data for the simply-laced series |

#### `chapters/examples/logarithmic_w_algebras.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:wp-kappa` | `proposition` | `ProvedHere` | 187 | 1 | 1 | Virasoro-line $\kappa$ for $\cW(p)$ |
| `prop:wp-c2-cofinite` | `proposition` | `ProvedElsewhere` | 277 | 0 | 1 | $C_2$-cofiniteness of $\cW(p)$ |
| `prop:wp-not-free-strong` | `proposition` | `ProvedHere` | 319 | 1 | 0 | No finite free strong generation |
| `prop:wp-modules` | `proposition` | `ProvedElsewhere` | 425 | 0 | 2 | Module category of $\cW(p)$ |

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

#### `chapters/examples/moonshine.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:moonshine-kappa` | `proposition` | `ProvedHere` | 95 | 3 | 0 | $\kappa(V^\natural) = 12$ |
| `thm:schellekens-three-mechanism` | `theorem` | `ProvedHere` | 339 | 4 | 0 | Schellekens structured decomposition at \texorpdfstring{$c=24$}{c=24} |

#### `chapters/examples/n2_superconformal.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:n2-kappa` | `proposition` | `ProvedHere` | 208 | 1 | 0 | Modular characteristic of the $\mathcal{N}=2$ SCA;\ |
| `prop:n2-complementarity` | `proposition` | `ProvedHere` | 257 | 0 | 0 | Complementarity for the $\mathcal{N}=2$ SCA;\ |
| `prop:n2-koszulness` | `proposition` | `ProvedHere` | 303 | 1 | 1 | PBW Koszulness of the $\mathcal{N}=2$ SCA;\ |

#### `chapters/examples/shadow_tower_extended_families.tex` (10)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:canonical-two-point-norms` | `proposition` | `ProvedElsewhere` | 75 | 1 | 4 | Canonical two-point norms |
| `prop:fateev-lukyanov-alpha` | `proposition` | `ProvedElsewhere` | 145 | 0 | 1 | Fateev--Lukyanov $W \cdot W$ coefficient at weight four |
| `thm:w3-s3-s4-tline` | `theorem` | `ProvedHere` | 175 | 1 | 0 | $\cW_3$ closed forms: $T$-line |
| `thm:w3-w-line-s4-zamolodchikov` | `theorem` | `ProvedHere` | 204 | 3 | 0 | $\cW_3$ closed forms: $W$-line with Zamolodchikov denominator |
| `thm:bp-t-line-rational-k` | `theorem` | `ProvedHere` | 280 | 2 | 0 | BP closed forms: $T$-line rational in $k$ |
| `thm:bp-other-lines` | `theorem` | `ProvedHere` | 344 | 1 | 0 | BP $J$-line and $G^\pm$ line |
| `cor:bp-feigin-frenkel-complementarity` | `corollary` | `ProvedHere` | 394 | 1 | 0 | Feigin--Frenkel complementarity on BP $T$-line |
| `thm:w-infinity-psi-degeneration` | `theorem` | `ProvedHere` | 428 | 3 | 0 | $\cW_\infty\lbrack\Psi\rbrack$ endpoint specialization |
| `thm:super-yangian-parity-sign` | `theorem` | `ProvedHere` | 512 | 1 | 0 | Super-Yangian $\mathfrak{gl}(1\|1)$ parity sign |
| `thm:denominator-factorization-pattern` | `theorem` | `ProvedHere` | 573 | 4 | 0 | Verified denominator factorization patterns |

#### `chapters/examples/symmetric_orbifolds.tex` (5)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:symn-kappa` | `proposition` | `ProvedHere` | 98 | 0 | 0 | Identity-sector modular characteristic |
| `prop:symn-twist-vanishing` | `proposition` | `ProvedHere` | 183 | 1 | 0 | Twist weights and the identity vacuum |
| `prop:symn-shadow-depth` | `proposition` | `ProvedHere` | 310 | 0 | 0 | Diagonal shadow depth of the fixed-point sector |
| `prop:symn-dmvv-kappa` | `proposition` | `ProvedHere` | 459 | 2 | 0 | DMVV does not compute ordered-bar $\kappa$ |
| `prop:symn-hecke-kappa` | `proposition` | `ProvedHere` | 716 | 2 | 0 | Hecke operators and the identity scalar |

#### `chapters/examples/w3_composite_fields.tex` (15)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | `ProvedElsewhere` | 78 | 2 | 2 | Virasoro composite and Fateev--Lukyanov coefficient |
| `prop:lambda-modes` | `proposition` | `ProvedHere` | 158 | 0 | 0 | Mode expansion |
| `thm:c-scaling` | `theorem` | `ProvedHere` | 209 | 0 | 0 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | `ProvedElsewhere` | 307 | 1 | 1 | Zamolodchikov normalization checks |
| `thm:w-w-ope-complete` | `theorem` | `ProvedElsewhere` | 353 | 1 | 1 | \texorpdfstring{$W$}{W}-\texorpdfstring{$W$}{W} OPE complete expansion \cite{Zamolodchikov} |
| `prop:lambda23-quasiprimary` | `proposition` | `ProvedElsewhere` | 481 | 2 | 0 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | `ProvedElsewhere` | 500 | 0 | 0 | Weight-6 Gram determinant |
| `prop:W-squared-qp` | `proposition` | `ProvedHere` | 550 | 1 | 0 | Finite-window quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | `ProvedElsewhere` | 588 | 0 | 0 | Visible norm of \texorpdfstring{$\Xi_W$}{XiW} |
| `thm:w3-null-level1` | `theorem` | `ProvedHere` | 646 | 2 | 0 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | `ProvedHere` | 749 | 0 | 0 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | `ProvedHere` | 804 | 2 | 0 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | `ProvedHere` | 846 | 2 | 0 | Kac determinant vanishing locus at level~1 |
| `thm:w3-kac-general` | `theorem` | `ProvedElsewhere` | 863 | 1 | 2 | \texorpdfstring{$W_3$}{W_3} Kac determinant: general structure |
| `comp:w3-gram-level2` | `computation` | `ProvedHere` | 903 | 2 | 0 | Level-2 Gram matrix |

#### `chapters/examples/w3_holographic_datum.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:w3hol-conductor` | `theorem` | `ProvedHere` | 296 | 1 | 0 | Koszul conductor and self-dual point |
| `thm:w3hol-r-channels` | `theorem` | `ProvedHere` | 387 | 1 | 0 | Channel-by-channel \texorpdfstring{$r$}{r}-matrix |
| `prop:w3hol-lambda-on-primaries` | `proposition` | `ProvedElsewhere` | 452 | 1 | 0 | Action of \texorpdfstring{$\Lambda_0$}{Lambda 0} on primaries |
| `thm:w3hol-Q-T` | `theorem` | `ProvedHere` | 657 | 0 | 0 | Shadow metric on the \texorpdfstring{$T$}{T}-line |
| `thm:w3hol-Q-W` | `theorem` | `ProvedHere` | 670 | 0 | 0 | Shadow metric on the \texorpdfstring{$W$}{W}-line |
| `thm:w3hol-commuting-differentials` | `theorem` | `ProvedHere` | 722 | 1 | 0 | Commuting differentials at \texorpdfstring{$N=3$}{N=3} |

#### `chapters/examples/w_algebras.tex` (66)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:w3-genus1-hessian` | `computation` | `ProvedHere` | 317 | 0 | 0 | The $\mathcal W_3$ genus-$1$ Hessian |
| `comp:w-entropy-ladder` | `computation` | `ProvedHere` | 359 | 1 | 0 | Completion entropy ladder |
| `prop:slodowy-properties` | `proposition` | `ProvedElsewhere` | 867 | 0 | 1 | Properties of the Slodowy slice |
| `thm:slodowy-quantization` | `theorem` | `ProvedElsewhere` | 899 | 0 | 3 | Quantization of Slodowy slices \textup{(}Gan--Ginzburg, Premet\textup{)} |
| `thm:arakawa-variety-intersection` | `theorem` | `ProvedElsewhere` | 951 | 0 | 2 | Arakawa's geometric localization for DS reduction |
| `thm:brst-properties` | `theorem` | `ProvedElsewhere` | 1082 | 0 | 1 | Properties of BRST cohomology \cite{FF} |
| `thm:generators-screening` | `theorem` | `ProvedElsewhere` | 1094 | 0 | 1 | Generators via screening \cite{Frenkel-Kac-Wakimoto92} |
| `thm:gko-coset` | `theorem` | `ProvedElsewhere` | 1163 | 0 | 1 | GKO coset for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} \cite{GKO85} |
| `thm:w-geometric-ope` | `theorem` | `ProvedHere` | 1254 | 0 | 1 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | `ProvedHere` | 1333 | 1 | 0 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `prop:virasoro-from-sl2` | `proposition` | `ProvedElsewhere` | 1481 | 0 | 1 | Virasoro from \texorpdfstring{$\mathfrak{sl}_2$}{sl2} \cite{FF} |
| `thm:virasoro-self-duality` | `theorem` | `ProvedHere` | 1556 | 3 | 0 | Virasoro quadratic self-duality |
| `prop:virasoro-generic-koszul-dual` | `proposition` | `ProvedHere` | 1650 | 3 | 0 | Virasoro Koszul dual at generic central charge |
| `prop:w3-central-charge` | `proposition` | `ProvedElsewhere` | 2019 | 0 | 1 | Central charge from level \cite{Zamolodchikov} |
| `thm:w3-wakimoto` | `theorem` | `ProvedElsewhere` | 2035 | 1 | 1 | Wakimoto realization of \texorpdfstring{$\mathcal{W}_3$}{W3} \cite{Frenkel-Kac-Wakimoto92} |
| `thm:feigin-frenkel-center` | `theorem` | `ProvedElsewhere` | 2663 | 0 | 1 | Feigin--Frenkel: centers at critical level \cite{Feigin-Frenkel} |
| `thm:w-ainfty-ops` | `theorem` | `ProvedHere` | 2813 | 2 | 0 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `prop:w-module-structure` | `proposition` | `ProvedElsewhere` | 3163 | 0 | 1 | Structure of \texorpdfstring{$\mathcal{W}$}{W}-algebra modules \cite{Arakawa17} |
| `prop:log-w-modules` | `proposition` | `ProvedElsewhere` | 3310 | 2 | 2 | Logarithmic W-modules via DS reduction \cite{ACL19} |
| `prop:w3-topological-enhancement` | `proposition` | `ProvedElsewhere` | 3456 | 1 | 1 | Topological enhancement in the $\mathcal{W}_3$ case |
| `prop:w3-3d-action` | `proposition` | `ProvedElsewhere` | 3585 | 2 | 1 | 3d HT Poisson sigma model for $\mathcal{W}_3$ {\cite{KhanZeng25}} |
| `prop:w3-cc-arithmetic` | `proposition` | `ProvedElsewhere` | 3629 | 3 | 0 | Central-charge arithmetic and the genus-1 pipeline |
| `prop:virasoro-beltrami-phase-space` | `proposition` | `ProvedElsewhere` | 3684 | 0 | 1 | Beltrami--quadratic-differential phase space; {} \cite{KhanZeng25} |
| `prop:schwarzian-central-charge` | `proposition` | `ProvedElsewhere` | 3706 | 0 | 1 | Schwarzian cocycle and central charge; {} \cite{KhanZeng25} |
| `prop:virasoro-3d-gravity-action` | `proposition` | `ProvedElsewhere` | 3725 | 3 | 1 | The 3d Virasoro gravity action; {} \cite{KhanZeng25} |
| `thm:w-universal-gravitational-cubic` | `theorem` | `ProvedHere` | 3847 | 0 | 0 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | `ProvedHere` | 3902 | 1 | 0 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | `ProvedHere` | 3939 | 1 | 0 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | `ProvedHere` | 4022 | 1 | 0 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-w3-mixed-shadow` | `theorem` | `ProvedHere` | 4493 | 2 | 0 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w3-two-dim-hessian-cubic` | `proposition` | `ProvedHere` | 4557 | 2 | 0 | Two-dimensional Hessian and universal cubic |
| `thm:w3-quartic-channel-decomposition` | `theorem` | `ProvedHere` | 4585 | 2 | 0 | $\mathcal{W}_3$ quartic channel decomposition |
| `prop:w3-denominator-filtration` | `proposition` | `ProvedHere` | 4646 | 2 | 0 | Denominator filtration by $W$-charge |
| `prop:rho-decreasing-with-N` | `proposition` | `ProvedHere` | 4790 | 1 | 0 | Asymptotic $T$-line shadow growth at fixed positive level |
| `prop:w-w3-weight6-resonance` | `proposition` | `ProvedHere` | 4917 | 1 | 0 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | `ProvedHere` | 4984 | 1 | 0 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | `ProvedHere` | 5010 | 0 | 0 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-virasoro-quintic-forced` | `theorem` | `ProvedHere` | 5166 | 2 | 0 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | `ProvedHere` | 5222 | 1 | 0 | Explicit quintic shadow for Virasoro |
| `thm:virasoro-shadow-generating-function` | `theorem` | `ProvedHere` | 5274 | 3 | 0 | Virasoro shadow metric |
| `thm:w-virasoro-genus1-hessian` | `theorem` | `ProvedHere` | 5635 | 3 | 0 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | `ProvedHere` | 5789 | 2 | 0 | $\mathcal{W}_3$ quintic obstruction |
| `prop:w3-wline-ring-relations` | `proposition` | `ProvedHere` | 6000 | 3 | 0 | Autonomous $W$-line ring relations |
| `thm:w-finite-degree-polynomial-pva` | `theorem` | `ProvedHere` | 6298 | 0 | 1 | Finite-degree theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | `ProvedHere` | 6336 | 2 | 0 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | `ProvedHere` | 6378 | 1 | 0 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | `ProvedHere` | 6405 | 0 | 0 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | `ProvedHere` | 6481 | 2 | 0 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | `ProvedHere` | 6506 | 3 | 0 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | `ProvedHere` | 6540 | 1 | 0 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | `ProvedHere` | 6578 | 1 | 0 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | `ProvedHere` | 6598 | 6 | 0 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `prop:miura-degree-sharp` | `proposition` | `ProvedHere` | 6682 | 1 | 0 | Miura degree bound is sharp |
| `thm:w-pbw-slodowy-collapse` | `theorem` | `ProvedHere` | 6833 | 0 | 0 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | `ProvedHere` | 6894 | 1 | 0 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-degree-detection` | `theorem` | `ProvedHere` | 7003 | 0 | 0 | Canonical degree detection |
| `thm:w-bp-strict` | `theorem` | `ProvedHere` | 7029 | 1 | 0 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | `ProvedHere` | 7079 | 1 | 0 | $\mathcal{W}_4^{(2)}$ has canonical degree~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | `ProvedHere` | 7138 | 1 | 0 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | `ProvedHere` | 7197 | 0 | 0 | Subregular Appell formula |
| `thm:w-unbounded-canonical-degree` | `theorem` | `ProvedHere` | 7235 | 4 | 0 | Unbounded canonical degree |
| `cor:w-subregular-degree-staircase` | `corollary` | `ProvedHere` | 7264 | 2 | 0 | The subregular degree staircase |
| `thm:w-subregular-classification` | `theorem` | `ProvedHere` | 7306 | 7 | 0 | Subregular classification |
| `prop:sl3-nilpotent-shadow-data` | `proposition` | `ProvedHere` | 7392 | 0 | 1 | $\mathfrak{sl}_3$ nilpotent orbits: shadow data |
| `prop:sl4-hook-shadow-data` | `proposition` | `ProvedHere` | 7442 | 0 | 0 | $\mathfrak{sl}_4$ hook-type shadow data |
| `thm:ds-shadow-functor-degree2` | `theorem` | `ProvedHere` | 7484 | 1 | 0 | DS shadow functor at degree~$2$ on computed type-$A$ rows |

#### `chapters/examples/w_algebras_deep.tex` (44)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:jet-flag` | `theorem` | `ProvedElsewhere` | 137 | 0 | 1 | Jet bundle realization \cite{BD04} |
| `thm:w-cdr` | `theorem` | `ProvedElsewhere` | 176 | 0 | 1 | \texorpdfstring{$\mathcal{W}$}{W}-algebras as chiral de Rham \cite{Arakawa17} |
| `thm:w-bar-coalg` | `theorem` | `ProvedHere` | 206 | 2 | 0 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:screen-res` | `theorem` | `ProvedElsewhere` | 266 | 0 | 1 | Screening resolution \cite{Frenkel-Kac-Wakimoto92} |
| `thm:w-toda` | `theorem` | `ProvedElsewhere` | 453 | 0 | 1 | \texorpdfstring{$\mathcal{W}$}{W}-algebras and Toda systems \cite{FF} |
| `thm:master-commutative-square` | `theorem` | `ProvedHere` | 1558 | 3 | 2 | Master commutative square for DS reduction |
| `prop:w3-deg3-vacuum` | `proposition` | `ProvedHere` | 1978 | 2 | 0 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-bar-formality` | `proposition` | `ProvedHere` | 2406 | 1 | 0 | DS--bar commutation via filtration formality |
| `thm:transport-closure-type-a` | `theorem` | `ProvedHere` | 2483 | 1 | 0 | Transport-closure in type $A$ |
| `prop:abelian-locus-type-a` | `proposition` | `ProvedHere` | 3498 | 0 | 0 | Abelian locus in type~$A$ |
| `prop:abelianity-complementarity-independence` | `proposition` | `ProvedHere` | 3541 | 1 | 0 | Independence of abelianity and same-family duality |
| `prop:bfn-slodowy-dimensions` | `proposition` | `ProvedHere` | 3572 | 0 | 1 | BFN--Slodowy dimension matching |
| `prop:svir-3d-sugra-action` | `proposition` | `ProvedElsewhere` | 3716 | 0 | 0 | SuperVirasoro 3d HT lift |
| `thm:winfty-scalar` | `theorem` | `ProvedHere` | 3866 | 0 | 0 | One-dimensional cyclic line for $\mathcal{W}_\infty$ |
| `prop:gram-wt4` | `proposition` | `ProvedHere` | 4021 | 0 | 0 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | `ProvedHere` | 4086 | 0 | 0 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | `ProvedHere` | 4129 | 2 | 0 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:higher-w-gravitational-cubic` | `proposition` | `ProvedHere` | 4324 | 1 | 0 | Gravitational cubic for $\Walg_N$ |
| `prop:higher-w-parity` | `proposition` | `ProvedHere` | 4367 | 0 | 0 | $\mathbb{Z}_2$ parity and the cubic shadow |
| `prop:weight-4-exchange-upgrade` | `proposition` | `ProvedHere` | 4426 | 1 | 0 | Weight-$4$ exchange spectrum upgrade at rank~$3$ |
| `prop:virasoro-primitive` | `proposition` | `ProvedHere` | 4715 | 1 | 0 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | `ProvedHere` | 4776 | 1 | 0 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | `ProvedHere` | 4817 | 1 | 0 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | `ProvedHere` | 4920 | 0 | 0 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | `ProvedHere` | 4953 | 1 | 0 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | `ProvedHere` | 4974 | 1 | 0 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | `ProvedHere` | 5006 | 0 | 0 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | `ProvedHere` | 5113 | 0 | 0 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | `ProvedHere` | 5149 | 2 | 0 | $\Walg_\infty$ bar-window series and Koszul entropy |
| `thm:n2-kappa` | `theorem` | `ProvedHere` | 5394 | 1 | 0 | $N=2$ modular characteristic |
| `prop:n2-koszul-duality` | `proposition` | `ProvedHere` | 5450 | 0 | 0 | $N=2$ Koszul duality |
| `prop:n2-channel-decomposition` | `proposition` | `ProvedHere` | 5521 | 0 | 0 | $N=2$ channel decomposition |
| `prop:n2-bosonic-shadow-metric` | `proposition` | `ProvedHere` | 5554 | 0 | 0 | $N=2$ bosonic shadow metric |
| `prop:n2-minimal-models` | `proposition` | `ProvedHere` | 5599 | 1 | 0 | $N=2$ minimal model shadow data |
| `thm:walgdeep-gaiotto-siegel-weight` | `theorem` | `ProvedHere` | 6144 | 4 | 0 | Borcherds / Siegel weight for class-$\mathcal S$ $A_{N-1}$ on $\Sigma_{0,24}$ |
| `thm:walgdeep-N6-reanchoring` | `theorem` | `ProvedHere` | 6370 | 2 | 0 | $N = 6$ umbral re-anchoring to $6 D_4$ |
| `lem:walgdeep-rank-arithmetic` | `lemma` | `ProvedHere` | 6452 | 0 | 0 | Rank arithmetic of $(24/N) A_{N-1}$ |
| `thm:walgdeep-N6-reanchor-A5-4-D4` | `theorem` | `ProvedHere` | 6472 | 2 | 2 | $N=6$ re-anchor to $A_5^4 D_4$ |
| `thm:walgdeep-N7-N8-re-anchor` | `theorem` | `ProvedHere` | 6676 | 2 | 7 | $N = 7$ and $N = 8$ re-anchors; ladder continuity $k_N^{\mathrm{int}} = N + 3$ |
| `thm:walgdeep-divisor-rule` | `theorem` | `ProvedHere` | 6856 | 1 | 1 | Corrected divisor rule for naive umbral labelling |
| `thm:walgdeep-substitute-anchors` | `theorem` | `ProvedHere` | 6918 | 1 | 0 | Substitute Niemeier anchors at $N \in \{8, 12\}$ via rank-gluing |
| `thm:walgdeep-N24-conway` | `theorem` | `ProvedHere` | 6979 | 0 | 0 | $N = 24$ escape to Conway moonshine via Leech |
| `thm:walgdeep-N9-N12-re-anchor` | `theorem` | `ProvedHere` | 7140 | 2 | 8 | $N \in \{9, 10, 11, 12\}$ re-anchors; ladder continuity $k_N^{\mathrm{int}} = N + 3$ across the Coxeter-void |
| `thm:walgdeep-N13-N24-ladder` | `theorem` | `ProvedHere` | 7405 | 3 | 4 | $N \in \{13, \ldots, 24\}$ ladder; four-regime completion terminating at the Leech escape |

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

#### `chapters/examples/yangians_computations.tex` (46)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bfn` | `theorem` | `ProvedElsewhere` | 37 | 0 | 1 | BFN construction |
| `conj:yangian-spectral-selfdual` | `proposition` | `ProvedHere` | 410 | 0 | 0 | Scalar-gauge inverse and sign reversal |
| `prop:yangian-rank-dependence` | `proposition` | `ProvedHere` | 594 | 0 | 0 | Finite-window rank dependence of the Yangian bar complex |
| `comp:sl3-yangian-from-ordered-bar` | `computation` | `ProvedHere` | 643 | 1 | 0 | The \texorpdfstring{$\mathfrak{sl}_3$}{sl3} Yangian $R$-matrix from the ordered bar |
| `thm:quantum-rmatrix-shadow` | `theorem` | `ProvedHere` | 954 | 1 | 0 | Fundamental quantum \texorpdfstring{$R$}{R}-matrix and classical residue |
| `prop:colored-rmatrix` | `proposition` | `ProvedElsewhere` | 1027 | 2 | 0 | Colored $R$-matrices and Casimir eigenvalues |
| `prop:eval-module-bar` | `proposition` | `ProvedHere` | 1354 | 0 | 0 | Evaluation quotient bar complex |
| `prop:dk2-thick-generation-typeA` | `proposition` | `ProvedHere` | 1625 | 0 | 1 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `cor:dk2-thick-generation-all-types` | `corollary` | `ProvedHere` | 1720 | 2 | 0 | Thick generation for all simple types |
| `lem:composition-thick-generation` | `lemma` | `ProvedHere` | 1745 | 0 | 0 | Thick generation from finite composition series |
| `thm:mc3-universal-multiplicity-free` | `theorem` | `ProvedHere` | 1884 | 1 | 0 | Finite-dimensional evaluation core from Drinfeld polynomials |
| `lem:monoidal-thick-extension` | `lemma` | `ProvedHere` | 2107 | 0 | 0 | Monoidal extension to thick closures |
| `lem:fd-thick-closure` | `lemma` | `ProvedHere` | 2301 | 0 | 0 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | `ProvedHere` | 2387 | 0 | 2 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | `ProvedHere` | 2638 | 1 | 0 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | `ProvedHere` | 2769 | 2 | 0 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | `ProvedHere` | 2927 | 0 | 0 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | `ProvedHere` | 2947 | 1 | 0 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | `ProvedHere` | 2972 | 1 | 0 | Sectorwise localizing generation |
| `prop:lqt-e1-subexponential-growth` | `proposition` | `ProvedHere` | 3044 | 0 | 0 | Sub-exponential growth of the \texorpdfstring{$E_1$}{E_1} page |
| `thm:baxter-exact-triangles-opoly` | `theorem` | `ProvedHere` | 3210 | 2 | 1 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `thm:baxter-exact-triangles` | `theorem` | `ProvedHere` | 3251 | 4 | 1 | Baxter exact triangles on shifted envelope \texorpdfstring{$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$}{Osh} |
| `prop:baxter-yangian-equivariance` | `proposition` | `ProvedHere` | 3322 | 0 | 0 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | `ProvedHere` | 3395 | 3 | 0 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `prop:prefundamental-clebsch-gordan` | `proposition` | `ProvedHere` | 3873 | 0 | 0 | Universal prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | `ProvedHere` | 3911 | 0 | 0 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | `ProvedHere` | 3924 | 2 | 0 | $K_0$ generation for all simple types |
| `prop:categorical-cg-typeA` | `proposition` | `ProvedHere` | 3973 | 2 | 2 | Categorical prefundamental CG decomposition, type~$A$ |
| `thm:mc3-arbitrary-type` | `theorem` | `ProvedHere` | 4472 | 1 | 6 | Categorical prefundamental CG decomposition, all types |
| `prop:e8-root-uniformity` | `proposition` | `ProvedHere` | 4986 | 0 | 0 | $E_8$ relevant-root uniformity |
| `prop:character-cg-all-types` | `proposition` | `ProvedHere` | 4996 | 0 | 0 | Character-level Clebsch--Gordan for all simple types |
| `thm:mc3-universal-multiplicity-free-five-family` | `theorem` | `ProvedHere` | 5118 | 1 | 3 | Finite-dimensional evaluation core from Drinfeld polynomials |
| `prop:monopole-hilbert-decomp` | `proposition` | `ProvedElsewhere` | 5301 | 0 | 1 | Hilbert space decomposition |
| `prop:dirichlet-character` | `proposition` | `ProvedElsewhere` | 5321 | 0 | 1 | Dirichlet boundary character |
| `prop:gauge-koszul-dual-shifted-cotangent` | `proposition` | `ProvedElsewhere` | 5392 | 0 | 1 | Koszul dual of gauge boundary chiral algebra |
| `thm:yangian-vector-seed-propagation` | `theorem` | `ProvedHere` | 5601 | 1 | 0 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | `ProvedHere` | 5631 | 0 | 0 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | `ProvedHere` | 5654 | 0 | 0 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | `ProvedHere` | 5669 | 0 | 0 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | `ProvedHere` | 5720 | 1 | 0 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | `ProvedHere` | 5745 | 0 | 0 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | `ProvedHere` | 5772 | 0 | 0 | Derived realization of the Baxter--Rees family |
| `thm:yangian-H2-reduction` | `theorem` | `ProvedHere` | 5839 | 1 | 0 | $H^2$-reduction to the three-leg sector |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | `ProvedHere` | 5925 | 0 | 0 | Concrete cocycle |
| `thm:u-zeta-8-PBW-wall-crossing` | `theorem` | `ProvedHere` | 6062 | 2 | 0 | Formal PBW increment past the De Concini--Kac wall $N = \ell/2 = 4$ |
| `rem:u-zeta-8-PBW-plateau` | `remark` | `ProvedHere` | 6098 | 0 | 0 | Plateau and the Lusztig Frobenius kernel |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (33)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:dk0-four-path` | `computation` | `ProvedHere` | 264 | 0 | 0 | Four-path Drinfeld--Kohno verification |
| `prop:yangian-canonical-envelope` | `proposition` | `ProvedHere` | 1117 | 0 | 0 | Canonical associative dg model of the Yangian formal-moduli target |
| `prop:finite-stage-tangent` | `proposition` | `ProvedHere` | 1884 | 0 | 1 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | `ProvedHere` | 1965 | 0 | 0 | Mittag-Leffler for finite RTT bar windows |
| `lem:yangian-fd-fundamental-generation` | `lemma` | `ProvedHere` | 3206 | 2 | 0 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | `ProvedHere` | 3236 | 1 | 2 | Finite-dimensional quantum-loop factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | `ProvedHere` | 3406 | 0 | 2 | Type-\texorpdfstring{$A$}{A} quantum-loop fundamental packet is generated by the vector evaluation line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | `ProvedHere` | 3534 | 0 | 2 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | `ProvedHere` | 3572 | 0 | 1 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-tower-mc4-criterion` | `proposition` | `ProvedHere` | 4629 | 4 | 0 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | `ProvedHere` | 4692 | 5 | 0 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | `ProvedHere` | 4727 | 0 | 0 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | `ProvedHere` | 4781 | 4 | 0 | Standard RTT tower satisfies the M-level MC4 package |
| `prop:free-propagator-matching` | `proposition` | `ProvedHere` | 6742 | 2 | 0 | Free/Heisenberg propagator matching |
| `prop:affine-propagator-matching` | `proposition` | `ProvedHere` | 6787 | 0 | 0 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `prop:rmatrix-pole-landscape` | `proposition` | `ProvedHere` | 6878 | 2 | 0 | The collision-residue $r$-matrix across the standard landscape |
| `prop:bosonic-parity-constraint` | `proposition` | `ProvedHere` | 6984 | 0 | 0 | Bosonic parity constraint on $r$-matrix poles |
| `prop:cybe-from-mc` | `proposition` | `ProvedHere` | 7027 | 4 | 0 | CYBE from bar-complex MC equation |
| `prop:rmatrix-from-bar-coproduct` | `proposition` | `ProvedHere` | 7139 | 6 | 1 | Quantum $R$-matrix from the bar coproduct |
| `prop:verlinde-from-shadow` | `proposition` | `ProvedHere` | 7610 | 2 | 1 | Verlinde formula from the shadow complex |
| `thm:spectral-derived-additive-kz` | `theorem` | `ProvedHere` | 8298 | 0 | 0 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | `ProvedHere` | 8396 | 1 | 0 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | `ProvedHere` | 8442 | 0 | 0 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | `ProvedHere` | 8515 | 1 | 0 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | `ProvedHere` | 8598 | 0 | 0 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | `ProvedHere` | 8654 | 0 | 0 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | `ProvedHere` | 8696 | 1 | 0 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | `ProvedHere` | 8731 | 0 | 0 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | `ProvedHere` | 8785 | 0 | 0 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | `ProvedHere` | 8856 | 0 | 0 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | `ProvedHere` | 8880 | 0 | 0 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | `ProvedHere` | 8919 | 0 | 0 | Exact free transport |
| `thm:spectral-conditional-strictification` | `theorem` | `ProvedHere` | 8952 | 8 | 0 | Conditional strictification criterion |

#### `chapters/examples/yangians_foundations.tex` (44)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:super-berezinian-central-automorphism` | `proposition` | `ProvedElsewhere` | 101 | 1 | 3 | Nazarov centrality and super-trace complementarity |
| `thm:yangian-e1` | `theorem` | `ProvedHere` | 528 | 3 | 0 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | `ProvedHere` | 667 | 3 | 0 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | `ProvedHere` | 700 | 2 | 0 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | `ProvedHere` | 803 | 0 | 0 | RTT associated-graded classical limit |
| `prop:yangian-koszul` | `proposition` | `ProvedHere` | 878 | 4 | 1 | RTT Yangian is Koszul |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | `ProvedHere` | 1723 | 4 | 0 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | `ProvedHere` | 1878 | 0 | 0 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | `ProvedHere` | 1982 | 1 | 0 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | `ProvedHere` | 2000 | 0 | 0 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | `ProvedHere` | 2030 | 0 | 0 | Explicit coefficient formula for the fundamental monodromy series |
| `prop:dg-shifted-rtt-boundary-support-bound` | `proposition` | `ProvedHere` | 2092 | 3 | 0 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | `ProvedHere` | 2156 | 3 | 0 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | `ProvedHere` | 2242 | 2 | 0 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | `ProvedHere` | 2339 | 2 | 0 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | `ProvedHere` | 2409 | 1 | 0 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | `ProvedHere` | 2478 | 1 | 0 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | `ProvedHere` | 2515 | 1 | 0 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | `ProvedHere` | 2571 | 1 | 0 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | `ProvedHere` | 2631 | 2 | 0 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | `ProvedHere` | 2692 | 7 | 0 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | `ProvedHere` | 2791 | 3 | 0 | Standard type-A fundamental line operator has the standard local residue |
| `prop:gauge-theory-koszul-dual` | `proposition` | `ProvedElsewhere` | 3067 | 0 | 0 | Gauge theory $\cA^!$ as shifted cotangent loop algebra |
| `thm:gauge-theory-yangian-structure` | `theorem` | `ProvedElsewhere` | 3106 | 0 | 1 | Full dg-shifted Yangian structure on $\cA^!$ |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | `ProvedHere` | 3220 | 0 | 0 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | `ProvedHere` | 3247 | 1 | 0 | Stabilized completed bar/cobar recovery |
| `thm:shifted-rtt-mc-descent` | `theorem` | `ProvedHere` | 3308 | 0 | 0 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | `ProvedHere` | 3396 | 0 | 0 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | `ProvedHere` | 3441 | 0 | 0 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | `ProvedHere` | 3489 | 0 | 0 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | `ProvedHere` | 3505 | 1 | 0 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | `ProvedHere` | 3535 | 0 | 0 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | `ProvedHere` | 3568 | 0 | 0 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | `ProvedHere` | 3602 | 0 | 0 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | `ProvedHere` | 3627 | 0 | 0 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | `ProvedHere` | 3699 | 1 | 0 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | `ProvedHere` | 3748 | 0 | 0 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | `ProvedHere` | 3774 | 0 | 0 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | `ProvedHere` | 3801 | 0 | 0 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | `ProvedHere` | 3823 | 0 | 0 | Kleinian associated graded at the nilpotent point |
| `thm:kzb-as-bar-cobar-alpha` | `theorem` | `ProvedElsewhere` | 3961 | 0 | 0 | KZB as elliptic bar--cobar twisting at leading $\alpha$ |
| `prop:elliptic-coproduct-coassoc-fay` | `proposition` | `ProvedHere` | 3994 | 0 | 0 | Elliptic coproduct is Fay-coassociative |
| `thm:felder-R-half-braiding` | `theorem` | `ProvedHere` | 4021 | 0 | 0 | Felder $R$-matrix as half-braiding |
| `prop:sl2-elliptic-yangian-triangle` | `proposition` | `ProvedHere` | 4040 | 0 | 0 | $\slnn{2}$ elliptic triangle coherence at order $\hbar$ |

### Part III: Connections (286)

#### `chapters/connections/arithmetic_shadows.tex` (121)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:shadow-spectral-correspondence` | `theorem` | `ProvedElsewhere` | 192 | 0 | 0 | Shadow--spectral correspondence |
| `prop:divisor-sum-decomposition` | `proposition` | `ProvedHere` | 306 | 0 | 0 | Divisor-sum decomposition |
| `cor:sewing-euler-product` | `corollary` | `ProvedElsewhere` | 331 | 1 | 0 | Euler product of the sewing determinant |
| `prop:sewing-trace-formula` | `proposition` | `ProvedHere` | 344 | 1 | 0 | Sewing trace formula |
| `thm:sewing-selberg-formula` | `theorem` | `ProvedHere` | 382 | 2 | 0 | Sewing--Selberg formula |
| `thm:narain-universality` | `theorem` | `ProvedHere` | 439 | 0 | 0 | Narain universality |
| `thm:e8-epstein` | `theorem` | `ProvedHere` | 470 | 0 | 0 | $E_8$ Epstein factorization |
| `prop:z2-epstein` | `proposition` | `ProvedHere` | 495 | 0 | 0 | $\bZ^2$ Epstein zeta |
| `prop:leech-epstein` | `proposition` | `ProvedHere` | 518 | 1 | 0 | Leech Epstein factorization |
| `prop:niemeier-multichannel` | `proposition` | `ProvedHere` | 778 | 1 | 0 | Multi-channel Niemeier discrimination |
| `prop:shadow-arithmetic-factorization` | `proposition` | `ProvedHere` | 866 | 0 | 0 | Shadow--arithmetic factorization |
| `prop:leading-hecke-identification` | `proposition` | `ProvedElsewhere` | 1172 | 1 | 0 | Leading-order Hecke identification |
| `prop:hecke-all-orders` | `proposition` | `ProvedHere` | 1199 | 0 | 0 | Exactness of the Hecke identification |
| `prop:period-shadow-dictionary` | `proposition` | `ProvedHere` | 1250 | 3 | 0 | Period--shadow dictionary |
| `comp:period-shadow-vz` | `computation` | `ProvedHere` | 1333 | 0 | 0 | $V_{\bZ}$: the Gaussian archetype |
| `comp:period-shadow-ve8` | `computation` | `ProvedHere` | 1351 | 1 | 0 | $V_{E_8}$: the Lie/tree archetype |
| `comp:period-shadow-leech` | `computation` | `ProvedHere` | 1373 | 1 | 0 | $V_{\mathrm{Leech}}$: the Ramanujan archetype |
| `comp:period-shadow-rank24-comparison` | `computation` | `ProvedHere` | 1425 | 0 | 0 | $D_{16}^+ \oplus D_{16}^+$ vs.\ $E_8^3$: same depth, different coefficient |
| `comp:period-shadow-rank2` | `computation` | `ProvedHere` | 1444 | 1 | 0 | $V_{\bZ^2}$ and $V_{A_2}$: Dedekind zeta at depth~$2$ |
| `thm:spectral-decomposition-principle` | `theorem` | `ProvedHere` | 1468 | 2 | 0 | Spectral decomposition principle |
| `prop:growth-rate-dictionary` | `proposition` | `ProvedHere` | 1555 | 0 | 0 | Growth-rate dictionary |
| `thm:bg-vir-coincidence` | `theorem` | `ProvedElsewhere` | 1581 | 0 | 0 | $\beta\gamma$--Virasoro rate coincidence |
| `prop:self-referentiality-criterion` | `proposition` | `ProvedHere` | 1599 | 2 | 0 | Self-referentiality criterion |
| `cor:conformal-vector-infinite-depth` | `corollary` | `ProvedHere` | 1669 | 1 | 0 | Conformal vector implies infinite shadow depth |
| `thm:shadow-tower-asymptotics` | `theorem` | `ProvedHere` | 1694 | 0 | 0 | Shadow obstruction tower leading asymptotics |
| `cor:rigorous-infinite-depth` | `corollary` | `ProvedHere` | 1726 | 4 | 0 | Rigorous Virasoro infinite shadow depth |
| `prop:bg-primary-counting` | `proposition` | `ProvedElsewhere` | 1770 | 0 | 0 | $\beta\gamma$ primary-counting function |
| `thm:refined-shadow-spectral` | `theorem` | `ProvedElsewhere` | 1783 | 0 | 0 | Refined shadow--spectral correspondence |
| `prop:ising-d-arith` | `proposition` | `ProvedHere` | 1813 | 0 | 0 | Ising model: $d_{\mathrm{arith}} = 0$ |
| `rem:ising-arithmetic-paradox` | `remark` | `ProvedHere` | 1841 | 1 | 0 | The Ising arithmetic paradox |
| `rem:non-unimodular` | `remark` | `ProvedHere` | 1909 | 0 | 0 | Non-unimodular lattices |
| `rem:vnatural-class-m` | `remark` | `ProvedHere` | 2128 | 1 | 0 | The moonshine module: same $\kappa$, different class |
| `thm:interacting-gram-positivity` | `theorem` | `ProvedHere` | 2220 | 2 | 0 | Interacting Gram positivity |
| `cor:virasoro-interacting-gram` | `corollary` | `ProvedHere` | 2260 | 1 | 0 | — |
| `thm:shadow-resonance-locus` | `theorem` | `ProvedHere` | 2273 | 1 | 0 | — |
| `thm:shadow-spectral-measure` | `theorem` | `ProvedHere` | 2311 | 2 | 0 | Shadow spectral measure |
| `prop:carleman-virasoro` | `proposition` | `ProvedHere` | 2417 | 1 | 0 | Carleman rigidity |
| `prop:shadow-periods` | `proposition` | `ProvedHere` | 2467 | 1 | 0 | Shadow amplitudes are periods |
| `prop:universal-stokes-constants` | `proposition` | `ProvedHere` | 2750 | 0 | 0 | Universal Stokes constants |
| `prop:gevrey-zero-degree` | `proposition` | `ProvedHere` | 2783 | 0 | 0 | Gevrey-$0$ degree growth |
| `prop:padic-convergence` | `proposition` | `ProvedHere` | 2841 | 0 | 0 | $p$-adic convergence radius |
| `rem:kummer-kubota-leopoldt` | `remark` | `ProvedHere` | 2867 | 0 | 0 | Kummer congruences and the Kubota--Leopoldt $p$-adic $L$-function |
| `thm:shadow-mzv-dictionary` | `theorem` | `ProvedHere` | 2972 | 1 | 1 | Shadow--MZV dictionary |
| `thm:partition-modular-classification` | `theorem` | `ProvedHere` | 3237 | 1 | 0 | Partition function modular classification |
| `prop:quasi-modular-propagator` | `proposition` | `ProvedHere` | 3299 | 1 | 0 | Quasi-modular content from the genus-$1$ propagator |
| `prop:hecke-eigenvalue-extraction` | `proposition` | `ProvedHere` | 3374 | 1 | 0 | Hecke eigenvalues from partition data |
| `prop:tau-large-primes` | `proposition` | `ProvedHere` | 3413 | 1 | 0 | Ramanujan $\tau(p)$ at primes $83 \leq p \leq 113$ |
| `prop:tau-primes-211-229` | `proposition` | `ProvedHere` | 3480 | 0 | 0 | Ramanujan $\tau(p)$ at primes $p\in\{211,223,227,229\}$ |
| `thm:spectral-curve` | `theorem` | `ProvedHere` | 3552 | 2 | 0 | Algebraic shadow generating function |
| `prop:moment-matrix-negativity` | `proposition` | `ProvedHere` | 3595 | 0 | 0 | Eisenstein moment minor |
| `thm:shadow-eisenstein` | `theorem` | `ProvedElsewhere` | 3763 | 0 | 0 | The genus-$1$ amplitude Mellin transform is Eisenstein |
| `rem:shadow-eisenstein-numerical-check` | `remark` | `ProvedHere` | 3976 | 3 | 0 | The value at $s = 0$ separates the two Dirichlet series |
| `thm:shadow-higgs-field` | `theorem` | `ProvedHere` | 4262 | 3 | 0 | Shadow Higgs field |
| `thm:shadow-bps` | `theorem` | `ProvedHere` | 4981 | 2 | 0 | The shadow obstruction tower as BPS spectrum |
| `cor:shadow-fredholm` | `corollary` | `ProvedElsewhere` | 5240 | 0 | 0 | Shadow Fredholm determinant |
| `prop:mc-bracket-determines-atoms` | `proposition` | `ProvedHere` | 5488 | 2 | 0 | MC bracket determines spectral atoms |
| `rem:mc-ramanujan-bridge` | `remark` | `ProvedHere` | 5538 | 2 | 0 | The bridge to the Ramanujan bound |
| `prop:koszul-field-criterion` | `proposition` | `ProvedHere` | 5791 | 2 | 0 | Koszul field-preservation criterion |
| `prop:heisenberg-koszul-epstein` | `proposition` | `ProvedHere` | 6032 | 1 | 0 | Degenerate case: Heisenberg |
| `comp:virasoro-c1-koszul-epstein` | `computation` | `ProvedHere` | 6084 | 0 | 0 | Virasoro at $c = 1$: numerical Koszul--Epstein value |
| `comp:fe-minimal-models` | `computation` | `ProvedHere` | 6109 | 1 | 0 | Functional equation for all unitary minimal models |
| `thm:spectral-continuation-bridge` | `theorem` | `ProvedHere` | 6189 | 3 | 0 | Hecke-equivariant MC element |
| `thm:schur-complement-quartic` | `theorem` | `ProvedHere` | 6427 | 1 | 0 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | `ProvedHere` | 6486 | 0 | 0 | — |
| `prop:on-off-line-distinction` | `proposition` | `ProvedHere` | 6563 | 1 | 0 | — |
| `prop:li-criterion-failure` | `proposition` | `ProvedHere` | 6973 | 2 | 1 | Structural failure of the Li criterion for the sewing lift |
| `prop:pure-spin-s-schur` | `proposition` | `ProvedHere` | 7123 | 1 | 0 | — |
| `prop:prime-side-defect-formula` | `proposition` | `ProvedHere` | 7231 | 1 | 0 | — |
| `thm:finite-miura-defect` | `theorem` | `ProvedHere` | 7301 | 2 | 0 | Finite Miura defect at genus one |
| `prop:bracket-hodge-index` | `proposition` | `ProvedHere` | 7916 | 0 | 0 | Bracket positivity and the Hodge index |
| `prop:lattice-ramanujan` | `proposition` | `ProvedHere` | 8040 | 0 | 1 | Ramanujan bound for lattice spectral measures |
| `prop:shadow-symmetric-power` | `proposition` | `ProvedHere` | 8082 | 0 | 0 | Shadow--symmetric power identification |
| `thm:petersson-identification` | `theorem` | `ProvedHere` | 8226 | 1 | 0 | Petersson identification |
| `prop:rigidity-threshold` | `proposition` | `ProvedHere` | 8349 | 1 | 0 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | `ProvedHere` | 8447 | 2 | 1 | Lattice Ramanujan from rigidity |
| `prop:stieltjes-signed-universal` | `proposition` | `ProvedHere` | 8641 | 1 | 0 | Universal signed Stieltjes measure |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | `ProvedHere` | 8674 | 0 | 0 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | `ProvedHere` | 8738 | 3 | 0 | Shadow arithmetic trichotomy |
| `prop:genus1-weight-bound` | `proposition` | `ProvedHere` | 8813 | 0 | 0 | Weight bound for genus-$1$ shadow projections |
| `thm:mc-recursion-moment` | `theorem` | `ProvedHere` | 8950 | 0 | 0 | MC recursion on moment $L$-functions |
| `thm:hecke-newton-lattice` | `theorem` | `ProvedHere` | 9094 | 4 | 0 | Hecke--Newton closure for lattice VOAs |
| `cor:unconditional-lattice` | `corollary` | `ProvedElsewhere` | 9157 | 1 | 0 | Unconditional operadic RS for lattice VOAs |
| `thm:non-lattice-ramanujan` | `theorem` | `ProvedHere` | 9189 | 0 | 1 | Non-lattice Ramanujan bound |
| `prop:mc-constraint-counting` | `proposition` | `ProvedHere` | 9716 | 2 | 0 | MC constraint counting |
| `thm:route-c-propagation` | `theorem` | `ProvedHere` | 9781 | 3 | 0 | Route~C: MC rigidity forces character-level prime-locality |
| `thm:hecke-verdier-commutation` | `theorem` | `ProvedHere` | 9943 | 0 | 0 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | `ProvedHere` | 9982 | 5 | 0 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | `ProvedHere` | 10057 | 0 | 1 | Theta decomposition bridge |
| `prop:sewing-spectral-bridge` | `proposition` | `ProvedHere` | 10238 | 3 | 1 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | `ProvedHere` | 10343 | 1 | 0 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | `ProvedHere` | 10390 | 0 | 0 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | `ProvedHere` | 10481 | 2 | 2 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | `ProvedHere` | 10655 | 1 | 0 | Genus-one saddle triviality |
| `cor:first-scattering-pole` | `corollary` | `ProvedElsewhere` | 10855 | 1 | 0 | Nonvanishing at the first scattering pole |
| `thm:scattering-coupling-factorization` | `theorem` | `ProvedHere` | 10955 | 5 | 0 | Scattering coupling factorization |
| `prop:hecke-defect-lattice` | `proposition` | `ProvedHere` | 11217 | 1 | 0 | Hecke defect vanishes for lattice VOAs |
| `thm:packet-connection-flatness` | `theorem` | `ProvedHere` | 11714 | 0 | 0 | Flatness and divisor independence |
| `cor:lattice-packet-diagonal` | `corollary` | `ProvedElsewhere` | 11781 | 1 | 0 | Lattice transparency |
| `prop:gauge-criterion-scattering` | `proposition` | `ProvedHere` | 11847 | 0 | 0 | Gauge criterion for scattering access |
| `rem:arithmetic-comparison-sharpening` | `remark` | `ProvedHere` | 11957 | 0 | 0 | Sharpening of the arithmetic comparison conjecture |
| `prop:miura-packet-splitting` | `proposition` | `ProvedHere` | 12031 | 5 | 0 | — |
| `prop:genus2-non-diagonal` | `proposition` | `ProvedHere` | 12397 | 0 | 0 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | `ProvedHere` | 12441 | 2 | 0 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | `ProvedHere` | 12640 | 1 | 1 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | `ProvedHere` | 12672 | 3 | 2 | B\"ocherer bridge |
| `rem:genus2-definitive-scope` | `remark` | `ProvedHere` | 12802 | 2 | 0 | Definitive scope of genus-$2$ arithmetic access |
| `rem:leech-all-sk` | `remark` | `ProvedHere` | 12857 | 0 | 0 | Leech: all genus-$2$ cusp forms are Saito--Kurokawa lifts |
| `thm:leech-chi12-projection` | `theorem` | `ProvedHere` | 12878 | 2 | 2 | Leech $\chi_{12}$-projection and Waldspurger consequence |
| `thm:prime-locality-obstructions` | `theorem` | `ProvedHere` | 13201 | 4 | 0 | Precise obstructions to prime-locality; {} where indicated |
| `thm:riccati-determinacy-assessment` | `theorem` | `ProvedElsewhere` | 13405 | 0 | 0 | Riccati determinacy |
| `prop:shadow-not-selberg` | `proposition` | `ProvedHere` | 13447 | 3 | 0 | The shadow zeta is not in the Selberg class |
| `thm:fricke-ldp-sub-leading` | `theorem` | `ProvedHere` | 13847 | 1 | 0 | Fricke LDP sub-leading correction at each node |
| `thm:shimura-waldspurger-higher-weights` | `theorem` | `ProvedElsewhere` | 13945 | 1 | 1 | Shimura--Waldspurger constants are period ratios |
| `thm:YD-delta-7-8-9` | `theorem` | `ProvedHere` | 14009 | 3 | 0 | $\delta^{(n)}$ for $n \in \{7, 8, 9, 10, 11, 12\}$ |
| `prop:humbert-heegner-admissibility-filter` | `proposition` | `ProvedHere` | 14183 | 7 | 1 | Humbert--Heegner admissibility filter; genus-$2$ bar--cobar scope |
| `thm:humbert-heegner-filter-g-geq-3` | `theorem` | `ProvedHere` | 14310 | 4 | 9 | Humbert--Heegner filter at $g\ge 3$; saturation at codim $2g-1$ |
| `thm:mu-32-refinement` | `theorem` | `ProvedHere` | 14600 | 1 | 0 | $\mu_{16}\to\mu_{32}$ gerbe refinement is not a consequence of the Bruinier lcm datum near the quadruple Humbert wall |
| `thm:as-monster-k3-cplus-product-invariant` | `theorem` | `ProvedHere` | 14822 | 4 | 1 | Monster--K$3$ $c_+$-product comparison |
| `cor:as-monster-196884-as-cplus-weighted` | `remark` | `ProvedHere` | 14910 | 1 | 1 | Monster $196884$ is not a $c_+$-weighted K$3$ elliptic-genus coefficient |
| `thm:YD-delta-13-16` | `theorem` | `ProvedHere` | 15248 | 2 | 0 | $\delta^{(n)}$ for $n \in \{13, 14, 15, 16\}$ |
| `thm:n-2-root-unity-vol-I-face` | `theorem` | `ProvedHere` | 15503 | 0 | 0 | $N = 2$ root-of-unity: $324$ is not a PBW dimension |

#### `chapters/connections/bv_brst.tex` (12)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:bv-bar-geometric` | `theorem` | `ProvedElsewhere` | 297 | 3 | 1 | Genus-$0$ BV complex and geometric bar complex; {} \cite{CG17} |
| `thm:brst-physical-states` | `theorem` | `ProvedElsewhere` | 513 | 0 | 2 | BRST cohomology on a nilpotent gauge-fixed complex; {} \cite{CG17,Polchinski1998} |
| `thm:log-form-ghost-law` | `theorem` | `ProvedHere` | 549 | 1 | 0 | Coordinate cocycle for collision logarithmic forms |
| `lem:brst-nilpotence` | `lemma` | `ProvedElsewhere` | 649 | 0 | 1 | BRST nilpotence; {} \cite{FGZ86} |
| `rem:ghost-superghost-koszul` | `remark` | `ProvedElsewhere` | 1062 | 0 | 2 | The ghost--superghost Koszul involution |
| `thm:bar-semi-infinite-km` | `theorem` | `ProvedHere` | 1159 | 4 | 5 | Bar complex = semi-infinite complex for KM |
| `prop:chain-level-three-obstructions` | `proposition` | `ProvedHere` | 1922 | 2 | 1 | Three chain-level obstructions and harmonic factorization |
| `comp:v1-burns-koszul-datum` | `computation` | `ProvedElsewhere` | 2719 | 0 | 0 | Burns space Koszul datum |
| `rem:non-cy-scope` | `remark` | `ProvedElsewhere` | 2837 | 1 | 0 | Scope and status |
| `prop:wzw-brst-bar-genus0` | `proposition` | `ProvedHere` | 2859 | 4 | 0 | Genus-\texorpdfstring{$0$}{0} WZW BRST complex from the affine bar complex |
| `thm:bvbrst-heegner-all-order` | `theorem` | `ProvedHere` | 3468 | 4 | 10 | Heegner pattern for the all-order BV obstruction tower |
| `thm:bvbrst-nonperturbative-completion` | `theorem` | `ProvedHere` | 4642 | 4 | 7 | Borcherds analytic completion of the BV obstruction tower |

#### `chapters/connections/concordance.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:glz-special-case` | `proposition` | `ProvedHere` | 684 | 1 | 0 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | `ProvedHere` | 714 | 0 | 1 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | `ProvedHere` | 1019 | 1 | 0 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | `ProvedHere` | 1043 | 1 | 0 | Polynomial level dependence |
| `prop:vol2-bar-cobar-bridge` | `proposition` | `ProvedElsewhere` | 4876 | 1 | 0 | Bar-cobar bridge |
| `prop:vol2-relative-holographic-bridge` | `proposition` | `ProvedElsewhere` | 4932 | 1 | 0 | Relative holographic deformation bridge |
| `prop:vol2-ribbon-thooft-bridge` | `proposition` | `ProvedElsewhere` | 4953 | 3 | 0 | Ribbon/'t~Hooft bridge |
| `comp:spectral-discriminants-standard` | `computation` | `ProvedHere` | 6398 | 0 | 0 | Spectral discriminants of standard families |
| `rem:concord-retraction` | `remark` | `ProvedElsewhere` | 12650 | 0 | 0 | Central charges for $\mathcal T[A_1, \Sigma_{0,24} |

#### `chapters/connections/editorial_constitution.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:master-pbw` | `theorem` | `ProvedElsewhere` | 199 | 4 | 0 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:en-koszul-duality-conc` | `theorem` | `ProvedElsewhere` | 1638 | 1 | 5 | \texorpdfstring{$\mathsf{E}_n$}{En} Koszul duality via configuration space integrals |
| `prop:en-n2-recovery` | `proposition` | `ProvedHere` | 1674 | 7 | 1 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | `ProvedHere` | 1820 | 1 | 1 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |

#### `chapters/connections/entanglement_modular_koszul.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `lem:ent-twist-dimension` | `lemma` | `ProvedElsewhere` | 95 | 1 | 1 | Twist operator dimension |
| `thm:ent-scalar-entropy` | `theorem` | `ProvedHere` | 121 | 4 | 0 | Entanglement entropy at the scalar level |
| `rem:ent-negative` | `remark` | `ProvedHere` | 1347 | 2 | 0 | Negative entanglement entropy at $c_{\mathrm{eff}} = -166$ |
| `prop:ent-real-root` | `proposition` | `ProvedHere` | 1379 | 3 | 0 | Real-root unitary submodule entanglement |
| `thm:ent-topological-entanglement` | `theorem` | `ProvedHere` | 1504 | 3 | 0 | Topological entanglement from non-semisimple total quantum dimension |
| `thm:ent-GSD-T2` | `theorem` | `ProvedHere` | 1583 | 4 | 0 | Ground-state degeneracy on $T^2$ for the 3d bulk TQFT |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:loop-genus-correspondence` | `theorem` | `ProvedElsewhere` | 130 | 0 | 1 | Loop-genus correspondence; {} \cite{costello-renormalization} |

#### `chapters/connections/feynman_diagrams.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | `ProvedHere` | 218 | 0 | 0 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `thm:kontsevich-formality-feynman` | `theorem` | `ProvedElsewhere` | 290 | 0 | 1 | Kontsevich formality |
| `prop:compactified-ternary-two-channel` | `proposition` | `ProvedHere` | 426 | 0 | 0 | Two-channel reduction after compactifying the ternary packet |
| `prop:m04-standard-log-basis` | `proposition` | `ProvedHere` | 506 | 0 | 0 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `thm:loop-genus-formula` | `theorem` | `ProvedElsewhere` | 670 | 0 | 1 | Graph loop number and ribbon genus; {} \cite{costello-renormalization} |
| `thm:mk-tree-level` | `theorem` | `ProvedElsewhere` | 924 | 1 | 0 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure-vol1` | `theorem` | `ProvedHere` | 947 | 5 | 1 | Formal all-genus stable-graph expansion |
| `prop:feyn-nekrasov-self-dual` | `proposition` | `ProvedElsewhere` | 1674 | 1 | 0 | Self-dual AGT block on \texorpdfstring{$\Sigma_{0,24}$}{Sigma 0,24} |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (36)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | `ProvedHere` | 120 | 6 | 0 | Protected dual transform and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | `ProvedHere` | 228 | 4 | 0 | Protected transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | `ProvedHere` | 281 | 2 | 0 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | `ProvedHere` | 322 | 4 | 0 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | `ProvedHere` | 376 | 1 | 0 | Scalar fixed-point rigidity on a full scalar package and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | `ProvedHere` | 490 | 1 | 0 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | `ProvedHere` | 603 | 1 | 0 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | `ProvedHere` | 721 | 1 | 0 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | `ProvedHere` | 792 | 5 | 0 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | `ProvedHere` | 924 | 5 | 0 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | `ProvedHere` | 1004 | 1 | 0 | The first nonlinear holographic anomaly |
| `prop:pva-degree-constraint` | `proposition` | `ProvedElsewhere` | 2209 | 0 | 1 | PVA degree constraint and the inevitability of $2{+}1$ dimensions |
| `thm:collision-depth-2-ybe` | `theorem` | `ProvedHere` | 2522 | 2 | 0 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `cor:shadow-connection-heisenberg` | `corollary` | `ProvedElsewhere` | 2604 | 1 | 0 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | `ProvedHere` | 2625 | 2 | 0 | Shadow connection for Virasoro and BPZ on the degenerate-representation surface |
| `comp:holographic-ss-vir` | `computation` | `ProvedHere` | 2796 | 1 | 0 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | `ProvedHere` | 2840 | 1 | 0 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | `ProvedHere` | 2863 | 1 | 0 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | `ProvedHere` | 2948 | 1 | 0 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | `ProvedHere` | 2978 | 0 | 0 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | `ProvedHere` | 3018 | 1 | 0 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | `ProvedHere` | 3109 | 0 | 0 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | `ProvedHere` | 3168 | 0 | 0 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | `ProvedHere` | 3264 | 1 | 0 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | `ProvedHere` | 3307 | 0 | 0 | Holographic datum for $\mathcal W_3$ |
| `cor:critical-dimensions` | `corollary` | `ProvedHere` | 3546 | 0 | 0 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | `ProvedHere` | 3657 | 1 | 0 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | `ProvedHere` | 3681 | 0 | 0 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | `ProvedHere` | 3717 | 0 | 0 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | `ProvedHere` | 3742 | 0 | 0 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | `ProvedHere` | 3854 | 1 | 0 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | `ProvedHere` | 3989 | 0 | 0 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | `ProvedHere` | 4164 | 0 | 0 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | `ProvedHere` | 4288 | 0 | 0 | Lifts as relative MC elements |
| `cor:holographic-deformation-cohomology` | `corollary` | `ProvedElsewhere` | 4319 | 0 | 0 | — |
| `comp:burns-space-holographic-datum` | `computation` | `ProvedHere` | 5658 | 1 | 2 | Burns space holographic modular Koszul datum |

#### `chapters/connections/genus1_seven_faces.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:g1sf-b-cycle-monodromy` | `theorem` | `ProvedHere` | 1314 | 2 | 0 | $B$-cycle monodromy of the collision residue |
| `prop:g1sf-seven-K3-faces` | `proposition` | `ProvedElsewhere` | 1520 | 3 | 1 | Seven K3-genus-$1$ faces of $r(z)$ |

#### `chapters/connections/genus_complete.tex` (28)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:elliptic-bar` | `theorem` | `ProvedElsewhere` | 83 | 1 | 1 | Elliptic bar complex; {} \cite{FBZ04} |
| `thm:master-tower` | `theorem` | `ProvedHere` | 284 | 1 | 0 | Master tower of boundary residues |
| `thm:chain-modular-functor` | `theorem` | `ProvedHere` | 391 | 6 | 1 | Chain-level boundary-residue modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | `ProvedHere` | 478 | 1 | 0 | Verdier-dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | `ProvedHere` | 787 | 3 | 0 | Bar complex defines tautological moduli integrals |
| `thm:poincare-extended` | `theorem` | `ProvedElsewhere` | 889 | 2 | 2 | Poincaré--Verdier duality for genus pieces; {} \cite{BD04,FG12} |
| `prop:bulk-from-boundary` | `proposition` | `ProvedElsewhere` | 955 | 0 | 3 | Algebraic open--closed bulk from the boundary; {} \cite{BD04,FG12,CG17} |
| `prop:sewing-universal-property` | `proposition` | `ProvedHere` | 1573 | 0 | 0 | Universal property of the sewing envelope |
| `prop:hs-trace-class` | `proposition` | `ProvedHere` | 1612 | 1 | 0 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | `ProvedHere` | 1627 | 0 | 0 | General HS-sewing criterion |
| `cor:hs-sewing-standard-landscape` | `corollary` | `ProvedElsewhere` | 1664 | 0 | 0 | Standard landscape |
| `cor:hs-implies-gram` | `corollary` | `ProvedHere` | 1702 | 2 | 0 | — |
| `thm:heisenberg-one-particle-sewing` | `theorem` | `ProvedHere` | 1721 | 0 | 2 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | `ProvedHere` | 1798 | 1 | 0 | Finite-window conilpotency and completed pro-conilpotency |
| `thm:dirichlet-weight-formula` | `theorem` | `ProvedHere` | 2104 | 0 | 0 | — |
| `cor:virasoro-mode-removal` | `corollary` | `ProvedHere` | 2161 | 2 | 0 | — |
| `thm:euler-koszul-criterion` | `theorem` | `ProvedHere` | 2220 | 2 | 0 | — |
| `comp:euler-koszul-defect-table` | `computation` | `ProvedHere` | 2257 | 2 | 0 | Euler--Koszul defect table for the standard landscape |
| `prop:zeta-zeros-defect-derivative` | `proposition` | `ProvedHere` | 2349 | 0 | 0 | — |
| `thm:li-closed-form` | `theorem` | `ProvedHere` | 2389 | 0 | 0 | — |
| `thm:li-asymptotics` | `theorem` | `ProvedHere` | 2423 | 2 | 0 | First Li coefficient and finite sign computation |
| `thm:surface-moment-positivity` | `theorem` | `ProvedHere` | 2563 | 0 | 0 | Gram positivity |
| `cor:virasoro-gram-ratio` | `corollary` | `ProvedHere` | 2586 | 0 | 0 | Virasoro sewing deficit |
| `thm:sewing-rkhs` | `theorem` | `ProvedHere` | 2628 | 2 | 0 | Sewing RKHS |
| `prop:collapse-permanence` | `proposition` | `ProvedHere` | 2699 | 3 | 0 | Collapse permanence |
| `prop:benjamin-chang-bridge` | `proposition` | `ProvedHere` | 2739 | 0 | 1 | — |
| `thm:euler-koszul-tier-classification` | `theorem` | `ProvedHere` | 2905 | 1 | 0 | — |
| `thm:sewing-hecke-reciprocity` | `theorem` | `ProvedHere` | 2986 | 4 | 0 | Diagonal Sewing--Hecke reciprocity |

#### `chapters/connections/grand_unification_platonic.tex` (10)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:grand-unification-platonic` | `theorem` | `ProvedHere` | 99 | 3 | 2 | Grand Unification, chiral bar--cobar |
| `cor:gu-theorem-a-platonic` | `corollary` | `ProvedHere` | 208 | 3 | 0 | Theorem~A is the adjunction itself |
| `cor:gu-theorem-b-platonic` | `corollary` | `ProvedHere` | 225 | 2 | 0 | Theorem~B is Positselski localisation |
| `cor:gu-theorem-c-platonic` | `corollary` | `ProvedHere` | 240 | 4 | 0 | Theorem~C is the scalar invariant of the double |
| `cor:gu-theorem-d-platonic` | `corollary` | `ProvedHere` | 264 | 4 | 0 | Theorem~D is obstruction-tower universality |
| `cor:gu-theorem-h-platonic` | `corollary` | `ProvedHere` | 281 | 4 | 0 | Theorem~H is Hochschild concentration |
| `cor:gu-L1-platonic` | `corollary` | `ProvedHere` | 304 | 2 | 0 | L1; chain-level ensemble via genus-$g$ trace |
| `cor:gu-L3-platonic` | `corollary` | `ProvedHere` | 369 | 1 | 3 | L3; $(\infty,1)$-categorical adjunction |
| `prop:L1-trace-identity-platonic` | `proposition` | `ProvedHere` | 470 | 3 | 1 | L1 trace identity |
| `thm:pr-alpha-X-local-global` | `theorem` | `ProvedHere` | 879 | 1 | 7 | Local-global gluing of $\mathrm{pr}_{\alpha_X}$ |

#### `chapters/connections/holographic_datum_master.tex` (4)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:hdm-face-3` | `theorem` | `ProvedHere` | 524 | 2 | 0 | Face~3: Khan--Zeng PVA \textup{(}genus~$0$ only\textup{)} |
| `thm:hdm-face-6` | `theorem` | `ProvedHere` | 813 | 2 | 1 | Face~6: Sklyanin bracket; \ (identification with classical limit of collision residue); \ (Sklyanin bracket: Semenov-Tian-Shansky 1983) |
| `rem:hdm-minfty-free-field-points` | `remark` | `ProvedHere` | 3828 | 0 | 0 | Free-boson $c=1$ and free-fermion $c=-2$ realisations |
| `thm:hdm-hbar-three-identification` | `theorem` | `ProvedElsewhere` | 4320 | 0 | 1 | Three-parameter $\hbar$ identification |

#### `chapters/connections/semistrict_modular_higher_spin_w3.tex` (16)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:finite-degree-polynomial-pva-chapter` | `theorem` | `ProvedHere` | 101 | 0 | 1 | Finite-degree theorem for polynomial PVAs |
| `cor:semistrictity-classical-W3-chapter` | `corollary` | `ProvedHere` | 139 | 1 | 1 | Semistrictity of the classical $W_3$ bulk |
| `prop:tree-identity-semistrict-chapter` | `proposition` | `ProvedHere` | 157 | 1 | 0 | Tree identity for semistrict cyclic theories |
| `prop:canonical-central-hodge-shadow-lift-chapter` | `proposition` | `ProvedHere` | 250 | 0 | 0 | Canonical central Hodge-shadow lift |
| `prop:clutching-duality-shadow-lift-chapter` | `proposition` | `ProvedHere` | 283 | 0 | 0 | Clutching additivity and duality symmetry |
| `thm:fiber-decomposition-shadow-base-point-chapter` | `theorem` | `ProvedHere` | 325 | 0 | 0 | Fiber decomposition over the shadow base point |
| `cor:shadow-centered-reduction-chapter` | `corollary` | `ProvedHere` | 353 | 1 | 0 | Shadow-centered reduction |
| `thm:finite-degree-convolution-chapter` | `theorem` | `ProvedHere` | 388 | 0 | 0 | Finite-degree convolution theorem |
| `thm:quadratic-cubic-twisting-theorem-chapter` | `theorem` | `ProvedHere` | 440 | 1 | 0 | Quadratic-cubic twisting theorem |
| `prop:admissibility-finite-slices-chapter` | `proposition` | `ProvedHere` | 515 | 0 | 0 | Admissibility and finite-dimensional weight slices |
| `thm:cubic-weight-recursion-chapter` | `theorem` | `ProvedHere` | 538 | 4 | 0 | Cubic weight recursion around the shadow base point |
| `cor:cubic-obstruction-classes-chapter` | `corollary` | `ProvedHere` | 569 | 1 | 0 | Cubic obstruction classes |
| `prop:stable-graph-identity-chapter` | `proposition` | `ProvedHere` | 582 | 1 | 0 | Stable-graph identity for semistrict modular theories |
| `prop:well-definedness-completed-boundary-model-chapter` | `proposition` | `ProvedHere` | 636 | 2 | 0 | Well-definedness of the completed boundary model |
| `thm:main-semistrict-modular-higher-spin-package-chapter` | `theorem` | `ProvedHere` | 666 | 8 | 0 | Main Theorem: the classical $W_3$ sector defines a semistrict modular higher-spin package |
| `cor:platonic-reduction-W3-frontier` | `corollary` | `ProvedHere` | 701 | 1 | 0 | Platonic reduction of the $W_3$ frontier |

#### `chapters/connections/subregular_hook_frontier.tex` (13)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:pbw-slodowy-collapse` | `theorem` | `ProvedHere` | 81 | 0 | 0 | PBW--Slodowy collapse |
| `cor:principal-w-completed-koszul` | `corollary` | `ProvedHere` | 140 | 1 | 0 | Principal affine \texorpdfstring{$W$}{W}-algebras are completed Koszul |
| `prop:transport-propagation` | `proposition` | `ProvedHere` | 256 | 0 | 0 | Transport propagation lemma |
| `prop:hook-ghost-constant` | `proposition` | `ProvedHere` | 330 | 0 | 0 | Hook ghost constant |
| `thm:canonical-degree-detection` | `theorem` | `ProvedHere` | 473 | 0 | 0 | Generator-degree detection of canonical degree |
| `thm:full-raw-coefficient-packet` | `theorem` | `ProvedHere` | 641 | 2 | 0 | Exact Bell recursion for the full singular packet |
| `thm:miura-product-formula` | `theorem` | `ProvedHere` | 799 | 0 | 0 | Subregular Miura product formula |
| `thm:subregular-appell-formula` | `theorem` | `ProvedHere` | 836 | 0 | 0 | Subregular Appell formula |
| `thm:bp-strict` | `theorem` | `ProvedHere` | 908 | 3 | 0 | Bershadsky--Polyakov is strict in canonical normal form |
| `thm:w4-cubic` | `theorem` | `ProvedHere` | 1132 | 2 | 0 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} has canonical degree $3$ |
| `thm:unbounded-canonical-degree` | `theorem` | `ProvedHere` | 1263 | 4 | 0 | Unbounded canonical degree in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | `ProvedHere` | 1317 | 0 | 0 | Triangular primary-renormalization theorem |
| `prop:nilpotent-transport-typeA` | `proposition` | `ProvedHere` | 1542 | 0 | 5 | Nilpotent transport for type $A$ |

#### `chapters/connections/thqg_entanglement_programme.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:thqg-barcobar-error-correction` | `proposition` | `ProvedHere` | 579 | 1 | 0 | Bar-cobar code structure |

#### `chapters/connections/thqg_introduction_supplement_body.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:thqg-intro-arnold-cybe` | `theorem` | `ProvedElsewhere` | 306 | 1 | 0 | Arnold $\Rightarrow$ CYBE |
| `thm:thqg-intro-quartic-linfty` | `theorem` | `ProvedElsewhere` | 341 | 1 | 0 | Quartic obstruction $=$ $L_\infty$ bracket |
| `prop:thqg-intro-flatness` | `proposition` | `ProvedElsewhere` | 460 | 0 | 0 | Flatness of the shadow connection |
| `thm:thqg-intro-operadic-complexity` | `theorem` | `ProvedElsewhere` | 893 | 1 | 0 | Operadic complexity; ; Theorem~\ref{thm:operadic-complexity} |
| `thm:thqg-intro-hs-general` | `theorem` | `ProvedElsewhere` | 1491 | 1 | 0 | General HS-sewing criterion |
| `thm:thqg-intro-heisenberg-sewing` | `theorem` | `ProvedElsewhere` | 1512 | 1 | 0 | Heisenberg sewing |

#### `chapters/connections/thqg_open_closed_realization.tex` (9)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:bd-algebraic-bridge` | `proposition` | `ProvedHere` | 113 | 3 | 1 | Bridge: BD chiral operad $\leftrightarrow$ algebraic $\mathcal{E}\!\mathit{nd}^{\mathrm{ch}}$ |
| `thm:thqg-brace-dg-algebra` | `theorem` | `ProvedHere` | 254 | 10 | 0 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | `ProvedHere` | 502 | 3 | 0 | Universal open/closed pair (chiral Swiss-cheese theorem) |
| `prop:mixed-sector-bulk-boundary` | `proposition` | `ProvedHere` | 600 | 2 | 0 | Mixed sector encodes bulk-to-boundary module structure |
| `thm:thqg-local-global-bridge` | `theorem` | `ProvedHere` | 667 | 7 | 0 | Local-global bridge |
| `thm:thqg-hochschild-register-separation` | `theorem` | `ProvedHere` | 788 | 8 | 0 | Separation of Hochschild, trace, THH, BV, and Koszul duality |
| `thm:thqg-annulus-trace` | `theorem` | `ProvedHere` | 922 | 11 | 5 | Annulus trace theorem |
| `thm:thqg-oc-mc-equation` | `theorem` | `ProvedHere` | 1302 | 2 | 0 | Open/closed MC equation |
| `prop:thqg-occ-CD-ANm1-24` | `proposition` | `ProvedHere` | 2128 | 0 | 0 | Chacaltana--Distler central charges for $\mathcal T\lbrack A_{N-1}, \Sigma_{0,24}\rbrack$ |

### Appendices (230)

#### `appendices/_sl2_yangian_insert.tex` (8)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `comp:ordered-bar-sl2` | `computation` | `ProvedHere` | 86 | 0 | 0 | Degree-$2$ ordered bar complex of $\widehat{\mathfrak{sl}}_2$ |
| `prop:ybe-from-d-squared` | `proposition` | `ProvedHere` | 164 | 1 | 0 | $d^2=0$ is the classical Yang--Baxter equation |
| `thm:yang-r-matrix` | `theorem` | `ProvedHere` | 227 | 0 | 0 | Yang $R$-matrix from the ordered bar complex |
| `thm:rtt-sl2` | `theorem` | `ProvedHere` | 302 | 5 | 0 | RTT presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:pbw-sl2` | `theorem` | `ProvedHere` | 420 | 0 | 0 | PBW basis of $Y_\hbar(\mathfrak{sl}_2)$ |
| `cor:hilbert-sl2` | `corollary` | `ProvedHere` | 456 | 1 | 0 | Hilbert series |
| `prop:eval-tensor-sl2` | `proposition` | `ProvedHere` | 502 | 1 | 0 | Tensor products and Yang--Baxter |
| `thm:sl2-koszul-dual` | `theorem` | `ProvedHere` | 533 | 7 | 0 | Open-colour Koszul dual of $\widehat{\mathfrak{sl}}_2$ is $Y_\hbar(\mathfrak{sl}_2)$ |

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
| `thm:concrete-bar-cobar` | `theorem` | `ProvedElsewhere` | 48 | 1 | 1 | Concrete bar-cobar equivalence \cite{LV12} |
| `thm:abstract-rh` | `theorem` | `ProvedElsewhere` | 92 | 0 | 1 | Abstract Riemann--Hilbert \cite{KS90} |
| `thm:geometric-infty-operads` | `theorem` | `ProvedHere` | 158 | 0 | 0 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |

#### `appendices/hochschild_conventions.tex` (1)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `prop:hochschild-crosswalk` | `proposition` | `ProvedHere` | 26 | 7 | 0 | Three Hochschild theories: type signatures, scope, and comparison rules |

#### `appendices/homotopy_transfer.tex` (13)

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
| `thm:bar-cobar-htt` | `theorem` | `ProvedHere` | 524 | 4 | 0 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | `ProvedHere` | 618 | 1 | 1 | Trees as boundary strata |

#### `appendices/koszul_reference.tex` (6)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:genus-graded-mc-appendix` | `theorem` | `ProvedElsewhere` | 230 | 5 | 0 | Genus-graded MC elements parametrize deformations |
| `thm:essential-image-koszul` | `theorem` | `ProvedHere` | 381 | 3 | 0 | Essential image of the chiral bar-dual coalgebra |
| `lem:conilpotency-necessary` | `lemma` | `ProvedHere` | 468 | 0 | 0 | Algebraic and completed conilpotency |
| `lem:connectedness-augmentation` | `lemma` | `ProvedHere` | 507 | 0 | 0 | Connectedness characterizes augmentation |
| `thm:koszul-geom-rep` | `theorem` | `ProvedHere` | 539 | 3 | 0 | Bar-dual coalgebras are geometrically representable |
| `thm:curvature-central-appendix` | `theorem` | `ProvedHere` | 619 | 1 | 1 | Central curvature and internal strictness |

#### `appendices/nonlinear_modular_shadows.tex` (56)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:nms-mc-principle` | `theorem` | `ProvedHere` | 184 | 2 | 0 | Algebra structure $=$ Maurer--Cartan element |
| `prop:nms-five-component` | `proposition` | `ProvedHere` | 341 | 4 | 0 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | `ProvedHere` | 401 | 1 | 0 | Shadow obstruction tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | `ProvedHere` | 441 | 0 | 0 | Standard-family evaluations of the universal class |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | `ProvedHere` | 538 | 0 | 0 | Ambient complementarity in tangent form |
| `thm:nms-ambient-complementarity-fmp` | `theorem` | `ProvedElsewhere` | 562 | 1 | 0 | Ambient complementarity as a shifted symplectic formal moduli problem; {} {\normalfont (see Theorem~\ref{thm:ambient-complementarity-fmp})} |
| `thm:nms-cotangent-normal-form` | `theorem` | `ProvedHere` | 592 | 0 | 0 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | `ProvedHere` | 638 | 0 | 0 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | `ProvedHere` | 647 | 0 | 0 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | `ProvedHere` | 668 | 1 | 0 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | `ProvedHere` | 683 | 0 | 0 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | `ProvedHere` | 782 | 2 | 0 | Quartic shadow master equations |
| `prop:nms-quartic-closure-envelope` | `proposition` | `ProvedHere` | 934 | 0 | 0 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | `ProvedHere` | 964 | 0 | 0 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | `ProvedHere` | 984 | 0 | 0 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | `ProvedHere` | 1048 | 0 | 0 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | `ProvedHere` | 1072 | 0 | 0 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | `ProvedHere` | 1165 | 2 | 0 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | `ProvedHere` | 1210 | 1 | 0 | Weight-changing projection of the quartic contact |
| `cor:nms-betagamma-boundary-law` | `corollary` | `ProvedHere` | 1235 | 0 | 0 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | `ProvedHere` | 1252 | 3 | 0 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | `ProvedHere` | 1281 | 0 | 0 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | `ProvedHere` | 1330 | 0 | 0 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | `ProvedHere` | 1368 | 1 | 0 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | `ProvedHere` | 1396 | 0 | 0 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | `ProvedHere` | 1468 | 1 | 0 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | `ProvedHere` | 1528 | 1 | 0 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `thm:nms-w3-full-quartic-gram` | `theorem` | `ProvedHere` | 1593 | 1 | 0 | Full $\mathcal W_3$ quartic Gram determinant |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | `ProvedHere` | 1666 | 1 | 0 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | `ProvedHere` | 1684 | 0 | 0 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | `ProvedHere` | 1700 | 2 | 0 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | `ProvedHere` | 1809 | 1 | 0 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | `ProvedHere` | 1861 | 0 | 0 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | `ProvedHere` | 1885 | 2 | 0 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behavior` | `corollary` | `ProvedHere` | 1973 | 3 | 0 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | `ProvedHere` | 2046 | 0 | 0 | Functoriality and duality through quartic order |
| `thm:nms-all-degree-master-equation` | `theorem` | `ProvedHere` | 2179 | 2 | 0 | All-degree master equation |
| `cor:nms-quintic-master-equation` | `corollary` | `ProvedHere` | 2215 | 1 | 0 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | `ProvedHere` | 2237 | 5 | 0 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | `ProvedHere` | 2261 | 0 | 0 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | `ProvedHere` | 2280 | 3 | 0 | Finite termination for primitive archetypes |
| `prop:nms-genus-loop-properties` | `proposition` | `ProvedHere` | 2393 | 1 | 0 | Basic properties of the genus loop operator |
| `cor:nms-genus-one-hessian-correction` | `corollary` | `ProvedHere` | 2436 | 1 | 0 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | `ProvedHere` | 2461 | 0 | 0 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | `ProvedHere` | 2542 | 0 | 0 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-bipartite-complementarity` | `theorem` | `ProvedHere` | 2977 | 1 | 0 | Bipartite complementarity principle |
| `thm:nms-bipartite-vanishing` | `theorem` | `ProvedHere` | 3089 | 1 | 0 | Bipartite vanishing theorem |
| `thm:reduced-weight-finiteness` | `theorem` | `ProvedHere` | 3438 | 1 | 0 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | `ProvedHere` | 3526 | 1 | 0 | Window locality |
| `cor:exact-stabilization` | `corollary` | `ProvedHere` | 3548 | 1 | 0 | Exact stabilization |
| `lem:nms-euler-inversion` | `lemma` | `ProvedHere` | 3724 | 1 | 0 | Euler inversion |
| `prop:kac-shadow-singularity` | `proposition` | `ProvedHere` | 3811 | 1 | 0 | Kac-shadow singularity principle |
| `thm:shadow-subalgebra-autonomy` | `theorem` | `ProvedHere` | 4130 | 4 | 0 | Shadow subalgebra autonomy |
| `cor:w-line-alternating-vanishing` | `corollary` | `ProvedHere` | 4206 | 1 | 0 | $W$-line alternating vanishing |
| `thm:nms-mc-moduli-curve-structure` | `theorem` | `ProvedHere` | 4408 | 1 | 0 | MC moduli curve structure |
| `cor:nms-mc-solution-counting` | `corollary` | `ProvedHere` | 4518 | 0 | 0 | MC solution counting |

#### `appendices/ordered_associative_chiral_kd.tex` (94)

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
| `prop:ordered-real-config-topology` | `proposition` | `ProvedHere` | 1737 | 0 | 0 | Topology of ordered real configurations |
| `lem:deconcatenation-coderivation` | `lemma` | `ProvedHere` | 2061 | 0 | 0 | Coderivation compatibility |
| `thm:heisenberg-ordered-bar` | `theorem` | `ProvedHere` | 2239 | 1 | 0 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | `ProvedHere` | 2353 | 0 | 0 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | `ProvedHere` | 2418 | 0 | 0 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | `ProvedHere` | 2474 | 0 | 0 | Formality: class~G, shadow depth~$2$ |
| `thm:bg-ordered-bar` | `theorem` | `ProvedHere` | 2589 | 0 | 0 | Free-field ordered bar complexes |
| `thm:wakimoto-ordered-bar` | `theorem` | `ProvedHere` | 2667 | 1 | 0 | Wakimoto bar complex descent |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | `ProvedHere` | 2767 | 1 | 0 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | `ProvedHere` | 2833 | 1 | 0 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | `ProvedHere` | 2893 | 2 | 0 | Ordered Koszul dual of lattice algebras |
| `thm:drinfeld-yangian-sl2` | `theorem` | `ProvedHere` | 2995 | 6 | 0 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | `ProvedHere` | 3085 | 0 | 0 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | `ProvedHere` | 3121 | 3 | 0 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | `ProvedHere` | 3173 | 3 | 0 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | `ProvedHere` | 3214 | 7 | 0 | Classical limit |
| `prop:vir-collision-residue` | `proposition` | `ProvedHere` | 3303 | 2 | 0 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | `ProvedHere` | 3333 | 1 | 0 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | `ProvedHere` | 3360 | 0 | 0 | Gravitational Yangian collapse |
| `thm:vir-non-formality` | `theorem` | `ProvedHere` | 3427 | 0 | 0 | Virasoro non-formality |
| `prop:grav-yangian-curvature` | `proposition` | `ProvedHere` | 3473 | 0 | 0 | Gravitational Yangian curvature |
| `cor:gauge-gravity-dichotomy-ordered` | `corollary` | `ProvedHere` | 3507 | 2 | 0 | Gauge-gravity complexity dichotomy |
| `thm:central-extension-invisible` | `theorem` | `ProvedHere` | 3603 | 0 | 0 | Central extension is invisible to the open-colour double bar |
| `thm:two-colour-double-kd` | `theorem` | `ProvedHere` | 3669 | 1 | 0 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | `ProvedHere` | 3703 | 2 | 0 | Non-redundancy of the two colours |
| `thm:km-yangian` | `theorem` | `ProvedHere` | 3785 | 4 | 0 | Universal Kac--Moody Yangian theorem |
| `thm:root-space-one-dim-v1` | `theorem` | `ProvedHere` | 4110 | 0 | 0 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | `ProvedHere` | 4159 | 1 | 0 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | `ProvedHere` | 4225 | 0 | 0 | Dynkin coefficient via the beta integral |
| `thm:complete-strictification-v1` | `theorem` | `ProvedHere` | 4306 | 3 | 0 | Complete strictification for all simple Lie algebras |
| `thm:sl3-triangle-coefficient` | `theorem` | `ProvedHere` | 4537 | 0 | 0 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | `ProvedHere` | 4621 | 0 | 0 | Serre relations from root-space vanishing |
| `thm:sl3-rtt` | `theorem` | `ProvedHere` | 4672 | 4 | 0 | RTT presentation for $Y_\hbar(\mathfrak{sl}_3)$ from the ordered bar complex |
| `thm:sl3-strictification` | `theorem` | `ProvedHere` | 4745 | 2 | 0 | Vanishing of the spectral Drinfeld class for $\mathfrak{sl}_3$ |
| `thm:sl4-quadrilateral` | `theorem` | `ProvedHere` | 4817 | 1 | 0 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:B2-ordered-bar` | `theorem` | `ProvedHere` | 4904 | 1 | 0 | Ordered bar complexes and Yangian $R$-matrices for rank-$2$ non-$A$ types |
| `thm:b-cycle-quantum-group` | `theorem` | `ProvedHere` | 5217 | 1 | 0 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | `ProvedHere` | 5342 | 2 | 0 | Drinfeld--Kohno; {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | `ProvedHere` | 5423 | 0 | 0 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | `ProvedHere` | 5488 | 0 | 0 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | `ProvedHere` | 5529 | 1 | 0 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | `ProvedHere` | 5692 | 0 | 0 | Ordered pole-depth spectrum |
| `thm:ordered-AOS` | `theorem` | `ProvedHere` | 5751 | 2 | 0 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | `ProvedHere` | 5830 | 1 | 0 | Averaging and surplus |
| `thm:FG-shadow-vol2` | `theorem` | `ProvedElsewhere` | 6121 | 0 | 0 | Comm\-utator-shadow theorem |
| `thm:ordered-associative-modular-mc` | `theorem` | `ProvedElsewhere` | 6204 | 0 | 0 | Associative modular Maurer--Cartan class |
| `thm:ordered-associative-ds-principal` | `theorem` | `ProvedElsewhere` | 6244 | 0 | 0 | Reduction commutes with associative chiral duality \textup{(}principal case\textup{)} |
| `thm:class-m-ds-transport` | `theorem` | `ProvedHere` | 6464 | 1 | 0 | Class~M persistence under DS transport |
| `thm:unshifted-identification` | `theorem` | `ProvedHere` | 6694 | 1 | 0 | Unshifted identification |
| `thm:factorisation-identification` | `theorem` | `ProvedHere` | 6738 | 0 | 0 | Factorisation identification on the Koszul locus |
| `prop:r-matrix-stable-envelope` | `proposition` | `ProvedHere` | 6783 | 0 | 0 | $R$-matrix comparison |
| `comp:sl2-eval` | `computation` | `ProvedHere` | 6927 | 0 | 0 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | `ProvedHere` | 6971 | 0 | 0 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | `ProvedHere` | 7019 | 1 | 0 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | `ProvedHere` | 7061 | 0 | 0 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | `ProvedHere` | 7096 | 0 | 0 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `thm:drinfeld-classification` | `theorem` | `ProvedElsewhere` | 7125 | 0 | 0 | Drinfeld classification |
| `prop:eval-drinfeld` | `proposition` | `ProvedHere` | 7148 | 0 | 0 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | `ProvedHere` | 7215 | 2 | 0 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | `ProvedHere` | 7276 | 0 | 0 | Braiding from the $R$-matrix |
| `thm:grothendieck-yangian` | `theorem` | `ProvedElsewhere` | 7321 | 0 | 0 | Grothendieck ring of Yangian modules |
| `thm:annular-bar-differential` | `theorem` | `ProvedHere` | 7432 | 1 | 0 | Annular bar differential |
| `thm:annular-HH` | `theorem` | `ProvedHere` | 7525 | 3 | 0 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | `ProvedHere` | 7625 | 1 | 0 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:elliptic-spectral-dichotomy` | `theorem` | `ProvedHere` | 7784 | 2 | 0 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `prop:r-matrix-eigenvalue` | `proposition` | `ProvedHere` | 7987 | 0 | 0 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | `ProvedHere` | 8003 | 1 | 0 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | `ProvedHere` | 8159 | 1 | 0 | $\mathsf{E}_1$ ordered bar landscape |

#### `appendices/q_convention_bridge_appendix.tex` (2)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:q-convention-bridge-main` | `theorem` | `ProvedHere` | 74 | 0 | 0 | Q-convention bridge |
| `thm:q-bridge-cocycle` | `theorem` | `ProvedHere` | 276 | 0 | 0 | Q-bridge as Z/2-cover cocycle |

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

#### `appendices/spectral_higher_genus.tex` (3)

| Label | Env | Status | Line | Refs | Cites | Title |
|---|---|---|---:|---:|---:|---|
| `thm:convergence-criterion-spectral` | `theorem` | `ProvedHere` | 73 | 0 | 0 | Convergence criterion |
| `thm:degeneration-special-c` | `theorem` | `ProvedElsewhere` | 104 | 0 | 2 | Degeneration at \texorpdfstring{$E_2$}{E2} \cite{FLM88, FBZ04} |
| `thm:bar-spectral-sequence-config` | `theorem` | `ProvedElsewhere` | 156 | 1 | 1 | Bar spectral sequence \cite{BD04} |
