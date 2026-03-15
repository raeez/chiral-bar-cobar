# Theorem Registry

Auto-generated on 2026-03-15 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 1074 |
| Total tagged claims | 1554 |
| Active files in `main.tex` | 61 |
| Total `.tex` files scanned | 70 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1074 |
| `ProvedElsewhere` | 317 |
| `Conjectured` | 140 |
| `Heuristic` | 23 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 417 |
| `proposition` | 364 |
| `corollary` | 180 |
| `lemma` | 73 |
| `computation` | 33 |
| `calculation` | 3 |
| `remark` | 2 |
| `conjecture` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 8 |
| Part I: Theory | 556 |
| Part II: Examples | 411 |
| Part III: Connections | 57 |
| Appendices | 42 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/bar_cobar_construction.tex` | 168 |
| `chapters/theory/higher_genus.tex` | 168 |
| `chapters/examples/yangians.tex` | 136 |
| `chapters/theory/chiral_modules.tex` | 52 |
| `chapters/examples/free_fields.tex` | 50 |
| `chapters/theory/configuration_spaces.tex` | 35 |
| `chapters/examples/genus_expansions.tex` | 34 |
| `chapters/examples/kac_moody_framework.tex` | 34 |
| `chapters/examples/lattice_foundations.tex` | 32 |
| `chapters/theory/deformation_theory.tex` | 29 |
| `chapters/theory/chiral_koszul_pairs.tex` | 26 |
| `chapters/examples/detailed_computations.tex` | 25 |
| `chapters/theory/koszul_pair_structure.tex` | 20 |
| `chapters/examples/w_algebras_framework.tex` | 19 |
| `chapters/connections/concordance.tex` | 18 |
| `chapters/examples/examples_summary.tex` | 18 |
| `chapters/theory/fourier_seed.tex` | 16 |
| `chapters/examples/beta_gamma.tex` | 15 |
| `chapters/examples/w3_composite_fields.tex` | 13 |
| `chapters/connections/bv_brst.tex` | 12 |

## Complete Proved Registry

### Frame (8)

#### `chapters/frame/heisenberg_frame.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 468 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 825 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 921 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1084 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1308 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1330 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1493 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1671 | Quantum complementarity for Heisenberg |

### Part I: Theory (556)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 449 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 737 | Geometric realization |
| `prop:orthogonal` | `proposition` | 862 | Orthogonality |

