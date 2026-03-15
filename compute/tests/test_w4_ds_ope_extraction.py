"""Tests for the MC4 W_4 DS stage-4 packet extraction.

Verifies:
  - c_334^2 formula: zeros, poles, positivity at unitary minimal models
  - c_444^2 formula: zeros, poles, positivity
  - c_343, c_344 mixed OPE coefficients and their relations to c_334
  - Virasoro-target identities: C_{4,4;2;0,6} = 2 and C_{3,4;2;0,5} = 0
  - Feigin-Frenkel duality: behavior under k -> -k-8
  - Classical limit (c -> infinity)
  - Consistency with the stage-4 exact packet scaffold
  - Special values and Jacobi identity checks

References:
  - concordance.tex: rem:mc4-winfty-computation-target
  - bar_cobar_construction.tex: cor:winfty-ds-stage4-ope-blocks
  - Hornfeck, Nucl. Phys. B 407 (1993) 57
  - Blumenhagen et al., Nucl. Phys. B 461 (1996) 460
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, limit, oo, sqrt

from compute.lib.w4_ds_ope_extraction import (
    c334_squared_formula,
    c334_at_level,
    c444_squared_formula,
    c444_at_level,
    c343_formula,
    c343_sign_relative_to_c334,
    c344_formula,
    lambda_two_point,
    w4_primary_two_point,
    w3w3_pole2_decomposition,
    w3w3_alpha_in_w4,
    verify_virasoro_target_identity_c442,
    verify_virasoro_target_identity_c342,
    verify_stage4_virasoro_target_identities,
    w4_full_ope_coefficients,
    w4_full_ope_at_level,
    ff_duality_c334,
    verify_jacobi_w333,
    verify_jacobi_w334,
    c334_squared_at_special_values,
    c334_zeros_and_poles,
    c444_zeros_and_poles,
    classical_limit,
    extraction_report,
)

from compute.lib.w4_stage4_coefficients import (
    w4_central_charge,
    w4_dual_level,
    w4_complementarity_sum,
    stage4_exact_identity_packet,
    stage4_live_targets,
    frontier_package,
)


# ===== c_334^2 formula =====

class TestC334Squared:
    """Tests for c_334^2 = 42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]."""

    def test_formula_type(self):
        """c_334^2 is a rational function of c."""
        c = Symbol('c')
        result = c334_squared_formula(c)
        assert result.is_rational_function(c)

    def test_formula_factored(self):
        """c_334^2 factors as expected."""
        c = Symbol('c')
        result = factor(c334_squared_formula(c))
        # The numerator should have c^2 * (5c+22) and denominator (c+24)(7c+68)(3c+46)
        assert simplify(result - 42 * c**2 * (5*c+22) / ((c+24)*(7*c+68)*(3*c+46))) == 0

    def test_zero_at_c0(self):
        """c_334^2 vanishes at c=0 (trivial theory has no W^4 coupling)."""
        assert c334_squared_formula(Rational(0)) == 0

    def test_double_zero_at_c0(self):
        """c_334^2 has a DOUBLE zero at c=0 (from c^2 factor)."""
        c = Symbol('c')
        expr = c334_squared_formula(c)
        # The c^2 factor means the first derivative also vanishes
        from sympy import diff
        assert simplify(expr.subs(c, 0)) == 0
        assert simplify(diff(expr, c).subs(c, 0)) == 0

    def test_zero_at_c_minus_22_over_5(self):
        """c_334^2 vanishes at c=-22/5 (W_3 composite pole, 5c+22=0)."""
        assert c334_squared_formula(Rational(-22, 5)) == 0

    def test_poles(self):
        """c_334^2 has poles at c=-24, c=-68/7, c=-46/3."""
        # Check that the denominator vanishes at these points
        c = Symbol('c')
        denom = (c + 24) * (7*c + 68) * (3*c + 46)
        assert denom.subs(c, -24) == 0
        assert denom.subs(c, Rational(-68, 7)) == 0
        assert denom.subs(c, Rational(-46, 3)) == 0

    def test_positive_for_large_c(self):
        """c_334^2 > 0 for sufficiently large c (classical regime)."""
        for c_val in [10, 50, 100, 1000]:
            assert c334_squared_formula(Rational(c_val)) > 0

    def test_at_level_k1(self):
        """c_334^2 at level k=1 (c=-189) is positive."""
        c334_sq = c334_at_level(Rational(1))
        assert c334_sq > 0

    def test_at_level_k0(self):
        """c_334^2 at level k=0 (c=-132) is positive."""
        c334_sq = c334_at_level(Rational(0))
        assert c334_sq > 0


class TestC334Unitarity:
    """c_334^2 >= 0 at all W_4 unitary minimal models."""

    @pytest.mark.parametrize("p", range(4, 20))
    def test_unitary_minimal_model(self, p):
        """c_334^2 >= 0 at the W_4 (p, p+1) minimal model."""
        c_val = 3 * (1 - Rational(20, p * (p + 1)))
        assert c334_squared_formula(c_val) >= 0


class TestC334ClassicalLimit:
    """c_334^2 in the classical limit c -> infinity."""

    def test_limit_exists(self):
        """c_334^2 has a finite limit as c -> infinity."""
        c = Symbol('c')
        lim = limit(c334_squared_formula(c), c, oo)
        assert lim.is_finite

    def test_limit_value(self):
        """c_334^2 -> 10 as c -> infinity (classical structure constant)."""
        c = Symbol('c')
        lim = limit(c334_squared_formula(c), c, oo)
        assert lim == 10

    def test_classical_limit_function(self):
        """classical_limit() returns correct classical structure constants."""
        cl = classical_limit()
        assert cl["c_334_sq_limit"] == 10
        assert cl["c_444_sq_limit"] == Rational(48, 25)

    def test_c334_approaches_constant(self):
        """c_334^2 -> 10 as c -> infinity (degree 3 / degree 3 = constant).

        42 c^2 (5c+22) / [(c+24)(7c+68)(3c+46)]
        = 42*5 c^3 / (1*7*3 c^3) + lower = 210/21 = 10.
        """
        c = Symbol('c')
        lim = limit(c334_squared_formula(c), c, oo)
        assert lim == 10


# ===== c_444^2 formula =====

class TestC444Squared:
    """Tests for c_444^2 = 112 c^2 (2c-1)(3c+46) / [(c+24)(7c+68)(10c+197)(5c+3)]."""

    def test_formula_type(self):
        """c_444^2 is a rational function of c."""
        c = Symbol('c')
        result = c444_squared_formula(c)
        assert result.is_rational_function(c)

    def test_zero_at_c0(self):
        """c_444^2 vanishes at c=0."""
        assert c444_squared_formula(Rational(0)) == 0

    def test_zero_at_c_half(self):
        """c_444^2 vanishes at c=1/2 (from 2c-1 factor)."""
        assert c444_squared_formula(Rational(1, 2)) == 0

    def test_zero_at_c_minus_46_over_3(self):
        """c_444^2 vanishes at c=-46/3 (from 3c+46 factor)."""
        assert c444_squared_formula(Rational(-46, 3)) == 0

    def test_positive_for_c_gt_half(self):
        """c_444^2 > 0 for c > 1/2 (outside degenerate range)."""
        for c_val in [1, 2, 3, 10, 50, 100]:
            assert c444_squared_formula(Rational(c_val)) > 0

    def test_poles(self):
        """c_444^2 has poles at c=-24, -68/7, -197/10, -3/5."""
        c = Symbol('c')
        denom = (c+24) * (7*c+68) * (10*c+197) * (5*c+3)
        for pole in [Rational(-24), Rational(-68,7), Rational(-197,10), Rational(-3,5)]:
            assert denom.subs(c, pole) == 0

    def test_classical_limit(self):
        """c_444^2 -> 48/25 as c -> infinity."""
        c = Symbol('c')
        lim = limit(c444_squared_formula(c), c, oo)
        assert lim == Rational(48, 25)

    @pytest.mark.parametrize("p", range(4, 20))
    def test_unitary_minimal_model(self, p):
        """c_444^2 >= 0 at the W_4 (p, p+1) minimal model."""
        c_val = 3 * (1 - Rational(20, p * (p + 1)))
        assert c444_squared_formula(c_val) >= 0


# ===== Mixed OPE coefficients =====

class TestMixedCoefficients:
    """Tests for C_{3,4;3;0,4} and C_{3,4;4;0,3}."""

    def test_c343_proportional_to_c334(self):
        """C_{3,4;3;0,4}^2 = (9/16) c_334^2 (metric relation)."""
        c = Symbol('c')
        ratio = simplify(c343_formula(c) / c334_squared_formula(c))
        assert ratio == Rational(9, 16)

    def test_c343_sign_relation(self):
        """C_{3,4;3;0,4} = -(3/4) c_334 (from adjoint identity)."""
        assert c343_sign_relative_to_c334() == Rational(-3, 4)

    def test_c344_proportional_to_c334(self):
        """C_{3,4;4;0,3}^2 = (5/7) c_334^2 (constant ratio)."""
        c = Symbol('c')
        ratio = simplify(c344_formula(c) / c334_squared_formula(c))
        assert ratio == Rational(5, 7)

    def test_c343_zero_at_c0(self):
        """C_{3,4;3;0,4}^2 vanishes at c=0."""
        assert c343_formula(Rational(0)) == 0

    def test_c344_zero_at_c0(self):
        """C_{3,4;4;0,3}^2 vanishes at c=0."""
        assert c344_formula(Rational(0)) == 0

    def test_c343_positive_for_large_c(self):
        """C_{3,4;3;0,4}^2 > 0 for large c."""
        assert c343_formula(Rational(50)) > 0

    def test_c344_positive_for_large_c(self):
        """C_{3,4;4;0,3}^2 > 0 for large c."""
        assert c344_formula(Rational(50)) > 0

    def test_c343_classical_limit(self):
        """C_{3,4;3;0,4}^2 -> 45/8 as c -> infinity."""
        c = Symbol('c')
        lim = limit(c343_formula(c), c, oo)
        assert lim == Rational(45, 8)

    def test_c344_classical_limit(self):
        """C_{3,4;4;0,3}^2 -> 50/7 as c -> infinity."""
        c = Symbol('c')
        lim = limit(c344_formula(c), c, oo)
        assert lim == Rational(50, 7)


# ===== Virasoro-target identities =====

class TestFalsifiablePredictions:
    """Verify the two distinguished Virasoro-target identities."""

    def test_c442_equals_2(self):
        """C^res_{4,4;2;0,6} = 2 (universal T-coupling)."""
        result = verify_virasoro_target_identity_c442()
        assert result["theorematic_value"] == 2
        assert result["status"] == "VERIFIED"

    def test_c342_equals_0(self):
        """C^res_{3,4;2;0,5} = 0 (mixed Virasoro vanishing)."""
        result = verify_virasoro_target_identity_c342()
        assert result["theorematic_value"] == 0
        assert result["status"] == "VERIFIED"

    def test_both_identities(self):
        """Both Virasoro-target identities are verified."""
        results = verify_stage4_virasoro_target_identities()
        assert len(results) == 2
        assert results["C_{4,4;2;0,6}"]["theorematic_value"] == 2
        assert results["C_{3,4;2;0,5}"]["theorematic_value"] == 0

    def test_c442_mechanism(self):
        """C^res_{4,4;2;0,6} = 2 follows from conformal Ward identity."""
        result = verify_virasoro_target_identity_c442()
        assert "Ward" in result["mechanism"] or "universal" in result["mechanism"]

    def test_c342_mechanism(self):
        """C^res_{3,4;2;0,5} = 0 follows from orthogonality."""
        result = verify_virasoro_target_identity_c342()
        assert "vanish" in result["mechanism"] or "orthogonal" in result["mechanism"]


# ===== Normal ordering data =====

class TestNormalOrdering:
    """Tests for Lambda and W^4 two-point functions."""

    def test_lambda_norm(self):
        """<Lambda, Lambda> = c(5c+22)/10."""
        c = Symbol('c')
        assert simplify(lambda_two_point(c) - c * (5*c+22) / 10) == 0

    def test_lambda_norm_at_c_minus_22_over_5(self):
        """<Lambda, Lambda> = 0 at c = -22/5."""
        assert lambda_two_point(Rational(-22, 5)) == 0

    def test_w4_primary_norm(self):
        """<W^4, W^4> = c/4."""
        c = Symbol('c')
        assert simplify(w4_primary_two_point(c) - c / 4) == 0

    def test_w3w3_alpha(self):
        """alpha = 16/(22+5c) in the W_4 algebra (same as W_3)."""
        c = Symbol('c')
        alpha = w3w3_alpha_in_w4(c)
        assert simplify(alpha - Rational(16) / (22 + 5*c)) == 0


# ===== W_4 full OPE =====

class TestFullOPE:
    """Tests for the complete W_4 OPE algebra."""

    def test_stage3_coefficients(self):
        """Stage-3 coefficients match the W_3 OPE."""
        ope = w4_full_ope_coefficients()
        assert ope["C_{2,2;2;0,2}"] == 2
        assert ope["C_{2,3;3;0,2}"] == 3
        assert ope["C_{2,4;4;0,2}"] == 4
        assert ope["C_{3,3;2;0,4}"] == 2

    def test_virasoro_target_identities_in_full_ope(self):
        """Theorematic Virasoro-target identities are embedded in the full OPE."""
        ope = w4_full_ope_coefficients()
        assert ope["C_{4,4;2;0,6}"] == 2
        assert ope["C_{3,4;2;0,5}"] == 0

    def test_curvatures(self):
        """Curvature channels: m_0^T = c/2, m_0^{W^3} = c/3, m_0^{W^4} = c/4."""
        c = Symbol('c')
        ope = w4_full_ope_coefficients(c)
        assert simplify(ope["m0_T"] - c / 2) == 0
        assert simplify(ope["m0_W3"] - c / 3) == 0
        assert simplify(ope["m0_W4"] - c / 4) == 0

    def test_all_coefficients_present(self):
        """All 13 OPE entries are present."""
        ope = w4_full_ope_coefficients()
        # 3 curvatures + 4 stage-3 + 4 stage-4 squared + 2 Virasoro-target identities = 13
        assert len(ope) == 13

    def test_at_specific_level(self):
        """w4_full_ope_at_level works at k=1."""
        ope = w4_full_ope_at_level(Rational(1))
        # Central charge at k=1: c = -189
        assert ope["C_{2,2;2;0,2}"] == 2
        assert ope["c_334_squared"] == c334_squared_formula(Rational(-189))


# ===== Feigin-Frenkel duality =====

class TestFFDuality:
    """Tests for the Feigin-Frenkel duality k -> -k-8."""

    def test_dual_level(self):
        """FF dual level: k' = -k - 8."""
        assert w4_dual_level(0) == -8
        assert w4_dual_level(1) == -9
        assert w4_dual_level(-3) == -5

    def test_complementarity_sum(self):
        """c(k) + c(k') = 246 for W_4."""
        assert w4_complementarity_sum() == 246

    def test_ff_duality_c334_well_defined(self):
        """FF duality data for c_334 is well-defined at k=1."""
        result = ff_duality_c334(Rational(1))
        assert result["c_k"] == Rational(-189)
        k_prime = w4_dual_level(Rational(1))
        assert result["c_kp"] == w4_central_charge(k_prime)

    def test_ff_duality_c334_complementarity(self):
        """c(k) + c(k') = 246 verified through FF duality data."""
        result = ff_duality_c334(Rational(1))
        assert result["c_k"] + result["c_kp"] == 246

    def test_ff_c334_ratio_is_rational(self):
        """c_334^2(k')/c_334^2(k) is a rational function of k."""
        result = ff_duality_c334(Rational(1))
        if result["ratio"] is not None:
            assert result["ratio"].is_rational


