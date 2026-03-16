# Theorem Registry

Auto-generated on 2026-03-16 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 1246 |
| Total tagged claims | 1757 |
| Active files in `main.tex` | 67 |
| Total `.tex` files scanned | 74 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 1246 |
| `ProvedElsewhere` | 352 |
| `Conjectured` | 140 |
| `Heuristic` | 19 |
| `Open` | 0 |

## ProvedHere By Environment

| Environment | Count |
|---|---:|
| `theorem` | 517 |
| `proposition` | 393 |
| `corollary` | 215 |
| `lemma` | 81 |
| `computation` | 33 |
| `calculation` | 3 |
| `remark` | 3 |
| `verification` | 1 |

## ProvedHere By Part

| Part | Count |
|---|---:|
| Frame | 14 |
| Part I: Theory | 587 |
| Part II: Examples | 428 |
| Part III: Connections | 95 |
| Appendices | 122 |

## Most Populated Proved Files

| File | ProvedHere claims |
|---|---:|
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 92 |
| `chapters/theory/higher_genus_modular_koszul.tex` | 72 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 68 |
| `chapters/theory/higher_genus_complementarity.tex` | 67 |
| `appendices/nonlinear_modular_shadows.tex` | 58 |
| `chapters/theory/higher_genus_foundations.tex` | 58 |
| `chapters/theory/chiral_modules.tex` | 52 |
| `chapters/examples/free_fields.tex` | 47 |
| `chapters/examples/kac_moody.tex` | 42 |
| `chapters/examples/genus_expansions.tex` | 35 |
| `chapters/theory/configuration_spaces.tex` | 35 |
| `chapters/examples/lattice_foundations.tex` | 34 |
| `chapters/examples/w_algebras.tex` | 32 |
| `chapters/theory/chiral_hochschild_koszul.tex` | 31 |
| `chapters/examples/yangians_computations.tex` | 29 |
| `chapters/theory/cobar_construction.tex` | 29 |
| `chapters/theory/chiral_koszul_pairs.tex` | 26 |
| `chapters/examples/bar_complex_tables.tex` | 25 |
| `chapters/examples/yangians_foundations.tex` | 25 |
| `chapters/theory/bar_construction.tex` | 25 |

## Complete Proved Registry

### Frame (14)

#### `chapters/frame/heisenberg_frame.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 465 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 822 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 918 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1081 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1305 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1327 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1490 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1668 | Quantum complementarity for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2273 | $\mathfrak{sl}_2$ bar complex as Swiss-cheese coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2345 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2394 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2475 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 2513 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 2781 | CS $R$-matrix from the bar complex |

### Part I: Theory (587)

#### `chapters/theory/algebraic_foundations.tex` (3)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:comparison-our-glz` | `proposition` | 529 | Comparison: our approach vs GLZ |
| `thm:geometric-bridge` | `theorem` | 817 | Geometric realization |
| `prop:orthogonal` | `proposition` | 942 | Orthogonality |

#### `chapters/theory/bar_cobar_adjunction_curved.tex` (92)

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
| `prop:winfty-stage4-visible-orthogonality` | `proposition` | 2488 | Stage-\texorpdfstring{$4$}{4} visible mixed-weight orthogonality from the Virasoro Ward identity |
| `prop:winfty-stage4-visible-w3-normalization` | `proposition` | 2519 | Stage-\texorpdfstring{$4$}{4} visible \texorpdfstring{$W^{(3)}$}{W3} normalization from the theorematic \texorpdfstring{$W_3$}{W3} packet |
| `cor:winfty-stage4-single-scalar-equivalent` | `corollary` | 2627 | Equivalent exact forms of the remaining \texorpdfstring{$W_\infty$}{W_infty} stage-\texorpdfstring{$4$}{4} input |
| `prop:winfty-stage4-residue-pairing-reduction` | `proposition` | 2675 | Stage-\texorpdfstring{$4$}{4} swap-even residue channel from a visible invariant pairing |
| `cor:winfty-stage4-residue-three-channel` | `corollary` | 2721 | Stage-\texorpdfstring{$4$}{4} residue packet as three higher-spin channels on the visible pairing locus |
| `cor:winfty-stage4-primitive-transport-square-triple` | `corollary` | 2748 | Stage-\texorpdfstring{$4$}{4} higher-spin comparison as a primitive-plus-transport square triple on the visible pairing locus |
| `cor:winfty-stage4-visible-borcherds-two-primitive` | `corollary` | 2890 | Equivalent exact forms of the remaining stage-\texorpdfstring{$4$}{4} higher-spin transport input on the visible pairing locus |
| `prop:winfty-stage4-local-attack-order` | `proposition` | 2929 | Exact local attack order for the stage-\texorpdfstring{$4$}{4} \texorpdfstring{$W_\infty$}{W_infty} packet |
| `prop:winfty-stage-growth-virasoro-target-contraction` | `proposition` | 2993 | Uniform Virasoro-target contraction of reduced incremental packets under the normalized residue package |
| `cor:winfty-stage5-residue-eight-channel` | `corollary` | 3048 | First reduced stage beyond \texorpdfstring{$\mathcal{I}_4$}{I4} under the normalized residue package |
| `cor:winfty-stage5-higher-spin-packet` | `corollary` | 3090 | First higher-spin packet beyond \texorpdfstring{$\mathcal{I}_4$}{I4} |
| `prop:winfty-stage5-visible-w5-normalization` | `proposition` | 3184 | Stage-\texorpdfstring{$5$}{5} visible \texorpdfstring{$W^{(5)}$}{W5} normalization from the theorematic \texorpdfstring{$W^{(5)}$-$W^{(5)}\to T$}{W5-W5 to T} coefficient |
| `prop:winfty-stage5-target5-pole3-pairing-vanishing` | `proposition` | 3209 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$3$}{3} transport singleton vanishes on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-from-self-return` | `proposition` | 3248 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton from the self-return singleton on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `prop:winfty-stage5-target5-pole4-w4-vanishing` | `proposition` | 3268 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} pole-\texorpdfstring{$4$}{4} transport singleton vanishes on a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-self-return-vanishing-on-pairing` | `corollary` | 3306 | Stage-\texorpdfstring{$5$}{5} self-return singleton vanishes on the visible \texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5} pairing locus |
| `prop:winfty-stage5-tail-from-w3-pairing` | `proposition` | 3323 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(3)}$}{W3}-pairing locus |
| `prop:winfty-stage5-tail-from-w4-pairing` | `proposition` | 3346 | Stage-\texorpdfstring{$5$}{5} reduced tail singleton from a visible \texorpdfstring{$W^{(4)}$}{W4}-pairing locus |
| `cor:winfty-stage5-tail-cross-target-reduction` | `corollary` | 3368 | Stage-\texorpdfstring{$5$}{5} tail singleton equates neighboring transport channels |
| `cor:winfty-stage5-target5-corridor-to-tail` | `corollary` | 3384 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor contracts to the tail singleton |
| `cor:winfty-stage5-target5-no-new-independent-data` | `corollary` | 3394 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$5$}{5} corridor carries no new independent coefficient |
| `prop:winfty-stage5-target4-pole5-w4-vanishing` | `proposition` | 3410 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-target3-pole5-w3-vanishing` | `proposition` | 3422 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$3$}{3} pole-\texorpdfstring{$5$}{5} transport singleton vanishes |
| `prop:winfty-stage5-transport-cross-target-reduction` | `proposition` | 3435 | Stage-\texorpdfstring{$5$}{5} target-\texorpdfstring{$4$}{4}/target-\texorpdfstring{$3$}{3} transport channels are paired on a visible \texorpdfstring{$W^{(5)}$}{W5}-pairing locus |
| `cor:winfty-stage5-transport-effective-independent-frontier` | `corollary` | 3453 | Stage-\texorpdfstring{$5$}{5} mixed transport frontier carries one effective independent coefficient |
| `cor:winfty-stage5-effective-independent-frontier` | `corollary` | 3468 | Stage-\texorpdfstring{$5$}{5} higher-spin packet reduces to one effective independent coefficient |
| `prop:winfty-stage5-local-attack-order` | `proposition` | 3487 | Exact local attack order for the first stage-\texorpdfstring{$5$}{5} higher-spin packet |
| `prop:winfty-stage5-principal-one-coefficient-factorization` | `proposition` | 3694 | Principal stage-\texorpdfstring{$5$}{5} one-coefficient normal form factors through the target-\texorpdfstring{$5$}{5} corridor and the residual front |
| `prop:winfty-stage5-one-coefficient-reduction` | `proposition` | 3711 | Stage-\texorpdfstring{$5$}{5} higher-spin comparison reduces to one coefficient on the full visible pairing locus |
| `cor:winfty-stage5-exact-remaining-input` | `corollary` | 3748 | Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input package |
| `cor:winfty-stage5-one-defect-family` | `corollary` | 3788 | Stage-\texorpdfstring{$5$}{5} higher-spin defect family collapses to one representative defect on the full visible pairing locus |
| `cor:winfty-stage5-visible-conjecture-network-collapse` | `corollary` | 4084 | Visible stage-\texorpdfstring{$5$}{5} local conjecture network collapses to one nontrivial singleton under principal normal form |
| `cor:winfty-stage5-visible-defect-classes` | `corollary` | 4126 | Visible stage-\texorpdfstring{$5$}{5} local defect classes under principal normal form |
| `cor:w4-ds-stage4-square-class-reduction` | `corollary` | 4354 | Principal stage-\texorpdfstring{$4$}{4} higher-spin packet from two primitive square classes |
| `thm:central-implies-strict` | `theorem` | 4592 | Centrality implies strict nilpotence |
| `thm:mc-deformations-DISABLED` | `theorem` | 4933 | MC elements as quantum deformations |
| `thm:mc-periods-DISABLED` | `theorem` | 4969 | MC elements via period integrals |
| `thm:genus-zero-strict` | `theorem` | 5030 | Strict nilpotence at genus zero |
| `thm:genus-induction-strict` | `theorem` | 5042 | Strict nilpotence at all genera |
| `thm:bar-modular-operad` | `theorem` | 5150 | Modular operad structure of the bar complex |
| `cor:genus-expansion-converges` | `corollary` | 5329 | Genus expansion convergence |
| `thm:bar-functorial-grothendieck` | `theorem` | 5389 | Functoriality of bar construction |

#### `chapters/theory/bar_cobar_adjunction_inversion.tex` (21)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:filtered-to-curved` | `proposition` | 325 | Filtered implies curved |
| `thm:bar-convergence` | `theorem` | 544 | Convergence of bar construction |
| `lem:chiral-co-contra-adjunction` | `lemma` | 853 | Adjunction |
| `prop:chiral-inj-proj-resolutions` | `proposition` | 968 | Injective and projective resolutions |
| `prop:cdg-hom-complex` | `proposition` | 1041 | Explicit CDG Hom-complex |
| `cor:coacyclic-injective-contractible` | `corollary` | 1085 | Contractibility of coacyclic injectives |
| `lem:Phi-Psi-properties` | `lemma` | 1153 | Key properties of \texorpdfstring{$\Phi_C^{\mathrm{ch}}$}{Phi_C^ch} and \texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch} |
| `thm:chiral-co-contra-correspondence` | `theorem` | 1219 | Chiral comodule-contramodule correspondence |
| `thm:positselski-chiral-proved` | `theorem` | 1354 | Positselski equivalence for chiral algebras |
| `thm:full-derived-module-equiv-proved` | `theorem` | 1420 | Full derived module equivalence |
| `thm:bar-cobar-inversion-qi` | `theorem` | 1540 | Bar-cobar inversion is quasi-isomorphism |
| `lem:bar-cobar-associated-graded` | `lemma` | 1673 | Associated graded |
| `thm:bar-cobar-spectral-sequence` | `theorem` | 1689 | Bar-cobar spectral sequence |
| `thm:spectral-sequence-collapse` | `theorem` | 1745 | Collapse at \texorpdfstring{$E_2$}{E2} |
| `thm:genus-graded-convergence` | `theorem` | 1768 | Genus-graded convergence |
| `lem:pushforward-preserves-qi` | `lemma` | 1828 | Derived pushforward preserves QI |
| `prop:counit-qi` | `proposition` | 1873 | Counit is quasi-isomorphism |
| `thm:bar-cobar-inversion-functorial` | `theorem` | 1885 | Functoriality |
| `cor:derived-equivalence-bar-cobar` | `corollary` | 1920 | Derived equivalence |
| `prop:bar-fh` | `proposition` | 2151 | Bar construction as factorization homology |
| `prop:cobar-fh` | `proposition` | 2229 | Cobar as factorization cohomology |

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

