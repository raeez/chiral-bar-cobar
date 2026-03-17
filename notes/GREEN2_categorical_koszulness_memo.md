# GREEN-2 Memo: Toward an Infinity-Categorical Characterization of Chiral Koszulness

**Author**: GREEN-2 (higher category theorist)
**Date**: 2026-03-17
**Status**: Research memo / proposal for future development


## Executive Summary

The monograph characterizes chiral Koszulness reductively: an algebra is chiral Koszul if its PBW-associated graded is classically Koszul and the resulting spectral sequence collapses (Definition `def:chiral-koszul-morphism`, Theorem `thm:pbw-koszulness-criterion`). This is a *verification criterion*, not an intrinsic characterization. From the perspective of stable infinity-categories, Koszulness should be a *property of the module category* --- or more precisely, a property of the factorization module category viewed as a stable infinity-category with t-structure.

This memo proposes seven interlocking infinity-categorical characterizations, grounded in the monograph's existing structures, and identifies the precise interaction between the RNW19 no-bifunctor obstruction and Koszulness.

---

## 0. Notation and Standing Conventions

Throughout: X is a smooth projective curve over C; A is an augmented chiral algebra on X; B(A) its bar coalgebra; A^! = H^*(B(A))^v the Koszul dual algebra; g^mod_A the modular convolution dg Lie algebra (Definition `def:modular-convolution-dg-lie`); Theta_A the universal MC element (Theorem `thm:mc2-bar-intrinsic`). We write Fact(X) for the symmetric monoidal infinity-category of factorization algebras on X, and FactMod(A) for the infinity-category of factorization modules over A.

---

## A. Module Category Characterization

### The Conjecture

**Conjecture A1** (Factorization module Koszul equivalence). *For a chiral Koszul pair (A, A^!) on X, there is an equivalence of stable infinity-categories*

```
Phi: FactMod(A) --~--> FactCoMod(A^!)
```

*induced by the bar functor B: M |-> B(A) otimes_A M. The algebra A is chiral Koszul if and only if Phi is t-exact with respect to the PBW t-structure on FactMod(A) and the cobar t-structure on FactCoMod(A^!).*

### Relationship to Monograph

