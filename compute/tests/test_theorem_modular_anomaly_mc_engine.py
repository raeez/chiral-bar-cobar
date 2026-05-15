r"""Focused tests for finite scalar modular-anomaly / MC witnesses.

The owned compute surface verifies exact arity-zero scalar coefficients.
It must not promote those finite checks to full MC reconstruction,
generic moduli proofs, derived-center data, or unrelated kappa slots.
"""

import pytest
from fractions import Fraction

F = Fraction

from compute.lib.theorem_modular_anomaly_mc_engine import (
    # Core invariants
    projection_scope,
    finite_mc_reconstruction_witness,
    genus_moduli_scope_witness,
    anomaly_datum_separation,
    k3xe_kappa_polysemy,
    _bernoulli_exact,
    lambda_fp_independent,
    _ahat_coefficients,
    # MC projection
    mc_projection_genus_g,
    mc_projection_all_genera,
    # Anomaly coefficients
    anomaly_coefficient_direct,
    anomaly_coefficient_gf,
    # Heat equation
    heat_equation_check,
    heat_equation_dressed_check,
    # Non-holomorphic
    non_holomorphic_completion,
    # Sewing
    sewing_trace_genus1,
    propagator_e2star_connection,
    # Ahat identities
    ahat_product_identity,
    ahat_recursion_from_anomaly,
    # Convolution bracket
    convolution_bracket_genus_g,
    # Full theorem
    verify_theorem_all_paths,
    # Cross-family
    cross_family_anomaly_check,
    # Explicit table
    explicit_anomaly_table,
    anomaly_generating_function_coeffs,
    # Multi-weight
    multi_weight_anomaly_correction,
    w3_cross_channel_corrections,
    # Numerical
    e2_quasimodular_qexp,
    numerical_anomaly_check,
    # BCOV comparison
    bcov_original_comparison,
    # Depth tower
    anomaly_depth_tower,
)


# =========================================================================
# Section 0: Scope and conflation guards
# =========================================================================

class TestScopeAndConflationGuards:
    """Finite scalar checks must advertise their missing axes."""

    def test_projection_scope_is_scalar_only(self):
        scope = projection_scope(3, arity=0, finite_depth=1)
        assert scope.stable_range is True
        assert scope.scalar_projection_only is True
        assert scope.can_reconstruct_full_mc is False
        assert "higher arity operations" in scope.missing_axes
        assert "derived-center comparison data" in scope.missing_axes

    def test_finite_checks_do_not_reconstruct_full_mc(self):
        witness = finite_mc_reconstruction_witness(max_genus=6, max_depth=2)
        assert witness["can_reconstruct_full_mc"] is False
        assert witness["claim_status"] == "finite scalar witness only"
        assert "moduli-dependent propagator kernels" in witness["missing_axes"]

    def test_genus_2_generic_moduli_check_is_not_a_proof(self):
        generic = genus_moduli_scope_witness(2, "generic")
        assert generic["stable_closed_arity_zero_range"] is True
        assert generic["generic_period_finite_check_is_proof"] is False
        assert generic["topological_degree_is_dynamic_witness"] is False

    def test_genus_2_diagonal_degenerates_to_genus_1_theorem(self):
        diagonal = genus_moduli_scope_witness(2, "diagonal")
        assert diagonal["diagonal_genus2_degenerates_to_genus1_theorem"] is True
        assert diagonal["generic_period_finite_check_is_proof"] is False

    def test_curvature_and_center_data_are_separate(self):
        data = anomaly_datum_separation(1, F(3))
        assert data["bar_scalar_trace"].value == F(1, 8)
        assert data["quillen_heisenberg_check"].value == F(1, 8)
        assert data["bar_differential_curvature"].value == F(3)
        assert data["arakelov_hodge_curvature"].value is None
        assert data["derived_center_bulk"].value is None
        assert data["derived_center_bulk"].feeds_scalar_anomaly is False

    def test_k3xe_kappa_polysemy_excludes_delta5_from_chiral_slot(self):
        data = k3xe_kappa_polysemy()
        assert data["kappa_ch_heisenberg_K3xE"] == F(3)
        assert data["kappa_bkm_Delta5"] == F(5)
        assert data["kappa_cat_K3xE"] == F(0)
        assert data["bkm_multiplier_is_chiral_modular_anomaly_kappa"] is False

    def test_anomaly_coefficient_requires_stable_genus(self):
        with pytest.raises(ValueError):
            anomaly_coefficient_direct(1, F(1))


