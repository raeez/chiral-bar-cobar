# Preface Interweaving Plan — Complete Catalogue and Synthesis

## Date: 2026-03-31

## The Current State

**Vol I preface** (7,625 lines at `c21fbe7`, now restored): Two movements.
- Movement I (§I–VII): Seven essay sections constructing Θ_A from first principles, through first consequences, modular homotopy type, holography, arithmetic, tautological classes, primitive kernel.
- Movement II (§1–12): Twelve technical sections: bar-cobar over a point (§1), curvature and genus tower (§2), modular homotopy theory (§3), universal MC element (§4), modular tangent complex (§5), shadow Postnikov tower (§6), standard landscape (§7), scalar saturation and Koszulness (§8), Swiss-cheese world (§9), modular PVA quantization (§10), holographic modular Koszul duality (§11), completion and frontier (§12).

**Vol II preface** (1,421 lines): Fourteen sections (I–XIV) building from two directions (C × R), through three worked examples (Heisenberg, KM, W₃), the 3d MC element α_T, Koszulness as Chriss-Ginzburg/Steinberg transversality, PVA descent from FM₃, bulk-boundary-line triangle, PVA quantization, the holographic programme (twisted holography, 3d gravity, BTZ, anomaly completion, doubling, t'Hooft, arithmetic face), and the fourteen theorems.

---

## I. THE COMPLETE CATALOGUE

Every idea, motif, calculation, and perspective relevant to the programme, organized by mathematical domain. Items marked [V1], [V2], or [V1+V2] indicate where the material primarily lives or should live.

### A. FOUNDATIONAL CONSTRUCTIONS

#### A1. The logarithmic seed η = d log(z₁ - z₂) [V1]
- Simple pole with residue 1, conformally invariant
- Arnold relation from partial fractions / commutativity of addition
- Bar differential as residue extraction: d_B[s⁻¹a | s⁻¹b] = Res_{z₁=z₂}[a(z₁)b(z₂)·η₁₂]
- Propagator as BRST ghost for diffeomorphisms (cocycle for Diff(X))

#### A2. The operadic hierarchy: algebras → operads → modular operads [V1]
- Bar construction of augmented algebra: B(A) = (Tᶜ(s⁻¹Ā), d_B), sums over sequences
- Operadic bar construction: sums over trees with det-line twists, d² = 0 is codimension-2 cancellation on associahedron
- Koszul duality: Com! = Lie (Ginzburg-Kapranov)
- Modular operads (Getzler-Kapranov): operations indexed by stable graphs of arbitrary genus
- Feynman transform: FO(g,n) = ⊕_Γ ℏ^{g(Γ)}/|Aut(Γ)| ⊗_v O(g(v),In(v)) ⊗ det(E(Γ))
- Differential = edge contraction; d² = 0 is codimension-2 boundary cancellation on moduli space
- FCom = stable graph complex (vertex factors one-dimensional)
- FAss = ribbon graph complex (cyclic ordering at each vertex) = algebraic t'Hooft 1/N expansion

#### A3. The convolution architecture (Chriss-Ginzburg principle) [V1]
- Three-level convolution ladder:
  - Algebra: Hom(B(Ass), End_A) → A∞-structures
  - Operad: Hom_Σ(B(P), End_V) → P∞-structures
  - Modular: Hom_Σ(FO, End_{B(A)}) → consistent genus towers
- g^mod_A := Hom_Σ(FCom, End_{B(A)}) is the ambient home of Θ_A
- Steinberg analogy: bar complex plays the role of Steinberg variety; Θ_A plays the role of fundamental class

#### A4. The graph-sum formula and bar-intrinsic construction [V1]
- Modular bar construction: B^{(g)}_X(A) = ⊕_Γ |Aut(Γ)|⁻¹ W_Γ ⊗ ⊗_v Φ^A_v
- Universal MC element: Θ_A = Σ_Γ |Aut(Γ)|⁻¹ W_Γ ⊗ Φ^A_Γ ∈ MC(g^mod_A)
- Bar-intrinsic construction: Θ_A := D_A - d_0; MC because D_A² = 0
- D_A² = 0 at convolution level from ∂² = 0 on M̄_{g,n}
- D_A² = 0 at ambient level via Mok's log FM normal-crossings [Mok25]
- Planted forests = Trop(FM_n(C|D))
- All-arity convergence Θ_A = varprojlim Θ_A^{≤r} (thm:recursive-existence)
- Every theorem of the monograph is a projection of Θ_A

#### A5. Scalar saturation [V1]
- H²_cyc(g,g) = H³(g) = C (one-dimensional for simple g)
- Cubic Casimir in H⁵(g) — degree 5 in cyclic cohomology vs MC at degree 2: degrees don't meet
- Θ_A^min = κ(A)·η⊗Λ: one number, one kernel, one class
- Proved for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity)

