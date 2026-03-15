# Theorem Registry

Auto-generated on 2026-03-15 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 1286 |
| Total tagged claims | 1786 |
| Active files in `main.tex` | 64 |
| Total `.tex` files scanned | 75 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1286 |
| `ProvedElsewhere` | 319 |
| `Conjectured` | 158 |
| `Heuristic` | 23 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 486 |
| `proposition` | 427 |
| `corollary` | 242 |
| `lemma` | 90 |
| `computation` | 35 |
| `calculation` | 3 |
| `remark` | 2 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 8 |
| Part I: Theory | 721 |
| Part II: Examples | 408 |
| Part III: Connections | 52 |
| Appendices | 97 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/higher_genus.tex` | 168 |
| `chapters/theory/bar_cobar_construction.tex` | 166 |
| `chapters/examples/yangians.tex` | 136 |
| `chapters/theory/bar_cobar_adjunction.tex` | 112 |
| `chapters/theory/chiral_modules.tex` | 52 |
| `chapters/examples/free_fields.tex` | 47 |
| `chapters/theory/configuration_spaces.tex` | 35 |
| `chapters/examples/genus_expansions.tex` | 34 |
| `chapters/examples/kac_moody_framework.tex` | 34 |
| `appendices/nonlinear_modular_shadows.tex` | 33 |
| `chapters/examples/lattice_foundations.tex` | 32 |
| `chapters/theory/cobar_construction.tex` | 29 |
| `chapters/theory/deformation_theory.tex` | 29 |
| `chapters/theory/chiral_koszul_pairs.tex` | 26 |
| `chapters/examples/detailed_computations.tex` | 25 |
| `chapters/theory/bar_construction.tex` | 25 |
| `appendices/branch_line_reductions.tex` | 21 |
| `chapters/theory/koszul_pair_structure.tex` | 20 |
| `chapters/examples/w_algebras_framework.tex` | 19 |
| `chapters/connections/concordance.tex` | 18 |

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

### Part I: Theory (721)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 455 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 743 | Geometric realization |
| `prop:orthogonal` | `proposition` | 868 | Orthogonality |

#### `chapters/theory/bar_cobar_adjunction.tex` (112)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:curvature-central` | `theorem` | 53 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 147 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 224 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 293 | Conilpotency ensures convergence |
| `prop:mc4-reduction-principle` | `proposition` | 424 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 489 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 526 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 564 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 613 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 664 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 697 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 761 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 797 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 873 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 970 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 986 | Factorization-envelope criterion for principal stages |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 1059 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 1105 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 1140 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 1160 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 1178 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 1197 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 1239 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 1279 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 1320 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 1387 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 1430 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 1476 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 1538 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 1579 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 1651 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 1738 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 1764 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 1789 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 1843 | Stage-\texorpdfstring{$4$}{4} frontier as one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 1871 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 1908 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 1939 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 1981 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 2008 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 2038 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 2081 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 2116 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 2146 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 2163 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 2214 | Exact MC4 frontier packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 2275 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 frontier |
| `cor:winfty-dual-candidate-construction` | `corollary` | 2314 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 2361 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} frontier on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 2400 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 2485 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 2516 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 2599 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 2647 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 2693 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 2720 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 2839 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 2878 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 2925 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 2980 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 3022 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 3116 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 3141 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 3180 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 3200 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 3238 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 3255 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 3278 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 3300 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 3316 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 3326 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 3342 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 3354 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 3367 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 3385 | Stage-\texorpdfstring{$5$}{5} mixed transport frontier carries one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 3400 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 3419 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 3626 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 3643 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 3680 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 3720 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-conjecture-network-collapse` | `corollary` | 4016 | Visible stage-\texorpdfstring{$5$}{5} local conjecture network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 4058 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 4216 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 4454 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 4795 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 4831 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 4892 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 4904 | Strict nilpotence at all genera |
| `cor:genus-expansion-converges` | `corollary` | 5123 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 5183 | Functoriality of bar construction |
| `prop:filtered-to-curved` | `proposition` | 5553 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 5772 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 6081 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 6196 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 6269 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 6313 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 6381 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 6447 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 6582 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 6648 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 6768 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 6901 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 6917 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 6973 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 6996 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 7056 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 7101 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 7113 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 7148 | Derived equivalence |
| `prop:bar-fh` | `proposition` | 7379 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 7457 | Cobar as factorization cohomology |

#### `chapters/theory/bar_cobar_construction.tex` (166)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-NAP-homology` | `theorem` | 248 | Bar construction as NAP homology |
| `lem:sign-compatibility` | `lemma` | 559 | Sign compatibility |
| `thm:bar-nilpotency-complete` | `theorem` | 649 | Nilpotency of bar differential |
| `prop:pole-decomposition` | `proposition` | 708 | Pole decomposition of the bar differential |
| `cor:bar-functorial` | `corollary` | 774 | Bar complex is functorial |
| `thm:stokes-config` | `theorem` | 802 | Stokes' theorem on configuration spaces |
| `cor:residues-anticommute` | `corollary` | 897 | Residues anticommute at corners |
| `thm:arnold-three` | `theorem` | 939 | Arnold relations |
| `comp:deg0` | `computation` | 982 | Degree 0 |
| `comp:deg1-general` | `computation` | 1000 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1113 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1152 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1158 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1190 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1213 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1280 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1331 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1348 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1435 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1461 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1485 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1549 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1624 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1686 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1796 | Bar complex is chiral |
| `lem:bar-holonomicity` | `lemma` | 1951 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 2012 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 2045 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 2127 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 2203 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 2317 | Verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 2566 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 2726 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 2944 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 3075 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 3121 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 3394 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 3442 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 3463 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 3509 | Topology |
| `thm:poincare-verdier` | `theorem` | 3568 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 3657 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 3681 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 3727 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 3862 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 3958 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 4099 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 4124 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 4177 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 4230 | Recognition principle |
| `lem:deformation-space` | `lemma` | 4602 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 4644 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 4692 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 4771 | Curved differential formula |
| `thm:curvature-central` | `theorem` | 4859 | Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle |
| `prop:curved-bar-acyclicity` | `proposition` | 4953 | Acyclicity of curved bar complexes |
| `thm:filtered-to-curved` | `theorem` | 5030 | When filtered reduces to curved |
| `thm:conilpotency-convergence` | `theorem` | 5099 | Conilpotency ensures convergence |
| `prop:mc4-reduction-principle` | `proposition` | 5230 | Reduction of MC4 to finite-stage compatibility |
| `cor:mc4-degreewise-stabilization` | `corollary` | 5295 | Degreewise stabilization criterion for MC4 |
| `cor:mc4-surjective-criterion` | `corollary` | 5332 | Finite-dimensional surjectivity criterion for MC4 |
| `prop:mc4-weight-cutoff` | `proposition` | 5370 | Weight-cutoff criterion for MC4 |
| `prop:winfty-mc4-criterion` | `proposition` | 5419 | \texorpdfstring{$W_\infty$}{W_infty} criterion from principal finite-type stages |
| `cor:winfty-weight-cutoff` | `corollary` | 5470 | Standard principal-stage cutoff for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:inverse-limit-differential-continuity` | `proposition` | 5503 | Continuity of inverse-limit bar and cobar differentials |
| `cor:winfty-standard-mc4-package` | `corollary` | 5567 | Standard principal-stage \texorpdfstring{$W_\infty$}{W_infty} tower satisfies the M-level MC4 package |
| `prop:completed-target-comparison` | `proposition` | 5603 | Comparison with a completed target by compatible finite quotients |
| `cor:winfty-hlevel-comparison-criterion` | `corollary` | 5679 | H-level comparison criterion for \texorpdfstring{$W_\infty$}{W_infty} |
| `prop:winfty-quotient-system-criterion` | `proposition` | 5776 | Formal descent criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization target |
| `prop:winfty-factorization-envelope-criterion` | `proposition` | 5792 | Factorization-envelope criterion for principal stages |
| `prop:winfty-higher-spin-ideal-criterion` | `proposition` | 5865 | Higher-spin ideal criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-spin-triangular-ideals` | `proposition` | 5911 | Spin-triangular OPE criterion for the \texorpdfstring{$W_\infty$}{W_infty} factorization ideals |
| `prop:winfty-ds-coefficient-criterion` | `proposition` | 5946 | Coefficient-level DS criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-local-coefficient-criterion` | `proposition` | 5966 | Local-coefficient criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-residue-identity-criterion` | `proposition` | 5984 | Residue-coefficient identity criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} quotients |
| `prop:winfty-ds-generator-seed` | `proposition` | 6003 | Generator-seed criterion for principal-stage \texorpdfstring{$W_\infty$}{W_infty} residue identities |
| `cor:winfty-ds-finite-seed-set` | `corollary` | 6045 | Finite primary seed set for principal-stage \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `cor:winfty-ds-lowstage-seeds` | `corollary` | 6085 | First principal-stage seed packets for \texorpdfstring{$W_\infty$}{W_infty} comparison |
| `prop:winfty-ds-stage-growth-packet` | `proposition` | 6126 | Incremental interacting packet from stage \texorpdfstring{$N$}{N} to stage \texorpdfstring{$N{+}1$}{N+1} |
| `cor:winfty-ds-stage-growth-top-parity` | `corollary` | 6193 | Top-pole/parity reduction of the incremental \texorpdfstring{$W_\infty$}{W_infty} stage-growth packet |
| `cor:winfty-ds-stage5-reduced-packet` | `corollary` | 6236 | First reduced incremental packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-ds-primary-top-pole` | `proposition` | 6282 | Primary top-pole criterion for generator seed packets |
| `prop:winfty-ds-self-ope-parity` | `proposition` | 6344 | Odd top-pole vanishing for identical even generators |
| `prop:winfty-ds-stage3-explicit-packet` | `proposition` | 6385 | Stage-\texorpdfstring{$3$}{3} principal packet from the explicit \texorpdfstring{$W_3$}{W3} OPE |
| `prop:winfty-ds-stage4-residual-packet` | `proposition` | 6457 | Stage-\texorpdfstring{$4$}{4} residual packet after the theorematic \texorpdfstring{$W_3$}{W3} sector |
| `cor:winfty-ds-stage4-top-pole-packet` | `corollary` | 6544 | Stage-\texorpdfstring{$4$}{4} top-pole packet after primaryity |
| `cor:winfty-ds-stage4-parity-packet` | `corollary` | 6570 | Stage-\texorpdfstring{$4$}{4} parity-compressed packet |
| `cor:winfty-ds-stage4-ope-blocks` | `corollary` | 6595 | Stage-\texorpdfstring{$4$}{4} packet as three local OPE blocks |
| `cor:winfty-ds-stage4-mixed-self-split` | `corollary` | 6649 | Stage-\texorpdfstring{$4$}{4} frontier as one mixed block and three self-coupling scalars |
| `prop:winfty-ds-mixed-top-pole-swap` | `proposition` | 6677 | Mixed top-pole swap parity for even generators |
| `cor:winfty-ds-stage4-mixed-swap-parity` | `corollary` | 6714 | Stage-\texorpdfstring{$4$}{4} mixed block split by swap parity |
| `prop:winfty-formal-mixed-virasoro-zero` | `proposition` | 6745 | Formal mixed Virasoro-target vanishing under a normalized two-point package |
| `prop:winfty-ds-mixed-virasoro-ds-zero` | `proposition` | 6787 | Principal Drinfeld--Sokolov vanishing of the mixed Virasoro target |
| `cor:winfty-ds-stage4-mixed-two-channel` | `corollary` | 6814 | Stage-\texorpdfstring{$4$}{4} mixed block as one vanishing channel and a parity pair |
| `prop:winfty-formal-self-t-coefficient` | `proposition` | 6844 | Formal self-coupling stress-tensor coefficient under a normalized two-point package |
| `prop:winfty-formal-self-normalization-from-t` | `proposition` | 6887 | Formal converse: the universal self-coupling \texorpdfstring{$T$}{T}-coefficient forces the normalized two-point function |
| `prop:winfty-ds-self-t-coefficient` | `proposition` | 6922 | Principal Drinfeld--Sokolov self-coupling stress-tensor coefficient |
| `cor:winfty-ds-stage4-self-t-normalization` | `corollary` | 6952 | Principal stage-\texorpdfstring{$4$}{4} self-coupling \texorpdfstring{$W^{(4)}$-$W^{(4)}\to T$}{W4-W4 to T} normalization |
| `cor:winfty-ds-stage4-five-plus-zero` | `corollary` | 6969 | Stage-\texorpdfstring{$4$}{4} principal target packet after theorematic Virasoro-target elimination |
| `prop:winfty-mc4-frontier-package` | `proposition` | 7020 | Exact MC4 frontier packet for the standard \texorpdfstring{$W_\infty$}{W_infty} tower |
| `cor:winfty-stage4-closure-criterion` | `corollary` | 7081 | Minimal closure criterion for the standard \texorpdfstring{$W_\infty$}{W_infty} MC4 frontier |
| `cor:winfty-dual-candidate-construction` | `corollary` | 7120 | Constructing the completed chiral Koszul-dual candidate for \texorpdfstring{$W_\infty$}{W_infty} |
| `cor:winfty-stage4-residue-four-channel` | `corollary` | 7167 | Stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} frontier on the Ward-normalized H-level locus |
| `prop:winfty-stage4-visible-pairing-gap` | `proposition` | 7206 | Exact missing input for the unconditional \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} contraction |
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 7291 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 7322 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 7405 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 7453 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 7499 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 7526 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 7645 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 7684 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 7731 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 7786 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 7828 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 7922 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 7947 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 7986 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 8006 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 8044 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 8061 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 8084 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 8106 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 8122 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 8132 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 8148 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 8160 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 8173 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 8191 | Stage-\texorpdfstring{$5$}{5} mixed transport frontier carries one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 8206 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 8225 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 8432 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 8449 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 8486 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 8526 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-conjecture-network-collapse` | `corollary` | 8822 | Visible stage-\texorpdfstring{$5$}{5} local conjecture network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 8864 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 9022 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 9260 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 9601 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 9637 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 9698 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 9710 | Strict nilpotence at all genera |
| `cor:genus-expansion-converges` | `corollary` | 9929 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 9989 | Functoriality of bar construction |
| `prop:filtered-to-curved` | `proposition` | 10359 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 10578 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 10887 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 11002 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 11075 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 11119 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 11187 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 11253 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 11388 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 11454 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 11574 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 11707 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 11723 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 11779 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 11802 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 11862 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 11907 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 11919 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 11954 | Derived equivalence |
| `prop:bar-fh` | `proposition` | 12185 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 12263 | Cobar as factorization cohomology |

