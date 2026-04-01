r"""
test_w3_prime_locality.py -- Adversarial attack on prime-locality for W_3.

Tests organized by attack vector:
  1. Vacuum character Fourier coefficients (7 tests)
  2. Eta-normalized character and Miura polynomial (5 tests)
  3. Sewing lift S_{W_3}(u) and channel decomposition (5 tests)
  4. Dirichlet coefficients and multiplicativity (8 tests)
  5. Self-dual point c = 50 (3 tests)
  6. Rational c = 2 minimal model (3 tests)
  7. Miura defect analysis (3 tests)
  8. Numerical verification and Euler product (3 tests)
  9. The verdict (2 tests)

Total: 39 tests.
"""

import math
from fractions import Fraction

import pytest

from compute.lib.w3_prime_locality import (
    w3_vacuum_character_coeffs,
    w3_partition_numbers,
    virasoro_partition_numbers,
    w3_excess_over_virasoro,
    eta_normalized_w3_coeffs,
    miura_polynomial_w3,
    S_w3,
    S_w3_T_channel,
    S_w3_W_channel,
    S_w3_channel_additivity,
    S_w3_cross_term,
    dirichlet_coeffs_heisenberg,
    dirichlet_coeffs_w3_total,
    dirichlet_coeffs_w3_T_channel,
    dirichlet_coeffs_w3_W_channel,
    check_multiplicativity,
    multiplicativity_defect_ratio,
    verify_heisenberg_multiplicativity,
    w3_self_dual_data,
    w3_c50_shadow_tower,
    w3_minimal_model_data,
    w3_minimal_model_vacuum_coeffs,
    miura_defect_w3_dirichlet,
    miura_defect_is_obstruction,
    numerical_sewing_lift_comparison,
    w3_euler_product_test,
    w3_prime_locality_verdict,
    sigma_minus_1,
)


# ============================================================================
# 1. Vacuum character Fourier coefficients
# ============================================================================

class TestVacuumCharacter:
    """Test W_3 vacuum character = product of two restricted partition GFs."""

    def test_vacuum_coeffs_initial(self):
        """d_0 = 1 (vacuum), d_1 = 0 (no weight-1 states)."""
        coeffs = w3_partition_numbers(10)
        assert coeffs[0] == 1
        assert coeffs[1] == 0

    def test_vacuum_grade2(self):
        """d_2 = 1: only L_{-2}|0> (T-descendant)."""
        coeffs = w3_partition_numbers(10)
        assert coeffs[2] == 1

    def test_vacuum_grade3(self):
        """d_3 = 2: L_{-3}|0> and W_{-3}|0>."""
        coeffs = w3_partition_numbers(10)
        assert coeffs[3] == 2

    def test_vacuum_grade4(self):
        """d_4: L_{-4}|0>, L_{-2}^2|0>, W_{-4}|0>.
        But W also contributes at grade 4 through the second product.
        Actually: from T: partitions of 4 with parts >= 2: {4}, {2,2} -> 2 states.
        From W: partitions of 4 with parts >= 3: {4}, {3}+something?
        Wait, W contributes 1/(1-q^3)(1-q^4)... at grade 4 we get q^4 -> 1 state.
        But the PRODUCT means we combine both:
          grade 4 = sum_{a+b=4} p_T(a)*p_W(b)
        where p_T counts partitions with parts >= 2 and p_W with parts >= 3.
        p_T(0)=1, p_T(2)=1, p_T(3)=1, p_T(4)=2.
        p_W(0)=1, p_W(3)=1, p_W(4)=1.
        d_4 = p_T(0)*p_W(4) + p_T(1)*p_W(3) + p_T(2)*p_W(2) + p_T(3)*p_W(1) + p_T(4)*p_W(0)
            = 1*1 + 0*1 + 1*0 + 1*0 + 2*1 = 3.
        """
        coeffs = w3_partition_numbers(10)
        assert coeffs[4] == 3

    def test_virasoro_partition_comparison(self):
        """W_3 has strictly more states than Virasoro at grade >= 3."""
        w3 = w3_partition_numbers(10)
        vir = virasoro_partition_numbers(10)
        for m in range(3):
            assert w3[m] == vir[m], f"Should agree at grade {m}"
        for m in range(3, 11):
            assert w3[m] > vir[m], f"W_3 should exceed Virasoro at grade {m}"

    def test_excess_starts_at_grade3(self):
        """The W-generator first contributes at grade 3."""
        excess = w3_excess_over_virasoro(10)
        assert excess[0] == 0
        assert excess[1] == 0
        assert excess[2] == 0
        assert excess[3] == 1  # W_{-3}|0>

    def test_first_20_coefficients_monotone(self):
        """Partition numbers are non-decreasing for m >= 2."""
        coeffs = w3_partition_numbers(20)
        for m in range(2, 20):
            assert coeffs[m + 1] >= coeffs[m], \
                f"d_{m+1} = {coeffs[m+1]} < d_{m} = {coeffs[m]}"


