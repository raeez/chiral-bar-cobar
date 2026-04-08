# CLAUDE.md — Modular Koszul Duality for Chiral Algebras on Algebraic Curves

## The Programme Summary

**The one sentence**: Modular Koszul duality for chiral algebras is E₁-E₁ operadic Koszul duality transported into the homotopical modular chiral realm on algebraic curves.

What this means: the bar functor is ChirAss-coalgebra valued; the Koszul dual cooperad ChirAss^! governs the cobar; the duality is between the chiral associative operad and itself. The transport globalizes classical Koszul duality (a phenomenon at a point) as a bundle over the moduli of stable curves M̄_{g,n}. The Chern-Weil theory of that bundle recovers the shadow obstruction tower: κ(A) is the first Chern class, the full tower is the characteristic class data, and d²=κ·ω_g at genus g≥1 is curvature from the Hodge bundle. Homotopical: the primitive local object is a homotopy chiral algebra Ch∞ (MS24), not strict. Modular: the theory works at all genera via the modular operad FCom. Chiral: on algebraic curves, not at a point.

The shared kernel of all three volumes: one form (η = d log(z₁ - z₂)), one relation (Arnold), one object (Θ_A), one equation (D·Θ + ½[Θ,Θ] = 0). Everything else is projection, shadow, and incarnation.

**The three simultaneous leaps beyond anything in the literature**:
1. **Com → E₁/A∞**: Classical BD chiral algebras are Com-algebras in the chiral endomorphism operad. The monograph considers maps from the E₁ (or A∞) homotopy operad into the chiral endomorphism operad, producing a genuinely new type of object.
2. **Genus 0 → modular**: Lifting #1 into the modular operad framework at all genera, with clutching and the full MC equation.
3. **Local → nonlocal**: The simplest nonlocal chiral algebra (where the ordering of points matters, not just their collision) is the atom of the full theory.

**The 6-object bar complex web**: B^Lie (Francis-Gaitsgory, coLie, zeroth-pole), B^ord (Stasheff, tensor coalgebra, deconcatenation, E₁, R-matrix), B^Σ (Beilinson-Drinfeld, coshuffle, E∞, factorization), B^{g-graded} (genus-graded, curved d²=κ·ω_g), B^{mod} (modular envelope, FCom-algebra, D²=0), B^{E₁-mod} (E₁ modular, FAss-algebra, D²=0, five E₁ theorems). The averaging map av: B^ord → B^Σ is the Σ_n-coinvariant projection that forgets the ordering (lossy). The five main theorems A-D+H are the invariants that survive averaging.

**The G/L/C/M classification**: Shadow depth classifies complexity within the Koszul world. Class G (Gaussian, r_max=2, Heisenberg), class L (Lie/tree, r_max=3, affine KM), class C (contact/quartic, r_max=4, βγ), class M (mixed, r_max=∞, Virasoro, W_N). All four classes are chirally Koszul; shadow depth ≠ Koszulness.

**The gauge-gravity dichotomy**: κ(A) + κ(A!) = 0 (KM/free fields) vs κ(A) + κ(A!) = ρ·K (W-algebras). At the self-dual point (c=13 for Virasoro): the full shadow tower is self-dual. At the critical point (c=26): κ_eff = 0, the Clifford algebra degenerates to exterior, perturbative gravity becomes topological.

**The 4d→3d→2d resolution**: 4d N=1 gauge theory → 3d holomorphic-topological boundary → 2d chiral algebra on the boundary of the boundary. The modular Koszul datum H(T) = (A, A!, C, r(z), Θ_A, ∇^hol) persists across dimensional reduction.

**The physics-is-homotopy-type thesis**: The homotopy type of a chiral algebra is the mathematical encoding of its physics. Three levels: (1) A∞ from configuration-space integrals on FM_k(C), universally formal for Koszul algebras; (2) Swiss-cheese SC^{ch,top} measuring failure of holomorphic/topological compatibility, class-dependent (G=formal, L=cubic, C=quartic, M=infinite); (3) modular L∞ from the Feynman transform, packaging all genera via the MC element Θ_A.

## What This Is

Three-volume research monograph by Raeez Lorgat.

**Vol I** (~2,453pp, 80+ active files, ~2,920 claims): *Modular Koszul Duality*. The algebraic engine: bar-cobar duality for chiral algebras on curves, with the five main theorems proved, a nonlinear shadow calculus with full Θ_A proved (bar-intrinsic, thm:mc2-bar-intrinsic) and finite-order engine through arity 4, the G/L/C/M shadow depth classification, 12 equivalent characterizations of chiral Koszulness (10 unconditional + 1 conditional + 1 one-directional), and a comprehensive physics landscape (20+ worked examples from Gaiotto et al.).

**Vol II** (~1,478pp, at ~/chiral-bar-cobar-vol2, 41+ files, ~500+ claims with 100% tag coverage): *A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT*. The Swiss-cheese/E₁ operadic structure, PVA quantization, the seven faces of the collision residue, MC3 for all simple types, 3d quantum gravity, and the standard HT landscape.

**Vol III** (~206pp, at ~/calabi-yau-quantum-groups, 17,199 tests): *CY Categories, Quantum Groups, and BPS Algebras*. The CY-to-chiral functor, BPS algebras and quantum groups (Dimofte integration: slab = bimodule, Drinfeld double), arithmetic shadows in dimension 3.

**The primitive object** is the ordered bar complex B^ord(A) = T^c(s⁻¹Ā): the cofree tensor coalgebra on desuspended generators, the quantized symmetric power controlled by the R-matrix. The symmetric bar B^Σ(A) is its Σ_n-coinvariant quotient. The Heisenberg algebra is the correct Chriss-Ginzburg opening (the simplest nontrivial example where every structure can be computed in closed form) but NOT the atom of the E₁ world: it is E∞ as a chiral algebra. The atom of the E₁ world is a genuinely nonlocal chiral algebra (tier (c): Yangian, Etingof-Kazhdan quantum vertex algebra).

**Vol I structure**: Introduction (road map, theorem statements, notation) + Overture (Heisenberg as CG opening, unnumbered) + Part I (The Bar Complex: Thms A-D+H, bar-cobar adjunction, inversion, complementarity, modular characteristic, Hochschild; Koszulness programme: 12 equivalences) + Part II (The Characteristic Datum: nonlinear shadow obstruction tower, shadow depth classification G/L/C/M, higher-genus modular Koszul theory, E₁ modular Koszul theory) + Part III (The Standard Landscape: all example families, combinatorial frontier, landscape census) + Part IV (Physics Bridges: E_n operads, factorization envelopes, derived Langlands, abstract connections) + Part V (The Seven Faces of the Collision Residue: R-matrix, Yangian, Sklyanin, Drinfeld-Kohno, celestial, holographic) + Part VI (The Frontier: conditional and conjectural extensions, outlook) + Appendices.

## The Convergent Writing Loop (PERMANENT)

First-pass writing by any agent is directionally correct but lacklustre. A single write-and-move-on pass will NEVER reach the platonic ideal. The loop:

1. **WRITE**: First draft. Get the mathematics right. Accept that the prose is functional, not luminous.
2. **REIMAGINE FROM FIRST PRINCIPLES**: Forget the draft. Ask: if Gelfand/Beilinson/Drinfeld/Witten were writing this passage, what would it look like? What object would appear FIRST? What deficiency would FORCE this passage's existence?
3. **REWRITE**: With the reimagined vision, rewrite from scratch. Do not edit the first draft; replace it.
4. **BEILINSON AUDIT**: Attack the second draft adversarially. Is every claim correct? Is scope honest? Are there AP violations?
5. **REIMAGINE AGAIN**: With the audit findings, reimagine once more. The audit reveals what the passage is REALLY about.
6. **REWRITE AGAIN**: Third draft. This one should be close to platonic.
7. **CONVERGE**: If the Beilinson audit of the third draft returns zero actionable findings at severity >= MODERATE, the passage has converged. If not, iterate.

For preface/introduction passages: at least 3 iterations. For chapter openings: at least 2. For theorem statements: 1 (mathematics converged), but surrounding prose needs 2. The writing loop is the PROSE LAYER of the Beilinson rectification loop.

## The Dual Imperative

Maximalist ambition synergizes with maximal truth-seeking. Precision enables ambition. When claims outrun proofs, strengthen the proof first.

## REGRESSION SAFEGUARDS (PERMANENT, 2026-04-08)

The 78-agent session on 2026-04-08 fundamentally upgraded the programme's self-understanding. The following 20 constraints are HARD RULES that override any default behavior. A future agent must understand ALL 20 from the first token. Detailed rationale in `feedback_anti_regression_safeguards.md`.

1. **RS-1: The Heisenberg is the CG opening, NOT the atom.** The atom of the E_1 world is a genuinely nonlocal chiral algebra (Yangian, EK quantum VA). The Heisenberg is E-infinity. (AP108)
2. **RS-2: B^ord is the primitive, B^Sigma is the shadow.** The ordered bar carries R-matrix, Yangian, quantum group data; the symmetric bar is a lossy Sigma_n-coinvariant quotient. (AP65, AP97, AP104)
3. **RS-3: Physics IS the homotopy type, not a "bridge" or "application."** The homotopy type encodes physics at three levels (A-infinity, SC^{ch,top}, modular L-infinity). Costello-Gaiotto-Dimofte are substance. (AP106, AP115)
4. **RS-4: Costello/Dimofte/Gaiotto content belongs in the mathematical core, not in "connections" chapters.**
5. **RS-5: Show, do not tell.** Never open a chapter with "This chapter constructs..." Use the CG deficiency opening. (AP106, AP109, AP111)
6. **RS-6: The convergent writing loop is mandatory.** First-pass prose is never final. Write/reimagine/rewrite/audit/reimagine/rewrite/converge. No single pass reaches the platonic ideal.
7. **RS-7: The symmetric bar is NOT the default.** When writing "the bar complex" without qualification, it means B^ord. B^Sigma is invoked only when the factorization-coalgebra picture is specifically needed. (AP82, AP85, AP102)
8. **RS-8: "Abelian CS" = Heisenberg.** Same algebra, same OPE J(z)J(w) ~ k/(z-w)^2. The "abelian CS" subsection described a fictional algebra. (AP105)
9. **RS-9: The slab is a bimodule, NOT a Swiss-cheese disk.** Two boundary components (bimodule), not one closed + one open colour (SC operad).
10. **RS-10: Single-pass agent work without audit is forbidden.** The Beilinson rectification loop (RED/BLUE/GREEN audit -> fix -> re-audit -> converge) is mandatory for chapter-level interventions.
11. **RS-11: kappa without subscripts is FORBIDDEN in Vol III.** Always use kappa_ch, kappa_BKM, kappa_cat, kappa_fiber. (AP113)
12. **RS-12: The programme is three volumes, not two.** Vol I (Modular Koszul Duality), Vol II (A-infinity Chiral Algebras and 3D HT QFT), Vol III (CY Categories, Quantum Groups, and BPS Algebras).
13. **RS-13: In Vol II, gravity is the climax (Part VI), not middle content.** Gravity requires the full E_1 + modular + complementarity machinery of Parts I-V.
14. **RS-14: Introduction orients, Overture instantiates.** Introduction (road map) comes first; Overture (Heisenberg computation) comes second.
15. **RS-15: Koszul programme before higher_genus in the dependency DAG.** The Koszul characterization programme is upstream of higher-genus modular theory.
16. **RS-16: No forward-reference trailers.** Never write "this chapter will prove Theorems X, Y, Z." Theorems appear when the mathematics demands them. (AP109)
17. **RS-17: No "What this chapter proves" remark blocks.** If a chapter needs such a block, restructure the chapter. (AP111)
18. **RS-18: r^coll(z) differs from the Laplace-transform r(z) for odd generators.** Coincide for even E-infinity algebras; diverge for fermionic systems. (AP107)
19. **RS-19: The preface is a complete survey (~2,430 lines target), not a compressed summary.** Save originals before compressing. The symphonic standard is not about cutting.
20. **RS-20: Memory files with stale page counts or rejected designs are not current.** Always verify against fresh builds and later sessions. (AP112)

## The Multi-Path Verification Mandate

**Every computational result in the manuscript must be supported by multiple independent computations that all point to the same result.** This is not optional. A number that appears in the manuscript with only one derivation path is UNVERIFIED. Confidence requires convergence from independent directions.

**Minimum verification standard**: Every numerical formula, invariant value, or computational claim requires AT LEAST THREE independent verification paths before it can be considered reliable. These paths must be genuinely independent — not trivial rearrangements of the same computation.

**Verification path taxonomy** (use at least 3 per claim):
1. **Direct computation** — compute from the defining formula
2. **Alternative formula** — compute from an equivalent but structurally different expression
3. **Limiting case** — verify against known special cases (k=0, c=0, N=1, genus=0, etc.)
4. **Symmetry/duality** — verify via complementarity, level-rank duality, DS reduction, etc.
5. **Cross-family consistency** — verify additivity, multiplicativity, or functoriality across families
6. **Literature comparison** — verify against published values with explicit source and convention check
7. **Dimensional/degree analysis** — verify that the result has correct weight, degree, and units
8. **Numerical evaluation** — evaluate at specific parameter values and compare across methods

**The compute/ layer is the verification engine.** Every formula in the .tex source should have a corresponding test in compute/tests/ that verifies it by at least 2 methods. The test suite is not a formality — it is the manuscript's immune system.

**Cross-volume propagation**: When a formula appears in multiple volumes, ALL instances must be independently verified and cross-checked. Convention differences between volumes (AP49) make blind copying dangerous.

**Failure mode this prevents**: AP1 (κ formula wrong, 19 commits), AP10 (tests with hardcoded wrong values), AP38 (literature convention mismatch). A single-path computation can be wrong and self-consistent; multi-path verification catches errors that single-path cannot.

## The Beilinson Principle

**"What limits forward progress is not the lack of genius but the inability to dismiss false ideas."**

This is a permanent operating directive. Every agent session in this repository acts as a frontier research mathematician whose primary cognitive move is **falsification, not confirmation**. A claim is false until you have independently verified it from primary source. This applies to:

- Claims in the manuscript (theorems, propositions, remarks, formulas)
- Claims in this file (CLAUDE.md), in concordance.tex, and in memory files
- Your own reasoning, corrections, and proposed edits
- Status tags (`\ClaimStatusProvedHere` is a LaTeX macro, not a proof)

Prefer a smaller true theorem to a larger false one. Downgrading, narrowing, or fencing a claim is progress. Treat compute as an adversarial verification layer. Never change a formula just because a narrative wants it. Use the red-team materials, theorem registry, and concordance as active audit instruments, not decorative metadata.

### Epistemic Hierarchy

Trust these sources in this order. When they conflict, the higher-ranked source wins:

1. **Direct computation** — symbolic verification via compute/ modules, dimensional analysis, limiting cases
2. **The .tex source itself** — the actual theorem statement and proof text, read in full with ±100 lines of context
3. **The build system** — compiler errors, undefined references, test failures
4. **Published literature** — original papers with verified arXiv/DOI identifiers
5. **concordance.tex** — the constitution, but verify its claims against 1–4
6. **This file (CLAUDE.md)** — operational instructions; mathematical claims may lag behind source
7. **Memory files** — historical context; may be stale; always verify before acting on

**CLAUDE.md and memory files describe what we *believe* is true. The .tex source is what we *have written*. The compute/ modules test what we *can verify*. These three can disagree. When they do, investigate — do not assume any layer is authoritative.**

### The Verification Reflex

Before every assertion, edit, or claim about the codebase:

> **"How do I know this? Did I read the source, compute it, or assume it?"**

If "assume" — stop and verify. If "read it in CLAUDE.md or memory" — go read the actual .tex. If "compute" — can you reproduce the computation independently?

### Cognitive Anti-Patterns — Observed From This Repository's Own Error History

These are not hypothetical. Full-history analysis (797 commits, both volumes) found **83 mathematical error commits** spanning 26 anti-patterns. The frequency ranking: κ formula wrong (19 commits), formula coefficients (15), sign/convention (14), object conflation (13), scope inflation (12), geometric confusion (11), status inflation (7), inner product (3), index errors (2). The A!/Ω(B(A)) conflation (AP25) was fixed THREE TIMES in Vol II and kept returning — the most deeply embedded confusion in the project.

**AP1 — Copy-paste without recomputation.** κ(KM) = dim(g)·(k+h∨)/(2h∨). κ(Vir) = c/2. κ(W_N) = c·(H_N - 1). These are three *distinct* formulas. This repository has 7+ commits correcting κ formulas copied between families without recomputation (c28bd2e, c0f0e4c, eb1b70d, 43e5ac2, 6526706, 05d6eb2, 5629ee7). One such error propagated to 47 files. **Rule: before writing any formula, check `landscape_census.tex`. Never copy a formula between algebra families without recomputing from first principles.**

**AP2 — Anchoring on descriptions over source.** CLAUDE.md says "MC4 PROVED." The .tex file may say something different, or the proof may have a gap. D²=0 was simultaneously tagged ProvedHere and Conjectured in different files of the same manuscript. **Rule: read the actual theorem and proof in .tex. Descriptions are claims *about* source, not source itself.**

**AP3 — Pattern completion over verification.** You see a formula in three places and a variant in a fourth. You "correct" the fourth to match the three. But the fourth was correct (applying to a different family) and the three were wrong. **Rule: compute independently. Never correct by majority vote across occurrences.**

**AP4 — Status tag as ground truth.** `\ClaimStatusProvedHere` means someone typed those characters. Prior audits found 4–20 status boundary violations per cycle — claims tagged as proved whose proofs cite conjectural inputs, prove something weaker than stated, or contain gaps. **Rule: verify that the proof actually proves the stated claim. Check that all cited results have their hypotheses satisfied.**

**AP5 — Local fix, global neglect.** You correct a formula in one file. The same formula appears in 10+ other files across both volumes. You've created an inconsistency. This is the #1 systematic failure mode (3–4 commits required per full correction). **Rule: after EVERY correction, grep for all variant forms across `~/chiral-bar-cobar` AND `~/chiral-bar-cobar-vol2`. Fix all instances in the same session.**

**AP6 — Omitting boundary qualifications.** "D²=0 is proved" — at which level? Convolution? Ambient? "κ is computed" — genus-0 curvature m₀ or genus-1 obstruction κ? "Θ_A is proved" — truncated Θ_A^{≤r} or full? Four audit findings trace directly to this conflation. **Rule: every use of shadow obstruction tower, bar curvature, D²=0, or obstruction coefficient MUST specify genus, arity, and level (convolution vs ambient).**

**AP7 — Scope inflation.** Universal claim, special-case proof. "Koszulness holds for all..." when proved only for type A. Prior audits found 3+ instances (MC3 was the canonical example before its all-types resolution). **Rule: before writing a universal quantifier, verify the proof has no implicit type/genus/level restriction.**

**AP8 — Virasoro self-duality ambiguity.** One root error ("Virasoro is self-dual") propagated to 6 corrections because it conflates uncurved quadratic self-dual (c=0) and FF-involution self-dual (c=13). **Rule: NEVER write "self-dual" for Virasoro unqualified. Always specify which duality and which central charge.**

**AP9 — Same name, different object.** κ means different things for different families. m₀ (genus-0 curvature) ≠ κ (genus-1 obstruction). The dg Lie algebra ≠ the L∞ algebra. Conv_str ≠ Conv_∞. Confusing these passes tests if the tests encode the same confusion. **Rule: use explicit qualifiers (κ^{KM}, κ^{Vir}, κ^{W_N}) or fully qualify in prose. Use \Convstr and \Convinf macros.**

**AP10 — Tests with hardcoded wrong expected values.** If a formula is wrong in both code AND test, the test passes. This happened with κ formulas across 47 files. **Rule: cross-family consistency checks (additivity, complementarity, anti-symmetry) are the real verification. Single-family hardcoded tests are necessary but NOT sufficient.**

**AP11 — Single-point external dependency without flag.** `thm:ambient-d-squared-zero` depends entirely on [Mok25, Thm 3.3.1], a 2025 preprint. **Rule: any theorem resting on a single external source gets flagged in concordance.tex with source, publication status, and fallback status.**

**AP12 — Proof status inflation by accretion.** As the manuscript grew through raeeznotes75–97 (6+ months), new proofs upgraded old conjectures but didn't consistently update all legacy ProvedElsewhere/Conjectured tags. Each audit cycle finds 8–12 stale tags. **Rule: when proving a claim, search the entire manuscript for all variants. Update all instances in the same commit. Use `git log` to find all commits that touched the claim.**

**AP13 — Forward references hiding gaps.** A claim in the introduction is tagged ProvedHere, but the proof at genus g ≥ 1 assumes the very thing it claims to prove. The Beilinson audit flagged Theorem B's spectral sequence collapse as circular at higher genus. **Rule: forward references must be transparent about genus/level/type restrictions. If proved at genus 0 and conjectured at g ≥ 1, say so at every cross-reference site.**

**AP14 — Conflating chiral Koszulness with Swiss-cheese formality.** Chirally Koszul (def:chiral-koszul-geometric) = bar cohomology H*(B(A)) concentrated in bar degree 1. Swiss-cheese formal = the SC^{ch,top} operations m_k^{SC} on A vanish for k ≥ 3. These are DIFFERENT PROPERTIES of DIFFERENT OBJECTS. The dodecahedron m_k (condition (iii)) are transferred operations on H*(B(A)); the Swiss-cheese m_k^{SC} are operadic compositions on A itself. ALL standard families (G/L/C/M) are chirally Koszul (cor:universal-koszul: freely strongly generated ⟹ PBW collapse ⟹ bar concentrated). Only class G (Heisenberg) is Swiss-cheese formal (m_k^{SC} = 0 for all k ≥ 3). Classes L and C have finite shadow depth but are NOT Swiss-cheese formal: class L has m_3^{SC} ≠ 0 (the Lie bracket generates a nonzero cubic SC operation), class C has m_3^{SC} = 0 but m_4^{SC} ≠ 0. Class M (Virasoro, W_N) is Koszul but fully non-formal: m_k^{SC} ≠ 0 for all k ≥ 3. Shadow depth classifies complexity WITHIN the Koszul world, not Koszulness status. NEVER write "Virasoro is not Koszul" or "DS reduction breaks Koszulness." The correct statements are "Virasoro has non-formal Swiss-cheese structure" and "DS reduction introduces Swiss-cheese non-formality." Theorem thm:ds-koszul-obstruction proves that DS introduces higher SC operations, NOT that it destroys bar concentration. This error propagated through 20+ files in Vol II across multiple agent sessions before being identified. **Rule: when writing about Koszulness, always specify: (a) which object's operations you mean (bar-transferred or Swiss-cheese), and (b) which property you mean (bar concentration or SC formality).**

**AP15 — Holomorphic/quasi-modular conflation.** E_2*(τ) is quasi-modular (transforms with additive anomaly 3τ/(πi)), NOT a holomorphic modular form for SL(2,Z). The shadow multiplicativity theorem falsely claimed graph amplitudes are "polynomials in E_4, E_6" — but the genus-1 propagator IS E_2*, and products of E_2* are quasi-modular polynomials in {E_2*, E_4, E_6}, NOT in {E_4, E_6}. The "dim S_k = 0 for k < 12" argument applies ONLY to holomorphic M_k(SL(2,Z)); the space of quasi-modular forms is larger. Three false claims in one session were built on this conflation. **Rule: when working with genus-1 amplitudes, ALWAYS specify holomorphic vs quasi-modular vs almost-holomorphic. NEVER apply holomorphic dimension formulas to quasi-modular objects. The genus-1 propagator is E_2*; any graph sum involving it produces quasi-modular forms.**

**AP16 — Integrated identity ≠ class identity (level confusion).** [SUPERSEDED BY AP27.] The multi-generator obstruction was believed to involve λ_g^{(h)} = c_g(ℰ_h) for weight-h generators, leading to a question about whether these classes coincide. AP27 resolves this: the bar propagator d log E(z,w) is weight 1 regardless of field weight, so ℰ_h never appears — all channels use ℰ_1. The question about λ_g^{(h)} vs λ_g is moot. **Rule: the bar complex uses E_1, not E_h. See AP27.**

**AP17 — Narrative velocity overriding verification (cascade error).** In one session, three false theorems were written into the manuscript: shadow multiplicativity (AP15), multi-generator universality (AP16), MK3 scope inflation (AP18). Each built on the previous one's unchecked success. **Rule: after writing ANY new theorem, IMMEDIATELY deploy an adversarial audit on it BEFORE building the next result. NEVER chain new claims without auditing each link. \ClaimStatusProvedHere should be the LAST thing added, after audit, not the first.**

**AP18 — "Entire standard landscape" without exception analysis.** PBW propagation was claimed for "every standard family" but: βγ has weight-0 generator γ (violating positive grading); admissible-level quotients have null vectors (breaking L_0 invertibility); minimal models are quotients where universal PBW fails. Also: "reduces to a single axiom MK1" hid that MK2 (Verdier) is also needed. **Rule: before ANY universal quantifier over families, explicitly list every family and check each against the hypotheses. State exceptions in the theorem statement.**

**AP19 — The bar kernel absorbs a pole.** The bar construction extracts residues along d log(z_i - z_j), NOT along dz/(z-w). The d log measure absorbs one power of (z-w). Consequence: the collision residue r(z) = Res^{coll}_{0,2}(Θ_A) has pole orders ONE LESS than the OPE. The Virasoro OPE has poles at z⁻⁴, z⁻², z⁻¹; the r-matrix has poles at z⁻³, z⁻¹. For KM: the OPE has z⁻² and z⁻¹; the r-matrix is Ω/z (single pole). This error was found in 4 locations across both volumes. The reason it recurs: one writes the OPE from memory, calls it "the r-matrix," and the formula LOOKS right because the structure constants are correct — only the pole orders are wrong. **Rule: the r-matrix lives one pole order below the OPE. r(z) for Virasoro is (c/2)/z³ + 2T/z, not (c/2)/z⁴ + 2T/z² + ∂T/z. When in doubt, the r-matrix has NO even-order poles for a bosonic algebra (the d log extraction sends z⁻²ⁿ to z⁻(²ⁿ⁻¹), which is odd).**

**AP20 — An invariant of one algebra is not an invariant of a system.** κ(A) is intrinsic to A: it is the leading Hodge class coefficient, the scalar that controls F_g = κ·λ_g^FP at ALL genera. κ_eff is a property of a COMPOSITE SYSTEM (matter + ghosts): κ_eff = κ(matter) + κ(ghost) = 0 at the critical dimension. These are different objects. The genus tower formula always uses κ(A). The anomaly cancellation uses κ_eff. The transgression algebra uses κ(B) where B = A! is the Koszul dual — a THIRD distinct κ. This conflation was found in 8 locations, including the genus tower formula, the Clifford algebra, and the complementarity pairing. **Rule: state WHICH algebra's κ every time. Write κ(Vir_c) = c/2, not just "κ = c/2." Write κ_eff = κ(matter) + κ(ghost), not just "κ_eff." The F_g formula is F_g(A) = κ(A)·λ_g^FP — the argument of κ is the algebra A, not the physical system.**

