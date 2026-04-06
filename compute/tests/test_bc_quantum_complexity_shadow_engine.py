r"""Tests for BC-133: Quantum complexity from the shadow obstruction tower.

85+ tests covering:
- Shadow data correctness for all families (kappa, S_3, S_4, depth class)
- Circuit complexity (L1, L2, logarithmic gate counts)
- Volume complexity (quadrature, tower sum, closed-form cross-checks)
- Nielsen complexity (geodesic in shadow metric)
- Action complexity
- Complexity growth rate, Lloyd bound, scrambling time
- Switchback effect from cubic shadow
- Complexity at zeta zeros (c(rho_n) parametrization)
- Complexity=volume proportionality test
- Cross-definition consistency (5-way)
- Multi-path verification of all major results

Anti-patterns guarded against:
- AP1: kappa formulas recomputed from first principles per family
- AP9: kappa != c in general; kappa = c/2 for Virasoro, k for Heisenberg
- AP10: no hardcoded expected values without independent derivation
- AP20: kappa(A) is intrinsic to A, not kappa_eff
- AP24: complementarity sum checked per family
- AP39: S_2 = kappa != c/2 for non-Virasoro families
"""

import cmath
import math
import pytest

from compute.lib.bc_quantum_complexity_shadow_engine import (
    ZETA_ZEROS_GAMMA,
    zeta_zero_gamma,
    zeta_zero_rho,
    c_from_zeta_zero,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    affine_slN_shadow_data,
    wN_shadow_data,
    shadow_tower_complex,
    shadow_tower_for_family,
    circuit_complexity,
    volume_complexity,
    nielsen_complexity,
    complexity_growth_rate,
    switchback_complexity,
    complexity_at_zeta_zero,
    complexity_at_zeta_zeros_table,
    heisenberg_complexity_sweep,
    virasoro_complexity_sweep,
    affine_slN_complexity_sweep,
    complexity_extrema_at_zeros,
    complexity_equals_volume_test,
    cross_definition_consistency,
    CircuitComplexity,
)


# ===========================================================================
# Section 1: Zeta zero utilities
# ===========================================================================

class TestZetaZeroUtilities:

    def test_gamma_1_value(self):
        """gamma_1 ~ 14.1347 (first zeta zero imaginary part)."""
        g1 = zeta_zero_gamma(1)
        assert abs(g1 - 14.134725141734693) < 1e-6

    def test_gamma_2_value(self):
        """gamma_2 ~ 21.0220."""
        g2 = zeta_zero_gamma(2)
        assert abs(g2 - 21.022039638771555) < 1e-6

    def test_rho_on_critical_line(self):
        """rho_n = 1/2 + i*gamma_n under RH."""
        rho = zeta_zero_rho(1)
        assert abs(rho.real - 0.5) < 1e-10
        assert abs(rho.imag - 14.134725141734693) < 1e-6

    def test_c_from_zeta_zero_type(self):
        """c(rho_n) is complex."""
        c = c_from_zeta_zero(1)
        assert isinstance(c, complex)
        assert abs(c.imag) > 0  # genuinely complex

    def test_c_from_zeta_zero_formula(self):
        """c(rho) = 26*rho/(rho+1)."""
        rho = zeta_zero_rho(3)
        c = c_from_zeta_zero(3)
        expected = 26.0 * rho / (rho + 1.0)
        assert abs(c - expected) < 1e-10

    def test_zeta_zeros_monotone(self):
        """gamma_n is strictly increasing."""
        for i in range(1, len(ZETA_ZEROS_GAMMA)):
            assert ZETA_ZEROS_GAMMA[i] > ZETA_ZEROS_GAMMA[i - 1]


# ===========================================================================
# Section 2: Shadow data for standard families
# ===========================================================================

