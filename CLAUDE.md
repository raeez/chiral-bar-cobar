# CLAUDE.md — Modular Homotopy Theory for Factorization Algebras on Curves

## What This Is

Two-volume research monograph by Raeez Lorgat. Vol I (~2,200pp, 77 active files, ~2,200 claims) is the algebraic engine: bar-cobar duality for chiral algebras on curves, with the five main theorems proved, a nonlinear shadow calculus with full Θ_A proved (bar-intrinsic, thm:mc2-bar-intrinsic) and finite-order engine through arity 4, and a comprehensive physics landscape (20+ worked examples from Gaiotto et al.). Vol II (~500pp, at ~/chiral-bar-cobar-vol2, 41+ files, ~500+ claims with 100% tag coverage) applies the engine to 3d holomorphic-topological QFT, PVA quantization, and holography.

**Vol I structure**: Overture (Heisenberg atom) + Part I (The Algebraic Engine: Thms A-D+H, HTT, nonlinear shadow tower, branch-line reductions) + Part II (The Standard Landscape: all example families + combinatorial frontier) + Part III (Bridges: Feynman, BV/BRST, YM boundary theory, E_n, Langlands) + Part IV (The Frontier, concordance) + Appendices (4 clusters: A-Foundations, B-Nonlinear Calculus, C-Extended Families, D-Physics+Reference).

**Vol I title**: *Modular Koszul Duality*
**Vol II title**: *A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT*

## The Dual Imperative

Maximalist ambition synergizes with maximal truth-seeking. Precision enables ambition. When claims outrun proofs, strengthen the proof first.

## Five Main Theorems (all proved)

- **(A)** Bar-cobar adjunction + Verdier intertwining on Ran(X)
- **(B)** Bar-cobar inversion: Omega(B(A)) -> A quasi-iso on Koszul locus
- **(C)** Complementarity: Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)); upgraded to shifted-symplectic Lagrangian geometry
- **(D)** Modular characteristic: kappa(A) universal, additive, anti-symmetric, A-hat GF
- **(H)** Hochschild: ChirHoch*(A) polynomial, Koszul-functorial

## Koszulness Characterization Programme

Major structural component. The meta-theorem (thm:koszul-equivalences-meta in chiral_koszul_pairs.tex) lists 12 equivalent characterizations of chiral Koszulness — **11 unconditionally proved + 1 conditional**. D-module purity is a 13th characterization, partially proved. Concordance section: sec:concordance-koszulness-programme.

**Unconditionally proved (11):**
- K1: PBW degeneration at all genera
- K2 (prop:ainfty-formality-implies-koszul): A∞ formality of bar cohomology implies Koszulness
- K3 (prop:shadow-formality-low-arity): shadow tower = L∞ formality obstruction tower at arities 2,3,4
- K4 (prop:e2-formality-hochschild): E₂-formality of ChirHoch*(A) for Koszul algebras
- K5 (prop:genus0-curve-independence): genus-0 Koszulness is independent of the curve X
- K6 (prop:pbw-universality): freely strongly generated vertex algebras are chirally Koszul
- K7 (thm:barr-beck-lurie-koszulness): Barr-Beck-Lurie monadic characterization
- K8 (thm:fh-concentration-koszulness): factorization homology concentration
- K9 (thm:fm-boundary-acyclicity): FM boundary acyclicity
- K10: tropical Koszulness (weight spectral sequence on real blowup)
- K12: bifunctor decomposition (one-slot + contractibility)

**Conditional (1):**
- K11 (thm:lagrangian-koszulness): Lagrangian criterion (conditional on perfectness/nondegeneracy hypotheses)

**Partially proved (13th characterization, outside meta-theorem):**
- conj:d-module-purity-koszulness: D-module purity (forward direction proved, converse open)

## Three Concentric Rings (the architecture)

