"""Tests for compute.lib.shadow_l_function_engine.

Covers the six task-specified families and the original default families,
with explicit per-family F_g values at g = 1, 2, 3, pole structure at
s = 1 and s = 2, and cross-module kappa consistency checks.
"""

from fractions import Fraction

import pytest

import compute.lib.shadow_l_function_engine as shadow_l_module
from compute.lib.shadow_l_function_engine import (
    HAS_MPMATH,
    SCOPE_ALL_WEIGHT_G1,
    SCOPE_UNIFORM_WEIGHT,
    SCOPE_UNIFORM_WEIGHT_PROJECTION,
    affine_sl2_family,
    all_standard_families,
    bc_family,
    bernoulli_number,
    betagamma_family,
    evaluate_task_families,
    faber_pandharipande_lambda,
    free_fermion_family,
    genus_free_energy,
    heisenberg_family,
    pole_info,
    pole_residue_at_one,
    pole_residue_at_two,
    principal_w3_family,
    shadow_l_at_s,
    task_families,
    virasoro_family,
    virasoro_self_dual_family,
    with_kappa,
)
from compute.lib.shadow_metric_census import (
    kappa_affine_sl2 as census_kappa_affine_sl2,
    kappa_bc as census_kappa_bc,
    kappa_betagamma as census_kappa_betagamma,
    kappa_heisenberg as census_kappa_heisenberg,
    kappa_virasoro as census_kappa_virasoro,
    kappa_w3 as census_kappa_w3,
)
from compute.lib.utils import lambda_fp as utils_lambda_fp

if HAS_MPMATH:
    import mpmath


def _to_fraction(value) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if hasattr(value, "p") and hasattr(value, "q"):
        return Fraction(int(value.p), int(value.q))
    return Fraction(value)


# ========================================================================
# Expected kappa values for the ORIGINAL default families (Vir at c=26)
# ========================================================================

# VERIFIED: [LT] CLAUDE.md C1 states kappa(H_k) = k; [DC] k = 1 gives 1.
HEIS_DEFAULT_KAPPA = Fraction(1)
# VERIFIED: [LT] CLAUDE.md C2 states kappa(Vir_c) = c/2; [DC] 26/2 = 13.
VIR_C26_KAPPA = Fraction(13)
# VERIFIED: [LT] CLAUDE.md C2 identifies c = 13 as self-dual; [DC] 13/2.
VIR_C13_KAPPA = Fraction(13, 2)
# VERIFIED: [LT] CLAUDE.md C3 gives 3(k+2)/4 for sl_2; [DC] k = 1 gives 9/4.
SL2_K1_KAPPA = Fraction(9, 4)
# VERIFIED: [LT] CLAUDE.md C4 gives kappa(W_3) = 5c/6; [DC] c = 2 gives 5/3.
W3_C2_KAPPA = Fraction(5, 3)
# VERIFIED: [LT] shadow_metric_census.py::kappa_betagamma; [DC] lambda = 1/2 gives -1/2.
BETAGAMMA_HALF_KAPPA = Fraction(-1, 2)
# VERIFIED: [LT] shadow_metric_census.py::kappa_bc; [DC] bc at lambda = 1/2 gives 1/2.
BC_HALF_KAPPA = Fraction(1, 2)

# ========================================================================
# Expected kappa values for the TASK families
# ========================================================================

# VERIFIED: [LT] CLAUDE.md C1; [DC] k = 1 -> kappa = 1.
TASK_HEIS_KAPPA = Fraction(1)
# VERIFIED: [LT] CLAUDE.md C2; [DC] c = 1 -> kappa = 1/2.
TASK_VIR_KAPPA = Fraction(1, 2)
# VERIFIED: [LT] CLAUDE.md C3; [DC] dim(sl_2)=3, h^v=2, k=1 -> 3*3/4 = 9/4.
TASK_SL2_KAPPA = Fraction(9, 4)
# VERIFIED: [LT] CLAUDE.md C4; [DC] H_3=11/6, H_3-1=5/6, c=2 -> 5*2/6 = 5/3.
#   [LC] N=2 check: H_2-1=1/2, kappa(W_2)=c/2=kappa(Vir). Consistent.
TASK_W3_KAPPA = Fraction(5, 3)
# VERIFIED: [LT] shadow_metric_census.py::kappa_betagamma; [DC] lambda=1 -> 6-6+1=1.
#   [CF] matches kappa(Heis,k=1)=1 (coincidence, not identity).
TASK_BG_KAPPA = Fraction(1)
# VERIFIED: [LT] shadow_metric_census.py::kappa_bc; [DC] lambda=1/2 -> -(3/2-3+1) = 1/2.
#   [CF] complementarity: kappa_bc(1/2) + kappa_bg(1/2) = 1/2 + (-1/2) = 0. Correct.
TASK_FF_KAPPA = Fraction(1, 2)

