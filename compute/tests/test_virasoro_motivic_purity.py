"""Exact algebraic checks for the formal Virasoro Riccati series.

The coefficients tested here are ``R_r(c)`` defined by
``t^2 sqrt(Q_L(t)) = sum r R_r(c) t^r``.  Rationality of these formal
coefficients is an algebraic statement in ``Q(c)[[t]]``.  The Ward engine
produces the canonical coordinate functions ``G_r`` and ``G_r^conn``.
An ordered scalar ``S_r(Vir_c; H_res)`` additionally uses an Arnold class
and a normalized residue projection.
"""

from __future__ import annotations

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.shadow_tower_higher_vir import (
    s5_riccati_candidate,
    s6_relation_candidate,
    s6_riccati_candidate,
)
from compute.lib.virasoro_ward_correlators import (
    ResidueProjectionRequired,
    require_residue_projection,
    standard_points,
    virasoro_connected_correlator,
)


# ---------------------------------------------------------------------------
# Local seeds and simplified weighted-Riccati formulas.
# ---------------------------------------------------------------------------


def _s2_vir(c):
    """S_2(Vir_c) = kappa_ch(Vir_c) = c/2 by definition (landscape_census)."""
    return sp.Rational(1, 2) * c


def _s3_vir():
    """Return the local three-point normalization ``R_3=2``."""
    return sp.Integer(2)


def _s4_vir_shapovalov(c):
    """The seed ``R_4=10/[c(5c+22)]`` from the Lambda norm.

    Here ``<Lambda|Lambda>=c(5c+22)/10``.
    This is the level-four seed supplied to the Riccati series."""
    return sp.Rational(10) / (c * (5 * c + 22))


def _s5_riccati_closed_form(c):
    """Return the simplified arity-five coefficient of ``H_Ricc``."""

    return s5_riccati_candidate(c)


def _s6_riccati_closed_form(c):
    """Return the simplified arity-six coefficient of ``H_Ricc``."""

    return s6_riccati_candidate(c)


def _s7_vir_closed_form(c):
    """S_7(Vir_c) = -2880(15c+61)/[7 c^4 (5c+22)^2]."""
    return sp.Rational(-2880) * (15 * c + 61) / (sp.Integer(7) * c**4 * (5 * c + 22) ** 2)


def _s8_vir_closed_form(c):
    """S_8(Vir_c) = 80(2025c^2 + 16470c + 33314)/[c^5(5c+22)^3]."""
    num = 2025 * c**2 + 16470 * c + 33314
    return sp.Rational(80) * num / (c**5 * (5 * c + 22) ** 3)


def _riccati_Q(c):
    """Q(t) = 4 kappa^2 + 12 kappa S_3 t + (9 S_3^2 + 16 kappa S_4) t^2
    for Virasoro; t symbol supplied externally."""
    kappa = _s2_vir(c)
    S3 = _s3_vir()
    S4 = _s4_vir_shapovalov(c)
    t = sp.Symbol("t")
    return 4 * kappa**2 + 12 * kappa * S3 * t + (9 * S3**2 + 16 * kappa * S4) * t**2


def _truncate_poly_in_t(expr, t, deg_max):
    """Drop every t^k with k > deg_max. Keeps rational-function c
    coefficients intact."""
    p = sp.Poly(expr, t)
    return sum(p.nth(k) * t**k for k in range(0, deg_max + 1))


def _riccati_H_expansion(c, r_max):
    """Expand H(t) = t^2 sqrt(Q(t)) to order t^{r_max} in Q(c)[[t]].
    The binomial series implements coefficient extraction from the defining
    square root.

    Implementation: sp.series(sp.sqrt(.)) with rational-function c
    coefficients is pathologically slow at order >= 9, so we factor
    sqrt(Q) = (2 kappa) sqrt(1 + u), u = P(t)/(2 kappa)^2 = P(t)/c^2,
    and apply the binomial expansion sqrt(1 + u) = sum_n binom(1/2, n)
    u^n. Since u has t-valuation 1, only n <= r_max - 2 contributes.
    """
    t = sp.Symbol("t")
    kappa = sp.Rational(1, 2) * c  # 2*kappa = c
    S3 = sp.Integer(2)
    S4 = _s4_vir_shapovalov(c)
    two_kappa_sq = (2 * kappa) ** 2  # = c^2
    u = sp.together(
        (12 * kappa * S3 * t + (9 * S3**2 + 16 * kappa * S4) * t**2) / two_kappa_sq
    )
    n_max = r_max - 2
    one_half = sp.Rational(1, 2)
    binomial_series = sp.Integer(0)
    u_power = sp.Integer(1)
    for n in range(0, n_max + 1):
        coeff = sp.binomial(one_half, n)
        binomial_series += coeff * u_power
        if n < n_max:
            u_power = _truncate_poly_in_t(sp.expand(u_power * u), t, n_max)
    sqrt_Q = (2 * kappa) * binomial_series
    H = sp.expand(t**2 * sqrt_Q)
    return _truncate_poly_in_t(H, t, r_max)


