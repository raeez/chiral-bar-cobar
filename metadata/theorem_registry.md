# Theorem Registry

Auto-generated on 2026-04-08 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2711 |
| Total tagged claims | 3463 |
| Active files in `main.tex` | 88 |
| Total `.tex` files scanned | 116 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2711 |
| `ProvedElsewhere` | 447 |
| `Conjectured` | 223 |
| `Conditional` | 33 |
| `Heuristic` | 46 |
| `Open` | 3 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 1181 |
| `proposition` | 897 |
| `corollary` | 387 |
| `lemma` | 121 |
| `computation` | 108 |
| `remark` | 12 |
| `calculation` | 3 |
| `maintheorem` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 15 |
| Part I: Theory | 1031 |
| Part II: Examples | 647 |
| Part III: Connections | 805 |
| Appendices | 213 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus_modular_koszul.tex` | 234 |
| `chapters/connections/arithmetic_shadows.tex` | 127 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 113 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 96 |
| `appendices/ordered_associative_chiral_kd.tex` | 89 |
| `chapters/theory/ordered_associative_chiral_kd.tex` | 89 |
| `chapters/theory/higher_genus_complementarity.tex` | 79 |
| `chapters/examples/w_algebras.tex` | 70 |
| `appendices/nonlinear_modular_shadows.tex` | 69 |
| `chapters/examples/free_fields.tex` | 67 |
| `chapters/theory/higher_genus_foundations.tex` | 63 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 54 |
| `chapters/examples/kac_moody.tex` | 54 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 52 |
| `chapters/theory/chiral_modules.tex` | 49 |
| `chapters/examples/yangians_computations.tex` | 48 |
| `chapters/connections/thqg_gravitational_s_duality.tex` | 46 |
| `chapters/examples/yangians_foundations.tex` | 44 |
| `chapters/examples/lattice_foundations.tex` | 43 |
| `chapters/theory/chiral_koszul_pairs.tex` | 40 |

## Complete Proved Registry

### Frame (15)

#### `chapters/frame/heisenberg_frame.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 495 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 844 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 933 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1135 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1358 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1380 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1528 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1711 | Quantum complementarity for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2345 | $\mathfrak{sl}_2$ bar complex as Swiss-cheese coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2417 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2466 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2549 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 2587 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 2855 | CS $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | 3583 | The Heisenberg center |

### Part I: Theory (1031)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 1021 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 1539 | Geometric realization |
| `prop:orthogonal` | `proposition` | 1720 | Orthogonality |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (113)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:curvature-central` | `theorem` | 232 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 337 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 485 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 554 | Conilpotency ensures convergence |
| `comp:virasoro-spectral-r-matrix` | `computation` | 727 | Virasoro spectral R-matrix on primary states |
| `lem:arity-cutoff` | `lemma` | 901 | Arity cutoff: finite MC equation at each stage |
| `thm:completed-bar-cobar-strong` | `theorem` | 920 | MC element lifts to the completed convolution algebra |
| `prop:standard-strong-filtration` | `proposition` | 1067 | Strong filtration for the standard landscape |
| `prop:mc4-reduction-principle` | `proposition` | 1150 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 1215 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 1252 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 1290 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 1339 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 1390 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 1453 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 1517 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 1553 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 1629 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 1726 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 1742 | Factorization-envelope criterion for principal stages |
| `cor:completion-closure-equivalence` | `corollary` | 1778 | Homotopy-categorical equivalence on the completion closure |
| `thm:coefficient-stability-criterion` | `theorem` | 1832 | Coefficient-stability criterion |
| `thm:completed-twisting-representability` | `theorem` | 1867 | Completed twisting representability |
| `thm:mc-twisting-closure` | `theorem` | 1890 | MC-twisting closure of the completion closure |
| `thm:uniform-pbw-bridge` | `theorem` | 1915 | Uniform PBW bridge from MC1 to MC4 |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 2021 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 2067 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 2102 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 2122 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 2140 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 2159 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 2201 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 2241 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 2282 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 2349 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 2391 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 2437 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 2499 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 2540 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 2612 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 2699 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 2725 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 2750 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 2804 | Stage-\texorpdfstring{$4$}{4} reduction to one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 2832 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 2869 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 2900 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 2942 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 2969 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 2999 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 3042 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 3077 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 3107 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 3124 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 3175 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 3236 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
| `cor:winfty-dual-candidate-construction` | `corollary` | 3275 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 3322 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} reduction on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 3361 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 3453 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 3484 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 3592 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 3640 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 3686 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 3713 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 3855 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 3892 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 3956 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 4011 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 4053 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 4147 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 4172 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 4211 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 4231 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 4269 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 4286 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 4309 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 4331 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 4347 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 4357 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 4373 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 4385 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 4398 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 4416 | Stage-\texorpdfstring{$5$}{5} mixed transport reduction to one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 4439 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 4470 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 4677 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 4695 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 4732 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 4769 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-network-collapse` | `corollary` | 5065 | Visible stage-\texorpdfstring{$5$}{5} local network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 5113 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 5337 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 5622 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 5964 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 6000 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 6061 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 6073 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 6181 | Bar complex as algebra over the modular operad |
| `cor:genus-expansion-converges` | `corollary` | 6472 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 6532 | Functoriality of bar construction |
| `thm:reconstruction-vs-duality` | `theorem` | 6641 | Reconstruction versus duality |
| `thm:recognition-koszul-pairs` | `theorem` | 6703 | Recognition theorem for finite chiral Koszul pairs |
| `thm:mixed-boundary-sseq` | `theorem` | 6758 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | 6782 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | 6830 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | 6859 | Universality |
| `prop:sugawara-contraction` | `proposition` | 6867 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | 6932 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | 6948 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | 6994 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | 7043 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | 7087 | Diagonal GKO transgression |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (52)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 354 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 576 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 939 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 1056 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1129 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1173 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1241 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1307 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1447 | Positselski equivalence for the chiral bar coalgebra |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1504 | Flat finite-type reduction on the completed-dual side |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1610 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 1779 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 1795 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 1849 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 1872 | Genus-graded convergence |
| `prop:counit-qi` | `proposition` | 1993 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 2005 | Functoriality of bar-cobar inversion |
| `lem:complete-filtered-comparison` | `lemma` | 2089 | Complete filtered comparison lemma |
| `cor:completed-derived-equivalence` | `corollary` | 2190 | Completed derived equivalence |
| `thm:barr-beck-lurie-koszulness` | `theorem` | 2302 | Barr--Beck--Lurie characterization of chiral Koszulness |
| `thm:fh-concentration-koszulness` | `theorem` | 2387 | Factorization homology concentration |
| `thm:fm-boundary-acyclicity` | `theorem` | 2447 | FM boundary acyclicity |
| `prop:lagrangian-perfectness` | `proposition` | 2638 | Perfectness for the standard landscape |
| `cor:lagrangian-unconditional` | `corollary` | 2774 | Unconditional Lagrangian criterion for the standard landscape |
| `prop:bar-fh` | `proposition` | 3155 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 3233 | Cobar as factorization cohomology |
| `prop:subexponential-growth-automatic` | `proposition` | 3783 | Sub-exponential growth is automatic |
| `thm:ks-centrality` | `theorem` | 4002 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | 4045 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | 4096 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | 4131 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | 4177 | Quadratic frontier |
| `prop:eta-hessian-transfer` | `proposition` | 4271 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | 4307 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | 4351 | Admissible cyclic rigidity |
| `cor:ds-not-first-frontier` | `corollary` | 4386 | Drinfeld--Sokolov reductions remain one-channel in the semisimple admissible sector |
| `thm:classification-scalar-genera` | `theorem` | 4431 | Classification of scalar genera |
| `thm:platonic-hierarchy-log` | `theorem` | 4502 | Five-step hierarchy of the categorical logarithm |
| `prop:cech-two-element-strict` | `proposition` | 5019 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | 5347 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | 5407 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | 5439 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | 5461 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | 5559 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | 5607 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | 5627 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | 5672 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | 5703 | Repeated roots encode extension data |
| `thm:common-core-exact-sequences-inv` | `theorem` | 5735 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | 5763 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | 5830 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | 5852 | Explicit coprime-locus projectors |

#### `chapters/theory/bar_construction.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 271 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 647 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 737 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 919 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 985 | Functoriality |
| `thm:stokes-config` | `theorem` | 1001 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 1096 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 1138 | Arnold relations |
| `comp:deg0` | `computation` | 1181 | Degree 0 |
| `comp:deg1-general` | `computation` | 1199 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1321 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1360 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1366 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1398 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1421 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1488 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1539 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1556 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1643 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1669 | Residue properties |
| `thm:three-bar-complexes` | `theorem` | 1741 | Three bar complexes and their inclusions |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1935 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 2010 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 2082 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 2192 | Bar complex is chiral |

#### `chapters/theory/chiral_center_theorem.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:partial-comp-assoc` | `lemma` | 189 | Associativity of partial compositions |
| `prop:pre-lie-chiral` | `proposition` | 494 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | 522 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | 543 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | 1225 | Chiral Deligne--Tamarkin |
| `prop:derived-center-explicit` | `proposition` | 1760 | Explicit derived center: Heisenberg, affine $\widehat{\mathfrak{sl}}_2$, Virasoro |
| `prop:heisenberg-bv-structure` | `proposition` | 1898 | BV algebra structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)$ |
| `prop:annulus-trace-standard` | `proposition` | 1997 | Annulus trace for standard families |

#### `chapters/theory/chiral_hochschild_koszul.tex` (39)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 189 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 340 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 378 | Hochschild spectral sequence |
| `lem:hochschild-shift-computation` | `lemma` | 495 | Hochschild duality shift |
| `thm:main-koszul-hoch` | `theorem` | 556 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `thm:hochschild-polynomial-growth` | `theorem` | 667 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 764 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `prop:e2-formality-hochschild` | `proposition` | 805 | $\Etwo$-formality of chiral Hochschild cohomology |
| `thm:convolution-formality-one-channel` | `theorem` | 885 | Scalar universal class implies convolution formality along its distinguished orbit |
| `thm:bifunctor-obstruction-decomposition` | `theorem` | 1079 | Bifunctor obstruction decomposition |
| `comp:boson-hochschild` | `computation` | 1295 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 1325 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 1430 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 1524 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 1622 | Kac--Moody cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | 1828 | Genus truncation |
| `prop:hochschild-shadow-projection` | `proposition` | 1901 | Hochschild as arity-$2$ shadow projection |
| `thm:mc2-1-km` | `theorem` | 1930 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 2047 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 2294 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 2380 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 2499 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | 2681 | Strictification principle for modular deformation theory |
| `prop:d-mod-squared-zero` | `proposition` | 2817 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2952 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 3126 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 3316 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 3442 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 3692 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 3848 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 3987 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 4072 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 4119 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 4417 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 4548 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 4595 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 4793 | $bc$/$\beta\gamma$ Koszul duality |
| `prop:hochschild-cech-ss` | `proposition` | 4995 | Hochschild--\v{C}ech spectral sequence |
| `prop:envelope-shadow` | `proposition` | 5433 | Factorization envelope shadow functor |

#### `chapters/theory/chiral_koszul_pairs.tex` (40)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 240 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 267 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 287 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 315 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 390 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 655 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 733 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 788 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 832 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 1012 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1124 | Formality implies chiral Koszulness |
| `thm:ainfty-koszul-characterization` | `theorem` | 1158 | Converse: formality implies chiral Koszulness |
| `conj:ext-diagonal-vanishing` | `theorem` | 1228 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1266 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1292 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1316 | Kac--Shapovalov criterion for simple quotients |
| `prop:li-bar-poisson-differential` | `proposition` | 1525 | Poisson differential on the Li--bar $E_1$ page |
| `thm:associated-variety-koszulness` | `theorem` | 1596 | Associated-variety criterion for Koszulness |
| `prop:large-orbit-obstruction` | `proposition` | 1698 | Nilradical obstruction at degenerate admissible levels |
| `thm:koszul-equivalences-meta` | `theorem` | 1832 | Equivalences of chiral Koszulness |
| `prop:d-module-purity-km` | `proposition` | 2227 | $\cD$-module purity for affine Kac--Moody algebras |
| `prop:koszulness-formality-equivalence` | `proposition` | 2375 | Koszulness as formality of the convolution algebra |
| `thm:koszulness-from-sklyanin` | `theorem` | 2479 | Koszulness from Sklyanin--Poisson rigidity; {} for affine KM |
| `prop:cumulant-window-inversion` | `proposition` | 2728 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 2784 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 2961 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 3021 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 3175 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 3269 | Bar computes Koszul dual, complete statement |
| `lem:completion-convergence` | `lemma` | 3357 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 3406 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 3965 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 4183 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:e1-module-koszul-duality` | `theorem` | 4270 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `prop:koszul-character-identity` | `proposition` | 4399 | Koszul character identity |
| `thm:structure-exchange` | `theorem` | 4441 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 4483 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 4529 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 4567 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 4776 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 179 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 284 | Module bar-comodule comparison on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `thm:monoidal-module-koszul` | `theorem` | 343 | Lax monoidal structure of the module bar functor |
| `prop:ext-tor-exchange` | `proposition` | 462 | Derived Ext exchange on the quadratic \texorpdfstring{$\Eone$}{E1} lane |
| `prop:conformal-blocks-bar` | `proposition` | 541 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 645 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 746 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 804 | KZB connection from the bar complex |
| `prop:tilting-bar` | `proposition` | 1649 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1712 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1912 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1972 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 2006 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:logarithmic-bar` | `proposition` | 2244 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2338 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2451 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2486 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2525 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2542 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2582 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2604 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2754 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2866 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2980 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3059 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3213 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3244 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3287 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3377 | Vacuum Verma under the module bar functor on the finite-type \texorpdfstring{$\Eone$}{E1} lane |
| `prop:shapovalov-koszul` | `proposition` | 3481 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3540 | Non-vacuum Verma modules under the module bar functor on the finite-type \texorpdfstring{$\Eone$}{E1} lane |
| `cor:singular-vector-symmetry` | `corollary` | 3623 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3700 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3755 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3848 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3902 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3968` | `calculation` | 3968 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3995` | `calculation` | 3995 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:4026` | `calculation` | 4026 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4144 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4269 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4319 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4443 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4485 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar at dual level via DS and Verdier intertwining |
| `thm:module-genus-tower` | `theorem` | 4556 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4598 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4740 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4889 | Fusion product compatibility on the module bar surface |
| `prop:heisenberg-fusion-splitting` | `proposition` | 5010 | Heisenberg fusion splitting |

#### `chapters/theory/cobar_construction.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 289 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 350 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 383 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 465 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 541 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 662 | Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 932 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 1092 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1310 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1441 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1493 | Explicit cobar-bar augmentation |
| `prop:cobar-modular-shadow` | `proposition` | 1765 | Cobar as modular shadow carrier |
| `thm:cobar-cech` | `theorem` | 1777 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1825 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1846 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1936 | Topology |
| `thm:poincare-verdier` | `theorem` | 1995 | Bar-cobar Verdier pairing |
| `thm:curved-mc-cobar` | `theorem` | 2095 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 2120 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 2166 | Level-shifting via Verdier duality |
| `thm:central-charge-cocycle` | `theorem` | 2355 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2451 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2592 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2617 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2714 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2767 | Recognition principle |
| `lem:deformation-space` | `lemma` | 3161 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 3203 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 3251 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3330 | Curved differential formula |

#### `chapters/theory/coderived_models.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 243 | Adequacy |
| `thm:stratified-conservative-restriction` | `theorem` | 578 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 654 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 704 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 731 | Factorization co-contra correspondence |
| `thm:off-koszul-ran-inversion` | `theorem` | 825 | Off-Koszul bar-cobar inversion on Ran |

#### `chapters/theory/computational_methods.tex` (17)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:comp-algebraic-shadow` | `theorem` | 101 | Riccati algebraicity |
| `thm:comp-denom-pattern` | `theorem` | 177 | Denominator theorem |
| `prop:comp-shadow-connection-properties` | `proposition` | 227 | Properties of the shadow connection |
| `thm:comp-shadow-asymptotics` | `theorem` | 354 | Shadow asymptotics |
| `prop:comp-borel-summability` | `proposition` | 454 | Borel summability |
| `prop:comp-mc-recursion` | `proposition` | 504 | MC recursion |
| `thm:comp-alg-rec-equivalence` | `theorem` | 533 | Algebraic--recursive equivalence |
| `thm:comp-ds-consistency` | `theorem` | 600 | DS transfer consistency |
| `prop:comp-ce-bar` | `proposition` | 681 | CE reduction |
| `thm:comp-zhu-c-dependence` | `theorem` | 704 | $c$-dependence for simple quotients |
| `thm:comp-three-way-bar` | `theorem` | 784 | Three-way agreement for bar cohomology |
| `prop:comp-explicit-theta-sl2` | `proposition` | 809 | Explicit $\Theta$ for $\AffKM{sl}_2$ |
| `thm:comp-e8-three-way` | `theorem` | 938 | $E_8$ genus-$2$ agreement |
| `prop:comp-n2-kappa` | `proposition` | 1090 | Modular characteristic |
| `prop:comp-n2-spectral-flow` | `proposition` | 1153 | Spectral flow invariance |
| `thm:comp-genus2-cross` | `theorem` | 1193 | Cross-consistency at genus~$2$ |
| `thm:s3-virasoro-c-independent` | `theorem` | 1431 | $c$-independence of $S_3$ for Virasoro |

#### `chapters/theory/configuration_spaces.tex` (37)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 360 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 480 | Normal crossings |
| `thm:closure-relations` | `theorem` | 575 | Closure relations |
| `thm:log-complex` | `theorem` | 692 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 731 | Arnold relations |
| `prop:twisting-morphism-propagator` | `proposition` | 812 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 879 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 946 | Residue operations |
| `prop:residue-local` | `proposition` | 1001 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 1086 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1328 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1395 | Conformal blocks from punctured bar complex |
| `thm:bordered-fm-properties` | `theorem` | 1813 | Properties of the bordered FM compactification |
| `prop:four-type-boundary` | `proposition` | 1912 | Four-type boundary decomposition |
| `thm:oc-convolution-dg-lie` | `theorem` | 2307 | dg~Lie structure on the open-closed convolution algebra |
| `thm:modular-mc-clutching` | `theorem` | 2555 | Modular MC equation with clutching |
| `cor:recovery-bar-intrinsic` | `corollary` | 2901 | Recovery of the bar-intrinsic MC element |
| `prop:eta` | `proposition` | 3077 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `lem:orientation-compatibility` | `lemma` | 3484 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 3545 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 3586 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 3613 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 3635 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 3675 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 3699 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 3734 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 3756 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 3790 | Residue evaluation complexity |
| `thm:arnold-jacobi` | `theorem` | 3907 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 3960 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 4006 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 4038 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 4083 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 4313 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 4383 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 4520 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:4730` | `computation` | 4730 | Explicit examples |

#### `chapters/theory/derived_langlands.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:langlands-bar-bridge` | `theorem` | 45 | Critical bar-to-oper bridge |
| `thm:oper-bar-h0-dl` | `theorem` | 269 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 304 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 328 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 365 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 446 | Differential analysis at arity 3 |
| `prop:d4-nonvanishing` | `proposition` | 526 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 585 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 598 | Full oper differential-form identification |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 937 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/e1_modular_koszul.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | 122 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | 141 | — |
| `rem:e1-mc-element` | `theorem` | 236 | $E_1$ Maurer--Cartan element |
| `prop:e1-shadow-r-matrix` | `proposition` | 269 | — |
| `thm:e1-mc-finite-arity` | `theorem` | 359 | $E_1$ MC equation at finite arity |
| `thm:e1-coinvariant-shadow` | `theorem` | 429 | Coinvariant projection: $E_1$ shadows to $E_\infty$ shadows |
| `thm:e1-theorem-A-modular` | `theorem` | 776 | Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction |
| `thm:e1-theorem-B-modular` | `theorem` | 833 | Theorem~$\mathrm{B}^{E_1}$ at all genera: ordered bar--cobar inversion |
| `thm:e1-theorem-C-modular` | `theorem` | 859 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
| `thm:e1-theorem-D-modular` | `theorem` | 898 | Theorem~$\mathrm{D}^{E_1}$ at all genera: formal ordered arity-$2$ shadow series |
| `thm:e1-theorem-H-modular` | `theorem` | 969 | Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered Hochschild at genus~$g$ |
| `lem:bare-graph-no-thooft` | `lemma` | 1162 | Bare graphs do not determine a 't~Hooft expansion |
| `thm:cyclicity-ribbon` | `theorem` | 1183 | Cyclicity is the ribbon-enabling datum |
| `cor:operads-too-small` | `corollary` | 1225 | Operads are too small for traces |
| `thm:exact-n-chi-weighting` | `theorem` | 1247 | Exact $N^{\chi}$ weighting from traced open color |

#### `chapters/theory/en_koszul_duality.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:en-chiral-bridge` | `theorem` | 48 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
| `prop:en-formality-mc-truncation` | `proposition` | 121 | Formality hierarchy as MC obstruction truncation |
| `prop:linking-sphere-residue` | `proposition` | 397 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 472 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 632 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 690 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:kappa-universality-en` | `proposition` | 818 | Kappa universality across $n$ |
| `prop:shadow-stabilization` | `proposition` | 844 | Shadow stabilization threshold |
| `prop:shadow-gc2-bridge` | `proposition` | 1035 | Shadow obstruction tower to $\mathrm{GC}_2$ bridge |
| `thm:bar-swiss-cheese` | `theorem` | 1224 | Bar complex as Swiss-cheese coalgebra |
| `prop:sc-koszul-dual-three-sectors` | `proposition` | 1458 | Koszul dual cooperad of \texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}: three sectors |
| `prop:operadic-center-existence` | `proposition` | 1572 | Existence of the operadic center |
| `thm:operadic-center-hochschild` | `theorem` | 1625 | The operadic center of $\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex |
| `thm:center-geometric-inevitability` | `theorem` | 1947 | Geometric inevitability of the chiral center |
| `prop:braces-from-center` | `proposition` | 2140 | Brace operations from the operadic center |
| `thm:operadic-brace-comparison` | `theorem` | 2189 | Comparison theorem: operadic center $=$ brace center |
| `thm:center-terminality` | `theorem` | 2265 | Terminality of the center |
| `cor:center-functor` | `corollary` | 2353 | The center functor |
| `thm:en-shadow-tower` | `theorem` | 2606 | $\En$ shadow obstruction tower: universality of $\kappa$ and formality collapse |
| `prop:e3-bar-structure` | `proposition` | 2771 | $\Etwo$ structure on $B(\cA)$ and the $\mathsf{E}_3$ obstruction |

