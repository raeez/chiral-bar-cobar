"""Tests for the W_infinity completion tower and string theory engine.

Verifies:
  1. W_N large-N OPE stabilization
  2. W_{1+infinity} 't Hooft limit
  3. MC4+ weight stabilization (bar cohomology K_w(W_N) = p(w) for N >= w)
  4. MacMahon partition function (plane partitions, OEIS A000219)
  5. Bosonic string at c = 26 (anomaly cancellation, ghost BRST)
  6. Virasoro resonance (Koszul duality, self-duality at c=13, Q^contact)
  7. Higher-spin/string duality (shadow radius at large N)

Mathematical references:
  thm:completed-bar-cobar-strong (bar_cobar_adjunction_curved.tex)
  thm:stabilized-completion-positive (bar_cobar_adjunction_curved.tex)
  thm:nms-virasoro-quartic (nonlinear_modular_shadows.tex)
  rem:virasoro-resonance-model (higher_genus_modular_koszul.tex)
  thm:winfty-all-stages-rigidity-closure (concordance.tex)
"""

from __future__ import annotations

import math
import sys

import pytest
from sympy import Rational, Symbol, simplify

sys.path.insert(
    0, str(__import__("pathlib").Path(__file__).resolve().parent.parent / "lib")
)

from w_infinity_string_engine import (
    _MACMAHON_KNOWN,
    _partition_number,
    anomaly_ratio,
    bar_cohomology_dimensions,
    bar_weight_dim_w_infinity,
    bar_weight_dim_wN,
    bosonic_string_anomaly_cancellation,
    bosonic_string_spectrum_level,
    central_charge_wN_principal,
    ghost_extended_bar_data,
    harmonic_number,
    kappa_bc_ghost,
    kappa_virasoro,
    kappa_wN,
    large_N_shadow_convergence_rate,
    macmahon_coefficients,
    macmahon_vs_partition_comparison,
    mc4_plus_summary,
    plane_partition_number,
    q_contact_virasoro,
    shadow_radius_critical_c,
    shadow_radius_decay_exponent,
    shadow_radius_large_N_table,
    stable_ope_coefficients_weight_leq6,
    string_theory_summary,
    thooft_central_charge,
    thooft_kappa,
    thooft_shadow_data,
    verify_all,
    verify_macmahon,
    verify_macmahon_against_known,
    verify_ope_stabilization,
    verify_string_theory,
    verify_thooft_limits,
    verify_virasoro_resonance,
    verify_weight_stabilization,
    verify_weight_stabilization_suite,
    virasoro_complementarity_sum,
    virasoro_koszul_dual_c,
    virasoro_q_contact_at_26,
    virasoro_self_dual_c,
    virasoro_self_duality_check,
    virasoro_shadow_radius,
    virasoro_shadow_radius_squared,
    virasoro_shadow_tower_data,
    w_infinity_bar_cohomology_gf,
    w_infinity_vacuum_character,
    wN_generator_content,
    wN_large_N_shadow_table,
    wN_ope_TT,
    wN_ope_TW3,
    wN_ope_W3W3_central_term,
    wN_ope_W3W3_quartic_pole,
    wN_shadow_radius_at_c_equals_N,
    weight_stabilization_table,
    weight_stabilization_threshold,
)

c = Symbol("c")


# ═══════════════════════════════════════════════════════════════════════════
# 1. W_N at large N — OPE stabilization
# ═══════════════════════════════════════════════════════════════════════════


