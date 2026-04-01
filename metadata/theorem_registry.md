# Theorem Registry

Auto-generated on 2026-04-01 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2376 |
| Total tagged claims | 3068 |
| Active files in `main.tex` | 84 |
| Total `.tex` files scanned | 109 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2376 |
| `ProvedElsewhere` | 411 |
| `Conjectured` | 207 |
| `Conditional` | 34 |
| `Heuristic` | 37 |
| `Open` | 3 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 1007 |
| `proposition` | 785 |
| `corollary` | 367 |
| `lemma` | 118 |
| `computation` | 88 |
| `remark` | 6 |
| `calculation` | 3 |
| `maintheorem` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 15 |
| Part I: Theory | 864 |
| Part II: Examples | 586 |
| Part III: Connections | 626 |
| Appendices | 285 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus_modular_koszul.tex` | 192 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 112 |
| `chapters/connections/arithmetic_shadows.tex` | 105 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 90 |
| `chapters/theory/higher_genus_complementarity.tex` | 79 |
| `appendices/nonlinear_modular_shadows.tex` | 75 |
| `chapters/examples/free_fields.tex` | 67 |
| `chapters/examples/w_algebras.tex` | 66 |
| `chapters/theory/higher_genus_foundations.tex` | 63 |
| `chapters/examples/kac_moody.tex` | 52 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 52 |
| `chapters/theory/chiral_modules.tex` | 49 |
| `chapters/connections/thqg_gravitational_s_duality.tex` | 46 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 42 |
| `chapters/examples/yangians_computations.tex` | 42 |
| `chapters/examples/yangians_foundations.tex` | 42 |
| `chapters/connections/thqg_gravitational_complexity.tex` | 39 |
| `chapters/theory/configuration_spaces.tex` | 39 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 38 |
| `chapters/theory/chiral_koszul_pairs.tex` | 37 |

## Complete Proved Registry

### Frame (15)

#### `chapters/frame/heisenberg_frame.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 490 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 847 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 942 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1148 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1372 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1394 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1557 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1741 | Quantum complementarity for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2377 | $\mathfrak{sl}_2$ bar complex as Swiss-cheese coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2449 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2498 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2581 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 2619 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 2887 | CS $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | 3620 | The Heisenberg center |

### Part I: Theory (864)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 1015 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 1412 | Geometric realization |
| `prop:orthogonal` | `proposition` | 1549 | Orthogonality |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (112)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:curvature-central` | `theorem` | 186 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 291 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 439 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 508 | Conilpotency ensures convergence |
| `lem:arity-cutoff` | `lemma` | 758 | Arity cutoff: finite MC equation at each stage |
| `thm:completed-bar-cobar-strong` | `theorem` | 777 | MC element lifts to the completed convolution algebra |
| `prop:standard-strong-filtration` | `proposition` | 924 | Strong filtration for the standard landscape |
| `prop:mc4-reduction-principle` | `proposition` | 1007 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 1072 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 1109 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 1147 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 1196 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 1247 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 1310 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 1374 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 1410 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 1486 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 1583 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 1599 | Factorization-envelope criterion for principal stages |
| `cor:completion-closure-equivalence` | `corollary` | 1635 | Homotopy-categorical equivalence on the completion closure |
| `thm:coefficient-stability-criterion` | `theorem` | 1689 | Coefficient-stability criterion |
| `thm:completed-twisting-representability` | `theorem` | 1724 | Completed twisting representability |
| `thm:mc-twisting-closure` | `theorem` | 1747 | MC-twisting closure of the completion closure |
| `thm:uniform-pbw-bridge` | `theorem` | 1772 | Uniform PBW bridge from MC1 to MC4 |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 1878 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 1924 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 1959 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 1979 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 1997 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 2016 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 2058 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 2098 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 2139 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 2206 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 2248 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 2294 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 2356 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 2397 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 2469 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 2556 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 2582 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 2607 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 2661 | Stage-\texorpdfstring{$4$}{4} reduction to one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 2689 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 2726 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 2757 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 2799 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 2826 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 2856 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 2899 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 2934 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 2964 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 2981 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 3032 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 3093 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
| `cor:winfty-dual-candidate-construction` | `corollary` | 3132 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 3179 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} reduction on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 3218 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 3310 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 3341 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 3449 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 3497 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 3543 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 3570 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 3712 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 3749 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 3813 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 3868 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 3910 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 4004 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 4029 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 4068 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 4088 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 4126 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 4143 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 4166 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 4188 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 4204 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 4214 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 4230 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 4242 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 4255 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 4273 | Stage-\texorpdfstring{$5$}{5} mixed transport reduction to one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 4296 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 4327 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 4534 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 4552 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 4589 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 4626 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-network-collapse` | `corollary` | 4922 | Visible stage-\texorpdfstring{$5$}{5} local network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 4970 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 5194 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 5467 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 5808 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 5844 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 5905 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 5917 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 6025 | Bar complex as algebra over the modular operad |
| `cor:genus-expansion-converges` | `corollary` | 6317 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 6377 | Functoriality of bar construction |
| `thm:reconstruction-vs-duality` | `theorem` | 6486 | Reconstruction versus duality |
| `thm:recognition-koszul-pairs` | `theorem` | 6548 | Recognition theorem for finite chiral Koszul pairs |
| `thm:mixed-boundary-sseq` | `theorem` | 6603 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | 6627 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | 6675 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | 6704 | Universality |
| `prop:sugawara-contraction` | `proposition` | 6712 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | 6777 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | 6793 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | 6839 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | 6888 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | 6932 | Diagonal GKO transgression |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (52)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 433 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 654 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 973 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 1090 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1163 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1207 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1275 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1341 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1481 | Positselski equivalence for the chiral bar coalgebra |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1538 | Flat finite-type reduction on the completed-dual side |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1636 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 1805 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 1821 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 1875 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 1898 | Genus-graded convergence |
| `prop:counit-qi` | `proposition` | 2019 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 2031 | Functoriality of bar-cobar inversion |
| `lem:complete-filtered-comparison` | `lemma` | 2115 | Complete filtered comparison lemma |
| `cor:completed-derived-equivalence` | `corollary` | 2216 | Completed derived equivalence |
| `thm:barr-beck-lurie-koszulness` | `theorem` | 2328 | Barr--Beck--Lurie characterization of chiral Koszulness |
| `thm:fh-concentration-koszulness` | `theorem` | 2413 | Factorization homology concentration |
| `thm:fm-boundary-acyclicity` | `theorem` | 2473 | FM boundary acyclicity |
| `prop:lagrangian-perfectness` | `proposition` | 2664 | Perfectness for the standard landscape |
| `cor:lagrangian-unconditional` | `corollary` | 2800 | Unconditional Lagrangian criterion for the standard landscape |
| `prop:bar-fh` | `proposition` | 3118 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 3196 | Cobar as factorization cohomology |
| `prop:subexponential-growth-automatic` | `proposition` | 3744 | Sub-exponential growth is automatic |
| `thm:ks-centrality` | `theorem` | 3964 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | 4007 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | 4058 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | 4093 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | 4139 | Quadratic frontier |
| `prop:eta-hessian-transfer` | `proposition` | 4233 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | 4269 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | 4313 | Admissible cyclic rigidity |
| `cor:ds-not-first-frontier` | `corollary` | 4348 | Drinfeld--Sokolov reductions remain one-channel in the semisimple admissible sector |
| `thm:classification-scalar-genera` | `theorem` | 4393 | Classification of scalar genera |
| `thm:platonic-hierarchy-log` | `theorem` | 4463 | Five-step hierarchy of the categorical logarithm |
| `prop:cech-two-element-strict` | `proposition` | 4978 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | 5306 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | 5366 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | 5398 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | 5420 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | 5518 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | 5566 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | 5586 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | 5631 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | 5662 | Repeated roots encode extension data |
| `thm:common-core-exact-sequences-inv` | `theorem` | 5694 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | 5722 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | 5789 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | 5811 | Explicit coprime-locus projectors |

#### `chapters/theory/bar_construction.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 266 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 655 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 745 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 927 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 993 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 1021 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 1116 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 1158 | Arnold relations |
| `comp:deg0` | `computation` | 1201 | Degree 0 |
| `comp:deg1-general` | `computation` | 1219 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1341 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1380 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1386 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1418 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1441 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1508 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1559 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1576 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1663 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1689 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1713 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1777 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1852 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1924 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 2034 | Bar complex is chiral |

#### `chapters/theory/chiral_center_theorem.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:partial-comp-assoc` | `lemma` | 191 | Associativity of partial compositions |
| `prop:pre-lie-chiral` | `proposition` | 496 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | 524 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | 545 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | 1228 | Chiral Deligne--Tamarkin |

#### `chapters/theory/chiral_hochschild_koszul.tex` (38)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 189 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 340 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 378 | Hochschild spectral sequence |
| `lem:hochschild-shift-computation` | `lemma` | 496 | Hochschild duality shift |
| `thm:main-koszul-hoch` | `theorem` | 557 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `thm:hochschild-polynomial-growth` | `theorem` | 668 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 767 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `prop:e2-formality-hochschild` | `proposition` | 808 | $\Etwo$-formality of chiral Hochschild cohomology |
| `thm:convolution-formality-one-channel` | `theorem` | 888 | Scalar universal class implies convolution formality along its distinguished orbit |
| `thm:bifunctor-obstruction-decomposition` | `theorem` | 1087 | Bifunctor obstruction decomposition |
| `comp:boson-hochschild` | `computation` | 1303 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 1333 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 1438 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 1532 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 1630 | Kac--Moody cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | 1836 | Genus truncation |
| `prop:hochschild-shadow-projection` | `proposition` | 1909 | Hochschild as arity-$2$ shadow projection |
| `thm:mc2-1-km` | `theorem` | 1938 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 2055 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 2303 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 2389 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 2508 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | 2690 | Strictification principle for modular deformation theory |
| `prop:d-mod-squared-zero` | `proposition` | 2827 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2963 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 3138 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 3328 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 3455 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 3705 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 3860 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 3999 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 4084 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 4131 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 4429 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 4560 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 4607 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 4805 | $bc$/$\beta\gamma$ Koszul duality |
| `prop:hochschild-cech-ss` | `proposition` | 5007 | Hochschild--\v{C}ech spectral sequence |

#### `chapters/theory/chiral_koszul_pairs.tex` (37)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 241 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 268 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 288 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 316 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 391 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 653 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 731 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 786 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 830 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 977 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1081 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1115 | Converse: formality implies chiral Koszulness |
| `conj:ext-diagonal-vanishing` | `theorem` | 1185 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1223 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1249 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1273 | Kac--Shapovalov criterion for simple quotients |
| `prop:li-bar-poisson-differential` | `proposition` | 1452 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | 1523 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | 1625 | Nilradical obstruction at degenerate admissible levels |
| `thm:koszul-equivalences-meta` | `theorem` | 1759 | Equivalences of chiral Koszulness |
| `prop:koszulness-formality-equivalence` | `proposition` | 2202 | Koszulness as formality of the convolution algebra |
| `prop:cumulant-window-inversion` | `proposition` | 2443 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 2499 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 2676 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 2736 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 2890 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 2984 | Bar computes Koszul dual, complete statement |
| `lem:completion-convergence` | `lemma` | 3072 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 3121 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 3680 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 3898 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:e1-module-koszul-duality` | `theorem` | 3985 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 4121 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 4163 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 4217 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 4252 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 4450 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 186 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 291 | Module bar-comodule comparison on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `thm:monoidal-module-koszul` | `theorem` | 350 | Lax monoidal structure of the module bar functor |
| `prop:ext-tor-exchange` | `proposition` | 469 | Derived Ext exchange on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `prop:conformal-blocks-bar` | `proposition` | 548 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 652 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 745 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 803 | KZB connection from the bar complex |
| `prop:tilting-bar` | `proposition` | 1648 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1711 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1911 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1969 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 2003 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:logarithmic-bar` | `proposition` | 2241 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2335 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2448 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2483 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2522 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2539 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2579 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2601 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2751 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2863 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2977 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3056 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3210 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3241 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3284 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3374 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3460 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3519 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3595 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3672 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3722 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3815 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3869 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3935` | `calculation` | 3935 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3962` | `calculation` | 3962 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3993` | `calculation` | 3993 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4111 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4236 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4286 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4410 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4452 | \texorpdfstring{$\mathcal{W}$}{W}-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4507 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4549 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4679 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4828 | Fusion product compatibility on the module bar surface |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4949 | Heisenberg fusion splitting |

#### `chapters/theory/cobar_construction.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 249 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 310 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 343 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 425 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 501 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 615 | Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 871 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 1031 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1249 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1380 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1432 | Explicit cobar-bar augmentation |
| `prop:cobar-modular-shadow` | `proposition` | 1704 | Cobar as modular shadow carrier |
| `thm:cobar-cech` | `theorem` | 1716 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1764 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1785 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1875 | Topology |
| `thm:poincare-verdier` | `theorem` | 1934 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 2024 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 2049 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 2095 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 2249 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2345 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2486 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2511 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2608 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2661 | Recognition principle |
| `lem:deformation-space` | `lemma` | 3055 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 3097 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 3145 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3224 | Curved differential formula |

#### `chapters/theory/computational_methods.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:comp-algebraic-shadow` | `theorem` | 101 | Riccati algebraicity |
| `thm:comp-denom-pattern` | `theorem` | 177 | Denominator theorem |
| `prop:comp-shadow-connection-properties` | `proposition` | 227 | Properties of the shadow connection |
| `thm:comp-shadow-asymptotics` | `theorem` | 354 | Shadow asymptotics |
| `prop:comp-borel-summability` | `proposition` | 453 | Borel summability |
| `prop:comp-mc-recursion` | `proposition` | 503 | MC recursion |
| `thm:comp-alg-rec-equivalence` | `theorem` | 532 | Algebraic--recursive equivalence |
| `thm:comp-ds-consistency` | `theorem` | 599 | DS transfer consistency |
| `prop:comp-ce-bar` | `proposition` | 677 | CE reduction |
| `thm:comp-zhu-c-dependence` | `theorem` | 700 | $c$-dependence for simple quotients |
| `thm:comp-three-way-bar` | `theorem` | 780 | Three-way agreement for bar cohomology |
| `prop:comp-explicit-theta-sl2` | `proposition` | 804 | Explicit $\Theta$ for $\AffKM{sl}_2$ |
| `thm:comp-e8-three-way` | `theorem` | 933 | $E_8$ genus-$2$ agreement |
| `prop:comp-n2-kappa` | `proposition` | 1055 | Modular characteristic |
| `prop:comp-n2-spectral-flow` | `proposition` | 1113 | Spectral flow invariance |
| `thm:comp-genus2-cross` | `theorem` | 1152 | Cross-consistency at genus~$2$ |