#### `chapters/theory/existence_criteria.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:classification-table` | `proposition` | 451 | Classification table \cite{FBZ04, BD04} |
| `prop:w-algebra-koszul` | `proposition` | 529 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul analysis |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 21 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 178 | Convergence criterion in the filtered/curved regimes |

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

#### `chapters/theory/higher_genus_complementarity.tex` (79)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:involution-splitting` | `lemma` | 171 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 226 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 300 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 398 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 583 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 638 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 723 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 786 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 837 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 982 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 1055 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 1095 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 1149 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1178 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 1366 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 1401 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 1453 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 1566 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 1597 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 1617 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 1722 | Verdier pairing and Lagrangian eigenspaces |
| `prop:ptvv-lagrangian` | `proposition` | 1940 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 2013 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 2114 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 2142 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 2179 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 2222 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 2258 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 2289 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 2540 | Fermion-boson Koszul duality |
| `prop:complementarity-landscape` | `proposition` | 2725 | Complementarity landscape |
| `thm:BD-genus-zero` | `theorem` | 2940 | BD 3.4.12: genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 2990 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 3003 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 3045 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 3104 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 3144 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 3172 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 3194 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 3238 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 3427 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 3475 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 3563 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 3590 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 3618 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 3654 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 3679 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 3740 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 3786 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 3825 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 3854 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 3882 | Algebra structure from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 3910 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 3942 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 3991 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 4017 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 4033 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 4138 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 4216 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 4264 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 4353 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | 4528 | Ambient complementarity in tangent form |
| `thm:ambient-complementarity-fmp` | `theorem` | 4571 | Ambient complementarity as shifted symplectic formal moduli problem |
| `thm:shifted-cotangent-normal-form` | `theorem` | 4829 | Shifted cotangent normal form |
| `prop:legendre-duality-potentials` | `proposition` | 4878 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | 4893 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | 4923 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | 4947 | Criterion for fake complementarity |
| `thm:holo-comp-bulk-reconstruction` | `theorem` | 5143 | Protected dual transform |
| `thm:holo-comp-cotangent-realization` | `theorem` | 5193 | Shifted cotangent realization |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | 5220 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | 5306 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | 5350 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | 5427 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | 5510 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | 5579 | First nonlinear holographic anomaly |
| `thm:critical-dimension` | `theorem` | 5685 | Critical dimension |
| `prop:non-critical-liouville` | `proposition` | 5854 | Non-critical complementarity and the Liouville sector |
| `cor:complementarity-discriminant-cancellation` | `corollary` | 5899 | Arity-$4$ discriminant cancellation |

#### `chapters/theory/higher_genus_foundations.tex` (63)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:gauss-manin-uncurving-chain` | `proposition` | 316 | Gauss--Manin uncurving at chain level |
| `prop:genus-g-curvature-package` | `proposition` | 486 | The genus-$g$ curvature package |
| `prop:chain-level-curvature-operator` | `proposition` | 601 | Chain-level curvature operator |
| `prop:genus-g-mc-element` | `proposition` | 727 | Genus-$g$ MC element |
| `thm:bar-ainfty-complete` | `theorem` | 921 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 1021 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 1116 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 1229 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 1336 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 1483 | Verdier duality of operations |
| `thm:bar-curved-ch-infty` | `theorem` | 1645 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
| `thm:convergence-filtered` | `theorem` | 1723 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1941 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1975 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 2009 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 2029 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 2045 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2349 | Bar-cobar isomorphism, retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 2434 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2649 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 3255 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 3458 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 3518 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 3771 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:genus1-d-squared` | `theorem` | 3865 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 3922 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 4190 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 4223 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 4350 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 4453 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 4507 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 4585 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 4702 | \texorpdfstring{$W_3$}{W3} fiberwise obstruction |
| `comp:w3-obs-explicit` | `computation` | 4758 | Explicit genus-$1$ value of the $W_3$ obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 4779 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 4808 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 4894 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4995 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 5291 | Multi-generator edge universality |
| `prop:f2-quartic-dependence` | `proposition` | 5334 | Genus-$2$ quartic dependence |
| `cor:anomaly-ratio` | `corollary` | 5392 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 5408 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 5434 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 5452 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 5475 | Universal genus-$1$ criticality criterion; scalar-lane collapse |
| `cor:tautological-class-map` | `corollary` | 5508 | Tautological class map on the scalar lane; universal genus-$1$ class |
| `prop:bar-tautological-filtration` | `proposition` | 5625 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 5697 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 5727 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 5825 | Scalar obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 5892 | Grothendieck--Riemann--Roch bridge on the proved uniform-weight scalar lane |
| `lem:stable-graph-d-squared` | `lemma` | 6065 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 6127 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 6165 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 6207 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 6296 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 6384 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 6453 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 6487 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 6528 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 6585 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 6613 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 6663 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (234)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:mcg-equivariance-tower` | `proposition` | 151 | MCG-equivariance of the genus tower |
| `thm:genus-graded-koszul` | `theorem` | 239 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 270 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 601 | Free-field examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 643 | Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 685 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 821 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 1086 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 1111 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1308 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1360 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1460 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1510 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1572 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:pbw-propagation` | `theorem` | 1748 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | 1907 | Locality of the collision differential |
| `thm:three-tier-architecture` | `theorem` | 1994 | Three-tier logical architecture of modular Koszul duality |
| `lem:e2-higher-genus` | `lemma` | 2240 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 2393 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 2501 | Modular characteristic |
| `cor:free-energy-ahat-genus` | `corollary` | 2639 | Scalar free energy as $\hat{A}$-genus |
| `thm:spectral-characteristic` | `theorem` | 2716 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 2749 | Universal modular Maurer--Cartan class |
| `prop:curvature-centrality-general` | `proposition` | 2883 | Centrality of higher-genus curvature |
| `thm:mc2-bar-intrinsic` | `theorem` | 2930 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 3327 | Shadow extraction |
| `prop:mc2-functoriality` | `proposition` | 3442 | Functoriality of the bar-intrinsic MC element |
| `thm:bipartite-linfty-tree` | `theorem` | 3545 | Bipartite shadow as $L_\infty$ tree-level structure |
| `thm:explicit-theta` | `theorem` | 3669 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 3888 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 4303 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 4382 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 4495 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 4529 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 4561 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 4766 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 4842 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 4907 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 5042 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 5139 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 5250 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 5387 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 5539 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 5713 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 5863 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 6057 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 6177 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 6276 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 6366 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 6478 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 6550 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 6632 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 6710 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 6787 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 6863 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 6938 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 7004 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 7084 | MC2 completion under explicit hypotheses |
| `thm:mc2-full-resolution` | `theorem` | 7170 | MC2 comparison completion on the proved scalar lane |
| `lem:mk67-from-mc2` | `lemma` | 7223 | Bar-intrinsic MC2 identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 7266 | One-channel line concentration of the minimal MC class |
| `thm:km-strictification` | `theorem` | 7337 | KM strictification of the universal class |
| `prop:w-algebra-scalar-saturation` | `proposition` | 7425 | One-channel line concentration for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 7472 | One-dimensional cyclic line persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 7533 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 7683 | One-channel line concentration for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 7786 | Cyclic rigidity and level-direction concentration |
| `prop:saturation-functorial` | `proposition` | 7977 | Functorial behavior of one-channel line concentration |
| `cor:effective-quadruple` | `corollary` | 8144 | Effective \texorpdfstring{$\Gamma$}{Gamma}-quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 8235 | Cyclic rigidity at generic level |
| `thm:algebraic-family-rigidity` | `theorem` | 8404 | Algebraic-family rigidity |
| `cor:saturation-algebraic-families` | `corollary` | 8516 | Level-direction concentration at all non-critical levels for algebraic families |
| `thm:conformal-bootstrap-rigidity` | `theorem` | 8585 | $L_0$-bootstrap rigidity |
| `cor:one-channel-no-lie` | `corollary` | 8692 | One-channel criterion without Lie symmetry |
| `thm:tautological-line-support` | `theorem` | 8950 | Tautological line support from genus universality |
| `cor:mc2-single-hypothesis` | `corollary` | 9062 | MC2 comparison gauntlet collapses on the proved scalar lane |
| `thm:convolution-dg-lie-structure` | `theorem` | 9249 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 9491 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 9939 | Modular homotopy convolution |
| `prop:modular-homotopy-type-structure` | `proposition` | 10023 | Structure of the modular homotopy type |
| `cor:strictification-comparison` | `corollary` | 10070 | Strictification comparison |
| `cor:vol1-theta-log-fm-twisting-data` | `corollary` | 10446 | $\Theta_\cA$ as universal modular twisting morphism |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | 10700 | First two weights |
| `comp:vol1-low-genus-log-fm-chart` | `computation` | 10775 | Low-genus amplitudes |
| `lem:shadow-bracket-well-defined` | `lemma` | 11386 | Well-definedness of the descended bracket |
| `prop:shadow-algebra-linfty` | `proposition` | 11408 | Transferred $L_\infty$ structure on the shadow algebra |
| `cor:shadow-algebra-functoriality` | `corollary` | 11516 | Functoriality of the shadow algebra |
| `prop:master-equation-from-mc` | `proposition` | 11554 | All-arity master equation from MC |
| `thm:ds-complementarity-tower-main` | `theorem` | 11618 | DS complementarity tower |
| `thm:recursive-existence` | `theorem` | 11734 | Recursive existence and shadow obstruction tower convergence |
| `thm:perturbative-exactness` | `theorem` | 11936 | Perturbative exactness of the modular MC element |
| `thm:universal-modular-deformation` | `theorem` | 12007 | Universal modular deformation functor |
| `thm:modular-propagator-existence` | `theorem` | 12158 | Modular propagator existence |
| `thm:logfm-modular-cocomposition` | `theorem` | 12192 | Log-FM modular cocomposition |
| `thm:stable-graph-pronilpotent-completion` | `theorem` | 12234 | Stable-graph pronilpotent completion |
| `thm:finite-rank-spectral-reduction` | `theorem` | 12285 | Finite-rank spectral reduction |
| `thm:primitive-to-global-reconstruction` | `theorem` | 12350 | Primitive-to-global reconstruction |
| `prop:primitive-shell-equations` | `proposition` | 12500 | Primitive shell equations |
| `prop:branch-master-equation` | `proposition` | 12638 | Branch quantum master equation |
| `cor:metaplectic-square-root` | `corollary` | 12691 | Determinantal half-density |
| `thm:primitive-flat-descent` | `theorem` | 12882 | Descent to the flat modular connection |
| `thm:conformal-block-reconstruction` | `theorem` | 12961 | Scalar free-energy and determinant reconstruction from the primitive kernel on the proved uniform-weight scalar lane |
| `thm:deformation-quantization-ope` | `theorem` | 13056 | Genus expansion from the OPE |
| `thm:ran-coherent-bar-cobar` | `theorem` | 13257 | Ran-coherent bar-cobar equivalence |
| `thm:shadow-channel-decomposition` | `theorem` | 13317 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 13397 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 13449 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 13575 | Direct derivation on the proved scalar lane |
| `lem:graph-sum-truncation` | `lemma` | 13856 | Graph-sum truncation criterion |
| `conj:operadic-complexity-detailed` | `theorem` | 13932 | Operadic complexity |
| `prop:shadow-formality-low-arity` | `proposition` | 14051 | Shadow--formality identification at low arity |
| `thm:shadow-formality-identification` | `theorem` | 14122 | Shadow obstruction tower as formality obstruction tower |
| `prop:shadow-formality-higher-arity` | `proposition` | 14395 | Shadow--formality identification at higher arities |
| `prop:linfty-obstruction-5-6` | `proposition` | 14751 | Explicit $L_\infty$ obstruction classes at arities $5$ and $6$ |
| `cor:operadic-complexity-5-7` | `corollary` | 15002 | Operadic complexity at arities $5$--$7$ |
| `thm:shadow-archetype-classification` | `theorem` | 15240 | Shadow archetype classification |
| `cor:shadow-depth-koszul-invariance` | `corollary` | 15437 | Shadow depth under Koszul duality |
| `thm:riccati-algebraicity` | `theorem` | 15560 | Riccati algebraicity: the shadow generating function is algebraic of degree~$2$ |
| `prop:hankel-extraction` | `proposition` | 15693 | Hankel extraction of the quartic contact invariant |
| `cor:signed-shadow-measure` | `corollary` | 15844 | Universal signed measure |
| `thm:shadow-epstein-zeta` | `theorem` | 15926 | The Epstein zeta function of the shadow metric |
| `prop:pole-purity` | `proposition` | 16262 | Pole purity |
| `prop:intrinsic-quartic` | `proposition` | 16280 | Intrinsic quartic principle |
| `thm:single-line-dichotomy` | `theorem` | 16315 | Single-line dichotomy |
| `prop:shadow-integrable-hierarchy` | `proposition` | 16503 | Shadow CohFT and integrable hierarchies |
| `thm:shadow-tau-kw` | `theorem` | 16565 | Shadow tau function |
| `thm:shadow-connection` | `theorem` | 16678 | Shadow connection |
| `cor:discriminant-atlas` | `corollary` | 16849 | The discriminant atlas |
| `thm:shadow-separation` | `theorem` | 17052 | Shadow separation and completeness |
| `thm:propagator-variance` | `proposition` | 17157 | Propagator variance inequality |
| `prop:t-line-autonomy` | `proposition` | 17267 | T-line autonomy |
| `prop:interchannel-coupling` | `proposition` | 17324 | Inter-channel coupling on sublines |
| `thm:shadow-radius` | `theorem` | 17469 | Shadow growth rate: structure and asymptotics |
| `cor:virasoro-shadow-radius` | `corollary` | 17575 | Virasoro shadow growth rate |
| `prop:critical-cubic-convergence` | `proposition` | 17767 | Critical cubic convergence threshold |
| `prop:virasoro-bottleneck` | `proposition` | 17856 | Virasoro bottleneck |
| `thm:koszul-exchange-regimes` | `theorem` | 18083 | Koszul exchange of shadow regimes |
| `prop:koszul-conductor-wn` | `proposition` | 18160 | Koszul conductor of \texorpdfstring{$\cW_N$}{WN} |
| `prop:propagator-universality` | `proposition` | 18218 | Propagator universality |
| `thm:hamilton-jacobi-shadow` | `theorem` | 18558 | Hamilton--Jacobi master equation on deformation spaces |
| `thm:shadow-finite-determination` | `theorem` | 18763 | Shadow finite determination |
| `cor:w3-reconstruction` | `corollary` | 18850 | $\cW_3$: seven parameters determine the full 2D tower |
| `thm:shadow-tautological-ring` | `theorem` | 19056 | Shadow classes in the tautological ring |
| `cor:analytic-shadow-realization` | `corollary` | 19199 | Analytic shadow realization |
| `thm:shadow-cohft` | `theorem` | 19285 | Shadow cohomological field theory |
| `thm:multi-weight-genus-expansion` | `theorem` | 19456 | Multi-weight genus expansion |
| `comp:w3-genus3-cross` | `computation` | 20042 | $\cW_3$ genus-$3$ cross-channel |
| `comp:w3-genus4-cross` | `computation` | 20101 | $\cW_3$ genus-$4$ cross-channel |
| `comp:w4-full-ope-cross` | `computation` | 20183 | $\cW_4$ full-OPE cross-channel correction |
| `comp:w5-full-ope-cross` | `computation` | 20310 | $\cW_5$ full-OPE cross-channel correction |
| `prop:universal-gravitational-cross-channel` | `proposition` | 20528 | Universal gravitational cross-channel formula for~$\cW_N$ |
| `prop:cross-channel-growth` | `proposition` | 20731 | Cross-channel growth |
| `thm:shadow-tautological-relations` | `theorem` | 20879 | Shadow tautological decomposition and conditional vanishing |
| `thm:mc-tautological-descent` | `theorem` | 20974 | MC descent to tautological relations |
| `prop:self-loop-vanishing` | `proposition` | 21449 | Self-loop parity vanishing |
| `cor:shadow-visibility-genus` | `corollary` | 21485 | Shadow visibility genus |
| `prop:ell2-genus1-mc` | `proposition` | 21604 | Genus-$1$ two-point function from MC |
| `prop:wdvv-from-mc` | `proposition` | 21636 | WDVV from MC at genus~$0$ |
| `prop:mumford-from-mc` | `proposition` | 21669 | Mumford relation from MC at arity~$2$ |
| `thm:planted-forest-structure` | `theorem` | 21701 | Planted-forest structure theorem |
| `thm:cohft-reconstruction` | `theorem` | 21827 | Reconstruction from the MC tangent complex |
| `prop:dressed-propagator-resolution` | `proposition` | 21919 | Dressed propagator coefficient and symmetry |
| `thm:pixton-from-mc-semisimple` | `theorem` | 22058 | Pixton ideal generation on the semisimple locus |
| `prop:non-semisimple-pixton-obstruction` | `proposition` | 22144 | Non-semisimple obstruction to Pixton generation |
| `cor:topological-recursion-mc-shadow` | `corollary` | 22182 | Topological recursion as MC shadow |
| `thm:pixton-mc-genus2` | `theorem` | 22372 | Pixton--MC bridge at genus~$2$ |
| `thm:pixton-mc-genus3` | `theorem` | 22435 | Pixton--MC bridge at genus~$3$ |
| `prop:mumford-from-mc-explicit` | `proposition` | 22510 | Mumford formula from MC |
| `thm:spectral-curve-from-shadow` | `theorem` | 22564 | Spectral curve from shadow metric |
| `thm:tr-shadow-free-energies` | `theorem` | 22598 | TR--shadow free energy identification |
| `thm:genus4-stable-graph-census` | `theorem` | 22637 | Genus-$4$ stable graph census |
| `thm:genus4-free-energy` | `theorem` | 22666 | Genus-$4$ free energy |
| `prop:genus4-spectral-sequence` | `proposition` | 22687 | Genus-$4$ spectral sequence |
| `thm:bar-macmahon` | `theorem` | 22713 | Bar--MacMahon correspondence |
| `prop:conifold-dt-gv` | `proposition` | 22740 | Conifold DT and GV |
| `thm:shadow-dt-curve-counting` | `theorem` | 22754 | Shadow obstruction tower and DT curve counting |
| `prop:tropical-shadow-amplitudes` | `proposition` | 22786 | Tropical shadow amplitudes |
| `prop:tropical-period-theta` | `proposition` | 22808 | Tropical theta function |
| `prop:fp-genus-decay-for-double` | `proposition` | 22867 | Faber--Pandharipande genus decay |
| `thm:shadow-double-convergence` | `theorem` | 22894 | Double convergence of the shadow partition function |
| `prop:shadow-genus-closed-form` | `proposition` | 23009 | Closed form and meromorphic continuation |
| `thm:shadow-borel-genus` | `theorem` | 23088 | Borel transform of the genus series |
| `prop:shadow-stokes-multipliers` | `proposition` | 23149 | Stokes multipliers of the genus expansion |
| `thm:shadow-transseries` | `theorem` | 23177 | Trans-series and instanton sectors |
| `prop:universal-instanton-action` | `proposition` | 23253 | Universal instanton action |
| `prop:c13-full-self-duality` | `proposition` | 23325 | Full tower self-duality at $c = 13$ |
| `prop:shadow-schwarzian` | `proposition` | 23368 | Spectral Schr\"odinger potential |
| `cor:shadow-schrodinger-singularities` | `corollary` | 23405 | Singularity classification |
| `prop:shadow-wkb` | `proposition` | 23477 | WKB expansion |
| `prop:shadow-voros-classical` | `proposition` | 23547 | Classical Voros period |
| `prop:shadow-gue-bridge` | `proposition` | 23590 | Shadow--GUE bridge |
| `prop:shadow-genus-constraints` | `proposition` | 23675 | Shadow genus constraints |
| `prop:winfinity-not-cyclically-admissible` | `proposition` | 23832 | $\mathcal{W}_{1+\infty}$ is not cyclically admissible |
| `prop:finite-jet-rigidity` | `proposition` | 23912 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 23935 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 23971 | Gaussian collapse for abelian input |
| `thm:cubic-gauge-triviality` | `theorem` | 24055 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | 24163 | Independent sum factorization |
| `prop:symn-kappa-linearity` | `proposition` | 24221 | Symmetric orbifold kappa linearity |
| `thm:envelope-koszul` | `theorem` | 24304 | Envelope Koszulness |
| `cor:generic-ht-koszul` | `corollary` | 24382 | Generic-parameter Koszulness for HT boundary algebras |
| `thm:platonic-adjunction` | `theorem` | 24488 | The modular factorization adjunction |
| `cor:envelope-universal-mc` | `corollary` | 24621 | The envelope carries the universal MC class |
| `prop:envelope-construction-strategies` | `proposition` | 24679 | Construction strategies for the modular envelope |
| `conj:shadow-depth-invariant` | `theorem` | 24751 | Shadow depth is a homotopy invariant |
| `conj:tropical-koszulness` | `theorem` | 24795 | Tropical Koszulness |
| `cor:tropical-cohen-macaulay` | `corollary` | 24886 | Tropical Koszulness as the Cohen--Macaulay property |
| `prop:genus0-curve-independence` | `proposition` | 24933 | Genus-$0$ curve-independence |
| `thm:open-stratum-curve-independence` | `theorem` | 24952 | Open-stratum curve-independence at higher genus |
| `prop:saddle-point-mc` | `proposition` | 25267 | MC element as saddle point |
| `prop:bcov-mc-projection` | `proposition` | 25454 | BCOV holomorphic anomaly equation as MC projection |
| `thm:five-from-theta` | `theorem` | 25705 | Five main theorems from the master MC element |
| `thm:obstruction-recursion` | `theorem` | 25930 | Obstruction recursion for the shadow obstruction tower |
| `thm:rectification-meta` | `theorem` | 26027 | Rectification meta-theorem |
| `thm:platonic-recovery` | `theorem` | 26123 | Recovery of the modular Koszul datum from $\Theta_\cA$ |
| `prop:chriss-ginzburg-structure` | `proposition` | 26343 | MC structure principle |
| `prop:planar-forest-coinvariant` | `proposition` | 26721 | Planar forests map to unordered forests |
| `thm:planar-forest-tropicalization` | `theorem` | 26754 | Planar tropicalization |
| `prop:ordered-log-fm-construction` | `proposition` | 26799 | Ordered log-FM construction |
| `cor:e1-ambient-d-squared-zero` | `corollary` | 26877 | $E_1$ ambient $D^2 = 0$ |
| `prop:coefficient-algebras-well-defined` | `proposition` | 26922 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 26955 | Square-zero: convolution level |
| `conj:differential-square-zero` | `theorem` | 26969 | Square-zero: ambient level |
| `thm:inductive-genus-determination` | `theorem` | 27156 | Inductive genus determination |
| `cor:genus-base-cases` | `corollary` | 27224 | Base cases |
| `rem:genus2-shell-activation` | `theorem` | 27261 | Genus-$2$ shell activation as depth diagnostic |
| `comp:vol1-genus-three-stable-graph-census` | `computation` | 27452 | Genus-$3$ stable graph census |
| `prop:2d-convergence` | `proposition` | 27731 | Two-dimensional convergence |
| `thm:analytic-algebraic-comparison` | `theorem` | 27787 | Analytic = algebraic |
| `thm:determinantal-branch-formula` | `theorem` | 27922 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | 27958 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | 27989 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | 28053 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | 28089 | The frontier is cubic |

#### `chapters/theory/hochschild_cohomology.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 104 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 188 | W-algebra Hochschild cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:419` | `computation` | 419 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 475 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 555 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 820 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 850 | Hochschild cup product exchange |
| `thm:derived-center-hochschild` | `theorem` | 1030 | Derived center $=$ Hochschild cochains |
| `thm:morita-invariance-HH` | `theorem` | 1114 | Morita invariance of $\mathrm{HH}^\bullet$ |
| `prop:explicit-morita-transfer` | `proposition` | 1144 | Explicit Morita transfer |
| `thm:circle-fh-hochschild` | `theorem` | 1315 | Factorization homology on $S^1$ $=$ Hochschild chains |
| `prop:monodromy-standard` | `proposition` | 1468 | Monodromy for standard families |

#### `chapters/theory/introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:e1-primacy` | `theorem` | 379 | $\Eone$ primacy |
| `thm:central-charge-complementarity` | `theorem` | 1625 | Central charge complementarity |
| `thm:ahat-universality-intro` | `theorem` | 2027 | $\hat{A}$-genus universality |
| `prop:modular-homotopy-classification` | `proposition` | 3373 | Classification by modular homotopy type |
| `prop:shadow-massey-identification` | `proposition` | 3443 | Genus-$0$ shadow obstructions $=$ $A_\infty$ Massey products |
| `prop:chirAss-self-dual` | `proposition` | 4918 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (29)

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
| `thm:affine-periodicity-critical` | `theorem` | 592 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 687 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 702 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 808 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 920 | Maurer--Cartan correspondence, quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 1011 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1041 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1251 | Positselski equivalence for the chiral bar coalgebra |
| `thm:full-derived-module-equiv` | `theorem` | 1300 | Flat finite-type reduction on the completed-dual side |
| `thm:cs-koszul-km` | `theorem` | 1414 | Affine Kac--Moody Maurer--Cartan and curvature package |
| `thm:linf-mc-flatness` | `theorem` | 1482 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan equation from a transferred \texorpdfstring{$A_\infty$}{A-infinity} model |
| `thm:bv-structure-bar` | `theorem` | 1653 | BV structure on bar complex |
| `thm:ordered-shuffle` | `theorem` | 1819 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | 1861 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | 1891 | Enveloping duality |
| `thm:ordered-bimod-bicomod` | `theorem` | 1930 | Bimodule--bicomodule equivalence |
| `thm:ordered-diagonal` | `theorem` | 1955 | Diagonal correspondence |
| `thm:ordered-HH-coHH-homology` | `theorem` | 2003 | Hochschild--coHochschild duality, homological version |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | 2034 | Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-pair-of-pants` | `theorem` | 2082 | Ordered pair-of-pants algebra |
| `thm:ordered-master` | `theorem` | 2106 | Master theorem: the ordered open trace formalism |