# ============================================================================
# 2. Eta-normalized character and Miura polynomial
# ============================================================================

class TestEtaNormalized:
    """Test eta^2 * chi_0^{W_3} = q^{(2-c)/24} * (1-q)^2 * (1-q^2)."""

    def test_eta_normalized_polynomial(self):
        """eta^2 * chi_0 should give a FINITE polynomial."""
        poly = eta_normalized_w3_coeffs(10)
        # (1-q)^2 * (1-q^2) = 1 - 2q + 0q^2 + 2q^3 - q^4
        assert poly[0] == 1
        assert poly[1] == -2
        assert poly[2] == 0
        assert poly[3] == 2
        assert poly[4] == -1
        for m in range(5, 11):
            assert poly[m] == 0, f"Should vanish at degree {m}"

    def test_miura_polynomial(self):
        """D_3(q) = (1-q)(1-q^2) = 1 - q - q^2 + q^3."""
        miura = miura_polynomial_w3(10)
        assert miura[0] == 1
        assert miura[1] == -1
        assert miura[2] == -1
        assert miura[3] == 1
        for m in range(4, 11):
            assert miura[m] == 0

    def test_miura_degree(self):
        """D_3(q) has degree N*(N-1)/2 = 3*2/2 = 3."""
        miura = miura_polynomial_w3(10)
        # Last nonzero coefficient at degree 3
        assert miura[3] != 0
        assert all(miura[m] == 0 for m in range(4, 11))

    def test_eta_normalized_vs_miura(self):
        """eta^2 * chi_0 = (1-q)^2*(1-q^2) = (1-q) * D_3(q)."""
        eta_norm = eta_normalized_w3_coeffs(10)
        miura = miura_polynomial_w3(10)
        # (1-q)*D_3(q) should give eta_norm
        product = [0] * 11
        for i in range(11):
            product[i] += miura[i]
            if i >= 1:
                product[i] -= miura[i - 1]
        for m in range(11):
            assert product[m] == eta_norm[m], \
                f"Mismatch at degree {m}: {product[m]} vs {eta_norm[m]}"

    def test_miura_sum_of_coefficients(self):
        """D_3(1) = 0 (vanishing at q=1)."""
        miura = miura_polynomial_w3(10)
        assert sum(miura) == 0


# ============================================================================
# 3. Sewing lift and channel decomposition
# ============================================================================

