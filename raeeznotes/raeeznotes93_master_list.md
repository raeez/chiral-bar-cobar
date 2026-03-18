# raeeznotes93 — Master Concept / Resource / Action List

## Part A: ATOMIC CONCEPT INVENTORY

### A1. THE THREE FOUNDATIONAL PREPRINTS

#### A1.1 Malikov–Schechtman (MS24): Homotopy Chiral Algebras
- **A1.1.1** Ch∞-algebra (homotopy chiral algebra) as the primitive local object
- **A1.1.2** Čech totalization: A∞^ch := Č•(U; A) as the correct derived chiral input
- **A1.1.3** Secondary Borcherds operations F_n: Lie(n) ⊗ Y(n) → P_n({A∞}, A∞)
- **A1.1.4** Jacobiator homotopy from ∂M̄_{0,4} (three boundary points)
- **A1.1.5** Global chiral data must be modeled by Ch∞-objects, NOT strict sheaves
- **A1.1.6** Rectification: every Ch∞-algebra rectifies to a strict chiral algebra
- **A1.1.7** Higher derived OPE operations encoded by F_n

#### A1.2 Robert-Nicoud–Wierstra (RNW19) + Vallette (Val16): Convolution L∞
- **A1.2.1** Operadic twisting morphism α: C → P yields L∞ on Hom(C-coalg, P-alg)
- **A1.2.2** ONE-SLOT-ONLY PRINCIPLE: functoriality for ∞-morphisms in EITHER slot, NOT both
- **A1.2.3** This is a structural constraint (coherence law), not a technical nuisance
- **A1.2.4** Taylor coefficients via coproduct formula: ℓ_k(f_1,...,f_k)(x) = γ_A(α∘1_D)(f_1⊗...⊗f_k)Δ_D^k(x)
- **A1.2.5** Vallette model structures on coalgebras over Koszul dual cooperad
- **A1.2.6** Quillen equivalence: Ho(dg P-alg) ≃ ∞-P-alg/~_h
- **A1.2.7** Rectification theorem: different Ch∞ presentations → quasi-iso deformation theories
- **A1.2.8** Bar-cobar B_κ ⊣ Ω_κ is a Quillen equivalence (thm:quillen-equivalence-chiral)
- **A1.2.9** Standing convention for manuscript: freeze one slot strict, let other vary by ∞-morphisms
- **A1.2.10** Colored convolution sL∞ algebra: explicit Taylor coefficients ℓ_m via RNW formula

#### A1.3 Mok (Mok25): Logarithmic Fulton–MacPherson Spaces
- **A1.3.1** FM_n(X|D) as simple-normal-crossings compactification on snc pairs
- **A1.3.2** Planted-forest stratification of boundary
- **A1.3.3** Rigid combinatorial types indexing boundary strata
- **A1.3.4** Log-smooth degeneration FM_n(W/B) → B (proper flat)
- **A1.3.5** Degeneration formula: FM_n(W/B)(ρ) → Π_{v∈V(S_ρ,1)} FM_{I_v}(Y_v|D_v)
- **A1.3.6** Tropical correspondence: G_pf = Trop(FM_n(C|D)) (planted forests)
- **A1.3.7** Codimension formula: codim W_ν = Σ w_i + Σ(|V(T_{v_j})| - 1)
- **A1.3.8** Seven boundary types of FM_3: {12, 23, 13, 123, 12<123, 23<123, 13<123}
- **A1.3.9** Codimension multiset for FM_3: [1,1,1,1,2,2,2]
- **A1.3.10** Rigid-type clutching correspondences (push-pull from birational modification)
- **A1.3.11** Geometric depth filtration on log FM chains
- **A1.3.12** Log FM ≠ classical FM; requires snc pair (X,D). Ordinary FM = D=∅ case

### A2. THE SYNTHESIS: MODULAR CONVOLUTION L∞ THEORY