#### `chapters/theory/configuration_spaces.tex` (39)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 299 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 409 | Normal crossings |
| `thm:closure-relations` | `theorem` | 504 | Closure relations |
| `thm:log-complex` | `theorem` | 617 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 656 | Arnold relations |
| `prop:twisting-morphism-propagator` | `proposition` | 737 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 804 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 871 | Residue operations |
| `prop:residue-local` | `proposition` | 926 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 975 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1221 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1288 | Conformal blocks from punctured bar complex |
| `thm:bordered-fm-properties` | `theorem` | 1706 | Properties of the bordered FM compactification |
| `prop:four-type-boundary` | `proposition` | 1805 | Four-type boundary decomposition |
| `thm:oc-convolution-dg-lie` | `theorem` | 2200 | dg~Lie structure on the open-closed convolution algebra |
| `thm:modular-mc-clutching` | `theorem` | 2448 | Modular MC equation with clutching |
| `cor:recovery-bar-intrinsic` | `corollary` | 2794 | Recovery of the bar-intrinsic MC element |
| `prop:eta` | `proposition` | 2962 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `lem:orientation-compatibility` | `lemma` | 3369 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 3475 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 3517 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 3544 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 3566 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 3606 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 3630 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 3665 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 3687 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 3721 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 3737 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 3759 | Nilpotency from Arnold relations |
| `thm:arnold-jacobi` | `theorem` | 3890 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 3943 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 3989 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 4021 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 4066 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 4297 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 4367 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 4504 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:4714` | `computation` | 4714 | Explicit examples |

#### `chapters/theory/derived_langlands.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:langlands-bar-bridge` | `theorem` | 94 | Critical bar-to-oper bridge |
| `thm:oper-bar-h0-dl` | `theorem` | 318 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 353 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 377 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 414 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 495 | Differential analysis at arity 3 |
| `prop:d4-nonvanishing` | `proposition` | 575 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 634 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 647 | Full oper differential-form identification |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 987 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/e1_modular_koszul.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | 123 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | 142 | — |
| `rem:e1-mc-element` | `theorem` | 194 | $E_1$ Maurer--Cartan element |
| `prop:e1-shadow-r-matrix` | `proposition` | 227 | — |
| `thm:e1-mc-finite-arity` | `theorem` | 310 | $E_1$ MC equation at finite arity |
| `thm:e1-coinvariant-shadow` | `theorem` | 380 | Coinvariant projection: $E_1$ shadows to $E_\infty$ shadows |
| `thm:e1-theorem-A-modular` | `theorem` | 704 | Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction |
| `thm:e1-theorem-B-modular` | `theorem` | 757 | Theorem~$\mathrm{B}^{E_1}$ at all genera: ordered bar--cobar inversion |
| `thm:e1-theorem-C-modular` | `theorem` | 782 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
| `thm:e1-theorem-D-modular` | `theorem` | 814 | Theorem~$\mathrm{D}^{E_1}$ at all genera: formal ordered arity-$2$ shadow series |
| `thm:e1-theorem-H-modular` | `theorem` | 884 | Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered Hochschild at genus~$g$ |
| `lem:bare-graph-no-thooft` | `lemma` | 1012 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | 1033 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | 1075 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | 1097 | Exact $N^{\chi}$ weighting from traced open color |

#### `chapters/theory/en_koszul_duality.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:en-chiral-bridge` | `theorem` | 48 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
| `prop:en-formality-mc-truncation` | `proposition` | 121 | Formality hierarchy as MC obstruction truncation |
| `prop:linking-sphere-residue` | `proposition` | 399 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 474 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 634 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 692 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |
| `thm:bar-swiss-cheese` | `theorem` | 1004 | Bar complex as Swiss-cheese coalgebra |
| `prop:operadic-center-existence` | `proposition` | 1233 | Existence of the operadic center |
| `thm:operadic-center-hochschild` | `theorem` | 1286 | The operadic center of $\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex |
| `thm:center-geometric-inevitability` | `theorem` | 1608 | Geometric inevitability of the chiral center |
| `prop:braces-from-center` | `proposition` | 1801 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | 1850 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | 1926 | Terminality of the center |
| `cor:center-functor` | `corollary` | 2014 | The center functor |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 27 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 170 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 58 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 115 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 224 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 270 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 319 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 348 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 410 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 437 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 494 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 552 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 632 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 802 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 823 | — |
| `thm:fourier-specialization` | `theorem` | 858 | Specialization |
| `rem:fourier-genus-preview` | `remark` | 1013 | Ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus_complementarity.tex` (79)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:involution-splitting` | `lemma` | 196 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 251 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 325 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 423 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 608 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 663 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 748 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 811 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 862 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 1007 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 1080 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 1120 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 1174 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1203 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 1391 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 1426 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 1478 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 1591 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 1622 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 1642 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 1747 | Verdier pairing and Lagrangian eigenspaces |
| `prop:ptvv-lagrangian` | `proposition` | 1964 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 2037 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 2138 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 2166 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 2203 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 2246 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 2282 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 2313 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 2554 | Fermion-boson Koszul duality |
| `prop:complementarity-landscape` | `proposition` | 2739 | Complementarity landscape |
| `thm:BD-genus-zero` | `theorem` | 2954 | BD 3.4.12: genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 3004 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 3017 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 3059 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 3118 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 3158 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 3186 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 3208 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 3252 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 3441 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 3489 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 3577 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 3604 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 3632 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 3666 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 3691 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 3752 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 3798 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 3837 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 3866 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 3890 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 3915 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 3947 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 3996 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 4022 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 4038 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 4143 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 4221 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 4269 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 4358 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | 4533 | Ambient complementarity in tangent form |
| `thm:ambient-complementarity-fmp` | `theorem` | 4576 | Ambient complementarity as shifted symplectic formal moduli problem |
| `thm:shifted-cotangent-normal-form` | `theorem` | 4834 | Shifted cotangent normal form |
| `prop:legendre-duality-potentials` | `proposition` | 4883 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | 4898 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | 4928 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | 4952 | Criterion for fake complementarity |
| `thm:holo-comp-bulk-reconstruction` | `theorem` | 5148 | Protected dual transform |
| `thm:holo-comp-cotangent-realization` | `theorem` | 5198 | Shifted cotangent realization |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | 5225 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | 5311 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | 5355 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | 5432 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | 5515 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | 5584 | First nonlinear holographic anomaly |
| `thm:critical-dimension` | `theorem` | 5689 | Critical dimension |
| `prop:non-critical-liouville` | `proposition` | 5854 | Non-critical complementarity and the Liouville sector |
| `cor:complementarity-discriminant-cancellation` | `corollary` | 5899 | Arity-$4$ discriminant cancellation |

#### `chapters/theory/higher_genus_foundations.tex` (63)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:gauss-manin-uncurving-chain` | `proposition` | 317 | Gauss--Manin uncurving at chain level |
| `prop:genus-g-curvature-package` | `proposition` | 487 | The genus-$g$ curvature package |
| `prop:chain-level-curvature-operator` | `proposition` | 603 | Chain-level curvature operator |
| `prop:genus-g-mc-element` | `proposition` | 729 | Genus-$g$ MC element |
| `thm:bar-ainfty-complete` | `theorem` | 920 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 1020 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 1111 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 1224 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 1331 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 1478 | Verdier duality of operations |
| `thm:bar-curved-ch-infty` | `theorem` | 1640 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
| `thm:convergence-filtered` | `theorem` | 1718 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1927 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1961 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1995 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 2015 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 2031 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2333 | Bar-cobar isomorphism, retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 2418 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2633 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 3239 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 3442 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 3502 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 3755 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:genus1-d-squared` | `theorem` | 3849 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 3906 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 4174 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 4207 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 4334 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 4437 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 4491 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 4569 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 4686 | \texorpdfstring{$W_3$}{W3} fiberwise obstruction |
| `comp:w3-obs-explicit` | `computation` | 4737 | Explicit genus-$1$ value of the $W_3$ obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 4758 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 4787 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 4873 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4974 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 5231 | Multi-generator edge universality |
| `prop:f2-quartic-dependence` | `proposition` | 5271 | Genus-$2$ quartic dependence |
| `cor:anomaly-ratio` | `corollary` | 5326 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 5342 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 5367 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 5385 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 5408 | Universal genus-$1$ criticality criterion; scalar-lane collapse |
| `cor:tautological-class-map` | `corollary` | 5441 | Tautological class map on the scalar lane; universal genus-$1$ class |
| `prop:bar-tautological-filtration` | `proposition` | 5558 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 5630 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 5660 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 5758 | Scalar obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 5825 | Grothendieck--Riemann--Roch bridge on the proved uniform-weight scalar lane |
| `lem:stable-graph-d-squared` | `lemma` | 5998 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 6060 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 6098 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 6140 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 6229 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 6317 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 6386 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 6420 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 6461 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 6518 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 6546 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 6596 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (192)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:mcg-equivariance-tower` | `proposition` | 155 | MCG-equivariance of the genus tower |
| `thm:genus-graded-koszul` | `theorem` | 243 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 274 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 608 | Free-field examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 653 | Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 695 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 831 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 1098 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 1123 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1320 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1372 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1472 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1522 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1584 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:pbw-propagation` | `theorem` | 1760 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | 1920 | Locality of the collision differential |
| `thm:three-tier-architecture` | `theorem` | 2007 | Three-tier logical architecture of modular Koszul duality |
| `lem:e2-higher-genus` | `lemma` | 2273 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 2423 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 2534 | Modular characteristic |
| `cor:free-energy-ahat-genus` | `corollary` | 2672 | Scalar free energy as $\hat{A}$-genus |
| `thm:spectral-characteristic` | `theorem` | 2755 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 2788 | Universal modular Maurer--Cartan class |
| `prop:curvature-centrality-general` | `proposition` | 2923 | Centrality of higher-genus curvature |
| `thm:mc2-bar-intrinsic` | `theorem` | 2971 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 3373 | Shadow extraction |
| `prop:mc2-functoriality` | `proposition` | 3488 | Functoriality of the bar-intrinsic MC element |
| `thm:bipartite-linfty-tree` | `theorem` | 3591 | Bipartite shadow as $L_\infty$ tree-level structure |
| `thm:explicit-theta` | `theorem` | 3717 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 3936 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 4350 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 4429 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 4542 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 4576 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 4608 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 4809 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 4885 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 4950 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 5085 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 5182 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 5293 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 5430 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 5582 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 5756 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 5906 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 6100 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 6220 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 6319 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 6409 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 6521 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 6593 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 6675 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 6753 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 6830 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 6906 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 6981 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 7047 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 7127 | MC2 completion under explicit hypotheses |
| `thm:mc2-full-resolution` | `theorem` | 7213 | MC2 comparison completion on the proved scalar lane |
| `lem:mk67-from-mc2` | `lemma` | 7266 | Bar-intrinsic MC2 identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 7309 | One-channel line concentration of the minimal MC class |
| `thm:km-strictification` | `theorem` | 7380 | KM strictification of the universal class |
| `prop:w-algebra-scalar-saturation` | `proposition` | 7468 | One-channel line concentration for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 7515 | One-dimensional cyclic line persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 7576 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 7726 | One-channel line concentration for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 7829 | Cyclic rigidity and level-direction concentration |
| `prop:saturation-functorial` | `proposition` | 8020 | Functorial behavior of one-channel line concentration |
| `cor:effective-quadruple` | `corollary` | 8187 | Effective \texorpdfstring{$\Gamma$}{Gamma}-quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 8278 | Cyclic rigidity at generic level |
| `thm:algebraic-family-rigidity` | `theorem` | 8447 | Algebraic-family rigidity |
| `cor:saturation-algebraic-families` | `corollary` | 8559 | Level-direction concentration at all non-critical levels for algebraic families |
| `thm:conformal-bootstrap-rigidity` | `theorem` | 8628 | $L_0$-bootstrap rigidity |
| `cor:one-channel-no-lie` | `corollary` | 8735 | One-channel criterion without Lie symmetry |
| `thm:tautological-line-support` | `theorem` | 8993 | Tautological line support from genus universality |
| `cor:mc2-single-hypothesis` | `corollary` | 9105 | MC2 comparison gauntlet collapses on the proved scalar lane |
| `thm:convolution-dg-lie-structure` | `theorem` | 9295 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 9537 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 9987 | Modular homotopy convolution |
| `prop:modular-homotopy-type-structure` | `proposition` | 10071 | Structure of the modular homotopy type |
| `cor:strictification-comparison` | `corollary` | 10118 | Strictification comparison |
| `cor:vol1-theta-log-fm-twisting-data` | `corollary` | 10494 | $\Theta_\cA$ as universal modular twisting morphism |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | 10748 | First two weights |
| `comp:vol1-low-genus-log-fm-chart` | `computation` | 10823 | Low-genus amplitudes |
| `lem:shadow-bracket-well-defined` | `lemma` | 11435 | Well-definedness of the descended bracket |
| `prop:shadow-algebra-linfty` | `proposition` | 11457 | Transferred $L_\infty$ structure on the shadow algebra |
| `cor:shadow-algebra-functoriality` | `corollary` | 11565 | Functoriality of the shadow algebra |
| `prop:master-equation-from-mc` | `proposition` | 11603 | All-arity master equation from MC |
| `thm:ds-complementarity-tower-main` | `theorem` | 11667 | DS complementarity tower |
| `thm:recursive-existence` | `theorem` | 11783 | Recursive existence and shadow tower convergence |
| `thm:perturbative-exactness` | `theorem` | 11985 | Perturbative exactness of the modular MC element |
| `thm:universal-modular-deformation` | `theorem` | 12055 | Universal modular deformation functor |
| `thm:modular-propagator-existence` | `theorem` | 12208 | Modular propagator existence |
| `thm:logfm-modular-cocomposition` | `theorem` | 12242 | Log-FM modular cocomposition |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | 12284 | Stable-graph pronilpotent completion |
| `thm:finite-rank-spectral-reduction` | `theorem` | 12335 | Finite-rank spectral reduction |
| `thm:primitive-to-global-reconstruction` | `theorem` | 12400 | Primitive-to-global reconstruction |
| `prop:primitive-shell-equations` | `proposition` | 12535 | Primitive shell equations |
| `prop:branch-master-equation` | `proposition` | 12673 | Branch quantum master equation |
| `cor:metaplectic-square-root` | `corollary` | 12726 | Determinantal half-density |
| `thm:primitive-flat-descent` | `theorem` | 12917 | Descent to the flat modular connection |
| `thm:conformal-block-reconstruction` | `theorem` | 12996 | Scalar free-energy and determinant reconstruction from the primitive kernel on the proved uniform-weight scalar lane |
| `thm:deformation-quantization-ope` | `theorem` | 13091 | Genus expansion from the OPE |
| `thm:ran-coherent-bar-cobar` | `theorem` | 13292 | Ran-coherent bar-cobar equivalence |
| `thm:shadow-channel-decomposition` | `theorem` | 13352 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 13432 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 13484 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 13610 | Direct derivation on the proved scalar lane |
| `lem:graph-sum-truncation` | `lemma` | 13891 | Graph-sum truncation criterion |
| `conj:operadic-complexity-detailed` | `theorem` | 13967 | Operadic complexity |
| `prop:shadow-formality-low-arity` | `proposition` | 14086 | Shadow--formality identification at low arity |
| `thm:shadow-formality-identification` | `theorem` | 14157 | Shadow tower as formality obstruction tower |
| `thm:shadow-archetype-classification` | `theorem` | 14559 | Shadow archetype classification |
| `cor:shadow-depth-koszul-invariance` | `corollary` | 14756 | Shadow depth under Koszul duality |
| `thm:riccati-algebraicity` | `theorem` | 14829 | Riccati algebraicity: the shadow generating function is algebraic of degree~$2$ |
| `prop:hankel-extraction` | `proposition` | 14962 | Hankel extraction of the quartic contact invariant |
| `thm:shadow-epstein-zeta` | `theorem` | 15153 | The Epstein zeta function of the shadow metric |
| `prop:pole-purity` | `proposition` | 15296 | Pole purity |
| `prop:intrinsic-quartic` | `proposition` | 15314 | Intrinsic quartic principle |
| `thm:single-line-dichotomy` | `theorem` | 15349 | Single-line dichotomy |
| `thm:shadow-connection` | `theorem` | 15486 | Shadow connection |
| `cor:discriminant-atlas` | `corollary` | 15657 | The discriminant atlas |
| `thm:shadow-separation` | `theorem` | 15860 | Shadow separation and completeness |
| `thm:propagator-variance` | `proposition` | 15965 | Propagator variance inequality |
| `prop:t-line-autonomy` | `proposition` | 16075 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | 16132 | Inter-channel coupling on sublines |
| `thm:shadow-radius` | `theorem` | 16277 | Shadow growth rate: structure and asymptotics |
| `cor:virasoro-shadow-radius` | `corollary` | 16383 | Virasoro shadow growth rate |
| `prop:critical-cubic-convergence` | `proposition` | 16575 | Critical cubic convergence threshold |
| `prop:virasoro-bottleneck` | `proposition` | 16664 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | 16891 | Koszul exchange of shadow regimes |
| `prop:koszul-conductor-wn` | `proposition` | 16968 | Koszul conductor of \texorpdfstring{$\cW_N$}{WN} |
| `prop:propagator-universality` | `proposition` | 17026 | Propagator universality |
| `thm:hamilton-jacobi-shadow` | `theorem` | 17369 | Hamilton--Jacobi master equation on deformation spaces |
| `thm:shadow-finite-determination` | `theorem` | 17578 | Shadow finite determination |
| `cor:w3-reconstruction` | `corollary` | 17665 | $\cW_3$: seven parameters determine the full 2D tower |
| `thm:shadow-tautological-ring` | `theorem` | 17871 | Shadow classes in the tautological ring |
| `cor:analytic-shadow-realization` | `corollary` | 18014 | Analytic shadow realization |
| `thm:shadow-cohft` | `theorem` | 18100 | Shadow cohomological field theory |
| `thm:shadow-tautological-relations` | `theorem` | 18371 | Shadow tautological decomposition and conditional vanishing |
| `thm:mc-tautological-descent` | `theorem` | 18462 | MC descent to tautological relations |
| `prop:self-loop-vanishing` | `proposition` | 18937 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | 18973 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | 19092 | Genus-$1$ two-point function from MC |
| `prop:wdvv-from-mc` | `proposition` | 19124 | WDVV from MC at genus~$0$ |
| `prop:mumford-from-mc` | `proposition` | 19157 | Mumford relation from MC at arity~$2$ |
| `thm:planted-forest-structure` | `theorem` | 19189 | Planted-forest structure theorem |
| `thm:cohft-reconstruction` | `theorem` | 19310 | Reconstruction from the MC tangent complex |
| `prop:dressed-propagator-resolution` | `proposition` | 19402 | Dressed propagator coefficient and symmetry |
| `cor:topological-recursion-mc-shadow` | `corollary` | 19541 | Topological recursion as MC shadow |
| `prop:fp-genus-decay-for-double` | `proposition` | 19695 | Faber--Pandharipande genus decay |
| `thm:shadow-double-convergence` | `theorem` | 19722 | Double convergence of the shadow partition function |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | 19891 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:finite-jet-rigidity` | `proposition` | 19972 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 19995 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 20031 | Gaussian collapse for abelian input |
| `thm:cubic-gauge-triviality` | `theorem` | 20115 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | 20223 | Independent sum factorization |
| `thm:envelope-koszul` | `theorem` | 20280 | Envelope Koszulness |
| `cor:generic-ht-koszul` | `corollary` | 20358 | Generic-parameter Koszulness for HT boundary algebras |
| `thm:platonic-adjunction` | `theorem` | 20465 | The platonic adjunction |
| `cor:envelope-universal-mc` | `corollary` | 20598 | The envelope carries the universal MC class |
| `prop:envelope-construction-strategies` | `proposition` | 20656 | Construction strategies for the modular envelope |
| `conj:shadow-depth-invariant` | `theorem` | 20728 | Shadow depth is a homotopy invariant |
| `conj:tropical-koszulness` | `theorem` | 20772 | Tropical Koszulness |
| `cor:tropical-cohen-macaulay` | `corollary` | 20863 | Tropical Koszulness as the Cohen--Macaulay property |
| `prop:genus0-curve-independence` | `proposition` | 20910 | Genus-$0$ curve-independence |
| `thm:open-stratum-curve-independence` | `theorem` | 20929 | Open-stratum curve-independence at higher genus |
| `prop:saddle-point-mc` | `proposition` | 21220 | MC element as saddle point |
| `thm:five-from-theta` | `theorem` | 21491 | Five main theorems from the master MC element |
| `thm:obstruction-recursion` | `theorem` | 21715 | Obstruction recursion for the shadow Postnikov tower |
| `thm:rectification-meta` | `theorem` | 21812 | Rectification meta-theorem |
| `thm:platonic-recovery` | `theorem` | 21908 | Recovery of the platonic package from $\Theta_\cA$ |
| `prop:chriss-ginzburg-structure` | `proposition` | 22130 | MC structure principle |
| `prop:planar-forest-coinvariant` | `proposition` | 22508 | Planar forests map to unordered forests |
| `thm:planar-forest-tropicalization` | `theorem` | 22541 | Planar tropicalization |
| `prop:ordered-log-fm-construction` | `proposition` | 22586 | Ordered log-FM construction |
| `cor:e1-ambient-d-squared-zero` | `corollary` | 22664 | $E_1$ ambient $D^2 = 0$ |
| `prop:coefficient-algebras-well-defined` | `proposition` | 22709 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 22742 | Square-zero: convolution level |
| `conj:differential-square-zero` | `theorem` | 22756 | Square-zero: ambient level |
| `thm:inductive-genus-determination` | `theorem` | 22943 | Inductive genus determination |
| `cor:genus-base-cases` | `corollary` | 23011 | Base cases |
| `rem:genus2-shell-activation` | `theorem` | 23048 | Genus-$2$ shell activation as depth diagnostic |
| `comp:vol1-genus-three-stable-graph-census` | `computation` | 23211 | Genus-$3$ stable graph census |
| `prop:2d-convergence` | `proposition` | 23490 | Two-dimensional convergence |
| `thm:analytic-algebraic-comparison` | `theorem` | 23546 | Analytic = algebraic |
| `thm:determinantal-branch-formula` | `theorem` | 23681 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | 23717 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | 23748 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | 23812 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | 23848 | The frontier is cubic |

#### `chapters/theory/hochschild_cohomology.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 103 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 147 | W-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:401` | `computation` | 401 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 457 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 537 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 792 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 824 | Hochschild cup product exchange |
| `thm:derived-center-hochschild` | `theorem` | 1005 | Derived center $=$ Hochschild cochains |
| `thm:morita-invariance-HH` | `theorem` | 1089 | Morita invariance of $\mathrm{HH}^\bullet$ |
| `prop:explicit-morita-transfer` | `proposition` | 1119 | Explicit Morita transfer |
| `thm:circle-fh-hochschild` | `theorem` | 1290 | Factorization homology on $S^1$ $=$ Hochschild chains |
| `prop:monodromy-standard` | `proposition` | 1443 | Monodromy for standard families |

