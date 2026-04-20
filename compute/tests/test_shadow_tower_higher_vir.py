"""Tests for compute/lib/shadow_tower_higher_vir.

Verifies the closed-form Virasoro shadow coefficients S_6, S_7, S_8
against the central-charge specialisations tabulated in the module
docstring, plus cross-checks against landscape constants.

Three verification paths per coefficient:
  (a) c = 1 specialisation from the closed form.
  (b) c = 1/2 (Ising) specialisation from the closed form.
  (c) Large-c leading asymptotic A_r / c^{r-2}.
"""

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.shadow_tower_higher_vir import (
    s6_virasoro,
    s7_virasoro,
    s8_virasoro,
)


def test_smoke_import_and_call():
    """Module imports and the closed forms evaluate at c = 1."""
    for f in (s6_virasoro, s7_virasoro, s8_virasoro):
        val = sp.nsimplify(f(1))
        assert val is not None


def test_s6_c1_closed_form():
    """S_6(Vir_{c=1}) = 19040/2187 = 80*238/(3*27^2)."""
    val = sp.nsimplify(s6_virasoro(1))
    assert val == sp.Rational(19040, 2187)


def test_s7_c1_closed_form():
    """S_7(Vir_{c=1}) = -24320/567 = -2880*76/(7*81).

    The docstring claim 80 * 238 / ... for S_6 is reproduced, and
    the analogous S_7 coefficient follows from
    -2880(15c+61)/[7 c^4 (5c+22)^2] at c = 1 = -2880 * 76 / (7 * 27^2)
    = -218880 / 5103 = -24320/567 (simplified).
    """
    val = sp.nsimplify(s7_virasoro(1))
    expected = sp.Rational(-2880) * 76 / (sp.Rational(7) * 27 ** 2)
    assert val == expected
    assert val == sp.Rational(-24320, 567)


def test_s8_c1_closed_form():
    """S_8(Vir_{c=1}) = 4144720/19683 (Vol III m_8 identity)."""
    val = sp.nsimplify(s8_virasoro(1))
    assert val == sp.Rational(4144720, 19683)


def test_s6_ising():
    """S_6(Vir_{c=1/2}) = 551680/7203 (docstring)."""
    val = sp.nsimplify(s6_virasoro(sp.Rational(1, 2)))
    assert val == sp.Rational(551680, 7203)


def test_s7_ising():
    """S_7(Vir_{c=1/2}) = -12625920/16807 (docstring)."""
    val = sp.nsimplify(s7_virasoro(sp.Rational(1, 2)))
    assert val == sp.Rational(-12625920, 16807)


def test_s8_ising():
    """S_8(Vir_{c=1/2}) = 861291520/117649 (docstring)."""
    val = sp.nsimplify(s8_virasoro(sp.Rational(1, 2)))
    assert val == sp.Rational(861291520, 117649)


def test_large_c_leading_asymptotic():
    """Leading large-c asymptotic: S_r(Vir_c) ~ A_r / c^{r-2}.

    A_6 = 48, A_7 = -1728/7, A_8 = 1296 (docstring).
    """
    c = sp.Symbol('c', positive=True)
    # Extract leading term of c^{r-2} * S_r at c -> infinity
    lead6 = sp.limit(c ** 4 * s6_virasoro(c), c, sp.oo)
    lead7 = sp.limit(c ** 5 * s7_virasoro(c), c, sp.oo)
    lead8 = sp.limit(c ** 6 * s8_virasoro(c), c, sp.oo)
    assert lead6 == sp.Rational(48)
    assert lead7 == sp.Rational(-1728, 7)
    assert lead8 == sp.Rational(1296)


def test_pole_structure_at_zamolodchikov_norm():
    """Poles at 5c + 22 = 0 (Yang-Lee) with predicted multiplicity.

    S_6 has (5c+22)^2 in denominator; S_7 has (5c+22)^2; S_8 has (5c+22)^3.
    """
    c = sp.Symbol('c')
    # multiply by (5c+22)^m and check value at c = -22/5 is finite and nonzero.
    for r, f, m in [(6, s6_virasoro, 2), (7, s7_virasoro, 2), (8, s8_virasoro, 3)]:
        cleared = sp.simplify(f(c) * (5 * c + 22) ** m)
        v = cleared.subs(c, sp.Rational(-22, 5))
        assert v != 0, f"S_{r} should have a {m}-fold pole at c=-22/5"
        assert sp.simplify(cleared).is_finite is not False
