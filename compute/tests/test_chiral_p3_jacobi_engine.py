from fractions import Fraction

from compute.lib.chiral_p3_jacobi_engine import ChiralP3BracketSL2, LieElement


def test_zero_mode_bracket_matches_sl2_structure_constants():
    bracket = ChiralP3BracketSL2(Fraction(1))
    assert bracket.zero_mode_bracket("e", "f") == LieElement.gen("h")
    assert bracket.zero_mode_bracket("h", "e") == LieElement.gen("e").scale(Fraction(2))


def test_zero_mode_and_pva_jacobi_hold_on_sample_triple():
    bracket = ChiralP3BracketSL2(Fraction(1))
    assert bracket.verify_zero_mode_jacobi("e", "f", "h").is_zero()
    assert bracket.verify_pva_jacobi("e", "f", "h") is True


def test_level_limits_and_kappa_checks():
    generic = ChiralP3BracketSL2(Fraction(1))
    level_zero = ChiralP3BracketSL2(Fraction(0))

    assert generic.verify_kappa_consistency() is True
    assert level_zero.verify_k0_limit() is True
    assert generic.verify_killing_ad_invariance() is True
