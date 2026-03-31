# Theorem Registry

Auto-generated on 2026-03-31 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2314 |
| Total tagged claims | 2981 |
| Active files in `main.tex` | 83 |
| Total `.tex` files scanned | 108 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2314 |
| `ProvedElsewhere` | 403 |
| `Conjectured` | 207 |
| `Conditional` | 25 |
| `Heuristic` | 32 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 990 |
| `proposition` | 743 |
| `corollary` | 371 |
| `lemma` | 118 |
| `computation` | 82 |
| `remark` | 5 |
| `calculation` | 3 |
| `maintheorem` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 15 |
| Part I: Theory | 846 |
| Part II: Examples | 553 |
| Part III: Connections | 615 |
| Appendices | 285 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus_modular_koszul.tex` | 182 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 112 |
| `chapters/connections/arithmetic_shadows.tex` | 99 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 84 |
| `chapters/theory/higher_genus_complementarity.tex` | 78 |
| `appendices/nonlinear_modular_shadows.tex` | 76 |
| `chapters/examples/w_algebras.tex` | 65 |
| `chapters/theory/higher_genus_foundations.tex` | 63 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 53 |
| `chapters/examples/kac_moody.tex` | 51 |
| `chapters/theory/chiral_modules.tex` | 51 |
| `chapters/connections/thqg_gravitational_s_duality.tex` | 46 |
| `chapters/examples/free_fields.tex` | 45 |
| `chapters/examples/yangians_computations.tex` | 45 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 42 |
| `chapters/examples/yangians_foundations.tex` | 42 |
| `chapters/theory/configuration_spaces.tex` | 40 |
| `chapters/connections/thqg_gravitational_complexity.tex` | 39 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 38 |
| `chapters/theory/chiral_koszul_pairs.tex` | 38 |

## Complete Proved Registry

### Frame (15)

#### `chapters/frame/heisenberg_frame.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 516 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 873 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 968 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1174 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1398 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1420 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1583 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1767 | Quantum complementarity for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2404 | $\mathfrak{sl}_2$ bar complex as Swiss-cheese coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2476 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2525 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2606 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 2644 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 2912 | CS $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | 3643 | The Heisenberg center |

### Part I: Theory (846)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 1015 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 1412 | Geometric realization |
| `prop:orthogonal` | `proposition` | 1549 | Orthogonality |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (112)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:curvature-central` | `theorem` | 181 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 286 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 363 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 432 | Conilpotency ensures convergence |
| `lem:arity-cutoff` | `lemma` | 682 | Arity cutoff: finite MC equation at each stage |
| `thm:completed-bar-cobar-strong` | `theorem` | 701 | MC element lifts to the completed convolution algebra |
| `prop:standard-strong-filtration` | `proposition` | 848 | Strong filtration for the standard landscape |
| `prop:mc4-reduction-principle` | `proposition` | 931 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 996 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 1033 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 1071 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 1120 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 1171 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 1234 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 1298 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 1334 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 1410 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 1507 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 1523 | Factorization-envelope criterion for principal stages |
| `cor:completion-closure-equivalence` | `corollary` | 1559 | Homotopy-categorical equivalence on the completion closure |
| `thm:coefficient-stability-criterion` | `theorem` | 1595 | Coefficient-stability criterion |
| `thm:completed-twisting-representability` | `theorem` | 1630 | Completed twisting representability |
| `thm:mc-twisting-closure` | `theorem` | 1653 | MC-twisting closure of the completion closure |
| `thm:uniform-pbw-bridge` | `theorem` | 1678 | Uniform PBW bridge from MC1 to MC4 |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 1784 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 1830 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 1865 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 1885 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 1903 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 1922 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 1964 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 2004 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 2045 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 2112 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 2154 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 2200 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 2262 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 2303 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 2375 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 2462 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 2488 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 2513 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 2567 | Stage-\texorpdfstring{$4$}{4} reduction to one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 2595 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 2632 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 2663 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 2705 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 2732 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 2762 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 2805 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 2840 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 2870 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 2887 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 2938 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 2999 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
| `cor:winfty-dual-candidate-construction` | `corollary` | 3038 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 3085 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} reduction on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 3124 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 3216 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 3247 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 3355 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 3403 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 3449 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 3476 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 3618 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 3655 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 3719 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 3774 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 3816 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 3910 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 3935 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 3974 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 3994 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 4032 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 4049 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 4072 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 4094 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 4110 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 4120 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 4136 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 4148 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 4161 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 4179 | Stage-\texorpdfstring{$5$}{5} mixed transport reduction to one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 4194 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 4213 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 4420 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 4438 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 4475 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 4512 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-network-collapse` | `corollary` | 4808 | Visible stage-\texorpdfstring{$5$}{5} local network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 4856 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 5080 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 5353 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 5694 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 5730 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 5791 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 5803 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 5911 | Modular operad structure of the bar complex |
| `cor:genus-expansion-converges` | `corollary` | 6203 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 6263 | Functoriality of bar construction |
| `thm:reconstruction-vs-duality` | `theorem` | 6372 | Reconstruction versus duality |
| `thm:recognition-koszul-pairs` | `theorem` | 6434 | Recognition theorem for finite chiral Koszul pairs |
| `thm:mixed-boundary-sseq` | `theorem` | 6489 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | 6513 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | 6561 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | 6590 | Universality |
| `prop:sugawara-contraction` | `proposition` | 6598 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | 6663 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | 6679 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | 6725 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | 6774 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | 6818 | Diagonal GKO transgression |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (53)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 434 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 655 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 973 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 1088 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1161 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1205 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1273 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1339 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1474 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1540 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1665 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 1834 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 1850 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 1904 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 1927 | Genus-graded convergence |
| `prop:counit-qi` | `proposition` | 2048 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 2060 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 2095 | Derived equivalence |
| `lem:complete-filtered-comparison` | `lemma` | 2183 | Complete filtered comparison lemma |
| `cor:completed-derived-equivalence` | `corollary` | 2284 | Completed derived equivalence |
| `thm:barr-beck-lurie-koszulness` | `theorem` | 2386 | Barr--Beck--Lurie characterization of chiral Koszulness |
| `thm:fh-concentration-koszulness` | `theorem` | 2471 | Factorization homology concentration |
| `thm:fm-boundary-acyclicity` | `theorem` | 2531 | FM boundary acyclicity |
| `prop:lagrangian-perfectness` | `proposition` | 2722 | Perfectness for the standard landscape |
| `cor:lagrangian-unconditional` | `corollary` | 2858 | Unconditional Lagrangian criterion for the standard landscape |
| `prop:bar-fh` | `proposition` | 3173 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 3251 | Cobar as factorization cohomology |
| `prop:subexponential-growth-automatic` | `proposition` | 3798 | Sub-exponential growth is automatic |
| `thm:ks-centrality` | `theorem` | 4015 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | 4058 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | 4109 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | 4144 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | 4190 | Quadratic frontier |
| `prop:eta-hessian-transfer` | `proposition` | 4284 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | 4320 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | 4365 | Admissible scalar rigidity |
| `cor:ds-not-first-frontier` | `corollary` | 4398 | Drinfeld--Sokolov reductions remain scalar-rigid |
| `thm:classification-scalar-genera` | `theorem` | 4440 | Classification of scalar genera |
| `thm:platonic-hierarchy-log` | `theorem` | 4510 | Five-step hierarchy of the categorical logarithm |
| `prop:cech-two-element-strict` | `proposition` | 5025 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | 5353 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | 5413 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | 5445 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | 5467 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | 5565 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | 5613 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | 5633 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | 5678 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | 5709 | Repeated roots encode extension data |
| `thm:common-core-exact-sequences-inv` | `theorem` | 5741 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | 5769 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | 5836 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | 5858 | Explicit coprime-locus projectors |

#### `chapters/theory/bar_construction.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 251 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 638 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 728 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 910 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 976 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 1004 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 1099 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 1141 | Arnold relations |
| `comp:deg0` | `computation` | 1184 | Degree 0 |
| `comp:deg1-general` | `computation` | 1202 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1315 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1354 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1360 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1392 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1415 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1482 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1533 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1550 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1637 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1663 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1687 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1751 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1826 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1888 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1998 | Bar complex is chiral |

#### `chapters/theory/chiral_center_theorem.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:partial-comp-assoc` | `lemma` | 186 | Associativity of partial compositions |
| `prop:pre-lie-chiral` | `proposition` | 491 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | 519 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | 540 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | 1223 | Chiral Deligne--Tamarkin |

#### `chapters/theory/chiral_hochschild_koszul.tex` (38)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 193 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 344 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 382 | Hochschild spectral sequence |
| `lem:hochschild-shift-computation` | `lemma` | 500 | Hochschild duality shift |
| `thm:main-koszul-hoch` | `theorem` | 561 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `thm:hochschild-polynomial-growth` | `theorem` | 672 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 771 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `prop:e2-formality-hochschild` | `proposition` | 812 | $\Etwo$-formality of chiral Hochschild cohomology |
| `thm:convolution-formality-one-channel` | `theorem` | 890 | Convolution formality $=$ one-channel |
| `thm:bifunctor-obstruction-decomposition` | `theorem` | 1125 | Bifunctor obstruction decomposition |
| `comp:boson-hochschild` | `computation` | 1337 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 1367 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 1472 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 1566 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 1664 | Kac--Moody cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | 1870 | Genus truncation |
| `prop:hochschild-shadow-projection` | `proposition` | 1943 | Hochschild as arity-$2$ shadow projection |
| `thm:mc2-1-km` | `theorem` | 1972 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 2089 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 2337 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 2423 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 2542 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | 2724 | Strictification principle for modular deformation theory |
| `prop:d-mod-squared-zero` | `proposition` | 2861 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2997 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 3172 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 3362 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 3489 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 3734 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 3880 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 4019 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 4104 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 4151 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 4449 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 4580 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 4627 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 4825 | $bc$/$\beta\gamma$ Koszul duality |
| `prop:hochschild-cech-ss` | `proposition` | 5027 | Hochschild--\v{C}ech spectral sequence |

#### `chapters/theory/chiral_koszul_pairs.tex` (38)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 198 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 225 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 245 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 273 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 348 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 610 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 688 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 743 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 787 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 934 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1038 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1072 | Converse: formality implies chiral Koszulness |
| `conj:ext-diagonal-vanishing` | `theorem` | 1142 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1180 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1206 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1230 | Kac--Shapovalov criterion for simple quotients |
| `prop:li-bar-poisson-differential` | `proposition` | 1404 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | 1463 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | 1606 | Nilradical obstruction at degenerate admissible levels |
| `thm:koszul-equivalences-meta` | `theorem` | 1767 | Equivalences of chiral Koszulness |
| `prop:koszulness-formality-equivalence` | `proposition` | 2061 | Koszulness as formality of the convolution algebra |
| `prop:cumulant-window-inversion` | `proposition` | 2297 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 2353 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 2530 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 2590 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 2744 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 2838 | Bar computes Koszul dual, complete statement |
| `lem:completion-convergence` | `lemma` | 2926 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 2975 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 3532 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 3750 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 3815 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 3876 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 3999 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 4041 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 4095 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 4130 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 4325 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (51)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 180 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 285 | Module Koszul equivalence |
| `thm:monoidal-module-koszul` | `theorem` | 332 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 472 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 548 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 652 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 745 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 803 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 958 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 1252 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1641 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1702 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1902 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1960 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1994 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:logarithmic-bar` | `proposition` | 2232 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2326 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2437 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2472 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2511 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2528 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2568 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2590 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2740 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2847 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2961 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3041 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3195 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3226 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3269 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3348 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3434 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3493 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3569 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3646 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3696 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3789 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3843 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3909` | `calculation` | 3909 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3936` | `calculation` | 3936 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3967` | `calculation` | 3967 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4085 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4210 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4260 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4384 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4426 | \texorpdfstring{$\mathcal{W}$}{W}-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4481 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4523 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4653 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4792 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4902 | Heisenberg fusion splitting |

#### `chapters/theory/cobar_construction.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 250 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 311 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 344 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 426 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 502 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 616 | Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 872 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 1032 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1250 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1381 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1433 | Explicit cobar-bar augmentation |
| `prop:cobar-modular-shadow` | `proposition` | 1705 | Cobar as modular shadow carrier |
| `thm:cobar-cech` | `theorem` | 1717 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1765 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1786 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1876 | Topology |
| `thm:poincare-verdier` | `theorem` | 1935 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 2025 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 2050 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 2096 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 2250 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2346 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2487 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2512 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2609 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2662 | Recognition principle |
| `lem:deformation-space` | `lemma` | 3034 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 3076 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 3124 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3203 | Curved differential formula |