class TestSewingLift:
    """Test S_{W_3}(u) = S^T(u) + S^W(u)."""

    @pytest.fixture(autouse=True)
    def _check_mpmath(self):
        pytest.importorskip("mpmath")

    def test_channel_additivity(self):
        """S_{W_3}(u) = S^T(u) + S^W(u) at u = 3."""
        err = S_w3_channel_additivity(3.0)
        assert err < 1e-25, f"Channel additivity error = {err}"

    def test_channel_additivity_multiple_u(self):
        """Additivity at several values of u."""
        for u_val in [2.5, 3.0, 4.0, 5.0, 10.0]:
            err = S_w3_channel_additivity(u_val)
            assert err < 1e-14, f"Additivity fails at u={u_val}: {err}"

    def test_no_cross_term(self):
        """Cross term is identically zero (up to floating-point)."""
        from mpmath import mpf
        for u_val in [2.5, 3.0, 5.0]:
            cross = S_w3_cross_term(mpf(u_val))
            assert abs(cross) < 1e-14

    def test_t_channel_equals_virasoro(self):
        """S^T(u) = S_Vir(u) = zeta(u+1)*(zeta(u) - 1)."""
        from mpmath import mpf, zeta as mp_zeta
        for u_val in [3.0, 4.0, 5.0]:
            u = mpf(u_val)
            t_ch = S_w3_T_channel(u)
            vir = mp_zeta(u + 1) * (mp_zeta(u) - 1)
            assert abs(float(t_ch - vir)) < 1e-25

    def test_w3_larger_than_heisenberg(self):
        """S_{W_3}(u) > S_H(u) for real u > 1.

        Actually this needs verification.  S_H = zeta(u)*zeta(u+1).
        S_{W_3} = zeta(u+1)*(2*zeta(u) - 2 - 2^{-u}).
        Ratio = (2*zeta(u) - 2 - 2^{-u})/zeta(u) = 2 - 2/zeta(u) - 2^{-u}/zeta(u).
        At u=3: 2/zeta(3) ~ 2/1.202 ~ 1.664, 2^{-3}/zeta(3) ~ 0.104.
        Ratio ~ 2 - 1.664 - 0.104 ~ 0.232.  So S_{W_3} < S_H.
        """
        from mpmath import mpf, zeta as mp_zeta
        u = mpf(3.0)
        w3_val = float(S_w3(u))
        heis_val = float(mp_zeta(u) * mp_zeta(u + 1))
        # W_3 has weight-2 and weight-3 generators, so its sewing lift
        # is SMALLER than Heisenberg (weight-1).
        assert w3_val < heis_val


# ============================================================================
# 4. Dirichlet coefficients and multiplicativity
# ============================================================================

