from fractions import Fraction

from compute.lib.cohft_dr_hierarchy_engine import (
    DRHierarchyRank1,
    cohft_string_equation_from_dr,
    dr_cycle_genus0,
    dr_cycle_genus1_coefficient,
    faber_pandharipande,
    r_matrix_coefficient,
    wk_intersection,
)


def test_witten_kontsevich_and_faber_pandharipande_seeds():
    assert wk_intersection(1, (1,)) == Fraction(1, 24)
    assert faber_pandharipande(2) == Fraction(7, 5760)
    assert r_matrix_coefficient(3) == Fraction(-139, 51840)


def test_low_genus_dr_cycle_formulas():
    assert dr_cycle_genus0((1, -1)) == Fraction(1)
    assert dr_cycle_genus0((1, 1)) == Fraction(0)
    assert dr_cycle_genus1_coefficient((1, -1)) == Fraction(1, 12)


def test_rank_one_hierarchy_and_string_bridge():
    heisenberg = DRHierarchyRank1.heisenberg(Fraction(1))
    bridge = cohft_string_equation_from_dr("G", 1)

    assert heisenberg.shadow_class == "G"
    assert heisenberg.propagator == Fraction(1)
    assert bridge["dr_string_equation"] == "UNCONDITIONAL"
    assert bridge["bridge"] == "COMPLETE"