#### `chapters/theory/bar_cobar_construction.tex` (168)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 249 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 560 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 650 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 709 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 775 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 803 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 898 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 940 | Arnold relations |
| `comp:deg0` | `computation` | 1048 | Degree 0 |
| `comp:deg1-general` | `computation` | 1066 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1179 | Bar construction is functorial |
| `lem:bar-induced-chain-map` | `lemma` | 1219 | Induced map is chain map |
| `lem:bar-induced-coalgebra` | `lemma` | 1252 | Induced map is coalgebra morphism |
| `cor:bar-natural` | `corollary` | 1317 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1323 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1355 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1378 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1445 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1496 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1513 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1600 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1626 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1650 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1714 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1789 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1851 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1961 | Bar complex is chiral |
| `lem:bar-holonomicity` | `lemma` | 2116 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 2177 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 2210 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 2292 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 2368 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 2482 | Verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 2731 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 2891 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 3109 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 3240 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 3286 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 3559 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 3607 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 3628 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 3674 | Topology |
| `thm:poincare-verdier` | `theorem` | 3733 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 3822 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 3846 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 3892 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 4027 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 4123 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 4264 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 4289 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 4342 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 4395 | Recognition principle |
| `lem:deformation-space` | `lemma` | 4767 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 4809 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 4857 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 4936 | Curved differential formula |
| `thm:curvature-central` | `theorem` | 5024 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 5118 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 5195 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 5264 | Conilpotency ensures convergence |
| `prop:mc4-reduction-principle` | `proposition` | 5395 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 5460 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 5497 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 5535 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 5584 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 5635 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 5668 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 5732 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 5768 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 5844 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 5941 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 5957 | Factorization-envelope criterion for principal stages |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 6030 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 6076 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 6111 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 6131 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 6149 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 6168 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 6210 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 6250 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 6291 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 6358 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 6401 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 6447 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 6509 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 6550 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 6646 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 6733 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 6759 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 6784 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 6838 | Stage-\texorpdfstring{$4$}{4} frontier as one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 6866 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 6903 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 6934 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 6976 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 7003 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 7033 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 7076 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 7111 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 7141 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 7158 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 7209 | Exact MC4 frontier packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 7270 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 frontier |
| `cor:winfty-dual-candidate-construction` | `corollary` | 7309 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 7356 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} frontier on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 7395 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 7480 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 7511 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 7594 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 7642 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 7688 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 7715 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 7834 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 7873 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 7920 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 7975 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 8017 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 8111 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 8136 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 8175 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 8195 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 8233 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 8250 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 8273 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 8295 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 8311 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 8321 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 8337 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 8349 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 8362 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 8380 | Stage-\texorpdfstring{$5$}{5} mixed transport frontier carries one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 8395 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 8414 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 8621 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 8638 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 8675 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 8715 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-conjecture-network-collapse` | `corollary` | 9011 | Visible stage-\texorpdfstring{$5$}{5} local conjecture network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 9053 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 9211 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 9449 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 9790 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 9826 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 9887 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 9899 | Strict nilpotence at all genera |
| `cor:genus-expansion-converges` | `corollary` | 10118 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 10178 | Functoriality of bar construction |
| `prop:filtered-to-curved` | `proposition` | 10548 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 10767 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 11076 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 11191 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 11264 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 11308 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 11376 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 11442 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 11577 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 11643 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 11763 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 11896 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 11912 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 11968 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 11991 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 12051 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 12096 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 12108 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 12143 | Derived equivalence |
| `prop:bar-fh` | `proposition` | 12374 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 12452 | Cobar as factorization cohomology |

#### `chapters/theory/chiral_koszul_pairs.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 143 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 170 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 190 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 218 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 293 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 548 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 626 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 681 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 725 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 872 | Bar concentration for Koszul pairs |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 937 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 1102 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 1162 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 1316 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 1410 | Bar computes Koszul dual — complete statement |
| `lem:completion-convergence` | `lemma` | 1498 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 1547 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 2118 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 2336 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 2401 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 2462 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 2585 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 2627 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 2681 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 2716 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 2911 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (52)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 136 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 241 | Module Koszul equivalence |
| `thm:monoidal-module-koszul` | `theorem` | 271 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 411 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 487 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 591 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 684 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 742 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 897 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 1191 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1580 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1641 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1841 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1899 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1934 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:orbit-duality` | `proposition` | 2060 | Orbit duality for affine vertex algebras |
| `prop:logarithmic-bar` | `proposition` | 2185 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2279 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2390 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2425 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2464 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2481 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2521 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2543 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2693 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2800 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2914 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 2994 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3148 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3179 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3231 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3310 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3396 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3455 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3531 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3608 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3658 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3751 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3805 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3871` | `calculation` | 3871 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3898` | `calculation` | 3898 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3929` | `calculation` | 3929 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4047 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4172 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4229 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4319 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4361 | \texorpdfstring{$\mathcal{W}$}{W}-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4416 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4458 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4588 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4727 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4837 | Heisenberg fusion splitting |

#### `chapters/theory/configuration_spaces.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 215 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 325 | Normal crossings |
| `thm:closure-relations` | `theorem` | 420 | Closure relations |
| `thm:log-complex` | `theorem` | 533 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 572 | Arnold relations |
| `prop:twisting-morphism-propagator` | `proposition` | 614 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 681 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 748 | Residue operations |
| `prop:residue-local` | `proposition` | 803 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 852 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1066 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1133 | Conformal blocks from punctured bar complex |
| `prop:eta` | `proposition` | 1297 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:FM-convergence` | `theorem` | 1647 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1706 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1812 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1854 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 1881 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 1903 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 1943 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 1967 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 2002 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 2024 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 2058 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2074 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2102 | Nilpotency from Arnold relations |
| `thm:arnold-jacobi` | `theorem` | 2251 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2304 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2350 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2382 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2427 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 2658 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 2728 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 2865 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3075` | `computation` | 3075 | Explicit examples |