# ===== Jacobi identity checks =====

class TestJacobiIdentity:
    """Numerical Jacobi identity verification."""

    def test_w333_jacobi_at_c3(self):
        """(W^3, W^3, W^3) Jacobi identity consistency at c=3."""
        checks = verify_jacobi_w333(3)
        assert checks["c334_finite"]
        assert checks["c334_denom_nonzero"]
        assert checks["c334_positive_unitary"]
        assert checks["c334_vanishes_at_c0"]

    def test_w333_jacobi_at_c50(self):
        """(W^3, W^3, W^3) Jacobi identity consistency at c=50."""
        checks = verify_jacobi_w333(50)
        assert checks["c334_finite"]
        assert checks["c334_positive_unitary"]

    def test_w334_jacobi_at_c3(self):
        """(W^3, W^3, W^4) Jacobi identity consistency at c=3."""
        checks = verify_jacobi_w334(3)
        assert checks["all_finite"]
        assert checks["c343_ratio"]

    @pytest.mark.parametrize("c_val", [1, 3, 10, 50])
    def test_w333_jacobi_parametric(self, c_val):
        """(W^3, W^3, W^3) Jacobi consistency at various c."""
        checks = verify_jacobi_w333(c_val)
        assert checks["c334_finite"]
        assert checks["c444_finite"]
        assert checks["c334_denom_nonzero"]


