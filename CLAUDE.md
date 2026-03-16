# CLAUDE.md — Modular Homotopy Theory for Factorization Algebras on Curves

## What This Is

Two-volume research monograph by Raeez Lorgat. Vol I (~1,800pp, 70+ active files, ~1,900+ claims) is the algebraic engine: bar-cobar duality for chiral algebras on curves, with the five main theorems proved, a finite-order nonlinear shadow calculus developed through arity 4, and a comprehensive physics landscape (20+ worked examples from Gaiotto et al.). Vol II (~500pp, at ~/chiral-bar-cobar-vol2, 41+ files, ~500+ claims with 100% tag coverage) applies the engine to 3d holomorphic-topological QFT, PVA quantization, and holography.

**Vol I structure**: Overture (Heisenberg atom) + Part I (The Algebraic Engine: Thms A-D+H, HTT, nonlinear shadow tower, branch-line reductions) + Part II (The Standard Landscape: all example families + combinatorial frontier) + Part III (Bridges: Feynman, BV/BRST, YM boundary theory, E_n, Langlands) + Part IV (The Frontier, concordance) + Appendices (3 clusters: Foundations, Nonlinear Technical, Physics Reference).

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

## Three Concentric Rings (the architecture)

**Ring 1** — Proved core: Theorems A-H, MC1/MC2, DK-0 through DK-3, **MC3 thick generation proved** (type A all N), **MC4 closed** (W_N rigidity at all stages, 21 conjectures resolved + Yangian eval-core 249 tests).
**Ring 2** — Nonlinear characteristic layer (the shadow Postnikov tower), FULLY INTEGRATED across Parts I-III. The primary mathematical object is the filtered finite-order engine: Theta_A^{<=2} (kappa), Theta_A^{<=3} (cubic shadow), Theta_A^{<=4} (quartic shadow), ... with obstruction classes o_{r+1}(A) in the cyclic deformation complex. Proved at finite order: kappa for all families, cubic shadows, quartic resonance class with clutching law (via Mok's log FM degeneration). Q^contact_Vir = 10/[c(5c+22)]. Genus-1 Hessian correction delta_H^(1)_Vir = 120/[c^2(5c+22)]x^2. Shadow archetypes computed in every example chapter: Heisenberg=Gaussian/terminates@2, affine=Lie/tree/terminates@3, betagamma=contact/quartic/terminates@4, Virasoro/W_N=mixed (infinite tower, quintic forced). Ambient complementarity = shifted-symplectic Lagrangian geometry, CONDITIONAL on perfectness/nondegeneracy hypotheses. The full unrestricted Theta_A (all arities, all genera) is the conjectural limit of the tower, not its starting point.
**Ring 3** — Physics-facing frontier: W-algebra axis (MC4 W_infty closed unconditionally), Yangian/RTT axis (**MC3 character-level proved**, DK-5 formal once categorical inputs established), holographic/celestial axis (anomaly-completed Koszul duality, M2 example in Vol II).

**Unifying principle**: The modular L∞ convolution algebra g^mod_A is the single organizing structure. It carries a natural modular L∞ structure (from the Feynman transform of the modular operad); the dg Lie algebra (def:modular-convolution-dg-lie) is its strict model. The shadow Postnikov tower is the finite-order projection of the universal MC element Θ_A. The proved content is the finite-order shadow tower: κ (arity 2), cubic shadow C (arity 3), quartic resonance class Q (arity 4), with each level a projection of the next. Theorems A-D+H and the genus expansion are proved projections of the scalar level κ. The full unrestricted MC element Θ_A ∈ MC(g^mod_A) satisfying D·Θ + ½[Θ,Θ] = 0 is the CONJECTURAL limit of the tower — it is the target, not the starting point. The weight filtration on g^mod controls the extension tower; each finite truncation Θ_A^{<=r} is constructive and does not require the full all-genera modular envelope.

## Three-Pillar Foundational Architecture (NEW)

Three preprints force upgrades at three levels. Recorded in concordance.tex sec:concordance-three-pillars.

**Pillar A** (MS24): Primitive local object = homotopy chiral algebra (Ch∞), not strict. Strict chiral algebra appears after rectification. Ch∞ → strict on H^• → PVA/coisson shadow.
**Pillar B** (RNW19+Val16): Universal deformation machine = filtered convolution sL∞-algebra hom_α(C,A). Deformation space = MC ∞-groupoid. dg Lie algebra = strict model. **Key constraint**: hom_α extends to ∞-morphisms in either slot separately but NOT both simultaneously (no-bifunctor obstruction). MC3 categorical lift must proceed one slot at a time.
**Pillar C** (Mok25): Global collision geometry = log FM compactification FM_n(X|D) on snc pairs. Tropicalization = planted forests (G_pf = Trop(FM_n(C|D))). Semistable degeneration formula → clutching laws.

**Seven identification theorems** (5 proved, 2 conjectural):
1. g^mod_A = hom_α(C^!_ch, P^ch) (thm:convolution-master-identification)
2. Θ_A ∈ MC(hom_α) ≅ Tw_α (cor:theta-twisting-morphism)
3. G_pf = Trop(FM_n(C|D)) (thm:planted-forest-tropicalization)
4. B(A) is Ch∞-algebra (thm:cech-hca)
5. B_κ ⊣ Ω_κ is Quillen equivalence (thm:quillen-equivalence-chiral)
6. A^sh is homotopy invariant (thm:shadow-homotopy-invariance)
7. One-slot obstruction constrains MC3 (RNW19 Theorem 6.1)

## The Chriss-Ginzburg Principle (the architecture)

Every algebraic structure in the monograph is a Maurer-Cartan element in a convolution dg Lie algebra. The key objects:

1. **Modular cyclic deformation complex** `Def_cyc^mod(A)` (def:modular-cyclic-deformation-complex in chiral_hochschild_koszul.tex): the ambient home. Differential from graph composition, bracket from stable-curve gluing.
2. **Stable-graph and planted-forest coefficient algebras** `G_st`, `G_pf` (def:stable-graph-coefficient-algebra, def:planted-forest-coefficient-algebra in higher_genus_modular_koszul.tex): the explicit combinatorial heart of g^amb_A.
3. **Shadow Postnikov tower** Θ_A^{<=r}: the proved finite-order truncations. Each level is a graph sum through arity r with obstruction class o_{r+1}(A) in the cyclic deformation complex.
4. **Bar complex as modular operad algebra** (thm:bar-modular-operad in bar_cobar_adjunction_curved.tex): {B^(g,n)(A)} is an algebra over FCom (Feynman transform of commutative modular operad). ∂²=0 at all genera is a formal consequence.
5. **Modular dg-shifted Yangian as pro-MC** (def:modular-yangian-pro in yangians_drinfeld_kohno.tex): Y_T^mod = pronilpotent completion of convolution dg Lie algebra. R_T^mod(z;ℏ) is an MC element.
6. **Shadow algebra** `A^sh` (def:shadow-algebra in higher_genus_modular_koszul.tex): H_•(Def_cyc^mod(A)) as graded commutative ring. Shadows (κ, Δ, C, Q, Sh_r) are graded projections at finite order. The all-arity master equation is the MC equation projected to arity r; convergence of the full tower is conjectural.

The proved core descends from finite-order truncations of the shadow tower. The full equation **D_A Θ_A + ½[Θ_A, Θ_A] = 0** is the conjectural all-arity limit; D²=0 at the convolution level is a THEOREM, but at the ambient level (with planted-forest corrections) D²=0 remains CONJECTURAL (conj:differential-square-zero).

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
**Virasoro**: Self-dual at c=13, NOT c=26. Vir_c^! = Vir_{26-c}.
**FM compactification**: Blowup along diagonals, NOT complement of diagonal.
**Prime form**: Section of K^{-1/2} boxtimes K^{-1/2} (NOT K^{+1/2}).
**QME**: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2).
**d_bracket^2 != 0**: PROVED (all 2048 signs). Full Borcherds d gives d^2=0.
**sl_2 bar H^2 = 5** (not 6; Riordan WRONG at n=2).
**Convolution algebra**: The dg Lie algebra Conv_str(C,P) is a STRICT MODEL of the underlying modular L∞ algebra Conv_∞(C,P). MC moduli coincide; full L∞ needed for transfer, formality, gauge equivalence. Bar-cobar preserves quasi-isos BECAUSE it is a quantum L∞ functor.
**Shadow tower (the primary object)**: The finite-order shadow Postnikov tower Θ_A^{<=r} is the proved content. κ, C, Q are successive projections of this tower. At finite order, define shadows directly from the graph sum and use analytics for computation. The full unrestricted Θ_A is the conjectural all-arity limit — do not present it as already established. When writing about Θ_A at all arities, use conjectural language. When writing about finite-order shadows (κ through quartic), these are proved.
**D²=0**: At the convolution level, D²=0 is a THEOREM (from ∂²=0 on M̄_{g,n}). At the ambient level (with planted-forest corrections), D²=0 is CONJECTURAL (conj:differential-square-zero).
**Three-pillar constraints**: (1) The convolution sL∞-algebra hom_α(C,A) is NOT a strict Lie algebra — it is shifted homotopy Lie with higher brackets ℓ_k (k≥3). The dg Lie is a strict MODEL only. (2) hom_α is functorial in either slot separately but FAILS as a bifunctor in both slots simultaneously (RNW19 §6). MC3 categorical lift must proceed one slot at a time. (3) Log FM compactification FM_n(X|D) ≠ classical FM; requires snc pair (X,D). Ordinary FM is the D=∅ special case.

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

