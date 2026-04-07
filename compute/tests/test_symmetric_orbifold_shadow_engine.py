r"""Tests for the symmetric orbifold shadow engine.

Verifies Sym^N(X) data for X = free boson, T^4, K3 via the multi-path
verification mandate: each claim tested by at least 2 independent paths.

60+ tests covering:
  - Central charge and kappa of Sym^N
  - Twist sector enumeration and conformal weights
  - DMVV partition function (Gottsche formula)
  - Shadow tower of Sym^N
  - Large-N limit and growth rates
  - Holographic modular Koszul datum
  - BTZ black hole entropy
  - Hawking-Page transition
  - Second-quantized partition function and Borcherds products
  - Cross-checks and internal consistency
"""

import math
from fractions import Fraction

import pytest

from compute.lib.symmetric_orbifold_shadow_engine import (
    FREE_BOSON,
    K3_SIGMA,
    LEECH_VOA,
    T4_SIGMA,
    HolographicDatum,
    SeedTheory,
    TwistSector,
    borcherds_kappa_bps,
    borcherds_product_weight,
    borcherds_ratio,
    btz_entropy_from_kappa,
    btz_entropy_kappa_formula,
    btz_entropy_with_shadow_corrections,
    btz_log_correction,
    central_charge_sym_n,
    colored_partitions,
    costello_paquette_comparison,
    dmvv_connected_f1,
    dmvv_log_coefficients,
    dmvv_partition_function_z0,
    enumerate_twist_sectors,
    gottsche_euler_char,
    hawking_page_beta_classical,
    hawking_page_free_energy_btz,
    hawking_page_free_energy_thermal_ads,
    hawking_page_phase_diagram,
    hawking_page_transition_beta,
    holographic_datum_ads3_k3,
    holographic_datum_ads3_t4,
    igusa_cusp_form_first_coefficients,
    kappa_growth_rate,
    kappa_sym_n,
    kappa_sym_n_free_boson,
    large_n_central_charge,
    large_n_free_energy_genus_g,
    large_n_kappa,
    large_n_kappa_over_c,
    number_of_twist_sectors,
    second_quantized_pf_coefficients,
    shadow_cubic_sym_n,
    shadow_depth_sym_n,
    shadow_kappa_sym_n,
    shadow_quartic_sym_n,
    shadow_tower_sym_n,
    twist_field_weight,
    twist_sector_weight,
    twist_sectors_with_weights,
    verify_btz_cardy_consistency,
    verify_dmvv_log_consistency,
    verify_gottsche_low_n,
    verify_hawking_page_large_n,
    verify_kappa_additivity,
    verify_twist_sector_counting,
)

F = Fraction
PI = math.pi


# =========================================================================
# Section 1: Central charge tests (6 tests)
# =========================================================================

class TestCentralCharge:
    """Central charge c(Sym^N(X)) = N * c(X)."""

    def test_central_charge_sym1_k3(self):
        """Sym^1(K3) = K3 with c = 6."""
        assert central_charge_sym_n(K3_SIGMA, 1) == F(6)

    def test_central_charge_sym_n_k3_linear(self):
        """c(Sym^N(K3)) = 6N for N = 1, ..., 10."""
        for N in range(1, 11):
            assert central_charge_sym_n(K3_SIGMA, N) == F(6 * N)

    def test_central_charge_sym_n_t4_linear(self):
        """c(Sym^N(T^4)) = 6N for N = 1, ..., 10."""
        for N in range(1, 11):
            assert central_charge_sym_n(T4_SIGMA, N) == F(6 * N)

    def test_central_charge_sym_n_free_boson(self):
        """c(Sym^N(free boson)) = N."""
        for N in range(1, 11):
            assert central_charge_sym_n(FREE_BOSON, N) == F(N)

    def test_central_charge_sym0(self):
        """c(Sym^0(X)) = 0."""
        assert central_charge_sym_n(K3_SIGMA, 0) == F(0)

    def test_central_charge_negative_n_raises(self):
        """Negative N should raise ValueError."""
        with pytest.raises(ValueError):
            central_charge_sym_n(K3_SIGMA, -1)


