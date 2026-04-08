# Frontier Research Questions

Eight open problems at the boundary of the seven-face programme. Each entry states the conjecture, the evidence, the obstruction, and the minimal input that would resolve it.

## 1. Spectral proof of Theorem B via Bethe completeness

**Conjecture.** Bar-cobar inversion (Theorem B) for affine Kac-Moody algebras admits a spectral proof: the Bethe ansatz eigenstates of the Gaudin model on evaluation modules span the full tensor product, and this completeness is equivalent to the bar-cobar quasi-isomorphism.

**Evidence.** The Gaudin-Yangian identification (Theorem thm:gaudin-yangian-identification) establishes that the GZ26 commuting Hamiltonians are the Gaudin Hamiltonians of the dg-shifted Yangian. The Bethe ansatz equations for the sl\_2 Gaudin model at n=3,4 points are solved explicitly in `theorem_bv_bethe_gaudin_frontier_engine.py` (68 tests), and the eigenvalues match exact diagonalization. Mukhin-Tarasov-Varchenko proved Bethe completeness for finite-dimensional g-modules.

**Obstruction.** The chiral bar complex involves infinite-dimensional modules (Verma modules, Fock spaces). MTV completeness applies to finite-dimensional modules only. Three specific difficulties: (a) the Bethe equations become transcendental for infinite-dimensional representations, (b) spectral simplicity fails at resonant levels, (c) the critical level k = -h^v is a wall where the Gaudin model degenerates.

**Minimal input.** Prove Bethe completeness for weight-graded tensor products of Verma modules by reducing weight-by-weight to the finite-dimensional case (exploiting the weight-space finiteness of chirally Koszul algebras). The weight-truncated Bethe completeness would give a spectral-sequence proof of Theorem B that converges arity-by-arity.

**Physics.** The Bethe-completeness approach connects bar-cobar inversion to the Feigin-Frenkel-Reshetikhin programme via opers: Bethe completeness for the Gaudin model is equivalent to the surjectivity of the Miura oper map, which is a theorem of Frenkel (2005) for generic levels. The spectral proof of Theorem B would embed bar-cobar inversion into geometric Langlands.

## 2. Seven-face categorification as a 2-functor

**Conjecture.** The seven faces of r(z) are seven 1-morphisms in a 2-category ChirKos\_2, and the seven-way agreement is a system of coherent 2-isomorphisms satisfying hexagonal coherence.

**Evidence.** The seven-face master theorem establishes agreement at the level of objects. The categorification engine (`theorem_seven_face_categorification_engine.py`, 89 tests) verifies functoriality for each face, natural isomorphism existence for all 21 pairs, and coherence for all 35 transitivity triples. DS reduction is functorial for faces 1, 5, 7.

**Obstruction.** The seven categories live in different mathematical worlds: the bar-cobar category is a model category of dg coalgebras, the Yangian category is a braided monoidal category of representations, the Gaudin category is a category of D-modules on configuration spaces. No existing framework addresses seven simultaneous functors with the required coherence.

**Minimal input.** Prove 2-functorial coherence for the triangle F1-F5-F7 (bar-cobar, Yangian, Gaudin). This triangle is the most tractable because all three are algebraic. The Lurie-Haugseng framework for enriched infinity-categories provides the ambient setting; the specific content is the construction of a natural 2-isomorphism between the composite F5 ∘ F1^{-1} and F7.

**Physics.** The 2-categorical structure encodes the physical statement that line operators in 3d holomorphic-topological QFT form a braided monoidal 2-category (the Kapustin-Rozansky-Witten structure). The seven faces are seven ways of extracting the braiding data from the bar complex.

## 3. Shifted-symplectic complementarity via the Sklyanin bracket

**Conjecture.** The (-1)-shifted symplectic structure on the complementarity stack T\_comp(A) (Theorem C) is the derived-geometric lift of the Sklyanin Poisson bracket on (g!)^\*, and the complementarity decomposition Q\_g(A) + Q\_g(A!) = H\*(M-bar\_g, Z(A)) is the Lagrangian intersection of two Lagrangian subvarieties in T\_comp(A).

**Evidence.** The Sklyanin Poisson cohomology for sl\_2 vanishes: H²\_π(sl\_2\*, {,}\_{STS}) = 0 (`theorem_sklyanin_poisson_cohomology_engine.py`, 57 tests). This proves infinitesimal rigidity of the Sklyanin bracket, the genus-0 arity-2 shadow of the (-1)-shifted structure. The complementarity sum κ + κ' = 0 for KM and κ + κ' = 13 for Virasoro (AP24) constrains the global structure.

**Obstruction.** The connection requires the PTVV shifted-symplectic geometry applied to the convolution dg Lie algebra setting. The convolution algebra g^mod\_A is a pro-nilpotent dg Lie algebra whose MC moduli is a formal derived stack. The passage from Sklyanin (genus 0, arity 2) to PTVV (all genera, all arities) requires the Kontsevich-Pridham correspondence at the modular level.

**Minimal input.** Show that the Sklyanin bracket is the genus-0 reduction of the PTVV shifted-symplectic structure on MC(g^mod\_A) via the CPTVV framework. Then derive the nondegeneracy hypothesis (H2) of Theorem C from Sklyanin nondegeneracy (H²\_π = 0).

**Physics.** The (-1)-shifted symplectic structure is the BV structure of the 3d holomorphic-topological sigma model. The complementarity decomposition is the BV antibracket pairing between the boundary algebra A and its Koszul dual A!. The Lagrangian intersection computes the partition function of the bulk theory as a state in the boundary Hilbert space.

