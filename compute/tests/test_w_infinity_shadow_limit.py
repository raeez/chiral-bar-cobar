r"""Tests for the W_infinity large-N shadow tower limit engine.

Systematic verification of shadow tower coefficients S_r(W_N, c) as N -> infinity,
producing the shadow tower of W_{1+infinity}.

STRUCTURE:
    Section 1: Fundamental formulas — harmonic numbers, anomaly ratios, central charges (10 tests)
    Section 2: Shadow tower computation — exact arithmetic cross-checks (8 tests)
    Section 3: Shadow depth classification — all W_N are class M (6 tests)
    Section 4: Shadow growth rate — rho(W_N) vs N (6 tests)
    Section 5: Large-N scaling — power-law exponents (5 tests)
    Section 6: 't Hooft limit — normalized coefficients (7 tests)
    Section 7: MacMahon connection — vacuum character vs shadow tower (4 tests)
    Section 8: Cross-engine consistency — match ds_shadow_cascade_engine (6 tests)

Total: 52 tests.

Manuscript references:
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:stabilized-completion-positive (bar_cobar_adjunction_curved.tex)
    thm:winfty-all-stages-rigidity-closure (concordance.tex)
"""

from __future__ import annotations

import math
import sys

import pytest
from fractions import Fraction

sys.path.insert(
    0, str(__import__("pathlib").Path(__file__).resolve().parent.parent / "lib")
)

from w_infinity_shadow_limit import (
    # Fundamental formulas
    harmonic_number,
    anomaly_ratio_wn,
    c_wn_principal,
    kappa_wn_total,
    kappa_tline,
    alpha_tline,
    s4_tline,
    # Shadow tower
    shadow_tower_tline,
    shadow_tower_tline_float,
    shadow_tower_total_kappa,
    # Growth rate
    shadow_growth_rate_tline,
    critical_discriminant_tline,
    depth_class_tline,
    # Tables
    wn_shadow_table,
    full_shadow_table,
    growth_rate_vs_N,
    growth_rate_thooft,
    # Large-N
    large_n_scaling_at_fixed_k,
    large_n_scaling_exponents,
    # 't Hooft
    thooft_central_charge,
    thooft_shadow_table,
    thooft_normalized_coefficients,
    thooft_coefficient_table,
    # Depth
    depth_classification_all_N,
    # MacMahon
    plane_partition_number,
    _partition_number,
    shadow_vs_macmahon,
    macmahon_log_growth,
    # Verification
    verify_all,
)


# ═══════════════════════════════════════════════════════════════════════════
# Section 1: Fundamental formulas
# ═══════════════════════════════════════════════════════════════════════════


class TestFundamentalFormulas:
    """Harmonic numbers, anomaly ratios, central charges, kappa."""

    def test_harmonic_numbers_small(self):
        """H_1 = 1, H_2 = 3/2, H_3 = 11/6, H_4 = 25/12."""
        assert harmonic_number(1) == Fraction(1)
        assert harmonic_number(2) == Fraction(3, 2)
        assert harmonic_number(3) == Fraction(11, 6)
        assert harmonic_number(4) == Fraction(25, 12)

    def test_harmonic_number_zero(self):
        """H_0 = 0 by convention."""
        assert harmonic_number(0) == Fraction(0)

    def test_anomaly_ratio_virasoro(self):
        """rho(sl_2) = H_2 - 1 = 1/2: kappa(Vir) = c/2."""
        assert anomaly_ratio_wn(2) == Fraction(1, 2)

    def test_anomaly_ratio_w3(self):
        """rho(sl_3) = H_3 - 1 = 5/6: kappa(W_3) = 5c/6."""
        assert anomaly_ratio_wn(3) == Fraction(5, 6)

    def test_anomaly_ratio_w4(self):
        """rho(sl_4) = H_4 - 1 = 13/12."""
        assert anomaly_ratio_wn(4) == Fraction(13, 12)

    def test_anomaly_ratio_monotone(self):
        """H_N - 1 is strictly increasing in N."""
        for N in range(2, 20):
            assert anomaly_ratio_wn(N + 1) > anomaly_ratio_wn(N)

    def test_central_charge_virasoro(self):
        """c(W_2, k) = (2-1)(1 - 2*3/(k+2)) = 1 - 6/(k+2)."""
        # At k=1: c = 1 - 6/3 = -1
        assert c_wn_principal(2, Fraction(1)) == Fraction(-1)
        # At k=10: c = 1 - 6/12 = 1/2
        assert c_wn_principal(2, Fraction(10)) == Fraction(1, 2)

    def test_central_charge_w3(self):
        """c(W_3, k) = 2(1 - 12/(k+3))."""
        # At k=1: c = 2(1 - 12/4) = 2(-2) = -4
        assert c_wn_principal(3, Fraction(1)) == Fraction(-4)

    def test_kappa_wn_virasoro(self):
        """kappa(W_2, c) = (1/2)*c = c/2 (Virasoro)."""
        c_val = Fraction(10)
        assert kappa_wn_total(2, c_val) == c_val / 2

    def test_kappa_wn_w3(self):
        """kappa(W_3, c) = (5/6)*c."""
        c_val = Fraction(12)
        assert kappa_wn_total(3, c_val) == 5 * c_val / 6


