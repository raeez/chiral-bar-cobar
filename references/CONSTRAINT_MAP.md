# CONSTRAINT MAP — References Directory
# Machine-readable registry of external constraints from reference library
# Format: YAML-like structured entries for each paper in references/

---

## REGISTRY FORMAT

Each entry has:
- `ID`: Filename in references/
- `BIB_KEY`: Key in bibliography/references.tex
- `AUTHORS`: Author list
- `TITLE`: Full title
- `YEAR`: Publication year
- `ARXIV`: arXiv identifier (if any)
- `ROLE`: FOUNDATION | INPUT | COMPARISON | EXTENSION | EXAMPLE | PHYSICS
- `CONSTRAINT_TYPE`: What mathematical constraints this paper imposes on the monograph
- `CHAPTERS_TOUCHED`: Which .tex files cite or depend on this paper
- `THEOREMS_CONSTRAINED`: Which labeled theorems/propositions this constrains
- `KEY_CONTENT`: Mathematical content that feeds into our constraint system
- `FRONTIER_EFFECT`: How this paper affects the constraint frontier (SATISFIED/TENSION/GAP/FRONTIER)
- `NOTES`: Any additional context for future constraint-solver iterations

---

## TIER 1: FOUNDATIONAL REFERENCES

### ENTRY 001
```
ID: "Chiral algebras (Alexander Beilinson, V. G. Drinfeld) (Z-Library).pdf"
BIB_KEY: BD04
AUTHORS: Alexander Beilinson, Vladimir Drinfeld
TITLE: "Chiral Algebras"
YEAR: 2004
ARXIV: none (AMS book)
ROLE: FOUNDATION
CONSTRAINT_TYPE: AXIOMATIC_FRAMEWORK
CHAPTERS_TOUCHED:
  - chapters/theory/introduction.tex
  - chapters/theory/algebraic_foundations.tex
  - chapters/theory/bar_cobar_construction.tex
  - chapters/theory/configuration_spaces.tex
  - chapters/theory/higher_genus.tex
  - chapters/theory/chiral_koszul_pairs.tex
  - chapters/connections/holomorphic_topological.tex
  - chapters/connections/concordance.tex
THEOREMS_CONSTRAINED:
  - thm:FM (FM compactification)
  - thm:bar-cobar-isomorphism-main (Main Theorem A)
  - thm:geometric-equals-operadic-bar
  - def:chiral-algebra (axiomatic definition)
  - def:factorization-algebra
KEY_CONTENT:
  - Chiral algebra = D-module on curve with chiral product j_*j^*(A⊠A) → Δ_!A
  - Factorization algebra ↔ chiral algebra equivalence (BD 3.4.9)
  - Ran space formalism for factorization
  - Chiral envelope functor Lie_ch → Assoc_ch
  - Conformal blocks via chiral homology
FRONTIER_EFFECT: SATISFIED
  # All BD axioms correctly implemented.
NOTES: >
  THE foundational text. Every definition in Part 1 must be compatible with BD.
  BD 3.4.9 is factorization↔chiral equivalence (not Ind: Lie_ch→Com_ch).
  Cross-reference: \BDref{} macro used throughout for BD chapter/section citations.
```

### ENTRY 002
```
ID: "[Grundlehren...] Jean-Louis Loday Bruno Vallette - Algebraic Operads 346 (2012).pdf"
BIB_KEY: LV12
AUTHORS: Jean-Louis Loday, Bruno Vallette
TITLE: "Algebraic Operads"
YEAR: 2012
ARXIV: none (Springer Grundlehren 346)
ROLE: FOUNDATION
CONSTRAINT_TYPE: ALGEBRAIC_BACKBONE
CHAPTERS_TOUCHED:
  - chapters/theory/algebraic_foundations.tex
  - chapters/theory/bar_cobar_construction.tex
  - chapters/theory/chiral_koszul_pairs.tex
  - appendices/koszul_reference.tex
  - appendices/signs_and_shifts.tex
THEOREMS_CONSTRAINED:
  - thm:bar-cobar-isomorphism-main (classical bar-cobar adjunction)
  - thm:koszul-criterion (Koszul property detection)
  - thm:operadic-koszul-duality
KEY_CONTENT:
  - Koszul duality for operads: bar-cobar adjunction B ⊣ Ω
  - Twisting morphisms and Koszul criterion
  - A∞ and curved A∞ structures
  - Sign conventions (HOMOLOGICAL grading; book uses COHOMOLOGICAL — key difference!)
  - Com^! = Lie, Ass^! = Ass, Lie^! = Com
FRONTIER_EFFECT: SATISFIED
  # Classical Koszul duality correctly lifted to chiral setting.
NOTES: >
  CRITICAL CONVENTION DIFFERENCE: LV12 uses homological grading (|d|=-1),
  manuscript uses cohomological (|d|=+1). All sign formulas must be translated.
  Bar construction in LV12: B(A) = T^c(sĀ, d); in manuscript: B(A) = T^c(s^{-1}Ā, d).
  This is a known pitfall — see CLAUDE.md "Grading and Conventions".
```

