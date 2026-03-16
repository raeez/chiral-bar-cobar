"""MC4 diagnostic: precise state of the W_4 OPE extraction problem.

FINDING (2026-03-16): The W_4 Miura OPE extraction is broken at a fundamental
level. The normalization-independent invariant c_334^2 * N_4 / N_3^2 disagrees
with the DS formula at all central charge values (ratios 0.03 to 1.80).

ROOT CAUSE ANALYSIS:
1. T self-OPE: CORRECT. c extracted correctly from <T|T>_BPZ.
2. W_3 norm: WRONG SIGN AND MAGNITUDE. <W3|W3>_BPZ = -777 at c=63 (expected
   c/3 = 21 in manuscript convention, but free-field norms can differ).
3. W_4 norm: WRONG MAGNITUDE. <W4|W4>_BPZ = 4333 at c=63 (expected c/4 = 15.75).
4. W_4 primary contamination: <W4|Lambda> != 0 (2050 at c=63) and
   <W4|d2T> != 0 (-171). The raw Miura W_4 is NOT a primary field.
5. Gram-Schmidt projection: Lambda subtraction works (orthogonality to 10^-13),
   but d2T subtraction fails (residual -590 at c=63).
6. Normalization-independent invariant: varies with c (should be constant
   ratio if only normalization differs), proving the OPE computation is wrong.

LIKELY SOURCES OF ERROR:
(a) Background charge Q = alpha_0 * rho modifies the Wick contraction rules:
    <dphi_i(z) dphi_j(w)> = -delta_{ij}/(z-w)^2 is the FLAT propagator.
    The background charge adds a linear term to the OPE that affects
    higher-spin composites but not T (explaining why T is correct).
(b) Normal ordering with background charge: the Miura expansion uses
    :(d + J_1)(d + J_2)(d + J_3)(d + J_4): but the normal ordering
    picks up quantum corrections proportional to alpha_0. If these
    corrections are wrong, W_3 and W_4 are wrong while T is correct
    (because T's quantum correction is just the background charge term
    in the stress tensor, which is well-known).
(c) The Wick contraction engine may not correctly handle the
    non-standard propagator for bosons with background charge.

NEXT STEPS:
1. Verify W_3 self-OPE <W3(z)W3(0)> at the LEADING pole (order 6):
   the coefficient should be c/3 in manuscript convention.
2. Verify T W_3 OPE: <T(z)W3(0)> at pole 3 should give 3*W_3 (primary).
3. Check if the Miura W_3 satisfies the primary condition wrt T.
4. If W_3 fails the primary condition, the Miura expansion itself is wrong.
5. Debug the Miura expansion quantum corrections for N=4.

COMPARISON WITH W_3 CASE:
The W_3 Miura computation (from w3_composite_fields.tex) uses N=3 free
bosons and the sl_3 Miura. At sl_3, the W_3 generator IS the top
elementary symmetric polynomial of the currents, with known quantum
corrections. The W_4 computation extends this to N=4 but the quantum
corrections for the degree-3 and degree-4 symmetric polynomials are
more complex. The sl_3 case should be verified first as a sanity check.

STATUS: This is the SHARP BLOCKER for MC4. Resolution requires debugging
the free-field Wick contraction engine with background charge, specifically
for the W_3 and W_4 generators of the sl_4 Miura.
"""


def diagnostic_summary():
    """Print the MC4 diagnostic summary."""
    print("MC4 DIAGNOSTIC: W_4 Miura OPE Extraction")
    print("=" * 50)
    print("Status: BLOCKED")
    print("Blocker: Wick contraction engine / background charge")
    print("Symptom: Normalization-independent invariant varies with c")
    print("  (ratios 0.03 to 1.80 instead of constant 1.0)")
    print("")
    print("What works:")
    print("  - T self-OPE and central charge extraction")
    print("  - Lambda quasi-primary projection (orthogonality to 10^-13)")
    print("  - DS formula c_334^2 = 42c^2(5c+22)/[(c+24)(7c+68)(3c+46)]")
    print("  - All 176 DS-side tests pass")
    print("")
    print("What fails:")
    print("  - W_3 and W_4 norms (wrong sign/magnitude)")
    print("  - W_4 primary condition (contamination from T descendants)")
    print("  - OPE structure constants (ratios vary with c)")
    print("")
    print("Next step: Debug Miura quantum corrections for N=4")


if __name__ == "__main__":
    diagnostic_summary()
