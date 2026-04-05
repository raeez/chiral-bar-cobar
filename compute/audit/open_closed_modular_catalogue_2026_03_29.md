# Systematic Catalogue: Open/Closed Modular E1 Chiral Homotopy Theory
## Beilinson-filtered ideas for the platonic ideal rewrite

Date: 2026-03-29

## I. Core Primitives (survive the deepest Beilinson pass)

### 1. The primitive object is a cyclic open factorization dg-category

**Status**: Defined in Vol II foundations.tex (def:oc-factorization-category, line 801).
**What exists**: The bordified curve (def:bordified-curve), mixed configuration spaces (def:mixed-config), and the categorical open sector are all defined. The boundary-algebra-from-vacuum theorem (thm:boundary-algebra-from-vacuum) and bulk-as-derived-center corollary (cor:bulk-derived-center-categorical) are proved.
**What is missing**: The global factorization descent theorem (gluing local open categories across the curve) is conjectural (sec:global in BBL core).
**Landing**: Vol II Part I (foundations.tex) and Part III (BBL core).

### 2. A boundary algebra is only a chart on the open sector

**Status**: Proved in Vol II foundations.tex (thm:boundary-algebra-from-vacuum).
**What exists**: The theorem that RHom(b,b) is an A∞-chiral algebra is proved. Morita invariance is stated.
**What is missing**: Nothing locally. The Morita-categorical perspective could be sharpened editorially.
**Landing**: Vol II Part I.

### 3. The bulk is the chiral derived center

**Status**: Proved in two independent ways:
- Vol I en_koszul_duality.tex: operadic center theorem (thm:operadic-center-hochschild) + chiral Deligne-Tamarkin (thm:chiral-deligne-tamarkin in chiral_center_theorem.tex)
- Vol II foundations.tex: categorical center (cor:bulk-derived-center-categorical)
- Vol II BBL core: boundary-linear LG theorem (thm:boundary-linear-bulk-boundary)
**What exists**: Complete local proofs from multiple angles.
**What is missing**: The 2d→3d conceptual explanation could be made more explicit as a named principle.
**Landing**: Vol I Part III (en_koszul_duality.tex), Vol II Parts I and III.

### 4. Bar/cobar classifies twisting data, not bulk observables

**Status**: Proved in Vol I (bar_cobar_adjunction_curved.tex). The Loday-Vallette universal twisting representability is used throughout.
**What exists**: The distinction between bar (twisting) and center (bulk) is clear in the concordance (concordance.tex principal contribution 9).
**What is missing**: The split could be made more explicit editorially — some exposition still conflates bar and bulk.
**Landing**: Vol I Part I, Vol II Part I.

### 5. Modularity = trace + clutching on the open sector

**Status**: Partially formalized. The loop-Connes bridge conjecture (conj:vol2-loop-connes-bridge in concordance.tex) states it. The curved looping section (foundations.tex subsec:curved-looping-coderived) treats the genus tower. The E1 ribbon/'t Hooft section (e1_modular_koszul.tex sec:e1-ribbon-thooft) treats cyclic traces.
**What exists**: Scattered pieces in both volumes.
**What is missing**: A single named principle unifying trace, ribbon, and modular structures as successive shadows of the open category's cyclic structure. This should be formalized.
**Landing**: Vol II Part I (foundations.tex) and concordance.

## II. The 2d → 3d mechanism

### 6. Chiral Deligne-Tamarkin-Swiss-cheese theorem

**Status**: PROVED in Vol I (thm:chiral-deligne-tamarkin, thm:operadic-center-hochschild).
**What exists**: The full operadic proof and the direct brace-algebra proof.
**What is missing**: An explicit remark making the conceptual chain crystal clear:
  A∞-chiral boundary → C_ch(A,A) = universal bulk → (C_ch(A,A), A) ∈ Alg_{W(SC^{ch,top})} → local 3d HT theory
This should reference the recognition theorem (thm:recognition in foundations.tex).
**Landing**: Vol I Part III (en_koszul_duality.tex), with forward reference to Vol II.

### 7. Khan-Zeng PVA-to-3d-HT realization