**MC frontier** (MC1-4 resolved; MC3 arbitrary-type + MC5 g>=2 are the remaining frontiers):
- MC1: **PROVED** (PBW concentration, all standard families)
- MC2: **PROVED AT FINITE ORDER** (shadow tower through arity 4, with Def_cyc^mod as explicit ambient algebra). Full all-arity Theta_A is the conjectural limit.
- MC3: **PROVED IN TYPE A** (thm:mc3-type-a-resolution): chromatic filtration + prefundamental CG closure + Efimov completion + DK on compacts. Extension to arbitrary simple type stated as conj:mc3-arbitrary-type (requires Hernández-Jimbo prefundamental CG for all Dynkin types). DK-5 now accessible in type A.
- MC4: **CLOSED** — W_infty unconditional at ALL stages via W_N rigidity (thm:winfty-all-stages-rigidity-closure, 21 conjectures -> ProvedElsewhere). Yangian eval-core verified (249 tests). DK-5 accessible in type A.
- MC5: Genus 0+1 proved; g>=2 requires Costello renormalization (analytic, downstream)
- Theta_A: Defined as graph sum in Def_cyc^mod(A). Shadow algebra A^sh = H_•(Def_cyc^mod). Finite-order shadows (κ through quartic) PROVED. All-arity master equation = MC equation projected to arity r; full convergence CONJECTURAL. Q^contact_Vir = 10/[c(5c+22)].

## Vol II (~/chiral-bar-cobar-vol2)

Five parts: I (Bar Complex -> Swiss-Cheese), II (Descent Calculus), III (Dualities and Bulk-Boundary-Line), IV (Standard Landscape), V (Quantization and Holography).

The bar complex's differential = C-direction factorization. Its coproduct = R-direction factorization. Together: Swiss-cheese algebra on FM_k(C) x Conf_k(R). At genus g >= 1: curved Swiss-cheese with curvature kappa * omega_g.

**Vol II status**: Recognition theorem PROVED. Homotopy-Koszulity of SC^{ch,top} PROVED (via Kontsevich formality + transfer from classical Swiss-cheese). Zero conjectural algebraic inputs remain; only the standing physical axioms (H1)-(H4). All claim status tags at 100% coverage. Cross-volume bridges catalogued in concordance.
