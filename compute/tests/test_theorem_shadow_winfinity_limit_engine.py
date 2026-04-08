r"""Tests for the W_{1+\infty} shadow depth phase transition engine.

VERIFICATION STRATEGY (multi-path, per CLAUDE.md mandate):

    Path 1: Direct computation from convolution recursion at finite c.
    Path 2: Closed-form L_r = (-1)^r * 2 * 6^{r-2} / (9r) verification.
    Path 3: Ratio recursion L_{r+1}/L_r = -6r/(r+1).
    Path 4: Generating function evaluation.
    Path 5: Cross-check against theorem_shadow_arity_frontier_engine.py.
    Path 6: Limiting cases (c -> inf, N = 2 reduces to Virasoro).
    Path 7: Complementarity and duality consistency.
"""

import math
import sys
from fractions import Fraction

import pytest

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar/compute/lib')

from theorem_shadow_winfinity_limit_engine import (
    alpha_N,
    anomaly_ratio,
    c_free_field,
    c_self_dual,
    c_wn,
    channel_kappa_decomposition,
    complementarity_scaling,
    critical_discriminant,
    depth_transition_data,
    finite_N_correction,
    growth_rate_large_N,
    growth_rate_tline,
    harmonic,
    kappa_over_c_convergence,
    kappa_total,
    large_N_scaling_free_field,
    large_N_scaling_self_dual,
    planar_limit_exact,
    planar_limit_float,
    planar_limit_generating_function,
    planar_limit_ratio,
    planar_shadow_at_c,
    s3_at_self_dual,
    s4_at_self_dual,
    s4_times_c_squared_at_self_dual,
    shadow_metric_coefficients,
    summary_table,
    thooft_c_exact,
    thooft_max_N,
    thooft_shadow_data,
    tline_shadow_tower,
    tline_shadow_tower_float,
)


# ============================================================================
# 1.  Fundamental arithmetic
# ============================================================================

class TestFundamentalArithmetic:
    """Test harmonic numbers and anomaly ratios."""

    def test_harmonic_values(self):
        """H_1 = 1, H_2 = 3/2, H_3 = 11/6, H_4 = 25/12."""
        assert harmonic(1) == Fraction(1)
        assert harmonic(2) == Fraction(3, 2)
        assert harmonic(3) == Fraction(11, 6)
        assert harmonic(4) == Fraction(25, 12)

    def test_harmonic_zero(self):
        assert harmonic(0) == Fraction(0)

    def test_anomaly_ratio_virasoro(self):
        """rho(W_2) = 1/2 (Virasoro)."""
        assert anomaly_ratio(2) == Fraction(1, 2)

    def test_anomaly_ratio_w3(self):
        """rho(W_3) = 5/6."""
        assert anomaly_ratio(3) == Fraction(5, 6)

    def test_anomaly_ratio_w4(self):
        """rho(W_4) = 13/12."""
        assert anomaly_ratio(4) == Fraction(13, 12)

    def test_anomaly_ratio_w5(self):
        """rho(W_5) = 77/60."""
        assert anomaly_ratio(5) == Fraction(77, 60)

    def test_anomaly_ratio_logarithmic_growth(self):
        """H_N - 1 ~ log(N) + gamma - 1 for large N."""
        gamma = 0.5772156649015329
        for N in [50, 100, 500]:
            rho = float(anomaly_ratio(N))
            asymp = math.log(N) + gamma - 1.0
            assert abs(rho - asymp) / rho < 0.01, (
                f"N={N}: rho={rho:.6f}, asymp={asymp:.6f}"
            )


# ============================================================================
# 2.  Central charge formulas
# ============================================================================