#### `chapters/theory/chiral_hochschild_koszul.tex` (31)

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
| `prop:modular-deformation-truncation` | `proposition` | 1192 | Genus truncation |
| `thm:mc2-1-km` | `theorem` | 1264 | MC2-1 for Kac--Moody algebras |
| `cor:km-minimal-linf` | `corollary` | 1381 | Minimal cyclic \texorpdfstring{$L_\infty$}{L-infinity} model for Kac--Moody |
| `prop:stokes-regularity-FM` | `proposition` | 1623 | Stokes regularity for graph amplitudes on FM compactifications |
| `thm:cyclic-linf-graph` | `theorem` | 1709 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} structure via chiral graph complex |
| `cor:killing-recovery-graph` | `corollary` | 1828 | Recovery of the Killing cocycle extension |
| `prop:d-mod-squared-zero` | `proposition` | 2096 | $d_{\mathrm{mod}}^2 = 0$ |
| `thm:quantum-master-equation` | `theorem` | 2232 | Quantum master equation |
| `thm:total-differential-from-mc` | `theorem` | 2407 | Total differential from the MC class |
| `prop:characteristic-hierarchy` | `proposition` | 2597 | Characteristic hierarchy |
| `thm:chiral-homology-recovery` | `theorem` | 2723 | Chiral homology recovery |
| `prop:non-scalar-criterion` | `proposition` | 2968 | Non-scalar criterion |
| `rem:step2-stabilization-threshold` | `remark` | 3114 | Step~2 gap: stabilization threshold |
| `prop:periodicity-quantum-input` | `proposition` | 3253 | Quantum periodicity profile under admissible-level KL/DS transport |
| `thm:geometric-periodicity-weak` | `theorem` | 3334 | Geometric tautological depth bound |
| `thm:geometric-depth-smooth` | `theorem` | 3381 | Sharp geometric depth on smooth moduli |
| `prop:periodicity-exchange-koszul` | `proposition` | 3673 | Periodicity-profile transport under Koszul duality |
| `thm:bar-cobar-resolution` | `theorem` | 3804 | Bar-cobar resolution |
| `thm:HH-config-space-formula` | `theorem` | 3851 | HH* via configuration spaces |
| `ver:boson-fermion-HH` | `verification` | 4044 | Boson-fermion duality |
| `prop:hochschild-cech-ss` | `proposition` | 4207 | Hochschild--\v{C}ech spectral sequence |

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
| `lem:cobar-sign-consistency` | `lemma` | 732 | Sign consistency for cobar differential |
| `thm:fermion-boson-koszul` | `theorem` | 892 | Fermion-boson Koszul duality |
| `thm:bar-cobar-verdier` | `theorem` | 1110 | Bar-cobar Verdier |
| `cor:bar-cobar-inverse` | `corollary` | 1241 | Bar-cobar mutual inverses |
| `prop:cobar-bar-augmentation` | `proposition` | 1287 | Explicit cobar-bar augmentation |
| `thm:cobar-cech` | `theorem` | 1560 | Cobar as Čech complex |
| `thm:cobar-free` | `theorem` | 1608 | Cobar as free chiral algebra |
| `thm:geom-unit` | `theorem` | 1629 | Geometric unit of adjunction |
| `thm:weak-topology` | `theorem` | 1675 | Topology |
| `thm:poincare-verdier` | `theorem` | 1734 | Bar-cobar as Poincaré--Verdier duality |
| `thm:curved-mc-cobar` | `theorem` | 1823 | Curved Maurer--Cartan equation |
| `prop:km-bar-curvature` | `proposition` | 1847 | Curvature of the affine bar complex |
| `cor:level-shifting-part1` | `corollary` | 1893 | Level-shifting duality |
| `thm:central-charge-cocycle` | `theorem` | 2028 | Central charge cocycle |
| `thm:genus1-cobar-bar` | `theorem` | 2124 | Genus 1 cobar-bar duality |
| `thm:universal-extension-tower` | `theorem` | 2265 | Universal extension tower |
| `thm:bar-complex-spectral-sequence` | `theorem` | 2290 | Bar complex spectral sequence |
| `thm:essential-image-bar` | `theorem` | 2343 | Complete essential image characterization |
| `cor:recognition-principle` | `corollary` | 2396 | Recognition principle |
| `lem:deformation-space` | `lemma` | 2768 | Deformation space |
| `lem:obs-def-pairing` | `lemma` | 2810 | Obstruction-deformation pairing |
| `lem:center-cohomology` | `lemma` | 2858 | Center as obstruction-deformation space |
| `cor:curved-differential` | `corollary` | 2937 | Curved differential formula |

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
| `thm:FM-convergence` | `theorem` | 1649 | Convergence criterion |
| `lem:orientation-compatibility` | `lemma` | 1708 | Orientation compatibility |
| `prop:operadic-structure` | `proposition` | 1814 | Operadic structure |
| `thm:nbc-basis-optimality` | `theorem` | 1856 | NBC basis optimality |
| `prop:nbc-sparsity` | `proposition` | 1883 | NBC sparsity analysis |
| `thm:presentation-independence` | `theorem` | 1905 | Presentation independence |
| `lem:arnold-boundary` | `lemma` | 1945 | Arnold relations on boundary |
| `thm:permutohedral-cell-complex` | `theorem` | 1969 | Permutohedral cell complex |
| `thm:complexity-bounds` | `theorem` | 2004 | Complexity bounds |
| `thm:spectral-convergence` | `theorem` | 2026 | Spectral sequence convergence |
| `prop:residue-evaluation-complexity` | `proposition` | 2060 | Residue evaluation complexity |
| `thm:arnold-topological` | `theorem` | 2076 | Arnold relations: topological form |
| `cor:nilpotency-arnold-comprehensive` | `corollary` | 2098 | Nilpotency from Arnold relations |
| `thm:arnold-jacobi` | `theorem` | 2220 | Arnold relations = Jacobi identity |
| `thm:arnold-orlik-solomon` | `theorem` | 2273 | Arnold--Orlik--Solomon relations |
| `cor:bar-d-squared-zero` | `corollary` | 2319 | Bar differential squares to zero |
| `thm:normal-crossings-preservation` | `theorem` | 2351 | Normal crossings preservation |
| `lem:fiber-product-NC` | `lemma` | 2396 | Fiber product normal crossings |
| `thm:complete-coordinates` | `theorem` | 2627 | Complete coordinate description |
| `thm:normal-bundle-formula` | `theorem` | 2697 | Normal bundle formula |
| `thm:normal-crossings-verified` | `theorem` | 2834 | Normal crossings property |
| `__unlabeled_chapters/theory/configuration_spaces.tex:3044` | `computation` | 3044 | Explicit examples |

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

#### `chapters/theory/higher_genus_complementarity.tex` (67)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:involution-splitting` | `lemma` | 86 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 141 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 215 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 305 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 461 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 516 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 601 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 664 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 715 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 860 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 933 | Duality for bar complexes |
| `lem:ss-duality-complete` | `lemma` | 973 | Spectral sequence duality |
| `cor:quantum-dual-complete` | `corollary` | 1027 | Quantum corrections are dual |
| `thm:kodaira-spencer-chiral-complete` | `theorem` | 1056 | Kodaira--Spencer map for chiral algebras |
| `lem:verdier-involution-moduli` | `lemma` | 1244 | Verdier involution on moduli cohomology |
| `sublem:center-isomorphism` | `lemma` | 1279 | Center isomorphism via module Koszul duality |
| `lem:eigenspace-decomposition-complete` | `lemma` | 1331 | Eigenspace decomposition |
| `lem:obs-def-split-complete` | `lemma` | 1444 | Obstructions vs.\ deformations |
| `lem:trivial-intersection-complete` | `lemma` | 1475 | Trivial intersection |
| `lem:exhaustion-complete` | `lemma` | 1495 | Exhaustion property |
| `prop:lagrangian-eigenspaces` | `proposition` | 1561 | Verdier pairing and Lagrangian eigenspaces |
| `thm:shifted-symplectic-complementarity` | `theorem` | 1652 | Shifted symplectic complementarity |
| `prop:ptvv-lagrangian` | `proposition` | 1783 | PTVV Lagrangian embedding |
| `thm:ss-genus-stratification` | `theorem` | 1851 | Spectral sequence as genus stratification |
| `cor:modular-properties` | `corollary` | 1949 | Modular properties |
| `cor:uniqueness-quantum` | `corollary` | 1977 | Uniqueness of quantum corrections |
| `cor:vanishing-quantum` | `corollary` | 2014 | Vanishing results |
| `thm:self-dual-halving` | `theorem` | 2057 | Self-dual halving |
| `cor:virasoro-quantum-dim` | `corollary` | 2093 | Virasoro quantum corrections |
| `cor:critical-uncurving` | `corollary` | 2119 | Critical level uncurving |
| `thm:fermion-boson-koszul-hg` | `theorem` | 2374 | Fermion-boson Koszul duality |
| `thm:BD-genus-zero` | `theorem` | 2555 | BD 3.4.12 --- genus zero acyclicity |
| `prop:factorization-over-moduli` | `proposition` | 2605 | Factorization over moduli |
| `thm:normal-crossings-persist` | `theorem` | 2618 | Normal crossings persist at higher genus |
| `thm:CC-acyclicity-higher-genus` | `theorem` | 2660 | Chevalley--Cousin acyclicity at higher genus |
| `lem:relative-diagonal` | `lemma` | 2719 | Relative diagonal embedding |
| `prop:gluing-at-nodes` | `proposition` | 2761 | Gluing formula at nodes |
| `lem:boundary-compatible` | `lemma` | 2789 | Boundary compatibility |
| `cor:CC-at-boundary` | `corollary` | 2811 | Chevalley--Cousin at boundary |
| `thm:quantum-diff-squares-zero` | `theorem` | 2855 | Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0} |
| `lem:quantum-preserves-acyclicity` | `lemma` | 3028 | Quantum corrections preserve acyclicity |
| `lem:graded-acyclic` | `lemma` | 3076 | Graded piece acyclicity |
| `prop:DR-preserves-duality` | `proposition` | 3164 | DR preserves duality structures |
| `thm:verdier-AF-compat` | `theorem` | 3191 | Geometric-topological duality compatibility |
| `lem:verdier-dual-chiral` | `lemma` | 3219 | Verdier dual of chiral algebra |
| `lem:AF-dual-chiral` | `lemma` | 3253 | AF duality for chiral algebras |
| `prop:key-compat-DR` | `proposition` | 3278 | Key compatibility |
| `cor:bar-is-fh` | `corollary` | 3338 | Bar complex computes factorization cohomology |
| `lem:DR-verdier-compat` | `lemma` | 3384 | De Rham and Verdier duality |
| `lem:ran-duality-AF` | `lemma` | 3423 | Ran space duality |
| `lem:bar-as-fact-hom-AF` | `lemma` | 3452 | Bar as factorization homology |
| `lem:coalgebra-verdier-AF` | `lemma` | 3476 | Coalgebra from Verdier dual |
| `lem:diagram-commutes-AF` | `lemma` | 3501 | Diagram commutes |
| `lem:higher-genus-open-stratum-qi` | `lemma` | 3533 | Open-stratum quasi-isomorphism |
| `lem:higher-genus-boundary-qi` | `lemma` | 3565 | Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g} |
| `lem:extension-across-boundary-qi` | `lemma` | 3591 | Extension across boundary |
| `thm:higher-genus-inversion` | `theorem` | 3607 | Higher genus inversion |
| `lem:e2-collapse-higher-genus` | `lemma` | 3700 | \texorpdfstring{$E_2$}{E2} collapse at higher genus |
| `prop:pants-excision` | `proposition` | 3776 | Pants decomposition as excision |
| `prop:genus-induction-excision` | `proposition` | 3824 | Genus induction is iterated excision |
| `prop:e2-collapse-formality` | `proposition` | 3913 | \texorpdfstring{$E_2$}{E2}-collapse as formality |
| `thm:ambient-complementarity-tangent` | `theorem` | 4088 | Ambient complementarity in tangent form |
| `thm:shifted-cotangent-normal-form` | `theorem` | 4352 | Shifted cotangent normal form |
| `prop:legendre-duality-potentials` | `proposition` | 4401 | Legendre duality of the two potentials |
| `prop:legendre-duality-cubic` | `proposition` | 4416 | Legendre duality of cubic tensors |
| `thm:derived-critical-locus` | `theorem` | 4446 | Derived critical locus of self-dual deformations |
| `prop:fake-complementarity-criterion` | `proposition` | 4470 | Criterion for fake complementarity |

