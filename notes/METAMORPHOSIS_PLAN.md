# METAMORPHOSIS PLAN — Architecture for the Expanded Monograph
# Written: Session 122, March 6 2026
# Status: ACTIVE — guides all editing decisions

---

## 1. The Narrative Arc

The reader begins with a classical observation — Poincaré duality exchanges homology and cohomology — and watches it undergo three successive deepenings. First, non-abelian Poincaré duality replaces vector spaces with algebraic structures, and configuration spaces become the geometric substrate for the resulting Koszul duality. Second, the passage from genus zero to higher genus reveals that quantum corrections are not a perturbation but the modular completion of duality itself: the genus tower is a single Maurer–Cartan deformation, and the obstruction invariant κ(A) is the first characteristic number of a universal class over the Deligne–Mumford modular operad. Third, this framework reaches into every corner of modern mathematics — derived algebraic geometry via the oper space at critical level, quantum groups via root-of-unity bar complexes, knot invariants via the Kontsevich integral, shifted symplectic geometry via the Lagrangian structure of complementarity, higher-dimensional topology via E_n propagators, and mathematical physics via the BV identification. The book's nine research programmes are not afterthoughts; they are the natural destinations toward which the three main theorems inevitably point. The examples — Heisenberg, Kac–Moody, Virasoro, W-algebras, Yangians, toroidal — are the laboratories in which this general theory becomes visible, and their invariants (the shared discriminant, the Â-genus, the complementarity sums) are its fingerprints.

---

## 2. Structural Decisions

### New Chapters (3)

**New Chapter: "Derived structures and the geometric Langlands correspondence"**
- Position: Part I (Theory), after chiral_modules.tex (Chapter 11) or as Chapter 13
- Scope: DAG prerequisites (derived stacks, cotangent complexes — M1 import level), the derived oper space Op^{dR}_{g∨}(X), the identification B̄(ĝ_{crit}) ≃ O(Op^{dR}), root-of-unity periodic CDG structure, the KL-from-bar-cobar roadmap
- Dependencies: bar_cobar_construction.tex, higher_genus.tex, kac_moody_framework.tex
- Programmes served: I (Langlands), II (KL), partially III (fusion)
- Estimated length: 40-60pp (2000-3000 lines)
- File: chapters/theory/derived_langlands.tex

**New Chapter: "E_n Koszul duality and higher-dimensional bar complexes"**
- Position: Part I (Theory), after poincare_duality_quantum.tex (Chapter 12) or as Chapter 14
- Scope: Totaro's presentation, E₂ bar complex construction, d²=0 from Totaro relations, connection to Ayala–Francis, the n=2 case in full detail, formulation for general n
- Dependencies: configuration_spaces.tex, bar_cobar_construction.tex
- Programmes served: IV (E_n)
- Estimated length: 30-50pp (1500-2500 lines)
- File: chapters/theory/en_koszul_duality.tex

**New Chapter: "Knot invariants and the Kontsevich integral"**
- Position: Part III (Connections), replacing/absorbing parts of feynman_connection.tex
- Scope: Vassiliev invariants, weight systems from bar complex, analytic continuation argument, Kontsevich integral as bar-cobar on S¹, Drinfeld associator from bar-cobar monodromy on C₃(ℂ), KZ equation
- Dependencies: bar_cobar_construction.tex, kac_moody_framework.tex, feynman_diagrams.tex
- Programmes served: V (Vassiliev)
- Estimated length: 30-40pp (1500-2000 lines)
- File: chapters/connections/kontsevich_integral.tex

### Major Expansions of Existing Chapters