#### `chapters/theory/configuration_spaces.tex` (40)

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
| `thm:FM-convergence` | `theorem` | 3306 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 3365 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 3471 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 3513 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 3540 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 3562 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 3602 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 3626 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 3661 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 3683 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 3717 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 3733 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 3755 | Nilpotency from Arnold relations |
| `thm:arnold-jacobi` | `theorem` | 3886 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 3939 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 3985 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 4017 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 4062 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 4293 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 4363 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 4500 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:4710` | `computation` | 4710 | Explicit examples |

#### `chapters/theory/derived_langlands.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:langlands-bar-bridge` | `theorem` | 86 | Bridge theorem: bar complex at critical level $\longrightarrow$ opers $\longrightarrow$ geometric Langlands |
| `thm:oper-bar-h0-dl` | `theorem` | 303 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 338 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 362 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 399 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 480 | Differential analysis at arity 3 |
| `prop:d4-nonvanishing` | `proposition` | 560 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 619 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 632 | Full derived identification |
| `prop:bar-as-localization` | `proposition` | 715 | The bar complex as localization |
| `prop:sl2-periodicity-dl` | `proposition` | 894 | Affine sl2 periodicity |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 970 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/e1_modular_koszul.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | 127 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | 146 | — |
| `rem:e1-mc-element` | `theorem` | 198 | $E_1$ Maurer--Cartan element |
| `prop:e1-shadow-r-matrix` | `proposition` | 231 | — |
| `thm:e1-mc-finite-arity` | `theorem` | 314 | $E_1$ MC equation at finite arity |
| `thm:e1-coinvariant-shadow` | `theorem` | 381 | Coinvariant projection: $E_1$ shadows to $E_\infty$ shadows |
| `thm:e1-theorem-A-modular` | `theorem` | 619 | Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction |
| `thm:e1-theorem-B-modular` | `theorem` | 667 | Theorem~$\mathrm{B}^{E_1}$ at all genera: ordered bar--cobar inversion |
| `thm:e1-theorem-C-modular` | `theorem` | 692 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
| `thm:e1-theorem-D-modular` | `theorem` | 724 | Theorem~$\mathrm{D}^{E_1}$ at all genera: modular $R$-matrix as $E_1$ characteristic |
| `thm:e1-theorem-H-modular` | `theorem` | 787 | Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered Hochschild at genus~$g$ |
| `lem:bare-graph-no-thooft` | `lemma` | 915 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | 936 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | 978 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | 1000 | Exact $N^{\chi}$ weighting from traced open color |

#### `chapters/theory/en_koszul_duality.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:en-chiral-bridge` | `theorem` | 60 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
| `prop:en-formality-mc-truncation` | `proposition` | 133 | Formality hierarchy as MC obstruction truncation |
| `prop:linking-sphere-residue` | `proposition` | 411 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 486 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 646 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 704 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |
| `thm:bar-swiss-cheese` | `theorem` | 1016 | Bar complex as Swiss-cheese coalgebra |
| `prop:operadic-center-existence` | `proposition` | 1245 | Existence of the operadic center |
| `thm:operadic-center-hochschild` | `theorem` | 1298 | The operadic center of $\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex |
| `thm:center-geometric-inevitability` | `theorem` | 1620 | Geometric inevitability of the chiral center |
| `prop:braces-from-center` | `proposition` | 1813 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | 1862 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | 1938 | Terminality of the center |
| `cor:center-functor` | `corollary` | 2026 | The center functor |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 40 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 183 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 58 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 115 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 224 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 270 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 318 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 347 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 409 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 436 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 493 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 551 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 631 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 801 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 822 | — |
| `thm:fourier-specialization` | `theorem` | 857 | Specialization |
| `rem:fourier-genus-preview` | `remark` | 1012 | Ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus_complementarity.tex` (78)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:involution-splitting` | `lemma` | 159 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 214 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 288 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 378 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 534 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 589 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 674 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 737 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 788 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 933 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 1006 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 1046 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 1100 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1129 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 1317 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 1352 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 1404 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 1517 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 1548 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 1568 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 1673 | Verdier pairing and Lagrangian eigenspaces |
| `prop:ptvv-lagrangian` | `proposition` | 1890 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 1963 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 2063 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 2091 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 2128 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 2171 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 2207 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 2238 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 2479 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 2660 | BD 3.4.12: genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 2710 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 2723 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 2765 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 2824 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 2866 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 2894 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 2916 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 2960 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 3149 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 3197 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 3285 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 3312 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 3340 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 3374 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 3399 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 3460 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 3506 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 3545 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 3574 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 3598 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 3623 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 3655 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 3704 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 3730 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 3746 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 3851 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 3929 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 3977 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 4066 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | 4241 | Ambient complementarity in tangent form |
| `thm:ambient-complementarity-fmp` | `theorem` | 4284 | Ambient complementarity as shifted symplectic formal moduli problem |
| `thm:shifted-cotangent-normal-form` | `theorem` | 4541 | Shifted cotangent normal form |
| `prop:legendre-duality-potentials` | `proposition` | 4590 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | 4605 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | 4635 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | 4659 | Criterion for fake complementarity |
| `thm:holo-comp-bulk-reconstruction` | `theorem` | 4855 | Protected dual transform |
| `thm:holo-comp-cotangent-realization` | `theorem` | 4905 | Shifted cotangent realization |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | 4932 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | 5018 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | 5062 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | 5139 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | 5222 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | 5291 | First nonlinear holographic anomaly |
| `thm:critical-dimension` | `theorem` | 5395 | Critical dimension |
| `prop:non-critical-liouville` | `proposition` | 5560 | Non-critical complementarity and the Liouville sector |
| `cor:complementarity-discriminant-cancellation` | `corollary` | 5605 | Arity-$4$ discriminant cancellation |

#### `chapters/theory/higher_genus_foundations.tex` (63)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:genus-g-curvature-package` | `proposition` | 350 | The genus-$g$ curvature package |
| `prop:genus-g-mc-element` | `proposition` | 466 | Genus-$g$ MC element |
| `thm:bar-ainfty-complete` | `theorem` | 657 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 757 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 848 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 961 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 1068 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 1215 | Verdier duality of operations |
| `thm:bar-curved-ch-infty` | `theorem` | 1377 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
| `thm:convergence-filtered` | `theorem` | 1455 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1664 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1698 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1732 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1752 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1768 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2070 | Bar-cobar isomorphism, retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 2155 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2370 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2976 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 3179 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 3239 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 3492 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:arnold-genus1` | `theorem` | 3551 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 3586 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 3643 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 3911 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3944 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 4071 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 4174 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 4228 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 4306 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 4423 | \texorpdfstring{$W_3$}{W3} obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 4494 | Explicit genus-\texorpdfstring{$1$}{1} value of the \texorpdfstring{$W_3$}{W3} obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 4515 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 4544 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 4629 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4731 | Genus universality |
| `thm:multi-generator-universality` | `theorem` | 4911 | Multi-generator universality |
| `prop:multi-generator-obstruction` | `proposition` | 5001 | Multi-generator obstruction decomposition |
| `prop:f2-quartic-dependence` | `proposition` | 5034 | Genus-$2$ quartic dependence |
| `cor:anomaly-ratio` | `corollary` | 5086 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 5102 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 5118 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 5136 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 5159 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 5181 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 5233 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 5305 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 5335 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 5421 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 5465 | Grothendieck--Riemann--Roch bridge |
| `lem:stable-graph-d-squared` | `lemma` | 5633 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 5695 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 5733 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 5775 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 5864 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 5952 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 6021 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 6055 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 6096 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 6153 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 6181 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 6231 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (182)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:genus-graded-koszul` | `theorem` | 124 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 155 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 488 | Free-field examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 521 | Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 562 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 698 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 965 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 990 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1187 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1239 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1339 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1389 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1451 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:pbw-propagation` | `theorem` | 1627 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | 1779 | Locality of the collision differential |
| `thm:three-tier-architecture` | `theorem` | 1866 | Three-tier logical architecture of modular Koszul duality |
| `lem:e2-higher-genus` | `lemma` | 2134 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 2261 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 2371 | Modular characteristic |
| `cor:free-energy-ahat-genus` | `corollary` | 2536 | Scalar free energy as $\hat{A}$-genus |
| `thm:spectral-characteristic` | `theorem` | 2619 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 2652 | Universal modular Maurer--Cartan class |
| `prop:curvature-centrality-general` | `proposition` | 2778 | Centrality of higher-genus curvature |
| `thm:mc2-bar-intrinsic` | `theorem` | 2833 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 3223 | Shadow extraction |
| `prop:mc2-functoriality` | `proposition` | 3337 | Functoriality of the bar-intrinsic MC element |
| `thm:bipartite-linfty-tree` | `theorem` | 3433 | Bipartite shadow as $L_\infty$ tree-level structure |
| `thm:explicit-theta` | `theorem` | 3559 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 3778 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 4192 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 4271 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 4384 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 4418 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 4450 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 4646 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 4722 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 4787 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 4922 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 5019 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 5130 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 5267 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 5419 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 5593 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 5743 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 5937 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 6057 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 6156 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 6246 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 6358 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 6430 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 6512 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 6590 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 6667 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 6743 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 6818 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 6884 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 6962 | MC2 completion under explicit hypotheses |
| `thm:mc2-full-resolution` | `theorem` | 7042 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 7089 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 7131 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 7188 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 7242 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 7275 | Scalar saturation for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 7313 | Scalar saturation persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 7366 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 7505 | Scalar saturation for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 7587 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 7765 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 7928 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 8011 | Cyclic rigidity at generic level |
| `thm:algebraic-family-rigidity` | `theorem` | 8171 | Algebraic-family rigidity |
| `cor:saturation-algebraic-families` | `corollary` | 8277 | Saturation at all non-critical levels for algebraic families |
| `thm:conformal-bootstrap-rigidity` | `theorem` | 8340 | $L_0$-bootstrap rigidity |
| `cor:one-channel-no-lie` | `corollary` | 8447 | One-channel criterion without Lie symmetry |
| `thm:tautological-line-support` | `theorem` | 8677 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 8779 | MC2 reduced to cyclic model |
| `thm:convolution-dg-lie-structure` | `theorem` | 8938 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 9176 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 9540 | Modular homotopy convolution |
| `prop:modular-homotopy-type-structure` | `proposition` | 9624 | Structure of the modular homotopy type |
| `cor:strictification-comparison` | `corollary` | 9671 | Strictification comparison |
| `cor:vol1-theta-log-fm-twisting-data` | `corollary` | 9994 | $\Theta_\cA$ as universal modular twisting morphism |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | 10248 | First two weights |
| `comp:vol1-low-genus-log-fm-chart` | `computation` | 10323 | Low-genus amplitudes |
| `lem:shadow-bracket-well-defined` | `lemma` | 10853 | Well-definedness of the descended bracket |
| `cor:shadow-algebra-functoriality` | `corollary` | 10875 | Functoriality of the shadow algebra |
| `prop:master-equation-from-mc` | `proposition` | 10901 | All-arity master equation from MC |
| `thm:ds-complementarity-tower-main` | `theorem` | 10954 | DS complementarity tower |
| `thm:recursive-existence` | `theorem` | 11070 | Recursive existence and shadow tower convergence |
| `thm:modular-propagator-existence` | `theorem` | 11376 | Modular propagator existence |
| `thm:logfm-modular-cocomposition` | `theorem` | 11410 | Log-FM modular cocomposition |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | 11452 | Stable-graph pronilpotent completion |
| `thm:finite-rank-spectral-reduction` | `theorem` | 11503 | Finite-rank spectral reduction |
| `thm:primitive-to-global-reconstruction` | `theorem` | 11568 | Primitive-to-global reconstruction |
| `prop:primitive-shell-equations` | `proposition` | 11703 | Primitive shell equations |
| `prop:branch-master-equation` | `proposition` | 11841 | Branch quantum master equation |
| `cor:metaplectic-square-root` | `corollary` | 11894 | Determinantal half-density |
| `thm:primitive-flat-descent` | `theorem` | 12085 | Descent to the conformal block connection |
| `thm:conformal-block-reconstruction` | `theorem` | 12163 | Conformal block reconstruction from the primitive kernel |
| `thm:deformation-quantization-ope` | `theorem` | 12252 | Genus expansion from the OPE |
| `thm:ran-coherent-bar-cobar` | `theorem` | 12448 | Ran-coherent bar-cobar equivalence |
| `thm:shadow-channel-decomposition` | `theorem` | 12508 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 12588 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 12640 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 12763 | The explicit formula: direct derivation |
| `lem:graph-sum-truncation` | `lemma` | 13050 | Graph-sum truncation criterion |
| `conj:operadic-complexity-detailed` | `theorem` | 13125 | Operadic complexity |
| `prop:shadow-formality-low-arity` | `proposition` | 13244 | Shadow--formality identification at low arity |
| `thm:shadow-formality-identification` | `theorem` | 13315 | Shadow tower as formality obstruction tower |
| `thm:shadow-archetype-classification` | `theorem` | 13653 | Shadow archetype classification |
| `cor:shadow-depth-koszul-invariance` | `corollary` | 13850 | Shadow depth under Koszul duality |
| `thm:riccati-algebraicity` | `theorem` | 13922 | Riccati algebraicity |
| `prop:pole-purity` | `proposition` | 14058 | Pole purity |
| `prop:intrinsic-quartic` | `proposition` | 14076 | Intrinsic quartic principle |
| `thm:single-line-dichotomy` | `theorem` | 14111 | Single-line dichotomy |
| `thm:shadow-connection` | `theorem` | 14248 | Shadow connection |
| `thm:shadow-separation` | `theorem` | 14530 | Shadow separation and completeness |
| `thm:propagator-variance` | `proposition` | 14635 | Propagator variance inequality |
| `prop:t-line-autonomy` | `proposition` | 14745 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | 14802 | Inter-channel coupling on sublines |
| `thm:shadow-radius` | `theorem` | 14947 | Shadow growth rate: structure and asymptotics |
| `cor:virasoro-shadow-radius` | `corollary` | 15053 | Virasoro shadow growth rate |
| `prop:virasoro-bottleneck` | `proposition` | 15211 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | 15425 | Koszul exchange of shadow regimes |
| `prop:propagator-universality` | `proposition` | 15502 | Propagator universality |
| `thm:hamilton-jacobi-shadow` | `theorem` | 15742 | Hamilton--Jacobi master equation on deformation spaces |
| `thm:shadow-finite-determination` | `theorem` | 15951 | Shadow finite determination |
| `cor:w3-reconstruction` | `corollary` | 16038 | $\cW_3$: seven parameters determine the full 2D tower |
| `thm:shadow-tautological-ring` | `theorem` | 16244 | Shadow classes in the tautological ring |
| `cor:analytic-shadow-realization` | `corollary` | 16387 | Analytic shadow realization |
| `thm:shadow-cohft` | `theorem` | 16473 | Shadow cohomological field theory |
| `thm:mc-tautological-descent` | `theorem` | 16644 | MC descent to tautological relations |
| `prop:self-loop-vanishing` | `proposition` | 17071 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | 17107 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | 17159 | Genus-$1$ two-point function from MC |
| `prop:wdvv-from-mc` | `proposition` | 17187 | WDVV from MC at genus~$0$ |
| `prop:mumford-from-mc` | `proposition` | 17220 | Mumford relation from MC at arity~$2$ |
| `thm:cohft-reconstruction` | `theorem` | 17252 | Reconstruction from the MC tangent complex |
| `prop:dressed-propagator-resolution` | `proposition` | 17341 | Dressed propagator coefficient and symmetry |
| `cor:topological-recursion-mc-shadow` | `corollary` | 17478 | Topological recursion as MC shadow |
| `prop:fp-genus-decay-for-double` | `proposition` | 17632 | Faber--Pandharipande genus decay |
| `thm:shadow-double-convergence` | `theorem` | 17659 | Double convergence of the shadow partition function |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | 17828 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:finite-jet-rigidity` | `proposition` | 17909 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 17932 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 17968 | Gaussian collapse for abelian input |
| `thm:cubic-gauge-triviality` | `theorem` | 18050 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | 18122 | Independent sum factorization |
| `thm:envelope-koszul` | `theorem` | 18179 | Envelope Koszulness |
| `cor:generic-ht-koszul` | `corollary` | 18257 | Generic-parameter Koszulness for HT boundary algebras |
| `thm:platonic-adjunction` | `theorem` | 18364 | The platonic adjunction |
| `cor:envelope-universal-mc` | `corollary` | 18497 | The envelope carries the universal MC class |
| `prop:envelope-construction-strategies` | `proposition` | 18555 | Construction strategies for the modular envelope |
| `conj:shadow-depth-invariant` | `theorem` | 18627 | Shadow depth is a homotopy invariant |
| `conj:tropical-koszulness` | `theorem` | 18671 | Tropical Koszulness |
| `cor:tropical-cohen-macaulay` | `corollary` | 18763 | Tropical Koszulness as the Cohen--Macaulay property |
| `prop:genus0-curve-independence` | `proposition` | 18810 | Genus-$0$ curve-independence |
| `thm:open-stratum-curve-independence` | `theorem` | 18829 | Open-stratum curve-independence at higher genus |
| `prop:saddle-point-mc` | `proposition` | 19120 | MC element as saddle point |
| `thm:five-from-theta` | `theorem` | 19391 | Five main theorems from the master MC element |
| `thm:obstruction-recursion` | `theorem` | 19615 | Obstruction recursion for the shadow Postnikov tower |
| `thm:rectification-meta` | `theorem` | 19712 | Rectification meta-theorem |
| `thm:platonic-recovery` | `theorem` | 19807 | Recovery of the platonic package from $\Theta_\cA$ |
| `prop:chriss-ginzburg-structure` | `proposition` | 20031 | MC structure principle |
| `prop:planar-forest-coinvariant` | `proposition` | 20410 | Planar forests map to unordered forests |
| `thm:planar-forest-tropicalization` | `theorem` | 20443 | Planar tropicalization |
| `prop:ordered-log-fm-construction` | `proposition` | 20488 | Ordered log-FM construction |
| `cor:e1-ambient-d-squared-zero` | `corollary` | 20566 | $E_1$ ambient $D^2 = 0$ |
| `prop:coefficient-algebras-well-defined` | `proposition` | 20611 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 20644 | Square-zero: convolution level |
| `conj:differential-square-zero` | `theorem` | 20658 | Square-zero: ambient level |
| `thm:inductive-genus-determination` | `theorem` | 20845 | Inductive genus determination |
| `cor:genus-base-cases` | `corollary` | 20913 | Base cases |
| `rem:genus2-shell-activation` | `theorem` | 20950 | Genus-$2$ shell activation as depth diagnostic |
| `comp:vol1-genus-three-stable-graph-census` | `computation` | 21054 | Genus-$3$ stable graph census |
| `prop:2d-convergence` | `proposition` | 21333 | Two-dimensional convergence |
| `thm:analytic-algebraic-comparison` | `theorem` | 21389 | Analytic = algebraic |
| `thm:determinantal-branch-formula` | `theorem` | 21524 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | 21560 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | 21591 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | 21655 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | 21691 | The frontier is cubic |