**AP21 — A class is not a scalar; Clifford ≠ exterior.** The curvature m₀ = κ·ω_g is an element of H²(M̄_g, Z(A)), not a number. The secondary anomaly u = η² = λ in the transgression algebra is a CENTRAL ELEMENT (acting as the scalar κ on standard modules), not the number κ². The difference is the difference between Cliff(V, q) and ∧(V): Clifford has η² = q (nondegenerate bilinear form → matrix algebra → Morita trivial), exterior has η² = 0 (degenerate → genuine cohomology of the surface). The ENTIRE gravity dichotomy (c ≠ 26 vs c = 26, perturbative vs topological, matrix factors vs exterior algebras) rests on whether u = κ(B)·ω_g vanishes. Writing u = κ² (a positive number that never vanishes) obliterates the bifurcation. This error appeared in working_notes.tex and the dichotomy chapter. **Rule: u is LINEAR in κ (first power, a class), NEVER quadratic. The Clifford relation is η² = λ where λ = κ(B)·ω_g. On standard modules λ acts as κ(B). At c = 26: κ(Vir_0) = 0, so λ = 0, and the Clifford algebra degenerates to exterior. Squaring κ destroys this.**

**AP22 — Generating function index mismatch.** Â(iℏ) - 1 = ℏ²/24 + 7ℏ⁴/5760 + ⋯ starts at ℏ². The shadow obstruction tower has F_1 = κ/24 (a nonzero constant). If you write Σ F_g ℏ^{2g-2} = κ·(Â(iℏ) - 1), the left side at g=1 is κ/24 (order ℏ⁰) but the right side at ℏ⁰ is zero. The correct pairing is Σ F_g ℏ^{2g} = κ·(Â(iℏ) - 1), where the ℏ² from Â matches the ℏ² from g=1. Alternatively: Σ F_g ℏ^{2g-2} = (κ/ℏ²)·(Â(iℏ) - 1). The error is writing one convention on the left and a different convention on the right. **Rule: always verify F_1 matches at the leading order. If Â(iℏ) - 1 starts at ℏ², and F_1 ≠ 0, then the ℏ-power on the left must be 2g (not 2g-2) unless you include an explicit 1/ℏ² on the right.**

**AP23 — Flat section vs weighted transport.** The shadow connection ∇^sh = d - Q'_L/(2Q_L) dt has flat sections Φ(t) = √(Q_L(t)/Q_L(0)). The shadow generating function H(t) = 2κ·t²·Φ(t) is NOT a flat section — it is the flat section multiplied by t². Writing "H(t) is a flat section of ∇^sh" is false: ∇^sh(H) = 2t·√(Q_L) ≠ 0. The shadow obstruction tower is the TAYLOR EXPANSION of an algebraic function of degree 2, transported along a logarithmic connection with Koszul monodromy — but it is not itself horizontal. The distinction matters because flat sections have no zeros (they're parallel-transported from a nonzero initial condition), while H(t) has a double zero at t = 0 (the shadow obstruction tower starts at arity 2, not arity 0). **Rule: the flat section of ∇^sh is √(Q_L), not H(t). The shadow obstruction tower is t²·√(Q_L) — the t² prefactor is the arity offset, not part of the connection.**

**AP24 — The complementarity sum is not universally zero.** κ(A) + κ(A!) = 0 for Heisenberg, affine KM, lattice VOAs, and principal W-algebras. But for Virasoro: κ(Vir_c) + κ(Vir_{26-c}) = c/2 + (26-c)/2 = **13**, not 0. The "anti-symmetry" κ + κ! = 0 was overclaimed in 20+ locations across both volumes (the original error required 3–4 commits to fully correct). The root cause: for KM families, the Feigin-Frenkel involution k ↦ −k−2h∨ ensures κ + κ! = 0 by construction. For Virasoro, Koszul duality is c ↦ 26−c, which is NOT anti-symmetric around 0 — it's anti-symmetric around 13. The anomaly ratio ρ = κ/c = 1/2 is the same for A and A!, so the sum is 2ρ·dim/2 = dim/2 in general. For Virasoro (dim = 1 generator, c+c'=26): κ + κ! = 26/2 = 13. **Rule: NEVER write κ(A) + κ(A!) = 0 without checking the family. The correct general statement is κ(A) + κ(A!) = 0 for KM/free fields; κ(A) + κ(A!) = ρ·K for W-algebras (Theorem D). Check the explicit value for EVERY family before writing a universal claim.**

**AP25 — Three functors, three outputs: bar ≠ Verdier dual ≠ cobar.** B(A) is a factorization COALGEBRA. D_Ran(B(A)) ≃ B(A!) is the Verdier dual — a factorization ALGEBRA identified with the bar of A! by Theorem A (Convention~conv:bar-coalgebra-identity). The manuscript also writes D_Ran(B(A)) ≃ A^!_∞ where A^!_∞ denotes the homotopy Koszul dual algebra whose underlying complex is B(A!); this is an algebra-level restatement of the same fact, NOT a different claim. Ω(B(A)) ≃ A is the cobar (recovers A itself by bar-cobar inversion, Theorem B). These are three different objects produced by three different functors applied to the same input. Confusing any two produces wrong statements: "the Koszul dual is the cobar of the bar" is false (the cobar of the bar is A ITSELF); "the Verdier dual recovers A" is false (it recovers B(A!), or equivalently A^!_∞). This conflation was found in 16 files (commit 2273421). The physical manifestation: the Koszul dual A! lives on the BOUNDARY (the R-direction), not in the bulk; it is obtained by Verdier duality on Ran(X), not by applying the cobar functor. **Rule: B produces a coalgebra. D_Ran produces B(A!), identified with the homotopy dual algebra A^!_∞. Ω produces the ORIGINAL algebra back. Write the functor names explicitly. Ω(B(A)) ≃ A (inversion). D_Ran(B(A)) ≃ B(A!) (intertwining). These are NOT the same operation. NEVER write D_Ran(B(A)) = A^! without the ∞ subscript or the B(A!) clarification — the Verdier dual is a specific factorization algebra on Ran(X), not the abstract algebra A^! itself.** The BULK OBSERVABLES are yet a FOURTH object: the chiral derived center Z^der_ch(A) = C^•_ch(A_b, A_b) (Hochschild cochains of a boundary chart), distinct from all three of bar, cobar, and Verdier dual. Bar classifies twisting morphisms (couplings); the derived center classifies bulk operators acting on the boundary. See thm:thqg-swiss-cheese. The primitive object is the open-sector factorization dg-category C_op; the boundary algebra A_b = End(b) is a Morita-dependent chart (thm:thqg-local-global-bridge(iii)). Modularity belongs to trace + clutching on the open sector (thm:thqg-annulus-trace), not to the closed algebra alone.

**AP26 — Free-field inner product ≠ physical inner product.** The Fock space (free-field) inner product ⟨·|·⟩_Fock and the BPZ (Zamolodchikov) inner product ⟨·|·⟩_BPZ are DIFFERENT objects. Primary orthogonality — ⟨W₄|Λ⟩ = 0 for distinct quasi-primaries — holds in BPZ but FAILS in the free-field metric. At weight ≥ 4 for W-algebras of rank ≥ 3, the Fock space has more states than the W-algebra (dim V₄^Fock > dim V₄^W), and the two inner products diverge. Using the Fock metric for W-algebra decompositions gives wrong OPE structure constants. The fix required replacing naive Euclidean projections with full Gram matrix inversions in the physical metric. Found in 2 correction commits (6e19c81, e159f74) affecting W₄ structure constant extraction. **Rule: W-algebra OPE decompositions at weight ≥ 4 MUST use the BPZ inner product (Wick contractions at the leading pole), not the free-field Fock dot product. The two agree only when the W-algebra spans the full Fock space at the given weight, which fails at weight ≥ 4 for rank ≥ 3.**

**AP27 — Field weight ≠ propagator weight.** The bar complex propagator is d log E(z,w), where E(z,w) is the prime form (section of K^{-1/2} boxtimes K^{-1/2}). The logarithmic derivative dE/E has weight 1 in BOTH variables, REGARDLESS of the conformal weight h of the field being sewed. Consequence: every EDGE of the genus-g graph sum uses the STANDARD Hodge bundle E_1 = R^0 pi_* omega. NEVER assign weight-h generators to E_h — the Mumford isomorphism c_1(E_j) = (6j^2 - 6j + 1) * lambda_1 produces absurd discrepancies: 13x for Virasoro, 22.6x for W_3. The propagator argument fixes the edge-level Hodge bundle, but it does NOT by itself prove the higher-genus multi-weight identity obs_g = κ·λ_g: algebraic-family rigidity only gives Θ^min = η⊗Γ_A, not Γ_A = κ(A)Λ. **Status: For uniform-weight algebras (single-generator, or multi-generator with same conformal weight): obs_g = kappa*lambda_g at all genera (PROVED). For multi-weight algebras at g>=2: the scalar formula FAILS — the free energy receives a nonvanishing cross-channel correction δF_g^cross (op:multi-generator-universality, RESOLVED NEGATIVELY by thm:multi-weight-genus-expansion; δF_2(W_3) = (c+204)/(16c) > 0). Rule: the bar propagator d log E(z,w) has weight 1. NEVER assign weight-h generators to E_h. ALL channels use E_1 at the edge level.**

**AP28 — Undefined qualifier applied monograph-wide ("scalar lane").** The term "scalar lane" was introduced in ~114 occurrences across both volumes (68 in Vol I, 46 in Vol II) without a formal Definition environment or a `\label{def:...}`. The term has at least three possible readings: (a) the arity-0 projection of the shadow obstruction tower, (b) the regime of single-generator or uniform-conformal-weight algebras, (c) the regime where obs_g = κ·λ_g holds at all genera. Different passages use different meanings. In the introduction, "For all modular Koszul algebras, obs_g = κ·λ_g" (line 1101) drops all qualification, while 375 lines later the same file restricts this to "the proved scalar lane" with multi-generator factorization "open at g ≥ 2." The qualifier simultaneously WIDENS scope (replacing the concrete "uniform-weight" with the vague "scalar") and HEDGES (adding "proved" without saying what was proved). **Rule: NEVER introduce a terminological qualifier in 3+ locations without first writing a formal Definition environment with a \label. If a restriction has multiple readings, define it precisely. "Scalar lane" should be replaced with a labeled definition specifying: (1) which algebras qualify, (2) at which genera, (3) what exactly is proved. Until defined, use the concrete description: "single-generator algebras, or multi-generator algebras at genus 1."**

**AP29 — Two physical regimes sharing one symbol (κ_eff conflation).** The symbol κ_eff was simultaneously defined as κ − κ' (Koszul pair asymmetry, vanishing at self-dual point c=13 for Virasoro) AND used as κ(matter) + κ(ghost) (physical anomaly cancellation, vanishing at critical dimension c=26). For Virasoro: κ − κ' = c − 13, but κ(matter) + κ(ghost) = c/2 + (−13) = (c−26)/2 — these differ by a factor of 2 and an offset of 13/2. The conflation made "effective curvature vanishes" simultaneously mean two different things at two different central charges. Now split into δ_κ = κ − κ' (complementarity asymmetry) and κ_eff = κ(matter) + κ(ghost) (effective curvature). **Rule: when a physical quantity has algebraic AND physical sources (Koszul pair invariant vs matter-ghost system invariant), give them distinct symbols FROM THE FIRST OCCURRENCE. Verify: do the two quantities vanish at the same point? If not, they are different objects. For Virasoro: δ_κ = 0 at c=13 (self-duality), κ_eff = 0 at c=26 (anomaly cancellation). These are 13 units apart.**

**AP30 — Unconditional axiom claim with hidden hypothesis (CohFT flat identity).** The shadow CohFT (thm:shadow-cohft) was claimed to satisfy "flat identity, equivariance, splitting" — all three CohFT axioms. In fact, the flat identity requires the vacuum |0⟩ to lie in the generating space V; this is NOT automatic for all modular Koszul algebras. The hidden hypothesis was invisible at 3+ downstream cross-reference sites (concordance, Teleman reconstruction discussion, open problem). The downstream consequence: Teleman's reconstruction theorem requires a CohFT with flat unit; citing it for the shadow CohFT without verifying this hypothesis is logically unsound. **Rule: when a theorem satisfies "most but not all" axioms of a standard algebraic structure (CohFT, operad algebra, Frobenius algebra, etc.), ALWAYS list which axioms are unconditional and which are conditional, at EVERY cross-reference site. NEVER write "the shadow CohFT" without specifying "(without flat unit)" or "(with flat unit when |0⟩ ∈ V)." This applies to any structure with named axioms — a claim of "is a CohFT" means ALL axioms hold.**

**AP31 — Vanishing of a scalar invariant ≠ vanishing of the full tower (κ = 0 ⇏ Θ = 0).** The claim "Θ_{Vir_0} = 0" was derived from "κ(Vir_0) = 0." But κ is the arity-2 scalar projection of Θ_A; the higher-arity components (cubic shadow C, quartic Q, etc.) are independent invariants. The bar complex being uncurved (d²=0) means the scalar curvature term vanishes, NOT that the full MC element vanishes. Similarly, "F_g(Vir_0) = 0 for all g ≥ 1" was derived from "F_1(Vir_0) = 0" — but F_g at higher genus could receive contributions from higher-arity shadow components that do not depend on κ. The distinction is between the arity-0 genus-g projection (which uses only κ) and the full genus-g amplitude (which sums over all arities). For Vir at c=0: κ = 0 implies F_g^{scal} = 0, but higher-arity corrections F_g^{(r)} for r ≥ 2 could be nonzero (the Virasoro has shadow depth r_max = ∞). **Rule: NEVER deduce vanishing of a full algebraic structure from vanishing of its leading scalar invariant. κ = 0 ⟹ m_0 = 0 (uncurved); it does NOT imply Θ_A = 0. F_1 = 0 does NOT imply F_g = 0 for all g when higher-arity contributions exist. For claims about "all genera" or "all arities," verify each component separately.**

**AP32 — Genus-1 unconditional ≠ all-genera unconditional (scope creep via genus omission).** Cyclic rigidity (dim H^2_cyc = 1) gives Θ^min = η⊗Γ_A, but the identification Γ_A = κ(A)Λ FAILS for multi-weight algebras: the free energy receives a cross-channel correction δF_g^cross ≠ 0 at g >= 2 (op:multi-generator-universality, RESOLVED NEGATIVELY by thm:multi-weight-genus-expansion; δF_2(W_3) = (c+204)/(16c)). **Current status: obs_g = κ · λ_g is proved at all genera on the uniform-weight lane, and obs_1 = κ·λ_1 is proved unconditionally for all families. For multi-weight algebras at g>=2, the scalar formula FAILS — cross-channel corrections are generically nonzero. Rule: AP32 remains an active anti-pattern. Never upgrade a genus-1 statement to an all-genera theorem without checking whether the algebra is uniform-weight. The multi-weight genus expansion (thm:multi-weight-genus-expansion) gives the correct decomposition F_g = κ·λ_g^FP + δF_g^cross.**

**AP33 — Koszul duality ≠ Feigin-Frenkel duality ≠ negative-level substitution.** Three operations on chiral algebras share surface similarities but are mathematically distinct. (1) KOSZUL DUALITY: A ↦ A^! where A^! = (H*(B(A)))^v, the linear dual of the bar cohomology. For Heisenberg: H_k^! = Sym^ch(V*) with curvature -k·ω. The Verdier intertwining (Theorem A, Convention conv:bar-coalgebra-identity) states D_Ran(B(A)) ≃ B(A!), identifying the Verdier dual with the bar of A! as factorization coalgebras. The manuscript also writes D_Ran(B(A)) ≃ A^!_∞ (homotopy Koszul dual algebra whose underlying complex is B(A!)). (2) FEIGIN-FRENKEL INVOLUTION: k ↦ -k-2h^v within the SAME family of affine algebras. For Heisenberg: k ↦ -k. This is a DIFFERENT operation. (3) NEGATIVE-LEVEL SUBSTITUTION: H_k ↦ H_{-k}, replacing the level parameter. For Heisenberg: κ(H_k^!) = -k = κ(H_{-k}), so the modular characteristics coincide, but H_k^! ≠ H_{-k} as chiral algebras (H_k^! = Sym^ch(V*) is generated by V* with its own OPE structure, while H_{-k} is generated by V with level -k). Confusing these three operations produced errors in 15+ locations across both volumes. **Rule: NEVER write H_k^! = H_{-k}. The Koszul dual H_k^! = Sym^ch(V*) has the same κ as H_{-k} but is a different algebra. D_Ran(B(A)) ≃ B(A!) (coalgebra intertwining, Convention conv:bar-coalgebra-identity). The line-side Yangian dual Y(u(1)) ≃ H_{-k} is a SEPARATE object from the chiral Koszul dual H_k^! = Sym^ch(V*).**

### The Meta-Principle

Every mathematical error in this manuscript traces to **confusing two objects that share a name, a formula, a surface resemblance, or a special-case coincidence**:
- κ(KM) ≈ c/2 at certain levels (coincidence) → wrong formula propagated (AP1)
- Koszulness ≈ formality in the classical case → wrong claim for chiral (AP14)
- OPE ≈ r-matrix (same structure constants) → wrong pole orders (AP19)
- κ(A) ≈ κ_eff ≈ κ(A!) in special cases → conflation (AP20)
- Clifford ≈ exterior when λ ≈ 0 → wrong bifurcation (AP21)
- κ+κ! ≈ 0 (true for KM) → wrong universal claim (AP24)
- B(A) ≈ Ω(B(A)) ≈ D(B(A)) → three functors confused (AP25)
- Fock ≈ BPZ (agree at low weight) → diverge at weight ≥ 4 (AP26)
- field weight h ≈ propagator weight (coincide for h=1) → wrong Hodge bundle at h≥2 (AP27)
- "scalar lane" ≈ "all algebras" (undefined qualifier) → scope creep in 114 locations (AP28)
- δ_κ = κ−κ' ≈ κ_eff = κ(matter)+κ(ghost) (same symbol, different objects) → conflation at c=13 vs c=26 (AP29)
- "CohFT" ≈ "CohFT with flat unit" (agree for most families) → hidden hypothesis at Teleman reconstruction (AP30)
- κ = 0 ≈ Θ = 0 (agree at arity 2) → wrong tower vanishing (AP31)
- genus-1 proved ≈ all-genera proved (agree for single-generator) → scope creep for W_N (AP32)
- H_k^! ≈ H_{-k} (same κ, different algebras) → Koszul dual conflated with negative-level algebra (AP33)
- Ω(B(A)) ≈ "open-to-closed passage" (bar-cobar inversion sounds like it transforms open into closed) → inversion recovers A itself, not the bulk (AP34)
- correct answer ≈ correct proof (agree when proof is valid) → false proof survives because conclusion is accidentally true (AP35)
- A ⟹ B ≈ A ⟺ B (agree when converse happens to hold) → biconditional overclaimed from one direction (AP36)
- pole order ≈ spectral sequence page (agree for quadratic algebras) → wrong page for W_N (AP37)
- DVV convention ≈ Eichler-Zagier convention (both correct in their papers) → wrong hardcoded values from convention mismatch (AP38)
- S₂ = c/2 ≈ κ (coincide for Virasoro, Heisenberg) → diverge for affine KM at rank > 1 (AP39)
- \begin{theorem} ≈ proved (agree when tag is ProvedHere) → theorem environment for conjectural claim (AP40)
- prose description ≈ mathematical mechanism (agree when prose is precise) → "residue extracts simple pole" when it extracts all modes (AP41)
- sophisticated identification ≈ naive instantiation (agree in simple cases) → "scattering = shadow" fails at naive BCH level (AP42)
- property list ≈ definition (agree when properties uniquely characterize) → central object used without construction (AP43)
- OPE mode coefficient ≈ λ-bracket coefficient (agree for n=0,1) → diverge by n! for n≥2 (AP44)
- |s⁻¹v| = |v|+1 ≈ |s⁻¹v| = |v|-1 (suspension vs desuspension sign) → wrong bar degree (AP45)
- ∏(1-qⁿ) ≈ η(q) (agree up to q^{1/24}) → missing prefactor corrupts bounds (AP46)
- evaluation-generated core ≈ full module category (agree for finite-dim reps) → MC3 scope conflation (AP47)
- κ(A) ≈ c(A)/2 (agree for Virasoro and dim V₁=0 holomorphic VOAs) → diverge for lattice VOAs, general VOAs with affine currents (AP48)
- Vol I formula ≈ Vol II formula (agree when conventions match) → convention-blind cross-volume paste (AP49)
- Heisenberg ≈ "abelian CS algebra" (same algebra, different names) → fictional simple-pole algebra invented when the real boundary algebra has a double pole (AP105)
- "This chapter constructs X" ≈ constructing X (agree when the prose is the mathematics) → narration about mathematics instead of mathematics (AP106)
- r^coll(z) ≈ r(z) (agree for even E_∞ algebras) → diverge for odd generators and E_1 algebras (AP107)
- CG opening ≈ theory atom (agree when the simplest example is the fundamental building block) → Heisenberg is the opening, not the atom of E_1 theory (AP108)
- chapter preview ≈ mathematical content (agree when the preview IS the theorem statement) → forward-reference listing adds zero content (AP109)
- CLAUDE.md architecture ≈ .tex source architecture (agree when metadata is enacted) → metadata declares E_1 primacy while source opens with E_∞ bar (AP115)

**AP34 — Bar-cobar inversion ≠ open-to-closed passage.** Three distinct functors act on B(A): (1) RECONSTRUCTION: Ω(B(A)) ≅ A recovers the ORIGINAL algebra (Theorem B). This is a round-trip, not a duality. (2) KOSZUL DUALITY: Ω(D_Ran(B(A))) ≅ A! produces the DUAL boundary condition via Verdier duality (Theorem A). This is S-duality/mirror symmetry, exchanging boundary conditions. (3) DERIVED CENTRE: C^•_ch(A,A) = RHom(Ω(B(A)), A) computes the UNIVERSAL BULK (closed-string observables) via Hochschild cochains (Theorem H). The passage from open-string to closed-string data is functor (3), not functor (1). Bar-cobar inversion (1) recovers the open-string algebra itself; it does NOT produce the bulk. The phrase "bar-cobar inversion controls the passage from open-string to closed-string" is FALSE — the correct statement is "the chiral derived centre Z^der_ch(A), computed via Hochschild cochains of the bar resolution, is the universal bulk." At genus 0, the Swiss-cheese operad enforces one-way information flow (closed → open only). At genus ≥ 1, the annulus trace Δ_ns(Tr_A) = κ·λ₁ provides the first open-to-closed map. The full genus tower progressively restores bidirectionality. **Rule: NEVER write "bar-cobar inversion produces the closed-string/bulk/gravitational algebra." Inversion recovers A itself. The bulk is the derived centre. The dual boundary is A!. These are three different functors on B(A).**

**AP35 — Accidentally correct theorem (false proof, true conclusion).** The R-matrix descent proof (Prop 11.3.2, commit b5e9f00) claimed involutivity ρ_R(σ_i)² = id via: "the double monodromy is trivial in Σ_n because the covering sheet returns to itself." This topological argument is WRONG — the double monodromy of a half-twist gives a pure braid generator γ_{i,i+1} ∈ P_n, nontrivial in B_n. The CORRECT argument is algebraic: the Casimir Ω is symmetric, so strong unitarity R₁₂(z)R₂₁(-z) = id holds. The theorem was accidentally correct because strong unitarity holds for ALL E_∞-chiral algebras. Same pattern: orientation convention double-error (commit 036d740 in Vol II: outward normal +∂_{ε_S} vs correct -∂_{ε_S}, final sign correct from double cancellation). Same pattern: elliptic r-matrix factorial AND derivative order both off by one (commit a8dce32: errors partially cancelled giving correct pole structure but wrong regular part). **Rule: a correct answer is NOT evidence of a correct proof. When a proof uses a fact about topology/geometry/combinatorics, verify that fact INDEPENDENTLY of the theorem it proves. If two errors cancel, fix BOTH — the cancellation is accidental and will break under generalization. A proof that reaches the right answer by the wrong route will fail the first time the accidental cancellation breaks.**

**AP36 — Biconditional overclaim (⟹ proved, ⟺ claimed).** "Convolution formality = one-channel" was retracted (commit bfa5160) to one-directional: scalar MC identity ⟹ scalar-orbit formality. The converse assumed the transfer φ_*(Θ) lies on the scalar line, which does NOT follow from formality alone. Same pattern: DS-KD intertwining was claimed for "all Koszul algebras at generic level" (commit 7f7db06) but only proved on the abelian-n+ lane via Kazhdan filtration. The introduction called this "formality of the BRST complex" (conflating filtration formality with dg formality — two different properties). Same pattern: the rectification meta-theorem claimed L∞-formality IFF one-channel (commit 141cafd, finding F129), retracted to one-directional. **Rule: before writing "if and only if" or "equivalent to," verify BOTH directions have independent proofs. If only the forward direction is proved, write "implies" and flag the converse as OPEN. "One-directional" is a valid and valuable theorem; "biconditional" requires twice the proof. Especially dangerous: "formality" has multiple non-equivalent meanings (E₁-degeneration, dg-formality, L∞-formality, filtered formality) — state which one.**

**AP37 — Spectral sequence page from pole order alone.** The W_N bar spectral sequence collapse was claimed at E₄ (commit 5d028a6 in Vol II); correct is E_{2N} for N ≥ 3 (the W_N self-OPE has pole order 2N, driving d_{2N-1} differentials from scalar contact terms). The page at which a spectral sequence collapses depends on the FULL OPE structure, not just the generic maximal pole order. Same commit: the ordered bar E₁ page was identified as Lie homology; correct is Hochschild homology (the ordered bar is a TENSOR construction, not an exterior construction; in char 0 the antisymmetrization map gives a quasi-isomorphism, but the objects are categorically different). **Rule: when computing spectral sequence pages, work from the FULL differential structure, not from pole-order heuristics. Lie homology (exterior powers, antisymmetric tensors) ≠ Hochschild homology (tensor powers, all tensors). The quasi-isomorphism in char 0 does NOT make them the same object — their functorial properties differ.**