#### `chapters/theory/introduction.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 1264 | Central charge complementarity |
| `prop:modular-homotopy-classification` | `proposition` | 2955 | Classification by modular homotopy type |
| `prop:shadow-massey-identification` | `proposition` | 3025 | Genus-$0$ shadow obstructions $=$ $A_\infty$ Massey products |
| `prop:chirAss-self-dual` | `proposition` | 4470 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:three-levels-mc-completion` | `proposition` | 122 | Three levels as MC at successive completions |
| `lem:chiral-enveloping-well-defined` | `lemma` | 172 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 217 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 257 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 276 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 333 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 396 | \texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 455 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 584 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 678 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 693 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 797 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 909 | Maurer--Cartan correspondence, quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 1000 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1030 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1240 | Positselski equivalence for the chiral bar coalgebra |
| `thm:full-derived-module-equiv` | `theorem` | 1289 | Flat finite-type reduction on the completed-dual side |
| `thm:cs-koszul-km` | `theorem` | 1403 | Affine Kac--Moody Maurer--Cartan and curvature package |
| `thm:linf-mc-flatness` | `theorem` | 1468 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan equation from a transferred \texorpdfstring{$A_\infty$}{A-infinity} model |
| `thm:cs-koszul-general` | `theorem` | 1523 | Higher Maurer--Cartan equation from non-quadratic transferred \texorpdfstring{$A_\infty$}{A-infinity} models |
| `thm:bv-structure-bar` | `theorem` | 1722 | BV structure on bar complex |
| `thm:ordered-shuffle` | `theorem` | 1888 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | 1930 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | 1960 | Enveloping duality |
| `thm:ordered-bimod-bicomod` | `theorem` | 1999 | Bimodule--bicomodule equivalence |
| `thm:ordered-diagonal` | `theorem` | 2024 | Diagonal correspondence |
| `thm:ordered-HH-coHH-homology` | `theorem` | 2072 | Hochschild--coHochschild duality, homological version |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | 2103 | Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-pair-of-pants` | `theorem` | 2151 | Ordered pair-of-pants algebra |
| `thm:ordered-master` | `theorem` | 2175 | Master theorem: the ordered open trace formalism |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 240 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 352 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 419 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 510 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 569 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 585 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 676 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 762 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `conj:bg-bar-coalg` | `proposition` | 227 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex coalgebra |
| `prop:chiral-operad-genus0` | `proposition` | 327 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 371 | Prism principle: operadic identification |
| `thm:prism-higher-genus` | `theorem` | 611 | Prism principle: higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | 683 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | 708 | The loop expansion is the genus expansion |
| `cor:prism-principle` | `corollary` | 813 | The prism principle |
| `thm:modular-convolution-structure` | `theorem` | 931 | dg~Lie structure |
| `thm:vol1-genus-completion` | `theorem` | 971 | Genus completion |
| `prop:vol1-structure-as-MC` | `proposition` | 1019 | The algebra structure as MC element |
| `thm:partition` | `theorem` | 1125 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:quantum-linfty-master` | `theorem` | 619 | Quantum $L_\infty$ master equation |
| `prop:two-element-strict` | `proposition` | 864 | Two-element covers are strict |
| `prop:borcherds-shadow-identification` | `proposition` | 1348 | Secondary Borcherds operations as shadow tower obstructions |

### Part II: Examples (586)

#### `chapters/examples/bar_complex_tables.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 705 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 798 | Modular rank of \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 877 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 938 | PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} |
| `comp:sl3-casimir-decomp` | `computation` | 1031 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | 1114 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | 1443 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1748 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1794 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | 1865 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | 1916 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2050 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2086 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2120 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2550 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2756 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2976 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 3030 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3067 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3437 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3616 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3913 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3975 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4172 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4322 | BGG involution under Koszul duality |

#### `chapters/examples/beta_gamma.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 243 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 294 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 329 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 382 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 420 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | 441 | — |
| `thm:cobar-fermions` | `theorem` | 469 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | 506 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 594 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 861 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 981 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 1082 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1223 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1307 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1458 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |
| `prop:mumford-exponent-complementarity` | `proposition` | 1633 | Mumford exponent complementarity |
| `thm:betagamma-quartic-birth` | `theorem` | 1982 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | 2018 | $\beta\gamma$ shadow Postnikov tower: arity~$4$ on weight-changing line |
| `prop:betagamma-primitive-kernel` | `proposition` | 2047 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive kernel |
| `prop:betagamma-primitive-shell` | `proposition` | 2095 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive shell equations |
| `lem:betagamma-ell2-vanishing` | `lemma` | 2242 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | 2289 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | 2399 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | 2441 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | 2471 | Pure contact boundary law |
| `prop:betagamma-translation-coproduct` | `proposition` | 2634 | Translation and coproduct |

#### `chapters/examples/deformation_quantization.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 134 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 187 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 419 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 532 | Genus expansion |
| `thm:boundary-linear-lg` | `theorem` | 1820 | Boundary-linear LG theorem |

#### `chapters/examples/deformation_quantization_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 449 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 521 | Deformation--duality compatibility |

#### `chapters/examples/free_fields.tex` (67)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fermion-shadow-invariants` | `proposition` | 205 | Shadow invariants of the free fermion |
| `prop:fermion-shadow-metric` | `proposition` | 284 | Shadow metric of the free fermion |
| `thm:fermion-genus-expansion` | `theorem` | 318 | Free fermion genus expansion |
| `prop:fermion-rmatrix` | `proposition` | 395 | Free fermion $r$-matrix |
| `prop:fermion-complementarity` | `proposition` | 450 | Free fermion complementarity |
| `thm:fermion-sewing` | `theorem` | 520 | Free fermion sewing |
| `prop:fermion-characteristic-data` | `proposition` | 607 | Free fermion characteristic data |
| `thm:single-fermion-boson-duality` | `theorem` | 765 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | 817 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 873 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 924 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 935 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `prop:betagamma-deformation-channels` | `proposition` | 1010 | $\beta\gamma$ deformation complex |
| `prop:betagamma-T-line-shadows` | `proposition` | 1052 | $\beta\gamma$ shadow tower: T-line data |
| `prop:betagamma-weight-line-shadows` | `proposition` | 1087 | $\beta\gamma$ shadow tower: weight-changing line |
| `thm:betagamma-global-depth` | `theorem` | 1109 | $\beta\gamma$ global shadow depth |
| `prop:betagamma-shadow-metric` | `proposition` | 1177 | $\beta\gamma$ shadow metric |
| `comp:betagamma-shadow-weights` | `computation` | 1213 | $\beta\gamma$ shadow tower: special weight table |
| `prop:betagamma-weight-symmetry` | `proposition` | 1249 | Weight symmetry $\neq$ Koszul duality |
| `thm:heisenberg-bar` | `theorem` | 1334 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 1357 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | 1399 | Heisenberg curved structure |
| `thm:lattice-voa-bar` | `theorem` | 1446 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1475 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | 1505 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1542 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | 1591 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 1615 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 1830 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 1906 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 1938 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 2073 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 2128 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 2178 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 2220 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 2373 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 2449 | Spectral flow under Koszul duality |
| `thm:heisenberg-not-self-dual` | `theorem` | 2683 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2788 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2819 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 3078 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 3192 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 3477 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 3626 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 3681 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3746 | Heisenberg level inversion: curved duality |
| `thm:fermion-genus1-partition` | `theorem` | 3895 | Free fermion genus-1 partition functions |
| `thm:fermion-F1-shadow` | `theorem` | 4027 | Free fermion genus-1 free energy |
| `thm:fermion-genus-g` | `theorem` | 4104 | Free fermion at genus $g$ |
| `thm:virasoro-moduli` | `theorem` | 4449 | Critical Virasoro descent at $c = 26$ |
| `prop:moduli-degeneration` | `proposition` | 4547 | Boundary-residue differential on moduli forms |
| `thm:algebraic-string-dictionary` | `theorem` | 4676 | Algebraic bar/BRST genus dictionary |
| `thm:genus-g-chiral-homology` | `theorem` | 4783 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 4894 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 4974 | Bar classes on moduli and boundary factorization |
| `thm:modular-invariance` | `theorem` | 5102 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 5139 | Modular anomaly for affine Kac--Moody algebras |
| `thm:wakimoto-bar` | `theorem` | 5255 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 5268 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 5273 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 5300 | Higher \texorpdfstring{$A_\infty$}{A-infinity} corrections in quantum \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `comp:heisenberg-five-theorems` | `computation` | 5351 | Five projections of $\Theta_{\cH_k}$ |
| `comp:fermion-five-theorems` | `computation` | 5394 | Five projections of $\Theta_{\mathcal{F}}$ |
| `comp:betagamma-five-theorems` | `computation` | 5436 | Five projections of $\Theta_{\beta\gamma}$ |
| `comp:bc-five-theorems` | `computation` | 5491 | Five projections of $\Theta_{bc}$ |
| `comp:lattice-five-theorems` | `computation` | 5538 | Five projections of $\Theta_{V_\Lambda}$ |
| `thm:filtered-bar-complex` | `theorem` | 5619 | Filtered bar complex |

#### `chapters/examples/genus_expansions.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 64 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 138 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `thm:lattice-all-genera` | `theorem` | 182 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 217 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 239 | \texorpdfstring{$\mathcal{W}$}{W}-algebra free energy |
| `thm:sl2-all-genera` | `theorem` | 436 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 585 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 726 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 768 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 822 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 933 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 1043 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1183 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1250 | Genus-2 Virasoro curvature |
| `comp:genus2-complementarity-table` | `computation` | 1401 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1533 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1563 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1581 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1616 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1690 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1818 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1860 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1939 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 2088 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2153 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:universal-fe-ratios` | `proposition` | 2398 | Universal free-energy ratios |
| `prop:complementarity-classification` | `proposition` | 2729 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2783 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 3078 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 3179 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 3195 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 3220 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 3252 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 3347 | Loop expansion interpretation |
| `thm:boundary-characters-bar-hilbert` | `theorem` | 3518 | Boundary characters as bar Hilbert series |

#### `chapters/examples/heisenberg_eisenstein.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:heisenberg-gaussian-termination` | `proposition` | 53 | Gaussian shadow termination for Heisenberg |
| `thm:heisenberg-sewing` | `theorem` | 173 | Heisenberg sewing theorem |
| `prop:heisenberg-r-matrix` | `proposition` | 233 | Heisenberg $r$-matrix |
| `prop:heisenberg-complementarity` | `proposition` | 274 | Heisenberg complementarity |
| `thm:heisenberg-genus-one-complete` | `theorem` | 414 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 501 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 543 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 661 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 764 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 813 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 1142 | Multi-boson Eisenstein corrections |
| `thm:heisenberg-exact-linearity` | `theorem` | 1469 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | 1509 | Heisenberg shadow Postnikov tower: finite termination at arity~$2$ |
| `cor:heisenberg-gaussian-boundary` | `corollary` | 1732 | Gaussian boundary law |
| `prop:heisenberg-primitive-kernel` | `proposition` | 1843 | Heisenberg primitive kernel |
| `prop:heisenberg-primitive-shell` | `proposition` | 1880 | Heisenberg primitive shell equations |

#### `chapters/examples/kac_moody.tex` (52)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:km-genus1-hessian` | `computation` | 195 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `thm:geometric-ope-kac-moody` | `theorem` | 426 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 460 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 500 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 573 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 737 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 768 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 806 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 864 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 900 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 969 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | 1003 | Killing form via structure constants |
| `prop:verdier-level-identification` | `proposition` | 1088 | Verdier level identification |
| `prop:ff-channel-shear` | `proposition` | 1439 | Feigin--Frenkel shear on channel pair |
| `prop:exceptional-shadow-invariants` | `proposition` | 1490 | Exceptional shadow invariants |
| `thm:screening-bar` | `theorem` | 1660 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 1726 | Critical fixed point for principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:kac-moody-ainfty` | `theorem` | 1795 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1834 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1888 | Closed-form OPE for Koszul dual |
| `comp:sl2-collision-residue-kz` | `computation` | 1947 | Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:km-quantum-groups` | `theorem` | 2240 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 2572 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 2644 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 2826 | Kac--Wakimoto formula at \texorpdfstring{$k=-1/2$}{k=-1/2} via bar spectral sequence |
| `prop:admissible-verlinde-bar` | `proposition` | 2998 | Admissible \texorpdfstring{$S$}{S}-matrix and Verlinde fusion package at \texorpdfstring{$k=-1/2$}{k=-1/2} |
| `prop:bar-whittaker` | `proposition` | 3303 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 3384 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 3449 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 3519 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 3585 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 3648 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 3694 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 3733 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 3770 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 3958 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 3988 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 4018 | Local oper differential-form identification |
| `thm:affine-cubic-normal-form` | `theorem` | 4283 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | 4319 | Affine shadow Postnikov tower: finite termination at arity~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | 4357 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | 4399 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | 4469 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 4517 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 4574 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 4651 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 4737 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 4773 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 4864 | Vanishing of the genus loop on the affine cubic |
| `prop:nsl-shadow-tower` | `proposition` | 4941 | Non-simply-laced shadow tower |
| `cor:level-rank-bar-intertwining` | `corollary` | 5232 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | 5260 | Kappa anti-symmetry under Feigin--Frenkel involution |

#### `chapters/examples/landscape_census.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 647 | Paired standard-tower MC4 completion packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 767 | Minimal closure conditions for the standard-tower MC4 completion target |
| `cor:anomaly-ratio-ds` | `corollary` | 1012 | Anomaly ratio and DS reduction |
| `cor:genus1-anomaly-ratio` | `corollary` | 1026 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `cor:subexp-free-field` | `corollary` | 1634 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 1644 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 1661 | DS reduction and bar cohomology generating functions |
| `thm:ds-spectral-branch-preservation` | `theorem` | 1820 | DS preservation of the sub-discriminant |
| `prop:ds-invariant-discriminant` | `proposition` | 1974 | DS-invariant discriminant subfactor |
| `prop:hred-sl2` | `proposition` | 2018 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 2212 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 2303 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 2400 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 2466 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 2521 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 2572 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 2587 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 2676 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2865 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 3171 | Spectral sequence collapse |

#### `chapters/examples/lattice_foundations.tex` (36)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lattice-sewing` | `theorem` | 124 | Lattice sewing envelope |
| `lem:lattice:cocycle-class` | `lemma` | 395 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 559 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 778 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 875 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 898 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 932 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 966 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 1011 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 1097 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 1142 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1347 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1392 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1434 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1457 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1581 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1598 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1623 | Lattice twisted-sector charge inversion on the bar surface |
| `prop:lattice:deformation-properties` | `proposition` | 1807 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1991 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2616 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2684 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2758 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2917 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3219 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3300 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3473 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3678 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3721 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3879 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3926 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 4012 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 4093 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |
| `prop:lattice:genus1-simple-pole` | `proposition` | 4282 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4299 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | 4396 | Lattice shadow Postnikov tower: termination at weight~$2$ |

#### `chapters/examples/minimal_model_examples.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 406 | Fusion from bar complex on the torus |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 82 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | 216 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 364 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 388 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | 423 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 448 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 527 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 554 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 614 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 634 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 661 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 757 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

#### `chapters/examples/toroidal_elliptic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 387 | Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0} |
| `thm:elliptic-vs-rational` | `theorem` | 485 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 857 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1053 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1131 | DYBE and bar nilpotency |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 45 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 147 | Mode expansion |
| `thm:c-scaling` | `theorem` | 198 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 297 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 462 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | 546 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 597 | Quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | 658 | Two-point function \texorpdfstring{$\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$}{:W2:_qp(z) :W2:_qp(w)} |
| `thm:w3-null-level1` | `theorem` | 718 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 821 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 892 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 934 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 1005 | Level-2 Gram matrix |

#### `chapters/examples/w_algebras.tex` (66)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:w3-genus1-hessian` | `computation` | 187 | The $\mathcal W_3$ genus-$1$ Hessian |
| `comp:w-entropy-ladder` | `computation` | 224 | Completion entropy ladder |
| `thm:w-algebra-koszul-main` | `theorem` | 279 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `thm:w-geometric-ope` | `theorem` | 1029 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 1100 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-koszul-precise` | `theorem` | 1158 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras, precise statement |
| `thm:virasoro-self-duality` | `theorem` | 1291 | Virasoro quadratic self-duality |
| `prop:virasoro-generic-koszul-dual` | `proposition` | 1385 | Virasoro Koszul dual at generic central charge |
| `thm:vir-genus1-curvature` | `theorem` | 1541 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1592 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1656 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1826 | Critical fixed point and general-level duality for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1906 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1972 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 2042 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 2137 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 2247 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 2268 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-ainfty-ops` | `theorem` | 2490 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `thm:w-universal-gravitational-cubic` | `theorem` | 3411 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | 3466 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | 3503 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | 3590 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-resonance-reorganization` | `theorem` | 3660 | Resonance reorganization |
| `cor:w-complementarity-potential-poles` | `corollary` | 3797 | Pole structure of the complementarity potential |
| `prop:virasoro-primitive-kernel` | `proposition` | 3852 | Virasoro primitive kernel |
| `prop:virasoro-primitive-shell` | `proposition` | 3904 | Virasoro primitive shell equations |
| `thm:w-w3-mixed-shadow` | `theorem` | 4061 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w3-two-dim-hessian-cubic` | `proposition` | 4123 | Two-dimensional Hessian and universal cubic |
| `thm:w3-quartic-channel-decomposition` | `theorem` | 4151 | $\mathcal{W}_3$ quartic channel decomposition |
| `prop:w3-denominator-filtration` | `proposition` | 4212 | Denominator filtration by $W$-charge |
| `thm:w3-quintic-nonvanishing` | `theorem` | 4240 | $\mathcal{W}_3$ quintic nonvanishing |
| `prop:ds-shadow-cascade` | `proposition` | 4285 | DS shadow cascade for $V_k(\mathfrak{sl}_N) \to \mathcal{W}_N$ |
| `prop:rho-decreasing-with-N` | `proposition` | 4342 | Shadow growth rate decreases with $N$ |
| `prop:w-w3-weight6-resonance` | `proposition` | 4423 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | 4494 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | 4520 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-archetype-trichotomy` | `theorem` | 4609 | Archetype trichotomy |
| `thm:w-virasoro-quintic-forced` | `theorem` | 4676 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | 4732 | Explicit quintic shadow for Virasoro |
| `thm:virasoro-shadow-generating-function` | `theorem` | 4784 | Virasoro shadow metric |
| `thm:w-finite-termination` | `theorem` | 5034 | Finite termination for primitive archetypes |
| `cor:virasoro-postnikov-nontermination` | `corollary` | 5107 | Virasoro/$\mathcal{W}_N$ shadow Postnikov tower: infinite |
| `thm:w-virasoro-genus1-hessian` | `theorem` | 5145 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | 5299 | $\mathcal{W}_3$ quintic obstruction |
| `prop:w3-wline-ring-relations` | `proposition` | 5494 | $W$-line ring relations |
| `thm:w-finite-arity-polynomial-pva` | `theorem` | 5783 | Finite-arity theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | 5821 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | 5863 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | 5890 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | 5966 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | 5991 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | 6025 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | 6063 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | 6083 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `prop:miura-arity-sharp` | `proposition` | 6167 | Miura arity bound is sharp |
| `thm:w-pbw-slodowy-collapse` | `theorem` | 6316 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | 6377 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-arity-detection` | `theorem` | 6485 | Canonical arity detection |
| `thm:w-bp-strict` | `theorem` | 6511 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | 6561 | $\mathcal{W}_4^{(2)}$ has canonical arity~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | 6620 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | 6679 | Subregular Appell formula |
| `thm:w-unbounded-canonical-arity` | `theorem` | 6717 | Unbounded canonical arity |
| `cor:w-subregular-arity-staircase` | `corollary` | 6746 | The subregular arity staircase |
| `thm:w-subregular-classification` | `theorem` | 6788 | Subregular classification |