| Chapter | Current lines | Programme content entering | Estimated new lines |
|---------|--------------|---------------------------|-------------------|
| kac_moody_framework.tex | 2760 | I (oper summary), II (root-of-unity summary), III (fusion) | +800 |
| higher_genus.tex | 7472 | Shifted symplectic structure, Lagrangian complementarity (DEEPAUDIT) | +600 |
| deformation_theory.tex | 1382 | VII (NC Hodge), fix F5/F6/F7 | +500 |
| yangians.tex | 1318 | VIII (shifted Yangian, CoHA, E₁ genus theory) | +600 |
| bv_brst.tex | 739 | VI-a (BV=bar rigorous, string amplitudes genus 0-1) | +800 |
| holomorphic_topological.tex | 1158 | VI-b (AGT), VI-c (CL conditions) | +600 |
| w_algebras_framework.tex | 2298 | VIII (W-orbit duality, subregular case) | +400 |
| concordance.tex | 569 | VI-d (CS as Koszul), VI-e (W∞), programme synthesis | +800 |
| toroidal_elliptic.tex | 1355 | VIII (toroidal Koszul dual, double-loop bar) | +400 |
| configuration_spaces.tex | 3942 | IV (Totaro presentation, referenced from new E_n chapter) | +300 |
| chiral_modules.tex | 4400 | III (fusion monoidality, separating-divisor coproduct) | +500 |
| introduction.tex | 1569 | Programme foreshadowing, expanded arc | +400 |
| free_fields.tex | 3540 | VI-a (elevate physics conjectures) | +300 |
| genus_expansions.tex | 2500 | V (Vassiliev connection), genus-2 extensions | +400 |

### Chapter Ordering (Expanded Book)

**Part I: Theory** (~16 chapters, up from ~14)
1. Introduction
2. Algebraic foundations (operads, Koszul duality)
3. Configuration spaces (FM compactification, OS algebra, **+Totaro for E_n**)
4. Bar and cobar constructions (**core chapter**)
5. Poincaré duality (Verdier, bar-computes-dual)
6. Higher genus extension and quantum corrections (**deepest chapter, +shifted symplectic**)
7. Chiral Koszul pairs
8. Koszul pair structure (periodicity, affine/Virasoro)
9. Chiral Hochschild cohomology and deformation theory (**+NC Hodge, fix F5/F6/F7**)
10. Chiral modules and representation theory (**+fusion monoidality**)
11. Poincaré duality: quantum corrections (modular operad, Feynman transform)
12. **NEW: E_n Koszul duality and higher-dimensional bar complexes**
13. **NEW: Derived structures and geometric Langlands**
14. Quantum corrections + filtered/curved (small chapters, possibly merge)
15. Hochschild cohomology (**+NC Hodge connection**)

**Part II: Examples** (~17 chapters, unchanged count but expanded)
16. Lattice foundations
17. Free fields (**+elevated physics conjectures**)
18. βγ-bc systems
19. Heisenberg-Eisenstein
20. Kac–Moody (**+oper summary, root-of-unity summary, fusion**)
21. W-algebras framework (**+W-orbit duality**)
22. W₃ composite fields
23. W-algebras deep (**+W∞ connection**)
24. Minimal model fusion + examples
25. Deformation quantization + examples
26. Yangians (**+shifted Yangian, CoHA, E₁ genus theory**)
27. Toroidal-elliptic (**+toroidal Koszul dual**)
28. Genus expansions (**+Vassiliev connection, genus-2**)
29. Detailed computations (**+computational expansion**)
30. Examples summary (Master Table)

**Part III: Connections and Applications** (~8-9 chapters, +1 new)
31. NAP computations
32. Feynman diagrams
33. **NEW: Knot invariants and the Kontsevich integral**
34. BV-BRST (**+rigorous BV=bar, string amplitudes**)
35. Holomorphic-topological (**+AGT, CL conditions**)
36. Physical origins (**+NC geometry, D-branes**)
37. Genus-complete theory
38. Concordance (**rewritten as programme synthesis**)

**Appendices** (14, unchanged)

---

## 3. Chapter-by-Chapter Plan

### PHASE A: THE CORE

