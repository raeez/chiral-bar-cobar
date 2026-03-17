# Theorem Registry

Auto-generated on 2026-03-17 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 1613 |
| Total tagged claims | 2202 |
| Active files in `main.tex` | 77 |
| Total `.tex` files scanned | 83 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1613 |
| `ProvedElsewhere` | 364 |
| `Conjectured` | 208 |
| `Heuristic` | 17 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 714 |
| `proposition` | 468 |
| `corollary` | 287 |
| `lemma` | 103 |
| `computation` | 34 |
| `calculation` | 3 |
| `remark` | 3 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 14 |
| Part I: Theory | 686 |
| Part II: Examples | 507 |
| Part III: Connections | 142 |
| Appendices | 264 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 111 |
| `chapters/theory/higher_genus_modular_koszul.tex` | 94 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 83 |
| `chapters/theory/higher_genus_complementarity.tex` | 75 |
| `appendices/nonlinear_modular_shadows.tex` | 61 |
| `chapters/theory/higher_genus_foundations.tex` | 60 |
| `chapters/examples/w_algebras.tex` | 53 |
| `chapters/theory/chiral_modules.tex` | 52 |
| `chapters/theory/bar_cobar_adjunction_inversion.tex` | 48 |
| `chapters/examples/free_fields.tex` | 47 |
| `chapters/examples/kac_moody.tex` | 43 |
| `chapters/examples/yangians_foundations.tex` | 42 |
| `chapters/examples/yangians_computations.tex` | 38 |
| `chapters/examples/genus_expansions.tex` | 35 |
| `chapters/examples/lattice_foundations.tex` | 35 |
| `chapters/theory/configuration_spaces.tex` | 35 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 34 |
| `chapters/theory/chiral_koszul_pairs.tex` | 31 |
| `chapters/theory/cobar_construction.tex` | 29 |
| `chapters/theory/koszul_pair_structure.tex` | 29 |

## Complete Proved Registry

### Frame (14)

#### `chapters/frame/heisenberg_frame.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 502 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 859 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 955 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1118 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1342 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1364 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1527 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1705 | Quantum complementarity for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2310 | $\mathfrak{sl}_2$ bar complex as Swiss-cheese coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2382 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2431 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2512 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 2550 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 2818 | CS $R$-matrix from the bar complex |

### Part I: Theory (686)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 879 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 1168 | Geometric realization |
| `prop:orthogonal` | `proposition` | 1293 | Orthogonality |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (111)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:curvature-central` | `theorem` | 182 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 286 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 363 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 432 | Conilpotency ensures convergence |
| `lem:arity-cutoff` | `lemma` | 590 | Arity cutoff for strong completion towers |
| `thm:completed-bar-cobar-strong` | `theorem` | 605 | Completed bar-cobar for strong completion towers |
| `prop:mc4-reduction-principle` | `proposition` | 713 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 778 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 815 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 853 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 902 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 953 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 1016 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 1080 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 1116 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 1192 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 1289 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 1305 | Factorization-envelope criterion for principal stages |
| `cor:completion-closure-equivalence` | `corollary` | 1341 | Homotopy-categorical equivalence on the completion closure |
| `thm:coefficient-stability-criterion` | `theorem` | 1377 | Coefficient-stability criterion |
| `thm:completed-twisting-representability` | `theorem` | 1412 | Completed twisting representability |
| `thm:mc-twisting-closure` | `theorem` | 1435 | MC-twisting closure of the completion closure |
| `thm:uniform-pbw-bridge` | `theorem` | 1460 | Uniform PBW bridge from MC1 to MC4 |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 1566 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 1612 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 1647 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 1667 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 1685 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 1704 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 1746 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 1786 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 1827 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 1894 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 1937 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 1983 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 2045 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 2086 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 2158 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 2245 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 2271 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 2296 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 2350 | Stage-\texorpdfstring{$4$}{4} reduction to one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 2378 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 2415 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 2446 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 2488 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 2515 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 2545 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 2588 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 2623 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 2653 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 2670 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 2721 | MC4 completion packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 2782 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 completion |
| `cor:winfty-dual-candidate-construction` | `corollary` | 2821 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 2868 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} reduction on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 2907 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 2997 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 3028 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 3136 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 3184 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 3230 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 3257 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 3399 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 3438 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 3502 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 3557 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 3599 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 3693 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 3718 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 3757 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 3777 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 3815 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 3832 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 3855 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 3877 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 3893 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 3903 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 3919 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 3931 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 3944 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 3962 | Stage-\texorpdfstring{$5$}{5} mixed transport reduction to one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 3977 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 3996 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 4203 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 4220 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 4257 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 4297 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-conjecture-network-collapse` | `corollary` | 4593 | Visible stage-\texorpdfstring{$5$}{5} local conjecture network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 4635 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 4863 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 5101 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 5442 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 5478 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 5539 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 5551 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 5659 | Modular operad structure of the bar complex |
| `cor:genus-expansion-converges` | `corollary` | 5929 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 5989 | Functoriality of bar construction |
| `thm:reconstruction-vs-duality` | `theorem` | 6098 | Reconstruction versus duality |
| `thm:recognition-koszul-pairs` | `theorem` | 6126 | Recognition theorem for finite chiral Koszul pairs |
| `thm:mixed-boundary-sseq` | `theorem` | 6181 | Mixed-boundary spectral sequence |
| `thm:pbw-regular-tensor` | `theorem` | 6205 | PBW-regular tensor theorem |
| `thm:universal-sugawara-d1` | `theorem` | 6253 | Universal first mixed Sugawara differential |
| `cor:sugawara-universality` | `corollary` | 6282 | Universality |
| `prop:sugawara-contraction` | `proposition` | 6290 | Contractibility on positive current weight |
| `thm:sugawara-casimir-transgression` | `theorem` | 6355 | Sugawara Casimir transgression |
| `thm:casimir-transgression-homology` | `theorem` | 6371 | Homology of the minimal Casimir-transgression complex |
| `thm:casimir-quadric-rigidity` | `theorem` | 6417 | Quadric rigidity: no higher $A_\infty$~corrections |
| `thm:ci-transgression-principle` | `theorem` | 6466 | Complete-intersection transgression principle |
| `thm:gko-transgression` | `theorem` | 6510 | Diagonal GKO transgression |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (48)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 434 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 653 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 962 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 1077 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1150 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1194 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1262 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1328 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1463 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1529 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1649 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 1793 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 1809 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 1865 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 1888 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 1948 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 1993 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 2005 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 2040 | Derived equivalence |
| `lem:complete-filtered-comparison` | `lemma` | 2128 | Complete filtered comparison lemma |
| `cor:completed-derived-equivalence` | `corollary` | 2229 | Completed derived equivalence |
| `prop:bar-fh` | `proposition` | 2790 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 2868 | Cobar as factorization cohomology |
| `thm:ks-centrality` | `theorem` | 3575 | Kodaira--Spencer centrality |
| `lem:two-eta-vanishing` | `lemma` | 3618 | Two-$\eta$ vanishing |
| `prop:square-zero-insertion` | `proposition` | 3669 | Square-zero insertion differential |
| `cor:two-step-scalar-sseq` | `corollary` | 3704 | Two-step scalar spectral sequence |
| `thm:quadratic-frontier` | `theorem` | 3750 | Quadratic frontier |
| `prop:eta-hessian-transfer` | `proposition` | 3844 | Homotopy-transfer construction of the $\eta$-Hessian |
| `lem:shifted-symmetry-H` | `lemma` | 3880 | Shifted symmetry on degree-two primitives |
| `thm:admissible-scalar-rigidity` | `theorem` | 3925 | Admissible scalar rigidity |
| `cor:ds-not-first-frontier` | `corollary` | 3958 | Drinfeld--Sokolov reductions remain scalar-rigid |
| `thm:classification-scalar-genera` | `theorem` | 4000 | Classification of scalar genera |
| `thm:platonic-hierarchy-log` | `theorem` | 4067 | Five-step hierarchy of the categorical logarithm |
| `prop:cech-two-element-strict` | `proposition` | 4587 | Two-element covers are strict |
| `thm:divisor-core-calculus-inv` | `theorem` | 4914 | Divisor-core calculus |
| `cor:divisors-classify-submodules-inv` | `corollary` | 4974 | Divisors classify submodules |
| `thm:hom-equals-gcd-inv` | `theorem` | 5006 | \texorpdfstring{$\operatorname{Hom} = \gcd$}{Hom = gcd} |
| `thm:factorization-through-common-core-inv` | `theorem` | 5028 | Universal factorization through the common core |
| `thm:minimal-intrinsic-realization-inv` | `theorem` | 5126 | Minimal intrinsic realization |
| `thm:sector-determinant-inv` | `theorem` | 5174 | Sector determinant |
| `thm:casimir-moment-reconstruction-inv` | `theorem` | 5194 | Casimir moment reconstruction |
| `thm:primary-jordan-filtration-inv` | `theorem` | 5239 | Primary Jordan filtration |
| `cor:repeated-roots-extension-data` | `corollary` | 5270 | Repeated roots encode extension data |
| `thm:common-core-exact-sequences-inv` | `theorem` | 5302 | Common-core exact sequences |
| `prop:transport-factors-inv` | `proposition` | 5330 | Transport factors through the common core |
| `prop:sl3-w3-defect-inv` | `proposition` | 5397 | Exact defect decomposition |
| `prop:sl3-w3-projectors` | `proposition` | 5419 | Explicit coprime-locus projectors |