# =========================================================================
# Section 1: Core invariant verification
# =========================================================================

class TestCoreInvariants:
    """Verify core invariants by 2+ independent methods."""

    def test_bernoulli_b0(self):
        """B_0 = 1."""
        assert _bernoulli_exact(0) == F(1)

    def test_bernoulli_b1(self):
        """B_1 = -1/2."""
        assert _bernoulli_exact(1) == F(-1, 2)

    def test_bernoulli_b2(self):
        """B_2 = 1/6."""
        assert _bernoulli_exact(2) == F(1, 6)

    def test_bernoulli_b4(self):
        """B_4 = -1/30."""
        assert _bernoulli_exact(4) == F(-1, 30)

    def test_bernoulli_b6(self):
        """B_6 = 1/42."""
        assert _bernoulli_exact(6) == F(1, 42)

    def test_bernoulli_odd_vanish(self):
        """B_n = 0 for odd n >= 3."""
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_exact(n) == F(0), f"B_{n} should vanish"

    def test_lambda1_equals_1_over_24(self):
        r"""lambda_1 = 1/24.

        Path 1: from Bernoulli: (2^1 - 1)|B_2|/(2^1 * 2!) = 1*(1/6)/(2*2) = 1/24.
        Path 2: from Ahat: coefficient of x^2 in (x/2)/sin(x/2) - 1 = 1/24.
        """
        assert lambda_fp_independent(1) == F(1, 24)

    def test_lambda2_equals_7_over_5760(self):
        r"""lambda_2 = 7/5760.

        Path 1: (2^3 - 1)|B_4|/(2^3 * 4!) = 7*(1/30)/(8*24) = 7/5760.
        Path 2: coefficient of x^4 in (x/2)/sin(x/2) - 1.
        """
        assert lambda_fp_independent(2) == F(7, 5760)

    def test_lambda3_equals_31_over_967680(self):
        r"""lambda_3 = 31/967680.

        (2^5 - 1)|B_6|/(2^5 * 6!) = 31*(1/42)/(32*720) = 31/967680.
        """
        assert lambda_fp_independent(3) == F(31, 967680)

    def test_lambda5_equals_73_over_3503554560(self):
        r"""lambda_5 = 73/3503554560 from the Bernoulli formula."""
        assert lambda_fp_independent(5) == F(73, 3503554560)

    def test_ahat_coefficients_match_lambda(self):
        """Ahat coefficients equal lambda_g (two independent methods)."""
        ahat = _ahat_coefficients(6)
        for g in range(1, 7):
            assert ahat[g] == lambda_fp_independent(g), f"Mismatch at g={g}"

    def test_lambda_positivity(self):
        """All lambda_g > 0 for g >= 1."""
        for g in range(1, 10):
            assert lambda_fp_independent(g) > 0, f"lambda_{g} not positive"


# =========================================================================
# Section 2: Path 1 — MC projection tests
# =========================================================================

