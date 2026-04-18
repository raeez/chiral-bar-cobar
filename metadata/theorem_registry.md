# Theorem Registry

Auto-generated on 2026-04-18 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2699 |
| Total tagged claims | 3566 |
| Active files in `main.tex` | 130 |
| Total `.tex` files scanned | 150 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2699 |
| `ProvedElsewhere` | 497 |
| `Conjectured` | 325 |
| `Conditional` | 15 |
| `Heuristic` | 27 |
| `Open` | 3 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 1152 |
| `proposition` | 906 |
| `corollary` | 382 |
| `lemma` | 125 |
| `computation` | 92 |
| `remark` | 37 |
| `calculation` | 3 |
| `conjecture` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 32 |
| Part I: Theory | 1402 |
| Part II: Examples | 715 |
| Part III: Connections | 334 |
| Appendices | 216 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus_modular_koszul.tex` | 269 |
| `chapters/connections/arithmetic_shadows.tex` | 122 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 113 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 97 |
| `chapters/theory/ordered_associative_chiral_kd.tex` | 90 |
| `appendices/ordered_associative_chiral_kd.tex` | 89 |
| `chapters/theory/higher_genus_complementarity.tex` | 81 |
| `chapters/examples/w_algebras.tex` | 70 |
| `appendices/nonlinear_modular_shadows.tex` | 69 |
| `chapters/theory/higher_genus_foundations.tex` | 67 |
| `chapters/examples/free_fields.tex` | 66 |
| `chapters/examples/yangians_computations.tex` | 59 |
| `chapters/examples/kac_moody.tex` | 55 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 54 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 53 |
| `chapters/theory/chiral_koszul_pairs.tex` | 53 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 50 |
| `chapters/theory/chiral_modules.tex` | 49 |
| `chapters/examples/yangians_foundations.tex` | 47 |
| `chapters/examples/lattice_foundations.tex` | 45 |

## Complete Proved Registry

### Frame (32)

#### `chapters/frame/guide_to_main_results.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `rem:guide-four-test-interface` | `remark` | 311 | The four-test interface |

#### `chapters/frame/heisenberg_frame.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 543 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 892 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 990 | Maurer--Cartan equation for Heisenberg |
| `prop:frame-drinfeld-classical-limit` | `proposition` | 2125 | Classical limit and vanishing check |
| `prop:frame-thesis-shadow-termination` | `proposition` | 2185 | Shadow tower termination for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2761 | $\mathfrak{sl}_2$ bar complex as $E_1$-chiral coassociative coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2833 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2882 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2965 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 3003 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 3931 | Odd current $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | 4835 | The Heisenberg center |

#### `chapters/frame/part_ii_platonic_introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:part-ii-quadrichotomy-coarse-projection` | `theorem` | 241 | Quadrichotomy is coarse projection of fingerprint |
| `thm:part-ii-fingerprint-complete-invariant` | `theorem` | 311 | Fingerprint is complete invariant of bar-complex structure |
| `thm:part-ii-motivic-purity-virasoro-r-le-8` | `theorem` | 372 | Motivic purity of $S_r(\Vir_c)$ through $r \le 8$ |
| `thm:part-ii-moonshine-via-fingerprint` | `theorem` | 506 | Moonshine via fingerprint twining |
| `prop:part-ii-higher-genus-fingerprint` | `proposition` | 623 | Higher-genus fingerprint |
| `thm:part-ii-platonic-completeness` | `theorem` | 677 | Platonic completeness of Part~II |

#### `chapters/frame/part_iii_platonic_introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:part-iii-landscape-as-moduli-stack` | `theorem` | 284 | Standard landscape as C-points of $\cM_{\ChirAlg}$ |
| `thm:part-iii-central-charge-is-emergent` | `theorem` | 328 | The central charge is a functional of the fingerprint |
| `thm:part-iii-rmatrix-emergent-from-pbw` | `theorem` | 386 | The classical r-matrix is determined by PBW and OPE data |
| `thm:part-iii-grt-orbit-structure` | `theorem` | 455 | $\GRT(\Q)$ acts on $\cM_{\ChirAlg}$ preserving the fingerprint stratification; the historical seven faces are $\Q$-rational orbit representatives |
| `thm:part-iii-atlas-completeness` | `theorem` | 509 | Every non-degenerate fingerprint vector is realized |
| `prop:part-iii-landscape-restated` | `proposition` | 719 | Standard landscape restated as moduli atlas |

#### `chapters/frame/part_iv_platonic_introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:part-iv-grt-torsor-of-bridges` | `theorem` | 361 | $\Face(\cA)$ is a $\GRT_1(\Q)$-torsor; nine $\Q$-rational orbit representatives |
| `thm:part-iv-universal-holography-unifies` | `theorem` | 448 | The holographic functor $\Phol$ unifies all Part~\ref{part:physics-bridges} bridges |
| `thm:part-iv-celestial-is-holographic-image` | `theorem` | 557 | Celestial factorization algebra is the Mellin-shadow image of $\Phol$; \ (internal identification); \ (celestial algebra construction: Pasterski--Shao--Strominger; Strominger $w_{1+\infty}$; Vol~II \texttt{V2-thm:uch-main}). Chain-level class-$M$ statement at $g \ge 1$ open, per Vol~II \texttt{V2-conj:uch-gravity-chain-level}. |
| `thm:part-iv-e-infinity-ladder` | `theorem` | 657 | — |
| `thm:part-iv-moonshine-via-holography` | `theorem` | 765 | Monster $V^\natural$ as holographic $\Z/2$-orbifold; Dijkgraaf--Witten vanishing; \ (holographic framing of the orbifold as $\Etwo$-topological structure on the orbifold chiral Hochschild complex); \ (construction of $V^\natural$ as $\Z/2$-orbifold of $V_{\Lambda_{24}}$: Frenkel--Lepowsky--Meurman; Monster denominator identity: Borcherds; genus-zero property of McKay--Thompson series: Gannon) |
| `prop:part-iv-bridges-restated` | `proposition` | 974 | Part~\ref{part:physics-bridges} restated as $\GRT_1(\Q)$-torsor of $\Phol$ |

#### `chapters/frame/programme_overview_platonic.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:programme-is-complete-on-nondegenerate-locus` | `theorem` | 443 | Programme completeness on the non-degenerate locus |

### Part I: Theory (1402)

#### `chapters/theory/algebraic_foundations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 1091 | Comparison: our approach vs GLZ |
| `prop:circ-associative` | `proposition` | 1183 | Associativity of the composition product |
| `thm:geometric-bridge` | `theorem` | 1671 | Geometric realization |
| `prop:orthogonal` | `proposition` | 1859 | Orthogonality |
| `prop:chirAss-self-dual` | `proposition` | 2301 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `thm:e1-chiral-notions-collapse` | `theorem` | 2388 | Collapse of $\Eone$-chiral notions on the Koszul locus |

#### `chapters/theory/all_tier_generating_function_platonic.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:all-tier-bivariate-generating-function` | `theorem` | 147 | \label{thm:all-tier-bivariate-generating-function}% Bivariate hypergeometric generating function for the Virasoro shadow tower |
| `thm:all-tier-laurent-stratification` | `theorem` | 267 | \label{thm:all-tier-laurent-stratification}% All-tier Laurent stratification of the Virasoro shadow tower at $c = \infty$ |
| `cor:tier-k-leading-coefficient` | `corollary` | 336 | \label{cor:tier-k-leading-coefficient}% Leading (highest-degree) coefficient of Tier-$K$ |
| `thm:tier-5-closed-form` | `theorem` | 382 | \label{thm:tier-5-closed-form}% Tier-5 closed form |
| `cor:tier-leading-denominator-pattern` | `corollary` | 450 | \label{cor:tier-leading-denominator-pattern}% Tier leading denominator pattern |
| `cor:tier-K-kummer-arithmetic` | `corollary` | 484 | \label{cor:tier-K-kummer-arithmetic}% Kummer-irregular content at fixed $r$, variable $K$ |
| `thm:all-tier-fuchsian-ode` | `theorem` | 527 | \label{thm:all-tier-fuchsian-ode}% Fuchsian ODE in $u$ for the bivariate generating function |
| `cor:three-disjoint-hz-iv-chains` | `corollary` | 631 | \label{cor:three-disjoint-hz-iv-chains}% Three disjoint independent-verification chains |
| `thm:all-tier-closed-form-proved` | `theorem` | 674 | \label{thm:all-tier-closed-form-proved}% All-tier closed form (consolidated ProvedHere) |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (113)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:curvature-central` | `theorem` | 280 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 385 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 535 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 604 | Conilpotency ensures convergence |
| `comp:virasoro-spectral-r-matrix` | `computation` | 777 | Virasoro spectral R-matrix on primary states |
| `lem:degree-cutoff` | `lemma` | 951 | Degree cutoff: finite MC equation at each stage |
| `thm:completed-bar-cobar-strong` | `theorem` | 969 | MC element lifts to the completed convolution algebra |
| `prop:standard-strong-filtration` | `proposition` | 1116 | Standard weight truncations and the induced bar filtration |
| `prop:mc4-reduction-principle` | `proposition` | 1237 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 1302 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 1339 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 1377 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 1426 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 1477 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 1540 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 1604 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 1640 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 1716 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 1813 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 1829 | Factorization-envelope criterion for principal stages |
| `cor:completion-closure-equivalence` | `corollary` | 1865 | Homotopy-categorical equivalence on the completion closure |
| `thm:coefficient-stability-criterion` | `theorem` | 1919 | Coefficient-stability criterion |
| `thm:completed-twisting-representability` | `theorem` | 1954 | Completed twisting representability |
| `thm:mc-twisting-closure` | `theorem` | 1977 | MC-twisting closure of the completion closure |
| `thm:uniform-pbw-bridge` | `theorem` | 2002 | Uniform PBW bridge from MC1 to MC4 |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 2108 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 2154 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 2189 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 2209 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 2227 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 2246 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 2288 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 2328 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 2368 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 2436 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 2478 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 2524 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 2586 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 2627 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 2699 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 2787 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 2813 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 2838 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 2892 | Stage-\texorpdfstring{$4$}{4} reduction to one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 2920 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 2957 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 2988 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 3030 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 3057 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 3087 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 3130 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 3165 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 3195 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 3212 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 3263 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 3325 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
| `cor:winfty-dual-candidate-construction` | `corollary` | 3364 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 3411 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} reduction on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 3450 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 3542 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 3573 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 3681 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 3729 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 3775 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 3802 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 3944 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 3981 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 4045 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 4100 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 4142 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 4236 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 4261 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 4300 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 4320 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 4358 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 4375 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 4398 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 4420 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 4436 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 4455 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 4485 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 4497 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 4510 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 4528 | Stage-\texorpdfstring{$5$}{5} mixed transport reduction to one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 4551 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 4582 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 4790 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 4808 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 4845 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 4881 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-network-collapse` | `corollary` | 5178 | Visible stage-\texorpdfstring{$5$}{5} local network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 5226 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 5451 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 5717 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 6035 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 6071 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 6132 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 6144 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 6252 | Bar complex as algebra over the modular operad |
| `cor:genus-expansion-converges` | `corollary` | 6553 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 6611 | Functoriality of bar construction |
| `thm:reconstruction-vs-duality` | `theorem` | 6719 | Reconstruction versus duality |
| `thm:recognition-koszul-pairs` | `theorem` | 6781 | Recognition theorem for finite chiral Koszul pairs |
| `thm:mixed-boundary-sseq` | `theorem` | 6836 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | 6860 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | 6908 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | 6937 | Universality |
| `prop:sugawara-contraction` | `proposition` | 6955 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | 7019 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | 7035 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | 7081 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | 7130 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | 7174 | Diagonal GKO transgression |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (54)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 373 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 595 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 963 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 1080 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1153 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1197 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1265 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1331 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1472 | Positselski equivalence for the chiral bar coalgebra |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1529 | Flat finite-type reduction on the completed-dual side |
| `thm:bar-cobar-platonic` | `theorem` | 1642 | Chiral bar--cobar duality, Platonic form |
| `cor:A-shriek-constructed` | `corollary` | 1730 | Constructed Koszul dual |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1789 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
| `lem:bar-cobar-associated-graded` | `lemma` | 2414 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 2440 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 2500 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 2554 | Genus-graded convergence |
| `prop:counit-qi` | `proposition` | 2672 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 2693 | Functoriality of bar-cobar inversion |
| `lem:complete-filtered-comparison` | `lemma` | 2777 | Complete filtered comparison lemma |
| `cor:completed-derived-equivalence` | `corollary` | 2878 | Completed derived equivalence |
| `thm:barr-beck-lurie-koszulness` | `theorem` | 2990 | Barr--Beck--Lurie characterization of chiral Koszulness |
| `thm:fh-concentration-koszulness` | `theorem` | 3092 | Factorization homology concentration |
| `thm:fm-boundary-acyclicity` | `theorem` | 3152 | FM boundary acyclicity |
| `prop:lagrangian-perfectness` | `proposition` | 3356 | Perfectness for the standard landscape |
| `cor:lagrangian-unconditional` | `corollary` | 3492 | Unconditional Lagrangian criterion for the standard landscape |
| `prop:bar-fh` | `proposition` | 3893 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 3971 | Cobar as factorization cohomology |
| `prop:subexponential-growth-automatic` | `proposition` | 4554 | Sub-exponential growth is automatic |
| `thm:ks-centrality` | `theorem` | 4778 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | 4821 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | 4872 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | 4907 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | 4953 | Quadratic frontier |
| `prop:eta-hessian-transfer` | `proposition` | 5047 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | 5083 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | 5133 | Admissible cyclic rigidity |
| `cor:ds-not-first-frontier` | `corollary` | 5168 | Drinfeld--Sokolov reductions remain one-channel in the semisimple admissible sector |
| `thm:classification-scalar-genera` | `theorem` | 5213 | Classification of scalar genera \textup{(}uniform-weight\textup{)} |
| `thm:platonic-hierarchy-log` | `theorem` | 5285 | Five-step hierarchy of the categorical logarithm |
| `prop:cech-two-element-strict` | `proposition` | 5801 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | 6129 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | 6189 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | 6225 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | 6247 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | 6345 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | 6393 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | 6416 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | 6461 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | 6492 | Repeated roots encode extension data |
| `thm:common-core-exact-sequences-inv` | `theorem` | 6539 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | 6571 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | 6645 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | 6685 | Explicit coprime-locus projectors |

#### `chapters/theory/bar_construction.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 377 | Bar construction as NAP homology |
| `lem:ddr-preserves-log` | `lemma` | 711 | $d_{\mathrm{form}}$ preserves logarithmic forms |
| `lem:sign-compatibility` | `lemma` | 923 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 1013 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 1195 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 1261 | Functoriality |
| `thm:stokes-config` | `theorem` | 1288 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 1383 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 1425 | Arnold relations |
| `comp:deg0` | `computation` | 1468 | Degree 0 |
| `comp:deg1-general` | `computation` | 1497 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1697 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1736 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1751 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1785 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1809 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1876 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1927 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1944 | Differential is coderivation |
| `lem:orientation` | `lemma` | 2037 | Orientation convention |
| `lem:residue-properties` | `lemma` | 2063 | Residue properties |
| `thm:three-bar-complexes` | `theorem` | 2135 | Three bar complexes and their inclusions |
| `thm:geometric-equals-operadic-bar` | `theorem` | 2352 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 2459 | Residue formula |
| `thm:bar-chiral` | `theorem` | 2641 | Bar complex is chiral |

#### `chapters/theory/chern_weil_level_shift_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:level-shift-universality` | `theorem` | 179 | Level-shift universality |
| `prop:shift-appears-universally` | `proposition` | 274 | Universal occurrence of $k + \hv$ |
| `thm:h-dual-coxeter-coincidence` | `theorem` | 363 | Dual Coxeter coincidence |
| `thm:trace-KZ-convention-bridge` | `theorem` | 446 | Trace--KZ convention bridge |
| `cor:ap126-healing-universal` | `corollary` | 547 | universal healing |

#### `chapters/theory/chiral_center_theorem.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:partial-comp-assoc` | `lemma` | 228 | Associativity of partial compositions |
| `prop:geometric-algebraic-hochschild` | `proposition` | 348 | Geometric--algebraic comparison for chiral Hochschild |
| `prop:pre-lie-chiral` | `proposition` | 669 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | 697 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | 718 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | 1422 | Chiral Deligne--Tamarkin |
| `prop:derived-center-explicit` | `proposition` | 1967 | Explicit derived center: Heisenberg, affine $\widehat{\mathfrak{sl}}_2$, Virasoro |
| `prop:chirhoch1-affine-km` | `proposition` | 2133 | Generic affine first chiral Hochschild group |
| `prop:chirhoch2-affine-km-general` | `proposition` | 2223 | Generic affine second chiral Hochschild group |
| `prop:gerstenhaber-sl2-bracket` | `proposition` | 2298 | Gerstenhaber bracket on $\ChirHoch^1(V_k(\mathfrak{sl}_2))$ |
| `prop:ds-chirhoch-compatibility` | `proposition` | 2425 | DS--ChirHoch compatibility |
| `prop:heisenberg-bv-structure` | `proposition` | 2566 | BV algebra structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)$ |
| `prop:annulus-trace-standard` | `proposition` | 2734 | Annulus trace for standard families |

#### `chapters/theory/chiral_climax_platonic.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:climax-vol1-platonic` | `theorem` | 465 | Vol~I Climax: two equations and four properties |
| `lem:pullback-presentation-nabla-platonic` | `lemma` | 567 | Pullback presentation of $\nabla(A)$ |
| `prop:cybe-equivalence-platonic` | `proposition` | 682 | CYBE equivalence |
| `cor:climax-drinfeld-kohno-platonic` | `corollary` | 716 | Drinfeld--Kohno from the climax |
| `cor:climax-verlinde-platonic` | `corollary` | 741 | Verlinde formula from the climax |
| `cor:climax-borcherds-platonic` | `corollary` | 771 | Borcherds product from the climax |
| `cor:climax-arnold-common-root-platonic` | `corollary` | 803 | Arnold $1969$ as common root |

#### `chapters/theory/chiral_hochschild_koszul.tex` (50)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 223 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 374 | chiral Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 412 | chiral Hochschild spectral sequence |
| `lem:hochschild-shift-computation` | `lemma` | 556 | Fulton--MacPherson collapse and chiral Hochschild duality shift |
| `lem:chiral-quadratic-koszul` | `lemma` | 657 | Quadratic-chiral Koszul transfer |
| `prop:fm-tower-collapse` | `proposition` | 769 | Configuration-space collapse via FM-formality spectral sequence |
| `prop:chirhoch-sharp-hilbert` | `proposition` | 1067 | Sharp bigraded Hilbert series of chiral Hochschild |
| `cor:chirhoch-heisenberg` | `corollary` | 1102 | Heisenberg chiral Hochschild concentration |
| `cor:chirhoch-affine-sl2` | `corollary` | 1129 | Affine $\mathfrak{sl}_{2}$ Hochschild total dimension |
| `cor:chirhoch-virasoro-hilbert` | `corollary` | 1157 | Virasoro Hochschild Hilbert series |
| `lem:chiral-homotopy-transport` | `lemma` | 1223 | Chiral transport of Shelton--Yuzvinsky contracting homotopy |
| `thm:hochschild-concentration-E1` | `theorem` | 1380 | Ordered-bar chiral Hochschild concentration via ordered FM and pure braid Orlik--Solomon |
| `cor:hochschild-averaging-symmetric` | `corollary` | 1438 | Averaging to symmetric ChirHoch |
| `lem:chirhoch-descent` | `lemma` | 1601 | Chiral Hochschild descent |
| `thm:main-koszul-hoch` | `theorem` | 1687 | Koszul duality for chiral Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `thm:hochschild-polynomial-growth` | `theorem` | 1814 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 2055 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `prop:e2-formality-hochschild` | `proposition` | 2096 | $\Etwo$-formality of chiral Hochschild cohomology |
| `thm:convolution-formality-one-channel` | `theorem` | 2176 | Scalar universal class implies convolution formality along its distinguished orbit |
| `thm:bifunctor-obstruction-decomposition` | `theorem` | 2371 | Bifunctor obstruction decomposition |
| `comp:boson-hochschild` | `computation` | 2587 | Boson chiral Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 2617 | Fermion chiral Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 2723 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 2817 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 2915 | Kac--Moody cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | 3122 | Genus truncation |
| `prop:hochschild-shadow-projection` | `proposition` | 3195 | Hochschild as degree-$2$ shadow projection |
| `thm:mc2-1-km` | `theorem` | 3224 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 3341 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 3588 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 3674 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 3793 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | 3975 | Strictification principle for modular deformation theory |
| `prop:d-mod-squared-zero` | `proposition` | 4110 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 4245 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 4419 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 4609 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 4735 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 4991 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 5147 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 5286 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 5371 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 5418 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 5716 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 5847 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 5894 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 6092 | $bc$/$\beta\gamma$ Koszul duality |
| `thm:gerstenhaber-structure` | `theorem` | 6116 | Chiral Gerstenhaber structure on $\ChirHoch^*$ |
| `prop:hochschild-cech-ss` | `proposition` | 6470 | chiral Hochschild--\v{C}ech spectral sequence |
| `prop:envelope-shadow` | `proposition` | 6908 | Factorization envelope shadow functor |

#### `chapters/theory/chiral_koszul_pairs.tex` (53)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 306 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 333 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 353 | Filtered comparison |
| `lem:filtered-comparison-unit` | `lemma` | 381 | Bar-side filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 432 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 508 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 788 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 866 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 921 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 965 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 1155 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1268 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1302 | Converse: chiral Koszulness implies formality |
| `thm:ext-diagonal-vanishing` | `theorem` | 1372 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1409 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1435 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1521 | Kac--Shapovalov criterion for simple quotients |
| `rem:admissible-koszul-status` | `remark` | 1592 | Status of admissible simple quotients |
| `prop:li-bar-poisson-differential` | `proposition` | 1947 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | 2018 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | 2120 | Nilradical obstruction at degenerate admissible levels |
| `thm:koszul-equivalences-meta` | `theorem` | 2372 | Equivalences and consequences of chiral Koszulness |
| `prop:koszul-closure-properties` | `proposition` | 3006 | Closure of chiral Koszulness under tensor, dualization, and base change |
| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 3106 | Swiss-cheese non-formality by shadow class |
| `prop:sc-formal-iff-class-g` | `proposition` | 3242 | SC-formality characterises class~$G$ |
| `prop:d-module-purity-km` | `proposition` | 3524 | $\cD$-module purity for affine Kac--Moody algebras |
| `prop:d-module-purity-km-equivalence` | `proposition` | 3560 | Kac--Moody equivalence via Saito--Kashiwara weight filtration |
| `prop:koszulness-formality-equivalence` | `proposition` | 3877 | Koszulness as formality of the convolution algebra |
| `thm:koszulness-from-sklyanin` | `theorem` | 4121 | Koszulness from Sklyanin--Poisson rigidity; {} for affine KM |
| `thm:koszulness-moduli-kp` | `theorem` | 4248 | Koszulness moduli |
| `thm:virasoro-koszulness-non-circular-kp` | `theorem` | 4364 | Virasoro Koszulness, non-circular |
| `thm:yangian-chart-inclusion-kp` | `theorem` | 4429 | Yangian chart inclusion |
| `thm:koszulness-bootstrap` | `theorem` | 4483 | Koszulness implies bootstrap closure |
| `prop:minimal-model-non-koszul` | `proposition` | 4541 | Minimal model non-Koszulness |
| `prop:cumulant-window-inversion` | `proposition` | 4739 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 4795 | Geometric bar--cobar duality |
| `prop:bar-cobar-relative-extension` | `proposition` | 4948 | Relative extension from relative Verdier base change |
| `thm:yangian-self-dual` | `theorem` | 5212 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 5272 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 5426 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 5520 | Bar computes Koszul dual, complete statement |
| `lem:completion-convergence` | `lemma` | 5608 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 5657 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 6244 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 6464 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:e1-module-koszul-duality` | `theorem` | 6588 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `prop:koszul-character-identity` | `proposition` | 6717 | Koszul character identity |
| `prop:bar-neq-quasiprimary` | `proposition` | 6753 | Bar cohomology $\neq$ quasi-primary count |
| `thm:structure-exchange` | `theorem` | 6932 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 6974 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 7020 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 7058 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 7267 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 179 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 284 | Module bar-comodule comparison on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `thm:monoidal-module-koszul` | `theorem` | 343 | Lax monoidal structure of the module bar functor |
| `prop:ext-tor-exchange` | `proposition` | 462 | Derived Ext exchange on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `prop:conformal-blocks-bar` | `proposition` | 541 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 646 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 747 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 805 | KZB connection from the bar complex |
| `prop:tilting-bar` | `proposition` | 1650 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1713 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1913 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1973 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 2007 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:logarithmic-bar` | `proposition` | 2252 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2346 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2466 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2501 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2540 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2557 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2597 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2619 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2769 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2881 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2995 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3074 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3228 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3259 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3316 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3406 | Vacuum Verma under the module bar functor on the finite-type \texorpdfstring{$\Eone$}{E1} lane |
| `prop:shapovalov-koszul` | `proposition` | 3510 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3569 | Non-vacuum Verma modules under the module bar functor on the finite-type \texorpdfstring{$\Eone$}{E1} lane |
| `cor:singular-vector-symmetry` | `corollary` | 3652 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3729 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3784 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3877 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3931 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3997` | `calculation` | 3997 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:4024` | `calculation` | 4024 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:4055` | `calculation` | 4055 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4173 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4298 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4348 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4472 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4514 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar at dual level via DS and Verdier intertwining |
| `thm:module-genus-tower` | `theorem` | 4670 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4712 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4854 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 5003 | Fusion product compatibility on the module bar surface |
| `prop:heisenberg-fusion-splitting` | `proposition` | 5124 | Heisenberg fusion splitting |

#### `chapters/theory/climax_theorem.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:climax-genus-zero` | `theorem` | 43 | Climax of Vol~I, genus-zero form |
| `cor:climax-drinfeld-kohno` | `corollary` | 124 | Drinfeld--Kohno along $A \mapsto U_q$ |
| `cor:climax-borcherds` | `corollary` | 141 | Borcherds along $A \mapsto V_\Lambda$ |
| `cor:climax-verlinde` | `corollary` | 157 | Verlinde along $A \mapsto \mathrm{RCFT}$ |

#### `chapters/theory/clutching_uniqueness_platonic.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:clutching-uniqueness-socle-projection` | `theorem` | 218 | Clutching uniqueness on the socle |
| `prop:obs-g-lower-degree-components` | `proposition` | 380 | Lower-degree components of the obstruction class |
| `cor:genus-2-explicit-match` | `corollary` | 537 | Explicit match at genus $2$ |
| `thm:H04-PTVV-alternative-disjoint` | `theorem` | 612 | Factorisation-homology derivation is disjoint from the tautological-ring path |

#### `chapters/theory/cobar_construction.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 322 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 383 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 416 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 498 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 574 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 694 | Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 964 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 1124 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1342 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1495 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1573 | Explicit cobar-bar augmentation |
| `prop:cobar-modular-shadow` | `proposition` | 1846 | Cobar as modular shadow carrier |
| `thm:cobar-free` | `theorem` | 1928 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1949 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 2078 | Topology |
| `thm:poincare-verdier` | `theorem` | 2137 | Bar-cobar Verdier pairing |
| `thm:curved-mc-cobar` | `theorem` | 2240 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 2265 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 2311 | Level-shifting via Verdier duality |
| `thm:central-charge-cocycle` | `theorem` | 2504 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2600 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2741 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2766 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2863 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2922 | Recognition principle |
| `lem:deformation-space` | `lemma` | 3351 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 3393 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 3441 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3521 | Curved differential formula |