#### `chapters/theory/bar_construction.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 247 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 568 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 658 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 717 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 783 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 811 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 906 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 948 | Arnold relations |
| `comp:deg0` | `computation` | 991 | Degree 0 |
| `comp:deg1-general` | `computation` | 1009 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1122 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1161 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1167 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1199 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1222 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1289 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1340 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1357 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1444 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1470 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1494 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1558 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1633 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1695 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1805 | Bar complex is chiral |

#### `chapters/theory/chiral_hochschild_koszul.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 161 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 312 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 350 | Hochschild spectral sequence |
| `thm:main-koszul-hoch` | `theorem` | 469 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `thm:hochschild-polynomial-growth` | `theorem` | 584 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 654 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `prop:e2-formality-hochschild` | `proposition` | 695 | $\Etwo$-formality of chiral Hochschild cohomology |
| `comp:boson-hochschild` | `computation` | 1126 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 1152 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 1254 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 1348 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 1446 | Kac--Moody cyclic deformation complex |
| `prop:modular-deformation-truncation` | `proposition` | 1652 | Genus truncation |
| `thm:mc2-1-km` | `theorem` | 1724 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1841 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 2089 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 2175 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 2294 | Recovery of the Killing cocycle extension |
| `prop:modular-strictification-principle` | `proposition` | 2476 | Strictification principle for modular deformation theory |
| `prop:d-mod-squared-zero` | `proposition` | 2613 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2749 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 2924 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 3114 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 3240 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 3485 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 3631 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 3770 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 3851 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 3898 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 4190 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 4321 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 4368 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 4561 | Boson-fermion duality |
| `prop:hochschild-cech-ss` | `proposition` | 4764 | Hochschild--\v{C}ech spectral sequence |

#### `chapters/theory/chiral_koszul_pairs.tex` (31)

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
| `prop:ainfty-formality-implies-koszul` | `proposition` | 1023 | Formality implies chiral Koszulness |
| `prop:pbw-universality` | `proposition` | 1111 | PBW universality |
| `cor:universal-koszul` | `corollary` | 1137 | Universal vertex algebras are chirally Koszul |
| `thm:koszul-equivalences-meta` | `theorem` | 1208 | Equivalences of chiral Koszulness |
| `prop:cumulant-window-inversion` | `proposition` | 1513 | Cumulant-to-window inversion |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 1571 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 1736 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 1796 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 1950 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 2044 | Bar computes Koszul dual — complete statement |
| `lem:completion-convergence` | `lemma` | 2132 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 2181 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 2738 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 2956 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 3021 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 3082 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 3205 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 3247 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 3301 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 3336 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 3531 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (52)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 185 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 290 | Module Koszul equivalence |
| `thm:monoidal-module-koszul` | `theorem` | 320 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 460 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 536 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 640 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 733 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 791 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 946 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 1240 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1629 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1690 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1890 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1948 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1982 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:orbit-duality` | `proposition` | 2108 | Orbit duality for affine vertex algebras |
| `prop:logarithmic-bar` | `proposition` | 2233 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2327 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2438 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2473 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2512 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2529 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2569 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2591 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2741 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2848 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2962 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3042 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3196 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3227 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3279 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3358 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3444 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3503 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3579 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3656 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3706 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3799 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3853 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3919` | `calculation` | 3919 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3946` | `calculation` | 3946 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3977` | `calculation` | 3977 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4095 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4220 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4277 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4367 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4409 | \texorpdfstring{$\mathcal{W}$}{W}-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4464 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4506 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4636 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4775 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4885 | Heisenberg fusion splitting |

#### `chapters/theory/cobar_construction.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 196 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 257 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 290 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 372 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 448 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 562 | Verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 810 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 970 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1188 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1319 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1365 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 1638 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1686 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1707 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1753 | Topology |
| `thm:poincare-verdier` | `theorem` | 1812 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 1901 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 1926 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 1972 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 2126 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2222 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2363 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2388 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2441 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2494 | Recognition principle |
| `lem:deformation-space` | `lemma` | 2866 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 2908 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 2956 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 3035 | Curved differential formula |

#### `chapters/theory/configuration_spaces.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 309 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 419 | Normal crossings |
| `thm:closure-relations` | `theorem` | 514 | Closure relations |
| `thm:log-complex` | `theorem` | 627 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 666 | Arnold relations |
| `prop:twisting-morphism-propagator` | `proposition` | 708 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 775 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 842 | Residue operations |
| `prop:residue-local` | `proposition` | 897 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 946 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1192 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1259 | Conformal blocks from punctured bar complex |
| `prop:eta` | `proposition` | 1423 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:FM-convergence` | `theorem` | 1770 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1829 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1935 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1977 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 2004 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 2026 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 2066 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 2090 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 2125 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 2147 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 2181 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2197 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2219 | Nilpotency from Arnold relations |
| `thm:arnold-jacobi` | `theorem` | 2341 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2394 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2440 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2472 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2517 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 2748 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 2818 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 2955 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3165` | `computation` | 3165 | Explicit examples |

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
| `prop:fourier-propagator-properties` | `proposition` | 74 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 131 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 240 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 286 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 334 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 363 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 425 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 452 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 509 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 567 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 647 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 817 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 838 | — |
| `thm:fourier-specialization` | `theorem` | 873 | Specialization |
| `thm:fourier-four-properties` | `theorem` | 928 | The four properties of the Fourier transform |
| `rem:fourier-genus-preview` | `remark` | 1028 | Ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus_complementarity.tex` (75)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:involution-splitting` | `lemma` | 157 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 212 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 286 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 376 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 532 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 587 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 672 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 735 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 786 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 931 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 1004 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 1044 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 1098 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1127 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 1315 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 1350 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 1402 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 1515 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 1546 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 1566 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 1632 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 1723 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 1876 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 1944 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 2042 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 2070 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 2107 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 2150 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 2186 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 2212 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 2467 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 2648 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 2698 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 2711 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 2753 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 2812 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 2854 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 2882 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 2904 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 2948 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 3126 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 3174 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 3262 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 3289 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 3317 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 3351 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 3376 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 3436 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 3482 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 3521 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 3550 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 3574 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 3599 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 3631 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 3663 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 3689 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 3705 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 3799 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 3875 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 3923 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 4012 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | 4187 | Ambient complementarity in tangent form |
| `thm:shifted-cotangent-normal-form` | `theorem` | 4451 | Shifted cotangent normal form |
| `prop:legendre-duality-potentials` | `proposition` | 4500 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | 4515 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | 4545 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | 4569 | Criterion for fake complementarity |
| `thm:holo-comp-bulk-reconstruction` | `theorem` | 4765 | Protected bulk reconstruction |
| `thm:holo-comp-cotangent-realization` | `theorem` | 4815 | Shifted cotangent realization |
| `cor:holo-comp-spectral-reciprocity` | `corollary` | 4842 | Spectral reciprocity and palindromicity |
| `thm:holo-comp-fourier-transport` | `theorem` | 4928 | Fourier intertwining |
| `thm:holo-comp-weyl-sewing` | `theorem` | 4972 | Weyl associativity, PBW, and linear sewing |
| `thm:holo-comp-gaussian-composition` | `theorem` | 5049 | Gaussian composition via Schur complement |
| `thm:holo-comp-metaplectic-cocycle` | `theorem` | 5132 | Metaplectic $2$-cocycle and strictification |
| `cor:holo-comp-first-nonlinear-anomaly` | `corollary` | 5201 | First nonlinear holographic anomaly |