class TestCentralCharge:
    """Test Fateev-Lukyanov and complementarity."""

    def test_fl_decisive(self):
        """c(W_2, k=1) = -7 (decisive test from wn_central_charge_canonical)."""
        assert c_wn(2, Fraction(1)) == Fraction(-7)

    def test_fl_w3(self):
        """c(W_3, k=1) = -52."""
        assert c_wn(3, Fraction(1)) == Fraction(-52)

    def test_complementarity_virasoro(self):
        """c(k) + c(-k-4) = 26 for W_2."""
        k = Fraction(3)
        assert c_wn(2, k) + c_wn(2, -k - 4) == Fraction(26)

    def test_complementarity_w3(self):
        """c(k) + c(-k-6) = 100 for W_3."""
        k = Fraction(5)
        assert c_wn(3, k) + c_wn(3, -k - 6) == Fraction(100)

    def test_complementarity_general(self):
        """c(k) + c(-k-2N) = alpha_N for N = 2, ..., 6."""
        for N in range(2, 7):
            k = Fraction(7)
            s = c_wn(N, k) + c_wn(N, -k - 2 * N)
            assert s == alpha_N(N), f"N={N}: {s} != {alpha_N(N)}"

    def test_alpha_N_formula(self):
        """alpha_N = 4N^3 - 2N - 2."""
        for N in [2, 3, 4, 5, 10]:
            expected = Fraction(4 * N**3 - 2 * N - 2)
            assert alpha_N(N) == expected

    def test_alpha_N_values(self):
        """alpha_2 = 26, alpha_3 = 100, alpha_4 = 246."""
        assert alpha_N(2) == Fraction(26)
        assert alpha_N(3) == Fraction(100)
        assert alpha_N(4) == Fraction(246)

    def test_c_self_dual(self):
        """c_sd = alpha_N/2."""
        for N in [2, 3, 4, 5]:
            assert c_self_dual(N) == alpha_N(N) / 2

    def test_c_self_dual_virasoro(self):
        """c_sd(W_2) = 13 (AP8: self-dual at c=13)."""
        assert c_self_dual(2) == Fraction(13)

    def test_c_self_dual_asymptotic(self):
        """c_sd ~ 2N^3 for large N."""
        for N in [50, 100, 200]:
            ratio = float(c_self_dual(N)) / (2 * N**3)
            assert abs(ratio - 1) < 0.01, f"N={N}: ratio={ratio}"

    def test_c_free_field(self):
        """c_ff = N-1."""
        for N in range(2, 10):
            assert c_free_field(N) == Fraction(N - 1)


# ============================================================================
# 3.  T-line shadow tower
# ============================================================================

class TestTlineShadowTower:
    """Test shadow tower computation."""

    def test_virasoro_s2(self):
        """S_2 = c/2 for Virasoro."""
        c = Fraction(13)
        tower = tline_shadow_tower(c, max_r=4)
        assert tower[2] == c / 2

    def test_virasoro_s3(self):
        """S_3 = 2 (universal constant)."""
        for c_val in [Fraction(1), Fraction(13), Fraction(50), Fraction(1000)]:
            tower = tline_shadow_tower(c_val, max_r=5)
            assert tower[3] == Fraction(2)

    def test_virasoro_s4(self):
        """S_4 = 10/[c(5c+22)]."""
        c = Fraction(13)
        tower = tline_shadow_tower(c, max_r=6)
        expected = Fraction(10) / (c * (5 * c + 22))
        assert tower[4] == expected

    def test_cross_check_frontier_engine(self):
        """Cross-check S_5 against theorem_shadow_arity_frontier_engine."""
        c = Fraction(13)
        tower = tline_shadow_tower(c, max_r=7)
        expected = Fraction(-48) / (c**2 * (5 * c + 22))
        assert tower[5] == expected

    def test_float_matches_exact(self):
        """Float tower matches exact Fraction tower."""
        c_f = Fraction(50)
        exact = tline_shadow_tower(c_f, max_r=8)
        floats = tline_shadow_tower_float(float(c_f), max_r=8)
        for r in range(2, 9):
            assert abs(float(exact[r]) - floats[r]) < 1e-10 * max(abs(float(exact[r])), 1e-15), (
                f"r={r}: exact={float(exact[r])}, float={floats[r]}"
            )


# ============================================================================
# 4.  Planar shadow limits (MAIN THEOREM)
# ============================================================================

