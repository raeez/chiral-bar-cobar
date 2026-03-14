# Theorem Registry

Auto-generated on 2026-03-14 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 1101 |
| Total tagged claims | 1595 |
| Active files in `main.tex` | 61 |
| Total `.tex` files scanned | 70 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1101 |
| `ProvedElsewhere` | 318 |
| `Conjectured` | 152 |
| `Heuristic` | 24 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 420 |
| `proposition` | 374 |
| `corollary` | 194 |
| `lemma` | 72 |
| `computation` | 33 |
| `calculation` | 3 |
| `remark` | 3 |
| `conjecture` | 1 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 7 |
| Part I: Theory | 568 |
| Part II: Examples | 428 |
| Part III: Connections | 57 |
| Appendices | 41 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/bar_cobar_construction.tex` | 185 |
| `chapters/theory/higher_genus.tex` | 170 |
| `chapters/examples/yangians.tex` | 152 |
| `chapters/examples/free_fields.tex` | 51 |
| `chapters/theory/chiral_modules.tex` | 49 |
| `chapters/theory/configuration_spaces.tex` | 39 |
| `chapters/examples/genus_expansions.tex` | 34 |
| `chapters/examples/kac_moody_framework.tex` | 34 |
| `chapters/examples/lattice_foundations.tex` | 32 |
| `chapters/examples/detailed_computations.tex` | 25 |
| `chapters/theory/chiral_koszul_pairs.tex` | 25 |
| `chapters/theory/deformation_theory.tex` | 24 |
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
| `thm:frame-heisenberg-bar` | `theorem` | 914 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1016 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1176 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1198 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1371 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1567 | Quantum complementarity for Heisenberg |

### Part I: Theory (568)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 197 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 428 | Geometric realization |
| `prop:orthogonal` | `proposition` | 553 | Orthogonality |

#### `chapters/theory/bar_cobar_construction.tex` (185)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 233 | Bar construction as NAP homology |
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
| `lem:orientation` | `lemma` | 1516 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1542 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1566 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1630 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1705 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1767 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1877 | Bar complex is chiral |
| `lem:bar-holonomicity` | `lemma` | 2032 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 2093 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 2126 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 2205 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 2281 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 2395 | Verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 2643 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 2803 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 3021 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 3152 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 3198 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 3442 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 3490 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 3511 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 3557 | Topology |
| `thm:poincare-verdier` | `theorem` | 3616 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 3705 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 3729 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 3775 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 3910 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 4006 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 4147 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 4172 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 4225 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 4278 | Recognition principle |
| `thm:deformation-obstruction` | `theorem` | 4488 | Quantum deformation-obstruction complementarity |
| `lem:deformation-space` | `lemma` | 4649 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 4691 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 4739 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 4818 | Curved differential formula |
| `thm:curvature-central` | `theorem` | 4894 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `thm:completion-necessity` | `theorem` | 4941 | When completion is necessary |
| `prop:curved-bar-acyclicity` | `proposition` | 4988 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 5084 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 5153 | Conilpotency ensures convergence |
| `prop:mc4-reduction-principle` | `proposition` | 5349 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 5433 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 5470 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 5508 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 5557 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 5608 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 5641 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 5705 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 5741 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 5817 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 5914 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 5941 | Factorization-envelope criterion for principal stages |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 6064 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 6116 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 6170 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 6216 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 6266 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 6316 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 6369 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 6409 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 6450 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 6547 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 6607 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 6688 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 6750 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 6791 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 6887 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 7020 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 7063 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 7096 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 7163 | Stage-\texorpdfstring{$4$}{4} frontier as one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 7196 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 7258 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 7298 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 7363 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 7390 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 7436 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 7531 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 7614 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 7644 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 7661 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 7728 | Exact MC4 frontier packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 7801 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 frontier |
| `cor:winfty-dual-candidate-construction` | `corollary` | 7840 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 7887 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} frontier on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 7946 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 8064 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 8135 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 8249 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 8297 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 8381 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 8420 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 8546 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 8620 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 8718 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 8795 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 8837 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-higher-spin-subblocks` | `proposition` | 8888 | First higher-spin packet as four exact source-pair subblocks |
| `cor:winfty-stage5-entry-transport` | `corollary` | 8959 | Stage-\texorpdfstring{$5$}{5} entry packet and mixed transport packet |
| `cor:winfty-stage5-entry-singletons` | `corollary` | 9018 | Entry packet as two singleton channels |
| `prop:winfty-stage5-entry-mixed-self` | `proposition` | 9050 | Stage-\texorpdfstring{$5$}{5} entry packet as mixed-entry and self-return singletons |
| `prop:winfty-stage5-reduced-tail-singleton` | `proposition` | 9091 | Exact reduced tail input at stage~\texorpdfstring{$5$}{5} |
| `prop:winfty-stage5-tail-mechanism` | `proposition` | 9121 | Exact missing mechanism for the reduced stage-\texorpdfstring{$5$}{5} tail singleton |
| `prop:winfty-stage5-transport-target-ladders` | `proposition` | 9155 | Stage-\texorpdfstring{$5$}{5} mixed transport packet as three fixed-target ladders |
| `prop:winfty-stage5-higher-spin-target-blocks` | `proposition` | 9206 | Stage-\texorpdfstring{$5$}{5} higher-spin packet by target spin |
| `cor:winfty-stage5-target5-corridor` | `corollary` | 9260 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor |
| `cor:winfty-stage5-target5-residual` | `corollary` | 9303 | Residual target-\texorpdfstring{$5$}{5} continuation after the tail singleton |
| `prop:winfty-stage5-target5-transport-mechanism` | `proposition` | 9336 | Residual target-\texorpdfstring{$5$}{5} continuation as mixed transport of the new generator |
| `prop:winfty-stage5-target5-transport-singletons` | `proposition` | 9372 | Residual target-\texorpdfstring{$5$}{5} continuation as two singleton transport channels |
| `prop:winfty-stage5-transport-pole-profiles` | `proposition` | 9423 | Stage-\texorpdfstring{$5$}{5} transport ladders ordered by pole profile |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 9467 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 9500 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 9572 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 9634 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 9687 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 9707 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 9782 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 9864 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring target-\texorpdfstring{$4$}{4} and target-\texorpdfstring{$3$}{3} transport channels on the visible \texorpdfstring{$W^{(3)}$}{W3}/\texorpdfstring{$W^{(4)}$}{W4} pairing locus |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 9893 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 9923 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient on the full visible \texorpdfstring{$W^{(3)}$}{W3}/\texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 9950 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 9989 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes on a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 10028 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 10095 | Stage-\texorpdfstring{$5$}{5} mixed transport frontier carries one effective independent coefficient on the full visible pairing locus |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 10129 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient on the full visible pairing locus |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 10173 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-target5-factorization` | `proposition` | 10324 | Principal target-\texorpdfstring{$5$}{5} corridor factorization at stage~\texorpdfstring{$5$}{5} |
| `prop:winfty-stage5-principal-residual-front-factorization` | `proposition` | 10408 | Principal residual stage-\texorpdfstring{$5$}{5} front factorization |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 10470 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 10496 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 10542 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 10597 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-conjecture-network-collapse` | `corollary` | 10901 | Visible stage-\texorpdfstring{$5$}{5} local conjecture network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 10985 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 11153 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 11382 | Centrality implies strict nilpotence |
| `thm:mc-deformations` | `theorem` | 11711 | MC elements as quantum deformations |
| `thm:mc-periods` | `theorem` | 11747 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 11806 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 11818 | Strict nilpotence at all genera |
| `cor:genus-expansion-converges` | `corollary` | 12041 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 12101 | Functoriality of bar construction |
| `prop:filtered-to-curved` | `proposition` | 12460 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 12679 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 12990 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 13105 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 13178 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 13222 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 13290 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 13356 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 13491 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 13557 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 13677 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 13810 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 13826 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 13882 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 13905 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 13965 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 14010 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 14022 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 14057 | Derived equivalence |
| `prop:bar-fh` | `proposition` | 14288 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 14366 | Cobar as factorization cohomology |

