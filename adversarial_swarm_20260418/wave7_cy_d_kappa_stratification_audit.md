# Wave-7 CY-D κ stratification audit (2026-04-18)

Target: Vol III `chapters/examples/cy_d_kappa_stratification.tex` (1394 lines), `compute/lib/kappa_bkm_universal.py`, `compute/lib/diagonal_siegel_cy_orbifolds.py::FRAME_SHAPE_DATA`, and the associated test files.

Scope: CLAUDE.md CY-D dimension stratification row. Adversarial sweep for AP238 statement/proof/engine drift, AP245 (forward), AP277 (vacuous HZ-IV), AP283 (formula confabulation), AP289 (Künneth multiplicative vs additive), AP310 (shared intermediate), AP290 (κ-subscript type swap).

## 1. Per-value Hodge supertrace verification

| d | X | h^{0,·} (inscribed) | Ξ = Σ (-1)^q h^{0,q} | κ_ch inscribed | verdict |
|---|---|---|---|---|---|
| 1 | E | (1,1) | 0 | 0 | ✓ |
| 2 | K3 | (1,0,1) | 2 | 2 | ✓ |
| 2 | E×E | (1,2,1) | 0 | 0 | ✓ |
| 2 | bielliptic | (1,1,0) | 0 | 0 | ✓ |
| 3 | X_5 quintic | (1,0,0,1) | 0 | 0 | ✓ |
| 3 | K3 × E | (1,1,1,1) (Künneth) | 0 | 0 | ✓ (multiplicative: 2·0 = 0) |
| 3 | E^3 | (1,3,3,1) | 0 | 0 | ✓ (Serre odd-d) |
| 3 | local P² | toric, via Dolbeault | 3/2 | 3/2 | ✓ inherited from thm:local-p2-shadow |
| 3 | conifold | non-compact | — | 1 (McKay) | ✓ not-local-surface, Cor ap38-44 |
| 4 | X_6 sextic | (1,0,0,0,1) | 2 | 2 | ✓ |
| 4 | octic double | (1,0,149,0,1) | 151 | 151 | ✓ |
| 4 | decic | (1,0,0,0,1) | 2 | 2 | ✓ |
| 4 | K3^{[2]} | (1,0,1,0,1) | 3 | 3 | ✓ (n+1 = 3 at n=2) |
| 4 | F(Y) | (1,0,1,0,1) | 3 | 3 | ✓ deformation to K3^{[2]} |
| 5 | X_7 septic | (1,0,0,0,0,1) | 0 | 0 | ✓ Serre 3 pairs |
| 5 | Borisov-Caldararu X,Y | (1,0,0,0,0,1) | 0 | 0 | ✓ |
| 5 | K3 × X_5 | (1,0,1,1,0,1) | 0 | 0 | ✓ Künneth |

ALL INSCRIBED κ_ch VALUES MATCH THE HODGE SUPERTRACE. No AP238 contradiction within the chapter body.

## 2. AP289 discipline (Künneth multiplicative vs additive)

Chapter explicitly states multiplicativity Ξ(X×Y) = Ξ(X)·Ξ(Y) at lines 156-169 and notes that the additive and multiplicative rules coincide on the tabulated products only because at least one factor has Ξ = 0. The K3 × K3^{[2]} divergence (mult 6 vs add 5) is explicitly flagged. The Wave-4 CY-D heal (13 edits) holds — no residual AP289 drift detected in this chapter.

## 3. Route A (Hodge supertrace) vs Route B (Heisenberg level) collision

Lines 414-426: explicit inscription. κ_ch(Φ_1(D^b(E))) = 0 (Route A), separately κ(H_1) = 1 (Vol I census κ_Heis = k, Route B). Reconciliation given: Φ_1 and Heisenberg-level-1 are distinct algebraizations. AP234 collision is NOT silently present; the chapter explicitly disambiguates. Wave-6 concern addressed.

## 4. κ_BKM universal formula: three-way contradiction (CRITICAL FINDING)