# ========================================================================
# Faber-Pandharipande coefficients
# ========================================================================

# VERIFIED: [LT] Theorem D / compute.lib.utils.lambda_fp; [DC] lambda_1^FP = 1/24.
LAMBDA_1 = Fraction(1, 24)
# VERIFIED: [LT] genus_expansions.tex F_2 = 7*kappa/5760; [DC] FP Bernoulli formula.
#   [CF] B_4 = -1/30, |B_4|/(4!) = 1/720, prefactor (2^3-1)/2^3 = 7/8, product = 7/5760.
LAMBDA_2 = Fraction(7, 5760)
# VERIFIED: [LT] theorem_pixton_ideal_mc_proof.py F_3 = 31*kappa/967680; [DC] FP formula.
#   [CF] B_6 = 1/42, |B_6|/(6!) = 1/30240, prefactor (2^5-1)/2^5 = 31/32, product = 31/967680.
LAMBDA_3 = Fraction(31, 967680)


EXPECTED_KAPPA_DEFAULT = {
    "Heis(k=1)": HEIS_DEFAULT_KAPPA,
    "Vir(c=26)": VIR_C26_KAPPA,
    "sl2_aff(k=1)": SL2_K1_KAPPA,
    "W3(c=2)": W3_C2_KAPPA,
    "betagamma(lambda=1/2)": BETAGAMMA_HALF_KAPPA,
    "bc(lambda=1/2)": BC_HALF_KAPPA,
}


# ========================================================================
# Per-family exact F_g values for the TASK families
# ========================================================================

# VERIFIED: [DC] F_g = kappa * lambda_g^FP, computed below.
# [CF] F_1 = kappa/24 cross-checks with AP120 Cauchy normalization.

TASK_F_VALUES = {
    # Heis(k=1): kappa = 1
    # VERIFIED: [DC] 1 * 1/24 = 1/24; [CF] kappa/24 = 1/24.
    "Heis": {1: Fraction(1, 24), 2: Fraction(7, 5760), 3: Fraction(31, 967680)},
    # Vir(c=1): kappa = 1/2
    # VERIFIED: [DC] (1/2) * 1/24 = 1/48; [CF] kappa/24 = 1/48.
    "Vir": {1: Fraction(1, 48), 2: Fraction(7, 11520), 3: Fraction(31, 1935360)},
    # sl_2(k=1): kappa = 9/4
    # VERIFIED: [DC] (9/4) * 1/24 = 9/96 = 3/32; [CF] kappa/24 = 3/32.
    "sl2": {1: Fraction(3, 32), 2: Fraction(7, 2560), 3: Fraction(31, 430080)},
    # W_3(c=2): kappa = 5/3
    # VERIFIED: [DC] (5/3) * 1/24 = 5/72; [CF] kappa/24 = 5/72.
    "W3": {1: Fraction(5, 72), 2: Fraction(7, 3456), 3: Fraction(31, 580608)},
    # betagamma(lambda=1): kappa = 1
    # VERIFIED: [DC] 1 * 1/24 = 1/24; [CF] same as Heis(k=1) (coincidence).
    "bg": {1: Fraction(1, 24), 2: Fraction(7, 5760), 3: Fraction(31, 967680)},
    # free fermion (bc lambda=1/2): kappa = 1/2
    # VERIFIED: [DC] (1/2) * 1/24 = 1/48; [CF] same as Vir(c=1) (coincidence).
    "ff": {1: Fraction(1, 48), 2: Fraction(7, 11520), 3: Fraction(31, 1935360)},
}


class TestDocumentation:
    def test_pole_documentation_is_present(self):
        doc = shadow_l_module.__doc__ or ""
        assert "s = 1" in doc
        assert "s = 2" in doc
        assert "kappa / 2" in doc
        assert "-kappa * pi^2 / 6" in doc

    def test_ap70_documentation(self):
        doc = shadow_l_module.__doc__ or ""
        assert "AP70" in doc
        assert "regular points" in doc


