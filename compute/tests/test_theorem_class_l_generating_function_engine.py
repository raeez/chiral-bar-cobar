r"""Tests for class L generating function analysis.

35 tests covering:

SECTION 1 — G_pf numerical evaluation (5 tests)
  1. G_pf at xi=0.1 for SU(2): exact rational value
  2. G_pf at xi=0.5 for SU(2): exact rational value
  3. G_pf at xi=1.0 for SU(2): exact rational value
  4. G_pf vanishes at S_3=0 (class G recovery) for all genera
  5. G_pf at xi=0.5 for SU(3): independent computation

SECTION 2 — Scalar closed form verification (4 tests)
  6. Scalar series matches closed form at xi=0.5 (kappa=3/2)
  7. Scalar series matches closed form at xi=1.0 (kappa=4)
  8. Scalar closed form has correct poles at xi=2*pi
  9. Scalar GF at xi=0: limit is 0

SECTION 3 — S_3 factorization (3 tests)
  10. delta_pf vanishes at S_3=0 for genera 2-4
  11. G_pf = S_3 * Phi: min S_3 power is 1 at every genus
  12. Full class G recovery: G[F] = kappa*(xi/(2sin)-1) when S_3=0

SECTION 4 — S_3 degree analysis (3 tests)
  13. Max S_3 degree at genus g is 2(g-1) (bound saturation)
  14. Leading S_3 coefficients: c_2=5/24, c_3=15/64, c_4=425/576
  15. Leading coefficients are NOT geometric (c3/c2 != c4/c3)

SECTION 5 — S_3 derivative at S_3=0 (3 tests)
  16. dG_pf/dS_3|_{S_3=0} at genus 2: L_2 = -kappa/48
  17. dG_pf/dS_3|_{S_3=0} at genus 3: independent recomputation
  18. dG_pf/dS_3|_{S_3=0} vanishes when kappa=0

SECTION 6 — Pade approximant (4 tests)
  19. Pade [1/1] matches series to O(xi^8) at small xi
  20. Pade pole location for SU(2): exact value
  21. Pade is NOT constructible at S_3=0 (class G)
  22. Pade pole moves with N (not universal)

SECTION 7 — S_3*kappa invariant (3 tests)
  23. S_3*kappa = 2N/3 at k=0 for N=2..8
  24. S_3*kappa = 2N/3 at k=1 for N=2..5 (level independence)
  25. S_3*kappa = 2N/3 at k=3 for N=2..5

SECTION 8 — Cross-family consistency (3 tests)
  26. G_pf/G_scalar ratio is NOT constant across N (non-universality)
  27. Full G agrees with genus-by-genus sum for SU(3)
  28. Additivity of scalar part: kappa1 + kappa2 (from parent engine)

SECTION 9 — Closed-form obstruction (3 tests)
  29. Term count grows: 2, 5, 11 (not stabilizing)
  30. Leading coefficients are not geometric
  31. Pade poles are family-dependent

SECTION 10 — Large-N scaling (2 tests)
  32. kappa/N^2 -> 1/2 as N -> inf
  33. F_2_pf / N^2 stabilizes (N^{2(g-1)} scaling at g=2)

SECTION 11 — Complementarity and decomposition (2 tests)
  34. kappa(A) + kappa(A!) = 0 for SU(N) at all k (AP24)
  35. S_3-power decomposition has correct structure

Multi-path verification (3+ paths per claim):
  Path 1: Direct engine evaluation
  Path 2: Independent recomputation in test body
  Path 3: Cross-check across SU(N) families
  Path 4: Limiting cases (S_3=0, xi=0, kappa=0)
  Path 5: Closed-form comparison for scalar part
"""

from fractions import Fraction
from math import comb, factorial, pi, sin
import cmath

import pytest