#### `chapters/theory/chiral_koszul_pairs.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 125 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 152 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 172 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 200 | Fundamental theorem of chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 498 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 587 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 642 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 686 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 857 | Bar concentration for Koszul pairs |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 939 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 1099 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 1159 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 1313 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 1407 | Bar computes Koszul dual — complete statement |
| `lem:completion-convergence` | `lemma` | 1495 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 1544 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 2111 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 2329 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 2394 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 2455 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 2578 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 2620 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 2674 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 2709 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 2904 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 163 | Fusion product of Heisenberg Fock modules |
| `thm:monoidal-module-koszul` | `theorem` | 251 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 401 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 491 | Conformal blocks via the bar complex |
| `prop:kzb-bar-complex` | `proposition` | 605 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 773 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 870 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1327 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1388 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1603 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1675 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1710 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:orbit-duality` | `proposition` | 1872 | Orbit duality for affine vertex algebras |
| `prop:logarithmic-bar` | `proposition` | 1997 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2101 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2226 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2261 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2300 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2317 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2357 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2379 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2529 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2636 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2750 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 2830 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 2994 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3025 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3078 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3180 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3266 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3325 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3401 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3478 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3528 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3637 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3691 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3757` | `calculation` | 3757 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3784` | `calculation` | 3784 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3815` | `calculation` | 3815 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 3933 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4092 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4165 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4255 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4297 | \texorpdfstring{$\mathcal{W}$}{W}-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4352 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4394 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4538 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4689 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4799 | Heisenberg fusion splitting |

