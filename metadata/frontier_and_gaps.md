# Frontier References and Computational Gap Analysis

Generated: 2026-03-05 (base report)
Last status refresh: 2026-03-15

> **Note (March 15, 2026)**: MC2 is now PROVED (all 3 packages resolved).
> The live frontier begins at MC3/MC4. References below to MC2 as "the
> foundational next target" or "open" are historical.

**Dual Imperative**: Gaps are tracked not to limit ambition but to enable it.
Precise knowledge of what remains open makes credible the push for the most
powerful theorems the subject admits.

## Frontier Reset (March 8, 2026)

- The higher-genus PBW concentration entry theorem is now treated as resolved
  for the standard finite-type interacting families:
  affine Kac-Moody, Virasoro, and principal finite-type `W_N`.
- The global dependency order is now:
  resolved MC1 entry theorem;
  MC2 as the foundational next target, already reduced on the theorem
  surface to the intrinsic cyclic model, the geometric completed tensor
  / clutching package, and the one-channel genus-by-genus normalization
  problem in the simple-Lie case;
  MC3/MC4 as structural extension and H-level comparison problems;
  MC5 as downstream physics completion.
- The finite-type `W_N` row in Part B is now theorem-level (generic principal
  locus), with `W_3` as explicit support and higher `N` tracked as a
  computation-depth gap rather than a theorem-status gap.
- The active `W` frontier is now split cleanly:
  the infinite-generator H-level comparison / coefficient-identity
  package for `W_\infty` and Yangian towers, and non-principal orbit
  duality (a distinct three-packet orbit-indexed frontier).  The latter is now read
  as three exact packets: dual-orbit input, orbit-indexed level shift,
  and paired DS seed transport/globalization.
- For Virasoro, the same-family partner `Vir_{26-c}` should be read as the
  proved M/S-level complementarity shadow used in genus and semi-infinite
  calculations.  The stronger H-level realization by an infinite-generator
  dual object (`W_\infty`) remains part of the MC4 frontier.
- The immediate foundational target is now MC2: cyclic deformation
  algebra and the universal `Theta_A` programme, i.e. the conjectural
  H-level completion of the modular characteristic hierarchy.  The live
  frontier is now concentrated in three exact packages:
  the intrinsic cyclic `\Defcyc(\cA)` model,
  the geometric completed tensor / modular-operadic clutching package,
  and the one-channel genus-by-genus normalization problem in the
  simple-Lie case.  The completed, weight-filtered/pronilpotent bar
  scaffold for standard infinite-generator towers should now be treated
  as supporting infrastructure rather than the live frontier bottleneck.
- The theorem-ready MC4 package should now be stated in input/output form:
  separated complete weight filtrations with finite-type truncations,
  a completed bar object
  `\widehat{\bar B}(\cA)=\varprojlim_N \bar B(\cA_{\le N})`,
  compatible finite-stage dg coalgebra structures so continuity of the
  completed differential is formal, and bar-cobar comparison maps
  compatible with the inverse system.
- Formal reduction is now proved: once continuity and inverse-limit
  compatibility are in place, Mittag--Leffler or degreewise stabilization
  of finite-stage bar cohomology is enough to recover the completed
  M-level bar-cobar object.
- The reduction is slightly sharper than a bare stabilization slogan:
  eventual surjectivity on finite-dimensional weight slices already
  suffices for the Mittag--Leffler input, so the live task is a
  weightwise tower theorem rather than global a priori constancy.
- Both principal MC4 examples now have theorem-ready specializations of
  that reduction.  For the standard principal-stage `W_\infty` tower,
  continuity is now formal and the completed M-level bar-cobar package
  is proved.  For the standard RTT Yangian tower, the inverse limit is
  now identified with the coefficientwise RTT completion and the
  completed M-level bar-cobar package is likewise proved.
- The principal examples for that package are
  `W_\infty = \varprojlim_N W_N` and Yangian towers assembled from finite
  RTT stages.  The remaining frontier is no longer the existence of
  standard M-level completions, but their comparison with the intended
  H-level dg-shifted or factorization-theoretic targets.
- That comparison is now reduced to a concrete filtered-target problem:
  construct a separated complete H-level model whose finite quotients
  recover the theorematic principal stages.  Once those compatible
  finite quotients exist, the comparison with the standard completion is
  formal by the inverse-limit criterion in the manuscript.
- The filtered-target problem has now been split into two explicit
  construction packages:
  a principal-stage compatible factorization model for `W_\infty`, and
  an RTT-adapted filtration on the dg-shifted Yangian whose finite
  quotients recover the finite RTT stages.
- The physics-facing frontier is downstream of those packages:
  MC5 does not ask first for a bulk/bar or AGT miracle.  It asks for a
  BV/BRST/bar, holographic, or AGT comparison only after the relevant
  filtered H-level target with the correct finite quotients has been
  constructed and matched coefficientwise to the theorematic finite
  stages.
- The formal descent layer is also separated now:
  quotient systems or preserved RTT-level ideals are enough to descend
  the relevant dg data; what remains open is constructing those
  quotient systems with the required finite-stage identifications.
- The live local input is sharper than that:
  on the Yangian side one needs an RTT-triangularity or pole-order
  locality theorem showing that the line-operator formulas preserve the
  ideals generated by modes above level `N`;
  on the `W_\infty` side one needs stable higher-spin factorization
  ideals whose quotients recover the principal stages.
- The next reduction is now also formalized:
  the Yangian preservation statement follows once the rational
  line-operator kernels are written coefficientwise in RTT level, and
  the `W_\infty` quotient system follows once the higher-spin OPE is
  spin-triangular and agrees stagewise with the principal DS formulas.
- The remaining open input after that preservation step is now exact:
  on the Yangian side one must match the coefficientwise truncated RTT
  relations and evaluation modules of the dg quotient with `Y_{\le N}`,
  while on the `W_\infty` side one must match the stagewise quotient
  OPE coefficients and residue/bar operations with the principal
  Drinfeld--Sokolov stages.
- The next reduction is now also formalized:
  the Yangian side is reduced to equality of the extracted
  line-operator kernel coefficients with the finite truncated RTT
  coefficients, and the `W_\infty` side is reduced to equality of the
  extracted local OPE/residue coefficients with the principal
  Drinfeld--Sokolov coefficients.
- The live MC4 coefficient tasks are now named mode by mode:
  prove `K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)` on the Yangian side and
  `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)` on the
  `W_\infty` side.
- The next finite reduction is now explicit:
  detect the Yangian identities on a faithful evaluation family, and
  detect the `W_\infty` identities from the finitely many
  generator-level residue coefficients plus translation closure.
- The finite checklists are now named:
  the Yangian side reduces to the boundary strip
  `{\Delta_{a,0}(N)}_{0\le a\le N}`, and the `W_\infty` side reduces to
  the explicit finite primary index set `\mathcal{I}_N`.
- The Yangian finite checklist is now sharper than that slogan:
  at stage `N`, the boundary strip is detected on generic tensor
  products of the fundamental evaluation module of lengths at most
  `N+1`.
- The Yangian reduction is now sharper still:
  once the fundamental `L`-operator satisfies the truncated RTT
  relation and the twisted coproduct multiplies monodromy matrices in
  the standard way, higher tensor lengths are formal.
- The Yangian reduction is now exact at the pairwise level:
  the remaining fundamental check is the auxiliary-space kernel
  identity `L_a(u)=R_{0a}(u-a)`, after which the RTT relation is just
  the Yang--Baxter equation.
- For the standard type-A RTT tower, that pairwise step is now reduced
  again: the auxiliary kernel is forced by three local checks on the
  fundamental line, namely `\mathfrak{sl}_M`-equivariance, unit
  asymptotic, and residue `-\hbar P`.
- In that same type-A setting, once the line-operator construction
  fixes symmetry and asymptotic normalization, the genuinely analytic
  Yangian task is only the residue computation at the simple pole, now
  reduced further to the two residue eigenvalues on `\Sym^2(V)` and
  `\Lambda^2(V)`, and in fact to the single ordered tensor-line
  residue `e_1\otimes e_2 \mapsto -\hbar\,e_2\otimes e_1`.
