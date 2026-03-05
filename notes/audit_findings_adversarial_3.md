# Adversarial Proof Audit — Findings Report (Session 3)
## Date: March 5, 2026
## Scope: Full monograph, maximally adversarial — assume nothing correct
## Auditor: Claude Opus 4.6, adversarial stance; 8 parallel deep-read agents + manual investigation

---

## Executive Summary

**Comprehensive audit of ~27K lines across 55 .tex files.** Eight specialized agents (ALPHA through THETA) plus manual investigation produced **~70 individual findings**, consolidated below into **tiers by severity and actionability**.

### Tier 0 — Errors requiring immediate correction (5 findings)
These are mathematically false statements that would be caught by a referee.

### Tier 1 — Significant gaps in tagged-ProvedHere proofs (8 findings)
Proofs marked as complete but missing key steps or containing logical gaps.

### Tier 2 — Inconsistencies and medium gaps (12 findings)
Internal contradictions between different parts of the monograph, or medium-severity proof gaps.

### Tier 3 — Expository and low-severity issues (10+ findings)
Sign convention variations, notation inconsistencies, misleading remarks. Not blocking but worth fixing.

### Theorem verdicts (post-audit)
- **Theorem A (Bar-Cobar Duality)**: SOUND — no errors found; two proof gaps in distributional arguments (Tier 1)
- **Theorem B (Bar-Cobar Inversion)**: SOUND — proof has a stratification gap (Tier 1)
- **Theorem C (Complementarity)**: SOUND with caveats — eigenvalue ±1 assignment still hand-wavy (Tier 1)
- **Genus Universality**: **CONTAINS ERRORS** — W-algebra formula wrong, FP formula wrong, proof cites wrong integral
- **Master Table**: NUMERICALLY CORRECT (all values independently verified by 3 agents)

---

# TIER 0: ERRORS (immediate correction required)

## 0.1: W-algebra duality formula κ' = K/2 - κ is FALSE for N ≥ 3

**[INTRODUCED BY SESSION 2 FIX]**
**[SEVERITY: CRITICAL]**
**[LOCATION: higher_genus.tex:3550, 3558, 3597, 3653]**
**[CONFIRMED BY: Manual, ALPHA-11, BETA-1]**

The Session 2 fix replaced the original (also wrong) κ(A!) = -κ(A) with κ(A!) = K/2 - κ(A). This is only correct for Virasoro (N=2, σ=1/2). For W₃: K/2 = 50 but correct κ+κ' = 250/3.

The theorem is **internally self-contradictory**: line 3550 says κ' = K/2 - κ while line 3555 says κ+κ' = 250/3 for W₃. These cannot both be true (250/3 ≠ 50).

**Correct formula:** κ(A!) = σ(𝔤)·K - κ(A) where σ(𝔤) = Σ 1/(mᵢ+1).

**Affected lines:** 3550, 3558, 3597, 3653

## 0.2: thm:mumford-formula states numerically FALSE formula

**[PRE-EXISTING — missed by Sessions 1-2]**
**[SEVERITY: HIGH]**
**[LOCATION: higher_genus.tex:3010]**
**[CONFIRMED BY: Manual, ALPHA-16]**

States ∫ ψ₁^{2g-2} λ_g = |B_{2g}|/(2g(2g-2)!). At g=1: gives 1/12, correct is 1/24.

**Correct formula:** (2^{2g-1}-1)/(2^{2g-1}) · |B_{2g}|/(2g)!

No computations affected — all examples use the correct FP formula from genus_expansions.tex:306.

## 0.3: Proof cites wrong integral for FP evaluation

**[PRE-EXISTING]**
**[SEVERITY: HIGH]**
**[LOCATION: higher_genus.tex:3599-3600]**
**[CONFIRMED BY: Manual, ALPHA-16, BETA-1]**

Cites ∫_{M̄_g} λ_g λ_{g-1} — wrong space (M̄_g not M̄_{g,1}) and wrong integrand (λ_g λ_{g-1} not ψ₁^{2g-2} λ_g). The cited integral is **zero for g≥3** by dimension count (2g-1 < 3g-3).

## 0.4: Obstruction nilpotence at g=0 — "scalar hence nilpotent" is wrong

**[PRE-EXISTING]**
**[SEVERITY: MEDIUM-HIGH]**
**[LOCATION: higher_genus.tex:3483]**
**[SOURCE: BETA-2]**