#### `chapters/theory/hochschild_cohomology.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 106 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 150 | W-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:404` | `computation` | 404 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 460 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 540 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 795 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 827 | Hochschild cup product exchange |
| `thm:derived-center-hochschild` | `theorem` | 1008 | Derived center $=$ Hochschild cochains |
| `thm:morita-invariance-HH` | `theorem` | 1092 | Morita invariance of $\mathrm{HH}^\bullet$ |
| `prop:explicit-morita-transfer` | `proposition` | 1122 | Explicit Morita transfer |
| `thm:circle-fh-hochschild` | `theorem` | 1293 | Factorization homology on $S^1$ $=$ Hochschild chains |
| `prop:monodromy-standard` | `proposition` | 1446 | Monodromy for standard families |

#### `chapters/theory/introduction.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 1067 | Central charge complementarity |
| `thm:modular-koszul-duality-main` | `theorem` | 1174 | Modular Koszul duality |
| `cor:shadow-separation-intro` | `corollary` | 1312 | Shadow separation; ; Theorem~\textup{\ref{thm:shadow-separation}} |
| `thm:rectification-bridge` | `theorem` | 2382 | Rectification bridge |
| `prop:modular-homotopy-classification` | `proposition` | 2648 | Classification by modular homotopy type |
| `prop:shadow-massey-identification` | `proposition` | 2718 | Genus-$0$ shadow obstructions $=$ $A_\infty$ Massey products |
| `prop:chirAss-self-dual` | `proposition` | 4133 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:three-levels-mc-completion` | `proposition` | 125 | Three levels as MC at successive completions |
| `lem:chiral-enveloping-well-defined` | `lemma` | 175 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 220 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 260 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 279 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 336 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 399 | \texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 458 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 587 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 681 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 696 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 800 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 922 | Maurer--Cartan correspondence — quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 1013 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1043 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1237 | Positselski comodule-contramodule equivalence |
| `thm:full-derived-module-equiv` | `theorem` | 1263 | Full derived module equivalence |
| `thm:cs-koszul-km` | `theorem` | 1383 | Affine Kac--Moody Maurer--Cartan and curvature package |
| `thm:linf-mc-flatness` | `theorem` | 1447 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan equation from bar operations |
| `thm:cs-koszul-general` | `theorem` | 1502 | Maurer--Cartan equation for non-quadratic bar \texorpdfstring{$L_\infty$}{L-infinity} algebras |
| `thm:bv-structure-bar` | `theorem` | 1698 | BV structure on bar complex |
| `thm:ordered-shuffle` | `theorem` | 1850 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | 1892 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | 1922 | Enveloping duality |
| `thm:ordered-bimod-bicomod` | `theorem` | 1961 | Bimodule--bicomodule equivalence |
| `thm:ordered-diagonal` | `theorem` | 1986 | Diagonal correspondence |
| `thm:ordered-HH-coHH-homology` | `theorem` | 2034 | Hochschild--coHochschild duality, homological version |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | 2065 | Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-pair-of-pants` | `theorem` | 2113 | Ordered pair-of-pants algebra |
| `thm:ordered-master` | `theorem` | 2137 | Master theorem: the ordered open trace formalism |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 232 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 344 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 411 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 502 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 561 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 577 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 668 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 752 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:chiral-operad-genus0` | `proposition` | 323 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 367 | Prism principle: operadic identification |
| `thm:prism-higher-genus` | `theorem` | 607 | Prism principle: higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | 679 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | 704 | The loop expansion is the genus expansion |
| `cor:prism-principle` | `corollary` | 809 | The prism principle |
| `thm:modular-convolution-structure` | `theorem` | 927 | dg~Lie structure |
| `thm:vol1-genus-completion` | `theorem` | 967 | Genus completion |
| `prop:vol1-structure-as-MC` | `proposition` | 1015 | The algebra structure as MC element |
| `thm:partition` | `theorem` | 1121 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:quantum-linfty-master` | `theorem` | 616 | Quantum $L_\infty$ master equation |
| `prop:two-element-strict` | `proposition` | 861 | Two-element covers are strict |
| `prop:borcherds-shadow-identification` | `proposition` | 1345 | Secondary Borcherds operations as shadow tower obstructions |

### Part II: Examples (553)

#### `chapters/examples/bar_complex_tables.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 714 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 807 | Modular rank of \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 886 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 947 | PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} |
| `comp:sl3-casimir-decomp` | `computation` | 1040 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | 1123 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | 1452 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1757 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1803 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | 1874 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | 1925 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2058 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2094 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2128 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2558 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2733 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2953 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 3007 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3044 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3318 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3497 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3794 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3856 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4053 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4203 | BGG involution under Koszul duality |

#### `chapters/examples/beta_gamma.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 188 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 239 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 274 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 327 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 365 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | 386 | — |
| `thm:cobar-fermions` | `theorem` | 414 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | 451 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 539 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 806 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 926 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 1027 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1168 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1252 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1403 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |
| `prop:mumford-exponent-complementarity` | `proposition` | 1577 | Mumford exponent complementarity |
| `thm:betagamma-quartic-birth` | `theorem` | 1926 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | 1962 | $\beta\gamma$ shadow Postnikov tower: arity~$4$ on weight-changing line |
| `prop:betagamma-primitive-kernel` | `proposition` | 1991 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive kernel |
| `prop:betagamma-primitive-shell` | `proposition` | 2039 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive shell equations |
| `lem:betagamma-ell2-vanishing` | `lemma` | 2186 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | 2233 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | 2343 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | 2385 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | 2415 | Pure contact boundary law |
| `prop:betagamma-translation-coproduct` | `proposition` | 2578 | Translation and coproduct |

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
| `prop:lattice-one-step` | `proposition` | 453 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 525 | Deformation--duality compatibility |

