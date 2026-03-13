# Theorem Registry

Auto-generated on 2026-03-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 1070 |
| Total tagged claims | 1562 |
| Active files in `main.tex` | 61 |
| Total `.tex` files scanned | 70 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1070 |
| `ProvedElsewhere` | 324 |
| `Conjectured` | 140 |
| `Heuristic` | 28 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 421 |
| `proposition` | 359 |
| `corollary` | 176 |
| `lemma` | 68 |
| `computation` | 34 |
| `remark` | 7 |
| `calculation` | 3 |
| `conjecture` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 7 |
| Part I: Theory | 560 |
| Part II: Examples | 415 |
| Part III: Connections | 51 |
| Appendices | 37 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/bar_cobar_construction.tex` | 178 |
| `chapters/theory/higher_genus.tex` | 168 |
| `chapters/examples/yangians.tex` | 139 |
| `chapters/examples/free_fields.tex` | 51 |
| `chapters/theory/chiral_modules.tex` | 49 |
| `chapters/theory/configuration_spaces.tex` | 39 |
| `chapters/examples/genus_expansions.tex` | 34 |
| `chapters/examples/kac_moody_framework.tex` | 34 |
| `chapters/examples/lattice_foundations.tex` | 32 |
| `chapters/theory/chiral_koszul_pairs.tex` | 26 |
| `chapters/examples/detailed_computations.tex` | 25 |
| `chapters/theory/deformation_theory.tex` | 23 |
| `chapters/theory/koszul_pair_structure.tex` | 20 |
| `chapters/examples/w_algebras_framework.tex` | 19 |
| `chapters/connections/concordance.tex` | 18 |
| `chapters/examples/examples_summary.tex` | 18 |
| `chapters/examples/beta_gamma.tex` | 15 |
| `chapters/examples/w3_composite_fields.tex` | 13 |
| `chapters/theory/fourier_seed.tex` | 13 |
| `chapters/connections/bv_brst.tex` | 12 |

## Complete Proved Registry

### Frame (7)

#### `chapters/frame/heisenberg_frame.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 470 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 914 | Heisenberg bar complex at genus~$0$ |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1016 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1176 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1198 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1371 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1567 | Quantum complementarity for Heisenberg |

### Part I: Theory (560)

#### `chapters/theory/algebraic_foundations.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 204 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 461 | Geometric realization |
| `prop:orthogonal` | `proposition` | 595 | Orthogonality |
| `__unlabeled_chapters/theory/algebraic_foundations.tex:653` | `computation` | 653 | Explicit verification |