class TestPath1MCProjection:
    """Verify the MC equation at (g,0) gives the anomaly equation."""

    def test_mc_residual_vanishes_g2(self):
        """MC equation: D + bracket = 0 at genus 2."""
        data = mc_projection_genus_g(2, F(1))
        assert data.mc_residual == F(0)
        assert data.is_consistent is True
        assert data.finite_check_reconstructs_full_mc is False

    def test_mc_residual_vanishes_g3(self):
        """MC equation: D + bracket = 0 at genus 3."""
        data = mc_projection_genus_g(3, F(1))
        assert data.mc_residual == F(0)

    def test_mc_residual_vanishes_g4(self):
        """MC equation: D + bracket = 0 at genus 4."""
        data = mc_projection_genus_g(4, F(1))
        assert data.mc_residual == F(0)

    def test_mc_residual_vanishes_all_genera(self):
        """MC residual vanishes at all genera 2..8."""
        results = mc_projection_all_genera(8, F(1))
        for g, data in results.items():
            assert data.mc_residual == F(0), f"MC residual nonzero at g={g}"
            assert data.is_consistent is True

    def test_anomaly_lhs_equals_rhs_g2(self):
        """Anomaly LHS = RHS at genus 2."""
        data = mc_projection_genus_g(2, F(1))
        assert data.anomaly_lhs == data.anomaly_rhs

    def test_anomaly_lhs_equals_rhs_all_genera(self):
        """Anomaly LHS = RHS at all genera 2..8."""
        results = mc_projection_all_genera(8, F(1))
        for g, data in results.items():
            assert data.anomaly_lhs == data.anomaly_rhs, f"Anomaly mismatch at g={g}"

    def test_bracket_is_convolution_square(self):
        r"""[Theta,Theta]^{(g,0)} = sum F_h F_{g-h} at genus 3.

        The bracket sums over genus splittings: (1,2) and (2,1).
        """
        data = convolution_bracket_genus_g(3, F(1))
        expected = lambda_fp_independent(1) * lambda_fp_independent(2) * 2
        assert data['bracket_sum'] == expected

    def test_mc_kappa_scaling(self):
        """MC projection scales as kappa^2 in the bracket term."""
        for kappa in [F(1), F(2), F(1, 2), F(5)]:
            data = mc_projection_genus_g(3, kappa)
            data_unit = mc_projection_genus_g(3, F(1))
            assert data.bracket_term == kappa ** 2 * data_unit.bracket_term

    def test_mc_bracket_half_normalizes_to_anomaly_by_factor_12(self):
        """(1/2)[Theta,Theta] is 12 times the normalized anomaly coefficient."""
        data = mc_projection_genus_g(4, F(1))
        assert data.mc_to_anomaly_factor == F(12)
        assert data.bracket_term == F(12) * data.anomaly_rhs
        assert data.scope.can_reconstruct_full_mc is False


# =========================================================================
# Section 3: Path 2 — Generating function convolution tests
# =========================================================================

class TestPath2GFConvolution:
    """Verify the Ahat product identity underlying the anomaly."""

    def test_direct_equals_gf_g2(self):
        """Direct and GF anomaly coefficients agree at genus 2."""
        d = anomaly_coefficient_direct(2, F(1))
        gf = anomaly_coefficient_gf(2, F(1))
        assert d == gf

    def test_direct_equals_gf_all_genera(self):
        """Direct and GF anomaly coefficients agree at all genera."""
        for g in range(2, 9):
            d = anomaly_coefficient_direct(g, F(1))
            gf = anomaly_coefficient_gf(g, F(1))
            assert d == gf, f"Mismatch at g={g}"

    def test_ahat_product_identity_all(self):
        """The Ahat product identity holds at all genera."""
        result = ahat_product_identity(8)
        assert result['all_match'] is True

    def test_anomaly_g2_explicit(self):
        r"""c_2 = (1/24) * lambda_1^2 = (1/24)*(1/24)^2 = 1/13824.

        Three independent paths:
        Path 1: direct formula.
        Path 2: GF convolution.
        Path 3: explicit computation: (1/24) * (1/576) = 1/13824.
        """
        expected = F(1, 24) * F(1, 24) ** 2  # (1/24)*(1/24)^2
        # = 1 / (24 * 576) = 1/13824
        assert expected == F(1, 13824)

        direct = anomaly_coefficient_direct(2, F(1))
        assert direct == expected

        gf = anomaly_coefficient_gf(2, F(1))
        assert gf == expected

    def test_anomaly_g3_explicit(self):
        r"""c_3 = (1/24) * 2*lambda_1*lambda_2.

        lambda_1*lambda_2 = (1/24)*(7/5760) = 7/138240
        2*lambda_1*lambda_2 = 7/69120
        c_3 = 7/69120/24 = 7/1658880
        """
        l1 = lambda_fp_independent(1)
        l2 = lambda_fp_independent(2)
        expected = F(2) * l1 * l2 / F(24)
        assert expected == F(7, 1658880)
        direct = anomaly_coefficient_direct(3, F(1))
        assert direct == expected

    def test_gf_coefficients_match_table(self):
        """GF coefficients match the explicit anomaly table."""
        gf_coeffs = anomaly_generating_function_coeffs(6)
        table = explicit_anomaly_table(6)
        for g in range(2, 7):
            assert gf_coeffs[g] == table[g]['anomaly_coefficient'], \
                f"Mismatch at g={g}"

    def test_ahat_recursion_reproduces_lambda(self):
        """Anomaly recursion (from sine relation) reproduces all lambda_g."""
        result = ahat_recursion_from_anomaly(8)
        assert result['all_match'] is True