**AP38 — Literature normalization convention in hardcoded values.** The BKM shadow obstruction tower engine (commit a0ff317 in Vol III) hardcoded phi_{0,1} Fourier coefficients in the DVV convention (f(0,0)=20, f(1,0)=-252) instead of the Eichler-Zagier convention (f(0,0)=10, f(1,0)=108). The two conventions normalize the SAME Jacobi form differently — both are correct in their respective papers, but mixing them produces silently wrong numerical results. Same pattern: Faber-Pandharipande test expectations (commit 5d028a6 in Vol II): λ₂ = 1/1152 was wrong; correct is 7/5760. The engine was correct; the test hardcoded a wrong expected value from a different normalization. Same pattern: F₁ coefficient (commit 036d740 in Vol II): -(k/24)log η(τ) → -k log η(τ), confusing η(τ) = q^{1/24}∏(1-q^n) with its logarithm. **Rule: when hardcoding numerical values from the literature, ALWAYS record the source paper and normalization convention in a comment. When writing tests, derive expected values from an INDEPENDENT computation (AP10), not from hardcoded literature values. When two sources give different numbers for the same object, suspect a normalization convention before suspecting an error.**

**AP39 — κ ≠ S₂ for non-Virasoro families (shadow coefficient ≠ modular characteristic).** The landscape table in Vol II (commit 5d028a6) had 8+ values wrong because column headers conflated S₂ = c/2 (the arity-2 shadow coefficient) with κ = dim(g)·(k+h∨)/(2h∨) (the modular characteristic). For Virasoro and Heisenberg, S₂ = κ (because dim = 1 and the c-to-κ ratio is 1/2). For affine KM at rank > 1: S₂ = c/2 ≠ κ. The same issue appeared in Vol III (commit 9bd9e07): Heisenberg κ was k/2 instead of k, propagated from an old Vol I error. **Rule: S₂ (the arity-2 shadow projection) and κ (the modular characteristic = genus-1 obstruction class coefficient) are DIFFERENT invariants that coincide only for rank-1 algebras. Table headers must distinguish them. NEVER copy κ from one family to another — recompute from the defining formula κ(A) = dim(g)·(k+h∨)/(2h∨) for KM, κ = c/2 for Virasoro, κ = k for Heisenberg.**

**AP40 — LaTeX environment contradicts claim status tag.** Three frontier conjectures in Vol II (commit 09653d0) were in \\begin{theorem} environments despite carrying \\ClaimStatusConjectured tags. At Annals grade, this is a scope-honesty failure: a reader scanning theorem environments will count these as proved. Same pattern: thm:Koszul_dual_Yangian in Vol II (commit 6199df0) was tagged ProvedHere but the statement cited "(Dimofte-Niu-Py, Theorem 5.5)" — an attribution paradox. **Rule: the LaTeX environment MUST match the claim status tag. Conjectured claims use \\begin{conjecture}. ProvedElsewhere uses \\begin{theorem} with the external attribution in a Remark, not in the theorem statement. ProvedHere means the proof appears in THIS manuscript. Systematic check: grep for ClaimStatusConjectured inside theorem environments, and for ClaimStatusProvedHere with external citations in the statement.**

**AP41 — Prose mechanism ≠ mathematical mechanism.** "The residue extracts the simple-pole coefficient of the OPE" (commit 036d740 in Vol II) was WRONG — the bar differential extracts ALL OPE modes via the logarithmic kernel d log(z-w), not just the simple-pole coefficient. The mathematical formulas in the text were correct; only the English description was wrong. Same pattern: "the shadow tautological relation is a proof of the class identity" (commit 50526a7) — it is a CONDITIONAL CONSEQUENCE of the scalar hypothesis, not a proof. Readers who rely on prose descriptions to build mental models will form incorrect ones. **Rule: after writing a prose description of a mechanism, verify that the description matches the formulas. The English sentence should be deducible from the mathematics. If the mechanism has multiple steps (e.g., d-log absorption reduces pole order, THEN residue extraction), name ALL steps. One-sentence summaries that skip steps are lies of omission.**

**AP42 — Correct at sophisticated level, false at naive level.** "Scattering diagram = shadow obstruction tower" (Vol III, commit 72ba062): the identification holds at the motivic Hall algebra level, but naive BCH pair-commutator does NOT reproduce phi_{0,1} multiplicities (quantitative mismatch by non-uniform ratios). The gap measures higher BPS bound-state contributions requiring full motivic DT theory. Same pattern: "CY-A works for all d" (Vol III, commit a0ff317): d=2 is proved; d=3 is a programme conditional on chain-level S³-framing. The slogan captures a deep structural truth that is false when instantiated naively. **Rule: when an identification holds "in principle" or "at the right level," STATE that level explicitly. Write "scattering = shadow at the motivic level (naive BCH insufficient)" rather than "scattering = shadow." Write "CY-A proved for d=2; programme for d=3" rather than "CY-A." The naive reader will instantiate the slogan at the simplest level — make the level of validity explicit from the first occurrence.**

**AP43 — Central object defined by aspiration, not by axioms.** The "quantum vertex chiral group" G(X) in Vol III (audit, commit 99167c2) was used in ~20 locations without ever receiving a formal \\begin{definition} environment. The "definition" in the notes files is a list of PROPERTIES that G(X) should satisfy, not a CONSTRUCTION or AXIOMATIC characterization. Same issue: "quantum chiral algebra" was defined as "equivalent to quantum group representation category" — this is a prayer, not a mathematical condition. Same root cause as AP28 ("scalar lane") but for OBJECTS rather than qualifiers. **Rule: the CENTRAL OBJECT of a chapter/volume MUST be formally defined before it is used. A list of properties is a conjecture about the object, not a definition of it. If the object doesn't yet have a construction, say so: "Conjecture: there exists an object G(X) satisfying..." is honest. Using G(X) in theorem statements without defining it is circular.**

**AP44 — OPE mode coefficient ≠ λ-bracket coefficient (divided-power convention).** The OPE mode T_{(3)}T = c/2 becomes {T_λ T} = (c/12)λ³ in the λ-bracket, because λ^(n) = λⁿ/n! is the divided power: the coefficient acquires a factor 1/n!. The Vol II preface had (c/2)λ³ in FOUR locations — all wrong by a factor of 6. The m₂(W,W;λ) formula had ALL coefficients wrong (c/3 instead of c/360 at order 5, 2T instead of T/3 at order 3). Root cause: copying the OPE-mode coefficient directly into the λ-bracket formula without applying the divided-power conversion. **Rule: when translating between OPE modes a_{(n)}b and λ-bracket {a_λ b} = Σ_n λ^(n) a_{(n)}b, remember that λ^(n) = λⁿ/n!, so the λ-bracket coefficient at order n is a_{(n)}b/n!, NOT a_{(n)}b. Similarly, the Borel transform B(K)(λ) = Σ λ^(n) c_n already has the 1/n! absorbed into λ^(n); do NOT divide by n! again. Verify by checking the leading term: {T_λ T} at order λ³ must give (c/2)/3! = c/12, not c/2.**

**AP45 — Desuspension LOWERS degree, not raises.** The bar complex uses desuspension s⁻¹. The sign appendix (signs_and_shifts.tex) is authoritative: |s⁻¹v| = |v| - 1 (desuspension LOWERS cohomological degree by 1). The Heisenberg frame chapter had |s⁻¹α| = |α| + 1 = 2, which is WRONG: correct is |s⁻¹α| = |α| - 1 = 0 for a degree-1 generator. The total bar degree (arity/tensor length) is the relevant grading for the bar spectral sequence, NOT the cohomological degree of individual desuspended elements. This error is insidious because the bar differential |d| = +1 in cohomological grading regardless — the confusion is between the degree of a SINGLE element s⁻¹v and the degree of the DIFFERENTIAL. **Rule: s⁻¹ shifts degree DOWN by 1. s shifts degree UP by 1. When in doubt, consult signs_and_shifts.tex. The bar complex element s⁻¹a₁ ⊗ ··· ⊗ s⁻¹aₙ has cohomological degree Σ(|aᵢ| - 1) = Σ|aᵢ| - n, not Σ|aᵢ| + n.**

**AP46 — Dedekind eta includes q^{1/24}.** η(q) = q^{1/24} ∏_{n≥1}(1-q^n). The q^{1/24} prefactor is NOT optional. The product ∏(1-q^n) alone is NOT η(q). In the Vol II perturbative finiteness chapter, ∏(1-q^n)^{-2|k|²} was equated to η(q)^{-2|k|²} — wrong by a factor of q^{-|k|²/12}. This error silently corrupts partition-function bounds: the missing q-power shifts the leading Fourier coefficient. Same pattern: log η(τ) = (2πiτ)/24 + Σ log(1-q^n) — confusing log η with log ∏ drops the (2πiτ)/24 term. **Rule: ALWAYS write η(q) = q^{1/24}∏(1-q^n) at first use in any computation. When a bound or asymptotic uses ∏(1-q^n)^α, do NOT replace it with η^α unless you account for the q^{α/24} factor. Cross-check: η(e^{-2πt}) ~ e^{-πt/12} as t→0⁺ (the 1/12 comes from q^{1/24}).**

**AP47 — Evaluation-generated core ≠ full category (MC3 scope).** MC3 (thick generation of the DK category) is PROVED for all simple types on the evaluation-generated core (Corollary cor:mc3-all-types). The residual problem — extending from the evaluation-generated core to the full module category — is DK-4/5, which is DOWNSTREAM of MC3, not a component of it. Writing "MC3 partially resolved" conflates two distinct problems: (1) the categorical CG decomposition on the evaluation core (PROVED), and (2) the completion/extension to the full Ran-space category (DK-4/5, OPEN). The manuscript had "partially resolved" in 10+ locations across 7 files, all corrected. **Rule: state the scope of the proved result precisely. "MC3 proved for all simple types on the evaluation-generated core; DK-4/5 (extension beyond evaluation modules) is downstream" is honest. "MC3 partially resolved" is vague and understates the proved content while overstating what remains.**

**AP48 — κ depends on the full algebra, not the Virasoro subalgebra.** For a VOA A with Virasoro subalgebra Vir_c ⊂ A, the modular characteristic κ(A) is NOT necessarily c/2. The formula κ = c/2 holds when the genus-1 bar obstruction is determined entirely by the Virasoro OPE. This occurs for: (a) the Virasoro algebra itself, and (b) holomorphic VOAs with dim V₁ = 0, where no affine currents contribute to the genus-1 bar obstruction (the weight-2 Griess algebra contributes to higher-arity shadows but not to κ). **RESOLVED: κ(V♮) = 12 = c/2.** The moonshine module V♮ (c=24, dim V₁=0) has κ = c/2 = 12, confirmed by 5 independent verification paths in moonshine_shadow_depth.py (Vol I Remark rem:lattice:monster-shadow; Vol III working_notes.tex). Since dim V₁♮ = 0, the Virasoro sector alone determines the genus-1 bar obstruction. V♮ is class M (Δ = 8κS₄ = 20/71 ≠ 0, infinite shadow depth). The 24 Niemeier lattice VOAs have κ(V_Λ) = rank(Λ) = 24 ≠ 12 = κ(V♮): genuine shadow-tower separation at the same central charge c = 24. The distinction: κ(V_Λ) = rank(Λ) counts FREE BOSON generators (Heisenberg formula κ = k), while κ(V♮) = c/2 counts the VIRASORO generator's contribution (no weight-1 currents survive the Z/2Z orbifold V_Leech → V♮). For non-lattice, non-Virasoro VOAs with dim V₁ > 0, κ must be computed from the full bar complex, not from c alone. **Rule: NEVER write κ(A) = c/2 for a general VOA. The formula κ = c/2 applies to: (i) the Virasoro algebra, (ii) holomorphic VOAs with dim V₁ = 0 (e.g., V♮). For lattice VOAs: κ = rank. For affine KM: κ = dim(g)(k+h∨)/(2h∨). For a general VOA with dim V₁ > 0: compute from the genus-1 bar complex. The central charge c and the modular characteristic κ are DISTINCT invariants that coincide only when the Virasoro sector alone determines the genus-1 obstruction (AP39 generalized).**

**AP49 — Cross-volume formula propagation without convention check.** The same mathematical object may be presented in different conventions across Vol I (OPE modes, cohomological grading), Vol II (λ-brackets, divided powers), and Vol III (motivic/categorical). A formula correct in one convention becomes wrong when transplanted to another without conversion. The Vol II preface errors (AP44) arose from copying Vol I OPE-mode coefficients into Vol II λ-bracket context. The Vol III working notes errors (sqfree cascade) arose from copying Vol I number-theoretic computations without verifying the factorization. **Rule: when citing a formula from another volume, ALWAYS (1) identify the source convention, (2) identify the target convention, (3) apply the conversion explicitly, (4) verify the converted formula at one numerical value. NEVER paste a formula between volumes without conversion. The three volumes use overlapping but distinct notation systems.**

**AP50 — Homotopy Koszul dual A^!_∞ ≠ strict Koszul dual A^!; Verdier duality ≠ linear duality of bar cohomology; their compatibility is Theorem A.** Two distinct operations produce two distinct objects that are COMPATIBLE but NOT IDENTICAL. (1) VERDIER DUALITY on Ran(X): D_Ran(B(A)) ≃ A^!_∞, the homotopy Koszul dual — a factorization ALGEBRA (not coalgebra) retaining full chain-level data. (2) LINEAR DUALITY of bar cohomology: A^i = H*(B(A)) (graded coalgebra), then A^! = (A^i)^v (graded linear dual, an algebra) — the strict Koszul dual, remembering only cohomology. These are different functors on different inputs producing different objects at different categorical levels. That they are compatible — that H*(A^!_∞) recovers A^! on the Koszul locus — is the content of Theorem A (the Verdier intertwining theorem), NOT a tautology. The preface conflated them in two ways: (a) calling the Verdier dual a "coalgebra" (Verdier duality converts coalgebra TO algebra), and (b) chaining "Verdier duality sends B(A) to X; the linear dual is A^! = ..." as if linear duality is a step within Verdier duality. These are independent operations that happen to converge on A^!, and the convergence requires proof. **Rule: A^!_∞ and A^! are DIFFERENT OBJECTS. A^!_∞ is the homotopy version (chain-level, from Verdier duality). A^! is the strict version (cohomological, from linear duality of bar cohomology). When presenting the Koszul dual, pick ONE route and state it cleanly. If using the two-step algebraic route, do not invoke Verdier duality. If invoking Verdier duality, produce A^!_∞ (not A^!) and note that the identification with A^! requires Theorem A. Never write "Verdier duality produces a coalgebra." Never present A^!_∞ = A^! without citing the theorem that proves it.**

**AP59 — Three distinct invariants must never be conflated: p_max, k_max, r_max.** A chiral algebra A has THREE distinct numerical invariants that measure different structural features: (a) p_max(A) = generator OPE pole order (maximal pole in the OPE between generating fields), (b) k_max(A) = collision depth (pole order of the arity-2 collision residue Res^coll_{0,2}(Theta_A)), (c) r_max(A) = shadow depth (arity at which the shadow obstruction tower terminates). The relation k_max = p_max - 1 always holds (d log absorption, AP19), but r_max is INDEPENDENT of p_max. The βγ system is the archetypal witness: p_max(βγ) = 1 (simple pole only), k_max(βγ) = 0 (trivial collision residue), r_max(βγ) = 4 (class C, quartic contact from composite fields). Conflation produces wrong classifications: e.g., assuming "shadow depth = OPE pole order" leads to placing βγ in class L (wrong) instead of class C. The error pattern: writing "depth" without specifying which invariant is meant. Found in T6 first draft (CRITICAL F16/F17, 2026-04-07). **Rule: when discussing depth, always specify which of the three invariants. NEVER write "βγ has shadow depth 1" — βγ has p_max=1, k_max=0, r_max=4. Formal definitions in chapters/theory/three_invariants.tex.**

**AP60 — Status inflation when combining new and known content.** When a theorem combines a new identification with classical results (Drinfeld 1985, Semenov-Tian-Shansky 1983, Feigin-Frenkel-Reshetikhin 1994, etc.), the natural temptation is to tag the entire theorem `\ClaimStatusProvedHere`. This is incorrect: the classical components are `\ClaimStatusProvedElsewhere` (with attribution); only the genuinely new identification is ProvedHere. Found in T5 (Sklyanin theorem) first draft (SERIOUS F12, 2026-04-07): the Yangian-Sklyanin theorem combined Drinfeld 1985 + Semenov-Tian-Shansky 1983 with the new three-parameter identification of ℏ. The correct pattern: split the theorem, OR restrict the ProvedHere claim to the genuinely new content via a parenthetical "(the new content of this theorem is...)". **Rule: before tagging a theorem ProvedHere, identify which sub-claims are genuinely new and which are reproved classical results. Always cite the classical result by name and year. Use \ClaimStatusProvedElsewhere for re-proved classical results.**

**AP61 — Hardcoded values from CLAUDE.md descriptions inherit conflations.** Compute engines that copy values from CLAUDE.md "shadow archetypes" descriptions can inherit semantic conflations. Example: the description "betagamma=contact/quartic/terminates@4" was interpreted as "βγ has p_max = 2" in theorem_three_paper_intersection_engine.py, hardcoding the wrong value. AP10 caught this only on cross-engine comparison after the manuscript-side error was found. The root cause: CLAUDE.md uses "depth" in informal slogans where the precise invariant is ambiguous; an engine reading these slogans must verify against the primary source (OPE table, landscape_census). **Rule: never copy a numerical invariant from a CLAUDE.md description without verifying against (1) the OPE table in the relevant example chapter, (2) the landscape_census.tex authoritative table, (3) at least one cross-engine comparison. The compute layer must NEVER trust CLAUDE.md slogans for numerical values.**

### Anti-Patterns from the 2026-04-07 Frontier Research Swarm (AP62-AP80)

The 125-agent session catalogued ~40 distinct error patterns. The following are the structurally NEW anti-patterns beyond AP1-AP61.

**AP62 — "Bar cohomology depends only on dim(g)" is TRUE for Euler characteristic, FALSE for individual dimensions.** The CE Euler series χ(B(V_k(g)))_w = [t^w] ∏(1-t^n)^d depends only on d = dim(g). But individual dimensions dim H^p(g_-, k) depend on the full bracket structure. Counterexample at d=3: sl₂ gives total dims [3,0,5,0,0,7]; abelian³ gives [3,6,13,24,42,73]; nilp Heis₃ gives [3,4,9,16,24,39]. Same Euler series, completely different cohomology. For SEMISIMPLE g the Garland-Lepowsky theorem concentrates cohomology into a single bidegree per weight, making |Euler coefficient| = total dim — this is an ACCIDENT of semisimplicity (Kostant-type concentration), NOT a general theorem. Found 2026-04-07 by the bar_cohomology_non_simply_laced agent. **Rule: never claim "bar cohomology depends only on dim(g)" without specifying "Euler characteristic" or restricting to semisimple finite-type g. The `bar_cohomology_non_simply_laced_engine` line 816 docstring should be qualified.**

**AP63 — CE of the negative loop Lie algebra ≠ chiral bar complex for multi-generator algebras.** For SINGLE-generator algebras (Heisenberg, Virasoro), CE(g_-) and B(A) agree. For MULTI-generator algebras (sl₂, W₃, N=2 SCA, Y-algebras), they DIFFER due to the Orlik-Solomon form factor on the chiral side. Example: sl₃ chiral H² = 36 (Sym² of adjoint) vs algebraic H² = 20 (Λ² of adjoint mod bracket). The chiral bar uses the tensor construction with OS form factor, while CE uses the exterior construction with Jacobi. The Y_{1,1,1} agent (2026-04-07) explicitly found: CE(A_-) for A_- = Witt_- ⋉ Heis_- has total H¹ dim 5 at weights 1,2,2,3,4 with H²≠0, while the chiral bar of Y_{1,1,1} has H*(B(Y_{1,1,1})) = {H¹ = {1:1, 2:1}, H^n = 0 for n ≥ 2}. These are DIFFERENT. **Rule: for multi-generator algebras, never substitute CE cohomology of the negative Lie algebra for chiral bar cohomology. The apparent non-Koszulness of the N=2 SCA CE complex may be an artifact not a statement about the vertex algebra.**

**AP64 — Same cohomology, different gradings produce different numerical sequences.** H*(B(A)) can be computed in (a) CONFORMAL WEIGHT grading (Garland-Lepowsky: sl₂ gives dim H^n = 2n+1 concentrated at weight n(n+1)/2 — linear growth), or (b) PBW DEGREE grading (Koszul dual Hilbert series: sl₂ gives [3, 5, 15, 36, 91, 232, ...] — Riordan-like sequence). These are the SAME cohomology in DIFFERENT gradings. The engines `bar_cohomology_sl2_explicit_engine` (124 tests) uses grading (a); `minimal_resolution_chiral_engine` (109 tests) uses grading (b). BOTH are correct. This is AP9 (same-name-different-object) specialized to cohomological gradings. Found 2026-04-07 when two agents produced apparently contradictory values. **Rule: every bar cohomology number must specify which grading (CE weight, PBW degree, total arity, Frobenius-character). Never compare numerical sequences across gradings without an explicit reindexing map.**

**AP65 — The ORDERED (E1) bar complex is the PRIMITIVE structure; the unordered/commutative bar is the derived quotient.** The ordered bar B^{ord}(A) = ⊕ V^⊗n with full S_n action carries: (1) quantum group R-matrix in degree (1,1), (2) full Frobenius characteristic in S_n irreps, (3) non-cocommutative coproduct (Drinfeld-Jimbo), (4) Stasheff associahedra cellular A∞ structure, (5) Yangian from collision residue r(z), (6) DK bridge / MC3, (7) Swiss-cheese E1 × E∞ structure. The unordered/symmetric bar B^{un}(A) = B^{ord}(A)^{S_n antisym} is the QUOTIENT by antisymmetrization — a quasi-iso in char 0 but losing all quantum group information. The manuscript currently treats the unordered/commutative story as primary and the E1/ordered as an afterthought — this is a structural architectural error identified by the user on 2026-04-07. **Rule: when writing about the bar complex, B^{ord}(A) is the primary object; B^{un}(A) is secondary, derived by quotient. The ordered-to-unordered passage LOSES the quantum group structure. The quantum group R-matrix lives in degree (1,1) of the ordered bar — verified in `bar_quantum_groups_engine.py`.**

**AP66 — Partition-type generating functions are NOT D-finite.** Standard families split into two classes by bar GF: INTERACTING algebras (affine KM sl_N, Virasoro, W_N, βγ, bc) have rational or algebraic GFs which are D-finite; FREE FIELDS (Heisenberg, FreeFermion, Lattice) have partition-type GFs ∏(1-q^n)^{-d} which are NOT D-finite (classical Lipshitz/Stanley result). The "all standard families have D-finite bar GFs" conjecture is FALSE. The D-finiteness dichotomy separates interacting (D-finite) from free-field (non-D-finite). Found 2026-04-07 by the bar_gf_universality agent. **Rule: never claim D-finiteness for free-field bar generating functions. The partition function η(q)^{-1} is the canonical non-D-finite example. When formulating a universal property of bar GFs, exclude free fields or state the D-finite class explicitly.**