#### `chapters/theory/bar_cobar_construction.tex` (178)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 236 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 477 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 567 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 625 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 691 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 719 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 814 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 856 | Arnold relations |
| `comp:deg0` | `computation` | 964 | Degree 0 |
| `comp:deg1-general` | `computation` | 982 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1095 | Bar construction is functorial |
| `lem:bar-induced-chain-map` | `lemma` | 1135 | Induced map is chain map |
| `lem:bar-induced-coalgebra` | `lemma` | 1168 | Induced map is coalgebra morphism |
| `cor:bar-natural` | `corollary` | 1233 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1239 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1271 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1294 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1361 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1412 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1429 | Differential is coderivation |
| `thm:bar-differential` | `theorem` | 1493 | Bar differential |
| `lem:orientation` | `lemma` | 1584 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1610 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1634 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1698 | Geometric bar $=$ operadic bar |
| `thm:residue-formula` | `theorem` | 1773 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1835 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1945 | Bar complex is chiral |
| `lem:bar-holonomicity` | `lemma` | 2100 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 2161 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 2194 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 2273 | $d_{\mathrm{cobar}}^2 = 0$ via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 2349 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 2463 | Verification of $d_{\text{cobar}}^2 = 0$ |
| `lem:cobar-sign-consistency` | `lemma` | 2711 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 2871 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 3089 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 3220 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 3266 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 3510 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 3558 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 3579 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 3625 | Topology |
| `thm:poincare-verdier` | `theorem` | 3684 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 3773 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 3797 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 3843 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 3978 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 4074 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 4215 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 4240 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 4293 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 4346 | Recognition principle |
| `thm:deformation-obstruction` | `theorem` | 4556 | Quantum deformation-obstruction complementarity |
| `lem:deformation-space` | `lemma` | 4717 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 4759 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 4807 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 4886 | Curved differential formula |
| `thm:curvature-central` | `theorem` | 4962 | Curvature as $\mu_1$-cycle |
| `thm:completion-necessity` | `theorem` | 5009 | When completion is necessary |
| `prop:curved-bar-acyclicity` | `proposition` | 5056 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 5152 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 5221 | Conilpotency ensures convergence |
| `prop:mc4-reduction-principle` | `proposition` | 5417 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 5501 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 5538 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 5576 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 5625 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 5676 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 5709 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 5773 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 5809 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 5885 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 5982 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 6009 | Factorization-envelope criterion for principal stages |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 6132 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 6184 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 6238 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 6284 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 6334 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 6384 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 6437 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 6477 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 6518 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 6615 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 6675 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 6756 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 6818 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 6859 | Stage-$3$ principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 6955 | Stage-$4$ residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 7088 | Stage-$4$ top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 7131 | Stage-$4$ parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 7164 | Stage-$4$ packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 7231 | Stage-$4$ frontier as one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 7264 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 7326 | Stage-$4$ mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 7366 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 7431 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 7458 | Stage-$4$ mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 7504 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 7599 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 7682 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 7712 | Principal stage-$4$ self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 7729 | Stage-$4$ principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 7796 | Exact MC4 frontier packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 7869 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 frontier |
| `cor:winfty-dual-candidate-construction` | `corollary` | 7908 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 7955 | Stage-$4$ \texorpdfstring{$W_\infty$}{W_infty} frontier on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 8014 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-$4$ contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 8132 | Stage-$4$ visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 8203 | Stage-$4$ visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 8317 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-$4$ input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 8365 | Stage-$4$ swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 8449 | Stage-$4$ residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 8488 | Stage-$4$ higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 8614 | Equivalent exact forms of the remaining stage-$4$ higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 8688 | Exact local attack order for the stage-$4$ \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 8786 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 8863 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 8905 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-higher-spin-subblocks` | `proposition` | 8956 | First higher-spin packet as four exact source-pair subblocks |
| `cor:winfty-stage5-entry-transport` | `corollary` | 9027 | Stage-$5$ entry packet and mixed transport packet |
| `cor:winfty-stage5-entry-singletons` | `corollary` | 9086 | Entry packet as two singleton channels |
| `prop:winfty-stage5-entry-mixed-self` | `proposition` | 9118 | Stage-$5$ entry packet as mixed-entry and self-return singletons |
| `prop:winfty-stage5-reduced-tail-singleton` | `proposition` | 9159 | Exact reduced tail input at stage~$5$ |
| `prop:winfty-stage5-tail-mechanism` | `proposition` | 9189 | Exact missing mechanism for the reduced stage-$5$ tail singleton |
| `prop:winfty-stage5-transport-target-ladders` | `proposition` | 9223 | Stage-$5$ mixed transport packet as three fixed-target ladders |
| `prop:winfty-stage5-higher-spin-target-blocks` | `proposition` | 9274 | Stage-$5$ higher-spin packet by target spin |
| `cor:winfty-stage5-target5-corridor` | `corollary` | 9328 | Stage-$5$ target-$5$ corridor |
| `cor:winfty-stage5-target5-residual` | `corollary` | 9371 | Residual target-$5$ continuation after the tail singleton |
| `prop:winfty-stage5-target5-transport-mechanism` | `proposition` | 9404 | Residual target-$5$ continuation as mixed transport of the new generator |
| `prop:winfty-stage5-target5-transport-singletons` | `proposition` | 9440 | Residual target-$5$ continuation as two singleton transport channels |
| `prop:winfty-stage5-transport-pole-profiles` | `proposition` | 9491 | Stage-$5$ transport ladders ordered by pole profile |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 9535 | Stage-$5$ visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 9568 | Stage-$5$ target-$5$ pole-$3$ transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 9640 | Stage-$5$ target-$5$ pole-$4$ transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 9702 | Stage-$5$ target-$5$ pole-$4$ transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 9755 | Stage-$5$ self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 9775 | Stage-$5$ reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 9850 | Stage-$5$ reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 9932 | Stage-$5$ tail singleton equates neighboring target-$4$ and target-$3$ transport channels on the visible \texorpdfstring{$W^{(3)}$}{W3}/\texorpdfstring{$W^{(4)}$}{W4} pairing locus |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 9961 | Stage-$5$ target-$5$ corridor contracts to the tail singleton on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 9991 | Stage-$5$ target-$5$ corridor carries no new independent coefficient on the full visible \texorpdfstring{$W^{(3)}$}{W3}/\texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 10018 | Stage-$5$ target-$4$ pole-$5$ transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 10057 | Stage-$5$ target-$3$ pole-$5$ transport singleton vanishes on a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 10096 | Stage-$5$ target-$4$/target-$3$ transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 10163 | Stage-$5$ mixed transport frontier carries one effective independent coefficient on the full visible pairing locus |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 10197 | Stage-$5$ higher-spin packet reduces to one effective independent coefficient on the full visible pairing locus |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 10241 | Exact local attack order for the first stage-$5$ higher-spin packet |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 10685 | Principal stage-$4$ higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 10916 | Centrality implies strict nilpotence |
| `thm:mc-deformations` | `theorem` | 11245 | MC elements as quantum deformations |
| `thm:mc-periods` | `theorem` | 11281 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 11340 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 11352 | Strict nilpotence at all genera |
| `cor:genus-expansion-converges` | `corollary` | 11575 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 11635 | Functoriality of bar construction |
| `prop:filtered-to-curved` | `proposition` | 11997 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 12216 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 12527 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 12642 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 12715 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 12759 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 12827 | Key properties of $\Phi_C^{\mathrm{ch}}$ and $\Psi_C^{\mathrm{ch}}$ |
| `thm:chiral-co-contra-correspondence` | `theorem` | 12893 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 13028 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 13094 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 13214 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 13347 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 13363 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 13419 | Collapse at $E_2$ |
| `thm:genus-graded-convergence` | `theorem` | 13442 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 13502 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 13547 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 13559 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 13594 | Derived equivalence |
| `prop:bar-fh` | `proposition` | 13825 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 13903 | Cobar as factorization cohomology |

#### `chapters/theory/chiral_koszul_pairs.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 123 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 150 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 170 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 198 | Fundamental theorem of chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 496 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 585 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 640 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 684 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 855 | Bar concentration for Koszul pairs |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 937 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 1116 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 1176 | Yangian Koszulness for all simple $\mathfrak{g}$ |
| `thm:coalgebra-axioms-verified` | `theorem` | 1439 | Coalgebra structure on $\mathcal{A}_2^!$ |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 1533 | Bar computes Koszul dual — complete statement |
| `lem:completion-convergence` | `lemma` | 1621 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 1670 | Circularity-free Koszul duality |
| `thm:feynman-bar-cobar` | `theorem` | 2349 | Feynman-bar-cobar correspondence |
| `thm:e1-chiral-koszul-duality` | `theorem` | 2450 | $\Eone$-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 2668 | $\Eone$--$\Eone$ Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 2733 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 2794 | $\Eone$-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 2917 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 2959 | $A_\infty$ duality |
| `prop:ff-involution-uniqueness` | `proposition` | 3013 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 3048 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 3243 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 162 | Fusion product of Heisenberg Fock modules |
| `thm:monoidal-module-koszul` | `theorem` | 250 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 400 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 490 | Conformal blocks via the bar complex |
| `prop:kzb-bar-complex` | `proposition` | 604 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 772 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 869 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1326 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1387 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1602 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1674 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1709 | $\mathcal{W}$-algebra Zhu algebras are Koszul-invariant |
| `prop:orbit-duality` | `proposition` | 1871 | Orbit duality for affine vertex algebras |
| `prop:logarithmic-bar` | `proposition` | 1996 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2100 | $\mathrm{Ext}$ groups for $\mathcal{W}(2)$ via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2225 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2260 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2299 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2316 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2356 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2378 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2528 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2635 | BGG pipeline for $\widehat{\mathfrak{sl}}_2$ at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2749 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 2829 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 2993 | $\mathrm{Ext}$ groups at level~$2$ |
| `rem:ext-koszul-dual-level` | `remark` | 3024 | $\mathrm{Ext}$ complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3076 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3178 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3264 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3323 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3399 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3476 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3538 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3658 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3712 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3778` | `calculation` | 3778 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3805` | `calculation` | 3805 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3836` | `calculation` | 3836 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 3954 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4113 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4186 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4268 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4310 | $\mathcal{W}$-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4365 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4407 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4551 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4702 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4803 | Heisenberg fusion splitting |

#### `chapters/theory/configuration_spaces.tex` (39)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 225 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 335 | Normal crossings |
| `thm:closure-relations` | `theorem` | 430 | Closure relations |
| `thm:log-complex` | `theorem` | 543 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 582 | Arnold relations |
| `lem:basic-log-form-residue` | `lemma` | 622 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 689 | Residue operations |
| `prop:residue-local` | `proposition` | 744 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 793 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1007 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1074 | Conformal blocks from punctured bar complex |
| `prop:eta` | `proposition` | 1238 | Properties of $\eta_{ij}$ |
| `thm:elliptic-compactification` | `theorem` | 1488 | Elliptic compactification |
| `thm:FM-convergence` | `theorem` | 1590 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1649 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1755 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1797 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 1824 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 1846 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 1886 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 1910 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 1945 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 1967 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 2001 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2017 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2125 | Nilpotency from Arnold relations |
| `thm:arnold-geometric` | `theorem` | 2165 | Arnold relations: geometric form |
| `cor:stokes-differential` | `corollary` | 2276 | Stokes theorem and differential |
| `thm:arnold-algebraic` | `theorem` | 2289 | Arnold relations: algebraic form |
| `thm:arnold-equivalence-complete` | `theorem` | 2408 | Equivalence of Arnold formulations |
| `thm:arnold-jacobi` | `theorem` | 2625 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2678 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2724 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2756 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2801 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 3032 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 3103 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 3240 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3450` | `computation` | 3450 | Explicit examples |