#### `chapters/theory/higher_genus_foundations.tex` (60)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:genus-g-curvature-package` | `proposition` | 273 | The genus-$g$ curvature package |
| `thm:bar-ainfty-complete` | `theorem` | 548 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 648 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 739 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 852 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 959 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 1106 | Verdier duality of operations |
| `thm:bar-curved-ch-infty` | `theorem` | 1268 | Genus-$g$ bar complex as curved $\mathrm{Ch}_\infty$-algebra |
| `thm:convergence-filtered` | `theorem` | 1346 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1555 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1589 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1623 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1643 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1659 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 1961 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 2046 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2261 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2530 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2733 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2793 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 3046 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:arnold-genus1` | `theorem` | 3105 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 3140 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 3197 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 3465 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3498 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 3625 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3728 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3782 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 3860 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 3977 | \texorpdfstring{$W_3$}{W3} obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 4048 | Explicit genus-\texorpdfstring{$1$}{1} value of the \texorpdfstring{$W_3$}{W3} obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 4069 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 4098 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 4183 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4285 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4439 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4472 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4488 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4504 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4522 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 4545 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4567 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4619 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4691 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4721 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4807 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4851 | Grothendieck--Riemann--Roch bridge |
| `lem:stable-graph-d-squared` | `lemma` | 5019 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 5081 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 5119 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 5161 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 5250 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 5338 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 5406 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 5440 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 5481 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 5538 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 5566 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 5616 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (94)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:genus-graded-koszul` | `theorem` | 120 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 151 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 483 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 516 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 557 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 693 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 960 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 985 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1182 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1234 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1334 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1384 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1446 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `lem:e2-higher-genus` | `lemma` | 1621 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 1748 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 1857 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 1963 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 1992 | Universal modular Maurer--Cartan class |
| `thm:mc2-bar-intrinsic` | `theorem` | 2130 | Bar-intrinsic MC2 |
| `cor:shadow-extraction` | `corollary` | 2289 | Shadow extraction |
| `thm:explicit-theta` | `theorem` | 2389 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 2610 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 3024 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 3103 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 3216 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 3250 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 3282 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 3478 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 3554 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 3619 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 3754 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 3851 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 3962 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 4099 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 4251 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 4425 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 4575 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 4769 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 4889 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 4988 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 5078 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 5190 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 5262 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 5344 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 5422 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 5499 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 5575 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 5650 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 5716 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 5794 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 5869 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 5916 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 5958 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 6017 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 6071 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 6104 | Scalar saturation for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 6142 | Scalar saturation persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 6195 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 6267 | Scalar saturation for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 6349 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 6521 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 6684 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 6767 | Cyclic rigidity at generic level |
| `thm:algebraic-family-rigidity` | `theorem` | 6915 | Algebraic-family rigidity |
| `cor:saturation-algebraic-families` | `corollary` | 7006 | Saturation at all non-critical levels for algebraic families |
| `thm:conformal-bootstrap-rigidity` | `theorem` | 7067 | $L_0$-bootstrap rigidity |
| `cor:one-channel-no-lie` | `corollary` | 7174 | One-channel criterion without Lie symmetry |
| `thm:tautological-line-support` | `theorem` | 7402 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 7504 | MC2 reduced to cyclic model |
| `thm:convolution-dg-lie-structure` | `theorem` | 7658 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 7723 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 8087 | Modular homotopy convolution |
| `cor:strictification-comparison` | `corollary` | 8119 | Strictification comparison |
| `prop:master-equation-from-mc` | `proposition` | 8385 | All-arity master equation from MC |
| `thm:recursive-existence` | `theorem` | 8437 | Recursive existence |
| `thm:shadow-channel-decomposition` | `theorem` | 8471 | Shadow channel decomposition |
| `cor:shadow-cauchy-schwarz` | `corollary` | 8551 | Shadow Cauchy--Schwarz inequality |
| `prop:critical-locus-complementarity` | `proposition` | 8601 | Critical-locus form of complementarity |
| `thm:theta-direct-derivation` | `theorem` | 8723 | The explicit formula: direct derivation |
| `lem:graph-sum-truncation` | `lemma` | 8918 | Graph-sum truncation criterion |
| `prop:shadow-formality-low-arity` | `proposition` | 9064 | Shadow--formality identification at low arity |
| `thm:shadow-formality-identification` | `theorem` | 9135 | Shadow tower as formality obstruction tower |
| `thm:cubic-gauge-triviality` | `theorem` | 9467 | Cubic gauge triviality and canonical quartic class |
| `prop:independent-sum-factorization` | `proposition` | 9539 | Independent sum factorization |
| `prop:genus0-curve-independence` | `proposition` | 9713 | Genus-$0$ curve-independence |
| `prop:chriss-ginzburg-structure` | `proposition` | 9901 | Chriss--Ginzburg structure principle |
| `prop:coefficient-algebras-well-defined` | `proposition` | 10240 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 10273 | Square-zero: convolution level |
| `conj:differential-square-zero` | `theorem` | 10287 | Square-zero: ambient level |
| `thm:determinantal-branch-formula` | `theorem` | 10494 | Determinantal branch formula |
| `thm:transport-lifted-covers` | `theorem` | 10530 | Transport of lifted covers |
| `thm:common-sheet-law` | `theorem` | 10561 | Common-sheet multiplication law |
| `thm:spectral-hierarchy` | `theorem` | 10625 | Hierarchy of spectral invariants |
| `cor:frontier-is-cubic` | `corollary` | 10661 | The frontier is cubic |

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

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 680 | Central charge complementarity |
| `prop:chirAss-self-dual` | `proposition` | 2145 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | 163 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 208 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 248 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 267 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 324 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 387 | \texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 446 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 575 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 669 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 684 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 788 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 910 | Maurer--Cartan correspondence — quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 1001 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1031 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1224 | Positselski comodule-contramodule equivalence |
| `thm:full-derived-module-equiv` | `theorem` | 1250 | Full derived module equivalence |
| `thm:cs-koszul-km` | `theorem` | 1367 | Chern--Simons equations from Koszul duality |
| `thm:linf-mc-flatness` | `theorem` | 1444 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan as homotopy flatness |
| `thm:cs-koszul-general` | `theorem` | 1514 | CS/Koszul for general non-quadratic algebras |
| `thm:bv-structure-bar` | `theorem` | 1702 | BV structure on bar complex |
| `thm:ordered-shuffle` | `theorem` | 1815 | Ordered chiral shuffle theorem |
| `thm:ordered-opposite` | `theorem` | 1857 | Opposite duality for ordered bar coalgebras |
| `cor:ordered-enveloping` | `corollary` | 1887 | Enveloping duality |
| `thm:ordered-bimod-bicomod` | `theorem` | 1926 | Bimodule--bicomodule equivalence |
| `thm:ordered-diagonal` | `theorem` | 1951 | Diagonal correspondence |
| `thm:ordered-HH-coHH-homology` | `theorem` | 1999 | Hochschild--coHochschild duality, homological version |
| `thm:ordered-HH-coHH-cohomology` | `theorem` | 2030 | Hochschild--coHochschild duality, cohomological version |
| `thm:ordered-pair-of-pants` | `theorem` | 2078 | Ordered pair-of-pants algebra |
| `thm:ordered-master` | `theorem` | 2102 | Master theorem: the ordered open trace formalism |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 224 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 336 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 403 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 494 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 553 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 569 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 660 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 744 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:chiral-operad-genus0` | `proposition` | 319 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 363 | Prism principle --- operadic identification |
| `thm:prism-higher-genus` | `theorem` | 572 | Prism principle --- higher-genus extension |
| `cor:prism-principle` | `corollary` | 679 | The prism principle |
| `thm:partition` | `theorem` | 830 | Partition complex structure |

#### `chapters/theory/quantum_corrections.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:two-element-strict` | `proposition` | 714 | Two-element covers are strict |
| `prop:borcherds-shadow-identification` | `proposition` | 1199 | Secondary Borcherds operations as shadow tower obstructions |

### Part II: Examples (507)

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
| `thm:betagamma-complete-bar` | `theorem` | 180 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 231 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 266 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 319 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 357 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | 378 | — |
| `thm:cobar-fermions` | `theorem` | 406 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | 443 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 531 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 798 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 918 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 1019 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1160 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1244 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1395 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |
| `thm:betagamma-quartic-birth` | `theorem` | 1829 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `cor:betagamma-postnikov-termination` | `corollary` | 1865 | $\beta\gamma$ shadow Postnikov tower: arity~$4$ on weight-changing line |
| `lem:betagamma-ell2-vanishing` | `lemma` | 1966 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | 2013 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | 2123 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | 2165 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | 2195 | Pure contact boundary law |
| `prop:betagamma-translation-coproduct` | `proposition` | 2328 | Translation and coproduct |

#### `chapters/examples/deformation_quantization.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 130 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 183 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 415 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 528 | Genus expansion |

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
| `thm:heisenberg-not-self-dual` | `theorem` | 1722 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 1827 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 1858 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2117 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 2231 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 2504 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 2653 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 2700 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 2759 | Heisenberg level inversion: curved duality |
| `thm:virasoro-moduli` | `theorem` | 2819 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 2857 | Geometric interpretation |
| `thm:virasoro-string` | `theorem` | 2936 | Virasoro-string duality |
| `thm:algebraic-string-dictionary` | `theorem` | 2972 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 3024 | Genus-\texorpdfstring{$0$}{0} string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 3066 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 3175 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 3255 | Bar complex computes genus-\texorpdfstring{$g$}{g} string integrands |
| `thm:modular-invariance` | `theorem` | 3393 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 3430 | Modular anomaly for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:wakimoto-bar` | `theorem` | 3539 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 3552 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 3557 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 3584 | Quantum integrability via \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:filtered-bar-complex` | `theorem` | 3644 | Filtered bar complex |