# =========================================================================
# Section 2: Kappa tests (10 tests)
# =========================================================================

class TestKappa:
    """Modular characteristic kappa(Sym^N(X)).

    AP48: kappa depends on the full algebra, NOT the Virasoro subalgebra.
    For sigma models: kappa = dim_C(target), NOT c/2.
    """

    def test_kappa_k3_n1(self):
        """kappa(K3) = 2 = dim_C(K3).  NOT c/2 = 3.  AP48."""
        assert kappa_sym_n(K3_SIGMA, 1) == F(2)
        assert kappa_sym_n(K3_SIGMA, 1) != K3_SIGMA.central_charge / 2

    def test_kappa_t4_n1(self):
        """kappa(T^4) = 2 = dim_C(T^4).  NOT c/2 = 3.  AP48."""
        assert kappa_sym_n(T4_SIGMA, 1) == F(2)

    def test_kappa_free_boson_n1(self):
        """kappa(free boson at level 1) = 1.  AP39."""
        assert kappa_sym_n(FREE_BOSON, 1) == F(1)

    def test_kappa_sym_n_additivity(self):
        """kappa(Sym^N) = N * kappa(seed): additivity check."""
        for N in range(1, 11):
            assert kappa_sym_n(K3_SIGMA, N) == N * F(2)

    def test_kappa_free_boson_sym_n(self):
        """kappa(Sym^N(free boson)) = N via dedicated function."""
        for N in range(1, 11):
            assert kappa_sym_n_free_boson(N) == F(N)

    def test_kappa_growth_rate_k3(self):
        """kappa(Sym^N(K3)) / N -> 2 as N -> infty."""
        assert kappa_growth_rate(K3_SIGMA) == F(2)

    def test_kappa_growth_rate_free_boson(self):
        """kappa(Sym^N(free boson)) / N -> 1."""
        assert kappa_growth_rate(FREE_BOSON) == F(1)

    def test_kappa_leech(self):
        """kappa(Leech VOA) = 24 = rank.  AP48: NOT c/2 = 12."""
        assert LEECH_VOA.kappa == F(24)
        assert LEECH_VOA.kappa != LEECH_VOA.central_charge / 2

    def test_kappa_not_c_over_2_for_sigma_models(self):
        """Verify that kappa != c/2 for all sigma model seeds (AP48)."""
        for seed in [T4_SIGMA, K3_SIGMA, LEECH_VOA]:
            assert seed.kappa != seed.central_charge / 2, \
                f"AP48 violation: {seed.name} has kappa = c/2 = {seed.central_charge / 2}"

    def test_kappa_additivity_verification(self):
        """Multi-path verification of additivity."""
        result = verify_kappa_additivity(K3_SIGMA, list(range(1, 8)))
        for check in result["checks"]:
            assert check["match"], f"Additivity fails at N={check['N']}"


# =========================================================================
# Section 3: Twist sector tests (9 tests)
# =========================================================================