#### `chapters/examples/free_fields.tex` (45)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:single-fermion-boson-duality` | `theorem` | 204 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | 256 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 312 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 363 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 374 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `thm:heisenberg-bar` | `theorem` | 446 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 469 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | 511 | Heisenberg curved structure |
| `thm:lattice-voa-bar` | `theorem` | 558 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 587 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | 617 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 654 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | 699 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 723 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 938 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 1014 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 1046 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 1181 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 1236 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 1286 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1328 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1481 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1557 | Spectral flow under Koszul duality |
| `thm:heisenberg-not-self-dual` | `theorem` | 1791 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 1896 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 1927 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2186 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 2300 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 2573 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 2722 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 2769 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 2832 | Heisenberg level inversion: curved duality |
| `thm:virasoro-moduli` | `theorem` | 2892 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 2975 | Geometric interpretation |
| `thm:algebraic-string-dictionary` | `theorem` | 3085 | Algebraic bar/BRST genus dictionary |
| `thm:genus-g-chiral-homology` | `theorem` | 3192 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 3303 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 3383 | Bar classes on moduli and boundary factorization |
| `thm:modular-invariance` | `theorem` | 3511 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 3548 | Modular anomaly for affine Kac--Moody algebras |
| `thm:wakimoto-bar` | `theorem` | 3663 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 3676 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 3681 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 3708 | Higher \texorpdfstring{$A_\infty$}{A-infinity} corrections in quantum \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:filtered-bar-complex` | `theorem` | 3788 | Filtered bar complex |

#### `chapters/examples/genus_expansions.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 79 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 153 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `thm:lattice-all-genera` | `theorem` | 197 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 232 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 254 | \texorpdfstring{$\mathcal{W}$}{W}-algebra free energy at all genera |
| `thm:sl2-all-genera` | `theorem` | 447 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 593 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 733 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 775 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 829 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 940 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 1050 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1190 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1257 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1322 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1408 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1540 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1570 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1587 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1622 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1693 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1821 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1863 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1942 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 2091 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2156 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:complementarity-classification` | `proposition` | 2392 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2446 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2741 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2841 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2857 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2882 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2914 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 3009 | Loop expansion interpretation |
| `thm:boundary-characters-bar-hilbert` | `theorem` | 3180 | Boundary characters as bar Hilbert series |

#### `chapters/examples/heisenberg_eisenstein.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:heisenberg-gaussian-termination` | `proposition` | 44 | Gaussian shadow termination for Heisenberg |
| `thm:heisenberg-sewing` | `theorem` | 164 | Heisenberg sewing theorem |
| `thm:heisenberg-genus-one-complete` | `theorem` | 310 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 397 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 439 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 557 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 660 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 709 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 1038 | Multi-boson Eisenstein corrections |
| `thm:heisenberg-exact-linearity` | `theorem` | 1349 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | 1389 | Heisenberg shadow Postnikov tower: finite termination at arity~$2$ |
| `cor:heisenberg-gaussian-boundary` | `corollary` | 1612 | Gaussian boundary law |
| `prop:heisenberg-primitive-kernel` | `proposition` | 1723 | Heisenberg primitive kernel |
| `prop:heisenberg-primitive-shell` | `proposition` | 1760 | Heisenberg primitive shell equations |

#### `chapters/examples/kac_moody.tex` (51)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:km-genus1-hessian` | `computation` | 139 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `thm:geometric-ope-kac-moody` | `theorem` | 363 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 397 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 437 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 503 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 632 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 663 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 701 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 759 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 795 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 864 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | 898 | Killing form via structure constants |
| `prop:verdier-level-identification` | `proposition` | 983 | Verdier level identification |
| `prop:ff-channel-shear` | `proposition` | 1324 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 1374 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 1440 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1504 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1543 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1597 | Closed-form OPE for Koszul dual |
| `comp:sl2-collision-residue-kz` | `computation` | 1654 | Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:km-quantum-groups` | `theorem` | 1947 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 2273 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 2339 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 2509 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 2621 | KW formula via bar complex: general simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `prop:admissible-verlinde-bar` | `proposition` | 2697 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2984 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 3065 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 3130 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 3201 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 3267 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 3330 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 3376 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 3415 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 3452 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 3631 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 3661 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 3691 | Full derived oper identification |
| `thm:affine-cubic-normal-form` | `theorem` | 3941 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | 3977 | Affine shadow Postnikov tower: finite termination at arity~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | 4015 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | 4057 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | 4127 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 4175 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 4232 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 4309 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 4395 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 4431 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 4520 | Vanishing of the genus loop on the affine cubic |
| `cor:level-rank-bar-intertwining` | `corollary` | 4738 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | 4766 | Kappa anti-symmetry under Feigin--Frenkel involution |

#### `chapters/examples/landscape_census.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 301 | Paired standard-tower MC4 completion packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 421 | Minimal closure conditions for the standard-tower MC4 completion target |
| `cor:anomaly-ratio-ds` | `corollary` | 569 | Anomaly ratio and DS reduction |
| `cor:genus1-anomaly-ratio` | `corollary` | 579 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `cor:subexp-free-field` | `corollary` | 1019 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 1029 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 1046 | DS reduction and bar cohomology generating functions |
| `thm:ds-spectral-branch-preservation` | `theorem` | 1205 | DS preservation of the sub-discriminant |
| `prop:ds-invariant-discriminant` | `proposition` | 1359 | DS-invariant discriminant subfactor |
| `prop:hred-sl2` | `proposition` | 1403 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 1597 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1688 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1785 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1851 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 1906 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1957 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1972 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 2061 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2250 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2556 | Spectral sequence collapse |

#### `chapters/examples/lattice_foundations.tex` (36)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lattice-sewing` | `theorem` | 124 | Lattice sewing envelope |
| `lem:lattice:cocycle-class` | `lemma` | 396 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 560 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 779 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 876 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 899 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 933 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 967 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 1012 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 1098 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 1143 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1348 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1393 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1435 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1458 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1582 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1599 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1624 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1826 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 2010 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2635 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2703 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2777 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2936 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3238 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3319 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3492 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3693 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3736 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3894 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3941 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 4027 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 4108 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |
| `prop:lattice:genus1-simple-pole` | `proposition` | 4296 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4313 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | 4410 | Lattice shadow Postnikov tower: termination at weight~$2$ |

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

#### `chapters/examples/w_algebras.tex` (65)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:w3-genus1-hessian` | `computation` | 158 | The $\mathcal W_3$ genus-$1$ Hessian |
| `comp:w-entropy-ladder` | `computation` | 194 | Completion entropy ladder |
| `thm:w-algebra-koszul-main` | `theorem` | 249 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `thm:w-geometric-ope` | `theorem` | 996 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 1067 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-critical-bar` | `theorem` | 1107 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 1144 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras, precise statement |
| `thm:virasoro-self-duality` | `theorem` | 1270 | Virasoro uncurved self-duality at \texorpdfstring{$c=0$}{c=0} |
| `prop:virasoro-generic-koszul-dual` | `proposition` | 1367 | Virasoro Koszul dual at generic central charge |
| `thm:vir-genus1-curvature` | `theorem` | 1439 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1490 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1554 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1723 | Koszul dual of \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1804 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1870 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 1940 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 2035 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 2131 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 2152 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-center-langlands` | `theorem` | 2241 | \texorpdfstring{$\mathcal{W}$}{W}-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 2346 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `thm:w-universal-gravitational-cubic` | `theorem` | 3131 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | 3186 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | 3223 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | 3310 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-resonance-reorganization` | `theorem` | 3380 | Resonance reorganization |
| `cor:w-complementarity-potential-poles` | `corollary` | 3517 | Pole structure of the complementarity potential |
| `prop:virasoro-primitive-kernel` | `proposition` | 3572 | Virasoro primitive kernel |
| `prop:virasoro-primitive-shell` | `proposition` | 3624 | Virasoro primitive shell equations |
| `thm:w-w3-mixed-shadow` | `theorem` | 3778 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w3-two-dim-hessian-cubic` | `proposition` | 3840 | Two-dimensional Hessian and universal cubic |
| `thm:w3-quartic-channel-decomposition` | `theorem` | 3868 | $\mathcal{W}_3$ quartic channel decomposition |
| `prop:w3-denominator-filtration` | `proposition` | 3929 | Denominator filtration by $W$-charge |
| `thm:w3-quintic-nonvanishing` | `theorem` | 3957 | $\mathcal{W}_3$ quintic nonvanishing |
| `prop:w-w3-weight6-resonance` | `proposition` | 4060 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | 4131 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | 4157 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-archetype-trichotomy` | `theorem` | 4233 | Archetype trichotomy |
| `thm:w-virasoro-quintic-forced` | `theorem` | 4300 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | 4356 | Explicit quintic shadow for Virasoro |
| `thm:virasoro-shadow-generating-function` | `theorem` | 4408 | Virasoro shadow metric |
| `thm:w-finite-termination` | `theorem` | 4595 | Finite termination for primitive archetypes |
| `cor:virasoro-postnikov-nontermination` | `corollary` | 4672 | Virasoro/$\mathcal{W}_N$ shadow Postnikov tower: infinite |
| `thm:w-virasoro-genus1-hessian` | `theorem` | 4710 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | 4877 | $\mathcal{W}_3$ quintic obstruction |
| `thm:w-finite-arity-polynomial-pva` | `theorem` | 5199 | Finite-arity theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | 5237 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | 5279 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | 5306 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | 5382 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | 5407 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | 5441 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | 5479 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | 5499 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `prop:miura-arity-sharp` | `proposition` | 5583 | Miura arity bound is sharp |
| `thm:w-pbw-slodowy-collapse` | `theorem` | 5732 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | 5793 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-arity-detection` | `theorem` | 5901 | Canonical arity detection |
| `thm:w-bp-strict` | `theorem` | 5927 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | 5977 | $\mathcal{W}_4^{(2)}$ has canonical arity~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | 6036 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | 6095 | Subregular Appell formula |
| `thm:w-unbounded-canonical-arity` | `theorem` | 6133 | Unbounded canonical arity |
| `cor:w-subregular-arity-staircase` | `corollary` | 6162 | The subregular arity staircase |
| `thm:w-subregular-classification` | `theorem` | 6204 | Subregular classification |

#### `chapters/examples/w_algebras_deep.tex` (27)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 139 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 921 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `thm:master-commutative-square` | `theorem` | 1201 | Master commutative square for DS reduction |
| `prop:w3-deg3-vacuum` | `proposition` | 1608 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-bar-formality` | `proposition` | 1895 | DS--bar commutation via filtration formality |
| `thm:transport-closure-type-a` | `theorem` | 1965 | Transport-closure in type $A$ |
| `prop:partition-dependent-complementarity` | `proposition` | 2019 | Partition-dependent complementarity constant |
| `thm:ds-platonic-functor` | `theorem` | 2061 | DS reduction as a functor on platonic packages |
| `cor:ds-theta-descent` | `corollary` | 2280 | DS descent of the universal MC element |
| `comp:wn-stabilization-windows` | `computation` | 2380 | Coefficient stabilization windows for $\mathcal{W}_N$ |
| `prop:abelian-locus-type-a` | `proposition` | 2450 | Abelian locus in type~$A$ |
| `prop:abelianity-complementarity-independence` | `proposition` | 2492 | Independence of abelianity and complementarity |
| `prop:bfn-slodowy-dimensions` | `proposition` | 2560 | BFN--Slodowy dimension matching |
| `prop:ghost-constant-monotonicity` | `proposition` | 2633 | Ghost constant monotonicity |
| `thm:winfty-scalar` | `theorem` | 2781 | Scalar saturation of $\mathcal{W}_\infty$: the shadow tower collapses |
| `prop:gram-wt4` | `proposition` | 2932 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | 2997 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | 3040 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:virasoro-primitive` | `proposition` | 3223 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | 3284 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | 3325 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | 3428 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | 3461 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | 3482 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | 3514 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | 3620 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | 3656 | $\Walg_\infty$ bar-window series and Koszul entropy |