def _extract_S_r_from_riccati(c, r):
    """Return ``R_r(c)=(1/r)[t^r]H_Ricc(t)``."""
    t = sp.Symbol("t")
    H = _riccati_H_expansion(c, r + 1)
    coeff = sp.Poly(H, t).nth(r)
    return sp.together(coeff / r)


# ---------------------------------------------------------------------------
# Tests for thm:virasoro-motivic-purity
# ---------------------------------------------------------------------------


def test_s2_s3_s4_virasoro_all_rational():
    """Base case: first three invariants are rational at c=1,2,13,25."""
    c = sp.Symbol("c")
    assert _s2_vir(c).free_symbols == {c}
    assert _s3_vir().is_rational is True
    # S_4(Vir_c) is a rational function of c with denominator c(5c+22).
    S4 = _s4_vir_shapovalov(c)
    num, den = sp.fraction(sp.together(S4))
    # Denominator must be c(5c+22) up to a scalar.
    assert sp.simplify(den - c * (5 * c + 22)) == 0
    # Numerator is a pure rational constant.
    assert sp.Poly(num, c).is_ground


def test_riccati_matches_closed_forms_r4_through_r8():
    """Coefficient extraction agrees with the simplified ``R_r(c)`` forms."""

    c = sp.Symbol("c")
    expected = {
        4: _s4_vir_shapovalov(c),
        5: _s5_riccati_closed_form(c),
        6: _s6_riccati_closed_form(c),
        7: _s7_vir_closed_form(c),
        8: _s8_vir_closed_form(c),
    }
    for r, ref in expected.items():
        S_r = _extract_S_r_from_riccati(c, r)
        diff = sp.simplify(S_r - ref)
        assert diff == 0, (
            f"Riccati expansion and closed form disagree at r={r}: "
            f"diff = {diff}"
        )


def test_connected_ward_functions_precede_scalar_extraction():
    """The Ward and residue constructions expose their respective types."""

    for arity in (5, 6):
        points = standard_points(arity)
        connected = virasoro_connected_correlator(points, sp.Symbol("c"))
        assert connected.free_symbols == set(points) | {sp.Symbol("c")}
        with pytest.raises(ResidueProjectionRequired):
            require_residue_projection(arity)


def test_weight_six_relation_and_riccati_constructions_are_distinct():
    """The formal relation and weighted-Riccati rules give distinct outputs."""

    c = sp.Symbol("c")
    riccati = s6_riccati_candidate(c)
    relation = s6_relation_candidate(c)
    expected_difference = -sp.Rational(4) * (180 * c + 767) / (
        3 * c**3 * (5 * c + 22) ** 2
    )
    assert sp.factor(relation - riccati - expected_difference) == 0

    r2 = c / 2
    r3 = sp.Integer(2)
    r4 = sp.Rational(10) / (c * (5 * c + 22))
    r5 = s5_riccati_candidate(c)
    assert sp.factor(2 * r2 * relation + 2 * r3 * r5 + r4**2) == 0
    assert sp.factor(_extract_S_r_from_riccati(c, 6) - riccati) == 0


def test_riccati_coefficients_are_rational_functions_of_c():
    """Every Taylor coefficient of ``H_Ricc(t)`` lies in
    Q(c) -- the field of rational functions. Verified by sympy's
    is_rational_function predicate."""
    c = sp.Symbol("c")
    for r in range(4, 9):
        S_r = _extract_S_r_from_riccati(c, r)
        assert S_r.is_rational_function(c), (
            f"R_{r}(c) left Q(c): {S_r}"
        )


def test_master_equation_preserves_rationality():
    """At c=1: direct substitution gives rational numerics. At c symbolic:
    sympy verifies rational-function predicate. Test across 4 values."""
    for c_val in (sp.Integer(1), sp.Rational(1, 2), sp.Integer(13), sp.Integer(25)):
        for r in range(4, 9):
            S_r = _extract_S_r_from_riccati(c_val, r)
            # At numeric c, result must be a pure rational number.
            assert S_r.is_rational, (
                f"R_{r}({c_val}) left Q: {S_r}"
            )


# ---------------------------------------------------------------------------
# Tests for prop:denominator-structure
# ---------------------------------------------------------------------------


