# Theorem Registry

Auto-generated on 2026-03-19 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 1999 |
| Total tagged claims | 2611 |
| Active files in `main.tex` | 78 |
| Total `.tex` files scanned | 102 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1999 |
| `ProvedElsewhere` | 388 |
| `Conjectured` | 196 |
| `Conditional` | 8 |
| `Heuristic` | 20 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 862 |
| `proposition` | 609 |
| `corollary` | 335 |
| `lemma` | 113 |
| `computation` | 72 |
| `calculation` | 3 |
| `remark` | 3 |
| `maintheorem` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 14 |
| Part I: Theory | 736 |
| Part II: Examples | 516 |
| Part III: Connections | 466 |
| Appendices | 267 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus_modular_koszul.tex` | 118 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 111 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 84 |
| `chapters/theory/higher_genus_complementarity.tex` | 77 |
| `appendices/nonlinear_modular_shadows.tex` | 61 |
| `chapters/theory/higher_genus_foundations.tex` | 60 |
| `chapters/examples/w_algebras.tex` | 57 |
| `chapters/theory/chiral_modules.tex` | 52 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 51 |
| `chapters/examples/free_fields.tex` | 47 |
| `chapters/examples/kac_moody.tex` | 45 |
| `chapters/connections/thqg_gravitational_s_duality.tex` | 42 |
| `chapters/examples/yangians_foundations.tex` | 42 |
| `chapters/connections/frontier_modular_holography_platonic.tex` | 40 |
| `chapters/connections/thqg_gravitational_complexity.tex` | 40 |
| `chapters/examples/yangians_computations.tex` | 38 |
| `chapters/connections/thqg_perturbative_finiteness.tex` | 35 |
| `chapters/examples/genus_expansions.tex` | 35 |
| `chapters/examples/lattice_foundations.tex` | 35 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 35 |

## Complete Proved Registry

### Frame (14)

#### `chapters/frame/heisenberg_frame.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 515 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 872 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 967 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1133 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1357 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1379 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1542 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1726 | Quantum complementarity for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2331 | $\mathfrak{sl}_2$ bar complex as Swiss-cheese coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2403 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2452 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2533 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 2571 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 2839 | CS $R$-matrix from the bar complex |

### Part I: Theory (736)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 871 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 1160 | Geometric realization |
| `prop:orthogonal` | `proposition` | 1285 | Orthogonality |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (111)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:curvature-central` | `theorem` | 181 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 285 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 362 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 431 | Conilpotency ensures convergence |
| `lem:arity-cutoff` | `lemma` | 603 | Arity cutoff: finite MC equation at each stage |
| `thm:completed-bar-cobar-strong` | `theorem` | 622 | MC element lifts to the completed convolution algebra |
| `prop:mc4-reduction-principle` | `proposition` | 764 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 829 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 866 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 904 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 953 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 1004 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 1067 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 1131 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 1167 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 1243 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 1340 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 1356 | Factorization-envelope criterion for principal stages |
| `cor:completion-closure-equivalence` | `corollary` | 1392 | Homotopy-categorical equivalence on the completion closure |
| `thm:coefficient-stability-criterion` | `theorem` | 1428 | Coefficient-stability criterion |
| `thm:completed-twisting-representability` | `theorem` | 1463 | Completed twisting representability |
| `thm:mc-twisting-closure` | `theorem` | 1486 | MC-twisting closure of the completion closure |
| `thm:uniform-pbw-bridge` | `theorem` | 1511 | Uniform PBW bridge from MC1 to MC4 |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 1617 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 1663 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 1698 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 1718 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 1736 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 1755 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 1797 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 1837 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 1878 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 1945 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 1988 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 2034 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 2096 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 2137 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 2209 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 2296 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 2322 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 2347 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 2401 | Stage-\texorpdfstring{$4$}{4} reduction to one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 2429 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 2466 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 2497 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 2539 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 2566 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 2596 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 2639 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 2674 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 2704 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 2721 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 2772 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 2833 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
| `cor:winfty-dual-candidate-construction` | `corollary` | 2872 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 2919 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} reduction on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 2958 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 3051 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 3082 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 3190 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 3238 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 3284 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 3311 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 3453 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 3492 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 3556 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 3611 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 3653 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 3747 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 3772 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 3811 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 3831 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 3869 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 3886 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 3909 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 3931 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 3947 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 3957 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 3973 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 3985 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 3998 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 4016 | Stage-\texorpdfstring{$5$}{5} mixed transport reduction to one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 4031 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 4050 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 4257 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 4274 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 4311 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 4351 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-conjecture-network-collapse` | `corollary` | 4647 | Visible stage-\texorpdfstring{$5$}{5} local conjecture network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 4689 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 4917 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 5155 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 5496 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 5532 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 5593 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 5605 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 5713 | Modular operad structure of the bar complex |
| `cor:genus-expansion-converges` | `corollary` | 5983 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 6043 | Functoriality of bar construction |
| `thm:reconstruction-vs-duality` | `theorem` | 6152 | Reconstruction versus duality |
| `thm:recognition-koszul-pairs` | `theorem` | 6215 | Recognition theorem for finite chiral Koszul pairs |
| `thm:mixed-boundary-sseq` | `theorem` | 6270 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | 6294 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | 6342 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | 6371 | Universality |
| `prop:sugawara-contraction` | `proposition` | 6379 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | 6444 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | 6460 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | 6506 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | 6555 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | 6599 | Diagonal GKO transgression |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (51)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 433 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 654 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 964 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 1079 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1152 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1196 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1264 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1330 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1465 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1531 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1651 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 1795 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 1811 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 1867 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 1890 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 1950 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 1995 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 2007 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 2042 | Derived equivalence |
| `lem:complete-filtered-comparison` | `lemma` | 2130 | Complete filtered comparison lemma |
| `cor:completed-derived-equivalence` | `corollary` | 2231 | Completed derived equivalence |
| `thm:barr-beck-lurie-koszulness` | `theorem` | 2333 | Barr--Beck--Lurie characterization of chiral Koszulness |
| `thm:fh-concentration-koszulness` | `theorem` | 2399 | Factorization homology concentration |
| `thm:fm-boundary-acyclicity` | `theorem` | 2459 | FM boundary acyclicity |
| `prop:bar-fh` | `proposition` | 2831 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 2909 | Cobar as factorization cohomology |
| `thm:ks-centrality` | `theorem` | 3613 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | 3656 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | 3707 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | 3742 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | 3788 | Quadratic frontier |
| `prop:eta-hessian-transfer` | `proposition` | 3882 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | 3918 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | 3963 | Admissible scalar rigidity |
| `cor:ds-not-first-frontier` | `corollary` | 3996 | Drinfeld--Sokolov reductions remain scalar-rigid |
| `thm:classification-scalar-genera` | `theorem` | 4038 | Classification of scalar genera |
| `thm:platonic-hierarchy-log` | `theorem` | 4105 | Five-step hierarchy of the categorical logarithm |
| `prop:cech-two-element-strict` | `proposition` | 4620 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | 4947 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | 5007 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | 5039 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | 5061 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | 5159 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | 5207 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | 5227 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | 5272 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | 5303 | Repeated roots encode extension data |
| `thm:common-core-exact-sequences-inv` | `theorem` | 5335 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | 5363 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | 5430 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | 5452 | Explicit coprime-locus projectors |

#### `chapters/theory/bar_construction.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 253 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 574 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 664 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 723 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 789 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 817 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 912 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 954 | Arnold relations |
| `comp:deg0` | `computation` | 997 | Degree 0 |
| `comp:deg1-general` | `computation` | 1015 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1128 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1167 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1173 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1205 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1228 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1295 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1346 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1363 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1450 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1476 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1500 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1564 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1639 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1701 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1811 | Bar complex is chiral |

#### `chapters/theory/chiral_hochschild_koszul.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 164 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 315 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 353 | Hochschild spectral sequence |
| `thm:main-koszul-hoch` | `theorem` | 472 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `thm:hochschild-polynomial-growth` | `theorem` | 587 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 657 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `prop:e2-formality-hochschild` | `proposition` | 698 | $\Etwo$-formality of chiral Hochschild cohomology |
| `conj:bifunctor-obstruction-decomposition` | `theorem` | 938 | Bifunctor obstruction decomposition |
| `comp:boson-hochschild` | `computation` | 1152 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 1178 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 1280 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 1374 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 1472 | Kac--Moody cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | 1678 | Genus truncation |
| `thm:mc2-1-km` | `theorem` | 1750 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1867 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 2115 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 2201 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 2320 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | 2502 | Strictification principle for modular deformation theory |
| `prop:d-mod-squared-zero` | `proposition` | 2639 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2775 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 2950 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 3140 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 3266 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 3511 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 3657 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 3796 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 3877 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 3924 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 4216 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 4347 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 4394 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 4587 | Boson-fermion duality |
| `prop:hochschild-cech-ss` | `proposition` | 4790 | Hochschild--\v{C}ech spectral sequence |

#### `chapters/theory/chiral_koszul_pairs.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 198 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 225 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 245 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 273 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 348 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 603 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 681 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 736 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 780 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 927 | Bar concentration for Koszul pairs |
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1029 | Formality implies chiral Koszulness |
| `conj:ainfty-koszul-characterization` | `theorem` | 1063 | Converse: formality implies chiral Koszulness |
| `conj:ext-diagonal-vanishing` | `theorem` | 1096 | Ext diagonal vanishing criterion |
| `prop:pbw-universality` | `proposition` | 1134 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1160 | Universal vertex algebras are chirally Koszul |
| `thm:kac-shapovalov-koszulness` | `theorem` | 1184 | Kac--Shapovalov criterion for simple quotients |
| `thm:koszul-equivalences-meta` | `theorem` | 1244 | Equivalences of chiral Koszulness |
| `prop:cumulant-window-inversion` | `proposition` | 1730 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 1788 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 1953 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 2013 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 2167 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 2261 | Bar computes Koszul dual — complete statement |
| `lem:completion-convergence` | `lemma` | 2349 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 2398 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 2955 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 3173 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 3238 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 3299 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 3422 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 3464 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 3518 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 3553 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 3748 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (52)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 180 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 285 | Module Koszul equivalence |
| `thm:monoidal-module-koszul` | `theorem` | 315 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 455 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 531 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 635 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 728 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 786 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 941 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 1235 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1624 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1685 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1885 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1943 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1977 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:orbit-duality` | `proposition` | 2103 | Orbit duality for affine vertex algebras |
| `prop:logarithmic-bar` | `proposition` | 2228 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2322 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2433 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2468 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2507 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2524 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2564 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2586 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2736 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2843 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2957 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3037 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3191 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3222 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3274 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3353 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3439 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3498 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3574 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3651 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3701 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3794 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3848 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3914` | `calculation` | 3914 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3941` | `calculation` | 3941 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3972` | `calculation` | 3972 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4090 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4215 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4272 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4362 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4404 | \texorpdfstring{$\mathcal{W}$}{W}-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4459 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4501 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4631 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4770 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4880 | Heisenberg fusion splitting |