class TestTwistSectors:
    """Twist sector enumeration and conformal weights."""

    def test_num_sectors_small_n(self):
        """p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        expected = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
        for N, p_n in expected.items():
            assert number_of_twist_sectors(N) == p_n

    def test_twist_sectors_s2(self):
        """S_2 has 2 conjugacy classes: (1,1) and (2)."""
        sectors = enumerate_twist_sectors(2)
        assert len(sectors) == 2
        partitions = [s.partition for s in sectors]
        assert (2,) in partitions
        assert (1, 1) in partitions

    def test_twist_sectors_s3(self):
        """S_3 has 3 conjugacy classes: (1,1,1), (2,1), (3)."""
        sectors = enumerate_twist_sectors(3)
        assert len(sectors) == 3

    def test_class_equation_s_n(self):
        """Sum of conjugacy class sizes = N! (class equation)."""
        for N in range(1, 8):
            result = verify_twist_sector_counting(N)
            assert result["class_equation_matches"], f"Class equation fails for S_{N}"

    def test_partition_count_matches(self):
        """Number of sectors matches partition count."""
        for N in range(1, 8):
            result = verify_twist_sector_counting(N)
            assert result["partition_count_matches"]

    def test_twist_weight_identity(self):
        """Identity (all 1-cycles) has h = 0."""
        assert twist_field_weight(F(6), 1) == F(0)

    def test_twist_weight_z2_free_boson(self):
        """Z_2 twist field of c=1 free boson: h = 1/16."""
        h = twist_field_weight(F(1), 2)
        assert h == F(1, 16)

    def test_twist_weight_z2_k3(self):
        """Z_2 twist field of c=6 K3: h = 6/16 = 3/8."""
        h = twist_field_weight(F(6), 2)
        assert h == F(3, 8)

    def test_twist_weight_z3_free_boson(self):
        """Z_3 twist field of c=1 free boson: h = (1/24)(9-1)/3 = 1/9."""
        h = twist_field_weight(F(1), 3)
        assert h == F(1, 9)


# =========================================================================
# Section 4: DMVV partition function tests (8 tests)
# =========================================================================

class TestDMVV:
    """DMVV / Gottsche partition function tests."""

    def test_gottsche_n0(self):
        """chi(Hilb^0) = 1."""
        assert gottsche_euler_char(0, 24) == 1

    def test_gottsche_n1_k3(self):
        """chi(Hilb^1(K3)) = chi(K3) = 24."""
        assert gottsche_euler_char(1, 24) == 24

    def test_gottsche_n2_k3(self):
        """chi(Hilb^2(K3)) = 324.

        24-colored partitions of 2:
          (2) in any of 24 colors: 24
          (1,1) with ordered colors: C(25, 2) = 300
          Total: 324.
        """
        assert gottsche_euler_char(2, 24) == 324

    def test_gottsche_n3_k3(self):
        """chi(Hilb^3(K3)) = 3200.

        24-colored partitions of 3:
          (3): 24
          (2,1): 24 * 24 = 576
          (1,1,1): C(26, 3) = 2600
          Total: 24 + 576 + 2600 = 3200.
        """
        assert gottsche_euler_char(3, 24) == 3200

    def test_gottsche_low_n_verification(self):
        """Multi-path verification of low-N Gottsche formula."""
        result = verify_gottsche_low_n(24)
        assert result["all_match"]

    def test_dmvv_connected_f1_n1(self):
        """F_1^{connected}(1) = chi(K3) * 1 = 24."""
        assert dmvv_connected_f1(1, 24) == F(24)

    def test_dmvv_connected_f1_n2(self):
        """F_1^{connected}(2) = 24 * (1 + 1/2) = 36."""
        assert dmvv_connected_f1(2, 24) == F(36)

    def test_dmvv_log_consistency(self):
        """log Z computed analytically vs numerically must agree.

        Two independent paths:
        Path 1: chi_S * sigma_{-1}(N).
        Path 2: Power-series log of Gottsche generating function.
        """
        result = verify_dmvv_log_consistency(8, 24)
        assert result["all_match"], \
            f"DMVV log consistency fails: {[m for m in result['matches'] if not m['match']]}"


# =========================================================================
# Section 5: Shadow tower tests (7 tests)
# =========================================================================

class TestShadowTower:
    """Shadow obstruction tower of Sym^N(X)."""

    def test_shadow_kappa_equals_kappa(self):
        """shadow_kappa_sym_n must equal kappa_sym_n."""
        for N in range(1, 6):
            assert shadow_kappa_sym_n(K3_SIGMA, N) == kappa_sym_n(K3_SIGMA, N)

    def test_shadow_depth_gaussian_seed(self):
        """Gaussian seed (free theory) => Sym^N has r_max = 2."""
        for N in range(1, 6):
            assert shadow_depth_sym_n(K3_SIGMA, N) == 2
            assert shadow_depth_sym_n(T4_SIGMA, N) == 2
            assert shadow_depth_sym_n(FREE_BOSON, N) == 2

    def test_shadow_tower_gaussian(self):
        """For Gaussian seed, tower has S_2 = kappa and S_r = 0 for r >= 3."""
        tower = shadow_tower_sym_n(K3_SIGMA, 5)
        assert tower[2] == F(10)  # 5 * 2
        for r in range(3, 7):
            assert tower[r] == F(0)

    def test_shadow_cubic_additivity(self):
        """S_3(Sym^N) = N * S_3(seed)."""
        seed_S3 = F(2)  # Virasoro-like cubic shadow
        for N in range(1, 6):
            assert shadow_cubic_sym_n(F(1), seed_S3, N) == N * seed_S3

    def test_shadow_quartic_additivity(self):
        """S_4(Sym^N) = N * S_4(seed)."""
        seed_S4 = F(1, 10)
        for N in range(1, 6):
            assert shadow_quartic_sym_n(F(1), seed_S4, N) == N * seed_S4

    def test_shadow_tower_with_custom_seeds(self):
        """Custom seed shadow data propagates correctly."""
        seed_shadows = {2: F(3), 3: F(1), 4: F(-1, 5)}
        tower = shadow_tower_sym_n(K3_SIGMA, 4, seed_shadows)
        assert tower[2] == F(12)     # 4 * 3
        assert tower[3] == F(4)      # 4 * 1
        assert tower[4] == F(-4, 5)  # 4 * (-1/5)

    def test_shadow_depth_monotone(self):
        """Shadow depth of Sym^N should not decrease with N."""
        for N in range(1, 6):
            assert shadow_depth_sym_n(K3_SIGMA, N) >= shadow_depth_sym_n(K3_SIGMA, 1)


# =========================================================================
# Section 6: Large-N limit tests (6 tests)
# =========================================================================

class TestLargeN:
    """Large-N behavior of Sym^N(X)."""

    def test_large_n_c_linear(self):
        """c(N) grows linearly with N."""
        for N in [10, 100, 1000]:
            assert large_n_central_charge(K3_SIGMA, N) == F(6 * N)

    def test_large_n_kappa_linear(self):
        """kappa(N) grows linearly with N."""
        for N in [10, 100, 1000]:
            assert large_n_kappa(K3_SIGMA, N) == F(2 * N)

    def test_large_n_kappa_over_c_constant(self):
        """kappa/c = kappa_seed/c_seed is N-independent."""
        ratio = large_n_kappa_over_c(K3_SIGMA)
        assert ratio == F(1, 3)

    def test_large_n_kappa_over_c_free_boson(self):
        """kappa/c = 1 for free boson."""
        assert large_n_kappa_over_c(FREE_BOSON) == F(1)

    def test_large_n_free_energy_scales_linearly(self):
        """F_g(Sym^N) = N * F_g(single copy) for scalar lane."""
        F1_single = large_n_free_energy_genus_g(K3_SIGMA, 1, 1)
        for N in [2, 5, 10]:
            F1_N = large_n_free_energy_genus_g(K3_SIGMA, N, 1)
            assert F1_N == N * F1_single

    def test_large_n_f1_value(self):
        """F_1(Sym^N(K3)) = 2N * lambda_1^FP = 2N * 1/24 = N/12."""
        F1 = large_n_free_energy_genus_g(K3_SIGMA, 1, 1)
        # kappa(K3) = 2, lambda_1^FP = 1/24
        assert F1 == F(2) * F(1, 24)
        assert F1 == F(1, 12)


# =========================================================================
# Section 7: Holographic datum tests (6 tests)
# =========================================================================

class TestHolographicDatum:
    """Holographic modular Koszul datum for AdS_3."""

    def test_ads3_t4_basic(self):
        """AdS_3 x S^3 x T^4: c = 6N, kappa = 2N."""
        datum = holographic_datum_ads3_t4(5)
        assert datum.central_charge == F(30)
        assert datum.kappa == F(10)
        assert datum.N == 5

    def test_ads3_k3_basic(self):
        """AdS_3 x S^3 x K3: c = 6N, kappa = 2N."""
        datum = holographic_datum_ads3_k3(10)
        assert datum.central_charge == F(60)
        assert datum.kappa == F(20)

    def test_ads3_koszul_dual_free_field(self):
        """For free fields: kappa(A!) = -kappa(A) (anti-symmetry)."""
        datum = holographic_datum_ads3_t4(5)
        assert datum.kappa_dual == -datum.kappa
        assert datum.kappa + datum.kappa_dual == F(0)

    def test_ads3_shadow_class_gaussian(self):
        """Both T^4 and K3 symmetric orbifolds are class G."""
        assert holographic_datum_ads3_t4(5).shadow_class == "G"
        assert holographic_datum_ads3_k3(5).shadow_class == "G"

    def test_costello_paquette_comparison_structure(self):
        """The CP comparison returns sensible data."""
        result = costello_paquette_comparison(10)
        assert result["c"] == F(60)
        assert result["kappa"] == F(20)
        assert "MATCHES" in result["costello_paquette_match"]["boundary_algebra"]
        assert len(result["novel_predictions"]) > 0

    def test_delta_kappa_free_field(self):
        """delta_kappa = kappa - kappa' = 2*kappa for free fields."""
        datum = holographic_datum_ads3_t4(5)
        assert datum.delta_kappa == 2 * datum.kappa