class TestKappaValues:
    def test_default_standard_family_kappas(self):
        for family in all_standard_families():
            assert family.kappa == EXPECTED_KAPPA_DEFAULT[family.key]

    def test_self_dual_virasoro_kappa(self):
        assert virasoro_self_dual_family().kappa == VIR_C13_KAPPA

    def test_cross_module_kappa_consistency(self):
        # VERIFIED: [CF] cross-check against compute.lib.shadow_metric_census.
        assert _to_fraction(census_kappa_heisenberg(1)) == HEIS_DEFAULT_KAPPA
        assert _to_fraction(census_kappa_virasoro(26)) == VIR_C26_KAPPA
        assert _to_fraction(census_kappa_affine_sl2(1)) == SL2_K1_KAPPA
        assert _to_fraction(census_kappa_w3(2)) == W3_C2_KAPPA
        assert _to_fraction(census_kappa_betagamma(Fraction(1, 2))) == BETAGAMMA_HALF_KAPPA
        assert _to_fraction(census_kappa_bc(Fraction(1, 2))) == BC_HALF_KAPPA


class TestTaskFamilyKappas:
    """Verify kappa for the six task-specified families."""

    def test_heisenberg_k1(self):
        # VERIFIED: [LT] CLAUDE.md C1; [DC] kappa(Heis) = k = 1.
        family = heisenberg_family(1)
        assert family.kappa == TASK_HEIS_KAPPA

    def test_virasoro_c1(self):
        # VERIFIED: [LT] CLAUDE.md C2; [DC] kappa(Vir) = c/2 = 1/2.
        family = virasoro_family(1)
        assert family.kappa == TASK_VIR_KAPPA

    def test_affine_sl2_k1(self):
        # VERIFIED: [LT] CLAUDE.md C3; [DC] 3*(1+2)/4 = 9/4.
        # [LC] k=0 -> 3*2/4 = 3/2, NOT zero (abelian limit, still Koszul).
        family = affine_sl2_family(1)
        assert family.kappa == TASK_SL2_KAPPA

    def test_w3_c2(self):
        # VERIFIED: [LT] CLAUDE.md C4; [DC] 5*2/6 = 5/3.
        # [LC] N=2: kappa(W_2) = c*(H_2-1) = c/2 = kappa(Vir).
        family = principal_w3_family(2)
        assert family.kappa == TASK_W3_KAPPA

    def test_betagamma_lambda1(self):
        # VERIFIED: [LT] shadow_metric_census.py; [DC] 6*1-6*1+1 = 1.
        # [CF] cross-check: census_kappa_betagamma(1) = 1.
        family = betagamma_family(1)
        assert family.kappa == TASK_BG_KAPPA
        assert _to_fraction(census_kappa_betagamma(1)) == TASK_BG_KAPPA

    def test_free_fermion(self):
        # VERIFIED: [LT] shadow_metric_census.py; [DC] -(6/4-3+1) = 1/2.
        # [CF] complementarity: kappa_bc + kappa_bg = 0 at lambda=1/2.
        family = free_fermion_family()
        assert family.kappa == TASK_FF_KAPPA
        assert _to_fraction(census_kappa_bc(Fraction(1, 2))) == TASK_FF_KAPPA

    def test_bc_betagamma_complementarity_at_half(self):
        # VERIFIED: [DC] kappa_bc(1/2) + kappa_bg(1/2) = 1/2 + (-1/2) = 0.
        # [LT] CLAUDE.md C7: c_bg + c_bc = 0.
        assert bc_family(Fraction(1, 2)).kappa + betagamma_family(Fraction(1, 2)).kappa == 0

    def test_task_families_count(self):
        assert len(task_families()) == 6