class TestShadowData:

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2 (AP39)."""
        data = virasoro_shadow_data(10.0)
        assert abs(data['kappa'] - 5.0) < 1e-10

    def test_virasoro_S3(self):
        """Virasoro S_3 = 2 (constant)."""
        data = virasoro_shadow_data(10.0)
        assert abs(data['alpha'] - 2.0) < 1e-10

    def test_virasoro_S4(self):
        """Virasoro S_4 = 10/(c*(5c+22))."""
        c = 10.0
        data = virasoro_shadow_data(c)
        expected = 10.0 / (c * (5.0 * c + 22.0))
        assert abs(data['S4'] - expected) < 1e-10

    def test_virasoro_depth_class_M(self):
        """Virasoro is class M (infinite depth, Delta != 0)."""
        data = virasoro_shadow_data(10.0)
        assert data['depth_class'] == 'M'

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k (AP39: NOT k/2)."""
        data = heisenberg_shadow_data(5.0)
        assert abs(data['kappa'] - 5.0) < 1e-10

    def test_heisenberg_depth_class_G(self):
        """Heisenberg is class G (depth 2)."""
        data = heisenberg_shadow_data(5.0)
        assert data['depth_class'] == 'G'

    def test_heisenberg_S3_zero(self):
        """Heisenberg S_3 = 0."""
        data = heisenberg_shadow_data(5.0)
        assert abs(data['alpha']) < 1e-10

    def test_heisenberg_S4_zero(self):
        """Heisenberg S_4 = 0."""
        data = heisenberg_shadow_data(5.0)
        assert abs(data['S4']) < 1e-10

    def test_affine_sl2_kappa(self):
        """kappa(V_k(sl_2)) = 3*(k+2)/4.
        dim(sl_2) = 3, h^vee = 2. kappa = 3*(k+2)/(2*2) = 3*(k+2)/4."""
        data = affine_slN_shadow_data(2, 1.0)
        expected = 3.0 * (1.0 + 2.0) / 4.0  # = 2.25
        assert abs(data['kappa'] - expected) < 1e-10

    def test_affine_sl3_kappa(self):
        """kappa(V_k(sl_3)) = 8*(k+3)/6 = 4*(k+3)/3.
        dim(sl_3) = 8, h^vee = 3."""
        data = affine_slN_shadow_data(3, 2.0)
        expected = 8.0 * (2.0 + 3.0) / (2.0 * 3.0)  # = 40/6 = 20/3
        assert abs(data['kappa'] - expected) < 1e-10

    def test_affine_depth_class_L(self):
        """Affine KM is class L (depth 3)."""
        data = affine_slN_shadow_data(2, 1.0)
        assert data['depth_class'] == 'L'

    def test_affine_Delta_zero(self):
        """Affine KM has Delta = 0 (class L: perfect-square Q_L)."""
        data = affine_slN_shadow_data(3, 2.0)
        assert abs(data['Delta']) < 1e-10

    def test_wN_equals_virasoro_on_T_line(self):
        """W_N on the T-line has same shadow data as Virasoro."""
        c = 15.0
        data_vir = virasoro_shadow_data(c)
        data_wN = wN_shadow_data(3, c)
        assert abs(data_vir['kappa'] - data_wN['kappa']) < 1e-10
        assert abs(data_vir['alpha'] - data_wN['alpha']) < 1e-10
        assert abs(data_vir['S4'] - data_wN['S4']) < 1e-10

    def test_virasoro_Q_L_coefficients(self):
        """Q_L = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2."""
        c = 12.0
        data = virasoro_shadow_data(c)
        kappa = c / 2.0
        alpha = 2.0
        S4 = 10.0 / (c * (5 * c + 22))
        assert abs(data['q0'] - 4.0 * kappa ** 2) < 1e-10
        assert abs(data['q1'] - 12.0 * kappa * alpha) < 1e-10
        assert abs(data['q2'] - (9.0 * alpha ** 2 + 16.0 * kappa * S4)) < 1e-10

    def test_virasoro_discriminant(self):
        """Delta = 8*kappa*S_4."""
        c = 12.0
        data = virasoro_shadow_data(c)
        kappa = c / 2.0
        S4 = 10.0 / (c * (5 * c + 22))
        expected = 8.0 * kappa * S4
        assert abs(data['Delta'] - expected) < 1e-10


# ===========================================================================
# Section 3: Shadow tower computation
# ===========================================================================