class TestMultiplicativity:
    """The core attack: are the Dirichlet coefficients multiplicative?"""

    def test_heisenberg_is_multiplicative(self):
        """CONTROL: sigma_{-1}(n) IS multiplicative."""
        assert verify_heisenberg_multiplicativity(30)

    def test_heisenberg_coeffs_match_sigma(self):
        """Heisenberg Dirichlet coefficients = sigma_{-1}."""
        coeffs = dirichlet_coeffs_heisenberg(20)
        for n in range(1, 21):
            assert coeffs[n] == sigma_minus_1(n)

    def test_w3_total_not_multiplicative(self):
        """W_3 total sewing lift is NOT multiplicative."""
        coeffs = dirichlet_coeffs_w3_total(30)
        result = multiplicativity_defect_ratio(coeffs, 30)
        assert not result['is_multiplicative'], \
            "W_3 total should NOT be multiplicative"
        assert result['n_violations'] > 0

    def test_w3_T_channel_not_multiplicative(self):
        """T-channel alone is NOT multiplicative."""
        coeffs = dirichlet_coeffs_w3_T_channel(30)
        result = multiplicativity_defect_ratio(coeffs, 30)
        assert not result['is_multiplicative']

    def test_w3_W_channel_not_multiplicative(self):
        """W-channel alone is NOT multiplicative."""
        coeffs = dirichlet_coeffs_w3_W_channel(30)
        result = multiplicativity_defect_ratio(coeffs, 30)
        assert not result['is_multiplicative']

    def test_channel_additivity_dirichlet(self):
        """a_N^{total} = a_N^T + a_N^W for all N."""
        total = dirichlet_coeffs_w3_total(30)
        t_ch = dirichlet_coeffs_w3_T_channel(30)
        w_ch = dirichlet_coeffs_w3_W_channel(30)
        for n in range(1, 31):
            assert total[n] == t_ch[n] + w_ch[n], \
                f"Channel additivity fails at N={n}"

    def test_smallest_violation(self):
        """Find the smallest (m,n) where multiplicativity fails for W_3."""
        coeffs = dirichlet_coeffs_w3_total(30)
        violations = check_multiplicativity(coeffs, 30, "W_3 total")
        assert len(violations) > 0
        first = violations[0]
        # The smallest coprime pair where it fails should be (2, 3)
        assert first['m'] == 2 and first['n'] == 3, \
            f"Expected first violation at (2,3), got ({first['m']}, {first['n']})"

    def test_violation_at_6_explicit(self):
        """Explicit check: a_6 != a_2 * a_3 for the total lift.

        a_2 = 1 (from f_2=1, f_1=0)
        a_3 = 2 (from f_3=2, f_1=0)
        a_6 should be sum_{d|6} f_d / (6/d):
          d=1: f_1/6 = 0
          d=2: f_2/3 = 1/3
          d=3: f_3/2 = 1
          d=6: f_6/1 = 2
          Total = 0 + 1/3 + 1 + 2 = 10/3

        a_2 * a_3 = 1 * 2 = 2 != 10/3.
        """
        coeffs = dirichlet_coeffs_w3_total(10)
        assert coeffs[2] == Fraction(1)
        assert coeffs[3] == Fraction(2)
        assert coeffs[6] == Fraction(10, 3)
        assert coeffs[6] != coeffs[2] * coeffs[3]


# ============================================================================
# 5. Self-dual point c = 50
# ============================================================================

class TestSelfDual:
    """W_3 at c = 50 (self-dual under c <-> 100-c)."""

    def test_kappa_at_c50(self):
        """kappa(W_3, 50) = 5*50/6 = 250/6."""
        data = w3_self_dual_data()
        assert data['kappa_total'] == Fraction(250, 6)

    def test_channel_decomposition(self):
        """kappa_T + kappa_W = kappa_total."""
        data = w3_self_dual_data()
        assert data['kappa_T'] + data['kappa_W'] == data['kappa_total']

    def test_shadow_tower_both_lines(self):
        """Both T-line and W-line towers are computable at c=50."""
        tower = w3_c50_shadow_tower(10)
        # T-line: S_2 = kappa_T = 25 -> coeff[0]/2 = 25
        assert abs(tower['T_line'][0] - 25.0) < 1e-10
        # W-line: S_2 = kappa_W = 50/3
        assert abs(tower['W_line'][0] - 50.0 / 3.0) < 1e-10
        # W-line odd arities vanish (Z_2 parity)
        for r_idx in range(len(tower['W_line'])):
            r = r_idx + 2  # arity
            if r % 2 == 1:
                assert abs(tower['W_line'][r_idx]) < 1e-10, \
                    f"W-line arity {r} should vanish, got {tower['W_line'][r_idx]}"


# ============================================================================
# 6. Rational c = 2 minimal model
# ============================================================================

class TestMinimalModel:
    """W_3 at c = 2: rationality does NOT help."""

    def test_kappa_at_c2(self):
        """kappa(W_3, 2) = 5/3."""
        data = w3_minimal_model_data()
        assert data['kappa_total'] == Fraction(5, 3)

    def test_rationality_irrelevant_for_sewing_lift(self):
        """The sewing lift depends on weight multiset {2,3}, NOT on c."""
        # The sewing lift S_{W_3}(u) is the SAME function for all c.
        # Multiplicativity failure is structural.
        coeffs = dirichlet_coeffs_w3_total(20)
        result = multiplicativity_defect_ratio(coeffs, 20)
        assert not result['is_multiplicative'], \
            "Rationality of c does NOT save multiplicativity"

    def test_minimal_model_vacuum_coeffs(self):
        """Generic partition numbers are an upper bound for minimal models."""
        generic = w3_partition_numbers(10)
        minimal = w3_minimal_model_vacuum_coeffs(10)
        # At generic c these are the same
        for m in range(11):
            assert generic[m] == minimal[m]