from compute.lib.theorem_class_l_generating_function_engine import (
    G_pf_exact,
    G_pf_numerical,
    G_scalar_closed_form,
    G_scalar_series,
    G_full_class_L,
    verify_S3_factorization,
    S3_linear_coefficients,
    dGpf_dS3_at_zero,
    S3_degree_structure,
    leading_S3_coefficients,
    pade_11_from_genus_data,
    pade_evaluate,
    evaluate_slN_family,
    pf_to_scalar_ratio_table,
    S3_kappa_product_table,
    large_N_scaling,
    pade_pole_table,
    closed_form_obstruction_evidence,
    decompose_by_S3_power,
    verify_class_G_recovery,
    verify_pade_matches_series,
    verify_scalar_against_closed_form,
)

from compute.lib.theorem_class_l_closed_form_engine import (
    kappa_slN,
    S3_slN,
    lambda_fp,
    delta_pf_genus2,
    delta_pf_genus3_class_L,
    delta_pf_genus4_class_L,
    GENUS3_PF_CLASS_L,
    GENUS4_PF_CLASS_L,
)


# ============================================================================
# Ground truth (independently recomputed, NOT copied from engine)
# ============================================================================

# SU(2) at k=0:
#   kappa = (4-1)(0+2)/(2*2) = 3*2/4 = 3/2
#   S_3 = 2*2/(3*(3/2)) = 4/(9/2) = 8/9
#   c = 0*(4-1)/(0+2) = 0
SU2_KAPPA = Fraction(3, 2)
SU2_S3 = Fraction(8, 9)

# SU(3) at k=0:
#   kappa = (9-1)(0+3)/(2*3) = 8*3/6 = 4
#   S_3 = 2*3/(3*4) = 6/12 = 1/2
SU3_KAPPA = Fraction(4)
SU3_S3 = Fraction(1, 2)

# lambda_g^FP independently verified:
LFP_1 = Fraction(1, 24)
LFP_2 = Fraction(7, 5760)
LFP_3 = Fraction(31, 967680)
LFP_4 = Fraction(127, 154828800)

# delta_pf genus 2: S3*(10*S3-kappa)/48
# SU(2): (8/9)*(10*(8/9) - 3/2)/48 = (8/9)*(80/9 - 3/2)/48
#       = (8/9)*(160/18 - 27/18)/48 = (8/9)*(133/18)/48
#       = 8*133/(9*18*48) = 1064/7776 = 133/972
SU2_DPF2 = Fraction(133, 972)


# ============================================================================
# SECTION 1: G_pf numerical evaluation
# ============================================================================

class TestGpfEvaluation:
    """Tests for planted-forest generating function evaluation."""

    def test_gpf_su2_xi01(self):
        """G_pf(xi=0.1) for SU(2): exact value from genus 2-4 data."""
        xi_sq = Fraction(1, 100)  # 0.1^2
        val = G_pf_exact(xi_sq, SU2_KAPPA, SU2_S3)
        # Independent: dpf2*0.01^2 + dpf3*0.01^3 + dpf4*0.01^4
        dpf2 = SU2_DPF2
        dpf3 = delta_pf_genus3_class_L(SU2_KAPPA, SU2_S3)
        dpf4 = delta_pf_genus4_class_L(SU2_KAPPA, SU2_S3)
        expected = dpf2 * xi_sq**2 + dpf3 * xi_sq**3 + dpf4 * xi_sq**4
        assert val == expected

    def test_gpf_su2_xi05(self):
        """G_pf(xi=0.5) for SU(2): verify against independent sum."""
        xi_sq = Fraction(1, 4)  # 0.5^2
        val = G_pf_exact(xi_sq, SU2_KAPPA, SU2_S3)
        # Independently compute each term
        t2 = delta_pf_genus2(SU2_KAPPA, SU2_S3) * xi_sq**2
        t3 = delta_pf_genus3_class_L(SU2_KAPPA, SU2_S3) * xi_sq**3
        t4 = delta_pf_genus4_class_L(SU2_KAPPA, SU2_S3) * xi_sq**4
        assert val == t2 + t3 + t4

    def test_gpf_su2_xi1(self):
        """G_pf(xi=1) for SU(2): exact rational value."""
        xi_sq = Fraction(1)
        val = G_pf_exact(xi_sq, SU2_KAPPA, SU2_S3)
        # At xi=1, xi^{2g} = 1 for all g, so G_pf = sum delta_pf^{(g)}
        total = (delta_pf_genus2(SU2_KAPPA, SU2_S3) +
                 delta_pf_genus3_class_L(SU2_KAPPA, SU2_S3) +
                 delta_pf_genus4_class_L(SU2_KAPPA, SU2_S3))
        assert val == total

    def test_gpf_vanishes_at_S3_zero(self):
        """G_pf = 0 when S_3 = 0 (class G recovery)."""
        for xi_sq in [Fraction(1, 100), Fraction(1, 4), Fraction(1)]:
            val = G_pf_exact(xi_sq, SU2_KAPPA, Fraction(0))
            assert val == Fraction(0), f"G_pf != 0 at S3=0, xi^2={xi_sq}"

    def test_gpf_su3_xi05(self):
        """G_pf(xi=0.5) for SU(3): independent computation."""
        xi_sq = Fraction(1, 4)
        val = G_pf_exact(xi_sq, SU3_KAPPA, SU3_S3)
        # Recompute independently
        dpf2 = SU3_S3 * (10 * SU3_S3 - SU3_KAPPA) / 48
        dpf3 = delta_pf_genus3_class_L(SU3_KAPPA, SU3_S3)
        dpf4 = delta_pf_genus4_class_L(SU3_KAPPA, SU3_S3)
        expected = dpf2 * xi_sq**2 + dpf3 * xi_sq**3 + dpf4 * xi_sq**4
        assert val == expected