#### `chapters/theory/configuration_spaces.tex` (39)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 226 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 336 | Normal crossings |
| `thm:closure-relations` | `theorem` | 431 | Closure relations |
| `thm:log-complex` | `theorem` | 544 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 583 | Arnold relations |
| `lem:basic-log-form-residue` | `lemma` | 623 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 690 | Residue operations |
| `prop:residue-local` | `proposition` | 745 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 794 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1008 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1075 | Conformal blocks from punctured bar complex |
| `prop:eta` | `proposition` | 1239 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:elliptic-compactification` | `theorem` | 1489 | Elliptic compactification |
| `thm:FM-convergence` | `theorem` | 1589 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1648 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1754 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1796 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 1823 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 1845 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 1885 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 1909 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 1944 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 1966 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 2000 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2016 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2124 | Nilpotency from Arnold relations |
| `thm:arnold-geometric` | `theorem` | 2164 | Arnold relations: geometric form |
| `cor:stokes-differential` | `corollary` | 2275 | Stokes theorem and differential |
| `thm:arnold-algebraic` | `theorem` | 2288 | Arnold relations: algebraic form |
| `thm:arnold-equivalence-complete` | `theorem` | 2407 | Equivalence of Arnold formulations |
| `thm:arnold-jacobi` | `theorem` | 2624 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2677 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2723 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2755 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2800 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 3031 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 3101 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 3238 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3448` | `computation` | 3448 | Explicit examples |

#### `chapters/theory/deformation_theory.tex` (24)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 118 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 269 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 307 | Hochschild spectral sequence |
| `thm:main-koszul-hoch` | `theorem` | 477 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 590 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `comp:boson-hochschild` | `computation` | 725 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 751 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 866 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 960 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 1058 | Kac--Moody cyclic deformation complex |
| `thm:mc2-1-km` | `theorem` | 1194 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1311 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 1618 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 1704 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 1811 | Recovery of the Killing cocycle extension |
| `prop:non-scalar-criterion` | `proposition` | 2061 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 2247 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 2594 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 2695 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 2754 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 3141 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 3286 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 3333 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 3529 | Boson-fermion duality |

#### `chapters/theory/derived_langlands.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:oper-bar-h0-dl` | `theorem` | 179 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 214 | First bar cohomology as oper one-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 238 | Second bar cohomology as oper two-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 275 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 367 | Differential analysis at arity 3 |
| `prop:d4-nonvanishing` | `proposition` | 447 | Non-vanishing of \texorpdfstring{$d_4$}{d4} |
| `cor:h3-oper` | `corollary` | 506 | Third cohomology at critical level |
| `thm:oper-bar-dl` | `theorem` | 519 | Full derived identification |
| `prop:bar-as-localization` | `proposition` | 627 | The bar complex as localization |
| `prop:sl2-periodicity-dl` | `proposition` | 773 | Affine sl2 periodicity |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 849 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/en_koszul_duality.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:linking-sphere-residue` | `proposition` | 308 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 383 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 566 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 624 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 20 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 123 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 41 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 98 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 207 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 253 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 301 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 330 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 371 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 398 | — |
| `comp:fourier-km-bar` | `computation` | 461 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 482 | — |
| `thm:fourier-specialization` | `theorem` | 517 | Specialization |
| `thm:fourier-four-properties` | `theorem` | 572 | The four properties of the Fourier transform |
| `rem:fourier-genus-preview` | `remark` | 672 | ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus.tex` (170)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | 411 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 469 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 560 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 673 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 780 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 927 | Verdier duality of operations |
| `thm:geometric-com-lie-enhancement` | `theorem` | 998 | Geometric enhancement of Com-Lie |
| `thm:ainfty-com-lie-interchange` | `theorem` | 1035 | Maximal vs.\ trivial \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:convergence-filtered` | `theorem` | 1124 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1315 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1348 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1382 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1402 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1418 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 1719 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 1829 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2044 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2312 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2548 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2642 | Concrete quantum differential |
| `thm:modular-vs-quasi` | `theorem` | 2812 | Modular vs quasi-modular |
| `thm:eta-properties-genus1` | `theorem` | 2895 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:arnold-genus1` | `theorem` | 2950 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 3035 | Nilpotency at genus 1 |
| `thm:e1-page-complete` | `theorem` | 3329 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3362 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 3489 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3576 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3630 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 3708 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 3825 | \texorpdfstring{$W_3$}{W3} obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 3896 | Explicit genus-\texorpdfstring{$1$}{1} value of the \texorpdfstring{$W_3$}{W3} obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 3917 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 3946 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 4048 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4150 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4267 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4300 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4316 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4332 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4350 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 4373 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4395 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4428 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4529 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4559 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4645 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4689 | Grothendieck--Riemann--Roch bridge |
| `lem:involution-splitting` | `lemma` | 4871 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 4926 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 5000 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 5112 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 5343 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 5398 | Spectral sequence for quantum corrections |
| `lem:quantum-from-ss` | `lemma` | 5481 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 5518 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 5663 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 5729 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 5769 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 5823 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 5852 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 6040 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 6075 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 6127 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 6215 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 6246 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 6266 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 6332 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 6433 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 6564 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 6646 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 6755 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 6783 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 6820 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 6876 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 6912 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 6938 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 7224 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 7383 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 7433 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 7446 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 7488 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 7547 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 7589 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 7617 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 7639 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 7683 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 7734 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 7782 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 7870 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 7897 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 7925 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 7959 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 7984 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 8044 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 8090 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 8129 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 8158 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 8182 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 8207 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 8239 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 8258 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 8280 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 8296 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 8362 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 8534 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 8582 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 8702 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:genus-graded-koszul` | `theorem` | 8853 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 8884 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 9269 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 9302 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 9343 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 9513 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 9780 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 9805 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 10002 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 10054 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 10154 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 10204 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 10266 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:genus-internalization` | `theorem` | 10622 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 10743 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 10858 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 10901 | Universal modular Maurer--Cartan class |
| `thm:explicit-theta` | `theorem` | 10961 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 11177 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 11670 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 11749 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 11862 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 11896 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 11928 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 12133 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 12209 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 12274 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 12409 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 12506 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 12617 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 12754 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 12906 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 13080 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 13230 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 13424 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 13544 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 13643 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 13733 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 13845 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 13917 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 13999 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 14077 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 14154 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 14230 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 14305 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 14371 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 14510 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 14585 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 14632 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 14682 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 14763 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 14817 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 14850 | Scalar saturation for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 14888 | Scalar saturation persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 14941 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 15026 | Scalar saturation for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 15280 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 15447 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 15610 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 15693 | Cyclic rigidity at generic level |
| `thm:tautological-line-support` | `theorem` | 16232 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 16369 | MC2 reduced to cyclic model |

