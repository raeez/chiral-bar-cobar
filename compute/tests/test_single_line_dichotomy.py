"""
Tests for single-line shadow tower dichotomy (thm:single-line-dichotomy).

Verifies:
  (1) Universal factorization: S_r = Delta * R_r for r >= 4
  (2) Delta = 0 termination: tower stops at arity 3
  (3) Even-arity cascade: alpha=0 => odd shadows zero, even nonzero
  (4) Virasoro recovery: alpha=2, Q=0 reproduces known coefficients
  (5) Closed-form coefficients S_4 through S_7 match eq:pump-S4--S7
"""

import pytest
from sympy import (
    Symbol, Rational, factor, simplify, S, oo
)

from compute.lib.single_line_dichotomy import (
    compute_single_line_tower,
    verify_universal_factorization,
    verify_even_cascade,
    verify_delta_zero_termination,
)


# ================================================================
# Symbolic parameters
# ================================================================

kappa = Symbol('kappa', nonzero=True)
alpha = Symbol('alpha')
Q_sym = Symbol('Q')
c = Symbol('c')


class TestUniversalFactorization:
    """S_r = Delta * R_r for all r >= 4 (thm:single-line-dichotomy)."""

    @pytest.mark.parametrize("r", range(4, 12))
    def test_delta_divides_sr(self, r):
        """Delta = 8*Q*kappa - 9*alpha^2 divides S_r for r >= 4."""
        results = verify_universal_factorization(r)
        assert results[r]['divides'], (
            f"Delta does not divide S_{r}: S_{r} = {results[r]['S_r']}"
        )

    def test_r4_explicit(self):
        """S_4 = Delta / (8*kappa) — eq:pump-S4."""
        coeffs = compute_single_line_tower(kappa, alpha, Q_sym, 4)
        Delta = 8 * Q_sym * kappa - 9 * alpha**2
        expected = Delta / (8 * kappa)
        assert simplify(coeffs[4] - expected) == 0

    def test_r5_explicit(self):
        """S_5 = -3*alpha*Delta / (10*kappa^2) — eq:pump-S5."""
        coeffs = compute_single_line_tower(kappa, alpha, Q_sym, 5)
        Delta = 8 * Q_sym * kappa - 9 * alpha**2
        expected = -3 * alpha * Delta / (10 * kappa**2)
        assert simplify(coeffs[5] - expected) == 0

    def test_r6_explicit(self):
        """S_6 = -(8Qk - 45a^2)*Delta / (48*k^3) — eq:pump-S6."""
        coeffs = compute_single_line_tower(kappa, alpha, Q_sym, 6)
        Delta = 8 * Q_sym * kappa - 9 * alpha**2
        expected = -(8 * Q_sym * kappa - 45 * alpha**2) * Delta / (
            48 * kappa**3
        )
        assert simplify(coeffs[6] - expected) == 0

    def test_r7_explicit(self):
        """S_7 = 9*a*(8Qk - 21a^2)*Delta / (56*k^4) — eq:pump-S7."""
        coeffs = compute_single_line_tower(kappa, alpha, Q_sym, 7)
        Delta = 8 * Q_sym * kappa - 9 * alpha**2
        expected = 9 * alpha * (
            8 * Q_sym * kappa - 21 * alpha**2
        ) * Delta / (56 * kappa**4)
        assert simplify(coeffs[7] - expected) == 0


class TestDeltaZeroTermination:
    """Delta = 0 => S_r = 0 for all r >= 4 (class L)."""

    def test_all_vanish_symbolic(self):
        all_zero, _ = verify_delta_zero_termination(10)
        assert all_zero, "Some S_r nonzero at Delta=0"

    @pytest.mark.parametrize("r", range(4, 11))
    def test_individual_vanish(self, r):
        """S_r vanishes when Q = 9*alpha^2/(8*kappa)."""
        Q_crit = 9 * alpha**2 / (8 * kappa)
        coeffs = compute_single_line_tower(kappa, alpha, Q_crit, r)
        assert simplify(coeffs[r]) == 0, f"S_{r} nonzero at Delta=0"