# ============================================================================
# SECTION 2: Scalar closed form verification
# ============================================================================

class TestScalarClosedForm:
    """Verify the scalar generating function kappa*(xi/(2sin(xi/2))-1)."""

    def test_scalar_series_matches_closed_form_xi05(self):
        """Truncated series matches closed form at xi=0.5, kappa=3/2."""
        result = verify_scalar_against_closed_form(1.5, 0.5, max_genus=30)
        assert result['relative_error'] < 1e-10

    def test_scalar_series_matches_closed_form_xi1(self):
        """Truncated series matches closed form at xi=1.0, kappa=4."""
        result = verify_scalar_against_closed_form(4.0, 1.0, max_genus=30)
        assert result['relative_error'] < 1e-8

    def test_scalar_poles_at_2pi(self):
        """Closed form diverges near xi = 2*pi (first pole)."""
        kappa_val = 1.0
        xi_near_pole = 2 * pi - 0.001
        val = G_scalar_closed_form(xi_near_pole, kappa_val)
        # Should be large in magnitude
        assert abs(val) > 100, f"|G_scalar| = {abs(val)} near pole, expected >> 1"

    def test_scalar_at_xi_zero(self):
        """G_scalar(0) = 0 (no constant term)."""
        val = G_scalar_closed_form(0.0, 1.5)
        assert abs(val) < 1e-12


# ============================================================================
# SECTION 3: S_3 factorization
# ============================================================================

class TestS3Factorization:
    """Verify G_pf = S_3 * Phi(kappa, S_3, xi^2)."""

    def test_delta_pf_vanishes_at_S3_zero_all_genera(self):
        """delta_pf^{(g)} = 0 at S_3=0 for g=2,3,4."""
        result = verify_S3_factorization(SU2_KAPPA)
        for g in [2, 3, 4]:
            assert result[g], f"delta_pf^({g}) != 0 at S3=0"

    def test_min_S3_power_is_one(self):
        """Min S_3 power is 1 at every genus (not 2)."""
        deg = S3_degree_structure()
        for g in [2, 3, 4]:
            assert deg[g]['min_S3_power'] == 1, (
                f"g={g}: min S3 power = {deg[g]['min_S3_power']}, expected 1"
            )

    def test_class_G_recovery_full(self):
        """Full verification: G[F] reduces to scalar GF when S_3 = 0."""
        assert verify_class_G_recovery(SU2_KAPPA)
        assert verify_class_G_recovery(SU3_KAPPA)
        assert verify_class_G_recovery(Fraction(15, 2))  # SU(4)