#### `chapters/theory/nilpotent_completion.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:geom-conilpotent` | `proposition` | 89 | Geometric manifestation |
| `thm:completion-convergence` | `theorem` | 117 | Completion convergence |
| `thm:completed-bar-cobar` | `theorem` | 193 | Completed bar-cobar duality |
| `thm:koszul-dual-characterization` | `theorem` | 253 | Characterization of Koszul duals |
| `thm:stabilized-completion-positive` | `theorem` | 564 | Stabilized completion for positive towers |
| `thm:resonance-filtered-bar-cobar` | `theorem` | 675 | Resonance-filtered completed bar/cobar |
| `prop:resonance-ss-degeneration` | `proposition` | 779 | Resonance spectral sequence degeneration |
| `prop:resonance-ranks-standard` | `proposition` | 806 | Resonance ranks of the standard families |
| `cor:virasoro-resonance-ss` | `corollary` | 874 | Virasoro resonance spectral sequence |
| `conj:platonic-completion` | `theorem` | 947 | Resonance completion |

#### `chapters/theory/ordered_associative_chiral_kd.tex` (89)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bicom-e` | `lemma` | 164 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | 247 | Ordered chiral shuffle theorem |
| `sec:r-matrix-descent-vol1` | `proposition` | 507 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | 652 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | 796 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | 837 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | 851 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | 862 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | 924 | — |
| `prop:one-defect` | `proposition` | 951 | — |
| `thm:tangent=K` | `theorem` | 973 | Tangent identification |
| `cor:infdual` | `corollary` | 1010 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | 1033 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | 1085 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | 1118 | Diagonal correspondence |
| `cor:unit` | `corollary` | 1166 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | 1184 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | 1213 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | 1245 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | 1271 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | 1291 | Cap action |
| `thm:pair-of-pants` | `theorem` | 1345 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | 1383 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | 1437 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | 1486 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | 1510 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | 1627 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | 2060 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | 2174 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | 2256 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | 2315 | Formality: class~G, shadow depth~$2$ |
| `thm:drinfeld-yangian-sl2` | `theorem` | 2453 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | 2543 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | 2579 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | 2631 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | 2672 | Classical limit |
| `thm:central-extension-invisible` | `theorem` | 2758 | Central extension is invisible to the open-colour double bar |
| `thm:two-colour-double-kd` | `theorem` | 2824 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | 2850 | Non-redundancy of the two colours |
| `prop:vir-collision-residue` | `proposition` | 2916 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | 2946 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | 2973 | Gravitational Yangian collapse |
| `thm:vir-non-formality` | `theorem` | 3040 | Virasoro non-formality |
| `prop:grav-yangian-curvature` | `proposition` | 3106 | Gravitational Yangian curvature |
| `cor:gauge-gravity-dichotomy-ordered` | `corollary` | 3141 | Gauge-gravity complexity dichotomy |
| `thm:km-yangian` | `theorem` | 3259 | Universal Kac--Moody Yangian theorem |
| `thm:root-space-one-dim-v1` | `theorem` | 3583 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | 3632 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | 3698 | Dynkin coefficient via the beta integral |
| `thm:complete-strictification-v1` | `theorem` | 3779 | Complete strictification for all simple Lie algebras |
| `thm:sl3-triangle-coefficient` | `theorem` | 4009 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | 4093 | Serre relations from root-space vanishing |
| `thm:sl3-rtt` | `theorem` | 4144 | RTT presentation for $Y_\hbar(\mathfrak{sl}_3)$ from the ordered bar complex |
| `thm:sl3-strictification` | `theorem` | 4216 | Vanishing of the spectral Drinfeld class for $\mathfrak{sl}_3$ |
| `thm:sl4-quadrilateral` | `theorem` | 4289 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:B2-ordered-bar` | `theorem` | 4376 | Ordered bar complexes and Yangian $R$-matrices for rank-$2$ non-$A$ types |
| `thm:annular-bar-differential` | `theorem` | 4584 | Annular bar differential |
| `thm:annular-HH` | `theorem` | 4677 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | 4800 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:b-cycle-quantum-group` | `theorem` | 5127 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | 5249 | Drinfeld--Kohno; {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | 5328 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | 5399 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | 5440 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | 5603 | Ordered depth spectrum |
| `thm:ordered-AOS` | `theorem` | 5655 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | 5725 | Averaging and surplus |
| `thm:elliptic-spectral-dichotomy` | `theorem` | 5863 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `thm:bg-ordered-bar` | `theorem` | 6079 | Free-field ordered bar complexes |
| `thm:wakimoto-ordered-bar` | `theorem` | 6151 | Wakimoto bar complex descent |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | 6254 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | 6320 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | 6380 | Ordered Koszul dual of lattice algebras |
| `comp:sl2-eval` | `computation` | 6534 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | 6578 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | 6626 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | 6668 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | 6703 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `prop:eval-drinfeld` | `proposition` | 6755 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | 6822 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | 6883 | Braiding from the $R$-matrix |
| `prop:r-matrix-eigenvalue` | `proposition` | 6990 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | 7006 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | 7104 | $\mathsf{E}_1$ ordered bar landscape |
| `thm:w3-ordered-bar` | `theorem` | 7640 | Ordered bar complex of $\mathcal{W}_3$ via DS transport |
| `thm:class-m-ds-transport` | `theorem` | 7789 | Class~M persistence under DS transport |
| `thm:unshifted-identification` | `theorem` | 8019 | Unshifted identification |
| `thm:factorisation-identification` | `theorem` | 8063 | Factorisation identification on the Koszul locus |
| `prop:r-matrix-stable-envelope` | `proposition` | 8108 | $R$-matrix comparison |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 244 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 356 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 423 | Bar construction = Verdier dual coalgebra via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 516 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 575 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 591 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 682 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 772 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:bg-bar-coalg` | `proposition` | 259 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex coalgebra |
| `prop:chiral-operad-genus0` | `proposition` | 359 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 403 | Prism principle: operadic identification |
| `thm:prism-higher-genus` | `theorem` | 643 | Prism principle: higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | 715 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | 740 | The loop expansion is the genus expansion |
| `cor:prism-principle` | `corollary` | 845 | The prism principle |
| `thm:modular-convolution-structure` | `theorem` | 968 | dg~Lie structure |
| `thm:vol1-genus-completion` | `theorem` | 1008 | Genus completion |
| `prop:vol1-structure-as-MC` | `proposition` | 1056 | The algebra structure as MC element |
| `thm:partition` | `theorem` | 1162 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:quantum-linfty-master` | `theorem` | 630 | Quantum $L_\infty$ master equation |
| `prop:two-element-strict` | `proposition` | 876 | Two-element covers are strict |
| `prop:borcherds-shadow-identification` | `proposition` | 1360 | Secondary Borcherds operations as shadow obstruction tower obstructions |

#### `chapters/theory/spectral_sequences.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ss` | `theorem` | 271 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 323 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 389 | Central charge and \texorpdfstring{$d_1$}{d1} |

#### `chapters/theory/three_invariants.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:three-invariants-relations` | `proposition` | 179 | Relations and independence |
| `thm:k-max-trichotomy` | `theorem` | 313 | The $k_{\max}$ trichotomy |

### Part II: Examples (647)

#### `chapters/examples/bar_complex_tables.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 705 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 798 | Modular rank of \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 877 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 938 | PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} |
| `comp:sl3-casimir-decomp` | `computation` | 1031 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | 1113 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | 1442 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1747 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1793 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | 1864 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | 1915 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2049 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2085 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2119 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2548 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2754 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2974 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 3028 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3065 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3435 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3614 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3911 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3973 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4170 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4320 | BGG involution under Koszul duality |

#### `chapters/examples/beta_gamma.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 329 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 380 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 415 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 468 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 506 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | 527 | — |
| `thm:cobar-fermions` | `theorem` | 555 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | 592 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 681 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 948 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 1068 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 1175 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1316 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1400 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1551 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |
| `prop:mumford-exponent-complementarity` | `proposition` | 1726 | Mumford exponent complementarity |
| `thm:betagamma-quartic-birth` | `theorem` | 2063 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | 2099 | $\beta\gamma$ shadow obstruction tower: arity~$4$ on weight-changing line |
| `prop:betagamma-primitive-kernel` | `proposition` | 2127 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive kernel |
| `prop:betagamma-primitive-shell` | `proposition` | 2175 | \texorpdfstring{$\beta\gamma$}{beta-gamma} primitive shell equations |
| `lem:betagamma-ell2-vanishing` | `lemma` | 2322 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | 2369 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | 2479 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | 2521 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | 2551 | Pure contact boundary law |
| `prop:betagamma-translation-coproduct` | `proposition` | 2714 | Translation and coproduct |

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
| `prop:fermion-shadow-invariants` | `proposition` | 235 | Shadow invariants of the free fermion |
| `prop:fermion-shadow-metric` | `proposition` | 314 | Shadow metric of the free fermion |
| `thm:fermion-genus-expansion` | `theorem` | 348 | Free fermion genus expansion |
| `prop:fermion-rmatrix` | `proposition` | 425 | Free fermion $r$-matrix |
| `prop:fermion-complementarity` | `proposition` | 480 | Free fermion complementarity |
| `thm:fermion-sewing` | `theorem` | 550 | Free fermion sewing |
| `prop:fermion-characteristic-data` | `proposition` | 637 | Free fermion characteristic data |
| `thm:single-fermion-boson-duality` | `theorem` | 795 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | 847 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 903 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 954 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 965 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `prop:betagamma-deformation-channels` | `proposition` | 1040 | $\beta\gamma$ deformation complex |
| `prop:betagamma-T-line-shadows` | `proposition` | 1082 | $\beta\gamma$ shadow obstruction tower: T-line data |
| `prop:betagamma-weight-line-shadows` | `proposition` | 1117 | $\beta\gamma$ shadow obstruction tower: weight-changing line |
| `thm:betagamma-global-depth` | `theorem` | 1139 | $\beta\gamma$ global shadow depth |
| `prop:betagamma-shadow-metric` | `proposition` | 1207 | $\beta\gamma$ shadow metric |
| `comp:betagamma-shadow-weights` | `computation` | 1243 | $\beta\gamma$ shadow obstruction tower: special weight table |
| `prop:betagamma-weight-symmetry` | `proposition` | 1279 | Weight symmetry $\neq$ Koszul duality |
| `thm:heisenberg-bar` | `theorem` | 1364 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 1387 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | 1429 | Heisenberg curved structure |
| `thm:lattice-voa-bar` | `theorem` | 1476 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1505 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | 1535 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1572 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | 1621 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 1645 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 1860 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 1936 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 1968 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 2103 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 2158 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 2208 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 2250 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 2403 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 2479 | Spectral flow under Koszul duality |
| `thm:heisenberg-not-self-dual` | `theorem` | 2713 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2818 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2849 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 3111 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 3225 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 3510 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 3659 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 3714 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3782 | Heisenberg level inversion: curved duality |
| `thm:fermion-genus1-partition` | `theorem` | 3931 | Free fermion genus-1 partition functions |
| `thm:fermion-F1-shadow` | `theorem` | 4063 | Free fermion genus-1 free energy |
| `thm:fermion-genus-g` | `theorem` | 4140 | Free fermion at genus $g$ |
| `thm:virasoro-moduli` | `theorem` | 4485 | Critical Virasoro descent at $c = 26$ |
| `prop:moduli-degeneration` | `proposition` | 4583 | Boundary-residue differential on moduli forms |
| `thm:algebraic-string-dictionary` | `theorem` | 4712 | Algebraic bar/BRST genus dictionary |
| `thm:genus-g-chiral-homology` | `theorem` | 4819 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 4930 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 5010 | Bar classes on moduli and boundary factorization |
| `thm:modular-invariance` | `theorem` | 5138 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 5175 | Modular anomaly for affine Kac--Moody algebras |
| `thm:wakimoto-bar` | `theorem` | 5295 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 5308 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 5313 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 5340 | Higher \texorpdfstring{$A_\infty$}{A-infinity} corrections in quantum \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `comp:heisenberg-five-theorems` | `computation` | 5391 | Five projections of $\Theta_{\cH_k}$ |
| `comp:fermion-five-theorems` | `computation` | 5434 | Five projections of $\Theta_{\mathcal{F}}$ |
| `comp:betagamma-five-theorems` | `computation` | 5476 | Five projections of $\Theta_{\beta\gamma}$ |
| `comp:bc-five-theorems` | `computation` | 5531 | Five projections of $\Theta_{bc}$ |
| `comp:lattice-five-theorems` | `computation` | 5578 | Five projections of $\Theta_{V_\Lambda}$ |
| `thm:filtered-bar-complex` | `theorem` | 5659 | Filtered bar complex |

#### `chapters/examples/genus_expansions.tex` (39)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 100 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 174 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `thm:lattice-all-genera` | `theorem` | 218 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 253 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 275 | Uniform-weight $\mathcal{W}$-algebra free energy |
| `thm:sl2-all-genera` | `theorem` | 479 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 628 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 769 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 811 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 865 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 976 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 1086 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1226 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1293 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1358 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-$2$ free energy |
| `prop:w3-genus3-cross-channel` | `proposition` | 1441 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-$3$ cross-channel correction |
| `comp:w4-w5-grav-cross` | `computation` | 1477 | Universal gravitational cross-channel: $\cW_4$ and $\cW_5$ specializations |
| `comp:w4-full-ope-examples` | `computation` | 1550 | $\cW_4$ full-OPE cross-channel: the first irrational correction |
| `comp:genus2-complementarity-table` | `computation` | 1613 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1751 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1781 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1799 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1834 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1908 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 2036 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 2078 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 2163 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 2312 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2377 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:universal-fe-ratios` | `proposition` | 2622 | Universal free-energy ratios |
| `prop:complementarity-classification` | `proposition` | 2967 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 3025 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 3320 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 3421 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 3437 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 3462 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 3494 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 3589 | Loop expansion interpretation |
| `thm:boundary-characters-bar-hilbert` | `theorem` | 3760 | Boundary characters as bar Hilbert series |

#### `chapters/examples/heisenberg_eisenstein.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:heisenberg-gaussian-termination` | `proposition` | 69 | Gaussian shadow termination for Heisenberg |
| `thm:heisenberg-sewing` | `theorem` | 189 | Heisenberg sewing theorem |
| `prop:heisenberg-r-matrix` | `proposition` | 249 | Heisenberg $r$-matrix |
| `prop:heisenberg-complementarity` | `proposition` | 290 | Heisenberg complementarity |
| `thm:heisenberg-genus-one-complete` | `theorem` | 433 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 520 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 562 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 680 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 783 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 832 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 1161 | Multi-boson Eisenstein corrections |
| `thm:heisenberg-exact-linearity` | `theorem` | 1488 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | 1528 | Heisenberg shadow obstruction tower: finite termination at arity~$2$ |
| `cor:heisenberg-gaussian-boundary` | `corollary` | 1752 | Gaussian boundary law |
| `prop:heisenberg-primitive-kernel` | `proposition` | 1863 | Heisenberg primitive kernel |
| `prop:heisenberg-primitive-shell` | `proposition` | 1900 | Heisenberg primitive shell equations |
| `prop:heisenberg-open-sector` | `proposition` | 1986 | Open-sector category for Heisenberg |
| `thm:heisenberg-modular-cooperad` | `theorem` | 2114 | Modular cooperad structure on $\Cop(\cH_\kappa)$ |

#### `chapters/examples/kac_moody.tex` (54)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:km-genus1-hessian` | `computation` | 210 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_2$ |
| `thm:geometric-ope-kac-moody` | `theorem` | 441 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 475 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 515 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 588 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 753 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 784 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 822 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 880 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 916 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 985 | Universal Koszul duality for affine Kac--Moody |
| `lem:killing-structure-constants` | `lemma` | 1019 | Killing form via structure constants |
| `prop:verdier-level-identification` | `proposition` | 1104 | Verdier level identification |
| `prop:ff-channel-shear` | `proposition` | 1455 | Feigin--Frenkel shear on channel pair |
| `prop:exceptional-shadow-invariants` | `proposition` | 1506 | Exceptional shadow invariants |
| `thm:screening-bar` | `theorem` | 1676 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 1742 | Critical fixed point for principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:kac-moody-ainfty` | `theorem` | 1811 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1850 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1904 | Closed-form OPE for Koszul dual |
| `comp:sl2-collision-residue-kz` | `computation` | 1963 | Collision residue and the KZ $r$-matrix for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:km-quantum-groups` | `theorem` | 2257 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 2608 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 2680 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 2862 | Kac--Wakimoto formula at \texorpdfstring{$k=-1/2$}{k=-1/2} via bar spectral sequence |
| `prop:admissible-verlinde-bar` | `proposition` | 3034 | Admissible \texorpdfstring{$S$}{S}-matrix and Verlinde fusion package at \texorpdfstring{$k=-1/2$}{k=-1/2} |
| `prop:bar-whittaker` | `proposition` | 3354 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 3435 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 3500 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 3570 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 3636 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 3699 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 3745 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 3784 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 3821 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 4029 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 4059 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 4089 | Local oper differential-form identification |
| `thm:affine-cubic-normal-form` | `theorem` | 4354 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | 4390 | Affine shadow obstruction tower: finite termination at arity~$3$ |
| `prop:affine-primitive-kernel` | `proposition` | 4428 | Affine primitive kernel |
| `prop:affine-primitive-shell` | `proposition` | 4470 | Affine primitive shell equations |
| `prop:affine-cyclic-slice-data` | `proposition` | 4540 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 4588 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 4645 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 4722 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 4808 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 4844 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 4935 | Vanishing of the genus loop on the affine cubic |
| `prop:nsl-shadow-tower` | `proposition` | 5012 | Non-simply-laced shadow obstruction tower |
| `prop:complete-exceptional-shadow` | `proposition` | 5150 | Complete exceptional shadow data |
| `prop:exceptional-anomaly-ratios` | `proposition` | 5234 | Anomaly ratios for exceptional principal $\mathcal{W}$-algebras |
| `cor:level-rank-bar-intertwining` | `corollary` | 5486 | Bar-complex intertwining |
| `prop:kappa-anti-symmetry-ff` | `proposition` | 5514 | Kappa anti-symmetry under Feigin--Frenkel involution |

#### `chapters/examples/landscape_census.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 691 | Paired standard-tower MC4 completion packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 811 | Minimal closure conditions for the standard-tower MC4 completion target |
| `cor:anomaly-ratio-ds` | `corollary` | 1056 | Anomaly ratio and DS reduction |
| `cor:genus1-anomaly-ratio` | `corollary` | 1070 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `cor:subexp-free-field` | `corollary` | 1875 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 1885 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 1902 | DS reduction and bar cohomology generating functions |
| `thm:ds-spectral-branch-preservation` | `theorem` | 2069 | DS preservation of the sub-discriminant |
| `prop:ds-invariant-discriminant` | `proposition` | 2223 | DS-invariant discriminant subfactor |
| `prop:hred-sl2` | `proposition` | 2267 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 2478 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 2569 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 2666 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 2732 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 2787 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 2838 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 2853 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 2942 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 3131 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 3437 | Spectral sequence collapse |

#### `chapters/examples/lattice_foundations.tex` (43)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lattice-sewing` | `theorem` | 119 | Lattice sewing envelope |
| `lem:lattice:cocycle-class` | `lemma` | 390 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 554 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 773 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 870 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 893 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 927 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 961 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 1006 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 1092 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 1137 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1342 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1387 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1429 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1452 | Modular invariance |
| `thm:lattice:niemeier-shadow-universality` | `theorem` | 1526 | Niemeier shadow universality |
| `prop:lattice:niemeier-theta-decomposition` | `proposition` | 1581 | Niemeier theta series decomposition |
| `thm:lattice:niemeier-siegel-genus2` | `theorem` | 1629 | Genus-$2$ Siegel theta series of Niemeier lattices |
| `prop:lattice:self-dual-criterion` | `proposition` | 1848 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1865 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1890 | Lattice twisted-sector charge inversion on the bar surface |
| `prop:lattice:deformation-properties` | `proposition` | 2074 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 2258 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2883 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2951 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 3025 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 3184 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3486 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3567 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3740 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3945 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3988 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 4146 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 4193 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 4279 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 4360 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |
| `prop:lattice:genus1-simple-pole` | `proposition` | 4549 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4566 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | 4663 | Lattice shadow obstruction tower: termination at weight~$2$ |
| `prop:xxx-shadow-data` | `proposition` | 4796 | XXX shadow data |
| `prop:transfer-matrix-shadow-dict` | `proposition` | 4835 | Transfer matrix--shadow dictionary |
| `prop:xxz-shadow-data` | `proposition` | 4883 | XXZ shadow data |
| `prop:shadow-cardy-corrections` | `proposition` | 4950 | Shadow hierarchy and Cardy corrections |

#### `chapters/examples/minimal_model_examples.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 406 | Fusion from bar complex on the torus |
| `prop:ising-shadow-invariants` | `proposition` | 541 | Ising shadow invariants |
| `thm:ising-shadow-growth-rate` | `theorem` | 578 | Ising shadow growth rate |
| `prop:ising-koszul-dual` | `proposition` | 640 | Koszul dual complementarity |
| `prop:ising-free-energies` | `proposition` | 679 | Ising scalar free energies |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 83 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | 217 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 365 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 389 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | 424 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 449 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 528 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 555 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 615 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 635 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 662 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 758 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

#### `chapters/examples/toroidal_elliptic.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 386 | Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0} |
| `thm:elliptic-vs-rational` | `theorem` | 484 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 856 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1052 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1130 | DYBE and bar nilpotency |
| `prop:kappa-k3` | `proposition` | 1685 | Modular characteristic of the K3 sigma model |
| `prop:bar-n4-sca` | `proposition` | 1749 | Bar complex structure |
| `prop:shadow-class-k3` | `proposition` | 1776 | K3 sigma model: class M |
| `prop:koszul-dual-k3` | `proposition` | 2036 | Koszul dual of $\cA_{K3}$ |
| `prop:boundary-sigma-ratio` | `proposition` | 2466 | Boundary-to-sigma ratio |
| `prop:kappa-bps-decomposition` | `proposition` | 2767 | The BPS modular characteristic |
| `prop:class-g-no-instantons` | `proposition` | 3544 | Class G algebras: shadow $=$ topological string |
| `prop:bar-hocolim` | `proposition` | 3588 | Bar functor commutes with homotopy colimits |
| `prop:shadow-k3e` | `proposition` | 3836 | Shadow amplitudes of $K3 \times E$ |
| `prop:shadow-gf-convergence` | `proposition` | 3891 | Convergence of the shadow generating function |
| `thm:shadow-siegel-gap` | `theorem` | 3946 | Shadow--Siegel gap |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 45 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 147 | Mode expansion |
| `thm:c-scaling` | `theorem` | 198 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 288 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 453 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | 537 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 588 | Quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | 649 | Two-point function \texorpdfstring{$\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$}{:W2:_qp(z) :W2:_qp(w)} |
| `thm:w3-null-level1` | `theorem` | 709 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 812 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 883 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 925 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 996 | Level-2 Gram matrix |

#### `chapters/examples/w3_holographic_datum.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3hol-conductor` | `theorem` | 239 | Koszul conductor and self-dual point |
| `thm:w3hol-r-channels` | `theorem` | 334 | Channel-by-channel \texorpdfstring{$r$}{r}-matrix |
| `thm:w3hol-propagator-variance` | `theorem` | 551 | Propagator variance for \texorpdfstring{$\Walg_3$}{W3} |
| `thm:w3hol-Q-T` | `theorem` | 604 | Shadow metric on the \texorpdfstring{$T$}{T}-line |
| `thm:w3hol-Q-W` | `theorem` | 617 | Shadow metric on the \texorpdfstring{$W$}{W}-line |
| `thm:w3hol-discriminants` | `theorem` | 628 | Critical discriminants and shadow class |
| `thm:w3hol-commuting-differentials` | `theorem` | 669 | Commuting differentials at \texorpdfstring{$N=3$}{N=3} |

#### `chapters/examples/w_algebras.tex` (70)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:w3-genus1-hessian` | `computation` | 213 | The $\mathcal W_3$ genus-$1$ Hessian |
| `comp:w-entropy-ladder` | `computation` | 262 | Completion entropy ladder |
| `thm:w-algebra-koszul-main` | `theorem` | 317 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `thm:w-geometric-ope` | `theorem` | 1073 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 1144 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-koszul-precise` | `theorem` | 1202 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras, precise statement |
| `thm:virasoro-self-duality` | `theorem` | 1335 | Virasoro quadratic self-duality |
| `prop:virasoro-generic-koszul-dual` | `proposition` | 1429 | Virasoro Koszul dual at generic central charge |
| `thm:vir-genus1-curvature` | `theorem` | 1585 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1636 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1700 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1870 | Critical fixed point and general-level duality for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1950 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 2016 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 2086 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 2181 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 2293 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 2314 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-ainfty-ops` | `theorem` | 2536 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `thm:agt-shadow-correspondence` | `theorem` | 2614 | AGT shadow correspondence |
| `thm:w-universal-gravitational-cubic` | `theorem` | 3554 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | 3609 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | 3646 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | 3733 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-resonance-reorganization` | `theorem` | 3803 | Resonance reorganization |
| `cor:w-complementarity-potential-poles` | `corollary` | 3940 | Pole structure of the complementarity potential |
| `prop:virasoro-primitive-kernel` | `proposition` | 3995 | Virasoro primitive kernel |
| `prop:virasoro-primitive-shell` | `proposition` | 4047 | Virasoro primitive shell equations |
| `thm:w-w3-mixed-shadow` | `theorem` | 4204 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w3-two-dim-hessian-cubic` | `proposition` | 4268 | Two-dimensional Hessian and universal cubic |
| `thm:w3-quartic-channel-decomposition` | `theorem` | 4296 | $\mathcal{W}_3$ quartic channel decomposition |
| `prop:w3-denominator-filtration` | `proposition` | 4357 | Denominator filtration by $W$-charge |
| `thm:w3-quintic-nonvanishing` | `theorem` | 4385 | $\mathcal{W}_3$ quintic nonvanishing |
| `prop:ds-shadow-cascade` | `proposition` | 4430 | DS shadow cascade for $V_k(\mathfrak{sl}_N) \to \mathcal{W}_N$ |
| `prop:rho-decreasing-with-N` | `proposition` | 4487 | Shadow growth rate decreases with $N$ |
| `prop:w-w3-weight6-resonance` | `proposition` | 4597 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | 4668 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | 4694 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-archetype-trichotomy` | `theorem` | 4783 | Archetype trichotomy |
| `thm:w-virasoro-quintic-forced` | `theorem` | 4850 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | 4906 | Explicit quintic shadow for Virasoro |
| `thm:virasoro-shadow-generating-function` | `theorem` | 4958 | Virasoro shadow metric |
| `thm:w-finite-termination` | `theorem` | 5208 | Finite termination for primitive archetypes |
| `cor:virasoro-postnikov-nontermination` | `corollary` | 5281 | Virasoro/$\mathcal{W}_N$ shadow obstruction tower: infinite |
| `thm:w-virasoro-genus1-hessian` | `theorem` | 5319 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | 5473 | $\mathcal{W}_3$ quintic obstruction |
| `prop:w3-wline-ring-relations` | `proposition` | 5668 | $W$-line ring relations |
| `thm:w-finite-arity-polynomial-pva` | `theorem` | 5961 | Finite-arity theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | 5999 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | 6041 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | 6068 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | 6144 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | 6169 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | 6203 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | 6241 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | 6261 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `prop:miura-arity-sharp` | `proposition` | 6345 | Miura arity bound is sharp |
| `thm:w-pbw-slodowy-collapse` | `theorem` | 6494 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | 6555 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-arity-detection` | `theorem` | 6663 | Canonical arity detection |
| `thm:w-bp-strict` | `theorem` | 6689 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | 6739 | $\mathcal{W}_4^{(2)}$ has canonical arity~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | 6798 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | 6857 | Subregular Appell formula |
| `thm:w-unbounded-canonical-arity` | `theorem` | 6895 | Unbounded canonical arity |
| `cor:w-subregular-arity-staircase` | `corollary` | 6924 | The subregular arity staircase |
| `thm:w-subregular-classification` | `theorem` | 6966 | Subregular classification |
| `prop:sl3-nilpotent-shadow-data` | `proposition` | 7050 | $\mathfrak{sl}_3$ nilpotent orbits: shadow data |
| `prop:sl4-hook-shadow-data` | `proposition` | 7104 | $\mathfrak{sl}_4$ hook-type shadow data |
| `thm:ds-shadow-functor-arity2` | `theorem` | 7145 | DS shadow functor at arity~$2$ |

#### `chapters/examples/w_algebras_deep.tex` (37)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 131 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 1037 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `thm:master-commutative-square` | `theorem` | 1322 | Master commutative square for DS reduction |
| `prop:w3-deg3-vacuum` | `proposition` | 1729 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-bar-formality` | `proposition` | 2022 | DS--bar commutation via filtration formality |
| `thm:transport-closure-type-a` | `theorem` | 2092 | Transport-closure in type $A$ |
| `prop:partition-dependent-complementarity` | `proposition` | 2146 | Kappa deficit and Koszul complementarity for non-principal DS |
| `thm:ds-platonic-functor` | `theorem` | 2239 | BRST reduction on total modular Koszul datums |
| `cor:ds-theta-descent` | `corollary` | 2466 | BRST descent of the universal MC element |
| `comp:wn-stabilization-windows` | `computation` | 2908 | Coefficient stabilization windows for $\mathcal{W}_N$ |
| `prop:abelian-locus-type-a` | `proposition` | 2978 | Abelian locus in type~$A$ |
| `prop:abelianity-complementarity-independence` | `proposition` | 3020 | Independence of abelianity and complementarity |
| `prop:bfn-slodowy-dimensions` | `proposition` | 3101 | BFN--Slodowy dimension matching |
| `prop:ghost-constant-monotonicity` | `proposition` | 3174 | Ghost constant monotonicity |
| `thm:winfty-scalar` | `theorem` | 3395 | One-dimensional cyclic line for $\mathcal{W}_\infty$ |
| `prop:gram-wt4` | `proposition` | 3550 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | 3615 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | 3658 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:higher-w-kappa-matrix` | `proposition` | 3786 | Kappa matrix for $\Walg_N$ |
| `prop:higher-w-gravitational-cubic` | `proposition` | 3849 | Gravitational cubic for $\Walg_N$ |
| `prop:higher-w-parity` | `proposition` | 3892 | $\mathbb{Z}_2$ parity and the cubic shadow |
| `prop:weight-4-exchange-upgrade` | `proposition` | 3949 | Weight-$4$ exchange spectrum upgrade at rank~$3$ |
| `prop:virasoro-primitive` | `proposition` | 4240 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | 4301 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | 4342 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | 4445 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | 4478 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | 4499 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | 4531 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | 4638 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | 4674 | $\Walg_\infty$ bar-window series and Koszul entropy |
| `thm:y-algebra-koszulness` | `theorem` | 4760 | Chiral Koszulness of $Y$-algebras |
| `thm:n2-kappa` | `theorem` | 4917 | $N=2$ modular characteristic |
| `prop:n2-koszul-duality` | `proposition` | 4973 | $N=2$ Koszul duality |
| `prop:n2-channel-decomposition` | `proposition` | 5000 | $N=2$ channel decomposition |
| `prop:n2-bosonic-shadow-metric` | `proposition` | 5033 | $N=2$ bosonic shadow metric |
| `prop:n2-minimal-models` | `proposition` | 5078 | $N=2$ minimal model shadow data |

#### `chapters/examples/yangians_computations.tex` (48)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:yangian-rank-dependence` | `proposition` | 525 | Rank dependence of Yangian bar complex |
| `comp:sl3-yangian-from-ordered-bar` | `computation` | 562 | The \texorpdfstring{$\mathfrak{sl}_3$}{sl3} Yangian $R$-matrix from the ordered bar |
| `prop:rmatrix-from-bar` | `proposition` | 723 | Classical and quantum $R$-matrices from the bar complex |
| `thm:quantum-rmatrix-shadow` | `theorem` | 831 | Quantum $R$-matrix from the shadow obstruction tower |
| `prop:colored-rmatrix` | `proposition` | 891 | Colored $R$-matrices and Casimir eigenvalues |
| `thm:bethe-from-mc` | `theorem` | 935 | Bethe ansatz from the MC equation |
| `thm:bae-from-mc` | `theorem` | 1038 | Bethe ansatz equations from the shadow potential |
| `prop:eval-module-bar` | `proposition` | 1175 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 1265 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 1315 | Bar-comodule Ext comparison for Yangian evaluation modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 1372 | DK-2 reduction to thick generation, conditional on an ambient exact extension |
| `prop:dk2-thick-generation-typeA` | `proposition` | 1437 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `cor:dk2-thick-generation-all-types` | `corollary` | 1532 | Thick generation for all simple types |
| `lem:composition-thick-generation` | `lemma` | 1557 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 1588 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `lem:monoidal-thick-extension` | `lemma` | 1726 | Monoidal extension to thick closures |
| `lem:fd-thick-closure` | `lemma` | 1916 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 2002 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 2253 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 2383 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 2541 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 2561 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 2586 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 2760 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:baxter-exact-triangles-opoly` | `theorem` | 2828 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `conj:baxter-exact-triangles` | `theorem` | 2870 | Baxter exact triangles on shifted envelope \texorpdfstring{$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$}{Osh} |
| `prop:baxter-yangian-equivariance` | `proposition` | 2918 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | 2992 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `thm:shifted-prefundamental-generation` | `theorem` | 3037 | $E_1$-chiral thick generation for $Y(\mathfrak{sl}_N)$ |
| `prop:prefundamental-clebsch-gordan` | `proposition` | 3262 | Universal prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | 3302 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | 3315 | $K_0$ generation for all simple types |
| `prop:categorical-cg-typeA` | `proposition` | 3364 | Categorical prefundamental CG decomposition, type~$A$ |
| `conj:pro-weyl-recovery` | `theorem` | 3461 | Pro-Weyl recovery of ordinary standards in type~$A$ |
| `thm:mc3-type-a-resolution` | `theorem` | 3719 | Type-$A$ MC3 reduction to the compact-completion packet |
| `conj:mc3-arbitrary-type` | `theorem` | 3798 | Categorical prefundamental CG decomposition, all types |
| `cor:mc3-all-types` | `corollary` | 3945 | All-types MC3 reduction after categorical CG closure |
| `prop:e8-root-uniformity` | `proposition` | 4070 | $E_8$ relevant-root uniformity |
| `prop:character-cg-all-types` | `proposition` | 4080 | Character-level Clebsch--Gordan for all simple types |
| `thm:yangian-vector-seed-propagation` | `theorem` | 4437 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | 4467 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | 4490 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | 4505 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | 4556 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | 4581 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | 4608 | Derived realization of the Baxter--Rees family |
| `thm:yangian-H2-reduction` | `theorem` | 4675 | $H^2$-reduction to the three-leg sector |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | 4752 | Concrete cocycle |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (96)

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
| `thm:factorization-positselski` | `theorem` | 1478 | Factorization Positselski equivalence on the bar-coalgebra surface |
| `thm:ind-completed-extension` | `theorem` | 1614 | Ind-completion of the generated-core DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 1814 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 1921 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 2019 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 2234 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 2314 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `thm:bridge-criterion` | `theorem` | 2495 | Bridge Criterion Theorem |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 2747 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 2867 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 2926 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 3009 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 3090 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 3121 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 3158 | Compact-core DK-5 functors from realization of a finite-dimensional factorization DK pair |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 3226 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 3256 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 3288 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 3347 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 3426 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 3455 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 3522 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 3554 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 3592 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 3607 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 3657 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 3714 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 3761 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 3852 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 3952 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 3992 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 4028 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 4055 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 4198 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 4236 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 4286 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 4324 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 4351 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 4390 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 4428 | DK-5 closes once the compact cores realize a finite-dimensional factorization DK pair |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 4453 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 4651 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 4714 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 4749 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 4803 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 4836 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 4902 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 4981 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts-orig` | `corollary` | 5135 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet-orig` | `corollary` | 5164 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization-orig` | `corollary` | 5197 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of a chosen finite-dimensional factorization DK pair |
| `cor:yangian-formal-moduli-plus-core-realization-orig` | `corollary` | 5227 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize a chosen finite-dimensional DK pair |
| `cor:yangian-typea-realization-plus-dg-packet-orig` | `corollary` | 5277 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 5385 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 5488 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 5549 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 5599 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 5658 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed-orig` | `corollary` | 5701 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line-orig` | `corollary` | 5734 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |
| `prop:ds-functor-primitive-triple` | `proposition` | 6324 | DS reduction on primitive triples |
| `prop:free-propagator-matching` | `proposition` | 6758 | Free/Heisenberg propagator matching |
| `prop:affine-propagator-matching` | `proposition` | 6803 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `prop:rmatrix-pole-landscape` | `proposition` | 6880 | The collision-residue $r$-matrix across the standard landscape |
| `prop:bosonic-parity-constraint` | `proposition` | 6983 | Bosonic parity constraint on $r$-matrix poles |
| `prop:cybe-from-mc` | `proposition` | 7026 | CYBE from bar-complex MC equation |
| `prop:rmatrix-from-bar-coproduct` | `proposition` | 7129 | Quantum $R$-matrix from the bar coproduct |
| `prop:elliptic-rmatrix-shadow` | `proposition` | 7217 | Elliptic $R$-matrix from the genus-$1$ shadow |
| `thm:bae-from-mc-stationarity` | `theorem` | 7329 | Bethe ansatz equations from the MC stationarity |
| `prop:kz-from-shadow` | `proposition` | 7436 | KZ equation from the shadow connection |
| `prop:verlinde-from-shadow` | `proposition` | 7540 | Verlinde formula from the shadow complex |
| `thm:rmatrix-koszul-inverse` | `theorem` | 7762 | Collision residue as binary Koszul inverse |
| `thm:r-matrix-koszul-dual-inverse` | `theorem` | 7889 | The $r$-matrix as Koszul-dual inverse |
| `thm:spectral-derived-additive-kz` | `theorem` | 8102 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | 8201 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | 8248 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | 8322 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | 8406 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | 8463 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | 8505 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | 8540 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | 8595 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | 8667 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | 8691 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | 8731 | Exact free transport |
| `thm:spectral-conditional-strictification` | `theorem` | 8765 | Conditional strictification criterion |

#### `chapters/examples/yangians_foundations.tex` (44)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:rtt-all-classical-types` | `theorem` | 236 | RTT R-matrices for all classical types |
| `thm:yangian-e1` | `theorem` | 381 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 468 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 501 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 560 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 622 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 677 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 741 | Koszul duality on Yangian modules |
| `thm:rtt-all-types` | `theorem` | 1187 | RTT presentation and MC3 for all simple types |
| `prop:dg-shifted-comparison` | `proposition` | 1423 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1550 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1594 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1705 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1809 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1827 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1857 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1919 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 1983 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 2069 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 2166 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 2236 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 2305 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 2342 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2398 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2458 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2519 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2618 | Standard type-A fundamental line operator has the standard local residue |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | 3044 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | 3071 | Stabilized completed bar/cobar recovery |
| `cor:shifted-rtt-tower-convergence` | `corollary` | 3102 | Automatic tower convergence |
| `thm:shifted-rtt-mc-descent` | `theorem` | 3132 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | 3220 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | 3265 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | 3313 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | 3329 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | 3359 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | 3392 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | 3426 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | 3451 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | 3523 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | 3572 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | 3598 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | 3625 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | 3647 | Kleinian associated graded at the nilpotent point |

### Part III: Connections (805)

#### `chapters/connections/arithmetic_shadows.tex` (127)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:shadow-spectral-correspondence` | `theorem` | 120 | Shadow--spectral correspondence |
| `prop:divisor-sum-decomposition` | `proposition` | 226 | Divisor-sum decomposition |
| `cor:sewing-euler-product` | `corollary` | 251 | Euler product of the sewing determinant |
| `prop:sewing-trace-formula` | `proposition` | 264 | Sewing trace formula |
| `thm:sewing-selberg-formula` | `theorem` | 296 | Sewing--Selberg formula |
| `thm:narain-universality` | `theorem` | 353 | Narain universality |
| `thm:e8-epstein` | `theorem` | 384 | $E_8$ Epstein factorization |
| `prop:z2-epstein` | `proposition` | 409 | $\bZ^2$ Epstein zeta |
| `prop:leech-epstein` | `proposition` | 432 | Leech Epstein factorization |
| `prop:niemeier-multichannel` | `proposition` | 600 | Multi-channel Niemeier discrimination |
| `prop:shadow-arithmetic-factorization` | `proposition` | 688 | Shadow--arithmetic factorization |
| `prop:leading-hecke-identification` | `proposition` | 903 | Leading-order Hecke identification |
| `rem:hecke-all-orders` | `proposition` | 930 | Exactness of the Hecke identification |
| `prop:period-shadow-dictionary` | `proposition` | 981 | Period--shadow dictionary |
| `comp:period-shadow-vz` | `computation` | 1064 | $V_{\bZ}$: the Gaussian archetype |
| `comp:period-shadow-ve8` | `computation` | 1082 | $V_{E_8}$: the Lie/tree archetype |
| `comp:period-shadow-leech` | `computation` | 1104 | $V_{\mathrm{Leech}}$: the Ramanujan archetype |
| `comp:period-shadow-rank24-comparison` | `computation` | 1156 | $D_{16}^+ \oplus D_{16}^+$ vs.\ $E_8^3$: same depth, different coefficient |
| `comp:period-shadow-rank2` | `computation` | 1175 | $V_{\bZ^2}$ and $V_{A_2}$: Dedekind zeta at depth~$2$ |
| `thm:spectral-decomposition-principle` | `theorem` | 1199 | Spectral decomposition principle |
| `prop:growth-rate-dictionary` | `proposition` | 1286 | Growth-rate dictionary |
| `thm:bg-vir-coincidence` | `theorem` | 1312 | $\beta\gamma$--Virasoro rate coincidence |
| `prop:self-referentiality-criterion` | `proposition` | 1330 | Self-referentiality criterion |
| `cor:conformal-vector-infinite-depth` | `corollary` | 1400 | Conformal vector implies infinite depth |
| `thm:shadow-tower-asymptotics` | `theorem` | 1423 | Shadow obstruction tower leading asymptotics |
| `cor:rigorous-infinite-depth` | `corollary` | 1455 | Rigorous infinite depth |
| `prop:bg-primary-counting` | `proposition` | 1489 | $\beta\gamma$ primary-counting function |
| `thm:refined-shadow-spectral` | `theorem` | 1502 | Refined shadow--spectral correspondence |
| `prop:ising-d-arith` | `proposition` | 1532 | Ising model: $d_{\mathrm{arith}} = 0$ |
| `rem:ising-arithmetic-paradox` | `remark` | 1560 | The Ising arithmetic paradox |
| `rem:non-unimodular` | `remark` | 1628 | Non-unimodular lattices |
| `thm:depth-decomposition` | `theorem` | 1697 | Depth decomposition |
| `rem:depth-decomposition-universality` | `remark` | 1789 | Universality and the complete $d_{\mathrm{alg}}$ table |
| `rem:vnatural-class-m` | `remark` | 1847 | The moonshine module: same $\kappa$, different class |
| `thm:ainfty-formality-depth` | `theorem` | 1885 | $A_\infty$ formality criterion |
| `thm:interacting-gram-positivity` | `theorem` | 1943 | Interacting Gram positivity |
| `cor:virasoro-interacting-gram` | `corollary` | 1983 | — |
| `thm:shadow-resonance-locus` | `theorem` | 1996 | — |
| `prop:shadow-spectral-measure` | `theorem` | 2034 | Shadow spectral measure |
| `prop:carleman-virasoro` | `proposition` | 2126 | Carleman rigidity |
| `prop:shadow-periods` | `proposition` | 2163 | Shadow amplitudes are periods |
| `prop:resurgent-orthogonality` | `proposition` | 2315 | Two orthogonal resurgent directions |
| `prop:padic-convergence` | `proposition` | 2379 | $p$-adic convergence radius |
| `rem:kummer-kubota-leopoldt` | `remark` | 2405 | Kummer congruences and the Kubota--Leopoldt $p$-adic $L$-function |
| `thm:shadow-mzv-dictionary` | `theorem` | 2510 | Shadow--MZV dictionary |
| `thm:drinfeld-associator-bar-transport` | `theorem` | 2590 | Drinfeld associator as bar transport |
| `thm:partition-modular-classification` | `theorem` | 2693 | Partition function modular classification |
| `prop:quasi-modular-propagator` | `proposition` | 2753 | Quasi-modular content from the genus-$1$ propagator |
| `prop:hecke-eigenvalue-extraction` | `proposition` | 2828 | Hecke eigenvalues from partition data |
| `thm:spectral-curve` | `theorem` | 2875 | Algebraic shadow generating function |
| `prop:moment-matrix-negativity` | `proposition` | 2918 | Eisenstein moment minor |
| `thm:shadow-higgs-field` | `theorem` | 3173 | Shadow Higgs field |
| `thm:general-nahc` | `theorem` | 3254 | General shadow triple |
| `prop:shadow-oper-rigid` | `proposition` | 3528 | Shadow oper as rigid hypergeometric |
| `prop:shadow-langlands-hierarchy` | `proposition` | 3614 | The $\cW_3$ shadow oper beyond Eisenstein |
| `thm:shadow-bps` | `theorem` | 3783 | The shadow obstruction tower as BPS spectrum |
| `thm:general-bps` | `theorem` | 3867 | General BPS spectrum of the shadow obstruction tower |
| `thm:sewing-shadow-intertwining` | `theorem` | 3967 | Sewing--shadow intertwining at genus~$1$ |
| `cor:shadow-fredholm` | `corollary` | 4042 | Shadow Fredholm determinant |
| `cor:spectral-measure-identification` | `corollary` | 4079 | Spectral measure identification |
| `sec:shadow-moduli-resolution` | `theorem` | 4133 | Shadow-moduli resolution |
| `thm:universality-of-G` | `theorem` | 4223 | Universality of $G$ |
| `prop:mc-bracket-determines-atoms` | `proposition` | 4291 | MC bracket determines spectral atoms |
| `rem:mc-ramanujan-bridge` | `remark` | 4341 | The bridge to the Ramanujan bound |
| `prop:heisenberg-koszul-epstein` | `proposition` | 4592 | Degenerate case: Heisenberg |
| `comp:virasoro-c1-koszul-epstein` | `computation` | 4644 | Virasoro at $c = 1$: numerical Koszul--Epstein value |
| `comp:fe-minimal-models` | `computation` | 4669 | Functional equation for all unitary minimal models |
| `thm:spectral-continuation-bridge` | `theorem` | 4749 | Hecke-equivariant MC element |
| `thm:schur-complement-quartic` | `theorem` | 4888 | — |
| `prop:virasoro-quartic-determinant` | `proposition` | 4947 | — |
| `prop:on-off-line-distinction` | `proposition` | 5024 | — |
| `prop:li-criterion-failure` | `proposition` | 5434 | Structural failure of the Li criterion for the sewing lift |
| `prop:pure-spin-s-schur` | `proposition` | 5584 | — |
| `prop:prime-side-defect-formula` | `proposition` | 5692 | — |
| `thm:finite-miura-defect` | `theorem` | 5762 | Finite Miura defect at genus one |
| `prop:modularity-constraint` | `proposition` | 6334 | Modularity constraint on the spectral measure |
| `sec:bracket-hodge-index` | `proposition` | 6377 | Bracket positivity and the Hodge index |
| `sec:proved-regime-ramanujan` | `proposition` | 6503 | Ramanujan bound for lattice spectral measures |
| `sec:symmetric-power-route` | `proposition` | 6546 | Shadow--symmetric power identification |
| `thm:petersson-identification` | `theorem` | 6693 | Petersson identification |
| `prop:modularity-constraint-atoms` | `proposition` | 6779 | Modularity constraint on atoms |
| `prop:rigidity-threshold` | `proposition` | 6816 | Rigidity threshold |
| `prop:lattice-ramanujan-rigidity` | `proposition` | 6914 | Lattice Ramanujan from rigidity |
| `prop:stieltjes-signed-universal` | `proposition` | 7110 | Universal signed Stieltjes measure |
| `prop:rational-cft-multiplicativity-failure` | `proposition` | 7143 | Multiplicativity failure for rational CFT |
| `prop:shadow-arithmetic-trichotomy` | `proposition` | 7207 | Shadow arithmetic trichotomy |
| `prop:genus1-weight-bound` | `proposition` | 7282 | Weight bound for genus-$1$ shadow projections |
| `thm:mc-recursion-moment` | `theorem` | 7414 | MC recursion on moment $L$-functions |
| `prop:shadow-chiral-graph` | `proposition` | 7481 | Shadow amplitudes as chiral graph integrals |
| `thm:hecke-newton-lattice` | `theorem` | 7554 | Hecke--Newton closure for lattice VOAs |
| `cor:unconditional-lattice` | `corollary` | 7617 | Unconditional operadic RS for lattice VOAs |
| `thm:non-lattice-ramanujan` | `theorem` | 7646 | Non-lattice Ramanujan bound |
| `prop:mc-constraint-counting` | `proposition` | 8163 | MC constraint counting |
| `thm:route-c-propagation` | `theorem` | 8228 | Route~C: MC rigidity forces character-level prime-locality |
| `cor:route-c-standard-landscape` | `corollary` | 8351 | Route~C for the standard landscape |
| `thm:hecke-verdier-commutation` | `theorem` | 8390 | Verdier--Hecke commutation at genus~$1$ |
| `thm:self-dual-factorization` | `theorem` | 8429 | Self-dual factorisation |
| `prop:theta-bridge-rational` | `proposition` | 8504 | Theta decomposition bridge |
| `prop:newton-shadow-hecke` | `proposition` | 8567 | Newton--shadow--Hecke correspondence |
| `prop:sewing-spectral-bridge` | `proposition` | 8685 | Sewing--spectral determinant bridge |
| `prop:rs-analytic-continuation` | `proposition` | 8790 | Meromorphic continuation of the RS integral |
| `prop:scattering-residue` | `proposition` | 8837 | Holomorphy at scattering poles |
| `prop:arith-geom-decomposition` | `proposition` | 8928 | Arithmetic--geometric decomposition |
| `prop:genus-one-saddle-triviality` | `proposition` | 9102 | Genus-one saddle triviality |
| `cor:first-scattering-pole` | `corollary` | 9302 | Nonvanishing at the first scattering pole |
| `thm:scattering-coupling-factorization` | `theorem` | 9403 | Scattering coupling factorization |
| `thm:structural-separation` | `theorem` | 9486 | Structural separation of algebraic and arithmetic content |
| `prop:hecke-defect-equivalences` | `proposition` | 9612 | Equivalent characterizations; \textup{(i)--(iii)} ; \textup{(iv)} |
| `prop:hecke-defect-lattice` | `proposition` | 9663 | Hecke defect vanishes for lattice VOAs |
| `prop:hecke-defect-families` | `proposition` | 9738 | Hecke defect for standard families |
| `thm:rigidity-inheritance` | `theorem` | 9858 | Rigidity inheritance |
| `thm:packet-connection-flatness` | `theorem` | 10159 | Flatness and divisor independence |
| `cor:lattice-packet-diagonal` | `corollary` | 10226 | Lattice transparency |
| `prop:gauge-criterion-scattering` | `proposition` | 10292 | Gauge criterion for scattering access |
| `rem:arithmetic-comparison-sharpening` | `remark` | 10402 | Sharpening of the arithmetic comparison conjecture |
| `prop:miura-packet-splitting` | `proposition` | 10476 | — |
| `prop:genus2-non-diagonal` | `proposition` | 10842 | Genus-$2$ sewing non-diagonality |
| `thm:genus2-non-collapse` | `theorem` | 10886 | Genus-$2$ sewing--Hecke non-collapse |
| `prop:leech-cusp-nonvanishing` | `proposition` | 11018 | Lattice cusp-form non-vanishing at genus~$2$ |
| `thm:bocherer-bridge` | `theorem` | 11050 | B\"ocherer bridge |
| `rem:genus2-definitive-scope` | `remark` | 11175 | Definitive scope of genus-$2$ arithmetic access |
| `rem:leech-all-sk` | `remark` | 11230 | Leech: all genus-$2$ cusp forms are Saito--Kurokawa lifts |
| `thm:leech-chi12-projection` | `theorem` | 11251 | Leech $\chi_{12}$-projection and Waldspurger consequence |
| `prop:prime-locality-proved-cases` | `proposition` | 11467 | Settled cases |
| `thm:prime-locality-obstructions` | `theorem` | 11508 | Precise obstructions to prime-locality; {} where indicated |
| `thm:riccati-determinacy-assessment` | `theorem` | 11710 | Riccati determinacy |
| `prop:shadow-not-selberg` | `proposition` | 11753 | The shadow zeta is not in the Selberg class |

#### `chapters/connections/bv_brst.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:log-form-ghost-law` | `theorem` | 349 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 454 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 605 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `thm:bar-semi-infinite-km` | `theorem` | 710 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 823 | Anomaly duality for Kac--Moody pairs |
| `cor:anomaly-duality-w` | `corollary` | 986 | Curvature complementarity for principal \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |
| `thm:heisenberg-bv-bar-all-genera` | `theorem` | 1204 | BV $=$ bar for the Heisenberg at all genera |
| `prop:chain-level-three-obstructions` | `proposition` | 1450 | Three chain-level obstructions |

#### `chapters/connections/casimir_divisor_core_transport.tex` (27)

| Label | Env | Line | Title |
|---|---|---:|---|
| `__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:66` | `proposition` | 66 | Universal property |
| `thm:divisor-core-calculus` | `theorem` | 109 | Divisor-core calculus |
| `__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:190` | `corollary` | 190 | Divisors classify submodules |
| `thm:hom-equals-gcd` | `theorem` | 212 | Hom \(=\) gcd |
| `thm:factorization-through-common-core` | `theorem` | 274 | Universal factorization through the maximal common core |
| `cor:spectral-defects` | `corollary` | 311 | Spectral defects |
| `thm:primary-jordan-filtration` | `theorem` | 350 | Primary Jordan filtration |
| `__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:387` | `corollary` | 387 | Repeated roots are extension data |
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
| `__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:1111` | `corollary` | 1111 | Corrected transport principle |
| `prop:squarefree-common-sector` | `proposition` | 1121 | Squarefree common-sector rigidity |
| `prop:sl3-w3-defect` | `proposition` | 1203 | Exact defect decomposition for \(\widehat{\mathfrak{sl}}_3/W_3\) |
| `__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:1225` | `corollary` | 1225 | All transport maps factor through the quadratic core |
| `prop:explicit-sl3-projectors` | `proposition` | 1244 | Explicit coprime-locus projectors |
| `__unlabeled_chapters/connections/casimir_divisor_core_transport.tex:1328` | `proposition` | 1328 | The \(L_1\)--\(L_2\) package on the one-channel squarefree locus |

#### `chapters/connections/concordance.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 425 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 439 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | 730 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 754 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 791 | Gaussian collapse for abelian input |
| `prop:five-theorems-mc-projections` | `proposition` | 2223 | Five main theorems as MC projections |
| `thm:operadic-complexity-concordance` | `theorem` | 2390 | Operadic complexity |
| `conj:pixton-from-shadows` | `theorem` | 3759 | Pixton ideal from shadow obstruction tower |
| `prop:vol2-relative-holographic-bridge` | `proposition` | 4215 | Relative holographic deformation bridge |
| `prop:vol2-ribbon-thooft-bridge` | `proposition` | 4236 | Ribbon/'t~Hooft bridge |
| `thm:lagrangian-complementarity` | `theorem` | 4577 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 4856 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 5207 | Discriminant as spectral determinant, verified cases |
| `thm:discriminant-spectral` | `theorem` | 5252 | Spectral discriminant, general case |
| `comp:spectral-discriminants-standard` | `computation` | 5478 | Spectral discriminants of standard families |
| `thm:family-index` | `theorem` | 5543 | Family index theorem for genus expansions |
| `rem:programme-vi-verification` | `remark` | 6817 | Programme VI: systematic verification of (H1)--(H4) |
| `rem:four-test-interface` | `remark` | 7003 | The four-test interface |
| `prop:descent-fan` | `proposition` | 8943 | Descent fan structure |

#### `chapters/connections/dg_shifted_factorization_bridge.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-additive-kz` | `theorem` | 144 | Derived additive KZ connection |
| `__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:200` | `corollary` | 200 | Derived Drinfeld--Kohno shadow |
| `thm:boundary-residue` | `theorem` | 210 | Boundary residue theorem |
| `thm:transfer-flat-spectral` | `theorem` | 252 | Transfer of flat spectral connections |
| `thm:quasi-factorization` | `theorem` | 319 | Quasi-factorization theorem |
| `thm:strictification-spectral-cohomology` | `theorem` | 378 | Strictification by spectral cohomology |
| `__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:423` | `proposition` | 423 | Quadratic hexagon obstruction |
| `__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:452` | `proposition` | 452 | Three-particle obstruction identity |
| `thm:abelian-strictification` | `theorem` | 490 | Abelian strictification theorem |
| `thm:residue-bounded-completion` | `theorem` | 510 | Residue-bounded completion theorem |
| `prop:cartan-shift-cocycle` | `proposition` | 563 | Cartan shift cocycle identities |
| `thm:cartan-gauge-twist` | `theorem` | 581 | Cartan gauge-twist theorem |
| `thm:cartan-diagonal-defect-exact` | `theorem` | 624 | Cartan-diagonal shift defect is exact |
| `thm:triangle-localization` | `theorem` | 696 | Triangle localization formula |
| `thm:adjacent-root-rigidity` | `theorem` | 758 | Adjacent-root rigidity |
| `__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:777` | `corollary` | 777 | Normalized rational triangle coefficient |
| `prop:triangle-shift-transport` | `proposition` | 822 | Triangle shift transport law |
| `lem:free-closed-generating-kernel` | `lemma` | 873 | Closed generating kernel |
| `thm:exact-free-transport` | `theorem` | 903 | Exact free two-body transport |
| `lem:class3-ordered-bch` | `lemma` | 977 | Class-$3$ ordered BCH coefficient |
| `thm:quadrilateral-localization` | `theorem` | 1012 | Quadrilateral localization formula |
| `thm:quadrilateral-rigidity` | `theorem` | 1104 | Quadrilateral rigidity |
| `cor:quadrilateral-normalized-rational` | `corollary` | 1132 | Normalized rational quadrilateral coefficient |
| `prop:quadrilateral-shift-transport` | `proposition` | 1168 | Quadrilateral shift transport law |
| `cor:no-new-filtration3-shift-obstruction` | `corollary` | 1198 | No new independent shift obstruction in filtration $3$ |
| `__unlabeled_chapters/connections/dg_shifted_factorization_bridge.tex:1233` | `theorem` | 1233 | Conditional strictification criterion |

#### `chapters/connections/editorial_constitution.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-pbw` | `theorem` | 194 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 220 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, resolved)} |
| `prop:en-n2-recovery` | `proposition` | 1652 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1798 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1856 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1890 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1906 | Physical anomaly cancellation for affine Kac--Moody algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2139 | Hodge symmetry from complementarity |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 2459 | Volume~I concrete modular datum |

#### `chapters/connections/entanglement_modular_koszul.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ent-scalar-entropy` | `theorem` | 160 | Entanglement entropy at the scalar level |
| `thm:entanglement-complementarity` | `theorem` | 234 | Entanglement complementarity |
| `prop:ent-complexity-classification` | `proposition` | 353 | Entanglement complexity classification |
| `cor:ent-full-entropy` | `corollary` | 451 | Full entanglement entropy |
| `thm:ent-landscape-census` | `theorem` | 568 | Standard landscape entanglement census |
| `thm:ent-btz-entropy` | `theorem` | 711 | BTZ entropy from the modular characteristic |
| `prop:ent-btz-complementarity` | `proposition` | 838 | BTZ complementarity |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 123 | Bar complex = path integral for the free boson |

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
| `thm:mk-tree-level` | `theorem` | 911 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 943 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (54)

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
| `thm:yangian-shadow-theorem` | `theorem` | 1400 | Yangian-shadow theorem |
| `thm:sphere-reconstruction` | `theorem` | 1457 | Sphere flatness and reconstruction on established comparison surfaces |
| `thm:gz26-commuting-differentials` | `theorem` | 1525 | GZ26 commuting differentials from the MC element |
| `thm:gaudin-yangian-identification` | `theorem` | 1631 | Gaudin--Yangian identification |
| `thm:yangian-sklyanin-quantization` | `theorem` | 1673 | Three-parameter identification of $\hbar$; {} on the new three-parameter identification; classical Sklyanin/Drinfeld content is |
| `thm:shadow-depth-operator-order` | `theorem` | 1726 | OPE pole order trichotomy for GZ\textup{26} Hamiltonians |
| `thm:kz-classical-quantum-bridge` | `theorem` | 1780 | Classical-to-quantum bridge: proved algebraic content |
| `thm:quartic-resonance-obstruction` | `theorem` | 1823 | Quartic resonance obstruction |
| `thm:collision-residue-twisting` | `theorem` | 2246 | Collision residue = universal twisting morphism |
| `thm:collision-depth-2-ybe` | `theorem` | 2302 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `thm:shadow-connection-kz` | `theorem` | 2340 | Shadow/KZ comparison on the affine Kac--Moody surface |
| `cor:shadow-connection-heisenberg` | `corollary` | 2384 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | 2405 | Shadow connection for Virasoro and BPZ on the degenerate-representation surface |
| `thm:quartic-obstruction-linf` | `theorem` | 2441 | Quartic obstruction = $L_\infty$ obstruction |
| `comp:holographic-ss-sl2` | `computation` | 2525 | The $E_1$ page for $\widehat{\mathfrak{sl}}_2$ |
| `comp:holographic-ss-vir` | `computation` | 2577 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | 2621 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | 2644 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | 2725 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | 2748 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | 2788 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | 2879 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | 2935 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | 3030 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | 3064 | Holographic datum for $\mathcal W_3$ |
| `thm:ds-central-charge-additivity` | `theorem` | 3188 | Central charge additivity under DS |
| `cor:critical-dimensions` | `corollary` | 3289 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | 3400 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | 3424 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | 3460 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | 3485 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | 3597 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | 3732 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | 3907 | Transport propagation lemma |
| `prop:lifts-as-relative-mc` | `proposition` | 4031 | Lifts as relative MC elements |
| `cor:holographic-deformation-cohomology` | `corollary` | 4062 | — |
| `prop:frontier-celestial-ope` | `proposition` | 4375 | Celestial OPE from the bar complex |
| `prop:frontier-sw-shadow` | `proposition` | 4453 | Shadow connection and Picard--Fuchs |
| `prop:frontier-cs-shadow` | `proposition` | 4520 | Chern--Simons from the shadow obstruction tower |
| `thm:frontier-twisted-holography` | `theorem` | 4629 | Twisted holography datum |
| `thm:frontier-abjm` | `theorem` | 4713 | ABJM holographic datum |
| `thm:frontier-m5` | `theorem` | 4851 | M5 brane holographic datum |
| `comp:burns-space-holographic-datum` | `computation` | 5034 | Burns space holographic modular Koszul datum |

#### `chapters/connections/genus1_seven_faces.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:g1sf-elliptic-regularization` | `theorem` | 137 | Elliptic regularization of the collision residue |
| `thm:g1sf-face-1` | `theorem` | 227 | Face~1 at genus~$1$: elliptic twisting morphism |
| `thm:g1sf-face-4` | `theorem` | 293 | Face~4 at genus~$1$: KZB connection |
| `thm:g1sf-face-5` | `theorem` | 418 | Face~5 at genus~$1$: elliptic $r$-matrix; {} \textup{(}identification with collision residue\textup{)}; {} \textup{(}classical elliptic $r$-matrix: Belavin 1981, Belavin--Drinfeld 1982\textup{)} |
| `thm:g1sf-face-7` | `theorem` | 527 | Face~7 at genus~$1$: elliptic Gaudin Hamiltonians |
| `thm:g1sf-virasoro` | `theorem` | 631 | Virasoro genus-$1$ collision residue |
| `thm:g1sf-wn` | `theorem` | 698 | $\cW_N$ genus-$1$ collision residue |
| `thm:g1sf-master` | `theorem` | 775 | Genus-$1$ seven-face identification for affine Kac--Moody |
| `thm:g1sf-degeneration` | `theorem` | 884 | Degeneration to genus~$0$ |
| `thm:g1sf-b-cycle-monodromy` | `theorem` | 1019 | $B$-cycle monodromy of the collision residue |

#### `chapters/connections/genus_complete.tex` (28)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 236 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 292 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 374 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 657 | Bar complex computes moduli integrals |
| `thm:full-modular-invariant-hierarchy` | `theorem` | 1216 | The full modular invariant hierarchy |
| `prop:sewing-universal-property` | `proposition` | 1338 | Universal property of the sewing envelope |
| `prop:hs-trace-class` | `proposition` | 1377 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | 1392 | General HS-sewing criterion |
| `cor:hs-sewing-standard-landscape` | `corollary` | 1424 | Standard landscape |
| `cor:hs-implies-gram` | `corollary` | 1462 | — |
| `thm:heisenberg-one-particle-sewing` | `theorem` | 1481 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | 1558 | Positive grading implies conilpotency |
| `prop:dirichlet-weight-formula` | `theorem` | 1861 | — |
| `cor:virasoro-mode-removal` | `corollary` | 1919 | — |
| `prop:euler-koszul-criterion` | `theorem` | 1978 | — |
| `comp:euler-koszul-defect-table` | `computation` | 2015 | Euler--Koszul defect table for the standard landscape |
| `prop:zeta-zeros-defect-derivative` | `proposition` | 2107 | — |
| `thm:li-closed-form` | `theorem` | 2145 | — |
| `prop:li-asymptotics` | `theorem` | 2178 | — |
| `prop:surface-moment-positivity` | `theorem` | 2306 | Gram positivity |
| `cor:virasoro-gram-ratio` | `corollary` | 2329 | — |
| `thm:sewing-rkhs` | `theorem` | 2364 | Sewing RKHS |
| `prop:collapse-permanence` | `proposition` | 2431 | Collapse permanence |
| `rem:benjamin-chang-bridge` | `proposition` | 2470 | — |
| `thm:shadow-euler-independence` | `theorem` | 2496 | — |
| `rem:two-faces-theta` | `corollary` | 2553 | — |
| `thm:euler-koszul-tier-classification` | `theorem` | 2635 | — |
| `thm:sewing-hecke-reciprocity` | `theorem` | 2716 | Sewing--Hecke reciprocity |

#### `chapters/connections/holographic_codes_koszul.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:hc-knill-laflamme` | `proposition` | 93 | Knill--Laflamme from Lagrangian isotropy |
| `thm:hc-symplectic-code` | `theorem` | 221 | Symplectic code structure |
| `thm:hc-koszulness-exact-qec` | `theorem` | 341 | \textbf{G12}: Koszulness $\Leftrightarrow$ exact holographic reconstruction |
| `thm:hc-shadow-redundancy` | `theorem` | 459 | Shadow depth controls redundancy |
| `thm:hc-dictionary` | `proposition` | 560 | 12-fold dictionary |
| `thm:hc-census` | `theorem` | 712 | Standard landscape code census |

#### `chapters/connections/holographic_datum_master.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:seven-faces-master` | `theorem` | 71 | Seven-face master theorem |
| `thm:hdm-face-1` | `theorem` | 137 | Face~1: bar-cobar twisting |
| `thm:hdm-face-2` | `theorem` | 194 | Face~2: DNP line operators |
| `thm:hdm-face-3` | `theorem` | 258 | Face~3: Khan--Zeng PVA |
| `thm:hdm-face-4` | `theorem` | 323 | Face~4: GZ26 commuting Hamiltonians |
| `thm:hdm-face-5` | `theorem` | 401 | Face~5: Drinfeld $r$-matrix; \ (identification with collision residue); \ (classical $r$-matrix theory: Drinfeld 1985) |
| `thm:hdm-face-6` | `theorem` | 474 | Face~6: Sklyanin bracket; \ (identification with classical limit of collision residue); \ (Sklyanin bracket: Semenov-Tian-Shansky 1983) |
| `thm:hdm-face-7` | `theorem` | 544 | Face~7: Gaudin Hamiltonians |
| `thm:hdm-seven-way-master` | `theorem` | 615 | Seven-way master theorem |
| `thm:hdm-higher-gaudin` | `theorem` | 744 | Higher Gaudin Hamiltonians |

#### `chapters/connections/holomorphic_topological.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:ht-bar-genus-zero` | `proposition` | 110 | Bar complex and genus-zero HT data |
| `thm:ht-mc-all-genera` | `theorem` | 142 | MC element and all-genus HT partition function |
| `cor:ht-shadow-archetype` | `corollary` | 173 | Shadow archetype classification |
| `prop:ht-five-shadow-synthesis` | `proposition` | 231 | Five-shadow synthesis |
| `prop:ht-four-recovery` | `proposition` | 273 | Four recovery theorems |
| `prop:witten-diagram-shadow-projection` | `proposition` | 819 | Witten diagrams as genus-$0$ shadow projections |

#### `chapters/connections/kontsevich_integral.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-weight-systems` | `theorem` | 108 | Bar complex weight systems |
| `prop:propagator-restriction` | `proposition` | 177 | Propagator restriction |
| `prop:kz-from-bar` | `proposition` | 266 | KZ connection from bar complex |
| `thm:drinfeld-associator-bar` | `theorem` | 314 | Drinfeld associator from bar-cobar |
| `prop:feynman-graph-complex` | `proposition` | 414 | Feynman transform and algebraic graph-complex refinement |

#### `chapters/connections/master_concordance.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-seven-face` | `theorem` | 38 | Seven-face identification; \ for faces $1$--$4$, $7$; \ for faces $5$--$6$ on Drinfeld $1985$ and Semenov-Tian-Shansky $1983$ |

#### `chapters/connections/outlook.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:operadic-complexity` | `theorem` | 245 | Operadic complexity |

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

#### `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex` (22)

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

#### `chapters/connections/subregular_hook_frontier.tex` (17)

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
| `comp:bp-kappa-three-paths` | `computation` | 905 | Modular characteristic of $\mathrm{BP}_k$ |
| `prop:bp-complementarity-constant` | `proposition` | 956 | Complementarity constant for $\mathrm{BP}_k$ |
| `thm:bp-koszul-self-dual` | `theorem` | 1001 | Bershadsky--Polyakov Koszul self-duality |
| `thm:w4-cubic` | `theorem` | 1111 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} has canonical arity $3$ |
| `thm:unbounded-canonical-arity` | `theorem` | 1242 | Unbounded canonical arity in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | 1296 | Triangular primary-renormalization theorem |
| `prop:nilpotent-transport-typeA` | `proposition` | 1521 | Nilpotent transport for type $A$ |

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
| `prop:shadow-critical` | `proposition` | 1426 | Shadow obstruction tower at critical central charges |
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
| `thm:thqg-entanglement-wedge` | `theorem` | 654 | Subregion structure from the open/closed realization |
| `thm:thqg-page-constraint` | `theorem` | 695 | Algebraic Page constraint |