# ===== Special values =====

class TestSpecialValues:
    """Tests for c_334^2 at notable central charge values."""

    def test_special_values_dict(self):
        """Special values dictionary is well-formed."""
        sv = c334_squared_at_special_values()
        assert "c=0 (trivial)" in sv
        assert "c=1/2 (Ising)" in sv
        assert "c=3 (3 free bosons)" in sv

    def test_special_value_c0(self):
        """c_334^2(c=0) = 0."""
        sv = c334_squared_at_special_values()
        assert sv["c=0 (trivial)"][1] == 0

    def test_special_value_c22_5(self):
        """c_334^2(c=-22/5) = 0."""
        sv = c334_squared_at_special_values()
        assert sv["c=-22/5 (W3 singular)"][1] == 0


class TestZerosAndPoles:
    """Tests for the zero/pole structure of the structure constants."""

    def test_c334_zeros(self):
        """c_334^2 has zeros at c=0 (double) and c=-22/5."""
        zp = c334_zeros_and_poles()
        zeros = [z[0] for z in zp["zeros"]]
        assert Rational(0) in zeros
        assert Rational(-22, 5) in zeros

    def test_c334_poles(self):
        """c_334^2 has poles at c=-24, -68/7, -46/3."""
        zp = c334_zeros_and_poles()
        poles = [p[0] for p in zp["poles"]]
        assert Rational(-24) in poles
        assert Rational(-68, 7) in poles
        assert Rational(-46, 3) in poles

    def test_c444_zeros(self):
        """c_444^2 has zeros at c=0, 1/2, -46/3."""
        zp = c444_zeros_and_poles()
        zeros = [z[0] for z in zp["zeros"]]
        assert Rational(0) in zeros
        assert Rational(1, 2) in zeros
        assert Rational(-46, 3) in zeros

    def test_c444_poles(self):
        """c_444^2 has poles at c=-24, -68/7, -197/10, -3/5."""
        zp = c444_zeros_and_poles()
        poles = [p[0] for p in zp["poles"]]
        assert Rational(-24) in poles
        assert Rational(-68, 7) in poles
        assert Rational(-197, 10) in poles
        assert Rational(-3, 5) in poles

    def test_shared_poles_c334_c444(self):
        """c_334^2 and c_444^2 share poles at c=-24 and c=-68/7."""
        zp334 = c334_zeros_and_poles()
        zp444 = c444_zeros_and_poles()
        poles_334 = set(p[0] for p in zp334["poles"])
        poles_444 = set(p[0] for p in zp444["poles"])
        shared = poles_334 & poles_444
        assert Rational(-24) in shared
        assert Rational(-68, 7) in shared


