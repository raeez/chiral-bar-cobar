# THE IMPLIED HORIZON

## What This File Is

This file maps results that are implied by the monograph's proven machinery but are not
explicitly stated or proved. It is organized by epistemological level — from formal
corollaries that could be added today, to multi-year research programs.

The map was built by systematic analysis of the three main theorems, the Master Table,
the 38-reference library, the 6 FRONTIER items in CONSTRAINT_MAP.md, and the full
Hochschild/module theory infrastructure (Session 94 exploration protocol).

**Usage**: The SESSION_PROMPT.md decision tree (Branch E) directs advancement work
toward these targets. The exploration prompt (Section 8) is the systematic search protocol
for discovering new entries.

**Last updated**: Session 108 (Mar 5, 2026) — 20 Level A (20 completed), 24 Level B (19 completed), 10 Level C, 5 Level D items.
Session 108: B13+B14 confirmed already proved (prop:conformal-block-duality, thm:ds-koszul-intertwine). Modular periodicity upgraded CJ→PH. MNO96 citation added. 29pt overfull fixed. Census: PH 622, CJ 84.
Session 103: Strategic Synthesis — BGG sl₂ matrix-level instantiation in detailed_computations.tex (sec:bgg-sl2-pipeline). Added prop:bar-bgg-sl2 + cor:bgg-koszul-involution. F1 now substantially closed.
Session 102: F1 (Module Theory Orphanage) further addressed — comp:bgg-sl2-pipeline in chiral_modules.tex chains 6 proved results into full bar-to-BGG pipeline for sl₂ at generic level.
Session 101: F6 (Lurie HA undercitation) addressed — 17 citations across 7 files. H7 (Positselski acyclicity) written as prop:curved-bar-acyclicity + rem:positselski-acyclicity in bar_cobar_construction.tex. B18 partially completed (Virasoro Zhu, cor:virasoro-zhu-koszul). F1 (BGG for sl₂) addressed: thm:bgg-sl2-bar-explicit + 2 computations in detailed_computations.tex.
Agent results from Session 94 captured in notes/agent_results_session94.md.
Exploration Engine (Phase 4) additions from Session 96: A11-A15, B11-B18, C6-C8.
Session 97: Completed A2, A8, A9, B1, B2, B3, B4, B5, B7, B8, B9, B10.
Session 98: Added A16-A20, B19-B23, C9-C10 from IMPLIED_RESULTS_MAP.md systematic exploration.
Session 98: Completed A16, A17, A19 (geometric-algebraic comparison, G₂ bar complex, vacuum module Koszul duality).
Full map: notes/archive/IMPLIED_RESULTS_MAP.md (21 items across 5 tiers, absorbed into this file).

---

## Level A: Unstated Corollaries

Results that follow formally from proved theorems. Could be added with <1 page of proof.

### A1. Deformation-obstruction exchange at genus 0 — COMPLETED (Session 95)
- **Written as**: cor:def-obs-exchange-genus0 in deformation_theory.tex
- **Statement**: HH²(A) ≅ HH⁰(A!)^∨ ⊗ ω_X (first-order deformations ↔ primary obstructions).

### A2. Genus expansion for all Master Table entries — COMPLETED (Session 97)
- **Written as**: comp:lattice-genus-expansion in genus_expansions.tex
- **Statement**: F_g(V_Λ) = d · (2^{2g-1}-1)/2^{2g-1} · |B_{2g}|/(2g)! for rank-d lattice VOA. Table with d=8,16,24.

### A3. Cyclic homology exchange — COMPLETED (Session 95)
- **Written as**: cor:cyclic-homology-duality in hochschild_cohomology.tex
- **Statement**: HC_n(A) ≅ HC_{-n}(A!)^∨ (periodic cyclic, shift absorbed by Connes S).

### A4. Universal generating function theorem — COMPLETED (Session 95)
- **Written as**: thm:universal-generating-function in genus_expansions.tex
- **Statement**: For ANY Koszul chiral algebra A with obstruction coefficient κ = κ(A):
  Σ_{g≥1} F_g(A) x^{2g} = κ · ((x/2)/sin(x/2) − 1)
  with radius of convergence |x| = 2π independent of A.

### A5. Obstruction coefficient additivity — COMPLETED (Session 95)
- **Written as**: cor:kappa-additivity in higher_genus.tex
- **Statement**: κ(A⊗B) = κ(A) + κ(B). Genus-g obstruction additive.

### A6. Critical level universality — COMPLETED (Session 95)
- **Written as**: cor:critical-level-universality in higher_genus.tex
- **Statement**: κ=0 ⟺ obs_g=0 ∀g ⟺ F_g=0 ∀g ⟺ uncurved bar ⟺ critical level. H⁰(B̄) is strict associative.

### A7. Tautological class map from Koszul chiral algebras — COMPLETED (Session 95)
- **Written as**: cor:tautological-class-map in higher_genus.tex
- **Statement**: A ↦ κ(A)·λ_g ∈ R^g(M̄_g) is a group homomorphism K₀(KCA) → Q.