# =========================================================================
# Section 8: BTZ entropy tests (7 tests)
# =========================================================================

class TestBTZEntropy:
    """BTZ black hole entropy from shadow tower data."""

    def test_btz_cardy_formula(self):
        """S_BH = 2*pi*sqrt(c*n/6) for Sym^N(K3)."""
        N, n = 10, F(100)
        S = btz_entropy_from_kappa(K3_SIGMA, N, n)
        c = float(central_charge_sym_n(K3_SIGMA, N))
        expected = 2 * PI * math.sqrt(c * 100.0 / 6.0)
        assert abs(S - expected) < 1e-10

    def test_btz_entropy_scales_sqrt_n(self):
        """S_BH ~ sqrt(N) at fixed excitation number n."""
        n = F(100)
        S1 = btz_entropy_from_kappa(K3_SIGMA, 1, n)
        S4 = btz_entropy_from_kappa(K3_SIGMA, 4, n)
        # S ~ sqrt(c) ~ sqrt(N), so S4/S1 = sqrt(4) = 2
        assert abs(S4 / S1 - 2.0) < 1e-10

    def test_btz_kappa_vs_cardy_disagree_for_sigma_model(self):
        """For sigma model, kappa != c/2, so shadow formula != Cardy.  AP48."""
        result = verify_btz_cardy_consistency(K3_SIGMA, 5, F(100))
        assert not result["kappa_equals_c_over_2"]
        assert not result["formulas_agree"]

    def test_btz_log_correction_universal(self):
        """The log correction coefficient is -3/2 (universal)."""
        assert btz_log_correction(6.0) == -1.5

    def test_btz_shadow_corrections_structure(self):
        """Shadow corrections have the right structure."""
        result = btz_entropy_with_shadow_corrections(K3_SIGMA, 10, F(100))
        assert result["S_BH"] > 0
        assert result["log_correction"] < 0  # negative log correction
        assert 2 in result["genus_corrections"]
        assert result["N"] == 10

    def test_btz_entropy_increases_with_n(self):
        """Entropy increases with excitation number n."""
        S1 = btz_entropy_from_kappa(K3_SIGMA, 5, F(10))
        S2 = btz_entropy_from_kappa(K3_SIGMA, 5, F(100))
        assert S2 > S1

    def test_btz_entropy_increases_with_N(self):
        """Entropy increases with N at fixed n."""
        S1 = btz_entropy_from_kappa(K3_SIGMA, 5, F(50))
        S2 = btz_entropy_from_kappa(K3_SIGMA, 10, F(50))
        assert S2 > S1