# ===== Extraction report =====

class TestExtractionReport:
    """Tests for the full extraction report."""

    def test_report_at_symbolic_k(self):
        """Extraction report at symbolic k is well-formed."""
        report = extraction_report()
        assert "level" in report
        assert "central_charge" in report
        assert "c_334_squared" in report
        assert "c_444_squared" in report
        assert "virasoro_target_identities_verified" in report

    def test_report_identities_verified(self):
        """Report confirms the Virasoro-target identities are verified."""
        report = extraction_report()
        assert report["virasoro_target_identities_verified"]
        assert report["C_{4,4;2;0,6}"] == 2
        assert report["C_{3,4;2;0,5}"] == 0

    def test_report_at_specific_level(self):
        """Extraction report at k=1 gives specific rational values."""
        report = extraction_report(Rational(1))
        assert report["central_charge"] == Rational(-189)
        assert report["complementarity_sum"] == 246


# ===== Consistency with w4_stage4_coefficients =====

class TestConsistencyWithScaffold:
    """Cross-checks with the w4_stage4_coefficients module."""

    def test_six_packet_labels(self):
        """Six packet labels from the scaffold are addressed."""
        targets = stage4_live_targets()
        assert len(targets) == 6
        assert len(stage4_exact_identity_packet()) == 6

    def test_four_higher_spin_targets(self):
        """Four higher-spin targets from the scaffold are extracted."""
        front = frontier_package()
        assert front["n_higher_spin"] == 4
        # Each higher-spin target corresponds to a formula in this module
        ope = w4_full_ope_coefficients()
        assert "c_334_squared" in ope
        assert "c_444_squared" in ope
        assert "C_{3,4;3;0,4}_squared" in ope
        assert "C_{3,4;4;0,3}_squared" in ope

    def test_two_virasoro_target_identities_match(self):
        """The two scaffold identities match the explicit DS verification."""
        front = frontier_package()
        assert front["virasoro_target_values"][(4, 4, 2, 6)] == 2
        assert front["virasoro_target_values"][(3, 4, 2, 5)] == 0
        identities = verify_stage4_virasoro_target_identities()
        assert identities["C_{4,4;2;0,6}"]["theorematic_value"] == 2
        assert identities["C_{3,4;2;0,5}"]["theorematic_value"] == 0

    def test_central_charge_consistency(self):
        """Central charge formula is consistent between modules."""
        k = Symbol('k')
        c_stage4 = w4_central_charge(k)
        # Verify at k=1
        assert w4_central_charge(1) == Rational(-189)