### B. THE FIVE THEOREMS AND THEIR PROJECTIONS

#### B1. Theorem A: Bar-cobar adjunction and Verdier intertwining [V1]
- B_X and Ω_X form adjunction on Ran(X)
- D_Ran ∘ B ≃ B ∘ (-)!

#### B2. Theorem B: Bar-cobar inversion [V1]
- Ω(B(A)) →∼ A on Koszul locus
- PBW spectral sequence degeneration at E₂

#### B3. Theorem C: Complementarity [V1]
- Q_g(A) ⊕ Q_g(A!) ≅ H*(M̄_g, Z_A)
- Shifted-symplectic Lagrangian geometry upgrade
- Central charge complementarity: c(Ĝ_k) + c(Ĝ_{-k-2h∨}) = 2 dim(g)

#### B4. Theorem D: Modular characteristic [V1]
- κ(A) universal, additive, duality-constrained
- Generating function: Σ F_g ℏ^{2g-2} = κ(A)·(Â(iℏ) - 1)
- Â(ix) = (x/2)/sin(x/2) has all positive coefficients
- Each F_g positive (Bernoulli signs)

#### B5. Theorem H: Chiral Hochschild [V1]
- ChirHoch*(A) polynomial on Koszul locus, Koszul-functorial

### C. CURVATURE, GENUS TOWER, AND THE THREE DIFFERENTIALS

#### C1. Three differentials [V1]
- d₀: genus-0 collision, d₀² = 0 by Arnold
- d_fib: fiberwise on Σ_g, d_fib² = κ·ω_g ≠ 0
- D_g: total corrected, D_g² = 0 (Lagrangian splitting via A-cycles)

#### C2. Curved A∞ framework [V1]
- m₀ = κ·ω_g, m₁²(a) = [m₀,a]
- κ = 0 ⟺ d_fib² = 0 ⟺ anomaly cancellation ⟺ c = 26 (for bosonic string)

#### C3. The two-pole obstruction [V1]
- d_br² = -{d_br, d_lev} (verified across all 2048 sign conventions)
- Total d squares to zero by Borcherds identity = Stokes on FM compactification

### D. THE SHADOW POSTNIKOV TOWER

#### D1. Tower structure [V1]
- Θ_A^{≤r} projects Θ_A to arity ≤ r
- r = 2: curvature κ(A); r = 3: cubic shadow C(A); r = 4: quartic resonance Q(A)
- Four depth classes: G (Gaussian, r_max=2), L (Lie/tree, r_max=3), C (contact, r_max=4), M (mixed, r_max=∞)
- Single-line dichotomy: r_max ∈ {2,3,∞} on 1D primary slice

#### D2. Shadow metric [V1]
- Q_L(t) = (2κ + 3αt)² + 2Δt², Δ = 8κS₄
- Logarithmic connection ∇^sh with residue 1/2, monodromy -1 (Koszul sign)
- Δ = 0 ↔ finite tower; Δ ≠ 0 ↔ infinite tower
- Discriminant complementarity: Δ(A) + Δ(A!) = 6960/[(5c+22)(152-5c)]
- Self-dual at c = 13

#### D3. Shadow growth rate [V1]
- ρ(A) = √(9α²+2Δ)/(2|κ|), continuous invariant on class M
- S_r ~ A·ρ^r·r^{-5/2}·cos(rθ+φ)
- Critical cubic 5c³+22c²-180c-872=0, c*≈6.125
- Shadow partition function Z^sh converges absolutely (genus + arity)

#### D4. Explicit shadow tower computations [V1]
- Virasoro S₂ = c/2, S₃ = 2, S₄ = 10/[c(5c+22)], S₅ = -48/[c²(5c+22)]
- S₆ = 80(45c+193)/[3c³(5c+22)²], S₇ = -2880(15c+61)/[7c⁴(5c+22)²]
- Denominator theorem: denom(S_r) = const·c^{r-3}(5c+22)^{⌊(r-2)/2⌋}
- Q^contact_Vir = 10/[c(5c+22)] — poles at Gram determinant zeros