#### `chapters/examples/w_algebras_deep.tex` (31)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 131 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 1034 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `thm:master-commutative-square` | `theorem` | 1319 | Master commutative square for DS reduction |
| `prop:w3-deg3-vacuum` | `proposition` | 1726 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-bar-formality` | `proposition` | 2013 | DS--bar commutation via filtration formality |
| `thm:transport-closure-type-a` | `theorem` | 2083 | Transport-closure in type $A$ |
| `prop:partition-dependent-complementarity` | `proposition` | 2137 | Kappa deficit and Koszul complementarity for non-principal DS |
| `thm:ds-platonic-functor` | `theorem` | 2229 | BRST reduction on total platonic packages |
| `cor:ds-theta-descent` | `corollary` | 2456 | BRST descent of the universal MC element |
| `comp:wn-stabilization-windows` | `computation` | 2879 | Coefficient stabilization windows for $\mathcal{W}_N$ |
| `prop:abelian-locus-type-a` | `proposition` | 2949 | Abelian locus in type~$A$ |
| `prop:abelianity-complementarity-independence` | `proposition` | 2991 | Independence of abelianity and complementarity |
| `prop:bfn-slodowy-dimensions` | `proposition` | 3072 | BFN--Slodowy dimension matching |
| `prop:ghost-constant-monotonicity` | `proposition` | 3145 | Ghost constant monotonicity |
| `thm:winfty-scalar` | `theorem` | 3296 | One-dimensional cyclic line for $\mathcal{W}_\infty$ |
| `prop:gram-wt4` | `proposition` | 3451 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | 3516 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | 3559 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:higher-w-kappa-matrix` | `proposition` | 3687 | Kappa matrix for $\Walg_N$ |
| `prop:higher-w-gravitational-cubic` | `proposition` | 3750 | Gravitational cubic for $\Walg_N$ |
| `prop:higher-w-parity` | `proposition` | 3793 | $\mathbb{Z}_2$ parity and the cubic shadow |
| `prop:weight-4-exchange-upgrade` | `proposition` | 3850 | Weight-$4$ exchange spectrum upgrade at rank~$3$ |
| `prop:virasoro-primitive` | `proposition` | 4141 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | 4202 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | 4243 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | 4346 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | 4379 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | 4400 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | 4432 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | 4539 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | 4575 | $\Walg_\infty$ bar-window series and Koszul entropy |

#### `chapters/examples/yangians_computations.tex` (42)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:yangian-rank-dependence` | `proposition` | 525 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 662 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 752 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 802 | Bar-comodule Ext comparison for Yangian evaluation modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 859 | DK-2 reduction to thick generation, conditional on an ambient exact extension |
| `prop:dk2-thick-generation-typeA` | `proposition` | 924 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `cor:dk2-thick-generation-all-types` | `corollary` | 1019 | Thick generation for all simple types |
| `lem:composition-thick-generation` | `lemma` | 1044 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 1075 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `lem:monoidal-thick-extension` | `lemma` | 1213 | Monoidal extension to thick closures |
| `lem:fd-thick-closure` | `lemma` | 1403 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 1489 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 1740 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 1870 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 2028 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 2048 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 2073 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 2247 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:baxter-exact-triangles-opoly` | `theorem` | 2315 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `conj:baxter-exact-triangles` | `theorem` | 2357 | Baxter exact triangles on shifted envelope \texorpdfstring{$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$}{Osh} |
| `prop:baxter-yangian-equivariance` | `proposition` | 2405 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | 2479 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `thm:shifted-prefundamental-generation` | `theorem` | 2524 | $E_1$-chiral thick generation for $Y(\mathfrak{sl}_N)$ |
| `prop:prefundamental-clebsch-gordan` | `proposition` | 2749 | Universal prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | 2789 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | 2802 | $K_0$ generation for all simple types |
| `prop:categorical-cg-typeA` | `proposition` | 2851 | Categorical prefundamental CG decomposition, type~$A$ |
| `conj:pro-weyl-recovery` | `theorem` | 2948 | Pro-Weyl recovery of ordinary standards in type~$A$ |
| `thm:mc3-type-a-resolution` | `theorem` | 3205 | Type-$A$ MC3 reduction to the compact-completion packet |
| `conj:mc3-arbitrary-type` | `theorem` | 3284 | Categorical prefundamental CG decomposition, all types |
| `cor:mc3-all-types` | `corollary` | 3431 | All-types MC3 reduction after categorical CG closure |
| `prop:e8-root-uniformity` | `proposition` | 3556 | $E_8$ relevant-root uniformity |
| `prop:character-cg-all-types` | `proposition` | 3566 | Character-level Clebsch--Gordan for all simple types |
| `thm:yangian-vector-seed-propagation` | `theorem` | 3923 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | 3953 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | 3976 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | 3991 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | 4042 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | 4067 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | 4094 | Derived realization of the Baxter--Rees family |
| `thm:yangian-H2-reduction` | `theorem` | 4161 | $H^2$-reduction to the three-leg sector |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | 4238 | Concrete cocycle |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (90)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-dk-affine` | `theorem` | 181 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 285 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 461 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 565 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 697 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 746 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 883 | Evaluation-generated-core DK comparison for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 1083 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 1124 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 1483 | Factorization Positselski equivalence on the bar-coalgebra surface |
| `thm:ind-completed-extension` | `theorem` | 1619 | Ind-completion of the generated-core DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 1819 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 1926 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 2024 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 2245 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 2327 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `thm:bridge-criterion` | `theorem` | 2512 | Bridge Criterion Theorem |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 2764 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 2884 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 2943 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 3026 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 3107 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 3138 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 3175 | Compact-core DK-5 functors from realization of a finite-dimensional factorization DK pair |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 3243 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 3273 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 3305 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 3364 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 3443 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 3472 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 3539 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 3571 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 3609 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 3624 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 3674 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 3731 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 3778 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 3869 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 3969 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 4009 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 4045 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 4072 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 4215 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 4253 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 4303 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 4341 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 4368 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 4407 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 4445 | DK-5 closes once the compact cores realize a finite-dimensional factorization DK pair |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 4470 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 4668 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 4731 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 4766 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 4820 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 4853 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 4919 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 4998 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts-orig` | `corollary` | 5152 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet-orig` | `corollary` | 5181 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization-orig` | `corollary` | 5214 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of a chosen finite-dimensional factorization DK pair |
| `cor:yangian-formal-moduli-plus-core-realization-orig` | `corollary` | 5244 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize a chosen finite-dimensional DK pair |
| `cor:yangian-typea-realization-plus-dg-packet-orig` | `corollary` | 5294 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 5402 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 5505 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 5566 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 5616 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 5675 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed-orig` | `corollary` | 5718 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line-orig` | `corollary` | 5751 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |
| `prop:ds-functor-primitive-triple` | `proposition` | 6341 | DS reduction on primitive triples |
| `prop:free-propagator-matching` | `proposition` | 6774 | Free/$\beta\gamma$ propagator matching |
| `prop:affine-propagator-matching` | `proposition` | 6820 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `prop:rmatrix-pole-landscape` | `proposition` | 6894 | The collision-residue $r$-matrix across the standard landscape |
| `prop:bosonic-parity-constraint` | `proposition` | 6997 | Bosonic parity constraint on $r$-matrix poles |
| `prop:cybe-from-mc` | `proposition` | 7040 | CYBE from bar-complex MC equation |
| `thm:rmatrix-koszul-inverse` | `theorem` | 7138 | Collision residue as binary Koszul inverse |
| `thm:r-matrix-koszul-dual-inverse` | `theorem` | 7266 | The $r$-matrix as Koszul-dual inverse |
| `thm:spectral-derived-additive-kz` | `theorem` | 7487 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | 7539 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | 7591 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | 7665 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | 7749 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | 7807 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | 7849 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | 7884 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | 7939 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | 8011 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | 8035 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | 8076 | Exact free transport |
| `thm:spectral-conditional-strictification` | `theorem` | 8110 | Conditional strictification criterion |

#### `chapters/examples/yangians_foundations.tex` (42)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 253 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 340 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 373 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 432 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 477 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 532 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 596 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 1074 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1199 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1243 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1354 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1458 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1476 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1506 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1568 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 1632 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 1718 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 1815 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 1885 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 1954 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 1991 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2047 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2107 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2168 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2267 | Standard type-A fundamental line operator has the standard local residue |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | 2693 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | 2720 | Stabilized completed bar/cobar recovery |
| `cor:shifted-rtt-tower-convergence` | `corollary` | 2751 | Automatic tower convergence |
| `thm:shifted-rtt-mc-descent` | `theorem` | 2781 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | 2869 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | 2914 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | 2962 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | 2978 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | 3008 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | 3041 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | 3075 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | 3100 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | 3172 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | 3221 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | 3247 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | 3274 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | 3296 | Kleinian associated graded at the nilpotent point |

### Part III: Connections (626)

#### `chapters/connections/arithmetic_shadows.tex` (105)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:shadow-spectral-correspondence` | `theorem` | 101 | Shadow--spectral correspondence |
| `prop:divisor-sum-decomposition` | `proposition` | 207 | Divisor-sum decomposition |
| `cor:sewing-euler-product` | `corollary` | 232 | Euler product of the sewing determinant |
| `prop:sewing-trace-formula` | `proposition` | 245 | Sewing trace formula |
| `thm:sewing-selberg-formula` | `theorem` | 277 | Sewing--Selberg formula |
| `thm:narain-universality` | `theorem` | 334 | Narain universality |
| `thm:e8-epstein` | `theorem` | 365 | $E_8$ Epstein factorization |
| `prop:z2-epstein` | `proposition` | 390 | $\bZ^2$ Epstein zeta |
| `prop:leech-epstein` | `proposition` | 413 | Leech Epstein factorization |
| `prop:leading-hecke-identification` | `proposition` | 577 | Leading-order Hecke identification |
| `rem:hecke-all-orders` | `proposition` | 604 | Exactness of the Hecke identification |
| `prop:period-shadow-dictionary` | `proposition` | 656 | Period--shadow dictionary |
| `comp:period-shadow-vz` | `computation` | 739 | $V_{\bZ}$: the Gaussian archetype |
| `comp:period-shadow-ve8` | `computation` | 757 | $V_{E_8}$: the Lie/tree archetype |
| `comp:period-shadow-leech` | `computation` | 779 | $V_{\mathrm{Leech}}$: the Ramanujan archetype |
| `comp:period-shadow-rank24-comparison` | `computation` | 832 | $D_{16}^+ \oplus D_{16}^+$ vs.\ $E_8^3$: same depth, different coefficient |
| `comp:period-shadow-rank2` | `computation` | 851 | $V_{\bZ^2}$ and $V_{A_2}$: Dedekind zeta at depth~$2$ |
| `thm:spectral-decomposition-principle` | `theorem` | 875 | Spectral decomposition principle |
| `prop:growth-rate-dictionary` | `proposition` | 962 | Growth-rate dictionary |
| `thm:bg-vir-coincidence` | `theorem` | 988 | $\beta\gamma$--Virasoro rate coincidence |
| `prop:self-referentiality-criterion` | `proposition` | 1006 | Self-referentiality criterion |
| `cor:conformal-vector-infinite-depth` | `corollary` | 1076 | Conformal vector implies infinite depth |
| `thm:shadow-tower-asymptotics` | `theorem` | 1099 | Shadow tower leading asymptotics |
| `cor:rigorous-infinite-depth` | `corollary` | 1131 | Rigorous infinite depth |
| `prop:bg-primary-counting` | `proposition` | 1166 | $\beta\gamma$ primary-counting function |
| `thm:refined-shadow-spectral` | `theorem` | 1179 | Refined shadow--spectral correspondence |
| `prop:ising-d-arith` | `proposition` | 1209 | Ising model: $d_{\mathrm{arith}} = 0$ |
| `rem:non-unimodular` | `remark` | 1258 | Non-unimodular lattices |
| `thm:depth-decomposition` | `theorem` | 1327 | Depth decomposition |
| `thm:ainfty-formality-depth` | `theorem` | 1424 | $A_\infty$ formality criterion |
| `thm:interacting-gram-positivity` | `theorem` | 1482 | Interacting Gram positivity |
| `cor:virasoro-interacting-gram` | `corollary` | 1522 | — |
| `thm:shadow-resonance-locus` | `theorem` | 1535 | — |
| `prop:shadow-spectral-measure` | `theorem` | 1573 | Shadow spectral measure |
| `prop:carleman-virasoro` | `proposition` | 1639 | Carleman rigidity |
| `prop:shadow-periods` | `proposition` | 1676 | Shadow amplitudes are periods |
| `thm:spectral-curve` | `theorem` | 1820 | Algebraic shadow generating function |
| `prop:moment-matrix-negativity` | `proposition` | 1863 | Eisenstein moment minor |
| `thm:shadow-higgs-field` | `theorem` | 1896 | Shadow Higgs field |
| `thm:general-nahc` | `theorem` | 1977 | General shadow triple |
| `thm:shadow-bps` | `theorem` | 2146 | The shadow tower as BPS spectrum |
| `thm:general-bps` | `theorem` | 2226 | General BPS spectrum of the shadow tower |
| `thm:sewing-shadow-intertwining` | `theorem` | 2271 | Sewing--shadow intertwining at genus~$1$ |
| `cor:shadow-fredholm` | `corollary` | 2346 | Shadow Fredholm determinant |
| `cor:spectral-measure-identification` | `corollary` | 2383 | Spectral measure identification |
| `sec:shadow-moduli-resolution` | `theorem` | 2437 | Shadow-moduli resolution |
| `thm:universality-of-G` | `theorem` | 2527 | Universality of $G$ |
| `prop:mc-bracket-determines-atoms` | `proposition` | 2595 | MC bracket determines spectral atoms |
| `rem:mc-ramanujan-bridge` | `remark` | 2645 | The bridge to the Ramanujan bound |
| `thm:spectral-continuation-bridge` | `theorem` | 2690 | Hecke-equivariant MC element |
| `thm:schur-complement-quartic` | `theorem` | 2829 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | 2888 | — |
| `prop:on-off-line-distinction` | `proposition` | 2965 | — |
| `prop:li-criterion-failure` | `proposition` | 3350 | Structural failure of the Li criterion for the sewing lift |
| `prop:pure-spin-s-schur` | `proposition` | 3500 | — |
| `prop:prime-side-defect-formula` | `proposition` | 3608 | — |
| `thm:finite-miura-defect` | `theorem` | 3678 | Finite Miura defect at genus one |
| `prop:modularity-constraint` | `proposition` | 4252 | Modularity constraint on the spectral measure |
| `sec:bracket-hodge-index` | `proposition` | 4295 | Bracket positivity and the Hodge index |
| `sec:proved-regime-ramanujan` | `proposition` | 4421 | Ramanujan bound for lattice spectral measures |
| `sec:symmetric-power-route` | `proposition` | 4464 | Shadow--symmetric power identification |
| `thm:petersson-identification` | `theorem` | 4612 | Petersson identification |
| `prop:modularity-constraint-atoms` | `proposition` | 4698 | Modularity constraint on atoms |
| `prop:rigidity-threshold` | `proposition` | 4735 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | 4833 | Lattice Ramanujan from rigidity |
| `prop:stieltjes-signed-universal` | `proposition` | 5032 | Universal signed Stieltjes measure |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | 5065 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | 5129 | Shadow arithmetic trichotomy |
| `prop:genus1-weight-bound` | `proposition` | 5204 | Weight bound for genus-$1$ shadow projections |
| `thm:mc-recursion-moment` | `theorem` | 5337 | MC recursion on moment $L$-functions |
| `prop:shadow-chiral-graph` | `proposition` | 5406 | Shadow amplitudes as chiral graph integrals |
| `thm:hecke-newton-lattice` | `theorem` | 5479 | Hecke--Newton closure for lattice VOAs |
| `cor:unconditional-lattice` | `corollary` | 5542 | Unconditional operadic RS for lattice VOAs |
| `thm:non-lattice-ramanujan` | `theorem` | 5571 | Non-lattice Ramanujan bound |
| `prop:mc-constraint-counting` | `proposition` | 6091 | MC constraint counting |
| `thm:route-c-propagation` | `theorem` | 6156 | Route~C: MC rigidity forces character-level prime-locality |
| `cor:route-c-standard-landscape` | `corollary` | 6279 | Route~C for the standard landscape |
| `thm:hecke-verdier-commutation` | `theorem` | 6324 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | 6363 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | 6438 | Theta decomposition bridge |
| `prop:newton-shadow-hecke` | `proposition` | 6501 | Newton--shadow--Hecke correspondence |
| `prop:sewing-spectral-bridge` | `proposition` | 6619 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | 6724 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | 6771 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | 6829 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | 7004 | Genus-one saddle triviality |
| `cor:first-scattering-pole` | `corollary` | 7204 | Nonvanishing at the first scattering pole |
| `thm:scattering-coupling-factorization` | `theorem` | 7306 | Scattering coupling factorization |
| `thm:structural-separation` | `theorem` | 7389 | Structural separation of algebraic and arithmetic content |
| `prop:hecke-defect-equivalences` | `proposition` | 7515 | Equivalent characterizations; \textup{(i)--(iii)} ; \textup{(iv)} |
| `prop:hecke-defect-lattice` | `proposition` | 7566 | Hecke defect vanishes for lattice VOAs |
| `prop:hecke-defect-families` | `proposition` | 7644 | Hecke defect for standard families; \textup{(i)} ; \textup{(ii)} ; \textup{(iii)} |
| `thm:rigidity-inheritance` | `theorem` | 7763 | Rigidity inheritance |
| `thm:packet-connection-flatness` | `theorem` | 8070 | Flatness and divisor independence |
| `cor:lattice-packet-diagonal` | `corollary` | 8137 | Lattice transparency |
| `prop:gauge-criterion-scattering` | `proposition` | 8203 | Gauge criterion for scattering access |
| `prop:miura-packet-splitting` | `proposition` | 8326 | — |
| `prop:genus2-non-diagonal` | `proposition` | 8692 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | 8736 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | 8868 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | 8900 | B\"ocherer bridge |
| `thm:leech-chi12-projection` | `theorem` | 9019 | Leech $\chi_{12}$-projection and Waldspurger consequence |
| `prop:prime-locality-proved-cases` | `proposition` | 9238 | Settled cases |
| `thm:prime-locality-obstructions` | `theorem` | 9279 | Precise obstructions to prime-locality; {} where indicated |
| `thm:riccati-determinacy-assessment` | `theorem` | 9481 | Riccati determinacy |