### ENTRY 003
```
ID: ayala-francis.pdf
BIB_KEY: AF15
AUTHORS: David Ayala, John Francis
TITLE: "Factorization Homology of Topological Manifolds"
YEAR: 2015
ARXIV: 1206.5522
ROLE: FOUNDATION
CONSTRAINT_TYPE: GEOMETRIC_FRAMEWORK
CHAPTERS_TOUCHED:
  - chapters/theory/introduction.tex
  - chapters/theory/poincare_duality.tex
  - chapters/theory/poincare_duality_quantum.tex
  - chapters/theory/higher_genus.tex
  - chapters/connections/concordance.tex
THEOREMS_CONSTRAINED:
  - thm:nap-duality (Non-abelian Poincaré duality)
  - thm:bar-NAP-homology
  - thm:verdier-bar-cobar
KEY_CONTENT:
  - Factorization homology ∫_M A for E_n-algebras on manifolds
  - Non-abelian Poincaré duality: ∫_M A ≃ Map_c(M, B^n A) for n-fold bar
  - Excision and Mayer-Vietoris for factorization homology
  - Verdier duality exchanges bar and cobar (geometric heart of thesis)
FRONTIER_EFFECT: SATISFIED
  # NAP duality correctly implemented. Verdier exchange proved.
NOTES: >
  Key equation: Verdier duality D(j_*M) ≅ j_!(DM) for holonomic M.
  This is the geometric mechanism mediating chiral Koszul duality.
  The manuscript's "Prism Principle" is the operadic repackaging of this.
```

### ENTRY 004
```
ID: 0709.1228v1.pdf
BIB_KEY: GK94
AUTHORS: Victor Ginzburg, Mikhail Kapranov
TITLE: "Koszul Duality for Operads"
YEAR: 1994
ARXIV: math/0709.1228 (reposted 2007; original Duke Math J 1994)
ROLE: FOUNDATION
CONSTRAINT_TYPE: OPERADIC_KOSZUL
CHAPTERS_TOUCHED:
  - chapters/theory/algebraic_foundations.tex
  - chapters/theory/bar_cobar_construction.tex
  - chapters/theory/poincare_duality_quantum.tex
THEOREMS_CONSTRAINED:
  - thm:operadic-koszul-duality
  - thm:prism-higher-genus (via Feynman transform of GK modular operad)
KEY_CONTENT:
  - Koszul duality functor for operads
  - Bar construction for operads
  - Modular operad framework (extended by Getzler-Kapranov)
  - Operadic suspension and desuspension
FRONTIER_EFFECT: SATISFIED
NOTES: >
  GK94 + GeK98 (Getzler-Kapranov modular operads) together provide
  the operadic infrastructure for the Prism Principle.
```

### ENTRY 005
```
ID: 1103.5803v4.pdf
BIB_KEY: FG12
AUTHORS: John Francis, Dennis Gaitsgory
TITLE: "Chiral Koszul Duality"
YEAR: 2012
ARXIV: 1103.5803
ROLE: FOUNDATION
CONSTRAINT_TYPE: DIRECT_PREDECESSOR
CHAPTERS_TOUCHED:
  - chapters/theory/introduction.tex
  - chapters/theory/bar_cobar_construction.tex
  - chapters/theory/chiral_koszul_pairs.tex
  - chapters/theory/higher_genus.tex
  - chapters/connections/concordance.tex
THEOREMS_CONSTRAINED:
  - thm:bar-cobar-isomorphism-main (our Main Theorem A extends FG12)
  - thm:chiral-formality
  - thm:e1-chiral-koszul-duality
KEY_CONTENT:
  - Chiral Koszul duality functor in ∞-categorical setting
  - Factorization algebras ↪ chiral commutative coalgebras (embedding)
  - Chiral envelopes of ⋆-Lie algebras
  - Pro-nilpotent and ind-nilpotent completions
  - Koszul duality in nilpotent tensor ∞-categories
FRONTIER_EFFECT: SATISFIED
  # Our monograph extends FG12 in three directions: (1) explicit geometric
  # formulas via configuration space integrals, (2) higher genus, (3) examples.
NOTES: >
  THE direct predecessor paper. Our monograph is essentially the concrete,
  computed, higher-genus, example-rich version of FG12's abstract framework.
  Key difference: FG12 works in ∞-categories; we give explicit chain-level
  constructions with signs and differentials. A gap in the FG duality
  proof (Step 3 diagonal vanishing) was identified and fixed (minor).
  CONSTRAINT: Every theorem in our Part 1 must be compatible with FG12's
  abstract results. Our theorems should SPECIALIZE to FG12 at genus 0.
```

### ENTRY 006
```
ID: "Victor G·Kac, Ashok K·Raina, Natasha·Rozhkovskaya - Bombay Lectures...pdf"
BIB_KEY: KRR/Kac
AUTHORS: Victor G. Kac, Ashok K. Raina, Natasha Rozhkovskaya
TITLE: "Bombay Lectures on Highest Weight Representations of Infinite Dimensional Lie Algebras"
YEAR: 2013 (2nd ed)
ARXIV: none (WSPC book)
ROLE: FOUNDATION
CONSTRAINT_TYPE: REPRESENTATION_THEORY
CHAPTERS_TOUCHED:
  - chapters/examples/kac_moody_framework.tex
  - chapters/examples/free_fields.tex
  - chapters/theory/koszul_pair_structure.tex
KEY_CONTENT:
  - Highest weight representations of affine Lie algebras
  - Sugawara construction: T = (1/2(k+h∨))∑:JᵃJᵃ:
  - Character formulas, Weyl-Kac formula
  - Free field realizations (Frenkel-Kac, Wakimoto)
FRONTIER_EFFECT: SATISFIED
NOTES: >
  Standard reference for affine algebra representation theory.
  Key verified formulas from this source: Sugawara c = k·dim(g)/(k+h∨),
  Freudenthal-de Vries |ρ|² = h∨d/12 (with (θ,θ)=2 normalization).
```