# =========================================================================
# Section 4: Path 3 — Heat equation / integrability tests
# =========================================================================

class TestPath3HeatEquation:
    """Verify finite Leibniz consistency of the anomaly recursion."""

    def test_heat_consistent_g2(self):
        """Heat equation consistent at genus 2."""
        h = heat_equation_check(2, F(1))
        assert h.is_consistent is True
        assert h.scalar_level_is_trivial is True
        assert h.proves_full_d_squared_zero is False

    def test_heat_consistent_all_genera(self):
        """Heat equation consistent at all genera."""
        for g in range(2, 9):
            h = heat_equation_check(g, F(1))
            assert h.is_consistent is True

    def test_dressed_heat_g3(self):
        """Dressed heat equation (depth-2 integrability) at genus 3."""
        dh = heat_equation_dressed_check(3, F(1))
        assert dh['integrability_holds'] is True
        assert dh['proves_full_d_squared_zero'] is False
        assert dh['scope'].can_reconstruct_full_mc is False

    def test_dressed_heat_g4(self):
        """Dressed heat equation at genus 4."""
        dh = heat_equation_dressed_check(4, F(1))
        assert dh['integrability_holds'] is True

    def test_dressed_heat_g5(self):
        """Dressed heat equation at genus 5."""
        dh = heat_equation_dressed_check(5, F(1))
        assert dh['integrability_holds'] is True

    def test_dressed_heat_g6(self):
        """Dressed heat equation at genus 6."""
        dh = heat_equation_dressed_check(6, F(1))
        assert dh['integrability_holds'] is True

    def test_dressed_heat_various_kappa(self):
        """Dressed heat equation holds for various kappa values."""
        for kappa in [F(1), F(1, 2), F(5), F(13)]:
            for g in range(3, 6):
                dh = heat_equation_dressed_check(g, kappa)
                assert dh['integrability_holds'] is True, \
                    f"Failed at g={g}, kappa={kappa}"


# =========================================================================
# Section 5: Path 4 — Non-holomorphic completion tests
# =========================================================================

class TestPath4NonHolomorphic:
    """Verify the finite non-holomorphic coefficient without overclaiming."""

    def test_nh_modular_invariant_g2(self):
        """The depth-1 coefficient is formal, not a proof of modularity."""
        nh = non_holomorphic_completion(2, F(1))
        assert nh.completion_is_formal is True
        assert nh.is_modular_invariant is False
        assert nh.finite_coefficient_proves_modularity is False

    def test_nh_modular_invariant_all_genera(self):
        """No finite coefficient is promoted to full modular invariance."""
        for g in range(2, 9):
            nh = non_holomorphic_completion(g, F(1))
            assert nh.is_modular_invariant is False
            assert nh.finite_coefficient_proves_modularity is False

    def test_nh_correction_proportional_to_anomaly(self):
        """The nh correction is -3 times the holomorphic anomaly coefficient."""
        for g in range(2, 7):
            nh = non_holomorphic_completion(g, F(1))
            anomaly = anomaly_coefficient_direct(g, F(1))
            assert nh.nh_correction_prefactor == -F(3) * anomaly


