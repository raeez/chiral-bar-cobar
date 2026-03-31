# Linear Read Audit — Vol I: Modular Koszul Duality
# Started: 2026-03-25
# Method: Page-by-page, linear, 6-examiner adversarial panel
# Examiners: Beilinson, Witten, Costello, Gaiotto, Drinfeld, Kontsevich

---

## FINDINGS REGISTER

### Pages 1-4 (Abstract)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F1 | p.3 | **CRITICAL** | Gaiotto | κ(W_N) formula WRONG: (N³-N)k/(k+N) → c·(H_N-1). Also CLAUDE.md had c·H_N → c·(H_N-1). | **FIXED** |
| F2 | p.2 | SERIOUS | Beilinson | CG formula "(all n)" → "(type A, generic parameters)". | **FIXED** |
| F3 | p.1 | SERIOUS | Witten | "Recovers Fourier-Mukai kernel" → "genus expansion controlled by Eisenstein series". | **FIXED** |
| F4 | p.1-2 | ~~SERIOUS~~ | Witten | ~~Modular invariance of F_g never verified.~~ Transformation laws ARE recorded (prop:eisenstein-modular). F_g coefficients are modular forms by construction. | **CLOSED** |
| F5 | p.2 | ~~MODERATE~~ | Costello | ~~6-component decomposition vs 3-5.~~ All 6 components named, defined, and described in preface §3.6 and main.tex lines 714-727. | **CLOSED** |
| F6 | p.2 | ~~MODERATE~~ | Drinfeld | ~~def:modular-yangian-pro missing.~~ EXISTS at yangians_drinfeld_kohno.tex:5577. | **CLOSED** |
| F7 | p.3 | ~~MODERATE~~ | Kontsevich | ~~"Postnikov" terminologically incorrect.~~ Metaphorical, well-documented (def:shadow-postnikov-tower line 10109); identification with L∞ obstructions proved at low arity. Standard usage. | **CLOSED** |
| F8 | p.3 | ~~MODERATE~~ | Kontsevich | ~~A∞/L∞ conflation.~~ Meta-theorem item (iii) precisely says "A∞-model of B̄(A) formal: m_n=0 for n≥3." This IS A∞-formality. Shadow-formality (prop:shadow-formality-low-arity) is a separate identification. No conflation in formal statements. | **CLOSED** |
| F9 | p.2 | ~~MODERATE~~ | Kontsevich | ~~"Forces" presented as one-way.~~ Standard mathematical usage for "is the mechanism ensuring." | **CLOSED** |
| F10 | p.2 | ~~MODERATE~~ | Costello | ~~Verdier-Quillen without proof.~~ Correctly styled as \begin{remark}, not a theorem. Standard practice. | **CLOSED** |
| F11 | p.3 | ~~MODERATE~~ | Drinfeld | ~~"Arnold implies CYBE" misleading.~~ Text says MC equation "reduces to" CYBE at genus 0. Correctly framed as genus reduction. | **CLOSED** |
| F12 | p.4 | ~~MODERATE~~ | Witten | ~~Physical meaning of α, Δ never explained.~~ Defined formally at def:shadow-metric (line 12972/12988). Physical roles explained in body chapters. Not expected in abstract. | **CLOSED** |
| F13 | p.4 | ~~MODERATE~~ | Witten | ~~Holographic datum overclaim.~~ Frontier section uses programme language ("governs", "recognition theorem identifies"). Appropriately cautious. | **CLOSED** |
| F14 | p.4 | ~~MINOR~~ | Witten | ~~HS-sewing Moriwaki dependency.~~ General HS-sewing (thm:general-hs-sewing) is self-contained. Only Heisenberg envelope clause (i) depends on Moriwaki; text separates these explicitly. | **CLOSED** |
| F15 | p.2 | ~~MINOR~~ | Kontsevich | ~~FCom homotopy upgrade only cited.~~ Theorem thm:bar-modular-operad is ProvedHere with full proof. GK98 cited only for FCom definition. Standard practice. | **CLOSED** |

### Pages 106-110 (Preface §7: standard landscape — Heisenberg, KM, W₃, βγ families)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F63 | p.108 | **SERIOUS** | Gaiotto | W₃ WW OPE coefficient 16/(22+5c) at line 5054, but body (w_algebras.tex:240,1638) and same preface line 5070 use 32/(22+5c). Internal inconsistency. | **FIXED**: 16→32 in preface OPE |
| F64 | p.109 | **SERIOUS** | Beilinson | βγ central charge formula 1-3(2λ-1)² = 12λ²-12λ+2: algebraic error. 1-3(2λ-1)² = -12λ²+12λ-2 (this is c_bc, not c_βγ). Correct: 3(2λ-1)²-1 = 12λ²-12λ+2. | **FIXED** |
| F65 | p.107 | **MODERATE** | Drinfeld | "symmetry c(k)=c(-k-2h∨)" FALSE. c(k)≠c(-k-2h∨) in general (e.g. sl₂: c(2)=3/2, c(-6)=9/2). Correct: c(k)+c(-k-2h∨)=2 dim g. | **FIXED** |
| F66 | p.100 | **MODERATE** | Costello | bc ghosts misclassified as Contact (C, depth 4) in depth table. Census and free_fields.tex:142 say Gaussian (G, depth 2). | **FIXED**: moved bc to Gaussian row |
| — | p.106-110 | VERIFIED | All | Heisenberg OPE, κ=k, Koszul dual Sym^ch(V*), depth G. KM OPE, κ=(k+h∨)dim g/(2h∨), FF duality k↔-k-2h∨. W₃ quasi-primary Λ = :TT:-3/10 ∂²T, c=-22/5 degeneration. βγ OPE, depth C, genus-2 shell profile. ✓ |

### Pages 96-105 (Preface §5.5-6.8: genus spectral sequence, shadow tower, depth classes, genus-2 shells)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F62 | p.97 | **SERIOUS** | Beilinson | Spectral sequence bidegree: d₁: E₁^{0,*}→E₁^{1,*-1} inconsistent with general formula d_r bidegree (r,-r+1). For r=1: d₁ has bidegree (1,0), so d₁: E₁^{0,*}→E₁^{1,*}. Same error in body (higher_genus_modular_koszul.tex:10320). | **FIXED** (both files) |
| — | p.96-105 | VERIFIED | All | D₁²=0 (BV identity), total weight w=2g-2+r+d, obstruction classes always exact (bar-intrinsic), cubic gauge triviality, canonical quartic Q^contact_Vir=10/[c(5c+22)], G/L/C/M depth classification (verified census), genus loop Λ_P computation (120/[c²(5c+22)]), loop ratio ρ^(1)=240/[c³(5c+22)], quintic forcing o^(5)=480/[c²(5c+22)]x⁵, independent sum factorization. ✓ |