#### `chapters/theory/higher_genus_foundations.tex` (58)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-ainfty-complete` | `theorem` | 385 | \texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex |
| `thm:ainfty-moduli` | `theorem` | 485 | \texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces |
| `thm:pentagon-identity` | `theorem` | 576 | Pentagon identity |
| `thm:cobar-ainfty-complete` | `theorem` | 689 | Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:chain-vs-homology` | `theorem` | 796 | Chain-level vs.\ homology-level structure |
| `thm:verdier-duality-operations` | `theorem` | 943 | Verdier duality of operations |
| `thm:convergence-filtered` | `theorem` | 1142 | Convergence for filtered algebras |
| `prop:deforming-heisenberg` | `proposition` | 1351 | Deforming Heisenberg |
| `prop:betagamma-deformations` | `proposition` | 1385 | \texorpdfstring{$\beta\gamma$}{beta-gamma} deformations |
| `thm:jacobiator-lie-type` | `theorem` | 1419 | Jacobiator for Lie-type algebras |
| `thm:chiral-bianchi` | `theorem` | 1439 | Chiral Bianchi identity |
| `cor:higher-associahedron-m6` | `corollary` | 1455 | Higher associahedron identity for \texorpdfstring{$m_6$}{m6} |
| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 1757 | Bar-cobar isomorphism --- retained for equation labels |
| `cor:hochschild-duality` | `corollary` | 1842 | Hochschild cohomology duality |
| `thm:quantum-arnold-relations` | `theorem` | 2057 | Quantum-corrected Arnold relations |
| `cor:universal-arakelov` | `corollary` | 2325 | Universal Arakelov form |
| `thm:genus-differential` | `theorem` | 2519 | Genus-dependent differential |
| `thm:concrete-quantum-differential` | `theorem` | 2579 | Concrete quantum differential |
| `thm:eta-properties-genus1` | `theorem` | 2832 | Properties of \texorpdfstring{$\eta_{ij}^{(1)}$}{eta-ij(1)} |
| `thm:arnold-genus1` | `theorem` | 2891 | Genus-1 Arnold relation |
| `thm:genus1-d-squared` | `theorem` | 2926 | Nilpotency at genus 1 |
| `thm:genus1-universal-curvature` | `theorem` | 2983 | Universal genus-1 curvature via the modular characteristic |
| `thm:e1-page-complete` | `theorem` | 3251 | \texorpdfstring{$E_1$}{E1} page explicit |
| `thm:e2-page-complete` | `theorem` | 3284 | \texorpdfstring{$E_2$}{E2} page structure |
| `thm:obstruction-quantum` | `theorem` | 3411 | Obstruction theory for quantum corrections |
| `thm:obstruction-general` | `theorem` | 3512 | Obstruction formula |
| `thm:heisenberg-obs` | `theorem` | 3566 | Heisenberg obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:kac-moody-obs` | `theorem` | 3644 | Kac--Moody obstruction at genus \texorpdfstring{$g$}{g} |
| `thm:w3-obstruction` | `theorem` | 3761 | \texorpdfstring{$W_3$}{W3} obstruction with central charge |
| `comp:w3-obs-explicit` | `computation` | 3832 | Explicit genus-\texorpdfstring{$1$}{1} value of the \texorpdfstring{$W_3$}{W3} obstruction |
| `thm:obstruction-nilpotent` | `theorem` | 3853 | Nilpotence of obstruction (\texorpdfstring{$g \leq 2$}{g <= 2}) |
| `thm:obstruction-nilpotent-all-genera` | `theorem` | 3882 | Nilpotence of obstruction (all genera) |
| `cor:mumford-multiplicative` | `corollary` | 3967 | Mumford multiplicative relations for obstruction classes |
| `thm:genus-universality` | `theorem` | 4069 | Genus universality |
| `prop:multi-generator-obstruction` | `proposition` | 4223 | Multi-generator obstruction decomposition |
| `cor:anomaly-ratio` | `corollary` | 4256 | Anomaly ratio identity |
| `cor:kappa-periodicity` | `corollary` | 4272 | \texorpdfstring{$\kappa$}{kappa}-periodicity under level shift |
| `cor:kappa-additivity` | `corollary` | 4288 | Additivity of the obstruction coefficient |
| `cor:kappa-sum-wn` | `corollary` | 4306 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
| `cor:critical-level-universality` | `corollary` | 4329 | Critical level characterization |
| `cor:tautological-class-map` | `corollary` | 4351 | Tautological class map |
| `prop:bar-tautological-filtration` | `proposition` | 4384 | Bar spectral sequence and tautological filtration |
| `thm:koszul-k0` | `theorem` | 4456 | Grothendieck group of Koszul chiral algebras |
| `thm:obs-def-pairing-explicit` | `theorem` | 4486 | Obstruction-deformation pairing |
| `prop:obstruction-lifting` | `proposition` | 4572 | Obstruction lifting criterion |
| `prop:grr-bridge` | `proposition` | 4616 | Grothendieck--Riemann--Roch bridge |
| `lem:stable-graph-d-squared` | `lemma` | 4784 | $\partial_{\mathcal{G}}^2 = 0$ |
| `prop:loop-filtration-compatible` | `proposition` | 4846 | Filtration compatibility |
| `thm:loop-order-spectral-sequence` | `theorem` | 4884 | Loop order spectral sequence |
| `prop:extremal-pages` | `proposition` | 4926 | Extremal pages |
| `thm:curvature-self-contraction` | `theorem` | 5015 | Curvature from loop contraction |
| `cor:anomaly-trace-standard` | `corollary` | 5103 | Anomaly = trace for standard families |
| `thm:loop-order-collapse` | `theorem` | 5171 | Loop order collapse |
| `cor:loop-decomposition-bar` | `corollary` | 5205 | Loop order decomposition of bar cohomology |
| `cor:feynman-duality-qch` | `corollary` | 5246 | Duality of quantum chiral homology |
| `thm:virtual-euler-char` | `theorem` | 5303 | Graph-sum formula for the virtual Euler characteristic |
| `cor:heisenberg-euler-char` | `corollary` | 5331 | Heisenberg Euler characteristic |
| `prop:weight-system-map` | `proposition` | 5381 | Weight system map |

#### `chapters/theory/higher_genus_modular_koszul.tex` (72)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:genus-graded-koszul` | `theorem` | 55 | Genus-graded Koszul duality |
| `lem:genus-graded-koszul-resolution` | `lemma` | 86 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 418 | Standard examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 451 | Interacting examples are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 492 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 628 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 895 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 920 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1117 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1169 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1269 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1319 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1381 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `thm:genus-internalization` | `theorem` | 1658 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 1765 | Modular characteristic |
| `thm:spectral-characteristic` | `theorem` | 1871 | Spectral characteristic theorem |
| `thm:universal-theta` | `theorem` | 1900 | Universal modular Maurer--Cartan class |
| `thm:explicit-theta` | `theorem` | 2025 | Explicit universal MC class |
| `cor:explicit-theta-specializations` | `corollary` | 2241 | Explicit modular package for all families |
| `prop:genus-completed-mc-framework` | `proposition` | 2655 | Genus-completed MC framework |
| `prop:cyclic-ce-identification` | `proposition` | 2734 | Cyclic CE cohomology identification |
| `cor:one-dim-obstruction` | `corollary` | 2847 | One-dimensional obstruction space |
| `prop:mc2-reduction-principle` | `proposition` | 2881 | MC2 reduction principle |
| `prop:geometric-modular-operadic-mc` | `proposition` | 2913 | Geometric modular-operadic MC framework |
| `prop:tautological-line-support-criterion` | `proposition` | 3109 | Tautological-line support criterion |
| `prop:one-channel-verdier-criterion` | `proposition` | 3185 | One-channel Verdier/Koszul criterion |
| `prop:one-channel-ptvv-criterion` | `proposition` | 3250 | One-channel PTVV / anti-involution criterion |
| `prop:one-channel-chain-model-criterion` | `proposition` | 3385 | One-channel chain-model criterion |
| `prop:one-channel-seed-criterion` | `proposition` | 3482 | One-channel bar-coderivation seed criterion |
| `prop:one-channel-minimal-seed-packet-criterion` | `proposition` | 3593 | One-channel minimal seed-packet criterion |
| `prop:one-channel-visible-lowarity-packet-criterion` | `proposition` | 3730 | One-channel visible low-arity seed-packet criterion |
| `prop:one-channel-canonical-transfer-criterion` | `proposition` | 3882 | One-channel canonical transfer-package criterion |
| `prop:one-channel-transfer-law-criterion` | `proposition` | 4056 | One-channel root-string transfer-law criterion |
| `prop:one-channel-root-string-chart-criterion` | `proposition` | 4206 | One-channel root-string chart criterion |
| `prop:one-channel-intrinsic-line-detection-criterion` | `proposition` | 4400 | One-channel intrinsic line-detection criterion |
| `prop:one-channel-automorphism-rigidity-criterion` | `proposition` | 4520 | One-channel automorphism-rigidity criterion |
| `prop:one-channel-support-graph-stabilizer-criterion` | `proposition` | 4619 | One-channel support-graph stabilizer criterion |
| `prop:one-channel-incidence-orbit-criterion` | `proposition` | 4709 | One-channel incidence-matrix / orbit-count criterion |
| `prop:one-channel-visible-orbit-table-criterion` | `proposition` | 4821 | One-channel visible root-string orbit-table criterion |
| `prop:one-channel-canonical-universal-orbit-table-criterion` | `proposition` | 4893 | One-channel canonical universal orbit-table criterion |
| `prop:one-channel-universal-invariant-signature-criterion` | `proposition` | 4975 | One-channel universal invariant-signature criterion |
| `prop:one-channel-signed-seed-character-criterion` | `proposition` | 5053 | One-channel signed seed-character criterion |
| `prop:one-channel-two-sign-plus-normalization-scalar-criterion` | `proposition` | 5130 | One-channel two-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-sign-plus-normalization-scalar-criterion` | `proposition` | 5206 | One-channel parity-sign plus normalization-scalar criterion |
| `prop:one-channel-parity-forcing-criterion` | `proposition` | 5281 | One-channel parity-forcing criterion |
| `prop:one-channel-normalization-criterion` | `proposition` | 5347 | One-channel normalization criterion |
| `thm:mc2-conditional-completion` | `theorem` | 5425 | MC2 conditional completion |
| `thm:mc2-full-resolution` | `theorem` | 5500 | MC2 full resolution |
| `lem:mk67-from-mc2` | `lemma` | 5547 | MC2 full resolution identifies MK6--MK7 |
| `cor:scalar-saturation` | `corollary` | 5589 | Scalar saturation of the universal MC class |
| `thm:km-strictification` | `theorem` | 5645 | KM strictification of the universal class |
| `prop:one-channel-gauge-rigidity` | `proposition` | 5699 | One-channel gauge rigidity |
| `prop:w-algebra-scalar-saturation` | `proposition` | 5732 | Scalar saturation for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `cor:winfty-scalar-saturation` | `corollary` | 5770 | Scalar saturation persists in the \texorpdfstring{$\mathcal{W}_\infty$}{W-infinity} limit |
| `prop:ds-package-functoriality` | `proposition` | 5823 | DS functoriality of the characteristic package |
| `prop:nonprincipal-scalar-saturation` | `proposition` | 5895 | Scalar saturation for non-principal \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:saturation-equivalence` | `proposition` | 5970 | Saturation equivalence criterion |
| `prop:saturation-functorial` | `proposition` | 6137 | Functorial stability of scalar saturation |
| `cor:effective-quadruple` | `corollary` | 6300 | Effective quadruple for the standard landscape |
| `thm:cyclic-rigidity-generic` | `theorem` | 6383 | Cyclic rigidity at generic level |
| `thm:tautological-line-support` | `theorem` | 6668 | Tautological line support |
| `cor:mc2-single-hypothesis` | `corollary` | 6770 | MC2 reduced to cyclic model |
| `thm:convolution-dg-lie-structure` | `theorem` | 6911 | dg~Lie structure from the modular operad |
| `thm:modular-quantum-linfty` | `theorem` | 6976 | Full homotopy upgrade: quantum $L_\infty$ structure |
| `thm:modular-homotopy-convolution` | `theorem` | 7122 | Modular homotopy convolution |
| `cor:strictification-comparison` | `corollary` | 7147 | Strictification comparison |
| `thm:theta-direct-derivation` | `theorem` | 7262 | The explicit formula: direct derivation |
| `prop:chriss-ginzburg-structure` | `proposition` | 7438 | Chriss--Ginzburg structure principle |
| `rem:coefficient-algebras-well-defined` | `proposition` | 7608 | Square-zero property of the ambient differential |
| `thm:convolution-d-squared-zero` | `theorem` | 7645 | Square-zero: convolution level |
| `prop:master-equation-from-mc` | `proposition` | 7746 | All-arity master equation from MC |
| `prop:critical-locus-complementarity` | `proposition` | 7833 | Critical-locus form of complementarity |

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
| `thm:central-charge-complementarity` | `theorem` | 396 | Central charge complementarity |
| `prop:chirAss-self-dual` | `proposition` | 1036 | \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |

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
| `thm:bv-structure-bar` | `theorem` | 1641 | BV structure on bar complex |