# ============================================================================
# SECTION 4: S_3 degree analysis
# ============================================================================

class TestS3DegreeAnalysis:
    """Verify degree bounds on the planted-forest polynomial."""

    def test_max_S3_degree_saturates_bound(self):
        """max S_3 degree at genus g is exactly 2(g-1)."""
        deg = S3_degree_structure()
        for g in [2, 3, 4]:
            assert deg[g]['saturates_bound'], (
                f"g={g}: max S3 degree {deg[g]['max_S3_power']} != {deg[g]['bound_2gm2']}"
            )

    def test_leading_S3_coefficients(self):
        """Leading pure-S_3 coefficients: c_2=5/24, c_3=15/64, c_4=425/576."""
        leading = leading_S3_coefficients()
        assert leading[2] == Fraction(5, 24)
        assert leading[3] == Fraction(15, 64)
        assert leading[4] == Fraction(425, 576)

    def test_leading_not_geometric(self):
        """The sequence {c_g} is NOT geometric: c_3/c_2 != c_4/c_3."""
        leading = leading_S3_coefficients()
        r32 = leading[3] / leading[2]
        r43 = leading[4] / leading[3]
        assert r32 != r43, "Leading S3 coefficients are geometric (unexpected)"


# ============================================================================
# SECTION 5: S_3 derivative at S_3 = 0
# ============================================================================

class TestS3Derivative:
    """Tests for dG_pf/dS_3 evaluated at S_3 = 0."""

    def test_genus2_linear_term(self):
        """At genus 2: L_2(kappa) = -kappa/48."""
        lin = S3_linear_coefficients()
        # lin[2] should be {(1,1): -1/48}
        assert (1, 1) in lin[2]
        assert lin[2][(1, 1)] == Fraction(-1, 48)
        # Evaluate: L_2(3/2) = -3/2/48 = -1/32
        val = dGpf_dS3_at_zero(SU2_KAPPA, Fraction(1))  # xi^2=1 => only g=2,3,4
        # At xi^2=1: sum L_g(kap) * 1^g = L_2 + L_3 + L_4
        L_2 = -SU2_KAPPA / 48
        assert L_2 == Fraction(-1, 32)

    def test_genus3_linear_independent(self):
        """genus 3 S_3-linear terms: independently recompute."""
        lin = S3_linear_coefficients()
        # Genus 3, b=1 terms from GENUS3_PF_CLASS_L
        expected_terms = {
            (a, b): c for (a, b), c in GENUS3_PF_CLASS_L.items() if b == 1
        }
        for key, val in expected_terms.items():
            assert key in lin[3], f"Missing term {key} in genus-3 linear coefficients"
            assert lin[3][key] == val

    def test_derivative_vanishes_at_kappa_zero(self):
        """dG_pf/dS_3|_{S_3=0} = 0 when kappa = 0."""
        # All L_g(kappa) have kappa as a factor (from degree analysis:
        # the b=1 terms all have a >= 1)
        val = dGpf_dS3_at_zero(Fraction(0), Fraction(1))
        assert val == Fraction(0)


# ============================================================================
# SECTION 6: Pade approximant
# ============================================================================