# =========================================================================
# Section 6: Sewing operator and propagator tests
# =========================================================================

class TestSewingPropagator:
    """Verify the sewing operator trace and propagator normalization."""

    def test_sewing_trace_g1(self):
        r"""Tr(S_sew) = kappa/24 at genus 1.

        This is F_1 = kappa * lambda_1 = kappa/24.
        """
        for kappa in [F(1), F(5), F(1, 2), F(13, 2)]:
            trace = sewing_trace_genus1(kappa)
            assert trace == kappa / F(24)

    def test_propagator_coefficient(self):
        """Propagator P = -E_2*/12."""
        data = propagator_e2star_connection(F(1))
        assert data['propagator_coefficient'] == F(-1, 12)

    def test_anomaly_prefactor_is_1_over_24(self):
        """The anomaly prefactor 1/24 = (1/12)*(1/2)."""
        data = propagator_e2star_connection(F(1))
        assert data['anomaly_prefactor'] == F(1, 24)
        assert data['propagator_coefficient'] * (-F(1)) * data['sewing_normalization'] \
            == F(1, 24)


# =========================================================================
# Section 7: Cross-family consistency tests (Path 5)
# =========================================================================

class TestPath5CrossFamily:
    """Verify anomaly scales as kappa^2 across families."""

    def test_cross_family_all_ratios(self):
        """All cross-family kappa^2 ratios are correct."""
        result = cross_family_anomaly_check()
        assert result['all_ratios_correct'] is True
        assert result['families']['K3xE_chiral_heisenberg_shadow']['kappa'] == F(3)
        assert result['excluded_non_chiral_kappas']['Delta5_BKM_multiplier'] == F(5)

    def test_anomaly_quadratic_in_kappa(self):
        """c_g(2*kappa) = 4*c_g(kappa) for all g."""
        for g in range(2, 7):
            c_k = anomaly_coefficient_direct(g, F(1))
            c_2k = anomaly_coefficient_direct(g, F(2))
            assert c_2k == F(4) * c_k, f"Quadratic scaling fails at g={g}"

    def test_anomaly_virasoro_c26(self):
        r"""Virasoro at c=26 (critical): kappa = 13, c_2 = 169/13824.

        kappa^2 = 169, c_2 = 169/13824.
        """
        c_2 = anomaly_coefficient_direct(2, F(13))
        assert c_2 == F(169, 13824)

    def test_anomaly_selfdual_c13(self):
        """Virasoro at c=13 (self-dual): kappa = 13/2."""
        c_2 = anomaly_coefficient_direct(2, F(13, 2))
        expected = F(13, 2) ** 2 * lambda_fp_independent(1) ** 2 / F(24)
        assert c_2 == expected

    def test_delta5_multiplier_not_used_as_k3xe_chiral_anomaly(self):
        """The BKM multiplier 5 is not the K3 x E chiral anomaly kappa."""
        result = cross_family_anomaly_check()
        assert 'K3xE' not in result['families']
        assert result['families']['K3xE_chiral_heisenberg_shadow']['kappa'] == F(3)


# =========================================================================
# Section 8: BCOV comparison tests (Path 6)
# =========================================================================