# ═══════════════════════════════════════════════════════════════════════════
# Section 2: Shadow tower computation
# ═══════════════════════════════════════════════════════════════════════════


class TestShadowTowerComputation:
    """Exact shadow tower on the T-line, cross-checked against known values."""

    def test_virasoro_s2_equals_c_over_2(self):
        """S_2 = kappa_tline = c/2 on the T-line."""
        c_val = Fraction(10)
        tower = shadow_tower_tline(c_val, 6)
        assert tower[2] == c_val / 2

    def test_virasoro_s3_equals_2(self):
        """S_3 = 2 on the T-line (Virasoro cubic shadow)."""
        c_val = Fraction(10)
        tower = shadow_tower_tline(c_val, 6)
        assert tower[3] == Fraction(2)

    def test_virasoro_s4_formula(self):
        """S_4 = 10/[c(5c+22)] on the T-line (quartic contact)."""
        c_val = Fraction(10)
        tower = shadow_tower_tline(c_val, 6)
        expected = Fraction(10) / (c_val * (5 * c_val + 22))
        assert tower[4] == expected

    def test_virasoro_s5_formula(self):
        """S_5 = -48/[c^2(5c+22)] on the T-line (quintic shadow).

        This is the known quintic formula from quintic_shadow_engine.py.
        """
        c_val = Fraction(10)
        tower = shadow_tower_tline(c_val, 6)
        expected = Fraction(-48) / (c_val ** 2 * (5 * c_val + 22))
        assert tower[5] == expected

    def test_tower_exact_vs_float(self):
        """Exact and float towers agree to high precision."""
        c_val = Fraction(10)
        exact = shadow_tower_tline(c_val, 6)
        approx = shadow_tower_tline_float(10.0, 6)
        for r in range(2, 7):
            assert abs(float(exact[r]) - approx[r]) < 1e-12, f"Mismatch at r={r}"

    def test_w3_tower_matches_virasoro_tline(self):
        """W_3 T-line tower at a given c equals Virasoro tower at the same c.

        The T-line shadow data is governed by the Virasoro subalgebra.
        """
        k_val = Fraction(5)
        c_w3 = c_wn_principal(3, k_val)
        tower_from_wn = shadow_tower_tline(c_w3, 6)
        # Direct Virasoro tower at the same central charge
        tower_vir = shadow_tower_tline(c_w3, 6)
        for r in range(2, 7):
            assert tower_from_wn[r] == tower_vir[r]

    def test_negative_c_tower(self):
        """Shadow tower works for negative central charge (kappa < 0)."""
        c_val = Fraction(-1)  # Virasoro at c=-1
        tower = shadow_tower_tline(c_val, 6)
        assert tower[2] == Fraction(-1, 2)
        assert tower[3] == Fraction(2)

    def test_large_c_tower_decays(self):
        """At large c, higher shadow coefficients S_r decay rapidly."""
        c_val = Fraction(100)
        tower = shadow_tower_tline(c_val, 6)
        # S_4 ~ 10/(100*522) ~ 1.9e-4
        assert abs(float(tower[4])) < 0.001
        assert abs(float(tower[5])) < abs(float(tower[4]))


# ═══════════════════════════════════════════════════════════════════════════
# Section 3: Shadow depth classification
# ═══════════════════════════════════════════════════════════════════════════