#### `chapters/theory/hochschild_cohomology.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 82 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 126 | W-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:379` | `computation` | 379 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 435 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 515 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 770 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 802 | Hochschild cup product exchange |

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 337 | Central charge complementarity |
| `prop:chirAss-self-dual` | `proposition` | 864 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | 122 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 160 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 200 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 219 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 276 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 339 | \texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology |
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
| `thm:linf-mc-flatness` | `theorem` | 1593 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan as homotopy flatness |
| `thm:cs-koszul-general` | `theorem` | 1663 | CS/Koszul for general non-quadratic algebras |
| `thm:bv-structure-bar` | `theorem` | 1902 | BV structure on bar complex |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 180 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 292 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 359 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 450 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 509 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 525 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 617 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 700 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bg-bar-coalg` | `theorem` | 440 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex coalgebra |
| `prop:chiral-operad-genus0` | `proposition` | 569 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 613 | Prism principle --- operadic identification |
| `thm:prism-higher-genus` | `theorem` | 822 | Prism principle --- higher-genus extension |
| `cor:prism-principle` | `corollary` | 929 | The prism principle |
| `thm:partition` | `theorem` | 1080 | Partition complex structure |

### Part II: Examples (428)

#### `chapters/examples/beta_gamma.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 76 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 127 | Bar cohomology of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `thm:betagamma-fermion-koszul` | `theorem` | 162 | Koszul dual of \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:bar-bc-system` | `proposition` | 215 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 253 | Cobar gives \texorpdfstring{$\beta\gamma$}{beta-gamma} |
| `prop:betagamma-bar-deg2` | `proposition` | 273 | — |
| `thm:cobar-fermions` | `theorem` | 301 | Cobar gives fermions |
| `thm:betagamma-bc-koszul-detailed` | `proposition` | 337 | Central charge complementarity for \texorpdfstring{$\beta\gamma$}{beta-gamma}/\texorpdfstring{$bc$}{bc} |
| `thm:beta-gamma-bar` | `theorem` | 425 | Bar complex of the \texorpdfstring{$\beta$}{beta}-\texorpdfstring{$\gamma$}{gamma} system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 692 | Acyclicity of the \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 812 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 913 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1054 | \texorpdfstring{$E_1$}{E1} page |
| `prop:betagamma-ss-collapse` | `proposition` | 1138 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1289 | \texorpdfstring{$\mathbb{Z}_2$}{Z_2}-equivariant bar cohomology |

#### `chapters/examples/deformation_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 511 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 616 | Deformation--duality compatibility |

#### `chapters/examples/deformation_quantization.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 109 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 162 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 394 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 507 | Genus expansion |

#### `chapters/examples/detailed_computations.tex` (25)

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
| `comp:bgg-weight-decomp` | `computation` | 2053 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2089 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2123 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2553 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2728 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2948 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 3002 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3039 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3313 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3492 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3789 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3851 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4048 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4198 | BGG involution under Koszul duality |

#### `chapters/examples/examples_summary.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 236 | Paired standard-tower MC4 frontier packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 453 | Minimal closure conditions for the standard-tower MC4 frontier |
| `cor:genus1-anomaly-ratio` | `corollary` | 583 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `prop:bar-dimensions` | `proposition` | 792 | Koszul dual Hilbert functions |
| `cor:subexp-free-field` | `corollary` | 1024 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 1034 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 1051 | DS reduction and bar cohomology generating functions |
| `prop:hred-sl2` | `proposition` | 1346 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 1546 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1637 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1734 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1800 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 1855 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1907 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1922 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 2011 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2200 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2506 | Spectral sequence collapse |