#### `chapters/examples/genus_expansions.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 86 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 160 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `thm:lattice-all-genera` | `theorem` | 204 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 239 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 261 | \texorpdfstring{$\mathcal{W}$}{W}-algebra free energy at all genera |
| `thm:sl2-all-genera` | `theorem` | 454 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 600 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 732 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 774 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 828 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 939 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 1049 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1189 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1256 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1321 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1407 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1539 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1569 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1586 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1621 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1692 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1820 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1862 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1941 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 2090 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2155 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:complementarity-classification` | `proposition` | 2391 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2445 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2740 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2840 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2856 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2881 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2913 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 3008 | Loop expansion interpretation |
| `thm:boundary-characters-bar-hilbert` | `theorem` | 3179 | Boundary characters as bar Hilbert series |

#### `chapters/examples/heisenberg_eisenstein.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-genus-one-complete` | `theorem` | 235 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 322 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 364 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 482 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 585 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 634 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 846 | Multi-boson Eisenstein corrections |
| `thm:heisenberg-exact-linearity` | `theorem` | 1138 | Heisenberg exact linearity |
| `cor:heisenberg-postnikov-termination` | `corollary` | 1178 | Heisenberg shadow Postnikov tower: finite termination at arity~$2$ |
| `cor:heisenberg-gaussian-boundary` | `corollary` | 1400 | Gaussian boundary law |

#### `chapters/examples/kac_moody.tex` (43)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-ope-kac-moody` | `theorem` | 327 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 361 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 401 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 467 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 596 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 627 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 665 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 723 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 759 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 828 | Universal Koszul duality for affine Kac--Moody |
| `prop:ff-channel-shear` | `proposition` | 955 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 1005 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 1071 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1135 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1174 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1228 | Closed-form OPE for Koszul dual |
| `thm:km-quantum-groups` | `theorem` | 1291 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 1617 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 1687 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 1775 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 1887 | KW formula via bar complex: general simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `prop:admissible-verlinde-bar` | `proposition` | 1957 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2196 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 2277 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 2342 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 2394 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 2460 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 2523 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 2569 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 2608 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 2645 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 2824 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 2854 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 2884 | Full derived oper identification |
| `thm:affine-cubic-normal-form` | `theorem` | 3120 | Affine cubic normal form |
| `cor:affine-postnikov-termination` | `corollary` | 3156 | Affine shadow Postnikov tower: finite termination at arity~$3$ |
| `prop:affine-cyclic-slice-data` | `proposition` | 3189 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 3237 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 3294 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 3371 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 3457 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 3493 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 3582 | Vanishing of the genus loop on the affine cubic |

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
| `prop:discriminant-characteristic` | `proposition` | 1619 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1710 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1807 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1873 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 1928 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1979 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1994 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 2083 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2272 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2578 | Spectral sequence collapse |

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
| `prop:lattice:self-dual-criterion` | `proposition` | 1462 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1479 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1504 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1706 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1890 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2515 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2583 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2657 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2816 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3119 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3200 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3370 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3566 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3609 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3767 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3814 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 3900 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 3981 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |
| `prop:lattice:genus1-simple-pole` | `proposition` | 4167 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4184 | Curvature-braiding orthogonality for quantum lattice VOAs |
| `cor:lattice-postnikov-termination` | `corollary` | 4281 | Lattice shadow Postnikov tower: termination at weight~$2$ |

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
| `prop:fay-implies-d-squared` | `proposition` | 381 | Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0} |
| `thm:elliptic-vs-rational` | `theorem` | 479 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 851 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1047 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1125 | DYBE and bar nilpotency |

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