#### `chapters/theory/bar_construction.tex` (25)

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
| `comp:deg0` | `computation` | 983 | Degree 0 |
| `comp:deg1-general` | `computation` | 1001 | Degree 1 |
| `thm:bar-functorial-complete` | `theorem` | 1114 | Bar construction is functorial |
| `cor:bar-natural` | `corollary` | 1153 | Natural transformation property |
| `prop:model-independence` | `proposition` | 1159 | Model independence |
| `thm:bar-coalgebra` | `theorem` | 1191 | Bar coalgebra |
| `thm:coassociativity-complete` | `theorem` | 1214 | Coassociativity |
| `thm:counit-axioms` | `theorem` | 1281 | Counit axioms |
| `cor:bar-is-dgcoalg` | `corollary` | 1332 | Bar complex is DG-coalgebra |
| `thm:diff-is-coderivation` | `theorem` | 1349 | Differential is coderivation |
| `lem:orientation` | `lemma` | 1436 | Orientation convention |
| `lem:residue-properties` | `lemma` | 1462 | Residue properties |
| `lem:residue-well-defined` | `lemma` | 1486 | Well-definedness of residue |
| `thm:geometric-equals-operadic-bar` | `theorem` | 1550 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 1625 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 1687 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 1797 | Bar complex is chiral |

