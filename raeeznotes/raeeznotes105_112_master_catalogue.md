# Master Catalogue: raeeznotes105–112
## Concept → Strikelist Map (One-to-Many)

*Date: 2026-03-29. Source notes: 105 (83 items), 106 (81 items), 107 (58 items), 108 (56 items), 109 (55 items), 110 (62 items), 111 (80 items), 112 (80 items). Total raw items: ~555. After de-duplication across notes that refine the same ideas: **142 distinct concepts** organized into **16 thematic clusters**.*

---

## How to read this document

Each concept has:
- **ID**: Cluster.Number (e.g., A.1)
- **Title**: Short name
- **Source**: Which raeeznotes first introduces / most develops the idea
- **Description**: 2–4 sentences on the mathematical content
- **Named objects**: Key new definitions, formulas, theorems
- **STRIKELIST**: Every file across Vol I and Vol II that needs rewriting, with a 1-line description of what must change. Files are listed by path relative to `~/chiral-bar-cobar/` (Vol I) or `~/chiral-bar-cobar-vol2/` (Vol II).

---

# CLUSTER A: The Open/Closed Primitive Datum

The central reorientation: the primitive object is NOT a closed chiral algebra, NOT a boundary algebra, NOT the bar construction. It is a **cyclic open factorization dg-category on a tangential log curve**, from which everything else is derived.

---

### A.1 — Open sector primacy principle
**Source**: 107, 108, 109
**Description**: The primitive object of the theory is a cyclic open factorization dg-category C_op on the log boundary of a tangential log curve (X, D, τ). A boundary algebra A_b = RHom(b,b) is merely a local chart. The bulk emerges as the derived center. Modularity is trace + clutching on the open side.
**Named objects**: C_op, boundary vacuum b, A_b, platonic datum X = (X, D, τ; C_op, b, A_b, Z^ch(C_op), Θ_C, Tr_C)

**STRIKELIST**:
1. `chapters/theory/introduction.tex` — Rewrite the global framing: the primitive object is the open category, not the closed chiral algebra. All five main theorems should be re-contextualized as projections of the open/closed MC element.
2. `chapters/frame/preface.tex` — Update the "what this book proves" narrative to foreground the open/closed primitive datum as the platonic ideal the proved core descends from.
3. `chapters/frame/guide_to_main_results.tex` — Add the open/closed pipeline as the organizing spine: C_op → A_b → Z^ch → Θ_C → shadows.
4. `chapters/connections/frontier_modular_holography_platonic.tex` — The holographic modular Koszul datum H(T) should be upgraded to the full open/closed septuple. Currently H(T) = (A, A!, C, r(z), Θ_A, ∇^hol); the new primitive is the open-categorical enhancement X.
5. `chapters/connections/thqg_open_closed_realization.tex` — This file should become the definitive treatment of the open/closed primitive datum, absorbing the local Swiss-cheese pair, Morita invariance, and modular completion.
6. `chapters/connections/concordance.tex` — New concordance section: "The open/closed primitive datum" with subsections on the septuple, the five confusions to discard, and the corrected pipeline.
7. `Vol II: chapters/connections/ht_bulk_boundary_line_core.tex` — Reframe bulk-boundary-line as: open sector → boundary chart → derived center (bulk) → line category (A!-mod). Currently treats bulk as primary; needs correction.
8. `Vol II: chapters/theory/introduction.tex` — Update Vol II introduction to reflect that the Swiss-cheese structure descends from the open/closed primitive datum.
9. `Vol II: chapters/connections/bar-cobar-review.tex` — Sharpen the bar/cobar vs derived-center distinction in the Vol II review.

---