# =========================================================================
# Section 9: Hawking-Page tests (6 tests)
# =========================================================================

class TestHawkingPage:
    """Hawking-Page phase transition for Sym^N(X)."""

    def test_hp_classical_beta(self):
        """Classical HP temperature: beta = 2*pi."""
        assert abs(hawking_page_beta_classical() - 2 * PI) < 1e-12

    def test_hp_free_energy_crossing(self):
        """At beta = 2*pi, F_AdS = F_BTZ (classical crossing)."""
        c = 60.0
        beta = 2 * PI
        F_ads = hawking_page_free_energy_thermal_ads(c, beta)
        F_btz = hawking_page_free_energy_btz(c, beta)
        assert abs(F_ads - F_btz) < 1e-10

    def test_hp_classical_transition(self):
        """At max_genus=0, beta_HP = 2*pi exactly."""
        beta = hawking_page_transition_beta(K3_SIGMA, 10, max_genus=0)
        assert abs(beta - 2 * PI) < 1e-12

    def test_hp_shadow_correction_sign(self):
        """Shadow correction to beta_HP is negative (lowers transition T)."""
        beta = hawking_page_transition_beta(K3_SIGMA, 10, max_genus=1)
        assert beta < 2 * PI  # correction is negative

    def test_hp_correction_kappa_over_c(self):
        """delta_beta = -kappa/c = -1/3 for K3."""
        beta = hawking_page_transition_beta(K3_SIGMA, 10, max_genus=1)
        expected_delta = -float(K3_SIGMA.kappa) / float(K3_SIGMA.central_charge)
        assert abs((beta - 2 * PI) - expected_delta) < 1e-10

    def test_hp_phase_diagram(self):
        """Phase diagram returns correct structure."""
        results = hawking_page_phase_diagram(K3_SIGMA, [1, 5, 10])
        assert len(results) == 3
        for r in results:
            assert "beta_HP_classical" in r
            assert "delta_beta" in r
            assert abs(r["beta_HP_classical"] - 2 * PI) < 1e-12