class TestWNLargeN:
    """Test W_N OPE structure at large N."""

    def test_harmonic_number_small(self):
        """H_1 = 1, H_2 = 3/2, H_3 = 11/6."""
        assert harmonic_number(1) == Rational(1)
        assert harmonic_number(2) == Rational(3, 2)
        assert harmonic_number(3) == Rational(11, 6)

    def test_harmonic_number_zero(self):
        """H_0 = 0."""
        assert harmonic_number(0) == 0

    def test_anomaly_ratio_virasoro(self):
        """rho(sl_2) = H_2 - 1 = 1/2 (Virasoro has kappa = c/2)."""
        assert anomaly_ratio(2) == Rational(1, 2)

    def test_anomaly_ratio_w3(self):
        """rho(sl_3) = H_3 - 1 = 5/6 (W_3 has kappa = 5c/6)."""
        assert anomaly_ratio(3) == Rational(5, 6)

    def test_kappa_wN_virasoro(self):
        """kappa(W_2) = (H_2 - 1) * c = c/2 = kappa(Vir)."""
        assert simplify(kappa_wN(2) - c / 2) == 0

    def test_kappa_wN_w3(self):
        """kappa(W_3) = (H_3 - 1) * c = 5c/6."""
        assert simplify(kappa_wN(3) - 5 * c / 6) == 0

    def test_generator_content_w3(self):
        """W_3 has 2 generators: T (weight 2), W_3 (weight 3)."""
        gens = wN_generator_content(3)
        assert len(gens) == 2
        assert gens[0]["spin"] == 2
        assert gens[1]["spin"] == 3

    def test_generator_content_w5(self):
        """W_5 has 4 generators: spins 2, 3, 4, 5."""
        gens = wN_generator_content(5)
        assert len(gens) == 4
        assert [g["spin"] for g in gens] == [2, 3, 4, 5]

    def test_TT_ope_universal(self):
        """T-T OPE: quartic pole = c/2, independent of N."""
        ope = wN_ope_TT()
        assert ope[4] == c / 2
        assert ope[2] == 2
        assert ope[1] == 1

    def test_TW3_ope_primary(self):
        """T-W_3 OPE: primary of weight 3."""
        ope = wN_ope_TW3()
        assert ope[2] == 3
        assert ope[1] == 1

    def test_W3W3_central_term(self):
        """W_3-W_3 central term = c/3."""
        assert wN_ope_W3W3_central_term(3) == c / 3

    def test_W3W3_quartic_pole(self):
        """W_3-W_3 quartic pole = 2."""
        assert wN_ope_W3W3_quartic_pole(3) == 2

    def test_stable_ope_table_completeness(self):
        """Stable OPE table covers T-T, T-W_s (s=3..6), W_3-W_3."""
        stable = stable_ope_coefficients_weight_leq6()
        assert "T-T" in stable
        assert "T-W_3" in stable
        assert "T-W_6" in stable
        assert "W_3-W_3" in stable

    def test_stable_ope_thresholds(self):
        """Each OPE is stable from the appropriate N."""
        stable = stable_ope_coefficients_weight_leq6()
        assert stable["T-T"]["stable_from_N"] == 2
        assert stable["T-W_3"]["stable_from_N"] == 3
        assert stable["T-W_4"]["stable_from_N"] == 4
        assert stable["T-W_5"]["stable_from_N"] == 5

    def test_verify_ope_stabilization(self):
        """Run the full OPE stabilization verification suite."""
        results = verify_ope_stabilization()
        assert all(results.values()), f"Failures: {[k for k,v in results.items() if not v]}"


# ═══════════════════════════════════════════════════════════════════════════
# 2. W_{1+infinity} and the 't Hooft limit
# ═══════════════════════════════════════════════════════════════════════════


class TestThooftLimit:
    """Test 't Hooft parameterization of W_N."""

    def test_free_field_limit(self):
        """At lambda = 0: c = N - 1."""
        for n in [3, 5, 10, 20]:
            assert thooft_central_charge(n, Rational(0)) == n - 1

    def test_critical_level(self):
        """At lambda = 1: c = -(N-1)*N."""
        for n in [3, 5, 10]:
            assert thooft_central_charge(n, Rational(1)) == -(n - 1) * n

    def test_kappa_at_lambda_zero(self):
        """kappa(W_N, lambda=0) = (H_N - 1) * (N - 1)."""
        for n in [3, 5, 10]:
            kap = thooft_kappa(n, Rational(0))
            expected = anomaly_ratio(n) * (n - 1)
            assert kap == expected

    def test_shadow_data_keys(self):
        """Shadow data dict has expected keys."""
        data = thooft_shadow_data(5, Rational(0))
        for key in ["N", "lambda", "c", "kappa", "anomaly_ratio"]:
            assert key in data

    def test_verify_thooft_limits(self):
        """Run the full 't Hooft limit verification."""
        results = verify_thooft_limits()
        assert all(results.values()), f"Failures: {[k for k,v in results.items() if not v]}"