#### `chapters/examples/yangians_computations.tex` (45)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:yangian-rank-dependence` | `proposition` | 525 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 662 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 751 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 807 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 857 | DK-2 reduction to thick generation in category~\texorpdfstring{$\mathcal{O}$}{O} |
| `prop:dk2-thick-generation-typeA` | `proposition` | 909 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `cor:dk2-thick-generation-all-types` | `corollary` | 1003 | Thick generation for all simple types |
| `lem:composition-thick-generation` | `lemma` | 1028 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 1059 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 1143 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 1245 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 1267 | Finite-dimensional factorization Drinfeld--Kohno, type~\texorpdfstring{$A$}{A} |
| `cor:dk-partial-conj` | `corollary` | 1341 | Type-$A$ evaluation-generated extension principle |
| `cor:dk-poly-catO` | `corollary` | 1371 | Factorization DK for polynomial category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A} |
| `lem:fd-thick-closure` | `lemma` | 1443 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 1529 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 1779 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 1909 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 2067 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 2087 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 2112 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 2285 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:baxter-exact-triangles-opoly` | `theorem` | 2347 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `prop:baxter-yangian-equivariance` | `proposition` | 2435 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | 2509 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `thm:shifted-prefundamental-generation` | `theorem` | 2554 | $E_1$-chiral thick generation for $Y(\mathfrak{sl}_N)$ |
| `prop:prefundamental-clebsch-gordan` | `proposition` | 2780 | Universal prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | 2820 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | 2833 | $K_0$ generation for all simple types |
| `prop:categorical-cg-typeA` | `proposition` | 2882 | Categorical prefundamental CG decomposition, type~$A$ |
| `thm:mc3-type-a-resolution` | `theorem` | 3229 | MC3 resolution in type $A$ |
| `conj:mc3-arbitrary-type` | `theorem` | 3313 | Categorical prefundamental CG decomposition, all types |
| `cor:mc3-all-types` | `corollary` | 3460 | MC3 for all simple types |
| `prop:mc3-automatic-generalization` | `proposition` | 3491 | All MC3 components are type-independent |
| `prop:e8-root-uniformity` | `proposition` | 3571 | $E_8$ relevant-root uniformity |
| `prop:character-cg-all-types` | `proposition` | 3581 | Character-level Clebsch--Gordan for all simple types |
| `thm:yangian-vector-seed-propagation` | `theorem` | 3938 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | 3968 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | 3991 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | 4006 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | 4057 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | 4082 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | 4109 | Derived realization of the Baxter--Rees family |
| `thm:yangian-H2-reduction` | `theorem` | 4176 | $H^2$-reduction to the three-leg sector |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | 4253 | Concrete cocycle |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (84)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-dk-affine` | `theorem` | 127 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 226 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 391 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 495 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 621 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 670 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 807 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 995 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 1036 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 1306 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 1427 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 1630 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 1737 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 1835 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 2053 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 2136 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `thm:bridge-criterion` | `theorem` | 2313 | Bridge Criterion Theorem |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 2473 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 2593 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 2652 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 2735 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 2816 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 2847 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 2884 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 2951 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 2981 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 3012 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 3071 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 3150 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 3179 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 3246 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 3278 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 3316 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 3331 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 3381 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 3438 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 3485 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 3576 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 3676 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 3716 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 3752 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 3779 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 3922 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 3954 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 4004 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 4042 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 4069 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 4102 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 4140 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 4166 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 4362 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 4420 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 4455 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 4509 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 4542 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 4608 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 4683 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts-orig` | `corollary` | 4839 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet-orig` | `corollary` | 4868 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization-orig` | `corollary` | 4901 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization-orig` | `corollary` | 4932 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet-orig` | `corollary` | 4983 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 5090 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 5189 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 5250 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 5300 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 5359 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed-orig` | `corollary` | 5402 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line-orig` | `corollary` | 5435 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |
| `prop:free-propagator-matching` | `proposition` | 6113 | Free/$\beta\gamma$ propagator matching |
| `prop:affine-propagator-matching` | `proposition` | 6159 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `thm:spectral-derived-additive-kz` | `theorem` | 6327 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | 6378 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | 6430 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | 6504 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | 6588 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | 6646 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | 6688 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | 6723 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | 6778 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | 6850 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | 6874 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | 6915 | Exact free transport |
| `thm:spectral-conditional-strictification` | `theorem` | 6949 | Conditional strictification criterion |

#### `chapters/examples/yangians_foundations.tex` (42)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 248 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 335 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 368 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 427 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 468 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 523 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 587 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 1060 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1185 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1229 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1339 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1443 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1461 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1491 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1553 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 1617 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 1703 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 1800 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 1870 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 1939 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 1976 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2032 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2092 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2153 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2252 | Standard type-A fundamental line operator has the standard local residue |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | 2675 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | 2702 | Stabilized completed bar/cobar recovery |
| `cor:shifted-rtt-tower-convergence` | `corollary` | 2733 | Automatic tower convergence |
| `thm:shifted-rtt-mc-descent` | `theorem` | 2763 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | 2851 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | 2896 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | 2944 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | 2960 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | 2990 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | 3023 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | 3057 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | 3082 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | 3154 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | 3203 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | 3229 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | 3256 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | 3278 | Kleinian associated graded at the nilpotent point |

### Part III: Connections (615)

#### `chapters/connections/arithmetic_shadows.tex` (99)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:shadow-spectral-correspondence` | `theorem` | 59 | Shadow--spectral correspondence |
| `prop:divisor-sum-decomposition` | `proposition` | 165 | Divisor-sum decomposition |
| `cor:sewing-euler-product` | `corollary` | 190 | Euler product of the sewing determinant |
| `prop:sewing-trace-formula` | `proposition` | 203 | Sewing trace formula |
| `thm:sewing-selberg-formula` | `theorem` | 235 | Sewing--Selberg formula |
| `thm:narain-universality` | `theorem` | 292 | Narain universality |
| `thm:e8-epstein` | `theorem` | 323 | $E_8$ Epstein factorization |
| `prop:z2-epstein` | `proposition` | 348 | $\bZ^2$ Epstein zeta |
| `prop:leech-epstein` | `proposition` | 371 | Leech Epstein factorization |
| `prop:leading-hecke-identification` | `proposition` | 532 | Leading-order Hecke identification |
| `rem:hecke-all-orders` | `proposition` | 559 | Exactness of the Hecke identification |
| `prop:period-shadow-dictionary` | `proposition` | 611 | Period--shadow dictionary |
| `comp:period-shadow-vz` | `computation` | 694 | $V_{\bZ}$: the Gaussian archetype |
| `comp:period-shadow-ve8` | `computation` | 712 | $V_{E_8}$: the Lie/tree archetype |
| `comp:period-shadow-leech` | `computation` | 734 | $V_{\mathrm{Leech}}$: the Ramanujan archetype |
| `comp:period-shadow-rank24-comparison` | `computation` | 787 | $D_{16}^+ \oplus D_{16}^+$ vs.\ $E_8^3$: same depth, different coefficient |
| `comp:period-shadow-rank2` | `computation` | 806 | $V_{\bZ^2}$ and $V_{A_2}$: Dedekind zeta at depth~$2$ |
| `thm:spectral-decomposition-principle` | `theorem` | 830 | Spectral decomposition principle |
| `prop:growth-rate-dictionary` | `proposition` | 917 | Growth-rate dictionary |
| `thm:bg-vir-coincidence` | `theorem` | 943 | $\beta\gamma$--Virasoro rate coincidence |
| `prop:self-referentiality-criterion` | `proposition` | 961 | Self-referentiality criterion |
| `cor:conformal-vector-infinite-depth` | `corollary` | 1031 | Conformal vector implies infinite depth |
| `thm:shadow-tower-asymptotics` | `theorem` | 1054 | Shadow tower leading asymptotics |
| `cor:rigorous-infinite-depth` | `corollary` | 1086 | Rigorous infinite depth |
| `prop:bg-primary-counting` | `proposition` | 1121 | $\beta\gamma$ primary-counting function |
| `thm:refined-shadow-spectral` | `theorem` | 1134 | Refined shadow--spectral correspondence |
| `prop:ising-d-arith` | `proposition` | 1164 | Ising model: $d_{\mathrm{arith}} = 0$ |
| `rem:non-unimodular` | `remark` | 1213 | Non-unimodular lattices |
| `thm:depth-decomposition` | `theorem` | 1282 | Depth decomposition |
| `thm:ainfty-formality-depth` | `theorem` | 1379 | $A_\infty$ formality criterion |
| `thm:interacting-gram-positivity` | `theorem` | 1437 | Interacting Gram positivity |
| `cor:virasoro-interacting-gram` | `corollary` | 1477 | — |
| `thm:shadow-resonance-locus` | `theorem` | 1490 | — |
| `prop:shadow-spectral-measure` | `theorem` | 1528 | Shadow spectral measure |
| `prop:carleman-virasoro` | `proposition` | 1594 | Carleman rigidity |
| `prop:shadow-periods` | `proposition` | 1631 | Shadow amplitudes are periods |
| `thm:spectral-curve` | `theorem` | 1775 | Algebraic shadow generating function |
| `prop:moment-matrix-negativity` | `proposition` | 1817 | Eisenstein moment minor |
| `thm:shadow-higgs-field` | `theorem` | 1850 | Shadow Higgs field |
| `thm:general-nahc` | `theorem` | 1931 | General shadow triple |
| `thm:shadow-bps` | `theorem` | 2098 | The shadow tower as BPS spectrum |
| `thm:general-bps` | `theorem` | 2177 | General BPS spectrum of the shadow tower |
| `thm:sewing-shadow-intertwining` | `theorem` | 2222 | Sewing--shadow intertwining at genus~$1$ |
| `cor:shadow-fredholm` | `corollary` | 2297 | Shadow Fredholm determinant |
| `cor:spectral-measure-identification` | `corollary` | 2334 | Spectral measure identification |
| `sec:shadow-moduli-resolution` | `theorem` | 2388 | Shadow-moduli resolution |
| `thm:universality-of-G` | `theorem` | 2478 | Universality of $G$ |
| `prop:mc-bracket-determines-atoms` | `proposition` | 2546 | MC bracket determines spectral atoms |
| `rem:mc-ramanujan-bridge` | `remark` | 2596 | The bridge to the Ramanujan bound |
| `thm:spectral-continuation-bridge` | `theorem` | 2641 | Hecke-equivariant MC element |
| `thm:schur-complement-quartic` | `theorem` | 2780 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | 2839 | — |
| `prop:on-off-line-distinction` | `proposition` | 2916 | — |
| `prop:pure-spin-s-schur` | `proposition` | 3346 | — |
| `prop:prime-side-defect-formula` | `proposition` | 3454 | — |
| `thm:finite-miura-defect` | `theorem` | 3524 | Finite Miura defect at genus one |
| `prop:modularity-constraint` | `proposition` | 4098 | Modularity constraint on the spectral measure |
| `sec:bracket-hodge-index` | `proposition` | 4141 | Bracket positivity and the Hodge index |
| `sec:proved-regime-ramanujan` | `proposition` | 4267 | Ramanujan bound for lattice spectral measures |
| `sec:symmetric-power-route` | `proposition` | 4310 | Shadow--symmetric power identification |
| `thm:petersson-identification` | `theorem` | 4458 | Petersson identification |
| `prop:modularity-constraint-atoms` | `proposition` | 4544 | Modularity constraint on atoms |
| `prop:rigidity-threshold` | `proposition` | 4581 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | 4656 | Lattice Ramanujan from rigidity |
| `thm:cps-from-mc` | `theorem` | 4761 | CPS hypotheses from MC $+$ HS-sewing |
| `cor:moment-automorphy` | `corollary` | 4808 | Automorphy of moment $L$-functions |
| `prop:stieltjes-signed-universal` | `proposition` | 4837 | Universal signed Stieltjes measure |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | 4870 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | 4934 | Shadow arithmetic trichotomy |
| `thm:shadow-multiplicativity-low-arity` | `theorem` | 5007 | Shadow-level multiplicativity at arities~$\le 5$ |
| `thm:mc-recursion-moment` | `theorem` | 5153 | MC recursion on moment $L$-functions |
| `prop:shadow-chiral-graph` | `proposition` | 5222 | Shadow amplitudes as chiral graph integrals |
| `thm:hecke-newton-lattice` | `theorem` | 5295 | Hecke--Newton closure for lattice VOAs |
| `cor:unconditional-lattice` | `corollary` | 5358 | Unconditional operadic RS for lattice VOAs |
| `thm:non-lattice-ramanujan` | `theorem` | 5387 | Non-lattice Ramanujan bound |
| `thm:hecke-verdier-commutation` | `theorem` | 5908 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | 5947 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | 6022 | Theta decomposition bridge |
| `prop:newton-shadow-hecke` | `proposition` | 6085 | Newton--shadow--Hecke correspondence |
| `prop:sewing-spectral-bridge` | `proposition` | 6203 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | 6308 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | 6355 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | 6413 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | 6588 | Genus-one saddle triviality |
| `cor:first-scattering-pole` | `corollary` | 6788 | Nonvanishing at the first scattering pole |
| `thm:scattering-coupling-factorization` | `theorem` | 6890 | Scattering coupling factorization |
| `thm:structural-separation` | `theorem` | 6973 | Structural separation of algebraic and arithmetic content |
| `prop:hecke-defect-equivalences` | `proposition` | 7099 | Equivalent characterizations; \textup{(i)--(iii)} ; \textup{(iv)} |
| `prop:hecke-defect-lattice` | `proposition` | 7150 | Hecke defect vanishes for lattice VOAs |
| `thm:rigidity-inheritance` | `theorem` | 7197 | Rigidity inheritance |
| `thm:packet-connection-flatness` | `theorem` | 7500 | Flatness and divisor independence |
| `cor:lattice-packet-diagonal` | `corollary` | 7567 | Lattice transparency |
| `prop:gauge-criterion-scattering` | `proposition` | 7633 | Gauge criterion for scattering access |
| `prop:miura-packet-splitting` | `proposition` | 7756 | — |
| `prop:genus2-non-diagonal` | `proposition` | 7893 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | 7937 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | 8069 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | 8101 | B\"ocherer bridge |
| `thm:leech-chi12-projection` | `theorem` | 8220 | Leech $\chi_{12}$-projection and Waldspurger consequence |

#### `chapters/connections/bv_brst.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:log-form-ghost-law` | `theorem` | 292 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 395 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 546 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `thm:bar-semi-infinite-km` | `theorem` | 642 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 746 | Anomaly duality for Kac--Moody pairs |
| `cor:anomaly-duality-w` | `corollary` | 904 | Curvature complementarity for principal \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |

#### `chapters/connections/concordance.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 313 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 327 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | 616 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 640 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 677 | Gaussian collapse for abelian input |
| `prop:five-theorems-mc-projections` | `proposition` | 2053 | Five main theorems as MC projections |
| `thm:operadic-complexity-concordance` | `theorem` | 2220 | Operadic complexity |
| `prop:vol2-relative-holographic-bridge` | `proposition` | 3634 | Relative holographic deformation bridge |
| `prop:vol2-ribbon-thooft-bridge` | `proposition` | 3655 | Ribbon/'t~Hooft bridge |
| `thm:lagrangian-complementarity` | `theorem` | 3966 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 4237 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 4574 | Discriminant as spectral determinant, verified cases |
| `thm:discriminant-spectral` | `theorem` | 4619 | Spectral discriminant, general case |
| `comp:spectral-discriminants-standard` | `computation` | 4843 | Spectral discriminants of standard families |
| `thm:family-index` | `theorem` | 4908 | Family index theorem for genus expansions |
| `rem:programme-vi-verification` | `remark` | 5937 | Programme VI: systematic verification of (H1)--(H4) |

#### `chapters/connections/editorial_constitution.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-pbw` | `theorem` | 191 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 217 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, resolved)} |
| `prop:en-n2-recovery` | `proposition` | 1608 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1754 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1812 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1846 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1862 | Physical anomaly cancellation for affine Kac--Moody algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2089 | Hodge symmetry from complementarity |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 2402 | Volume~I concrete modular datum |