#### `chapters/connections/bv_brst.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:log-form-ghost-law` | `theorem` | 293 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 396 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 547 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `thm:bar-semi-infinite-km` | `theorem` | 643 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 747 | Anomaly duality for Kac--Moody pairs |
| `cor:anomaly-duality-w` | `corollary` | 905 | Curvature complementarity for principal \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |

#### `chapters/connections/concordance.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 423 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 437 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | 730 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 754 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 791 | Gaussian collapse for abelian input |
| `prop:five-theorems-mc-projections` | `proposition` | 2211 | Five main theorems as MC projections |
| `thm:operadic-complexity-concordance` | `theorem` | 2378 | Operadic complexity |
| `prop:vol2-relative-holographic-bridge` | `proposition` | 4023 | Relative holographic deformation bridge |
| `prop:vol2-ribbon-thooft-bridge` | `proposition` | 4044 | Ribbon/'t~Hooft bridge |
| `thm:lagrangian-complementarity` | `theorem` | 4369 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 4642 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 4993 | Discriminant as spectral determinant, verified cases |
| `thm:discriminant-spectral` | `theorem` | 5038 | Spectral discriminant, general case |
| `comp:spectral-discriminants-standard` | `computation` | 5264 | Spectral discriminants of standard families |
| `thm:family-index` | `theorem` | 5329 | Family index theorem for genus expansions |
| `rem:programme-vi-verification` | `remark` | 6536 | Programme VI: systematic verification of (H1)--(H4) |
| `rem:four-test-interface` | `remark` | 6710 | The four-test interface |
| `prop:descent-fan` | `proposition` | 8540 | Descent fan structure |

#### `chapters/connections/editorial_constitution.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-pbw` | `theorem` | 197 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 223 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, resolved)} |
| `prop:en-n2-recovery` | `proposition` | 1654 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1800 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1858 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1892 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1908 | Physical anomaly cancellation for affine Kac--Moody algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2136 | Hodge symmetry from complementarity |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 2456 | Volume~I concrete modular datum |

#### `chapters/connections/entanglement_modular_koszul.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ent-scalar-entropy` | `theorem` | 165 | Entanglement entropy at the scalar level |
| `thm:entanglement-complementarity` | `theorem` | 239 | Entanglement complementarity |
| `prop:ent-complexity-classification` | `proposition` | 359 | Entanglement complexity classification |
| `cor:ent-full-entropy` | `corollary` | 457 | Full entanglement entropy |
| `prop:ent-qes` | `proposition` | 490 | QES from shadow connection |
| `thm:ent-landscape-census` | `theorem` | 572 | Standard landscape entanglement census |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 112 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 190 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 295 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 340 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 367 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 407 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 425 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 446 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 493 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 552 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 908 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 940 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (42)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | 137 | Protected dual transform and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | 235 | Protected transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | 288 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | 329 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | 383 | Scalar fixed-point rigidity on a full scalar package and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | 498 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | 611 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | 732 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | 803 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | 935 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | 1015 | The first nonlinear holographic anomaly |
| `thm:yangian-shadow-theorem` | `theorem` | 1404 | Yangian-shadow theorem |
| `thm:sphere-reconstruction` | `theorem` | 1461 | Sphere flatness and reconstruction on established comparison surfaces |
| `thm:quartic-resonance-obstruction` | `theorem` | 1537 | Quartic resonance obstruction |
| `thm:collision-residue-twisting` | `theorem` | 1961 | Collision residue = universal twisting morphism |
| `thm:collision-depth-2-ybe` | `theorem` | 2017 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `thm:shadow-connection-kz` | `theorem` | 2055 | Shadow/KZ comparison on the affine Kac--Moody surface |
| `cor:shadow-connection-heisenberg` | `corollary` | 2099 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | 2120 | Shadow connection for Virasoro and BPZ on the degenerate-representation surface |
| `thm:quartic-obstruction-linf` | `theorem` | 2156 | Quartic obstruction = $L_\infty$ obstruction |
| `comp:holographic-ss-sl2` | `computation` | 2240 | The $E_1$ page for $\widehat{\mathfrak{sl}}_2$ |
| `comp:holographic-ss-vir` | `computation` | 2292 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | 2336 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | 2359 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | 2440 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | 2463 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | 2503 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | 2594 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | 2650 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | 2745 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | 2779 | Holographic datum for $\mathcal W_3$ |
| `thm:ds-central-charge-additivity` | `theorem` | 2899 | Central charge additivity under DS |
| `cor:critical-dimensions` | `corollary` | 3000 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | 3111 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | 3135 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | 3171 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | 3196 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | 3308 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | 3444 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | 3619 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | 3743 | Lifts as relative MC elements |
| `cor:holographic-deformation-cohomology` | `corollary` | 3774 | — |

#### `chapters/connections/genus_complete.tex` (28)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 236 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 292 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 374 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 656 | Bar complex computes moduli integrals |
| `thm:full-modular-invariant-hierarchy` | `theorem` | 1215 | The full modular invariant hierarchy |
| `prop:sewing-universal-property` | `proposition` | 1337 | Universal property of the sewing envelope |
| `prop:hs-trace-class` | `proposition` | 1376 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | 1391 | General HS-sewing criterion |
| `cor:hs-sewing-standard-landscape` | `corollary` | 1423 | Standard landscape |
| `cor:hs-implies-gram` | `corollary` | 1461 | — |
| `thm:heisenberg-one-particle-sewing` | `theorem` | 1480 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | 1557 | Positive grading implies conilpotency |
| `prop:dirichlet-weight-formula` | `theorem` | 1859 | — |
| `cor:virasoro-mode-removal` | `corollary` | 1917 | — |
| `prop:euler-koszul-criterion` | `theorem` | 1976 | — |
| `comp:euler-koszul-defect-table` | `computation` | 2013 | Euler--Koszul defect table for the standard landscape |
| `prop:zeta-zeros-defect-derivative` | `proposition` | 2105 | — |
| `thm:li-closed-form` | `theorem` | 2143 | — |
| `prop:li-asymptotics` | `theorem` | 2176 | — |
| `prop:surface-moment-positivity` | `theorem` | 2304 | Gram positivity |
| `cor:virasoro-gram-ratio` | `corollary` | 2327 | — |
| `thm:sewing-rkhs` | `theorem` | 2362 | Sewing RKHS |
| `prop:collapse-permanence` | `proposition` | 2429 | Collapse permanence |
| `rem:benjamin-chang-bridge` | `proposition` | 2468 | — |
| `thm:shadow-euler-independence` | `theorem` | 2494 | — |
| `rem:two-faces-theta` | `corollary` | 2551 | — |
| `thm:euler-koszul-tier-classification` | `theorem` | 2633 | — |
| `thm:sewing-hecke-reciprocity` | `theorem` | 2714 | Sewing--Hecke reciprocity |

#### `chapters/connections/holographic_codes_koszul.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:hc-knill-laflamme` | `proposition` | 93 | Knill--Laflamme from Lagrangian isotropy |
| `thm:hc-symplectic-code` | `theorem` | 221 | Symplectic code structure |
| `thm:hc-koszulness-exact-qec` | `theorem` | 341 | \textbf{G12}: Koszulness $\Leftrightarrow$ exact holographic reconstruction |
| `thm:hc-shadow-redundancy` | `theorem` | 459 | Shadow depth controls redundancy |
| `thm:hc-dictionary` | `proposition` | 560 | 12-fold dictionary |
| `thm:hc-census` | `theorem` | 683 | Standard landscape code census |

#### `chapters/connections/holomorphic_topological.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:ht-bar-genus-zero` | `proposition` | 108 | Bar complex and genus-zero HT data |
| `thm:ht-mc-all-genera` | `theorem` | 137 | MC element and all-genus HT partition function |
| `cor:ht-shadow-archetype` | `corollary` | 168 | Shadow archetype classification |
| `prop:ht-five-shadow-synthesis` | `proposition` | 226 | Five-shadow synthesis |
| `prop:ht-four-recovery` | `proposition` | 268 | Four recovery theorems |

#### `chapters/connections/kontsevich_integral.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-weight-systems` | `theorem` | 108 | Bar complex weight systems |
| `prop:propagator-restriction` | `proposition` | 177 | Propagator restriction |
| `prop:kz-from-bar` | `proposition` | 266 | KZ connection from bar complex |
| `thm:drinfeld-associator-bar` | `theorem` | 309 | Drinfeld associator from bar-cobar |
| `prop:feynman-graph-complex` | `proposition` | 409 | Feynman transform and algebraic graph-complex refinement |

#### `chapters/connections/outlook.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:operadic-complexity` | `theorem` | 250 | Operadic complexity |

#### `chapters/connections/poincare_computations.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-c26-selfdual` | `proposition` | 161 | Virasoro NAP duality at \texorpdfstring{$c=26$}{c=26} |
| `thm:genus-complementarity` | `theorem` | 288 | Genus complementarity |

#### `chapters/connections/semistrict_modular_higher_spin_w3.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:finite-arity-polynomial-pva-chapter` | `theorem` | 100 | Finite-arity theorem for polynomial PVAs |
| `cor:semistrictity-classical-W3-chapter` | `corollary` | 138 | Semistrictity of the classical $W_3$ bulk |
| `prop:tree-identity-semistrict-chapter` | `proposition` | 156 | Tree identity for semistrict cyclic theories |
| `prop:canonical-central-hodge-shadow-lift-chapter` | `proposition` | 242 | Canonical central Hodge-shadow lift |
| `prop:clutching-duality-shadow-lift-chapter` | `proposition` | 275 | Clutching additivity and duality symmetry |
| `thm:fiber-decomposition-shadow-base-point-chapter` | `theorem` | 317 | Fiber decomposition over the shadow base point |
| `cor:shadow-centered-reduction-chapter` | `corollary` | 345 | Shadow-centered reduction |
| `thm:finite-arity-convolution-chapter` | `theorem` | 380 | Finite-arity convolution theorem |
| `thm:quadratic-cubic-twisting-theorem-chapter` | `theorem` | 432 | Quadratic-cubic twisting theorem |
| `prop:admissibility-finite-slices-chapter` | `proposition` | 507 | Admissibility and finite-dimensional weight slices |
| `thm:cubic-weight-recursion-chapter` | `theorem` | 530 | Cubic weight recursion around the shadow base point |
| `cor:cubic-obstruction-classes-chapter` | `corollary` | 561 | Cubic obstruction classes |
| `prop:stable-graph-identity-chapter` | `proposition` | 574 | Stable-graph identity for semistrict modular theories |
| `prop:well-definedness-completed-boundary-model-chapter` | `proposition` | 628 | Well-definedness of the completed boundary model |
| `thm:main-semistrict-modular-higher-spin-package-chapter` | `theorem` | 658 | Main Theorem: the classical $W_3$ sector defines a semistrict modular higher-spin package |
| `cor:platonic-reduction-W3-frontier` | `corollary` | 693 | Platonic reduction of the $W_3$ frontier |

#### `chapters/connections/thqg_critical_string_dichotomy.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:transgression-kills-curvature` | `proposition` | 127 | Transgression kills curvature |
| `prop:g9-quotient` | `proposition` | 204 | Quotient identification |
| `prop:secondary-anomaly-properties` | `proposition` | 302 | Properties of $u$ |
| `prop:g9-ses-transgression` | `proposition` | 378 | Short exact sequence of the transgression |
| `cor:g9-bockstein` | `corollary` | 417 | Bockstein long exact sequence |
| `thm:clifford-relations` | `theorem` | 505 | Clifford relations for handle operators |
| `thm:topological-regime` | `theorem` | 745 | Topological regime |
| `thm:gravitational-regime` | `theorem` | 816 | Gravitational regime |
| `thm:critical-string-dichotomy` | `theorem` | 1041 | Critical string dichotomy for the Virasoro |
| `thm:ghost-sector-c26` | `theorem` | 1204 | Ghost sector at $c = 26$ |
| `thm:vir-self-duality-c13` | `theorem` | 1277 | Virasoro self-duality at $c = 13$ |
| `thm:critical-dichotomy-summary` | `theorem` | 1350 | Critical string dichotomy: structural summary |
| `prop:shadow-critical` | `proposition` | 1426 | Shadow tower at critical central charges |
| `prop:hodge-clifford` | `proposition` | 1499 | Hodge--Clifford compatibility |
| `prop:clifford-spectral-degeneration` | `proposition` | 1577 | Degeneration |
| `prop:bosonic-string-identifications` | `proposition` | 1607 | Bosonic string structural identifications |
| `thm:localization-sequence` | `theorem` | 1786 | Localization sequence |
| `cor:g9-localization-vir` | `corollary` | 1834 | Localization for the Virasoro |
| `prop:g9-bialgebra` | `proposition` | 1884 | Bialgebra extension |
| `cor:g9-u-coproduct` | `corollary` | 1915 | Coproduct of the secondary anomaly |
| `prop:g9-universal` | `proposition` | 1966 | Universal property |
| `cor:g9-comparison-universal` | `corollary` | 2003 | The comparison map is universal |
| `prop:g9-clifford-deformation` | `proposition` | 2029 | Deformation of the Clifford algebra |
| `prop:g9-trace-formula` | `proposition` | 2104 | Trace formula |
| `cor:g9-partition-trace` | `corollary` | 2128 | Genus-$g$ partition function via trace |

#### `chapters/connections/thqg_entanglement_programme.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-lagrangian-constraint` | `theorem` | 173 | Lagrangian constraint theorem |
| `thm:thqg-qes-convergence` | `theorem` | 327 | QES convergence |
| `prop:thqg-barcobar-error-correction` | `proposition` | 588 | Bar-cobar code structure |
| `thm:thqg-entanglement-wedge` | `theorem` | 653 | Subregion structure from the open/closed realization |
| `thm:thqg-page-constraint` | `theorem` | 694 | Algebraic Page constraint |

#### `chapters/connections/thqg_fredholm_partition_functions.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-X-sewing-filtration` | `proposition` | 194 | Sewing envelope: conformal weight filtration |
| `lem:thqg-X-sewing-schatten` | `lemma` | 332 | Schatten class properties of $\sewop_q$ |
| `lem:thqg-X-composition-decay` | `lemma` | 446 | Exponential decay of composition coefficients |
| `prop:thqg-X-second-quantization` | `proposition` | 484 | Second quantization |
| `thm:thqg-X-heisenberg-sewing-full` | `theorem` | 564 | Heisenberg sewing theorem: full development |
| `prop:polyakov-alvarez-shadow-specialization` | `proposition` | 868 | Polyakov--Alvarez as shadow metric specialization |
| `thm:thqg-X-genus-1-fredholm` | `theorem` | 947 | Genus-1 Fredholm determinant |
| `comp:thqg-X-genus-1-series` | `computation` | 1050 | Genus-1 Fredholm determinant: explicit series |
| `thm:thqg-X-genus-2-fredholm` | `theorem` | 1095 | Genus-2 Fredholm determinant |
| `comp:thqg-X-genus-2-series` | `computation` | 1203 | Genus-2 Fredholm determinant: leading terms |
| `thm:thqg-X-genus-3-fredholm` | `theorem` | 1230 | Genus-3 Fredholm determinant |
| `thm:thqg-X-general-genus-fredholm` | `theorem` | 1350 | General-genus Fredholm structure |
| `prop:thqg-X-free-energy-ahat` | `proposition` | 1424 | Free energy: $\hat{A}$-genus verification |
| `thm:thqg-X-class-G-fredholm` | `theorem` | 1500 | Fredholm scalar partition function on the Gaussian scalar lane |
| `prop:thqg-X-rank-additivity` | `proposition` | 1594 | Rank additivity |
| `thm:thqg-X-feynman-expansion` | `theorem` | 1661 | Feynman integral expansion |
| `prop:thqg-X-class-L-feynman` | `proposition` | 1724 | Class-L Feynman integrals |
| `prop:thqg-X-class-C-quartic` | `proposition` | 1818 | Class-C quartic contact |
| `prop:thqg-X-virasoro-decomposition` | `proposition` | 1902 | Virasoro: Fredholm base + corrections |
| `prop:thqg-X-analytic-bar-bounded` | `proposition` | 1999 | Analytic bar differential is bounded |
| `prop:thqg-X-analytic-coproduct` | `proposition` | 2027 | Analytic coproduct |
| `prop:thqg-X-coderived-fredholm-G` | `proposition` | 2107 | Coderived = Fredholm for class~G |
| `prop:givental-vertex-reconstruction` | `proposition` | 2376 | Givental reconstruction of higher-genus vertex factors |
| `thm:gravitational-complementarity-genus-expansion` | `theorem` | 2496 | Gravitational complementarity genus expansion |
| `prop:virasoro-F2-full` | `proposition` | 2611 | Full genus-$2$ free energy for Virasoro |
| `prop:cohft-complementarity` | `proposition` | 2662 | CohFT complementarity |

