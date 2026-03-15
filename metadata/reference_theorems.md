# Reference Theorem Extraction — Chiral Bar-Cobar Monograph

Generated: 2026-03-05

**Purpose**: Identify usable theorems from 10 reference PDFs that could combine with the manuscript's three main proved theorems:
- **(A)** Geometric Bar-Cobar Duality (thm:bar-cobar-isomorphism-main)
- **(B)** Bar-Cobar Inversion (thm:higher-genus-inversion)
- **(C)** Deformation-Obstruction Complementarity (thm:quantum-complementarity-main)

---

## TIER 1 (Read in full)

---

### AF15 — Ayala-Francis, "A Factorization Homology Primer" (53 pp)

**Current citation status**: Heavily cited (~20 citations). Used for factorization homology framework, Weiss covers, NAP duality. Specific theorems cited: Thm 4.5, Thm 4.19, Thm 5.1.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Prop 6.9** (cofiltration of FH) | For an augmented n-disk algebra A, there is a natural cofiltration of the factorization homology int_M A whose associated graded is Conf_k(M) tensor_{Sigma_k} LA^{otimes k}, where LA is the (derived) indecomposables. | M framed n-manifold, A augmented E_n-algebra | **(A)+(B)**: The cofiltration provides a spectral sequence from configuration space homology with coefficients in indecomposables to factorization homology. This is exactly the genus-0 bar filtration. Could make the bar complex spectral sequence (Thm B) more explicit by identifying E_1 page with Conf_k(X) tensor (s^{-1}A-bar)^{otimes k}. | **NO** | **HIGH** |
| 2 | **Prop 6.12** (Goodwillie derivatives) | The k-th Goodwillie derivative of factorization homology as a functor of algebras is partial_k(int_M -) = Conf_k(M) tensor Sigma_k^{triv}. | M framed n-manifold | **(A)**: Identifies configuration spaces as Goodwillie derivatives of factorization homology. This gives a conceptual explanation for why bar construction involves configuration spaces: it IS the Goodwillie tower of int_M. | **NO** | **HIGH** |
| 3 | **Thm 7.8** (Poincare/Koszul duality) | For A an augmented n-disk algebra satisfying finiteness, (int_M A)^vee = int_M MC_A where MC_A is the Maurer-Cartan algebra (Koszul dual). | A nilpotent, M closed n-manifold | **(A)+(C)**: This is the topological shadow of Theorem A. The chiral bar-cobar duality geometrizes this by replacing E_n-algebras with chiral algebras and n-manifolds with algebraic curves. Combining: for X a smooth proper curve, (int_X A)^vee = int_X A^! (up to twists). | Cited indirectly (in concordance.tex) | **HIGH** |
| 4 | **Prop 8.27** (defect algebras) | For a stratified manifold M with a defect along a submanifold N, the factorization homology decomposes into bulk and defect contributions. The defect algebra is an E_{n-k}-algebra (k = codimension). | Stratified manifold, compatible algebra | **(C)**: Defect algebras provide a geometric mechanism for quantum corrections. The defect along the diagonal in M x M is an E_1-algebra whose deformations could be identified with the genus-1 corrections in Theorem C. | **NO** | **MEDIUM** |
| 5 | **Cor 8.30** (nested E_i structure) | For M an n-manifold with nested submanifolds M_1 subset M_2 subset ... subset M, factorization homology carries compatible E_{n-dim(M_i)} structures. | Nested stratification | **(A)**: Relevant to the separate topological `E_n` ladder by explaining how a curve inside a real surface carries nested little-disks structure. It should be used to clarify the `n=2` topological shadow of the curve-level bar complex, not to derive the internal `E_1`/`E_∞`-chiral hierarchy from manifold dimension. | **NO** | **MEDIUM** |
| 6 | **Thm 8.25** (characterization) | Factorization homology is characterized as the unique homology theory for E_n-algebras satisfying excision (otimes-excision). | E_n-algebra valued in a tensor category | **(B)**: Could be used to show that the bar-cobar construction is the UNIQUE construction satisfying certain axioms. If Omega(B(A)) -> A is the unit of the unique adjunction satisfying excision, this gives a stronger form of Theorem B. | Cited implicitly | **MEDIUM** |

---

### FG12 — Francis-Gaitsgory, "Chiral Koszul Duality" (43 pp)