# ============================================================================
# 7. Miura defect analysis
# ============================================================================

class TestMiuraDefect:
    """Is D_3(q) the obstruction to prime-locality?"""

    def test_miura_vs_dirichlet_different(self):
        """Miura defect (q-series) != Dirichlet defect."""
        result = miura_defect_is_obstruction(20)
        assert not result['is_identical'], \
            "Miura and Dirichlet defects should be DIFFERENT objects"

    def test_miura_defect_dirichlet_coefficients(self):
        """Check the Dirichlet defect coefficients explicitly."""
        defect = miura_defect_w3_dirichlet(10)
        # O_1 = (sigma_1(1) - 2 - 0)/1 = (1 - 2)/1 = -1
        assert defect[1] == Fraction(-1)
        # O_2 = (sigma_1(2) - 2 - 2)/2 = (3 - 4)/2 = -1/2
        assert defect[2] == Fraction(-1, 2)
        # O_3 = (sigma_1(3) - 2 - 0)/3 = (4 - 2)/3 = 2/3
        assert defect[3] == Fraction(2, 3)

    def test_miura_polynomial_vs_defect_mismatch(self):
        """Miura polynomial [1,-1,-1,1,0,...] differs from Dirichlet defect."""
        miura = miura_polynomial_w3(5)
        defect = miura_defect_w3_dirichlet(5)
        # They should NOT match term-by-term
        mismatch_count = 0
        for n in range(1, 5):
            if miura[n] != defect[n]:
                mismatch_count += 1
        assert mismatch_count > 0


# ============================================================================
# 8. Numerical verification and Euler product
# ============================================================================

class TestNumerical:
    """High-precision numerical checks."""

    @pytest.fixture(autouse=True)
    def _check_mpmath(self):
        pytest.importorskip("mpmath")

    def test_numerical_comparison(self):
        """Basic numerical sanity at u=3."""
        result = numerical_sewing_lift_comparison(3.0)
        assert result['additivity_error'] < 1e-20
        assert result['S_W3'] > 0
        assert result['ratio_W3_over_H'] < 1  # W_3 < Heisenberg

    def test_euler_product_fails(self):
        """S_{W_3}(u) does NOT have an Euler product."""
        result = w3_euler_product_test(3.0)
        assert result['has_euler_product'] is False

    def test_numerical_at_multiple_points(self):
        """Channel additivity at multiple u values."""
        for u_val in [2.5, 3.0, 4.0, 6.0]:
            result = numerical_sewing_lift_comparison(u_val)
            assert result['additivity_error'] < 1e-15


# ============================================================================
# 9. The verdict
# ============================================================================

class TestVerdict:
    """Final comprehensive test."""

    def test_full_verdict(self):
        """Run the full verdict and verify conclusions."""
        verdict = w3_prime_locality_verdict(20)

        # Heisenberg IS multiplicative (control)
        assert verdict['conclusion']['heisenberg_multiplicative']

        # W_3 is NOT multiplicative at any level
        assert not verdict['conclusion']['w3_total_multiplicative']
        assert not verdict['conclusion']['w3_T_channel_multiplicative']
        assert not verdict['conclusion']['w3_W_channel_multiplicative']

    def test_virasoro_also_fails(self):
        """Virasoro (= T-channel of W_3) also fails multiplicativity.

        This is a consequence: S_Vir = S^T_{W_3} is the same series,
        and we already showed it fails.
        """
        t_coeffs = dirichlet_coeffs_w3_T_channel(20)
        result = multiplicativity_defect_ratio(t_coeffs, 20)
        assert not result['is_multiplicative']
