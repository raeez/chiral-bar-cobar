"""Tests for Bekenstein-Hawking entropy from the shadow CohFT.

Three-path verification:
    (a) Saddle-point of Z^sh
    (b) Cardy formula from modular S-transform of F_1
    (c) Ryu-Takayanagi from entanglement

Multi-path verification mandate (CLAUDE.md): every numerical result needs
3+ independent verification paths.

AP warnings checked:
    AP20: kappa(A) is intrinsic to A. kappa_eff = kappa(matter) + kappa(ghost).
    AP22: sum F_g hbar^{2g}, NOT hbar^{2g-2}.
    AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
    AP29: kappa_eff = (c-26)/2 != delta_kappa = c - 13.
    AP31: kappa = 0 does NOT imply Theta = 0.
    AP39: kappa = c/2 for Virasoro ONLY.
    AP46: eta(q) = q^{1/24} prod(1-q^n).
"""

import math
import pytest
from fractions import Fraction

from compute.lib.bh_entropy_shadow_cohft import (
    kappa_virasoro,
    kappa_virasoro_exact,
    kappa_eff_gravity,
    lambda_fp_float,
    F_g_virasoro,
    F_g_virasoro_exact,
    free_energy_table,
    shadow_log_partition,
    shadow_log_partition_closed,
    shadow_partition_function,
    shadow_partition_closed,
    cardy_entropy,
    btz_entropy,
    btz_from_mass_spin,
    cardy_from_shadow_F1,
    saddle_point_entropy,
    rt_entropy,
    rt_to_bh_matching,
    entanglement_complementarity,
    three_path_verification,
    shadow_genus_table,
    borel_transform_genus,
    large_c_saddle,
    non_perturbative_correction,
    special_central_charges,
    derivation_assessment,
)

PI = math.pi
TWO_PI = 2 * PI


# =====================================================================
# Test 1-3: kappa values (AP39)
# =====================================================================

class TestKappaValues:
    """Verify kappa(Vir_c) = c/2 and related invariants."""

    def test_kappa_virasoro_basic(self):
        """kappa(Vir_c) = c/2 for several values of c."""
        for c in [1, 13, 26, 100]:
            assert kappa_virasoro(c) == c / 2.0

    def test_kappa_exact(self):
        """Exact rational kappa values."""
        assert kappa_virasoro_exact(1) == Fraction(1, 2)
        assert kappa_virasoro_exact(13) == Fraction(13, 2)
        assert kappa_virasoro_exact(26) == Fraction(13)

    def test_kappa_eff_gravity(self):
        """kappa_eff = (c-26)/2: vanishes at c=26, not at c=13 (AP29)."""
        assert kappa_eff_gravity(26) == 0.0
        assert kappa_eff_gravity(13) == -6.5
        assert kappa_eff_gravity(0) == -13.0
        # AP29: kappa_eff != delta_kappa
        # delta_kappa = kappa - kappa' = c/2 - (26-c)/2 = c - 13
        # kappa_eff = c/2 - 13 = (c-26)/2
        assert kappa_eff_gravity(13) != (13 - 13)  # delta_kappa = 0 at c=13


# =====================================================================
# Test 4-6: Faber-Pandharipande numbers
# =====================================================================

class TestFaberPandharipande:
    """Verify lambda_g^FP values and F_g = kappa * lambda_g^FP."""

    def test_lambda_1(self):
        """lambda_1^FP = 1/24."""
        assert abs(lambda_fp_float(1) - 1.0 / 24.0) < 1e-15

    def test_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        assert abs(lambda_fp_float(2) - 7.0 / 5760.0) < 1e-15

    def test_F1_virasoro(self):
        """F_1(Vir_c) = c/48 (the genus-1 free energy controlling Cardy)."""
        for c in [1, 13, 26, 100]:
            expected = c / 48.0
            assert abs(F_g_virasoro(c, 1) - expected) < 1e-14


# =====================================================================
# Test 7-9: Shadow partition function convergence
# =====================================================================

class TestShadowPartition:
    """Verify convergence and closed-form agreement."""

    def test_series_closed_form_agreement(self):
        """Series and closed form of log Z^sh agree at small hbar."""
        for c in [1.0, 13.0, 26.0]:
            for hbar in [0.5, 1.0, 2.0]:
                series_val = shadow_log_partition(c, hbar, g_max=50)
                closed_val = shadow_log_partition_closed(c, hbar)
                rel = abs(series_val - closed_val) / max(abs(closed_val), 1e-15)
                assert rel < 1e-10, f"c={c}, hbar={hbar}: series={series_val}, closed={closed_val}"

    def test_convergence_within_radius(self):
        """Shadow partition converges for |hbar| < 2*pi."""
        c = 26.0
        # Well within convergence radius
        Z1 = shadow_partition_closed(c, 1.0)
        assert Z1 > 0 and math.isfinite(Z1)
        # Near the boundary
        Z_near = shadow_partition_closed(c, 5.0)
        assert math.isfinite(Z_near)

    def test_closed_form_is_sin_based(self):
        """log Z^sh = kappa * [(h/2)/sin(h/2) - 1]."""
        c = 10.0
        hbar = 1.5
        kappa = c / 2.0
        expected = kappa * (hbar / 2.0 / math.sin(hbar / 2.0) - 1.0)
        actual = shadow_log_partition_closed(c, hbar)
        assert abs(actual - expected) < 1e-14