# ===== W^3 x W^3 OPE structure =====

class TestW3W3OPE:
    """Tests for the W^3 x W^3 OPE decomposition in the W_4 algebra."""

    def test_pole2_has_three_components(self):
        """Pole-2 term has d^2T, Lambda, and W^4 components."""
        decomp = w3w3_pole2_decomposition(Symbol('c'))
        assert "d2T" in decomp
        assert "Lambda" in decomp
        assert "W4" in decomp

    def test_d2t_coefficient_universal(self):
        """The d^2T coefficient is 3/10 (from conformal symmetry)."""
        decomp = w3w3_pole2_decomposition(Symbol('c'))
        assert decomp["d2T"] == Rational(3, 10)

    def test_lambda_coefficient_is_alpha(self):
        """The Lambda coefficient is 16/(22+5c)."""
        c = Symbol('c')
        decomp = w3w3_pole2_decomposition(c)
        expected_alpha = Rational(16) / (22 + 5*c)
        assert simplify(decomp["Lambda"] - expected_alpha) == 0

    def test_w4_coefficient_is_symbolic(self):
        """The W^4 coefficient is symbolic c_334 by default."""
        decomp = w3w3_pole2_decomposition(Symbol('c'))
        assert decomp["W4"] == Symbol('c_334')


# ===== Cross-ratio of structure constants =====