### Pages 93-96 (Preface §5: tangent complex, Chern-Weil, κ table, spectral discriminant, quartic shadow)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F54 | p.94 | **SERIOUS** | Gaiotto | κ(ψ) = 1/2 WRONG (landscape_census confirms 1/4). Free fermion c=1/2, κ=c/2=1/4. | **FIXED** |
| F55 | p.95 | **SERIOUS** | Gaiotto | βγ Hilbert series 1/(1-q)² and Δ=(1-x)² WRONG. Correct: h=√((1+q)/(1-3q)), Δ=(1-3x)(1+x). Confirmed by free_fields.tex:122 and beta_gamma.tex:18. | **FIXED** |
| F57 | p.95 | **MODERATE** | Beilinson | Chern character formula: [(-1)^{r-1}/(r-1)!] d^r log Δ ≠ (1/r)tr(T^r). Correct: [1/r!] d^r (-log Δ) = (1/r)tr(T^r). | **FIXED** |
| F61 | p.95 | MINOR | Kontsevich | det vs sdet inconsistency: formal definition (l.3839) used det, but l.1117 and l.3958 use sdet. | **FIXED**: changed to sdet |
| F58 | p.96 | MINOR | Costello | "cubic also vanishes" for βγ — wrong. Cubic is nonzero but gauge-trivial (thm:cubic-gauge-triviality). | **FIXED** |
| — | p.93-96 | VERIFIED | All | κ table (H, KM, Vir, βγ, lattice, W_N), Δ self-duality, sl₃ eigenvalues (8,(3±√13)/2), Chern-Weil dictionary, genus spectral sequence intro. ✓ |

### Pages 92-93 (Preface §4: Γ-amplitudes, bar-intrinsic construction, weight filtration, all-genus recursion)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F56 | p.92 | **SERIOUS** | Kontsevich | ℏ double-counting: ℓ₁^(1) and ℓ₂^(1) defined WITH ℏ, but full sum ℓ = Σ ℏ^g ℓ_k^(g)/k! adds another ℏ^g. BV operator would appear at O(ℏ²) not O(ℏ). | **FIXED**: removed ℏ from ℓ₁^(1) and ℓ₂^(1) definitions |
| F53 | p.92 | **MODERATE** | Gaiotto | "fifteen trees, five trivalent topologies, each with three planar labelings" — wrong. Two unlabeled topologies: balanced (3 labelings) + caterpillar (12). Also "five faces of K₄" → vertices. | **FIXED** |
| F59 | p.93 | **MODERATE** | Drinfeld | Recursion ordering: "2g'-2+n' < 2g-2+n" wrong (BV term has same EC). Correct: lexicographic in (g,n). | **FIXED** |
| F60 | p.93 | MINOR | Witten | "pentagon identity for the A∞ structure" — should be L∞ (10 divisors = symmetric, not planar). | **FIXED** |
| — | p.92-93 | VERIFIED | All | MC expansion D²=0 → [d₀,Θ]+½[Θ,Θ]=0. Weight filtration tower. (0,4) Borcherds identity Φ_s+Φ_t+Φ_u=F₃. (1,1) Casimir element. Clutching identity factorization. Tridegree, depth filtration, algebraic convergence. ✓ |

### Pages 87-91 (Preface §3: homotopy chiral algebras, log-FM, convolution L∞, assembly, bar functor, D²=0)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F51 | p.90 | **SERIOUS** | Witten | "Non-separating edges: cutting increases b₁ by one" — WRONG. Cutting DECREASES b₁; CREATION increases it. The ℏΔ operator creates, not cuts. | **FIXED**: "whose creation increases b₁ by one" |
| F52 | p.87 | **SERIOUS** | Beilinson | "(n-2)-associahedron" — off by 2. M̄_{0,n+1} ≅ K_n (Stasheff). For n=3: K₁ is a point but M̄_{0,4}=P¹ is 1-dim. | **FIXED**: "the associahedron K_n" |
| — | p.87-91 | VERIFIED | All | Čech totalisation, Ch∞ structure (Malikov-Schechtman), F₂=bracket, F₃ from M̄_{0,4}, HTT for higher F_n, rectification (Vallette), log-FM compactification, planted-forest types, tropicalization, Mok codimension formula, graphwise cocomposition, convolution L∞ formula, one-slot functoriality, strict chart MC moduli agreement, six-component differential (d_Č+d_{Ch∞}+d_coll+d_sew+d_pf+ℏΔ), orientation line det(kE)⊗det(H₁)^{-1}, coinvariants, D²=0 three mechanisms (vertex/one-edge/codim-2). ✓ |

### Pages 90-91 (Preface: clutching identity, modular tangent complex, κ table, three projections)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F34 | p.91 | **CRITICAL** | Gaiotto | W_N κ formula in table WRONG: stated (N-1)(N²k+N²-1)/(N+k), correct is c·(H_N-1). Sum rule also wrong: stated 0, correct is K_N·(H_N-1) ≠ 0. Same-family AP1 error. | **FIXED**: table now uses c·(H_N-1), c'·(H_N-1), K_N·(H_N-1). |
| — | p.88-89 | VERIFIED | All | Weight filtration, MC tower, boundary divisor counts (M̄_{0,4}: 3, M̄_{0,5}: 10 Petersen), planted-forest layer. ✓ |
| — | p.86-87 | VERIFIED | All | Explicit L∞ brackets, bar-intrinsic construction, universal twisting morphism. All correct. ✓ |
| — | p.80-85 | VERIFIED | All | Complementarity, FF duality, total space, Ch∞, log-FM, six-component differential. ✓ |

### Pages 78-79 (Preface: genus-g propagator, curvature, period integrals, genus tower, Â-genus, complementarity)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F33 | p.79 | **CRITICAL** | Beilinson/Gaiotto | F_g signs WRONG: listed F₁=-κ/24, F₂=+7κ/5760, F₃=-31κ/967680 (alternating from Â(x)). Correct: ALL POSITIVE (from Â(iℏ) = (ℏ/2)/sin(ℏ/2)). Compute tests confirm F₁=+κ/24. Also pattern "(-1)^g B_{2g}/(2g)!" wrong — missing (2^{2g-1}-1)/2^{2g-1} factor. | **FIXED**: corrected signs to all positive + correct FP pattern formula. |
| — | p.78-79 | VERIFIED | Witten | D²_g = d²_fib + [d_fib,∇^GM] + (∇^GM)² = κω_g - κω_g + 0 = 0. ✓ |
| — | p.78 | VERIFIED | Kontsevich | Genus-g propagator with (Im Ω)^{-1} correction is standard Arakelov. ✓ |
| — | p.78 | VERIFIED | All | κ(ĝ_k) = (k+h∨)dim g/(2h∨), κ=0 at critical level. ✓ |

### Pages 76-77 (Preface: Koszul dual construction, Heisenberg atom, KM OPE, prime form)

| — | p.76-77 | VERIFIED | All 6 | All formulas correct: residue sign, KM decomposition (dη distributional), prime form K^{-1/2}, FM contractibility, Heisenberg OPE, curved A∞ commutator. ✓ |

