# Wave 6 — Shadow = GW(C^3) + Z_g closed forms + arithmetic duality: adversarial attack + heal

**Date:** 2026-04-17
**Target:** Vol I Shadow = GW(C^3) identification, Z_g closed forms (Hurwitz-Bernoulli), arithmetic duality at leading Kummer-irregular primes {691, 3617}.
**Files inspected:**
- `chapters/theory/z_g_kummer_bernoulli_platonic.tex` (primary Z_g + Kummer locus)
- `chapters/theory/shadow_tower_higher_coefficients.tex` (primary S_r tower + Kummer-absence theorem)
- `chapters/theory/higher_genus_modular_koszul.tex` (bar-MacMahon correspondence, DT curve counting)
- `chapters/theory/shadow_L_function_platonic.tex` (shadow-Feynman bridge, citing Shadow=GW row)
- `standalone/cy_to_chiral_functor.tex` (Shadow=GW(C^3) remark)
- `standalone/cy_quantum_groups_6d_hcs.tex` (prop:v3-qg-shadow-gw)
- `compute/tests/test_z_g_s_r_arithmetic_duality.py` (HZ-IV decorators)

## Phase 1. Attack findings

### A1 (VERIFIED). Z_g low-genus closed form
- P_g(n) = n^{g-1}(n^2-1) R_{g-2}(n^2) at g=2 gives n(n^2-1)/6. Substitute n=3: Z_2(1)=4. ✓
- g=3 formula n^2(n^2-1)(n^2+11)/180 at n=3: 9·8·20/180=8. ✓
- Direct cosecant: Z_2(1) = (3/2)(csc²(π/3)+csc²(2π/3)) = (3/2)(4/3+4/3) = 4. ✓

### A2 (VERIFIED). Bernoulli leading 691, 3617 factorization
- B_12 = −691/2730; num(B_12) = −691 (single prime). ✓
- B_16 = −3617/510; num(B_16) = −3617 (single prime). ✓
- 2111 does NOT divide num(B_{2m}) for 2≤2m≤16. ✓ (as required for sharpness claim)

### A3 (VERIFIED). S_r closed forms through r=11 independent of chapter
- Independently recursing the MC master equation S_r = −(1/(rc))·Σ f(j,k)·jk·S_jS_k with initial data (c/2, 2, 10/(c(5c+22)), −48/(c²(5c+22))):
  - S_6 = 80(45c+193)/[3c³(5c+22)²] ✓ (matches chapter thm:s6)
  - S_7 = −2880(15c+61)/[7c⁴(5c+22)²] ✓ (matches thm:s7)
  - S_8 at c=1: 4144720/19683 ✓ (matches CLAUDE.md and thm:s8)

### A4 (VERIFIED). Kummer-irregular prime absence from S_r through r=11
- Independent recursion + polynomial clearing produces integer numerators:
  - N_6 = 45c+193 (primes {3, 5, 193}) — 691, 3617 ABSENT ✓
  - N_7 = −(15c+61) (primes {3, 5, 61}) — 691, 3617 ABSENT ✓
  - N_8 coeffs {33314=2·16657, 16470, 2025} — 691, 3617 ABSENT ✓
  - N_9 coeffs {−29554=−2·7·2111, −15570, −2025} — 691, 3617 ABSENT; 2111 PRESENT (sharpness witness) ✓
  - N_10 coeffs {4969967, 3989790, 1050975, 91125} with primes {2,3,5,7,17,173,2111,292351} — 691, 3617 ABSENT ✓
  - N_11 coeffs {−3988097, −3500190, −990225, −91125} with primes {2,3,5,163,38891,3988097} — 691, 3617 ABSENT ✓
- Full prime set P_{≤11} = {2,3,5,7,17,61,163,173,193,2111,16657,38891,292351,3988097} (matches chapter line 2496-2497).
- CLAUDE.md summary "{61, 193, 2111, 16657, 3988097}" is an abbreviation; the full list in-chapter is correct.