**Status**: Referenced but not deeply integrated. frontier_modular_holography_platonic.tex cites KhanZeng25 in the deformation-quantization conjecture context. The 3d_gravity.tex file doesn't cite it at all.
**What exists**: The PVA descent theorem (Vol II thm:cohomology-PVA-main) provides the A∞→PVA functor. Khan-Zeng provides the PVA→3d-HT functor. Together they complete the chain.
**What is missing**: (a) The degree constraint d+2=2d+k forcing (d,k)=(1,1) for a one-variable PVA; (b) the Virasoro enhancement theorem (inner Virasoro makes HT → topological); (c) the explicit connection to the existing holographic datum.
**Landing**: Vol I frontier chapter, Vol II Part V (3d gravity, modular PVA quantization).

### 8. The propagator factorization

**Status**: Not explicitly stated as a theorem in either volume.
**What exists**: The mixed propagator P(t,z) ~ Θ(t)·1/(2πiz) is implicit in the FM calculus and the spectral braiding sections.
**What is missing**: A clean proposition stating that the Green kernel of d_t + ∂̄ factorizes as step function × Cauchy kernel, explaining why local operation spaces are products FM_k(C) × Conf_m(R).
**Landing**: Vol II Part II (fm-calculus.tex) or Part I (foundations.tex).

## III. The exact local models

### 9. Boundary-linear Landau-Ginzburg sector

**Status**: FULLY PROVED in Vol II BBL core (thm:boundary-linear-bulk-boundary, thm:dcrit-shiftedcot, cor:free-polarization).
**What exists**: Complete local theorem package: boundary dg algebra, derived zero locus, shifted cotangent, derived center = dCrit(W).
**What is missing**: Nothing locally. The chiral/jet chiralization of A_F could be made more explicit.
**Landing**: Vol II Part III.

### 10. One-step Jacobi coalgebra and exact pointed line algebra

**Status**: PROVED in Vol II BBL core (thm:exact-line, cor:explicit-line).
**What exists**: Complete construction with explicit A∞ formulas from Taylor coefficients.
**What is missing**: Nothing. This is the cleanest exact model in the programme.
**Landing**: Vol II Part III.

### 11. Boundary Kuranishi elimination

**Status**: PROVED in Vol II BBL core (thm:boundary-kuranishi, thm:minimal-pointed-line).
**What exists**: Full implicit-function-theorem reduction to minimal line algebra.
**What is missing**: The recursive formula for effective couplings could be computed more explicitly for the standard families.
**Landing**: Vol II Part III.

### 12. The fortified local triangle

**Status**: PROVED in Vol II BBL core (thm:fortified-local-triangle, thm:line-mather-yau).
**What exists**: Local bulk/boundary/line triangle with Mather-Yau classification.
**What is missing**: The global extension is conjectural.
**Landing**: Vol II Part III.

## IV. Applications to quantum gravity and holography

### 13. Gravitational Koszul triangle (3d gravity)

**Status**: PROVED except Cardy formula. Vol II 3d_gravity.tex (thm:gravity-koszul-triangle, thm:gravity-mc).
**What exists**: Boundary = Vir_c, Lines = Vir_{26-c}-mod, Bulk = C[[c]]. Brown-Henneaux. BTZ as MC deformation.
**What is missing**: (a) Cardy formula from MC moduli (prop:cardy-mc, conjectural); (b) explicit quartic shadow correction from Vol I's shadow obstruction tower.
**Landing**: Vol II Part V.

### 14. Holographic modular Koszul datum

**Status**: DEFINED and partially proved. Vol I frontier chapter (def:holographic-modular-koszul-datum). 43 proved claims, 8 conjectures.
**What exists**: Six-tuple H(T) = (A, A!, C, r(z), Θ_A, ∇^hol). Protected dual transform. Collision filtration. Recovery theorems. Factorization-envelope shadow functor.
**What is missing**: 8 conjectures, each with a single identified obstruction (reduction table in frontier chapter).
**Landing**: Vol I Part IV (frontier chapter).

### 15. S-duality as Koszul duality

**Status**: CONJECTURED in Vol I holomorphic_topological.tex (conj:ht-s-duality-koszul). Proved for affine KM at generic level.
**What exists**: The conjecture and one proved instance.
**What is missing**: Extension beyond affine KM.
**Landing**: Vol I Part III (holomorphic_topological.tex).

### 16. Celestial holography and boundary transfer

**Status**: Sketched in both volumes. Vol I holomorphic_topological.tex has a summary section. Vol II has celestial_boundary_transfer_core.tex and celestial_holography_core.tex.
**What exists**: The wedge A∞ construction and obstruction tower.
**What is missing**: Full development as formal theorems rather than discursive summaries.
**Landing**: Vol I Part III, Vol II Parts III and VII.