#### D5. The weight-4 Gram matrix [V1]
- G = ((5c, 3c), (3c, c(c+8)/2)), det G = c²(5c+22)/2
- Quasi-primary |Λ⟩ = L₋₂²|0⟩ - (3/5)L₋₄|0⟩, norm c(5c+22)/10
- W₄ structure constant c₃₃₄² = 42c²(5c+22)/[(c+24)(7c+68)(3c+46)]
- Shadow tower poles = representation theory zeros

### E. THE MODULAR HOMOTOPY TYPE

#### E1. Modular convolution algebra [V1]
- g^mod_A = Hom_Σ(FCom, End_{B(A)}): dg Lie algebra, strict model of underlying modular L∞
- MC moduli coincide; full L∞ needed for transfer, formality, gauge equivalence

#### E2. Homotopy types in three stages [V1]
- Stage 1 (over a point): A∞-structure, formality = all m_k = 0 for k ≥ 3
- Stage 2 (over C): chiral operations, Koszul duality
- Stage 3 (over a curve): modular L∞ brackets ℓ_k^{(g)}, formality → Gaussian archetype

#### E3. Completion [V1]
- Strong completion-tower theorem (thm:completed-bar-cobar-strong)
- MC4 splitting: MC4⁺ (positive, solved by stabilization) vs MC4⁰ (resonant, finite resonance)
- Resonance rank ρ(A) classifies completion difficulty

### F. THE SWISS-CHEESE WORLD

#### F1. Two directions: C × R [V2]
- Holomorphic direction → OPE residue → bar differential D_A
- Topological direction → cut R → deconcatenation coproduct Δ
- Coderivation property: Δ ∘ D_A = (D_A ⊗ id + id ⊗ D_A) ∘ Δ
- Bar element parametrized by FM_k(C) × Conf_k^<(R)

#### F2. The Swiss-cheese operad SC^{ch,top} [V2]
- Closed: FM_k(C); Open: E₁(m); Mixed: FM_k(C) × E₁(m); Open→Closed: ∅
- Directionality = Springer pattern: G → B only
- Bar complex = SC^{ch,top}-coalgebra (NOT algebra)
- Koszul self-duality: (SC^{ch,top})! ≃ SC^{ch,top}

#### F3. Homotopy-Koszulity [V2]
- Classical SC is Koszul (Livernet)
- Kontsevich formality: C*(FM_k(C)) ≃ H*(FM_k(C)) ≅ E₂(k) (Gerstenhaber)
- Bar-cobar resolution: ΩB(SC^{ch,top}) →∼ SC^{ch,top}
- Quillen equivalence on SC^{ch,top}-algebras

#### F4. The A∞ chiral operations [V2]
- m_k: A^⊗k → A((λ₁))···((λ_{k-1})), deg m_k = 2-k
- D_A² = 0 ↔ Stasheff relations; each relation = Stokes on FM_n(C)
- n=1: m₁² = 0 (BRST); n=2: Leibniz; n=3: homotopy-associativity (associahedron K₃ = interval)
- n=4: pentagon K₄ (five faces), m₄ for W₃ has coefficient 32/(22+5c)

#### F5. The resolvent principle [V2]
- Dressed propagator Φ = ι + h ∘ m₂ ∘ Φ^⊗2 (tree-level bootstrap)
- Tree formula: m_k^H = Σ_{T ∈ PRT_k} p ∘ m(T) ∘ ι^⊗k, |PRT_k| = C_{k-1}
- One equation, one binary input, Catalan-many trees

#### F6. Lagrangian self-intersection [V1+V2]
- Bar complex = formal model of L ×_M^h L in (-2)-shifted symplectic stack
- Holomorphic = Koszul differential of Lagrangian embedding
- Topological = groupoid diagonal
- HKR recovers T*[-1]L_A from boundary; ambient requires Darboux 1-form

### G. THE 3D MC ELEMENT AND PROJECTIONS

#### G1. The 3d MC element α_T [V2]
- α_T ∈ MC(g^SC_T), where g^SC_T = Hom_Σ(B(SC^{ch,top}), End_{(B_∂, C_line)})
- Exists because SC^{ch,top} is homotopy-Koszul
- Formula: α_T = Σ_Γ |Aut(Γ)|⁻¹ W_Γ ⊗ Φ^T_Γ