# =====================================================================
# Test 10-13: PATH (a) — Saddle-point
# =====================================================================

class TestPathA:
    """Saddle-point extraction of Bekenstein-Hawking entropy."""

    def test_saddle_gives_cardy(self):
        """Saddle-point entropy equals 2pi sqrt(c Delta/6)."""
        for c in [1.0, 13.0, 26.0, 100.0]:
            for Delta in [1.0, 10.0, 100.0]:
                sp = saddle_point_entropy(c, Delta)
                expected = 2 * PI * math.sqrt(c * Delta / 6.0)
                assert abs(sp['S_BH'] - expected) < 1e-10

    def test_log_correction_coefficient(self):
        """The one-loop log correction is -(3/2) log(S_BH/(2pi))."""
        sp = saddle_point_entropy(26.0, 100.0)
        S_BH = sp['S_BH']
        expected_log = -1.5 * math.log(S_BH / TWO_PI)
        assert abs(sp['log_correction'] - expected_log) < 1e-10

    def test_large_c_semiclassical(self):
        """At large c, corrections are suppressed."""
        Delta = 10.0
        result = large_c_saddle(Delta)
        # At c = 10000, relative log correction should be < 1%
        assert result['results'][10000.0]['relative_log'] < 0.01

    def test_F1_controls_leading(self):
        """F_1 = kappa/24 controls the Cardy density."""
        sp = saddle_point_entropy(26.0, 10.0)
        assert abs(sp['F_1'] - 26.0 / 48.0) < 1e-14


# =====================================================================
# Test 14-17: PATH (b) — Cardy formula
# =====================================================================

class TestPathB:
    """Cardy formula from modular S-transform of F_1."""

    def test_cardy_formula(self):
        """S = 2pi sqrt(c Delta / 6)."""
        assert abs(cardy_entropy(26.0, 10.0) - 2 * PI * math.sqrt(26 * 10 / 6.0)) < 1e-10

    def test_cardy_from_F1(self):
        """Cardy derived from F_1 matches direct formula."""
        result = cardy_from_shadow_F1(26.0, 100.0)
        assert result['match']

    def test_btz_non_chiral(self):
        """BTZ entropy is sum of left and right Cardy formulas."""
        c = 26.0
        h_L, h_R = 10.0, 5.0
        S = btz_entropy(c, h_L, h_R)
        expected = (2 * PI * math.sqrt(c * h_L / 6.0)
                    + 2 * PI * math.sqrt(c * h_R / 6.0))
        assert abs(S - expected) < 1e-10

    def test_btz_conformal_weight_area_match(self):
        """BTZ from conformal weights matches area formula."""
        for h_L in [5.0, 10.0, 50.0, 100.0]:
            result = btz_from_mass_spin(c=26.0, h_L=h_L, h_R=h_L, ell=1.0)
            assert result['match'], (
                f"h_L={h_L}: S_Cardy={result['S_Cardy']}, S_area={result['S_area']}"
            )


# =====================================================================
# Test 18-20: PATH (c) — RT / Entanglement
# =====================================================================