#### `chapters/theory/deformation_theory.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 113 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 264 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 302 | Hochschild spectral sequence |
| `thm:main-koszul-hoch` | `theorem` | 421 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 534 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `comp:boson-hochschild` | `computation` | 669 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 695 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 795 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 889 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 987 | Kac--Moody cyclic deformation complex |
| `thm:mc2-1-km` | `theorem` | 1123 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1240 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 1482 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 1568 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 1687 | Recovery of the Killing cocycle extension |
| `prop:d-mod-squared-zero` | `proposition` | 1928 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2064 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 2239 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 2429 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 2555 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 2797 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 2943 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 3082 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 3163 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 3210 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 3502 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 3633 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 3680 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 3873 | Boson-fermion duality |

#### `chapters/theory/derived_langlands.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:oper-bar-h0-dl` | `theorem` | 172 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 207 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 231 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 268 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 349 | Differential analysis at arity 3 |
| `prop:d4-nonvanishing` | `proposition` | 429 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 488 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 501 | Full derived identification |
| `prop:bar-as-localization` | `proposition` | 584 | The bar complex as localization |
| `prop:sl2-periodicity-dl` | `proposition` | 706 | Affine sl2 periodicity |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 782 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/en_koszul_duality.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:linking-sphere-residue` | `proposition` | 296 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 371 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 531 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 589 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 13 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 116 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 34 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 91 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 200 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 246 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 294 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 323 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 385 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 412 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 469 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 527 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 607 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 777 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 798 | — |
| `thm:fourier-specialization` | `theorem` | 833 | Specialization |
| `thm:fourier-four-properties` | `theorem` | 888 | The four properties of the Fourier transform |
| `rem:fourier-genus-preview` | `remark` | 988 | Ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus.tex` (168)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | 366 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 466 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 557 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 670 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 777 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 924 | Verdier duality of operations |
| `thm:convergence-filtered` | `theorem` | 1123 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1332 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1366 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1400 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1420 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1436 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 1738 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 1823 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2038 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2306 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2542 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2602 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 2855 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:arnold-genus1` | `theorem` | 2910 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 2995 | Nilpotency at genus 1 |
| `thm:e1-page-complete` | `theorem` | 3266 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3299 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 3426 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3513 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3567 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 3645 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 3762 | \texorpdfstring{$W_3$}{W3} obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 3833 | Explicit genus-\texorpdfstring{$1$}{1} value of the \texorpdfstring{$W_3$}{W3} obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 3854 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 3883 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 3968 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4070 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4200 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4233 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4249 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4265 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4283 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 4306 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4328 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4361 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4433 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4463 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4549 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4593 | Grothendieck--Riemann--Roch bridge |
| `lem:involution-splitting` | `lemma` | 4727 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 4782 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 4856 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 4946 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 5102 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 5157 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 5242 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 5305 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 5356 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 5501 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 5574 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 5614 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 5668 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 5697 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 5885 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 5920 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 5972 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 6085 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 6116 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 6136 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 6202 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 6293 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 6424 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 6492 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 6590 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 6618 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 6655 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 6698 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 6734 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 6760 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 7015 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 7174 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 7224 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 7237 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 7279 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 7338 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 7380 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 7408 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 7430 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 7474 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 7647 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 7695 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 7783 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 7810 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 7838 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 7872 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 7897 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 7957 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 8003 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 8042 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 8071 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 8095 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 8120 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 8152 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 8184 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 8210 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 8226 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 8299 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 8375 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 8423 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 8512 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:genus-graded-koszul` | `theorem` | 8631 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 8662 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 8994 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 9027 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 9068 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 9204 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 9471 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 9496 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 9693 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 9745 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 9845 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 9895 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 9957 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:genus-internalization` | `theorem` | 10234 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 10324 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 10400 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 10429 | Universal modular Maurer--Cartan class |
| `thm:explicit-theta` | `theorem` | 10554 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 10762 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 11176 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 11255 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 11368 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 11402 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 11434 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 11630 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 11706 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 11771 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 11906 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 12003 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 12114 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 12251 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 12403 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 12577 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 12727 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 12921 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 13041 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 13140 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 13230 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 13342 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 13414 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 13496 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 13574 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 13651 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 13727 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 13802 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 13868 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 13946 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 14021 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 14068 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 14110 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 14166 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 14220 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 14253 | Scalar saturation for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 14291 | Scalar saturation persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 14344 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 14416 | Scalar saturation for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 14491 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 14658 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 14821 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 14904 | Cyclic rigidity at generic level |
| `thm:tautological-line-support` | `theorem` | 15189 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 15291 | MC2 reduced to cyclic model |

#### `chapters/theory/hochschild_cohomology.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 66 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 110 | W-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:364` | `computation` | 364 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 420 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 500 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 755 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 787 | Hochschild cup product exchange |

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 390 | Central charge complementarity |
| `prop:chirAss-self-dual` | `proposition` | 917 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | 114 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 159 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 199 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 218 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 275 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 338 | \texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 397 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 526 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 620 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 635 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 739 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 861 | Maurer--Cartan correspondence — quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 952 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 982 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1167 | Positselski comodule-contramodule equivalence |
| `thm:full-derived-module-equiv` | `theorem` | 1193 | Full derived module equivalence |
| `thm:cs-koszul-km` | `theorem` | 1310 | Chern--Simons equations from Koszul duality |
| `thm:linf-mc-flatness` | `theorem` | 1387 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan as homotopy flatness |
| `thm:cs-koszul-general` | `theorem` | 1457 | CS/Koszul for general non-quadratic algebras |
| `thm:bv-structure-bar` | `theorem` | 1643 | BV structure on bar complex |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 183 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 295 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 362 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 453 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 512 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 528 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 619 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 703 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:chiral-operad-genus0` | `proposition` | 298 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 342 | Prism principle --- operadic identification |
| `thm:prism-higher-genus` | `theorem` | 551 | Prism principle --- higher-genus extension |
| `cor:prism-principle` | `corollary` | 658 | The prism principle |
| `thm:partition` | `theorem` | 809 | Partition complex structure |

