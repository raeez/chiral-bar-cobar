# Frontier References and Computational Gap Analysis

Generated: 2026-03-05

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
- **Non-renormalization Theorem 4.1**: The OPE of line operators is computed exactly at tree level (1-loop exact).
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
- The non-renormalization theorem parallels the spectral sequence collapse at E_2 (the Koszul property).
- The A_infinity Yang-Baxter equation for r(z) is the E_1 analog of the curved A_infinity structure in the manuscript's framework.

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
- The Feynman diagram framework provides the physics realization of the bar complex differential: each Feynman diagram corresponds to a residue computation on the FM compactification.
- The L_infinity structure from eta^2 = 0 is the same as the A_infinity structure on the bar complex (with L_infinity being the commutative/Lie version).
- The non-renormalization theorem corresponds to the spectral sequence collapse at E_2 in the Koszul setting.
- The operatope geometry may provide a new perspective on the FM compactification and its stratification.

**potential_new_examples**:
- Explicit Feynman diagram computations of bar complex differentials for interacting theories (beyond free fields and Kac-Moody).
- Higher operations (m_k for k >= 3) computed via Feynman diagrams, providing data for the curved A_infinity structure.
- Operatope compactifications as alternatives to FM compactifications for specific diagram topologies.

**would_need**:
- A precise dictionary between GKW's Feynman diagrams and the manuscript's residue computations on FM spaces.
- Verification that the L_infinity structure matches the bar complex differential in specific examples.
- Understanding when the non-renormalization theorem (1-loop exactness) corresponds to Koszulness.

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
| Module category | **Moderate** | Minimal models via coset (ex:minimal-coset). Module Koszul duality for Vir not explicitly developed (only the algebra-level duality Vir_c <-> Vir_{26-c}). |
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
- The non-principal nilpotent case (Conjecture conj:w-orbit-duality) remains open.

#### 9. W_N (General)

| Computation | Status | Details |
|-------------|--------|---------|
| Bar complex | **Only abstract** | Via W-algebra Koszul main theorem. No explicit computation for N >= 4. |
| Genus pipeline | **Via universality** | kappa = c * sum_{j=2}^N 1/j. |
| Module category | **None** | Only the abstract theorem. |
| Spectral sequence | **Claimed via universal theorem** | No explicit verification for N >= 4. |

**Gaps**: Essentially the same situation as hat{E}_8 -- a formula row with no worked computation behind it for N >= 4.

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
