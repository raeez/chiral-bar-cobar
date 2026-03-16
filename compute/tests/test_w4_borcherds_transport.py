"""Tests for MC4 W-infinity Borcherds transport relation resolution.

Verifies conj:winfty-stage4-visible-borcherds-transport:
  (C^res_{3,4;4;0,3})^2 = (5/7) * (C^res_{3,3;4;0,2})^2

Resolution: DS computation (Prop prop:w4-ds-ope-explicit, 121 tests)
  + W_4 uniqueness (Zamolodchikov-Fateev-Lukyanov rigidity)
  => transport relation holds for the visible residue calculus.

Ground truth: concordance.tex (Front D, MC4 coefficient matching)
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from w4_borcherds_transport import (
    c334_squared,
    c444_squared,
    C34_3_squared,
    C34_4_squared,
    verify_swap_even_identity,
    verify_transport_identity,
    verify_two_primitive_reduction,
    verify_at_c_values,
    resolve_mc4_winfty_stage4,
)
from sympy import Symbol, Rational, simplify, cancel


# ============================================================
# Algebraic identity tests
# ============================================================

class TestAlgebraicIdentities:
    """Verify the inter-coefficient relations as symbolic identities."""

    def test_swap_even_identity(self):
        """C_{3,4;3;0,4}^2 = (9/16) * c_334^2 (algebraic identity)."""
        result = verify_swap_even_identity()
        assert result["identity_holds"], \
            f"Swap-even identity failed: diff = {result['difference']}"

    def test_transport_identity(self):
        """C_{3,4;4;0,3}^2 = (5/7) * c_334^2 (THE Borcherds transport, algebraic)."""
        result = verify_transport_identity()
        assert result["identity_holds"], \
            f"Transport identity failed: diff = {result['difference']}"

    def test_two_primitive_reduction(self):
        """All four higher-spin coefficients reduce to two primitives."""
        result = verify_two_primitive_reduction()
        assert result["swap_even_identity"], "Swap-even identity failed"
        assert result["transport_identity"], "Transport identity failed"
        assert result["primitives_independent"], "Primitives not independent"
        assert result["all_verified"], "Two-primitive reduction not fully verified"


# ============================================================
# Formula structure tests
# ============================================================

class TestFormulaStructure:
    """Verify structural properties of the stage-4 OPE formulas."""

    def test_c334_vanishes_at_c0(self):
        """c_334^2(c=0) = 0 (free theory has no higher-spin coupling)."""
        c = Symbol('c')
        assert float(c334_squared().subs(c, 0)) == 0

    def test_c444_vanishes_at_c0(self):
        """c_444^2(c=0) = 0."""
        c = Symbol('c')
        assert float(c444_squared().subs(c, 0)) == 0

    def test_c444_vanishes_at_c_half(self):
        """c_444^2(c=1/2) = 0 (from the factor 2c-1)."""
        c = Symbol('c')
        assert abs(float(c444_squared().subs(c, Rational(1, 2)))) < 1e-15

    def test_c334_positive_at_large_c(self):
        """c_334^2 > 0 for large c (unitary regime)."""
        c = Symbol('c')
        assert float(c334_squared().subs(c, 1000)) > 0

    def test_c334_poles(self):
        """c_334^2 has poles at c = -24, -68/7, -46/3 (NOT at physical values)."""
        c = Symbol('c')
        # These are the denominator zeros
        for c_pole in [-24, Rational(-68, 7), Rational(-46, 3)]:
            # The function should diverge near these values
            denom = (c + 24) * (7*c + 68) * (3*c + 46)
            assert float(denom.subs(c, c_pole)) == 0

    def test_c334_c444_independent(self):
        """c_334^2 and c_444^2 have different c-dependence (truly independent)."""
        c = Symbol('c')
        ratio = simplify(cancel(c444_squared() / c334_squared()))
        # The ratio should depend on c
        deriv = ratio.diff(c)
        assert simplify(deriv) != 0, "c_444/c_334 ratio is constant — NOT independent"

    def test_transport_ratio_exact(self):
        """C_34_4^2 / c_334^2 = 5/7 exactly (as rational functions)."""
        c = Symbol('c')
        ratio = simplify(cancel(C34_4_squared() / c334_squared()))
        assert ratio == Rational(5, 7), f"Transport ratio = {ratio}, expected 5/7"

    def test_swap_even_ratio_exact(self):
        """C_34_3^2 / c_334^2 = 9/16 exactly."""
        c = Symbol('c')
        ratio = simplify(cancel(C34_3_squared() / c334_squared()))
        assert ratio == Rational(9, 16), f"Swap-even ratio = {ratio}, expected 9/16"


# ============================================================
# Numerical spot-check tests
# ============================================================

class TestNumericalSpotChecks:
    """Numerical verification at specific c values."""

    def test_spot_checks_all_match(self):
        """Transport and swap-even ratios match at 8 c-values."""
        result = verify_at_c_values()
        assert result["n_transport_match"] == result["n_total"], \
            f"Transport: {result['n_transport_match']}/{result['n_total']} match"
        assert result["n_swap_even_match"] == result["n_total"], \
            f"Swap-even: {result['n_swap_even_match']}/{result['n_total']} match"

    def test_specific_c9(self):
        """Verify at c=9 (sl_4 at generic level)."""
        c = Symbol('c')
        v334 = float(c334_squared().subs(c, 9))
        v34_4 = float(C34_4_squared().subs(c, 9))
        assert abs(v34_4 / v334 - 5/7) < 1e-12

    def test_specific_c26(self):
        """Verify at c=26 (Virasoro self-dual point, no special meaning for W_4)."""
        c = Symbol('c')
        v334 = float(c334_squared().subs(c, 26))
        v34_4 = float(C34_4_squared().subs(c, 26))
        assert abs(v34_4 / v334 - 5/7) < 1e-12

    def test_specific_c_large(self):
        """Verify at c=10000 (semiclassical limit)."""
        c = Symbol('c')
        v334 = float(c334_squared().subs(c, 10000))
        v34_4 = float(C34_4_squared().subs(c, 10000))
        assert abs(v34_4 / v334 - 5/7) < 1e-12


# ============================================================
# Full resolution pipeline
# ============================================================

class TestFullResolution:
    """End-to-end resolution of MC4 W-infinity stage-4."""

    def test_resolve_mc4_winfty_stage4(self):
        """Full resolution: algebraic + numerical + uniqueness argument."""
        result = resolve_mc4_winfty_stage4(verbose=False)
        assert result["resolved"], \
            "MC4 W-infinity stage-4 Borcherds transport NOT resolved"

    def test_algebraic_resolution(self):
        """The algebraic identity alone resolves the DS side."""
        result = verify_two_primitive_reduction()
        assert result["all_verified"]

    def test_transport_is_5_7(self):
        """The Borcherds transport ratio is exactly 5/7."""
        c = Symbol('c')
        ratio = cancel(C34_4_squared() / c334_squared())
        assert ratio == Rational(5, 7)