class TestPathC:
    """Ryu-Takayanagi from entanglement entropy."""

    def test_rt_entropy_formula(self):
        """S_EE = (c/3) log(L/eps)."""
        c = 26.0
        L = 100.0
        eps = 0.01
        S = rt_entropy(c, L, eps)
        expected = (c / 3.0) * math.log(L / eps)
        assert abs(S - expected) < 1e-10

    def test_rt_area_matching(self):
        """RT surface matches area formula for BTZ."""
        result = rt_to_bh_matching(c=26.0, r_plus=5.0, ell=1.0)
        assert result['area_cardy_match']

    def test_entanglement_complementarity(self):
        """S_EE(c) + S_EE(26-c) = (26/3) log(L/eps) (AP24)."""
        for c in [1.0, 5.0, 13.0, 20.0, 25.0]:
            result = entanglement_complementarity(c)
            assert result['match'], f"c={c}: sum={result['S_sum']}, expected={result['S_expected']}"

    def test_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c (AP24)."""
        for c in [0, 1, 5, 13, 20, 25, 26]:
            result = entanglement_complementarity(float(c))
            assert abs(result['kappa_sum'] - 13.0) < 1e-12


# =====================================================================
# Test 21-23: Three-path cross-verification
# =====================================================================

class TestThreePathCross:
    """Verify all three paths agree."""

    def test_three_paths_c1(self):
        """All three paths agree at c=1."""
        result = three_path_verification(1.0, 10.0)
        assert result['all_three_match']

    def test_three_paths_c26(self):
        """All three paths agree at c=26 (critical string)."""
        result = three_path_verification(26.0, 100.0)
        assert result['all_three_match']

    def test_three_paths_c100(self):
        """All three paths agree at c=100 (large c)."""
        result = three_path_verification(100.0, 50.0)
        assert result['all_three_match']


# =====================================================================
# Test 24-26: Non-perturbative structure
# =====================================================================

class TestNonPerturbative:
    """Non-perturbative corrections and Borel structure."""

    def test_borel_singularity_location(self):
        """First Borel singularity at u = (2pi)^2 ~ 39.48."""
        result = non_perturbative_correction(26.0, 1.0)
        assert abs(result['borel_singularity'] - (2 * PI) ** 2) < 1e-10

    def test_np_correction_suppressed(self):
        """Non-perturbative correction exponentially small at small hbar."""
        result = non_perturbative_correction(26.0, 0.5)
        # exp(-4pi^2 / 0.25) ~ exp(-158) ~ 0
        assert result['np_correction'] < 1e-60

    def test_borel_transform_finite(self):
        """Borel transform is finite (entire function in xi)."""
        for xi in [1.0, 10.0, 50.0]:
            B = borel_transform_genus(26.0, xi)
            assert math.isfinite(B)


# =====================================================================
# Test 27-29: Special central charges and AP checks
# =====================================================================

class TestSpecialCentralCharges:
    """Tests at physically distinguished central charges."""

    def test_self_dual_c13(self):
        """At c=13: self-dual, kappa = kappa' = 13/2 (AP24)."""
        data = special_central_charges()
        c13 = data['c=13']
        assert abs(c13['kappa'] - 6.5) < 1e-14
        assert abs(c13['kappa_dual'] - 6.5) < 1e-14
        assert abs(c13['kappa_sum'] - 13.0) < 1e-14

    def test_critical_c26(self):
        """At c=26: kappa_eff = 0 (anomaly cancellation, AP29)."""
        data = special_central_charges()
        c26 = data['c=26']
        assert abs(c26['kappa_eff']) < 1e-14
        # But kappa itself is NOT zero (AP31):
        assert abs(c26['kappa'] - 13.0) < 1e-14

    def test_ap31_kappa_zero_not_theta_zero(self):
        """AP31: kappa(Vir_0) = 0 but the A-infinity tower persists.

        The scalar free energies vanish but higher-arity shadows
        do not. We verify that F_g = 0 at c=0 (scalar level only).
        """
        for g in range(1, 6):
            assert F_g_virasoro(0.0, g) == 0.0
        # The FULL Theta_A is NOT zero at c=0 (Remark rem:vir-zero-type-V).
        # The A-infinity operations m_k for k >= 3 are c-independent.
        # This test verifies only the scalar (kappa) level.


# =====================================================================
# Test 30-32: Genus table computations
# =====================================================================

class TestGenusTable:
    """Compute F_g at specific central charges for g=1..10."""

    def test_genus_table_c1(self):
        """F_g(Vir_1) = (1/2) lambda_g^FP for g=1..10."""
        table = free_energy_table(1.0, 10)
        assert len(table) == 10
        # F_1 = 1/48
        assert abs(table[1] - 1.0 / 48.0) < 1e-15

    def test_genus_table_c26(self):
        """F_g(Vir_26) for g=1..10."""
        table = free_energy_table(26.0, 10)
        # F_1 = 26/48 = 13/24
        assert abs(table[1] - 13.0 / 24.0) < 1e-14
        # F_2 = 13 * 7/5760 = 91/5760
        assert abs(table[2] - 13.0 * 7.0 / 5760.0) < 1e-14

    def test_decay_rate(self):
        """F_{g+1}/F_g -> 1/(2pi)^2 ~ 0.0253 as g -> infty."""
        table = free_energy_table(26.0, 30)
        target = 1.0 / (2 * PI) ** 2
        # Check ratio at g=20 is close to target
        ratio = table[20] / table[19]
        assert abs(ratio - target) / target < 0.05


# =====================================================================
# Test 33: Derivation assessment
# =====================================================================

class TestAssessment:
    """Verify the epistemic assessment."""

    def test_assessment_structure(self):
        """The assessment should identify key results and gaps."""
        a = derivation_assessment()
        assert 'PROVED' in a['leading_order']
        assert 'HEURISTIC' in a['logarithmic']
        assert a['three_paths_agree'] == 'YES: saddle-point, Cardy, RT all give same leading answer'
        assert 'F_1' in a['key_input']