#### `chapters/connections/thqg_gravitational_complexity.tex` (39)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-two-sources` | `proposition` | 70 | Two sources of gravitational obstruction |
| `thm:thqg-complexity-controls-bulk` | `theorem` | 174 | Shadow-depth stabilization and transferred arity cutoff |
| `prop:thqg-depth-qi-invariant` | `proposition` | 216 | Shadow depth is a quasi-isomorphism invariant |
| `lem:thqg-cubic-source` | `lemma` | 243 | Cubic source permanence |
| `thm:thqg-four-class` | `theorem` | 277 | Four-class complexity classification |
| `thm:thqg-grav-content` | `theorem` | 374 | Transferred \texorpdfstring{$L_\infty$}{L-infty} profiles of the four classes |
| `thm:thqg-gaussian-termination` | `theorem` | 431 | Gaussian termination |
| `cor:thqg-gaussian-potential` | `corollary` | 451 | Gaussian complementarity potential |
| `thm:thqg-lie-termination` | `theorem` | 499 | Lie termination |
| `thm:thqg-contact-termination` | `theorem` | 564 | Contact termination |
| `prop:thqg-cubic-gauge` | `proposition` | 598 | Cubic gauge triviality mechanism |
| `thm:thqg-virasoro-quintic` | `theorem` | 626 | Virasoro quintic obstruction |
| `thm:thqg-virasoro-infinite` | `theorem` | 661 | Virasoro shadow tower is infinite |
| `thm:thqg-virasoro-tower-explicit` | `theorem` | 704 | Virasoro shadow tower through septic order |
| `prop:thqg-virasoro-structure` | `proposition` | 780 | Structural properties of the Virasoro tower |
| `thm:thqg-virasoro-potential` | `theorem` | 832 | Virasoro complementarity potential |
| `thm:thqg-genus1-hessian` | `theorem` | 879 | Genus-$1$ Hessian correction |
| `cor:thqg-virasoro-genus1` | `corollary` | 895 | Virasoro genus-$1$ Hessian |
| `thm:thqg-genus2-diagnostic` | `theorem` | 939 | Genus-$2$ binary diagnostic |
| `thm:thqg-obstruction-table` | `theorem` | 1002 | Complete obstruction data through arity~$6$ |
| `thm:thqg-vanishing-mechanisms` | `theorem` | 1076 | Classification of vanishing mechanisms |
| `thm:thqg-independent-sum` | `theorem` | 1116 | Independent sum factorization |
| `prop:thqg-depth-koszulness-independent` | `proposition` | 1148 | Depth and Koszulness are independent |
| `cor:thqg-duality-table` | `corollary` | 1199 | Duality-complexity table |
| `prop:thqg-tropical-profiles` | `proposition` | 1237 | Tropical profiles |
| `thm:thqg-holographic-type` | `theorem` | 1274 | Primary-line shadow profile from the depth class |
| `prop:thqg-wn-stabilization` | `proposition` | 1328 | $\mathcal{W}_N$ complexity stabilises |
| `thm:thqg-grav-landscape` | `theorem` | 1357 | Gravitational complexity census |
| `thm:thqg-g2-main` | `maintheorem` | 1405 | Shadow-depth classification; result (G2) |
| `prop:thqg-complexity-functor` | `proposition` | 1453 | Functoriality of complexity |
| `prop:thqg-coefficient-asymptotics` | `proposition` | 1528 | Coefficient asymptotics |
| `prop:thqg-generic-constancy` | `proposition` | 1597 | Generic constancy |
| `thm:thqg-mc-euler-lagrange` | `theorem` | 1652 | Primary-line MC critical-point equation |
| `thm:thqg-holographic-ss` | `theorem` | 1750 | Collision-filtration spectral sequence |
| `prop:thqg-collapse-criteria` | `proposition` | 1784 | Collapse criteria by complexity class |
| `prop:thqg-e1-virasoro` | `proposition` | 1841 | $E_1$ page for Virasoro |
| `prop:thqg-collapse-L` | `proposition` | 1888 | Collapse for class~$\mathbf{L}$ |
| `prop:thqg-collapse-C` | `proposition` | 1912 | Collapse for class~$\mathbf{C}$ |
| `prop:thqg-curve-independence` | `proposition` | 1957 | Curve independence |

#### `chapters/connections/thqg_gravitational_s_duality.tex` (46)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-IV-verdier-graph-composition` | `lemma` | 135 | Verdier compatibility with graph composition |
| `prop:thqg-IV-verdier-dg-lie` | `proposition` | 221 | Properties of the Verdier involution |
| `cor:thqg-IV-verdier-mc` | `corollary` | 274 | Verdier involution preserves MC elements |
| `thm:thqg-IV-theta-duality` | `theorem` | 300 | Gravitational $S$-duality |
| `cor:thqg-IV-involutivity` | `corollary` | 360 | Involutivity |
| `prop:thqg-IV-fundamental-diagram` | `proposition` | 388 | Fundamental commutative diagram |
| `cor:thqg-IV-twisted-tangent` | `corollary` | 411 | Twisted tangent complex duality |
| `thm:thqg-IV-shadow-duality` | `theorem` | 440 | Shadow duality |
| `prop:thqg-IV-kappa-duality` | `proposition` | 475 | Curvature duality |
| `prop:thqg-IV-cubic-duality` | `proposition` | 539 | Cubic shadow duality |
| `cor:thqg-IV-cubic-gauge-duality` | `corollary` | 575 | Cubic gauge triviality under duality |
| `prop:thqg-IV-quartic-duality` | `proposition` | 593 | Quartic resonance duality |
| `prop:thqg-IV-shadow-algebra-iso` | `proposition` | 650 | Shadow algebra isomorphism |
| `cor:thqg-IV-obstruction-duality` | `corollary` | 677 | Obstruction class duality |
| `cor:thqg-IV-shadow-depth` | `corollary` | 693 | Shadow depth is a duality invariant |
| `thm:thqg-IV-kz-duality` | `theorem` | 755 | Shadow/KZ duality on the affine comparison surface |
| `prop:thqg-IV-bpz-duality` | `proposition` | 793 | BPZ duality from $S$-duality |
| `prop:shadow-connection-s-duality` | `proposition` | 845 | Shadow connection $S$-duality |
| `thm:thqg-IV-local-system-duality` | `theorem` | 916 | Local system duality |
| `prop:thqg-IV-monodromy-duality` | `proposition` | 950 | Monodromy eigenvalue reciprocation |
| `prop:thqg-IV-heisenberg-K` | `proposition` | 1030 | Heisenberg complementarity |
| `thm:thqg-IV-km-K` | `theorem` | 1057 | Affine Kac--Moody complementarity |
| `prop:thqg-IV-bc-bg-K` | `proposition` | 1135 | \texorpdfstring{$bc$--$\beta\gamma$}{bc-betagamma} complementarity |
| `prop:thqg-IV-lattice-K` | `proposition` | 1169 | Lattice complementarity |
| `thm:thqg-IV-virasoro-K` | `theorem` | 1186 | Virasoro complementarity |
| `thm:thqg-IV-w-K` | `theorem` | 1236 | Principal $\mathcal{W}$-algebra complementarity |
| `prop:thqg-IV-conductor-growth` | `proposition` | 1315 | Koszul conductor asymptotics |
| `thm:thqg-IV-exponent-sum` | `theorem` | 1334 | Exponent sum formula |
| `thm:ds-complementarity-tower` | `theorem` | 1459 | DS complementarity tower |
| `cor:level-independence-filtration` | `corollary` | 1590 | Level-independence filtration |
| `thm:sigma-ring-finite-generation` | `theorem` | 1652 | Recursive determination of $(\cA^{\mathrm{sh}})^\sigma$ |
| `thm:thqg-IV-c26` | `theorem` | 1714 | The $c = 26$ degeneration |
| `prop:thqg-IV-c13` | `proposition` | 1773 | The $c = 13$ self-dual point |
| `thm:thqg-IV-critical-degeneration` | `theorem` | 1825 | Critical-level degeneration |
| `prop:thqg-IV-self-dual-classification` | `proposition` | 1883 | Classification of self-dual points |
| `thm:thqg-IV-four-facets` | `theorem` | 1955 | Four-facet decomposition |
| `thm:thqg-IV-free-energy` | `theorem` | 2025 | Scalar free-energy complementarity |
| `cor:thqg-IV-self-dual-generating` | `corollary` | 2067 | Self-dual scalar free energies |
| `prop:thqg-IV-partition-duality` | `proposition` | 2082 | Partition function functional equation |
| `prop:thqg-IV-holographic-datum` | `proposition` | 2171 | Holographic modular Koszul datum under $S$-duality |
| `prop:thqg-IV-naturality` | `proposition` | 2240 | Naturality of $\mathcal{S}$ |
| `prop:thqg-IV-clutching` | `proposition` | 2257 | Clutching compatibility |
| `prop:thqg-IV-spectral-duality` | `proposition` | 2349 | Spectral sequence duality |
| `cor:thqg-IV-e2-duality` | `corollary` | 2368 | $E_2$ duality |
| `cor:thqg-IV-degeneration` | `corollary` | 2375 | Degeneration preservation |
| `thm:thqg-IV-cc-sum` | `theorem` | 2448 | Central charge sum |

#### `chapters/connections/thqg_gravitational_yangian.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-V-collision-lie-compatibility` | `lemma` | 173 | Lie compatibility of the collision filtration |
| `prop:thqg-V-depth-zero` | `proposition` | 219 | Associated graded at depth zero |
| `prop:thqg-V-depth-one` | `proposition` | 257 | Associated graded at depth one |
| `prop:thqg-V-collapse-criterion` | `proposition` | 322 | Collapse criterion from shadow depth |
| `lem:thqg-V-collision-nilpotent` | `lemma` | 395 | Nilpotency of the collision differential |
| `prop:thqg-V-arnold-cohomology` | `proposition` | 418 | Arnold cohomology and collision forms |
| `prop:thqg-V-poincare-collision` | `proposition` | 487 | Poincar\'e polynomial of the collision filtration |
| `thm:thqg-V-collision-twisting` | `theorem` | 582 | Collision residue = twisting morphism, revisited |
| `comp:thqg-V-heisenberg-r` | `computation` | 648 | Heisenberg $r$-matrix |
| `comp:thqg-V-affine-r` | `computation` | 698 | Affine Kac--Moody $r$-matrix |
| `comp:thqg-V-virasoro-r` | `computation` | 754 | Virasoro $r$-matrix |
| `prop:thqg-V-gravitational-propagator` | `proposition` | 879 | Gravitational propagator from collision residue |
| `thm:thqg-V-cybe-from-arnold` | `theorem` | 1023 | CYBE from the Arnold relation via MC |
| `cor:thqg-V-ibr` | `corollary` | 1150 | Infinitesimal braid relation |
| `prop:thqg-V-ainfty-ybe` | `proposition` | 1194 | $A_\infty$-enhancement of the CYBE |
| `prop:thqg-V-n-point-ybe-proof` | `proposition` | 1271 | $n$-point YBE from boundary of $\overline{\mathcal{M}}_{0,n+1}$ |
| `prop:thqg-V-yangian-differential` | `proposition` | 1393 | Differential structure |
| `thm:thqg-V-pro-mc-element` | `theorem` | 1436 | Formal genus-refined binary shadow series $R^{\mathrm{bin}}_\cA$ |
| `cor:thqg-V-genus-zero-r` | `corollary` | 1466 | Genus-$0$ component = classical $r$-matrix |
| `prop:thqg-V-pro-mc-convergence` | `proposition` | 1564 | Formal \texorpdfstring{$\hbar$}{hbar}-adic convergence of the candidate binary shadow series |
| `prop:thqg-V-rtt-from-sgybe` | `proposition` | 1637 | RTT relation from the genus-zero collision YBE |
| `comp:thqg-V-three-graviton` | `computation` | 1797 | Three-graviton vertex |
| `comp:thqg-V-quartic-graviton` | `computation` | 1838 | Quartic graviton vertex and contact invariant |
| `prop:thqg-V-verma-gravitational` | `proposition` | 1898 | Verma modules as gravitational representations |
| `prop:thqg-V-c13-self-duality` | `proposition` | 1970 | Self-duality of the gravitational Yangian at $c = 13$ |
| `thm:thqg-V-mc3-thick-generation` | `theorem` | 2104 | Type-$A$ MC3 reduction via the gravitational Yangian |
| `cor:thqg-V-dk5-type-a` | `corollary` | 2143 | Type-$A$ DK-5 reduction to the compact-completion packet |
| `comp:thqg-V-heis-yangian` | `computation` | 2307 | Gravitational Yangian of Heisenberg |
| `comp:thqg-V-affine-yangian` | `computation` | 2327 | Gravitational Yangian of affine KM |
| `comp:thqg-V-vir-yangian-summary` | `computation` | 2349 | Gravitational Yangian of $\mathrm{Vir}_c$ |

#### `chapters/connections/thqg_holographic_reconstruction.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:obstruction-extension-sequence` | `proposition` | 133 | Obstruction-extension sequence |
| `thm:shadow-depth-dichotomy` | `theorem` | 205 | Shadow depth dichotomy |
| `cor:mittag-leffler-shadow-tower` | `corollary` | 311 | Mittag--Leffler for the shadow tower |
| `thm:gaussian-rmax-two` | `theorem` | 409 | $r_{\max}(\mathcal{H}_k) = 2$ |
| `thm:lie-rmax-three` | `theorem` | 539 | $r_{\max}(\widehat{\mathfrak{g}}_k) = 3$ |
| `thm:contact-rmax-four` | `theorem` | 740 | $r_{\max}(\beta\gamma) = 4$ |
| `thm:virasoro-rmax-infinity` | `theorem` | 895 | $r_{\max}(\mathrm{Vir}_c) = \infty$ |
| `comp:virasoro-tower-data` | `computation` | 919 | Virasoro tower data |
| `comp:virasoro-jet-dimensions` | `computation` | 1150 | Virasoro jet space dimensions |
| `thm:jet-space-polynomial-growth` | `theorem` | 1236 | Polynomial growth of Virasoro jet spaces |
| `prop:virasoro-shadow-coefficients` | `proposition` | 1322 | Virasoro shadow coefficients, cubic-source approximation |
| `cor:shadow-asymptotic-decay` | `corollary` | 1396 | Asymptotic shadow decay |
| `comp:virasoro-shadow-table` | `computation` | 1450 | Virasoro shadow coefficients through arity~$10$, cubic-source approximation |
| `prop:wn-class-m` | `proposition` | 1584 | $\Walg_N$ is class~\textbf{M} for $N \geq 2$ |
| `prop:postnikov-filtration-structure` | `proposition` | 1646 | Structure of the Postnikov filtration |
| `prop:mc-formal-moduli` | `proposition` | 1691 | The MC moduli as a formal moduli problem |
| `thm:holographic-reconstruction` | `theorem` | 1736 | Finite-order shadow reconstruction theorem |
| `prop:shapovalov-shadow-singularities` | `proposition` | 1864 | Shapovalov singularities of the shadow tower |
| `prop:pole-structure-shadow-series` | `proposition` | 1909 | Pole structure of the full shadow series |
| `comp:shapovalov-zeros-shadow` | `computation` | 1964 | Shapovalov zeros and shadow singularities |
| `thm:complexity-hierarchy` | `theorem` | 2046 | Complexity hierarchy |

#### `chapters/connections/thqg_introduction_supplement_body.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `conj:thqg-intro-operadic-complexity` | `theorem` | 855 | Operadic complexity; ; Theorem~\ref{thm:operadic-complexity} |

#### `chapters/connections/thqg_modular_bootstrap.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-VII-genus-g-mc` | `proposition` | 292 | Genus-$g$ MC equation |
| `prop:thqg-VII-genus0` | `proposition` | 465 | Genus-$0$ MC equation |
| `prop:thqg-VII-genus1` | `proposition` | 487 | Genus-$1$ MC equation |
| `prop:thqg-VII-genus2` | `proposition` | 518 | Genus-$2$ MC equation |
| `prop:thqg-VII-genus3` | `proposition` | 563 | Genus-$3$ MC equation |
| `prop:thqg-VII-genus4` | `proposition` | 594 | Genus-$4$ MC equation |
| `thm:thqg-VII-contracting-homotopy` | `theorem` | 754 | Contracting homotopy |
| `thm:thqg-VII-uniqueness` | `theorem` | 900 | Uniqueness up to gauge |
| `prop:thqg-VII-genus1-solution` | `proposition` | 945 | Genus-$1$ solution |
| `comp:thqg-VII-genus2` | `computation` | 995 | Genus-$2$ MC recursion |
| `thm:thqg-VII-genus-ss` | `theorem` | 1128 | Genus spectral sequence for the bootstrap |
| `prop:thqg-VII-E1-koszul` | `proposition` | 1241 | $E_1$~page for a Koszul algebra |
| `thm:thqg-VII-ss-convergence` | `theorem` | 1294 | Convergence of the genus spectral sequence |
| `cor:thqg-VII-gaussian-degeneration` | `corollary` | 1329 | Degeneration for Gaussian algebras |
| `prop:thqg-VII-mixed-nondegeneration` | `proposition` | 1363 | Non-degeneration for mixed-type algebras |
| `thm:thqg-VII-ss-shadow-obstruction` | `theorem` | 1398 | Spectral sequence differentials as shadow obstructions |
| `thm:thqg-VII-mc-vs-bootstrap` | `theorem` | 1487 | MC recursion vs.\ conformal bootstrap |
| `thm:thqg-VII-crossing-from-mc` | `theorem` | 1554 | Crossing symmetry from the MC equation |
| `cor:thqg-VII-genus-g-bootstrap` | `corollary` | 1618 | Genus-$g$ bootstrap from MC |
| `prop:thqg-VII-bootstrap-gap` | `proposition` | 1699 | The bootstrap gap |
| `comp:thqg-VII-heis-g0` | `computation` | 1798 | Genus-$0$ Heisenberg |
| `comp:thqg-VII-heis-g1` | `computation` | 1829 | Genus-$1$ Heisenberg |
| `comp:thqg-VII-heis-g2` | `computation` | 1877 | Genus-$2$ Heisenberg |
| `comp:thqg-VII-heis-g3` | `computation` | 1974 | Genus-$3$ Heisenberg |
| `comp:thqg-VII-heis-g4` | `computation` | 2047 | Genus-$4$ Heisenberg |
| `thm:thqg-VII-recursion-closed` | `theorem` | 2171 | Recursion reproduces the closed form |
| `cor:thqg-VII-rank-d` | `corollary` | 2247 | Rank-$d$ Heisenberg |
| `thm:thqg-VII-one-loop-gravity` | `theorem` | 2505 | Genus-\texorpdfstring{$1$}{1} scalar term from \texorpdfstring{$\Theta^{(1)}$}{Theta(1)} |
| `thm:thqg-VII-g-loop-amplitude` | `theorem` | 2547 | Integrated genus-\texorpdfstring{$g$}{g} MC functional |
| `thm:thqg-VII-non-renormalization` | `theorem` | 2599 | Scalar genus expansion for Gaussian algebras |
| `prop:thqg-VII-complexity-bounds` | `proposition` | 2678 | Complexity bounds on genus-\texorpdfstring{$g$}{g} integrand classes |
| `thm:thqg-VII-depth-classification` | `theorem` | 2781 | Shadow depth classifies gravitational theories |

#### `chapters/connections/thqg_open_closed_realization.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-brace-dg-algebra` | `theorem` | 172 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | 325 | Universal open/closed pair (chiral Swiss-cheese theorem) |
| `thm:thqg-local-global-bridge` | `theorem` | 419 | Local-global bridge |
| `thm:thqg-annulus-trace` | `theorem` | 520 | Annulus trace theorem |
| `prop:thqg-annulus-degeneration-kappa` | `proposition` | 792 | Annulus degeneration and the genus-$1$ curvature |
| `thm:thqg-oc-mc-equation` | `theorem` | 867 | Open/closed MC equation |
| `thm:thqg-oc-projection` | `theorem` | 928 | Open/closed projection principle |
| `thm:thqg-mc-forced-consistency` | `theorem` | 987 | MC-forced open-closed consistency |
| `thm:thqg-oc-quartic-vanishing` | `theorem` | 1141 | Vanishing and nonvanishing of $\mathfrak{R}^{\mathrm{oc}}_{4}$ |

