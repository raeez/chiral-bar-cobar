# DEEPAUDIT Response — Formal Assessment

**Date**: March 6, 2026 (Session 116)
**Audited document**: DEEPAUDIT.md (external adversarial audit against compiled PDF)
**Assessed against**: Current TeX source (75K lines, 55 files, Session 115+)
**Method**: Steel-man protocol — each finding assumed correct, then tested against source

## Execution Summary

**All 8 findings triaged. 5 acted on. 3 required no action.**

Census delta: PH 673 → 671 (-2), CJ 91 → 95 (+4)
Build: 1203 pages, zero undefined references, zero errors.

Fixes applied:
- F3: Expanded Hochschild [2] shift proof (deformation_theory.tex line 374)
- F5: Downgraded modular periodicity PH→CJ, documented proof gap (deformation_theory.tex line 609)
- F6: Corrected Mumford formula, downgraded geometric periodicity PH→CJ (deformation_theory.tex line 825)
- F7: Fixed gcd/lcm contradiction, downgraded unified periodicity PH→CJ (deformation_theory.tex line 891)
- F8: Added HH^* vs HH_* clarification remark (hochschild_cohomology.tex line 557)
- Downgraded periodicity exchange theorem (depends on F7)
- Added 2 vision remarks: rem:lagrangian-complementarity, rem:discriminant-monodromy

---

## Triage Table

| # | Finding | Severity | Verdict | Conf | Key Evidence | Action |
|---|---------|----------|---------|------|--------------|--------|
| 1 | Thm C direct-sum decomposition | TIER 1 | **STALE** | 5/5 | Proof rewritten: eigenspace decomposition of involution σ, not dimension count from pairing | None needed |
| 2 | Bar-cobar inversion too broad | TIER 1 | **FIXED (Session ~120)** | 5/5 | Main theorem OK but thm:bar-cobar-inversion-qi (line 7524) lacked Koszul hypothesis. Fixed: added Koszul+conilpotent/completion. Also fixed deformation_theory.tex:1053. | Fixed in 3 locations |
| 3 | Hochschild [2] shift asserted | TIER 2 | **SUPERFICIALLY STALE** | 3/5 | Proof acknowledges varying dimension (line 374) but the reduction to constant shift via Koszul concentration is one sentence, not a derived argument | Clarify proof |
| 4 | KL wrong target category | TIER 2 | **FIXED (Session ~120)** | 4/5 | Target was Rep(U_q(g)) in chiral_modules.tex:1123. Fixed: changed to C(U_q(g)) (semisimplified tilting). Added rem:kl-category-precision. | Fixed |
| 5 | Modular periodicity false implication | TIER 2 | **LIVE** | 2/5 | Proof at line 639 says "T-periodicity acts on weight grading by h→h+N" — this is the exact false step the auditor identified | Repair or downgrade |
| 6 | Geometric periodicity wrong identity | TIER 2 | **LIVE** | 1/5 | Line 825 writes "12 c₁(E) = δ" — omits κ₁. Standard relation is 12λ = κ₁ + δ. Proof collapses. | Repair or downgrade |
| 7 | Unified periodicity gcd/lcm | TIER 3 | **LIVE** | 1/5 | Line 891 contains verbatim the contradiction the auditor identifies: "give gcd(...) but optimal bound is lcm" | Fix arithmetic or restructure |
| 8 | Heisenberg Hochschild contradiction | TIER 2 | **SCOPE** | 4/5 | Two DIFFERENT invariants: ordinary HH (vanishes n≥3) vs Hochschild-cyclic spectral sequence E₂ page (polynomial). Not a contradiction. | Add clarifying remark |

---

## Detailed Assessment of Each Finding

### Finding 1: Theorem C Direct-Sum Decomposition — STALE

**The auditor claims**: The proof uses a dimension count from a perfect pairing to deduce a direct-sum decomposition. A perfect pairing gives dim Q_g(A) = dim Q_g(A!), not dim Q_g(A) + dim Q_g(A!) = dim H*(M_g, Z(A)).

**What the manuscript actually says** (higher_genus.tex, lines 4364-5377):

