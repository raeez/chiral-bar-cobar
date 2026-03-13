# Theorem Registry

Auto-generated on 2026-03-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 942 |
| Total tagged claims | 1417 |
| Active files in `main.tex` | 61 |
| Total `.tex` files scanned | 70 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 942 |
| `ProvedElsewhere` | 323 |
| `Conjectured` | 124 |
| `Heuristic` | 28 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 421 |
| `proposition` | 295 |
| `corollary` | 117 |
| `lemma` | 64 |
| `computation` | 34 |
| `remark` | 7 |
| `calculation` | 3 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 7 |
| Part I: Theory | 509 |
| Part II: Examples | 342 |
| Part III: Connections | 47 |
| Appendices | 37 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus.tex` | 168 |
| `chapters/theory/bar_cobar_construction.tex` | 127 |
| `chapters/examples/yangians.tex` | 69 |
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
| `chapters/connections/concordance.tex` | 16 |
| `chapters/examples/examples_summary.tex` | 16 |
| `chapters/examples/beta_gamma.tex` | 15 |
| `chapters/examples/w3_composite_fields.tex` | 13 |
| `chapters/theory/fourier_seed.tex` | 13 |
| `chapters/connections/bv_brst.tex` | 12 |

## Complete Proved Registry

### Frame (7)

#### `chapters/frame/heisenberg_frame.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 460 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 904 | Heisenberg bar complex at genus~$0$ |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1006 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1166 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1188 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1361 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1557 | Quantum complementarity for Heisenberg |

### Part I: Theory (509)

#### `chapters/theory/algebraic_foundations.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 196 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 453 | Geometric realization |
| `prop:orthogonal` | `proposition` | 587 | Orthogonality |
| `__unlabeled_chapters/theory/algebraic_foundations.tex:645` | `computation` | 645 | Explicit verification |

#### `chapters/theory/bar_cobar_construction.tex` (127)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 227 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 468 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 558 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 616 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 682 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 710 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 805 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 847 | Arnold relations |
| `comp:deg0` | `computation` | 955 | Degree 0 |
| `comp:deg1-general` | `computation` | 973 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1086 | Bar construction is functorial |
| `lem:bar-induced-chain-map` | `lemma` | 1126 | Induced map is chain map |
| `lem:bar-induced-coalgebra` | `lemma` | 1159 | Induced map is coalgebra morphism |
| `cor:bar-natural` | `corollary` | 1224 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1230 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1262 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1285 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1352 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1403 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1420 | Differential is coderivation |
| `thm:bar-differential` | `theorem` | 1484 | Bar differential |
| `lem:orientation` | `lemma` | 1575 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1601 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1625 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1689 | Geometric bar $=$ operadic bar |
| `thm:residue-formula` | `theorem` | 1764 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1826 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1936 | Bar complex is chiral |
| `lem:bar-holonomicity` | `lemma` | 2091 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 2152 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 2185 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 2264 | $d_{\mathrm{cobar}}^2 = 0$ via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 2340 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 2454 | Verification of $d_{\text{cobar}}^2 = 0$ |
| `lem:cobar-sign-consistency` | `lemma` | 2702 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 2862 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 3080 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 3209 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 3255 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 3499 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 3547 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 3568 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 3614 | Topology |
| `thm:poincare-verdier` | `theorem` | 3673 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 3762 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 3786 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 3832 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 3967 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 4063 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 4204 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 4229 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 4282 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 4335 | Recognition principle |
| `thm:deformation-obstruction` | `theorem` | 4545 | Quantum deformation-obstruction complementarity |
| `lem:deformation-space` | `lemma` | 4706 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 4748 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 4796 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 4875 | Curved differential formula |
| `thm:curvature-central` | `theorem` | 4951 | Curvature as $\mu_1$-cycle |
| `thm:completion-necessity` | `theorem` | 4998 | When completion is necessary |
| `prop:curved-bar-acyclicity` | `proposition` | 5045 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 5141 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 5210 | Conilpotency ensures convergence |
| `prop:mc4-reduction-principle` | `proposition` | 5407 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 5491 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 5528 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 5566 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 5615 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 5665 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 5698 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 5762 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 5798 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 5874 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 5971 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 5998 | Factorization-envelope criterion for principal stages |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 6116 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 6168 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 6222 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 6268 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 6318 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 6368 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 6421 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 6461 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 6501 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 6563 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 6604 | Stage-$3$ principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 6700 | Stage-$4$ residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 6833 | Stage-$4$ top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 6876 | Stage-$4$ parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 6909 | Stage-$4$ packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 6976 | Stage-$4$ frontier as one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 7009 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 7071 | Stage-$4$ mixed block split by swap parity |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 7111 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 7160 | Stage-$4$ mixed block as one vanishing channel and a parity pair |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 7206 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 7278 | Principal stage-$4$ self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 7295 | Stage-$4$ frontier after theorematic mixed Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 7356 | Exact MC4 frontier packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `thm:central-implies-strict` | `theorem` | 7666 | Centrality implies strict nilpotence |
| `thm:mc-deformations` | `theorem` | 7995 | MC elements as quantum deformations |
| `thm:mc-periods` | `theorem` | 8031 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 8090 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 8102 | Strict nilpotence at all genera |
| `cor:genus-expansion-converges` | `corollary` | 8325 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 8385 | Functoriality of bar construction |
| `prop:filtered-to-curved` | `proposition` | 8751 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 8970 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 9281 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 9396 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 9469 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 9513 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 9581 | Key properties of $\Phi_C^{\mathrm{ch}}$ and $\Psi_C^{\mathrm{ch}}$ |
| `thm:chiral-co-contra-correspondence` | `theorem` | 9647 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 9782 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 9848 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 9968 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 10101 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 10117 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 10173 | Collapse at $E_2$ |
| `thm:genus-graded-convergence` | `theorem` | 10196 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 10256 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 10301 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 10313 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 10348 | Derived equivalence |
| `prop:bar-fh` | `proposition` | 10579 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 10657 | Cobar as factorization cohomology |

