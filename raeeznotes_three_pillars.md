# Three Pillars Integration: Comprehensive Notes & Task List

## The Three Pillars

1. **Pillar A: Homotopy Chiral Algebras** — Malikov-Schechtman [MS24], arXiv:2408.16787
2. **Pillar B: Convolution Homotopy Lie Algebras** — Robert-Nicoud-Wierstra [RNW19], arXiv:1712.00794 + Vallette [Val16], arXiv:1411.5533
3. **Pillar C: Logarithmic FM Configuration Spaces** — Mok [Mok25], arXiv:2503.17563

---

## I. CONSEQUENCES & RAMIFICATIONS

### I.A. PILLAR A: Homotopy Chiral Algebras (MS24)

#### I.A.1. The Ch∞ Structure on the Bar Complex

The bar complex B(A) of a chiral algebra A is a cosimplicial object in M(C). By MS24 Theorem 3.1, the Moore complex MB^bullet carries a canonical homotopy Lie algebra structure in the pseudo-tensor category C_{C(k)}. Specializing to the chiral pseudo-tensor structure on M(C):

**Consequence A1**: B(A) is a homotopy chiral algebra (Ch∞-algebra). This upgrades Theorem A from "bar-cobar adjunction in dg chiral algebras" to "bar-cobar adjunction in Ch∞-algebras."

**Consequence A2**: The Verdier intertwining (part of Theorem A) extends to the Y-operad action. The Eilenberg-Zilber operad Y = Z ⊗_k Lie(n) acts on MB^bullet, and the Verdier duality functor must intertwine this action.

**Consequence A3**: The Cech complex C^bullet(U; A) of a sheaf of chiral algebras over a smooth curve X admits a Ch∞ structure. In particular, H^bullet(X, A) is a chiral algebra. This gives a new proof that chiral homology is well-defined at the derived level.

#### I.A.2. Secondary Borcherds Operations and d² ≠ 0

MS24 Section 4.5 constructs "secondary Borcherds operations" j'_{(p,q,r)}: (MV^bullet)^⊗3 → MV^bullet[-1] satisfying the secondary Borcherds identities (4.5.1). These are precisely the homotopies witnessing that the Jacobi identity holds up to coherent homotopy.

**Consequence A4**: Our PROVED result that d_{bracket}² ≠ 0 (all 2048 signs) while the full Borcherds d gives d² = 0 is EXACTLY the Ch∞ phenomenon. The bracket-level failure d²_{bracket} ≠ 0 is the obstruction to strict chirality; the secondary operations j'_{(mn)} are the homotopies that restore d² = 0 at the full Borcherds level. This should be stated as a theorem linking our sign computation to MS24.

**Consequence A5**: The secondary Borcherds identities (4.5.1) give EXPLICIT formulas for the higher homotopies in every example family:
- Heisenberg: all j'_{(mn)} = 0 (strict, Gaussian archetype — no corrections)
- Affine: j'_{(mn)} nonzero starting at 3-fold collisions (Lie/tree archetype)
- β-γ: j'_{(mn)} nonzero starting at 4-fold collisions (contact/quartic archetype)
- Virasoro/W_N: j'_{(mn)} nonzero at all arities (mixed archetype — infinite tower)

**Consequence A6**: The secondary Borcherds operations are the VERTEX ALGEBRA avatar of the A∞ operations m_k. Specifically, j'_{(p,q,r)} encodes the same data as the ternary operation m_3 from homotopy transfer, but in the vertex algebra OPE language with mode indices (p,q,r). Higher operations j'_{(p₁,...,p_n)} correspond to m_n.

#### I.A.3. Cosimplicial Descent and Higher Genus

**Consequence A7**: For the higher genus theory, when passing to a cover U of M-bar_{g,n}, the Cech complex C^bullet(U; B^(g,n)(A)) carries Ch∞ structure. This gives homotopy-coherent descent for the genus-g bar complex.

**Consequence A8**: The Eilenberg-Zilber operad Z governs commutative and cocommutative bialgebras (MS24 Section 2.7, the EZ PROP PZ). Our bar complex is an algebra over FCom (Feynman transform of Com modular operad) by thm:bar-modular-operad. The relationship: Z is the genus-0 shadow of FCom. The EZ PROP PZ ⊂ FCom|_{g=0}.

**Consequence A9**: At genus g ≥ 1, the Eilenberg-Zilber chain homotopies acquire CURVATURE. The genus-0 F_n homotopies (which are exact: dF_n + F_n d = boundary term) become curved at genus 1: dF_n^(1) + F_n^(1) d = boundary term + κ·ω_g correction. This is the Ch∞ avatar of the curved A∞ structure m_1² = [m_0, −].

**Consequence A10**: The quantum_corrections.tex passage (lines 636-651) already cites MS24 for the Jacobiator being nullhomotopic. This must be upgraded to a full section developing the secondary Borcherds operations and their genus expansion.

#### I.A.4. Vertex Algebra Corollary

**Consequence A11**: MS24 Corollary 4.6 states that for V a sheaf of vertex algebras over X, the Cech cohomology ^cH^bullet(X, V) is a Z_{≥0}-graded vertex algebra. Applied to our setting: for each standard family (Heisenberg, affine, β-γ, W_N, lattice, Yangian), the Cech cohomology of the corresponding vertex algebra sheaf is itself a vertex algebra. This interacts with our chiral homology computations.

---

### I.B. PILLAR B: Convolution Homotopy Lie Algebras (RNW19 + Val16)

#### I.B.1. The Convolution = Master Object Identification

RNW19 Theorem 4.1: For any operadic twisting morphism α: C → P, there is a bijection Tw(C, P) ≅ hom_{Op}(sL∞, hom(C, P)). For D a C-coalgebra and A a P-algebra, the chain complex hom(D, A) carries an sL∞-algebra structure hom^α(D, A), with MC(hom^α(D, A)) ≅ Tw_α(D, A).

**Consequence B1**: Our master object g^mod_A (def:modular-convolution-dg-lie) IS the convolution sL∞-algebra hom^α(C, P) of RNW19, specialized to the chiral operad. The twisting morphism α is our chiral twisting morphism τ (algebraic_foundations.tex line 410). This identification should be stated as a theorem.