#### `chapters/theory/cobar_construction.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 197 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 258 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 291 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 373 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 449 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 563 | Verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 809 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 969 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1187 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1318 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1370 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 1643 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1691 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1712 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1802 | Topology |
| `thm:poincare-verdier` | `theorem` | 1861 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 1950 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 1975 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 2021 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 2175 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2271 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2412 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2437 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2490 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2543 | Recognition principle |
| `lem:deformation-space` | `lemma` | 2915 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 2957 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 3005 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3084 | Curved differential formula |

#### `chapters/theory/configuration_spaces.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 299 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 409 | Normal crossings |
| `thm:closure-relations` | `theorem` | 504 | Closure relations |
| `thm:log-complex` | `theorem` | 617 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 656 | Arnold relations |
| `prop:twisting-morphism-propagator` | `proposition` | 698 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 765 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 832 | Residue operations |
| `prop:residue-local` | `proposition` | 887 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 936 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1182 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1249 | Conformal blocks from punctured bar complex |
| `prop:eta` | `proposition` | 1413 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:FM-convergence` | `theorem` | 1760 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1819 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1925 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1967 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 1994 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 2016 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 2056 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 2080 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 2115 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 2137 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 2171 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2187 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2209 | Nilpotency from Arnold relations |
| `thm:arnold-jacobi` | `theorem` | 2331 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2384 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2430 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2462 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2507 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 2738 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 2808 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 2945 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3155` | `computation` | 3155 | Explicit examples |

#### `chapters/theory/derived_langlands.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:langlands-bar-bridge` | `theorem` | 82 | Bridge theorem: bar complex at critical level $\longrightarrow$ opers $\longrightarrow$ geometric Langlands |
| `thm:oper-bar-h0-dl` | `theorem` | 288 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 323 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 347 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 384 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 465 | Differential analysis at arity 3 |
| `prop:d4-nonvanishing` | `proposition` | 545 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 604 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 617 | Full derived identification |
| `prop:bar-as-localization` | `proposition` | 700 | The bar complex as localization |
| `prop:sl2-periodicity-dl` | `proposition` | 822 | Affine sl2 periodicity |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 898 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/e1_modular_koszul.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fass-d-squared-zero` | `theorem` | 123 | — |
| `thm:fcom-coinvariant-fass` | `theorem` | 142 | — |
| `rem:e1-mc-element` | `theorem` | 194 | $E_1$ Maurer--Cartan element |
| `prop:e1-shadow-r-matrix` | `proposition` | 227 | — |
| `thm:e1-mc-finite-arity` | `theorem` | 311 | $E_1$ MC equation at finite arity |
| `thm:e1-coinvariant-shadow` | `theorem` | 379 | Coinvariant projection: $E_1$ shadows to $E_\infty$ shadows |
| `thm:e1-theorem-A-modular` | `theorem` | 560 | Theorem~$\mathrm{A}^{E_1}$ at all genera: ordered bar--cobar adjunction |
| `thm:e1-theorem-B-modular` | `theorem` | 609 | Theorem~$\mathrm{B}^{E_1}$ at all genera: ordered bar--cobar inversion |
| `thm:e1-theorem-C-modular` | `theorem` | 635 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
| `thm:e1-theorem-D-modular` | `theorem` | 669 | Theorem~$\mathrm{D}^{E_1}$ at all genera: modular $R$-matrix as $E_1$ characteristic |
| `thm:e1-theorem-H-modular` | `theorem` | 733 | Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered Hochschild at genus~$g$ |

#### `chapters/theory/en_koszul_duality.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:en-chiral-bridge` | `theorem` | 60 | Bridge theorem: $\En$ bar-cobar and the chiral $\Eone$ engine |
| `prop:linking-sphere-residue` | `proposition` | 394 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 469 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 629 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 687 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |
| `thm:bar-swiss-cheese` | `theorem` | 999 | Bar complex as Swiss-cheese coalgebra |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 40 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 143 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 65 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 122 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 231 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 277 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 325 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 354 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 416 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 443 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 500 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 558 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 638 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 808 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 829 | — |
| `thm:fourier-specialization` | `theorem` | 864 | Specialization |
| `thm:fourier-four-properties` | `theorem` | 919 | The four properties of the Fourier transform |
| `rem:fourier-genus-preview` | `remark` | 1019 | Ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus_complementarity.tex` (77)

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
| `prop:lagrangian-eigenspaces` | `proposition` | 1634 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 1725 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 1878 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 1946 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 2046 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 2074 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 2111 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 2154 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 2190 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 2216 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 2471 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 2652 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 2702 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 2715 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 2757 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 2816 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 2858 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 2886 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 2908 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 2952 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 3130 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 3178 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 3266 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 3293 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 3321 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 3355 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 3380 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 3440 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 3486 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 3525 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 3554 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 3578 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 3603 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 3635 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 3667 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 3693 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 3709 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 3803 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 3879 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 3927 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 4016 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | 4191 | Ambient complementarity in tangent form |
| `thm:ambient-complementarity-fmp` | `theorem` | 4234 | Ambient complementarity as shifted symplectic formal moduli problem |
| `thm:shifted-cotangent-normal-form` | `theorem` | 4492 | Shifted cotangent normal form |
| `prop:legendre-duality-potentials` | `proposition` | 4541 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | 4556 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | 4586 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | 4610 | Criterion for fake complementarity |
| `thm:holo-comp-bulk-reconstruction` | `theorem` | 4806 | Protected bulk reconstruction |
| `thm:holo-comp-cotangent-realization` | `theorem` | 4856 | Shifted cotangent realization |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | 4883 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | 4969 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | 5013 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | 5090 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | 5173 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | 5242 | First nonlinear holographic anomaly |
| `thm:critical-dimension` | `theorem` | 5346 | Critical dimension |

#### `chapters/theory/higher_genus_foundations.tex` (60)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:genus-g-curvature-package` | `proposition` | 331 | The genus-$g$ curvature package |
| `thm:bar-ainfty-complete` | `theorem` | 606 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 706 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 797 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 910 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 1017 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 1164 | Verdier duality of operations |
| `thm:bar-curved-ch-infty` | `theorem` | 1326 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
| `thm:convergence-filtered` | `theorem` | 1404 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1613 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1647 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1681 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1701 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1717 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2019 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 2104 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2319 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2588 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2791 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2851 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 3104 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:arnold-genus1` | `theorem` | 3163 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 3198 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 3255 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 3523 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3556 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 3683 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3786 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3840 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 3918 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 4035 | \texorpdfstring{$W_3$}{W3} obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 4106 | Explicit genus-\texorpdfstring{$1$}{1} value of the \texorpdfstring{$W_3$}{W3} obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 4127 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 4156 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 4241 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4343 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4497 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4530 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4546 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4562 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4580 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 4603 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4625 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4677 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4749 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4779 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4865 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4909 | Grothendieck--Riemann--Roch bridge |
| `lem:stable-graph-d-squared` | `lemma` | 5077 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 5139 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 5177 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 5219 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 5308 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 5396 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 5464 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 5498 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 5539 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 5596 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 5624 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 5674 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (118)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:genus-graded-koszul` | `theorem` | 124 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 155 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 488 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 521 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 562 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 698 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 965 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 990 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1187 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1239 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1339 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1389 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1451 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `lem:e2-higher-genus` | `lemma` | 1626 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 1753 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 1863 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 1969 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 1998 | Universal modular Maurer--Cartan class |
| `thm:mc2-bar-intrinsic` | `theorem` | 2136 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 2295 | Shadow extraction |
| `thm:explicit-theta` | `theorem` | 2395 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 2616 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 3030 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 3109 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 3222 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 3256 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 3288 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 3484 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 3560 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 3625 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 3760 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 3857 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 3968 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 4105 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 4257 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 4431 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 4581 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 4775 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 4895 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 4994 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 5084 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 5196 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 5268 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 5350 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 5428 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 5505 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 5581 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 5656 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 5722 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 5800 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 5875 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 5922 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 5964 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 6023 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 6077 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 6110 | Scalar saturation for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 6148 | Scalar saturation persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 6201 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 6273 | Scalar saturation for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 6355 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 6527 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 6690 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 6773 | Cyclic rigidity at generic level |
| `thm:algebraic-family-rigidity` | `theorem` | 6933 | Algebraic-family rigidity |
| `cor:saturation-algebraic-families` | `corollary` | 7039 | Saturation at all non-critical levels for algebraic families |
| `thm:conformal-bootstrap-rigidity` | `theorem` | 7100 | $L_0$-bootstrap rigidity |
| `cor:one-channel-no-lie` | `corollary` | 7207 | One-channel criterion without Lie symmetry |
| `thm:tautological-line-support` | `theorem` | 7435 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 7537 | MC2 reduced to cyclic model |
| `thm:convolution-dg-lie-structure` | `theorem` | 7691 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 7756 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 8120 | Modular homotopy convolution |
| `prop:modular-homotopy-type-structure` | `proposition` | 8204 | Structure of the modular homotopy type |
| `cor:strictification-comparison` | `corollary` | 8251 | Strictification comparison |
| `cor:vol1-theta-log-fm-twisting-data` | `corollary` | 8574 | $\Theta_\cA$ as universal modular twisting morphism |
| `prop:vol1-first-two-weights-log-fm` | `proposition` | 8828 | First two weights |
| `comp:vol1-low-genus-log-fm-chart` | `computation` | 8903 | Low-genus amplitudes |
| `prop:master-equation-from-mc` | `proposition` | 9315 | All-arity master equation from MC |
| `thm:recursive-existence` | `theorem` | 9367 | Recursive existence |
| `thm:ran-coherent-bar-cobar` | `theorem` | 9400 | Ran-coherent bar-cobar equivalence |
| `thm:shadow-channel-decomposition` | `theorem` | 9460 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 9540 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 9590 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 9713 | The explicit formula: direct derivation |
| `lem:graph-sum-truncation` | `lemma` | 10000 | Graph-sum truncation criterion |
| `conj:operadic-complexity-detailed` | `theorem` | 10075 | Operadic complexity |
| `prop:shadow-formality-low-arity` | `proposition` | 10161 | Shadow--formality identification at low arity |
| `thm:shadow-formality-identification` | `theorem` | 10232 | Shadow tower as formality obstruction tower |
| `thm:shadow-archetype-classification` | `theorem` | 10540 | Shadow archetype classification |
| `cor:shadow-depth-koszul-invariance` | `corollary` | 10624 | Shadow depth under Koszul duality |
| `thm:shadow-separation` | `theorem` | 10645 | Shadow separation and completeness |
| `thm:shadow-tautological-ring` | `theorem` | 10790 | Shadow classes in the tautological ring |
| `cor:analytic-shadow-realization` | `corollary` | 10933 | Analytic shadow realization |
| `prop:finite-jet-rigidity` | `proposition` | 11079 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 11102 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 11138 | Gaussian collapse for abelian input |
| `thm:cubic-gauge-triviality` | `theorem` | 11220 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | 11292 | Independent sum factorization |
| `thm:platonic-adjunction` | `theorem` | 11364 | The platonic adjunction |
| `cor:envelope-universal-mc` | `corollary` | 11497 | The envelope carries the universal MC class |
| `conj:tropical-koszulness` | `theorem` | 11579 | Tropical Koszulness |
| `prop:genus0-curve-independence` | `proposition` | 11671 | Genus-$0$ curve-independence |
| `prop:chriss-ginzburg-structure` | `proposition` | 11859 | MC structure principle |
| `prop:planar-forest-coinvariant` | `proposition` | 12238 | Planar forests map to unordered forests |
| `thm:planar-forest-tropicalization` | `theorem` | 12271 | Planar tropicalization |
| `prop:coefficient-algebras-well-defined` | `proposition` | 12348 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 12381 | Square-zero: convolution level |
| `conj:differential-square-zero` | `theorem` | 12395 | Square-zero: ambient level |
| `thm:inductive-genus-determination` | `theorem` | 12544 | Inductive genus determination |
| `cor:genus-base-cases` | `corollary` | 12612 | Base cases |
| `rem:genus2-shell-activation` | `theorem` | 12649 | Genus-$2$ shell activation as depth diagnostic |
| `prop:2d-convergence` | `proposition` | 12763 | Two-dimensional convergence |
| `thm:analytic-algebraic-comparison` | `theorem` | 12819 | Analytic = algebraic |
| `thm:determinantal-branch-formula` | `theorem` | 12955 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | 12991 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | 13022 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | 13086 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | 13122 | The frontier is cubic |