class TestPath6BCOVComparison:
    """Verify agreement with original BCOV formulation."""

    def test_bcov_match_g2(self):
        """Our anomaly matches BCOV at genus 2."""
        result = bcov_original_comparison(2, F(1))
        assert result['match'] is True
        assert result['full_bcov_reconstruction'] is False

    def test_bcov_match_g3(self):
        """Our anomaly matches BCOV at genus 3."""
        result = bcov_original_comparison(3, F(1))
        assert result['match'] is True

    def test_bcov_match_all_genera(self):
        """Our anomaly matches BCOV at all genera 2..8."""
        for g in range(2, 9):
            result = bcov_original_comparison(g, F(1))
            assert result['match'] is True, f"BCOV mismatch at g={g}"

    def test_bcov_dilaton_arity(self):
        """The dilaton term lives at arity 2, not arity 0."""
        result = bcov_original_comparison(3, F(1))
        assert result['dilaton_term_arity'] == 2


# =========================================================================
# Section 9: Depth tower tests (Path 8)
# =========================================================================

class TestDepthTower:
    """Verify the iterated anomaly depth tower."""

    def test_depth0_is_scalar(self):
        """Depth 0 = kappa * lambda_g (scalar amplitude)."""
        for g in range(1, 7):
            tower = anomaly_depth_tower(g, F(1))
            assert tower['depth_coefficients'][0] == lambda_fp_independent(g)
            assert tower['finite_check_reconstructs_full_mc'] is False

    def test_depth1_is_anomaly(self):
        """Depth 1 = anomaly coefficient."""
        for g in range(2, 7):
            tower = anomaly_depth_tower(g, F(1))
            anomaly = anomaly_coefficient_direct(g, F(1))
            assert tower['depth_coefficients'][1] == anomaly

    def test_depth2_g3(self):
        """Depth 2 at genus 3 = triple convolution / 24^2."""
        tower = anomaly_depth_tower(3, F(1), max_depth=2)
        # Triple convolution at g=3: partitions (1,1,1)
        triple = lambda_fp_independent(1) ** 3
        expected = triple / F(24) ** 2
        assert tower['depth_coefficients'][2] == expected

    def test_depth2_g4(self):
        """Depth 2 at genus 4 from triple convolution."""
        tower = anomaly_depth_tower(4, F(1), max_depth=2)
        # Partitions of 4 into 3 parts >= 1: (1,1,2), (2,1,1), (1,2,1)
        # = 3 * lambda_1^2 * lambda_2
        l1 = lambda_fp_independent(1)
        l2 = lambda_fp_independent(2)
        triple = F(3) * l1 ** 2 * l2
        expected = triple / F(24) ** 2
        assert tower['depth_coefficients'][2] == expected

    def test_depth_tower_kappa_power(self):
        r"""Depth p coefficient scales as kappa^{p+1}."""
        for p in range(3):
            tower_1 = anomaly_depth_tower(4, F(1), max_depth=p)
            tower_2 = anomaly_depth_tower(4, F(2), max_depth=p)
            if tower_1['depth_coefficients'].get(p, F(0)) != F(0):
                ratio = tower_2['depth_coefficients'][p] / tower_1['depth_coefficients'][p]
                assert ratio == F(2) ** (p + 1), \
                    f"kappa scaling fails at depth {p}: expected {2**(p+1)}, got {ratio}"


# =========================================================================
# Section 10: Full theorem verification
# =========================================================================