#### `chapters/theory/poincare_duality.tex` (8)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:dual-differentials` | `theorem` | 176 | Dual differentials |
| `thm:coalgebra-via-NAP` | `theorem` | 288 | Coalgebra structure via NAP |
| `thm:bar-computes-dual` | `theorem` | 355 | Bar construction = Verdier dual via NAP |
| `comp:bar-dual-low-degrees` | `computation` | 446 | Degree 0 and 1 |
| `prop:koszul-pair-NAP` | `proposition` | 505 | Chiral Koszul pair via NAP |
| `thm:symmetric-koszul` | `theorem` | 521 | Symmetric Koszul duality |
| `thm:completion-koszul` | `theorem` | 612 | Completion and Koszul duality |
| `thm:main-NAP-resolution` | `theorem` | 696 | Resolution of circularity |

#### `chapters/theory/poincare_duality_quantum.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:chiral-operad-genus0` | `proposition` | 288 | Genus-zero identification |
| `thm:prism-operadic` | `theorem` | 332 | Prism principle --- operadic identification |
| `thm:prism-higher-genus` | `theorem` | 541 | Prism principle --- higher-genus extension |
| `cor:prism-principle` | `corollary` | 648 | The prism principle |
| `thm:partition` | `theorem` | 799 | Partition complex structure |

### Part II: Examples (428)

#### `chapters/examples/bar_complex_tables.tex` (25)

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

#### `chapters/examples/beta_gamma.tex` (22)

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
| `thm:betagamma-quartic-birth` | `theorem` | 1680 | \texorpdfstring{$\beta\gamma$}{beta-gamma} quartic birth |
| `lem:betagamma-ell2-vanishing` | `lemma` | 1793 | $\ell_2^{\mathrm{tr}}(\eta,\eta) = 0$ |
| `prop:betagamma-ell3-vanishing` | `proposition` | 1840 | $\ell_3^{\mathrm{tr}}(\eta,\eta,\eta) = 0$ |
| `cor:betagamma-mu-vanishing` | `corollary` | 1939 | Vanishing of the quartic contact invariant |
| `thm:betagamma-rank-one-rigidity` | `theorem` | 1981 | Rank-one abelian rigidity |
| `cor:betagamma-pure-contact-boundary` | `corollary` | 2011 | Pure contact boundary law |
| `prop:betagamma-translation-coproduct` | `proposition` | 2120 | Translation and coproduct |

#### `chapters/examples/deformation_quantization.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:chiral-quantization` | `theorem` | 102 | Coisson quantization at genus \texorpdfstring{$0$}{0} |
| `thm:chiral-kontsevich` | `theorem` | 155 | Chiral Kontsevich formula |
| `prop:mc-star-product` | `proposition` | 387 | MC \texorpdfstring{$\Leftrightarrow$}{iff} star product |
| `thm:deformation-genus-expansion` | `theorem` | 500 | Genus expansion |

#### `chapters/examples/deformation_quantization_examples.tex` (2)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:lattice-one-step` | `proposition` | 422 | Lattice deformation is one-step |
| `thm:dq-koszul-compatible` | `theorem` | 494 | Deformation--duality compatibility |

#### `chapters/examples/free_fields.tex` (47)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:single-fermion-boson-duality` | `theorem` | 77 | Single-generator fermion-boson duality |
| `thm:fermion-bar-complex-genus-0` | `theorem` | 129 | Free fermion bar complex at genus 0 |
| `thm:fermion-bar-coalg` | `theorem` | 185 | Fermion bar complex coalgebra |
| `thm:betagamma-bar-complex` | `theorem` | 236 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex |
| `thm:betagamma-bar-dim` | `theorem` | 247 | \texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank |
| `thm:heisenberg-bar` | `theorem` | 319 | Heisenberg bar complex at genus 0 |
| `lem:orientation-freefields` | `lemma` | 342 | Orientation consistency |
| `thm:heisenberg-curved-structure` | `theorem` | 384 | Heisenberg curved structure |
| `thm:lattice-voa-bar` | `theorem` | 431 | Lattice VOA bar complex |
| `prop:A2-lattice-bar` | `proposition` | 460 | \texorpdfstring{$A_2$}{A2} lattice computation |
| `thm:elliptic-fermion-bar` | `theorem` | 490 | Elliptic free fermion bar complex |
| `thm:heisenberg-higher-genus` | `theorem` | 527 | Higher genus Heisenberg |
| `prop:bc-betagamma-orthogonality` | `proposition` | 572 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} orthogonality |
| `thm:betagamma-bc-koszul` | `theorem` | 596 | \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} Koszul duality |
| `prop:bg-bc-module-kd` | `proposition` | 811 | Module Koszul duality for \texorpdfstring{$\beta\gamma$}{beta-gamma}--\texorpdfstring{$bc$}{bc} |
| `thm:heisenberg-koszul-dual-early` | `theorem` | 887 | Heisenberg Koszul dual |
| `cor:heisenberg-module-equivalence` | `corollary` | 919 | Heisenberg module-comodule equivalence |
| `prop:fock-bar-resolution` | `proposition` | 1054 | Fock module bar resolution |
| `prop:fock-koszul-dual` | `proposition` | 1109 | Koszul dual module |
| `cor:fock-character-koszul` | `corollary` | 1159 | Fock module character from Koszul resolution |
| `prop:fock-ext` | `proposition` | 1201 | Ext groups between Fock modules |
| `prop:twisted-fermion-kd` | `proposition` | 1354 | Twisted module Koszul duality for fermions |
| `prop:spectral-flow-kd` | `proposition` | 1430 | Spectral flow under Koszul duality |
| `thm:heisenberg-not-self-dual` | `theorem` | 1596 | Heisenberg is not self-dual |
| `prop:bar-bv-free-fields` | `proposition` | 1701 | Bar complex as BV complex |
| `thm:heisenberg-genus-g` | `theorem` | 1732 | Quantum complementarity for Heisenberg |
| `prop:abelian-bar-factorization` | `proposition` | 1991 | Abelian factorization of the bar differential |
| `prop:nonabelian-kernel-nonfactorization` | `proposition` | 2105 | Non-abelian kernel non-factorization |
| `prop:en-fourier-hierarchy` | `proposition` | 2368 | \texorpdfstring{$\En$}{En} Fourier hierarchy |
| `thm:heisenberg-bar-complete` | `theorem` | 2517 | Heisenberg bar complex: complete calculation |
| `lem:bar-dims-partitions` | `lemma` | 2564 | Bar dimensions as partition numbers |
| `thm:heisenberg-level-inversion` | `theorem` | 2623 | Heisenberg level inversion: curved duality |
| `thm:virasoro-moduli` | `theorem` | 2683 | Virasoro-moduli correspondence |
| `prop:moduli-degeneration` | `proposition` | 2721 | Geometric interpretation |
| `thm:virasoro-string` | `theorem` | 2800 | Virasoro-string duality |
| `thm:algebraic-string-dictionary` | `theorem` | 2836 | Algebraic string theory dictionary |
| `cor:string-amplitude-genus0` | `corollary` | 2888 | Genus-\texorpdfstring{$0$}{0} string amplitudes from bar complex |
| `thm:genus-g-chiral-homology` | `theorem` | 2930 | Genus-\texorpdfstring{$g$}{g} chiral homology from bar complex |
| `thm:genus-deformation-exact` | `theorem` | 3039 | Genus expansion as curved deformation |
| `thm:bar-string-integrand` | `theorem` | 3119 | Bar complex computes genus-\texorpdfstring{$g$}{g} string integrands |
| `thm:modular-invariance` | `theorem` | 3257 | Modular invariance of bar complex |
| `thm:modular-anomaly-km-w` | `theorem` | 3294 | Modular anomaly for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:wakimoto-bar` | `theorem` | 3403 | Wakimoto bar complex |
| `prop:wakimoto-graph` | `proposition` | 3416 | Graphical interpretation |
| `thm:w-algebra-ainfty` | `theorem` | 3421 | \texorpdfstring{$A_\infty$}{A-infinity} structure on \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-integrability` | `theorem` | 3448 | Quantum integrability via \texorpdfstring{$A_\infty$}{A-infinity} |
| `thm:filtered-bar-complex` | `theorem` | 3508 | Filtered bar complex |

