"""Tests for the formal Virasoro weighted-Riccati and relation outputs.

Verifies the weighted-Riccati coefficients ``R_6``, ``R_7``, ``R_8``
and the distinct formal weight-six relation candidate against exact
central-charge specializations.

Three verification paths per coefficient:
  (a) c = 1 specialisation from the closed form.
  (b) c = 1/2 (Ising) specialisation from the closed form.
  (c) Large-c leading asymptotic A_r / c^{r-2}.
"""

import sympy as sp

from compute.lib.shadow_tower_higher_vir import (
    WEIGHT_SIX_RELATION_SEMANTICS,
    WEIGHT_SIX_RELATION_VALUES,
    s5_riccati_candidate,
    s6_null_candidate,
    s6_relation_candidate,
    s6_riccati_candidate,
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
    """The weighted-Riccati value is ``R_6(1)=19040/2187``."""
    val = sp.nsimplify(s6_virasoro(1))
    assert val == sp.Rational(19040, 2187)


def test_s7_c1_closed_form():
    """The weighted-Riccati value is ``R_7(1)=-24320/567``.

    The value of ``R_6`` is reproduced, and the analogous ``R_7``
    coefficient follows from
    -2880(15c+61)/[7 c^4 (5c+22)^2] at c = 1 = -2880 * 76 / (7 * 27^2)
    = -218880 / 5103 = -24320/567 (simplified).
    """
    val = sp.nsimplify(s7_virasoro(1))
    expected = sp.Rational(-2880) * 76 / (sp.Rational(7) * 27 ** 2)
    assert val == expected
    assert val == sp.Rational(-24320, 567)


def test_s8_c1_closed_form():
    """The weighted-Riccati value is ``R_8(1)=4144720/19683``."""
    val = sp.nsimplify(s8_virasoro(1))
    assert val == sp.Rational(4144720, 19683)


def test_s6_ising():
    """The weighted-Riccati value is ``R_6(1/2)=551680/7203``."""
    val = sp.nsimplify(s6_virasoro(sp.Rational(1, 2)))
    assert val == sp.Rational(551680, 7203)


def test_s7_ising():
    """The weighted-Riccati value is ``R_7(1/2)=-12625920/16807``."""
    val = sp.nsimplify(s7_virasoro(sp.Rational(1, 2)))
    assert val == sp.Rational(-12625920, 16807)


def test_s8_ising():
    """The weighted-Riccati value is ``R_8(1/2)=861291520/117649``."""
    val = sp.nsimplify(s8_virasoro(sp.Rational(1, 2)))
    assert val == sp.Rational(861291520, 117649)


def test_large_c_leading_asymptotic():
    """Leading large-c asymptotic: ``R_r(c) ~ A_r/c^(r-2)``.

    A_6 = 48, A_7 = -1728/7, A_8 = 1296 (docstring).
    """
    c = sp.Symbol('c', positive=True)
    # Extract the leading term of c^{r-2} R_r as c tends to infinity.
    lead6 = sp.limit(c ** 4 * s6_virasoro(c), c, sp.oo)
    lead7 = sp.limit(c ** 5 * s7_virasoro(c), c, sp.oo)
    lead8 = sp.limit(c ** 6 * s8_virasoro(c), c, sp.oo)
    assert lead6 == sp.Rational(48)
    assert lead7 == sp.Rational(-1728, 7)
    assert lead8 == sp.Rational(1296)


def test_pole_structure_at_zamolodchikov_norm():
    """Poles at 5c + 22 = 0 (Yang-Lee) with predicted multiplicity.

    ``R_6`` and ``R_7`` have a square factor; ``R_8`` has a cube.
    """
    c = sp.Symbol('c')
    # multiply by (5c+22)^m and check value at c = -22/5 is finite and nonzero.
    for r, f, m in [(6, s6_virasoro, 2), (7, s7_virasoro, 2), (8, s8_virasoro, 3)]:
        cleared = sp.simplify(f(c) * (5 * c + 22) ** m)
        v = cleared.subs(c, sp.Rational(-22, 5))
        assert v != 0, f"R_{r} has a {m}-fold pole at c=-22/5"
        assert sp.simplify(cleared).is_finite is not False


def test_weight_six_relation_candidate_is_the_unique_formal_solution():
    """Direct solution of the defining relation recovers ``C_6^rel``."""

    c = sp.Symbol("c")
    candidate = sp.Symbol("candidate")
    r2 = c / 2
    r3 = sp.Integer(2)
    r4 = sp.Rational(10) / (c * (5 * c + 22))
    r5 = s5_riccati_candidate(c)
    equation = 2 * r2 * candidate + 2 * r3 * r5 + r4**2
    solved = sp.solve(sp.Eq(equation, 0), candidate)

    assert len(solved) == 1
    relation = s6_relation_candidate(c)
    assert sp.factor(solved[0] - relation) == 0
    assert sp.factor(equation.subs(candidate, relation)) == 0


def test_weight_six_relation_values_and_large_c_distinguish_riccati():
    """Regular specializations and asymptotics separate the constructions."""

    expected = {
        sp.Integer(1): sp.Rational(5084, 729),
        sp.Rational(1, 2): sp.Rational(147328, 2401),
        sp.Integer(13): sp.Rational(16604, 16629093),
    }
    assert WEIGHT_SIX_RELATION_VALUES == expected
    for central_charge, value in expected.items():
        assert s6_relation_candidate(central_charge) == value

    c = sp.Symbol("c", positive=True)
    relation_lead = sp.limit(c**4 * s6_relation_candidate(c), c, sp.oo)
    riccati_lead = sp.limit(c**4 * s6_riccati_candidate(c), c, sp.oo)
    assert relation_lead == sp.Rational(192, 5)
    assert riccati_lead == sp.Integer(48)


def test_legacy_alias_carries_explicit_relation_semantics():
    """The compatibility alias and semantic record name the required map."""

    c = sp.Symbol("c")
    assert sp.factor(s6_null_candidate(c) - s6_relation_candidate(c)) == 0
    assert WEIGHT_SIX_RELATION_SEMANTICS == {
        "canonical_function": "s6_relation_candidate",
        "defining_relation": "2 R_2 C_6^rel + 2 R_3 R_5 + R_4^2 = 0",
        "domain": "c(5c+22) != 0",
        "status": "formal relation candidate",
        "singular_vector_requirement": "explicit level-six radical/decoupling map",
    }
    assert "formal-relation semantics" in s6_null_candidate.__doc__
    assert "level-six radical/decoupling map" in s6_null_candidate.__doc__