class TestFullTheorem:
    """Integration tests for the finite scalar verification surface."""

    def test_all_paths_kappa_1(self):
        """All 4 paths agree for kappa = 1."""
        result = verify_theorem_all_paths(F(1), max_genus=6)
        assert result.path1_mc_projection is True
        assert result.path2_gf_convolution is True
        assert result.path3_heat_integrability is True
        assert result.path4_nh_completion is True
        assert result.all_paths_agree is True
        assert result.full_mc_reconstructed is False
        assert result.details['full_mc_reconstruction']['can_reconstruct_full_mc'] is False

    def test_all_paths_kappa_half(self):
        """All 4 paths agree for kappa = 1/2 (Virasoro c=1)."""
        result = verify_theorem_all_paths(F(1, 2), max_genus=6)
        assert result.all_paths_agree is True

    def test_all_paths_kappa_5(self):
        """All finite scalar paths agree for kappa = 5 as a formal input."""
        result = verify_theorem_all_paths(F(5), max_genus=6)
        assert result.all_paths_agree is True
        assert result.full_mc_reconstructed is False

    def test_all_paths_kappa_13(self):
        """All 4 paths agree for kappa = 13 (Virasoro c=26, critical)."""
        result = verify_theorem_all_paths(F(13), max_genus=6)
        assert result.all_paths_agree is True

    def test_recursion_from_anomaly(self):
        """The independent sine recursion reproduces Ahat coefficients."""
        result = verify_theorem_all_paths(F(1), max_genus=8)
        assert result.details['recursion_from_anomaly'] is True


# =========================================================================
# Section 11: Multi-weight anomaly correction tests
# =========================================================================

class TestMultiWeight:
    """Verify multi-weight corrections are not erased by scalar formulas."""

    def test_mc_holds_with_correction(self):
        """A nonzero correction changes the arity-zero anomaly coefficient."""
        corrections = {2: F(5)}
        result = multi_weight_anomaly_correction(3, F(1), cross_corrections=corrections)
        assert result['cross_channel_correction'] != F(0)
        assert result['total_anomaly'] != result['scalar_anomaly']
        assert result['mc_still_holds'] == 'not certified by scalar coefficient check'
        assert result['full_mc_reconstruction'] is False

    def test_scalar_anomaly_matches(self):
        """Scalar anomaly matches the direct computation."""
        for g in range(2, 7):
            result = multi_weight_anomaly_correction(g, F(1))
            direct = anomaly_coefficient_direct(g, F(1))
            assert result['scalar_anomaly'] == direct
            assert result['total_anomaly'] == direct
            assert result['scalar_formula_complete'] is True

    def test_w3_cross_channel_corrections_are_exact(self):
        """The W_3 delta F_2 and delta F_3 formulas are exact rationals."""
        corrections = w3_cross_channel_corrections(F(6))
        assert corrections[2] == F(35, 16)
        expected_delta3 = (
            F(5) * F(6) ** 3
            + F(3792) * F(6) ** 2
            + F(1149120) * F(6)
            + F(217071360)
        ) / (F(138240) * F(6) ** 2)
        assert corrections[3] == expected_delta3

    def test_w3_delta_f2_changes_genus3_anomaly(self):
        """delta F_2 contributes first to the genus-3 anomaly."""
        corrections = w3_cross_channel_corrections(F(6))
        result = multi_weight_anomaly_correction(
            3, F(5), cross_corrections={2: corrections[2]}
        )
        expected_extra = F(2) * (F(5) * lambda_fp_independent(1)) * corrections[2] / F(24)
        assert result['cross_channel_correction'] == expected_extra


# =========================================================================
# Section 12: Numerical cross-check tests
# =========================================================================

class TestNumericalCrossCheck:
    """Numerical cross-checks of the anomaly equation."""

    def test_numerical_g2(self):
        """Numerical anomaly coefficient at genus 2."""
        result = numerical_anomaly_check(1.0, 2)
        expected = float(anomaly_coefficient_direct(2, F(1)))
        assert abs(result['anomaly_coefficient'] - expected) < 1e-15

    def test_numerical_g3(self):
        """Numerical anomaly coefficient at genus 3."""
        result = numerical_anomaly_check(1.0, 3)
        expected = float(anomaly_coefficient_direct(3, F(1)))
        assert abs(result['anomaly_coefficient'] - expected) < 1e-15

    def test_numerical_kappa_5(self):
        """Numerical anomaly for the formal scalar input kappa = 5."""
        result = numerical_anomaly_check(5.0, 2)
        expected = float(anomaly_coefficient_direct(2, F(5)))
        assert abs(result['anomaly_coefficient'] - expected) < 1e-12
        assert result['finite_check_reconstructs_full_mc'] is False

    def test_e2_qexp_uses_complex_q_powers(self):
        """E_2* at tau=1/4+i has a nonzero imaginary q-expansion part."""
        value = e2_quasimodular_qexp(0.25 + 1.0j, terms=4)
        assert abs(value.imag) > 0