#### A1. introduction.tex
**Stays**: Central thesis, three main theorems, modular Koszul definition, Θ_A class
**Rewrite for synthesis**:
- Opening §1.1: Replace "Classical Poincaré duality establishes an isomorphism..." with a question: "What is the correct non-abelian generalization of Poincaré duality? Classical duality exchanges homology and cohomology of a manifold — both abelian invariants. When the coefficients carry algebraic structure — when they form an algebra rather than a vector space — the duality must itself become algebraic."
- §Dictionary (line 309): Currently a catalog of definitions. Transform into a flowing narrative: the three levels E∞/E₁/P∞ arise not from abstract classification but from the geometry of collision patterns — E∞ from symmetric configuration spaces, E₁ from ordered configurations, P∞ from the Poisson structure on the classical limit.
- §Relationship to foundational work (line 234): Currently a laundry list. Rewrite as synthesis: each prior work is a face of the same phenomenon, and the monograph's contribution is the geometric mechanism (configuration space integrals) that reveals their unity.
- **New content**: After §central-thesis, add "§The nine programmes" (2-3 pages) foreshadowing how the three theorems point toward Langlands, quantum groups, knot theory, E_n duality, BV formalism, NC Hodge, and mathematical physics. Not a list — a narrative showing how each programme emerges inevitably from the theorems.
- **Shadow sentence** after Theorem A statement: "This equivalence, when specialized to the critical level k = −h∨, produces the derived oper space of geometric Langlands (Chapter X); when restricted to S¹ ⊂ ℂ, it produces the Kontsevich integral (Chapter Y)."

#### A2. bar_cobar_construction.tex
**Stays**: All proved content (84 PH claims)
**Rewrite for synthesis**:
- Opening already strong ("The bar construction is the point where three mathematical traditions converge"). Keep but sharpen: add the E_n shadow — "In dimension one, collision patterns on a curve produce chiral bar-cobar duality; in dimension n, collision patterns on an n-manifold produce E_n bar-cobar. This chapter treats the foundational case n = 1 in full; Chapter X develops the general theory."
- After Prop prop:pole-decomposition (the d_res = d_bracket + d_curvature theorem), add a shadow sentence connecting to BV: "The decomposition d = d_bracket + d_curvature is the geometric shadow of the physicist's decomposition Q_BV = Q_BRST + ħΔ; the curvature term is the quantum correction (Chapter ch:bv-brst)."
- The Verdier duality section: add forward reference to shifted symplectic structure (DEEPAUDIT vision)
**New content**: Brief remark pointing to the E_n chapter, establishing the n=1 case as the foundation for higher n.

#### A3. higher_genus.tex
**Stays**: All 102 PH claims, all three main theorem proofs
**Rewrite for synthesis**:
- Opening: Replace "This chapter contains the deepest results of the monograph" with: "At genus zero, bar-cobar duality is a formal consequence of operadic Koszul theory — it could be stated without reference to curves at all. The passage to higher genus reveals that the genus tower is not a perturbation but a modular completion: a single Maurer–Cartan deformation whose scalar shadow is the genus universality formula obs_g(A) = κ(A)·λ_g. This chapter proves the three main theorems and constructs the universal obstruction class Θ_A."
**New content (DEEPAUDIT shifted symplectic)**:
- After thm:quantum-complementarity-main, add a new section "§Shifted symplectic structure on the modular deformation complex" (10-15pp):
  - Define the shifted symplectic pairing on RΓ(M̄_g, Z_A) from Verdier duality on the center local system
  - Prove that the deformation space Q_g(A) and obstruction space Q_g(A!) embed as complementary Lagrangians (this strengthens the existing eigenspace proof with a richer structural result)
  - Connect to PTVV (Pantev–Toën–Vaquié–Vezzosi) shifted symplectic geometry
  - State the interpretation: what one algebra sees as tangent directions, the dual sees as obstruction directions, because both are opposite polarizations of a single ambient symplectic deformation problem
- This section is the single most important mathematical addition to the core theory. It converts rem:lagrangian-complementarity from a remark into a theorem.