#### `chapters/connections/thqg_fredholm_partition_functions.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-X-sewing-filtration` | `proposition` | 195 | Sewing envelope: conformal weight filtration |
| `lem:thqg-X-sewing-schatten` | `lemma` | 333 | Schatten class properties of $\sewop_q$ |
| `lem:thqg-X-composition-decay` | `lemma` | 447 | Exponential decay of composition coefficients |
| `prop:thqg-X-second-quantization` | `proposition` | 485 | Second quantization |
| `thm:thqg-X-heisenberg-sewing-full` | `theorem` | 565 | Heisenberg sewing theorem: full development |
| `prop:polyakov-alvarez-shadow-specialization` | `proposition` | 869 | Polyakov--Alvarez as shadow metric specialization |
| `thm:thqg-X-genus-1-fredholm` | `theorem` | 948 | Genus-1 Fredholm determinant |
| `comp:thqg-X-genus-1-series` | `computation` | 1051 | Genus-1 Fredholm determinant: explicit series |
| `thm:thqg-X-genus-2-fredholm` | `theorem` | 1096 | Genus-2 Fredholm determinant |
| `comp:thqg-X-genus-2-series` | `computation` | 1204 | Genus-2 Fredholm determinant: leading terms |
| `thm:thqg-X-genus-3-fredholm` | `theorem` | 1231 | Genus-3 Fredholm determinant |
| `thm:thqg-X-general-genus-fredholm` | `theorem` | 1351 | General-genus Fredholm structure |
| `prop:thqg-X-free-energy-ahat` | `proposition` | 1425 | Free energy: $\hat{A}$-genus verification |
| `thm:thqg-X-class-G-fredholm` | `theorem` | 1501 | Fredholm scalar partition function on the Gaussian scalar lane |
| `prop:thqg-X-rank-additivity` | `proposition` | 1594 | Rank additivity |
| `thm:thqg-X-feynman-expansion` | `theorem` | 1661 | Feynman integral expansion |
| `prop:thqg-X-class-L-feynman` | `proposition` | 1724 | Class-L Feynman integrals |
| `prop:thqg-X-class-C-quartic` | `proposition` | 1818 | Class-C quartic contact |
| `prop:thqg-X-virasoro-decomposition` | `proposition` | 1902 | Virasoro: Fredholm base + corrections |
| `prop:thqg-X-analytic-bar-bounded` | `proposition` | 1999 | Analytic bar differential is bounded |
| `prop:thqg-X-analytic-coproduct` | `proposition` | 2027 | Analytic coproduct |
| `prop:thqg-X-coderived-fredholm-G` | `proposition` | 2107 | Coderived = Fredholm for class~G |
| `prop:givental-vertex-reconstruction` | `proposition` | 2377 | Givental reconstruction of higher-genus vertex factors |
| `thm:gravitational-complementarity-genus-expansion` | `theorem` | 2497 | Gravitational complementarity genus expansion |
| `prop:virasoro-F2-full` | `proposition` | 2612 | Full genus-$2$ free energy for Virasoro |
| `prop:cohft-complementarity` | `proposition` | 2663 | CohFT complementarity |

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
| `thm:thqg-virasoro-infinite` | `theorem` | 661 | Virasoro shadow obstruction tower is infinite |
| `thm:thqg-virasoro-tower-explicit` | `theorem` | 704 | Virasoro shadow obstruction tower through septic order |
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
| `prop:thqg-wn-stabilization` | `proposition` | 1331 | $\mathcal{W}_N$ complexity stabilises |
| `thm:thqg-grav-landscape` | `theorem` | 1360 | Gravitational complexity census |
| `thm:thqg-g2-main` | `maintheorem` | 1408 | Shadow-depth classification; result (G2) |
| `prop:thqg-complexity-functor` | `proposition` | 1456 | Functoriality of complexity |
| `prop:thqg-coefficient-asymptotics` | `proposition` | 1531 | Coefficient asymptotics |
| `prop:thqg-generic-constancy` | `proposition` | 1600 | Generic constancy |
| `thm:thqg-mc-euler-lagrange` | `theorem` | 1655 | Primary-line MC critical-point equation |
| `thm:thqg-holographic-ss` | `theorem` | 1753 | Collision-filtration spectral sequence |
| `prop:thqg-collapse-criteria` | `proposition` | 1787 | Collapse criteria by complexity class |
| `prop:thqg-e1-virasoro` | `proposition` | 1844 | $E_1$ page for Virasoro |
| `prop:thqg-collapse-L` | `proposition` | 1891 | Collapse for class~$\mathbf{L}$ |
| `prop:thqg-collapse-C` | `proposition` | 1915 | Collapse for class~$\mathbf{C}$ |
| `prop:thqg-curve-independence` | `proposition` | 1960 | Curve independence |

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
| `thm:thqg-IV-kz-duality` | `theorem` | 757 | Shadow/KZ duality on the affine comparison surface |
| `prop:thqg-IV-bpz-duality` | `proposition` | 795 | BPZ duality from $S$-duality |
| `prop:shadow-connection-s-duality` | `proposition` | 847 | Shadow connection $S$-duality |
| `thm:thqg-IV-local-system-duality` | `theorem` | 918 | Local system duality |
| `prop:thqg-IV-monodromy-duality` | `proposition` | 952 | Monodromy eigenvalue reciprocation |
| `prop:thqg-IV-heisenberg-K` | `proposition` | 1032 | Heisenberg complementarity |
| `thm:thqg-IV-km-K` | `theorem` | 1060 | Affine Kac--Moody complementarity |
| `prop:thqg-IV-bc-bg-K` | `proposition` | 1139 | \texorpdfstring{$bc$--$\beta\gamma$}{bc-betagamma} complementarity |
| `prop:thqg-IV-lattice-K` | `proposition` | 1173 | Lattice complementarity |
| `thm:thqg-IV-virasoro-K` | `theorem` | 1190 | Virasoro complementarity |
| `thm:thqg-IV-w-K` | `theorem` | 1240 | Principal $\mathcal{W}$-algebra complementarity |
| `prop:thqg-IV-conductor-growth` | `proposition` | 1314 | Koszul conductor asymptotics |
| `thm:thqg-IV-exponent-sum` | `theorem` | 1333 | Exponent sum formula |
| `thm:ds-complementarity-tower` | `theorem` | 1458 | DS complementarity tower |
| `cor:level-independence-filtration` | `corollary` | 1589 | Level-independence filtration |
| `thm:sigma-ring-finite-generation` | `theorem` | 1651 | Recursive determination of $(\cA^{\mathrm{sh}})^\sigma$ |
| `thm:thqg-IV-c26` | `theorem` | 1713 | The $c = 26$ degeneration |
| `prop:thqg-IV-c13` | `proposition` | 1772 | The $c = 13$ chiral Koszul self-dual point |
| `thm:thqg-IV-critical-degeneration` | `theorem` | 1824 | Critical-level degeneration |
| `prop:thqg-IV-self-dual-classification` | `proposition` | 1882 | Classification of self-dual points |
| `thm:thqg-IV-four-facets` | `theorem` | 1954 | Four-facet decomposition |
| `thm:thqg-IV-free-energy` | `theorem` | 2024 | Scalar free-energy complementarity |
| `cor:thqg-IV-self-dual-generating` | `corollary` | 2066 | Self-dual scalar free energies |
| `prop:thqg-IV-partition-duality` | `proposition` | 2081 | Partition function functional equation |
| `prop:thqg-IV-holographic-datum` | `proposition` | 2170 | Holographic modular Koszul datum under $S$-duality |
| `prop:thqg-IV-naturality` | `proposition` | 2239 | Naturality of $\mathcal{S}$ |
| `prop:thqg-IV-clutching` | `proposition` | 2256 | Clutching compatibility |
| `prop:thqg-IV-spectral-duality` | `proposition` | 2348 | Spectral sequence duality |
| `cor:thqg-IV-e2-duality` | `corollary` | 2367 | $E_2$ duality |
| `cor:thqg-IV-degeneration` | `corollary` | 2374 | Degeneration preservation |
| `thm:thqg-IV-cc-sum` | `theorem` | 2447 | Central charge sum |