#### `chapters/examples/free_fields.tex` (51)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fermion-bar-complex-genus-0` | `theorem` | 44 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 103 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 175 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 186 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `prop:bc-betagamma-orthogonality` | `proposition` | 247 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 270 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 453 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:single-fermion-boson-duality` | `theorem` | 528 | Single-generator fermion-boson duality |
| `thm:heisenberg-bar` | `theorem` | 580 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 603 | Orientation consistency |
| `prop:curved-convergence` | `proposition` | 638 | Convergence in curved structure |
| `thm:monodromy-finite` | `theorem` | 657 | Monodromy finiteness |
| `thm:heisenberg-curved-structure` | `theorem` | 679 | Heisenberg curved structure |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 710 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 742 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 877 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 933 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 983 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1025 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1200 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1276 | Spectral flow under Koszul duality |
| `thm:lattice-voa-bar` | `theorem` | 1352 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1381 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:virasoro-moduli` | `theorem` | 1424 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 1456 | Geometric interpretation |
| `thm:elliptic-fermion-bar` | `theorem` | 1497 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1534 | Higher genus Heisenberg |
| `rem:koszul-table-status` | `remark` | 1616 | Status of Koszul duality identifications |
| `thm:filtered-bar-complex` | `theorem` | 1796 | Filtered bar complex |
| `thm:virasoro-string` | `theorem` | 1962 | Virasoro-string duality |
| `thm:w-algebra-bar-flag` | `theorem` | 2110 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar complex |
| `thm:wakimoto-bar` | `theorem` | 2174 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 2204 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 2237 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 2309 | Quantum integrability via \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:heisenberg-not-self-dual` | `theorem` | 2416 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2495 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2591 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2920 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 3070 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 3424 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 3685 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 3732 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3792 | Heisenberg level inversion: curved duality |
| `thm:algebraic-string-dictionary` | `theorem` | 3869 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 3921 | Genus-\texorpdfstring{$0$}{0} string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 3963 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 4123 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 4214 | Bar complex computes genus-\texorpdfstring{$g$}{g} string integrands |
| `thm:modular-invariance` | `theorem` | 4386 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 4423 | Modular anomaly for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |

#### `chapters/examples/genus_expansions.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 23 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 100 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `thm:lattice-all-genera` | `theorem` | 144 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 179 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 230 | \texorpdfstring{$\mathcal{W}$}{W}-algebra free energy at all genera |
| `thm:sl2-all-genera` | `theorem` | 442 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 517 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 543 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 585 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 639 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 750 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 860 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1056 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1123 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1204 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1305 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1458 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1488 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1505 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1531 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1616 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1744 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1786 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1884 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 2033 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2098 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:complementarity-classification` | `proposition` | 2346 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2400 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2601 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2725 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2741 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2766 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2798 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 2925 | Loop expansion interpretation |

#### `chapters/examples/heisenberg_eisenstein.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-genus-one-complete` | `theorem` | 106 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 193 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 235 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 353 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 456 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 505 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 717 | Multi-boson Eisenstein corrections |

#### `chapters/examples/kac_moody_framework.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-ope-kac-moody` | `theorem` | 198 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 232 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 272 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 338 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 467 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 498 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 537 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 595 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 646 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 731 | Universal Koszul duality for affine Kac--Moody |
| `prop:ff-channel-shear` | `proposition` | 843 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 893 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 959 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1033 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1072 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1126 | Closed-form OPE for Koszul dual |
| `thm:km-quantum-groups` | `theorem` | 1236 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 1577 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 1647 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 1735 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 1855 | KW formula via bar complex: general simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `prop:admissible-verlinde-bar` | `proposition` | 1939 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2178 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 2259 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 2324 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 2376 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 2442 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 2515 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 2561 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 2600 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 2637 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 2889 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 2919 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 2949 | Full derived oper identification |

#### `chapters/examples/lattice_foundations.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:lattice:cocycle-class` | `lemma` | 173 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 335 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 554 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 651 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 674 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 708 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 742 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 787 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 873 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 918 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1137 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1182 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1224 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1247 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1388 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1405 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1430 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1633 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1817 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2442 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2510 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2584 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2743 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3047 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3128 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3298 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3495 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3538 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3696 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3743 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 3829 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 3901 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |

#### `chapters/examples/minimal_model_examples.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 421 | Fusion from bar complex on the torus |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 74 | \texorpdfstring{$W_3$}{W_3} minimal models |
| `thm:grothendieck-structure` | `theorem` | 209 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 364 | \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 388 | Quantum dimensions for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:s-matrix-5-4` | `computation` | 417 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 442 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 521 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 548 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 608 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 628 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 655 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 751 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

#### `chapters/examples/toroidal_elliptic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 475 | Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0} |
| `thm:elliptic-vs-rational` | `theorem` | 573 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 945 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1141 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1219 | DYBE and bar nilpotency |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 40 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 142 | Mode expansion |
| `thm:c-scaling` | `theorem` | 193 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 292 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 457 | Quasi-primarity of \texorpdfstring{$\Lambda_2$}{Lambda_2} and \texorpdfstring{$\Lambda_3$}{Lambda_3} |
| `comp:weight6-two-point` | `computation` | 541 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 592 | Quasi-primary projection of \texorpdfstring{${:}W^2{:}$}{:W2:} |
| `comp:W2-twopt` | `computation` | 653 | Two-point function \texorpdfstring{$\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$}{:W2:_qp(z) :W2:_qp(w)} |
| `thm:w3-null-level1` | `theorem` | 713 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 816 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 887 | \texorpdfstring{$W_3$}{W_3} Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 929 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 1000 | Level-2 Gram matrix |