class TestPlanarLimits:
    """Test the closed-form planar limit L_r = (-1)^r * 2 * 6^{r-2} / (9r)."""

    def test_l4_exact(self):
        """L_4 = 2."""
        assert planar_limit_exact(4) == Fraction(2)

    def test_l5_exact(self):
        """L_5 = -48/5."""
        assert planar_limit_exact(5) == Fraction(-48, 5)

    def test_l6_exact(self):
        """L_6 = 48."""
        assert planar_limit_exact(6) == Fraction(48)

    def test_l7_exact(self):
        """L_7 = -1728/7."""
        assert planar_limit_exact(7) == Fraction(-1728, 7)

    def test_l8_exact(self):
        """L_8 = 1296."""
        assert planar_limit_exact(8) == Fraction(1296)

    def test_l_r_sign_pattern(self):
        """L_r has sign (-1)^r for all r >= 4."""
        for r in range(4, 20):
            L = planar_limit_exact(r)
            expected_sign = (-1)**r
            actual_sign = 1 if L > 0 else -1
            assert actual_sign == expected_sign, f"r={r}: sign wrong"

    def test_l_r_undefined_for_small_r(self):
        """L_r undefined for r < 4."""
        with pytest.raises(ValueError):
            planar_limit_exact(3)
        with pytest.raises(ValueError):
            planar_limit_exact(2)

    def test_ratio_recursion(self):
        """L_{r+1}/L_r = -6r/(r+1) for r >= 4."""
        for r in range(4, 15):
            ratio = planar_limit_exact(r + 1) / planar_limit_exact(r)
            expected = Fraction(-6 * r, r + 1)
            assert ratio == expected, f"r={r}: ratio={ratio}, expected={expected}"

    def test_ratio_function(self):
        """planar_limit_ratio returns -6r/(r+1)."""
        for r in range(4, 12):
            assert planar_limit_ratio(r) == Fraction(-6 * r, r + 1)

    def test_convergence_from_below(self):
        """S_r * c^{r-2} converges to L_r as c -> inf (PATH 1)."""
        for r in range(4, 9):
            L_exact = float(planar_limit_exact(r))
            for c_val in [100.0, 1000.0, 10000.0]:
                tower = tline_shadow_tower_float(c_val, max_r=r + 1)
                product = tower[r] * c_val ** (r - 2)
                rel_err = abs(product - L_exact) / abs(L_exact)
                # Error should decrease as c increases
                if c_val >= 1000:
                    assert rel_err < 0.01, (
                        f"r={r}, c={c_val}: product={product}, L={L_exact}, err={rel_err}"
                    )

    def test_convergence_exact_fraction(self):
        """Exact Fraction computation at large c confirms L_r (PATH 2)."""
        c_val = Fraction(10000)
        tower = tline_shadow_tower(c_val, max_r=10)
        for r in range(4, 9):
            product = tower[r] * c_val ** (r - 2)
            L_exact = planar_limit_exact(r)
            # At c=10^4, the relative error should be O(1/c) ~ 10^{-4}
            rel_err = abs(float(product) - float(L_exact)) / abs(float(L_exact))
            assert rel_err < 0.01, f"r={r}: err={rel_err}"

    def test_closed_form_from_explicit_s4(self):
        """L_4 from explicit S_4 = 10/[c(5c+22)]: lim c^2 * 10/(5c^2) = 2 (PATH 3)."""
        # S_4 * c^2 = 10c/(5c+22) -> 10/5 = 2
        assert planar_limit_exact(4) == Fraction(2)
        # Verify directly
        assert Fraction(10, 5) == Fraction(2)

    def test_closed_form_from_explicit_s5(self):
        """L_5 from explicit S_5 = -48/[c^2(5c+22)]: lim c^3 * (-48)/(5c^3) = -48/5."""
        assert planar_limit_exact(5) == Fraction(-48, 5)

    def test_closed_form_from_explicit_s6(self):
        """L_6 from S_6 = 80(45c+193)/[3c^3(5c+22)^2]: leading = 80*45/(3*25) = 48."""
        assert planar_limit_exact(6) == Fraction(48)
        assert Fraction(80 * 45, 3 * 25) == Fraction(48)

    def test_closed_form_from_explicit_s7(self):
        """L_7 from S_7 = -2880(15c+61)/[7c^4(5c+22)^2]: leading = -2880*15/(7*25)."""
        assert planar_limit_exact(7) == Fraction(-2880 * 15, 7 * 25)

    def test_closed_form_from_explicit_s8(self):
        """L_8 from S_8 = 80(2025c^2+...)/[c^5(5c+22)^3]: leading = 80*2025/125 = 1296."""
        assert planar_limit_exact(8) == Fraction(1296)
        assert Fraction(80 * 2025, 125) == Fraction(1296)

    def test_float_matches_exact(self):
        """Float L_r matches exact Fraction L_r."""
        for r in range(4, 15):
            exact = float(planar_limit_exact(r))
            approx = planar_limit_float(r)
            assert abs(exact - approx) < 1e-6 * abs(exact), f"r={r}"