### Part II: Examples (411)

#### `chapters/examples/beta_gamma.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 67 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 118 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 153 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 206 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 244 | Koszul dual of the free fermion |
| `prop:betagamma-bar-deg2` | `proposition` | 265 | — |
| `thm:cobar-fermions` | `theorem` | 293 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bc-koszul-detailed` | `proposition` | 330 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 418 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 685 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 805 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 906 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1047 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1131 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1282 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |

#### `chapters/examples/deformation_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 422 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 494 | Deformation--duality compatibility |

#### `chapters/examples/deformation_quantization.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 95 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 148 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 380 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 493 | Genus expansion |

#### `chapters/examples/detailed_computations.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 706 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 799 | Modular rank of \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 878 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 939 | PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} |
| `comp:sl3-casimir-decomp` | `computation` | 1032 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | 1115 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | 1444 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1749 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1795 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | 1866 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | 1917 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2046 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2082 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2116 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2546 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2721 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2941 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 2995 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3032 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3306 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3485 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3782 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3844 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4041 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4191 | BGG involution under Koszul duality |

#### `chapters/examples/examples_summary.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 192 | Paired standard-tower MC4 frontier packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 387 | Minimal closure conditions for the standard-tower MC4 frontier |
| `cor:genus1-anomaly-ratio` | `corollary` | 517 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `prop:bar-dimensions` | `proposition` | 726 | Koszul dual Hilbert functions |
| `cor:subexp-free-field` | `corollary` | 958 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 968 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 985 | DS reduction and bar cohomology generating functions |
| `prop:hred-sl2` | `proposition` | 1280 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 1480 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1571 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1668 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1734 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 1789 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1840 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1855 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 1944 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2133 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2439 | Spectral sequence collapse |

#### `chapters/examples/free_fields.tex` (50)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fermion-bar-complex-genus-0` | `theorem` | 42 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 101 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 173 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 184 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `prop:bc-betagamma-orthogonality` | `proposition` | 245 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 268 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 491 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:single-fermion-boson-duality` | `theorem` | 566 | Single-generator fermion-boson duality |
| `thm:heisenberg-bar` | `theorem` | 632 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 655 | Orientation consistency |
| `prop:curved-convergence` | `proposition` | 690 | Convergence in curved structure |
| `thm:monodromy-finite` | `theorem` | 709 | Monodromy finiteness |
| `thm:heisenberg-curved-structure` | `theorem` | 731 | Heisenberg curved structure |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 762 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 794 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 929 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 985 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 1035 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1077 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1229 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1305 | Spectral flow under Koszul duality |
| `thm:lattice-voa-bar` | `theorem` | 1381 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1410 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:virasoro-moduli` | `theorem` | 1457 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 1495 | Geometric interpretation |
| `thm:elliptic-fermion-bar` | `theorem` | 1536 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1573 | Higher genus Heisenberg |
| `thm:filtered-bar-complex` | `theorem` | 1763 | Filtered bar complex |
| `thm:virasoro-string` | `theorem` | 1929 | Virasoro-string duality |
| `thm:w-algebra-bar-flag` | `theorem` | 2077 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar complex |
| `thm:wakimoto-bar` | `theorem` | 2141 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 2171 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 2204 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 2277 | Quantum integrability via \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:heisenberg-not-self-dual` | `theorem` | 2334 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2439 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2514 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2773 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 2887 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 3150 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 3299 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 3346 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3399 | Heisenberg level inversion: curved duality |
| `thm:algebraic-string-dictionary` | `theorem` | 3451 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 3503 | Genus-\texorpdfstring{$0$}{0} string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 3545 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 3652 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 3731 | Bar complex computes genus-\texorpdfstring{$g$}{g} string integrands |
| `thm:modular-invariance` | `theorem` | 3874 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 3911 | Modular anomaly for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |

#### `chapters/examples/genus_expansions.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 16 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 64 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `thm:lattice-all-genera` | `theorem` | 108 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 143 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 165 | \texorpdfstring{$\mathcal{W}$}{W}-algebra free energy at all genera |
| `thm:sl2-all-genera` | `theorem` | 358 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 433 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 459 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 501 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 555 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 666 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 776 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 916 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 983 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1048 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1134 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1266 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1296 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1313 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1339 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1410 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1538 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1580 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1659 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 1808 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 1873 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:complementarity-classification` | `proposition` | 2106 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2160 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2330 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2430 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2446 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2471 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2503 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 2598 | Loop expansion interpretation |

#### `chapters/examples/heisenberg_eisenstein.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-genus-one-complete` | `theorem` | 116 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 203 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 245 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 363 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 466 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 515 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 727 | Multi-boson Eisenstein corrections |

#### `chapters/examples/kac_moody_framework.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-ope-kac-moody` | `theorem` | 207 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 241 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 281 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 347 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 476 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 507 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 545 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 603 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 639 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 708 | Universal Koszul duality for affine Kac--Moody |
| `prop:ff-channel-shear` | `proposition` | 835 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 885 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 951 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1015 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1054 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1108 | Closed-form OPE for Koszul dual |
| `thm:km-quantum-groups` | `theorem` | 1171 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 1497 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 1567 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 1655 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 1767 | KW formula via bar complex: general simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `prop:admissible-verlinde-bar` | `proposition` | 1837 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2076 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 2157 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 2222 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 2274 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 2340 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 2403 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 2449 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 2488 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 2525 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 2693 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 2723 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 2753 | Full derived oper identification |

#### `chapters/examples/lattice_foundations.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:lattice:cocycle-class` | `lemma` | 169 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 331 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 550 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 647 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 670 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 704 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 738 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 783 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 869 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 914 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1119 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1164 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1206 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1229 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1355 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1372 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1397 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1599 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1783 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2408 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2476 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2550 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2709 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3012 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3093 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3263 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3459 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3502 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3660 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3707 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 3793 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 3865 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |

#### `chapters/examples/minimal_model_examples.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 388 | Fusion from bar complex on the torus |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 65 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | 199 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 347 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 371 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | 400 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 425 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 504 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 531 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 591 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 611 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 638 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 734 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

#### `chapters/examples/toroidal_elliptic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 325 | Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0} |
| `thm:elliptic-vs-rational` | `theorem` | 423 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 795 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 991 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1069 | DYBE and bar nilpotency |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 29 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 131 | Mode expansion |
| `thm:c-scaling` | `theorem` | 182 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 281 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 446 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | 530 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 581 | Quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | 642 | Two-point function \texorpdfstring{$\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$}{:W2:_qp(z) :W2:_qp(w)} |
| `thm:w3-null-level1` | `theorem` | 702 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 805 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 876 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 918 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 989 | Level-2 Gram matrix |

#### `chapters/examples/w_algebras_deep.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 83 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 786 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `prop:w3-deg3-vacuum` | `proposition` | 1295 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1502 | DS hierarchy and Koszul duality |