### A8. Complementarity sum as root datum invariant — COMPLETED (Session 97)
- **Written as**: thm:complementarity-root-datum + comp:complementarity-classical in genus_expansions.tex
- **Statement**: κ(W^k(g)) + κ(W^{k'}(g)) = (c+c')·σ(g), level-independent. Table for all simple types.

### A9. W_N obstruction for general g — COMPLETED (Session 97)
- **Written as**: cor:general-w-obstruction + rem:general-w-kappa-values in w_algebras_framework.tex
- **Statement**: κ(W^k(g)) = c·σ(g) where σ(g) = Σ 1/(m_i+1). Table of σ(g) for all simple types A₁–E₈.

### A10. DS of bar at dual level — COMPLETED (Session 95)
- **Written as**: cor:ds-bar-level-shift in chiral_modules.tex
- **Statement**: H⁰_DS(B̄(ĝ_k)) ≅ B̄_W(W^k(g)) and H⁰_DS(Ω(B̄(ĝ_k))) ≅ W^{k'}(g).

### A11. KM bar complex dimensions are level-independent — COMPLETED (Session 99, corrected Session 104)
- **Written as**: rem:bar-dims-level-independent in kac_moody_framework.tex
- **Statement**: Chain-group dim B̄^n(ĝ_k) = (dim g)^n · (n-1)! (generator × Orlik-Solomon form factor), independent of level k. Bar COHOMOLOGY (Table tab:bar-dimensions) much smaller: sl₂ = Riordan R(n+3), growth ~d^n.

### A12. sl₃ "Three Theorems in Action" genus expansion — COMPLETED (Session 99)
- **Written as**: comp:sl3-genus-expansion, prop:sl3-complementarity-all-genera, comp:sl3-multi-level in genus_expansions.tex
- **Statement**: κ(sl₃_k) = 4(k+3)/3, complementarity κ+κ' = 0, c+c' = 16. F_g through g=5 at k=1,2,3. Critical level k=-3 is uncurved.

### A13. Heisenberg bar dimensions match partition numbers — COMPLETED (Session 99)
- **Written as**: rem:bar-dims-partitions in free_fields.tex
- **Statement**: Free fermion: dim B̄^n = p(n-1). Heisenberg: dim B̄^n = p(n-2) for n≥2. Generating functions via cofree coalgebra structure.

### A14. Feynman transform double involution — COMPLETED (Session 99)
- **Written as**: cor:feynman-transform-involution, rem:ft-vs-bar-cobar in poincare_duality_quantum.tex
- **Statement**: FT∘FT → Id is a weak equivalence (GeK98 Theorem 5.4). All-genera generalization of Main Theorem B.

### A15. Hochschild-cyclic spectral sequence E₂ page for all Master Table entries — COMPLETED (Session 100)
- **Written as**: ex:E2-sl3, ex:E2-lattice in hochschild_cohomology.tex + expanded table (11 rows, up from 6)
- **Statement**: E₂ pages computed for sl₃ (C[Θ₂,Θ₄], rank-2 polynomial growth), W_N (C[Θ₂,...,Θ_N]), lattice VOAs (C[c]^⊗d), Yangian (conjectural). Table now covers all Master Table algebras.

### A16. Geometric-algebraic bar comparison for sl₂ (term-by-term) — COMPLETED (Session 98)
- **Written as**: comp:geom-alg-comparison-deg2, comp:geom-alg-comparison-deg3, comp:sl2-bar-matrix, rem:comparison-summary in detailed_computations.tex
- **Statement**: Term-by-term verification that geometric residue on FM₃(P¹) = algebraic bar differential. Degree 2: Res_{D₁₂} extracts structure constants, curvature from B-cycle period. Degree 3: Arnold relation = Jacobi identity. Explicit 3×9 differential matrix for sl₂.

### A17. G₂ bar complex (exceptional non-simply-laced) — COMPLETED (Session 98)
- **Written as**: comp:G2-roots, comp:G2-structure, comp:G2-ope, comp:G2-bar-deg2, comp:G2-curvature, comp:G2-genus, comp:G2-serre, prop:G2-bar-dims, rem:G2-context in detailed_computations.tex
- **Statement**: Full G₂ bar complex through degree 3. Root system (14-dim, lacing r∨=3), OPE with asymmetric double poles (k/3 short, k long), curvature κ = 7(k+4)/4, dual level -k-8, genus expansion, Serre relations at degrees 3 and 5. Comparison table across all lacing numbers {1,2,3}.

### A18. Pentagon identity via m₄ for Virasoro — COMPLETED (Session 100)
- **Written as**: comp:virasoro-m4 in feynman_diagrams.tex
- **Statement**: m₄(T⊗⁴) has leading term (c²/144)∂⁴T. Five trees from K₄ pentagon enumerated. Pentagon A∞ identity verified at leading order. Addresses F4 (A∞ mirage).

### A19. Vacuum Verma module under Koszul duality — COMPLETED (Session 98)
- **Written as**: prop:vacuum-verma-koszul, prop:shapovalov-koszul, rem:module-koszul-beyond-vacuum in chiral_modules.tex
- **Statement**: Φ(M(0)_k) ≃ M(0)_{-k-4}. Shapovalov determinant: det S_n(-k-4) = (-1)^{s_n}·det S_n(k). Singular vector loci complementary under Feigin-Frenkel involution. Critical level k=-2 self-dual. Extension to arbitrary highest weight λ noted.

### A20. Hochschild periodicity and Koszul duality — COMPLETED (Session 100)
- **Written as**: cor:hochschild-ring-koszul in koszul_pair_structure.tex
- **Statement**: CH*(A) ≅ CH*(A!) as graded rings for same-type Koszul pairs. Deformation dimension dim CH²(A) is Koszul-invariant. Via Keller derived Morita + Gel'fand-Fuchs.

---

## Level B: Provable from Framework + Known External Results

Require combining manuscript machinery with theorems from reference library.

### B1. Derived module category equivalence (Positselski extension) — COMPLETED (Session 97)
- **Written as**: conj:positselski-chiral in koszul_pair_structure.tex (ClaimStatusConjectured — full proof requires verifying Positselski's framework in chiral setting)
- **Statement**: D^{co}(A-CoMod^{conil}) ≃ D^{ctr}(A!-ContraMod) for Koszul chiral A.

### B2. Hochschild periodicity preservation — COMPLETED (Session 97)
- **Written as**: prop:periodicity-same-type + rem:periodicity-mixed-type in koszul_pair_structure.tex
- **Statement**: For same-type Koszul pairs (A, A!), CH*(A) has period d iff CH*(A!) has period d. Mixed-type case noted as open.

### B3. Conformal block dimensions from bar complex — COMPLETED (Session 97)
- **Written as**: prop:bar-verlinde-asymptotics in genus_expansions.tex
- **Statement**: Bar free energy F_g captures subleading asymptotics of conformal block dimensions: log dim V_{g,k} = (g-1)dim(g)log k + κ·λ_g^FP + O(1/k).

### B4. Tautological classes span computation — COMPLETED (Session 97)
- **Written as**: rem:tautological-span in higher_genus.tex
- **Statement**: All obstruction classes proportional to λ_g (rank-1 in R^g). Higher tautological classes from bar spectral sequence noted as open direction (see C6).

### B5. BGG reciprocity from bar filtration — COMPLETED (Session 97)
- **Written as**: rem:bgg-bar-spectral in chiral_modules.tex
- **Statement**: Bar spectral sequence E_1 page recovers BGG multiplicities. KL polynomial extraction from E_2 noted as requiring wall-crossing analysis (open).

### B6. Bernoulli universality of genus convergence — COMPLETED (Session 95)
- **Written as**: thm:bernoulli-universality in genus_expansions.tex
- **Statement**: Bar-complex genus expansion converges geometrically (ratio 1/(2π)²), in structural contrast with string (2g)! divergence.

### B7. W_N complementarity sum closed form — COMPLETED (Session 97)
- **Written as**: Merged with A8 as thm:complementarity-root-datum in genus_expansions.tex
- **Statement**: κ + κ' = (c+c')·σ(g) for all simple g, with σ(g) = Σ 1/(m_i+1) tabulated.

### B8. Hochschild cup product exchange under Koszul duality — COMPLETED (Session 97)
- **Written as**: cor:hochschild-cup-exchange + rem:cup-exchange-virasoro in hochschild_cohomology.tex
- **Statement**: Θ ↔ -Θ' under Verdier anti-commutativity. Verified for Virasoro case.

### B9. Multiplicative genus from Koszul duality — COMPLETED (Session 97)
- **Written as**: prop:multiplicative-genus + cor:complementary-genera + rem:genus-index-theory in genus_expansions.tex (new sec:multiplicative-genus)
- **Statement**: φ_A(x) = κ(A)·(x/2)/sin(x/2). Complementary genera: φ_A + φ_{A!} = (κ+κ')·φ₀.

### B10. Bar spectral sequence terminates at admissible levels — COMPLETED (Session 97)
- **Written as**: cor:bar-admissible-finiteness in kac_moody_framework.tex
- **Statement**: At non-degenerate admissible k = -h∨+p/q, bar degrees finite-dimensional, spectral sequence terminates, total cohomology finite-dimensional.

### B11. Ext ↔ Tor exchange via module Koszul duality — COMPLETED (Session 100)
- **Written as**: prop:ext-tor-exchange + rem:ext-tor-interpretation in chiral_modules.tex
- **Statement**: Ext^n_A(M,N) ≅ Tor_n^{A!}(M!,N!)^∨ for uncurved Koszul pairs. Extensions ↔ co-extensions. Curved case noted via Positselski. Addresses F1 (module theory).

### B12. Module tensor products dualize under Koszul — COMPLETED (already proved)
- **Written as**: thm:monoidal-module-koszul in chiral_modules.tex (lines 249-278)
- **Statement**: Lax monoidal: Φ(M ⊠_A N) → Φ(M) ⊠_{A!,c} Φ(N), QIS for Koszul modules. Braiding reversal σ! = σ⁻¹ for finite-type A!.

### B13. Conformal block rank complementarity — COMPLETED (already proved)
- **Written as**: prop:conformal-block-duality + rem:conformal-block-complementarity in chiral_modules.tex (lines 748-839)
- **Statement**: For Koszul pair (A, A!) both C₂-cofinite: (i) fusion coefficients preserved, (ii) genus-g conformal block ranks equal, (iii) KZB connections dual. Full proof via monoidal module Koszul duality + Verlinde formula.

### B14. DS reduction commutes with bar complex at module level — COMPLETED (already proved)
- **Written as**: thm:ds-koszul-intertwine in chiral_modules.tex (lines 3878-3957)
- **Statement**: For any module M ∈ Mod(ĝ_k): B̄_W(H⁰_DS(M)) ≃ H⁰_DS(B̄(M)). Full proof via double complex + BRST spectral sequence degeneration.

### B15. Logarithmic FM bar complex on punctured curves [Exploration Engine addition]
- **Follows from**: def:log-fm-compactification (configuration_spaces.tex) + thm:bar-cobar-isomorphism-main
- **Statement**: For X = Σ_g \ {p₁,...,p_n} (punctured curve), the FM compactification FM_m(X) has logarithmic boundary divisors. The bar complex B̄(A; M₁,...,M_n) with module insertions at punctures is computed by log-differential forms on FM_m(X). Residues at log divisors encode module OPE data.
- **Gap**: The log FM compactification for punctured curves needs explicit description (partially in configuration_spaces.tex). The interplay between FM boundary and puncture divisors is not developed.
- **Confidence**: MEDIUM — construction clear in principle, technical details substantial
- **Scale**: PAPER (15-20 pages)

### B16. Bar complex for Heisenberg dual Sym^ch(V*) — COMPLETED (Session 100)
- **Written as**: comp:bar-sym-ch in free_fields.tex
- **Statement**: B̄(Sym^ch(V*)) = coLie^ch(s⁻¹V*). Rank 1: concentrated in degree 1. Rank m: Witt formula ℓ(n,m) = (1/n)Σ_{d|n} μ(d)m^{n/d}. m=2 table: 2,1,2,3,6. Koszul inversion verified.

### B17. dg-shifted Yangian comparison with DNP25 [Exploration Engine addition]
- **Follows from**: thm:yangian-e1 (yangians.tex) + DNP25 (FRONTIER reference)
- **Statement**: The manuscript's E₁-chiral Yangian Y^{E₁}(g) should be quasi-isomorphic to the dg-shifted Yangian of Davison-Nekrasov-Pusztai (DNP25). Both are E₁-deformations of ĝ_k with spectral parameter. If confirmed, this provides a geometric (configuration space) construction of dg-shifted Yangians.
- **Gap**: Need detailed comparison of generators and relations. DNP25 uses cohomological Hall algebra methods; manuscript uses FM integrals. The comparison requires identifying the spectral parameter with the FM coordinate.
- **Reference**: DNP25 (FRONTIER), yangians.tex thm:yangian-e1
- **Confidence**: MEDIUM — structural similarity strong, but details untested
- **Scale**: PAPER (10-15 pages)

### B18. W-algebra Zhu algebra under Koszul duality — COMPLETED (Session 107)
- **Written as**: thm:w-algebra-zhu-koszul + rem:zhu-w-algebras-explicit in chiral_modules.tex
- **Statement**: For any simple g and generic k, A(W^k(g)) ≅ Z(U(g)) ≅ ℂ[p₁,...,p_r] (polynomial in Casimirs). Level-independent, hence Koszul-invariant. Proof chains Frenkel-Zhu → Arakawa → Kostant → Harish-Chandra. Resolves ALL W-algebra Zhu invariance questions at generic level. Admissible levels: NOT invariant in general.

### B19. Full derived module category equivalence (Positselski extension) [Session 98]
- **Extends**: B1 (Positselski conjectured)
- **Follows from**: thm:e1-module-koszul-duality + Positselski "Two Kinds" Thm 6.1 + BGS96 Thm 1.2.6
- **Statement**: D^b(Mod^compl(A)) ≃ D^co(CoMod^conil(A!)) with Ext^n_A(M₁,M₂) ≅ Ext^{d-n}_{A!}(Φ(M₁),Φ(M₂))∨. Goes beyond B1 by establishing the full triangulated equivalence (B1 only states the comodule-contramodule correspondence).
- **Gap**: Verifying Positselski's "contraherent cosheaf" condition (his Thm 8.1) in the chiral D-module setting.
- **Confidence**: MEDIUM — composition of known formalisms in new setting
- **Scale**: PAPER (10-15 pages)
- **Source**: IMPLIED_RESULTS_MAP.md item I.1

### B20. Genus-2 bar differential for sl₂ — COMPLETED (Session 102)
- **Written as**: prop:km-genus2-propagator, thm:sl2-genus2-bar-differential, thm:sl2-genus2-curvature, prop:sl2-genus2-relation in genus_expansions.tex
- **Statement**: First non-abelian genus-2 bar differential. Two-channel curvature κ = 3k/4 + 3/2. Resolves F2 (genus-2 wall).

### B21. Yangian Category O via E₁-chiral bar complex [Session 98]
- **Follows from**: thm:yangian-bar-rtt + thm:yangian-koszul-dual + thm:e1-module-koszul-duality
- **Statement**: Bar complex of Y(sl₂) induces BGG-type resolution of evaluation modules V(a). Module Koszul duality sends V(a) → V(-a) for Y_{R^{-1}}(sl₂). Spectral parameter a → -a under ℏ → -ℏ.
- **Gap**: Conditional on Yangian Koszulness conjecture (rem:yangian-collapse-conj).
- **Confidence**: MEDIUM — blocked by open conjecture
- **Scale**: PAPER (10-15 pages)
- **Source**: IMPLIED_RESULTS_MAP.md item II.5

### B22. KL equivalence from bar-cobar [Session 98]
- **Extends**: C2 (already in HORIZON as Level C)
- **Follows from**: thm:e1-module-koszul-duality + KL93 Parts I-IV + B19
- **Statement**: At admissible k = -h∨+p/q, periodic CDG structure of B̄(ĝ_k) matches representation category of U_q(g). Configuration space integrals give geometric proof of KL.
- **Gap**: Root-of-unity bar analysis, tensor structure preservation. Essentially a new proof of KL.
- **Confidence**: LOW — requires substantial new mathematics
- **Scale**: PROGRAM (2-3 years)
- **Source**: IMPLIED_RESULTS_MAP.md item II.1

### B23. Fusion product preservation under bar-cobar [Session 98]
- **Follows from**: thm:e1-module-koszul-duality + prop:fock-fusion-product + Huang-Lepowsky-Zhang
- **Statement**: Φ(M₁ ⊠_V M₂) ≅ Φ(M₁) ⊠_{V!} Φ(M₂) (or dual). For Heisenberg Fock modules: braiding phase e^{2πiλμ/κ} → e^{-2πiλμ/κ} under level shift.
- **Gap**: Bar coalgebra coproduct must intertwine with fusion tensor product. Hardest part of KL93.
- **Confidence**: LOW — requires substantial new mathematics
- **Scale**: PROGRAM (2-3 years)
- **Source**: IMPLIED_RESULTS_MAP.md item II.4

### B24. Positselski acyclicity of curved bar complexes at higher genus — COMPLETED (Session 101)
- **Written as**: prop:curved-bar-acyclicity + rem:positselski-acyclicity in bar_cobar_construction.tex
- **Statement**: At genus g≥1 with κ≠0, the curved bar complex B̄^(g)(A) has acyclic underlying cochain complex. This necessitates Positselski's coderived category D^co rather than ordinary D^b. Explains the structural necessity of exotic derived categories in Conjecture conj:positselski-chiral.

---

## Level C: New Approaches to Known Open Problems

### C1. Geometric Langlands from critical level bar complex
- **Approach**: At k=−h∨, bar complex is uncurved, H⁰ recovers FF center z(ĝ_{-h∨})≅Fun(Op).
  Full bar complex B̄(ĝ_{-h∨}) is a resolution of the oper space.
  Bar-cobar at critical level gives ĝ ↔ ĝ∨ at chain level.
- **Known problem**: Frenkel-Gaitsgory geometric Langlands program
- **New angle**: Our bar complex provides explicit chain-level resolution
- **BLOCKER**: Full oper identification requires derived algebraic geometry methods
- **Scale**: PROGRAM (multi-year)

### C2. KL equivalence from bar-cobar
- **Approach**: At admissible k = −h∨+p/q, bar curvature ~ p/q. At roots of unity (p/q rational),
  the bar complex of ĝ_k should have same homology as bar complex of U_q(g).
- **Known problem**: KL93 equivalence O_k(ĝ) ≃ Rep^fd(U_q(g))
- **New angle**: Configuration space proof via periodic curvature
- **BLOCKER**: Root-of-unity bar analysis not developed
- **Scale**: PAPER-PROGRAM (2-3 years)

### C3. Higher-dimensional chiral Koszul duality
- **Approach**: AF15 + manuscript's propagator formulas → E_n Koszul duality on n-manifolds
- **Known problem**: Poincaré-Koszul duality for E_n-algebras (AF Thm 7.8)
- **New angle**: Explicit configuration space integral formulas (replace Arnold with Totaro)
- **BLOCKER**: E_n configuration integrals on surfaces/3-manifolds not developed
- **Scale**: PROGRAM

### C4. Bar complex as chain-level modular functor
- **Follows from**: thm:prism-higher-genus (B̄^full ≅ FT_Mod(A)) + Segal-Bakalov-Kirillov axioms
- **Statement**: For a Koszul chiral algebra A, the full genus-graded bar complex B̄^full(A) = ⊕_g B̄^(g)(A) satisfies the axioms of a chain-level modular functor: (i) vector space V_g for each genus; (ii) factorization V_{g₁} ⊗ V_{g₂} → V_{g₁+g₂} from boundary clutching; (iii) self-sewing V_g → V_{g+1}.
- **New angle**: Chain-level (before passing to cohomology), resolving the well-known problem that modular functors are typically defined only at the homology level. The A∞ structure provides the homotopy coherences.
- **BLOCKER**: Verify the Segal axioms at chain level. May need to weaken to homotopy-coherent version.
- **Scale**: PAPER (15-20 pages)

### C5. Koszul duality as duality of multiplicative genera
- **Follows from**: B9 + thm:quantum-complementarity-main
- **Statement**: The genus expansion packages Koszul duality into a duality of multiplicative genera: A ↦ φ_A sends Koszul pairs to complementary genera with φ_A + φ_{A!} = const·φ_universal. This is a new algebro-geometric manifestation not visible in FG12 or CG17.
- **BLOCKER**: Formal group law identification needs development
- **Scale**: PAPER

### C6. Tautological class generation beyond λ-classes [Exploration Engine addition]
- **Extends**: B4 (tautological classes span computation)
- **Approach**: The genus universality theorem shows obs_g = κ·λ_g ∈ R^g(M̄_g). But the FULL bar spectral sequence E_r^{p,q} at each page provides classes in R^*(M̄_g) beyond just λ_g. The d_r differentials of the bar spectral sequence may generate ψ-classes, κ-classes, or boundary classes [Δ_irr], [Δ_{i,S}].
- **Known problem**: Which tautological classes lie in the image of "algebraic" constructions?
- **New angle**: The bar spectral sequence provides a FILTRATION of R*(M̄_g) indexed by bar degree, and the d_r differentials give explicit relations.
- **BLOCKER**: Need to compute E_3 page or higher for at least one example. E_2 is known but E_3 requires substantial work.
- **Scale**: PAPER

### C7. Genus-graded module categories [Exploration Engine addition]
- **Approach**: The full bar complex B̄^full(A) = ⊕_g B̄^(g)(A) is genus-graded. If A-mod has a genus-graded enhancement, then modules M_g at genus g form a "genus tower" with coproduct Δ: M_{g₁+g₂} → M_{g₁} ⊗ M_{g₂} from boundary clutching in M̄_g.
- **Known problem**: Constructing "higher-genus module categories" for vertex algebras
- **New angle**: The Feynman transform FT_Mod(A) ≅ B̄^full(A) automatically provides genus-grading. The obstruction to strict genus-graded modules is the curvature m₀^(g) mixing genera.
- **BLOCKER**: The coproduct Δ is only defined at the chain level (not on cohomology) due to curvature. Need to develop homotopy-coherent genus-graded module theory.
- **Scale**: PAPER-PROGRAM

### C8. λ_g² = 0 in R^{2g}(M̄_g) for g ≥ 3 [Exploration Engine addition]
- **Approach**: thm:obstruction-nilpotent proves obs_g² = 0 for g ≤ 2 by dimension counting. For g ≥ 3, obs_g² = κ²·λ_g² and the question reduces to λ_g² = 0 in R^{2g}(M̄_g).
- **Known problem**: Relations in the tautological ring R*(M̄_g)
- **New angle**: If proved, this would imply obs_g² = 0 for ALL g (completing conj:obstruction-nilpotent-higher). The manuscript identifies this as the single algebraic-geometry input needed to close the last structural gap.
- **Reference**: Faber's conjectures, Pandharipande-Pixton-Zvonkine relations
- **BLOCKER**: R^{2g}(M̄_g) is 1-dimensional (Faber) but λ_g² lives in degree 2g, not g. Need: is λ_g² in R^{2g} zero? For g=3: λ_3² ∈ R^6(M̄_3) — check against known relations.
- **Scale**: PAPER (algebraic geometry, possibly short if relation is known)

### C9. Higher-dimensional Koszul duality (E_n on n-manifolds) [Session 98]
- **Approach**: AF15 Thm 7.8 (Poincaré-Koszul duality) + our propagator formulas → E_n Koszul duality on n-manifolds. Replace Arnold with Totaro for higher-dim configuration space cohomology.
- **Known problem**: Explicit E_n bar-cobar duality
- **New angle**: Configuration space integral formulas generalize from curves to higher-dim
- **BLOCKER**: Higher-dim propagators not explicit; Totaro's theorem gives H* but not form presentation for bar differentials
- **Scale**: PROGRAM (3-5 years)
- **Source**: IMPLIED_RESULTS_MAP.md item III.1

### C10. Vassiliev invariants from Feynman transform [Session 98]
- **Approach**: Prism Principle B̄^full ≅ FT_Mod + GeK98 → Kontsevich integral from bar complex. Weight system from Lie algebra g matches KM use.
- **Known problem**: Universal Vassiliev invariants from configuration space integrals
- **New angle**: Our holomorphic propagators vs. Kontsevich's real propagator ω = (1/2π)d arg(z_i-z_j)
- **BLOCKER**: Passage from C_n(X) (complex curve) to C_n(S¹) (real 1-manifold); comparing holomorphic and topological Feynman transforms
- **Scale**: PROGRAM (3-5 years)
- **Source**: IMPLIED_RESULTS_MAP.md item III.3

---

## Level D: Speculative Extensions

### D1. Anomaly cancellation as Koszul-theoretic necessity
- **Idea**: BV-BRST identification B̄(A) ≃ C^BRST(A) + d²=0 → all quantum anomalies
  determined by Koszul property. Ghost c=26-c_matter would be geometric.
- **Status**: Interesting but requires physics → math bridge (rigorous path integral)
- **Scale**: 3+ years

### D2. AdS₃/CFT₂ as curved Koszul duality
- **Idea**: Costello-Paquette (CP2020) show twisted supergravity on AdS₃ controlled by
  boundary Koszul duality. Our curved A∞ = bulk non-perturbative theory.
- **Status**: CP2020 footnote 8 conjectures this explicitly. Our framework is the tool.
- **Scale**: 3+ years

### D3. 3d mirror symmetry from chiral Koszul duality
- **Idea**: E₁-chiral + Costello-Li + Gaiotto → bar=Higgs, cobar=Coulomb.
  Curved A∞ = mass/FI parameter deformation.
- **Status**: Highly speculative. Would unify Nakajima varieties, symplectic duality, 3d N=4.
- **Scale**: 5+ years

### D4. Noncommutative Hodge theory from genus tower
- **Idea**: Genus tower B̄^(g) as NC Hodge filtration. E₂ degeneration = Hodge symmetry.
  h^{p,q} = dim E₂^{p,q} of genus spectral sequence.
- **Status**: Foundational work needed. No existing framework to dock into.
- **Scale**: 5+ years

### D5. Vassiliev invariants from Feynman transform
- **Idea**: Prism Principle B̄^full ≃ FT_Mod. For A=ĝ_k: Vassiliev invariants from bar
  complex. Kontsevich integral as configuration space integral special case.
- **Reference**: GeK98 (Feynman transform of Com → Vassiliev)
- **Scale**: 3+ years

---

## Dependency Graph

```
Level A (independent, ready to write):
  A1 DONE, A2 DONE, A3 DONE, A4 DONE, A5 DONE, A6 DONE, A7 DONE, A8 DONE, A9 DONE, A10 DONE
  A11 ← independent (formal observation)
  A12 ← extends A2 (sl₃ subgoal), needs Master Table sl₃ data
  A13 ← independent (combinatorial identity)
  A14 ← uses thm:prism-higher-genus + GeK98
  A15 ← extends hochschild_cohomology.tex tables

Level B:
  B1 DONE (conjectured), B2 DONE, B3 DONE, B4 DONE, B5 DONE (remark), B6 DONE, B7 DONE, B8 DONE, B9 DONE, B10 DONE
  B11 ← uses thm:e1-module-koszul-duality (uncurved case easy)
  B12 ← uses B11 + fusion product structure
  B13 ← uses thm:verlinde-bar + analytic continuation
  B14 ← uses A10 + B11 (module-level DS)
  B15 ← uses configuration_spaces.tex log FM
  B16 ← uses A13 + chirCom/chirLie duality
  B17 ← needs DNP25 comparison (FRONTIER)
  B18 ← uses prop:zhu-koszul-compatibility (test case)
  B19 ← uses B1 + B11 (full derived equivalence)
  B20 ← uses A16 result + genus-2 theta functions
  B21 ← conditional on Yangian Koszulness
  B22 ← extends C2 (KL from bar-cobar)
  B23 ← uses B19 + fusion product (hardest)

Level C:
  C4 ← uses A4, B1
  C5 ← uses B9, A8
  C6 ← extends B4, needs E₃ page computation
  C7 ← uses A14 (FT involution) + B11 (module duality)
  C8 ← independent (algebraic geometry input)
  C9 ← independent (higher-dim geometry)
  C10 ← uses A14 + GeK98
  C1, C2, C3 ← independent programs
```

---

## Priority Ranking

**Completed (Sessions 95-97):**
1. ~~A1 — Def-obs exchange genus 0~~ → cor:def-obs-exchange-genus0
2. ~~A2 — Lattice VOA genus expansion~~ → comp:lattice-genus-expansion
3. ~~A3 — Cyclic homology exchange~~ → cor:cyclic-homology-duality
4. ~~A4 — Universal generating function~~ → thm:universal-generating-function
5. ~~A5 — κ additivity~~ → cor:kappa-additivity
6. ~~A6 — Critical level universality~~ → cor:critical-level-universality
7. ~~A7 — Tautological class map~~ → cor:tautological-class-map
8. ~~A8 — Complementarity sum~~ → thm:complementarity-root-datum
9. ~~A9 — General W obstruction~~ → cor:general-w-obstruction
10. ~~A10 — DS of bar at dual level~~ → cor:ds-bar-level-shift
11. ~~B1 — Positselski (conjectured)~~ → conj:positselski-chiral
12. ~~B2 — Hochschild periodicity~~ → prop:periodicity-same-type
13. ~~B3 — Verlinde asymptotics~~ → prop:bar-verlinde-asymptotics
14. ~~B4 — Tautological span~~ → rem:tautological-span
15. ~~B5 — BGG from bar~~ → rem:bgg-bar-spectral
16. ~~B6 — Bernoulli universality~~ → thm:bernoulli-universality
17. ~~B7 — W_N complementarity~~ → (merged with A8)
18. ~~B8 — Cup product exchange~~ → cor:hochschild-cup-exchange
19. ~~B9 — Multiplicative genus~~ → prop:multiplicative-genus
20. ~~B10 — Admissible finiteness~~ → cor:bar-admissible-finiteness

**Immediate (write now, <1 page each):**
21. A11 — KM bar dimensions level-independent (REMARK)
22. A13 — Heisenberg bar dims = partition numbers (REMARK)
23. A14 — Feynman transform double involution (COROLLARY)

**Completed (Session 98):**
24. ~~A16 — Geometric-algebraic bar comparison for sl₂~~ → comp:geom-alg-comparison-deg2 etc.
25. ~~A17 — G₂ bar complex~~ → comp:G2-roots, prop:G2-bar-dims etc.
26. ~~A19 — Vacuum module under Koszul duality~~ → prop:vacuum-verma-koszul etc.

**Short-term (1-5 pages each, high impact-per-effort):**
27. A12 — sl₃ Three Theorems showcase
28. A18 — Pentagon m₄ for Virasoro (fills F4, ~5 pages)
29. A15 — HC spectral sequence for all Master Table
30. B16 — Bar complex for Sym^ch(V*)
31. B11 — Ext ↔ Tor exchange (uncurved case)

**Medium-term (5-15 pages each):**
32. A20 — Hochschild periodicity under Koszul duality
33. B14 — Module-level DS + bar
34. B18 — W-algebra Zhu test
35. B17 — dg-shifted Yangian comparison (needs DNP25)
36. B19 — Full derived module equivalence
37. B20 — Genus-2 sl₂ bar differential (fills F2)

---

## Exploration Protocol

To discover NEW entries for this map, use `notes/EXPLORATION_ENGINE.md` (the full
5-phase protocol optimized for Claude Opus 4.6). The protocol requires:
1. Reading actual manuscript sections and reference PDFs
2. Providing specific theorem labels for every claimed implication
3. Distinguishing Levels A-D honestly
4. Passing the 4-filter Critical Pipeline (F1-F4)
5. Checking against 16 anti-patterns

Last run: Session 96 (Mar 5, 2026). Added 16 new items (A11-A15, B11-B18, C6-C8).
Rejected 2 duplicates. See `metadata/exploration_rejected.md` for full rejected list.

---

## Rejected Candidates

Items considered but filtered out as NOT implied by the framework:

- **AGT from bar factorization**: The 4d N=2 → 2d reduction producing W-algebras is a
  physics process. Our bar complex may participate in AGT, but AGT is not implied by
  bar-cobar duality alone. Requires 4d input.
- **Celestial OPE = FM residues**: Celestial holography operates on P¹ with specific
  soft limits. Our FM residues are more general. The connection is suggestive but the
  conformally soft limit structure is not part of our framework.
- **Ghost c=26 is Koszul-theoretic necessity**: The statement confuses levels. The bar
  complex computes B̄(matter⊗ghosts), not B̄(matter) alone. The c=26 criticality is a
  condition for overall d²=0, which is a HYPOTHESIS of our theorems, not a conclusion.
- **R-matrix transformation under factorization QG duality**: The predicted R(z) ↦
  R(-z-2h∨)^{-1,t} is an extrapolation from the level-shift k↔-k-2h∨. The R-matrix
  involves spectral parameters that are not part of the genus-0 bar complex.
- **κ determines the chiral algebra**: FALSE. κ is a single number; many non-isomorphic
  algebras share the same κ (e.g., H₁ and Vir₂ both have κ = 1).
- **Genus expansion converges to the physical partition function**: FALSE. F_g extracts a
  single tautological intersection number; Z_g depends on the full moduli. See
  rem:heisenberg-partition for the explicit distinction.
- **Periodicity of CH*(A) implies periodicity of CH*(A!) via Koszul duality alone**: NOT
  implied in general. All computed pairs are of the same type (KM-KM, Vir-Vir, W-W), so
  both sides have periodicity independently. Need a genuinely mixed-type pair to test.
- **Bar complex computes WRT invariants**: WRT invariants involve quantum groups at roots
  of unity. The connection goes through KL equivalence (Level C2), requiring substantial
  new work.
- **[Session 96] Multiplicative genus from bar-cobar (duplicate of B9)**: Candidate
  re-derived the existing B9 entry. Filtered as exact duplicate.
- **[Session 96] Complementarity sum closed form (duplicate of A8/B7)**: Candidate
  re-derived the existing A8 + B7 entries. Filtered as exact duplicate.

---

## Manuscript Inconsistencies Found by Exploration Engine

### ISSUE: βγ bar complex dimensions (3-way inconsistency) — RESOLVED
- **Conjecture conj:betagamma-bar-dim** (free_fields.tex:185): dim = 2·3^{n-1} = CHAIN SPACE dimension (all bar-n elements before cohomology)
- **Master Table** (examples_summary.tex:328): 2, 4, 10, 26, 70 = BAR COHOMOLOGY (lowest-weight truncation)
- **Generating function** 1/(1-t)²·1/(1-t²) was INCORRECT (produced 1, 2, 4, 6, 9, 12 matching neither)
- **Fix applied**: Removed incorrect GF from rem:betagamma-conventions. Added comparison table showing chain ≥ cohomology at each degree, analogous to KM (chain dim >> bar cohomology). Both values are correct for what they count.

### Additional Findings from Reference Agent (BETA)
Key uncited results from reference PDFs (metadata/reference_theorems.md):
- AF15 Prop 6.9+6.12: Bar filtration = Goodwillie cofiltration of factorization homology
- GeK98 Thm 8.13/Cor 8.15: Generating function formulas (Bernoulli, plethystic exp)
- BFN08 (entirely uncited): Loop space/center interpretation, E_n-Hochschild, 2d TFT
- Zhu96 + BGS96: Zhu algebra Koszul duality (connects to B18)