#### G2. Six projections of α_T [V2]
- Closed face → boundary A∞ algebra B_∂
- Open face → line category B_∂!-mod
- Arity-(2,0) Laplace → spectral R-matrix, YBE
- Arity-(1,1) mixed → A_bulk ≃ Z_der(B_∂)
- Closed genus expansion → Θ_A (Vol I)
- Closed cohomology → PVA {-_λ-}

#### G3. Colour decomposition [V2]
- α_T = α_T^cl + α_T^mix + α_T^op
- Pure closed: Vol I MC equation
- Mixed: r-matrix and PVA bracket are Θ_A-twisted cocycles
- Pure open: full open MC equation

### H. THREE WORKED EXAMPLES AT FULL DEPTH

#### H1. Heisenberg H_k [V1+V2]
- m₁ = 0, m₂(J,J;λ) = kλ, m_k = 0 for k ≥ 3 (formal)
- PVA: {J_λ J} = kλ; r(z) = k/z²; R(z) = exp(kℏ/z)
- Lines: Fock spaces F_μ (semisimple); R_{μ₁,μ₂}(z) = exp(kμ₁μ₂ℏ/z)
- Bulk = Z_der(H_k) = H_k (abelian = own derived centre)
- κ = k; F₁ = -(k/24)log η(τ)
- Bar cohomology: partitions p(n-2): 1,1,1,2,3,5,7,11,...
- H_k! = Sym^ch(V*) ≠ H_{-k}
- α_{H_k} = m₂ + ℏk·η⊗Λ

#### H2. Kac-Moody Ĝ_k [V1+V2]
- m₂(J^a,J^b;λ) = f^{ab}_c J^c + kδ^{ab}λ; m₃ ≠ 0 (Jacobiator); m_k = 0 for k ≥ 4
- PVA: {J^a_λ J^b} = f^{ab}_c J^c + kδ^{ab}λ
- r(z) = Ω/z (Casimir); KZ connection ∇ = d - ℏΩ/z; monodromy = R-matrix of U_ℏ(g)
- Koszul dual A!_ch = Ĝ_{-k-2h∨} (Feigin-Frenkel); FF involution is Verdier duality
- dg-shifted Yangian Y^dg(g) governs line category; lines = cat O at dual level
- DK duality: braided module category = quantum group category
- κ = dim(g)·(k+h∨)/(2h∨); anti-symmetry κ_k + κ_{-k-2h∨} = 0
- Critical level k = -h∨: Sugawara undefined, κ = 0, H⁰(B(Ĝ_{-h∨})) = Fun(Op_{g∨}(D))
- Bar cohomology: 3,5,15,36,91,232,... (modified Riordan); H²(B(ŝl₂)) = 5 not 6
- Jones polynomial from bar complex (cor:jones-polynomial)

#### H3. W₃ and the birth of nonlinearity [V1+V2]
- Two generators T (weight 2), W (weight 3); WW OPE up to order 6
- Composite field Λ = :(TT): - (3/10)∂²T, coefficient 16/(22+5c)
- m₃ ≠ 0 (Jacobiator with Λ); m₄ ≠ 0 (quartic from FM₄, coefficient 32/(22+5c))
- A∞ structure does NOT terminate
- Cumulant coalgebra: new cogenerator Λ* with non-primitive coproduct
- G_{W₃}(t) = (t+t²+t³)/(1-t); h_K ≈ 0.772
- dg-shifted Yangian non-abelian; genuine matrix R-matrix

### I. PVA DESCENT AND YANG-BAXTER

#### I1. PVA from cohomology [V2]
- Higher m_k vanish on cohomology (contractibility of Conf_k^<(R))
- m₂ decomposes: regular part → commutative product μ; singular part → λ-bracket via Borel transform
- (μ, {-_λ-}) form (-1)-shifted PVA on H•(A,Q)

#### I2. Jacobi from FM₃ [V2]
- Three strata D₁₂, D₂₃, D₁₃ of ∂FM₃(C)
- Stokes on FM₃ → {a_λ{b_μ c}} - {b_μ{a_λ c}} = {{a_λ b}_{λ+μ} c}
- Leibniz from factorization of regular part through collision stratum
- Skew-symmetry from exchange automorphism z₁ ↔ z₂

#### I3. YBE as open-colour projection [V2]
- Three parallel lines at z₁,z₂,z₃ braided in two orders
- YBE = cancellation of integral over ∂FM₃(C)
- Jacobi = closed projection; YBE = open projection; both = Stasheff at n=3