#### `chapters/theory/chiral_koszul_pairs.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 113 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 140 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 160 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 188 | Fundamental theorem of chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 486 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 575 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 630 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 674 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 845 | Bar concentration for Koszul pairs |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 927 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 1106 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 1166 | Yangian Koszulness for all simple $\mathfrak{g}$ |
| `thm:coalgebra-axioms-verified` | `theorem` | 1429 | Coalgebra structure on $\mathcal{A}_2^!$ |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 1523 | Bar computes Koszul dual — complete statement |
| `lem:completion-convergence` | `lemma` | 1611 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 1660 | Circularity-free Koszul duality |
| `thm:feynman-bar-cobar` | `theorem` | 2339 | Feynman-bar-cobar correspondence |
| `thm:e1-chiral-koszul-duality` | `theorem` | 2440 | $\Eone$-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 2658 | $\Eone$--$\Eone$ Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 2723 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 2784 | $\Eone$-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 2907 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 2949 | $A_\infty$ duality |
| `prop:ff-involution-uniqueness` | `proposition` | 3003 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 3038 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 3233 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (49)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 154 | Fusion product of Heisenberg Fock modules |
| `thm:monoidal-module-koszul` | `theorem` | 242 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 392 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 482 | Conformal blocks via the bar complex |
| `prop:kzb-bar-complex` | `proposition` | 596 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 764 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 861 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1318 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1379 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1594 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1666 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1701 | $\mathcal{W}$-algebra Zhu algebras are Koszul-invariant |
| `prop:orbit-duality` | `proposition` | 1863 | Orbit duality for affine vertex algebras |
| `prop:logarithmic-bar` | `proposition` | 1988 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2092 | $\mathrm{Ext}$ groups for $\mathcal{W}(2)$ via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2217 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2252 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2291 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2308 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2348 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2370 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2520 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2627 | BGG pipeline for $\widehat{\mathfrak{sl}}_2$ at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2741 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 2821 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 2985 | $\mathrm{Ext}$ groups at level~$2$ |
| `rem:ext-koszul-dual-level` | `remark` | 3016 | $\mathrm{Ext}$ complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3068 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3170 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3256 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3315 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3391 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3468 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3530 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3650 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3704 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3770` | `calculation` | 3770 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3797` | `calculation` | 3797 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3828` | `calculation` | 3828 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 3946 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4105 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4178 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4260 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4302 | $\mathcal{W}$-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4357 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4399 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4543 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4694 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4795 | Heisenberg fusion splitting |

#### `chapters/theory/configuration_spaces.tex` (39)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 217 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 327 | Normal crossings |
| `thm:closure-relations` | `theorem` | 422 | Closure relations |
| `thm:log-complex` | `theorem` | 535 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 574 | Arnold relations |
| `lem:basic-log-form-residue` | `lemma` | 614 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 681 | Residue operations |
| `prop:residue-local` | `proposition` | 736 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 785 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 999 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1066 | Conformal blocks from punctured bar complex |
| `prop:eta` | `proposition` | 1230 | Properties of $\eta_{ij}$ |
| `thm:elliptic-compactification` | `theorem` | 1480 | Elliptic compactification |
| `thm:FM-convergence` | `theorem` | 1582 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1641 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1747 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1789 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 1816 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 1838 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 1878 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 1902 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 1937 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 1959 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 1993 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2009 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2117 | Nilpotency from Arnold relations |
| `thm:arnold-geometric` | `theorem` | 2157 | Arnold relations: geometric form |
| `cor:stokes-differential` | `corollary` | 2268 | Stokes theorem and differential |
| `thm:arnold-algebraic` | `theorem` | 2281 | Arnold relations: algebraic form |
| `thm:arnold-equivalence-complete` | `theorem` | 2400 | Equivalence of Arnold formulations |
| `thm:arnold-jacobi` | `theorem` | 2617 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2670 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2716 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2748 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2793 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 3024 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 3095 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 3232 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3442` | `computation` | 3442 | Explicit examples |

#### `chapters/theory/deformation_theory.tex` (23)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 113 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 264 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 302 | Hochschild spectral sequence |
| `thm:main-koszul-hoch` | `theorem` | 472 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 585 | Deformation-obstruction exchange at genus $0$ |
| `comp:boson-hochschild` | `computation` | 720 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 746 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 823 | Genus-$0$ cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 917 | Killing cocycle $L_\infty$ extension |
| `cor:km-cyclic-deformation` | `corollary` | 1015 | Kac--Moody cyclic deformation complex |
| `thm:mc2-1-km` | `theorem` | 1151 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1266 | Minimal cyclic $L_\infty$ model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 1571 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 1657 | Cyclic $L_\infty$ structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 1764 | Recovery of the Killing cocycle extension |
| `rem:step2-stabilization-threshold` | `remark` | 2029 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 2376 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 2477 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 2536 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 2923 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 3068 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 3115 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 3311 | Boson-fermion duality |

#### `chapters/theory/derived_langlands.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:oper-bar-h0-dl` | `theorem` | 173 | Zeroth bar cohomology = oper functions |
| `prop:oper-bar-h1-dl` | `proposition` | 208 | First bar cohomology = oper $1$-forms |
| `prop:oper-bar-h2-dl` | `proposition` | 232 | Second bar cohomology = oper $2$-forms |
| `prop:whitehead-spectral-decomposition` | `proposition` | 269 | Whitehead spectral decomposition |
| `prop:h3-differential-analysis` | `proposition` | 361 | Differential analysis at $n = 3$ |
| `prop:d4-nonvanishing` | `proposition` | 441 | Non-vanishing of $d_4$ |
| `cor:h3-oper` | `corollary` | 500 | $H^3$ at critical level |
| `thm:oper-bar-dl` | `theorem` | 513 | Full derived identification |
| `prop:bar-as-localization` | `proposition` | 621 | The bar complex as localization |
| `prop:sl2-periodicity-dl` | `proposition` | 767 | $\widehat{\mathfrak{sl}}_2$ periodicity |
| `thm:kl-bar-cobar-adjunction` | `theorem` | 843 | Chain-level KL adjunction from bar-cobar |

