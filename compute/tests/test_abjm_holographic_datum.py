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
    assert summary["A^i"] == "H^*(B(A_ABJM(1,1)))"
    assert summary["A!"] == "A_ABJM(1,1)!"
    assert summary["c(A)"] == "-2"
    assert summary["kappa(A)"] == "-1"
    assert summary["kappa(A!)"] == "1"
    assert summary["complementarity"] == "0"
    assert summary["C (bulk)"] == "RW(T*(C^1/Z_1))"
    assert summary["r(z)"] == "rational (Casimir/z)"
    assert summary["shadow_depth"] == "4"
    assert summary["nabla^hol flat"] == "True"
    assert datum.r_matrix_type == "rational (Casimir/z)"
    assert datum.theta_kappa == Fraction(-1)
    assert datum.connection_is_flat is True
    assert general_r["residue"] == "Omega_gl(2)/z"
    assert general_r["satisfies_cybe"] is True


def test_abjm_datum_exposes_seven_entry_package_as_projections():
    datum = make_abjm_datum(2, 1)

    seven_entry_package = {
        "A": datum.A_name,
        "A^i": datum.A_bar_dual_name,
        "A!": datum.A_dual_name,
        "C": datum.bulk_tft,
        "r(z)": datum.r_matrix_type,
        "Theta_A": datum.theta_kappa,
        "nabla^hol": datum.connection_is_flat,
    }

    assert tuple(seven_entry_package) == (
        "A",
        "A^i",
        "A!",
        "C",
        "r(z)",
        "Theta_A",
        "nabla^hol",
    )
    assert seven_entry_package["A"] == "A_ABJM(2,1)"
    assert seven_entry_package["A^i"] == "H^*(B(A_ABJM(2,1)))"
    assert seven_entry_package["A!"] == "A_ABJM(2,1)!"
    assert seven_entry_package["C"] == "RW(T*(C^2/Z_1))"
    assert seven_entry_package["r(z)"] == "rational (Casimir/z)"
    assert seven_entry_package["Theta_A"] == Fraction(-4)
    assert seven_entry_package["nabla^hol"] is True


def test_abjm_dual_companion_and_bulk_slots_are_distinct():
    summary = make_abjm_datum(1, 1).summary()

    assert len({
        summary["A"],
        summary["A^i"],
        summary["A!"],
        summary["C (bulk)"],
    }) == 4
    assert summary["A^i"].startswith("H^*(B(")
    assert summary["A!"].endswith("!")
    assert summary["C (bulk)"].startswith("RW(")
    assert "Z_ch^der(A)" in summary["bulk_slot_scope"]
    assert "distinct from A, B(A), A^i, and A!" in summary["bulk_slot_scope"]


def test_abjm_bar_cobar_scope_is_inversion_not_duality():
    summary = make_abjm_datum(1, 1).summary()

    assert summary["dual_slot_scope"] == (
        "A! is a Verdier/Koszul companion scalar summary, not Omega(B(A))"
    )
    assert summary["bar_cobar_scope"] == (
        "Omega(B(A)) recovers A by inversion; it is not the A! slot"
    )
    assert summary["A!"] != "Omega(B(A))"
    assert "duality" not in summary["bar_cobar_scope"].lower()


def test_abjm_compute_package_is_scalar_descriptor_only():
    summary = make_abjm_datum(1, 1).summary()

    assert summary["compute_package_scope"] == (
        "six primary projections: scalar/descriptor package; not VOA reconstruction"
    )
    assert "scalar summary" in summary["dual_slot_scope"]
    assert "not VOA reconstruction" in summary["compute_package_scope"]