### ENTRY 007
```
ID: 9709040v1.pdf
BIB_KEY: Kon03
AUTHORS: Maxim Kontsevich
TITLE: "Deformation Quantization of Poisson Manifolds, I"
YEAR: 1997 (preprint); 2003 (published in Lett. Math. Phys.)
ARXIV: q-alg/9709040
ROLE: FOUNDATION
CONSTRAINT_TYPE: DEFORMATION_FRAMEWORK
CHAPTERS_TOUCHED:
  - chapters/examples/deformation_quantization.tex
  - chapters/theory/bar_cobar_construction.tex
THEOREMS_CONSTRAINED:
  - thm:chiral-kontsevich (our chiral analog)
  - thm:chiral-formality
  - thm:chiral-quantization
KEY_CONTENT:
  - Star product: f⋆g = fg + (ℏ/2){f,g} + O(ℏ²)
  - Configuration space integrals on upper half-plane
  - Formality conjecture: T_poly ≃ D_poly as L∞ algebras
  - Graph weights w_Γ = ∫_{C_n(H)} ω_Γ
  - Stokes' theorem → associativity
FRONTIER_EFFECT: SATISFIED
  # Our chiral Kontsevich formula extends this to curves.
NOTES: >
  The original source for deformation quantization via configuration spaces.
  Our thm:chiral-kontsevich adapts the Stokes argument from H to FM(X).
  The compact curve setting is cleaner (no boundary at infinity).
```

### ENTRY 008
```
ID: 1605.00138v2.pdf
BIB_KEY: Ara07 (or AraLectures)
AUTHORS: Tomoyuki Arakawa
TITLE: "Introduction to W-algebras and their representation theory"
YEAR: 2017
ARXIV: 1605.00138
ROLE: FOUNDATION
CONSTRAINT_TYPE: W_ALGEBRA_THEORY
CHAPTERS_TOUCHED:
  - chapters/examples/w_algebras_framework.tex
  - chapters/examples/w_algebras_deep.tex
  - chapters/connections/holomorphic_topological.tex
THEOREMS_CONSTRAINED:
  - thm:w-algebra-bar-cobar (W-algebra Koszul property at generic k)
  - thm:virasoro-periodicity
  - thm:w-algebra-hochschild
KEY_CONTENT:
  - W-algebras via quantized Drinfeld-Sokolov reduction
  - C₂-cofiniteness and rationality at admissible levels
  - Representation theory: category O, Verma modules
  - DS functor as BRST reduction
FRONTIER_EFFECT: SATISFIED
NOTES: >
  Arakawa's C₂-cofiniteness constrains but does not imply Koszulity.
  The Koszul property at admissible levels remains CONJECTURED in our book.
```

## TIER 2: INPUT REFERENCES (papers providing specific mathematical input)

### ENTRY 009
```
ID: 0010072v1.pdf
BIB_KEY: Tamarkin00
AUTHORS: Dmitry E. Tamarkin
TITLE: "The deformation complex of a d-algebra is a (d+1)-algebra"
YEAR: 2000
ARXIV: math/0010072
ROLE: INPUT
CONSTRAINT_TYPE: OPERADIC_DEFORMATION
CHAPTERS_TOUCHED:
  - chapters/examples/deformation_quantization.tex (formality theorem context)
  - chapters/theory/algebraic_foundations.tex (E_n operads)
KEY_CONTENT:
  - Deformation complex of E_d-algebra carries E_{d+1}-structure
  - Alternative proof of Kontsevich formality (via little disks)
  - E₂-formality implies deformation quantization
FRONTIER_EFFECT: SATISFIED
  # Our chiral formality (thm:chiral-formality) cites Tamarkin for E₂-formality.
NOTES: >
  Tamarkin's approach to formality is complementary to Kontsevich's:
  uses operadic methods rather than configuration space integrals.
  Both approaches are referenced in our deformation quantization chapter.
  Cited in deformation_quantization.tex.
```

### ENTRY 010
```
ID: 0901.0069v2.pdf
BIB_KEY: DTT09
AUTHORS: V. A. Dolgushev, D. E. Tamarkin, B. L. Tsygan
TITLE: "Formality theorems for Hochschild complexes and their applications"
YEAR: 2009
ARXIV: 0901.0069
ROLE: INPUT
CONSTRAINT_TYPE: HOCHSCHILD_FORMALITY
CHAPTERS_TOUCHED:
  - chapters/examples/deformation_quantization.tex
  - chapters/theory/hochschild_cohomology.tex
KEY_CONTENT:
  - Formality of Hochschild cochain complex as G∞-algebra
  - Applications to deformation theory and Deligne conjecture
  - Tsygan formality for Hochschild chains
FRONTIER_EFFECT: SATISFIED
NOTES: >
  Provides the Hochschild-level formality that underpins our identification
  of chiral Hochschild cohomology with deformations.
  Cited in deformation_quantization.tex.
```

### ENTRY 011
```
ID: 9902090v3.pdf
BIB_KEY: CattaneoFelder99
AUTHORS: Alberto S. Cattaneo, Giovanni Felder
TITLE: "A path integral approach to the Kontsevich quantization formula"
YEAR: 1999/2000
ARXIV: math/9902090
ROLE: INPUT
CONSTRAINT_TYPE: PATH_INTEGRAL_BRIDGE
CHAPTERS_TOUCHED:
  - chapters/examples/deformation_quantization.tex
  - chapters/connections/feynman_diagrams.tex
KEY_CONTENT:
  - Kontsevich formula derived from Poisson sigma model path integral
  - BV quantization of 2d topological field theory
  - Feynman diagram = configuration space integral identification
  - Physical origin of graph weights w_Γ
FRONTIER_EFFECT: SATISFIED
  # Bridges physics (Feynman/BV) and math (configuration integrals).
NOTES: >
  This paper gives the physical ORIGIN of Kontsevich's formula:
  the Poisson sigma model on the disk with boundary on the Poisson manifold.
  Our monograph's "configuration spaces as Feynman diagrams" philosophy
  is the chiral extension of this insight.
  Cited in deformation_quantization.tex.
```