class TestBernoulliAndLambda:
    def test_bernoulli_numbers(self):
        # VERIFIED: [LT] classical Bernoulli table; [DC] exact recursion.
        assert bernoulli_number(0) == Fraction(1)
        assert bernoulli_number(1) == Fraction(-1, 2)
        assert bernoulli_number(2) == Fraction(1, 6)
        assert bernoulli_number(4) == Fraction(-1, 30)
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_faber_pandharipande_coefficients(self):
        assert faber_pandharipande_lambda(1) == LAMBDA_1
        assert faber_pandharipande_lambda(2) == LAMBDA_2
        assert faber_pandharipande_lambda(3) == LAMBDA_3

    def test_lambda_cross_check_against_utils(self):
        assert faber_pandharipande_lambda(1) == _to_fraction(utils_lambda_fp(1))
        assert faber_pandharipande_lambda(2) == _to_fraction(utils_lambda_fp(2))
        assert faber_pandharipande_lambda(3) == _to_fraction(utils_lambda_fp(3))

    def test_lambda_2_derivation(self):
        # VERIFIED: [DC] |B_4|=1/30, 4!=24, |B_4|/4!=1/720,
        # prefactor=(2^3-1)/2^3=7/8, product=7/5760.
        # [CF] matches compute.lib.utils.lambda_fp(2).
        b4 = abs(bernoulli_number(4))
        assert b4 == Fraction(1, 30)
        prefactor = Fraction(2**3 - 1, 2**3)
        assert prefactor == Fraction(7, 8)
        result = prefactor * b4 / Fraction(24)
        assert result == Fraction(7, 5760)

    def test_lambda_3_derivation(self):
        # VERIFIED: [DC] |B_6|=1/42, 6!=720, |B_6|/6!=1/30240,
        # prefactor=(2^5-1)/2^5=31/32, product=31/967680.
        # [CF] matches compute.lib.utils.lambda_fp(3).
        b6 = abs(bernoulli_number(6))
        assert b6 == Fraction(1, 42)
        prefactor = Fraction(2**5 - 1, 2**5)
        assert prefactor == Fraction(31, 32)
        result = prefactor * b6 / Fraction(720)
        assert result == Fraction(31, 967680)


class TestSpecialValues:
    def test_f1_equals_kappa_over_24_for_every_default_family(self):
        for family in all_standard_families():
            point = shadow_l_at_s(family, -1)
            assert point.kind == "special_value"
            assert point.genus == 1
            assert point.scope_tag == SCOPE_ALL_WEIGHT_G1
            assert point.value_exact == family.kappa * LAMBDA_1
            assert point.value_exact == family.kappa / 24

    def test_g2_and_g3_match_kappa_times_fp_coefficients(self):
        expected_by_genus = {2: LAMBDA_2, 3: LAMBDA_3}
        for family in all_standard_families():
            for genus, coefficient in expected_by_genus.items():
                point = shadow_l_at_s(family, 1 - 2 * genus)
                assert point.kind == "special_value"
                assert point.genus == genus
                assert point.value_exact == family.kappa * coefficient

    def test_uniform_weight_scope_tags_on_g_ge_2(self):
        uniform_weight_families = (
            heisenberg_family(),
            virasoro_family(),
            affine_sl2_family(),
            betagamma_family(),
            bc_family(),
        )
        for family in uniform_weight_families:
            for genus in (2, 3):
                point = shadow_l_at_s(family, 1 - 2 * genus)
                assert point.scope_tag == SCOPE_UNIFORM_WEIGHT

        for genus in (2, 3):
            point = shadow_l_at_s(principal_w3_family(), 1 - 2 * genus)
            assert point.scope_tag == SCOPE_UNIFORM_WEIGHT_PROJECTION
            assert "delta_F_g^cross" in point.connection_note

    def test_virasoro_self_dual_special_values(self):
        family = virasoro_self_dual_family()
        assert shadow_l_at_s(family, -1).value_exact == VIR_C13_KAPPA * LAMBDA_1
        assert shadow_l_at_s(family, -3).value_exact == VIR_C13_KAPPA * LAMBDA_2
        assert shadow_l_at_s(family, -5).value_exact == VIR_C13_KAPPA * LAMBDA_3

    def test_genus_free_energy_matches_special_value_api(self):
        family = affine_sl2_family()
        for genus in (1, 2, 3):
            point = shadow_l_at_s(family, 1 - 2 * genus)
            assert point.value_exact == genus_free_energy(family.kappa, genus)