# =========================================================================
# Section 13: Convolution bracket structure tests
# =========================================================================

class TestConvolutionBracket:
    """Verify the structure of [Theta,Theta] at (g,0)."""

    def test_bracket_g2_single_term(self):
        """At genus 2, the bracket has one term: (1,1)."""
        data = convolution_bracket_genus_g(2, F(1))
        assert len(data['individual_terms']) == 1
        assert (1, 1) in data['individual_terms']

    def test_bracket_g3_two_terms(self):
        """At genus 3, the bracket has two terms: (1,2) and (2,1)."""
        data = convolution_bracket_genus_g(3, F(1))
        assert len(data['individual_terms']) == 2

    def test_bracket_g4_three_terms(self):
        """At genus 4, the bracket has three terms: (1,3), (2,2), (3,1)."""
        data = convolution_bracket_genus_g(4, F(1))
        assert len(data['individual_terms']) == 3

    def test_bracket_symmetry(self):
        """The bracket sum is symmetric: contribution from (h,g-h) = (g-h,h)."""
        data = convolution_bracket_genus_g(5, F(1))
        terms = data['individual_terms']
        for (h, gh) in terms:
            if h != gh:
                assert terms[(h, gh)] == terms[(gh, h)]

    def test_mc_bracket_half_equals_anomaly_times_12(self):
        r"""(1/2)[Theta,Theta]^{(g,0)} = 12 * (anomaly coefficient at kappa=1).

        Because: mc_bracket/2 = (1/2)*sum F_h F_{g-h}
        anomaly = (1/24)*sum F_h F_{g-h}
        So mc_bracket/2 = 12 * anomaly.
        """
        for g in range(2, 7):
            data = convolution_bracket_genus_g(g, F(1))
            anomaly = anomaly_coefficient_direct(g, F(1))
            assert data['mc_bracket_half'] == F(12) * anomaly
            assert data['finite_check_reconstructs_full_mc'] is False


# =========================================================================
# Section 14: Explicit anomaly table tests
# =========================================================================

class TestExplicitTable:
    """Verify the explicit anomaly coefficient table."""

    def test_table_g2(self):
        """Genus 2 anomaly = 1/13824."""
        table = explicit_anomaly_table(2)
        assert table[2]['anomaly_coefficient'] == F(1, 13824)

    def test_table_g3(self):
        """Genus 3 anomaly = 7/1658880."""
        table = explicit_anomaly_table(3)
        assert table[3]['anomaly_coefficient'] == F(7, 1658880)

    def test_table_g2_single_term(self):
        """Genus 2 has one distinct term."""
        table = explicit_anomaly_table(2)
        assert table[2]['num_distinct_terms'] == 1

    def test_table_internal_consistency(self):
        """Table convolution sums are 24 times the anomaly coefficients."""
        table = explicit_anomaly_table(6)
        for g in range(2, 7):
            assert table[g]['convolution_sum'] == F(24) * table[g]['anomaly_coefficient']

    def test_gf_coefficients_zero_at_g0_g1(self):
        """Anomaly GF has zero coefficients at genus 0 and 1."""
        coeffs = anomaly_generating_function_coeffs(5)
        assert coeffs[0] == F(0)
        assert coeffs[1] == F(0)

    def test_gf_coefficients_nonzero_g2_plus(self):
        """Anomaly GF has nonzero coefficients at genus >= 2."""
        coeffs = anomaly_generating_function_coeffs(6)
        for g in range(2, 7):
            assert coeffs[g] > F(0), f"c_{g} should be positive"