#### `chapters/connections/entanglement_modular_koszul.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ent-scalar-entropy` | `theorem` | 136 | Entanglement entropy at the scalar level |
| `thm:entanglement-complementarity` | `theorem` | 212 | Entanglement complementarity |
| `prop:ent-complexity-classification` | `proposition` | 328 | Entanglement complexity classification |
| `cor:ent-full-entropy` | `corollary` | 426 | Full entanglement entropy |
| `prop:ent-qes` | `proposition` | 458 | QES from shadow connection |
| `thm:ent-landscape-census` | `theorem` | 538 | Standard landscape entanglement census |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 112 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 191 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 296 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 341 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 368 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 408 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 426 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 447 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 494 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 553 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 909 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 941 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (42)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | 137 | Protected dual transform and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | 235 | Protected transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | 288 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | 329 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | 382 | Scalar fixed-point rigidity and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | 495 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | 608 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | 729 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | 800 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | 932 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | 1012 | The first nonlinear holographic anomaly |
| `thm:yangian-shadow-theorem` | `theorem` | 1393 | Yangian-shadow theorem |
| `thm:sphere-reconstruction` | `theorem` | 1450 | Sphere reconstruction |
| `thm:quartic-resonance-obstruction` | `theorem` | 1530 | Quartic resonance obstruction |
| `thm:collision-residue-twisting` | `theorem` | 1954 | Collision residue = universal twisting morphism |
| `thm:collision-depth-2-ybe` | `theorem` | 2010 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `thm:shadow-connection-kz` | `theorem` | 2048 | Shadow connection for affine Kac--Moody = KZ |
| `cor:shadow-connection-heisenberg` | `corollary` | 2091 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | 2112 | Shadow connection for Virasoro recovers BPZ |
| `thm:quartic-obstruction-linf` | `theorem` | 2148 | Quartic obstruction = $L_\infty$ obstruction |
| `comp:holographic-ss-sl2` | `computation` | 2232 | The $E_1$ page for $\widehat{\mathfrak{sl}}_2$ |
| `comp:holographic-ss-vir` | `computation` | 2284 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | 2328 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | 2351 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | 2427 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | 2450 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | 2490 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | 2581 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | 2637 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | 2732 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | 2766 | Holographic datum for $\mathcal W_3$ |
| `thm:ds-central-charge-additivity` | `theorem` | 2886 | Central charge additivity under DS |
| `cor:critical-dimensions` | `corollary` | 2987 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | 3098 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | 3122 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | 3158 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | 3183 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | 3295 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | 3431 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | 3606 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | 3730 | Lifts as relative MC elements |
| `cor:holographic-deformation-cohomology` | `corollary` | 3761 | — |

#### `chapters/connections/genus_complete.tex` (27)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 235 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 290 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 372 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 649 | Bar complex computes moduli integrals |
| `thm:full-modular-invariant-hierarchy` | `theorem` | 1206 | The full modular invariant hierarchy |
| `prop:hs-trace-class` | `proposition` | 1367 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | 1382 | General HS-sewing criterion |
| `cor:hs-sewing-standard-landscape` | `corollary` | 1414 | Standard landscape |
| `cor:hs-implies-gram` | `corollary` | 1452 | — |
| `thm:heisenberg-one-particle-sewing` | `theorem` | 1471 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | 1548 | Positive grading implies conilpotency |
| `prop:dirichlet-weight-formula` | `theorem` | 1850 | — |
| `cor:virasoro-mode-removal` | `corollary` | 1908 | — |
| `prop:euler-koszul-criterion` | `theorem` | 1967 | — |
| `comp:euler-koszul-defect-table` | `computation` | 2004 | Euler--Koszul defect table for the standard landscape |
| `prop:zeta-zeros-defect-derivative` | `proposition` | 2096 | — |
| `thm:li-closed-form` | `theorem` | 2134 | — |
| `prop:li-asymptotics` | `theorem` | 2167 | — |
| `prop:surface-moment-positivity` | `theorem` | 2295 | Gram positivity |
| `cor:virasoro-gram-ratio` | `corollary` | 2318 | — |
| `thm:sewing-rkhs` | `theorem` | 2353 | Sewing RKHS |
| `prop:collapse-permanence` | `proposition` | 2420 | Collapse permanence |
| `rem:benjamin-chang-bridge` | `proposition` | 2459 | — |
| `thm:shadow-euler-independence` | `theorem` | 2485 | — |
| `rem:two-faces-theta` | `corollary` | 2542 | — |
| `thm:euler-koszul-tier-classification` | `theorem` | 2624 | — |
| `thm:sewing-hecke-reciprocity` | `theorem` | 2705 | Sewing--Hecke reciprocity |

#### `chapters/connections/holographic_codes_koszul.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:hc-knill-laflamme` | `proposition` | 92 | Knill--Laflamme from Lagrangian isotropy |
| `thm:hc-koszulness-exact-qec` | `theorem` | 231 | \textbf{G12}: Koszulness $\Leftrightarrow$ exact quantum error correction |
| `thm:hc-shadow-redundancy` | `theorem` | 349 | Shadow depth controls redundancy |
| `thm:hc-dictionary` | `proposition` | 450 | 12-fold dictionary |
| `thm:hc-census` | `theorem` | 573 | Standard landscape code census |

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
| `prop:feynman-graph-complex` | `proposition` | 406 | Feynman transform and algebraic graph-complex refinement |

#### `chapters/connections/outlook.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:operadic-complexity` | `theorem` | 235 | Operadic complexity |

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
| `prop:transgression-kills-curvature` | `proposition` | 126 | Transgression kills curvature |
| `prop:g9-quotient` | `proposition` | 203 | Quotient identification |
| `prop:secondary-anomaly-properties` | `proposition` | 301 | Properties of $u$ |
| `prop:g9-ses-transgression` | `proposition` | 377 | Short exact sequence of the transgression |
| `cor:g9-bockstein` | `corollary` | 416 | Bockstein long exact sequence |
| `thm:clifford-relations` | `theorem` | 504 | Clifford relations for handle operators |
| `thm:topological-regime` | `theorem` | 744 | Topological regime |
| `thm:gravitational-regime` | `theorem` | 815 | Gravitational regime |
| `thm:critical-string-dichotomy` | `theorem` | 992 | Critical string dichotomy for the Virasoro |
| `thm:ghost-sector-c26` | `theorem` | 1152 | Ghost sector at $c = 26$ |
| `thm:vir-self-duality-c13` | `theorem` | 1225 | Virasoro self-duality at $c = 13$ |
| `thm:critical-dichotomy-summary` | `theorem` | 1294 | Critical string dichotomy: structural summary |
| `prop:shadow-critical` | `proposition` | 1370 | Shadow tower at critical central charges |
| `prop:hodge-clifford` | `proposition` | 1432 | Hodge--Clifford compatibility |
| `prop:clifford-spectral-degeneration` | `proposition` | 1510 | Degeneration |
| `prop:bosonic-string-identifications` | `proposition` | 1540 | Bosonic string structural identifications |
| `thm:localization-sequence` | `theorem` | 1719 | Localization sequence |
| `cor:g9-localization-vir` | `corollary` | 1767 | Localization for the Virasoro |
| `prop:g9-bialgebra` | `proposition` | 1817 | Bialgebra extension |
| `cor:g9-u-coproduct` | `corollary` | 1848 | Coproduct of the secondary anomaly |
| `prop:g9-universal` | `proposition` | 1899 | Universal property |
| `cor:g9-comparison-universal` | `corollary` | 1936 | The comparison map is universal |
| `prop:g9-clifford-deformation` | `proposition` | 1962 | Deformation of the Clifford algebra |
| `prop:g9-trace-formula` | `proposition` | 2037 | Trace formula |
| `cor:g9-partition-trace` | `corollary` | 2061 | Genus-$g$ partition function via trace |

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
| `prop:thqg-X-sewing-filtration` | `proposition` | 192 | Sewing envelope: conformal weight filtration |
| `lem:thqg-X-sewing-schatten` | `lemma` | 330 | Schatten class properties of $\sewop_q$ |
| `lem:thqg-X-composition-decay` | `lemma` | 444 | Exponential decay of composition coefficients |
| `prop:thqg-X-second-quantization` | `proposition` | 482 | Second quantization |
| `thm:thqg-X-heisenberg-sewing-full` | `theorem` | 562 | Heisenberg sewing theorem: full development |
| `prop:polyakov-alvarez-shadow-specialization` | `proposition` | 866 | Polyakov--Alvarez as shadow metric specialization |
| `thm:thqg-X-genus-1-fredholm` | `theorem` | 945 | Genus-1 Fredholm determinant |
| `comp:thqg-X-genus-1-series` | `computation` | 1048 | Genus-1 Fredholm determinant: explicit series |
| `thm:thqg-X-genus-2-fredholm` | `theorem` | 1093 | Genus-2 Fredholm determinant |
| `comp:thqg-X-genus-2-series` | `computation` | 1201 | Genus-2 Fredholm determinant: leading terms |
| `thm:thqg-X-genus-3-fredholm` | `theorem` | 1228 | Genus-3 Fredholm determinant |
| `thm:thqg-X-general-genus-fredholm` | `theorem` | 1348 | General-genus Fredholm structure |
| `prop:thqg-X-free-energy-ahat` | `proposition` | 1422 | Free energy: $\hat{A}$-genus verification |
| `thm:thqg-X-class-G-fredholm` | `theorem` | 1494 | Fredholm partition function for class-G algebras |
| `prop:thqg-X-rank-additivity` | `proposition` | 1589 | Rank additivity |
| `thm:thqg-X-feynman-expansion` | `theorem` | 1656 | Feynman integral expansion |
| `prop:thqg-X-class-L-feynman` | `proposition` | 1719 | Class-L Feynman integrals |
| `prop:thqg-X-class-C-quartic` | `proposition` | 1813 | Class-C quartic contact |
| `prop:thqg-X-virasoro-decomposition` | `proposition` | 1897 | Virasoro: Fredholm base + corrections |
| `prop:thqg-X-analytic-bar-bounded` | `proposition` | 1993 | Analytic bar differential is bounded |
| `prop:thqg-X-analytic-coproduct` | `proposition` | 2021 | Analytic coproduct |
| `prop:thqg-X-coderived-fredholm-G` | `proposition` | 2101 | Coderived = Fredholm for class~G |
| `prop:givental-vertex-reconstruction` | `proposition` | 2370 | Givental reconstruction of higher-genus vertex factors |
| `thm:gravitational-complementarity-genus-expansion` | `theorem` | 2490 | Gravitational complementarity genus expansion |
| `prop:virasoro-F2-full` | `proposition` | 2605 | Full genus-$2$ free energy for Virasoro |
| `prop:cohft-complementarity` | `proposition` | 2656 | CohFT complementarity |

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
| `thm:thqg-lie-termination` | `theorem` | 495 | Lie termination |
| `thm:thqg-contact-termination` | `theorem` | 560 | Contact termination |
| `prop:thqg-cubic-gauge` | `proposition` | 594 | Cubic gauge triviality mechanism |
| `thm:thqg-virasoro-quintic` | `theorem` | 622 | Virasoro quintic obstruction |
| `thm:thqg-virasoro-infinite` | `theorem` | 657 | Virasoro shadow tower is infinite |
| `thm:thqg-virasoro-tower-explicit` | `theorem` | 700 | Virasoro shadow tower through septic order |
| `prop:thqg-virasoro-structure` | `proposition` | 776 | Structural properties of the Virasoro tower |
| `thm:thqg-virasoro-potential` | `theorem` | 828 | Virasoro complementarity potential |
| `thm:thqg-genus1-hessian` | `theorem` | 875 | Genus-$1$ Hessian correction |
| `cor:thqg-virasoro-genus1` | `corollary` | 891 | Virasoro genus-$1$ Hessian |
| `thm:thqg-genus2-diagnostic` | `theorem` | 935 | Genus-$2$ binary diagnostic |
| `thm:thqg-obstruction-table` | `theorem` | 998 | Complete obstruction data through arity~$6$ |
| `thm:thqg-vanishing-mechanisms` | `theorem` | 1072 | Classification of vanishing mechanisms |
| `thm:thqg-independent-sum` | `theorem` | 1112 | Independent sum factorization |
| `prop:thqg-depth-koszulness-independent` | `proposition` | 1144 | Depth and Koszulness are independent |
| `cor:thqg-duality-table` | `corollary` | 1195 | Duality-complexity table |
| `prop:thqg-tropical-profiles` | `proposition` | 1233 | Tropical profiles |
| `thm:thqg-holographic-type` | `theorem` | 1270 | Primary-line shadow profile from the depth class |
| `prop:thqg-wn-stabilization` | `proposition` | 1324 | $\mathcal{W}_N$ complexity stabilises |
| `thm:thqg-grav-landscape` | `theorem` | 1353 | Gravitational complexity census |
| `thm:thqg-g2-main` | `maintheorem` | 1401 | Shadow-depth classification; result (G2) |
| `prop:thqg-complexity-functor` | `proposition` | 1449 | Functoriality of complexity |
| `prop:thqg-coefficient-asymptotics` | `proposition` | 1524 | Coefficient asymptotics |
| `prop:thqg-generic-constancy` | `proposition` | 1593 | Generic constancy |
| `thm:thqg-mc-euler-lagrange` | `theorem` | 1648 | Primary-line MC critical-point equation |
| `thm:thqg-holographic-ss` | `theorem` | 1746 | Collision-filtration spectral sequence |
| `prop:thqg-collapse-criteria` | `proposition` | 1780 | Collapse criteria by complexity class |
| `prop:thqg-e1-virasoro` | `proposition` | 1834 | $E_1$ page for Virasoro |
| `prop:thqg-collapse-L` | `proposition` | 1881 | Collapse for class~$\mathbf{L}$ |
| `prop:thqg-collapse-C` | `proposition` | 1905 | Collapse for class~$\mathbf{C}$ |
| `prop:thqg-curve-independence` | `proposition` | 1950 | Curve independence |

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
| `thm:thqg-IV-kz-duality` | `theorem` | 755 | KZ duality |
| `prop:thqg-IV-bpz-duality` | `proposition` | 791 | BPZ duality from $S$-duality |
| `prop:shadow-connection-s-duality` | `proposition` | 843 | Shadow connection $S$-duality |
| `thm:thqg-IV-local-system-duality` | `theorem` | 914 | Local system duality |
| `prop:thqg-IV-monodromy-duality` | `proposition` | 948 | Monodromy eigenvalue reciprocation |
| `prop:thqg-IV-heisenberg-K` | `proposition` | 1028 | Heisenberg complementarity |
| `thm:thqg-IV-km-K` | `theorem` | 1055 | Affine Kac--Moody complementarity |
| `prop:thqg-IV-bc-bg-K` | `proposition` | 1133 | \texorpdfstring{$bc$--$\beta\gamma$}{bc-betagamma} complementarity |
| `prop:thqg-IV-lattice-K` | `proposition` | 1167 | Lattice complementarity |
| `thm:thqg-IV-virasoro-K` | `theorem` | 1184 | Virasoro complementarity |
| `thm:thqg-IV-w-K` | `theorem` | 1234 | Principal $\mathcal{W}$-algebra complementarity |
| `prop:thqg-IV-conductor-growth` | `proposition` | 1313 | Koszul conductor asymptotics |
| `thm:thqg-IV-exponent-sum` | `theorem` | 1332 | Exponent sum formula |
| `thm:ds-complementarity-tower` | `theorem` | 1457 | DS complementarity tower |
| `cor:level-independence-filtration` | `corollary` | 1588 | Level-independence filtration |
| `thm:sigma-ring-finite-generation` | `theorem` | 1650 | Recursive determination of $(\cA^{\mathrm{sh}})^\sigma$ |
| `thm:thqg-IV-c26` | `theorem` | 1712 | The $c = 26$ degeneration |
| `prop:thqg-IV-c13` | `proposition` | 1766 | The $c = 13$ self-dual point |
| `thm:thqg-IV-critical-degeneration` | `theorem` | 1809 | Critical-level degeneration |
| `prop:thqg-IV-self-dual-classification` | `proposition` | 1860 | Classification of self-dual points |
| `thm:thqg-IV-four-facets` | `theorem` | 1932 | Four-facet decomposition |
| `thm:thqg-IV-free-energy` | `theorem` | 2002 | Free energy complementarity |
| `cor:thqg-IV-self-dual-generating` | `corollary` | 2031 | Self-dual generating function |
| `prop:thqg-IV-partition-duality` | `proposition` | 2037 | Partition function functional equation |
| `prop:thqg-IV-holographic-datum` | `proposition` | 2118 | Holographic modular Koszul datum under $S$-duality |
| `prop:thqg-IV-naturality` | `proposition` | 2187 | Naturality of $\mathcal{S}$ |
| `prop:thqg-IV-clutching` | `proposition` | 2204 | Clutching compatibility |
| `prop:thqg-IV-spectral-duality` | `proposition` | 2296 | Spectral sequence duality |
| `cor:thqg-IV-e2-duality` | `corollary` | 2315 | $E_2$ duality |
| `cor:thqg-IV-degeneration` | `corollary` | 2322 | Degeneration preservation |
| `thm:thqg-IV-cc-sum` | `theorem` | 2387 | Central charge sum |

