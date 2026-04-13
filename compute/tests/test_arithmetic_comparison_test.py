from compute.lib.arithmetic_comparison_test import (
    extract_arithmetic_from_mc_heisenberg,
    extract_arithmetic_from_mc_leech,
    full_comparison_suite,
    minimal_arity_for_nabla,
    niemeier_root_counts,
    niemeier_scalar_mc_comparison,
)


def test_niemeier_root_counts_separate_leech_from_e8_cubed():
    roots = niemeier_root_counts()
    assert roots["Leech"] == 0
    assert roots["E8^3"] == 720


def test_scalar_mc_is_not_enough_for_niemeier_packets():
    comparison = niemeier_scalar_mc_comparison()
    assert comparison["scalar_mc_identical"] is True
    assert comparison["nabla_arith_distinct"] is True
    assert comparison["n_distinct_cusp_coefficients"] > 1


def test_minimal_arity_tracks_family_depth():
    assert extract_arithmetic_from_mc_heisenberg(1.0)["arity_needed"] == 2
    assert extract_arithmetic_from_mc_leech()["arity_needed_for_cusp"] == 3

    lattice = minimal_arity_for_nabla("lattice", 24)
    assert lattice["weight"] == 12
    assert lattice["min_arity"] == 3


def test_full_comparison_suite_covers_standard_families():
    suite = full_comparison_suite()
    assert {"Heisenberg", "affine_sl2", "E8", "Leech", "Virasoro_c25"} <= set(suite)
    assert suite["Heisenberg"]["mc_determines_nabla"] is True