def test_denominator_bound_r4_through_r8():
    """The denominator of ``R_r(c)`` divides the stated polynomial bound."""
    import math

    c = sp.Symbol("c")
    closed_forms = {
        4: _s4_vir_shapovalov(c),
        5: _s5_riccati_closed_form(c),
        6: _s6_riccati_closed_form(c),
        7: _s7_vir_closed_form(c),
        8: _s8_vir_closed_form(c),
    }
    for r, expr in closed_forms.items():
        num, den = sp.fraction(sp.together(expr))
        den_poly = sp.Poly(den, c)
        # Expected bound.
        expected_c_power = max(0, r - 3)
        expected_factor_power = math.ceil((r - 2) / 2)
        # Check den divides c^{expected_c_power} * (5c+22)^{expected_factor_power}.
        bound = (c ** expected_c_power) * ((5 * c + 22) ** expected_factor_power)
        bound_poly = sp.Poly(sp.expand(bound), c)
        # Denominator polynomial should divide the bound polynomial.
        quot, rem = sp.div(bound_poly, den_poly, c)
        assert sp.simplify(rem.as_expr()) == 0, (
            f"Denominator of S_{r} does not divide D_{r}: "
            f"den = {den}, bound = {bound}"
        )


def test_only_two_irreducible_factors_in_denominator():
    """No new irreducible factor (7c+68, c+1, c+2, ...) ever enters."""
    c = sp.Symbol("c")
    closed_forms = {
        4: _s4_vir_shapovalov(c),
        5: _s5_riccati_closed_form(c),
        6: _s6_riccati_closed_form(c),
        7: _s7_vir_closed_form(c),
        8: _s8_vir_closed_form(c),
    }
    allowed_factors = {c, 5 * c + 22}
    for r, expr in closed_forms.items():
        _, den = sp.fraction(sp.together(expr))
        den_factored = sp.factor(den)
        # Extract the irreducible factors.
        if isinstance(den_factored, sp.Mul):
            factors = den_factored.args
        else:
            factors = (den_factored,)
        for f in factors:
            # Unwrap Pow.
            base = f.base if isinstance(f, sp.Pow) else f
            # Ignore pure rational scalars.
            if base.is_rational:
                continue
            # Check membership in allowed factors.
            is_allowed = any(
                sp.simplify(base - a) == 0 for a in allowed_factors
            )
            assert is_allowed, (
                f"S_{r} denominator contains unexpected irreducible factor "
                f"{base} (full denominator: {den_factored})"
            )


# ---------------------------------------------------------------------------
# Tests for thm:virasoro-riccati-transport-rationality
# ---------------------------------------------------------------------------


def test_transport_output_is_formal_power_series_in_Qc():
    """Riccati transport output is a formal power series with Q(c)
    coefficients."""
    c = sp.Symbol("c")
    H = _riccati_H_expansion(c, 9)
    for r in range(2, 9):
        coeff = sp.Poly(H, sp.Symbol("t")).nth(r)
        # Check coeff is rational in c (finite combination via is_rational_function).
        assert sp.simplify(coeff).is_rational_function(c), (
            f"H(t) coefficient at t^{r} is not in Q(c): {coeff}"
        )


# ---------------------------------------------------------------------------
# Rational specializations of the formal series
# ---------------------------------------------------------------------------


def test_rational_specializations_of_weighted_riccati_series():
    """At rational ``c``, each displayed weighted-Riccati output is rational."""
    for c_val in (
        Fraction(1),
        Fraction(1, 2),
        Fraction(13),
        Fraction(25),
        Fraction(26),
    ):
        c_sp = sp.Rational(c_val.numerator, c_val.denominator)
        for r in (4, 5, 6, 7, 8):
            S_r = _extract_S_r_from_riccati(c_sp, r)
            assert S_r.is_rational, (
                f"R_{r}({c_val}) left Q: {S_r}"
            )


# ---------------------------------------------------------------------------
# Rational substitution along the principal W_3 central-charge family
# ---------------------------------------------------------------------------


def test_weighted_riccati_series_under_W3_central_charge_substitution():
    """A rational central-charge substitution preserves ``Q``-rationality."""
    k = sp.Symbol("k")
    # c(V_k(sl_3)) = k * dim(sl_3) / (k + h^v) = 8 k / (k + 3).
    c_affine = sp.Rational(8) * k / (k + 3)
    # DS shift: c(W_3) = c_affine - 12 |rho|^2 / (k + h^v); rho.rho = 4 for sl_3.
    # We use the universal W_3 central charge formula directly
    # (Fateev-Lukyanov 1988) c(W_3) = 50 - 24/(k+3) - 24(k+3).
    c_w3 = sp.Integer(50) - sp.Rational(24) / (k + 3) - sp.Rational(24) * (k + 3)
    # Substitute k = 4: c(W_3) at k=4.
    c_val = c_w3.subs(k, 4)
    for r in (4, 5, 6, 7, 8):
        S_r = _extract_S_r_from_riccati(c_val, r)
        assert S_r.is_rational, (
            f"R_{r}(c(W_3,4)) left Q at c={c_val}: {S_r}"
        )