#### `chapters/examples/w_algebras.tex` (53)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-algebra-koszul-main` | `theorem` | 156 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 359 | Subregular \texorpdfstring{$\mathcal{W}$}{W}-algebra duality for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} |
| `thm:w-geometric-ope` | `theorem` | 688 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 759 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-critical-bar` | `theorem` | 799 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 836 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 962 | Virasoro uncurved self-duality at \texorpdfstring{$c=0$}{c=0} |
| `thm:vir-genus1-curvature` | `theorem` | 1091 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1142 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1206 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1375 | Koszul dual of \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1456 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1522 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 1592 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 1687 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 1783 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 1804 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-center-langlands` | `theorem` | 1893 | \texorpdfstring{$\mathcal{W}$}{W}-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 1998 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `thm:w-universal-gravitational-cubic` | `theorem` | 2751 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | 2806 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | 2843 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | 2930 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-w3-mixed-shadow` | `theorem` | 3010 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w-w3-weight6-resonance` | `proposition` | 3092 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | 3163 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | 3189 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-archetype-trichotomy` | `theorem` | 3265 | Archetype trichotomy |
| `thm:w-virasoro-quintic-forced` | `theorem` | 3332 | Virasoro quintic forced |
| `cor:virasoro-quintic-shadow-explicit` | `corollary` | 3377 | Explicit quintic shadow for Virasoro |
| `thm:w-finite-termination` | `theorem` | 3486 | Finite termination for primitive archetypes |
| `cor:virasoro-postnikov-nontermination` | `corollary` | 3563 | Virasoro/$\mathcal{W}_N$ shadow Postnikov tower: infinite |
| `thm:w-virasoro-genus1-hessian` | `theorem` | 3601 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | 3768 | $\mathcal{W}_3$ quintic obstruction |
| `thm:w-finite-arity-polynomial-pva` | `theorem` | 3993 | Finite-arity theorem for polynomial PVAs |
| `cor:w-semistrictity-classical-w3` | `corollary` | 4031 | Semistrictity of the classical $\mathcal{W}_3$ bulk |
| `prop:w-semistrict-tree-identity` | `proposition` | 4073 | Tree identity for semistrict cyclic theories |
| `prop:w-semistrict-stable-graph` | `proposition` | 4100 | Stable-graph identity for semistrict modular theories |
| `prop:w-semistrict-admissibility` | `proposition` | 4168 | Admissibility of the weight filtration |
| `thm:w-cubic-weight-recursion` | `theorem` | 4193 | Cubic weight recursion |
| `cor:w-cubic-obstruction-classes` | `corollary` | 4227 | Cubic obstruction classes |
| `prop:w-boundary-model-well-defined` | `proposition` | 4265 | Well-definedness |
| `thm:w-semistrict-package` | `theorem` | 4285 | The $\mathcal{W}_3$ semistrict modular higher-spin package |
| `thm:w-pbw-slodowy-collapse` | `theorem` | 4463 | PBW--Slodowy collapse |
| `cor:w-principal-completed-koszul` | `corollary` | 4524 | Principal $W$-algebras are completed Koszul |
| `thm:w-canonical-arity-detection` | `theorem` | 4590 | Canonical arity detection |
| `thm:w-bp-strict` | `theorem` | 4616 | Bershadsky--Polyakov is strict |
| `thm:w-w4-cubic` | `theorem` | 4666 | $\mathcal{W}_4^{(2)}$ has canonical arity~$3$ |
| `thm:w-full-raw-coefficient-packet` | `theorem` | 4725 | Full raw coefficient packet |
| `thm:w-subregular-appell` | `theorem` | 4784 | Subregular Appell formula |
| `thm:w-unbounded-canonical-arity` | `theorem` | 4822 | Unbounded canonical arity |
| `cor:w-subregular-arity-staircase` | `corollary` | 4851 | The subregular arity staircase |
| `thm:w-subregular-classification` | `theorem` | 4893 | Subregular classification |

#### `chapters/examples/w_algebras_deep.tex` (17)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 139 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 832 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `prop:w3-deg3-vacuum` | `proposition` | 1341 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1551 | DS hierarchy and Koszul duality: proved cases |
| `thm:winfty-scalar` | `theorem` | 1792 | Scalar saturation of $\mathcal{W}_\infty$: the shadow tower collapses |
| `prop:gram-wt4` | `proposition` | 1944 | Weight-$4$ Gram matrix |
| `cor:lambda-qp` | `corollary` | 2009 | Quasi-primary at weight~$4$ |
| `thm:c334` | `theorem` | 2052 | Structure constant of the $\mathcal{W}_4$ algebra |
| `prop:virasoro-primitive` | `proposition` | 2235 | Virasoro primitive series |
| `prop:virasoro-bar-window` | `proposition` | 2296 | Virasoro bar windows |
| `prop:virasoro-entropy` | `proposition` | 2337 | Virasoro Koszul entropy |
| `prop:w3-basis-weight3` | `proposition` | 2440 | $\Walg_3$ exact bar basis at reduced weight~$3$ |
| `prop:w3-entropy` | `proposition` | 2473 | $\Walg_3$ Koszul entropy |
| `prop:wn-character-primitive` | `proposition` | 2494 | $\Walg_N$ character and primitive series |
| `prop:wn-entropy-ladder` | `proposition` | 2526 | $\Walg_N$ entropy ladder |
| `prop:winfty-macmahon` | `proposition` | 2585 | $\Walg_\infty$ character and MacMahon factorization |
| `prop:winfty-bar-window` | `proposition` | 2621 | $\Walg_\infty$ bar-window series and Koszul entropy |

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

#### `chapters/examples/yangians_drinfeld_kohno.tex` (83)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-dk-affine` | `theorem` | 101 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 200 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 365 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 465 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 580 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 629 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 766 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 954 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 995 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 1265 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 1386 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 1588 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 1695 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 1793 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 1999 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 2078 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `thm:bridge-criterion` | `theorem` | 2246 | Bridge Criterion Theorem |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 2398 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 2515 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 2574 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 2657 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 2738 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 2769 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 2806 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 2873 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 2903 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 2934 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 2993 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 3072 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 3101 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 3168 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 3200 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 3238 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 3253 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 3303 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 3360 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 3407 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 3498 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 3598 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 3638 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 3674 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 3701 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 3844 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 3876 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 3926 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 3964 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 3991 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 4024 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 4062 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 4088 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 4274 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 4337 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 4372 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 4426 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 4459 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 4510 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 4585 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts-orig` | `corollary` | 4741 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet-orig` | `corollary` | 4770 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization-orig` | `corollary` | 4803 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization-orig` | `corollary` | 4834 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet-orig` | `corollary` | 4885 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 4992 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 5091 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 5152 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 5202 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 5261 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed-orig` | `corollary` | 5304 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line-orig` | `corollary` | 5337 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |
| `prop:free-propagator-matching` | `proposition` | 6015 | Free/$\beta\gamma$ propagator matching |
| `prop:affine-propagator-matching` | `proposition` | 6061 | Affine $\hat{\mathfrak{sl}}_2$ propagator matching |
| `thm:spectral-derived-additive-kz` | `theorem` | 6229 | Derived additive KZ connection |
| `thm:spectral-boundary-residue` | `theorem` | 6280 | Boundary residue theorem |
| `thm:spectral-transfer-flat` | `theorem` | 6332 | Transfer of flat spectral connections |
| `thm:spectral-quasi-factorization` | `theorem` | 6406 | Quasi-factorization theorem |
| `thm:spectral-strictification-cohomology` | `theorem` | 6490 | Strictification by spectral cohomology |
| `thm:spectral-triangle-localization` | `theorem` | 6548 | Triangle localization |
| `thm:spectral-quadrilateral-localization` | `theorem` | 6590 | Quadrilateral localization |
| `thm:spectral-cartan-diagonal-exact` | `theorem` | 6678 | Cartan-diagonal Drinfeld class is exact |
| `thm:spectral-abelian-strictification` | `theorem` | 6750 | Abelian strictification |
| `thm:spectral-residue-bounded-completion` | `theorem` | 6774 | Residue-bounded completion |
| `prop:spectral-exact-free-transport` | `proposition` | 6815 | Exact free transport |
| `thm:spectral-conditional-strictification` | `theorem` | 6849 | Conditional strictification criterion |

#### `chapters/examples/yangians_foundations.tex` (42)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 228 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 313 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 346 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 405 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 446 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 501 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 565 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 1030 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1151 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1195 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1305 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1386 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1404 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1434 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1496 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 1560 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 1646 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 1743 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 1813 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 1882 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 1919 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 1975 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2035 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2096 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2195 | Standard type-A fundamental line operator has the expected local residue |
| `lem:shifted-rtt-bar-stabilization` | `lemma` | 2618 | Weightwise stabilization of the bar complex |
| `thm:shifted-rtt-stabilized-recovery` | `theorem` | 2645 | Stabilized completed bar/cobar recovery |
| `cor:shifted-rtt-tower-convergence` | `corollary` | 2676 | Automatic tower convergence |
| `thm:shifted-rtt-mc-descent` | `theorem` | 2691 | Weightwise Maurer--Cartan descent |
| `thm:shifted-rtt-trace-duality` | `theorem` | 2779 | Trace-theoretic bar duality |
| `cor:shifted-rtt-lagrangian-envelope` | `corollary` | 2824 | The Lagrangian envelope |
| `lem:shifted-rtt-scalar-gauge` | `lemma` | 2872 | Scalar gauge invariance |
| `cor:shifted-rtt-inverse-sign` | `corollary` | 2888 | Inverse kernel versus sign reversal |
| `thm:shifted-rtt-bar-adjointness` | `theorem` | 2918 | Finite-stage RTT bar adjointness |
| `cor:shifted-rtt-twisting-cochain` | `corollary` | 2951 | Degree-$2$ twisting cochain |
| `thm:shifted-rtt-twist-transport` | `theorem` | 2985 | Twist transport of the RTT relation space |
| `thm:shifted-rtt-shifted-bar-adjointness` | `theorem` | 3010 | Shifted bar adjointness under bi-diagonal twist |
| `thm:shifted-rtt-coideal-descent` | `theorem` | 3082 | Quotient/coideal descent |
| `prop:stage-one-cartan-collapse` | `proposition` | 3131 | Naive Cartan collapse at stage~$1$ |
| `thm:shifted-rtt-rank-one-coideal` | `theorem` | 3157 | Rank-one orthogonal coideal |
| `cor:shifted-rtt-weyl-algebra` | `corollary` | 3184 | Generalized Weyl algebra structure |
| `thm:shifted-rtt-kleinian` | `theorem` | 3206 | Kleinian associated graded at the nilpotent point |

### Part III: Connections (142)

#### `chapters/connections/bv_brst.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bv-bar-bridge` | `theorem` | 15 | Bridge theorem: BV complex = bar complex |
| `thm:qme-bar-cobar` | `theorem` | 163 | Quantum master equation as Maurer--Cartan equation |
| `thm:genus0-amplitude-bar` | `theorem` | 220 | Genus-\texorpdfstring{$0$}{0} amplitudes from bar complex |
| `thm:log-form-ghost-law` | `theorem` | 305 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 408 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 559 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `thm:bar-semi-infinite-km` | `theorem` | 655 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 759 | Anomaly duality for Kac--Moody pairs |
| `thm:bar-semi-infinite-w` | `theorem` | 850 | Bar complex = semi-infinite complex for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:virasoro-semi-infinite` | `corollary` | 936 | Virasoro bar complex = semi-infinite complex |
| `cor:anomaly-duality-w` | `corollary` | 960 | Anomaly complementarity for \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |
| `thm:config-space-bv` | `theorem` | 1061 | Configuration space BV structure |
| `thm:bv-functor` | `theorem` | 1134 | BV functor |