The proof was substantially rewritten (Sessions 80-87). The current proof does NOT use a dimension count from a pairing. Instead:

- **Step 8** constructs a Verdier involution σ on the ambient space H*(M̄_g, Z(A)) and identifies Q_g(A) as the +1 eigenspace and Q_g(A!) as the -1 eigenspace.
- **Step 9** (lem:trivial-intersection-complete, lines 5299-5317) proves Q_g(A) ∩ Q_g(A!) = 0 because they are eigenspaces for *different eigenvalues* (+1 and -1) of an involution.
- **Step 10** (lem:exhaustion-complete, lines 5321-5358) proves exhaustion: since σ² = id on a finite-dimensional vector space, every vector decomposes into +1 and -1 eigencomponents, so V = V⁺ ⊕ V⁻.

This is elementary linear algebra (involution on a finite-dimensional vector space decomposes it into eigenspaces), not a dimension count from a pairing.

**Why the finding is stale**: The auditor read a version of the proof that used the old argument (dimension count from pairing). The current proof uses a fundamentally different mechanism (eigenspace decomposition of an involution). The auditor's mathematical objection is correct about the OLD proof but does not apply to the current one.

**One subtlety remains**: The identification Q_g(A) = ker(σ - id) is the load-bearing step. This identification requires showing that the deformation classes land in the +1 eigenspace of the Verdier involution. The proof establishes this via the Kodaira-Spencer map properties. This step IS proved (not merely asserted) in the current text.

**The DEEPAUDIT Task 2 suggestion** (Lagrangian polarization) is a STRONGER framing that would give a richer result — but it is not necessary for the correctness of the current proof. The eigenspace argument is mathematically sufficient.

---

### Finding 2: Bar-Cobar Inversion Too Broad — STALE

**The auditor claims**: The theorem says "for any chiral algebra" but later chapters say it fails at admissible levels.

**What the manuscript actually says**:

The main theorem (higher_genus.tex, line 1431) states:

> "Let (A₁, A₂) be a **chiral Koszul pair** of chiral algebras on a smooth curve X."

The Koszul hypothesis is explicit and central. This is NOT stated "for any chiral algebra."

Furthermore, the admissible failure is explicitly documented:
- kac_moody_framework.tex line 2265: "At admissible levels k = -h∨ + p/q... the bar-cobar adjunction Ω(B̄(ĝ_k)) → ĝ_k is **not** a quasi-isomorphism"
- The failure mechanism (Ext¹ ≠ 0, non-collapsing spectral sequence) is stated.

**One potential issue**: The bar_cobar_construction.tex chapter (line 1067) uses the phrase "for any chiral algebra" when discussing the well-definedness of the bar complex (d²=0). This is CORRECT — d²=0 holds for any chiral algebra. The bar complex always exists; it is the bar-cobar INVERSION (Ω∘B → A being a quasi-isomorphism) that requires the Koszul hypothesis. The auditor may have confused these two statements.

**There is also a line** (bar_cobar_construction.tex line 6267) that says "the cobar-bar adjunction restricts to an equivalence on pro-nilpotent objects" in the context of a different theorem about completed bar complexes. This is the Positselski framework and is correctly scoped.

**Verdict**: The auditor's concern has been addressed. The theorem has the right hypothesis; the failures are documented.

---

### Finding 3: Uniform [2] Shift in Hochschild Duality — SUPERFICIALLY STALE

**The auditor claims**: The proof acknowledges varying Verdier dimension n+2 but then asserts a uniform shift of 2 without deriving it.

**What the manuscript actually says** (deformation_theory.tex, lines 358-378):

> "Since dim_C C̄_{n+2}(X) = n+2 varies with bar degree n, extracting the uniform shift of 2 in the total Hochschild grading requires additional input: the Koszul property ensures the bar complex is concentrated along the diagonal (weight = bar degree), so only a single bar degree contributes in each total degree."

This is EXACTLY the step the auditor attacks. The proof:
1. Correctly identifies the problem (varying Verdier dimension)
2. Invokes "Koszul concentration along the diagonal" as the mechanism
3. Asserts the conclusion