#### `chapters/theory/chiral_koszul_pairs.tex` (26)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:twisted-product-cone-counit` | `lemma` | 141 | Left twisted tensor product as mapping cone |
| `lem:twisted-product-cone-unit` | `lemma` | 168 | Right twisted tensor product as mapping cone |
| `lem:filtered-comparison` | `lemma` | 188 | Filtered comparison |
| `thm:fundamental-twisting-morphisms` | `theorem` | 216 | Fundamental theorem of chiral twisting morphisms |
| `cor:three-bijections` | `corollary` | 291 | Three bijections for chiral twisting morphisms |
| `thm:pbw-koszulness-criterion` | `theorem` | 546 | PBW criterion for chiral Koszulness |
| `thm:km-chiral-koszul` | `theorem` | 624 | Affine Kac--Moody algebras are chiral Koszul |
| `thm:virasoro-chiral-koszul` | `theorem` | 679 | Virasoro chiral Koszulness |
| `cor:bar-cohomology-koszul-dual` | `corollary` | 723 | Bar cohomology computes Koszul dual |
| `thm:bar-concentration` | `theorem` | 870 | Bar concentration for Koszul pairs |
| `thm:bar-cobar-isomorphism-main` | `theorem` | 943 | Geometric bar--cobar duality |
| `thm:yangian-self-dual` | `theorem` | 1108 | Yangian quadratic dual |
| `prop:yangian-koszul-general` | `proposition` | 1168 | Yangian Koszulness for all simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `thm:coalgebra-axioms-verified` | `theorem` | 1322 | Coalgebra structure on \texorpdfstring{$\mathcal{A}_2^!$}{A2-dual} |
| `thm:bar-computes-koszul-dual-complete` | `theorem` | 1416 | Bar computes Koszul dual — complete statement |
| `lem:completion-convergence` | `lemma` | 1504 | Completion convergence |
| `cor:circularity-free-koszul` | `corollary` | 1553 | Circularity-free Koszul duality |
| `thm:e1-chiral-koszul-duality` | `theorem` | 2110 | \texorpdfstring{$\Eone$}{E1}-chiral Koszul duality |
| `cor:e1-self-duality` | `corollary` | 2328 | \texorpdfstring{$\Eone$}{E1}--\texorpdfstring{$\Eone$}{E1} Self-Duality |
| `thm:module-category-equivalence` | `theorem` | 2393 | Module category equivalence |
| `thm:e1-module-koszul-duality` | `theorem` | 2454 | \texorpdfstring{$\Eone$}{E1}-module category Koszul duality |
| `thm:structure-exchange` | `theorem` | 2577 | Structure exchange |
| `thm:ainfty-duality-exchange` | `theorem` | 2619 | \texorpdfstring{$A_\infty$}{A-infinity} duality |
| `prop:ff-involution-uniqueness` | `proposition` | 2673 | Uniqueness of the Feigin--Frenkel involution |
| `thm:curved-koszul-pairs` | `theorem` | 2708 | Curved Koszul pairs |
| `prop:koszul-dual-tensor-product` | `proposition` | 2903 | Koszul dual of tensor products in the quadratic case |

#### `chapters/theory/chiral_modules.tex` (52)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fock-fusion-product` | `proposition` | 144 | Fusion product of Heisenberg Fock modules |
| `prop:module-koszul-equivalence` | `proposition` | 249 | Module Koszul equivalence |
| `thm:monoidal-module-koszul` | `theorem` | 279 | Monoidal module Koszul duality |
| `prop:ext-tor-exchange` | `proposition` | 419 | Ext--Tor exchange via module Koszul duality |
| `prop:conformal-blocks-bar` | `proposition` | 495 | Conformal blocks via the bar complex |
| `thm:module-bar-verdier` | `theorem` | 599 | Module-level Verdier intertwining |
| `cor:conformal-block-dim-invariance` | `corollary` | 692 | Dimension invariance under Koszul duality |
| `prop:kzb-bar-complex` | `proposition` | 750 | KZB connection from the bar complex |
| `prop:conformal-block-duality` | `proposition` | 905 | Conformal block duality |
| `prop:koszul-t-structures` | `proposition` | 1199 | Koszul duality and t-structures |
| `prop:tilting-bar` | `proposition` | 1588 | Tilting modules and the bar complex |
| `prop:verma-bar-complex` | `proposition` | 1649 | Verma module bar complex |
| `prop:zhu-koszul-compatibility` | `proposition` | 1849 | Zhu algebra under level-shifting Koszul duality |
| `cor:virasoro-zhu-koszul` | `corollary` | 1907 | Virasoro Zhu algebra is Koszul-invariant |
| `thm:w-algebra-zhu-koszul` | `theorem` | 1942 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Zhu algebras are Koszul-invariant |
| `prop:orbit-duality` | `proposition` | 2068 | Orbit duality for affine vertex algebras |
| `prop:logarithmic-bar` | `proposition` | 2193 | Logarithmic modules and bar complex extensions |
| `prop:w2-ext-bar` | `proposition` | 2287 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups for \texorpdfstring{$\mathcal{W}(2)$}{W(2)} via bar resolution |
| `lem:free-chiral-module-structure` | `lemma` | 2398 | Structure of free chiral modules |
| `thm:bar-resolution-acyclic` | `theorem` | 2433 | Bar resolution is acyclic |
| `thm:geometric-bar-module` | `theorem` | 2472 | Geometric bar complex |
| `thm:character-acyclic-resolution` | `theorem` | 2489 | Character via acyclic resolution |
| `thm:koszul-resolution-module` | `theorem` | 2529 | Koszul pairs simplify resolutions |
| `cor:character-koszul` | `corollary` | 2551 | Character formula for Koszul case |
| `thm:bgg-from-bar` | `theorem` | 2701 | BGG resolution from bar complex |
| `comp:bgg-sl2-pipeline` | `computation` | 2808 | BGG pipeline for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} at generic level |
| `thm:weyl-kac-geometric` | `theorem` | 2922 | Weyl--Kac character formula |
| `prop:weyl-kac-sl2-bar` | `proposition` | 3002 | Character from bar resolution |
| `prop:ext-sl2-level2` | `proposition` | 3156 | \texorpdfstring{$\mathrm{Ext}$}{Ext} groups at level~\texorpdfstring{$2$}{2} |
| `prop:ext-koszul-dual-level` | `proposition` | 3187 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
| `prop:character-koszul-duality` | `proposition` | 3239 | Characters under level-shifting Koszul duality |
| `prop:vacuum-verma-koszul` | `proposition` | 3318 | Vacuum Verma under Koszul duality |
| `prop:shapovalov-koszul` | `proposition` | 3404 | Shapovalov form under Koszul duality |
| `prop:nonvacuum-verma-koszul` | `proposition` | 3463 | Non-vacuum Verma modules under Koszul duality |
| `cor:singular-vector-symmetry` | `corollary` | 3539 | Singular vector locus symmetry |
| `prop:virasoro-verma-koszul` | `proposition` | 3616 | Virasoro Verma module under the same-family involution |
| `prop:virasoro-kac-koszul` | `proposition` | 3666 | Virasoro Kac determinant under Koszul duality |
| `thm:character-homological-corrections` | `theorem` | 3759 | Character with homological corrections |
| `thm:deformation-acyclicity` | `theorem` | 3813 | Deformation of acyclicity |
| `__unlabeled_chapters/theory/chiral_modules.tex:3879` | `calculation` | 3879 | Boson vacuum module |
| `__unlabeled_chapters/theory/chiral_modules.tex:3906` | `calculation` | 3906 | Fermion vacuum |
| `__unlabeled_chapters/theory/chiral_modules.tex:3937` | `calculation` | 3937 | W-algebra at critical level |
| `prop:bar-localization` | `proposition` | 4055 | Bar complex as localization |
| `prop:bar-singular-support` | `proposition` | 4180 | Bar complex and singular support |
| `thm:ds-koszul-intertwine` | `theorem` | 4237 | DS reduction intertwines with Koszul duality |
| `cor:ds-character-compatibility` | `corollary` | 4327 | Characters under DS reduction |
| `cor:ds-bar-level-shift` | `corollary` | 4369 | \texorpdfstring{$\mathcal{W}$}{W}-algebra cobar from KM bar |
| `thm:module-genus-tower` | `theorem` | 4424 | Module tower from bar complex with insertions |
| `prop:genus-module-koszul` | `proposition` | 4466 | Koszul duality of genus-graded modules |
| `prop:ext-bar-resolution` | `proposition` | 4596 | Ext via bar resolution |
| `thm:fusion-bar-cobar` | `theorem` | 4735 | Fusion product preservation |
| `prop:heisenberg-fusion-splitting` | `proposition` | 4845 | Heisenberg fusion splitting |

