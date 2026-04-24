# Theorem Registry

Auto-generated on 2026-04-24 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2937 |
| Total tagged claims | 3871 |
| Active files in `main.tex` | 131 |
| Total `.tex` files scanned | 151 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2937 |
| `ProvedElsewhere` | 526 |
| `Conjectured` | 348 |
| `Conditional` | 28 |
| `Heuristic` | 29 |
| `Open` | 3 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 1276 |
| `proposition` | 950 |
| `corollary` | 424 |
| `lemma` | 137 |
| `computation` | 92 |
| `remark` | 53 |
| `calculation` | 3 |
| `conjecture` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 31 |
| Part I: Theory | 1556 |
| Part II: Examples | 739 |
| Part III: Connections | 395 |
| Appendices | 216 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus_modular_koszul.tex` | 284 |
| `chapters/connections/arithmetic_shadows.tex` | 137 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 115 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 97 |
| `chapters/theory/ordered_associative_chiral_kd.tex` | 91 |
| `appendices/ordered_associative_chiral_kd.tex` | 89 |
| `chapters/theory/higher_genus_complementarity.tex` | 81 |
| `chapters/examples/w_algebras.tex` | 70 |
| `appendices/nonlinear_modular_shadows.tex` | 69 |
| `chapters/theory/higher_genus_foundations.tex` | 68 |
| `chapters/examples/free_fields.tex` | 66 |
| `chapters/examples/yangians_computations.tex` | 61 |
| `chapters/examples/kac_moody.tex` | 56 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 55 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 54 |
| `chapters/theory/chiral_koszul_pairs.tex` | 54 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 53 |
| `chapters/theory/chiral_modules.tex` | 49 |
| `chapters/examples/w_algebras_deep.tex` | 48 |
| `chapters/examples/yangians_foundations.tex` | 47 |

## Complete Proved Registry

### Frame (31)

#### `chapters/frame/guide_to_main_results.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `rem:guide-four-test-interface` | `remark` | 449 | The four-test interface |

#### `chapters/frame/heisenberg_frame.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 550 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 899 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 997 | Maurer--Cartan equation for Heisenberg |
| `prop:frame-drinfeld-classical-limit` | `proposition` | 2133 | Classical limit and vanishing check |
| `prop:frame-thesis-shadow-termination` | `proposition` | 2193 | Shadow tower termination for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2769 | $\mathfrak{sl}_2$ bar complex as $E_1$-chiral coassociative coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2841 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2890 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2973 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 3011 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 3939 | Odd current $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | 4843 | The Heisenberg center |

#### `chapters/frame/part_ii_platonic_introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:part-ii-quadrichotomy-coarse-projection` | `theorem` | 241 | Quadrichotomy is coarse projection of fingerprint |
| `thm:part-ii-fingerprint-complete-invariant` | `theorem` | 311 | Fingerprint is complete invariant of bar-complex structure |
| `thm:part-ii-motivic-purity-virasoro-r-le-8` | `theorem` | 372 | Motivic purity of $S_r(\Vir_c)$ through $r \le 8$ |
| `thm:part-ii-moonshine-via-fingerprint` | `theorem` | 510 | Moonshine via fingerprint twining |
| `prop:part-ii-higher-genus-fingerprint` | `proposition` | 627 | Higher-genus fingerprint |
| `thm:part-ii-platonic-completeness` | `theorem` | 681 | Platonic completeness of Part~II |

#### `chapters/frame/part_iii_platonic_introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:part-iii-landscape-as-moduli-stack` | `theorem` | 284 | Standard landscape as C-points of $\cM_{\ChirAlg}$ |
| `thm:part-iii-central-charge-is-emergent` | `theorem` | 328 | The central charge is a functional of the fingerprint |
| `thm:part-iii-rmatrix-emergent-from-pbw` | `theorem` | 386 | The classical r-matrix is determined by PBW and OPE data |
| `thm:part-iii-grt-orbit-structure` | `theorem` | 455 | $\GRT(\Q)$ acts on $\cM_{\ChirAlg}$ preserving the fingerprint stratification; the historical seven faces are $\Q$-rational orbit representatives |
| `thm:part-iii-atlas-completeness` | `theorem` | 509 | Every non-degenerate fingerprint vector is realized |
| `prop:part-iii-landscape-restated` | `proposition` | 796 | Standard landscape restated as moduli atlas |

#### `chapters/frame/part_iv_platonic_introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:part-iv-grt-torsor-of-bridges` | `theorem` | 365 | $\Face(\cA)$ carries a $\GRT_1(\Q)$ associator action; the fingerprint quotient has nine $\Q$-rational atlas charts |
| `thm:part-iv-universal-holography-unifies` | `theorem` | 462 | The holographic functor $\Phol$ unifies all Part~\ref{part:physics-bridges} bridges |
| `thm:part-iv-celestial-is-holographic-image` | `theorem` | 571 | Celestial factorization algebra is the Mellin-shadow image of $\Phol$; \ (internal identification); \ (celestial algebra construction: Pasterski--Shao--Strominger; Strominger $w_{1+\infty}$; Vol~II \texttt{V2-thm:uch-main}). Chain-level class-$M$ statement at $g \ge 1$ open, per Vol~II \texttt{V2-conj:uch-gravity-chain-level}. |
| `thm:part-iv-e-infinity-ladder` | `theorem` | 671 | — |
| `thm:part-iv-moonshine-via-holography` | `theorem` | 779 | Monster $V^\natural$ as holographic $\Z/2$-orbifold; Dijkgraaf--Witten vanishing; \ (holographic framing of the orbifold as $\Etwo$-topological structure on the orbifold chiral Hochschild complex); \ (construction of $V^\natural$ as $\Z/2$-orbifold of $V_{\Lambda_{24}}$: Frenkel--Lepowsky--Meurman; Monster denominator identity: Borcherds; genus-zero property of McKay--Thompson series: Gannon) |
| `prop:part-iv-bridges-restated` | `proposition` | 999 | Part~\ref{part:physics-bridges} restated as the finite $\GRT_1(\Q)$ fingerprint atlas of $\Phol$ |

### Part I: Theory (1556)

#### `chapters/theory/algebraic_foundations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 1090 | Comparison: our approach vs GLZ |
| `prop:circ-associative` | `proposition` | 1182 | Associativity of the composition product |
| `thm:geometric-bridge` | `theorem` | 1670 | Geometric realization |
| `prop:orthogonal` | `proposition` | 1858 | Orthogonality |
| `prop:chirAss-self-dual` | `proposition` | 2300 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `thm:e1-chiral-notions-collapse` | `theorem` | 2387 | Collapse of $\Eone$-chiral notions on the Koszul locus |

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

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (115)

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
| `thm:bcac-extension-obstruction-across-Hn` | `theorem` | 7616 | Extension/obstruction formula for curved bar-cobar across $H_n$ |
| `thm:bcac-global-cech-descent` | `theorem` | 7759 | Global curved bar-cobar inversion via \v Cech descent |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (54)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 374 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 596 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 964 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 1081 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1154 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1198 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1266 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1332 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1473 | Positselski equivalence for the chiral bar coalgebra |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1530 | Flat finite-type reduction on the completed-dual side |
| `thm:bar-cobar-platonic` | `theorem` | 1644 | Chiral bar--cobar reconstruction, Platonic form |
| `cor:A-shriek-constructed` | `corollary` | 1924 | Constructed Koszul dual |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1984 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
| `lem:bar-cobar-associated-graded` | `lemma` | 2610 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 2636 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 2696 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 2750 | Genus-graded convergence |
| `prop:counit-qi` | `proposition` | 2868 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 2889 | Functoriality of bar-cobar inversion |
| `lem:complete-filtered-comparison` | `lemma` | 2973 | Complete filtered comparison lemma |
| `cor:completed-derived-equivalence` | `corollary` | 3074 | Completed derived equivalence |
| `thm:barr-beck-lurie-koszulness` | `theorem` | 3186 | Barr--Beck--Lurie characterization of chiral Koszulness |
| `thm:fh-concentration-koszulness` | `theorem` | 3288 | Factorization homology concentration |
| `thm:fm-boundary-acyclicity` | `theorem` | 3348 | FM boundary acyclicity |
| `prop:lagrangian-perfectness` | `proposition` | 3552 | Perfectness for the standard landscape |
| `cor:lagrangian-unconditional` | `corollary` | 3688 | Unconditional Lagrangian criterion for the standard landscape |
| `prop:bar-fh` | `proposition` | 4089 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 4167 | Cobar as factorization cohomology |
| `prop:subexponential-growth-automatic` | `proposition` | 4750 | Sub-exponential growth is automatic |
| `thm:ks-centrality` | `theorem` | 4974 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | 5017 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | 5068 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | 5103 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | 5149 | Quadratic frontier |
| `prop:eta-hessian-transfer` | `proposition` | 5243 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | 5279 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | 5329 | Admissible cyclic rigidity |
| `cor:ds-not-first-frontier` | `corollary` | 5364 | Drinfeld--Sokolov reductions remain one-channel in the semisimple admissible sector |
| `thm:classification-scalar-genera` | `theorem` | 5409 | Classification of scalar genera \textup{(}uniform-weight\textup{)} |
| `thm:platonic-hierarchy-log` | `theorem` | 5481 | Five-step hierarchy of the categorical logarithm |
| `prop:cech-two-element-strict` | `proposition` | 5997 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | 6325 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | 6385 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | 6421 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | 6443 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | 6541 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | 6589 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | 6612 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | 6657 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | 6688 | Repeated roots encode extension data |
| `thm:common-core-exact-sequences-inv` | `theorem` | 6735 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | 6767 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | 6841 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | 6881 | Explicit coprime-locus projectors |

#### `chapters/theory/bar_construction.tex` (30)

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
| `prop:dgla-axioms-k3-convolution` | `proposition` | 2773 | dGLA axioms for $\mathfrak{C}_{\mathbf{H}_{\Delta_5}}$ |
| `rem:theta-universal-MC-k3` | `remark` | 2839 | Universal Maurer--Cartan element $\Theta_{\mathbf{H}_{\Delta_5}}$ |
| `thm:MC-hbar3-hbar4-k3` | `theorem` | 2879 | MC verification at $\hbar^3,\hbar^4$ |
| `thm:MC-hbar7-hbar12-k3` | `theorem` | 2922 | MC verification through weight $\hbar^{12}$ |
| `thm:bc-unconditional-depth-reduction` | `theorem` | 3001 | Unconditional depth-reduction of the pentagon tower on the K3 side |

#### `chapters/theory/chern_weil_level_shift_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:level-shift-universality` | `theorem` | 177 | Level-shift universality |
| `prop:shift-appears-universally` | `proposition` | 272 | Universal occurrence of $k + \hv$ |
| `thm:h-dual-coxeter-coincidence` | `theorem` | 361 | Dual Coxeter coincidence |
| `thm:trace-KZ-convention-bridge` | `theorem` | 444 | Trace--KZ convention bridge |
| `cor:ap126-healing-universal` | `corollary` | 545 | universal healing |

#### `chapters/theory/chiral_center_theorem.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:partial-comp-assoc` | `lemma` | 228 | Associativity of partial compositions |
| `prop:geometric-algebraic-hochschild` | `proposition` | 348 | Geometric--algebraic comparison for chiral Hochschild |
| `prop:pre-lie-chiral` | `proposition` | 669 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | 697 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | 718 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | 1422 | Chiral Deligne--Tamarkin |
| `prop:derived-center-explicit` | `proposition` | 1967 | Explicit derived center: Heisenberg, affine $\widehat{\mathfrak{sl}}_2$, Virasoro |
| `prop:chirhoch1-affine-km` | `proposition` | 2136 | Generic affine first chiral Hochschild group |
| `prop:chirhoch2-affine-km-general` | `proposition` | 2230 | Generic affine second chiral Hochschild group |
| `prop:gerstenhaber-sl2-bracket` | `proposition` | 2305 | Gerstenhaber bracket on $\ChirHoch^1(V_k(\mathfrak{sl}_2))$ |
| `prop:ds-chirhoch-compatibility` | `proposition` | 2432 | DS--ChirHoch compatibility |
| `prop:heisenberg-bv-structure` | `proposition` | 2573 | BV algebra structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)$ |
| `prop:annulus-trace-standard` | `proposition` | 2741 | Annulus trace for standard families |
| `thm:derived-centre-complementarity-strengthened` | `theorem` | 2799 | Derived-centre complementarity across the standard landscape |

#### `chapters/theory/chiral_climax_platonic.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:climax-vol1-platonic` | `theorem` | 472 | Vol~I Climax surface: genus-zero pullback, verified ghost families, and five-theorem readout |
| `lem:pullback-presentation-nabla-platonic` | `lemma` | 603 | Pullback presentation of $\nabla(A)$ |
| `prop:cybe-equivalence-platonic` | `proposition` | 718 | CYBE equivalence |
| `cor:climax-drinfeld-kohno-platonic` | `corollary` | 752 | Drinfeld--Kohno from the climax |
| `cor:climax-verlinde-platonic` | `corollary` | 777 | Verlinde formula from the climax |
| `cor:climax-borcherds-platonic` | `corollary` | 807 | Borcherds product from the climax |
| `cor:climax-arnold-common-root-platonic` | `corollary` | 839 | Arnold $1969$ as common root |
| `prop:theorem-a-dual-lane-local-readout` | `proposition` | 924 | Theorem~A read back in chain-level and presentable $(\infty,1)$-categorical ambients |
| `rem:k3-koszul-structure-precise` | `remark` | 1132 | Koszul structure of the K3 chiral bialgebra: what is actually proved |
| `thm:cclimax-global-inversion-all-admissible` | `theorem` | 2641 | Climax global inversion theorem for $\mathbf{H}_{\Delta_5}$ on $\overline{\mathcal{A}_2}$ |
| `thm:unified-five-theorem-identity` | `theorem` | 2867 | Unified five-theorem identity for chiral Koszul duality |
| `prop:five-archetype-specialisation` | `proposition` | 3031 | Five-archetype landscape specialisation |
| `prop:unified-identity-three-path-verification` | `proposition` | 3099 | Three-path verification of the unified identity |
| `thm:climax-crown-canonical-curve` | `theorem` | 3288 | The canonical curve for the crown row |
| `cor:climax-crown-genus-stratified` | `corollary` | 3376 | The crown row is genus-stratified |

#### `chapters/theory/chiral_hochschild_koszul.tex` (53)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 224 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 375 | chiral Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 413 | chiral Hochschild spectral sequence |
| `lem:hochschild-shift-computation` | `lemma` | 557 | Fulton--MacPherson collapse and chiral Hochschild duality shift |
| `lem:totalization-amplitude` | `lemma` | 659 | Per-bar-degree to totalization amplitude transport |
| `lem:chiral-quadratic-koszul` | `lemma` | 805 | Quadratic-chiral Koszul transfer |
| `prop:fm-tower-collapse` | `proposition` | 917 | Configuration-space collapse via FM-formality spectral sequence |
| `prop:chirhoch-sharp-hilbert` | `proposition` | 1215 | Sharp bigraded Hilbert series of chiral Hochschild |
| `cor:chirhoch-heisenberg` | `corollary` | 1250 | Heisenberg chiral Hochschild concentration |
| `cor:chirhoch-affine-sl2` | `corollary` | 1277 | Affine $\mathfrak{sl}_{2}$ Hochschild total dimension |
| `cor:chirhoch-virasoro-hilbert` | `corollary` | 1305 | Virasoro Hochschild Hilbert series |
| `lem:chiral-homotopy-transport` | `lemma` | 1367 | Chiral transport of Shelton--Yuzvinsky contracting homotopy |
| `thm:hochschild-concentration-E1` | `theorem` | 1524 | Ordered-bar chiral Hochschild concentration via ordered FM and pure braid Orlik--Solomon |
| `cor:hochschild-averaging-symmetric` | `corollary` | 1582 | Averaging to symmetric ChirHoch |
| `lem:chirhoch-descent` | `lemma` | 1745 | Chiral Hochschild descent |
| `thm:main-koszul-hoch` | `theorem` | 1831 | Koszul duality for chiral Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `thm:hochschild-polynomial-growth` | `theorem` | 1964 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 2210 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `prop:e2-formality-hochschild` | `proposition` | 2251 | $\Etwo$-formality of chiral Hochschild cohomology |
| `thm:bd-fact-vs-chirhoch` | `theorem` | 2359 | BD factorization cohomology versus chiral Hochschild |
| `cor:thm-H-bd-extension` | `corollary` | 2633 | Theorem~H extends to BD factorization cohomology |
| `thm:convolution-formality-one-channel` | `theorem` | 2707 | Scalar universal class implies convolution formality along its distinguished orbit |
| `thm:bifunctor-obstruction-decomposition` | `theorem` | 2902 | Bifunctor obstruction decomposition |
| `comp:boson-hochschild` | `computation` | 3118 | Boson chiral Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 3148 | Fermion chiral Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 3254 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 3348 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 3446 | Kac--Moody cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | 3653 | Genus truncation |
| `prop:hochschild-shadow-projection` | `proposition` | 3726 | Hochschild as degree-$2$ shadow projection |
| `thm:mc2-1-km` | `theorem` | 3755 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 3872 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 4119 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 4205 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 4324 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | 4506 | Strictification principle for modular deformation theory |
| `prop:d-mod-squared-zero` | `proposition` | 4641 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 4776 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 4950 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 5140 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 5266 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 5522 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 5678 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 5817 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 5902 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 5949 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 6247 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 6378 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 6425 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 6623 | $bc$/$\beta\gamma$ Koszul duality |
| `thm:gerstenhaber-structure` | `theorem` | 6647 | Chiral Gerstenhaber structure on $\ChirHoch^*$ |
| `prop:hochschild-cech-ss` | `proposition` | 7001 | chiral Hochschild--\v{C}ech spectral sequence |
| `prop:envelope-shadow` | `proposition` | 7439 | Factorization envelope shadow functor |