### Pages 74-75 (Preface: bar complex on X, d²=0 proof, categorical logarithm, Verdier duality)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F32 | p.74 | SERIOUS | Kontsevich | Bar complex formula used H^{n-1}(FM̄_n, Ω^{n-1}_log) but body text uses Γ (global sections). Bar differential acts on FORMS, not cohomology classes. H^{n-1} is wrong. | **FIXED**: changed to Γ in both occurrences (preface.tex:2259, 2454). |
| — | p.74-75 | VERIFIED | Beilinson | d²=0 nine-term proof structure (3 diagonal + 3 cross + 3 cancellations). ✓ |
| — | p.75 | VERIFIED | Gaiotto | Same-pair residue d²_res^{(ij)} = 0 (vacuous after collision). ✓ |
| — | p.75 | VERIFIED | Drinfeld | D_Ran B̄(A) ≃ A^!_∞ correctly stated (hypotheses implicit). ✓ |

### Pages 72-73 (Preface: Section 1 categorical logarithm, bar/cobar formulas, quadratic duality, chiral algebras)

| — | p.72-73 | VERIFIED | All 6 | Bar/cobar signs, Borcherds identity, Com^!=Lie, chiral algebra def. All correct. ✓ |

### Pages 70-71 (Preface: quartic closure, tautological classes, CohFT, primitive kernel, BV action)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F31 | p.70 | MODERATE | Gaiotto | Preface says "Mumford's relation λ_g²=0" but body proposition (prop:mumford-from-mc) proves a clutching law Σ ξ_sep(λ_{g₁}·λ_{g₂})+ξ_nsep(λ_{g-1})=0. Not the same statement. | **FIXED**: changed to "Mumford λ-class clutching relation". |
| — | p.70 | VERIFIED | Beilinson | Three conjectures (M.13.9, M.13.31, M.13.27) properly tagged \ClaimStatusConjectured. ✓ |
| — | p.70 | VERIFIED | Kontsevich | MC→WDVV at genus 0 correct (prop:wdvv-from-mc). ✓ |
| — | p.70 | VERIFIED | Witten | EO recursion = MC shadow proved for Koszul case. ✓ |
| — | p.71 | VERIFIED | Costello | Pre-Lie product ⋆ correctly defined; primitive master eq correct. ✓ |
| — | p.71 | VERIFIED | Drinfeld | Branch BV action standard; kinetic term ½Ω(K^br x,x) correct. ✓ |

### Pages 68-69 (Preface: Weil analogy, Polyakov dictionary, arithmetic packet, Miura defect)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F29 | p.68 | MODERATE | Witten | Polyakov dictionary "Ghost bc ↔ Koszul dual A^!" conflates BRST pairing with algebraic Koszul dual. | **FIXED**: added "(BRST pairing, not literal)". |
| F30 | p.68 | MODERATE | Kontsevich | Weil table "Frob²=q ↔ D²=0" conflates functional equation with nilpotence. | **FIXED**: added "(functional equation)" and "(nilpotence)" labels. |
| — | p.68-69 | VERIFIED | Gaiotto | Miura defect χ_{W_2}/χ_H = (1-q) correct. ✓ |
| — | p.68-69 | VERIFIED | Beilinson | Ramanujan chain honest about Deligne external input. ✓ |
| — | p.66-69 | VERIFIED | All | All Dirichlet series, Euler-Koszul tiers, L-objects verified. ✓ |

### Pages 64-65 (Preface: DS reduction, central charge additivity, geometric localization)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F28 | p.64 | **CRITICAL** | Drinfeld/Gaiotto | "κ → ∞ on affine side" at critical level k=-3 is WRONG. Formula gives κ = 4(k+3)/3 = 0. Should be "κ → 0 (curvature vanishes)." AP3 pattern-completion error. | **FIXED** (preface.tex:1348) |
| — | p.64-65 | VERIFIED | Gaiotto | κ(ŝl₃_k) = 4(k+3)/3 correct by (k+h∨)dim g/(2h∨). ✓ |
| — | p.64-65 | VERIFIED | Beilinson | FF duality: dual of ŝl₃_k is ŝl₃_{-k-6}. ✓ |
| — | p.65 | VERIFIED | Witten | c_ghost = 6 = 2|Δ⁺(sl₃)| correct. ✓ |
| — | p.65 | VERIFIED | All | c(ŝl₃_k)=8k/(k+3), c(W₃)=2-24/(k+3), c_ghost=6 additivity. ✓ |

### Pages 62-63 (Preface: Hessian, spectral discriminant, critical dimension, W₃ datum)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F27 | p.63 | **SERIOUS** | Costello | W₃ Hessian matrix uses κ_c without definition. κ_c = (c-50)/2 (Hessian eigenvalue), NOT κ = 5c/6 (modular characteristic). Notational collision — same symbol used for different objects 24 lines apart. | **FIXED**: added "κ_c := (c-50)/2" and clarifying remark in preface.tex:1244. |
| — | p.62-63 | VERIFIED | Gaiotto | κ(W₃) = 5c/6, K₃ = 100. ✓ |
| — | p.62 | VERIFIED | Beilinson | Δ_{ŝl₂}(x) = (1-kx)(1-(k+4)x)/(1-2x). ✓ |
| — | p.63 | VERIFIED | Witten | Polyakov formula = arity-2 shadow at κ=1. ✓ |
| — | p.62 | VERIFIED | Kontsevich | βγ genus-2 shell: only loop² (no cubic ⟹ no sepoloop). ✓ |
| — | p.63 | VERIFIED | Drinfeld | [ℓ₄^(0)] = 16/(22+5c)·Λ for W₃. ✓ |

### Pages 60-61 (Preface: Section IV Holography, holographic datum, three examples, arithmetic)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F25 | p.61 | MODERATE | Witten | "Genre tower is the perturbative expansion of 3d quantum gravity" — unsupported physics claim. | **FIXED**: downgraded to "has the formal structure of a perturbative expansion". |
| F26 | p.61 | MODERATE | Drinfeld | KZ connection ℏ undefined in ∇_KZ = d - ℏΩ/z. | **FIXED**: added "(with ℏ = 1/(k+2))". |
| — | p.60-61 | VERIFIED | Gaiotto | Affine level notation ŝl₂_k correct (FF: -k-4). ✓ |
| — | p.60-61 | VERIFIED | Kontsevich | Deconcatenation coproduct and coderivation property standard. ✓ |
| — | p.60-61 | VERIFIED | Costello | MacMahon formula Π_{n≥2}(1-q^n)^{-(n-1)} correct (proved in w_algebras_deep.tex). ✓ |

### Pages 58-59 (Preface: modular homotopy type, projection table, completion, finite windows)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| — | p.58-59 | VERIFIED | All 6 | Genus-1 MC equation, projection table, strong filtration axiom, zigzag theorem, collision→r-matrix, κ examples. All correct. | ✓ |