- The first nontrivial `W_\infty` seed packet is now explicit:
  beyond the theorematic Virasoro block, stage `N=3` is exactly a list
  of `15` primary coefficients.
- That stage-`3` packet is now mostly discharged on the theorem
  surface: the explicit `W_3` OPE reduces it to `3` nonzero primary
  coefficients and `12` forced vanishing statements, so the next
  genuinely new higher-spin packet is stage `N=4`.
- The stage-`4` packet is now compressed as well:
  after removing the exact stress-tensor sector and the theorematic
  `(3,3)` `W_3` sector, the residual stage-`4` packet has exactly
  `29` primary coefficients.
- Primaryity first compresses that stage-`4` packet again:
  only the `7` top-pole coefficients can be nonzero, while the
  remaining `22` entries are forced zeros.
- Skew-symmetry then compresses it once more:
  the odd self-OPE coefficient `(4,4,3,5)` vanishes, leaving `6`
  live stage-`4` coefficients and `23` forced zeros.
- Those `6` coefficients now sit in three explicit local OPE blocks:
  one `(3,3)\to 4` block, one mixed `(3,4)` block, and one even
  `(4,4)` block.
- Among those three blocks, the only genuinely mixed stage-`4`
  higher-spin data are the three coefficients in the mixed `(3,4)`
  block.
- Within that mixed `(3,4)` block, the `W^{(3)}` target channel is
  swap-even under reversing the mixed OPE order, while the
  `W^{(2)}` and `W^{(4)}` target channels are swap-odd.
- On the principal Drinfeld--Sokolov side, the mixed `W^{(2)}` target
  channel vanishes by mixed-weight orthogonality plus the Virasoro Ward
  identity, while the principal `W^{(4)}`-`W^{(4)}\to T` coefficient is
  universally fixed to `2`.  The live stage-`4` comparison therefore
  consists of four free coefficient channels
  `c_{334}`, `c_{444}`, `\mathsf{C}_{3,4;3;0,4}`,
  `\mathsf{C}_{3,4;4;0,3}`, together with the residue-side checks
  `\mathsf{C}^{\mathrm{res}}_{4,4;2;0,6}=2` and
  `\mathsf{C}^{\mathrm{res}}_{3,4;2;0,5}=0`.
- This finite-detection pair is now the active repo-wide MC4
  open-problem ledger:
  build the filtered H-level targets, prove the exact identities
  `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)` and
  `K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)`, and close these two
  finite-detection packages; on the `W_\infty` side the first live
  packets are already reduced on the theorem surface to the stage-`3`
  fifteen-coefficient packet and the exact stage-`4` endpoint given by
  the four channels `c_{334}`, `c_{444}`,
  `\mathsf{C}_{3,4;3;0,4}`, `\mathsf{C}_{3,4;4;0,3}` together with the
  residue-side checks `\mathsf{C}^{\mathrm{res}}_{4,4;2;0,6}=2` and
  `\mathsf{C}^{\mathrm{res}}_{3,4;2;0,5}=0`.
- Periodicity is not part of that master-conjecture chain.
  Its structural lcm/profile shadow is theorematic, but modular
  bar-cohomology periodicity and the sharp geometric factors remain a
  weak auxiliary frontier and should not be used to inflate the proved
  core.

---

## PART A: FRONTIER REFERENCE ANALYSIS

### 1. Mok25 -- Logarithmic Fulton-MacPherson Configuration Spaces

**Source**: `references/2503.17563v2.pdf` (Mok, 2025)

**main_results**:
- **Thm 1.1.1 (=3.3.1)**: For a smooth pair (X, D) with D an snc divisor, the logarithmic FM space FM_n(X|D) is an snc compactification of Conf_n(X \ D). It is a wonderful compactification in the sense of De Concini-Procesi, obtained by blowing up logarithmic diagonals.
- **Thm 1.1.2 (=5.2.3)**: For a log smooth degeneration W/B, there exists a log smooth degeneration FM_n(W/B) -> B of FM configuration spaces, compatible with the FM compactification on each fiber.
- **Thm 1.1.3 (=5.3.4)**: Degeneration formula -- each irreducible component of the special fiber of FM_n(W/B) is a birational modification of a product of logarithmic FM spaces associated to the components of the special fiber.

**open_questions**:
- Logarithmic unramified Gromov-Witten theory using log FM spaces.
- Intersection theory on log FM spaces (Chow rings, tautological classes).
- Comparison with other compactifications (Hassett, tropical).

**connection_to_manuscript**:
- The FM compactification C-bar_n(X) is the geometric engine of the entire monograph. Mok25 extends this to pairs (X, D), which is exactly what is needed for:
  - Configuration spaces on punctured curves (relevant for conformal blocks with insertions).
  - Degeneration limits in the genus expansion (where curves acquire nodes = boundary divisor D).
  - The log smooth degeneration theorem (1.1.2) could provide the geometric foundation for the higher-genus bar complex degeneration that is currently handled abstractly via sewing/gluing axioms.

**potential_new_examples**:
- Bar complexes on punctured curves Sigma_g \ {p_1,...,p_n} using log FM spaces. This would give a geometric construction of the bar complex with insertions, currently missing.
- Explicit degeneration formulas for bar complex dimensions as curves degenerate, providing a geometric proof of the boundary restriction formulas in rem:genus2-degeneration.
- Configuration spaces on normal crossings surfaces (beyond curves).

**would_need**:
- Log Arnold relations: the analog of the Arnold relation eta_12 ^ eta_23 + eta_23 ^ eta_31 + eta_31 ^ eta_12 = 0 for logarithmic forms on FM_n(X|D).
- Log Verdier duality on FM_n(X|D): does the Poincare duality mechanism that exchanges bar and cobar extend to the logarithmic setting?
- Comparison map FM_n(X|D) -> FM_n(X) and its effect on the OS algebra.

---

### 2. CDG20 -- Boundary Chiral Algebras and Holomorphic Twists

**Source**: `references/Boundary Chiral Algebras and Holomorphic Twists.pdf` (Costello-Dimofte-Gaiotto, 2020)