## 4. Higher-genus seven faces beyond genus 1

**Conjecture.** At genus g ≥ 2, the genus-g collision residue r\_A^{(g)}(z\_1,...,z\_n; Σ\_g) on a genus-g surface Σ\_g has seven equivalent realizations generalizing the genus-0 and genus-1 cases.

**Evidence.** Genus 0: proved (seven-face master theorem, 72 tests). Genus 1: proved for affine KM (thm:g1sf-master), with the KZB connection, elliptic r-matrix, and elliptic Gaudin all agreeing. The genus-1 Virasoro collision residue involves ζ, ℘, ℘' (higher-order elliptic operators, genuinely new).

**Obstruction.** At genus ≥ 2, the bar propagator becomes the Szegő kernel on Σ\_g, which depends on a choice of spin structure. The period matrix τ ∈ H\_g replaces the single modular parameter τ of genus 1. The theory of automorphic r-matrices does not exist beyond genus 1.

**Minimal input for genus 2.** Construct the genus-2 KZB connection via Enriquez's framework for flat connections on configuration spaces of algebraic curves. Prove a genus-2 Drinfeld-Kohno theorem identifying the monodromy with the quantum group.

**Physics.** The genus-g seven-face identification encodes the partition function of the 3d holomorphic-topological theory on Σ\_g × ℝ. The genus-2 case controls the first nontrivial gravitational correction beyond the torus. The Hodge-bundle curvature κ · ω\_g is the modular anomaly that measures the failure of genus-g factorization.

## 5. Koszulness from Sklyanin for classes C and M

**Conjecture.** The vanishing H²\_π = 0 of the Poisson cohomology associated to the collision residue implies chiral Koszulness for all standard families, including classes C (βγ) and M (Virasoro, W\_N).

**Evidence.** Proved for classes G and L via Whitehead's second lemma (thm:koszulness-from-sklyanin, 57 tests).

**Obstruction.** For class M, the collision residue r(z) = (c/2)/z³ + 2T/z has poles of order 3. The resulting Sklyanin bracket is a differential Poisson bracket of order 2. The Lichnerowicz-Poisson complex for such brackets is non-standard, and Whitehead's lemma does not apply. For class C, the collision residue vanishes (k\_max = 0), so the Sklyanin bracket is trivial; Koszulness comes from the quartic contact invariant at arity 4, invisible to genus-0 arity-2 data.

**Minimal input.** Develop a theory of differential Poisson cohomology for brackets of order ≥ 2. Compute H² for the Virasoro-type bracket on ℂ. Alternatively, develop a "charged Sklyanin bracket" incorporating higher-arity shadow data.

**Physics.** The differential Poisson brackets arise from higher-spin currents in the 3d HT theory. The Virasoro bracket involves the stress tensor (spin 2), with OPE pole order 4. The W\_N brackets involve spin-N currents with pole order 2N. The deformation quantization of these brackets is the vertex algebra quantization problem for higher-spin theories.

## 6. Multi-weight genus ≥ 5

**Status.** The genus-g free energy for multi-weight algebras decomposes as F\_g(A) = κ · λ\_g^FP + δ\_pf^{(g,0)} + δF\_g^cross. Computed exactly at genera 2 (73 tests), 3 (43 tests), 4 (57 tests). Growth: δF\_g / δF\_{g-1} grows factorially.

**What is open.** Genus ≥ 5 requires enumerating > 2000 stable graphs. The computation is algorithmic. The conceptual question: does δF\_g^cross have a closed-form generating function?

**Physics.** The factorial growth is the multi-weight analogue of the (2g)! divergence of the bosonic string partition function. The generating function (if it exists) encodes the resurgent structure of the multi-weight partition function.

## 7. Non-principal W-algebras beyond hook type

**Status.** Hook-type transport duality established for type A. BP algebra self-dual with K\_BP = 196 (63 tests). The sl\_5 partition (3,2) is the minimal non-hook test case (39 tests): 8 strong generators, centralizer dim 8, Koszul dual conjectural.

**What is open.** Is (W\_k(sl\_5, f\_{(3,2)}))^! a W-algebra? The transpose partition (2,2,1) is also non-hook. The minimal test: compute bar cohomology H\*(B(W\_k(sl\_5, f\_{(3,2)}))) at low arity.

**Physics.** Non-hook W-algebras arise from boundary conditions in 4d N=2 gauge theories with non-regular punctures (Gaiotto's class S programme). Their Koszul duality controls Coulomb-branch/Higgs-branch duality for these theories.

## 8. BV/BRST = bar at genus ≥ 2 for interacting theories

**Status.** Proved at genus 0 universally. At genus 1: scalar match for all families (59 tests); chain-level for classes G and L (62 tests). The decisive genus-2 test value: F\_2^bar(sl\_2, k=1) = 21469/69120 (63 tests). The 7 stable graphs and their BV Feynman rules are documented (75 tests).

**What is open.** Computing the BV 2-loop integral on M-bar\_{2,0} × ℝ for holomorphic Chern-Simons. This requires the genus-2 Szegő kernel, the CS vertex, and integration over the 5-dimensional moduli space.

**Physics.** BV/BRST = bar at genus g is the statement that perturbative quantization of the 3d HT sigma model on Σ\_g × ℝ is equivalent to the algebraic bar complex. If proved, it eliminates path-integral methods at higher genus, replacing them with algebraic computation.