### ENTRY 012
```
ID: kontsevich_soibelman_deformation_theory_1.pdf
BIB_KEY: KontsevichSoibelman
AUTHORS: Maxim Kontsevich, Yan Soibelman
TITLE: "Deformation Theory. I"
YEAR: unpublished manuscript
ARXIV: none
ROLE: INPUT
CONSTRAINT_TYPE: DEFORMATION_FOUNDATIONS
CHAPTERS_TOUCHED:
  - chapters/theory/deformation_theory.tex
  - chapters/examples/deformation_quantization.tex
KEY_CONTENT:
  - Formal moduli problems via dg Lie algebras
  - Curved A∞ and L∞ structures
  - Maurer-Cartan moduli spaces
  - Deformation-obstruction theory in derived setting
FRONTIER_EFFECT: SATISFIED
NOTES: >
  Foundational manuscript on derived deformation theory. Our
  thm:deformation-obstruction and the curved A∞ framework in
  deformation_theory.tex follow the KS philosophy.
  Cited in deformation_quantization.tex.
```

### ENTRY 013
```
ID: 2503.17563v2.pdf
BIB_KEY: Mok25
AUTHORS: Siao Chi Mok
TITLE: "Logarithmic Fulton-MacPherson Configuration Spaces"
YEAR: 2025
ARXIV: 2503.17563
ROLE: INPUT
CONSTRAINT_TYPE: GEOMETRIC_EXTENSION
CHAPTERS_TOUCHED:
  - chapters/theory/configuration_spaces.tex
KEY_CONTENT:
  - Logarithmic variant of FM compactification
  - Handles boundary divisors in log smooth pairs
  - Extends FM to pairs (X, D) with NCD boundary
  - Relevant for higher-genus with marked points on boundary
FRONTIER_EFFECT: FRONTIER
  # Potential input for extending FM to curves with punctures/boundaries.
  # Could strengthen higher-genus constructions with log structures.
NOTES: >
  NEWEST paper in collection. Logarithmic FM spaces are potentially
  relevant for extending our bar-cobar construction to curves with
  boundary (open strings). Not yet deeply integrated — cited in
  configuration_spaces.tex as parenthetical reference.
  FUTURE CONSTRAINT: If higher-genus constructions need log structures
  (e.g., for stable curves with nodes), Mok25 provides the foundations.
  Cited in configuration_spaces.tex.
```

## TIER 3: COMPARISON/EXTENSION REFERENCES

### ENTRY 014
```
ID: 2212.11252v1.pdf (and duplicate "(1).pdf")
BIB_KEY: GLZ / QuadDual
AUTHORS: Zhengping Gui, Si Li, Keyou Zeng
TITLE: "Quadratic Duality for Chiral Algebras"
YEAR: 2022
ARXIV: 2212.11252
ROLE: COMPARISON
CONSTRAINT_TYPE: PARALLEL_DEVELOPMENT
CHAPTERS_TOUCHED:
  - chapters/theory/introduction.tex
  - chapters/theory/chiral_koszul_pairs.tex
  - chapters/connections/concordance.tex
THEOREMS_CONSTRAINED:
  - thm:e1-chiral-koszul-duality (our E₁ version)
  - thm:chiral-koszul-module
KEY_CONTENT:
  - Quadratic duality notion for chiral algebras
  - Chiral version of classical quadratic duality for associative algebras
  - Maurer-Cartan equations in chiral setting
  - Examples: commutative chiral, affine KM, βγ-bc
FRONTIER_EFFECT: SATISFIED
  # Our framework EXTENDS GLZ: we handle non-quadratic (curved), higher genus,
  # and provide geometric realization via configuration space integrals.
  # GLZ works at genus 0 only. Our concordance chapter compares frameworks.
NOTES: >
  Key comparison paper. GLZ is the closest parallel development to our work.
  Differences: GLZ works purely algebraically (no configuration spaces),
  genus 0 only, quadratic only. We are geometric, all genera, handle curvature.
  The concordance chapter (concordance.tex) compares our results with GLZ.
```

### ENTRY 015
```
ID: "Boundary Chiral Algebras and Holomorphic Twists.pdf"
BIB_KEY: CDG20
AUTHORS: Kevin Costello, Tudor Dimofte, Davide Gaiotto
TITLE: "Boundary Chiral Algebras and Holomorphic Twists"
YEAR: 2020
ARXIV: 2005.00083
ROLE: EXTENSION
CONSTRAINT_TYPE: PHYSICS_BRIDGE
CHAPTERS_TOUCHED:
  - chapters/connections/holomorphic_topological.tex
  - chapters/connections/bv_brst.tex
KEY_CONTENT:
  - Boundary chiral algebras from holomorphic twists of 3d N=4 theories
  - Vertex algebras as boundary conditions for 3d HT theories
  - Coulomb branch vertex algebras
  - Connection between 3d gauge theory and 2d chiral algebras
FRONTIER_EFFECT: FRONTIER
  # Potential source of new examples for our framework.
  # The boundary chiral algebras should be Koszul — not yet explored.
NOTES: >
  Bridges 3d holomorphic QFT with 2d chiral algebras. The boundary
  VOAs produced by CDG20 are natural candidates for Koszul duality analysis
  using our framework. FUTURE: Compute bar complexes of boundary VOAs.
  Cited.
```