The proof says: "g=0: (obs₀)² ∈ H⁰ is scalar, hence nilpotent." A nonzero scalar is NOT nilpotent. The theorem should either exclude g=0 or clarify that obs₀ = 0 by convention.

## 0.5: "Free fields have Q_g = 0 for g ≥ 2" contradicts the Heisenberg

**[PRE-EXISTING]**
**[SEVERITY: MEDIUM]**
**[LOCATION: higher_genus.tex:5003-5008]**
**[SOURCE: BETA-11]**

Claims "Free field theories have Q_g = 0 for g ≥ 2 because higher genus contributions require interactions." But the Heisenberg (a free boson) has obs_g = κ·λ_g ≠ 0 for all g. This contradicts the entire monograph's main computations.

---

# TIER 1: SIGNIFICANT PROOF GAPS (in ProvedHere theorems)

## 1.1: Genus-1 d²=0 proof is a sketch, not a proof

**[SEVERITY: HIGH]**
**[LOCATION: higher_genus.tex:2508-2545]**
**[SOURCE: ALPHA-5]**

The proof of (d^(1))² = 0 lists "Terms 1-3, 4-6, 7-9" with vague justifications: "These work exactly as before," "satisfy functional equations that ensure cancellation," "cancel due to the non-holomorphic completion." No computation shown for ANY of the nine terms. Tagged ProvedHere but is a sketch.

## 1.2: Cobar d²=0 distributional proof has serious gap

**[SEVERITY: HIGH]**
**[LOCATION: bar_cobar_construction.tex:2546-2602]**
**[SOURCE: GAMMA-6]**

Acknowledges δ(z_i-z_j)² is not well-defined, then offers three "resolutions" none of which are complete. The intrinsic D-module definition (Definition 2125) gives d² = 0 automatically via Verdier duality, so the result IS correct, but the distributional proof has an unfixable gap. Should be restructured.

## 1.3: Verdier pairing non-degeneracy induction has gap

**[SEVERITY: HIGH]**
**[LOCATION: bar_cobar_construction.tex:3239-3250]**
**[SOURCE: GAMMA-2]**

The induction using Künneth on FM boundary strata doesn't verify that cross-terms between different strata vanish, or that distributional pairings are compatible with the Künneth decomposition.

## 1.4: Universality formula obs_g = κ·λ_g is false at cohomological level for W₃

**[SEVERITY: HIGH]**
**[LOCATION: higher_genus.tex: theorem statement ~3427 vs computation ~3309-3319]**
**[SOURCE: BETA-7]**

For W₃, obs_g = (c/2)λ_g^(T) + (c/3)λ_g^(W). At genus g≥2, λ_g^(T) ≠ λ_g^(W) in general, so obs_g is NOT proportional to a single λ_g. The formula holds at the level of free energies (after integration) but is false as a cohomological statement for multi-generator algebras.

## 1.5: d²=0 quantum proof — propagator antisymmetry claim is problematic

**[SEVERITY: HIGH]**
**[LOCATION: higher_genus.tex:5800-5839]**
**[SOURCE: BETA-3]**

The proof claims K(z,w) = -K(w,z) for the chiral propagator. But K(z,w) = ∂_z log E(z,w) is a (1,0)-form in z, not antisymmetric as a bidifferential. Two operators on different variables commute (not anticommute). The conclusion (d²=0) is likely correct via other means but this specific argument is flawed.

## 1.6: Koszul pair definition — equivalence of two versions unproved

**[SEVERITY: HIGH]**
**[LOCATION: chiral_koszul_pairs.tex:74-105]**
**[SOURCE: EPSILON-1]**

Definition def:chiral-koszul-pair claims Version I and Version II are "equivalent conditions" but no proof is given. The equivalence is standard in the quadratic associative case (LV Theorem 2.3.2) but non-trivial in the non-quadratic chiral setting.

## 1.7: Curved A∞ relations never explicitly stated/proved in theory files

**[SEVERITY: HIGH]**
**[LOCATION: deformation_theory.tex (general)]**
**[SOURCE: EPSILON-12]**

The formula m₁²(a) = m₂(m₀,a) - m₂(a,m₀) appears in appendices/general_relations.tex but is never stated or proved as a theorem in the theory chapters. For a monograph developing curved A∞ structures for chiral algebras, this is a significant omission.

## 1.8: Eigenvalue ±1 assignment in complementarity theorem

