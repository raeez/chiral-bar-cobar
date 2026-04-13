from sympy import Rational

from compute.lib.bv_brst_purity_engine import (
    BRSTComplex,
    compute_brst_cohomology_sl2,
    dmodule_purity_bv_sl2,
    sl2_data,
    verify_qme_factor,
)


def test_sl2_brst_complex_has_expected_level_one_data():
    brst = BRSTComplex(lie_data=sl2_data(), level=Rational(1))
    assert brst.kappa == Rational(9, 4)
    assert brst.central_charge == Rational(1)
    assert brst.brst_nilpotent is True


def test_sl2_bar_cohomology_uses_correct_h2_dimension():
    data = compute_brst_cohomology_sl2(max_degree=4)
    assert data.cohomology_dims[0] == 1
    assert data.cohomology_dims[2] == 5
    assert data.is_nondegenerate[1] is True


def test_qme_factor_and_purity_verdict():
    purity = dmodule_purity_bv_sl2(Rational(1))
    assert verify_qme_factor()["factor"] == Rational(1, 2)
    assert purity.purity_holds is True
    assert purity.has_irregular_singularities is False
