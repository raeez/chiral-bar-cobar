"""First-principles checks for the Chern-Weil level-shift chapter."""

from __future__ import annotations

from fractions import Fraction


def killing_inverse_in_trace_units(h_dual: int) -> Fraction:
    """If B_Kil = 2 h^vee B_tr, then B_Kil^{-1} = (2h^vee)^{-1} B_tr^{-1}."""
    return Fraction(1, 2 * h_dual)


def kappa_km(dim_g: int, h_dual: int, k: int) -> Fraction:
    return Fraction(dim_g * (k + h_dual), 2 * h_dual)


def sugawara_central_charge(dim_g: int, h_dual: int, k: int) -> Fraction:
    return Fraction(k * dim_g, k + h_dual)


def test_killing_inverse_tensor_scales_contravariantly():
    for h_dual in [2, 3, 4, 30]:
        omega_kil = killing_inverse_in_trace_units(h_dual)
        omega_kz = 2 * h_dual * omega_kil
        assert omega_kil == Fraction(1, 2 * h_dual)
        assert omega_kz == 1


def test_trace_and_kz_coefficients_are_not_generically_equal():
    h_dual = 2
    for k in [0, 1, 2, 5]:
        trace_coeff = Fraction(k, 1)
        kz_coeff = Fraction(1, k + h_dual)
        assert trace_coeff != kz_coeff
    assert Fraction(0, 1) == 0
    assert Fraction(1, h_dual) != 0


def test_old_level_shift_roots_do_not_solve_fixed_rescaling_identity():
    for h_dual in [2, 3, 4, 30]:
        old_positive = h_dual
        old_negative = -2 * h_dual
        assert old_positive * (old_positive + h_dual) != 2 * h_dual
        assert old_negative * (old_negative + h_dual) != 2 * h_dual


def test_standard_kappa_and_central_charge_values_at_level_one():
    cases = {
        "sl2": (3, 2, Fraction(9, 4), Fraction(1, 1)),
        "sl3": (8, 3, Fraction(16, 3), Fraction(2, 1)),
        "so5": (10, 3, Fraction(20, 3), Fraction(5, 2)),
        "g2": (14, 4, Fraction(35, 4), Fraction(14, 5)),
        "e8": (248, 30, Fraction(248 * 31, 60), Fraction(248, 31)),
    }

    for _name, (dim_g, h_dual, expected_kappa, expected_c) in cases.items():
        assert kappa_km(dim_g, h_dual, 1) == expected_kappa
        assert sugawara_central_charge(dim_g, h_dual, 1) == expected_c