#### `chapters/theory/coderived_models.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 251 | Adequacy |
| `prop:coderived-bar-degree-spectral-sequence` | `proposition` | 316 | Coderived bar-degree spectral sequence |
| `thm:stratified-conservative-restriction` | `theorem` | 670 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 746 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 796 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 823 | Factorization co-contra correspondence |
| `thm:off-koszul-ran-inversion` | `theorem` | 917 | Off-Koszul bar-cobar inversion on Ran |

#### `chapters/theory/compact_completed_mc3_comparison_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:compact-completed-mc3-comparison` | `theorem` | 129 | Compact/completed MC3 comparison |
| `prop:compact-approximation-exists` | `proposition` | 234 | Compact approximation exists |
| `thm:mc3-full-DK-in-completed-category` | `theorem` | 340 | MC3 thick generation in the completed category |
| `cor:comparison-gap-healed-completed` | `corollary` | 389 | Compact/completed comparison gap healed in completed ambient |
| `rem:status-table-comparison-gap-completed` | `remark` | 649 | Status table |

#### `chapters/theory/computational_methods.tex` (17)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:comp-algebraic-shadow` | `theorem` | 100 | Riccati algebraicity |
| `thm:comp-denom-pattern` | `theorem` | 176 | Denominator theorem |
| `prop:comp-shadow-connection-properties` | `proposition` | 226 | Properties of the shadow connection |
| `thm:comp-shadow-asymptotics` | `theorem` | 353 | Shadow asymptotics |
| `prop:comp-borel-summability` | `proposition` | 453 | Borel summability |
| `prop:comp-mc-recursion` | `proposition` | 503 | MC recursion |
| `thm:comp-alg-rec-equivalence` | `theorem` | 532 | Algebraic--recursive equivalence |
| `thm:comp-ds-consistency` | `theorem` | 599 | DS transfer consistency |
| `prop:comp-ce-bar` | `proposition` | 699 | CE reduction |
| `thm:comp-zhu-c-dependence` | `theorem` | 733 | $c$-dependence for simple quotients |
| `thm:comp-three-way-bar` | `theorem` | 826 | Three-way agreement for bar cohomology |
| `prop:comp-explicit-theta-sl2` | `proposition` | 864 | Explicit $\Theta$ for $\AffKM{sl}_2$ |
| `thm:comp-e8-three-way` | `theorem` | 1007 | $E_8$ genus-$2$ agreement |
| `prop:comp-n2-kappa` | `proposition` | 1159 | Modular characteristic |
| `prop:comp-n2-spectral-flow` | `proposition` | 1222 | Spectral flow invariance |
| `thm:comp-genus2-cross` | `theorem` | 1272 | Cross-consistency at genus~$2$ |
| `thm:s3-virasoro-c-independent` | `theorem` | 1510 | $c$-independence of $S_3$ for Virasoro |

#### `chapters/theory/configuration_spaces.tex` (37)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 433 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 553 | Normal crossings |
| `thm:closure-relations` | `theorem` | 648 | Closure relations |
| `thm:log-complex` | `theorem` | 765 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 803 | Arnold relations: flatness of $\nabla_{\mathrm{Arnold}}$ |
| `prop:arnold-higher-genus` | `proposition` | 902 | Higher-genus correction to the Arnold-only presentation |
| `prop:twisting-morphism-propagator` | `proposition` | 1195 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 1262 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 1329 | Residue operations |
| `prop:residue-local` | `proposition` | 1384 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 1469 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1747 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1820 | Conformal blocks from punctured bar complex |
| `thm:bordered-fm-properties` | `theorem` | 2238 | Properties of the bordered FM compactification |
| `prop:four-type-boundary` | `proposition` | 2337 | Four-type boundary decomposition |
| `thm:oc-convolution-dg-lie` | `theorem` | 2731 | dg~Lie structure on the open-closed convolution algebra |
| `thm:modular-mc-clutching` | `theorem` | 2979 | Modular MC equation with clutching |
| `cor:recovery-bar-intrinsic` | `corollary` | 3325 | Recovery of the bar-intrinsic MC element |
| `prop:eta` | `proposition` | 3515 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `lem:orientation-compatibility` | `lemma` | 3922 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 3983 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 4022 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 4049 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 4071 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 4111 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 4135 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 4170 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 4192 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 4226 | Residue evaluation complexity |
| `thm:arnold-orlik-solomon` | `theorem` | 4368 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 4414 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 4449 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 4494 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 4724 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 4794 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 4931 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5141` | `computation` | 5141 | Explicit examples |

#### `chapters/theory/conformal_anomaly_rigidity_platonic.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:casimir-nonvanishing` | `lemma` | 140 | Nonvanishing and integrality of $\Cas$ |
| `thm:conformal-anomaly-rigidity` | `theorem` | 183 | Conformal-anomaly rigidity |
| `thm:c-zero-coproduct-is-constant` | `theorem` | 240 | Coproduct is constant at $c = 0$ |
| `prop:spectral-parameter-forced-at-nonzero-c` | `proposition` | 275 | Spectral parameter is forced at $c \neq 0$ |
| `thm:universal-coefficient` | `theorem` | 299 | Universality of the coefficient |
| `cor:forbidden-c-0-locus-chiralization` | `corollary` | 339 | Chiralisation is obstructed away from $c = 0$ |

#### `chapters/theory/derived_langlands.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:langlands-bar-bridge` | `theorem` | 95 | Critical bar-to-oper bridge |
| `thm:oper-bar-h0-dl` | `theorem` | 321 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 356 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 380 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 417 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 498 | Differential analysis at degree 3 |
| `prop:d4-nonvanishing` | `proposition` | 578 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 637 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 650 | Full oper differential-form identification |
| `rem:critical-level-theta` | `remark` | 806 | The MC element $\Theta_{\cA}$ at critical level |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 1179 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/e1_modular_koszul.tex` (23)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | 227 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | 246 | — |
| `thm:e1-mc-element` | `theorem` | 343 | $E_1$ Maurer--Cartan element |
| `prop:e1-nonsplitting-obstruction` | `proposition` | 428 | $E_1$ non-splitting obstruction |
| `prop:e1-nonsplitting-genus1` | `proposition` | 533 | $E_1$ non-splitting at genus~$1$: quasi-modular obstruction |
| `prop:e1-shadow-r-matrix` | `proposition` | 819 | — |
| `prop:symmetric-descent` | `proposition` | 962 | Symmetric descent |
| `thm:e1-formality-bridge` | `theorem` | 1283 | Formality bridge |
| `thm:e1-formality-failure` | `theorem` | 1322 | Formality failure for genuinely $\Eone$-chiral algebras |
| `thm:e1-mc-finite-degree` | `theorem` | 1435 | $E_1$ MC equation at finite degree |
| `thm:e1-coinvariant-shadow` | `theorem` | 1506 | Coinvariant projection: $E_1$ shadows to $E_\infty$ shadows |
| `rem:ribbon-structure-count` | `remark` | 1557 | Ribbon structure count |
| `rem:fcom-fass-scalar-agreement` | `remark` | 1588 | $F\!\Com = F\!\Ass$ at the scalar level |
| `thm:e1-theorem-A-modular` | `theorem` | 1972 | Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction |
| `thm:e1-theorem-B-modular` | `theorem` | 2029 | Theorem~$\mathrm{B}^{E_1}$ at all genera: ordered bar--cobar inversion |
| `thm:e1-theorem-C-modular` | `theorem` | 2055 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
| `thm:e1-theorem-D-modular` | `theorem` | 2095 | Theorem~$\mathrm{D}^{E_1}$ at all genera: formal ordered degree-$2$ shadow series |
| `thm:e1-theorem-H-modular` | `theorem` | 2166 | Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered chiral Hochschild at genus~$g$ |
| `prop:sn-irrep-decomposition-bar` | `proposition` | 2373 | $\Sigma_n$-irreducible decomposition of the ordered bar complex |
| `lem:bare-graph-no-thooft` | `lemma` | 2482 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | 2503 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | 2545 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | 2567 | Exact $N^{\chi}$ weighting from traced open color |

#### `chapters/theory/e3_identification_chain_level_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:e3-identification-chain-level-associator-fixed` | `theorem` | 413 | Chain-level $\Ethree$-identification, $\Phi = \Phi_{\KZ}$ |
| `prop:associator-dependence-explicit` | `proposition` | 597 | Associator-dependence of the chain map |
| `thm:operad-level-to-algebra-level-lift` | `theorem` | 743 | Operad-level to algebra-level formality lift |
| `cor:e3-solvable-unconditional` | `corollary` | 871 | Chain-level identification for solvable~$\fg$ is unconditional |
| `prop:sl2-associator-test` | `proposition` | 1065 | $\mathfrak{sl}_2$ associator-test |

#### `chapters/theory/en_koszul_duality.tex` (40)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:en-chiral-bridge` | `theorem` | 153 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
| `prop:en-formality-mc-truncation` | `proposition` | 227 | Formality hierarchy as MC obstruction truncation |
| `prop:linking-sphere-residue` | `proposition` | 503 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 578 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 738 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 796 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:kappa-universality-en` | `proposition` | 924 | Kappa universality across $n$ |
| `prop:shadow-stabilization` | `proposition` | 950 | Shadow stabilization threshold |
| `prop:shadow-gc2-bridge` | `proposition` | 1141 | Shadow obstruction tower to $\mathrm{GC}_2$ bridge |
| `thm:bar-swiss-cheese` | `theorem` | 1400 | Bar complex as $\Eone$-chiral coassociative coalgebra |
| `prop:sc-koszul-dual-three-sectors` | `proposition` | 1703 | Koszul dual cooperad of \texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}: three sectors |
| `prop:operadic-center-existence` | `proposition` | 1846 | Existence of the operadic center |
| `thm:operadic-center-hochschild` | `theorem` | 1899 | The operadic center of $\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex |
| `thm:center-geometric-inevitability` | `theorem` | 2249 | Geometric inevitability of the chiral center |
| `prop:braces-from-center` | `proposition` | 2442 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | 2491 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | 2567 | Terminality of the center |
| `cor:center-functor` | `corollary` | 2656 | The center functor |
| `thm:topologization` | `theorem` | 3078 | Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}} |
| `thm:e-infinity-topologization` | `theorem` | 3219 | $E_\infty$-Topologization via iterated Sugawara |
| `cor:e-ladder-vir-wn-winfty` | `corollary` | 3243 | $E_n$ ladder specializations |
| `thm:e-infinity-topologization` | `theorem` | 3935 | $\Einf$-topologization master theorem |
| `cor:virasoro-N-2-climax` | `corollary` | 4185 | Virasoro ($N=2$) recovers the Volume~II climax |
| `cor:WN-E-Nplus1-top` | `corollary` | 4205 | $\cW_N$ gives $E_{N+1}$-topological |
| `cor:Winfty-Einf-top` | `corollary` | 4224 | $\cW_\infty$ gives $\Einf$-topological |
| `thm:coset-conformal-inheritance` | `theorem` | 4301 | Coset conformal inheritance |
| `prop:sugawara-gauge-rectification` | `proposition` | 4440 | Chain-level $\Ethree^{\mathrm{top}}$ for affine Kac--Moody via gauge rectification |
| `prop:e3-via-dunn` | `proposition` | 4915 | $\Ethree^{\mathrm{top}}$ via Dunn additivity, bypassing the Higher Deligne Conjecture |
| `lem:en-formality-deformation-classification` | `lemma` | 5248 | Formality reduction for $\En$-deformations of commutative algebras |
| `thm:e3-identification` | `theorem` | 5346 | Identification of $\Ethree$-deformation families |
| `prop:e3-explicit-sl2` | `proposition` | 5845 | Explicit $\Ethree$ operations on $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\mathfrak{sl}_2))$ |
| `prop:e3-ek-quantum` | `proposition` | 6227 | {$\Ethree$ operations on $Z^{\mathrm{der}}_{\mathrm{ch}}(V_{\mathrm{EK}})$} |
| `prop:chiral-p3-structure` | `proposition` | 6390 | The chiral $\Pthree$ structure |
| `thm:chiral-e3-structure` | `theorem` | 6477 | Structure of the chiral $\Ethree$-algebra |
| `lem:bv-p3-commutativity` | `lemma` | 6738 | Commutativity of the BV operator and the chiral $\Pthree$ bracket |
| `prop:chiral-e3-dmod` | `proposition` | 6879 | The $\cD$-module structure |
| `thm:chiral-e3-cfg` | `theorem` | 6965 | Formal disk restriction recovers CFG |
| `prop:khan-zeng-topological` | `proposition` | 7178 | Topological enhancement via Sugawara |
| `thm:en-shadow-tower` | `theorem` | 7591 | $\En$ shadow obstruction tower: universality of $\kappa$ and formality collapse |
| `prop:e3-bar-structure` | `proposition` | 7765 | $\Etwo$ structure on the bar complex and the $\mathsf{E}_3$ obstruction |

#### `chapters/theory/existence_criteria.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:classification-table` | `proposition` | 453 | Classification table \cite{FBZ04, BD04} |
| `prop:w-algebra-koszul` | `proposition` | 553 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul analysis |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 16 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 171 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 58 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 115 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 224 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 270 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 319 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 348 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 408 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 435 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 492 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 550 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 630 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 800 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 821 | — |
| `thm:fourier-specialization` | `theorem` | 863 | Specialization |

#### `chapters/theory/ftm_seven_fold_tfae_platonic.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ftm-seven-fold-tfae-via-hub-spoke` | `theorem` | 167 | Six-fold TFAE on the Koszul locus, with a class-$G$ seventh equivalence |
| `cor:ftm-seventh-class-G` | `corollary` | 217 | Seventh (SC-formality) equivalence on class~$G$ |
| `prop:ftm-spoke-koszul-pbw` | `proposition` | 235 | Spoke 1 |
| `prop:ftm-spoke-counit-pbw` | `proposition` | 260 | Spoke 2 |
| `prop:ftm-spoke-unit-pbw` | `proposition` | 291 | Spoke 3 |
| `prop:ftm-spoke-ttacyclic-pbw` | `proposition` | 317 | Spoke 4 |
| `prop:ftm-spoke-bar-conc-pbw` | `proposition` | 358 | Spoke 5 |
| `prop:ftm-spoke-sc-pbw` | `proposition` | 401 | Spoke 6, parametrised |
| `prop:no-tautology-at-g0` | `proposition` | 439 | Non-tautology at genus zero |
| `cor:TFAE-extends-to-genus-1-uniform-weight` | `corollary` | 515 | Genus extension of each spoke |
| `prop:class-L-witness` | `proposition` | 635 | Class-$L$ witness |
| `rem:kac-moody-filtered-comparison` | `remark` | 675 | Kashiwara filtration on the Kac--Moody vacuum module |

#### `chapters/theory/genus_2_ddybe_platonic.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:g2-face-model-bypass-scope-restricted` | `theorem` | 383 | Face-model DDYBE, scope-restricted |
| `cor:g2-chi-minus-12` | `corollary` | 659 | $\chi=-12$ from rank-$4$ KZB local system |

#### `chapters/theory/higher_genus_complementarity.tex` (81)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:involution-splitting` | `lemma` | 251 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 306 | Perfectness criterion for the strict flat relative bar family |
| `thm:fiber-center-identification` | `theorem` | 389 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 541 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 787 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 842 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 933 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 996 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 1052 | Flat fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 1098 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 1171 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 1211 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 1265 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1301 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 1491 | Verdier involution on moduli cohomology |
| `lem:center-isomorphism` | `lemma` | 1526 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 1579 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 1692 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 1723 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 1743 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 1849 | Verdier pairing and Lagrangian eigenspaces |
| `lem:bar-chart-lagrangian-lift` | `lemma` | 1947 | Bar chart transport of the ambient Lagrangian polarization |
| `prop:ptvv-lagrangian` | `proposition` | 2195 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 2268 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 2380 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 2408 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 2446 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 2489 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 2525 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 2556 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 2807 | Fermion-boson Koszul duality |
| `prop:complementarity-landscape` | `proposition` | 2986 | Complementarity landscape |
| `thm:BD-genus-zero` | `theorem` | 3322 | BD 3.4.12: genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 3372 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 3385 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 3427 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 3486 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 3526 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 3554 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 3576 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 3620 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 3814 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 3862 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 3950 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 3977 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 4005 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 4041 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 4068 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 4129 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 4175 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 4214 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 4243 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 4271 | Algebra structure from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 4299 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 4331 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 4380 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 4406 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 4422 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 4532 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 4610 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 4658 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 4747 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | 4922 | Ambient complementarity in tangent form |
| `thm:ambient-complementarity-fmp` | `theorem` | 4965 | Ambient complementarity as shifted symplectic formal moduli problem |
| `thm:lagrangian-complementarity-global-upgrade` | `theorem` | 5055 | Global Lagrangian complementarity across genera: clutching-coherent section of the Verdier-symplectic bundle on $\overline{\mathcal{M}}_{g,n}$; clauses~\textup{(i)--(iii)}~; clause~\textup{(iv)}~ |
| `thm:shifted-cotangent-normal-form` | `theorem` | 5398 | Shifted cotangent normal form |
| `prop:legendre-duality-potentials` | `proposition` | 5447 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | 5462 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | 5492 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | 5516 | Criterion for fake complementarity |
| `thm:holo-comp-bulk-reconstruction` | `theorem` | 5712 | Protected dual transform |
| `thm:holo-comp-cotangent-realization` | `theorem` | 5762 | Shifted cotangent realization |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | 5789 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | 5875 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | 5919 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | 5996 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | 6079 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | 6148 | First nonlinear holographic anomaly |
| `thm:critical-dimension` | `theorem` | 6258 | Critical dimension |
| `prop:non-critical-liouville` | `proposition` | 6427 | Non-critical complementarity and the Liouville sector |
| `cor:complementarity-discriminant-cancellation` | `corollary` | 6472 | Degree-$4$ discriminant cancellation |