class TestTaskFamilyFgValues:
    """Explicit numerical F_g tests for the six task-specified families.

    Each expected value is independently derived:
      [DC] F_g = kappa * lambda_g^FP (direct computation)
      [CF] cross-family coincidence check
      [LC] limiting case (g=1: F_1 = kappa/24, unconditional)
    """

    def test_heis_k1_f1(self):
        # VERIFIED: [DC] 1 * 1/24 = 1/24; [LC] F_1 = kappa/24 unconditional.
        point = shadow_l_at_s(heisenberg_family(1), -1)
        assert point.value_exact == Fraction(1, 24)

    def test_heis_k1_f2(self):
        # VERIFIED: [DC] 1 * 7/5760 = 7/5760; [CF] matches bg(lambda=1).
        point = shadow_l_at_s(heisenberg_family(1), -3)
        assert point.value_exact == Fraction(7, 5760)

    def test_heis_k1_f3(self):
        # VERIFIED: [DC] 1 * 31/967680 = 31/967680; [CF] matches bg(lambda=1).
        point = shadow_l_at_s(heisenberg_family(1), -5)
        assert point.value_exact == Fraction(31, 967680)

    def test_vir_c1_f1(self):
        # VERIFIED: [DC] (1/2) * 1/24 = 1/48; [LC] F_1 = kappa/24 = 1/48.
        point = shadow_l_at_s(virasoro_family(1), -1)
        assert point.value_exact == Fraction(1, 48)

    def test_vir_c1_f2(self):
        # VERIFIED: [DC] (1/2) * 7/5760 = 7/11520; [CF] matches ff.
        point = shadow_l_at_s(virasoro_family(1), -3)
        assert point.value_exact == Fraction(7, 11520)

    def test_vir_c1_f3(self):
        # VERIFIED: [DC] (1/2) * 31/967680 = 31/1935360; [CF] matches ff.
        point = shadow_l_at_s(virasoro_family(1), -5)
        assert point.value_exact == Fraction(31, 1935360)

    def test_sl2_k1_f1(self):
        # VERIFIED: [DC] (9/4) * 1/24 = 9/96 = 3/32; [LC] F_1 = kappa/24.
        point = shadow_l_at_s(affine_sl2_family(1), -1)
        assert point.value_exact == Fraction(3, 32)

    def test_sl2_k1_f2(self):
        # VERIFIED: [DC] (9/4) * 7/5760 = 63/23040 = 7/2560.
        # [DA] numerator: 9*7=63, denominator: 4*5760=23040, gcd=9 -> 7/2560.
        point = shadow_l_at_s(affine_sl2_family(1), -3)
        assert point.value_exact == Fraction(7, 2560)

    def test_sl2_k1_f3(self):
        # VERIFIED: [DC] (9/4) * 31/967680 = 279/3870720 = 31/430080.
        # [DA] 9*31=279, 4*967680=3870720, gcd=9 -> 31/430080.
        point = shadow_l_at_s(affine_sl2_family(1), -5)
        assert point.value_exact == Fraction(31, 430080)

    def test_w3_c2_f1(self):
        # VERIFIED: [DC] (5/3) * 1/24 = 5/72; [LC] F_1 = kappa/24.
        point = shadow_l_at_s(principal_w3_family(2), -1)
        assert point.value_exact == Fraction(5, 72)

    def test_w3_c2_f2(self):
        # VERIFIED: [DC] (5/3) * 7/5760 = 35/17280 = 7/3456.
        # [DA] 5*7=35, 3*5760=17280, gcd=5 -> 7/3456.
        point = shadow_l_at_s(principal_w3_family(2), -3)
        assert point.value_exact == Fraction(7, 3456)

    def test_w3_c2_f3(self):
        # VERIFIED: [DC] (5/3) * 31/967680 = 155/2903040 = 31/580608.
        # [DA] 5*31=155, 3*967680=2903040, gcd=5 -> 31/580608.
        point = shadow_l_at_s(principal_w3_family(2), -5)
        assert point.value_exact == Fraction(31, 580608)

    def test_betagamma_lambda1_f1(self):
        # VERIFIED: [DC] 1 * 1/24 = 1/24; [CF] same as Heis(k=1).
        point = shadow_l_at_s(betagamma_family(1), -1)
        assert point.value_exact == Fraction(1, 24)

    def test_betagamma_lambda1_f2(self):
        # VERIFIED: [DC] 1 * 7/5760 = 7/5760; [CF] same as Heis(k=1).
        point = shadow_l_at_s(betagamma_family(1), -3)
        assert point.value_exact == Fraction(7, 5760)

    def test_betagamma_lambda1_f3(self):
        # VERIFIED: [DC] 1 * 31/967680 = 31/967680; [CF] same as Heis(k=1).
        point = shadow_l_at_s(betagamma_family(1), -5)
        assert point.value_exact == Fraction(31, 967680)

    def test_free_fermion_f1(self):
        # VERIFIED: [DC] (1/2) * 1/24 = 1/48; [CF] same as Vir(c=1).
        point = shadow_l_at_s(free_fermion_family(), -1)
        assert point.value_exact == Fraction(1, 48)

    def test_free_fermion_f2(self):
        # VERIFIED: [DC] (1/2) * 7/5760 = 7/11520; [CF] same as Vir(c=1).
        point = shadow_l_at_s(free_fermion_family(), -3)
        assert point.value_exact == Fraction(7, 11520)

    def test_free_fermion_f3(self):
        # VERIFIED: [DC] (1/2) * 31/967680 = 31/1935360; [CF] same as Vir(c=1).
        point = shadow_l_at_s(free_fermion_family(), -5)
        assert point.value_exact == Fraction(31, 1935360)

    def test_all_task_f_values_against_table(self):
        """Cross-check all 18 F_g values against the TASK_F_VALUES table."""
        families_by_label = {
            "Heis": heisenberg_family(1),
            "Vir": virasoro_family(1),
            "sl2": affine_sl2_family(1),
            "W3": principal_w3_family(2),
            "bg": betagamma_family(1),
            "ff": free_fermion_family(),
        }
        for label, family in families_by_label.items():
            for g in (1, 2, 3):
                point = shadow_l_at_s(family, 1 - 2 * g)
                expected = TASK_F_VALUES[label][g]
                assert point.value_exact == expected, (
                    f"{label} g={g}: got {point.value_exact}, expected {expected}"
                )