### J. BULK-BOUNDARY-LINE TRIANGLE

#### J1. The corrected triangle [V2]
- A_bulk ≃ Z_der(B_∂) ≃ Z_der(C_line) ≃ HH•_ch(A!)
- C_line ≃ A!-mod
- Derived centre Z_der(B_∂) := RHom_{B_∂-B_∂}(B_∂,B_∂)

#### J2. Examples [V2]
- Heisenberg: Z_der(H_k) = H_k (abelian = own centre)
- KM at critical: Z_der(Ĝ_{-h∨}) = Feigin-Frenkel centre = algebra of opers

### K. KOSZULNESS AS TRANSVERSALITY

#### K1. Chriss-Ginzburg/Steinberg parallel [V1+V2]
- Steinberg: H*^BM(Ñ ×_g Ñ) ≅ H_W
- Bar complex on FM_k × Conf_k^< = chiral convolution algebra
- Koszulness = concentration = transversality of Lagrangian self-intersection
- Non-concentration ↔ excess Tor ≠ 0 ↔ higher derived structure
- Full dictionary: Springer↔Lagrangian, KL basis↔MC element, KL polynomials↔shadow tower, Hecke eigenvalues↔R-matrix

#### K2. Koszulness programme [V1]
- Meta-theorem: 12 characterizations, 10 unconditional + 1 conditional + 1 one-directional
- Shadow depth classifies COMPLEXITY, not Koszulness itself
- V_k(g) Koszul for all k; L_k(g) may fail at admissible levels

### L. HOLOGRAPHIC PROGRAMME AND QUANTUM GRAVITY

#### L1. Holographic modular Koszul datum [V1+V2]
- H(T) = (A, A!, C, r(z), Θ_A, ∇^hol) — six projections of α_T
- Completed platonic datum Π^oc_X(A) — eight-fold

#### L2. Twisted holography [V2]
- 3d N=2 gauge theory on R₊ × C, CS level k
- Boundary = chiral algebra B_∂; Bulk = Z_der(B_∂); Lines = B_∂!-mod
- Spectral R-matrix = quantum group R-matrix at q = e^{iπ/(k+h∨)}

#### L3. 3d gravity as SL(2,R) CS [V2]
- A_± = ω ± e/ℓ; S_grav = S_CS[A₊;k₊] - S_CS[A₋;k₋]
- B_∂ = Vir_c with c = 6k = 3ℓ/(2G) (Brown-Henneaux)
- B_∂! = Vir_{26-c}; self-duality at c = 13, NOT c = 26
- c = 26: dual curvature vanishes; gravity becomes topological
- R-matrix = Virasoro fusion kernel = 6j-symbol; YBE = pentagon identity = graviton scattering
- Shadow tower = perturbative quantum gravity; quartic contact = four-graviton interaction
- h_K(Vir) ≈ 0.567 = kinematic growth rate of gravitational corrections

#### L4. MC replaces sum over topologies [V2]
- Genus-g MC equation: d^tree Θ^(g) = -Σ[Θ^(g₁),Θ^(g₂)] - Θ^(g-1)_clutch
- On Koszul locus: unique solution, no free parameters at any genus
- Maloney-Witten negative coefficients: MC replaces, does not repair

#### L5. Anomaly completion [V2]
- Transgression algebra B_Θ with η, dη = Θ, secondary anomaly u = η²
- u ≠ 0: Clifford Morita equivalence to genus 0
- u = 0 (c = 26): exterior-algebra extension, topological gravity
- c = 13 (symmetry) vs c = 26 (bifurcation): separated by 13 units

#### L6. BTZ black holes as MC deformations [V2]
- BTZ = MC deformation of vacuum α_T
- Linearized equation = Klein-Gordon on BTZ background
- Cardy formula = asymptotic density of MC deformations

### M. ARITHMETIC PROGRAMME

#### M1. Dirichlet-sewing lift [V1]
- S_A(u) = Σ a_A(N) N^{-u} from sewing kernel
- Three-tier Euler-Koszul classification:
  - Tier I (Euler): D_A = 0 (Heisenberg, lattice)
  - Tier II (finite): D_A rational (βγ, affine)
  - Tier III (arithmetic): D_A involves ζ-zeros (Virasoro, W_N)