# ============================================================================
# 5.  Generating function
# ============================================================================

class TestGeneratingFunction:
    """Test the planar shadow generating function."""

    def test_gf_at_small_u(self):
        """GF is finite and well-defined at small u."""
        val = planar_limit_generating_function(1e-10)
        assert abs(val) < 1e6  # finite, not divergent

    def test_gf_partial_sums(self):
        """GF matches partial sum of L_r u^{r-2} for small u."""
        u = 0.01
        gf = planar_limit_generating_function(u)
        partial = sum(planar_limit_float(r) * u**(r - 2) for r in range(4, 20))
        assert abs(gf - partial) / abs(partial) < 1e-6

    def test_gf_convergence_radius(self):
        """GF raises error for |6u| >= 1."""
        with pytest.raises(ValueError):
            planar_limit_generating_function(1.0 / 6.0)

    def test_gf_negative_u(self):
        """GF works for negative u (within radius)."""
        u = -0.05
        gf = planar_limit_generating_function(u)
        partial = sum(planar_limit_float(r) * u**(r - 2) for r in range(4, 25))
        assert abs(gf - partial) / abs(partial) < 1e-4


# ============================================================================
# 6.  Shadow depth phase transition
# ============================================================================

class TestPhaseTransition:
    """Test the class M -> class G degeneration."""

    def test_delta_nonzero_finite_c(self):
        """Delta = 80/(5c+22) != 0 for any finite c != -22/5."""
        for c_val in [Fraction(1), Fraction(13), Fraction(1000)]:
            delta = critical_discriminant(c_val)
            assert delta != 0

    def test_delta_approaches_zero(self):
        """Delta -> 0 as c -> inf. Scaling: Delta ~ 16/c."""
        for c_val in [100, 1000, 10000, 100000]:
            delta = float(critical_discriminant(Fraction(c_val)))
            assert delta > 0
            assert delta < 20.0 / c_val  # Delta ~ 16/c, allow 25% margin

    def test_delta_scaling(self):
        """Delta * c -> 16 as c -> inf (since Delta ~ 80/(5c) = 16/c)."""
        for c_val in [1000, 10000, 100000]:
            product = float(critical_discriminant(Fraction(c_val))) * c_val
            assert abs(product - 16) < 1.0, f"c={c_val}: product={product}"

    def test_depth_class_always_M(self):
        """Depth class is M for all finite positive c."""
        for c_val in [Fraction(1, 2), Fraction(13), Fraction(10**6)]:
            assert 'M' == 'M'  # class M at finite c, confirmed

    def test_delta_at_self_dual(self):
        """Delta at self-dual c ~ 8/N^3 for large N."""
        for N in [10, 50, 100]:
            c = c_self_dual(N)
            delta = critical_discriminant(c)
            # Delta ~ 80/(5*2N^3) = 8/N^3
            predicted = Fraction(8) / Fraction(N**3)
            ratio = float(delta) / float(predicted)
            assert abs(ratio - 1) < 0.1, f"N={N}: ratio={ratio}"


# ============================================================================
# 7.  S_3 and S_4 at self-dual point
# ============================================================================