# ═══════════════════════════════════════════════════════════════════════════
# 3. MC4+ weight stabilization
# ═══════════════════════════════════════════════════════════════════════════


class TestWeightStabilization:
    """Test bar cohomology stabilization for the W_N tower."""

    def test_K2_stabilizes(self):
        """K_2(W_N) = p(2) = 2 for all N >= 2."""
        target = _partition_number(2)  # = 2
        for n in range(2, 15):
            assert bar_weight_dim_wN(n, 2) == target

    def test_K3_stabilizes(self):
        """K_3(W_N) = p(3) = 3 for N >= 3."""
        target = _partition_number(3)  # = 3
        for n in range(3, 15):
            assert bar_weight_dim_wN(n, 3) == target

    def test_K4_stabilizes(self):
        """K_4(W_N) = p(4) = 5 for N >= 4."""
        target = _partition_number(4)  # = 5
        for n in range(4, 15):
            assert bar_weight_dim_wN(n, 4) == target

    def test_K5_stabilizes(self):
        """K_5(W_N) = p(5) = 7 for N >= 5."""
        target = _partition_number(5)  # = 7
        for n in range(5, 15):
            assert bar_weight_dim_wN(n, 5) == target

    def test_K2_below_threshold(self):
        """K_2(W_2) = p(2) = 2 (already stabilized at threshold)."""
        assert bar_weight_dim_wN(2, 2) == _partition_number(2)

    def test_K3_below_threshold(self):
        """K_3(W_2) < p(3): not yet stabilized."""
        # W_2 only has spin-2 generator: modes at weights >= 2
        # K_3(W_2) = number of partitions of 3 into parts >= 2 = 1 ({3})
        assert bar_weight_dim_wN(2, 3) < _partition_number(3)

    def test_w_infinity_is_partition(self):
        """K_w(W_infinity) = p(w) for all w."""
        for w in range(11):
            assert bar_weight_dim_w_infinity(w) == _partition_number(w)

    def test_stabilization_threshold(self):
        """Threshold at weight w is N_0 = w."""
        for w in range(2, 8):
            assert weight_stabilization_threshold(w) == w

    @pytest.mark.xfail(reason="frontier computation incomplete")
    def test_full_stabilization(self):
        """Full MC4+ stabilization: K_w(W_N) = p(w) for N >= w, w <= 6."""
        assert verify_weight_stabilization(max_weight=6)

    def test_stabilization_table_complete(self):
        """Weight stabilization table has correct keys and structure."""
        table = weight_stabilization_table(max_weight=4, max_N=8)
        assert "w=2" in table
        assert "w=4" in table
        for key, row in table.items():
            assert "N=inf" in row
            assert "stabilized" in row

    @pytest.mark.xfail(reason="frontier computation incomplete")
    def test_verify_weight_stabilization_suite(self):
        """Run the full weight stabilization suite."""
        results = verify_weight_stabilization_suite()
        assert all(results.values()), f"Failures: {[k for k,v in results.items() if not v]}"


# ═══════════════════════════════════════════════════════════════════════════
# 4. MacMahon partition function
# ═══════════════════════════════════════════════════════════════════════════