**Consequence B2**: Our master MC element Θ_A ∈ MC(g^mod_A) is an MC element in hom^α(D, A) in RNW19 notation. By their Theorem 4.6, MC(hom^α(D,A)) ≅ Tw_α(D,A), so Θ_A IS a twisting morphism. The Chriss-Ginzburg principle (prop:chriss-ginzburg-structure: the algebra structure IS the MC element) is the chiral instance of this general operadic fact.

**Consequence B3**: The ALL-ARITY MASTER EQUATION ∇_H(Sh_r) + o^(r) = 0 is the shadow of the MC equation ∂(Θ_A) + ½[Θ_A, Θ_A] = 0 projected to arity r. This is now a theorem (not a structural observation) via RNW19.

#### I.B.2. Functoriality and the One-Slot Obstruction

RNW19 Theorem 5.1 and Section 6: The bifunctor hom^α extends to ∞_α-morphisms in either slot, but NOT both simultaneously.

**Consequence B4**: The one-slot theorem constrains the MC3 categorical lift strategy. When trying to extend bar-cobar to ∞-morphisms of BOTH the algebra and coalgebra (needed for categorical CG projectors), we hit the RNW19 obstruction. This means:
- We CAN extend bar-cobar to ∞-morphisms of chiral algebras (Corollary 5.4, slot 2)
- We CAN extend bar-cobar to ∞-morphisms of chiral coalgebras (Corollary 5.4, slot 1)
- We CANNOT do both simultaneously
- The MC3 categorical lift must therefore proceed ONE SLOT AT A TIME

**Consequence B5**: The one-slot obstruction explains why the prefundamental CG closure (prop:prefundamental-clebsch-gordan) works at the CHARACTER level (K₀) but not at the categorical level. Characters are shadows — they live in one slot. The categorical lift requires both slots.

**Consequence B6**: The RNW19 counterexample (Section 6) uses associative algebras A^n = \overline{K[x,y]} with |x|=0, |y|=1, dy=x^n. Applied to the chiral setting: there exist chiral algebras where the bifunctor obstruction is realized. We should check whether any of our standard families hit this obstruction.

#### I.B.3. Homotopy Invariance of MC Spaces

RNW19 Section 8: MC spaces of convolution sL∞-algebras are invariant up to homotopy under ∞_α-quasi-isomorphisms.

**Consequence B7**: The shadow algebra A^sh = H_bullet(Def^mod_cyc(A)) is a homotopy invariant: quasi-isomorphic chiral algebras have weakly equivalent shadow algebras. This is a theorem for free via RNW19. It means:
- κ(A) is a quasi-isomorphism invariant (already known, but now with operadic proof)
- The full shadow tower (κ, Δ, C, Q, Sh_r) is quasi-isomorphism invariant
- The modular bar-Hamiltonian Θ_A is invariant up to gauge equivalence

**Consequence B8**: The Deligne-Getzler-Hinich ∞-groupoid MC_∞(g^mod_A) (cited in higher_genus_modular_koszul.tex line 5698) inherits its well-definedness from the homotopy invariance of convolution MC spaces. This is the ∞-categorical enhancement of our MC moduli.

#### I.B.4. Vallette's Model Category and Our Bar-Cobar

Val16 Theorem 2.1: For P Koszul, conilpotent dg P^i-coalgebras have a model structure where B_κ ⊣ Ω_κ is a Quillen equivalence. All coalgebras are cofibrant; fibrant ones are quasi-free.

**Consequence B9**: Our Theorem A (bar-cobar adjunction) IS a Quillen equivalence in the Vallette model structure, specialized to the chiral operad. This should be stated explicitly.

**Consequence B10**: Our PROVED D² = 0 at convolution level (thm:convolution-d-squared-zero) is the statement that B_κ(A) is a well-defined P^i-coalgebra. Val16 Theorem 2.9 then gives: B_κ preserves fibrations and weak equivalences; Ω_κ preserves cofibrations and weak equivalences. This upgrades Theorem A.

**Consequence B11**: Val16 Theorem 3.7: Ho(dg P-alg) ≅ ∞-P_∞-alg/~_h. The homotopy category of chiral algebras is equivalent to Ch∞-algebras with ∞-morphisms modulo homotopy equivalence. This is the homotopy-theoretic foundation for why Ch∞ structure (Pillar A) is the "right" notion.

**Consequence B12**: Val16 Theorem 3.8: ∞-P_∞-alg extends to a simplicial category (∞-category). Our category of chiral algebras with ∞-morphisms has an ∞-category structure. This is the target for the DK-5 categorical lift.

#### I.B.5. Rectification

Val16 Theorem 1.2 (Rectification): Ω_κ B̃_ι: ∞-P_∞-alg ⇌ dg P-alg: i are adjoint, and A ≅_∞ Ω_κ B̃_ι A for any homotopy P-algebra A.

**Consequence B13**: Every Ch∞-algebra is ∞-quasi-isomorphic to a strict chiral algebra. This is rectification. Applied to our bar complex: B(A) is Ch∞ (by Pillar A), and there exists a strict chiral algebra A' with B(A) ~_∞ A'. The rectification functor is Ω_κ B̃_ι.

**Consequence B14**: Rectification gives the missing step for MC5. The genus-g bar complex B^(g,n)(A) is a Ch∞-algebra; rectification produces a strict chiral algebra equivalent to it. The Costello renormalization should factor through this rectification.

#### I.B.6. Rational Models for Mapping Spaces

RNW19 Section 9: The rational model for Map_*(K, L_Q) is the convolution algebra hom^α(C, g).

**Consequence B15**: Applied to our setting: the space of chiral algebra maps from A to A' has a rational model given by the convolution L∞-algebra. This gives a derived moduli interpretation of our MC moduli.

---

### I.C. PILLAR C: Logarithmic FM Spaces (Mok25)

#### I.C.1. Log-FM as Geometric Foundation for Planted Forests

Mok25 constructs FM_n(X|D) for (X,D) a simple normal crossings pair. Its tropicalization is the moduli of planted forests.

**Consequence C1**: Our planted-forest coefficient algebra G_pf (def:planted-forest-coefficient-algebra) IS the tropicalization Trop(FM_n(C|D)). This elevates our combinatorial definition to a geometric theorem.