#### `chapters/theory/en_koszul_duality.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:linking-sphere-residue` | `proposition` | 300 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 375 | $d^2 = 0$ from Totaro relations |
| `cor:n2-recovery` | `corollary` | 558 | Recovery of chiral bar-cobar at $n = 2$ |
| `prop:refines-af` | `proposition` | 616 | Our construction refines AF at $n = 2$ |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 12 | Filtered $\Rightarrow$ curved |
| `thm:bar-convergence-fc` | `theorem` | 115 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 36 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 93 | Genus-$1$ propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 200 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 246 | $n = 2$ |
| `comp:fourier-heisenberg-n3` | `computation` | 294 | $n = 3$ |
| `thm:fourier-heisenberg-bar` | `theorem` | 323 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 364 | Heisenberg on $E_\tau$ |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 391 | — |
| `comp:fourier-km-bar` | `computation` | 454 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 475 | — |
| `thm:fourier-specialization` | `theorem` | 510 | Specialization |
| `thm:fourier-four-properties` | `theorem` | 565 | The four properties of the Fourier transform |
| `rem:fourier-genus-preview` | `remark` | 665 | ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus.tex` (168)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | 384 | $A_\infty$ structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 442 | $A_\infty$ operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 533 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 646 | Cobar $A_\infty$ structure |
| `thm:chain-vs-homology` | `theorem` | 753 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 903 | Verdier duality of operations |
| `thm:geometric-com-lie-enhancement` | `theorem` | 974 | Geometric enhancement of Com-Lie |
| `thm:ainfty-com-lie-interchange` | `theorem` | 1011 | Maximal vs.\ trivial $A_\infty$ |
| `thm:convergence-filtered` | `theorem` | 1100 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1291 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1324 | $\beta\gamma$ deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1358 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1378 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1394 | Higher associahedron identity for $m_6$ |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 1695 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 1805 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2020 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2284 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2520 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2584 | Concrete quantum differential |
| `thm:modular-vs-quasi` | `theorem` | 2754 | Modular vs quasi-modular |
| `thm:eta-properties-genus1` | `theorem` | 2837 | Properties of $\eta_{ij}^{(1)}$ |
| `thm:arnold-genus1` | `theorem` | 2892 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 2977 | Nilpotency at genus 1 |
| `thm:e1-page-complete` | `theorem` | 3247 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3280 | $E_2$ page structure |
| `thm:obstruction-quantum` | `theorem` | 3407 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3494 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3548 | Heisenberg obstruction at genus $g$ |
| `thm:kac-moody-obs` | `theorem` | 3626 | Kac--Moody obstruction at genus $g$ |
| `thm:w3-obstruction` | `theorem` | 3743 | $W_3$ obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 3814 | Explicit values for low genus |
| `thm:obstruction-nilpotent` | `theorem` | 3835 | Nilpotence of obstruction ($g \leq 2$) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 3864 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 3966 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4068 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4185 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4218 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4234 | $\kappa$-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4250 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4268 | Obstruction complementarity for $\mathcal{W}_N$ |
| `cor:critical-level-universality` | `corollary` | 4291 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4313 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4346 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4447 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4477 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4556 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4600 | Grothendieck--Riemann--Roch bridge |
| `lem:involution-splitting` | `lemma` | 4783 | Involution splitting in characteristic~$0$ |
| `lem:perfectness-criterion` | `lemma` | 4838 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 4912 | Fiber--center identification \textup{(Theorem~$\mathrm{C}_0$)} |
| `thm:quantum-complementarity-main` | `theorem` | 5024 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 5233 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 5288 | Spectral sequence for quantum corrections |
| `lem:quantum-from-ss` | `lemma` | 5371 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 5408 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 5553 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 5619 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 5659 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 5713 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 5742 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 5930 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 5965 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 6017 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 6105 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 6136 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 6156 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 6222 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 6323 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 6454 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 6536 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 6645 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 6673 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 6710 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 6766 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 6802 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 6828 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 7114 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 7273 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 7323 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 7336 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 7378 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 7437 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 7479 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 7507 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 7529 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 7573 | Key property: $\Dg{g}^{\,2} = 0$ |
| `lem:quantum-preserves-acyclicity` | `lemma` | 7624 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 7672 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 7760 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 7787 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 7815 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 7849 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 7874 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 7934 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 7980 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 8019 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 8048 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 8072 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 8097 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 8129 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 8148 | Boundary-stratum compatibility of $\psi_g$ |
| `lem:extension-across-boundary-qi` | `lemma` | 8170 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 8186 | Higher genus inversion |
| `prop:pants-excision` | `proposition` | 8394 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 8442 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 8562 | $E_2$-collapse as formality |
| `thm:genus-graded-koszul` | `theorem` | 8713 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 8744 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 9129 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 9162 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 9203 | PBW concentration at all genera for principal finite-type $\mathcal{W}$-algebras |
| `thm:pbw-genus1-km` | `theorem` | 9373 | PBW degeneration at genus~$1$ for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 9640 | Unconditional modular Koszulity at genus~$1$ |
| `thm:pbw-allgenera-km` | `theorem` | 9665 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 9862 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 9910 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 10010 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 10056 | Unconditional modular Koszulity for principal finite-type $\mathcal{W}$-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 10113 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:genus-internalization` | `theorem` | 10468 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 10589 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 10684 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 10727 | Universal modular Maurer--Cartan class |
| `thm:explicit-theta` | `theorem` | 10787 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 11003 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 11496 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 11575 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 11688 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 11722 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 11754 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 11959 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 12035 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 12100 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 12235 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 12332 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 12443 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 12580 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 12732 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 12906 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 13056 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 13250 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 13370 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 13469 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 13559 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 13671 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 13743 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 13825 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 13903 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 13980 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 14056 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 14131 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 14197 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 14336 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 14411 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 14458 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 14508 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 14589 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 14643 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 14676 | Scalar saturation for $\mathcal{W}$-algebras |
| `prop:ds-package-functoriality` | `proposition` | 14713 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 14798 | Scalar saturation for non-principal $\mathcal{W}$-algebras |
| `prop:saturation-equivalence` | `proposition` | 15049 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 15216 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 15375 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 15458 | Cyclic rigidity at generic level |
| `thm:tautological-line-support` | `theorem` | 15961 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 16098 | MC2 reduced to cyclic model |

#### `chapters/theory/hochschild_cohomology.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 78 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 122 | $\mathcal{W}$-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:320` | `computation` | 320 | Explicit \texorpdfstring{$E_2$}{E2} page |
| `thm:hochschild-chain-complex` | `theorem` | 376 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 456 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 711 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 743 | Hochschild cup product exchange |

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 275 | Central charge complementarity |
| `prop:chirAss-self-dual` | `proposition` | 801 | $\chirAss$ self-duality |