### Page 57 (Preface: Section III, modular homotopy type in three stages)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F24 | p.57 | MODERATE | Witten | "Two spaces have same rational homotopy type iff minimal models isomorphic" — missing "simply connected" hypothesis. | **FIXED** (preface.tex:630) |
| — | p.57 | VERIFIED | Kontsevich | Sullivan minimal model description correct. ✓ |
| — | p.57 | VERIFIED | Beilinson | Stage 1 bar complex signs (moot since x²=0). ✓ |
| — | p.57 | VERIFIED | Costello | HPL transfer and Massey product m₃. ✓ |
| — | p.57 | VERIFIED | Gaiotto | Heisenberg = formal = Gaussian archetype. ✓ |

### Page 56 (Preface: shadow metric, HJ equation, growth rate, inter-channel coupling)

| — | p.56 | VERIFIED | All 6 | All formulas verified exactly (shadow metric, HJ, δ₆, ρ, critical cubic). ✓ |

### Page 55 (Preface: curvature at genus g≥1, κ formulas, Virasoro shadow tower, complementarity)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F23 | p.55 | MODERATE | Beilinson | "anti-symmetry κ+κ^!=0 holds only when Koszul dual stays in same linear family" — misleading phrasing. Virasoro IS same family but κ+κ^!=13≠0. Text logically correct (P⟹Q) but readers will misread as P⟺Q. | **FIXED**: clarified to "holds for KM/free-field; for W-algebras sum = K(g)·(H_N-1) nonzero". |
| — | p.55 | VERIFIED | Gaiotto | κ(ŝl_{2k}) = 3(k+2)/4 correct by (k+h∨)dim g/(2h∨). ✓ |
| — | p.55 | VERIFIED | Gaiotto | κ(βγ_λ) = 6λ²-6λ+1 = c(βγ)/2 correct. ✓ |
| — | p.55 | VERIFIED | Witten | Q^contact_Vir = 10/(c(5c+22)), poles at c=0, c=-22/5 ((2,5)-minimal). ✓ |
| — | p.55 | VERIFIED | Kontsevich | Quartic contact = Schur complement is a PROVED theorem (thm:schur-complement-quartic). ✓ |
| — | p.55 | VERIFIED | Drinfeld | Anomaly ratio ρ = Σ(m_i+1)^{-1} matches κ/c for all families. ✓ |
| — | p.55 | VERIFIED | Costello | Genus-2 three-shell decomposition (loopoloop/sepoloop/pf) by graph type. ✓ |

### Page 54 (Preface: graph-sum formula, Heisenberg collapse, Koszul dual, complementarity)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F21 | p.54 | **CRITICAL** | Gaiotto | F_g formula WRONG: stated B_{2g}/(2g(2g-2)), correct is (2^{2g-1}-1)/2^{2g-1} · \|B_{2g}\|/(2g)! (Faber-Pandharipande). Wrong formula propagated to 4 files (AP5). Division by zero at g=1. | **FIXED** (4 files: preface.tex:337,980; poincare_duality_quantum.tex:732; thqg_preface_supplement.tex:560; frontier_modular_holography_platonic.tex:1714) |
| F22 | p.54 | ~~SERIOUS~~ | Beilinson | ~~D_Ran B̄(A) ≃ A^!_∞ stated without proof.~~ **RETRACTED**: proved as thm:bar-cobar-isomorphism-main (chiral_koszul_pairs.tex:2344, ProvedHere). |
| — | p.54 | VERIFIED | Witten | κ=0 at critical level k=-h∨ is correct (Sugawara undefined, not divergent). ✓ |
| — | p.54 | VERIFIED | Drinfeld | Feigin-Frenkel involution k↦-k-2h∨ correct. ✓ |
| — | p.54 | VERIFIED | Kontsevich | Â-genus generating function correct (matches compute tests once wrong explicit formula removed). ✓ |

### Page 53 (Preface: modular convolution algebra, E₁ variant, from point to curve, graph-sum formula)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F20 | p.53 | MODERATE | Beilinson | "Every theorem is a projection of Θ_A" — rhetorical overclaim. Five main theorems ARE projections (§10.22.10.2), but "every" is false for ~2,850 claims. | **FIXED** → "the five main theorems are projections" with §-ref. |
| — | p.53 | VERIFIED | Witten | 't Hooft 1/N expansion (preface.tex:218-226). λ used as formal variable. Standard. ✓ |
| — | p.53 | VERIFIED | Kontsevich | Shadow tower algebraicity Q_L: PROVED (thm:riccati-algebraicity). ✓ |
| — | p.53 | VERIFIED | Costello | HPL transfer: Chapter 8 develops this fully. ✓ |
| — | p.53 | VERIFIED | Drinfeld | FAss/ribbon graph identification: standard, in preface.tex:207-216. ✓ |
| — | p.53 | VERIFIED | Gaiotto | d²_fib = κ·ω_g: correct; distinct from Weyl anomaly (c/12)·χ. ✓ |

### Page 52 (Preface: Feynman transform, stable graph complex, convolution table)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F18 | p.52 | MODERATE | Beilinson | "codim-2 boundary reached by exactly two one-edge degenerations" — imprecise. Should say "codim-2 stratum is intersection of exactly two codim-1 divisors, with opposite orientations." | **FIXED** (preface.tex:98-100) |
| F19 | p.52 | MINOR | Kontsevich | ℏ^{g(Γ)} uses total genus (b₁+Σg(v)), not loop number b₁ alone. Correct for modular operads but differs from classical GK convention. Already defined at line 71. | **CLOSED** (convention stated) |
| — | p.52 | VERIFIED | Costello | End_{B̄(A)} in convolution table is correct (bar complex IS the target). ✓ |
| — | p.52 | VERIFIED | Drinfeld | Lie bracket Koszul signs correct in cohomological convention. ✓ |
| — | p.52 | VERIFIED | Gaiotto | FCom(0,n) = B(Com)(n) at genus 0, recovering Lie cooperad. ✓ |
| — | p.52 | VERIFIED | Witten | ℏ^{g(Γ)} correctly captures total genus for path integrals on curves. ✓ |

### Page 51 (Preface: Section I, "From algebras to operads / modular operads")

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F16 | p.51 | **CRITICAL** | Beilinson | algebraic_foundations.tex:45 had T^c(sĀ) but differential uses s^{-1}. | **FIXED** |
| F17 | p.51 | ~~MINOR~~ | Kontsevich | ~~Cobar notation s vs s^{-1}.~~ Preface states "Cohomological convention throughout: |d|=+1" (line 2084) and applies consistently. No error. | **CLOSED** |

---

## SUMMARY: Pages 1-96 audited, 50 findings resolved

| Category | Count | Details |
|----------|-------|---------|
| **FIXED** (text corrections applied) | 31 | F1-F3, F16, F18, F20-F21, F23-F50, F51-F61 |
| **CLOSED** (verified not errors) | 19 | F4-F15, F17, F19, F22, + 5 from §3-5 panels |
| **OPEN** | 0 | — |

---

## CUMULATIVE GLOSSARY (terms as first encountered)