The chapter (line 1163), CLAUDE.md CY-D row, and FRAME_SHAPE_DATA agree:
- N=1 → weight 5, c_1(0) = 10, κ_BKM = 5 (via Gritsenko Δ_5, paramodular level 1)
- N=2 → weight 4, c_2(0) = 8, κ_BKM = 4
- N=3 → weight 3, c_3(0) = 6, κ_BKM = 3
- N=4 → weight 2, c_4(0) = 4, κ_BKM = 2
- N=6 → weight 1, c_6(0) = 2, κ_BKM = 1

BUT `compute/tests/test_cy_d_kappa_stratification.py::TestBorcherdsWeightUniversal::test_borcherds_weights_universal` (lines 437-448) hardcodes a DOUBLED table:

```
(1, 20, 10),  # N=1: c_1(0)=20, weight 10 — DOUBLES Gritsenko Δ_5 to Igusa Φ_10
(2, 12, 6),   # N=2: c_2(0)=12, weight 6 — DOUBLES FRAME_SHAPE_DATA[2]
(3, 6, 3),    # matches
(4, 4, 2),    # matches
(6, 2, 1),    # matches
```

This is an AP238 statement/proof/engine inconsistency at N=1,2 specifically. The test comment claims source "Gritsenko-Hulek-Sankaran 2008 Moduli of K3 Chapter 5" but GHS Ch.5 for PARAMODULAR level N=1 is Gritsenko Δ_5 at weight 5, not Igusa Φ_10 at weight 10. The test file conflates SIEGEL GENUS-2 at level 1 (Igusa Φ_10) with PARAMODULAR LEVEL 1 (Gritsenko Δ_5). At N=2 analogous doubling appears (weight 6 vs 4; the chapter specifies weight 4 via c_2(0)/2 with c_2(0)=8).

Test `test_N1_naive_decomposition_fails` (line 457) inherits the bug: `N1_weight = F(10)` — this asserts "κ_BKM = 10" for K3×E, contradicting the chapter's inscribed κ_BKM(Φ_1) = 5.

## 5. HZ-IV decorator disjointness (AP277 / AP310 finding)

99+ BKM universality tests rely on `FRAME_SHAPE_DATA[N]` where `borcherds_weight` and `c_disc_0` are BOTH hardcoded with the tautological relation `borcherds_weight = c_disc_0 / 2` baked into the table. The acknowledgment comment at test_kappa_bkm_universal.py:759-767 is honest: "those tests are tautological: verification source identical to derivation source."

GENUINE DISJOINT DECORATOR: `TestIndependentVerificationN1::test_c0_K3_via_theta_ratio_matches_frame_shape` (line 787-849) is CORRECTLY wired — independent computation via `phi01_fourier.phi01_by_discriminant(0)` through Eichler-Zagier theta-ratio algebra. This IS a genuine AP277-compliant disjoint verification. Counts as 1 of the 2 Vol III HZ-IV genuine entries per CLAUDE.md HZ-IV coverage snapshot.

The 8 `@independent_verification` decorators in `test_cy_d_kappa_stratification.py` — not individually audited in this note; Wave-9 AP288 lint recommended for full body-disjointness pass. The BKM-universal decorator at line 403 passes label disjointness (frame-shape vs Borcherds 1995 vs GHS 2008) but the test BODY (line 427-448) computes only `Fraction(c0, 2) == Fraction(weight)` using the bug-doubled table — this is AP288 violation (decorator labels disjoint, body computes single pseudo-check with stale numerics).

## 6. Engine N=5,7,8 scope drift vs CLAUDE.md "five Borcherds families"

FRAME_SHAPE_DATA contains N ∈ {1..8}; chapter and CLAUDE.md restrict to N ∈ {1,2,3,4,6} "five Borcherds families". Engine entries at N=5 (Frame {1^4, 5^4}, wt 2, c_0 4), N=7 (wt 1, c_0 2), N=8 (wt 1, c_0 2) are present without corresponding chapter coverage. Not an error in the chapter, but a scope inflation hazard for future agents reading only the engine. RECOMMEND: engine docstring note that N=5,7,8 are non-K3-orbifold frames (Mathieu M_24 classes with frame shape but not CY₃ orbifold realization) and chapter covers only the five CY-K3 orbifold families.