#### A4. deformation_theory.tex
**Stays**: The deformation-obstruction framework, all correct proofs
**Fix F5** (~line 639): Modular periodicity — either provide correct argument (finite fusion category → eventual stabilization of bar cohomology by representation theory of rational VOAs) or strengthen scope remark + downgrade cleanly. The correct argument would use: rational VOA has finitely many simple modules, the bar complex in weight h decomposes as ⊕_i (chain groups built from module M_i spaces), and by finiteness these spaces stabilize.
**Fix F6** (~line 825): Correct "12c₁(E) = δ" to "12λ = κ₁ + δ". Attempt proof of geometric periodicity using correct tautological ring structure: the key is that in the tautological ring R*(M̄_g), the Hodge class λ satisfies Mumford's relation, and bar cohomology lives in a specific subring determined by the center local system. If this doesn't work, downgrade with precise scope remark.
**Fix F7** (~line 891): Remove the gcd/lcm contradiction. State: "Period | gcd(N_mod, N_quant, N_geom)" as the strong bound, with a remark that if the periodicities are in independent grading directions, the effective period could be lcm.
**Expand F3** (~line 374): Write out the [2] shift telescoping: "In total degree d, Koszul concentration places all contributing bar elements in bar degree n = d. The Verdier shift on C̄_{d+2}(X) carries H^d to H^{(d+2)−d,∨} = H^{2,∨}. Thus in every total degree, the Verdier shift lands in cohomological degree 2 — yielding the uniform shift HH^d(A) ≅ HH^{2−d}(A!)∨ ⊗ ω_X."
**New content (Programme VII: NC Hodge)**:
- New section "§Noncommutative Hodge structures on the genus tower" (15-20pp):
  - Import the Kontsevich–Soibelman NC Hodge framework (M1: definitions + key properties, cite KS08, KKP08)
  - Define the nc Hodge filtration on {B̄^{(g)}} using the weight filtration from the bar bigrading
  - The genus expansion parameter g_s as twistor parameter λ
  - Prove: for Koszul algebras, the Hodge-to-de-Rham spectral sequence of the chiral Hochschild complex degenerates at E₂ (this should follow from the Koszul diagonal concentration)
  - Compute NC Hodge numbers for Master Table algebras (Heisenberg, sl₂, Virasoro, W₃)

### PHASE B: THE EXPANSIONS

#### B5. kac_moody_framework.tex
**Stays**: All 31 PH claims, Feigin-Frenkel identification, screening, Wakimoto, admissible
**New content (Programme I summary)**:
- New section "§The oper space at critical level" (10pp): Summarize the derived oper space O(Op^{dR}_{g∨}), state thm:oper-bar-h0 and prop:oper-bar-h1, point forward to the new derived_langlands chapter for the full treatment
- Shadow sentence: "The zeroth cohomology of the bar complex at critical level is the algebra of functions on opers — the same opers that parametrize Hecke eigensheaves in the geometric Langlands programme. The bar complex is computing the derived structure of the Langlands correspondence."
**New content (Programme II summary)**:
- New section "§Root-of-unity structure at admissible levels" (10pp): Define periodic CDG structure, state the periodicity B̄^{n+2q} ≅ B̄^n at admissible levels, connect to KL
**New content (Programme III)**:
- New section "§Fusion monoidality" (5pp): The separating-divisor coproduct, statement of monoidality for genus 0, forward reference to chiral_modules chapter

#### B6. chiral_modules.tex
**Stays**: All 43 PH claims
**New content (Programme III)**:
- Expand the fusion product section with the separating-divisor coproduct construction
- Prove genus-0 monoidality: Φ(M₁ ⊠_A M₂) ≅ Φ(M₁) ⊠_{A!} Φ(M₂) for M₁, M₂ in O_k(ĝ), using the pants decomposition of M̄_{0,4}
- The genus-1 monoidal obstruction: relate to curvature m₀
- Connection to Verlinde formula: bar-cobar should produce the Verlinde dimensions via Euler characteristic of bar complex with module insertions

#### B7. yangians.tex
**Stays**: All 12 PH claims, RTT presentation, E₁ bar complex
**New content (Programme VIII)**:
- New section "§Shifted Yangians and Coulomb branches" (15pp):
  - BFN construction of Coulomb branches as shifted Yangian modules
  - The E₁-chiral structure on shifted Yangians: Y_μ(g) with shift μ
  - Koszul duality for shifted Yangians: formulate precisely
- New section "§Cohomological Hall algebras" (10pp):
  - CoHA as E₁-chiral algebra: the Hecke product is the E₁ multiplication
  - Factorization structure from dimension vectors
  - Connection to Yangian bar complex: CoHA should be the derived dual
- New section "§E₁ genus theory on bordered surfaces" (10pp):
  - Swiss-cheese operad structure
  - Bordered bar complex: bar on Σ_{g,b} with b boundary components
  - State the E₁ genus theory conjecture with full framework