#### `chapters/connections/thqg_gravitational_yangian.tex` (31)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-V-collision-lie-compatibility` | `lemma` | 167 | Lie compatibility of the collision filtration |
| `prop:thqg-V-depth-zero` | `proposition` | 213 | Associated graded at depth zero |
| `prop:thqg-V-depth-one` | `proposition` | 251 | Associated graded at depth one |
| `prop:thqg-V-collapse-criterion` | `proposition` | 316 | Collapse criterion from shadow depth |
| `lem:thqg-V-collision-nilpotent` | `lemma` | 389 | Nilpotency of the collision differential |
| `prop:thqg-V-arnold-cohomology` | `proposition` | 412 | Arnold cohomology and collision forms |
| `prop:thqg-V-poincare-collision` | `proposition` | 481 | Poincar\'e polynomial of the collision filtration |
| `thm:thqg-V-collision-twisting` | `theorem` | 576 | Collision residue = twisting morphism, revisited |
| `comp:thqg-V-heisenberg-r` | `computation` | 642 | Heisenberg $r$-matrix |
| `comp:thqg-V-affine-r` | `computation` | 692 | Affine Kac--Moody $r$-matrix |
| `comp:thqg-V-virasoro-r` | `computation` | 748 | Virasoro $r$-matrix |
| `prop:thqg-V-gravitational-propagator` | `proposition` | 867 | Gravitational propagator from collision residue |
| `thm:thqg-V-cybe-from-arnold` | `theorem` | 1011 | CYBE from the Arnold relation via MC |
| `cor:thqg-V-ibr` | `corollary` | 1138 | Infinitesimal braid relation |
| `prop:thqg-V-ainfty-ybe` | `proposition` | 1182 | $A_\infty$-enhancement of the CYBE |
| `prop:thqg-V-n-point-ybe-proof` | `proposition` | 1259 | $n$-point YBE from boundary of $\overline{\mathcal{M}}_{0,n+1}$ |
| `prop:thqg-V-yangian-differential` | `proposition` | 1377 | Differential structure |
| `thm:thqg-V-pro-mc-element` | `theorem` | 1419 | The pro-MC element $R^{\mathrm{mod}}_\cA$ |
| `cor:thqg-V-genus-zero-r` | `corollary` | 1474 | Genus-$0$ component = classical $r$-matrix |
| `cor:thqg-V-genus-one-correction` | `corollary` | 1487 | Genus-$1$ correction |
| `prop:thqg-V-pro-mc-convergence` | `proposition` | 1584 | Convergence of the pro-MC element |
| `prop:thqg-V-rtt-from-sgybe` | `proposition` | 1657 | RTT relation from the sgYBE |
| `comp:thqg-V-three-graviton` | `computation` | 1817 | Three-graviton vertex |
| `comp:thqg-V-quartic-graviton` | `computation` | 1858 | Quartic graviton vertex and contact invariant |
| `prop:thqg-V-verma-gravitational` | `proposition` | 1918 | Verma modules as gravitational representations |
| `prop:thqg-V-c13-self-duality` | `proposition` | 1990 | Self-duality of the gravitational Yangian at $c = 13$ |
| `thm:thqg-V-mc3-thick-generation` | `theorem` | 2119 | MC3 thick generation via the gravitational Yangian |
| `cor:thqg-V-dk5-type-a` | `corollary` | 2184 | DK-5 accessibility |
| `comp:thqg-V-heis-yangian` | `computation` | 2350 | Gravitational Yangian of Heisenberg |
| `comp:thqg-V-affine-yangian` | `computation` | 2369 | Gravitational Yangian of affine KM |
| `comp:thqg-V-vir-yangian-summary` | `computation` | 2391 | Gravitational Yangian of $\mathrm{Vir}_c$ |

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
| `prop:postnikov-filtration-structure` | `proposition` | 1645 | Structure of the Postnikov filtration |
| `prop:mc-formal-moduli` | `proposition` | 1690 | The MC moduli as a formal moduli problem |
| `thm:holographic-reconstruction` | `theorem` | 1735 | Finite-order shadow reconstruction theorem |
| `prop:shapovalov-shadow-singularities` | `proposition` | 1863 | Shapovalov singularities of the shadow tower |
| `prop:pole-structure-shadow-series` | `proposition` | 1908 | Pole structure of the full shadow series |
| `comp:shapovalov-zeros-shadow` | `computation` | 1963 | Shapovalov zeros and shadow singularities |
| `thm:complexity-hierarchy` | `theorem` | 2045 | Complexity hierarchy |

#### `chapters/connections/thqg_introduction_supplement_body.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `conj:thqg-intro-operadic-complexity` | `theorem` | 837 | Operadic complexity; ; Theorem~\ref{thm:operadic-complexity} |

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

#### `chapters/connections/thqg_open_closed_realization.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-brace-dg-algebra` | `theorem` | 172 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | 325 | Universal open/closed pair --- chiral Swiss-cheese theorem |
| `thm:thqg-local-global-bridge` | `theorem` | 419 | Local-global bridge |
| `thm:thqg-annulus-trace` | `theorem` | 520 | Annulus trace theorem |
| `thm:thqg-oc-mc-equation` | `theorem` | 600 | Open/closed MC equation |
| `thm:thqg-oc-projection` | `theorem` | 661 | Open/closed projection principle |
| `thm:thqg-oc-quartic-vanishing` | `theorem` | 761 | Vanishing and nonvanishing of $\mathfrak{R}^{\mathrm{oc}}_{4}$ |

#### `chapters/connections/thqg_perturbative_finiteness.tex` (36)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-I-completeness` | `lemma` | 69 | Completeness and separability |
| `prop:thqg-I-inclusion-maps` | `proposition` | 79 | Inclusion maps |
| `lem:thqg-I-schatten` | `lemma` | 120 | Schatten class hierarchy |
| `prop:thqg-I-uniform-trace-bound` | `proposition` | 360 | Uniform bound on the trace |
| `cor:thqg-I-genus-g-partition` | `corollary` | 374 | Genus-$g$ partition function |
| `thm:thqg-I-absolute-convergence` | `theorem` | 531 | Absolute convergence of the generating function |
| `prop:thqg-I-Fg-values` | `proposition` | 564 | Shadow free energies through genus $10$ |
| `prop:thqg-I-partial-sums` | `proposition` | 628 | Cumulative partial sums |
| `thm:thqg-I-perturbative-finiteness` | `theorem` | 684 | Perturbative finiteness of twisted gravity |
| `prop:thqg-I-koszulness-finiteness` | `proposition` | 733 | Koszulness and finiteness |
| `prop:thqg-I-graph-count` | `proposition` | 756 | Effective graph count |
| `prop:thqg-I-genus-g-decomposition` | `proposition` | 772 | Genus-$g$ amplitude decomposition |
| `prop:thqg-I-exponential-rep` | `proposition` | 907 | Exponential representation |
| `prop:thqg-I-heisenberg-detail` | `proposition` | 983 | Heisenberg: detailed HS verification |
| `prop:thqg-I-affine-detail` | `proposition` | 1001 | Affine Kac--Moody: detailed HS verification |
| `prop:thqg-I-virasoro-detail` | `proposition` | 1020 | Virasoro: detailed HS verification |
| `prop:thqg-I-convergence-radii` | `proposition` | 1041 | Convergence radii of the scalar partition function |
| `thm:thqg-I-btz` | `theorem` | 1158 | BTZ partition function from shadow theory |
| `prop:thqg-I-btz-higher-genus` | `proposition` | 1183 | Higher-genus BTZ corrections |
| `prop:thqg-I-1c-expansion` | `proposition` | 1249 | Leading gravitational coupling expansion |
| `prop:thqg-I-newton-expansion` | `proposition` | 1263 | Newton's constant expansion |
| `prop:thqg-I-graph-sum-sewing` | `proposition` | 1383 | Graph-sum representation of sewing amplitudes |
| `prop:thqg-I-graph-sum-convergence` | `proposition` | 1403 | Convergence of the graph sum at fixed genus |
| `prop:thqg-I-consistency` | `proposition` | 1429 | Consistency of algebraic and analytic finiteness |
| `thm:thqg-I-full-convergence` | `theorem` | 1450 | Full partition function convergence |
| `prop:thqg-I-hs-filtration` | `proposition` | 1525 | HS-sewing and the strong filtration |
| `prop:thqg-I-effective-bound` | `proposition` | 1547 | Effective bound on the genus-$g$ free energy |
| `cor:thqg-I-tail-bound` | `corollary` | 1567 | Tail bound for the genus expansion |
| `thm:thqg-I-2d-convergence` | `theorem` | 1603 | Two-dimensional convergence |
| `cor:thqg-I-heisenberg-selberg` | `corollary` | 1685 | Heisenberg partition function via Selberg zeta |
| `prop:polyakov-chern-weil` | `proposition` | 1739 | Polyakov formula as Chern--Weil image of the arity-$2$ shadow |
| `prop:thqg-I-pole-structure` | `proposition` | 1781 | Pole structure of the meromorphic continuation |
| `prop:thqg-I-tensor-product` | `proposition` | 1887 | Finiteness for tensor-product theories |
| `comp:thqg-I-fp-detailed` | `computation` | 1938 | Faber--Pandharipande coefficients through genus $15$ |
| `prop:thqg-I-asymptotic-precision` | `proposition` | 1973 | Asymptotic precision |
| `prop:thqg-I-fp-monotone` | `proposition` | 1989 | Monotonicity of the FP coefficients |