#### `chapters/examples/w_algebras_deep.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 92 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 795 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `prop:w3-deg3-vacuum` | `proposition` | 1304 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1511 | DS hierarchy and Koszul duality |

#### `chapters/examples/w_algebras_framework.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-algebra-koszul-main` | `theorem` | 55 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 275 | Subregular \texorpdfstring{$\mathcal{W}$}{W}-algebra duality for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} |
| `thm:w-geometric-ope` | `theorem` | 628 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 699 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-critical-bar` | `theorem` | 739 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 776 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 942 | Virasoro self-duality at \texorpdfstring{$c=0$}{c=0} |
| `thm:vir-genus1-curvature` | `theorem` | 1068 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1119 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1183 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1366 | Koszul dual of \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1447 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1513 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 1583 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 1683 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 1779 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 1800 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-center-langlands` | `theorem` | 1889 | \texorpdfstring{$\mathcal{W}$}{W}-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 1994 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |

#### `chapters/examples/yangians.tex` (152)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 144 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 229 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 262 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 321 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 362 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 415 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 465 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 709 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 824 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `corollary` | 912 | Seed-normalized extraction of the dg-shifted local coefficient |
| `prop:dg-shifted-rtt-degree2-scalar-normalization` | `proposition` | 970 | Degree-\texorpdfstring{$2$}{2} scalar normalization removes the identity channel |
| `cor:dg-shifted-rtt-degree2-casimir-normalization` | `corollary` | 1092 | Trace-zero Casimir convention reduces to the same scalar packet |
| `prop:dg-shifted-rtt-degree2-fundamental-casimir` | `proposition` | 1133 | Fundamental Casimir insertion fixes the normalized one-loop scalar |
| `cor:factorization-fundamental-casimir-identity` | `corollary` | 1217 | Factorization-side fundamental Casimir identity |
| `prop:dg-shifted-factorization-shared-seed` | `proposition` | 1277 | Shared bar seed transports the fundamental degree-\texorpdfstring{$2$}{2} coefficient |
| `cor:yangian-typea-dg-local-closure` | `corollary` | 1351 | Shared bar seed closes the local dg-shifted type-\texorpdfstring{$A$}{A} MC4 packet |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1548 | Presentation-level criterion for finite RTT dg quotients |
| `prop:dg-shifted-rtt-locality-criterion` | `proposition` | 1587 | Pole-order locality criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-formula-preservation` | `proposition` | 1639 | RTT-level preservation from the rational line-operator formulas |
| `prop:dg-shifted-rtt-coefficient-criterion` | `proposition` | 1711 | Coefficient-level RTT criterion for finite-stage identification |
| `prop:dg-shifted-rtt-kernel-coefficient-criterion` | `proposition` | 1764 | Kernel-coefficient criterion for finite RTT identification |
| `prop:dg-shifted-rtt-oneloop-kernel-criterion` | `proposition` | 1814 | One-loop kernel identity criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-evaluation-detection` | `proposition` | 1872 | Evaluation-detection criterion for one-loop RTT identities |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1914 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1961 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 2023 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `corollary` | 2085 | Line-side boundary-strip support bound on generic tensor powers |
| `prop:dg-shifted-rtt-defect-support-mechanism` | `proposition` | 2146 | Defect-side support mechanism from RTT degree |
| `prop:dg-shifted-rtt-universal-generic-packets` | `proposition` | 2196 | Universal generic packet reduction for the boundary strip |
| `cor:dg-shifted-rtt-minimal-canonical-family` | `corollary` | 2280 | Minimal canonical family from the boundary-strip induction |
| `prop:dg-shifted-rtt-finite-tensor-detection` | `proposition` | 2320 | Finite tensor-length detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 2401 | Top-packet induction step on the universal family |
| `prop:dg-shifted-rtt-top-packet-line-formula` | `proposition` | 2450 | Closed-form line-side top-support class on the top packet |
| `cor:dg-shifted-rtt-top-packet-comparison` | `corollary` | 2532 | Abstract top-packet comparison |
| `prop:dg-shifted-rtt-top-packet-standard-discharge` | `proposition` | 2567 | Standard-evaluation discharge of the RTT top-packet class |
| `cor:dg-shifted-rtt-top-packet-conditional-closure` | `corollary` | 2621 | Conditional closure of the top-packet induction step |
| `prop:dg-shifted-rtt-universal-evaluation-rigidity` | `proposition` | 2650 | Universal-packet evaluation rigidity from the fundamental line |
| `cor:dg-shifted-rtt-top-packet-from-one-factor` | `corollary` | 2710 | Top-packet closure from the one-factor universal packet |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 2740 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 2837 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 2907 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 2976 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 3013 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 3069 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 3129 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 3190 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 3289 | Standard type-A fundamental line operator has the expected local residue |
| `prop:yangian-rank-dependence` | `proposition` | 4127 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 4264 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 4353 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 4409 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 4459 | DK-2 reduction to thick generation in category~\texorpdfstring{$\mathcal{O}$}{O} |
| `prop:dk2-thick-generation-typeA` | `proposition` | 4511 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `lem:composition-thick-generation` | `lemma` | 4605 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 4636 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 4720 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 4822 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 4844 | Finite-dimensional factorization Drinfeld--Kohno, type~\texorpdfstring{$A$}{A} |
| `cor:dk-partial-conj` | `corollary` | 4919 | Partial resolution of Conjecture~\textup{\ref{conj:full-derived-dk}} |
| `cor:dk-poly-catO` | `corollary` | 4938 | Factorization DK for polynomial category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A} |
| `lem:fd-thick-closure` | `lemma` | 5041 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 5127 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 5378 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 5487 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 5645 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 5665 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 5690 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 5892 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:derived-dk-affine` | `theorem` | 6304 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 6402 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 6555 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 6634 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 6806 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 6855 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 6992 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 7180 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 7221 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 7518 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 7639 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 7841 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 7948 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 8046 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 8257 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 8336 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 8389 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 8506 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 8565 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 8648 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 8729 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 8760 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 8797 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 8864 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 8894 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 8925 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 8984 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 9063 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 9098 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 9178 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 9231 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 9281 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 9307 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 9371 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 9447 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 9515 | Loop rotation is intrinsic on a multiplicative spectral realization of the compact core |
| `cor:yangian-dk5-spectral-one-seed` | `corollary` | 9582 | On the multiplicative spectral realization locus, one vector seed forces the full spectral DK-5 packet |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 9637 | Realization of the standard spectral vector seed-and-shift datum forces the full spectral DK-5 packet |
| `cor:yangian-dk5-spectral-factorization-vector-line` | `corollary` | 9752 | On the multiplicative spectral realization locus, vector-line realization already closes the spectral DK-5 packet |
| `prop:yangian-dk5-spectral-factorization-core-from-vector-line` | `proposition` | 9804 | On the multiplicative spectral factorization locus, the compact core is forced by the realized vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-vector-line` | `corollary` | 9892 | Ambient multiplicative vector-line realization forces the full spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-line` | `proposition` | 9946 | On the multiplicative spectral factorization locus, one ambient vector seed forces the ambient vector line |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 10067 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 10117 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 10164 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `proposition` | 10198 | On the ambient dilation orbit, ordered vector-packet monodromy is determined by the seed-pair family |
| `cor:yangian-dk5-spectral-factorization-seed-mono` | `corollary` | 10297 | After the Schur-simple ambient seed, the remaining local spectral datum is the seed-pair monodromy family |
| `prop:yangian-dk5-spectral-factorization-seed-trig` | `proposition` | 10327 | On the ambient dilation orbit, standard ordered vector-packet braiding is equivalent to the seed-pair trigonometric identity |
| `cor:yangian-dk5-spectral-factorization-seed-trig` | `corollary` | 10408 | After the Schur-simple ambient seed, the live local spectral check is the trigonometric seed-pair identity |
| `prop:yangian-dk5-spectral-factorization-seed-channels` | `proposition` | 10439 | Type-\texorpdfstring{$A$}{A} seed-pair comparison reduces to the symmetric and antisymmetric channels |
| `cor:yangian-dk5-spectral-factorization-seed-single-line` | `corollary` | 10542 | Under highest-weight normalization, the seed-pair trigonometric identity reduces to one mixed tensor line |
| `prop:yangian-dk5-spectral-factorization-seed-exchange` | `proposition` | 10630 | Under highest-weight normalization, the seed-pair local packet is one scalar exchange coefficient family |
| `cor:yangian-dk5-spectral-factorization-seed-exchange-mult` | `corollary` | 10728 | The exchange coefficient descends to the multiplicative spectral ratio |
| `prop:yangian-dk5-spectral-factorization-seed-alt-mult` | `proposition` | 10807 | The multiplicative-ratio local packet is the antisymmetric-channel character |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 10882 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 10977 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 11052 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 11110 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 11154 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 11200 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 11249 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 11281 | Minimal closure criterion for the standard type-\texorpdfstring{$A$}{A} Yangian MC4 frontier |
| `cor:yangian-typea-degree2-plus-generators` | `corollary` | 11329 | Standard type-\texorpdfstring{$A$}{A} Yangian MC4 packet under one-loop exactness |
| `cor:yangian-typea-casimir-plus-generators` | `corollary` | 11381 | Fundamental Casimir insertion reduces the standard type-\texorpdfstring{$A$}{A} Yangian MC4 packet to compact generators |
| `cor:yangian-typea-factorization-local-closure` | `corollary` | 11427 | Factorization-side standard type-\texorpdfstring{$A$}{A} local MC4 packet closes |
| `cor:yangian-typea-shared-seed-plus-generators` | `corollary` | 11458 | Shared ordered bar seed reduces the standard type-\texorpdfstring{$A$}{A} Yangian MC4 packet to compact generators |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 11713 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 11764 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 11799 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 11853 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 11886 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 11937 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `cor:yangian-typea-realization-plus-compacts` | `corollary` | 12012 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet` | `corollary` | 12041 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization` | `corollary` | 12074 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization` | `corollary` | 12105 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet` | `corollary` | 12156 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 12261 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 12360 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 12421 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 12471 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 12530 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed` | `corollary` | 12571 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line` | `corollary` | 12604 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |

### Part III: Connections (57)

#### `chapters/connections/bv_brst.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:qme-bar-cobar` | `theorem` | 86 | Quantum master equation = bar-cobar duality |
| `thm:genus0-amplitude-bar` | `theorem` | 175 | Genus-\texorpdfstring{$0$}{0} amplitudes from bar complex |
| `thm:log-form-ghost-law` | `theorem` | 322 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 471 | Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 677 | Physical anomaly cancellation at genus \texorpdfstring{$0$}{0} |
| `thm:bar-semi-infinite-km` | `theorem` | 773 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 912 | Anomaly duality for Kac--Moody pairs |
| `thm:bar-semi-infinite-w` | `theorem` | 1014 | Bar complex = semi-infinite complex for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:virasoro-semi-infinite` | `corollary` | 1100 | Virasoro bar complex = semi-infinite complex |
| `cor:anomaly-duality-w` | `corollary` | 1124 | Anomaly complementarity for \texorpdfstring{$\mathcal{W}$}{W}-algebra pairs |
| `thm:config-space-bv` | `theorem` | 1570 | Configuration space BV structure |
| `thm:bv-functor` | `theorem` | 1663 | BV functor |