#### `chapters/theory/cobar_construction.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:bar-holonomicity` | `lemma` | 118 | Holonomicity of the bar complex |
| `lem:verdier-extension-exchange` | `lemma` | 179 | Verdier duality exchanges extensions |
| `thm:cobar-distributional-model` | `theorem` | 212 | Distributional model of the cobar |
| `cor:cobar-nilpotence-verdier` | `corollary` | 294 | \texorpdfstring{$d_{\mathrm{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} via Verdier duality |
| `thm:cobar-diff-geom` | `theorem` | 370 | Cobar differential |
| `thm:cobar-d-squared-zero` | `theorem` | 484 | Verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0} |
| `lem:cobar-sign-consistency` | `lemma` | 733 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 893 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1111 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1242 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1288 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 1561 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1609 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1630 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1676 | Topology |
| `thm:poincare-verdier` | `theorem` | 1735 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 1824 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 1848 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 1894 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 2029 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2125 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2266 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2291 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2344 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2397 | Recognition principle |
| `lem:deformation-space` | `lemma` | 2769 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 2811 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 2859 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 2938 | Curved differential formula |

#### `chapters/theory/configuration_spaces.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:local-coords-boundary` | `theorem` | 220 | Local coordinates near boundary |
| `thm:normal-crossings` | `theorem` | 330 | Normal crossings |
| `thm:closure-relations` | `theorem` | 425 | Closure relations |
| `thm:log-complex` | `theorem` | 538 | Logarithmic complex |
| `thm:arnold-relations` | `theorem` | 577 | Arnold relations |
| `prop:twisting-morphism-propagator` | `proposition` | 619 | Geometric realization of the universal twisting morphism |
| `lem:basic-log-form-residue` | `lemma` | 686 | Basic logarithmic form |
| `thm:residue-operations` | `theorem` | 753 | Residue operations |
| `prop:residue-local` | `proposition` | 808 | Residue computation in local coordinates |
| `thm:residue-sequence` | `theorem` | 857 | Residue sequence |
| `thm:bar-punctured-curve` | `theorem` | 1071 | Bar complex on punctured curves |
| `cor:conformal-blocks-punctured-bar` | `corollary` | 1138 | Conformal blocks from punctured bar complex |
| `prop:eta` | `proposition` | 1302 | Properties of \texorpdfstring{$\eta_{ij}$}{eta-ij} |
| `thm:FM-convergence` | `theorem` | 1652 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1711 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1817 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1859 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 1886 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 1908 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 1948 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 1972 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 2007 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 2029 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 2063 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2079 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2101 | Nilpotency from Arnold relations |
| `thm:arnold-jacobi` | `theorem` | 2223 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2276 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2322 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2354 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2399 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 2630 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 2700 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 2837 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3047` | `computation` | 3047 | Explicit examples |

#### `chapters/theory/deformation_theory.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-hochschild-differential` | `theorem` | 112 | The chiral Hochschild differential |
| `thm:hochschild-bar-cobar` | `theorem` | 263 | Hochschild via bar-cobar |
| `thm:hochschild-spectral-sequence` | `theorem` | 301 | Hochschild spectral sequence |
| `thm:main-koszul-hoch` | `theorem` | 420 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
| `cor:def-obs-exchange-genus0` | `corollary` | 533 | Deformation-obstruction exchange at genus \texorpdfstring{$0$}{0} |
| `comp:boson-hochschild` | `computation` | 668 | Boson Hochschild cohomology |
| `comp:fermion-hochschild` | `computation` | 694 | Fermion Hochschild cohomology |
| `prop:genus0-cyclic-coderivation` | `proposition` | 794 | Genus-\texorpdfstring{$0$}{0} cyclic coderivation complex |
| `prop:killing-linf-extension` | `proposition` | 888 | Killing cocycle \texorpdfstring{$L_\infty$}{L-infinity} extension |
| `cor:km-cyclic-deformation` | `corollary` | 986 | Kac--Moody cyclic deformation complex |
| `thm:mc2-1-km` | `theorem` | 1122 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1239 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 1481 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 1567 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 1686 | Recovery of the Killing cocycle extension |
| `prop:d-mod-squared-zero` | `proposition` | 1927 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2063 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 2238 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 2428 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 2554 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 2796 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 2942 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 3081 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 3162 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 3209 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 3501 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 3632 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 3679 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 3872 | Boson-fermion duality |

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

#### `chapters/theory/en_koszul_duality.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:linking-sphere-residue` | `proposition` | 296 | Residue as linking sphere integral |
| `thm:e2-d-squared` | `theorem` | 371 | \texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations |
| `cor:n2-recovery` | `corollary` | 531 | Recovery of chiral bar-cobar at \texorpdfstring{$n = 2$}{n = 2} |
| `prop:refines-af` | `proposition` | 589 | Our construction refines AF at \texorpdfstring{$n = 2$}{n = 2} |
| `thm:bar-swiss-cheese` | `theorem` | 901 | Bar complex as Swiss-cheese coalgebra |

#### `chapters/theory/filtered_curved.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved-fc` | `proposition` | 13 | Filtered \texorpdfstring{$\Rightarrow$}{=>} curved |
| `thm:bar-convergence-fc` | `theorem` | 116 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (16)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 33 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 90 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 199 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 245 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 293 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 322 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 384 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 411 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 468 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 526 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 606 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 776 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 797 | — |
| `thm:fourier-specialization` | `theorem` | 832 | Specialization |
| `thm:fourier-four-properties` | `theorem` | 887 | The four properties of the Fourier transform |
| `rem:fourier-genus-preview` | `remark` | 987 | Ref.\ Theorem~\ref{thm:mc2-full-resolution} |

#### `chapters/theory/higher_genus.tex` (168)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | 365 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 465 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 556 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 669 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 776 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 923 | Verdier duality of operations |
| `thm:convergence-filtered` | `theorem` | 1122 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1331 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1365 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1399 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1419 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1435 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 1737 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 1822 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2037 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2305 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2499 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2559 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 2812 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:arnold-genus1` | `theorem` | 2871 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 2906 | Nilpotency at genus 1 |
| `thm:e1-page-complete` | `theorem` | 3177 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3210 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 3337 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3424 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3478 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 3556 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 3673 | \texorpdfstring{$W_3$}{W3} obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 3744 | Explicit genus-\texorpdfstring{$1$}{1} value of the \texorpdfstring{$W_3$}{W3} obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 3765 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 3794 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 3879 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 3981 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4111 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4144 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4160 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4176 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4194 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 4217 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4239 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4272 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4344 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4374 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4460 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4504 | Grothendieck--Riemann--Roch bridge |
| `lem:involution-splitting` | `lemma` | 4638 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 4693 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 4767 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 4857 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 5013 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 5068 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 5153 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 5216 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 5267 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 5412 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 5485 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 5525 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 5579 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 5608 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 5796 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 5831 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 5883 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 5996 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 6027 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 6047 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 6113 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 6204 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 6335 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 6403 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 6501 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 6529 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 6566 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 6609 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 6645 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 6671 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 6926 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 7085 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 7135 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 7148 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 7190 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 7249 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 7291 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 7319 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 7341 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 7385 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 7558 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 7606 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 7694 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 7721 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 7749 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 7783 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 7808 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 7868 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 7914 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 7953 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 7982 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 8006 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 8031 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 8063 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 8095 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 8121 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 8137 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 8210 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 8286 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 8334 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 8423 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:genus-graded-koszul` | `theorem` | 8542 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 8573 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 8905 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 8938 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 8979 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 9115 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 9382 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 9407 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 9604 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 9656 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 9756 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 9806 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 9868 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:genus-internalization` | `theorem` | 10145 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 10235 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 10311 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 10340 | Universal modular Maurer--Cartan class |
| `thm:explicit-theta` | `theorem` | 10465 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 10673 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 11087 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 11166 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 11279 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 11313 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 11345 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 11541 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 11617 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 11682 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 11817 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 11914 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 12025 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 12162 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 12314 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 12488 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 12638 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 12832 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 12952 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 13051 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 13141 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 13253 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 13325 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 13407 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 13485 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 13562 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 13638 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 13713 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 13779 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 13857 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 13932 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 13979 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 14021 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 14077 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 14131 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 14164 | Scalar saturation for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 14202 | Scalar saturation persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 14255 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 14327 | Scalar saturation for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 14402 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 14569 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 14732 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 14815 | Cyclic rigidity at generic level |
| `thm:tautological-line-support` | `theorem` | 15100 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 15202 | MC2 reduced to cyclic model |

#### `chapters/theory/hochschild_cohomology.tex` (7)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:virasoro-hochschild` | `theorem` | 65 | Virasoro Hochschild cohomology |
| `thm:w-algebra-hochschild` | `theorem` | 109 | W-algebra cohomology |
| `__unlabeled_chapters/theory/hochschild_cohomology.tex:363` | `computation` | 363 | Explicit second-page computation |
| `thm:hochschild-chain-complex` | `theorem` | 419 | Hochschild complex is a chain complex |
| `lem:cyclic-commutes` | `lemma` | 499 | Cyclic operator commutes with Hochschild differential |
| `cor:cyclic-homology-duality` | `corollary` | 754 | Cyclic homology duality |
| `cor:hochschild-cup-exchange` | `corollary` | 786 | Hochschild cup product exchange |

#### `chapters/theory/introduction.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:central-charge-complementarity` | `theorem` | 389 | Central charge complementarity |
| `prop:chirAss-self-dual` | `proposition` | 1018 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

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
| `thm:positselski-chiral` | `theorem` | 1163 | Positselski comodule-contramodule equivalence |
| `thm:full-derived-module-equiv` | `theorem` | 1189 | Full derived module equivalence |
| `thm:cs-koszul-km` | `theorem` | 1306 | Chern--Simons equations from Koszul duality |
| `thm:linf-mc-flatness` | `theorem` | 1383 | \texorpdfstring{$L_\infty$}{L-infinity} Maurer--Cartan as homotopy flatness |
| `thm:cs-koszul-general` | `theorem` | 1453 | CS/Koszul for general non-quadratic algebras |
| `thm:bv-structure-bar` | `theorem` | 1639 | BV structure on bar complex |

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

### Part II: Examples (408)

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
| `thm:chiral-quantization` | `theorem` | 102 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 155 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 387 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 500 | Genus expansion |

#### `chapters/examples/detailed_computations.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:sl3-serre-cohomology` | `proposition` | 695 | Serre relations determine degree-3 cohomology |
| `comp:sl3-modular-rank` | `computation` | 788 | Modular rank of \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} bar differential |
| `comp:sl3-chiral-bracket-os` | `computation` | 867 | Chiral bracket rank with Orlik--Solomon forms |
| `prop:sl3-pbw-ss` | `proposition` | 928 | PBW spectral sequence for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3} |
| `comp:sl3-casimir-decomp` | `computation` | 1021 | Casimir decomposition of \texorpdfstring{$\mathfrak{sl}_3^{\otimes n}$}{sl_3tensor n} |
| `comp:sl3-koszul-dual-scan` | `computation` | 1104 | Quadratic relation scan for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:so5-bar-dims` | `proposition` | 1433 | Bar complex dimensions for \texorpdfstring{$\widehat{\mathfrak{so}}_{5,k}$}{so_5,k} |
| `prop:pbw-e2-from-vacuum-module` | `proposition` | 1738 | PBW \texorpdfstring{$E_2$}{E_2} from vacuum module data |
| `comp:sl2-bar-deg3-curvature` | `computation` | 1784 | Degree-3 bar differential and curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `comp:sl2-ce-sdr` | `computation` | 1855 | SDR and formality for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `comp:sl2-ce-verification` | `computation` | 1906 | CE cohomology of \texorpdfstring{$\mathfrak{sl}_2 \otimes t^{-1}\mathbb{C}{[t^{-1} |
| `comp:bgg-weight-decomp` | `computation` | 2035 | Weight decomposition at degrees~1 and~2 |
| `comp:bgg-differential` | `computation` | 2071 | Bar differential as BGG differential |
| `thm:bgg-sl2-bar-explicit` | `theorem` | 2105 | BGG resolution of \texorpdfstring{$L(\Lambda_0)$}{L(Lambda_0)} via bar complex |
| `prop:G2-bar-dims` | `proposition` | 2535 | Bar complex dimensions for \texorpdfstring{$\widehat{G}_{2,k}$}{G_2,k} |
| `prop:arnold-virasoro-deg3` | `proposition` | 2710 | Arnold cancellation in the Virasoro bar complex |
| `prop:heisenberg-maximal-form-cycles` | `proposition` | 2930 | Heisenberg bar complex: maximal-form cycles |
| `prop:km-generic-acyclicity` | `proposition` | 2984 | Kac--Moody acyclicity at generic level |
| `prop:w3-vacuum-dichotomy` | `proposition` | 3021 | \texorpdfstring{$\mathcal{W}_3$}{W_3} vacuum leakage dichotomy |
| `prop:fermion-bar-symmetric` | `proposition` | 3295 | Free fermion bar complex: coalgebra structure |
| `prop:E8-koszul-acyclic` | `proposition` | 3474 | \texorpdfstring{$E_8$}{E_8} bar complex Koszul acyclicity |
| `prop:virasoro-koszul-acyclic` | `proposition` | 3771 | Virasoro bar cohomology and Koszul property |
| `prop:universal-dim-formula` | `proposition` | 3833 | Universal bar complex dimension formula |
| `prop:bar-bgg-sl2` | `proposition` | 4030 | Bar--BGG for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `cor:bgg-koszul-involution` | `corollary` | 4180 | BGG involution under Koszul duality |

#### `chapters/examples/examples_summary.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 192 | Paired standard-tower MC4 frontier packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 387 | Minimal closure conditions for the standard-tower MC4 frontier |
| `cor:genus1-anomaly-ratio` | `corollary` | 517 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `prop:bar-dimensions` | `proposition` | 724 | Koszul dual Hilbert functions |
| `cor:subexp-free-field` | `corollary` | 956 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 966 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 983 | DS reduction and bar cohomology generating functions |
| `prop:hred-sl2` | `proposition` | 1278 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 1478 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1569 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1666 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1732 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 1787 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1838 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1853 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 1942 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2131 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2437 | Spectral sequence collapse |