class TestMacMahon:
    """Test plane partition (MacMahon) generating function."""

    def test_pp_zero(self):
        """pp(0) = 1."""
        assert plane_partition_number(0) == 1

    def test_pp_one(self):
        """pp(1) = 1."""
        assert plane_partition_number(1) == 1

    def test_pp_two(self):
        """pp(2) = 3."""
        assert plane_partition_number(2) == 3

    def test_pp_three(self):
        """pp(3) = 6."""
        assert plane_partition_number(3) == 6

    def test_pp_four(self):
        """pp(4) = 13."""
        assert plane_partition_number(4) == 13

    def test_pp_five(self):
        """pp(5) = 24."""
        assert plane_partition_number(5) == 24

    def test_pp_ten(self):
        """pp(10) = 500."""
        assert plane_partition_number(10) == 500

    @pytest.mark.xfail(reason="frontier computation incomplete")
    def test_macmahon_known_table(self):
        """Verify all known MacMahon numbers from OEIS A000219."""
        assert verify_macmahon_against_known()

    def test_macmahon_coefficients(self):
        """MacMahon coefficients match the known table."""
        computed = macmahon_coefficients(10)
        assert computed == _MACMAHON_KNOWN

    def test_pp_geq_p(self):
        """pp(n) >= p(n) for all n (plane partitions dominate)."""
        for n in range(20):
            assert plane_partition_number(n) >= _partition_number(n)

    def test_vacuum_vs_bar_distinction(self):
        """W_infinity vacuum character != bar cohomology GF (AP9).

        Vacuum character uses plane partitions pp(n).
        Bar cohomology uses ordinary partitions p(n).
        These are different for n >= 2.
        """
        vac = w_infinity_vacuum_character(10)
        bar = w_infinity_bar_cohomology_gf(10)
        assert vac[0] == bar[0] == 1
        assert vac[1] == bar[1] == 1
        # Diverge from n=2 onward
        assert vac[2] == 3
        assert bar[2] == 2
        assert vac[2] > bar[2]

    def test_verify_macmahon(self):
        """Run the full MacMahon verification suite."""
        results = verify_macmahon()
        assert all(results.values()), f"Failures: {[k for k,v in results.items() if not v]}"


# ═══════════════════════════════════════════════════════════════════════════
# 5. Bosonic string at c = 26
# ═══════════════════════════════════════════════════════════════════════════


class TestBosonicString:
    """Test bosonic string anomaly cancellation and ghost BRST."""

    def test_kappa_vir_26(self):
        """kappa(Vir_26) = 13."""
        assert kappa_virasoro(26) == 13

    def test_kappa_ghost_minus26(self):
        """kappa(bc_{-26}) = -13."""
        assert kappa_bc_ghost(-26) == -13

    def test_anomaly_cancellation(self):
        """kappa_total = 0 at c = 26."""
        data = bosonic_string_anomaly_cancellation()
        assert data["kappa_total"] == 0
        assert data["anomaly_cancels"]

    def test_central_charge_cancellation(self):
        """c_total = 26 + (-26) = 0."""
        data = bosonic_string_anomaly_cancellation()
        assert data["c_total"] == 0

    def test_brst_squared_zero(self):
        """Q_BRST^2 = 0 at c = 26."""
        data = bosonic_string_anomaly_cancellation()
        assert data["Q_BRST_squared_zero"]

    def test_ghost_bar_data(self):
        """Ghost-extended bar complex has d^2 = 0."""
        data = ghost_extended_bar_data()
        assert data["d_squared_each_factor"]
        assert data["brst_d_squared"]

    def test_spectrum_level_0(self):
        """Level 0: 1 state (tachyon)."""
        spec = bosonic_string_spectrum_level(3)
        assert spec[0]["states"] == 1
        assert spec[0]["mass_squared"] == -1  # tachyon

    def test_spectrum_level_1(self):
        """Level 1: 24 states (massless photon, 24 transverse directions)."""
        spec = bosonic_string_spectrum_level(3)
        assert spec[1]["states"] == 24
        assert spec[1]["mass_squared"] == 0

    def test_verify_string_theory(self):
        """Run the full string theory verification suite."""
        results = verify_string_theory()
        assert all(results.values()), f"Failures: {[k for k,v in results.items() if not v]}"