#### `chapters/connections/thqg_gravitational_yangian.tex` (30)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-V-collision-lie-compatibility` | `lemma` | 170 | Lie compatibility of the collision filtration |
| `prop:thqg-V-depth-zero` | `proposition` | 216 | Associated graded at depth zero |
| `prop:thqg-V-depth-one` | `proposition` | 254 | Associated graded at depth one |
| `prop:thqg-V-collapse-criterion` | `proposition` | 319 | Collapse criterion from shadow depth |
| `lem:thqg-V-collision-nilpotent` | `lemma` | 392 | Nilpotency of the collision differential |
| `prop:thqg-V-arnold-cohomology` | `proposition` | 415 | Arnold cohomology and collision forms |
| `prop:thqg-V-poincare-collision` | `proposition` | 484 | Poincar\'e polynomial of the collision filtration |
| `thm:thqg-V-collision-twisting` | `theorem` | 579 | Collision residue = twisting morphism, revisited |
| `comp:thqg-V-heisenberg-r` | `computation` | 645 | Heisenberg $r$-matrix |
| `comp:thqg-V-affine-r` | `computation` | 703 | Affine Kac--Moody $r$-matrix |
| `comp:thqg-V-virasoro-r` | `computation` | 759 | Virasoro $r$-matrix |
| `prop:thqg-V-gravitational-propagator` | `proposition` | 884 | Gravitational propagator from collision residue |
| `thm:thqg-V-cybe-from-arnold` | `theorem` | 1028 | CYBE from the Arnold relation via MC |
| `cor:thqg-V-ibr` | `corollary` | 1155 | Infinitesimal braid relation |
| `prop:thqg-V-ainfty-ybe` | `proposition` | 1199 | $A_\infty$-enhancement of the CYBE |
| `prop:thqg-V-n-point-ybe-proof` | `proposition` | 1276 | $n$-point YBE from boundary of $\overline{\mathcal{M}}_{0,n+1}$ |
| `prop:thqg-V-yangian-differential` | `proposition` | 1398 | Differential structure |
| `thm:thqg-V-pro-mc-element` | `theorem` | 1441 | Formal genus-refined binary shadow series $R^{\mathrm{bin}}_\cA$ |
| `cor:thqg-V-genus-zero-r` | `corollary` | 1471 | Genus-$0$ component = classical $r$-matrix |
| `prop:thqg-V-pro-mc-convergence` | `proposition` | 1569 | Formal \texorpdfstring{$\hbar$}{hbar}-adic convergence of the candidate binary shadow series |
| `prop:thqg-V-rtt-from-sgybe` | `proposition` | 1642 | RTT relation from the genus-zero collision YBE |
| `comp:thqg-V-three-graviton` | `computation` | 1802 | Three-graviton vertex |
| `comp:thqg-V-quartic-graviton` | `computation` | 1843 | Quartic graviton vertex and contact invariant |
| `prop:thqg-V-verma-gravitational` | `proposition` | 1903 | Verma modules as gravitational representations |
| `prop:thqg-V-c13-self-duality` | `proposition` | 1975 | Self-duality of the gravitational Yangian at $c = 13$ |
| `thm:thqg-V-mc3-thick-generation` | `theorem` | 2108 | Type-$A$ MC3 reduction via the gravitational Yangian |
| `cor:thqg-V-dk5-type-a` | `corollary` | 2147 | Type-$A$ DK-5 reduction to the compact-completion packet |
| `comp:thqg-V-heis-yangian` | `computation` | 2311 | Gravitational Yangian of Heisenberg |
| `comp:thqg-V-affine-yangian` | `computation` | 2331 | Gravitational Yangian of affine KM |
| `comp:thqg-V-vir-yangian-summary` | `computation` | 2353 | Gravitational Yangian of $\mathrm{Vir}_c$ |

