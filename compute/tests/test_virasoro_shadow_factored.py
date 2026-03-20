"""Tests for the Virasoro shadow tower Delta-factored form.

Verifies:
  - S_r = Delta_Vir * R_r for r = 4, ..., 10
  - R_r are rational functions of c
  - Poles of R_r are only at c = 0 and c = -22/5
  - Closed-form R_4 = 1/(4c) = 1/(8*kappa), R_5 = -6/(5c^2)
  - Delta_Vir = 8*kappa*S_4 = 40/(5c+22)
  - Pole order growth pattern
  - Sign alternation of R_r
  - Consistency with existing shadow tower module
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, cancel, fraction, solve, S

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))
from virasoro_shadow_factored import (
    compute_shadow_tower,
    delta_factored_quotients,
    verify_delta_factorization,
    verify_pole_structure,
    verify_closed_forms,
    delta_origin,
    pole_orders,
    sign_pattern,
    Delta_Vir,
    kappa,
    c,
)


class TestDeltaOrigin:
    """Verify the discriminant Delta_Vir = 8*kappa*S_4."""

    def test_delta_equals_40_over_5c_plus_22(self):
        expected = Rational(40) / (5 * c + 22)
        assert simplify(Delta_Vir - expected) == 0

    def test_delta_from_kappa_and_s4(self):
        """Delta_Vir = 8 * kappa * S_4 where kappa = c/2."""
        assert delta_origin()

    def test_kappa_is_c_over_2(self):
        assert simplify(kappa - c / 2) == 0

    def test_delta_pole_at_minus_22_over_5(self):
        val = Delta_Vir.subs(c, Rational(-22, 5))
        from sympy import zoo, oo, nan
        assert val in (zoo, oo, -oo, nan) or not val.is_finite

    def test_delta_positive_for_positive_c(self):
        for c_val in [1, 2, 13, 26, 100]:
            assert Delta_Vir.subs(c, c_val) > 0


class TestDeltaFactorization:
    """Verify S_r = Delta_Vir * R_r for all computed arities."""

    def test_factorization_r4_through_r10(self):
        """Core factorization identity."""
        assert verify_delta_factorization(10)

    def test_factorization_at_each_arity(self):
        """Verify individually at each arity for clear diagnostics."""
        tower = compute_shadow_tower(10)
        quotients = delta_factored_quotients(10)
        for r in range(4, 11):
            reconstructed = cancel(Delta_Vir * quotients[r])
            diff = simplify(tower[r] - reconstructed)
            assert diff == 0, f"Factorization fails at r={r}"

    def test_factorization_numerical_c1(self):
        """Numerical check at c=1."""
        tower = compute_shadow_tower(10)
        quotients = delta_factored_quotients(10)
        delta_val = float(Delta_Vir.subs(c, 1))
        for r in range(4, 11):
            s_val = float(tower[r].subs(c, 1))
            r_val = float(quotients[r].subs(c, 1))
            assert abs(s_val - delta_val * r_val) < 1e-12, (
                f"Numerical factorization fails at r={r}, c=1"
            )

    def test_factorization_numerical_c26(self):
        """Numerical check at c=26 (bosonic string)."""
        tower = compute_shadow_tower(10)
        quotients = delta_factored_quotients(10)
        delta_val = float(Delta_Vir.subs(c, 26))
        for r in range(4, 11):
            s_val = float(tower[r].subs(c, 26))
            r_val = float(quotients[r].subs(c, 26))
            assert abs(s_val - delta_val * r_val) < 1e-12, (
                f"Numerical factorization fails at r={r}, c=26"
            )

    def test_factorization_numerical_c13(self):
        """Numerical check at c=13 (self-dual point)."""
        tower = compute_shadow_tower(10)
        quotients = delta_factored_quotients(10)
        delta_val = float(Delta_Vir.subs(c, 13))
        for r in range(4, 11):
            s_val = float(tower[r].subs(c, 13))
            r_val = float(quotients[r].subs(c, 13))
            assert abs(s_val - delta_val * r_val) < 1e-12, (
                f"Numerical factorization fails at r={r}, c=13"
            )


class TestClosedForms:
    """Verify closed-form expressions for R_4 and R_5."""

    def test_r4_equals_1_over_4c(self):
        quotients = delta_factored_quotients(5)
        expected = Rational(1, 4) / c
        assert simplify(quotients[4] - expected) == 0

    def test_r4_equals_1_over_8kappa(self):
        """R_4 = 1/(8*kappa) with kappa = c/2."""
        quotients = delta_factored_quotients(5)
        assert simplify(quotients[4] - 1 / (8 * kappa)) == 0

    def test_r5_equals_minus_6_over_5c2(self):
        quotients = delta_factored_quotients(5)
        expected = Rational(-6, 5) / c**2
        assert simplify(quotients[5] - expected) == 0

    def test_verify_closed_forms_function(self):
        assert verify_closed_forms()


class TestPoleStructure:
    """Verify poles of R_r lie only at c = 0 and c = -22/5."""

    def test_allowed_poles_r4_through_r10(self):
        """All poles must be in {0, -22/5}."""
        verify_pole_structure(10)

    def test_r4_pole_only_at_zero(self):
        quotients = delta_factored_quotients(5)
        _, denom = fraction(cancel(quotients[4]))
        roots = solve(denom, c)
        assert set(roots) == {S.Zero}

    def test_r5_pole_only_at_zero(self):
        quotients = delta_factored_quotients(5)
        _, denom = fraction(cancel(quotients[5]))
        roots = solve(denom, c)
        assert set(roots) == {S.Zero}

    def test_r6_poles_at_zero_and_minus_22_over_5(self):
        quotients = delta_factored_quotients(6)
        _, denom = fraction(cancel(quotients[6]))
        roots = solve(denom, c)
        assert set(roots) == {S.Zero, Rational(-22, 5)}

    def test_pole_structure_function_returns_data(self):
        poles = verify_pole_structure(10)
        assert isinstance(poles, dict)
        assert 4 in poles and 10 in poles


class TestPoleOrders:
    """Verify pole order growth pattern."""

    def test_pole_order_at_zero(self):
        """ord_{c=0}(R_r) = r - 3."""
        orders = pole_orders(10)
        for r in range(4, 11):
            expected_order = r - 3
            actual = orders[r].get(S.Zero, 0)
            assert actual == expected_order, (
                f"Pole order at c=0 for R_{r}: "
                f"expected {expected_order}, got {actual}"
            )

    def test_pole_order_at_minus_22_over_5(self):
        """ord_{c=-22/5}(R_r) = floor((r-4)/2)."""
        orders = pole_orders(10)
        for r in range(4, 11):
            expected_order = (r - 4) // 2
            actual = orders[r].get(Rational(-22, 5), 0)
            assert actual == expected_order, (
                f"Pole order at c=-22/5 for R_{r}: "
                f"expected {expected_order}, got {actual}"
            )


class TestSignAlternation:
    """Verify sign alternation of R_r."""

    def test_alternating_signs_at_c1(self):
        """R_r alternates sign: R_4 > 0, R_5 < 0, R_6 > 0, ..."""
        signs = sign_pattern(10, c_val=1)
        for r in range(4, 11):
            expected = 1 if r % 2 == 0 else -1
            assert signs[r] == expected, (
                f"Sign of R_{r} at c=1: expected {expected}, got {signs[r]}"
            )

    def test_alternating_signs_at_c26(self):
        """Sign alternation at c=26."""
        signs = sign_pattern(10, c_val=26)
        for r in range(4, 11):
            expected = 1 if r % 2 == 0 else -1
            assert signs[r] == expected, (
                f"Sign of R_{r} at c=26: expected {expected}, got {signs[r]}"
            )


class TestRationality:
    """Verify R_r are rational functions of c (no square roots, etc.)."""

    def test_quotients_are_rational_functions(self):
        quotients = delta_factored_quotients(10)
        for r in range(4, 11):
            R_r = cancel(quotients[r])
            num, den = fraction(R_r)
            # Both numerator and denominator should be polynomials in c
            from sympy import Poly
            try:
                Poly(num, c, domain='QQ')
                Poly(den, c, domain='QQ')
            except Exception:
                pytest.fail(
                    f"R_{r} is not a rational function over Q: {quotients[r]}"
                )


class TestConsistencyWithExistingModule:
    """Cross-check against virasoro_shadow_tower.py."""

    def test_shadow_coefficients_match(self):
        """Our tower agrees with virasoro_shadow_tower.shadow_coefficients."""
        from virasoro_shadow_tower import shadow_coefficients as existing_coeffs
        our_tower = compute_shadow_tower(7)
        existing = existing_coeffs(7)
        for r in range(2, 8):
            diff = simplify(our_tower[r] - existing[r])
            assert diff == 0, (
                f"Mismatch at r={r}: ours={our_tower[r]}, "
                f"existing={existing[r]}"
            )

    def test_s4_matches_q_contact(self):
        """S_4 = Q^contact_Vir = 10/[c(5c+22)]."""
        tower = compute_shadow_tower(4)
        Q_contact = Rational(10) / (c * (5 * c + 22))
        assert simplify(tower[4] - Q_contact) == 0

    def test_s5_matches_known(self):
        """S_5 = -48/[c^2(5c+22)]."""
        tower = compute_shadow_tower(5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(tower[5] - expected) == 0


class TestDeltaFactoredReconstruction:
    """Verify that the full shadow can be reconstructed from the factored form."""

    def test_reconstruct_s4(self):
        """S_4 = Delta * R_4 = [40/(5c+22)] * [1/(4c)] = 10/[c(5c+22)]."""
        R4 = Rational(1, 4) / c
        S4_reconstructed = cancel(Delta_Vir * R4)
        S4_expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(S4_reconstructed - S4_expected) == 0

    def test_reconstruct_s5(self):
        """S_5 = Delta * R_5 = [40/(5c+22)] * [-6/(5c^2)] = -48/[c^2(5c+22)]."""
        R5 = Rational(-6, 5) / c**2
        S5_reconstructed = cancel(Delta_Vir * R5)
        S5_expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(S5_reconstructed - S5_expected) == 0

    def test_numerical_reconstruction_all_arities(self):
        """Numerical reconstruction at c=7."""
        tower = compute_shadow_tower(10)
        quotients = delta_factored_quotients(10)
        delta_val = float(Delta_Vir.subs(c, 7))
        for r in range(4, 11):
            s_val = float(tower[r].subs(c, 7))
            r_val = float(quotients[r].subs(c, 7))
            assert abs(s_val - delta_val * r_val) < 1e-14, (
                f"Numerical reconstruction fails at r={r}, c=7"
            )


class TestHeisenbergLimit:
    """At c -> infinity, the shadow tower should reduce to the Heisenberg limit."""

    def test_delta_vanishes_at_large_c(self):
        """Delta_Vir -> 0 as c -> infinity."""
        from sympy import limit, oo
        lim = limit(Delta_Vir, c, oo)
        assert lim == 0

    def test_r_r_finite_at_large_c(self):
        """R_r -> 0 as c -> infinity for all r >= 4."""
        from sympy import limit, oo
        quotients = delta_factored_quotients(10)
        for r in range(4, 11):
            lim = limit(quotients[r], c, oo)
            assert lim == 0, (
                f"R_{r} does not vanish at c -> infinity: limit = {lim}"
            )


class TestDualityCompatibility:
    """Check compatibility with Vir_c^! = Vir_{26-c} duality."""

    def test_delta_duality(self):
        """Delta_Vir(c) vs Delta_Vir(26-c)."""
        delta_dual = Delta_Vir.subs(c, 26 - c)
        expected_dual = Rational(40) / (5 * (26 - c) + 22)
        assert simplify(delta_dual - expected_dual) == 0

    def test_delta_at_self_dual_point(self):
        """Delta_Vir(13) = 40/(5*13+22) = 40/87."""
        val = Delta_Vir.subs(c, 13)
        assert val == Rational(40, 87)

    def test_r_r_duality_ratio(self):
        """R_r(c)/R_r(26-c) should be a rational function."""
        quotients = delta_factored_quotients(7)
        for r in range(4, 8):
            R_dual = quotients[r].subs(c, 26 - c)
            ratio = cancel(quotients[r] / R_dual)
            num, den = fraction(ratio)
            from sympy import Poly
            # Both should be polynomials in c
            Poly(num, c, domain='QQ')
            Poly(den, c, domain='QQ')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