#### A2.1 The Core Object
- **A2.1.1** g_A^mod := Conv_α^mod(C_mod^logFM, End_{Ch∞}(A∞^ch)) — the modular convolution L∞-algebra
- **A2.1.2** Two inputs: geometric cooperad (log FM chains) + derived chiral endomorphism operad
- **A2.1.3** L∞ structure from RNW convolution theory
- **A2.1.4** Homotopy invariance from Vallette's rectification
- **A2.1.5** Strict chart: Convstr(C_mod^logFM, End_{Ch∞}(A∞^ch))
- **A2.1.6** The coderivation dg Lie algebra L_mod(C) = Coder(B_mod(C))[-1] is strict model
- **A2.1.7** Convolution description: L_mod ≅ Hom(B_mod, sC)[-1] with commutator bracket

#### A2.2 Logarithmic FM Coefficient System
- **A2.2.1** C_{X,D}^logFM(n) := C•(FM_n(X|D)) — chains on log FM for log curves
- **A2.2.2** C_{W/B}^logFM(n) := C•(FM_n(W/B)) — chains for semistable families
- **A2.2.3** Graphwise factorization over rigid types
- **A2.2.4** Log FM chain cooperad C_mod^logFM as the coefficient cooperad
- **A2.2.5** Graphwise log-FM cocomposition: Δ_Γ^log := (ν_Γ)_* ∘ Res_{D_Γ^log}

#### A2.3 Modular Homotopy Type
- **A2.3.1** M_A^mod(R) := MC(g_A^mod ⊗̂_m R)/~ for local Artin R
- **A2.3.2** Formal moduli problem packaging all genera + all collision/clutching data
- **A2.3.3** Replaces "modular deformation tower" with homotopy-theoretic object

#### A2.4 Ontological Shift
- **A2.4.1** OLD: "build Def_cyc(A), solve MC, recover Θ_A"
- **A2.4.2** NEW: "the actual object is Conv_α^mod(...); Θ_A is graph-sum MC by construction"
- **A2.4.3** Scalar/spectral package = characteristic shadows, not separate packages
- **A2.4.4** The completed programme = modular Chern–Weil theory of factorization algebras
- **A2.4.5** MC2 should become organizing spine, not final conjectural appendix

### A3. MODULAR BAR CONSTRUCTION

#### A3.1 Modular Bar Datum (Abstract Axioms)
- **A3.1.1** Internal differential d: C(F) → C(F) of degree +1
- **A3.1.2** One-edge expansion maps Δ_ε for each ε ∈ OE(F)
- **A3.1.3** Separating expansion: two vertices joined by one edge
- **A3.1.4** Nonseparating expansion: one vertex carrying one loop
- **A3.1.5** Codimension-two cancellation axiom (signed sum of two paths = 0)
- **A3.1.6** Anticommutation: d anticommutes with every Δ_ε

#### A3.2 Complete Modular Bar Coalgebra
- **A3.2.1** B_mod(C) = Π_{[Γ]} (C[Γ])_{Aut(Γ)} completed over total genus
- **A3.2.2** C[Γ] = orline(Γ) ⊗ ⊗_{v∈V(Γ)} s C(Fl(v))
- **A3.2.3** Orientation line: orline(Γ) = det(kE(Γ)) ⊗ det(H_1(Γ;k))^{-1}
- **A3.2.4** D^2 = 0 theorem (three cancellation mechanisms)
- **A3.2.5** Complete conilpotent modular dg coalgebra
- **A3.2.6** Tree-level truncation B^ch(C) = genus-0 subquotient

#### A3.3 Concrete Graphwise Formula
- **A3.3.1** B_mod(A)(g,n) = ⊕_{Γ∈StGr(g,n)} (⊗_v B̄^ch_loc(A∞^ch; In(v)) ⊗ C_Γ^logFM ⊗ Det(E(Γ)))_{Aut(Γ)}
- **A3.3.2** Each vertex: transferred local Ch∞-bar contribution
- **A3.3.3** Each edge: propagator/cyclic pairing contraction
- **A3.3.4** C_Γ^logFM: chain complex of log FM stratum
- **A3.3.5** Det(E(Γ)): edge-orientation line