#### `chapters/connections/thqg_holographic_reconstruction.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:obstruction-extension-sequence` | `proposition` | 133 | Obstruction-extension sequence |
| `thm:shadow-depth-dichotomy` | `theorem` | 205 | Shadow depth dichotomy |
| `cor:mittag-leffler-shadow-tower` | `corollary` | 311 | Mittag--Leffler for the shadow obstruction tower |
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
| `prop:shapovalov-shadow-singularities` | `proposition` | 1864 | Shapovalov singularities of the shadow obstruction tower |
| `prop:pole-structure-shadow-series` | `proposition` | 1909 | Pole structure of the full shadow series |
| `comp:shapovalov-zeros-shadow` | `computation` | 1964 | Shapovalov zeros and shadow singularities |
| `thm:complexity-hierarchy` | `theorem` | 2046 | Complexity hierarchy |

#### `chapters/connections/thqg_introduction_supplement_body.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `conj:thqg-intro-operadic-complexity` | `theorem` | 860 | Operadic complexity; ; Theorem~\ref{thm:operadic-complexity} |

#### `chapters/connections/thqg_modular_bootstrap.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-VII-genus-g-mc` | `proposition` | 279 | Genus-$g$ MC equation |
| `prop:thqg-VII-genus0` | `proposition` | 450 | Genus-$0$ MC equation |
| `prop:thqg-VII-genus1` | `proposition` | 472 | Genus-$1$ MC equation |
| `prop:thqg-VII-genus2` | `proposition` | 503 | Genus-$2$ MC equation |
| `prop:thqg-VII-genus3` | `proposition` | 548 | Genus-$3$ MC equation |
| `prop:thqg-VII-genus4` | `proposition` | 579 | Genus-$4$ MC equation |
| `thm:thqg-VII-contracting-homotopy` | `theorem` | 743 | Contracting homotopy |
| `thm:thqg-VII-uniqueness` | `theorem` | 889 | Uniqueness up to gauge |
| `prop:thqg-VII-genus1-solution` | `proposition` | 934 | Genus-$1$ solution |
| `comp:thqg-VII-genus2` | `computation` | 984 | Genus-$2$ MC recursion |
| `thm:thqg-VII-genus-ss` | `theorem` | 1117 | Genus spectral sequence for the bootstrap |
| `prop:thqg-VII-E1-koszul` | `proposition` | 1230 | $E_1$~page for a Koszul algebra |
| `thm:thqg-VII-ss-convergence` | `theorem` | 1283 | Convergence of the genus spectral sequence |
| `cor:thqg-VII-gaussian-degeneration` | `corollary` | 1318 | Degeneration for Gaussian algebras |
| `prop:thqg-VII-mixed-nondegeneration` | `proposition` | 1352 | Non-degeneration for mixed-type algebras |
| `thm:thqg-VII-ss-shadow-obstruction` | `theorem` | 1387 | Spectral sequence differentials as shadow obstructions |
| `thm:thqg-VII-mc-vs-bootstrap` | `theorem` | 1476 | MC recursion vs.\ conformal bootstrap |
| `thm:thqg-VII-crossing-from-mc` | `theorem` | 1543 | Crossing symmetry from the MC equation |
| `cor:thqg-VII-genus-g-bootstrap` | `corollary` | 1607 | Genus-$g$ bootstrap from MC |
| `prop:thqg-VII-bootstrap-gap` | `proposition` | 1688 | The bootstrap gap |
| `comp:thqg-VII-heis-g0` | `computation` | 1788 | Genus-$0$ Heisenberg |
| `comp:thqg-VII-heis-g1` | `computation` | 1819 | Genus-$1$ Heisenberg |
| `comp:thqg-VII-heis-g2` | `computation` | 1867 | Genus-$2$ Heisenberg |
| `comp:thqg-VII-heis-g3` | `computation` | 1964 | Genus-$3$ Heisenberg |
| `comp:thqg-VII-heis-g4` | `computation` | 2037 | Genus-$4$ Heisenberg |
| `thm:thqg-VII-recursion-closed` | `theorem` | 2161 | Recursion reproduces the closed form |
| `cor:thqg-VII-rank-d` | `corollary` | 2237 | Rank-$d$ Heisenberg |
| `thm:thqg-VII-one-loop-gravity` | `theorem` | 2495 | Genus-\texorpdfstring{$1$}{1} scalar term from \texorpdfstring{$\Theta^{(1)}$}{Theta(1)} |
| `thm:thqg-VII-g-loop-amplitude` | `theorem` | 2537 | Integrated genus-\texorpdfstring{$g$}{g} MC functional |
| `thm:thqg-VII-non-renormalization` | `theorem` | 2589 | Scalar genus expansion for Gaussian algebras |
| `prop:thqg-VII-complexity-bounds` | `proposition` | 2668 | Complexity bounds on genus-\texorpdfstring{$g$}{g} integrand classes |
| `thm:thqg-VII-depth-classification` | `theorem` | 2771 | Shadow depth classifies gravitational theories |