- **Chiral algebra** (p.1): A on smooth curve X; D-module with chiral bracket μ: A⊠A → Δ_*A
- **Bar complex** B̄_X(A) (p.1): Wedge A^⊠n against η = ∧d log(z_i-z_j) on FM compactification, extract residues
- **Arnold relation** (p.1): η_ij∧η_jk + η_jk∧η_ki + η_ki∧η_ij = 0; equivalent to d²=0
- **Fulton-MacPherson** C̄_n(X) (p.1): Compactification of Conf_n(X) by iterated real blowup along diagonals
- **Verdier duality** D_Ran (p.1): Duality on D-modules on Ran(X); produces A^!_∞ from B̄_X(A)
- **Koszul locus** (p.1): Where bar spectral sequence collapses at E_2; A^!_∞ formal there
- **Three pillars** (p.1): MS24 (homotopy chiral), Mok25 (log FM), RNW19 (convolution sL∞)
- **Modular convolution algebra** g^mod_A (p.1): Conv_∞(C^{logFM}_mod, End_{Ch∞}(A^ch_∞))
- **Universal MC element** Θ_A (p.1): D_A - d_0; satisfies MC because D²_A = 0
- **Shadow tower** Θ^{≤r}_A (p.2): Finite-arity truncations of Θ_A
- **κ** (p.3): Modular characteristic; scalar trace of Θ_A at arity 2
- **Shadow metric** Q_L(t) (p.3): (2κ+3αt)²+2Δt²; classifies shadow depth
- **Shadow depth** r_max (p.3): G(2), L(3), C(4), M(∞) classification
- **Koszulness** (p.3): 12 conditions; 10 unconditional equivalences + 1 conditional + 1 one-directional
- **Operad** P (p.51): Collection {P(n)} with Σ_n-action, composition, unit
- **Operadic bar** B(P) (p.51): ⊕_T ⊗_v P(In(v)) ⊗ det(E(T)), sum over trees
- **Modular operad** O (p.51): Operations indexed by connected stable graphs; genus labels g(v) with stability 2g(v)-2+val(v)>0
- **Stable graph** Γ (p.51): Connected graph with genus labels; total genus g(Γ) = b₁(Γ) + Σ g(v)
- **Separating gluing** ξ_sep (p.51): O(g₁,n₁+1)⊗O(g₂,n₂+1) → O(g₁+g₂,n₁+n₂)
- **Non-separating gluing** ξ_ns (p.51): O(g,n+2) → O(g+1,n)

---

## PAGE-BY-PAGE NOTES

### Pages 1-2 (Abstract: construction and organizing principle)
- Bar complex from log forms on FM compactification; D²=0 from Arnold + modular operad boundary
- Three-pillar integration: MS24 + Mok25 + RNW19
- Θ_A := D_A - d_0; six-component differential (all 6 defined)

### Pages 3-4 (Abstract: main theorems and landscape)
- Theorems A-D+H correctly summarized
- Shadow tower, metric, depth classification G/L/C/M
- Koszulness 12 conditions (10+1+1)
- κ formula table: ~~W_N wrong~~ FIXED to c·(H_N-1)
- Frontier: Yangian/RTT, HS-sewing, Swiss-cheese, holographic programme

### Pages 5-50 (Table of Contents)
- Pure structural; no mathematical claims
- Ch.10 (Higher genus) is 320pp — the heart of the book
- Ch.7 (Bar-cobar adjunction) is 130pp
- Structure: Overture + Part I (Engine) + Part II (Landscape) + Part III (Bridges) + Part IV (Frontier) + Appendices

### Page 51 (Preface: Section I, From algebras to operads / modular operads)
- Classical bar-cobar over a point: standard, correct
- Operadic bar formula (1) with det(E(T)): matches GK94/LV12
- Modular operads: stability condition, gluing maps — all correct
- ~~Desuspension error~~ FIXED in algebraic_foundations.tex:45

### Concordance constitutional pass (2026-03-31, Codex)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F67 | — | **SERIOUS** | Beilinson | Concordance opening compressed Theorems A--H into “projections of the scalar level $\kappa$,” conflating theorem-level consequences of the full MC package with the scalar trace. Matching overclaims also appeared in `algebraic_foundations.tex` and `higher_genus_modular_koszul.tex`. | **FIXED** |
| F68 | — | **MODERATE** | Gaiotto | Concordance Theorem D summary omitted the single-generator scope of the cohomological identity and overcompressed the multi-weight case. Narrowed to the single-generator class identity plus the proven free-energy output. | **FIXED** |
| F69 | — | **MODERATE** | Kontsevich | Concordance/preface/theory prose stated “the shadow tower is the $L_\infty$ formality obstruction tower” without the genus-$0$ restriction required by `thm:shadow-formality-identification`; positive-genus corrections belong to the quantum layer. | **FIXED** |
| F70 | — | **SERIOUS** | Witten | Concordance promotions table advertised `conj:EO-recursion`(b) as promoted to “EO recursion for Koszul algebras,” but the source still carries a conditional/heuristic spectral-curve identification. Replaced with the proved MC-shadow recursion statement and fenced the residual conditionality. | **FIXED** |

### Uniform-weight Theorem D / GRR pass (2026-03-31, Codex)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F71 | — | **SERIOUS** | Beilinson | `introduction.tex` still summarized Theorem D as a globally universal scalar package: all-genus `\mathrm{obs}_g=\kappa\lambda_g`, all-genus `\hat A` series, and anomaly cancellation at all genera. The source theorem only gives all-genus scalar factorization on the uniform-weight lane, with genus~1 unconditional for arbitrary modular Koszul algebras. | **FIXED** |
| F72 | — | **CRITICAL** | Beilinson | `higher_genus_foundations.tex` Theorem `thm:genus-universality` still stated the Faber--Pandharipande free-energy formula without the multi-weight fence, even though its own proof and `rem:multi-generator-obs` show the higher-genus multi-weight factorization is open. Narrowed item (iii) to the uniform-weight lane and genus~1 unconditionality. | **FIXED** |
| F73 | — | **SERIOUS** | Kontsevich | The downstream GRR / generating-function theorems (`prop:grr-bridge`, `thm:universal-generating-function`, `thm:family-index`) inherited the same overstatement and presented the all-genus `\hat A` series as global. These were rewritten to state the proved uniform-weight scope and the residual genus~1 unconditional clause explicitly. | **FIXED** |
| F74 | — | **MODERATE** | Witten | Connection-layer summaries (`concordance.tex`, `thqg_perturbative_finiteness.tex`, `genus_complete.tex`, `bv_brst.tex`) still advertised the scalar free-energy formula as an unrestricted output of Theorem D. The stale summaries were narrowed to the uniform-weight lane so the narrative no longer outruns the theorem surface. | **FIXED** |

### THQG fixed-genus / scalar-lane convergence pass (2026-03-31, Codex)