**Current citation status**: Heavily cited (~25 citations). The manuscript's foundational reference for chiral Lie/Com duality.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Thm 5.1.1** (C^ch = Prim^ch[-1]) | The chiral commutative envelope functor and chiral primitive functor form an equivalence: C^ch: chirLie-alg_{Ran} <-> chirCom-coalg_{Ran}^{conil}: Prim^ch[-1]. | Ran space formulation, pro-nilpotent/ind-nilpotent | **(A)**: This is the genus-0, chirLie-chirCom specialization of Theorem A. The manuscript's Theorem A generalizes to chirAss (E_1-chiral) and to higher genus. Combining: Thm 5.1.1 is the associated graded of Thm A under PBW filtration. This comparison is stated in concordance.tex but could be made into a theorem. | **YES** (concordance.tex) | **MEDIUM** |
| 2 | **Thm 5.2.1** (factorization criterion) | An ind-scheme Y on Ran(X) is a chiral commutative coalgebra iff Y is a factorization ind-scheme (i.e., Y(I) = prod_{i in I} Y({i}) for I-colored Ran). | ind-scheme on Ran | **(A)**: Provides a geometric criterion for when the output of bar construction is a factorization coalgebra. Could be combined with Thm A to give a factorization criterion for bar-cobar equivalence. | **NO** | **MEDIUM** |
| 3 | **Prop 4.1.2** (KD equivalence) | The Koszul duality functor KD: chirLie-alg_{Ran}^{pro-nilp} -> chirCom-coalg_{Ran}^{ind-nilp} is an equivalence of infinity-categories. | Pro-nilpotent/ind-nilpotent categories | **(A)**: The categorical setting (pro-nilpotent algebras <-> ind-nilpotent coalgebras) is precisely the setting where Theorem A gives an equivalence (not just adjunction). This could sharpen the Koszulness hypothesis in Thm A. | **YES** (implicitly in bar_cobar_construction.tex) | **MEDIUM** |
| 4 | **Cor 6.5.2** (PBW for chiral envelopes) | For a chiral Lie algebra L, there is a PBW filtration on the chiral universal envelope U^ch(L) with associated graded Sym^ch(L). | L a chirLie algebra on X | **(A)+(B)**: The PBW filtration on U^ch(L) induces a filtration on B(U^ch(L)) whose associated graded is B(Sym^ch(L)). Combined with Thm B, this gives a filtered quasi-isomorphism Omega(B(U^ch(L))) -> U^ch(L). The spectral sequence of this filtration degenerates at E_2 for Koszul L. | **NO** | **HIGH** |
| 5 | **Prop 7.1.6** (module KD) | For L a chiral Lie algebra and C = C^ch(L) its chiral commutative envelope, there is a KD functor KD_mod: L-mod^{pro-nilp}_{Ran} -> C-comod^{ind-nilp}_{Ran}. | Pro-nilpotent L-modules | **(A)**: Extends bar-cobar duality to module categories. Combined with Theorem A, this gives: for Koszul A, Mod_A^{pro-nilp} = Comod_{A^!}^{ind-nilp}. This is exactly the module Koszul duality in chiral_modules.tex. | **YES** (chiral_modules.tex) | **MEDIUM** |
| 6 | **Cor 7.1.8** (module KD equivalence) | Under Koszulness, KD_mod is an equivalence. | L Koszul, pro-nilpotent modules | **(A)**: Combined with Thm A, gives the full module-level bar-cobar equivalence. | **YES** (cited as PE in chiral_modules.tex) | **LOW** |
| 7 | **Cor 7.3.2** (chiral modules = factorization comodules) | Chiral L-modules on Ran(X) are equivalent to factorization C-comodules. | L chirLie, C = C^ch(L) | **(A)**: Provides the factorization-algebraic interpretation of the module Koszul duality. Not currently used to strengthen the module story. | **NO** | **MEDIUM** |
| 8 | **Thm 5.2.1 + Prop 4.3.1** (formal moduli) | The chiral Koszul duality functor identifies pro-nilpotent chiral Lie algebras with formal moduli problems on Ran(X). | Augmented chirLie algebras | **(C)**: Deformation-obstruction theory (Thm C) can be recast as a statement about formal moduli problems on Ran(X). The quantum corrections Q_g(A) parametrize a formal moduli problem whose tangent complex is controlled by A^!. | **NO** | **HIGH** |