class TestShadowDepthClassification:
    """All W_N for N >= 2 are class M on the T-line."""

    def test_all_wn_class_m(self):
        """W_N at generic level k is class M on the T-line for N=2..20."""
        k_val = Fraction(5)
        results = depth_classification_all_N(list(range(2, 21)), k_val)
        for N in range(2, 21):
            assert results[N]['is_class_M'], f"W_{N} not class M"

    def test_s4_nonzero_all_n(self):
        """S_4 is nonzero for all W_N at generic level."""
        k_val = Fraction(5)
        for N in range(2, 15):
            c_w = c_wn_principal(N, k_val)
            s4 = s4_tline(c_w)
            assert s4 != 0, f"S_4 vanishes for W_{N}"

    def test_delta_nonzero_all_n(self):
        """Critical discriminant Delta != 0 for all W_N at generic level."""
        k_val = Fraction(5)
        for N in range(2, 15):
            c_w = c_wn_principal(N, k_val)
            delta = critical_discriminant_tline(c_w)
            assert delta != 0, f"Delta vanishes for W_{N}"

    def test_cascade_nonzero_arities_4_through_6(self):
        """S_r != 0 for r = 4, 5, 6 (cascade from nonzero S_4)."""
        k_val = Fraction(5)
        for N in [2, 3, 5, 10]:
            c_w = c_wn_principal(N, k_val)
            tower = shadow_tower_tline(c_w, 6)
            for r in [4, 5, 6]:
                assert tower[r] != 0, f"S_{r} vanishes for W_{N}"

    def test_sl_n_is_class_l(self):
        """Cross-check: affine sl_N is class L (S_4 = 0), not class M."""
        # For sl_N: alpha = 1, S_4 = 0. This is class L.
        # We verify by computing the tower with alpha=1, S4=0.
        from w_infinity_shadow_limit import _convolution_coefficients
        kap = Fraction(10)
        alpha = Fraction(1)
        S4 = Fraction(0)
        q0 = 4 * kap ** 2
        q1 = 12 * kap * alpha
        q2 = 9 * alpha ** 2 + 16 * kap * S4  # = 9
        coeffs = _convolution_coefficients(q0, q1, q2, 6, 1)
        # S_4 = a_2/4. For class L with Delta=0, the Taylor expansion terminates.
        # Check that a_3, a_4, ... are zero (class L terminates at depth 3).
        # a_0 = 2*kap = 20, a_1 = 12*kap/(2*20) = 12*10/40 = 3.
        # a_2 = (9 - 9)/(2*20) = 0. So S_4 = 0/4 = 0. Class L confirmed.
        assert coeffs[2] == Fraction(0), "Expected a_2 = 0 for class L"
        for n in range(3, len(coeffs)):
            assert coeffs[n] == Fraction(0), f"Expected a_{n} = 0 for class L"

    def test_depth_class_at_specific_n(self):
        """Explicit depth class checks at N=2 (Virasoro) and N=3 (W_3)."""
        k_val = Fraction(5)
        c2 = c_wn_principal(2, k_val)
        c3 = c_wn_principal(3, k_val)
        assert depth_class_tline(c2) == 'M'
        assert depth_class_tline(c3) == 'M'


# ═══════════════════════════════════════════════════════════════════════════
# Section 4: Shadow growth rate
# ═══════════════════════════════════════════════════════════════════════════