#### `chapters/examples/free_fields.tex` (47)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:fermion-bar-complex-genus-0` | `theorem` | 49 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 105 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 177 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 188 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `prop:bc-betagamma-orthogonality` | `proposition` | 249 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 272 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 495 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:single-fermion-boson-duality` | `theorem` | 570 | Single-generator fermion-boson duality |
| `thm:heisenberg-bar` | `theorem` | 618 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 641 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | 682 | Heisenberg curved structure |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 713 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 745 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 880 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 936 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 986 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1028 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1180 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1256 | Spectral flow under Koszul duality |
| `thm:lattice-voa-bar` | `theorem` | 1332 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 1361 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:virasoro-moduli` | `theorem` | 1413 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 1451 | Geometric interpretation |
| `thm:elliptic-fermion-bar` | `theorem` | 1492 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 1529 | Higher genus Heisenberg |
| `thm:filtered-bar-complex` | `theorem` | 1697 | Filtered bar complex |
| `thm:virasoro-string` | `theorem` | 1779 | Virasoro-string duality |
| `thm:wakimoto-bar` | `theorem` | 1834 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 1864 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 1897 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 1970 | Quantum integrability via \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:heisenberg-not-self-dual` | `theorem` | 2027 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 2132 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 2163 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 2422 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 2536 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 2799 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 2948 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 2995 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 3048 | Heisenberg level inversion: curved duality |
| `thm:algebraic-string-dictionary` | `theorem` | 3082 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 3134 | Genus-\texorpdfstring{$0$}{0} string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 3176 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 3283 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 3362 | Bar complex computes genus-\texorpdfstring{$g$}{g} string integrands |
| `thm:modular-invariance` | `theorem` | 3505 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 3542 | Modular anomaly for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |

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
| `thm:universal-generating-function` | `theorem` | 1348 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1419 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1547 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1589 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1668 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 1817 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 1882 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:complementarity-classification` | `proposition` | 2115 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2169 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2339 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2439 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2455 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2480 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2512 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 2607 | Loop expansion interpretation |

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
| `thm:geometric-ope-kac-moody` | `theorem` | 211 | Geometric OPE formula |
| `thm:level-shifting-abstract` | `theorem` | 245 | Level-shifting duality, abstract form |
| `thm:wakimoto-koszul` | `theorem` | 285 | Wakimoto realization is Koszul dual |
| `thm:sl2-koszul-dual` | `theorem` | 351 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl3-koszul-dual` | `theorem` | 480 | Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `lem:bar-dims-level-independent` | `lemma` | 511 | Bar chain groups are level-independent |
| `thm:km-bar-bicomplex` | `theorem` | 549 | Bicomplex structure of the KM bar complex |
| `cor:critical-level-spectral` | `corollary` | 607 | Critical-level spectral sequence |
| `thm:bar-cohomology-level-independence` | `theorem` | 643 | Generic level-independence of bar cohomology |
| `thm:universal-kac-moody-koszul` | `theorem` | 712 | Universal Koszul duality for affine Kac--Moody |
| `prop:ff-channel-shear` | `proposition` | 839 | Feigin--Frenkel shear on channel pair |
| `thm:screening-bar` | `theorem` | 889 | Screening charges implement bar differential |
| `thm:w-algebra-koszul` | `theorem` | 955 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality at critical level |
| `thm:kac-moody-ainfty` | `theorem` | 1019 | \texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody |
| `thm:km-higher-genus-corrections` | `theorem` | 1058 | Higher genus corrections to Koszul duality |
| `thm:closed-form-ope` | `theorem` | 1112 | Closed-form OPE for Koszul dual |
| `thm:km-quantum-groups` | `theorem` | 1175 | Connection to quantum groups |
| `prop:bar-admissible` | `proposition` | 1501 | Bar complex at admissible level |
| `cor:bar-admissible-finiteness` | `corollary` | 1571 | Bar complex finiteness at non-degenerate admissible levels |
| `thm:kw-bar-spectral` | `theorem` | 1659 | Kac--Wakimoto formula via bar spectral sequence |
| `thm:kw-bar-general-rank` | `theorem` | 1771 | KW formula via bar complex: general simple \texorpdfstring{$\mathfrak{g}$}{g} |
| `prop:admissible-verlinde-bar` | `proposition` | 1841 | Admissible fusion rules from bar complex |
| `prop:bar-whittaker` | `proposition` | 2080 | Bar complex via Whittaker resolution |
| `thm:sl2-genus1-curvature` | `theorem` | 2161 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-inversion` | `theorem` | 2226 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} |
| `thm:sl2-genus1-complementarity` | `theorem` | 2278 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at generic level |
| `prop:sl2-genus1-partition` | `proposition` | 2344 | Partition function via complementarity |
| `thm:sl3-genus1-curvature` | `theorem` | 2407 | Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-inversion` | `theorem` | 2453 | Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `thm:sl3-genus1-complementarity` | `theorem` | 2492 | Genus-1 complementarity for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} |
| `prop:sl3-genus1-partition` | `proposition` | 2529 | Partition function for \texorpdfstring{$\widehat{\mathfrak{sl}}_{3,k}$}{sl-hat_3,k} at genus 1 |
| `thm:oper-bar-h0` | `theorem` | 2697 | Oper space from bar complex at \texorpdfstring{$H^0$}{H0} |
| `prop:oper-bar-h1` | `proposition` | 2727 | \texorpdfstring{$H^1$}{H1} at critical level |
| `thm:oper-bar` | `theorem` | 2757 | Full derived oper identification |