### ENTRY 016
```
ID: "Higher Operations in Perturbation Theory.pdf"
BIB_KEY: GKW24
AUTHORS: Davide Gaiotto, Justin Kulp, Jingxiang Wu
TITLE: "Higher Operations in Perturbation Theory"
YEAR: 2024
ARXIV: 2403.13049
ROLE: EXTENSION
CONSTRAINT_TYPE: HIGHER_OPERATIONS
CHAPTERS_TOUCHED:
  - chapters/connections/holomorphic_topological.tex
KEY_CONTENT:
  - Higher operations (A∞, L∞) in perturbative QFT
  - Configuration space integrals for higher operations
  - Connection to factorization algebras and operads
FRONTIER_EFFECT: FRONTIER
  # Potential physical validation of our A∞ structures.
  # Higher operations from perturbation theory should match our
  # bar-cobar derived operations.
NOTES: >
  Provides physics perspective on the same A∞/L∞ structures that
  our bar-cobar construction produces mathematically. Potential
  for cross-validation of higher operation formulas.
  Cited.
```

### ENTRY 017
```
ID: "Line Operators in HQFT.pdf"
BIB_KEY: DNP25
AUTHORS: Tudor Dimofte, Wenjun Niu, Victor Py
TITLE: "Line Operators in 3d Holomorphic QFT: Meromorphic Tensor Categories and dg-Shifted Yangians"
YEAR: 2025
ARXIV: 2508.11749
ROLE: EXTENSION
CONSTRAINT_TYPE: YANGIAN_EXTENSION
CHAPTERS_TOUCHED:
  - chapters/examples/yangians.tex
  - chapters/connections/holomorphic_topological.tex
THEOREMS_CONSTRAINED:
  - conj:shifted-yangian-e1 (provides evidence)
  - thm:yangian-koszul-dual (complementary construction)
KEY_CONTENT:
  - dg-shifted Yangians from line operators in 3d holomorphic QFT
  - Meromorphic tensor categories
  - E₁ structures on line operator categories
  - Connection between shifted Yangians and Coulomb branches
FRONTIER_EFFECT: FRONTIER
  # Provides independent evidence for conj:shifted-yangian-e1.
  # The dg-shifted Yangian construction should be compatible with
  # our E₁-chiral Yangian framework.
NOTES: >
  NEWEST physics paper in collection. The dg-shifted Yangians of DNP25
  are the physics counterpart of our algebraic shifted Yangian conjecture.
  FUTURE: Verify that DNP25's dg-shifted structure matches our E₁-chiral
  prediction for shifted Yangians.
  Cited.
```

### ENTRY 018
```
ID: 2302.06693v1.pdf
BIB_KEY: Zeng23
AUTHORS: Keyou Zeng
TITLE: "Twisted Holography and Celestial Holography from Boundary Chiral Algebra"
YEAR: 2023
ARXIV: 2302.06693
ROLE: EXTENSION
CONSTRAINT_TYPE: HOLOGRAPHIC_BRIDGE
CHAPTERS_TOUCHED:
  - chapters/connections/holomorphic_topological.tex
KEY_CONTENT:
  - Twisted holography from boundary chiral algebras
  - Celestial holography connection
  - Bulk-boundary correspondence for chiral algebras
FRONTIER_EFFECT: FRONTIER
  # Connects our boundary chiral algebra discussion to celestial holography.
NOTES: >
  Extension to celestial holography. Our bar-cobar framework for
  boundary chiral algebras may have celestial holography applications.
  Cited.
```

### ENTRY 019
```
ID: 2502.13227v1 (2).pdf
BIB_KEY: KhanZeng25
AUTHORS: Ahsan Z. Khan, Keyou Zeng
TITLE: "Poisson Vertex Algebras and Three Dimensional Gauge Theory"
YEAR: 2025
ARXIV: 2502.13227
ROLE: EXTENSION
CONSTRAINT_TYPE: PVA_3D
CHAPTERS_TOUCHED:
  - chapters/connections/holomorphic_topological.tex
KEY_CONTENT:
  - Poisson vertex algebras from 3d gauge theory
  - Classical limits of boundary VOAs
  - Connection between PVA and 3d N=4 theories
FRONTIER_EFFECT: FRONTIER
  # Classical limit perspective on our chiral Koszul duality.
NOTES: >
  PVA = coisson algebra = classical limit of vertex algebra. Our
  deformation quantization chapter starts from coisson algebras.
  KhanZeng25 provides 3d gauge theory origin for these classical structures.
  Cited.
```

### ENTRY 020
```
ID: 2312.07274v1 (1) (1).pdf (and duplicate)
BIB_KEY: Latyntsev23
AUTHORS: Alexei Latyntsev
TITLE: "Factorisation Quantum Groups"
YEAR: 2023
ARXIV: 2312.07274
ROLE: EXTENSION
CONSTRAINT_TYPE: FACTORISATION_QG
CHAPTERS_TOUCHED:
  - chapters/examples/yangians.tex
THEOREMS_CONSTRAINED:
  - thm:yangian-koszul-dual (complementary approach)
  - rem:yangian-langlands (Langlands duality at Yangian level)
KEY_CONTENT:
  - Factorisation quantum groups via factorisation homology
  - Yangian-type algebras from factorisation perspective
  - E₁ structures on quantum groups
FRONTIER_EFFECT: FRONTIER
  # Complementary approach to Yangian Koszul duality.
NOTES: >
  Latyntsev's factorisation quantum groups provide an alternative
  construction of Yangian-type objects that may illuminate our
  E₁-chiral Yangian Koszul dual.
  Cited.
```