# =========================================================================
# Section 10: Borcherds / second-quantized tests (7 tests)
# =========================================================================

class TestBorcherds:
    """Second-quantized partition function and Borcherds products."""

    def test_borcherds_weight_k3(self):
        """Weight of Phi_10 is 10 for K3."""
        assert borcherds_product_weight(24) == 10

    def test_borcherds_kappa_bps_k3(self):
        """kappa_BPS = chi(K3)/4 - 1 = 5."""
        assert borcherds_kappa_bps(24) == 5

    def test_borcherds_ratio_k3(self):
        """kappa_BPS / kappa(K3) = 5/2."""
        assert borcherds_ratio(K3_SIGMA, 24) == F(5, 2)

    def test_second_quantized_pf_low_n(self):
        """Check second-quantized partition function at low N."""
        pf = second_quantized_pf_coefficients(24, 3)
        assert pf[0] == 1
        assert pf[1] == 24
        assert pf[2] == 324

    def test_igusa_first_coeff(self):
        """First Fourier coefficient of Phi_10: tau(1) = 1."""
        coeffs = igusa_cusp_form_first_coefficients(5)
        assert coeffs[(1, 0)] == 1

    def test_igusa_ramanujan_tau(self):
        """tau(2) = -24 (Ramanujan tau function)."""
        coeffs = igusa_cusp_form_first_coefficients(5)
        assert coeffs[(2, 0)] == -24

    def test_second_quantized_pf_matches_gottsche(self):
        """second_quantized_pf_coefficients must equal dmvv_partition_function_z0."""
        for N_max in [3, 5]:
            a = second_quantized_pf_coefficients(24, N_max)
            b = dmvv_partition_function_z0(N_max, 24)
            assert a == b