#### `chapters/connections/concordance.tex` (10)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 300 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 314 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `prop:finite-jet-rigidity` | `proposition` | 584 | Finite-jet rigidity |
| `prop:polynomial-level-dependence` | `proposition` | 608 | Polynomial level dependence |
| `prop:gaussian-collapse-abelian` | `proposition` | 645 | Gaussian collapse for abelian input |
| `thm:lagrangian-complementarity` | `theorem` | 2141 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 2243 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 2479 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 2524 | Spectral discriminant --- general case |
| `thm:family-index` | `theorem` | 2755 | Family index theorem for genus expansions |

#### `chapters/connections/editorial_constitution.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-pbw` | `theorem` | 234 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 260 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, originally conjectured)} |
| `prop:standard-tower-mc5-reduction` | `proposition` | 556 | Standard-tower MC5 reduction after MC3 and realized MC4 |
| `cor:standard-tower-mc5-closure` | `corollary` | 644 | Standard-tower MC5 closure on the canonical Yangian locus |
| `rem:conjecture-attack-strategies` | `remark` | 953 | Conjecture-by-conjecture attack strategies |
| `prop:en-n2-recovery` | `proposition` | 1586 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1732 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1790 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1824 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1840 | Physical anomaly cancellation for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2058 | Hodge symmetry from complementarity |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 2369 | Volume~I concrete modular datum |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 97 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:feynman-bar-bridge` | `theorem` | 5 | Bridge theorem: Feynman--bar dictionary |
| `thm:ainfty-constraint-formula` | `theorem` | 219 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 324 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 363 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 390 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 426 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 444 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 465 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 512 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 571 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 930 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 962 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/frontier_modular_holography_platonic.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:frontier-protected-bulk-antiinvolution` | `theorem` | 98 | Protected bulk reconstruction and anti-involution |
| `thm:frontier-transposition-cotangent` | `theorem` | 195 | Holographic transposition and cotangent realization |
| `lem:frontier-determinant-parity` | `lemma` | 248 | Determinant parity for shifted cotangent pairs |
| `cor:frontier-spectral-reciprocity-palindromicity` | `corollary` | 289 | Spectral reciprocity, palindromicity, and parity rigidity |
| `thm:frontier-scalar-fixed-point-rigidity` | `theorem` | 342 | Scalar fixed-point rigidity and genus-$1$ completeness |
| `thm:frontier-heisenberg-fourier-transport` | `theorem` | 455 | Heisenberg relations and Fourier transport |
| `thm:frontier-weyl-pbw-linear-sewing` | `theorem` | 568 | Associativity, PBW, and exact linear Weyl sewing |
| `lem:frontier-formal-gaussian-differential-identity` | `lemma` | 689 | Formal Gaussian differential identity |
| `thm:frontier-gaussian-composition-schur-anomaly` | `theorem` | 760 | Gaussian composition, Schur complement, and determinant anomaly |
| `thm:frontier-metaplectic-cocycle-strictification` | `theorem` | 892 | Cocycle law and metaplectic strictification |
| `cor:frontier-first-nonlinear-holographic-anomaly` | `corollary` | 972 | The first nonlinear holographic anomaly |
| `thm:collision-residue-twisting` | `theorem` | 1556 | Collision residue = universal twisting morphism |
| `thm:collision-depth-2-ybe` | `theorem` | 1612 | MC at collision depth~$2$ gives $A_\infty$-YBE |
| `thm:shadow-connection-kz` | `theorem` | 1650 | Shadow connection for affine Kac--Moody = KZ |
| `cor:shadow-connection-heisenberg` | `corollary` | 1693 | Heisenberg shadow connection |
| `prop:shadow-connection-bpz` | `proposition` | 1714 | Shadow connection for Virasoro recovers BPZ |
| `thm:quartic-obstruction-linf` | `theorem` | 1750 | Quartic obstruction = $L_\infty$ obstruction |
| `comp:heisenberg-holographic-datum` | `computation` | 1883 | Complete holographic datum for Heisenberg |
| `prop:finite-jet-rigidity-frontier` | `proposition` | 1987 | Finite-jet rigidity |
| `thm:level-polynomial` | `theorem` | 2011 | Level-polynomial theorem |
| `thm:gaussian-collapse` | `theorem` | 2047 | Gaussian collapse |
| `prop:independent-sums-factor` | `proposition` | 2072 | Independent sums factor |
| `thm:quartic-stability-filtered-mc` | `theorem` | 2174 | Quartic stability from filtered MC |
| `prop:sewing-envelope-universal` | `proposition` | 2310 | Universal property of the sewing envelope |
| `prop:transport-propagation-frontier` | `proposition` | 2474 | Transport propagation lemma |