#### `chapters/theory/deformation_theory.tex` (23)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 121 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 272 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 310 | Hochschild spectral sequence |
| `thm:main-koszul-hoch` | `theorem` | 480 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 593 | Deformation-obstruction exchange at genus $0$ |
| `comp:boson-hochschild` | `computation` | 728 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 754 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 831 | Genus-$0$ cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 925 | Killing cocycle $L_\infty$ extension |
| `cor:km-cyclic-deformation` | `corollary` | 1023 | Kac--Moody cyclic deformation complex |
| `thm:mc2-1-km` | `theorem` | 1159 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1276 | Minimal cyclic $L_\infty$ model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 1583 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 1669 | Cyclic $L_\infty$ structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 1776 | Recovery of the Killing cocycle extension |
| `rem:step2-stabilization-threshold` | `remark` | 2041 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 2388 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 2489 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 2548 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 2935 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 3080 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 3127 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 3323 | Boson-fermion duality |

#### `chapters/theory/derived_langlands.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:oper-bar-h0-dl` | `theorem` | 181 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 216 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 240 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 277 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 369 | Differential analysis at arity 3 |
| `prop:d4-nonvanishing` | `proposition` | 449 | Non-vanishing of $d_4$ |
| `cor:h3-oper` | `corollary` | 508 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 521 | Full derived identification |
| `prop:bar-as-localization` | `proposition` | 629 | The bar complex as localization |
| `prop:sl2-periodicity-dl` | `proposition` | 775 | Affine sl2 periodicity |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 851 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/en_koszul_duality.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:linking-sphere-residue` | `proposition` | 308 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 383 | $d^2 = 0$ from Totaro relations |
| `cor:n2-recovery` | `corollary` | 566 | Recovery of chiral bar-cobar at $n = 2$ |
| `prop:refines-af` | `proposition` | 624 | Our construction refines AF at $n = 2$ |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 20 | Filtered $\Rightarrow$ curved |
| `thm:bar-convergence-fc` | `theorem` | 123 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 44 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 101 | Genus-$1$ propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 210 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 256 | $n = 2$ |
| `comp:fourier-heisenberg-n3` | `computation` | 304 | $n = 3$ |
| `thm:fourier-heisenberg-bar` | `theorem` | 333 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 374 | Heisenberg on $E_\tau$ |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 401 | — |
| `comp:fourier-km-bar` | `computation` | 464 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 485 | — |
| `thm:fourier-specialization` | `theorem` | 520 | Specialization |
| `thm:fourier-four-properties` | `theorem` | 575 | The four properties of the Fourier transform |
| `rem:fourier-genus-preview` | `remark` | 675 | ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus.tex` (168)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | 392 | $A_\infty$ structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 450 | $A_\infty$ operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 541 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 654 | Cobar $A_\infty$ structure |
| `thm:chain-vs-homology` | `theorem` | 761 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 911 | Verdier duality of operations |
| `thm:geometric-com-lie-enhancement` | `theorem` | 982 | Geometric enhancement of Com-Lie |
| `thm:ainfty-com-lie-interchange` | `theorem` | 1019 | Maximal vs.\ trivial $A_\infty$ |
| `thm:convergence-filtered` | `theorem` | 1108 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1299 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1332 | $\beta\gamma$ deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1366 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1386 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1402 | Higher associahedron identity for $m_6$ |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 1703 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 1813 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2028 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2296 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2532 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2596 | Concrete quantum differential |
| `thm:modular-vs-quasi` | `theorem` | 2766 | Modular vs quasi-modular |
| `thm:eta-properties-genus1` | `theorem` | 2849 | Properties of $\eta_{ij}^{(1)}$ |
| `thm:arnold-genus1` | `theorem` | 2904 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 2989 | Nilpotency at genus 1 |
| `thm:e1-page-complete` | `theorem` | 3259 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3292 | $E_2$ page structure |
| `thm:obstruction-quantum` | `theorem` | 3419 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3506 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3560 | Heisenberg obstruction at genus $g$ |
| `thm:kac-moody-obs` | `theorem` | 3638 | Kac--Moody obstruction at genus $g$ |
| `thm:w3-obstruction` | `theorem` | 3755 | $W_3$ obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 3826 | Explicit genus-$1$ value of the $W_3$ obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 3847 | Nilpotence of obstruction ($g \leq 2$) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 3876 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 3978 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4080 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4197 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4230 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4246 | $\kappa$-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4262 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4280 | Obstruction complementarity for $\mathcal{W}_N$ |
| `cor:critical-level-universality` | `corollary` | 4303 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4325 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4358 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4459 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4489 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4568 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4612 | Grothendieck--Riemann--Roch bridge |
| `lem:involution-splitting` | `lemma` | 4795 | Involution splitting in characteristic~$0$ |
| `lem:perfectness-criterion` | `lemma` | 4850 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 4924 | Fiber--center identification \textup{(Theorem~$\mathrm{C}_0$)} |
| `thm:quantum-complementarity-main` | `theorem` | 5036 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 5245 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 5300 | Spectral sequence for quantum corrections |
| `lem:quantum-from-ss` | `lemma` | 5383 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 5420 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 5565 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 5631 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 5671 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 5725 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 5754 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 5942 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 5977 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 6029 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 6117 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 6148 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 6168 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 6234 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 6335 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 6466 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 6548 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 6657 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 6685 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 6722 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 6778 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 6814 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 6840 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 7126 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 7285 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 7335 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 7348 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 7390 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 7449 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 7491 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 7519 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 7541 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 7585 | Key property: $\Dg{g}^{\,2} = 0$ |
| `lem:quantum-preserves-acyclicity` | `lemma` | 7636 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 7684 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 7772 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 7799 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 7827 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 7861 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 7886 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 7946 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 7992 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 8031 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 8060 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 8084 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 8109 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 8141 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 8160 | Boundary-stratum compatibility of $\psi_g$ |
| `lem:extension-across-boundary-qi` | `lemma` | 8182 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 8198 | Higher genus inversion |
| `prop:pants-excision` | `proposition` | 8406 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 8454 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 8574 | $E_2$-collapse as formality |
| `thm:genus-graded-koszul` | `theorem` | 8725 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 8756 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 9141 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 9174 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 9215 | PBW concentration at all genera for principal finite-type $\mathcal{W}$-algebras |
| `thm:pbw-genus1-km` | `theorem` | 9385 | PBW degeneration at genus~$1$ for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 9652 | Unconditional modular Koszulity at genus~$1$ |
| `thm:pbw-allgenera-km` | `theorem` | 9677 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 9874 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 9922 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 10022 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 10068 | Unconditional modular Koszulity for principal finite-type $\mathcal{W}$-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 10125 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:genus-internalization` | `theorem` | 10481 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 10602 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 10697 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 10740 | Universal modular Maurer--Cartan class |
| `thm:explicit-theta` | `theorem` | 10800 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 11016 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 11509 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 11588 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 11701 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 11735 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 11767 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 11972 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 12048 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 12113 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 12248 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 12345 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 12456 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 12593 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 12745 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 12919 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 13069 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 13263 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 13383 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 13482 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 13572 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 13684 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 13756 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 13838 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 13916 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 13993 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 14069 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 14144 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 14210 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 14349 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 14424 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 14471 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 14521 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 14602 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 14656 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 14689 | Scalar saturation for $\mathcal{W}$-algebras |
| `prop:ds-package-functoriality` | `proposition` | 14726 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 14811 | Scalar saturation for non-principal $\mathcal{W}$-algebras |
| `prop:saturation-equivalence` | `proposition` | 15065 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 15232 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 15395 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 15478 | Cyclic rigidity at generic level |
| `thm:tautological-line-support` | `theorem` | 15983 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 16120 | MC2 reduced to cyclic model |

#### `chapters/theory/hochschild_cohomology.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 86 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 130 | W-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:328` | `computation` | 328 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 384 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 464 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 719 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 751 | Hochschild cup product exchange |

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 612 | Central charge complementarity |
| `prop:chirAss-self-dual` | `proposition` | 1141 | $\chirAss$ self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | 122 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 160 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 200 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 219 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 276 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 339 | $A_\infty$ structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 398 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 539 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 661 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 676 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 861 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 993 | Maurer--Cartan correspondence — quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 1119 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1149 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1351 | Positselski comodule-contramodule equivalence |
| `thm:full-derived-module-equiv` | `theorem` | 1399 | Full derived module equivalence |
| `thm:cs-koszul-km` | `theorem` | 1516 | Chern--Simons equations from Koszul duality |
| `thm:linf-mc-flatness` | `theorem` | 1593 | $L_\infty$ Maurer--Cartan as homotopy flatness |
| `thm:cs-koszul-general` | `theorem` | 1663 | CS/Koszul for general non-quadratic algebras |
| `thm:bv-structure-bar` | `theorem` | 1902 | BV structure on bar complex |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 182 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 294 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 361 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 452 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 511 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 527 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 593 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 676 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bg-bar-coalg` | `theorem` | 440 | $\beta\gamma$ bar complex coalgebra |
| `prop:chiral-operad-genus0` | `proposition` | 569 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 613 | Prism principle --- operadic identification |
| `thm:prism-higher-genus` | `theorem` | 822 | Prism principle --- higher-genus extension |
| `cor:prism-principle` | `corollary` | 929 | The prism principle |
| `thm:partition` | `theorem` | 1080 | Partition complex structure |