#### `chapters/examples/w_algebras_framework.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-algebra-koszul-main` | `theorem` | 56 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 241 | Subregular \texorpdfstring{$\mathcal{W}$}{W}-algebra duality for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} |
| `thm:w-geometric-ope` | `theorem` | 550 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 621 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-critical-bar` | `theorem` | 661 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 698 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 824 | Virasoro self-duality at \texorpdfstring{$c=0$}{c=0} |
| `thm:vir-genus1-curvature` | `theorem` | 950 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1001 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1065 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1248 | Koszul dual of \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1329 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1395 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 1465 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 1560 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 1656 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 1677 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-center-langlands` | `theorem` | 1766 | \texorpdfstring{$\mathcal{W}$}{W}-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 1871 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |

#### `chapters/examples/yangians.tex` (136)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 137 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 222 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 255 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 314 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 355 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 410 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 474 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 718 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 839 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `corollary` | 927 | Seed-normalized extraction of the dg-shifted local coefficient |
| `prop:dg-shifted-rtt-degree2-scalar-normalization` | `proposition` | 985 | Degree-\texorpdfstring{$2$}{2} scalar normalization removes the identity channel |
| `cor:dg-shifted-rtt-degree2-casimir-normalization` | `corollary` | 1107 | Trace-zero Casimir convention reduces to the same scalar packet |
| `prop:dg-shifted-rtt-degree2-fundamental-casimir` | `proposition` | 1148 | Fundamental Casimir insertion fixes the normalized one-loop scalar |
| `cor:factorization-fundamental-casimir-identity` | `corollary` | 1232 | Factorization-side fundamental Casimir identity |
| `prop:dg-shifted-factorization-shared-seed` | `proposition` | 1292 | Shared bar seed transports the fundamental degree-\texorpdfstring{$2$}{2} coefficient |
| `cor:yangian-typea-dg-local-closure` | `corollary` | 1366 | Shared bar seed closes the local dg-shifted type-\texorpdfstring{$A$}{A} MC4 packet |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1454 | Presentation-level criterion for finite RTT dg quotients |
| `prop:dg-shifted-rtt-locality-criterion` | `proposition` | 1493 | Pole-order locality criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-formula-preservation` | `proposition` | 1545 | RTT-level preservation from the rational line-operator formulas |
| `prop:dg-shifted-rtt-coefficient-criterion` | `proposition` | 1617 | Coefficient-level RTT criterion for finite-stage identification |
| `prop:dg-shifted-rtt-kernel-coefficient-criterion` | `proposition` | 1670 | Kernel-coefficient criterion for finite RTT identification |
| `prop:dg-shifted-rtt-oneloop-kernel-criterion` | `proposition` | 1720 | One-loop kernel identity criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-evaluation-detection` | `proposition` | 1778 | Evaluation-detection criterion for one-loop RTT identities |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1820 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1867 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1929 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `corollary` | 1991 | Line-side boundary-strip support bound on generic tensor powers |
| `prop:dg-shifted-rtt-defect-support-mechanism` | `proposition` | 2052 | Defect-side support mechanism from RTT degree |
| `prop:dg-shifted-rtt-universal-generic-packets` | `proposition` | 2102 | Universal generic packet reduction for the boundary strip |
| `cor:dg-shifted-rtt-minimal-canonical-family` | `corollary` | 2186 | Minimal canonical family from the boundary-strip induction |
| `prop:dg-shifted-rtt-finite-tensor-detection` | `proposition` | 2226 | Finite tensor-length detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 2307 | Top-packet induction step on the universal family |
| `prop:dg-shifted-rtt-top-packet-line-formula` | `proposition` | 2356 | Closed-form line-side top-support class on the top packet |
| `cor:dg-shifted-rtt-top-packet-comparison` | `corollary` | 2438 | Abstract top-packet comparison |
| `prop:dg-shifted-rtt-top-packet-standard-discharge` | `proposition` | 2473 | Standard-evaluation discharge of the RTT top-packet class |
| `cor:dg-shifted-rtt-top-packet-conditional-closure` | `corollary` | 2527 | Conditional closure of the top-packet induction step |
| `prop:dg-shifted-rtt-universal-evaluation-rigidity` | `proposition` | 2556 | Universal-packet evaluation rigidity from the fundamental line |
| `cor:dg-shifted-rtt-top-packet-from-one-factor` | `corollary` | 2616 | Top-packet closure from the one-factor universal packet |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 2646 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 2743 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 2813 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 2882 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 2919 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2975 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 3035 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 3096 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 3195 | Standard type-A fundamental line operator has the expected local residue |
| `prop:yangian-rank-dependence` | `proposition` | 3950 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 4087 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 4176 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 4232 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 4282 | DK-2 reduction to thick generation in category~\texorpdfstring{$\mathcal{O}$}{O} |
| `prop:dk2-thick-generation-typeA` | `proposition` | 4334 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `lem:composition-thick-generation` | `lemma` | 4428 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 4459 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 4543 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 4645 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 4667 | Finite-dimensional factorization Drinfeld--Kohno, type~\texorpdfstring{$A$}{A} |
| `cor:dk-partial-conj` | `corollary` | 4742 | Partial resolution of Conjecture~\textup{\ref{conj:full-derived-dk}} |
| `cor:dk-poly-catO` | `corollary` | 4761 | Factorization DK for polynomial category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A} |
| `lem:fd-thick-closure` | `lemma` | 4833 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 4919 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 5170 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 5279 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 5437 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 5457 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 5482 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 5655 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:derived-dk-affine` | `theorem` | 6062 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 6161 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 6314 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 6393 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 6508 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 6557 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 6694 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 6882 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 6923 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 7179 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 7300 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 7502 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 7609 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 7707 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 7913 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 7992 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 8045 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 8162 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 8221 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 8304 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 8385 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 8416 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 8453 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 8520 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 8550 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 8581 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 8640 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 8719 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 8748 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 8815 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 8847 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 8885 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 8900 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 8950 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 9007 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 9054 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 9145 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 9245 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 9285 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 9321 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 9348 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 9491 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 9523 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 9573 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 9611 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 9638 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 9671 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 9709 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 9735 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 9921 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 9972 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 10007 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 10061 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 10094 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 10145 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 10220 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts` | `corollary` | 10376 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet` | `corollary` | 10405 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization` | `corollary` | 10438 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization` | `corollary` | 10469 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet` | `corollary` | 10520 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 10627 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 10726 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 10787 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 10837 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 10896 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed` | `corollary` | 10939 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line` | `corollary` | 10972 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |

### Part III: Connections (57)

#### `chapters/connections/bv_brst.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:qme-bar-cobar` | `theorem` | 95 | Quantum master equation as Maurer--Cartan equation |
| `thm:genus0-amplitude-bar` | `theorem` | 184 | Genus-\texorpdfstring{$0$}{0} amplitudes from bar complex |
| `thm:log-form-ghost-law` | `theorem` | 269 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 379 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 537 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `thm:bar-semi-infinite-km` | `theorem` | 633 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 742 | Anomaly duality for Kac--Moody pairs |
| `thm:bar-semi-infinite-w` | `theorem` | 833 | Bar complex = semi-infinite complex for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:virasoro-semi-infinite` | `corollary` | 919 | Virasoro bar complex = semi-infinite complex |
| `cor:anomaly-duality-w` | `corollary` | 943 | Anomaly complementarity for \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |
| `thm:config-space-bv` | `theorem` | 1343 | Configuration space BV structure |
| `thm:bv-functor` | `theorem` | 1436 | BV functor |

#### `chapters/connections/concordance.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 225 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 239 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `thm:master-pbw` | `theorem` | 520 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 546 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, originally conjectured)} |
| `prop:standard-tower-mc5-reduction` | `proposition` | 728 | Standard-tower MC5 reduction after MC3 and realized MC4 |
| `cor:standard-tower-mc5-closure` | `corollary` | 816 | Standard-tower MC5 closure on the canonical Yangian locus |
| `prop:en-n2-recovery` | `proposition` | 1742 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1888 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1946 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1980 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1996 | Physical anomaly cancellation for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2214 | Hodge symmetry from complementarity |
| `thm:lagrangian-complementarity` | `theorem` | 2560 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 2595 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 2774 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 2819 | Spectral discriminant --- general case |
| `thm:family-index` | `theorem` | 3050 | Family index theorem for genus expansions |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 3631 | Volume~I concrete modular datum |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 207 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 190 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 295 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 334 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 361 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 397 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 415 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 436 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 483 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 542 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 917 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 953 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/genus_complete.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 194 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 221 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 303 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 534 | Bar complex computes moduli integrals |

#### `chapters/connections/holomorphic_topological.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:open-string-bar` | `theorem` | 310 | Open-string bar identification |
| `thm:w-algebra-bar-complex` | `theorem` | 450 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar complex |
| `thm:genus-graded-bar` | `theorem` | 529 | Genus-graded bar complex |
| `conj:w-algebra-bar-cobar` | `conjecture` | 603 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar-cobar duality |
| `thm:agt-2d-bar` | `theorem` | 743 | AGT 2D side: bar complex = semi-infinite complex |