---

### GeK98 — Getzler-Kapranov, "Modular Operads" (40 pp read)

**Current citation status**: Moderately cited (~12 citations). Used for modular operad definition, Feynman transform, boundary stratification.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Thm 5.4** (Feynman transform involution) | F_{D^vee} F_D A -> A is a weak equivalence for any modular D-algebra A with D a modular operad. | D a modular operad, A a D-algebra satisfying finiteness | **(B)**: This is the operadic statement underlying Theorem B. The Feynman transform F_D plays the role of bar, and F_{D^vee} plays cobar. The involutivity F_{D^vee} F_D = id is exactly Omega(B(A)) = A at the operadic level. Currently used implicitly but not cited for this specific theorem. | **NO** (implicitly used) | **HIGH** |
| 2 | **Prop 6.11** (topological Feynman transform) | F^{top} pGrav = C_*(M-bar, D), i.e., the topological Feynman transform of the partial gravity operad is chains on the Deligne-Mumford compactification with the dualizing complex. | Partial gravity operad | **(A)+(B)**: Provides the explicit geometric model for the Feynman transform in terms of Deligne-Mumford spaces. Combined with Thm A, this says the higher-genus bar complex is computed by C_*(M-bar_{g,n}, D) tensor A^{tensor n}. | **NO** | **HIGH** |
| 3 | **Thm 8.13** (characteristic of modular operad) | The character of a modular operad M(V) = sum_g sum_n h^g M((g,n)) tensor_{S_n} V^{tensor n} satisfies Ch(MV) = exp(sum_{g>=0} h^g sum_n M((g,n))^{S_n} / n!). | Modular operad M | **(C)**: Could compute the generating function of quantum corrections Q_g(A) by applying this to the modular operad {M-bar_{g,n}} with A-coefficients. The complementarity Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)) would then become an identity of generating functions. | **NO** | **HIGH** |
| 4 | **Cor 8.15** (Feynman transform characteristic) | Ch(F_D A) is the plethystic exponential of Ch(A) twisted by Ch(D). | D modular operad, A a D-algebra | **(B)+(C)**: Gives an explicit formula for the Poincare series of B(A) in terms of the Poincare series of A and the Euler characteristics of M_{g,n}. Combined with Thm B (B(A) = A for Koszul A), this constrains the Poincare series of Koszul chiral algebras. | **NO** | **HIGH** |
| 5 | **Cor 7.22** (bar = Legendre transform) | The bar construction on a cyclic operad P is computed by the Legendre transform: Ch(B(P)) = -L(Ch(P)) where L is the functional inverse under plethystic composition. | P a cyclic operad | **(B)**: The Legendre transform provides a combinatorial formula for bar. For Koszul P, B(P) = P^! and the Legendre transform identity becomes Ch(P^!) = -L(Ch(P)). This could give new proofs of Koszulness by verifying the Legendre identity. | **NO** | **MEDIUM** |
| 6 | **Thm 8.18** (plethystic Fourier) | The plethystic Fourier transform interchanges bar and cobar at the level of generating functions: F(Ch(B(A))) = Ch(Omega(A)). | Modular operad context | **(B)**: Provides a generating-function-level verification of Thm B. If Omega(B(A)) = A, then F(Ch(B(A))) = Ch(A), which is a nontrivial identity of formal power series. | **NO** | **MEDIUM** |
| 7 | **Prop 9.5** (moduli Euler characteristics) | Explicit formulas for chi(M_{g,n}) in terms of Bernoulli numbers: chi(M_{g,n}) = (-1)^n (2g-3+n)! B_{2g} / (2g)! for n > 0, and chi(M_g) = B_{2g}/(2g(2g-2)) for n=0. | g >= 2, n >= 0 | **(C)**: These Euler characteristics control the leading term of quantum corrections Q_g(A). Combined with Thm C: dim Q_g(A) ~ chi(M_g) * dim Z(A) for large g, giving explicit growth rates for quantum corrections. | **NO** | **HIGH** |

---

### Get95 — Getzler, "Operads and Moduli Spaces of Genus 0 Riemann Surfaces" (24 pp)