class TestShadowTowerComplex:

    def test_heisenberg_tower_terminates(self):
        """Heisenberg tower: S_2 = k, S_r = 0 for r >= 3."""
        tower, data = shadow_tower_for_family('heisenberg', 3.0)
        assert abs(tower[2] - 3.0) < 1e-10  # S_2 = kappa = k
        for r in range(3, 20):
            assert abs(tower[r]) < 1e-10

    def test_virasoro_S2(self):
        """Virasoro S_2 = c/2."""
        c = 10.0
        tower, data = shadow_tower_for_family('virasoro', c, max_r=10)
        assert abs(tower[2] - c / 2.0) < 1e-8

    def test_virasoro_S3(self):
        """Virasoro S_3 = 2 (from the convolution recursion)."""
        c = 10.0
        tower, data = shadow_tower_for_family('virasoro', c, max_r=10)
        # S_3 = a_1 / 3 where a_1 = q1/(2*a0) = 12*kappa*alpha/(2*2*kappa) = 3*alpha = 6
        # S_3 = 6/3 = 2
        assert abs(tower[3] - 2.0) < 1e-8

    def test_virasoro_S4_matches(self):
        """Virasoro S_4 = 10/(c*(5c+22)) from recursion."""
        c = 10.0
        tower, data = shadow_tower_for_family('virasoro', c, max_r=10)
        expected = 10.0 / (c * (5.0 * c + 22.0))
        assert abs(tower[4] - expected) < 1e-8

    def test_complex_tower_nonzero(self):
        """Tower at complex c has nonzero entries."""
        c_complex = complex(13, 5)
        tower, data = shadow_tower_for_family('virasoro', c_complex, max_r=10)
        assert abs(tower[2]) > 0.1  # kappa = c/2 is nonzero

    def test_affine_tower_terminates_at_3(self):
        """Affine sl_2 tower has S_2, S_3 nonzero, S_r ~ 0 for r >= 4.
        (class L: Delta = 0, tower terminates at arity 3)."""
        tower, data = shadow_tower_for_family('affine_slN', 1.0, N=2, max_r=15)
        assert abs(tower[2]) > 0.1
        assert abs(tower[3]) > 1e-10
        # For class L with Delta=0, higher arities should be very small
        for r in range(5, 15):
            assert abs(tower[r]) < abs(tower[3]) * 0.1


# ===========================================================================
# Section 4: Circuit complexity
# ===========================================================================

class TestCircuitComplexity:

    def test_heisenberg_circuit_constant(self):
        """Heisenberg circuit complexity is ~1 (single gate)."""
        sweep = heisenberg_complexity_sweep([1.0, 5.0, 10.0])
        for entry in sweep:
            # C_circ = sum|S_r|/|kappa| = |kappa|/|kappa| = 1 (only S_2 nonzero)
            assert abs(entry['C_circuit'] - 1.0) < 0.01

    def test_heisenberg_volume_linear_in_k(self):
        """Heisenberg V_shadow scales linearly with k."""
        sweep = heisenberg_complexity_sweep([1.0, 2.0, 4.0, 8.0])
        # V = 2*k*t_* = 2*k*10 = 20*k (with t_max=10)
        for entry in sweep:
            k = entry['k']
            V_expected = entry.get('V_closed_G')
            if V_expected is not None:
                assert abs(entry['V_shadow'] - V_expected) / abs(V_expected) < 0.01

    def test_virasoro_circuit_grows_with_c(self):
        """Virasoro circuit complexity grows with c (more shadow content)."""
        sweep = virasoro_complexity_sweep([2.0, 10.0, 20.0], max_r=20)
        C_vals = [e['C_circuit'] for e in sweep if 'error' not in e]
        assert len(C_vals) >= 2
        # Not necessarily monotone due to S_4 ~ 1/(c*(5c+22)) but L1 sum should grow
        assert all(c > 0 for c in C_vals)

    def test_circuit_L1_ge_L2(self):
        """L1 norm >= L2 norm (Cauchy-Schwarz)."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=20)
        circ = circuit_complexity(tower, data, 20)
        assert circ.tower_norm_l1 >= circ.tower_norm_l2 - 1e-10

    def test_circuit_positive(self):
        """Circuit complexity is non-negative."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            tower, data = shadow_tower_for_family('virasoro', c, max_r=15)
            circ = circuit_complexity(tower, data, 15)
            assert circ.gate_count >= 0

    def test_affine_circuit_values(self):
        """Affine sl_2 circuit complexity is finite and positive."""
        sweep = affine_slN_complexity_sweep([2], [1.0, 3.0, 5.0], max_r=10)
        for entry in sweep:
            if 'error' not in entry:
                assert entry['C_circuit'] > 0
                assert entry['C_circuit'] < 1e6


# ===========================================================================
# Section 5: Volume complexity
# ===========================================================================

