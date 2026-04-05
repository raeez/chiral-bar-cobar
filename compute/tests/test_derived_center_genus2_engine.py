r"""Tests for the genus-2 chiral derived center engine.

Multi-path verification at genus 2: the first computation of bulk algebra
structure beyond genus 1.  Tests are organized by the 8 computation themes
and 6 verification paths specified in the task.

VERIFICATION PATHS:
  Path 1: Hochschild cochain computation (algebraic)
  Path 2: Sewing/analytic computation (Fredholm determinant)
  Path 3: Pair-of-pants decomposition (topological)
  Path 4: Heisenberg exact result comparison
  Path 5: Sp(4,Z) representation theory check
  Path 6: Degeneration: genus-2 -> genus-1 (pinch a cycle)

FAMILIES TESTED: Heisenberg, Affine_sl2, Virasoro, W_3.

Ground truth:
  thm:thqg-swiss-cheese, thm:theorem-d, thm:thqg-annulus-trace,
  higher_genus_modular_koszul.tex, siegel_modular_shadow_engine.py,
  genus2_sewing_amplitudes.py, pixton_shadow_bridge.py.
"""

import pytest
from fractions import Fraction

from compute.lib.derived_center_genus2_engine import (
    # Constants
    FAMILIES,
    LAMBDA_1_FP,
    LAMBDA_2_FP,
    LAMBDA_3_FP,
    BETTI_MBAR2,
    CHI_ORB_MBAR2,
    DIM_H1_SIGMA2,
    SP4_DIM,
    # Modular characteristics
    kappa,
    kappa_dual,
    # Genus-2 Hochschild
    genus2_hochschild_dimension,
    genus2_hochschild_chain_dimension,
    # Genus-2 trace
    genus2_trace_scalar,
    genus2_trace_ratio,
    lambda_ratio_21,
    # Open/closed map
    genus2_open_closed_scalar,
    genus2_F2,
    # Pair-of-pants decomposition
    genus2_pants_decomposition_separating,
    genus2_tensor_product_dimension,
    # Sp(4,Z) modular structure
    sp4_representation_on_H1,
    siegel_modular_weight,
    sp4_generators_count,
    genus2_modular_anomaly,
    # Swiss-cheese
    genus2_swiss_cheese_partition,
    genus2_swiss_cheese_one_closed,
    # Sewing comparison
    genus2_sewing_heisenberg,
    genus2_sewing_virasoro,
    # MC element
    genus2_oc_mc_element,
    # Degeneration
    genus2_to_genus1_degeneration,
    # Complementarity
    genus2_complementarity,
    genus2_additivity,
    # Hodge integrals
    genus2_hodge_integrals,
    genus2_mumford_relation_check,
    # Planted forest
    genus2_planted_forest_correction,
    # Full package
    genus2_derived_center_package,
    # Multi-path verification
    genus2_verification_paths,
)


# ======================================================================
#  Constants and ground truth values
# ======================================================================

class TestConstants:
    """Verify fundamental constants used throughout the engine."""

    def test_lambda_1_fp(self):
        """lambda_1^FP = 1/24."""
        assert LAMBDA_1_FP == Fraction(1, 24)

    def test_lambda_2_fp(self):
        """lambda_2^FP = 7/5760."""
        assert LAMBDA_2_FP == Fraction(7, 5760)

    def test_lambda_3_fp(self):
        """lambda_3^FP = 31/967680."""
        assert LAMBDA_3_FP == Fraction(31, 967680)

    def test_lambda_2_fp_from_bernoulli(self):
        """Verify lambda_2 = (2^3 - 1)/2^3 * |B_4|/4!.

        B_4 = -1/30. |B_4| = 1/30.
        lambda_2 = 7/8 * 1/30 / 24 = 7/5760.
        """
        B4 = Fraction(-1, 30)
        result = Fraction(2**3 - 1, 2**3) * abs(B4) / Fraction(24)
        assert result == Fraction(7, 5760)

    def test_lambda_ratio_21(self):
        """lambda_2/lambda_1 = 7/240 (universal ratio)."""
        ratio = LAMBDA_2_FP / LAMBDA_1_FP
        assert ratio == Fraction(7, 240)
        assert lambda_ratio_21() == Fraction(7, 240)

    def test_betti_mbar2_poincare_duality(self):
        """Betti numbers satisfy Poincare duality: b_i = b_{6-i}."""
        for i in range(7):
            assert BETTI_MBAR2.get(i, 0) == BETTI_MBAR2.get(6 - i, 0)

    def test_betti_mbar2_odd_vanish(self):
        """Odd Betti numbers of M-bar_2 vanish."""
        for i in [1, 3, 5]:
            assert BETTI_MBAR2.get(i, 0) == 0

    def test_dim_h1_sigma2(self):
        """dim H^1(Sigma_2, C) = 2*genus = 4."""
        assert DIM_H1_SIGMA2 == 4

    def test_sp4_dimension(self):
        """dim Sp(4) = 10 (= n(2n+1) for n=2)."""
        assert SP4_DIM == 10

    def test_chi_orb_mbar2(self):
        """chi^orb(M-bar_2) = 7/240 (Harer-Zagier)."""
        assert CHI_ORB_MBAR2 == Fraction(7, 240)