- S_Vir(u) = ζ(u+1)(ζ(u)-1); defect D_Vir(u) = 1 - 1/ζ(u)
- Total depth d = 1 + d_arith + d_alg; depths ≥ 5 purely arithmetic (cusp forms)

#### M2. Shadow-moduli resolution [V1]
- MC equation projected to Newton power sums = MC bracket
- Operadic Rankin-Selberg conjecture: arity-r moments = symmetric-power L-functions
- Hecke-Newton closure for lattice VOAs → unconditional Ramanujan bounds

#### M3. Arithmetic packet connection [V1]
- ∇^arith_A flat, with unipotent monodromy from algebraic defect
- Principle: arithmetic is semisimple; homotopy defect is unipotent
- Miura splitting for W_N; frontier defect form Ω_A

#### M4. Interacting Gram matrix [V1]
- Gram positivity, Nyman-Beurling, Li criterion
- Weil analogy dictionary

#### M5. Constrained Epstein zeta [from raeeznotes111-112]
- ε^c_s(V_Λ) literally is Riemann zeta for V_Z: ε¹_s(R=1) = 4ζ(2s)
- Hecke decomposition: ε^r_s = linear combination of L-functions
- Shadow depth d gives d-1 critical lines
- Zeta zeros = scattering resonances of Laplacian on M_{1,1}

### N. TAUTOLOGICAL CLASSES AND TOPOLOGICAL RECURSION

#### N1. Shadow CohFT [V1]
- MC tautological descent: Θ_A → R*(M̄_{g,n})
- WDVV from MC (arity 3); Mumford from MC (genus 1)
- Givental R-matrix = complementarity propagator
- Eynard-Orantin topological recursion = MC shadow

#### N2. Primitive kernel and cofree reduction [V1]
- K_A: kernel of bar comultiplication at each genus
- (Q^mod)² = 0 iff dK + K⋆K = 0 (MC on K_A = shell equation)
- Branch BV action S^br with metaplectic half-density δ² = Δ

### O. THE FACTORIZATION-PRIMARY HIERARCHY (from specs)

#### O1. The six-layer framework [V2, new]
- Layer 0: geometric substrate (curves, Ran space, M̄_{g,n})
- Layer 1: factorizable D-modules (BD structure)
- Layer 2: HT product geometry (Σ_g × R)
- Layer 3: bar complex as factorization coalgebra
- Layer 4: Koszul duality as factorization duality
- Layer 5: three models as three gauges (flat/corrected/curved)
- Layer 6: local shadow (SC^{ch,top} = formal completion)

#### O2. Local vs global tension [V2, new]
- SC^{ch,top} sees: collision data, Arnold/Fay, A!, directionality, formal-disc propagator
- SC^{ch,top} misses: D-module monodromy, period corrections, Arakelov propagator, curvature κ·ω_g
- Corrected holomorphic D^(g)² = 0: visible to local operad (Fay is local)
- Curved d_fib² = κ·ω_g: invisible to local operad (global D-module data)

#### O3. Three routes unified [V2, new]
- Route B (factorization): global truth — factorization on Ran(Σ_g) × Ran(R) over M̄_g
- Route A (operadic): local approximation — SC^{ch,top}_mod at formal completions
- Route C (relative FT): algebraic skeleton — FT_{Com_mod/SC^{ch,top}} as common abstraction
- Derived-coderived equivalence requires: modular homotopy-Koszulity + factorization Koszulity + chiral RH correspondence

### P. PVA QUANTIZATION AND THE HALF-SPACE BV

#### P1. Quantization problem [V2]
- Given PVA, construct A∞ chiral algebra recovering it on cohomology
- Obstruction in HH³_ch(V); Khan-Zeng 3d sigma model gives physical proof

#### P2. Doubling principle [V2]
- Embed half-space in double via method of images
- σ(z,t) = (z̄,-t); reflected propagator
- Four types of boundary strata = σ-orbits of FM strata
- Chain: logarithmic SC-algebra → reflected weight identity → boundary VA

#### P3. DS transport [V2]
- DS preserves SC^{ch,top} structure
- Virasoro and W_N enter via affine bridge + DS transport
- Non-principal: hook-type in type A proved; general conjectural

### Q. ENTANGLEMENT, ERROR CORRECTION, HOLOGRAPHIC CODES

#### Q1. RT from proved core [V1]
- S_EE = (c/3)log(L/ε) from κ
- Complementarity sum 26/3
- Four-class entanglement complexity (G/L/C/M)