**Current citation status**: Well cited (~10 citations). Used for HyCom/Grav Koszul duality, fundamental classes.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Thm 4.13** (HyCom Koszul) | The operad HyCom is Koszul and HyCom^! = Grav. Equivalently, the bar construction B(HyCom) is quasi-isomorphic to Grav^c. | None (absolute statement) | **(A)+(B)**: This is the genus-0 engine of the manuscript. Already cited and used. The new observation: combined with Thm A, this says B^{ch}(A) for a HyCom-algebra A is a Grav^c-coalgebra, and combined with Thm B, Omega(B(A)) -> A collapses at E_2. | **YES** | **LOW** |
| 2 | **Thm 4.6** (bar HyCom = Grav) | The natural map B(HyCom) -> Grav is a homotopy equivalence of operads. The map is induced by integration over M-bar_{0,n}. | None | **(A)**: Provides the explicit integration map that identifies the bar differential with the boundary of M-bar_{0,n}. This is the configuration-space integral that makes Thm A concrete at genus 0. | **YES** | **LOW** |
| 3 | **Thm 5.7** (Poincare characteristic of M_{0,n}) | The Poincare polynomial of M_{0,n} is P_t(M_{0,n}) = (1+t)(1+2t)...(1+(n-3)t) for n >= 3, and the Euler characteristic is chi(M_{0,n}) = (-1)^{n-3}(n-3)!. | n >= 3 | **(C)**: Combined with the genus-0 part of Thm C, this gives explicit dimensions for Q_0(A) in terms of A. Already implicitly used but the explicit polynomial could strengthen the genus-0 computations. | **YES** (implicitly) | **LOW** |
| 4 | **Thm 5.9** (Poincare characteristic of M-bar_{0,n}) | The Poincare polynomial of M-bar_{0,n} is P_t(M-bar_{0,n}) = sum_T prod_{v in T} (1+n(v)t+...+(n(v)-2)^{floor}t^{n(v)-3}) where T ranges over stable trees. | n >= 3 | **(A)**: Gives the Poincare polynomial of the FM compactification in the genus-0 case. Combined with Thm A, determines the Hilbert series of B(A) at genus 0. | **NO** | **LOW** |

---

## TIER 2 (Read first 10 pages)

---

### Positselski — "Two Kinds of Derived Categories, Koszul Duality, and Comodule-Contramodule Correspondence"

**Current citation status**: Moderately cited (~10 citations). Used for curved Koszul duality, CDG-algebras.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Thm (Ch 6)** (Comodule-contramodule correspondence) | For a conilpotent DG-coalgebra C, there is an equivalence D^{co}(C-comod) = D^{ctr}(C-contra) between the coderived category of C-comodules and the contraderived category of C-contramodules. | C conilpotent DG-coalgebra | **(A)**: For A Koszul chiral, B(A) = A^{!,c} is a conilpotent coalgebra. The comodule-contramodule correspondence then gives D^{co}(A^{!,c}-comod) = D^{ctr}(A^{!,c}-contra). Combined with Thm A (module KD): this extends the module Koszul duality to the coderived/contraderived level. | **NO** | **HIGH** |
| 2 | **Thm (Ch 6)** (Two kinds of derived categories) | For a CDG-algebra B, the "first kind" derived category D(B-mod) differs from the "second kind" D^{co}(B-mod). The second kind (coderived) is the correct target for Koszul duality. | B a CDG-algebra (e.g., curved A-infinity) | **(A)+(B)**: The bar construction B(A) for non-Koszul A has curvature, making it a CDG-coalgebra. The correct version of Thm B in the curved case uses the coderived category: Omega(B(A)) -> A is a quasi-isomorphism in D^{co}, not in D. The manuscript mentions this distinction but doesn't fully exploit it. | Mentioned but not formally used | **HIGH** |
| 3 | **D-Omega duality** | For a complete filtered algebra A-hat, there is an equivalence D^b(A-hat-mod) = D^{co}(Omega(A-hat)-comod) where Omega is the DG-resolution. This extends to D-modules: D-mod on X = CDG-mod on Omega_X. | Complete filtered algebra | **(A)**: Provides the D-module interpretation of bar-cobar: chiral algebras ARE D-modules on X, and bar-cobar duality is a shadow of D-Omega duality. This could give a new proof of Thm A by reducing to Positselski's D-Omega equivalence. | **NO** | **HIGH** |
| 4 | **Koszul duality for nonconilpotent** | Extends Koszul duality beyond the conilpotent case using curved coalgebras and complete algebras. The bar-cobar adjunction becomes: CDG-coalgebras <-> complete augmented DG-algebras. | Nonconilpotent setting | **(A)**: Relevant for chiral algebras at non-generic levels (e.g., critical level) where the bar construction is not conilpotent. Thm A currently assumes Koszulness, which implies conilpotence. This could extend Thm A to the critical level. | **NO** | **MEDIUM** |