#### `chapters/connections/thqg_perturbative_finiteness.tex` (36)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-I-completeness` | `lemma` | 80 | Completeness and separability |
| `prop:thqg-I-inclusion-maps` | `proposition` | 90 | Inclusion maps |
| `lem:thqg-I-schatten` | `lemma` | 131 | Schatten class hierarchy |
| `prop:thqg-I-uniform-trace-bound` | `proposition` | 371 | Uniform bound on the trace |
| `cor:thqg-I-genus-g-partition` | `corollary` | 385 | Genus-$g$ partition function |
| `thm:thqg-I-absolute-convergence` | `theorem` | 587 | Absolute convergence of the scalar generating function on the scalar lane |
| `prop:thqg-I-Fg-values` | `proposition` | 642 | Shadow free energies through genus $10$ on the scalar lane |
| `prop:thqg-I-partial-sums` | `proposition` | 712 | Cumulative partial sums |
| `thm:thqg-I-perturbative-finiteness` | `theorem` | 778 | Perturbative finiteness of twisted gravity |
| `prop:thqg-I-koszulness-finiteness` | `proposition` | 840 | Koszulness and finiteness |
| `prop:thqg-I-graph-count` | `proposition` | 863 | Effective graph count |
| `prop:thqg-I-genus-g-decomposition` | `proposition` | 879 | Genus-$g$ amplitude decomposition |
| `prop:thqg-I-exponential-rep` | `proposition` | 1049 | Exponential representation |
| `prop:thqg-I-heisenberg-detail` | `proposition` | 1128 | Heisenberg: detailed HS verification |
| `prop:thqg-I-affine-detail` | `proposition` | 1146 | Affine Kac--Moody: detailed HS verification |
| `prop:thqg-I-virasoro-detail` | `proposition` | 1165 | Virasoro: detailed HS verification |
| `prop:thqg-I-convergence-radii` | `proposition` | 1186 | Convergence radii of the scalar partition function |
| `thm:thqg-I-btz` | `theorem` | 1312 | BTZ-normalized scalar shadow series |
| `prop:thqg-I-btz-higher-genus` | `proposition` | 1360 | Higher-genus BTZ-normalized scalar coefficients |
| `prop:thqg-I-1c-expansion` | `proposition` | 1432 | Leading gravitational coupling expansion of the reduced scalar series |
| `prop:thqg-I-newton-expansion` | `proposition` | 1466 | Newton's constant expansion |
| `prop:thqg-I-graph-sum-sewing` | `proposition` | 1609 | Graph-sum representation of sewing amplitudes |
| `prop:thqg-I-graph-sum-convergence` | `proposition` | 1629 | Convergence of the graph sum at fixed genus |
| `prop:thqg-I-consistency` | `proposition` | 1658 | Parallel analytic and algebraic finiteness |
| `thm:thqg-I-full-convergence` | `theorem` | 1707 | Full partition function at fixed genus and on the Gaussian lane |
| `prop:thqg-I-hs-filtration` | `proposition` | 1790 | HS-sewing and the strong filtration |
| `prop:thqg-I-effective-bound` | `proposition` | 1812 | Effective bound on the genus-$g$ scalar free energy on the scalar lane |
| `cor:thqg-I-tail-bound` | `corollary` | 1835 | Tail bound for the scalar genus expansion on the scalar lane |
| `thm:thqg-I-2d-convergence` | `theorem` | 1871 | Fixed-genus arity convergence and Gaussian two-parameter convergence |
| `cor:thqg-I-heisenberg-selberg` | `corollary` | 1995 | Heisenberg partition function via Selberg zeta |
| `prop:polyakov-chern-weil` | `proposition` | 2054 | Polyakov formula as Chern--Weil image of the arity-$2$ shadow |
| `prop:thqg-I-pole-structure` | `proposition` | 2108 | Pole structure of the meromorphic continuation |
| `prop:thqg-I-tensor-product` | `proposition` | 2224 | Finiteness for tensor-product theories |
| `comp:thqg-I-fp-detailed` | `computation` | 2287 | Faber--Pandharipande coefficients through genus $15$ |
| `prop:thqg-I-asymptotic-precision` | `proposition` | 2322 | Asymptotic precision |
| `prop:thqg-I-fp-monotone` | `proposition` | 2338 | Monotonicity of the FP coefficients |

#### `chapters/connections/thqg_soft_graviton_theorems.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-VI-arity-decomposition` | `proposition` | 228 | Arity decomposition of the shadow connection |
| `thm:thqg-VI-flatness-by-arity` | `theorem` | 271 | Flatness by arity |
| `thm:thqg-VI-ward-determines-correlators` | `theorem` | 432 | Shadow Ward identities determine correlators |
| `prop:thqg-VI-kappa-action` | `proposition` | 576 | Action of $\kappa$ on conformal blocks |
| `thm:thqg-VI-leading-soft` | `theorem` | 631 | Leading soft graviton theorem |
| `cor:thqg-VI-bms-supertranslation` | `corollary` | 721 | BMS supertranslation Ward identity |
| `prop:thqg-VI-cubic-action` | `proposition` | 789 | Cubic shadow action on conformal blocks |
| `thm:thqg-VI-subleading-soft` | `theorem` | 831 | Subleading soft graviton theorem |
| `thm:thqg-VI-cubic-gauge-triviality` | `theorem` | 909 | Cubic gauge triviality and subleading soft theorems |
| `cor:thqg-VI-superrotation` | `corollary` | 982 | Superrotation Ward identity |
| `prop:thqg-VI-quartic-action` | `proposition` | 1082 | Quartic shadow action on conformal blocks |
| `thm:thqg-VI-virasoro-quartic` | `theorem` | 1118 | Virasoro quartic contact coefficient |
| `thm:thqg-VI-clutching-law` | `theorem` | 1245 | Clutching law for the quartic contact invariant |
| `comp:thqg-VI-virasoro-clutching` | `computation` | 1333 | Clutching law for Virasoro |
| `thm:thqg-VI-sub-subleading-soft` | `theorem` | 1372 | Sub-subleading soft graviton theorem |
| `thm:thqg-VI-general-soft` | `theorem` | 1481 | General arity-$r$ soft graviton theorem |
| `cor:thqg-VI-soft-recursion` | `corollary` | 1530 | Soft factor recursion |
| `thm:thqg-VI-quintic-forced` | `theorem` | 1556 | The Virasoro quintic shadow is forced |
| `comp:thqg-VI-virasoro-quintic-soft` | `computation` | 1681 | Quintic soft factor for Virasoro |
| `prop:thqg-VI-inductive-nontermination` | `proposition` | 1716 | Inductive non-termination for class $\mathbf{M}$ |
| `prop:thqg-VI-polynomial-growth` | `proposition` | 1796 | Polynomial growth of soft factors |
| `cor:thqg-VI-soft-convergence` | `corollary` | 1845 | Convergence of the soft expansion |
| `prop:thqg-VI-celestial-structure` | `proposition` | 1912 | Structure of the celestial soft algebra |
| `thm:thqg-VI-soft-ope` | `theorem` | 1992 | Soft graviton OPE |
| `prop:thqg-VI-asymptotic-symmetry` | `proposition` | 2063 | Asymptotic symmetry algebra from the shadow tower |

#### `chapters/connections/thqg_symplectic_polarization.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-III-ambient-properties` | `proposition` | 126 | Properties of the holographic ambient complex |
| `prop:thqg-III-involutivity` | `proposition` | 237 | Involutivity and anti-symmetry |
| `prop:thqg-III-mc-compatibility` | `proposition` | 297 | Compatibility with the modular MC element |
| `lem:thqg-III-nondegeneracy` | `lemma` | 386 | Nondegeneracy of the holographic pairing |
| `prop:thqg-III-degree-shift` | `proposition` | 419 | Degree shift at each genus |
| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 472 | Holographic eigenspace decomposition (C1) |
| `cor:thqg-III-complementarity-exchange` | `corollary` | 653 | Complementarity exchange principle |
| `cor:thqg-III-dimension-parity` | `corollary` | 676 | Dimension parity |
| `prop:thqg-III-genus-0` | `proposition` | 692 | Genus-$0$ complementarity |
| `prop:thqg-III-genus-1` | `proposition` | 717 | Genus-$1$ complementarity |
| `prop:thqg-III-compatibility` | `proposition` | 1097 | Compatibility of the BV antibracket with the Verdier pairing |
| `thm:thqg-III-genus-1-holographic` | `theorem` | 1435 | Holographic complementarity at genus $1$ |
| `thm:thqg-III-landscape-census` | `theorem` | 1706 | Standard landscape complementarity census |
| `prop:thqg-III-genus-2` | `proposition` | 1881 | Genus-$2$ complementarity dimensions |
| `prop:thqg-III-independent-sum` | `proposition` | 1922 | Independent sum factorization |
| `thm:thqg-III-universality` | `theorem` | 2023 | Universality of the complementarity package |

#### `chapters/connections/twisted_holography_quantum_gravity.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-g1-finiteness` | `theorem` | 121 | \textbf{G1}: Perturbative finiteness |
| `thm:thqg-g2-complexity` | `theorem` | 132 | \textbf{G2}: Shadow-depth classification |
| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
| `thm:thqg-g4-s-duality` | `theorem` | 161 | \textbf{G4}: Gravitational $S$-duality |
| `thm:thqg-g5-yangian` | `theorem` | 173 | \textbf{G5}: Gravitational Yangian |
| `thm:thqg-g6-soft-graviton` | `theorem` | 187 | \textbf{G6}: Soft graviton theorems |
| `thm:thqg-g7-bootstrap` | `theorem` | 210 | \textbf{G7}: Modular bootstrap |
| `thm:thqg-g8-reconstruction` | `theorem` | 227 | \textbf{G8}: Holographic reconstruction |
| `thm:thqg-g9-critical-string` | `theorem` | 244 | \textbf{G9}: Critical string dichotomy |
| `thm:thqg-g10-fredholm` | `theorem` | 267 | \textbf{G10}: Partition function convergence |
| `thm:thqg-g14-error-correction` | `theorem` | 320 | \textbf{G14}: Holographic code structure |
| `thm:thqg-g15-page` | `theorem` | 333 | \textbf{G15}: Algebraic Page constraint |
| `thm:thqg-dependency` | `theorem` | 357 | Dependency theorem |

#### `chapters/connections/ym_boundary_theory.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ym-bar-bridge` | `theorem` | 47 | Bridge theorem: boundary chiral algebra $\to$ visible center via bar-cobar |
| `thm:twisted-ym-boundary-brst` | `theorem` | 209 | Boundary BRST recovery for twisted Yang--Mills data |
| `thm:twisted-ym-tangent-center` | `theorem` | 235 | Tangent-to-center principle |
| `cor:twisted-ym-center-rigidity` | `corollary` | 254 | Center-vanishing rigidity criterion |
| `cor:twisted-ym-one-parameter` | `corollary` | 264 | One-parameter criterion |
| `thm:twisted-ym-tangent-factors-through-center` | `theorem` | 286 | The tangent functor factors through the dual center |
| `cor:twisted-ym-interface-invariance` | `corollary` | 312 | Interface invariance of tangent data |
| `cor:twisted-ym-center-comparison` | `corollary` | 330 | Comparison without full boundary equivalence |
| `thm:twisted-ym-dual-unobstructedness` | `theorem` | 372 | Dual unobstructedness criterion |
| `thm:twisted-ym-central-formality` | `theorem` | 395 | Central formality theorem |
| `lem:twisted-ym-center-tensor` | `lemma` | 455 | Center of a chiral tensor product |
| `thm:twisted-ym-binary-mixed-couplings` | `theorem` | 493 | Binary mixed-coupling theorem |
| `cor:twisted-ym-multibody-couplings` | `corollary` | 558 | Multi-body coupling expansion |
| `cor:twisted-ym-mixed-rigidity` | `corollary` | 592 | Mixed rigidity criterion |

#### `chapters/connections/ym_higher_body_couplings.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:relative-duality-theorem` | `theorem` | 86 | Relative duality theorem |
| `cor:relative-tangent-center-principle` | `corollary` | 136 | Relative tangent-to-center principle |
| `cor:relative-dual-unobstructedness` | `corollary` | 147 | Relative dual unobstructedness |
| `thm:relative-central-formality` | `theorem` | 166 | Relative central formality |
| `lem:mixed-ks-well-defined` | `lemma` | 216 | Well-definedness and invariance |
| `thm:first-correction-theorem` | `theorem` | 225 | First-correction theorem |
| `cor:persistence-criterion-quadratic-law` | `corollary` | 255 | Persistence criterion for the quadratic law |
| `thm:universal-interaction-brackets` | `theorem` | 268 | Universal interaction brackets on mixed couplings |
| `lem:w-boundary-simplex-homotopy-invariance` | `lemma` | 371 | Homotopy invariance |
| `thm:w-boundary-cech-duality` | `theorem` | 392 | Higher-body \v{C}ech duality |
| `thm:w-augmented-center-tensor-model` | `theorem` | 465 | Tensor-product model for the augmented center complex |
| `cor:w-pure-mbody-coupling-theorem` | `corollary` | 522 | Pure $m$-body coupling theorem |
| `thm:w-higher-mayer-vietoris-couplings` | `theorem` | 539 | Higher Mayer--Vietoris descent for couplings |
| `thm:w-filtered-stability-pure-mbody` | `theorem` | 581 | Filtered stability of pure $m$-body couplings |

#### `chapters/connections/ym_instanton_screening.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:novikov-completion-theorem` | `theorem` | 95 | Novikov completion theorem |
| `thm:instanton-completed-tangent-center` | `theorem` | 156 | Instanton-completed tangent-to-center principle |
| `thm:screened-tangent-center` | `theorem` | 221 | Screened tangent-to-center principle |
| `prop:koszul-identification-visible-center` | `proposition` | 262 | Koszul identification of the visible center |
| `thm:instanton-screening-spectral-sequence` | `theorem` | 288 | Instanton-screening spectral sequence |
| `thm:central-localization-confinement` | `theorem` | 332 | Central localization criterion for confinement |
| `thm:screened-cech-duality` | `theorem` | 384 | Higher-body \v{C}ech duality after screening |
| `thm:screening-hodge-theorem` | `theorem` | 447 | Screening Hodge theorem |
| `cor:screening-spectral-gap-criterion` | `corollary` | 473 | Screening spectral gap criterion |
| `cor:stable-untwisting-bounded-error` | `corollary` | 526 | Stable untwisting under bounded error |
| `prop:internal-screening-form` | `proposition` | 620 | Operator-algebraic meaning of the screening form |
| `thm:mass-gap-reduction-internal-screening` | `theorem` | 696 | Mass-gap reduction to an internal screening estimate |
| `cor:exact-reduction-screening-estimate` | `corollary` | 730 | Exact formulation of the reduction principle |

### Appendices (285)

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
| `prop:scalar-mc-skeleton` | `proposition` | 174 | The scalar shadow is an abelian MC element |
| `thm:spectral-cumulant-hierarchy` | `theorem` | 233 | Spectral cumulant hierarchy |
| `thm:first-obstruction-traceless-quadratic` | `theorem` | 315 | First obstruction is traceless and quadratic |
| `cor:filtered-lift-vanishing` | `corollary` | 388 | Vanishing criterion for filtered lifts |
| `lem:positive-weight-contraction` | `lemma` | 456 | Positive-weight contraction |
| `thm:vir-positive-weight-acyclic` | `theorem` | 473 | Positive-weight Virasoro sectors are acyclic |
| `cor:vir-localization-reduced-spectral` | `corollary` | 492 | Localization to reduced spectral sectors |
| `prop:odd-sheet-rigidity` | `proposition` | 520 | Odd-sheet rigidity for one-line reductions |
| `cor:mu2-centered-at-13` | `corollary` | 561 | The genus-\(2\) one-line coefficient is centered at \texorpdfstring{$13$}{13} |
| `lem:universal-branch-moments` | `lemma` | 624 | Universal branch moments |
| `thm:hodge-depth-formula` | `theorem` | 686 | Depth formula |
| `lem:separating-hodge-splitting` | `lemma` | 719 | Separating Hodge splitting |
| `lem:nonseparating-hodge-extension` | `lemma` | 761 | Nonseparating Hodge extension |
| `thm:genus-two-transparency` | `theorem` | 800 | Genus-\(2\) transparency on a one-line branch quotient |
| `cor:vir-genus-two-vanishing` | `corollary` | 844 | Virasoro genus-\(2\) coefficient vanishes in the one-line quotient |
| `cor:first-primitive-genus-three` | `corollary` | 856 | The first primitive traceless coefficient begins in genus \texorpdfstring{$3$}{3} |
| `lem:genus-three-rose-unique` | `lemma` | 874 | Uniqueness of the primitive rose in genus \texorpdfstring{$3$}{3} |
| `thm:pure-branch-primitive-coefficient` | `theorem` | 904 | Pure-branch primitive coefficient on a rank-two sheet |
| `thm:first-primitive-top-hodge-layer` | `theorem` | 999 | First primitive top-Hodge layer |
| `cor:genus-three-primitive-top-hodge` | `corollary` | 1036 | The genus-\(3\) primitive coefficient |
| `cor:shared-sheet-universal-coefficients` | `corollary` | 1108 | Universal coefficients on the shared sheet |

#### `appendices/casimir_divisor_core_transport.tex` (27)

| Label | Env | Line | Title |
|---|---|---:|---|
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:66` | `proposition` | 66 | Universal property |
| `thm:divisor-core-calculus` | `theorem` | 109 | Divisor-core calculus |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:190` | `corollary` | 190 | Divisors classify submodules |
| `thm:hom-equals-gcd` | `theorem` | 212 | Hom \(=\) gcd |
| `thm:factorization-through-common-core` | `theorem` | 274 | Universal factorization through the maximal common core |
| `cor:spectral-defects` | `corollary` | 311 | Spectral defects |
| `thm:primary-jordan-filtration` | `theorem` | 350 | Primary Jordan filtration |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:387` | `corollary` | 387 | Repeated roots are extension data |
| `thm:squarefree-sheet` | `theorem` | 411 | Squarefree spectral sheet theorem |
| `prop:coprime-functional-calculus` | `proposition` | 438 | Coprime-locus functional calculus |
| `prop:no-projector` | `proposition` | 467 | No universal polynomial projector off the coprime locus |
| `thm:minimal-intrinsic-realization` | `theorem` | 540 | Minimal intrinsic realization |
| `lem:generic-separator` | `lemma` | 588 | Generic Casimir separator |
| `thm:casimir-moment-reconstruction` | `theorem` | 614 | Casimir moment reconstruction |
| `cor:finite-scalar-probes` | `corollary` | 665 | Finite scalar probes suffice |
| `thm:pbw-recurrence` | `theorem` | 745 | PBW recurrence theorem for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} |
| `thm:growth-mode-factorization` | `theorem` | 875 | Growth-mode factorization for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} |
| `cor:growth-ds-divisor-cores` | `corollary` | 937 | Divisor-core interpretation of the factorization |
| `thm:sector-determinant` | `theorem` | 1015 | Characteristic polynomial of a sector |
| `thm:common-core-exact-sequences` | `theorem` | 1064 | Common-core exact sequences |
| `prop:transport-factors-through-common-core` | `proposition` | 1088 | Shift-compatible transport factors through the common core |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1111` | `corollary` | 1111 | Corrected transport principle |
| `prop:squarefree-common-sector` | `proposition` | 1121 | Squarefree common-sector rigidity |
| `prop:sl3-w3-defect` | `proposition` | 1203 | Exact defect decomposition for \(\widehat{\mathfrak{sl}}_3/W_3\) |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1225` | `corollary` | 1225 | All transport maps factor through the quadratic core |
| `prop:explicit-sl3-projectors` | `proposition` | 1244 | Explicit coprime-locus projectors |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1327` | `proposition` | 1327 | The \(L_1\)--\(L_2\) package on the one-channel squarefree locus |