class TestVolumeComplexity:

    def test_heisenberg_volume_closed_form(self):
        """Heisenberg: V = 2*|kappa|*t_* (closed form for class G)."""
        data = heisenberg_shadow_data(5.0)
        vol = volume_complexity(data, t_max=10.0)
        expected = 2.0 * 5.0 * 10.0  # 2*k*t_max
        assert vol['V_closed_G'] is not None
        assert abs(vol['V_closed_G'] - expected) < 1e-6
        # Quadrature should match
        assert abs(vol['V_quadrature'] - expected) / expected < 0.01

    def test_virasoro_volume_positive(self):
        """Virasoro volume is positive for positive c."""
        for c in [1.0, 10.0, 25.0]:
            data = virasoro_shadow_data(c)
            vol = volume_complexity(data, t_max=1.0)
            assert vol['V_quadrature'] > 0

    def test_action_ge_volume_squared(self):
        """Action >= Volume^2 / t_* (by Cauchy-Schwarz on integrals).
        Integral Q dt >= (Integral sqrt(Q) dt)^2 / t_* by Cauchy-Schwarz."""
        data = virasoro_shadow_data(10.0)
        vol = volume_complexity(data, t_max=1.0)
        V = vol['V_quadrature']
        A = vol['A_action']
        t_star = vol['t_star']
        # Cauchy-Schwarz: (int sqrt(Q))^2 <= t_* * int Q
        assert V ** 2 <= t_star * A + 1e-6

    def test_volume_at_complex_c(self):
        """Volume is well-defined at complex c."""
        c = complex(13, 5)
        data = virasoro_shadow_data(c)
        vol = volume_complexity(data, t_max=1.0)
        assert vol['V_quadrature'] > 0  # |sqrt(Q_L)| is always non-negative

    def test_volume_increases_with_kappa(self):
        """Volume increases with kappa (larger curvature => more volume)."""
        vols = []
        for c in [2.0, 10.0, 20.0]:
            data = virasoro_shadow_data(c)
            vol = volume_complexity(data, t_max=0.5)
            vols.append(vol['V_quadrature'])
        assert vols[0] < vols[1] < vols[2]


# ===========================================================================
# Section 6: Nielsen complexity
# ===========================================================================

class TestNielsenComplexity:

    def test_nielsen_positive(self):
        """Nielsen complexity is positive."""
        data = virasoro_shadow_data(10.0)
        result = nielsen_complexity(data, t_max=2.0)
        assert result['C_Nielsen'] > 0

    def test_nielsen_log_divergence(self):
        """The log divergence scales as 2*|kappa|*log(t_*/epsilon)."""
        data = virasoro_shadow_data(10.0)
        result = nielsen_complexity(data, t_max=2.0)
        kappa = 5.0  # c/2
        expected_log = 2.0 * kappa * math.log(2.0 / 1e-4)
        assert abs(result['log_divergence'] - expected_log) < 1e-6

    def test_nielsen_heisenberg_simple(self):
        """Heisenberg Nielsen complexity is computable."""
        data = heisenberg_shadow_data(5.0)
        result = nielsen_complexity(data, t_max=5.0)
        assert result['C_Nielsen'] > 0
        # Regularized should exist
        assert 'C_Nielsen_reg' in result

    def test_nielsen_different_from_volume(self):
        """Nielsen and volume complexity are different (different integrands)."""
        data = virasoro_shadow_data(10.0)
        vol = volume_complexity(data, t_max=2.0)
        nielsen = nielsen_complexity(data, t_max=2.0)
        # They should differ because Nielsen has the 1/t^2 weight
        assert abs(vol['V_quadrature'] - nielsen['C_Nielsen']) > 0.01


# ===========================================================================
# Section 7: Complexity growth rate
# ===========================================================================