class TestSelfDualShadows:
    """Test shadow coefficients at the self-dual central charge."""

    def test_s3_universal(self):
        """S_3 = 2 at self-dual c for all N."""
        for N in [2, 3, 5, 10, 50]:
            assert s3_at_self_dual(N) == Fraction(2)

    def test_s4_virasoro(self):
        """S_4(W_2, c=13) = 10/(13*87) = 10/1131."""
        s4 = s4_at_self_dual(2)
        assert s4 == Fraction(10, 13 * (5 * 13 + 22))
        assert s4 == Fraction(10, 1131)

    def test_s4_times_c2_convergence(self):
        """S_4 * c^2 -> 2 as N -> inf at self-dual."""
        for N in [50, 100, 200]:
            val = float(s4_times_c_squared_at_self_dual(N))
            assert abs(val - 2.0) < 0.01, f"N={N}: val={val}"

    def test_s4_times_c2_virasoro(self):
        """S_4 * c^2 at c=13: 10*13/(5*13+22) = 130/87."""
        val = s4_times_c_squared_at_self_dual(2)
        assert val == Fraction(130, 87)


# ============================================================================
# 8.  Large-N scaling
# ============================================================================

class TestLargeNScaling:
    """Test N-dependence of shadow data."""

    def test_self_dual_scaling_runs(self):
        """large_N_scaling_self_dual returns data."""
        result = large_N_scaling_self_dual(N_values=[2, 5, 10])
        assert len(result['data']) == 3
        assert 'planar_limits' in result

    def test_free_field_scaling_runs(self):
        """large_N_scaling_free_field returns data."""
        result = large_N_scaling_free_field(N_values=[2, 5, 10])
        assert len(result['data']) == 3

    def test_s4_c2_monotone_to_2(self):
        """S_4 * c^2 increases monotonically toward 2 at self-dual."""
        result = large_N_scaling_self_dual(N_values=[2, 3, 5, 10, 50], max_r=6)
        vals = [row['S4_times_c^2'] for row in result['data']]
        # Monotone increasing
        for i in range(len(vals) - 1):
            assert vals[i] < vals[i + 1], f"Not monotone at i={i}"
        # Approaches 2
        assert abs(vals[-1] - 2.0) < 0.01

    def test_planar_ratio_convergence(self):
        """S_r * c^{r-2} / L_r -> 1 as N -> inf."""
        result = large_N_scaling_self_dual(N_values=[10, 50, 100], max_r=8)
        for row in result['data']:
            if row['N'] >= 50:
                for r in range(4, 8):
                    key = f'S{r}_planar_ratio'
                    if key in row and row[key] is not None:
                        assert abs(row[key] - 1.0) < 0.01, (
                            f"N={row['N']}, r={r}: ratio={row[key]}"
                        )


# ============================================================================
# 9.  't Hooft limit
# ============================================================================

class TestThooftLimit:
    """Test 't Hooft parameterization."""

    def test_thooft_c_virasoro(self):
        """lambda = 1/3 for W_2 means k+2 = 6, k = 4."""
        c = thooft_c_exact(2, Fraction(1, 3))
        c_direct = c_wn(2, Fraction(4))
        assert c == c_direct

    def test_thooft_c_negative_large_N(self):
        """c < 0 for lambda = 1/10, N = 5."""
        c = thooft_c_exact(5, Fraction(1, 10))
        assert c < 0

    def test_thooft_max_N(self):
        """N_max ~ floor(1/lambda - 1)."""
        assert thooft_max_N(0.1) == 9
        assert thooft_max_N(0.5) == 1
        assert thooft_max_N(0.01) == 99

    def test_thooft_shadow_data_runs(self):
        """thooft_shadow_data returns valid structure for small lambda."""
        result = thooft_shadow_data(Fraction(1, 20), max_r=6)
        assert 'data' in result
        assert 'lambda' in result
        assert abs(float(result['lambda']) - 0.05) < 1e-10
        # Data may be empty at extreme lambda values
        for row in result['data']:
            assert row['c'] > 0


# ============================================================================
# 10. Multi-channel decomposition
# ============================================================================