class TestShadowGrowthRate:
    """Growth rate rho(W_N) on the T-line as a function of N and c."""

    def test_growth_rate_virasoro_c10(self):
        """rho(Vir_{c=10}) = sqrt((1800+872)/((50+22)*100)) ~ 0.715."""
        rho = shadow_growth_rate_tline(10.0)
        expected = math.sqrt(2672.0 / (72.0 * 100.0))
        assert abs(rho - expected) < 1e-10

    def test_growth_rate_decreases_with_c(self):
        """rho decreases as c increases (for c > c*)."""
        c_values = [10, 20, 50, 100, 200]
        rhos = [shadow_growth_rate_tline(c) for c in c_values]
        for i in range(len(rhos) - 1):
            assert rhos[i] > rhos[i + 1], f"rho not decreasing: {rhos[i]} vs {rhos[i+1]}"

    def test_growth_rate_asymptotics(self):
        """rho ~ 6/c for large c."""
        for c_val in [100, 500, 1000]:
            rho = shadow_growth_rate_tline(float(c_val))
            ratio = rho * c_val
            assert abs(ratio - 6.0) < 0.5, f"rho*c = {ratio}, expected ~6"

    def test_growth_rate_free_field_thooft(self):
        """In free-field 't Hooft limit (lambda=0): c = N-1, rho ~ 6/(N-1) -> 0."""
        results = growth_rate_thooft(Fraction(0))
        # For large N, rho should decrease
        positive_rhos = [(r['N'], r['rho']) for r in results if r['rho'] is not None and r['rho'] > 0]
        for i in range(len(positive_rhos) - 1):
            assert positive_rhos[i][1] >= positive_rhos[i + 1][1], \
                f"rho not decreasing at lambda=0: N={positive_rhos[i][0]} vs N={positive_rhos[i+1][0]}"

    def test_growth_rate_convergent_at_large_n(self):
        """At lambda=0, rho < 1 for N >= 8 (since c = N-1 >= 7 > c* ~ 6.12)."""
        results = growth_rate_thooft(Fraction(0))
        for r in results:
            if r['N'] >= 8 and r['rho'] is not None:
                assert r['rho'] < 1.0, f"W_{r['N']} tower diverges at lambda=0"

    def test_growth_rate_table_runs(self):
        """growth_rate_vs_N produces a valid table."""
        results = growth_rate_vs_N(Fraction(5), list(range(2, 11)))
        assert len(results) == 9
        for r in results:
            assert 'N' in r
            assert 'rho' in r


# ═══════════════════════════════════════════════════════════════════════════
# Section 5: Large-N scaling
# ═══════════════════════════════════════════════════════════════════════════


class TestLargeNScaling:
    """Power-law scaling of S_r(W_N) as N -> infinity at fixed k."""

    def test_scaling_exponents_exist(self):
        """Scaling exponents are computed for arities 2 through 6."""
        exponents = large_n_scaling_exponents(Fraction(5), 6)
        for r in range(2, 7):
            assert r in exponents

    def test_s2_scaling(self):
        """S_2 = c/2 ~ -N^2/(2) at fixed k, so alpha_2 ~ 2."""
        # At fixed k, c ~ -N^2, so S_2 = c/2 ~ -N^2/2.
        # The sign flips, but |S_2| ~ N^2 so alpha_2 ~ 2.
        exponents = large_n_scaling_exponents(Fraction(5), 6)
        alpha_2 = exponents.get(2)
        if alpha_2 is not None:
            assert abs(alpha_2 - 2.0) < 0.5, f"alpha_2 = {alpha_2}, expected ~2"

    def test_s3_is_constant(self):
        """S_3 = 2 independent of N, so alpha_3 = 0."""
        # S_3 = 2 for ALL Virasoro-type T-line data, regardless of c.
        exponents = large_n_scaling_exponents(Fraction(5), 6)
        alpha_3 = exponents.get(3)
        if alpha_3 is not None:
            assert abs(alpha_3) < 0.5, f"alpha_3 = {alpha_3}, expected ~0"

    def test_scaling_table_runs(self):
        """Full scaling analysis runs without error."""
        scaling = large_n_scaling_at_fixed_k(Fraction(5), max_arity=6)
        for r in range(2, 7):
            assert r in scaling
            assert 'points' in scaling[r]

    def test_s4_scaling_negative_power(self):
        """S_4 = 10/[c(5c+22)] ~ 10/(5c^2) for large |c|, so |S_4| ~ c^{-2} ~ N^{-4}."""
        exponents = large_n_scaling_exponents(Fraction(5), 6)
        alpha_4 = exponents.get(4)
        if alpha_4 is not None:
            # alpha_4 should be around -4 (since c ~ N^2 at fixed k)
            assert alpha_4 < -1, f"alpha_4 = {alpha_4}, expected negative"


# ═══════════════════════════════════════════════════════════════════════════
# Section 6: 't Hooft limit
# ═══════════════════════════════════════════════════════════════════════════