#### `chapters/theory/hochschild_cohomology.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 106 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 150 | W-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:404` | `computation` | 404 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 460 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 540 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 795 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 827 | Hochschild cup product exchange |

#### `chapters/theory/introduction.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 714 | Central charge complementarity |
| `thm:modular-koszul-duality-main` | `theorem` | 816 | Modular Koszul duality |
| `cor:shadow-separation-intro` | `corollary` | 916 | Shadow separation; ; Theorem~\textup{\ref{thm:shadow-separation}} |
| `prop:modular-homotopy-classification` | `proposition` | 1334 | Classification by modular homotopy type |
| `prop:shadow-massey-identification` | `proposition` | 1404 | Genus-$0$ shadow obstructions $=$ $A_\infty$ Massey products |
| `prop:chirAss-self-dual` | `proposition` | 2631 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | 155 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 200 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 240 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 259 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 316 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 379 | \texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 438 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 567 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 661 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 676 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 780 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 902 | Maurer--Cartan correspondence — quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 993 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1023 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1217 | Positselski comodule-contramodule equivalence |
| `thm:full-derived-module-equiv` | `theorem` | 1243 | Full derived module equivalence |
| `thm:cs-koszul-km` | `theorem` | 1360 | Chern--Simons equations from Koszul duality |
| `thm:linf-mc-flatness` | `theorem` | 1437 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan as homotopy flatness |
| `thm:cs-koszul-general` | `theorem` | 1507 | CS/Koszul for general non-quadratic algebras |
| `thm:bv-structure-bar` | `theorem` | 1695 | BV structure on bar complex |
| `thm:ordered-shuffle` | `theorem` | 1847 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | 1889 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | 1919 | Enveloping duality |
| `thm:ordered-bimod-bicomod` | `theorem` | 1958 | Bimodule--bicomodule equivalence |
| `thm:ordered-diagonal` | `theorem` | 1983 | Diagonal correspondence |
| `thm:ordered-HH-coHH-homology` | `theorem` | 2031 | Hochschild--coHochschild duality, homological version |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | 2062 | Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-pair-of-pants` | `theorem` | 2110 | Ordered pair-of-pants algebra |
| `thm:ordered-master` | `theorem` | 2134 | Master theorem: the ordered open trace formalism |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 223 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 335 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 402 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 493 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 552 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 568 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 659 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 743 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:chiral-operad-genus0` | `proposition` | 319 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 363 | Prism principle --- operadic identification |
| `thm:prism-higher-genus` | `theorem` | 572 | Prism principle --- higher-genus extension |
| `cor:feynman-genus0-reduction` | `corollary` | 644 | Genus-$0$ reduction to the operadic bar construction |
| `cor:hbar-genus-identification` | `corollary` | 669 | The loop expansion is the genus expansion |
| `cor:prism-principle` | `corollary` | 785 | The prism principle |
| `thm:partition` | `theorem` | 936 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:two-element-strict` | `proposition` | 707 | Two-element covers are strict |
| `prop:borcherds-shadow-identification` | `proposition` | 1191 | Secondary Borcherds operations as shadow tower obstructions |

### Part II: Examples (516)

#### `chapters/examples/bar_complex_tables.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 713 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 806 | Modular rank of \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 885 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 946 | PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} |
| `comp:sl3-casimir-decomp` | `computation` | 1039 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | 1122 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | 1451 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1756 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1802 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | 1873 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | 1924 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2057 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2093 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2127 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2557 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2732 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2952 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 3006 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3043 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3317 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3496 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3793 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3855 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4052 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4202 | BGG involution under Koszul duality |

#### `chapters/examples/beta_gamma.tex` (23)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 187 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 238 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 273 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 326 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 364 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | 385 | — |
| `thm:cobar-fermions` | `theorem` | 413 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | 450 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 538 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 805 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 925 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 1026 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1167 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1251 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1402 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |
| `thm:betagamma-quartic-birth` | `theorem` | 1836 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | 1872 | $\beta\gamma$ shadow Postnikov tower: arity~$4$ on weight-changing line |
| `lem:betagamma-ell2-vanishing` | `lemma` | 1973 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | 2020 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | 2130 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | 2172 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | 2202 | Pure contact boundary law |
| `prop:betagamma-translation-coproduct` | `proposition` | 2365 | Translation and coproduct |

#### `chapters/examples/deformation_quantization.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 128 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 181 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 413 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 526 | Genus expansion |

#### `chapters/examples/deformation_quantization_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 452 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 524 | Deformation--duality compatibility |

#### `chapters/examples/free_fields.tex` (47)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:single-fermion-boson-duality` | `theorem` | 203 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | 255 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 311 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 362 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 373 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `thm:heisenberg-bar` | `theorem` | 445 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 468 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | 510 | Heisenberg curved structure |
| `thm:lattice-voa-bar` | `theorem` | 557 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 586 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | 616 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 653 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | 698 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 722 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 937 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 1013 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 1045 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 1180 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 1235 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 1285 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1327 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1480 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1556 | Spectral flow under Koszul duality |
| `thm:heisenberg-not-self-dual` | `theorem` | 1775 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 1880 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 1911 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2170 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 2284 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 2557 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 2706 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 2753 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 2812 | Heisenberg level inversion: curved duality |
| `thm:virasoro-moduli` | `theorem` | 2872 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 2910 | Geometric interpretation |
| `thm:virasoro-string` | `theorem` | 2989 | Virasoro-string duality |
| `thm:algebraic-string-dictionary` | `theorem` | 3025 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 3077 | Genus-\texorpdfstring{$0$}{0} string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 3119 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 3228 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 3308 | Bar complex computes genus-\texorpdfstring{$g$}{g} string integrands |
| `thm:modular-invariance` | `theorem` | 3446 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 3483 | Modular anomaly for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:wakimoto-bar` | `theorem` | 3592 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 3605 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 3610 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 3637 | Quantum integrability via \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:filtered-bar-complex` | `theorem` | 3697 | Filtered bar complex |

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
| `prop:bivariate-gf` | `proposition` | 725 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 767 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 821 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 932 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 1042 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1182 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1249 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1314 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1400 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1532 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1562 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1579 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1614 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1685 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1813 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1855 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1934 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 2083 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2148 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:complementarity-classification` | `proposition` | 2384 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2438 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2733 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2833 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2849 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2874 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2906 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 3001 | Loop expansion interpretation |
| `thm:boundary-characters-bar-hilbert` | `theorem` | 3172 | Boundary characters as bar Hilbert series |

#### `chapters/examples/heisenberg_eisenstein.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-sewing` | `theorem` | 117 | Heisenberg sewing theorem |
| `thm:heisenberg-genus-one-complete` | `theorem` | 263 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 350 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 392 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 510 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 613 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 662 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 874 | Multi-boson Eisenstein corrections |
| `thm:heisenberg-exact-linearity` | `theorem` | 1166 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | 1206 | Heisenberg shadow Postnikov tower: finite termination at arity~$2$ |
| `cor:heisenberg-gaussian-boundary` | `corollary` | 1428 | Gaussian boundary law |

#### `chapters/examples/kac_moody.tex` (45)

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
| `prop:ff-channel-shear` | `proposition` | 991 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 1041 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 1107 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1171 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1210 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1264 | Closed-form OPE for Koszul dual |
| `thm:km-quantum-groups` | `theorem` | 1338 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 1664 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 1734 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 1822 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 1934 | KW formula via bar complex: general simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `prop:admissible-verlinde-bar` | `proposition` | 2004 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2243 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 2324 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 2389 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 2441 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 2507 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 2570 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 2616 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 2655 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 2692 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 2871 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 2901 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 2931 | Full derived oper identification |
| `thm:affine-cubic-normal-form` | `theorem` | 3167 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | 3203 | Affine shadow Postnikov tower: finite termination at arity~$3$ |
| `prop:affine-cyclic-slice-data` | `proposition` | 3230 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 3278 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 3335 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 3412 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 3498 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 3534 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 3623 | Vanishing of the genus loop on the affine cubic |
| `cor:level-rank-bar-intertwining` | `corollary` | 3841 | Bar-complex intertwining |

#### `chapters/examples/landscape_census.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 282 | Paired standard-tower MC4 completion packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 483 | Minimal closure conditions for the standard-tower MC4 completion target |
| `cor:genus1-anomaly-ratio` | `corollary` | 612 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `prop:bar-dimensions` | `proposition` | 819 | Koszul dual Hilbert functions |
| `cor:subexp-free-field` | `corollary` | 1050 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 1060 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 1077 | DS reduction and bar cohomology generating functions |
| `thm:ds-spectral-branch-preservation` | `theorem` | 1236 | DS preservation of the sub-discriminant |
| `prop:hred-sl2` | `proposition` | 1419 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 1613 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1704 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1801 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1867 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 1922 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1973 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1988 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 2077 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2266 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2572 | Spectral sequence collapse |

#### `chapters/examples/lattice_foundations.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:lattice:cocycle-class` | `lemma` | 276 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 438 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 657 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 754 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 777 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 811 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 845 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 890 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 976 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 1021 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1226 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1271 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1313 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1336 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1460 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1477 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1502 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1704 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1888 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2513 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2581 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2655 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2814 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3116 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3197 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3370 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3567 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3610 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3768 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3815 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 3901 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 3982 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |
| `prop:lattice:genus1-simple-pole` | `proposition` | 4168 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4185 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | 4282 | Lattice shadow Postnikov tower: termination at weight~$2$ |

#### `chapters/examples/minimal_model_examples.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 405 | Fusion from bar complex on the torus |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 81 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | 215 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 363 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 387 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | 422 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 447 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 526 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 553 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 613 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 633 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 660 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 756 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