class TestPoles:
    def test_pole_at_one_detection_and_residue(self):
        point = shadow_l_at_s(heisenberg_family(), 1)
        assert point.kind == "pole"
        assert point.pole_order == 1
        assert point.residue_exact == Fraction(1, 2)
        assert point.residue_exact == pole_residue_at_one(HEIS_DEFAULT_KAPPA)
        assert point.residue_formula == "kappa/2"

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_pole_at_two_detection_and_residue(self):
        point = shadow_l_at_s(virasoro_family(), 2)
        expected = pole_residue_at_two(VIR_C26_KAPPA)
        numeric = mpmath.mpf(point.residue_numeric)
        assert point.kind == "pole"
        assert point.pole_order == 1
        assert point.residue_formula == "-kappa*pi^2/6"
        assert abs(numeric - expected) < mpmath.mpf("1e-16")

    def test_pole_at_one_for_all_task_families(self):
        """Verify residue at s=1 for every task family."""
        expected_kappas = [
            TASK_HEIS_KAPPA, TASK_VIR_KAPPA, TASK_SL2_KAPPA,
            TASK_W3_KAPPA, TASK_BG_KAPPA, TASK_FF_KAPPA,
        ]
        for family, kappa in zip(task_families(), expected_kappas):
            point = shadow_l_at_s(family, 1)
            assert point.kind == "pole"
            assert point.pole_order == 1
            # VERIFIED: [DC] residue = kappa/2 at s=1.
            assert point.residue_exact == kappa / 2

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_pole_at_two_for_all_task_families(self):
        """Verify residue at s=2 for every task family."""
        expected_kappas = [
            TASK_HEIS_KAPPA, TASK_VIR_KAPPA, TASK_SL2_KAPPA,
            TASK_W3_KAPPA, TASK_BG_KAPPA, TASK_FF_KAPPA,
        ]
        for family, kappa in zip(task_families(), expected_kappas):
            point = shadow_l_at_s(family, 2)
            assert point.kind == "pole"
            assert point.pole_order == 1
            assert point.residue_formula == "-kappa*pi^2/6"
            expected = pole_residue_at_two(kappa)
            numeric = mpmath.mpf(point.residue_numeric)
            assert abs(numeric - expected) < mpmath.mpf("1e-16")

    def test_pole_info_structure(self):
        """Verify pole_info returns data for both poles."""
        family = heisenberg_family(1)
        info = pole_info(family)
        assert len(info["poles"]) == 2
        assert info["poles"][0]["s"] == 1
        assert info["poles"][0]["order"] == 1
        assert info["poles"][0]["residue_exact"] == Fraction(1, 2)
        assert info["poles"][0]["residue_formula"] == "kappa/2"
        assert info["poles"][1]["s"] == 2
        assert info["poles"][1]["order"] == 1
        assert info["poles"][1]["residue_formula"] == "-kappa*pi^2/6"

    def test_pole_info_for_all_task_families(self):
        """Every task family has exactly two poles at s=1 and s=2."""
        for family in task_families():
            info = pole_info(family)
            assert len(info["poles"]) == 2
            pole_locations = [p["s"] for p in info["poles"]]
            assert pole_locations == [1, 2]
            for p in info["poles"]:
                assert p["order"] == 1, f"{family.key}: pole at s={p['s']} should be simple"