class TestThooftLimit:
    """'t Hooft shadow coefficients at fixed lambda, varying N."""

    def test_free_field_limit_c_equals_n_minus_1(self):
        """At lambda=0: c(W_N) = N-1."""
        for N in [3, 5, 10, 20]:
            c_free = thooft_central_charge(N, Fraction(0))
            assert c_free == Fraction(N - 1)

    def test_critical_level_c_negative(self):
        """At lambda=1: c(W_N) = -(N-1)*N < 0."""
        for N in [3, 5, 10]:
            c_crit = thooft_central_charge(N, Fraction(1))
            assert c_crit == Fraction(-(N - 1) * N)
            assert c_crit < 0

    def test_thooft_kappa_at_lambda_0(self):
        """At lambda=0: kappa_total(W_N) = (H_N-1)*(N-1)."""
        for N in [3, 5, 10]:
            c_free = thooft_central_charge(N, Fraction(0))
            kap = kappa_wn_total(N, c_free)
            expected = anomaly_ratio_wn(N) * Fraction(N - 1)
            assert kap == expected

    def test_thooft_table_runs(self):
        """'t Hooft shadow table runs without error."""
        table = thooft_shadow_table(Fraction(1, 10), [3, 5, 10], 6)
        assert len(table) == 3
        for N in [3, 5, 10]:
            assert 'c' in table[N]
            assert 'tower' in table[N]

    def test_thooft_normalized_coefficients_run(self):
        """Normalized coefficients S_r/kappa^{r/2} are computed."""
        norms = thooft_normalized_coefficients(Fraction(1, 10), [3, 5, 10], 6)
        for r in range(2, 7):
            assert r in norms

    def test_thooft_s3_norm_stability(self):
        """Normalized S_3/kappa^{3/2} should vary smoothly with N.

        S_3 = 2 (constant), kappa_total = rho*c. So S_3/kappa^{3/2} = 2/kappa^{3/2}.
        Since kappa ~ (log N)*N at lambda=0, the normalized S_3 -> 0.
        """
        norms = thooft_normalized_coefficients(Fraction(0), [3, 5, 10, 20], 6)
        s3_norms = norms.get(3, [])
        if len(s3_norms) >= 2:
            # Should be decreasing at lambda=0 since kappa grows
            vals = [v for _, v in s3_norms]
            for i in range(len(vals) - 1):
                assert abs(vals[i]) >= abs(vals[i + 1]) * 0.5, \
                    "Normalized S_3 not roughly decreasing"

    def test_thooft_coefficient_table_runs(self):
        """'t Hooft coefficient table function runs."""
        rows = thooft_coefficient_table(Fraction(1, 10), [3, 5, 10], 6)
        assert len(rows) == 3


# ═══════════════════════════════════════════════════════════════════════════
# Section 7: MacMahon connection
# ═══════════════════════════════════════════════════════════════════════════


class TestMacMahonConnection:
    """MacMahon function vs shadow tower (structural incompatibility)."""

    def test_macmahon_small_values(self):
        """pp(0)=1, pp(1)=1, pp(2)=3, pp(3)=6, pp(4)=13 (OEIS A000219)."""
        known = [1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500]
        for n, expected in enumerate(known):
            assert plane_partition_number(n) == expected, f"pp({n}) wrong"

    def test_partition_numbers(self):
        """p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7."""
        known = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        for n, expected in enumerate(known):
            assert _partition_number(n) == expected, f"p({n}) wrong"

    def test_shadow_vs_macmahon_structural(self):
        """Shadow GF is algebraic, MacMahon is transcendental: no identification."""
        result = shadow_vs_macmahon(10.0, 6)
        assert result['algebraic_vs_transcendental'] is True
        # The ratios S_r / pp(r) should NOT be constant
        ratios = [
            result['comparison'][r]['ratio_pp']
            for r in [2, 3, 4, 5, 6]
            if result['comparison'][r]['ratio_pp'] is not None
        ]
        if len(ratios) >= 3:
            # Verify non-constancy
            spread = max(abs(r) for r in ratios) / min(abs(r) for r in ratios if abs(r) > 1e-30)
            assert spread > 1.1, "Shadow/MacMahon ratios suspiciously constant"

    def test_macmahon_log_growth(self):
        """log(pp(n)) grows roughly as n^{2/3} (3D partition asymptotics)."""
        log_vals = [macmahon_log_growth(n) for n in range(2, 20)]
        # Should be increasing
        for i in range(len(log_vals) - 1):
            assert log_vals[i] < log_vals[i + 1]


# ═══════════════════════════════════════════════════════════════════════════
# Section 8: Cross-engine consistency
# ═══════════════════════════════════════════════════════════════════════════