#### `chapters/theory/chiral_koszul_pairs.tex` (54)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 306 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 478 | Right twisted tensor product as mapping cone |
| `prop:canonical-contracting-homotopy` | `proposition` | 519 | Explicit contracting homotopy for the canonical universal pair |
| `lem:filtered-comparison` | `lemma` | 648 | Filtered comparison |
| `lem:filtered-comparison-unit` | `lemma` | 676 | Bar-side filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 727 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 803 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 1083 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 1161 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 1216 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 1260 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 1450 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1563 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1597 | Converse: chiral Koszulness implies formality |
| `thm:ext-diagonal-vanishing` | `theorem` | 1667 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1704 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1730 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1816 | Kac--Shapovalov criterion for simple quotients |
| `rem:admissible-koszul-status` | `remark` | 1887 | Status of admissible simple quotients |
| `prop:li-bar-poisson-differential` | `proposition` | 2242 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | 2313 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | 2415 | Nilradical obstruction at degenerate admissible levels |
| `thm:koszul-equivalences-meta` | `theorem` | 2667 | Equivalences and consequences of chiral Koszulness |
| `prop:koszul-closure-properties` | `proposition` | 3301 | Closure of chiral Koszulness under tensor, dualization, and base change |
| `prop:swiss-cheese-nonformality-by-class` | `proposition` | 3401 | Swiss-cheese non-formality by shadow class |
| `prop:sc-formal-iff-class-g` | `proposition` | 3537 | SC-formality characterises class~$G$ |
| `prop:d-module-purity-km` | `proposition` | 3819 | $\cD$-module purity for affine Kac--Moody algebras |
| `prop:d-module-purity-km-equivalence` | `proposition` | 3855 | Kac--Moody equivalence via Saito--Kashiwara weight filtration |
| `prop:koszulness-formality-equivalence` | `proposition` | 4172 | Koszulness as formality of the convolution algebra |
| `thm:koszulness-from-sklyanin` | `theorem` | 4416 | Koszulness from Sklyanin--Poisson rigidity; {} for affine KM |
| `thm:koszulness-moduli-kp` | `theorem` | 4543 | Koszulness moduli |
| `thm:virasoro-koszulness-non-circular-kp` | `theorem` | 4659 | Virasoro Koszulness, non-circular |
| `thm:yangian-chart-inclusion-kp` | `theorem` | 4724 | Yangian chart inclusion |
| `thm:koszulness-bootstrap` | `theorem` | 4778 | Koszulness implies bootstrap closure |
| `prop:minimal-model-non-koszul` | `proposition` | 4836 | Minimal model non-Koszulness |
| `prop:cumulant-window-inversion` | `proposition` | 5034 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 5090 | Geometric bar--cobar duality |
| `prop:bar-cobar-relative-extension` | `proposition` | 5243 | Relative extension from relative Verdier base change |
| `thm:yangian-self-dual` | `theorem` | 5507 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 5567 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 5721 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 5815 | Bar computes Koszul dual, complete statement |
| `lem:completion-convergence` | `lemma` | 5903 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 5952 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 6539 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 6759 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:e1-module-koszul-duality` | `theorem` | 6883 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `prop:koszul-character-identity` | `proposition` | 7012 | Koszul character identity |
| `prop:bar-neq-quasiprimary` | `proposition` | 7048 | Bar cohomology $\neq$ quasi-primary count |
| `thm:structure-exchange` | `theorem` | 7227 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 7269 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 7315 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 7353 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 7562 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 182 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 287 | Module bar-comodule comparison on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `thm:monoidal-module-koszul` | `theorem` | 346 | Lax monoidal structure of the module bar functor |
| `prop:ext-tor-exchange` | `proposition` | 465 | Derived Ext exchange on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `prop:conformal-blocks-bar` | `proposition` | 544 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 649 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 750 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 808 | KZB connection from the bar complex |
| `prop:tilting-bar` | `proposition` | 1653 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1716 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1916 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1976 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 2010 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:logarithmic-bar` | `proposition` | 2255 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2349 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2469 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2504 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2543 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2560 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2600 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2622 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2772 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2884 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2998 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3077 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3231 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3262 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3319 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3409 | Vacuum Verma under the module bar functor on the finite-type \texorpdfstring{$\Eone$}{E1} lane |
| `prop:shapovalov-koszul` | `proposition` | 3513 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3572 | Non-vacuum Verma modules under the module bar functor on the finite-type \texorpdfstring{$\Eone$}{E1} lane |
| `cor:singular-vector-symmetry` | `corollary` | 3655 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3732 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3787 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3880 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3934 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:4000` | `calculation` | 4000 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:4027` | `calculation` | 4027 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:4058` | `calculation` | 4058 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4176 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4301 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4351 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4475 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4517 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar at dual level via DS and Verdier intertwining |
| `thm:module-genus-tower` | `theorem` | 4673 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4715 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4857 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 5006 | Fusion product compatibility on the module bar surface |
| `prop:heisenberg-fusion-splitting` | `proposition` | 5127 | Heisenberg fusion splitting |

#### `chapters/theory/climax_theorem.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:climax-genus-zero` | `theorem` | 43 | Climax of Vol~I, genus-zero form |
| `cor:climax-drinfeld-kohno` | `corollary` | 124 | Drinfeld--Kohno along $A \mapsto U_q$ |
| `cor:climax-borcherds` | `corollary` | 141 | Borcherds along $A \mapsto V_\Lambda$ |
| `cor:climax-verlinde` | `corollary` | 157 | Verlinde along $A \mapsto \mathrm{RCFT}$ |

#### `chapters/theory/clutching_uniqueness_platonic.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:clutching-uniqueness-socle-projection` | `theorem` | 221 | Clutching uniqueness on the socle |
| `prop:obs-g-lower-degree-components` | `proposition` | 383 | Lower-degree components of the obstruction class |
| `cor:genus-2-explicit-match` | `corollary` | 580 | Explicit match at genus $2$ |
| `thm:H04-PTVV-alternative-disjoint` | `theorem` | 655 | Factorisation-homology derivation is disjoint from the tautological-ring path |
| `lem:theorem-D-type-discipline` | `lemma` | 842 | Type discipline in the identity $\mathrm{obs}_g=\kscal\cdot\lambda_g$ |
| `prop:theta-A-genus1` | `proposition` | 898 | Genus-$1$ MC element |
| `prop:theta-A-genus2` | `proposition` | 960 | Genus-$2$ MC element, explicit form |
| `cor:theta-A-g2-three-paths` | `corollary` | 1097 | Three independent verifications of $\Theta_\cA^{(2)}$ |
| `prop:theta-A-genus3` | `proposition` | 1151 | Genus-$3$ MC element |
| `thm:theta-A-induction` | `theorem` | 1198 | Induction step for the universal MC ladder |
| `prop:mc-direct-g1-verification` | `proposition` | 1285 | $g=1$ direct MC verification |
| `prop:grr-verification-all-g` | `proposition` | 1316 | GRR verification at all $g$ |
| `prop:archetype-specialisation-obs-g` | `proposition` | 1350 | Archetype specialisation |

#### `chapters/theory/cobar_construction.tex` (32)

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
| `thm:geom-unit` | `theorem` | 1951 | Chiral bar-cobar adjunction backbone, geometric form |
| `lem:cobar-derivation-extension` | `lemma` | 2153 | Cobar derivation extension |
| `cor:chiral-adjunction-hom-bijection` | `corollary` | 2260 | Chiral bar-cobar Hom-bijection backbone |
| `thm:weak-topology` | `theorem` | 2401 | Topology |
| `thm:poincare-verdier` | `theorem` | 2460 | Bar-cobar Verdier pairing |
| `thm:curved-mc-cobar` | `theorem` | 2563 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 2588 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 2634 | Level-shifting via Verdier duality |
| `thm:central-charge-cocycle` | `theorem` | 2827 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2923 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 3064 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 3089 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 3186 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 3245 | Recognition principle |
| `lem:deformation-space` | `lemma` | 3674 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 3716 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 3764 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3844 | Curved differential formula |
| `prop:bar-cobar-MC-naturality-k3` | `proposition` | 3987 | Bar-cobar naturality of MC |

#### `chapters/theory/coderived_models.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 251 | Adequacy |
| `prop:coderived-bar-degree-spectral-sequence` | `proposition` | 316 | Coderived bar-degree spectral sequence |
| `thm:stratified-conservative-restriction` | `theorem` | 670 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 746 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 796 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 823 | Factorization co-contra correspondence |

#### `chapters/theory/compact_completed_mc3_comparison_platonic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:compact-completed-mc3-comparison` | `theorem` | 131 | Compact/completed MC3 comparison |
| `prop:compact-approximation-exists` | `proposition` | 236 | Compact approximation exists |
| `thm:mc3-full-DK-in-completed-category` | `theorem` | 342 | MC3 thick generation in the completed category |
| `cor:comparison-gap-healed-completed` | `corollary` | 391 | Compact/completed comparison gap healed in completed ambient |
| `rem:status-table-comparison-gap-completed` | `remark` | 660 | Status table |

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

#### `chapters/theory/configuration_spaces.tex` (45)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 433 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 553 | Normal crossings |
| `thm:closure-relations` | `theorem` | 648 | Closure relations |
| `thm:log-complex` | `theorem` | 765 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 803 | Arnold relations: flatness of $\nabla_{\mathrm{Arnold}}$ |
| `prop:arnold-higher-genus` | `proposition` | 902 | Higher-genus correction to the Arnold-only presentation |
| `prop:twisting-morphism-propagator` | `proposition` | 1203 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 1270 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 1337 | Residue operations |
| `prop:residue-local` | `proposition` | 1392 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 1477 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1755 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1828 | Conformal blocks from punctured bar complex |
| `thm:bordered-fm-properties` | `theorem` | 2246 | Properties of the bordered FM compactification |
| `prop:four-type-boundary` | `proposition` | 2345 | Four-type boundary decomposition |
| `thm:oc-convolution-dg-lie` | `theorem` | 2739 | dg~Lie structure on the open-closed convolution algebra |
| `thm:modular-mc-clutching` | `theorem` | 2987 | Modular MC equation with clutching |
| `cor:recovery-bar-intrinsic` | `corollary` | 3333 | Recovery of the bar-intrinsic MC element |
| `prop:eta` | `proposition` | 3523 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `lem:orientation-compatibility` | `lemma` | 3930 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 3991 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 4030 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 4057 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 4079 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 4119 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 4143 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 4178 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 4200 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 4234 | Residue evaluation complexity |
| `thm:arnold-orlik-solomon` | `theorem` | 4376 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 4422 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 4457 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 4502 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 4732 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 4802 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 4939 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:5149` | `computation` | 5149 | Explicit examples |
| `thm:confspaces-canonical-curve-HDeltaFive` | `theorem` | 5416 | The canonical curve for $\mathbf{H}_{\Delta_5}$ |
| `prop:confspaces-ran-space-nod-smooth-regularisation` | `proposition` | 5627 | C1. $\mathrm{Ran}(E^{\mathrm{nod,sm}}_{24})$ is a valid factorisation base |
| `thm:confspaces-factorisation-axiom-disjoint-opens` | `theorem` | 5675 | C2. Factorisation axiom for $\mathbf{H}_{\Delta_5}$ on disjoint opens |
| `thm:confspaces-locality-homotopy-colimit` | `theorem` | 5737 | C3. Locality and homotopy-colimit descent |
| `prop:confspaces-unit-axiom` | `proposition` | 5774 | C3.~bis. Unit axiom |
| `thm:confspaces-co-associativity-nodal-coproduct` | `theorem` | 5798 | C4. Co-associativity of the nodal local coproduct at chain level |
| `thm:confspaces-ran-space-cocycle-witness` | `theorem` | 5880 | C5. Chain-level cocycle witness for the Ran-space class |
| `cor:confspaces-five-axioms-discharged` | `corollary` | 5958 | Five axioms discharged at chain level |

#### `chapters/theory/conformal_anomaly_rigidity_platonic.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:casimir-nonvanishing` | `lemma` | 139 | Nonvanishing and integrality of $\Cas$ |
| `thm:conformal-anomaly-rigidity` | `theorem` | 182 | Conformal-anomaly rigidity |
| `thm:c-zero-coproduct-is-constant` | `theorem` | 239 | Coproduct is constant at $c = 0$ |
| `prop:spectral-parameter-forced-at-nonzero-c` | `proposition` | 274 | Spectral parameter is forced at $c \neq 0$ |
| `thm:universal-coefficient` | `theorem` | 298 | Universality of the coefficient |
| `cor:forbidden-c-0-locus-chiralization` | `corollary` | 338 | Chiralisation is obstructed away from $c = 0$ |

#### `chapters/theory/derived_langlands.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:langlands-bar-bridge` | `theorem` | 97 | Critical bar-to-oper bridge |
| `thm:oper-bar-h0-dl` | `theorem` | 323 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 358 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 382 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 419 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 500 | Differential analysis at degree 3 |
| `prop:d4-nonvanishing` | `proposition` | 580 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 639 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 652 | Full oper differential-form identification |
| `rem:critical-level-theta` | `remark` | 808 | The MC element $\Theta_{\cA}$ at critical level |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 1181 | Chain-level KL adjunction from bar-cobar |
| `thm:dl-octachotomy-satake-bridge` | `theorem` | 1921 | Octachotomy--derived-Satake bridge at $g=2$; \ on $U_2^{\mathrm{adm}}$, \ on the $H$-strata |
| `thm:dl-C1-r-existence` | `theorem` | 2943 | C1 -- existence and pole-order structure |
| `thm:dl-C2-CYBE` | `theorem` | 2979 | C2 -- classical Yang--Baxter equation |
| `thm:dl-C3-lie-bialgebra` | `theorem` | 3021 | C3 -- Lie bialgebra structure on $\frakg_{\Delta_5}$ |
| `thm:dl-kazhdan-classical-limit` | `theorem` | 3068 | Kazhdan classical-limit theorem |
| `thm:dl-chenevier-nonreduced-delta5` | `theorem` | 3614 | Chenevier determinant on the non-reduced deformation ring $R^{\mathrm{def}}_{\Delta_5}$ |
| `thm:dl-kazhdan-C1-mukai-eigenvalue` | `theorem` | 4080 | Mukai-graded Hecke eigenvalue formula |
| `thm:dl-derived-chenevier-gv-delta5` | `theorem` | 4338 | Derived Chenevier--Galatius--Venkatesh ring on $\Delta_5$ |
| `rem:dl-derived-chiral-bridge` | `remark` | 4700 | Cross-volume bridge: derived ring and chiral $\mathbf H_{\Delta_5}$ |
| `thm:dl-selmer-generators-explicit` | `theorem` | 4945 | Three explicit generators of $\pi_1\mathcal R^{\mathrm{der}}_{\Delta_5}$ |

#### `chapters/theory/e1_modular_koszul.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | 231 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | 250 | — |
| `thm:e1-mc-element` | `theorem` | 347 | $E_1$ Maurer--Cartan element |
| `prop:e1-nonsplitting-obstruction` | `proposition` | 432 | $E_1$ non-splitting obstruction |
| `prop:e1-nonsplitting-genus1` | `proposition` | 537 | $E_1$ non-splitting at genus~$1$: quasi-modular obstruction |
| `prop:e1-shadow-r-matrix` | `proposition` | 823 | — |
| `prop:symmetric-descent` | `proposition` | 966 | Symmetric descent |
| `thm:av-functoriality` | `theorem` | 1003 | Functoriality of the averaging map under chiral algebra morphisms |
| `cor:av-kernel-deg3-split` | `corollary` | 1173 | Ordered/symmetric chain-level kernel split, class-by-class, at degree~3 |
| `thm:av-kernel-graded-lie-structure` | `theorem` | 1323 | Structural description of $\ker(\operatorname{av})$ as a graded Lie algebra, with degree-$3$ Ihara bracket and cohomological map to $\mathfrak{grt}_1$ |
| `cor:r-matrix-sigma2-symmetric` | `corollary` | 1835 | $r$-matrix $\Sigma_2$-symmetry on the four archetypes |
| `thm:e1-formality-bridge` | `theorem` | 2188 | Formality bridge |
| `thm:e1-formality-failure` | `theorem` | 2227 | Formality failure for genuinely $\Eone$-chiral algebras |
| `thm:e1-mc-finite-degree` | `theorem` | 2340 | $E_1$ MC equation at finite degree |
| `thm:e1-coinvariant-shadow` | `theorem` | 2411 | Coinvariant projection: $E_1$ shadows to $E_\infty$ shadows |
| `rem:ribbon-structure-count` | `remark` | 2462 | Ribbon structure count |
| `rem:fcom-fass-scalar-agreement` | `remark` | 2493 | $F\!\Com = F\!\Ass$ at the scalar level |
| `thm:e1-theorem-A-modular` | `theorem` | 2877 | Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction |
| `thm:e1-theorem-B-modular` | `theorem` | 2934 | Theorem~$\mathrm{B}^{E_1}$ at all genera: ordered bar--cobar inversion |
| `thm:e1-theorem-C-modular` | `theorem` | 2960 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
| `thm:e1-theorem-D-modular` | `theorem` | 3000 | Theorem~$\mathrm{D}^{E_1}$ at all genera: formal ordered degree-$2$ shadow series |
| `thm:e1-theorem-H-modular` | `theorem` | 3071 | Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered chiral Hochschild at genus~$g$ |
| `prop:sn-irrep-decomposition-bar` | `proposition` | 3278 | $\Sigma_n$-irreducible decomposition of the ordered bar complex |
| `lem:bare-graph-no-thooft` | `lemma` | 3387 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | 3408 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | 3450 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | 3472 | Exact $N^{\chi}$ weighting from traced open color |
| `thm:bd-factorisation-bi-unipotent-compatibility` | `theorem` | 3851 | Factorisation compatibility of the bi-unipotent pro-ambient |
| `cor:bd-factorisation-bar-cobar-preservation` | `corollary` | 3998 | Strict chain-level bar--cobar inversion preserves BD factorisation |

#### `chapters/theory/e3_identification_chain_level_platonic.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:e3-identification-chain-level-associator-fixed` | `theorem` | 411 | Chain-level $\Ethree$-identification, $\Phi = \Phi_{\KZ}$ |
| `prop:associator-dependence-explicit` | `proposition` | 595 | Associator-dependence of the chain map |
| `thm:operad-level-to-algebra-level-lift` | `theorem` | 741 | Operad-level to algebra-level formality lift |
| `cor:e3-solvable-unconditional` | `corollary` | 869 | Chain-level identification for solvable~$\fg$ is unconditional |
| `prop:sl2-associator-test` | `proposition` | 1063 | $\mathfrak{sl}_2$ associator-test |
| `thm:humbert-lusztig-mukai-8` | `theorem` | 1246 | Humbert--Lusztig--Mukai triple coincidence on the $\mathcal{B}$-family |
| `cor:kl-equivalence-k3-bkm` | `corollary` | 1365 | Kazhdan--Lusztig equivalence at $q_{\mathrm{K3}} = e^{2\pi i/8}$ |

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
| `prop:braces-from-center` | `proposition` | 2443 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | 2492 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | 2568 | Terminality of the center |
| `cor:center-functor` | `corollary` | 2657 | The center functor |
| `thm:topologization` | `theorem` | 3079 | Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}} |
| `thm:e-infinity-topologization` | `theorem` | 3220 | $E_\infty$-Topologization via iterated Sugawara |
| `cor:e-ladder-vir-wn-winfty` | `corollary` | 3244 | $E_n$ ladder specializations |
| `thm:e-infinity-topologization` | `theorem` | 3936 | $\Einf$-topologization master theorem |
| `cor:virasoro-N-2-climax` | `corollary` | 4186 | Virasoro ($N=2$) recovers the Volume~II climax |
| `cor:WN-E-Nplus1-top` | `corollary` | 4206 | $\cW_N$ gives $E_{N+1}$-topological |
| `cor:Winfty-Einf-top` | `corollary` | 4225 | $\cW_\infty$ gives $\Einf$-topological |
| `thm:coset-conformal-inheritance` | `theorem` | 4302 | Coset conformal inheritance |
| `prop:sugawara-gauge-rectification` | `proposition` | 4441 | Chain-level $\Ethree^{\mathrm{top}}$ for affine Kac--Moody via gauge rectification |
| `prop:e3-via-dunn` | `proposition` | 4916 | $\Ethree^{\mathrm{top}}$ via Dunn additivity, bypassing the Higher Deligne Conjecture |
| `lem:en-formality-deformation-classification` | `lemma` | 5249 | Formality reduction for $\En$-deformations of commutative algebras |
| `thm:e3-identification` | `theorem` | 5347 | Identification of $\Ethree$-deformation families |
| `prop:e3-explicit-sl2` | `proposition` | 5846 | Explicit $\Ethree$ operations on $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\mathfrak{sl}_2))$ |
| `prop:e3-ek-quantum` | `proposition` | 6228 | {$\Ethree$ operations on $Z^{\mathrm{der}}_{\mathrm{ch}}(V_{\mathrm{EK}})$} |
| `prop:chiral-p3-structure` | `proposition` | 6391 | The chiral $\Pthree$ structure |
| `thm:chiral-e3-structure` | `theorem` | 6478 | Structure of the chiral $\Ethree$-algebra |
| `lem:bv-p3-commutativity` | `lemma` | 6739 | Commutativity of the BV operator and the chiral $\Pthree$ bracket |
| `prop:chiral-e3-dmod` | `proposition` | 6880 | The $\cD$-module structure |
| `thm:chiral-e3-cfg` | `theorem` | 6966 | Formal disk restriction recovers CFG |
| `prop:khan-zeng-topological` | `proposition` | 7179 | Topological enhancement via Sugawara |
| `thm:en-shadow-tower` | `theorem` | 7592 | $\En$ shadow obstruction tower: universality of $\kappa$ and formality collapse |
| `prop:e3-bar-structure` | `proposition` | 7766 | $\Etwo$ structure on the bar complex and the $\mathsf{E}_3$ obstruction |

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
| `thm:ftm-seven-fold-tfae-via-hub-spoke` | `theorem` | 156 | Six-fold TFAE on the Koszul locus, with a class-$G$ seventh equivalence |
| `cor:ftm-seventh-class-G` | `corollary` | 206 | Seventh (SC-formality) equivalence on class~$G$ |
| `prop:ftm-spoke-koszul-pbw` | `proposition` | 224 | Spoke 1 |
| `prop:ftm-spoke-counit-pbw` | `proposition` | 249 | Spoke 2 |
| `prop:ftm-spoke-unit-pbw` | `proposition` | 280 | Spoke 3 |
| `prop:ftm-spoke-ttacyclic-pbw` | `proposition` | 306 | Spoke 4 |
| `prop:ftm-spoke-bar-conc-pbw` | `proposition` | 347 | Spoke 5 |
| `prop:ftm-spoke-sc-pbw` | `proposition` | 390 | Spoke 6, parametrised |
| `prop:no-tautology-at-g0` | `proposition` | 428 | Non-tautology at genus zero |
| `cor:TFAE-extends-to-genus-1-uniform-weight` | `corollary` | 504 | Genus extension of each spoke |
| `prop:class-L-witness` | `proposition` | 624 | Class-$L$ witness |
| `rem:kac-moody-filtered-comparison` | `remark` | 664 | Kashiwara filtration on the Kac--Moody vacuum module |