#### A3.4 Five-Component Differential
- **A3.4.1** D_mod = d_Č + d_{Ch∞} + d_coll + d_sew + d_loop
- **A3.4.2** d_Č: Čech descent (globalization)
- **A3.4.3** d_{Ch∞}: transferred higher chiral operations (MS24)
- **A3.4.4** d_coll: collision = residues/integration along FM boundary divisors
- **A3.4.5** d_sew: boundary clutching (separating edges)
- **A3.4.6** d_loop: self-gluing / genus-raising contractions (nonseparating edges)
- **A3.4.7** Alternative: D = d_int + [τ, -] + d_sew + d_pf + ℏΔ

#### A3.5 One-Edge Decomposition
- **A3.5.1** D_exp = D_sep + D_nsep
- **A3.5.2** D_0 = D_int + D_sep (preserves total genus)
- **A3.5.3** D_1 = D_nsep (raises total genus by 1)
- **A3.5.4** D_0² = 0, D_0 D_1 + D_1 D_0 = 0, D_1² = 0

#### A3.6 The One-Edge Principle
- **A3.6.1** "A deformation theory that only remembers trees cannot see modular obstructions"
- **A3.6.2** Necessity theorem: if d preserves genus exactly, g=0 MC extends tautologically
- **A3.6.3** Nonseparating one-edge expansion = algebraic counterpart of first loop correction
- **A3.6.4** The primitive genus-raising operator is NOT a generic higher operator — it is precisely one-edge expansion

#### A3.7 Curved Extension (S-tails)
- **A3.7.1** Gui–Li–Zeng twisted pairs (B, B°, S)
- **A3.7.2** S-tail expansion: attach univalent S-decorated vertex
- **A3.7.3** Curved modular bar from S-tail + one-edge expansions
- **A3.7.4** Modular analogue of curved MC equation μ((S+α)⊠(S+α)) = 0

#### A3.8 Planted-Forest Differential
- **A3.8.1** d_pf = Σ_{ρ∈PF^rig} ε_ρ (κ_ρ)_* pr_ρ* ⊗ μ_ρ
- **A3.8.2** Mok's degeneration formula transported into modular convolution algebra
- **A3.8.3** Rigid planted-forest types as indexing set

### A4. UNIVERSAL MODULAR CURVATURE Θ_A

#### A4.1 Graph-Sum Formula
- **A4.1.1** Θ_A = Σ_{Γ∈StGr} (1/|Aut(Γ)|) W_Γ^logFM ⊗ Φ_Γ^A
- **A4.1.2** W_Γ^logFM: chain/fundamental propagator weight from log FM stratum
- **A4.1.3** Φ_Γ^A: vertex decorations by transferred Ch∞-operations + edge contractions by cyclic pairing
- **A4.1.4** This is the modular analogue of Kontsevich's graph-sum formula

#### A4.2 Bar-Intrinsic Realization
- **A4.2.1** Θ_A = D_mod - D_tree = D - (d_int + [τ, -])
- **A4.2.2** D_mod² = 0 ⟺ dΘ_A + ½[Θ_A, Θ_A] = 0
- **A4.2.3** The positive-genus part of D_mod IS Θ_A
- **A4.2.4** Θ_A is PROVED by bar-intrinsic construction (thm:mc2-bar-intrinsic)

#### A4.3 Full L∞ MC Equation
- **A4.3.1** ℓ_1(Θ_A) + ½ℓ_2(Θ_A, Θ_A) + (1/3!)ℓ_3(Θ_A, Θ_A, Θ_A) + ... = 0
- **A4.3.2** Scalar trace: tr(Θ_A) = Σ_{g≥1} κ_g(A) λ_g
- **A4.3.3** One-parameter regime: tr(Θ_A) = Σ_{g≥1} κ(A) λ_g

#### A4.4 All-Genus Recursion
- **A4.4.1** dΘ_A^(g,n) + ½Σ ℓ_2(Θ_A^(g1,n1), Θ_A^(g2,n2)) + Δ_ns Θ_A^(g-1,n+2) + (higher) = 0
- **A4.4.2** Separating gluing: Σ_{g1+g2=g, n1+n2=n+2} ℓ_2 contribution
- **A4.4.3** Nonseparating gluing: Δ_ns Θ_A^(g-1,n+2) contribution
- **A4.4.4** Higher transferred terms from higher L∞ brackets