## V. Modular and logarithmic geometry

### 17. Log-Fulton-MacPherson compactifications (Mok)

**Status**: Used throughout Vol I (thm:ambient-d-squared-zero depends on Mok25 Thm 3.3.1). Referenced in Vol II BBL core (line 2307).
**What exists**: The dependency on Mok is flagged in concordance with fallback clauses.
**What is missing**: A systematic treatment of how log-FM strata produce the planted-forest corrections at codimension ≥ 2 in the modular cooperad. The quartic logarithmic contact class q_4 is the first genuinely new object.
**Landing**: Vol I (higher_genus_modular_koszul.tex, nonlinear_modular_shadows.tex), Vol II Part III (BBL core).

### 18. Quartic logarithmic contact class

**Status**: NOT YET DEFINED as a named object.
**What exists**: Vol I's quartic resonance class (R^mod_{4,g,n}(A) in nonlinear_modular_shadows.tex) and the clutching law via Mok's degeneration. Vol II BBL core has the modular homotopy type.
**What is missing**: A new proposition defining q_4 ∈ H^2(gr_4 M_{≤4}(A)) as the first logarithmic modular obstruction, proving it vanishes in the boundary-linear LG sector.
**Landing**: Vol II Part III (BBL core).

### 19. Shadow obstruction tower as open-sector trace expansion

**Status**: Partially stated. Vol I's shadow obstruction tower (Θ_A^{≤r}) is the primary nonlinear object. The connection to open-sector traces is hinted in the E1 ribbon section and the loop-Connes conjecture.
**What is missing**: An explicit identification: the genus-g, arity-n shadow Sh_{g,n}(Θ_A) should be identified as the weight-(g,n) component of the cyclic factorization homology of C_op, i.e. the image of the modular twisting morphism Θ_C projected to weight (g,n).
**Landing**: Vol I (higher_genus_modular_koszul.tex), Vol II (foundations.tex, BBL core).

## VI. Line operators and spectral data

### 20. Line category as A!-modules

**Status**: Defined in Vol I holomorphic_topological.tex (line 89) and frontier chapter. Referenced from Vol II BBL core citing DNP25.
**What exists**: The statement C_line ≃ A!-mod. The dg-shifted Yangian package.
**What is missing**: A rigorous comparison functor between the abstract C_line and the concrete A!-mod. This is part of the global conjectural triangle.
**Landing**: Vol II Part III (line-operators.tex, BBL core).

### 21. dg-shifted Yangian and spectral transport

**Status**: PROVED at genus 0. Vol I (yangians_drinfeld_kohno.tex, yangians_foundations.tex). Vol II (spectral-braiding-core.tex).
**What exists**: The R-matrix, DK theorems, categorical CG closure (MC3 all types).
**What is missing**: The genus ≥ 1 extension of the spectral transport — this connects to the modular twisting morphism.
**Landing**: Vol I Part I (yangians chapters), Vol II Part III.

## VII. Cross-volume bridges (already catalogued in concordance)

### 22. Five proved bridges + 3 conjectural bridges

From concordance.tex sec:cross-volume-bridges:
- prop:vol2-bar-cobar-bridge (proved)
- conj:vol2-hochschild-bridge (conjectural — bulk = derived center)
- prop:vol2-dk-ybe-bridge (proved)
- prop:vol2-w-algebra-bridge (proved)
- prop:vol2-relative-holographic-bridge (proved)
- prop:vol2-ribbon-thooft-bridge (proved)
- conj:vol2-loop-connes-bridge (conjectural — modularity = open trace)
- conj:vol2-bv-functor-bridge (conjectural — analytic BV)

## VIII. Execution priority

### Tier 1 (highest impact, immediate)
- Task 2: Sharpen 2d→3d in en_koszul_duality.tex
- Task 3: Formalize modular trace principle in foundations.tex
- Task 4: Integrate Khan-Zeng into frontier chapter

### Tier 2 (high impact, requires more computation)
- Task 5: Quartic logarithmic contact class in BBL core
- Task 6: Virasoro quartic shadow in 3d gravity chapter

### Tier 3 (editorial, after Tier 1-2)
- Sharpen the bar-vs-center distinction editorially
- Connect shadow obstruction tower to open-sector trace expansion
- Update concordance with new results