#### `chapters/examples/toroidal_elliptic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 375 | Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0} |
| `thm:elliptic-vs-rational` | `theorem` | 473 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 845 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1041 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1119 | DYBE and bar nilpotency |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 44 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 146 | Mode expansion |
| `thm:c-scaling` | `theorem` | 197 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 296 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 461 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | 545 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 596 | Quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | 657 | Two-point function \texorpdfstring{$\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$}{:W2:_qp(z) :W2:_qp(w)} |
| `thm:w3-null-level1` | `theorem` | 717 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 820 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 891 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 933 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 1004 | Level-2 Gram matrix |

#### `chapters/examples/w_algebras.tex` (57)

| Label | Env | Line | Title |
|---|---|---:|---|
| `comp:w3-genus1-hessian` | `computation` | 159 | The $\mathcal W_3$ genus-$1$ Hessian |
| `comp:w-entropy-ladder` | `computation` | 195 | Completion entropy ladder |
| `thm:w-algebra-koszul-main` | `theorem` | 250 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 453 | Subregular \texorpdfstring{$\mathcal{W}$}{W}-algebra duality for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} |
| `thm:w-geometric-ope` | `theorem` | 783 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 854 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-critical-bar` | `theorem` | 894 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 931 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 1057 | Virasoro uncurved self-duality at \texorpdfstring{$c=0$}{c=0} |
| `thm:vir-genus1-curvature` | `theorem` | 1186 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1237 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1301 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1470 | Koszul dual of \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1551 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1617 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 1687 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 1782 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 1878 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 1899 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-center-langlands` | `theorem` | 1988 | \texorpdfstring{$\mathcal{W}$}{W}-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 2093 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `thm:w-universal-gravitational-cubic` | `theorem` | 2846 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | 2901 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | 2938 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | 3025 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-resonance-reorganization` | `theorem` | 3095 | Resonance reorganization |
| `cor:w-complementarity-potential-poles` | `corollary` | 3232 | Pole structure of the complementarity potential |
| `thm:w-w3-mixed-shadow` | `theorem` | 3300 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w-w3-weight6-resonance` | `proposition` | 3382 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | 3453 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | 3479 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-archetype-trichotomy` | `theorem` | 3555 | Archetype trichotomy |
| `thm:w-virasoro-quintic-forced` | `theorem` | 3622 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | 3667 | Explicit quintic shadow for Virasoro |
| `thm:w-finite-termination` | `theorem` | 3772 | Finite termination for primitive archetypes |
| `cor:virasoro-postnikov-nontermination` | `corollary` | 3849 | Virasoro/$\mathcal{W}_N$ shadow Postnikov tower: infinite |
| `thm:w-virasoro-genus1-hessian` | `theorem` | 3887 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | 4054 | $\mathcal{W}_3$ quintic obstruction |
| `thm:w-finite-arity-polynomial-pva` | `theorem` | 4279 | Finite-arity theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | 4317 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | 4359 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | 4386 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | 4462 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | 4487 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | 4521 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | 4559 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | 4579 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `thm:w-pbw-slodowy-collapse` | `theorem` | 4757 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | 4818 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-arity-detection` | `theorem` | 4884 | Canonical arity detection |
| `thm:w-bp-strict` | `theorem` | 4910 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | 4960 | $\mathcal{W}_4^{(2)}$ has canonical arity~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | 5019 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | 5078 | Subregular Appell formula |
| `thm:w-unbounded-canonical-arity` | `theorem` | 5116 | Unbounded canonical arity |
| `cor:w-subregular-arity-staircase` | `corollary` | 5145 | The subregular arity staircase |
| `thm:w-subregular-classification` | `theorem` | 5187 | Subregular classification |

#### `chapters/examples/w_algebras_deep.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 138 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 830 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `prop:w3-deg3-vacuum` | `proposition` | 1339 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1549 | DS hierarchy and Koszul duality: proved cases |
| `thm:ds-platonic-functor` | `theorem` | 1619 | DS reduction as a functor on platonic packages |
| `thm:winfty-scalar` | `theorem` | 2005 | Scalar saturation of $\mathcal{W}_\infty$: the shadow tower collapses |
| `prop:gram-wt4` | `proposition` | 2156 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | 2221 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | 2264 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:virasoro-primitive` | `proposition` | 2447 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | 2508 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | 2549 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | 2652 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | 2685 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | 2706 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | 2738 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | 2797 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | 2833 | $\Walg_\infty$ bar-window series and Koszul entropy |

#### `chapters/examples/yangians_computations.tex` (38)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:yangian-rank-dependence` | `proposition` | 520 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 657 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 746 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 802 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 852 | DK-2 reduction to thick generation in category~\texorpdfstring{$\mathcal{O}$}{O} |
| `prop:dk2-thick-generation-typeA` | `proposition` | 904 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `lem:composition-thick-generation` | `lemma` | 998 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 1029 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 1113 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 1215 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 1237 | Finite-dimensional factorization Drinfeld--Kohno, type~\texorpdfstring{$A$}{A} |
| `cor:dk-partial-conj` | `corollary` | 1312 | Partial resolution of Conjecture~\textup{\ref{conj:full-derived-dk}} |
| `cor:dk-poly-catO` | `corollary` | 1331 | Factorization DK for polynomial category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A} |
| `lem:fd-thick-closure` | `lemma` | 1403 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 1489 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 1740 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 1870 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 2028 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 2048 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 2073 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 2246 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:baxter-exact-triangles-opoly` | `theorem` | 2308 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `prop:baxter-yangian-equivariance` | `proposition` | 2390 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | 2464 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `thm:shifted-prefundamental-generation` | `theorem` | 2509 | $E_1$-chiral thick generation for $Y(\mathfrak{sl}_N)$ |
| `prop:prefundamental-clebsch-gordan` | `proposition` | 2733 | Prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | 2758 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | 2772 | $K_0$ generation of $\mathcal{O}_Y$ |
| `thm:mc3-type-a-resolution` | `theorem` | 3065 | MC3 resolution in type $A$ |
| `thm:yangian-vector-seed-propagation` | `theorem` | 3501 | Propagation from the vector seed |
| `cor:compact-core-rigidity` | `corollary` | 3531 | Compact-core rigidity |
| `prop:yangian-failure-unweighted` | `proposition` | 3554 | Failure of unweighted stabilization |
| `thm:yangian-weightwise-MC4` | `theorem` | 3569 | Weightwise MC4 for the principal RTT tower |
| `thm:yangian-baxter-rees-algebraicity` | `theorem` | 3620 | Algebraicity of the Baxter--Rees family |
| `thm:yangian-generic-boundary-fibers` | `theorem` | 3645 | Generic and boundary fibers |
| `prop:baxter-rees-derived-realization` | `proposition` | 3672 | Derived realization of the Baxter--Rees family |
| `thm:yangian-H2-reduction` | `theorem` | 3739 | $H^2$-reduction to the three-leg sector |
| `prop:yangian-baxter-KS-cocycle` | `proposition` | 3816 | Concrete cocycle |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (84)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-dk-affine` | `theorem` | 106 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 205 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 370 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 474 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 591 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 640 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 777 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 965 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 1006 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 1276 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 1397 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 1599 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 1706 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 1804 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 2022 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 2105 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `thm:bridge-criterion` | `theorem` | 2272 | Bridge Criterion Theorem |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 2424 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 2541 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 2600 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 2683 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 2764 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 2795 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 2832 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 2899 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 2929 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 2960 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 3019 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 3098 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 3127 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 3194 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 3226 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 3264 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 3279 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 3329 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 3386 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 3433 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 3524 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 3624 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 3664 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 3700 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 3727 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 3870 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 3902 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 3952 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 3990 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 4017 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 4050 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 4088 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 4114 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 4310 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 4373 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 4408 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 4462 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 4495 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 4554 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 4629 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts-orig` | `corollary` | 4785 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet-orig` | `corollary` | 4814 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization-orig` | `corollary` | 4847 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization-orig` | `corollary` | 4878 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet-orig` | `corollary` | 4929 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 5036 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 5135 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 5196 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 5246 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 5305 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed-orig` | `corollary` | 5348 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line-orig` | `corollary` | 5381 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |
| `prop:free-propagator-matching` | `proposition` | 6061 | Free/$\beta\gamma$ propagator matching |
| `prop:affine-propagator-matching` | `proposition` | 6107 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `thm:spectral-derived-additive-kz` | `theorem` | 6275 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | 6326 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | 6378 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | 6452 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | 6536 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | 6594 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | 6636 | Quadrilateral localization |
| `lem:class3-bch-spectral` | `lemma` | 6671 | Class-$3$ ordered BCH coefficient |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | 6726 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | 6798 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | 6822 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | 6863 | Exact free transport |
| `thm:spectral-conditional-strictification` | `theorem` | 6897 | Conditional strictification criterion |

#### `chapters/examples/yangians_foundations.tex` (42)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 229 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 316 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 349 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 408 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 449 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 504 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 568 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 1041 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1166 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1210 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1320 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1424 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1442 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1472 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1534 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 1598 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 1684 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 1781 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 1851 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 1920 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 1957 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2013 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2073 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2134 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2233 | Standard type-A fundamental line operator has the expected local residue |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | 2656 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | 2683 | Stabilized completed bar/cobar recovery |
| `cor:shifted-rtt-tower-convergence` | `corollary` | 2714 | Automatic tower convergence |
| `thm:shifted-rtt-mc-descent` | `theorem` | 2738 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | 2826 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | 2871 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | 2919 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | 2935 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | 2965 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | 2998 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | 3032 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | 3057 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | 3129 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | 3178 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | 3204 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | 3231 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | 3253 | Kleinian associated graded at the nilpotent point |

### Part III: Connections (466)

#### `chapters/connections/bv_brst.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bv-bar-bridge` | `theorem` | 22 | Bridge theorem: BV complex = bar complex |
| `thm:qme-bar-cobar` | `theorem` | 222 | Quantum master equation as Maurer--Cartan equation |
| `thm:genus0-amplitude-bar` | `theorem` | 280 | Genus-\texorpdfstring{$0$}{0} amplitudes from bar complex |
| `thm:log-form-ghost-law` | `theorem` | 365 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 468 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 619 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `thm:bar-semi-infinite-km` | `theorem` | 715 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 819 | Anomaly duality for Kac--Moody pairs |
| `thm:bar-semi-infinite-w` | `theorem` | 910 | Bar complex = semi-infinite complex for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:virasoro-semi-infinite` | `corollary` | 996 | Virasoro bar complex = semi-infinite complex |
| `cor:anomaly-duality-w` | `corollary` | 1020 | Anomaly complementarity for \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |
| `thm:config-space-bv` | `theorem` | 1121 | Configuration space BV structure |
| `thm:bv-functor` | `theorem` | 1194 | BV functor |

#### `chapters/connections/concordance.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 279 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 293 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | 563 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 587 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 624 | Gaussian collapse for abelian input |
| `conj:operadic-complexity` | `theorem` | 1647 | Operadic complexity |
| `thm:lagrangian-complementarity` | `theorem` | 2464 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 2725 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 2967 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 3012 | Spectral discriminant --- general case |
| `comp:spectral-discriminants-standard` | `computation` | 3236 | Spectral discriminants of standard families |
| `thm:family-index` | `theorem` | 3301 | Family index theorem for genus expansions |