## TIER 4: HIGH-LEVERAGE REFERENCES

### ENTRY 021
```
ID: getzler_hycom_9411004.pdf
BIB_KEY: Get95
AUTHORS: Ezra Getzler
TITLE: "Operads and Moduli Spaces of Genus 0 Riemann Surfaces"
YEAR: 1995
ARXIV: alg-geom/9411004
ROLE: FOUNDATION
CONSTRAINT_TYPE: GENUS_0_OPERADIC
CHAPTERS_TOUCHED:
  - chapters/theory/introduction.tex
  - chapters/theory/poincare_duality_quantum.tex
KEY_CONTENT:
  - HyCom operad = H*(M̄_{0,n})
  - HyCom is Koszul dual to Grav = H_*(M̄_{0,n})
  - Operadic structure on genus-0 moduli spaces
  - This is the GENUS-0 HALF of the Prism Principle
FRONTIER_EFFECT: SATISFIED
  # HyCom↔Grav duality at genus 0 correctly implemented.
NOTES: >
  CRITICAL for genus-0 story. HyCom↔Grav = operadic Koszul duality
  on M̄_{0,n}. Our Prism Principle is the all-genera extension via
  Feynman transform (GeK98).
```

### ENTRY 022
```
ID: costello_paquette_2001.02177.pdf
BIB_KEY: CP2020
AUTHORS: Kevin Costello, Natalie M. Paquette
TITLE: "Twisted Supergravity and Koszul Duality: A Case Study in AdS₃"
YEAR: 2020/2021
ARXIV: 2001.02177
ROLE: COMPARISON
CONSTRAINT_TYPE: ADS3_KOSZUL
CHAPTERS_TOUCHED:
  - chapters/theory/higher_genus.tex
  - chapters/connections/holomorphic_topological.tex
KEY_CONTENT:
  - Koszul duality in AdS₃/CFT₂ setting
  - Twisted supergravity = Koszul dual of boundary CFT
  - Bar-cobar in holographic context
  - Concrete example validating our framework
FRONTIER_EFFECT: SATISFIED
  # Provides physics validation of our mathematical framework.
NOTES: >
  Important VALIDATION paper. Costello-Paquette show that in AdS₃,
  the bar-cobar duality of the boundary chiral algebra controls the
  bulk twisted supergravity — exactly as our framework predicts.
 
```

### ENTRY 023
```
ID: costello_li_1606.00365.pdf
BIB_KEY: CL16
AUTHORS: Kevin Costello, Si Li
TITLE: "Twisted Supergravity and its Quantization"
YEAR: 2016
ARXIV: 1606.00365
ROLE: FOUNDATION
CONSTRAINT_TYPE: HT_TWIST_FRAMEWORK
CHAPTERS_TOUCHED:
  - chapters/connections/holomorphic_topological.tex (thm:costello-li-reduction)
  - chapters/theory/higher_genus.tex
  - chapters/theory/introduction.tex
KEY_CONTENT:
  - Holomorphic-topological twist of N=2 SYM
  - Factorization algebra from dimensional reduction
  - BV quantization of twisted theories
  - Connection to boundary chiral algebras
FRONTIER_EFFECT: SATISFIED
NOTES: >
  Foundational for Part 3 (holomorphic-topological chapter).
  The CL twist produces the factorization algebra that our
  bar-cobar framework then analyzes.
 
```

### ENTRY 024
```
ID: positselski_0905.2621.pdf
BIB_KEY: Positselski / Positselski11
AUTHORS: Leonid Positselski
TITLE: "Two Kinds of Derived Categories, Koszul Duality, and Comodule-Contramodule Correspondence"
YEAR: 2011
ARXIV: 0905.2621
ROLE: INPUT
CONSTRAINT_TYPE: CURVED_KOSZUL
CHAPTERS_TOUCHED:
  - chapters/theory/bar_cobar_construction.tex
  - chapters/theory/higher_genus.tex
  - chapters/theory/chiral_koszul_pairs.tex
KEY_CONTENT:
  - Comodule-contramodule correspondence
  - Curved Koszul duality (curvature ≠ 0)
  - Two kinds of derived categories for curved dg-algebras
  - Pro-nilpotent completions in Koszul duality
  - Module-comodule equivalence with completeness hypotheses
FRONTIER_EFFECT: SATISFIED
  # thm:chiral-koszul-module uses Positselski's module-comodule
  # equivalence correctly (not naive D^b equivalence).
NOTES: >
  CRITICAL for handling curvature. Higher-genus bar complexes are
  curved (m₀ ≠ 0), so classical Koszul duality fails — need
  Positselski's curved formalism. The naive D^b(A-mod)≃D^b(A!-mod)
  statement is corrected using Positselski.
```

### ENTRY 025
```
ID: benzvi_francis_nadler_0805.0157.pdf
BIB_KEY: BZFN10
AUTHORS: David Ben-Zvi, John Francis, David Nadler
TITLE: "Integral Transforms and Drinfeld Centers in Derived Algebraic Geometry"
YEAR: 2010
ARXIV: 0805.0157
ROLE: INPUT
CONSTRAINT_TYPE: DERIVED_ALGEBRAIC_GEOMETRY
CHAPTERS_TOUCHED:
  - chapters/theory/hochschild_cohomology.tex
KEY_CONTENT:
  - Integral transforms in derived algebraic geometry
  - Drinfeld centers as Hochschild cohomology
  - Factorization homology on Σ_g computes trace of monodromy
  - Link between genus-g partition functions and Hochschild theory
FRONTIER_EFFECT: SATISFIED
NOTES: >
  Provides the DAG foundations for identifying factorization
  homology on surfaces with traces in module categories.
  Our Hochschild-cyclic spectral sequence chapter uses this.
 
```