| # | Page | Severity | Examiner | Finding | Status |
|---|------|----------|----------|---------|--------|
| F94 | — | **MODERATE** | Beilinson | Residual definition and concordance surfaces still wrote `\mathrm{obs}_g=\kappa\lambda_g` as a global identity. In `higher_genus_foundations.tex` this even appeared inside the definition of the obstruction projection itself, and in `concordance.tex` Theorem D was still summarized without the lane restriction. These were narrowed to: genus~1 universally, all genera only on the proved uniform-weight scalar lane. | **FIXED** |
| F95 | — | **CRITICAL** | Witten | `thqg_perturbative_finiteness.tex` still contained a source-level analytic overclaim cluster: the scalar partition-function definition, genus decomposition, effective bound, two-dimensional convergence theorem, tensor-product theorem, large-`N` `\mathcal W_N` remark, and quantitative tables all silently re-exported the obsolete global scalar closed form. This also produced a concrete falsehood: Gaussian rows were assigned `R_{\mathrm{grav}}=\infty`, conflating finite arity depth with infinite genus radius, and `\beta\gamma` still carried unsupported higher-genus entries. The chapter now distinguishes genuswise finiteness from scalar-lane convergence, replaces the false bidisk theorem by fixed-genus/Gaussian statements, corrects Gaussian radii to `4\pi^2`, and removes unsupported multi-weight higher-genus table data. | **FIXED** |
| F96 | — | **SERIOUS** | Witten | The BTZ subsection in both Volume I and Volume II was still claiming that the Virasoro scalar shadow series is the **full** perturbative BTZ partition function and that the shadow method therefore “extends automatically to all genera.” What is actually proved is narrower: Brown--Henneaux identifies the Virasoro scalar normalization, giving the genus~1 scalar term and the all-genus scalar series on the Virasoro scalar lane, but no comparison theorem to the full analytic BTZ partition function is constructed. Both volumes were rewritten to say “BTZ-normalized scalar shadow series,” and the higher-genus proposition was retitled accordingly. | **FIXED** |
| F97 | — | **CRITICAL** | Beilinson | The semiclassical/large-`c` subsection in both volumes contained a source-level bookkeeping error: it described the Virasoro scalar series as an “asymptotic expansion in `1/\kappa` that happens to converge,” and the proposition `prop:thqg-I-1c-expansion` outright identified `\log Z_{\mathrm{grav}}^{\mathrm{scal}}` with the genus series, contradicting the chapter’s own definition `Z_{\mathrm{grav}}^{\mathrm{scal}}=\sum_g F_g \hbar^g`. The corrected statement now concerns the **reduced scalar series** `Z_{\mathrm{grav}}^{\mathrm{scal}}-F_0`, keeps the tree-level term separate, and states the honest convergent `1/c` expansion on the Virasoro scalar lane. | **FIXED** |
| F98 | — | **MODERATE** | Kontsevich | The monster-CFT numerical example in both volumes still evaluated the scalar closed form at `\hbar=1` incorrectly by a factor of `2`: it wrote `12/\sin(1/2) \approx 25.0`, but the scalar bookkeeping series is `12\cdot(1/2)/\sin(1/2) \approx 12.515`. The same sentence also called this the “total perturbative partition function,” reintroducing the scalar-vs-full conflation by example. Both remarks now use the corrected scalar bookkeeping value, and the older Volume II Gaussian-complexity summary was aligned to the narrower Volume I wording. | **FIXED** |
| F99 | — | **CRITICAL** | Beilinson | Volume II still contained the pre-rectification THQG wrapper layer even after Volume I had been narrowed: the scalar partition-function definition still inserted the global closed form, the perturbative-finiteness and full-partition theorems still claimed a general full genus-sum radius and an `O(\hbar/\kappa^2)` scalar dominance statement, the two-parameter theorem still advertised a bidisk convergence result, and the quantitative table still listed Gaussian `R_{\mathrm{grav}}=\infty` plus unsupported higher-genus `\beta\gamma` data. These statements were all downgraded to the current proved surface: fixed-genus finiteness generally, scalar closed form only on the uniform-weight lane, Gaussian full-partition convergence with radius `4\pi^2`, and no general bidisk/full-radius theorem beyond that lane. | **FIXED** |
| F100 | — | **CRITICAL** | Beilinson | The early “shadow free energies” subsection was still exporting all-genus scalar universality upstream of the later corrected theorems. In both volumes, the definition of `F_g` built in the demoted identity `\int \kappa\lambda_g`, the vacuum-energy remark treated the Faber--Pandharipande package as global, and the explicit-values proposition listed the Bernoulli formulas as unconditional. Volume II was further stale in the closed-form proposition, universality remark, generating-function theorem, absolute-convergence theorem, and related remarks, all of which still treated the scalar closed form as valid for arbitrary modular Koszul algebras. The subsection now states the honest scope: all-genus Bernoulli/`\hat A` formulas only on the uniform-weight scalar lane, genus~1 universally, and descriptive remarks fenced to that proved lane. | **FIXED** |
| F101 | — | **SERIOUS** | Witten | Volume II still had downstream THQG connective tissue that re-imported the obsolete global scalar package after the theorem surfaces had been repaired: the genus-decomposition proposition wrote `F_g^{\mathrm{scal}}=\kappa\lambda_g^{\mathrm{FP}}` without the lane fence, the boundary-to-bulk summary said the closed partition function “follows” algorithmically from OPE data, the finiteness-mechanism chain concluded directly with `F_g=\kappa\lambda_g^{\mathrm{FP}}<\infty`, the tensor-product proposition/proof treated higher-genus scalar additivity as unconditional, and the “complete finiteness theorem” remark again claimed global convergence and meromorphic continuation. These were all narrowed to the current record: genuswise finiteness generally, scalar closed form and higher-genus additivity only on the proved scalar lane, and universal genus~1 separately. | **FIXED** |
| F102 | — | **CRITICAL** | Beilinson | The `S`-duality free-energy chapter in both volumes was still asserting a global all-genus scalar complementarity theorem and using it to derive Virasoro and bosonic-string cancellations at every genus. That contradicted the corrected Theorem~D surface, where genus~1 is universal but all-genus scalar factorization is only proved on the uniform-weight scalar lane. The theorem, its self-dual/partition-function corollaries, the Virasoro functional-equation example, the `c=26` degeneration theorem, and the bosonic-string budget were all narrowed to: universal genus~1 identities, all-genus formulas only under the explicit uniform-weight hypothesis, and no higher-genus Virasoro/bosonic cancellation claim outside that lane. | **FIXED** |
| F103 | — | **CRITICAL** | Beilinson | The scalar-lane fence had leaked back into the constitution and the Volume II summary atlas. In `concordance.tex` and `higher_genus_modular_koszul.tex`, the Hodge--lambda description of Theorem~D had reverted to an unqualified global identity `F_g=\kappa\lambda_g^{\mathrm{FP}}`. In `rosetta_stone.tex`, the `\hat A` theorem and its remarks escalated this into “everything in the monograph that depends on genus” and the outright false claim that classes `\mathbf{L}` and `\mathbf{C}` have no higher-arity shadow corrections, contradicting the shadow-depth classification `r_{\max}=3,4`. The affected surfaces now state the all-genus `\hat A` package only on the uniform-weight scalar lane, keep genus~1 universal separately, and treat classes `\mathbf{G}`/`\mathbf{L}`/`\mathbf{C}`/`\mathbf{M}` according to their actual finite or infinite shadow depth. | **FIXED** |
| F104 | — | **CRITICAL** | Beilinson | The core Theorem~D chain had regressed again. In `higher_genus_foundations.tex`, the theorem statement itself still said the Faber--Pandharipande formula holds for all modular Koszul algebras at all genera, its proof promoted the weight-1 propagator to a full multi-channel factorization theorem, and the later GRR bridge/family-index export inherited the same false global scope. The introduction repeated the same overclaim in both its early overview and its `\kappa`-properties synopsis, and the Virasoro functional-equation computation in `thqg_gravitational_s_duality.tex` ended by restating the false global factorization. These surfaces were all narrowed together: all-genus `\mathrm{obs}_g` / `F_g` factorization only on the proved uniform-weight scalar lane, genus~1 universal separately, multi-weight higher-genus factorization explicitly open, and GRR/family-index exports restricted to the scalar lane they actually use. | **FIXED** |
| F105 | — | **CRITICAL** | Beilinson | A new regression cluster was promoting vanishing of the scalar obstruction coefficient `\kappa` into vanishing of the full Maurer--Cartan/shadow tower. In `higher_genus_foundations.tex`, the “critical level characterization,” “tautological class map,” and “obstruction lifting criterion” were still stated globally, and `rem:dichotomy-theta` literally concluded that `\kappa=0` makes the universal MC element trivial. Downstream copies in the Virasoro `c=0` / `c=26` discussions (`thqg_gravitational_s_duality.tex`, `thqg_critical_string_dichotomy.tex`, `bar_complex_tables.tex`, `frontier_modular_holography_platonic.tex`) and in `arithmetic_shadows.tex` were accordingly calling `\mathrm{Vir}_0` “trivial” or setting `\Theta_{\mathrm{Vir}_0}^{\le r}=0`. These surfaces are now aligned to the honest statement: `\kappa=0` universally kills the genus~1 scalar term and, on the proved scalar lane, the scalar all-genus package; it does not by itself force the full higher-arity tower or the full MC element to vanish. | **FIXED** |
| F106 | — | **CRITICAL** | Beilinson | The critical-level / zero-anomaly surfaces were still conflating scalar cancellation with full differential collapse. In `thqg_gravitational_s_duality.tex` (both volumes), the affine critical-level theorem claimed `\Theta_{\widehat{\fg}_{-h^\vee}}=0` and `D=\dzero` from `\kappa=0`, even though the critical-level bar differential still contains the nontrivial simple-pole/screening part. In `higher_genus_modular_koszul.tex`, the same false import reappeared as “at critical level the MC element vanishes.” In Volume II’s `thqg_anomaly_extensions.tex`, effective matter--ghost scalar cancellation at `c=26` was escalated into a full “gravitational collapse,” calling `\mathrm{Vir}_0` trivial and using `\Theta=0` as if it described the coupled system. These surfaces now distinguish the vanishing scalar/minimal class `\Theta^{\min}` from the full MC/transgression object, keep the affine critical theorem at the uncurved-but-nonzero-differential level, and demote the `c=26` anomaly story to the proved effective scalar cancellation plus a formal zero-anomaly specialization. | **FIXED** |
| F107 | — | **CRITICAL** | Beilinson | A final copy-drift layer was still exporting the same false collapse into constitution, preface, example, and Volume II gravity-summary surfaces. In Volume I, `concordance.tex`, `preface.tex`, `kac_moody.tex`, and `thqg_perturbative_finiteness.tex` still said the Feigin--Frenkel/critical-level story occurs “where the shadow tower collapses” or even `\Theta_\cA=0`, instead of the corrected statement that only the scalar class vanishes and the bar complex becomes uncurved. In `editorial_constitution.tex`, self-duality was still incorrectly promoted to `\Theta_\cA = -\Theta_\cA = 0`, contradicting the nonzero self-dual Virasoro point at `c=13`. In Volume II, `holomorphic_topological.tex`, `ht_physical_origins.tex`, `3d_gravity.tex`, and `thqg_3d_gravity_movements_vi_x.tex` were still turning the Witt / `c=26` degeneration into “no higher `A_\infty` corrections,” “the genus tower vanishes,” “the transgression is trivial,” and even a trivial gravitational partition function. These surfaces now keep only the proved scalar/effective vanishing statements, explicitly separate them from the full higher-arity tower, and fence the remaining closed-string/Witt identifications as open. | **FIXED** |
| F108 | — | **CRITICAL** | Beilinson | The `G9` theorem surface in `twisted_holography_quantum_gravity.tex` had regressed into a direct contradiction of the corrected critical-string chapters. In Volume I it still said the dual sector at `c=26` is “trivial,” that the resonance-filtered bar-cobar “collapses,” and that the two Lagrangian summands coincide; in Volume II the same theorem was even worse, calling `\mathcal{H}(\mathrm{Vir}_{26})` self-conjugate under `S`-duality and `\mathrm{Vir}_0` the “trivial Virasoro algebra.” The Vol II `3d_gravity.tex` summary exported the same mistake by presenting `|\eta|^{(c-26)/6}` as the full partition function and calling the `c=26` exterior degeneration a full topological-gravity point. These surfaces are now aligned to the actual record: `c=13` is the Koszul self-dual point; `c=26` is the maximally asymmetric critical-string point where the dual scalar package vanishes, the depth-zero resonance model closes only at the scalar level, and the exterior/Clifford degeneration is only the effective scalar specialization, not the full coupled theory. | **FIXED** |
| F109 | — | **CRITICAL** | Beilinson | A further export layer in Volume II was still conflating the effective scalar series with the full gravitational theory. In `thqg_3d_gravity_movements_vi_x.tex`, the theorem “Gravitational partition function” stated `Z_{\mathrm{grav}}=\exp(((c-26)/2)(\hat A(i\hbar)-1))` as the full all-genera partition function of 3d Virasoro gravity, then specialized this to `Z_{\mathrm{grav}}=1` and “the gravitational theory is trivial” at `c=26`. The surrounding decomposition proposition and later summary line repeated the same mistake, while the THQG overview files (`twisted_holography_quantum_gravity.tex` in both volumes) still called `\mathrm{Vir}_0` “trivial Virasoro,” and `thqg_anomaly_extensions.tex` still used the same phrase in a quartic-resonance summary. These surfaces are now aligned to the corrected anomaly record: the closed `\hat A` formula is the effective scalar partition function, `c=26` makes that scalar series trivial but does not trivialize the full gravitational theory, and `\mathrm{Vir}_0` is only on the uncurved scalar locus, not a trivial algebra. | **FIXED** |
| F110 | — | **CRITICAL** | Beilinson | The `c=26` Virasoro/string surface was still carrying a source-level theorem mismatch. In `free_fields.tex`, `thm:virasoro-moduli` claimed a full identification `H^*(\barB_{\mathrm{geom}}(\mathrm{Vir}_{26})) \cong H^*(\overline{\mathcal M}_{0,n+3})`, the opening summary said BRST, amplitudes, and modular invariance “follow,” and the ghost remark promoted the genus-0 total-string BRST/bar comparison into a direct matter-only identity `Q_{\mathrm{BRST}} = d_{\barB}` with physical states equal to matter bar cohomology. `concordance.tex` was simultaneously citing the same theorem label as a proved constitutional item, and Volume II’s `anomaly_completed_frontier.tex` still said effective scalar cancellation at `c=26` “restores modular invariance.” These surfaces are now aligned to the actual record: the proved theorem is the critical genus-0 descent statement `d_{\mathrm{equiv}}^2 = (c-26)\mu`, giving an honest quotient cochain complex at `c=26`; the proved BRST/bar result is the genus-0 quasi-isomorphism for the total matter+ghost theory; moduli-space cohomology, amplitude localization, and full modular invariance remain conditional or heuristic. | **FIXED** |
| F111 | — | **SERIOUS** | Beilinson | The immediate satellites of the repaired `c=26` theorem in `free_fields.tex` were still exporting the old overclaim. The Koszul-duality summary table listed `\mathrm{Vir}_{26}` with context “Moduli ↔ BRST” and status `\ClaimStatusProvedHere`, the proposition `prop:moduli-degeneration` was still identifying a moduli-space residue operator with “the bar differential restricted to forms on moduli,” and the “Low degrees for Virasoro” example still reported `H^0,H^1,H^2` by reading off the cohomology of `\overline{\mathcal M}_{0,n+3}`. These are now narrowed to the honest surface: the table records only the proved genus-0 BRST/bar comparison; the proposition is a geometric boundary-residue model on logarithmic forms on moduli space; and the low-degree example is explicitly the moduli-space model, not an internal computation of Virasoro bar cohomology. | **FIXED** |
| F112 | — | **CRITICAL** | Beilinson | The critical-string application chapters were still promoting the repaired algebraic `c=26` shadow into the full classical no-ghost theorem. In both versions of `thqg_critical_string_dichotomy.tex`, the remark “The no-ghost theorem in bar-cobar language” literally identified the physical state space with `H^*(\barB^{(g)}(\mathrm{Vir}_0))`. In Volume II, the chapter opening also said `u=0` *is* the no-ghost theorem, and in both versions of `thqg_gravitational_s_duality.tex` the Lagrangian remark said positivity of the physical Hilbert space “follows” from the complementarity pairing. These surfaces are now aligned to the actual record: `u=0` and the exterior ghost factor provide an algebraic shadow of ghost-sector simplification, and the complementarity pairing gives an algebraic nondegenerate pairing, but the manuscript does not prove the classical no-ghost theorem or identify the full bosonic-string physical state space with Virasoro bar cohomology. | **FIXED** |
| F113 | — | **SERIOUS** | Beilinson | Two remaining `c=26` export surfaces were still overstating the algebraic record after the no-ghost cleanup. In `deformation_quantization_examples.tex`, the Virasoro compatibility computation ended with “at `c=26` the roles reverse (the no-ghost theorem),” collapsing the repaired algebraic shadow back into the full physical theorem. In `thqg_preface_supplement.tex`, the “transgression algebra” discussion went further: it claimed the bosonic-string BRST complex is a strict dg algebra and that the physical state space is `H^*(\mathrm{Tr}_{26})`, then said the gravitational path integral reduces to ordinary cohomology. These are now narrowed to the actual record: `\mathrm{Tr}_{26}` is a strict algebraic transgression model, not an identified physical-state complex; its ordinary cohomology is an algebraic invariant; and any physical BRST/path-integral interpretation requires extra comparison input not proved in the manuscript. | **FIXED** |
| F114 | — | **MODERATE** | Beilinson | After the broader no-ghost cleanup, one literal mirror slogan still remained in Volume I: the opening paragraph of `thqg_critical_string_dichotomy.tex` still said `u=0` *is* the no-ghost theorem expressed in bar-cobar language, even though the later Volume I remark and the entire Volume II surface had already been narrowed to the weaker “algebraic shadow” statement. This final stale sentence is now aligned with the corrected wording, so both volumes consistently describe `u=0` only as the exterior/uncurved algebraic shadow of the ghost-sector simplification appearing in the no-ghost theorem. | **FIXED** |
| F115 | — | **MODERATE** | Beilinson | A final status-drift line remained in the conjecture index. `editorial_constitution.tex` was still summarizing `conj:cobar-physical` as “Cobar construction as physical state space,” but the actual conjecture in `cobar_construction.tex` is already narrower: cobar elements are heuristic algebraic shadow data for on-shell propagators, and the cohomology is only conjectured to model physical on-shell scattering amplitudes. The index entry is now aligned to that actual conjectural scope. | **FIXED** |
| F116 | — | **CRITICAL** | Beilinson | The BRST/bar dictionary still had a source-level overclaim cluster. In `thqg_preface_supplement.tex`, a subsection was still stating that “the BRST complex of the bosonic string is the bar construction,” equating the anomaly-free locus with literal bar/BRST identity and extending the same language to the open-closed case. The underlying heuristic conjecture in `cobar_construction.tex` was malformed at the source level as well: it identified the bar complex itself with BRST cohomology and mapped “physical states” directly to bar classes, while `editorial_constitution.tex` exported that slogan as if it were the settled conjectural content. Volume II’s `thqg_anomaly_extensions.tex` then pushed the same drift one step further by identifying the BRST cohomology of the genus-`g` exterior ghost algebra with the full genus-`g` physical string state space. These surfaces are now aligned to the honest record: the proved algebraic input is the genus-`0` total matter+ghost BRST/bar quasi-isomorphism; beyond that, the BRST/bar dictionary is heuristic; curved/coderived bar models remain algebraic shadow data rather than proved physical-state complexes; and the exterior ghost algebra supplies only ghost zero-mode bookkeeping, not the full genus-`g` physical state space. | **FIXED** |
| F117 | — | **CRITICAL** | Beilinson | The new scalar-saturation proof had a real source-level gap. In `higher_genus_modular_koszul.tex`, Proposition `prop:saturation-equivalence` was using `\dim H^2_{\mathrm{cyc}}=1` to conclude `\Theta_{\cA}^{\min}=\kappa(\cA)\eta\otimes\Lambda`, but one-dimensionality of the cyclic direction only gives `\Theta_{\cA}^{\min}=\eta\otimes\Gamma_{\cA}` for some tautological coefficient `\Gamma_{\cA}`. The Kuranishi map vanishes by parity, so the MC equation places no constraint on which class in `H^*(\overline{\mathcal M}_g)` appears. This invalidated the claimed proof of `thm:algebraic-family-rigidity` as a global scalar-saturation theorem and forced `thm:multi-generator-universality` back to a conditional statement. The correction propagated to the introduction, concordance, `W`-algebra summaries, THQG finiteness chapter, `CLAUDE.md`, and the new compute/test surfaces, which now distinguish proved cyclic line-concentration from the still-open tautological-purity step `\Gamma_{\cA}=\kappa(\cA)\Lambda`. | **FIXED** |