#### Q2. Koszulness = exact QEC [V1]
- Knill-Laflamme from Lagrangian isotropy
- Shadow depth = redundancy channels
- 12-fold K1-K12 code dictionary

### R. ADMISSIBLE LEVELS AND LOGARITHMIC CFT (from raeeznotes109)

#### R1. Periodic CDG structure [V1+V2, frontier]
- At admissible k = -h∨ + p/q: bar complex acquires periodic CDG indexed by q-th roots of unity
- Door to logarithmic CFT
- Three-layer separation: twisting data / bulk operators / global modular geometry

### S. THE POLYAKOV PROGRAMME

#### S1. Polyakov-bar-cobar dictionary [V1]
- Polyakov effective action from shadow tower
- Functional-integral origin
- BPZ-Koszul S-duality; instanton bridge
- Ghost-Koszul identification; anomaly ratio table

---

## II. THE INTERWEAVING PLAN

### Principle

The two prefaces serve complementary architectural functions:
- **Vol I preface**: constructs the algebraic engine — from η₁₂ through operads, modular operads, Feynman transforms, to Θ_A — then unfolds its consequences through the standard landscape, shadow tower, arithmetic, tautological classes, and into the Swiss-cheese world and holographic programme. It IS the Chriss-Ginzburg-style constructive development: definitions → constructions → computations → landscape → frontier.
- **Vol II preface**: constructs the 3d extension — from C × R through FM_k(C) × Conf_k^<(R), three worked examples, α_T with six projections — then unfolds into Koszulness-as-transversality, PVA descent, bulk-boundary-line, quantization, holography, and gravity. Same style: definitions → constructions → computations → landscape → frontier.

### What's Missing / Needs Strengthening

#### In Vol I preface:

1. **The factorization-primary hierarchy (O1-O3)** — currently absent from Vol I preface. The six-layer framework belongs in §3 (modular homotopy theory) or as a dedicated section between §3 and §4. The local/global tension should be stated when the three differentials appear.

2. **The Polyakov programme (S1)** — currently absent from the Vol I preface. The Polyakov-bar-cobar dictionary, functional-integral origin, anomaly ratio table deserve a dedicated subsection within §V (arithmetic) or as §V-bis.

3. **Entanglement and holographic codes (Q1-Q2)** — currently absent. S_EE = (c/3)log(L/ε) from κ is a theorem that belongs in the first consequences (Movement I, §II or as a new §II-bis) or in the holography section (§IV).

4. **Admissible levels / logarithmic CFT (R1)** — the periodic CDG structure at admissible levels is frontier material that should be mentioned in §12 (completion and the frontier).

5. **The constrained Epstein zeta and zeta-zero connection (M5)** — the identification ε¹_s(R=1) = 4ζ(2s) is a concrete result that should appear in §V (arithmetic), alongside the Hecke decomposition and the observation that zeta zeros = scattering resonances.

6. **MC replaces sum over topologies (L4)** — this is stated in Vol II but is equally a Vol I result (it follows from the MC recursion of Θ_A). Should appear in Movement I §IV (holography) or Movement II §11.

7. **The Gram matrix and quartic contact (D5)** should be more prominent in Movement I (currently only in Movement II §7.3–§7.4).

#### In Vol II preface:

1. **The factorization-primary hierarchy (O1-O3)** — the specs demand this but the current Vol II preface is entirely operadic. The six-layer framework needs to be woven into §XIII (holographic programme), specifically in the subsection on the modular bar complex as genus expansion (lines 1360-1374) where the local/global tension is already mentioned.

2. **The relative Feynman transform (O3, Route C)** — currently absent from Vol II preface. The recognition B_mod = FT_{Com_mod/SC^{ch,top}} and involutivity belong after §XIII.

3. **The arithmetic face is anemic** (lines 1406-1408, only 3 lines). Vol I has a rich §V on arithmetic with 10 subsections. The Vol II preface should have at least a paragraph on the Dirichlet-sewing lift and the three-tier classification.

4. **The constrained Epstein zeta connection** should be mentioned as a frontier direction.

### The Synthesis

**Vol I preface interweaving targets** (additions to the restored 7,625-line version):