#### B8. w_algebras_framework.tex + w_algebras_deep.tex
**Stays**: All 21 PH claims across both files
**New content (Programme VIII)**:
- New section in w_algebras_framework.tex "§W-algebras for general nilpotent orbits" (15pp):
  - The orbit-dependent DS reduction: W^k(g, e) for nilpotent e ∈ g
  - The duality conjecture: W^k(g, e)! ≅ W^{k'}(g∨, e∨) where e∨ is the Barbasch–Vogan dual
  - The subregular case: write in detail, including the subregular W-algebra for sl_3
  - Partial results toward the conjecture: principal case proved (our existing thm), subregular case partial
- New section in w_algebras_deep.tex "§W∞ and the large-N limit" (10pp):
  - W_{1+∞} as colimit of W_N
  - Bar-cobar for the colimit: define B̄(W_{1+∞}) as inverse limit
  - Connection to Gaberdiel–Gopakumar: minimal model holography as large-N Koszul duality

### PHASE C: THE EXAMPLES DEEPENED

#### C9. free_fields.tex + beta_gamma.tex
**Stays**: All 59 PH claims across both files
**Elevate physics conjectures (Programme VI-a)**:
- The string amplitude conjectures in free_fields.tex: for each one, identify the precise mathematical physics framework (Costello perturbative QFT, or BV formalism) that brings it into scope. Where possible, prove the genus-0 case and formulate the higher-genus case as a precise conjecture with mathematical hypotheses (not physics motivation).
- The bc-ghost system at c = -26: the anomaly cancellation is PROVED (thm:anomaly-koszul). Write the connection to Costello's renormalization framework: the BV quantization of the bc-ghost system is the bar complex B̄(bc), and the QME is d² = 0.

#### C10. genus_expansions.tex
**Stays**: All 32 PH claims, Three Theorems showcase
**New content (Programme V connection)**:
- New section "§From genus expansions to knot invariants" (5pp): Bridge section pointing forward to the Kontsevich integral chapter. Show how the genus expansion F_g(ĝ_k) at genus 0 produces weight systems, and how the full genus tower produces the loop expansion.
**New content (genus-2 extensions)**:
- Extend at least one algebra (sl₂ or Virasoro) from genus-1 to genus-2 using existing proved formulas (thm:genus-universality + Faber-Pandharipande). The computation is: F_2(A) = κ(A) · λ_2 where λ_2 = (2⁴-1)/2⁴ · |B_4|/(4!) = 7/16 · 1/720 · 30 = 7/384.

#### C11. detailed_computations.tex + examples_summary.tex
**Stays**: All 30 PH claims
**Programme IX (Computational expansion)**:
- sl₃ bar GF: write the E₂ page computation (spectral sequence approach)
- W₃ bar GF: write the generators-and-relations analysis supporting H⁵ = 171
- Document the H⁴(W₃) = 52 derivation (currently missing) or downgrade
- Update Master Table with any new values

### PHASE D: THE CONNECTIONS ELEVATED

#### D14. bv_brst.tex
**Stays**: All 5 PH claims
**New content (Programme VI-a: rigorous BV = bar)**:
- Expand the BV = bar identification using Costello–Gwilliam framework (M1: import the precise theorem from CG Vol 2)
- Prove the genus-0 string amplitude formula: ∫_{M̄_{0,n}} ω₁ ∧ ... ∧ ωₙ = bar complex Euler characteristic (this should follow from the existing identification)
- The genus-1 partition function: Z₁ = exp(F₁) = exp(κ/24) via bar complex. Connect to the chiral partition function.
- The QME coefficient 1/2: explain why this is the curvature m₀ = κ/2 (the factor 1/2 in the QME matches the factor 1/2 in the Sugawara formula — this is NOT a coincidence).
- Anomaly = curvature: expand the identification. The conformal anomaly c/12 on a torus is exactly F₁(Vir_c) = c/24 (Mumford isomorphism). This is PROVED.

#### D15. holomorphic_topological.tex
**Stays**: All 7 PH claims
**New content (Programme VI-c: CL conditions)**:
- Prove: the CL construction produces a genuine chiral algebra (not just factorization algebra) when the 4d theory has N=4 SUSY. The proof: N=4 ensures holomorphic dependence on the curve coordinate, the dimensional reduction preserves the conformal symmetry via the topological twist along the transverse direction, and the resulting algebra has a chiral bracket from the OPE of the reduced fields. Cite Costello-Li precisely.
- For N=2: state the conditions precisely as a theorem (sufficient conditions on the matter content).
**New content (Programme VI-b: AGT)**:
- The AGT correspondence as bar-cobar on W-algebras: W_k(gl_N) acts on the equivariant cohomology of instanton moduli M(r,n). The bar complex B̄(W_k) should correspond to the derived category D^b(Coh(M(r,n))). State this precisely, citing Schiffmann-Vasserot and Maulik-Okounkov.

#### D16. feynman_diagrams.tex + NEW kontsevich_integral.tex
**feynman_diagrams.tex stays**: All 6 PH claims, Feynman diagram interpretation
**New chapter kontsevich_integral.tex** (Programme V):
- §1: Vassiliev invariants and weight systems (mathematical setup, Bar-Natan)
- §2: Weight systems from the bar complex (our prop:vassiliev-genus0, expanded)
- §3: The analytic continuation: holomorphic → topological Feynman transforms
  - The key argument: on S¹ ⊂ ℂ, the holomorphic propagator ω_{ij} = d log(z_i - z_j) restricts to d log(e^{iθ_i} - e^{iθ_j}) = i·dθ_i·e^{iθ_i}/(e^{iθ_i} - e^{iθ_j}) + similar, which after taking the real part gives (1/2π)·d arg(t_i - t_j) + exact terms. The exact terms don't contribute to residues/weight systems by Stokes.
- §4: The Kontsevich integral as bar-cobar at genus 0 on S¹
  - Z_K(K) = ∫_{C_n(S¹)} ∏ ω^K_{ij} · W_Γ is the pairing of bar complex forms with weight systems
- §5: The Drinfeld associator from bar-cobar monodromy
  - The parallel transport of B̄(ĝ_k) around C₃(ℂ) produces Φ_KZ
  - This is the KZ equation: ∂/∂z_i Φ = (Σ_{j≠i} t_{ij}/(z_i - z_j)) Φ where t_{ij} = Ω acting on the i,j tensor factor — these are exactly the bar complex propagators!

#### D17. concordance.tex (REWRITTEN)
**Current content**: Literature comparison, principal contributions, programme vision
**Rewrite**: This becomes the culminating chapter — "Concordance, programmes, and the form of the theory"
- §1: Principal contributions (keep, sharpen)
- §2: Literature concordance (keep, but transform tables into flowing synthesis)
- §3: The nine programmes (fully expanded):
  - Each programme: precise mathematical formulation, proved ingredients, specific gap, research roadmap
  - Cross-programme connections: how Programme I (Langlands) connects to Programme II (KL) via the critical → admissible deformation; how Programme V (Vassiliev) connects to Programme IV (E_n) via specialization to n=1
  - The unifying vision: modular Koszul duality for factorization algebras
- §4: CS as Koszul duality (Programme VI-d):
  - The identification CS(M³, G) = ∫_M B̄(ĝ_k) as factorization homology
  - Prove for M = S³: ∫_{S³} B̄(ĝ_k) = WRT invariant (this follows from factorization homology computations on S³ = D³ ∪_{S²} D³ using the excision property)
- §5: W∞ and higher spin (Programme VI-e)

#### D18. physical_origins.tex (expanded)
**New content (Programme VI-f)**:
- NC geometry: E₁-chiral structure from non-commutativity — the NC torus T²_θ produces an E₁-chiral algebra via the Moyal product, and Koszul duality exchanges θ ↔ 1/θ (Morita equivalence)
- D-brane categories: module categories over E₁-chiral algebras as D-brane categories, citing Kontsevich–Soibelman

### PHASE E: REMAINING THEORY + NEW CHAPTERS

#### E19. NEW: en_koszul_duality.tex
Full new chapter (Programme IV):
- §1: "Higher-dimensional configuration spaces" — C_n(ℝ^d), Totaro's presentation, comparison with Arnold for d=1
- §2: "The E_n propagator" — closed (n-1)-form G on C₂(ℝ^n), residues as integration over linking spheres S^{n-1}
- §3: "The E₂ bar complex in detail" — definition of B̄_{E₂}(A) for an E₂-algebra A on a surface Σ, the bar differential from residues of the propagator, d²=0 from Totaro relations
- §4: "E_n Koszul duality theorem" — formulation: B̄_{E_n}(A) computes E_n-factorization homology ∫_{ℝ^n} A. For Koszul A, the bar-cobar adjunction is an equivalence.
- §5: "Connection to Ayala–Francis" — our construction is the chain-level refinement of AF's ∞-categorical Poincaré–Koszul duality at each n. At n=1, recover our chiral bar-cobar exactly.
- §6: "The n=2 Kontsevich formality" — bar-cobar for E₂-algebras and its relationship to Kontsevich's formality theorem in dimension 2

#### E20. NEW: derived_langlands.tex
Full new chapter (Programmes I + II):
- §1: "Derived algebraic geometry: prerequisites" — derived stacks (M1: import from Toën–Vezzosi), cotangent complexes L_X, derived structure sheaves. Only what is needed.
- §2: "The derived oper space" — Op^{dR}_{g∨}(X) as a derived stack, its tangent complex, the Frenkel–Gaitsgory description
- §3: "Bar complex at critical level = derived oper functions" — the identification B̄(ĝ_{crit}) ≃ O(Op^{dR}_{g∨}(X)):
  - Prove: H⁰ ≅ Fun(Op) (rephrase thm:oper-bar-h0)
  - Prove: H¹ ≅ Ω¹(Op) (rephrase prop:oper-bar-h1)
  - Formulate: H^n ≅ ∧^n L_{Op} (cotangent complex identification)
  - The spectral sequence: bar filtration → cotangent complex spectral sequence
- §4: "Root-of-unity bar complexes" — the periodic CDG structure at admissible levels:
  - Positselski's framework for CDG algebras (M1 import)
  - Construction of the periodic structure B̄^{n+2q} ≅ B̄^n
  - The passage to semisimplified tilting category
- §5: "The Kazhdan-Lusztig equivalence from bar-cobar" — the full roadmap:
  - State conj:kl-from-bar-cobar with all hypotheses
  - The 5 proved ingredients (list with theorem references)
  - The 1 remaining ingredient (periodic CDG at roots of unity)
  - Why this would be a geometric proof of KL
- §6: "Connections to geometric Langlands" — the derived Satake:
  - Bar-cobar at critical level → opers → Hecke eigensheaves
  - The Frenkel–Gaitsgory conjecture in our language

#### E21-E25. Remaining chapters
- configuration_spaces.tex: Add §Totaro's presentation for ℝ^d (reference for E_n chapter)
- chiral_koszul_pairs.tex: Strengthen with root-of-unity perspective
- poincare_duality_quantum.tex: Add shifted symplectic framework reference
- hochschild_cohomology.tex: Fix F8, add NC Hodge connection
- algebraic_foundations.tex: Add brief DAG prerequisites if not covered in derived_langlands chapter
- Appendices: Update as needed

---

## 4. Cross-Chapter Synthesis Points

These are mathematical connections between chapters that should exist as explicit sentences or remarks:

| From | To | Connection |
|------|----|-----------|
| bar_cobar (d = d_bracket + d_curvature) | bv_brst (Q = Q_BRST + ħΔ) | Pole decomposition = BV decomposition |
| higher_genus (complementarity eigenspaces) | derived_langlands (Lagrangian in shifted symplectic) | Eigenspace decomposition is the shadow of Lagrangian polarization |
| kac_moody (FF involution k ↔ -k-2h∨) | derived_langlands (oper at critical level) | At k = -h∨, the duality degenerates: A = A!, bar complex is uncurved, and computes the oper space |
| genus_expansions (shared discriminant Δ) | examples_summary (monodromy interpretation) | Δ(x) = det(1 - x·KS | H^{red}_1(A)) — discriminant is monodromy characteristic polynomial |
| yangians (E₁ bar-cobar) | en_koszul_duality (E_n for general n) | Yangian = E₁ case; E₂ would give factorization homology on surfaces; general E_n is dimensional ladder |
| configuration_spaces (Arnold relations) | en_koszul_duality (Totaro relations) | Arnold for n=1 is special case of Totaro for general n; the relations ensure d²=0 at each level |
| deformation_theory (NC Hodge) | higher_genus (genus tower) | The genus expansion parameter g_s IS the twistor parameter λ of the NC Hodge structure |
| bv_brst (anomaly = curvature) | higher_genus (genus universality) | The conformal anomaly c/12 at genus 1 equals 2F₁(Vir_c) = 2·c/24 = c/12 (Mumford isomorphism) |
| concordance (CS as Koszul) | kontsevich_integral (KZ/Drinfeld) | CS on S³ produces WRT via bar factorization homology; CS monodromy on C₃ produces KZ equation and Drinfeld associator |

---

## 5. Representation Theory Depth Charge

The DEEPAUDIT says: don't just define E₁-chiral algebras, construct and study their representation theory. Current state and targets:

| Algebra | Rep theory currently | Depth target |
|---------|---------------------|-------------|
| ĝ_k | Category O described, KL equivalence cited, bar-BGG for sl₂ computed | Full: bar resolution = BGG resolution (extend to sl₃, sp₄). Module Koszul duality explicit. |
| Virasoro | Verma modules, Kac det, BPZ | Bar resolution of Verma modules. DS reduction of module bar-cobar. |
| W_N | Simplicity ≠ semisimplicity noted | W-orbit duality for module categories. Subregular case explicit. |
| Yangian | RTT modules described, E₁ structure | Shifted Yangian modules. CoHA as E₁-module factory. Coulomb branch as Koszul dual module category. |
| Toroidal | Basic description | Double-loop module theory. Fay identity on elliptic curve modules. |
| Free fields | Fock modules | Symplectic fermion modules and logarithmic extensions. |

---

## 6. The Chriss-Ginzburg Layer (Systematic Edits)

For EVERY chapter, apply:

### Opening Transformation (T1)
Every chapter that currently opens with "This chapter develops/contains/constructs X" gets replaced with a mathematical question or tension.

### Catalog Elimination (T3)
Priority targets (currently bullet-list heavy):
- introduction.tex §Dictionary (~line 309)
- introduction.tex §Relationship to foundational work (~line 234)
- holomorphic_topological.tex §rem:fact-vs-chiral (~line 34)
- bv_brst.tex §BV data definition (~line 11)
- concordance.tex §Literature tables (~line 64)

### Shadow Sentences (T2)
Every major theorem (all 3 Main Theorems, all Koszul pair identifications, all genus expansion formulas) gets one shadow sentence connecting it to a distant chapter.

### Synthesis Paragraphs (T5)
At every Part boundary (Theory→Examples, Examples→Connections) and every 3-chapter boundary within a Part.

---

## 7. Estimated Edit Count and Pacing

| Phase | Chapters | Edits (T1-T7) | Edits (M1-M5) | New lines | Time estimate |
|-------|----------|---------------|---------------|-----------|---------------|
| A (Core) | 4 | ~20 | ~15 | ~2000 | 3-4 hours |
| B (Expansions) | 4 | ~12 | ~20 | ~3000 | 3-4 hours |
| C (Examples) | 5 | ~15 | ~10 | ~1500 | 2-3 hours |
| D (Connections) | 5+1new | ~15 | ~15 | ~3000 | 3-4 hours |
| E (Theory+New) | 7+2new | ~20 | ~25 | ~5000 | 4-6 hours |
| **Total** | **25+3new** | **~82** | **~85** | **~14500** | **~18 hours** |

This exceeds a single session. Priority: Phase A complete, Phase B partial (kac_moody + yangians), Phase D partial (bv_brst + concordance). The plan persists for continuation sessions.

---

## 8. Session Execution Order (First Session)

Given context window constraints, this session targets:
1. ✅ Write this plan
2. introduction.tex — full T1-T7 + programme foreshadowing
3. bar_cobar_construction.tex — T1-T7 + E_n forward references
4. higher_genus.tex — T1-T7 + shifted symplectic section
5. deformation_theory.tex — Fix F5/F6/F7 + NC Hodge section start
6. kac_moody_framework.tex — Programme I/II summaries
7. bv_brst.tex — Programme VI-a expansion
8. concordance.tex — Programme synthesis rewrite start

If context remains: begin new chapter stubs (en_koszul_duality.tex, derived_langlands.tex, kontsevich_integral.tex).