#### `chapters/examples/genus_expansions.tex` (35)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-all-genera` | `theorem` | 16 | Heisenberg free energy at all genera |
| `prop:betagamma-all-genera` | `proposition` | 64 | \texorpdfstring{$\beta\gamma$}{beta-gamma} genus expansion |
| `thm:lattice-all-genera` | `theorem` | 108 | Lattice VOA free energy |
| `cor:lattice-rank-only` | `corollary` | 143 | Lattice-independence of genus expansion |
| `thm:w-algebra-all-genera` | `theorem` | 165 | \texorpdfstring{$\mathcal{W}$}{W}-algebra free energy at all genera |
| `thm:sl2-all-genera` | `theorem` | 358 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} free energy at all genera |
| `prop:sl2-complementarity-all-genera` | `proposition` | 504 | \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl2-hat} complementarity |
| `prop:bivariate-gf` | `proposition` | 636 | Bivariate generating function |
| `prop:km-genus2-propagator` | `proposition` | 678 | Non-abelian genus-2 propagator |
| `thm:sl2-genus2-bar-differential` | `theorem` | 732 | Genus-2 bar differential for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:sl2-genus2-curvature` | `theorem` | 843 | Genus-2 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `prop:sl2-genus2-relation` | `proposition` | 953 | Genus-2 relation for \texorpdfstring{$\widehat{\mathfrak{sl}}_2$}{sl-hat_2} |
| `thm:virasoro-genus2-bar` | `theorem` | 1093 | Genus-2 bar differential for \texorpdfstring{$\mathrm{Vir}_c$}{Vir_c} |
| `cor:virasoro-genus2-curvature` | `corollary` | 1160 | Genus-2 Virasoro curvature |
| `prop:w3-genus2-curvature` | `proposition` | 1225 | \texorpdfstring{$\mathcal{W}_3$}{W_3} genus-2 curvature |
| `comp:genus2-complementarity-table` | `computation` | 1311 | Genus-2 complementarity dimensions |
| `prop:genus-expansion-convergence` | `proposition` | 1443 | Convergence of the genus expansion |
| `thm:bernoulli-universality` | `theorem` | 1473 | Bernoulli universality |
| `prop:complementarity-genus-series` | `proposition` | 1490 | Central charge genus series |
| `thm:universal-generating-function` | `theorem` | 1525 | Universal generating function |
| `prop:bar-verlinde-asymptotics` | `proposition` | 1596 | Bar free energy and Verlinde asymptotics |
| `thm:vir-all-genera` | `theorem` | 1724 | Virasoro free energy |
| `prop:vir-complementarity` | `proposition` | 1766 | Virasoro complementarity |
| `prop:sl3-complementarity-all-genera` | `proposition` | 1845 | \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl3-hat} complementarity |
| `thm:fermion-all-genera` | `theorem` | 1994 | Free fermion free energy at all genera |
| `prop:fermion-complementarity` | `proposition` | 2059 | \texorpdfstring{$bc$}{bc}--\texorpdfstring{$\beta\gamma$}{beta-gamma} complementarity |
| `prop:complementarity-classification` | `proposition` | 2292 | Classification of complementarity types |
| `thm:complementarity-root-datum` | `theorem` | 2346 | Complementarity sum as root datum invariant |
| `prop:universal-growth-rate` | `proposition` | 2640 | Universal growth rate |
| `prop:multiplicative-genus` | `proposition` | 2740 | Koszul duality determines a multiplicative genus |
| `cor:complementary-genera` | `corollary` | 2756 | Koszul complementarity of genera |
| `prop:koszul-genus-involution` | `proposition` | 2781 | Koszul duality as genus involution |
| `thm:genus-determines-pair` | `theorem` | 2813 | Genus duality determines the Koszul pair |
| `prop:loop-expansion-knots` | `proposition` | 2908 | Loop expansion interpretation |
| `thm:boundary-characters-bar-hilbert` | `theorem` | 3079 | Boundary characters as bar Hilbert series |

#### `chapters/examples/heisenberg_eisenstein.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:heisenberg-genus-one-complete` | `theorem` | 116 | Complete genus-1 Heisenberg correlators |
| `thm:heisenberg-genus-two` | `theorem` | 203 | Genus-2 Heisenberg correlators |
| `thm:heisenberg-genus2-obstruction` | `theorem` | 245 | Genus-2 obstruction class for \texorpdfstring{$\mathcal{H}_\kappa$}{H_kappa} |
| `thm:heisenberg-all-genus` | `theorem` | 363 | Heisenberg at general genus |
| `thm:eta-appearance` | `theorem` | 466 | Partition function and determinant regularization |
| `thm:dmvv-agreement` | `theorem` | 515 | Agreement with Dijkgraaf--Moore--Verlinde--Verlinde |
| `prop:multi-boson-eisenstein` | `proposition` | 727 | Multi-boson Eisenstein corrections |
| `thm:heisenberg-exact-linearity` | `theorem` | 977 | Heisenberg exact linearity |
| `cor:heisenberg-gaussian-boundary` | `corollary` | 1219 | Gaussian boundary law |

#### `chapters/examples/kac_moody.tex` (42)

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
| `thm:affine-cubic-normal-form` | `theorem` | 2948 | Affine cubic normal form |
| `prop:affine-cyclic-slice-data` | `proposition` | 2993 | Affine cyclic slice data |
| `prop:affine-cubic-ad-invariance` | `proposition` | 3041 | Cubic shadow via ad-invariance |
| `prop:affine-jacobi-quartic-vanishing` | `proposition` | 3098 | Jacobi mechanism for quartic vanishing |
| `prop:affine-sl2-boundary-quartic` | `proposition` | 3175 | Explicit boundary quartic for $\mathfrak{sl}_2$ |
| `prop:affine-sl2-genus-loop` | `proposition` | 3261 | Genus loop for $\mathfrak{sl}_2$ |
| `cor:affine-boundary-quartic` | `corollary` | 3297 | Boundary-generated quartic nonlinearity |
| `thm:affine-genus-loop-weyl` | `theorem` | 3386 | Vanishing of the genus loop on the affine cubic |

#### `chapters/examples/landscape_census.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:paired-standard-mc4-frontier` | `proposition` | 192 | Paired standard-tower MC4 frontier packets |
| `cor:paired-standard-mc4-closure` | `corollary` | 391 | Minimal closure conditions for the standard-tower MC4 frontier |
| `cor:genus1-anomaly-ratio` | `corollary` | 521 | Genus-\texorpdfstring{$1$}{1} free energy and anomaly ratio |
| `prop:bar-dimensions` | `proposition` | 728 | Koszul dual Hilbert functions |
| `cor:subexp-free-field` | `corollary` | 960 | Sub-exponential growth characterizes free fields |
| `cor:algebraicity-koszul` | `corollary` | 970 | Algebraicity of bar generating functions for interacting algebras |
| `thm:ds-bar-gf-discriminant` | `theorem` | 987 | DS reduction and bar cohomology generating functions |
| `thm:ds-spectral-branch-preservation` | `theorem` | 1146 | DS preservation of the sub-discriminant |
| `prop:hred-sl2` | `proposition` | 1329 | Construction of \texorpdfstring{$H^{\mathrm{red}}_1$}{Hred_1} for \texorpdfstring{$\mathfrak{sl}_2$}{sl_2} |
| `prop:discriminant-characteristic` | `proposition` | 1529 | Discriminant as first characteristic invariant |
| `thm:discriminant-linear-dependence` | `theorem` | 1620 | Linear dependence in the discriminant family |
| `prop:linear-relation-functorial` | `proposition` | 1717 | Functorial origin of the linear relation |
| `prop:pole-singularity-type` | `proposition` | 1783 | Pole decomposition and singularity type |
| `lem:bar-deg2-symmetric-square` | `lemma` | 1838 | Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight |
| `cor:growth-rate-dimg` | `corollary` | 1889 | Exponential growth rate from Lie algebra dimension |
| `thm:dominant-branch-point` | `theorem` | 1904 | Dominant branch point for Kac--Moody algebras |
| `thm:motzkin-path-model` | `theorem` | 1993 | Motzkin path model for Virasoro bar cohomology |
| `cor:betagamma-inverse-discriminant` | `corollary` | 2182 | {\texorpdfstring{$\beta\gamma$}{beta-gamma} generating function via discriminant} |
| `prop:spectral-collapse-summary` | `proposition` | 2488 | Spectral sequence collapse |

#### `chapters/examples/lattice_foundations.tex` (34)

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
| `prop:lattice:genus1-simple-pole` | `proposition` | 4048 | Simple-pole residues unchanged at genus~$1$ |
| `thm:lattice:curvature-braiding-orthogonal` | `theorem` | 4065 | Curvature-braiding orthogonality for quantum lattice VOAs |

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
| `comp:s-matrix-5-4` | `computation` | 406 | S-matrix for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:fusion-5-4` | `computation` | 431 | Fusion rules for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |
| `comp:m65-primaries` | `computation` | 510 | \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} primary fields |
| `comp:fusion-phi12-6-5` | `computation` | 537 | Fusion rules for \texorpdfstring{$\Phi_{1,2}$}{_1,2} in \texorpdfstring{$\mathcal{M}(6,5)$}{M(6,5)} |
| `thm:fusion-ring-generators` | `theorem` | 597 | Generators of the fusion ring |
| `prop:fusion-ring-p-2` | `proposition` | 617 | Fusion ring for \texorpdfstring{$\mathcal{M}(p,2)$}{M(p,2)} |
| `thm:fusion-ring-quotient` | `theorem` | 644 | Fusion ring as polynomial quotient |
| `comp:twist-5-4` | `computation` | 740 | Twist values for \texorpdfstring{$\mathcal{M}(5,4)$}{M(5,4)} |

#### `chapters/examples/toroidal_elliptic.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fay-implies-d-squared` | `proposition` | 345 | Fay identity implies elliptic \texorpdfstring{$d^2 = 0$}{d2 = 0} |
| `thm:elliptic-vs-rational` | `theorem` | 443 | Elliptic vs rational homology |
| `prop:ell-bar-decomposition` | `proposition` | 815 | Decomposition of the elliptic bar complex |
| `prop:dybe-reduces-to-fay` | `proposition` | 1011 | DYBE reduces to Fay |
| `prop:dybe-bar-nilpotency` | `proposition` | 1089 | DYBE and bar nilpotency |

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

#### `chapters/examples/w_algebras.tex` (32)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-algebra-koszul-main` | `theorem` | 55 | \texorpdfstring{$\mathcal{W}$}{W}-algebra Koszul duality for principal nilpotent |
| `prop:bp-duality` | `proposition` | 240 | Subregular \texorpdfstring{$\mathcal{W}$}{W}-algebra duality for \texorpdfstring{$\mathfrak{sl}_3$}{sl_3} |
| `thm:w-geometric-ope` | `theorem` | 548 | Geometric OPE formula for \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:w-bar-curvature` | `theorem` | 619 | Curvature of \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} structure |
| `thm:w-critical-bar` | `theorem` | 659 | Bar complex at critical level |
| `thm:w-koszul-precise` | `theorem` | 696 | Koszul duality for \texorpdfstring{$\mathcal{W}$}{W}-algebras --- precise statement |
| `thm:virasoro-self-duality` | `theorem` | 822 | Virasoro self-duality at \texorpdfstring{$c=0$}{c=0} |
| `thm:vir-genus1-curvature` | `theorem` | 948 | Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-inversion` | `theorem` | 999 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:vir-genus1-complementarity` | `theorem` | 1063 | Genus-1 complementarity for \texorpdfstring{$\mathrm{Vir}_c$}{Virc} |
| `thm:w3-koszul-dual` | `theorem` | 1232 | Koszul dual of \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-curvature` | `theorem` | 1313 | Genus-1 curvature for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-inversion` | `theorem` | 1379 | Genus-1 bar-cobar inversion for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:w3-genus1-complementarity` | `theorem` | 1449 | Genus-1 complementarity for \texorpdfstring{$\mathcal{W}_3$}{W3} |
| `thm:wn-obstruction` | `theorem` | 1544 | Obstruction coefficient for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:wn-complementarity` | `corollary` | 1640 | Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN} |
| `cor:general-w-obstruction` | `corollary` | 1661 | Obstruction coefficient for general \texorpdfstring{$\mathcal{W}(\mathfrak{g})$}{W(g)} |
| `thm:w-center-langlands` | `theorem` | 1750 | \texorpdfstring{$\mathcal{W}$}{W}-algebra centers and Langlands duality |
| `thm:w-ainfty-ops` | `theorem` | 1855 | \texorpdfstring{$\mathcal{W}$}{W}-algebra \texorpdfstring{$A_\infty$}{A-infinity} operations |
| `thm:w-universal-gravitational-cubic` | `theorem` | 2601 | Universal gravitational cubic tensor |
| `thm:w-virasoro-mixed-shadow` | `theorem` | 2656 | Virasoro mixed shadow |
| `thm:w-virasoro-quartic-explicit` | `theorem` | 2693 | Explicit Virasoro quartic contact coefficient |
| `prop:w-virasoro-lee-yang-degeneration` | `proposition` | 2780 | Lee--Yang degeneration of the quartic shadow |
| `thm:w-w3-mixed-shadow` | `theorem` | 2860 | $\mathcal{W}_3$ mixed-shadow normal form |
| `prop:w-w3-weight6-resonance` | `proposition` | 2942 | Weight-$6$ Gram determinant and visible resonance divisor |
| `thm:w-principal-wn-hessian-cubic` | `theorem` | 3013 | Diagonal Hessian and universal cubic for principal $\mathcal{W}_N$ |
| `thm:w-principal-wn-contact-nonvanishing` | `theorem` | 3039 | Nonvanishing of contact quartics for $\mathcal{W}_N$ |
| `thm:w-archetype-trichotomy` | `theorem` | 3072 | Archetype trichotomy |
| `thm:w-virasoro-quintic-forced` | `theorem` | 3138 | Virasoro quintic forced |
| `thm:w-finite-termination` | `theorem` | 3183 | Finite termination for primitive archetypes |
| `thm:w-virasoro-genus1-hessian` | `theorem` | 3237 | Genus-$1$ Hessian correction for Virasoro |
| `prop:w-w3-quintic-obstruction` | `proposition` | 3404 | $\mathcal{W}_3$ quintic obstruction |

#### `chapters/examples/w_algebras_deep.tex` (4)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:w-bar-coalg` | `theorem` | 89 | \texorpdfstring{$\mathcal{W}$}{W}-algebra bar coalgebra |
| `thm:winfty-factorization-kd` | `theorem` | 782 | Factorization Koszul dual of \texorpdfstring{$\mathcal{W}_\infty$}{W_infinity} via DS--sectorwise convergence |
| `prop:w3-deg3-vacuum` | `proposition` | 1291 | \texorpdfstring{$\mathcal{W}_3$}{W_3} degree-3 vacuum cancellation |
| `prop:ds-koszul-hierarchy` | `proposition` | 1501 | DS hierarchy and Koszul duality |