| Target | Location | Content | Category |
|--------|----------|---------|----------|
| Factorization primacy remark | §I.3 "From a point to a curve" | After introducing the three differentials, add a remark: factorization on Ran(Σ_g) is the global truth; the local operad sees the corrected holomorphic model but not the curvature | O2 |
| Entanglement from κ | §II "First consequences", after shadow growth rate | New subsection: S_EE = (c/3)log(L/ε), complementarity sum, 4-class entanglement complexity | Q1 |
| Polyakov programme | §V "Arithmetic", after shadow-moduli resolution | New subsection: Polyakov-bar-cobar dictionary, functional-integral origin | S1 |
| Constrained Epstein zeta | §V "Arithmetic", after Weil analogy | New subsection: ε^c_s(V_Λ) = 4ζ(2s) for V_Z; zeta zeros as scattering resonances | M5 |
| MC replaces topologies | §IV "Holography" or §11 | The genus-g MC recursion determines Z_g uniquely; no sum over topologies needed | L4 |
| Admissible/logarithmic | §12.5 "The boxed machine" | At admissible k = -h∨ + p/q: periodic CDG structure, door to logarithmic CFT | R1 |
| Gram matrix promotion | §I.4 "Virasoro shadow tower" | Move the Gram matrix / quartic contact computation to Movement I for prominence | D5 |

**Vol II preface interweaving targets** (additions to the existing 1,421-line version):

| Target | Location | Content | Category |
|--------|----------|---------|----------|
| Factorization primacy | §XIII, modular bar subsection | Expand 3-line mention to a paragraph: six-layer hierarchy, local = operadic, global = factorization, curvature is the gap; three models as three gauges | O1-O2 |
| Relative FT recognition | New subsection after §XIII arithmetic face | B_mod = FT_{Com_mod/SC^{ch,top}}; involutivity; the three routes unified | O3 |
| Arithmetic expansion | §XIII arithmetic face | Expand from 3 lines to paragraph: Dirichlet-sewing lift, three-tier classification, Virasoro defect at zeta zeros, shadow-moduli resolution | M1-M2 |
| Constrained Epstein | §XIII arithmetic face | Mention ε¹_s(R=1) = 4ζ(2s) as concrete bridge between chiral algebras and number theory | M5 |

---

## III. ARCHITECTURAL PRINCIPLES

### The Chriss-Ginzburg style applied to both prefaces

1. **Open with a construction, not a description.** Vol I opens with η₁₂ and immediately builds the bar complex. Vol II opens with two operators on C × R and immediately computes the coderivation property. Both correct.

2. **Derive every structural fact from a computation.** Vol II achieves this (Jacobi from FM₃, YBE from FM₃, PVA from contractibility of Conf_k). Vol I achieves this in Movement II (§1-§12) but Movement I (§I-§VII) sometimes narrates rather than constructs. Movement I should be strengthened where possible.

3. **Let deep connections emerge from the mathematics.** The key synthesis: Jacobi = YBE = Stasheff = Stokes = Steinberg = complementarity = shadow = Koszul sign. Both prefaces achieve this.

4. **Three worked examples at full depth.** Vol II: Heisenberg → KM → W₃, each revealing a new layer. Vol I: the standard landscape (§7) covers Heisenberg, affine, Virasoro, W₃, βγ, lattice, Yangians — but less depth per example in Movement I. The strength of Vol I is that Movement II does give depth.

5. **The monograph computes the local geometry at a point.** Vol II's closing line: "A chiral algebra is a point in the derived symplectic category... The entire content of both volumes is the local geometry of the derived symplectic category at this single point." This should be echoed in Vol I's closing, perhaps as the final sentence of §12.5.

### What makes the two prefaces a unified whole

The two prefaces tell the same story from two perspectives:
- **Vol I**: One 1-form → one relation → one extraction of residues → one MC element → the entire nonlinear modular structure. The construction goes inward: from geometry to algebra to arithmetic.
- **Vol II**: Two directions (C and R) → one product space FM_k(C) × Conf_k^<(R) → one MC element α_T → six projections → the entire holographic system. The construction goes outward: from algebra to geometry to physics.

The pivot between the two is the Swiss-cheese operad: Vol I arrives at it (§9) after building the algebraic engine; Vol II starts from it (§III) and unfolds the 3d world.

The interweaving ensures that both prefaces:
- State the factorization-primary hierarchy
- Touch the arithmetic programme
- Name the entanglement programme
- Reference the frontier (logarithmic CFT, non-principal W-duality, completion)
- Close with the same geometric vision: everything is the local geometry of one point in the derived symplectic category