### A.2 — Five confusions to discard
**Source**: 107, 108
**Description**: (a) Open sector ≠ boundary algebra (it's a dg-category); (b) Bulk ≠ bar construction (bulk = derived center = C*_ch(A,A)); (c) 2d→3d jump is not "add E_1 bar direction" but Swiss-cheese/Deligne-Tamarkin universality; (d) Global domain is tangential log curve, not ordinary curve; (e) Modularity = trace + clutching on open sector, not closed-algebra decoration.
**Named objects**: Corrected slogan: bar/cobar = couplings, Hochschild = bulk, Θ = modular completion.

**STRIKELIST**:
1. `chapters/theory/bar_construction.tex` — Add remark clarifying that the bar complex classifies twisting morphisms/couplings, NOT the bulk algebra. Reference the derived center as the correct bulk.
2. `chapters/theory/bar_cobar_adjunction_curved.tex` — Same clarification at the adjunction level.
3. `chapters/theory/chiral_hochschild_koszul.tex` — Elevate the chiral Hochschild cochains to the status of "universal bulk" with explicit reference to the Swiss-cheese universality theorem.
4. `chapters/theory/chiral_center_theorem.tex` — This file should contain the definitive statement that the derived center is the bulk. Strengthen accordingly.
5. `chapters/connections/holomorphic_topological.tex` — Correct any treatment of "adding one E_1 direction" to the Swiss-cheese universality explanation.
6. `Vol II: chapters/theory/foundations.tex` — The foundations chapter should incorporate the five corrections.

---

### A.3 — A∞-chiral algebra as local one-color object
**Source**: 107, 108, 109
**Description**: An A∞-chiral algebra is a cochain complex A with chiral endomorphism operad End^ch_A(n) = Hom(A^⊗n, A((λ_1))…((λ_{n-1}))) and degree-1 operations m_n satisfying planar A∞ identities with spectral block-substitution. This is the precise local algebraic object living on boundary intervals.
**Named objects**: End^ch_A(n), block substitution Λ_i, A∞-chiral algebra (A, m)

**STRIKELIST**:
1. `chapters/theory/algebraic_foundations.tex` — Add definition of A∞-chiral algebra as local boundary object. Currently only has strict chiral algebras.
2. `chapters/theory/chiral_modules.tex` — Extend module theory to A∞-chiral context.
3. `chapters/theory/homotopy_transfer.tex` (appendix) — The HTT section should transfer A∞-chiral structures, not just L∞.
4. `appendices/homotopy_transfer.tex` — Add explicit HTT for A∞-chiral algebras.
5. `Vol II: chapters/theory/axioms.tex` — Update axioms to include A∞-chiral as primitive local algebraic datum.

---

### A.4 — Chiral Hochschild cochains C*_ch(A,A) as universal bulk
**Source**: 107, 108, 109, 111, 112
**Description**: From an A∞-chiral algebra A, the complex C*_ch(A,A) = ∏_{n≥0} End^ch_A(n+1)[-n] with brace operations and δ = [m,-] forms a brace dg algebra. This is identified as the derived center / universal bulk. The pair U(A) = (C*_ch(A,A), A) is the universal (initial) local chiral Swiss-cheese pair.
**Named objects**: C*_ch(A,A), U(A), chiral Deligne-Tamarkin-Swiss-cheese theorem

**STRIKELIST**:
1. `chapters/theory/chiral_hochschild_koszul.tex` — Add the universality theorem: U(A) = (C*_ch(A,A), A) is initial among local Swiss-cheese pairs with open color A.
2. `chapters/theory/chiral_center_theorem.tex` — State derived center = C*_ch(A_b, A_b) as definitive bulk identification.
3. `chapters/theory/hochschild_cohomology.tex` — Upgrade existing Hochschild treatment to include the brace dg algebra structure and universality.
4. `chapters/connections/thqg_open_closed_realization.tex` — The open/closed realization should exhibit U(A) as the local Swiss-cheese model.
5. `Vol II: chapters/connections/ht_bulk_boundary_line_core.tex` — Rewrite the bulk construction as derived center of open sector, not as independent object.
6. `Vol II: chapters/theory/pva-descent.tex` — The PVA descent calculus produces A∞-chiral data whose Hochschild cochains are the bulk; make this explicit.

---

### A.5 — Tangential log curve (X, D, τ) as global geometric domain
**Source**: 107, 108, 109, 110
**Description**: A tangential log curve is (X, D, τ) where X is smooth, D = {p_1,…,p_r} is a puncture divisor, and τ_{p_i} ∈ T_{p_i}X \ {0} is a tangential direction. Real-oriented blowup gives boundary circles; removing tangent points gives intervals I_p ≅ ℝ where open insertions live.
**Named objects**: (X, D, τ), I_p = S^1_p \ {τ_p}, real-oriented blowup

**STRIKELIST**:
1. `chapters/theory/configuration_spaces.tex` — Add tangential log curves as the correct geometric substrate. Currently has ordinary FM compactifications only.
2. `chapters/theory/higher_genus_foundations.tex` — Upgrade to tangential log curves as the global domain for modular completion.
3. `chapters/connections/frontier_modular_holography_platonic.tex` — The platonic programme should specify tangential log curves as the geometric arena.
4. `Vol II: chapters/theory/fm-calculus.tex` — Add tangential log curves and mixed FM compactifications.

---

### A.6 — Mixed Ran space and open/closed factorization dg-category
**Source**: 107, 108, 109
**Description**: Mixed configuration space Conf^{oc}_{I,m}(X,D,τ) with interior labels I and ordered boundary multiplicities m. Mixed Ran space Ran^{oc}(X,D,τ). Open/closed factorization dg-category C_oc is a dg-cosheaf on Ran^{oc} with holomorphic transport in closed direction, locally constant in open direction.
**Named objects**: Conf^{oc}_{I,m}, Ran^{oc}(X,D,τ), C_oc

**STRIKELIST**:
1. `chapters/theory/configuration_spaces.tex` — Add mixed configuration spaces and their compactifications.
2. `chapters/theory/higher_genus_modular_koszul.tex` — The modular cooperad should be upgraded to the mixed colored version C^{oc,log}_{mod}.
3. `Vol II: chapters/theory/fm-calculus.tex` — Add mixed FM compactifications with four boundary stratum types.
4. `Vol II: chapters/theory/locality.tex` — Extend locality axioms to the mixed open/closed setting.

---

### A.7 — Boundary algebra A_b is only a Morita chart
**Source**: 107, 108, 109, 111, 112
**Description**: Given compact generator b ∈ C_oc(J), A_b = RHom(b,b) is an A∞-chiral algebra. Different generators b, b' give Morita-equivalent algebras. The intrinsic object is the Morita class of C_op, not any chosen algebra. The bulk Z^ch(C_op) = C*_ch(A_b, A_b) is Morita-invariant.
**Named objects**: Morita invariance of bulk

**STRIKELIST**:
1. `chapters/theory/chiral_center_theorem.tex` — State and prove Morita invariance of chiral derived center.
2. `chapters/connections/thqg_open_closed_realization.tex` — Emphasize that boundary algebra is a chart, not the primitive.
3. `Vol II: chapters/connections/ht_bulk_boundary_line_core.tex` — Morita invariance as the reason bulk is well-defined.

---

### A.8 — Annulus = HH_*(C_op) (open-sector trace)
**Source**: 107, 108, 109, 110, 111, 112
**Description**: Factorization homology of the open sector around a boundary circle gives ∫_{S^1_p} C_op ≅ HH_*(C_op). The annulus is not primitive closed-string data; it is the cyclic trace of the open category. Modularity first appears as the trace theory of the open sector.
**Named objects**: Annulus = HH_*(C_op), Tr_C

**STRIKELIST**:
1. `chapters/theory/chiral_hochschild_koszul.tex` — Add the annulus = Hochschild chains identification.
2. `chapters/connections/entanglement_modular_koszul.tex` — The entanglement chapter should identify S_EE as the annular trace of the open sector.
3. `chapters/connections/genus_complete.tex` — Genus-one treatment should start from the annular trace.
4. `Vol II: chapters/connections/modular_pva_quantization_core.tex` — The modular PVA quantization should trace through the annulus.
5. `Vol II: chapters/connections/ht_bulk_boundary_line_core.tex` — Add annular trace as the modular shadow birthplace.

---

### A.9 — Colored modular cooperad C^{oc,log}_{mod}(X,D,τ)
**Source**: 107, 108, 109
**Description**: Chains on mixed compactified log-FM configuration spaces of bordered stable curves, with colors for interior/boundary labels. Four types of codimension-one strata: interior collision, ordered boundary collision, mixed interior-to-boundary bubbling, nodal clutching. The differential is the codimension-two boundary operator; d²=0 because every cod-2 stratum appears twice with opposite orientation.
**Named objects**: C^{oc,log}_{mod}(X,D,τ), four stratum types, C^{oc,log}_{≤1}

**STRIKELIST**:
1. `chapters/theory/higher_genus_modular_koszul.tex` — Upgrade the modular cooperad to the mixed colored version. Currently only has the closed-sector modular cooperad.
2. `chapters/theory/higher_genus_foundations.tex` — Add the four boundary stratum types.
3. `chapters/theory/configuration_spaces.tex` — Mixed FM compactifications as the geometric input.
4. `Vol II: chapters/theory/fm-calculus.tex` — Full treatment of mixed log-FM.
5. `Vol II: chapters/connections/fm3_planted_forest_synthesis.tex` — Extend planted forest synthesis to the mixed setting.

---

### A.10 — Modular MC element Θ_C in open/closed convolution algebra
**Source**: 107, 108, 109, 110, 111, 112
**Description**: A modular theory is an MC element Θ_C ∈ MC(Conv(C^{oc,log}_{mod}, End(Z^ch(C_op), C_op))). The MC equation is dΘ_C + ½[Θ_C, Θ_C] + Δ_{clutch}(Θ_C) = 0. This literally encodes the vanishing of the total codimension-one boundary of compactified one-dimensional families of bordered configurations.
**Named objects**: Θ_C, Δ_{clutch}, g_X := Conv(C^{oc,log}_{mod}, End(Z^ch(C_op), A_b))

**STRIKELIST**:
1. `chapters/theory/higher_genus_modular_koszul.tex` — The MC element should be stated in the open/closed convolution algebra, not just the closed-sector version.
2. `chapters/connections/concordance.tex` — Update the MC2 entry: Θ_A is the closed-sector projection of the open/closed Θ_C.
3. `chapters/connections/frontier_modular_holography_platonic.tex` — The holographic MC element is Θ_C, not just Θ_A.
4. `Vol II: chapters/connections/modular_pva_quantization_core.tex` — The modular PVA quantization MC element should be identified as the PVA projection of Θ_C.

---

# CLUSTER B: Connected Dirichlet-Sewing Lift and Arithmetic Interface

---

### B.1 — Connected Dirichlet-sewing lift S_A(u)
**Source**: 105, 106
**Description**: The connected genus-one sewing free energy F^{conn}_A(q) = -log det(1 - K_q(A)) = Σ a_A(N)q^N. The connected Dirichlet-sewing lift S_A(u) := Σ a_A(N)N^{-u}. For bosonic weight multiset W(A) = {w_i}: S_A(u) = ζ(u+1) · Σ_i(ζ(u) - H_{w_i-1}(u)).
**Named objects**: S_A(u), F^{conn}_A(q)

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the connected Dirichlet-sewing lift as a new section: definition, general formula, relation to weight multiset.
2. `chapters/connections/genus_complete.tex` — The genus-complete chapter should reference S_A(u) as the arithmetic face of genus-one data.
3. `chapters/connections/concordance.tex` — Add S_A(u) to the characteristic package: (Θ_A, κ, Δ_A, S_A, Π_A, H_A).
4. `chapters/examples/heisenberg_eisenstein.tex` — Add the Heisenberg sewing-to-Euler-product identity S_H(u) = ζ(u)ζ(u+1).
5. `chapters/examples/w_algebras.tex` — Add the W_N Dirichlet-sewing lift with finite harmonic defect.
6. `chapters/connections/thqg_fredholm_partition_functions.tex` — The Fredholm partition function treatment should include the Dirichlet lift.

---

### B.2 — Heisenberg sewing = Euler product (σ_{-1})
**Source**: 105, 106
**Description**: -log det(1 - K_q) = Σ σ_{-1}(N)q^N where σ_{-1}(N) = Σ_{d|N} 1/d. The Dirichlet series Σ σ_{-1}(N)N^{-s} = ζ(s)ζ(s+1), which factors as an Euler product: each prime p contributes (1-p^{-s})^{-1}(1-p^{-s-1})^{-1}.
**Named objects**: Euler-product decomposition of sewing determinant

**STRIKELIST**:
1. `chapters/examples/heisenberg_eisenstein.tex` — This is a major new result for the Heisenberg chapter.
2. `chapters/connections/arithmetic_shadows.tex` — The sewing-to-Euler identity is the first entry in the arithmetic programme.
3. `chapters/connections/thqg_fredholm_partition_functions.tex` — The Fredholm determinant chapter should exhibit this Euler product.

---

### B.3 — Finite Miura defect theorem
**Source**: 105, 106
**Description**: χ^{vac}_{W_N}(q) = χ_H(q)^{N-1} · D_N(q), where D_N(q) = ∏_{m=1}^{N-1}(1-q^m)^{N-m}. D_N is a finite polynomial. All non-Heisenberg genus-one arithmetic information is concentrated in finitely many low modes. Virasoro: D_2(q) = 1-q. W_3: D_3(q) = (1-q)²(1-q²).
**Named objects**: D_N(q) (Miura defect polynomial), finite defect theorem

**STRIKELIST**:
1. `chapters/examples/w_algebras.tex` — Add the finite Miura defect theorem for principal W_N.
2. `chapters/examples/w_algebras_deep.tex` — Extended discussion with Dirichlet-lift form.
3. `chapters/connections/arithmetic_shadows.tex` — The Miura defect as the arithmetic face of DS reduction.
4. `chapters/connections/concordance.tex` — Record as a new proved result.
5. `chapters/examples/landscape_census.tex` — Add D_N(q) to the census tables.

---

### B.4 — Prime-side Li-like coefficients λ̃_n(A)
**Source**: 105, 106
**Description**: Regularize Ξ̃_A(u) := (u-1)S_A(u), define λ̃_n(A) := (1/(n-1)!) d^n/du^n(u^{n-1} log Ξ̃_A(u))|_{u=1}. Heisenberg: λ̃_1(H) ≈ 0.007 (positive). Virasoro: λ̃_1(Vir) ≈ -0.993 (negative). W_N: λ̃_1(W_N) ~ -log N (asymptotically more negative).
**Named objects**: λ̃_n(A) (prime-side Li coefficients)

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Define prime-side Li coefficients and compute for standard families.
2. `chapters/connections/concordance.tex` — Record the two Li theories (zero-side and prime-side).

---

### B.5 — Euler-Koszul condition
**Source**: 105, 106
**Description**: A modular Koszul object is "Euler-Koszul" if its connected sewing lift admits prime-local factors compatible with tensor product, duality, and clutching. Heisenberg = exact Euler-Koszul. Virasoro/W_N = finitely defective. Generic Epstein with h(D) ≥ 2 = not Euler-Koszul.
**Named objects**: Euler-Koszul condition

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Define Euler-Koszul condition; classify standard landscape.
2. `chapters/theory/chiral_koszul_pairs.tex` — Add Euler-Koszul as a new characterization of Koszul-like algebras.

---

### B.6 — Two-variable L-object L_A(s,u)
**Source**: 105, 106
**Description**: L_A(s,u) ∼ ∫_{Γ\H}^{reg} ⟨π_r Θ_A^{conn}(τ), E*(τ,s)⟩ y^{u-2} dμ(τ). The s-variable = zero-side Rankin-Selberg/Eisenstein. The u-variable = prime-side Mellin/Dirichlet sewing. Scalar s-slice = zeta-zero interface. Scalar u-slice = S_A(u).
**Named objects**: L_A(s,u) (two-variable L-object), L_A^{(r)}(s,u) (arity-r version)

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Define the two-variable L-object as the platonic end-state of the arithmetic programme.
2. `chapters/connections/frontier_modular_holography_platonic.tex` — L_A(s,u) as the arithmetic face of the holographic datum.
3. `chapters/connections/concordance.tex` — Record L_A(s,u) in the frontier section.

---

### B.7 — Sewing-Selberg formula
**Source**: 111, 112
**Description**: ∫_{M_{1,1}} log det(1-K(τ)) · E_s(τ) dμ = -2(2π)^{-(s-1)} Γ(s-1) ζ(s-1)ζ(s). The sewing operator, integrated against the Eisenstein series over moduli, produces ζ(s-1)ζ(s).
**Named objects**: Sewing-Selberg formula

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the sewing-Selberg formula as a proved identity.
2. `chapters/connections/thqg_fredholm_partition_functions.tex` — The Fredholm chapter should exhibit this as the spectral bridge.
3. `chapters/connections/concordance.tex` — Record.

---

# CLUSTER C: Quartic Residue/Resonance Programme

---

### C.1 — Hankel moment matrix: Schur complement = quartic contact invariant
**Source**: 105, 106
**Description**: From mixed (s,u)-transforms, moments μ_n define a 3×3 Hankel matrix. In centered gauge: Σ_2 = μ_4 - μ_3²/μ_2 - μ_2² = Q^{ct}_v (quartic contact coefficient exactly). Potential-side D_2 = H_v · Q^{ct}_v. Gram-side D_2 gives quartic resonance norm. They are reciprocal.
**Named objects**: Hankel moment matrix H_2, Schur complement Σ_2

**STRIKELIST**:
1. `chapters/theory/higher_genus_modular_koszul.tex` — Add the Hankel/Schur complement extraction of Q^{ct} as a new construction in the shadow tower.
2. `appendices/nonlinear_modular_shadows.tex` — Add the Hankel determinant interpretation of quartic resonance.
3. `chapters/connections/arithmetic_shadows.tex` — The quartic residue moment matrix as the meeting point of MC shadows and spectral data.

---

### C.2 — Quartic compatibility divisor D_{4,g,n} and clutching defect K
**Source**: 105, 106
**Description**: D_{4,g,n}(A,ρ;u_0) := div(s^{res}_{4,g,n}(A,ρ;u_0) ⊗ (s^{mod}_{4,g,n}(A))^{-1}). Clutching defect: K = ξ*D - p_1*D - p_2*D - T_{3,ξ}^{res}. On-line residues satisfy K=0; off-line fail.
**Named objects**: D_{4,g,n} (quartic compatibility divisor), K_{A,ρ,ξ} (clutching defect)

**STRIKELIST**:
1. `chapters/theory/higher_genus_modular_koszul.tex` — Add the quartic compatibility divisor as the residue-side counterpart of R^{mod}_{4,g,n}.
2. `chapters/connections/arithmetic_shadows.tex` — The compatibility divisor as the arithmetic meeting point.
3. `appendices/nonlinear_modular_shadows.tex` — Explicit Virasoro and W_3 divisors.

---

### C.3 — Crossing-weighted bilinear residue kernel
**Source**: 105, 106
**Description**: The bare spectral measure omits structure constants and collapses a bilinear crossing kernel to scalar. The corrected kernel K^{Liouv}_{c,ρ;u_0,P_0,τ}(P',P'') incorporates DOZZ three-point constants and toric modular kernel. Bilinear because modular transformation acts on conformal blocks, not a scalar density.
**Named objects**: K^{Liouv}(P',P''), crossing-weighted Gram test

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the crossing-weighted kernel construction.
2. `chapters/connections/thqg_modular_bootstrap.tex` — The modular bootstrap chapter should reference this as the correct residue shadow.

---

### C.4 — Beilinson functional B_{A,v}
**Source**: 105, 106
**Description**: B_{A,v} := (m_3^♯/C_{A,v} - 1)² + (S^{res}_{4,A,v}/Q^{ct}_{A,v} - 1)². Vanishes exactly when residue data matches MC shadow data. Global: B_{global}(ρ) := Σ_{A,v} ∫ B_{A,v} dμ.
**Named objects**: Beilinson functional B_{A,v}, closure conjecture

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Define the Beilinson functional.
2. `chapters/connections/concordance.tex` — Record the closure conjecture.

---

# CLUSTER D: Constrained Epstein Zeta and Spectral Bridge

---

### D.1 — Constrained Epstein zeta = literal Riemann zeta (c=1 lattice)
**Source**: 111, 112
**Description**: ε^1_s(V_Z, R=1) = 4ζ(2s). The primary spectrum of the simplest chiral algebra directly reproduces the Riemann zeta function.
**Named objects**: ε^c_s(A) (constrained Epstein zeta)

**STRIKELIST**:
1. `chapters/examples/lattice_foundations.tex` — Add the ε^c_s = 4ζ(2s) identity for V_Z.
2. `chapters/connections/arithmetic_shadows.tex` — This is the foundational bridge between the modular Koszul programme and number theory.

---

### D.2 — Hecke decomposition and shadow depth = number of L-functions
**Source**: 111, 112
**Description**: For lattice VOA V_Λ, ε^r_s(V_Λ) decomposes via Hecke eigenforms. Shadow depth d(A) counts independent L-functions: V_Z (1), V_{E_8} (2), V_{Leech} (3, including L(s,Δ_{12})).
**Named objects**: Hecke decomposition, shadow-depth-counts-L-functions principle

**STRIKELIST**:
1. `chapters/examples/lattice_foundations.tex` — Hecke decomposition for lattice Epstein zeta.
2. `chapters/connections/arithmetic_shadows.tex` — Shadow depth = number of L-functions as a structural principle.
3. `chapters/connections/concordance.tex` — Record this identification.

---

### D.3 — Structural obstruction: real line vs complex poles
**Source**: 111, 112
**Description**: The shadow tower constrains spectral coefficients on the real spectral line. Zeta zeros live at complex spectral parameters. MC constraints cannot reach scattering poles without analytic continuation. Three-gap decomposition: Gap 1 (intertwining/bar-cobar, hard), Gap 2 (arithmetic descent/Hecke for VVMFs, medium), Gap 3 (non-perturbative completion, partially proved).
**Named objects**: Three-gap decomposition, structural obstruction

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the structural obstruction and three-gap analysis.
2. `chapters/connections/concordance.tex` — Honest fencing of what the programme can and cannot do.
3. `chapters/connections/outlook.tex` — The outlook should discuss the three gaps.

---

# CLUSTER E: Arithmetic Packet Connection

---

### E.1 — Arithmetic packet connection ∇^{arith}_A
**Source**: 111, 112
**Description**: For Θ_A and Hecke module M_A = ⊕_χ M_χ with meromorphic packets Λ_χ(s) and nilpotent N_χ: ∇^{arith}_A = d - ⊕_χ d log Λ_χ(s)(id_{M_χ} + N_χ). Flat. Singular divisor D_A = ∪_χ div(Λ_χ) is independent of N_χ.
**Named objects**: ∇^{arith}_A, M_A, Λ_χ(s), N_χ

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — This is already partially installed (def:arithmetic-packet-connection). Needs full treatment with flatness proof, horizontal sections, monodromy formula.
2. `chapters/connections/concordance.tex` — Update the arithmetic packet connection entry.

---

### E.2 — Arithmetic skeleton Ask(A) and algebraic defect Def_{alg}(A)
**Source**: 111, 112
**Description**: Ask(A) := M_A^{ss} (semisimple part). Def_{alg}(A) := ⊕_χ N_χ M_χ (nilpotent part). Slogan: "arithmetic is semisimple; homotopy defect is unipotent." Depth splitting: d(A) = 1 + d_{arith} + d_{alg}.
**Named objects**: Ask(A), Def_{alg}(A), depth decomposition

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Already partially installed. Strengthen with explicit lattice transparency and Virasoro analysis.
2. `chapters/connections/concordance.tex` — Record the "arithmetic is semisimple, defect is unipotent" principle.

---

### E.3 — Frontier defect form Ω_A and gauge criterion
**Source**: 111, 112
**Description**: Ω_A = d log Λ_{Eis}(s) - d log φ(s), comparing Eisenstein packet with automorphic scattering. Gauge criterion: Eisenstein block matches scattering iff N_{Eis} = 0 and Ω_A exact.
**Named objects**: Ω_A (frontier defect form), gauge criterion

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Already partially installed. Fortify with the gauge criterion as a proposition.
2. `chapters/connections/frontier_modular_holography_platonic.tex` — The holographic frontier should reference Ω_A.
3. `chapters/connections/concordance.tex` — Record the gauge criterion.

---

### E.4 — Inevitable comparison conjecture
**Source**: 111, 112
**Description**: Θ_A canonically determines ∇^{arith}_A, functorial under quasi-isomorphism. Semisimplification = Hecke-semisimple quotient. Only obstruction to matching automorphic scattering = frontier defect form on Eisenstein block.
**Named objects**: Inevitable comparison conjecture

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — State as a named conjecture.
2. `chapters/connections/concordance.tex` — Add to the conjectural frontier.

---

# CLUSTER F: Entanglement-Annulus Theorem

---

### F.1 — Entropy = annular trace of modular open/closed chiral homotopy
**Source**: 108
**Description**: S_EE(C_op) = (2κ/3)log(L/ε) + Σ_{r≥3} ΔS_r, where ΔS_r = -∂_n|_{n=1}(1/r!)Tr^{(n)}_C(⟨Θ^{(r)}_C, [A_n]^{(r)}_{conn}⟩). The scalar term = Calabrese-Cardy. Shadow corrections = annular connected expansion of Θ_C.
**Named objects**: S_ann(X), [A_n]^{(r)}_{conn} (connected r-vertex annular chain), replica annuli

**STRIKELIST**:
1. `chapters/connections/entanglement_modular_koszul.tex` — Rewrite to derive S_EE from the annular trace of the open sector, not as an independent construction.
2. `chapters/connections/thqg_entanglement_programme.tex` — Upgrade with the entanglement-annulus theorem.
3. `chapters/connections/concordance.tex` — Record the entanglement-annulus theorem.
4. `Vol II: chapters/connections/modular_pva_quantization_core.tex` — The PVA quantization should exhibit the entropy formula.

---

### F.2 — Complementarity as modular anti-symmetry Θ_A + Θ_{A!} = 0
**Source**: 108
**Description**: Dual open sectors contribute opposite nonlinear annular shadows. For Virasoro: S^{scalar}_EE(Vir_c) + S^{scalar}_EE(Vir_{26-c}) = (26/3)log(L/ε) and shadow corrections preserve this.
**Named objects**: Θ_A + Θ_{A!} = 0 (modular anti-symmetry)

**STRIKELIST**:
1. `chapters/theory/higher_genus_complementarity.tex` — Reinterpret complementarity as modular anti-symmetry at the annular level.
2. `chapters/connections/entanglement_modular_koszul.tex` — Complementarity as conservation law for entropy.
3. `chapters/connections/concordance.tex` — Update Theorem C description.

---

### F.3 — W_3 first nonlinear entropy correction
**Source**: 108, 110
**Description**: ΔS^{mod}_4(W_3) = -∂_n|_{n=1} Tr^{(n)}_{W_3}(⟨R^{mod}_{4,ann}(W_3), [A_n]_{conn}⟩). This is the first genuinely nonlinear modular entropy correction, forced by Λ = :TT: - (3/10)∂²T.
**Named objects**: ΔS^{mod}_4(W_3), quartic annular correction

**STRIKELIST**:
1. `chapters/connections/entanglement_modular_koszul.tex` — Add the W_3 quartic prediction.
2. `chapters/examples/w_algebras.tex` — Add the W_3 entropy correction to the W_3 shadow archetype.
3. `chapters/connections/concordance.tex` — Record.

---

# CLUSTER G: Logarithmic CFT via Root Stacks

---

### G.1 — q-root boundary as geometric cyclotomic input
**Source**: 109
**Description**: Replace the formal boundary disc D by its q-fold Kummer cover D̃ = Spec ℂ((u)), t = u^q. Deck group μ_q acts by ζ·u = ζu. Root stack D^{(q)} = [Spec ℂ[[u]]/μ_q]. This makes q geometric rather than requiring a choice of internal automorphism σ. Tautological line bundle T with section u.
**Named objects**: D^{(q)} (q-root boundary), Kummer local systems L_j = T^{⊗j}

**STRIKELIST**:
1. `chapters/theory/filtered_curved.tex` — Add the root stack construction as the geometric source of CDG periodicity.
2. `chapters/connections/concordance.tex` — New section on logarithmic CFT foundations.
3. `appendices/nilpotent_completion.tex` — The nilpotent completion appendix should reference q-root boundaries.

---

### G.2 — Canonical cyclotomic boundary chart A^{cyc}_{k,q}
**Source**: 109
**Description**: At admissible k = -h^∨ + p/q, pull V_k to q-root boundary. Canonical boundary vacuum b^{cyc}_{k,q} := ⊕_{j∈ℤ/qℤ} T^{⊗j} ⊗ π_q^*V_k. Chart: A^{cyc}_{k,q} := RHom(b^{cyc}, b^{cyc}). Generators: sector idempotents e_j, currents J^a_j(n+r/q), shift arrows s_j. Relations: QLS (quadratic-linear-scalar). Nilpotent q-cycle on special fiber forces logarithmicity.
**Named objects**: A^{cyc}_{k,q}, b^{cyc}_{k,q}, sector-shift operator S_q, canonical cyclotomic boundary theorem

**STRIKELIST**:
1. `chapters/theory/filtered_curved.tex` — Add the cyclotomic chart construction.
2. `chapters/examples/kac_moody.tex` — Add the admissible-level cyclotomic boundary chart for affine algebras.
3. `chapters/theory/chiral_koszul_pairs.tex` — QLS structure of cyclotomic charts feeds into quadratic duality.
4. `chapters/connections/concordance.tex` — Record the canonical cyclotomic boundary theorem.
5. `Vol II: chapters/connections/log_ht_monodromy_core.tex` — The log-HT monodromy should reference root-stack logarithmicity.

---

### G.3 — Nilpotent q-cycle forces logarithmicity
**Source**: 109
**Description**: On the special fiber t=0, the composition s_{j+q-1}∘⋯∘s_j = t·id_j = 0 is nilpotent. The boundary algebra's radical is generated by shift arrows. The local module category is never semisimple when q > 1. Logarithmicity comes from root-boundary geometry, not imported externally.
**Named objects**: Nilpotent degeneration, automatic logarithmicity

**STRIKELIST**:
1. `chapters/theory/filtered_curved.tex` — Explain the mechanism: nilpotent q-cycle ⟹ nonsemisimple category.
2. `chapters/connections/concordance.tex` — "Where does logarithmicity come from?" answer: root-boundary geometry.

---

# CLUSTER H: 3d HT Realizations and Explicit Computations

---

### H.1 — Khan-Zeng 3d HT gauge theory from PVA
**Source**: 107, 110
**Description**: S[φ,η] = ∫_{ℝ×ℂ} dz(η_i(dt+d̄)φ_i + ½η_iΠ^{ij}(∂)η_j). Gauge invariance ⟺ λ-Jacobi identity. Inner Virasoro ⟹ topological upgrade.
**Named objects**: Khan-Zeng 3d HT action

**STRIKELIST**:
1. `chapters/connections/holomorphic_topological.tex` — Add the Khan-Zeng construction as the PVA→3d bridge.
2. `Vol II: chapters/connections/bv_ht_physics.tex` — Reference Khan-Zeng as concrete realization.
3. `Vol II: chapters/theory/pva-descent.tex` — The PVA descent should mention gauge-invariance = λ-Jacobi.

---

### H.2 — Explicit boundary OPE from Feynman computation
**Source**: 107
**Description**: Full first-principles derivation: bulk propagator → boundary propagator by method of images → unique tree-level diagram → Feynman parameter evaluation of half-space integral I(z,z̄) = -2π/z → final OPE ψ̂_i(z)ψ̂_j(0) ~ (1/z)∂_i∂_jW|_L.
**Named objects**: Half-space integral I(z,z̄), boundary OPE derivation

**STRIKELIST**:
1. `Vol II: chapters/connections/affine_half_space_bv.tex` — Add the complete Feynman computation as a worked example.
2. `chapters/connections/ym_boundary_theory.tex` — Reference for boundary OPE from bulk propagator.
3. `Vol II: chapters/connections/bv_ht_physics.tex` — The BV/HT physics chapter should include this computation.

---

### H.3 — Explicit A∞ line-operator algebra A^!(d) and dg-shifted Yangian
**Source**: 107
**Description**: For W(X) = (1/d!)X^d: generators X_n, ψ_n with m_k(ψ_{n_1},…,ψ_{n_k}) = -(1/(k!(d-k)!))Σ X_{m_1}⋯X_{m_{d-k}}, m_k = 0 for k ≥ d. Degree d = height of higher-operation tower. Universal MC element r(z) defining twisted coproduct and A∞ Yang-Baxter equation.
**Named objects**: A^!(d), r(z), Δ_z, A∞ Yang-Baxter

**STRIKELIST**:
1. `chapters/examples/yangians_foundations.tex` — Add the explicit A^!(d) construction from Dimofte-Niu-Py.
2. `chapters/examples/yangians_drinfeld_kohno.tex` — The dg-shifted Yangian should reference A∞ Yang-Baxter.
3. `chapters/connections/frontier_modular_holography_platonic.tex` — r(z) as binary genus-0 shadow of Θ_A.
4. `Vol II: chapters/connections/ht_bulk_boundary_line_core.tex` — Line operators = A^!-modules with dg-shifted Yangian.

---

# CLUSTER I: Mellin-Clutching Transform and Zeta-Zero Bridge

---

### I.1 — Annular partition function Z_ann(q,u) and Mellin-clutching transform Ξ_X(s)
**Source**: 110
**Description**: Z_ann(q,u) := Tr_{HH_*(C_op)}(q^{L_0-c/24}u^H). Mellin-clutching: Ξ_X(s) := ∫_0^∞(Z_ann(e^{-t},1) - CT_0(t) - CT_∞(t))t^{s/2-1}dt. Nodal clutching ⟹ s↔1-s symmetry.
**Named objects**: Z_ann(q,u), Ξ_X(s)

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the Mellin-clutching transform.
2. `chapters/connections/thqg_fredholm_partition_functions.tex` — Connect to Fredholm partition functions.
3. `chapters/connections/concordance.tex` — Record.

---

### I.2 — Clutching-symmetrized Mellin = completed zeta ξ(s) (PROVED for Heisenberg)
**Source**: 110
**Description**: For the Heisenberg open factorization category on (P¹,{0,∞}), the scalar annular resonance trace is ϑ(t) = Σ_{n∈ℤ}e^{-πn²t}. THEOREM: Ξ_{ann}(s) = ξ(s) = ½s(s-1)π^{-s/2}Γ(s/2)ζ(s). Proof: Mellin representation + Poisson summation.
**Named objects**: Ξ_{ann}(s) = ξ(s), full open-sector datum X_Θ

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — This is a MAJOR result: the modular Koszul programme reproduces ξ(s) in the Heisenberg sector.
2. `chapters/examples/heisenberg_eisenstein.tex` — Add as a theorem in the Heisenberg chapter.
3. `chapters/connections/concordance.tex` — Record as proved.
4. `chapters/connections/outlook.tex` — The outlook should discuss what this means for the RH interface.

---

### I.3 — Modular normal form and exact cancellation theorem
**Source**: 110
**Description**: Θ_C = Θ_2 + Θ_3 + Θ_4 + ⋯ (shadow degree decomposition). Cubic annular gauge triviality: Θ^{ann}_3 = D_2K_2 (D_2-exact). Cyclic trace kills boundaries: Tr_C(D_2η) = 0. After normal form, scalar annular trace sees only cohomology classes of nonlinear shadows.
**Named objects**: D_2 (quadratic modular differential), exact cancellation theorem, [(Θ'_4)^{ann}] as decisive obstruction

**STRIKELIST**:
1. `chapters/theory/higher_genus_modular_koszul.tex` — Add the modular normal form decomposition and exact cancellation theorem.
2. `appendices/nonlinear_modular_shadows.tex` — The shadow tower should include the normal form analysis.
3. `chapters/connections/concordance.tex` — Record.

---

### I.4 — Three levels of spectral rigidity
**Source**: 110
**Description**: (A) Exact analytic rigidity: if E(t) satisfies Poisson symmetry, δΞ is entire with δΞ(s) = δΞ(1-s). (B) Finite-window Rouché rigidity: sup-norm bounds on δΞ vs inf of |ξ| on contours. (C) First-order critical-line rigidity: E real ⟹ δΞ real on critical line. GUE/pair-correlation rigidity remains OPEN.
**Named objects**: Three rigidity levels (A, B, C), Rouché bounds

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the three rigidity levels.
2. `chapters/connections/outlook.tex` — Discuss as the spectral frontier.

---

# CLUSTER J: Genus-Zero Skeleton and Modular Globalization

---

### J.1 — Genus-zero skeleton S_0(A_b) = (A_b, C*_ch, A^!, r(z))
**Source**: 111, 112
**Description**: The genus-zero data package: boundary chart, intrinsic bulk (Hochschild cochains), line Koszul dual, and genus-zero line-OPE datum.
**Named objects**: S_0(A_b)

**STRIKELIST**:
1. `chapters/connections/frontier_modular_holography_platonic.tex` — Define S_0(A_b) as the genus-zero skeleton of the holographic datum.
2. `chapters/connections/concordance.tex` — Add genus-zero skeleton.

---

### J.2 — Modular globalization conjecture
**Source**: 111, 112
**Description**: ∃ filtered dg Lie algebra g_X := Conv(C^{mod}_{oc,log}, End(Z^ch(C_op), A_b)) such that modular completions of S_0(A_b) are MC elements Θ_C ∈ MC(g_X), genus-zero part recovers S_0(A_b).
**Named objects**: g_X, modular globalization conjecture

**STRIKELIST**:
1. `chapters/theory/higher_genus_modular_koszul.tex` — State the modular globalization conjecture.
2. `chapters/connections/concordance.tex` — Record as conjectural.
3. `chapters/connections/frontier_modular_holography_platonic.tex` — The platonic programme should target modular globalization.

---

### J.3 — First obstruction theorem (quartic)
**Source**: 111, 112
**Description**: First obstruction to modular globalization lies in quartic filtration, represented by [R^{mod}_{4,g,n}] ∈ H²(gr⁴_F g_X). This is because cubic gauge triviality removes the cubic obstruction.
**Named objects**: First obstruction theorem

**STRIKELIST**:
1. `chapters/theory/higher_genus_modular_koszul.tex` — State as theorem target.
2. `chapters/connections/concordance.tex` — Record.

---

# CLUSTER K: Beilinson Falsification Pass

---

### K.1 — Eight hard discard criteria
**Source**: 105, 106
**Description**: Any candidate idea fails if it: (1) doesn't recover BD complementarity; (2) treats bar-cobar as arithmetic rigidity; (3) ignores Miura injectivity; (4) proposes un-regularized shadow; (5) places quartic rigidity in Heisenberg core; (6) compares residues only as scalars; (7) relies on zeta-proxy; (8) seeks positivity on curve without polarized lift.

**STRIKELIST**:
1. `chapters/connections/concordance.tex` — Add the eight discard criteria as a permanent filter.

---

### K.2 — Killed ideas: MC⟹Li, bar-cobar⟹RH, naive spectral zeta, etc.
**Source**: 105, 106, 111, 112
**Description**: Seven explicitly falsified research directions. MC is flatness, not positivity. Bar-cobar is homotopical, not spectral. Heisenberg is quartically blind. Single-family closure fails. CDG loses information vs twisted pair.

**STRIKELIST**:
1. `chapters/connections/concordance.tex` — Honest fencing: record what the programme cannot do.
2. `chapters/connections/outlook.tex` — Explicitly list killed directions.
3. `chapters/connections/arithmetic_shadows.tex` — Ensure no false claims about MC⟹Li survive.

---

### K.3 — Twisted pair (B, B^∘, S) as primary dual object (not CDG reduction)
**Source**: 111, 112
**Description**: Gui-Li-Zeng: passing from twisted pair to CDG chiral algebra loses information. The twisted pair carries the natural twisted MC equation μ((S+α) ⊠ (S+α)) = 0. For dualizable effective QLS data: bijection between morphisms out of A and solutions of twisted MC.
**Named objects**: twisted pair T_A = (B ⊂ B^∘, S), twisted MC equation

**STRIKELIST**:
1. `chapters/theory/chiral_koszul_pairs.tex` — Emphasize twisted pair over CDG; state the Gui-Li-Zeng theorem.
2. `chapters/theory/filtered_curved.tex` — Clarify that CDG is a coarsening of the twisted pair.
3. `chapters/connections/concordance.tex` — Record.

---

# CLUSTER L: W_3 as Critical Test Case

---

### L.1 — W_3 forces nonlinear composites unavoidably
**Source**: 107, 108, 110
**Description**: {W_λ W} produces Λ = :TT: - (3/10)∂²T with β² = 16/(22+5c). The algebra does not close linearly on T, W. This forces higher composites, genuine open categories, and modular towers.
**Named objects**: Λ, β² = 16/(22+5c)

**STRIKELIST**:
1. `chapters/examples/w_algebras.tex` — Strengthen the treatment of Λ as the structural generator of nonlinearity.
2. `chapters/examples/w3_composite_fields.tex` — Upgrade to full quartic shadow analysis.
3. `chapters/connections/concordance.tex` — W_3 as the decisive test case for nonlinear modularity.

---

### L.2 — W_3 quartic Gram determinant: closed form
**Source**: 110
**Description**: det G^{ct}_{W_3,norm} = (1/10)c³(2c-1)(5c+22)². Multiplicities: 3[c=0] + [2c-1=0] + 2[5c+22=0]. The weight-4 block (Λ) contributes ⟨Λ,Λ⟩ = c(5c+22)/10. The weight-6 block (Λ_2, Λ_3) contributes det G_6 ∝ c²(2c-1)(5c+22).
**Named objects**: det G^{ct}_{W_3}, quartic resonance multiplicities

**STRIKELIST**:
1. `chapters/examples/w3_composite_fields.tex` — Add the closed-form quartic Gram determinant.
2. `chapters/examples/w_algebras.tex` — Add to the W_3 shadow archetype.
3. `appendices/nonlinear_modular_shadows.tex` — Add W_3 quartic resonance divisor.
4. `chapters/examples/landscape_census.tex` — Add to census tables.

---

### L.3 — Quartic shadow envelope E_{W_3}[4]
**Source**: 110
**Description**: E_{W_3}[4] = ℂ⟨T, W, Λ, Λ_2, Λ_3⟩ with weight-4 and weight-6 quasi-primary composites. Normal form: H_{W_3} = (c/2)t² + (c/3)w², C^{grav}_{W_3} = 2t³ + 3tw², plus quartic contact sector.
**Named objects**: E_{W_3}[4], Θ^{≤4}_{W_3}

**STRIKELIST**:
1. `chapters/examples/w3_composite_fields.tex` — Define the quartic shadow envelope.
2. `chapters/theory/higher_genus_modular_koszul.tex` — Reference as first nonlinear shadow example.

---

### L.4 — W_3 nonlinear deformation of theta/oper kernel
**Source**: 110
**Description**: Ξ^{(4)}_{W_3}(s;ε,c) = ∫_0^∞(Z_θ(e^{-t})·exp(ε·Q^{ann}_{W_3}(e^{-t};c)) - CT)t^{s/2-1}dt. At ε=0 collapses to theta/oper kernel. At first order: tests whether W_3 quartic completion perturbs zero statistics.
**Named objects**: Ξ^{(4)}_{W_3}, Q^{ann}_{W_3}

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the nonlinear deformation of the spectral kernel.
2. `chapters/connections/outlook.tex` — Discuss as the first concrete nonlinear numerical target.

---

# CLUSTER M: Multi-Color Swarm Architecture

---

### M.1 — Five simultaneous forward vectors
**Source**: 111, 112
**Description**: (a) Parametrized bar-cobar / intertwiner family (Blue-1); (b) Arithmetic descent via VVMF Hecke theory (Green-1); (c) Completed genus-by-genus MC machine (Blue-2); (d) Nonlinear modular shadow calculus with quintic/sextic (Blue-3); (e) Boundary/defect realization (Magenta). Plus Red adversarial teams for falsification.

**STRIKELIST**:
1. `chapters/connections/outlook.tex` — The outlook chapter should organize future directions along these five vectors.
2. `chapters/connections/concordance.tex` — Record the five-vector programme.

---

# CLUSTER N: Five-Theorem Programme (F1–F5)

---

### N.1 — F1: Arithmetic shadow theorem
**Source**: 105, 106
**Description**: Construct regularized L_A(s,u) for every admissible modular-Koszul family, functorial in A, compatible with modular scattering in s and connected sewing in u.

### N.2 — F2: Miura defect theorem
**Source**: 105, 106
**Description**: L_{W_N} = L_H^{N-1} + L^{def}_{W_N} with genus-one u-face defect from D_N(q).

### N.3 — F3: Residue-resonance theorem
**Source**: 105, 106
**Description**: At arity 4: s^{res}_{4,g,n}(A,ρ;u_0) = s^{mod}_{4,g,n}(A) iff Re(ρ) = 1/2.

### N.4 — F4: Surface realization theorem
**Source**: 105, 106
**Description**: Realize quartic Gram determinant line on modular surface with polarized intersection control.

### N.5 — F5: Simultaneous-family rigidity theorem
**Source**: 105, 106
**Description**: ∩_F {ρ : D_{4,g,n}(A,ρ;u_0) = 0 ∀A∈F} = {ρ : Re(ρ) = 1/2}.

**STRIKELIST for N.1–N.5**:
1. `chapters/connections/arithmetic_shadows.tex` — State all five theorems as the target programme.
2. `chapters/connections/concordance.tex` — Record all five as conjectural targets.
3. `chapters/connections/outlook.tex` — Organize as the five-theorem programme.

---

# CLUSTER O: Analytic Continuation as Functor

---

### O.1 — Analytic continuation must be a functor, not a trick
**Source**: 111, 112
**Description**: AC(A) should take completed modular Koszul data → meromorphic automorphic scattering data, separate d_{arith} from d_{alg}, be invariant under L∞ quasi-isomorphism, and admit boundary/defect geometric realization.
**Named objects**: AC(A) (completed arithmetic transform functor)

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — State the functoriality requirement.
2. `chapters/connections/concordance.tex` — Record as a desideratum.

---

### O.2 — Affine Grassmannian as geometric realization of continuation
**Source**: 111, 112
**Description**: Boundary bundles trivialized on boundary extend to punctured disc with finite-order poles, identifying complex-analytic and algebro-geometric affine Grassmannian. Continuation should live as motion in Gr_G family.

**STRIKELIST**:
1. `chapters/connections/frontier_modular_holography_platonic.tex` — Reference affine Grassmannian as geometric continuation site.
2. `chapters/theory/derived_langlands.tex` — Add the affine Grassmannian continuation picture.

---

### O.3 — VVMF Hecke theory as Gap-2 closure
**Source**: 111, 112
**Description**: Character vectors of rational VOAs are VVMFs. Franc-Mason (2017) develop Hecke operators. Needed: decomposition into Hecke eigenforms → L-functions → analytic continuation → Langlands parametrization by opers.

**STRIKELIST**:
1. `chapters/connections/arithmetic_shadows.tex` — Add the VVMF Hecke programme.
2. `chapters/connections/concordance.tex` — Record as the arithmetic descent gap.

---

# CLUSTER P: Corrected Trichotomy and Structural Principles

---

### P.1 — Bar/cobar = couplings, Hochschild = bulk, Lines = A^!-mod
**Source**: 107, 108, 109, 111, 112
**Description**: The non-negotiable three-way split. Bar/cobar classifies twisting morphisms (Hom(ΩC, A) = Tw(C,A) = Hom(C, BA)). The bulk is the chiral Hochschild cochain algebra C*_ch(A_b, A_b). The line category is A^!-mod. These are three different objects that must never be conflated.

**STRIKELIST**:
1. `chapters/theory/introduction.tex` — State the trichotomy prominently.
2. `chapters/theory/bar_construction.tex` — Add remark: "bar/cobar classifies couplings, not the bulk."
3. `chapters/theory/chiral_hochschild_koszul.tex` — Add remark: "Hochschild cochains = the bulk."
4. `chapters/connections/concordance.tex` — Record the corrected trichotomy.
5. `Vol II: chapters/connections/bar-cobar-review.tex` — Correct any conflation.
6. `Vol II: chapters/connections/ht_bulk_boundary_line_core.tex` — Enforce the trichotomy.

---

### P.2 — Frontier reframed: "Can S_0(A_b) be modularized?"
**Source**: 111, 112
**Description**: The frontier is no longer "Can finite shadow data see zeta zeros?" It is: "Can the genus-zero skeleton be modularized, and is the first modular obstruction exactly the quartic resonance class?"

**STRIKELIST**:
1. `chapters/connections/outlook.tex` — Reframe the frontier question.
2. `chapters/connections/concordance.tex` — Update the frontier description.
3. `chapters/connections/frontier_modular_holography_platonic.tex` — Reframe accordingly.

---

# Summary Statistics

| Cluster | # Concepts | Key new objects | Primary strike targets |
|---------|-----------|----------------|----------------------|
| A (Open/Closed) | 10 | X, C_op, U(A), Ran^{oc}, C^{oc,log}_{mod}, Θ_C | introduction, concordance, higher_genus_modular_koszul, frontier_modular_holography_platonic, Vol II ht_bulk_boundary_line |
| B (Dirichlet-Sewing) | 7 | S_A(u), D_N(q), λ̃_n, L_A(s,u) | arithmetic_shadows, heisenberg_eisenstein, w_algebras, concordance |
| C (Quartic Residue) | 4 | H_2, D_{4,g,n}, K_{A,ρ,ξ}, B_{A,v} | higher_genus_modular_koszul, arithmetic_shadows, nonlinear_modular_shadows |
| D (Epstein/Spectral) | 3 | ε^c_s, Hecke decomposition, 3-gap | lattice_foundations, arithmetic_shadows, concordance |
| E (Packet Connection) | 4 | ∇^{arith}_A, Ask(A), Ω_A | arithmetic_shadows, concordance |
| F (Entanglement-Annulus) | 3 | S_ann, Θ_A+Θ_{A!}=0, ΔS_4(W_3) | entanglement_modular_koszul, concordance, w_algebras |
| G (Root Stacks/Log CFT) | 3 | D^{(q)}, A^{cyc}_{k,q}, nilpotent q-cycle | filtered_curved, kac_moody, concordance |
| H (3d HT/Feynman) | 3 | Khan-Zeng action, A^!(d), boundary OPE | holomorphic_topological, yangians, Vol II bv_ht_physics |
| I (Mellin-Clutching) | 4 | Ξ_X(s), Ξ_{ann}=ξ(s), normal form, 3 rigidities | arithmetic_shadows, heisenberg_eisenstein, concordance |
| J (Globalization) | 3 | S_0(A_b), g_X, first obstruction thm | frontier_modular_holography_platonic, higher_genus_modular_koszul, concordance |
| K (Beilinson Pass) | 3 | 8 discard criteria, killed ideas, twisted pair primacy | concordance, outlook, chiral_koszul_pairs |
| L (W_3 Test) | 4 | det G^{ct}_{W_3}, E_{W_3}[4], Ξ^{(4)}_{W_3} | w3_composite_fields, w_algebras, landscape_census |
| M (Swarm) | 1 | 5 forward vectors | outlook, concordance |
| N (F1–F5) | 5 | F1–F5 programme | arithmetic_shadows, concordance, outlook |
| O (Continuation) | 3 | AC(A), Gr_G, VVMF Hecke | arithmetic_shadows, derived_langlands, concordance |
| P (Trichotomy) | 2 | Corrected trichotomy, reframed frontier | introduction, concordance, bar_construction |

**Total distinct concepts: 62 clusters containing 142 items**
**Total distinct strike targets: ~45 files across Vol I and Vol II**
**Most-hit files**: concordance.tex (32 strikes), arithmetic_shadows.tex (22 strikes), higher_genus_modular_koszul.tex (10 strikes), frontier_modular_holography_platonic.tex (8 strikes), outlook.tex (7 strikes)