#### `chapters/examples/lattice_foundations.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:lattice:cocycle-class` | `lemma` | 166 | Cocycle classification |
| `thm:lattice:e1-vs-einf` | `theorem` | 328 | \texorpdfstring{$\Eone$}{E1} vs.\ \texorpdfstring{$\Einf$}{E-infinity} classification |
| `thm:lattice:bar-structure` | `theorem` | 547 | Lattice bar complex structure |
| `prop:lattice:bar-D4` | `proposition` | 644 | \texorpdfstring{$D_4$}{D4} bar complex and triality |
| `prop:lattice:bar-E8` | `proposition` | 667 | \texorpdfstring{$E_8$}{E8} bar complex and self-duality |
| `thm:lattice:unimodular-self-dual` | `theorem` | 701 | Unimodular lattice self-duality |
| `thm:lattice:koszul-dual` | `theorem` | 735 | Koszul dual of lattice vertex algebra |
| `thm:lattice:koszul-morphism` | `theorem` | 780 | Koszul morphism for lattice algebras |
| `thm:lattice:direct-sum` | `theorem` | 866 | Tensor product from direct sum |
| `prop:lattice:sublattice` | `proposition` | 911 | Sublattice maps |
| `thm:lattice:hochschild` | `theorem` | 1116 | Lattice Hochschild cohomology |
| `cor:lattice:hochschild-unimodular` | `corollary` | 1161 | Unimodular case |
| `prop:lattice:genus-1` | `proposition` | 1203 | Genus-1 partition function |
| `thm:lattice:modular-invariance` | `theorem` | 1226 | Modular invariance |
| `prop:lattice:self-dual-criterion` | `proposition` | 1352 | Koszul self-duality criterion |
| `prop:lattice:D4-triality` | `proposition` | 1369 | \texorpdfstring{$D_4$}{D4} and triality |
| `prop:lattice-module-koszul` | `proposition` | 1394 | Lattice VOA modules under Koszul duality |
| `prop:lattice:deformation-properties` | `proposition` | 1596 | Deformation properties |
| `prop:lattice:ordering-cycle-phase` | `proposition` | 1780 | Phase dependence of the ordering cycle |
| `thm:quantum-lattice-structure` | `theorem` | 2405 | Quantum lattice algebra: structural properties |
| `thm:lattice:e1-bar-cohomology` | `theorem` | 2473 | \texorpdfstring{$\Eone$}{E1} bar cohomology |
| `thm:e1-inversion-principle` | `theorem` | 2547 | \texorpdfstring{$\Eone$}{E1} inversion principle |
| `prop:lattice:screening-structure` | `proposition` | 2706 | Screening current structure |
| `prop:lattice:factorization-decomposition` | `proposition` | 3009 | Lattice factorization decomposition |
| `thm:lattice:factorization-koszul` | `theorem` | 3090 | Lattice factorization Koszul pair |
| `cor:lattice:factorization-dk-level1` | `corollary` | 3260 | Factorization DK at level \texorpdfstring{$1$}{1} |
| `prop:lattice:sectorwise-compactness` | `proposition` | 3456 | Sectorwise compactness |
| `thm:lattice:homotopy-factorization-dk` | `theorem` | 3499 | Homotopy-level lattice factorization DK |
| `prop:lattice:level-k-factorization` | `proposition` | 3657 | Level-\texorpdfstring{$k$}{k} lattice factorization bar-cobar |
| `thm:lattice:level-k-dk` | `theorem` | 3704 | Level-\texorpdfstring{$k$}{k} factorization DK for KM algebras |
| `thm:lattice:quantum-factorization-dk` | `theorem` | 3790 | Quantum lattice factorization DK |
| `prop:lattice:yangian-bridge-level1` | `proposition` | 3862 | Lattice--Yangian DK bridge at level \texorpdfstring{$1$}{1} |

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
| `thm:w-bar-coalg` | `theorem` | 89 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 792 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `prop:w3-deg3-vacuum` | `proposition` | 1301 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1508 | DS hierarchy and Koszul duality |