#### `chapters/connections/kontsevich_integral.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-weight-systems` | `theorem` | 88 | Bar complex weight systems |
| `prop:propagator-restriction` | `proposition` | 157 | Propagator restriction |
| `prop:kz-from-bar` | `proposition` | 243 | KZ connection from bar complex |
| `thm:drinfeld-associator-bar` | `theorem` | 286 | Drinfeld associator from bar-cobar |

#### `chapters/connections/poincare_computations.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-c26-selfdual` | `proposition` | 145 | Virasoro NAP duality at \texorpdfstring{$c=26$}{c=26} |
| `thm:genus-complementarity` | `theorem` | 272 | Genus complementarity |

### Appendices (42)

#### `appendices/arnold_relations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:operadic-equivalence-arnold` | `proposition` | 62 | Operadic equivalence: Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d^2 = 0$}{d\textasciicircum 2 = 0} |
| `thm:bar-d-squared-arnold` | `theorem` | 81 | Bar differential squares to zero |
| `cor:bar-d-squared-zero-arnold` | `corollary` | 153 | Bar differential squares to zero |
| `thm:arnold-iff-nilpotent` | `theorem` | 169 | Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d_{\text{residue}}^2 = 0$}{d\_residue\textasciicircum 2 = 0} |
| `thm:config-boundary-relations` | `theorem` | 367 | Configuration space boundary relations |
| `cor:dres-squared-global` | `corollary` | 490 | \texorpdfstring{$d_{\mathrm{res}}^2 = 0$}{d\_res\textasciicircum 2 = 0} globally |

#### `appendices/coderived_models.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 247 | Adequacy |
| `thm:stratified-conservative-restriction` | `theorem` | 578 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 654 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 704 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 731 | Factorization co-contra correspondence |

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-pade` | `proposition` | 747 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dual_methodology.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-infty-operads` | `theorem` | 158 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |

#### `appendices/existence_criteria.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:classification-table` | `proposition` | 440 | Classification table \cite{FBZ04, BD04} |

#### `appendices/homotopy_transfer.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:sdr-existence` | `lemma` | 95 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 404 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 471 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 565 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 679 | Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0} |

#### `appendices/koszul_reference.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:extended-koszul-appendix` | `theorem` | 17 | Extended Koszul duality |
| `thm:genus-graded-koszul-duality-appendix` | `theorem` | 73 | Genus-graded Koszul duality theorem |
| `lem:genus-graded-koszul-resolution-appendix` | `lemma` | 110 | Genus-graded Koszul complex resolution |
| `thm:genus-graded-mc-appendix` | `theorem` | 131 | Genus-graded MC elements parametrize deformations |
| `thm:essential-image-koszul` | `theorem` | 293 | Essential image of Koszul duality |
| `lem:conilpotency-necessary` | `lemma` | 355 | Conilpotency is necessary |
| `lem:connectedness-augmentation` | `lemma` | 384 | Connectedness characterizes augmentation |
| `thm:koszul-geom-rep` | `theorem` | 413 | Koszul duals are geometrically representable |
| `cor:geom-implies-koszul` | `corollary` | 445 | Converse: geometric representability implies Koszul |
| `thm:curvature-central-appendix` | `theorem` | 495 | Curvature must be central |
| `thm:uniqueness-algebra` | `theorem` | 648 | Uniqueness up to quasi-isomorphism |

#### `appendices/nilpotent_completion.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:geom-conilpotent` | `proposition` | 98 | Geometric manifestation |
| `thm:completion-convergence` | `theorem` | 126 | Completion convergence |
| `thm:completed-bar-cobar` | `theorem` | 198 | Completed bar-cobar duality |
| `thm:koszul-dual-characterization` | `theorem` | 258 | Characterization of Koszul duals |

#### `appendices/sign_conventions.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:LV-conversion-complete` | `proposition` | 381 | Loday--Vallette conversion |

#### `appendices/signs_and_shifts.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:graded-jacobi` | `proposition` | 40 | Graded Jacobi identity |
| `prop:duality-grading` | `proposition` | 169 | Duality and grading reversal |
| `prop:susp-diff` | `proposition` | 273 | Suspension and differentials |

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