#### `chapters/examples/yangians_computations.tex` (29)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:yangian-rank-dependence` | `proposition` | 496 | Rank dependence of Yangian bar complex |
| `prop:eval-module-bar` | `proposition` | 633 | Evaluation module bar complex |
| `thm:yangian-bgg` | `theorem` | 722 | Yangian BGG resolution |
| `cor:yangian-ext-exchange` | `corollary` | 778 | Ext exchange for Yangian modules |
| `prop:yangian-dk2-thick-generation` | `proposition` | 828 | DK-2 reduction to thick generation in category~\texorpdfstring{$\mathcal{O}$}{O} |
| `prop:dk2-thick-generation-typeA` | `proposition` | 880 | Thick generation by evaluation modules in type~\texorpdfstring{$A$}{A} |
| `lem:composition-thick-generation` | `lemma` | 974 | Thick generation from finite composition series |
| `thm:catO-thick-generation` | `theorem` | 1005 | Thick generation of category~\texorpdfstring{$\mathcal{O}$}{O} by evaluation modules, type~\texorpdfstring{$A$}{A} |
| `prop:bar-cobar-kazhdan-candidate` | `proposition` | 1089 | Bar-cobar as factorization Kazhdan candidate |
| `lem:monoidal-thick-extension` | `lemma` | 1191 | Monoidal extension to thick closures |
| `thm:dk-fd-typeA` | `theorem` | 1213 | Finite-dimensional factorization Drinfeld--Kohno, type~\texorpdfstring{$A$}{A} |
| `cor:dk-partial-conj` | `corollary` | 1288 | Partial resolution of Conjecture~\textup{\ref{conj:full-derived-dk}} |
| `cor:dk-poly-catO` | `corollary` | 1307 | Factorization DK for polynomial category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A} |
| `lem:fd-thick-closure` | `lemma` | 1379 | Finite-dimensional thick-closure constraint |
| `prop:yangian-bar-loop-weight` | `proposition` | 1465 | Loop-weight filtration of the Yangian bar complex |
| `prop:thick-gen-projective` | `proposition` | 1716 | Thick generation via projective resolutions |
| `prop:bgg-criterion` | `proposition` | 1846 | BGG resolution criterion for thick generation |
| `prop:heart-capture-criterion` | `proposition` | 2004 | Heart-capture criterion |
| `prop:standard-capture-criterion` | `proposition` | 2024 | Standard-capture criterion |
| `cor:sectorwise-localizing-generation` | `corollary` | 2049 | Sectorwise localizing generation |
| `thm:eval-core-identification` | `theorem` | 2222 | Evaluation-generated core identification, type~\texorpdfstring{$A$}{A} |
| `thm:baxter-exact-triangles-opoly` | `theorem` | 2284 | Baxter exact triangles on \texorpdfstring{$\mathcal{O}_{\mathrm{poly}}$}{Opoly} |
| `prop:baxter-yangian-equivariance` | `proposition` | 2366 | Yangian equivariance of the Baxter singular vector |
| `cor:baxter-naturality-opoly` | `corollary` | 2440 | Naturality on $\mathcal{O}_{\mathrm{poly}}$ |
| `thm:shifted-prefundamental-generation` | `theorem` | 2485 | $E_1$-chiral thick generation for $Y(\mathfrak{sl}_N)$ |
| `prop:prefundamental-clebsch-gordan` | `proposition` | 2709 | Prefundamental Clebsch--Gordan |
| `cor:universal-character-containment` | `corollary` | 2734 | Universal character containment |
| `cor:k0-generation-OY` | `corollary` | 2748 | $K_0$ generation of $\mathcal{O}_Y$ |
| `thm:mc3-type-a-resolution` | `theorem` | 3041 | MC3 resolution in type $A$ |

#### `chapters/examples/yangians_drinfeld_kohno.tex` (68)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:derived-dk-affine` | `theorem` | 76 | Chain-level derived Drinfeld--Kohno for affine algebras |
| `thm:derived-dk-yangian` | `theorem` | 175 | Derived Drinfeld--Kohno on the evaluation-generated subcategory |
| `thm:factorization-dk-eval` | `theorem` | 340 | Factorization DK on evaluation locus |
| `prop:yangian-dk3-generated-core` | `proposition` | 419 | DK-3 reduction to evaluation-generated factorization cores |
| `thm:sectorwise-spectral-convergence` | `theorem` | 534 | Sectorwise spectral convergence |
| `thm:h-level-factorization-kd` | `theorem` | 583 | \texorpdfstring{$\infty$}{infinity}-categorical factorization Koszul duality via sectorwise convergence |
| `cor:dk23-all-types` | `corollary` | 720 | DK-2/3 for all simple types via sectorwise convergence |
| `prop:yangian-canonical-hlevel-target` | `proposition` | 908 | Canonical Yangian H-level dg target from factorization formal moduli |
| `prop:yangian-canonical-envelope` | `proposition` | 949 | Canonical associative dg model of the Yangian formal-moduli target |
| `thm:factorization-positselski` | `theorem` | 1219 | Factorization Positselski equivalence |
| `thm:ind-completed-extension` | `theorem` | 1340 | Ind-completed factorization DK equivalence |
| `prop:finite-stage-tangent` | `proposition` | 1542 | Finite-stage tangent Lie algebras |
| `thm:rtt-mittag-leffler` | `theorem` | 1649 | Mittag-Leffler for the RTT bar cohomology tower |
| `cor:completed-bar-cobar-yangian` | `corollary` | 1747 | Completed bar-cobar equivalence for Yangians |
| `prop:dg-shifted-quotient-criterion` | `proposition` | 1953 | Formal quotient criterion for dg-shifted Yangians |
| `prop:yangian-dk-mc4-reduction` | `proposition` | 2032 | Formal reduction principle from DK-3 to DK-4/DK-5 |
| `prop:yangian-dk4-typea-frontier` | `proposition` | 2085 | DK-4 reduction to the fundamental residue packet in standard type~A |
| `prop:yangian-dk5-compact-generators` | `proposition` | 2202 | DK-5 reduction to compact-generator comparison |
| `prop:yangian-dk5-fundamental-packet` | `proposition` | 2261 | Compact-core comparison reduces to the completed fundamental packet |
| `prop:yangian-dk5-ind-extension` | `proposition` | 2344 | DK-5 comparison functor is the ind-extension of the compact core |
| `cor:yangian-dk5-compact-core` | `corollary` | 2425 | DK-5 reduces to the compact-core equivalence |
| `cor:yangian-dk5-fundamental-packet` | `corollary` | 2456 | DK-5 reduces to compact generation plus completed fundamental-packet transport |
| `prop:yangian-dk5-core-realization` | `proposition` | 2493 | Compact-core DK-5 functors from realization of the proved finite-dimensional factorization DK core |
| `lem:yangian-fd-fundamental-generation` | `lemma` | 2560 | Finite-dimensional Yangian factorization core is generated by fundamental evaluation objects |
| `lem:quantum-fd-fundamental-generation` | `lemma` | 2590 | Finite-dimensional quantum-group factorization core is generated by fundamental evaluation objects |
| `prop:yangian-dk5-spectral-realization-formal` | `proposition` | 2621 | Spectral compact-core realization is formal from generator transport |
| `prop:yangian-dk5-spectral-fundamental-packet` | `proposition` | 2680 | On the spectral side, ordered tensor-generator transport is forced by the completed fundamental packet |
| `lem:quantum-fd-vector-fundamental-generation` | `lemma` | 2759 | Type-\texorpdfstring{$A$}{A} quantum-group fundamental packet is generated by the vector evaluation line |
| `prop:yangian-dk5-spectral-vector-packet` | `proposition` | 2788 | On the spectral side, the completed fundamental packet is forced by the completed vector packet |
| `prop:yangian-dk5-spectral-vector-line` | `proposition` | 2855 | On the spectral side, ordered vector-packet transport is forced by the completed vector line |
| `prop:quantum-fd-vector-seed-shifts` | `proposition` | 2887 | Standard quantum-loop vector seed and additive log-spectral shifts |
| `lem:quantum-fd-vector-seed-schur` | `lemma` | 2925 | Quantum-loop vector seed is Schur-simple |
| `prop:yangian-dk5-spectral-vector-seed` | `proposition` | 2940 | On the spectral side, the completed vector line is forced by one completed vector seed together with spectral shifts |
| `prop:yangian-dk5-spectral-seed-shift-construction` | `proposition` | 2990 | On the realized spectral vector-line locus, the completed vector seed and spectral shifts are canonical |
| `prop:yangian-dk5-spectral-core-shifts` | `proposition` | 3047 | On the realized spectral vector-line locus, loop rotation descends to the full spectral compact core |
| `prop:yangian-dk5-spectral-factorization-shifts` | `proposition` | 3094 | Factorization-locus specializations: \texorpdfstring{$\rho_a$}{rho\_a} pullback, core from vector line, seed-line forcing |
| `cor:yangian-dk5-spectral-seed-realization` | `corollary` | 3185 | One-seed closure: four variants |
| `cor:yangian-dk5-spectral-factorization-schur-seed-line` | `corollary` | 3285 | Schur-simple ambient seed criterion for the multiplicative spectral vector line |
| `cor:yangian-dk5-spectral-factorization-ambient-one-seed` | `corollary` | 3325 | One ambient multiplicative vector seed closes the spectral DK-5 side |
| `cor:yangian-dk5-spectral-factorization-ambient-schur-seed` | `corollary` | 3361 | One Schur-simple ambient multiplicative vector seed closes the spectral DK-5 side |
| `prop:yangian-dk5-spectral-factorization-seed-mono` | `theorem` | 3388 | Spectral DK-5 seed-pair reduction hierarchy |
| `cor:yangian-dk5-spectral-packet-ind` | `corollary` | 3531 | On the realized spectral packet locus, the ambient spectral category is the ind-completion of the spectral compact core |
| `prop:yangian-dg-fundamental-packet-realization` | `proposition` | 3563 | Canonical completed dg fundamental packet from the theorematic finite RTT quotients |
| `prop:yangian-dk5-dg-extension-existence` | `proposition` | 3613 | Canonical exact braided-monoidal extension of the dg packet |
| `prop:yangian-dk5-dg-realization-formal` | `proposition` | 3651 | dg compact-core realization is formal from extension of the completed fundamental packet |
| `cor:yangian-dk5-dg-packet-ind` | `corollary` | 3678 | Compact generation of the completed dg module category identifies the ambient dg side with the ind-completion of the dg compact core |
| `cor:yangian-dk5-dg-half-only` | `corollary` | 3711 | Given dg compact-core realization, the remaining DK-5 input is spectral vector seed-and-shift realization |
| `cor:yangian-dk5-core-realization` | `corollary` | 3749 | DK-5 closes once the compact cores realize the proved finite-dimensional factorization DK core |
| `cor:yangian-typea-mc4-closure-criterion` | `corollary` | 3775 | Type-\texorpdfstring{$A$}{A} MC4 reduction chain: five closure criteria |
| `prop:yangian-tower-mc4-criterion` | `proposition` | 3961 | Yangian tower criterion from finite RTT stages |
| `cor:yangian-weight-cutoff` | `corollary` | 4022 | Standard RTT cutoff for Yangian towers |
| `prop:yangian-rtt-completion-identification` | `proposition` | 4057 | Inverse-limit identification of the standard RTT completion |
| `cor:yangian-standard-mc4-package` | `corollary` | 4111 | Standard RTT tower satisfies the M-level MC4 package |
| `cor:yangian-hlevel-comparison-criterion` | `corollary` | 4144 | H-level comparison criterion for dg-shifted Yangians |
| `prop:yangian-typea-realization-criterion` | `proposition` | 4195 | Standard type-\texorpdfstring{$A$}{A} realization criterion from shared bar seed and finite RTT quotients |
| `thm:yangian-dk45-closure-variants` | `theorem` | 4270 | Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses |
| `cor:yangian-typea-realization-plus-compacts` | `corollary` | 4426 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and compact core |
| `cor:yangian-typea-realization-plus-fundamental-packet` | `corollary` | 4455 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from realization and completed fundamental packet |
| `cor:yangian-typea-realization-plus-core-realization` | `corollary` | 4488 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from dg-shifted realization and compact-core realization of the proved finite-dimensional factorization DK core |
| `cor:yangian-formal-moduli-plus-core-realization` | `corollary` | 4519 | Canonical formal-moduli Yangian target closes DK-4/DK-5 once the compact cores realize the proved finite-dimensional DK core |
| `cor:yangian-typea-realization-plus-dg-packet` | `corollary` | 4570 | Standard type-\texorpdfstring{$A$}{A} DK-4/DK-5 closure from spectral vector-line realization |
| `cor:yangian-canonical-realization-to-spectral-seed` | `corollary` | 4677 | Canonical formal-moduli Yangian target: exact remaining input after RTT-adapted realization |
| `cor:yangian-canonical-realization-to-single-line` | `corollary` | 4776 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one mixed-tensor line on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange` | `corollary` | 4837 | Canonical formal-moduli Yangian target: the local spectral packet contracts to one exchange coefficient family on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-to-exchange-mult` | `corollary` | 4887 | Canonical formal-moduli Yangian target: the local spectral packet descends to one multiplicative-ratio scalar family |
| `cor:yangian-canonical-realization-to-alt-mult` | `corollary` | 4946 | Canonical formal-moduli Yangian target: the local spectral packet is the antisymmetric-channel character on the multiplicative spectral line |
| `cor:yangian-canonical-realization-plus-one-seed` | `corollary` | 4989 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from one canonical spectral seed on the equivariant multiplicative locus |
| `cor:yangian-canonical-realization-plus-vector-line` | `corollary` | 5022 | Canonical formal-moduli Yangian target closes DK-4/DK-5 from spectral vector-line realization |