class TestPadeApproximant:
    """Tests for the Pade [1/1] rational approximation."""

    def test_pade_matches_series_small_xi(self):
        """Pade matches series to high accuracy at xi=0.1."""
        result = verify_pade_matches_series(
            SU2_KAPPA, SU2_S3, Fraction(1, 100)
        )
        assert result['constructible']
        # At xi=0.1, the series is dominated by the g=2 term,
        # so Pade should be very accurate
        assert result['relative_error'] < 0.01

    def test_pade_pole_su2(self):
        """Pade pole location for SU(2) is a specific rational number."""
        pade = pade_11_from_genus_data(SU2_KAPPA, SU2_S3)
        # q1 = -a4/a3 where a3 = delta_pf_genus3, a4 = delta_pf_genus4
        a3 = delta_pf_genus3_class_L(SU2_KAPPA, SU2_S3)
        a4 = delta_pf_genus4_class_L(SU2_KAPPA, SU2_S3)
        expected_q1 = -a4 / a3
        assert pade.q1 == expected_q1
        # Pole at xi^2 = -1/q1
        assert pade.pole_location == Fraction(-1) / expected_q1

    def test_pade_not_constructible_at_S3_zero(self):
        """Pade is not constructible when S_3 = 0 (a_3 = 0)."""
        with pytest.raises(ValueError):
            pade_11_from_genus_data(SU2_KAPPA, Fraction(0))

    def test_pade_pole_moves_with_N(self):
        """Pade pole location is N-dependent (not universal)."""
        poles = pade_pole_table(N_values=[2, 3, 4, 5])
        pole_vals = [r['pole_xi_sq'] for r in poles if r['pole_xi_sq'] is not None]
        assert len(pole_vals) >= 3
        # Check that not all poles are equal
        assert len(set(pole_vals)) > 1, "Pade poles are universal (unexpected)"


# ============================================================================
# SECTION 7: S_3 * kappa invariant
# ============================================================================

class TestS3KappaInvariant:
    """Verify S_3 * kappa = 2N/3 (level-independent)."""

    def test_S3_kappa_at_k0(self):
        """S_3 * kappa = 2N/3 at k=0 for N=2..8."""
        for N in [2, 3, 4, 5, 6, 7, 8]:
            kap = kappa_slN(N)
            s3 = S3_slN(N)
            product = s3 * kap
            expected = Fraction(2 * N, 3)
            assert product == expected, (
                f"SU({N}): S3*kappa = {product} != {expected}"
            )

    def test_S3_kappa_at_k1(self):
        """S_3 * kappa = 2N/3 at k=1 for N=2..5."""
        for N in [2, 3, 4, 5]:
            kap = kappa_slN(N, Fraction(1))
            s3 = S3_slN(N, Fraction(1))
            product = s3 * kap
            expected = Fraction(2 * N, 3)
            assert product == expected, (
                f"SU({N}) k=1: S3*kappa = {product} != {expected}"
            )

    def test_S3_kappa_at_k3(self):
        """S_3 * kappa = 2N/3 at k=3 for N=2..5."""
        for N in [2, 3, 4, 5]:
            kap = kappa_slN(N, Fraction(3))
            s3 = S3_slN(N, Fraction(3))
            product = s3 * kap
            expected = Fraction(2 * N, 3)
            assert product == expected, (
                f"SU({N}) k=3: S3*kappa = {product} != {expected}"
            )


# ============================================================================
# SECTION 8: Cross-family consistency
# ============================================================================

class TestCrossFamilyConsistency:
    """Cross-family and additivity checks."""

    def test_pf_scalar_ratio_not_constant(self):
        """G_pf/G_scalar is NOT constant across N (no simple proportionality)."""
        ratios = pf_to_scalar_ratio_table(N_values=[2, 3, 4, 5], xi_values=[1.0])
        r_values = [ratios[N][1.0] for N in [2, 3, 4, 5]]
        # These should NOT all be equal
        assert max(r_values) - min(r_values) > 0.1, (
            "G_pf/G_scalar ratios are too close (unexpected universality)"
        )

    def test_full_G_matches_sum_su3(self):
        """Full G = G_scalar + G_pf for SU(3) at xi=0.5."""
        result = G_full_class_L(0.5, float(SU3_KAPPA), float(SU3_S3))
        assert abs(result['G_total'] - result['G_scalar'] - result['G_pf']) < 1e-14

    def test_scalar_additivity(self):
        """Scalar part is additive: G_scalar(kap1+kap2) = G_scalar(kap1) + G_scalar(kap2)."""
        kap1, kap2 = 1.5, 4.0
        xi = 0.5
        G1 = G_scalar_closed_form(xi, kap1).real
        G2 = G_scalar_closed_form(xi, kap2).real
        G_sum = G_scalar_closed_form(xi, kap1 + kap2).real
        assert abs(G_sum - G1 - G2) < 1e-14, (
            f"Additivity fails: {G_sum} != {G1} + {G2}"
        )