#### `chapters/connections/thqg_open_closed_realization.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-brace-dg-algebra` | `theorem` | 172 | Brace dg algebra structure on chiral Hochschild cochains |
| `thm:thqg-swiss-cheese` | `theorem` | 325 | Universal open/closed pair (chiral Swiss-cheese theorem) |
| `prop:mixed-sector-bulk-boundary` | `proposition` | 408 | Mixed sector encodes bulk-to-boundary module structure |
| `thm:thqg-local-global-bridge` | `theorem` | 458 | Local-global bridge |
| `thm:thqg-annulus-trace` | `theorem` | 559 | Annulus trace theorem |
| `prop:thqg-annulus-degeneration-kappa` | `proposition` | 830 | Annulus degeneration and the genus-$1$ curvature |
| `thm:thqg-oc-mc-equation` | `theorem` | 905 | Open/closed MC equation |
| `thm:thqg-oc-projection` | `theorem` | 966 | Open/closed projection principle |
| `thm:thqg-mc-forced-consistency` | `theorem` | 1025 | MC-forced open-closed consistency |
| `thm:thqg-oc-quartic-vanishing` | `theorem` | 1181 | Vanishing and nonvanishing of $\mathfrak{R}^{\mathrm{oc}}_{4}$ |

#### `chapters/connections/thqg_perturbative_finiteness.tex` (36)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-I-completeness` | `lemma` | 80 | Completeness and separability |
| `prop:thqg-I-inclusion-maps` | `proposition` | 90 | Inclusion maps |
| `lem:thqg-I-schatten` | `lemma` | 131 | Schatten class hierarchy |
| `prop:thqg-I-uniform-trace-bound` | `proposition` | 371 | Uniform bound on the trace |
| `cor:thqg-I-genus-g-partition` | `corollary` | 385 | Genus-$g$ partition function |
| `thm:thqg-I-absolute-convergence` | `theorem` | 588 | Absolute convergence of the scalar generating function on the scalar lane |
| `prop:thqg-I-Fg-values` | `proposition` | 643 | Shadow free energies through genus $10$ on the scalar lane |
| `prop:thqg-I-partial-sums` | `proposition` | 713 | Cumulative partial sums |
| `thm:thqg-I-perturbative-finiteness` | `theorem` | 779 | Perturbative finiteness of twisted gravity |
| `prop:thqg-I-koszulness-finiteness` | `proposition` | 841 | Koszulness and finiteness |
| `prop:thqg-I-graph-count` | `proposition` | 864 | Effective graph count |
| `prop:thqg-I-genus-g-decomposition` | `proposition` | 880 | Genus-$g$ amplitude decomposition |
| `prop:thqg-I-exponential-rep` | `proposition` | 1050 | Exponential representation |
| `prop:thqg-I-heisenberg-detail` | `proposition` | 1129 | Heisenberg: detailed HS verification |
| `prop:thqg-I-affine-detail` | `proposition` | 1147 | Affine Kac--Moody: detailed HS verification |
| `prop:thqg-I-virasoro-detail` | `proposition` | 1166 | Virasoro: detailed HS verification |
| `prop:thqg-I-convergence-radii` | `proposition` | 1187 | Convergence radii of the scalar partition function |
| `thm:thqg-I-btz` | `theorem` | 1313 | BTZ-normalized scalar shadow series |
| `prop:thqg-I-btz-higher-genus` | `proposition` | 1361 | Higher-genus BTZ-normalized scalar coefficients |
| `prop:thqg-I-1c-expansion` | `proposition` | 1433 | Leading gravitational coupling expansion of the reduced scalar series |
| `prop:thqg-I-newton-expansion` | `proposition` | 1467 | Newton's constant expansion |
| `prop:thqg-I-graph-sum-sewing` | `proposition` | 1611 | Graph-sum representation of sewing amplitudes |
| `prop:thqg-I-graph-sum-convergence` | `proposition` | 1631 | Convergence of the graph sum at fixed genus |
| `prop:thqg-I-consistency` | `proposition` | 1660 | Parallel analytic and algebraic finiteness |
| `thm:thqg-I-full-convergence` | `theorem` | 1709 | Full partition function at fixed genus and on the Gaussian lane |
| `prop:thqg-I-hs-filtration` | `proposition` | 1792 | HS-sewing and the strong filtration |
| `prop:thqg-I-effective-bound` | `proposition` | 1814 | Effective bound on the genus-$g$ scalar free energy on the scalar lane |
| `cor:thqg-I-tail-bound` | `corollary` | 1837 | Tail bound for the scalar genus expansion on the scalar lane |
| `thm:thqg-I-2d-convergence` | `theorem` | 1873 | Fixed-genus arity convergence and Gaussian two-parameter convergence |
| `cor:thqg-I-heisenberg-selberg` | `corollary` | 1997 | Heisenberg partition function via Selberg zeta |
| `prop:polyakov-chern-weil` | `proposition` | 2056 | Polyakov formula as Chern--Weil image of the arity-$2$ shadow |
| `prop:thqg-I-pole-structure` | `proposition` | 2110 | Pole structure of the meromorphic continuation |
| `prop:thqg-I-tensor-product` | `proposition` | 2226 | Finiteness for tensor-product theories |
| `comp:thqg-I-fp-detailed` | `computation` | 2289 | Faber--Pandharipande coefficients through genus $15$ |
| `prop:thqg-I-asymptotic-precision` | `proposition` | 2324 | Asymptotic precision |
| `prop:thqg-I-fp-monotone` | `proposition` | 2340 | Monotonicity of the FP coefficients |