#### `chapters/connections/thqg_soft_graviton_theorems.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-VI-arity-decomposition` | `proposition` | 228 | Arity decomposition of the shadow connection |
| `thm:thqg-VI-flatness-by-arity` | `theorem` | 271 | Flatness by arity |
| `thm:thqg-VI-ward-determines-correlators` | `theorem` | 432 | Shadow Ward identities determine correlators |
| `prop:thqg-VI-kappa-action` | `proposition` | 572 | Action of $\kappa$ on conformal blocks |
| `thm:thqg-VI-leading-soft` | `theorem` | 627 | Leading soft graviton theorem |
| `cor:thqg-VI-bms-supertranslation` | `corollary` | 717 | BMS supertranslation Ward identity |
| `prop:thqg-VI-cubic-action` | `proposition` | 785 | Cubic shadow action on conformal blocks |
| `thm:thqg-VI-subleading-soft` | `theorem` | 827 | Subleading soft graviton theorem |
| `thm:thqg-VI-cubic-gauge-triviality` | `theorem` | 905 | Cubic gauge triviality and subleading soft theorems |
| `cor:thqg-VI-superrotation` | `corollary` | 978 | Superrotation Ward identity |
| `prop:thqg-VI-quartic-action` | `proposition` | 1078 | Quartic shadow action on conformal blocks |
| `thm:thqg-VI-virasoro-quartic` | `theorem` | 1114 | Virasoro quartic contact coefficient |
| `thm:thqg-VI-clutching-law` | `theorem` | 1241 | Clutching law for the quartic contact invariant |
| `comp:thqg-VI-virasoro-clutching` | `computation` | 1329 | Clutching law for Virasoro |
| `thm:thqg-VI-sub-subleading-soft` | `theorem` | 1368 | Sub-subleading soft graviton theorem |
| `thm:thqg-VI-general-soft` | `theorem` | 1477 | General arity-$r$ soft graviton theorem |
| `cor:thqg-VI-soft-recursion` | `corollary` | 1526 | Soft factor recursion |
| `thm:thqg-VI-quintic-forced` | `theorem` | 1552 | The Virasoro quintic shadow is forced |
| `comp:thqg-VI-virasoro-quintic-soft` | `computation` | 1677 | Quintic soft factor for Virasoro |
| `prop:thqg-VI-inductive-nontermination` | `proposition` | 1712 | Inductive non-termination for class $\mathbf{M}$ |
| `prop:thqg-VI-polynomial-growth` | `proposition` | 1792 | Polynomial growth of soft factors |
| `cor:thqg-VI-soft-convergence` | `corollary` | 1841 | Convergence of the soft expansion |
| `prop:thqg-VI-celestial-structure` | `proposition` | 1908 | Structure of the celestial soft algebra |
| `thm:thqg-VI-soft-ope` | `theorem` | 1988 | Soft graviton OPE |
| `prop:thqg-VI-asymptotic-symmetry` | `proposition` | 2059 | Asymptotic symmetry algebra from the shadow tower |

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
| `thm:thqg-g6-soft-graviton` | `theorem` | 183 | \textbf{G6}: Soft graviton theorems |
| `thm:thqg-g7-bootstrap` | `theorem` | 206 | \textbf{G7}: Modular bootstrap |
| `thm:thqg-g8-reconstruction` | `theorem` | 223 | \textbf{G8}: Holographic reconstruction |
| `thm:thqg-g9-critical-string` | `theorem` | 240 | \textbf{G9}: Critical string dichotomy |
| `thm:thqg-g10-fredholm` | `theorem` | 258 | \textbf{G10}: Fredholm partition functions |
| `thm:thqg-g14-error-correction` | `theorem` | 307 | \textbf{G14}: Holographic code structure |
| `thm:thqg-g15-page` | `theorem` | 320 | \textbf{G15}: Algebraic Page constraint |
| `thm:thqg-dependency` | `theorem` | 344 | Dependency theorem |

#### `chapters/connections/ym_boundary_theory.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ym-bar-bridge` | `theorem` | 58 | Bridge theorem: boundary chiral algebra $\to$ visible center via bar-cobar |
| `thm:twisted-ym-boundary-brst` | `theorem` | 220 | Boundary BRST recovery for twisted Yang--Mills data |
| `thm:twisted-ym-tangent-center` | `theorem` | 245 | Tangent-to-center principle |
| `cor:twisted-ym-center-rigidity` | `corollary` | 264 | Center-vanishing rigidity criterion |
| `cor:twisted-ym-one-parameter` | `corollary` | 274 | One-parameter criterion |
| `thm:twisted-ym-tangent-factors-through-center` | `theorem` | 296 | The tangent functor factors through the dual center |
| `cor:twisted-ym-interface-invariance` | `corollary` | 322 | Interface invariance of tangent data |
| `cor:twisted-ym-center-comparison` | `corollary` | 340 | Comparison without full boundary equivalence |
| `thm:twisted-ym-dual-unobstructedness` | `theorem` | 382 | Dual unobstructedness criterion |
| `thm:twisted-ym-central-formality` | `theorem` | 405 | Central formality theorem |
| `lem:twisted-ym-center-tensor` | `lemma` | 462 | Center of a chiral tensor product |
| `thm:twisted-ym-binary-mixed-couplings` | `theorem` | 500 | Binary mixed-coupling theorem |
| `cor:twisted-ym-multibody-couplings` | `corollary` | 565 | Multi-body coupling expansion |
| `cor:twisted-ym-mixed-rigidity` | `corollary` | 599 | Mixed rigidity criterion |

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
| `prop:scalar-mc-skeleton` | `proposition` | 172 | The scalar shadow is an abelian MC element |
| `thm:spectral-cumulant-hierarchy` | `theorem` | 231 | Spectral cumulant hierarchy |
| `thm:first-obstruction-traceless-quadratic` | `theorem` | 313 | First obstruction is traceless and quadratic |
| `cor:filtered-lift-vanishing` | `corollary` | 386 | Vanishing criterion for filtered lifts |
| `lem:positive-weight-contraction` | `lemma` | 454 | Positive-weight contraction |
| `thm:vir-positive-weight-acyclic` | `theorem` | 471 | Positive-weight Virasoro sectors are acyclic |
| `cor:vir-localization-reduced-spectral` | `corollary` | 490 | Localization to reduced spectral sectors |
| `prop:odd-sheet-rigidity` | `proposition` | 518 | Odd-sheet rigidity for one-line reductions |
| `cor:mu2-centered-at-13` | `corollary` | 559 | The genus-\(2\) one-line coefficient is centered at \texorpdfstring{$13$}{13} |
| `lem:universal-branch-moments` | `lemma` | 622 | Universal branch moments |
| `thm:hodge-depth-formula` | `theorem` | 684 | Depth formula |
| `lem:separating-hodge-splitting` | `lemma` | 717 | Separating Hodge splitting |
| `lem:nonseparating-hodge-extension` | `lemma` | 759 | Nonseparating Hodge extension |
| `thm:genus-two-transparency` | `theorem` | 798 | Genus-\(2\) transparency on a one-line branch quotient |
| `cor:vir-genus-two-vanishing` | `corollary` | 842 | Virasoro genus-\(2\) coefficient vanishes in the one-line quotient |
| `cor:first-primitive-genus-three` | `corollary` | 854 | The first primitive traceless coefficient begins in genus \texorpdfstring{$3$}{3} |
| `lem:genus-three-rose-unique` | `lemma` | 872 | Uniqueness of the primitive rose in genus \texorpdfstring{$3$}{3} |
| `thm:pure-branch-primitive-coefficient` | `theorem` | 902 | Pure-branch primitive coefficient on a rank-two sheet |
| `thm:first-primitive-top-hodge-layer` | `theorem` | 997 | First primitive top-Hodge layer |
| `cor:genus-three-primitive-top-hodge` | `corollary` | 1034 | The genus-\(3\) primitive coefficient |
| `cor:shared-sheet-universal-coefficients` | `corollary` | 1106 | Universal coefficients on the shared sheet |

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
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1324` | `proposition` | 1324 | The \(L_1\)--\(L_2\) package on the one-channel squarefree locus |

#### `appendices/coderived_models.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 240 | Adequacy |
| `thm:stratified-conservative-restriction` | `theorem` | 572 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 648 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 698 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 725 | Factorization co-contra correspondence |
| `thm:off-koszul-ran-inversion` | `theorem` | 817 | Off-Koszul bar-cobar inversion on Ran |

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

#### `appendices/existence_criteria.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:classification-table` | `proposition` | 433 | Classification table \cite{FBZ04, BD04} |

#### `appendices/homotopy_transfer.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:htt-rectification` | `proposition` | 15 | Homotopy transfer as rectification mechanism |
| `lem:sdr-existence` | `lemma` | 146 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 455 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 521 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 615 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 729 | Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0} |

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

#### `appendices/nonlinear_modular_shadows.tex` (76)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:nms-mc-principle` | `theorem` | 179 | Algebra structure $=$ Maurer--Cartan element |
| `prop:shadow-linfty-obstruction` | `proposition` | 212 | Shadow tower as $L_\infty$ formality obstruction tower |
| `prop:nms-five-component` | `proposition` | 307 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | 367 | Shadow tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | 407 | All families from universal evaluation |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | 500 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | 554 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | 600 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | 609 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | 630 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | 645 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | 744 | Quartic shadow master equations |
| `thm:nms-separating-boundary-recursion` | `theorem` | 783 | Separating boundary recursion through quartic order |
| `thm:nms-shadow-cocycle-characterization` | `theorem` | 845 | Finite-order realization of the universal class |
| `prop:nms-quartic-closure-envelope` | `proposition` | 896 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | 926 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | 946 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | 985 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | 1009 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | 1090 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | 1114 | Vanishing of the quartic contact invariant |
| `cor:nms-betagamma-boundary-law` | `corollary` | 1138 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | 1155 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | 1183 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | 1225 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | 1263 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | 1291 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | 1363 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | 1418 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `prop:nms-w3-visible-resonance-factor` | `proposition` | 1457 | Visible quartic resonance factor for \texorpdfstring{$\mathcal W_3$}{W3} |
| `thm:nms-w3-full-quartic-gram` | `theorem` | 1480 | Full $\mathcal W_3$ quartic Gram determinant |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | 1551 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | 1569 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | 1585 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | 1694 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | 1746 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 1770 | Clutching law for the modular quartic resonance class |
| `thm:nms-first-nonlinear-shadow-theta` | `theorem` | 1844 | The first nonlinear shadow of \texorpdfstring{$\Theta_{\cA}$}{ThetaA} |
| `cor:nms-family-boundary-behavior` | `corollary` | 1857 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | 1926 | Functoriality and duality through quartic order |
| `conj:nms-full-resonance-tower` | `theorem` | 1952 | Full resonance tower |
| `thm:nms-all-arity-master-equation` | `theorem` | 2058 | All-arity master equation |
| `cor:nms-quintic-master-equation` | `corollary` | 2081 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | 2101 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | 2120 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | 2139 | Finite termination for primitive archetypes |
| `thm:nms-all-arity-separating-boundary` | `theorem` | 2164 | All-arity separating boundary recursion |
| `cor:nms-quintic-separating-boundary` | `corollary` | 2180 | Quintic separating boundary recursion |
| `prop:nms-genus-loop-properties` | `proposition` | 2226 | Basic properties of the genus loop operator |
| `thm:nms-nonseparating-clutching-law` | `theorem` | 2243 | Non-separating clutching law for the shadow tower |
| `cor:nms-genus-one-hessian-correction` | `corollary` | 2267 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | 2291 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2366 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2400 | Ambient complementarity and nonlinear modular shadows |
| `conj:nms-all-arity-resonance-boundary` | `theorem` | 2569 | All-arity boundary law for the resonance tower |
| `thm:nms-bipartite-complementarity` | `theorem` | 2770 | Bipartite complementarity principle |
| `thm:nms-bipartite-vanishing` | `theorem` | 2875 | Bipartite vanishing theorem |
| `prop:nms-basis-independence-specialization-restated` | `proposition` | 3162 | Basis independence and specialization |
| `thm:nms-clutching-law-modular-resonance-restated` | `theorem` | 3190 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behaviour` | `corollary` | 3220 | Family-by-family boundary behaviour |
| `thm:nms-genus-loop-model-families-restated` | `theorem` | 3346 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat-restated` | `theorem` | 3414 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary-restated` | `theorem` | 3446 | Ambient complementarity and nonlinear modular shadows |
| `thm:reduced-weight-finiteness` | `theorem` | 3649 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | 3737 | Window locality |
| `cor:exact-stabilization` | `corollary` | 3759 | Exact stabilization |
| `lem:nms-euler-inversion` | `lemma` | 3935 | Euler inversion |
| `prop:kac-shadow-singularity` | `proposition` | 4022 | Kac-shadow singularity principle |
| `thm:ds-shadow-depth-increase` | `theorem` | 4133 | DS shadow depth increase |
| `thm:shadow-subalgebra-autonomy` | `theorem` | 4337 | Shadow subalgebra autonomy |
| `cor:w-line-alternating-vanishing` | `corollary` | 4413 | $W$-line alternating vanishing |
| `thm:nms-shadow-mc-potential` | `theorem` | 4442 | Shadow tower as cyclic $L_\infty$ MC potential |
| `prop:nms-shadow-convergence` | `proposition` | 4506 | Shadow potential convergence |
| `thm:nms-mc-moduli-curve-structure` | `theorem` | 4615 | MC moduli curve structure |
| `thm:nms-hadamard-mc-potential` | `theorem` | 4678 | Hadamard factorization of the MC potential |
| `cor:nms-mc-solution-counting` | `corollary` | 4725 | MC solution counting |

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
| `prop:LV-conversion-complete` | `proposition` | 1085 | Loday--Vallette conversion |

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
| `thm:canonical-arity-detection` | `theorem` | 464 | Generator-degree detection of canonical arity |
| `thm:full-raw-coefficient-packet` | `theorem` | 612 | Exact Bell recursion for the full singular packet |
| `thm:miura-product-formula` | `theorem` | 770 | Subregular Miura product formula |
| `thm:subregular-appell-formula` | `theorem` | 807 | Subregular Appell formula |
| `thm:bp-strict` | `theorem` | 879 | Bershadsky--Polyakov is strict in canonical normal form |
| `thm:w4-cubic` | `theorem` | 926 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} has canonical arity $3$ |
| `thm:unbounded-canonical-arity` | `theorem` | 1057 | Unbounded canonical arity in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | 1111 | Triangular primary-renormalization theorem |

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