#### `chapters/connections/editorial_constitution.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-pbw` | `theorem` | 186 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 212 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, originally conjectured)} |
| `prop:standard-tower-mc5-reduction` | `proposition` | 533 | Standard-tower MC5 reduction after MC3 and realized MC4 |
| `cor:standard-tower-mc5-closure` | `corollary` | 621 | Standard-tower MC5 closure on the canonical Yangian locus |
| `rem:conjecture-attack-strategies` | `remark` | 954 | Conjecture-by-conjecture attack strategies |
| `prop:en-n2-recovery` | `proposition` | 1587 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1733 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1791 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1825 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1841 | Physical anomaly cancellation for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2060 | Hodge symmetry from complementarity |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 2373 | Volume~I concrete modular datum |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 97 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:feynman-bar-bridge` | `theorem` | 5 | Bridge theorem: Feynman--bar dictionary |
| `thm:ainfty-constraint-formula` | `theorem` | 218 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 323 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 362 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 389 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 425 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 443 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 464 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 511 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 570 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 926 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 958 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (40)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | 120 | Protected bulk reconstruction and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | 217 | Holographic transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | 270 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | 311 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | 364 | Scalar fixed-point rigidity and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | 477 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | 590 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | 711 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | 782 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | 914 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | 994 | The first nonlinear holographic anomaly |
| `thm:yangian-shadow-theorem` | `theorem` | 1361 | Yangian-shadow theorem |
| `thm:sphere-reconstruction` | `theorem` | 1418 | Sphere reconstruction |
| `thm:quartic-resonance-obstruction` | `theorem` | 1498 | Quartic resonance obstruction |
| `thm:collision-residue-twisting` | `theorem` | 1831 | Collision residue = universal twisting morphism |
| `thm:collision-depth-2-ybe` | `theorem` | 1887 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `thm:shadow-connection-kz` | `theorem` | 1925 | Shadow connection for affine Kac--Moody = KZ |
| `cor:shadow-connection-heisenberg` | `corollary` | 1968 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | 1989 | Shadow connection for Virasoro recovers BPZ |
| `thm:quartic-obstruction-linf` | `theorem` | 2025 | Quartic obstruction = $L_\infty$ obstruction |
| `comp:holographic-ss-sl2` | `computation` | 2109 | The $E_1$ page for $\widehat{\mathfrak{sl}}_2$ |
| `comp:holographic-ss-vir` | `computation` | 2161 | The $E_1$ page for $\mathrm{Vir}_c$ |
| `comp:holographic-ss-betagamma` | `computation` | 2205 | The $E_1$ page for $\beta\gamma$ |
| `comp:holographic-ss-w3` | `computation` | 2228 | The $E_1$ page for $\mathcal W_3$ |
| `comp:heisenberg-holographic-datum` | `computation` | 2304 | Complete holographic datum for Heisenberg |
| `comp:affine-holographic-datum` | `computation` | 2327 | Holographic datum for affine Kac--Moody |
| `comp:kz-from-graph-sum` | `computation` | 2367 | Derivation of the KZ connection from the graph-sum formula |
| `comp:sl3-genus1-hessian` | `computation` | 2458 | Genus-$1$ Hessian for $\widehat{\mathfrak{sl}}_3$ |
| `comp:virasoro-holographic-datum` | `computation` | 2514 | Holographic datum for Virasoro |
| `comp:betagamma-holographic-datum` | `computation` | 2609 | Holographic datum for $\beta\gamma$ |
| `comp:w3-holographic-datum` | `computation` | 2643 | Holographic datum for $\mathcal W_3$ |
| `thm:ds-central-charge-additivity` | `theorem` | 2763 | Central charge additivity under DS |
| `cor:critical-dimensions` | `corollary` | 2864 | Critical dimensions |
| `prop:finite-jet-rigidity-frontier` | `proposition` | 2975 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | 2999 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | 3035 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | 3060 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | 3172 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | 3308 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | 3483 | Transport propagation lemma |

#### `chapters/connections/genus_complete.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 235 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 290 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 372 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 648 | Bar complex computes moduli integrals |
| `thm:full-modular-invariant-hierarchy` | `theorem` | 1131 | The full modular invariant hierarchy |
| `prop:hs-trace-class` | `proposition` | 1292 | Closed amplitudes are trace class |
| `thm:general-hs-sewing` | `theorem` | 1307 | General HS-sewing criterion |
| `cor:hs-sewing-standard-landscape` | `corollary` | 1339 | Standard landscape |
| `thm:heisenberg-one-particle-sewing` | `theorem` | 1378 | Heisenberg: one-particle sewing |
| `prop:analytic-conilpotency` | `proposition` | 1447 | Positive grading implies conilpotency |

#### `chapters/connections/kontsevich_integral.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-weight-systems` | `theorem` | 108 | Bar complex weight systems |
| `prop:propagator-restriction` | `proposition` | 177 | Propagator restriction |
| `prop:kz-from-bar` | `proposition` | 263 | KZ connection from bar complex |
| `thm:drinfeld-associator-bar` | `theorem` | 306 | Drinfeld associator from bar-cobar |

#### `chapters/connections/outlook.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `conj:operadic-complexity` | `theorem` | 228 | Operadic complexity |

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

#### `chapters/connections/thqg_fredholm_partition_functions.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-X-sewing-filtration` | `proposition` | 192 | Sewing envelope: conformal weight filtration |
| `lem:thqg-X-sewing-schatten` | `lemma` | 330 | Schatten class properties of $\sewop_q$ |
| `lem:thqg-X-composition-decay` | `lemma` | 444 | Exponential decay of composition coefficients |
| `prop:thqg-X-second-quantization` | `proposition` | 482 | Second quantization |
| `thm:thqg-X-heisenberg-sewing-full` | `theorem` | 562 | Heisenberg sewing theorem: full development |
| `thm:thqg-X-genus-1-fredholm` | `theorem` | 862 | Genus-1 Fredholm determinant |
| `comp:thqg-X-genus-1-series` | `computation` | 965 | Genus-1 Fredholm determinant: explicit series |
| `thm:thqg-X-genus-2-fredholm` | `theorem` | 1010 | Genus-2 Fredholm determinant |
| `comp:thqg-X-genus-2-series` | `computation` | 1118 | Genus-2 Fredholm determinant: leading terms |
| `thm:thqg-X-genus-3-fredholm` | `theorem` | 1145 | Genus-3 Fredholm determinant |
| `thm:thqg-X-general-genus-fredholm` | `theorem` | 1265 | General-genus Fredholm structure |
| `prop:thqg-X-free-energy-ahat` | `proposition` | 1339 | Free energy: $\hat{A}$-genus verification |
| `thm:thqg-X-class-G-fredholm` | `theorem` | 1411 | Fredholm partition function for class-G algebras |
| `prop:thqg-X-rank-additivity` | `proposition` | 1506 | Rank additivity |
| `thm:thqg-X-feynman-expansion` | `theorem` | 1573 | Feynman integral expansion |
| `prop:thqg-X-class-L-feynman` | `proposition` | 1636 | Class-L Feynman integrals |
| `prop:thqg-X-class-C-quartic` | `proposition` | 1730 | Class-C quartic contact |
| `prop:thqg-X-virasoro-decomposition` | `proposition` | 1814 | Virasoro: Fredholm base + corrections |
| `prop:thqg-X-analytic-bar-bounded` | `proposition` | 1910 | Analytic bar differential is bounded |
| `prop:thqg-X-analytic-coproduct` | `proposition` | 1938 | Analytic coproduct |
| `prop:thqg-X-coderived-fredholm-G` | `proposition` | 2018 | Coderived = Fredholm for class~G |

#### `chapters/connections/thqg_gravitational_complexity.tex` (40)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-two-sources` | `proposition` | 70 | Two sources of gravitational obstruction |
| `thm:thqg-complexity-controls-bulk` | `theorem` | 174 | Gravitational complexity controls bulk vertices |
| `prop:thqg-depth-qi-invariant` | `proposition` | 207 | Shadow depth is a quasi-isomorphism invariant |
| `lem:thqg-cubic-source` | `lemma` | 234 | Cubic source permanence |
| `thm:thqg-four-class` | `theorem` | 268 | Four-class complexity classification |
| `thm:thqg-grav-content` | `theorem` | 365 | Gravitational content of the four classes |
| `thm:thqg-gaussian-termination` | `theorem` | 420 | Gaussian termination |
| `cor:thqg-gaussian-potential` | `corollary` | 440 | Gaussian complementarity potential |
| `thm:thqg-lie-termination` | `theorem` | 484 | Lie termination |
| `thm:thqg-contact-termination` | `theorem` | 549 | Contact termination |
| `prop:thqg-cubic-gauge` | `proposition` | 583 | Cubic gauge triviality mechanism |
| `thm:thqg-virasoro-quintic` | `theorem` | 611 | Virasoro quintic obstruction |
| `thm:thqg-virasoro-infinite` | `theorem` | 646 | Virasoro shadow tower is infinite |
| `thm:thqg-virasoro-tower-explicit` | `theorem` | 689 | Virasoro shadow tower through septic order |
| `prop:thqg-virasoro-structure` | `proposition` | 765 | Structural properties of the Virasoro tower |
| `thm:thqg-virasoro-potential` | `theorem` | 817 | Virasoro complementarity potential |
| `thm:thqg-genus1-hessian` | `theorem` | 864 | Genus-$1$ Hessian correction |
| `cor:thqg-virasoro-genus1` | `corollary` | 880 | Virasoro genus-$1$ Hessian |
| `thm:thqg-genus2-diagnostic` | `theorem` | 916 | Genus-$2$ binary diagnostic |
| `thm:thqg-obstruction-table` | `theorem` | 979 | Complete obstruction data through arity~$6$ |
| `thm:thqg-vanishing-mechanisms` | `theorem` | 1053 | Classification of vanishing mechanisms |
| `thm:thqg-independent-sum` | `theorem` | 1093 | Independent sum factorization |
| `prop:thqg-depth-koszulness-independent` | `proposition` | 1125 | Depth and Koszulness are independent |
| `prop:thqg-duality-preserves-complexity` | `proposition` | 1163 | Complexity is a Koszul duality invariant |
| `cor:thqg-duality-table` | `corollary` | 1176 | Duality-complexity table |
| `prop:thqg-tropical-profiles` | `proposition` | 1214 | Tropical profiles |
| `thm:thqg-holographic-type` | `theorem` | 1251 | Holographic type from complexity |
| `prop:thqg-wn-stabilization` | `proposition` | 1300 | $\mathcal{W}_N$ complexity stabilises |
| `thm:thqg-grav-landscape` | `theorem` | 1329 | Gravitational complexity census |
| `thm:thqg-g2-main` | `maintheorem` | 1377 | Gravitational complexity; result (G2) |
| `prop:thqg-complexity-functor` | `proposition` | 1421 | Functoriality of complexity |
| `prop:thqg-coefficient-asymptotics` | `proposition` | 1496 | Coefficient asymptotics |
| `prop:thqg-generic-constancy` | `proposition` | 1565 | Generic constancy |
| `thm:thqg-mc-euler-lagrange` | `theorem` | 1620 | MC equation = Euler--Lagrange equation |
| `thm:thqg-holographic-ss` | `theorem` | 1721 | Holographic spectral sequence |
| `prop:thqg-collapse-criteria` | `proposition` | 1755 | Collapse criteria by complexity class |
| `prop:thqg-e1-virasoro` | `proposition` | 1809 | $E_1$ page for Virasoro |
| `prop:thqg-collapse-L` | `proposition` | 1856 | Collapse for class~$\mathbf{L}$ |
| `prop:thqg-collapse-C` | `proposition` | 1880 | Collapse for class~$\mathbf{C}$ |
| `prop:thqg-curve-independence` | `proposition` | 1925 | Curve independence |