### Part II: Examples (415)

#### `chapters/examples/beta_gamma.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 38 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 86 | Bar cohomology of $\beta\gamma$ |
| `thm:betagamma-fermion-koszul` | `theorem` | 121 | Koszul dual of $\beta\gamma$ |
| `prop:bar-bc-system` | `proposition` | 174 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 212 | Cobar gives $\beta\gamma$ |
| `prop:betagamma-bar-deg2` | `proposition` | 232 | — |
| `thm:cobar-fermions` | `theorem` | 260 | Cobar gives fermions |
| `thm:betagamma-bc-koszul-detailed` | `theorem` | 296 | $\beta\gamma \leftrightarrow bc$ Koszul duality |
| `thm:beta-gamma-bar` | `theorem` | 495 | Bar complex of the $\beta$-$\gamma$ system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 762 | Acyclicity of the $\beta\gamma$ bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 882 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 983 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1124 | $E_1$ page |
| `prop:betagamma-ss-collapse` | `proposition` | 1208 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1359 | $\mathbb{Z}_2$-equivariant bar cohomology |

#### `chapters/examples/deformation_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 508 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 613 | Deformation--duality compatibility |

#### `chapters/examples/deformation_quantization.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 111 | Coisson quantization at genus $0$ |
| `thm:chiral-kontsevich` | `theorem` | 164 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 396 | MC $\Leftrightarrow$ star product |
| `thm:deformation-genus-expansion` | `theorem` | 509 | Genus expansion |

#### `chapters/examples/detailed_computations.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 714 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 807 | Modular rank of $\widehat{\mathfrak{sl}}_3$ bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 886 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 947 | PBW spectral sequence for $\widehat{\mathfrak{sl}}_3$ |
| `comp:sl3-casimir-decomp` | `computation` | 1040 | Casimir decomposition of $\mathfrak{sl}_3^{\otimes n}$ |
| `comp:sl3-koszul-dual-scan` | `computation` | 1123 | Quadratic relation scan for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `prop:so5-bar-dims` | `proposition` | 1452 | Bar complex dimensions for $\widehat{\mathfrak{so}}_{5,k}$ |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1757 | PBW $E_2$ from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1803 | Degree-3 bar differential and curvature for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `comp:sl2-ce-sdr` | `computation` | 1874 | SDR and formality for $\mathfrak{sl}_2$ |
| `comp:sl2-ce-verification` | `computation` | 1925 | CE cohomology of $\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2054 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2090 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2124 | BGG resolution of $L(\Lambda_0)$ via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2554 | Bar complex dimensions for $\widehat{G}_{2,k}$ |
| `prop:arnold-virasoro-deg3` | `proposition` | 2729 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2949 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 3003 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3040 | $\mathcal{W}_3$ vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3314 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3493 | $E_8$ bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3790 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3852 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4049 | Bar--BGG for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `cor:bgg-koszul-involution` | `corollary` | 4199 | BGG involution under Koszul duality |