#### `chapters/theory/koszul_pair_structure.tex` (20)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:chiral-enveloping-well-defined` | `lemma` | 114 | Well-definedness of chiral enveloping algebra |
| `thm:chiral-bar-resolution-exact` | `theorem` | 152 | Exactness of chiral bar resolution |
| `thm:chiral-hochschild-complex` | `theorem` | 192 | Chiral Hochschild complex |
| `thm:geometric-chiral-hochschild` | `theorem` | 211 | Geometric model of chiral Hochschild cohomology |
| `prop:cup-product-properties` | `proposition` | 268 | Properties of cup product |
| `thm:ainfty-chiral-hochschild` | `theorem` | 331 | $A_\infty$ structure on chiral Hochschild cohomology |
| `thm:periodicity-virasoro` | `theorem` | 390 | Periodicity for Virasoro |
| `thm:affine-periodicity-critical` | `theorem` | 531 | Chiral Hochschild cohomology at critical level |
| `prop:periodicity-same-type` | `proposition` | 653 | Hochschild periodicity for same-type pairs |
| `cor:hochschild-ring-koszul` | `corollary` | 668 | Hochschild ring isomorphism under Koszul duality |
| `prop:admissible-levels-permuted` | `proposition` | 853 | Admissible levels are permuted under Koszul duality |
| `thm:mc-quadratic` | `theorem` | 985 | Maurer--Cartan correspondence — quadratic case |
| `thm:chiral-yangian-km` | `theorem` | 1111 | Affine Kac--Moody as chiral algebra |
| `thm:yangian-bar-complex-structure` | `theorem` | 1141 | Bar complex structure |
| `thm:positselski-chiral` | `theorem` | 1343 | Positselski comodule-contramodule equivalence |
| `thm:full-derived-module-equiv` | `theorem` | 1391 | Full derived module equivalence |
| `thm:cs-koszul-km` | `theorem` | 1508 | Chern--Simons equations from Koszul duality |
| `thm:linf-mc-flatness` | `theorem` | 1585 | $L_\infty$ Maurer--Cartan as homotopy flatness |
| `thm:cs-koszul-general` | `theorem` | 1655 | CS/Koszul for general non-quadratic algebras |
| `thm:bv-structure-bar` | `theorem` | 1894 | BV structure on bar complex |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 174 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 286 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 353 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 444 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 503 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 519 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 585 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 668 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bg-bar-coalg` | `theorem` | 432 | $\beta\gamma$ bar complex coalgebra |
| `prop:chiral-operad-genus0` | `proposition` | 561 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 605 | Prism principle --- operadic identification |
| `thm:prism-higher-genus` | `theorem` | 814 | Prism principle --- higher-genus extension |
| `cor:prism-principle` | `corollary` | 921 | The prism principle |
| `thm:partition` | `theorem` | 1072 | Partition complex structure |

### Part II: Examples (342)

#### `chapters/examples/beta_gamma.tex` (15)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:betagamma-complete-bar` | `theorem` | 30 | Complete bar complex |
| `thm:betagamma-bar-cohomology` | `theorem` | 78 | Bar cohomology of $\beta\gamma$ |
| `thm:betagamma-fermion-koszul` | `theorem` | 113 | Koszul dual of $\beta\gamma$ |
| `prop:bar-bc-system` | `proposition` | 166 | Bar complex structure |
| `thm:cobar-betagamma` | `theorem` | 204 | Cobar gives $\beta\gamma$ |
| `prop:betagamma-bar-deg2` | `proposition` | 224 | — |
| `thm:cobar-fermions` | `theorem` | 252 | Cobar gives fermions |
| `thm:betagamma-bc-koszul-detailed` | `theorem` | 288 | $\beta\gamma \leftrightarrow bc$ Koszul duality |
| `thm:beta-gamma-bar` | `theorem` | 487 | Bar complex of the $\beta$-$\gamma$ system |
| `prop:betagamma-bar-acyclicity` | `proposition` | 754 | Acyclicity of the $\beta\gamma$ bar complex |
| `prop:betagamma-genus1-curvature` | `proposition` | 874 | Genus-1 curvature |
| `prop:betagamma-obstruction-coefficient` | `proposition` | 975 | Obstruction coefficient |
| `prop:betagamma-E1-page` | `proposition` | 1116 | $E_1$ page |
| `prop:betagamma-ss-collapse` | `proposition` | 1200 | Spectral sequence collapse |
| `prop:symplectic-equivariant-cohomology` | `proposition` | 1351 | $\mathbb{Z}_2$-equivariant bar cohomology |

#### `chapters/examples/deformation_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 500 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 605 | Deformation--duality compatibility |

#### `chapters/examples/deformation_quantization.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 103 | Coisson quantization at genus $0$ |
| `thm:chiral-kontsevich` | `theorem` | 156 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 388 | MC $\Leftrightarrow$ star product |
| `thm:deformation-genus-expansion` | `theorem` | 501 | Genus expansion |

#### `chapters/examples/detailed_computations.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 706 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 799 | Modular rank of $\widehat{\mathfrak{sl}}_3$ bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 878 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 939 | PBW spectral sequence for $\widehat{\mathfrak{sl}}_3$ |
| `comp:sl3-casimir-decomp` | `computation` | 1032 | Casimir decomposition of $\mathfrak{sl}_3^{\otimes n}$ |
| `comp:sl3-koszul-dual-scan` | `computation` | 1115 | Quadratic relation scan for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `prop:so5-bar-dims` | `proposition` | 1443 | Bar complex dimensions for $\widehat{\mathfrak{so}}_{5,k}$ |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1748 | PBW $E_2$ from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1794 | Degree-3 bar differential and curvature for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `comp:sl2-ce-sdr` | `computation` | 1865 | SDR and formality for $\mathfrak{sl}_2$ |
| `comp:sl2-ce-verification` | `computation` | 1916 | CE cohomology of $\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2045 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2081 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2115 | BGG resolution of $L(\Lambda_0)$ via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2545 | Bar complex dimensions for $\widehat{G}_{2,k}$ |
| `prop:arnold-virasoro-deg3` | `proposition` | 2720 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2940 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 2994 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3031 | $\mathcal{W}_3$ vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3305 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3484 | $E_8$ bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3781 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3843 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4040 | Bar--BGG for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `cor:bgg-koszul-involution` | `corollary` | 4190 | BGG involution under Koszul duality |