#### `chapters/connections/thqg_gravitational_s_duality.tex` (42)

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
| `thm:thqg-IV-local-system-duality` | `theorem` | 828 | Local system duality |
| `prop:thqg-IV-monodromy-duality` | `proposition` | 862 | Monodromy eigenvalue reciprocation |
| `prop:thqg-IV-heisenberg-K` | `proposition` | 942 | Heisenberg complementarity |
| `thm:thqg-IV-km-K` | `theorem` | 969 | Affine Kac--Moody complementarity |
| `prop:thqg-IV-bc-bg-K` | `proposition` | 1047 | \texorpdfstring{$bc$--$\beta\gamma$}{bc-betagamma} complementarity |
| `prop:thqg-IV-lattice-K` | `proposition` | 1081 | Lattice complementarity |
| `thm:thqg-IV-virasoro-K` | `theorem` | 1098 | Virasoro complementarity |
| `thm:thqg-IV-w-K` | `theorem` | 1148 | Principal $\mathcal{W}$-algebra complementarity |
| `prop:thqg-IV-conductor-growth` | `proposition` | 1227 | Koszul conductor asymptotics |
| `thm:thqg-IV-exponent-sum` | `theorem` | 1246 | Exponent sum formula |
| `thm:thqg-IV-c26` | `theorem` | 1330 | The $c = 26$ degeneration |
| `prop:thqg-IV-c13` | `proposition` | 1384 | The $c = 13$ self-dual point |
| `thm:thqg-IV-critical-degeneration` | `theorem` | 1427 | Critical-level degeneration |
| `prop:thqg-IV-self-dual-classification` | `proposition` | 1478 | Classification of self-dual points |
| `thm:thqg-IV-four-facets` | `theorem` | 1550 | Four-facet decomposition |
| `thm:thqg-IV-free-energy` | `theorem` | 1620 | Free energy complementarity |
| `cor:thqg-IV-self-dual-generating` | `corollary` | 1649 | Self-dual generating function |
| `prop:thqg-IV-partition-duality` | `proposition` | 1655 | Partition function functional equation |
| `prop:thqg-IV-holographic-datum` | `proposition` | 1736 | Holographic modular Koszul datum under $S$-duality |
| `prop:thqg-IV-naturality` | `proposition` | 1805 | Naturality of $\mathcal{S}$ |
| `prop:thqg-IV-clutching` | `proposition` | 1822 | Clutching compatibility |
| `prop:thqg-IV-spectral-duality` | `proposition` | 1914 | Spectral sequence duality |
| `cor:thqg-IV-e2-duality` | `corollary` | 1933 | $E_2$ duality |
| `cor:thqg-IV-degeneration` | `corollary` | 1940 | Degeneration preservation |
| `thm:thqg-IV-cc-sum` | `theorem` | 2005 | Central charge sum |

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
| `prop:thqg-V-gravitational-propagator` | `proposition` | 843 | Gravitational propagator from collision residue |
| `thm:thqg-V-cybe-from-arnold` | `theorem` | 987 | CYBE from the Arnold relation via MC |
| `cor:thqg-V-ibr` | `corollary` | 1114 | Infinitesimal braid relation |
| `prop:thqg-V-ainfty-ybe` | `proposition` | 1158 | $A_\infty$-enhancement of the CYBE |
| `prop:thqg-V-n-point-ybe-proof` | `proposition` | 1235 | $n$-point YBE from boundary of $\overline{\mathcal{M}}_{0,n+1}$ |
| `prop:thqg-V-yangian-differential` | `proposition` | 1353 | Differential structure |
| `thm:thqg-V-pro-mc-element` | `theorem` | 1395 | The pro-MC element $R^{\mathrm{mod}}_\cA$ |
| `cor:thqg-V-genus-zero-r` | `corollary` | 1450 | Genus-$0$ component = classical $r$-matrix |
| `cor:thqg-V-genus-one-correction` | `corollary` | 1463 | Genus-$1$ correction |
| `prop:thqg-V-pro-mc-convergence` | `proposition` | 1560 | Convergence of the pro-MC element |
| `prop:thqg-V-rtt-from-sgybe` | `proposition` | 1633 | RTT relation from the sgYBE |
| `comp:thqg-V-three-graviton` | `computation` | 1793 | Three-graviton vertex |
| `comp:thqg-V-quartic-graviton` | `computation` | 1834 | Quartic graviton vertex and contact invariant |
| `prop:thqg-V-verma-gravitational` | `proposition` | 1894 | Verma modules as gravitational representations |
| `prop:thqg-V-c13-self-duality` | `proposition` | 1966 | Self-duality of the gravitational Yangian at $c = 13$ |
| `thm:thqg-V-mc3-thick-generation` | `theorem` | 2095 | MC3 thick generation via the gravitational Yangian |
| `cor:thqg-V-dk5-type-a` | `corollary` | 2160 | DK-5 accessibility in type A |
| `comp:thqg-V-heis-yangian` | `computation` | 2325 | Gravitational Yangian of Heisenberg |
| `comp:thqg-V-affine-yangian` | `computation` | 2344 | Gravitational Yangian of affine KM |
| `comp:thqg-V-vir-yangian-summary` | `computation` | 2366 | Gravitational Yangian of $\mathrm{Vir}_c$ |

#### `chapters/connections/thqg_holographic_reconstruction.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:obstruction-extension-sequence` | `proposition` | 133 | Obstruction-extension sequence |
| `thm:shadow-depth-dichotomy` | `theorem` | 205 | Shadow depth dichotomy |
| `cor:mittag-leffler-shadow-tower` | `corollary` | 311 | Mittag--Leffler for the shadow tower |
| `thm:gaussian-rmax-two` | `theorem` | 409 | $r_{\max}(\mathcal{H}_k) = 2$ |
| `thm:lie-rmax-three` | `theorem` | 539 | $r_{\max}(\widehat{\mathfrak{g}}_k) = 3$ |
| `thm:contact-rmax-four` | `theorem` | 743 | $r_{\max}(\beta\gamma) = 4$ |
| `thm:virasoro-rmax-infinity` | `theorem` | 898 | $r_{\max}(\mathrm{Vir}_c) = \infty$ |
| `comp:virasoro-tower-data` | `computation` | 922 | Virasoro tower data |
| `comp:virasoro-jet-dimensions` | `computation` | 1153 | Virasoro jet space dimensions |
| `thm:jet-space-polynomial-growth` | `theorem` | 1239 | Polynomial growth of Virasoro jet spaces |
| `prop:virasoro-shadow-coefficients` | `proposition` | 1324 | Virasoro shadow coefficients |
| `cor:shadow-asymptotic-decay` | `corollary` | 1377 | Asymptotic shadow decay |
| `comp:virasoro-shadow-table` | `computation` | 1422 | Virasoro shadow coefficients through arity~$10$ |
| `prop:wn-class-m` | `proposition` | 1541 | $\Walg_N$ is class~\textbf{M} for $N \geq 2$ |
| `prop:postnikov-filtration-structure` | `proposition` | 1602 | Structure of the Postnikov filtration |
| `prop:mc-formal-moduli` | `proposition` | 1647 | The MC moduli as a formal moduli problem |
| `thm:holographic-reconstruction` | `theorem` | 1692 | Holographic reconstruction theorem |
| `prop:shapovalov-shadow-singularities` | `proposition` | 1821 | Shapovalov singularities of the shadow tower |
| `prop:pole-structure-shadow-series` | `proposition` | 1858 | Pole structure of the full shadow series |
| `comp:shapovalov-zeros-shadow` | `computation` | 1913 | Shapovalov zeros and shadow singularities |
| `thm:complexity-hierarchy` | `theorem` | 1995 | Complexity hierarchy |

#### `chapters/connections/thqg_introduction_supplement_body.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `conj:thqg-intro-operadic-complexity` | `theorem` | 817 | Operadic complexity; ; Theorem~\ref{conj:operadic-complexity} |

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
| `thm:thqg-VII-one-loop-gravity` | `theorem` | 2500 | One-loop gravity from genus-$1$ MC |
| `thm:thqg-VII-g-loop-amplitude` | `theorem` | 2540 | The $g$-loop gravitational amplitude |
| `thm:thqg-VII-non-renormalization` | `theorem` | 2587 | Non-renormalization from the MC recursion |
| `prop:thqg-VII-complexity-bounds` | `proposition` | 2667 | Complexity bounds on gravitational amplitudes |
| `thm:thqg-VII-depth-classification` | `theorem` | 2769 | Shadow depth classifies gravitational theories |

#### `chapters/connections/thqg_perturbative_finiteness.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:thqg-I-completeness` | `lemma` | 64 | Completeness and separability |
| `prop:thqg-I-inclusion-maps` | `proposition` | 74 | Inclusion maps |
| `lem:thqg-I-schatten` | `lemma` | 115 | Schatten class hierarchy |
| `prop:thqg-I-uniform-trace-bound` | `proposition` | 355 | Uniform bound on the trace |
| `cor:thqg-I-genus-g-partition` | `corollary` | 369 | Genus-$g$ partition function |
| `thm:thqg-I-absolute-convergence` | `theorem` | 522 | Absolute convergence of the generating function |
| `prop:thqg-I-Fg-values` | `proposition` | 555 | Shadow free energies through genus $10$ |
| `prop:thqg-I-partial-sums` | `proposition` | 619 | Cumulative partial sums |
| `thm:thqg-I-perturbative-finiteness` | `theorem` | 675 | Perturbative finiteness of twisted gravity |
| `prop:thqg-I-koszulness-finiteness` | `proposition` | 724 | Koszulness and finiteness |
| `prop:thqg-I-graph-count` | `proposition` | 747 | Effective graph count |
| `prop:thqg-I-genus-g-decomposition` | `proposition` | 763 | Genus-$g$ amplitude decomposition |
| `prop:thqg-I-exponential-rep` | `proposition` | 898 | Exponential representation |
| `prop:thqg-I-heisenberg-detail` | `proposition` | 974 | Heisenberg: detailed HS verification |
| `prop:thqg-I-affine-detail` | `proposition` | 992 | Affine Kac--Moody: detailed HS verification |
| `prop:thqg-I-virasoro-detail` | `proposition` | 1011 | Virasoro: detailed HS verification |
| `prop:thqg-I-convergence-radii` | `proposition` | 1032 | Convergence radii of the scalar partition function |
| `thm:thqg-I-btz` | `theorem` | 1149 | BTZ partition function from shadow theory |
| `prop:thqg-I-btz-higher-genus` | `proposition` | 1174 | Higher-genus BTZ corrections |
| `prop:thqg-I-1c-expansion` | `proposition` | 1240 | Leading gravitational coupling expansion |
| `prop:thqg-I-newton-expansion` | `proposition` | 1254 | Newton's constant expansion |
| `prop:thqg-I-graph-sum-sewing` | `proposition` | 1374 | Graph-sum representation of sewing amplitudes |
| `prop:thqg-I-graph-sum-convergence` | `proposition` | 1394 | Convergence of the graph sum at fixed genus |
| `prop:thqg-I-consistency` | `proposition` | 1420 | Consistency of algebraic and analytic finiteness |
| `thm:thqg-I-full-convergence` | `theorem` | 1441 | Full partition function convergence |
| `prop:thqg-I-hs-filtration` | `proposition` | 1516 | HS-sewing and the strong filtration |
| `prop:thqg-I-effective-bound` | `proposition` | 1538 | Effective bound on the genus-$g$ free energy |
| `cor:thqg-I-tail-bound` | `corollary` | 1558 | Tail bound for the genus expansion |
| `thm:thqg-I-2d-convergence` | `theorem` | 1594 | Two-dimensional convergence |
| `cor:thqg-I-heisenberg-selberg` | `corollary` | 1676 | Heisenberg partition function via Selberg zeta |
| `prop:thqg-I-pole-structure` | `proposition` | 1732 | Pole structure of the meromorphic continuation |
| `prop:thqg-I-tensor-product` | `proposition` | 1838 | Finiteness for tensor-product theories |
| `comp:thqg-I-fp-detailed` | `computation` | 1893 | Faber--Pandharipande coefficients through genus $15$ |
| `prop:thqg-I-asymptotic-precision` | `proposition` | 1928 | Asymptotic precision |
| `prop:thqg-I-fp-monotone` | `proposition` | 1944 | Monotonicity of the FP coefficients |

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