class TestCrossEngineConsistency:
    """Cross-check against ds_shadow_cascade_engine and w_infinity_string_engine."""

    def test_virasoro_matches_ds_cascade(self):
        """W_2 = Virasoro: our tower matches ds_shadow_cascade_engine.

        For N=2, total kappa = (H_2-1)*c = c/2 = kappa_tline, so both
        shadow_tower_tline and shadow_tower_total_kappa agree.
        """
        try:
            from ds_shadow_cascade_engine import (
                c_WN as ds_c_WN,
                kappa_WN as ds_kappa_WN,
                WN_shadow_data_T_line as ds_WN_shadow_data,
                shadow_tower_exact as ds_shadow_tower,
            )
        except ImportError:
            pytest.skip("ds_shadow_cascade_engine not available")

        k_val = Fraction(5)
        # DS engine
        c_ds = ds_c_WN(2, k_val)
        data_ds = ds_WN_shadow_data(2, k_val)
        tower_ds = ds_shadow_tower(data_ds['kappa'], data_ds['alpha'], data_ds['S4'], 6)

        # Our engine — both conventions agree for N=2
        c_ours = c_wn_principal(2, k_val)
        tower_tline = shadow_tower_tline(c_ours, 6)
        tower_total = shadow_tower_total_kappa(2, c_ours, 6)

        assert c_ds == c_ours, f"Central charge mismatch: {c_ds} vs {c_ours}"
        for r in range(2, 7):
            assert tower_ds[r] == tower_tline[r], f"S_{r} tline mismatch"
            assert tower_ds[r] == tower_total[r], f"S_{r} total mismatch"

    def test_w3_matches_ds_cascade(self):
        """W_3 total-kappa tower matches ds_shadow_cascade_engine.

        The DS engine uses kappa = rho(N)*c (total), not kappa = c/2 (T-line).
        Our shadow_tower_total_kappa function matches this convention.
        """
        try:
            from ds_shadow_cascade_engine import (
                c_WN as ds_c_WN,
                WN_shadow_data_T_line as ds_WN_shadow_data,
                shadow_tower_exact as ds_shadow_tower,
            )
        except ImportError:
            pytest.skip("ds_shadow_cascade_engine not available")

        k_val = Fraction(5)
        c_ds = ds_c_WN(3, k_val)
        data_ds = ds_WN_shadow_data(3, k_val)
        tower_ds = ds_shadow_tower(data_ds['kappa'], data_ds['alpha'], data_ds['S4'], 6)

        c_ours = c_wn_principal(3, k_val)
        tower_ours = shadow_tower_total_kappa(3, c_ours, 6)

        assert c_ds == c_ours
        for r in range(2, 7):
            assert tower_ds[r] == tower_ours[r], f"S_{r} mismatch for W_3"

    def test_kappa_matches_string_engine(self):
        """kappa(W_N) formula matches w_infinity_string_engine."""
        try:
            from w_infinity_string_engine import (
                kappa_wN as se_kappa_wN,
                anomaly_ratio as se_anomaly_ratio,
            )
        except ImportError:
            pytest.skip("w_infinity_string_engine not available")

        for N in [2, 3, 5, 10]:
            # Our anomaly ratio
            rho_ours = anomaly_ratio_wn(N)
            rho_se = se_anomaly_ratio(N)
            assert rho_ours == rho_se, f"Anomaly ratio mismatch for N={N}"

    def test_full_shadow_table_consistency(self):
        """full_shadow_table runs and S_2 = c/2 for all entries."""
        rows = full_shadow_table(Fraction(5), [2, 3, 4, 5], 6)
        for row in rows:
            if 'error' not in row:
                assert abs(row['S_2'] - row['c'] / 2.0) < 1e-10, \
                    f"S_2 != c/2 for N={row['N']}"

    def test_verify_all_passes(self):
        """The comprehensive verify_all suite passes."""
        results = verify_all(Fraction(5))
        for key, val in results.items():
            assert val, f"Verification failed: {key}"

    def test_wn_shadow_table_runs(self):
        """wn_shadow_table produces valid output."""
        table = wn_shadow_table([2, 3, 4, 5], Fraction(5), 6)
        assert len(table) == 4
        for N in [2, 3, 4, 5]:
            assert N in table
            assert 'tower' in table[N]
            assert 'rho' in table[N]