#### `chapters/theory/genus_2_ddybe_platonic.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:g2-face-model-bypass-scope-restricted` | `theorem` | 378 | Face-model DDYBE, scope-restricted |
| `cor:g2-chi-minus-12` | `corollary` | 654 | $\chi=-12$ from rank-$4$ KZB local system |

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

#### `chapters/theory/higher_genus_foundations.tex` (68)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:gauss-manin-uncurving-chain` | `proposition` | 385 | Gauss--Manin uncurving at chain level |
| `prop:genus-g-curvature-package` | `proposition` | 557 | The genus-$g$ curvature package |
| `prop:chain-level-curvature-operator` | `proposition` | 696 | Chain-level curvature operator |
| `prop:genus-g-mc-element` | `proposition` | 844 | Genus-$g$ MC element |
| `thm:genus-extension-hierarchy` | `theorem` | 876 | Genus extension hierarchy |
| `thm:bar-ainfty-complete` | `theorem` | 1265 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 1365 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 1460 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 1573 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 1680 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 1827 | Verdier duality of operations |
| `thm:bar-curved-ch-infty` | `theorem` | 1989 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
| `thm:convergence-filtered` | `theorem` | 2067 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 2285 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 2319 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 2353 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 2373 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 2389 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2707 | Bar-cobar isomorphism, retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 2792 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 3007 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 3613 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 3816 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 3876 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 4129 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:genus1-d-squared` | `theorem` | 4223 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 4280 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 4629 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 4662 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 4789 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 4961 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 5015 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 5095 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 5255 | \texorpdfstring{$W_3$}{W3} fiberwise obstruction |
| `comp:w3-obs-explicit` | `computation` | 5316 | Explicit genus-$1$ value of the $W_3$ obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 5353 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 5382 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 5469 | Mumford multiplicative relations for obstruction classes |
| `prop:scalar-obstruction-hodge-euler` | `proposition` | 5582 | Scalar obstruction equals Hodge Euler class |
| `lem:k-theoretic-globalization-bar` | `lemma` | 5750 | $K$-theoretic globalization of the scalar bar class |
| `prop:lambda-g-clutching` | `proposition` | 6176 | Clutching formulas for the Hodge Euler class |
| `prop:clutching-uniqueness` | `proposition` | 6266 | Clutching uniqueness of the Hodge Euler class, socle scope |
| `thm:genus-universality` | `theorem` | 6627 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 7119 | Multi-generator edge universality |
| `prop:f2-quartic-dependence` | `proposition` | 7167 | Genus-$2$ quartic dependence |
| `cor:anomaly-ratio` | `corollary` | 7228 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 7244 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 7271 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 7289 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 7312 | Universal genus-$1$ criticality criterion; scalar-lane collapse |
| `cor:tautological-class-map` | `corollary` | 7347 | Tautological class map on the scalar lane; universal genus-$1$ class |
| `prop:bar-tautological-filtration` | `proposition` | 7466 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 7538 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 7568 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 7666 | Scalar obstruction lifting criterion |
| `prop:grr-bridge` | `theorem` | 7737 | Wick-rotated \texorpdfstring{$\widehat{A}$}{A-hat} generating function on the proved scalar lane |
| `lem:stable-graph-d-squared` | `lemma` | 8014 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 8076 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 8114 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 8156 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 8245 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 8333 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 8402 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 8436 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 8491 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 8548 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 8576 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 8626 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (284)

| Label | Env | Line | Title |
|---|---|---:|---|
| `__unlabeled_chapters/theory/higher_genus_modular_koszul.tex:295` | `proposition` | 295 | MCG-equivariance of the genus tower |
| `thm:genus-graded-koszul` | `theorem` | 383 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 414 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 729 | Free-field examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 773 | Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 815 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `lem:pbw-weightwise-g-module` | `lemma` | 958 | Weightwise reduction of the genus enrichment to \texorpdfstring{$\fg$}{g}-modules |
| `lem:pbw-mixed-factorization` | `lemma` | 1017 | Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)} |
| `thm:pbw-genus1-km` | `theorem` | 1065 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 1383 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 1408 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1616 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1668 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1768 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1818 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1880 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `prop:hook-pbw` | `proposition` | 2041 | Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses |
| `thm:pbw-propagation` | `theorem` | 2133 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | 2292 | Locality of the collision differential |
| `thm:three-tier-architecture` | `theorem` | 2379 | Three-tier logical architecture of modular Koszul duality |
| `lem:e2-higher-genus` | `lemma` | 2691 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 2845 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 2954 | Modular characteristic |
| `prop:kappa-zero-noniff-critical-level` | `proposition` | 3782 | Falsification of the universal $\kappa = 0 \iff$ critical level claim |
| `prop:kappa-three-routes` | `proposition` | 3952 | Three recovery routes for $\kappa$ on the scalar lane |
| `cor:free-energy-ahat-genus` | `corollary` | 4218 | Scalar free energy as $\hat{A}$-genus |
| `prop:gue-universality` | `proposition` | 4628 | GUE universality |
| `rem:shadow-tr-pf-decomposition-identity` | `remark` | 4713 | Shadow/topological-recursion/planted-forest decomposition |
| `thm:spectral-characteristic` | `theorem` | 4752 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 4785 | Universal modular Maurer--Cartan class |
| `prop:curvature-centrality-general` | `proposition` | 4924 | Centrality of higher-genus curvature |
| `thm:mc2-bar-intrinsic` | `theorem` | 4986 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 5578 | Shadow extraction |
| `prop:mc2-functoriality` | `proposition` | 5693 | Functoriality of the bar-intrinsic MC element |
| `thm:bipartite-linfty-tree` | `theorem` | 5796 | Bipartite shadow as $L_\infty$ tree-level structure |
| `thm:explicit-theta` | `theorem` | 5920 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 6147 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 6594 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 6673 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 6786 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 6820 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 6852 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 7057 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 7134 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 7199 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 7334 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 7431 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 7542 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowdegree-packet-criterion` | `proposition` | 7679 | One-channel visible low-degree seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 7831 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 8005 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 8155 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 8349 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 8469 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 8568 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 8658 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 8770 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 8842 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 8924 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 9002 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 9079 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 9155 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 9230 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 9296 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 9376 | MC2 completion under explicit hypotheses |
| `thm:mc2-full-resolution` | `theorem` | 9462 | MC2 comparison completion on the proved scalar lane |
| `lem:mk67-from-mc2` | `lemma` | 9515 | Bar-intrinsic MC2 identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 9558 | One-channel line concentration of the minimal MC class |
| `thm:km-strictification` | `theorem` | 9629 | KM strictification of the universal class |
| `prop:w-algebra-scalar-saturation` | `proposition` | 9717 | One-channel line concentration for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 9764 | One-dimensional cyclic line persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 9825 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 9975 | One-channel line concentration for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 10078 | Cyclic rigidity and level-direction concentration |
| `prop:saturation-functorial` | `proposition` | 10271 | Functorial behavior of one-channel line concentration |
| `cor:effective-quadruple` | `corollary` | 10438 | Effective \texorpdfstring{$\Gamma$}{Gamma}-quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 10529 | Cyclic rigidity at generic level |
| `thm:algebraic-family-rigidity` | `theorem` | 10698 | Algebraic-family rigidity |
| `cor:saturation-algebraic-families` | `corollary` | 10810 | Level-direction concentration at all non-critical levels for algebraic families |
| `thm:conformal-bootstrap-rigidity` | `theorem` | 10879 | $L_0$-bootstrap rigidity |
| `cor:one-channel-no-lie` | `corollary` | 10986 | One-channel criterion without Lie symmetry |
| `thm:kappa-universal-class` | `theorem` | 11226 | Universal $\kappa$ class: existence, uniqueness, specialization |
| `thm:tautological-line-support` | `theorem` | 11384 | Tautological line support from genus universality |
| `cor:mc2-single-hypothesis` | `corollary` | 11498 | MC2 comparison gauntlet collapses on the proved scalar lane |
| `thm:convolution-dg-lie-structure` | `theorem` | 11685 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 11927 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 12375 | Modular homotopy convolution |
| `prop:modular-homotopy-type-structure` | `proposition` | 12467 | Structure of the modular homotopy type |
| `cor:strictification-comparison` | `corollary` | 12514 | Strictification comparison |
| `cor:vol1-theta-log-fm-twisting-data` | `corollary` | 12890 | $\Theta_\cA$ as universal modular twisting morphism |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | 13151 | First two weights |
| `comp:vol1-low-genus-log-fm-chart` | `computation` | 13226 | Low-genus amplitudes |
| `lem:shadow-bracket-well-defined` | `lemma` | 14005 | Well-definedness of the descended bracket |
| `prop:shadow-algebra-linfty` | `proposition` | 14027 | Transferred $L_\infty$ structure on the shadow algebra |
| `cor:shadow-algebra-functoriality` | `corollary` | 14135 | Functoriality of the shadow algebra |
| `prop:master-equation-from-mc` | `proposition` | 14173 | All-degree master equation from MC |
| `thm:ds-complementarity-tower-main` | `theorem` | 14237 | DS complementarity tower |
| `thm:recursive-existence` | `theorem` | 14478 | Recursive existence and shadow obstruction tower convergence |
| `thm:perturbative-exactness` | `theorem` | 14740 | Perturbative exactness of the modular MC element |
| `thm:universal-modular-deformation` | `theorem` | 14813 | Universal modular deformation functor |
| `thm:modular-propagator-existence` | `theorem` | 14964 | Modular propagator existence |
| `thm:logfm-modular-cocomposition` | `theorem` | 14998 | Log-FM modular cocomposition |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | 15040 | Stable-graph pronilpotent completion |
| `thm:finite-rank-spectral-reduction` | `theorem` | 15091 | Finite-rank spectral reduction |
| `thm:primitive-to-global-reconstruction` | `theorem` | 15156 | Primitive-to-global reconstruction |
| `prop:primitive-shell-equations` | `proposition` | 15306 | Primitive shell equations |
| `prop:branch-master-equation` | `proposition` | 15445 | Branch quantum master equation |
| `cor:metaplectic-square-root` | `corollary` | 15498 | Determinantal half-density |
| `thm:primitive-flat-descent` | `theorem` | 15689 | Descent to the flat modular connection |
| `thm:conformal-block-reconstruction` | `theorem` | 15768 | Scalar free-energy and determinant reconstruction from the primitive kernel on the proved uniform-weight scalar lane |
| `thm:deformation-quantization-ope` | `theorem` | 15865 | Genus expansion from the OPE |
| `thm:ran-coherent-bar-cobar` | `theorem` | 16066 | Ran-coherent bar-cobar equivalence |
| `thm:shadow-channel-decomposition` | `theorem` | 16126 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 16206 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 16258 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 16406 | Direct derivation on the proved scalar lane |
| `lem:graph-sum-truncation` | `lemma` | 16737 | Graph-sum truncation criterion |
| `thm:operadic-complexity-detailed` | `theorem` | 16813 | Operadic complexity |
| `prop:shadow-formality-low-degree` | `proposition` | 16931 | Shadow--formality identification at low degree |
| `thm:shadow-formality-identification` | `theorem` | 17002 | Shadow obstruction tower as formality obstruction tower |
| `prop:shadow-tower-three-lenses` | `proposition` | 17276 | Three lenses on the shadow obstruction tower |
| `prop:shadow-formality-higher-degree` | `proposition` | 17373 | Shadow--formality identification at higher degrees |
| `prop:linfty-obstruction-5-6` | `proposition` | 17729 | Explicit $L_\infty$ obstruction classes at degrees $5$ and $6$ |
| `prop:shadow-coefficient-rationality` | `proposition` | 17981 | Shadow coefficient rationality |
| `cor:operadic-complexity-5-7` | `corollary` | 18006 | Operadic complexity at degrees $5$--$7$ |
| `thm:shadow-archetype-classification` | `theorem` | 18392 | Shadow archetype classification |
| `cor:shadow-depth-koszul-invariance` | `corollary` | 18652 | Shadow depth under Koszul duality |
| `prop:sc-formality-by-class` | `proposition` | 18737 | Swiss-cheese formality classification by shadow class |
| `prop:shadow-depth-escalator` | `proposition` | 18827 | Shadow depth escalator |
| `thm:riccati-algebraicity` | `theorem` | 19028 | Riccati algebraicity: the shadow generating function is algebraic of degree~$2$ |
| `lem:depth-three-impossible` | `lemma` | 19191 | Impossibility of $d_{\mathrm{alg}} = 3$ |
| `prop:depth-gap-trichotomy` | `proposition` | 19272 | Algebraic depth gap: no $d_{\mathrm{alg}} = 3$ |
| `prop:hankel-extraction` | `proposition` | 19497 | Hankel extraction of the quartic contact invariant |
| `cor:signed-shadow-measure` | `corollary` | 19648 | Universal signed measure |
| `thm:shadow-epstein-zeta` | `theorem` | 19730 | The Epstein zeta function of the shadow metric |
| `prop:pole-purity` | `proposition` | 20066 | Pole purity |
| `prop:intrinsic-quartic` | `proposition` | 20084 | Intrinsic quartic principle |
| `thm:single-line-dichotomy` | `theorem` | 20119 | Single-line dichotomy |
| `prop:shadow-integrable-hierarchy` | `proposition` | 20307 | Shadow CohFT and integrable hierarchies |
| `thm:shadow-tau-kw` | `theorem` | 20371 | Shadow tau function |
| `thm:shadow-connection` | `theorem` | 20538 | Shadow connection |
| `prop:galois-koszul-sign` | `proposition` | 20664 | The Galois involution is the Koszul sign |
| `cor:discriminant-atlas` | `corollary` | 20769 | The discriminant atlas |
| `thm:shadow-separation` | `theorem` | 21022 | Shadow separation and completeness |
| `prop:propagator-variance` | `proposition` | 21126 | Propagator variance inequality |
| `prop:t-line-autonomy` | `proposition` | 21236 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | 21293 | Inter-channel coupling on sublines |
| `thm:shadow-radius` | `theorem` | 21438 | Shadow growth rate: structure and asymptotics |
| `prop:shadow-tower-growth-rate` | `proposition` | 21544 | Shadow tower growth from the shadow metric |
| `cor:virasoro-shadow-radius` | `corollary` | 21660 | Virasoro shadow growth rate |
| `prop:virasoro-shadow-ratio-riccati` | `proposition` | 21728 | Virasoro shadow ratio: Riccati recurrence and root asymptotics |
| `prop:critical-cubic-convergence` | `proposition` | 22140 | Critical cubic convergence threshold |
| `prop:virasoro-bottleneck` | `proposition` | 22229 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | 22456 | Koszul exchange of shadow regimes |
| `prop:koszul-conductor-wn` | `proposition` | 22533 | Koszul conductor of \texorpdfstring{$\cW_N$}{WN} |
| `prop:koszul-conductor-anomaly-vanishing` | `proposition` | 22592 | Anomaly-free characterisation of the Koszul conductor |
| `prop:propagator-universality` | `proposition` | 22677 | Propagator universality |
| `thm:hamilton-jacobi-shadow` | `theorem` | 23018 | Hamilton--Jacobi master equation on deformation spaces |
| `thm:shadow-finite-determination` | `theorem` | 23223 | Shadow finite determination |
| `cor:w3-reconstruction` | `corollary` | 23310 | $\cW_3$: seven parameters determine the full 2D tower |
| `thm:shadow-tautological-ring` | `theorem` | 23516 | Shadow classes in the tautological ring |
| `cor:analytic-shadow-realization` | `corollary` | 23659 | Analytic shadow realization |
| `thm:shadow-cohft` | `theorem` | 23745 | Shadow cohomological field theory |
| `thm:multi-weight-genus-expansion` | `theorem` | 23924 | Multi-weight genus expansion |
| `prop:free-field-scalar-exact` | `proposition` | 24089 | Free-field exactness of the scalar formula |
| `rem:delta-f2-graph-decomposition` | `remark` | 25207 | $\delta F_2$ graph-stratum decomposition |
| `comp:w3-genus3-cross` | `computation` | 25263 | $\cW_3$ genus-$3$ cross-channel |
| `comp:w3-genus4-cross` | `computation` | 25338 | $\cW_3$ genus-$4$ cross-channel |
| `comp:w4-full-ope-cross` | `computation` | 25437 | $\cW_4$ full-OPE cross-channel correction |
| `rem:w4-irrational-cross-channel` | `remark` | 25582 | $\cW_4$: the first irrational cross-channel correction |
| `comp:w5-full-ope-cross` | `computation` | 25614 | $\cW_5$ full-OPE cross-channel correction |
| `prop:universal-gravitational-cross-channel` | `proposition` | 25851 | Universal gravitational cross-channel formula for~$\cW_N$ |
| `rem:large-n-delta-f2-planar` | `remark` | 26118 | Large-$N$ and 't~Hooft limit of $\delta F_2$ |
| `prop:cross-channel-growth` | `proposition` | 26240 | Cross-channel growth |
| `prop:cross-channel-no-closed-form` | `proposition` | 26389 | Irreducible bivariance of the cross-channel generating function |
| `thm:shadow-tautological-relations` | `theorem` | 26589 | Shadow tautological decomposition and conditional vanishing |
| `thm:mc-tautological-descent` | `theorem` | 26685 | MC descent to tautological relations |
| `prop:self-loop-vanishing` | `proposition` | 27161 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | 27197 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | 27366 | Genus-$1$ two-point function from MC |
| `prop:wdvv-from-mc` | `proposition` | 27398 | WDVV from MC at genus~$0$ |
| `prop:mumford-from-mc` | `proposition` | 27431 | Mumford relation from MC at degree~$2$ |
| `thm:planted-forest-structure` | `theorem` | 27463 | Planted-forest structure theorem |
| `prop:w3-genus2-cross-channel-sharp-negative` | `proposition` | 27585 | $\cW_3$ genus-$2$ cross-channel: sharp negative for uniform-weight scalar formulas |
| `thm:cohft-reconstruction` | `theorem` | 27647 | Reconstruction from the MC tangent complex |
| `prop:dressed-propagator-resolution` | `proposition` | 27741 | Dressed propagator coefficient and symmetry |
| `thm:pixton-from-mc-semisimple` | `theorem` | 27880 | Pixton ideal generation on the semisimple locus |
| `prop:non-semisimple-pixton-obstruction` | `proposition` | 27967 | Non-semisimple obstruction to Pixton generation |
| `rem:pixton-mc-five-paths` | `remark` | 28029 | Five-path verification of Pixton ideal membership |
| `cor:topological-recursion-mc-shadow` | `corollary` | 28080 | Topological recursion as MC shadow |
| `thm:pixton-mc-genus2` | `theorem` | 28292 | Pixton--MC bridge at genus~$2$ |
| `thm:pixton-mc-genus3` | `theorem` | 28355 | Pixton--MC bridge at genus~$3$ |
| `prop:mumford-from-mc-explicit` | `proposition` | 28430 | Mumford formula from MC |
| `thm:spectral-curve-from-shadow` | `theorem` | 28485 | Spectral curve from shadow metric |
| `thm:tr-shadow-free-energies` | `theorem` | 28519 | TR--shadow free energy identification |
| `thm:genus4-stable-graph-census` | `theorem` | 28559 | Genus-$4$ stable graph census |
| `thm:genus4-free-energy` | `theorem` | 28588 | Genus-$4$ free energy |
| `prop:genus4-spectral-sequence` | `proposition` | 28609 | Genus-$4$ spectral sequence |
| `thm:bar-macmahon` | `theorem` | 28658 | Bar--MacMahon correspondence |
| `prop:conifold-dt-gv` | `proposition` | 28685 | Conifold DT and GV |
| `thm:shadow-dt-curve-counting` | `theorem` | 28699 | Shadow obstruction tower and DT curve counting |
| `prop:tropical-shadow-amplitudes` | `proposition` | 28736 | Tropical shadow amplitudes |
| `prop:tropical-period-theta` | `proposition` | 28759 | Tropical theta function |
| `prop:fp-genus-decay-for-double` | `proposition` | 28820 | Faber--Pandharipande genus decay |
| `thm:shadow-double-convergence` | `theorem` | 28847 | Double convergence of the shadow partition function |
| `prop:shadow-genus-closed-form` | `proposition` | 28963 | Closed form and meromorphic continuation |
| `thm:shadow-borel-genus` | `theorem` | 29043 | Borel transform of the genus series |
| `prop:shadow-stokes-multipliers` | `proposition` | 29104 | Stokes multipliers of the genus expansion |
| `thm:shadow-transseries` | `theorem` | 29132 | Trans-series and instanton sectors |
| `prop:universal-instanton-action` | `proposition` | 29207 | Universal instanton action |
| `prop:c13-full-self-duality` | `proposition` | 29526 | Full tower self-duality at $c = 13$ |
| `prop:shadow-schwarzian` | `proposition` | 29769 | Spectral Schr\"odinger potential |
| `cor:shadow-schrodinger-singularities` | `corollary` | 29806 | Singularity classification |
| `prop:shadow-wkb` | `proposition` | 29878 | WKB expansion |
| `prop:shadow-voros-classical` | `proposition` | 29948 | Classical Voros period |
| `prop:shadow-gue-bridge` | `proposition` | 29991 | Shadow--GUE bridge |
| `prop:shadow-genus-constraints` | `proposition` | 30077 | Shadow genus constraints |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | 30234 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:finite-jet-rigidity` | `proposition` | 30314 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 30337 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 30373 | Gaussian collapse for abelian input |
| `thm:cubic-gauge-triviality` | `theorem` | 30457 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | 30565 | Independent sum factorization |
| `prop:symn-kappa-linearity` | `proposition` | 30623 | Symmetric orbifold kappa linearity |
| `rem:symmetric-orbifold-kappa` | `remark` | 30707 | Symmetric orbifold kappa: four independent verifications |
| `thm:envelope-koszul` | `theorem` | 30733 | Envelope Koszulness |
| `cor:generic-ht-koszul` | `corollary` | 30811 | Generic-parameter Koszulness for HT boundary algebras |
| `thm:platonic-adjunction` | `theorem` | 30915 | Modular envelope construction and adjunction frontier |
| `cor:envelope-universal-mc` | `corollary` | 31011 | The envelope carries the canonical MC class |
| `prop:platonic-sl2-specialization` | `proposition` | 31106 | Affine \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} specialization |
| `prop:envelope-construction-strategies` | `proposition` | 31144 | Construction strategies for the modular envelope |
| `thm:shadow-depth-invariant` | `theorem` | 31216 | Shadow depth is a homotopy invariant |
| `thm:tropical-koszulness` | `theorem` | 31260 | Tropical Koszulness |
| `cor:tropical-cohen-macaulay` | `corollary` | 31350 | Tropical Koszulness as the Cohen--Macaulay property |
| `prop:genus0-curve-independence` | `proposition` | 31397 | Genus-$0$ curve-independence |
| `thm:open-stratum-curve-independence` | `theorem` | 31416 | Open-stratum curve-independence at higher genus |
| `prop:saddle-point-mc` | `proposition` | 31746 | MC element as saddle point |
| `prop:bcov-mc-projection` | `proposition` | 31933 | BCOV holomorphic anomaly equation as MC projection |
| `thm:five-from-theta` | `theorem` | 32185 | Five main theorems from the master MC element |
| `thm:obstruction-recursion` | `theorem` | 32459 | Obstruction recursion for the shadow obstruction tower |
| `thm:rectification-meta` | `theorem` | 32556 | Rectification meta-theorem |
| `thm:platonic-recovery` | `theorem` | 32652 | Recovery of the modular Koszul datum from $\Theta_\cA$ |
| `prop:chriss-ginzburg-structure` | `proposition` | 32875 | MC structure principle |
| `prop:planar-forest-coinvariant` | `proposition` | 33255 | Planar forests map to unordered forests |
| `thm:planar-forest-tropicalization` | `theorem` | 33288 | Planar tropicalization |
| `prop:ordered-log-fm-construction` | `proposition` | 33333 | Ordered log-FM construction |
| `cor:e1-ambient-d-squared-zero` | `corollary` | 33411 | $E_1$ ambient $D^2 = 0$ |
| `prop:coefficient-algebras-well-defined` | `proposition` | 33474 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 33507 | Square-zero: convolution level |
| `thm:differential-square-zero` | `theorem` | 33521 | Square-zero: ambient level |
| `thm:inductive-genus-determination` | `theorem` | 33751 | Inductive genus determination |
| `cor:genus-base-cases` | `corollary` | 33819 | Base cases |
| `thm:genus2-shell-activation` | `theorem` | 33873 | Genus-$2$ shell activation as depth diagnostic |
| `comp:vol1-genus-three-stable-graph-census` | `computation` | 34072 | Genus-$3$ stable graph census |
| `prop:2d-convergence` | `proposition` | 34369 | Two-dimensional convergence |
| `thm:analytic-algebraic-comparison` | `theorem` | 34425 | Analytic = algebraic |
| `thm:verlinde-polynomial-family` | `theorem` | 34981 | Verlinde polynomial family |
| `prop:g2-degree0` | `proposition` | 35342 | Degree-$0$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree1` | `proposition` | 35396 | Degree-$1$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-degree2` | `proposition` | 35726 | Degree-$2$ ordered chiral homology on $\Sigma_2$ |
| `prop:g2-conformal-block-degree` | `proposition` | 35823 | Genus-$2$ conformal block decomposition by degree |
| `prop:genus-g-euler-general` | `proposition` | 35884 | Euler characteristic of degree-$2$ KZB local systems: general rank and genus |
| `prop:g2-euler-n` | `proposition` | 35978 | Euler characteristic at low degrees, genus~$2$ |
| `prop:g2-nonsep-degen` | `proposition` | 36196 | Non-separating degeneration: $\Sigma_2 \to E_\tau$ |
| `prop:g2-sep-degen` | `proposition` | 36309 | Separating degeneration: $\Sigma_2 \to E_\tau \cup E_{\tau'}$ |
| `thm:determinantal-branch-formula` | `theorem` | 36692 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | 36728 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | 36759 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | 36823 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | 36859 | The frontier is cubic |
| `thm:hgmk-abar4-bar-cobar-scope` | `theorem` | 37798 | Genus-$4$ bar--cobar scope: Schottky stratum as a new stratum class; deca-unipotent Malcev closure |
| `cor:hgmk-abar4-twenty-stratum` | `corollary` | 37959 | Genus-$4$ octachotomy analogue: the twenty-stratum ambient tower on $\AbarFour$ |
| `thm:hgmk-abar5-bar-cobar-scope` | `theorem` | 38174 | Genus-$5$ bar--cobar scope: Andreotti--Mayer codim-$3$ Jacobian locus meets the tri-unipotent NL-intersection; pentadeca-unipotent Malcev closure |
| `cor:hgmk-abar5-twentyeight-stratum` | `corollary` | 38349 | Genus-$5$ octachotomy analogue: the twenty-eight-stratum ambient tower on $\AbarFive$ |
| `thm:hgmk-abar6-bar-cobar-scope` | `theorem` | 38688 | Bar--cobar scope on $\AbarSix$: unconditional $21$-unipotent Malcev ladder with hexa-unipotent Andreotti--Mayer rung |
| `thm:raw-chain-level-object-genus-g` | `theorem` | 39095 | The raw chain-level bar on $\overline{\mathcal M}_{g,n}$ is the derived pushforward of the $!$-extended ordered bar |
| `lem:hgmk-humbert-restriction-raw` | `lemma` | 39357 | Humbert-restriction of the F5 raw Schiffer extension class at $g=2$; explicit Faber--Pandharipande evaluation |
| `lem:hgmk-higher-genus-f5-restriction-g345` | `lemma` | 39654 | Higher-genus F5 raw extension class at $g=3,4,5$; class-by-class evaluation on Humbert/Heegner admissible cycles |
| `thm:hgmk-f5-raw-essential-image` | `theorem` | 40037 | Essential image of the F5 raw chain-level object across the shadow-tower quadrichotomy |
| `thm:hgmk-class-c-finite-pro-ambient` | `theorem` | 40232 | Class $\mathsf C$ F5 refinement: depth-$4$ finite pro-ambient suffices for $\beta\gamma$ |
| `thm:hgmk-am-tightness-ladder-saturation` | `theorem` | 40503 | AM tightness $\Rightarrow$ saturation of the mixed ladder at every $g\geq 6$ |
| `cor:hgmk-am-tight-iff-ladder-sat-2g-1` | `corollary` | 40598 | AM tightness $\Leftrightarrow k_{\max}(g)$-ladder saturation at every $k\leq 2g-1$ |
| `thm:hgmk-bv-implies-am-tightness` | `theorem` | 40684 | Beauville--Voisin for $\mathrm{Hilb}^{g-1}(K3)$ $\Rightarrow \AMtightG$ via Ciliberto--van~der~Geer |
| `thm:hgmk-am-tightness-g9-conditional` | `theorem` | 40841 | Andreotti--Mayer tightness at $g=9$ from Beauville--Voisin at $S^{[8 |

#### `chapters/theory/higher_kummer_arithmetic_duality_platonic.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:higher-kummer-z-g-presence` | `theorem` | 71 | Kummer-irregular primes witnessed on the $Z_g$ side |
| `thm:higher-kummer-s-r-absence-through-r-13` | `theorem` | 180 | Higher Kummer-irregular primes absent from $S_r(\Vir_c)$ through $r = 13$ |
| `thm:higher-kummer-refined-duality` | `theorem` | 312 | Refined $Z_g \leftrightarrow S_r$ arithmetic duality through $r = 13$ |

#### `chapters/theory/hochschild_cohomology.tex` (28)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 198 | Virasoro chiral Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 310 | W-algebra chiral Hochschild cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:546` | `computation` | 546 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 602 | Chiral Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 682 | Cyclic operator commutes with the chiral Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 963 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 993 | Chiral Hochschild cup product exchange |
| `thm:derived-center-hochschild` | `theorem` | 1181 | Derived center $=$ categorical Hochschild cohomology $=$ algebraic Hochschild cochains via a compact generator |
| `thm:morita-invariance-HH` | `theorem` | 1270 | Morita invariance of algebraic Hochschild cohomology |
| `prop:explicit-morita-transfer` | `proposition` | 1302 | Explicit Morita transfer |
| `thm:circle-fh-hochschild` | `theorem` | 1480 | Factorization homology on $S^1$ $=$ algebraic Hochschild chains |
| `prop:monodromy-standard` | `proposition` | 1640 | Monodromy for standard families |
| `thm:chirhoch3-Delta5-chain-level` | `theorem` | 1986 | Explicit non-vanishing chain-level $\ChirHoch^3$-cocycle on $\mathbf H_{\Delta_5}$, Siegel chamber |
| `thm:hpd-obstruction-k3e-relative-replacement` | `theorem` | 2386 | Fano obstruction to absolute HPD on~$\mathrm{K3}\times E$; relative-HPD replacement over~$E$ |
| `thm:chirhoch3-Delta5-feigin-tsygan` | `theorem` | 2547 | Chiral Feigin--Tsygan derivation of $[\chi_3 |
| `thm:chi3-siegel-eisenstein-period` | `theorem` | 2822 | Siegel--Eisenstein period identity for $\langle[\chi_3 |
| `thm:chi3-L-function-andrianov-kalinin` | `theorem` | 3049 | $L$-function of the degree-$3$ Hochschild cocycle $\chi_3$: Andrianov--Kalinin Euler factors, functional equation, Arthur--Clozel spin A-packet |
| `thm:chirhoch-above-degree-d-vanishes` | `theorem` | 3276 | $\ChirHoch^{k\ge d+1}$ vanishes on CY-$d$-chiralised algebras; Theorem~H top-degree sharpness |
| `thm:coha-yplus-voa-degree-3-dictionary` | `theorem` | 3679 | CoHA $\to \Yplus \to $ VOA dictionary at degree $3$; Polyakov $:T\partial T:$ as the $\Phi_3$-image of $h_3\in\Yplus$ |
| `thm:chirhoch3-five-archetype-portrait` | `theorem` | 4288 | Five-archetype portrait of $\ChirHoch^3$ |
| `cor:chirhoch3-unified-formula` | `corollary` | 4513 | Scoped degree-three formula across the landscape |
| `thm:chirhoch3-Delta5-derived-deformation` | `theorem` | 4587 | Derived-deformation classification of $[\chi_3 |
| `cor:chirhoch3-six-fold-confirmation` | `corollary` | 4884 | Six-way confirmation of the degree-$3$ unified formula |
| `thm:chi-hodge-derham-degenerate-delta5` | `theorem` | 4959 | Chiral NC Hodge-to-de-Rham degeneration on the Koszul locus for $\mathbf H_{\Delta_5}$ |
| `thm:chi3-mukai-hochschild-pairing` | `theorem` | 5091 | Mukai--Hochschild pairing on $\chi_3$: explicit rational value |
| `cor:chi3-mukai-nondegeneracy` | `corollary` | 5185 | Non-degeneracy of the Mukai--Hochschild pairing on $\chi_3$ |
| `thm:chirhoch3-seven-path-comparison` | `theorem` | 5257 | Seven-path comparison for $[\chi_3 |
| `cor:chirhoch3-seven-fold-confirmation` | `corollary` | 5506 | Seven-fold confirmation of the unified formula |

#### `chapters/theory/infinite_fingerprint_classification.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:fingerprint-slot-presentation-independence` | `lemma` | 81 | Presentation-independence of the fingerprint slots on the standard landscape |
| `thm:fingerprint-is-complete-invariant` | `theorem` | 163 | Infinite fingerprint classification; strengthening of Theorem~\ref{thm:fingerprint-completeness} |
| `thm:fifth-class-FF` | `theorem` | 309 | Feigin--Frenkel stratum at the critical affine fixed point |
| `thm:pole-depth-independence` | `theorem` | 465 | Pole--depth independence |
| `prop:class-from-full-tower` | `proposition` | 507 | Class determination from full shadow tower; formalisation of AP-CY\textup{12} |
| `thm:d-alg-r-max-bijection` | `theorem` | 537 | Depth bijection; closes FM\textup{110} |
| `thm:quadrichotomy-is-coarse-projection` | `theorem` | 599 | Quadrichotomy is a coarse projection; strengthening of Proposition~\ref{prop:coarse-projection-functor} |
| `thm:DS-fingerprint-transport` | `theorem` | 695 | DS transport of the fingerprint; closes FM\textup{108} |
| `cor:fingerprint-separates-landscape` | `corollary` | 846 | Completeness on the standard landscape |
| `thm:schellekens-structured-subset` | `theorem` | 878 | Structured-subset derivation of the holomorphic \texorpdfstring{$c=24$}{c=24} census; closes AP\textup{290} |
| `prop:schellekens-weight-two-threshold` | `proposition` | 1064 | Uniform weight-two threshold across the three holomorphic \texorpdfstring{$c=24$}{c=24} machineries |

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 1270 | Central charge complementarity |
| `thm:e1-primacy` | `theorem` | 1557 | $\Eone$ primacy |

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

#### `chapters/theory/koszulness_moduli_scheme.tex` (14)

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
| `rem:kms-K3-placement` | `remark` | 1128 | K3 chart placement on the Koszulness moduli scheme |
| `rem:kms-grt-transport-312` | `remark` | 1162 | $\mathrm{GRT}_1$-transport of $c_{2d}=-214$ across charts |
| `rem:kms-humbert-cocycle` | `remark` | 1195 | Humbert-$H_1$ monodromy as K3 chart-transition cocycle |

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
| `thm:mc3-evaluation-core-five-family` | `theorem` | 97 | MC3 on the evaluation-generated core, five-family mechanism |
| `prop:mc3-type-A-asymptotic-prefundamentals-platonic` | `proposition` | 208 | Asymptotic prefundamentals: rational type~$A$ |
| `prop:mc3-type-BCD-reflection-shapovalov-platonic` | `proposition` | 262 | Reflection-equation Shapovalov: twisted B/C/D |
| `prop:mc3-uniform-chari-moura-platonic` | `proposition` | 307 | Chari--Moura multiplicity-free $\ell$-weights: classical and simply-laced exceptional types |
| `prop:mc3-elliptic-theta-divisor-platonic` | `proposition` | 405 | Elliptic Bethe / DYBE: theta-divisor complement |
| `prop:mc3-super-parity-balance-platonic` | `proposition` | 439 | Super-Yangian parity-balance: $Y_\hbar(\mathfrak{gl}_{m\|n})$ |
| `prop:baxter-retraction-type-A-artifact` | `proposition` | 568 | Baxter hyperplane as a type-$A$ rational artifact |
| `cor:five-family-union-coverage` | `corollary` | 724 | Five-family union coverage |

#### `chapters/theory/mc5_class_m_chain_level_platonic.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:mc5-class-m-chain-level-pro-ambient` | `theorem` | 232 | MC5 class $\mathsf{M}$ chain-level in the pro-ambient |
| `cor:mc5-class-m-chain-level-on-inverse-limit` | `corollary` | 417 | Chain-level MC5 class $\mathsf{M}$ on the inverse limit |
| `thm:mc5-class-m-topological-chain-level-j-adic` | `theorem` | 525 | MC5 class $\mathsf{M}$ chain-level in the $J$-adic topological ambient |
| `prop:ambient-equivalence` | `proposition` | 591 | Ambient equivalence for chain-level MC5 |
| `prop:central-m0-vacuum-proportionality` | `proposition` | 785 | Sub-argument (b): vacuum-proportionality uniqueness of the central degree-2 curvature |
| `thm:mc5-wall-of-walls-strict-chain-level` | `theorem` | 1056 | Strict chain-level bar-cobar inversion on the wall-of-walls in the Deligne--Malcev bi-unipotent pro-ambient |
| `cor:global-strict-bar-cobar-humbert-stratum` | `corollary` | 1276 | Global strict chain-level bar-cobar inversion across the full Humbert stratum |
| `thm:mc5-admissible-heegner-strict-chain-level` | `theorem` | 1603 | Strict chain-level bar-cobar inversion on the admissible Heegner union in the bi-unipotent Malcev ladder |
| `cor:global-strict-admissible-heegner` | `corollary` | 1795 | Global chain-level bar-cobar inversion on the full admissible Heegner locus |
| `thm:codim3-heegner-transversality` | `theorem` | 1992 | Codim-$3$ Heegner transversality on $\overline{\mathcal A_2}$ |
| `thm:codim4-admissible-heegner-emptiness` | `theorem` | 2137 | Codim-$4$ admissible Heegner emptiness on $\overline{\mathcal A_2}$ |
| `thm:universal-k-tower-malcev-closure` | `theorem` | 2342 | Universal $k$-tower Malcev closure on $\overline{\mathcal A_g}$ |
| `thm:mc5-infty-one-obstruction-tower` | `theorem` | 2602 | $(\infty,1)$-bar--cobar inversion on $\Perf(\AbarTwo)$: the obstruction tower |
| `thm:mc5-bridgeland-slicing-reads-obstruction-tower` | `theorem` | 2651 | Bridgeland slicing reads the obstruction tower |
| `thm:mc5-compatibility-square` | `theorem` | 2741 | Chain-level $\leftrightarrow$ $(\infty,1)$-categorical compatibility square |
| `thm:compat-data-torsor-uniqueness` | `theorem` | 2924 | Uniqueness of the compatibility homotopy up to contractible choice |
| `thm:mc5-infty-two-adjunction` | `theorem` | 3220 | $(\infty,2)$-adjunction $\Om\dashv\Bch$ with triangular 2-cell structure |
| `thm:chiral-kontsevich-formality` | `theorem` | 3714 | Chiral Kontsevich formality on the Humbert-free complement |
| `cor:bar-cobar-inversion-from-formality` | `corollary` | 3889 | Bar--cobar inversion on $\mathcal U_{\mathrm{Humb}}^{\mathrm{c}}$ as a corollary of formality |
| `lem:uadm-is-koszul-locus-bar-cobar` | `lemma` | 4210 | $\Uadm$ as the Koszul locus of bar--cobar inversion |
| `thm:chiral-kontsevich-formality-unified` | `theorem` | 4293 | Chiral Kontsevich formality on $\Uadm$, unified form |

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
| `thm:shadow-tower-depth-1-rationality` | `theorem` | 80 | \label{thm:shadow-tower-depth-1-rationality}Shadow residues are depth-$1$ Arnold data |
| `thm:e1-vs-e2-mzv-depth-distinction` | `theorem` | 152 | \label{thm:e1-vs-e2-mzv-depth-distinction} $E_1$-chiral residue vs $E_2$-topological iterated integral |
| `thm:w-n-motivic-rationality-all-r` | `theorem` | 229 | \label{thm:w-n-motivic-rationality-all-r}Principal $\cW_N$ motivic rationality in all weights |
| `prop:w3-w-line-motivic-rationality` | `proposition` | 271 | \label{prop:w3-w-line-motivic-rationality} $\cW_3$ W-line explicit rationality |
| `thm:bp-motivic-rationality-arakawa` | `theorem` | 320 | \label{thm:bp-motivic-rationality-arakawa}BP motivic rationality in Arakawa convention |
| `prop:bp-fl-convention-caveat` | `proposition` | 369 | \label{prop:bp-fl-convention-caveat}FL-convention Koszul conductor: distinct constant |
| `thm:w-infty-motivic-rationality-all-r` | `theorem` | 435 | \label{thm:w-infty-motivic-rationality-all-r} $\cW_{\infty}$ motivic rationality |
| `thm:class-m-motivic-rationality-full` | `theorem` | 496 | \label{thm:class-m-motivic-rationality-full} Class M motivic rationality |

#### `chapters/theory/motivic_shadow_tower.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:shadow-tower-motivic-lift` | `theorem` | 238 | \label{thm:shadow-tower-motivic-lift}Motivic lift of the shadow tower |
| `thm:grt-motivic-coaction` | `theorem` | 352 | \label{thm:grt-motivic-coaction}GRT motivic coaction on the shadow tower |
| `prop:s4-vir-mot` | `proposition` | 432 | \label{prop:s4-vir-mot}Motivic lift of $S_4(\Vir_c)$ |
| `prop:s5-vir-mot` | `proposition` | 485 | \label{prop:s5-vir-mot}Motivic lift of $S_5(\Vir_c)$ |
| `prop:s6-w3-mot` | `proposition` | 529 | \label{prop:s6-w3-mot}Motivic lift of $S_6(W_3)$ carries $\zet^{\mot}(3)$ |
| `thm:virasoro-motivic-rationality-all-r` | `theorem` | 627 | \label{thm:virasoro-motivic-rationality-all-r}Virasoro motivic rationality in all weights |
| `rem:characteristic-primes-are-riccati-arithmetic` | `remark` | 847 | \label{rem:characteristic-primes-are-riccati-arithmetic}Characteristic primes of the shadow tower are Riccati-recurrence integer combinations, NOT Kac-determinant discriminants |
| `cor:shadow-L-pole` | `corollary` | 931 | \label{cor:shadow-L-pole}Pole structure of the motivic shadow L-function |
| `thm:kappa-vs-beta-split` | `theorem` | 1003 | \label{thm:kappa-vs-beta-split}Motivic kappa, modular beta |
| `prop:mst-nekrasov-humbert-motivic` | `proposition` | 1319 | Humbert residues are motivic weights at self-dual |
| `cor:mst-nekrasov-c3-H3` | `corollary` | 1392 | $c_3 = -8$ at $H_3$: explicit verification |

#### `chapters/theory/nilpotent_completion.tex` (14)

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
| `thm:nc-grt1-super-torsor-delta5` | `theorem` | 1970 | $\mathrm{GRT}_1^{\mathrm{super}}$-torsor structure on super-EK quantisations of $\mathfrak g_{\Delta_5}$ |
| `cor:nc-h-delta5-unique-up-to-grt1` | `corollary` | 2120 | Uniqueness of $\mathbf H_{\Delta_5}$ up to $\mathrm{GRT}_1^{\mathrm{super}}$ |
| `prop:nc-massey-triple-rrr-E8` | `proposition` | 2387 | Associator-free chain-level triple Massey product |
| `prop:nc-delta-n-explicit-higher` | `proposition` | 2645 | Explicit recurrence for $\delta^{(n)}$ at $n \ge 7$ |

#### `chapters/theory/ordered_associative_chiral_kd.tex` (91)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bicom-e` | `lemma` | 213 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | 296 | Ordered chiral shuffle theorem |
| `sec:r-matrix-descent-vol1` | `proposition` | 557 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | 702 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | 846 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | 887 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | 938 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | 958 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | 1020 | — |
| `prop:one-defect` | `proposition` | 1047 | — |
| `thm:tangent=K` | `theorem` | 1069 | Tangent identification |
| `cor:infdual` | `corollary` | 1106 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | 1138 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | 1190 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | 1223 | Diagonal correspondence |
| `cor:unit` | `corollary` | 1271 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | 1289 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | 1325 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | 1357 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | 1383 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | 1408 | Cap action |
| `thm:pair-of-pants` | `theorem` | 1471 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | 1509 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | 1563 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | 1612 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | 1642 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | 1760 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | 2231 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | 2346 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | 2427 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | 2485 | Formality: class~G, shadow depth~$2$ |
| `thm:drinfeld-yangian-sl2` | `theorem` | 2623 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | 2713 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | 2749 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | 2801 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | 2842 | Classical limit |
| `thm:central-extension-invisible` | `theorem` | 2928 | Central extension is invisible to the ordered double bar |
| `thm:two-colour-double-kd` | `theorem` | 3003 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | 3029 | Non-redundancy of the two colours |
| `prop:vir-collision-residue` | `proposition` | 3108 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | 3143 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | 3172 | Gravitational Yangian collapse |
| `thm:vir-non-formality` | `theorem` | 3239 | Virasoro non-formality |
| `prop:grav-yangian-curvature` | `proposition` | 3305 | Gravitational Yangian curvature |
| `cor:gauge-gravity-dichotomy-ordered` | `corollary` | 3350 | Gauge-gravity complexity dichotomy |
| `thm:grav-coproduct-primitive` | `theorem` | 3409 | Gravitational coproduct primitivity |
| `thm:km-yangian` | `theorem` | 3536 | Universal Kac--Moody Yangian theorem |
| `thm:root-space-one-dim-v1` | `theorem` | 3922 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | 3971 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | 4037 | Dynkin coefficient via the beta integral |
| `thm:complete-strictification-v1` | `theorem` | 4118 | Complete strictification for all simple Lie algebras |
| `rem:k3-chiral-quantum-group-identification` | `remark` | 4374 | Identification of the chiral quantum group undergirding the K3 BKM: chain-level naming |
| `thm:sl3-triangle-coefficient` | `theorem` | 4630 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | 4714 | Serre relations from root-space vanishing |
| `thm:sl3-rtt` | `theorem` | 4765 | RTT presentation for $Y_\hbar(\mathfrak{sl}_3)$ from the ordered bar complex |
| `thm:sl3-strictification` | `theorem` | 4837 | Vanishing of the spectral Drinfeld class for $\mathfrak{sl}_3$ |
| `thm:sl4-quadrilateral` | `theorem` | 4910 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:B2-ordered-bar` | `theorem` | 4997 | Ordered bar complexes and Yangian $R$-matrices for rank-$2$ non-$A$ types |
| `thm:annular-bar-differential` | `theorem` | 5205 | Annular bar differential |
| `thm:annular-HH` | `theorem` | 5298 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | 5421 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:b-cycle-quantum-group` | `theorem` | 5749 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | 6002 | Drinfeld--Kohno; {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | 6083 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | 6157 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | 6198 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | 6360 | Ordered depth spectrum |
| `thm:ordered-AOS` | `theorem` | 6412 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | 6482 | Averaging and surplus |
| `prop:ker-av-schur-weyl` | `proposition` | 6632 | Kernel of the Reynolds projector: general simple Lie algebras |
| `thm:elliptic-spectral-dichotomy` | `theorem` | 6886 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `thm:bg-ordered-bar` | `theorem` | 7103 | Free-field ordered bar complexes |
| `thm:wakimoto-ordered-bar` | `theorem` | 7174 | Wakimoto bar complex descent |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | 7277 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | 7343 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | 7403 | Ordered Koszul dual of lattice algebras |
| `comp:sl2-eval` | `computation` | 7557 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | 7618 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | 7666 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | 7708 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | 7757 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `prop:eval-drinfeld` | `proposition` | 7829 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | 7896 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | 7957 | Braiding from the $R$-matrix |
| `prop:r-matrix-eigenvalue` | `proposition` | 8064 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | 8091 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | 8189 | $\mathsf{E}_1$ ordered bar landscape |
| `thm:chiral-qg-equiv` | `theorem` | 8677 | Chiral bialgebra equivalence on the Koszul locus |
| `cor:bar-encodes-all` | `corollary` | 8861 | The ordered bar encodes all three structures |
| `thm:w-infty-chiral-qg` | `theorem` | 9053 | $\cW_{1+\infty}[\Psi |
| `rem:spin2-ceff-miura-w1infty` | `remark` | 9474 | Effective central charge and intertwining in the Miura basis |

#### `chapters/theory/periodic_cdg_admissible.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:screening-adjoint-squares` | `lemma` | 100 | Screening adjoints square to zero and satisfy quantum Serre |
| `thm:periodic-cdg-is-koszul-compatible` | `theorem` | 228 | Periodic CDG is Koszul-compatible on filtration quotients |
| `thm:admissible-kl-bar-cobar-adjunction` | `theorem` | 416 | Admissible-KL bar-cobar adjunction |
| `thm:adams-analog-construction` | `theorem` | 603 | Chiral Adams functor, rank one |
| `cor:class-M-admissible-minimal-model` | `corollary` | 729 | Class-M admissible minimal-model adjunction |

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

#### `chapters/theory/shadow_L_function_platonic.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:shL-convergence-half-plane` | `proposition` | 103 | \label{prop:shL-convergence-half-plane}Formal uniqueness and analytic growth datum |
| `thm:Fg-from-L-sh-correctly` | `theorem` | 283 | \label{thm:Fg-from-L-sh-correctly}Genus-slot bridge: $F_g$ from the $r=2g-2$ coefficient |

#### `chapters/theory/shadow_tower_higher_coefficients.tex` (45)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-shadow-recurrence` | `theorem` | 175 | \label{thm:virasoro-shadow-recurrence}Virasoro shadow recurrence |
| `thm:s6-virasoro-closed-form` | `theorem` | 249 | \label{thm:s6-virasoro-closed-form}Closed form for $S_6(\Vir_c)$ |
| `thm:s7-virasoro-closed-form` | `theorem` | 316 | \label{thm:s7-virasoro-closed-form}Closed form for $S_7(\Vir_c)$ |
| `thm:s8-virasoro-closed-form` | `theorem` | 385 | \label{thm:s8-virasoro-closed-form}Closed form for $S_8(\Vir_c)$ |
| `prop:sth-boundary-checks` | `proposition` | 508 | \label{prop:sth-boundary-checks}Boundary values through weight 8 |
| `prop:sth-leading-asymp` | `proposition` | 566 | \label{prop:sth-leading-asymp}Leading large-$c$ asymptotic coefficient |
| `thm:shadow-exponential-base-Virasoro` | `theorem` | 634 | \label{thm:shadow-exponential-base-Virasoro} The shadow-exponential base of Virasoro is $C_\Vir = 6$ |
| `thm:universal-class-M-C-is-6` | `theorem` | 678 | \label{thm:universal-class-M-C-is-6} Universal class M shadow-exponential base |
| `prop:W3-T-line-matches-Vir-subleading` | `proposition` | 735 | \label{prop:W3-T-line-matches-Vir-subleading} $\cW_3$ $T$-line subleading asymptotic matches Virasoro |
| `thm:shadow-series-closed-form-Virasoro` | `theorem` | 815 | \label{thm:shadow-series-closed-form-Virasoro} Closed-form Virasoro shadow series |
| `thm:shadow-series-closed-form-Virasoro-subleading` | `theorem` | 872 | \label{thm:shadow-series-closed-form-Virasoro-subleading} Closed-form subleading Virasoro shadow series |
| `thm:pole-doubling-all-k` | `theorem` | 968 | \label{thm:pole-doubling-all-k} Pole-doubling pattern for all $k$ |
| `prop:phi-k-leading-coefficient-arithmetic` | `proposition` | 1015 | \label{prop:phi-k-leading-coefficient-arithmetic} Arithmetic of the leading $\varphi_k$ coefficient |
| `cor:arithmetic-uniformity-class-M` | `corollary` | 1099 | \label{cor:arithmetic-uniformity-class-M} $\{2, 3\}$-adic arithmetic is uniform across universal class M stratum |
| `prop:C-A-inverse-radius` | `proposition` | 1236 | \label{prop:C-A-inverse-radius} $C_\cA$ is the inverse radius of convergence of the shadow series |
| `thm:w3-wline-closed-form` | `theorem` | 1869 | \label{thm:w3-wline-closed-form} $W_3$ $W$-line integer sequence closed form |
| `thm:w3-wline-exponential-base` | `theorem` | 1921 | \label{thm:w3-wline-exponential-base} $W$-line shadow-exponential base $C_{W_3}^{W\text{-line}} = 12$ |
| `thm:w3-wline-generating-function` | `theorem` | 1961 | \label{thm:w3-wline-generating-function} Exact generating-function closed form for the $W$-line sequence |
| `cor:w3-wline-self-consistency` | `corollary` | 2013 | \label{cor:w3-wline-self-consistency} Riccati self-consistency at the radius of convergence |
| `prop:sth-virasoro-rational-through-8` | `proposition` | 2319 | \label{prop:sth-virasoro-rational-through-8}No motivic period enters Virasoro through weight 8 |
| `prop:sth-summary` | `proposition` | 2376 | \label{prop:sth-summary}Closed-form Virasoro shadow spectrum through weight 8 |
| `thm:s-r-kummer-absent-through-r-11` | `theorem` | 2436 | \label{thm:s-r-kummer-absent-through-r-11}The Bernoulli-leading Kummer pair $\{691, 3617\}$ is absent from $S_r(\Vir_c)$ through $r = 11$ |
| `thm:s9-virasoro-closed-form` | `theorem` | 2676 | \label{thm:s9-virasoro-closed-form}Closed form for $S_9(\Vir_c)$ |
| `thm:s10-virasoro-closed-form` | `theorem` | 2739 | \label{thm:s10-virasoro-closed-form}Closed form for $S_{10}(\Vir_c)$ |
| `thm:s11-virasoro-closed-form` | `theorem` | 2789 | \label{thm:s11-virasoro-closed-form}Closed form for $S_{11}(\Vir_c)$ |
| `thm:shadow-tower-asymptotic-closed-form` | `theorem` | 2826 | \label{thm:shadow-tower-asymptotic-closed-form}Closed form for the leading asymptotic |
| `cor:virasoro-23-smoothness` | `corollary` | 2896 | \label{cor:virasoro-23-smoothness}Every leading numerator is $\{2, 3\}$-smooth |
| `cor:virasoro-motivic-purity-r-leq-11` | `corollary` | 2926 | \label{cor:virasoro-motivic-purity-r-leq-11}Motivic purity through weight 11 (SPECIAL CASE of Theorem~\ref{thm:virasoro-motivic-rationality-all-r}) |
| `lem:subleading-combinatorial-identity` | `lemma` | 2997 | \label{lem:subleading-combinatorial-identity}Combinatorial identity for the subleading source |
| `thm:shadow-tower-subleading-closed-form` | `theorem` | 3023 | \label{thm:shadow-tower-subleading-closed-form}Closed form for the subleading asymptotic |
| `cor:subleading-characteristic-primes` | `corollary` | 3141 | \label{cor:subleading-characteristic-primes}Riccati- arithmetic primes of the subleading layer |
| `lem:sub-subleading-cubic-identity` | `lemma` | 3275 | \label{lem:sub-subleading-cubic-identity} Cubic combinatorial identity |
| `cor:kummer-emergence-at-r-8` | `corollary` | 3322 | \label{cor:kummer-emergence-at-r-8}Emergence of the Kummer-irregular prime $691$ at $\Gamma_{8}$ |
| `cor:tier-3-characteristic-primes` | `corollary` | 3374 | \label{cor:tier-3-characteristic-primes}Tier-3 prime content through $r = 11$ |
| `thm:shadow-tower-tier-4-closed-form` | `theorem` | 3413 | \label{thm:shadow-tower-tier-4-closed-form}Closed form for the Tier-4 sub-sub-subleading asymptotic |
| `lem:quintic-combinatorial` | `lemma` | 3473 | \label{lem:quintic-combinatorial}Quintic combinatorial identities |
| `thm:kummer-laurent-depth-controlled` | `theorem` | 3560 | \label{thm:kummer-laurent-depth-controlled}% Laurent-depth-controlled Kummer emergence |
| `cor:bernoulli-leading-duality-sharpness` | `corollary` | 3682 | \label{cor:bernoulli-leading-duality-sharpness}% Sharpness of the Bernoulli-leading arithmetic duality |
| `lem:floor-parity-subadditive` | `lemma` | 3784 | \label{lem:floor-parity-subadditive}Parity subadditivity of the floor |
| `cor:floor-shift-j-plus-k` | `corollary` | 3811 | \label{cor:floor-shift-j-plus-k}Floor shift on the index set of the shadow recurrence |
| `thm:s-r-rational-denominator-pattern` | `theorem` | 3832 | \label{thm:s-r-rational-denominator-pattern}Rational denominator pattern for the Virasoro shadow tower |
| `thm:shadow-chirhoch-dictionary` | `theorem` | 4077 | \label{thm:shadow-chirhoch-dictionary}Shadow tower $\leftrightarrow$ chiral Hochschild: chain-level dictionary |
| `cor:chirhoch-depth-forces-shadow-depth` | `corollary` | 4224 | \label{cor:chirhoch-depth-forces-shadow-depth} Shadow depth forces Hochschild depth |
| `thm:phi-n-humbert-heegner-admissibility` | `theorem` | 4352 | Humbert--Heegner admissibility filter; pentagon-tower polar cutoff; composite three-filter scope |
| `thm:phi-n-weight-11-12-13` | `theorem` | 4439 | Explicit $\phi^{(11)},\phi^{(12)},\phi^{(13)}$ in the Brown canonical basis |

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

#### `chapters/theory/shadow_tower_quadrichotomy_platonic.tex` (23)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:s2-s3-roles` | `proposition` | 214 | $S_2$ as the curvature, $S_3$ as the cubic colour |
| `thm:riccati-master` | `theorem` | 245 | Riccati master equation |
| `prop:riccati-three-presentations` | `proposition` | 294 | Three equivalent presentations |
| `thm:quadrichotomy` | `theorem` | 362 | Quadrichotomy of standard-landscape chirally Koszul vertex algebras |
| `prop:moduli-stratification-codim` | `proposition` | 486 | Moduli stratification, codimension count |
| `thm:spectral-hyperelliptic-pf` | `theorem` | 601 | Spectral hyperelliptic curve and Picard--Fuchs |
| `cor:branch-points-instantons` | `corollary` | 654 | Branch points and instanton actions |
| `prop:c1-riccati-mc` | `proposition` | 719 | C1: Riccati MC element |
| `thm:borel-summability-classM` | `theorem` | 795 | C3: Borel summability of class M, asymptotic regime |
| `thm:c4-shadow-feynman-gk` | `theorem` | 879 | C4: Shadow--Feynman as $\partial^{2} = 0$ at $b_1 = L$ |
| `prop:c5-hardy-ramanujan-cardy` | `proposition` | 979 | Hardy--Ramanujan--Cardy density at generic $c$ |
| `thm:c5-zwegers-mu-shadow-explicit` | `theorem` | 1028 | Zwegers $\mu$-shadow at generic $c$ for $\Vir_c$ |
| `cor:c5-liouville-critical-shadow` | `corollary` | 1140 | Shadow vanishing at Liouville-critical locus $c = 25$ |
| `prop:stqp-312-factor` | `proposition` | 1583 | $c_{2d} = -214$ shadow-tower decomposition |
| `prop:stqp-signature` | `proposition` | 1889 | Hyperbolic Cartan signature $(2,1)$ for $\mathbf H_{\Delta_5}$ |
| `prop:stqp-unitary-spectrum` | `proposition` | 1987 | Positive-energy unitary spectrum |
| `cor:stqp-real-imag-dichotomy` | `corollary` | 2048 | Real-root / imaginary-root dichotomy |
| `prop:stqp-theta-p-clustering` | `proposition` | 2209 | Fricke-phase clustering of Satake angles on the 22 primes $p \le 79$ |
| `prop:stqp-gauss-kuzmin` | `proposition` | 2299 | Large-deviations Gauss-Kuzmin statistic near Fricke nodes on the $22$-prime sample |
| `thm:stqp-archimedean-sign` | `theorem` | 2373 | Archimedean-$p = 2$ Arthur sign global consistency via Hilbert reciprocity |
| `thm:stqp-fricke-z8-phase-leading` | `theorem` | 2501 | $\mathbb Z/8$-phase asymptotics: leading order at the Fricke nodes |
| `thm:stqp-fricke-z8-phase-subleading` | `theorem` | 2583 | $\mathbb Z/8$-phase subleading correction: the $\cos(2\theta^*_k)$ curvature term |
| `thm:stqp-fricke-z8-ldp` | `theorem` | 2640 | Large-deviations principle for Fricke-phase clustering around the 9 $\mathbb Z/8$-nodes |

#### `chapters/theory/shadow_tower_sub_subleading_platonic.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:phi-recurrence` | `lemma` | 118 | \label{lem:phi-recurrence}Phi-recurrence |
| `prop:gamma-recurrence` | `proposition` | 150 | \label{prop:gamma-recurrence}Gamma recurrence |
| `lem:gamma-source-ratio-closed-form` | `lemma` | 180 | \label{lem:gamma-source-ratio-closed-form}Source-ratio closed form |
| `thm:shadow-tower-sub-subleading-closed-form` | `theorem` | 244 | \label{thm:shadow-tower-sub-subleading-closed-form} Sub-subleading Virasoro shadow asymptotic |
| `lem:gamma-numerator-quartic-polynomial` | `lemma` | 367 | \label{lem:gamma-numerator-quartic-polynomial}Gamma numerator polynomial |
| `lem:gamma-numerator-irreducible` | `lemma` | 395 | \label{lem:gamma-numerator-irreducible}Irreducibility over $\mathbb{Q}$ |
| `rem:gamma-691-emergence-sporadic` | `remark` | 415 | \label{rem:gamma-691-emergence-sporadic}The $691$ at $r = 8$ is a modular coincidence |
| `rem:gamma-irregular-primes-dense-but-structureless` | `remark` | 439 | \label{rem:gamma-irregular-primes-dense-but-structureless} Irregular primes appear densely but structurelessly |

#### `chapters/theory/spectral_sequences.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ss` | `theorem` | 277 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 329 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 399 | Central charge and \texorpdfstring{$d_1$}{d1} |

#### `chapters/theory/theorem_A_infinity_2.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:koszul-reflection` | `theorem` | 162 | Theorem~A: bar-cobar adjunction, reconstruction, and Verdier duality |
| `lem:archetype-H123-witness` | `lemma` | 353 | Archetype witnesses for (H1)--(H3) |
| `cor:eight-cor-twisting-morphism` | `corollary` | 558 | Twisting morphism $\tau\colon\Bbarch_X(\cA)\to\cA$ is a Maurer--Cartan element |
| `cor:eight-cor-counit-qi` | `corollary` | 585 | Counit quasi-isomorphism on $\Kosz(X)$ |
| `cor:eight-cor-unit-weq` | `corollary` | 600 | Unit weak equivalence on $\Conil(X)$ |
| `cor:eight-cor-twisted-tensor` | `corollary` | 616 | Twisted tensor acyclicity |
| `cor:eight-cor-bar-weight-1` | `corollary` | 642 | Bar concentrated in weight~$1$ at $g=0$ on class~$\mathsf{G}$ |
| `cor:eight-cor-sc-formality` | `corollary` | 674 | SC-formality on class~$\mathsf{G}$ only |
| `cor:eight-cor-R-descent` | `corollary` | 702 | $R$-twisted $\Sigma_n$-descent (unitary $R$) $\barB^{\Sigma}(\cA)\simeq B^{\ord}(\cA)^{R\text{-}\Sigma_n}$ |
| `cor:eight-cor-properad-equiv` | `corollary` | 733 | Francis--Gaitsgory $(\infty,2)$-equivalence at properad level |
| `thm:A-infinity-2` | `theorem` | 968 | Theorem~$A^{\infty,2}$: Francis--Gaitsgory bar--cobar $(\infty,2)$-equivalence at properad level |
| `cor:classical-A-from-A-infinity-2` | `corollary` | 1396 | Classical Theorem~A from Theorem~$A^{\infty,2}$ |
| `lem:R-twisted-descent` | `lemma` | 1434 | $R$-matrix-twisted $\Sigma_n$-descent, unitary $R$ |
| `cor:ainf2-downstream-list` | `corollary` | 1590 | Downstream corollaries of $A^{\infty,2}$ |
| `cor:chiral-KK-formal-smoothness` | `corollary` | 1893 | Chiral Koszulness implies properad-level formal smoothness |

#### `chapters/theory/theorem_B_scope_platonic.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-positselski-at-each-weight` | `theorem` | 188 | Chiral Positselski at each finite weight |
| `thm:chiral-positselski-weight-completed` | `theorem` | 254 | Chiral Positselski on the weight-completed bar coalgebra |
| `prop:chiral-positselski-raw-direct-sum-class-M-false` | `proposition` | 390 | Raw direct-sum chiral Positselski fails for class M at chain level |
| `lem:bar-cobar-adjunction-direction-canonical` | `lemma` | 655 | Bar-cobar adjunction direction; canonical $\Omega^{\mathrm{ch}} \dashv \bar B^{\mathrm{ch}}$ versus opposite-notation $\bar B^{\mathrm{ch}} \dashv \Omega^{\mathrm{ch}}$ |
| `thm:thm-B-coalgebra-side-unit-qi` | `theorem` | 772 | Bar-cobar unit on the coalgebra side |
| `rem:thm-B-coalg-side-ambient` | `remark` | 888 | Ambient qualifier on Theorem~B coalgebra-side unit |
| `thm:strict-chain-level-across-humbert-walls` | `theorem` | 1715 | Strict chain-level bar-cobar inversion on the formal three-wall neighbourhood |
| `thm:wall-of-walls-obstruction` | `theorem` | 2208 | Wall-of-walls obstruction: hidden structure at $H_i\cap H_j$ |
| `cor:sharpened-quadrichotomy-after-monodromy-refinement` | `corollary` | 2402 | Sharpened quadrichotomy for Theorem B after the monodromy refinement |
| `thm:tbsp-lim1-is-fourier-coefficient` | `theorem` | 2666 | $\lim^1$-obstruction is a Fourier coefficient of $\phi_{-2,1}$ |
| `prop:tbsp-baily-borel-compatibility` | `proposition` | 2765 | Baily--Borel boundary compatibility of the nearby-cycle comparison |
| `thm:tbsp-global-inversion-all-admissible` | `theorem` | 2817 | Global inversion theorem for chiral bar-cobar on $\overline{\mathcal{A}_2}$ |
| `thm:tbsp-module-theorem-B-valpha1` | `theorem` | 3233 | Module-level Theorem B for $V_{\alpha_1}$: chain-level verification |
| `prop:tbsp-homotopy-n4-valpha1` | `proposition` | 3616 | Chain-homotopy identity at $n=4$ |
| `prop:tbsp-homotopy-n5-valpha1` | `proposition` | 3670 | Chain-homotopy identity at $n=5$ |
| `prop:tbsp-homotopy-n6-valpha1` | `proposition` | 3723 | Chain-homotopy identity at $n=6$ |
| `cor:tbsp-homotopy-all-n-valpha1` | `corollary` | 3750 | Uniform identity at every bar degree |
| `thm:tbsp-theorem-B-vacuum` | `theorem` | 3806 | Theorem B on vacuum |
| `thm:tbsp-theorem-B-adjoint` | `theorem` | 3898 | Theorem B on adjoint |
| `thm:tbsp-theorem-B-Vbeta` | `theorem` | 4020 | Theorem B on isotropic imaginary-root module |

#### `chapters/theory/theorem_C_refinements_platonic.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `ch:theorem-C-refinements-platonic` | `conjecture` | 50 | — |

#### `chapters/theory/theorem_h_off_koszul_platonic.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:theorem-h-on-koszul-locus` | `theorem` | 125 | Theorem~H on the Koszul locus; sharp bigraded Hilbert series |

#### `chapters/theory/three_hochschild_unification_platonic.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:three-hochschild-chain-level-agreement-low-degree` | `theorem` | 170 | Image-level comparison in low degrees on the Koszul locus |
| `thm:three-hochschild-cohomological-agreement-all-degree` | `theorem` | 315 | Cohomological agreement on the full range on the Koszul locus |
| `prop:three-hochschild-high-degree-divergence` | `proposition` | 371 | High-degree divergence of the three theories |
| `thm:critical-level-ff-center-unification` | `theorem` | 431 | Critical-level degree-zero comparison |

#### `chapters/theory/three_invariants.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:three-invariants-relations` | `proposition` | 188 | Relations and independence |
| `thm:k-max-trichotomy` | `theorem` | 335 | The $k_{\max}$ trichotomy |
| `thm:fingerprint-completeness` | `theorem` | 413 | Fingerprint completeness |
| `thm:five-class-stratum` | `theorem` | 484 | Five-class stratum |
| `prop:coarse-projection-functor` | `proposition` | 533 | Coarse projection functor |

#### `chapters/theory/topologization_chain_level_platonic.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:QG1-remainder` | `proposition` | 237 | Explicit $Q$-variation of $G_1$ |
| `prop:eta-i-primitive` | `proposition` | 326 | $\eta_1^{(\mathrm i)}$ is a $Q$-primitive of $R_{\mathrm{ghost}}$ |
| `prop:eta-ii-primitive` | `proposition` | 389 | $\eta_1^{(\mathrm{ii})}$ is a $Q$-primitive of $R_{\mathrm{self}}$ |
| `cor:eta-primitive` | `corollary` | 413 | $\eta_1$ is a $Q$-primitive of $R_1 := R_{\mathrm{ghost}} + R_{\mathrm{self}}$ |
| `thm:sugawara-antighost-primitive-chain-level` | `theorem` | 425 | Sugawara antighost primitive, chain level |
| `prop:translation-inv-tildeG` | `proposition` | 459 | Translation invariance of $\widetilde G_1$ |
| `thm:chain-level-E3-top-class-L` | `theorem` | 482 | Chain-level $\Ethree^{\mathrm{top}}$ for class $L$ |
| `prop:eta-formula-sl2-k1-explicit` | `proposition` | 541 | $\eta_1$ formula at sl$_2$ level $1$ |
| `prop:critical-level-collapse` | `proposition` | 598 | Critical-level collapse to $\Etwo^{\mathrm{top}}$ |

#### `chapters/theory/universal_conductor_K_platonic.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:uc-universal-conductor` | `theorem` | 172 | \textbf{Universal conductor as ordered-to-symmetric descent} |
| `thm:uc-trinity` | `theorem` | 243 | \textbf{Three descriptions of the image} |
| `prop:uc-kernel-dimension` | `proposition` | 301 | Schur--Weyl kernel count |
| `thm:uc-kernel-archetypes` | `theorem` | 323 | Named kernel witnesses by archetype |
| `thm:uc-landscape-universality` | `theorem` | 444 | Constructed universality map, verified row-by-row |
| `thm:uc-K-Atiyah` | `theorem` | 516 | Ordered-Koszul boundary for Vol~III comparisons |
| `cor:uc-K-heisenberg` | `corollary` | 602 | Heisenberg compatibility value |
| `cor:uc-K-affine-KM` | `corollary` | 618 | Affine Kac--Moody compatibility value |
| `cor:uc-K-virasoro` | `corollary` | 632 | Virasoro compatibility value |
| `cor:uc-K-WN` | `corollary` | 646 | Principal \texorpdfstring{$W_N$}{WN} compatibility value |
| `cor:uc-K-BP` | `corollary` | 664 | Bershadsky--Polyakov compatibility value |
| `cor:uc-K-lattice` | `corollary` | 678 | Lattice compatibility value |

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
| `thm:z-g-closed-form-polynomial` | `theorem` | 60 | $Z_g(k)$ closed form |
| `thm:z-g-polynomial-form` | `theorem` | 145 | Polynomial factorisation of $Z_g$ |
| `thm:z-g-leading-coefficient-bernoulli` | `theorem` | 208 | Hurwitz--Bernoulli leading coefficient |
| `thm:z-g-kummer-congruence` | `theorem` | 323 | Irregular-prime witnesses |
| `thm:z-g-s-r-arithmetic-duality` | `theorem` | 527 | $Z_g$ vs $S_r(\Vir_c)$ arithmetic duality at the Bernoulli-leading Kummer pair |

### Part II: Examples (739)

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

#### `chapters/examples/bershadsky_polyakov.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bp-koszul-conductor-polynomial` | `theorem` | 205 | Bershadsky--Polyakov Koszul-conductor polynomial identity;\ |
| `prop:bp-self-duality` | `proposition` | 253 | BP Koszul self-duality;\ |
| `prop:sl3-conductor-shift-formula` | `proposition` | 309 | Unified shift formula for $\mathfrak{sl}_3$ Koszul conductors;\ |
| `prop:bp-kappa` | `proposition` | 440 | Modular characteristic of $\mathcal{B}^k$;\ |
| `prop:bp-complementarity` | `proposition` | 527 | Complementarity;\ |
| `prop:bp-tline-depth` | `proposition` | 561 | T-line shadow depth;\ |
| `prop:bp-jline-depth` | `proposition` | 599 | J-line shadow depth;\ |
| `prop:bp-sigma` | `proposition` | 645 | Sigma non-vanishing;\ |
| `prop:bp-hook-series` | `proposition` | 725 | Self-transpose hooks;\ |

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
| `prop:bar-euler-hilbert` | `proposition` | 195 | Bar-Euler product = Hilbert series |
| `thm:moonshine-bar-euler-master` | `theorem` | 246 | Master bar-Euler moonshine identity |
| `thm:conway-chiral-structure` | `theorem` | 551 | Conway chiral structure |
| `thm:thompson-chiral` | `theorem` | 608 | Thompson chiral refinement |
| `cor:kummer-congruence-moonshine` | `corollary` | 862 | Kummer-congruence moonshine |

#### `chapters/examples/deformation_quantization.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 134 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 187 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 419 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 536 | Genus expansion |
| `prop:jacobi-nilpotent` | `proposition` | 1366 | $b_F^2 = 0$ is automatic |
| `lem:dcrit-boundary-linear` | `lemma` | 1740 | dCrit for boundary-linear $W$ |
| `thm:boundary-linear-lg` | `theorem` | 1834 | Boundary-linear LG theorem |
| `prop:defq-C1-existence` | `proposition` | 2260 | C1 -- existence and pole structure |
| `thm:defq-C2-CYBE` | `theorem` | 2288 | CYBE verification for $r(u, Z)$ -- chain-level |
| `thm:defq-C3-lie-bialgebra` | `theorem` | 2392 | C3 -- Lie bialgebra |
| `thm:defq-kazhdan-classical-limit` | `theorem` | 2445 | Kazhdan classical-limit theorem, Vol~I form |
| `thm:defq-star-product-specialisation` | `theorem` | 2622 | $\hbar^2 = -1/8$ specialisation converges and recovers $\mathbf H_{\Delta_5}$ |
| `thm:defq-unified-kontsevich-theorem` | `theorem` | 2796 | $\mathbf H_{\Delta_5}$ as super-Kontsevich deformation quantisation at $\hbar^2 = -1/8$ |

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

#### `chapters/examples/kac_moody.tex` (56)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:km-genus1-hessian` | `computation` | 279 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `thm:geometric-ope-kac-moody` | `theorem` | 579 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 613 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 653 | Wakimoto realization is Koszul dual |
| `thm:wakimoto-brst-full-nondegenerate` | `theorem` | 758 | Wakimoto BRST exactness on the full non-degenerate locus |
| `thm:sl2-koszul-dual` | `theorem` | 1116 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 1318 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 1349 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 1387 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 1445 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 1481 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 1610 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | 1644 | Killing form via structure constants |
| `prop:verdier-level-identification` | `proposition` | 1729 | Verdier level identification |
| `prop:ff-channel-shear` | `proposition` | 2085 | Feigin--Frenkel shear on channel pair |
| `prop:exceptional-shadow-invariants` | `proposition` | 2136 | Exceptional shadow invariants |
| `thm:screening-bar` | `theorem` | 2306 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 2372 | Critical fixed point for principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:kac-moody-ainfty` | `theorem` | 2441 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 2480 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 2534 | Closed-form OPE for Koszul dual |
| `comp:sl2-collision-residue-kz` | `computation` | 2593 | Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:km-quantum-groups` | `theorem` | 2887 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 3275 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 3347 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 3529 | Kac--Wakimoto formula at \texorpdfstring{$k=-1/2$}{k=-1/2} via bar spectral sequence |
| `prop:admissible-verlinde-bar` | `proposition` | 3701 | Admissible \texorpdfstring{$S$}{S}-matrix and Verlinde fusion package at \texorpdfstring{$k=-1/2$}{k=-1/2} |
| `prop:bar-whittaker` | `proposition` | 4123 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 4204 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 4272 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 4342 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 4408 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 4471 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 4517 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 4556 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 4593 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 4802 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 4832 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 4862 | Local oper differential-form identification |
| `thm:affine-cubic-normal-form` | `theorem` | 5127 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | 5163 | Affine shadow obstruction tower: finite termination at degree~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | 5201 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | 5243 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | 5313 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 5361 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 5418 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 5495 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 5581 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 5617 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 5783 | Vanishing of the genus loop on the affine cubic |
| `prop:km-cubic-shadow-level-independence` | `proposition` | 5848 | Level-independence of the cubic shadow product |
| `prop:nsl-shadow-tower` | `proposition` | 5973 | Non-simply-laced shadow obstruction tower |
| `prop:complete-exceptional-shadow` | `proposition` | 6116 | Complete exceptional shadow data |
| `prop:exceptional-anomaly-ratios` | `proposition` | 6203 | Anomaly ratios for exceptional principal $\mathcal{W}$-algebras |
| `cor:level-rank-bar-intertwining` | `corollary` | 6455 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | 6483 | Kappa anti-symmetry under Feigin--Frenkel involution |

#### `chapters/examples/landscape_census.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:minimal-model-class-transport` | `proposition` | 409 | Minimal-model class transport |
| `prop:paired-standard-mc4-frontier` | `proposition` | 1134 | Paired standard-tower MC4 completion packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 1254 | Minimal closure conditions for the standard-tower MC4 completion target |
| `cor:anomaly-ratio-ds` | `corollary` | 1519 | Anomaly ratio and DS reduction |
| `cor:genus1-anomaly-ratio` | `corollary` | 1533 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `thm:census-witness-complementarity` | `theorem` | 1587 | Witness-family complementarity from Verdier duality |
| `prop:archetype-complementarity-bridge` | `proposition` | 1758 | Archetype-by-archetype $\kappa + \kappa^!$ arithmetic with anomaly-ratio bridge |
| `prop:G-B-heisenberg-rho-bifurcation` | `proposition` | 1953 | Anomaly-ratio bifurcation between $\mathsf{G}$- and $\mathsf{B}$-Heisenbergs |
| `thm:census-self-dual-locus` | `theorem` | 2161 | Koszul self-dual locus across the witness landscape |
| `cor:subexp-free-field` | `corollary` | 3226 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 3236 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 3253 | DS reduction and bar cohomology generating functions |
| `thm:ds-spectral-branch-preservation` | `theorem` | 3420 | DS preservation of the sub-discriminant |
| `prop:ds-invariant-discriminant` | `proposition` | 3574 | DS-invariant discriminant subfactor |
| `prop:hred-sl2` | `proposition` | 3618 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `thm:bar-gf-classification` | `theorem` | 3833 | Bar cohomology generating function classification |
| `prop:discriminant-characteristic` | `proposition` | 4038 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 4129 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 4226 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 4292 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 4347 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 4398 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 4413 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 4502 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 4691 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 5003 | Spectral sequence collapse |

#### `chapters/examples/lattice_foundations.tex` (45)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lattice-sewing` | `theorem` | 110 | Lattice sewing envelope |
| `lem:lattice:cocycle-class` | `lemma` | 381 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 545 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 860 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 957 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 980 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 1015 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 1049 | Dual coalgebra of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 1100 | Koszul morphism for lattice algebras |
| `rem:lattice:koszul-dual-kappa` | `remark` | 1145 | Koszul dual kappa for non-unimodular lattices |
| `rem:lattice:dual-structure` | `remark` | 1209 | Structural form of the lattice Koszul dual |
| `thm:lattice:direct-sum` | `theorem` | 1342 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 1387 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1700 | Lattice chiral Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1745 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1787 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1810 | Modular invariance |
| `thm:lattice:niemeier-shadow-universality` | `theorem` | 1884 | Niemeier shadow universality |
| `prop:lattice:niemeier-theta-decomposition` | `proposition` | 1942 | Niemeier theta series decomposition |
| `thm:lattice:niemeier-siegel-genus2` | `theorem` | 1990 | Genus-$2$ Siegel theta series of Niemeier lattices |
| `prop:lattice:self-dual-criterion` | `proposition` | 2210 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 2227 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 2252 | Lattice twisted-sector charge inversion on the bar surface |
| `prop:lattice:deformation-properties` | `proposition` | 2436 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 2620 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 3245 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 3313 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 3387 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 3546 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3847 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3928 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 4101 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 4306 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 4349 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 4507 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 4554 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 4640 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 4721 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |
| `prop:lattice:genus1-simple-pole` | `proposition` | 4910 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4927 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | 5025 | Lattice shadow obstruction tower: termination at weight~$2$ |
| `prop:xxx-shadow-data` | `proposition` | 5158 | XXX shadow data |
| `prop:transfer-matrix-shadow-dict` | `proposition` | 5197 | Transfer matrix--shadow dictionary |
| `prop:xxz-shadow-data` | `proposition` | 5246 | XXZ shadow data |
| `prop:shadow-cardy-corrections` | `proposition` | 5313 | Shadow hierarchy and Cardy corrections |

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
| `thm:w3-minimal-complete` | `theorem` | 128 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | 262 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 410 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 434 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | 469 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 494 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 573 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 600 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 660 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 680 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 707 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 803 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

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
| `prop:symn-hecke-kappa` | `proposition` | 673 | Hecke consistency with shadow scaling |

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

#### `chapters/examples/w_algebras_deep.tex` (48)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 190 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 1187 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `thm:master-commutative-square` | `theorem` | 1473 | Master commutative square for DS reduction |
| `prop:w3-deg3-vacuum` | `proposition` | 1880 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-bar-formality` | `proposition` | 2239 | DS--bar commutation via filtration formality |
| `thm:transport-closure-type-a` | `theorem` | 2309 | Transport-closure in type $A$ |
| `prop:partition-dependent-complementarity` | `proposition` | 2363 | Kappa deficit and Koszul complementarity for non-principal DS |
| `thm:ds-platonic-functor` | `theorem` | 2545 | BRST reduction on total modular Koszul datums |
| `cor:ds-theta-descent` | `corollary` | 2772 | BRST descent of the universal MC element |
| `comp:wn-stabilization-windows` | `computation` | 3217 | Coefficient stabilization windows for $\mathcal{W}_N$ |
| `prop:abelian-locus-type-a` | `proposition` | 3287 | Abelian locus in type~$A$ |
| `prop:abelianity-complementarity-independence` | `proposition` | 3329 | Independence of abelianity and complementarity |
| `prop:bfn-slodowy-dimensions` | `proposition` | 3410 | BFN--Slodowy dimension matching |
| `prop:ghost-constant-monotonicity` | `proposition` | 3483 | Ghost constant monotonicity |
| `thm:winfty-scalar` | `theorem` | 3704 | One-dimensional cyclic line for $\mathcal{W}_\infty$ |
| `prop:gram-wt4` | `proposition` | 3859 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | 3924 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | 3967 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:higher-w-kappa-matrix` | `proposition` | 4094 | Kappa matrix for $\Walg_N$ |
| `prop:higher-w-gravitational-cubic` | `proposition` | 4157 | Gravitational cubic for $\Walg_N$ |
| `prop:higher-w-parity` | `proposition` | 4200 | $\mathbb{Z}_2$ parity and the cubic shadow |
| `prop:weight-4-exchange-upgrade` | `proposition` | 4257 | Weight-$4$ exchange spectrum upgrade at rank~$3$ |
| `prop:virasoro-primitive` | `proposition` | 4548 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | 4609 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | 4650 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | 4753 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | 4786 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | 4807 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | 4839 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | 4946 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | 4982 | $\Walg_\infty$ bar-window series and Koszul entropy |
| `thm:y-algebra-koszulness` | `theorem` | 5068 | Chiral Koszulness of $Y$-algebras |
| `thm:n2-kappa` | `theorem` | 5227 | $N=2$ modular characteristic |
| `prop:n2-koszul-duality` | `proposition` | 5283 | $N=2$ Koszul duality |
| `prop:n2-channel-decomposition` | `proposition` | 5354 | $N=2$ channel decomposition |
| `prop:n2-bosonic-shadow-metric` | `proposition` | 5387 | $N=2$ bosonic shadow metric |
| `prop:n2-minimal-models` | `proposition` | 5432 | $N=2$ minimal model shadow data |
| `thm:walgdeep-gaiotto-siegel-weight` | `theorem` | 5956 | Borcherds / Siegel weight for $\mathcal T[A_{N-1}, \Sigma_{0,24} |
| `thm:walgdeep-N6-reanchoring` | `theorem` | 6205 | $N = 6$ umbral re-anchoring to $6 D_4$ |
| `lem:walgdeep-rank-bookkeeping` | `lemma` | 6294 | Rank bookkeeping of $(24/N) A_{N-1}$ |
| `thm:walgdeep-N6-reanchor-A5-4-D4` | `theorem` | 6314 | $N=6$ re-anchor to $A_5^4 D_4$ |
| `thm:walgdeep-N7-N8-re-anchor` | `theorem` | 6518 | $N = 7$ and $N = 8$ re-anchors; ladder continuity $k_N^{\mathrm{honest}} = N + 3$ |
| `thm:walgdeep-divisor-rule` | `theorem` | 6711 | Corrected divisor rule for naive umbral labelling |
| `thm:walgdeep-substitute-anchors` | `theorem` | 6787 | Substitute Niemeier anchors at $N \in \{8, 12\}$ via rank-gluing |
| `thm:walgdeep-N24-conway` | `theorem` | 6854 | $N = 24$ escape to Conway moonshine via Leech |
| `thm:walgdeep-N9-N12-re-anchor` | `theorem` | 7035 | $N \in \{9, 10, 11, 12\}$ re-anchors; ladder continuity $k_N^{\mathrm{honest}} = N + 3$ across the Coxeter-void |
| `thm:walgdeep-N13-N24-ladder` | `theorem` | 7317 | $N \in \{13, \ldots, 24\}$ ladder; four-regime completion terminating at the Leech escape |
| `thm:walgdeep-m24-equivariant-schur` | `theorem` | 7579 | $M_{24}$-equivariant Schur-index refinement of $\mathcal T[A_1, \Sigma_{0, 24} |

#### `chapters/examples/y_algebras.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:y-central-charge` | `theorem` | 209 | {Central charge of $Y_{N_1,N_2,N_3}[\Psi |
| `comp:y-special-cases-c` | `computation` | 237 | Special cases of the central charge |
| `thm:y111-central-charge` | `theorem` | 275 | $c(Y_{1,1,1}) = 0$ |
| `thm:y111-kappa-channels` | `theorem` | 327 | {Channel-by-channel $\kappa$ for $Y_{1,1,1}[\Psi |
| `thm:y-kappa-general` | `theorem` | 383 | {General $\kappa$ for $Y_{N_1,N_2,N_3}[\Psi |
| `prop:y-koszul-dual` | `proposition` | 434 | {Koszul dual of $Y_{N_1,N_2,N_3}[\Psi |
| `prop:y-complementarity` | `proposition` | 463 | {Complementarity for $Y_{1,1,1}[\Psi |
| `thm:y-shadow-depth` | `theorem` | 500 | Shadow depth of $Y$-algebras |
| `comp:y111-collision-residue` | `computation` | 584 | {Collision residue for $Y_{1,1,1}[\Psi |
| `thm:y-koszulness` | `theorem` | 658 | {Chiral Koszulness of $Y_{N_1,N_2,N_3}[\Psi |
| `comp:y-wn-specialization` | `computation` | 692 | $Y_{0,0,N} \simeq \cW_N \times \mathfrak{gl}(1)$ |
| `comp:y-affine-specialization` | `computation` | 714 | $Y_{N,0,0} \simeq \widehat{\mathfrak{gl}}(N)$ |
| `prop:y111-genus1` | `proposition` | 733 | {Genus-$1$ free energy of $Y_{1,1,1}[\Psi |
| `prop:y111-genus-tower` | `proposition` | 752 | {Higher-genus tower of $Y_{1,1,1}[\Psi |

#### `chapters/examples/yangians_computations.tex` (61)

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
| `thm:u-zeta-8-PBW-wall-crossing` | `theorem` | 5831 | PBW increment past the De Concini--Kac wall $N = \ell/2 = 4$ |
| `rem:u-zeta-8-PBW-plateau` | `remark` | 5883 | Plateau and the Lusztig Frobenius kernel |

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
| `thm:rtt-all-classical-types` | `theorem` | 363 | RTT R-matrices for all classical types |
| `thm:yangian-e1` | `theorem` | 517 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 623 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 656 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 715 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 777 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 832 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 896 | Koszul duality on Yangian modules |
| `thm:all-types-yangian-structure` | `theorem` | 1198 | All-types Yangian structure |
| `prop:dg-shifted-comparison` | `proposition` | 1444 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1571 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `prop:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1615 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1726 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1830 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1848 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1878 | Explicit coefficient formula for the fundamental monodromy series |
| `prop:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1940 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 2004 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 2090 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 2187 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 2257 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 2326 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 2363 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2419 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2479 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2540 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2639 | Standard type-A fundamental line operator has the standard local residue |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | 3065 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | 3092 | Stabilized completed bar/cobar recovery |
| `cor:shifted-rtt-tower-convergence` | `corollary` | 3123 | Automatic tower convergence |
| `thm:shifted-rtt-mc-descent` | `theorem` | 3153 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | 3241 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | 3286 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | 3334 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | 3350 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | 3380 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | 3413 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | 3447 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | 3472 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | 3544 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | 3593 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | 3619 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | 3646 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | 3668 | Kleinian associated graded at the nilpotent point |
| `prop:elliptic-coproduct-coassoc-fay` | `proposition` | 3839 | Elliptic coproduct is Fay-coassociative |
| `thm:felder-R-half-braiding` | `theorem` | 3866 | Felder $R$-matrix as half-braiding |
| `prop:sl2-elliptic-yangian-triangle` | `proposition` | 3885 | $\slnn{2}$ elliptic triangle coherence at order $\hbar$ |

### Part III: Connections (395)

#### `chapters/connections/arithmetic_shadows.tex` (137)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:divisor-sum-decomposition` | `proposition` | 314 | Divisor-sum decomposition |
| `prop:sewing-trace-formula` | `proposition` | 352 | Sewing trace formula |
| `thm:sewing-selberg-formula` | `theorem` | 390 | Sewing--Selberg formula |
| `thm:narain-universality` | `theorem` | 447 | Narain universality |
| `thm:e8-epstein` | `theorem` | 478 | $E_8$ Epstein factorization |
| `prop:z2-epstein` | `proposition` | 503 | $\bZ^2$ Epstein zeta |
| `prop:leech-epstein` | `proposition` | 526 | Leech Epstein factorization |
| `prop:niemeier-multichannel` | `proposition` | 767 | Multi-channel Niemeier discrimination |
| `prop:shadow-arithmetic-factorization` | `proposition` | 855 | Shadow--arithmetic factorization |
| `prop:hecke-all-orders` | `proposition` | 1194 | Exactness of the Hecke identification |
| `prop:period-shadow-dictionary` | `proposition` | 1245 | Period--shadow dictionary |
| `comp:period-shadow-vz` | `computation` | 1328 | $V_{\bZ}$: the Gaussian archetype |
| `comp:period-shadow-ve8` | `computation` | 1346 | $V_{E_8}$: the Lie/tree archetype |
| `comp:period-shadow-leech` | `computation` | 1368 | $V_{\mathrm{Leech}}$: the Ramanujan archetype |
| `comp:period-shadow-rank24-comparison` | `computation` | 1420 | $D_{16}^+ \oplus D_{16}^+$ vs.\ $E_8^3$: same depth, different coefficient |
| `comp:period-shadow-rank2` | `computation` | 1439 | $V_{\bZ^2}$ and $V_{A_2}$: Dedekind zeta at depth~$2$ |
| `thm:spectral-decomposition-principle` | `theorem` | 1463 | Spectral decomposition principle |
| `prop:growth-rate-dictionary` | `proposition` | 1550 | Growth-rate dictionary |
| `prop:self-referentiality-criterion` | `proposition` | 1594 | Self-referentiality criterion |
| `cor:conformal-vector-infinite-depth` | `corollary` | 1664 | Conformal vector implies infinite shadow depth |
| `thm:shadow-tower-asymptotics` | `theorem` | 1687 | Shadow obstruction tower leading asymptotics |
| `cor:rigorous-infinite-depth` | `corollary` | 1719 | Rigorous infinite shadow depth |
| `prop:ising-d-arith` | `proposition` | 1796 | Ising model: $d_{\mathrm{arith}} = 0$ |
| `rem:ising-arithmetic-paradox` | `remark` | 1824 | The Ising arithmetic paradox |
| `rem:non-unimodular` | `remark` | 1892 | Non-unimodular lattices |
| `thm:depth-decomposition` | `theorem` | 1961 | Depth decomposition |
| `rem:depth-decomposition-universality` | `remark` | 2053 | Universality and the complete $d_{\mathrm{alg}}$ table |
| `rem:vnatural-class-m` | `remark` | 2111 | The moonshine module: same $\kappa$, different class |
| `thm:ainfty-formality-depth` | `theorem` | 2145 | $A_\infty$ formality criterion |
| `thm:interacting-gram-positivity` | `theorem` | 2203 | Interacting Gram positivity |
| `cor:virasoro-interacting-gram` | `corollary` | 2243 | — |
| `thm:shadow-resonance-locus` | `theorem` | 2256 | — |
| `thm:shadow-spectral-measure` | `theorem` | 2294 | Shadow spectral measure |
| `prop:carleman-virasoro` | `proposition` | 2386 | Carleman rigidity |
| `prop:shadow-periods` | `proposition` | 2423 | Shadow amplitudes are periods |
| `prop:resurgent-orthogonality` | `proposition` | 2665 | Two orthogonal resurgent directions |
| `prop:universal-stokes-constants` | `proposition` | 2707 | Universal Stokes constants |
| `prop:gevrey-zero-degree` | `proposition` | 2739 | Gevrey-$0$ degree growth |
| `prop:padic-convergence` | `proposition` | 2797 | $p$-adic convergence radius |
| `rem:kummer-kubota-leopoldt` | `remark` | 2823 | Kummer congruences and the Kubota--Leopoldt $p$-adic $L$-function |
| `thm:shadow-mzv-dictionary` | `theorem` | 2928 | Shadow--MZV dictionary |
| `thm:drinfeld-associator-bar-transport` | `theorem` | 3008 | Drinfeld associator as bar transport |
| `thm:partition-modular-classification` | `theorem` | 3193 | Partition function modular classification |
| `prop:quasi-modular-propagator` | `proposition` | 3253 | Quasi-modular content from the genus-$1$ propagator |
| `prop:hecke-eigenvalue-extraction` | `proposition` | 3327 | Hecke eigenvalues from partition data |
| `prop:tau-large-primes` | `proposition` | 3366 | Ramanujan $\tau(p)$ at primes $83 \leq p \leq 113$ |
| `prop:tau-primes-211-229` | `proposition` | 3433 | Ramanujan $\tau(p)$ at primes $p\in\{211,223,227,229\}$ |
| `thm:spectral-curve` | `theorem` | 3505 | Algebraic shadow generating function |
| `prop:moment-matrix-negativity` | `proposition` | 3548 | Eisenstein moment minor |
| `prop:calogero-shadow-dictionary` | `proposition` | 3604 | Calogero--Moser / shadow tower dictionary |
| `rem:shadow-eisenstein-numerical-check` | `remark` | 3937 | Numerical check at $s = 0$ |
| `thm:shadow-higgs-field` | `theorem` | 4226 | Shadow Higgs field |
| `thm:general-nahc` | `theorem` | 4307 | General shadow triple |
| `rem:ode-im-shadow-identification` | `remark` | 4580 | ODE/IM correspondence as shadow projection |
| `prop:shadow-oper-rigid` | `proposition` | 4686 | Shadow oper as rigid hypergeometric |
| `prop:shadow-langlands-hierarchy` | `proposition` | 4773 | The $\cW_3$ shadow oper beyond Eisenstein |
| `thm:shadow-bps` | `theorem` | 4942 | The shadow obstruction tower as BPS spectrum |
| `thm:general-bps` | `theorem` | 5026 | General BPS spectrum of the shadow obstruction tower |
| `thm:sewing-shadow-intertwining` | `theorem` | 5126 | Sewing--shadow intertwining at genus~$1$ |
| `cor:spectral-measure-identification` | `corollary` | 5238 | Spectral measure identification |
| `thm:shadow-moduli-resolution` | `theorem` | 5292 | Shadow-moduli resolution |
| `thm:universality-of-G` | `theorem` | 5381 | Universality of $G$ |
| `prop:mc-bracket-determines-atoms` | `proposition` | 5449 | MC bracket determines spectral atoms |
| `rem:mc-ramanujan-bridge` | `remark` | 5499 | The bridge to the Ramanujan bound |
| `prop:koszul-field-criterion` | `proposition` | 5748 | Koszul field-preservation criterion |
| `prop:two-fixed-points` | `proposition` | 5823 | The two fixed points are unrelated |
| `prop:heisenberg-koszul-epstein` | `proposition` | 5989 | Degenerate case: Heisenberg |
| `comp:virasoro-c1-koszul-epstein` | `computation` | 6041 | Virasoro at $c = 1$: numerical Koszul--Epstein value |
| `comp:fe-minimal-models` | `computation` | 6066 | Functional equation for all unitary minimal models |
| `thm:spectral-continuation-bridge` | `theorem` | 6146 | Hecke-equivariant MC element |
| `thm:schur-complement-quartic` | `theorem` | 6361 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | 6420 | — |
| `prop:on-off-line-distinction` | `proposition` | 6497 | — |
| `prop:li-criterion-failure` | `proposition` | 6907 | Structural failure of the Li criterion for the sewing lift |
| `prop:pure-spin-s-schur` | `proposition` | 7057 | — |
| `prop:prime-side-defect-formula` | `proposition` | 7165 | — |
| `thm:finite-miura-defect` | `theorem` | 7235 | Finite Miura defect at genus one |
| `prop:modularity-constraint` | `proposition` | 7807 | Modularity constraint on the spectral measure |
| `prop:bracket-hodge-index` | `proposition` | 7850 | Bracket positivity and the Hodge index |
| `prop:lattice-ramanujan` | `proposition` | 7974 | Ramanujan bound for lattice spectral measures |
| `prop:shadow-symmetric-power` | `proposition` | 8016 | Shadow--symmetric power identification |
| `thm:petersson-identification` | `theorem` | 8160 | Petersson identification |
| `prop:modularity-constraint-atoms` | `proposition` | 8246 | Modularity constraint on atoms |
| `prop:rigidity-threshold` | `proposition` | 8283 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | 8381 | Lattice Ramanujan from rigidity |
| `prop:stieltjes-signed-universal` | `proposition` | 8577 | Universal signed Stieltjes measure |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | 8610 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | 8674 | Shadow arithmetic trichotomy |
| `prop:genus1-weight-bound` | `proposition` | 8749 | Weight bound for genus-$1$ shadow projections |
| `thm:mc-recursion-moment` | `theorem` | 8882 | MC recursion on moment $L$-functions |
| `prop:shadow-chiral-graph` | `proposition` | 8949 | Shadow amplitudes as chiral graph integrals |
| `thm:hecke-newton-lattice` | `theorem` | 9022 | Hecke--Newton closure for lattice VOAs |
| `thm:non-lattice-ramanujan` | `theorem` | 9114 | Non-lattice Ramanujan bound |
| `prop:mc-constraint-counting` | `proposition` | 9631 | MC constraint counting |
| `thm:route-c-propagation` | `theorem` | 9696 | Route~C: MC rigidity forces character-level prime-locality |
| `cor:route-c-standard-landscape` | `corollary` | 9819 | Route~C for the standard landscape |
| `thm:hecke-verdier-commutation` | `theorem` | 9858 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | 9897 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | 9972 | Theta decomposition bridge |
| `prop:newton-shadow-hecke` | `proposition` | 10035 | Newton--shadow--Hecke correspondence |
| `prop:sewing-spectral-bridge` | `proposition` | 10153 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | 10258 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | 10305 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | 10396 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | 10570 | Genus-one saddle triviality |
| `thm:scattering-coupling-factorization` | `theorem` | 10871 | Scattering coupling factorization |
| `thm:structural-separation` | `theorem` | 10954 | Structural separation of algebraic and arithmetic content |
| `prop:hecke-defect-equivalences` | `proposition` | 11080 | Equivalent characterizations; \textup{(i)--(iii)} ; \textup{(iv)} |
| `prop:hecke-defect-lattice` | `proposition` | 11131 | Hecke defect vanishes for lattice VOAs |
| `prop:hecke-defect-families` | `proposition` | 11206 | Hecke defect for standard families |
| `thm:rigidity-inheritance` | `theorem` | 11326 | Rigidity inheritance |
| `thm:packet-connection-flatness` | `theorem` | 11627 | Flatness and divisor independence |
| `prop:gauge-criterion-scattering` | `proposition` | 11760 | Gauge criterion for scattering access |
| `rem:arithmetic-comparison-sharpening` | `remark` | 11870 | Sharpening of the arithmetic comparison conjecture |
| `prop:miura-packet-splitting` | `proposition` | 11944 | — |
| `prop:genus2-non-diagonal` | `proposition` | 12310 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | 12354 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | 12559 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | 12591 | B\"ocherer bridge |
| `rem:genus2-definitive-scope` | `remark` | 12716 | Definitive scope of genus-$2$ arithmetic access |
| `rem:leech-all-sk` | `remark` | 12771 | Leech: all genus-$2$ cusp forms are Saito--Kurokawa lifts |
| `thm:leech-chi12-projection` | `theorem` | 12792 | Leech $\chi_{12}$-projection and Waldspurger consequence |
| `thm:prime-locality-obstructions` | `theorem` | 13124 | Precise obstructions to prime-locality; {} where indicated |
| `prop:shadow-not-selberg` | `proposition` | 13368 | The shadow zeta is not in the Selberg class |
| `thm:fricke-ldp-sub-leading` | `theorem` | 13740 | Fricke LDP sub-leading correction at each node |
| `thm:monster-lusztig-universal-ratio` | `theorem` | 13791 | Universal ratio $\ell_X/\ell_Y = c_+(L_X)/c_+(L_Y)$ pins $\ell_{\mathrm{Monster}} = 2$ |
| `thm:shimura-waldspurger-higher-weights` | `theorem` | 13851 | $C_k$ at weights $k + 1 \in \{5, 7, 9, 11\}$ |
| `thm:YD-delta-7-8-9` | `theorem` | 13911 | $\delta^{(n)}$ for $n \in \{7, 8, 9, 10, 11, 12\}$ |
| `prop:humbert-heegner-admissibility-filter` | `proposition` | 14085 | Humbert--Heegner admissibility filter; genus-$2$ bar--cobar scope |
| `thm:humbert-heegner-filter-g-geq-3` | `theorem` | 14212 | Humbert--Heegner filter at $g\ge 3$; saturation at codim $2g-1$ |
| `thm:mu-32-refinement` | `theorem` | 14501 | $\mu_{16}\to\mu_{32}$ gerbe refinement near the quadruple Humbert wall |
| `thm:super-quasi-hopf-plancherel-K-theoretic` | `theorem` | 14561 | $K$-theoretic Plancherel at super-quasi-Hopf level |
| `thm:monster-k3-lusztig-cplus-face` | `theorem` | 14636 | Monster--K$3$ Lusztig ratio equals $c_+$-ratio; Vol~I face of the Theorem~C $\mathsf B$-row ceiling |
| `thm:exact-pbw-u-zeta-8-truncation` | `theorem` | 14746 | Exact Lusztig small-quantum-group dimension on the height-$8$ K$3$-BKM truncation |
| `thm:YD-delta-13-16` | `theorem` | 14847 | $\delta^{(n)}$ for $n \in \{13, 14, 15, 16\}$ |
| `thm:grt-1-transitivity-delta5` | `theorem` | 14935 | GRT$_1$-transitivity on the $\Delta_5$ BKM; Vol~I face |
| `thm:n-2-root-unity-vol-I-face` | `theorem` | 15063 | $N = 2$ root-of-unity: $324$ and degenerate $S$; Vol~I face |

#### `chapters/connections/bv_brst.tex` (17)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:log-form-ghost-law` | `theorem` | 482 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 587 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 738 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `prop:koszul-brst-anomaly-preservation` | `proposition` | 780 | Koszul duality preserves BRST anomaly cancellation |
| `comp:v1-superstring-ghost-koszul` | `computation` | 863 | Superstring ghost/superghost Koszul dual |
| `thm:bar-semi-infinite-km` | `theorem` | 1015 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 1128 | Anomaly duality for Kac--Moody pairs |
| `cor:anomaly-duality-w` | `corollary` | 1291 | Curvature complementarity for principal \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |
| `thm:heisenberg-bv-bar-all-genera` | `theorem` | 1509 | BV $=$ bar for the Heisenberg at all genera |
| `prop:chain-level-three-obstructions` | `proposition` | 1756 | Three chain-level obstructions and harmonic factorization |
| `rem:bv-sewing-chain-level-classes` | `remark` | 1967 | BV sewing at the chain level: class-by-class status |
| `prop:harmonic-factorization` | `proposition` | 2017 | Harmonic factorization of higher bar differentials |
| `thm:bv-bar-coderived` | `theorem` | 2199 | BV$=$bar in the coderived category |
| `prop:wzw-brst-bar-genus0` | `proposition` | 2693 | Genus-\texorpdfstring{$0$}{0} WZW BRST complex from the affine bar complex |
| `thm:bvbrst-heegner-all-order` | `theorem` | 3288 | Heegner pattern for the all-order BV obstruction tower |
| `thm:bvbrst-nonperturbative-completion` | `theorem` | 4467 | Non-perturbative completion of the BV obstruction tower |
| `thm:bvbrst-allloop-resummation` | `theorem` | 4716 | All-loop Borcherds-product resummation of the BV obstruction tower |

#### `chapters/connections/concordance.tex` (17)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 679 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 693 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | 984 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 1008 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 1045 | Gaussian collapse for abelian input |
| `thm:operadic-complexity-concordance` | `theorem` | 2734 | Operadic complexity |
| `rem:kappa-polysemy` | `remark` | 5077 | The $\kappa$ polysemy |
| `thm:universal-MC` | `theorem` | 5715 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 6070 | Discriminant as spectral determinant, verified cases |
| `thm:discriminant-spectral` | `theorem` | 6115 | Spectral discriminant, general case |
| `comp:spectral-discriminants-standard` | `computation` | 6341 | Spectral discriminants of standard families |
| `thm:family-index` | `theorem` | 6406 | Family index theorem for genus expansions |
| `rem:c13-concordance-holographic` | `remark` | 7047 | The self-dual central charge $c = 13$ |
| `rem:programme-vi-verification` | `remark` | 7955 | Programme VI: systematic verification of (H1)--(H4) |
| `rem:four-test-interface` | `remark` | 8184 | The four-test interface |
| `prop:descent-fan` | `proposition` | 10300 | Descent fan structure |
| `rem:concord-shimura-waldspurger-bridge` | `remark` | 12750 | Shimura--Waldspurger bridge: constitutional conversion factor between Gritsenko and Borcherds Fourier tables |

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

#### `chapters/connections/entanglement_modular_koszul.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ent-scalar-entropy` | `theorem` | 160 | Entanglement entropy at the scalar level |
| `thm:entanglement-complementarity` | `theorem` | 235 | Entanglement complementarity |
| `prop:ent-complexity-classification` | `proposition` | 354 | Entanglement complexity classification |
| `thm:ent-landscape-census` | `theorem` | 569 | Standard landscape entanglement census |
| `thm:ent-btz-entropy` | `theorem` | 712 | BTZ entropy from the modular characteristic |
| `prop:ent-btz-complementarity` | `proposition` | 840 | BTZ complementarity |
| `rem:ent-negative` | `remark` | 1320 | Negative entanglement entropy at $c_{\mathrm{eff}} = -166$ |
| `prop:ent-real-root` | `proposition` | 1352 | Real-root unitary submodule entanglement |
| `thm:ent-topological-entanglement` | `theorem` | 1477 | Topological entanglement from non-semisimple total quantum dimension |
| `thm:ent-GSD-T2` | `theorem` | 1556 | Ground-state degeneracy on $T^2$ for the 3d bulk TQFT |

#### `chapters/connections/feynman_diagrams.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 196 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 301 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 346 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 373 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 413 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 431 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 452 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 499 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 558 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 915 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 947 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (55)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | 140 | Protected dual transform and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | 238 | Protected transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | 291 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | 332 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | 386 | Scalar fixed-point rigidity on a full scalar package and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | 500 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | 613 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | 731 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | 802 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | 934 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | 1014 | The first nonlinear holographic anomaly |
| `thm:yangian-shadow-theorem` | `theorem` | 1496 | Yangian-shadow theorem |
| `rem:frontier-hall-drinfeld-vs-yangian` | `remark` | 1553 | Frontier DNA: the Hall--Drinfeld double is not a Yangian; Manin-pair signature obstruction and Schiffmann--Vasserot shuffle |
| `thm:sphere-reconstruction` | `theorem` | 1634 | Sphere flatness and reconstruction on established comparison surfaces |
| `thm:gz26-commuting-differentials` | `theorem` | 1702 | GZ26 commuting differentials from the MC element |
| `thm:gaudin-yangian-identification` | `theorem` | 1808 | Gaudin--Yangian identification |
| `thm:yangian-sklyanin-quantization` | `theorem` | 1850 | Three-parameter identification of $\hbar$; {} on the new three-parameter identification; classical Sklyanin/Drinfeld content is |
| `thm:shadow-depth-operator-order` | `theorem` | 1905 | OPE pole order trichotomy for GZ\textup{26} Hamiltonians |
| `thm:kz-classical-quantum-bridge` | `theorem` | 1959 | Classical-to-quantum bridge: proved algebraic content |
| `thm:quartic-resonance-obstruction` | `theorem` | 2002 | Quartic resonance obstruction |
| `thm:collision-residue-twisting` | `theorem` | 2425 | Collision residue = universal twisting morphism |
| `thm:collision-depth-2-ybe` | `theorem` | 2481 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `thm:shadow-connection-kz` | `theorem` | 2519 | Shadow/KZ comparison on the affine Kac--Moody surface |
| `prop:shadow-connection-bpz` | `proposition` | 2584 | Shadow connection for Virasoro and BPZ on the degenerate-representation surface |
| `thm:quartic-obstruction-linf` | `theorem` | 2620 | Quartic obstruction = $L_\infty$ obstruction |
| `comp:holographic-ss-sl2` | `computation` | 2703 | The $E_1$ page for $\widehat{\mathfrak{sl}}_2$ |
| `comp:holographic-ss-vir` | `computation` | 2755 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | 2799 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | 2822 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | 2904 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | 2927 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | 2967 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | 3058 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | 3117 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | 3213 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | 3247 | Holographic datum for $\mathcal W_3$ |
| `thm:ds-central-charge-additivity` | `theorem` | 3371 | Central charge additivity under DS |
| `cor:critical-dimensions` | `corollary` | 3482 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | 3593 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | 3617 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | 3653 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | 3678 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | 3790 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | 3925 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | 4100 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | 4224 | Lifts as relative MC elements |
| `prop:frontier-celestial-ope` | `proposition` | 4637 | Celestial OPE from the bar complex |
| `prop:frontier-sw-shadow` | `proposition` | 4711 | Shadow connection and Picard--Fuchs |
| `prop:frontier-cs-shadow` | `proposition` | 4778 | Chern--Simons from the shadow obstruction tower |
| `thm:frontier-twisted-holography` | `theorem` | 4888 | Twisted holography datum |
| `thm:frontier-abjm` | `theorem` | 4978 | ABJM holographic datum |
| `thm:frontier-m5` | `theorem` | 5116 | M5 brane holographic datum |
| `prop:phantom-m5-koszul-dual` | `proposition` | 5248 | Phantom M5 Koszul dual |
| `rem:frontier-class-S-K3-parent` | `remark` | 5331 | Frontier DNA: 4d class-$\mathcal S$ $A_1$ on $\Sigma_{0,24}$ as the $\mathcal N{=}2$ parent of the K3-coupled M5 datum |
| `comp:burns-space-holographic-datum` | `computation` | 5523 | Burns space holographic modular Koszul datum |

#### `chapters/connections/genus1_seven_faces.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:g1sf-elliptic-regularization` | `theorem` | 164 | Elliptic regularization of the collision residue |
| `thm:g1sf-face-1` | `theorem` | 256 | Face~1 at genus~$1$: elliptic twisting morphism |
| `thm:g1sf-face-4` | `theorem` | 333 | Face~4 at genus~$1$: KZB connection |
| `thm:g1sf-face-5` | `theorem` | 471 | Face~5 at genus~$1$: elliptic $r$-matrix; {} \textup{(}identification with collision residue\textup{)}; {} \textup{(}classical elliptic $r$-matrix: Belavin 1981, Belavin--Drinfeld 1982\textup{)} |
| `lem:g1sf-casimir-bridge` | `lemma` | 570 | Casimir-convention bridge at genus~$1$ |
| `thm:g1sf-face-7` | `theorem` | 787 | Face~7 at genus~$1$: elliptic Gaudin Hamiltonians |
| `thm:g1sf-virasoro` | `theorem` | 896 | Virasoro genus-$1$ collision residue |
| `thm:g1sf-wn` | `theorem` | 963 | $\cW_N$ genus-$1$ collision residue |
| `thm:g1sf-master` | `theorem` | 1041 | Genus-$1$ seven-face identification for affine Kac--Moody |
| `thm:g1sf-degeneration` | `theorem` | 1159 | Degeneration to genus~$0$ |
| `thm:g1sf-b-cycle-monodromy` | `theorem` | 1322 | $B$-cycle monodromy of the collision residue |

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

#### `chapters/connections/grand_unification_platonic.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:grand-unification-platonic` | `theorem` | 99 | Grand Unification, chiral bar--cobar |
| `cor:gu-theorem-a-platonic` | `corollary` | 208 | Theorem~A is the adjunction itself |
| `cor:gu-theorem-b-platonic` | `corollary` | 225 | Theorem~B is Positselski localisation |
| `cor:gu-theorem-c-platonic` | `corollary` | 240 | Theorem~C is the scalar invariant of the double |
| `cor:gu-theorem-d-platonic` | `corollary` | 264 | Theorem~D is obstruction-tower universality |
| `cor:gu-theorem-h-platonic` | `corollary` | 281 | Theorem~H is Hochschild concentration |
| `cor:gu-L1-platonic` | `corollary` | 304 | L1 --- chain-level ensemble via genus-$g$ trace |
| `cor:gu-L3-platonic` | `corollary` | 369 | L3 --- $(\infty,1)$-categorical adjunction |
| `prop:L1-trace-identity-platonic` | `proposition` | 470 | L1 trace identity |
| `cor:programme-scale-platonic` | `corollary` | 575 | Three volumes, three lanes of the adjunction |
| `thm:pr-alpha-X-local-global` | `theorem` | 876 | Local-global gluing of $\mathrm{pr}_{\alpha_X}$ |

#### `chapters/connections/holographic_codes_koszul.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:hc-knill-laflamme` | `proposition` | 96 | Knill--Laflamme from Lagrangian isotropy |
| `thm:hc-symplectic-code` | `theorem` | 224 | Symplectic code structure |
| `thm:hc-koszulness-exact-qec` | `theorem` | 344 | \textbf{G12}: Koszulness $\Leftrightarrow$ exact holographic reconstruction |
| `thm:hc-shadow-redundancy` | `theorem` | 463 | Shadow depth controls redundancy |
| `prop:hc-dictionary` | `proposition` | 564 | 12-fold dictionary |
| `thm:hc-census` | `theorem` | 719 | Standard landscape code census |

#### `chapters/connections/holographic_datum_master.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:hdm-face-1` | `theorem` | 324 | Face~1: bar-cobar twisting |
| `thm:hdm-face-2` | `theorem` | 381 | Face~2: DNP line operators; \ (identification with collision residue); \ (DNP line-operator package: Dimofte--Niu--Py 2025; Vol.~II cross-volume matching) |
| `thm:hdm-face-3` | `theorem` | 464 | Face~3: Khan--Zeng PVA \textup{(}genus~$0$ only\textup{)} |
| `thm:hdm-face-4` | `theorem` | 537 | Face~4: GZ26 commuting Hamiltonians |
| `thm:hdm-face-5` | `theorem` | 627 | Face~5: Drinfeld $r$-matrix; \ (identification with collision residue); \ (classical $r$-matrix theory: Drinfeld 1985) |
| `thm:hdm-face-6` | `theorem` | 758 | Face~6: Sklyanin bracket; \ (identification with classical limit of collision residue); \ (Sklyanin bracket: Semenov-Tian-Shansky 1983) |
| `thm:hdm-face-7` | `theorem` | 836 | Face~7: Gaudin Hamiltonians |
| `thm:hdm-seven-way-master` | `theorem` | 913 | Seven-way master theorem |
| `prop:hdm-averaging-compatibility` | `proposition` | 1002 | Averaging compatibility of the seven faces |
| `thm:hdm-grt-cocycle-ledger` | `theorem` | 1277 | Vol~I face-cocycle ledger; degree-$2$ collapse |
| `prop:hdm-upgrade-theta` | `proposition` | 1669 | Upgrade~(U1): existence and universality of $\Theta_\cA$ |
| `prop:hdm-upgrade-rectification` | `proposition` | 1705 | Upgrade~(U2): strict Verdier/Koszul rectification |
| `prop:hdm-upgrade-bulk-slot` | `proposition` | 1735 | Upgrade~(U3): the bulk slot is the derived chiral centre, with line-side comparison on named lanes |
| `thm:hdm-u-a-universal-property` | `theorem` | 1889 | Universal property of $U_\cA$ |
| `cor:hdm-u-a-six-projections` | `corollary` | 1964 | Six projections as forgetful functors |
| `prop:hdm-four-recovery-directions` | `proposition` | 2065 | Four recovery directions with precise scope |
| `thm:hdm-u-a-drinfeld-center` | `theorem` | 2253 | $U_\cA$ as Drinfeld $\infty$-centre, on and off locus |
| `cor:hdm-u-a-drinfeld-center-flagships` | `corollary` | 2393 | Flagship verifications of the Drinfeld-centre identification |
| `thm:hdm-u-a-final-object` | `theorem` | 2612 | Final-object characterisation of $U_\cA$ |
| `thm:hdm-matched-pair-canonicity` | `theorem` | 2749 | Koszul canonicity of the matched-pair actions |
| `cor:hdm-u-a-bondal-reconstruction` | `corollary` | 2939 | Bondal reconstruction from finality |
| `thm:hdm-five-recovery-functors` | `theorem` | 3064 | Five recovery functors out of $U_\cA$ |
| `thm:hdm-hexagon` | `theorem` | 3186 | Compatibility hexagon of the six projections |
| `thm:hdm-koszul-loss-classes` | `theorem` | 3263 | Koszul-loss classes of $P_{\cA^!}$ and $P_\cC$ |
| `lem:hdm-koszul-loss-kunneth` | `lemma` | 3381 | Tensor-product K\"unneth law for the Koszul-loss classes |
| `thm:hdm-class-m-infty-fibre` | `theorem` | 3561 | Class-$\mathsf M_\infty$ fibre |
| `rem:hdm-minfty-free-field-points` | `remark` | 3672 | Free-boson $c=1$ and free-fermion $c=-2$ realisations |
| `rem:hdm-m-vs-minfty` | `remark` | 3709 | Class-$\mathsf M_\infty$ vs class-$\mathsf M$ fibre |
| `thm:hdm-m-infty-tensor-kunneth` | `theorem` | 3732 | Tensor-product K\"unneth for the $\mathsf M_\infty$ tower |
| `thm:hdm-m-infty-nfold-kunneth` | `theorem` | 3937 | $n$-fold tensor K\"unneth and Kirchhoff law for the $\mathsf M_\infty$ tower |
| `thm:hdm-higher-gaudin` | `theorem` | 4227 | Higher Gaudin Hamiltonians |
| `thm:hdm-triangle-composite` | `theorem` | 4709 | Cross-volume composite triangle on the boundary-linear $\Phi_d$-image |

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

#### `chapters/connections/thqg_open_closed_realization.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:bd-algebraic-bridge` | `proposition` | 111 | Bridge: BD chiral operad $\leftrightarrow$ algebraic $\mathcal{E}\!\mathit{nd}^{\mathrm{ch}}$ |
| `thm:thqg-brace-dg-algebra` | `theorem` | 249 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | 467 | Universal open/closed pair (chiral Swiss-cheese theorem) |
| `prop:mixed-sector-bulk-boundary` | `proposition` | 550 | Mixed sector encodes bulk-to-boundary module structure |
| `thm:thqg-local-global-bridge` | `theorem` | 618 | Local-global bridge |
| `thm:thqg-annulus-trace` | `theorem` | 719 | Annulus trace theorem |
| `prop:thqg-annulus-degeneration-kappa` | `proposition` | 996 | Annulus degeneration and the genus-$1$ curvature |
| `thm:thqg-oc-mc-equation` | `theorem` | 1073 | Open/closed MC equation |
| `thm:thqg-oc-projection` | `theorem` | 1134 | Open/closed projection principle |
| `thm:thqg-mc-forced-consistency` | `theorem` | 1193 | MC-forced open-closed consistency |
| `thm:thqg-oc-quartic-vanishing` | `theorem` | 1517 | Vanishing and nonvanishing of $\mathfrak{R}^{\mathrm{oc}}_{4}$ |
| `prop:thqg-occ-CD-ANm1-24` | `proposition` | 1864 | Chacaltana--Distler central charges for $\mathcal T[A_{N-1}, \Sigma_{0,24} |

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
| `prop:virasoro-pade` | `proposition` | 990 | Pad\'e matching for the Virasoro bar sequence |

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
| `thm:q-convention-bridge-main` | `theorem` | 81 | Q-convention bridge |
| `thm:q-bridge-cocycle` | `theorem` | 285 | Q-bridge as Z/2-cover cocycle |

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