#### `chapters/examples/examples_summary.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 236 | Paired standard-tower MC4 frontier packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 431 | Minimal closure conditions for the standard-tower MC4 frontier |
| `cor:genus1-anomaly-ratio` | `corollary` | 561 | Genus-$1$ free energy and anomaly ratio |
| `prop:bar-dimensions` | `proposition` | 770 | Koszul dual Hilbert functions |
| `cor:subexp-free-field` | `corollary` | 1002 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 1012 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 1029 | DS reduction and bar cohomology generating functions |
| `prop:hred-sl2` | `proposition` | 1324 | Construction of $H^{\mathrm{red}}_1$ for $\mathfrak{sl}_2$ |
| `prop:discriminant-characteristic` | `proposition` | 1524 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1615 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1712 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1778 | Pole decomposition and singularity type |
| `rem:bar-deg2-symmetric-square` | `remark` | 1833 | Degree-$2$ bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1884 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1899 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 1988 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2177 | {$\beta\gamma$ generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2483 | Spectral sequence collapse |

#### `chapters/examples/free_fields.tex` (51)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fermion-bar-complex-genus-0` | `theorem` | 48 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 107 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 179 | $\beta\gamma$ bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 190 | $\beta\gamma$ bar complex rank |
| `prop:bc-betagamma-orthogonality` | `proposition` | 251 | $bc$--$\beta\gamma$ orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 274 | $\beta\gamma$--$bc$ Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 457 | Module Koszul duality for $\beta\gamma$--$bc$ |
| `thm:single-fermion-boson-duality` | `theorem` | 532 | Single-generator fermion-boson duality |
| `thm:heisenberg-bar` | `theorem` | 584 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 607 | Orientation consistency |
| `prop:curved-convergence` | `proposition` | 642 | Convergence in curved structure |
| `thm:monodromy-finite` | `theorem` | 661 | Monodromy finiteness |
| `thm:heisenberg-curved-structure` | `theorem` | 683 | Heisenberg curved structure |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 714 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 746 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 881 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 937 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 987 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1029 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1204 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1280 | Spectral flow under Koszul duality |
| `thm:lattice-voa-bar` | `theorem` | 1356 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1385 | $A_2$ lattice computation |
| `thm:virasoro-moduli` | `theorem` | 1428 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 1460 | Geometric interpretation |
| `thm:elliptic-fermion-bar` | `theorem` | 1501 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1538 | Higher genus Heisenberg |
| `rem:koszul-table-status` | `remark` | 1620 | Status of Koszul duality identifications |
| `thm:filtered-bar-complex` | `theorem` | 1796 | Filtered bar complex |
| `thm:virasoro-string` | `theorem` | 1962 | Virasoro-string duality |
| `thm:w-algebra-bar-flag` | `theorem` | 2110 | $\mathcal{W}$-algebra bar complex |
| `thm:wakimoto-bar` | `theorem` | 2174 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 2204 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 2237 | $A_\infty$ structure on $\mathcal{W}$-algebras |
| `thm:w-integrability` | `theorem` | 2309 | Quantum integrability via $A_\infty$ |
| `thm:heisenberg-not-self-dual` | `theorem` | 2416 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2495 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2591 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2920 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 3070 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 3424 | $\En$ Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 3685 | Heisenberg bar complex: complete calculation |
| `rem:bar-dims-partitions` | `remark` | 3732 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3791 | Heisenberg level inversion: curved duality |
| `thm:algebraic-string-dictionary` | `theorem` | 3868 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 3920 | Genus-$0$ string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 3962 | Genus-$g$ chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 4122 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 4213 | Bar complex computes genus-$g$ string integrands |
| `thm:modular-invariance` | `theorem` | 4385 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 4422 | Modular anomaly for KM and $\mathcal{W}$-algebras |

#### `chapters/examples/genus_expansions.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 26 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 103 | $\beta\gamma$ genus expansion |
| `thm:lattice-all-genera` | `theorem` | 147 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 182 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 233 | $\mathcal{W}$-algebra free energy at all genera |
| `thm:sl2-all-genera` | `theorem` | 445 | $\widehat{\mathfrak{sl}}_2$ free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 520 | $\widehat{\mathfrak{sl}}_2$ complementarity |
| `prop:bivariate-gf` | `proposition` | 546 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 588 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 642 | Genus-2 bar differential for $\widehat{\mathfrak{sl}}_2$ |
| `thm:sl2-genus2-curvature` | `theorem` | 753 | Genus-2 curvature for $\widehat{\mathfrak{sl}}_2$ |
| `prop:sl2-genus2-relation` | `proposition` | 863 | Genus-2 relation for $\widehat{\mathfrak{sl}}_2$ |
| `thm:virasoro-genus2-bar` | `theorem` | 1059 | Genus-2 bar differential for $\mathrm{Vir}_c$ |
| `cor:virasoro-genus2-curvature` | `corollary` | 1126 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1207 | $\mathcal{W}_3$ genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1308 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1461 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1491 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1508 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1534 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1619 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1747 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1789 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1887 | $\widehat{\mathfrak{sl}}_3$ complementarity |
| `thm:fermion-all-genera` | `theorem` | 2036 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2101 | $bc$--$\beta\gamma$ complementarity |
| `prop:complementarity-classification` | `proposition` | 2349 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2403 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2604 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2728 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2744 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2769 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2801 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 2928 | Loop expansion interpretation |

#### `chapters/examples/heisenberg_eisenstein.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-genus-one-complete` | `theorem` | 106 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 193 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 235 | Genus-2 obstruction class for $\mathcal{H}_\kappa$ |
| `thm:heisenberg-all-genus` | `theorem` | 353 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 456 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 505 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 717 | Multi-boson Eisenstein corrections |

#### `chapters/examples/kac_moody_framework.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-ope-kac-moody` | `theorem` | 204 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 238 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 278 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 344 | Koszul dual of $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:sl3-koszul-dual` | `theorem` | 464 | Koszul dual of $\widehat{\mathfrak{sl}}_{3,k}$ |
| `rem:bar-dims-level-independent` | `remark` | 495 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 533 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 591 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 642 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 727 | Universal Koszul duality for affine Kac--Moody |
| `prop:ff-channel-shear` | `proposition` | 839 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 889 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 955 | $\mathcal{W}$-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1029 | $A_\infty$ operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1068 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1122 | Closed-form OPE for Koszul dual |
| `thm:km-quantum-groups` | `theorem` | 1232 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 1572 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 1642 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 1730 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 1850 | KW formula via bar complex: general simple $\mathfrak{g}$ |
| `prop:admissible-verlinde-bar` | `proposition` | 1934 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2173 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 2254 | Genus-1 curvature for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:sl2-genus1-inversion` | `theorem` | 2319 | Genus-1 bar-cobar inversion for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:sl2-genus1-complementarity` | `theorem` | 2371 | Genus-1 complementarity for $\widehat{\mathfrak{sl}}_{2,k}$ at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 2437 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 2510 | Genus-1 curvature for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `thm:sl3-genus1-inversion` | `theorem` | 2556 | Genus-1 bar-cobar inversion for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `thm:sl3-genus1-complementarity` | `theorem` | 2595 | Genus-1 complementarity for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `prop:sl3-genus1-partition` | `proposition` | 2632 | Partition function for $\widehat{\mathfrak{sl}}_{3,k}$ at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 2884 | Oper space from bar complex at $H^0$ |
| `prop:oper-bar-h1` | `proposition` | 2914 | $H^1$ at critical level |
| `thm:oper-bar` | `theorem` | 2944 | Full derived oper identification |

#### `chapters/examples/lattice_foundations.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:lattice:cocycle-class` | `lemma` | 177 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 339 | $\Eone$ vs.\ $\Einf$ classification |
| `thm:lattice:bar-structure` | `theorem` | 558 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 655 | $D_4$ bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 678 | $E_8$ bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 712 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 746 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 791 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 877 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 922 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1141 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1186 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1228 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1251 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1392 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1409 | $D_4$ and triality |
| `prop:lattice-module-koszul` | `proposition` | 1434 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1637 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1821 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2446 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2514 | $\Eone$ bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2588 | $\Eone$ inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2747 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3051 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3132 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3302 | Factorization DK at level $1$ |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3499 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3542 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3700 | Level-$k$ lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3747 | Level-$k$ factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 3833 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 3905 | Lattice--Yangian DK bridge at level $1$ |

#### `chapters/examples/minimal_model_examples.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 461 | Fusion from bar complex on the torus |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 74 | $W_3$ minimal models |
| `thm:grothendieck-structure` | `theorem` | 209 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 364 | $\mathcal{M}(5,4)$ primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 388 | Quantum dimensions for $\mathcal{M}(5,4)$ |
| `comp:s-matrix-5-4` | `computation` | 417 | S-matrix for $\mathcal{M}(5,4)$ |
| `comp:fusion-5-4` | `computation` | 442 | Fusion rules for $\mathcal{M}(5,4)$ |
| `comp:m65-primaries` | `computation` | 521 | $\mathcal{M}(6,5)$ primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 548 | Fusion rules for $\Phi_{1,2}$ in $\mathcal{M}(6,5)$ |
| `thm:fusion-ring-generators` | `theorem` | 608 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 628 | Fusion ring for $\mathcal{M}(p,2)$ |
| `thm:fusion-ring-quotient` | `theorem` | 655 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 751 | Twist values for $\mathcal{M}(5,4)$ |

#### `chapters/examples/toroidal_elliptic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 440 | Fay identity implies elliptic $d^2 = 0$ |
| `thm:elliptic-vs-rational` | `theorem` | 538 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 910 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1106 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1184 | DYBE and bar nilpotency |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 40 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 142 | Mode expansion |
| `thm:c-scaling` | `theorem` | 193 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 292 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 457 | Quasi-primarity of $\Lambda_2$ and $\Lambda_3$ |
| `comp:weight6-two-point` | `computation` | 541 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 592 | Quasi-primary projection of ${:}W^2{:}$ |
| `comp:W2-twopt` | `computation` | 653 | Two-point function $\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$ |
| `thm:w3-null-level1` | `theorem` | 713 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 816 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 887 | $W_3$ Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 929 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 1000 | Level-2 Gram matrix |

#### `chapters/examples/w_algebras_deep.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 92 | $\mathcal{W}$-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 794 | Factorization Koszul dual of $\mathcal{W}_\infty$ via DS--sectorwise convergence |
| `prop:w3-deg3-vacuum` | `proposition` | 1313 | $\mathcal{W}_3$ degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1520 | DS hierarchy and Koszul duality |

#### `chapters/examples/w_algebras_framework.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-algebra-koszul-main` | `theorem` | 57 | $\mathcal{W}$-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 277 | Subregular $\mathcal{W}$-algebra duality for $\mathfrak{sl}_3$ |
| `thm:w-geometric-ope` | `theorem` | 630 | Geometric OPE formula for $\mathcal{W}$-algebras |
| `thm:w-bar-curvature` | `theorem` | 701 | Curvature of $\mathcal{W}$-algebra $A_\infty$ structure |
| `thm:w-critical-bar` | `theorem` | 741 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 778 | Koszul duality for $\mathcal{W}$-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 944 | Virasoro self-duality at $c=0$ |
| `thm:vir-genus1-curvature` | `theorem` | 1070 | Genus-1 curvature for $\mathrm{Vir}_c$ |
| `thm:vir-genus1-inversion` | `theorem` | 1121 | Genus-1 bar-cobar inversion for $\mathrm{Vir}_c$ |
| `thm:vir-genus1-complementarity` | `theorem` | 1185 | Genus-1 complementarity for $\mathrm{Vir}_c$ |
| `thm:w3-koszul-dual` | `theorem` | 1368 | Koszul dual of $\mathcal{W}_3$ |
| `thm:w3-genus1-curvature` | `theorem` | 1449 | Genus-1 curvature for $\mathcal{W}_3$ |
| `thm:w3-genus1-inversion` | `theorem` | 1515 | Genus-1 bar-cobar inversion for $\mathcal{W}_3$ |
| `thm:w3-genus1-complementarity` | `theorem` | 1585 | Genus-1 complementarity for $\mathcal{W}_3$ |
| `thm:wn-obstruction` | `theorem` | 1685 | Obstruction coefficient for $\mathcal{W}_N$ |
| `cor:wn-complementarity` | `corollary` | 1781 | Central charge complementarity sum for $\mathcal{W}_N$ |
| `cor:general-w-obstruction` | `corollary` | 1802 | Obstruction coefficient for general $\mathcal{W}(\mathfrak{g})$ |
| `thm:w-center-langlands` | `theorem` | 1891 | $\mathcal{W}$-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 1996 | $\mathcal{W}$-algebra $A_\infty$ operations |

#### `chapters/examples/yangians.tex` (139)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 111 | Yangian as $\Eone$-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 179 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 212 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 271 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 312 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 365 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 415 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 659 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 774 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `corollary` | 862 | Seed-normalized extraction of the dg-shifted local coefficient |
| `prop:dg-shifted-rtt-degree2-scalar-normalization` | `proposition` | 920 | Degree-$2$ scalar normalization removes the identity channel |
| `cor:dg-shifted-rtt-degree2-casimir-normalization` | `corollary` | 1042 | Trace-zero Casimir convention reduces to the same scalar packet |
| `prop:dg-shifted-rtt-degree2-fundamental-casimir` | `proposition` | 1083 | Fundamental Casimir insertion fixes the normalized one-loop scalar |
| `cor:factorization-fundamental-casimir-identity` | `corollary` | 1167 | Factorization-side fundamental Casimir identity |
| `prop:dg-shifted-factorization-shared-seed` | `proposition` | 1227 | Shared bar seed transports the fundamental degree-$2$ coefficient |
| `cor:yangian-typea-dg-local-closure` | `corollary` | 1301 | Shared bar seed closes the local dg-shifted type-$A$ MC4 packet |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1498 | Presentation-level criterion for finite RTT dg quotients |
| `prop:dg-shifted-rtt-locality-criterion` | `proposition` | 1537 | Pole-order locality criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-formula-preservation` | `proposition` | 1589 | RTT-level preservation from the rational line-operator formulas |
| `prop:dg-shifted-rtt-coefficient-criterion` | `proposition` | 1661 | Coefficient-level RTT criterion for finite-stage identification |
| `prop:dg-shifted-rtt-kernel-coefficient-criterion` | `proposition` | 1714 | Kernel-coefficient criterion for finite RTT identification |
| `prop:dg-shifted-rtt-oneloop-kernel-criterion` | `proposition` | 1764 | One-loop kernel identity criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-evaluation-detection` | `proposition` | 1822 | Evaluation-detection criterion for one-loop RTT identities |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1864 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1911 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1973 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `corollary` | 2035 | Line-side boundary-strip support bound on generic tensor powers |
| `prop:dg-shifted-rtt-defect-support-mechanism` | `proposition` | 2096 | Defect-side support mechanism from RTT degree |
| `prop:dg-shifted-rtt-universal-generic-packets` | `proposition` | 2146 | Universal generic packet reduction for the boundary strip |
| `cor:dg-shifted-rtt-minimal-canonical-family` | `corollary` | 2230 | Minimal canonical family from the boundary-strip induction |
| `prop:dg-shifted-rtt-finite-tensor-detection` | `proposition` | 2270 | Finite tensor-length detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 2351 | Top-packet induction step on the universal family |
| `prop:dg-shifted-rtt-top-packet-line-formula` | `proposition` | 2400 | Closed-form line-side top-support class on the top packet |
| `cor:dg-shifted-rtt-top-packet-comparison` | `corollary` | 2482 | Abstract top-packet comparison |
| `prop:dg-shifted-rtt-top-packet-standard-discharge` | `proposition` | 2517 | Standard-evaluation discharge of the RTT top-packet class |
| `cor:dg-shifted-rtt-top-packet-conditional-closure` | `corollary` | 2571 | Conditional closure of the top-packet induction step |
| `prop:dg-shifted-rtt-universal-evaluation-rigidity` | `proposition` | 2600 | Universal-packet evaluation rigidity from the fundamental line |
| `cor:dg-shifted-rtt-top-packet-from-one-factor` | `corollary` | 2660 | Top-packet closure from the one-factor universal packet |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 2690 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 2787 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 2857 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 2926 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 2963 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 3019 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 3079 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 3140 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 3239 | Standard type-A fundamental line operator has the expected local residue |
| `prop:yangian-rank-dependence` | `proposition` | 4077 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 4214 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 4303 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 4359 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 4409 | DK-2 reduction to thick generation in category~$\mathcal{O}$ |
| `prop:dk2-thick-generation-typeA` | `proposition` | 4461 | Thick generation by evaluation modules in type~$A$ |
| `lem:composition-thick-generation` | `lemma` | 4555 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 4586 | Thick generation of category~$\mathcal{O}$ by evaluation modules, type~$A$ |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 4670 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 4772 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 4794 | Finite-dimensional factorization Drinfeld--Kohno, type~$A$ |
| `cor:dk-partial-conj` | `corollary` | 4869 | Partial resolution of Conjecture~\textup{\ref{conj:full-derived-dk}} |
| `cor:dk-poly-catO` | `corollary` | 4888 | Factorization DK for polynomial category~$\mathcal{O}$, type~$A$ |
| `lem:fd-thick-closure` | `lemma` | 4990 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 5076 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 5327 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 5436 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 5594 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 5614 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 5639 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 5841 | Evaluation-generated core identification, type~$A$ |
| `thm:derived-dk-affine` | `theorem` | 6199 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 6297 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 6450 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 6529 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 6701 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 6750 | $\infty$-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 6887 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 7027 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 7068 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 7365 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 7486 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 7688 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 7795 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 7893 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 8102 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 8181 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 8234 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 8351 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 8410 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 8493 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 8574 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 8605 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 8642 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 8709 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 8739 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 8770 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 8829 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 8908 | Type-$A$ quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 8943 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 9023 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 9076 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 9126 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 9152 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 9216 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 9292 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 9360 | Loop rotation is intrinsic on a multiplicative spectral realization of the compact core |
| `cor:yangian-dk5-spectral-one-seed` | `corollary` | 9427 | On the multiplicative spectral realization locus, one vector seed forces the full spectral DK-5 packet |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 9482 | Realization of the standard spectral vector seed-and-shift datum forces the full spectral DK-5 packet |
| `cor:yangian-dk5-spectral-factorization-vector-line` | `corollary` | 9597 | On the multiplicative spectral realization locus, vector-line realization already closes the spectral DK-5 packet |
| `prop:yangian-dk5-spectral-factorization-core-from-vector-line` | `proposition` | 9649 | On the multiplicative spectral factorization locus, the compact core is forced by the realized vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-vector-line` | `corollary` | 9737 | Ambient multiplicative vector-line realization forces the full spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-line` | `proposition` | 9791 | On the multiplicative spectral factorization locus, one ambient vector seed forces the ambient vector line |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 9912 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 9962 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 10009 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `proposition` | 10043 | On the ambient dilation orbit, ordered vector-packet monodromy is determined by the seed-pair family |
| `cor:yangian-dk5-spectral-factorization-seed-mono` | `corollary` | 10142 | After the Schur-simple ambient seed, the remaining local spectral datum is the seed-pair monodromy family |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 10172 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 10262 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 10337 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 10395 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 10439 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 10485 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 10534 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 10566 | Minimal closure criterion for the standard type-$A$ Yangian MC4 frontier |
| `cor:yangian-typea-degree2-plus-generators` | `corollary` | 10614 | Standard type-$A$ Yangian MC4 packet under one-loop exactness |
| `cor:yangian-typea-casimir-plus-generators` | `corollary` | 10666 | Fundamental Casimir insertion reduces the standard type-$A$ Yangian MC4 packet to compact generators |
| `cor:yangian-typea-factorization-local-closure` | `corollary` | 10712 | Factorization-side standard type-$A$ local MC4 packet closes |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 10936 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 10987 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 11022 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 11076 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 11109 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 11160 | Standard type-$A$ realization criterion from shared bar seed and finite RTT quotients |
| `cor:yangian-typea-realization-plus-compacts` | `corollary` | 11235 | Standard type-$A$ DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet` | `corollary` | 11264 | Standard type-$A$ DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization` | `corollary` | 11297 | Standard type-$A$ DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization` | `corollary` | 11328 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet` | `corollary` | 11379 | Standard type-$A$ DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 11465 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-plus-vector-line` | `corollary` | 11552 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |

### Part III: Connections (51)

#### `chapters/connections/bv_brst.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:qme-bar-cobar` | `theorem` | 86 | Quantum master equation = bar-cobar duality |
| `thm:genus0-amplitude-bar` | `theorem` | 175 | Genus-$0$ amplitudes from bar complex |
| `thm:log-form-ghost-law` | `theorem` | 322 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 470 | Genus-$0$ BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 676 | Physical anomaly cancellation at genus $0$ |
| `thm:bar-semi-infinite-km` | `theorem` | 772 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 911 | Anomaly duality for Kac--Moody pairs |
| `thm:bar-semi-infinite-w` | `theorem` | 1013 | Bar complex = semi-infinite complex for $\mathcal{W}$-algebras |
| `cor:virasoro-semi-infinite` | `corollary` | 1099 | Virasoro bar complex = semi-infinite complex |
| `cor:anomaly-duality-w` | `corollary` | 1123 | Anomaly complementarity for $\mathcal{W}$-algebra pairs |
| `thm:config-space-bv` | `theorem` | 1576 | Configuration space BV structure |
| `thm:bv-functor` | `theorem` | 1669 | BV functor |

#### `chapters/connections/concordance.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 245 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 259 | FG duality from $\chirAss$ self-duality |
| `thm:master-pbw` | `theorem` | 540 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 566 | Cyclic $L_\infty$ deformation algebra and universal $\Theta_\cA$ {\normalfont (MC2, originally conjectured)} |
| `prop:standard-tower-mc5-reduction` | `proposition` | 748 | Standard-tower MC5 reduction after MC3 and realized MC4 |
| `cor:standard-tower-mc5-closure` | `corollary` | 836 | Standard-tower MC5 closure on the canonical Yangian locus |
| `prop:en-n2-recovery` | `proposition` | 2707 | $n = 2$ recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 2853 | Genus-$0$ weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 2911 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 2945 | Physical anomaly cancellation, genus~$0$ |
| `thm:anomaly-physical-km-w` | `theorem` | 2961 | Physical anomaly cancellation for KM and $\mathcal{W}$-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 3179 | Hodge symmetry from complementarity |
| `thm:lagrangian-complementarity` | `theorem` | 3462 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 3497 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 3676 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 3721 | Spectral discriminant --- general case |
| `thm:family-index` | `theorem` | 3952 | Family index theorem for genus expansions |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 4515 | Volume~I concrete modular datum |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 297 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 384 | $A_\infty$ constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 508 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 547 | Anomaly-free genus-$0$ collapse of the local packet |
| `thm:mk-tree-level` | `theorem` | 926 | Tree-level $m_k$ structure |
| `thm:mk-general-structure` | `theorem` | 970 | All-genus $m_k$ Feynman expansion |

#### `chapters/connections/genus_complete.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 211 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 242 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 332 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 568 | Bar complex computes moduli integrals |

#### `chapters/connections/holomorphic_topological.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:open-string-bar` | `theorem` | 454 | Open-string bar identification |
| `thm:w-algebra-bar-complex` | `theorem` | 696 | $\mathcal{W}$-algebra bar complex |
| `thm:genus-graded-bar` | `theorem` | 791 | Genus-graded bar complex |
| `conj:w-algebra-bar-cobar` | `conjecture` | 925 | $\mathcal{W}$-algebra bar-cobar duality |
| `thm:agt-2d-bar` | `theorem` | 1137 | AGT 2D side: bar complex = semi-infinite complex |

#### `chapters/connections/kontsevich_integral.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-weight-systems` | `theorem` | 97 | Bar complex weight systems |
| `prop:propagator-restriction` | `proposition` | 166 | Propagator restriction |
| `prop:kz-from-bar` | `proposition` | 252 | KZ connection from bar complex |
| `thm:drinfeld-associator-bar` | `theorem` | 295 | Drinfeld associator from bar-cobar |

#### `chapters/connections/poincare_computations.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-c26-selfdual` | `proposition` | 152 | Virasoro NAP duality at $c=26$ |
| `thm:genus-complementarity` | `theorem` | 279 | Genus complementarity |

### Appendices (37)

#### `appendices/arnold_relations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:operadic-equivalence-arnold` | `proposition` | 115 | Operadic equivalence: Arnold relations $\Leftrightarrow$ $d^2 = 0$ |
| `thm:bar-d-squared-arnold` | `theorem` | 132 | Bar differential squares to zero |
| `cor:bar-d-squared-zero-arnold` | `corollary` | 276 | Bar differential squares to zero |
| `thm:arnold-iff-nilpotent` | `theorem` | 366 | Arnold relations $\Leftrightarrow$ $d_{\text{residue}}^2 = 0$ |
| `thm:config-boundary-relations` | `theorem` | 560 | Configuration space boundary relations |
| `cor:dres-squared-global` | `corollary` | 683 | $d_{\mathrm{res}}^2 = 0$ globally |

#### `appendices/coderived_models.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 252 | Adequacy |

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-pade` | `proposition` | 752 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dual_methodology.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-infty-operads` | `theorem` | 207 | Geometric models for $\infty$-operads |

#### `appendices/homotopy_transfer.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:sdr-existence` | `lemma` | 143 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 452 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 519 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 613 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 727 | Genus-$1$ curvature as $m_0$ |

#### `appendices/koszul_reference.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:extended-koszul-appendix` | `theorem` | 24 | Extended Koszul duality |
| `thm:genus-graded-koszul-duality-appendix` | `theorem` | 50 | Genus-graded Koszul duality theorem |
| `lem:genus-graded-koszul-resolution-appendix` | `lemma` | 87 | Genus-graded Koszul complex resolution |
| `thm:genus-graded-mc-appendix` | `theorem` | 108 | Genus-graded MC elements parametrize deformations |
| `thm:essential-image-koszul` | `theorem` | 270 | Essential image of Koszul duality |
| `lem:conilpotency-necessary` | `lemma` | 325 | Conilpotency is necessary |
| `lem:connectedness-augmentation` | `lemma` | 354 | Connectedness characterizes augmentation |
| `thm:koszul-geom-rep` | `theorem` | 383 | Koszul duals are geometrically representable |
| `cor:geom-implies-koszul` | `corollary` | 410 | Converse: geometric representability implies Koszul |
| `thm:curvature-central-appendix` | `theorem` | 459 | Curvature must be central |
| `thm:uniqueness-algebra` | `theorem` | 563 | Uniqueness up to quasi-isomorphism |

#### `appendices/nilpotent_completion.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:geom-conilpotent` | `proposition` | 105 | Geometric manifestation |
| `thm:completion-convergence` | `theorem` | 133 | Completion convergence |
| `thm:completed-bar-cobar` | `theorem` | 200 | Completed bar-cobar duality |
| `thm:koszul-dual-characterization` | `theorem` | 260 | Characterization of Koszul duals |

#### `appendices/sign_conventions.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:LV-conversion-complete` | `proposition` | 388 | Loday--Vallette conversion |

#### `appendices/signs_and_shifts.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:graded-jacobi` | `proposition` | 47 | Graded Jacobi identity |
| `prop:duality-grading` | `proposition` | 176 | Duality and grading reversal |
| `prop:susp-diff` | `proposition` | 273 | Suspension and differentials |

#### `appendices/spectral_higher_genus.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:convergence-criterion-spectral` | `theorem` | 32 | Convergence criterion |

#### `appendices/spectral_sequences.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ss` | `theorem` | 248 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 300 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 364 | Central charge and $d_1$ |