#### `chapters/connections/thqg_symplectic_polarization.tex` (17)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:thqg-III-ambient-properties` | `proposition` | 123 | Properties of the holographic ambient complex |
| `prop:thqg-III-involutivity` | `proposition` | 234 | Involutivity and anti-symmetry |
| `prop:thqg-III-mc-compatibility` | `proposition` | 294 | Compatibility with the modular MC element |
| `lem:thqg-III-nondegeneracy` | `lemma` | 382 | Nondegeneracy of the holographic pairing |
| `prop:thqg-III-degree-shift` | `proposition` | 415 | Degree shift at each genus |
| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 468 | Holographic eigenspace decomposition (C1) |
| `cor:thqg-III-complementarity-exchange` | `corollary` | 649 | Complementarity exchange principle |
| `cor:thqg-III-dimension-parity` | `corollary` | 672 | Dimension parity |
| `prop:thqg-III-genus-0` | `proposition` | 688 | Genus-$0$ complementarity |
| `prop:thqg-III-genus-1` | `proposition` | 713 | Genus-$1$ complementarity |
| `thm:thqg-III-bv-lagrangian` | `theorem` | 895 | BV Lagrangian polarization |
| `prop:thqg-III-compatibility` | `proposition` | 1148 | Compatibility of the two symplectic structures |
| `thm:thqg-III-genus-1-holographic` | `theorem` | 1494 | Holographic complementarity at genus $1$ |
| `thm:thqg-III-landscape-census` | `theorem` | 1764 | Standard landscape complementarity census |
| `prop:thqg-III-genus-2` | `proposition` | 1927 | Genus-$2$ complementarity dimensions |
| `prop:thqg-III-independent-sum` | `proposition` | 1968 | Independent sum factorization |
| `thm:thqg-III-universality` | `theorem` | 2069 | Universality of the complementarity package |

#### `chapters/connections/twisted_holography_quantum_gravity.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:thqg-g1-finiteness` | `theorem` | 120 | \textbf{G1}: Perturbative finiteness |
| `thm:thqg-g2-complexity` | `theorem` | 131 | \textbf{G2}: Gravitational complexity |
| `thm:thqg-g3-polarization` | `theorem` | 148 | \textbf{G3}: Symplectic polarization |
| `thm:thqg-g4-s-duality` | `theorem` | 158 | \textbf{G4}: Gravitational $S$-duality |
| `thm:thqg-g5-yangian` | `theorem` | 168 | \textbf{G5}: Gravitational Yangian |
| `thm:thqg-g6-soft-graviton` | `theorem` | 178 | \textbf{G6}: Soft graviton theorems |
| `thm:thqg-g7-bootstrap` | `theorem` | 201 | \textbf{G7}: Modular bootstrap |
| `thm:thqg-g8-reconstruction` | `theorem` | 218 | \textbf{G8}: Holographic reconstruction |
| `thm:thqg-g9-critical-string` | `theorem` | 235 | \textbf{G9}: Critical string dichotomy |
| `thm:thqg-g10-fredholm` | `theorem` | 253 | \textbf{G10}: Fredholm partition functions |
| `thm:thqg-dependency` | `theorem` | 270 | Dependency theorem |

#### `chapters/connections/ym_boundary_theory.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ym-bar-bridge` | `theorem` | 58 | Bridge theorem: boundary chiral algebra $\to$ mass-gap criterion via bar-cobar |
| `thm:grand-synthesis-principle` | `theorem` | 128 | Grand synthesis principle |
| `thm:twisted-ym-boundary-brst` | `theorem` | 221 | Boundary BRST recovery for twisted Yang--Mills data |
| `thm:twisted-ym-tangent-center` | `theorem` | 246 | Tangent-to-center principle |
| `cor:twisted-ym-center-rigidity` | `corollary` | 265 | Center-vanishing rigidity criterion |
| `cor:twisted-ym-one-parameter` | `corollary` | 275 | One-parameter criterion |
| `thm:twisted-ym-tangent-factors-through-center` | `theorem` | 297 | The tangent functor factors through the dual center |
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
| `prop:internal-screening-form` | `proposition` | 616 | Operator-algebraic meaning of the screening form |
| `thm:mass-gap-reduction-internal-screening` | `theorem` | 692 | Mass-gap reduction to an internal screening estimate |
| `cor:exact-reduction-screening-estimate` | `corollary` | 726 | Exact formulation of the reduction principle |

### Appendices (267)

#### `appendices/arnold_relations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:operadic-equivalence-arnold` | `proposition` | 58 | Operadic equivalence: Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d^2 = 0$}{d\textasciicircum 2 = 0} |
| `thm:bar-d-squared-arnold` | `theorem` | 77 | Bar differential squares to zero |
| `cor:bar-d-squared-zero-arnold` | `corollary` | 149 | Bar differential squares to zero |
| `thm:arnold-iff-nilpotent` | `theorem` | 165 | Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d_{\text{residue}}^2 = 0$}{d\_residue\textasciicircum 2 = 0} |
| `thm:config-boundary-relations` | `theorem` | 363 | Configuration space boundary relations |
| `cor:dres-squared-global` | `corollary` | 486 | \texorpdfstring{$d_{\mathrm{res}}^2 = 0$}{d\_res\textasciicircum 2 = 0} globally |

#### `appendices/branch_line_reductions.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:scalar-mc-skeleton` | `proposition` | 142 | The scalar shadow is an abelian MC element |
| `thm:spectral-cumulant-hierarchy` | `theorem` | 201 | Spectral cumulant hierarchy |
| `thm:first-obstruction-traceless-quadratic` | `theorem` | 283 | First obstruction is traceless and quadratic |
| `cor:filtered-lift-vanishing` | `corollary` | 356 | Vanishing criterion for filtered lifts |
| `lem:positive-weight-contraction` | `lemma` | 424 | Positive-weight contraction |
| `thm:vir-positive-weight-acyclic` | `theorem` | 441 | Positive-weight Virasoro sectors are acyclic |
| `cor:vir-localization-reduced-spectral` | `corollary` | 460 | Localization to reduced spectral sectors |
| `prop:odd-sheet-rigidity` | `proposition` | 488 | Odd-sheet rigidity for one-line reductions |
| `cor:mu2-centered-at-13` | `corollary` | 529 | The genus-\(2\) one-line coefficient is centered at \texorpdfstring{$13$}{13} |
| `lem:universal-branch-moments` | `lemma` | 592 | Universal branch moments |
| `thm:hodge-depth-formula` | `theorem` | 654 | Depth formula |
| `lem:separating-hodge-splitting` | `lemma` | 687 | Separating Hodge splitting |
| `lem:nonseparating-hodge-extension` | `lemma` | 729 | Nonseparating Hodge extension |
| `thm:genus-two-transparency` | `theorem` | 768 | Genus-\(2\) transparency on a one-line branch quotient |
| `cor:vir-genus-two-vanishing` | `corollary` | 812 | Virasoro genus-\(2\) coefficient vanishes in the one-line quotient |
| `cor:first-primitive-genus-three` | `corollary` | 824 | The first primitive traceless coefficient begins in genus \texorpdfstring{$3$}{3} |
| `lem:genus-three-rose-unique` | `lemma` | 842 | Uniqueness of the primitive rose in genus \texorpdfstring{$3$}{3} |
| `thm:pure-branch-primitive-coefficient` | `theorem` | 872 | Pure-branch primitive coefficient on a rank-two sheet |
| `thm:first-primitive-top-hodge-layer` | `theorem` | 967 | First primitive top-Hodge layer |
| `cor:genus-three-primitive-top-hodge` | `corollary` | 1004 | The genus-\(3\) primitive coefficient |
| `cor:shared-sheet-universal-coefficients` | `corollary` | 1076 | Universal coefficients on the shared sheet |

#### `appendices/casimir_divisor_core_transport.tex` (27)