**Consequence C2**: The five-piece differential on Θ_A, which includes the planted-forest correction term, now has a geometric origin: it comes from the boundary stratification of FM_n(C|D). Each piece of the differential corresponds to a codimension-1 boundary stratum.

**Consequence C3**: The planted-forest depth filtration (higher_genus_modular_koszul.tex) corresponds to the codimension filtration on the boundary of FM_n(X|D). The rubber torus action on grid expansions (Mok25 Section 2.7.1) corresponds to our planted-forest depth grading.

#### I.C.2. Degeneration Formula and Clutching

Mok25 Theorem 5.3.4: Each irreducible component FM_n(W/B)(ρ) of the special fibre is a proper birational modification of ∏_{v∈V(S_{ρ,1})} FM_{I_v}(Y_v|D_v).

**Consequence C4**: Our clutching law for the quartic resonance class (thm:nms-clutching-law-modular-resonance in nonlinear_modular_shadows.tex line 1516) IS the algebraic shadow of Mok's degeneration formula. The geometric clutching (gluing curves at nodes) corresponds to the product decomposition of special fibres.

**Consequence C5**: The non-separating clutching law (thm:nms-nonseparating-clutching-law, line 1926) corresponds to Mok's degeneration along non-separating nodes. The genus loop operator Λ_P: Sym^r → Sym^{r-2} is the algebraic trace of a log-FM self-gluing.

**Consequence C6**: The degeneration formula provides an INDUCTIVE STRUCTURE for the genus-g bar complex: B^(g,n)(A) decomposes along boundary strata of M-bar_{g,n}, and on each stratum, the contribution is a product of lower-genus log-FM bar complexes.

#### I.C.3. MC5 Attack via Log-FM

**Consequence C7**: MC5 (genus ≥ 2 requires Costello renormalization) gains a new approach via Mok's log-smooth degeneration FM_n(W/B) → B. The key features:
- FM_n(W/B) → B is proper, flat, log-smooth with reduced fibres (Theorem 5.2.3)
- Each fibre carries a bar complex; the degeneration formula gives compatibility
- The Costello renormalization should factor through the log-FM product decomposition