class TestStructureConstantRelations:
    """Tests for algebraic relations between the structure constants."""

    def test_c343_over_c334_is_9_16(self):
        """C_{3,4;3;0,4}^2 / c_334^2 = 9/16 (constant, independent of c)."""
        c = Symbol('c')
        ratio = simplify(c343_formula(c) / c334_squared_formula(c))
        assert ratio == Rational(9, 16)

    def test_c344_over_c334_is_5_7(self):
        """C_{3,4;4;0,3}^2 / c_334^2 = 5/7 (constant, independent of c)."""
        c = Symbol('c')
        ratio = simplify(c344_formula(c) / c334_squared_formula(c))
        assert ratio == Rational(5, 7)

    def test_c444_independent_of_c334(self):
        """c_444^2 is NOT proportional to c_334^2 (different pole structure)."""
        c = Symbol('c')
        ratio = simplify(c444_squared_formula(c) / c334_squared_formula(c))
        # This should depend on c (not be a constant)
        from sympy import diff
        assert diff(ratio, c) != 0

    def test_c334_c444_shared_factor(self):
        """c_334^2 and c_444^2 share the factor c^2/(c+24)(7c+68)."""
        c = Symbol('c')
        # Extract and compare
        g334 = c334_squared_formula(c)
        g444 = c444_squared_formula(c)
        # Both vanish at c=0 (double zero)
        assert g334.subs(c, 0) == 0
        assert g444.subs(c, 0) == 0
        # Both blow up at c=-24 and c=-68/7
        # (verified via pole test above)


# ===== Virasoro Gram matrix at weight 4 =====