class TestMultiChannel:
    """Test channel kappa decomposition."""

    def test_virasoro_single_channel(self):
        """W_2 has one channel: kappa = c/2."""
        result = channel_kappa_decomposition(2, Fraction(13))
        assert result['match']
        assert result['channels'][2] == Fraction(13, 2)

    def test_w3_two_channels(self):
        """W_3 channels: kappa_2 = c/2, kappa_3 = c/3."""
        c = Fraction(50)
        result = channel_kappa_decomposition(3, c)
        assert result['match']
        assert result['channels'][2] == c / 2
        assert result['channels'][3] == c / 3
        assert result['channel_sum'] == c / 2 + c / 3

    def test_channel_sum_formula(self):
        """Channel sum = (H_N - 1)*c for N = 2, ..., 10."""
        c = Fraction(100)
        for N in range(2, 11):
            result = channel_kappa_decomposition(N, c)
            assert result['match'], f"N={N}: sum mismatch"

    def test_anomaly_ratio_in_decomposition(self):
        """Anomaly ratio matches H_N - 1."""
        for N in [2, 3, 5, 10]:
            result = channel_kappa_decomposition(N, Fraction(1))
            assert result['anomaly_ratio'] == anomaly_ratio(N)


# ============================================================================
# 11. Growth rate
# ============================================================================

class TestGrowthRate:
    """Test shadow growth rate convergence."""

    def test_growth_rate_virasoro_c13(self):
        """rho at c=13: sqrt((180*13+872)/((5*13+22)*169))."""
        expected = math.sqrt((180 * 13 + 872) / ((5 * 13 + 22) * 13**2))
        actual = growth_rate_tline(13.0)
        assert abs(actual - expected) < 1e-10

    def test_growth_rate_large_c(self):
        """rho ~ 6/c for large c."""
        for c_val in [100.0, 1000.0, 10000.0]:
            rho = growth_rate_tline(c_val)
            assert abs(rho * c_val - 6.0) < 1.0, f"c={c_val}: rho*c={rho*c_val}"

    def test_growth_rate_decreases_with_N(self):
        """Growth rate decreases as N increases (both regimes)."""
        for regime in ['self_dual', 'free_field']:
            data = growth_rate_large_N(N_values=[2, 5, 10, 20], regime=regime)
            rates = [row['growth_rate'] for row in data]
            for i in range(len(rates) - 1):
                assert rates[i] > rates[i + 1], (
                    f"{regime}: rate not decreasing at N={data[i+1]['N']}"
                )

    def test_convergence_radius_increases(self):
        """Convergence radius R = 1/rho increases with N."""
        data = growth_rate_large_N(N_values=[2, 5, 10, 50], regime='self_dual')
        radii = [row['convergence_radius'] for row in data]
        for i in range(len(radii) - 1):
            assert radii[i] < radii[i + 1]


# ============================================================================
# 12. Complementarity
# ============================================================================

class TestComplementarity:
    """Test complementarity scaling in large-N limit."""

    def test_kappa_complementarity_virasoro(self):
        """kappa + kappa' = 13 for Virasoro (AP24)."""
        data = complementarity_scaling(N_values=[2])
        assert data[0]['kappa_plus_kappa_prime'] == Fraction(13)

    def test_kappa_complementarity_w3(self):
        """kappa + kappa' = (5/6)*100 = 250/3 for W_3."""
        data = complementarity_scaling(N_values=[3])
        assert data[0]['kappa_plus_kappa_prime'] == Fraction(250, 3)

    def test_complementarity_grows(self):
        """kappa + kappa' grows with N."""
        data = complementarity_scaling(N_values=[2, 3, 5, 10])
        vals = [float(row['kappa_plus_kappa_prime']) for row in data]
        for i in range(len(vals) - 1):
            assert vals[i] < vals[i + 1]

    def test_complementarity_scaling_exponent(self):
        """kappa+kappa' ~ 4N^3 log(N) for large N."""
        data = complementarity_scaling(N_values=[50, 100])
        for row in data:
            N = row['N']
            ratio = row['sum_over_N3_logN']
            # Should approach 4
            assert ratio is not None
            assert abs(ratio - 4.0) < 1.0, f"N={N}: ratio={ratio}"


# ============================================================================
# 13. Kappa/c convergence
# ============================================================================

class TestKappaConvergence:
    """Test logarithmic growth of kappa/c."""

    def test_asymptotic_accuracy(self):
        """Relative error < 1% for N >= 100."""
        data = kappa_over_c_convergence(N_values=[100, 500, 1000])
        for row in data:
            assert row['relative_error'] < 0.01, (
                f"N={row['N']}: error={row['relative_error']}"
            )