## 7. κ-subscript discipline (HZ-7 / AP290)

Grepped for bare `\kappa[^_]`; chapter consistently uses `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{cat}}`, `\kappa_{\mathrm{BKM}}`, `\kappa_{\mathrm{fiber}}`. No violations. Proposition at line 1174 and surrounding discussion uses the correct subscripts for each claim. AP290 type-swap check: chapter's κ_ch formulas consistently use Hodge-supertrace (correct for κ_ch via the identification theorem); κ_BKM formulas consistently use Borcherds weight c_N(0)/2 (correct). No type-swap detected.

## 8. Heals

### Heal H1 (MINIMAL, AP238/AP245 fix). Test `test_borcherds_weights_universal` N=1,2 rows

```python
# in /Users/raeez/calabi-yau-quantum-groups/compute/tests/test_cy_d_kappa_stratification.py:437-443
# BEFORE (incorrect; Igusa Φ_10 / doubled Gritsenko convention mixed with level-3,4,6)
(1, 20, 10),
(2, 12, 6),
(3, 6, 3),
(4, 4, 2),
(6, 2, 1),
# AFTER (paramodular-level-N convention, matching chapter + FRAME_SHAPE_DATA + CLAUDE.md)
(1, 10, 5),    # Gritsenko Δ_5 paramodular level 1, c_1(0) = 10, weight = 5
(2, 8, 4),     # paramodular level 2, c_2(0) = 8, weight = 4
(3, 6, 3),
(4, 4, 2),
(6, 2, 1),
```

Docstring N=1..N=6 in test header (lines 430-435) needs parallel correction:
- N=1: Δ_5 (Gritsenko paramodular level 1), weight 5, c_1(0) = 10
- N=2: paramodular level 2, weight 4, c_2(0) = 8

### Heal H2 (AP238). `test_N1_naive_decomposition_fails`

Line 457: `N1_weight = F(10)` → `N1_weight = F(5)`. Parallel update to line 450-463 docstring: "κ_BKM(Δ_5) = 5 is NOT κ_ch(K3×E) + χ(O_E) = 0+0 = 0".

### Heal H3 (AP238). `test_N2_kummer_decomposition_fails`

Line 467: `N2_weight_from_c0 = F(12, 2)  # = 6` → `N2_weight_from_c0 = F(8, 2)  # = 4`. Downstream assertions in that function must be re-verified (not read in this audit).

### Heal H4 (AP277/AP310 upgrade, OPTIONAL). Non-N=1 BKM universality

For N=2,3,4,6: add per-N disjoint verification paths analogous to N=1. Candidate disjoint sources for N=2 Gritsenko form: (a) Aoki-Ibukiyama 2005 explicit Fourier expansion of Siegel paramodular Jacobi form of level 2; (b) direct orbifold-averaging computation of Frame shape {1^8, 2^8} character trace. Tabulation without independent computation remains AP310-SHARED-INTERMEDIATE.

## 9. Residual open

- **OF1 (Wave-3 carryover)**: A1 Zwegers polar-coefficient scope vs full shadow-equation check at d=2 Mock modular K3 — not touched by this audit; upstream of the CY-D chapter.
- **OF2**: HKR chain-level at d ≥ 3. Chapter's Theorem thm:kappa-hodge-supertrace-identification Step 1 cites "Theorem thm:hkr-cy". Status of that theorem at d ≥ 3 unverified here.
- **OF3**: Engine scope for N ∈ {5,7,8} non-CY orbifold frames (see §6).

## 10. Commit plan

No commits by this agent (readonly mission). Recommended owner-side commits:
1. Apply H1 + H2 + H3 (3-line diff in `test_cy_d_kappa_stratification.py`) as a single commit titled `Vol III CY-D κ_BKM test H1/H2/H3: align test-N=1,2 with Gritsenko paramodular convention (AP238 heal)`.
2. Verify `make test` passes after the changes (the assertions were passing on doubled values, so a simple numerics flip will cause re-verification).
3. Cross-check CLAUDE.md N=1,2 entries remain consistent (they already do; no CLAUDE.md change required).

Signed: adversarial-audit agent, 2026-04-18.