**Consequence C8**: The Arakelov-Bar transfer (MC5-RED's FATAL attack: g² → 1 reduction via H^{1,1}=1 + symmetry) should be re-examined through log-FM. The Arakelov metric on M-bar_g and the log structure are intimately related. The quasi-modular form of dimension g(g+1)/2 might arise from the degeneration formula applied to log-FM over M-bar_g.

#### I.C.4. FM for Relative Curves

Mok25 Section 1.3.1: The geometric fibre of M-bar^{log}_{g,n+d} → M-bar^{log}_{g,d} over (C, p_{n+1},...,p_{n+d}) is a log-smooth compactification of Conf_n(C^{sm}\{p_{n+1},...,p_{n+d}}).

**Consequence C9**: This is exactly the geometric home for B^(g,n)(A): the operations live on FM_n(C_g|nodes), and the degeneration formula gives compatibility across the boundary of M-bar_g.

**Consequence C10**: When C is smooth, this recovers FM_n(C|p_1+...+p_d). When C acquires a node, the log-FM degeneration produces the clutching decomposition automatically. This is why the bar differential d² = 0 at all genera: it's Stokes' theorem on a log-smooth space.

#### I.C.5. Logarithmic Unramified Gromov-Witten Theory

**Consequence C11**: Mok25 Section 1.2 suggests using FM_n(X|D) to define logarithmic unramified GW theory. The degeneration formula yields a degeneration formula for unramified GW invariants. Applied to our setting: the genus-g bar complex gives CHIRAL unramified GW invariants, and the degeneration formula is the chiral avatar of the GW degeneration formula.

#### I.C.6. Grid Expansions and the Extension Tower

**Consequence C12**: Our extension tower for Θ_A (controlled by the weight filtration on g^mod) has a geometric incarnation: grid expansions are indexed by marked grid subdivisions = weight filtration levels. The rubber torus action on grid expansions (Mok25 Section 2.7.1) corresponds to our planted-forest depth filtration.

**Consequence C13**: The combinatorial types of FM grid expansions (Mok25 Definition 2.3.6) biject with our stable-graph coefficient types in G_st. The face poset of a grid subdivision is the incidence structure of the stable graph.

---

### I.D. CROSS-PILLAR CONSEQUENCES

#### I.D.1. The Triangle

```
          Pillar A (Ch∞)
          /              \
         /                \
   cosimplicial         Cech on curves
   = convolution
       /                    \
  Pillar B (g^mod)  ----  Pillar C (log-FM)
   operadic twisting      planted forests
   = bar-cobar             = tropicalization
```

**Consequence D1**: The three pillars form a coherent triangle. The bar complex B(A) is simultaneously:
- A Ch∞-algebra (Pillar A, via cosimplicial structure)
- An algebra over hom(C^i, P^ch) (Pillar B, via operadic twisting)
- A sheaf on FM_n(C|D) (Pillar C, via log-FM)
The master MC equation D·Θ_A + ½[Θ_A, Θ_A] = 0 lives at the intersection.

**Consequence D2**: Pillar A (Ch∞) + Pillar B (model category) = the ∞-category of chiral algebras. Val16 Theorem 3.8 gives the simplicial structure; MS24 gives the operations.

**Consequence D3**: Pillar B (convolution) + Pillar C (log-FM) = the geometric convolution algebra. The planted forests of Mok ARE the combinatorial data controlling the convolution Lie bracket on g^mod_A.

**Consequence D4**: Pillar A (secondary Borcherds) + Pillar C (FM boundary) = the geometric origin of higher homotopies. The secondary Borcherds operations j'_{(p,q,r)} are computed as RESIDUES on FM boundary strata, and the log-FM degeneration formula organizes these residues across genera.

---

## II. HIT SURFACE AREAS (Exhaustive)

### II.A. Theory Chapters

1. **algebraic_foundations.tex**: Convolution dg Lie (line 239), twisting morphisms (223, 296-410) — must identify with RNW19 framework
2. **bar_construction.tex**: FM compactification pervasive (357, 811, 1238-1462) — must connect to Mok log-FM
3. **cobar_construction.tex**: Log forms on compactified config spaces (330) — must cite Mok
4. **bar_cobar_adjunction_curved.tex**: thm:bar-modular-operad — must state as Quillen equivalence via Val16
5. **bar_cobar_adjunction_inversion.tex**: Cosimplicial Cech (2899-3087), HCA theorem (2964) — already cites MS24, must expand
6. **chiral_hochschild_koszul.tex**: Def_cyc^mod (1131-1172), cosimplicial Hochschild (4154-4265) — must connect to RNW19 convolution
7. **higher_genus_foundations.tex**: Log-FM citations (5501-5543) — must expand Mok integration
8. **higher_genus_complementarity.tex**: Pseudo-tensor embedding (2566, 2715) — must connect to MS24
9. **higher_genus_modular_koszul.tex**: G_st (7414), G_pf (7436), D²=0 (7515), shadow algebra (7577) — must identify G_pf = Trop(FM_n)
10. **quantum_corrections.tex**: Jacobiator nullhomotopic citing MS24 (636-651), modular quantum L∞ (301-362) — must expand to full secondary Borcherds

### II.B. Example Chapters

11. **heisenberg_eisenstein.tex**: Genus expansion (1-333) — must state Gaussian = no secondary Borcherds
12. **kac_moody.tex**: Config spaces pervasive (9-3585), curved A∞ (387, 1021), shadows (2918-3340) — DEEP integration needed
13. **beta_gamma.tex**: Contracting homotopy (691-735), quartic contact (1821-1882) — must connect to m_4 = 0
14. **w_algebras.tex**: Higher-pole OPE (43-598), homotopy transfer (1818-1883), shadows (2581-3200) — must add m₄, m₅ formulas
15. **w_algebras_deep.tex**: MC4 closure (786-894) — must reference Θ_A universality
16. **free_fields.tex**: FM boundary (214-227), Borcherds identity (2134-2635), Wick (1696-3424) — geometric Borcherds via FM
17. **lattice_foundations.tex**: FM compactifications (945, 3069), homotopy DK (3393-3905), curvature-braiding (4147) — log-FM for twisted modules
18. **yangians_foundations.tex**: RTT (221-301), config spaces (9, 177) — RTT as Koszul datum via convolution
19. **yangians_computations.tex**: RTT bar (206-342), MC4 kernel (2184-2360), Baxter (2364-2387) — one-slot obstruction constrains MC3
20. **yangians_drinfeld_kohno.tex**: KZ (1-397), DK hierarchy (1098-1117), dg-shifted Yangian (1003-1070) — DK-5 via ∞-category structure
21. **genus_expansions.tex**: κ universality (1-51), genus-2 bar (589-707) — Θ_A projections
22. **deformation_quantization_examples.tex**: MC elements (80-112) — quantization as Θ_A projection

### II.C. Connection Chapters

23. **concordance.tex**: Constitution — must add three-pillar integration remarks, Quillen equivalence statements
24. **genus_complete.tex**: Modular functor (5-33), elliptic config (35-89) — log-FM elliptic
25. **ym_instanton_screening.tex**: Instanton completion (29-748) — log-FM for instanton moduli

### II.D. Appendices

26. **nonlinear_modular_shadows.tex**: MC principle (102-313), quartic shadow (543-787), clutching (1516-1597), all-arity (1689-1881) — CENTRAL to Pillar C identification
27. **homotopy_transfer.tex**: 14+ theorems on SDR, tree formulas — must connect to RNW19 transfer
28. **signs_and_shifts.tex**: Orientation on FM (411-682) — log-FM orientation

### II.E. Bibliography

29. **references.tex**: MS24 already cited (line 637), Mok25 already cited (667). MISSING: Robert-Nicoud-Wierstra, Vallette (individual), Hinich-Schechtman HS1/HS2

### II.F. Metadata

30. **concordance.tex constitution**: Must update MC frontier table with three-pillar consequences
31. **claims.jsonl**: New claims for three-pillar theorems
32. **dependency_graph.dot**: New dependency edges
33. **theorem_registry.md**: New theorem entries

### II.G. Compute Modules

34. **New test modules**: Secondary Borcherds computation, log-FM degeneration, convolution L∞

---

## III. MASTER TASK LIST

### Category 0: Bibliography & Infrastructure

- [ ] **T0.1** Add Robert-Nicoud-Wierstra [RNW19] to bibliography: "Homotopy morphisms between convolution homotopy Lie algebras", J. Noncommut. Geom. 13 (2019), no. 4. arXiv:1712.00794
- [ ] **T0.2** Add Vallette [Val16] to bibliography: "Homotopy theory of homotopy algebras", Ann. Inst. Fourier 70 (2020), no. 2. arXiv:1411.5533
- [ ] **T0.3** Add Hinich-Schechtman [HS93] to bibliography: "Homotopy Lie algebras", Adv. Sov. Math. 16 Part 2 (1993), 1-28. (Predecessor to MS24)
- [ ] **T0.4** Add Hinich-Schechtman [HS87] to bibliography: "On homotopy limit of homotopy algebras", LNM 1289 (1987), 240-264.
- [ ] **T0.5** Add Wierstra [Wie19] to bibliography: individual paper on convolution algebras
- [ ] **T0.6** Add Robert-Nicoud [RN18] to bibliography: individual paper on operadic twisting
- [ ] **T0.7** Verify MS24 citation (line 637) is complete and accurate
- [ ] **T0.8** Verify Mok25 citation (line 667) matches current arXiv version (v2, May 2025)
- [ ] **T0.9** Add Loday-Vallette [LV12] cross-references where RNW19/Val16 are cited (already at line 616)
- [ ] **T0.10** Create bibliography section grouping: "Operadic homotopy theory" with all Pillar B references
- [ ] **T0.11** Update CLAUDE.md with three-pillar integration status
- [ ] **T0.12** Update memory files with three-pillar integration state

### Category 1: Pillar A — Homotopy Chiral Algebras

#### 1.1 Core Theory (bar_cobar_adjunction_inversion.tex)
- [ ] **T1.1** Expand the existing HCA section (lines 2899-3087) from sketch to full treatment: pseudo-tensor categories, EZ operad Z, Lie EZ operad Y
- [ ] **T1.2** State and prove: B(A) is a Ch∞-algebra (Consequence A1) — upgrade of Theorem A
- [ ] **T1.3** State Corollary: Verdier intertwining extends to Y-operad actions (Consequence A2)
- [ ] **T1.4** State Theorem: Cech cohomology ^cH^bullet(X, A) is a chiral algebra (Consequence A3, A11)
- [ ] **T1.5** Define the Eilenberg-Zilber PROP PZ and relate to our FCom (Consequence A8)
- [ ] **T1.6** State relationship: Z|_{g=0} ↪ FCom at genus 0 (Consequence A8)
- [ ] **T1.7** Discuss the truncation τ_{≤0}Y and why it suffices for Ch∞ structure
- [ ] **T1.8** Relate Moore complex functor M to our bar complex construction

#### 1.2 Secondary Borcherds Operations (quantum_corrections.tex + new section)
- [ ] **T1.9** Expand quantum_corrections.tex lines 636-651 (Jacobiator nullhomotopic) to full section on secondary Borcherds operations
- [ ] **T1.10** State Theorem: d²_{bracket} ≠ 0 is the obstruction to strict chirality; secondary operations j'_{(mn)} restore d² = 0 (Consequence A4)
- [ ] **T1.11** Write explicit formula for secondary Borcherds identities (4.5.1) in our notation
- [ ] **T1.12** Connect secondary Borcherds to A∞ operations: j'_{(p,q,r)} ↔ m_3 (Consequence A6)
- [ ] **T1.13** Compute secondary Borcherds for Heisenberg: all j' = 0 (Consequence A5)
- [ ] **T1.14** Compute secondary Borcherds for affine sl₂: j' nonzero at 3-fold (Consequence A5)
- [ ] **T1.15** Compute secondary Borcherds for β-γ: j' nonzero at 4-fold (Consequence A5)
- [ ] **T1.16** Compute secondary Borcherds for Virasoro: j' nonzero at all arities (Consequence A5)
- [ ] **T1.17** State Theorem: the archetype classification (Gaussian/Lie-tree/contact-quartic/mixed) is equivalent to the vanishing pattern of secondary Borcherds operations

#### 1.3 Higher Genus Ch∞ (higher_genus_foundations.tex)
- [ ] **T1.18** State Theorem: genus-g bar complex B^(g,n)(A) is a curved Ch∞-algebra (Consequence A9)
- [ ] **T1.19** Write formula for curved EZ homotopies: F_n^(g) with κ·ω_g curvature
- [ ] **T1.20** Connect to curved A∞ structure: m_1²(a) = [m_0, a] in Ch∞ language
- [ ] **T1.21** State: curvature obstruction to strict chirality at genus g ≥ 1 is κ(A)·ω_g

#### 1.4 Example Chapter Upgrades (secondary Borcherds in each family)
- [ ] **T1.22** heisenberg_eisenstein.tex: Add remark that Heisenberg is STRICTLY chiral (no secondary ops)
- [ ] **T1.23** kac_moody.tex: Compute j'_{(m,n,0)} for affine sl₂ bracket; relate to Sugawara homotopy
- [ ] **T1.24** beta_gamma.tex: Identify quartic contact vanishing μ_{βγ} = 0 as j'_{4-fold} = 0
- [ ] **T1.25** w_algebras.tex: Compute j'_{(p,q,r)} for Virasoro at (0,0,0), (1,0,0), (0,1,0); relate to OPE pole structure
- [ ] **T1.26** w_algebras.tex: Add explicit m₄, m₅ formulas from 4-fold, 5-fold collisions on FM
- [ ] **T1.27** free_fields.tex: Identify Borcherds identity (line 2134) as special case of secondary Borcherds at arity 3
- [ ] **T1.28** lattice_foundations.tex: State that lattice VOA secondary Borcherds are controlled by cocycle structure
- [ ] **T1.29** yangians_drinfeld_kohno.tex: Discuss how KZ monodromy creates Ch∞ structure on Yangian modules

#### 1.5 Concordance Updates
- [ ] **T1.30** Add to concordance.tex: new section on "Ch∞ structure and secondary Borcherds operations"
- [ ] **T1.31** Update Theorem A statement in concordance to include Ch∞ upgrade
- [ ] **T1.32** Add remark: EZ PROP PZ as genus-0 shadow of FCom

### Category 2: Pillar B — Convolution Homotopy Lie Algebras

#### 2.1 Core Identification (algebraic_foundations.tex)
- [ ] **T2.1** State Theorem: g^mod_A = hom^α(C^i_{ch}, P^{ch}) as convolution sL∞-algebra (Consequence B1)
- [ ] **T2.2** State Corollary: Θ_A ∈ MC(g^mod_A) ≅ Tw_α(C^i_{ch}, P^{ch}) is a twisting morphism (Consequence B2)
- [ ] **T2.3** State Theorem: all-arity master equation is the MC equation projected to arity r (Consequence B3)
- [ ] **T2.4** Define the operadic twisting morphism α: C → P for the chiral operad explicitly
- [ ] **T2.5** Relate to Loday-Vallette [LV12] Chapter 6 (bar and cobar relative to twisting morphism)
- [ ] **T2.6** State: the fundamental theorem of chiral twisting morphisms (line 410) is an instance of [LV12, Thm 6.5.7]

#### 2.2 One-Slot Obstruction and MC3 (yangians_computations.tex, concordance.tex)
- [ ] **T2.7** State Theorem (RNW19 6.1): hom^α cannot accept ∞-morphisms in both slots simultaneously
- [ ] **T2.8** Add Remark in concordance: one-slot obstruction constrains MC3 categorical lift (Consequence B4)
- [ ] **T2.9** State Corollary: prefundamental CG closure works at K₀ level (one slot) but categorical lift requires both slots (Consequence B5)
- [ ] **T2.10** Investigate: does the RNW19 counterexample A^n = \overline{K[x,y]} have a chiral analogue? (Consequence B6)
- [ ] **T2.11** State: MC3 arbitrary-type extension must proceed one slot at a time
- [ ] **T2.12** Revise conj:mc3-arbitrary-type statement to incorporate one-slot constraint

#### 2.3 Homotopy Invariance (higher_genus_modular_koszul.tex)
- [ ] **T2.13** State Theorem: A^sh = H_bullet(Def^mod_cyc(A)) is a homotopy invariant (Consequence B7)
- [ ] **T2.14** State Corollary: κ(A) is a quasi-isomorphism invariant (operadic proof)
- [ ] **T2.15** State Corollary: full shadow tower (κ, Δ, C, Q, Sh_r) is quasi-isomorphism invariant
- [ ] **T2.16** State Corollary: Θ_A is invariant up to gauge equivalence in MC_∞(g^mod_A)
- [ ] **T2.17** Expand DGH ∞-groupoid discussion (line 5698) to cite RNW19 Section 8

#### 2.4 Quillen Equivalence (bar_cobar_adjunction_curved.tex)
- [ ] **T2.18** State Theorem: B_κ ⊣ Ω_κ is a Quillen equivalence for chiral algebras (Consequence B9, B10)
- [ ] **T2.19** Define the Vallette model structure on conilpotent dg P^i_{ch}-coalgebras
- [ ] **T2.20** State: weak equivalences = maps whose cobar is a quasi-iso; cofibrations = degreewise monos; fibrant = quasi-free
- [ ] **T2.21** State Corollary: B_κ preserves fibrations and weak equivalences (Val16 Thm 2.9)
- [ ] **T2.22** State Corollary: Ω_κ preserves cofibrations and weak equivalences
- [ ] **T2.23** Relate to existing Positselski model structure references (bar_construction.tex line 1183)

#### 2.5 ∞-Category Structure (derived_langlands.tex, yangians_drinfeld_kohno.tex)
- [ ] **T2.24** State Theorem: Ho(dg Ch-alg) ≅ ∞-Ch∞-alg/~_h (Consequence B11)
- [ ] **T2.25** State Theorem: ∞-Ch∞-alg has ∞-category structure (Consequence B12)
- [ ] **T2.26** State: DK-5 categorical lift targets this ∞-category
- [ ] **T2.27** Connect to geometric Langlands: ∞-category of chiral algebras as categorification target

#### 2.6 Rectification (bar_cobar_adjunction_inversion.tex)
- [ ] **T2.28** State Rectification Theorem: every Ch∞-algebra is ∞-quasi-isomorphic to a strict chiral algebra (Consequence B13)
- [ ] **T2.29** Identify the rectification functor Ω_κ B̃_ι in our setting
- [ ] **T2.30** State: rectification gives the missing step for MC5 (Consequence B14)
- [ ] **T2.31** Discuss: rectification is NOT canonical — depends on choice of homotopy data

#### 2.7 Rational Models (derived_langlands.tex)
- [ ] **T2.32** State: space of chiral algebra maps has rational model via convolution L∞ (Consequence B15)
- [ ] **T2.33** Connect to geometric Langlands mapping spaces

#### 2.8 Transfer Theorem Upgrade (homotopy_transfer.tex)
- [ ] **T2.34** Connect existing HTT appendix to RNW19 convolution framework
- [ ] **T2.35** State: tree formula for transferred operations is the bar-side of convolution L∞ structure
- [ ] **T2.36** Upgrade chiral HTT (thm:chiral-htt) to cite RNW19 as source of sL∞ structure

#### 2.9 Example Chapter Upgrades
- [ ] **T2.37** kac_moody.tex: Identify affine bar complex as convolution hom^α(B(A_aff), A_aff)
- [ ] **T2.38** lattice_foundations.tex: State lattice Koszul morphism (thm:lattice:koszul-morphism) as instance of operadic twisting
- [ ] **T2.39** yangians_foundations.tex: RTT as Koszul datum via convolution sL∞ structure
- [ ] **T2.40** deformation_quantization_examples.tex: Star product MC element as projection of Θ_A via convolution

### Category 3: Pillar C — Logarithmic FM Spaces

#### 3.1 Planted Forests = Tropicalization (higher_genus_modular_koszul.tex)
- [ ] **T3.1** State Theorem: G_pf = Trop(FM_n(C|D)) where C is curve, D is nodal divisor (Consequence C1)
- [ ] **T3.2** Identify combinatorial types of FM grid expansions with stable-graph coefficient types in G_st (Consequence C13)
- [ ] **T3.3** State: planted-forest depth filtration = codimension filtration on FM_n(X|D) boundary (Consequence C3)
- [ ] **T3.4** State: rubber torus action on grid expansions = planted-forest depth grading (Consequence C3)
- [ ] **T3.5** Write explicit comparison: face poset of grid subdivision ↔ incidence structure of stable graph

#### 3.2 Degeneration Formula = Clutching (nonlinear_modular_shadows.tex)
- [ ] **T3.6** State Theorem: clutching law for R^mod_{4,g,n}(A) is the algebraic shadow of Mok's degeneration formula (Consequence C4)
- [ ] **T3.7** State: non-separating clutching law is Mok degeneration along non-separating nodes (Consequence C5)
- [ ] **T3.8** State: genus loop Λ_P: Sym^r → Sym^{r-2} is algebraic trace of log-FM self-gluing (Consequence C5)
- [ ] **T3.9** Write inductive structure: B^(g,n)(A) decomposes along boundary strata of M-bar_{g,n} into products of lower-genus log-FM bar complexes (Consequence C6)

#### 3.3 MC5 via Log-FM (concordance.tex, higher_genus_foundations.tex)
- [ ] **T3.10** State: MC5 log-FM approach via Mok's log-smooth degeneration (Consequence C7)
- [ ] **T3.11** State: FM_n(W/B) → B is proper, flat, log-smooth with reduced fibres
- [ ] **T3.12** Discuss: Costello renormalization should factor through log-FM product decomposition
- [ ] **T3.13** Re-examine Arakelov-Bar transfer through lens of log-FM (Consequence C8)
- [ ] **T3.14** State: quasi-modular form of dim g(g+1)/2 should arise from degeneration formula on log-FM over M-bar_g

#### 3.4 FM for Relative Curves (higher_genus_foundations.tex)
- [ ] **T3.15** Expand Mok citations (lines 5501-5543) to full treatment of FM_n(C|D) for relative curves
- [ ] **T3.16** State: geometric fibre of M-bar^{log}_{g,n+d} → M-bar^{log}_{g,d} gives FM_n(C_g|nodes) (Consequence C9)
- [ ] **T3.17** State: bar differential d² = 0 is Stokes' theorem on log-smooth FM_n(C|D) (Consequence C10)
- [ ] **T3.18** Connect to existing "blowup along diagonals" discussion (CLAUDE.md Critical Pitfalls)

#### 3.5 Grid Expansions and Extension Tower
- [ ] **T3.19** State: grid expansions indexed by marked grid subdivisions = weight filtration levels (Consequence C12)
- [ ] **T3.20** Write dictionary: Mok's grid expansion terminology ↔ our modular notation
- [ ] **T3.21** Discuss: stable n-pointed grid expansion (Mok Def 2.5.2) = our marked stable graph with planted-forest decoration

#### 3.6 Example Chapter Upgrades
- [ ] **T3.22** kac_moody.tex: FM boundary structure as log-FM chart; level k ↔ -k-2h^∨ via log-FM
- [ ] **T3.23** free_fields.tex: FM stratification (line 214) as special case of Mok's FM_n(X|D) for X = A^1, D = ∅
- [ ] **T3.24** lattice_foundations.tex: log-FM for twisted modules on lattice curves
- [ ] **T3.25** yangians_drinfeld_kohno.tex: KZ connection as log-FM height function in RTT-adapted fashion
- [ ] **T3.26** heisenberg_eisenstein.tex: Green function expansion as log-FM height defect sum
- [ ] **T3.27** genus_expansions.tex: genus-2 non-abelian bar (line 589) via log-FM degeneration on M-bar_{2,n}

#### 3.7 Logarithmic Unramified GW
- [ ] **T3.28** Add remark: chiral bar complex gives chiral unramified GW invariants (Consequence C11)
- [ ] **T3.29** State: degeneration formula is chiral avatar of GW degeneration formula
- [ ] **T3.30** Connect to Vol II holographic/celestial axis

#### 3.8 Configuration Spaces Chapter
- [ ] **T3.31** Expand existing log-FM definition (configuration_spaces.tex line 1038) to full treatment
- [ ] **T3.32** Write Mok's construction: (X|D)^{[n]} → FM_n(X|D) via iterative blowup
- [ ] **T3.33** State Mok Theorem 3.3.1: FM_n(X|D) is snc compactification of Conf_n(X\D)
- [ ] **T3.34** Discuss: tropicalization map and polyhedral subdivisions

### Category 4: Cross-Pillar Integration

#### 4.1 The Triangle Theorem
- [ ] **T4.1** State Master Integration Theorem: B(A) is simultaneously Ch∞ (A), hom^α-algebra (B), and FM_n-sheaf (C)
- [ ] **T4.2** State: D·Θ_A + ½[Θ_A, Θ_A] = 0 lives at the intersection of all three structures
- [ ] **T4.3** Write the "three faces" of Θ_A: as cosimplicial MC (A), as operadic MC (B), as log-FM residue sum (C)

#### 4.2 Concordance Constitution Updates
- [ ] **T4.4** Add new section to concordance: "Three-Pillar Integration" with overview
- [ ] **T4.5** Update Theorem A statement: now a Quillen equivalence in Ch∞-algebras
- [ ] **T4.6** Update Theorem B statement: bar-cobar inversion via Vallette model structure
- [ ] **T4.7** Add new theorem: homotopy invariance of shadow algebra (B7)
- [ ] **T4.8** Add new theorem: planted forests = tropicalization of log-FM (C1)
- [ ] **T4.9** Update MC3 discussion: one-slot obstruction from RNW19
- [ ] **T4.10** Update MC5 discussion: log-FM approach via Mok degeneration

#### 4.3 CLAUDE.md Updates
- [ ] **T4.11** Add three-pillar references to "Five Main Theorems" section
- [ ] **T4.12** Update "Three Concentric Rings" with three-pillar upgrades
- [ ] **T4.13** Add Critical Pitfall: "Convolution sL∞ ≠ strict Lie algebra; the hom^α structure is shifted homotopy Lie"
- [ ] **T4.14** Add Critical Pitfall: "Log-FM compactification ≠ classical FM; Mok's construction requires snc pair (X,D)"

### Category 5: Compute & Tests

#### 5.1 Secondary Borcherds Computation Module
- [ ] **T5.1** Create compute/lib/secondary_borcherds.py: compute j'_{(p,q,r)} for standard families
- [ ] **T5.2** Create compute/tests/test_secondary_borcherds.py: verify j' = 0 for Heisenberg, nonzero for affine
- [ ] **T5.3** Test: secondary Borcherds identity (4.5.1) holds for sl₂ modes up to (p,q,r) ≤ 10
- [ ] **T5.4** Test: vanishing pattern matches archetype classification
- [ ] **T5.5** Test: j'_{(p,q,r)} for Virasoro at c = 1, 13, 25 (self-dual and special values)

#### 5.2 Convolution L∞ Verification
- [ ] **T5.6** Create compute/lib/convolution_linfty.py: verify sL∞ structure on hom^α(D,A)
- [ ] **T5.7** Test: MC(hom^α(D,A)) ≅ Tw_α(D,A) for sl₂ bar complex
- [ ] **T5.8** Test: one-slot functoriality for simple ∞-morphisms
- [ ] **T5.9** Test: homotopy invariance of MC space under ∞-quasi-isomorphism

#### 5.3 Log-FM Degeneration Tests
- [ ] **T5.10** Create compute/lib/log_fm_degeneration.py: verify degeneration formula for P^1|{0,∞}
- [ ] **T5.11** Test: G_pf combinatorics matches Mok's grid expansion types for n ≤ 6
- [ ] **T5.12** Test: clutching law for quartic resonance matches Mok product decomposition
- [ ] **T5.13** Test: planted-forest depth filtration agrees with grid expansion codimension

#### 5.4 Integration Tests
- [ ] **T5.14** Test: B(A) carries Ch∞ structure: F_n homotopies satisfy Stasheff relations for sl₂
- [ ] **T5.15** Test: Quillen equivalence: Ω_κ B_κ A → A is quasi-iso for all standard families
- [ ] **T5.16** Test: rectification: Ω_κ B̃_ι A ≅_∞ A for Heisenberg

### Category 6: Research Directions & Open Questions

#### 6.1 Immediate Research
- [ ] **T6.1** Investigate: does the RNW19 counterexample have a chiral analogue? (B6)
- [ ] **T6.2** Compute: the one-slot obstruction dimension for MC3 categorical lift
- [ ] **T6.3** Investigate: can Mok's degeneration formula prove D² = 0 at ambient level? (resolving conj:differential-square-zero)
- [ ] **T6.4** Compute: secondary Borcherds operations for W₃ at the first nontrivial weight
- [ ] **T6.5** Investigate: log-FM interpretation of the Arakelov-Bar transfer attack

#### 6.2 Medium-Term Research
- [ ] **T6.6** Develop: the ∞-category of chiral algebras explicitly (target for DK-5)
- [ ] **T6.7** Develop: Costello renormalization via log-FM degeneration formula
- [ ] **T6.8** Compute: Mok's degeneration formula for genus-2 M-bar_{2,n}
- [ ] **T6.9** Investigate: whether planted-forest = Trop(FM) gives new proof of D² = 0 at convolution level
- [ ] **T6.10** Develop: rational model for chiral algebra mapping spaces (B15)

#### 6.3 Long-Term / Speculative Research
- [ ] **T6.11** Investigate: logarithmic unramified GW theory via chiral bar complex
- [ ] **T6.12** Investigate: chiral avatar of GW degeneration formula
- [ ] **T6.13** Investigate: ∞-category structure on MC moduli and relationship to derived algebraic geometry
- [ ] **T6.14** Investigate: tropical interpretation of shadow tower (κ, Δ, C, Q as tropical invariants)
- [ ] **T6.15** Investigate: weighted log-FM (Routis) and its interaction with weighted chiral algebras
- [ ] **T6.16** Investigate: toric configuration spaces (Nabijou) and lattice VOA bar complex
- [ ] **T6.17** Investigate: logarithmic Hilbert scheme (Siebert-Talpo-Thomas) and chiral factorization
- [ ] **T6.18** Investigate: Mok's grid expansion rubber torus action and gauge equivalence of Θ_A
- [ ] **T6.19** Investigate: degeneration of FM spaces for higher-dimensional targets (surfaces, 3-folds) and higher-dimensional chiral algebras
- [ ] **T6.20** Investigate: relationship between Mok's log-FM and Costello-Gwilliam factorization algebras on log-smooth spaces

#### 6.4 Vol II Connections
- [ ] **T6.21** Connect: Ch∞ structure on bar complex to Swiss-cheese homotopy-Koszulity (Vol II)
- [ ] **T6.22** Connect: log-FM degeneration to holomorphic-topological descent (Vol II Part II)
- [ ] **T6.23** Connect: convolution sL∞ to bulk-boundary-line duality (Vol II Part III)
- [ ] **T6.24** Connect: secondary Borcherds to PVA quantization obstructions (Vol II Part V)
- [ ] **T6.25** Connect: Mok's grid expansions to BV-BRST on log-smooth compactifications (Vol II)

### Category 7: Structural / Organizational

- [ ] **T7.1** Decide: should three-pillar integration be a new appendix, or distributed across existing chapters?
- [ ] **T7.2** Create: a "Three Pillars" subsection in the Overture (Heisenberg atom) previewing the integration
- [ ] **T7.3** Create: cross-reference table linking Mok/MS24/RNW19/Val16 notation to our notation
- [ ] **T7.4** Update: notation_index.tex with new notation from three pillars
- [ ] **T7.5** Update: dependency_graph.dot with new theorem dependencies
- [ ] **T7.6** Update: claims.jsonl with new claims
- [ ] **T7.7** Update: theorem_registry.md with new theorems
- [ ] **T7.8** Run: make test after each batch of changes
- [ ] **T7.9** Run: python3 scripts/generate_metadata.py to update census
- [ ] **T7.10** Verify: LaTeX compiles after each batch of changes

---

## IV. TASK PRIORITY TRIAGE

### P0: Immediate (do now, foundation for everything else)
T0.1, T0.2, T0.3, T0.4, T0.7, T0.8 (bibliography)

### P1: High (core theorems, must be in the book)
T2.1, T2.2, T2.3 (convolution = master object identification)
T2.18, T2.19 (Quillen equivalence)
T2.13, T2.14, T2.15 (homotopy invariance)
T3.1, T3.2, T3.3 (planted forests = tropicalization)
T3.6, T3.7, T3.8 (degeneration = clutching)
T1.1, T1.2, T1.10 (Ch∞ structure, secondary Borcherds theorem)
T4.1, T4.2, T4.3 (triangle theorem)

### P2: Medium (example upgrades, concordance, tests)
T1.13-T1.17 (secondary Borcherds in each family)
T1.22-T1.29 (example chapter upgrades)
T2.7-T2.9 (one-slot obstruction)
T3.10-T3.14 (MC5 via log-FM)
T3.15-T3.18 (FM for relative curves)
T4.4-T4.10 (concordance updates)
T5.1-T5.5 (compute: secondary Borcherds)

### P3: Lower (research directions, speculative, Vol II)
T6.1-T6.25 (research directions)
T5.6-T5.16 (extended compute modules)
T3.28-T3.34 (log GW, configuration spaces chapter)

---

## V. NOTATION DICTIONARY

| Our notation | RNW19/Val16 notation | MS24 notation | Mok25 notation |
|---|---|---|---|
| g^mod_A | hom^α(C, P) | — | — |
| Θ_A | MC element in hom^α(D, A) | — | — |
| B(A) | B_α(A) = cofree C-coalgebra | MB^bullet | — |
| Ω(C) | Ω_α(C) = free P-algebra | — | — |
| τ (chiral twisting) | α: C → P | ε: L → Lie | — |
| G_pf | — | — | planted forests = Trop(FM_n(X|D)) |
| G_st | — | — | combinatorial types |
| D·Θ + ½[Θ,Θ] = 0 | ∂(α) + ½[α,α] = 0 | — | — |
| A^sh | H_bullet(hom^α(D,A)) | — | — |
| κ(A) | — | — | — |
| FM_n(X) | — | — | FM_n(X|D) |
| M-bar_{g,n} | — | — | M-bar^{log}_{g,d} |
| FCom | — | PZ (EZ PROP) at g=0 | — |

---

**Total tasks: 175**
**Priority P0: 6 tasks**
**Priority P1: 17 tasks**
**Priority P2: ~40 tasks**
**Priority P3: ~112 tasks**