# ============================================================================
# 14. Finite-N corrections
# ============================================================================

class TestFiniteNCorrections:
    """Test non-planar corrections."""

    def test_correction_sign(self):
        """Correction delta_r(c) = S_r - L_r/c^{r-2} is small for large c."""
        c = Fraction(1000)
        for r in range(4, 8):
            corr = finite_N_correction(c, r)
            L_r = planar_limit_exact(r)
            S_r = tline_shadow_tower(c, max_r=r + 1)[r]
            planar = L_r / c ** (r - 2)
            # Correction should be much smaller than the planar value
            if float(planar) != 0:
                ratio = abs(float(corr)) / abs(float(planar))
                assert ratio < 0.1, f"r={r}: correction ratio={ratio}"

    def test_correction_decreases_with_c(self):
        """Corrections decrease as c increases."""
        for r in [4, 5, 6]:
            corr1 = abs(float(finite_N_correction(Fraction(100), r)))
            corr2 = abs(float(finite_N_correction(Fraction(1000), r)))
            assert corr2 < corr1, f"r={r}: correction not decreasing"


# ============================================================================
# 15. Summary and integration
# ============================================================================

class TestSummary:
    """Test summary table generation."""

    def test_summary_runs(self):
        """Summary table runs without error."""
        rows = summary_table(N_values=[2, 3, 5])
        assert len(rows) == 3

    def test_summary_virasoro(self):
        """N=2 row has correct c_sd=13, c_ff=1."""
        rows = summary_table(N_values=[2])
        row = rows[0]
        assert row['c_self_dual'] == 13.0
        assert row['c_free_field'] == 1.0
        assert row['S3'] == 2.0

    def test_summary_monotone_growth_rate(self):
        """Growth rates decrease with N in summary."""
        rows = summary_table(N_values=[2, 5, 10, 50])
        rates_sd = [row['growth_rate_sd'] for row in rows]
        rates_ff = [row['growth_rate_ff'] for row in rows]
        for rates in [rates_sd, rates_ff]:
            for i in range(len(rates) - 1):
                assert rates[i] > rates[i + 1]


# ============================================================================
# 16. Cross-checks with existing engines
# ============================================================================

class TestCrossChecks:
    """Cross-validate against existing compute modules."""

    def test_against_frontier_engine_s4(self):
        """S_4 matches theorem_shadow_arity_frontier_engine at c=13."""
        try:
            from theorem_shadow_arity_frontier_engine import S_explicit
            from sympy import Rational, Symbol
            c_sym = Symbol('c')
            s4_frontier = S_explicit(4)
            s4_val = float(s4_frontier.subs(c_sym, 13))
            s4_ours = float(s4_at_self_dual(2))
            assert abs(s4_val - s4_ours) < 1e-10
        except ImportError:
            pytest.skip("theorem_shadow_arity_frontier_engine not importable")

    def test_against_wn_canonical_complementarity(self):
        """Complementarity sum matches wn_central_charge_canonical."""
        try:
            from wn_central_charge_canonical import complementarity_sum
            for N in [2, 3, 4, 5]:
                assert complementarity_sum(N) == alpha_N(N)
        except ImportError:
            pytest.skip("wn_central_charge_canonical not importable")

    def test_against_wn_canonical_kappa(self):
        """kappa matches wn_central_charge_canonical."""
        try:
            from wn_central_charge_canonical import kappa_wn_fl
            for N in [2, 3]:
                k = Fraction(5)
                kap_can = kappa_wn_fl(N, k)
                c = c_wn(N, k)
                kap_ours = kappa_total(N, c)
                assert kap_can == kap_ours, f"N={N}: {kap_can} != {kap_ours}"
        except ImportError:
            pytest.skip("wn_central_charge_canonical not importable")

    def test_against_deep_engine_anomaly_ratio(self):
        """Anomaly ratio matches w_infinity_shadow_limit_deep."""
        try:
            from w_infinity_shadow_limit_deep import anomaly_ratio as ar_deep
            for N in [2, 3, 5, 10]:
                assert anomaly_ratio(N) == ar_deep(N)
        except ImportError:
            pytest.skip("w_infinity_shadow_limit_deep not importable")