#### `chapters/examples/w_algebras_framework.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-algebra-koszul-main` | `theorem` | 55 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 240 | Subregular \texorpdfstring{$\mathcal{W}$}{W}-algebra duality for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} |
| `thm:w-geometric-ope` | `theorem` | 549 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 620 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-critical-bar` | `theorem` | 660 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 697 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 823 | Virasoro self-duality at \texorpdfstring{$c=0$}{c=0} |
| `thm:vir-genus1-curvature` | `theorem` | 949 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 1000 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1064 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1247 | Koszul dual of \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1328 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1394 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 1464 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 1559 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 1655 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 1676 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-center-langlands` | `theorem` | 1765 | \texorpdfstring{$\mathcal{W}$}{W}-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 1870 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |

#### `chapters/examples/yangians.tex` (136)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 136 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 221 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 254 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 313 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 354 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 409 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 473 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 717 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 838 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `corollary` | 882 | Seed-normalized extraction of the dg-shifted local coefficient |
| `prop:dg-shifted-rtt-degree2-scalar-normalization` | `proposition` | 905 | Degree-\texorpdfstring{$2$}{2} scalar normalization and Casimir reduction |
| `cor:dg-shifted-rtt-degree2-casimir-normalization` | `corollary` | 935 | Trace-zero Casimir convention reduces to the same scalar packet |
| `prop:dg-shifted-rtt-degree2-fundamental-casimir` | `proposition` | 947 | Fundamental Casimir insertion fixes the normalized one-loop scalar |
| `cor:factorization-fundamental-casimir-identity` | `corollary` | 967 | Factorization-side fundamental Casimir identity |
| `prop:dg-shifted-factorization-shared-seed` | `proposition` | 987 | Shared bar seed transports the fundamental degree-\texorpdfstring{$2$}{2} coefficient |
| `cor:yangian-typea-dg-local-closure` | `corollary` | 1008 | Shared bar seed closes the local dg-shifted type-\texorpdfstring{$A$}{A} MC4 packet |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1064 | Presentation-level criterion for finite RTT dg quotients |
| `prop:dg-shifted-rtt-locality-criterion` | `proposition` | 1082 | Pole-order locality criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-formula-preservation` | `proposition` | 1106 | RTT-level preservation from the rational line-operator formulas |
| `prop:dg-shifted-rtt-coefficient-criterion` | `proposition` | 1128 | Coefficient-level RTT criterion for finite-stage identification |
| `prop:dg-shifted-rtt-kernel-coefficient-criterion` | `proposition` | 1148 | Kernel-coefficient criterion for finite RTT identification |
| `prop:dg-shifted-rtt-oneloop-kernel-criterion` | `proposition` | 1164 | One-loop kernel identity criterion for finite RTT quotients |
| `prop:dg-shifted-rtt-evaluation-detection` | `proposition` | 1189 | Evaluation-detection criterion for one-loop RTT identities |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1209 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1227 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1257 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `corollary` | 1319 | Line-side boundary-strip support bound on generic tensor powers |
| `prop:dg-shifted-rtt-defect-support-mechanism` | `proposition` | 1380 | Defect-side support mechanism from RTT degree |
| `prop:dg-shifted-rtt-universal-generic-packets` | `proposition` | 1430 | Universal generic packet reduction for the boundary strip |
| `cor:dg-shifted-rtt-minimal-canonical-family` | `corollary` | 1514 | Minimal canonical family from the boundary-strip induction |
| `prop:dg-shifted-rtt-finite-tensor-detection` | `proposition` | 1554 | Finite tensor-length detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 1635 | Top-packet induction step on the universal family |
| `prop:dg-shifted-rtt-top-packet-line-formula` | `proposition` | 1684 | Closed-form line-side top-support class on the top packet |
| `cor:dg-shifted-rtt-top-packet-comparison` | `corollary` | 1766 | Abstract top-packet comparison |
| `prop:dg-shifted-rtt-top-packet-standard-discharge` | `proposition` | 1801 | Standard-evaluation discharge of the RTT top-packet class |
| `cor:dg-shifted-rtt-top-packet-conditional-closure` | `corollary` | 1855 | Conditional closure of the top-packet induction step |
| `prop:dg-shifted-rtt-universal-evaluation-rigidity` | `proposition` | 1884 | Universal-packet evaluation rigidity from the fundamental line |
| `cor:dg-shifted-rtt-top-packet-from-one-factor` | `corollary` | 1944 | Top-packet closure from the one-factor universal packet |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 1974 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 2071 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 2141 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 2210 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 2247 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 2303 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 2363 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2424 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2523 | Standard type-A fundamental line operator has the expected local residue |
| `prop:yangian-rank-dependence` | `proposition` | 3278 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 3415 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 3504 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 3560 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 3610 | DK-2 reduction to thick generation in category~\texorpdfstring{$\mathcal{O}$}{O} |
| `prop:dk2-thick-generation-typeA` | `proposition` | 3662 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `lem:composition-thick-generation` | `lemma` | 3756 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 3787 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 3871 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 3973 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 3995 | Finite-dimensional factorization Drinfeld--Kohno, type~\texorpdfstring{$A$}{A} |
| `cor:dk-partial-conj` | `corollary` | 4070 | Partial resolution of Conjecture~\textup{\ref{conj:full-derived-dk}} |
| `cor:dk-poly-catO` | `corollary` | 4089 | Factorization DK for polynomial category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A} |
| `lem:fd-thick-closure` | `lemma` | 4161 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 4247 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 4498 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 4607 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 4765 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 4785 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 4810 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 4983 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:derived-dk-affine` | `theorem` | 5390 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 5489 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 5642 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 5721 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 5836 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 5885 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 6022 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 6210 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 6251 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 6507 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 6628 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 6830 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 6937 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 7035 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 7241 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 7320 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 7373 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 7490 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 7549 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 7632 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 7713 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 7744 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 7781 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 7848 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 7878 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 7909 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 7968 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 8047 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 8076 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 8143 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 8175 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 8213 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 8228 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 8278 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 8335 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 8382 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 8473 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 8573 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 8613 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 8649 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 8676 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 8819 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 8851 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 8901 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 8939 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 8966 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 8999 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 9037 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 9063 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 9249 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 9300 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 9335 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 9389 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 9422 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 9473 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 9548 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts` | `corollary` | 9704 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet` | `corollary` | 9733 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization` | `corollary` | 9766 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization` | `corollary` | 9797 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet` | `corollary` | 9848 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 9955 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 10054 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 10115 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 10165 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 10224 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed` | `corollary` | 10267 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line` | `corollary` | 10300 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |

### Part III: Connections (52)

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
| `thm:config-space-bv` | `theorem` | 1050 | Configuration space BV structure |
| `thm:bv-functor` | `theorem` | 1143 | BV functor |

#### `chapters/connections/concordance.tex` (18)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 225 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 239 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `thm:master-pbw` | `theorem` | 512 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 538 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, originally conjectured)} |
| `prop:standard-tower-mc5-reduction` | `proposition` | 720 | Standard-tower MC5 reduction after MC3 and realized MC4 |
| `cor:standard-tower-mc5-closure` | `corollary` | 808 | Standard-tower MC5 closure on the canonical Yangian locus |
| `prop:en-n2-recovery` | `proposition` | 1560 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 1706 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 1764 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 1798 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 1814 | Physical anomaly cancellation for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2032 | Hodge symmetry from complementarity |
| `thm:lagrangian-complementarity` | `theorem` | 2469 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 2504 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 2683 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 2728 | Spectral discriminant --- general case |
| `thm:family-index` | `theorem` | 2959 | Family index theorem for genus expansions |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 3483 | Volume~I concrete modular datum |

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
| `prop:virasoro-c26-selfdual` | `proposition` | 152 | Virasoro NAP duality at \texorpdfstring{$c=26$}{c=26} |
| `thm:genus-complementarity` | `theorem` | 279 | Genus complementarity |

### Appendices (97)

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
| `prop:scalar-mc-skeleton` | `proposition` | 114 | The scalar shadow is an abelian MC element |
| `thm:spectral-cumulant-hierarchy` | `theorem` | 173 | Spectral cumulant hierarchy |
| `thm:first-obstruction-traceless-quadratic` | `theorem` | 255 | First obstruction is traceless and quadratic |
| `cor:filtered-lift-vanishing` | `corollary` | 328 | Vanishing criterion for filtered lifts |
| `lem:positive-weight-contraction` | `lemma` | 396 | Positive-weight contraction |
| `thm:vir-positive-weight-acyclic` | `theorem` | 413 | Positive-weight Virasoro sectors are acyclic |
| `cor:vir-localization-reduced-spectral` | `corollary` | 432 | Localization to reduced spectral sectors |
| `prop:odd-sheet-rigidity` | `proposition` | 460 | Odd-sheet rigidity for one-line reductions |
| `cor:mu2-centered-at-13` | `corollary` | 501 | The genus-\(2\) one-line coefficient is centered at \texorpdfstring{$13$}{13} |
| `lem:universal-branch-moments` | `lemma` | 564 | Universal branch moments |
| `thm:hodge-depth-formula` | `theorem` | 626 | Depth formula |
| `lem:separating-hodge-splitting` | `lemma` | 659 | Separating Hodge splitting |
| `lem:nonseparating-hodge-extension` | `lemma` | 701 | Nonseparating Hodge extension |
| `thm:genus-two-transparency` | `theorem` | 740 | Genus-\(2\) transparency on a one-line branch quotient |
| `cor:vir-genus-two-vanishing` | `corollary` | 784 | Virasoro genus-\(2\) coefficient vanishes in the one-line quotient |
| `cor:first-primitive-genus-three` | `corollary` | 796 | The first primitive traceless coefficient begins in genus \texorpdfstring{$3$}{3} |
| `lem:genus-three-rose-unique` | `lemma` | 814 | Uniqueness of the primitive rose in genus \texorpdfstring{$3$}{3} |
| `thm:pure-branch-primitive-coefficient` | `theorem` | 844 | Pure-branch primitive coefficient on a rank-two sheet |
| `thm:first-primitive-top-hodge-layer` | `theorem` | 939 | First primitive top-Hodge layer |
| `cor:genus-three-primitive-top-hodge` | `corollary` | 976 | The genus-\(3\) primitive coefficient |
| `cor:shared-sheet-universal-coefficients` | `corollary` | 1048 | Universal coefficients on the shared sheet |

#### `appendices/coderived_models.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:coderived-adequacy` | `proposition` | 240 | Adequacy |
| `thm:stratified-conservative-restriction` | `theorem` | 571 | Stratified conservative restriction |
| `prop:provisional-embedding` | `proposition` | 647 | Provisional embedding |
| `prop:bar-ran-well-defined` | `proposition` | 697 | Bar functor well-definedness on Ran |
| `thm:fact-co-contra-general` | `theorem` | 724 | Factorization co-contra correspondence |

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
| `prop:classification-table` | `proposition` | 433 | Classification table \cite{FBZ04, BD04} |

#### `appendices/homotopy_transfer.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:sdr-existence` | `lemma` | 100 | Existence of SDR |
| `thm:chiral-htt` | `theorem` | 409 | Chiral homotopy transfer |
| `thm:bar-cobar-htt` | `theorem` | 476 | Bar-cobar inversion via homotopy transfer |
| `prop:trees-boundary-strata` | `proposition` | 570 | Trees as boundary strata |
| `prop:genus1-curvature-m0` | `proposition` | 684 | Genus-\texorpdfstring{$1$}{1} curvature as \texorpdfstring{$m_0$}{m0} |

#### `appendices/koszul_reference.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:extended-koszul-appendix` | `theorem` | 17 | Extended Koszul duality |
| `thm:genus-graded-koszul-duality-appendix` | `theorem` | 73 | Genus-graded Koszul duality theorem |
| `lem:genus-graded-koszul-resolution-appendix` | `lemma` | 110 | Genus-graded Koszul complex resolution |
| `thm:genus-graded-mc-appendix` | `theorem` | 131 | Genus-graded MC elements parametrize deformations |
| `thm:essential-image-koszul` | `theorem` | 260 | Essential image of Koszul duality |
| `lem:conilpotency-necessary` | `lemma` | 322 | Conilpotency is necessary |
| `lem:connectedness-augmentation` | `lemma` | 351 | Connectedness characterizes augmentation |
| `thm:koszul-geom-rep` | `theorem` | 380 | Koszul duals are geometrically representable |
| `cor:geom-implies-koszul` | `corollary` | 412 | Converse: geometric representability implies Koszul |
| `thm:curvature-central-appendix` | `theorem` | 462 | Curvature must be central |
| `thm:uniqueness-algebra` | `theorem` | 615 | Uniqueness up to quasi-isomorphism |

#### `appendices/nilpotent_completion.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:geom-conilpotent` | `proposition` | 90 | Geometric manifestation |
| `thm:completion-convergence` | `theorem` | 118 | Completion convergence |
| `thm:completed-bar-cobar` | `theorem` | 190 | Completed bar-cobar duality |
| `thm:koszul-dual-characterization` | `theorem` | 250 | Characterization of Koszul duals |

#### `appendices/nonlinear_modular_shadows.tex` (33)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:nms-ambient-complementarity-tangent` | `theorem` | 92 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | 146 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | 192 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | 201 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | 222 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | 237 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | 336 | Quartic shadow master equations |
| `thm:nms-separating-boundary-recursion` | `theorem` | 375 | Separating boundary recursion through quartic order |
| `thm:nms-shadow-cocycle-characterization` | `theorem` | 437 | Finite-order realization of the universal class |
| `prop:nms-quartic-closure-envelope` | `proposition` | 488 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | 511 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | 531 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | 555 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | 579 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | 646 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-boundary-law` | `corollary` | 670 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | 687 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | 708 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | 734 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | 772 | Virasoro mixed shadow theorem |
| `cor:nms-virasoro-cubic-leading` | `corollary` | 800 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | 830 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `prop:nms-w3-visible-resonance-factor` | `proposition` | 869 | Visible quartic resonance factor for \texorpdfstring{$\mathcal W_3$}{W3} |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | 909 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | 927 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | 943 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | 1052 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | 1104 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 1128 | Clutching law for the modular quartic resonance class |
| `thm:nms-first-nonlinear-shadow-theta` | `theorem` | 1168 | The first nonlinear shadow of \texorpdfstring{$\Theta_{\cA}$}{ThetaA} |
| `cor:nms-family-boundary-behavior` | `corollary` | 1181 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | 1250 | Functoriality and duality through quartic order |
| `thm:nms-unified-summary` | `theorem` | 1305 | Ambient complementarity and nonlinear modular shadows |

#### `appendices/sign_conventions.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:LV-conversion-complete` | `proposition` | 381 | Loday--Vallette conversion |

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