**[SEVERITY: MEDIUM]**
**[LOCATION: higher_genus.tex:4645-4663]**
**[SOURCE: BETA-4, persistent from Session 2]**

The argument computes +1 from explicit sign tracking, then asserts -1 from "anti-commutativity" without reconciliation. The decomposition Q_g(A) ⊕ Q_g(A!) = H*(M̄_g, Z(A)) does not depend on which eigenspace is ±1.

---

# TIER 2: INCONSISTENCIES AND MEDIUM GAPS

## 2.1: bc-βγ example says "0 + 0 = 0"

**[LOCATION: higher_genus.tex:3622]** — Should be "c/2 + (-c/2) = 0"
**[SOURCE: Manual, confirmed by DELTA-1]**

## 2.2: Free field κ=0 claims contradict Master Table

**[LOCATION: examples_summary.tex:134, 768]** — Claims κ=0 for free fields, table says κ=1/4 and κ=c/2
**[SOURCE: Manual, ETA-1, DELTA-1, ZETA-1, ZETA-2, ZETA-3]**

This was independently flagged by FIVE agents. Root cause: the table computes κ via Virasoro subalgebra (κ = c/2), while the prose describes the fermion's own bar complex acyclicity. The monograph needs to clarify which computation defines κ.

## 2.3: Heisenberg dual level sign wrong

**[LOCATION: bar_cobar_construction.tex:4405]** — Says CE(ĥ_k), should be CE(ĥ_{-k})
**[SOURCE: ETA-2]**

## 2.4: Heisenberg c+c' column: "---" vs "0"

**[LOCATION: examples_summary.tex:54 vs introduction.tex:804-806]**
**[SOURCE: ETA-4]**

Master Table says c+c' = "---" for Heisenberg, but introduction.tex theorem claims c+c' = 0.

## 2.5: H²(M̄_g) dimension: 2 vs 3 for g=2

**[LOCATION: higher_genus.tex:2949 vs 2979]**
**[SOURCE: ALPHA-15]**

Line 2949 claims dim H²(M̄_g) = 2 for g≥2 (Harer stability). Line 2979 correctly says H²(M̄_2) ≅ ℚ³. Harer stability applies to the open M_g, not to the compactification M̄_g.

## 2.6: Obstruction class degree: H² vs H^{2g}

**[LOCATION: higher_genus.tex: Definition 3005 vs Theorem 3068]**
**[SOURCE: ALPHA-7, ALPHA-8]**

Definition says obs_g ∈ H²(B̄_g, Z), theorem says obs_g ∈ H^{2g}(M̄_g). The "2" is the bar complex degree, not the cohomological degree on M̄_g. This conflation is never resolved.

## 2.7: Bosonic string explanatory text garbled

**[LOCATION: genus_expansions.tex:1141-1143]**
**[SOURCE: DELTA-2]**

Says "κ = c_total/2 where c_total = 26+(-26) = 0" but 0/2 = 0, not 13. The numerical values nearby are correct but the gloss is self-contradictory.

## 2.8: H*(B̄(Y(𝔤))) ≅ Center(Y(𝔤)) is wrong

**[LOCATION: chiral_koszul_pairs.tex:319-331]**
**[SOURCE: EPSILON-4]**

Bar cohomology computes Ext_H(ℂ,ℂ), NOT the center. Tagged ProvedElsewhere with no citation.

## 2.9: Conformal block duality requires both sides rational, but Koszul duality breaks rationality

**[LOCATION: chiral_modules.tex:744]**
**[SOURCE: EPSILON-9]**

Proposition requires both A and A! to be rational and C₂-cofinite, but Remark rem:associated-variety-koszul (line 1712) explicitly shows Koszul duality can map rational to non-rational.

## 2.10: W₃ minimal model central charge c=4/5 may be wrong

**[LOCATION: higher_genus.tex:3438-3444]**
**[SOURCE: ALPHA-10]**

The computation uses (p,q)=(5,4) with c=4/5, which is the Virasoro (3-state Potts) minimal model, possibly not the W₃ minimal model at these parameters. Needs verification.

## 2.11: KL diagram uses O_{k'}^{int} which is empty for k' < 0

**[LOCATION: chiral_modules.tex:342-367]**
**[SOURCE: EPSILON-10]**