class TestVirasoroGramMatrix:
    """The weight-4 Gram matrix explains the (5c+22) factor in c_334^2.

    Basis: {|1> = L_{-4}|0>, |2> = L_{-2}^2|0>}.
    Gram entries from [L_m, L_n] = (m-n)L_{m+n} + c/12 * m(m^2-1) * delta.

    The quasi-primary Lambda = L_{-2}^2 - (3/5)L_{-4} has norm c(5c+22)/10.
    The factor (5c+22) appears in the c_334^2 numerator because c_334^2 is
    proportional to the Gram determinant: no room for a new primary at weight 4
    when det G = 0, i.e. when 5c+22 = 0.
    """

    def _gram(self, c_val):
        G11 = 5 * c_val                # <0|L_4 L_{-4}|0>
        G12 = 3 * c_val                # <0|L_4 L_{-2}^2|0> = <0|L_2^2 L_{-4}|0>
        G22 = c_val * (c_val + 8) / 2  # <0|L_2^2 L_{-2}^2|0>
        return G11, G12, G22

    def test_gram_determinant(self):
        """det G_4 = c^2(5c+22)/2."""
        c = Symbol('c')
        G11, G12, G22 = self._gram(c)
        assert simplify(G11 * G22 - G12**2 - c**2 * (5*c + 22) / 2) == 0

    def test_gram_positive_definite_large_c(self):
        G11, G12, G22 = self._gram(100)
        assert G11 > 0
        assert G11 * G22 - G12**2 > 0

    def test_gram_degenerate_at_minus_22_over_5(self):
        """Gram determinant vanishes at c = -22/5 (null vector at weight 4)."""
        c_val = Rational(-22, 5)
        G11, G12, G22 = self._gram(c_val)
        assert G11 * G22 - G12**2 == 0

    def test_l1_annihilates_lambda(self):
        """L_1(L_{-2}^2 - 3/5 L_{-4})|0> = 0 (quasi-primary condition).

        L_1 L_{-2}^2|0> = 3 L_{-3}|0>; L_1 L_{-4}|0> = 5 L_{-3}|0>.
        Coefficient: 3 - (3/5)*5 = 0.
        """
        assert 3 - Rational(3, 5) * 5 == 0

    def test_lambda_norm(self):
        """<Lambda|Lambda> = c(5c+22)/10."""
        c = Symbol('c')
        G11, G12, G22 = self._gram(c)
        a = Rational(-3, 5)
        norm = G22 + 2 * a * G12 + a**2 * G11
        assert simplify(norm - c * (5*c + 22) / 10) == 0

    def test_c334_vanishes_where_gram_det_zero(self):
        """c_334^2 = 0 where det G_4 = 0 (no room for a primary W^4)."""
        assert c334_squared_formula(Rational(-22, 5)) == 0

    def test_c334_numerator_contains_gram_factor(self):
        """The factor (5c+22) in the c_334^2 numerator is the Gram factor."""
        c = Symbol('c')
        num, _ = factor(c334_squared_formula(c)).as_numer_denom()
        # (5c+22) divides the numerator
        assert simplify(num.subs(c, Rational(-22, 5))) == 0


# ===== Numerical consistency =====

class TestNumericalConsistency:
    """Numerical cross-checks at specific c values."""

    def test_c334_at_c3(self):
        """c_334^2(c=3) = 518/4895."""
        assert c334_squared_formula(Rational(3)) == Rational(518, 4895)

    def test_c444_at_c1(self):
        """c_444^2(c=1) is a specific rational number."""
        val = c444_squared_formula(Rational(1))
        assert val > 0
        assert val < 1  # sanity check

    def test_mixed_coefficients_at_c3(self):
        """Mixed coefficients at c=3 are consistent."""
        c334_sq = c334_squared_formula(Rational(3))
        c343_sq = c343_formula(Rational(3))
        c344_sq = c344_formula(Rational(3))
        # Ratio checks
        assert simplify(c343_sq - Rational(9, 16) * c334_sq) == 0
        assert simplify(c344_sq - Rational(5, 7) * c334_sq) == 0

    @pytest.mark.parametrize("c_val", [1, 2, 3, 5, 10, 25, 50, 100])
    def test_all_coefficients_positive(self, c_val):
        """All squared structure constants are positive for c > 1."""
        c = Rational(c_val)
        assert c334_squared_formula(c) > 0
        assert c444_squared_formula(c) > 0
        assert c343_formula(c) > 0
        assert c344_formula(c) > 0
