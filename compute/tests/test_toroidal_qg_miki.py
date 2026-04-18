"""Audited Vol I tests for the toroidal formal-disk DIM surface.

These tests are intentionally scoped to what is locally verified in Vol I:

- the DIM parameter convention q_1 = q, q_2 = t^{-1}, q_3 = t/q;
- the cyclic parameter action attached to the Miki symmetry at the level of
  the scalar structure function;
- the current-exchange kernel G(w/z) for the formal-disk currents;
- the degeneration at t = q, where the standard DIM convention collapses to
  q_3 = 1 and G(x) = 1;
- the additive/rational classical limit prod_i (u + h_i)/(u - h_i).

The tests do NOT claim a full 2 x 2 RTT/FRT matrix presentation for
U_{q,t}(ddot sl_2).  They verify the current-level surface that is actually
encoded by the DIM structure function and use that surface to falsify two
overstrong folklore phrases:

1. "t = q gives the elliptic Hall algebra" in the standard DIM convention;
2. "(q,t) -> (1,1) yields a proved Yangian x Yangian factorization."
"""

from sympy import Rational, Symbol, simplify, symbols

from compute.lib.toroidal_qg_miki import (
    classical_limit_denominator,
    classical_limit_factor,
    classical_limit_from_multiplicative,
    classical_limit_structure_function,
    current_exchange_factor,
    dim_parameters,
    miki_orbit,
    structure_function,
    t_equals_q_degeneracy,
)


def test_dim_convention_satisfies_cy_condition():
    q, t = symbols("q t", nonzero=True)
    params = dim_parameters(q, t)
    assert simplify(params.q1 * params.q2 * params.q3 - 1) == 0
    assert simplify(params.q1 - q) == 0
    assert simplify(params.q2 - 1 / t) == 0
    assert simplify(params.q3 - t / q) == 0


def test_current_exchange_factor_uses_two_spectral_variables():
    q = Symbol("q", nonzero=True)
    t = Symbol("t", nonzero=True)
    z = Symbol("z", nonzero=True)
    w = Symbol("w", nonzero=True)
    factor = current_exchange_factor(z, w, q, t)
    assert simplify(factor - structure_function(w / z, q=q, t=t)) == 0


def test_miki_parameter_cycle_has_order_three():
    q = Symbol("q", nonzero=True)
    t = Symbol("t", nonzero=True)
    orbit = miki_orbit(q, t, length=3)
    assert simplify(orbit[3].q - q) == 0
    assert simplify(orbit[3].t - t) == 0


def test_structure_function_is_invariant_under_miki_cycle():
    q = Symbol("q", nonzero=True)
    t = Symbol("t", nonzero=True)
    x = Symbol("x", nonzero=True)
    orbit = miki_orbit(q, t, length=1)
    g0 = structure_function(x, q=q, t=t)
    g1 = structure_function(x, q=orbit[1].q, t=orbit[1].t)
    assert simplify(g0 - g1) == 0


def test_t_equals_q_degenerates_structure_function_to_one():
    q = Symbol("q", nonzero=True)
    x = Symbol("x", nonzero=True)
    # VERIFIED [DC] direct substitution in the DIM triple;
    #           [LC] q_3 = 1 boundary specialization;
    #           [CF] matches the existing Vol III convention q_1=q, q_2=t^{-1}, q_3=t/q.
    assert simplify(t_equals_q_degeneracy(q, x) - 1) == 0


def test_t_equals_q_is_not_a_nontrivial_formal_disk_specialization():
    q = Symbol("q", nonzero=True)
    params = dim_parameters(q, q)
    assert simplify(params.q3 - 1) == 0


def test_single_factor_classical_limit():
    u, h, eps = symbols("u h eps")
    factor_limit = classical_limit_factor(u, h, h, eps)
    assert simplify(factor_limit - (u + h) / (u - h)) == 0


def test_full_classical_limit_matches_rational_toroidal_formula():
    u, h1, h2, eps = symbols("u h1 h2 eps")
    direct_limit = classical_limit_from_multiplicative(u, h1, h2, eps)
    expected = classical_limit_structure_function(u, h1, h2)
    # VERIFIED [DC] direct multiplicative->additive limit;
    #           [LC] reproduces the single-factor limit termwise;
    #           [LT] this is the standard affine-Yangian/toroidal rational kernel.
    assert simplify(direct_limit - expected) == 0


def test_classical_limit_retains_three_additive_directions_generically():
    u, h1, h2 = symbols("u h1 h2")
    denom = classical_limit_denominator(u, h1, h2)
    h3 = simplify(-h1 - h2)
    assert simplify(denom - (u - h1) * (u - h2) * (u - h3)) == 0


def test_numeric_miki_orbit_and_classical_limit_examples():
    orbit = miki_orbit(2, 3, length=3)
    assert orbit[1].q == Rational(1, 3)
    assert orbit[1].t == Rational(2, 3)
    assert orbit[2].q == Rational(3, 2)
    assert orbit[2].t == Rational(1, 2)
    assert orbit[3].q == Rational(2, 1)
    assert orbit[3].t == Rational(3, 1)

    eps = Symbol("eps")
    numeric_limit = classical_limit_from_multiplicative(Symbol("u"), 1, -2, eps)
    expected = classical_limit_structure_function(Symbol("u"), 1, -2)
    assert simplify(numeric_limit - expected) == 0
