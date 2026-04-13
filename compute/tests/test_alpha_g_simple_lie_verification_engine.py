from compute.lib.alpha_g_simple_lie_verification_engine import (
    LIE_ALGEBRA_TABLE,
    alpha_g_for_algebra,
    check_b2_c2_isomorphism,
    check_d3_a3_isomorphism,
    compute_all_alpha_g,
    verify_all_classical_data,
)


def test_table_and_classical_checks_pass():
    assert len(LIE_ALGEBRA_TABLE) == 31
    assert verify_all_classical_data() == []


def test_boundary_alpha_values_are_stable():
    results = compute_all_alpha_g()

    assert alpha_g_for_algebra("A1") == 26
    assert alpha_g_for_algebra("E8") == 29776
    assert results["E8"].rank_contribution == 16
    assert results["E8"].curvature_contribution == 29760


def test_low_rank_isomorphism_checks_hold():
    assert check_b2_c2_isomorphism()[0] is True
    assert check_d3_a3_isomorphism()[0] is True