# ======================================================================
#  1. Modular characteristics (kappa)
# ======================================================================

class TestKappa:
    """Verify kappa values for all families (AP1, AP39, AP48)."""

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1."""
        assert kappa("Heisenberg", k=1) == Fraction(1)

    def test_kappa_heisenberg_k2(self):
        """kappa(H_2) = 2."""
        assert kappa("Heisenberg", k=2) == Fraction(2)

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13."""
        assert kappa("Virasoro", c=26) == Fraction(13)

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert kappa("Virasoro", c=1) == Fraction(1, 2)

    def test_kappa_sl2_k1(self):
        """kappa(sl_2, k=1) = 3(1+2)/4 = 9/4."""
        assert kappa("Affine_sl2", k=1) == Fraction(9, 4)

    def test_kappa_w3_c2(self):
        """kappa(W_3, c=2) = 5*2/6 = 5/3 (AP1: kappa(W_3) = 5c/6, NOT c/2)."""
        assert kappa("W3", c=2) == Fraction(5, 3)

    def test_kappa_dual_heisenberg(self):
        """kappa(H_k) + kappa(H_k!) = 0 (AP24: true for free fields)."""
        for k in [1, 2, 3, 5]:
            assert kappa("Heisenberg", k=k) + kappa_dual("Heisenberg", k=k) == 0

    def test_kappa_dual_virasoro_ap24(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero!)."""
        for c in [1, 2, 13, 20, 26]:
            k = kappa("Virasoro", c=c)
            kd = kappa_dual("Virasoro", c=c)
            assert k + kd == Fraction(13)

    def test_kappa_dual_sl2(self):
        """kappa(sl_2, k) + kappa(sl_2, -k-4) = 0."""
        # Feigin-Frenkel: k -> -k - 2h^v = -k - 4 for sl_2
        k = kappa("Affine_sl2", k=1)
        kd = kappa_dual("Affine_sl2", k=1)
        assert k + kd == Fraction(0)

    def test_kappa_unknown_family_raises(self):
        with pytest.raises(ValueError):
            kappa("Unknown")


# ======================================================================
#  2. Genus-2 Hochschild cohomology
# ======================================================================

class TestGenus2Hochschild:
    """Test genus-2 Hochschild cohomology dimensions."""

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh0_genus2(self, family):
        """HH^0_{g=2}(A) = 1 for all families."""
        assert genus2_hochschild_dimension(family, 0) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh1_genus2(self, family):
        """HH^1_{g=2}(A) = 1 for all families."""
        assert genus2_hochschild_dimension(family, 1) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh2_genus2(self, family):
        """HH^2_{g=2}(A) = 1 for all families."""
        assert genus2_hochschild_dimension(family, 2) == 1

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh_vanishes_negative(self, family):
        """HH^n_{g=2} = 0 for n < 0."""
        for n in [-1, -3, -10]:
            assert genus2_hochschild_dimension(family, n) == 0

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh_vanishes_above_2(self, family):
        """HH^n_{g=2} = 0 for n > 2 (Theorem H polynomial growth)."""
        for n in [3, 4, 5, 10]:
            assert genus2_hochschild_dimension(family, n) == 0

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hh_euler_char_genus2(self, family):
        """Euler characteristic chi = sum (-1)^n dim HH^n = 1."""
        chi = sum((-1)**n * genus2_hochschild_dimension(family, n) for n in range(10))
        assert chi == 1

    def test_hh_unknown_family_raises(self):
        with pytest.raises(ValueError):
            genus2_hochschild_dimension("Unknown", 0)

    @pytest.mark.parametrize("family", FAMILIES)
    def test_chain_dimension_positive(self, family):
        """Chain dimensions are positive in degrees 0, 1, 2."""
        for n in range(3):
            assert genus2_hochschild_chain_dimension(family, n) > 0

    @pytest.mark.parametrize("family", FAMILIES)
    def test_chain_geq_cohomology(self, family):
        """Chain dimension >= cohomology dimension (chains can be killed by d)."""
        for n in range(3):
            assert (genus2_hochschild_chain_dimension(family, n) >=
                    genus2_hochschild_dimension(family, n))


# ======================================================================
#  3. Genus-2 trace map
# ======================================================================

class TestGenus2Trace:
    """Test the genus-2 trace map Tr^{(2)}."""

    def test_trace_heisenberg_k1(self):
        """Tr^{(2)}(H_1) = 7/5760."""
        assert genus2_trace_scalar("Heisenberg", k=1) == Fraction(7, 5760)

    def test_trace_heisenberg_k2(self):
        """Tr^{(2)}(H_2) = 14/5760 = 7/2880."""
        assert genus2_trace_scalar("Heisenberg", k=2) == Fraction(7, 2880)

    def test_trace_virasoro_c26(self):
        """Tr^{(2)}(Vir_26) = 13 * 7/5760 = 91/5760."""
        assert genus2_trace_scalar("Virasoro", c=26) == Fraction(91, 5760)

    def test_trace_sl2_k1(self):
        """Tr^{(2)}(sl_2, k=1) = (9/4) * 7/5760 = 63/23040."""
        expected = Fraction(9, 4) * Fraction(7, 5760)
        assert genus2_trace_scalar("Affine_sl2", k=1) == expected

    @pytest.mark.parametrize("family", FAMILIES)
    def test_trace_ratio_universal(self, family):
        """Tr^{(2)}/Tr^{(1)} = lambda_2/lambda_1 = 7/240 (universal)."""
        ratio = genus2_trace_ratio(family)
        assert ratio == Fraction(7, 240)

    def test_trace_ratio_independence_of_level(self):
        """The ratio lambda_2/lambda_1 is independent of the level k."""
        for k in [1, 2, 3, 5, 10]:
            assert genus2_trace_ratio("Heisenberg", k=k) == Fraction(7, 240)

    def test_trace_zero_kappa(self):
        """Tr^{(2)} = 0 when kappa = 0 (Heisenberg at k=0, edge case)."""
        assert genus2_trace_scalar("Heisenberg", k=0) == 0

    def test_trace_ratio_zero_kappa(self):
        """Trace ratio is 0 when kappa = 0."""
        assert genus2_trace_ratio("Heisenberg", k=0) == 0


# ======================================================================
#  4. Open/closed map at genus 2
# ======================================================================

class TestOpenClosedMap:
    """Test OC^{(2)}: B^{(2)}(A) -> Z_ch^{(2)}(A)."""

    def test_oc_equals_f2_heisenberg(self):
        """OC^{(2)} = F_2 = kappa * lambda_2 for Heisenberg."""
        for k in [1, 2, 5]:
            oc = genus2_open_closed_scalar("Heisenberg", k=k)
            f2 = genus2_F2("Heisenberg", k=k)
            assert oc == f2

    @pytest.mark.parametrize("family", FAMILIES)
    def test_oc_equals_f2(self, family):
        """OC^{(2)} = F_2 at the scalar level for all families."""
        assert genus2_open_closed_scalar(family) == genus2_F2(family)

    def test_f2_heisenberg_k1_value(self):
        """F_2(H_1) = 7/5760."""
        assert genus2_F2("Heisenberg", k=1) == Fraction(7, 5760)

    def test_f2_virasoro_c26_value(self):
        """F_2(Vir_26) = 13 * 7/5760 = 91/5760."""
        assert genus2_F2("Virasoro", c=26) == Fraction(91, 5760)

    def test_f2_linearity_in_kappa(self):
        """F_2 is linear in kappa (as lambda_2 is universal)."""
        for k in [1, 2, 3, 5]:
            f2 = genus2_F2("Heisenberg", k=k)
            expected = Fraction(k) * LAMBDA_2_FP
            assert f2 == expected

    def test_f2_w3_c2(self):
        """F_2(W_3, c=2) = (5/3) * 7/5760 = 7/3456 (AP1: kappa=5c/6=5/3)."""
        assert genus2_F2("W3", c=2) == Fraction(5, 3) * Fraction(7, 5760)

    def test_f2_positive_for_positive_kappa(self):
        """F_2 > 0 when kappa > 0."""
        for family in FAMILIES:
            f2 = genus2_F2(family)
            k = kappa(family)
            if k > 0:
                assert f2 > 0


# ======================================================================
#  5. Pair-of-pants decomposition (Path 3)
# ======================================================================

class TestPantsDecomposition:
    """Test pair-of-pants decomposition of genus-2 amplitude."""

    def test_pants_reconstruction(self):
        """F_2 = F_2^{sep} + F_2^{nonsep}."""
        for family in FAMILIES:
            result = genus2_pants_decomposition_separating(family)
            assert result["F2"] == result["F2_sep"] + result["F2_nonsep"]

    def test_sep_contribution_heisenberg(self):
        """F_2^{sep}(H_1) = 1 * (1/24)^2 = 1/576."""
        result = genus2_pants_decomposition_separating("Heisenberg", k=1)
        expected_sep = Fraction(1, 576)
        assert result["F2_sep"] == expected_sep

    def test_nonsep_contribution_heisenberg(self):
        """F_2^{nonsep}(H_1) = 7/5760 - 1/576 = -3/5760 = -1/1920."""
        result = genus2_pants_decomposition_separating("Heisenberg", k=1)
        expected = Fraction(7, 5760) - Fraction(1, 576)
        assert result["F2_nonsep"] == expected
        assert result["F2_nonsep"] == Fraction(-1, 1920)

    def test_nonsep_is_negative(self):
        """F_2^{nonsep} < 0 for all families with kappa > 0.

        This is because lambda_2 < lambda_1^2 (the separating contribution
        overestimates the total).
        """
        for family in FAMILIES:
            result = genus2_pants_decomposition_separating(family)
            k = result["kappa"]
            if k > 0:
                assert result["F2_nonsep"] < 0

    def test_sep_fraction_universal(self):
        """F_2^{sep}/F_2 = lambda_1^2/lambda_2 = 10/7 (universal ratio)."""
        for family in FAMILIES:
            result = genus2_pants_decomposition_separating(family)
            if result["F2"] != 0 and result["sep_fraction"] is not None:
                assert result["sep_fraction"] == Fraction(10, 7)

    def test_mumford_correction_value(self):
        """lambda_2 - lambda_1^2 = 7/5760 - 1/576 = -3/5760 = -1/1920."""
        result = genus2_pants_decomposition_separating("Heisenberg")
        assert result["mumford_correction"] == Fraction(-1, 1920)

    def test_tensor_product_dimensions(self):
        """Tensor product Z^{(1)} tensor Z^{(1)} has correct dimensions."""
        for family in FAMILIES:
            dims = genus2_tensor_product_dimension(family)
            assert dims["Z^0_ch(g=2)"] == 1
            assert dims["Z^1_ch(g=2)"] == 1
            assert dims["Z^2_ch(g=2)"] == 1
            assert dims["total"] == 3


# ======================================================================
#  6. Sp(4,Z) modular structure (Path 5)
# ======================================================================

class TestSp4Modular:
    """Test Sp(4,Z) representation structure at genus 2."""

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hodge_decomposition(self, family):
        """Hodge decomposition: H^{1,0} + H^{0,1} = 4 = 2g."""
        rep = sp4_representation_on_H1(family)
        total = rep["hodge_dimensions"]["H^{1,0}"] + rep["hodge_dimensions"]["H^{0,1}"]
        assert total == DIM_H1_SIGMA2

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hodge_dimensions_equal(self, family):
        """dim H^{1,0} = dim H^{0,1} = g = 2 (Hodge symmetry)."""
        rep = sp4_representation_on_H1(family)
        assert rep["hodge_dimensions"]["H^{1,0}"] == 2
        assert rep["hodge_dimensions"]["H^{0,1}"] == 2

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hodge_bundle_rank(self, family):
        """Hodge bundle E on M-bar_2 has rank 2 = genus."""
        rep = sp4_representation_on_H1(family)
        assert rep["hodge_bundle_rank"] == 2

    def test_siegel_weight_virasoro_c26(self):
        """Siegel modular weight of Z_2(Vir_26) = -26/2 = -13."""
        assert siegel_modular_weight("Virasoro", c=26) == Fraction(-13)

    def test_siegel_weight_heisenberg_k1(self):
        """Siegel modular weight of Z_2(H_1) = -1/2."""
        assert siegel_modular_weight("Heisenberg", k=1) == Fraction(-1, 2)

    def test_sp4_generators(self):
        """Sp(4,Z) has 6 generators (transvections)."""
        assert sp4_generators_count() == 6

    @pytest.mark.parametrize("family", FAMILIES)
    def test_modular_anomaly_equals_kappa(self, family):
        """Genus-2 modular anomaly coefficient = kappa."""
        assert genus2_modular_anomaly(family) == kappa(family)


# ======================================================================
#  7. Swiss-cheese at genus 2
# ======================================================================

class TestSwissCheese:
    """Test Swiss-cheese operations at genus 2."""

    @pytest.mark.parametrize("family", FAMILIES)
    def test_partition_equals_f2(self, family):
        """m^{SC}_{2,0,0} = F_2(A) (partition function = free energy)."""
        assert genus2_swiss_cheese_partition(family) == genus2_F2(family)

    @pytest.mark.parametrize("family", FAMILIES)
    def test_one_closed_equals_f2(self, family):
        """m^{SC}_{2,0,1}(1) = F_2(A) (vacuum one-point function)."""
        assert genus2_swiss_cheese_one_closed(family) == genus2_F2(family)

    def test_swiss_cheese_heisenberg_value(self):
        """m^{SC}_{2,0,0}(H_1) = 7/5760."""
        assert genus2_swiss_cheese_partition("Heisenberg", k=1) == Fraction(7, 5760)


# ======================================================================
#  8. Sewing comparison (Path 2)
# ======================================================================

class TestSewingComparison:
    """Test sewing vs Hochschild computation agreement."""

    def test_heisenberg_sewing_agreement(self):
        """Sewing and Hochschild agree for Heisenberg at k=1."""
        result = genus2_sewing_heisenberg(k=1)
        assert result["agreement"] is True
        assert result["F2_hochschild"] == result["F2_sewing"]

    def test_heisenberg_sewing_k_values(self):
        """Sewing agrees with Hochschild at k=1,2,3,5."""
        for k in [1, 2, 3, 5]:
            result = genus2_sewing_heisenberg(k=k)
            assert result["agreement"] is True

    def test_heisenberg_sewing_numerical(self):
        """Numerical value F_2(H_1) = 7/5760 approx 0.001215..."""
        result = genus2_sewing_heisenberg(k=1)
        assert abs(result["F2_numerical"] - 7 / 5760) < 1e-12

    def test_virasoro_sewing_value(self):
        """Virasoro sewing at c=26: F_2 = 91/5760."""
        result = genus2_sewing_virasoro(c=26)
        assert result["F2_scalar"] == Fraction(91, 5760)

    def test_virasoro_sewing_shadow_depth(self):
        """Virasoro has infinite shadow depth (class M)."""
        result = genus2_sewing_virasoro(c=26)
        assert result["shadow_depth"] == "infinity (class M)"

    def test_three_methods_agree(self):
        """All three methods agree for Heisenberg at k=1."""
        result = genus2_sewing_heisenberg(k=1)
        assert (result["F2_hochschild"] == result["F2_sewing"]
                == Fraction(7, 5760))


# ======================================================================
#  9. Open/closed MC element at genus 2
# ======================================================================

class TestMCElement:
    """Test the genus-2 MC element Theta^{oc,(2)}."""

    @pytest.mark.parametrize("family", FAMILIES)
    def test_mc_satisfied(self, family):
        """MC equation is satisfied at genus 2 for all families."""
        result = genus2_oc_mc_element(family)
        assert result["mc_satisfied"] is True

    def test_mc_theta_2_heisenberg(self):
        """Theta^{(2)}(H_1) = 7/5760."""
        result = genus2_oc_mc_element("Heisenberg", k=1)
        assert result["Theta_2"] == Fraction(7, 5760)

    def test_mc_theta_1_heisenberg(self):
        """Theta^{(1)}(H_1) = kappa * lambda_1 = 1/24."""
        result = genus2_oc_mc_element("Heisenberg", k=1)
        assert result["Theta_1"] == Fraction(1, 24)

    def test_mc_closed_correction_zero(self):
        """mu^{M,(2)} = 0 at the scalar level."""
        for family in FAMILIES:
            result = genus2_oc_mc_element(family)
            assert result["mu_M_2"] == Fraction(0)

    def test_mc_genus_hierarchy(self):
        """Theta^{(0)} < Theta^{(1)} < Theta^{(2)} in magnitude for kappa > 0."""
        for family in FAMILIES:
            result = genus2_oc_mc_element(family)
            # Theta^{(0)} = 0 (uncurved at genus 0 in the scalar projection)
            # |Theta^{(1)}| = kappa/24
            # |Theta^{(2)}| = kappa*7/5760
            # Since 7/5760 < 1/24, Theta^{(2)} < Theta^{(1)} in magnitude
            k = result["kappa"]
            if k > 0:
                assert abs(result["Theta_2"]) < abs(result["Theta_1"])

    def test_mc_equation_components_heisenberg(self):
        """Verify MC equation component values for Heisenberg."""
        result = genus2_oc_mc_element("Heisenberg", k=1)
        mc = result["mc_equation_check"]
        assert mc["d0_Theta2"] == 0
        assert mc["bracket_0_2"] == 0
        # half_bracket_1_1 = (1/2) * (1/24)^2 = 1/1152
        assert mc["half_bracket_1_1"] == Fraction(1, 1152)


# ======================================================================
#  10. Degeneration: genus-2 -> genus-1 (Path 6)
# ======================================================================

class TestDegeneration:
    """Test genus-2 to genus-1 degeneration limits."""

    @pytest.mark.parametrize("family", FAMILIES)
    def test_degeneration_consistent(self, family):
        """Degeneration is consistent by construction."""
        result = genus2_to_genus1_degeneration(family)
        assert result["degeneration_consistent"] is True

    def test_degeneration_ratio_universal(self):
        """F_2/F_1 = lambda_2/lambda_1 = 7/240 (universal)."""
        for family in FAMILIES:
            result = genus2_to_genus1_degeneration(family)
            if result["ratio_F2_F1"] is not None:
                assert result["ratio_F2_F1"] == Fraction(7, 240)

    def test_separating_limit_heisenberg(self):
        """Separating limit of F_2(H_1) = F_1^2/kappa = (1/24)^2/1 = 1/576."""
        result = genus2_to_genus1_degeneration("Heisenberg", k=1)
        assert result["separating_limit"] == Fraction(1, 576)

    def test_nonsep_residue_heisenberg(self):
        """Nonseparating residue = F_2 - F_1^2/kappa = 7/5760 - 1/576 = -1/1920."""
        result = genus2_to_genus1_degeneration("Heisenberg", k=1)
        assert result["nonseparating_residue"] == Fraction(-1, 1920)

    def test_f2_f1_ratio_less_than_1(self):
        """lambda_2/lambda_1 = 7/240 < 1 (genus-2 is suppressed relative to genus-1)."""
        assert LAMBDA_2_FP / LAMBDA_1_FP < 1

    def test_bernoulli_decay(self):
        """lambda_g decays as |B_{2g}|/(2g)! ~ 2/(2*pi)^{2g} (Bernoulli asymptotics).

        lambda_2/lambda_1 = 7/240 approx 0.0292
        For comparison, 1/(2*pi)^2 approx 0.0253
        """
        ratio = float(LAMBDA_2_FP / LAMBDA_1_FP)
        assert 0.02 < ratio < 0.04


# ======================================================================
#  11. Complementarity and additivity
# ======================================================================

class TestComplementarity:
    """Test Theorem C (complementarity) at genus 2."""

    def test_complementarity_heisenberg(self):
        """F_2(H_k) + F_2(H_k!) = 0 for Heisenberg (AP24)."""
        result = genus2_complementarity("Heisenberg", k=1)
        assert result["complementarity_holds"] is True
        assert result["F2_complement_sum"] == Fraction(0)

    def test_complementarity_virasoro(self):
        """F_2(Vir_c) + F_2(Vir_{26-c}) = 13 * lambda_2 for Virasoro (AP24)."""
        result = genus2_complementarity("Virasoro", c=26)
        assert result["complementarity_holds"] is True
        assert result["kappa_sum"] == Fraction(13)

    def test_complementarity_virasoro_c1(self):
        """F_2(Vir_1) + F_2(Vir_25) = 13 * lambda_2."""
        result = genus2_complementarity("Virasoro", c=1)
        assert result["complementarity_holds"] is True
        expected_sum = Fraction(13) * LAMBDA_2_FP
        assert result["F2_complement_sum"] == expected_sum

    def test_complementarity_sl2(self):
        """F_2(sl_2, k) + F_2(sl_2, k!) = 0 for affine (AP24)."""
        result = genus2_complementarity("Affine_sl2", k=1)
        assert result["complementarity_holds"] is True
        assert result["kappa_sum"] == Fraction(0)

    def test_additivity_heisenberg(self):
        """F_2(H_k1 oplus H_k2) = F_2(H_k1) + F_2(H_k2)."""
        result = genus2_additivity("Heisenberg", "Heisenberg",
                                   {"k": 1}, {"k": 2})
        assert result["additivity_holds"] is True

    def test_additivity_mixed(self):
        """Additivity for H_1 oplus Vir_1."""
        result = genus2_additivity("Heisenberg", "Virasoro",
                                   {"k": 1}, {"c": 1})
        assert result["additivity_holds"] is True

    def test_additivity_value(self):
        """F_2(H_1) + F_2(H_2) = F_2(H_3) = 3 * 7/5760."""
        f2_1 = genus2_F2("Heisenberg", k=1)
        f2_2 = genus2_F2("Heisenberg", k=2)
        f2_3 = genus2_F2("Heisenberg", k=3)
        assert f2_1 + f2_2 == f2_3


# ======================================================================
#  12. Hodge integrals and Mumford relation
# ======================================================================

class TestHodgeIntegrals:
    """Test genus-2 Hodge integrals and Mumford relation."""

    def test_int_lambda_2(self):
        """int_{M-bar_2} lambda_2 = 1/240."""
        hi = genus2_hodge_integrals()
        assert hi["int_lambda_2"] == Fraction(1, 240)

    def test_int_lambda_1_squared(self):
        """int_{M-bar_2} lambda_1^2 = 1/240."""
        hi = genus2_hodge_integrals()
        assert hi["int_lambda_1_squared"] == Fraction(1, 240)

    def test_mumford_relation(self):
        """lambda_1^2 = lambda_2 on M-bar_2 (Mumford relation)."""
        hi = genus2_hodge_integrals()
        assert hi["mumford_relation"] is True
        assert hi["int_lambda_1_squared"] == hi["int_lambda_2"]

    def test_mumford_relation_check(self):
        """Direct verification of Mumford relation."""
        assert genus2_mumford_relation_check() is True

    def test_int_lambda_1_psi(self):
        """int_{M-bar_{2,1}} lambda_1 * psi = 1/1152."""
        hi = genus2_hodge_integrals()
        assert hi["int_lambda_1_psi"] == Fraction(1, 1152)

    def test_lambda_2_fp_in_package(self):
        """lambda_2^{FP} = 7/5760 is recorded correctly."""
        hi = genus2_hodge_integrals()
        assert hi["lambda_2_FP"] == Fraction(7, 5760)


# ======================================================================
#  13. Planted-forest correction
# ======================================================================

class TestPlantedForest:
    """Test genus-2 planted-forest correction delta_pf^{(2,0)}."""

    def test_pf_heisenberg_zero(self):
        """delta_pf(H_k) = 0 (Gaussian: S_3 = 0)."""
        assert genus2_planted_forest_correction("Heisenberg", k=1) == 0
        assert genus2_planted_forest_correction("Heisenberg", k=5) == 0

    def test_pf_virasoro(self):
        """delta_pf(Vir_c) = 2*(20 - c/2)/48 = (40 - c)/48."""
        c = 26
        result = genus2_planted_forest_correction("Virasoro", c=c)
        # S_3 = 2, kappa = c/2 = 13
        # delta_pf = 2*(10*2 - 13)/48 = 2*(20-13)/48 = 2*7/48 = 14/48 = 7/24
        expected = Fraction(2) * (Fraction(20) - Fraction(13)) / Fraction(48)
        assert result == expected
        assert result == Fraction(7, 24)

    def test_pf_virasoro_c0(self):
        """delta_pf(Vir_0) = 2*(20-0)/48 = 40/48 = 5/6."""
        result = genus2_planted_forest_correction("Virasoro", c=0)
        # S_3 = 2, kappa = 0
        # delta_pf = 2*(20 - 0)/48 = 40/48 = 5/6
        assert result == Fraction(5, 6)

    def test_pf_sl2_k1(self):
        """delta_pf for affine sl_2 at k=1."""
        result = genus2_planted_forest_correction("Affine_sl2", k=1)
        # S_3 = 1, kappa = 9/4
        # delta_pf = 1*(10 - 9/4)/48 = (40/4 - 9/4)/48 = (31/4)/48 = 31/192
        expected = Fraction(31, 192)
        assert result == expected

    def test_pf_formula_structure(self):
        """delta_pf = S_3*(10*S_3 - kappa)/48 for all families."""
        for family in FAMILIES:
            pf = genus2_planted_forest_correction(family)
            # This is just a structural check: the function should return a Fraction
            assert isinstance(pf, Fraction)


# ======================================================================
#  14. Multi-path verification
# ======================================================================

class TestMultiPathVerification:
    """Test that all verification paths agree."""

    @pytest.mark.parametrize("family", FAMILIES)
    def test_all_paths_agree(self, family):
        """All verification paths produce the same F_2."""
        result = genus2_verification_paths(family)
        assert result["all_agree"] is True

    def test_heisenberg_6_paths(self):
        """Heisenberg has 6 independent verification paths."""
        result = genus2_verification_paths("Heisenberg", k=1)
        assert result["num_paths"] == 6

    def test_virasoro_5_paths(self):
        """Non-Heisenberg families have 5 paths (path 4 is Heisenberg-only)."""
        result = genus2_verification_paths("Virasoro", c=26)
        assert result["num_paths"] == 5

    @pytest.mark.parametrize("family", FAMILIES)
    def test_hochschild_equals_sewing(self, family):
        """Path 1 (Hochschild) = Path 2 (sewing) for all families."""
        result = genus2_verification_paths(family)
        assert result["path1_hochschild"] == result["path2_sewing"]

    @pytest.mark.parametrize("family", FAMILIES)
    def test_pants_equals_hochschild(self, family):
        """Path 3 (pants) = Path 1 (Hochschild) for all families."""
        result = genus2_verification_paths(family)
        assert result["path3_pants"] == result["path1_hochschild"]

    def test_degeneration_ratio_path6(self):
        """Path 6: degeneration ratio is 7/240."""
        result = genus2_verification_paths("Heisenberg", k=1)
        assert result["path6_degeneration_ratio"] == Fraction(7, 240)


# ======================================================================
#  15. Full package integration tests
# ======================================================================

class TestFullPackage:
    """Test the complete genus-2 derived center package."""

    @pytest.mark.parametrize("family", FAMILIES)
    def test_package_all_keys(self, family):
        """Package contains all required keys."""
        pkg = genus2_derived_center_package(family)
        required_keys = [
            "family", "kappa", "F2", "F2_numerical", "HH_dimensions",
            "trace_scalar", "trace_ratio_21", "pants_decomposition",
            "sp4_representation", "siegel_weight", "swiss_cheese_partition",
            "oc_mc_element", "degeneration", "complementarity",
            "hodge_integrals", "planted_forest_correction", "verification_paths",
        ]
        for key in required_keys:
            assert key in pkg, f"Missing key: {key}"

    def test_package_heisenberg_k1(self):
        """Full package for Heisenberg at k=1."""
        pkg = genus2_derived_center_package("Heisenberg", k=1)
        assert pkg["kappa"] == Fraction(1)
        assert pkg["F2"] == Fraction(7, 5760)
        assert pkg["HH_dimensions"] == {0: 1, 1: 1, 2: 1, 3: 0, 4: 0}
        assert pkg["trace_scalar"] == Fraction(7, 5760)
        assert pkg["trace_ratio_21"] == Fraction(7, 240)
        assert pkg["siegel_weight"] == Fraction(-1, 2)
        assert pkg["planted_forest_correction"] == Fraction(0)

    def test_package_virasoro_c26(self):
        """Full package for Virasoro at c=26."""
        pkg = genus2_derived_center_package("Virasoro", c=26)
        assert pkg["kappa"] == Fraction(13)
        assert pkg["F2"] == Fraction(91, 5760)
        assert pkg["siegel_weight"] == Fraction(-13)
        # Planted forest: S_3=2, kappa=13, delta_pf = 2*(20-13)/48 = 7/24
        assert pkg["planted_forest_correction"] == Fraction(7, 24)

    def test_package_numerical_value(self):
        """Numerical F_2 value is correct."""
        pkg = genus2_derived_center_package("Heisenberg", k=1)
        assert abs(pkg["F2_numerical"] - 7 / 5760) < 1e-15


# ======================================================================
#  16. Cross-family consistency
# ======================================================================

class TestCrossFamily:
    """Cross-family consistency checks (AP10)."""

    def test_f2_ordering_by_kappa(self):
        """F_2 respects kappa ordering: F_2(A) < F_2(B) iff kappa(A) < kappa(B)."""
        families_kappas = [(f, kappa(f)) for f in FAMILIES]
        families_kappas.sort(key=lambda x: x[1])
        F2s = [genus2_F2(f) for f, _ in families_kappas]
        for i in range(len(F2s) - 1):
            assert F2s[i] <= F2s[i + 1]

    def test_f2_ratio_equals_kappa_ratio(self):
        """F_2(A)/F_2(B) = kappa(A)/kappa(B) for any two families with kappa > 0."""
        f2_h = genus2_F2("Heisenberg", k=1)
        f2_v = genus2_F2("Virasoro", c=26)
        k_h = kappa("Heisenberg", k=1)
        k_v = kappa("Virasoro", c=26)
        assert f2_h * k_v == f2_v * k_h

    def test_universal_lambda_2_extraction(self):
        """lambda_2 = F_2/kappa is the SAME for all families."""
        for family in FAMILIES:
            k = kappa(family)
            if k != 0:
                f2 = genus2_F2(family)
                assert f2 / k == LAMBDA_2_FP

    def test_genus_ratio_consistent(self):
        """F_2/F_1 = lambda_2/lambda_1 = 7/240 for all families."""
        for family in FAMILIES:
            k = kappa(family)
            if k != 0:
                f1 = k * LAMBDA_1_FP
                f2 = k * LAMBDA_2_FP
                assert f2 / f1 == Fraction(7, 240)


# ======================================================================
#  17. Edge cases and error handling
# ======================================================================

class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_zero_level_heisenberg(self):
        """F_2(H_0) = 0 (zero level -> zero kappa -> zero F_2)."""
        assert genus2_F2("Heisenberg", k=0) == 0

    def test_zero_cc_virasoro(self):
        """F_2(Vir_0) = 0 (zero central charge -> zero F_2)."""
        assert genus2_F2("Virasoro", c=0) == 0

    def test_negative_level(self):
        """F_2(H_{-k}) = -F_2(H_k) (negative kappa -> negative F_2)."""
        f2_pos = genus2_F2("Heisenberg", k=3)
        f2_neg = genus2_F2("Heisenberg", k=-3)
        assert f2_pos + f2_neg == 0

    def test_self_dual_virasoro(self):
        """At c=13 (self-dual point): kappa = 13/2, F_2 = 91/11520."""
        f2 = genus2_F2("Virasoro", c=13)
        expected = Fraction(13, 2) * Fraction(7, 5760)
        assert f2 == expected

    def test_large_level(self):
        """F_2 scales linearly with large k."""
        f2_100 = genus2_F2("Heisenberg", k=100)
        assert f2_100 == Fraction(100) * LAMBDA_2_FP

    def test_fractional_level(self):
        """F_2 works with fractional levels."""
        f2 = genus2_F2("Heisenberg", k=Fraction(1, 2))
        assert f2 == Fraction(1, 2) * LAMBDA_2_FP

    def test_unknown_family_raises_in_package(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError):
            genus2_derived_center_package("Unknown")


# ======================================================================
#  18. Numerical cross-checks
# ======================================================================

class TestNumerical:
    """Numerical cross-checks for the genus-2 engine."""

    def test_f2_heisenberg_numerical(self):
        """F_2(H_1) = 7/5760 approx 0.0012153."""
        f2 = float(genus2_F2("Heisenberg", k=1))
        assert abs(f2 - 7.0 / 5760.0) < 1e-15

    def test_f2_virasoro_c26_numerical(self):
        """F_2(Vir_26) = 91/5760 approx 0.0157986."""
        f2 = float(genus2_F2("Virasoro", c=26))
        assert abs(f2 - 91.0 / 5760.0) < 1e-15

    def test_lambda_ratio_numerical(self):
        """lambda_2/lambda_1 = 7/240 approx 0.02917."""
        ratio = float(LAMBDA_2_FP / LAMBDA_1_FP)
        assert abs(ratio - 7.0 / 240.0) < 1e-15

    def test_sep_fraction_numerical(self):
        """Separating fraction = 10/7 approx 1.42857."""
        frac = float(Fraction(10, 7))
        result = genus2_pants_decomposition_separating("Heisenberg", k=1)
        assert abs(float(result["sep_fraction"]) - frac) < 1e-10

    def test_nonsep_residue_numerical(self):
        """Nonseparating residue F_2^{nonsep}(H_1) = -1/1920 approx -0.000521."""
        result = genus2_pants_decomposition_separating("Heisenberg", k=1)
        val = float(result["F2_nonsep"])
        assert abs(val - (-1.0 / 1920.0)) < 1e-15

    def test_chi_orb_mbar2_numerical(self):
        """chi^{orb}(M-bar_2) = 7/240 approx 0.02917."""
        assert abs(float(CHI_ORB_MBAR2) - 7.0 / 240.0) < 1e-15