#### `chapters/connections/concordance.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 244 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 258 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `thm:master-pbw` | `theorem` | 539 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 565 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, originally conjectured)} |
| `prop:standard-tower-mc5-reduction` | `proposition` | 761 | Standard-tower MC5 reduction after MC3 and realized MC4 |
| `cor:standard-tower-mc5-closure` | `corollary` | 849 | Standard-tower MC5 closure on the canonical Yangian locus |
| `prop:en-n2-recovery` | `proposition` | 2876 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 3022 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 3080 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 3114 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 3130 | Physical anomaly cancellation for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 3348 | Hodge symmetry from complementarity |
| `thm:lagrangian-complementarity` | `theorem` | 3694 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 3729 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 3908 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 3953 | Spectral discriminant --- general case |
| `thm:family-index` | `theorem` | 4184 | Family index theorem for genus expansions |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 4765 | Volume~I concrete modular datum |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 297 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 206 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 310 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 349 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 376 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 412 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 430 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 451 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 498 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 557 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 932 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 976 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

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
| `thm:open-string-bar` | `theorem` | 456 | Open-string bar identification |
| `thm:w-algebra-bar-complex` | `theorem` | 698 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar complex |
| `thm:genus-graded-bar` | `theorem` | 793 | Genus-graded bar complex |
| `conj:w-algebra-bar-cobar` | `conjecture` | 927 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar-cobar duality |
| `thm:agt-2d-bar` | `theorem` | 1139 | AGT 2D side: bar complex = semi-infinite complex |

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
| `prop:virasoro-c26-selfdual` | `proposition` | 152 | Virasoro NAP duality at \texorpdfstring{$c=26$}{c=26} |
| `thm:genus-complementarity` | `theorem` | 279 | Genus complementarity |