#### `chapters/connections/genus_complete.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 235 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 290 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 372 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 648 | Bar complex computes moduli integrals |
| `thm:full-modular-invariant-hierarchy` | `theorem` | 1101 | The full modular invariant hierarchy |

#### `chapters/connections/kontsevich_integral.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-weight-systems` | `theorem` | 111 | Bar complex weight systems |
| `prop:propagator-restriction` | `proposition` | 180 | Propagator restriction |
| `prop:kz-from-bar` | `proposition` | 266 | KZ connection from bar complex |
| `thm:drinfeld-associator-bar` | `theorem` | 309 | Drinfeld associator from bar-cobar |

#### `chapters/connections/poincare_computations.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-c26-selfdual` | `proposition` | 164 | Virasoro NAP duality at \texorpdfstring{$c=26$}{c=26} |
| `thm:genus-complementarity` | `theorem` | 291 | Genus complementarity |

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
| `thm:finite-arity-convolution-chapter` | `theorem` | 381 | Finite-arity convolution theorem |
| `thm:quadratic-cubic-twisting-theorem-chapter` | `theorem` | 433 | Quadratic-cubic twisting theorem |
| `prop:admissibility-finite-slices-chapter` | `proposition` | 508 | Admissibility and finite-dimensional weight slices |
| `thm:cubic-weight-recursion-chapter` | `theorem` | 531 | Cubic weight recursion around the shadow base point |
| `cor:cubic-obstruction-classes-chapter` | `corollary` | 562 | Cubic obstruction classes |
| `prop:stable-graph-identity-chapter` | `proposition` | 575 | Stable-graph identity for semistrict modular theories |
| `prop:well-definedness-completed-boundary-model-chapter` | `proposition` | 629 | Well-definedness of the completed boundary model |
| `thm:main-semistrict-modular-higher-spin-package-chapter` | `theorem` | 659 | Main Theorem: the classical $W_3$ sector defines a semistrict modular higher-spin package |
| `cor:platonic-reduction-W3-frontier` | `corollary` | 694 | Platonic reduction of the $W_3$ frontier |

#### `chapters/connections/ym_boundary_theory.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ym-bar-bridge` | `theorem` | 62 | Bridge theorem: boundary chiral algebra $\to$ mass-gap criterion via bar-cobar |
| `thm:grand-synthesis-principle` | `theorem` | 132 | Grand synthesis principle |
| `thm:twisted-ym-boundary-brst` | `theorem` | 225 | Boundary BRST recovery for twisted Yang--Mills data |
| `thm:twisted-ym-tangent-center` | `theorem` | 250 | Tangent-to-center principle |
| `cor:twisted-ym-center-rigidity` | `corollary` | 269 | Center-vanishing rigidity criterion |
| `cor:twisted-ym-one-parameter` | `corollary` | 279 | One-parameter criterion |
| `thm:twisted-ym-tangent-factors-through-center` | `theorem` | 301 | The tangent functor factors through the dual center |
| `cor:twisted-ym-interface-invariance` | `corollary` | 327 | Interface invariance of tangent data |
| `cor:twisted-ym-center-comparison` | `corollary` | 345 | Comparison without full boundary equivalence |
| `thm:twisted-ym-dual-unobstructedness` | `theorem` | 387 | Dual unobstructedness criterion |
| `thm:twisted-ym-central-formality` | `theorem` | 410 | Central formality theorem |
| `lem:twisted-ym-center-tensor` | `lemma` | 467 | Center of a chiral tensor product |
| `thm:twisted-ym-binary-mixed-couplings` | `theorem` | 505 | Binary mixed-coupling theorem |
| `cor:twisted-ym-multibody-couplings` | `corollary` | 570 | Multi-body coupling expansion |
| `cor:twisted-ym-mixed-rigidity` | `corollary` | 604 | Mixed rigidity criterion |

#### `chapters/connections/ym_higher_body_couplings.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:relative-duality-theorem` | `theorem` | 94 | Relative duality theorem |
| `cor:relative-tangent-center-principle` | `corollary` | 144 | Relative tangent-to-center principle |
| `cor:relative-dual-unobstructedness` | `corollary` | 155 | Relative dual unobstructedness |
| `thm:relative-central-formality` | `theorem` | 174 | Relative central formality |
| `lem:mixed-ks-well-defined` | `lemma` | 224 | Well-definedness and invariance |
| `thm:first-correction-theorem` | `theorem` | 233 | First-correction theorem |
| `cor:persistence-criterion-quadratic-law` | `corollary` | 263 | Persistence criterion for the quadratic law |
| `thm:universal-interaction-brackets` | `theorem` | 276 | Universal interaction brackets on mixed couplings |
| `lem:w-boundary-simplex-homotopy-invariance` | `lemma` | 379 | Homotopy invariance |
| `thm:w-boundary-cech-duality` | `theorem` | 400 | Higher-body \v{C}ech duality |
| `thm:w-augmented-center-tensor-model` | `theorem` | 473 | Tensor-product model for the augmented center complex |
| `cor:w-pure-mbody-coupling-theorem` | `corollary` | 530 | Pure $m$-body coupling theorem |
| `thm:w-higher-mayer-vietoris-couplings` | `theorem` | 547 | Higher Mayer--Vietoris descent for couplings |
| `thm:w-filtered-stability-pure-mbody` | `theorem` | 589 | Filtered stability of pure $m$-body couplings |

#### `chapters/connections/ym_instanton_screening.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:novikov-completion-theorem` | `theorem` | 106 | Novikov completion theorem |
| `thm:instanton-completed-tangent-center` | `theorem` | 167 | Instanton-completed tangent-to-center principle |
| `thm:screened-tangent-center` | `theorem` | 232 | Screened tangent-to-center principle |
| `prop:koszul-identification-visible-center` | `proposition` | 273 | Koszul identification of the visible center |
| `thm:instanton-screening-spectral-sequence` | `theorem` | 299 | Instanton-screening spectral sequence |
| `thm:central-localization-confinement` | `theorem` | 343 | Central localization criterion for confinement |
| `thm:screened-cech-duality` | `theorem` | 396 | Higher-body \v{C}ech duality after screening |
| `thm:screening-hodge-theorem` | `theorem` | 460 | Screening Hodge theorem |
| `cor:screening-spectral-gap-criterion` | `corollary` | 486 | Screening spectral gap criterion |
| `cor:stable-untwisting-bounded-error` | `corollary` | 539 | Stable untwisting under bounded error |
| `prop:internal-screening-form` | `proposition` | 631 | Operator-algebraic meaning of the screening form |
| `thm:mass-gap-reduction-internal-screening` | `theorem` | 710 | Mass-gap reduction to an internal screening estimate |
| `cor:exact-reduction-screening-estimate` | `corollary` | 744 | Exact formulation of the reduction principle |