#### A4.5 Clutching Law (Explicit)
- **A4.5.1** Θ_A|_ρ = (κ_ρ)_*(⊗_{v∈V(S_ρ)} Θ_{A,v}) for each rigid type ρ
- **A4.5.2** κ_ρ = push-pull from Mok's degeneration FM_n(W/B)(ρ) → Π FM_{I_v}(Y_v|D_v)
- **A4.5.3** Abstract clutching slogan ξ*(Θ_A) = Θ_A ⋆ Θ_A → actual M-level formula
- **A4.5.4** Vertexwise tensoring and clutching of lower pieces on each rigid planted-forest stratum

### A5. CHARACTERISTIC SHADOW HIERARCHY

#### A5.1 Modular Chern–Weil Theory
- **A5.1.1** Θ_A = universal modular curvature
- **A5.1.2** κ(A) = first Chern class / scalar trace shadow
- **A5.1.3** Δ_A(x) = det(1 - x T_{br,A}) = determinant of linearized branch transport
- **A5.1.4** Π_A = periodicity profile
- **A5.1.5** R^mod_{4,g,n}(A) = pr_{4,g,n}(Θ_A) = quartic resonance (first nonlinear shadow)
- **A5.1.6** Higher nonlinear shadows = higher characteristic classes/cumulants

#### A5.2 Modular Tangent Complex
- **A5.2.1** T^mod_{Θ_A} := (Def∞^mod_log(A; U), d_{Θ_A})
- **A5.2.2** κ(A) = tr(Θ_A)_{2,0}
- **A5.2.3** Δ_A(t) = sdet(1 - t H(d_{Θ_A}|_red))
- **A5.2.4** R^mod_{4,g,n}(A) = pr_{4,g,n}(Θ_A)

#### A5.3 Unification Principle
- **A5.3.1** Verdier duality = cyclic pairing
- **A5.3.2** Clutching = operadic coproduct
- **A5.3.3** Genus-1 curvature = first MC coefficient
- **A5.3.4** κ(A) = first Chern number
- **A5.3.5** Δ_A = determinant class of tangent transport
- **A5.3.6** Complementarity = Lagrangian polarization of shifted-symplectic moduli
- **A5.3.7** Full Θ_A = universal modular curvature field

### A6. WEIGHT FILTRATION AND LOW-GENUS FORMULAS

#### A6.1 Weight Filtration
- **A6.1.1** Weight 0: local/internal differential only
- **A6.1.2** Weight 1: tree homotopies (∂M̄_{0,4}) + one-loop BV (∂M̄_{1,1})
- **A6.1.3** Weight 2: first genuinely logarithmic layer (rigid planted forests appear)
- **A6.1.4** "Tree homotopies and one-loop BV at weight 1; genuine logarithmic modularity begins at weight 2"

#### A6.2 Weight-1 Formulas
- **A6.2.1** Θ_A^[1]|_{(0,4)} = [δ_s]⊗Φ_s + [δ_t]⊗Φ_t + [δ_u]⊗Φ_u
- **A6.2.2** Θ_A^[1]|_{(1,1)} = [δ_irr]⊗Δ (BV loop operator)
- **A6.2.3** [D_loc, Θ_A^[1]] = 0
- **A6.2.4** [D_loc, Θ_A^[2]] + ½[Θ_A^[1], Θ_A^[1]] = 0