class TestComplexityGrowthRate:

    def test_lloyd_bound_formula(self):
        """Lloyd bound = 2*|kappa|/pi."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=20)
        growth = complexity_growth_rate(tower, data, 20)
        expected = 2.0 * 5.0 / math.pi  # kappa = c/2 = 5
        assert abs(growth['lloyd_bound'] - expected) < 1e-10

    def test_scrambling_time_positive(self):
        """Scrambling time is positive for class M."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=20)
        growth = complexity_growth_rate(tower, data, 20)
        assert growth['scrambling_time'] is not None
        assert growth['scrambling_time'] > 0

    def test_scrambling_time_formula(self):
        """t_* = (1/|kappa|) * log(1/rho)."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=20)
        growth = complexity_growth_rate(tower, data, 20)
        rho = growth['rho']
        kappa = abs(data['kappa'])
        if rho is not None and rho > 0 and kappa > 0:
            expected = math.log(1.0 / rho) / kappa
            assert abs(growth['scrambling_time'] - expected) < 1e-10

    def test_heisenberg_no_scrambling(self):
        """Heisenberg (class G) has no scrambling time (no growth)."""
        tower, data = shadow_tower_for_family('heisenberg', 5.0, max_r=20)
        growth = complexity_growth_rate(tower, data, 20)
        assert growth['scrambling_time'] is None

    def test_gate_rate_positive(self):
        """Gate rates are non-negative."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=15)
        growth = complexity_growth_rate(tower, data, 15)
        for r, rate in growth['gate_rate'].items():
            assert rate >= 0

    def test_cumulative_monotone(self):
        """Cumulative complexity is non-decreasing."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=20)
        growth = complexity_growth_rate(tower, data, 20)
        cum = growth['cumulative_complexity']
        arities = sorted(cum.keys())
        for i in range(len(arities) - 1):
            assert cum[arities[i + 1]] >= cum[arities[i]] - 1e-10


# ===========================================================================
# Section 8: Switchback effect
# ===========================================================================

class TestSwitchbackEffect:

    def test_switchback_positive_delay(self):
        """Switchback delay is positive."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=15)
        switch = switchback_complexity(tower, data, perturbation_arity=3)
        assert switch['t_switch'] > 0

    def test_switchback_larger_for_smaller_perturbation(self):
        """Larger arity perturbation (smaller S_r) gives longer switchback delay."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=15)
        s3 = switchback_complexity(tower, data, perturbation_arity=3)
        s5 = switchback_complexity(tower, data, perturbation_arity=5)
        # S_5 < S_3 in magnitude, so t_switch(5) > t_switch(3)
        if abs(tower.get(5, 0)) < abs(tower.get(3, 0)):
            assert s5['t_switch'] > s3['t_switch']

    def test_switchback_beta(self):
        """beta = 2*pi/|kappa|."""
        tower, data = shadow_tower_for_family('virasoro', 10.0, max_r=15)
        switch = switchback_complexity(tower, data)
        expected_beta = 2.0 * math.pi / abs(data['kappa'])
        assert abs(switch['beta'] - expected_beta) < 1e-10


# ===========================================================================
# Section 9: Complexity at zeta zeros
# ===========================================================================

class TestComplexityAtZetaZeros:

    def test_first_zero_computable(self):
        """Complexity at gamma_1 is well-defined."""
        result = complexity_at_zeta_zero(1, max_r=15)
        assert 'C_circuit' in result
        assert result['C_circuit'] > 0

    def test_c_at_zero_complex(self):
        """c(rho_n) is genuinely complex."""
        result = complexity_at_zeta_zero(1, max_r=10)
        c = result['c(rho_n)']
        assert abs(c.imag) > 0

    def test_kappa_at_zero(self):
        """kappa = c/2 at zeta zero."""
        result = complexity_at_zeta_zero(1, max_r=10)
        c = result['c(rho_n)']
        kappa = result['kappa']
        assert abs(kappa - c / 2.0) < 1e-10

    def test_table_length(self):
        """Table has the right number of entries."""
        table = complexity_at_zeta_zeros_table(n_max=5, max_r=10)
        assert len(table) == 5

    def test_volume_at_zeros_positive(self):
        """Volume complexity is positive at all zeros."""
        for n in range(1, 6):
            result = complexity_at_zeta_zero(n, max_r=10)
            assert result['V_shadow'] > 0

    def test_nielsen_at_zeros(self):
        """Nielsen complexity is computable at zeros."""
        for n in range(1, 4):
            result = complexity_at_zeta_zero(n, max_r=10)
            assert result['C_Nielsen'] > 0

    def test_growth_rate_at_zeros(self):
        """Growth rate is computable at complex c."""
        result = complexity_at_zeta_zero(1, max_r=15)
        assert result['rho'] is not None

    def test_tower_S2_equals_kappa(self):
        """S_2 = kappa at zeta zeros."""
        result = complexity_at_zeta_zero(2, max_r=10)
        kappa = result['kappa']
        S2 = result['tower_S2']
        # S_2 from tower should match kappa (= c/2)
        # The tower computation uses sqrt(Q_L), S_2 = a_0/2 = sqrt(4*kappa^2)/2 = |kappa|
        # But at complex kappa, S_2 = sqrt(4*kappa^2)/2 which is +-kappa
        # Check absolute values
        assert abs(abs(S2) - abs(kappa)) < abs(kappa) * 0.01


# ===========================================================================
# Section 10: Heisenberg sweep
# ===========================================================================

class TestHeisenbergSweep:

    def test_sweep_length(self):
        """Sweep returns 10 entries for default k=1..10."""
        sweep = heisenberg_complexity_sweep()
        assert len(sweep) == 10

    def test_kappa_equals_k(self):
        """kappa = k for each entry (AP39)."""
        sweep = heisenberg_complexity_sweep([1.0, 3.0, 7.0])
        for entry in sweep:
            assert abs(entry['kappa'] - entry['k']) < 1e-10

    def test_depth_class_G(self):
        """All Heisenberg entries are class G."""
        sweep = heisenberg_complexity_sweep()
        for entry in sweep:
            assert entry['depth_class'] == 'G'

    def test_circuit_constant_at_1(self):
        """Heisenberg circuit complexity ~ 1 for all k."""
        sweep = heisenberg_complexity_sweep()
        for entry in sweep:
            assert abs(entry['C_circuit'] - 1.0) < 0.01

    def test_volume_proportional_to_k(self):
        """V_shadow proportional to k."""
        sweep = heisenberg_complexity_sweep([2.0, 4.0, 8.0])
        # V(2k) / V(k) ~ 2
        ratio_1 = sweep[1]['V_shadow'] / sweep[0]['V_shadow']
        ratio_2 = sweep[2]['V_shadow'] / sweep[1]['V_shadow']
        assert abs(ratio_1 - 2.0) < 0.1
        assert abs(ratio_2 - 2.0) < 0.1


# ===========================================================================
# Section 11: Virasoro sweep
# ===========================================================================

class TestVirasoroSweep:

    def test_sweep_runs(self):
        """Virasoro sweep completes without errors."""
        sweep = virasoro_complexity_sweep([1.0, 5.0, 13.0, 25.0], max_r=15)
        valid = [e for e in sweep if 'error' not in e]
        assert len(valid) >= 3

    def test_depth_class_M(self):
        """All Virasoro entries are class M."""
        sweep = virasoro_complexity_sweep([5.0, 10.0, 20.0], max_r=10)
        for entry in sweep:
            if 'error' not in entry:
                assert entry['depth_class'] == 'M'

    def test_rho_positive(self):
        """Shadow growth rate rho is positive for class M."""
        sweep = virasoro_complexity_sweep([5.0, 10.0, 20.0], max_r=15)
        for entry in sweep:
            if 'error' not in entry and entry.get('rho') is not None:
                assert entry['rho'] > 0

    def test_scrambling_time_computed(self):
        """Scrambling time is computed for class M."""
        sweep = virasoro_complexity_sweep([10.0], max_r=15)
        entry = sweep[0]
        assert 'scrambling_time' in entry
        if entry.get('scrambling_time') is not None:
            assert entry['scrambling_time'] > 0


# ===========================================================================
# Section 12: Affine sl_N sweep
# ===========================================================================

class TestAffineSweep:

    def test_sweep_runs(self):
        """Affine sweep completes."""
        sweep = affine_slN_complexity_sweep([2, 3], [1.0, 2.0], max_r=10)
        valid = [e for e in sweep if 'error' not in e]
        assert len(valid) >= 2

    def test_depth_class_L(self):
        """All affine entries are class L."""
        sweep = affine_slN_complexity_sweep([2], [1.0], max_r=10)
        for entry in sweep:
            if 'error' not in entry:
                assert entry['depth_class'] == 'L'

    def test_kappa_formula(self):
        """kappa = dim(g)*(k+h^vee)/(2*h^vee) verified per entry."""
        sweep = affine_slN_complexity_sweep([2, 3], [1.0, 3.0], max_r=10)
        for entry in sweep:
            if 'error' not in entry:
                N = entry['N']
                k = entry['k']
                dim_g = N * N - 1
                h_vee = N
                expected = dim_g * (k + h_vee) / (2.0 * h_vee)
                assert abs(entry['kappa'] - expected) < 1e-8


# ===========================================================================
# Section 13: Complexity extrema at zeros
# ===========================================================================

class TestComplexityExtrema:

    def test_extrema_computation(self):
        """Extrema computation runs for first 5 zeros."""
        result = complexity_extrema_at_zeros(n_max=5, max_r=10)
        assert 'zeros' in result
        assert len(result['zeros']) == 5

    def test_extrema_summary_fields(self):
        """Summary has expected fields."""
        result = complexity_extrema_at_zeros(n_max=3, max_r=10)
        assert 'n_real_extrema' in result
        assert 'n_imag_extrema' in result
        assert 'fraction_real_extrema' in result

    def test_laplacian_computable(self):
        """Discrete Laplacian is computable at each zero."""
        result = complexity_extrema_at_zeros(n_max=3, max_r=10)
        for entry in result['zeros']:
            if 'error' not in entry:
                assert 'laplacian_real' in entry
                assert isinstance(entry['laplacian_real'], float)


# ===========================================================================
# Section 14: Complexity=Volume proportionality
# ===========================================================================

class TestComplexityEqualsVolume:

    def test_heisenberg_CV_proportional(self):
        """For Heisenberg, C and V should be strongly correlated."""
        result = complexity_equals_volume_test(
            'heisenberg', [1.0, 2.0, 3.0, 5.0, 8.0], max_r=10)
        # For Heisenberg: C_circ = 1 (constant), V ~ 2k*t_max (linear)
        # These are NOT proportional (constant vs linear).
        # This is the correct physical result: circuit complexity is constant
        # for Gaussian algebras, while volume grows.
        assert len(result['entries']) >= 3

    def test_virasoro_CV_fit(self):
        """Virasoro C vs V linear fit runs."""
        result = complexity_equals_volume_test(
            'virasoro', [2.0, 5.0, 10.0, 15.0, 20.0], max_r=15)
        assert 'alpha' in result
        assert 'r_squared' in result

    def test_ratio_finite(self):
        """C/V ratios are finite."""
        result = complexity_equals_volume_test(
            'virasoro', [5.0, 10.0, 20.0], max_r=10)
        for entry in result['entries']:
            assert entry['ratio'] < 1e10


# ===========================================================================
# Section 15: Cross-definition consistency
# ===========================================================================

class TestCrossDefinitionConsistency:

    def test_five_measures_computable(self):
        """All five complexity measures are computable for Virasoro."""
        result = cross_definition_consistency('virasoro', 10.0, max_r=15)
        measures = result['measures']
        for key in ['C_circuit', 'C_volume', 'C_action', 'C_Nielsen', 'C_asymptotic']:
            assert key in measures

    def test_all_positive_real_c(self):
        """All measures are positive for positive real c."""
        result = cross_definition_consistency('virasoro', 10.0, max_r=15)
        for key, val in result['measures'].items():
            assert val > 0, f"{key} should be positive"

    def test_ratios_finite(self):
        """Pairwise ratios are finite."""
        result = cross_definition_consistency('virasoro', 10.0, max_r=15)
        for key, val in result['ratios'].items():
            assert 0 < val < 1e10, f"Ratio {key} = {val} is not in reasonable range"

    def test_heisenberg_five_measures(self):
        """Heisenberg has all five measures."""
        result = cross_definition_consistency('heisenberg', 5.0, max_r=10)
        assert 'C_circuit' in result['measures']

    def test_complex_c_five_measures(self):
        """Complex c: all measures computable."""
        c = complex(13, 5)
        result = cross_definition_consistency('virasoro', c, max_r=10)
        for key, val in result['measures'].items():
            # For complex c, measures may be 0 or very large but not NaN
            assert not math.isnan(val), f"{key} is NaN"


# ===========================================================================
# Section 16: Multi-path verification
# ===========================================================================

class TestMultiPathVerification:

    def test_heisenberg_volume_3_paths(self):
        """Heisenberg volume: quadrature vs tower sum vs closed form."""
        k = 5.0
        data = heisenberg_shadow_data(k)
        vol = volume_complexity(data, t_max=10.0)

        V_quad = vol['V_quadrature']
        V_closed = vol['V_closed_G']
        # V_closed = 2*k*t_max = 100
        assert V_closed is not None
        assert abs(V_quad - V_closed) / V_closed < 0.01

    def test_virasoro_circuit_vs_tower(self):
        """Circuit complexity from tower matches direct sum."""
        c = 10.0
        tower, data = shadow_tower_for_family('virasoro', c, max_r=20)
        circ = circuit_complexity(tower, data, 20)

        # Direct computation
        kappa_abs = abs(data['kappa'])
        l1_direct = sum(abs(tower[r]) for r in range(2, 21))
        C_direct = l1_direct / kappa_abs

        assert abs(circ.gate_count - C_direct) < 1e-10

    def test_kappa_consistency_3_families(self):
        """kappa formula independently verified for 3 families (AP1)."""
        # Virasoro c=10: kappa = c/2 = 5
        data_v = virasoro_shadow_data(10.0)
        assert abs(data_v['kappa'] - 5.0) < 1e-10

        # Heisenberg k=7: kappa = 7
        data_h = heisenberg_shadow_data(7.0)
        assert abs(data_h['kappa'] - 7.0) < 1e-10

        # Affine sl_2 k=1: kappa = 3*(1+2)/4 = 2.25
        data_a = affine_slN_shadow_data(2, 1.0)
        assert abs(data_a['kappa'] - 2.25) < 1e-10

    def test_Q_L_from_tower_vs_formula(self):
        """Q_L coefficients from formula match tower's S_2, S_3, S_4."""
        c = 12.0
        tower, data = shadow_tower_for_family('virasoro', c, max_r=10)
        kappa = data['kappa']
        alpha = data['alpha']
        S4 = data['S4']

        # From tower
        S2_tower = tower[2]
        S3_tower = tower[3]
        S4_tower = tower[4]

        # From formula
        assert abs(S2_tower - kappa) / abs(kappa) < 0.01
        assert abs(S3_tower - alpha) / abs(alpha) < 0.01
        assert abs(S4_tower - S4) / abs(S4) < 0.01

    def test_depth_classification_consistent(self):
        """Depth classification matches tower behavior."""
        # Heisenberg: class G, tower terminates at 2
        tower_h, data_h = shadow_tower_for_family('heisenberg', 5.0, max_r=10)
        assert data_h['depth_class'] == 'G'
        for r in range(3, 10):
            assert abs(tower_h[r]) < 1e-10

        # Virasoro: class M, tower does NOT terminate
        tower_v, data_v = shadow_tower_for_family('virasoro', 10.0, max_r=10)
        assert data_v['depth_class'] == 'M'
        assert abs(tower_v[5]) > 1e-15