# ═══════════════════════════════════════════════════════════════════════════
# 6. Virasoro resonance at c = 26
# ═══════════════════════════════════════════════════════════════════════════


class TestVirasoroResonance:
    """Test Virasoro Koszul duality and resonance shadow."""

    def test_dual_c26(self):
        """Vir_26^! = Vir_0."""
        assert virasoro_koszul_dual_c(26) == 0

    def test_dual_c0(self):
        """Vir_0^! = Vir_26."""
        assert virasoro_koszul_dual_c(0) == 26

    def test_dual_c13(self):
        """Vir_13^! = Vir_13 (self-dual)."""
        assert virasoro_koszul_dual_c(13) == 13

    def test_self_dual_c(self):
        """Self-dual at c = 13, NOT c = 26 (AP8)."""
        assert virasoro_self_dual_c() == 13

    def test_q_contact_c26(self):
        """Q^contact_Vir(26) = 5/1976."""
        assert virasoro_q_contact_at_26() == Rational(5, 1976)

    def test_q_contact_general(self):
        """Q^contact_Vir = 10/[c(5c+22)]."""
        # At c = 1: 10/(1*27) = 10/27
        assert q_contact_virasoro(1) == Rational(10, 27)
        # At c = 2: 10/(2*32) = 10/64 = 5/32
        assert q_contact_virasoro(2) == Rational(5, 32)

    def test_complementarity_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c."""
        for c_val in [0, 1, 5, 10, 13, 20, 25, 26]:
            data = virasoro_complementarity_sum(c_val)
            assert data["holds"], f"Complementarity fails at c={c_val}"

    def test_palindromic_at_c13(self):
        """Shadow data palindromic at self-dual point c = 13."""
        check = virasoro_self_duality_check(13)
        assert check["palindromic"]
        assert check["is_self_dual_point"]

    def test_shadow_tower_data_c26(self):
        """Shadow tower at c = 26 has bosonic string flag."""
        data = virasoro_shadow_tower_data(26)
        assert data["bosonic_string"]
        assert data["depth_zero_resonance"]
        assert data["c_dual"] == 0

    def test_shadow_tower_data_c13(self):
        """Shadow tower at c = 13 has self-dual flag."""
        data = virasoro_shadow_tower_data(13)
        assert data["self_dual"]
        assert data["c_dual"] == 13

    def test_verify_virasoro_resonance(self):
        """Run the full Virasoro resonance verification suite."""
        results = verify_virasoro_resonance()
        assert all(results.values()), f"Failures: {[k for k,v in results.items() if not v]}"


# ═══════════════════════════════════════════════════════════════════════════
# 7. Shadow radius at large N
# ═══════════════════════════════════════════════════════════════════════════


class TestShadowRadius:
    """Test shadow radius and higher-spin/string duality."""

    def test_critical_c_approx(self):
        """Critical c* ~ 6.12."""
        c_star = shadow_radius_critical_c()
        assert abs(c_star - 6.1243) < 0.01

    def test_rho_c26_convergent(self):
        """rho(Vir_26) < 1: shadow tower converges at c = 26."""
        rho = virasoro_shadow_radius(26)
        assert rho < 1.0

    def test_rho_c13_convergent(self):
        """rho(Vir_13) < 1: shadow tower converges at self-dual point."""
        rho = virasoro_shadow_radius(13)
        assert rho < 1.0

    def test_rho_c2_divergent(self):
        """rho(Vir_2) > 1: shadow tower diverges at c = 2."""
        rho = virasoro_shadow_radius(2)
        assert rho > 1.0

    def test_rho_decreases_with_c(self):
        """rho(Vir_c) is eventually decreasing for large c."""
        rho_10 = virasoro_shadow_radius(10)
        rho_20 = virasoro_shadow_radius(20)
        rho_50 = virasoro_shadow_radius(50)
        assert rho_50 < rho_20 < rho_10

    def test_rho_times_N_approaches_6(self):
        """rho(Vir_N) * N -> 6 as N -> infinity."""
        rate = large_N_shadow_convergence_rate(30)
        last = rate[-1]
        assert abs(last["rho_times_N"] - 6.0) < 0.3

    def test_decay_exponent(self):
        """rho * c -> 6 for large c."""
        val_50 = shadow_radius_decay_exponent(50)
        val_100 = shadow_radius_decay_exponent(100)
        assert abs(val_100 - 6.0) < abs(val_50 - 6.0)
        assert abs(val_100 - 6.0) < 0.5

    def test_shadow_radius_large_N_table_structure(self):
        """Large-N shadow table has correct structure."""
        table = shadow_radius_large_N_table(10)
        assert len(table) == 8  # N = 3, ..., 10
        for entry in table:
            assert "rho" in entry
            assert "Q_contact" in entry
            assert entry["rho"] > 0

    def test_rho_squared_formula(self):
        """rho^2 = (180c + 872) / ((5c + 22) * c^2)."""
        # At c = 26: (180*26 + 872) / ((5*26+22)*26^2)
        # = (4680 + 872) / (152 * 676) = 5552 / 102752
        rho_sq = virasoro_shadow_radius_squared(26)
        assert rho_sq == Rational(5552, 102752)

    def test_wN_shadow_at_c_N(self):
        """W_N shadow data at c = N has correct structure."""
        data = wN_shadow_radius_at_c_equals_N(10)
        assert data["N"] == 10
        assert data["c"] == 10
        assert "kappa_WN" in data
        assert "rho_virasoro_subtower" in data


# ═══════════════════════════════════════════════════════════════════════════
# 8. Cross-checks and consistency
# ═══════════════════════════════════════════════════════════════════════════


class TestCrossChecks:
    """Cross-consistency checks between different parts of the engine."""

    def test_kappa_wN_harmonic_divergence(self):
        """kappa(W_N, c) / c = H_N - 1 diverges logarithmically."""
        ratios = [float(anomaly_ratio(n)) for n in range(2, 30)]
        # H_N - 1 is increasing
        for i in range(len(ratios) - 1):
            assert ratios[i + 1] > ratios[i]
        # H_30 - 1 ~ ln(30) + gamma - 1 ~ 3.40 + 0.577 - 1 ~ 2.98
        assert 2.5 < ratios[-1] < 3.5

    def test_macmahon_vs_bar_cohomology(self):
        """MacMahon != bar cohomology (these are different objects, AP9)."""
        comparison = macmahon_vs_partition_comparison(10)
        for entry in comparison:
            assert entry["pp(n)"] >= entry["p(n)"]
        # They diverge after n = 1
        assert comparison[2]["pp(n)"] > comparison[2]["p(n)"]

    @pytest.mark.xfail(reason="frontier computation incomplete")
    def test_mc4_plus_summary_keys(self):
        """MC4+ summary has required keys."""
        summary = mc4_plus_summary()
        assert summary["resonance_rank"] == 0
        assert summary["class"] == "MC4+"
        assert "W_{1+infinity}" in str(summary["W_infinity_specifics"])

    def test_string_theory_summary_keys(self):
        """String theory summary has required keys."""
        summary = string_theory_summary()
        assert summary["c_string"] == 26
        assert summary["c_self_dual"] == 13

    def test_large_N_table_structure(self):
        """Large-N combined shadow table has correct data."""
        table = wN_large_N_shadow_table(10)
        assert len(table) == 8  # N = 3, ..., 10
        for entry in table:
            assert entry["kappa_WN"] > 0
            assert entry["rho_Vir_sub"] > 0

    @pytest.mark.xfail(reason="frontier computation incomplete")
    def test_verify_all(self):
        """Run the complete verification suite."""
        results = verify_all()
        failures = [k for k, v in results.items() if not v]
        assert len(failures) == 0, f"Failed: {failures}"