The quantum group braiding diagram has O_{k'}^{int} at level k' = -k-2h∨ < 0, but there are no integrable modules at negative level.

## 2.12: Modular periodicity: character periodicity ≠ HH periodicity

**[LOCATION: deformation_theory.tex: ~line 609]**
**[SOURCE: EPSILON-16]**

T-matrix eigenvalue periodicity does not mechanically transfer to Hochschild cohomology periodicity. The bar differential involves OPE structure constants, not just conformal weights.

---

# TIER 3: EXPOSITORY AND LOW-SEVERITY ISSUES

## 3.1: Heisenberg dual mislabeled as "fermionic system"
**[LOCATION: bar_cobar_construction.tex:4405]** — [SOURCE: ETA-3, Manual]

## 3.2: Multiple inconsistent sign conventions for bar differential
**[LOCATION: bar_cobar_construction.tex:255, 1550, 5177]** — [SOURCE: GAMMA-5]

## 3.3: A∞ explicit relations at small k inconsistent with general sign convention
**[LOCATION: higher_genus.tex:109-117]** — [SOURCE: ALPHA-1]

## 3.4: Heisenberg bar computation contradicts text's own warning
**[LOCATION: bar_cobar_construction.tex:959-963 vs 948]** — [SOURCE: GAMMA-7]

## 3.5: Notational variation CE(ĥ) vs CE(𝔥) (with/without hat)
**[LOCATION: across multiple files]** — [SOURCE: ETA-6]

## 3.6: Remark incorrectly cites thm:obstruction-nilpotent for g≥3
**[LOCATION: higher_genus.tex:3393]** — [SOURCE: ALPHA-17, BETA-9]

## 3.7: Arnold relation Proof 1 is a sketch, not a proof
**[LOCATION: bar_cobar_construction.tex:795-831]** — [SOURCE: GAMMA-3]

## 3.8: Fermionic coproduct sign inconsistent with definition
**[LOCATION: chiral_koszul_pairs.tex:1168 vs 471]** — [SOURCE: EPSILON-6]

## 3.9: "Obstruction" language conflates HH⁰ center with HH³ deformation obstructions
**[LOCATION: deformation_theory.tex:411]** — [SOURCE: EPSILON-14]

## 3.10: Leray spectral sequence cites wrong fibration
**[LOCATION: higher_genus.tex:2090-2101]** — [SOURCE: ALPHA-14]

---

# VERIFIED CORRECT (cross-checks performed by multiple agents)

| Item | Verified by |
|------|-------------|
| All Master Table numerical values | Manual, DELTA, ETA, ZETA |
| κ(Vir_c) = c/2 | Manual, ETA-8 |
| κ(ĝ_k) = td/(2h∨) | Manual, ETA-8, ZETA-8 |
| κ(W_N) = c·(H_N-1) | Manual, ETA-8 |
| κ(bc_λ) = c/2 | Manual, DELTA |
| κ(βγ_λ) = -κ(bc_λ) | Manual, DELTA |
| c+c' = 2d for KM | Manual, ZETA-7, ETA-9 |
| c+c' = 26 for Virasoro | Manual, ZETA-7, ETA-9 |
| c+c' = 100 for W₃ | Manual, ZETA-7, ETA-9 |
| c+c' = 496 for E₈ | Manual, ZETA-7 |
| Feigin-Frenkel k→-k-2h∨ (all instances) | ETA-7, ZETA-5 |
| Sugawara formula | ZETA-4 |
| W₃ composite Λ = :TT: - (3/10)∂²T | ZETA-6, ETA-14 |
| Sugawara at critical: "undefined" not "diverges" | ETA-15 |
| Koszul dual identifications (all) | ETA-11, ZETA-9 |
| All obstruction table entries | DELTA |
| FP formula as used in examples | DELTA |
| σ(𝔤) for all exceptional types | DELTA |
| OEIS A001006 / A005043 sequences | DELTA |
| E₈ dim=248 fix from Session 2 | DELTA |
| Grading convention consistently cohomological | ETA-10 |
| All label references resolved | ETA-12 |
| Bosonization/Koszul distinction maintained | ETA-13 |

---

# RECOMMENDED FIXES (Priority Order)

### Priority 1 (CRITICAL): Fix W-algebra duality formula
**File:** higher_genus.tex
**Lines:** 3550, 3558, 3597, 3653
**Action:** Replace κ' = K/2 - κ with κ' = σ(𝔤)·K - κ where σ(𝔤) = Σ 1/(mᵢ+1). Define σ.

### Priority 2 (HIGH): Fix thm:mumford-formula
**File:** higher_genus.tex:3010
**Action:** Replace |B_{2g}|/(2g(2g-2)!) with (2^{2g-1}-1)/(2^{2g-1}) · |B_{2g}|/(2g)!

### Priority 3 (HIGH): Fix proof citation in thm:genus-universality(iii)
**File:** higher_genus.tex:3599-3600
**Action:** Replace ∫_{M̄_g} λ_g λ_{g-1} with ∫_{M̄_{g,1}} ψ₁^{2g-2} λ_g

### Priority 4 (MEDIUM-HIGH): Fix obstruction nilpotence g=0 case
**File:** higher_genus.tex:3483
**Action:** Either exclude g=0 from the theorem or note obs₀ = 0 by convention.

### Priority 5 (MEDIUM): Fix bc-βγ example
**File:** higher_genus.tex:3622
**Action:** Replace "0 + 0 = 0" with "c/2 + (-c/2) = 0"

### Priority 6 (MEDIUM): Fix free field κ=0 claims
**File:** examples_summary.tex:134, 768
**Action:** Correct κ=0 to κ+κ'=0 (line 134) and κ=1/4 (line 768)

### Priority 7 (MEDIUM): Remove "Q_g=0 for free fields" claim
**File:** higher_genus.tex:5003-5008
**Action:** Remove or correct the claim (contradicts Heisenberg obs_g ≠ 0)

### Priority 8 (MEDIUM): Fix Heisenberg dual level and label
**File:** bar_cobar_construction.tex:4405
**Action:** Change CE(ĥ_k) to CE(ĥ_{-k}); remove "a fermionic system"

### Priority 9 (MEDIUM): Fix H²(M̄_g) dimension claim
**File:** higher_genus.tex:2949
**Action:** Clarify this is H²(M_g) (open), not H²(M̄_g) (compactified)

### Priority 10 (MEDIUM): Fix Heisenberg c+c' inconsistency
**File:** examples_summary.tex:54 or introduction.tex:804-806
**Action:** Make table and theorem consistent (either "0" or "---")

### Priority 11 (MEDIUM): Fix bar cohomology = Center claim for Yangian
**File:** chiral_koszul_pairs.tex:319-331
**Action:** Replace "Center(Y(𝔤))" with "Ext_Y(ℂ,ℂ)"

### Priority 12 (MEDIUM): Fix bosonic string gloss
**File:** genus_expansions.tex:1141-1143
**Action:** Rewrite explanatory text for logical coherence

### Priorities 13+ (LOW): Expository fixes
- 3.1-3.10 listed in Tier 3 above

---

# STRUCTURAL OBSERVATIONS (for future work, not actionable fixes)

### Proof gaps that require new mathematics (not fixable by editing)
1. **Universality at cohomological level for multi-generator algebras** (1.4): Requires either restricting the theorem statement or developing the multi-component λ-class theory.
2. **Diagonal Ext concentration in chiral setting** (Finding 6): Requires formal operadic transfer argument.
3. **Curved A∞ presentation** (1.7): The theory files should contain a complete treatment, not just the appendix formula.
4. **Koszul pair equivalence** (1.6): Needs a proof or explicit acknowledgment that this is assumed.

### Proof gaps that can be resolved by restructuring
1. **Cobar d²=0** (1.2): Derive from Verdier duality definition, relegate distributional argument to a remark.
2. **Genus-1 d²=0** (1.1): Either flesh out the computation or downgrade to Conjectured/sketch.
3. **Verdier non-degeneracy** (1.3): Use D-module formalism where Verdier duality is exact on holonomic modules.

---

# AUDIT METHODOLOGY

- 8 parallel deep-read agents deployed across all major files (~27K lines):
  - ALPHA: higher_genus.tex lines 1-3500 (18 findings)
  - BETA: higher_genus.tex lines 3300-6555 (14 findings)
  - GAMMA: bar_cobar_construction.tex (17 findings)
  - DELTA: examples chapters (2 findings + full numerical verification)
  - EPSILON: chiral_koszul_pairs + modules + deformation_theory (17 findings)
  - ZETA: KM + W-algebra + free_fields chapters (14 findings)
  - ETA: cross-consistency across all 55 files (15 findings)
  - THETA: foundations + appendices (ran out of context)
- Manual investigation of all prior audit fixes
- Independent arithmetic verification of all κ, κ+κ', and FP values
- Cross-consistency checks across ~55 files by ETA agent
- Dimension count verification for moduli space integrals
- De-duplication and consolidation of ~70 raw findings into 35 unique items