---

### BGS96 — Beilinson-Ginzburg-Soergel, "Koszul Duality Patterns in Representation Theory"

**Current citation status**: Moderately cited (~8 citations). Used for Koszul criterion (diagonal purity), derived equivalences.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Thm 1.1.3** (parabolic-singular duality) | For a semisimple Lie algebra g, there is a Koszul duality equivalence between (1) the parabolic category O^p (with Verma filtrations) and (2) the singular category O^s (with projective filtrations). | g semisimple, p a parabolic | **(A)+(module KD)**: The parabolic-singular duality is a representation-theoretic incarnation of module Koszul duality. Combined with Thm A: for the affine Lie algebra g-hat at generic level, a chiral analog of parabolic-singular duality should hold. Category O_kappa for g-hat should be Koszul dual to a "singular" category. | **NO** | **HIGH** |
| 2 | **Thm 1.2.5** (E involution) | For a Koszul algebra A, the Koszul dual of the Koszul dual is the original: E(E(A)) = A (where E(A) = Ext_A(k,k)). | A Koszul | **(A)+(B)**: This is the algebraic statement underlying Thm B at genus 0. The chiral version: for Koszul chiral A, (A^!)^! = A. Already implicit in the manuscript but could be stated as a formal corollary. | Implicitly used | **LOW** |
| 3 | **Thm 1.2.6** (Koszul duality functor K) | For Koszul A, the functor K: D^b(A-mof) -> D^b(A^!-mof) is an equivalence of triangulated categories, sending simples to projectives (up to shift). | A Koszul, finite-dimensional | **(A)**: Combined with Thm A, gives a derived equivalence D^b(A^{ch}-mod) -> D^b((A^{ch})^!-mod) for Koszul chiral algebras. The functor K is the bar functor B restricted to modules. | **YES** (chiral_modules.tex) | **LOW** |
| 4 | **Thm 1.4.2** (perverse sheaves = Koszul modules) | The category of perverse sheaves on a flag variety is equivalent to the category of finitely generated modules over a Koszul algebra (the Ext algebra of IC sheaves). | Flag variety, semisimple group | **(A)+(C)**: Could provide geometric models for module categories of chiral Koszul algebras. If A^{ch} is the chiral algebra associated to g, then the module category should be perverse sheaves on an infinite-dimensional flag variety (affine Grassmannian). | **NO** | **MEDIUM** |
| 5 | **Prop 2.1.3** (Koszul = maximally close to semisimple) | A is Koszul iff Ext^i_A(k,k) is concentrated in internal degree i for all i. Equivalently, A has a "linear" resolution. | A augmented graded algebra | **(B)**: The "linear resolution" characterization of Koszulness. Combined with Thm B: the spectral sequence Omega(B(A)) -> A collapses at E_2 iff A has a linear resolution. This gives a computational criterion for checking Thm B. | **YES** (chiral_koszul_pairs.tex) | **LOW** |
| 6 | **Thm 2.10.1** (diagonal purity criterion) | A is Koszul iff Ext^i_A(k,k)_j = 0 for i != j (diagonal purity of Ext). | A graded augmented | **(B)**: Already cited and used as the main Koszulness criterion. | **YES** | **LOW** |

---

### KL93 — Kazhdan-Lusztig, "Tensor Structures Arising from Affine Lie Algebras. I"