**AP67 — Strong generation ≠ FREE strong generation.** The triplet algebra W(p) has 4 strong generators (T at weight 2 + sl_2 triplet W^+, W^0, W^- at weight 2p-1). This is STRONG generation. But whether these generators are FREELY strongly generated (PBW basis with no relations among normally ordered monomials) is OPEN. Screening kernels do NOT inherit free generation from the ambient lattice VOA — a sub-VOA of a freely strongly generated VOA need NOT itself be freely strongly generated. The W(p) Koszulness "prediction" was downgraded to OPEN on 2026-04-07 because all 4 proposed proof paths failed: (i) screening construction (kernel doesn't inherit FSG), (ii) Feigin-Tipunin presentation (strong ≠ free), (iii) character comparison (convention ambiguities), (iv) deformation argument (p is discrete). **Rule: the implication "freely strongly generated ⟹ chirally Koszul" (cor:universal-koszul) requires FREE generation, not just strong generation. Never apply prop:pbw-universality to an algebra that is merely strongly generated.**

**AP68 — PVA slab ghost central charge ≠ chiral algebra modular characteristic (AP20 sharpened).** For N=1 SuperVirasoro, the manuscript at w_algebras_deep.tex:3281 originally had κ(SVir_c) = (c+11)/2 = c/2 + 11/2, derived from a faulty analogy with the PVA slab central charge c_slab = 37. The correct formula is κ(SVir_c) = (3c-2)/4, complementarity sum Σ_1 = 41/4. The test that caught the error: hierarchy monotonicity. Σ_0 (Virasoro) = 13, Σ_1 (N=1) = 41/4 = 10.25, Σ_2 (N=2) = 1, Σ_4 (N=4) = 0 — strictly decreasing. The manuscript formula gave Σ_1 = 37/2 = 18.5 > 13, violating monotonicity. Four errors fixed across 3 .tex files on 2026-04-07 via the CRITICAL SVir κ resolution agent. **Rule: NEVER derive the modular characteristic κ by analogy with a sigma-model / PVA slab / BRST ghost central charge. κ is an invariant of the chiral algebra computed from the bar complex (or equivalently from F_1/λ_1 or the genus-1 Hodge class coefficient). Ghost sigma models have their OWN independent central charge that is NOT κ.**

**AP69 — τ_shadow = τ_KW^κ satisfies κ-DEFORMED KdV, NOT standard KdV.** The naive expectation that "τ^κ is a KdV tau function for all κ" is false: the nonlinear term u·∂u/∂t₀ scales as κ², giving an obstruction κ(κ-1). Standard KdV is recovered only at κ=1 (Witten-Kontsevich point) and κ=0 (trivial). The correct equation for τ_shadow is u_t + (6/κ)uu_x + u_xxx = 0, equivalent to standard KdV for v = u/κ with a rank-κ matrix model Poisson bracket. Proved 2026-04-07 by the τ_KW^κ theorem agent and the shadow hierarchy agent. The MC equation in g^mod_A is the correct governing equation; κ-deformed KdV is the scalar projection at genus 0 arity 3. **Rule: τ_shadow is NOT a standard integrable hierarchy tau function for generic κ. Do not apply KdV integrability results (Hirota bilinear identity, Kadomtsev-Petviashvili hierarchy, Sato Grassmannian) directly to τ_shadow. The correct hierarchy is κ-deformed KdV or, more generally, the MC equation itself.**

**AP70 — Shadow L-function L^sh(s) = -κ·ζ(s)·ζ(s-1) has POLES at positive integers, not finite values.** Specifically: L^sh has poles at s=1 (from ζ(s)) and s=2 (from ζ(s-1)), with residues involving κ. The negative integers ARE trivial zeros — for s = 1-2g with g ≥ 1, the factor ζ(s-1) = ζ(-2g) = 0 for g ≥ 1. Consequently: (a) the conjecture "F_g ↔ L^sh(1-2g)" via Riemann functional equation FAILS, since every 1-2g with g≥1 is a trivial zero; (b) physical central charge values don't give "finite special values" at s=2 — they give pole residues; (c) at s=0, L^sh(0) = -κ/24 (not -κ/12), obtained via ζ(0)=-1/2 and ζ(-1)=-1/12. Found 2026-04-07 by the shadow_l_function_arithmetic agent. **Rule: before citing a special value of L^sh at an integer, check the pole structure of both ζ(s) and ζ(s-1). Trivial zeros of ζ kill all negative-integer specializations except s=0.**

**AP71 — Shadow κ is a chiral algebra invariant, NOT a Dyson β or Painlevé parameter.** The Dyson β = 1, 2, 4 ensembles (GOE/GUE/GSE) correspond to different random matrix symmetry classes, NOT to shadow κ values. Tracy-Widom F₂ is governed by Painlevé II Hastings-McLeod (soft edge of GUE), NOT Painlevé I. Painlevé I corresponds to the (2,3) minimal model / pure 2D gravity, which is related to shadow κ via τ_shadow = τ_KW^κ — but shadow κ is a CHIRAL ALGEBRA invariant (κ = c/2 for Virasoro, k for Heisenberg, rank for lattice VOA), while Dyson β parameterizes symmetry classes of random matrices. A related common trap: "at c=13, κ=13" is FALSE — at c=13, κ = c/2 = 13/2 = 6.5. The value 13 is the SUM κ+κ' for the Koszul pair (AP24), not κ itself. Found 2026-04-07 by the κ-Painlevé agent. **Rule: never identify shadow κ with a random matrix parameter, Painlevé transcendent parameter, or other physical constant without explicit derivation. κ is the genus-1 obstruction class coefficient, period.**

**AP72 — W-algebra ordered associative bar complex (with normally ordered product as multiplication) does NOT have d²=0.** For W₃ (and presumably higher W_N), the normally ordered product a_{(-1)}b is NOT associative. The ordered associative bar complex constructed with NOP as multiplication does not satisfy d²=0. The chiral bar complex uses the FULL singular OPE μ(a,b) = Σ_{k≥0} a_{(k)}b with the Orlik-Solomon algebra on configuration spaces. d²=0 holds at the SHEAF LEVEL via the Borcherds identity + Arnold relation, NOT via ordered merges with NOP as the multiplication. Found 2026-04-07 by the W₃ bar cohomology agent. **Rule: when constructing a bar complex for a non-commutative VOA, use the full singular OPE with Orlik-Solomon form factor, NOT the normally ordered product with naive ordered multiplication. The existing `make_w3` function in `bar_cohomology_dimensions.py` gives incorrect results because of this.**

**AP73 — BV Laplacian = sewing operator at chain level is CONDITIONAL on shadow class.** The identification Δ_BV = d_sew is UNCONDITIONAL for classes G, L (Heisenberg, affine KM) where all four proof paths (operator definition, spectral sequence, Heisenberg extraction, modular operad) converge. For classes C, M (βγ, Virasoro, W_N), the identification is CONDITIONAL on the harmonic propagator decoupling at quartic and higher levels — this is Obstruction 3 of prop:chain-level-three-obstructions. Found 2026-04-07 by the BV-sewing theorem agent (96 tests). **Rule: manuscript claims of "BV=bar at chain level" must specify the shadow class. Classes G/L: proved unconditionally. Classes C/M: conditional on harmonic decoupling (open). The scalar-level match F_g = κ·λ_g^FP is ALWAYS proved by Theorem D; the chain-level identification is the deeper claim.**

**AP74 — Shadow Eisenstein theorem proof cites a FALSE Bernoulli-Dirichlet identity (applies AP35).** The proof of thm:shadow-eisenstein in arithmetic_shadows.tex invokes "Σ_{r≥1} B_{2r}/(2r)! · r^{-s} = -ζ(s)·ζ(s-1)" as a Ramanujan-type identity. This is numerically FALSE: at s=0, LHS = 1/(e-1) - 1/2 ≈ 0.0820 (entire function of s, since Bernoulli coefficients decay as 2(2π)^{-2r}) vs RHS = -(-1/2)(-1/12) = -1/24 ≈ -0.0417 (meromorphic with poles at s=1, 2). The two cannot be equal — they disagree even in analytic structure. The theorem's conclusion (L^sh is an Eisenstein L-function) may be correct via graph-amplitude reorganization using the intertwining kernel M[G_r], but the cited Bernoulli-Dirichlet step requires rewriting. This is AP35 (accidentally correct theorem, false proof) applied to a specific case. Found 2026-04-07 by the shadow_l_function_arithmetic agent. **Rule: before citing a "Ramanujan identity" for a Bernoulli-Dirichlet sum, verify numerically at s=0 that LHS = RHS as specific rational numbers. The generating function 1/(e^t - 1) - 1/2 = Σ B_{2r} t^{2r-1}/(2r)! is ENTIRE; Mellin-transformed Dirichlet series from it are entire too.**

**AP75 — Koszulness does NOT mean H^k = 0 for k ≥ 2 in conformal weight grading.** Koszulness = PBW spectral sequence collapse at E₂, which concentrates cohomology in PBW DEGREE (= bar degree). In CONFORMAL WEIGHT grading, the Koszul dual A! has generators (H¹), relations (H²), syzygies (H³), and potentially higher homological degrees — all nonzero in the weight grading. The existing docstring "Koszulness means H^k = 0 for k ≥ 2" in `bar_cohomology_virasoro_explicit_engine.py` line 61 is MISLEADING in the weight grading. Found 2026-04-07 by the PBW spectral sequence agent. **Rule: Koszulness is a statement about PBW degree concentration (bar degree), NOT about cohomological degree concentration in any other grading. When stating "H^k = 0 for k ≥ 2", always specify which grading.**

**AP76 — Y_{N₁,N₂,N₃}[Ψ] central charge vanishes when σ = h₁+h₂+h₃ = 0.** For Y_{1,1,1}[Ψ], the algebraic identity σ = h₁+h₂+h₃ = 0 (from the truncation curve) forces all λ_i = 0, giving c(Y_{1,1,1}) = (-1)³ + 1 = 0, NOT 3. The "κ = c/2" approximation used by the previous GR landscape engine gives the WRONG answer κ = 0; the correct κ for Y_{1,1,1} comes from the Heisenberg channel via κ_T = 0, κ_J = Ψ, total κ = Ψ. This is AP48 (κ depends on full algebra, not Virasoro subalgebra) applied to Y-algebras. Found 2026-04-07 by the Y_{1,1,1} bar cohomology agent. **Rule: for Y-algebras and other corner VOAs, compute κ channel by channel. Do NOT use κ = c/2 as a default approximation. The Virasoro channel may have κ_T = 0 while other channels contribute.**

**AP77 — Stokes ratio tests on convergent series give spurious instanton actions.** The Stokes S₁ engine originally applied the ratio test F_{g+1}/F_g ~ (2g+2)(2g+1)/(A²) to extract the instanton action A. This works for FACTORIALLY DIVERGENT series. But the shadow free energy F_g = κ·λ_g^FP decreases GEOMETRICALLY (not factorially): the (2g+2)(2g+1) factorial factor is SPURIOUS. The engine returned A ≈ 406707 instead of 39.48 = (2π)². Found and fixed 2026-04-07 in the deep Beilinson rectification. A similar bug: applying Borel-Padé to a CONVERGENT series produces an entire function with no poles — the Padé found a spurious pole at ~796 instead of 39.5. Fix: apply Padé directly to Z(u), not to the Borel transform. **Rule: before applying factorial-based asymptotic tests, verify the series is actually factorially divergent. Geometric decay requires different analysis (direct pole extraction, not Borel).**

**AP78 — The Hardy-Ramanujan number 1729 coincidence in δF₂ values is illusory.** The user and/or agent observed A₂(N) values 51, 179, 434, ... and conjectured A₂(6) = 1729/4 (the Hardy-Ramanujan number). This is WRONG: A₂(6) = 439/2, not 1729/4. The "1729 coincidence" is pattern-matching without computation. The correct values are (51, 179, 434, 878, 1585, 2641, ...) for 4·A₂(N) — none of these is 1729. Found 2026-04-07 by the A₂(N) combinatorics agent. **Rule: NEVER conjecture a combinatorial identity based on isolated number-theoretic coincidences (especially beloved ones like 1729, 24, 12). Verify EVERY conjectured value by independent computation. The pattern-completion instinct (AP3) extends to arithmetic coincidences.**

**AP79 — W(p) strong generation count is 4 (T + sl_2 triplet), not 2 (just T + W).** The triplet algebra W(p) at weight 2p-1 has an sl_2 triplet of generators W^+, W^0, W^- plus the stress tensor T, giving FOUR strong generators. The previous `logarithmic_voa_shadow_engine.py` had `num_generators = 2` (conflating the sl_2 triplet as a single generator). Found and fixed 2026-04-07 by the deep Beilinson rectification. **Rule: when counting strong generators, count the full set of fields, not isotypic components. An sl_2 triplet contributes 3 generators, not 1.**

**AP80 — Agents can produce an engine without a test file due to context truncation.** The CE vs chiral bar reconciliation agent (2026-04-07) wrote a 40KB engine file but was truncated before writing any tests. A follow-up audit step must always verify BOTH engine AND test files exist. **Rule: after every agent completion, check `ls compute/lib/<name>.py` AND `ls compute/tests/test_<name>.py`. If only the engine exists, relaunch specifically for the test file.**

### Anti-Patterns from the 2026-04-08 Bar/SC/E_1 Primacy Research (AP81-AP104)

The 22-agent bar construction / Swiss-cheese / E_1 primacy investigation catalogued the following operadic, coalgebraic, and architectural anti-patterns. These arise at the OPERADIC LAYER — the interface between operad theory and the manuscript's bar/cobar machinery.

**AP81 — Operadic bar of a P-algebra ≠ operadic bar of the operad P.** The operadic bar of an OPERAD P is the cofree COOPERAD generated by s⁻¹P̄ — a cooperad in S-modules. The operadic bar of an ALGEBRA A over P is the cofree P¡-coalgebra on s⁻¹Ā — a coalgebra over the Koszul dual cooperad P¡. These live at DIFFERENT categorical levels: BP is a cooperad, B_P(A) is a P¡-coalgebra. The error: writing "B(P)" when "B_P(A)" is meant, or vice versa. Found in algebraic_foundations.tex (2026-04-08, agent a34b1bc6). **Rule: use BP for the operadic/cooperadic bar of an operad; use B_P(A) for the bar of a P-algebra A. Never use a bare "B" without specifying which input it acts on.**

**AP82 — Three coalgebra structures on the bar: Lie^c, Sym^c, T^c.** The same underlying graded vector space carries THREE genuinely different cofree-coalgebra structures. (a) The coLie cooperad gives the HARRISON cofree coalgebra Lie^c — antisymmetric, with Lie cobracket, used by Andre-Quillen and as the operadic bar of Com-algebras. (b) The Sym^c structure (cocommutative coshuffle) is BOTH cocommutative AND coassociative, with 2^n terms summing over all bipartitions; this is the factorization coalgebra on Ran(X). (c) The T^c structure (deconcatenation) is coassociative but NOT cocommutative, with n+1 terms from consecutive cuts; this is the standard Stasheff tensor coalgebra and the E_1 bar. The error: assuming "the bar coalgebra" is unambiguous. **Rule: state which of Lie^c, Sym^c, T^c is meant. Default for the operadic bar of A∞-algebras is T^c (Stasheff). Default for factorization coalgebras on Ran(X) is Sym^c. Never write "the cofree coalgebra on s⁻¹Ā" without specifying which cooperad.**

**AP83 — Coshuffle ≠ deconcatenation.** The COSHUFFLE coproduct on Sym^c sums over ALL bipartitions of an unordered set: 2^n terms. The DECONCATENATION coproduct on T^c sums over CONSECUTIVE cuts of an ordered tuple: n+1 terms. At n=2 they superficially resemble each other (3 vs 3 terms modulo augmentation); at n≥3 they differ dramatically (8 vs 4 terms). Found at line 1563 of bar_construction.tex where a coderivation proof referred to the coshuffle as "deconcatenation." Corrected by agent a728d5ec (2026-04-08). **Rule: count the terms. 2^n summands = coshuffle (cocommutative). n+1 summands = deconcatenation (non-cocommutative). NEVER use the terms interchangeably.**

**AP84 — B_{Com}(A) is a cofree coLie coalgebra, NOT cocommutative.** The operadic bar of a commutative algebra (over Com) is a coalgebra over Com¡ = Lie^c. The output is a HARRISON COMPLEX with coLie cobracket. The cocommutative coalgebra Sym^c on Λ(s⁻¹Ā) is the Chevalley-Eilenberg complex of A viewed as an abelian Lie algebra — a DIFFERENT model computing the same cohomology in characteristic 0 via the antisymmetrization map. They are quasi-isomorphic in char 0 but live in different operadic categories. **Rule: NEVER write "B_{Com}(A) is cocommutative." The CE complex is cocommutative; the operadic bar B_{Com}(A) is coLie. They compute the same homology but are categorically distinct.**

**AP85 — Factorization coproduct ≠ deconcatenation coproduct; they live on different objects.** The FACTORIZATION coproduct of B^Σ(A) on Ran(X) is cocommutative: it sums over all unordered bipartitions I⊔J, inherited from the factorization isomorphism on Ran(X). The DECONCATENATION coproduct on B^ord(A) = T^c(s⁻¹Ā) is NOT cocommutative: it sums over n+1 consecutive splittings. They live on different objects (Sym^c vs T^c), arise from different geometries (unordered Ran(X) vs ordered Conf_n^<(R)), and detect different data (E_∞-coalgebra vs E_1-coalgebra). The R-matrix descent B^Σ ≃ (B^ord)^{R-Σ_n} relates them. **Rule: do NOT identify the Vol I factorization coproduct with the Vol II deconcatenation coproduct. The Vol I bar B^Σ(A) has the coshuffle (cocommutative). The Vol II bar B^ord(A) has deconcatenation (non-cocommutative). The Swiss-cheese SC^{ch,top} packages BOTH simultaneously.**

**AP86 — FM_n(X) does not factor as a product; only its boundary strata do.** The Fulton-MacPherson compactification FM_n(X) is a connected manifold with corners obtained by iterated real blowup along diagonals. It CANNOT be written as FM_a(X) × FM_b(X). However, each codimension-1 boundary stratum D_S ≃ FM_{|S|} × FM_{n-|S|+1} (cluster plus residual). The bar coproduct restricts forms via these BOUNDARY STRATA, not via a global product decomposition. The error: treating the bar coproduct as if FM_n factored globally. **Rule: FM_n(X) is connected; only its boundary strata factor. The factorization coproduct arises from RESTRICTION TO boundary strata, not from a global product decomposition. Name the boundary stratum when writing the coproduct.**

**AP87 — SC^{ch,top,!} mixed-sector dimension is (k-1)!·C(k+m,m), NOT (k-1)!·m!.** The Koszul dual cooperad of SC^{ch,top} has mixed-sector components parametrizing operations with k closed and m open inputs. The dimension is (k-1)!·C(k+m,m) — Lie/cyclic orderings of k closed inputs times C(k+m,m) shuffles of m open inputs. It is NOT the naive product (k-1)!·m!. The shuffle binomial C(k+m,m) counts how m open inputs interleave with the cyclically-ordered k closed inputs along the boundary of a Swiss-cheese disk. Computed by sc_koszul_dual_cooperad_engine.py (2026-04-08). **Rule: mixed-sector dimensions for SC^{ch,top,!} are Lie ⊗ shuffles, not Lie ⊗ ordered tuples. NEVER use a plain product of factorials for mixed-sector dimensions.**

**AP88 — Koszul dual cooperad P¡ vs Koszul dual operad P^! notation collision.** The PRIMITIVE notion is the cooperad P¡ (Loday-Vallette: S-module cooperad of cogenerators, dual to the relations of P). The operad P^! = (P¡)^∨ is its linear dual. They contain the same information but live in dual categorical settings. The "!" notation is used inconsistently in the literature: some authors use P^! for the cooperad, others for the operad. Found in algebraic_foundations.tex (2026-04-08) where "Ass^!" was used for the cooperad (Ass^! = Ass as an operad; the cooperad is Ass¡ = Ass^c with desuspension). **Rule: use P¡ for the cooperad and P^! for its linear-dual operad. State the categorical level explicitly: "the Koszul dual COOPERAD P¡" vs "the Koszul dual OPERAD P^!."**

**AP89 — Type-checking violation: B_{SC}(A) for a one-coloured input A is ill-formed.** The Swiss-cheese operad SC^{ch,top} is TWO-COLOURED. An SC^{ch,top}-algebra is a PAIR (V_c, V_o). The operadic bar B_{SC} requires a two-coloured pair as input, not a single chiral algebra. Writing "B_{SC}(A)" is a type error. **Rule: B_{SC} requires a two-coloured input (V_c, V_o). For a one-coloured chiral algebra A, use the promotion functor (AP90): A ↦ (A, A). Write B_{SC}(A, A), not B_{SC}(A).**

**AP90 — Promotion functor A ↦ (A, A): a chiral algebra is its own boundary module by self-action.** Given a chiral algebra A (one-coloured), the canonical promotion to an SC^{ch,top}-algebra is (V_c, V_o) := (A, A), where A acts on itself by its own algebra structure. The operadic bar B_{SC}(A, A) decomposes into: closed sector B_{closed}(A) ≃ B_{Com}(A), open sector B_{open}(A) ≃ B_{Ass}(A), and mixed sector. This is how the Vol I bar (one-coloured) connects to the Vol II Swiss-cheese bar (two-coloured). **Rule: when transporting Vol I results to the Vol II Swiss-cheese setting, ALWAYS use the promotion A ↦ (A, A). The closed-sector projection recovers the Vol I bar; the open-sector projection produces the boundary/Yangian dual.**

**AP91 — Curved differential d² = κ·ω_g is NOT a coderivation at genus g ≥ 1.** At genus g ≥ 1, the bar differential acquires curvature d² = κ(A)·ω_g. Despite κ·ω_g being a scalar central element, d (with d² ≠ 0) is NOT a coderivation of the bar coproduct. The cross terms 2(d⊗d)∘Δ at interior splittings produce TWICE the contribution of d²∘Δ — a factor-2 discrepancy verified for Heisenberg at genus 1 by curved_sc_higher_genus_engine (2026-04-08). Only the period-corrected differential D^{(g)} (Fay trisecant + period integrals) IS both flat AND a coderivation. **Rule: NEVER claim the curved bar differential at g ≥ 1 is a coderivation. Centrality of κ·ω_g is necessary but NOT sufficient — the coderivation condition involves cross terms at interior splittings that curvature breaks.**

**AP92 — Algebra-level curvature μ_0 (genus 0, strict) vs fiberwise curvature d_fib² = κ·ω_g (genus ≥ 1, Hodge-class).** Two distinct curvature loci on the bar complex. (a) The ALGEBRA-LEVEL curvature μ_0 is a scalar central element of A proportional to the unit; at GENUS 0, μ_0 = 0 and d² = 0 strictly. (b) The FIBERWISE curvature d_fib² = κ(A)·ω_g at genus g ≥ 1 lives on the Hodge bundle over M̄_g and reflects global geometry. Both are scalar and central; ONLY the fiberwise version has the coderivation problem (AP91). Distinguished by agent ab23aca7 (2026-04-08). **Rule: μ_0 (algebra-level, genus 0) and d_fib² = κ·ω_g (fiberwise, genus ≥ 1) are DIFFERENT objects at different scales. State which is meant.**

**AP93 — δF_g^cross lives in the CLOSED sector, NOT the mixed sector.** For multi-weight algebras at genus g ≥ 2, the cross-channel correction δF_g^cross arises from CLOSED-sector mixed-channel graph sums on M̄_{g,0} — no open inputs. The "mixed-channel" in "δF_g^cross" refers to MIXED PROPAGATOR CHANNELS within the closed sector (different generators paired through different pole structures), not the open/closed mixed sector of Swiss-cheese. Agent 18 hypothesized mixed sector; agent 16 falsified this (2026-04-08). **Rule: "mixed channels" (propagator structure within the closed sector) and "mixed sector" (closed-open interaction in SC^{ch,top}) share an adjective but live in different operadic structures. Cross-channel free-energy corrections live in the closed sector.**

**AP94 — Polynomial Hilbert series ≠ polynomial RING (CRITICAL).** ChirHoch^*(Vir_c) was claimed to be "a polynomial ring ℂ[Θ]" with infinite-dimensional cohomology. WRONG. Vol I Theorem H proves concentration in degrees {0, 1, 2}: total dimension ≤ 4. "Polynomial growth" refers to the Hilbert series being a polynomial of degree ≤ 2, NOT to cohomology being a polynomial ring. Found by agent a237e09b in chiral_center_theorem (2026-04-08), propagated to 4 files. **Rule: "polynomial Hilbert series" means the dimension function is a polynomial; it does NOT mean a polynomial ring. ChirHoch^*(modular Koszul A) has TOTAL DIMENSION ≤ 4 over ℂ. NEVER write "ChirHoch^*(A) = ℂ[Θ]."**

**AP95 — Chiral Hochschild cohomology ≠ Gel'fand-Fuchs cohomology of Diff(S¹).** H^*_{GF}(Diff(S¹)) IS infinite-dimensional (Godbillon-Vey class and descendants). ChirHoch^*(Vir_c) is bounded by Vol I Theorem H: concentrated in {0, 1, 2}. The two are UNRELATED: GF is for the Lie algebra Vect(S¹) (no central charge, no chiral structure); ChirHoch is for the Virasoro vertex algebra on a 1d algebraic curve. The error: invoking GF to justify "infinite-dimensional ChirHoch." Found in chiral_center_theorem.tex (2026-04-08). **Rule: NEVER cite Gel'fand-Fuchs to predict ChirHoch dimensions. The authoritative bound is Theorem H.**

**AP96 — Shadow algebra A^sh is a bigraded LIE ALGEBRA, NOT a graded-commutative ring.** The shadow algebra A^sh = H_•(Def_cyc^mod) at line 11345 of higher_genus_modular_koszul.tex carries a graded LIE BRACKET of degree 0 with arity map r_1 × r_2 → r_1 + r_2 - 2. The bracket is ANTISYMMETRIC and satisfies Jacobi. The named shadows κ, C, Q are projections of MC elements under this Lie bracket, not multiplicative generators. Found in 3 instances by agent a1b6a0ee (2026-04-08), with propagation targets at preface line 5423 and introduction line 2486. **Rule: NEVER call the shadow algebra a "ring." It is a graded Lie algebra. The bracket descends from the convolution bracket on Def_cyc^mod. Use [κ, C] for bracket; never write κ·C as a product.**

**AP97 — The averaging map av: g^{E_1} → g^mod is a LOSSY projection.** The E_1 convolution algebra g^{E_1} (on T^c) is strictly richer than the modular algebra g^mod (on Sym^c). The averaging map av is the Σ_n-coinvariant projection, which FORGETS the linear ordering. At arity 2: av(r(z)) = κ(A) — the R-matrix has a z-dependent profile killed by coinvariance. At arity n: av(Θ^{E_1}_n) = (Θ_A)_n. The shadow obstruction tower is the coinvariant image of the ordered MC element. **Rule: av is a projection, not an isomorphism. NEVER claim the modular tower contains the same information as the ordered tower. The R-matrix r(z) ∈ g^{E_1} has more information than κ ∈ g^mod. The ordered story is the primitive; the modular story is the av-image.**

**AP98 — κ Eulerian weight is representation-dependent (parity of desuspended generator).** For HEISENBERG (s⁻¹J of degree 0 = even): Σ_2 acts trivially on (s⁻¹J)^⊗2, so κ(H) lives in SYMMETRIC Eulerian weight 2 — invisible to Harrison/coLie. For VIRASORO (s⁻¹T of degree 1 = odd): Σ_2 acts by sign on (s⁻¹T)^⊗2, so κ(Vir) lives in ANTISYMMETRIC Harrison weight 1. Both are consistent within Sym^c, but the Eulerian-weight decomposition differs by parity. **Rule: when computing κ in the Eulerian/Harrison decomposition, check the parity of the desuspended generator. Even → symmetric weight 2 (Harrison-invisible). Odd → antisymmetric weight 1 (Harrison-visible). The weight decomposition is parity-dependent.**

**AP99 — Lagrangian Koszulness criterion (K11) is CONDITIONAL: two hidden hypotheses.** Theorem thm:ambient-complementarity-tangent items (i)-(ii) (nondegeneracy, isotropy) are UNCONDITIONAL. Item (iii) (Lagrangian property: T_A^⊥ = T_{A!}) is CONDITIONAL on: (a) PERFECTNESS of the cyclic pairing restricted to tangent complexes, and (b) BAR-COBAR identification of the normal complex. Flagged by agent ac37cca2 (2026-04-08). The original meta-theorem listed K11 as unconditional. **Rule: NEVER list K11 as unconditional. State both hypotheses explicitly: perfectness of the cyclic pairing AND bar-cobar identification of the normal complex.**

**AP100 — Theorem C eigenspace decomposition (C1) is unconditional; scalar identity F_g = κ·λ_g (C2) is multi-weight conditional.** Theorem C has two layers. (C1) The eigenspace decomposition of H^•(M̄_g, Z(A)) under the complementarity action is UNCONDITIONAL for all modular Koszul algebras at all genera. (C2) The scalar identity F_g(A) = κ(A)·λ_g^FP requires the uniform-weight lane. For multi-weight algebras at g ≥ 2: F_g = κ·λ_g^FP + δF_g^cross. The error: citing "Theorem C" universally without specifying which layer. **Rule: state which layer. (C1) is unconditional. (C2) requires uniform weight. For multi-weight at g ≥ 2, use the corrected formula F_g = κ·λ_g^FP + δF_g^cross.**

**AP101 — "qi, not merely iso on cohomology" is technically vacuous.** A quasi-isomorphism IS by definition a chain map inducing iso on cohomology. The intended distinction is between (a) a qi OF A∞-ALGEBRAS (structure-respecting, intertwining all m_k) and (b) a bare chain map that happens to induce iso on cohomology but does NOT respect higher structure. Found in bar_cobar_inversion.tex by agent af4c2790 (2026-04-08). **Rule: use "qi of A∞-algebras" or "qi of SC^{ch,top}-algebras" for the structured notion; "chain qi" for the linear notion. NEVER write "qi, not merely iso on cohomology" — it is tautological.**

**AP102 — Theorem statements MUST specify which bar complex (B^ord, B^Σ, or B^Lie).** Theorems about "the bar complex" without specifying B^ord (ordered, T^c, deconcatenation, E_1), B^Σ (symmetric, Sym^c, factorization, E_∞), or B^Lie = B^FG (Francis-Gaitsgory, Lie^c, zeroth pole) are AMBIGUOUS. The deconcatenation coproduct only makes sense on B^ord; the factorization coproduct only on B^Σ. Theorem thm:bar-swiss-cheese was originally stated on generic "B̄^ch" but requires B^ord — the theorem is false on B^Σ as written. Fixed by agent a58a1d66 (2026-04-08). **Rule: every theorem involving "the bar complex" MUST name which bar. Swiss-cheese theorem → B^ord. Factorization coalgebra theorem → B^Σ. FG/chiral Lie theorem → B^Lie.**

**AP103 — Cotriple bar resolution ≠ Koszul-dual operadic bar.** The COTRIPLE (monadic, simplicial) bar B^cotr(P, A) = ... → P∘P∘A → P∘A is the standard free resolution from the monad P; it always exists for any P and any P-algebra A. The KOSZUL-DUAL operadic bar B_P(A) = P¡ ∘ A is the cofree P¡-coalgebra on s⁻¹Ā; it requires the Koszul locus. They agree as computing Tor on the Koszul locus but are different objects in different categories (one is a simplicial P-algebra, the other is a P¡-coalgebra). **Rule: state which bar resolution. Cotriple is always defined, lives in P-algebras. Operadic requires Koszulness, lives in P¡-coalgebras. They agree as Tor in char 0 on the Koszul locus but are categorically distinct.**

**AP104 — The E_1/ordered story is the primitive; the modular/symmetric story is the av-image (architectural anti-pattern).** The primitive mathematical structure is B^ord(A) on T^c with deconcatenation, the convolution algebra g^{E_1}_A, the MC element Θ^{E_1}_A, and the R-matrix r(z). The modular story (B^Σ(A), g^mod_A, Θ_A, κ(A), shadow obstruction tower) is the IMAGE under av. NEVER write text that treats the E_1/ordered story as "an extension," "a refinement," "a physics application," "auxiliary," or "frontier-facing." It is THE primitive. The modular/symmetric story is the av-image. The framing direction is reversed in the "E_1/Ordered as Primitive" architectural section. **Rule: when introducing any bar-complex object, state its E_1/ordered version first, then describe the modular version as its av-image. NEVER present the modular story as primary and the ordered story as derived.**

**AP105 — Heisenberg = abelian KM at level k = boundary algebra of abelian U(1) Chern-Simons. These are the SAME algebra.** The OPE is J(z)J(w) ~ k/(z-w)² (double pole); the λ-bracket is {J_λ J} = kλ. The confusion arose from conflating three distinct brackets: (a) the zero-mode Lie bracket J₍₀₎J = 0 (vanishes — the underlying finite-dimensional Lie algebra is abelian), (b) the λ-bracket / full singular OPE {J_λ J} = kλ (nonzero — the level k survives as kλ), (c) the secondary odd Poisson bracket in 3d holomorphic twists (Costello-Dimofte-Gaiotto) — a different bracket from the VOA current OPE. A fictional "abelian CS algebra" with simple-pole OPE J(z)J(w) ~ k/(z-w) was sometimes described. This is IMPOSSIBLE for an even bosonic current: PVA skew-symmetry {J_λ J} = -{J_{-λ-∂} J} applied to a constant bracket gives k = -k, forcing k = 0. Only ODD generators can have constant λ-brackets (the sign flips for odd parity). The correct simple-pole algebra is the odd current algebra (symplectic fermion / bc ghost self-bracket), which is a DIFFERENT object from both Heisenberg and abelian CS. See rem:abelian-cs-is-heisenberg in heisenberg_frame.tex. **Rule: NEVER treat "abelian CS boundary algebra" as a different algebra from Heisenberg. They are the same: OPE J(z)J(w) ~ k/(z-w)² (double pole), λ-bracket {J_λ J} = kλ. The 3d bulk theory is legitimately called "abelian Chern-Simons"; the 2d boundary algebra is the Heisenberg = abelian KM at level k. The simple-pole algebra with OPE k/(z-w) requires an ODD generator (symplectic fermion / bc ghost); it is the odd current algebra, not "abelian CS."**

### Anti-Patterns from the 2026-04-08 Wave 2-3 Architectural Audit (AP106-AP115)

The 43-agent session (10 RED + 10 FRONTIER + 10 COHERENCE + 13 supplementary) catalogued the following PROSE-ARCHITECTURAL anti-patterns. These arise at the EXPOSITORY LAYER — the interface between the Chriss-Ginzburg standard and the actual .tex source.

**AP106 — "This chapter constructs..." narration pattern (meta-expository announcement).** 26 instances found across Vol I chapter openings. The Chriss-Ginzburg standard: the chapter IS the construction; you do not announce what you are about to do, you do it. "This chapter constructs the bar complex" has zero mathematical content — the reader already knows what the chapter will do from its title. The CG opening move is the DEFICIENCY OPENING: state the problem that forces the construction, not the construction itself. "The bar-cobar adjunction of Theorem A requires a coalgebra structure on the bar complex" — the reader now knows WHY the construction exists, not just THAT it exists. Found in 26 chapter openings across Vols I-II during RED-1 through RED-5 audits (2026-04-08). Same pattern: "In this section we prove..." (the section title already says this); "We now turn to..." (transition filler); "The goal of this part is..." (Part-level announcements belong in the Part epigraph, not the first chapter). **Rule: NEVER open a chapter, section, or part with "This chapter/section/part constructs/proves/studies..." The opening sentence states the MATHEMATICAL PROBLEM that the chapter solves. The construction appears when the problem demands it. If you cannot state the problem in one sentence, the chapter lacks a clear mathematical purpose.**

**AP107 — r^coll (bar-intrinsic collision residue) ≠ r(z) (Laplace transform of λ-bracket).** Two objects share the name "r-matrix" but are defined by different operations: (a) r^coll(z) = Res^{coll}_{0,2}(Θ_A) is the BAR-INTRINSIC collision residue — it extracts the arity-2 component of the MC element Θ_A via the collision map on FM_2(X), (b) r(z) = ∫₀^∞ e^{-λz}{·_λ·}dλ is the LAPLACE TRANSFORM of the λ-bracket — it sums all OPE modes with exponential weights. For Heisenberg (single mode J_{(1)}J = k): r^coll(z) = k/z AND r(z) = k/z — they coincide because there is only one OPE mode. For affine KM (two modes J_{(0)}J = [J,J], J_{(1)}J = kδ): both give r(z) = Ω/z (the Casimir) — they still coincide because d log absorption (AP19) converts the two-mode OPE to a single-pole r-matrix. For the ODD CURRENT (single mode b_{(0)}b = k, weight-0 bracket): r^coll = k (constant, no z-dependence — the collision residue of a simple-pole OPE is a constant by AP19) but r(z) = k/z (the Laplace transform of a constant λ-bracket is k/z). These DIVERGE. The discrepancy: the collision residue sees the GEOMETRIC pole structure (d log kernel), while the Laplace transform sees the ALGEBRAIC mode structure (λ-bracket generating function). They agree when the algebra is E_∞-commutative and even-parity; they can diverge for odd-parity or non-standard algebras. Found during Heisenberg = abelian CS resolution (2026-04-08). **Rule: when writing "the r-matrix of A," specify which: bar-intrinsic r^coll(z) = Res^{coll}_{0,2}(Θ_A) or Laplace r(z) = ∫e^{-λz}{·_λ·}dλ. Tables must label columns. For standard even-parity E_∞ algebras they coincide; for odd generators or genuinely E_1 algebras, verify independently.**

**AP108 — "Atom" applied to the Heisenberg (CG opening ≠ theory primitive).** The Heisenberg is the correct Chriss-Ginzburg OPENING: the simplest commutative (E_∞) chiral algebra, exhibiting all invariants (κ, genus tower, complementarity) on the simplest object. But it is NOT the "atom" of the theory in the sense of the simplest object from which the theory is BUILT. The atom of E_1-E_1 operadic Koszul duality should be a genuinely NONLOCAL chiral algebra (tier (c): Yangian, Etingof-Kazhdan quantum VA, or twisted lattice VOA like V_{A₂}^{3,1}). The monograph opens in the E_∞ world (Heisenberg) and progressively reveals the E_1 world; calling the Heisenberg the "atom" suggests it is the primitive of the full theory when it is only the primitive of the commutative sector. The error was identified during the COHERENCE wave (2026-04-08) after the Heisenberg = abelian CS resolution exposed the two-atom design as comparing an algebra with itself. **Rule: the Heisenberg is the CG OPENING (simplest example, all invariants visible). It is NOT the atom of the E_1 world. NEVER write "the Heisenberg is the atom of the theory" without qualifying "of the commutative/E_∞ sector." The atom of the full E_1 theory is a nonlocal chiral algebra. The architectural role of the Heisenberg is "simplest illustration," not "fundamental building block."**

**AP109 — Forward-reference previews (trailers) in chapter openings.** Listing "this chapter will prove Theorems X, Y, Z" before proving them adds zero mathematical content and violates the CG momentum principle: every paragraph forces the next. A preview paragraph is a paragraph that could be removed without the reader noticing — the theorems will appear when proved. The CG alternative: state the PROBLEM in one sentence, then let the construction unfold with the theorems appearing at the moments of maximum mathematical necessity. Found in 15+ chapter openings across Vols I-II during RED-1 through RED-5 audits (2026-04-08). Same pattern: "Outline of the chapter" subsections (tables of contents masquerading as mathematics); "Roadmap" remarks; "The plan is as follows..." paragraphs. **Rule: NEVER list results before proving them. Let theorems appear when the mathematics demands them. If a chapter needs a roadmap, the chapter structure is unclear — fix the structure, not the introduction. The sole exception: the PREFACE and INTRODUCTION, which survey the entire monograph. Chapter openings are not introductions to themselves.**

**AP110 — Preface/introduction describing other volumes.** "Volume II constructs..." or "In Volume III we will..." is narration about a different document that the reader may not have. Each volume's preface opens its own story: the problem it solves, the tools it builds, the theorems it proves. Cross-volume references belong in clearly marked "Connections to Volume N" subsections, not in the main narrative thread. Found in Vol I preface (describing Vol II/III at length), Vol II preface (describing Vol I), and Vol III introduction (describing Vol I/II) during RED-4, RED-5, RED-9 audits (2026-04-08). The deeper issue: describing another volume's content is a form of AP41 (prose about mathematics that is not present) — the reader cannot verify the description, and descriptions drift as the other volume evolves (AP112, AAP8). **Rule: each volume's preface/introduction tells its OWN story. Cross-volume connections appear in clearly delineated subsections or forward-reference remarks, never in the main narrative flow. "Volume II constructs X" is replaced by "The construction of X (treated in Volume II) provides..." — the mathematical object is named, not the book.**

**AP111 — "What this chapter proves" remark blocks.** Remark environments titled "What this chapter proves" or "Summary of results" function as tables of contents, not CG deficiency moves. They duplicate the theorem statements that follow, creating maintenance burden (AP5 within a single file) and bloating the page count without adding mathematical content. The CG principle: the opening sentence states the PROBLEM; the theorems appear when the construction demands them; no intermediate catalogue is needed. Found in 8 chapters across Vol I during RED-1 through RED-3 audits (2026-04-08). Same pattern: "Overview" subsections that restate every definition and theorem before presenting them; "Recap" subsections that restate what was just proved. These are symptoms of AP106 (narration about mathematics rather than mathematics). **Rule: NEVER create a "What this chapter proves" or "Summary of results" remark block inside a chapter. If the chapter structure is clear, the reader does not need a table of contents. If it is unclear, restructure the chapter. The sole exception: the concordance (concordance.tex), which is explicitly a cross-reference document.**

**AP112 — Memory file page counts diverging from build reality.** Memory files (MEMORY.md, session summaries) record page counts at the moment of writing. These become stale as the manuscript evolves. The 2026-04-08 session found memory claims of "Vol I: 2,541pp" while the actual build produced 2,451pp — a 90-page discrepancy. Agents reading memory files plan work based on page counts; stale counts produce wrong estimates of scope, coverage, and remaining work. The root cause: page counts are written by agents at session end but never updated when subsequent sessions modify the manuscript. **Rule: NEVER trust a page count from a memory file without verifying against a fresh build. When writing a session summary, record the page count from the ACTUAL build output, not from memory or previous session summaries. Mark all page counts with the date they were recorded. When a build produces a count differing by more than 5% from memory, update the memory file.**

**AP113 — κ-spectrum polysemy (AP9 generalized to the CY setting).** In Vol III (calabi-yau-quantum-groups), multiple κ values coexist for a single CY threefold X: (a) κ_ch = chiral modular characteristic of the associated chiral algebra A_X, (b) κ_BKM = BKM shadow coefficient from the BKM denominator formula, (c) κ_cat = categorical κ from the DT category DT(X), (d) κ_fiber = κ of the elliptic fiber for elliptically fibered X. Writing bare "κ" without subscript invites conflation (AP9 meta-principle). The 2026-04-08 RED-7 audit found κ(K3×E) = 3 vs κ(K3×E) = 5 in two different chapters of Vol III — a CRITICAL contradiction arising from different κ definitions (one was κ_ch = Euler/4 = 3, the other was κ_BKM from the BKM product = 5). **Rule: in Vol III and any context where multiple κ-like invariants coexist, ALWAYS subscript: κ_ch, κ_BKM, κ_cat, κ_fiber. Bare "κ" is FORBIDDEN in multi-κ contexts. Before writing any κ value, state which definition is being used.**

**AP114 — Skeletal stub chapters appearing in compiled documents.** A chapter with fewer than 50 lines of content and no theorem/proposition/definition environments creates a false impression of completeness when it appears in the compiled PDF. The reader encounters a chapter title, perhaps a one-paragraph introduction, and then the next chapter — suggesting the material is "covered" when it is not. Found in 12 stub chapters in Vol III during RED-7 audit (2026-04-08). Same pattern in Vol I: frontier chapters with only a section header and a forward reference. **Rule: a chapter included in main.tex via \\include MUST contain at least one formal mathematical environment (definition, theorem, proposition, or computation). If the chapter has no mathematical content, comment out the \\include line and add a TODO. NEVER ship a stub chapter in a compiled document — it is worse than omitting it entirely, because it suggests coverage where none exists.**

**AP115 — E_1 primacy declared in CLAUDE.md but not enacted in .tex source (metadata-source gap).** The architectural commitment (2026-04-08, inscribed in CLAUDE.md and concordance.tex) says B^ord is the primitive bar complex and the modular/symmetric bar is the av-image. But bar_construction.tex opens with B^Σ (the symmetric/factorization bar) and treats B^ord as a later variant. The preface describes the bar complex in terms of the factorization coalgebra (B^Σ), not the tensor coalgebra (B^ord). This is the most dangerous failure mode: the metadata layer (CLAUDE.md, concordance, memory files) describes the INTENDED architecture, while the source (.tex) still enacts the OLD architecture. An agent reading CLAUDE.md will believe E_1 is primary; an agent reading bar_construction.tex will write text treating E_∞ as primary. The gap between metadata intent and source reality produces contradictory prose across the manuscript. Found during COHERENCE wave (2026-04-08): 10 agents attempted to enforce E_1 primacy but found the source chapters still framed the symmetric bar first. **Rule: EVERY architectural commitment inscribed in CLAUDE.md or concordance.tex MUST be enacted in the .tex source within the same session or the next. A metadata claim about "what the manuscript does" is FALSE until the manuscript actually does it. When an architectural directive cannot be immediately enacted (too large, too risky), record it as a TODO in concordance.tex with an explicit timeline, NOT as a present-tense assertion in CLAUDE.md. The gap between metadata and source is the single most dangerous anti-pattern — it produces agents that confidently write text contradicting the actual manuscript.**

---

**The meta-rule: never trust a coincidence that holds in special cases. Verify at the most general case, at the highest weight, at the most general level, at the most general algebra family.**

**The meta-meta-rule (from AP28-AP32): the same error can recur at different abstraction levels.** AP1-AP27 catch mathematical errors (wrong formulas, wrong objects). AP28-AP32 catch STRUCTURAL errors in how the manuscript TALKS ABOUT its own results: undefined terminology applied systematically (AP28), conflated physical regimes (AP29), hidden axiom hypotheses (AP30), scalar-to-tower extrapolation (AP31), genus-to-all-genera extrapolation (AP32). These are METACOGNITIVE errors — the mathematics may be correct in the theorem statement, but the CROSS-REFERENCE NETWORK propagates overclaims. The most dangerous errors are not wrong formulas; they are correct formulas cited at the wrong scope.

**The meta-meta-meta-rule (from AP35-AP43): the same error can recur at different EPISTEMIC levels.** AP35-AP39 catch errors in the VERIFICATION LAYER: proofs that reach correct answers by wrong routes (AP35), implications upgraded to equivalences without proof (AP36), spectral sequence pages from heuristics not computation (AP37), literature values imported without convention checking (AP38), invariants that coincide in rank 1 but diverge in general (AP39). AP40-AP43 catch errors in the COMMUNICATION LAYER: environments that contradict tags (AP40), prose that contradicts formulas (AP41), slogans that are true at a sophisticated level but false naively (AP42), and central objects used without definition (AP43). The deepest errors are not in the mathematics, not in the cross-reference network, but in the INTERFACE between the mathematician's understanding and what appears on the page.

**The meta^4-rule (from AP62-AP80): the same error can recur at different STRUCTURAL levels.** AP62-AP80 catch errors in the COMPUTATION AND CLASSIFICATION LAYER: Euler characteristic ≠ dimension (AP62), CE ≠ chiral bar (AP63), grading confusion (AP64), ordered ≠ unordered (AP65), D-finiteness scope (AP66), strong ≠ free strong generation (AP67), PVA slab ≠ κ (AP68), KdV deformation (AP69), L-function pole structure (AP70), κ ≠ physical parameters (AP71), ordered NOP bar ≠ chiral bar (AP72), BV=sewing conditionality (AP73), Bernoulli-Dirichlet falsity (AP74), Koszulness grading confusion (AP75), Y-algebra central charge vanishing (AP76), convergent vs divergent (AP77), arithmetic coincidences (AP78), generator counting (AP79), engine-test completeness (AP80).

**The meta^5-rule (from AP81-AP105): the same error can recur at the OPERADIC-ARCHITECTURAL level.** AP81-AP105 catch errors in the OPERADIC LAYER: algebra-vs-operad bar conflation (AP81), three-coalgebra conflation (AP82), coshuffle ≠ deconcatenation (AP83), B_{Com} ≠ cocommutative (AP84), factorization ≠ deconcatenation coproduct (AP85), FM non-factoring (AP86), mixed-sector dimensions (AP87), cooperad ≠ operad notation (AP88), two-coloured type violations (AP89-AP90), curved coderivation failure (AP91-AP92), closed-vs-mixed sector (AP93), polynomial-ring conflation (AP94-AP95), shadow Lie-vs-ring (AP96), averaging lossy projection (AP97), Eulerian parity (AP98), K11 conditionality (AP99), Theorem C layers (AP100), qi tautology (AP101), bar disambiguation (AP102), cotriple ≠ operadic (AP103), E_1 primacy (AP104), Heisenberg = abelian CS boundary (AP105). The deepest errors are not in formulas, not in cross-references, not in communication, not in computation, but in the CATEGORICAL LEVEL at which bar-cobar operates — confusing which operad, which cooperad, which coalgebra structure, and which colour an operation lives in.

**The meta^6-rule (from AP106-AP115): the same error can recur at the EXPOSITORY-ARCHITECTURAL level.** AP106-AP115 catch errors in the PROSE LAYER: narration announcing construction instead of performing it (AP106), collision residue vs Laplace r-matrix conflation (AP107), CG opening conflated with theory primitive (AP108), forward-reference previews adding no content (AP109), cross-volume narration in preface (AP110), result-listing remark blocks (AP111), stale page counts in metadata (AP112), κ-spectrum polysemy across volumes (AP113), skeletal stub chapters creating false coverage (AP114), metadata-source architectural gap (AP115). These errors are not in formulas, not in cross-references, not in communication, not in computation, not in operadic structures, but in the INTERFACE BETWEEN ARCHITECTURAL INTENT AND TEXTUAL REALITY — the gap between what the metadata says the manuscript does and what the .tex source actually does.

### Agent Anti-Patterns (AAP): Systematic Errors in Automated Rectification

These patterns were identified by archaeological survey of 300 commits across all three volumes. They are distinct from AP1-AP50 (which catch mathematical errors): AAPs catch errors in the AGENT WORKFLOW LAYER — the interface between automated rectification tools and the codebase.

**AAP1 — Tool-markup leaking into source files.** XML/tool-call fragments (`</invoke>`, `<parameter>`, angle-bracket artifacts) can leak into .tex files when the agent confuses the content/envelope boundary. A single leaked character breaks a 2,400-page build with a cryptic error. **Rule:** After EVERY write to a .tex file, inspect the last 5 lines for XML/HTML artifacts. A pre-commit grep for `antml` or `</invoke>` in .tex files catches this before it reaches the build.

**AAP2 — Terminology rename campaigns fragmented across sessions.** A single terminology change ("shadow Postnikov tower" → "shadow obstruction tower") required 14+ commits across 3 volumes because each session missed variant spellings, compute-layer docstrings, CLAUDE.md, READMEs, or entire volumes. **Rule:** A terminology rename MUST be atomic across ALL THREE volumes in a single session. Use `grep -ri "old_term" ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups` with ALL variant forms. The rename is not complete until grep returns zero hits.

**AAP3 — Formula reimplemented N times in compute modules with independent divergent implementations.** The W_N central charge formula appeared in 29 library modules with independent implementations. When the formula was wrong, all 29 were wrong simultaneously. Similarly κ(H_k) = k/2 appeared in one engine while 10+ others correctly had k. **Rule:** Every family-specific formula must be implemented ONCE in a canonical module and imported everywhere else. No compute engine may implement its own local version. Grep for `def.*central_charge\|def.*kappa_formula` and eliminate duplicates.

**AAP4 — \\begin{proof} after \\begin{conjecture} (evidence masquerading as proof).** 20+ instances across 6 commits: an agent writes a conjectural claim correctly in a conjecture environment, then follows it with `\begin{proof}` containing heuristic justification. **Rule:** `\begin{proof}` may ONLY follow a theorem/proposition/lemma with `\ClaimStatusProvedHere`. For conjectures, use `\begin{remark}[Evidence]` or `\begin{remark}[Conditional derivation]`.

**AAP5 — Build-artifact commits obscuring mathematical history.** 30+ "Build artifacts: recompile" and "release pdf" commits across 3 volumes (~15-20% of commit history) carry zero mathematical content and obscure actual changes when agents read `git log`. **Rule:** Batch build artifacts with the content commit that produced them. Never commit build artifacts as standalone commits.

**AAP6 — Status oscillation: theorem → conjecture → theorem across sessions.** An agent writes a theorem, an audit agent downgrades it (cannot find the cross-volume proof), a third agent re-upgrades it. **Rule:** Before downgrading a `ProvedHere` claim, search ALL THREE volumes for the proof. Before writing a NEW theorem, verify the proof chain is complete in THIS session. Write claims at their final status level exactly once.

**AAP7 — Intra-file formula inconsistency: correct at line 300, wrong at line 600.** Agents process files in chunks (~200-500 lines). A formula stated correctly early in a file is regenerated from memory later in the same file, producing a different version. **Rule:** Before writing ANY formula that appears elsewhere in the SAME file, grep the current file for all variant forms. Read the earlier instance before writing the later one.

**AAP8 — README/metadata claims diverge from source truth (documentation drift).** README badges and prose are written by agents optimizing for impressive claims, not accuracy. "Computationally verified at arities 2-6" was false: tests verified only the BKM side, not the shadow tower. **Rule:** README claims must be independently verifiable by reading the test suite. Before writing "verified," read the test assertions to confirm they test what you claim.

**AAP9 — Premature agent relaunch causes cascading rate limits.** Relaunching an agent while other agents from the current batch are still running can trigger rate limits for ALL concurrently running agents. In the 2026-04-07 session this happened multiple times: relaunches triggered while previous batches were finishing caused 3-8 agents to hit the rate limit simultaneously. **Rule:** wait for EVERY agent from the current batch to send its completion task-notification before launching any new agents. Check `ls` on the tasks output directory and verify each file is stable (not growing) before launching. Never overlap batches.

**AAP10 — Agents can produce an engine file without a test file due to context truncation.** An agent may exhaust its context budget after writing the engine but before writing the test file, resulting in a zero-test "complete" engine. The CE vs chiral bar reconciliation agent did exactly this on 2026-04-07 (40KB engine, no test file). **Rule:** after every agent completion, verify BOTH the engine file AND the test file exist with non-trivial size. Run `ls compute/lib/<name>.py compute/tests/test_<name>.py`. If only the engine exists, immediately relaunch specifically to write the test file. Never count an agent "done" without both artifacts.

**AAP11 — Test expectations can encode anti-patterns (AP10 at the test level).** Tests with hardcoded wrong expected values silently pass when the engine has matching wrong values. The 2026-04-07 session found: sl₂ tests expected Riordan numbers [3, 6, 15, ...] when the correct CE cohomology gives [3, 5, 7, ...] at weights n(n+1)/2. 16 such AP10 violations were found and fixed across 12 files during the RED κ rectification. **Rule:** every hardcoded test expected value must be derivable by at least TWO independent computation paths. If the expected value can only be verified by matching the engine output, it's not a real test — it's a tautology.

**AAP12 — Tolerance bounds in asymptotic tests can be too tight.** Tests like `assert abs(ratio - 3.0) < 0.1` may fail at small sample sizes where convergence hasn't kicked in. The W₅/W₆ engine test failed at 20-term truncation with ratio 2.808 (needed 0.25 tolerance, not 0.1). Similarly, the δF₂ intersection engine had large-c asymptotic tolerance issues. **Rule:** for asymptotic tests, either (a) use a tolerance proportional to 1/log(N), (b) use a large enough sample that convergence is below machine epsilon, or (c) verify asymptotic behavior via two independent methods (ratio test AND direct formula).

**AAP13 — Silent model downgrade without testing.** When a 429 rate limit is observed, do NOT silently downgrade to a weaker model. Always test availability (a quick probe). Never downgrade without explicit user permission. Found 2026-04-07 when all 5 Tier 0 agents were downgraded from opus to sonnet without testing. **Rule:** on rate limit, wait and retry; never downgrade silently.

**AAP14 — Worktree branch collisions across agents.** Multiple agents in worktree isolation can end up sharing the same git branch unintentionally. **Rule:** verify worktree branch ownership before assuming a branch is dedicated to the current agent. Each agent should have a unique branch name derived from the agent ID.

**AAP15 — Parallel pdflatex SIGKILL races.** When multiple agent sessions run pdflatex concurrently in the same working directory, they kill each other's builds via pkill -9 -f pdflatex. **Rule:** either serialize builds or use truly isolated worktrees with their own build directories. Never run pkill -9 -f pdflatex if another agent may be building.

**AAP16 — git stash is destructive.** Never use git stash (or stash pop) in this codebase. Multiple agents have lost work to failed stash pops. The PERMANENT "no destructive git" rule explicitly forbids stash. Found 2026-04-07 in agents a728d5ec and a1b6a0ee. **Rule:** git stash is FORBIDDEN. Use git diff > patch.diff + git apply instead. Or use worktrees.

**AAP17 — Truncated agent final reports.** Agents can produce reports that end mid-sentence (token limit). The actual edits are often more extensive than the reports indicate. **Rule:** ALWAYS verify edits via git diff, not just the agent's narrative. The diff is the ground truth; the report is a possibly-incomplete summary.

**AAP18 — Confabulating operadic theory rather than computing or reading.** When asked about operadic structures (Koszul dual cooperads, mixed sectors, bar functors), the temptation is to pattern-match from component operads rather than explicitly compute. This produces wrong answers. **Rule:** always verify via direct computation OR direct citation (Loday-Vallette, Vallette, Livernet, Willwacher). NEVER reason about operadic dimensions by analogy. Compute or cite.

### Rectification Dynamics (Active)

This repository is in a sustained correction-and-rectification phase. Assume all three volumes still contain many undiscovered errors. At even a 2% error rate across ~3,463 tagged claims: ~69 errors. At 5%: ~173. The job is falsification.

**Upstream-first ordering.** Verify claims in dependency-DAG order. The DAG has 1,297 theorem nodes and 1,669 edges. 522 root nodes have zero upstream dependencies — these are safe to verify in any order and should be verified first. Then Layer 1 (direct dependents of roots), then Layer 2, etc. Critical bottleneck: `thm:mc2:bar:intrinsic` (37 downstream citations). Most complex cone: Thm C (25 upstream deps).

**Verification windows (upstream-first):**
1. **Roots** (522 nodes): definitions, basic lemmas, frame examples — no upstream deps
2. **Thm A** (adjunction) — root theorem, no upstream deps, verify first among main theorems
3. **Thm B** (inversion, 11 upstream) — depends on genus-graded convergence, Barr-Beck-Lurie, log convergence
4. **Thm C** (complementarity, 25 upstream) — depends on anomaly duality, concrete modular datum
5. **Thm D** (modular characteristic, 13 upstream) — depends on generating function, closed forms
6. **MC2 bar-intrinsic** (37 downstream) — the single biggest bottleneck; verify after Thms A–D
7. **MC4 completion** (15 upstream) — depends on resonance-filtered bar-cobar
8. **MC5 sewing** (14 downstream) — depends on general HS-sewing
9. **All remaining claims** in topological order through the DAG

**The correction loop.** For each suspected error:
1. **Locate**: exact file, line, ±100 lines of context
2. **Classify**: A (logical/circular), B (formula), C (structural/label), D (status), E (editorial)
3. **Verify the diagnosis**: confirm this is wrong, not a convention difference or your misunderstanding
4. **Compute the correction** independently — not by pattern, not by majority vote
5. **Grep all variants** across both volumes: `~/chiral-bar-cobar` and `~/chiral-bar-cobar-vol2`
6. **Apply** with minimal blast radius
7. **Build + test**: `make fast` and `make test` must pass
8. **Propagate** to all instances found in step 5
9. **Document**: what was found, what class, what was corrected

**The double-edged Beilinson.** The principle applies to your corrections too:
> **"Am I certain this correction is right, or am I merely confident?"**
Certainty requires independent verification. If you cannot independently verify a correction, mark it `% RECTIFICATION-FLAG: [reason]` rather than silently applying. A wrong correction is worse than no correction.

## Deep Beilinson Audit — Procedure

When instructed to "perform a deep Beilinson audit," execute the following protocol on every page of the manuscript, proceeding linearly from page 1. Deployable on Vol I, Vol II, or both at will.

### Core Principle

**"What holds back forward progress is not the lack of genius but the inability to dismiss false ideas."** Every claim is false until independently verified. The audit's purpose is FALSIFICATION, not confirmation.

### Per-Page Protocol

For each page of the PDF:

1. **Read the page** via PDF extraction. Simultaneously read the corresponding .tex source to catch PDF-vs-source discrepancies.
2. **Enumerate every mathematical claim** on the page: formulas, theorem statements, proof steps, definitions, examples, table entries, sign conventions, scope qualifications.
3. **For each claim, independently verify:**
   - **Formulas**: Recompute from first principles. Do NOT pattern-match against other occurrences — compute independently (AP1, AP3).
   - **Proof steps**: Check logical validity. Does the hypothesis of each cited result match how it's used? Are there unstated assumptions? (AP4, AP7)
   - **Conventions**: Verify sign/shift conventions (s vs s⁻¹, cohomological vs homological, ℏ normalization) against the signs appendix (appendices/signs_and_shifts.tex) which is AUTHORITATIVE.
   - **Scope**: Check universal claims against known counterexamples. "For all" means ALL — verify edge cases (critical level, admissible, self-dual points). (AP7)
   - **Cross-references**: Verify cited theorem numbers resolve. Read the cited result to confirm hypotheses match.
   - **Status tags**: For any claim tagged ProvedHere, verify the proof actually proves the stated claim, not something weaker.
4. **Cross-check against the compute layer**: For any numerical formula (κ values, F_g, Q^contact, discriminants, growth rates), verify against compute/tests/ and compute/lib/. Run targeted tests if needed.
5. **Cross-check against the literature**: For standard results (Arnold relations, Faber-Pandharipande, Koszul duality Com^!=Lie, Feigin-Frenkel involution), verify the manuscript's statement matches the published version.
6. **Propagation check (AP5)**: After finding ANY error, immediately grep the entire codebase (both volumes, all .tex files, CLAUDE.md, memory files) for ALL other occurrences of the same formula/claim. Fix all instances in the same pass.
7. **Record findings**: Update `compute/audit/linear_read_notes.md` with:
   - Finding number, page, severity (CRITICAL/SERIOUS/MODERATE/MINOR)
   - Exact claim, exact issue, exact fix
   - Status (FIXED/OPEN/RETRACTED)
8. **Fix immediately**: Apply fixes to source files as they are found. Build after each fix to verify compilation. Do not accumulate unfixed findings.

### The Six Hostile Examiners

Deploy the following adversarial perspectives on formula-dense or conceptually novel pages:

- **Beilinson** (falsification-first): Is every "proved" claim actually proved? Are there circular dependencies? Is the scope honest?
- **Witten** (mathematical physics): Does the mathematics reproduce known physics? Are physical claims rigorous or heuristic? Are they correctly qualified?
- **Costello** (factorization algebras): Is the categorical framework correct? Are Ran space constructions well-defined? Is "factorization coalgebra" used correctly?
- **Gaiotto** (vertex algebras/W-algebras): Are κ formulas correct? Are Koszul duals correctly identified? Do shadow obstruction tower computations match the VOA literature?
- **Drinfeld** (Yangians/quantum groups): Are Yangian structures correctly defined? Is the DK bridge correctly stated? Are prefundamental modules correctly characterized?
- **Kontsevich** (operads/formality): Is the operadic framework correct? Are formality claims properly proved? Is the L∞ structure correctly defined? Is terminology precise?

### Known Error Patterns (from audit history)

The manuscript has specific recurring failure modes. Watch for:

- **AP1**: κ(W_N) formula copied incorrectly between sections (7+ correction commits historically)
- **AP3**: Pattern-completing a formula from adjacent families without recomputing
- **AP5**: Fixing a formula in one location but not propagating to all other occurrences
- **AP8**: Writing "self-dual" for Virasoro without specifying which duality and which c
- **AP9**: Confusing κ (modular characteristic) with c (central charge) or with κ_c (Hessian eigenvalue)
- **Shift confusion**: s vs s⁻¹ in bar (desuspension) and cobar (also desuspension in this manuscript's convention per signs appendix line 1316)
- **Bernoulli signs**: Â(x) has alternating signs, Â(ix) = (x/2)/sin(x/2) has all positive coefficients. F_g values are POSITIVE.
- **Heisenberg non-self-duality**: H_k^! = Sym^ch(V*) ≠ H_{-k}. This is a critical pitfall.

### Pace and Depth

- **Pages with no math** (TOC, blank, part titles): Note structural consistency, move on immediately.
- **Expository pages** (preface, introduction): Full verification of every formula. Error rate ~1 per 2-3 pages historically.
- **Formal proof pages** (body chapters 3-11): Verify theorem statements, check proof logic, verify key sign computations. Error rate ~0 historically but verify anyway.
- **Formula tables**: Verify EVERY entry independently. Tables are the #1 error source (copied formulas).

### Build Discipline

- After every fix: rebuild (`make fast` or `pdflatex`). Verify 0 undefined references.
- After every 10 pages: run compute tests (`python3 -m pytest compute/tests/ -x --tb=short -q`).
- Never accumulate more than 3 unfixed findings before building.

### Completion Criteria

The audit is complete when:
- Every page of the target volume(s) has been read and verified
- Every finding has been fixed, retracted, or documented as OPEN with justification
- The build is clean (0 undefined references, 0 undefined citations)
- All compute tests pass (22,000+)
- The findings register is complete with running totals

## Beilinson Rectification Loop — Chapter-Level Protocol

When instructed to "run the Beilinson loop on [TARGET]" (where TARGET is a chapter .tex path), execute the following **convergent iterative loop**. The loop has three stages per iteration and repeats until convergence (Stage 3 audit returns zero actionable findings). This protocol uses Claude Code's tool primitives directly: parallel Agent dispatch, background execution, worktree isolation, and TaskCreate/TaskUpdate for persistent state.

**The loop may run for hours. That is expected and correct.** Each iteration tightens the chapter. Convergence is the only exit condition.

### Initialization: TASK SETUP

Use TaskCreate to register the chapter as a tracked unit of work:
```
TaskCreate(description="Beilinson loop: [TARGET]", status="in_progress")
```

Record iteration count N=0.

---

### ITERATION N (repeat until convergence)

Increment N. Update task: `TaskUpdate(note="Iteration N starting")`

---

### Stage 1: DEEP BEILINSON AUDIT (read-only, adversarial, parallel, falsification-maximizing)

The goal is **maximal falsification from first principles**. Every claim is false until independently verified. Deploy the Six Hostile Examiners (Beilinson, Witten, Costello, Gaiotto, Drinfeld, Kontsevich) on every formula-dense or conceptually novel passage.

Launch THREE Agent tool calls in a SINGLE message (parallel dispatch):

```
Agent(subagent_type="general-purpose", run_in_background=true,
  description="RED audit [chapter] iter N",
  prompt="DEEP FALSIFICATION AUDIT of [TARGET], iteration N.
  Read the ENTIRE file. For every mathematical claim — theorem statements,
  proof steps, formulas, definitions, examples, table entries, sign
  conventions, scope qualifiers — INDEPENDENTLY VERIFY from first principles:
  - Recompute every formula (AP1, AP3). Do NOT pattern-match.
  - Check every proof step for logical validity (AP4, AP7, AP13).
  - Verify sign/shift conventions against the signs appendix.
  - Check universal claims against ALL edge cases (AP7, AP18).
  - Verify every cross-reference resolves and hypotheses match.
  - Check status tags against what the proof actually proves (AP4, AP12).
  - Deploy the Six Hostile Examiners on dense passages.
  - Cross-check numerical formulas against compute/tests/ and compute/lib/.
  Output: numbered findings (line, severity, class, claim, issue, proposed fix).
  Be MAXIMALLY adversarial. A finding you miss now propagates forever.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="BLUE audit [chapter] iter N",
  prompt="STALENESS + CONSISTENCY AUDIT of [TARGET], iteration N.
  Read TARGET + concordance.tex + CLAUDE.md + landscape_census.tex.
  - Flag every claim whose status changed (conjecture->theorem, restricted->general).
  - Flag every formula that differs from landscape_census.tex or the compute layer.
  - Flag duplicate subsection numbers, broken label references, AP12 violations.
  - Flag AP5 violations: formulas that appear in other files with different values.
  - Flag AP8/AP9 violations: ambiguous terminology, same-name-different-object.
  - Flag AP14 violations: Koszulness/formality conflation.
  - Flag AP15 violations: holomorphic/quasi-modular conflation.
  - Grep BOTH ~/chiral-bar-cobar AND ~/chiral-bar-cobar-vol2 for variant forms.
  Output: numbered findings with exact file:line locations across both volumes.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="GREEN audit [chapter] iter N",
  prompt="COMPLETENESS + FRONTIER AUDIT of [TARGET], iteration N.
  Read TARGET + git log -50 + concordance.tex + memory files.
  - Identify proved results that SHOULD appear in this chapter but are missing.
  - Identify structural gaps: missing definitions, unproved lemmas cited, dangling
    forward references, proof chains with unstated hypotheses.
  - Rank every gap by mathematical importance (load-bearing vs cosmetic).
  - For each gap, assess: can it be CLOSED with existing tools, or is it genuinely open?
  - Check against the full MC1-5 status, Koszulness programme, shadow obstruction tower status,
    three-pillar architecture, resonance completion theorem, entanglement programme,
    open/closed realization, shadow-formality all-arity.
  - Identify opportunities to STRENGTHEN: conjectures that are now theorems,
    conditional results whose conditions can be removed, scope restrictions that
    can be lifted.
  Output: numbered findings ranked by mathematical priority, with concrete proposals.")
```

All three run in background. When all three report back, merge findings into a single **FINDINGS REGISTER** with deduplication. Classify each: (A) logical/circular, (B) formula, (C) structural, (D) status, (E) editorial. Severity: CRITICAL > SERIOUS > MODERATE > MINOR. This register is the input to Stage 2.

Update task: `TaskUpdate(note="Iteration N Stage 1 complete: F findings (C critical, S serious, M moderate)")`

---

### Stage 2: ADVANCE (rewrite, rescaffold, close gaps, advance frontier)

**The north star**: Chriss-Ginzburg. The standard: Witten, Costello, Gaiotto, Kac, Etingof, Bezrukavnikov, Gelfand, Drinfeld, Kontsevich. Every object earns its place by solving a specific problem. Every paragraph forces the next. Scope is honest at every claim boundary. The mathematics is CORRECT, COMPLETE, and BEAUTIFUL.

This stage has two sub-phases executed sequentially:

#### Stage 2a: SURGICAL FIXES (build-gated)

For each finding from Stage 1 with severity >= MODERATE, in dependency order:

1. Read the exact location (±50 lines context)
2. Compute the correction independently — NOT by pattern (AP3)
3. Apply the minimal fix with Edit tool
4. Grep BOTH `~/chiral-bar-cobar` AND `~/chiral-bar-cobar-vol2` for all variant forms (AP5)
5. Fix all instances in the same pass

**Build gate**: After every 3 fixes, run `make fast`. Never accumulate > 3 unfixed findings before building. If a fix breaks the build, revert immediately.

Update task: `TaskUpdate(note="Iteration N Stage 2a: J/F findings fixed")`

#### Stage 2b: RECONSTITUTE + ADVANCE (architectural, isolated)

With all audit errors fixed, launch the reconstitution in a worktree for safety:

```
Agent(subagent_type="general-purpose", isolation="worktree",
  description="Reconstitute+advance [chapter] iter N",
  prompt="ARCHITECTURAL RECONSTITUTION AND FRONTIER ADVANCE of [TARGET],
  iteration N. All Stage 1 audit errors are fixed. Now the task is twofold:

  PART I — RECONSTITUTION. Assess against the Chriss-Ginzburg standard:
  (1) Does every object earn its place by solving a specific problem?
  (2) Does every paragraph force the next?
  (3) Is Theta_A the single organizing thread?
  (4) Is scope honest at every claim boundary?
  (5) Would Witten, Costello, Gaiotto, Beilinson, Kac, Etingof, Bezrukavnikov, Gelfand find this satisfactory?

  Propose and execute structural changes: reordering, merging, splitting,
  new material blocks, deleted redundancy, tightened prose. The standard is
  Witten, Costello, Gaiotto, and the elite Russian school — no hedging, no filler, no AI slop, every
  sentence carries mathematical weight.

  PART II — FRONTIER ADVANCE. From the GREEN audit's gap analysis:
  (1) Close every gap that can be closed with existing tools.
  (2) Prove every lemma that is cited but unproved, if the proof is within reach.
  (3) Upgrade conjectures to theorems where the proof now exists.
  (4) Remove unnecessary conditions from conditional results.
  (5) Add missing definitions, constructions, or examples that the chapter needs.
  (6) Write new compute tests for any new or modified mathematical claims.
  (7) Strengthen the narrative arc — every chapter should tell a single story
      with Theta_A as protagonist.

  Build after each edit. Report all changes made, gaps closed, and build status.
  If any edit breaks the build, revert that edit and continue.
  Run `make test` after all edits to verify no regressions.")
```

Review the worktree diff. Apply successful changes to main. Discard failed changes.

Update task: `TaskUpdate(note="Iteration N Stage 2b complete: G gaps closed, R rewrites applied")`

---

### Stage 3: RE-AUDIT (adversarial verification of what was just written)

**Critical**: This is NOT a rubber stamp. This is a FRESH adversarial audit of everything written in Stage 2, with the same intensity as Stage 1. The purpose is to catch errors introduced by the rewrite — new formulas that are wrong, new proofs with gaps, new scope claims that are too broad, prose that hedges or bloats.

Launch THREE Agent tool calls in a SINGLE message (parallel dispatch):

```
Agent(subagent_type="general-purpose", run_in_background=true,
  description="RED re-audit [chapter] iter N",
  prompt="ADVERSARIAL RE-AUDIT of [TARGET], iteration N Stage 3.
  Stage 2 just rewrote and advanced this chapter. Your job: FALSIFY
  everything that was just written. Focus especially on:
  - NEW formulas: recompute each one from first principles (AP1, AP3, AP17).
  - NEW proofs: check every logical step. Are hypotheses satisfied? Is scope honest?
  - NEW definitions: are they well-formed? Do they conflict with existing ones?
  - UPGRADED claims: was the upgrade justified? Did the proof actually prove this?
  - REMOVED material: was anything load-bearing deleted?
  - AP17 cascade check: did the rewrite chain multiple unchecked claims?
  Read the FULL file. Output: numbered findings. If you find ZERO actionable
  findings, explicitly state 'CONVERGED: no actionable findings.'")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="BLUE re-audit [chapter] iter N",
  prompt="CONSISTENCY RE-AUDIT of [TARGET], iteration N Stage 3.
  Stage 2 just modified this chapter. Check:
  - Do all new/modified formulas match landscape_census.tex and compute/?
  - Do all new/modified cross-references resolve?
  - Are there new AP5 violations (formula changed here but not elsewhere)?
  - Are there new AP8/AP9/AP14/AP15 violations introduced by the rewrite?
  - Does the chapter still compile? Are there new undefined references?
  - Grep both volumes for any inconsistencies introduced.
  Output: numbered findings. State 'CONVERGED' if zero actionable findings.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="GREEN re-audit [chapter] iter N",
  prompt="QUALITY RE-AUDIT of [TARGET], iteration N Stage 3.
  Stage 2 just rewrote this chapter. Assess against the Chriss-Ginzburg +
  Witten/Costello/Gaiotto/Kac/Etingof/Bezrukavnikov/Gelfand standard:
  - Does the prose meet the standard? No AI slop, no hedging, no dashes where
    a colon or period suffices, no 'notably', 'crucially', 'remarkably'.
  - Does every object earn its place?
  - Are there still structural gaps that Stage 2 missed or introduced?
  - Is there redundancy that should be eliminated?
  - Would a hostile referee at Inventiones accept this chapter as-is?
  Output: numbered findings. State 'CONVERGED' if zero actionable findings.")
```

When all three report back, merge into a FINDINGS REGISTER.

**Convergence test**: If ALL THREE re-audit agents report CONVERGED (zero actionable findings at severity >= MODERATE), proceed to FINALIZE. Otherwise, the findings become the input to the NEXT iteration: return to Stage 1 with N+1, using the Stage 3 findings as the starting register (skip re-auditing claims already verified in this iteration; focus on new/modified material).

Update task: `TaskUpdate(note="Iteration N Stage 3: [CONVERGED | NOT CONVERGED, K new findings]")`

---

### FINALIZE (after convergence)

1. Build both volumes: `pkill -9 -f pdflatex; sleep 2; make fast` and `cd ~/chiral-bar-cobar-vol2 && make`
2. Run full tests: `make test`
3. Grep for any new AP1-AP18 violations introduced by this session
4. Update task: `TaskUpdate(status="completed", note="CONVERGED after N iterations. Npp, M undef refs, K tests passed, J total findings fixed, G gaps closed")`
5. If any theorem status changed, update concordance.tex
6. Report to user: iteration count, total findings fixed, gaps closed, frontier advances, final build status

### Loop State

The TaskCreate/TaskUpdate system persists across context compression and session boundaries. To see loop progress: `TaskList`. To resume after interruption: read the task list, find the latest iteration, and continue from the current stage.

**Chapter ordering** follows the upstream-first dependency DAG: foundations and definitions first, then the five main theorems in order (A, B, C, D, H), then examples, then connections, then appendices.

### Execution Rules (inherited from Beilinson Principle)

- Never edit without reading first
- Never write a formula without computing it
- Never change a correct formula to match a wrong narrative
- After every correction, grep BOTH volumes (AP5)
- The .tex source is ground truth; CLAUDE.md and memory describe beliefs
- A smaller true chapter beats a larger false one
- When agents disagree, trust computation > source > description
- A wrong correction is worse than no correction — mark uncertain fixes with `% RECTIFICATION-FLAG`
- **AP17 applies to your own rewrites**: after writing ANY new theorem in Stage 2, audit it in Stage 3 before building on it in the next iteration
- **The loop runs until convergence, not until fatigue.** If iteration 5 finds errors, iteration 6 runs. Hours-long execution is expected and correct.

## Five Main Theorems (all proved)

- **(A)** Bar-cobar adjunction + Verdier intertwining on Ran(X)
- **(B)** Bar-cobar inversion: Omega(B(A)) -> A quasi-iso on Koszul locus
- **(C)** Complementarity: Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)); upgraded to shifted-symplectic Lagrangian geometry
- **(D)** Modular characteristic: obs_g = kappa(A) * lambda_g for uniform-weight modular Koszul algebras at all genera; genus-1 universality obs_1 = kappa * lambda_1 PROVED unconditionally for all families. kappa(A) universal, additive, duality-constrained (kappa+kappa'=0 for KM/free fields; kappa+kappa'=rho*K for W-algebras), A-hat GF. The bar propagator d log E(z,w) is weight 1 (rem:propagator-weight-universality), so all edge-level Hodge data is standard. For multi-weight algebras at g>=2: the scalar formula FAILS — the free energy receives a cross-channel correction δF_g^cross from mixed-propagator graphs (op:multi-generator-universality, RESOLVED NEGATIVELY by thm:multi-weight-genus-expansion). The full decomposition is F_g(A) = κ(A)·λ_g^FP + δF_g^cross(A), where δF_2(W_3) = (c+204)/(16c) > 0 for all c > 0. The correction is R-matrix independent and vanishes iff the algebra is uniform-weight.
- **(H)** Hochschild: ChirHoch*(A) polynomial, Koszul-functorial