#### `chapters/examples/examples_summary.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `cor:genus1-anomaly-ratio` | `corollary` | 257 | Genus-$1$ free energy and anomaly ratio |
| `prop:bar-dimensions` | `proposition` | 463 | Koszul dual Hilbert functions |
| `cor:subexp-free-field` | `corollary` | 695 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 705 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 722 | DS reduction and bar cohomology generating functions |
| `prop:hred-sl2` | `proposition` | 1015 | Construction of $H^{\mathrm{red}}_1$ for $\mathfrak{sl}_2$ |
| `prop:discriminant-characteristic` | `proposition` | 1215 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1306 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1403 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1469 | Pole decomposition and singularity type |
| `rem:bar-deg2-symmetric-square` | `remark` | 1524 | Degree-$2$ bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1573 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1588 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 1677 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 1866 | {$\beta\gamma$ generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2172 | Spectral sequence collapse |

#### `chapters/examples/free_fields.tex` (51)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fermion-bar-complex-genus-0` | `theorem` | 40 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 99 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 171 | $\beta\gamma$ bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 182 | $\beta\gamma$ bar complex rank |
| `prop:bc-betagamma-orthogonality` | `proposition` | 243 | $bc$--$\beta\gamma$ orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 266 | $\beta\gamma$--$bc$ Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 449 | Module Koszul duality for $\beta\gamma$--$bc$ |
| `thm:single-fermion-boson-duality` | `theorem` | 524 | Single-generator fermion-boson duality |
| `thm:heisenberg-bar` | `theorem` | 576 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 599 | Orientation consistency |
| `prop:curved-convergence` | `proposition` | 634 | Convergence in curved structure |
| `thm:monodromy-finite` | `theorem` | 653 | Monodromy finiteness |
| `thm:heisenberg-curved-structure` | `theorem` | 675 | Heisenberg curved structure |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 706 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 738 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 873 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 929 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 979 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1021 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1196 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1272 | Spectral flow under Koszul duality |
| `thm:lattice-voa-bar` | `theorem` | 1348 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1377 | $A_2$ lattice computation |
| `thm:virasoro-moduli` | `theorem` | 1420 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 1452 | Geometric interpretation |
| `thm:elliptic-fermion-bar` | `theorem` | 1493 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1530 | Higher genus Heisenberg |
| `rem:koszul-table-status` | `remark` | 1612 | Status of Koszul duality identifications |
| `thm:filtered-bar-complex` | `theorem` | 1788 | Filtered bar complex |
| `thm:virasoro-string` | `theorem` | 1954 | Virasoro-string duality |
| `thm:w-algebra-bar-flag` | `theorem` | 2102 | $\mathcal{W}$-algebra bar complex |
| `thm:wakimoto-bar` | `theorem` | 2166 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 2196 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 2229 | $A_\infty$ structure on $\mathcal{W}$-algebras |
| `thm:w-integrability` | `theorem` | 2301 | Quantum integrability via $A_\infty$ |
| `thm:heisenberg-not-self-dual` | `theorem` | 2408 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2487 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2583 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2798 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 2948 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 3302 | $\En$ Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 3563 | Heisenberg bar complex: complete calculation |
| `rem:bar-dims-partitions` | `remark` | 3610 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3669 | Heisenberg level inversion: curved duality |
| `thm:algebraic-string-dictionary` | `theorem` | 3746 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 3798 | Genus-$0$ string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 3840 | Genus-$g$ chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 4000 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 4091 | Bar complex computes genus-$g$ string integrands |
| `thm:modular-invariance` | `theorem` | 4263 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 4300 | Modular anomaly for KM and $\mathcal{W}$-algebras |

#### `chapters/examples/genus_expansions.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 18 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 95 | $\beta\gamma$ genus expansion |
| `thm:lattice-all-genera` | `theorem` | 139 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 174 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 225 | $\mathcal{W}$-algebra free energy at all genera |
| `thm:sl2-all-genera` | `theorem` | 437 | $\widehat{\mathfrak{sl}}_2$ free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 512 | $\widehat{\mathfrak{sl}}_2$ complementarity |
| `prop:bivariate-gf` | `proposition` | 538 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 580 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 634 | Genus-2 bar differential for $\widehat{\mathfrak{sl}}_2$ |
| `thm:sl2-genus2-curvature` | `theorem` | 745 | Genus-2 curvature for $\widehat{\mathfrak{sl}}_2$ |
| `prop:sl2-genus2-relation` | `proposition` | 855 | Genus-2 relation for $\widehat{\mathfrak{sl}}_2$ |
| `thm:virasoro-genus2-bar` | `theorem` | 1051 | Genus-2 bar differential for $\mathrm{Vir}_c$ |
| `cor:virasoro-genus2-curvature` | `corollary` | 1118 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1199 | $\mathcal{W}_3$ genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1300 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1453 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1483 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1500 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1526 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1611 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1721 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1763 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1861 | $\widehat{\mathfrak{sl}}_3$ complementarity |
| `thm:fermion-all-genera` | `theorem` | 2010 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2075 | $bc$--$\beta\gamma$ complementarity |
| `prop:complementarity-classification` | `proposition` | 2316 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2370 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2571 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2695 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2711 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2736 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2768 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 2894 | Loop expansion interpretation |

#### `chapters/examples/heisenberg_eisenstein.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-genus-one-complete` | `theorem` | 98 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 185 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 227 | Genus-2 obstruction class for $\mathcal{H}_\kappa$ |
| `thm:heisenberg-all-genus` | `theorem` | 345 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 448 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 497 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 709 | Multi-boson Eisenstein corrections |

#### `chapters/examples/kac_moody_framework.tex` (34)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-ope-kac-moody` | `theorem` | 196 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 230 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 270 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 336 | Koszul dual of $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:sl3-koszul-dual` | `theorem` | 456 | Koszul dual of $\widehat{\mathfrak{sl}}_{3,k}$ |
| `rem:bar-dims-level-independent` | `remark` | 487 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 525 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 583 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 634 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 719 | Universal Koszul duality for affine Kac--Moody |
| `prop:ff-channel-shear` | `proposition` | 831 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 881 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 947 | $\mathcal{W}$-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1021 | $A_\infty$ operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1060 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1114 | Closed-form OPE for Koszul dual |
| `thm:km-quantum-groups` | `theorem` | 1224 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 1564 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 1634 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 1722 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 1842 | KW formula via bar complex: general simple $\mathfrak{g}$ |
| `prop:admissible-verlinde-bar` | `proposition` | 1926 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2165 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 2246 | Genus-1 curvature for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:sl2-genus1-inversion` | `theorem` | 2311 | Genus-1 bar-cobar inversion for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:sl2-genus1-complementarity` | `theorem` | 2363 | Genus-1 complementarity for $\widehat{\mathfrak{sl}}_{2,k}$ at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 2429 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 2502 | Genus-1 curvature for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `thm:sl3-genus1-inversion` | `theorem` | 2548 | Genus-1 bar-cobar inversion for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `thm:sl3-genus1-complementarity` | `theorem` | 2587 | Genus-1 complementarity for $\widehat{\mathfrak{sl}}_{3,k}$ |
| `prop:sl3-genus1-partition` | `proposition` | 2624 | Partition function for $\widehat{\mathfrak{sl}}_{3,k}$ at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 2876 | Oper space from bar complex at $H^0$ |
| `prop:oper-bar-h1` | `proposition` | 2906 | $H^1$ at critical level |
| `thm:oper-bar` | `theorem` | 2936 | Full derived oper identification |

#### `chapters/examples/lattice_foundations.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:lattice:cocycle-class` | `lemma` | 169 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 331 | $\Eone$ vs.\ $\Einf$ classification |
| `thm:lattice:bar-structure` | `theorem` | 550 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 647 | $D_4$ bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 670 | $E_8$ bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 704 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 738 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 783 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 869 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 914 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1133 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1178 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1220 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1243 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1384 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1401 | $D_4$ and triality |
| `prop:lattice-module-koszul` | `proposition` | 1426 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1629 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1813 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2438 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2506 | $\Eone$ bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2580 | $\Eone$ inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2739 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3043 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3124 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3294 | Factorization DK at level $1$ |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3480 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3523 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3681 | Level-$k$ lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3728 | Level-$k$ factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 3814 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 3886 | Lattice--Yangian DK bridge at level $1$ |

#### `chapters/examples/minimal_model_examples.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fusion-bar-torus` | `theorem` | 453 | Fusion from bar complex on the torus |

#### `chapters/examples/minimal_model_fusion.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w3-minimal-complete` | `theorem` | 66 | $W_3$ minimal models |
| `thm:grothendieck-structure` | `theorem` | 201 | Structure of Grothendieck ring |
| `comp:m54-primaries` | `computation` | 356 | $\mathcal{M}(5,4)$ primary fields |
| `prop:quantum-dim-5-4` | `proposition` | 380 | Quantum dimensions for $\mathcal{M}(5,4)$ |
| `comp:s-matrix-5-4` | `computation` | 409 | S-matrix for $\mathcal{M}(5,4)$ |
| `comp:fusion-5-4` | `computation` | 434 | Fusion rules for $\mathcal{M}(5,4)$ |
| `comp:m65-primaries` | `computation` | 513 | $\mathcal{M}(6,5)$ primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 540 | Fusion rules for $\Phi_{1,2}$ in $\mathcal{M}(6,5)$ |
| `thm:fusion-ring-generators` | `theorem` | 600 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 620 | Fusion ring for $\mathcal{M}(p,2)$ |
| `thm:fusion-ring-quotient` | `theorem` | 647 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 743 | Twist values for $\mathcal{M}(5,4)$ |

#### `chapters/examples/toroidal_elliptic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 432 | Fay identity implies elliptic $d^2 = 0$ |
| `thm:elliptic-vs-rational` | `theorem` | 530 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 902 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1098 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1176 | DYBE and bar nilpotency |

#### `chapters/examples/w3_composite_fields.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:lambda-coefficients-derivation` | `theorem` | 32 | Derivation of coefficients |
| `prop:lambda-modes` | `proposition` | 134 | Mode expansion |
| `thm:c-scaling` | `theorem` | 185 | Central charge scaling |
| `thm:arakawa-verification-complete` | `theorem` | 284 | Zamolodchikov verification |
| `prop:lambda23-quasiprimary` | `proposition` | 449 | Quasi-primarity of $\Lambda_2$ and $\Lambda_3$ |
| `comp:weight6-two-point` | `computation` | 533 | Two-point functions of weight-6 composites |
| `prop:W-squared-qp` | `proposition` | 584 | Quasi-primary projection of ${:}W^2{:}$ |
| `comp:W2-twopt` | `computation` | 645 | Two-point function $\langle {:}W^2{:}_{\mathrm{qp}}(z)\, {:}W^2{:}_{\mathrm{qp}}(w)\rangle$ |
| `thm:w3-null-level1` | `theorem` | 705 | Level-1 null vector |
| `prop:null-bar-relation` | `proposition` | 808 | Null vectors and bar complex relations |
| `thm:w3-kac-level1` | `theorem` | 879 | $W_3$ Kac determinant at level~1 |
| `comp:kac-vanishing-level1` | `computation` | 921 | Kac determinant vanishing locus at level~1 |
| `comp:w3-gram-level2` | `computation` | 992 | Level-2 Gram matrix |

#### `chapters/examples/w_algebras_deep.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 84 | $\mathcal{W}$-algebra bar coalgebra |
| `prop:w3-deg3-vacuum` | `proposition` | 835 | $\mathcal{W}_3$ degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1042 | DS hierarchy and Koszul duality |

#### `chapters/examples/w_algebras_framework.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-algebra-koszul-main` | `theorem` | 49 | $\mathcal{W}$-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 269 | Subregular $\mathcal{W}$-algebra duality for $\mathfrak{sl}_3$ |
| `thm:w-geometric-ope` | `theorem` | 622 | Geometric OPE formula for $\mathcal{W}$-algebras |
| `thm:w-bar-curvature` | `theorem` | 693 | Curvature of $\mathcal{W}$-algebra $A_\infty$ structure |
| `thm:w-critical-bar` | `theorem` | 733 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 770 | Koszul duality for $\mathcal{W}$-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 936 | Virasoro self-duality at $c=0$ |
| `thm:vir-genus1-curvature` | `theorem` | 1062 | Genus-1 curvature for $\mathrm{Vir}_c$ |
| `thm:vir-genus1-inversion` | `theorem` | 1113 | Genus-1 bar-cobar inversion for $\mathrm{Vir}_c$ |
| `thm:vir-genus1-complementarity` | `theorem` | 1177 | Genus-1 complementarity for $\mathrm{Vir}_c$ |
| `thm:w3-koszul-dual` | `theorem` | 1360 | Koszul dual of $\mathcal{W}_3$ |
| `thm:w3-genus1-curvature` | `theorem` | 1441 | Genus-1 curvature for $\mathcal{W}_3$ |
| `thm:w3-genus1-inversion` | `theorem` | 1507 | Genus-1 bar-cobar inversion for $\mathcal{W}_3$ |
| `thm:w3-genus1-complementarity` | `theorem` | 1577 | Genus-1 complementarity for $\mathcal{W}_3$ |
| `thm:wn-obstruction` | `theorem` | 1677 | Obstruction coefficient for $\mathcal{W}_N$ |
| `cor:wn-complementarity` | `corollary` | 1773 | Central charge complementarity sum for $\mathcal{W}_N$ |
| `cor:general-w-obstruction` | `corollary` | 1794 | Obstruction coefficient for general $\mathcal{W}(\mathfrak{g})$ |
| `thm:w-center-langlands` | `theorem` | 1883 | $\mathcal{W}$-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 1988 | $\mathcal{W}$-algebra $A_\infty$ operations |

#### `chapters/examples/yangians.tex` (69)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 103 | Yangian as $\Eone$-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 171 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 204 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 263 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 304 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 357 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 407 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 651 | Structural comparison |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 862 | Presentation-level criterion for finite RTT dg quotients |
| `prop:dg-shifted-rtt-locality-criterion` | `proposition` | 901 | Pole-order locality criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-formula-preservation` | `proposition` | 953 | RTT-level preservation from the rational line-operator formulas |
| `prop:dg-shifted-rtt-coefficient-criterion` | `proposition` | 1025 | Coefficient-level RTT criterion for finite-stage identification |
| `prop:dg-shifted-rtt-kernel-coefficient-criterion` | `proposition` | 1078 | Kernel-coefficient criterion for finite RTT identification |
| `prop:dg-shifted-rtt-oneloop-kernel-criterion` | `proposition` | 1128 | One-loop kernel identity criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-evaluation-detection` | `proposition` | 1186 | Evaluation-detection criterion for one-loop RTT identities |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1228 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1275 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1337 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `corollary` | 1399 | Line-side boundary-strip support bound on generic tensor powers |
| `prop:dg-shifted-rtt-defect-support-mechanism` | `proposition` | 1460 | Defect-side support mechanism from RTT degree |
| `prop:dg-shifted-rtt-finite-tensor-detection` | `proposition` | 1510 | Finite tensor-length detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 1585 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 1682 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 1752 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 1821 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 1858 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 1914 | Type-A residue detection on one mixed tensor line |
| `prop:yangian-rank-dependence` | `proposition` | 2687 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 2824 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 2913 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 2969 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 3019 | DK-2 reduction to thick generation in category~$\mathcal{O}$ |
| `prop:dk2-thick-generation-typeA` | `proposition` | 3071 | Thick generation by evaluation modules in type~$A$ |
| `lem:composition-thick-generation` | `lemma` | 3165 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 3196 | Thick generation of category~$\mathcal{O}$ by evaluation modules, type~$A$ |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 3280 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 3382 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 3404 | Finite-dimensional factorization Drinfeld--Kohno, type~$A$ |
| `cor:dk-partial-conj` | `corollary` | 3479 | Partial resolution of Conjecture~\textup{\ref{conj:full-derived-dk}} |
| `cor:dk-poly-catO` | `corollary` | 3498 | Factorization DK for polynomial category~$\mathcal{O}$, type~$A$ |
| `lem:fd-thick-closure` | `lemma` | 3600 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 3686 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 3926 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 4035 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 4193 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 4213 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 4238 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 4440 | Evaluation-generated core identification, type~$A$ |
| `thm:derived-dk-affine` | `theorem` | 4797 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 4895 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 5048 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 5124 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 5296 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 5345 | $\infty$-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 5482 | DK-2/3 for all simple types via sectorwise convergence |
| `thm:factorization-positselski` | `theorem` | 5801 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 5922 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 6124 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 6228 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 6326 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 6534 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 6613 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 6666 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 6736 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 6886 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 6937 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 6972 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 7026 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 7059 | H-level comparison criterion for dg-shifted Yangians |

### Part III: Connections (47)

#### `chapters/connections/bv_brst.tex` (12)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:qme-bar-cobar` | `theorem` | 78 | Quantum master equation = bar-cobar duality |
| `thm:genus0-amplitude-bar` | `theorem` | 167 | Genus-$0$ amplitudes from bar complex |
| `thm:log-form-ghost-law` | `theorem` | 314 | Ghost transformation law for log forms |
| `thm:brst-bar-genus0` | `theorem` | 462 | Genus-$0$ BRST-bar quasi-isomorphism |
| `cor:anomaly-physical-genus0` | `corollary` | 668 | Physical anomaly cancellation at genus $0$ |
| `thm:bar-semi-infinite-km` | `theorem` | 764 | Bar complex = semi-infinite complex for KM |
| `cor:anomaly-duality-km` | `corollary` | 903 | Anomaly duality for Kac--Moody pairs |
| `thm:bar-semi-infinite-w` | `theorem` | 1005 | Bar complex = semi-infinite complex for $\mathcal{W}$-algebras |
| `cor:virasoro-semi-infinite` | `corollary` | 1091 | Virasoro bar complex = semi-infinite complex |
| `cor:anomaly-duality-w` | `corollary` | 1115 | Anomaly complementarity for $\mathcal{W}$-algebra pairs |
| `thm:config-space-bv` | `theorem` | 1568 | Configuration space BV structure |
| `thm:bv-functor` | `theorem` | 1661 | BV functor |

#### `chapters/connections/concordance.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 237 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 251 | FG duality from $\chirAss$ self-duality |
| `thm:master-pbw` | `theorem` | 531 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 557 | Cyclic $L_\infty$ deformation algebra and universal $\Theta_\cA$ {\normalfont (MC2, originally conjectured)} |
| `prop:en-n2-recovery` | `proposition` | 1814 | $n = 2$ recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1960 | Genus-$0$ weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 2018 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 2052 | Physical anomaly cancellation, genus~$0$ |
| `thm:anomaly-physical-km-w` | `theorem` | 2068 | Physical anomaly cancellation for KM and $\mathcal{W}$-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2286 | Hodge symmetry from complementarity |
| `thm:lagrangian-complementarity` | `theorem` | 2565 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 2600 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 2779 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 2824 | Spectral discriminant --- general case |
| `thm:family-index` | `theorem` | 3055 | Family index theorem for genus expansions |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 3618 | Volume~I concrete modular datum |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 289 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 376 | $A_\infty$ constraint formula |
| `thm:mk-tree-level` | `theorem` | 815 | Tree-level $m_k$ structure |
| `thm:mk-general-structure` | `theorem` | 859 | All-genus $m_k$ Feynman expansion |

#### `chapters/connections/genus_complete.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 203 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 234 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 324 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 560 | Bar complex computes moduli integrals |

#### `chapters/connections/holomorphic_topological.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:open-string-bar` | `theorem` | 437 | Open-string bar identification |
| `thm:w-algebra-bar-complex` | `theorem` | 679 | $\mathcal{W}$-algebra bar complex |
| `thm:genus-graded-bar` | `theorem` | 774 | Genus-graded bar complex |
| `thm:w-algebra-bar-cobar` | `theorem` | 908 | $\mathcal{W}$-algebra bar-cobar duality |
| `thm:agt-2d-bar` | `theorem` | 1120 | AGT 2D side: bar complex = semi-infinite complex |

#### `chapters/connections/kontsevich_integral.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-weight-systems` | `theorem` | 89 | Bar complex weight systems |
| `prop:propagator-restriction` | `proposition` | 158 | Propagator restriction |
| `prop:kz-from-bar` | `proposition` | 244 | KZ connection from bar complex |
| `thm:drinfeld-associator-bar` | `theorem` | 287 | Drinfeld associator from bar-cobar |

#### `chapters/connections/poincare_computations.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-c26-selfdual` | `proposition` | 144 | Virasoro NAP duality at $c=26$ |
| `thm:genus-complementarity` | `theorem` | 271 | Genus complementarity |

### Appendices (37)

#### `appendices/arnold_relations.tex` (6)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:operadic-equivalence-arnold` | `proposition` | 107 | Operadic equivalence: Arnold relations $\Leftrightarrow$ $d^2 = 0$ |
| `thm:bar-d-squared-arnold` | `theorem` | 124 | Bar differential squares to zero |
| `cor:bar-d-squared-zero-arnold` | `corollary` | 268 | Bar differential squares to zero |
| `thm:arnold-iff-nilpotent` | `theorem` | 358 | Arnold relations $\Leftrightarrow$ $d_{\text{residue}}^2 = 0$ |
| `thm:config-boundary-relations` | `theorem` | 552 | Configuration space boundary relations |
| `cor:dres-squared-global` | `corollary` | 675 | $d_{\mathrm{res}}^2 = 0$ globally |

#### `appendices/coderived_models.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 244 | Adequacy |

#### `appendices/combinatorial_frontier.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:virasoro-pade` | `proposition` | 744 | Pad\'e matching for the Virasoro bar sequence |

#### `appendices/dual_methodology.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:geometric-infty-operads` | `theorem` | 199 | Geometric models for $\infty$-operads |

#### `appendices/homotopy_transfer.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:sdr-existence` | `lemma` | 135 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 444 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 511 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 605 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 719 | Genus-$1$ curvature as $m_0$ |

#### `appendices/koszul_reference.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:extended-koszul-appendix` | `theorem` | 16 | Extended Koszul duality |
| `thm:genus-graded-koszul-duality-appendix` | `theorem` | 42 | Genus-graded Koszul duality theorem |
| `lem:genus-graded-koszul-resolution-appendix` | `lemma` | 79 | Genus-graded Koszul complex resolution |
| `thm:genus-graded-mc-appendix` | `theorem` | 100 | Genus-graded MC elements parametrize deformations |
| `thm:essential-image-koszul` | `theorem` | 262 | Essential image of Koszul duality |
| `lem:conilpotency-necessary` | `lemma` | 317 | Conilpotency is necessary |
| `lem:connectedness-augmentation` | `lemma` | 346 | Connectedness characterizes augmentation |
| `thm:koszul-geom-rep` | `theorem` | 375 | Koszul duals are geometrically representable |
| `cor:geom-implies-koszul` | `corollary` | 402 | Converse: geometric representability implies Koszul |
| `thm:curvature-central-appendix` | `theorem` | 451 | Curvature must be central |
| `thm:uniqueness-algebra` | `theorem` | 555 | Uniqueness up to quasi-isomorphism |

#### `appendices/nilpotent_completion.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:geom-conilpotent` | `proposition` | 97 | Geometric manifestation |
| `thm:completion-convergence` | `theorem` | 125 | Completion convergence |
| `thm:completed-bar-cobar` | `theorem` | 192 | Completed bar-cobar duality |
| `thm:koszul-dual-characterization` | `theorem` | 252 | Characterization of Koszul duals |

#### `appendices/sign_conventions.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:LV-conversion-complete` | `proposition` | 380 | Loday--Vallette conversion |

#### `appendices/signs_and_shifts.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:graded-jacobi` | `proposition` | 39 | Graded Jacobi identity |
| `prop:duality-grading` | `proposition` | 168 | Duality and grading reversal |
| `prop:susp-diff` | `proposition` | 265 | Suspension and differentials |

#### `appendices/spectral_higher_genus.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:convergence-criterion-spectral` | `theorem` | 24 | Convergence criterion |

#### `appendices/spectral_sequences.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ss` | `theorem` | 240 | Bar spectral sequence |
| `prop:degen-koszul` | `proposition` | 292 | Degeneration for Koszul algebras |
| `prop:central-charge-d1` | `proposition` | 356 | Central charge and $d_1$ |