### Appendices (41)

#### `appendices/arnold_relations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:operadic-equivalence-arnold` | `proposition` | 115 | Operadic equivalence: Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d^2 = 0$}{d\textasciicircum 2 = 0} |
| `thm:bar-d-squared-arnold` | `theorem` | 132 | Bar differential squares to zero |
| `cor:bar-d-squared-zero-arnold` | `corollary` | 276 | Bar differential squares to zero |
| `thm:arnold-iff-nilpotent` | `theorem` | 366 | Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d_{\text{residue}}^2 = 0$}{d\_residue\textasciicircum 2 = 0} |
| `thm:config-boundary-relations` | `theorem` | 560 | Configuration space boundary relations |
| `cor:dres-squared-global` | `corollary` | 683 | \texorpdfstring{$d_{\mathrm{res}}^2 = 0$}{d\_res\textasciicircum 2 = 0} globally |

#### `appendices/coderived_models.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 252 | Adequacy |
| `thm:stratified-conservative-restriction` | `theorem` | 583 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 659 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 709 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 736 | Factorization co-contra correspondence |

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-pade` | `proposition` | 752 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dual_methodology.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-infty-operads` | `theorem` | 207 | Geometric models for \texorpdfstring{$\infty$}{infinity}-operads |

#### `appendices/homotopy_transfer.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:sdr-existence` | `lemma` | 143 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 452 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 519 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 613 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 727 | Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0} |

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
| `prop:central-charge-d1` | `proposition` | 364 | Central charge and \texorpdfstring{$d_1$}{d1} |