## Koszulness Characterization Programme

Major structural component. Two overlapping numbering schemes exist:

**Meta-theorem (thm:koszul-equivalences-meta in chiral_koszul_pairs.tex)**: items (i)-(xii). **10 unconditional equivalences + 1 conditional + 1 one-directional (D-module purity)**. Item (xii) = D-module purity (forward proved, converse open). Concordance section: sec:concordance-koszulness-programme.

**Preface K-numbering (K1-K12)**: a different list of 12 where K12 = bifunctor decomposition (proved). D-module purity is a 13th item outside this list.

**The meta-theorem items (authoritative, matching thm:koszul-equivalences-meta):**
- (i) Chirally Koszul (Definition ref:chiral-koszul-morphism) — unconditional
- (ii) PBW spectral sequence collapses at E₂ — unconditional
- (iii) A∞ formality of bar cohomology (m_n = 0 for n ≥ 3) — unconditional
- (iv) Ext diagonal vanishing — unconditional
- (v) Bar-cobar counit is quasi-iso — unconditional
- (vi) Barr-Beck-Lurie comparison is equivalence — unconditional
- (vii) FH concentrated in degree 0 for all g — unconditional
- (viii) ChirHoch* polynomial in degrees {0,1,2} — unconditional
- (ix) Kac-Shapovalov det nonzero in bar-relevant range — unconditional
- (x) FM boundary acyclicity (restriction to FM boundary strata acyclic) — unconditional
- (xi) Lagrangian criterion — **CONDITIONAL** on perfectness/nondegeneracy
- (xii) D-module purity — **ONE-DIRECTIONAL** ((x)⟹(xii) proved, converse open)