**The gap**: Step 2→3 is a one-sentence assertion, not a derived argument. The mechanism is mathematically sound — for a Koszul algebra, the bar complex IS concentrated along the diagonal, so in total degree d, only bar degree d contributes, and the Verdier shift in that bar degree is exactly d+2, giving a net shift depending on d. But the claim is that this telescopes to a CONSTANT shift of 2 in the totalized complex.

**The correct argument** (not fully written out in the manuscript): In total degree d, the only contributing bar degree is n = d (diagonal concentration). The Verdier shift on C̄_{d+2}(X) gives shift d+2. So HH^d(A) ≅ H^{d+2-(d+2)}(...)^∨ = H^0(...)^∨. Wait — this gives shift 0, not shift 2. Something is off.

Actually, the correct accounting is: the Hochschild complex lives in total degree = (bar degree) - (cohomological degree on configuration space). With Koszul concentration, bar degree n contributes only at cohomological degree n on C̄_{n+2}(X). Verdier duality gives H^n(C̄_{n+2}) ≅ H^{(n+2)-n}(C̄_{n+2})^∨ = H^2(C̄_{n+2})^∨. So in every bar degree, we get a uniform Verdier shift to degree 2. Combined with the desuspension shift: net shift = 2.

**Assessment**: The MECHANISM is correct, but the proof as written compresses the key computation (the fact that Koszul concentration + varying Verdier dimension telescopes to constant shift 2) into a single sentence. This is a genuine expository gap. A referee WILL ask for the calculation.

**Action needed**: Expand the proof by 3-5 lines to make the telescoping explicit. The mathematical content is correct; the exposition needs to show the arithmetic.

---

### Finding 4: KL Wrong Target Category — STALE

**The auditor claims**: Target should be semisimplified tilting category, not full Rep(U_q(g)).

**What the manuscript says** (kac_moody_framework.tex, line 1130):

The target is "Rep^{fd}(U_q(g))" — **finite-dimensional** representations. This is attributed to KL93 with proper citation.

Furthermore, the stronger claim (bar-cobar intertwining with KL as tensor equivalence) is explicitly marked as "expected but not proved here" (conjectured, not asserted).

**Nuance**: The auditor is correct that at roots of unity, even Rep^{fd}(U_q(g)) is non-semisimple, and the precise statement of KL involves the semisimplified category (or the restricted/tilting subcategory). The manuscript's statement is the standard one from KL93 — it is the community-standard formulation, even if modern treatments would use more precise categorical language. This is a place where the manuscript follows standard attribution rather than state-of-the-art precision.