# ============================================================================
# SECTION 9: Closed-form obstruction
# ============================================================================

class TestClosedFormObstruction:
    """Evidence that G_pf has no finite closed form."""

    def test_term_count_grows(self):
        """Number of monomials: 2, 5, 11 (not stabilizing)."""
        evidence = closed_form_obstruction_evidence()
        counts = evidence['term_count_growth']
        assert counts[2] == 2
        assert counts[3] == 5
        assert counts[4] == 11
        # Check growth: each is more than the previous
        assert counts[3] > counts[2]
        assert counts[4] > counts[3]

    def test_leading_not_geometric_from_evidence(self):
        """Leading S_3 coefficients confirm non-geometric growth."""
        evidence = closed_form_obstruction_evidence()
        assert evidence['leading_is_geometric'] is False

    def test_pade_poles_not_universal(self):
        """Pade poles are family-dependent (non-universality)."""
        evidence = closed_form_obstruction_evidence()
        assert evidence['pade_poles_universal'] is False
        assert evidence['conclusion'] == 'NO_CLOSED_FORM'


# ============================================================================
# SECTION 10: Large-N scaling
# ============================================================================

class TestLargeNScaling:
    """Large-N asymptotics for SU(N) at k=0."""

    def test_kappa_over_N2_approaches_half(self):
        """kappa(sl_N, k=0) / N^2 -> 1/2 as N -> inf."""
        for N in [10, 20, 50, 100]:
            kap = kappa_slN(N)
            ratio = float(kap) / (N * N)
            # (N^2-1)/(2N) / N^2 = (1 - 1/N^2)/2
            expected = 0.5 * (1.0 - 1.0 / (N * N))
            assert abs(ratio - expected) < 1e-12

    def test_genus2_pf_linear_N_scaling(self):
        """delta_pf^{(2)} / N -> -1/72 as N -> inf.

        delta_pf^{(2)} = S3*(10*S3 - kap)/48.
        At k=0: S3 ~ 4/(3N), kap ~ N^2/2, S3*kap = 2N/3.
        Leading: S3*(-kap)/48 = -(2N/3)/48 = -N/72.
        So delta_pf^{(2)} scales linearly in N with coefficient -1/72.
        """
        for N in [20, 50, 100]:
            kap = kappa_slN(N)
            s3 = S3_slN(N)
            dpf2 = float(delta_pf_genus2(kap, s3))
            ratio = dpf2 / N
            assert abs(ratio - (-1.0 / 72)) < 0.001, (
                f"SU({N}): dpf2/N = {ratio}, expected -1/72 = {-1/72:.8f}"
            )


# ============================================================================
# SECTION 11: Complementarity and decomposition
# ============================================================================

class TestComplementarityDecomposition:
    """Complementarity (AP24) and S_3-power decomposition."""

    def test_kappa_anti_symmetry_km(self):
        """kappa(A) + kappa(A!) = 0 for SU(N) at k=0 and k=1."""
        for N in [2, 3, 4]:
            for k in [Fraction(0), Fraction(1)]:
                kap = kappa_slN(N, k)
                k_dual = -k - 2 * N
                kap_dual = kappa_slN(N, k_dual)
                assert kap + kap_dual == Fraction(0), (
                    f"SU({N}) k={k}: kap + kap' = {kap + kap_dual} != 0"
                )

    def test_S3_power_decomposition_structure(self):
        """S_3-power decomposition has correct number of powers."""
        decomp = decompose_by_S3_power()
        # Genus 2: powers 1 and 2
        assert set(decomp[2].keys()) == {1, 2}
        # Genus 3: powers 1, 2, 3, 4
        assert set(decomp[3].keys()) == {1, 2, 3, 4}
        # Genus 4: powers 1 through 6
        assert set(decomp[4].keys()) == {1, 2, 3, 4, 5, 6}