# =========================================================================
# Section 11: Cross-check and consistency tests (7 tests)
# =========================================================================

class TestCrossChecks:
    """Multi-path verification and cross-consistency checks."""

    def test_colored_partitions_base_cases(self):
        """Colored partitions: p(0, c) = 1, p(n<0, c) = 0."""
        for c in [1, 6, 24]:
            assert colored_partitions(0, c) == 1
            assert colored_partitions(-1, c) == 0

    def test_colored_partitions_1color(self):
        """1-colored partitions = ordinary partition function."""
        # p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7
        expected = {1: 1, 2: 2, 3: 3, 4: 5, 5: 7}
        for n, p_n in expected.items():
            assert colored_partitions(n, 1) == p_n

    def test_k3_t4_same_c_different_chi(self):
        """K3 and T^4 have same c = 6, same kappa = 2, but chi differs."""
        assert K3_SIGMA.central_charge == T4_SIGMA.central_charge
        assert K3_SIGMA.kappa == T4_SIGMA.kappa
        assert K3_SIGMA.chi != T4_SIGMA.chi

    def test_gottsche_k3_vs_t4(self):
        """Gottsche formula: K3 (chi=24) and T^4 (chi=0) differ.

        For T^4 with chi=0: prod (1-p^n)^0 = 1, so chi(Sym^N) = delta_{N,0}.
        """
        # T^4 has chi = 0
        for N in range(1, 5):
            assert gottsche_euler_char(N, 0) == 0
        assert gottsche_euler_char(0, 0) == 1

    def test_dmvv_f1_prime_n(self):
        """For prime N: sigma_{-1}(N) = 1 + 1/N."""
        for p in [2, 3, 5, 7]:
            f1 = dmvv_connected_f1(p, 24)
            expected = F(24) * (F(1) + F(1, p))
            assert f1 == expected

    def test_kappa_over_c_families(self):
        """kappa/c ratios for different families."""
        # Free boson: kappa/c = 1
        assert large_n_kappa_over_c(FREE_BOSON) == F(1)
        # K3: kappa/c = 2/6 = 1/3
        assert large_n_kappa_over_c(K3_SIGMA) == F(1, 3)
        # T^4: kappa/c = 2/6 = 1/3
        assert large_n_kappa_over_c(T4_SIGMA) == F(1, 3)

    def test_twist_weight_sum_for_full_cycle(self):
        """Total twist weight for the full N-cycle: h = (c/24)(N - 1/N)."""
        c = F(6)
        for N in range(2, 8):
            h = twist_sector_weight(c, (N,))
            expected = c * F(N * N - 1, 24 * N)
            assert h == expected


# =========================================================================
# Section 12: Seed theory tests (4 tests)
# =========================================================================

class TestSeedTheory:
    """Tests for the seed theory data structures."""

    def test_seed_k3_data(self):
        """K3 sigma model: c=6, kappa=2, dim=2, chi=24."""
        assert K3_SIGMA.central_charge == F(6)
        assert K3_SIGMA.kappa == F(2)
        assert K3_SIGMA.dim_target == 2
        assert K3_SIGMA.chi == 24
        assert K3_SIGMA.shadow_depth == 2

    def test_seed_t4_data(self):
        """T^4 sigma model: c=6, kappa=2, dim=2, chi=0."""
        assert T4_SIGMA.central_charge == F(6)
        assert T4_SIGMA.kappa == F(2)
        assert T4_SIGMA.dim_target == 2
        assert T4_SIGMA.chi == 0

    def test_seed_free_boson_data(self):
        """Free boson: c=1, kappa=1, dim=1."""
        assert FREE_BOSON.central_charge == F(1)
        assert FREE_BOSON.kappa == F(1)

    def test_seed_leech_data(self):
        """Leech VOA: c=24, kappa=24, dim=24."""
        assert LEECH_VOA.central_charge == F(24)
        assert LEECH_VOA.kappa == F(24)
        assert LEECH_VOA.dim_target == 24