class TestEvenArityCascade:
    """alpha = 0, Q != 0: even pump, odd vanishing."""

    def test_odd_arities_vanish(self):
        odd_zero, _, _ = verify_even_cascade(14)
        assert odd_zero, "Some odd-arity shadow nonzero with alpha=0"

    def test_even_arities_nonzero(self):
        _, even_nz, _ = verify_even_cascade(14)
        assert even_nz, "Some even-arity shadow zero with alpha=0, Q!=0"

    def test_s6_explicit(self):
        """S_6 = -4*Q^2/(3*kappa) when alpha=0."""
        Q_sym_nz = Symbol('Q', nonzero=True)
        coeffs = compute_single_line_tower(kappa, S.Zero, Q_sym_nz, 6)
        expected = -4 * Q_sym_nz**2 / (3 * kappa)
        assert simplify(coeffs[6] - expected) == 0

    def test_s8_explicit(self):
        """S_8 = 4*Q^3/kappa^2 when alpha=0."""
        Q_sym_nz = Symbol('Q', nonzero=True)
        coeffs = compute_single_line_tower(kappa, S.Zero, Q_sym_nz, 8)
        expected = 4 * Q_sym_nz**3 / kappa**2
        assert simplify(coeffs[8] - expected) == 0


class TestVirasoroRecovery:
    """Recover Virasoro tower from alpha=2, kappa=c/2.

    Convention: Sh_2 = kappa * x^2 = (c/2) * x^2.
    The Virasoro cubic: Sh_3 = 2 * x^3 (alpha = 2).
    The quartic S_4 = 10/[c(5c+22)] includes the
    cubic-derived part and the direct contact contribution Q_Vir.
    """

    def test_virasoro_recover_from_virasoro_code(self):
        """Match the Virasoro code.

        Convention: Sh_2 = (kappa/2)*x^2 = (c/2)*x^2, so kappa=c.
        Virasoro has alpha=2, and Q_Vir is derived from the known S_4.
        """
        from compute.lib.virasoro_shadow_tower import shadow_coefficients
        vir_coeffs = shadow_coefficients(7)

        # kappa = c in our convention (Sh_2 = (c/2)*x^2)
        kappa_vir = c
        S4_derived = -9 * 4 / (8 * kappa_vir)  # = -9/(2c)
        Q_vir = simplify(vir_coeffs[4] - S4_derived)

        coeffs = compute_single_line_tower(kappa_vir, 2, Q_vir, 7)
        for r in range(4, 8):
            diff_r = simplify(coeffs[r] - vir_coeffs[r])
            assert diff_r == 0, (
                f"S_{r} mismatch: got {coeffs[r]}, "
                f"expected {vir_coeffs[r]}, diff={diff_r}"
            )

    def test_virasoro_delta_nonzero(self):
        """Virasoro has Delta != 0, confirming class M."""
        kappa_vir = c
        S4_derived = -9 * 4 / (8 * kappa_vir)
        Q_vir = Rational(10) / (c * (5 * c + 22)) - S4_derived
        Delta_vir = simplify(8 * Q_vir * kappa_vir - 9 * 4)
        assert Delta_vir != 0


class TestGaussianClass:
    """alpha = 0, Q = 0: tower terminates at arity 2."""

    def test_all_vanish(self):
        coeffs = compute_single_line_tower(kappa, S.Zero, S.Zero, 10)
        for r in range(3, 11):
            assert coeffs[r] == 0, f"S_{r} nonzero in Gaussian case"


class TestNoIntermediateDepth:
    """No 4 <= r_max < infinity on a single line."""

    @pytest.mark.parametrize("alpha_val,Q_val", [
        (1, 1),
        (1, 0),
        (0, 1),
        (3, 2),
        (Rational(1, 2), Rational(1, 3)),
    ])
    def test_no_finite_termination_above_3(self, alpha_val, Q_val):
        """If tower doesn't terminate at 3, it doesn't terminate at all."""
        kappa_val = Rational(1)
        Delta_val = 8 * Q_val * kappa_val - 9 * alpha_val**2
        coeffs = compute_single_line_tower(
            kappa_val, alpha_val, Q_val, 10
        )

        if Delta_val == 0:
            # Class L: terminates at 3
            for r in range(4, 11):
                assert coeffs[r] == 0
        elif alpha_val == 0 and Q_val == 0:
            # Class G: terminates at 2
            for r in range(3, 11):
                assert coeffs[r] == 0
        else:
            # Must have infinitely many nonzero: check through 10
            nonzero_count = sum(
                1 for r in range(4, 11) if coeffs[r] != 0
            )
            assert nonzero_count >= 3, (
                f"Too few nonzero shadows for alpha={alpha_val}, "
                f"Q={Q_val}: expected infinite tower"
            )