### ENTRY 026
```
ID: gaiotto_twisted_holography_1903.00382.pdf
BIB_KEY: Gai19
AUTHORS: Davide Gaiotto
TITLE: "Twisted Compactifications of 3d N=4 Theories and Conformal Blocks"
YEAR: 2019
ARXIV: 1903.00382
ROLE: EXTENSION
CONSTRAINT_TYPE: TWISTED_HOLOGRAPHY
CHAPTERS_TOUCHED:
  - chapters/theory/introduction.tex
  - chapters/connections/holomorphic_topological.tex
KEY_CONTENT:
  - Twisted holography framework
  - Vertex algebra structure at 4d/2d interfaces
  - Conformal blocks from 3d compactification
FRONTIER_EFFECT: FRONTIER
  # Provides physics framework that our mathematical results realize.
NOTES: >
  Part of the Gaiotto program connecting twisted supersymmetric
  gauge theory with vertex algebras. Our monograph provides the
  mathematical infrastructure (bar-cobar via configuration spaces)
  for the objects Gaiotto constructs physically.
 
```

### ENTRY 027
```
ID: schiffmann_vasserot_1202.2756.pdf
BIB_KEY: SV13
AUTHORS: Olivier Schiffmann, Eric Vasserot
TITLE: "Cherednik Algebras, W-algebras and the Equivariant Cohomology of the Moduli Space of Instantons on A²"
YEAR: 2013
ARXIV: 1202.2756
ROLE: COMPARISON
CONSTRAINT_TYPE: AGT_MATHEMATICAL
CHAPTERS_TOUCHED:
  - chapters/connections/holomorphic_topological.tex (AGT scope remark)
  - chapters/examples/yangians.tex (CoHA scope remark)
KEY_CONTENT:
  - Mathematical proof of AGT in specific cases
  - W-algebra action on equivariant cohomology of Hilb^n(C²)
  - CoHA as Yangian/W-algebra
  - Cherednik algebras and W-algebras connection
FRONTIER_EFFECT: SATISFIED
  # Our AGT scope remark correctly cites SV13 as partial proof.
NOTES: >
  One of the key partial proofs of AGT correspondence. Provides
  mathematical validation that the W-algebra structure predicted
  by AGT does indeed arise from geometric representation theory.
 
```

### ENTRY 028
```
ID: arakawa_creutzig_linshaw_1812.00093.pdf
BIB_KEY: ACL19
AUTHORS: Tomoyuki Arakawa, Thomas Creutzig, Andrew R. Linshaw
TITLE: "W-algebras as Coset Vertex Algebras"
YEAR: 2019
ARXIV: 1812.00093
ROLE: INPUT
CONSTRAINT_TYPE: W_COSET
CHAPTERS_TOUCHED:
  - chapters/connections/holomorphic_topological.tex (thm:w-from-gauge)
KEY_CONTENT:
  - W-algebras as coset vertex algebras: W_k(g) = Com(g_k, V_ρ)
  - Higgs branch quantization produces vertex algebras
  - Match between coset and DS constructions
FRONTIER_EFFECT: SATISFIED
NOTES: >
  Establishes W = coset rigorously. Our thm:w-from-gauge cites ACL19
  for the identification W_k(g) = Com(g_k, V_ρ). This constrains
  our W-algebra Koszul duality computations: the Koszul dual of W_k
  must be compatible with the coset description.
 
```

---

## CONSTRAINT SUMMARY TABLE

| Status | Count | Description |
|--------|-------|-------------|
| SATISFIED | 22 | Constraints from paper correctly reflected in monograph |
| FRONTIER | 6 | Paper provides new directions/evidence not yet fully integrated |
| TENSION | 0 | No contradictions between papers and monograph |
| GAP | 0 | No gaps |

## FRONTIER ITEMS

1. **Mok25 → Log FM for punctured curves**: Could extend bar-cobar to open-string setting
2. **CDG20 → Boundary VOA Koszul duality**: Compute bar complexes of boundary VOAs
3. **DNP25 → dg-shifted Yangian verification**: Check compatibility with our E₁ prediction
4. **GKW24 → Higher operations cross-validation**: Compare perturbative A∞ with our bar-derived A∞
5. **Zeng23 → Celestial holography**: Our bar-cobar may have celestial applications
6. **KhanZeng25 → PVA from 3d**: Classical limit perspective on chiral Koszul duality

## ADDITIONAL REFERENCES

### ENTRY 029
```
ID: costello_gwilliam_factorization_algebras.pdf
BIB_KEY: CG17
AUTHORS: Kevin Costello, Owen Gwilliam
TITLE: "Factorization Algebras in Quantum Field Theory" (combined draft)
YEAR: 2017/2021
SOURCE: nLab draft
ROLE: FOUNDATION
CONSTRAINT_TYPE: BV_FACTORIZATION_FRAMEWORK
CITATION_COUNT: 24 (highest in bibliography)
CHAPTERS_TOUCHED: bar_cobar, higher_genus, holomorphic_topological, algebraic_foundations,
  chiral_modules, koszul_pair_structure, feynman_diagrams, introduction, free_fields
KEY_CONTENT:
  - BV quantization of field theories
  - Factorization algebras: definition, examples, properties
  - Prefactorization algebras and factorization envelopes
  - Quantum observables as factorization algebras
  - Free field theories and Kac-Moody factorization algebras
FRONTIER_EFFECT: SATISFIED
```