class TestF1MatchesLsh:
    """Verify F_g = L^sh(1-2g) at g=1 for each task family (AP120 sanity check)."""

    def test_f1_is_kappa_over_24_for_every_task_family(self):
        """The genus-1 identity F_1 = kappa/24 is unconditional (ALL-WEIGHT g=1)."""
        expected_kappas = [
            TASK_HEIS_KAPPA, TASK_VIR_KAPPA, TASK_SL2_KAPPA,
            TASK_W3_KAPPA, TASK_BG_KAPPA, TASK_FF_KAPPA,
        ]
        for family, kappa in zip(task_families(), expected_kappas):
            point = shadow_l_at_s(family, -1)  # s = 1 - 2*1 = -1
            assert point.genus == 1
            assert point.scope_tag == SCOPE_ALL_WEIGHT_G1
            # VERIFIED: [DC] F_1 = kappa/24; [LT] CLAUDE.md Theorem D; [CF] AP120.
            assert point.value_exact == kappa / 24


class TestEvaluateTaskFamilies:
    """Test the batch evaluation API."""

    def test_evaluate_returns_18_evaluations(self):
        results = evaluate_task_families()
        assert len(results) == 18  # 6 families x 3 genera

    def test_evaluate_covers_all_genera(self):
        results = evaluate_task_families()
        genera_seen = set()
        for r in results:
            genera_seen.add(r.genus)
        assert genera_seen == {1, 2, 3}

    def test_evaluate_covers_all_families(self):
        results = evaluate_task_families()
        keys_seen = set()
        for r in results:
            keys_seen.add(r.family_key)
        assert len(keys_seen) == 6


class TestZeroKappaConsistency:
    def test_zero_kappa_annihilates_special_values_and_residues(self):
        for family in all_standard_families():
            zero_family = with_kappa(family, 0)
            for s in (-1, -3, -5):
                point = shadow_l_at_s(zero_family, s)
                assert point.value_exact == 0

            pole_one = shadow_l_at_s(zero_family, 1)
            assert pole_one.residue_exact == 0

            pole_two = shadow_l_at_s(zero_family, 2)
            if HAS_MPMATH:
                assert abs(mpmath.mpf(pole_two.residue_numeric)) < mpmath.mpf("1e-30")


class TestNumerics:
    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_special_values_have_high_precision_numeric_output(self):
        point = shadow_l_at_s(affine_sl2_family(), -5)
        expected = mpmath.mpf(point.value_exact.numerator) / point.value_exact.denominator
        numeric = mpmath.mpf(point.value_numeric)
        assert abs(numeric - expected) < mpmath.mpf("1e-16")

    @pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")
    def test_residue_at_two_has_high_precision_numeric_output(self):
        residue = pole_residue_at_two(BC_HALF_KAPPA)
        point = shadow_l_at_s(bc_family(), 2)
        numeric = mpmath.mpf(point.residue_numeric)
        assert abs(numeric - residue) < mpmath.mpf("1e-16")


class TestEdgeCases:
    def test_invalid_s_raises(self):
        family = heisenberg_family(1)
        with pytest.raises(ValueError):
            shadow_l_at_s(family, 0)
        with pytest.raises(ValueError):
            shadow_l_at_s(family, -2)  # even, not a genus point
        with pytest.raises(ValueError):
            shadow_l_at_s(family, 3)

    def test_negative_kappa_betagamma_half(self):
        """betagamma at lambda=1/2 has kappa=-1/2: negative kappa is valid."""
        family = betagamma_family(Fraction(1, 2))
        assert family.kappa == Fraction(-1, 2)
        point = shadow_l_at_s(family, -1)
        assert point.value_exact == Fraction(-1, 48)

    def test_genus_1_is_always_all_weight(self):
        """Even multi-weight families get ALL-WEIGHT tag at g=1 (AP32)."""
        w3 = principal_w3_family(2)
        assert not w3.uniform_weight
        point = shadow_l_at_s(w3, -1)
        assert point.scope_tag == SCOPE_ALL_WEIGHT_G1