### Appendices (264)

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

#### `appendices/casimir_divisor_core_transport.tex` (24)

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
| `thm:sector-determinant` | `theorem` | 710 | Characteristic polynomial of a sector |
| `thm:common-core-exact-sequences` | `theorem` | 759 | Common-core exact sequences |
| `prop:transport-factors-through-common-core` | `proposition` | 783 | Shift-compatible transport factors through the common core |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:806` | `corollary` | 806 | Corrected transport principle |
| `prop:squarefree-common-sector` | `proposition` | 816 | Squarefree common-sector rigidity |
| `prop:sl3-w3-defect` | `proposition` | 898 | Exact defect decomposition for \(\widehat{\mathfrak{sl}}_3/W_3\) |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:920` | `corollary` | 920 | All transport maps factor through the quadratic core |
| `prop:explicit-sl3-projectors` | `proposition` | 939 | Explicit coprime-locus projectors |
| `__unlabeled_appendices/casimir_divisor_core_transport.tex:1019` | `proposition` | 1019 | The \(L_1\)--\(L_2\) package on the one-channel squarefree locus |

#### `appendices/coderived_models.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 240 | Adequacy |
| `thm:stratified-conservative-restriction` | `theorem` | 571 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 647 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 697 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 724 | Factorization co-contra correspondence |
| `thm:off-koszul-ran-inversion` | `theorem` | 816 | Off-Koszul bar-cobar inversion on Ran |

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-pade` | `proposition` | 846 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dg_shifted_factorization_bridge.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-additive-kz` | `theorem` | 115 | Derived additive KZ connection |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:171` | `corollary` | 171 | Derived Drinfeld--Kohno shadow |
| `thm:boundary-residue` | `theorem` | 181 | Boundary residue theorem |
| `thm:transfer-flat-spectral` | `theorem` | 223 | Transfer of flat spectral connections |
| `thm:quasi-factorization` | `theorem` | 290 | Quasi-factorization theorem |
| `thm:strictification-spectral-cohomology` | `theorem` | 349 | Strictification by spectral cohomology |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:394` | `proposition` | 394 | Quadratic hexagon obstruction |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:423` | `proposition` | 423 | Three-particle obstruction identity |
| `thm:abelian-strictification` | `theorem` | 461 | Abelian strictification theorem |
| `thm:residue-bounded-completion` | `theorem` | 481 | Residue-bounded completion theorem |
| `prop:cartan-shift-cocycle` | `proposition` | 534 | Cartan shift cocycle identities |
| `thm:cartan-gauge-twist` | `theorem` | 552 | Cartan gauge-twist theorem |
| `thm:cartan-diagonal-defect-exact` | `theorem` | 595 | Cartan-diagonal shift defect is exact |
| `thm:triangle-localization` | `theorem` | 667 | Triangle localization formula |
| `thm:adjacent-root-rigidity` | `theorem` | 729 | Adjacent-root rigidity |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:748` | `corollary` | 748 | Normalized rational triangle coefficient |
| `prop:triangle-shift-transport` | `proposition` | 793 | Triangle shift transport law |
| `lem:free-closed-generating-kernel` | `lemma` | 844 | Closed generating kernel |
| `thm:exact-free-transport` | `theorem` | 874 | Exact free two-body transport |
| `lem:class3-ordered-bch` | `lemma` | 948 | Class-$3$ ordered BCH coefficient |
| `thm:quadrilateral-localization` | `theorem` | 983 | Quadrilateral localization formula |
| `thm:quadrilateral-rigidity` | `theorem` | 1075 | Quadrilateral rigidity |
| `cor:quadrilateral-normalized-rational` | `corollary` | 1103 | Normalized rational quadrilateral coefficient |
| `prop:quadrilateral-shift-transport` | `proposition` | 1139 | Quadrilateral shift transport law |
| `cor:no-new-filtration3-shift-obstruction` | `corollary` | 1169 | No new independent shift obstruction in filtration $3$ |
| `__unlabeled_appendices/dg_shifted_factorization_bridge.tex:1204` | `theorem` | 1204 | Conditional strictification criterion |

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
| `thm:nms-mc-principle` | `theorem` | 181 | Algebra structure $=$ Maurer--Cartan element |
| `prop:nms-five-component` | `proposition` | 214 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | 274 | Shadow tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | 314 | All families from universal evaluation |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | 407 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | 461 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | 507 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | 516 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | 537 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | 552 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | 651 | Quartic shadow master equations |
| `thm:nms-separating-boundary-recursion` | `theorem` | 690 | Separating boundary recursion through quartic order |
| `thm:nms-shadow-cocycle-characterization` | `theorem` | 752 | Finite-order realization of the universal class |
| `prop:nms-quartic-closure-envelope` | `proposition` | 803 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | 826 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | 846 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | 870 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | 894 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | 961 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | 985 | Vanishing of the quartic contact invariant |
| `cor:nms-betagamma-boundary-law` | `corollary` | 1009 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | 1026 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | 1047 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | 1073 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | 1111 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | 1139 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | 1211 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | 1241 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `prop:nms-w3-visible-resonance-factor` | `proposition` | 1280 | Visible quartic resonance factor for \texorpdfstring{$\mathcal W_3$}{W3} |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | 1320 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | 1338 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | 1354 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | 1463 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | 1515 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 1539 | Clutching law for the modular quartic resonance class |
| `thm:nms-first-nonlinear-shadow-theta` | `theorem` | 1613 | The first nonlinear shadow of \texorpdfstring{$\Theta_{\cA}$}{ThetaA} |
| `cor:nms-family-boundary-behavior` | `corollary` | 1626 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | 1695 | Functoriality and duality through quartic order |
| `thm:nms-all-arity-master-equation` | `theorem` | 1798 | All-arity master equation |
| `cor:nms-quintic-master-equation` | `corollary` | 1821 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | 1841 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | 1860 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | 1879 | Finite termination for primitive archetypes |
| `thm:nms-all-arity-separating-boundary` | `theorem` | 1904 | All-arity separating boundary recursion |
| `cor:nms-quintic-separating-boundary` | `corollary` | 1920 | Quintic separating boundary recursion |
| `prop:nms-genus-loop-properties` | `proposition` | 1966 | Basic properties of the genus loop operator |
| `thm:nms-nonseparating-clutching-law` | `theorem` | 1983 | Non-separating clutching law for the shadow tower |
| `cor:nms-genus-one-hessian-correction` | `corollary` | 2007 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | 2031 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2114 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2148 | Ambient complementarity and nonlinear modular shadows |
| `prop:nms-nonlinear-phase-standard` | `proposition` | 2347 | Nonlinear phase of the standard families |
| `prop:nms-basis-independence-specialization-restated` | `proposition` | 2706 | Basis independence and specialization |
| `thm:nms-clutching-law-modular-resonance-restated` | `theorem` | 2734 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behaviour` | `corollary` | 2764 | Family-by-family boundary behaviour |
| `thm:nms-genus-loop-model-families-restated` | `theorem` | 2890 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat-restated` | `theorem` | 2958 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary-restated` | `theorem` | 2990 | Ambient complementarity and nonlinear modular shadows |
| `thm:reduced-weight-finiteness` | `theorem` | 3193 | Reduced-weight finiteness |
| `thm:window-locality` | `theorem` | 3281 | Window locality |
| `cor:exact-stabilization` | `corollary` | 3303 | Exact stabilization |

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
| `thm:bar-ss` | `theorem` | 241 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 293 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 357 | Central charge and \texorpdfstring{$d_1$}{d1} |

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