#### `chapters/connections/thqg_soft_graviton_theorems.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-VI-arity-decomposition` | `proposition` | 230 | Arity decomposition of the shadow connection |
| `thm:thqg-VI-flatness-by-arity` | `theorem` | 273 | Flatness by arity |
| `thm:thqg-VI-ward-determines-correlators` | `theorem` | 434 | Shadow Ward identities determine correlators |
| `prop:thqg-VI-kappa-action` | `proposition` | 578 | Action of $\kappa$ on conformal blocks |
| `thm:thqg-VI-leading-soft` | `theorem` | 633 | Leading soft graviton theorem |
| `cor:thqg-VI-bms-supertranslation` | `corollary` | 723 | BMS supertranslation Ward identity |
| `prop:thqg-VI-cubic-action` | `proposition` | 791 | Cubic shadow action on conformal blocks |
| `thm:thqg-VI-subleading-soft` | `theorem` | 833 | Subleading soft graviton theorem |
| `thm:thqg-VI-cubic-gauge-triviality` | `theorem` | 911 | Cubic gauge triviality and subleading soft theorems |
| `cor:thqg-VI-superrotation` | `corollary` | 984 | Superrotation Ward identity |
| `prop:thqg-VI-quartic-action` | `proposition` | 1084 | Quartic shadow action on conformal blocks |
| `thm:thqg-VI-virasoro-quartic` | `theorem` | 1120 | Virasoro quartic contact coefficient |
| `thm:thqg-VI-clutching-law` | `theorem` | 1247 | Clutching law for the quartic contact invariant |
| `comp:thqg-VI-virasoro-clutching` | `computation` | 1335 | Clutching law for Virasoro |
| `thm:thqg-VI-sub-subleading-soft` | `theorem` | 1373 | Sub-subleading soft graviton theorem |
| `thm:thqg-VI-general-soft` | `theorem` | 1482 | General arity-$r$ soft graviton theorem |
| `cor:thqg-VI-soft-recursion` | `corollary` | 1531 | Soft factor recursion |
| `thm:thqg-VI-quintic-forced` | `theorem` | 1557 | The Virasoro quintic shadow is forced |
| `comp:thqg-VI-virasoro-quintic-soft` | `computation` | 1682 | Quintic soft factor for Virasoro |
| `prop:thqg-VI-inductive-nontermination` | `proposition` | 1717 | Inductive non-termination for class $\mathbf{M}$ |
| `prop:thqg-VI-polynomial-growth` | `proposition` | 1798 | Polynomial growth of soft factors |
| `cor:thqg-VI-soft-convergence` | `corollary` | 1847 | Convergence of the soft expansion |
| `prop:thqg-VI-celestial-structure` | `proposition` | 1914 | Structure of the celestial soft algebra |
| `thm:thqg-VI-soft-ope` | `theorem` | 1994 | Soft graviton OPE |
| `prop:thqg-VI-asymptotic-symmetry` | `proposition` | 2065 | Asymptotic symmetry algebra from the shadow obstruction tower |

#### `chapters/connections/thqg_symplectic_polarization.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-III-ambient-properties` | `proposition` | 126 | Properties of the holographic ambient complex |
| `prop:thqg-III-involutivity` | `proposition` | 237 | Involutivity and anti-symmetry |
| `prop:thqg-III-mc-compatibility` | `proposition` | 297 | Compatibility with the modular MC element |
| `lem:thqg-III-nondegeneracy` | `lemma` | 388 | Nondegeneracy of the holographic pairing |
| `prop:thqg-III-degree-shift` | `proposition` | 421 | Degree shift at each genus |
| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
| `cor:thqg-III-complementarity-exchange` | `corollary` | 655 | Complementarity exchange principle |
| `cor:thqg-III-dimension-parity` | `corollary` | 678 | Dimension parity |
| `prop:thqg-III-genus-0` | `proposition` | 694 | Genus-$0$ complementarity |
| `prop:thqg-III-genus-1` | `proposition` | 719 | Genus-$1$ complementarity |
| `prop:thqg-III-compatibility` | `proposition` | 1099 | Compatibility of the BV antibracket with the Verdier pairing |
| `thm:thqg-III-genus-1-holographic` | `theorem` | 1437 | Holographic complementarity at genus $1$ |
| `thm:thqg-III-landscape-census` | `theorem` | 1709 | Standard landscape complementarity census |
| `prop:thqg-III-genus-2` | `proposition` | 1883 | Genus-$2$ complementarity dimensions |
| `prop:thqg-III-independent-sum` | `proposition` | 1924 | Independent sum factorization |
| `thm:thqg-III-universality` | `theorem` | 2025 | Universality of the complementarity package |

#### `chapters/connections/twisted_holography_quantum_gravity.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-g1-finiteness` | `theorem` | 121 | \textbf{G1}: Perturbative finiteness |
| `thm:thqg-g2-complexity` | `theorem` | 132 | \textbf{G2}: Shadow-depth classification |
| `thm:thqg-g3-polarization` | `theorem` | 151 | \textbf{G3}: Symplectic polarization |
| `thm:thqg-g4-s-duality` | `theorem` | 161 | \textbf{G4}: Gravitational $S$-duality |
| `thm:thqg-g5-yangian` | `theorem` | 176 | \textbf{G5}: Gravitational Yangian |
| `thm:thqg-g6-soft-graviton` | `theorem` | 190 | \textbf{G6}: Soft graviton theorems |
| `thm:thqg-g7-bootstrap` | `theorem` | 215 | \textbf{G7}: Modular bootstrap |
| `thm:thqg-g8-reconstruction` | `theorem` | 232 | \textbf{G8}: Holographic reconstruction |
| `thm:thqg-g9-critical-string` | `theorem` | 249 | \textbf{G9}: Critical string dichotomy |
| `thm:thqg-g10-fredholm` | `theorem` | 272 | \textbf{G10}: Partition function convergence |
| `thm:thqg-g14-error-correction` | `theorem` | 325 | \textbf{G14}: Holographic code structure |
| `thm:thqg-g15-page` | `theorem` | 338 | \textbf{G15}: Algebraic Page constraint |
| `thm:thqg-dependency` | `theorem` | 362 | Dependency theorem |

#### `chapters/connections/typeA_baxter_rees_theta.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:vector-seed-propagation` | `theorem` | 146 | Propagation from the vector seed |
| `lem:equivariant-normal-form` | `lemma` | 205 | Equivariant normal form on $V\otimes V$ |
| `thm:schur-envelope-formula` | `theorem` | 244 | Schur-envelope formula |
| `cor:one-coefficient-forces-reduced-core` | `corollary` | 298 | One ordered coefficient forces the reduced core |
| `thm:pairwise-to-all-point-reconstruction` | `theorem` | 339 | Pairwise-to-all-point reconstruction |
| `prop:weight-stability-algebra-tower` | `proposition` | 432 | Weight-stability of the algebra tower |
| `prop:failure-unweighted-stabilization` | `proposition` | 461 | Failure of unweighted stabilization |
| `lem:weight-stability-bar-tower` | `lemma` | 511 | Weight-stability of the bar tower |
| `thm:weightwise-MC4-principal-RTT` | `theorem` | 546 | Weightwise MC4 for the principal RTT tower |
| `thm:recognition-completed-dg-shifted-yangian` | `theorem` | 596 | Recognition of the completed dg-shifted Yangian |
| `thm:derived-realization-ordinary-asymptotic` | `theorem` | 681 | Derived realization of ordinary asymptotic modules |
| `thm:derived-realization-negative-prefundamental` | `theorem` | 743 | Derived realization of negative prefundamentals |
| `thm:baxter-envelope-criterion` | `theorem` | 789 | Baxter-envelope criterion |
| `thm:algebraicity-baxter-rees-family` | `theorem` | 849 | Algebraicity of the Baxter--Rees family |
| `thm:generic-and-boundary-fibers` | `theorem` | 883 | Generic and boundary fibers |
| `thm:derived-realization-baxter-rees-family` | `theorem` | 924 | Derived realization of the Baxter--Rees family |
| `cor:formal-neighborhood-generated-by-KR` | `corollary` | 960 | Formal neighborhood generated by the compact KR packet |
| `thm:concrete-cocycle-representative` | `theorem` | 1002 | Concrete cocycle representative |
| `lem:weightwise-polynomial-continuation` | `lemma` | 1039 | Weightwise polynomial continuation |
| `thm:continuation-of-polynomial-R-matrices` | `theorem` | 1086 | Continuation of polynomial $R$-matrices to the boundary |
| `thm:continuation-of-theta-associators` | `theorem` | 1152 | Continuation of Theta-associators to the boundary |
| `cor:formal-braided-boundary-germ` | `corollary` | 1197 | Formal braided boundary germ |
| `thm:linearized-boundary-equations` | `theorem` | 1244 | Linearized boundary equations |
| `thm:compact-to-completed-extension-principle` | `theorem` | 1319 | Compact-to-completed extension principle |
| `thm:typeA-reduction-full-derived-DK-frontier` | `theorem` | 1356 | Type-$A$ reduction of the full derived DK frontier |
| `cor:what-remains-after-present-appendix` | `corollary` | 1403 | What remains after the present appendix |

#### `chapters/connections/ym_boundary_theory.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ym-bar-bridge` | `theorem` | 43 | Bridge theorem: boundary chiral algebra $\to$ visible center via bar-cobar |
| `thm:twisted-ym-boundary-brst` | `theorem` | 205 | Boundary BRST recovery for twisted Yang--Mills data |
| `thm:twisted-ym-tangent-center` | `theorem` | 231 | Tangent-to-center principle |
| `cor:twisted-ym-center-rigidity` | `corollary` | 250 | Center-vanishing rigidity criterion |
| `cor:twisted-ym-one-parameter` | `corollary` | 260 | One-parameter criterion |
| `thm:twisted-ym-tangent-factors-through-center` | `theorem` | 282 | The tangent functor factors through the dual center |
| `cor:twisted-ym-interface-invariance` | `corollary` | 308 | Interface invariance of tangent data |
| `cor:twisted-ym-center-comparison` | `corollary` | 326 | Comparison without full boundary equivalence |
| `thm:twisted-ym-dual-unobstructedness` | `theorem` | 368 | Dual unobstructedness criterion |
| `thm:twisted-ym-central-formality` | `theorem` | 391 | Central formality theorem |
| `lem:twisted-ym-center-tensor` | `lemma` | 451 | Center of a chiral tensor product |
| `thm:twisted-ym-binary-mixed-couplings` | `theorem` | 489 | Binary mixed-coupling theorem |
| `cor:twisted-ym-multibody-couplings` | `corollary` | 554 | Multi-body coupling expansion |
| `cor:twisted-ym-mixed-rigidity` | `corollary` | 588 | Mixed rigidity criterion |

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

### Appendices (213)

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
| `thm:nms-mc-principle` | `theorem` | 179 | Algebra structure $=$ Maurer--Cartan element |
| `prop:shadow-linfty-obstruction` | `proposition` | 212 | Genus-$0$ shadow obstruction tower as $L_\infty$ formality obstruction tower |
| `prop:nms-five-component` | `proposition` | 314 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | 374 | Shadow obstruction tower from MC evaluation |
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
| `thm:nms-nonseparating-clutching-law` | `theorem` | 2250 | Non-separating clutching law for the shadow obstruction tower |
| `cor:nms-genus-one-hessian-correction` | `corollary` | 2274 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | 2298 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2373 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2407 | Ambient complementarity and nonlinear modular shadows |
| `conj:nms-all-arity-resonance-boundary` | `theorem` | 2576 | All-arity boundary law for the resonance tower |
| `thm:nms-bipartite-complementarity` | `theorem` | 2777 | Bipartite complementarity principle |
| `thm:nms-bipartite-vanishing` | `theorem` | 2882 | Bipartite vanishing theorem |
| `thm:reduced-weight-finiteness` | `theorem` | 3222 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | 3310 | Window locality |
| `cor:exact-stabilization` | `corollary` | 3332 | Exact stabilization |
| `lem:nms-euler-inversion` | `lemma` | 3508 | Euler inversion |
| `prop:kac-shadow-singularity` | `proposition` | 3595 | Kac-shadow singularity principle |
| `thm:ds-shadow-depth-increase` | `theorem` | 3706 | DS shadow depth increase |
| `thm:shadow-subalgebra-autonomy` | `theorem` | 3911 | Shadow subalgebra autonomy |
| `cor:w-line-alternating-vanishing` | `corollary` | 3987 | $W$-line alternating vanishing |
| `thm:nms-shadow-mc-potential` | `theorem` | 4016 | Shadow obstruction tower as cyclic $L_\infty$ MC potential |
| `prop:nms-shadow-convergence` | `proposition` | 4080 | Shadow potential convergence |
| `thm:nms-mc-moduli-curve-structure` | `theorem` | 4189 | MC moduli curve structure |
| `thm:nms-hadamard-mc-potential` | `theorem` | 4252 | Hadamard factorization of the MC potential |
| `cor:nms-mc-solution-counting` | `corollary` | 4299 | MC solution counting |

#### `appendices/ordered_associative_chiral_kd.tex` (89)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bicom-e` | `lemma` | 167 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | 250 | Ordered chiral shuffle theorem |
| `prop:r-matrix-descent-vol1` | `proposition` | 510 | $R$-matrix twisted descent |
| `cor:pole-free-descent` | `corollary` | 655 | Pole-free descent is naive |
| `thm:opposite` | `theorem` | 798 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | 839 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | 853 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | 864 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | 927 | — |
| `prop:one-defect` | `proposition` | 954 | — |
| `thm:tangent=K` | `theorem` | 976 | Tangent identification |
| `cor:infdual` | `corollary` | 1013 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | 1036 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | 1088 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | 1121 | Diagonal correspondence |
| `cor:unit` | `corollary` | 1169 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | 1187 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | 1216 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | 1248 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | 1274 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | 1294 | Cap action |
| `thm:pair-of-pants` | `theorem` | 1349 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | 1387 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | 1441 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | 1490 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | 1514 | Master theorem |
| `prop:ordered-real-config-topology` | `proposition` | 1627 | Topology of ordered real configurations |
| `thm:heisenberg-ordered-bar` | `theorem` | 2034 | The Heisenberg ordered bar complex |
| `thm:heisenberg-rmatrix` | `theorem` | 2148 | Collision residue and $R$-matrix |
| `thm:heisenberg-yangian` | `theorem` | 2217 | Open-colour Koszul dual: the abelian Yangian |
| `thm:heisenberg-formality` | `theorem` | 2273 | Formality: class~G, shadow depth~$2$ |
| `thm:bg-ordered-bar` | `theorem` | 2386 | Free-field ordered bar complexes |
| `thm:wakimoto-ordered-bar` | `theorem` | 2458 | Wakimoto bar complex descent |
| `thm:lattice-symmetric-ordered-bar` | `theorem` | 2560 | Ordered bar complex with symmetric cocycle |
| `thm:lattice-nonsymmetric-ordered-bar` | `theorem` | 2626 | Ordered bar complex with non-symmetric cocycle |
| `thm:lattice-ordered-koszul-dual` | `theorem` | 2686 | Ordered Koszul dual of lattice algebras |
| `thm:drinfeld-yangian-sl2` | `theorem` | 2786 | Drinfeld presentation of $Y_\hbar(\mathfrak{sl}_2)$ |
| `prop:gauss-decomposition-sl2` | `proposition` | 2876 | Gauss decomposition |
| `thm:twisted-coproduct-sl2` | `theorem` | 2912 | Twisted coproduct |
| `thm:PBW-yangian-sl2` | `theorem` | 2964 | PBW theorem for $Y_\hbar(\mathfrak{sl}_2)$ |
| `thm:classical-limit-sl2` | `theorem` | 3005 | Classical limit |
| `prop:vir-collision-residue` | `proposition` | 3094 | Virasoro collision residue |
| `prop:vir-CYBE-ordered` | `proposition` | 3124 | Virasoro CYBE |
| `thm:grav-yangian-collapse` | `theorem` | 3151 | Gravitational Yangian collapse |
| `thm:vir-non-formality` | `theorem` | 3218 | Virasoro non-formality |
| `prop:grav-yangian-curvature` | `proposition` | 3264 | Gravitational Yangian curvature |
| `cor:gauge-gravity-dichotomy-ordered` | `corollary` | 3299 | Gauge-gravity complexity dichotomy |
| `thm:central-extension-invisible` | `theorem` | 3395 | Central extension is invisible to the open-colour double bar |
| `thm:two-colour-double-kd` | `theorem` | 3461 | Two-colour double Koszul duality is involutive |
| `cor:two-colours-non-redundant` | `corollary` | 3487 | Non-redundancy of the two colours |
| `thm:km-yangian` | `theorem` | 3569 | Universal Kac--Moody Yangian theorem |
| `thm:root-space-one-dim-v1` | `theorem` | 3887 | Root-space one-dimensionality |
| `lem:jacobi-collapse-v1` | `lemma` | 3936 | Jacobi collapse for star sectors |
| `thm:dynkin-beta-integral` | `theorem` | 4002 | Dynkin coefficient via the beta integral |
| `thm:complete-strictification-v1` | `theorem` | 4083 | Complete strictification for all simple Lie algebras |
| `thm:sl3-triangle-coefficient` | `theorem` | 4312 | Triangle coefficient for $\mathfrak{sl}_3$ |
| `prop:sl3-serre` | `proposition` | 4396 | Serre relations from root-space vanishing |
| `thm:sl3-rtt` | `theorem` | 4447 | RTT presentation for $Y_\hbar(\mathfrak{sl}_3)$ from the ordered bar complex |
| `thm:sl3-strictification` | `theorem` | 4519 | Vanishing of the spectral Drinfeld class for $\mathfrak{sl}_3$ |
| `thm:sl4-quadrilateral` | `theorem` | 4591 | Quadrilateral coefficient for $\mathfrak{sl}_4$ |
| `thm:B2-ordered-bar` | `theorem` | 4678 | Ordered bar complexes and Yangian $R$-matrices for rank-$2$ non-$A$ types |
| `thm:b-cycle-quantum-group` | `theorem` | 4983 | Quantum group from $B$-cycle monodromy |
| `thm:drinfeld-kohno` | `theorem` | 5105 | Drinfeld--Kohno; {} for the affine lineage |
| `thm:yangian-quantum-group` | `theorem` | 5184 | Yangian--quantum group deformation for the affine lineage |
| `cor:sl2-root-of-unity` | `corollary` | 5255 | $U_q(\mathfrak{sl}_2)$ at roots of unity from affine $\mathfrak{sl}_2$ |
| `thm:jones-genus1` | `theorem` | 5296 | Jones polynomial from genus-$1$ bar-complex monodromy |
| `thm:ordered-depth-spectrum` | `theorem` | 5459 | Ordered depth spectrum |
| `thm:ordered-AOS` | `theorem` | 5511 | Ordered AOS reduction |
| `prop:averaging-surplus` | `proposition` | 5581 | Averaging and surplus |
| `thm:w3-ordered-bar` | `theorem` | 5905 | Ordered bar complex of $\mathcal{W}_3$ via DS transport |
| `thm:class-m-ds-transport` | `theorem` | 6054 | Class~M persistence under DS transport |
| `thm:unshifted-identification` | `theorem` | 6284 | Unshifted identification |
| `thm:factorisation-identification` | `theorem` | 6328 | Factorisation identification on the Koszul locus |
| `prop:r-matrix-stable-envelope` | `proposition` | 6373 | $R$-matrix comparison |
| `comp:sl2-eval` | `computation` | 6517 | $\mathfrak{sl}_2$ evaluation module |
| `thm:sl2-R-matrix` | `theorem` | 6561 | $R$-matrix on $V_a\otimes V_b$ for $\mathfrak{sl}_2$ |
| `cor:sl2-clebsch-gordan` | `corollary` | 6609 | Clebsch--Gordan decomposition and non-semisimplicity |
| `comp:sl3-eval-fundamental` | `computation` | 6651 | $\mathfrak{sl}_3$ fundamental evaluation module |
| `comp:sl3-eval-adjoint` | `computation` | 6686 | $\mathfrak{sl}_3$ adjoint evaluation module |
| `prop:eval-drinfeld` | `proposition` | 6738 | Evaluation modules as single-root Drinfeld polynomials |
| `thm:line-category` | `theorem` | 6805 | Line category as Yangian modules |
| `thm:eval-braiding` | `theorem` | 6866 | Braiding from the $R$-matrix |
| `thm:annular-bar-differential` | `theorem` | 7022 | Annular bar differential |
| `thm:annular-HH` | `theorem` | 7115 | Annular bar complex computes chiral Hochschild homology |
| `thm:curvature-braiding-dichotomy` | `theorem` | 7215 | Curvature--braiding dichotomy at genus~$1$ |
| `thm:elliptic-spectral-dichotomy` | `theorem` | 7374 | Elliptic spectral dichotomy, genus-$1$ specialisation |
| `prop:r-matrix-eigenvalue` | `proposition` | 7577 | Eigenvalue decomposition |
| `thm:yang-r-sl2` | `theorem` | 7593 | Yang $R$-matrix for $\mathfrak{sl}_N$ |
| `thm:e1-ordered-bar-landscape` | `theorem` | 7876 | $\mathsf{E}_1$ ordered bar landscape |

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