| Label | Env | Line | Title |
|---|---|---:|---|
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:72` | `proposition` | 72 | Universal property |
| `thm:divisor-core-calculus` | `theorem` | 115 | Divisor-core calculus |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:196` | `corollary` | 196 | Divisors classify submodules |
| `thm:hom-equals-gcd` | `theorem` | 218 | Hom \(=\) gcd |
| `thm:factorization-through-common-core` | `theorem` | 280 | Universal factorization through the maximal common core |
| `cor:spectral-defects` | `corollary` | 317 | Spectral defects |
| `thm:primary-jordan-filtration` | `theorem` | 356 | Primary Jordan filtration |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:393` | `corollary` | 393 | Repeated roots are extension data |
| `thm:squarefree-sheet` | `theorem` | 417 | Squarefree spectral sheet theorem |
| `prop:coprime-functional-calculus` | `proposition` | 444 | Coprime-locus functional calculus |
| `prop:no-projector` | `proposition` | 473 | No universal polynomial projector off the coprime locus |
| `thm:minimal-intrinsic-realization` | `theorem` | 546 | Minimal intrinsic realization |
| `lem:generic-separator` | `lemma` | 594 | Generic Casimir separator |
| `thm:casimir-moment-reconstruction` | `theorem` | 620 | Casimir moment reconstruction |
| `cor:finite-scalar-probes` | `corollary` | 671 | Finite scalar probes suffice |
| `thm:pbw-recurrence` | `theorem` | 751 | PBW recurrence theorem |
| `thm:growth-mode-factorization` | `theorem` | 874 | Growth-mode factorization |
| `cor:growth-ds-divisor-cores` | `corollary` | 937 | Divisor-core interpretation of the factorization |
| `thm:sector-determinant` | `theorem` | 1016 | Characteristic polynomial of a sector |
| `thm:common-core-exact-sequences` | `theorem` | 1065 | Common-core exact sequences |
| `prop:transport-factors-through-common-core` | `proposition` | 1089 | Shift-compatible transport factors through the common core |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1112` | `corollary` | 1112 | Corrected transport principle |
| `prop:squarefree-common-sector` | `proposition` | 1122 | Squarefree common-sector rigidity |
| `prop:sl3-w3-defect` | `proposition` | 1204 | Exact defect decomposition for \(\widehat{\mathfrak{sl}}_3/W_3\) |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1226` | `corollary` | 1226 | All transport maps factor through the quadratic core |
| `prop:explicit-sl3-projectors` | `proposition` | 1245 | Explicit coprime-locus projectors |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1325` | `proposition` | 1325 | The \(L_1\)--\(L_2\) package on the one-channel squarefree locus |

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
| `prop:virasoro-pade` | `proposition` | 846 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dg_shifted_factorization_bridge.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-additive-kz` | `theorem` | 147 | Derived additive KZ connection |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:203` | `corollary` | 203 | Derived Drinfeld--Kohno shadow |
| `thm:boundary-residue` | `theorem` | 213 | Boundary residue theorem |
| `thm:transfer-flat-spectral` | `theorem` | 255 | Transfer of flat spectral connections |
| `thm:quasi-factorization` | `theorem` | 322 | Quasi-factorization theorem |
| `thm:strictification-spectral-cohomology` | `theorem` | 381 | Strictification by spectral cohomology |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:426` | `proposition` | 426 | Quadratic hexagon obstruction |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:455` | `proposition` | 455 | Three-particle obstruction identity |
| `thm:abelian-strictification` | `theorem` | 493 | Abelian strictification theorem |
| `thm:residue-bounded-completion` | `theorem` | 513 | Residue-bounded completion theorem |
| `prop:cartan-shift-cocycle` | `proposition` | 566 | Cartan shift cocycle identities |
| `thm:cartan-gauge-twist` | `theorem` | 584 | Cartan gauge-twist theorem |
| `thm:cartan-diagonal-defect-exact` | `theorem` | 627 | Cartan-diagonal shift defect is exact |
| `thm:triangle-localization` | `theorem` | 699 | Triangle localization formula |
| `thm:adjacent-root-rigidity` | `theorem` | 761 | Adjacent-root rigidity |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:780` | `corollary` | 780 | Normalized rational triangle coefficient |
| `prop:triangle-shift-transport` | `proposition` | 825 | Triangle shift transport law |
| `lem:free-closed-generating-kernel` | `lemma` | 876 | Closed generating kernel |
| `thm:exact-free-transport` | `theorem` | 906 | Exact free two-body transport |
| `lem:class3-ordered-bch` | `lemma` | 980 | Class-$3$ ordered BCH coefficient |
| `thm:quadrilateral-localization` | `theorem` | 1015 | Quadrilateral localization formula |
| `thm:quadrilateral-rigidity` | `theorem` | 1107 | Quadrilateral rigidity |
| `cor:quadrilateral-normalized-rational` | `corollary` | 1135 | Normalized rational quadrilateral coefficient |
| `prop:quadrilateral-shift-transport` | `proposition` | 1171 | Quadrilateral shift transport law |
| `cor:no-new-filtration3-shift-obstruction` | `corollary` | 1201 | No new independent shift obstruction in filtration $3$ |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:1236` | `theorem` | 1236 | Conditional strictification criterion |

#### `appendices/dual_methodology.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-infty-operads` | `theorem` | 158 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |

#### `appendices/existence_criteria.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:classification-table` | `proposition` | 433 | Classification table \cite{FBZ04, BD04} |

#### `appendices/homotopy_transfer.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:sdr-existence` | `lemma` | 100 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 409 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 475 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 569 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 683 | Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0} |

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

#### `appendices/nilpotent_completion.tex` (9)

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

#### `appendices/nonlinear_modular_shadows.tex` (61)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:nms-mc-principle` | `theorem` | 186 | Algebra structure $=$ Maurer--Cartan element |
| `prop:nms-five-component` | `proposition` | 219 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | 279 | Shadow tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | 319 | All families from universal evaluation |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | 412 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | 466 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | 512 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | 521 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | 542 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | 557 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | 656 | Quartic shadow master equations |
| `thm:nms-separating-boundary-recursion` | `theorem` | 695 | Separating boundary recursion through quartic order |
| `thm:nms-shadow-cocycle-characterization` | `theorem` | 757 | Finite-order realization of the universal class |
| `prop:nms-quartic-closure-envelope` | `proposition` | 808 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | 831 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | 851 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | 875 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | 899 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | 966 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | 990 | Vanishing of the quartic contact invariant |
| `cor:nms-betagamma-boundary-law` | `corollary` | 1014 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | 1031 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | 1052 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | 1078 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | 1116 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | 1144 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | 1216 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | 1246 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `prop:nms-w3-visible-resonance-factor` | `proposition` | 1285 | Visible quartic resonance factor for \texorpdfstring{$\mathcal W_3$}{W3} |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | 1325 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | 1343 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | 1359 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | 1468 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | 1520 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 1544 | Clutching law for the modular quartic resonance class |
| `thm:nms-first-nonlinear-shadow-theta` | `theorem` | 1618 | The first nonlinear shadow of \texorpdfstring{$\Theta_{\cA}$}{ThetaA} |
| `cor:nms-family-boundary-behavior` | `corollary` | 1631 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | 1700 | Functoriality and duality through quartic order |
| `thm:nms-all-arity-master-equation` | `theorem` | 1803 | All-arity master equation |
| `cor:nms-quintic-master-equation` | `corollary` | 1826 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | 1846 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | 1865 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | 1884 | Finite termination for primitive archetypes |
| `thm:nms-all-arity-separating-boundary` | `theorem` | 1909 | All-arity separating boundary recursion |
| `cor:nms-quintic-separating-boundary` | `corollary` | 1925 | Quintic separating boundary recursion |
| `prop:nms-genus-loop-properties` | `proposition` | 1971 | Basic properties of the genus loop operator |
| `thm:nms-nonseparating-clutching-law` | `theorem` | 1988 | Non-separating clutching law for the shadow tower |
| `cor:nms-genus-one-hessian-correction` | `corollary` | 2012 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | 2036 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2119 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2153 | Ambient complementarity and nonlinear modular shadows |
| `prop:nms-nonlinear-phase-standard` | `proposition` | 2352 | Nonlinear phase of the standard families |
| `prop:nms-basis-independence-specialization-restated` | `proposition` | 2711 | Basis independence and specialization |
| `thm:nms-clutching-law-modular-resonance-restated` | `theorem` | 2739 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behaviour` | `corollary` | 2769 | Family-by-family boundary behaviour |
| `thm:nms-genus-loop-model-families-restated` | `theorem` | 2895 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat-restated` | `theorem` | 2963 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary-restated` | `theorem` | 2995 | Ambient complementarity and nonlinear modular shadows |
| `thm:reduced-weight-finiteness` | `theorem` | 3198 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | 3286 | Window locality |
| `cor:exact-stabilization` | `corollary` | 3308 | Exact stabilization |

#### `appendices/ordered_associative_chiral_kd.tex` (24)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bicom-e` | `lemma` | 217 | Bicomodules as comodules over the enveloping coalgebra |
| `thm:shuffle` | `theorem` | 300 | Ordered chiral shuffle theorem |
| `thm:opposite` | `theorem` | 405 | Opposite-duality for ordered bar coalgebras |
| `cor:anti` | `corollary` | 446 | Anti-involutions survive duality |
| `lem:closure` | `lemma` | 460 | Closure of admissibility under opposite and enveloping constructions |
| `cor:enveloping` | `corollary` | 471 | Enveloping duality |
| `lem:Kbi-dg` | `lemma` | 534 | — |
| `prop:one-defect` | `proposition` | 561 | — |
| `thm:tangent=K` | `theorem` | 583 | Tangent identification |
| `cor:infdual` | `corollary` | 620 | Infinitesimal dual coalgebra |
| `prop:infann` | `proposition` | 643 | Infinitesimal annular variation |
| `thm:bimod-bicomod` | `theorem` | 695 | PBW-complete bimodule/bicomodule equivalence |
| `thm:diagonal` | `theorem` | 728 | Diagonal correspondence |
| `cor:unit` | `corollary` | 776 | The diagonal is the unit for composition |
| `cor:tensor-cotensor` | `corollary` | 794 | Tensor--cotensor gluing |
| `thm:HH-coHH-homology` | `theorem` | 823 | Associative chiral Hochschild/coHochschild homology |
| `thm:HH-coHH-cohomology` | `theorem` | 855 | Associative chiral Hochschild/coHochschild cohomology |
| `cor:annulus` | `corollary` | 881 | The annulus as self-cotrace |
| `cor:cap` | `corollary` | 901 | Cap action |
| `thm:pair-of-pants` | `theorem` | 956 | Ordered pair-of-pants algebra |
| `thm:ordered-open` | `theorem` | 994 | Ordered genus-zero open trace formalism |
| `thm:CY` | `theorem` | 1048 | Shifted ordered Frobenius structure |
| `cor:cardy` | `corollary` | 1097 | Cardy operator on the coalgebra side |
| `thm:master` | `theorem` | 1121 | Master theorem |

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
| `thm:convergence-criterion-spectral` | `theorem` | 25 | Convergence criterion |

#### `appendices/spectral_sequences.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ss` | `theorem` | 271 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 323 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 387 | Central charge and \texorpdfstring{$d_1$}{d1} |

#### `appendices/subregular_hook_frontier.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:pbw-slodowy-collapse` | `theorem` | 66 | PBW--Slodowy collapse |
| `cor:principal-w-completed-koszul` | `corollary` | 125 | Principal affine \texorpdfstring{$W$}{W}-algebras are completed Koszul |
| `thm:hook-transport-corridor` | `theorem` | 214 | Hook-type transport corridor |
| `prop:transport-propagation` | `proposition` | 240 | Transport propagation lemma |
| `thm:canonical-arity-detection` | `theorem` | 305 | Generator-degree detection of canonical arity |
| `thm:full-raw-coefficient-packet` | `theorem` | 453 | Exact Bell recursion for the full singular packet |
| `thm:miura-product-formula` | `theorem` | 611 | Subregular Miura product formula |
| `thm:subregular-appell-formula` | `theorem` | 648 | Subregular Appell formula |
| `thm:bp-strict` | `theorem` | 720 | Bershadsky--Polyakov is strict in canonical normal form |
| `thm:w4-cubic` | `theorem` | 767 | \texorpdfstring{$\mathcal W_4^{(2)}$}{W4(2)} has canonical arity $3$ |
| `thm:unbounded-canonical-arity` | `theorem` | 898 | Unbounded canonical arity in the subregular line |
| `thm:triangular-primary-renormalization` | `theorem` | 952 | Triangular primary-renormalization theorem |

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