### A5 (VERIFIED). Bar-MacMahon correspondence
- M(q) = Π(1−q^n)^{−n} has coefficient sequence 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500, ... (MacMahon's plane-partition count, OEIS A000219). ✓
- The chapter claim at `thm:bar-macmahon` (higher_genus_modular_koszul.tex:27528-27538) matches independent enumeration.

### A6 (ERROR FOUND). c_9 prefactor arithmetic
- **Chapter claim (z_g_kummer_bernoulli_platonic.tex:384-387):**
  `c_9 = 2^8·8!/16! ... reduces to 1/405405, denominator 3^4·5·7·11·13`
- **Independent computation:** 2^8·8!/16! = 256·40320/20922789888000 = 1/2027025. Prime factorization 2027025 = 3^4 · 5^2 · 7 · 11 · 13.
- The chapter has dropped a factor of 5 (should be 5^2, not 5^1). 2027025 = 5·405405.
- **Impact on conclusion:** NEGLIGIBLE. gcd(3617, 2027025) = 1 (the prime 3617 > max prime in 2027025, which is 13), so 3617 still does NOT appear in c_9's denominator and the Kummer-divisibility conclusion stands. But the arithmetic is wrong as written.
- **Heal:** Replace `1/405405` with `1/2027025` and `3^4·5·7·11·13` with `3^4·5^2·7·11·13`.

### A7 (SCOPE-QUALIFY). Shadow = F_g^{GW,const}(C^3) identification
- C^3 is **noncompact**; classical χ(C^3) is ill-defined. The constant-map GW integral `F_g^{GW,const}(X) = (χ(X)/2)·∫_{M_g} λ_{g-1}^3` (Faber-Pandharipande; BCOV) requires a **compact** X, or equivariantly χ^T(C^3) in the MNOP setup.
- The claim at `cy_quantum_groups_6d_hcs.tex:794-799` and `cy_to_chiral_functor.tex:851-861` asserts equality of the shadow tower at κ=Ψ with F_g^{GW,const}(C^3) "the full GW answer for C^3 (which has no compact curves, hence no worldsheet instantons)". The reasoning is sound (no curve classes for C^3) but the normalization factor — χ(X)/2 — is exactly where non-compactness matters. The claim needs "equivariant" qualification.
- The Volume I CLAUDE.md status table row `Shadow = GW(C^3) | IDENTIFIED | Shadow tower at κ=Ψ produces perturbative constant-map GW free energies...` is consistent with the remark-level (not theorem-level) claim in Vol III standalones.
- **Heal:** The Vol III standalone remark is already appropriately tagged as a Remark (not Theorem), with a Proposition `prop:v3-qg-shadow-gw` making only the DT/MacMahon side explicit. No Vol I edit needed; the identification lives only in CLAUDE.md status row + standalone remarks. Recommend appending equivariant qualification at the next rectification pass.

### A8 (VERIFIED). HZ-IV decorator disjointness
- `test_z_g_s_r_arithmetic_duality.py` declares:
  - derived_from: Hurwitz-Bernoulli leading + MC master-equation
  - verified_against: (i) OEIS A000928 Kummer tabulation; (ii) SymPy bernoulli + factorint
  - disjoint_rationale: Z_g on Bun_{SL_2}; S_r on ChirHoch(Vir_c); verification paths black-box number-theoretic
- Disjointness argument is genuinely sound: the Z_g derivation (cosecant series + Euler even-zeta) shares NO intermediate lemma with the S_r derivation (Riccati MC recurrence on initial data). SymPy factoring has no moduli-of-bundles or chiral-algebra input.
- VERDICT: decorator is non-tautological and the disjoint-rationale holds.

## Phase 2. Heal

The only required correction is A6. A7 is scope-qualification for a remark that already lives in an appropriately hedged environment.

## Phase 3. Summary

**Status after audit:**
- Z_g closed form + Hurwitz-Bernoulli leading + Kummer witnesses {691 @ g=7, 3617 @ g=9}: UNCONDITIONALLY VERIFIED (✓ all low-genus spot checks, ✓ Bernoulli numerators, ✓ prefactor modulo the typo fixed).
- S_r tower through r=11 + Kummer-absence of {691, 3617}: UNCONDITIONALLY VERIFIED.
- Arithmetic duality thm:z-g-s-r-arithmetic-duality: PROVED with genuine HZ-IV disjointness.
- Shadow = F_g^{GW,const}(C^3): appropriately scoped as REMARK + PROPOSITION in Vol III standalones. The MacMahon/MNOP DT side is proved (bar-MacMahon theorem + Bryan-Pandharipande). The GW side on C^3 requires equivariant framing; treat as structural identification, not chain-level equality.

No .tex theorem needs downgrading. One prefactor arithmetic typo (c_9 denominator) to heal.