#### `appendices/coderived_models.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 243 | Adequacy |
| `thm:stratified-conservative-restriction` | `theorem` | 578 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 654 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 704 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 731 | Factorization co-contra correspondence |
| `thm:off-koszul-ran-inversion` | `theorem` | 825 | Off-Koszul bar-cobar inversion on Ran |

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-pade` | `proposition` | 894 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dg_shifted_factorization_bridge.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-additive-kz` | `theorem` | 144 | Derived additive KZ connection |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:200` | `corollary` | 200 | Derived Drinfeld--Kohno shadow |
| `thm:boundary-residue` | `theorem` | 210 | Boundary residue theorem |
| `thm:transfer-flat-spectral` | `theorem` | 252 | Transfer of flat spectral connections |
| `thm:quasi-factorization` | `theorem` | 319 | Quasi-factorization theorem |
| `thm:strictification-spectral-cohomology` | `theorem` | 378 | Strictification by spectral cohomology |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:423` | `proposition` | 423 | Quadratic hexagon obstruction |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:452` | `proposition` | 452 | Three-particle obstruction identity |
| `thm:abelian-strictification` | `theorem` | 490 | Abelian strictification theorem |
| `thm:residue-bounded-completion` | `theorem` | 510 | Residue-bounded completion theorem |
| `prop:cartan-shift-cocycle` | `proposition` | 563 | Cartan shift cocycle identities |
| `thm:cartan-gauge-twist` | `theorem` | 581 | Cartan gauge-twist theorem |
| `thm:cartan-diagonal-defect-exact` | `theorem` | 624 | Cartan-diagonal shift defect is exact |
| `thm:triangle-localization` | `theorem` | 696 | Triangle localization formula |
| `thm:adjacent-root-rigidity` | `theorem` | 758 | Adjacent-root rigidity |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:777` | `corollary` | 777 | Normalized rational triangle coefficient |
| `prop:triangle-shift-transport` | `proposition` | 822 | Triangle shift transport law |
| `lem:free-closed-generating-kernel` | `lemma` | 873 | Closed generating kernel |
| `thm:exact-free-transport` | `theorem` | 903 | Exact free two-body transport |
| `lem:class3-ordered-bch` | `lemma` | 977 | Class-$3$ ordered BCH coefficient |
| `thm:quadrilateral-localization` | `theorem` | 1012 | Quadrilateral localization formula |
| `thm:quadrilateral-rigidity` | `theorem` | 1104 | Quadrilateral rigidity |
| `cor:quadrilateral-normalized-rational` | `corollary` | 1132 | Normalized rational quadrilateral coefficient |
| `prop:quadrilateral-shift-transport` | `proposition` | 1168 | Quadrilateral shift transport law |
| `cor:no-new-filtration3-shift-obstruction` | `corollary` | 1198 | No new independent shift obstruction in filtration $3$ |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:1233` | `theorem` | 1233 | Conditional strictification criterion |

#### `appendices/dual_methodology.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-infty-operads` | `theorem` | 158 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |

#### `appendices/existence_criteria.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:classification-table` | `proposition` | 453 | Classification table \cite{FBZ04, BD04} |
| `prop:w-algebra-koszul` | `proposition` | 531 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul analysis |

#### `appendices/homotopy_transfer.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:htt-rectification` | `proposition` | 15 | Homotopy transfer as rectification mechanism |
| `lem:sdr-existence` | `lemma` | 146 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 455 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 521 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 615 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 731 | Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0} |

#### `appendices/koszul_reference.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:extended-koszul-appendix` | `theorem` | 17 | Extended Koszul duality |
| `thm:genus-graded-koszul-duality-appendix` | `theorem` | 73 | Genus-graded Koszul duality theorem |
| `lem:genus-graded-koszul-resolution-appendix` | `lemma` | 110 | Genus-graded Koszul complex resolution |
| `thm:genus-graded-mc-appendix` | `theorem` | 131 | Genus-graded MC elements parametrize deformations |
| `thm:essential-image-koszul` | `theorem` | 261 | Essential image of Koszul duality |
| `lem:conilpotency-necessary` | `lemma` | 323 | Conilpotency is necessary |
| `lem:connectedness-augmentation` | `lemma` | 352 | Connectedness characterizes augmentation |
| `thm:koszul-geom-rep` | `theorem` | 381 | Koszul duals are geometrically representable |
| `cor:geom-implies-koszul` | `corollary` | 413 | Converse: geometric representability implies Koszul |
| `thm:curvature-central-appendix` | `theorem` | 463 | Curvature must be central |
| `thm:uniqueness-algebra` | `theorem` | 616 | Uniqueness up to quasi-isomorphism |

#### `appendices/nilpotent_completion.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:geom-conilpotent` | `proposition` | 91 | Geometric manifestation |
| `thm:completion-convergence` | `theorem` | 119 | Completion convergence |
| `thm:completed-bar-cobar` | `theorem` | 191 | Completed bar-cobar duality |
| `thm:koszul-dual-characterization` | `theorem` | 251 | Characterization of Koszul duals |
| `thm:stabilized-completion-positive` | `theorem` | 561 | Stabilized completion for positive towers |
| `thm:resonance-filtered-bar-cobar` | `theorem` | 672 | Resonance-filtered completed bar/cobar |
| `prop:resonance-ss-degeneration` | `proposition` | 776 | Resonance spectral sequence degeneration |
| `prop:resonance-ranks-standard` | `proposition` | 803 | Resonance ranks of the standard families |
| `cor:virasoro-resonance-ss` | `corollary` | 871 | Virasoro resonance spectral sequence |
| `conj:platonic-completion` | `theorem` | 944 | Platonic completion |

#### `appendices/nonlinear_modular_shadows.tex` (75)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:nms-mc-principle` | `theorem` | 179 | Algebra structure $=$ Maurer--Cartan element |
| `prop:shadow-linfty-obstruction` | `proposition` | 212 | Genus-$0$ shadow tower as $L_\infty$ formality obstruction tower |
| `prop:nms-five-component` | `proposition` | 314 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | 374 | Shadow tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | 414 | All families from universal evaluation |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | 507 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | 561 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | 607 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | 616 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | 637 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | 652 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | 751 | Quartic shadow master equations |
| `thm:nms-separating-boundary-recursion` | `theorem` | 790 | Separating boundary recursion through quartic order |
| `thm:nms-shadow-cocycle-characterization` | `theorem` | 852 | Finite-order realization of the universal class |
| `prop:nms-quartic-closure-envelope` | `proposition` | 903 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | 933 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | 953 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | 992 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | 1016 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | 1097 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | 1121 | Vanishing of the quartic contact invariant |
| `cor:nms-betagamma-boundary-law` | `corollary` | 1145 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | 1162 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | 1190 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | 1232 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | 1270 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | 1298 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | 1370 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | 1426 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `thm:nms-w3-full-quartic-gram` | `theorem` | 1485 | Full $\mathcal W_3$ quartic Gram determinant |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | 1558 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | 1576 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | 1592 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | 1701 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | 1753 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 1777 | Clutching law for the modular quartic resonance class |
| `thm:nms-first-nonlinear-shadow-theta` | `theorem` | 1851 | The first nonlinear shadow of \texorpdfstring{$\Theta_{\cA}$}{ThetaA} |
| `cor:nms-family-boundary-behavior` | `corollary` | 1864 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | 1933 | Functoriality and duality through quartic order |
| `conj:nms-full-resonance-tower` | `theorem` | 1959 | Full resonance tower |
| `thm:nms-all-arity-master-equation` | `theorem` | 2065 | All-arity master equation |
| `cor:nms-quintic-master-equation` | `corollary` | 2088 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | 2108 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | 2127 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | 2146 | Finite termination for primitive archetypes |
| `thm:nms-all-arity-separating-boundary` | `theorem` | 2171 | All-arity separating boundary recursion |
| `cor:nms-quintic-separating-boundary` | `corollary` | 2187 | Quintic separating boundary recursion |
| `prop:nms-genus-loop-properties` | `proposition` | 2233 | Basic properties of the genus loop operator |
| `thm:nms-nonseparating-clutching-law` | `theorem` | 2250 | Non-separating clutching law for the shadow tower |
| `cor:nms-genus-one-hessian-correction` | `corollary` | 2274 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | 2298 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2373 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2407 | Ambient complementarity and nonlinear modular shadows |
| `conj:nms-all-arity-resonance-boundary` | `theorem` | 2576 | All-arity boundary law for the resonance tower |
| `thm:nms-bipartite-complementarity` | `theorem` | 2777 | Bipartite complementarity principle |
| `thm:nms-bipartite-vanishing` | `theorem` | 2882 | Bipartite vanishing theorem |
| `prop:nms-basis-independence-specialization-restated` | `proposition` | 3170 | Basis independence and specialization |
| `thm:nms-clutching-law-modular-resonance-restated` | `theorem` | 3198 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behaviour` | `corollary` | 3228 | Family-by-family boundary behaviour |
| `thm:nms-genus-loop-model-families-restated` | `theorem` | 3354 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat-restated` | `theorem` | 3422 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary-restated` | `theorem` | 3454 | Ambient complementarity and nonlinear modular shadows |
| `thm:reduced-weight-finiteness` | `theorem` | 3659 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | 3747 | Window locality |
| `cor:exact-stabilization` | `corollary` | 3769 | Exact stabilization |
| `lem:nms-euler-inversion` | `lemma` | 3945 | Euler inversion |
| `prop:kac-shadow-singularity` | `proposition` | 4032 | Kac-shadow singularity principle |
| `thm:ds-shadow-depth-increase` | `theorem` | 4143 | DS shadow depth increase |
| `thm:shadow-subalgebra-autonomy` | `theorem` | 4347 | Shadow subalgebra autonomy |
| `cor:w-line-alternating-vanishing` | `corollary` | 4423 | $W$-line alternating vanishing |
| `thm:nms-shadow-mc-potential` | `theorem` | 4452 | Shadow tower as cyclic $L_\infty$ MC potential |
| `prop:nms-shadow-convergence` | `proposition` | 4516 | Shadow potential convergence |
| `thm:nms-mc-moduli-curve-structure` | `theorem` | 4625 | MC moduli curve structure |
| `thm:nms-hadamard-mc-potential` | `theorem` | 4688 | Hadamard factorization of the MC potential |
| `cor:nms-mc-solution-counting` | `corollary` | 4735 | MC solution counting |

#### `appendices/ordered_associative_chiral_kd.tex` (24)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bicom-e` | `lemma` | 204 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | 287 | Ordered chiral shuffle theorem |
| `thm:opposite` | `theorem` | 392 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | 433 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | 447 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | 458 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | 521 | — |
| `prop:one-defect` | `proposition` | 548 | — |
| `thm:tangent=K` | `theorem` | 570 | Tangent identification |
| `cor:infdual` | `corollary` | 607 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | 630 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | 682 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | 715 | Diagonal correspondence |
| `cor:unit` | `corollary` | 763 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | 781 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | 810 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | 842 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | 868 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | 888 | Cap action |
| `thm:pair-of-pants` | `theorem` | 943 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | 981 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | 1035 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | 1084 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | 1108 | Master theorem |

#### `appendices/shifted_rtt_duality_orthogonal_coideals.tex` (22)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:weightwise-stabilization-bar-complex` | `lemma` | 83 | Weightwise stabilization of the bar complex |
| `thm:stabilized-completed-recovery` | `theorem` | 120 | Stabilized completed bar/cobar recovery |
| `cor:automatic-tower-convergence-positive-degree` | `corollary` | 154 | Automatic tower convergence in positive degree |
| `thm:weightwise-maurer-cartan-descent` | `theorem` | 161 | Weightwise Maurer--Cartan descent |
| `prop:module-comodule-stabilized` | `proposition` | 193 | Module/comodule passage for stabilized towers |
| `thm:trace-theoretic-bar-duality` | `theorem` | 250 | Trace-theoretic bar duality |
| `cor:lagrangian-envelope` | `corollary` | 311 | The Lagrangian envelope |
| `lem:generator-extension-exact-monoidal` | `lemma` | 346 | Generator extension of exact monoidal functors |
| `thm:meromorphic-tannakian-reconstruction` | `theorem` | 382 | Meromorphic Tannakian reconstruction |
| `cor:recognition-compact-boundary-modules` | `corollary` | 430 | Recognition on compact boundary modules |
| `lem:scalar-gauge-invariance-finite-rtt` | `lemma` | 471 | Scalar gauge invariance of finite RTT stages |
| `cor:inverse-kernel-sign-reversal` | `corollary` | 494 | Inverse kernel versus sign reversal |
| `thm:finite-stage-rtt-adjointness` | `theorem` | 536 | Finite-stage RTT bar adjointness |
| `cor:degree-two-twisting-cochain` | `corollary` | 572 | The degree-$2$ twisting cochain |
| `thm:transport-of-finite-rtt-relation-space` | `theorem` | 621 | Transport of the finite RTT relation space |
| `thm:finite-stage-shifted-bar-adjointness` | `theorem` | 647 | Finite-stage shifted bar adjointness |
| `thm:quotient-coideal-descent` | `theorem` | 732 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse-appendix` | `proposition` | 774 | Stage $N=1$ twist is trivial; naive Cartan fixing collapses the root sector |
| `thm:explicit-rank-one-orthogonal-coideal` | `theorem` | 849 | Explicit rank-one orthogonal coideal and curved cobar model |
| `cor:generalized-weyl-normal-form` | `corollary` | 882 | Generalized Weyl normal form |
| `cor:kleinian-associated-graded` | `corollary` | 930 | Kleinian associated graded at the nilpotent point |
| `thm:fortified-frontier-package` | `theorem` | 984 | Fortified frontier package |

#### `appendices/signs_and_shifts.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:graded-jacobi` | `proposition` | 40 | Graded Jacobi identity |
| `prop:duality-grading` | `proposition` | 169 | Duality and grading reversal |
| `prop:susp-diff` | `proposition` | 273 | Suspension and differentials |
| `prop:LV-conversion-complete` | `proposition` | 1076 | Loday--Vallette conversion |

#### `appendices/spectral_higher_genus.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:convergence-criterion-spectral` | `theorem` | 73 | Convergence criterion |

#### `appendices/spectral_sequences.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ss` | `theorem` | 271 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 323 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 387 | Central charge and \texorpdfstring{$d_1$}{d1} |

#### `appendices/subregular_hook_frontier.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:pbw-slodowy-collapse` | `theorem` | 81 | PBW--Slodowy collapse |
| `cor:principal-w-completed-koszul` | `corollary` | 140 | Principal affine \texorpdfstring{$W$}{W}-algebras are completed Koszul |
| `prop:transport-propagation` | `proposition` | 256 | Transport propagation lemma |
| `prop:hook-ghost-constant` | `proposition` | 330 | Hook ghost constant |
| `prop:ds-bar-hook-commutation` | `proposition` | 381 | Hook-type compatibility criteria |
| `thm:canonical-arity-detection` | `theorem` | 473 | Generator-degree detection of canonical arity |
| `thm:full-raw-coefficient-packet` | `theorem` | 621 | Exact Bell recursion for the full singular packet |
| `thm:miura-product-formula` | `theorem` | 779 | Subregular Miura product formula |
| `thm:subregular-appell-formula` | `theorem` | 816 | Subregular Appell formula |
| `thm:bp-strict` | `theorem` | 888 | Bershadsky--Polyakov is strict in canonical normal form |
| `thm:w4-cubic` | `theorem` | 935 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} has canonical arity $3$ |
| `thm:unbounded-canonical-arity` | `theorem` | 1066 | Unbounded canonical arity in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | 1120 | Triangular primary-renormalization theorem |

#### `appendices/typeA_baxter_rees_theta.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:vector-seed-propagation` | `theorem` | 153 | Propagation from the vector seed |
| `lem:equivariant-normal-form` | `lemma` | 212 | Equivariant normal form on $V\otimes V$ |
| `thm:schur-envelope-formula` | `theorem` | 251 | Schur-envelope formula |
| `cor:one-coefficient-forces-reduced-core` | `corollary` | 305 | One ordered coefficient forces the reduced core |
| `thm:pairwise-to-all-point-reconstruction` | `theorem` | 346 | Pairwise-to-all-point reconstruction |
| `prop:weight-stability-algebra-tower` | `proposition` | 439 | Weight-stability of the algebra tower |
| `prop:failure-unweighted-stabilization` | `proposition` | 468 | Failure of unweighted stabilization |
| `lem:weight-stability-bar-tower` | `lemma` | 518 | Weight-stability of the bar tower |
| `thm:weightwise-MC4-principal-RTT` | `theorem` | 553 | Weightwise MC4 for the principal RTT tower |
| `thm:recognition-completed-dg-shifted-yangian` | `theorem` | 603 | Recognition of the completed dg-shifted Yangian |
| `thm:derived-realization-ordinary-asymptotic` | `theorem` | 688 | Derived realization of ordinary asymptotic modules |
| `thm:derived-realization-negative-prefundamental` | `theorem` | 750 | Derived realization of negative prefundamentals |
| `thm:baxter-envelope-criterion` | `theorem` | 796 | Baxter-envelope criterion |
| `thm:algebraicity-baxter-rees-family` | `theorem` | 856 | Algebraicity of the Baxter--Rees family |
| `thm:generic-and-boundary-fibers` | `theorem` | 890 | Generic and boundary fibers |
| `thm:derived-realization-baxter-rees-family` | `theorem` | 931 | Derived realization of the Baxter--Rees family |
| `cor:formal-neighborhood-generated-by-KR` | `corollary` | 967 | Formal neighborhood generated by the compact KR packet |
| `thm:concrete-cocycle-representative` | `theorem` | 1009 | Concrete cocycle representative |
| `lem:weightwise-polynomial-continuation` | `lemma` | 1046 | Weightwise polynomial continuation |
| `thm:continuation-of-polynomial-R-matrices` | `theorem` | 1093 | Continuation of polynomial $R$-matrices to the boundary |
| `thm:continuation-of-theta-associators` | `theorem` | 1159 | Continuation of Theta-associators to the boundary |
| `cor:formal-braided-boundary-germ` | `corollary` | 1204 | Formal braided boundary germ |
| `thm:linearized-boundary-equations` | `theorem` | 1251 | Linearized boundary equations |
| `thm:compact-to-completed-extension-principle` | `theorem` | 1326 | Compact-to-completed extension principle |
| `thm:typeA-reduction-full-derived-DK-frontier` | `theorem` | 1363 | Type-$A$ reduction of the full derived DK frontier |
| `cor:what-remains-after-present-appendix` | `corollary` | 1410 | What remains after the present appendix |