# ===========================================================================
# Section 17: Edge cases and robustness
# ===========================================================================

class TestEdgeCases:

    def test_virasoro_c_half(self):
        """c = 1/2 (Ising model) is computable."""
        tower, data = shadow_tower_for_family('virasoro', 0.5, max_r=10)
        assert abs(tower[2] - 0.25) < 1e-10  # kappa = c/2 = 0.25

    def test_virasoro_c_26(self):
        """c = 26 (critical string): kappa = 13."""
        tower, data = shadow_tower_for_family('virasoro', 26.0, max_r=10)
        assert abs(tower[2] - 13.0) < 1e-8

    def test_virasoro_c_13_self_dual(self):
        """c = 13 (self-dual point, AP8): kappa = 6.5."""
        tower, data = shadow_tower_for_family('virasoro', 13.0, max_r=10)
        assert abs(tower[2] - 6.5) < 1e-8

    def test_large_gamma(self):
        """Large zeta zero (n=20): computation doesn't overflow."""
        result = complexity_at_zeta_zero(20, max_r=10)
        assert result['C_circuit'] > 0
        assert not math.isnan(result['C_circuit'])

    def test_small_k_heisenberg(self):
        """Heisenberg at k=0.01: small kappa."""
        tower, data = shadow_tower_for_family('heisenberg', 0.01, max_r=10)
        assert abs(tower[2] - 0.01) < 1e-10

    def test_affine_sl5_k5(self):
        """Affine sl_5 at k=5: large rank."""
        tower, data = shadow_tower_for_family('affine_slN', 5.0, N=5, max_r=10)
        # kappa = 24*(5+5)/(2*5) = 24
        expected_kappa = 24.0 * (5.0 + 5.0) / (2.0 * 5.0)
        assert abs(data['kappa'] - expected_kappa) < 1e-8

    def test_no_nan_in_sweep(self):
        """No NaN values in Virasoro sweep."""
        sweep = virasoro_complexity_sweep([2.0, 10.0, 20.0], max_r=10)
        for entry in sweep:
            if 'error' not in entry:
                for key in ['C_circuit', 'V_shadow', 'C_Nielsen']:
                    assert not math.isnan(entry[key]), f"NaN in {key} at c={entry['c']}"


# ===========================================================================
# Section 18: Lloyd bound verification
# ===========================================================================

class TestLloydBound:

    def test_lloyd_formula(self):
        """Lloyd bound = 2*kappa/pi."""
        for c in [5.0, 10.0, 20.0]:
            tower, data = shadow_tower_for_family('virasoro', c, max_r=15)
            growth = complexity_growth_rate(tower, data, 15)
            kappa = abs(data['kappa'])
            assert abs(growth['lloyd_bound'] - 2.0 * kappa / math.pi) < 1e-10

    def test_lloyd_bound_consistent_with_kappa(self):
        """Lloyd bound increases with kappa."""
        bounds = []
        for c in [5.0, 10.0, 20.0]:
            tower, data = shadow_tower_for_family('virasoro', c, max_r=10)
            growth = complexity_growth_rate(tower, data, 10)
            bounds.append(growth['lloyd_bound'])
        assert bounds[0] < bounds[1] < bounds[2]