**Current citation status**: Well cited (~8 citations). Used for category O_kappa, tensor structure, Weyl modules.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Prop 2.12** (irreducibility for irrational kappa) | For irrational kappa (i.e., kappa not of the form rational + h-dual), the Weyl module V^kappa_lambda is irreducible. | kappa irrational | **(C)**: At irrational levels, there are no quantum corrections (Q_g = 0 for g >= 1) because the representation theory is semisimple. This provides a representation-theoretic explanation for why Thm C is most interesting at rational levels. | **NO** | **MEDIUM** |
| 2 | **Tensor structure via KZ** | O_kappa admits a tensor structure defined via the Knizhnik-Zamolodchikov connection on configuration spaces of points on P^1. | kappa non-rational | **(A)**: The KZ connection IS the genus-0 propagator in the bar construction. The tensor product on O_kappa is computed by the genus-0 bar complex with 2 inputs. Combined with Thm A: the tensor structure on O_kappa extends to higher genus via the higher-genus bar construction, giving a "genus-g tensor product." | **NO** | **HIGH** |
| 3 | **Duality functor D** | There is a contravariant exact duality functor D: O_kappa -> O_{kappa'} where kappa' = -kappa - 2h-dual. | kappa generic | **(C)**: The KL duality functor D sends level kappa to -kappa-2h-dual, which is the Feigin-Frenkel involution. Combined with Thm C: Q_g(A_kappa) + Q_g(A_{kappa'}) = H*(M_g, Z(A)). The KL duality interchanges the two summands. | Implicitly used (Feigin-Frenkel) | **MEDIUM** |
| 4 | **Sugawara operator** | The Sugawara construction T = (1/2(k+h^vee)) sum :J^a J^a: defines a conformal vector in the vacuum module at non-critical level. The Virasoro central charge is c = k*dim(g)/(k+h^vee). | k != -h^vee | **(C)**: The Sugawara operator is the obstruction to extending the chiral algebra from genus 0 to genus 1. At the critical level k = -h^vee, Sugawara is undefined and the center becomes huge (Feigin-Frenkel). Combined with Thm C: Q_1(KM_k) depends on c(k) and diverges as k -> -h^vee. | **YES** (multiple places) | **LOW** |

---

### Zhu96 — Zhu, "Modular Invariance of Characters of Vertex Operator Algebras"

**Current citation status**: Well cited (~8 citations). Used for Zhu's algebra, modular invariance.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Thm 5.3.2** (SL_2(Z) invariance) | For a rational VOA V, the vector space spanned by characters (graded traces) of irreducible V-modules is invariant under SL_2(Z). | V rational (finitely many irred modules, complete reducibility) | **(C)**: Combined with Thm C at genus 1: the space of quantum corrections Q_1(A) for rational A carries an SL_2(Z) action (from the modular group of the elliptic curve). The complementarity Q_1(A) + Q_1(A^!) = H^*(M_1, Z(A)) should be SL_2(Z)-equivariant. | **YES** (toroidal_elliptic.tex, free_fields.tex) | **MEDIUM** |
| 2 | **A(V) <-> V-mod correspondence** | There is a bijection between irreducible N-gradable V-modules and irreducible A(V)-modules, where A(V) = V / O(V) is Zhu's algebra. | V a VOA | **(A)+(module KD)**: Zhu's algebra A(V) computes the genus-0 part of the module category. Combined with module Koszul duality (Thm A at module level): A(A^{ch}) should be Koszul dual to A((A^{ch})^!) in the sense of BGS96. | **NO** | **HIGH** |
| 3 | **Genus-1 correlation functions** | n-point correlation functions on the torus for a rational VOA V satisfy a system of differential equations (KZB-type) and have modular transformation properties. | V rational, modules M_1,...,M_n | **(C)**: The genus-1 n-point functions are exactly the data computed by the genus-1 bar complex B^{(1)}(A) with n insertions. Combined with Thm C: the modular properties of these functions should be explained by the complementarity formula. | Partially cited | **MEDIUM** |

---

## TIER 3 (Abstract + main theorem)

---

### CP2020 — Costello-Paquette, "Twisted Supergravity and Koszul Duality: A Case Study in AdS_3"

**Current citation status**: Cited 4 times (all in poincare_duality_quantum.tex), for the physical context of AdS_3/CFT_2.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Section 6.1** (KD as universal defect) | For a topological field theory with operator algebra A (dg-algebra with BRST differential Q), the Koszul dual A^! is the algebra of operators of the "universal line defect": coupling to a quantum mechanics B is the same as giving a homomorphism A^! -> B. | A a dg-algebra (BRST cohomology of local operators), deformation of free theory | **(A)+(C)**: This physical interpretation of Koszul duality gives a field-theoretic meaning to Theorem A: the bar construction B(A) should be read as algebraic shadow data for the universal defect algebra. Combined with Thm C: quantum corrections Q_g(A) measure the failure of the universal defect to extend from genus 0 to genus g. | Physical context cited, this specific theorem **NO** | **HIGH** |
| 2 | **Eq (6.2.19)** (MC <-> Hom bijection) | MC(A tensor B) <-> Hom(A^!, B). Solutions to the Maurer-Cartan equation in A tensor B biject with algebra maps from A^! to B. | A augmented dg-algebra, B in ghost number 0 | **(C)**: This is the deformation-theoretic content of Koszul duality. Combined with Thm C: the genus-g Maurer-Cartan space MC_g(A) (controlling deformations of A on a genus-g curve) should biject with Hom(A^!, B_g) for an appropriate B_g constructed from M_g. | **NO** | **HIGH** |
| 3 | **Section 6.2.3** (4d CS KD = Yangian) | The Koszul dual of the algebra of local operators of 4d Chern-Simons theory with Lie algebra g is the Yangian Y(g). | 4d Chern-Simons theory | **(A)**: Provides an explicit physical example: 4d CS is an E_1-algebra whose bar construction should model Y(g)^! as algebraic shadow data. Combined with the yangians.tex chapter: this motivates the Yangian example without collapsing the remaining comparison work into a proved bar-cobar identification. | **NO** | **MEDIUM** |
| 4 | **Section 7** (deformed KD and holography) | Backreaction of branes produces a deformation of the Koszul dual algebra. In the N -> infinity limit, the deformed Koszul dual of twisted supergravity on AdS_3 is conjecturally compared with the chiral algebra of the symmetric orbifold Sym^N(T^4). | Twisted supergravity, large N | **(C)**: This is a physical instance of deformation-obstruction complementarity: the backreaction (= deformation of bulk) is compared with a specific boundary algebra (= obstruction resolved) through a conjectural holographic dictionary. | **YES** (poincare_duality_quantum.tex) | **LOW** |

---

### BFN08 — Ben-Zvi, Francis, Nadler, "Integral Transforms and Drinfeld Centers in Derived Algebraic Geometry"

**Current citation status**: Not cited in manuscript.

| # | Theorem | Statement (condensed) | Hypotheses | Combinability | Cited? | Priority |
|---|---------|----------------------|------------|---------------|--------|----------|
| 1 | **Cor 5.2** (Drinfeld center = loop space sheaves) | For X a perfect stack, there are canonical equivalences QC(LX) = Z(QC(X)) = Tr(QC(X)), where LX = Map(S^1, X) is the derived loop space, Z is the Drinfeld center, and Tr is the trace. | X perfect stack | **(A)+(C)**: For X = BG (classifying stack), QC(LX) = QC(G/G) = sheaves on the adjoint quotient. The Drinfeld center Z(QC(X)) is the Hochschild cohomology category. Combined with Thm A: for chiral algebra A, the Hochschild cohomology HH*(A^{ch}) should be computed by factorization homology on the loop space of the moduli of A-bundles. Combined with Thm C: Z(A) (the center appearing in complementarity) has a loop-space interpretation. | **NO** | **HIGH** |
| 2 | **Thm 5.3** (center of convolution = loop space) | For p: X -> Y a map of perfect stacks satisfying descent, Z(QC(X x_Y X)) = QC(LY). | p satisfying descent | **(A)**: The convolution category QC(X x_Y X) is the Hecke category. Its Drinfeld center is sheaves on the loop space of Y. Combined with Thm A: if Y = Bun_G(Sigma) (moduli of G-bundles on a curve), then the center of the Hecke category on Sigma is QC(L Bun_G(Sigma)), relating to the higher-genus bar construction. | **NO** | **HIGH** |
| 3 | **Cor 5.12** (E_n-Hochschild cohomology = mapping space) | For X perfect, the E_n-Hochschild cohomology of QC(X) is QC(X^{S^n}), where X^{S^n} = Map(S^n, X). | X perfect stack, E_n-tensor product | **(A)**: The E_n-Hochschild cohomology categorifies the Hochschild-to-cyclic spectral sequence. For n=1 (E_1 = chiral/associative): HH^{E_1}(QC(X)) = QC(LX). For n=2 (E_2): HH^{E_2}(QC(X)) = QC(X^{S^2}). Combined with the E_1-chiral framework: the E_1-Hochschild cohomology of a chiral algebra category should be computed by the bar complex on the torus (genus 1). | **NO** | **HIGH** |
| 4 | **Prop 6.3** (2d TFT from perfect stacks) | For X a perfect stack, there is a 2d TFT Z_X: 2Cob -> Cat^{ex}_infty with Z_X(S^1) = QC(LX) and Z_X(Sigma) = Gamma(X^Sigma, O). | X perfect stack | **(A)+(B)+(C)**: This is a categorified version of the factorization homology framework. Combined with all three theorems: the 2d TFT Z_X applied to genus-g surfaces computes the genus-g bar complex, the inversion (Thm B) is the 2d TFT pants-product unitality, and the complementarity (Thm C) comes from the TFT pairing on the closed surface. | **NO** | **HIGH** |
| 5 | **Cor 6.7** (Deligne conjecture: center is E_2) | For X perfect, the center Tr(QC(X)) = QC(LX) has the structure of a stable framed E_2-category. For a map X -> Y, Tr(QC(X x_Y X)) = QC(LY) is also a framed E_2-category. | X perfect stack | **(A)**: Combined with the E_1-chiral structure: the center of the chiral algebra module category should carry an E_2 structure, which at the character level is the braided tensor structure of conformal blocks. | **NO** | **MEDIUM** |
| 6 | **Cor 6.8** (Kontsevich conjecture) | For X perfect, the E_n-Hochschild cohomology of the stable E_n-category QC(X) has the structure of a stable (framed) E_{n+1}-category. | X perfect stack | **(A)**: Categorified Kontsevich conjecture. The E_1-Hochschild cohomology (= Drinfeld center) has E_2 structure, the E_2-Hochschild cohomology has E_3 structure, etc. This hierarchy is related to the deformation theory of chiral algebras: each level of E_n-structure controls deformations at the next level. | **NO** | **MEDIUM** |

---

## SYNTHESIS: Top Priority Combinations

### Priority 1: New results directly provable from manuscript + references

1. **AF15 Prop 6.9 + Thm A**: The bar filtration IS the Goodwillie cofiltration of factorization homology. This identifies the bar spectral sequence E_1 page as Conf_k(X) tensor (s^{-1}A-bar)^{otimes k}. *(AF15, not cited)*

2. **GeK98 Thm 5.4 + Thm B**: The Feynman transform involution F_{D^vee} F_D = id is the operadic form of bar-cobar inversion. *(GeK98, not cited for this specific result)*

3. **GeK98 Thm 8.13 + Cor 8.15 + Thm C**: Generating function identity for quantum corrections: the complementarity formula becomes an identity of plethystic exponentials. *(GeK98, not cited)*

4. **Positselski comodule-contramodule + Thm A**: The module Koszul duality extends to coderived/contraderived categories: D^{co}(A^{!,c}-comod) = D^{ctr}(A^{!,c}-contra). *(Positselski, not cited for this specific result)*

### Priority 2: Results requiring moderate new work

5. **FG12 Thm 5.2.1 + Prop 4.3.1 + Thm C**: Deformation-obstruction theory as formal moduli problems on Ran(X). The quantum corrections parametrize a formal moduli problem. *(FG12, not cited for this specific combination)*

6. **Zhu96 A(V) + BGS96 Thm 1.1.3 + Thm A**: Zhu's algebra A(A^{ch}) is Koszul dual to A((A^{ch})^!) in the sense of BGS96 parabolic-singular duality. *(Zhu96+BGS96, not combined in manuscript)*

7. **BFN08 Cor 5.2 + Thm C**: The center Z(A) in the complementarity formula has a loop-space interpretation: Z(A) = QC(L(Bun_A)). *(BFN08, not cited)*

8. **KL93 tensor structure + Thm A**: The KZ-defined tensor product on O_kappa extends to a "genus-g tensor product" via the higher-genus bar construction. *(KL93, not combined with Thm A)*

### Priority 3: Conceptual enhancements

9. **AF15 Prop 6.12**: Configuration spaces are Goodwillie derivatives of factorization homology. Gives conceptual foundation for the Prism Principle.

10. **CP2020 Section 6.1 + Thm A**: Physical interpretation: bar construction = universal defect algebra. Quantum corrections = failure of defect to extend across genera.

11. **BFN08 Prop 6.3 + Thms A+B+C**: A categorified 2d TFT framework that unifies all three theorems.

12. **GeK98 Prop 9.5 + Thm C**: Explicit growth rates for quantum corrections using Bernoulli-number formulas for chi(M_g).