**main_results**:
- For a 3d N=2 theory with holomorphic twist, the bulk algebra V is a commutative PVA (Poisson vertex algebra = Coisson algebra in the manuscript's terminology).
- The boundary algebra V_partial[B] associated to a boundary condition B is a (possibly non-commutative) chiral algebra.
- There is a bulk-boundary map beta: V -> Z(V_partial[B]) making the boundary algebra a V-module.
- Boundary for gauge theory with Neumann b.c.: V_partial = (V_partial^matter)^{G_C[[z]]} (invariants under the gauge group formal loop algebra).
- Examples computed: free chirals, superpotential (LG models), SQED <-> XYZ mirror symmetry duality.

**open_questions**:
- Higher A_infinity structures on the boundary algebra (discussed but not computed).
- Full proof of the SQED/XYZ boundary algebra equivalence.
- Generalization beyond N=2 to N=4 boundary conditions.

**connection_to_manuscript**:
- The bulk-boundary relationship V (Coisson/PVA) -> V_partial (chiral algebra) is exactly the Coisson-to-vertex-algebra quantization studied in ch:chiral-deformation (Theorem thm:chiral-kontsevich).
- The boundary Koszul duality: if V_partial[B] is a chiral algebra, the manuscript's bar-cobar machinery applies. The Koszul dual of V_partial would encode the "dual boundary condition."
- The BRST/DS reduction V_partial = (V_partial^matter)^{G_C[[z]]} parallels the W-algebra construction via DS reduction.

**potential_new_examples**:
- Boundary chiral algebras for 3d mirror pairs as Koszul dual pairs. E.g., SQED boundary algebra vs. XYZ model boundary algebra could be related by bar-cobar duality.
- The bulk PVA as a P_infinity-chiral algebra (the manuscript's framework), with the boundary algebra as its E_infinity quantization.
- Module categories for boundary algebras: the D-brane category on the boundary should correspond to the module Koszul dual category.

**would_need**:
- Explicit OPE computations for V_partial[B] in examples (to feed into bar complex computations).
- Verification that the bulk-boundary map beta respects the bar complex structure.
- A theorem relating boundary condition duality to chiral Koszul duality.

---

### 3. DNP25 -- Line Operators in Holomorphic-Topological QFT

**Source**: `references/Line Operators in HQFT.pdf` (Dimofte-Niu-Py, 2025)

**main_results**:
- The category C of line operators in a 3d HT QFT is equivalent to A!-mod (modules for the Koszul dual A!), where A is the local operator algebra.
- **Theorem 4.1**: For quasi-linear theories and line operators defined by linear MC couplings, the singular part of the line-operator OPE is given exactly by a new MC element; there are no higher bulk-insertion corrections.
- A! carries the structure of a "dg-shifted Yangian" with Maurer-Cartan element r(z) satisfying an A_infinity Yang-Baxter equation.
- **Theorem 7.1**: In gauge theories with matter + superpotential, A! is explicitly a dg-shifted Yangian.
- **Conjecture 5.2**: A! is always a dg-shifted Yangian in perturbative 3d HT QFT.

**open_questions**:
- Is A! always a dg-shifted Yangian? (Conjecture 5.2)
- Non-perturbative corrections to line operator OPEs.
- Relation to the Coulomb branch construction of Braverman-Finkelberg-Nakajima.

**connection_to_manuscript**:
- This is the most directly relevant reference. The identification C = A!-mod is precisely the module Koszul duality of Chapter chiral_modules (Theorem thm:e1-module-koszul-duality).
- The dg-shifted Yangian structure on A! connects to the Yangian chapter (chap:yangians), where Y(g)^! = Y_{R^{-1}}(g) is proved.
- The quasi-linear non-renormalization theorem is best read as perturbative evidence for the standard Yangian MC4 target, not as a proof of the manuscript's Koszul spectral-sequence collapse.
- The A_infinity Yang-Baxter equation for r(z) is strong structural evidence for the twisting-morphism picture, but the identification with the manuscript's bar differential still needs a direct comparison theorem.

**potential_new_examples**:
- dg-shifted Yangians as explicit Koszul duals: compute bar complexes for specific examples (e.g., SQCD, Chern-Simons-matter theories).
- Line operator categories as module Koszul dual categories, providing concrete examples for the abstract theory in chiral_modules.tex.
- The MC element r(z) as a twisting morphism in the bar-cobar adjunction.

**would_need**:
- A precise comparison between the "dg-shifted Yangian" of DNP25 and the E_1-chiral Yangian of the manuscript (Definition def:yangian-rtt).
- Verification that the A_infinity Yang-Baxter equation is equivalent to the d^2 = 0 condition on the bar complex.
- An explicit computation of the bar complex of a dg-shifted Yangian (beyond what is in Theorem thm:yangian-bar-rtt).

---

### 4. GKW24 -- Higher Operations in Perturbation Theory

**Source**: `references/Higher Operations in Perturbation Theory.pdf` (Gaiotto-Kulp-Wu, 2024)

**main_results**:
- Systematic Feynman diagram framework for computing BRST anomaly brackets (= higher operations) in HT QFT.
- Configuration space perspective (Section 3.6) connecting Feynman diagrams to operads and factorization algebras.
- Non-renormalization theorem: for theories with T >= 2 topological directions, the higher operations are 1-loop exact.
- Quadratic identities (Wess-Zumino consistency) from operatope geometry.
- L_infinity structure on interactions from eta^2 = 0 (BRST nilpotency).

**open_questions**:
- Beyond 1-loop: what happens when the non-renormalization theorem fails (T < 2)?
- The role of operatopes in organizing higher operations.
- Relation to the BV formalism and master equation.

**connection_to_manuscript**:
- The paper gives the closest perturbative HT source of local higher-operation data for MC5, but at present only on the flat-space BRST/factorization side.
- Its configuration-space perspective and compactification heuristic suggest a route toward the FM boundary calculus used in the manuscript, but they do not yet identify the perturbative brackets with the curvewise bar differential.
- The L_infinity and quadratic-axiom package should be treated as local M/S-level evidence for a bar/FM dictionary, not as an H-level proof of the all-genus BV/BRST = bar statement.
- The operatope geometry may provide an auxiliary local model for certain compactified integration regions, but it is not yet a replacement for the FM compactification in the manuscript.

**potential_new_examples**:
- Explicit Feynman diagram computations of bar complex differentials for interacting theories (beyond free fields and Kac-Moody).
- Higher operations (m_k for k >= 3) computed via Feynman diagrams, providing data for the curved A_infinity structure.
- Operatope compactifications as alternatives to FM compactifications for specific diagram topologies.

**would_need**:
- A precise dictionary between GKW's Feynman diagrams and the manuscript's residue computations on FM spaces.
- A theorem identifying the local perturbative BRST brackets with the bar differential on the standard disk/FM chart.
- On the theorematic anomaly-free genus-0 BRST/bar locus, completion of the remaining ternary comparison on `\overline{C}_3`; the binary propagator/residue packet is already theorematic there.
- A compactification/Stokes comparison showing that the perturbative integrands extend to the FM boundary calculus used in the manuscript.
- After that compactification step, only two ternary boundary channels on `\overline{M}_{0,4} \cong \mathbb{P}^1` remain independent; the third is forced by the residue theorem.
- In the standard `0,1,\infty` chart on `\overline{M}_{0,4}`, the remaining genus-0 compactified packet is exactly the residue comparison at `0` and `1`.
- Equivalently, on that standard chart the compactified genus-0 packet is the vanishing of the two coefficients of `d\log t` and `d\log(1-t)`.
- Equivalently again, the remaining compactified genus-0 MC5 task is the pair of named coefficient identities `\mathsf{a}_{\mathrm{pert}}=\mathsf{a}_{\mathrm{bar}}` and `\mathsf{b}_{\mathrm{pert}}=\mathsf{b}_{\mathrm{bar}}`.
- Verification in specific examples that the local L_infinity brackets recover the manuscript's bar operations before any genuswise clutching step.

---

### 5. Zeng23 -- Celestial Holography from Boundary Chiral Algebra

**Source**: `references/2302.06693v1.pdf` (Zeng, 2023)

**main_results**:
- KK reduction of 6d holomorphic theories on S^3 to 1d BF theory.
- A_infinity structure on tangential CR cohomology H^{0,*}_b(S^3).
- Twisted holography conjecture (Conjecture 1.1, from Costello): lim_{N -> infinity} A_N = B^! (the large-N limit of the boundary algebra is the Koszul dual of the bulk algebra B).
- Holomorphic CS KK-reduced to 1d BF theory with boundary algebra C*(g[[w]]).
- Non-planar sector accessible via matrix contraction.

**open_questions**:
- Proof of the twisted holography conjecture (Conjecture 1.1).
- Non-perturbative completion of the A_infinity structure.
- Higher-genus celestial amplitudes.

**connection_to_manuscript**:
- The twisted holography conjecture lim A_N = B^! is a large-N version of Koszul duality: the Koszul dual appears as the large-N limit of boundary algebras.
- The A_infinity structure on CR cohomology is an instance of the curved A_infinity structure arising from bar complexes.
- The KK reduction from 6d to 1d provides a physical mechanism for the bar complex: the tower of KK modes becomes the bar complex filtration.

**potential_new_examples**:
- Explicit A_infinity computations on H^{0,*}_b(S^3) as bar complex computations.
- Large-N limits of Koszul dual pairs: how does the bar complex behave as the rank of the gauge group grows?
- Celestial holography as a form of chiral Koszul duality between 4d and 2d algebras.

**would_need**:
- A precise formulation of "large-N Koszul duality" within the manuscript's framework.
- Explicit computation of the A_infinity structure on H^{0,*}_b(S^3) through degree >= 3.
- Verification that the twisted holography conjecture is compatible with the bar-cobar adjunction.

---

### 6. KhanZeng25 -- PVA from 3d Gauge Theory

**Source**: `references/2502.13227v1 (2).pdf` (Khan-Zeng, 2025)

**main_results**:
- Construction of a 3d HT Poisson sigma model from any PVA (Poisson vertex algebra = Coisson algebra).
- Main result: gauge invariance of the action holds if and only if the lambda-bracket satisfies the Jacobi identity (i.e., the PVA axioms).
- Examples: affine KM PVA -> Chern-Simons theory; Virasoro PVA -> 3d gravity; W-algebra PVAs -> higher-spin gravity.
- Phase space for Virasoro model = T*T_g (cotangent bundle of Teichmuller space).
- Connection to deformation quantization of PVAs.

**open_questions**:
- Quantization of the 3d HT Poisson sigma model (beyond the classical level).
- Non-perturbative aspects of the Virasoro/W-algebra sigma models.
- Relation to known 3d gravity theories (Chern-Simons formulation).

**connection_to_manuscript**:
- The PVA -> 3d sigma model correspondence provides a physical realization of the Coisson-to-chiral quantization path studied in ch:chiral-deformation.
- The gauge invariance <=> PVA Jacobi identity theorem is the physics version of the d^2 = 0 theorem for the bar complex (Theorem thm:bar-nilpotency-complete).
- The phase space T*T_g for the Virasoro model connects to the genus-g moduli space M_g, providing a physics perspective on the higher-genus bar complex.

**potential_new_examples**:
- Bar complexes for the 3d sigma models: the bar complex of the boundary chiral algebra should compute the perturbative expansion of the sigma model.
- Genus-g partition functions of the sigma models as instances of the genus universality theorem.
- W-algebra PVAs -> higher-spin gravity: the Koszul dual of the boundary W-algebra should give the dual gravitational theory.

**would_need**:
- A theorem relating the 3d sigma model partition function to the bar complex free energy F_g.
- Explicit quantization of the affine KM and Virasoro sigma models, producing the chiral algebras hat{g}_k and Vir_c.
- Comparison of the gauge invariance <=> PVA Jacobi with the d^2 = 0 proof in the manuscript.

---

## PART B: COMPUTATIONAL GAP ANALYSIS

### Master Table Cross-Check

The Master Table (Table tab:master-invariants in examples_summary.tex) lists these algebras:
Free fermion, bc ghosts, Heisenberg, hat{sl}_2, hat{sl}_3, hat{E}_8, Vir_c, W_3, W_N (general), Yangian Y(g).

For each, we analyze the state of four computations:
1. **Bar complex**: computed through what degree?
2. **Genus pipeline**: F_g computed through what genus?
3. **Module category**: how much representation theory is developed?
4. **Spectral sequence**: E_2 page computed? Convergence analyzed?

---

### Algebra-by-Algebra Analysis

#### 1. Free Fermion (psi)

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-3 explicit, deg 4-5 by argument** | Fermion antisymmetry forces vanishing in deg >= 2 at genus 0 (free_fields.tex). Coalgebra structure proved. |
| Genus pipeline | **F_g = 0 for all g** | kappa = 0, so no obstruction at any genus. Complete. |
| Module category | **Minimal** | Fock module defined, but no systematic module Koszul duality beyond the algebra level. |
| Spectral sequence | **E_1 collapse proved** | Exact Koszul, acyclic bar complex. Complete. |

**Gaps**: Module Koszul duality for fermion modules (Fock spaces parameterized by boundary conditions) not developed. The genus >= 1 bar complex (where H^1(Sigma_g) contributes) is noted but not computed explicitly.

#### 2. bc-betagamma System

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-5 explicit for betagamma** | Dimensions: 2, 4, 10, 26, 70 (exponential growth). bc: 2, 3, 6, 13, 28. Verified in beta_gamma.tex through degree 5 with full differential. |
| Genus pipeline | **F_g = 0 for all g** | kappa = 0 (exact Koszul). betagamma genus expansion in genus_expansions.tex. |
| Module category | **Well-developed** | Fock modules M_lambda^{bg} and M_q^{bc} defined, module Koszul duality proved (Proposition prop:bg-bc-module-kd), spectral flow analyzed. |
| Spectral sequence | **E_1 collapse proved** | Exact Koszul, bar differential strict. |

**Gaps**: Derived bc-betagamma system (Conjecture conj:extended-ferm-ghost) remains conjectural. The full generating function for bar complex dimensions is conjectured but not proved (Conjecture conj:betagamma-bar-dim: dim B^n = 2 * 3^{n-1}).

#### 3. Heisenberg (H_kappa)

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-5 explicit** | Dimensions: 1, 1, 1, 2, 3 (partition function). Full differential computed through degree 4 (comp:heisenberg-deg3-full, comp:heisenberg-deg4). MC equation verified through degree 4. |
| Genus pipeline | **F_g for ALL g** | Complete closed formula: F_g = kappa * (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!. Explicit values through g=5. Generating function summed. Convergence proved. |
| Module category | **Minimal** | Fock modules defined but module Koszul duality not systematically developed. |
| Spectral sequence | **E_2 collapse proved** | Koszul, curved (m_0 = kappa). |

**Gaps**: Module Koszul duality for Heisenberg modules not developed. The Heisenberg is the simplest curved example, so working out module Koszul duality here would be a valuable test case. The rank-d Heisenberg has genus-1 and genus-2 computations (heisenberg_eisenstein.tex) but the multi-boson bar complex at higher degree is not computed explicitly.

#### 4. hat{sl}_2 at Level k

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-3 full, deg 4-5 from growth rate** | Dimensions: 3, 6, 15, 36, 91 (polynomial). Full differential through degree 3. Acyclicity at generic level verified (comp:km-acyclic). |
| Genus pipeline | **F_g for ALL g** | Complete formula: F_g = 3(k+2)/4 * lambda_g^FP. Explicit values through g=5 in genus_expansions.tex. Complementarity F_g + F_g' = 0 proved. |
| Module category | **Well-developed** | Admissible modules, Whittaker modules, KZB connection, Verlinde formula. Genus-1 pipeline complete (kac_moody_framework.tex). Module Koszul duality at genus 1 proved. |
| Spectral sequence | **E_2 collapse proved at generic k** | Koszul at generic k. At critical level k=-2: higher differentials from FF center. At admissible levels: collapse fails. |

**Gaps**: The bar complex differential at degree 4 and 5 is not computed explicitly (only the dimensions are given). The genus-1 module Koszul duality is proved but the genus >= 2 module theory is not developed. Non-simply-laced analogs (e.g., hat{so}_5 in detailed_computations.tex) have only degree-2 differentials.

#### 5. hat{sl}_3 at Level k

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-3 full, deg 4-5 MISSING** | Dimensions: 8, 36, 204, ---, ---. Degree-3 Serre relation computation complete (comp:sl3-degree3-complete). Degree-2 differential full (comp:sl3-bar). **Degrees 4 and 5 not computed.** |
| Genus pipeline | **F_g for all g (via universality)** | Uses kappa = 4(k+3)/3 and the universal formula. But no explicit evaluation beyond applying the formula. |
| Module category | **Minimal beyond algebra level** | OPE and structure constants computed (comp:sl3-ope). Wakimoto at critical level stated (thm:w3-wakimoto-sl3). No module Koszul duality. |
| Spectral sequence | **E_2 collapse claimed** | By universal KM Koszul theorem. No explicit E_2 page computation. |

**Gaps**:
- **Major gap**: Bar complex dimensions at degree 4 and 5 are listed as "---" in the Master Table. The dimension table (comp:sl3-dim-table) gives 24576 and 786432, but these are the raw tensor product dimensions, not the bar complex cohomology.
- No explicit bar differential at degree >= 4.
- No module Koszul duality.
- The "Three Theorems in Action" showcase is done for sl_2 but NOT for sl_3.

#### 6. hat{E}_8 at Level k

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **Only abstract** | Via universal KM theorem. No explicit computation. |
| Genus pipeline | **Via universality only** | kappa = 62(k+30)/15. |
| Module category | **None** | Only the Frenkel-Kac-Segal identification via E_8 root lattice (lattice_foundations.tex). |
| Spectral sequence | **Claimed via universal theorem** | No explicit verification. |

**Gaps**: This is essentially a placeholder row in the Master Table. No explicit bar complex, no module theory, no worked computation. Given dim(E_8) = 248, even degree-2 has dimension 248^2 = 61504, making explicit computation challenging but the structure (single orbit of roots) should simplify it.

#### 7. Virasoro (Vir_c)

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-5 explicit** | Dimensions: 1, 2, 5, 12, 30 (Catalan numbers). Full differential at degree 2 (comp:virasoro-bar-diff). Curvature element m_0 = c/2 computed. |
| Genus pipeline | **F_g for all g** | kappa = c/2. Complete formula. Complementarity c + c' = 26. Genus-1 pipeline complete. |
| Module category | **Moderate** | Minimal models via coset (ex:minimal-coset). Module Koszul duality for Vir not explicitly developed; the current manuscript only fixes the same-family complementarity partner Vir_c <-> Vir_{26-c} at the model/shadow level. |
| Spectral sequence | **E_2 collapse at generic c** | Koszul. Special values c=0 (uncurved) and c=26 (dual uncurved) analyzed. |

**Gaps**:
- Bar differential at degree 3 through 5 not explicitly computed (only the degree-2 differential and the curvature element).
- Module Koszul duality for Verma/highest-weight modules not developed.
- The Catalan number pattern for dim B^n is stated but not proved (only verified through degree 5).

#### 8. W_3 Algebra

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-4 explicit, deg 5 MISSING** | Dimensions: 2, 5, 16, 52, ---. Full degree-2 differential (comp:w3-bar-degree2). All n-th products computed (comp:w3-nthproducts). Curvature and dual level verified (comp:w3-curvature-dual-detail). |
| Genus pipeline | **F_g for all g** | kappa = 5c/6. c + c' = 100. Genus-1 pipeline complete. |
| Module category | **Minimal** | DS reduction computed (comp:ds-w3). OPE coefficients verified. No module Koszul duality. |
| Spectral sequence | **E_2 collapse at generic k** | Koszul property proved via W-algebra Koszul main theorem. |

**Gaps**:
- **Degree-5 bar complex dimension missing** (listed as "---" in Master Table).
- No explicit degree-3 or degree-4 bar differential (only dimensions given).
- Module Koszul duality for W_3 modules not developed.
- The non-principal nilpotent case (Conjecture conj:w-orbit-duality) remains open,
  but the type-A hook/subregular combinatorial frontier scaffold is now
  implemented in `compute/lib/nonprincipal_ds_orbits.py`. This scaffold
  serves the orbit-indexed non-principal transport problem and should
  not be conflated with the exact MC4 coefficient-identification packet
  for `W_\infty` / Yangian towers.
- Exact remaining packet 1: determine the dual-orbit input required by
  Conjecture `conj:w-orbit-duality` beyond the current seeded type-A
  catalog, including the needed component-group compatibilities.
- Exact remaining packet 2: determine the orbit-indexed non-principal
  level-shift rule `k' = k'(k,f)` beyond the current seeded correction
  table.
- Exact remaining packet 3: construct and globalize paired
  non-principal DS seed transports so that survivor brackets,
  cohomology profiles, and normalization data agree on dual orbit
  pairs beyond the present hook/subregular theorematic seeds.
- The non-principal DS seed layer is now split into
  `compute/lib/bv_duality.py` (type-A BV dual pairs, including the first
  non-self-dual hook pair at `A_3`) and
  `compute/lib/nonprincipal_ds_reduction.py` (proved `sl_3` subregular BP
  seed invariants + family-level hook/subregular seed catalog records). The BP
  central-charge formulas presently implemented there give a level-independent
  sum `c(k)+c(k')=76` for `k'=-k-6`; reconciling this with the chapter-level
  `22` normalization claim is now an explicit frontier consistency task.
- The normalization bridge is now explicit in
  `compute/lib/nonprincipal_ds_normalization.py` (shift-only convention map
  from the raw `76` sum to the chapter-target `22` sum), and the chain-input
  DS scaffold is initialized in `compute/lib/ds_reduction.py`
  (subregular `sl_3` triple, positive-grade root profile, BRST ghost weights).
- The `sl_3` subregular DS seed now includes an explicit truncated BRST
  differential (`d = \chi \wedge -` on the seed ghost exterior algebra) with
  verified `d^2=0`, and the first non-self-dual hook pair (`A_3`:
  `(3,1) \leftrightarrow (2,1,1)`) now has paired DS seed complexes with
  symbolic nilpotence checks. This has now been promoted to a family catalog:
  `compute/lib/ds_reduction.py` builds hook/subregular pair seeds for all
  type-A `(n,r)` hook cases up to a chosen cutoff, with propagated
  partition/level-shift checks and explicit alignment checks against the
  non-principal DS seed catalog.
- The generic hook/subregular DS catalogs now use an explicit type-A
  constraint-count ansatz derived from canonical hook `sl_2` triples
  (counting positive simple-root grades, with the proved `sl_3` subregular
  case anchored at count `2`), replacing the previous fixed-size
  placeholder sectors.
- The orbit layer now also carries explicit hook-pair profile records
  (`hook_orbit_pair_profile`, catalog + verification) in
  `compute/lib/nonprincipal_ds_orbits.py`, bundling source/dual partitions,
  orbit/centralizer dimensions, positive graded basis labels, and the same
  simple-root count data consumed by the DS sizing ansatz.
- The same orbit ledger now has a first non-hook scaffold too:
  type-A two-row non-hook cases are catalogued (`(n-s,s)` with `s \ge 2`),
  with partition/dual propagation, matrix/triple checks, and dimension
  identities; this extends the frontier beyond hook/subregular-only coverage.
- That non-hook orbit scaffold is no longer two-row-only:
  `compute/lib/nonprincipal_ds_orbits.py` now also enumerates the seeded
  general type-A non-principal catalog (`general_nonprincipal` partitions such
  as `(2,2,1)` and `(3,2,1)`), with the same matrix, `sl_2`-triple, dimension,
  and level-shift propagation checks on the broader seeded range.
- Non-principal level-shift propagation is now routed through an
  orbit-indexed data API (`nonprincipal_orbit_level_shift_type_a`) rather than
  a single hook-ansatz callsite, so future orbit-correction entries can be
  inserted per partition family without changing verifier wiring.
- The orbit-indexed correction table is no longer zero-only: seeded non-hook
  entries are now populated (for example `(4,2)`, `(3,3)`, `(3,2,1)` in type
  A), and a seeded transpose-invariant fallback now propagates this shift data
  through the broader non-hook seed catalog and orbit verifiers.
- The truncated seed complexes now expose cohomology dimensions explicitly:
  the subregular specialization (`\chi=(1,0)`) is acyclic
  (`H^0=H^1=H^2=0`), and both first-hook-pair specializations
  (`(1,0)` / `(0,1)`) are acyclic at the same truncated level. The new
  hook-family catalog also verifies acyclic nonzero-character specializations
  case-by-case at this truncated seed level.
- The `sl_3` subregular seed now also has an explicit surviving `g^f`
  strong-field profile in `compute/lib/ds_reduction.py`: the candidate basis
  `J \sim H_2 + \frac{1}{2}H_1`, `G^+ \sim E_{23}`, `G^- \sim F_{13}`,
  `T \sim F_{12}` centralizes `f = F_{12}` and has DS weights
  `(1, 3/2, 3/2, 2)`, matching the Bershadsky--Polyakov strong presentation.
  The same code now exposes the canonical splitting
  `\mathfrak{sl}_3 = [e,\mathfrak{sl}_3] \oplus \mathfrak{g}^f` and the
  corresponding projection from basis currents to the surviving strong fields.
  At the same linearized level, the projected survivor bracket is now
  explicit and matches the expected seed pattern
  `[J,G^\pm] = \pm \frac{3}{2} G^\pm`, `[G^+,G^-]=T`, `T` central.
- The orbit-combinatorial hook scaffold now also has matrix representatives:
  `compute/lib/nonprincipal_ds_orbits.py` builds standard nilpotent matrices
  for type-A hook partitions, recovers their Jordan types from kernel
  dimensions of powers, and checks their centralizer dimensions directly. In
  particular, the first genuine non-self-dual pair
  `(3,1) \leftrightarrow (2,1,1)` now exists as an explicit matrix-level seed.
  The same code now also produces explicit traceless centralizer bases for
  that pair, with dimensions `5` and `9`, and standard `sl_2` triples with
  explicit `ad(h)` grading multiplicities on `\mathfrak{sl}_4`. The positive
  graded basis labels are now explicit too, so the first hook pair has
  concrete candidate ghost directions at the orbit-data level. Those actual
  five positive directions are now used by the first hook-pair linear
  constraint blocks in `compute/lib/ds_reduction.py`, with explicit ghost
  conformal weights on both sides. The first hook-pair truncated exterior BRST
  seed now uses the same five directions as well.
- The same first hook pair now also has an explicit homogeneous
  `\mathfrak{g}^f` survivor basis and reduced bracket at the seed level:
  the source survivor DS weights are `(1,2,2,2,3)`, while the target survivor
  DS weights are `(1,1,1,1,3/2,3/2,3/2,3/2,2)`. Its positive sectors are also
  now explicitly non-abelian, so the hook-pair BRST problem has moved past the
  abelian toy regime: the quadratic ghost term is genuinely present. This is
  now encoded directly in first-hook-pair BRST blueprints in
  `compute/lib/ds_reduction.py`, together with explicit nonzero quadratic-ghost
  support entries.
- The first hook pair now also has the actual finite ghost-sector BRST
  complexes in compute, including the character term and the explicit
  quadratic `c c b` support. Both source and target satisfy `d^2=0` and are
  acyclic in all ghost degrees, and they are matched by an explicit canonical
  relabeling of the five positive directions.
- Beyond the pure ghost sector, `compute/lib/ds_reduction.py` now builds mixed
  fixed constraint-degree blocks on shifted currents `u_i`, `c`-ghosts, and
  `b`-ghosts. For the first hook pair these mixed blocks are verified through
  constraint degree `2`, and on both source and target they satisfy `d^2=0`
  and have zero cohomology in every available BRST degree. They also match
  under the same canonical source-to-target relabeling as the pure ghost
  complexes.
- The same mixed-block formalism now also covers the self-dual `sl_3`
  subregular seed through constraint degree `3`: the quadratic ghost term is
  absent there, and every tested mixed block is square-zero and acyclic.
- The mixed/nonlinear hook machinery is now family-level as well:
  `compute/lib/ds_reduction.py` exposes generic hook-pair APIs for constraints,
  positive-sector brackets, quadratic `c c b` support, current-action terms,
  and mixed/nonlinear `u-c-b` blocks for any type-A `(n,r)` hook pair (with
  explicit truncation controls).
- Family transpose-duality checks are now automated at block level:
  mixed and nonlinear hook-pair blocks are compared under dual swap
  (`r \leftrightarrow n-r-1`) via canonical side relabeling, and catalog-level
  verifiers now check this symmetry across the seeded type-A range.
- The survivor-coupled layer is now family-level as well:
  `compute/lib/ds_reduction.py` now exposes generic hook-pair survivor-action
  terms and survivor-coupled block builders, and the transpose-dual symmetry
  check is now lifted to survivor-coupled blocks through a dedicated catalog
  verifier (currently run on a tractable seeded range).
- This chain-level family machinery now extends beyond hooks:
  non-hook type-A two-row families are now wired through the same mixed,
  nonlinear, and survivor-coupled block builders, with canonical relabel /
  dual-swap verifiers on the seeded non-hook range; for the cheaper mixed and
  nonlinear sectors those two-row checks now run through `\mathfrak{sl}_9`.
- The same partition-pair machinery now reaches the next seeded
  `general_nonprincipal` family as well:
  small general type-A partitions (for example `(3,2,1)`) now run through the
  same mixed/nonlinear/survivor-coupled block builders, and the general mixed
  and nonlinear verification layer is now reduced by transpose symmetry, so
  those checks hold on a symmetry-reduced seeded range through size `9`; the
  same general survivor-coupled family-via-duality layer now also remains
  positive through size `12` in survivor degree `1` and through size `11`
  in survivor degree `2`.
- That generic partition-pair layer no longer stops at the survivor-coupled
  truncation. The same seeded two-row and `general_nonprincipal` families now
  carry witness-level survivor-action lifts, first-transfer correction data,
  internal survivor CE blocks, and corrected semidirect survivor blocks at the
  first tested truncation `(0,1,1)`. On that seeded non-hook range the naive
  semidirect coupling remains the obstruction test, while the corrected
  semidirect blocks restore `d^2=0` and satisfy the same dual-swap checks.
- The corrected semidirect non-hook verification layer is now sharper too:
  two-row families are checked by a one-pass seeded bundle through
  `\mathfrak{sl}_8` at the first corrected-semidirect truncation
  `(0,1,1)`; the same two-row family-via-duality layer now also remains
  positive in survivor degree `2` through `\mathfrak{sl}_8`, and the
  broader seeded `general_nonprincipal` family is
  now reduced by transpose symmetry, so at the first corrected semidirect
  truncation `(0,1,1)` explicit symmetry-reduced verification now reaches
  size `14` in survivor degree `1`; this now also runs as the stable seeded
  bundle after replacing repeated tall exact solves in the reduced
  survivor-bracket layer by a fixed row-minor solver and pruning
  semidirect branches that cannot contribute at internal CE cutoff `1`.
  The same
  general family-via-duality layer remains positive in survivor degree `2`
  through size `11`, rather than only on the first general seed.
- The first non-self-dual hook pair now also carries the first nonlinear
  current/OPE correction on top of those mixed `u-c-b` truncations: the
  `c \cdot \rho` action of the positive sector on shifted currents and
  `b`-ghosts, derived directly from the explicit positive-sector brackets.
  This current-action term is nontrivial, but through constraint degree `2`
  the resulting nonlinear mixed blocks still satisfy `d^2=0`, have zero
  cohomology in every available BRST degree, and match source-to-target under
  the same canonical relabeling. In the self-dual `sl_3` subregular control
  case the analogous nonlinear term vanishes because the constrained positive
  sector is abelian.
- The same truncation now also carries the first reduced survivor feedback:
  linear survivor degree is added, and the positive sector acts on survivor
  variables through the induced quotient action
  `\mathfrak{g}/[e,\mathfrak{g}] \cong \mathfrak{g}^f`. For the first
  non-self-dual hook pair this survivor-feedback term is genuinely nonzero
  (`6` source terms and `14` target terms), but the first tested
  survivor-coupled truncation (constraint degree `\le 1`, survivor degree `1`)
  is still square-zero and acyclic on both sides. In the self-dual
  `sl_3` subregular control case the survivor action is also explicit and the
  corresponding truncation remains square-zero and acyclic through constraint
  degree `2`.
- With the exact-rank path accelerated, the same first hook-pair
  survivor-coupled truncation is now checked at survivor degree `2`; it still
  collapses through constraint degree `1`.
- The next live obstruction is therefore the internal reduced `g^f` current /
  ghost sector itself. That layer is now explicit in compute as finite CE
  blocks on survivor polynomials plus survivor ghosts, built from the closed
  reduced survivor bracket table. Unlike the earlier survivor-coupled
  truncations, these blocks are square-zero but already have nonzero
  cohomology at survivor polynomial degree `1` on both the subregular control
  case and the first non-self-dual hook pair.
- The next attempted coupling is now also explicit and equally informative:
  the naive semidirect product of the positive-sector BRST layer with that
  internal survivor CE sector fails `d^2=0` already at the first tested
  truncations. The obstruction is concrete: the projected positive action on
  survivors is not a derivation of the reduced survivor bracket. Compute now
  exposes the derivation-defect tensors for both the subregular control case
  and the first non-self-dual hook pair.
- The subregular `sl_3` control case now has explicit witness-level transfer
  data beyond that obstruction: the positive survivor action is decomposed into
  projected terms plus chosen `[e,\mathfrak{g}]` witnesses, each derivation
  defect is recovered from an unreduced witness identity, and the first
  transferred cubic BRST correction is computed exactly. On that control case
  the correction cancels the naive reduced survivor action and restores
  `d^2=0` for the corrected semidirect truncation. The next frontier is to
  port this witness-based correction mechanism to the first genuinely
  non-self-dual hook pair.
- That first non-self-dual hook-pair step is now also in compute at first
  order: the derivation-coboundary equation on the survivor sector is solvable
  for every active positive ghost on both source and target. The resulting
  correction terms cancel the naive reduced survivor action completely, and the
  corrected semidirect survivor blocks restore `d^2=0` at the same low
  truncation where the naive quotient-level coupling failed.
- The hook side now has the first piece of that upgrade: compute records
  explicit hook-pair survivor-action lifts into projected plus `[e,g]` witness
  parts, and the hook-pair derivation defects are recovered from the same
  unreduced witness identity as in the subregular control case. That upgrade is
  now pushed one layer further: the first transferred correction itself is
  witness-driven, with explicit constrained-current preimages and survivor
  action lifts recorded termwise.
- Low-rank hook-family evidence is now sharper too: through `\mathfrak{sl}_7`
  every seeded hook pair in compute has all constrained currents `ad_e`-exact,
  and the witness-driven first transfer cancels the reduced survivor action on
  both source and target sides.
- The corrected semidirect picture is also no longer restricted to the first
  non-self-dual pair: at the first tested truncation
  `(0,1,1)` the corrected semidirect hook blocks are square-zero for every hook
  orientation through `\mathfrak{sl}_6`, and those corrected semidirect blocks
  satisfy dual-swap symmetry through the same range.
- The next hook rank is now also controlled in a sharper symmetry-reduced
  form: `\mathfrak{sl}_7` has first-transfer cancellation on every hook
  orientation, and the corrected semidirect truncation at `(0,1,1)` is
  verified for the full hook family by square-zero checks on the half-catalog
  `r=1,2,3` together with dual-swap checks on the nontrivial pairs `r=1,2`.
- The next rank is now open in compute as well: after replacing repeated exact
  ambient-coordinate projection solves with cached traceless-basis inverses,
  `\mathfrak{sl}_8` now has first-transfer cancellation on every hook
  orientation, and the corrected semidirect truncation at `(0,1,1)` is
  verified for the full hook family by half-catalog square-zero checks
  `r=1,2,3` together with dual-swap checks on those same three nontrivial
  pairs.
- The same optimization now pushes the semidirect hook-family evidence one rank
  further: `\mathfrak{sl}_9` satisfies the corrected semidirect check at
  `(0,1,1)` for the full hook family, via square-zero on the half-catalog
  `r=1,2,3,4` and dual-swap on the nontrivial pairs `r=1,2,3`. Beyond that,
  the first-transfer layer is already explicitly positive on the extreme hook
  `r=1`.
- The family boundary has now moved once more: `\mathfrak{sl}_{10}` satisfies
  the corrected semidirect check at `(0,1,1)` for the full hook family, via
  square-zero on the half-catalog `r=1,2,3,4` and dual-swap on the nontrivial
  pairs `r=1,2,3`, and its first-transfer layer is positive on every hook
  orientation `r=1,\dots,8`.
- The same frontier is now open one rank further again: after fixing a
  high-rank basis-label collision in the standard traceless orbit basis,
  `\mathfrak{sl}_{11}` satisfies the corrected semidirect check at `(0,1,1)`
  for the full hook family, via square-zero on the half-catalog
  `r=1,2,3,4,5` and dual-swap on the nontrivial pairs `r=1,2,3,4`, and its
  first-transfer layer is positive on every hook orientation `r=1,\dots,9`.
  The next scaling limit is the transpose-dual comparison itself rather than
  the survivor-projection step.
- One step past that family boundary is already computationally open: the
  extreme hook `(\mathfrak{sl}_{12}, r=1)` has positive first-transfer
  cancellation, corrected semidirect square-zero at `(0,1,1)`, and positive
  transpose-dual comparison, and the next interior hook `r=2` already has
  positive first-transfer cancellation and corrected semidirect square-zero at
  the same truncation. The remaining `\mathfrak{sl}_{12}` question is
  therefore the rest of the half-catalog, not whether the rank opens at all.
- That question is now resolved at the same truncation. After replacing the
  semidirect dual-swap comparison path by relabeled block-spec comparison
  rather than full BRST-block reconstruction, `\mathfrak{sl}_{12}` satisfies
  the corrected semidirect check at `(0,1,1)` for the full hook family, via
  half-catalog square-zero on `r=1,2,3,4,5` and dual-swap on the nontrivial
  pairs `r=1,2,3,4,5`, and its first-transfer layer is positive on every hook
  orientation `r=1,\dots,10`. The live family frontier is now
  `\mathfrak{sl}_{13}`.
- The same frontier has now moved one rank further again. After replacing the
  remaining projector bottlenecks by direct standard-basis coordinate
  extraction, one-pass `[e,g]` basis pivot extraction, and sparse basis-column
  assembly, `\mathfrak{sl}_{13}` satisfies the corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog: square-zero on `r=1,2,3,4,5,6`,
  dual-swap on the nontrivial pairs `r=1,2,3,4,5`, and first-transfer
  cancellation on the same half-catalog `r=1,\dots,6`. The live family
  frontier is now `\mathfrak{sl}_{14}`.
- One step beyond that written boundary is already positive in compute:
  `\mathfrak{sl}_{14}` now satisfies the corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog `r=1,\dots,6`, with positive
  transpose-dual comparison on the nontrivial pairs and first-transfer
  cancellation on the same half-catalog. The live family frontier is now
  `\mathfrak{sl}_{15}`.
- The next rank is already computationally open at low depth:
  `\mathfrak{sl}_{15}` now satisfies the corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog `r=1,\dots,7`, with positive
  transpose-dual comparison on the nontrivial pairs and first-transfer
  cancellation on the same half-catalog. The live family frontier is now
  `\mathfrak{sl}_{16}`.
- One step beyond that written boundary is already open at low depth:
  `\mathfrak{sl}_{16}` now satisfies the corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog `r=1,\dots,7`, with positive
  transpose-dual comparison on the nontrivial pairs and first-transfer
  cancellation on the same half-catalog. The live family frontier is now
  `\mathfrak{sl}_{17}`.
- The next rank is already computationally open at low depth:
  `\mathfrak{sl}_{17}` now satisfies the corrected semidirect check at
  `(0,1,1)` on the full hook half-catalog `r=1,\dots,8`, with positive
  transpose-dual comparison on the nontrivial pairs and first-transfer
  cancellation on the same half-catalog. The next live family target is now
  `\mathfrak{sl}_{18}`.
- That target is now fully closed at the same truncation:
  `\mathfrak{sl}_{18}` satisfies the corrected semidirect check at `(0,1,1)`
  on the full hook half-catalog `r=1,\dots,8`, with positive
  transpose-dual comparison on the nontrivial pairs and first-transfer
  cancellation on the same half-catalog. The next live family target is now
  `\mathfrak{sl}_{19}`.
- One step beyond that written boundary is now fully closed too:
  `\mathfrak{sl}_{19}` satisfies the corrected semidirect check at `(0,1,1)`
  on the full hook half-catalog `r=1,\dots,9`, with positive
  transpose-dual comparison on the nontrivial pairs and first-transfer
  cancellation on the same half-catalog. The next live family target is now
  `\mathfrak{sl}_{20}`.
- One step beyond that new written boundary is already open at the extreme
  hook: `\mathfrak{sl}_{20}, r=1` satisfies first-transfer cancellation and
  corrected semidirect square-zero at `(0,1,1)`.

#### 9. W_N (General)

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **Finite-type theorem + low-weight support** | Principal finite-type `W`-algebras now satisfy all-genera PBW concentration. The proof uses the unique weight-2 stress tensor and the upper-triangular `d_2` weight argument, with explicit low-weight support from the `W_3` vacuum-module computation. No explicit high-degree bar differential for `N >= 4` yet. |
| Genus pipeline | **Theorem-level for all g** | `kappa = c * sum_{j=2}^N 1/j`, and the higher-genus obstruction theory is unconditional on the principal finite-type locus. |
| Module category | **None** | Only the abstract theorem. |
| Spectral sequence | **E_2 collapse proved for generic principal finite-type W** | Explicit `W_3` checks plus the generator-weight argument identify an invertible diagonal `L_0` term and strictly weight-raising off-diagonal higher-spin contributions. |

**Gaps**:
- No explicit high-degree bar differential or bar-cohomology table for `N >= 4`.
- No module Koszul duality for principal `W_N` modules.
- The live `W` frontier has moved to the filtered H-level / factorization realization packages for `W_\infty` and to the distinct three-packet non-principal orbit frontier (dual-orbit input, orbit-indexed level shift, paired DS seed transport/globalization), not finite-type PBW degeneration; the standard completed M-level principal-stage package is already theorematic.
- On the `W_\infty` side, the exact MC4 task is now the residue-identity
  package `C^{res}_{s,t;u;m,n}(N)=C^{DS}_{s,t;u;m,n}(N)`, detected from
  the finite primary seed set and translation closure.

#### 10. Yangian Y(sl_2)

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **deg 1-3 explicit, deg 4-5 MISSING** | Dimensions: 4, 10, 28, ---, ---. RTT bar complex computed (thm:yangian-bar-rtt). Koszul dual identified as Y_{R^{-1}} (thm:yangian-koszul-dual). |
| Genus pipeline | **None** | kappa not defined (E_1-chiral, no standard genus expansion). The manuscript notes this is a "significant open problem" (rem:toroidal-three-theorems). |
| Module category | **Moderate** | Evaluation modules, R-matrix braiding, module Koszul duality (prop:yangian-module-koszul). |
| Spectral sequence | **E_2 collapse CONJECTURED** | The Koszulness is proved (prop:yangian-koszul) but the E_2 collapse for the chiral bar complex spectral sequence is only conjectured (rem:yangian-collapse-conj). |

**Gaps**:
- **Major gap**: Degrees 4 and 5 of the bar complex are missing.
- **Major gap**: No genus expansion at all. The E_1-chiral genus theory is undeveloped.
- The spectral sequence collapse is conjectured, not proved, for the chiral bar complex.
- Only sl_2 is computed; no explicit computation for Y(sl_N) with N >= 3.
- The dg-shifted/factorization MC4 frontier is no longer generic
  completion rhetoric: the exact open task is the kernel-identity
  package `K^{line}_{a,b}(N)=K^{RTT}_{a,b}(N)`, with finite detection on
  tensor products of fundamental evaluation modules.

#### 11. Toroidal/Elliptic Algebras

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **Only the Fay d^2 = 0 proof** | The elliptic bar complex nilpotency is proved (prop:fay-implies-d-squared). No explicit bar complex dimensions. |
| Genus pipeline | **None** | All three main theorems are "expected" forms only (rem:toroidal-three-theorems). |
| Module category | **Definitions only** | Elliptic quantum group defined (def:elliptic-quantum). No module Koszul duality. |
| Spectral sequence | **Not analyzed** | |

**Gaps**: Almost everything. The E_1-chiral structure itself is only conjectured (thm:toroidal-e1). The Koszul dual is conjectured (conj:toroidal-koszul-dual). The bar complex has not been computed at any explicit degree.

#### 12. Lattice VOA (V_Lambda)

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **Inherited from Heisenberg** | Via Kunneth theorem. Lattice vertex operators do not contribute to curvature. |
| Genus pipeline | **F_g for all g** | F_g(V_Lambda) = d * lambda_g^FP, depending only on rank(Lambda). |
| Module category | **Moderate** | Lattice module theory, discriminant group, Siegel theta series. Frenkel-Kac-Segal identification proved. |
| Spectral sequence | **E_1 collapse** | Heisenberg sector acyclic. |

**Gaps**: The bar complex of the lattice vertex operator sector (beyond the Heisenberg sector) is not computed. The lattice theta function contribution to genus >= 2 partition functions is discussed but not connected to the bar complex.

#### 13. Deformation Quantization

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **Abstract only** | Chiral Kontsevich theorem stated (thm:chiral-kontsevich). No explicit bar complex for specific Poisson manifolds. |
| Genus pipeline | **None** | |
| Module category | **None** | |
| Spectral sequence | **Not analyzed** | |

**Gaps**: No explicit computation for any specific Poisson manifold/variety. The chiral Kontsevich formality (all-orders Stokes convergence) is conjectured. No worked example of deformation quantization through the bar-cobar machinery.

---

### Summary of Specific Computational Gaps

#### Bar Complex Dimension Gaps (from Master Table)

| Algebra | Missing degrees | Priority |
|---------|----------------|----------|
| hat{sl}_3 | deg 4, deg 5 | HIGH -- first non-abelian example beyond sl_2 |
| W_3 | deg 5 | MEDIUM -- degree 4 is done |
| Yangian Y(sl_2) | deg 4, deg 5 | HIGH -- only E_1-chiral example with computations |
| hat{E}_8 | all degrees | LOW -- very large dimensions make this hard |
| Toroidal | all degrees | LOW -- E_1 structure not proved |

#### Genus Pipeline Gaps

| Algebra | Status | Gap |
|---------|--------|-----|
| hat{sl}_3 | Formula only | No "Three Theorems in Action" showcase |
| W_3 | Formula only | No explicit genus-3 value |
| Yangian | None | E_1 genus theory undeveloped |
| Toroidal | None | E_1 genus theory undeveloped |
| Deformation quantization | None | No genus expansion at all |

#### Module Category Gaps

| Algebra | Status | Gap |
|---------|--------|-----|
| Heisenberg | Minimal | Module Koszul duality not developed |
| Virasoro | Moderate | Verma module Koszul duality not developed |
| W_3 | Minimal | No module theory |
| hat{E}_8 | None | No module theory |
| W_N (N >= 4) | None | No module theory |
| Toroidal/Elliptic | Definitions only | No module Koszul duality |

#### Spectral Sequence Gaps

| Algebra | Gap |
|---------|-----|
| Yangian | E_2 collapse only conjectured for chiral bar complex |
| Toroidal | Not analyzed |
| Deformation quantization | Not analyzed |

---

### Priority Ranking of Gaps

**Tier 1 (highest priority -- would most strengthen the manuscript)**:
1. hat{sl}_3 bar complex at degrees 4-5 (fills the most visible gap in the Master Table for a core example)
2. Yangian bar complex at degrees 4-5 (fills the gap for the only E_1-chiral example)
3. Module Koszul duality for Virasoro Verma modules (natural test case, high visibility)

**Tier 2 (medium priority)**:
4. W_3 bar complex at degree 5
5. "Three Theorems in Action" showcase for hat{sl}_3
6. Heisenberg module Koszul duality
7. Explicit deformation quantization example (specific Poisson manifold through bar-cobar)

**Tier 3 (lower priority or dependent on open problems)**:
8. hat{E}_8 explicit bar complex
9. E_1 genus theory for Yangians (requires new theory)
10. Toroidal algebra E_1-chiral structure (requires proving the conjectured structure)
11. Derived bc-betagamma system (Conjecture conj:extended-ferm-ghost)

---

### Connections Between Frontier References and Gaps

| Reference | Most relevant gap it could help fill |
|-----------|--------------------------------------|
| Mok25 (Log FM) | Genus pipeline via degeneration formulas; bar complex on punctured curves |
| CDG20 (Boundary chiral) | New examples of Koszul dual pairs from boundary conditions; module categories |
| DNP25 (Line operators) | Yangian bar complex; module Koszul duality; E_1-chiral computations |
| GKW24 (Higher operations) | Bar complex differentials via Feynman diagrams; explicit m_k computations |
| Zeng23 (Celestial) | Large-N Koszul duality; A_infinity computations on CR cohomology |
| KhanZeng25 (PVA sigma model) | Deformation quantization examples; Virasoro/W-algebra genus expansion from 3d gravity |