**Additional proved characterizations (outside meta-theorem):**
- Tropical Koszulness (thm:tropical-koszulness) — unconditional
- Bifunctor decomposition (thm:bifunctor-obstruction-decomposition) — one consequence of Koszulness (not an equivalence)
- Curve independence (prop:genus0-curve-independence) — proved
- PBW universality (prop:pbw-universality) — proved (sufficient condition)

## Three Concentric Rings (the architecture)

**Ring 1** — Proved core: Theorems A-H, **all five MC1-5 proved (MC3 all simple types)**, DK-0 through DK-3, MC3 thick generation (all simple types), MC4 strong completion towers (thm:completed-bar-cobar-strong, W_N rigidity, 21 conjectures resolved), MC5 all-genera sewing (thm:general-hs-sewing, thm:heisenberg-sewing), Koszulness 10 unconditional + 1 conditional + 1 one-directional (thm:koszul-equivalences-meta); D-module purity partially proved (13th characterization).
**Ring 2** — Nonlinear characteristic layer (the shadow obstruction tower), FULLY INTEGRATED across Parts I-III. The primary mathematical object is the filtered finite-order engine: Theta_A^{<=2} (kappa), Theta_A^{<=3} (cubic shadow), Theta_A^{<=4} (quartic shadow), ... with obstruction classes o_{r+1}(A) in the cyclic deformation complex. Proved at finite order: kappa for all families, cubic shadows, quartic resonance class with clutching law (via Mok's log FM degeneration). Q^contact_Vir = 10/[c(5c+22)]. Genus-1 Hessian correction delta_H^(1)_Vir = 120/[c^2(5c+22)]x^2. Shadow archetypes computed in every example chapter: Heisenberg=Gaussian/terminates@2, affine=Lie/tree/terminates@3, betagamma=contact/quartic/terminates@4, Virasoro/W_N=mixed (infinite tower, quintic forced). Shadow depth classification into four classes: G (Gaussian, r_max=2), L (Lie/tree, r_max=3), C (contact/quartic, r_max=4), M (mixed, r_max=infinity). Operadic complexity conjecture (conj:operadic-complexity): r_max(A) = A∞-depth = L∞-formality level. The shadow obstruction tower = L∞ formality obstruction tower identification is PROVED at all arities by induction on r (thm:shadow-formality-identification; the low-arity cases arities 2,3,4 were the base cases, prop:shadow-formality-low-arity). Ambient complementarity = shifted-symplectic Lagrangian geometry, CONDITIONAL on perfectness/nondegeneracy hypotheses. The full Theta_A (all arities, all genera) is PROVED by the bar-intrinsic construction (thm:mc2-bar-intrinsic): Theta_A := D_A - d_0 is MC because D_A^2 = 0. The shadow obstruction tower consists of its finite-order projections.
**Ring 3** — Physics-facing frontier: W-algebra axis (MC4 W_infty closed unconditionally), Yangian/RTT axis (**MC3 fully proved all types**, DK-5 accessible), holographic/celestial axis (anomaly-completed Koszul duality, M2 example in Vol II, holographic modular Koszul datum H(T) = (A, A!, C, r(z), Θ_A, ∇^hol) packaging the full HT holographic system into a single modular MC problem with five theorem targets). **MC4 splitting**: MC4⁺ (positive towers: W_{1+∞}, affine Yangians, RTT — SOLVED by weight stabilization, thm:stabilized-completion-positive) vs MC4⁰ (resonant towers: Virasoro, non-quadratic W_N — reduced to finite resonance problem by thm:resonance-filtered-bar-cobar). Resonance rank ρ(A) (def:resonance-rank) classifies completion difficulty. Resonance completion conjecture (conj:platonic-completion): every positive-energy chiral algebra has ρ < ∞. Vir_{26-c} reinterpreted as depth-zero resonance shadow. **Analytic completion programme** (raeeznotes90): sewing envelope A^sew (Hausdorff completion for sewing-amplitude seminorms), analytic bar coalgebra B^an(A) (graph-norm closure), analytic Koszul pairs, HS-sewing condition (Hilbert-Schmidt multiplication → trace-class amplitudes), coderived analytic shadows Q_g^an(A), shadow partition function. Platonic chain: A_alg ⊂ A^sew ⇝ F_A ∈ IndHilb ⇝ Q•^an(A). Four target theorems/conjectures: (A_an) Heisenberg sewing theorem (thm:heisenberg-sewing, PROVED: one-particle Bergman reduction, Fredholm determinant, thm:heisenberg-one-particle-sewing), (B_an) lattice sewing envelope (thm:lattice-sewing, PROVED), (C_an) analytic realization criterion (conj:analytic-realization, conjectural), (D_an) boundary bar duality (conj:boundary-bar-duality, conjectural). HS-sewing PROVED for entire standard landscape (thm:general-hs-sewing: polynomial OPE growth + subexponential sector growth ⟹ convergence). References: Moriwaki 2026 (conformally flat FH in IndHilb, Heisenberg/Bergman), Adamo-Moriwaki-Tanimoto 2024 (conformal OS for unitary full VOAs).

**Unifying principle**: The modular L∞ convolution algebra g^mod_A is the single organizing structure. It carries a natural modular L∞ structure (from the Feynman transform of the modular operad); the dg Lie algebra (def:modular-convolution-dg-lie) is its strict model. The shadow obstruction tower is the finite-order projection of the universal MC element Θ_A. The shadow obstruction tower — κ (arity 2), cubic shadow C (arity 3), quartic resonance class Q (arity 4) — consists of finite-order projections of the universal MC element Θ_A (thm:mc2-bar-intrinsic). Theorems A-D+H and the genus expansion are proved projections of the scalar level κ. The full MC element Θ_A ∈ MC(g^mod_A) satisfying D·Θ + ½[Θ,Θ] = 0 is PROVED: Θ_A := D_A - d_0 is MC because D_A² = 0 (thm:convolution-d-squared-zero). The weight filtration on g^mod controls the extension tower; each finite truncation Θ_A^{<=r} is constructive and does not require the full all-genera modular envelope.

## E₁/Ordered as Primitive: The Architectural Inversion (PERMANENT, 2026-04-08)

**Thesis.** The natural primitive of the manuscript is the E₁/ordered story, NOT the E_∞/symmetric story. The modular/symmetric layer is the av-image (Σ_n-coinvariant projection) of the ordered/E₁ layer. Information flows in only one direction: from the rich E₁ side (containing the R-matrix, the KZ associator, the full Yangian deformation, the braided/quantum-group categorical content) to the coarser modular side (containing only κ, the shadow obstruction tower, the genus expansion). The five main theorems A-D+H are the invariants that survive averaging.

**The averaging map and its kernel.** There is a Σ_n-coinvariant projection
```
av : g^{E₁}_A = Hom(B^ord(A), End_A)  ⟶  g^mod_A = Hom_{Σ_n}(B^Σ(A), End_A)
```
where B^ord(A) = T^c(s⁻¹Ā) is the ordered/tensor bar (deconcatenation coproduct, n+1 terms, coassociative not cocommutative) and B^Σ(A) = Sym^c(s⁻¹Ā) is the symmetric/factorization bar (coshuffle coproduct, 2^n terms, cocommutative AND coassociative). The map av is **injection of information** — it discards Σ_n-noninvariant components. Concretely:
- av(Θ^{E₁}_A) = Θ_A (the modular MC element of Theorem A)
- av(r(z)) = κ(A) at arity 2 (the modular characteristic of Theorem D)
- av(Φ_KZ) = C(A) at arity 3 (the cubic shadow)
- av(Yangian higher coproduct) = quartic resonance class Q at arity 4
- av extends to the full shadow obstruction tower as the arity-by-arity projection of the E₁ obstruction tower

**Why E₁ is the natural primitive — five reasons.**

1. **Operadic primacy (Stasheff).** The bar functor of any A∞-algebra is canonically the cofree tensor coalgebra T^c(s⁻¹Ā) with deconcatenation. This is what bar IS — Stasheff's theorem. The symmetric bar B^Σ is a *quotient* obtained by Σ_n-symmetrisation; the cocommutative coproduct on Sym^c is defined only for E_∞-algebras. The default operadic bar is ordered; the symmetric one is a specialisation.

2. **Information content.** The E₁ side is strictly richer at every arity. The R-matrix R(z), the KZ associator, the full Yangian/braided deformation — all live on the ordered side. The averaging map throws information away: κ = av(r(z)) is the leading scalar that survives; the higher Fourier modes of r(z) (and the full associator) are killed by Σ_n-coinvariance. To recover the rich content from the modular side requires re-introducing the ordered structure as auxiliary data.

3. **Physical primacy.** Every physical object the manuscript wants to model is naturally ordered: 3d HT theories live on ℂ × ℝ where the ℝ direction is *linearly ordered* (this is the open colour of SC^{ch,top}); line operators have a canonical ordering on the line; open string field theory uses T^c with deconcatenation (open strings have endpoints); integrable lattice models live on a *line* with sites θ₁ < ⋯ < θ_N; the Yangian coproduct Δ(T(u)) = T(u) ⊗̇ T(u) is non-cocommutative; Drinfeld-Kohno is fundamentally an E₁ statement; DK-0 through DK-5 / MC3 are about LINE-operator categories, not modular categories.

4. **Operadic architecture of SC^{ch,top}.** The Swiss-cheese operad has the E₁ open colour as primitive input data. The closed colour is an operadic *retract* (no-open-to-closed rule). The manuscript's own operad has the ordered side as the primary structural axis. The Koszul dual cooperad SC^{ch,top,!} has three sectors — closed (Lie cooperad, dim (n-1)!), open (Ass cooperad, dim m!), mixed (Lie ⊗ shuffles, dim (k-1)!·C(k+m,m)) — and the mixed sector encodes the inter-colour interaction that LIVES on the ordered side.

5. **Categorical primacy.** Quantum groups U_q(𝔤), Yangians Y(𝔤), braided tensor categories — all are E₁ objects. Modular tensor categories arise from them by Drinfeld centre / modular extension — a *derived* operation. Line operators are the natural categorical objects; modular tensor categories are their projections.

**The historical bias being corrected.** The manuscript developed from Beilinson-Drinfeld factorization algebras (unordered, on Ran(X)) → factorization homology (Costello-Gwilliam) → twisted holography (Costello-Gaiotto). That entire lineage works on the symmetric side. The modular convolution algebra g^mod_A and the central role of κ are inherited from this lineage. But for the *physical and operadic content* the manuscript actually proves, the natural framing is the inverse: g^{E₁} primary, g^mod = Σ_n-coinvariants, κ = av(r(z)) as the leading-order scalar shadow.

**What this commits us to.**
- Whenever discussing the bar complex without further qualification, the **default meaning is the ordered bar B^ord(A) = T^c(s⁻¹Ā)** with deconcatenation. The symmetric bar B^Σ(A) is invoked when the factorization-coalgebra/Theorem-A picture is specifically required.
- Whenever defining a convolution algebra or MC element, the **primitive object is g^{E₁}_A and Θ^{E₁}_A**. The modular versions g^mod_A and Θ_A appear as derived/averaged shadows.
- Whenever introducing κ, we say "κ(A) = av(r(z)) is the Σ_2-coinvariant of the r-matrix" — making the av map explicit at every occurrence.
- The shadow obstruction tower (κ, cubic shadow C, quartic resonance Q) is the **arity-by-arity av-projection** of the much richer E₁ obstruction tower (r-matrix, KZ associator, Yangian higher coherences).
- The five main theorems A-D+H are presented as **the invariants that survive averaging** — what's preserved when you Σ_n-quotient the rich ordered/braided structure.
- The Yangian, RTT, BAE, line-operator content is NOT auxiliary "physics-facing application" material — it is the *primary data* of which the modular shadows are projections.
- We DO NOT re-prove the existing five main theorems on the E₁ side. The architectural inversion is a *narrative* and *cross-reference* commitment, not a re-proof. The proofs of A-D+H stand on the symmetric side where they were proved; the inversion is an interpretation layer.

**Anti-pattern to avoid (AP-PRIM).** Do not write text that treats the E₁/ordered story as "an extension," "a refinement," "a physics application," "auxiliary," "frontier-facing," or "an alternative framework." It is THE primitive. The modular/symmetric story is the av-image. Reverse the framing direction at every opportunity.

**Connection to known anti-patterns.**
- AP35-AP47 (E_∞/E₁ confusions): the E₁ primacy thesis means the ordered side is primary data; E_∞ is a *property* (locality/Σ_n-equivariance) of certain examples, not a structural reduction.
- AP25/AP34/AP-OC (three functors): bar/cobar/Verdier classify twisting morphisms (couplings), Z^der_ch classifies bulk operators. The PRIMITIVE coupling-classification lives on the E₁ side via Θ^{E₁}; the modular coupling Θ_A is the av-image.
- AP-CHR: the chromatic-height-zero/algebraic content of the manuscript is precisely the av-image of the E₁ structure. Chromatic features only appear after spectralisation.

**Implementation status (2026-04-08 session).** Architectural elevation in progress: dedicated agents installing the E₁-as-primitive thesis in introduction.tex (W4-1), e1_modular_koszul.tex (planned), preface, and concordance. Cross-references being updated throughout. The proofs of A-D+H are NOT touched. See compute/audit/e1_primacy_architectural_elevation.md for the full intervention plan.

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
7. One-slot obstruction constrains MC3 (RNW19 Theorem 6.6)
8. F_n = o_n: secondary Borcherds operations = shadow obstruction tower obstruction classes (prop:borcherds-shadow-identification)
9. Quartic clutching law via Mok's degeneration formula [Mok25, Cor 5.3.4] (constr:arity4-degeneration)
10. Log clutching conjecture proved via [Mok25, Cor 5.3.4] (conj:log-clutching-degeneration → proved)
11. Ambient D²=0 proved via Mok's log FM normal-crossings [Mok25, Thm 3.3.1] (thm:ambient-d-squared-zero)

## The Chriss-Ginzburg Principle (the architecture)

Every algebraic structure in the monograph is a Maurer-Cartan element in a convolution dg Lie algebra. The key objects:

1. **Modular cyclic deformation complex** `Def_cyc^mod(A)` (def:modular-cyclic-deformation-complex in chiral_hochschild_koszul.tex): the ambient home. Differential from graph composition, bracket from stable-curve gluing.
2. **Stable-graph and planted-forest coefficient algebras** `G_st`, `G_pf` (def:stable-graph-coefficient-algebra, def:planted-forest-coefficient-algebra in higher_genus_modular_koszul.tex): the explicit combinatorial heart of g^amb_A.
3. **Shadow Postnikov obstruction tower** Θ_A^{<=r}: the proved finite-order truncations. Each level is a graph sum through arity r with obstruction class o_{r+1}(A) in the cyclic deformation complex.
4. **Bar complex as modular operad algebra** (thm:bar-modular-operad in bar_cobar_adjunction_curved.tex): {B^(g,n)(A)} is an algebra over FCom (Feynman transform of commutative modular operad). ∂²=0 at all genera is a formal consequence.
5. **Modular dg-shifted Yangian as pro-MC** (def:modular-yangian-pro in yangians_drinfeld_kohno.tex): Y_T^mod = pronilpotent completion of convolution dg Lie algebra. R_T^mod(z;ℏ) is an MC element.
6. **Shadow algebra** `A^sh` (def:shadow-algebra in higher_genus_modular_koszul.tex): H_•(Def_cyc^mod(A)) as graded commutative ring. Shadows (κ, Δ, C, Q, Sh_r) are graded projections at finite order. The all-arity master equation is the MC equation projected to arity r. The full tower convergence Θ_A = varprojlim Θ_A^{<=r} is PROVED (thm:recursive-existence).
7. **Koszulness characterization programme** (sec:concordance-koszulness-programme in concordance.tex, thm:koszul-equivalences-meta in chiral_koszul_pairs.tex): 12 equivalent characterizations of chiral Koszulness (K1-K12, **10 unconditionally proved equivalent + 1 conditional + 1 one-directional**; D-module purity = 13th, partially proved). K1-K12: PBW degeneration, A∞ formality, shadow-formality, E₂-formality, curve independence, PBW universality, Barr-Beck-Lurie, FH concentration, FM boundary acyclicity, tropical Koszulness, Lagrangian criterion (conditional on perfectness/nondegeneracy), bifunctor decomposition.

8. **Modular Koszul datum** Π_X(L) (constr:platonic-package in concordance.tex): six-fold datum (Fact_X(L), B̄_X(L), Θ_L, L_L, (V^br_L, T^br_L), R_4^mod(L)) from cyclically admissible Lie conformal algebra L (def:cyclically-admissible). Target: modular factorization envelope U^mod_X as left adjoint of primitive-current functor Prim^mod (conj:platonic-adjunction). Envelope + bar coalgebra + universal MC class = modular form datum. **UPGRADED** to eight-fold **completed modular Koszul datum** Π^oc_X(A) (def:thqg-completed-platonic-datum in thqg_open_closed_realization.tex): adds chiral derived center Z^der_ch(A) (universal bulk), annulus trace Tr_A ≃ HH_*(A) (first modular shadow of open sector), and nonlinear resonance tower R^oc_•(A) (quartic and higher obstructions in Z^2). **KEY DISTINCTION**: bar/cobar classifies TWISTING MORPHISMS (universal couplings between A and A!); the derived center classifies BULK OPERATORS acting on the boundary. The open/closed MC element Θ^oc = Θ_A + Σ μ^{M_j} packages both (constr:thqg-oc-mc-element).
9. **Cubic gauge triviality** (thm:cubic-gauge-triviality in higher_genus_modular_koszul.tex): If H^1(F^3g/F^4g, d_2) = 0, then cubic MC term is gauge-trivial and the quartic class [Θ'_4] ∈ H^2(F^4g/F^5g, d_2) is canonical. Abstract reason first nonlinear shadow is quartic.
10. **Independent sum factorization** (prop:independent-sum-factorization in higher_genus_modular_koszul.tex): For L = L₁ ⊕ L₂ with vanishing mixed OPE, all shadows separate: κ additive, T^br direct sum, Δ multiplicative, R_4^mod additive.
11. **Graphwise cocomposition** (const:vol1-graphwise-log-fm-cocomposition): Δ^log_Γ := (ν_Γ)_* ∘ Res_{D^log_Γ}, Γ-amplitude ℓ_Γ, Taylor coefficients ℓ_k^(g) = Σ_Γ |Aut(Γ)|^{-1} ℓ_Γ.
12. **Boundary operators as residue correspondences** (const:vol1-boundary-operators-residue): d_sew, d_pf, ℏΔ as residue/pushforward on log-FM strata. D²=0 = codimension-2 face cancellation.
13. **Depth filtration and tridegree** (def:vol1-rigid-planted-forest-depth-filtration): Tridegree (g,n,d) = (loop genus, arity, log boundary depth) from Mok's stratification.
14. **Genus spectral sequence** (const:vol1-genus-spectral-sequence): E_1 page isolates tree (p=0), one-loop (p=1), genus-2 shell (p=2) data. Differentials = obstruction maps Ob_g. DISTINCT from PBW spectral sequence.
15. **Modular tangent complex** (const:vol1-modular-tangent-complex): L∞ twisted differential d_{Θ_A}(x) = Σ (ℏ^g/n!) ℓ_{n+1}^(g)(Θ_A^⊗n, x); strict chart = d + [Θ_A, -]. Characteristic projections: κ, Δ_A, R^mod_4.
16. **Θ_A as universal twisting morphism** (cor:vol1-theta-log-fm-twisting-data): MC_•(Def∞^mod_log) ≃ Tw_α^mod.

17. **Shadow metric** `Q_L` (def:shadow-metric in higher_genus_modular_koszul.tex): quadratic form on each primary line L. The MC equation on L is equivalent to H² = t⁴Q (thm:riccati-algebraicity): shadow obstruction tower is algebraic of degree 2. Gaussian decomposition Q = (2κ+3αt)² + 2Δt². Critical discriminant Δ = 8κS₄ classifies shadow depth: Δ = 0 ⟺ tower terminates.
18. **Shadow connection** ∇^sh = d - Q'/(2Q) dt (thm:shadow-connection): logarithmic connection of Q_L. Residue 1/2 at zeros of Q. Monodromy = -1 (Koszul sign). Complementarity of discriminants: Δ(A) + Δ(A!) = 6960/[(5c+22)(152-5c)] (constant numerator). Self-dual at c=13.
19. **Propagator variance** δ_mix = Σf_i²/κ_i - (Σf_i)²/Σκ_i (thm:propagator-variance): multi-channel non-autonomy on the diagonal. Non-negative by Cauchy-Schwarz. Vanishes iff quartic gradient curvature-proportional (enhanced symmetry). Mixing polynomial P(W₃) = 25c²+100c-428. Computable from arity 2+4 alone.
20. **Arithmetic packet connection** ∇^arith_A (def:arithmetic-packet-connection in arithmetic_shadows.tex): flat meromorphic connection on the arithmetic packet module M_A = ⊕_χ M_χ over the spectral s-line. Singular divisor D_A = ∪_χ div(Λ_χ) is independent of nilpotent parts (thm:packet-connection-flatness). Arithmetic skeleton Ask(A) = M_A^ss controls divisor; algebraic defect Def_alg(A) = ⊕ N_χ M_χ contributes only unipotent monodromy. Principle: **arithmetic is semisimple; homotopy defect is unipotent**. Frontier defect form Ω_A = d log Λ_Eis - d log φ measures discrepancy between activated L-packets and automorphic scattering (def:frontier-defect-form). Gauge criterion (prop:gauge-criterion-scattering): Eisenstein block matches scattering connection iff Ω_A exact. Miura splitting for W_N (prop:miura-packet-splitting): Heisenberg core arithmetically inert; all obstructions in finite defect sector. Arithmetic comparison conjecture (conj:arithmetic-comparison): Θ_A canonically determines ∇^arith, higher-genus MC data accesses frontier defect residues.

21. **Shadow Eisenstein theorem** (thm:shadow-eisenstein in arithmetic_shadows.tex): The genus-1 amplitude Dirichlet series D_2(A,s) = −24κ · ζ(s) · ζ(s−1) is an Eisenstein L-function (PROVED, via σ_1 Dirichlet convolution applied to the Fourier coefficients of κ·E_2*(τ)). The shadow L-function L_A^sh(s) := Σ_{r≥2} S_r r^{-s} is a DIFFERENT object (extracts constant terms, not Fourier coefficients) and does NOT equal −κ·ζ(s)·ζ(s−1). All connections to Riemann zeta zeros are mediated through Eisenstein scattering. Intertwining kernel M[G_r](s) = r! Γ(s−1)/(2π)^{s−1} · ζ(s−1) · ζ(s+r−2), exact at r=2.
22. **Categorical zeta** (rem:categorical-zeta-riemann in arithmetic_shadows.tex): ζ^{DK}_{sl₂}(s) = ζ(s) − 1. The Riemann zeta function is the dimension-counting zeta of sl₂ irreps. For N ≥ 3: NOT multiplicative (no Euler product).
23. **D-module purity reduction** (rem:d-module-purity-content, prop:d-module-purity-km in chiral_koszul_pairs.tex): The converse direction (Koszulness ⟹ D-module purity) is reduced to PBW filtration = Saito weight filtration from MHM on FM_n(X). PROVED for affine KM via chiral localization + Hitchin. OPEN for Virasoro/W-algebras. Zero counterexamples.
24. **Universal instanton action** (prop:universal-instanton-action in higher_genus_modular_koszul.tex): A = (2π)² universal. Stokes constant S₁ = −4π²κi. MC equation constrains Stokes multipliers via Ecalle's bridge equation.
25. **c=13 full tower self-duality** (prop:c13-full-self-duality): At c=13, the ENTIRE shadow tower is self-dual (not just κ). RTF = 0 for all test functions.
26. **Admissible Koszulness for sl₂** (rem:admissible-koszul-status updated): L_k(sl₂) is chirally Koszul at ALL admissible levels. sl₃ and higher rank OPEN.
27. **Shadow negative results**: Shadow zeta NOT in Selberg class (S₃/S₄ fail). NOT multiplicative (no Euler product). Shadow and Riemann zeta generically independent (Dixmier trace). Subconvexity μ(1/2) = 0 for class M. Shadow Ferrero-Washington FAILS (μ ≠ 0 at p=2,5). KP tau: shadow is NOT a KP tau function.

The proved core descends from finite-order truncations of the shadow obstruction tower. The full equation **D_A Θ_A + ½[Θ_A, Θ_A] = 0** is PROVED at all levels: D²=0 at the convolution level is a THEOREM (from ∂²=0 on M̄_{g,n}), and at the ambient level D²=0 is also PROVED (thm:ambient-d-squared-zero, via Mok's log FM normal-crossings result). The all-arity inverse limit Θ_A = varprojlim Θ_A^{≤r} exists (thm:recursive-existence). Scalar saturation universality is proved for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape at all non-critical levels (for affine Kac-Moody, this includes admissible levels; for W-algebras, the UNIVERSAL algebra W^k(g) is Koszul at ALL levels by Feigin-Frenkel free generation; the SIMPLE QUOTIENT W_k(g) at admissible levels has Koszulness OPEN (bar-Ext vs ordinary-Ext gap)).

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I (~2,453pp)
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II (~1,478pp)
cd ~/calabi-yau-quantum-groups && make                            # Vol III (~206pp)
make test                                                         # Fast tests
make test-full                                                    # All tests
python3 scripts/generate_metadata.py                              # Census (authoritative)
```

**Build status** (2026-04-08): Vol I 2,453pp clean, Vol II 1,478pp clean, Vol III 206pp clean. Total 4,137pp, 0 undefined references. 118,823 test definitions across 1,315 test files and 1,255 compute engines. 3,463 tagged claims (2,898 ProvedHere = 83.7%).

**CAUTION**: Watcher spawns competing pdflatex; always kill before builds.

## Session Entry

1. Read this file — especially the Programme Summary, Beilinson Principle, and anti-patterns AP1–AP115
2. Build: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast`
3. Run tests: `make test`
4. `git log --oneline -10` for recent context
5. Identify which rectification tier/task to continue (upstream-first in the dependency DAG)
6. Read relevant .tex source before any edit — never write from memory or description
7. After each change: build + test. After each correction: grep ALL THREE volumes for all variants (AP5, AP112)
8. Never guess a formula — compute it or cite it. Check `landscape_census.tex` (AP1)
9. Apply the convergent writing loop to all prose: write → reimagine → rewrite → audit → converge
10. At session end: build all three volumes, run tests, summarize errors found by class

## Critical Pitfalls — MEMORIZE THESE

**Five objects that must never be conflated:**
- A: the algebra. B(A): the bar coalgebra. A^i = H*(B(A)): the dual coalgebra. A^! = (A^i)^v: the dual algebra.
- Omega(B(A)) = A (bar-cobar INVERSION, not duality). A^! is obtained by VERDIER/LINEAR duality, not cobar.
- Z^der_ch(A) = H*(C^•_ch(A,A), δ): the chiral derived center (UNIVERSAL BULK). This is NOT the bar complex. Bar/cobar = twisting morphisms (couplings). Derived center = bulk operators acting on boundary. The open/closed MC element Θ^oc = Θ_A + Σμ^M packages both (thm:thqg-swiss-cheese, thm:thqg-oc-mc-equation).

**Four-stage open/closed architecture** (par:concordance-four-stage-architecture in concordance.tex): (1) Local one-color theorem: A∞-chiral → braces → derived center = universal bulk (PROVED). (2) Open primitive: C_op is primitive, A_b = End(b) is a chart, Morita invariance (PROVED). (3) Globalization: tangential log curves (X,D,τ), bordered FM, local-global bridge (PROVED locally, modest globally). (4) Modularization: trace + clutching on open sector (annulus trace PROVED; full modular cooperad = PROGRAMME). Each stage depends on its predecessor. Never discuss stage k before establishing stage k-1.

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
**Shadow obstruction tower (the primary object)**: The shadow obstruction tower Θ_A^{<=r} consists of finite-order projections of the bar-intrinsic MC element Θ_A := D_A - d_0 (thm:mc2-bar-intrinsic). κ, C, Q are successive projections. The full Θ_A is PROVED by the bar-intrinsic construction. All-arity convergence Θ_A = varprojlim Θ_A^{<=r} is PROVED (thm:recursive-existence). Scalar saturation universality is PROVED for all algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the entire standard Lie-theoretic landscape. The residual conjecture is restricted to non-algebraic-family constructions (no known modular Koszul example with simple Lie symmetry).
**D²=0**: At the convolution level, D²=0 is a THEOREM (from ∂²=0 on M̄_{g,n}). At the ambient level (with planted-forest corrections), D²=0 is now PROVED (thm:ambient-d-squared-zero, via Mok's log FM normal-crossings, [Mok25, Thm 3.3.1]).
**Shadow depth vs Koszulness**: Shadow depth r_max does NOT characterize Koszulness. Both finite (Heis@2, aff@3, βγ@4) and infinite (Vir@∞) shadow depth algebras are Koszul. Shadow depth classifies COMPLEXITY of Koszul algebras (G/L/C/M classes), not Koszulness itself.
**Single-line dichotomy** (thm:single-line-dichotomy): On any 1D primary slice of Def_cyc^mod, the shadow metric Q_L(t) = (2κ + 3αt)² + 2Δt² with critical discriminant Δ = 8κS₄ forces r_max ∈ {2, 3, ∞}. The four-class partition G/L/C/M is structural: Δ = 0 ↔ perfect square Q_L ↔ finite tower (G or L); Δ ≠ 0 ↔ irreducible Q_L ↔ infinite tower (M). The contact class C (r_max = 4) escapes via STRATUM SEPARATION: the quartic contact invariant lives on a charged stratum whose self-bracket exits the complex by rank-one rigidity. Total depth d = 1 + d_arith + d_alg (thm:depth-decomposition). Algebraic depth d_alg ∈ {0, 1, 2, ∞}. Depths ≥ 5 are purely arithmetic (cusp forms).
**Universal vs simple quotient**: V_k(g) is Koszul for ALL k (prop:pbw-universality). L_k(g) may fail at admissible levels. The PBW criterion applies to the UNIVERSAL algebra; failure for simple quotients comes from vacuum null vectors.
**Three-pillar constraints**: (1) The convolution sL∞-algebra hom_α(C,A) is NOT a strict Lie algebra — it is shifted homotopy Lie with higher brackets ℓ_k (k≥3). The dg Lie is a strict MODEL only. (2) hom_α is functorial in either slot separately but FAILS as a bifunctor in both slots simultaneously (RNW19 §6). MC3 categorical lift must proceed one slot at a time. (3) Log FM compactification FM_n(X|D) ≠ classical FM; requires snc pair (X,D). Ordinary FM is the D=∅ special case.
**Non-principal W-duality**: DS reduction for arbitrary nilpotent f EXISTS (Kac-Roan-Wakimoto). The obstruction is NOT defining W_k(g,f); it is proving bar-cobar/Koszul COMMUTES with non-principal reduction. Hook-type in type A is PROVED corridor. Full arbitrary-nilpotent BV duality is CONJECTURAL. Proposition 21.19.29 in current global form COLLAPSES theorem/conjecture boundary — must be restricted to proved cases (principal, sl₃ subregular/minimal, hook-type).
**Factorization envelopes**: Nishinaka's construction starts from Lie conformal algebras, NOT arbitrary vertex algebras. The factorization envelope gives the ENVELOPING vertex algebra, not an arbitrary one. Vicedo's construction is the full/non-chiral analogue. Neither constructs the MODULAR completion — that is the frontier.
**Analytic vs algebraic**: The bare VOA/chiral algebra is a dense algebraic skeleton. The actual object for partition functions and sewing is the sewing envelope A^sew (Hausdorff completion). Curvature at genus g ≥ 1 forces coderived/contraderived categories, NOT ordinary derived categories. IndHilb-valued factorization homology (Moriwaki 2026) is 1-categorical, metric-dependent, conformally flat only — NOT yet the full analytic story.
**Planted-forest correction**: δ_pf^{(g,0)} is the d_pf component of D acting on Mok's rigid codimension-≥2 log-FM strata. Genus-2 formula EXACT: S_3(10S_3−κ)/48. Genus-3: 11-term polynomial in κ,S_3,S_4,S_5 (eq:delta-pf-genus3-explicit, genus-1+ vertex weights approximate). 35 planted-forest graphs among 42 total stable graphs of M̄_{3,0} (1 one-vertex, 9 two-vertex, 14 three-vertex, 11 four-vertex). Self-loop parity vanishing (prop:self-loop-vanishing): single-vertex (0,2k) with k self-loops has I=0 for ALL k≥2 (odd-dimensional parity obstruction). Shadow visibility genus: g_min(S_r) = floor(r/2)+1 (cor:shadow-visibility-genus). Pixton conjecture (conj:pixton-from-shadows): class-M algebras generate Pixton ideal via infinite MC tower — computationally supported at genus 2-3, formal ideal membership OPEN (requires strata algebra/admcycles). Compute module: pixton_shadow_bridge.py (82 tests).
**Heisenberg is the CG opening, NOT the atom (AP108/AP113)**: The Heisenberg is the simplest E∞ chiral algebra. Its R-matrix r^coll(z) = k/z is nontrivial but tier (b): derived from the local OPE, not independent input. The atom of the E₁ world is a genuinely nonlocal chiral algebra (tier (c): Yangian, EK quantum VA). The Heisenberg is the correct Chriss-Ginzburg opening (simplest nontrivial example whose deficiency forces the next construction), NOT the atom of the full theory. NEVER write "Heisenberg is the atom of the E₁ world."
**r^coll ≠ r(z) for the odd current algebra (AP107)**: The collision residue r^coll = Res^{coll}_{0,2}(Θ_A) and the classical r-matrix r(z) coincide for EVEN generators (parity of s⁻¹v = even) but DIFFER by a sign for ODD generators. For the odd current algebra (fermionic field with h=1/2), the bar desuspension introduces an extra sign. Verify case-by-case.
**Physics IS the homotopy type**: The homotopy type of a chiral algebra encodes its physics. The G/L/C/M classification is a classification of PHYSICS: G = free field (no BPS corrections), L = tree-level only, C = one-loop contact, M = all-order (maximally non-formal). This is not a metaphor. The SC^{ch,top} operations m_k^{SC} ARE the BPS corrections. Shadow depth = number of nonvanishing BPS orders.
**All standard chiral algebras are E∞**: Heisenberg, affine KM, Virasoro, W-algebras, lattice VOAs are ALL commutative as chiral algebras (factorization on UNORDERED Ran(X)). Non-abelian OPE (e.g., sl₂ structure constants) does NOT mean non-commutative in the operadic sense. E₁ = nonlocal OPE (ordering of points matters), NOT non-abelian OPE.

## The Symphonic Standard (PERMANENT)

**The monograph must move like the greatest symphony the world has ever known.** Every sentence carries mathematical weight. Every construction is inevitable. Every theorem earns its place by solving a problem the reader already feels. The standard is set by the combined qualities of the researchers channeled below. This applies to ALL writing in the programme: the manuscript proper, standalone papers, working notes, concordance, preface, introduction, appendices. No exceptions.

### The Voices and What They Demand

**Gelfand** (functorial inevitability): Every definition is a theorem in disguise. The right level of generality is not maximal but natural — the level where the proof works cleanly and could not work at any other level. Constructions have a "could not be otherwise" quality. Unnecessary hypotheses are absent. The reader feels that the mathematics discovered itself.

**Beilinson** (falsification and depth): No false ideas survive. The derived category is the natural habitat, not a technical convenience. Every claim is attacked before it is stated. Sparse, surgical prose — a Beilinson paper has no word that could be removed. The epistemic hierarchy is always visible: what is proved, what is conjectured, what is open.

**Drinfeld** (deformation-theoretic soul): Quantum groups emerge from geometry, not axioms. The R-matrix is a shadow of something deeper — the MC element in the convolution algebra. Every algebraic construction has a deformation-theoretic origin. The formal and the geometric are unified, never parallel.

**Kazhdan** (D-modules as language): The correct categorical framework is not decoration but substance. No shortcuts in geometric or representation-theoretic arguments. The Kazhdan-Lusztig programme is the template: geometry controls representation theory, not conversely.

**Etingof** (crystal clarity through computation): Every representation-theoretic fact earns its keep through explicit computation. Exposition is luminously clear — a graduate student can follow the argument on first reading. Abstraction serves computation, never the reverse.

**Nekrasov** (partition functions as algebra): Instanton counting computes invariants. The generating function IS the mathematical object, not a bookkeeping device. Physical partition functions and mathematical invariants are the same thing seen from different angles. No gap between "the physics" and "the mathematics."

**Polyakov** (the functional integral is real): Conformal bootstrap as a way of life. Path integrals yield theorems. The OPE is not an axiom but a consequence of locality. Physical reasoning is not heuristic motivation — it is the deepest layer of the argument.

**Kapranov** (higher categories as substance): Operads and higher categories are not decoration — they are the substance of the theory. The Swiss-cheese operad, the modular operad, the Fulton-MacPherson compactification have geometric content that drives the mathematics. Categorical structures solve problems; they are never invoked for their own sake.

**Ginzburg** (the Chriss-Ginzburg standard): Every object earns its place by solving a specific problem. Every paragraph forces the next. The symplectic resolution organizes everything. There is no dead weight. The architecture of the text mirrors the architecture of the mathematics. Redundancy is eliminated. The reader is carried forward by necessity.

**Costello** (factorization algebras as rigorous physics): Perturbative QFT is a theorem, not a programme. Factorization algebras make physics rigorous without killing its soul. The exposition tells the physical story first, then the mathematical framework, then the results. Every chapter opens with the problem it solves.

**Gaiotto** (dualities as computational tools): Dualities are not philosophy — they are tools for computing invariants. Every vertex algebra computation is simultaneously a physics prediction. The standard landscape is not an illustration of the theory but its testing ground. Worked examples are not optional; they are where the theory proves itself.

**Witten** (physical insight precedes proof): The deep structure is always geometric. Physical insight precedes and guides mathematical proof. The introduction states what is true and why it matters — in three pages, not thirty. No hedging, no equivocation. The reader knows from the first paragraph what the monograph proves and why it is important.

### Prose Laws (apply to ALL writing in the programme)

1. **No AI slop.** Zero tolerance for: "notably", "crucially", "remarkably", "it is worth noting", "interestingly", "this is particularly significant", "it turns out that", "one might wonder", "the key insight is." These are filler. Delete them.
2. **No hedging where the mathematics is clear.** If a theorem is proved, state it. If a conjecture is open, state it. "We believe that" and "it seems likely" are forbidden when the status is known.
3. **No em dashes for subordinate clauses.** Use colons, semicolons, or separate sentences. Em dashes are the hallmark of uncertain prose.
4. **No passive voice hedging.** "It can be shown that" → state the theorem. "The result follows from" → cite the result. "One expects that" → state the conjecture and its evidence.
5. **Every paragraph forces the next.** If a paragraph could be moved without the reader noticing, it does not belong. The text has momentum — reading it feels like being carried forward by mathematical necessity.
6. **State once, prove once, use everywhere.** No triple duplication. No restating theorems in different words. The definition appears once; every subsequent use is a cross-reference.
7. **The opening sentence of every chapter states the problem it solves.** Not "In this chapter we study..." but the actual mathematical problem, stated concretely.
8. **Comparison with prior work is surgical, not exhaustive.** One sentence per paper, stating what they prove and how we extend it. No multi-page comparison tables in the introduction.
9. **Scope is always explicit.** "For all" specifies the universe. "Proved" specifies the hypotheses. "Unconditional" means no hidden assumptions. The reader never has to guess the domain of a quantifier.
10. **The physical and mathematical are unified.** Physical motivation is not a separate section — it is woven into the mathematical development. The reader who knows physics sees their theory; the reader who knows mathematics sees rigorous proofs. Both see the same text.

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

**MC frontier** (all five MC1-5 proved; MC3 all simple types via multiplicity-free ℓ-weights):
- MC1: **PROVED** (PBW concentration, all standard families)
- MC2: **PROVED** (bar-intrinsic construction, thm:mc2-bar-intrinsic): Θ_A := D_A - d_0 is automatically MC because D_A² = 0. No restriction to simple Lie symmetry needed. Algebraic-family rigidity proves vanishing primitive tangent space / level-direction concentration for algebraic families with rational OPE coefficients (thm:algebraic-family-rigidity), covering the standard Lie-theoretic landscape at all non-critical levels; the stronger identity Θ = κ·η⊗Λ is proved on the uniform-weight lane and FAILS for multi-weight families (op:multi-generator-universality, RESOLVED NEGATIVELY by thm:multi-weight-genus-expansion; δF_2(W_3) = (c+204)/(16c) > 0). For affine Kac-Moody, this includes admissible levels of the UNIVERSAL algebra; for W-algebras, the UNIVERSAL algebra W^k(g) is Koszul at ALL levels by Feigin-Frenkel free generation, while the SIMPLE QUOTIENT W_k(g) at admissible levels has Koszulness OPEN for rank ≥ 2 (bar-Ext vs ordinary-Ext gap); for sl₂, L_k(sl₂) IS Koszul at all admissible levels (structural argument from single-weight null vector + Kac-Wakimoto character formula). Residual universality conjecture restricted to non-algebraic-family constructions.
- MC3: **PROVED FOR ALL SIMPLE TYPES** (thm:categorical-cg-all-types, cor:mc3-all-types): chromatic filtration + categorical prefundamental CG closure via multiplicity-free ℓ-weights (Chari-Moura) + Francis-Gaitsgory pro-nilpotent completion + DK on compacts. The type A proof (thm:mc3-type-a-resolution) was the original template; the all-types generalization replaces the minuscule hypothesis with the strictly weaker multiplicity-free ℓ-weight property. DK-5 now accessible for all simple types.
- MC4: **PROVED** — Strong completion-tower theorem (thm:completed-bar-cobar-strong): finite-stage bar-cobar passes to inverse limits automatically via strong filtration axiom μ_r(F^{i_1},...,F^{i_r}) ⊂ F^{i_1+...+i_r}, yielding arity cutoff (lem:arity-cutoff) that makes continuity + ML automatic. CompCl(F_ft) carries quasi-inverse bar-cobar homotopy equivalence (cor:completion-closure-equivalence), stable under MC twisting (thm:mc-twisting-closure), with completed twisting representability (thm:completed-twisting-representability). Coefficient-stability criterion (thm:coefficient-stability-criterion) reduces convergence to finite matrix stabilization. Uniform PBW bridge (thm:uniform-pbw-bridge) connects MC1→MC4. **MC4 SPLITTING**: MC4⁺ (positive towers: W_{1+∞}, affine Yangians, RTT — SOLVED by weight stabilization) vs MC4⁰ (resonant towers: Virasoro, non-quadratic W_N — reduced to finite resonance problem by thm:resonance-filtered-bar-cobar). W_N rigidity (thm:winfty-all-stages-rigidity-closure, 21 conjectures resolved). Remaining example-specific task: coefficient stabilization on finite windows + H-level target identification.
- MC5: **PROVED** (analytic sewing) — Inductive genus determination + 2D convergence (no UV renormalization needed) + analytic-algebraic comparison + general HS-sewing criterion (thm:general-hs-sewing: polynomial OPE growth + subexponential sector growth implies convergence at all genera). Heisenberg sewing theorem proved (thm:heisenberg-sewing, thm:heisenberg-one-particle-sewing: one-particle Bergman reduction, Fredholm determinant). Note: BV/BRST=bar at higher genus remains CONJECTURAL (conj:master-bv-brst).
- Theta_A: **PROVED** by bar-intrinsic construction (thm:mc2-bar-intrinsic): Θ_A := D_A - d_0 ∈ MC(Def_cyc(A) ⊗̂ G_mod). Shadow algebra A^sh = H_•(Def_cyc^mod). Named shadows (κ, Δ, C, Q) are projections of this single element (cor:shadow-extraction). All-arity master equation = MC equation projected to arity r. Q^contact_Vir = 10/[c(5c+22)]. Algebraic-family rigidity proves only the weaker line-concentration statement Θ_A^{min} = η⊗Γ_A for algebraic families; the stronger scalar package Θ_A^{min} = κ(A)·η⊗Λ is proved on the uniform-weight lane and FAILS for multi-weight families (op:multi-generator-universality, RESOLVED NEGATIVELY by thm:multi-weight-genus-expansion; δF_2(W_3) = (c+204)/(16c) > 0).
- Koszulness characterization programme: recorded in concordance.tex sec:concordance-koszulness-programme. 12 equivalent characterizations K1-K12 of chiral Koszulness (**10 unconditionally proved equivalent + 1 conditional + 1 one-directional**, thm:koszul-equivalences-meta in chiral_koszul_pairs.tex). 10 unconditional: PBW degeneration, A∞ formality, shadow-formality, E₂-formality, curve independence, PBW universality, Barr-Beck-Lurie, FH concentration, FM boundary acyclicity, tropical Koszulness. 1 conditional: Lagrangian criterion (K11, thm:lagrangian-koszulness, pending perfectness/nondegeneracy). 1 one-directional: D-module purity (meta-theorem item (xii), forward direction proved, converse open). The preface K-numbering lists K12 = bifunctor decomposition (a separate proved consequence). D-module purity is item (xii) of the meta-theorem, not the preface K12.

## Six Frontier Research Directions (raeeznotes85-91)

**Direction 1: Platonic Holographic Programme** (raeeznotes86). Every HT holographic system T should be controlled by a holographic modular Koszul datum H(T) = (A, A!, C, r(z), Θ_A, ∇^hol). Central claim: the dg-shifted Yangian r(z) is the binary genus-0 shadow of Θ_A, i.e. r(z) = Res^coll_{0,2}(Θ_A). Five theorem targets: boundary-defect realization, Yangian-shadow, sphere reconstruction (2026 GZ commuting differentials = scalar shadow of Sh_{0,n}(Θ_A)), quartic resonance obstruction, singular-fiber descent. Modular shadow connection ∇^hol_{g,n} = d − Sh_{g,n}(Θ_A). Deformation-quantization bridge Q_HT: classical coisson → quantum Koszul (Khan-Zeng 3d PVA sigma model).

**Direction 2: Analytic Sewing Programme** (raeeznotes89). The platonic ideal: formal OPE data ⊂ sewing envelope ⇝ Hilbert factorization theory ⇝ coderived shadow invariants. Sewing envelope A^sew = Hausdorff completion for all-amplitude seminorm topology. HS-sewing condition: Σ q^{a+b+c} ‖m^c_{a,b}‖²_HS < ∞ implies trace-class closed amplitudes. Analytic bar coalgebra. Analytic Koszul pair. Heisenberg sewing theorem PROVED (thm:heisenberg-sewing: one-particle Bergman reduction, Fredholm determinant). HS-sewing PROVED for entire standard landscape (thm:general-hs-sewing). Curvature forces coderived passage at genus g ≥ 1. IndHilb-valued conformally flat factorization homology (Moriwaki 2026).

**Direction 3: Factorization-Envelope Technology** (raeeznotes90/91). Pipeline: Lie conformal algebra → factorization envelope → factorization algebra → vertex algebra ≅ enveloping VA (Nishinaka 2025/26, generalizing KM + Virasoro; Vicedo 2025, full/non-chiral). Platonic target: universal modular factorization envelope U^mod_X(L) as left adjoint of modular primitive-current functor Prim_mod. Six-fold package Π_X(L) = (F_X, B̄_X, Θ_L, L_L, (V^br, T^br), R^mod_4). Envelope-shadow functor Θ^env_{≤r}(R). DS reduction as functor on modular Koszul datums: Θ_{W_N} = DS(Θ_{ĝ}).

**Direction 4: Non-Principal W-Algebra Duality** (raeeznotes88). Hook-type in type A is the first genuine proved non-principal corridor (Fehily, Creutzig-Linshaw-Nakatsuka-Sato, 2023-2025). Transport propagation lemma: hook-type seeds + edge-compatibility → transport-closure duality. Type-A transport-to-transpose conjecture: (W_k(sl_N, f_λ))! ≃ W_{k^∨_λ}(sl_N, f_{λ^t}). KEY CORRECTION: arbitrary DS reduction EXISTS (Kac-Roan-Wakimoto); what remains is proving bar-cobar/Koszul commutes with non-principal reduction.

**Direction 5: MC4 Completion Programme** (raeeznotes87). MC4 PROVED. MC4 splits into MC4⁺ (positive towers: solved by stabilization) and MC4⁰ (resonant towers: finite resonance). Resonance rank ρ(A) classifies completion difficulty. Resonance completion conjecture: every positive-energy chiral algebra has ρ < ∞. Virasoro: Vir_{26-c} = depth-zero resonance shadow, not final dual. MC5 analytic sewing PROVED (all-genera HS-sewing); BV/BRST=bar at higher genus CONJECTURAL (conj:master-bv-brst).

**Direction 6: Strategic Bottleneck** (raeeznotes85). All five MC1-5 proved. The MC3 extension to all simple types is now complete (cor:mc3-all-types). The completed inverse-limit bar/cobar problem for non-quadratic, infinite-generator chiral algebras is resolved by the strong completion-tower theorem (MC4). Non-principal W-duality and factorization-envelope technology are the active growth directions.

### Computation Frontier Conjectures (from the 2026-04-07/08 swarm)

These are the structurally new computation-level conjectures emerging from 217+ agents across ~118,823 tests:

1. **Virasoro denominator structure**: The bar GF denominator through arity 32 exhibits a systematic factorization pattern conjectured to extend to all arities.
2. **Rank-2 bar GF rationality**: For multi-generator algebras of rank 2, bar GFs are rational with denominators involving the golden ratio φ = (1+√5)/2 factor (verified for sl₂, conjectured universal for rank 2).
3. **MC equation = conformal bootstrap**: The shadow MC equation Σ F_g ℏ^{2g} = κ·(Â(iℏ) - 1) at the scalar level IS the conformal bootstrap at genus 0+1 (matching crossing symmetry = complementarity, unitarity = positivity of κ). At higher genus, the MC equation extends the bootstrap to the modular operad.
4. **Double resurgence**: The shadow obstruction tower has Gevrey-0 growth (convergent, instanton action A = (2π)²), and the Borel sum reproduces the shadow partition function exactly. The Stokes constant S₁ = -4π²κi is universal. The resurgence is "double" because both the genus expansion AND the arity expansion are independently resurgent.
5. **δF₂ universal N-formula**: For W_N algebras, the genus-2 cross-channel correction δF₂(W_N) has a universal closed-form polynomial in N (PROVED through N=8, conjectured universal).
6. **Pixton ideal from shadows**: Class-M algebras (infinite shadow tower) generate the Pixton ideal in the tautological ring R*(M̄_g) via the infinite MC tower. Computationally supported at genus 2-3, formal ideal membership OPEN.
7. **Shadow = matrix model at motivic level**: The shadow partition function Z_A^sh = exp(Σ F_g ℏ^{2g}) coincides with a κ-deformed matrix model partition function at the motivic Hall algebra level. Naive BCH pair-commutator is INSUFFICIENT (quantitative mismatch); full motivic DT theory required.
8. **Admissible sl₃ Koszulness**: L_k(sl₃) is expected to FAIL Koszulness at denominator q ≥ 3 (bar H² = rank = 8 > 3 = dim of expected Koszul dual generators). Computational verification at 15 admissible levels pending.
9. **All exceptional types class L**: G₂, F₄, E₆, E₇, E₈ affine algebras are conjectured to be uniformly class L (shadow depth 3). Verified for G₂ and E₆; others pending.
10. **DK-5 for sl₂**: The Drinfeld-Kohno DK-5 theorem (categorical equivalence at the homotopy level) should close for sl₂ via FRT construction from the explicit R-matrix.

## Vol II (~/chiral-bar-cobar-vol2)

**Title**: *A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT*
**Current**: ~1,478 pages, clean build, 0 undefined references.

Seven parts: I (The Open Primitive), II (The E₁ Reading), III (The Seven Faces of r(z)), IV (Modularity as Trace and Clutching), V (The Standard HT Landscape), VI (The Frontier), VII (Three-Dimensional Quantum Gravity — LAST, gravity is the most downstream application requiring the full E₁ + modular + complementarity machinery).

The bar complex's differential = C-direction factorization. Its coproduct = R-direction factorization. Together: Swiss-cheese algebra on FM_k(C) x Conf_k(R). At genus g >= 1: curved Swiss-cheese with curvature kappa * omega_g.

**Vol II status**: ALL foundational items PROVED. Recognition theorem PROVED (Weiss cosheaf descent, lem:product-weiss-descent). Homotopy-Koszulity of SC^{ch,top} PROVED (via Kontsevich formality + transfer from classical Swiss-cheese). PVA descent D2-D6 ALL PROVED: D2-D5 via repaired geometric proofs (exchange cylinder + three-face Stokes on FM_3(C)); D6 via H3(a) factorization + topological contractibility (no extra hypothesis beyond (H1)-(H4)). Operad⟹axioms (F4) PROVED. Axioms⟹operad (F5, rectification) PROVED via homotopy-Koszulity. Stokes⟹A∞ (FM1) PROVED. Zero conjectural algebraic inputs remain beyond the standing physical axioms (H1)-(H4) and standard published results (Kontsevich formality, GK94, BM03, CG17, AF15). Cross-volume bridges catalogued in concordance.

## Vol III (~/calabi-yau-quantum-groups)

**Title**: *CY Categories, Quantum Groups, and BPS Algebras*
**Current**: ~206 pages, clean build, 17,199 tests passed.

Five parts: I (CY-to-chiral functor, d=2 proved, d=3 conditional on chain-level S³-framing), II (BPS algebras and quantum groups: Dimofte integration, slab = bimodule NOT SC disk, Drinfeld double), III (Standard HT landscape at d=3), IV (Arithmetic shadows in dimension 3), V (The Frontier).

**Critical fix needed**: abstract currently missing entirely; kappa(K3 x E) = 3 vs 5 contradiction requires subscript notation (kappa_Heis = 3 from rank-3 Heisenberg, kappa_total = 5 including Virasoro).