**Ring 1** — Proved core: Theorems A-H, **MC1-5 ALL PROVED**, DK-0 through DK-3, MC3 thick generation (type A all N), MC4 strong completion towers (thm:completed-bar-cobar-strong, W_N rigidity, 21 conjectures resolved), MC5 all-genera sewing (thm:general-hs-sewing, thm:heisenberg-sewing), Koszulness 11 unconditional + 1 conditional (thm:koszul-equivalences-meta); D-module purity partially proved (13th characterization).
**Ring 2** — Nonlinear characteristic layer (the shadow Postnikov tower), FULLY INTEGRATED across Parts I-III. The primary mathematical object is the filtered finite-order engine: Theta_A^{<=2} (kappa), Theta_A^{<=3} (cubic shadow), Theta_A^{<=4} (quartic shadow), ... with obstruction classes o_{r+1}(A) in the cyclic deformation complex. Proved at finite order: kappa for all families, cubic shadows, quartic resonance class with clutching law (via Mok's log FM degeneration). Q^contact_Vir = 10/[c(5c+22)]. Genus-1 Hessian correction delta_H^(1)_Vir = 120/[c^2(5c+22)]x^2. Shadow archetypes computed in every example chapter: Heisenberg=Gaussian/terminates@2, affine=Lie/tree/terminates@3, betagamma=contact/quartic/terminates@4, Virasoro/W_N=mixed (infinite tower, quintic forced). Shadow depth classification into four classes: G (Gaussian, r_max=2), L (Lie/tree, r_max=3), C (contact/quartic, r_max=4), M (mixed, r_max=infinity). Operadic complexity conjecture (conj:operadic-complexity): r_max(A) = A∞-depth = L∞-formality level. The shadow tower = L∞ formality obstruction tower identification is PROVED at arities 2,3,4 (prop:shadow-formality-low-arity). Ambient complementarity = shifted-symplectic Lagrangian geometry, CONDITIONAL on perfectness/nondegeneracy hypotheses. The full Theta_A (all arities, all genera) is PROVED by the bar-intrinsic construction (thm:mc2-bar-intrinsic): Theta_A := D_A - d_0 is MC because D_A^2 = 0. The shadow tower consists of its finite-order projections.
**Ring 3** — Physics-facing frontier: W-algebra axis (MC4 W_infty closed unconditionally), Yangian/RTT axis (**MC3 character-level proved**, DK-5 formal once categorical inputs established), holographic/celestial axis (anomaly-completed Koszul duality, M2 example in Vol II, holographic modular Koszul datum H(T) = (A, A!, C, r(z), Θ_A, ∇^hol) packaging the full HT holographic system into a single modular MC problem with five theorem targets). **MC4 splitting**: MC4⁺ (positive towers: W_{1+∞}, affine Yangians, RTT — SOLVED by weight stabilization, thm:stabilized-completion-positive) vs MC4⁰ (resonant towers: Virasoro, non-quadratic W_N — reduced to finite resonance problem by thm:resonance-filtered-bar-cobar). Resonance rank ρ(A) (def:resonance-rank) classifies completion difficulty. Platonic completion conjecture (conj:platonic-completion): every positive-energy chiral algebra has ρ < ∞. Vir_{26-c} reinterpreted as depth-zero resonance shadow. **Analytic completion programme** (raeeznotes90): sewing envelope A^sew (Hausdorff completion for sewing-amplitude seminorms), analytic bar coalgebra B^an(A) (graph-norm closure), analytic Koszul pairs, HS-sewing condition (Hilbert-Schmidt multiplication → trace-class amplitudes), coderived analytic shadows Q_g^an(A), shadow partition function. Platonic chain: A_alg ⊂ A^sew ⇝ F_A ∈ IndHilb ⇝ Q•^an(A). Four target theorems/conjectures: (A_an) Heisenberg sewing theorem (thm:heisenberg-sewing, PROVED: one-particle Bergman reduction, Fredholm determinant, thm:heisenberg-one-particle-sewing), (B_an) lattice sewing envelope (conj:lattice-sewing, conjectural), (C_an) analytic realization criterion (conj:analytic-realization, conjectural), (D_an) boundary bar duality (conj:boundary-bar-duality, conjectural). HS-sewing PROVED for entire standard landscape (thm:general-hs-sewing: polynomial OPE growth + subexponential sector growth ⟹ convergence). References: Moriwaki 2026 (conformally flat FH in IndHilb, Heisenberg/Bergman), Adamo-Moriwaki-Tanimoto 2024 (conformal OS for unitary full VOAs).

**Unifying principle**: The modular L∞ convolution algebra g^mod_A is the single organizing structure. It carries a natural modular L∞ structure (from the Feynman transform of the modular operad); the dg Lie algebra (def:modular-convolution-dg-lie) is its strict model. The shadow Postnikov tower is the finite-order projection of the universal MC element Θ_A. The shadow Postnikov tower — κ (arity 2), cubic shadow C (arity 3), quartic resonance class Q (arity 4) — consists of finite-order projections of the universal MC element Θ_A (thm:mc2-bar-intrinsic). Theorems A-D+H and the genus expansion are proved projections of the scalar level κ. The full MC element Θ_A ∈ MC(g^mod_A) satisfying D·Θ + ½[Θ,Θ] = 0 is PROVED: Θ_A := D_A - d_0 is MC because D_A² = 0 (thm:convolution-d-squared-zero). The weight filtration on g^mod controls the extension tower; each finite truncation Θ_A^{<=r} is constructive and does not require the full all-genera modular envelope.

## Three-Pillar Foundational Architecture (NEW)

Three preprints force upgrades at three levels. Recorded in concordance.tex sec:concordance-three-pillars.

**Pillar A** (MS24): Primitive local object = homotopy chiral algebra (Ch∞), not strict. Strict chiral algebra appears after rectification. Ch∞ → strict on H^• → PVA/coisson shadow.
**Pillar B** (RNW19+Val16): Universal deformation machine = filtered convolution sL∞-algebra hom_α(C,A). Deformation space = MC ∞-groupoid. dg Lie algebra = strict model. **Key constraint**: hom_α extends to ∞-morphisms in either slot separately but NOT both simultaneously (no-bifunctor obstruction). MC3 categorical lift must proceed one slot at a time.
**Pillar C** (Mok25): Global collision geometry = log FM compactification FM_n(X|D) on snc pairs. Tropicalization = planted forests (G_pf = Trop(FM_n(C|D))). Semistable degeneration formula → clutching laws.

**Eleven identification theorems** (9 proved, 2 structural):
1. g^mod_A = hom_α(C^!_ch, P^ch) (thm:convolution-master-identification)
2. Θ_A ∈ MC(hom_α) ≅ Tw_α (cor:theta-twisting-morphism)
3. G_pf = Trop(FM_n(C|D)) (thm:planted-forest-tropicalization)
4. B(A) is Ch∞-algebra (thm:cech-hca)
5. B_κ ⊣ Ω_κ is Quillen equivalence (thm:quillen-equivalence-chiral)
6. A^sh is homotopy invariant (thm:shadow-homotopy-invariance)
7. One-slot obstruction constrains MC3 (RNW19 Theorem 6.1)
8. F_n = o_n: secondary Borcherds operations = shadow tower obstruction classes (prop:borcherds-shadow-identification)
9. Quartic clutching law via Mok's degeneration formula [Mok25, Cor 5.3.4] (constr:arity4-degeneration)
10. Log clutching conjecture proved via [Mok25, Cor 5.3.4] (conj:log-clutching-degeneration → proved)
11. Ambient D²=0 proved via Mok's log FM normal-crossings [Mok25, Thm 3.3.1] (thm:ambient-d-squared-zero)

## The Chriss-Ginzburg Principle (the architecture)

Every algebraic structure in the monograph is a Maurer-Cartan element in a convolution dg Lie algebra. The key objects:

1. **Modular cyclic deformation complex** `Def_cyc^mod(A)` (def:modular-cyclic-deformation-complex in chiral_hochschild_koszul.tex): the ambient home. Differential from graph composition, bracket from stable-curve gluing.
2. **Stable-graph and planted-forest coefficient algebras** `G_st`, `G_pf` (def:stable-graph-coefficient-algebra, def:planted-forest-coefficient-algebra in higher_genus_modular_koszul.tex): the explicit combinatorial heart of g^amb_A.
3. **Shadow Postnikov tower** Θ_A^{<=r}: the proved finite-order truncations. Each level is a graph sum through arity r with obstruction class o_{r+1}(A) in the cyclic deformation complex.
4. **Bar complex as modular operad algebra** (thm:bar-modular-operad in bar_cobar_adjunction_curved.tex): {B^(g,n)(A)} is an algebra over FCom (Feynman transform of commutative modular operad). ∂²=0 at all genera is a formal consequence.
5. **Modular dg-shifted Yangian as pro-MC** (def:modular-yangian-pro in yangians_drinfeld_kohno.tex): Y_T^mod = pronilpotent completion of convolution dg Lie algebra. R_T^mod(z;ℏ) is an MC element.
6. **Shadow algebra** `A^sh` (def:shadow-algebra in higher_genus_modular_koszul.tex): H_•(Def_cyc^mod(A)) as graded commutative ring. Shadows (κ, Δ, C, Q, Sh_r) are graded projections at finite order. The all-arity master equation is the MC equation projected to arity r. The full tower convergence Θ_A = varprojlim Θ_A^{<=r} is PROVED (thm:recursive-existence).
7. **Koszulness characterization programme** (sec:concordance-koszulness-programme in concordance.tex, thm:koszul-equivalences-meta in chiral_koszul_pairs.tex): 12 equivalent characterizations of chiral Koszulness (K1-K12, **11 unconditionally proved + 1 conditional**; D-module purity = 13th, partially proved). K1-K12: PBW degeneration, A∞ formality, shadow-formality, E₂-formality, curve independence, PBW universality, Barr-Beck-Lurie, FH concentration, FM boundary acyclicity, tropical Koszulness, Lagrangian criterion (conditional on perfectness/nondegeneracy), bifunctor decomposition.

8. **Platonic package** Π_X(L) (constr:platonic-package in concordance.tex): six-fold datum (Fact_X(L), B̄_X(L), Θ_L, L_L, (V^br_L, T^br_L), R_4^mod(L)) from cyclically admissible Lie conformal algebra L (def:cyclically-admissible). Target: modular factorization envelope U^mod_X as left adjoint of primitive-current functor Prim^mod (conj:platonic-adjunction). Envelope + bar coalgebra + universal MC class = platonic form.
9. **Cubic gauge triviality** (thm:cubic-gauge-triviality in higher_genus_modular_koszul.tex): If H^1(F^3g/F^4g, d_2) = 0, then cubic MC term is gauge-trivial and the quartic class [Θ'_4] ∈ H^2(F^4g/F^5g, d_2) is canonical. Abstract reason first nonlinear shadow is quartic.
10. **Independent sum factorization** (prop:independent-sum-factorization in higher_genus_modular_koszul.tex): For L = L₁ ⊕ L₂ with vanishing mixed OPE, all shadows separate: κ additive, T^br direct sum, Δ multiplicative, R_4^mod additive.
11. **Graphwise cocomposition** (const:vol1-graphwise-log-fm-cocomposition): Δ^log_Γ := (ν_Γ)_* ∘ Res_{D^log_Γ}, Γ-amplitude ℓ_Γ, Taylor coefficients ℓ_k^(g) = Σ_Γ |Aut(Γ)|^{-1} ℓ_Γ.
12. **Boundary operators as residue correspondences** (const:vol1-boundary-operators-residue): d_sew, d_pf, ℏΔ as residue/pushforward on log-FM strata. D²=0 = codimension-2 face cancellation.
13. **Depth filtration and tridegree** (def:vol1-rigid-planted-forest-depth-filtration): Tridegree (g,n,d) = (loop genus, arity, log boundary depth) from Mok's stratification.
14. **Genus spectral sequence** (const:vol1-genus-spectral-sequence): E_1 page isolates tree (p=0), one-loop (p=1), genus-2 shell (p=2) data. Differentials = obstruction maps Ob_g. DISTINCT from PBW spectral sequence.
15. **Modular tangent complex** (const:vol1-modular-tangent-complex): L∞ twisted differential d_{Θ_A}(x) = Σ (ℏ^g/n!) ℓ_{n+1}^(g)(Θ_A^⊗n, x); strict chart = d + [Θ_A, -]. Characteristic projections: κ, Δ_A, R^mod_4.
16. **Θ_A as universal twisting morphism** (cor:vol1-theta-log-fm-twisting-data): MC_•(Def∞^mod_log) ≃ Tw_α^mod.

17. **Shadow metric** `Q_L` (def:shadow-metric in higher_genus_modular_koszul.tex): quadratic form on each primary line L. The MC equation on L is equivalent to H² = t⁴Q (thm:riccati-algebraicity): shadow tower is algebraic of degree 2. Gaussian decomposition Q = (2κ+αt)² + 2κΔt². Critical discriminant Δ = 8κS₄ classifies shadow depth: Δ = 0 ⟺ tower terminates.
18. **Shadow connection** ∇^sh = d - Q'/(2Q) dt (thm:shadow-connection): logarithmic connection of Q_L. Residue 1/2 at zeros of Q. Monodromy = -1 (Koszul sign). Complementarity of discriminants: Δ(A) + Δ(A!) = 6960/[(5c+22)(152-5c)] (constant numerator). Self-dual at c=13.
19. **Propagator variance** δ_mix = Σf_i²/κ_i - (Σf_i)²/Σκ_i (thm:propagator-variance): multi-channel non-autonomy on the diagonal. Non-negative by Cauchy-Schwarz. Vanishes iff quartic gradient curvature-proportional (enhanced symmetry). Mixing polynomial P(W₃) = 25c²+100c-428. Computable from arity 2+4 alone.

The proved core descends from finite-order truncations of the shadow tower. The full equation **D_A Θ_A + ½[Θ_A, Θ_A] = 0** is PROVED at all levels: D²=0 at the convolution level is a THEOREM (from ∂²=0 on M̄_{g,n}), and at the ambient level D²=0 is also PROVED (thm:ambient-d-squared-zero, via Mok's log FM normal-crossings result). The all-arity inverse limit Θ_A = varprojlim Θ_A^{≤r} exists (thm:recursive-existence). Scalar saturation universality is proved for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape at all non-critical levels including admissible ones.

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
make test                                                         # Fast tests (~8.1K)
make test-full                                                    # All tests (~8.8K)
python3 scripts/generate_metadata.py                              # Census (authoritative)
```

**CAUTION**: Watcher spawns competing pdflatex; always kill before builds.

## Session Entry

1. Read this file and concordance.tex (the constitution)
2. Build: `make fast` (kill pdflatex first)
3. Read relevant source files before writing
4. After each change: verify build compiles
5. Never guess a formula — compute it or cite it

## Critical Pitfalls — MEMORIZE THESE

**Four objects that must never be conflated:**
- A: the algebra. B(A): the bar coalgebra. A^i = H*(B(A)): the dual coalgebra. A^! = (A^i)^v: the dual algebra.
- Omega(B(A)) = A (bar-cobar INVERSION, not duality). A^! is obtained by VERDIER/LINEAR duality, not cobar.

**Grading**: COHOMOLOGICAL (|d|=+1). Bar uses DESUSPENSION.
**Koszul duality**: Com^! = Lie (NOT coLie). Heisenberg NOT self-dual. Chiral Koszulness != classical Koszulness.
**Curved A-infinity**: m_1^2(a) = [m_0, a] (COMMUTATOR, MINUS sign). Bar d^2=0 always; curvature shows as m_1^2 != 0.
**Sugawara**: UNDEFINED at critical level k=-h^v (not "c diverges"). Feigin-Frenkel: k <-> -k-2h^v.
**Virasoro**: Self-dual at c=13, NOT c=26. Vir_c^! = Vir_{26-c}. The same-family shadow Vir_{26-c} is the DEPTH-ZERO RESONANCE SHADOW (rem:virasoro-resonance-model): it is the image of the finite-dimensional resonance truncation R_Vir, not the final dual. The genuine W_∞-type dual requires the full resonance-filtered completion (conj:platonic-completion).
**FM compactification**: Blowup along diagonals, NOT complement of diagonal.
**Prime form**: Section of K^{-1/2} boxtimes K^{-1/2} (NOT K^{+1/2}).
**QME**: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2).
**d_bracket^2 != 0**: PROVED (all 2048 signs). Full Borcherds d gives d^2=0.
**sl_2 bar H^2 = 5** (not 6; Riordan WRONG at n=2).
**Convolution algebra**: The dg Lie algebra Conv_str(C,P) is a STRICT MODEL of the underlying modular L∞ algebra Conv_∞(C,P). MC moduli coincide; full L∞ needed for transfer, formality, gauge equivalence. Bar-cobar preserves quasi-isos BECAUSE it is a quantum L∞ functor.
**Shadow tower (the primary object)**: The shadow Postnikov tower Θ_A^{<=r} consists of finite-order projections of the bar-intrinsic MC element Θ_A := D_A - d_0 (thm:mc2-bar-intrinsic). κ, C, Q are successive projections. The full Θ_A is PROVED by the bar-intrinsic construction. All-arity convergence Θ_A = varprojlim Θ_A^{<=r} is PROVED (thm:recursive-existence). Scalar saturation universality is PROVED for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape. The residual conjecture is restricted to non-algebraic-family constructions (no known modular Koszul example with simple Lie symmetry).
**D²=0**: At the convolution level, D²=0 is a THEOREM (from ∂²=0 on M̄_{g,n}). At the ambient level (with planted-forest corrections), D²=0 is now PROVED (thm:ambient-d-squared-zero, via Mok's log FM normal-crossings, [Mok25, Thm 3.3.1]).
**Shadow depth vs Koszulness**: Shadow depth r_max does NOT characterize Koszulness. Both finite (Heis@2, aff@3, βγ@4) and infinite (Vir@∞) shadow depth algebras are Koszul. Shadow depth classifies COMPLEXITY of Koszul algebras (G/L/C/M classes), not Koszulness itself.
**Single-line dichotomy** (thm:single-line-dichotomy): On any 1D primary slice of Def_cyc^mod, the shadow metric Q_L(t) = (2κ + αt)² + 2Δt² with critical discriminant Δ = 8κS₄ forces r_max ∈ {2, 3, ∞}. The four-class partition G/L/C/M is structural: Δ = 0 ↔ perfect square Q_L ↔ finite tower (G or L); Δ ≠ 0 ↔ irreducible Q_L ↔ infinite tower (M). The contact class C (r_max = 4) escapes via STRATUM SEPARATION: the quartic contact invariant lives on a charged stratum whose self-bracket exits the complex by rank-one rigidity. Total depth d = 1 + d_arith + d_alg (thm:depth-decomposition). Algebraic depth d_alg ∈ {0, 1, 2, ∞}. Depths ≥ 5 are purely arithmetic (cusp forms).
**Universal vs simple quotient**: V_k(g) is Koszul for ALL k (prop:pbw-universality). L_k(g) may fail at admissible levels. The PBW criterion applies to the UNIVERSAL algebra; failure for simple quotients comes from vacuum null vectors.
**Three-pillar constraints**: (1) The convolution sL∞-algebra hom_α(C,A) is NOT a strict Lie algebra — it is shifted homotopy Lie with higher brackets ℓ_k (k≥3). The dg Lie is a strict MODEL only. (2) hom_α is functorial in either slot separately but FAILS as a bifunctor in both slots simultaneously (RNW19 §6). MC3 categorical lift must proceed one slot at a time. (3) Log FM compactification FM_n(X|D) ≠ classical FM; requires snc pair (X,D). Ordinary FM is the D=∅ special case.
**Non-principal W-duality**: DS reduction for arbitrary nilpotent f EXISTS (Kac-Roan-Wakimoto). The obstruction is NOT defining W_k(g,f); it is proving bar-cobar/Koszul COMMUTES with non-principal reduction. Hook-type in type A is PROVED corridor. Full arbitrary-nilpotent BV duality is CONJECTURAL. Proposition 21.19.29 in current global form COLLAPSES theorem/conjecture boundary — must be restricted to proved cases (principal, sl₃ subregular/minimal, hook-type).
**Factorization envelopes**: Nishinaka's construction starts from Lie conformal algebras, NOT arbitrary vertex algebras. The factorization envelope gives the ENVELOPING vertex algebra, not an arbitrary one. Vicedo's construction is the full/non-chiral analogue. Neither constructs the MODULAR completion — that is the frontier.
**Analytic vs algebraic**: The bare VOA/chiral algebra is a dense algebraic skeleton. The actual object for partition functions and sewing is the sewing envelope A^sew (Hausdorff completion). Curvature at genus g ≥ 1 forces coderived/contraderived categories, NOT ordinary derived categories. IndHilb-valued factorization homology (Moriwaki 2026) is 1-categorical, metric-dependent, conformally flat only — NOT yet the full analytic story.

## LaTeX Rules

- All macros in main.tex preamble — NEVER \newcommand in chapter files (use \providecommand for compatibility)
- Document class: memoir; fonts: EB Garamond via newtxmath + ebgaramond
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic
- Label everything: \label{def:}, \label{thm:}, etc. Cross-reference with \ref, never hardcode.

## What NOT To Do

- Do not add packages without checking preamble compatibility
- Do not change verified formulas without checking Critical Pitfalls
- Do not create new .tex files when content belongs in existing chapter
- Do not duplicate definitions — reference from Part I
- Do not guess file locations — use Glob/Grep to find them

## Key File Renames (from platonic cleanup)

| Old name | New name |
|----------|----------|
| kac_moody_framework.tex | kac_moody.tex |
| w_algebras_framework.tex | w_algebras.tex |
| detailed_computations.tex | bar_complex_tables.tex |
| examples_summary.tex | landscape_census.tex |
| deformation_theory.tex | chiral_hochschild_koszul.tex |
| deformation_examples.tex | deformation_quantization_examples.tex |

## Titan Splits (dispatchers → parts)

| Original | Split into |
|----------|-----------|
| higher_genus.tex | higher_genus_foundations + higher_genus_complementarity + higher_genus_modular_koszul |
| yangians.tex | yangians_foundations + yangians_computations + yangians_drinfeld_kohno |
| bar_cobar_adjunction.tex | bar_cobar_adjunction_curved + bar_cobar_adjunction_inversion |

## Git — HARD RULE

All commits authored by Raeez Lorgat. **Never credit an LLM.** No "co-authored-by", no "generated by", no AI attribution anywhere.

## Constitution

**Single source of truth**: concordance.tex (the constitution). When chapters disagree, the constitution is right.

**MC frontier** (MC1-5 ALL PROVED; MC3 arbitrary-type extension is the remaining frontier):
- MC1: **PROVED** (PBW concentration, all standard families)
- MC2: **PROVED** (bar-intrinsic construction, thm:mc2-bar-intrinsic): Θ_A := D_A - d_0 is automatically MC because D_A² = 0. No restriction to simple Lie symmetry needed. Scalar saturation (Θ = κ·η⊗Λ) proved for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape at all non-critical levels including admissible ones. Residual universality conjecture restricted to non-algebraic-family constructions.
- MC3: **PROVED IN TYPE A** (thm:mc3-type-a-resolution): chromatic filtration + prefundamental CG closure + Efimov completion + DK on compacts. Extension to arbitrary simple type stated as conj:mc3-arbitrary-type (requires Hernández-Jimbo prefundamental CG for all Dynkin types). DK-5 now accessible in type A.
- MC4: **PROVED** — Strong completion-tower theorem (thm:completed-bar-cobar-strong): finite-stage bar-cobar passes to inverse limits automatically via strong filtration axiom μ_r(F^{i_1},...,F^{i_r}) ⊂ F^{i_1+...+i_r}, yielding arity cutoff (lem:arity-cutoff) that makes continuity + ML automatic. CompCl(F_ft) carries quasi-inverse bar-cobar homotopy equivalence (cor:completion-closure-equivalence), stable under MC twisting (thm:mc-twisting-closure), with completed twisting representability (thm:completed-twisting-representability). Coefficient-stability criterion (thm:coefficient-stability-criterion) reduces convergence to finite matrix stabilization. Uniform PBW bridge (thm:uniform-pbw-bridge) connects MC1→MC4. **MC4 SPLITTING**: MC4⁺ (positive towers: W_{1+∞}, affine Yangians, RTT — SOLVED by weight stabilization) vs MC4⁰ (resonant towers: Virasoro, non-quadratic W_N — reduced to finite resonance problem by thm:resonance-filtered-bar-cobar). W_N rigidity (thm:winfty-all-stages-rigidity-closure, 21 conjectures resolved). Remaining example-specific task: coefficient stabilization on finite windows + H-level target identification.
- MC5: **PROVED** — Inductive genus determination + 2D convergence (no UV renormalization needed) + analytic-algebraic comparison + general HS-sewing criterion (thm:general-hs-sewing: polynomial OPE growth + subexponential sector growth implies convergence at all genera). Heisenberg sewing theorem proved (thm:heisenberg-sewing, thm:heisenberg-one-particle-sewing: one-particle Bergman reduction, Fredholm determinant).
- Theta_A: **PROVED** by bar-intrinsic construction (thm:mc2-bar-intrinsic): Θ_A := D_A - d_0 ∈ MC(Def_cyc(A) ⊗̂ G_mod). Shadow algebra A^sh = H_•(Def_cyc^mod). Named shadows (κ, Δ, C, Q) are projections of this single element (cor:shadow-extraction). All-arity master equation = MC equation projected to arity r. Q^contact_Vir = 10/[c(5c+22)]. Scalar saturation proved for all algebraic families (thm:algebraic-family-rigidity) via Whitehead reduction + algebraic semicontinuity; residual conjecture restricted to non-algebraic-family constructions.
- Koszulness characterization programme: recorded in concordance.tex sec:concordance-koszulness-programme. 12 equivalent characterizations K1-K12 of chiral Koszulness (**11 unconditionally proved + 1 conditional**, thm:koszul-equivalences-meta in chiral_koszul_pairs.tex). 11 unconditional: PBW degeneration, A∞ formality, shadow-formality, E₂-formality, curve independence, PBW universality, Barr-Beck-Lurie, FH concentration, FM boundary acyclicity, tropical Koszulness, bifunctor decomposition. Conditional: Lagrangian criterion (K11, thm:lagrangian-koszulness, pending perfectness/nondegeneracy). D-module purity is a 13th characterization, partially proved (forward direction established, converse open).

## Six Frontier Research Directions (raeeznotes85-91)

**Direction 1: Platonic Holographic Programme** (raeeznotes86). Every HT holographic system T should be controlled by a holographic modular Koszul datum H(T) = (A, A!, C, r(z), Θ_A, ∇^hol). Central claim: the dg-shifted Yangian r(z) is the binary genus-0 shadow of Θ_A, i.e. r(z) = Res^coll_{0,2}(Θ_A). Five theorem targets: boundary-defect realization, Yangian-shadow, sphere reconstruction (2026 GZ commuting differentials = scalar shadow of Sh_{0,n}(Θ_A)), quartic resonance obstruction, singular-fiber descent. Modular shadow connection ∇^hol_{g,n} = d − Sh_{g,n}(Θ_A). Deformation-quantization bridge Q_HT: classical coisson → quantum Koszul (Khan-Zeng 3d PVA sigma model).

**Direction 2: Analytic Sewing Programme** (raeeznotes89). The platonic ideal: formal OPE data ⊂ sewing envelope ⇝ Hilbert factorization theory ⇝ coderived shadow invariants. Sewing envelope A^sew = Hausdorff completion for all-amplitude seminorm topology. HS-sewing condition: Σ q^{a+b+c} ‖m^c_{a,b}‖²_HS < ∞ implies trace-class closed amplitudes. Analytic bar coalgebra. Analytic Koszul pair. Heisenberg sewing theorem PROVED (thm:heisenberg-sewing: one-particle Bergman reduction, Fredholm determinant). HS-sewing PROVED for entire standard landscape (thm:general-hs-sewing). Curvature forces coderived passage at genus g ≥ 1. IndHilb-valued conformally flat factorization homology (Moriwaki 2026).

**Direction 3: Factorization-Envelope Technology** (raeeznotes90/91). Pipeline: Lie conformal algebra → factorization envelope → factorization algebra → vertex algebra ≅ enveloping VA (Nishinaka 2025/26, generalizing KM + Virasoro; Vicedo 2025, full/non-chiral). Platonic target: universal modular factorization envelope U^mod_X(L) as left adjoint of modular primitive-current functor Prim_mod. Six-fold package Π_X(L) = (F_X, B̄_X, Θ_L, L_L, (V^br, T^br), R^mod_4). Envelope-shadow functor Θ^env_{≤r}(R). DS reduction as functor on platonic packages: Θ_{W_N} = DS(Θ_{ĝ}).

**Direction 4: Non-Principal W-Algebra Duality** (raeeznotes88). Hook-type in type A is the first genuine proved non-principal corridor (Fehily, Creutzig-Linshaw-Nakatsuka-Sato, 2023-2025). Transport propagation lemma: hook-type seeds + edge-compatibility → transport-closure duality. Type-A transport-to-transpose conjecture: (W_k(sl_N, f_λ))! ≃ W_{k^∨_λ}(sl_N, f_{λ^t}). KEY CORRECTION: arbitrary DS reduction EXISTS (Kac-Roan-Wakimoto); what remains is proving bar-cobar/Koszul commutes with non-principal reduction.

**Direction 5: MC4 Completion Programme** (raeeznotes87). MC4 PROVED. MC4 splits into MC4⁺ (positive towers: solved by stabilization) and MC4⁰ (resonant towers: finite resonance). Resonance rank ρ(A) classifies completion difficulty. Platonic completion conjecture: every positive-energy chiral algebra has ρ < ∞. Virasoro: Vir_{26-c} = depth-zero resonance shadow, not final dual. MC5 now also PROVED (all-genera HS-sewing).

**Direction 6: Strategic Bottleneck** (raeeznotes85). MC1-5 ALL PROVED. The remaining frontier is MC3 extension to arbitrary simple type (conj:mc3-arbitrary-type: Hernandez-Jimbo prefundamental CG for all Dynkin types). The completed inverse-limit bar/cobar problem for non-quadratic, infinite-generator chiral algebras is resolved by the strong completion-tower theorem (MC4). Non-principal W-duality and factorization-envelope technology are the active growth directions.

## Vol II (~/chiral-bar-cobar-vol2)

Five parts: I (Bar Complex -> Swiss-Cheese), II (Descent Calculus), III (Dualities and Bulk-Boundary-Line), IV (Standard Landscape), V (Quantization and Holography).

The bar complex's differential = C-direction factorization. Its coproduct = R-direction factorization. Together: Swiss-cheese algebra on FM_k(C) x Conf_k(R). At genus g >= 1: curved Swiss-cheese with curvature kappa * omega_g.

**Vol II status**: ALL foundational items PROVED. Recognition theorem PROVED (Weiss cosheaf descent, lem:product-weiss-descent). Homotopy-Koszulity of SC^{ch,top} PROVED (via Kontsevich formality + transfer from classical Swiss-cheese). PVA descent D2-D6 ALL PROVED: D2-D5 via repaired geometric proofs (exchange cylinder + three-face Stokes on FM_3(C)); D6 via H3(a) factorization + topological contractibility (no extra hypothesis beyond (H1)-(H4)). Operad⟹axioms (F4) PROVED. Axioms⟹operad (F5, rectification) PROVED via homotopy-Koszulity. Stokes⟹A∞ (FM1) PROVED. Zero conjectural algebraic inputs remain; only the standing physical axioms (H1)-(H4). Cross-volume bridges catalogued in concordance.