#### A6.3 First Taylor Coefficients (Low-Genus Control Terms)
- **A6.3.1** ℓ_3^(0)(α,β,γ): tree-level cubic from Trees_3, transferred homotopy-transfer operations
- **A6.3.2** ℓ_4^(0)(α,β,γ,δ): tree-level quartic from Trees_4
- **A6.3.3** ℓ_1^(1) = ℏΔ_cyc: reduced odd Laplacian (first genuine modular term)
- **A6.3.4** Graphwise Taylor: ℓ_Γ(f_1,...,f_k) = μ_Γ ∘ (α_Γ^mod ⊗ f's) ∘ Δ_Γ^log
- **A6.3.5** ℓ_k^(g) = Σ_Γ (1/|Aut(Γ)|) ℓ_Γ

#### A6.4 PVA Coordinate Residue Formulas
- **A6.4.1** ℓ_3^(0)(u1,u2,u3) = Σ_T Res_{D_T^log} ω^T
- **A6.4.2** ℓ_4^(0)(u1,...,u4) = Σ_F ε_F Res_{D_F^log} ω^F (contact + additive + tree rigid types)
- **A6.4.3** ℓ_1^(1) = ℏΔ_cyc in PVA coordinates
- **A6.4.4** Secondary Borcherds formula for ℓ_3^(0) (explicit mode-level)

#### A6.5 Genus-0 Transfer Operations
- **A6.5.1** m_n^ch = Σ_{Γ∈Tree_n} (1/|Aut Γ|) ∫_{FM_n(X|D)_Γ} ω_Γ(A)
- **A6.5.2** Arnold relation = first boundary cancellation in modular bar differential
- **A6.5.3** Genus-0 = seed of the whole theory

#### A6.6 Genus-1 Component
- **A6.6.1** Θ_A^(1) = Σ_{Γ: b_1(Γ)=1} (1/|Aut Γ|) ∫_{FM_Γ^log} ω_Γ(A) Γ
- **A6.6.2** Scalar trace = κ(A)λ_1 (already proved curvature class)
- **A6.6.3** Lifts known scalar curvature d_fib² = κ(A)ω_1 to chain-level one-loop MC cocycle

### A7. ARCHETYPE CLASSIFICATION

#### A7.1 Four Shadow Archetypes
- **A7.1.1** Gaussian (G): ℓ_3^(0)=0, ℓ_4^(0)=0. r_max=2. Examples: Heisenberg, free
- **A7.1.2** Lie/tree (L): ℓ_3^(0)≠0, ℓ_4^(0)=0. r_max=3. Examples: affine/current
- **A7.1.3** Contact/quartic (C): ℓ_3^(0)=0, ℓ_4^(0)≠0. r_max=4. Examples: βγ
- **A7.1.4** Mixed modular (M): ℓ_3^(0)≠0, ℓ_4^(0)≠0. r_max=∞. Examples: Virasoro, W_N

#### A7.2 Archetype Formulas (Explicit)
- **A7.2.1** Heisenberg: ℓ_3^(0)=0, ℓ_4^(0)=0, ℓ_1^(1) = ℏΣ K^ij ∂²/(∂a^i ∂a^j)
- **A7.2.2** Affine: [ℓ_3^(0)] = [f_{abc} J^a⊗J^b⊗J^c], ℓ_4^(0)=0
- **A7.2.3** W_3: Λ = :TT: - (3/10)∂²T, [ℓ_4^(0)] ∝ 16/(22+5c) Λ
- **A7.2.4** First planted-forest correction = bar-side avatar of nonlinear WW-bracket

#### A7.3 Genus-Two Shells
- **A7.3.1** Three shells: loop-loop, sep-loop, planted-forest
- **A7.3.2** Θ^(2) = Θ^(2)_{loop∘loop} + Θ^(2)_{sep∘loop} + Θ^(2)_pf
- **A7.3.3** Heisenberg → only loop-loop
- **A7.3.4** Affine → loop-loop + sep-loop
- **A7.3.5** Virasoro/W_N → all three (first point where all three geometries become inseparable)

#### A7.4 Quartic Channels
- **A7.4.1** Four primitive quartic channels: contact, 12|34, 13|24, 14|23
- **A7.4.2** Contact = local quartic vertex; others = one-edge separating

### A8. VOLUME II SPECIFIC STRUCTURES

#### A8.1 Colored Modular Deformation Object (HT)
- **A8.1.1** g_mod^{HT,log} = hom^{α_HT}(C•(FM^log_{•,SC}), End_{Ch∞}(Obs^hol_∞, Obs^∂_∞, Obs^ℓ_∞))
- **A8.1.2** Three-colored: bulk + boundary + line

#### A8.2 Modular Effective Action
- **A8.2.1** S_HT^mod = Σ_Γ (ℏ^{b_1(Γ)}/|Aut(Γ)|) W_Γ^log O_Γ
- **A8.2.2** BV QME: (d_BV + ℏΔ_odd) exp(S_HT^mod/ℏ) = 0

#### A8.3 Rigid-Type Clutching Law (HT)
- **A8.3.1** Θ^{HT,log}|_ρ = (κ_ρ)_*(⊗_v Θ^{HT,log}_v) + ∂(birational correction)

#### A8.4 Projected Modular Recursion (HT)
- **A8.4.1** ∂Θ^{HT,log,(g,n)} + Σ_sep (κ_ρ)_*(Θ⊠Θ) + Δ_ns Θ^{(g-1,n+2)} + Σ_pf ∂_ν Θ = 0

#### A8.5 Low-Order Graph Dictionary
- **A8.5.1** (0,3): codim-1 FM_3 face → first higher OPE / Jacobi correction
- **A8.5.2** (0,4)_cont: rigid 4-point contact → quartic contact vertex
- **A8.5.3** (0,4)_pf: planted-forest depth-1 → iterated cubic exchange
- **A8.5.4** (1,1)_tad: non-separating loop → one-loop odd Laplacian
- **A8.5.5** (1,2)_sep: rigid separating boundary → tree/loop clutching

#### A8.6 PVA Quantization Programme
- **A8.6.1** Filtered quadratic PVA definition
- **A8.6.2** Resolved classical datum assumption
- **A8.6.3** Genus-graded Koszul duality theorem (thm:genus-graded-koszul)
- **A8.6.4** Genus-graded Koszul complex resolution (lem:genus-graded-koszul-resolution)
- **A8.6.5** Obstruction recursion theorems (Ob1, Obg)
- **A8.6.6** Khan-Zeng 3d HT Poisson sigma model connection
- **A8.6.7** Gui-Li-Zeng quadratic duality for chiral algebras
- **A8.6.8** W_3 modular obstruction vanishing computation
- **A8.6.9** W_3 relevant shifted H¹ computation (one-loop sector)

### A9. REMAINING OPEN PROBLEMS
- **A9.1** Build cyclic L∞-enhancement of Def_cyc(A)
- **A9.2** Prove stable-graph/log-FM sum convergent in completed tensor product
- **A9.3** Verify MC equation globally (not just scalar shadow)
- **A9.4** Genus-2 stable-graph tables for Heisenberg, affine ŝl_2, Virasoro, W_N in log-FM chart
- **A9.5** Explicit propagator integrals for first nontrivial log rigid types
- **A9.6** W_3 central-parameter rigid planted-forest coefficients
- **A9.7** Push modular twisting-morphism into nonlinear shadow appendix (quartic/sextic from weight filtration)
- **A9.8** Compute genus-2/two-boundary coefficients of S_HT^mod
- **A9.9** Extract linearized transport operator T_Θ for spectral determinant in holographic sectors
- **A9.10** Produce W_3 and line-operator quartic/sextic shadow tables in log chart
- **A9.11** Rewrite holographic/celestial so higher transport factors through colored modular-convolution object

---

## Part B: RESOURCE INVENTORY

### B1. Modified TeX Files (in raeeznotes/ bundle)
| File | Size | Content |
|------|------|---------|
| higher_genus_modular_koszul.tex | 445KB | Vol I theory chapter with chain-level subsection |
| concordance.tex | 157KB | Vol I constitution with three-pillars chain-level summary |
| modular_pva_quantization.tex | 72KB | Vol II chapter: stable-graph bar, modular deformation, PVA quantization |

### B2. Python Modules (in raeeznotes/ bundle)
| File | Size | Content |
|------|------|---------|
| modular_bar.py | 4KB | Low-genus modular-bar combinatorics: Mok codim, FM_3 forests, quartic channels, genus-2 shells, archetypes |
| test_modular_bar.py | 2KB | 11 tests for modular_bar.py |

### B3. Alignment Reports (in raeeznotes/ bundle)
| File | Size | Content |
|------|------|---------|
| three_preprints_chain_level_alignment.md | 4KB | Vol I chain-level alignment memo |
| three_preprints_chain_level_alignment (1).md | 5KB | Vol II chain-level alignment memo |
| three_preprints_chain_level_alignment_report.md | 4KB | Combined alignment report with file change log |

### B4. Archive Bundle
| File | Size | Content |
|------|------|---------|
| three_preprints_endstate_pass_bundle.zip | 195KB | Combined patch bundle (not yet extracted) |

### B5. Prior Notes (context)
| File | Content |
|------|---------|
| raeeznotes91.md | Completion kinematics programme (already absorbed) |
| raeeznotes92.md | Completion kinematics continued (already absorbed) |

---

## Part C: ACTION / STRIKE LIST

### C1. STRIKE LIST — Vol I: chapters/theory/higher_genus_modular_koszul.tex

| # | Action | Section | Concept refs |
|---|--------|---------|-------------|
| C1.1 | INSERT/REWRITE: Three-preprints chain-level subsection | subsec:three-preprints-chain-level | A2.1, A3.3, A3.4, A4.1 |
| C1.2 | INSERT: Log-FM coefficient cooperad definition | new definition | A2.2 |
| C1.3 | INSERT: Modular convolution L∞-algebra definition | new definition | A2.1 |
| C1.4 | INSERT: Modular bar datum axioms + D²=0 theorem | new theorem/proof | A3.1, A3.2 |
| C1.5 | INSERT: One-edge principle + necessity proposition | new proposition | A3.6 |
| C1.6 | INSERT: Five-component differential decomposition | new construction | A3.4 |
| C1.7 | INSERT: Graphwise Taylor coefficients formula | new construction | A6.3, A6.4 |
| C1.8 | INSERT: Weight filtration with low-genus formulas | new subsection | A6.1, A6.2 |
| C1.9 | INSERT: Genus-two shell decomposition | new construction | A7.3 |
| C1.10 | STRENGTHEN: Shadow Postnikov tower as projections of bar-intrinsic Θ_A | existing section | A4.2, A5.1 |
| C1.11 | INSERT: Modular tangent complex + Chern-Weil viewpoint | new construction | A5.2 |
| C1.12 | INSERT: Planted-forest differential formula | new construction | A3.8 |
| C1.13 | STRENGTHEN: Existing archetype formulas with PVA residue expressions | existing subsections | A7.2 |

### C2. STRIKE LIST — Vol I: chapters/connections/concordance.tex

| # | Action | Section | Concept refs |
|---|--------|---------|-------------|
| C2.1 | INSERT/REWRITE: Three-pillars chain-level summary | sum:three-pillars-chain-level | A1.1-A1.3, A2.1 |
| C2.2 | UPDATE: MC2 status to reflect bar-intrinsic + log-FM chain-level presentation | MC frontier table | A4.2 |
| C2.3 | UPDATE: Three concentric rings with modular convolution L∞ as organizing structure | three-rings section | A2.4 |
| C2.4 | INSERT: Low-order graph dictionary | new summary | A8.5 |
| C2.5 | INSERT: Ontological shift remark (old vs new MC2 framing) | new remark | A2.4 |

### C3. STRIKE LIST — Vol I: Example Chapters (Part II)

| # | Action | File | Concept refs |
|---|--------|------|-------------|
| C3.1 | STRENGTHEN: Heisenberg shadow as Gaussian archetype with ℓ_3=ℓ_4=0 | heisenberg_frame.tex | A7.1.1, A7.2.1 |
| C3.2 | STRENGTHEN: Affine shadow as Lie/tree archetype with ℓ_3≠0, ℓ_4=0 | kac_moody.tex | A7.1.2, A7.2.2 |
| C3.3 | STRENGTHEN: βγ shadow as Contact/quartic archetype | beta_gamma.tex | A7.1.3 |
| C3.4 | STRENGTHEN: Virasoro/W_N as Mixed modular archetype, W_3 quartic formula | w_algebras.tex | A7.1.4, A7.2.3 |
| C3.5 | INSERT: Genus-2 shell profile for each family | all example chapters | A7.3 |

### C4. STRIKE LIST — Vol I: Other Theory Chapters

| # | Action | File | Concept refs |
|---|--------|------|-------------|
| C4.1 | STRENGTHEN: One-slot functoriality principle | chiral_koszul_pairs.tex | A1.2.2 |
| C4.2 | INSERT: Ch∞-Čech model definition | bar_cobar_adjunction_curved.tex or new section | A1.1.2 |
| C4.3 | STRENGTHEN: Modular bar as FCom-algebra with log-FM coefficients | bar_cobar_adjunction_curved.tex | A3.3 |
| C4.4 | UPDATE: Shadow depth classification with log-FM grounding | chiral_hochschild_koszul.tex | A7.1 |
| C4.5 | STRENGTHEN: Quartic resonance class as arity-4 projection of Θ_A | nonlinear_modular_shadows.tex | A5.1.5 |
| C4.6 | INSERT: Curved modular bar extension (S-tails, GLZ) | bar_cobar_adjunction_curved.tex | A3.7 |

### C5. STRIKE LIST — Vol I: Appendices

| # | Action | File | Concept refs |
|---|--------|------|-------------|
| C5.1 | INSERT: Mok codimension formula, FM_3 planted forest types | nilpotent_completion.tex or new appendix | A1.3.7-A1.3.9 |
| C5.2 | STRENGTHEN: Planted-forest stratification in computation appendix | bar_complex_tables.tex | A1.3.2 |

### C6. STRIKE LIST — Vol II

| # | Action | File | Concept refs |
|---|--------|------|-------------|
| C6.1 | ABSORB: Full modular_pva_quantization.tex chapter | new chapter or existing | A8.1-A8.6 |
| C6.2 | STRENGTHEN: Swiss-cheese algebra with log-FM coefficients | existing SC chapter | A2.2 |
| C6.3 | INSERT: Colored modular deformation object | existing connections chapter | A8.1 |
| C6.4 | INSERT: Modular effective action formula | existing or new | A8.2 |
| C6.5 | INSERT: Low-order graph dictionary | existing or new | A8.5 |
| C6.6 | STRENGTHEN: PVA descent with log-FM residue formulas | existing PVA chapter | A6.4 |
| C6.7 | INSERT: Explicit archetype formulas in boundary coordinates | existing or new | A7.2 |

### C7. STRIKE LIST — Compute Tree

| # | Action | File | Concept refs |
|---|--------|------|-------------|
| C7.1 | INSTALL: modular_bar.py into compute/lib/ | compute/lib/modular_bar.py | A1.3.7, A7.3, A7.4 |
| C7.2 | INSTALL: test_modular_bar.py into compute/tests/ | compute/tests/test_modular_bar.py | tests |
| C7.3 | RUN: Validate 11 tests pass | pytest | verification |

### C8. BIBLIOGRAPHY

| # | Action | Concept refs |
|---|--------|-------------|
| C8.1 | ADD: Malikov-Schechtman 2024 (MS24) | A1.1 |
| C8.2 | ADD/VERIFY: Robert-Nicoud–Wierstra 2019 (RNW19) | A1.2 |
| C8.3 | ADD/VERIFY: Vallette 2016 (Val16) | A1.2 |
| C8.4 | ADD/VERIFY: Mok 2025 (Mok25) | A1.3 |
| C8.5 | ADD: Khan-Zeng 2025 (KZ25) | A8.6.6 |
| C8.6 | ADD: Gui-Li-Zeng 2022 (GLZ22) | A8.6.7 |
| C8.7 | ADD: Gaiotto-Kulp-Wu 2025 (GKW25) | A8.5 |
| C8.8 | ADD: Dimofte-Niu-Py 2025 (DNP25) | A8.5 |

---

## Part D: DEPENDENCY ORDER

1. **C7.1-C7.3**: Install compute modules + run tests (zero risk, immediate)
2. **C1.1-C1.13**: higher_genus_modular_koszul.tex (the theory heart)
3. **C2.1-C2.5**: concordance.tex (constitutional update)
4. **C3.1-C3.5**: Example chapters (archetype formulas)
5. **C4.1-C4.6**: Other theory chapters (cross-references)
6. **C5.1-C5.2**: Appendices
7. **C6.1-C6.7**: Vol II strikes
8. **C8.1-C8.8**: Bibliography
9. **BUILD**: make fast (Vol I), make (Vol II), make test