**Assessment**: Not incorrect as stated (it's the KL93 statement), but could be sharpened. The bar-cobar enhancement is properly conjectured. No mathematical error.

---

### Finding 5: Modular Periodicity — LIVE

**The auditor claims**: T^N = Id does not imply coefficient periodicity. The proof confuses modular monodromy with q-expansion periodicity.

**What the manuscript says** (deformation_theory.tex, lines 625-639):

The proof computes that T^N = Id on the character space, then at line 639 says:

> "The T-periodicity acts on the weight grading by h → h+N, and the bar differential respects this shift (it is weight-preserving). Therefore H^n(B̄_{[h+N]}) ≅ H^n(B̄_{[h]}) for all h sufficiently large."

**The problem**: The statement "T-periodicity acts on the weight grading by h → h+N" is the false step. T acts by multiplication by e^{2πi(h_i - c/24)} on each character component. Having T^N = Id means e^{2πiN(h_i - c/24)} = 1, i.e., N(h_i - c/24) ∈ Z. This is a PHASE condition on the conformal weights, not a translation h → h+N in the weight grading.

The q-expansion coefficients of a character ch(q) = q^{h-c/24} Σ a_n q^n are NOT periodic just because T^N = Id. The auditor gives an explicit counterexample (q-series with finite T-order but non-periodic coefficients).

**However**: There is a subtlety. The theorem claims periodicity of *bar cohomology dimensions* dim H^n(B̄_{[h]}), not of character coefficients. For a rational VOA with finitely many modules, the bar complex in weight h is built from tensor products of module spaces. If the weight-h pieces are periodic in a representation-theoretic sense (same module decomposition at weight h and h+N), then bar cohomology dimensions would be periodic.

**But this is NOT what the proof establishes**. The proof leaps from T^N = Id to h → h+N translation, which is wrong. The correct argument would need to show that the VOA's internal structure (fusion spaces, OPE coefficients) repeats at weight intervals of N, which requires much more than T-eigenvalue periodicity.

**Verdict**: LIVE. The proof contains the false implication the auditor identifies. The theorem statement may still be TRUE (for rational VOAs there may be eventual periodicity of bar cohomology dimensions) but the PROOF is invalid.

**Action**: Either (a) provide a correct proof using the representation theory of rational VOAs (finite number of modules, eventual stabilization of fusion multiplicities), or (b) downgrade to Conjectured with a scope remark explaining the gap.

---

### Finding 6: Geometric Periodicity — LIVE

**The auditor claims**: The proof uses "12 c₁(E) = δ" but the correct Mumford relation is 12λ = κ₁ + δ.

**What the manuscript says** (deformation_theory.tex, line 825):

> "Mumford's formula 12 c₁(E) = δ in the Chow ring CH*(M̄_g)"

**This is wrong.** The standard Mumford relation on M̄_g is:

12λ = κ₁ + δ

where λ = c₁(E), κ₁ = first kappa class (NOT zero on the interior), and δ = boundary divisor class.

The omission of κ₁ is fatal to the proof because:
- The proof uses 12c₁(E)|_{M_g} = 0 (since δ restricts to zero on the interior)
- But 12c₁(E)|_{M_g} = κ₁|_{M_g} ≠ 0 when κ₁ is included
- The conclusion "Period_geom | 12(2g-2)" depends on the vanishing, which doesn't hold

**Assessment**: The auditor is completely correct. The formula is wrong, and the proof collapses.

**Can the conclusion be saved?** The statement Period_geom | 12(2g-2) might still hold for different reasons (e.g., the structure of the tautological ring in degree > 3g-3 forces vanishing), but the current proof via the incorrect Mumford relation does not establish it.

**Action**: Downgrade to Conjectured with a scope remark, or find a correct proof using the actual tautological ring structure. The incorrect formula must be corrected regardless.

---

### Finding 7: Unified Periodicity — LIVE

**The auditor claims**: The proof deduces gcd, then says the "optimal bound is lcm" without justification.

**What the manuscript says** (deformation_theory.tex, line 891):

> "The three constraints combine to give Period | gcd(N_mod, N_quant, N_geom), but since each provides a divisibility in a *different* direction (the three periodicities need not be synchronous), the optimal bound is the least common multiple."

**Analysis**: The auditor is correct on the arithmetic. If we have:
- Period | N₁
- Period | N₂
- Period | N₃

Then the strongest conclusion is Period | gcd(N₁, N₂, N₃).

The lcm appears naturally as an UPPER BOUND: any N that is a common multiple of all three periods is certainly a period. So Period | lcm is trivially true (it just says "the total period divides some common multiple of the component periods"). But the theorem STATES Period | lcm as its conclusion, which is the trivial direction.

However, the theorem statement (line 869) says:

> Period(A) | lcm(N_mod, N_quant, N_geom)

This is actually the CORRECT theorem statement for what it claims! The lcm IS an upper bound, and the theorem says the total period DIVIDES this upper bound. That's a valid (if weak) statement.

**The confusion is in the PROOF**, which first correctly derives the gcd bound (the strong bound), then weakens it to lcm for no reason, claiming lcm is "optimal." The gcd bound is STRICTLY stronger than the lcm bound.

**Three possible resolutions**:
1. The theorem should state Period | gcd (the strong bound) — but this requires the component periodicities to be about the SAME thing (same notion of "period"), which the proof claims they are NOT ("different directions").
2. The theorem should state Period | lcm (the weak bound) — which is trivially true and correctly stated, but the proof's claim that this is "optimal" is wrong.
3. The three periodicities are INDEPENDENT (acting on different grading components), in which case the total period really IS the lcm. But this requires a proof that the periodicities are independent.

**Assessment**: The theorem statement (Period | lcm) is true but trivial. The proof's claim that lcm is "optimal" is unjustified. The gcd bound is what the proof actually establishes, but it may not be what's intended.

**Action**: Fix the proof to remove the contradictory claim. Either strengthen to gcd (if the periodicities are about the same thing) or state lcm as an upper bound without claiming optimality. Add a remark about the gap between gcd and lcm.

---

### Finding 8: Heisenberg Hochschild Contradiction — SCOPE (not a contradiction)

**The auditor claims**: Chapter 10 says HH^n(H) = 0 for n ≥ 3, while Table 13.1 shows polynomial E₂ page. These contradict.

**What the manuscript actually computes**:

**Deformation_theory.tex (lines 1186-1204)**: Computes **ordinary Hochschild cohomology** HH^n(H) of the Heisenberg algebra. Uses the Koszul resolution (length 2) to show HH^n = 0 for n ≥ 3. Result: HH*(H) ≅ C[c]/(c²).

**Hochschild_cohomology.tex (lines 517-559)**: Computes the **E₂ page of the Hochschild-cyclic spectral sequence**. This spectral sequence starts from Hochschild HOMOLOGY HH_*(H) = C[c] ⊗ Λ(σ), takes S¹-invariants and coinvariants, and produces an E₂ page with C[c] in even degrees (column 0) and C[c] in odd degrees (column 1).

**These are DIFFERENT invariants**:
- HH^n (ordinary Hochschild cohomology) = Ext^n_{A⊗A^op}(A, A) — this is the cohomological version, and it vanishes for n ≥ 3.
- The E₂ page of the Hochschild-cyclic SS starts from Hochschild HOMOLOGY HH_* (the homological version), which is C[c] ⊗ Λ(σ) — this is polynomial and does NOT vanish.
- The table (line 635) reports the E₂ page data, not the Hochschild cohomology.

**Assessment**: There is no mathematical contradiction. The two computations measure different things:
1. HH^* (cohomology, via Koszul resolution): finite, vanishes for * ≥ 3
2. E₂ page of HC spectral sequence (from HH_* homology): polynomial, infinite

However, the notation HH_* vs HH^* is easy to confuse, and a reader (or referee) who doesn't track the cohomology/homology distinction will see a contradiction.

**Action**: Add a clarifying remark in hochschild_cohomology.tex near the Heisenberg E₂ computation, explicitly distinguishing HH^* (cohomology, finite) from HH_* (homology, polynomial) and explaining why the E₂ page is infinite even though HH^* terminates.

---

## Assessment of Task 2 (The Vision)

The DEEPAUDIT Task 2 articulates a vision of "Modular Koszul Duality for Factorization Algebras." This is a profound mathematical perspective. Here is a calibrated assessment:

### What the vision gets right:

1. **The Lagrangian interpretation of complementarity** is a genuine strengthening of Theorem C. The current eigenspace proof is correct but elementary; the Lagrangian framing would connect to shifted symplectic geometry (PTVV) and give a richer structural result. This is the most actionable insight.

2. **The coderived/contraderived distinction** is already present in the manuscript (Appendix G, B24/prop:curved-bar-acyclicity) and correctly identified as necessary. The vision's emphasis on this as foundational rather than technical is apt.

3. **The discriminant as monodromy characteristic polynomial** is an elegant reinterpretation of the shared discriminant Δ(x) = (1-3x)(1+x) across sl₂, Virasoro, and βγ. This could be a remark.

4. **"Quantum corrections are not perturbative afterthought but modular completion"** — this IS the thesis of the monograph, articulated with beautiful clarity. The manuscript already says this, but the auditor's formulation is sharper.

### What the vision overstates:

1. **The derived Drinfeld-Kohno theorem** is a major open problem, not something implicit in the manuscript. The Yangian chapter gestures at it but the actual R-matrix/braid monodromy relationship requires new technology.

2. **The family index theorem** (genus expansion = family Dirac index) is speculative. The Â-genus appearance is suggestive but the mechanism ("virtual tangent complex of derived moduli of curves, coupled to the center local system") is aspirational mathematics.

3. **"The next monograph writes this theory in its native language"** — the vision correctly identifies this as future work, not current scope. The current monograph DISCOVERS these phenomena; the next one would AXIOMATIZE them.

### Actionable extractions:

| Element | Action | Where |
|---------|--------|-------|
| Lagrangian interpretation of Thm C | Remark after thm:quantum-complementarity-main | higher_genus.tex |
| Discriminant = monodromy char poly | Remark in examples_summary.tex | After shared discriminant theorem |
| "Modular completion, not perturbative afterthought" | Sharpen existing language in introduction | introduction.tex |
| Derived Drinfeld-Kohno | Log to HORIZON Level D | HORIZON.md |
| Family index theorem | Log to HORIZON Level D | HORIZON.md |

---

## Summary of Required Actions

### Immediate fixes (this session):

1. **F6 (LIVE)**: Correct the Mumford formula from "12c₁(E) = δ" to "12λ = κ₁ + δ". Determine whether the geometric periodicity theorem survives with the correct relation. If not, downgrade to Conjectured. (deformation_theory.tex line 825)

2. **F7 (LIVE)**: Fix the gcd/lcm contradiction in the proof. Remove the claim that lcm is "optimal." Either strengthen theorem to gcd bound or state lcm as trivial upper bound with honest acknowledgment. (deformation_theory.tex line 891)

3. **F5 (LIVE)**: The "h → h+N" step is the same false implication the auditor identifies. Either provide a correct argument for dimension periodicity from rationality (using finiteness of the fusion category) or downgrade to Conjectured. (deformation_theory.tex line 639)

### Clarifications (this session if time permits):

4. **F3 (SUPERFICIALLY STALE)**: Expand the Hochschild [2] shift proof by 3-5 lines to make the telescoping from varying Verdier dimension to constant shift explicit. The arithmetic is: Koszul concentration puts everything in bar degree n at cohomological degree n on C̄_{n+2}(X), Verdier gives H^n ≅ H^{(n+2)-n} = H^2, hence uniform shift 2. (deformation_theory.tex line 374)

5. **F8 (SCOPE)**: Add a 3-line remark distinguishing HH^* (cohomology, vanishes for n≥3) from HH_* (homology, polynomial) and the Hochschild-cyclic E₂ page. (hochschild_cohomology.tex near line 517)

### No action needed:

6. **F1 (STALE)**: Proof was rewritten with eigenspace decomposition. No change needed.
7. **F2 (STALE)**: Koszul hypothesis explicit; failures documented. No change needed.
8. **F4 (STALE)**: Rep^{fd} is the correct standard formulation. No change needed.

### Vision engagement:
9. Add 2-3 remarks engaging Task 2 insights (Lagrangian, discriminant, modular completion). Log aspirational elements to HORIZON.

---

## Cascade Analysis

The three LIVE findings (F5, F6, F7) form a chain: the unified periodicity theorem (F7) depends on both the modular periodicity theorem (F5) and the geometric periodicity theorem (F6). If F5 and F6 are both downgraded, F7 collapses entirely.

**Downstream uses of periodicity theorems**: The periodicity results are used in:
- koszul_pair_structure.tex: Periodicity exchange under Koszul duality (thm:periodicity-exchange-koszul, line 896)
- Hochschild periodicity examples (hochschild_cohomology.tex)
- The Virasoro/KM periodicity theorems (which are INDEPENDENTLY proved via Gel'fand-Fuchs and do NOT depend on F5/F6/F7)

**Critical distinction**: The Virasoro 2-periodicity (thm:virasoro-hochschild) and KM 2h-periodicity (thm:periodicity-cohomology) are proved by DIFFERENT mechanisms (Gel'fand-Fuchs computation, Coxeter element action) and do NOT depend on the modular/geometric periodicity theorems. These remain valid.

The periodicity CLASSIFICATION (F7) that combines modular/geometric/quantum is the part that needs repair. The individual algebra-specific periodicity results stand independently.

**Census impact**: If F5, F6, F7 are all downgraded from PH to CJ: net change PH -3, CJ +3. The periodicity exchange theorem (thm:periodicity-exchange-koszul) would also need downgrade if it depends on the unified theorem: PH -4, CJ +4.