#### `chapters/examples/yangians_foundations.tex` (25)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:yangian-e1` | `theorem` | 136 | Yangian as \texorpdfstring{$\Eone$}{E1}-chiral |
| `thm:yangian-bar-rtt` | `theorem` | 221 | Yangian bar complex via RTT |
| `thm:yangian-koszul-dual` | `theorem` | 254 | Yangian Koszul dual |
| `cor:yangian-classical-self-dual` | `corollary` | 313 | Yangian classical limit |
| `prop:yangian-koszul` | `proposition` | 354 | RTT Yangian is Koszul |
| `cor:yangian-bar-cobar` | `corollary` | 409 | Yangian bar-cobar recovery |
| `prop:yangian-module-koszul` | `proposition` | 473 | Koszul duality on Yangian modules |
| `prop:dg-shifted-comparison` | `proposition` | 938 | Structural comparison |
| `prop:dg-shifted-rtt-degree2-mixed-tensor-criterion` | `proposition` | 1059 | Degree-2 mixed-tensor criterion for dg-shifted local transport |
| `cor:dg-shifted-rtt-seed-normalized-coefficient` | `proposition` | 1103 | Scalar normalization and Casimir reduction chain |
| `prop:dg-shifted-rtt-presentation-criterion` | `proposition` | 1213 | Stepwise reduction to evaluation detection |
| `prop:dg-shifted-rtt-boundary-seed` | `proposition` | 1294 | Boundary-seed criterion for truncated RTT defects |
| `prop:dg-shifted-rtt-boundary-coefficient-formula` | `proposition` | 1312 | Boundary-strip coefficient formula on the evaluation packet |
| `prop:dg-shifted-rtt-fundamental-coefficient-formula` | `proposition` | 1342 | Explicit coefficient formula for the fundamental monodromy series |
| `cor:dg-shifted-rtt-boundary-support-bound` | `proposition` | 1404 | Support bound and finite detection for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-top-packet-induction` | `proposition` | 1468 | Top-packet induction and closure |
| `prop:dg-shifted-rtt-fundamental-propagation` | `proposition` | 1554 | Fundamental propagation criterion for boundary-strip RTT defects |
| `prop:dg-shifted-rtt-auxiliary-kernel-criterion` | `proposition` | 1651 | Auxiliary-kernel criterion for fundamental RTT propagation |
| `prop:dg-shifted-rtt-typea-auxiliary-uniqueness` | `proposition` | 1721 | Type-A uniqueness of the auxiliary kernel on the fundamental line |
| `cor:dg-shifted-rtt-typea-residue-reduction` | `corollary` | 1790 | Type-A residue reduction for the auxiliary kernel |
| `prop:dg-shifted-rtt-typea-residue-channels` | `proposition` | 1827 | Type-A residue detection on the symmetric and antisymmetric channels |
| `cor:dg-shifted-rtt-typea-single-line` | `corollary` | 1883 | Type-A residue detection on one mixed tensor line |
| `prop:dg-shifted-rtt-typea-uniform-single-line` | `proposition` | 1943 | Uniform residue extraction from one ordered tensor line |
| `cor:dg-shifted-rtt-typea-single-line-bootstrap` | `corollary` | 2004 | Type-A single-line bootstrap to standard evaluation and boundary-strip vanishing |
| `prop:dg-shifted-rtt-standard-typea-local-packet` | `proposition` | 2103 | Standard type-A fundamental line operator has the expected local residue |

### Part III: Connections (95)

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

#### `chapters/connections/concordance.tex` (19)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:glz-special-case` | `proposition` | 274 | GLZ as special case |
| `thm:fg-from-assch` | `theorem` | 288 | FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality |
| `thm:master-pbw` | `theorem` | 599 | Higher-genus PBW concentration for the standard finite-type interacting families |
| `thm:master-theta` | `theorem` | 625 | Cyclic \texorpdfstring{$L_\infty$}{L-infinity} deformation algebra and universal \texorpdfstring{$\Theta_\cA$}{Theta\_A} {\normalfont (MC2, originally conjectured)} |
| `prop:standard-tower-mc5-reduction` | `proposition` | 871 | Standard-tower MC5 reduction after MC3 and realized MC4 |
| `cor:standard-tower-mc5-closure` | `corollary` | 959 | Standard-tower MC5 closure on the canonical Yangian locus |
| `rem:conjecture-attack-strategies` | `remark` | 1260 | Conjecture-by-conjecture attack strategies |
| `prop:en-n2-recovery` | `proposition` | 1887 | \texorpdfstring{$n = 2$}{n = 2} recovery and AF comparison |
| `prop:vassiliev-genus0` | `proposition` | 2033 | Genus-\texorpdfstring{$0$}{0} weight systems from bar complex |
| `thm:anomaly-koszul` | `theorem` | 2091 | Anomaly cancellation as Koszul constraint |
| `thm:anomaly-physical-genus0` | `theorem` | 2125 | Physical anomaly cancellation, genus~\texorpdfstring{$0$}{0} |
| `thm:anomaly-physical-km-w` | `theorem` | 2141 | Physical anomaly cancellation for KM and \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `prop:nc-hodge-symmetry` | `proposition` | 2359 | Hodge symmetry from complementarity |
| `thm:lagrangian-complementarity` | `theorem` | 2957 | Lagrangian complementarity |
| `thm:universal-MC` | `theorem` | 2992 | Universal MC class |
| `thm:discriminant-spectral-verified` | `theorem` | 3214 | Discriminant as spectral determinant --- verified cases |
| `thm:discriminant-spectral` | `theorem` | 3259 | Spectral discriminant --- general case |
| `thm:family-index` | `theorem` | 3490 | Family index theorem for genus expansions |
| `thm:volume-one-concrete-modular-datum` | `theorem` | 4014 | Volume~I concrete modular datum |

#### `chapters/connections/feynman_connection.tex` (1)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:bar-cobar-path-integral-heisenberg` | `theorem` | 207 | Bar complex = path integral for the free boson |

#### `chapters/connections/feynman_diagrams.tex` (11)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:ainfty-constraint-formula` | `theorem` | 188 | \texorpdfstring{$A_\infty$}{A-infinity} constraint formula |
| `prop:disk-local-binary-ternary-reduction` | `proposition` | 293 | Binary-ternary reduction for the disk-local packet |
| `cor:disk-local-ternary-on-brstbar-locus` | `corollary` | 332 | Anomaly-free genus-\texorpdfstring{$0$}{0} collapse of the local packet |
| `prop:compactified-ternary-two-channel` | `proposition` | 359 | Two-channel reduction after compactifying the ternary packet |
| `cor:genus0-compactified-ternary-two-channel` | `corollary` | 395 | Genus-\texorpdfstring{$0$}{0} post-compactification ternary target |
| `cor:genus0-standard-chart-two-residues` | `corollary` | 413 | Standard-chart form of the remaining genus-\texorpdfstring{$0$}{0} packet |
| `prop:m04-standard-log-basis` | `proposition` | 434 | Standard logarithmic basis on \texorpdfstring{$\overline{M}_{0,4}$}{M_0,4} |
| `cor:genus0-two-coefficient-packet` | `corollary` | 481 | Two-coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `cor:genus0-named-coefficient-packet` | `corollary` | 540 | Named coefficient form of the remaining genus-\texorpdfstring{$0$}{0} compactified packet |
| `thm:mk-tree-level` | `theorem` | 913 | Tree-level \texorpdfstring{$m_k$}{m_k} structure |
| `thm:mk-general-structure` | `theorem` | 949 | All-genus \texorpdfstring{$m_k$}{m_k} Feynman expansion |