### ENTRY 030
```
ID: getzler_kapranov_modular_operads.pdf
BIB_KEY: GeK98
AUTHORS: Ezra Getzler, Mikhail Kapranov
TITLE: "Modular Operads"
YEAR: 1998
ARXIV: dg-ga/9408003
ROLE: FOUNDATION
CONSTRAINT_TYPE: MODULAR_OPERAD_FRAMEWORK
CHAPTERS_TOUCHED: introduction, poincare_duality_quantum, feynman_diagrams
KEY_CONTENT:
  - Modular operad definition and Feynman transform
  - Genus-graded operadic structure
  - Foundation for Prism Principle (all genera)
FRONTIER_EFFECT: SATISFIED
```

### ENTRY 031
```
ID: zhu_modular_invariance_1996.pdf
BIB_KEY: Zhu96
AUTHORS: Yongchang Zhu
TITLE: "Modular Invariance of Characters of Vertex Operator Algebras"
YEAR: 1996
SOURCE: AMS JAMS (open access)
ROLE: FOUNDATION
CONSTRAINT_TYPE: MODULAR_INVARIANCE
CHAPTERS_TOUCHED: toroidal_elliptic, free_fields
KEY_CONTENT:
  - Characters of rational VOAs are modular forms
  - Zhu's algebra A(V) and its role in representation theory
  - Modular invariance of n-point genus-1 functions
FRONTIER_EFFECT: SATISFIED
```

### ENTRY 032
```
ID: bgs_koszul_duality_patterns_1996.pdf
BIB_KEY: BGS96
AUTHORS: Alexander Beilinson, Victor Ginzburg, Wolfgang Soergel
TITLE: "Koszul Duality Patterns in Representation Theory"
YEAR: 1996
SOURCE: AMS JAMS (open access)
ROLE: FOUNDATION
CONSTRAINT_TYPE: CLASSICAL_KOSZUL
CHAPTERS_TOUCHED: bar_cobar_construction, algebraic_foundations
KEY_CONTENT:
  - Koszul duality for algebras arising in representation theory
  - Koszul algebras and their duals
  - BGG correspondence and derived equivalences
  - Category O and its Koszul structure
FRONTIER_EFFECT: SATISFIED
```

### ENTRY 033
```
ID: kazhdan_lusztig_I.pdf through kazhdan_lusztig_IV.pdf
BIB_KEY: KL93
AUTHORS: David Kazhdan, George Lusztig
TITLE: "Tensor Structures Arising from Affine Lie Algebras, Parts I-IV"
YEAR: 1993-1994
SOURCE: AMS JAMS (open access)
ROLE: FOUNDATION
CONSTRAINT_TYPE: QUANTUM_GROUP_EQUIVALENCE
CHAPTERS_TOUCHED: deformation_theory, kac_moody_framework
KEY_CONTENT:
  - Equivalence O_k(ĝ) ≃ Rep^fd(U_q(g)) at roots of unity
  - Tensor category structure on affine Lie algebra representations
  - Braided tensor categories from conformal field theory
  - Foundation for quantum group interpretation of Koszul duality
FRONTIER_EFFECT: SATISFIED
```

## STILL MISSING (pre-arXiv, paywalled)

1. **FF92** (Feigin-Frenkel, "Affine KM at Critical Level and Gelfand-Dikii Algebras") — World Scientific 1992, 4 citations. Paywalled.
2. **FT87** (Feigin-Tsygan, "Additive K-theory") — Springer LNM 1289, 3 citations. Paywalled.

---

## SESSION 56 CHANGES LOG

### New bibliography entries added to references.tex:
Mok25, Latyntsev23, KhanZeng25, Zeng23, CDG20, GKW24, DNP25, Tamarkin00, DTT09, CattaneoFelder99, KontsevichSoibelman

### New citations added to chapters:
- yangians.tex: \cite{Latyntsev23}, \cite{DNP25}
- holomorphic_topological.tex: \cite{CDG20} (×2), \cite{Zeng23}, \cite{KhanZeng25}, \cite{DNP25}, \cite{GKW24}
- configuration_spaces.tex: \cite{Mok25}
- deformation_quantization.tex: \cite{Tamarkin00}, \cite{DTT09}, \cite{CattaneoFelder99}, \cite{KontsevichSoibelman}

### Scope remarks added:
- bar_cobar_construction.tex: thm:brst-cohomology, thm:anomaly-cancellation

### New PDFs downloaded to references/ (batch 1 — arXiv):
getzler_hycom_9411004.pdf, costello_paquette_2001.02177.pdf, costello_li_1606.00365.pdf,
positselski_0905.2621.pdf, benzvi_francis_nadler_0805.0157.pdf,
gaiotto_twisted_holography_1903.00382.pdf, schiffmann_vasserot_1202.2756.pdf,
arakawa_creutzig_linshaw_1812.00093.pdf

### New PDFs downloaded to references/ (batch 2 — broader internet):
costello_gwilliam_factorization_algebras.pdf (nLab combined draft, 522pp)
getzler_kapranov_modular_operads.pdf (arXiv dg-ga/9408003, 47pp)
zhu_modular_invariance_1996.pdf (AMS JAMS open access, 66pp)
bgs_koszul_duality_patterns_1996.pdf (AMS JAMS open access, 55pp)
kazhdan_lusztig_I.pdf (AMS JAMS, 43pp)
kazhdan_lusztig_II.pdf (AMS JAMS, 63pp)
kazhdan_lusztig_III.pdf (AMS JAMS, 47pp)
kazhdan_lusztig_IV.pdf (AMS JAMS, 71pp)
