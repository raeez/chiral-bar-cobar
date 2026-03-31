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