#### `chapters/connections/genus_complete.tex` (5)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:master-tower` | `theorem` | 221 | Master tower of extensions |
| `thm:chain-modular-functor` | `theorem` | 276 | Chain-level modular functor from bar complex |
| `cor:dual-modular-functor` | `corollary` | 358 | Koszul dual modular functors |
| `thm:bar-moduli-integrals` | `theorem` | 634 | Bar complex computes moduli integrals |
| `thm:full-modular-invariant-hierarchy` | `theorem` | 1078 | The full modular invariant hierarchy |

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

#### `chapters/connections/ym_boundary_theory.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:grand-synthesis-principle` | `theorem` | 32 | Grand synthesis principle |
| `thm:twisted-ym-boundary-brst` | `theorem` | 125 | Boundary BRST recovery for twisted Yang--Mills data |
| `thm:twisted-ym-tangent-center` | `theorem` | 150 | Tangent-to-center principle |
| `cor:twisted-ym-center-rigidity` | `corollary` | 169 | Center-vanishing rigidity criterion |
| `cor:twisted-ym-one-parameter` | `corollary` | 179 | One-parameter criterion |
| `thm:twisted-ym-tangent-factors-through-center` | `theorem` | 201 | The tangent functor factors through the dual center |
| `cor:twisted-ym-interface-invariance` | `corollary` | 227 | Interface invariance of tangent data |
| `cor:twisted-ym-center-comparison` | `corollary` | 245 | Comparison without full boundary equivalence |
| `thm:twisted-ym-dual-unobstructedness` | `theorem` | 287 | Dual unobstructedness criterion |
| `thm:twisted-ym-central-formality` | `theorem` | 310 | Central formality theorem |
| `lem:twisted-ym-center-tensor` | `lemma` | 367 | Center of a chiral tensor product |
| `thm:twisted-ym-binary-mixed-couplings` | `theorem` | 405 | Binary mixed-coupling theorem |
| `cor:twisted-ym-multibody-couplings` | `corollary` | 470 | Multi-body coupling expansion |
| `cor:twisted-ym-mixed-rigidity` | `corollary` | 504 | Mixed rigidity criterion |

#### `chapters/connections/ym_higher_body_couplings.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:relative-duality-theorem` | `theorem` | 67 | Relative duality theorem |
| `cor:relative-tangent-center-principle` | `corollary` | 117 | Relative tangent-to-center principle |
| `cor:relative-dual-unobstructedness` | `corollary` | 128 | Relative dual unobstructedness |
| `thm:relative-central-formality` | `theorem` | 147 | Relative central formality |
| `lem:mixed-ks-well-defined` | `lemma` | 197 | Well-definedness and invariance |
| `thm:first-correction-theorem` | `theorem` | 206 | First-correction theorem |
| `cor:persistence-criterion-quadratic-law` | `corollary` | 236 | Persistence criterion for the quadratic law |
| `thm:universal-interaction-brackets` | `theorem` | 249 | Universal interaction brackets on mixed couplings |
| `lem:w-boundary-simplex-homotopy-invariance` | `lemma` | 352 | Homotopy invariance |
| `thm:w-boundary-cech-duality` | `theorem` | 373 | Higher-body \v{C}ech duality |
| `thm:w-augmented-center-tensor-model` | `theorem` | 446 | Tensor-product model for the augmented center complex |
| `cor:w-pure-mbody-coupling-theorem` | `corollary` | 503 | Pure $m$-body coupling theorem |
| `thm:w-higher-mayer-vietoris-couplings` | `theorem` | 520 | Higher Mayer--Vietoris descent for couplings |
| `thm:w-filtered-stability-pure-mbody` | `theorem` | 562 | Filtered stability of pure $m$-body couplings |

#### `chapters/connections/ym_instanton_screening.tex` (13)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:novikov-completion-theorem` | `theorem` | 79 | Novikov completion theorem |
| `thm:instanton-completed-tangent-center` | `theorem` | 140 | Instanton-completed tangent-to-center principle |
| `thm:screened-tangent-center` | `theorem` | 205 | Screened tangent-to-center principle |
| `prop:koszul-identification-visible-center` | `proposition` | 246 | Koszul identification of the visible center |
| `thm:instanton-screening-spectral-sequence` | `theorem` | 272 | Instanton-screening spectral sequence |
| `thm:central-localization-confinement` | `theorem` | 316 | Central localization criterion for confinement |
| `thm:screened-cech-duality` | `theorem` | 369 | Higher-body \v{C}ech duality after screening |
| `thm:screening-hodge-theorem` | `theorem` | 433 | Screening Hodge theorem |
| `cor:screening-spectral-gap-criterion` | `corollary` | 459 | Screening spectral gap criterion |
| `cor:stable-untwisting-bounded-error` | `corollary` | 512 | Stable untwisting under bounded error |
| `prop:internal-screening-form` | `proposition` | 604 | Operator-algebraic meaning of the screening form |
| `thm:mass-gap-reduction-internal-screening` | `theorem` | 683 | Mass-gap reduction to an internal screening estimate |
| `cor:exact-reduction-screening-estimate` | `corollary` | 717 | Exact formulation of the reduction principle |

### Appendices (122)

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
| `prop:virasoro-pade` | `proposition` | 825 | Pad\'e matching for the Virasoro bar sequence |

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

#### `appendices/nonlinear_modular_shadows.tex` (58)

| Label | Env | Line | Title |
|---|---|---:|---|
| `thm:nms-mc-principle` | `theorem` | 170 | Algebra structure $=$ Maurer--Cartan element |
| `prop:nms-five-component` | `proposition` | 203 | Five-component decomposition |
| `thm:nms-shadow-tower-mc` | `theorem` | 251 | Shadow tower from MC evaluation |
| `cor:nms-all-families-universal` | `corollary` | 291 | All families from universal evaluation |
| `thm:nms-ambient-complementarity-tangent` | `theorem` | 384 | Ambient complementarity in tangent form |
| `thm:nms-cotangent-normal-form` | `theorem` | 438 | Shifted cotangent normal form |
| `prop:nms-legendre-duality` | `proposition` | 484 | Legendre duality of the two potentials |
| `prop:nms-legendre-cubic` | `proposition` | 493 | Legendre duality of cubic tensors |
| `thm:nms-derived-critical-locus` | `theorem` | 514 | Derived critical locus of self-dual deformations |
| `prop:nms-fake-complementarity` | `proposition` | 529 | Criterion for fake complementarity |
| `thm:nms-shadow-master-equations` | `theorem` | 628 | Quartic shadow master equations |
| `thm:nms-separating-boundary-recursion` | `theorem` | 667 | Separating boundary recursion through quartic order |
| `thm:nms-shadow-cocycle-characterization` | `theorem` | 729 | Finite-order realization of the universal class |
| `prop:nms-quartic-closure-envelope` | `proposition` | 780 | Quartic closure of the shadow envelope |
| `thm:nms-heisenberg-exact-linearity` | `theorem` | 803 | Heisenberg exact linearity |
| `cor:nms-heisenberg-gaussian-boundary` | `corollary` | 823 | Gaussian boundary law |
| `thm:nms-affine-cubic-normal-form` | `theorem` | 847 | Affine cubic normal form |
| `cor:nms-affine-boundary-tree` | `corollary` | 871 | Boundary-generated quartic nonlinearity |
| `thm:nms-betagamma-quartic-birth` | `theorem` | 938 | \texorpdfstring{$\beta\gamma$}{betagamma} quartic birth |
| `cor:nms-betagamma-mu-vanishing` | `corollary` | 962 | Vanishing of the quartic contact invariant |
| `cor:nms-betagamma-boundary-law` | `corollary` | 986 | Pure contact boundary law |
| `thm:nms-archetype-trichotomy` | `theorem` | 1003 | Primitive nonlinear archetype trichotomy |
| `thm:nms-rank-one-rigidity` | `theorem` | 1024 | Rank-one abelian rigidity |
| `thm:nms-universal-gravitational-cubic` | `theorem` | 1050 | Universal gravitational cubic tensor |
| `thm:nms-virasoro-mixed-shadow` | `theorem` | 1088 | Virasoro mixed shadow theorem |
| `thm:nms-virasoro-quartic-explicit` | `theorem` | 1116 | Explicit Virasoro quartic contact coefficient |
| `cor:nms-virasoro-cubic-leading` | `corollary` | 1188 | Cubic-leading Virasoro at the uncurved point |
| `thm:nms-w3-mixed-shadow-normal-form` | `theorem` | 1218 | \texorpdfstring{$\mathcal W_3$}{W3} mixed-shadow normal form |
| `prop:nms-w3-visible-resonance-factor` | `proposition` | 1257 | Visible quartic resonance factor for \texorpdfstring{$\mathcal W_3$}{W3} |
| `thm:nms-principal-wn-hessian-cubic` | `theorem` | 1297 | Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `thm:nms-principal-wn-contact-nonvanishing` | `theorem` | 1315 | Nonvanishing of contact quartics for principal \texorpdfstring{$\mathcal W_N$}{WN} |
| `cor:nms-principal-wn-mixed` | `corollary` | 1331 | Principal \texorpdfstring{$\mathcal W_N$}{WN} is mixed cubic--quartic |
| `prop:nms-basis-independence-specialization` | `proposition` | 1440 | Basis independence and specialization |
| `thm:nms-boundary-filtration-quartic-envelope` | `theorem` | 1492 | Boundary filtration of the quartic envelope |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 1516 | Clutching law for the modular quartic resonance class |
| `thm:nms-first-nonlinear-shadow-theta` | `theorem` | 1556 | The first nonlinear shadow of \texorpdfstring{$\Theta_{\cA}$}{ThetaA} |
| `cor:nms-family-boundary-behavior` | `corollary` | 1569 | Family-by-family boundary behavior |
| `prop:nms-functoriality-duality-quartic` | `proposition` | 1638 | Functoriality and duality through quartic order |
| `thm:nms-all-arity-master-equation` | `theorem` | 1741 | All-arity master equation |
| `cor:nms-quintic-master-equation` | `corollary` | 1764 | The quintic master equation |
| `thm:nms-quintic-frame-families` | `theorem` | 1784 | Quintic shadow for the three frame families |
| `thm:nms-virasoro-quintic-forced` | `theorem` | 1803 | The Virasoro quintic is forced |
| `thm:nms-finite-termination` | `theorem` | 1822 | Finite termination for primitive archetypes |
| `thm:nms-all-arity-separating-boundary` | `theorem` | 1847 | All-arity separating boundary recursion |
| `cor:nms-quintic-separating-boundary` | `corollary` | 1863 | Quintic separating boundary recursion |
| `prop:nms-genus-loop-properties` | `proposition` | 1909 | Basic properties of the genus loop operator |
| `thm:nms-nonseparating-clutching-law` | `theorem` | 1926 | Non-separating clutching law for the shadow tower |
| `cor:nms-genus-one-hessian-correction` | `corollary` | 1950 | Genus-$1$ Hessian correction from genus-$0$ quartic shadow |
| `thm:nms-genus-loop-model-families` | `theorem` | 1974 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2057 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2091 | Ambient complementarity and nonlinear modular shadows |
| `prop:nms-nonlinear-phase-standard` | `proposition` | 2290 | Nonlinear phase of the standard families |
| `prop:nms-basis-independence-specialization` | `proposition` | 2596 | Basis independence and specialization |
| `thm:nms-clutching-law-modular-resonance` | `theorem` | 2624 | Clutching law for the modular quartic resonance class |
| `cor:nms-family-boundary-behaviour` | `corollary` | 2654 | Family-by-family boundary behaviour |
| `thm:nms-genus-loop-model-families` | `theorem` | 2687 | Genus loop operator on the model families |
| `thm:nms-beyond-ahat` | `theorem` | 2755 | The modular invariant hierarchy beyond $\hat{A}$ |
| `thm:nms-unified-summary` | `theorem` | 2787 | Ambient complementarity and nonlinear modular shadows |

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