#### `chapters/theory/higher_genus_foundations.tex` (67)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:gauss-manin-uncurving-chain` | `proposition` | 369 | Gauss--Manin uncurving at chain level |
| `prop:genus-g-curvature-package` | `proposition` | 541 | The genus-$g$ curvature package |
| `prop:chain-level-curvature-operator` | `proposition` | 677 | Chain-level curvature operator |
| `prop:genus-g-mc-element` | `proposition` | 825 | Genus-$g$ MC element |
| `thm:genus-extension-hierarchy` | `theorem` | 857 | Genus extension hierarchy |
| `thm:bar-ainfty-complete` | `theorem` | 1243 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 1343 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 1438 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 1551 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 1658 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 1805 | Verdier duality of operations |
| `thm:bar-curved-ch-infty` | `theorem` | 1967 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
| `thm:convergence-filtered` | `theorem` | 2045 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 2263 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 2297 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 2331 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 2351 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 2367 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2672 | Bar-cobar isomorphism, retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 2757 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2972 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 3578 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 3781 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 3841 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 4094 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:genus1-d-squared` | `theorem` | 4188 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 4245 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 4515 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 4548 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 4675 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 4847 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 4901 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 4981 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 5141 | \texorpdfstring{$W_3$}{W3} fiberwise obstruction |
| `comp:w3-obs-explicit` | `computation` | 5202 | Explicit genus-$1$ value of the $W_3$ obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 5239 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 5268 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 5355 | Mumford multiplicative relations for obstruction classes |
| `prop:scalar-obstruction-hodge-euler` | `proposition` | 5468 | Scalar obstruction equals Hodge Euler class |
| `lem:k-theoretic-globalization-bar` | `lemma` | 5636 | $K$-theoretic globalization of the scalar bar class |
| `prop:clutching-uniqueness` | `proposition` | 6064 | Clutching uniqueness of the Hodge Euler class, socle scope |
| `thm:genus-universality` | `theorem` | 6376 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 6820 | Multi-generator edge universality |
| `prop:f2-quartic-dependence` | `proposition` | 6868 | Genus-$2$ quartic dependence |
| `cor:anomaly-ratio` | `corollary` | 6929 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 6945 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 6972 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 6990 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 7013 | Universal genus-$1$ criticality criterion; scalar-lane collapse |
| `cor:tautological-class-map` | `corollary` | 7048 | Tautological class map on the scalar lane; universal genus-$1$ class |
| `prop:bar-tautological-filtration` | `proposition` | 7167 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 7239 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 7269 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 7367 | Scalar obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 7438 | Grothendieck--Riemann--Roch bridge on the proved uniform-weight scalar lane |
| `lem:stable-graph-d-squared` | `lemma` | 7640 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 7702 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 7740 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 7782 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 7871 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 7959 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 8028 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 8062 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 8117 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 8174 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 8202 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 8252 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (269)

| Label | Env | Line | Title |
|---|---|---:|---|
| `__unlabeled_chapters/theory/higher_genus_modular_koszul.tex:287` | `proposition` | 287 | MCG-equivariance of the genus tower |
| `thm:genus-graded-koszul` | `theorem` | 375 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 406 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 721 | Free-field examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 765 | Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 807 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `lem:pbw-weightwise-g-module` | `lemma` | 950 | Weightwise reduction of the genus enrichment to \texorpdfstring{$\fg$}{g}-modules |
| `lem:pbw-mixed-factorization` | `lemma` | 1009 | Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)} |
| `thm:pbw-genus1-km` | `theorem` | 1057 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 1375 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 1400 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1608 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1660 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1760 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1810 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1872 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `prop:hook-pbw` | `proposition` | 2033 | Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses |
| `thm:pbw-propagation` | `theorem` | 2125 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | 2284 | Locality of the collision differential |
| `thm:three-tier-architecture` | `theorem` | 2371 | Three-tier logical architecture of modular Koszul duality |
| `lem:e2-higher-genus` | `lemma` | 2620 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 2774 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 2883 | Modular characteristic |
| `prop:kappa-three-routes` | `proposition` | 3141 | Three recovery routes for $\kappa$ on the scalar lane |
| `cor:free-energy-ahat-genus` | `corollary` | 3407 | Scalar free energy as $\hat{A}$-genus |
| `prop:gue-universality` | `proposition` | 3744 | GUE universality |
| `rem:shadow-tr-pf-decomposition-identity` | `remark` | 3829 | Shadow/topological-recursion/planted-forest decomposition |
| `thm:spectral-characteristic` | `theorem` | 3868 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 3901 | Universal modular Maurer--Cartan class |
| `prop:curvature-centrality-general` | `proposition` | 4040 | Centrality of higher-genus curvature |
| `thm:mc2-bar-intrinsic` | `theorem` | 4102 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 4694 | Shadow extraction |
| `prop:mc2-functoriality` | `proposition` | 4809 | Functoriality of the bar-intrinsic MC element |
| `thm:bipartite-linfty-tree` | `theorem` | 4912 | Bipartite shadow as $L_\infty$ tree-level structure |
| `thm:explicit-theta` | `theorem` | 5036 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 5263 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 5710 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 5789 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 5902 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 5936 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 5968 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 6173 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 6250 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 6315 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 6450 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 6547 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 6658 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowdegree-packet-criterion` | `proposition` | 6795 | One-channel visible low-degree seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 6947 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 7121 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 7271 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 7465 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 7585 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 7684 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 7774 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 7886 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 7958 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 8040 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 8118 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 8195 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 8271 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 8346 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 8412 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 8492 | MC2 completion under explicit hypotheses |
| `thm:mc2-full-resolution` | `theorem` | 8578 | MC2 comparison completion on the proved scalar lane |
| `lem:mk67-from-mc2` | `lemma` | 8631 | Bar-intrinsic MC2 identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 8674 | One-channel line concentration of the minimal MC class |
| `thm:km-strictification` | `theorem` | 8745 | KM strictification of the universal class |
| `prop:w-algebra-scalar-saturation` | `proposition` | 8833 | One-channel line concentration for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 8880 | One-dimensional cyclic line persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 8941 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 9091 | One-channel line concentration for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 9194 | Cyclic rigidity and level-direction concentration |
| `prop:saturation-functorial` | `proposition` | 9387 | Functorial behavior of one-channel line concentration |
| `cor:effective-quadruple` | `corollary` | 9554 | Effective \texorpdfstring{$\Gamma$}{Gamma}-quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 9645 | Cyclic rigidity at generic level |
| `thm:algebraic-family-rigidity` | `theorem` | 9814 | Algebraic-family rigidity |
| `cor:saturation-algebraic-families` | `corollary` | 9926 | Level-direction concentration at all non-critical levels for algebraic families |
| `thm:conformal-bootstrap-rigidity` | `theorem` | 9995 | $L_0$-bootstrap rigidity |
| `cor:one-channel-no-lie` | `corollary` | 10102 | One-channel criterion without Lie symmetry |
| `thm:kappa-universal-class` | `theorem` | 10342 | Universal $\kappa$ class: existence, uniqueness, specialization |
| `thm:tautological-line-support` | `theorem` | 10500 | Tautological line support from genus universality |
| `cor:mc2-single-hypothesis` | `corollary` | 10614 | MC2 comparison gauntlet collapses on the proved scalar lane |
| `thm:convolution-dg-lie-structure` | `theorem` | 10801 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 11043 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 11491 | Modular homotopy convolution |
| `prop:modular-homotopy-type-structure` | `proposition` | 11583 | Structure of the modular homotopy type |
| `cor:strictification-comparison` | `corollary` | 11630 | Strictification comparison |
| `cor:vol1-theta-log-fm-twisting-data` | `corollary` | 12006 | $\Theta_\cA$ as universal modular twisting morphism |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | 12267 | First two weights |
| `comp:vol1-low-genus-log-fm-chart` | `computation` | 12342 | Low-genus amplitudes |
| `lem:shadow-bracket-well-defined` | `lemma` | 13121 | Well-definedness of the descended bracket |
| `prop:shadow-algebra-linfty` | `proposition` | 13143 | Transferred $L_\infty$ structure on the shadow algebra |
| `cor:shadow-algebra-functoriality` | `corollary` | 13251 | Functoriality of the shadow algebra |
| `prop:master-equation-from-mc` | `proposition` | 13289 | All-degree master equation from MC |
| `thm:ds-complementarity-tower-main` | `theorem` | 13353 | DS complementarity tower |
| `thm:recursive-existence` | `theorem` | 13594 | Recursive existence and shadow obstruction tower convergence |
| `thm:perturbative-exactness` | `theorem` | 13856 | Perturbative exactness of the modular MC element |
| `thm:universal-modular-deformation` | `theorem` | 13929 | Universal modular deformation functor |
| `thm:modular-propagator-existence` | `theorem` | 14080 | Modular propagator existence |
| `thm:logfm-modular-cocomposition` | `theorem` | 14114 | Log-FM modular cocomposition |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | 14156 | Stable-graph pronilpotent completion |
| `thm:finite-rank-spectral-reduction` | `theorem` | 14207 | Finite-rank spectral reduction |
| `thm:primitive-to-global-reconstruction` | `theorem` | 14272 | Primitive-to-global reconstruction |
| `prop:primitive-shell-equations` | `proposition` | 14422 | Primitive shell equations |
| `prop:branch-master-equation` | `proposition` | 14561 | Branch quantum master equation |
| `cor:metaplectic-square-root` | `corollary` | 14614 | Determinantal half-density |
| `thm:primitive-flat-descent` | `theorem` | 14805 | Descent to the flat modular connection |
| `thm:conformal-block-reconstruction` | `theorem` | 14884 | Scalar free-energy and determinant reconstruction from the primitive kernel on the proved uniform-weight scalar lane |
| `thm:deformation-quantization-ope` | `theorem` | 14981 | Genus expansion from the OPE |
| `thm:ran-coherent-bar-cobar` | `theorem` | 15182 | Ran-coherent bar-cobar equivalence |
| `thm:shadow-channel-decomposition` | `theorem` | 15242 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 15322 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 15374 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 15522 | Direct derivation on the proved scalar lane |
| `lem:graph-sum-truncation` | `lemma` | 15853 | Graph-sum truncation criterion |
| `thm:operadic-complexity-detailed` | `theorem` | 15929 | Operadic complexity |
| `prop:shadow-formality-low-degree` | `proposition` | 16047 | Shadow--formality identification at low degree |
| `thm:shadow-formality-identification` | `theorem` | 16118 | Shadow obstruction tower as formality obstruction tower |
| `prop:shadow-tower-three-lenses` | `proposition` | 16392 | Three lenses on the shadow obstruction tower |
| `prop:shadow-formality-higher-degree` | `proposition` | 16489 | Shadow--formality identification at higher degrees |
| `prop:linfty-obstruction-5-6` | `proposition` | 16845 | Explicit $L_\infty$ obstruction classes at degrees $5$ and $6$ |
| `prop:shadow-coefficient-rationality` | `proposition` | 17097 | Shadow coefficient rationality |
| `cor:operadic-complexity-5-7` | `corollary` | 17122 | Operadic complexity at degrees $5$--$7$ |
| `thm:shadow-archetype-classification` | `theorem` | 17508 | Shadow archetype classification |
| `cor:shadow-depth-koszul-invariance` | `corollary` | 17768 | Shadow depth under Koszul duality |
| `prop:sc-formality-by-class` | `proposition` | 17853 | Swiss-cheese formality classification by shadow class |
| `prop:shadow-depth-escalator` | `proposition` | 17943 | Shadow depth escalator |
| `thm:riccati-algebraicity` | `theorem` | 18144 | Riccati algebraicity: the shadow generating function is algebraic of degree~$2$ |
| `lem:depth-three-impossible` | `lemma` | 18307 | Impossibility of $d_{\mathrm{alg}} = 3$ |
| `prop:depth-gap-trichotomy` | `proposition` | 18388 | Algebraic depth gap: no $d_{\mathrm{alg}} = 3$ |
| `prop:hankel-extraction` | `proposition` | 18613 | Hankel extraction of the quartic contact invariant |
| `cor:signed-shadow-measure` | `corollary` | 18764 | Universal signed measure |
| `thm:shadow-epstein-zeta` | `theorem` | 18846 | The Epstein zeta function of the shadow metric |
| `prop:pole-purity` | `proposition` | 19182 | Pole purity |
| `prop:intrinsic-quartic` | `proposition` | 19200 | Intrinsic quartic principle |
| `thm:single-line-dichotomy` | `theorem` | 19235 | Single-line dichotomy |
| `prop:shadow-integrable-hierarchy` | `proposition` | 19423 | Shadow CohFT and integrable hierarchies |
| `thm:shadow-tau-kw` | `theorem` | 19487 | Shadow tau function |
| `thm:shadow-connection` | `theorem` | 19654 | Shadow connection |
| `prop:galois-koszul-sign` | `proposition` | 19780 | The Galois involution is the Koszul sign |
| `cor:discriminant-atlas` | `corollary` | 19885 | The discriminant atlas |
| `thm:shadow-separation` | `theorem` | 20138 | Shadow separation and completeness |
| `prop:propagator-variance` | `proposition` | 20242 | Propagator variance inequality |
| `prop:t-line-autonomy` | `proposition` | 20352 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | 20409 | Inter-channel coupling on sublines |
| `thm:shadow-radius` | `theorem` | 20554 | Shadow growth rate: structure and asymptotics |
| `prop:shadow-tower-growth-rate` | `proposition` | 20660 | Shadow tower growth from the shadow metric |
| `cor:virasoro-shadow-radius` | `corollary` | 20776 | Virasoro shadow growth rate |
| `prop:virasoro-shadow-ratio-riccati` | `proposition` | 20844 | Virasoro shadow ratio: Riccati recurrence and root asymptotics |
| `prop:critical-cubic-convergence` | `proposition` | 21256 | Critical cubic convergence threshold |
| `prop:virasoro-bottleneck` | `proposition` | 21345 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | 21572 | Koszul exchange of shadow regimes |
| `prop:koszul-conductor-wn` | `proposition` | 21649 | Koszul conductor of \texorpdfstring{$\cW_N$}{WN} |
| `prop:koszul-conductor-anomaly-vanishing` | `proposition` | 21708 | Anomaly-free characterisation of the Koszul conductor |
| `prop:propagator-universality` | `proposition` | 21793 | Propagator universality |
| `thm:hamilton-jacobi-shadow` | `theorem` | 22134 | Hamilton--Jacobi master equation on deformation spaces |
| `thm:shadow-finite-determination` | `theorem` | 22339 | Shadow finite determination |
| `cor:w3-reconstruction` | `corollary` | 22426 | $\cW_3$: seven parameters determine the full 2D tower |
| `thm:shadow-tautological-ring` | `theorem` | 22632 | Shadow classes in the tautological ring |
| `cor:analytic-shadow-realization` | `corollary` | 22775 | Analytic shadow realization |
| `thm:shadow-cohft` | `theorem` | 22861 | Shadow cohomological field theory |
| `thm:multi-weight-genus-expansion` | `theorem` | 23040 | Multi-weight genus expansion |
| `prop:free-field-scalar-exact` | `proposition` | 23205 | Free-field exactness of the scalar formula |
| `rem:delta-f2-graph-decomposition` | `remark` | 24258 | $\delta F_2$ graph-stratum decomposition |
| `comp:w3-genus3-cross` | `computation` | 24314 | $\cW_3$ genus-$3$ cross-channel |
| `comp:w3-genus4-cross` | `computation` | 24389 | $\cW_3$ genus-$4$ cross-channel |
| `comp:w4-full-ope-cross` | `computation` | 24488 | $\cW_4$ full-OPE cross-channel correction |
| `rem:w4-irrational-cross-channel` | `remark` | 24633 | $\cW_4$: the first irrational cross-channel correction |
| `comp:w5-full-ope-cross` | `computation` | 24665 | $\cW_5$ full-OPE cross-channel correction |
| `prop:universal-gravitational-cross-channel` | `proposition` | 24902 | Universal gravitational cross-channel formula for~$\cW_N$ |
| `rem:large-n-delta-f2-planar` | `remark` | 25169 | Large-$N$ and 't~Hooft limit of $\delta F_2$ |
| `prop:cross-channel-growth` | `proposition` | 25291 | Cross-channel growth |
| `prop:cross-channel-no-closed-form` | `proposition` | 25440 | Irreducible bivariance of the cross-channel generating function |
| `thm:shadow-tautological-relations` | `theorem` | 25640 | Shadow tautological decomposition and conditional vanishing |
| `thm:mc-tautological-descent` | `theorem` | 25736 | MC descent to tautological relations |
| `prop:self-loop-vanishing` | `proposition` | 26212 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | 26248 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | 26417 | Genus-$1$ two-point function from MC |
| `prop:wdvv-from-mc` | `proposition` | 26449 | WDVV from MC at genus~$0$ |
| `prop:mumford-from-mc` | `proposition` | 26482 | Mumford relation from MC at degree~$2$ |
| `thm:planted-forest-structure` | `theorem` | 26514 | Planted-forest structure theorem |
| `prop:w3-genus2-cross-channel-sharp-negative` | `proposition` | 26636 | $\cW_3$ genus-$2$ cross-channel: sharp negative for uniform-weight scalar formulas |
| `thm:cohft-reconstruction` | `theorem` | 26698 | Reconstruction from the MC tangent complex |
| `prop:dressed-propagator-resolution` | `proposition` | 26792 | Dressed propagator coefficient and symmetry |
| `thm:pixton-from-mc-semisimple` | `theorem` | 26931 | Pixton ideal generation on the semisimple locus |
| `prop:non-semisimple-pixton-obstruction` | `proposition` | 27018 | Non-semisimple obstruction to Pixton generation |
| `rem:pixton-mc-five-paths` | `remark` | 27080 | Five-path verification of Pixton ideal membership |
| `cor:topological-recursion-mc-shadow` | `corollary` | 27131 | Topological recursion as MC shadow |
| `thm:pixton-mc-genus2` | `theorem` | 27343 | Pixton--MC bridge at genus~$2$ |
| `thm:pixton-mc-genus3` | `theorem` | 27406 | Pixton--MC bridge at genus~$3$ |
| `prop:mumford-from-mc-explicit` | `proposition` | 27481 | Mumford formula from MC |
| `thm:spectral-curve-from-shadow` | `theorem` | 27536 | Spectral curve from shadow metric |
| `thm:tr-shadow-free-energies` | `theorem` | 27570 | TR--shadow free energy identification |
| `thm:genus4-stable-graph-census` | `theorem` | 27610 | Genus-$4$ stable graph census |
| `thm:genus4-free-energy` | `theorem` | 27639 | Genus-$4$ free energy |
| `prop:genus4-spectral-sequence` | `proposition` | 27660 | Genus-$4$ spectral sequence |
| `thm:bar-macmahon` | `theorem` | 27709 | Bar--MacMahon correspondence |
| `prop:conifold-dt-gv` | `proposition` | 27736 | Conifold DT and GV |
| `thm:shadow-dt-curve-counting` | `theorem` | 27750 | Shadow obstruction tower and DT curve counting |
| `prop:tropical-shadow-amplitudes` | `proposition` | 27787 | Tropical shadow amplitudes |
| `prop:tropical-period-theta` | `proposition` | 27810 | Tropical theta function |
| `prop:fp-genus-decay-for-double` | `proposition` | 27871 | Faber--Pandharipande genus decay |
| `thm:shadow-double-convergence` | `theorem` | 27898 | Double convergence of the shadow partition function |
| `prop:shadow-genus-closed-form` | `proposition` | 28014 | Closed form and meromorphic continuation |
| `thm:shadow-borel-genus` | `theorem` | 28094 | Borel transform of the genus series |
| `prop:shadow-stokes-multipliers` | `proposition` | 28155 | Stokes multipliers of the genus expansion |
| `thm:shadow-transseries` | `theorem` | 28183 | Trans-series and instanton sectors |
| `prop:universal-instanton-action` | `proposition` | 28258 | Universal instanton action |
| `prop:c13-full-self-duality` | `proposition` | 28577 | Full tower self-duality at $c = 13$ |
| `prop:shadow-schwarzian` | `proposition` | 28820 | Spectral Schr\"odinger potential |
| `cor:shadow-schrodinger-singularities` | `corollary` | 28857 | Singularity classification |
| `prop:shadow-wkb` | `proposition` | 28929 | WKB expansion |
| `prop:shadow-voros-classical` | `proposition` | 28999 | Classical Voros period |
| `prop:shadow-gue-bridge` | `proposition` | 29042 | Shadow--GUE bridge |
| `prop:shadow-genus-constraints` | `proposition` | 29128 | Shadow genus constraints |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | 29285 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:finite-jet-rigidity` | `proposition` | 29365 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 29388 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 29424 | Gaussian collapse for abelian input |
| `thm:cubic-gauge-triviality` | `theorem` | 29508 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | 29616 | Independent sum factorization |
| `prop:symn-kappa-linearity` | `proposition` | 29674 | Symmetric orbifold kappa linearity |
| `rem:symmetric-orbifold-kappa` | `remark` | 29758 | Symmetric orbifold kappa: four independent verifications |
| `thm:envelope-koszul` | `theorem` | 29784 | Envelope Koszulness |
| `cor:generic-ht-koszul` | `corollary` | 29862 | Generic-parameter Koszulness for HT boundary algebras |
| `thm:platonic-adjunction` | `theorem` | 29966 | Modular envelope construction and adjunction frontier |
| `cor:envelope-universal-mc` | `corollary` | 30062 | The envelope carries the canonical MC class |
| `prop:platonic-sl2-specialization` | `proposition` | 30157 | Affine \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} specialization |
| `prop:envelope-construction-strategies` | `proposition` | 30195 | Construction strategies for the modular envelope |
| `thm:shadow-depth-invariant` | `theorem` | 30267 | Shadow depth is a homotopy invariant |
| `thm:tropical-koszulness` | `theorem` | 30311 | Tropical Koszulness |
| `cor:tropical-cohen-macaulay` | `corollary` | 30401 | Tropical Koszulness as the Cohen--Macaulay property |
| `prop:genus0-curve-independence` | `proposition` | 30448 | Genus-$0$ curve-independence |
| `thm:open-stratum-curve-independence` | `theorem` | 30467 | Open-stratum curve-independence at higher genus |
| `prop:saddle-point-mc` | `proposition` | 30797 | MC element as saddle point |
| `prop:bcov-mc-projection` | `proposition` | 30984 | BCOV holomorphic anomaly equation as MC projection |
| `thm:five-from-theta` | `theorem` | 31236 | Five main theorems from the master MC element |
| `thm:obstruction-recursion` | `theorem` | 31510 | Obstruction recursion for the shadow obstruction tower |
| `thm:rectification-meta` | `theorem` | 31607 | Rectification meta-theorem |
| `thm:platonic-recovery` | `theorem` | 31703 | Recovery of the modular Koszul datum from $\Theta_\cA$ |
| `prop:chriss-ginzburg-structure` | `proposition` | 31926 | MC structure principle |
| `prop:planar-forest-coinvariant` | `proposition` | 32306 | Planar forests map to unordered forests |
| `thm:planar-forest-tropicalization` | `theorem` | 32339 | Planar tropicalization |
| `prop:ordered-log-fm-construction` | `proposition` | 32384 | Ordered log-FM construction |
| `cor:e1-ambient-d-squared-zero` | `corollary` | 32462 | $E_1$ ambient $D^2 = 0$ |
| `prop:coefficient-algebras-well-defined` | `proposition` | 32525 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 32558 | Square-zero: convolution level |
| `thm:differential-square-zero` | `theorem` | 32572 | Square-zero: ambient level |
| `thm:inductive-genus-determination` | `theorem` | 32802 | Inductive genus determination |
| `cor:genus-base-cases` | `corollary` | 32870 | Base cases |
| `thm:genus2-shell-activation` | `theorem` | 32924 | Genus-$2$ shell activation as depth diagnostic |
| `comp:vol1-genus-three-stable-graph-census` | `computation` | 33123 | Genus-$3$ stable graph census |
| `prop:2d-convergence` | `proposition` | 33420 | Two-dimensional convergence |
| `thm:analytic-algebraic-comparison` | `theorem` | 33476 | Analytic = algebraic |
| `thm:verlinde-polynomial-family` | `theorem` | 34032 | Verlinde polynomial family |
| `prop:g2-degree0` | `proposition` | 34393 | Degree-$0$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree1` | `proposition` | 34447 | Degree-$1$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree2` | `proposition` | 34777 | Degree-$2$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-conformal-block-degree` | `proposition` | 34874 | Genus-$2$ conformal block decomposition by degree |
| `prop:genus-g-euler-general` | `proposition` | 34935 | Euler characteristic of degree-$2$ KZB local systems: general rank and genus |
| `prop:g2-euler-n` | `proposition` | 35029 | Euler characteristic at low degrees, genus~$2$ |
| `prop:g2-nonsep-degen` | `proposition` | 35247 | Non-separating degeneration: $\Sigma_2 \to E_\tau$ |
| `prop:g2-sep-degen` | `proposition` | 35360 | Separating degeneration: $\Sigma_2 \to E_\tau \cup E_{\tau'}$ |
| `thm:determinantal-branch-formula` | `theorem` | 35672 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | 35708 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | 35739 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | 35803 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | 35839 | The frontier is cubic |

#### `chapters/theory/higher_kummer_arithmetic_duality_platonic.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:higher-kummer-z-g-presence` | `theorem` | 79 | Kummer-irregular primes witnessed on the $Z_g$ side |
| `thm:higher-kummer-s-r-absence-through-r-13` | `theorem` | 181 | Higher Kummer-irregular primes absent from $S_r(\Vir_c)$ through $r = 13$ |
| `thm:higher-kummer-refined-duality` | `theorem` | 314 | Refined $Z_g \leftrightarrow S_r$ arithmetic duality through $r = 13$ |

#### `chapters/theory/hochschild_cohomology.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 149 | Virasoro chiral Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 261 | W-algebra chiral Hochschild cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:497` | `computation` | 497 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 553 | Chiral Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 633 | Cyclic operator commutes with the chiral Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 914 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 944 | Chiral Hochschild cup product exchange |
| `thm:derived-center-hochschild` | `theorem` | 1132 | Derived center $=$ categorical Hochschild cohomology $=$ algebraic Hochschild cochains via a compact generator |
| `thm:morita-invariance-HH` | `theorem` | 1221 | Morita invariance of algebraic Hochschild cohomology |
| `prop:explicit-morita-transfer` | `proposition` | 1253 | Explicit Morita transfer |
| `thm:circle-fh-hochschild` | `theorem` | 1424 | Factorization homology on $S^1$ $=$ topological Hochschild chains |
| `prop:monodromy-standard` | `proposition` | 1577 | Monodromy for standard families |

#### `chapters/theory/infinite_fingerprint_classification.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fingerprint-is-complete-invariant` | `theorem` | 71 | Infinite fingerprint classification; strengthening of Theorem~\ref{thm:fingerprint-completeness} |
| `thm:fifth-class-FF` | `theorem` | 173 | Fifth class: critical-level bar structure; closes FM\textup{77}/AP\textup{77} |
| `thm:pole-depth-independence` | `theorem` | 298 | Pole--depth independence |
| `prop:class-from-full-tower` | `proposition` | 338 | Class determination from full shadow tower; formalisation of AP-CY\textup{12} |
| `thm:d-alg-r-max-bijection` | `theorem` | 368 | Depth bijection; closes FM\textup{110} |
| `thm:quadrichotomy-is-coarse-projection` | `theorem` | 430 | Quadrichotomy is a coarse projection; strengthening of Proposition~\ref{prop:coarse-projection-functor} |
| `thm:DS-fingerprint-transport` | `theorem` | 526 | DS transport of the fingerprint; closes FM\textup{108} |
| `cor:fingerprint-separates-landscape` | `corollary` | 671 | Completeness on the standard landscape |

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 1178 | Central charge complementarity |
| `thm:e1-primacy` | `theorem` | 1465 | $\Eone$ primacy |

#### `chapters/theory/kappa_conductor.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:conductor-trinity` | `theorem` | 72 | Trinity |
| `thm:platonic-conductor` | `theorem` | 119 | Platonic Conductor |

#### `chapters/theory/koszul_pair_structure.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:three-levels-mc-completion` | `proposition` | 163 | Three levels as MC at successive completions |
| `lem:chiral-enveloping-well-defined` | `lemma` | 213 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 258 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 315 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 334 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 391 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 454 | \texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 513 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 650 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 747 | Chiral Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 762 | chiral Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 868 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 980 | Maurer--Cartan correspondence, quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 1071 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1101 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1311 | Positselski equivalence for the chiral bar coalgebra |
| `thm:full-derived-module-equiv` | `theorem` | 1360 | Flat finite-type reduction on the completed-dual side |
| `thm:cs-koszul-km` | `theorem` | 1474 | Affine Kac--Moody Maurer--Cartan and curvature package |
| `thm:linf-mc-flatness` | `theorem` | 1542 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan equation from a transferred \texorpdfstring{$A_\infty$}{A-infinity} model |
| `thm:bv-structure-bar` | `theorem` | 1713 | BV structure on bar complex |
| `thm:ordered-shuffle` | `theorem` | 1903 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | 1945 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | 1975 | Enveloping duality |
| `thm:ordered-bimod-bicomod` | `theorem` | 2014 | Bimodule--bicomodule equivalence |
| `thm:ordered-diagonal` | `theorem` | 2039 | Diagonal correspondence |
| `thm:ordered-HH-coHH-homology` | `theorem` | 2087 | chiral Hochschild--coHochschild duality, homological version |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | 2118 | chiral Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-pair-of-pants` | `theorem` | 2166 | Ordered pair-of-pants algebra |
| `thm:ordered-master` | `theorem` | 2190 | Master theorem: the ordered open trace formalism |

#### `chapters/theory/koszulness_moduli_scheme.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `v1-thm:kms-moduli` | `theorem` | 170 | Koszulness moduli, Kontsevich--Tamarkin reformulation |
| `v1-cor:kms-grt-invariant` | `corollary` | 300 | Associator-independence of the Koszulness property |
| `v1-thm:kms-fourteen-unconditional` | `theorem` | 355 | Fourteen characterisations, unconditional on their home chart |
| `v1-prop:kms-at-chart` | `proposition` | 494 | Alekseev--Torossian chart |
| `v1-prop:kms-hodge-betti-chart` | `proposition` | 556 | Hodge--Betti chart |
| `v1-prop:kms-elliptic-chart` | `proposition` | 597 | Enriquez elliptic chart |
| `v1-prop:kms-kontsevich-chart` | `proposition` | 646 | Kontsevich integral chart |
| `v1-thm:kms-koszulness-is-grt-invariant` | `theorem` | 713 | Koszulness is $\mathrm{GRT}_1$-invariant; characterisations are charts |
| `v1-thm:kms-virasoro-noncircular` | `theorem` | 749 | Virasoro Koszulness, non-circular |
| `v1-thm:kms-yangian-embedding` | `theorem` | 854 | Yangian chart inclusion |
| `v1-thm:kms-meta-koszulness` | `theorem` | 945 | Meta-Koszulness |

#### `chapters/theory/koszulness_vii_multiweight_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:koszulness-vii-multiweight-up-to-correction` | `theorem` | 121 | Characterization~(vii) at multi-weight: scalar equivalence up to explicit correction |
| `prop:delta-f-cross-universal-formula` | `proposition` | 221 | Universal form of the cross-channel correction |
| `cor:uniform-weight-correction-vanishes` | `corollary` | 347 | Uniform-weight correction vanishes |
| `cor:free-field-correction-vanishes` | `corollary` | 374 | Free-field correction vanishes at multi-weight |
| `thm:koszulness-vii-upgrade` | `theorem` | 399 | Characterization~(vii) upgrade: scope-restriction $\to$ equivalence up to explicit correction |

#### `chapters/theory/mc3_five_family_platonic.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:mc3-evaluation-core-five-family` | `theorem` | 102 | MC3 on the evaluation-generated core, five-family mechanism |
| `prop:mc3-type-A-asymptotic-prefundamentals-platonic` | `proposition` | 213 | Asymptotic prefundamentals: rational type~$A$ |
| `prop:mc3-type-BCD-reflection-shapovalov-platonic` | `proposition` | 267 | Reflection-equation Shapovalov: twisted B/C/D |
| `prop:mc3-uniform-chari-moura-platonic` | `proposition` | 312 | Chari--Moura multiplicity-free $\ell$-weights: classical and simply-laced exceptional types |
| `prop:mc3-elliptic-theta-divisor-platonic` | `proposition` | 410 | Elliptic Bethe / DYBE: theta-divisor complement |
| `prop:mc3-super-parity-balance-platonic` | `proposition` | 444 | Super-Yangian parity-balance: $Y_\hbar(\mathfrak{gl}_{m\|n})$ |
| `prop:baxter-retraction-type-A-artifact` | `proposition` | 573 | Baxter hyperplane as a type-$A$ rational artifact |
| `cor:five-family-union-coverage` | `corollary` | 729 | Five-family union coverage |

#### `chapters/theory/mc5_class_m_chain_level_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:mc5-class-m-chain-level-pro-ambient` | `theorem` | 230 | MC5 class $\mathsf{M}$ chain-level in the pro-ambient |
| `cor:mc5-class-m-chain-level-on-inverse-limit` | `corollary` | 415 | Chain-level MC5 class $\mathsf{M}$ on the inverse limit |
| `thm:mc5-class-m-topological-chain-level-j-adic` | `theorem` | 523 | MC5 class $\mathsf{M}$ chain-level in the $J$-adic topological ambient |
| `prop:ambient-equivalence` | `proposition` | 589 | Ambient equivalence for chain-level MC5 |
| `prop:central-m0-vacuum-proportionality` | `proposition` | 783 | Sub-argument (b): vacuum-proportionality uniqueness of the central degree-2 curvature |

#### `chapters/theory/mc5_genus0_genus1_wall_platonic.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:mc5-g0g1-wall-five-point-sewing` | `theorem` | 166 | MC5 5-point sewing at the genus-0/genus-1 wall |
| `cor:mc5-g0g1-heisenberg-elliptic-function` | `corollary` | 505 | Heisenberg elliptic function at the wall |
| `cor:mc5-g0g1-virasoro-class-m-corrections` | `corollary` | 540 | Virasoro class-$\mathsf{M}$ shadow corrections at the wall |
| `cor:mc5-g0g1-k3-elliptic-genus` | `corollary` | 582 | K3 elliptic genus at the wall |

#### `chapters/theory/motivic_shadow_full_class_m_platonic.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:shadow-tower-depth-1-rationality` | `theorem` | 79 | \label{thm:shadow-tower-depth-1-rationality}Shadow residues are depth-$1$ Arnold data |
| `thm:e1-vs-e2-mzv-depth-distinction` | `theorem` | 151 | \label{thm:e1-vs-e2-mzv-depth-distinction} $E_1$-chiral residue vs $E_2$-topological iterated integral |
| `thm:w-n-motivic-rationality-all-r` | `theorem` | 228 | \label{thm:w-n-motivic-rationality-all-r}Principal $\cW_N$ motivic rationality in all weights |
| `prop:w3-w-line-motivic-rationality` | `proposition` | 270 | \label{prop:w3-w-line-motivic-rationality} $\cW_3$ W-line explicit rationality |
| `thm:bp-motivic-rationality-arakawa` | `theorem` | 319 | \label{thm:bp-motivic-rationality-arakawa}BP motivic rationality in Arakawa convention |
| `prop:bp-fl-convention-caveat` | `proposition` | 368 | \label{prop:bp-fl-convention-caveat}FL-convention Koszul conductor: distinct constant |
| `thm:w-infty-motivic-rationality-all-r` | `theorem` | 434 | \label{thm:w-infty-motivic-rationality-all-r} $\cW_{\infty}$ motivic rationality |
| `thm:class-m-motivic-rationality-full` | `theorem` | 495 | \label{thm:class-m-motivic-rationality-full} Class M motivic rationality |

#### `chapters/theory/motivic_shadow_tower.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:shadow-tower-motivic-lift` | `theorem` | 236 | \label{thm:shadow-tower-motivic-lift}Motivic lift of the shadow tower |
| `thm:grt-motivic-coaction` | `theorem` | 343 | \label{thm:grt-motivic-coaction}GRT motivic coaction on the shadow tower |
| `prop:s4-vir-mot` | `proposition` | 418 | \label{prop:s4-vir-mot}Motivic lift of $S_4(\Vir_c)$ |
| `prop:s5-vir-mot` | `proposition` | 471 | \label{prop:s5-vir-mot}Motivic lift of $S_5(\Vir_c)$ |
| `prop:s6-w3-mot` | `proposition` | 518 | \label{prop:s6-w3-mot}Motivic lift of $S_6(W_3)$ carries $\zet^{\mot}(3)$ |
| `thm:virasoro-motivic-rationality-all-r` | `theorem` | 616 | \label{thm:virasoro-motivic-rationality-all-r}Virasoro motivic rationality in all weights |
| `thm:kummer-from-motivic` | `theorem` | 769 | \label{thm:kummer-from-motivic}Kummer congruences from motivic Bernoulli-Kummer |
| `rem:characteristic-primes-are-riccati-arithmetic` | `remark` | 835 | \label{rem:characteristic-primes-are-riccati-arithmetic}Characteristic primes of the shadow tower are Riccati-recurrence integer combinations, NOT Kac-determinant discriminants |
| `cor:shadow-L-pole` | `corollary` | 919 | \label{cor:shadow-L-pole}Pole structure of the motivic shadow L-function |
| `thm:kappa-vs-beta-split` | `theorem` | 991 | \label{thm:kappa-vs-beta-split}Motivic kappa, modular beta |

#### `chapters/theory/nilpotent_completion.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:geom-conilpotent` | `proposition` | 87 | Geometric manifestation |
| `thm:completion-convergence` | `theorem` | 115 | Completion convergence |
| `thm:completed-bar-cobar` | `theorem` | 191 | Completed bar-cobar duality |
| `thm:koszul-dual-characterization` | `theorem` | 251 | Characterization of Koszul duals |
| `thm:stabilized-completion-positive` | `theorem` | 562 | Stabilized completion for positive towers |
| `thm:resonance-filtered-bar-cobar` | `theorem` | 673 | Resonance-filtered completed bar/cobar |
| `prop:resonance-ss-degeneration` | `proposition` | 777 | Resonance spectral sequence degeneration |
| `prop:resonance-ranks-standard` | `proposition` | 804 | Resonance ranks of the standard families |
| `cor:virasoro-resonance-ss` | `corollary` | 875 | Virasoro resonance spectral sequence |
| `thm:platonic-completion` | `theorem` | 948 | Resonance completion |

#### `chapters/theory/ordered_associative_chiral_kd.tex` (90)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bicom-e` | `lemma` | 211 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | 294 | Ordered chiral shuffle theorem |
| `sec:r-matrix-descent-vol1` | `proposition` | 555 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | 700 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | 844 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | 885 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | 936 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | 956 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | 1018 | — |
| `prop:one-defect` | `proposition` | 1045 | — |
| `thm:tangent=K` | `theorem` | 1067 | Tangent identification |
| `cor:infdual` | `corollary` | 1104 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | 1136 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | 1188 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | 1221 | Diagonal correspondence |
| `cor:unit` | `corollary` | 1269 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | 1287 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | 1323 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | 1355 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | 1381 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | 1406 | Cap action |
| `thm:pair-of-pants` | `theorem` | 1469 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | 1507 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | 1561 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | 1610 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | 1640 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | 1758 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | 2229 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | 2344 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | 2425 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | 2483 | Formality: class~G, shadow depth~$2$ |
| `thm:drinfeld-yangian-sl2` | `theorem` | 2621 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | 2711 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | 2747 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | 2799 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | 2840 | Classical limit |
| `thm:central-extension-invisible` | `theorem` | 2926 | Central extension is invisible to the ordered double bar |
| `thm:two-colour-double-kd` | `theorem` | 3001 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | 3027 | Non-redundancy of the two colours |
| `prop:vir-collision-residue` | `proposition` | 3106 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | 3141 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | 3170 | Gravitational Yangian collapse |
| `thm:vir-non-formality` | `theorem` | 3237 | Virasoro non-formality |
| `prop:grav-yangian-curvature` | `proposition` | 3303 | Gravitational Yangian curvature |
| `cor:gauge-gravity-dichotomy-ordered` | `corollary` | 3348 | Gauge-gravity complexity dichotomy |
| `thm:grav-coproduct-primitive` | `theorem` | 3407 | Gravitational coproduct primitivity |
| `thm:km-yangian` | `theorem` | 3534 | Universal Kac--Moody Yangian theorem |
| `thm:root-space-one-dim-v1` | `theorem` | 3864 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | 3913 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | 3979 | Dynkin coefficient via the beta integral |
| `thm:complete-strictification-v1` | `theorem` | 4060 | Complete strictification for all simple Lie algebras |
| `thm:sl3-triangle-coefficient` | `theorem` | 4403 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | 4487 | Serre relations from root-space vanishing |
| `thm:sl3-rtt` | `theorem` | 4538 | RTT presentation for $Y_\hbar(\mathfrak{sl}_3)$ from the ordered bar complex |
| `thm:sl3-strictification` | `theorem` | 4610 | Vanishing of the spectral Drinfeld class for $\mathfrak{sl}_3$ |
| `thm:sl4-quadrilateral` | `theorem` | 4683 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:B2-ordered-bar` | `theorem` | 4770 | Ordered bar complexes and Yangian $R$-matrices for rank-$2$ non-$A$ types |
| `thm:annular-bar-differential` | `theorem` | 4978 | Annular bar differential |
| `thm:annular-HH` | `theorem` | 5071 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | 5194 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:b-cycle-quantum-group` | `theorem` | 5522 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | 5775 | Drinfeld--Kohno; {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | 5856 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | 5930 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | 5971 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | 6133 | Ordered depth spectrum |
| `thm:ordered-AOS` | `theorem` | 6185 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | 6255 | Averaging and surplus |
| `prop:ker-av-schur-weyl` | `proposition` | 6405 | Kernel of the Reynolds projector: general simple Lie algebras |
| `thm:elliptic-spectral-dichotomy` | `theorem` | 6659 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `thm:bg-ordered-bar` | `theorem` | 6876 | Free-field ordered bar complexes |
| `thm:wakimoto-ordered-bar` | `theorem` | 6947 | Wakimoto bar complex descent |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | 7050 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | 7116 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | 7176 | Ordered Koszul dual of lattice algebras |
| `comp:sl2-eval` | `computation` | 7330 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | 7391 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | 7439 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | 7481 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | 7530 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `prop:eval-drinfeld` | `proposition` | 7602 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | 7669 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | 7730 | Braiding from the $R$-matrix |
| `prop:r-matrix-eigenvalue` | `proposition` | 7837 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | 7864 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | 7962 | $\mathsf{E}_1$ ordered bar landscape |
| `thm:chiral-qg-equiv` | `theorem` | 8407 | Chiral bialgebra equivalence on the Koszul locus |
| `cor:bar-encodes-all` | `corollary` | 8547 | The ordered bar encodes all three structures |
| `thm:w-infty-chiral-qg` | `theorem` | 8739 | $\cW_{1+\infty}[\Psi |
| `rem:spin2-ceff-miura-w1infty` | `remark` | 9160 | Effective central charge and intertwining in the Miura basis |

#### `chapters/theory/periodic_cdg_admissible.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:screening-adjoint-squares` | `lemma` | 99 | Screening adjoints square to zero and satisfy quantum Serre |
| `thm:periodic-cdg-is-koszul-compatible` | `theorem` | 227 | Periodic CDG is Koszul-compatible on filtration quotients |
| `thm:admissible-kl-bar-cobar-adjunction` | `theorem` | 415 | Admissible-KL bar-cobar adjunction |
| `thm:adams-analog-construction` | `theorem` | 602 | Chiral Adams functor, rank one |
| `cor:class-M-admissible-minimal-model` | `corollary` | 728 | Class-M admissible minimal-model adjunction |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 282 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 394 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 461 | Bar construction = Verdier dual coalgebra via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 554 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 613 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 643 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 734 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 824 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:bg-bar-coalg` | `proposition` | 277 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex coalgebra |
| `prop:chiral-operad-genus0` | `proposition` | 377 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 421 | Prism principle: operadic identification |
| `thm:prism-higher-genus` | `theorem` | 661 | Prism principle: higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | 733 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | 758 | The loop expansion is the genus expansion |
| `cor:prism-principle` | `corollary` | 863 | The prism principle |
| `thm:modular-convolution-structure` | `theorem` | 986 | dg~Lie structure |
| `thm:vol1-genus-completion` | `theorem` | 1026 | Genus completion |
| `prop:vol1-structure-as-MC` | `proposition` | 1074 | The algebra structure as MC element |
| `thm:partition` | `theorem` | 1180 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:quantum-linfty-master` | `theorem` | 640 | Quantum $L_\infty$ master equation |
| `prop:two-element-strict` | `proposition` | 886 | Two-element covers are strict |
| `prop:borcherds-shadow-identification` | `proposition` | 1370 | Secondary Borcherds operations as shadow obstruction tower obstructions |

#### `chapters/theory/shadow_L_function_platonic.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:shL-convergence-half-plane` | `proposition` | 157 | \label{prop:shL-convergence-half-plane}Convergence half-plane |
| `thm:shadow-L-analytic-continuation` | `theorem` | 239 | \label{thm:shadow-L-analytic-continuation}Meromorphic continuation of $\Lsh(\Vir_c; s)$ |
| `thm:trivial-zeros-structure` | `theorem` | 349 | \label{thm:trivial-zeros-structure}Trivial zeros of $\Lsh(\Vir_c; s)$ |
| `thm:Fg-from-L-sh-correctly` | `theorem` | 452 | \label{thm:Fg-from-L-sh-correctly}Mellin-residue bridge: $F_g$ from $\Lsh$ |
| `thm:kummer-congruence-prediction` | `theorem` | 627 | \label{thm:kummer-congruence-prediction}Kummer congruences from the Mellin-residue bridge |
| `cor:shadow-L-motivic-upgrade` | `corollary` | 722 | \label{cor:shadow-L-motivic-upgrade}Motivic shadow $L$-function is entire except at $s = 2$ |

#### `chapters/theory/shadow_tower_higher_coefficients.tex` (41)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-shadow-recurrence` | `theorem` | 175 | \label{thm:virasoro-shadow-recurrence}Virasoro shadow recurrence |
| `thm:s6-virasoro-closed-form` | `theorem` | 249 | \label{thm:s6-virasoro-closed-form}Closed form for $S_6(\Vir_c)$ |
| `thm:s7-virasoro-closed-form` | `theorem` | 316 | \label{thm:s7-virasoro-closed-form}Closed form for $S_7(\Vir_c)$ |
| `thm:s8-virasoro-closed-form` | `theorem` | 385 | \label{thm:s8-virasoro-closed-form}Closed form for $S_8(\Vir_c)$ |
| `prop:sth-boundary-checks` | `proposition` | 508 | \label{prop:sth-boundary-checks}Boundary values through weight 8 |
| `prop:sth-leading-asymp` | `proposition` | 566 | \label{prop:sth-leading-asymp}Leading large-$c$ asymptotic coefficient |
| `thm:shadow-exponential-base-Virasoro` | `theorem` | 633 | \label{thm:shadow-exponential-base-Virasoro} The shadow-exponential base of Virasoro is $C_\Vir = 6$ |
| `thm:universal-class-M-C-is-6` | `theorem` | 677 | \label{thm:universal-class-M-C-is-6} Universal class M shadow-exponential base |
| `prop:W3-T-line-matches-Vir-subleading` | `proposition` | 734 | \label{prop:W3-T-line-matches-Vir-subleading} $\cW_3$ $T$-line subleading asymptotic matches Virasoro |
| `thm:shadow-series-closed-form-Virasoro` | `theorem` | 814 | \label{thm:shadow-series-closed-form-Virasoro} Closed-form Virasoro shadow series |
| `thm:shadow-series-closed-form-Virasoro-subleading` | `theorem` | 871 | \label{thm:shadow-series-closed-form-Virasoro-subleading} Closed-form subleading Virasoro shadow series |
| `thm:pole-doubling-all-k` | `theorem` | 967 | \label{thm:pole-doubling-all-k} Pole-doubling pattern for all $k$ |
| `prop:phi-k-leading-coefficient-arithmetic` | `proposition` | 1014 | \label{prop:phi-k-leading-coefficient-arithmetic} Arithmetic of the leading $\varphi_k$ coefficient |
| `cor:arithmetic-uniformity-class-M` | `corollary` | 1098 | \label{cor:arithmetic-uniformity-class-M} $\{2, 3\}$-adic arithmetic is uniform across universal class M stratum |
| `prop:C-A-inverse-radius` | `proposition` | 1235 | \label{prop:C-A-inverse-radius} $C_\cA$ is the inverse radius of convergence of the shadow series |
| `thm:w3-wline-closed-form` | `theorem` | 1868 | \label{thm:w3-wline-closed-form} $W_3$ $W$-line integer sequence closed form |
| `thm:w3-wline-exponential-base` | `theorem` | 1920 | \label{thm:w3-wline-exponential-base} $W$-line shadow-exponential base $C_{W_3}^{W\text{-line}} = 12$ |
| `thm:w3-wline-generating-function` | `theorem` | 1960 | \label{thm:w3-wline-generating-function} Exact generating-function closed form for the $W$-line sequence |
| `cor:w3-wline-self-consistency` | `corollary` | 2012 | \label{cor:w3-wline-self-consistency} Riccati self-consistency at the radius of convergence |
| `prop:sth-virasoro-rational-through-8` | `proposition` | 2318 | \label{prop:sth-virasoro-rational-through-8}No motivic period enters Virasoro through weight 8 |
| `prop:sth-summary` | `proposition` | 2375 | \label{prop:sth-summary}Closed-form Virasoro shadow spectrum through weight 8 |
| `thm:s-r-kummer-absent-through-r-11` | `theorem` | 2435 | \label{thm:s-r-kummer-absent-through-r-11}The first two Kummer-irregular primes $\{691, 3617\}$ are absent from $S_r(\Vir_c)$ through $r = 11$ |
| `thm:s9-virasoro-closed-form` | `theorem` | 2683 | \label{thm:s9-virasoro-closed-form}Closed form for $S_9(\Vir_c)$ |
| `thm:s10-virasoro-closed-form` | `theorem` | 2746 | \label{thm:s10-virasoro-closed-form}Closed form for $S_{10}(\Vir_c)$ |
| `thm:s11-virasoro-closed-form` | `theorem` | 2796 | \label{thm:s11-virasoro-closed-form}Closed form for $S_{11}(\Vir_c)$ |
| `thm:shadow-tower-asymptotic-closed-form` | `theorem` | 2833 | \label{thm:shadow-tower-asymptotic-closed-form}Closed form for the leading asymptotic |
| `cor:virasoro-23-smoothness` | `corollary` | 2903 | \label{cor:virasoro-23-smoothness}Every leading numerator is $\{2, 3\}$-smooth |
| `cor:virasoro-motivic-purity-r-leq-11` | `corollary` | 2934 | \label{cor:virasoro-motivic-purity-r-leq-11}Motivic purity through weight 11 (SPECIAL CASE of Theorem~\ref{thm:virasoro-motivic-rationality-all-r}) |
| `lem:subleading-combinatorial-identity` | `lemma` | 3006 | \label{lem:subleading-combinatorial-identity}Combinatorial identity for the subleading source |
| `thm:shadow-tower-subleading-closed-form` | `theorem` | 3032 | \label{thm:shadow-tower-subleading-closed-form}Closed form for the subleading asymptotic |
| `cor:subleading-characteristic-primes` | `corollary` | 3150 | \label{cor:subleading-characteristic-primes}Riccati- arithmetic primes of the subleading layer |
| `lem:sub-subleading-cubic-identity` | `lemma` | 3286 | \label{lem:sub-subleading-cubic-identity} Cubic combinatorial identity |
| `cor:kummer-emergence-at-r-8` | `corollary` | 3333 | \label{cor:kummer-emergence-at-r-8}Emergence of the Kummer-irregular prime $691$ at $\Gamma_{8}$ |
| `cor:tier-3-characteristic-primes` | `corollary` | 3385 | \label{cor:tier-3-characteristic-primes}Tier-3 prime content through $r = 11$ |
| `thm:shadow-tower-tier-4-closed-form` | `theorem` | 3424 | \label{thm:shadow-tower-tier-4-closed-form}Closed form for the Tier-4 sub-sub-subleading asymptotic |
| `lem:quintic-combinatorial` | `lemma` | 3484 | \label{lem:quintic-combinatorial}Quintic combinatorial identities |
| `thm:kummer-laurent-depth-controlled` | `theorem` | 3571 | \label{thm:kummer-laurent-depth-controlled}% Laurent-depth-controlled Kummer emergence |
| `cor:bernoulli-leading-duality-sharpness` | `corollary` | 3695 | \label{cor:bernoulli-leading-duality-sharpness}% Sharpness of the Bernoulli-leading arithmetic duality |
| `lem:floor-parity-subadditive` | `lemma` | 3798 | \label{lem:floor-parity-subadditive}Parity subadditivity of the floor |
| `cor:floor-shift-j-plus-k` | `corollary` | 3825 | \label{cor:floor-shift-j-plus-k}Floor shift on the index set of the shadow recurrence |
| `thm:s-r-rational-denominator-pattern` | `theorem` | 3846 | \label{thm:s-r-rational-denominator-pattern}Rational denominator pattern for the Virasoro shadow tower |

#### `chapters/theory/shadow_tower_other_class_M_platonic.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:shadow-tower-master-equation-classM` | `proposition` | 56 | Shadow-tower master equation, class-M form |
| `prop:w3-tline-virasoro-inheritance` | `proposition` | 128 | $W_3$ $T$-line: full inheritance of the Virasoro tower |
| `cor:w3-tline-asymptotic` | `corollary` | 157 | $T$-line asymptotic, $W_3$ |
| `prop:w3-wline-closed-form` | `proposition` | 176 | $W_3$ $W$-line: closed-form coefficients through $r = 10$ |
| `prop:w3-wline-leading-asymptotic` | `proposition` | 218 | $W_3$ $W$-line leading large-$c$ behaviour |
| `prop:bp-tline-rational` | `proposition` | 288 | BP $T$-line: rationality in $k$ |
| `cor:bp-tline-koszul-conductor` | `corollary` | 311 | BP $T$-line: Koszul conductor, Feigin--Frenkel duality |
| `prop:bp-jline-gaussian` | `proposition` | 326 | BP $J$-line: Gaussian, depth 2 |
| `prop:wn-line-decomposition` | `proposition` | 369 | $W_N$ line decomposition of $\kappa$ |
| `prop:wn-tline-and-w-lines` | `proposition` | 392 | $W_N$ $T$-line and principal $W$-lines |
| `prop:w-infinity-line-decomposition` | `proposition` | 448 | $W_\infty[\mu |
| `thm:shadow-tower-w-infinity-asymptotic` | `theorem` | 468 | $W_\infty[\mu |
| `prop:super-yangian-kappa` | `proposition` | 554 | Super-Yangian modular characteristic |
| `prop:super-yangian-tline-shadow` | `proposition` | 576 | Super-Yangian $T$-line: Virasoro shadow with graded parity |
| `prop:super-yangian-fermionic-line` | `proposition` | 599 | Super-Yangian fermionic-line shadow: sign-reversed Wick |
| `cor:super-yangian-tline-asymptotic` | `corollary` | 628 | Super-Yangian leading $T$-line asymptotic |
| `thm:universal-asymptotic-factor` | `theorem` | 644 | Universal asymptotic factor for class-M algebras |
| `cor:universal-asymptotic-factor` | `corollary` | 714 | Universal asymptotic factor |
| `prop:wp-cartan-shadow-through-r6` | `proposition` | 831 | $W(p)$ Cartan-line shadow coefficients through weight six |
| `rem:wp-cross-channel-quartic` | `remark` | 948 | Cross-channel quartic on the $T$-$W$ mixed line |

#### `chapters/theory/shadow_tower_quadrichotomy_platonic.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:s2-s3-roles` | `proposition` | 214 | $S_2$ as the curvature, $S_3$ as the cubic colour |
| `thm:riccati-master` | `theorem` | 245 | Riccati master equation |
| `prop:riccati-three-presentations` | `proposition` | 294 | Three equivalent presentations |
| `thm:quadrichotomy` | `theorem` | 362 | Quadrichotomy of standard-landscape chirally Koszul vertex algebras |
| `prop:moduli-stratification-codim` | `proposition` | 486 | Moduli stratification, codimension count |
| `thm:spectral-hyperelliptic-pf` | `theorem` | 602 | Spectral hyperelliptic curve and Picard--Fuchs |
| `cor:branch-points-instantons` | `corollary` | 655 | Branch points and instanton actions |
| `prop:c1-riccati-mc` | `proposition` | 720 | C1: Riccati MC element |
| `thm:borel-summability-classM` | `theorem` | 796 | C3: Borel summability of class M, asymptotic regime |
| `thm:c4-shadow-feynman-gk` | `theorem` | 880 | C4: Shadow--Feynman as $\partial^{2} = 0$ at $b_1 = L$ |

#### `chapters/theory/shadow_tower_sub_subleading_platonic.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:phi-recurrence` | `lemma` | 121 | \label{lem:phi-recurrence}Phi-recurrence |
| `prop:gamma-recurrence` | `proposition` | 153 | \label{prop:gamma-recurrence}Gamma recurrence |
| `lem:gamma-source-ratio-closed-form` | `lemma` | 183 | \label{lem:gamma-source-ratio-closed-form}Source-ratio closed form |
| `thm:shadow-tower-sub-subleading-closed-form` | `theorem` | 247 | \label{thm:shadow-tower-sub-subleading-closed-form} Sub-subleading Virasoro shadow asymptotic |
| `lem:gamma-numerator-quartic-polynomial` | `lemma` | 372 | \label{lem:gamma-numerator-quartic-polynomial}Gamma numerator polynomial |
| `lem:gamma-numerator-irreducible` | `lemma` | 400 | \label{lem:gamma-numerator-irreducible}Irreducibility over $\mathbb{Q}$ |
| `rem:gamma-691-emergence-sporadic` | `remark` | 420 | \label{rem:gamma-691-emergence-sporadic}The $691$ at $r = 8$ is a modular coincidence |
| `rem:gamma-irregular-primes-dense-but-structureless` | `remark` | 444 | \label{rem:gamma-irregular-primes-dense-but-structureless} Irregular primes appear densely but structurelessly |

#### `chapters/theory/spectral_sequences.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ss` | `theorem` | 277 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 329 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 399 | Central charge and \texorpdfstring{$d_1$}{d1} |

#### `chapters/theory/theorem_A_infinity_2.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:koszul-reflection` | `theorem` | 148 | Theorem~A: the Koszul Reflection ($K^{2}\simeq\mathrm{id}$) |
| `cor:eight-cor-twisting-morphism` | `corollary` | 325 | Twisting morphism $\tau\colon\Bbarch_X(\cA)\to\cA$ is a Maurer--Cartan element |
| `cor:eight-cor-counit-qi` | `corollary` | 352 | Counit quasi-isomorphism on $\Kosz(X)$ |
| `cor:eight-cor-unit-weq` | `corollary` | 368 | Unit weak equivalence on $\Conil(X)$ |
| `cor:eight-cor-twisted-tensor` | `corollary` | 384 | Twisted tensor acyclicity |
| `cor:eight-cor-bar-weight-1` | `corollary` | 410 | Bar concentrated in weight~$1$ at $g=0$ on class~$\mathsf{G}$ |
| `cor:eight-cor-sc-formality` | `corollary` | 442 | SC-formality on class~$\mathsf{G}$ only |
| `cor:eight-cor-R-descent` | `corollary` | 470 | $R$-twisted $\Sigma_n$-descent (unitary $R$) $\barB^{\Sigma}(\cA)\simeq B^{\ord}(\cA)^{R\text{-}\Sigma_n}$ |
| `cor:eight-cor-properad-equiv` | `corollary` | 501 | Francis--Gaitsgory $(\infty,2)$-equivalence at properad level |
| `thm:A-infinity-2` | `theorem` | 735 | Theorem~$A^{\infty,2}$: Francis--Gaitsgory bar--cobar $(\infty,2)$-equivalence at properad level |
| `cor:classical-A-from-A-infinity-2` | `corollary` | 1162 | Classical Theorem~A from Theorem~$A^{\infty,2}$ |
| `lem:R-twisted-descent` | `lemma` | 1200 | $R$-matrix-twisted $\Sigma_n$-descent, unitary $R$ |
| `cor:ainf2-downstream-list` | `corollary` | 1356 | Downstream corollaries of $A^{\infty,2}$ |
| `cor:chiral-KK-formal-smoothness` | `corollary` | 1648 | Chiral Koszulness implies properad-level formal smoothness |

#### `chapters/theory/theorem_B_scope_platonic.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-positselski-at-each-weight` | `theorem` | 179 | Chiral Positselski at each finite weight |
| `thm:chiral-positselski-weight-completed` | `theorem` | 245 | Chiral Positselski on the weight-completed bar coalgebra |
| `prop:chiral-positselski-raw-direct-sum-class-M-false` | `proposition` | 381 | Raw direct-sum chiral Positselski fails for class M at chain level |

#### `chapters/theory/theorem_C_refinements_platonic.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `ch:theorem-C-refinements-platonic` | `conjecture` | 52 | — |

#### `chapters/theory/theorem_h_off_koszul_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:theorem-h-on-koszul-locus` | `theorem` | 145 | Theorem~H on the Koszul locus; sharp bigraded Hilbert series |
| `thm:theorem-h-off-koszul-explicit-correction` | `theorem` | 193 | Theorem~H off the Koszul locus; explicit correction |
| `thm:theorem-h-logarithmic-w(p)` | `theorem` | 329 | Theorem~H for logarithmic $\cW(p)$ |
| `thm:theorem-h-at-critical-level` | `theorem` | 467 | Theorem~H at critical level |
| `thm:theorem-h-platonic-unified` | `theorem` | 605 | Platonic Theorem~H; unified Hilbert series |

#### `chapters/theory/three_hochschild_unification_platonic.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:three-hochschild-chain-level-agreement-low-degree` | `theorem` | 170 | Chain-level agreement in low degrees on the Koszul locus |
| `thm:three-hochschild-cohomological-agreement-all-degree` | `theorem` | 307 | Cohomological agreement on the full range on the Koszul locus |
| `prop:three-hochschild-high-degree-divergence` | `proposition` | 363 | High-degree divergence of the three theories |
| `thm:critical-level-ff-center-unification` | `theorem` | 423 | Critical-level unification in degree zero |

#### `chapters/theory/three_invariants.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:three-invariants-relations` | `proposition` | 188 | Relations and independence |
| `thm:k-max-trichotomy` | `theorem` | 334 | The $k_{\max}$ trichotomy |
| `thm:fingerprint-completeness` | `theorem` | 412 | Fingerprint completeness |
| `thm:five-class-stratum` | `theorem` | 483 | Five-class stratum |
| `prop:coarse-projection-functor` | `proposition` | 520 | Coarse projection functor |

#### `chapters/theory/topologization_chain_level_platonic.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:QG1-remainder` | `proposition` | 239 | Explicit $Q$-variation of $G_1$ |
| `prop:eta-i-primitive` | `proposition` | 328 | $\eta_1^{(\mathrm i)}$ is a $Q$-primitive of $R_{\mathrm{ghost}}$ |
| `prop:eta-ii-primitive` | `proposition` | 391 | $\eta_1^{(\mathrm{ii})}$ is a $Q$-primitive of $R_{\mathrm{self}}$ |
| `cor:eta-primitive` | `corollary` | 415 | $\eta_1$ is a $Q$-primitive of $R_1 := R_{\mathrm{ghost}} + R_{\mathrm{self}}$ |
| `thm:sugawara-antighost-primitive-chain-level` | `theorem` | 427 | Sugawara antighost primitive, chain level |
| `prop:translation-inv-tildeG` | `proposition` | 461 | Translation invariance of $\widetilde G_1$ |
| `thm:chain-level-E3-top-class-L` | `theorem` | 484 | Chain-level $\Ethree^{\mathrm{top}}$ for class $L$ |
| `prop:eta-formula-sl2-k1-explicit` | `proposition` | 543 | $\eta_1$ formula at sl$_2$ level $1$ |
| `prop:critical-level-collapse` | `proposition` | 600 | Critical-level collapse to $\Etwo^{\mathrm{top}}$ |

#### `chapters/theory/universal_conductor_K_platonic.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:uc-universal-conductor` | `theorem` | 252 | \textbf{Universal Conductor} |
| `thm:uc-trinity` | `theorem` | 376 | \textbf{Trinity: per-family} |

#### `chapters/theory/virasoro_motivic_purity.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-motivic-purity` | `theorem` | 210 | \label{thm:virasoro-motivic-purity}Virasoro motivic purity |
| `prop:denominator-structure` | `proposition` | 315 | \label{prop:denominator-structure}Denominator of $S_r(\Vir_c)$ |
| `thm:virasoro-riccati-transport-rationality` | `theorem` | 423 | \label{thm:virasoro-riccati-transport-rationality} Rationality of the Riccati transport operator on Virasoro |
| `cor:virasoro-no-mzv-contribution` | `corollary` | 502 | \label{cor:virasoro-no-mzv-contribution}Motivic coaction on Virasoro shadow tower is trivial |
| `cor:vir-purity-propagates-to-dress-reduced` | `corollary` | 603 | \label{cor:vir-purity-propagates-to-dress-reduced} Motivic purity in the Drinfeld--Sokolov reduction chain |

#### `chapters/theory/virasoro_motivic_purity_all_r_platonic.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-s-r-motivic-purity-all-r` | `theorem` | 208 | \label{thm:virasoro-s-r-motivic-purity-all-r}Virasoro shadow-tower motivic purity, all $r \geq 2$ via master-equation recursion |
| `thm:class-M-motivic-purity-algebras-with-Q-rational-OPE` | `theorem` | 319 | \label{thm:class-M-motivic-purity-algebras-with-Q-rational-OPE} Motivic purity for class-M chirally Koszul algebras with $\mathbb{Q}$-rational OPE |
| `cor:vmpar-concrete-Q-rational-families` | `corollary` | 373 | \label{cor:vmpar-concrete-Q-rational-families} Concrete families with all-$r$ motivic purity |
| `prop:mzv-would-enter-at-what-weight` | `proposition` | 417 | \label{prop:mzv-would-enter-at-what-weight} Virasoro shadow coefficients contain no odd-zeta of any weight |
| `thm:structural-reason-for-purity` | `theorem` | 466 | \label{thm:structural-reason-for-purity}The shadow tower is associator-free; motivic content can enter only through the chiral coproduct |
| `cor:item-19-closed` | `corollary` | 590 | \label{cor:item-19-closed}Item 19 of the platonic- reconstitution frontier list is closed |

#### `chapters/theory/z_g_kummer_bernoulli_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:z-g-closed-form-polynomial` | `theorem` | 62 | $Z_g(k)$ closed form |
| `thm:z-g-polynomial-form` | `theorem` | 147 | Polynomial factorisation of $Z_g$ |
| `thm:z-g-leading-coefficient-bernoulli` | `theorem` | 209 | Hurwitz--Bernoulli leading coefficient |
| `thm:z-g-kummer-congruence` | `theorem` | 339 | Irregular-prime witnesses |
| `thm:z-g-s-r-arithmetic-duality` | `theorem` | 573 | $Z_g$ vs $S_r(\Vir_c)$ arithmetic duality at the leading Kummer-irregular primes |

### Part II: Examples (715)

#### `chapters/examples/bar_complex_tables.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 694 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 786 | Modular rank of \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 865 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 925 | PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} |
| `comp:sl3-casimir-decomp` | `computation` | 1018 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | 1100 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | 1426 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1731 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1777 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | 1848 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | 1899 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2034 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2070 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2104 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2533 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2739 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2959 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 3013 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3050 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3420 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3599 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3896 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3960 | Universal bar complex dimension formula |
| `comp:bar-cohomology-gfs` | `computation` | 4106 | Bar cohomology generating functions across standard families |
| `prop:bar-bgg-sl2` | `proposition` | 4267 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4417 | BGG involution under Koszul duality |

#### `chapters/examples/bershadsky_polyakov.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bp-koszul-conductor-polynomial` | `theorem` | 205 | Bershadsky--Polyakov Koszul-conductor polynomial identity;\ |
| `prop:bp-self-duality` | `proposition` | 253 | BP Koszul self-duality;\ |
| `prop:bp-kappa` | `proposition` | 311 | Modular characteristic of $\mathcal{B}^k$;\ |
| `prop:bp-complementarity` | `proposition` | 344 | Complementarity;\ |
| `prop:bp-tline-depth` | `proposition` | 378 | T-line shadow depth;\ |
| `prop:bp-jline-depth` | `proposition` | 416 | J-line shadow depth;\ |
| `prop:bp-sigma` | `proposition` | 462 | Sigma non-vanishing;\ |
| `prop:bp-hook-series` | `proposition` | 542 | Self-transpose hooks;\ |

#### `chapters/examples/beta_gamma.tex` (27)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 373 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 424 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 459 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 512 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 550 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | 571 | — |
| `thm:cobar-fermions` | `theorem` | 599 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | 636 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 725 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 992 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 1112 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 1219 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1365 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1449 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1600 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |
| `prop:mumford-exponent-complementarity` | `proposition` | 1774 | Mumford exponent complementarity |
| `thm:betagamma-quartic-birth` | `theorem` | 2111 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | 2146 | $\beta\gamma$ weight-changing line is shadow-trivial |
| `prop:betagamma-primitive-kernel` | `proposition` | 2181 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive kernel |
| `prop:betagamma-primitive-shell` | `proposition` | 2229 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive shell equations |
| `lem:betagamma-ell2-vanishing` | `lemma` | 2376 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | 2423 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | 2533 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | 2575 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | 2605 | Pure contact boundary law |
| `prop:betagamma-sugawara-class-c` | `proposition` | 2683 | Why $\beta\gamma$ is class~$\mathsf{C}$: standard conformal-weight family |
| `prop:betagamma-translation-coproduct` | `proposition` | 2796 | Translation and coproduct |

#### `chapters/examples/chiral_moonshine_unified.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:bar-euler-hilbert` | `proposition` | 193 | Bar-Euler product = Hilbert series |
| `thm:moonshine-bar-euler-master` | `theorem` | 244 | Master bar-Euler moonshine identity |
| `thm:conway-chiral-structure` | `theorem` | 546 | Conway chiral structure |
| `thm:thompson-chiral` | `theorem` | 603 | Thompson chiral refinement |
| `cor:kummer-congruence-moonshine` | `corollary` | 852 | Kummer-congruence moonshine |

#### `chapters/examples/deformation_quantization.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 134 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 187 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 419 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 536 | Genus expansion |
| `prop:jacobi-nilpotent` | `proposition` | 1366 | $b_F^2 = 0$ is automatic |
| `lem:dcrit-boundary-linear` | `lemma` | 1740 | dCrit for boundary-linear $W$ |
| `thm:boundary-linear-lg` | `theorem` | 1833 | Boundary-linear LG theorem |

#### `chapters/examples/deformation_quantization_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 465 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 537 | Deformation--duality compatibility |

#### `chapters/examples/exceptional_yangian_koszul_duality_platonic.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:exceptional-yangian-template` | `proposition` | 117 | Four-step template for Yangian Koszul duality |
| `cor:exceptional-yangian-graded` | `corollary` | 221 | Exceptional-type graded identification |
| `prop:exceptional-yangian-koszul-E6` | `proposition` | 262 | $E_6$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-E7` | `proposition` | 302 | $E_7$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-E8` | `proposition` | 335 | $E_8$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-F4` | `proposition` | 385 | $F_4$ Yangian Koszul duality |
| `prop:exceptional-yangian-koszul-G2` | `proposition` | 432 | $G_2$ Yangian Koszul duality |
| `thm:exceptional-yangian-koszul-duality-all-five-types` | `theorem` | 477 | Exceptional-type Yangian Koszul duality, all five types |
| `cor:exceptional-yangian-all-simple` | `corollary` | 507 | All-simple-type unconditional closure |

#### `chapters/examples/free_fields.tex` (66)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fermion-shadow-invariants` | `proposition` | 234 | Shadow invariants of the free fermion |
| `prop:fermion-shadow-metric` | `proposition` | 313 | Shadow metric of the free fermion |
| `thm:fermion-genus-expansion` | `theorem` | 348 | Free fermion genus expansion |
| `prop:fermion-rmatrix` | `proposition` | 426 | Free fermion $r$-matrix |
| `prop:fermion-complementarity` | `proposition` | 481 | Free fermion complementarity |
| `thm:fermion-sewing` | `theorem` | 551 | Free fermion sewing |
| `prop:fermion-characteristic-data` | `proposition` | 638 | Free fermion characteristic data |
| `thm:single-fermion-boson-duality` | `theorem` | 846 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | 898 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 954 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 1005 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 1016 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `prop:betagamma-deformation-channels` | `proposition` | 1094 | $\beta\gamma$ deformation complex |
| `prop:betagamma-T-line-shadows` | `proposition` | 1136 | $\beta\gamma$ shadow obstruction tower: T-line data |
| `prop:betagamma-weight-line-shadows` | `proposition` | 1171 | $\beta\gamma$ shadow obstruction tower: weight-changing line |
| `prop:betagamma-shadow-metric` | `proposition` | 1243 | $\beta\gamma$ shadow metric |
| `comp:betagamma-shadow-weights` | `computation` | 1279 | $\beta\gamma$ shadow obstruction tower: special weight table |
| `prop:betagamma-weight-symmetry` | `proposition` | 1315 | Weight symmetry $\neq$ Koszul duality |
| `thm:heisenberg-bar` | `theorem` | 1401 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 1424 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | 1466 | Heisenberg curved structure |
| `thm:lattice-voa-bar` | `theorem` | 1513 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1542 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | 1572 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1609 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | 1658 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 1682 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 1897 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 1973 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 2005 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 2142 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 2197 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 2247 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 2289 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 2442 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 2518 | Spectral flow under Koszul duality |
| `thm:heisenberg-not-self-dual` | `theorem` | 2752 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2860 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2891 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 3153 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 3267 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 3552 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 3701 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 3756 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3824 | Heisenberg level inversion: curved duality |
| `thm:fermion-genus1-partition` | `theorem` | 3973 | Free fermion genus-1 partition functions |
| `thm:fermion-F1-shadow` | `theorem` | 4105 | Free fermion genus-1 free energy |
| `thm:fermion-genus-g` | `theorem` | 4183 | Free fermion at genus $g$ |
| `thm:virasoro-moduli` | `theorem` | 4532 | Critical Virasoro descent at $c = 26$ |
| `prop:moduli-degeneration` | `proposition` | 4630 | Boundary-residue differential on moduli forms |
| `thm:algebraic-string-dictionary` | `theorem` | 4759 | Algebraic bar/BRST genus dictionary |
| `thm:genus-g-chiral-homology` | `theorem` | 4866 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 4978 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 5058 | Bar classes on moduli and boundary factorization |
| `thm:modular-invariance` | `theorem` | 5186 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 5223 | Modular anomaly for affine Kac--Moody algebras |
| `thm:wakimoto-bar` | `theorem` | 5343 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 5356 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 5361 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 5388 | Higher \texorpdfstring{$A_\infty$}{A-infinity} corrections in quantum \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `comp:heisenberg-five-theorems` | `computation` | 5439 | Five projections of $\Theta_{\cH_k}$ |
| `comp:fermion-five-theorems` | `computation` | 5502 | Five projections of $\Theta_{\mathcal{F}}$ |
| `comp:betagamma-five-theorems` | `computation` | 5544 | Five projections of $\Theta_{\beta\gamma}$ |
| `comp:bc-five-theorems` | `computation` | 5595 | Five projections of $\Theta_{bc}$ |
| `comp:lattice-five-theorems` | `computation` | 5642 | Five projections of $\Theta_{V_\Lambda}$ |
| `thm:filtered-bar-complex` | `theorem` | 5723 | Filtered bar complex |

#### `chapters/examples/genus_expansions.tex` (40)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 99 | Heisenberg free energy at all genera |
| `__unlabeled_chapters/examples/genus_expansions.tex:169` | `proposition` | 169 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `__unlabeled_chapters/examples/genus_expansions.tex:211` | `theorem` | 211 | Lattice VOA free energy |
| `__unlabeled_chapters/examples/genus_expansions.tex:245` | `corollary` | 245 | Lattice-independence of genus expansion |
| `__unlabeled_chapters/examples/genus_expansions.tex:266` | `theorem` | 266 | Uniform-weight $\mathcal{W}$-algebra free energy |
| `thm:sl2-all-genera` | `theorem` | 468 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 620 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 764 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 806 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 860 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 971 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 1081 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1221 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1288 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1353 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-$2$ free energy |
| `prop:w3-genus3-cross-channel` | `proposition` | 1436 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-$3$ cross-channel correction |
| `prop:w3-genus4-cross-channel` | `proposition` | 1488 | Genus-4 cross-channel correction |
| `comp:w4-w5-grav-cross` | `computation` | 1560 | Universal gravitational cross-channel: $\cW_4$ and $\cW_5$ specializations |
| `comp:w4-full-ope-examples` | `computation` | 1634 | $\cW_4$ full-OPE cross-channel: the first irrational correction |
| `comp:genus2-complementarity-table` | `computation` | 1698 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1831 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1863 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1881 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1918 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 2015 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 2143 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 2187 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 2277 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 2429 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2495 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:universal-fe-ratios` | `proposition` | 2742 | Universal free-energy ratios |
| `prop:complementarity-classification` | `proposition` | 3089 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 3134 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 3434 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 3538 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 3554 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 3580 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 3612 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 3708 | Loop expansion interpretation |
| `thm:boundary-characters-bar-hilbert` | `theorem` | 3880 | Boundary characters as bar Hilbert series |

#### `chapters/examples/heisenberg_eisenstein.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:heisenberg-gaussian-termination` | `proposition` | 95 | Gaussian shadow termination for Heisenberg |
| `thm:heisenberg-sewing` | `theorem` | 215 | Heisenberg sewing theorem |
| `prop:heisenberg-r-matrix` | `proposition` | 275 | Heisenberg $r$-matrix |
| `prop:heisenberg-complementarity` | `proposition` | 316 | Heisenberg complementarity |
| `thm:heisenberg-genus-one-complete` | `theorem` | 458 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 545 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 587 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 705 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 808 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 857 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 1186 | Multi-boson Eisenstein corrections |
| `thm:heisenberg-exact-linearity` | `theorem` | 1513 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | 1553 | Heisenberg shadow obstruction tower: finite termination at degree~$2$ |
| `cor:heisenberg-gaussian-boundary` | `corollary` | 1778 | Gaussian boundary law |
| `prop:heisenberg-primitive-kernel` | `proposition` | 1890 | Heisenberg primitive kernel |
| `prop:heisenberg-primitive-shell` | `proposition` | 1927 | Heisenberg primitive shell equations |
| `prop:heisenberg-open-sector` | `proposition` | 2016 | Open-sector category for Heisenberg |
| `thm:heisenberg-modular-cooperad` | `theorem` | 2145 | CT-$2$ for Heisenberg: modular cooperad on $\Cop(\cH_\kappa)$; \textup{(}UNIFORM-WEIGHT\textup{}) |

#### `chapters/examples/kac_moody.tex` (55)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:km-genus1-hessian` | `computation` | 279 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `thm:geometric-ope-kac-moody` | `theorem` | 510 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 544 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 584 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 657 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 859 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 890 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 928 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 986 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 1022 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 1151 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | 1185 | Killing form via structure constants |
| `prop:verdier-level-identification` | `proposition` | 1270 | Verdier level identification |
| `prop:ff-channel-shear` | `proposition` | 1626 | Feigin--Frenkel shear on channel pair |
| `prop:exceptional-shadow-invariants` | `proposition` | 1677 | Exceptional shadow invariants |
| `thm:screening-bar` | `theorem` | 1847 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 1913 | Critical fixed point for principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:kac-moody-ainfty` | `theorem` | 1982 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 2021 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 2075 | Closed-form OPE for Koszul dual |
| `comp:sl2-collision-residue-kz` | `computation` | 2134 | Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:km-quantum-groups` | `theorem` | 2428 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 2816 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 2888 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 3070 | Kac--Wakimoto formula at \texorpdfstring{$k=-1/2$}{k=-1/2} via bar spectral sequence |
| `prop:admissible-verlinde-bar` | `proposition` | 3242 | Admissible \texorpdfstring{$S$}{S}-matrix and Verlinde fusion package at \texorpdfstring{$k=-1/2$}{k=-1/2} |
| `prop:bar-whittaker` | `proposition` | 3664 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 3745 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 3813 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 3883 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 3949 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 4012 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 4058 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 4097 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 4134 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 4343 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 4373 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 4403 | Local oper differential-form identification |
| `thm:affine-cubic-normal-form` | `theorem` | 4668 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | 4704 | Affine shadow obstruction tower: finite termination at degree~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | 4742 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | 4784 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | 4854 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 4902 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 4959 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 5036 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 5122 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 5158 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 5324 | Vanishing of the genus loop on the affine cubic |
| `prop:km-cubic-shadow-level-independence` | `proposition` | 5389 | Level-independence of the cubic shadow product |
| `prop:nsl-shadow-tower` | `proposition` | 5514 | Non-simply-laced shadow obstruction tower |
| `prop:complete-exceptional-shadow` | `proposition` | 5657 | Complete exceptional shadow data |
| `prop:exceptional-anomaly-ratios` | `proposition` | 5744 | Anomaly ratios for exceptional principal $\mathcal{W}$-algebras |
| `cor:level-rank-bar-intertwining` | `corollary` | 5996 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | 6024 | Kappa anti-symmetry under Feigin--Frenkel involution |

#### `chapters/examples/landscape_census.tex` (23)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:minimal-model-class-transport` | `proposition` | 402 | Minimal-model class transport |
| `prop:paired-standard-mc4-frontier` | `proposition` | 1069 | Paired standard-tower MC4 completion packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 1189 | Minimal closure conditions for the standard-tower MC4 completion target |
| `cor:anomaly-ratio-ds` | `corollary` | 1454 | Anomaly ratio and DS reduction |
| `cor:genus1-anomaly-ratio` | `corollary` | 1468 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `thm:census-witness-complementarity` | `theorem` | 1522 | Witness-family complementarity from Verdier duality |
| `cor:subexp-free-field` | `corollary` | 2468 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 2478 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 2495 | DS reduction and bar cohomology generating functions |
| `thm:ds-spectral-branch-preservation` | `theorem` | 2662 | DS preservation of the sub-discriminant |
| `prop:ds-invariant-discriminant` | `proposition` | 2816 | DS-invariant discriminant subfactor |
| `prop:hred-sl2` | `proposition` | 2860 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `thm:bar-gf-classification` | `theorem` | 3075 | Bar cohomology generating function classification |
| `prop:discriminant-characteristic` | `proposition` | 3280 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 3371 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 3468 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 3534 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 3589 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 3640 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 3655 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 3744 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 3933 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 4242 | Spectral sequence collapse |

#### `chapters/examples/lattice_foundations.tex` (45)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lattice-sewing` | `theorem` | 107 | Lattice sewing envelope |
| `lem:lattice:cocycle-class` | `lemma` | 378 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 542 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 761 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 858 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 881 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 916 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 950 | Dual coalgebra of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 1001 | Koszul morphism for lattice algebras |
| `rem:lattice:koszul-dual-kappa` | `remark` | 1046 | Koszul dual kappa for non-unimodular lattices |
| `rem:lattice:dual-structure` | `remark` | 1110 | Structural form of the lattice Koszul dual |
| `thm:lattice:direct-sum` | `theorem` | 1243 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 1288 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1493 | Lattice chiral Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1538 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1580 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1603 | Modular invariance |
| `thm:lattice:niemeier-shadow-universality` | `theorem` | 1677 | Niemeier shadow universality |
| `prop:lattice:niemeier-theta-decomposition` | `proposition` | 1735 | Niemeier theta series decomposition |
| `thm:lattice:niemeier-siegel-genus2` | `theorem` | 1783 | Genus-$2$ Siegel theta series of Niemeier lattices |
| `prop:lattice:self-dual-criterion` | `proposition` | 2003 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 2020 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 2045 | Lattice twisted-sector charge inversion on the bar surface |
| `prop:lattice:deformation-properties` | `proposition` | 2229 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 2413 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 3038 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 3106 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 3180 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 3339 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3640 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3721 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3894 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 4099 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 4142 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 4300 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 4347 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 4433 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 4514 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |
| `prop:lattice:genus1-simple-pole` | `proposition` | 4703 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4720 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | 4818 | Lattice shadow obstruction tower: termination at weight~$2$ |
| `prop:xxx-shadow-data` | `proposition` | 4951 | XXX shadow data |
| `prop:transfer-matrix-shadow-dict` | `proposition` | 4990 | Transfer matrix--shadow dictionary |
| `prop:xxz-shadow-data` | `proposition` | 5039 | XXZ shadow data |
| `prop:shadow-cardy-corrections` | `proposition` | 5106 | Shadow hierarchy and Cardy corrections |

#### `chapters/examples/level1_bridge.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:level1-kappa-reduction` | `proposition` | 228 | Level-$1$ $\kappa$ reduction |
| `prop:level1-cubic-vanishing` | `proposition` | 325 | Cubic shadow vanishing at level~$1$ |
| `comp:level1-ade-bridge` | `computation` | 445 | Level-$1$ bridge data for the simply-laced series |

#### `chapters/examples/logarithmic_w_algebras.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:wp-kappa` | `proposition` | 188 | $\kappa(\cW(p))$ |
| `prop:wp-shadow-class` | `proposition` | 454 | Shadow class of $\cW(p)$ |

#### `chapters/examples/minimal_model_examples.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 432 | Fusion from bar complex on the torus |
| `prop:ising-shadow-invariants` | `proposition` | 567 | Ising shadow invariants |
| `thm:ising-shadow-growth-rate` | `theorem` | 604 | Ising shadow growth rate |
| `prop:ising-koszul-dual` | `proposition` | 665 | Koszul dual complementarity |
| `prop:ising-free-energies` | `proposition` | 705 | Ising scalar free energies |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 126 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | 260 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 408 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 432 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | 467 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 492 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 571 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 598 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 658 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 678 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 705 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 801 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

#### `chapters/examples/moonshine.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:moonshine-kappa` | `proposition` | 104 | $\kappa(V^\natural) = 12$ |

#### `chapters/examples/n2_superconformal.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:n2-kappa` | `proposition` | 208 | Modular characteristic of the $\mathcal{N}=2$ SCA;\ |
| `prop:n2-complementarity` | `proposition` | 257 | Complementarity for the $\mathcal{N}=2$ SCA;\ |
| `prop:n2-koszulness` | `proposition` | 303 | PBW Koszulness of the $\mathcal{N}=2$ SCA;\ |

#### `chapters/examples/shadow_tower_extended_families.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-s3-s4-tline` | `theorem` | 164 | $\cW_3$ closed forms: $T$-line |
| `thm:w3-w-line-s4-zamolodchikov` | `theorem` | 193 | $\cW_3$ closed forms: $W$-line with Zamolodchikov denominator |
| `thm:bp-t-line-rational-k` | `theorem` | 292 | BP closed forms: $T$-line rational in $k$ |
| `thm:bp-other-lines` | `theorem` | 354 | BP $J$-line and $G^\pm$ line |
| `cor:bp-feigin-frenkel-complementarity` | `corollary` | 386 | Feigin--Frenkel complementarity on BP $T$-line |
| `thm:w-infinity-psi-degeneration` | `theorem` | 420 | $\cW_\infty[\Psi |
| `thm:super-yangian-parity-sign` | `theorem` | 488 | Super-Yangian $\mathfrak{sl}(1\|1)$ parity sign |
| `thm:denominator-factorization-pattern` | `theorem` | 554 | Denominator factorization pattern |

#### `chapters/examples/symmetric_orbifolds.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:symn-kappa` | `proposition` | 87 | Symmetric orbifold modular characteristic |
| `prop:symn-twist-vanishing` | `proposition` | 146 | Twist-sector vanishing at genus~$1$ |
| `prop:symn-shadow-depth` | `proposition` | 242 | Shadow depth of the symmetric orbifold |
| `prop:symn-koszulness` | `proposition` | 305 | Symmetric orbifold Koszulness |
| `prop:symn-dmvv-kappa` | `proposition` | 394 | DMVV consistency with $\kappa$ |
| `prop:symn-hecke-kappa` | `proposition` | 645 | Hecke consistency with shadow scaling |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 68 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 170 | Mode expansion |
| `thm:c-scaling` | `theorem` | 221 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 311 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 476 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | 560 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 611 | Quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | 672 | Two-point function \texorpdfstring{$\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$}{:W2:_qp(z) :W2:_qp(w)} |
| `thm:w3-null-level1` | `theorem` | 732 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 835 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 906 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 948 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 1019 | Level-2 Gram matrix |

#### `chapters/examples/w3_holographic_datum.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3hol-conductor` | `theorem` | 271 | Koszul conductor and self-dual point |
| `thm:w3hol-r-channels` | `theorem` | 366 | Channel-by-channel \texorpdfstring{$r$}{r}-matrix |
| `thm:w3hol-propagator-variance` | `theorem` | 584 | Propagator variance for \texorpdfstring{$\Walg_3$}{W3} |
| `thm:w3hol-Q-T` | `theorem` | 637 | Shadow metric on the \texorpdfstring{$T$}{T}-line |
| `thm:w3hol-Q-W` | `theorem` | 650 | Shadow metric on the \texorpdfstring{$W$}{W}-line |
| `thm:w3hol-discriminants` | `theorem` | 661 | Critical discriminants and shadow class |
| `thm:w3hol-commuting-differentials` | `theorem` | 702 | Commuting differentials at \texorpdfstring{$N=3$}{N=3} |

#### `chapters/examples/w_algebras.tex` (70)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:w3-genus1-hessian` | `computation` | 269 | The $\mathcal W_3$ genus-$1$ Hessian |
| `comp:w-entropy-ladder` | `computation` | 318 | Completion entropy ladder |
| `thm:w-algebra-koszul-main` | `theorem` | 373 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `thm:w-geometric-ope` | `theorem` | 1129 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 1200 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-koszul-precise` | `theorem` | 1258 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras, precise statement |
| `thm:virasoro-self-duality` | `theorem` | 1391 | Virasoro quadratic self-duality |
| `prop:virasoro-generic-koszul-dual` | `proposition` | 1485 | Virasoro Koszul dual at generic central charge |
| `thm:vir-genus1-curvature` | `theorem` | 1641 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1693 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1757 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1927 | Critical fixed point and general-level duality for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 2007 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 2074 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 2144 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 2239 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 2351 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 2372 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-ainfty-ops` | `theorem` | 2595 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `thm:agt-shadow-correspondence` | `theorem` | 2673 | AGT shadow correspondence |
| `thm:w-universal-gravitational-cubic` | `theorem` | 3614 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | 3669 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | 3706 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | 3793 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-resonance-reorganization` | `theorem` | 3863 | Resonance reorganization |
| `cor:w-complementarity-potential-poles` | `corollary` | 4000 | Pole structure of the complementarity potential |
| `prop:virasoro-primitive-kernel` | `proposition` | 4055 | Virasoro primitive kernel |
| `prop:virasoro-primitive-shell` | `proposition` | 4107 | Virasoro primitive shell equations |
| `thm:w-w3-mixed-shadow` | `theorem` | 4264 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w3-two-dim-hessian-cubic` | `proposition` | 4328 | Two-dimensional Hessian and universal cubic |
| `thm:w3-quartic-channel-decomposition` | `theorem` | 4356 | $\mathcal{W}_3$ quartic channel decomposition |
| `prop:w3-denominator-filtration` | `proposition` | 4417 | Denominator filtration by $W$-charge |
| `thm:w3-quintic-nonvanishing` | `theorem` | 4445 | $\mathcal{W}_3$ quintic nonvanishing |
| `prop:ds-shadow-cascade` | `proposition` | 4490 | DS shadow cascade for $V_k(\mathfrak{sl}_N) \to \mathcal{W}_N$ |
| `prop:rho-decreasing-with-N` | `proposition` | 4547 | Shadow growth rate decreases with $N$ |
| `prop:w-w3-weight6-resonance` | `proposition` | 4657 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | 4728 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | 4754 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-archetype-trichotomy` | `theorem` | 4843 | Archetype trichotomy |
| `thm:w-virasoro-quintic-forced` | `theorem` | 4910 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | 4966 | Explicit quintic shadow for Virasoro |
| `thm:virasoro-shadow-generating-function` | `theorem` | 5018 | Virasoro shadow metric |
| `thm:w-finite-termination` | `theorem` | 5268 | Finite termination for primitive archetypes |
| `cor:virasoro-postnikov-nontermination` | `corollary` | 5343 | Virasoro/$\mathcal{W}_N$ shadow obstruction tower: infinite |
| `thm:w-virasoro-genus1-hessian` | `theorem` | 5381 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | 5535 | $\mathcal{W}_3$ quintic obstruction |
| `prop:w3-wline-ring-relations` | `proposition` | 5730 | $W$-line ring relations |
| `thm:w-finite-degree-polynomial-pva` | `theorem` | 6023 | Finite-degree theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | 6061 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | 6103 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | 6130 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | 6206 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | 6231 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | 6265 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | 6303 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | 6323 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `prop:miura-degree-sharp` | `proposition` | 6407 | Miura degree bound is sharp |
| `thm:w-pbw-slodowy-collapse` | `theorem` | 6556 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | 6617 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-degree-detection` | `theorem` | 6725 | Canonical degree detection |
| `thm:w-bp-strict` | `theorem` | 6751 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | 6801 | $\mathcal{W}_4^{(2)}$ has canonical degree~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | 6860 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | 6919 | Subregular Appell formula |
| `thm:w-unbounded-canonical-degree` | `theorem` | 6957 | Unbounded canonical degree |
| `cor:w-subregular-degree-staircase` | `corollary` | 6986 | The subregular degree staircase |
| `thm:w-subregular-classification` | `theorem` | 7028 | Subregular classification |
| `prop:sl3-nilpotent-shadow-data` | `proposition` | 7112 | $\mathfrak{sl}_3$ nilpotent orbits: shadow data |
| `prop:sl4-hook-shadow-data` | `proposition` | 7166 | $\mathfrak{sl}_4$ hook-type shadow data |
| `thm:ds-shadow-functor-degree2` | `theorem` | 7207 | DS shadow functor at degree~$2$ |

#### `chapters/examples/w_algebras_deep.tex` (37)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 188 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 1185 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `thm:master-commutative-square` | `theorem` | 1471 | Master commutative square for DS reduction |
| `prop:w3-deg3-vacuum` | `proposition` | 1878 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-bar-formality` | `proposition` | 2237 | DS--bar commutation via filtration formality |
| `thm:transport-closure-type-a` | `theorem` | 2307 | Transport-closure in type $A$ |
| `prop:partition-dependent-complementarity` | `proposition` | 2361 | Kappa deficit and Koszul complementarity for non-principal DS |
| `thm:ds-platonic-functor` | `theorem` | 2543 | BRST reduction on total modular Koszul datums |
| `cor:ds-theta-descent` | `corollary` | 2770 | BRST descent of the universal MC element |
| `comp:wn-stabilization-windows` | `computation` | 3215 | Coefficient stabilization windows for $\mathcal{W}_N$ |
| `prop:abelian-locus-type-a` | `proposition` | 3285 | Abelian locus in type~$A$ |
| `prop:abelianity-complementarity-independence` | `proposition` | 3327 | Independence of abelianity and complementarity |
| `prop:bfn-slodowy-dimensions` | `proposition` | 3408 | BFN--Slodowy dimension matching |
| `prop:ghost-constant-monotonicity` | `proposition` | 3481 | Ghost constant monotonicity |
| `thm:winfty-scalar` | `theorem` | 3702 | One-dimensional cyclic line for $\mathcal{W}_\infty$ |
| `prop:gram-wt4` | `proposition` | 3857 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | 3922 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | 3965 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:higher-w-kappa-matrix` | `proposition` | 4092 | Kappa matrix for $\Walg_N$ |
| `prop:higher-w-gravitational-cubic` | `proposition` | 4155 | Gravitational cubic for $\Walg_N$ |
| `prop:higher-w-parity` | `proposition` | 4198 | $\mathbb{Z}_2$ parity and the cubic shadow |
| `prop:weight-4-exchange-upgrade` | `proposition` | 4255 | Weight-$4$ exchange spectrum upgrade at rank~$3$ |
| `prop:virasoro-primitive` | `proposition` | 4546 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | 4607 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | 4648 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | 4751 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | 4784 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | 4805 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | 4837 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | 4944 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | 4980 | $\Walg_\infty$ bar-window series and Koszul entropy |
| `thm:y-algebra-koszulness` | `theorem` | 5066 | Chiral Koszulness of $Y$-algebras |
| `thm:n2-kappa` | `theorem` | 5226 | $N=2$ modular characteristic |
| `prop:n2-koszul-duality` | `proposition` | 5282 | $N=2$ Koszul duality |
| `prop:n2-channel-decomposition` | `proposition` | 5353 | $N=2$ channel decomposition |
| `prop:n2-bosonic-shadow-metric` | `proposition` | 5386 | $N=2$ bosonic shadow metric |
| `prop:n2-minimal-models` | `proposition` | 5431 | $N=2$ minimal model shadow data |

#### `chapters/examples/y_algebras.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:y-central-charge` | `theorem` | 208 | {Central charge of $Y_{N_1,N_2,N_3}[\Psi |
| `comp:y-special-cases-c` | `computation` | 236 | Special cases of the central charge |
| `thm:y111-central-charge` | `theorem` | 274 | $c(Y_{1,1,1}) = 0$ |
| `thm:y111-kappa-channels` | `theorem` | 326 | {Channel-by-channel $\kappa$ for $Y_{1,1,1}[\Psi |
| `thm:y-kappa-general` | `theorem` | 382 | {General $\kappa$ for $Y_{N_1,N_2,N_3}[\Psi |
| `prop:y-koszul-dual` | `proposition` | 433 | {Koszul dual of $Y_{N_1,N_2,N_3}[\Psi |
| `prop:y-complementarity` | `proposition` | 462 | {Complementarity for $Y_{1,1,1}[\Psi |
| `thm:y-shadow-depth` | `theorem` | 499 | Shadow depth of $Y$-algebras |
| `comp:y111-collision-residue` | `computation` | 583 | {Collision residue for $Y_{1,1,1}[\Psi |
| `thm:y-koszulness` | `theorem` | 657 | {Chiral Koszulness of $Y_{N_1,N_2,N_3}[\Psi |
| `comp:y-wn-specialization` | `computation` | 691 | $Y_{0,0,N} \simeq \cW_N \times \mathfrak{gl}(1)$ |
| `comp:y-affine-specialization` | `computation` | 713 | $Y_{N,0,0} \simeq \widehat{\mathfrak{gl}}(N)$ |
| `prop:y111-genus1` | `proposition` | 732 | {Genus-$1$ free energy of $Y_{1,1,1}[\Psi |
| `prop:y111-genus-tower` | `proposition` | 751 | {Higher-genus tower of $Y_{1,1,1}[\Psi |

#### `chapters/examples/yangians_computations.tex` (59)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:yangian-rank-dependence` | `proposition` | 524 | Rank dependence of Yangian bar complex |
| `comp:sl3-yangian-from-ordered-bar` | `computation` | 561 | The \texorpdfstring{$\mathfrak{sl}_3$}{sl3} Yangian $R$-matrix from the ordered bar |
| `prop:rmatrix-from-bar` | `proposition` | 724 | Classical and quantum $R$-matrices from the bar complex |
| `thm:quantum-rmatrix-shadow` | `theorem` | 838 | Quantum $R$-matrix from the shadow obstruction tower |
| `prop:colored-rmatrix` | `proposition` | 899 | Colored $R$-matrices and Casimir eigenvalues |
| `thm:bethe-from-mc` | `theorem` | 943 | Bethe ansatz from the MC equation |
| `thm:bae-from-mc` | `theorem` | 1046 | Bethe ansatz equations from the shadow potential |
| `prop:eval-module-bar` | `proposition` | 1183 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 1273 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 1323 | Bar-comodule Ext comparison for Yangian evaluation modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 1380 | DK-2 reduction to thick generation, conditional on an ambient exact extension |
| `prop:dk2-thick-generation-typeA` | `proposition` | 1445 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `cor:dk2-thick-generation-all-types` | `corollary` | 1540 | Thick generation for all simple types |
| `lem:composition-thick-generation` | `lemma` | 1565 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 1596 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `prop:mc3-asymptotic-prefundamentals` | `proposition` | 1632 | Asymptotic prefundamentals thick-generate without Baxter |
| `prop:mc3-reflection-equation` | `proposition` | 1665 | Reflection-equation singular vectors for twisted Yangians |
| `thm:mc3-universal-multiplicity-free` | `theorem` | 1694 | Universal multiplicity-freeness of $\ell$-weight spectra |
| `prop:mc3-elliptic-theta-divisor` | `proposition` | 1720 | Elliptic thick generation on the theta-divisor complement |
| `prop:mc3-super-parity-balance` | `proposition` | 1750 | Super-Yangian parity-balanced Baxter |
| `lem:monoidal-thick-extension` | `lemma` | 1912 | Monoidal extension to thick closures |
| `lem:fd-thick-closure` | `lemma` | 2102 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 2188 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 2439 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 2570 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 2728 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 2748 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 2773 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 2947 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:baxter-exact-triangles-opoly` | `theorem` | 3015 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `thm:baxter-exact-triangles` | `theorem` | 3057 | Baxter exact triangles on shifted envelope \texorpdfstring{$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$}{Osh} |
| `prop:baxter-yangian-equivariance` | `proposition` | 3128 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | 3202 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `thm:shifted-prefundamental-generation` | `theorem` | 3250 | Shifted-prefundamental generation on the shifted envelope |
| `prop:prefundamental-clebsch-gordan` | `proposition` | 3681 | Universal prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | 3721 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | 3734 | $K_0$ generation for all simple types |
| `prop:categorical-cg-typeA` | `proposition` | 3783 | Categorical prefundamental CG decomposition, type~$A$ |
| `thm:pro-weyl-recovery` | `theorem` | 3880 | Pro-Weyl recovery of ordinary standards in type~$A$ |
| `thm:mc3-type-a-resolution` | `theorem` | 4197 | Type-$A$ MC3 reduction to the compact-completion packet |
| `thm:mc3-arbitrary-type` | `theorem` | 4287 | Categorical prefundamental CG decomposition, all types |
| `cor:mc3-all-types` | `corollary` | 4434 | Three-layer MC3 status after categorical CG closure |
| `prop:completion-extension-weight-bounded` | `proposition` | 4486 | MC3 completion extension via weight-bounded t-structure |
| `prop:e8-root-uniformity` | `proposition` | 4796 | $E_8$ relevant-root uniformity |
| `prop:character-cg-all-types` | `proposition` | 4806 | Character-level Clebsch--Gordan for all simple types |
| `prop:mc3-asymptotic-prefundamentals` | `proposition` | 4842 | Asymptotic prefundamentals replace the Baxter locus for $Y_\hbar(\mathfrak{sl}_N)$ |
| `prop:mc3-reflection-equation` | `proposition` | 4881 | Reflection-equation singular vectors for non-type-$A$ |
| `thm:mc3-universal-multiplicity-free` | `theorem` | 4920 | Universal thick generation via multiplicity-free $\ell$-weights |
| `prop:mc3-elliptic-theta-divisor` | `proposition` | 4954 | Elliptic Yangian $E_{\rho,\eta}(\mathfrak{sl}_N)$: theta-divisor failure locus |
| `prop:mc3-super-parity-balance` | `proposition` | 4988 | Super-Yangian $Y_\hbar(\mathfrak{gl}_{m\|n})$: parity-balance constraint |
| `thm:yangian-vector-seed-propagation` | `theorem` | 5398 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | 5428 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | 5451 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | 5466 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | 5517 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | 5542 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | 5569 | Derived realization of the Baxter--Rees family |
| `thm:yangian-H2-reduction` | `theorem` | 5636 | $H^2$-reduction to the three-leg sector |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | 5713 | Concrete cocycle |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (97)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-dk-affine` | `theorem` | 162 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `comp:dk0-four-path` | `computation` | 264 | Four-path Drinfeld--Kohno verification |
| `thm:derived-dk-yangian` | `theorem` | 283 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 459 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 560 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 692 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 741 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 878 | Evaluation-generated-core DK comparison for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 1078 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 1119 | Canonical associative dg model of the Yangian formal-moduli target |
| `prop:dk5-sl2-frt` | `proposition` | 1309 | DK-5 for $\mathfrak{sl}_2$ via FRT reconstruction |
| `thm:factorization-positselski` | `theorem` | 1523 | Factorization Positselski equivalence on the bar-coalgebra surface |
| `thm:ind-completed-extension` | `theorem` | 1659 | Ind-completion of the generated-core DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 1859 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 1966 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 2064 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 2279 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 2359 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `thm:bridge-criterion` | `theorem` | 2539 | Bridge Criterion Theorem |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 2791 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 2911 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 2970 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 3053 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 3134 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 3165 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 3202 | Compact-core DK-5 functors from realization of a finite-dimensional factorization DK pair |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 3270 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 3300 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 3332 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 3391 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 3470 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 3499 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 3566 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 3598 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 3636 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 3651 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 3701 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 3758 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 3805 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 3896 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 3996 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 4036 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 4072 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `thm:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 4099 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 4240 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 4278 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 4328 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 4366 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 4393 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 4432 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 4470 | DK-5 closes once the compact cores realize a finite-dimensional factorization DK pair |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 4495 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 4693 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 4756 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 4791 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 4845 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 4878 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 4944 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 5023 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts-orig` | `corollary` | 5177 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet-orig` | `corollary` | 5206 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization-orig` | `corollary` | 5239 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of a chosen finite-dimensional factorization DK pair |
| `cor:yangian-formal-moduli-plus-core-realization-orig` | `corollary` | 5269 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize a chosen finite-dimensional DK pair |
| `cor:yangian-typea-realization-plus-dg-packet-orig` | `corollary` | 5319 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 5427 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 5530 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 5591 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 5641 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 5700 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed-orig` | `corollary` | 5743 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line-orig` | `corollary` | 5776 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |
| `prop:ds-functor-primitive-triple` | `proposition` | 6364 | DS reduction on primitive triples |
| `prop:free-propagator-matching` | `proposition` | 6795 | Free/Heisenberg propagator matching |
| `prop:affine-propagator-matching` | `proposition` | 6840 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `prop:rmatrix-pole-landscape` | `proposition` | 6917 | The collision-residue $r$-matrix across the standard landscape |
| `prop:bosonic-parity-constraint` | `proposition` | 7019 | Bosonic parity constraint on $r$-matrix poles |
| `prop:cybe-from-mc` | `proposition` | 7062 | CYBE from bar-complex MC equation |
| `prop:rmatrix-from-bar-coproduct` | `proposition` | 7165 | Quantum $R$-matrix from the bar coproduct |
| `prop:elliptic-rmatrix-shadow` | `proposition` | 7253 | Elliptic $R$-matrix from the genus-$1$ shadow |
| `thm:bae-from-mc-stationarity` | `theorem` | 7394 | Bethe ansatz equations from the MC stationarity |
| `prop:kz-from-shadow` | `proposition` | 7501 | KZ equation from the shadow connection |
| `prop:verlinde-from-shadow` | `proposition` | 7606 | Verlinde formula from the shadow complex |
| `thm:rmatrix-koszul-inverse` | `theorem` | 7932 | Collision residue as binary Koszul inverse |
| `thm:r-matrix-koszul-dual-inverse` | `theorem` | 8059 | The $r$-matrix as Koszul-dual inverse |
| `thm:spectral-derived-additive-kz` | `theorem` | 8271 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | 8369 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | 8415 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | 8488 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | 8571 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | 8627 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | 8669 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | 8704 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | 8758 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | 8829 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | 8853 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | 8892 | Exact free transport |
| `thm:spectral-conditional-strictification` | `theorem` | 8925 | Conditional strictification criterion |

#### `chapters/examples/yangians_foundations.tex` (47)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:rtt-all-classical-types` | `theorem` | 360 | RTT R-matrices for all classical types |
| `thm:yangian-e1` | `theorem` | 514 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 620 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 653 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 712 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 774 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 829 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 893 | Koszul duality on Yangian modules |
| `thm:all-types-yangian-structure` | `theorem` | 1195 | All-types Yangian structure |
| `prop:dg-shifted-comparison` | `proposition` | 1441 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1568 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `prop:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1612 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1723 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1827 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1845 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1875 | Explicit coefficient formula for the fundamental monodromy series |
| `prop:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1937 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 2001 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 2087 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 2184 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 2254 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 2323 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 2360 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2416 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2476 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2537 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2636 | Standard type-A fundamental line operator has the standard local residue |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | 3062 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | 3089 | Stabilized completed bar/cobar recovery |
| `cor:shifted-rtt-tower-convergence` | `corollary` | 3120 | Automatic tower convergence |
| `thm:shifted-rtt-mc-descent` | `theorem` | 3150 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | 3238 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | 3283 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | 3331 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | 3347 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | 3377 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | 3410 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | 3444 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | 3469 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | 3541 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | 3590 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | 3616 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | 3643 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | 3665 | Kleinian associated graded at the nilpotent point |
| `prop:elliptic-coproduct-coassoc-fay` | `proposition` | 3836 | Elliptic coproduct is Fay-coassociative |
| `thm:felder-R-half-braiding` | `theorem` | 3863 | Felder $R$-matrix as half-braiding |
| `prop:sl2-elliptic-yangian-triangle` | `proposition` | 3882 | $\slnn{2}$ elliptic triangle coherence at order $\hbar$ |

### Part III: Connections (334)

#### `chapters/connections/arithmetic_shadows.tex` (122)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:divisor-sum-decomposition` | `proposition` | 311 | Divisor-sum decomposition |
| `prop:sewing-trace-formula` | `proposition` | 349 | Sewing trace formula |
| `thm:sewing-selberg-formula` | `theorem` | 387 | Sewing--Selberg formula |
| `thm:narain-universality` | `theorem` | 444 | Narain universality |
| `thm:e8-epstein` | `theorem` | 475 | $E_8$ Epstein factorization |
| `prop:z2-epstein` | `proposition` | 500 | $\bZ^2$ Epstein zeta |
| `prop:leech-epstein` | `proposition` | 523 | Leech Epstein factorization |
| `prop:niemeier-multichannel` | `proposition` | 691 | Multi-channel Niemeier discrimination |
| `prop:shadow-arithmetic-factorization` | `proposition` | 779 | Shadow--arithmetic factorization |
| `prop:hecke-all-orders` | `proposition` | 1022 | Exactness of the Hecke identification |
| `prop:period-shadow-dictionary` | `proposition` | 1073 | Period--shadow dictionary |
| `comp:period-shadow-vz` | `computation` | 1156 | $V_{\bZ}$: the Gaussian archetype |
| `comp:period-shadow-ve8` | `computation` | 1174 | $V_{E_8}$: the Lie/tree archetype |
| `comp:period-shadow-leech` | `computation` | 1196 | $V_{\mathrm{Leech}}$: the Ramanujan archetype |
| `comp:period-shadow-rank24-comparison` | `computation` | 1248 | $D_{16}^+ \oplus D_{16}^+$ vs.\ $E_8^3$: same depth, different coefficient |
| `comp:period-shadow-rank2` | `computation` | 1267 | $V_{\bZ^2}$ and $V_{A_2}$: Dedekind zeta at depth~$2$ |
| `thm:spectral-decomposition-principle` | `theorem` | 1291 | Spectral decomposition principle |
| `prop:growth-rate-dictionary` | `proposition` | 1378 | Growth-rate dictionary |
| `prop:self-referentiality-criterion` | `proposition` | 1422 | Self-referentiality criterion |
| `cor:conformal-vector-infinite-depth` | `corollary` | 1492 | Conformal vector implies infinite shadow depth |
| `thm:shadow-tower-asymptotics` | `theorem` | 1515 | Shadow obstruction tower leading asymptotics |
| `cor:rigorous-infinite-depth` | `corollary` | 1547 | Rigorous infinite shadow depth |
| `prop:ising-d-arith` | `proposition` | 1624 | Ising model: $d_{\mathrm{arith}} = 0$ |
| `rem:ising-arithmetic-paradox` | `remark` | 1652 | The Ising arithmetic paradox |
| `rem:non-unimodular` | `remark` | 1720 | Non-unimodular lattices |
| `thm:depth-decomposition` | `theorem` | 1789 | Depth decomposition |
| `rem:depth-decomposition-universality` | `remark` | 1881 | Universality and the complete $d_{\mathrm{alg}}$ table |
| `rem:vnatural-class-m` | `remark` | 1939 | The moonshine module: same $\kappa$, different class |
| `thm:ainfty-formality-depth` | `theorem` | 1973 | $A_\infty$ formality criterion |
| `thm:interacting-gram-positivity` | `theorem` | 2031 | Interacting Gram positivity |
| `cor:virasoro-interacting-gram` | `corollary` | 2071 | — |
| `thm:shadow-resonance-locus` | `theorem` | 2084 | — |
| `thm:shadow-spectral-measure` | `theorem` | 2122 | Shadow spectral measure |
| `prop:carleman-virasoro` | `proposition` | 2214 | Carleman rigidity |
| `prop:shadow-periods` | `proposition` | 2251 | Shadow amplitudes are periods |
| `prop:resurgent-orthogonality` | `proposition` | 2493 | Two orthogonal resurgent directions |
| `prop:universal-stokes-constants` | `proposition` | 2535 | Universal Stokes constants |
| `prop:gevrey-zero-degree` | `proposition` | 2567 | Gevrey-$0$ degree growth |
| `prop:padic-convergence` | `proposition` | 2625 | $p$-adic convergence radius |
| `rem:kummer-kubota-leopoldt` | `remark` | 2651 | Kummer congruences and the Kubota--Leopoldt $p$-adic $L$-function |
| `thm:shadow-mzv-dictionary` | `theorem` | 2756 | Shadow--MZV dictionary |
| `thm:drinfeld-associator-bar-transport` | `theorem` | 2836 | Drinfeld associator as bar transport |
| `thm:partition-modular-classification` | `theorem` | 3021 | Partition function modular classification |
| `prop:quasi-modular-propagator` | `proposition` | 3081 | Quasi-modular content from the genus-$1$ propagator |
| `prop:hecke-eigenvalue-extraction` | `proposition` | 3155 | Hecke eigenvalues from partition data |
| `thm:spectral-curve` | `theorem` | 3202 | Algebraic shadow generating function |
| `prop:moment-matrix-negativity` | `proposition` | 3245 | Eisenstein moment minor |
| `prop:calogero-shadow-dictionary` | `proposition` | 3301 | Calogero--Moser / shadow tower dictionary |
| `rem:shadow-eisenstein-numerical-check` | `remark` | 3634 | Numerical check at $s = 0$ |
| `thm:shadow-higgs-field` | `theorem` | 3923 | Shadow Higgs field |
| `thm:general-nahc` | `theorem` | 4004 | General shadow triple |
| `rem:ode-im-shadow-identification` | `remark` | 4277 | ODE/IM correspondence as shadow projection |
| `prop:shadow-oper-rigid` | `proposition` | 4383 | Shadow oper as rigid hypergeometric |
| `prop:shadow-langlands-hierarchy` | `proposition` | 4470 | The $\cW_3$ shadow oper beyond Eisenstein |
| `thm:shadow-bps` | `theorem` | 4639 | The shadow obstruction tower as BPS spectrum |
| `thm:general-bps` | `theorem` | 4723 | General BPS spectrum of the shadow obstruction tower |
| `thm:sewing-shadow-intertwining` | `theorem` | 4823 | Sewing--shadow intertwining at genus~$1$ |
| `cor:spectral-measure-identification` | `corollary` | 4935 | Spectral measure identification |
| `thm:shadow-moduli-resolution` | `theorem` | 4989 | Shadow-moduli resolution |
| `thm:universality-of-G` | `theorem` | 5078 | Universality of $G$ |
| `prop:mc-bracket-determines-atoms` | `proposition` | 5146 | MC bracket determines spectral atoms |
| `rem:mc-ramanujan-bridge` | `remark` | 5196 | The bridge to the Ramanujan bound |
| `prop:koszul-field-criterion` | `proposition` | 5445 | Koszul field-preservation criterion |
| `prop:two-fixed-points` | `proposition` | 5520 | The two fixed points are unrelated |
| `prop:heisenberg-koszul-epstein` | `proposition` | 5686 | Degenerate case: Heisenberg |
| `comp:virasoro-c1-koszul-epstein` | `computation` | 5738 | Virasoro at $c = 1$: numerical Koszul--Epstein value |
| `comp:fe-minimal-models` | `computation` | 5763 | Functional equation for all unitary minimal models |
| `thm:spectral-continuation-bridge` | `theorem` | 5843 | Hecke-equivariant MC element |
| `thm:schur-complement-quartic` | `theorem` | 5982 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | 6041 | — |
| `prop:on-off-line-distinction` | `proposition` | 6118 | — |
| `prop:li-criterion-failure` | `proposition` | 6528 | Structural failure of the Li criterion for the sewing lift |
| `prop:pure-spin-s-schur` | `proposition` | 6678 | — |
| `prop:prime-side-defect-formula` | `proposition` | 6786 | — |
| `thm:finite-miura-defect` | `theorem` | 6856 | Finite Miura defect at genus one |
| `prop:modularity-constraint` | `proposition` | 7428 | Modularity constraint on the spectral measure |
| `prop:bracket-hodge-index` | `proposition` | 7471 | Bracket positivity and the Hodge index |
| `prop:lattice-ramanujan` | `proposition` | 7595 | Ramanujan bound for lattice spectral measures |
| `prop:shadow-symmetric-power` | `proposition` | 7637 | Shadow--symmetric power identification |
| `thm:petersson-identification` | `theorem` | 7781 | Petersson identification |
| `prop:modularity-constraint-atoms` | `proposition` | 7867 | Modularity constraint on atoms |
| `prop:rigidity-threshold` | `proposition` | 7904 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | 8002 | Lattice Ramanujan from rigidity |
| `prop:stieltjes-signed-universal` | `proposition` | 8198 | Universal signed Stieltjes measure |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | 8231 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | 8295 | Shadow arithmetic trichotomy |
| `prop:genus1-weight-bound` | `proposition` | 8370 | Weight bound for genus-$1$ shadow projections |
| `thm:mc-recursion-moment` | `theorem` | 8503 | MC recursion on moment $L$-functions |
| `prop:shadow-chiral-graph` | `proposition` | 8570 | Shadow amplitudes as chiral graph integrals |
| `thm:hecke-newton-lattice` | `theorem` | 8643 | Hecke--Newton closure for lattice VOAs |
| `thm:non-lattice-ramanujan` | `theorem` | 8735 | Non-lattice Ramanujan bound |
| `prop:mc-constraint-counting` | `proposition` | 9252 | MC constraint counting |
| `thm:route-c-propagation` | `theorem` | 9317 | Route~C: MC rigidity forces character-level prime-locality |
| `cor:route-c-standard-landscape` | `corollary` | 9440 | Route~C for the standard landscape |
| `thm:hecke-verdier-commutation` | `theorem` | 9479 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | 9518 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | 9593 | Theta decomposition bridge |
| `prop:newton-shadow-hecke` | `proposition` | 9656 | Newton--shadow--Hecke correspondence |
| `prop:sewing-spectral-bridge` | `proposition` | 9774 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | 9879 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | 9926 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | 10017 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | 10191 | Genus-one saddle triviality |
| `thm:scattering-coupling-factorization` | `theorem` | 10492 | Scattering coupling factorization |
| `thm:structural-separation` | `theorem` | 10575 | Structural separation of algebraic and arithmetic content |
| `prop:hecke-defect-equivalences` | `proposition` | 10701 | Equivalent characterizations; \textup{(i)--(iii)} ; \textup{(iv)} |
| `prop:hecke-defect-lattice` | `proposition` | 10752 | Hecke defect vanishes for lattice VOAs |
| `prop:hecke-defect-families` | `proposition` | 10827 | Hecke defect for standard families |
| `thm:rigidity-inheritance` | `theorem` | 10947 | Rigidity inheritance |
| `thm:packet-connection-flatness` | `theorem` | 11248 | Flatness and divisor independence |
| `prop:gauge-criterion-scattering` | `proposition` | 11381 | Gauge criterion for scattering access |
| `rem:arithmetic-comparison-sharpening` | `remark` | 11491 | Sharpening of the arithmetic comparison conjecture |
| `prop:miura-packet-splitting` | `proposition` | 11565 | — |
| `prop:genus2-non-diagonal` | `proposition` | 11931 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | 11975 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | 12107 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | 12139 | B\"ocherer bridge |
| `rem:genus2-definitive-scope` | `remark` | 12264 | Definitive scope of genus-$2$ arithmetic access |
| `rem:leech-all-sk` | `remark` | 12319 | Leech: all genus-$2$ cusp forms are Saito--Kurokawa lifts |
| `thm:leech-chi12-projection` | `theorem` | 12340 | Leech $\chi_{12}$-projection and Waldspurger consequence |
| `thm:prime-locality-obstructions` | `theorem` | 12597 | Precise obstructions to prime-locality; {} where indicated |
| `prop:shadow-not-selberg` | `proposition` | 12841 | The shadow zeta is not in the Selberg class |

#### `chapters/connections/bv_brst.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:log-form-ghost-law` | `theorem` | 481 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 586 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 737 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `prop:koszul-brst-anomaly-preservation` | `proposition` | 779 | Koszul duality preserves BRST anomaly cancellation |
| `comp:v1-superstring-ghost-koszul` | `computation` | 862 | Superstring ghost/superghost Koszul dual |
| `thm:bar-semi-infinite-km` | `theorem` | 1014 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 1127 | Anomaly duality for Kac--Moody pairs |
| `cor:anomaly-duality-w` | `corollary` | 1290 | Curvature complementarity for principal \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |
| `thm:heisenberg-bv-bar-all-genera` | `theorem` | 1508 | BV $=$ bar for the Heisenberg at all genera |
| `prop:chain-level-three-obstructions` | `proposition` | 1755 | Three chain-level obstructions and harmonic factorization |
| `rem:bv-sewing-chain-level-classes` | `remark` | 1966 | BV sewing at the chain level: class-by-class status |
| `prop:harmonic-factorization` | `proposition` | 2016 | Harmonic factorization of higher bar differentials |
| `thm:bv-bar-coderived` | `theorem` | 2198 | BV$=$bar in the coderived category |
| `prop:wzw-brst-bar-genus0` | `proposition` | 2692 | Genus-\texorpdfstring{$0$}{0} WZW BRST complex from the affine bar complex |

#### `chapters/connections/concordance.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 572 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 586 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | 877 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 901 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 938 | Gaussian collapse for abelian input |
| `thm:operadic-complexity-concordance` | `theorem` | 2626 | Operadic complexity |
| `thm:universal-MC` | `theorem` | 5409 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 5764 | Discriminant as spectral determinant, verified cases |
| `thm:discriminant-spectral` | `theorem` | 5809 | Spectral discriminant, general case |
| `comp:spectral-discriminants-standard` | `computation` | 6035 | Spectral discriminants of standard families |
| `thm:family-index` | `theorem` | 6100 | Family index theorem for genus expansions |
| `rem:c13-concordance-holographic` | `remark` | 6741 | The self-dual central charge $c = 13$ |
| `rem:programme-vi-verification` | `remark` | 7646 | Programme VI: systematic verification of (H1)--(H4) |
| `rem:four-test-interface` | `remark` | 7875 | The four-test interface |
| `prop:descent-fan` | `proposition` | 9991 | Descent fan structure |

#### `chapters/connections/editorial_constitution.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:en-n2-recovery` | `proposition` | 1673 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1819 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1877 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1911 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1927 | Physical anomaly cancellation for affine Kac--Moody algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2164 | Hodge symmetry from complementarity |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 2484 | Volume~I concrete modular datum |

#### `chapters/connections/entanglement_modular_koszul.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ent-scalar-entropy` | `theorem` | 160 | Entanglement entropy at the scalar level |
| `thm:entanglement-complementarity` | `theorem` | 235 | Entanglement complementarity |
| `prop:ent-complexity-classification` | `proposition` | 354 | Entanglement complexity classification |
| `thm:ent-landscape-census` | `theorem` | 569 | Standard landscape entanglement census |
| `thm:ent-btz-entropy` | `theorem` | 712 | BTZ entropy from the modular characteristic |
| `prop:ent-btz-complementarity` | `proposition` | 840 | BTZ complementarity |

#### `chapters/connections/feynman_diagrams.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 193 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 298 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 343 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 370 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 410 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 428 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 449 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 496 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 555 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 912 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 944 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (53)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | 139 | Protected dual transform and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | 237 | Protected transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | 290 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | 331 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | 385 | Scalar fixed-point rigidity on a full scalar package and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | 499 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | 612 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | 730 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | 801 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | 933 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | 1013 | The first nonlinear holographic anomaly |
| `thm:yangian-shadow-theorem` | `theorem` | 1422 | Yangian-shadow theorem |
| `thm:sphere-reconstruction` | `theorem` | 1479 | Sphere flatness and reconstruction on established comparison surfaces |
| `thm:gz26-commuting-differentials` | `theorem` | 1547 | GZ26 commuting differentials from the MC element |
| `thm:gaudin-yangian-identification` | `theorem` | 1653 | Gaudin--Yangian identification |
| `thm:yangian-sklyanin-quantization` | `theorem` | 1695 | Three-parameter identification of $\hbar$; {} on the new three-parameter identification; classical Sklyanin/Drinfeld content is |
| `thm:shadow-depth-operator-order` | `theorem` | 1750 | OPE pole order trichotomy for GZ\textup{26} Hamiltonians |
| `thm:kz-classical-quantum-bridge` | `theorem` | 1804 | Classical-to-quantum bridge: proved algebraic content |
| `thm:quartic-resonance-obstruction` | `theorem` | 1847 | Quartic resonance obstruction |
| `thm:collision-residue-twisting` | `theorem` | 2270 | Collision residue = universal twisting morphism |
| `thm:collision-depth-2-ybe` | `theorem` | 2326 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `thm:shadow-connection-kz` | `theorem` | 2364 | Shadow/KZ comparison on the affine Kac--Moody surface |
| `prop:shadow-connection-bpz` | `proposition` | 2429 | Shadow connection for Virasoro and BPZ on the degenerate-representation surface |
| `thm:quartic-obstruction-linf` | `theorem` | 2465 | Quartic obstruction = $L_\infty$ obstruction |
| `comp:holographic-ss-sl2` | `computation` | 2548 | The $E_1$ page for $\widehat{\mathfrak{sl}}_2$ |
| `comp:holographic-ss-vir` | `computation` | 2600 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | 2644 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | 2667 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | 2749 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | 2772 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | 2812 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | 2903 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | 2962 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | 3058 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | 3092 | Holographic datum for $\mathcal W_3$ |
| `thm:ds-central-charge-additivity` | `theorem` | 3216 | Central charge additivity under DS |
| `cor:critical-dimensions` | `corollary` | 3327 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | 3438 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | 3462 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | 3498 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | 3523 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | 3635 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | 3770 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | 3945 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | 4069 | Lifts as relative MC elements |
| `prop:frontier-celestial-ope` | `proposition` | 4482 | Celestial OPE from the bar complex |
| `prop:frontier-sw-shadow` | `proposition` | 4556 | Shadow connection and Picard--Fuchs |
| `prop:frontier-cs-shadow` | `proposition` | 4623 | Chern--Simons from the shadow obstruction tower |
| `thm:frontier-twisted-holography` | `theorem` | 4733 | Twisted holography datum |
| `thm:frontier-abjm` | `theorem` | 4823 | ABJM holographic datum |
| `thm:frontier-m5` | `theorem` | 4961 | M5 brane holographic datum |
| `prop:phantom-m5-koszul-dual` | `proposition` | 5093 | Phantom M5 Koszul dual |
| `comp:burns-space-holographic-datum` | `computation` | 5229 | Burns space holographic modular Koszul datum |

#### `chapters/connections/genus1_seven_faces.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:g1sf-elliptic-regularization` | `theorem` | 161 | Elliptic regularization of the collision residue |
| `thm:g1sf-face-1` | `theorem` | 253 | Face~1 at genus~$1$: elliptic twisting morphism |
| `thm:g1sf-face-4` | `theorem` | 330 | Face~4 at genus~$1$: KZB connection |
| `thm:g1sf-face-5` | `theorem` | 464 | Face~5 at genus~$1$: elliptic $r$-matrix; {} \textup{(}identification with collision residue\textup{)}; {} \textup{(}classical elliptic $r$-matrix: Belavin 1981, Belavin--Drinfeld 1982\textup{)} |
| `thm:g1sf-face-7` | `theorem` | 583 | Face~7 at genus~$1$: elliptic Gaudin Hamiltonians |
| `thm:g1sf-virasoro` | `theorem` | 691 | Virasoro genus-$1$ collision residue |
| `thm:g1sf-wn` | `theorem` | 758 | $\cW_N$ genus-$1$ collision residue |
| `thm:g1sf-master` | `theorem` | 836 | Genus-$1$ seven-face identification for affine Kac--Moody |
| `thm:g1sf-degeneration` | `theorem` | 954 | Degeneration to genus~$0$ |
| `thm:g1sf-b-cycle-monodromy` | `theorem` | 1101 | $B$-cycle monodromy of the collision residue |

#### `chapters/connections/genus_complete.tex` (28)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 235 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 290 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 373 | Koszul dual modular functors |
| `__unlabeled_chapters/connections/genus_complete.tex:507` | `remark` | 507 | Evidence |
| `thm:bar-moduli-integrals` | `theorem` | 657 | Bar complex computes moduli integrals |
| `thm:full-modular-invariant-hierarchy` | `theorem` | 1216 | The full modular invariant hierarchy |
| `prop:sewing-universal-property` | `proposition` | 1336 | Universal property of the sewing envelope |
| `prop:hs-trace-class` | `proposition` | 1375 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | 1390 | General HS-sewing criterion |
| `cor:hs-implies-gram` | `corollary` | 1460 | — |
| `thm:heisenberg-one-particle-sewing` | `theorem` | 1479 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | 1556 | Positive grading implies conilpotency |
| `thm:dirichlet-weight-formula` | `theorem` | 1858 | — |
| `cor:virasoro-mode-removal` | `corollary` | 1915 | — |
| `thm:euler-koszul-criterion` | `theorem` | 1974 | — |
| `comp:euler-koszul-defect-table` | `computation` | 2011 | Euler--Koszul defect table for the standard landscape |
| `prop:zeta-zeros-defect-derivative` | `proposition` | 2103 | — |
| `thm:li-closed-form` | `theorem` | 2140 | — |
| `thm:li-asymptotics` | `theorem` | 2173 | — |
| `thm:surface-moment-positivity` | `theorem` | 2299 | Gram positivity |
| `cor:virasoro-gram-ratio` | `corollary` | 2322 | — |
| `thm:sewing-rkhs` | `theorem` | 2357 | Sewing RKHS |
| `prop:collapse-permanence` | `proposition` | 2424 | Collapse permanence |
| `prop:benjamin-chang-bridge` | `proposition` | 2463 | — |
| `thm:shadow-euler-independence` | `theorem` | 2488 | — |
| `cor:two-faces-theta` | `corollary` | 2545 | — |
| `thm:euler-koszul-tier-classification` | `theorem` | 2626 | — |
| `thm:sewing-hecke-reciprocity` | `theorem` | 2707 | Sewing--Hecke reciprocity |

#### `chapters/connections/holographic_codes_koszul.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:hc-knill-laflamme` | `proposition` | 96 | Knill--Laflamme from Lagrangian isotropy |
| `thm:hc-symplectic-code` | `theorem` | 224 | Symplectic code structure |
| `thm:hc-koszulness-exact-qec` | `theorem` | 344 | \textbf{G12}: Koszulness $\Leftrightarrow$ exact holographic reconstruction |
| `thm:hc-shadow-redundancy` | `theorem` | 463 | Shadow depth controls redundancy |
| `prop:hc-dictionary` | `proposition` | 564 | 12-fold dictionary |
| `thm:hc-census` | `theorem` | 719 | Standard landscape code census |

#### `chapters/connections/holographic_datum_master.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:hdm-face-1` | `theorem` | 222 | Face~1: bar-cobar twisting |
| `thm:hdm-face-2` | `theorem` | 279 | Face~2: DNP line operators; \ (identification with collision residue); \ (DNP line-operator package: Dimofte--Niu--Py 2025; Vol.~II cross-volume matching) |
| `thm:hdm-face-3` | `theorem` | 343 | Face~3: Khan--Zeng PVA \textup{(}genus~$0$ only\textup{)} |
| `thm:hdm-face-4` | `theorem` | 408 | Face~4: GZ26 commuting Hamiltonians |
| `thm:hdm-face-5` | `theorem` | 492 | Face~5: Drinfeld $r$-matrix; \ (identification with collision residue); \ (classical $r$-matrix theory: Drinfeld 1985) |
| `thm:hdm-face-6` | `theorem` | 580 | Face~6: Sklyanin bracket; \ (identification with classical limit of collision residue); \ (Sklyanin bracket: Semenov-Tian-Shansky 1983) |
| `thm:hdm-face-7` | `theorem` | 658 | Face~7: Gaudin Hamiltonians |
| `thm:hdm-seven-way-master` | `theorem` | 735 | Seven-way master theorem |
| `prop:hdm-four-recovery-directions` | `proposition` | 887 | Four recovery directions with precise scope |
| `thm:hdm-higher-gaudin` | `theorem` | 1156 | Higher Gaudin Hamiltonians |

#### `chapters/connections/master_concordance.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-seven-face` | `theorem` | 39 | Seven-face identification; \ for faces $1$--$4$, $7$; \ for faces $5$--$6$ on Drinfeld $1985$ and Semenov-Tian-Shansky $1983$ |

#### `chapters/connections/poincare_computations.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-c26-selfdual` | `proposition` | 163 | Virasoro NAP duality at \texorpdfstring{$c=26$}{c=26} |
| `thm:genus-complementarity` | `theorem` | 290 | Genus complementarity |

#### `chapters/connections/semistrict_modular_higher_spin_w3.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:finite-degree-polynomial-pva-chapter` | `theorem` | 100 | Finite-degree theorem for polynomial PVAs |
| `cor:semistrictity-classical-W3-chapter` | `corollary` | 138 | Semistrictity of the classical $W_3$ bulk |
| `prop:tree-identity-semistrict-chapter` | `proposition` | 156 | Tree identity for semistrict cyclic theories |
| `prop:canonical-central-hodge-shadow-lift-chapter` | `proposition` | 243 | Canonical central Hodge-shadow lift |
| `prop:clutching-duality-shadow-lift-chapter` | `proposition` | 276 | Clutching additivity and duality symmetry |
| `thm:fiber-decomposition-shadow-base-point-chapter` | `theorem` | 318 | Fiber decomposition over the shadow base point |
| `cor:shadow-centered-reduction-chapter` | `corollary` | 346 | Shadow-centered reduction |
| `thm:finite-degree-convolution-chapter` | `theorem` | 381 | Finite-degree convolution theorem |
| `thm:quadratic-cubic-twisting-theorem-chapter` | `theorem` | 433 | Quadratic-cubic twisting theorem |
| `prop:admissibility-finite-slices-chapter` | `proposition` | 508 | Admissibility and finite-dimensional weight slices |
| `thm:cubic-weight-recursion-chapter` | `theorem` | 531 | Cubic weight recursion around the shadow base point |
| `cor:cubic-obstruction-classes-chapter` | `corollary` | 562 | Cubic obstruction classes |
| `prop:stable-graph-identity-chapter` | `proposition` | 575 | Stable-graph identity for semistrict modular theories |
| `prop:well-definedness-completed-boundary-model-chapter` | `proposition` | 629 | Well-definedness of the completed boundary model |
| `thm:main-semistrict-modular-higher-spin-package-chapter` | `theorem` | 659 | Main Theorem: the classical $W_3$ sector defines a semistrict modular higher-spin package |
| `cor:platonic-reduction-W3-frontier` | `corollary` | 694 | Platonic reduction of the $W_3$ frontier |

#### `chapters/connections/subregular_hook_frontier.tex` (17)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:pbw-slodowy-collapse` | `theorem` | 81 | PBW--Slodowy collapse |
| `cor:principal-w-completed-koszul` | `corollary` | 140 | Principal affine \texorpdfstring{$W$}{W}-algebras are completed Koszul |
| `prop:transport-propagation` | `proposition` | 256 | Transport propagation lemma |
| `prop:hook-ghost-constant` | `proposition` | 330 | Hook ghost constant |
| `prop:ds-bar-hook-commutation` | `proposition` | 381 | Hook-type compatibility criteria |
| `thm:canonical-degree-detection` | `theorem` | 473 | Generator-degree detection of canonical degree |
| `thm:full-raw-coefficient-packet` | `theorem` | 621 | Exact Bell recursion for the full singular packet |
| `thm:miura-product-formula` | `theorem` | 779 | Subregular Miura product formula |
| `thm:subregular-appell-formula` | `theorem` | 816 | Subregular Appell formula |
| `thm:bp-strict` | `theorem` | 888 | Bershadsky--Polyakov is strict in canonical normal form |
| `comp:bp-kappa-three-paths` | `computation` | 905 | Modular characteristic of $\mathrm{BP}_k$ |
| `prop:bp-complementarity-constant` | `proposition` | 956 | Complementarity constant for $\mathrm{BP}_k$ |
| `thm:bp-koszul-self-dual` | `theorem` | 1002 | Bershadsky--Polyakov Koszul self-duality |
| `thm:w4-cubic` | `theorem` | 1109 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} has canonical degree $3$ |
| `thm:unbounded-canonical-degree` | `theorem` | 1240 | Unbounded canonical degree in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | 1294 | Triangular primary-renormalization theorem |
| `prop:nilpotent-transport-typeA` | `proposition` | 1519 | Nilpotent transport for type $A$ |

#### `chapters/connections/thqg_entanglement_programme.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-lagrangian-constraint` | `theorem` | 174 | Lagrangian constraint theorem |
| `thm:thqg-qes-convergence` | `theorem` | 331 | QES convergence |
| `prop:thqg-barcobar-error-correction` | `proposition` | 595 | Bar-cobar code structure |
| `thm:thqg-entanglement-wedge` | `theorem` | 661 | Subregion structure from the open/closed realization |
| `thm:thqg-page-constraint` | `theorem` | 702 | Algebraic Page constraint |

#### `chapters/connections/thqg_open_closed_realization.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:bd-algebraic-bridge` | `proposition` | 111 | Bridge: BD chiral operad $\leftrightarrow$ algebraic $\mathcal{E}\!\mathit{nd}^{\mathrm{ch}}$ |
| `thm:thqg-brace-dg-algebra` | `theorem` | 249 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | 467 | Universal open/closed pair (chiral Swiss-cheese theorem) |
| `prop:mixed-sector-bulk-boundary` | `proposition` | 550 | Mixed sector encodes bulk-to-boundary module structure |
| `thm:thqg-local-global-bridge` | `theorem` | 618 | Local-global bridge |
| `thm:thqg-annulus-trace` | `theorem` | 719 | Annulus trace theorem |
| `prop:thqg-annulus-degeneration-kappa` | `proposition` | 990 | Annulus degeneration and the genus-$1$ curvature |
| `thm:thqg-oc-mc-equation` | `theorem` | 1065 | Open/closed MC equation |
| `thm:thqg-oc-projection` | `theorem` | 1126 | Open/closed projection principle |
| `thm:thqg-mc-forced-consistency` | `theorem` | 1185 | MC-forced open-closed consistency |
| `thm:thqg-oc-quartic-vanishing` | `theorem` | 1509 | Vanishing and nonvanishing of $\mathfrak{R}^{\mathrm{oc}}_{4}$ |

### Appendices (216)

#### `appendices/_sl2_yangian_insert.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:ordered-bar-sl2` | `computation` | 86 | Degree-$2$ ordered bar complex of $\widehat{\mathfrak{sl}}_2$ |
| `prop:ybe-from-d-squared` | `proposition` | 164 | $d^2=0$ is the classical Yang--Baxter equation |
| `thm:yang-r-matrix` | `theorem` | 227 | Yang $R$-matrix from the ordered bar complex |
| `thm:rtt-sl2` | `theorem` | 302 | RTT presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:pbw-sl2` | `theorem` | 420 | PBW basis of $Y_\hbar(\mathfrak{sl}_2)$ |
| `cor:hilbert-sl2` | `corollary` | 456 | Hilbert series |
| `prop:eval-tensor-sl2` | `proposition` | 502 | Tensor products and Yang--Baxter |
| `thm:sl2-koszul-dual` | `theorem` | 533 | Open-colour Koszul dual of $\widehat{\mathfrak{sl}}_2$ is $Y_\hbar(\mathfrak{sl}_2)$ |

#### `appendices/arnold_relations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:operadic-equivalence-arnold` | `proposition` | 73 | Operadic equivalence: Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d^2 = 0$}{d\textasciicircum 2 = 0} |
| `thm:bar-d-squared-arnold` | `theorem` | 92 | Bar differential squares to zero |
| `cor:bar-d-squared-zero-arnold` | `corollary` | 164 | Bar differential squares to zero |
| `thm:arnold-iff-nilpotent` | `theorem` | 180 | Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d_{\text{residue}}^2 = 0$}{d\_residue\textasciicircum 2 = 0} |
| `thm:config-boundary-relations` | `theorem` | 378 | Configuration space boundary relations |
| `cor:dres-squared-global` | `corollary` | 501 | \texorpdfstring{$d_{\mathrm{res}}^2 = 0$}{d\_res\textasciicircum 2 = 0} globally |

#### `appendices/branch_line_reductions.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:scalar-mc-skeleton` | `proposition` | 175 | The scalar shadow is an abelian MC element |
| `thm:spectral-cumulant-hierarchy` | `theorem` | 234 | Spectral cumulant hierarchy |
| `thm:first-obstruction-traceless-quadratic` | `theorem` | 316 | First obstruction is traceless and quadratic |
| `cor:filtered-lift-vanishing` | `corollary` | 389 | Vanishing criterion for filtered lifts |
| `lem:positive-weight-contraction` | `lemma` | 457 | Positive-weight contraction |
| `thm:vir-positive-weight-acyclic` | `theorem` | 474 | Positive-weight Virasoro sectors are acyclic |
| `cor:vir-localization-reduced-spectral` | `corollary` | 493 | Localization to reduced spectral sectors |
| `prop:odd-sheet-rigidity` | `proposition` | 521 | Odd-sheet rigidity for one-line reductions |
| `cor:mu2-centered-at-13` | `corollary` | 562 | The genus-\(2\) one-line coefficient is centered at \texorpdfstring{$13$}{13} |
| `lem:universal-branch-moments` | `lemma` | 625 | Universal branch moments |
| `thm:hodge-depth-formula` | `theorem` | 687 | Depth formula |
| `lem:separating-hodge-splitting` | `lemma` | 720 | Separating Hodge splitting |
| `lem:nonseparating-hodge-extension` | `lemma` | 762 | Nonseparating Hodge extension |
| `thm:genus-two-transparency` | `theorem` | 801 | Genus-\(2\) transparency on a one-line branch quotient |
| `cor:vir-genus-two-vanishing` | `corollary` | 845 | Virasoro genus-\(2\) coefficient vanishes in the one-line quotient |
| `cor:first-primitive-genus-three` | `corollary` | 857 | The first primitive traceless coefficient begins in genus \texorpdfstring{$3$}{3} |
| `lem:genus-three-rose-unique` | `lemma` | 875 | Uniqueness of the primitive rose in genus \texorpdfstring{$3$}{3} |
| `thm:pure-branch-primitive-coefficient` | `theorem` | 905 | Pure-branch primitive coefficient on a rank-two sheet |
| `thm:first-primitive-top-hodge-layer` | `theorem` | 1000 | First primitive top-Hodge layer |
| `cor:genus-three-primitive-top-hodge` | `corollary` | 1037 | The genus-\(3\) primitive coefficient |
| `cor:shared-sheet-universal-coefficients` | `corollary` | 1109 | Universal coefficients on the shared sheet |

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-pade` | `proposition` | 904 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dual_methodology.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-infty-operads` | `theorem` | 158 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |

#### `appendices/hochschild_conventions.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:hochschild-crosswalk` | `proposition` | 26 | Three Hochschild theories: type signatures, scope, and comparison rules |

#### `appendices/homotopy_transfer.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:htt-rectification` | `proposition` | 15 | Homotopy transfer as rectification mechanism |
| `lem:sdr-existence` | `lemma` | 146 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 455 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 524 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 618 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 734 | Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0} |

#### `appendices/koszul_reference.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:essential-image-koszul` | `theorem` | 268 | Essential image of Koszul duality |
| `lem:conilpotency-necessary` | `lemma` | 330 | Conilpotency is necessary |
| `lem:connectedness-augmentation` | `lemma` | 359 | Connectedness characterizes augmentation |
| `thm:koszul-geom-rep` | `theorem` | 388 | Koszul duals are geometrically representable |
| `cor:geom-implies-koszul` | `corollary` | 420 | Converse: geometric representability implies Koszul |
| `thm:curvature-central-appendix` | `theorem` | 470 | Curvature must be central |
| `thm:uniqueness-algebra` | `theorem` | 622 | Uniqueness up to quasi-isomorphism |

#### `appendices/nonlinear_modular_shadows.tex` (69)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:nms-mc-principle` | `theorem` | 178 | Algebra structure $=$ Maurer--Cartan element |
| `prop:shadow-linfty-obstruction` | `proposition` | 211 | Genus-$0$ shadow obstruction tower as $L_\infty$ formality obstruction tower |
| `prop:nms-five-component` | `proposition` | 335 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | 395 | Shadow obstruction tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | 435 | All families from universal evaluation |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | 528 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | 582 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | 628 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | 637 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | 658 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | 673 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | 772 | Quartic shadow master equations |
| `thm:nms-separating-boundary-recursion` | `theorem` | 811 | Separating boundary recursion through quartic order |
| `thm:nms-shadow-cocycle-characterization` | `theorem` | 873 | Finite-order realization of the universal class |
| `prop:nms-quartic-closure-envelope` | `proposition` | 924 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | 954 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | 974 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | 1038 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | 1062 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | 1143 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | 1167 | Vanishing of the quartic contact invariant |
| `cor:nms-betagamma-boundary-law` | `corollary` | 1191 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | 1208 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | 1236 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | 1278 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | 1316 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | 1344 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | 1416 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | 1472 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `thm:nms-w3-full-quartic-gram` | `theorem` | 1531 | Full $\mathcal W_3$ quartic Gram determinant |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | 1604 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | 1622 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | 1638 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | 1747 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | 1799 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 1823 | Clutching law for the modular quartic resonance class |
| `thm:nms-first-nonlinear-shadow-theta` | `theorem` | 1897 | The first nonlinear shadow of \texorpdfstring{$\Theta_{\cA}$}{ThetaA} |
| `cor:nms-family-boundary-behavior` | `corollary` | 1910 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | 1979 | Functoriality and duality through quartic order |
| `thm:nms-full-resonance-tower` | `theorem` | 2005 | Full resonance tower |
| `thm:nms-all-degree-master-equation` | `theorem` | 2110 | All-degree master equation |
| `cor:nms-quintic-master-equation` | `corollary` | 2133 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | 2153 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | 2172 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | 2191 | Finite termination for primitive archetypes |
| `thm:nms-all-degree-separating-boundary` | `theorem` | 2216 | All-degree separating boundary recursion |
| `cor:nms-quintic-separating-boundary` | `corollary` | 2232 | Quintic separating boundary recursion |
| `prop:nms-genus-loop-properties` | `proposition` | 2278 | Basic properties of the genus loop operator |
| `thm:nms-nonseparating-clutching-law` | `theorem` | 2295 | Non-separating clutching law for the shadow obstruction tower |
| `cor:nms-genus-one-hessian-correction` | `corollary` | 2319 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | 2343 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2418 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2452 | Ambient complementarity and nonlinear modular shadows |
| `thm:nms-all-degree-resonance-boundary` | `theorem` | 2621 | All-degree boundary law for the resonance tower |
| `thm:nms-bipartite-complementarity` | `theorem` | 2821 | Bipartite complementarity principle |
| `thm:nms-bipartite-vanishing` | `theorem` | 2926 | Bipartite vanishing theorem |
| `thm:reduced-weight-finiteness` | `theorem` | 3269 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | 3357 | Window locality |
| `cor:exact-stabilization` | `corollary` | 3379 | Exact stabilization |
| `lem:nms-euler-inversion` | `lemma` | 3555 | Euler inversion |
| `prop:kac-shadow-singularity` | `proposition` | 3642 | Kac-shadow singularity principle |
| `thm:ds-shadow-depth-increase` | `theorem` | 3753 | DS shadow depth increase |
| `thm:shadow-subalgebra-autonomy` | `theorem` | 3958 | Shadow subalgebra autonomy |
| `cor:w-line-alternating-vanishing` | `corollary` | 4034 | $W$-line alternating vanishing |
| `thm:nms-shadow-mc-potential` | `theorem` | 4063 | Shadow obstruction tower as cyclic $L_\infty$ MC potential |
| `prop:nms-shadow-convergence` | `proposition` | 4127 | Shadow potential convergence |
| `thm:nms-mc-moduli-curve-structure` | `theorem` | 4236 | MC moduli curve structure |
| `thm:nms-hadamard-mc-potential` | `theorem` | 4299 | Hadamard factorization of the MC potential |
| `cor:nms-mc-solution-counting` | `corollary` | 4346 | MC solution counting |

#### `appendices/ordered_associative_chiral_kd.tex` (89)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bicom-e` | `lemma` | 167 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | 250 | Ordered chiral shuffle theorem |
| `prop:r-matrix-descent-vol1` | `proposition` | 510 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | 655 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | 798 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | 839 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | 871 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | 882 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | 945 | — |
| `prop:one-defect` | `proposition` | 972 | — |
| `thm:tangent=K` | `theorem` | 994 | Tangent identification |
| `cor:infdual` | `corollary` | 1031 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | 1054 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | 1106 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | 1139 | Diagonal correspondence |
| `cor:unit` | `corollary` | 1187 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | 1205 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | 1234 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | 1266 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | 1292 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | 1312 | Cap action |
| `thm:pair-of-pants` | `theorem` | 1367 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | 1405 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | 1459 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | 1508 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | 1532 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | 1645 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | 2076 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | 2190 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | 2258 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | 2314 | Formality: class~G, shadow depth~$2$ |
| `thm:bg-ordered-bar` | `theorem` | 2425 | Free-field ordered bar complexes |
| `thm:wakimoto-ordered-bar` | `theorem` | 2496 | Wakimoto bar complex descent |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | 2598 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | 2664 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | 2724 | Ordered Koszul dual of lattice algebras |
| `thm:drinfeld-yangian-sl2` | `theorem` | 2824 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | 2914 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | 2950 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | 3002 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | 3043 | Classical limit |
| `prop:vir-collision-residue` | `proposition` | 3132 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | 3162 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | 3189 | Gravitational Yangian collapse |
| `thm:vir-non-formality` | `theorem` | 3256 | Virasoro non-formality |
| `prop:grav-yangian-curvature` | `proposition` | 3302 | Gravitational Yangian curvature |
| `cor:gauge-gravity-dichotomy-ordered` | `corollary` | 3338 | Gauge-gravity complexity dichotomy |
| `thm:central-extension-invisible` | `theorem` | 3434 | Central extension is invisible to the open-colour double bar |
| `thm:two-colour-double-kd` | `theorem` | 3500 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | 3526 | Non-redundancy of the two colours |
| `thm:km-yangian` | `theorem` | 3608 | Universal Kac--Moody Yangian theorem |
| `thm:root-space-one-dim-v1` | `theorem` | 3926 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | 3975 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | 4041 | Dynkin coefficient via the beta integral |
| `thm:complete-strictification-v1` | `theorem` | 4122 | Complete strictification for all simple Lie algebras |
| `thm:sl3-triangle-coefficient` | `theorem` | 4353 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | 4437 | Serre relations from root-space vanishing |
| `thm:sl3-rtt` | `theorem` | 4488 | RTT presentation for $Y_\hbar(\mathfrak{sl}_3)$ from the ordered bar complex |
| `thm:sl3-strictification` | `theorem` | 4560 | Vanishing of the spectral Drinfeld class for $\mathfrak{sl}_3$ |
| `thm:sl4-quadrilateral` | `theorem` | 4632 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:B2-ordered-bar` | `theorem` | 4719 | Ordered bar complexes and Yangian $R$-matrices for rank-$2$ non-$A$ types |
| `thm:b-cycle-quantum-group` | `theorem` | 5031 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | 5156 | Drinfeld--Kohno; {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | 5237 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | 5311 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | 5352 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | 5515 | Ordered depth spectrum |
| `thm:ordered-AOS` | `theorem` | 5567 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | 5637 | Averaging and surplus |
| `thm:w3-ordered-bar` | `theorem` | 6094 | Ordered bar complex of $\mathcal{W}_3$ via DS transport |
| `thm:class-m-ds-transport` | `theorem` | 6243 | Class~M persistence under DS transport |
| `thm:unshifted-identification` | `theorem` | 6473 | Unshifted identification |
| `thm:factorisation-identification` | `theorem` | 6517 | Factorisation identification on the Koszul locus |
| `prop:r-matrix-stable-envelope` | `proposition` | 6562 | $R$-matrix comparison |
| `comp:sl2-eval` | `computation` | 6706 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | 6750 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | 6798 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | 6840 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | 6875 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `prop:eval-drinfeld` | `proposition` | 6927 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | 6994 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | 7055 | Braiding from the $R$-matrix |
| `thm:annular-bar-differential` | `theorem` | 7211 | Annular bar differential |
| `thm:annular-HH` | `theorem` | 7304 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | 7404 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:elliptic-spectral-dichotomy` | `theorem` | 7563 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `prop:r-matrix-eigenvalue` | `proposition` | 7766 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | 7782 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | 8065 | $\mathsf{E}_1$ ordered bar landscape |

#### `appendices/q_convention_bridge_appendix.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:q-convention-bridge-main` | `theorem` | 82 | Q-convention bridge |
| `thm:q-bridge-cocycle` | `theorem` | 286 | Q-bridge as Z/2-cover cocycle |

#### `appendices/signs_and_shifts.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:graded-jacobi` | `proposition` | 40 | Graded Jacobi identity |
| `prop:duality-grading` | `proposition` | 169 | Duality and grading reversal |
| `prop:susp-diff` | `proposition` | 273 | Suspension and differentials |
| `prop:LV-conversion-complete` | `proposition` | 1050 | Loday--Vallette conversion |

#### `appendices/spectral_higher_genus.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:convergence-criterion-spectral` | `theorem` | 73 | Convergence criterion |