The monograph already proves the key ingredient: Proposition `prop:koszul-t-structures` establishes that Koszul duality exchanges the standard t-structure on D^b(O_k) with the Koszul t-structure on D^b(O_{k'}), with the heart of the Koszul t-structure being the original category O. The equivalence Phi(L(lambda)) lies in the heart for all lambda (lines 1260-1264 of `chiral_modules.tex`).

What is missing is the upgrade from the triangulated level (D^b) to the stable infinity-categorical level, and from category O to the full factorization module category. The triangulated statement is a shadow of the infinity-categorical one.

**Precise formulation**: Define the PBW t-structure on FactMod(A) by declaring M in D^{<=0} iff the bar filtration spectral sequence for B(M) has E_1^{p,q} = 0 for p+q > 0. Define the cobar t-structure on FactCoMod(A^!) dually. Then:
- t-exactness of Phi is *equivalent to* the PBW spectral sequence collapsing at E_2 for all modules M, not just the algebra A itself.
- The heart preservation condition is *equivalent to* the Koszul linearity property: B_n(L(lambda)) is concentrated in internal degree n + h(lambda).

### Three-Pillar Interaction

Pillar A (MS24): The homotopy chiral algebra structure ensures that FactMod(A) is an infinity-category, not merely a 1-category. The rectification theorem (Corollary `cor:rectification-ch-infty`) guarantees that the homotopy and strict module categories are equivalent.

Pillar B (RNW19): The convolution sL_infty-algebra hom_alpha(C,A) controls the *deformations* of the functor Phi. The MC infinity-groupoid MC_bullet(hom_alpha) classifies *all* twisted tensor product functors; Phi is the one corresponding to the universal twisting morphism.

Pillar C (Mok25): The log FM compactification provides the geometric skeleton for factorization modules: a factorization module M over A is controlled by its restriction to FM_n^{log}(X|D), and the module-level bar resolution lives on these spaces.

### Feasibility

Medium-high. The triangulated version is proved (Proposition `prop:koszul-t-structures`). The upgrade requires:
1. Constructing the infinity-categorical enhancement of the derived categories of factorization (co)modules, using the model category of Vallette (Theorem `thm:quillen-equivalence-chiral`).
2. Verifying that the bar functor B is a left t-exact functor of stable infinity-categories, and that t-exactness is equivalent to the PBW collapse for modules.

---

## B. Barr-Beck-Lurie Characterization

### The Conjecture

**Conjecture B1** (Barr-Beck-Lurie for bar-cobar). *The bar-cobar adjunction*

```
B_kappa: dg-Ch-alg  <-->  conil-dg-C^!_ch-coalg : Omega_kappa
```

*satisfies the Barr-Beck-Lurie conditions. Precisely:*

1. *B_kappa is conservative (detects equivalences).*
2. *B_kappa preserves totalizations of B_kappa-split cosimplicial objects.*
3. *Chiral Koszulness of A is equivalent to the Barr-Beck comparison functor being an equivalence on the fiber over B(A), i.e., the cobar-bar counit Omega(B(A)) -> A is an equivalence (not merely fully faithful on hom-sets).*

### Relationship to Monograph

The monograph proves exactly condition (3) for Koszul algebras: the counit Omega(B(A)) -> A is a quasi-isomorphism on the Koszul locus (Theorem `thm:bar-cobar-inversion-qi`, fundamental theorem of chiral twisting morphisms `thm:fundamental-twisting-morphisms`). Off the Koszul locus, the object persists only in the coderived category (Remark `rem:construction-vs-resolution`).

The Quillen equivalence (Theorem `thm:quillen-equivalence-chiral`) gives the derived-level version: the homotopy categories are equivalent. But Barr-Beck-Lurie is *sharper*: it says the equivalence arises from a monadicity/comonadicity pattern. The comonad is G = B circ Omega, and the comparison functor sends a coalgebra C to the totalization of the cosimplicial object B(Omega(C)) => B(Omega(B(Omega(C)))) => ...

**Koszulness = comonadicity**: The Barr-Beck viewpoint identifies Koszulness as the condition under which the bar construction creates an *effective* descent datum. Off the Koszul locus, the descent data is non-effective --- this is the infinity-categorical content of "the bar-cobar object lives in the coderived category, not the derived category."

### Precise Conditions

Condition (1), conservativity: B_kappa detects quasi-isomorphisms. This is proved as part of the Quillen equivalence (Theorem `thm:quillen-equivalence-chiral`, item (iv): B_kappa preserves fibrations and weak equivalences; it also *reflects* weak equivalences because Omega_kappa does, by the two-out-of-three property).

Condition (2), totalization preservation: This requires B_kappa to preserve certain limits. Since B_kappa is a left adjoint, it preserves colimits automatically; the totalization condition is the nontrivial one. On the Koszul locus, this follows from the PBW filtration being compatible with arbitrary bar-length filtrations.

### Three-Pillar Interaction

The key insight is that the Barr-Beck conditions interact differently with the three pillars:
- Conservativity (condition 1) is a Pillar B statement: it follows from the MC moduli being detected by the convolution algebra.
- Totalization preservation (condition 2) is a Pillar C statement: it requires the log FM compactification to have the correct homotopy type (contractible fibers over collision strata).
- The comparison functor being an equivalence (condition 3) is a Pillar A statement: it says the Ch_infty rectification is effective.

### Feasibility

High. The Quillen equivalence is proved. The upgrade to Barr-Beck-Lurie requires checking that the adjunction satisfies the simplicial enrichment conditions of [Lurie, Higher Algebra, Theorem 4.7.3.5]. This is straightforward given the model structure.

---

## C. Hochschild Cohomology / E_2-Formality Characterization

### The Conjecture

**Conjecture C1** (Koszulness as E_2-formality). *A chiral algebra A on X is chiral Koszul if and only if its chiral Hochschild complex C^*_{chiral}(A) is formal as an E_2-algebra.*

More precisely: the E_2 structure on ChirHoch^*(A) (from the brace operations on the Hochschild complex) is quasi-isomorphic to its cohomology H^*(ChirHoch(A)) as an E_2-algebra.

### Relationship to Monograph

Theorem H (Theorem `thm:hochschild-polynomial-growth`, Theorem `thm:main-koszul-hoch`) proves two things:
1. ChirHoch^n(A) = 0 for n outside {0,1,2} (polynomial growth).
2. ChirHoch^n(A) = ChirHoch^{2-n}(A^!)^v tensor omega_X (Koszul duality for Hochschild).

The polynomial growth statement already implies *partial* formality: the Hochschild complex is concentrated in three degrees, so many Massey products vanish for degree reasons. Full E_2-formality is the statement that *all* higher E_2 operations are trivial on cohomology.

The E_n chapter (Chapter `ch:en-koszul-duality`) establishes the formality hierarchy: at n=2, E_2 formality holds by Kontsevich's theorem for symmetric chiral algebras. For E_1-chiral algebras, the transferred A_infty structure is genuinely non-formal (Theorem `thm:en-chiral-bridge`(iii)). This suggests:

**Refined Conjecture C1'**: *A is chiral Koszul if and only if ChirHoch^*(A) is formal as an E_2-algebra in the factorization category Fact(X).*

### The Key Distinction

Classical formality (Kontsevich) gives E_2-formality for the little 2-disks operad itself. But chiral Hochschild cohomology lives on configuration spaces of a *curve*, not of the plane. The formality of ChirHoch^*(A) as an E_2-algebra encodes:
- Genus-0 data: the OPE is determined by finitely many terms (the Koszul dual). This is the PBW collapse.
- Genus-1 data: the curvature kappa(A) is the *unique* obstruction to extending the E_2-formality to the genus-1 enrichment. This is the content of the modular characteristic theorem (Theorem `thm:modular-characteristic`).

### Three-Pillar Interaction

Pillar A (MS24): The secondary Borcherds operations F_n (identified with the shadow tower obstruction classes o_n, Remark `rem:three-pillar-identifications`(8)) are *precisely* the obstructions to E_2-formality. F_3 = o_3 is the Jacobiator homotopy; F_4 = o_4 is the quartic resonance class. E_2-formality of ChirHoch^*(A) is equivalent to all F_n being cohomologically trivial.

Pillar B (RNW19): The convolution sL_infty-algebra hom_alpha carries the deformation of the E_2 structure. Formality of ChirHoch^*(A) as E_2 is equivalent to formality of the relevant truncation of hom_alpha.

### Feasibility

Medium. The concentration in degrees {0,1,2} is proved. The E_2 structure on ChirHoch^*(A) needs to be constructed explicitly (the brace operations), and the formality statement needs to be verified against the PBW collapse. The E_n chapter provides the operadic framework.

---

## D. Convolution Algebra / MC Moduli Characterization

### The Conjecture

**Conjecture D1** (Koszulness as formality of convolution algebra). *A modular Koszul chiral algebra A has g^mod_A formal as a quantum L_infty-algebra if and only if A is one-channel (scalar-saturated): Theta_A = kappa . eta tensor Lambda.*

**Conjecture D2** (Koszulness as smoothness of MC moduli). *A is chiral Koszul if and only if the MC moduli stack MC(g^mod_A) is smooth at Theta_A (unobstructed deformations in the PBW direction).*

### Relationship to Monograph

The monograph's Remark `rem:full-homotopy-why` (line 7756) states explicitly: "modular-formal = quantum L_infty is formal; for Koszul algebras this holds by one-channel + concentration." This is a direct claim that formality and Koszulness are linked through the one-channel property.

The modular convolution algebra g^mod_A = prod_{g,n} Hom_{Sigma_n}(C_*(M_{g,n}), End_A(n)) (Definition `def:modular-convolution-dg-lie`) carries the five-component differential D = d_int + [tau,-] + d_sew + d_pf + hbar Delta (Theorem `thm:convolution-dg-lie-structure`). Formality of g^mod_A as a quantum L_infty algebra means: the inclusion of cohomology H^*(g^mod_A) -> g^mod_A extends to a quantum L_infty quasi-isomorphism.

For Koszul algebras, the PBW collapse means that the only nontrivial cohomology classes are those forced by the modular operad structure. The MC element Theta_A = D_A - d_0 is then determined by its scalar trace kappa(A) and the formal structure of the modular operad boundary --- this is scalar saturation.

**The critical distinction**: Formality of g^mod_A is *stronger* than Koszulness of A. Koszulness is a genus-0 property (PBW collapse for the bar complex); formality of g^mod_A is an all-genera property (PBW collapse for the genus-g bar complex at all g). The monograph's modular Koszulness (Definition `def:modular-koszul-chiral`, axiom MK3) bridges this: it requires PBW concentration at all genera.

### Three-Pillar Interaction

Pillar B is dominant here. The convolution sL_infty-algebra hom_alpha(C,A) is the deformation-theoretic home of g^mod_A. Formality of g^mod_A means the deformation theory is controlled by cohomological data alone --- no chain-level corrections survive.

Pillar C (Mok25): The planted-forest coefficient algebra G_pf = Trop(FM_n^{log}(X|D)) controls the non-formal corrections in g^mod_A. If the log FM compactification has trivial cohomological contributions from planted-forest strata, then g^mod_A is formal.

### Feasibility

Conjecture D2 (smoothness): High feasibility. The obstruction to smoothness of MC(g^mod_A) at Theta_A is H^2(g^mod_A, ad(Theta_A)), and vanishing of this group is closely related to the PBW collapse.

Conjecture D1 (formality = one-channel): Medium feasibility. The one-channel property is verified computationally for all standard families, but the theoretical identification of formality with one-channel requires a Kontsevich-type formality argument at the modular level.

---

## E. Factorization Homology Characterization

### The Conjecture

**Conjecture E1** (Koszulness and factorization homology concentration). *A is chiral Koszul if and only if the factorization homology*

```
int_Sigma_g A
```

*is concentrated in degree 0 for all smooth curves Sigma_g, with the higher homology groups detecting deviations from Koszulness.*

### Relationship to Monograph

Proposition `prop:bar-fh` (line 2250-2326 of `bar_cobar_adjunction_inversion.tex`) proves B^{geom}_X(A) = int_X A^{Lie}: the bar complex IS factorization homology. Remark `rem:chiral-homology-derived-conformal` (lines 1204-1234 of `chiral_modules.tex`) makes the connection explicit: "For Koszul algebras, the E_2 collapse forces H^{>0} = 0: the conformal block IS the full chiral homology."

This is precisely the statement that Koszulness implies concentration of factorization homology. The reverse direction requires checking that concentration of int_Sigma_g A in degree 0 for all g implies the PBW collapse.

**Refined version using Ayala-Francis**: By [AF15, Proposition 6.12], the k-th Goodwillie derivative of int_M(-) is Conf_k(M). The Goodwillie tower of int_X A is:

```
int_X A  =  A  +  Conf_2(X) tensor_{S_2} (s^{-1}A-bar)^{tensor 2}  +  ...
```

The bar spectral sequence IS the Goodwillie filtration of factorization homology. Concentration means the Goodwillie tower converges (which is the PBW collapse).

### Poincare/Koszul Duality

The Ayala-Francis Poincare/Koszul duality [AF15, Theorem 5.1] gives:

```
int_X A  =  int^X A^!   (factorization homology = factorization cohomology of dual)
```

This is the factorization-homology incarnation of Theorem C (complementarity). Koszulness ensures this Poincare duality is an equivalence, not merely a map.

### Three-Pillar Interaction

Pillar C (Mok25): The log FM compactification FM_n^{log}(X|D) provides the geometric skeleton for int_X A. At genus g >= 1, the factorization homology int_{Sigma_g} A has contributions from log-smooth boundary strata; these are controlled by the planted-forest tropicalization G_pf.

### Feasibility

Medium-high. The genus-0 direction (Koszulness implies concentration) is proved. The genus-g direction uses the modular Koszulness axiom MK3. The converse (concentration implies Koszulness) requires showing that concentration of factorization homology at all genera forces the PBW spectral sequence to collapse.

---

## F. Chiral BGG Correspondence

### The Conjecture

**Conjecture F1** (Chiral BGG). *For a chiral Koszul pair (A, A^!) with A = hat{g}_k, there is an exact functor*

```
BGG: O_k --> D^b(Coh(Gr_G))
```

*from category O at level k to the derived category of coherent sheaves on the affine Grassmannian Gr_G, such that:*
1. *Verma modules M(lambda) map to structure sheaves O_{S_lambda} of Schubert cells.*
2. *The BGG resolution of the simple module L(lambda) maps to the Cousin resolution of O_{S_lambda}.*
3. *The functor is the composition: bar resolution in O_k, then Koszul duality to comodules, then geometric Satake to Gr_G.*

### Relationship to Monograph

The monograph has substantial BGG content:
- Theorem `thm:bgg-from-bar` (line 2701 of `chiral_modules.tex`): BGG resolution from bar complex.
- Proposition `prop:bar-bgg-sl2` (line 4030 of `bar_complex_tables.tex`): explicit Bar-BGG for sl_2.
- Corollary `cor:bgg-koszul-involution` (line 4180): BGG involution under Koszul duality.
- Theorem `thm:yangian-bgg` (line 722 of `yangians_computations.tex`): Yangian BGG resolution.

The classical BGG correspondence gives: on the Koszul locus, the bar resolution of a simple module is *linear* (the n-th term is concentrated in internal degree n + h(lambda)), and this linear resolution is the BGG resolution. The monograph proves this for affine Kac-Moody algebras and Yangians.

**The infinity-categorical upgrade**: Classically, BGG gives a functor from the principal block of O_g to graded modules over the coinvariant algebra. In the chiral setting, the target should be factorization modules over A^!, or equivalently (by geometric Satake) constructible sheaves on Gr_G. The linearity of the bar resolution on the Koszul locus is the combinatorial content; the geometric content is that the bar complex *is* the Cousin complex of the IC sheaf under the Satake functor.

### The Weight Decomposition

For a chiral Koszul algebra, the derived category D^b(A-mod) admits a semi-orthogonal decomposition by conformal weight (see Section F below). The BGG correspondence sends each weight stratum to a stratum of the Grassmannian filtration. The compatibility of these two decompositions is the content of the Kazhdan-Lusztig equivalence (Theorem `thm:kazhdan-lusztig-equivalence`).

### Three-Pillar Interaction

Pillar A: The Ch_infty structure on B(A) (Theorem `thm:cech-hca`) ensures that the BGG resolution carries homotopy-coherent data, not just a chain complex. The secondary Borcherds operations F_n appear as the higher A_infty products on the BGG resolution.

Pillar C: The log FM compactification provides the collision geometry for the BGG differentials: each differential in the BGG resolution is a residue at a log-smooth boundary stratum of FM_n^{log}(X|D).

### Feasibility

Medium. The bar-BGG identification is proved for specific algebras. The full chiral BGG as a functor to Gr_G requires the geometric Satake correspondence at the factorization level, which is not developed in the monograph.

---

## G. Semi-Orthogonal Decomposition by Weight

### The Conjecture

**Conjecture G1** (Koszul weight decomposition). *For a chiral Koszul algebra A, the stable infinity-category FactMod(A) admits a semi-orthogonal decomposition*

```
FactMod(A) = <C_0, C_1, C_2, ...>
```

*indexed by conformal weight, where C_n = {M in FactMod(A) : M is generated in weight n}. The semi-orthogonality is: Hom(M, N) = 0 for M in C_i, N in C_j, i > j. Koszulness is equivalent to this decomposition being split (the projection functors are exact).*

### Relationship to Monograph

The monograph already has the key ingredients:
- The semiorthogonal decomposition of CDG-comodule and CDG-contramodule homotopy categories (line 1072-1078 of `bar_cobar_adjunction_inversion.tex`): "The homotopy categories admit semiorthogonal decompositions: the coderived category D^{co}(C-comod^{ch}) is equivalent to the homotopy category of CDG-comodules with injective underlying graded comodules."
- The Koszul t-structure (Proposition `prop:koszul-t-structures`): the equivalence D^b(O_k) -> D^b(O_{k'}) exchanges the standard t-structure with the Koszul t-structure.

The weight decomposition is the *algebraic* version of the BGG decomposition (Section F): each weight stratum C_n corresponds to the subcategory of modules whose bar resolution starts in degree n. Semi-orthogonality follows from the linearity of the bar resolution on the Koszul locus.

**The key statement**: Off the Koszul locus, the weight decomposition *fails to be semi-orthogonal*. There exist non-zero morphisms from higher weight to lower weight, mediated by the non-vanishing higher bar cohomology. Koszulness is *equivalent to* the vanishing of these cross-weight morphisms.

### Precise Formulation

Define the weight filtration on FactMod(A) by F_n = {M : M is generated in weights <= n}. The associated graded pieces C_n = F_n / F_{n-1} are the weight strata. The semi-orthogonal decomposition says: the natural inclusions C_n -> FactMod(A) admit left and right adjoints, and the composition C_i -> FactMod(A) -> C_j is zero for i > j.

On the Koszul locus, this follows from the linearity of bar resolutions (bar degree = internal degree). Off the Koszul locus, non-linear bar terms produce cross-weight Ext groups.

### Three-Pillar Interaction

Pillar B: The weight filtration on g^mod_A (from the genus/arity grading) controls the weight decomposition at the deformation-theoretic level. Formality of g^mod_A (Conjecture D1) implies that the weight decomposition is split.

### Feasibility

Medium-high. The semiorthogonal decomposition for CDG-categories is proved. The upgrade to the factorization module level requires constructing the weight filtration on FactMod(A) and checking the adjunction properties.

---

## H. The Key Question: No-Bifunctor Obstruction and Koszulness

### Statement

**Question**: Does Koszulness of A *imply* that the RNW19 no-bifunctor obstruction vanishes for hom_alpha(B(A), A)?

### Analysis

The no-bifunctor obstruction of Robert-Nicoud--Wierstra [RNW19, Theorem 6.6] states that hom_alpha(C, P) extends to infinity-morphisms in either slot separately but NOT both simultaneously. The counterexample is at arity 3: there is an explicit obstruction class in the arity-3 component of the convolution algebra that prevents simultaneous two-sided functoriality.

**My claim**: Koszulness does NOT make the bifunctor obstruction vanish. Rather, Koszulness makes the obstruction *irrelevant* by ensuring that all constructions can be factored through one slot at a time.

Here is the precise argument:

1. **The obstruction is structural, not cohomological**. The RNW19 counterexample works for *any* cooperad-operad pair, including Koszul ones. The obstruction is in the *morphism space* of the convolution algebra, not in its MC space (Remark `rem:two-level-convention`, lines 7822-7826: "The strict model has ell_k = 0 for k >= 3, so it computes MC *spaces* exactly; the full L_infty structure is needed for the *morphism spaces* between them. This dichotomy (objects vs. morphisms) is the root cause of the one-slot obstruction").

2. **Koszulness gives one-sided sufficiency**. For a Koszul pair (A, A^!), the bar-cobar adjunction B dashv Omega is a Quillen equivalence (Theorem `thm:quillen-equivalence-chiral`). This means: every infinity-morphism of chiral algebras f: A -> A' can be transported to an infinity-morphism of coalgebras B(f): B(A) -> B(A'), and conversely. But you never need to transport in *both slots simultaneously*.

3. **The MC3 obstruction is the interaction point**. The MC3 categorical lift (Remark `rem:three-pillar-mc-unification`, lines 780-785) is precisely where two-sided functoriality would be needed: to lift from K_0-generation (which is one-slot) to categorical splitting (which needs both slots). The monograph's strategy is to proceed "one slot at a time" via prefundamental CG closure. This works at the character level but leaves the categorical lift as the remaining open problem.

4. **Partial resolution**: For Koszul algebras with simple Lie symmetry, the MC3 resolution in type A (Theorem `thm:mc3-type-a-resolution`) uses chromatic filtration + prefundamental CG + Efimov completion + DK on compacts. Each step is one-slot. The full categorical lift for arbitrary type requires Hernandez-Jimbo prefundamental CG for all Dynkin types. This is a *representation-theoretic* obstruction, not a *homotopical* one.

### The Refined Conjecture

**Conjecture H1** (Koszulness and the bifunctor obstruction). *The RNW19 no-bifunctor obstruction for hom_alpha(B(A), A) does not vanish for Koszul algebras. However, for modular Koszul algebras (Definition `def:modular-koszul-chiral`), the following weaker property holds: the bifunctor obstruction class*

```
obs_3 in H^2(hom_alpha^{(3)}(B(A), A))
```

*is non-zero but lies in the image of the "one-slot factorization" map. Concretely: every two-sided infinity-morphism that fails to exist as a genuine bifunctor morphism can be *decomposed* into a one-sided coalgebra morphism followed by a one-sided algebra morphism, and the composition is independent of the order of composition up to homotopy.*

This decomposition property is precisely what makes the MC3 one-slot-at-a-time strategy work.

### Three-Pillar Interaction

This is the deepest interaction point of all three pillars:
- Pillar A (MS24): The Ch_infty rectification gives one-slot functoriality on the algebra side.
- Pillar B (RNW19): The one-slot obstruction is the structural constraint.
- Pillar C (Mok25): The log FM geometry gives an alternative geometric resolution: instead of extending infinity-morphisms in both slots, one uses the geometric decomposition of FM_n^{log}(X|D) into rigid components, each of which involves only one slot.

### Feasibility

This is the hardest of the conjectures. The arity-3 counterexample of RNW19 would need to be analyzed in the specific context of chiral Koszul pairs to determine whether the obstruction class has the decomposition property. This requires explicit computation of the arity-3 component of hom_alpha for specific examples (Heisenberg, affine Kac-Moody).

---

## Summary Table

| Conjecture | Statement | Monograph basis | Feasibility | Primary pillar |
|:-----------|:----------|:----------------|:------------|:---------------|
| A1 | FactMod(A) = FactCoMod(A^!) t-exact | prop:koszul-t-structures | Medium-high | A+B |
| B1 | Barr-Beck-Lurie for B dashv Omega | thm:quillen-equivalence-chiral | High | B |
| C1 | ChirHoch^*(A) formal as E_2 | thm:hochschild-polynomial-growth | Medium | A |
| D1 | g^mod_A formal iff one-channel | rem:full-homotopy-why | Medium | B+C |
| D2 | MC moduli smooth at Theta_A | thm:mc2-bar-intrinsic | Medium-high | B |
| E1 | int_X A concentrated in deg 0 | prop:bar-fh | Medium-high | C |
| F1 | Chiral BGG to Gr_G | thm:bgg-from-bar | Medium | A+C |
| G1 | SOD by weight iff Koszul | semiorthogonal decomp | Medium-high | B |
| H1 | Bifunctor obstruction decomposes | rem:two-level-convention | Low-medium | A+B+C |

---

## Recommended Priority

1. **B1 (Barr-Beck-Lurie)**: Highest priority. The Quillen equivalence is proved; the upgrade to Barr-Beck-Lurie is the most straightforward and gives the most conceptual characterization. It directly explains why the bar-cobar adjunction is special (it satisfies descent) and why Koszulness is the condition for descent to be effective.

2. **A1 (Module category)**: The t-exactness characterization is the most useful for applications. It gives a *checkable* condition at the module level: Koszulness iff the bar functor is t-exact on modules.

3. **E1 (Factorization homology)**: This gives the most geometric characterization and directly connects to the Ayala-Francis program. The identification bar = factorization homology is proved.

4. **H1 (Bifunctor obstruction)**: This is the most novel conjecture and the most important for the MC3 program. Understanding the interaction between Koszulness and the RNW19 obstruction would clarify the categorical lift strategy.

---

## Architectural Recommendation

The monograph currently characterizes chiral Koszulness through Definition `def:chiral-koszul-morphism` (acyclicity + associated graded Koszul + convergence) and the PBW criterion (Theorem `thm:pbw-koszulness-criterion`). I recommend adding a section to the concordance or to Chapter `chap:koszul-pairs` that states the following meta-theorem:

**Meta-Theorem** (Equivalences of Koszulness). *For an augmented chiral algebra A on a smooth projective curve X, the following are equivalent:*
1. *A is chiral Koszul (Definition `def:chiral-koszul-morphism`).*
2. *The bar-cobar counit Omega(B(A)) -> A is a quasi-isomorphism.*
3. *The bar complex B(A) is concentrated along the diagonal in bar/weight bigrading.*
4. *The PBW spectral sequence collapses at E_2.*
5. *The Barr-Beck comparison functor for B dashv Omega is an equivalence on A.*
6. *The factorization homology int_X A is concentrated in degree 0.*
7. *The chiral Hochschild complex ChirHoch^*(A) is polynomial (vanishes outside {0,1,2}).*

Items (1)-(4) are proved (fundamental theorem of chiral twisting morphisms). Items (5)-(7) are accessible from the existing infrastructure with moderate effort and would complete the infinity-categorical picture.
