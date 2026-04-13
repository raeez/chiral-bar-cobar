from fractions import Fraction

from sympy import Rational, pi, simplify

from compute.lib.abjm_holographic_datum import (
    ABJMData,
    abjm_B_k,
    abjm_N32_coefficient,
    abjm_r_matrix_general,
    make_abjm_datum,
)


def test_abjm_data_invariants():
    data = ABJMData(N=2, k=1)
    assert data.central_charge == Fraction(-8)
    assert data.kappa == Fraction(-4)
    assert data.kappa_dual == Fraction(4)
    assert data.complementarity_sum == Fraction(0)
    assert data.shadow_depth == 1000


def test_abjm_level_one_shift_and_scaling_coefficient():
    assert abjm_B_k(1) == Rational(5, 24)
    assert simplify(abjm_N32_coefficient(2) - 2 * pi / 3) == 0


def test_abjm_holographic_summary_matches_rank_one_datum():
    datum = make_abjm_datum(1, 1)
    summary = datum.summary()
    general_r = abjm_r_matrix_general(2, 1)

    assert summary["A"] == "A_ABJM(1,1)"
    assert summary["kappa(A)"] == "-1"
    assert datum.r_matrix_type == "rational (Casimir/z)"
    assert datum.connection_is_flat is True
    assert general_r["residue"] == "Omega_gl(2)/z"
    assert general_r["satisfies_cybe"] is True
